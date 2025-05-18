"""
orbit_data_manager.py - Advanced orbit data caching and management

This module handles the efficient storage and retrieval of orbital path data,
using an incremental approach to minimize API calls and processing time.
"""

import json
import os
from datetime import datetime, timedelta
import numpy as np
from typing import Dict, List, Optional, Any, Tuple, Union
import traceback

from astroquery.jplhorizons import Horizons
from astropy.time import Time
import plotly.graph_objs as go

# Constants
ORBIT_PATHS_FILE = "orbit_paths.json"
DEFAULT_DAYS_AHEAD = 730  # Default to looking 2 years ahead
MAX_DATA_AGE_DAYS = 90  # Maximum age for data before pruning (optional)

# Global variables
orbit_paths_over_time = {}
refresh_all = False
status_display = None  # Will be set from the main module
root = None  # Will be set from the main module
center_object_var = None  # Will be set from the main module

# Add at module level:
last_center_updated = None
last_update_time = None

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
    Load orbit paths from file with backward compatibility.
    
    Parameters:
        file_path: Path to the orbit paths data file
        
    Returns:
        dict: The loaded orbit paths data, converted to the new format if needed
    """
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
            
            # Check if data is in old format and convert if needed
            if data and isinstance(data, dict):
                first_key = next(iter(data), None)
                if first_key and isinstance(data.get(first_key, {}), dict) and "x" in data.get(first_key, {}):
                    # Old format detected, convert to new format
                    return convert_to_new_format(data)
            return data
    except FileNotFoundError:
        print(f"No existing orbit paths file found at {file_path}, creating new cache.")
        return {}
    except Exception as e:
        print(f"Error loading orbit paths: {e}")
        traceback.print_exc()
        return {}


def save_orbit_paths(data=None, file_path=ORBIT_PATHS_FILE):
    """
    Save orbit paths data to file.
    
    Parameters:
        data: Orbit paths data to save (defaults to global orbit_paths_over_time)
        file_path: Path to save the data to
    """
    global orbit_paths_over_time
    
    if data is None:
        data = orbit_paths_over_time
        
    try:
        with open(file_path, "w") as f:
            json.dump(data, f)
        print(f"Orbit paths saved to {file_path}")
    except Exception as e:
        print(f"Error saving orbit paths: {e}")
        traceback.print_exc()


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
    
    Parameters:
        existing_data: Existing orbit data
        new_data: New orbit data to merge
        new_start_date: Start date of new data
        new_end_date: End date of new data
        
    Returns:
        dict: Merged orbit data
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
    
    # Update metadata
    if isinstance(new_end_date, datetime):
        merged_data["metadata"]["latest_date"] = new_end_date.strftime("%Y-%m-%d")
    else:
        merged_data["metadata"]["latest_date"] = new_end_date
        
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
                                     days_ahead=DEFAULT_DAYS_AHEAD, planetary_params=None, 
                                     parent_planets=None, root_widget=None):
    """
    Incrementally update orbit paths by only fetching data for dates not already in the cache.
    
    Parameters:
        object_list: List of objects to update (defaults to all)
        center_object_name: Name of central body (default: 'Sun')
        days_ahead: Number of days to look ahead (default: 730)
        planetary_params: Dictionary of orbital parameters
        parent_planets: Dictionary mapping planets to their satellites
        root_widget: Tkinter root for UI updates
        
    Returns:
        tuple: (updated_count, already_current, total_objects, time_saved_hours)
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