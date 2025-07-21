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

# In apsidal_markers.py, add these functions:

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
    start_date, end_date = date_range
    
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
    
    # Convert string dates to datetime objects
    near_dates = [datetime.strptime(d, '%Y-%m-%d') for d in near_dates]
    far_dates = [datetime.strptime(d, '%Y-%m-%d') for d in far_dates]
    
    # Filter dates within the display range
    near_dates = [d for d in near_dates if start_date <= d <= end_date]
    far_dates = [d for d in far_dates if start_date <= d <= end_date]
    
    # Add markers for near points (perihelion/perigee)
    for date in near_dates:
        date_str = date.strftime('%Y-%m-%d')
        if date_str in positions_dict:
            pos = positions_dict[date_str]
            
            # Calculate distance from center
            distance_au = np.sqrt(pos['x']**2 + pos['y']**2 + pos['z']**2)
    #        distance_km = distance_au * 149597870.7  # Convert AU to km

            fig.add_trace(
                go.Scatter3d(
                    x=[pos['x']],
                    y=[pos['y']],
                    z=[pos['z']],
            #        mode='markers+text',
                    mode='markers',                    
                    marker=dict(
                        size=8,
            #            color=color_map(obj_name),
                        color='white',                        
                        symbol='square-open',
                #        line=dict(color='white', width=2)
                    ),
                    text=f"⊙ {obj_name} {near_label}<br>{date_str} (actual)",
                    textposition='top center',
                    textfont=dict(size=10, color=color_map(obj_name)),
                    name=f"{obj_name} Actual {near_label}",
                    hovertemplate=(
                        f"<b>{obj_name} at {near_label}</b><br>"
                        f"Date: {date_str} (actual)<br>"
                        f"Distance from {center_body}: {distance_au:.3f} AU<br>"        # originally .6f
                        "<extra></extra>"
                    ),
                    showlegend=True
                )
            )
    
    # Add markers for far points (aphelion/apogee)
    for date in far_dates:
        date_str = date.strftime('%Y-%m-%d')
        if date_str in positions_dict:
            pos = positions_dict[date_str]
            
            # Calculate distance from center
            distance_au = np.sqrt(pos['x']**2 + pos['y']**2 + pos['z']**2)
    #        distance_km = distance_au * 149597870.7  # Convert AU to km

            fig.add_trace(
                go.Scatter3d(
                    x=[pos['x']],
                    y=[pos['y']],
                    z=[pos['z']],
            #        mode='markers+text',
                    mode='markers',                    
                    marker=dict(
                        size=8,
                #        color=color_map(obj_name),
                        color='white',                        
                        symbol='square-open',
                #        line=dict(color=color_map(obj_name), width=2)
                    ),
                    text=f"◯ {obj_name} {far_label}<br>{date_str} (actual)",
                    textposition='top center',
                    textfont=dict(size=10, color=color_map(obj_name)),
                    name=f"{obj_name} Actual {far_label}",
                    hovertemplate=(
                        f"<b>{obj_name} at {far_label}</b><br>"
                        f"Date: {date_str} (actual)<br>"
                        f"Distance from {center_body}: {distance_au:.3f} AU<br>"
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
    start_date, end_date = date_range
    
    # Get all apsidal dates
    if is_satellite:
        all_dates = params.get('perigee_dates', []) + params.get('apogee_dates', [])
    else:
        all_dates = params.get('perihelion_dates', []) + params.get('aphelion_dates', [])
    
    # Convert and filter dates
    for date_str in all_dates:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        if start_date <= date_obj <= end_date:
            # Fetch position for this date
            pos_data = fetch_position(obj_id, date_obj, center_id=center_id, id_type=id_type)
            if pos_data and 'x' in pos_data:
                positions[date_str] = pos_data
    
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
    Add a perihelion/perigee marker to the plot with accurate date calculation.
    
    Parameters:
        fig: Plotly figure object
        x, y, z: Coordinates of perihelion point
        obj_name: Name of the object
        a: Semi-major axis
        e: Eccentricity
        date: Current date
        current_position: Dict with 'x', 'y', 'z' keys for current position
        orbital_params: Dict with orbital elements
        color_map: Function to get color for object
        q: Perihelion distance (optional, will be calculated if not provided)
    
    Returns:
        None (modifies fig in place)
    """
    # Calculate perihelion distance if not provided
    if q is None:
        q = a * (1 - e) if e < 1 else abs(a) * (e - 1)
    
    # Calculate perihelion date
    perihelion_date_str = ""
    if date is not None and current_position is not None:
        perihelion_date, _ = calculate_apsidal_dates(
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
            perihelion_date_str = f"<br>Date: {perihelion_date.strftime('%Y-%m-%d')}"
        elif e >= 1:
            perihelion_date_str = "<br>Past perihelion (hyperbolic)"
    elif date is not None:
        # Fallback to current date if position not available
        perihelion_date_str = f"<br>Date: {date.strftime('%Y-%m-%d')}"
    
    # Determine label based on context
    label = "Ideal Periapsis" 
    
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
            text=[f"{obj_name} {label}{perihelion_date_str}<br>q={q:.3f} AU"],
            customdata=[label],
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    )


def add_apohelion_marker(fig, x, y, z, obj_name, a, e, date, current_position,
                        orbital_params, color_map):
    """
    Add an apohelion/apogee marker to the plot with accurate date calculation.
    
    Parameters:
        fig: Plotly figure object
        x, y, z: Coordinates of apohelion point
        obj_name: Name of the object
        a: Semi-major axis
        e: Eccentricity
        date: Current date
        current_position: Dict with 'x', 'y', 'z' keys for current position
        orbital_params: Dict with orbital elements
        color_map: Function to get color for object
    
    Returns:
        None (modifies fig in place)
    """
    # Skip apohelion for hyperbolic orbits
    if e >= 1:
        return
    
    # Calculate apohelion distance
    Q = a * (1 + e)
    
    # Calculate apohelion date
    date_str = ""
    if date is not None and current_position is not None:
        _, apohelion_date = calculate_apsidal_dates(
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
        
        if apohelion_date is not None:
            date_str = f"<br>Date: {apohelion_date.strftime('%Y-%m-%d')}"
    elif date is not None:
        # Fallback calculation
        orbital_period_days = 365.25 * np.sqrt(a**3)
        # This is a rough estimate
        apohelion_date = date + timedelta(days=orbital_period_days/2)
        date_str = f"<br>Date: ~{apohelion_date.strftime('%Y-%m-%d')} (estimate)"
    
    # Determine label based on context
    label = "Ideal Apoapsis"
    
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
            text=[f"{obj_name} {label}{date_str}<br>Q={Q:.3f} AU"],
            customdata=[label],
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    )

