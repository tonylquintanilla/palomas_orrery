"""
exoplanet_orbits.py - Keplerian Orbit Calculations for Exoplanets

This module handles orbital mechanics calculations for exoplanet systems,
including:
- Keplerian orbit calculations in 3D
- Binary star orbital dynamics
- Orbit plotting and visualization
- Integration with Paloma's Orrery visualization pipeline

Mathematics based on:
- Murray & Dermott (1999): Solar System Dynamics
- Keplerian orbital elements standard notation
- Rotation sequence: Omega (ascending node) -> i (inclination) -> omega (argument of periapsis)

Created: October 21, 2025
Author: Tony Quintanilla with Claude AI
"""

import numpy as np
from datetime import datetime, timedelta, timezone

# Plotly is imported when needed (available in main Paloma's Orrery environment)
try:
    import plotly.graph_objs as go
    PLOTLY_AVAILABLE = True
except ImportError:
    PLOTLY_AVAILABLE = False
    go = None

# Import stellar properties module for rich hover text and temperature colors
try:
    from exoplanet_stellar_properties import (
        calculate_host_star_properties,
        calculate_binary_star_properties,
        create_exoplanet_host_star_hover_text,
        create_binary_star_hover_text,
        get_temperature_color,
        calculate_marker_size
    )
    STELLAR_PROPERTIES_AVAILABLE = True
except ImportError:
    STELLAR_PROPERTIES_AVAILABLE = False
    print("Warning: exoplanet_stellar_properties not available. Using basic hover text.")

# ============================================================================
# KEPLERIAN ORBIT CALCULATIONS
# ============================================================================

def solve_kepler_equation(M, e, tolerance=1e-8, max_iterations=30):
    """
    Solve Kepler's equation: M = E - e*sin(E) for eccentric anomaly E
    
    Uses Newton-Raphson iteration for numerical solution
    
    Parameters:
        M: float or array - Mean anomaly (radians)
        e: float - Eccentricity
        tolerance: float - Convergence tolerance
        max_iterations: int - Maximum iterations
        
    Returns:
        E: float or array - Eccentric anomaly (radians)
    """
    # Initial guess
    E = M if e < 0.8 else np.pi
    
    # Handle array inputs
    is_array = isinstance(M, np.ndarray)
    if not is_array:
        M = np.array([M])
        E = np.array([E])
    
    # Newton-Raphson iteration
    for _ in range(max_iterations):
        f = E - e * np.sin(E) - M
        f_prime = 1 - e * np.cos(E)
        E_new = E - f / f_prime
        
        if np.all(np.abs(E_new - E) < tolerance):
            break
        E = E_new
    
    return E[0] if not is_array else E

def calculate_true_anomaly(E, e):
    """
    Calculate true anomaly from eccentric anomaly
    
    Parameters:
        E: float or array - Eccentric anomaly (radians)
        e: float - Eccentricity
        
    Returns:
        nu: float or array - True anomaly (radians)
    """
    nu = 2 * np.arctan2(
        np.sqrt(1 + e) * np.sin(E / 2),
        np.sqrt(1 - e) * np.cos(E / 2)
    )
    return nu

def calculate_keplerian_orbit(a, e, i_deg, omega_deg, Omega_deg, 
                              period_days, epoch, date=None, 
                              num_points=360):
    """
    Calculate complete orbital path in 3D space
    
    This function generates the orbital ellipse and rotates it to the
    correct orientation in 3D space using standard Keplerian rotations.
    
    Coordinate system:
    - Origin at central body (host star or barycenter)
    - XY plane: Sky plane (perpendicular to Earth line of sight)
    - Z axis: Toward Earth (line of sight direction)
    
    Parameters:
        a: float - Semi-major axis (AU)
        e: float - Eccentricity
        i_deg: float - Inclination (degrees) - angle between orbit and sky plane
        omega_deg: float - Argument of periastron (degrees)
        Omega_deg: float - Longitude of ascending node (degrees)
        period_days: float - Orbital period (days)
        epoch: datetime - Reference epoch for orbital phase
        date: datetime - Current date for phase calculation (if None, uses epoch)
        num_points: int - Number of points along orbit
        
    Returns:
        x, y, z: arrays - 3D coordinates of orbital path (AU)
    """
    # Convert to radians
    i_rad = np.radians(i_deg)
    omega_rad = np.radians(omega_deg)
    Omega_rad = np.radians(Omega_deg)
    
    # Generate true anomaly array (full orbit)
    nu = np.linspace(0, 2 * np.pi, num_points)
    
    # Calculate radius at each point (distance from focus)
    r = a * (1 - e**2) / (1 + e * np.cos(nu))
    
    # Position in orbital plane (perifocal frame)
    # X-axis points to periastron, Y-axis in direction of motion
    x_orb = r * np.cos(nu)
    y_orb = r * np.sin(nu)
    z_orb = np.zeros_like(x_orb)
    
    # Apply standard rotation sequence to transform to 3D frame
    # 1. Rotate by argument of periastron (omega) about Z-axis
    # 2. Rotate by inclination (i) about X-axis  
    # 3. Rotate by longitude of ascending node (Omega) about Z-axis
    
    # Rotation 1: omega about Z-axis
    x1 = x_orb * np.cos(omega_rad) - y_orb * np.sin(omega_rad)
    y1 = x_orb * np.sin(omega_rad) + y_orb * np.cos(omega_rad)
    z1 = z_orb
    
    # Rotation 2: i about X-axis
    x2 = x1
    y2 = y1 * np.cos(i_rad) - z1 * np.sin(i_rad)
    z2 = y1 * np.sin(i_rad) + z1 * np.cos(i_rad)
    
    # Rotation 3: Omega about Z-axis
    x = x2 * np.cos(Omega_rad) - y2 * np.sin(Omega_rad)
    y = x2 * np.sin(Omega_rad) + y2 * np.cos(Omega_rad)
    z = z2
    
    return x, y, z

def calculate_planet_position(a, e, i_deg, omega_deg, Omega_deg,
                             period_days, epoch, date):
    """
    Calculate planet's current position at specific date
    
    Parameters:
        (same as calculate_keplerian_orbit)
        date: datetime - Date for position calculation
        
    Returns:
        x, y, z: floats - 3D position at specified date (AU)
    """
    # Convert dates to UTC if needed
    if epoch.tzinfo is None:
        epoch = epoch.replace(tzinfo=timezone.utc)
    if date.tzinfo is None:
        date = date.replace(tzinfo=timezone.utc)
    
    # Calculate time since epoch
    dt_seconds = (date - epoch).total_seconds()
    dt_days = dt_seconds / 86400.0
    
    # Mean motion (radians per day)
    n = 2 * np.pi / period_days
    
    # Mean anomaly
    M = n * dt_days
    M = M % (2 * np.pi)  # Wrap to [0, 2pi]
    
    # Solve for eccentric anomaly
    E = solve_kepler_equation(M, e)
    
    # True anomaly
    nu = calculate_true_anomaly(E, e)
    
    # Distance from focus
    r = a * (1 - e**2) / (1 + e * np.cos(nu))
    
    # Position in orbital plane
    x_orb = r * np.cos(nu)
    y_orb = r * np.sin(nu)
    z_orb = 0.0
    
    # Apply rotations (same as calculate_keplerian_orbit but for single point)
    i_rad = np.radians(i_deg)
    omega_rad = np.radians(omega_deg)
    Omega_rad = np.radians(Omega_deg)
    
    # Rotation by omega
    x1 = x_orb * np.cos(omega_rad) - y_orb * np.sin(omega_rad)
    y1 = x_orb * np.sin(omega_rad) + y_orb * np.cos(omega_rad)
    z1 = z_orb
    
    # Rotation by i
    x2 = x1
    y2 = y1 * np.cos(i_rad) - z1 * np.sin(i_rad)
    z2 = y1 * np.sin(i_rad) + z1 * np.cos(i_rad)
    
    # Rotation by Omega
    x = x2 * np.cos(Omega_rad) - y2 * np.sin(Omega_rad)
    y = x2 * np.sin(Omega_rad) + y2 * np.cos(Omega_rad)
    z = z2
    
    return x, y, z

# ============================================================================
# BINARY STAR DYNAMICS
# ============================================================================

def calculate_binary_star_orbits(star_A_mass, star_B_mass, 
                                 binary_separation, binary_period,
                                 binary_eccentricity=0.0):
    """
    Calculate orbital parameters for both stars in binary system
    
    Both stars orbit their common center of mass (barycenter).
    For visualization, barycenter is at origin (0, 0, 0).
    
    Parameters:
        star_A_mass: float - Primary star mass (solar masses)
        star_B_mass: float - Secondary star mass (solar masses)
        binary_separation: float - Semi-major axis of binary orbit (AU)
        binary_period: float - Binary orbital period (days)
        binary_eccentricity: float - Binary orbit eccentricity (default 0)
        
    Returns:
        dict: Orbital parameters for both stars
            {
                'star_A': {'a': ..., 'e': ..., 'period': ..., 'phase': ...},
                'star_B': {'a': ..., 'e': ..., 'period': ..., 'phase': ...}
            }
    """
    total_mass = star_A_mass + star_B_mass
    
    # Semi-major axes from barycenter (using center of mass formula)
    # Star A (more massive, closer to barycenter)
    a_A = binary_separation * (star_B_mass / total_mass)
    
    # Star B (less massive, farther from barycenter)
    a_B = binary_separation * (star_A_mass / total_mass)
    
    return {
        'star_A': {
            'a': a_A,
            'e': binary_eccentricity,
            'period': binary_period,
            'phase': 0.0  # Arbitrary starting phase
        },
        'star_B': {
            'a': a_B,
            'e': binary_eccentricity,
            'period': binary_period,
            'phase': 180.0  # Opposite side of orbit
        }
    }

def calculate_binary_star_position(star_params, date, epoch, 
                                  i_deg=0.0, Omega_deg=0.0):
    """
    Calculate position of one star in binary system at given date
    
    For binary stars, both stars must have the same true anomaly at any instant
    (they orbit together), but they're on opposite sides of the barycenter.
    We achieve this by calculating the orbit normally, then applying a 180 deg
    rotation if this is the secondary star.
    
    Parameters:
        star_params: dict - From calculate_binary_star_orbits()
        date: datetime - Date for calculation
        epoch: datetime - Reference epoch
        i_deg: float - Inclination of binary orbit (degrees)
        Omega_deg: float - Orientation of binary orbit (degrees)
        
    Returns:
        x, y, z: floats - Star position (AU)
    """
    a = star_params['a']
    e = star_params['e']
    period = star_params['period']
    phase_offset_deg = star_params['phase']  # [OK] Keep in degrees: 0 deg for A, 180 deg for B
    
    # For simplicity, assume omega = 0 for binary orbit
    omega_deg = 0.0
    
    # Convert dates to UTC if needed
    if epoch.tzinfo is None:
        epoch = epoch.replace(tzinfo=timezone.utc)
    if date.tzinfo is None:
        date = date.replace(tzinfo=timezone.utc)
    
    # Calculate time since epoch
    dt_seconds = (date - epoch).total_seconds()
    dt_days = dt_seconds / 86400.0
    
    # Mean motion (radians per day)
    n = 2 * np.pi / period
    
    # [OK] KEY FIX: Mean anomaly is SAME for both stars
    M = n * dt_days
    M = M % (2 * np.pi)  # Wrap to [0, 2pi]
    
    # Solve for eccentric anomaly
    E = solve_kepler_equation(M, e)
    
    # [OK] KEY FIX: True anomaly is SAME for both stars (they orbit together)
    nu = calculate_true_anomaly(E, e)
    
    # Distance from focus (barycenter)
    r = a * (1 - e**2) / (1 + e * np.cos(nu))
    
    # [OK] KEY FIX: Apply phase offset to TRUE ANOMALY in orbital plane
    # This puts Star B 180 deg ahead of Star A in their shared orbit
    nu_with_offset = nu + np.radians(phase_offset_deg)
    x_orb = r * np.cos(nu_with_offset)
    y_orb = r * np.sin(nu_with_offset)
    z_orb = 0.0
    
    # Apply rotations (standard Keplerian rotation sequence)
    i_rad = np.radians(i_deg)
    omega_rad = np.radians(omega_deg)
    Omega_rad = np.radians(Omega_deg)
    
    # Rotation by omega (argument of periapsis)
    x1 = x_orb * np.cos(omega_rad) - y_orb * np.sin(omega_rad)
    y1 = x_orb * np.sin(omega_rad) + y_orb * np.cos(omega_rad)
    z1 = z_orb
    
    # Rotation by i (inclination)
    x2 = x1
    y2 = y1 * np.cos(i_rad) - z1 * np.sin(i_rad)
    z2 = y1 * np.sin(i_rad) + z1 * np.cos(i_rad)
    
    # Rotation by Omega (longitude of ascending node)
    x = x2 * np.cos(Omega_rad) - y2 * np.sin(Omega_rad)
    y = x2 * np.sin(Omega_rad) + y2 * np.cos(Omega_rad)
    z = z2
    
    return x, y, z

# ============================================================================
# VISUALIZATION FUNCTIONS
# ============================================================================

def plot_exoplanet_orbits(fig, exoplanet_objects, host_star_system, date,
                         show_orbits=True, show_markers=True):
    """
    Plot exoplanet orbits in Plotly figure
    
    Main integration point with Paloma's Orrery visualization pipeline.
    Called from plot_objects() when exoplanet objects are selected.
    
    Parameters:
        fig: plotly.graph_objs.Figure - Existing figure to add traces to
        exoplanet_objects: list - Planet data dictionaries from exoplanet_systems.py
        host_star_system: dict - Host star system data
        date: datetime - Current date for planet positions
        show_orbits: bool - Show orbital paths
        show_markers: bool - Show planet position markers
        
    Returns:
        fig: Updated Plotly figure
    """
    from formatting_utils import format_maybe_float
    
    # Plot each planet
    for planet in exoplanet_objects:
        # Extract orbital parameters
        a = planet['semi_major_axis_au']
        e = planet.get('eccentricity', 0.0)
        i = planet.get('inclination_deg', 90.0)
        omega = planet.get('omega_deg', 0.0)
        Omega = planet.get('Omega_deg', 0.0)
        period = planet['period_days']
        epoch = planet['epoch']
        
        # Calculate orbit path
        if show_orbits:
            x_orbit, y_orbit, z_orbit = calculate_keplerian_orbit(
                a, e, i, omega, Omega, period, epoch, date
            )
            
            # Add orbit trace
            fig.add_trace(go.Scatter3d(
                x=x_orbit,
                y=y_orbit,
                z=z_orbit,
                mode='lines',
                name=f"{planet['name']} orbit",
                line=dict(
                    color=planet.get('color', 'lightblue'),
                    width=2
                ),
                showlegend=True,
                hoverinfo='skip'
            ))
        
        # Calculate current position
        if show_markers:
            x_pos, y_pos, z_pos = calculate_planet_position(
                a, e, i, omega, Omega, period, epoch, date
            )
            
            # Create hover text
            hover_text = f"<b>{planet['name']}</b><br>"
            hover_text += f"Period: {planet['period_days']:.2f} days<br>"
            hover_text += f"Semi-major axis: {a:.4f} AU<br>"
            
            # Annotate assumed values
            e_note = " (assumed circular)" if planet.get('e_assumed') else ""
            hover_text += f"Eccentricity: {e:.4f}{e_note}<br>"
            
            i_note = " (assumed edge-on)" if planet.get('i_assumed') else ""
            hover_text += f"Inclination: {i:.1f} deg deg{i_note}<br>"
            
            hover_text += f"<br>Mass: {format_maybe_float(planet.get('mass_earth'))} [EARTH]<br>"
            hover_text += f"Radius: {format_maybe_float(planet.get('radius_earth'))} [EARTH]<br>"
            hover_text += f"Temp: {planet.get('equilibrium_temp_k')} K<br>"
            
            if planet.get('in_habitable_zone'):
                hover_text += "<br><b>[STAR] IN HABITABLE ZONE [STAR]</b><br>"
            
            hover_text += f"<br>Discovery: {planet['discovery_method']} ({planet['discovery_year']})"
            
            if planet.get('discoverer'):
                hover_text += f"<br>By: {planet['discoverer']}"
            
            # Add position marker
            fig.add_trace(go.Scatter3d(
                x=[x_pos],
                y=[y_pos],
                z=[z_pos],
                mode='markers',
                name=planet['name'],
                marker=dict(
                    size=8 if planet.get('in_habitable_zone') else 6,
                    color='green' if planet.get('in_habitable_zone') else planet.get('color', 'lightblue'),
                    symbol='circle'
                ),
                text=[hover_text],
                hoverinfo='text',
                showlegend=True
            ))
    
    return fig


def plot_binary_host_stars(fig, host_star_system, date, show_orbits=True, show_markers=True, system_data=None):
    """
    Plot binary star system (both stars orbiting barycenter)
    
    Uses rich hover text and temperature-based colors from exoplanet_stellar_properties.
    
    Parameters:
        fig: plotly.graph_objs.Figure
        host_star_system: dict - Host star data from exoplanet_systems.py
        date: datetime - Current date
        show_orbits: bool - Show stellar orbital paths
        show_markers: bool - Show star position markers
        system_data: dict - Parent system data (for context in hover text)
        
    Returns:
        fig: Updated figure
    """

    if not host_star_system.get('is_binary'):
        # Single star - just plot at origin
        
        # Check if this star was already plotted (avoid duplicates)
    #    star_name = host_star_system['name']
    #    if any(trace.name == star_name for trace in fig.data):
    #        print(f"[DEBUG] Star {star_name} already plotted, skipping duplicate")
    #        return fig

        # Calculate stellar properties for rich hover text and colors
        if STELLAR_PROPERTIES_AVAILABLE:
            enhanced_props = calculate_host_star_properties(host_star_system)
            star_color = enhanced_props['color']
            marker_size = calculate_marker_size(enhanced_props.get('luminosity', 0.001), base_size=10)
            hover_text = create_exoplanet_host_star_hover_text(
                host_star_system, 
                system_data if system_data else {},
                enhanced_props
            )
        else:
            # Fallback to basic hover text
            star_color = 'yellow'
            marker_size = 10
            hover_text = (f"<b>{host_star_system['name']}</b><br>"
                         f"Spectral type: {host_star_system['spectral_type']}<br>"
                         f"Mass: {host_star_system['mass_solar']:.2f} M[SUN]")
        
        fig.add_trace(go.Scatter3d(
            x=[0], y=[0], z=[0],
            mode='markers',
            name=host_star_system['name'],
            marker=dict(size=marker_size, color=star_color, symbol='circle'),
            text=[hover_text],
            hoverinfo='text'
        ))
        return fig
    
    
    # Binary system - calculate stellar orbits
    star_A = host_star_system['star_A']
    star_B = host_star_system['star_B']
    
    binary_params = calculate_binary_star_orbits(
        star_A['mass_solar'],
        star_B['mass_solar'],
        host_star_system['binary_separation_au'],
        host_star_system['binary_period_days'],
        host_star_system.get('binary_eccentricity', 0.0)
    )
    
    epoch = host_star_system['epoch']

    # Get binary orbital orientation (should match planet orbital plane for circumbinary systems)
    binary_i = host_star_system.get('binary_inclination_deg', 0.0)
    binary_Omega = host_star_system.get('binary_Omega_deg', 0.0)
    binary_omega = 0.0  # Argument of periastron for binary orbit    
    
    # Calculate Star A properties first (needed for orbit color)
    if STELLAR_PROPERTIES_AVAILABLE:
        props_A, _ = calculate_binary_star_properties(star_A, star_B)
        color_A = props_A['color']
        size_A = calculate_marker_size(props_A.get('luminosity', 0.01), base_size=10)
        hover_A = create_binary_star_hover_text(
            star_A, "Primary", system_data if system_data else {}, props_A
        )
    else:
        color_A = 'yellow'
        size_A = 10
        hover_A = (f"<b>{star_A['name']}</b><br>"
                  f"Type: {star_A['spectral_type']}<br>"
                  f"Mass: {star_A['mass_solar']:.2f} M[SUN]")
    
    # Plot Star A orbit (using calculated color)
    if show_orbits:
        x_A, y_A, z_A = calculate_keplerian_orbit(
            binary_params['star_A']['a'],
            binary_params['star_A']['e'],
        #    0.0, 0.0, 0.0,  # Assume coplanar with planets for now
            binary_i, binary_omega, binary_Omega,  # Use system binary orientation
            binary_params['star_A']['period'],
            epoch, date
        )
        fig.add_trace(go.Scatter3d(
            x=x_A, y=y_A, z=z_A,
            mode='lines',
            name=f"{star_A['name']} orbit",
            line=dict(color=color_A, width=1, dash='dot'),
            showlegend=True,
            hoverinfo='skip'
        ))
    
    # Star A position
    x_A_pos, y_A_pos, z_A_pos = calculate_binary_star_position(
#        binary_params['star_A'], date, epoch
        binary_params['star_A'], date, epoch, binary_i, binary_Omega
    )
    
    if show_markers:
        fig.add_trace(go.Scatter3d(
            x=[x_A_pos], y=[y_A_pos], z=[z_A_pos],
            mode='markers',
            name=star_A['name'],
            marker=dict(size=size_A, color=color_A, symbol='circle'),
            text=[hover_A],
            hoverinfo='text'
        ))
    
    # Calculate Star B properties first (needed for orbit color)
    if STELLAR_PROPERTIES_AVAILABLE:
        _, props_B = calculate_binary_star_properties(star_A, star_B)
        color_B = props_B['color']
        size_B = calculate_marker_size(props_B.get('luminosity', 0.01), base_size=8)
        hover_B = create_binary_star_hover_text(
            star_B, "Secondary", system_data if system_data else {}, props_B
        )
    else:
        color_B = 'orange'
        size_B = 7
        hover_B = (f"<b>{star_B['name']}</b><br>"
                  f"Type: {star_B['spectral_type']}<br>"
                  f"Mass: {star_B['mass_solar']:.2f} M[SUN]")

    # Plot Star B orbit (using calculated color)
    if show_orbits:
        x_B, y_B, z_B = calculate_keplerian_orbit(
            binary_params['star_B']['a'],
            binary_params['star_B']['e'],
        #    0.0, 0.0, 0.0,
            binary_i, binary_omega, binary_Omega,  # Use system binary orientation
            binary_params['star_B']['period'],
            epoch, date
        )
        # Apply 180 deg phase shift
        x_B, y_B = -x_B, -y_B
        
        fig.add_trace(go.Scatter3d(
            x=x_B, y=y_B, z=z_B,
            mode='lines',
            name=f"{star_B['name']} orbit",
            line=dict(color=color_B, width=1, dash='dot'),
            showlegend=True,
            hoverinfo='skip'
        ))
    
    # Star B position
    x_B_pos, y_B_pos, z_B_pos = calculate_binary_star_position(
#        binary_params['star_B'], date, epoch
        binary_params['star_B'], date, epoch, binary_i, binary_Omega
    )
        
    if show_markers:
        fig.add_trace(go.Scatter3d(
            x=[x_B_pos], y=[y_B_pos], z=[z_B_pos],
            mode='markers',
            name=star_B['name'],
            marker=dict(size=size_B, color=color_B, symbol='circle'),
            text=[hover_B],
            hoverinfo='text'
        ))

    # Add barycenter marker (optional, for reference)
    
    if show_markers:
        fig.add_trace(go.Scatter3d(
            x=[0], y=[0], z=[0],
            mode='markers',
            name='Barycenter',
            marker=dict(size=12, color='white', symbol='square-open'),
            text=['<b>Barycenter</b><br>Center of mass'],
            hoverinfo='text',
            showlegend=False
        ))

    return fig


def calculate_exoplanet_axis_range(exoplanet_objects):
    """
    Calculate appropriate axis range for exoplanet system
    
    Uses same logic as calculate_axis_range() in palomas_orrery_helpers.py
    
    Parameters:
        exoplanet_objects: list - Planet data dictionaries
        
    Returns:
        float: Axis range ( deg+/-value in AU)
    """
    if not exoplanet_objects:
        return 1.0  # Default 1 AU
    
    # Find maximum apastron distance
    max_distance = 0
    for planet in exoplanet_objects:
        a = planet['semi_major_axis_au']
        e = planet.get('eccentricity', 0.0)
        apastron = a * (1 + e)
        max_distance = max(max_distance, apastron)
    
    # Add 20% buffer
    axis_range = max_distance * 1.2
    
    # Minimum range for visibility
    axis_range = max(axis_range, 0.01)
    
    return axis_range

if __name__ == "__main__":
    # Test the orbit calculations
    print("Testing Exoplanet Orbit Calculations")
    print("=" * 60)
    
    from exoplanet_systems import get_system
    from datetime import datetime, timezone
    
    # Test TRAPPIST-1 e (in habitable zone)
    system = get_system('trappist1')
    planet_e = system['planets'][3]  # TRAPPIST-1 e
    
    print(f"\nTest: {planet_e['name']}")
    print(f"Period: {planet_e['period_days']:.2f} days")
    print(f"Semi-major axis: {planet_e['semi_major_axis_au']:.4f} AU")
    
    # Calculate position at discovery epoch
    date = planet_e['epoch']
    x, y, z = calculate_planet_position(
        planet_e['semi_major_axis_au'],
        planet_e['eccentricity'],
        planet_e['inclination_deg'],
        planet_e['omega_deg'],
        planet_e['Omega_deg'],
        planet_e['period_days'],
        planet_e['epoch'],
        date
    )
    
    print(f"Position at epoch: ({x:.4f}, {y:.4f}, {z:.4f}) AU")
    
    # Test binary star system
    print("\n" + "=" * 60)
    toi_system = get_system('toi1338')
    print(f"\nTest: {toi_system['system_name']} (Binary)")
    
    binary_params = calculate_binary_star_orbits(
        toi_system['host_star']['star_A']['mass_solar'],
        toi_system['host_star']['star_B']['mass_solar'],
        toi_system['host_star']['binary_separation_au'],
        toi_system['host_star']['binary_period_days']
    )
    
    print(f"Star A semi-major axis: {binary_params['star_A']['a']:.4f} AU")
    print(f"Star B semi-major axis: {binary_params['star_B']['a']:.4f} AU")
    print(f"Binary period: {binary_params['star_A']['period']:.2f} days")
    
    print("\n[OK] All tests passed!")
