"""
orbit_data_manager.py - Advanced orbit data caching and management

This module handles the efficient storage and retrieval of orbital path data,
using an incremental approach to minimize API calls and processing time.
"""

import json
import os
import shutil  # Add this - needed for file operations
from datetime import datetime, timedelta
import numpy as np
from typing import Dict, List, Optional, Any, Tuple, Union
import traceback

from astroquery.jplhorizons import Horizons
from astropy.time import Time
import plotly.graph_objs as go

        # Track which orbits we've already shown conversion messages for
_conversion_messages_shown = set()

# Global variables
orbit_paths_over_time = {}
refresh_all = False
status_display = None  # Will be set from the main module
root = None  # Will be set from the main module
center_object_var = None  # Will be set from the main module
_startup_complete = False  # Add this line

# Constants
ORBIT_PATHS_FILE = "orbit_paths.json"
DEFAULT_DAYS_AHEAD = 730  # Default to looking 2 years ahead
MAX_DATA_AGE_DAYS = 90  # Maximum age for data before pruning (optional)

# Add at module level:
last_center_updated = None
last_update_time = None

def repair_cache_on_load():
    """Load cache and remove only corrupted entries"""
    if not os.path.exists('orbit_paths.json'):
        return {}
    
    try:
        with open('orbit_paths.json', 'r') as f:
            cache_data = json.load(f)
        
        # Track what we remove
        removed_entries = []
        cleaned_cache = {}
        
        for orbit_key, orbit_data in cache_data.items():
            try:
                # Validate this entry
                if isinstance(orbit_data, dict) and (
                    'data_points' in orbit_data or  # New format
                    ('x' in orbit_data and 'y' in orbit_data and 'z' in orbit_data)  # Old format
                ):
                    # Entry looks good, keep it
                    cleaned_cache[orbit_key] = orbit_data
                else:
                    removed_entries.append(orbit_key)
            except Exception:
                # Any error processing this entry = corrupted
                removed_entries.append(orbit_key)
        
        if removed_entries:
            print(f"[CACHE REPAIR] Removed {len(removed_entries)} corrupted entries: {removed_entries}")
            print(f"[CACHE REPAIR] Kept {len(cleaned_cache)} valid entries")
            
            # Save the cleaned cache back
            with open('orbit_paths.json', 'w') as f:
                json.dump(cleaned_cache, f)
        
        return cleaned_cache
        
    except json.JSONDecodeError:
        # Entire file is corrupted
        print("[CACHE ERROR] Entire cache file corrupted, starting fresh")
        return {}

def initialize(status_widget=None, root_widget=None, center_var=None, data_file=ORBIT_PATHS_FILE):
    """
    Initialize the orbit data manager by loading cached data.
    
    Parameters:
        status_widget: UI widget for displaying status messages
        root_widget: Root Tkinter widget for UI updates
        center_var: Tkinter variable controlling center object selection
        data_file: Path to the orbit data cache file
    
    Returns:
        dict: The loaded orbit paths data
    """
    global orbit_paths_over_time, status_display, root, center_object_var
    
    status_display = status_widget
    root = root_widget
    center_object_var = center_var
    orbit_paths_over_time = load_orbit_paths(data_file)
    return orbit_paths_over_time

def load_orbit_paths(file_path=ORBIT_PATHS_FILE):
    """
    Load orbit paths from file with automatic repair of corrupted entries.
    
    Parameters:
        file_path: Path to the orbit paths data file
        
    Returns:
        dict: The loaded orbit paths data, with corrupted entries removed
    """
    global status_display
    
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
            
        if not isinstance(data, dict):
            error_msg = "[CACHE ERROR] Cache file has invalid structure, starting fresh"
            print(error_msg)
            update_status(error_msg)
            return {}
            
        # Validate and clean the data
        cleaned_data = {}
        removed_entries = []
        total_entries = len(data)
        
        for orbit_key, orbit_data in data.items():
            try:
                # Basic validation
                if not isinstance(orbit_data, dict):
                    removed_entries.append((orbit_key, "Not a dictionary"))
                    continue
                
                # Check for new format (time-indexed with data_points)
                if "data_points" in orbit_data:
                    if not isinstance(orbit_data["data_points"], dict):
                        removed_entries.append((orbit_key, "Invalid data_points structure"))
                        continue
                    
                    # Validate at least one data point
                    if orbit_data["data_points"]:
                        sample_key = next(iter(orbit_data["data_points"]))
                        sample_point = orbit_data["data_points"][sample_key]
                        
                        if not isinstance(sample_point, dict) or \
                           not all(k in sample_point for k in ['x', 'y', 'z']):
                            removed_entries.append((orbit_key, "Invalid data point structure"))
                            continue
                    
                    # Valid new format
                    cleaned_data[orbit_key] = orbit_data
                    
                # Check for old format (arrays)
                elif all(k in orbit_data for k in ['x', 'y', 'z']):
                    # Validate arrays
                    if not all(isinstance(orbit_data[k], list) for k in ['x', 'y', 'z']):
                        removed_entries.append((orbit_key, "Invalid coordinate arrays"))
                        continue
                        
                    # Check lengths match
                    x_len = len(orbit_data['x'])
                    y_len = len(orbit_data['y'])
                    z_len = len(orbit_data['z'])
                    
                    if x_len != y_len or y_len != z_len:
                        removed_entries.append((orbit_key, f"Mismatched array lengths: x={x_len}, y={y_len}, z={z_len}"))
                        continue
                        
                    if x_len == 0:
                        removed_entries.append((orbit_key, "Empty coordinate arrays"))
                        continue
                    
                    if orbit_key not in _conversion_messages_shown and _startup_complete:
                        print(f"Converting old format data for {orbit_key}")
                        _conversion_messages_shown.add(orbit_key)

                    converted = convert_single_orbit_to_new_format(orbit_key, orbit_data)
                    if converted:
                        cleaned_data[orbit_key] = converted
                    else:
                        removed_entries.append((orbit_key, "Failed to convert old format"))
                        
                else:
                    removed_entries.append((orbit_key, "Missing required data fields"))
                    
            except Exception as e:
                removed_entries.append((orbit_key, f"Validation error: {str(e)}"))
        
        # Report what was cleaned
        if removed_entries:
            # Console output
            print(f"\n[CACHE REPAIR] Removed {len(removed_entries)} corrupted entries out of {total_entries}:")
            for entry, reason in removed_entries[:5]:
                print(f"  - {entry}: {reason}")
            if len(removed_entries) > 5:
                print(f"  ... and {len(removed_entries) - 5} more")
            print(f"[CACHE REPAIR] Keeping {len(cleaned_data)} valid entries")
            
            # Status display output
            status_msg = f"Cache repaired: removed {len(removed_entries)} corrupted entries, kept {len(cleaned_data)} valid"
            update_status(status_msg)
            
            # Save cleaned data back to file
            save_orbit_paths(cleaned_data, file_path)
        else:
            # Report success
            if total_entries > 0:
                status_msg = f"Cache loaded successfully: {total_entries} valid entries"
                update_status(status_msg)
        
        return cleaned_data
            
    except FileNotFoundError:
        msg = f"No existing orbit paths file found at {file_path}, creating new cache."
        print(msg)
        update_status("Starting with fresh cache (no existing file found)")
        return {}
        
    except json.JSONDecodeError as e:
        error_msg = f"[CACHE ERROR] Cache file is corrupted: {e}"
        print(error_msg)
        update_status("Cache file corrupted - starting fresh")
        
        # Rename corrupted file instead of deleting
        backup_name = file_path + '.corrupted.' + datetime.now().strftime('%Y%m%d_%H%M%S')
        try:
            import shutil
            shutil.move(file_path, backup_name)
            backup_msg = f"[CACHE BACKUP] Corrupted file saved as: {backup_name}"
            print(backup_msg)
            update_status(f"Corrupted cache backed up, starting fresh")
        except Exception as backup_error:
            print(f"[CACHE BACKUP] Could not backup corrupted file: {backup_error}")
            
        return {}
        
    except Exception as e:
        error_msg = f"Error loading orbit paths: {e}"
        print(error_msg)
        update_status("Error loading cache - check console for details")
        traceback.print_exc()
        return {}

def convert_single_orbit_to_new_format(orbit_key, orbit_data):
    """
    Convert a single orbit from old format to new format.
    
    Parameters:
        orbit_key: The key for this orbit (e.g., "Mars_Sun")
        orbit_data: The old format data with x, y, z arrays
        
    Returns:
        dict: Converted data in new format or None if conversion fails
    """

    global _conversion_messages_shown
    
    if orbit_key not in _conversion_messages_shown:
        print(f"Converting old format data for {orbit_key}")
        _conversion_messages_shown.add(orbit_key)
    
    try:
        # Extract object and center names
        if "_" in orbit_key:
            obj_name, center_name = orbit_key.split("_", 1)
        else:
            obj_name, center_name = orbit_key, "Sun"
        
        # Get coordinate arrays
        x_coords = orbit_data['x']
        y_coords = orbit_data['y']
        z_coords = orbit_data['z']
        
        num_points = len(x_coords)
        if num_points == 0:
            return None
            
        # Generate synthetic dates
        today = datetime.today()
        days_span = DEFAULT_DAYS_AHEAD
        days_between = days_span / (num_points - 1) if num_points > 1 else 1
        
        data_points = {}
        for i in range(num_points):
            point_date = today - timedelta(days=days_span/2) + timedelta(days=i * days_between)
            date_str = point_date.strftime("%Y-%m-%d")
            
            data_points[date_str] = {
                "x": x_coords[i],
                "y": y_coords[i],
                "z": z_coords[i]
            }
        
        return {
            "data_points": data_points,
            "metadata": {
                "start_date": (today - timedelta(days=days_span/2)).strftime("%Y-%m-%d"),
                "end_date": (today + timedelta(days=days_span/2)).strftime("%Y-%m-%d"),
                "center_body": center_name,
                "last_updated": today.strftime("%Y-%m-%d"),
                "converted_from_old_format": True
            }
        }
        
    except Exception as e:
        print(f"Error converting orbit {orbit_key}: {e}")
        return None

# Replace the save_orbit_paths function in orbit_data_manager.py with this safer version

def save_orbit_paths(data=None, file_path=ORBIT_PATHS_FILE):
    """
    Save orbit paths data to file with safety checks.
    
    Parameters:
        data: Orbit paths data to save (defaults to global orbit_paths_over_time)
        file_path: Path to save the data to
    """
    global orbit_paths_over_time
    
    if data is None:
        data = orbit_paths_over_time
    
    # Safety check: Don't save empty or tiny data over existing large file
    if os.path.exists(file_path):
        try:
            current_size = os.path.getsize(file_path)
            # Serialize data to check its size
            data_str = json.dumps(data)
            new_size = len(data_str)
            
            # If current file is > 1MB and new data is < 1KB, something's wrong
            if current_size > 1_000_000 and new_size < 1000:
                print(f"[SAFETY] Refusing to overwrite large file ({current_size:,} bytes) with small data ({new_size:,} bytes)")
                print(f"[SAFETY] Data has only {len(data)} entries")
                
                # Create an emergency backup
                emergency_backup = file_path + '.emergency.' + datetime.now().strftime('%Y%m%d_%H%M%S')
                shutil.copy2(file_path, emergency_backup)
                print(f"[SAFETY] Created emergency backup: {emergency_backup}")
                
                # Still refuse to save
                raise ValueError("Safety check failed: Attempting to save suspiciously small data over large file")
        except (OSError, IOError) as e:
            print(f"[WARNING] Could not check file size: {e}")
    
    # Create a temporary file first
    temp_file = file_path + '.tmp'
    backup_file = file_path + '.backup'
    
    try:
        # Write to temporary file
        with open(temp_file, 'w') as f:
            json.dump(data, f)
        
        # Verify the temp file was written correctly
        with open(temp_file, 'r') as f:
            json.load(f)  # This will raise an exception if JSON is invalid
        
        # If original exists, create backup
        if os.path.exists(file_path):
            if os.path.exists(backup_file):
                os.remove(backup_file)
            shutil.move(file_path, backup_file)
        
        # Move temp file to final location
        shutil.move(temp_file, file_path)
        
        print(f"Orbit paths saved to {file_path}")
        
        # Clean up old backup if save was successful and new file is reasonable size
        if os.path.exists(backup_file) and os.path.getsize(file_path) > 100:
            os.remove(backup_file)
            
    except Exception as e:
        print(f"Error saving orbit paths: {e}")
        
        # Try to restore from backup
        if os.path.exists(backup_file):
            try:
                shutil.copy2(backup_file, file_path)
                print(f"[RECOVERY] Restored from backup after save failure")
            except Exception as restore_error:
                print(f"[CRITICAL] Could not restore backup: {restore_error}")
        
        # Clean up temp file if it exists
        if os.path.exists(temp_file):
            try:
                os.remove(temp_file)
            except:
                pass
                
        traceback.print_exc()
        raise  # Re-raise the exception

def convert_to_new_format(old_data):
    """
    Convert old format orbit data to new time-indexed format.
    
    Parameters:
        old_data: Dictionary containing orbit data in old format
        
    Returns:
        dict: Converted data in new time-indexed format
    """
    new_data = {}
    today = datetime.today()
    today_str = today.strftime("%Y-%m-%d")
    
    print("Converting orbit data to new time-indexed format...")
    
    for key, coords in old_data.items():
        # Skip entries that don't have coordinate data
        if not isinstance(coords, dict) or "x" not in coords:
            continue
            
        # Extract object and center names from key
        if "_" in key:
            obj_name, center_name = key.split("_", 1)
        else:
            obj_name, center_name = key, "Sun"  # Default for backward compatibility
            
        # Create synthetic dates for the points (estimate)
        num_points = len(coords.get("x", []))
        if num_points > 0:
            # Assume points cover a 2-year period
            days_between = DEFAULT_DAYS_AHEAD / (num_points - 1) if num_points > 1 else 1
            
            data_points = {}
            for i in range(num_points):
                point_date = today - timedelta(days=1) + timedelta(days=i * days_between)
                date_str = point_date.strftime("%Y-%m-%d")
                
                # Only add the point if all coordinates are available
                if (i < len(coords.get("x", [])) and 
                    i < len(coords.get("y", [])) and 
                    i < len(coords.get("z", []))):
                    
                    data_points[date_str] = {
                        "x": coords["x"][i],
                        "y": coords["y"][i],
                        "z": coords["z"][i]
                    }
            
            new_data[key] = {
                "data_points": data_points,
                "metadata": {
                    "earliest_date": today.strftime("%Y-%m-%d"),
                    "latest_date": (today + timedelta(days=DEFAULT_DAYS_AHEAD)).strftime("%Y-%m-%d"),
                    "center_body": center_name,
                    "last_updated": today_str,
                    "converted_from_legacy": True
                }
            }
    
    print(f"Converted {len(new_data)} orbit paths to new format.")
    return new_data


def determine_interval_for_object(obj, orbital_params=None, parent_planets=None):
    """
    Determine appropriate time interval for fetching orbit data.
    
    Parameters:
        obj: Object info dictionary
        orbital_params: Dictionary of orbital parameters for known objects
        parent_planets: Dictionary mapping planets to their satellites
        
    Returns:
        str: Time interval string (e.g., "1d", "12h", "6h", "1h")
    """
    # Handle special case for Planet 9
    if obj.get('id') == 'planet9_placeholder':
        return "1d"  # Default interval for Planet 9 (though not actually used)
    
    # Default interval
    interval = "1d"
    
    # Check if this is a comet
    if obj.get('is_comet', False):
        interval = "6h"
    
    # Check if this is a mission
    elif obj.get('is_mission', False):
        interval = "6h"
    
    # Check if this is a satellite of the center object
    elif parent_planets and any(obj['name'] in moons for planet, moons in parent_planets.items()):
        interval = "1h"
    
    # Check for high eccentricity objects
    elif orbital_params and obj['name'] in orbital_params:
        e = orbital_params[obj['name']].get('e', 0)
        if e > 0.5:  # High eccentricity
            interval = "12h"
    
    return interval


def fetch_orbit_path(obj_info, start_date, end_date, interval, center_id='@0', id_type=None):
    """
    Fetch orbit path data from JPL Horizons.
    
    Parameters:
        obj_info: Object information dictionary
        start_date: Start date for the orbit path
        end_date: End date for the orbit path
        interval: Time interval (e.g., "1d", "12h")
        center_id: ID of the central body (default: '@0' for solar system barycenter)
        id_type: Type of ID for the object
        
    Returns:
        dict: Dictionary with keys 'x', 'y', and 'z' or None on failure
    """
    # Handle special case for Planet 9 (calculated instead of fetched)
    if obj_info.get('id') == 'planet9_placeholder':
        return calculate_planet9_orbit(start_date, end_date, interval)
    
    try:
        # Use the object's id and id_type
        object_id = obj_info['id']
        
        # Format the center_id appropriately
        location = center_id
        if not location.startswith('@'):
            location = '@' + location
        
        # Format dates as required by Horizons
        epochs = {
            'start': start_date.strftime('%Y-%m-%d'),
            'stop': end_date.strftime('%Y-%m-%d'),
            'step': interval  # e.g. "1d" for one day, "12h" for 12 hours
        }

        # Create Horizons object and fetch vectors        
        obj = Horizons(id=object_id, id_type=id_type, location=location, epochs=epochs)
        eph = obj.vectors()
        
        # Process the ephemerides table to extract x, y, z coordinates
        x_coords = list(eph['x'])
        y_coords = list(eph['y'])
        z_coords = list(eph['z'])
        
        return {'x': x_coords, 'y': y_coords, 'z': z_coords}
    except Exception as e:
        print(f"Error fetching orbit path for {obj_info['name']}: {e}")
        traceback.print_exc()
        return None


def calculate_planet9_orbit(start_date, end_date, interval):
    """
    Calculate synthetic orbit for hypothetical Planet 9.
    
    Parameters:
        start_date: Start date for the orbit
        end_date: End date for the orbit
        interval: Time interval
        
    Returns:
        dict: Synthetic orbit data
    """
    # Calculate days between start and end
    days_total = (end_date - start_date).days
    
    # Determine number of points based on interval
    if interval == "1d":
        num_points = days_total + 1
    elif interval == "12h":
        num_points = days_total * 2 + 1
    elif interval == "6h":
        num_points = days_total * 4 + 1
    elif interval == "1h":
        num_points = days_total * 24 + 1
    else:
        # Default to daily
        num_points = days_total + 1
    
    # Planet 9 orbital parameters (hypothetical)
    a = 600  # Semi-major axis (AU)
    e = 0.30  # Eccentricity
    i = 6     # Inclination (degrees)
    Omega = 90  # Longitude of ascending node (degrees)
    omega = 150  # Argument of perihelion (degrees)
    
    # Period in years (Kepler's third law)
    P = np.sqrt(a**3)  # Period in years
    P_days = P * 365.25  # Period in days
    
    # Create time points
    t = np.linspace(0, days_total, num_points)
    
    # Calculate mean anomaly at each time
    M = 360 * t / P_days
    
    # Solve Kepler's equation to get eccentric anomaly (simplified)
    # For a proper implementation, this would be an iterative solution
    E = M + e * np.sin(np.radians(M))
    
    # Calculate true anomaly
    theta = 2 * np.arctan2(np.sqrt(1 + e) * np.sin(np.radians(E/2)), 
                           np.sqrt(1 - e) * np.cos(np.radians(E/2)))
    theta = np.degrees(theta)
    
    # Calculate distance from Sun
    r = a * (1 - e**2) / (1 + e * np.cos(np.radians(theta)))
    
    # Calculate position in orbital plane
    xp = r * np.cos(np.radians(theta))
    yp = r * np.sin(np.radians(theta))
    zp = np.zeros_like(xp)
    
    # Rotate to account for orbital orientation
    # Convert angles to radians
    i_rad = np.radians(i)
    omega_rad = np.radians(omega)
    Omega_rad = np.radians(Omega)
    
    # Initialize result arrays
    x = np.zeros_like(xp)
    y = np.zeros_like(yp)
    z = np.zeros_like(zp)
    
    # Perform rotations for each point
    for j in range(len(xp)):
        # Rotate by argument of perihelion
        x1 = xp[j] * np.cos(omega_rad) - yp[j] * np.sin(omega_rad)
        y1 = xp[j] * np.sin(omega_rad) + yp[j] * np.cos(omega_rad)
        
        # Rotate by inclination
        x2 = x1
        y2 = y1 * np.cos(i_rad)
        z2 = y1 * np.sin(i_rad)
        
        # Rotate by longitude of ascending node
        x[j] = x2 * np.cos(Omega_rad) - y2 * np.sin(Omega_rad)
        y[j] = x2 * np.sin(Omega_rad) + y2 * np.cos(Omega_rad)
        z[j] = z2
    
    return {'x': x.tolist(), 'y': y.tolist(), 'z': z.tolist()}


def calculate_planet9_position(theta_offset=75):
    """
    Calculate a fixed position for Planet 9 based on our best estimate.
    This function returns a single position rather than a full orbit.
    
    Parameters:
        theta_offset: Angle offset in degrees to position Planet 9 along its orbit
        
    Returns:
        tuple: (x, y, z, range_value) position and distance
    """
    # Planet 9 orbital parameters
    a = 600  # Semi-major axis (AU)
    e = 0.30  # Eccentricity
    i = 6     # Inclination (degrees)
    Omega = 90  # Longitude of ascending node (degrees)
    omega = 150  # Argument of perihelion (degrees)
    theta = theta_offset  # True anomaly - where along the orbit the planet is positioned
    
    # Convert angles to radians
    i_rad = np.radians(i)
    omega_rad = np.radians(omega)
    Omega_rad = np.radians(Omega)
    theta_rad = np.radians(theta)
    
    # Calculate distance from Sun at this point in the orbit
    r = a * (1 - e**2) / (1 + e * np.cos(theta_rad))
    
    # Calculate position in orbital plane
    x_orbit = r * np.cos(theta_rad)
    y_orbit = r * np.sin(theta_rad)
    
    # Rotate to account for orientation of orbit in 3D space
    # First, rotate by argument of perihelion
    x_perihelion = x_orbit * np.cos(omega_rad) - y_orbit * np.sin(omega_rad)
    y_perihelion = x_orbit * np.sin(omega_rad) + y_orbit * np.cos(omega_rad)
    
    # Then, rotate to account for inclination
    x_inclined = x_perihelion
    y_inclined = y_perihelion * np.cos(i_rad)
    z_inclined = y_perihelion * np.sin(i_rad)
    
    # Finally, rotate by longitude of ascending node
    x = x_inclined * np.cos(Omega_rad) - y_inclined * np.sin(Omega_rad)
    y = x_inclined * np.sin(Omega_rad) + y_inclined * np.cos(Omega_rad)
    z = z_inclined
    
    # Calculate range (distance from Sun)
    range_val = np.sqrt(x**2 + y**2 + z**2)
    
    return x, y, z, range_val

def update_status(message):
    """
    Update status display if available and print to console.
    
    Parameters:
        message: Status message to display
    """
    # Always print to console for logging
    print(message)
    
    # Update status display if available
    global status_display, root
    if status_display:
        try:
            # Check if widget still exists before updating
            if root and root.winfo_exists() and status_display.winfo_exists():
                status_display.config(text=message)
                root.update_idletasks()  # Use update_idletasks instead of update
        except Exception as e:
            # Just print the error, don't try to update the display again
            print(f"Error updating status display: {e}")

def fetch_orbit_path_by_dates(obj_info, start_date, end_date, interval, center_id='@0', id_type=None):
    """
    Fetch orbit path data for specific date range and convert to time-indexed format.
    
    Parameters:
        obj_info: Object information dictionary
        start_date: Start date for the orbit path
        end_date: End date for the orbit path
        interval: Time interval (e.g., "1d", "12h")
        center_id: ID of the central body
        id_type: Type of ID for the object
        
    Returns:
        dict: Orbit data in time-indexed format
    """
    # Special case for Planet 9 - don't fetch from Horizons
    if obj_info.get('id') == 'planet9_placeholder':
        # For Planet 9, we'll create a synthetic orbit
        raw_data = calculate_planet9_orbit(start_date, end_date, interval)
    else:
        update_status(f"Fetching orbit data for {obj_info['name']} from {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}")
        raw_data = fetch_orbit_path(obj_info, start_date, end_date, interval, center_id, id_type)
    
    if not raw_data or 'x' not in raw_data or not raw_data['x']:
        return None
        
    # Convert array format to time-indexed format
    data_points = {}
    
    # Calculate number of days between start and end
    total_days = (end_date - start_date).days
    
    # Assuming points are evenly distributed between start and end dates
    num_points = len(raw_data['x'])
    
    if num_points <= 1:
        return None
        
    days_between = total_days / (num_points - 1)
    
    for i in range(num_points):
        point_date = start_date + timedelta(days=i * days_between)
        date_str = point_date.strftime("%Y-%m-%d")
        
        data_points[date_str] = {
            "x": raw_data['x'][i],
            "y": raw_data['y'][i],
            "z": raw_data['z'][i]
        }
    
    center_name = center_id
    if isinstance(center_id, str):
        center_name = center_id.replace('@', '') if center_id.startswith('@') else center_id
    
    return {
        "data_points": data_points,
        "metadata": {
            "earliest_date": start_date.strftime("%Y-%m-%d"),
            "latest_date": end_date.strftime("%Y-%m-%d"),
            "center_body": center_name,
            "last_updated": datetime.today().strftime("%Y-%m-%d")
        }
    }

def merge_orbit_data(existing_data, new_data, new_start_date, new_end_date):
    """
    Merge new orbit data with existing data.
    """
    if not new_data or "data_points" not in new_data:
        return existing_data
        
    # Create a copy of existing data
    merged_data = {
        "data_points": existing_data.get("data_points", {}).copy(),
        "metadata": existing_data.get("metadata", {}).copy()
    }
    
    # Add new data points
    merged_data["data_points"].update(new_data.get("data_points", {}))
    
    # Update metadata to reflect the actual data range
    all_dates = sorted(merged_data["data_points"].keys())
    if all_dates:
        merged_data["metadata"]["start_date"] = all_dates[0]
        merged_data["metadata"]["end_date"] = all_dates[-1]
        
    merged_data["metadata"]["last_updated"] = datetime.today().strftime("%Y-%m-%d")
    
    return merged_data

def fetch_complete_orbit_path(obj, orbit_key, today, end_window, interval, center_id, center_id_type):
    """
    Fetch and store a complete orbit path for an object.
    
    Parameters:
        obj: Object information dictionary
        orbit_key: Key for storing the orbit data
        today: Start date
        end_window: End date
        interval: Time interval
        center_id: ID of the central body
        center_id_type: Type of ID for the central body
        
    Returns:
        bool: Success status
    """
    global orbit_paths_over_time
    
    # Special case for Planet 9 - don't fetch from Horizons
    if obj.get('id') == 'planet9_placeholder':
        # For Planet 9, we'll create a synthetic orbit and store it
        update_status(f"Calculating synthetic orbit for {obj['name']}")
        path_data = calculate_planet9_orbit(today, end_window, interval)
    else:
        update_status(f"Fetching complete orbit path for {obj['name']} relative to {center_id}")
        path_data = fetch_orbit_path(
            obj, today, end_window, interval,
            center_id=center_id, id_type=obj.get('id_type')
        )
    
    if not path_data:
        return False
        
    # Convert to new format
    orbit_paths_over_time[orbit_key] = {
        "data_points": {},
        "metadata": {
            "earliest_date": today.strftime("%Y-%m-%d"),
            "latest_date": end_window.strftime("%Y-%m-%d"),
            "center_body": center_id_type or center_id,
            "last_updated": today.strftime("%Y-%m-%d")
        }
    }
    
    # Convert array data to time-indexed format
    num_points = len(path_data['x'])
    if num_points > 0:
        days_span = (end_window - today).days
        days_between = days_span / (num_points - 1) if num_points > 1 else 1
        
        for i in range(num_points):
            point_date = today + timedelta(days=i * days_between)
            date_str = point_date.strftime("%Y-%m-%d")
            
            orbit_paths_over_time[orbit_key]["data_points"][date_str] = {
                "x": path_data['x'][i],
                "y": path_data['y'][i],
                "z": path_data['z'][i]
            }
    
    return True


def get_planet9_data(center_object_name='Sun'):
    """
    Get Planet 9 data for different center objects.
    
    Parameters:
        center_object_name: Name of the central body
        
    Returns:
        dict: Planet 9 data in the requested reference frame
    """
    # If the center is Sun, return the standard Planet 9 position
    if center_object_name == 'Sun':
        x, y, z, r = calculate_planet9_position()
        return {
            'x': x,
            'y': y, 
            'z': z,
            'range': r
        }
    
    # For other centers, we need to offset Planet 9 by the position of the center object
    # This is a placeholder for proper implementation that would account for the position
    # of the center body relative to the Sun
    return {
        'x': 0,
        'y': 0,
        'z': 0,
        'range': 0
    }

def update_orbit_paths_incrementally(object_list=None, center_object_name="Sun", 
                                     days_ahead=365, fetch_requests=None,
                                     planetary_params=None, 
                                     parent_planets=None, root_widget=None):
    """
    Update orbit paths incrementally, fetching only missing data.
    
    Parameters:
        object_list: List of objects to update
        center_object_name: Name of central body
        days_ahead: Default days to look ahead (used if fetch_requests is None)
        fetch_requests: List of specific fetch requests with date ranges
        planetary_params: Dictionary of orbital parameters
        parent_planets: Dictionary mapping planets to their satellites
        root_widget: Root Tkinter widget for UI updates
    """
    global orbit_paths_over_time, root
    
    # Update root reference if provided
    if root_widget:
        root = root_widget
    
    today = datetime.today()
    end_window = today + timedelta(days=days_ahead)
    end_window_str = end_window.strftime("%Y-%m-%d")
    
    update_status(f"Checking orbit data for updates to {end_window_str}...")
    
    # Get center object info from the provided object_list
    center_object_info = None
    if object_list:
        center_object_info = next((obj for obj in object_list if obj['name'] == center_object_name), None)
    
    if center_object_info:
        center_id = center_object_info['id']
        center_id_type = center_object_info.get('id_type')
    else:
        center_id = 'Sun'
        center_id_type = None
    
    # If we have specific fetch requests, use those instead of the default behavior
    if fetch_requests:
        updated_count = 0
        time_saved_hours = 0
        
        for request in fetch_requests:
            obj = request['object']
            fetch_start = request['fetch_start']
            fetch_end = request['fetch_end']
            reason = request.get('reason', 'requested')
            
            orbit_key = f"{obj['name']}_{center_object_name}"
            
            # Determine appropriate interval
            interval = determine_interval_for_object(obj, planetary_params, parent_planets)
            
            # Update status
            days_to_fetch = (fetch_end - fetch_start).days + 1
            update_status(f"Fetching {days_to_fetch} days for {obj['name']} ({reason})")
            if root:
                root.update()
            
            # Special handling for Planet 9
            if obj.get('id') == 'planet9_placeholder':
                # Calculate synthetic orbit
                path_data = calculate_planet9_orbit(fetch_start, fetch_end, interval)
                
                # Convert to time-indexed format
                new_data = {
                    "data_points": {},
                    "metadata": {
                        "start_date": fetch_start.strftime("%Y-%m-%d"),
                        "end_date": fetch_end.strftime("%Y-%m-%d"),
                        "center_body": center_object_name,
                        "last_updated": today.strftime("%Y-%m-%d")
                    }
                }
                
                # Convert array data to time-indexed format
                num_points = len(path_data['x'])
                if num_points > 0:
                    days_span = (fetch_end - fetch_start).days
                    days_between = days_span / (num_points - 1) if num_points > 1 else 1
                    
                    for i in range(num_points):
                        point_date = fetch_start + timedelta(days=i * days_between)
                        date_str = point_date.strftime("%Y-%m-%d")
                        
                        new_data["data_points"][date_str] = {
                            "x": path_data['x'][i],
                            "y": path_data['y'][i],
                            "z": path_data['z'][i]
                        }
            else:
                # Fetch the specific date range from JPL Horizons
                new_data = fetch_orbit_path_by_dates(
                    obj, fetch_start, fetch_end, interval,
                    center_id=center_id, id_type=obj.get('id_type')
                )
            
            if new_data:
                # Check if we have existing data to merge with
                if orbit_key in orbit_paths_over_time:
                    # Calculate time saved by not re-fetching existing data
                    existing_data = orbit_paths_over_time[orbit_key]
                    existing_points = len(existing_data.get("data_points", {}))
                    if existing_points > 0:
                        # Estimate based on interval
                        calls_saved = existing_points
                        if interval == "12h":
                            calls_saved /= 2
                        elif interval == "6h":
                            calls_saved /= 4
                        elif interval == "1h":
                            calls_saved /= 24
                        
                        # Each API call might take ~1-2 seconds
                        time_saved_seconds = calls_saved * 1.5
                        time_saved_hours += time_saved_seconds / 3600
                    
                    # Merge with existing data
                    orbit_paths_over_time[orbit_key] = merge_orbit_data(
                        orbit_paths_over_time[orbit_key], new_data,
                        fetch_start, fetch_end
                    )
                else:
                    # New entry
                    orbit_paths_over_time[orbit_key] = new_data
                
                updated_count += 1
        
        # Save the updated data
        save_orbit_paths(orbit_paths_over_time)
        
        update_status(f"Smart fetch complete: Updated {updated_count} orbits with minimal data fetching. "
                     f"Saved approximately {time_saved_hours:.1f} hours of fetch time.")
        
        return updated_count, 0, len(fetch_requests), time_saved_hours
    
    # Otherwise, continue with the existing logic...
    # Default to all objects if none specified
    if not object_list:
        update_status("No object list provided, cannot update orbit paths incrementally.")
        return 0, 0, 0, 0
    
    # Filter object list to exclude center object
    object_list = [obj for obj in object_list if 'id' in obj and obj['name'] != center_object_name]
    
    updated_count = 0
    already_current = 0
    time_saved_hours = 0
    
    for obj in object_list:
        # Special case for Planet 9
        if obj.get('id') == 'planet9_placeholder':
            # Planet 9 is synthetic, doesn't need updating from Horizons
            orbit_key = f"{obj['name']}_{center_object_name}"
            
            # Only create/update Planet 9 data if it doesn't exist yet
            if orbit_key not in orbit_paths_over_time:
                update_status(f"Generating synthetic orbit for {obj['name']}")
                # Use a default interval
                interval = "1d"
                fetch_complete_orbit_path(obj, orbit_key, today, end_window, interval, center_id, center_id_type)
                updated_count += 1
            else:
                already_current += 1
                
            continue
        
        orbit_key = f"{obj['name']}_{center_object_name}"
        
        # Determine appropriate interval based on object type
        interval = determine_interval_for_object(obj, planetary_params, parent_planets)
        
        # Check if we have existing data
        if orbit_key in orbit_paths_over_time:
            metadata = orbit_paths_over_time[orbit_key].get("metadata", {})
            latest_date_str = metadata.get("latest_date")
            
            if latest_date_str:
                latest_date = datetime.strptime(latest_date_str, "%Y-%m-%d")
                
                # Only update if our data doesn't extend to the desired end window
                if latest_date < end_window:
                    # Start fetching from the day after the latest date we have
                    new_start_date = latest_date + timedelta(days=1)
                    new_start_date_str = new_start_date.strftime("%Y-%m-%d")
                    
                    # Estimate time saved by incremental update (vs full refetch)
                    days_already_have = (latest_date - today).days
                    if days_already_have > 0:
                        # Rough estimate based on time interval
                        calls_saved = days_already_have
                        if interval == "12h":
                            calls_saved *= 2
                        elif interval == "6h":
                            calls_saved *= 4
                        elif interval == "1h":
                            calls_saved *= 24
                        
                        # Each API call might take ~1-2 seconds
                        time_saved_seconds = calls_saved * 1.5
                        time_saved_hours += time_saved_seconds / 3600
                    
                    update_status(f"Incrementally updating {obj['name']} from {new_start_date_str} to {end_window_str}")
                    if root:
                        root.update()
                    
                    # Fetch only the missing date range
                    new_data = fetch_orbit_path_by_dates(
                        obj, new_start_date, end_window, interval, 
                        center_id=center_id, id_type=obj.get('id_type')
                    )
                    
                    if new_data:
                        # Merge the new data with existing data
                        orbit_paths_over_time[orbit_key] = merge_orbit_data(
                            orbit_paths_over_time[orbit_key], new_data, 
                            new_start_date, end_window
                        )
                        
                        # Update metadata
                        orbit_paths_over_time[orbit_key]["metadata"]["latest_date"] = end_window_str
                        orbit_paths_over_time[orbit_key]["metadata"]["last_updated"] = today.strftime("%Y-%m-%d")
                        
                        updated_count += 1
                else:
                    already_current += 1
            else:
                # Missing metadata, treat as new entry
                fetch_complete_orbit_path(obj, orbit_key, today, end_window, interval, center_id, center_id_type)
                updated_count += 1
        else:
            # No existing data, fetch complete path
            fetch_complete_orbit_path(obj, orbit_key, today, end_window, interval, center_id, center_id_type)
            updated_count += 1
    
    # Save the updated data
    save_orbit_paths(orbit_paths_over_time)
    
    update_status(
        f"Updated {updated_count} orbit paths, {already_current} already current. "
        f"Data now extends to {end_window_str}. Saved approximately {time_saved_hours:.1f} hours of fetch time."
    )
    
    return updated_count, already_current, len(object_list), time_saved_hours

def prune_old_data(max_age_days=MAX_DATA_AGE_DAYS):
    """
    Prune very old data points to keep the file size manageable.
    
    Parameters:
        max_age_days: Maximum age of data to keep (default: 90 days)
        
    Returns:
        int: Number of data points pruned
    """
    global orbit_paths_over_time
    
    if not max_age_days or max_age_days <= 0:
        return 0
        
    today = datetime.today()
    cutoff_date = today - timedelta(days=max_age_days)
    cutoff_str = cutoff_date.strftime("%Y-%m-%d")
    
    points_removed = 0
    
    for key, orbit_data in orbit_paths_over_time.items():
        if "data_points" in orbit_data:
            dates_to_remove = []
            
            for date_str in orbit_data["data_points"]:
                try:
                    point_date = datetime.strptime(date_str, "%Y-%m-%d")
                    if point_date < cutoff_date:
                        dates_to_remove.append(date_str)
                except ValueError:
                    # Skip invalid date formats
                    continue
            
            # Remove old points
            for date_str in dates_to_remove:
                del orbit_data["data_points"][date_str]
                points_removed += 1
            
            # Update metadata if points were removed
            if dates_to_remove and orbit_data["data_points"]:
                remaining_dates = [datetime.strptime(d, "%Y-%m-%d") for d in orbit_data["data_points"].keys()]
                if remaining_dates:
                    earliest_date = min(remaining_dates)
                    orbit_data["metadata"]["earliest_date"] = earliest_date.strftime("%Y-%m-%d")
    
    # Save if changes were made
    if points_removed > 0:
        save_orbit_paths(orbit_paths_over_time)
        
    return points_removed


def get_orbit_data_for_plotting(objects_to_plot, center_object_name='Sun'):
    """
    Get orbit path data for plotting.
    
    Parameters:
        objects_to_plot: List of objects to get data for
        center_object_name: Name of central body
        
    Returns:
        dict: Dictionary mapping object names to their orbit path data in plotting format
    """
    plot_data = {}
    
    # Extract just the names from the objects_to_plot list
    selected_names = [obj['name'] for obj in objects_to_plot]
    
    for name in selected_names:
        if name == center_object_name:
            continue
            
        orbit_key = f"{name}_{center_object_name}"
        
        if orbit_key in orbit_paths_over_time:
            orbit_data = orbit_paths_over_time[orbit_key]
            
            # Extract coordinates from time-indexed data
            data_points = orbit_data.get("data_points", {})
            dates = sorted(data_points.keys())
            
            if not dates:
                continue
                
            # Reconstruct coordinate arrays
            x_coords = []
            y_coords = []
            z_coords = []
            
            for date in dates:
                point = data_points[date]
                x_coords.append(point["x"])
                y_coords.append(point["y"])
                z_coords.append(point["z"])
            
            plot_data[name] = {
                'x': x_coords,
                'y': y_coords,
                'z': z_coords,
                'dates': dates
            }
        
        # Fallback to old key format if the new format isn't found
        elif name in orbit_paths_over_time:
            # Handle legacy format data that might still be in the cache
            path = orbit_paths_over_time[name]
            if 'x' in path and 'y' in path and 'z' in path:
                plot_data[name] = {
                    'x': path['x'],
                    'y': path['y'],
                    'z': path['z'],
                    'dates': []  # No dates in legacy format
                }
    
    return plot_data


def get_data_stats():
    """
    Get statistics about the stored orbit data.
    
    Returns:
        dict: Statistics about the orbit data
    """
    stats = {
        "total_objects": len(orbit_paths_over_time),
        "total_points": 0,
        "earliest_date": None,
        "latest_date": None,
        "file_size_mb": 0,
        "center_bodies": set(),
        "objects_per_center": {}
    }
    
    try:
        file_size = os.path.getsize(ORBIT_PATHS_FILE) / (1024 * 1024)
        stats["file_size_mb"] = round(file_size, 2)
    except (FileNotFoundError, OSError):
        pass
    
    earliest_dates = []
    latest_dates = []
    
    for key, data in orbit_paths_over_time.items():
        # Count data points
        if "data_points" in data:
            stats["total_points"] += len(data["data_points"])
            
            # Extract center body
            if "_" in key:
                _, center = key.split("_", 1)
                stats["center_bodies"].add(center)
                
                # Count objects per center
                if center not in stats["objects_per_center"]:
                    stats["objects_per_center"][center] = 0
                stats["objects_per_center"][center] += 1
            
            # Track date ranges
            metadata = data.get("metadata", {})
            if "earliest_date" in metadata:
                try:
                    earliest_dates.append(datetime.strptime(metadata["earliest_date"], "%Y-%m-%d"))
                except ValueError:
                    pass
                
            if "latest_date" in metadata:
                try:
                    latest_dates.append(datetime.strptime(metadata["latest_date"], "%Y-%m-%d"))
                except ValueError:
                    pass
    
    # Find overall date range
    if earliest_dates:
        stats["earliest_date"] = min(earliest_dates).strftime("%Y-%m-%d")
    
    if latest_dates:
        stats["latest_date"] = max(latest_dates).strftime("%Y-%m-%d")
    
    return stats


def on_center_change(*args, objects=None, planetary_params=None, parent_planets=None):
    """
    Update orbit paths when the center object is changed.
    
    Parameters:
        *args: Variable arguments for Tkinter trace_add
        objects: List of all celestial objects
        planetary_params: Dictionary of orbital parameters
        parent_planets: Dictionary mapping planets to their satellites
        
    Returns:
        None
    """
#    global center_object_var, root, status_display
    global center_object_var, root, status_display, last_center_updated, last_update_time
    
    # If any required parameters are missing, return early
    if not center_object_var or not objects:
        return
    
    center_object = center_object_var.get()

    # Check if this is the same center we just updated
    now = datetime.now()
    if (center_object == last_center_updated and 
        last_update_time and 
        (now - last_update_time).total_seconds() < 600):  # 10 minutes cache
        update_status(f"Using cached data for center: {center_object}")
        return

    if center_object != 'Sun':

        # Only fetch non-Sun centered paths when needed to avoid excessive startup time
#        if status_display:
#            status_display.config(text=f"Updating orbit paths for center: {center_object}...")
#        if root:
#            root.update()  # Force GUI to refresh

        # Only fetch non-Sun centered paths when needed to avoid excessive startup time
        update_status(f"Updating orbit paths for center: {center_object}...")
        if root:
            root.update()  # Force GUI to refresh            
        
        # Call the incremental update with the new center
        updated, current, total, time_saved = update_orbit_paths_incrementally(
            object_list=objects,
            center_object_name=center_object,
            days_ahead=730,
            planetary_params=planetary_params,
            parent_planets=parent_planets,
            root_widget=root
        )
        
#        if status_display:
#            status_display.config(
#                text=f"Updated {updated} orbit paths, {current} already current for center: {center_object}"
#            )

        # Update our cache information
        last_center_updated = center_object
        last_update_time = now
        
        update_status(
            f"Updated {updated} orbit paths, {current} already current for center: {center_object}"
        )


def plot_orbit_paths(fig, objects_to_plot, center_object_name='Sun', color_map=None, parent_planets=None):
    """
    Plot orbit paths using time-indexed data.
    
    Parameters:
        fig: Plotly figure object
        objects_to_plot: List of objects to plot orbits for
        center_object_name: Name of the central body (default: 'Sun')
        color_map: Function to get color for an object
        parent_planets: Dictionary mapping planets to their satellites
        
    Returns:
        plotly.graph_objects.Figure: The modified figure with orbits added
    """
    # Debug output to verify we're getting the right list of selected objects
    selected_names = [obj['name'] for obj in objects_to_plot]
    print("\nSelected objects for orbit paths:")
    for name in selected_names:
        print(f"  - {name}")

    for name in selected_names:
        # Skip objects that are the center
        if name == center_object_name:
            continue
            
        # Check if this is a satellite of the center object
        is_satellite_of_center = False
        if parent_planets and center_object_name in parent_planets:
            is_satellite_of_center = name in parent_planets.get(center_object_name, [])
        
        # Generate a unique key for this object-center pair
        orbit_key = f"{name}_{center_object_name}"
        
        # Check if we have the orbit path for this object-center combination
        if orbit_key in orbit_paths_over_time:
            orbit_data = orbit_paths_over_time[orbit_key]
            
            # Extract coordinates from time-indexed data
            data_points = orbit_data.get("data_points", {})
            dates = sorted(data_points.keys())
            
            if not dates:
                print(f"No data points found for {name} relative to {center_object_name}")
                continue
                
            # Reconstruct coordinate arrays
            x_coords = []
            y_coords = []
            z_coords = []
            
            for date in dates:
                point = data_points[date]
                x_coords.append(point["x"])
                y_coords.append(point["y"])
                z_coords.append(point["z"])
            
            # Create the hover text
            if is_satellite_of_center:
                hover_text = [f"{name} Orbit around {center_object_name}"] * len(x_coords)
                orbit_name = f"{name} Orbit around {center_object_name}"
            else:
                hover_text = [f"{name} Orbit"] * len(x_coords)
                orbit_name = f"{name} Orbit"

            print(f"Plotting orbit for {name} relative to {center_object_name} ({len(x_coords)} points)")
            
            # Get color if color_map is provided
            color = 'white'  # Default color
            if color_map:
                color = color_map(name)
                
            # Add orbit trace to figure
            fig.add_trace(
                go.Scatter3d(
                    x=x_coords,
                    y=y_coords,
                    z=z_coords,
                    mode='lines',
                    line=dict(width=1, color=color),  # uses the color from color_map
                    name=orbit_name,
                    text=hover_text,
                    customdata=hover_text,
                    hovertemplate='%{text}<extra></extra>',
                    showlegend=True
                )
            )
            
        # Fallback to old key format if the new format isn't found
        elif name in orbit_paths_over_time:
            path = orbit_paths_over_time[name]
            
            # Skip entries that don't have proper coordinates
            if not isinstance(path, dict) or 'x' not in path:
                continue
                
            # Create the hover text arrays
            hover_text = [f"{name} Orbit"] * len(path['x'])
            
            # Get color if color_map is provided
            color = 'white'  # Default color
            if color_map:
                color = color_map(name)

            fig.add_trace(
                go.Scatter3d(
                    x=path['x'],
                    y=path['y'],
                    z=path['z'],
                    mode='lines',
                    line=dict(width=1, color=color),
                    name=f"{name} Orbit",
                    text=hover_text,
                    customdata=hover_text,
                    hovertemplate='%{text}<extra></extra>',
                    showlegend=True
                )
            )
        else:
            print(f"No orbit path found for {name} relative to {center_object_name}")
            
    return fig