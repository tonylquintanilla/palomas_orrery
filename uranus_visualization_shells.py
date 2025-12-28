import numpy as np
import math
import plotly.graph_objs as go
from planet_visualization_utilities import (URANUS_RADIUS_AU, KM_PER_AU, create_sphere_points, create_magnetosphere_shape, 
                                            rotate_points)
from saturn_visualization_shells import create_ring_points_saturn
from shared_utilities import create_sun_direction_indicator

# Uranus Shell Creation Functions

uranus_core_info = (
            "2.4 MB PER FRAME FOR HTML.\n\n"
            "Uranus core: Scientists believe Uranus has a relatively small, rocky core. This core is likely composed of silicate and \n" 
            "metallic iron-nickel. It's estimated to have a mass roughly equivalent to that of Earth. Temperatures near the core can \n" 
            "reach incredibly high values, around 4982 degC (5255 K) degrees Celsius."
)

def create_uranus_core_shell(center_position=(0, 0, 0)):
    """Creates Uranus's core shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 0.2,  # Approximately 20% of Uranus's radius
        'color': 'rgb(255, 215, 0)',  # estimated black body color at about 4982 degC (5255 K)
        'opacity': 1.0,
        'name': 'Core',
        'description': (
            "Uranus core: Scientists believe Uranus has a relatively small, rocky core. This core is likely composed of silicate and <br>" 
            "metallic iron-nickel. It's estimated to have a mass roughly equivalent to that of Earth. Temperatures near the core can <br>" 
            "reach incredibly high values, around 4982 degC (5255 K) degrees Celsius."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * URANUS_RADIUS_AU
    
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
            name=f"Uranus: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Uranus: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

uranus_mantle_info = (
            "2.1 MB PER FRAME FOR HTML.\n\n"
            "mantle: Surrounding the rocky core is a dense fluid layer often referred to as an \"icy mantle.\" This layer makes up the \n" 
            "majority (80% or more) of the planet's mass. It's not ice in the traditional sense but rather a hot, dense fluid \n" 
            "containing water, ammonia, and methane under immense pressure. These are sometimes referred to as \"ices\" by planetary \n" 
            "scientists. This mantle is electrically conductive and is thought to be the region where Uranus' unusual magnetic field \n" 
            "is generated."
)

def create_uranus_mantle_shell(center_position=(0, 0, 0)):
    """Creates Uranus's matel shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 0.7,  # Up to about 70% of Uranus's radius
        'color': 'rgb(255, 138, 18)',  # estimated black body color at about 2,000 K
        'opacity': 0.9,
        'name': 'mantle',
        'description': (
            "mantle: Surrounding the rocky core is a dense fluid layer often referred to as an \"icy mantle.\" This layer makes up the <br>" 
            "majority (80% or more) of the planet's mass. It's not ice in the traditional sense but rather a hot, dense fluid <br>" 
            "containing water, ammonia, and methane under immense pressure. These are sometimes referred to as \"ices\" by planetary <br>" 
            "scientists. This mantle is electrically conductive and is thought to be the region where Uranus' unusual magnetic field <br>" 
            "is generated.<br>" 
            "* It's estimated to extend out to roughly 60-70% of Uranus' total radius.<br>" 
            "* The temperature of Uranus' mantle is thought to range from around 2,000 K at its outer edge to about 5,000 K near <br>" 
            "the core.<br>" 
            "* The theoretical black body color of Uranus' mantle would transition from a deep orange-red in the outer regions to <br>" 
            "a pale yellow-white in the deeper regions near the core, if we could somehow observe its thermal radiation directly."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * URANUS_RADIUS_AU
    
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
            name=f"Uranus: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Uranus: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

uranus_cloud_layer_info = (
            "USE MANUAL SCALED OF 0.005 AU TO VIEW CLOSELY."
            "4.6 MB PER FRAME FOR HTML.\n\n"
            "Troposphere: This is the lowest and densest part of the atmosphere, extending from where the pressure is about 100 bar \n" 
            "(deep inside) up to an altitude of roughly 50 kilometers, where the pressure is around 0.1 bar. In the troposphere, the \n" 
            "temperature generally decreases with altitude, ranging from around 320 K at the base to a frigid 53 K at the top. This \n" 
            "region is where most of Uranus' cloud activity occurs. There are several cloud layers within the troposphere, thought to \n" 
            "be composed of water ice (deepest), ammonium hydrosulfide, ammonia and hydrogen sulfide, and finally methane ice at the \n" 
            "highest levels."
)

def create_uranus_cloud_layer_shell(center_position=(0, 0, 0)):
    """Creates Uranus's cloud layer shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 1.0,  # the top of the troposphere is actually 1.002
        'color': 'rgb(173, 216, 230)',  # optical
        'opacity': 1.0,
        'name': 'Cloud Layer',
        'description': (
            "Uranus Cloud Layer<br>" 
            "(Note: toggle off the cloud layer in the legend to better see the interior structure.)<br><br>"
            "Troposphere: This is the lowest and densest part of the atmosphere, extending from where the pressure is about 100 bar <br>" 
            "(deep inside) up to an altitude of roughly 50 kilometers, where the pressure is around 0.1 bar. In the troposphere, the <br>" 
            "temperature generally decreases with altitude, ranging from around 320 K at the base to a frigid 53 K at the top. This <br>" 
            "region is where most of Uranus' cloud activity occurs. There are several cloud layers within the troposphere, thought to <br>" 
            "be composed of water ice (deepest), ammonium hydrosulfide, ammonia and hydrogen sulfide, and finally methane ice at the <br>" 
            "highest levels.<br>" 
            "* Radius Definition: The top of the troposphere, or the cloud layer, is not equivalent to the radius of Uranus. The radius of Uranus is <br>" 
            "  defined at a specific pressure level in its atmosphere. The quoted radius of Uranus (around 25,559 km at the equator) <br>" 
            "  is typically given at the 1 bar pressure level. This is an arbitrary but standard reference point in the atmosphere of <br>" 
            "  gas giants, roughly equivalent to Earth's sea-level atmospheric pressure. Since Uranus doesn't have a solid surface, this <br>" 
            "  pressure level serves as a convenient marker for the planet's \"size.\"<br>"
            "* Troposphere and Cloud Layer Altitude: The troposphere of Uranus extends from deep within the atmosphere (pressures <br>" 
            "  around 100 bar) up to an altitude of about 50 km above the 1 bar level, where the pressure is around 0.1 bar. The <br>" 
            "  cloud layers exist within this troposphere. The uppermost cloud layer, composed of methane ice, is found at a pressure <br>" 
            "  level of about 1.2 bar. The visible cloud layer and the top of the troposphere are located within Uranus' atmosphere, <br>" 
            "  at altitudes significantly lower than the radius defined at the 1 bar pressure level. The radius encompasses all these <br>" 
            "  atmospheric layers down to that defined pressure. The radius of Uranus is like saying the \"surface\" is at a certain <br>" 
            "  depth in the atmosphere. The clouds are features that exist above that deeper level.<br>" 
            "* The top of Uranus' troposphere is defined by the tropopause, which is the temperature minimum in the atmosphere, <br>" 
            "  separating the troposphere from the stratosphere. This occurs at an altitude of approximately 50 kilometers above the <br>" 
            "  1 bar pressure level. At this altitude, the pressure is around 0.1 bar. Since the radius of Uranus is conventionally <br>" 
            "  defined at the 1 bar pressure level as approximately 25,559 kilometers, the equivalent radius at the top of the <br>" 
            "  troposphere (or cloud layer, which is within the upper troposphere) would be approximately 25,559 km + 50 km = 25,609 <br>" 
            "  kilometers. Therefore, the radius at the top of the troposphere is about 25,609 kilometers. To express this as a <br>" 
            "  fraction of Uranus' radius at the 1 bar level: Fraction = 25,609 km / 25,559 km ~ 1.002."
            )
    }
    
    # Calculate radius in AU
    radius = layer_info['radius_fraction'] * URANUS_RADIUS_AU
    
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
        name=f"Uranus: {layer_info['name']}",
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
    layer_name = f"Uranus: {layer_info['name']}"
    minimal_hover_texts = [layer_name] * len(x_hover)

    # Create hover trace with direct text assignment
    hover_trace = go.Scatter3d(
        x=x_hover, 
        y=y_hover, 
        z=z_hover,
        mode='markers',
        marker=dict(
            size=2,  # originally 5
            color='rgb(173, 216, 230)',  # Layer color, originally 'white'
            opacity=1.0,  # originally 0.8
            line=dict(  # Add a contrasting outline
                width=1,
                color='black'
            )
        ),
        name=f"Uranus: {layer_info['name']} (Info)",
        text=hover_texts,  # IMPORTANT: Matching length with coordinate arrays
        customdata=minimal_hover_texts,  # For "Object Names Only" mode
        hovertemplate='%{text}<extra></extra>',  # Use the standard hover template
        showlegend=False  # Don't show in legend since it's just for hover
    )

    return [surface_trace, hover_trace]

uranus_upper_atmosphere_info = (
            "2.7 MB PER FRAME FOR HTML.\n\n"
            "Atmosphere: Uranus has a thick atmosphere primarily composed of Hydrogen (H2): Making up about 83% of the atmosphere; \n" 
            "Helium (He): Constituting around 15%; Methane (CH4): Present in smaller amounts, around 2.3%. This methane absorbs red \n" 
            "light, giving Uranus its characteristic blue-green hue. Trace amounts: Water (H2O) and ammonia (NH3) are also present \n" 
            "in small quantities. Other hydrocarbons like ethane, acetylene, and methyl acetylene exist in trace amounts, formed by \n" 
            "the breakdown of methane by sunlight. The atmosphere lacks the prominent banding seen on Jupiter and Saturn but does \n" 
            "experience extremely cold temperatures, reaching as low as 49 Kelvin (-224  degC), making it the coldest planetary \n" 
            "atmosphere in our solar system. The atmosphere is layered into a troposphere, stratosphere, and thermosphere."
)

def create_uranus_upper_atmosphere_shell(center_position=(0, 0, 0)):
    """Creates Uranus's upper atmosphere shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 1.16,  
        'color': 'rgb(240, 245, 250)',  # optical pale blue
        'opacity': 0.5,
        'name': 'Upper Atmosphere',
        'description': (
            "Atmosphere: Uranus has a thick atmosphere primarily composed of Hydrogen (H2): Making up about 83% of the atmosphere; <br>" 
            "Helium (He): Constituting around 15%; Methane (CH4): Present in smaller amounts, around 2.3%. This methane absorbs red <br>" 
            "light, giving Uranus its characteristic blue-green hue. Trace amounts: Water (H2O) and ammonia (NH3) are also present <br>" 
            "in small quantities. Other hydrocarbons like ethane, acetylene, and methyl acetylene exist in trace amounts, formed by <br>" 
            "the breakdown of methane by sunlight. The atmosphere lacks the prominent banding seen on Jupiter and Saturn but does <br>" 
            "experience extremely cold temperatures, reaching as low as 49 Kelvin (-224  degC), making it the coldest planetary <br>" 
            "atmosphere in our solar system. The atmosphere is layered into a troposphere, stratosphere, and thermosphere.<br>" 
            "* The altitude of the top of Uranus' thermosphere is not as sharply defined as the tropopause. The thermosphere <br>" 
            "  gradually transitions into the exosphere. The stratosphere extends up to about 4,000 kilometers above the 1 bar <br>" 
            "  level. The thermosphere and exosphere then extend from this altitude outwards. Some sources suggest the thermosphere <br>" 
            "  can reach as high as two Uranus radii from the planet's center.<br>" 
            "* Top of Stratosphere (approximate lower bound of Thermosphere): Radius at 1 bar level: ~ 25,559 km; Altitude of <br>" 
            "  stratopause: ~ 4,000 km; Equivalent radius: 25,559 km + 4,000 km = 29,559 kilometers; Fraction of Uranus' radius <br>" 
            "  (at 1 bar): 29,559 km / 25,559 km ~ 1.157.<br>" 
            "* Outer Extent of Thermosphere/Exosphere (approximate upper bound): Radius at 1 bar level: ~ 25,559 km; Two Uranus radii <br>" 
            "  from the center: 2 * 25,559 km = 51,118 kilometers. Therefore, the equivalent radius at the top of the thermosphere <br>" 
            "  (or more accurately, the extended thermosphere/exosphere region) is estimated to range from approximately 1.16 to 2.0 <br>" 
            "  times the radius of Uranus as defined at the 1 bar pressure level. This indicates that the thermosphere of Uranus is a <br>" 
            "  very extended and diffuse region of its upper atmosphere."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * URANUS_RADIUS_AU
    
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
            name=f"Uranus: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Uranus: {layer_info['name']}"] * len(x),
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

uranus_magnetosphere_info = (
            "SELECT MANUAL SCALE OF AT LEAST 0.2 AU TO VISUALIZE.\n"
            "1.4 MB PER FRAME FOR HTML.\n\n"

            "Magnetic Field (Magnetosphere): Uranus possesses a unique and peculiar magnetic field. Unlike most planets, its \n" 
            "magnetic axis is tilted at a dramatic angle of nearly 60 degrees relative to its rotational axis. Furthermore, the \n" 
            "magnetic field is offset from the planet's center by about one-third of Uranus' radius. This unusual orientation \n" 
            "leads to a magnetosphere that is highly distorted and asymmetric. The magnetic field is generated by the convective \n" 
            "motions of electrically conductive materials (likely the icy mantle) within the planet. The strength of Uranus' \n" 
            "dipole magnetic field is significant, about 50 times that of Earth's, although smaller than Jupiter's. The \n" 
            "magnetosphere deflects the solar wind, creating a complex boundary called the magnetopause, which extends a \n" 
            "considerable distance from the planet."                      
)

def create_uranus_magnetosphere(center_position=(0, 0, 0)):
    """Creates Uranus's main magnetosphere structure."""
    # Parameters for magnetosphere components (in Uranus radii)
    params = {
        # Compressed sunward side
        'sunward_distance': 21,  # Compressed toward the sun, ranges from 18-24 Ru
        
        # Equatorial extension (wider than polar)
        'equatorial_radius': 27.5,   # ranges from 25-30 Ru
        'polar_radius': 17.5,         # ranges from 15-20 Rs
        
        # Magnetotail parameters
        'tail_length': 300,  # Length of visible magnetotail, ranges from 200-500 Ru
        'tail_base_radius': 15,  # Radius at the base of the tail, ranges from 10-20 Ru
        'tail_end_radius': 75,  # Radius at the end of the tail, ranges from 50-100 Ru
    }
    
    # Scale everything by Uranus's radius in AU
    for key in params:
        params[key] *= URANUS_RADIUS_AU
    
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
                opacity=0.3
            ),
            name='Uranus: Magnetosphere',
            text=["Magnetic Field (Magnetosphere): Uranus possesses a unique and peculiar magnetic field. Unlike most planets, its <br>" 
            "magnetic axis is tilted at a dramatic angle of nearly 60 degrees relative to its rotational axis. Furthermore, the <br>" 
            "magnetic field is offset from the planet's center by about one-third of Uranus' radius. This unusual orientation <br>" 
            "leads to a magnetosphere that is highly distorted and asymmetric. The magnetic field is generated by the convective <br>" 
            "motions of electrically conductive materials (likely the icy mantle) within the planet. The strength of Uranus' <br>" 
            "dipole magnetic field is significant, about 50 times that of Earth's, although smaller than Jupiter's. The <br>" 
            "magnetosphere deflects the solar wind, creating a complex boundary called the magnetopause, which extends a <br>" 
            "considerable distance from the planet.<br>" 
            "The Bow Shock points towards the Sun along the X-axis. The XY plane is the ecliptic.<br>" 
            "* The distance to Uranus' magnetopause (the boundary where the planet's magnetic field meets the solar wind) on the <BR>" 
            "  sunward side is estimated to be around 18-24 Ru.<br>" 
            "* The equatorial radius of Uranus' magnetosphere varies depending on solar wind conditions, but a typical estimate is <br>" 
            "  around 25-30 Ru.<br>" 
            "* The polar radius of Uranus' magnetosphere, measured from the center of the planet to the magnetopause along the <br>" 
            "  magnetic poles, is typically smaller than the equatorial radius due to the interaction with the solar wind and the <br>" 
            "  shape of the magnetic field. Estimates range, but it's likely in the order of 15-20 Ru.<br>" 
            "* The magnetotail is the region of the magnetosphere that extends away from the Sun, stretched by the solar wind. The <br>" 
            "  length of Uranus' magnetotail is highly variable and depends on the conditions of the solar wind. However, Voyager 2 <br>" 
            "  observations provided some insights. Estimates for the length of Uranus' magnetotail range significantly, but it's <br>" 
            "  often cited to extend hundreds of Uranus radii downwind. A reasonable estimate based on observations would be in the <br>" 
            "  order of several hundred Ru, perhaps around 200-500 Ru or even more under certain solar wind conditions.<br>" 
            "* The \"base\" of the magnetotail is the region connected to the planet's nightside magnetosphere. Its radius is <br>" 
            "  related to the size of the obstacle the planet presents to the solar wind. A typical estimate for the radius of the <br>" 
            "  magnetotail near the planet (the base) is on the order of the planet's radius. So, the tail base radius is estimated <br>" 
            "  to be around 10-20 Ru.<br>" 
            "* The magnetotail flares out as it extends away from the planet. The radius at the \"end\" (where it becomes less <br>" 
            "  well-defined and merges with the interplanetary medium) would be larger than at the base. This is even more variable <br>" 
            "  and less well-defined than the tail length. It could be several tens of Uranus radii. So, a rough estimate for the <br>" 
            "  tail end radius is ~50-100 Ru."] * len(x),
            customdata=['Magnetosphere'] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    sun_traces = create_sun_direction_indicator(
        center_position=center_position, 
        shell_radius=300 * URANUS_RADIUS_AU
    )
    for trace in sun_traces:
        traces.append(trace)

    return traces

uranus_radiation_belts_info = (
            "560 KB PER FRAME FOR HTML.\n\n"
            "Zones of trapped high-energy particles in uranus's magnetosphere"                     
)

def create_uranus_radiation_belts(center_position=(0, 0, 0)):
    """Creates Uranus's radiation belts."""
    belt_colors = ['rgb(255, 255, 100)', 'rgb(100, 255, 150)']
    belt_names = ['Inner Radiation Belt', 'Outer Radiation Belt']
    belt_texts = [
        "Radiation Belts: Regions in its magnetosphere where charged particles (mainly electrons and protons) are trapped and <br>" 
        "accelerated by the magnetic field. Voyager 2 data revealed that Uranus' electron radiation belts are surprisingly intense, <br>" 
        "comparable to Earth's and much stronger than Saturn's. The source of these energetic particles is primarily the planet's <br>" 
        "upper atmosphere.<br>" 
        "* Voyager 2 was the first and so far only spacecraft to directly observe them during its flyby in 1986.<br>" 
        "* Composition: The primary charged particles in Uranus' radiation belts are electrons and protons. There is also a minor <br>" 
        "  component of molecular hydrogen ions.<br>" 
        "* Intensity: The intensity of Uranus' electron radiation belts was surprisingly found to be similar to those of Earth and <br>" 
        "  significantly more intense than those of Saturn. However, the proton radiation belts were observed to be much weaker than <br>" 
        "  expected, about 100 times lower than predicted.<br>" 
        "* Effects: The intense radiation in the electron belts can cause rapid darkening (within about 100,000 years) of any methane <br>" 
        "  trapped in the icy surfaces of Uranus' inner moons and ring particles. This is a likely contributor to the uniformly dark <br>" 
        "  and gray appearance of these objects. Uranus' moons can also create gaps in the radiation belts by sweeping up charged <br>" 
        "  particles as they orbit the planet.<br>" 
        "* Distances from Uranus' Center: The precise boundaries of Uranus' radiation belts are not as sharply defined as Earth's <br>" 
        "  Van Allen belts, and their structure is influenced by Uranus' unusual, highly tilted, and offset magnetic field. However, <br>" 
        "  based on Voyager 2 data and subsequent modeling, we can provide approximate ranges:<br>" 
        "  * Inner Radiation Belt (primarily protons): This belt is thought to be relatively weak and located closer to the planet, <br>" 
        "    likely within a few Uranus radii. Estimates suggest it may extend from around 1 to 3 R. However, its intensity is much <br>" 
        "    lower than expected.<br>" 
        "  * Outer Radiation Belt (primarily electrons): This belt is surprisingly intense, comparable to Earth's and much stronger <br>" 
        "    than Saturn's. It is believed to extend further out, roughly from 3 to 10 R. Some models suggest it might even extend <br>" 
        "    beyond this range, but the most intense regions are within 10 R.<br>" 
        "  * Asymmetry: Due to the complex magnetic field, the radiation belts are likely asymmetric and their extent can vary with <br>" 
        "    latitude and longitude.<br>" 
        "  * Dynamic: The structure and intensity of the belts can be influenced by solar wind activity.<br>" 
        "  * Data Limitations: Our understanding is primarily based on a single flyby from Voyager 2. Future missions are needed for <br>" 
        "    a more comprehensive mapping of Uranus' radiation belts.<br>",

        "Radiation Belts: Regions in its magnetosphere where charged particles (mainly electrons and protons) are trapped and <br>" 
        "accelerated by the magnetic field. Voyager 2 data revealed that Uranus' electron radiation belts are surprisingly intense, <br>" 
        "comparable to Earth's and much stronger than Saturn's. The source of these energetic particles is primarily the planet's <br>" 
        "upper atmosphere.<br>" 
        "* Voyager 2 was the first and so far only spacecraft to directly observe them during its flyby in 1986.<br>" 
        "* Composition: The primary charged particles in Uranus' radiation belts are electrons and protons. There is also a minor <br>" 
        "  component of molecular hydrogen ions.<br>" 
        "* Intensity: The intensity of Uranus' electron radiation belts was surprisingly found to be similar to those of Earth and <br>" 
        "  significantly more intense than those of Saturn. However, the proton radiation belts were observed to be much weaker than <br>" 
        "  expected, about 100 times lower than predicted.<br>" 
        "* Effects: The intense radiation in the electron belts can cause rapid darkening (within about 100,000 years) of any methane <br>" 
        "  trapped in the icy surfaces of Uranus' inner moons and ring particles. This is a likely contributor to the uniformly dark <br>" 
        "  and gray appearance of these objects. Uranus' moons can also create gaps in the radiation belts by sweeping up charged <br>" 
        "  particles as they orbit the planet.<br>" 
        "* Distances from Uranus' Center: The precise boundaries of Uranus' radiation belts are not as sharply defined as Earth's <br>" 
        "  Van Allen belts, and their structure is influenced by Uranus' unusual, highly tilted, and offset magnetic field. However, <br>" 
        "  based on Voyager 2 data and subsequent modeling, we can provide approximate ranges:<br>" 
        "  * Inner Radiation Belt (primarily protons): This belt is thought to be relatively weak and located closer to the planet, <br>" 
        "    likely within a few Uranus radii. Estimates suggest it may extend from around 1 to 3 R. However, its intensity is much <br>" 
        "    lower than expected.<br>" 
        "  * Outer Radiation Belt (primarily electrons): This belt is surprisingly intense, comparable to Earth's and much stronger <br>" 
        "    than Saturn's. It is believed to extend further out, roughly from 3 to 10 R. Some models suggest it might even extend <br>" 
        "    beyond this range, but the most intense regions are within 10 R.<br>" 
        "  * Asymmetry: Due to the complex magnetic field, the radiation belts are likely asymmetric and their extent can vary with <br>" 
        "    latitude and longitude.<br>" 
        "  * Dynamic: The structure and intensity of the belts can be influenced by solar wind activity.<br>" 
        "  * Data Limitations: Our understanding is primarily based on a single flyby from Voyager 2. Future missions are needed for <br>" 
        "    a more comprehensive mapping of Uranus' radiation belts.<br>" 
    ]
    
    # Belt distances in Uranus radii from the planet's center
    belt_distances = [2, 6]
    belt_thickness = 0.5 * URANUS_RADIUS_AU
    
    # Scale distances by Uranus's radius in AU
    belt_distances = [d * URANUS_RADIUS_AU for d in belt_distances]
    
    # Unpack center position
    center_x, center_y, center_z = center_position

    # uranus tilt is 97.77 degrees, 105 was arrived at by trial and error
    uranus_tilt = np.radians(105)
    
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
        belt_x_tilted, belt_y_tilted, belt_z_tilted = rotate_points(belt_x, belt_y, belt_z, uranus_tilt, 'x')
            
            
            # First apply rotation around x-axis
    #    x_tilted, y_tilted, z_tilted = rotate_points(x, y, z, np.radians(uranus_tilt), 'x')
            
            # Then apply rotation around y-axis with the same angle
        belt_x_final, belt_y_final, belt_z_final = rotate_points(belt_x_tilted, belt_y_tilted, belt_z_tilted, uranus_tilt, 'y')        

        # Apply center position offset
    #    x = np.array(x) + center_x
    #    y = np.array(y) + center_y
    #    z = np.array(z) + center_z

        # Apply center position offset
    #    x_final = np.array(x_tilted) + center_x
    #    y_final = np.array(y_tilted) + center_y
    #    z_final = np.array(z_tilted) + center_z
        
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
        shell_radius= 6.0 * URANUS_RADIUS_AU
    )
    for trace in sun_traces:
        traces.append(trace)

    return traces
    
uranus_ring_system_info = (
                "22.2 MB PER FRAME FOR HTML.\n\n"

                "Uranus has a system of 13 known rings. These rings are generally very narrow, dark (reflecting very little light, \n" 
                "similar to charcoal), and composed of dust and larger particles that are icy and darkened by rock. The rings are \n" 
                "grouped into two main systems:\n" 
                "* Inner Rings: Nine narrow, dark rings.\n" 
                "* Outer Rings: Two more distant rings, one of which is bluish and the other reddish.\n" 
                "While the main rings of Uranus are narrow bands, there are also broader, more diffuse rings made of dust. These \n" 
                "dusty rings could be considered to have a more toroidal (donut-like) distribution of material compared to the thin, \n" 
                "distinct main rings. For example, the outermost rings (Nu and Mu) are quite broad and dusty.\n" 
                "* There are nine main, narrow rings. These rings are relatively dense and have well-defined edges. They are composed \n" 
                "  mostly of larger, darker particles, often described as being the color of charcoal. Examples of the main rings include \n" 
                "  the Epsilon, Delta, Gamma, Eta, Beta, Alpha, and the numbered rings 4, 5, and 6. The Epsilon ring is the outermost and \n" 
                "  widest of the main rings.\n" 
                "* There are two outer rings: the Nu ring and the Mu ring. These rings are much fainter and more diffuse than the main \n" 
                "  rings. They are composed of fine dust particles. The Mu ring is quite broad and has a more torus-like distribution of \n" 
                "  material. It also has a distinct blue color, similar to Saturn's E ring. The Nu ring is reddish in color, similar to \n" 
                "  dusty rings seen elsewhere in the solar system.\n" 
                "* Composition: The main rings are primarily larger, dark particles, while the outer rings are predominantly fine dust.\n" 
                "* Structure: The main rings are narrow and well-defined, whereas the outer rings are broad and diffuse, with the Mu \n" 
                "  ring exhibiting a clear torus-like structure.\n" 
                "* Origin and Evolution: The origins and the processes that shape these different sets of rings might vary. The dusty \n" 
                "  outer rings are likely fed by dust kicked off Uranus' inner moons by micrometeoroid impacts.\n" 
                "* Visual Characteristics: The main rings are dark and difficult to see, requiring specific observation techniques. The \n" 
                "  outer rings are even fainter, with the Mu ring having a unique blue color.\n" 
                "In summary, while all are part of Uranus' ring system, the significant differences in their composition, structure, and \n" 
                "likely origin make it accurate and informative to distinguish between the narrow, dark main rings and the broad, dusty, \n" 
                "and torus-like outer rings."                                           
)

def create_uranus_ring_system(center_position=(0, 0, 0)):
    """
    Creates a visualization of Saturn's ring system.
    
    Parameters:
        center_position (tuple): (x, y, z) position of Saturn's center
        
    Returns:
        list: A list of plotly traces representing the ring components

    Uranus Ring System Transformation:

    For proper alignment with satellite orbits, Uranus's ring system requires a specific 
    compound rotation approach due to the planet's extreme axial tilt (97.77 deg).

    The transformation uses these key elements:
    1. A 105 deg rotation around the X-axis followed by a 105 deg rotation around the Y-axis
    (empirically determined to match satellite orbit alignment)
    2. Converting point coordinates to NumPy arrays before rotation
    3. Applying center position offset to the final coordinates after both rotations

    This approach ensures that all components of the Uranian system (rings, satellites, 
    radiation belts) share the same reference frame, correctly representing the planet's
    unique orientation in space.

    NOTE: The 105 deg value, rather than the nominal 97.77 deg axial tilt, accounts for the 
    specific reference frame conversion between Uranus's equatorial plane and the
    ecliptic coordinate system used for visualization.
    
    """
    traces = []
    
    # Define Saturn's ring parameters in kilometers from Saturn's center
    # Then convert to Saturn radii, and finally to AU
    ring_params = {

        'ring_6': {
            'inner_radius_km': 41800,  # Inner edge (in km from Uranus's center)
            'outer_radius_km': 41802,  # Outer edge (in km from Uranus's center)
            'thickness_km': 2,         # Approximate thickness
            'color': 'rgb(60, 60, 60)',  
            'opacity': 0.4,
            'name': 'Ring 6',
            'description': (
                "Ring 6: Very narrow. Dark gray. 2 km thick. Very narrow, faint.<br>" 
                "* Dark, likely icy particles darkened by radiation<br>" 
                "* Relatively high density for its width.<br>" 
                "* Possibly fragments from small, disrupted moons or impacts on existing moons.<br>" 
                "* Narrow, relatively uniform width."
            )
        },

        'ring_5': {
            'inner_radius_km': 42200,  # Inner edge (in km from Uranus's center)
            'outer_radius_km': 42207,  # Outer edge (in km from Uranus's center)
            'thickness_km': 7,         # Approximate thickness, 2 to 7 km
            'color': 'rgb(65, 65, 65)',  
            'opacity': 0.4,
            'name': 'Ring 5',
            'description': (
                "Ring 5: Narrow. Dark gray. 2 to 7 km thick.<br>" 
                "* Narrow, slightly wider than Ring 6.<br>" 
                "* Dark, likely icy particles darkened by radiation.<br>" 
                "* Relatively high density for its width.<br>" 
                "* Possibly fragments from small, disrupted moons or impacts on existing moons.<br>" 
                "* Narrow, relatively uniform width."
            )
        },

        'ring_4': {
            'inner_radius_km': 42600,  # Inner edge (in km from Uranus's center)
            'outer_radius_km': 42603,  # Outer edge (in km from Uranus's center)
            'thickness_km': 3,         # Approximate thickness 
            'color': 'rgb(60, 60, 60)',  
            'opacity': 0.4,
            'name': 'Ring 4',
            'description': (
                "Ring 4: Narrow. Dark gray. 3 km thick.<br>" 
                "* Narrow, very faint.<br>" 
                "* Dark, likely icy particles darkened by radiation.<br>" 
                "* Relatively high density for its width.<br>" 
                "* Possibly fragments from small, disrupted moons or impacts on existing moons.<br>" 
                "* Narrow, relatively uniform width."
            )
        },

        'alpha_ring': {
            'inner_radius_km': 44700,  # Inner edge (in km from Uranus's center)
            'outer_radius_km': 44710,  # Outer edge (in km from Uranus's center)
            'thickness_km': 10,         # Approximate thickness, 4 to 10 km
            'color': 'rgb(70, 70, 70)',  
            'opacity': 0.3,
            'name': 'Alpha Ring',
            'description': (
                "Alpha Ring: Relatively narrow. Dark gray. 4 to 10 km thick.<br>" 
                "* Relatively narrow, but wider than 4, 5, 6.<br>" 
                "* Shows some brightness variations.<br>" 
                "* Dark, likely icy particles darkened by radiation.<br>" 
                "* Moderate to high density for its width.<br>" 
                "* Possibly fragments from small, disrupted moons or impacts on existing moons, perhaps confined by shepherd moons.<br>" 
                "* Narrow, slight variations in width."
            )
        },

        'beta_ring': {
            'inner_radius_km': 45700,  # Inner edge (in km from Uranus's center)
            'outer_radius_km': 45711,  # Outer edge (in km from Uranus's center)
            'thickness_km': 11,         # Approximate thickness, 5 to 11 km
            'color': 'rgb(75, 75, 75)',  
            'opacity': 0.4,
            'name': 'Beta Ring',
            'description': (
                "Beta Ring: Relatively narrow, but can be brighter than Alpha. Dark gray, sometimes appears slightly lighter. <br>" 
                "5 to 11 km thick.<br>" 
                "* Relatively narrow, can be brighter than Alpha.<br>" 
                "* Shows some structure.<br>" 
                "* Dark, likely icy particles darkened by radiation.<br>" 
                "* Moderate to high density for its width.<br>" 
                "* Possibly fragments from small, disrupted moons or impacts on existing moons, perhaps confined by shepherd moons.<br>" 
                "* Narrow, slight variations in width."
            )
        },        

        'eta_ring': {
            'inner_radius_km': 47200,  # Inner edge (in km from Uranus's center)
            'outer_radius_km': 47202,  # Outer edge (in km from Uranus's center)
            'thickness_km': 2,         
            'color': 'rgb(80, 70, 70)',  
            'opacity': 0.2,
            'name': 'Eta Ring',
            'description': (
                "Eta Ring: Narrow, has a dusty component. Dark gray with a possible faint reddish tint due to associated dust. 2 km thick.<br>" 
                "* Narrow, has a faint, dusty component extending inwards and outwards.<br>" 
                "* Associated with the moon Mab's orbit.<br>" 
                "* Dark, likely icy particles mixed with fine dust.<br>" 
                "* Low to moderate density.<br>" 
                "* Likely generated by micrometeoroid impacts on small inner moons, with dustier regions.<br>" 
                "* Narrow core with broader, diffuse edges."
            )
        }, 

        'gamma_ring': {
            'inner_radius_km': 47600,  # Inner edge (in km from Uranus's center)
            'outer_radius_km': 47604,  # Outer edge (in km from Uranus's center)
            'thickness_km': 4,         # 1 to 4 km
            'color': 'rgb(70, 75, 70)',  
            'opacity': 0.4,
            'name': 'Gamma Ring',
            'description': (
                "Gamma Ring: Narrow, can appear brighter than Eta. Dark gray, sometimes appears slightly greenish in false-color <br>" 
                "images used to study composition. 1 to 4 km thick.<br>" 
                "* Narrow, can appear brighter than Eta.<br>" 
                "* Shows some evidence of structure.<br>" 
                "* Dark, likely icy particles darkened by radiation.<br>" 
                "* Relatively high density for its width.<br>" 
                "* Possibly fragments from small, disrupted moons or impacts on existing moons, perhaps confined by shepherd moons.<br>" 
                "* Narrow, relatively uniform width."
            )
        },

         'delta_ring': {
            'inner_radius_km': 48300,  # Inner edge (in km from Uranus's center)
            'outer_radius_km': 48307,  # Outer edge (in km from Uranus's center)
            'thickness_km': 7,         # 3 to 7 km
            'color': 'rgb(70, 70, 75)',  
            'opacity': 0.3,
            'name': 'Delta Ring',
            'description': (
                "Delta Ring: Narrow, shows some variations in width and brightness. Dark gray, may show a subtle bluish tint in some <br>" 
                "enhanced images, but overall very dark. 3 to 7 km thick.<br>" 
                "* Narrow, shows significant variations in width and brightness along its circumference.<br>" 
                "* Has a faint, inner dusty component.<br>" 
                "* Dark, likely icy particles darkened by radiation mixed with some dust.<br>" 
                "* Moderate density.<br>" 
                "* Possibly fragments from small, disrupted moons or impacts, with confinement and dust generation mechanisms.<br>" 
                "* Narrow, with localized wider and fainter regions."
            )
        },    

         'epsilon_ring': {
            'inner_radius_km': 51100,  # Inner edge (in km from Uranus's center)
            'outer_radius_km': 51190,  # Outer edge (in km from Uranus's center)
            'thickness_km': 60,         # 20-100 km
            'color': 'rgb(70, 70, 70)',  
            'opacity': 0.3,
            'name': 'Epsilon Ring',
            'description': (
                "Epsilon Ring: Widest and most substantial of the main rings, density variations along it. Neutral dark gray. While <br>" 
                "the outer dusty Mu ring is bluish, the main Epsilon ring itself is generally considered neutral in color. 20-100 km thick.<br>" 
                "* Widest and most substantial of the main rings.<br>" 
                "* Shows significant density variations and kinks.<br>" 
                "* Confined by shepherd moons Cordelia and Ophelia.<br>" 
                "* Dark, likely icy particles darkened by radiation.<br>" 
                "* Variable density, generally moderate.<br>" 
                "* Likely fragments from a disrupted moon, with its sharp edges maintained by shepherd moons.<br>" 
                "* Relatively wide, with varying width and density."
            )
        },           

         'nu_gossamer_ring': {
            'inner_radius_km': 62000,  # Inner edge (in km from Uranus's center)
            'outer_radius_km': 97700,  # Outer edge (in km from Uranus's center)
            'thickness_km': 9500,         # 7000 to 12000 km
            'color': 'rgb(150, 100, 100)',  
            'opacity': 0.1,
            'name': 'Nu Gossamer Ring',
            'description': (
                "Nu Gossamer Ring: Broad, faint, and dusty outer ring. It's associated with the moon Portia. Faint reddish/dusty. <br>" 
                "7,000 to 12,000 km thick. These rings are much fainter and more diffuse than the main rings, composed primarily of <br>" 
                "fine dust particles. Their thicknesses are much greater than the main rings due to their diffuse nature. <br>" 
                "* The Mu ring's inner boundary (~86,000 km) is well within the Nu ring's outer boundary (~97,700 km). There is a <br>" 
                "  region between approximately 86,000 km and 97,700 km from Uranus' center where material from both rings can be <br>" 
                "  found. However, it's important to remember that these are broad, dusty rings. The density of particles within <br>" 
                "  them is likely quite low, and the overlap doesn't necessarily mean a dense collision zone like you might imagine <br>" 
                "  with solid rings. Instead, it's a region where the diffuse dust distributions of both rings coexist.<br>" 
                "* Faint and Diffuse: The Mu and Nu rings are indeed very faint and were discovered much later than the main rings, <br>" 
                "  requiring sensitive instruments like the Hubble Space Telescope and Voyager 2. Their low brightness indicates a low <br>" 
                "  density of particles.<br>" 
                "* Dust-Dominated: Observations confirm that these outer rings are primarily composed of fine dust particles. This is <br>" 
                "  evidenced by their colors (bluish for Mu, reddish for Nu), which are likely due to the way these small particles <br>" 
                "  scatter sunlight.<br>" 
                "* Source Moons: Both rings are strongly associated with small inner moons. Mu ring is linked to the moon Mab, which <br>" 
                "  orbits within it and is believed to be the primary source of its dust through micrometeoroid impacts. Nu ring is <br>" 
                "  associated with the moon Portia, although the exact mechanism of its dust generation is still being studied.<br>" 
                "* Broad Radial Extent: As the radius information shows, both the Mu and Nu rings are significantly broader than the <br>" 
                "  narrow main rings of Uranus.<br>"                
                "* Broad, faint, and dusty outer ring extending significantly outwards.<br>" 
                "* Fine dust.<br>" 
                "* Very low density.<br>"  
                "* Broad, diffuse, torus-like."
            )
        },

         'Mu__goassamer_ring': {
            'inner_radius_km': 86000,  # Inner edge (in km from Uranus's center)
            'outer_radius_km': 102000,  # Outer edge (in km from Uranus's center)
            'thickness_km': 16000,         # 15000 to 17000 km
            'color': 'rgb(100, 150, 200)',  
            'opacity': 0.1,
            'name': 'Mu Gossamer Ring',
            'description': (
                "Mu Gossamer Ring: Very broad, faint, and dusty outermost ring. It has a distinct bluish color and is associated with <br>" 
                "the moon Mab. Muted blue. 15,000 to 17,000 km thick. These rings are much fainter and more diffuse than the main <br>" 
                "rings, composed primarily of fine dust particles.<br>"
                "* The Mu ring's inner boundary (~86,000 km) is well within the Nu ring's outer boundary (~97,700 km). There is a <br>" 
                "  region between approximately 86,000 km and 97,700 km from Uranus' center where material from both rings can be <br>" 
                "  found. However, it's important to remember that these are broad, dusty rings. The density of particles within <br>" 
                "  them is likely quite low, and the overlap doesn't necessarily mean a dense collision zone like you might imagine <br>" 
                "  with solid rings. Instead, it's a region where the diffuse dust distributions of both rings coexist.<br>" 
                "* Faint and Diffuse: The Mu and Nu rings are indeed very faint and were discovered much later than the main rings, <br>" 
                "  requiring sensitive instruments like the Hubble Space Telescope and Voyager 2. Their low brightness indicates a low <br>" 
                "  density of particles.<br>" 
                "* Dust-Dominated: Observations confirm that these outer rings are primarily composed of fine dust particles. This is <br>" 
                "  evidenced by their colors (bluish for Mu, reddish for Nu), which are likely due to the way these small particles <br>" 
                "  scatter sunlight.<br>" 
                "* Source Moons: Both rings are strongly associated with small inner moons. Mu ring is linked to the moon Mab, which <br>" 
                "  orbits within it and is believed to be the primary source of its dust through micrometeoroid impacts. Nu ring is <br>" 
                "  associated with the moon Portia, although the exact mechanism of its dust generation is still being studied.<br>" 
                "* Broad Radial Extent: As the radius information shows, both the Mu and Nu rings are significantly broader than the <br>" 
                "  narrow main rings of Uranus.<br>"                 
                "* Very broad, faint, and dusty outermost ring with a distinct bluish color.<br>" 
                "* Strongly associated with the moon Mab, which orbits within it.<br>" 
                "* Fine dust (icy?)<br>" 
                "* Very low density.<br>" 
                "* Primarily generated by micrometeoroid impacts ejecting material from the surface of the small moon Mab.<br>" 
                "* Very broad, diffuse, torus-like, somewhat clumpy."                
            )
        },

    }
    
    # Unpack center position
    center_x, center_y, center_z = center_position
    
    uranus_tilt = np.radians(105)  # Convert to radians here, once; actual tilt is 97.77 but using 105 that is best fit empirically

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
        
        # Convert to numpy arrays BEFORE applying rotations
        x = np.array(x)
        y = np.array(y)
        z = np.array(z)           
            
            # Apply the SAME compound rotation as for satellites
            # First apply rotation around x-axis
        x_tilted, y_tilted, z_tilted = rotate_points(x, y, z, uranus_tilt, 'x')
            
            # Then apply rotation around y-axis with the same angle
        x_final, y_final, z_final = rotate_points(x_tilted, y_tilted, z_tilted, uranus_tilt, 'y')        

        # Apply center position offset to the FINAL coordinates
        x_final = x_final + center_x  # Use x_final from Y rotation
        y_final = y_final + center_y  # Use y_final from Y rotation
        z_final = z_final + center_z  # Use z_final from Y rotation
        
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
                name=f"Uranus: {ring_info['name']}",
                text=text_array,
                customdata=[f"Uranus: {ring_info['name']}"] * len(x),
                hovertemplate='%{text}<extra></extra>',
                showlegend=True
            )
        )
    
    sun_traces = create_sun_direction_indicator(
        center_position=center_position, 
        shell_radius=102000 / KM_PER_AU
    )
    for trace in sun_traces:
        traces.append(trace)

    return traces

uranus_hill_sphere_info = (
            "SELECT MANUAL SCALE OF AT LEAST 0.6 AU TO VISUALIZE.\n" 
            "1.3 MB PER FRAME FOR HTML.\n\n"

            "The Hill sphere (also known as the Roche sphere) represents the region around a celestial body where its own gravity \n" 
            "is the dominant force attracting satellites. Uranus has a Hill radius around 7.02x10^7 km, which corresponds to about \n" 
            "2 770 Uranus radii (mean radius ~25 360 km). This means that any moon or other object orbiting Uranus within this \n" 
            "sphere is primarily gravitationally bound to the planet. The major moons and rings of Uranus lie well within its Hill \n" 
            "sphere."                     
)

def create_uranus_hill_sphere_shell(center_position=(0, 0, 0)):
    """Creates Uranus's Hill sphere shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 2770, 
        'color': 'rgb(0, 255, 0)',  # Green for Hill sphere
        'opacity': 0.25,
        'name': 'Hill Sphere',
        'description': (
            "SET MANUAL SCALE OF AT LEAST 0.6 AU TO VISUALIZE.<br><br>"
    "The Hill sphere (also known as the Roche sphere) represents the region around a celestial body where its own gravity <br>" 
    "is the dominant force attracting satellites. Uranus has a Hill radius around 7.02x10^7 km, which corresponds to about <br>" 
    "2 770 Uranus radii (mean radius ~25 360 km). This means that any moon or other object orbiting Uranus within this <br>" 
    "sphere is primarily gravitationally bound to the planet. The major moons and rings of Uranus lie well within its Hill Sphere<br><br>" 
                "The Hill sphere is the region around a where its own gravity is the dominant force in attracting satellites. For <br>" 
                "a planet orbiting a star, it's the region where the planet's gravity is stronger than the star's tidal forces.<br><br>" 
                "The Hill Sphere radius can be described in words as follows: it is equal to the planet's average distance from the <br>" 
                "Sun (its orbital semi-major axis) multiplied by the cube root of the ratio between the planet's mass and three times <br>" 
                "the Sun's mass. In other words, you take how far the planet orbits out from the Sun, then scale that distance by the <br>" 
                "cube root of (planet mass / [3 x solar mass]) to find the boundary within which the planet's gravity dominates over the Sun's."
        )
    }
        
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * URANUS_RADIUS_AU
    
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
            name=f"Uranus: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Uranus: {layer_info['name']}"] * len(x),
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