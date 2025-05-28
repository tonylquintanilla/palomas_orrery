import numpy as np
import math
import plotly.graph_objs as go
from planet_visualization_utilities import (ERIS_RADIUS_AU, create_sphere_points)
from shared_utilities import create_sun_direction_indicator

# Eris Shell Creation Functions

eris_core_info = (
            "2.4 MB PER FRAME FOR HTML.\n\n"
            "Eris, a dwarf planet in the Kuiper Belt, has a structure that scientists have been piecing together through observations \n" 
            "and theoretical modeling. Here's what we currently understand:\n" 
            "Core: Eris is believed to have a rocky core. Its high bulk density (around 2.5 g/cm³) suggests that it is composed \n" 
            "primarily of rock, making up a significant portion of its mass (possibly over 85%). This core likely contains radioactive \n" 
            "elements, which produce internal heat."
)

def create_eris_core_shell(center_position=(0, 0, 0)):
    """Creates Eris's core shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 0.60,  # range is .5 to .65
        'color': 'rgb(187, 63, 63)',  # dull red at 875 K
        'opacity': 1.0,
        'name': 'Core',
        'description': (
            "Eris, a dwarf planet in the Kuiper Belt, has a structure that scientists have been piecing together through observations <br>" 
            "and theoretical modeling. Here's what we currently understand:<br>" 
            "Core: Eris is believed to have a rocky core. Its high bulk density (around 2.5 g/cm³) suggests that it is composed <br>" 
            "primarily of rock, making up a significant portion of its mass (possibly over 85%). This core likely contains radioactive <br>" 
            "elements, which produce internal heat.<br>" 
            "* Determining the precise radius fraction of Eris's core is challenging because we don't have direct observations of its <br>" 
            "  internal structure. However, we can make estimations based on its known properties:<br>" 
            "  * Total Radius: Eris has a radius of approximately 1163 ± 6 kilometers.<br>" 
            "  * Density: Its density is estimated to be around 2.52 ± 0.07 g/cm³. This high density suggests a significant rocky component.<br>" 
            "  * Compositional Models: Based on its density, scientists believe Eris is composed largely of rock (possibly over 85% of its <br>" 
            "    mass) with the remainder being primarily water ice. The ice forms the mantle surrounding the rocky core.<br>" 
            "* Considering these factors, and drawing comparisons to other icy bodies with rocky cores like Europa or Ganymede in the outer <br>" 
            "  solar system, a reasonable estimate for the radius fraction of Eris's core would likely be around 50-65% of its total radius. <br>" 
            "  To achieve Eris's high bulk density with a significant ice mantle, the denser rocky core must occupy a substantial portion of <br>" 
            "  its volume. If the core were much smaller (a smaller radius fraction), the overall density would likely be lower, given the <br>" 
            "  lower density of water ice. Conversely, if the core occupied a much larger fraction, there would be less room for the <br>" 
            "  substantial ice mantle that is believed to exist. Therefore, while we don't have a definitive number, the rocky core of Eris <br>" 
            "  likely makes up roughly half to two-thirds of its total radius.<br>" 
            "* Temperature:<br>" 
            "  * Radiogenic Heating: The rocky core of Eris likely contains radioactive isotopes (such as uranium, thorium, and <br>" 
            "    potassium) that decay over time, releasing heat.<br>" 
            "  * Recent research based on data from the James Webb Space Telescope provides indirect evidence for a warm, potentially <br>" 
            "    even hot, rocky core in Eris. The detection of a moderate deuterium-to-hydrogen (D/H) ratio in methane ice on its surface <br>" 
            "    suggests that the methane was likely produced through geochemical processes in the interior, requiring elevated <br>" 
            "    temperatures (possibly above 150°C or 300°F) within the rocky core. Theoretical modeling of Eris's interior, considering <br>" 
            "    radiogenic heating and thermal conductivity, suggests that the central temperature could have been as high as 875 K.<br>" 
            "  * This warmth might even be sufficient to support a subsurface ocean at the core-mantle boundary."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * ERIS_RADIUS_AU
    
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
            name=f"Eris/Dysnomia: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Eris/Dysnomia: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

eris_mantle_info = (
            "2.1 MB PER FRAME FOR HTML.\n\n"
            "Mantle: Surrounding the rocky core is a substantial mantle made of water ice. Unlike Pluto's ice shell, Eris's ice \n" 
            "mantle is thought to be convecting. This means that the warmer ice closer to the core rises, while the colder ice near \n" 
            "the surface sinks, a process that helps dissipate the internal heat generated by the core. The thickness of this ice \n" 
            "shell is estimated to be around 100 kilometers. There is currently no evidence to suggest the presence of a subsurface \n" 
            "ocean within Eris."
)

def create_eris_mantle_shell(center_position=(0, 0, 0)):
    """Creates Eris's mantle shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 0.66,  
        'color': 'rgb(150, 0, 0)',  # These still represent red but with a lower intensity,  
        'opacity': 0.9,
        'name': 'Mantle',
        'description': (
            "Mantle: Surrounding the rocky core is a substantial mantle made of water ice. Unlike Pluto's ice shell, Eris's ice <br>" 
            "mantle is thought to be convecting. This means that the warmer ice closer to the core rises, while the colder ice near <br>" 
            "the surface sinks, a process that helps dissipate the internal heat generated by the core. The thickness of this ice <br>" 
            "shell is estimated to be around 100 kilometers. There is currently no evidence to suggest the presence of a subsurface <br>" 
            "ocean within Eris.<br>"
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * ERIS_RADIUS_AU
    
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
                size=3.5,
                color=layer_info['color'],
                opacity=layer_info['opacity']
            ),
            name=f"Eris/Dysnomia: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Eris/Dysnomia: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

eris_crust_info = (
            "USE MANUAL SCALED OF 0.005 AU TO VIEW CLOSELY."
            "4.6 MB PER FRAME FOR HTML.\n\n"
            "Crust: The outermost layer is a crust of frozen gases, primarily nitrogen and methane ice. Eris has a very high albedo \n" 
            "(reflectivity), reflecting about 96% of the sunlight that hits it. This bright surface is likely due to a frost layer \n" 
            "formed from the condensation of its atmosphere when it is far from the Sun."
)

def create_eris_crust_shell(center_position=(0, 0, 0)):
    """Creates eris's cloud layer shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 1.0,  # the top of the troposphere is actually 1.002
        'color': 'rgb(240, 240, 240)',  # optical, a color that is very close to white but with a slight hint of gray
        'opacity': 1.0,
        'name': 'Crust',
        'description': (
            "Eris Crust<br>" 
            "(Note: toggle off the cloud layer in the legend to better see the interior structure.)<br><br>"
            "Crust: The outermost layer is a crust of frozen gases, primarily nitrogen and methane ice. Eris has a very high albedo <br>" 
            "(reflectivity), reflecting about 96% of the sunlight that hits it. This bright surface is likely due to a frost layer <br>" 
            "formed from the condensation of its atmosphere when it is far from the Sun.<br>" 
            "* The optical color of Eris is primarily characterized by its very high albedo, meaning it reflects a large percentage <br>" 
            "  of the sunlight that hits it (around 96%). This high reflectivity is due to a relatively fresh layer of frozen nitrogen <br>" 
            "  and methane on its surface. The color is largely that of the illuminating source (the Sun). <br>" 
            "* Atmospheric effects (if any): Although its atmosphere is currently thought to be very thin or mostly frozen, any past or <br>" 
            "  transient atmosphere could have slightly altered the light scattering and thus the observed color."
            )
    }
    
    # Calculate radius in AU
    radius = layer_info['radius_fraction'] * ERIS_RADIUS_AU
    
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
        name=f"Eris/Dysnomia: {layer_info['name']}",
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
    layer_name = f"Eris/Dysnomia: {layer_info['name']}"
    minimal_hover_texts = [layer_name] * len(x_hover)

    # Create hover trace with direct text assignment
    hover_trace = go.Scatter3d(
        x=x_hover, 
        y=y_hover, 
        z=z_hover,
        mode='markers',
        marker=dict(
            size=2,  # originally 5
            color='rgb(240, 240, 240)',  
            opacity=1.0,  # originally 0.8
            line=dict(  # Add a contrasting outline
                width=1,
                color='black'
            )
        ),
        name=f"Eris/Dysnomia: {layer_info['name']} (Info)",
        text=hover_texts,  # IMPORTANT: Matching length with coordinate arrays
        customdata=minimal_hover_texts,  # For "Object Names Only" mode
        hovertemplate='%{text}<extra></extra>',  # Use the standard hover template
        showlegend=False  # Don't show in legend since it's just for hover
    )

    return [surface_trace, hover_trace]

eris_atmosphere_info = (
            "2.7 MB PER FRAME FOR HTML.\n\n"
            "Atmosphere: Eris has a very tenuous atmosphere that is dynamic. When Eris is at its farthest point from the Sun \n" 
            "(aphelion), the extremely cold temperatures cause its atmosphere, likely composed of nitrogen and methane, to freeze \n" 
            "and fall as snow onto the surface. As Eris moves closer to the Sun in its highly elliptical orbit (perihelion), the \n" 
            "surface warms up, and these ices sublimate, potentially creating a temporary atmosphere similar to Pluto's. However, \n" 
            "observations have placed a very low upper limit on the current atmospheric pressure, suggesting it is currently very \n" 
            "thin or mostly frozen."
)

def create_eris_atmosphere_shell(center_position=(0, 0, 0)):
    """Creates eris's atmosphere shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 1.005,  # almost none and intermittent
        'color': 'rgb(240, 245, 250)',  # optical pale blue
        'opacity': 0.1,
        'name': 'Atmosphere',
        'description': (
            "Atmosphere: Eris has a very tenuous atmosphere that is dynamic. When Eris is at its farthest point from the Sun <br>" 
            "(aphelion), the extremely cold temperatures cause its atmosphere, likely composed of nitrogen and methane, to freeze <br>" 
            "and fall as snow onto the surface. As Eris moves closer to the Sun in its highly elliptical orbit (perihelion), the <br>" 
            "surface warms up, and these ices sublimate, potentially creating a temporary atmosphere similar to Pluto's. However, <br>" 
            "observations have placed a very low upper limit on the current atmospheric pressure, suggesting it is currently very <br>" 
            "thin or mostly frozen.<br>" 
            "* The current understanding of Eris's atmosphere is that it is extremely tenuous, with an upper limit on surface <br>" 
            "  pressure of about 1 nanobar. This is about 10,000 times thinner than Pluto's current atmosphere. Given such a low <br>" 
            "  pressure, the extent of the atmosphere in terms of Eris's radii would be very small and likely not easily definable <br>" 
            "  in a significant way.<br>" 
            "* Near-Surface Existence: At such low pressures, the \"atmosphere\" is likely confined to a very thin layer near the <br>" 
            "  surface. The density of gas molecules would drop off extremely rapidly with altitude.<br>" 
            "* Collapse at Aphelion: Eris is currently near its aphelion (farthest point from the Sun). At these extremely cold <br>" 
            "  temperatures (around -240°C), the primary atmospheric constituents, nitrogen and methane, would freeze and deposit <br>" 
            "  as frost on the surface. Any atmosphere present would be minimal.<br>" 
            "* Potential Sublimation at Perihelion: As Eris gets closer to the Sun (perihelion), the surface temperature will increase <br>" 
            "  slightly, potentially causing some of these ices to sublimate and form a transient, thin atmosphere. However, even in <br>" 
            "  this case, the extent is not expected to be a significant fraction of Eris's radius. In practical terms, the extent of <br>" 
            "  Eris's atmosphere in radii is considered negligible for most structural considerations. Scientists often discuss the <br>" 
            "  surface composition and potential for a thin, dynamic atmosphere rather than a significant, extended gaseous envelope. <br>" 
            "* To put it in perspective: if Eris had an atmosphere that extended even a few kilometers, that would be a tiny fraction <br>" 
            "  (less than 0.01) of its total radius. The current observational limits suggest it's likely much less than that for a <br>" 
            "  sustained atmosphere at its current distance from the Sun."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * ERIS_RADIUS_AU
    
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
                size=3.0,
                color=layer_info['color'],
                opacity=layer_info['opacity']
            ),
            name=f"Eris/Dysnomia: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Eris/Dysnomia: {layer_info['name']}"] * len(x),
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

eris_hill_sphere_info = (
            "SELECT MANUAL SCALE OF AT LEAST 0.1 AU TO VISUALIZE.\n" 
            "1.3 MB PER FRAME FOR HTML.\n\n"

            "Hill Sphere: The Hill sphere, or Roche sphere, of Eris is the region around it where its own gravity is the dominant \n" 
            "force attracting satellites. For Eris, the radius of its Hill sphere is estimated to be about 8.1 million kilometers \n" 
            "(0.054 astronomical units). This is the region where its moon, Dysnomia, orbits. Any object within this sphere is more \n" 
            "likely to be gravitationally bound to Eris."                      
)

def create_eris_hill_sphere_shell(center_position=(0, 0, 0)):
    """Creates Eris's Hill sphere shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 6965, 
        'color': 'rgb(0, 255, 0)',  # Green for Hill sphere
        'opacity': 0.25,
        'name': 'Hill Sphere',
        'description': (
            "SET MANUAL SCALE OF AT LEAST 0.05 AU TO VISUALIZE.<br><br>"
            "Hill Sphere: The Hill sphere, or Roche sphere, of Eris is the region around it where its own gravity is the dominant <br>" 
            "force attracting satellites. For Eris, the radius of its Hill sphere is estimated to be about 8.1 million kilometers <br>" 
            "(0.054 astronomical units). This is the region where its moon, Dysnomia, orbits. Any object within this sphere is more <br>" 
            "likely to be gravitationally bound to Eris.<br>" 
            "* The region where Eris's gravity is the dominant force attracting satellites extends to a distance of roughly 6965 <br>" 
            "  Eris radii from its center."          
            )
    }
        
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * ERIS_RADIUS_AU
    
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
            name=f"Eris/Dysnomia: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Eris/Dysnomia: {layer_info['name']}"] * len(x),
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