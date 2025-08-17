"""
apsidal_markers.py

Module for calculating perihelion, apohelion, perigee, and apogee dates
based on current orbital positions and orbital elements.

This module provides functions to:
- Calculate true anomaly from 3D position
- Convert between anomaly types (true, eccentric, mean)
- Calculate dates for apsidal points (perihelion/apohelion, perigee/apogee)
- Add apsidal markers to Plotly 3D plots
"""

import numpy as np
import plotly.graph_objects as go
from constants_new import KNOWN_ORBITAL_PERIODS, color_map
from datetime import datetime, timedelta

def calculate_exact_apsides(a, e, i, omega, Omega, rotate_points):
    """
    Calculate exact apsidal positions at theta=0 (periapsis) and theta=pi (apoapsis).
    Uses the mathematical fact that periapsis is always at true anomaly = 0
    and apoapsis is always at true anomaly = pi.
    
    Parameters:
        a: Semi-major axis (AU)
        e: Eccentricity
        i: Inclination (degrees)
        omega: Argument of periapsis (degrees)
        Omega: Longitude of ascending node (degrees)
        rotate_points: Function to rotate points in 3D space
        
    Returns:
        dict: {
            'periapsis': {'x': float, 'y': float, 'z': float, 'distance': float},
            'apoapsis': {'x': float, 'y': float, 'z': float, 'distance': float} or None
        }
    """
    import numpy as np
    
    # Convert angles to radians for rotations
    i_rad = np.radians(i)
    omega_rad = np.radians(omega)
    Omega_rad = np.radians(Omega)
    
    # ========== CALCULATE PERIAPSIS AT THETA=0 ==========
    theta_periapsis = 0.0
    
    # Calculate radius at periapsis
    if e < 1:  # Elliptical orbit
        # r = a(1-e²)/(1+e*cos(θ)) at θ=0 becomes r = a(1-e²)/(1+e) = a(1-e)
        r_periapsis = a * (1 - e)
    else:  # Hyperbolic orbit (e >= 1)
        # r = |a|(e²-1)/(1+e*cos(θ)) at θ=0 becomes r = |a|(e²-1)/(1+e) = |a|(e-1)
        r_periapsis = abs(a) * (e - 1)
    
    # Position in orbital plane at theta=0
    x_orbit_peri = r_periapsis  # r * cos(0) = r
    y_orbit_peri = 0.0          # r * sin(0) = 0
    z_orbit_peri = 0.0
    
    # Apply orbital element rotations to transform from orbital plane to 3D space
    # 1. Rotate by argument of periapsis (ω) around z-axis
    x_temp, y_temp, z_temp = rotate_points([x_orbit_peri], [y_orbit_peri], [z_orbit_peri], omega_rad, 'z')
    # 2. Rotate by inclination (i) around x-axis
    x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, i_rad, 'x')
    # 3. Rotate by longitude of ascending node (Ω) around z-axis
    x_peri, y_peri, z_peri = rotate_points(x_temp, y_temp, z_temp, Omega_rad, 'z')
    
    # Extract single point (rotate_points returns arrays)
    peri_x = x_peri[0]
    peri_y = y_peri[0]
    peri_z = z_peri[0]
    peri_distance = np.sqrt(peri_x**2 + peri_y**2 + peri_z**2)
    
    # Create periapsis result
    periapsis_result = {
        'x': peri_x,
        'y': peri_y,
        'z': peri_z,
        'distance': peri_distance
    }
    
    # ========== CALCULATE APOAPSIS AT THETA=PI (for elliptical only) ==========
    apoapsis_result = None
    
    if e < 1:  # Only elliptical orbits have apoapsis
        theta_apoapsis = np.pi  # 180 degrees
        
        # Calculate radius at apoapsis
        # r = a(1-e²)/(1+e*cos(θ)) at θ=π becomes r = a(1-e²)/(1-e) = a(1+e)
        r_apoapsis = a * (1 + e)
        
        # Position in orbital plane at theta=pi
        x_orbit_apo = r_apoapsis * np.cos(theta_apoapsis)  # r * cos(π) = -r
        y_orbit_apo = r_apoapsis * np.sin(theta_apoapsis)  # r * sin(π) = 0
        z_orbit_apo = 0.0
        
        # Apply orbital element rotations
        # 1. Rotate by argument of periapsis (ω) around z-axis
        x_temp, y_temp, z_temp = rotate_points([x_orbit_apo], [y_orbit_apo], [z_orbit_apo], omega_rad, 'z')
        # 2. Rotate by inclination (i) around x-axis
        x_temp, y_temp, z_temp = rotate_points(x_temp, y_temp, z_temp, i_rad, 'x')
        # 3. Rotate by longitude of ascending node (Ω) around z-axis
        x_apo, y_apo, z_apo = rotate_points(x_temp, y_temp, z_temp, Omega_rad, 'z')
        
        # Extract single point
        apo_x = x_apo[0]
        apo_y = y_apo[0]
        apo_z = z_apo[0]
        apo_distance = np.sqrt(apo_x**2 + apo_y**2 + apo_z**2)
        
        # Create apoapsis result
        apoapsis_result = {
            'x': apo_x,
            'y': apo_y,
            'z': apo_z,
            'distance': apo_distance
        }
    
    return {
        'periapsis': periapsis_result,
        'apoapsis': apoapsis_result
    }

def add_apsidal_range_note(fig, obj_name, perihelion_date, aphelion_date, color_map):
    """
    Add legend entries explaining why actual apsidal markers aren't shown
    when dates are outside JPL Horizons' range.
    Now creates separate legend entries for perihelion and aphelion.
    """
    from datetime import datetime
    import plotly.graph_objects as go
    
    # JPL Horizons data limit
    JPL_MAX_DATE = datetime(2199, 12, 29)
    JPL_MIN_DATE = datetime(1900, 1, 1)
    
    added_notes = False
    
    # Check and add perihelion note separately
    if perihelion_date:
        if perihelion_date > JPL_MAX_DATE:
            date_str = perihelion_date.strftime('%Y-%m-%d')
            note_text = f"{obj_name}: Next perihelion: {date_str} (beyond JPL limit)"
            
            # Add an invisible trace for perihelion
            fig.add_trace(
                go.Scatter3d(
                    x=[None],  # No actual points
                    y=[None],
                    z=[None],
                    mode='markers',
                    marker=dict(
                        size=6,
                        color=color_map(obj_name),
                        symbol='square'  # Open square for perihelion
                    ),
                    name=note_text,
                    showlegend=True,
                    hoverinfo='skip'  # Don't show hover for this invisible trace
                )
            )
            added_notes = True
            
        elif perihelion_date < JPL_MIN_DATE:
            date_str = perihelion_date.strftime('%Y-%m-%d')
            note_text = f"{obj_name}: Perihelion: {date_str} (before JPL limit)"
            
            fig.add_trace(
                go.Scatter3d(
                    x=[None],
                    y=[None],
                    z=[None],
                    mode='markers',
                    marker=dict(
                        size=6,
                        color=color_map(obj_name),
                        symbol='square-open'
                    ),
                    name=note_text,
                    showlegend=True,
                    hoverinfo='skip'
                )
            )
            added_notes = True
    
    # Check and add aphelion note separately
    if aphelion_date:
        if aphelion_date > JPL_MAX_DATE:
            date_str = aphelion_date.strftime('%Y-%m-%d')
            note_text = f"{obj_name}: Next aphelion: {date_str} (beyond JPL limit)"
            
            # Add an invisible trace for aphelion
            fig.add_trace(
                go.Scatter3d(
                    x=[None],  # No actual points
                    y=[None],
                    z=[None],
                    mode='markers',
                    marker=dict(
                        size=6,
                        color=color_map(obj_name),
                        symbol='square'  # Solid square for aphelion
                    ),
                    name=note_text,
                    showlegend=True,
                    hoverinfo='skip'  # Don't show hover for this invisible trace
                )
            )
            added_notes = True
            
        elif aphelion_date < JPL_MIN_DATE:
            date_str = aphelion_date.strftime('%Y-%m-%d')
            note_text = f"{obj_name}: Aphelion: {date_str} (before JPL limit)"
            
            fig.add_trace(
                go.Scatter3d(
                    x=[None],
                    y=[None],
                    z=[None],
                    mode='markers',
                    marker=dict(
                        size=6,
                        color=color_map(obj_name),
                        symbol='square'
                    ),
                    name=note_text,
                    showlegend=True,
                    hoverinfo='skip'
                )
            )
            added_notes = True
    
    return added_notes

def compute_apsidal_dates_with_notes(obj_name, params, current_date=None):
    """
    Compute perihelion/aphelion dates from TP and orbital period.
    Returns both the dates and whether they're within JPL range.
    
    Parameters:
        obj_name: Name of the object
        params: Dictionary containing TP
        current_date: Current date (datetime object) to find next apsidal dates after
    
    Returns:
        tuple: (perihelion_date, aphelion_date, perihelion_in_range, aphelion_in_range)
    """
    from astropy.time import Time
    from constants_new import KNOWN_ORBITAL_PERIODS
    from datetime import timedelta, datetime
    
    # JPL Horizons data limits
    JPL_MIN_DATE = datetime(1900, 1, 1)
    JPL_MAX_DATE = datetime(2199, 12, 29)
    
    if current_date is None:
        current_date = datetime.now()
    
    next_perihelion = None
    next_aphelion = None
    perihelion_in_range = False
    aphelion_in_range = False
    
    if 'TP' in params:
        tp_jd = params['TP']
        tp_time = Time(tp_jd, format='jd')
        tp_datetime = tp_time.datetime
        
        # Get orbital period
        if obj_name in KNOWN_ORBITAL_PERIODS and KNOWN_ORBITAL_PERIODS[obj_name] is not None:
            period_days = KNOWN_ORBITAL_PERIODS[obj_name]
            
            # Find the next perihelion after current_date
            perihelion = tp_datetime
            while perihelion < current_date:
                perihelion += timedelta(days=period_days)
            next_perihelion = perihelion
            
            # Check if it's within JPL range
            perihelion_in_range = JPL_MIN_DATE <= next_perihelion <= JPL_MAX_DATE
            
            # Calculate the corresponding aphelion (halfway through orbit)
            # Only for elliptical orbits
            if params.get('e', 0) < 1:
                next_aphelion = next_perihelion + timedelta(days=period_days/2)
                aphelion_in_range = JPL_MIN_DATE <= next_aphelion <= JPL_MAX_DATE
    
    return next_perihelion, next_aphelion, perihelion_in_range, aphelion_in_range

def estimate_hyperbolic_perihelion_date(current_position, q, e, date):
    """
    Estimate perihelion date for hyperbolic orbits.
    """
    if not current_position or 'x' not in current_position or not date:
        return "Date unknown"
    
    try:
        current_dist = np.sqrt(
            current_position['x']**2 + 
            current_position['y']**2 + 
            current_position['z']**2
        )
        
        if current_dist > q:  # Still approaching perihelion
            distance_to_go = current_dist - q
            
            # Rough velocity estimate for hyperbolic orbit (AU/day)
            if e > 5:  # Very hyperbolic
                estimated_velocity = 0.1
            else:  # Near-parabolic
                estimated_velocity = 0.05
            
            days_to_perihelion = distance_to_go / estimated_velocity
            
            if days_to_perihelion < 365:
                perihelion_date = date + timedelta(days=days_to_perihelion)
                return perihelion_date.strftime('%Y-%m-%d') + " (est)"
            else:
                return "Approaching"
        else:
            return "Near/Past perihelion"
            
    except Exception as e:
        print(f"Error estimating hyperbolic perihelion: {e}")
        return "Approaching"

# In compute_apsidal_dates_from_tp function:
def compute_apsidal_dates_from_tp(obj_name, params, current_date=None):
    """
    Compute the next perihelion/aphelion dates from TP with full time precision.
    For hyperbolic/parabolic orbits (e >= 1), returns the single perihelion date.
    For elliptical orbits (e < 1), computes based on orbital period.
    """
    from astropy.time import Time
    from constants_new import KNOWN_ORBITAL_PERIODS
    from datetime import timedelta, datetime
    
    # JPL Horizons data limits
    JPL_MIN_DATE = datetime(1900, 1, 1)
    JPL_MAX_DATE = datetime(2199, 12, 29)
    
    if current_date is None:
        current_date = datetime.now()
    
    next_perihelion = None
    next_aphelion = None
    
    if 'TP' not in params:
        return None, None
    
    tp_jd = params['TP']
    tp_time = Time(tp_jd, format='jd')
    tp_datetime = tp_time.datetime  # This preserves full precision
    
    # Check eccentricity to determine orbit type
    e = params.get('e', 0)
    
    # Also check if period is -1 (our flag for hyperbolic/parabolic)
    period = KNOWN_ORBITAL_PERIODS.get(obj_name, None)
    is_hyperbolic = (e >= 1) or (period == -1)
    
    if is_hyperbolic:
        # HYPERBOLIC OR PARABOLIC ORBIT
        # These objects make only one pass by the Sun
        # TP is the exact date and time of perihelion passage
        next_perihelion = tp_datetime  # Keep full datetime precision
        
        # No aphelion for hyperbolic/parabolic orbits
        next_aphelion = None
        
        # Log the result with full precision
        if JPL_MIN_DATE <= next_perihelion <= JPL_MAX_DATE:
            # Format with milliseconds (remove last 3 digits of microseconds)
            time_str = next_perihelion.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
            print(f"  {obj_name}: Hyperbolic/parabolic perihelion: {time_str} UTC")
        else:
            time_str = next_perihelion.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
            print(f"  {obj_name}: Hyperbolic/parabolic perihelion: {time_str} UTC (outside JPL range)")
            
    else:
        # ELLIPTICAL ORBIT
        # Get orbital period
        if period and period > 0:  # Valid period
            period_days = period
            
            # Find the next perihelion after current_date
            perihelion = tp_datetime
            while perihelion < current_date:
                perihelion += timedelta(days=period_days)
            next_perihelion = perihelion
            
            # Check if the next perihelion is beyond JPL range
            if next_perihelion > JPL_MAX_DATE:
                print(f"  {obj_name}: Next perihelion ({next_perihelion.strftime('%Y-%m-%d %H:%M:%S')}) is beyond JPL range")
                
                # Find the most recent perihelion within JPL range
                perihelion = tp_datetime
                most_recent_perihelion = None
                while perihelion < JPL_MAX_DATE:
                    if perihelion < current_date:
                        most_recent_perihelion = perihelion
                    perihelion += timedelta(days=period_days)
                
                if most_recent_perihelion:
                    next_perihelion = most_recent_perihelion
                    print(f"  Using most recent perihelion: {next_perihelion.strftime('%Y-%m-%d %H:%M:%S')}")
                else:
                    next_perihelion = tp_datetime
                    print(f"  Using original TP date: {next_perihelion.strftime('%Y-%m-%d %H:%M:%S')}")
            else:
                print(f"  {obj_name}: Next perihelion: {next_perihelion.strftime('%Y-%m-%d %H:%M:%S')}")
            
            # Calculate the corresponding aphelion (halfway through orbit)
            if next_perihelion:
                next_aphelion = next_perihelion + timedelta(days=period_days/2)
                
                if next_aphelion > JPL_MAX_DATE:
                    print(f"  {obj_name}: Aphelion ({next_aphelion.strftime('%Y-%m-%d %H:%M:%S')}) is beyond JPL range")
                else:
                    print(f"  {obj_name}: Next aphelion: {next_aphelion.strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            print(f"  {obj_name}: No valid orbital period")
    
    return next_perihelion, next_aphelion

def add_actual_apsidal_markers(fig, obj_name, params, date_range, positions_dict, color_map, 
                             center_body='Sun', is_satellite=False):
    """
    Add markers for actual perihelion/aphelion (or perigee/apogee) dates.
    
    Parameters:
    -----------
    fig : plotly.graph_objects.Figure
        The figure to add markers to
    obj_name : str
        Name of the celestial object
    params : dict
        Orbital parameters including actual apsidal dates
    date_range : tuple
        (start_date, end_date) to filter which markers to show
    positions_dict : dict
        Dictionary mapping dates to positions {'YYYY-MM-DD': {'x': x, 'y': y, 'z': z}}
    color_map : function
        Function to get color for the object
    center_body : str
        Name of the central body
    is_satellite : bool
        True if object is a satellite (use perigee/apogee instead of perihelion/aphelion)
    """
    from datetime import datetime
    import numpy as np
    import plotly.graph_objects as go
    
    # Handle the case where date_range might be None
    if date_range:
        start_date, end_date = date_range
    else:
        # If no date range, we'll show all markers
        start_date = None
        end_date = None
    
    # Determine which date lists to use
    if is_satellite:
        near_dates = params.get('perigee_dates', [])
        far_dates = params.get('apogee_dates', [])
        near_label = 'Perigee'
        far_label = 'Apogee'
    else:
        near_dates = params.get('perihelion_dates', [])
        far_dates = params.get('aphelion_dates', [])
        near_label = 'Perihelion'
        far_label = 'Aphelion'
    
    # Convert string dates to datetime objects for processing
    # Handle both old format (%Y-%m-%d) and new format (%Y-%m-%d %H:%M:%S)

    near_dates_dt = []
    for d in near_dates:
        try:
            # Try full datetime format first
            dt = datetime.strptime(d, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            # Fall back to date-only format
            dt = datetime.strptime(d, '%Y-%m-%d')
        near_dates_dt.append(dt)

    far_dates_dt = []
    for d in far_dates:
        try:
            # Try full datetime format first
            dt = datetime.strptime(d, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            # Fall back to date-only format
            dt = datetime.strptime(d, '%Y-%m-%d')
        far_dates_dt.append(dt)

    # Add markers for near points (perihelion/perigee)
    for i, date in enumerate(near_dates_dt):
#        date_str = near_dates[i]  # Get the original string format
        
        # Extract just the date part for position lookup
        date_key = date.strftime('%Y-%m-%d')
        
        if date_key in positions_dict:
            pos = positions_dict[date_key]
            
            # Calculate distance from center
            distance_au = np.sqrt(pos['x']**2 + pos['y']**2 + pos['z']**2)
            
            # Display full datetime if available
            date_display = date.strftime('%Y-%m-%d %H:%M:%S')
            
            fig.add_trace(
                go.Scatter3d(
                    x=[pos['x']],
                    y=[pos['y']],
                    z=[pos['z']],
                    mode='markers',                    
                    marker=dict(
                        size=8,
                        color='white',                        
                        symbol='square-open',  # Solid square for actual
                    ),
                    name=f"{obj_name} Actual {near_label}",
                    text=[f"{obj_name} Actual {near_label}"],
                    hovertemplate=(
                        f"<b>{obj_name} at {near_label}</b><br>"
                        f"Date: {date_display} UTC<br>"
                        f"Distance from {center_body}: {distance_au:.6f} AU<br>"
                        "<extra></extra>"
                    ),
                    showlegend=True
                )
            )

    # Add markers for far points (aphelion/apogee)
    for i, date in enumerate(far_dates_dt):
        date_str = far_dates[i]  # Get the original string format
        
        # Extract just the date part for position lookup
        date_key = date.strftime('%Y-%m-%d')
        
        if date_key in positions_dict:
            pos = positions_dict[date_key]
            
            # Calculate distance from center
            distance_au = np.sqrt(pos['x']**2 + pos['y']**2 + pos['z']**2)
            
            # Display full datetime if available
            date_display = date.strftime('%Y-%m-%d %H:%M:%S')
            
            fig.add_trace(
                go.Scatter3d(
                    x=[pos['x']],
                    y=[pos['y']],
                    z=[pos['z']],
                    mode='markers',                    
                    marker=dict(
                        size=8,
                        color='white',                        
                        symbol='square-open',  # Solid square for actual
                    ),
                    name=f"{obj_name} Actual {far_label}",
                    text=[f"{obj_name} Actual {far_label}"],
                    hovertemplate=(
                        f"<b>{obj_name} at {far_label}</b><br>"
                        f"Date: {date_display} UTC<br>"
                        f"Distance from {center_body}: {distance_au:.6f} AU<br>"
                        "<extra></extra>"
                    ),
                    showlegend=True
                )
            )

def fetch_positions_for_apsidal_dates(obj_id, params, date_range, center_id='Sun', 
                                    id_type=None, is_satellite=False, fetch_position=None):
    """
    Fetch actual positions for all apsidal dates within the date range.
    
    Returns:
        dict: Mapping of date strings to position dictionaries
    """
    from datetime import datetime

    if fetch_position is None:
        raise ValueError("fetch_position function must be provided")

    positions = {}

    # Remove the line that unpacks date_range since we're not using it
#    start_date, end_date = date_range
    
    # Get all apsidal dates
    if is_satellite:
        all_dates = params.get('perigee_dates', []) + params.get('apogee_dates', [])
    else:
        all_dates = params.get('perihelion_dates', []) + params.get('aphelion_dates', [])
    
    for date_str in all_dates:
        try:
            # Try to parse with time first, then fall back to date-only
            try:
                date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
            except ValueError:
                date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            
            # Always fetch, no date range check
            pos_data = fetch_position(obj_id, date_obj, center_id=center_id, id_type=id_type)
            if pos_data and 'x' in pos_data:
                # Store with date-only key for compatibility
                date_key = date_obj.strftime('%Y-%m-%d')
                positions[date_key] = pos_data
                print(f"    Fetched position for {date_str}")

        except Exception as e:
            print(f"    Could not fetch position for {date_str}: {e}")                
    
    return positions

def get_orbital_period_days(body_name, semi_major_axis_au=None):
    """
    Get orbital period in Earth days for a given body.
    
    Parameters:
    -----------
    body_name : str
        Name of the celestial body
    semi_major_axis_au : float, optional
        Semi-major axis in AU (used for unknown bodies via Kepler's third law)
    
    Returns:
    --------
    float
        Orbital period in Earth days
    """
    if body_name in KNOWN_ORBITAL_PERIODS:
        period = KNOWN_ORBITAL_PERIODS[body_name]
        # Handle special cases (hyperbolic/parabolic objects)
        if period is None:
            if semi_major_axis_au:
                # For hyperbolic/parabolic orbits, use Kepler's third law
                # This gives a notional period for visualization purposes
                return 365.25 * np.sqrt(abs(semi_major_axis_au)**3)
            else:
                raise ValueError(f"{body_name} has no defined orbital period (hyperbolic/parabolic orbit)")
        return period
    elif semi_major_axis_au:
        # Use Kepler's third law as fallback for unknown bodies
        # P² = a³ (where P is in years and a is in AU)
        # So P_days = 365.25 * sqrt(a³)
        return 365.25 * np.sqrt(abs(semi_major_axis_au)**3)
    else:
        raise ValueError(f"Unknown body {body_name} and no semi-major axis provided")

def calculate_true_anomaly_from_position(x, y, z, a, e, i, omega, Omega):
    """
    Calculate the true anomaly from a position in 3D space.
    
    Parameters:
        x, y, z: Current position in heliocentric/planetocentric coordinates (AU or km)
        a: Semi-major axis (same units as position)
        e: Eccentricity
        i: Inclination (degrees)
        omega: Argument of periapsis (degrees)
        Omega: Longitude of ascending node (degrees)
    
    Returns:
        float: True anomaly in radians (0 to 2π)
    """
    # Convert angles to radians
    i_rad = np.radians(i)
    omega_rad = np.radians(omega)
    Omega_rad = np.radians(Omega)
    
    # Reverse rotation transformations to get back to orbital plane
    # First, reverse the Omega rotation (around z-axis)
    x1 = x * np.cos(-Omega_rad) - y * np.sin(-Omega_rad)
    y1 = x * np.sin(-Omega_rad) + y * np.cos(-Omega_rad)
    z1 = z
    
    # Then, reverse the inclination rotation (around x-axis)
    x2 = x1
    y2 = y1 * np.cos(-i_rad) - z1 * np.sin(-i_rad)
    z2 = y1 * np.sin(-i_rad) + z1 * np.cos(-i_rad)
    
    # Finally, reverse the omega rotation (around z-axis)
    x_orbital = x2 * np.cos(-omega_rad) - y2 * np.sin(-omega_rad)
    y_orbital = x2 * np.sin(-omega_rad) + y2 * np.cos(-omega_rad)
    
    # Calculate true anomaly
    true_anomaly = np.arctan2(y_orbital, x_orbital)
    
    # Ensure positive angle (0 to 2π)
    if true_anomaly < 0:
        true_anomaly += 2 * np.pi
    
    return true_anomaly


def true_to_eccentric_anomaly(true_anomaly, e):
    """
    Convert true anomaly to eccentric anomaly.
    
    Parameters:
        true_anomaly: True anomaly in radians
        e: Eccentricity
    
    Returns:
        float: Eccentric anomaly in radians (or hyperbolic eccentric anomaly for e > 1)
    """
    if e < 1:  # Elliptical orbit
        # For elliptical orbits
        cos_E = (e + np.cos(true_anomaly)) / (1 + e * np.cos(true_anomaly))
        sin_E = np.sqrt(1 - e**2) * np.sin(true_anomaly) / (1 + e * np.cos(true_anomaly))
        E = np.arctan2(sin_E, cos_E)
        
        # Ensure E is positive
        if E < 0:
            E += 2 * np.pi
            
        return E
        
    else:  # Hyperbolic orbit (e > 1)
        # For hyperbolic orbits, use hyperbolic eccentric anomaly
        if abs(true_anomaly) > np.arccos(-1/e):
            # True anomaly is beyond the asymptote - invalid for hyperbolic orbit
            return float('nan')
            
        cosh_F = (e + np.cos(true_anomaly)) / (1 + e * np.cos(true_anomaly))
        F = np.arccosh(cosh_F)
        
        # F should have the same sign as true anomaly
        if true_anomaly > np.pi:
            F = -F
            
        return F


def eccentric_to_mean_anomaly(E, e):
    """
    Convert eccentric anomaly to mean anomaly.
    Uses Kepler's equation.
    
    Parameters:
        E: Eccentric anomaly in radians (or hyperbolic eccentric anomaly)
        e: Eccentricity
    
    Returns:
        float: Mean anomaly in radians
    """
    if e < 1:  # Elliptical orbit
        M = E - e * np.sin(E)
    else:  # Hyperbolic orbit
        M = e * np.sinh(E) - E  # M = e*sinh(F) - F for hyperbolic
    return M


def calculate_time_to_anomaly(current_M, target_M, orbital_period_days):
    """
    Calculate time to reach a target mean anomaly from current mean anomaly.
    
    Parameters:
        current_M: Current mean anomaly (radians)
        target_M: Target mean anomaly (radians)
        orbital_period_days: Orbital period in days
    
    Returns:
        float: Days until target anomaly is reached
    """
    # Calculate angular distance (always forward in time)
    if target_M >= current_M:
        delta_M = target_M - current_M
    else:
        delta_M = (2 * np.pi) + target_M - current_M
    
    # Convert to time
    fraction_of_orbit = delta_M / (2 * np.pi)
    days_to_target = fraction_of_orbit * orbital_period_days
    
    return days_to_target


def calculate_apsidal_dates(date, current_x, current_y, current_z, a, e, i, omega, Omega, body_name="Object"):
    """
    Calculate dates for perihelion/apohelion (or perigee/apogee for satellites).
    
    Parameters:
        date: Current date (datetime object)
        current_x, current_y, current_z: Current position
        a: Semi-major axis
        e: Eccentricity
        i: Inclination (degrees)
        omega: Argument of periapsis (degrees)
        Omega: Longitude of ascending node (degrees)
        body_name: Name of the body (for error messages)
    
    Returns:
        tuple: (perihelion_date, apohelion_date) or (None, None) if calculation fails
    """
    try:
        # Calculate current true anomaly
        current_theta = calculate_true_anomaly_from_position(
            current_x, current_y, current_z, a, e, i, omega, Omega
        )
        
        if e >= 1:  # Hyperbolic orbit
            # For hyperbolic orbits, apohelion doesn't exist
            # Check if we're approaching or past perihelion
            if current_theta < np.pi:
                # Approaching perihelion - estimate time
                if current_theta < 0.1:  # Very close
                    perihelion_date = date
                else:
                    # Rough estimate for hyperbolic approach
                    # This is simplified - proper calculation would be complex
                    days_estimate = 30 * (1 - current_theta/np.pi)
                    perihelion_date = date + timedelta(days=days_estimate)
            else:
                # Past perihelion
                perihelion_date = None
                
            return perihelion_date, None
                
        # For elliptical orbits
        # Get orbital period using the helper function
        try:
            orbital_period_days = get_orbital_period_days(body_name, a)
        except ValueError:
            # If body not found and no semi-major axis, use default
            print(f"Warning: Using Kepler's law for unknown body {body_name}")
            orbital_period_days = 365.25 * np.sqrt(abs(a)**3)

        # Convert current position to mean anomaly
        E_current = true_to_eccentric_anomaly(current_theta, e)
        M_current = eccentric_to_mean_anomaly(E_current, e)
        
        # Perihelion is at M = 0
        days_to_perihelion = calculate_time_to_anomaly(M_current, 0, orbital_period_days)
        perihelion_date = date + timedelta(days=days_to_perihelion)
        
        # Apohelion is at M = π
        days_to_apohelion = calculate_time_to_anomaly(M_current, np.pi, orbital_period_days)
        apohelion_date = date + timedelta(days=days_to_apohelion)
        
        return perihelion_date, apohelion_date
        
    except Exception as ex:
        print(f"Warning: Could not calculate apsidal dates for {body_name}: {ex}")
        return None, None

def add_perihelion_marker(fig, x, y, z, obj_name, a, e, date, current_position, 
                        orbital_params, color_map, q=None):
    """
    Add a perihelion/perigee marker with accurate date calculation.
    Now handles full datetime precision from TP.
    """
    # Calculate perihelion distance if not provided
    if q is None:
        q = a * (1 - e)
    
    # Calculate perihelion date
    perihelion_date_str = ""
    if date is not None and current_position is not None and e < 1:
        perihelion_date, aphelion_date = calculate_apsidal_dates(
            date,
            current_position['x'],
            current_position['y'],
            current_position['z'],
            orbital_params.get('a', a),
            orbital_params.get('e', e),
            orbital_params.get('i', 0),
            orbital_params.get('omega', 0),
            orbital_params.get('Omega', 0),
            obj_name
        )
        
        if perihelion_date is not None:
            # For elliptical orbits with TP, we can calculate precise perihelion time
            if 'TP' in orbital_params and obj_name in KNOWN_ORBITAL_PERIODS:
                period_days = KNOWN_ORBITAL_PERIODS[obj_name]
                if period_days and period_days not in [None, 1e99]:  # Valid period
                    from astropy.time import Time
                    from datetime import timedelta
                    tp_time = Time(orbital_params['TP'], format='jd')
                    tp_datetime = tp_time.datetime
                    
                    # Find the next perihelion after the current date
                    precise_perihelion = tp_datetime
                    while precise_perihelion < date:
                        precise_perihelion += timedelta(days=period_days)
                    
                    perihelion_date_str = f"<br>Date: {precise_perihelion.strftime('%Y-%m-%d %H:%M:%S')} UTC"
                else:
                    # For objects without precise period info
                    perihelion_date_str = f"<br>Date: {perihelion_date.strftime('%Y-%m-%d')}"
            else:
                # No TP available, use calculated date
                perihelion_date_str = f"<br>Date: {perihelion_date.strftime('%Y-%m-%d')}"

    # For hyperbolic orbits, use TP if available
    elif 'TP' in orbital_params and e >= 1:
        from astropy.time import Time
        tp_time = Time(orbital_params['TP'], format='jd')
        tp_datetime = tp_time.datetime
        perihelion_date_str = f"<br>Date: {tp_datetime.strftime('%Y-%m-%d %H:%M:%S')} UTC"
    elif date is not None:
        perihelion_date_str = f"<br>Date: {date.strftime('%Y-%m-%d')}"
    
    # Accuracy note
    accuracy_note = ""
    if e > 0.15:  # High eccentricity
        accuracy_note = "<br><i>Accuracy: ±0.002 AU (strong perturbations)</i>"
    elif e > 0.05:  # Moderate eccentricity
        accuracy_note = "<br><i>Accuracy: ±0.001 AU (moderate perturbations)</i>"
    else:  # Low eccentricity
        accuracy_note = "<br><i>Accuracy: ±0.0005 AU (minimal perturbations)</i>"
    
    # Determine label
    label = "Ideal Periapsis"
    
    # Create hover text with all information
    hover_text = f"<b>{obj_name} {label}</b>{perihelion_date_str}<br>q={q:.6f} AU{accuracy_note}"
    
    fig.add_trace(
        go.Scatter3d(
            x=[x],
            y=[y],
            z=[z],
            mode='markers',
            marker=dict(
                size=6,
                color=color_map(obj_name),
                symbol='square-open'
            ),
            name=f"{obj_name} {label}",
            text=[hover_text],
            customdata=[label],
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    )

def add_apohelion_marker(fig, x, y, z, obj_name, a, e, date, current_position,
                        orbital_params, color_map):
    """
    Add an apohelion/apogee marker to the plot with accurate date calculation.
    Now handles full datetime precision from TP.
    """
    # Calculate aphelion distance
    if e < 1:
        Q = a * (1 + e)
    else:
        # No aphelion for hyperbolic orbits
        return
    
    # Calculate aphelion date
    aphelion_date_str = ""
    if date is not None and current_position is not None and e < 1:
        perihelion_date, aphelion_date = calculate_apsidal_dates(
            date,
            current_position['x'],
            current_position['y'],
            current_position['z'],
            orbital_params.get('a', a),
            orbital_params.get('e', e),
            orbital_params.get('i', 0),
            orbital_params.get('omega', 0),
            orbital_params.get('Omega', 0),
            obj_name
        )
        
        if aphelion_date is not None:
            # For elliptical orbits with TP, we can calculate precise aphelion time
            if 'TP' in orbital_params and obj_name in KNOWN_ORBITAL_PERIODS:
                period_days = KNOWN_ORBITAL_PERIODS[obj_name]
                if period_days and period_days != 1e99:  # Not a hyperbolic placeholder
                    from astropy.time import Time
                    from datetime import timedelta
                    tp_time = Time(orbital_params['TP'], format='jd')
                    tp_datetime = tp_time.datetime
                    # Aphelion is half period after perihelion
                    precise_aphelion = tp_datetime + timedelta(days=period_days/2)
                    # Adjust for multiple orbits if needed
                    while precise_aphelion < date:
                        precise_aphelion += timedelta(days=period_days)
                    aphelion_date_str = f"<br>Date: {precise_aphelion.strftime('%Y-%m-%d %H:%M:%S')} UTC"
                else:
                    aphelion_date_str = f"<br>Date: {aphelion_date.strftime('%Y-%m-%d')}"
            else:
                aphelion_date_str = f"<br>Date: {aphelion_date.strftime('%Y-%m-%d')}"
    elif date is not None:
        aphelion_date_str = f"<br>Date: {date.strftime('%Y-%m-%d')}"
    
    # Accuracy note
    accuracy_note = ""
    if e > 0.15:  # High eccentricity
        accuracy_note = "<br><i>Accuracy: ±0.002 AU (strong perturbations)</i>"
    elif e > 0.05:  # Moderate eccentricity
        accuracy_note = "<br><i>Accuracy: ±0.001 AU (moderate perturbations)</i>"
    else:  # Low eccentricity
        accuracy_note = "<br><i>Accuracy: ±0.0005 AU (minimal perturbations)</i>"
    
    # Determine label
    label = "Ideal Apoapsis"
    
    # Create hover text
    hover_text = f"<b>{obj_name} {label}</b>{aphelion_date_str}<br>Q={Q:.6f} AU{accuracy_note}"
    
    fig.add_trace(
        go.Scatter3d(
            x=[x],
            y=[y],
            z=[z],
            mode='markers',
            marker=dict(
                size=6,
                color=color_map(obj_name),
                symbol='square-open'
            ),
            name=f"{obj_name} {label}",
            text=[hover_text],
            customdata=[label],
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    )


