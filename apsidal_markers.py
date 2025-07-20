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
from datetime import timedelta
import plotly.graph_objects as go
from constants_new import KNOWN_ORBITAL_PERIODS

def get_orbital_period_days(body_name, semi_major_axis_au=None):
    """
    Get orbital period in days for a given body.
    
    Parameters:
        body_name: Name of the celestial body
        semi_major_axis_au: Semi-major axis in AU (optional, for validation)
    
    Returns:
        float: Orbital period in days
    """
    if body_name not in KNOWN_ORBITAL_PERIODS:
        # Use Kepler's third law as fallback
        if semi_major_axis_au:
            return 365.25 * np.sqrt(abs(semi_major_axis_au)**3)
        else:
            raise ValueError(f"Unknown body {body_name} and no semi-major axis provided")
    
    period_value = KNOWN_ORBITAL_PERIODS[body_name]
    
    # Use semi-major axis to determine if value is in years or days
    if semi_major_axis_au and semi_major_axis_au > 0.1:
        # Likely a planet or distant object - value is in years
        # (No moon orbits at > 0.1 AU from its planet)
        return period_value * 365.25
    elif period_value < 0.5:
        # Very small value - must be years (e.g., Mercury at 0.24)
        return period_value * 365.25
    elif period_value > 200:
        # Large value - already in days (e.g., Phoebe at 550.56)
        return period_value
    else:
        # Most satellites fall here - value is in days
        return period_value

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
            perihelion_date_str = f"<br>Date: {perihelion_date.strftime('%Y-%m-%d %H:%M UTC')}"
        elif e >= 1:
            perihelion_date_str = "<br>Past perihelion (hyperbolic)"
    elif date is not None:
        # Fallback to current date if position not available
        perihelion_date_str = f"<br>Date: {date.strftime('%Y-%m-%d %H:%M UTC')}"
    
    # Determine label based on context
    label = "Periapsis" 
    
    fig.add_trace(
        go.Scatter3d(
            x=[x],
            y=[y],
            z=[z],
            mode='markers',
            marker=dict(
                size=5,
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
            date_str = f"<br>Date: {apohelion_date.strftime('%Y-%m-%d %H:%M UTC')}"
    elif date is not None:
        # Fallback calculation
        orbital_period_days = 365.25 * np.sqrt(a**3)
        # This is a rough estimate
        apohelion_date = date + timedelta(days=orbital_period_days/2)
        date_str = f"<br>Date: ~{apohelion_date.strftime('%Y-%m-%d')} (estimate)"
    
    # Determine label based on context
    label = "Apoapsis"
    
    fig.add_trace(
        go.Scatter3d(
            x=[x],
            y=[y],
            z=[z],
            mode='markers',
            marker=dict(
                size=5,
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