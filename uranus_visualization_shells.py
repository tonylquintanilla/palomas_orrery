"""
uranus_visualization_shells.py - Uranus interior, ring, and magnetosphere shell traces.

Sphere shells for Uranus interior (core, mantle, clouds). Custom geometry
for the ring system, radiation belts, tilted magnetosphere (59 degrees
from rotation axis), and Hill sphere. Uranus rotates nearly on its side,
making its magnetosphere geometry unique.

Consumed by: planet_visualization.py (routing dispatcher)

Module updated: May 2026 with Anthropic's Claude Opus 4.7
    D3.1 sweep (May 2026): hovertext/legendgroup consolidation.
Source: NASA Uranus Fact Sheet; Ness et al. (1986) Science (magnetosphere/radiation belts);
Nettelmann et al. (2013) Icarus (interior model); Voyager 2 (1986) in-situ measurements.
"""
import numpy as np
import math
import plotly.graph_objs as go
from planet_visualization_utilities import (URANUS_RADIUS_AU, KM_PER_AU, create_sphere_points, create_magnetosphere_shape, 
                                            rotate_points)
from orrery_rendering import create_ring_points, rotate_to_sunward, create_info_marker
from shared_utilities import create_sun_direction_indicator

# Uranus Shell Creation Functions

# Source: NASA Uranus Fact Sheet; Nettelmann et al. (2013) Icarus -- rocky core ~1 Earth mass, 5255 K estimate
uranus_core_info = (
            "2.4 MB PER FRAME FOR HTML.<br><br>"
            "Uranus core: Scientists believe Uranus has a relatively small, rocky core. This core is likely composed of silicate and <br>" 
            "metallic iron-nickel. It's estimated to have a mass roughly equivalent to that of Earth. Temperatures near the core can <br>" 
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
    x, y, z = create_sphere_points(layer_radius, n_points=25)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    r_info = layer_radius * 1.05
    trace_name = f"Uranus: {layer_info['name']}"

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
        marker=dict(size=6, color=layer_info['color'], opacity=0.9,
                    symbol='cross', line=dict(color='white', width=1)),
        name='',
        legendgroup=trace_name,
        text=[f"{trace_name}<br><br>{layer_info['description']}"],
        customdata=[trace_name],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    )

    traces = [shell_trace, info_trace]
    
    return traces

# Source: Nettelmann et al. (2013) -- interior model; ice/rock mantle 10-13 Earth masses
uranus_mantle_info = (
            "2.1 MB PER FRAME FOR HTML.<br><br>"
            "mantle: Surrounding the rocky core is a dense fluid layer often referred to as an \"icy mantle.\" This layer makes up the <br>" 
            "majority (80% or more) of the planet's mass. It's not ice in the traditional sense but rather a hot, dense fluid <br>" 
            "containing water, ammonia, and methane under immense pressure. These are sometimes referred to as \"ices\" by planetary <br>" 
            "scientists. This mantle is electrically conductive and is thought to be the region where Uranus' unusual magnetic field <br>" 
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
    x, y, z = create_sphere_points(layer_radius, n_points=25)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    r_info = layer_radius * 1.05
    trace_name = f"Uranus: {layer_info['name']}"

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
        marker=dict(size=6, color=layer_info['color'], opacity=0.9,
                    symbol='cross', line=dict(color='white', width=1)),
        name='',
        legendgroup=trace_name,
        text=[f"{trace_name}<br><br>{layer_info['description']}"],
        customdata=[trace_name],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    )

    traces = [shell_trace, info_trace]
    
    return traces

# Source: Lindal et al. (1987) JGR; Sromovsky et al. (2011) -- cloud pressures, temperatures, composition
uranus_cloud_layer_info = (
            "USE MANUAL SCALED OF 0.005 AU TO VIEW CLOSELY."
            "4.6 MB PER FRAME FOR HTML.<br><br>"
            "Troposphere: This is the lowest and densest part of the atmosphere, extending from where the pressure is about 100 bar <br>" 
            "(deep inside) up to an altitude of roughly 50 kilometers, where the pressure is around 0.1 bar. In the troposphere, the <br>" 
            "temperature generally decreases with altitude, ranging from around 320 K at the base to a frigid 53 K at the top. This <br>" 
            "region is where most of Uranus' cloud activity occurs. There are several cloud layers within the troposphere, thought to <br>" 
            "be composed of water ice (deepest), ammonium hydrosulfide, ammonia and hydrogen sulfide, and finally methane ice at the <br>" 
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
        legendgroup=f"Uranus: {layer_info['name']}",
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
    trace_name = f"Uranus: {layer_info['name']}"

    hover_trace = go.Scatter3d(
        x=[center_x], y=[center_y], z=[center_z + r_info],
        mode='markers',
        marker=dict(size=6, color=layer_info['color'], opacity=0.9,
                    symbol='cross', line=dict(color='white', width=1)),
        name=trace_name,
        legendgroup=trace_name,
        text=[f"{trace_name}<br><br>{layer_info['description']}"],
        customdata=[f"Uranus: {layer_info['name']}"],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    )

    return [surface_trace, hover_trace]

# Source: NASA Uranus Fact Sheet; Lindal et al. (1987) JGR -- Voyager 2 radio occultation; atmospheric structure
uranus_upper_atmosphere_info = (
            "2.7 MB PER FRAME FOR HTML.<br><br>"
            "Atmosphere: Uranus has a thick atmosphere primarily composed of Hydrogen (H2): Making up about 83% of the atmosphere; <br>" 
            "Helium (He): Constituting around 15%; Methane (CH4): Present in smaller amounts, around 2.3%. This methane absorbs red <br>" 
            "light, giving Uranus its characteristic blue-green hue. Trace amounts: Water (H2O) and ammonia (NH3) are also present <br>" 
            "in small quantities. Other hydrocarbons like ethane, acetylene, and methyl acetylene exist in trace amounts, formed by <br>" 
            "the breakdown of methane by sunlight. The atmosphere lacks the prominent banding seen on Jupiter and Saturn but does <br>" 
            "experience extremely cold temperatures, reaching as low as 49 Kelvin (-224  degC), making it the coldest planetary <br>" 
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
    x, y, z = create_sphere_points(layer_radius, n_points=20)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    r_info = layer_radius * 1.05
    trace_name = f"Uranus: {layer_info['name']}"

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
        marker=dict(size=6, color=layer_info['color'], opacity=0.9,
                    symbol='cross', line=dict(color='white', width=1)),
        name='',
        legendgroup=trace_name,
        text=[f"{trace_name}<br><br>{layer_info['description']}"],
        customdata=[trace_name],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    )

    traces = [shell_trace, info_trace]

    return traces

# Source: Ness et al. (1986) Science -- Voyager 2; magnetic axis 59 deg offset; Herbert (2009) magnetosphere model
uranus_magnetosphere_info = (
            "SELECT MANUAL SCALE OF AT LEAST 0.2 AU TO VISUALIZE.<br>"
            "1.4 MB PER FRAME FOR HTML.<br><br>"

            "Magnetic Field (Magnetosphere): Uranus possesses a unique and peculiar magnetic field. Unlike most planets, its <br>" 
            "magnetic axis is tilted at a dramatic angle of nearly 60 degrees relative to its rotational axis. Furthermore, the <br>" 
            "magnetic field is offset from the planet's center by about one-third of Uranus' radius. This unusual orientation <br>" 
            "leads to a magnetosphere that is highly distorted and asymmetric. The magnetic field is generated by the convective <br>" 
            "motions of electrically conductive materials (likely the icy mantle) within the planet. The strength of Uranus' <br>" 
            "dipole magnetic field is significant, about 50 times that of Earth's, although smaller than Jupiter's. The <br>" 
            "magnetosphere deflects the solar wind, creating a complex boundary called the magnetopause, which extends a <br>" 
            "considerable distance from the planet."                      
)

def create_uranus_magnetosphere(center_position=(0, 0, 0), sun_position=(0, 0, 0)):
    """Creates Uranus's main magnetosphere structure.

    Phase C4: rotated to face the actual Sun direction via
    rotate_to_sunward(). magnetic_tilt_deg=60 applies an additional
    rotation about the X axis (bow-shock-to-tail) to model Uranus's
    60-degree dipole-vs-rotation-axis offset.

    Note: source had no info marker (pre-existing omission, same
    pattern as Mars C1 item 14). C4 adds one via create_info_marker(),
    positioned at the first point of the rendered geometry (matching
    the radiation-belts and ring-system pattern in this module).

    Module updated: May 2026 with Anthropic's Claude Opus 4.7
    """
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
    
    # Create magnetosphere main shape (generated with -X as sunward)
    x, y, z = create_magnetosphere_shape(params)

    x = np.array(x)
    y = np.array(y)
    z = np.array(z)

    # Phase C4: rotate to face actual Sun direction, with magnetic tilt
    # (X-axis rotation about the bow-shock-to-tail axis; see Section 3.1
    # for physics rationale)
    x, y, z = rotate_to_sunward(
        x, y, z,
        center_position=center_position,
        sun_position=sun_position,
        magnetic_tilt_deg=60,
    )

    # Apply center offset to rotated geometry
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z

    trace_name = 'Uranus: Magnetosphere'

    description = (
        "Uranus's Magnetosphere: tilted 60 degrees from the rotation axis -- <br>"
        "itself tilted 97.77 degrees from the orbital plane. This produces a <br>"
        "magnetosphere geometry with no analog in the rest of the solar system: <br>"
        "the dipole axis sweeps a wide cone as Uranus rotates, modulating the <br>"
        "magnetosphere's solar-wind interaction on a ~17-hour cycle.<br><br>"
        "Source: Ness et al. (1986) Science -- Voyager 2 magnetometer."
    )

    geom_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(
            size=2.0,
            color='rgb(200, 200, 255)',
            opacity=0.3
        ),
        name=trace_name,
        legendgroup=trace_name,
        hoverinfo='skip',
        showlegend=True,
    )

    # Phase C4: add info marker at first point of rendered geometry
    # (pre-existing omission in source). Matches the source's
    # radiation-belt and ring-system info marker pattern.
    info_trace = create_info_marker(
        x[0], y[0], z[0],
        'rgb(200, 200, 255)', f"{trace_name}<br><br>{description}", trace_name
    )

    return [geom_trace, info_trace]

# Source: Ness et al. (1986) Science -- Voyager 2 magnetometer; 3-10 R_U belt extent; 59-deg magnetic tilt
uranus_radiation_belts_info = (
            "560 KB PER FRAME FOR HTML.<br><br>"
            "Zones of trapped high-energy particles in uranus's magnetosphere"                     
)

def create_uranus_radiation_belts(center_position=(0, 0, 0)):
    """Creates Uranus's radiation belts."""
    # Source: NASA Voyager 2 Uranus Science Summary; Ness et al. (1986) Science -- 3-10 R_U extent,
    # asymmetry from 59-deg magnetic tilt, Voyager 2 (1986) sole in-situ measurement
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
        
        # Phase C4: Apply axial tilt (rotate around x-axis).
        # Dead code stripped: pre-tilt offset, no-op recast, dead Y-axis rotation.
        # The post-tilt offset at the end is the correct application.
        belt_x = np.array(belt_x)
        belt_y = np.array(belt_y)
        belt_z = np.array(belt_z)
        belt_x_tilted, belt_y_tilted, belt_z_tilted = rotate_points(belt_x, belt_y, belt_z, uranus_tilt, 'x')

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
                legendgroup=belt_names[i],
                hoverinfo='skip',
                showlegend=True
            )
        )
        traces.append(create_info_marker(
            belt_x_final[0], belt_y_final[0], belt_z_final[0],
            belt_colors[i], f"{belt_names[i]}<br><br>{belt_texts[i]}", belt_names[i]
        ))

    return traces
    
# Source: Elliot et al. (1977) Nature -- Uranus rings discovery; Voyager 2 (1986) confirmed 13 rings; de Pater et al. (2006)
uranus_ring_system_info = (
                "22.2 MB PER FRAME FOR HTML.<br><br>"

                "Uranus has a system of 13 known rings. These rings are generally very narrow, dark (reflecting very little light, <br>" 
                "similar to charcoal), and composed of dust and larger particles that are icy and darkened by rock. The rings are <br>" 
                "grouped into two main systems:<br>" 
                "* Inner Rings: Nine narrow, dark rings.<br>" 
                "* Outer Rings: Two more distant rings, one of which is bluish and the other reddish.<br>" 
                "While the main rings of Uranus are narrow bands, there are also broader, more diffuse rings made of dust. These <br>" 
                "dusty rings could be considered to have a more toroidal (donut-like) distribution of material compared to the thin, <br>" 
                "distinct main rings. For example, the outermost rings (Nu and Mu) are quite broad and dusty.<br>" 
                "* There are nine main, narrow rings. These rings are relatively dense and have well-defined edges. They are composed <br>" 
                "  mostly of larger, darker particles, often described as being the color of charcoal. Examples of the main rings include <br>" 
                "  the Epsilon, Delta, Gamma, Eta, Beta, Alpha, and the numbered rings 4, 5, and 6. The Epsilon ring is the outermost and <br>" 
                "  widest of the main rings.<br>" 
                "* There are two outer rings: the Nu ring and the Mu ring. These rings are much fainter and more diffuse than the main <br>" 
                "  rings. They are composed of fine dust particles. The Mu ring is quite broad and has a more torus-like distribution of <br>" 
                "  material. It also has a distinct blue color, similar to Saturn's E ring. The Nu ring is reddish in color, similar to <br>" 
                "  dusty rings seen elsewhere in the solar system.<br>" 
                "* Composition: The main rings are primarily larger, dark particles, while the outer rings are predominantly fine dust.<br>" 
                "* Structure: The main rings are narrow and well-defined, whereas the outer rings are broad and diffuse, with the Mu <br>" 
                "  ring exhibiting a clear torus-like structure.<br>" 
                "* Origin and Evolution: The origins and the processes that shape these different sets of rings might vary. The dusty <br>" 
                "  outer rings are likely fed by dust kicked off Uranus' inner moons by micrometeoroid impacts.<br>" 
                "* Visual Characteristics: The main rings are dark and difficult to see, requiring specific observation techniques. The <br>" 
                "  outer rings are even fainter, with the Mu ring having a unique blue color.<br>" 
                "In summary, while all are part of Uranus' ring system, the significant differences in their composition, structure, and <br>" 
                "likely origin make it accurate and informative to distinguish between the narrow, dark main rings and the broad, dusty, <br>" 
                "and torus-like outer rings."                                           
)

# Source: Elliot et al. (1977) Nature -- ring discovery; Voyager 2 (1986) confirmed 13 rings;
# de Pater et al. (2006) Science -- ring properties, widths, colors; Showalter & Lissauer (2006)
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

        # Source: Elliot et al. (1977) Nature; Voyager 2 (1986); de Pater et al. (2006) Science
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

         # Source: Elliot et al. (1977) Nature; de Pater et al. (2006) Science -- ring widths, opacity, colors
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
        x, y, z = create_ring_points(inner_radius_au, outer_radius_au, n_points, thickness_au)
        
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
                legendgroup=f"Uranus: {ring_info['name']}",
                hoverinfo='skip',
                showlegend=True
            )
        )
        mx_t, my_t, mz_t = rotate_points([outer_radius_au], [0.0], [0.0], uranus_tilt, 'x')
        mx_t2, my_t2, mz_t2 = rotate_points(mx_t, my_t, mz_t, uranus_tilt, 'y')
        traces.append(create_info_marker(
            mx_t2[0] + center_x, my_t2[0] + center_y, mz_t2[0] + center_z,
            ring_info['color'], f"Uranus: {ring_info['name']}<br><br>{ring_info['description']}",
            f"Uranus: {ring_info['name']}"
        ))
    
    return traces

# Source: NASA Uranus Fact Sheet (nssdc.gsfc.nasa.gov); Hill sphere radius ~47 AU from planetary mass ratio
uranus_hill_sphere_info = (
            "SELECT MANUAL SCALE OF AT LEAST 0.6 AU TO VISUALIZE.<br>" 
            "1.3 MB PER FRAME FOR HTML.<br><br>"

            "The Hill sphere (also known as the Roche sphere) represents the region around a celestial body where its own gravity <br>" 
            "is the dominant force attracting satellites. Uranus has a Hill radius around 7.02x10^7 km, which corresponds to about <br>" 
            "2 770 Uranus radii (mean radius ~25 360 km). This means that any moon or other object orbiting Uranus within this <br>" 
            "sphere is primarily gravitationally bound to the planet. The major moons and rings of Uranus lie well within its Hill <br>" 
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
    x, y, z = create_sphere_points(layer_radius, n_points=20)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    r_info = layer_radius * 1.05
    trace_name = f"Uranus: {layer_info['name']}"

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
        marker=dict(size=6, color=layer_info['color'], opacity=0.9,
                    symbol='cross', line=dict(color='white', width=1)),
        name='',
        legendgroup=trace_name,
        text=[f"{trace_name}<br><br>{layer_info['description']}"],
        customdata=[trace_name],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    )

    traces = [shell_trace, info_trace]

    return traces