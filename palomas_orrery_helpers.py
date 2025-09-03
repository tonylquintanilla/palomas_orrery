#Paloma's Orrery - Solar System Visualization Tool

# Import necessary libraries
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
from astroquery.jplhorizons import Horizons
import numpy as np
from datetime import datetime, timedelta
import calendar
import plotly.graph_objs as go
import webbrowser
import os
import warnings
from astropy.utils.exceptions import ErfaWarning
from astropy.time import Time
import traceback
import threading
import time  # Used here for simulation purposes
import subprocess
import sys
import math
import json
import orbit_data_manager
import shutil

from idealized_orbits import plot_idealized_orbits, planetary_params, parent_planets, planet_tilts, rotate_points 
from formatting_utils import format_maybe_float, format_km_float
from shared_utilities import create_sun_direction_indicator
from planet_visualization import (
    create_celestial_body_visualization,
    create_planet_visualization,
    create_planet_shell_traces,
    create_sun_visualization,

    mercury_inner_core_info,
    mercury_outer_core_info,
    mercury_mantle_info,
    mercury_crust_info,
    mercury_atmosphere_info,
    mercury_magnetosphere_info,
    mercury_hill_sphere_info,

    venus_core_info,
    venus_mantle_info,
    venus_crust_info,
    venus_atmosphere_info,
    venus_upper_atmosphere_info,
    venus_magnetosphere_info,
    venus_hill_sphere_info,

    earth_inner_core_info,
    earth_outer_core_info,
    earth_lower_mantle_info,
    earth_upper_mantle_info,
    earth_crust_info,
    earth_atmosphere_info,
    earth_upper_atmosphere_info,
    earth_magnetosphere_info,
    earth_hill_sphere_info,

    moon_inner_core_info,
    moon_outer_core_info,
    moon_mantle_info,
    moon_crust_info,
    moon_exosphere_info,
    moon_hill_sphere_info,

    mars_inner_core_info,
    mars_outer_core_info,
    mars_mantle_info,
    mars_crust_info,
    mars_atmosphere_info,
    mars_upper_atmosphere_info,
    mars_magnetosphere_info,
    mars_hill_sphere_info,

    jupiter_core_info,
    jupiter_metallic_hydrogen_info,
    jupiter_molecular_hydrogen_info,
    jupiter_cloud_layer_info,
    jupiter_upper_atmosphere_info,
    jupiter_ring_system_info,
    jupiter_radiation_belts_info,
    jupiter_io_plasma_torus_info,
    jupiter_magnetosphere_info,
    jupiter_hill_sphere_info,

    saturn_core_info,
    saturn_metallic_hydrogen_info,
    saturn_molecular_hydrogen_info,
    saturn_cloud_layer_info,
    saturn_upper_atmosphere_info,
    saturn_ring_system_info,
    saturn_radiation_belts_info,
    saturn_enceladus_plasma_torus_info,
    saturn_magnetosphere_info,
    saturn_hill_sphere_info,

    uranus_core_info,
    uranus_mantle_info,
    uranus_cloud_layer_info,
    uranus_upper_atmosphere_info,
    uranus_ring_system_info,
    uranus_radiation_belts_info,
    uranus_magnetosphere_info,
    uranus_hill_sphere_info, 

    neptune_core_info,
    neptune_mantle_info,
    neptune_cloud_layer_info,
    neptune_upper_atmosphere_info,
    neptune_ring_system_info,
    neptune_radiation_belts_info,
    neptune_magnetosphere_info,
    neptune_hill_sphere_info,

    pluto_core_info,
    pluto_mantle_info,
    pluto_crust_info,
    pluto_haze_layer_info,
    pluto_atmosphere_info,
    pluto_hill_sphere_info,

    eris_core_info,
    eris_mantle_info,
    eris_crust_info,
    eris_atmosphere_info,
    eris_hill_sphere_info, 

    planet9_surface_info,
    planet9_hill_sphere_info           
)

from solar_visualization_shells import (
    hover_text_sun,
    gravitational_influence_info,
    outer_oort_info,
    inner_oort_info,
    inner_limit_oort_info,
    solar_wind_info,
    termination_shock_info,
    outer_corona_info,
    inner_corona_info,
    chromosphere_info,
    photosphere_info,
    radiative_zone_info,
    core_info
)

from constants_new import (
    color_map,
    note_text,
    INFO,
    CENTER_BODY_RADII,
    KM_PER_AU, 
    LIGHT_MINUTES_PER_AU,
    KNOWN_ORBITAL_PERIODS
)

from visualization_utils import (format_hover_text, add_hover_toggle_buttons, format_detailed_hover_text)

from save_utils import save_plot

from shutdown_handler import PlotlyShutdownHandler, create_monitored_thread, show_figure_safely

DEFAULT_MARKER_SIZE = 6
HORIZONS_MAX_DATE = datetime(2199, 12, 29, 0, 0, 0)
CENTER_MARKER_SIZE = 10  # For central objects like the Sun

# Constants
LIGHT_MINUTES_PER_AU = 8.3167  # Approximate light-minutes per Astronomical Unit
KM_PER_AU = 149597870.7       # Kilometers per Astronomical Unit
CORE_AU = 0.00093               # Core in AU, or approximately 0.2 Solar radii
RADIATIVE_ZONE_AU = 0.00325     # Radiative zone in AU, or approximately 0.7 Solar radii
SOLAR_RADIUS_AU = 0.00465047  # Sun's radius in AU
INNER_LIMIT_OORT_CLOUD_AU = 2000   # Inner Oort cloud inner boundary in AU.
INNER_OORT_CLOUD_AU = 20000   # Inner Oort cloud outer boundary in AU.
OUTER_OORT_CLOUD_AU = 100000   # Oort cloud outer boundary in AU.
GRAVITATIONAL_INFLUENCE_AU = 126000   # Sun's gravitational influence in AU.
CHROMOSPHERE_RADII = 1.5    # The Chromosphere extends from about 1 to 1.5 solar radii or about 0.00465 - 0.0070 AU
INNER_CORONA_RADII = 3  # Inner corona extends to 2 to 3 solar radii or about 0.01 AU
OUTER_CORONA_RADII = 50       # Outer corona extends up to 50 solar radii or about 0.2 AU, more typically 10 to 20 solar radii
TERMINATION_SHOCK_AU = 94       # Termination shock where the solar wind slows to subsonic speeds. 
HELIOPAUSE_RADII = 26449         # Outer boundary of the solar wind and solar system, about 123 AU. 
PARKER_CLOSEST_RADII = 8.2    # Parker's closest approach was 3.8 million miles on 12-24-24 at 6:53 AM EST (0.41 AU, 8.2 solar radii)

# Add these constants after existing constants
TEMP_CACHE_FILE = "orbit_paths_temp.json"
CLEANUP_TRACKING_FILE = ".last_orbit_cleanup"
temp_cache = {}  # In-memory temporary cache
remember_update_choice = None  # Session memory for dialog choice
update_choice_remembered = False  # Flag for remembering choice

def calculate_planet9_position_on_orbit(a=600, e=0.30, i=6, omega=150, Omega=90, theta=75):
    """
    Calculate position that lies exactly on the orbit defined by the parameters
    
    Parameters:
        a: Semi-major axis in AU
        e: Eccentricity
        i: Inclination in degrees
        omega: Argument of perihelion in degrees
        Omega: Longitude of ascending node in degrees
        theta: True anomaly in degrees - adjusted to place object on orbit
    
    Returns:
        (x, y, z) position in AU and range (distance from Sun)
    """
    # Convert angles to radians
    i_rad = math.radians(i)
    omega_rad = math.radians(omega)
    Omega_rad = math.radians(Omega)
    theta_rad = math.radians(theta)
    
    # Calculate distance from Sun at this point in the orbit
    r = a * (1 - e**2) / (1 + e * math.cos(theta_rad))
    
    # Calculate position in orbital plane
    x_orbit = r * math.cos(theta_rad)
    y_orbit = r * math.sin(theta_rad)
    
    # Rotate to account for orientation of orbit in 3D space
    # First, rotate by argument of perihelion
    x_perihelion = x_orbit * math.cos(omega_rad) - y_orbit * math.sin(omega_rad)
    y_perihelion = x_orbit * math.sin(omega_rad) + y_orbit * math.cos(omega_rad)
    
    # Then, rotate to account for inclination
    x_inclined = x_perihelion
    y_inclined = y_perihelion * math.cos(i_rad)
    z_inclined = y_perihelion * math.sin(i_rad)
    
    # Finally, rotate by longitude of ascending node
    x = x_inclined * math.cos(Omega_rad) - y_inclined * math.sin(Omega_rad)
    y = x_inclined * math.sin(Omega_rad) + y_inclined * math.cos(Omega_rad)
    z = z_inclined
    
    # Calculate range for consistency
    range_val = math.sqrt(x**2 + y**2 + z**2)
    
    return x, y, z, range_val

def rotate_points2(x, y, z, angle, axis='z'):
    """
    Rotates points (x,y,z) about the given axis by 'angle' radians.
    Returns (xr, yr, zr) as numpy arrays.
    
    Parameters:
        x (array-like): x coordinates
        y (array-like): y coordinates
        z (array-like): z coordinates
        angle (float): rotation angle in radians
        axis (str): axis of rotation ('x', 'y', or 'z')
        
    Returns:
        tuple: (xr, yr, zr) rotated coordinates
    """
    import numpy as np
    
    # Convert inputs to numpy arrays if they aren't already
    x = np.array(x, copy=True)
    y = np.array(y, copy=True)
    z = np.array(z, copy=True)

    # Initialize rotated coordinates
    xr = x.copy()
    yr = y.copy()
    zr = z.copy()

    # Perform rotation based on specified axis
    if axis == 'z':
        # Rotate about z-axis
        xr = x * np.cos(angle) - y * np.sin(angle)
        yr = x * np.sin(angle) + y * np.cos(angle)
        # zr remains the same
    elif axis == 'x':
        # Rotate about x-axis
        yr = y * np.cos(angle) - z * np.sin(angle)
        zr = y * np.sin(angle) + z * np.cos(angle)
        # xr remains the same
    elif axis == 'y':
        # Rotate about y-axis
        zr = z * np.cos(angle) - x * np.sin(angle)
        xr = z * np.sin(angle) + x * np.cos(angle)
        # yr remains the same
    else:
        raise ValueError(f"Unknown rotation axis: {axis}. Use 'x', 'y', or 'z'.")

    return xr, yr, zr

def calculate_axis_range(objects_to_plot):
    """Calculate appropriate axis range based on outermost planet"""
    # Find the maximum semi-major axis of selected planets
    max_orbit = max(planetary_params[obj['name']]['a'] 
                   for obj in objects_to_plot 
                   if obj['name'] in planetary_params)
    
    # Add 20% padding
    max_range = max_orbit * 1.2
    
    # Print debug info
    print(f"\nAxis range calculation:")
    print(f"Maximum orbit (AU): {max_orbit}")
    print(f"Range with padding: ±{max_range}")
    
    return [-max_range, max_range]
    
def fetch_trajectory(object_id, dates_list, center_id='Sun', id_type=None):
    """
    Fetch trajectory data in batch for all dates, handling missing epochs through interpolation.
    Includes velocity calculations and additional orbital parameters for each point.
    
    Parameters:
        object_id (str): ID of the object to fetch
        dates_list (list): List of datetime objects
        center_id (str): ID of central body (default: 'Sun')
        id_type (str): Type of ID (e.g., None, 'smallbody')
        
    Returns:
        list: List of position dictionaries with complete orbital data
    """
    # Debug output for BepiColombo
    if object_id == '-121':
        print(f"\nNOTE: BepiColombo trajectory has a known display bug.")
        print(f"      Position marker shows correctly; trajectory line may not appear.")
        print(f"      Debug: {len(dates_list)} dates requested from {dates_list[0].strftime('%Y-%m-%d')} to {dates_list[-1].strftime('%Y-%m-%d')}")
    # KNOWN BUG: BepiColombo trajectory not plotting (as of Aug 2025)
    # Symptoms:
    #   - Current position marker displays correctly
    #   - Trajectory path shows "No ephemeris available for -121"
    #   - Issue specific to BepiColombo; other spacecraft work
    #   - Verified data exists in Horizons through 2027-04-05
    # 
    # Attempted fixes that didn't work:
    #   - Changing id_type (None, 'id', omitted)
    #   - Converting to TDB time scale (broke ALL spacecraft)
    #   - Using vectors vs ephemerides
    #
    # Workaround: BepiColombo shows current position only
    # TODO: Revisit after other trajectory improvements        
    
    # Skip trajectory fetching for Planet 9
    if object_id == 'planet9_placeholder':
        # Return a list of None values matching the length of dates_list
        return [None] * len(dates_list)

    try:
        # Convert dates to Julian Date
        times = Time(dates_list)
        epochs = times.jd.tolist()
        
        # Query Horizons
        obj = Horizons(id=object_id, id_type=id_type, location='@' + center_id, epochs=epochs)
        vectors = obj.vectors()

        # Use a small tolerance when matching returned JD to requested epochs
        tolerance = 1e-3    # original 1e-5 does not work for spacecraft BepiColombo; loosening the tolerance
        positions = [None] * len(epochs)
        
        print(f"\nProcessing trajectory for {object_id}:")
        print(f"Requested epochs: {len(epochs)}")
        print(f"Returned vectors: {len(vectors)}")
        
        # First pass: Match direct positions using tolerance
        for vec in vectors:
            jd_returned = float(vec['datetime_jd'])
            # Find the closest epoch in our list
            differences = [abs(jd_returned - epoch) for epoch in epochs]
            idx = differences.index(min(differences))
            if differences[idx] < tolerance:
                # Extract position components
                x = float(vec['x']) if 'x' in vec.colnames else None
                y = float(vec['y']) if 'y' in vec.colnames else None
                z = float(vec['z']) if 'z' in vec.colnames else None
                
                # Extract velocity components
                vx = float(vec['vx']) if 'vx' in vec.colnames else None
                vy = float(vec['vy']) if 'vy' in vec.colnames else None
                vz = float(vec['vz']) if 'vz' in vec.colnames else None
                
                # Calculate velocity magnitude
                velocity = np.sqrt(vx**2 + vy**2 + vz**2) if (vx is not None and 
                                                             vy is not None and 
                                                             vz is not None) else 'N/A'
                
                # Extract range and range_rate
                range_ = float(vec['range']) if 'range' in vec.colnames else None
                range_rate = float(vec['range_rate']) if 'range_rate' in vec.colnames else None
                
                # Calculate distance in light-minutes and light-hours
                distance_km = range_ * KM_PER_AU if range_ is not None else 'N/A'
                distance_lm = range_ * LIGHT_MINUTES_PER_AU if range_ is not None else 'N/A'
                distance_lh = (distance_lm / 60) if isinstance(distance_lm, float) else 'N/A'
                
                # Store complete position data
                positions[idx] = {
                    'x': x,
                    'y': y,
                    'z': z,
                    'vx': vx,
                    'vy': vy,
                    'vz': vz,
                    'velocity': velocity,
                    'range': range_,
                    'range_rate': range_rate,
                    'distance_km': distance_km,
                    'distance_lm': distance_lm,
                    'distance_lh': distance_lh,
                    'date': dates_list[idx]
                }

        # Count how many direct matches we got
        direct_matches = sum(1 for pos in positions if pos is not None)
        print(f"Direct position matches: {direct_matches}")

        # Second pass: Fill in missing entries through interpolation
        interpolated_count = 0
        for i in range(len(positions)):
            if positions[i] is None:
                # Search backward for previous valid position
                prev_idx = i - 1
                while prev_idx >= 0 and positions[prev_idx] is None:
                    prev_idx -= 1
                    
                # Search forward for next valid position
                next_idx = i + 1
                while next_idx < len(positions) and positions[next_idx] is None:
                    next_idx += 1

                # Attempt interpolation if we have both bounds
                if prev_idx >= 0 and next_idx < len(positions):
                    # Calculate interpolation fraction based on timestamps
                    t0 = dates_list[prev_idx].timestamp()
                    t1 = dates_list[next_idx].timestamp()
                    t = dates_list[i].timestamp()
                    frac = (t - t0) / (t1 - t0)
                    
                    # Linear interpolation for position
                    interp_x = (1 - frac) * positions[prev_idx]['x'] + frac * positions[next_idx]['x']
                    interp_y = (1 - frac) * positions[prev_idx]['y'] + frac * positions[next_idx]['y']
                    interp_z = (1 - frac) * positions[prev_idx]['z'] + frac * positions[next_idx]['z']
                    
                    # Initialize interpolated values
                    interp_vx = None
                    interp_vy = None
                    interp_vz = None
                    interp_velocity = 'N/A'
                    interp_range = None
                    interp_range_rate = None
                    interp_distance_km = 'N/A'
                    interp_distance_lm = 'N/A'
                    interp_distance_lh = 'N/A'
                    
                    # Interpolate velocity components if available
                    if (isinstance(positions[prev_idx]['vx'], (int, float)) and 
                        isinstance(positions[next_idx]['vx'], (int, float))):
                        interp_vx = (1 - frac) * positions[prev_idx]['vx'] + frac * positions[next_idx]['vx']
                        interp_vy = (1 - frac) * positions[prev_idx]['vy'] + frac * positions[next_idx]['vy']
                        interp_vz = (1 - frac) * positions[prev_idx]['vz'] + frac * positions[next_idx]['vz']
                        interp_velocity = np.sqrt(interp_vx**2 + interp_vy**2 + interp_vz**2)
                    
                    # Interpolate range if available
                    if (isinstance(positions[prev_idx]['range'], (int, float)) and 
                        isinstance(positions[next_idx]['range'], (int, float))):
                        interp_range = (1 - frac) * positions[prev_idx]['range'] + frac * positions[next_idx]['range']
                        interp_distance_km = interp_range * KM_PER_AU
                        interp_distance_lm = interp_range * LIGHT_MINUTES_PER_AU
                        interp_distance_lh = interp_distance_lm / 60
                    
                    # Interpolate range_rate if available
                    if (isinstance(positions[prev_idx]['range_rate'], (int, float)) and 
                        isinstance(positions[next_idx]['range_rate'], (int, float))):
                        interp_range_rate = (1 - frac) * positions[prev_idx]['range_rate'] + frac * positions[next_idx]['range_rate']
                    
                    positions[i] = {
                        'x': interp_x,
                        'y': interp_y,
                        'z': interp_z,
                        'vx': interp_vx,
                        'vy': interp_vy,
                        'vz': interp_vz,
                        'velocity': interp_velocity,
                        'range': interp_range,
                        'range_rate': interp_range_rate,
                        'distance_km': interp_distance_km,
                        'distance_lm': interp_distance_lm,
                        'distance_lh': interp_distance_lh,
                        'date': dates_list[i]
                    }
                    interpolated_count += 1
                    
                # If we only have data on one side, use nearest neighbor
                elif prev_idx >= 0:
                    positions[i] = positions[prev_idx].copy()
                    positions[i]['date'] = dates_list[i]
                    interpolated_count += 1
                elif next_idx < len(positions):
                    positions[i] = positions[next_idx].copy()
                    positions[i]['date'] = dates_list[i]
                    interpolated_count += 1

        print(f"Interpolated positions: {interpolated_count}")
        print(f"Final coverage: {direct_matches + interpolated_count}/{len(epochs)} epochs")
        
        # If we have very low coverage, warn the user
        coverage_pct = (direct_matches + interpolated_count) / len(epochs) * 100
        if coverage_pct < 50:
            print(f"Warning: Low data coverage ({coverage_pct:.1f}%) for {object_id}")
        
        return positions
        
    except Exception as e:
        if "No ephemeris for target" in str(e):
            print(f"No ephemeris available for {object_id}")
            return [None] * len(dates_list)
        print(f"Error fetching trajectory for {object_id}: {e}")
        traceback.print_exc()  # Add traceback for better debugging
        return [None] * len(dates_list)
    
def fetch_orbit_path(obj_info, start_date, end_date, interval, center_id='@0', id_type=None):
    """
    Fetch orbit path data from JPL Horizons for the given object between start_date and end_date,
    using the specified time interval.
    Returns a dictionary with keys 'x', 'y', and 'z' or None on failure.
    
    Parameters:
        obj_info (dict): Object information dictionary
        start_date (datetime): Start date for the orbit path
        end_date (datetime): End date for the orbit path
        interval (str): Time interval (e.g., "1d", "12h")
        center_id (str): ID of the central body (default: '@0' for solar system barycenter)
        id_type (str): Type of ID for the object (None, 'id', 'smallbody', etc.)
    """
# def fetch_orbit_path(obj_info, start_date, end_date, interval):

    try:
        from astroquery.jplhorizons import Horizons
        # Use the object's id and id_type
        object_id = obj_info['id']
        id_type = obj_info.get('id_type', None)
        
        # Format the center_id appropriately
        location = center_id
        if not location.startswith('@'):
            location = '@' + location

#        location = "@0"  # This typically refers to the solar system barycenter
        
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
        return None
    
def pad_trajectory(global_dates, object_start_date, object_end_date, object_id, center_id, id_type):
    """Fetch trajectory and pad with None before start_date and after end_date."""
    # Filter dates within the object's active period
    filtered_dates = [d for d in global_dates if object_start_date <= d <= object_end_date]
    # Fetch trajectory for active dates
    fetched_positions = fetch_trajectory(object_id, filtered_dates, center_id=center_id, id_type=id_type)
    
    # Calculate padding
    start_pad_count = 0
    end_pad_count = 0
    
    # Count dates before start_date
    for d in global_dates:
        if d < object_start_date:
            start_pad_count += 1
        else:
            break
    
    # Count dates after end_date
    for d in reversed(global_dates):
        if d > object_end_date:
            end_pad_count += 1
        else:
            break
    
    # Pad with None before and after
    padded_positions = (
        [None] * start_pad_count +
        fetched_positions +
        [None] * end_pad_count
    )
    
    return padded_positions

def add_url_buttons(fig, objects_to_plot, selected_objects):
    """
    Add URL buttons for missions and objects in solar system visualizations.
    Displays buttons in two rows if needed (max 14 per row).
    
    Parameters:
        fig: plotly figure object
        objects_to_plot: full list of available objects
        selected_objects: list of currently selected object names
        
    Returns:
        plotly.graph_objects.Figure: The modified figure with URL buttons added
    """
    # Collect objects with URLs that are currently selected
    url_objects = []
    for obj in objects_to_plot:
        if obj['var'].get() == 1 and ('mission_url' in obj or 'url' in obj):          # adds urls for any object   
            url_objects.append({
                'name': obj['name'],
                'url': obj.get('mission_url') or obj.get('url')                        # Use either URL field
            })
    
    # Remove duplicates while preserving order
    seen = set()
    url_objects = [x for x in url_objects if x['name'] not in seen and not seen.add(x['name'])]
    
    if not url_objects:
        return fig

    # Get existing annotations and create new list
    annotations = list(fig.layout.annotations) if fig.layout.annotations else []

    # Constants for button layout
    max_per_row = 14
    button_width = 0.075  # Slight reduction from 0.07 to fit more buttons
    start_x = -0.05  # Starting position after existing links

    # Add URL buttons while preserving existing annotations
    for idx, obj in enumerate(url_objects):
        padded_name = obj['name'].ljust(12)  # This adds spaces to make it exactly 12 chars
        # Determine row and position within row
        row = idx // max_per_row
        position_in_row = idx % max_per_row
        # Calculate x position - each row starts from the left
        button_x = start_x + (position_in_row * button_width)
        # Calculate y position based on row (row 0 is at y=0, row 1 is at y=-0.05)
        button_y = 0.07 - (row * 0.06)
        
        annotations.append(dict(
    #        text=f"<a href='{obj['url']}' target='_blank' style='color:#1E90FF;'>{obj['name']}</a>",
    #        text=f"<a href='{obj['url']}' target='_blank' style='color:#1E90FF;'>{padded_name}</a>",
            text=f"<a href='{obj['url']}' target='_blank' style='color:#1E90FF; font-family:monospace;'>{padded_name}</a>",  # uniform
            xref='paper',
            yref='paper',
            x=button_x,
            y=button_y,  
            showarrow=False,
            font=dict(size=12, color='#1E90FF'),
            align='left',
            bgcolor='rgba(255, 255, 255, 0.1)',
            bordercolor='#1E90FF',
            borderwidth=1,
            borderpad=4,
            xanchor='left',
            yanchor='middle'
        ))

    # Update layout with new annotations using update_layout
    fig.update_layout(annotations=annotations)
    
    return fig

def get_default_camera():
    """Return the default orthographic camera settings for top-down view"""
    return {
        "projection": {
            "type": "orthographic"
        },
        # Looking straight down the z-axis
        "eye": {"x": 0, "y": 0, "z": 1},  # Position above the x-y plane
        "center": {"x": 0, "y": 0, "z": 0},  # Looking at origin
        "up": {"x": 0, "y": 1, "z": 0}  # "Up" direction aligned with y-axis
    }

def print_planet_positions(positions):
    """Print positions and distances for planets."""
    print("\nCurrent Object Positions:")
    print("=" * 50)
    for name, data in positions.items():
        if data is None:
            print(f"{name:15} No position data available")
            continue
            
        x = data.get('x', 'N/A')
        y = data.get('y', 'N/A')
        z = data.get('z', 'N/A')
        distance = data.get('range', 'N/A')
        
        # Format position information
        if isinstance(x, (int, float)) and isinstance(y, (int, float)) and isinstance(z, (int, float)):
            pos_str = f"({x:8.3f}, {y:8.3f}, {z:8.3f}) AU"
        else:
            pos_str = "Position data unavailable"
            
        # Format distance information
        if isinstance(distance, (int, float)):
            dist_str = f"{distance:8.3f} AU"
        else:
            dist_str = "Distance data unavailable"
        
        print(f"{name:15} Position: {pos_str:35} Distance from center: {dist_str}")
    print("=" * 50)

# Helper function to create backup
def create_orbit_backup():
    """Create a backup of orbit cache on startup"""
    if os.path.exists('orbit_paths.json'):
        try:
            shutil.copy('orbit_paths.json', 'orbit_paths_backup.json')
            file_size = os.path.getsize('orbit_paths.json') / (1024 * 1024)  # MB
            message = f"Backup created: orbit_paths_backup.json ({file_size:.1f}MB)"
            print(f"[STARTUP] {message}")
            
            # Print cache statistics to terminal
            with open('orbit_paths.json', 'r') as f:
                orbit_data = json.load(f)
                print(f"[CACHE INFO] Total orbits cached: {len(orbit_data)}")
                print("[CACHE INFO] To manually delete cache, remove 'orbit_paths.json' file")
            
            return message, 'info'
                
        except Exception as e:
            error_msg = f"Warning: Could not create backup: {e}"
            print(f"[ERROR] {error_msg}")
            return error_msg, 'error'
    else:
        message = "No cache found. Will create new cache as needed."
        print(f"[STARTUP] {message}")
        return message, 'info'
    
# Weekly cleanup function -- deprecated
def cleanup_old_orbits():
    """Remove orbit data older than 30 days"""
    try:
        # Check if it's been 7 days since last cleanup
        should_cleanup = True
        if os.path.exists(CLEANUP_TRACKING_FILE):
            with open(CLEANUP_TRACKING_FILE, 'r') as f:
                last_cleanup = float(f.read())
                days_since = (time.time() - last_cleanup) / (24 * 60 * 60)
                should_cleanup = days_since >= 7
        
        if not should_cleanup:
            return None, None
        
        # Load orbit data
        if not os.path.exists('orbit_paths.json'):
            return None, None
            
        with open('orbit_paths.json', 'r') as f:
            orbit_data = json.load(f)
        
        initial_count = len(orbit_data)
        cutoff_time = time.time() - (30 * 24 * 60 * 60)  # 30 days ago
        cleaned_data = {}
        
        # Keep only recent data
        for key, data in orbit_data.items():
            # Add timestamp to old data if missing
            if isinstance(data, dict) and 'last_accessed' not in data:
                data['last_accessed'] = time.time()
            
            # Check age
            if isinstance(data, dict) and 'last_accessed' in data:
                if data['last_accessed'] > cutoff_time:
                    cleaned_data[key] = data
            else:
                # Keep data without timestamp but add one
                if isinstance(data, dict):
                    data['last_accessed'] = time.time()
                cleaned_data[key] = data
        
        removed_count = initial_count - len(cleaned_data)
        
        if removed_count > 0:
            # Save cleaned data
            with open('orbit_paths.json', 'w') as f:
                json.dump(cleaned_data, f)
            
            message = f"Cleanup: Removed {removed_count} orbits older than 30 days"
            print(f"[CLEANUP] {message}")
            print(f"[CLEANUP] Remaining orbits: {len(cleaned_data)}")
            
            # Update tracking file
            with open(CLEANUP_TRACKING_FILE, 'w') as f:
                f.write(str(time.time()))
                
            return message, 'success'
        
        # Update tracking file even if nothing removed
        with open(CLEANUP_TRACKING_FILE, 'w') as f:
            f.write(str(time.time()))
            
        return None, None
            
    except Exception as e:
        error_msg = f"Cleanup error: {e}"
        print(f"[ERROR] {error_msg}")
        return error_msg, 'error'
    
def show_animation_safely(fig, default_name):
    """Show and optionally save an animated Plotly figure with proper cleanup."""
    import tkinter as tk
    from tkinter import filedialog, messagebox
    import webbrowser
    import os
    import tempfile
    
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)

    save_response = messagebox.askyesno(
        "Save Animation",
        "Would you like to save this animation as an interactive HTML file?\n"
        "Click 'Yes' to save, or 'No' to continue without saving.",
        parent=root
    )
    
    try:

        if save_response:
            # Get save location from user
            file_path = filedialog.asksaveasfilename(
                parent=root,
                initialfile=f"{default_name}.html",
                defaultextension=".html",
                filetypes=[("HTML files", "*.html")]
            )
            
            if file_path:
                # Save directly to user's chosen location
                fig.write_html(file_path, include_plotlyjs='cdn', auto_play=False)
                print(f"Animation saved to {file_path}")
                webbrowser.open(f'file://{os.path.abspath(file_path)}')
        else:

            # If user doesn't want to save, just display the animation temporarily
            with tempfile.NamedTemporaryFile(suffix='.html', delete=False) as tmp:
                temp_path = tmp.name
                fig.write_html(temp_path, include_plotlyjs='cdn', auto_play=False)
                webbrowser.open(f'file://{os.path.abspath(temp_path)}')
                
                # Schedule cleanup of temporary file
                def cleanup_temp():
                    try:
                        if os.path.exists(temp_path):
                            os.unlink(temp_path)
                    except Exception as e:
                        print(f"Error cleaning up temporary file: {e}")
                
                # Schedule cleanup after a delay to ensure browser has loaded the file
                root.after(5000, cleanup_temp)
    
    except Exception as e:
        messagebox.showerror(
            "Save Error",
            f"An error occurred:\n{str(e)}",
            parent=root
        )
    finally:
        root.destroy()

