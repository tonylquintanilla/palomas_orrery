import numpy as np
import math
import plotly.graph_objs as go
from planet_visualization_utilities import (SATURN_RADIUS_AU, KM_PER_AU, create_sphere_points, create_magnetosphere_shape, rotate_points)
from shared_utilities import create_sun_direction_indicator

def create_ring_points_saturn (inner_radius, outer_radius, n_points, thickness=0):
    """
    Create points for a ring with inner and outer radius.
    
    Parameters:
        inner_radius (float): Inner radius of the ring
        outer_radius (float): Outer radius of the ring
        n_points (int): Number of points to generate
        thickness (float): Thickness of the ring in z-direction
        
    Returns:
        tuple: (x, y, z) arrays of coordinates
    """
    # Generate angular positions
    theta = np.linspace(0, 2*np.pi, n_points)
    
    # Calculate radial positions
    r = np.linspace(inner_radius, outer_radius, int(n_points/10))
    
    # Create a meshgrid for combinations
    theta_grid, r_grid = np.meshgrid(theta, r)
    
    # Convert to cartesian coordinates
    x = r_grid.flatten() * np.cos(theta_grid.flatten())
    y = r_grid.flatten() * np.sin(theta_grid.flatten())
    
    # Add some thickness in z-direction if specified
    if thickness > 0:
        z = np.random.uniform(-thickness/2, thickness/2, size=x.shape)
    else:
        z = np.zeros_like(x)
    
    return x, y, z

# Saturn Shell Creation Functions

saturn_core_info = (
            "2.4 MB PER FRAME FOR HTML.\n\n"
            "Saturn likely has a dense core composed of metallic elements like iron and nickel, surrounded by rocky material and \n" 
            "other compounds solidified by immense pressure and heat. This core is estimated to be about 10 to 15 times the mass \n" 
            "of Earth. It's smaller relative to the planet's overall size compared to Jupiter's core."
)

def create_saturn_core_shell(center_position=(0, 0, 0)):
    """Creates saturn's core shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 0.6,  # Approximately 10% of saturn's radius
        'color': 'rgb(240, 240, 255)',  # estimated black body color at about 11,000 K
        'opacity': 1.0,
        'name': 'Core',
        'description': (
            "Saturn likely has a dense core composed of metallic elements like iron and nickel, surrounded by rocky material and <br>" 
            "other compounds solidified by immense pressure and heat. This core is estimated to be about 10 to 15 times the mass <br>" 
            "of Earth. It's smaller relative to the planet's overall size compared to Jupiter's core.<br><br>" 
            "The core's size and the planet's overall radius are not precisely defined and are subject to ongoing research and <br>" 
            "modeling. However, based on current scientific understanding and models of Saturn's interior, we can provide an <br>" 
            "estimated range.<br>" 
            "* Saturn's Mean Radius is approximately 58,232 kilometers. This is often used as the reference radius.<br>" 
            "* Core Radius Estimates: Scientific studies suggest that Saturn's core is not sharply defined and likely consists of a <br>" 
            "  dense, sloshy mix of ice, rock, and metallic hydrogen that gradually transitions into the overlying layers. One recent <br>" 
            "  study, analyzing waves in Saturn's rings, indicated that the fuzzy core extends out to about 60% of Saturn's radius. <br>" 
            "* This core mass would contain about 17 Earth masses of rock and ice, but mixed with hydrogen and helium, the total mass <br>" 
            "  of this region is about 55 Earth masses. Earlier estimates often suggested a more compact core, but the \"fuzzy core\" <br>" 
            "  model, where the core material is more dispersed into the inner envelope, is gaining acceptance.<br>" 
            "It's important to note that 60% is an estimate based on current models and interpretations of data. The precise nature and <br>" 
            "extent of Saturn's core remain areas of active research.<br>" 
            "* Approximate Temperature: Estimated to be around 12,000 K. Some sources suggest even higher temperatures.<br>" 
            "* Approximate Color: At these extreme temperatures, if we could observe it directly, it would likely appear white-hot to <br>" 
            "  bluish-white, based on black body radiation principles. Given the extreme white-hot to bluish-white temperature, <br>" 
            "  slightly blue-tinted white.<br>" 
            "  * RGB: (255, 255, 255) (pure white) or perhaps something very slightly blue like (240, 240, 255)."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * SATURN_RADIUS_AU
    
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
            name=f"Saturn: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Saturn: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

saturn_metallic_hydrogen_info = (
            "2.1 MB PER FRAME FOR HTML.\n\n"
            "Surrounding the core is a thick layer of liquid metallic hydrogen, similar to Jupiter. Above this is a layer of liquid \n" 
            "hydrogen and helium, which gradually transitions to a gaseous atmosphere with increasing altitude. Due to lower pressure \n" 
            "and a smaller metallic hydrogen zone, Saturn's magnetic field is weaker than Jupiter's."
)

def create_saturn_metallic_hydrogen_shell(center_position=(0, 0, 0)):
    """Creates Saturn's liquid metallic hydrogen shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 0.9,  # Up to about 90% of Saturn's radius
        'color': 'rgb(225, 225, 220)',  # estimated black body color at about 6,000 K
        'opacity': 0.9,
        'name': 'Metallic Hydrogen Layer',
        'description': (
            "Metallic Hydrogen Layer:<br>" 
            "Surrounding the core is a thick layer of liquid metallic hydrogen, similar to Jupiter. Above this is a layer of liquid <br>" 
            "hydrogen and helium, which gradually transitions to a gaseous atmosphere with increasing altitude. Due to lower pressure <br>" 
            "and a smaller metallic hydrogen zone, Saturn's magnetic field is weaker than Jupiter's.<br>" 
            "The transition to metallic hydrogen is thought to begin around 0.4 - 0.5 R and extends outwards to about 0.9 R.<br>" 
            "* Approximate Temperature: Temperatures in this layer would range from thousands of degrees Kelvin, increasing with depth. <br>" 
            "  Estimates around the transition to metallic hydrogen are around ~6,000 K and increase significantly deeper.<br>" 
            "* Approximate Color: Similar to the core, if visible, it would likely glow with a yellowish-white to white color due to its <br>" 
            "  high temperature.<br>" 
            "* RGB: (255, 255, 220) (a slightly yellowish white, like cream) to (255, 255, 255) (pure white), depending on how deep <br>" 
            "  within the layer you're representing."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * SATURN_RADIUS_AU
    
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
            name=f"Saturn: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Saturn: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

saturn_molecular_hydrogen_info = (
            "2.5 MB PER FRAME FOR HTML.\n\n"
            "Liquid Molecular Hydrogen Layer: Approximately 0.8 - 0.9 R to around 1.0 R, at the level where the atmosphere is \n" 
            "considered mostly gaseous. This layer lies above the metallic hydrogen and gradually transitions into the gaseous \n" 
            "atmosphere. The 1.0 R here is a nominal boundary often taken at the cloud tops, which are a distinct layer."
)

def create_saturn_molecular_hydrogen_shell(center_position=(0, 0, 0)):
    """Creates Saturn's molecular hydrogen shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 0.99,  # Up to about 99+% of Saturn's radius
        'color': 'rgb(220, 230, 240)',   
        'opacity': 0.5,
        'name': 'Molecular Hydrogen Layer',
        'description': (
            "Molecular Hydrogen Layer:<br>" 
            "Liquid Molecular Hydrogen Layer: Approximately 0.8 - 0.9 R to around 1.0 R, at the level where the atmosphere is <br>" 
            "considered mostly gaseous. This layer lies above the metallic hydrogen and gradually transitions into the gaseous <br>" 
            "atmosphere. The 1.0 R here is a nominal boundary often taken at the cloud tops, which are a distinct layer.<br>" 
            "* Approximate Temperature: The temperature decreases as you move outwards in this layer, ranging from thousands of <br>" 
            "  degrees Kelvin at the boundary with the metallic hydrogen layer to around -130 °C at the upper boundary near the <br>" 
            "  atmosphere.<br>" 
            "* Approximate Color: This layer is primarily composed of hydrogen, which is transparent. We wouldn't see a black body <br>" 
            "  color associated with its temperature in the visible spectrum at these lower ranges.<br>" 
            "* RGB (for visual representation only): (240, 240, 240) (light grey) or (220, 230, 240) (very light blue-grey)."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * SATURN_RADIUS_AU
    
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
            name=f"Saturn: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Saturn: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

saturn_cloud_layer_info = (
            "USE MANUAL SCALED OF 0.005 AU TO VIEW CLOSELY."
            "4.6 MB PER FRAME FOR HTML.\n\n"
            "Saturn's atmosphere is primarily hydrogen (about 75%) and helium (about 25%), with trace amounts of methane, ammonia, \n" 
            "and water ice. Like Jupiter, it exhibits banded structures due to strong east-west winds, but these bands are much \n" 
            "fainter and less distinct due to a hazy upper atmosphere. Saturn is one of the windiest places in the Solar System, \n" 
            "with equatorial wind speeds reaching up to 1,800 kilometers per hour. A unique feature is a long-lasting hexagonal \n" 
            "jet stream at its north pole. Cloud layers exist at different depths, composed of ammonia ice (uppermost), ammonium \n" 
            "hydrosulfide, and water ice (lowest)."
)

def create_saturn_cloud_layer_shell(center_position=(0, 0, 0)):
    """Creates Saturn's cloud layer shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 1.0,  # The visible "surface" - 100% of Saturn's radius
        'color': 'rgb(210, 180, 140)',  # optical
        'opacity': 1.0,
        'name': 'Cloud Layer',
        'description': (
            "Saturn Cloud Layer<br>" 
            "(Note: toggle off the cloud layer in the legend to better see the interior structure.)<br><br>"
            "Saturn's atmosphere is primarily hydrogen (about 75%) and helium (about 25%), with trace amounts of methane, ammonia, <br>" 
            "and water ice. Like Jupiter, it exhibits banded structures due to strong east-west winds, but these bands are much <br>" 
            "fainter and less distinct due to a hazy upper atmosphere. Saturn is one of the windiest places in the Solar System, <br>" 
            "with equatorial wind speeds reaching up to 1,800 kilometers per hour. A unique feature is a long-lasting hexagonal <br>" 
            "jet stream at its north pole. Cloud layers exist at different depths, composed of ammonia ice (uppermost), ammonium <br>" 
            "hydrosulfide, and water ice (lowest).<br>" 
            "* Atmosphere: The outermost layer, which transitions from a gaseous to a liquid state with increasing depth, starts <br>" 
            "  at the visible clouds and extends inwards.<br>" 
            "* Liquid Molecular Hydrogen transitioning to gaseous hydrogen in the atmosphere. There isn't a solid surface or a <br>" 
            "  distinct \"cloud layer atmosphere\" that we would definitively consider the surface of Saturn in the same way we <br>" 
            "  think of the surface of a rocky planet like Earth.<br>" 
            "* Gradual Transition: Saturn's atmosphere transitions gradually from a gaseous state in the upper layers to a denser, <br>" 
            "  liquid state deeper within the planet. There's no sharp boundary or interface where you'd suddenly go from atmosphere <br>" 
            "  to a solid or liquid \"surface.\"<br>" 
            "* Increasing Pressure and Density: As you descend into Saturn's atmosphere, the pressure and density increase dramatically. <br>" 
            "  The gases become compressed until they behave more like a fluid. Eventually, the pressure becomes so immense that <br>" 
            "  hydrogen transitions into a liquid metallic state.<br>" 
            "* No Solid Ground: Unlike Earth or Mars, Saturn doesn't have a rocky or icy crust. If you were to descend into Saturn, you <br>" 
            "  would never reach a solid surface to stand on. You would simply experience increasingly extreme temperatures and <br>" 
            "  pressures. What we often refer to as the \"visible surface\" of Saturn are the uppermost cloud layers. These are the layers <br>" 
            "  that reflect sunlight and are what we see through telescopes.<br>" 
            "* Vertical Structure: Similar to Jupiter, Saturn's upper troposphere contains three main cloud layers, composed of <br>" 
            "  different chemicals at varying depths:<br>" 
            "  * Ammonia ice clouds: These are the highest and coldest clouds.<br>" 
            "  * Ammonium hydrosulfide clouds: Below the ammonia clouds.<br>" 
            "  * Water ice clouds: Thought to be the deepest layer of clouds.<br>" 
            "* Thickness: Estimates suggest the total thickness of these three cloud layers on Saturn could be around 200 kilometers, <br>" 
            "  * Haze Layer: Above the ammonia ice clouds, Saturn has a more prominent haze layer formed by photochemical reactions in <br>" 
            "    its upper atmosphere. This haze layer further obscures the deeper, potentially more colorful, cloud layers.<br>" 
            "  * Visibility: Because Saturn's clouds are thicker and overlaid by a more substantial haze, we rarely get clear views of <br>" 
            "    the deeper cloud layers with their distinct colors, as we do on Jupiter. This is why Saturn appears more uniformly <br>" 
            "    pale yellow or butterscotch in color. The contrast between the bands and zones is much less pronounced on Saturn. So, <br>" 
            "    while Saturn does have distinct cloud layers with different chemical compositions, they are not as sharply defined or <br>" 
            "    visually apparent as Jupiter's due to their greater thickness and the overlying haze. Therefore, while you could <br>" 
            "    consider this region of clouds as a distinct layer within Saturn's atmosphere, its characteristics (thickness, visibility) <br>" 
            "    differ noticeably from Jupiter's more vibrant and thinner cloud bands.<br>" 
            "  * To put a rough estimate on the thickness relative to Saturn's radius, a 200 km thick cloud layer would be approximately <br>" 
            "    ≈0.0034R.<br>"
            "  * Visualization: It is the primary visual feature we observe and therefore should be represented as a distinct layer.<br>"
            "    * Visual Boundary: The cloud tops are effectively the limit of what we can directly see with telescopes (in visible <br>" 
            "      light). While the atmosphere extends far above and the molecular hydrogen layer lies deep below, the cloud layer is <br>" 
            "      the \"face\" Saturn presents to us.<br>" 
            "    * Saturn's cloud layer exhibits dynamic features like bands, storms (including the polar hexagon), and variations in <br>" 
            "      haze. These are important aspects of Saturn's atmospheric activity. The cloud layer marks a visually and physically <br>" 
            "      significant region within that transition.<br>" 
            "* Approximate Temperature: Varies with altitude within the cloud layers:<br>" 
            "  * Ammonia ice clouds (highest): Around -173 °C (-280 °F).<br>" 
            "  * Ammonium hydrosulfide clouds: Warmer than the ammonia clouds.<br>" 
            "  * Water ice clouds (deepest): Ranging from -88 °C (-127 °F) to -3 °C (26 °F).<br>"
            "* Approximate Color: The overall visible color of Saturn's clouds is a pale yellow to butterscotch. This color is <br>" 
            "  thought to be due to photochemical haze in the upper atmosphere interacting with sunlight, potentially involving <br>" 
            "  hydrocarbons. Trace amounts of other elements might contribute subtle hues.<br>"
            "In summary, while the cloud layers are a prominent and visible feature of Saturn, they are not a surface. Saturn is a fluid <br>" 
            "planet that becomes increasingly dense with depth, without a distinct solid or liquid surface."       
            )
    }
    
    # Calculate radius in AU
    radius = layer_info['radius_fraction'] * SATURN_RADIUS_AU
    
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
        name=f"Saturn: {layer_info['name']}",
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
    layer_name = f"Saturn: {layer_info['name']}"
    minimal_hover_texts = [layer_name] * len(x_hover)

    # Create hover trace with direct text assignment
    hover_trace = go.Scatter3d(
        x=x_hover, 
        y=y_hover, 
        z=z_hover,
        mode='markers',
        marker=dict(
            size=2,  # originally 5
            color='rgb(210, 180, 140)',  # Layer color, originally 'white'
            opacity=1.0,  # originally 0.8
            line=dict(  # Add a contrasting outline
                width=1,
                color='black'
            )
        ),
        name=f"Saturn: {layer_info['name']} (Info)",
        text=hover_texts,  # IMPORTANT: Matching length with coordinate arrays
        customdata=minimal_hover_texts,  # For "Object Names Only" mode
        hovertemplate='%{text}<extra></extra>',  # Use the standard hover template
        showlegend=False  # Don't show in legend since it's just for hover
    )

    return [surface_trace, hover_trace]

saturn_upper_atmosphere_info = (
            "2.7 MB PER FRAME FOR HTML.\n\n"
            "While the colorful cloud bands are the most visually prominent feature of Saturn, there's a significant and complex \n" 
            "structure of gases extending far above them, each layer with its own characteristics and processes. The Cassini mission \n" 
            "provided a wealth of information about these upper atmospheric layers."
)

# Fix for create_saturn_upper_atmosphere_shell function - Implementation missing
def create_saturn_upper_atmosphere_shell(center_position=(0, 0, 0)):
    """Creates Saturn's upper atmosphere shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 1.1,  # Extends about 10% beyond the visible radius
        'color': 'rgb(240, 245, 250)',  # optical pale blue
        'opacity': 0.5,
        'name': 'Upper Atmosphere',
        'description': (
            "Saturn definitely has an upper atmosphere above its cloud layers. Similar to Earth, Jupiter, and other planets with <br>" 
            "atmospheres, Saturn's atmosphere doesn't just abruptly end at the visible clouds. It extends far beyond.<br>" 
            "Here's a breakdown of the regions above the main cloud layer in Saturn's atmosphere:<br>" 
            "* Troposphere: This is the lowest layer, where the visible clouds reside and where most of the planet's weather occurs. <br>" 
            "  The temperature generally decreases with altitude in this layer.<br>" 
            "* Tropopause: This is a transition layer above the troposphere where the temperature stops decreasing and starts to become <br>" 
            "  stable. It marks the upper boundary of the troposphere.<br>" 
            "* Stratosphere: Above the tropopause, the temperature generally increases with altitude as this layer absorbs ultraviolet (UV) <br>" 
            "  radiation from the Sun. In Saturn's stratosphere, hydrocarbons like methane, ethane, and acetylene are formed through <br>" 
            "  photochemical reactions driven by sunlight.<br>" 
            "* Mesosphere: Above the stratosphere, the temperature generally decreases with altitude again. This layer is less well-studied <br>" 
            "  in Saturn compared to its lower atmosphere.<br>" 
            "* Thermosphere: In this upper layer, the atmosphere becomes very thin, and the temperature increases significantly with altitude <br>" 
            "  due to absorption of high-energy solar radiation. Saturn's thermosphere is heated by auroral electric currents, similar to <br>" 
            "  how Earth's thermosphere is heated.<br>" 
            "* Exosphere: This is the outermost and most tenuous layer of Saturn's atmosphere, where the gas molecules are so far apart that <br>" 
            "  they can escape into space. There is no clear upper boundary to the exosphere. It extends far beyond the denser parts <br>" 
            "  of the upper atmosphere<br>" 
            "So, while the colorful cloud bands are the most visually prominent feature of Saturn, there's a significant and complex <br>" 
            "structure of gases extending far above them, each layer with its own characteristics and processes. The Cassini mission <br>" 
            "provided a wealth of information about these upper atmospheric layers. These layers are all part of the gaseous <br>" 
            "atmosphere above the cloud layers. They are characterized by different temperature profiles and chemical compositions <br>" 
            "as altitude increases. Their exact outer boundaries are not defined by a specific fraction of Saturn's radius in a simple <br>" 
            "way, as they gradually thin out.<br>" 
            "* Gradual Transitions: The boundaries between these layers are not sharp lines but rather zones of transition where the <br>" 
            "  physical properties of the material change.<br>" 
            "* Atmospheric Extent: The atmosphere doesn't have a clear \"top\" in terms of a specific radial fraction in the same way <br>" 
            "  the internal layers do. It thins out gradually into space.<br>" 
            "* Modeling: These fractions are based on current scientific models, which are continually being refined. The atmosphere <br>" 
            "  extends outwards from what we typically consider the \"surface\" at 1 R (the cloud tops).<br>" 
            "* Approximate Temperature: The temperature generally decreases with altitude in the troposphere (below the tropopause). <br>" 
            "  Above the tropopause, in the stratosphere, it increases due to absorption of UV radiation. The thermosphere, the upper <br>" 
            "  part of the atmosphere, becomes surprisingly hot, reaching hundreds of degrees Celsius (e.g., 300 °C near the poles) <br>" 
            "  due to auroral heating.<br>" 
            "* Approximate Color: The upper atmosphere is primarily composed of hydrogen and helium, which are transparent. We don't <br>" 
            "  associate a specific visible \"color\" with these gases at these temperatures. Auroras in the polar regions would emit <br>" 
            "  light, similar to Earth's auroras, with colors depending on the excited gases (e.g., greens and reds from oxygen, blues <br>" 
            "  from nitrogen).<br>" 
            "* Exosphere: Temperatures in the exosphere are very high, reaching hundreds to thousands of degrees Kelvin. However, <br>" 
            "  the gas density is extremely low, so this heat wouldn't feel like anything to a spacecraft. The exosphere is extremely <br>" 
            "  tenuous and doesn't have a visible color in the same way as the denser layers or hot objects. Individual atoms and <br>" 
            "  molecules might emit light at specific wavelengths if excited, but the overall appearance is essentially transparent.<br>" 
            "* Defining a precise upper boundary for the \"upper atmosphere\" is challenging because it gradually thins out. The main <br>" 
            "  cloud layers extend up to a few hundred kilometers above the 1-bar pressure level (which is often considered the \"top\" <br>" 
            "  of the troposphere and roughly 1 R. Sources suggest the cloud layers are spread over about 300 km in altitude. The <br>" 
            "  stratosphere and mesosphere extend further outwards, but their density decreases significantly with altitude. The <br>" 
            "  thermosphere, where temperatures rise again due to solar radiation and auroral activity, is even more tenuous. <br>" 
            "  Considering these factors, a rough estimate for the outermost extent before it significantly transitions into the exosphere <br>" 
            "  could be a few thousand kilometers above the 1-bar level. ≈0.086R. The edge around 1.05 to 1.1 R. However, the atmosphere <br>" 
            "  continues to thin out gradually beyond this.<br>" 
            "* Exosphere Extent: The exosphere of Saturn, like other planets, is primarily influenced by Saturn's gravitational pull. <br>" 
            "  While it's the outermost layer of the atmosphere, its density decreases exponentially with distance." 
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * SATURN_RADIUS_AU
    
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
            name=f"Saturn: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Saturn: {layer_info['name']}"] * len(x),
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

def create_saturn_magnetosphere(center_position=(0, 0, 0)):
    """Creates Saturn's main magnetosphere structure."""
    # Parameters for magnetosphere components (in Saturn radii)
    params = {
        # Compressed sunward side
        'sunward_distance': 22,  # Compressed toward the sun, ranges from 20-25 Rs
        
        # Equatorial extension (wider than polar)
        'equatorial_radius': 45,   # ranges from 40-50 Rs
        'polar_radius': 35,         # ranges from 30-40 Rs
        
        # Magnetotail parameters
        'tail_length': 500,  # Length of visible magnetotail, ranges from 400-600 Rs
        'tail_base_radius': 75,  # Radius at the base of the tail, ranges from 50-100 Rs
        'tail_end_radius': 100,  # Radius at the end of the tail, ranges from 75-125 Rs
    }
    
    # Scale everything by Saturn's radius in AU
    for key in params:
        params[key] *= SATURN_RADIUS_AU
    
    # Create magnetosphere main shape
    x, y, z = create_magnetosphere_shape(params)
    
    # Unpack center position
    center_x, center_y, center_z = center_position
    
    # Apply center position offset
    x = np.array(x) + center_x
    y = np.array(y) + center_y
    z = np.array(z) + center_z
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=2.0,
                color='rgb(200, 200, 255)', # Light blue for magnetic field
                opacity=0.25
            ),
            name='Saturn: Magnetosphere',
            text=["Saturn has a large magnetosphere, the region of space dominated by its magnetic field. Saturn's magnetic field is <br>" 
                  "unique because its magnetic axis is almost perfectly aligned with its rotational axis. The magnetosphere deflects <br>" 
                  "the solar wind and traps charged particles, leading to auroras at the poles.<br>" 
                  "Material from Enceladus's plumes contributes plasma to Saturn's magnetosphere and its E ring.<br>" 
                  "The Bow Shock points towards the Sun along the X-axis. The XY plane is the ecliptic."] * len(x),
            customdata=['Saturn: Magnetosphere'] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    sun_traces = create_sun_direction_indicator(
        center_position=center_position, 
        shell_radius=500 * SATURN_RADIUS_AU
    )
    for trace in sun_traces:
        traces.append(trace)

    return traces

saturn_enceladus_plasma_torus_info = ("634 KB PER FRAME FOR HTML.\n\n"
              "Donut-shaped region of charged particles from saturn's moon Io")

def create_saturn_enceladus_plasma_torus(center_position=(0, 0, 0)):
    """Creates Saturn's Enceladus plasma torus."""
    # Parameters
    enceladus_torus_distance = 3.95 * SATURN_RADIUS_AU  
    enceladus_torus_thickness = 1 * SATURN_RADIUS_AU
    enceladus_torus_width = 2 * SATURN_RADIUS_AU
    
    # Unpack center position
    center_x, center_y, center_z = center_position

    # Saturn's axial tilt in radians (-26.73 degrees)
    saturn_tilt = np.radians(-26.73)
    
    # Create the Io plasma torus points
    enceladus_torus_x = []
    enceladus_torus_y = []
    enceladus_torus_z = []
    
    n_points = 100
    n_rings = 8
    
    for i_ring in range(n_rings):
        # Vary the radius slightly to create thickness
        radius_offset = (i_ring / (n_rings-1) - 0.5) * enceladus_torus_thickness
        torus_radius = enceladus_torus_distance + radius_offset
        
        for i in range(n_points):
            angle = (i / n_points) * 2 * np.pi

            # Position in x-y plane (equatorial)
            x = torus_radius * np.cos(angle)
            y = torus_radius * np.sin(angle)
            z = 0  # In the equatorial plane    
            
            # Add some thickness variation
            jitter = (np.random.random() - 0.5) * enceladus_torus_width
            
            enceladus_torus_x.append(x)
            enceladus_torus_y.append(y)
            enceladus_torus_z.append(z + jitter)     # Apply jitter to z axis
    
    # Apply center position offset
    enceladus_torus_x = np.array(enceladus_torus_x) 
    enceladus_torus_y = np.array(enceladus_torus_y) 
    enceladus_torus_z = np.array(enceladus_torus_z) 

    # Apply Saturn's axial tilt (rotate around x-axis)
    enceladus_torus_x_tilted, enceladus_torus_y_tilted, enceladus_torus_z_tilted = rotate_points(
        enceladus_torus_x, enceladus_torus_y, enceladus_torus_z, saturn_tilt, 'x'
    )

    # Apply center position offset
    enceladus_torus_x_final = enceladus_torus_x_tilted + center_x
    enceladus_torus_y_final = enceladus_torus_y_tilted + center_y
    enceladus_torus_z_final = enceladus_torus_z_tilted + center_z

    # Create the enceladus plasma torus hover text and customdata arrays
    enceladus_text = ["Enceladus plasma torus: Primarily sourced by water vapor and icy particles vented from the geysers on the <br>" 
                      "south pole of Enceladus. These geysers release hundreds of kilograms of water vapor per second.<br>" 
                      "* Composition: Dominated by water group ions and also contains hydrogen ions.<br>" 
                      "* Location: Forms a torus centered around Enceladus's orbit, which is within Saturn's vast E ring. The E ring <br>" 
                      "  itself is largely composed of icy particles ejected from Enceladus.<br>" 
                      "* Influence: The Enceladus plasma torus is a significant source of plasma for Saturn's inner magnetosphere. <br>" 
                      "  This plasma is crucial for populating Saturn's magnetosphere with water-group ions. The mass loading from <br>" 
                      "  Enceladus is estimated to be around 100 kg/s. This plasma gradually moves outward and eventually escapes <br>" 
                      "  through Saturn's magnetotail.<br>" 
                      "* Ionization: Ionization of the water vapor is driven by UV radiation and electron bombardment within the torus.<br>"
                      "* Color: Neutral gases like water vapor are colorless and transparent. Any visible color would arise from the scattering of <br>" 
                      "  light by the ice particles within the torus. Pure water ice is typically white or very light blue due to scattering."
                      ] * len(enceladus_torus_x_final)
    enceladus_customdata = ['Saturn: Enceladus Plasma Torus'] * len(enceladus_torus_x_final)
    
    
    traces = [
        go.Scatter3d(
            x=enceladus_torus_x_final,
            y=enceladus_torus_y_final,
            z=enceladus_torus_z_final,
            mode='markers',
            marker=dict(
                size=1.5,
                color='rgb(200, 220, 255)',  # a very subtle blue tint for plasma torus
                opacity=0.3
            ),
            name='Saturn: Enceladus Plasma Torus',
            text=enceladus_text,
            customdata=enceladus_customdata,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    sun_traces = create_sun_direction_indicator(
        center_position=center_position, 
        shell_radius=enceladus_torus_distance
    )
    for trace in sun_traces:
        traces.append(trace)

    return traces

saturn_radiation_belts_info = (
            "560 KB PER FRAME FOR HTML.\n\n"
            "Zones of trapped high-energy particles in Saturn's magnetosphere"                     
)

def create_saturn_radiation_belts(center_position=(0, 0, 0)):
    """Creates Saturn's radiation belts."""
    belt_colors = ['rgb(255, 255, 100)', 'rgb(100, 255, 150)', 'rgb(100, 200, 255)',
                  'rgb(255, 100, 100)', 'rgb(100, 100, 255)', 'rgb(255, 200, 100)']
    belt_names = ['Belt from A-Ring to Mimas', 'Belt from Mimas to Enceladus', 'Belt from Enceladus to Tethys', 
                  'Belt from Tethys to Dione', 'Belt from Dione to Rhea', 'Belt outward of Rhea']
    belt_texts = [
        "Belt from A-Ring to Mimas: Saturn radiation belts, regions where charged particles are trapped by the planet's magnetic <br>" 
        "field. They are heavily influenced by Saturn's rings and moons, which absorb many of the charged particles, creating gaps <br>" 
        "in the belts. The primary source of high-energy particles is the collision of galactic cosmic rays.",

        "Belt from Mimas to Enceladus: Saturn radiation belts, regions where charged particles are trapped by the planet's magnetic <br>" 
        "field. They are heavily influenced by Saturn's rings and moons, which absorb many of the charged particles, creating gaps <br>" 
        "in the belts. The primary source of high-energy particles is the collision of galactic cosmic rays.",

        "Belt from Enceladus to Tethys: Saturn radiation belts, regions where charged particles are trapped by the planet's magnetic <br>" 
        "field. They are heavily influenced by Saturn's rings and moons, which absorb many of the charged particles, creating gaps <br>" 
        "in the belts. The primary source of high-energy particles is the collision of galactic cosmic rays.",

        "Belt from Tethys to Dione: Saturn radiation belts, regions where charged particles are trapped by the planet's magnetic <br>" 
        "field. They are heavily influenced by Saturn's rings and moons, which absorb many of the charged particles, creating gaps <br>" 
        "in the belts. The primary source of high-energy particles is the collision of galactic cosmic rays.",

        "Belt from Dione to Rhea: Saturn radiation belts, regions where charged particles are trapped by the planet's magnetic <br>" 
        "field. They are heavily influenced by Saturn's rings and moons, which absorb many of the charged particles, creating gaps <br>" 
        "in the belts. The primary source of high-energy particles is the collision of galactic cosmic rays. Rhea's influence on <br>" 
        "sharply defining a gap might be less pronounced than the inner moons.",

        "Belt outward of Rhea: Saturn radiation belts, regions where charged particles are trapped by the planet's magnetic <br>" 
        "field. They are heavily influenced by Saturn's rings and moons, which absorb many of the charged particles, creating gaps <br>" 
        "in the belts. The primary source of high-energy particles is the collision of galactic cosmic rays. The radiation <br>" 
        "environment beyond Rhea becomes more variable and less clearly defined into stable, distinct belts solely by moon orbits."
    ]
    
    # Belt distances in Saturn radii
    belt_distances = [2.7, 3.5, 4.4, 5.6, 7.4, 9.0]
    belt_thickness = 0.5 * SATURN_RADIUS_AU
    
    # Scale distances by Saturn's radius in AU
    belt_distances = [d * SATURN_RADIUS_AU for d in belt_distances]
    
    # Unpack center position
    center_x, center_y, center_z = center_position

    # Saturn's axial tilt in radians (-26.73 degrees)
    saturn_tilt = np.radians(-26.73)
    
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
                
                # Create a belt around Saturn's rotational axis
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
        belt_text = [belt_texts[i]] * len(belt_x)
        belt_customdata = [belt_names[i]] * len(belt_x)

        # Apply center position offset
        belt_x = np.array(belt_x)
        belt_y = np.array(belt_y)
        belt_z = np.array(belt_z)
        
        # Apply Saturn's axial tilt (rotate around x-axis)
        belt_x_tilted, belt_y_tilted, belt_z_tilted = rotate_points(belt_x, belt_y, belt_z, saturn_tilt, 'x')
        
        # Apply center position offset
        belt_x_final = belt_x_tilted + center_x
        belt_y_final = belt_y_tilted + center_y
        belt_z_final = belt_z_tilted + center_z

        traces.append(
            go.Scatter3d(
                x=belt_x_final,
                y=belt_y_final,
                z=belt_z_final,
                mode='markers',
                marker=dict(
                    size=1.5,
                    color=belt_colors[i],
                    opacity=0.3
                ),
                name=belt_names[i],
                text=belt_text,
                customdata=belt_customdata,
                hovertemplate='%{text}<extra></extra>',
                showlegend=True
            )
        )
    
    sun_traces = create_sun_direction_indicator(
        center_position=center_position, 
        shell_radius= 9.0 * SATURN_RADIUS_AU
    )
    for trace in sun_traces:
        traces.append(trace)

    return traces
    
saturn_hill_sphere_info = (
            "SELECT MANUAL SCALE OF AT LEAST 0.6 AU TO VISUALIZE.\n" 
            "1.3 MB PER FRAME FOR HTML.\n\n"

            "Saturn: Its Hill sphere, the region around the planet where its gravity dominates over the Sun's, has a radius of \n" 
            "approximately 91 million kilometers (about 151 Saturn radii). This is smaller than Jupiter's Hill sphere due to \n" 
            "Saturn's lower mass. The Hill sphere is crucial for determining the maximum distance at which a moon can stably orbit \n" 
            "Saturn."                     
)

def create_saturn_hill_sphere_shell(center_position=(0, 0, 0)):
    """Creates Saturn's Hill sphere shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 1120,  
        'color': 'rgb(0, 255, 0)',  # Green for Hill sphere
        'opacity': 0.3,
        'name': 'Hill Sphere',
        'description': (
            "SET MANUAL SCALE OF AT LEAST 0.3 AU TO VISUALIZE.<br><br>"
            "Saturn: Its Hill sphere, the region around the planet where its gravity dominates over the Sun's, has a radius of <br>" 
            "approximately 91 million kilometers (about 151 Saturn radii). This is smaller than Jupiter's Hill sphere due to <br>" 
            "Saturn's lower mass. The Hill sphere is crucial for determining the maximum distance at which a moon can stably orbit <br>" 
            "Saturn.<br><br>"
                "The Hill sphere is the region around a where its own gravity is the dominant force in attracting satellites. For <br>" 
                "a planet orbiting a star, it's the region where the planet's gravity is stronger than the star's tidal forces.<br><br>" 
                "The Hill Sphere radius can be described in words as follows: it is equal to the planet's average distance from the <br>" 
                "Sun (its orbital semi-major axis) multiplied by the cube root of the ratio between the planet's mass and three times <br>" 
                "the Sun's mass. In other words, you take how far the planet orbits out from the Sun, then scale that distance by the <br>" 
                "cube root of (planet mass ÷ [3 x solar mass]) to find the boundary within which the planet's gravity dominates over the Sun's."        
        )
    }
        
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * SATURN_RADIUS_AU
    
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
            name=f"Saturn: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Saturn: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    # Add sun direction indicator scaled to this shell's radius
    sun_traces = create_sun_direction_indicator(
        center_position=center_position, 
        shell_radius=layer_radius
    )
    for trace in sun_traces:
        traces.append(trace)

    return traces

saturn_ring_system_info = (
                "22.2 MB PER FRAME FOR HTML.\n\n"

                "The main ring is reddish and composed of dust ejected from Saturn's small inner moons,\n"
                "Metis and Adrastea, due to high-speed impacts by micrometeoroids.\n\n"

                "The Halo Ring is a faint, thick torus of material.\n"
                "The ring likely consists of fine dust particles pushed out of the main ring\n"
                "by electromagnetic forces from Saturn's powerful magnetosphere.\n\n" 

                "The Amalthea Gossamer Ring is an extremely faint and wide ring.\n"
                "It is composed of dust particles ejected from Amalthea by micrometeoroid impacts.\n\n"   

                "The Thebe Gossamer Ring is another very faint and wide ring.\n"
                "It is composed of dust particles ejected from Thebe by micrometeoroid impacts."                                           
)

def create_saturn_ring_system(center_position=(0, 0, 0)):
    """
    Creates a visualization of Saturn's ring system.
    
    Parameters:
        center_position (tuple): (x, y, z) position of Saturn's center
        
    Returns:
        list: A list of plotly traces representing the ring components
    """
    traces = []
    
    # Define Saturn's ring parameters in kilometers from Saturn's center
    # Then convert to Saturn radii, and finally to AU
    ring_params = {
        'd_ring': {
            'inner_radius_km': 66900,  # Inner edge (in km from Saturn's center)
            'outer_radius_km': 74500,  # Outer edge (in km from Saturn's center)
            'thickness_km': 10,         # Approximate thickness
            'color': 'rgb(50, 50, 50)',  # Very dark/grayish
            'opacity': 0.4,
            'name': 'D Ring',
            'description': (
                "D Ring: The innermost and faintest of the main rings.<br><br>" 
                "Saturn is famous for its spectacular and extensive ring system, composed primarily of water ice particles, with <br>" 
                "some rocky debris and dust. The rings are incredibly wide, extending hundreds of thousands of kilometers from the <br>" 
                "planet, but are typically only about 10 meters thick. They are divided into several main rings (A, B, C) and <br>" 
                "fainter rings (D, E, F, G), with gaps between them, most notably the Cassini Division."
            )
        },
        'c_ring': {
            'inner_radius_km': 74658,  # Inner edge (in km from Saturn's center)
            'outer_radius_km': 92000,  # Outer edge (in km from Saturn's center)
            'thickness_km': 10,      # Approximate thickness (thicker than the main ring)
            'color': 'rgb(100, 100, 100)',  # Darker gray
            'opacity': 0.5,
            'name': 'C Ring',
            'description': (
                "C Ring: Wider but fainter than the A and B rings.<br><br>" 
                "Saturn is famous for its spectacular and extensive ring system, composed primarily of water ice particles, with <br>" 
                "some rocky debris and dust. The rings are incredibly wide, extending hundreds of thousands of kilometers from the <br>" 
                "planet, but are typically only about 10 meters thick. They are divided into several main rings (A, B, C) and <br>" 
                "fainter rings (D, E, F, G), with gaps between them, most notably the Cassini Division."
            )
        },
        'b_ring': {
            'inner_radius_km': 92000,  # Inner edge (in km from Saturn's center)
            'outer_radius_km': 117500,  # Outer edge 
            'thickness_km': 10,       # Approximate thickness
            'color': 'rgb(180, 180, 170)',  # Brightest, whitish-gray with subtle tones
            'opacity': 0.8,
            'name': 'B Ring',
            'description': (
                "B Ring: The brightest and most massive ring.<br><br>" 
                "Saturn is famous for its spectacular and extensive ring system, composed primarily of water ice particles, with <br>" 
                "some rocky debris and dust. The rings are incredibly wide, extending hundreds of thousands of kilometers from the <br>" 
                "planet, but are typically only about 10 meters thick. They are divided into several main rings (A, B, C) and <br>" 
                "fainter rings (D, E, F, G), with gaps between them, most notably the Cassini Division."
            )
        },
        'a_ring': {
            'inner_radius_km': 122340,  # Inner edge (in km from Saturn's center)
            'outer_radius_km': 136800,  # Outer edge 
            'thickness_km': 30,       # Approximate thickness
            'color': 'rgb(160, 160, 150)',  # Slightly darker than B, grayish
            'opacity': 0.7,
            'name': 'A Ring',
            'description': (
                "A Ring: The outermost of the bright main rings. Pan orbits within the Encke Gap in the A Ring and is responsible for <br>"
                "keeping it largely clear of ring material. It also creates wavy edges in the gap. Daphnis orbits within the Keeler Gap <br>" 
                "in the outer A Ring and creates waves in the edges of the gap.<br><br>" 
                "Saturn is famous for its spectacular and extensive ring system, composed primarily of water ice particles, with <br>" 
                "some rocky debris and dust. The rings are incredibly wide, extending hundreds of thousands of kilometers from the <br>" 
                "planet, but are typically only about 10 meters thick. They are divided into several main rings (A, B, C) and <br>" 
                "fainter rings (D, E, F, G), with gaps between them, most notably the Cassini Division."
            )
        },
        'f_ring': {
            'inner_radius_km': 140210,  # Inner edge (in km from Saturn's center)
            'outer_radius_km': 140420,  # Outer edge 
            'thickness_km': 1,       # Approximate thickness
            'color': 'rgb(200, 200, 200)',  # Narrow, brightish
            'opacity': 0.3,
            'name': 'F Ring',
            'description': (
              "F Ring: A narrow and dynamic ring just outside the A ring, shepherded by the moons Pandora and Prometheus.<br><br>" 
                "Saturn is famous for its spectacular and extensive ring system, composed primarily of water ice particles, with <br>" 
                "some rocky debris and dust. The rings are incredibly wide, extending hundreds of thousands of kilometers from the <br>" 
                "planet, but are typically only about 10 meters thick. They are divided into several main rings (A, B, C) and <br>" 
                "fainter rings (D, E, F, G), with gaps between them, most notably the Cassini Division."
            )
        },
        'g_ring': {
            'inner_radius_km': 166000,  # Inner edge (in km from Saturn's center)
            'outer_radius_km': 175000,  # Outer edge 
            'thickness_km': 100,       # Approximate thickness
            'color': 'rgb(220, 220, 200)',  # Faint, light gray/dusty
            'opacity': 0.2,
            'name': 'G Ring',
            'description': (
              "G Ring: A faint and dusty ring farther out.<br><br>" 
                "Saturn is famous for its spectacular and extensive ring system, composed primarily of water ice particles, with <br>" 
                "some rocky debris and dust. The rings are incredibly wide, extending hundreds of thousands of kilometers from the <br>" 
                "planet, but are typically only about 10 meters thick. They are divided into several main rings (A, B, C) and <br>" 
                "fainter rings (D, E, F, G), with gaps between them, most notably the Cassini Division."
            )
        },
        'e_ring': {
            'inner_radius_km': 180000,  # Inner edge (in km from Saturn's center)
            'outer_radius_km': 480000,  # Outer edge 
            'thickness_km': 1000,       # Approximate thickness
            'color': 'rgb(230, 230, 250)',  # Very faint, bluish-white due to water ice
            'opacity': 0.1,
            'name': 'E Ring',
            'description': (
              "E Ring: A very wide and diffuse ring, extending far beyond the main rings and sourced by icy particles from the moon Enceladus.<br><br>" 
                "Saturn is famous for its spectacular and extensive ring system, composed primarily of water ice particles, with <br>" 
                "some rocky debris and dust. The rings are incredibly wide, extending hundreds of thousands of kilometers from the <br>" 
                "planet, but are typically only about 10 meters thick. They are divided into several main rings (A, B, C) and <br>" 
                "fainter rings (D, E, F, G), with gaps between them, most notably the Cassini Division."
            )
        }
    }
    
    # Unpack center position
    center_x, center_y, center_z = center_position
    
    # Saturn's axial tilt in radians (-26.73)
    saturn_tilt = np.radians(-26.73)         

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
        x, y, z = create_ring_points_saturn (inner_radius_au, outer_radius_au, n_points, thickness_au)
        
        # Apply Saturn's axial tilt
        # Rotation around the y-axis by saturn_tilt angle
        x_tilted, y_tilted, z_tilted = rotate_points(x, y, z, saturn_tilt, 'x')

        # Apply center position offset
    #    x = np.array(x) + center_x
    #    y = np.array(y) + center_y
    #    z = np.array(z) + center_z

        # Apply center position offset
        x_final = np.array(x_tilted) + center_x
        y_final = np.array(y_tilted) + center_y
        z_final = np.array(z_tilted) + center_z
        
        # Create a text list for hover information
        text_array = [ring_info['description'] for _ in range(len(x))]
        
        # Add ring trace
        traces.append(
            go.Scatter3d(
    #            x=x, y=y, z=z,
                x=x_final,
                y=y_final,
                z=z_final,
                mode='markers',
                marker=dict(
                    size=1.5,  # Small markers for rings
                    color=ring_info['color'],
                    opacity=ring_info['opacity']
                ),
                name=f"Saturn: {ring_info['name']}",
                text=text_array,
                customdata=[f"Saturn: {ring_info['name']}"] * len(x),
                hovertemplate='%{text}<extra></extra>',
                showlegend=True
            )
        )
    
    sun_traces = create_sun_direction_indicator(
        center_position=center_position, 
        shell_radius=480000 / KM_PER_AU
    )
    for trace in sun_traces:
        traces.append(trace)

    return traces

saturn_magnetosphere_info = (
            "SELECT MANUAL SCALE OF AT LEAST 0.2 AU TO VISUALIZE.\n"
            "1.4 MB PER FRAME FOR HTML.\n\n"

            "Saturn has a large magnetosphere, the region of space dominated by its magnetic field. Saturn's magnetic field is \n" 
            "unique because its magnetic axis is almost perfectly aligned with its rotational axis. The magnetosphere deflects \n" 
            "the solar wind and traps charged particles, leading to auroras at the poles. Material from Enceladus's plumes \n" 
            "contributes plasma to Saturn's magnetosphere and its E ring."                      
)
