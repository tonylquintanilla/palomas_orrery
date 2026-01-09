"""
sgr_a_visualization_core.py
Core visualization module for S-Stars orbiting Sagittarius A*.

Stage 1: Static visualization - elliptical orbits around the black hole.
Stage 2: Animation with mean anomaly stepping.
Stage 3: Relativistic precession (rosette pattern).
Stage 4: Multiple stars, historical events.

Part of Paloma's Orrery - Data Preservation is Climate Action
"""

import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from save_utils import show_and_save

# Import our data module
from sgr_a_star_data import (
    S_STAR_CATALOG, SGR_A_MASS_SOLAR, SCHWARZSCHILD_RADIUS_AU,
    get_star_data, list_stars,
    calculate_periapsis_au, calculate_apoapsis_au,
    calculate_periapsis_velocity, format_velocity,
    calculate_schwarzschild_precession_per_orbit,
    solve_kepler_equation, eccentric_to_true_anomaly,
    radius_from_true_anomaly,
    # New: Temperature-based colors and rich hover text
    get_star_color, get_star_temperature, create_star_hover_text,
    calculate_orbital_velocity
)

# =============================================================================
# ORBIT GENERATION
# =============================================================================

def generate_orbit_points(star_data, num_points=360, precession_offset_deg=0.0):
    """
    Generate 3D orbit points for a star.
    
    Args:
        star_data: Dictionary with orbital elements
        num_points: Number of points around the orbit
        precession_offset_deg: Additional rotation to argument of periapsis (for GR precession)
    
    Returns:
        x, y, z: Arrays of orbit coordinates in AU (centered on Sgr A*)
    """
    # Extract orbital elements
    a = star_data['a_au']
    e = star_data['e']
    i = np.radians(star_data['inclination_deg'])
    omega = np.radians(star_data['arg_periapsis_deg'] + precession_offset_deg)  # Argument of periapsis
    Omega = np.radians(star_data['asc_node_deg'])  # Longitude of ascending node
    
    # Generate true anomaly values (0 to 2*pi)
    nu_values = np.linspace(0, 2*np.pi, num_points)
    
    # Calculate radius at each true anomaly
    # r = a(1-e^2) / (1 + e*cos(nu))
    p = a * (1 - e**2)  # Semi-latus rectum
    r_values = p / (1 + e * np.cos(nu_values))
    
    # Position in orbital plane (x' along periapsis, y' perpendicular)
    x_orbital = r_values * np.cos(nu_values)
    y_orbital = r_values * np.sin(nu_values)
    
    # Rotation matrices to convert from orbital plane to 3D space
    # 1. Rotate by argument of periapsis (omega)
    # 2. Rotate by inclination (i)
    # 3. Rotate by longitude of ascending node (Omega)
    
    # Combined rotation (standard orbital mechanics convention)
    cos_omega = np.cos(omega)
    sin_omega = np.sin(omega)
    cos_i = np.cos(i)
    sin_i = np.sin(i)
    cos_Omega = np.cos(Omega)
    sin_Omega = np.sin(Omega)
    
    # Rotation matrix elements
    # x = (cos_Omega*cos_omega - sin_Omega*sin_omega*cos_i)*x' + (-cos_Omega*sin_omega - sin_Omega*cos_omega*cos_i)*y'
    # y = (sin_Omega*cos_omega + cos_Omega*sin_omega*cos_i)*x' + (-sin_Omega*sin_omega + cos_Omega*cos_omega*cos_i)*y'
    # z = (sin_omega*sin_i)*x' + (cos_omega*sin_i)*y'
    
    Px = cos_Omega * cos_omega - sin_Omega * sin_omega * cos_i
    Qx = -cos_Omega * sin_omega - sin_Omega * cos_omega * cos_i
    
    Py = sin_Omega * cos_omega + cos_Omega * sin_omega * cos_i
    Qy = -sin_Omega * sin_omega + cos_Omega * cos_omega * cos_i
    
    Pz = sin_omega * sin_i
    Qz = cos_omega * sin_i
    
    # Transform to 3D coordinates
    x = Px * x_orbital + Qx * y_orbital
    y = Py * x_orbital + Qy * y_orbital
    z = Pz * x_orbital + Qz * y_orbital
    
    return x, y, z

def generate_position_at_true_anomaly(star_data, true_anomaly_rad, precession_offset_deg=0.0):
    """
    Generate 3D position for a star at a specific true anomaly.
    
    Returns:
        x, y, z: Position in AU
        r: Distance from Sgr A* in AU
    """
    a = star_data['a_au']
    e = star_data['e']
    i = np.radians(star_data['inclination_deg'])
    omega = np.radians(star_data['arg_periapsis_deg'] + precession_offset_deg)
    Omega = np.radians(star_data['asc_node_deg'])
    
    nu = true_anomaly_rad
    
    # Radius
    p = a * (1 - e**2)
    r = p / (1 + e * np.cos(nu))
    
    # Position in orbital plane
    x_orbital = r * np.cos(nu)
    y_orbital = r * np.sin(nu)
    
    # Rotation (same as above)
    cos_omega = np.cos(omega)
    sin_omega = np.sin(omega)
    cos_i = np.cos(i)
    sin_i = np.sin(i)
    cos_Omega = np.cos(Omega)
    sin_Omega = np.sin(Omega)
    
    Px = cos_Omega * cos_omega - sin_Omega * sin_omega * cos_i
    Qx = -cos_Omega * sin_omega - sin_Omega * cos_omega * cos_i
    Py = sin_Omega * cos_omega + cos_Omega * sin_omega * cos_i
    Qy = -sin_Omega * sin_omega + cos_Omega * cos_omega * cos_i
    Pz = sin_omega * sin_i
    Qz = cos_omega * sin_i
    
    x = Px * x_orbital + Qx * y_orbital
    y = Py * x_orbital + Qy * y_orbital
    z = Pz * x_orbital + Qz * y_orbital
    
    return x, y, z, r

# =============================================================================
# VISUALIZATION COMPONENTS
# =============================================================================

def create_sgr_a_marker(scale_factor=50):
    """
    Create the Sagittarius A* black hole marker.
    
    Since the actual Schwarzschild radius (~0.08 AU) would be invisible
    at orbit scales (~1000 AU), we create an artistic representation.
    
    Accretion disk based on observations:
    - Bright inner ring: ~5.2x Schwarzschild radius (EHT 2022)
    - Cool outer disk: extends to ~1000 AU (ALMA 2019, Murchikova et al.)
    
    Trace order matters for rendering:
    - Lensing traces added FIRST (render behind)
    - Black hole sphere added LAST (render in front)
    
    Args:
        scale_factor: How much larger than Rs to draw the marker
    
    Returns:
        List of Plotly traces for Sgr A*
    """
    traces = []
    
    # Effective visual radius (not to physical scale)
    visual_radius = SCHWARZSCHILD_RADIUS_AU * scale_factor
    
    # Disk dimensions (needed for lensing)
    disk_inner = visual_radius * 1.2
    disk_outer = visual_radius * 6
    
    # Photon sphere radius (where light orbits)
    photon_sphere = visual_radius * 1.5
    
    # ==========================================================================
    # GRAVITATIONAL LENSING EFFECT - Added FIRST so it renders BEHIND
    # ==========================================================================
    # Light from the back of the accretion disk bends around the black hole.
    # We create a dome of rings above and below the disk that represent
    # lensed light. This looks similar from any horizontal viewing angle.
    
    n_dome_rings = 10
    lensing_hover = "Gravitational lensing: light from far side of disk bent around the black hole"
    
    # First lensing ring gets the legend entry
    first_lensing = True
    
    for i in range(n_dome_rings):
        t = (i + 1) / (n_dome_rings + 1)
        
        height = visual_radius * 1.8 * (1 - np.cos(t * np.pi / 2))
        ring_radius = photon_sphere + (disk_outer - photon_sphere) * (1 - t * 0.7)
        
        brightness = 0.4 + 0.6 * t
        r_col = int(255 * brightness)
        g_col = int(180 * brightness)
        b_col = int(80 * brightness)
        alpha = 0.3 + 0.4 * t
        width = 1.5 + 2 * t
        
        theta_ring = np.linspace(0, 2*np.pi, 60)
        
        # Ring ABOVE the disk
        traces.append(go.Scatter3d(
            x=ring_radius * np.cos(theta_ring),
            y=ring_radius * np.sin(theta_ring),
            z=np.full_like(theta_ring, height),
            mode='lines',
            line=dict(
                color=f'rgba({r_col},{g_col},{b_col},{alpha})',
                width=width
            ),
            hovertext=lensing_hover,
            hoverinfo='text',
            name='Gravitational Lensing' if first_lensing else None,
            legendgroup='lensing',
            showlegend=first_lensing
        ))
        first_lensing = False
        
        # Ring BELOW the disk (mirror)
        traces.append(go.Scatter3d(
            x=ring_radius * np.cos(theta_ring),
            y=ring_radius * np.sin(theta_ring),
            z=np.full_like(theta_ring, -height),
            mode='lines',
            line=dict(
                color=f'rgba({r_col},{g_col},{b_col},{alpha})',
                width=width
            ),
            hovertext=lensing_hover,
            hoverinfo='text',
            legendgroup='lensing',
            showlegend=False
        ))
    
    # ==========================================================================
    # ACCRETION DISK - Based on observations
    # ==========================================================================
    r_disk = np.linspace(disk_inner, disk_outer, 30)
    theta_disk = np.linspace(0, 2*np.pi, 60)
    R, Theta = np.meshgrid(r_disk, theta_disk)
    
    X_disk = R * np.cos(Theta)
    Y_disk = R * np.sin(Theta)
    Z_disk = np.zeros_like(R)
    
    color_values = 1 - (R - disk_inner) / (disk_outer - disk_inner)
    
    disk_hover = (
        "<b>Accretion Disk</b><br><br>"
        "<b>Observed Properties:</b><br>"
        "Inner bright ring: ~5x Schwarzschild radius<br>"
        "Cool outer disk: extends to ~1000 AU<br>"
        "Temperature: 10,000 K (outer) to millions K (inner)<br>"
        "Mass: ~0.1 Jupiter masses of hydrogen gas<br><br>"
        "<b>Physics:</b><br>"
        "Gas spirals inward, losing angular momentum<br>"
        "Friction heats gas to millions of degrees<br>"
        "Emits X-rays, radio, and infrared light<br><br>"
        "<b>Gravitational Lensing:</b><br>"
        "Light from the far side bends around the black hole<br>"
        "Creates the iconic 'wrapped' appearance<br><br>"
        "<i>First imaged by ALMA 2019 (Murchikova et al.)</i><br>"
        "<i>EHT captured bright inner ring, May 2022</i>"
    )
    
    traces.append(go.Surface(
        x=X_disk, y=Y_disk, z=Z_disk,
        surfacecolor=color_values,
        colorscale=[
            [0.0, 'rgba(50,20,0,0.3)'],
            [0.3, 'rgba(150,60,0,0.5)'],
            [0.6, 'rgba(255,150,0,0.7)'],
            [1.0, 'rgba(255,200,100,0.9)']
        ],
        showscale=False,
        opacity=0.7,
        name='Accretion Disk',
        text=disk_hover,
        hoverinfo='text',
        showlegend=True
    ))
    
    # ==========================================================================
    # PHOTON RING - at the photon sphere
    # ==========================================================================
    photon_ring_theta = np.linspace(0, 2*np.pi, 80)
    
    traces.append(go.Scatter3d(
        x=photon_sphere * np.cos(photon_ring_theta),
        y=photon_sphere * np.sin(photon_ring_theta),
        z=np.zeros_like(photon_ring_theta),
        mode='lines',
        line=dict(color='rgba(255,230,180,0.9)', width=3),
        name='Photon Ring',
        hovertext=(
            "Photon Ring: cross-section of the photon sphere at 1.5x Schwarzschild radius. "
            "Light can orbit here, but orbits are unstable - any perturbation sends photons "
            "falling into the black hole or escaping to infinity."
        ),
        hoverinfo='text',
        showlegend=True
    ))
    
    # ==========================================================================
    # BLACK HOLE SPHERE & EVENT HORIZON - Added LAST so it renders IN FRONT
    # ==========================================================================
    u = np.linspace(0, 2*np.pi, 30)
    v = np.linspace(0, np.pi, 20)
    
    x = visual_radius * np.outer(np.cos(u), np.sin(v))
    y = visual_radius * np.outer(np.sin(u), np.sin(v))
    z = visual_radius * np.outer(np.ones(np.size(u)), np.cos(v))
    
    sgr_a_hover = (
        "<b>Sagittarius A* (Sgr A*)</b><br><br>"
        f"<b>Supermassive Black Hole</b><br>"
        f"Mass: 4.154 million solar masses<br>"
        f"Schwarzschild Radius: {SCHWARZSCHILD_RADIUS_AU:.4f} AU ({SCHWARZSCHILD_RADIUS_AU * 149597870.7:.0f} km)<br>"
        f"Distance from Earth: 26,670 light-years<br><br>"
        f"<b>Visual Representation (scaled {scale_factor}x):</b><br>"
        f"Black sphere: Event horizon (artistic)<br>"
        f"Red sphere: Actual size to scale<br>"
        f"White ring: Event horizon boundary<br>"
        f"Orange disk: Accretion disk<br><br>"
        f"<i>First imaged by Event Horizon Telescope, May 2022</i>"
    )
    
    # Black sphere - full opacity to occlude lensing behind it
    traces.append(go.Surface(
        x=x, y=y, z=z,
        colorscale=[[0, 'rgb(10,0,20)'], [1, 'rgb(30,0,50)']],
        showscale=False,
        opacity=1.0,  # Full opacity to ensure it occludes
        name='Sgr A* (Black Hole)',
        text=sgr_a_hover,
        hoverinfo='text',
        showlegend=True
    ))
    
    # Event horizon boundary ring (white for visibility)
    theta = np.linspace(0, 2*np.pi, 100)
    traces.append(go.Scatter3d(
        x=visual_radius * np.cos(theta),
        y=visual_radius * np.sin(theta),
        z=np.zeros_like(theta),
        mode='lines',
        line=dict(color='white', width=2),
        name='Event Horizon',
        hovertext="Event Horizon boundary (scaled for visibility)",
        hoverinfo='text',
        showlegend=True
    ))
    
    # ==========================================================================
    # ACTUAL SIZE BLACK HOLE - True Schwarzschild radius for comparison
    # ==========================================================================
    # This tiny sphere shows the real size of the event horizon relative to
    # the S-star orbits. At ~0.08 AU, it's smaller than Mercury's orbit!
    # S4714's periapsis of 12.6 AU is still ~150x the Schwarzschild radius.
    
    actual_radius = SCHWARZSCHILD_RADIUS_AU  # ~0.0828 AU
    
    # Create sphere at actual scale
    x_actual = actual_radius * np.outer(np.cos(u), np.sin(v))
    y_actual = actual_radius * np.outer(np.sin(u), np.sin(v))
    z_actual = actual_radius * np.outer(np.ones(np.size(u)), np.cos(v))
    
    actual_hover = (
        "<b>Sgr A* - Actual Size</b><br><br>"
        f"<b>True Schwarzschild Radius:</b><br>"
        f"{SCHWARZSCHILD_RADIUS_AU:.4f} AU ({SCHWARZSCHILD_RADIUS_AU * 149597870.7:.0f} km)<br><br>"
        f"<b>For comparison:</b><br>"
        f"Mercury's orbit: 0.39 AU<br>"
        f"Sun's radius: 0.00465 AU<br>"
        f"S4714 periapsis: 12.6 AU (~150x this size)<br>"
        f"S2 periapsis: 120 AU (~1,450x this size)<br><br>"
        f"<i>The artistic representation is {scale_factor}x larger</i><br>"
        f"<i>Red color is for illustration only - black holes emit no visible light</i>"
    )
    
    # Bright red sphere - stands out against the purple/orange
    traces.append(go.Surface(
        x=x_actual, y=y_actual, z=z_actual,
        colorscale=[[0, 'rgb(200,0,0)'], [1, 'rgb(255,50,50)']],
        showscale=False,
        opacity=1.0,
        name='Sgr A* (Actual Scale)',
        text=actual_hover,
        hoverinfo='text',
        showlegend=True
    ))
    
    return traces

def create_orbit_trace(star_name, star_data, show_periapsis=True):
    """
    Create the orbital path trace for a star.
    
    Returns:
        List of Plotly traces
    """
    traces = []
    
    # Get temperature-based color (consistent with exoplanet stars)
    star_color = get_star_color(star_data)
    
    # Generate orbit
    x, y, z = generate_orbit_points(star_data)
    
    # Main orbit line
    traces.append(go.Scatter3d(
        x=x, y=y, z=z,
        mode='lines',
        line=dict(
            color=star_color,
            width=3
        ),
        name=star_data['name'],
        hovertemplate=(
            f"<b>{star_data['name']}</b><br>"
            f"Period: {star_data['period_yrs']:.1f} years<br>"
            f"Eccentricity: {star_data['e']:.3f}<br>"
            "<extra></extra>"
        )
    ))
    
    if show_periapsis:
        # Mark periapsis (closest approach) - true anomaly = 0
        x_peri, y_peri, z_peri, r_peri = generate_position_at_true_anomaly(star_data, 0.0)
        v_peri = calculate_periapsis_velocity(star_data['a_au'], star_data['e'])
        
        traces.append(go.Scatter3d(
            x=[x_peri], y=[y_peri], z=[z_peri],
            mode='markers',
            marker=dict(
                size=8,
                color=star_color,
                symbol='diamond'
            ),
            name=f'{star_name} Periapsis',
            hovertemplate=(
                f"<b>{star_data['name']} Periapsis</b><br>"
                f"Distance: {r_peri:.1f} AU<br>"
                f"Velocity: {format_velocity(v_peri)}<br>"
                "<extra></extra>"
            ),
            showlegend=False
        ))
        
        # Mark apoapsis (farthest point) - true anomaly = pi
        x_apo, y_apo, z_apo, r_apo = generate_position_at_true_anomaly(star_data, np.pi)
        
        traces.append(go.Scatter3d(
            x=[x_apo], y=[y_apo], z=[z_apo],
            mode='markers',
            marker=dict(
                size=5,
                color=star_color,
                symbol='circle',
                opacity=0.5
            ),
            name=f'{star_name} Apoapsis',
            hovertemplate=(
                f"<b>{star_data['name']} Apoapsis</b><br>"
                f"Distance: {r_apo:.1f} AU<br>"
                "<extra></extra>"
            ),
            showlegend=False
        ))
    
    return traces

def create_star_marker(star_name, star_data, true_anomaly_rad=0.0, precession_offset_deg=0.0):
    """
    Create a marker showing the star's current position.
    
    Uses temperature-based colors (blackbody) and rich hover text
    consistent with exoplanet host star visualization.
    
    Args:
        star_name: Key from catalog
        star_data: Star data dictionary
        true_anomaly_rad: Current position (radians from periapsis)
        precession_offset_deg: Accumulated precession
    
    Returns:
        Plotly Scatter3d trace
    """
    x, y, z, r = generate_position_at_true_anomaly(
        star_data, true_anomaly_rad, precession_offset_deg
    )
    
    # Calculate current velocity (vis-viva)
    v = calculate_orbital_velocity(star_data['a_au'], r)
    
    # Get temperature-based color (consistent with exoplanet stars)
    star_color = get_star_color(star_data)
    
    # Create rich hover text
    hover_text = create_star_hover_text(
        star_name, star_data,
        current_distance_au=r,
        current_velocity_km_s=v
    )
    
    return go.Scatter3d(
        x=[x], y=[y], z=[z],
        mode='markers',
        marker=dict(
            size=12,
            color=star_color,
            symbol='circle',
            line=dict(color='white', width=2)
        ),
        name=f'{star_data["name"]} (current)',
        text=[hover_text],
        hoverinfo='text',
        showlegend=False
    )

# =============================================================================
# MAIN VISUALIZATION FUNCTION
# =============================================================================

def create_sgr_a_figure(stars_to_show=None, show_all_stars=False):
    """
    Create the main Sagittarius A* visualization figure.
    
    Args:
        stars_to_show: List of star names to display. If None, shows S2.
        show_all_stars: If True, shows all stars in catalog.
    
    Returns:
        Plotly Figure
    """
    if show_all_stars:
        stars_to_show = list_stars()
    elif stars_to_show is None:
        stars_to_show = ['S2']
    
    traces = []
    
    # Add Sgr A* (the black hole)
    traces.extend(create_sgr_a_marker())
    
    # Add selected star orbits
    for star_name in stars_to_show:
        star_data = get_star_data(star_name)
        if star_data:
            traces.extend(create_orbit_trace(star_name, star_data))
            # Add current position marker (at periapsis for static view)
            traces.append(create_star_marker(star_name, star_data, true_anomaly_rad=0.0))
    
    # Calculate axis range based on largest orbit
    max_range = 0
    for star_name in stars_to_show:
        star_data = get_star_data(star_name)
        if star_data:
            apoapsis = calculate_apoapsis_au(star_data['a_au'], star_data['e'])
            max_range = max(max_range, apoapsis)
    
    # Add some padding
    axis_range = max_range * 1.1
    
    # Create figure
    fig = go.Figure(data=traces)
    
    # Layout
    fig.update_layout(
        title=dict(
            text="<b>S-Stars Orbiting Sagittarius A*</b><br><sup>The Supermassive Black Hole at the Center of the Milky Way</sup>",
            x=0.5,
            font=dict(size=18)
        ),
        scene=dict(
            xaxis=dict(
                title='X (AU)',
                range=[-axis_range, axis_range],
                backgroundcolor='rgb(10,10,20)',
                gridcolor='rgb(50,50,70)',
                showbackground=True
            ),
            yaxis=dict(
                title='Y (AU)',
                range=[-axis_range, axis_range],
                backgroundcolor='rgb(10,10,20)',
                gridcolor='rgb(50,50,70)',
                showbackground=True
            ),
            zaxis=dict(
                title='Z (AU)',
                range=[-axis_range, axis_range],
                backgroundcolor='rgb(10,10,20)',
                gridcolor='rgb(50,50,70)',
                showbackground=True
            ),
            aspectmode='cube',
            camera=dict(
                eye=dict(x=1.5, y=1.5, z=0.8)
            )
        ),
        paper_bgcolor='rgb(10,10,20)',
        plot_bgcolor='rgb(10,10,20)',
        font=dict(color='white'),
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01,
            bgcolor='rgba(0,0,0,0.5)'
        ),
        margin=dict(l=0, r=0, t=80, b=0)
    )
    
    # Add annotation about scale
    fig.add_annotation(
        text=f"Schwarzschild radius: {SCHWARZSCHILD_RADIUS_AU:.2f} AU (black hole marker not to scale)",
        xref="paper", yref="paper",
        x=0.5, y=0.02,
        showarrow=False,
        font=dict(size=10, color='gray')
    )
    
    return fig

# =============================================================================

if __name__ == "__main__":
    print("Creating S-Star visualization...")
    
    # Create figure with all stars
    fig = create_sgr_a_figure(show_all_stars=True)
    
    # Show and offer save dialog
    show_and_save(fig, "sgr_a_visualization_stage1")
    
    # Also show orbit statistics
    print("\n--- Orbit Statistics ---")
    for star_name in list_stars():
        star = get_star_data(star_name)
        peri = calculate_periapsis_au(star['a_au'], star['e'])
        apo = calculate_apoapsis_au(star['a_au'], star['e'])
        v_peri = calculate_periapsis_velocity(star['a_au'], star['e'])
        precession = calculate_schwarzschild_precession_per_orbit(star['a_au'], star['e'])
        print(f"\n{star['name']}:")
        print(f"  Periapsis: {peri:.1f} AU, Apoapsis: {apo:.1f} AU")
        print(f"  Max velocity: {format_velocity(v_peri)}")
        print(f"  Precession: {precession:.3f} deg/orbit")


