import numpy as np
import math
import plotly.graph_objs as go
from planet_visualization_utilities import (EARTH_RADIUS_AU, create_sphere_points, create_magnetosphere_shape)
from shared_utilities import create_sun_direction_indicator

# Earth Shell Creation Functions

earth_inner_core_info = (
            "Earth's inner core is a solid sphere composed primarily of iron and nickel.\n"
            "Despite incredible pressure, temperatures of 5,400°C (9,800°F) keep it nearly\n"
            "at melting point. It rotates slightly faster than the rest of Earth, creating\n"
            "complex dynamics in Earth's magnetic field. The inner core is approximately\n"
            "1,220 km (760 miles) in radius."
)

def create_earth_inner_core_shell(center_position=(0, 0, 0)):
    """Creates Earth's inner core shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 0.19,  # Inner core: 0-19% of Earth's radius
        'color': 'rgb(255, 180, 140)',  # Orange-red for hot iron core
        'opacity': 1.0,
        'name': 'Inner Core',
        'description': (
            "Earth's inner core is a solid sphere composed primarily of iron and nickel.<br>"
            "Despite incredible pressure, temperatures of 5,400°C (9,800°F) keep it nearly<br>"
            "at melting point. It rotates slightly faster than the rest of Earth, creating<br>"
            "complex dynamics in Earth's magnetic field. The inner core is approximately<br>"
            "1,220 km (760 miles) in radius."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * EARTH_RADIUS_AU
    
    # Create sphere points
    x, y, z = create_sphere_points(layer_radius, n_points=50)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=4.0,
                color=layer_info['color'],
                opacity=layer_info['opacity']
            ),
            name=f"Earth: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Earth: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

earth_outer_core_info = (
            "The outer core is a liquid layer of iron, nickel, and lighter elements.\n"
            "Convection currents in this highly conductive fluid generate Earth's\n"
            "magnetic field through a process called the geodynamo. It extends from\n"
            "1,220 to 3,500 km from Earth's center and has temperatures ranging from\n"
            "4,500°C (8,100°F) to 5,400°C (9,800°F)."
)

def create_earth_outer_core_shell(center_position=(0, 0, 0)):
    """Creates Earth's outer core shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 0.55,  # Outer core: 19-55% of Earth's radius
        'color': 'rgb(255, 140, 0)',  # Deeper orange for liquid metal
        'opacity': 0.8,
        'name': 'Outer Core',
        'description': (
            "The outer core is a liquid layer of iron, nickel, and lighter elements.<br>"
            "Convection currents in this highly conductive fluid generate Earth's<br>"
            "magnetic field through a process called the geodynamo. It extends from<br>"
            "1,220 to 3,500 km from Earth's center and has temperatures ranging from<br>"
            "4,500°C (8,100°F) to 5,400°C (9,800°F)."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * EARTH_RADIUS_AU
    
    # Create sphere points
    x, y, z = create_sphere_points(layer_radius, n_points=50)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=3.7,
                color=layer_info['color'],
                opacity=layer_info['opacity']
            ),
            name=f"Earth: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Earth: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

earth_lower_mantle_info = (
            "The lower mantle is composed of solid silicate rocks rich in iron and magnesium.\n"
            "Despite being solid, it flows very slowly through convection, driving plate tectonics.\n"
            "This region extends from 660 to 2,900 km below Earth's surface and experiences\n"
            "temperatures from 2,200°C to 4,500°C (4,000°F to 8,100°F) and extreme pressure."
)

def create_earth_lower_mantle_shell(center_position=(0, 0, 0)):
    """Creates Earth's lower mantle shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 0.85,  # Lower mantle: 55-85% of Earth's radius
        'color': 'rgb(230, 100, 20)',  # Reddish-brown
        'opacity': 0.7,
        'name': 'Lower Mantle',
        'description': (
            "The lower mantle is composed of solid silicate rocks rich in iron and magnesium.<br>"
            "Despite being solid, it flows very slowly through convection, driving plate tectonics.<br>"
            "This region extends from 660 to 2,900 km below Earth's surface and experiences<br>"
            "temperatures from 2,200°C to 4,500°C (4,000°F to 8,100°F) and extreme pressure."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * EARTH_RADIUS_AU
    
    # Create sphere points
    x, y, z = create_sphere_points(layer_radius, n_points=50)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=3.4,
                color=layer_info['color'],
                opacity=layer_info['opacity']
            ),
            name=f"Earth: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Earth: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

earth_upper_mantle_info = (
            "The upper mantle includes the asthenosphere, a partially molten layer where\n"
            "most magma originates. This region flows more readily than the lower mantle,\n"
            "allowing tectonic plates to move. It extends from about 30 to 660 km below\n"
            "the surface, with temperatures from 500°C to 2,200°C (900°F to 4,000°F)."
)

def create_earth_upper_mantle_shell(center_position=(0, 0, 0)):
    """Creates Earth's upper mantle shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 0.98,  # Upper mantle: 85-98% of Earth's radius
        'color': 'rgb(205, 85, 85)',  # Lighter reddish-brown
        'opacity': 0.6,
        'name': 'Upper Mantle',
        'description': (
            "The upper mantle includes the asthenosphere, a partially molten layer where<br>"
            "most magma originates. This region flows more readily than the lower mantle,<br>"
            "allowing tectonic plates to move. It extends from about 30 to 660 km below<br>"
            "the surface, with temperatures from 500°C to 2,200°C (900°F to 4,000°F)."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * EARTH_RADIUS_AU
    
    # Create sphere points
    x, y, z = create_sphere_points(layer_radius, n_points=50)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=3.1,
                color=layer_info['color'],
                opacity=layer_info['opacity']
            ),
            name=f"Earth: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Earth: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

earth_crust_info = (
            "Earth's crust is the thin, solid outer layer where humans live. It's divided into\n"
            "oceanic crust (5-10 km thick) made mostly of basalt, and continental crust (30-50 km thick)\n"
            "made primarily of granite. The crust contains all known life and the accessible portion\n"
            "of Earth's geological resources. Surface temperatures range from -80°C to 60°C (-112°F to 140°F)."
)

def create_earth_crust_shell(center_position=(0, 0, 0)):
    """Creates Earth's crust shell using Mesh3d for better performance with improved hover."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 1.0,  # Crust: 100% of Mars's radius
        'color': 'rgb(70, 120, 160)',  # Bluish for oceans, brown for land
        'opacity': 1.0,
        'name': 'Crust',
        'description': (
            "Earth Crust<br>" 
            "(Note: toggle off the crust layer in the legend to better see the interior structure.)<br><br>"
            "Earth's crust is the thin, solid outer layer where humans live. It's divided into<br>"
            "oceanic crust (5-10 km thick) made mostly of basalt, and continental crust (30-50 km thick)<br>"
            "made primarily of granite. The crust contains all known life and the accessible portion<br>"
            "of Earth's geological resources. Surface temperatures range from -80°C to 60°C (-112°F to 140°F)."
        )
    }
    
    # Calculate radius in AU
    radius = layer_info['radius_fraction'] * EARTH_RADIUS_AU
    
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
        name=f"Earth: {layer_info['name']}",
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
    hover_texts = [layer_info['description']] * len(x_hover)

    # Just the name for "Object Names Only" mode
    layer_name = f"Earth: {layer_info['name']}"
    minimal_hover_texts = [layer_name] * len(x_hover)

    # Create hover trace with direct text assignment
    hover_trace = go.Scatter3d(
        x=x_hover, 
        y=y_hover, 
        z=z_hover,
        mode='markers',
        marker=dict(
            size=2,  # originally 5
            color='rgb(70, 120, 160)',  # Layer color, originally 'white'
            opacity=1.0,  # originally 0.8
            line=dict(  # Add a contrasting outline
                width=1,
                color='black'
            )
        ),
        name=f"Earth: {layer_info['name']} (Info)",
        text=hover_texts,  # IMPORTANT: Matching length with coordinate arrays
        customdata=minimal_hover_texts,  # For "Object Names Only" mode
        hovertemplate='%{text}<extra></extra>',  # Use the standard hover template
        showlegend=False  # Don't show in legend since it's just for hover
    )

    return [surface_trace, hover_trace]

earth_atmosphere_info = (
            "The lower atmosphere includes the troposphere (0-12 km) where weather occurs, and\n"
            "the stratosphere (12-50 km) which contains the ozone layer. These regions contain\n"
            "99% of atmospheric mass, primarily nitrogen and oxygen. Temperature varies from\n"
            "about 15°C (59°F) at sea level to -60°C (-76°F) at the stratopause."
)

def create_earth_atmosphere_shell(center_position=(0, 0, 0)):
    """Creates Earth's lower atmosphere shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 1.05,  # Troposphere and stratosphere
        'color': 'rgb(150, 200, 255)',  # Light blue for atmosphere
        'opacity': 0.5,
        'name': 'Lower Atmosphere',
        'description': (
            "The lower atmosphere includes the troposphere (0-12 km) where weather occurs, and<br>"
            "the stratosphere (12-50 km) which contains the ozone layer. These regions contain<br>"
            "99% of atmospheric mass, primarily nitrogen and oxygen. Temperature varies from<br>"
            "about 15°C (59°F) at sea level to -60°C (-76°F) at the stratopause."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * EARTH_RADIUS_AU
    
    # Create sphere points
    x, y, z = create_sphere_points(layer_radius, n_points=50)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=2.5,
                color=layer_info['color'],
                opacity=layer_info['opacity']
            ),
            name=f"Earth: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Earth: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

earth_upper_atmosphere_info = (
            "The upper atmosphere extends from 50 km to about 1,000 km altitude. It includes\n"
            "the mesosphere where meteors burn up, the thermosphere where the aurora occurs and\n"
            "the International Space Station orbits, and the exosphere which gradually transitions\n"
            "to space. In the thermosphere, temperatures can reach 2,000°C (3,600°F), though the\n"
            "gas is so thin that it would feel cold to human skin."
)

def create_earth_upper_atmosphere_shell(center_position=(0, 0, 0)):
    """Creates Earth's upper atmosphere shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 1.25,  # Mesosphere, thermosphere, and exosphere
        'color': 'rgb(100, 150, 255)',  # Lighter blue
        'opacity': 0.3,
        'name': 'Upper Atmosphere',
        'description': (
            "The upper atmosphere extends from 50 km to about 1,000 km altitude. It includes<br>"
            "the mesosphere where meteors burn up, the thermosphere where the aurora occurs and<br>"
            "the International Space Station orbits, and the exosphere which gradually transitions<br>"
            "to space. In the thermosphere, temperatures can reach 2,000°C (3,600°F), though the<br>"
            "gas is so thin that it would feel cold to human skin."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * EARTH_RADIUS_AU
    
    # Create sphere points
    x, y, z = create_sphere_points(layer_radius, n_points=50)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=2.0,
                color=layer_info['color'],
                opacity=layer_info['opacity']
            ),
            name=f"Earth: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Earth: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    sun_traces = create_sun_direction_indicator(
        center_position=center_position, 
        shell_radius=layer_radius
    )
    for trace in sun_traces:
        traces.append(trace) 

    return traces

earth_magnetosphere_info = (
            "SET MANUAL SCALE TO AT LEAST 0.01 AU TO VISUALIZE.\n\n" 

            "Earth's magnetosphere extends about 10 Earth radii on the Sun-facing side\n"
            "and stretches into a long magnetotail on the night side. It protects Earth\n"
            "from solar radiation and cosmic rays, making complex life possible.\n\n"

            "Bow Shock: The boundary where the supersonic solar wind is first slowed\n"
            "by Earth's magnetic field, typically located about 15 Earth radii upstream\n"
            "from Earth on the Sun-facing side.\n\n"

            "Inner Van Allen Belt: Region of trapped charged particles (mainly protons)\n"
            "extending from about 1,000 km to 6,000 km above Earth's surface.\n"
            "Outer Van Allen Belt: Region of trapped charged particles (mainly electrons)\n"
            "extending from about 13,000 km to 60,000 km above Earth's surface."
)

def create_earth_magnetosphere_shell(center_position=(0, 0, 0)):
    """Creates Earth's magnetosphere."""
    traces = []
    
    # Parameters for magnetosphere components (in Earth radii)
    params = {
        # Compressed sunward side
        'sunward_distance': 10,  # Compressed toward the sun
        
        # Equatorial extension (wider than polar)
        'equatorial_radius': 12,
        'polar_radius': 10,
        
        # Magnetotail parameters
        'tail_length': 100,  # Length of visible magnetotail
        'tail_base_radius': 15,  # Radius at the base of the tail
        'tail_end_radius': 25,  # Radius at the end of the tail
        
        # Radiation belts
        'inner_belt_distance': 1.5,  # Distance in Earth radii
        'outer_belt_distance': 4.5,  # Distance in Earth radii
        'belt_thickness': 0.5,
    }
    
    # Scale everything by Earth's radius in AU
    for key in params:
        params[key] *= EARTH_RADIUS_AU
    
    # Create magnetosphere main shape
    x, y, z = create_magnetosphere_shape(params)
    
    # Unpack center position
    center_x, center_y, center_z = center_position
    
    # 1. Add the main magnetosphere structure
    x = np.array(x) + center_x
    y = np.array(y) + center_y
    z = np.array(z) + center_z
    
    magnetosphere_text = ["Earth's magnetosphere extends about 10 Earth radii on the Sun-facing side<br>"
                 "and stretches into a long magnetotail on the night side. It protects Earth<br>"
                 "from solar radiation and cosmic rays, making complex life possible."]
    
    magnetosphere_customdata = ['Earth: Magnetosphere']

    traces.append(
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=2.0,
                color='rgb(180, 180, 255)', # Light blue for magnetic field
                opacity=0.2
            ),
            name='Earth: Magnetosphere',
            text=magnetosphere_text * len(x),
            customdata=magnetosphere_customdata * len(x),      
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    )
    
    # 2. Create and add bow shock
    bow_shock_x = []
    bow_shock_y = []
    bow_shock_z = []
    
    n_phi = 30
    n_theta = 30
    bow_shock_standoff = 15 * EARTH_RADIUS_AU
    bow_shock_width = 25 * EARTH_RADIUS_AU
    
    # Create a paraboloid for the bow shock
    for i_phi in range(n_phi):
        phi = (i_phi / (n_phi-1)) * np.pi  # Only the front half
        
        for i_theta in range(n_theta):
            theta = (i_theta / (n_theta-1)) * 2 * np.pi
            
            # Paraboloid shape, flattened in x-direction for bow shock
            x = -bow_shock_standoff * np.cos(phi)  # Negative for sunward direction
            rho = bow_shock_width * (1 + np.sin(phi)) / 2  # Wider for larger phi (away from sun)
            y = rho * np.cos(theta)
            z = rho * np.sin(theta)
            
            bow_shock_x.append(x)
            bow_shock_y.append(y)
            bow_shock_z.append(z)
    
    # Apply center position offset
    bow_shock_x = np.array(bow_shock_x) + center_x
    bow_shock_y = np.array(bow_shock_y) + center_y
    bow_shock_z = np.array(bow_shock_z) + center_z
    
    bow_shock_text = ["Bow Shock: The boundary where the supersonic solar wind is first slowed<br>"
                "by Earth's magnetic field, typically located about 15 Earth radii upstream<br>"
                "from Earth on the Sun-facing side.<br>"
                "The Bow Shock points towards the Sun along the X-axis. The XY plane is the ecliptic."]
    
    bow_shock_customdata = ['Earth: Bow Shock']

    traces.append(
        go.Scatter3d(
            x=bow_shock_x,
            y=bow_shock_y,
            z=bow_shock_z,
            mode='markers',
            marker=dict(
                size=1.5,
                color='rgb(255, 200, 150)',  # Orange-ish color for bow shock
                opacity=0.2
            ),
            name='Earth: Bow Shock',
            text=bow_shock_text * len(bow_shock_x),
            customdata=bow_shock_customdata * len(bow_shock_x),  # This was the line causing the error
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    )
    
    # 3. Create and add Van Allen radiation belts
    belt_colors = ['rgb(255, 100, 100)', 'rgb(100, 200, 255)']
    belt_names = ['Earth: Inner Radiation Belt', 'Earth: Outer Radiation Belt']
    belt_texts = [
        "Inner Van Allen Belt: Region of trapped charged particles (mainly protons)<br>"
        "extending from about 1,000 km to 6,000 km above Earth's surface.",
        "Outer Van Allen Belt: Region of trapped charged particles (mainly electrons)<br>"
        "extending from about 13,000 km to 60,000 km above Earth's surface."
    ]
    
    belt_distances = [
        params['inner_belt_distance'],
        params['outer_belt_distance']
    ]
    
    for i, belt_distance in enumerate(belt_distances):
        belt_x = []
        belt_y = []
        belt_z = []
        
        n_points = 80
        n_rings = 5
        
        for i_ring in range(n_rings):
            # Vary the radius slightly to create thickness
            radius_offset = (i_ring / (n_rings-1) - 0.5) * params['belt_thickness']
            belt_radius = belt_distance + radius_offset
            
            for j in range(n_points):
                angle = (j / n_points) * 2 * np.pi
                
                # Create a belt around Earth's rotational axis
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
        
        belt_text = [belt_texts[i]]
        belt_customdata = [belt_names[i]]

        traces.append(
            go.Scatter3d(
                x=belt_x,
                y=belt_y,
                z=belt_z,
                mode='markers',
                marker=dict(
                    size=1.5,
                    color=belt_colors[i],
                    opacity=0.2
                ),
                name=belt_names[i],
                text=belt_text * len(belt_x),
                customdata=belt_customdata * len(belt_x),  # Fix here as well
                hovertemplate='%{text}<extra></extra>',
                showlegend=True
            )
        )
    
    sun_traces = create_sun_direction_indicator(
        center_position=center_position, 
        shell_radius=100 * EARTH_RADIUS_AU
    )
    for trace in sun_traces:
        traces.append(trace)

    return traces

earth_hill_sphere_info = (
            "SET MANUAL SCALE TO AT LEAST 0.02 AU TO VISUALIZE.\n\n" 
            "Earth's Hill Sphere (extends to ~235 Earth radii or about 1.5 million km)."
)

def create_earth_hill_sphere_shell(center_position=(0, 0, 0)):
    """Creates Earth's Hill sphere."""
    # Hill sphere radius in Earth radii
    radius_fraction = 235  # Earth's Hill sphere is about 235 Earth radii
    
    # Calculate radius in AU
    radius_au = radius_fraction * EARTH_RADIUS_AU
    
    # Create sphere points with fewer points for memory efficiency
    n_points = 30  # Reduced for large spheres
    x, y, z = create_sphere_points(radius_au, n_points=n_points)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    # Create hover text
    hover_text = ("Earth's Hill Sphere (extends to ~235 Earth radii or about 1.5 million km)<br><br>"
                "The Hill sphere is the region around a where its own gravity is the dominant force in attracting satellites. For <br>" 
                "a planet orbiting a star, it's the region where the planet's gravity is stronger than the star's tidal forces.<br><br>" 
                "The Hill Sphere radius can be described in words as follows: it is equal to the planet's average distance from the <br>" 
                "Sun (its orbital semi-major axis) multiplied by the cube root of the ratio between the planet's mass and three times <br>" 
                "the Sun's mass. In other words, you take how far the planet orbits out from the Sun, then scale that distance by the <br>" 
                "cube root of (planet mass ÷ [3 x solar mass]) to find the boundary within which the planet's gravity dominates over the Sun's."                  
                )
    
    # Create the trace
    traces = [
        go.Scatter3d(
            x=x,
            y=y,
            z=z,
            mode='markers',
            marker=dict(
                size=1.0,
                color='rgb(0, 255, 0)',  # Green for Hill sphere
                opacity=0.25
            ),
            name='Earth: Hill Sphere',
            text=[hover_text] * len(x),
            customdata=['Earth: Hill Sphere'] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    sun_traces = create_sun_direction_indicator(
        center_position=center_position, 
        shell_radius=radius_au
    )
    for trace in sun_traces:
        traces.append(trace) 

    return traces

