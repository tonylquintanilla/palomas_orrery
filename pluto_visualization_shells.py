import numpy as np
import math
import plotly.graph_objs as go
from planet_visualization_utilities import (PLUTO_RADIUS_AU, create_sphere_points)
from shared_utilities import create_sun_direction_indicator

# Pluto Shell Creation Functions

pluto_core_info = (
            "2.4 MB PER FRAME FOR HTML.\n\n"
            "Pluto core: Scientists believe Pluto has a dense, rocky core, likely composed of silicates and iron. The core's diameter \n" 
            "is hypothesized to be about 1700 km, which is approximately 70% of Pluto's total diameter. Heat generated from the decay \n" 
            "of radioactive elements within the core may still be present today."
)

def create_pluto_core_shell(center_position=(0, 0, 0)):
    """Creates pluto's core shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 0.70,  
        'color': 'rgb(255, 56, 0)',  # This represents a color that is strongly biased towards red with very little green and no blue.
        'opacity': 1.0,
        'name': 'Core',
        'description': (
            "Pluto core: Scientists believe Pluto has a dense, rocky core, likely composed of silicates and iron. The core's diameter <br>" 
            "is hypothesized to be about 1700 km, which is approximately 70% of Pluto's total diameter. Heat generated from the decay <br>" 
            "of radioactive elements within the core may still be present today.<br>" 
            "* Radioactive Isotopes: Based on theoretical models and our understanding of its composition and formation, scientists have made <br>" 
            "  estimations. Pluto's density suggests it differentiated early in its history, forming a rocky core and an icy mantle. <br>" 
            "  This differentiation process itself would have released heat. Like other rocky bodies in our solar system, Pluto's core <br>" 
            "  likely contains radioactive isotopes such as Uranium-238, Uranium-235, Thorium-232, and Potassium-40. The decay of these <br>" 
            "  elements over billions of years generates heat within the core. This is considered a primary source of its internal heat.<br>" 
            "* Initial Accretional Heat: The heat generated from the collisions of smaller bodies that accreted to form Pluto would have <br>" 
            "  also contributed to its initial core temperature. While much of this heat would have dissipated over time, some likely remains.<br>" 
            "* Subsurface Ocean Evidence: The potential presence of a subsurface liquid water ocean beneath Pluto's icy mantle suggests that <br>" 
            "  the core is warm enough to prevent this ocean from completely freezing. The heat flow from the core would be crucial for <br>" 
            "  maintaining this liquid layer.<br>" 
            "* Estimated Temperature: The estimated temperature of Pluto's core is around 1000 K. This estimate comes from models that <br>" 
            "  consider the heat generated by radioactive decay within a rocky core. These models also need to account for the heat transfer <br>" 
            "  through the icy mantle. Future research and more detailed data could refine this value. The exact temperature would depend on <br>" 
            "  the precise composition of the core and the efficiency of heat transfer through the mantle. In comparison, the surface <br>" 
            "  temperature of Pluto is extremely cold, around 40 K. The significant difference highlights the internal heating processes at <br>" 
            "  work within the dwarf planet. "
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * PLUTO_RADIUS_AU
    
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
            name=f"Pluto: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Pluto: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

pluto_mantle_info = (
            "2.1 MB PER FRAME FOR HTML.\n\n"
            "Mantle: Surrounding the rocky core is a mantle made of water ice. There's a compelling theory that a subsurface ocean \n" 
            "of liquid water, possibly mixed with ammonia, exists at the boundary between the core and the ice mantle. This ocean \n" 
            "could be 100 to 180 km thick. The presence of this ocean is supported by geological features observed on Pluto's surface."
)

def create_pluto_mantle_shell(center_position=(0, 0, 0)):
    """Creates pluto's mantle shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 0.99,  
        'color': 'rgb(150, 0, 0)',  # These still represent red but with a lower intensity,  
        'opacity': 0.9,
        'name': 'mantle',
        'description': (
            "mantle: Surrounding the rocky core is a mantle made of water ice. There's a compelling theory that a subsurface ocean <br>" 
            "of liquid water, possibly mixed with ammonia, exists at the boundary between the core and the ice mantle. This ocean <br>" 
            "could be 100 to 180 km thick. The presence of this ocean is supported by geological features observed on Pluto's surface.<br>" 
            "* This layer is primarily water ice. Within this icy mantle, there is strong evidence for a subsurface ocean of liquid <br>" 
            "  water, potentially mixed with ammonia, located above the rocky core.<br>" 
            "* Inner Icy Layer (if ocean exists): A layer of solid water ice may exist directly above the rocky core, potentially <br>" 
            "  forming the bottom of the ocean.<br>" 
            "* Subsurface Ocean: A layer of liquid water (possibly with dissolved substances). The thickness of this ocean is estimated <br>" 
            "  to be potentially 100 to 180 kilometers.<br>" 
            "* Outer Icy Layer (Lithosphere): A rigid outer shell of water ice above the potential ocean (or the main icy mantle if no <br>" 
            "  ocean is present). This layer is thought to be significant in thickness, potentially ranging from 45 to several hundred <br>" 
            "  kilometers."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * PLUTO_RADIUS_AU
    
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
            name=f"Pluto: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Pluto: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

pluto_crust_info = (
            "USE MANUAL SCALED OF 0.005 AU TO VIEW CLOSELY."
            "4.6 MB PER FRAME FOR HTML.\n\n"
            "Crust (Surface Layer): This is the outermost layer, composed of more volatile ices: primarily nitrogen ice, with smaller\n" 
            "amounts of methane and carbon monoxide ice. The thickness of this layer likely varies but is estimated to be relatively \n" 
            "thin in many regions, perhaps ranging from a few to tens of kilometers. In the deep Sputnik Planitia basin, the nitrogen \n" 
            "ice layer is estimated to be several kilometers thick and overlies the water-ice lithosphere."
)

def create_pluto_crust_shell(center_position=(0, 0, 0)):
    """Creates pluto's cloud layer shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 1.0,  # the top of the troposphere is actually 1.002
        'color': 'rgb(83, 68, 55)',  # optical brownish
        'opacity': 1.0,
        'name': 'Crust',
        'description': (
            "Pluto Crust<br>" 
            "(Note: toggle off the cloud layer in the legend to better see the interior structure.)<br><br>"
            "Crust (Surface Layer): This is the outermost layer, composed of more volatile ices: primarily nitrogen ice, with smaller <br>" 
            "amounts of methane and carbon monoxide ice. The thickness of this layer likely varies but is estimated to be relatively <br>" 
            "thin in many regions, perhaps ranging from a few to tens of kilometers. In the deep Sputnik Planitia basin, the nitrogen <br>" 
            "ice layer is estimated to be several kilometers thick and overlies the water-ice lithosphere.<br>" 
            "* Pluto's surface, or crust, is composed of various ices, primarily nitrogen ice (over 98%). It also contains smaller <br>" 
            "  amounts of methane and carbon monoxide ices.<br>" 
            "* Interestingly, mountains on Pluto can reach heights comparable to the Rocky Mountains on Earth and are believed to be <br>" 
            "  made of water ice, which is strong enough to support such structures at Pluto's frigid temperatures. These water-ice <br>" 
            "  mountains likely \"float\" in the denser nitrogen ice.<br>" 
            "* The surface exhibits a wide range of colors and brightness, with features like the bright \"heart\" (Tombaugh Regio) and <br>" 
            "  dark regions like Cthulhu Macula (\"the Whale\").<bR>" 
            "* Sputnik Planitia, the western lobe of the \"heart,\" is a vast basin of nitrogen and carbon monoxide ices showing <br>" 
            "  evidence of convection cells and glacial flow. The lack of impact craters in this region suggests it's geologically <br>" 
            "  young (possibly less than 10 million years old)."
            )
    }
    
    # Calculate radius in AU
    radius = layer_info['radius_fraction'] * PLUTO_RADIUS_AU
    
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
        name=f"Pluto: {layer_info['name']}",
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
    layer_name = f"Pluto: {layer_info['name']}"
    minimal_hover_texts = [layer_name] * len(x_hover)

    # Create hover trace with direct text assignment
    hover_trace = go.Scatter3d(
        x=x_hover, 
        y=y_hover, 
        z=z_hover,
        mode='markers',
        marker=dict(
            size=2,  # originally 5
            color='rgb(83, 68, 55)',  # brownish
            opacity=1.0,  # originally 0.8
            line=dict(  # Add a contrasting outline
                width=1,
                color='black'
            )
        ),
        name=f"Pluto: {layer_info['name']} (Info)",
        text=hover_texts,  # IMPORTANT: Matching length with coordinate arrays
        customdata=minimal_hover_texts,  # For "Object Names Only" mode
        hovertemplate='%{text}<extra></extra>',  # Use the standard hover template
        showlegend=False  # Don't show in legend since it's just for hover
    )

    return [surface_trace, hover_trace]

pluto_haze_layer_info = (
            "2.7 MB PER FRAME FOR HTML.\n\n"
            "Atmosphere: Pluto has a very thin atmosphere, about 1/100,000th the surface pressure of Earth's. It's primarily composed \n" 
            "of nitrogen (N₂), with smaller amounts of methane (CH₄) and carbon monoxide (CO). This atmosphere is dynamic and changes \n" 
            "with Pluto's orbit around the Sun. As Pluto moves farther away, the atmosphere freezes and falls to the surface as ice. \n" 
            "When it's closer to the Sun, the surface ice sublimates, forming a gaseous atmosphere. The atmosphere contains layers of \n" 
            "haze, extending up to 200 km above the surface, likely formed from the interaction of the atmospheric gases with high-energy \n" 
            "radiation. Counterintuitively, Pluto's upper atmosphere is significantly warmer than its surface due to a temperature \n" 
            "inversion, possibly caused by the presence of methane."
)

def create_pluto_haze_layer_shell(center_position=(0, 0, 0)):
    """Creates pluto's haze layer shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 1.17,  
        'color': 'rgb(135, 206, 235)',  # optical pale blue
        'opacity': 0.5,
        'name': 'Haze Layer',
        'description': (
            "Haze Layer: Pluto has a very thin atmosphere, about 1/100,000th the surface pressure of Earth's. It's primarily composed <br>" 
            "of nitrogen (N₂), with smaller amounts of methane (CH₄) and carbon monoxide (CO). This atmosphere is dynamic and changes <br>" 
            "with Pluto's orbit around the Sun. As Pluto moves farther away, the atmosphere freezes and falls to the surface as ice. <br>" 
            "When it's closer to the Sun, the surface ice sublimates, forming a gaseous atmosphere. The atmosphere contains layers of <br>" 
            "haze, extending up to 200 km above the surface, likely formed from the interaction of the atmospheric gases with high-energy <br>" 
            "radiation. Counterintuitively, Pluto's upper atmosphere is significantly warmer than its surface due to a temperature <br>" 
            "inversion, possibly caused by the presence of methane.<br>" 
            "* Composition and Formation: Pluto's atmosphere is primarily nitrogen (N₂) with smaller amounts of methane (CH₄) and <br>" 
            "  carbon monoxide (CO). The haze is thought to form when ultraviolet sunlight and high-energy radiation (like cosmic <br>" 
            "  rays) break apart methane molecules in the upper atmosphere. This breakdown leads to the formation of more complex <br>" 
            "  hydrocarbon gases, such as acetylene (C₂H₂) and ethylene (C₂H₄), as well as heavier compounds called tholins. As these <br>" 
            "  hydrocarbons drift to the lower, colder parts of the atmosphere, they condense into tiny ice particles, forming the haze. <br>" 
            "  Continued exposure to ultraviolet sunlight then chemically converts these haze particles into the dark, reddish-brown tholins <br>" 
            "  that contribute to the color of Pluto's surface.<br>" 
            "* Structure and Extent: The New Horizons mission revealed a surprisingly complex, multi-layered haze extending up to 200 km or <br>" 
            "  more above Pluto's surface. Scientists have observed as many as 20 distinct layers of haze. These layers can extend <br>" 
            "  horizontally for hundreds of kilometers and are not always perfectly parallel to the surface. There can be variations in haze <br>" 
            "  density and layer structure with altitude and even geographic location on Pluto.<br>" 
            "* Color: The haze has a blue tint when viewed in backlit images (like those taken as New Horizons sped away). This blue color <br>" 
            "  arises because the small haze particles efficiently scatter blue light from the sun.<br>" 
            "* Particle Settling: The haze particles eventually settle out of the atmosphere and onto Pluto's surface, contributing to the <br>" 
            "  surface composition and color over time.<br>" 
            "* Condensation and Coagulation: As particles descend, they can grow through condensation of atmospheric gases onto them and by <br>" 
            "  sticking together (coagulation).<br>" 
            "* Temperature Regulation: By absorbing infrared light, the haze can influence the atmospheric temperature profile, potentially <br>" 
            "  keeping the upper atmosphere cooler than it otherwise would be.<br>" 
            "* Haze Layers: Within the lower atmosphere, haze layers extend up to about 200 km altitude. This is approximately: ≈0.17 So, <br>" 
            "  the distinct haze layers reach about 0.17 Pluto radii above the surface." 
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * PLUTO_RADIUS_AU
    
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
            name=f"Pluto: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Pluto: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
        
    return traces

pluto_atmosphere_info = (
            "2.7 MB PER FRAME FOR HTML.\n\n"
            "Atmosphere: Pluto has a very thin atmosphere, about 1/100,000th the surface pressure of Earth's. It's primarily composed \n" 
            "of nitrogen (N₂), with smaller amounts of methane (CH₄) and carbon monoxide (CO). This atmosphere is dynamic and changes \n" 
            "with Pluto's orbit around the Sun. As Pluto moves farther away, the atmosphere freezes and falls to the surface as ice. \n" 
            "When it's closer to the Sun, the surface ice sublimates, forming a gaseous atmosphere. The atmosphere contains layers of \n" 
            "haze, extending up to 200 km above the surface, likely formed from the interaction of the atmospheric gases with high-energy \n" 
            "radiation. Counterintuitively, Pluto's upper atmosphere is significantly warmer than its surface due to a temperature \n" 
            "inversion, possibly caused by the presence of methane."
)

def create_pluto_atmosphere_shell(center_position=(0, 0, 0)):
    """Creates pluto's atmosphere shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 1.43,  
        'color': 'rgb(240, 245, 250)',  # optical pale blue
        'opacity': 0.3,
        'name': 'Atmosphere',
        'description': (
            "Atmosphere: Pluto has a very thin atmosphere, about 1/100,000th the surface pressure of Earth's. It's primarily composed <br>" 
            "of nitrogen (N₂), with smaller amounts of methane (CH₄) and carbon monoxide (CO). This atmosphere is dynamic and changes <br>" 
            "with Pluto's orbit around the Sun. As Pluto moves farther away, the atmosphere freezes and falls to the surface as ice. <br>" 
            "When it's closer to the Sun, the surface ice sublimates, forming a gaseous atmosphere. The atmosphere contains layers of <br>" 
            "haze, extending up to 200 km above the surface, likely formed from the interaction of the atmospheric gases with high-energy <br>" 
            "radiation. Counterintuitively, Pluto's upper atmosphere is significantly warmer than its surface due to a temperature <br>" 
            "inversion, possibly caused by the presence of methane.<br>" 
            "The extent of Pluto's atmosphere is surprisingly large relative to the dwarf planet itself. While it's very thin in terms <br>" 
            "of density compared to Earth's, it stretches far out into space. Here's a breakdown in terms of Pluto's radius <br>" 
            "(approximately 1188 km):<br>" 
            "* Significant Atmosphere: The atmosphere, composed primarily of nitrogen with traces of methane and carbon monoxide, has <br>" 
            "  been detected extending up to 1700 km above the surface (the exobase).<br>" 
            "* In Pluto radii: To express this as a fraction of Pluto's radius: ≈1.43.<br>" 
            "* Outer Limits: Some research suggests that the outer, most tenuous parts of Pluto's atmosphere might extend even further, <br>" 
            "  perhaps to several times Pluto's radius, gradually merging with the vacuum of space. One New Horizons science brief even <br>" 
            "  mentioned an outer limit potentially as far as seven times Pluto's radius, although this is very ill-defined.<br>" 
            "* Haze Layers: Within the lower atmosphere, haze layers extend up to about 200 km altitude. This is approximately: ≈0.17 So, <br>" 
            "  the distinct haze layers reach about 0.17 Pluto radii above the surface.<br>" 
            "In summary, while the bulk of Pluto's atmosphere is very thin, its outer reaches are quite extended. For a general extent, <br>" 
            "considering the exobase, the atmosphere reaches about 0.43 Pluto radii above the surface, or 1.43 Pluto radii from the center. <br>" 
            "If you consider the more diffuse outer limits, it could be even larger."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * PLUTO_RADIUS_AU
    
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
            name=f"Pluto: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Pluto: {layer_info['name']}"] * len(x),
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

pluto_hill_sphere_info = (
            "SELECT MANUAL SCALE OF AT LEAST 0.1 AU TO VISUALIZE.\n" 
            "1.3 MB PER FRAME FOR HTML.\n\n"

            "Hill Sphere: Pluto's Hill sphere, or Roche sphere, is the region around it where its gravitational influence dominates \n" 
            "over the Sun's. The radius of Pluto's Hill sphere is quite large, approximately 5.99 million kilometers (0.04 AU). This is \n" 
            "significantly larger than Earth's Hill sphere in terms of volume. Any moon orbiting Pluto within this sphere is \n" 
            "gravitationally bound to it. Pluto has five known moons: Charon, Styx, Nix, Kerberos, and Hydra, all of which reside within \n" 
            "its Hill sphere."                     
)

def create_pluto_hill_sphere_shell(center_position=(0, 0, 0)):
    """Creates pluto's Hill sphere shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 4685, 
        'color': 'rgb(0, 255, 0)',  # Green for Hill sphere
        'opacity': 0.25,
        'name': 'Hill Sphere',
        'description': (
            "SET MANUAL SCALE OF AT LEAST 0.05 AU TO VISUALIZE.<br><br>"
            "Hill Sphere: Pluto's Hill sphere, or Roche sphere, is the region around it where its gravitational influence dominates <br>" 
            "over the Sun's. The radius of Pluto's Hill sphere is quite large, approximately 5.99 million kilometers (0.04 AU). This is <br>" 
            "significantly larger than Earth's Hill sphere in terms of volume. Any moon orbiting Pluto within this sphere is <br>" 
            "gravitationally bound to it. Pluto has five known moons: Charon, Styx, Nix, Kerberos, and Hydra, all of which reside within <br>" 
            "its Hill sphere."          
            )
    }
        
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * PLUTO_RADIUS_AU
    
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
            name=f"Pluto: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Pluto: {layer_info['name']}"] * len(x),
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