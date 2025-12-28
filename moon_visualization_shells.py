import numpy as np
import math
import plotly.graph_objs as go
from planet_visualization_utilities import (MOON_RADIUS_AU, create_sphere_points, create_magnetosphere_shape)
from shared_utilities import create_sun_direction_indicator

# Moon Shell Creation Functions

moon_inner_core_info = (
            "The Moon has a small, partially molten core. Seismic data from Apollo missions and more recent studies of the Moon\'s wobble suggest:\n" 
            "* Inner Core: Believed to be a solid, iron-rich core, roughly 240 kilometers in radius."
)

def create_moon_inner_core_shell(center_position=(0, 0, 0)):
    """Creates the Moon's inner core shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 0.1485,  
        'color': 'rgb(255, 100, 0)',  # dark red-orange at 1700K
        'opacity': 1.0,
        'name': 'Inner Core',
        'description': (
            "The Moon has a small, partially molten core. Seismic data from Apollo missions and more recent studies of the Moon\'s wobble suggest:<br>" 
            "* Inner Core: Believed to be a solid, iron-rich core, roughly 240 kilometers in radius:<br>" 
            "  * Estimates for the temperature of the Moon\'s inner core vary slightly depending on the studies and methods used, but <br>" 
            "    some more recent reanalyses of seismic data suggest temperatures around 1600-1700 K." 
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * MOON_RADIUS_AU
    
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
            name=f"Moon: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Moon: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

moon_outer_core_info = (
            "Outer Core: Surrounding the inner core, this is thought to be a liquid, iron-rich outer core with a radius of about \n" 
            "330 kilometers. There might also be a small, partially molten layer of silicates around the outer core."
)

def create_moon_outer_core_shell(center_position=(0, 0, 0)):
    """Creates the Moon's outer core shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 0.2083,  
        'color': 'rgb(255, 50, 0)',  # very dark, deep red, almost a "charcoal red" or "ember red"
        'opacity': 0.8,
        'name': 'Outer Core',
        'description': (
            "Outer Core: Surrounding the inner core, this is thought to be a liquid, iron-rich outer core with a radius of about <br>" 
            "330 kilometers. There might also be a small, partially molten layer of silicates around the outer core.<br>:" 
            "* The Moon's outer core is generally understood to be hotter than its solid inner core, as it is in a molten or liquid <br>" 
            "  state. <br>" 
            "* Estimated Temperature: This layer would be slightly cooler than the inner core, but still hot enough to be molten at <br>" 
            "  the lower pressures found here. Estimates typically fall around 1300 K to 1600 K. Let's use 1500 K as a representative <br>" 
            "  value for the outer core for your model.<br>" 
            "* Reasoning: As you move outwards, the temperature gradually decreases, but crucially, the pressure also decreases. At this <br>" 
            "  depth and pressure, the temperature is above the melting point of the iron-rich material, allowing it to be liquid."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * MOON_RADIUS_AU
    
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
            name=f"Moon: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Moon: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

moon_mantle_info = (
            "Above the core lies the Moon's mantle, which makes up the bulk of its interior:\n" 
            "* Composition: Primarily composed of silicate rocks, similar to Earth's mantle, but with different proportions of \n" 
            "  elements. It's thought to be rich in olivine and pyroxene.\n" 
            "* State: The Moon's mantle is largely solid today. However, in its early history, it would have been at least partially \n" 
            "  molten, leading to volcanic activity that formed the vast maria (dark plains) on the lunar surface.\n" 
            "* Lunar Deep Moonquakes: Seismometers left by Apollo missions detected \"deep moonquakes\" originating in the mantle at \n" 
            "  depths of 700 to 1,200 km (435-745 miles). These are likely caused by tidal stresses from Earth."
)

def create_moon_mantle_shell(center_position=(0, 0, 0)):
    """Creates the Moon's lower mantle shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 0.85,  # Lower mantle: 55-85% of Earth's radius
        'color': 'rgb(0, 50, 0)',  # very dark green for peridotite
        'opacity': 0.9655,
        'name': 'Mantle',
        'description': (
            "Above the core lies the Moon's mantle, which makes up the bulk of its interior:<br>" 
            "* Composition: Primarily composed of silicate rocks, similar to Earth's mantle, but with different proportions of <br>" 
            "  elements. It's thought to be rich in olivine and pyroxene.<br>" 
            "* State: The Moon's mantle is largely solid today. However, in its early history, it would have been at least partially <br>" 
            "  molten, leading to volcanic activity that formed the vast maria (dark plains) on the lunar surface.<br>" 
            "* Lunar Deep Moonquakes: Seismometers left by Apollo missions detected \"deep moonquakes\" originating in the mantle at <br>" 
            "  depths of 700 to 1,200 km (435-745 miles). These are likely caused by tidal stresses from Earth.<br>" 
            "* The Moon's mantle is a thick, largely solid layer, and its temperature varies significantly with depth, becoming <br>" 
            "  cooler as you move outwards towards the crust.<br>" 
            "  * Estimates for the temperature at the boundary between the mantle and the outer core range from 1573 K to 1743 K.<br>" 
            "  * Estimates for the crust-mantle boundary are roughly 623 K to 823 K.<br>" 
            "* The \"Draper point\" is around 798 K, which is the approximate temperature at which all solids start to glow a dim <br>" 
            "  red. Therefore, the upper mantle, at these temperatures, would not visibly glow from black body radiation in normal <br>" 
            "  conditions. Its primary emission would be in the infrared spectrum, invisible to the human eye. For the bulk of the <br>" 
            "  mantle, it is primarily composed of silicate rocks like olivine and pyroxene. When seen in rock samples, these tend <br>" 
            "  to be dark greenish to black (e.g., peridotite).<br>" 
            "* Outer boundary of the mantle (base of the crust) as a fraction of Rm: 1677.4 km/1737.4 km~0.9655"
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * MOON_RADIUS_AU
    
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
            name=f"Moon: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Moon: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

moon_crust_info = (
            "The outermost layer of the Moon is its crust, which is significantly thicker on the far side than on the near side:\n" 
            "* Composition: Dominated by anorthositic rocks (rich in plagioclase feldspar), which are lighter in color and form the \n" 
            "  lunar highlands. The dark maria, on the other hand, are vast basaltic plains formed by ancient volcanic eruptions that \n" 
            "  filled large impact basins.<br>" 
            "* Thickness: The lunar crust varies in thickness. On the near side (facing Earth), it's estimated to be around 30-50 \n" 
            "  kilometers thick. On the far side, it can be much thicker, possibly reaching up to 100 kilometers or more. This \n" 
            "  asymmetry is a major characteristic of the Moon. The most compelling explanations for the Moon's crustal thickness \n" 
            "  asymmetry point to a combination of factors related to its formation in Earth\'s intense thermal environment and a \n" 
            "  massive early impact that shaped its internal heat distribution and subsequent geological evolution.\n" 
            "* Surface Features: The crust is heavily cratered due to billions of years of impacts from asteroids and comets. Other \n" 
            "  features include rilles (channels, often associated with lava flows), domes, and wrinkle ridges."
)

def create_moon_crust_shell(center_position=(0, 0, 0)):
    """Creates Earth's crust shell using Mesh3d for better performance with improved hover."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 1.0,  
        'color': 'rgb(190, 190, 180)',  # slightly warm grey
        'opacity': 1.0,
        'name': 'Crust',
        'description': (
            "The outermost layer of the Moon is its crust, which is significantly thicker on the far side than on the near side:<br>" 
            "* Composition: Dominated by anorthositic rocks (rich in plagioclase feldspar), which are lighter in color and form the <br>" 
            "  lunar highlands. The dark maria, on the other hand, are vast basaltic plains formed by ancient volcanic eruptions that <br>" 
            "  filled large impact basins.<br>" 
            "* Thickness: The lunar crust varies in thickness. On the near side (facing Earth), it's estimated to be around 30-50 <br>" 
            "  kilometers thick. On the far side, it can be much thicker, possibly reaching up to 100 kilometers or more. This <br>" 
            "  asymmetry is a major characteristic of the Moon. The most compelling explanations for the Moon's crustal thickness <br>" 
            "  asymmetry point to a combination of factors related to its formation in Earth\'s intense thermal environment and a <br>" 
            "  massive early impact that shaped its internal heat distribution and subsequent geological evolution.<br>" 
            "* Surface Features: The crust is heavily cratered due to billions of years of impacts from asteroids and comets. Other <br>" 
            "  features include rilles (channels, often associated with lava flows), domes, and wrinkle ridges.<br>" 
            "* Given the mix of lighter highlands and darker maria, and the overall neutral tone, a medium, slightly warm grey.<br>" 
            "* Unlike Earth, the Moon does not have a global, internally generated magnetic field today. However, rocks collected <br>" 
            "  during the Apollo missions showed evidence of remnant magnetism, indicating that the Moon did possess a global <br>" 
            "  magnetic field in its early history, likely generated by a liquid core dynamo similar to Earth's. Today, there are <br>" 
            "  localized magnetic anomalies on the lunar surface, thought to be remnants of this ancient magnetic field or perhaps <br>" 
            "  due to impact processes. These regions can sometimes interact with the solar wind, creating small <br>" 
            "  \"mini-magnetospheres.\".<br>" 
            "* Solar Wind Interaction: Without a global magnetic field, the Moon is directly exposed to the solar wind, a stream of <br>" 
            "  charged particles from the Sun. This constant bombardment contributes to space weathering of the lunar surface.<br>" 
            "* Water Ice: One of the most significant discoveries in recent lunar exploration is the confirmed presence of water ice, <br>" 
            "  particularly in permanently shadowed regions within craters at the Moon\'s poles.<br>" 
            "* Regolith: The entire lunar surface is covered by a layer of fine, powdery dust and broken rock fragments called regolith. <br>" 
            "  It\'s formed by billions of years of micrometeoroid impacts and varies in thickness from a few meters in the maria to tens <br>" 
            "  of meters in the highlands.<br>" 
            "* Tidally Locked: The Moon is tidally locked with Earth, meaning the same side of the Moon (the \"near side\") always faces <br>" 
            "  Earth."
        )
    }
    
    # Calculate radius in AU
    radius = layer_info['radius_fraction'] * MOON_RADIUS_AU
    
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
        name=f"Moon: {layer_info['name']}",
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
    layer_name = f"Moon: {layer_info['name']}"
    minimal_hover_texts = [layer_name] * len(x_hover)

    # Create hover trace with direct text assignment
    hover_trace = go.Scatter3d(
        x=x_hover, 
        y=y_hover, 
        z=z_hover,
        mode='markers',
        marker=dict(
            size=2,  # originally 5
            color='rgb(190, 190, 180)',  # Layer color
            opacity=1.0,  # originally 0.8
            line=dict(  # Add a contrasting outline
                width=1,
                color='black'
            )
        ),
        name=f"Moon: {layer_info['name']} (Info)",
        text=hover_texts,  # IMPORTANT: Matching length with coordinate arrays
        customdata=minimal_hover_texts,  # For "Object Names Only" mode
        hovertemplate='%{text}<extra></extra>',  # Use the standard hover template
        showlegend=False  # Don't show in legend since it's just for hover
    )

    return [surface_trace, hover_trace]

moon_exosphere_info = (
            "The Moon essentially has no atmosphere in the traditional sense. Instead, it has an exosphere. It's an incredibly \n" 
            "tenuous layer of gases, far less dense than a vacuum on Earth. It's so thin that gas molecules rarely collide with \n" 
            "each other.\n" 
            "* Sources: The exosphere is formed from gases released from the Moon\'s interior from radioactive decay, outgassing \n" 
            "  from the surface due to solar wind bombardment, and micrometeoroid impacts.\n" 
            "* Composition: Primarily composed of noble gases like argon and helium, along with trace amounts of sodium, potassium, \n" 
            "  hydrogen, and other elements.\n" 
            "* No Weather: Due to its extreme thinness, there's no atmospheric pressure, no wind, no weather, and no significant \n" 
            "  shielding from solar radiation or micrometeoroids."
)

def create_moon_exosphere_shell(center_position=(0, 0, 0)):
    """Creates the Moon's exosphere shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 1.06, 
        'color': 'rgb(100, 150, 255)',  # Lighter blue
        'opacity': 0.3,
        'name': 'Exosphere',
        'description': (
            "The Moon essentially has no atmosphere in the traditional sense. Instead, it has an exosphere. It's an incredibly <br>" 
            "tenuous layer of gases, far less dense than a vacuum on Earth. It's so thin that gas molecules rarely collide with <br>" 
            "each other.<br>" 
            "* Sources: The exosphere is formed from gases released from the Moon\'s interior from radioactive decay, outgassing <br>" 
            "  from the surface due to solar wind bombardment, and micrometeoroid impacts.<br>" 
            "* Composition: Primarily composed of noble gases like argon and helium, along with trace amounts of sodium, potassium, <br>" 
            "  hydrogen, and other elements.<br>" 
            "* No Weather: Due to its extreme thinness, there's no atmospheric pressure, no wind, no weather, and no significant <br>" 
            "  shielding from solar radiation or micrometeoroids.<br>"  
            "* Practical or \"Dense\" Extent: For most practical purposes, where collisions between particles are still somewhat <br>" 
            "  relevant or where density is higher, the exosphere is often considered to extend up to about 100 kilometers above <br>" 
            "  the lunar surface. So, a more \"dense\" part of the exosphere extends from 1.0 Rm to roughly 1.06 Rm."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * MOON_RADIUS_AU
    
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
            name=f"Moon: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Moon: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

moon_hill_sphere_info = (
            "SET MANUAL SCALE TO AT LEAST 0.001 AU TO VISUALIZE.\n\n" 
            "The Moon's Hill sphere (also known as the Roche sphere in this context) is the region around it where its own gravity \n" 
            "is the dominant force attracting satellites, as opposed to the much stronger gravitational pull of the Earth. If an \n" 
            "object is outside the Moon\'s Hill sphere, it would typically end up orbiting Earth instead of the Moon.\n" 
            "* The estimated radius of the Moon's Hill sphere is approximately 60,000 kilometers, approximately 34.53 lunar radii." 
            )

def create_moon_hill_sphere_shell(center_position=(0, 0, 0)):
    """Creates the Moon's Hill sphere."""
    # Hill sphere radius in Moonn radii
    radius_fraction = 34.53  
    
    # Calculate radius in AU
    radius_au = radius_fraction * MOON_RADIUS_AU
    
    # Create sphere points with fewer points for memory efficiency
    n_points = 30  # Reduced for large spheres
    x, y, z = create_sphere_points(radius_au, n_points=n_points)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    # Create hover text
    hover_text = (
            "The Moon's Hill sphere (also known as the Roche sphere in this context) is the region around it where its own gravity <br>" 
            "is the dominant force attracting satellites, as opposed to the much stronger gravitational pull of the Earth. If an <br>" 
            "object is outside the Moon\'s Hill sphere, it would typically end up orbiting Earth instead of the Moon.<br>" 
            "* The estimated radius of the Moon's Hill sphere is approximately 60,000 kilometers, approximately 34.53 lunar radii." 
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
            name='Hill Sphere',
            text=[hover_text] * len(x),
            customdata=['Hill Sphere'] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True

        )
    ]
    
    return traces

