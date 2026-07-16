"""
jupiter_visualization_shells.py - Jupiter interior, ring, and magnetosphere shell traces.

Sphere shells for Jupiter's interior (core through cloud layer). Custom
geometry for the ring system, Io plasma torus, radiation belts, and
magnetosphere. Jupiter's magnetosphere is the largest structure in the
solar system after the heliosphere.

Consumed by: planet_visualization.py (routing dispatcher)

Module updated: May 2026 with Anthropic's Claude Opus 4.7
    D3.1 sweep (May 2026): hovertext/legendgroup consolidation.
    April 17, 2026: provenance audit source citations added, Gemini fact-check applied.
    Hill sphere inconsistency resolved (info string said 530 R_J / 0.25 AU;
    correct is 740 R_J / 0.35 AU). Hill sphere "around a" typo fixed.
    Provenance audit identified by Anthropic's Claude Opus 4.7
May 27, 2026: Stage 3 info-marker standard sweep + Sun Direction cleanup
    (Opus 4.7). 6 info markers brought to red-border standard;
    2 dormant sun_direction calls removed (upper_atmosphere, hill_sphere
    -- v9 Residual Cleanup item 1); dead import removed.
"""
import numpy as np
import math
import plotly.graph_objs as go
from planet_visualization_utilities import (JUPITER_RADIUS_AU, KM_PER_AU, create_sphere_points, create_magnetosphere_shape, create_bow_shock_shape)
from orrery_rendering import rotate_to_sunward, create_info_marker
from idealized_orbits import orient_to_planet_pole  # N15: pole-vector ring orientation

def create_ring_points_jupiter (inner_radius, outer_radius, n_points=100, thickness=0.01):
    """
    Create points for a ring structure (for planets like Saturn).
    
    Parameters:
        inner_radius (float): Inner radius of the ring in AU
        outer_radius (float): Outer radius of the ring in AU
        n_points (int): Number of points to generate for each ring dimension
        thickness (float): Thickness of the ring in AU
        
    Returns:
        tuple: (x, y, z) coordinates as flattened arrays
    """
    # Generate radial and angular points
    radii = np.linspace(inner_radius, outer_radius, n_points // 4)
    thetas = np.linspace(0, 2*np.pi, n_points)
    
    # Create a meshgrid of radii and angles
    r, theta = np.meshgrid(radii, thetas)
    
    # Generate the ring coords on x-y plane
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    
    # Generate some points along z to give minimal thickness
    z_values = np.linspace(-thickness/2, thickness/2, 3)
    
    # Replicate the x, y coordinates for each z value
    x_all = []
    y_all = []
    z_all = []
    
    for z_val in z_values:
        x_all.append(x.flatten())
        y_all.append(y.flatten())
        z_all.append(np.full_like(x.flatten(), z_val))
    
    # Combine all points
    return np.concatenate(x_all), np.concatenate(y_all), np.concatenate(z_all)

# Jupiter Shell Creation Functions

# Source: NASA Juno Mission; Wahl et al. (2017)
# Verified: April 2026 via Gemini fact-check
jupiter_core_info = (
            "2.4 MB PER FRAME FOR HTML.<br><br>"
            "Jupiter's core is believed to be a dense mixture of rock, metal, and hydrogen compounds.<br>"
            "It may be up to 10 times the mass of Earth. Recent models suggest the core might be<br>"
            "partially dissolved or 'fuzzy' rather than a distinct solid structure. Its temperature<br>"
            "is estimated at about 20,000K and up to 40,000K. The color chosen approximates a black body."
)

def create_jupiter_core_shell(center_position=(0, 0, 0)):
    """Creates Jupiter's core shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 0.1,  # Approximately 10% of Jupiter's radius
        'color': 'rgb(175, 175, 255)',  # estimated black body color at about 20,000 K
        'opacity': 1.0,
        'name': 'Core',
        'description': (
            "Jupiter's core is believed to be a dense mixture of rock, metal, and hydrogen compounds.<br>"
            "It may be up to 10 times the mass of Earth. Recent models suggest the core might be<br>"
            "partially dissolved or 'fuzzy' rather than a distinct solid structure. Its temperature<br>"
            "is estimated at about 20,000K and up to 40,000K. The color chosen approximates a black body."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * JUPITER_RADIUS_AU
    
    # Create sphere points
    x, y, z = create_sphere_points(layer_radius, n_points=25)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    r_info = layer_radius * 1.05
    trace_name = f"Jupiter: {layer_info['name']}"

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(
            size=4.0,
            color=layer_info['color'],
            opacity=layer_info['opacity']
        ),
        name=trace_name,
        legendgroup=trace_name,
        hoverinfo='skip',
        showlegend=True
    )
    info_trace = go.Scatter3d(
        x=[center_x], y=[center_y], z=[center_z + r_info],
        mode='markers',
        marker=dict(size=8, color=layer_info['color'], opacity=1.0,
                    symbol='cross', line=dict(color='red', width=2)),
        name='',
        legendgroup=trace_name,
        text=[f"{trace_name}<br><br>{layer_info['description']}"],
        customdata=[trace_name],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    )

    traces = [shell_trace, info_trace]
    
    return traces

# Source: NASA Jupiter Fact Sheet; Juno Science Results
# Verified: April 2026 via Gemini fact-check
jupiter_metallic_hydrogen_info = (
            "2.1 MB PER FRAME FOR HTML.<br><br>"
            "Under extreme pressure, hydrogen transitions to a metallic state in this layer.<br>"
            "It behaves like an electrical conductor and is responsible for generating<br>"
            "Jupiter's powerful magnetic field. Temperatures in this region may reach 10,000K."
)

def create_jupiter_metallic_hydrogen_shell(center_position=(0, 0, 0)):
    """Creates Jupiter's metallic hydrogen shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 0.8,  # Up to about 80% of Jupiter's radius
        'color': 'rgb(225, 225, 255)',  # estimated black body color at about 10,000 K
        'opacity': 0.9,
        'name': 'Metallic Hydrogen Layer',
        'description': (
            "Metallic Hydrogen Layer:<br>" 
            "Under extreme pressure, hydrogen transitions to a metallic state in this layer.<br>"
            "It behaves like an electrical conductor and is responsible for generating<br>"
            "Jupiter's powerful magnetic field. Temperatures in this region may reach 10,000K."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * JUPITER_RADIUS_AU
    
    # Create sphere points
    x, y, z = create_sphere_points(layer_radius, n_points=25)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    r_info = layer_radius * 1.05
    trace_name = f"Jupiter: {layer_info['name']}"

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(
            size=3.5,
            color=layer_info['color'],
            opacity=layer_info['opacity']
        ),
        name=trace_name,
        legendgroup=trace_name,
        hoverinfo='skip',
        showlegend=True
    )
    info_trace = go.Scatter3d(
        x=[center_x], y=[center_y], z=[center_z + r_info],
        mode='markers',
        marker=dict(size=8, color=layer_info['color'], opacity=1.0,
                    symbol='cross', line=dict(color='red', width=2)),
        name='',
        legendgroup=trace_name,
        text=[f"{trace_name}<br><br>{layer_info['description']}"],
        customdata=[trace_name],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    )

    traces = [shell_trace, info_trace]
    
    return traces

# Source: NASA Jupiter Fact Sheet; Juno Science Results
# Verified: April 2026 via Gemini fact-check
jupiter_molecular_hydrogen_info = (
            "2.5 MB PER FRAME FOR HTML.<br><br>"
            "This layer consists of hydrogen in its molecular form. The transition from metallic<br>"
            "to molecular hydrogen is gradual. This layer makes up the bulk of Jupiter's mass<br>"
            "and is marked by decreasing temperature and pressure as you move outward. The temperature<br>"
            "ranges from about 5,000K (outer) to 10,000K (inner)."
)

def create_jupiter_molecular_hydrogen_shell(center_position=(0, 0, 0)):
    """Creates Jupiter's molecular hydrogen shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 0.97,  # Up to about 97% of Jupiter's radius
        'color': 'rgb(255, 255, 200)',  # estimated black body color at about 5,000 K 
        'opacity': 0.5,
        'name': 'Molecular Hydrogen Layer',
        'description': (
            "Molecular Hydrogen Layer:<br>" 
            "This layer consists of hydrogen in its molecular form. The transition from metallic<br>"
            "to molecular hydrogen is gradual. This layer makes up the bulk of Jupiter's mass<br>"
            "and is marked by decreasing temperature and pressure as you move outward. The temperature<br>"
            "ranges from about 5,000K (outer) to 10,000K (inner)."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * JUPITER_RADIUS_AU
    
    # Create sphere points
    x, y, z = create_sphere_points(layer_radius, n_points=25)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    r_info = layer_radius * 1.05
    trace_name = f"Jupiter: {layer_info['name']}"

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(
            size=3.0,
            color=layer_info['color'],
            opacity=layer_info['opacity']
        ),
        name=trace_name,
        legendgroup=trace_name,
        hoverinfo='skip',
        showlegend=True
    )
    info_trace = go.Scatter3d(
        x=[center_x], y=[center_y], z=[center_z + r_info],
        mode='markers',
        marker=dict(size=8, color=layer_info['color'], opacity=1.0,
                    symbol='cross', line=dict(color='red', width=2)),
        name='',
        legendgroup=trace_name,
        text=[f"{trace_name}<br><br>{layer_info['description']}"],
        customdata=[trace_name],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    )

    traces = [shell_trace, info_trace]
    
    return traces

# Source: NASA Jupiter Fact Sheet; Galileo Probe Results
# Verified: April 2026 via Gemini fact-check
jupiter_cloud_layer_info = (
            "USE MANUAL SCALED OF 0.005 AU TO VIEW CLOSELY."
            "4.6 MB PER FRAME FOR HTML.<br><br>"
            "Jupiter's visible cloud layer consists of bands of different colors, caused by<br>"
            "variations in chemical composition and atmospheric dynamics. The clouds are primarily<br>"
            "composed of ammonia, ammonium hydrosulfide, and water. The famous Great Red Spot<br>"
            "is a massive storm system located in this layer. Temperature ranges from 120 K in<br>" 
            "the highest ammonia ice clouds to about 200 K in the lower ammonium hydrosulfide clouds."
)

def create_jupiter_cloud_layer_shell(center_position=(0, 0, 0)):
    """Creates Jupiter's cloud layer shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 1.0,  # The visible "surface" - 100% of Jupiter's radius
        'color': 'rgb(255, 255, 235)',  # optical
        'opacity': 1.0,
        'name': 'Cloud Layer',
        'description': (
            "Jupiter Cloud Layer<br>" 
            "(Note: toggle off the cloud layer in the legend to better see the interior structure.)<br><br>"
            "Jupiter's visible cloud layer consists of bands of different colors, caused by<br>"
            "variations in chemical composition and atmospheric dynamics. The clouds are primarily<br>"
            "composed of ammonia, ammonium hydrosulfide, and water. The famous Great Red Spot<br>"
            "is a massive storm system located in this layer. Temperature ranges from 120 K in<br>" 
            "the highest ammonia ice clouds to about 200 K in the lower ammonium hydrosulfide clouds."
        )
    }
    
    # Calculate radius in AU
    radius = layer_info['radius_fraction'] * JUPITER_RADIUS_AU
    
    # Unpack center position
    center_x, center_y, center_z = center_position
    
    # Create mesh with reasonable resolution for performance
    resolution = 24  # Reduced from typical 50 for markers
    
    # Create a UV sphere
    phi = np.linspace(0, 2*np.pi, resolution)
    theta = np.linspace(-np.pi/2, np.pi/2, resolution)
    phi, theta = np.meshgrid(phi, theta)
    
    x = radius * np.cos(theta) * np.cos(phi)
    y = radius * np.cos(theta) * np.sin(phi)
    z = radius * np.sin(theta)
    
    # Apply center position offset
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    # Create triangulation
    indices = []
    for i in range(resolution-1):
        for j in range(resolution-1):
            p1 = i * resolution + j
            p2 = i * resolution + (j + 1)
            p3 = (i + 1) * resolution + j
            p4 = (i + 1) * resolution + (j + 1)
            
            indices.append([p1, p2, p4])
            indices.append([p1, p4, p3])
    
    # Create main surface
    surface_trace = go.Mesh3d(
        x=x.flatten(), 
        y=y.flatten(), 
        z=z.flatten(),
        i=[idx[0] for idx in indices],
        j=[idx[1] for idx in indices],
        k=[idx[2] for idx in indices],
        color=layer_info['color'],
        opacity=layer_info['opacity'],
        name=f"Jupiter: {layer_info['name']}",
        legendgroup=f"Jupiter: {layer_info['name']}",
        showlegend=True,
        hoverinfo='none',  # Disable hover on mesh surface
        # Add these new parameters to make hover text invisible
        hovertemplate=' ',  # Empty template instead of None
        hoverlabel=dict(
    #        bgcolor='rgba(0,0,0,0)',  # Transparent background
            font=dict(
                color='rgba(0,0,0,0)',  # Transparent text
    #            size=0                  # Zero font size
            ),
            bordercolor='rgba(0,0,0,0)'  # Transparent border
        ), 
        # Add these new parameters to eliminate shading
        flatshading=True,  # Use flat shading instead of smooth
        lighting=dict(
            ambient=1.0,     # Set to maximum (1.0)
            diffuse=0.0,     # Turn off diffuse lighting
            specular=0.0,    # Turn off specular highlights
            roughness=1.0,   # Maximum roughness
            fresnel=0.0      # Turn off fresnel effect
        ),
        lightposition=dict(
            x=0,  # Centered light
            y=0,  # Centered light
            z=10000  # Light from very far above to minimize shadows
        )       
    )
        
    # Use the Fibonacci sphere algorithm for more even point distribution
    def fibonacci_sphere(samples=1000):
        points = []
        phi = math.pi * (3. - math.sqrt(5.))  # Golden angle in radians
        
        for i in range(samples):
            y = 1 - (i / float(samples - 1)) * 2  # y goes from 1 to -1
            radius_at_y = math.sqrt(1 - y * y)  # Radius at y
            
            theta = phi * i  # Golden angle increment
            
            x = math.cos(theta) * radius_at_y
            z = math.sin(theta) * radius_at_y
            
            points.append((x, y, z))
        
        return points
    
    # Generate fibonacci sphere points
    fib_points = fibonacci_sphere(samples=50)  # Originally, 50 hover points evenly distributed
    
    # Scale and offset the points
    x_hover = [p[0] * radius + center_x for p in fib_points]
    y_hover = [p[1] * radius + center_y for p in fib_points]
    z_hover = [p[2] * radius + center_z for p in fib_points]
        
    # Create a list of repeated descriptions for each point
    # This is crucial - we need exactly one text entry per point

    # Just the name for "Object Names Only" mode

    # Create hover trace with direct text assignment
    # Single info marker at north pole, 5% above radius
    r_info = radius * 1.05
    trace_name = f"Jupiter: {layer_info['name']}"

    hover_trace = go.Scatter3d(
        x=[center_x], y=[center_y], z=[center_z + r_info],
        mode='markers',
        marker=dict(size=8, color=layer_info['color'], opacity=1.0,
                    symbol='cross', line=dict(color='red', width=2)),
        name=trace_name,
        legendgroup=trace_name,
        text=[f"{trace_name}<br><br>{layer_info['description']}"],
        customdata=[f"Jupiter: {layer_info['name']}"],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    )

    return [surface_trace, hover_trace]

# Source: NASA Jupiter Fact Sheet; Juno Science Results
# Verified: April 2026 via Gemini fact-check
jupiter_upper_atmosphere_info = (
            "2.7 MB PER FRAME FOR HTML.<br><br>"
            "Jupiter's upper atmosphere includes the stratosphere and thermosphere.<br>"
            "It's less dense than the cloud layer below and contains hydrocarbon haze<br>"
            "produced by solar ultraviolet radiation. Aurora activity can be observed<br>"
            "at Jupiter's poles, caused by interactions with its magnetic field. Temperature<br>"
            "ranges from 200K in the stratosphere to 1000K in the thermosphere and exosphere."
)

# Fix for create_jupiter_upper_atmosphere_shell function - Implementation missing
def create_jupiter_upper_atmosphere_shell(center_position=(0, 0, 0)):
    """Creates Jupiter's upper atmosphere shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 1.1,  # Extends about 10% beyond the visible radius
        'color': 'rgb(220, 240, 255)',  # optical
        'opacity': 0.5,
        'name': 'Upper Atmosphere',
        'description': (
            "Jupiter's upper atmosphere includes the stratosphere and thermosphere.<br>"
            "It's less dense than the cloud layer below and contains hydrocarbon haze<br>"
            "produced by solar ultraviolet radiation. Aurora activity can be observed<br>"
            "at Jupiter's poles, caused by interactions with its magnetic field. Temperature<br>"
            "ranges from 200K in the stratosphere to 1000K in the thermosphere and exosphere."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * JUPITER_RADIUS_AU
    
    # Create sphere points
    x, y, z = create_sphere_points(layer_radius, n_points=20)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    r_info = layer_radius * 1.05
    trace_name = f"Jupiter: {layer_info['name']}"

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(
            size=3.0,
            color=layer_info['color'],
            opacity=layer_info['opacity']
        ),
        name=trace_name,
        legendgroup=trace_name,
        hoverinfo='skip',
        showlegend=True
    )
    info_trace = go.Scatter3d(
        x=[center_x], y=[center_y], z=[center_z + r_info],
        mode='markers',
        marker=dict(size=8, color=layer_info['color'], opacity=1.0,
                    symbol='cross', line=dict(color='red', width=2)),
        name='',
        legendgroup=trace_name,
        text=[f"{trace_name}<br><br>{layer_info['description']}"],
        customdata=[trace_name],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    )

    traces = [shell_trace, info_trace]
    

    return traces

def create_jupiter_magnetosphere(center_position=(0, 0, 0), sun_position=(0, 0, 0)):
    """Creates Jupiter's main magnetosphere structure."""
    # Parameters for magnetosphere components (in Jupiter radii)
    params = {
        # Compressed sunward side
        'sunward_distance': 65,  # Source: Joy et al. 2002 -- median subsolar magnetopause ~65 R_J (Gemini Mode-7: was 50, too compressed)
        
        # Equatorial extension (wider than polar)
        'equatorial_radius': 100,
        'polar_radius': 80,
        
        # Magnetotail parameters
        'tail_length': 500,  # Length of visible magnetotail
        'tail_base_radius': 150,  # Radius at the base of the tail
        'tail_end_radius': 200,  # Radius at the end of the tail
    }
    
    # Scale everything by Jupiter's radius in AU
    for key in params:
        params[key] *= JUPITER_RADIUS_AU
    
    # Create magnetosphere main shape (generated with -X as sunward)
    x, y, z = create_magnetosphere_shape(params)
    
    # Unpack center position
    center_x, center_y, center_z = center_position
    
    # Rotate to actual sunward direction, then offset to center position
    x, y, z = np.array(x), np.array(y), np.array(z)
    # Phase D2: sun_position + magnetic tilt. Jupiter's magnetic dipole
    # is tilted ~10 deg from its rotation axis.
    x, y, z = rotate_to_sunward(
        x, y, z, center_position=center_position,
        sun_position=sun_position, magnetic_tilt_deg=10,
    )
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=2.0,
                color='rgb(200, 200, 255)', # Light blue for magnetic field
                opacity=0.3
            ),
            name='Jupiter: Magnetosphere',
            legendgroup='Jupiter: Magnetosphere',
            hoverinfo='skip',
            showlegend=True
        )
    ]
    mag_desc = ("Jupiter's magnetosphere extends up to 100 Jupiter radii on the sunward side<br>"
               "and forms a magnetotail stretching beyond Saturn's orbit in the opposite direction.<br>"
               "It traps charged particles, creating intense radiation belts that would be lethal to humans.<br>"
               "The Bow Shock points towards the Sun along the X-axis. The XY plane is the ecliptic.")
    traces.append(create_info_marker(
        x[0], y[0], z[0],
        'rgb(200, 200, 255)', f"Jupiter: Magnetosphere<br><br>{mag_desc}", 'Jupiter: Magnetosphere'
    ))
    
    # ------------------------------------------------------------------
    # Bow shock (conic-section model via shared builder).
    # Module updated: June 2026 with Anthropic's Claude Opus 4.8.
    # ------------------------------------------------------------------
    bs_standoff = 82 * JUPITER_RADIUS_AU  # Source: Joy et al. 2002 (mean ~84 R_J, highly variable)
    bs_x, bs_y, bs_z = create_bow_shock_shape(
        bs_standoff, width=bs_standoff * 1.6, eccentricity=1.05
    )
    bs_x, bs_y, bs_z = np.array(bs_x), np.array(bs_y), np.array(bs_z)
    bs_x, bs_y, bs_z = rotate_to_sunward(
        bs_x, bs_y, bs_z, center_position=center_position, sun_position=sun_position
    )
    bs_cx, bs_cy, bs_cz = center_position
    bs_x = bs_x + bs_cx
    bs_y = bs_y + bs_cy
    bs_z = bs_z + bs_cz
    bs_km = bs_standoff * KM_PER_AU
    bs_text = (
        "Jupiter: Bow Shock<br><br>"
        "Subsolar standoff ~82 R_J "
        f"({bs_km:,.0f} km / {bs_standoff:.4f} AU).<br>"
        "Source: Joy et al. 2002 (mean ~84 R_J, highly variable).<br>"
        "The Bow Shock points towards the Sun along the X-axis. The XY plane is the ecliptic."
    )
    traces.append(
        go.Scatter3d(
            x=bs_x, y=bs_y, z=bs_z,
            mode='markers',
            marker=dict(size=1.5, color='rgb(255, 200, 150)', opacity=0.2),
            name='Jupiter: Bow Shock',
            legendgroup='Jupiter: Bow Shock',
            hoverinfo='skip',
            showlegend=True,
        )
    )
    traces.append(create_info_marker(
        bs_x[0], bs_y[0], bs_z[0],
        'rgb(255, 200, 150)', bs_text, 'Jupiter: Bow Shock'
    ))

    return traces

jupiter_io_plasma_torus_info = ("634 KB PER FRAME FOR HTML.<br><br>"
              "Donut-shaped region of charged particles from Jupiter's moon Io")

def create_jupiter_io_plasma_torus(center_position=(0, 0, 0)):
    """Creates Jupiter's Io plasma torus."""
    # Parameters
    io_torus_distance = 5.9 * JUPITER_RADIUS_AU  # Io's orbit is at about 5.9 Jupiter radii
    io_torus_thickness = 2 * JUPITER_RADIUS_AU
    io_torus_width = 1 * JUPITER_RADIUS_AU
    
    # Unpack center position
    center_x, center_y, center_z = center_position
    
    # Create the Io plasma torus points
    io_torus_x = []
    io_torus_y = []
    io_torus_z = []
    
    n_points = 100
    n_rings = 8
    
    for i_ring in range(n_rings):
        # Vary the radius slightly to create thickness
        radius_offset = (i_ring / (n_rings-1) - 0.5) * io_torus_thickness
        torus_radius = io_torus_distance + radius_offset
        
        for i in range(n_points):
            angle = (i / n_points) * 2 * np.pi

            # Position in x-y plane (equatorial)
            x = torus_radius * np.cos(angle)
            y = torus_radius * np.sin(angle)
            z = 0  # In the equatorial plane    
            
            # Add some thickness variation
            jitter = (np.random.random() - 0.5) * io_torus_width
            
            io_torus_x.append(x)
            io_torus_y.append(y)
            io_torus_z.append(z + jitter)     # Apply jitter to z axis
    
    # Apply center position offset
    io_torus_x = np.array(io_torus_x) + center_x
    io_torus_y = np.array(io_torus_y) + center_y
    io_torus_z = np.array(io_torus_z) + center_z

    # Create the Io plasma torus hover text and customdata arrays
    io_desc = ("Io plasma torus: A donut-shaped region of charged particles emanating from<br>"
              "Jupiter's moon Io due to volcanic activity. These particles become trapped<br>"
              "in Jupiter's magnetic field, forming this distinctive structure.")
    
    traces = [
        go.Scatter3d(
            x=io_torus_x,
            y=io_torus_y,
            z=io_torus_z,
            mode='markers',
            marker=dict(
                size=1.5,
                color='rgb(255, 100, 100)',  # Reddish color for plasma torus
                opacity=0.3
            ),
            name='Jupiter: Io Plasma Torus',
            legendgroup='Jupiter: Io Plasma Torus',
            hoverinfo='skip',
            showlegend=True
        )
    ]
    traces.append(create_info_marker(
        io_torus_x[0], io_torus_y[0], io_torus_z[0],
        'rgb(255, 100, 100)', f"Jupiter: Io Plasma Torus<br><br>{io_desc}", 'Jupiter: Io Plasma Torus'
    ))
    
    return traces

# Source: NASA Jupiter Magnetosphere Overview; Juno Mission
# Verified: April 2026 via Gemini fact-check
jupiter_radiation_belts_info = (
            "560 KB PER FRAME FOR HTML.<br><br>"
            "Vizualize at a manual scale of 0.005 AU.<br><br>"
            "Zones of trapped high-energy particles in Jupiter's magnetosphere"                     
)

def create_jupiter_radiation_belts(center_position=(0, 0, 0)):
    """Creates Jupiter's radiation belts."""
    belt_colors = ['rgb(255, 255, 100)', 'rgb(100, 255, 150)', 'rgb(100, 200, 255)']
    belt_names = ['Jupiter: Inner Radiation Belt', 'Jupiter: Middle Radiation Belt', 'Jupiter: Outer Radiation Belt']
    belt_texts = [
        "Inner radiation belt: Intense region of trapped high-energy particles near Jupiter",
        "Middle radiation belt: Region of trapped charged particles at intermediate distances from Jupiter",
        "Outer radiation belt: Extended region of trapped particles in Jupiter's outer magnetosphere"
    ]
    
    # Belt distances in Jupiter radii
    belt_distances = [1.5, 3.0, 6.0]
    belt_thickness = 0.5 * JUPITER_RADIUS_AU
    
    # Scale distances by Jupiter's radius in AU
    belt_distances = [d * JUPITER_RADIUS_AU for d in belt_distances]
    
    # Unpack center position
    center_x, center_y, center_z = center_position
    
    traces = []
    
    for i, belt_distance in enumerate(belt_distances):
        belt_x = []
        belt_y = []
        belt_z = []
        
        n_points = 80
        n_rings = 5
        
        for i_ring in range(n_rings):
            # Vary the radius slightly to create thickness
            radius_offset = (i_ring / (n_rings-1) - 0.5) * belt_thickness
            belt_radius = belt_distance + radius_offset
            
            for j in range(n_points):
                angle = (j / n_points) * 2 * np.pi
                
                # Create a belt around Jupiter's rotational axis
                x = belt_radius * np.cos(angle)
                y = belt_radius * np.sin(angle)
                
                # Add some z variation based on angle to create the shape of a belt
                # rather than a perfect torus (thinner near poles)
                z_scale = 0.2 * belt_radius  # Controls how flat the belts are
                z = z_scale * np.sin(2 * angle)
                
                belt_x.append(x)
                belt_y.append(y)
                belt_z.append(z)
        
        # Apply center position offset
        belt_x = np.array(belt_x) + center_x
        belt_y = np.array(belt_y) + center_y
        belt_z = np.array(belt_z) + center_z
        
        # Create the radiation belt hover text and customdata arrays

        traces.append(
            go.Scatter3d(
                x=belt_x,
                y=belt_y,
                z=belt_z,
                mode='markers',
                marker=dict(
                    size=1.5,
                    color=belt_colors[i],
                    opacity=0.3
                ),
                name=belt_names[i],
                legendgroup=belt_names[i],
                hoverinfo='skip',
                showlegend=True
            )
        )
        traces.append(create_info_marker(
            belt_x[0], belt_y[0], belt_z[0],
            belt_colors[i], f"{belt_names[i]}<br><br>{belt_texts[i]}", belt_names[i]
        ))
    
    return traces
    
# Source: NASA Solar System Dynamics
# Verified: April 2026 via Gemini fact-check
jupiter_hill_sphere_info = (
            "SELECT MANUAL SCALE OF AT LEAST 0.5 AU TO VISUALIZE.<br>" 
            "1.3 MB PER FRAME FOR HTML.<br><br>"
            "Jupiter's Hill Sphere (extends to ~740 Jupiter radii, about 0.35 AU or ~53 million km)"                      
)

def create_jupiter_hill_sphere_shell(center_position=(0, 0, 0)):
    """Creates Jupiter's Hill sphere shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 740,  
        'color': 'rgb(0, 255, 0)',  # Green for Hill sphere
        'opacity': 0.25,
        'name': 'Hill Sphere',
        'description': (
            "SET MANUAL SCALE OF AT LEAST 0.5 AU TO VISUALIZE.<br><br>"
            "Jupiter's Hill Sphere (extends to ~740 Jupiter radii, ~0.35 AU or ~53 million km)<br><br>"
                "The Hill sphere is the region around a body where its own gravity is the dominant force in attracting satellites. For <br>" 
                "a planet orbiting a star, it's the region where the planet's gravity is stronger than the star's tidal forces.<br><br>" 
                "The Hill Sphere radius can be described in words as follows: it is equal to the planet's average distance from the <br>" 
                "Sun (its orbital semi-major axis) multiplied by the cube root of the ratio between the planet's mass and three times <br>" 
                "the Sun's mass. In other words, you take how far the planet orbits out from the Sun, then scale that distance by the <br>" 
                "cube root of (planet mass / [3 x solar mass]) to find the boundary within which the planet's gravity dominates over the Sun's."            
        )
    }
        
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * JUPITER_RADIUS_AU
    
    # Create sphere points
    x, y, z = create_sphere_points(layer_radius, n_points=20)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    r_info = layer_radius * 1.05
    trace_name = f"Jupiter: {layer_info['name']}"

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(
            size=2.0,
            color=layer_info['color'],
            opacity=layer_info['opacity']
        ),
        name=trace_name,
        legendgroup=trace_name,
        hoverinfo='skip',
        showlegend=True
    )
    info_trace = go.Scatter3d(
        x=[center_x], y=[center_y], z=[center_z + r_info],
        mode='markers',
        marker=dict(size=8, color=layer_info['color'], opacity=1.0,
                    symbol='cross', line=dict(color='red', width=2)),
        name='',
        legendgroup=trace_name,
        text=[f"{trace_name}<br><br>{layer_info['description']}"],
        customdata=[trace_name],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    )

    traces = [shell_trace, info_trace]
    
    # Add a sun direction indicator (arrow pointing toward Sun along negative X-axis)
#    sun_traces = create_sun_direction_indicator(center_position)
#    for trace in sun_traces:
#        traces.append(trace)


    return traces

jupiter_ring_system_info = (
                "22.2 MB PER FRAME FOR HTML.<br><br>"

                "The main ring is reddish and composed of dust ejected from Jupiter's small inner moons,<br>"
                "Metis and Adrastea, due to high-speed impacts by micrometeoroids.<br><br>"

                "The Halo Ring is a faint, thick torus of material.<br>"
                "The ring likely consists of fine dust particles pushed out of the main ring<br>"
                "by electromagnetic forces from Jupiter's powerful magnetosphere.<br><br>" 

                "The Amalthea Gossamer Ring is an extremely faint and wide ring.<br>"
                "It is composed of dust particles ejected from Amalthea by micrometeoroid impacts.<br><br>"   

                "The Thebe Gossamer Ring is another very faint and wide ring.<br>"
                "It is composed of dust particles ejected from Thebe by micrometeoroid impacts."                                           
)

def create_jupiter_ring_system(center_position=(0, 0, 0)):
    """
    Creates a visualization of Jupiter's ring system.
    
    Parameters:
        center_position (tuple): (x, y, z) position of Jupiter's center
        
    Returns:
        list: A list of plotly traces representing the ring components
    """
    traces = []
    
    # Source: NASA Jupiter Ring Fact Sheet; Galileo spacecraft data
    # Verified: April 2026 via Gemini fact-check
    # Scope of the above citation: ring geometry only (inner/outer radius,
    # thickness). Colors below are selected by the developer for visual
    # distinction, not verified against the cited source or any other
    # photometric measurement -- do not read this citation as covering
    # them (Tony's call, July 16, 2026; see LEDGER_CONSOLIDATED.md L-124).
    # Define Jupiter's ring parameters in kilometers from Jupiter's center
    # Then convert to Jupiter radii, and finally to AU
    ring_params = {
        'main_ring': {
            'inner_radius_km': 122500,  # Inner edge (in km from Jupiter's center)
            'outer_radius_km': 129000,  # Outer edge (in km from Jupiter's center)
            'thickness_km': 30,         # Approximate thickness
            'color': 'rgb(180, 120, 100)',  # Reddish color
            'opacity': 0.7,
            'name': 'Main Ring',
            'description': (
                "Jupiter's Main Ring is a relatively bright and very thin ring.<br>"
                "It extends from about 122,500 km to 129,000 km from Jupiter's center.<br>"
                "Its thickness is only about 30-300 km.<br>"
                "The main ring is reddish and composed of dust ejected from Jupiter's small inner moons,<br>"
                "Metis and Adrastea, due to high-speed impacts by micrometeoroids."
            )
        },
        'halo_ring': {
            'inner_radius_km': 100000,  # Inner edge (in km from Jupiter's center)
            'outer_radius_km': 122500,  # Outer edge (in km from Jupiter's center)
            'thickness_km': 12500,      # Approximate thickness (thicker than the main ring)
            'color': 'rgb(150, 150, 150)',  # Grayish color
            'opacity': 0.4,
            'name': 'Halo Ring',
            'description': (
                "The Halo Ring is a faint, thick torus of material.<br>"
                "It extends inward from the main ring to about 100,000 km from Jupiter's center.<br>"
                "It is much thicker than the main ring, extending about 12,500 km vertically.<br>"
                "The ring likely consists of fine dust particles pushed out of the main ring<br>"
                "by electromagnetic forces from Jupiter's powerful magnetosphere."
            )
        },
        'amalthea_gossamer': {
            'inner_radius_km': 129000,  # Inner edge (in km from Jupiter's center)
            'outer_radius_km': 182000,  # Outer edge (at Amalthea's orbit)
            'thickness_km': 2000,       # Approximate thickness
            'color': 'rgb(170, 170, 190)',  # Faint bluish-gray
            'opacity': 0.2,
            'name': 'Amalthea Gossamer Ring',
            'description': (
                "The Amalthea Gossamer Ring is an extremely faint and wide ring.<br>"
                "It extends outwards from the main ring (129,000 km) to Amalthea's orbit (182,000 km).<br>"
                "It is composed of dust particles ejected from Amalthea by micrometeoroid impacts.<br>"
                "It is much fainter and more diffuse than the main ring."
            )
        },
        'thebe_gossamer': {
            'inner_radius_km': 129000,  # Inner edge (in km from Jupiter's center)
            'outer_radius_km': 226000,  # Outer edge (at Thebe's orbit)
            'thickness_km': 8600,       # Approximate thickness
            'color': 'rgb(170, 170, 190)',  # Faint bluish-gray (same as Amalthea ring)
            'opacity': 0.15,
            'name': 'Thebe Gossamer Ring',
            'description': (
                "The Thebe Gossamer Ring is another very faint and wide ring.<br>"
                "It extends outwards from the main ring (129,000 km) to beyond Thebe's orbit (226,000 km).<br>"
                "It is composed of dust particles ejected from Thebe by micrometeoroid impacts.<br>"
                "It is the faintest of Jupiter's rings, with a vertical extension of about 8,600 km."
            )
        }
    }
    
    # Unpack center position
    center_x, center_y, center_z = center_position
    
    # Create traces for each ring
    for ring_name, ring_info in ring_params.items():
        # Convert km to AU
        inner_radius_au = ring_info['inner_radius_km'] / KM_PER_AU
        outer_radius_au = ring_info['outer_radius_km'] / KM_PER_AU
        thickness_au = ring_info['thickness_km'] / KM_PER_AU
        
        # Reduce point count for very large rings to improve performance
        n_points = 100
        if 'gossamer' in ring_name:
            n_points = 80  # Fewer points for larger gossamer rings
        
        # Create ring points
        x, y, z = create_ring_points_jupiter (inner_radius_au, outer_radius_au, n_points, thickness_au)
        
        # Orient into the ecliptic via the IAU pole vector (N15 migration June 2026;
        # Jupiter obliquity ~3 deg, so the shift is small -- done for consistency with
        # Saturn/Uranus/Neptune, replacing the prior no-rotation flat ring).
        x = np.array(x)
        y = np.array(y)
        z = np.array(z)
        x_final, y_final, z_final = orient_to_planet_pole(x, y, z, 'Jupiter')

        # Apply center position offset to the FINAL coordinates
        x_final = x_final + center_x
        y_final = y_final + center_y
        z_final = z_final + center_z

        # Add ring trace
        traces.append(
            go.Scatter3d(
                x=x_final, y=y_final, z=z_final,
                mode='markers',
                marker=dict(
                    size=1.5,  # Small markers for rings
                    color=ring_info['color'],
                    opacity=ring_info['opacity']
                ),
                name=f"Jupiter: {ring_info['name']}",
                legendgroup=f"Jupiter: {ring_info['name']}",
                hoverinfo='skip',
                showlegend=True
            )
        )
        # Ring marker -- first point of the oriented, offset ring (mirrors
        # Saturn/Uranus/Neptune), so it rides the ring's actual plane.
        traces.append(create_info_marker(
            x_final[0], y_final[0], z_final[0],
            ring_info['color'], f"Jupiter: {ring_info['name']}<br><br>{ring_info['description']}",
            f"Jupiter: {ring_info['name']}"
        ))
    
    return traces

# Source: NASA Jupiter Magnetosphere Overview; Juno Mission
# Verified: April 2026 via Gemini fact-check
jupiter_magnetosphere_info = (
            "SELECT MANUAL SCALE OF AT LEAST 0.4 AU TO VISUALIZE.<br>"
            "1.4 MB PER FRAME FOR HTML.<br><br>"

            "Jupiter's magnetosphere extends up to 100 Jupiter radii on the sunward side<br>"
            "and forms a magnetotail stretching beyond Saturn's orbit in the opposite direction.<br>"
            "It traps charged particles, creating intense radiation belts that would be lethal to humans.<br><br>"

            "Io plasma torus: A donut-shaped region of charged particles emanating from<br>"
            "Jupiter's moon Io due to volcanic activity. These particles become trapped<br>"
            "in Jupiter's magnetic field, forming this distinctive structure.<br><br>"  

            "Inner radiation belt: Intense region of trapped high-energy particles near Jupiter<br>"
            "Middle radiation belt: Region of trapped charged particles at intermediate distances from Jupiter<br>"
            "Outer radiation belt: Extended region of trapped particles in Jupiter's outer magnetosphere"                      
)