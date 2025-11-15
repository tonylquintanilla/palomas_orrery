import numpy as np
import math
import plotly.graph_objs as go
from shared_utilities import create_sun_direction_indicator
from planet_visualization_utilities import (MERCURY_RADIUS_AU, KM_PER_AU, create_sphere_points, create_magnetosphere_shape)


# Mercury Shell Creation Functions

mercury_inner_core_info = (
            "Inner Core: Mercury has a very large metallic core, unlike Earth's which is proportionally smaller.\n" 
            "Evidence suggests that Mercury has a solid inner core, similar to Earth's. It is estimated to be about \n" 
            "1,000 kilometers thick based on Messenger findings (2019)."
)

def create_mercury_inner_core_shell(center_position=(0, 0, 0)):
    """Creates Mercury's inner core shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 0.41,  # Inner core: 0-52% of Mercury's radius
        'color': 'rgb(255, 180, 140)',  # Orange-red for hot iron core
        'opacity': 1.0,
        'name': 'Inner Core',
        'description': (
            "Inner Core: Mercury has a very large metallic core, unlike Earth's which is proportionally smaller.<br>" 
            "Evidence suggests that Mercury has a solid inner core, similar to Earth's. It is estimated to be about <br>" 
            "1,000 kilometers thick based on Messenger findings (2019)."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * MERCURY_RADIUS_AU
    
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
            name=f"Mercury: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Mercury: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

mercury_outer_core_info = (
            "Outer Core: Surrounding the solid inner core is a liquid metallic outer core. The movement of this molten iron \n" 
            "is thought to be the source of Mercury's weak magnetic field. About 1074 km thick."
)

def create_mercury_outer_core_shell(center_position=(0, 0, 0)):
    """Creates Mercury's outer core shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 0.85,  # Outer core: 82-85% of Mercury's radius
        'color': 'rgb(255, 140, 0)',  # Deeper orange for liquid metal
        'opacity': 0.8,
        'name': 'Outer Core',
        'description': (
            "Outer Core: Surrounding the solid inner core is a liquid metallic outer core. The movement of this molten iron <br>" 
            "is thought to be the source of Mercury's weak magnetic field. About 1074 km thick."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * MERCURY_RADIUS_AU
    
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
            name=f"Mercury: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Mercury: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

mercury_mantle_info = (
            "Mantle: Surrounding the core is a rocky mantle. Recent research suggests this mantle might even contain a layer of \n" 
            "diamonds, formed from ancient carbon-rich material under immense pressure. The mantle is significantly thinner than \n" 
            "Earth's, estimated to be only about 331 kilometers thick."
)

def create_mercury_mantle_shell(center_position=(0, 0, 0)):
    """Creates Mercury's mantle shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 0.98,  # Lower mantle: 85-98% of Earth's radius
        'color': 'rgb(230, 100, 20)',  # Reddish-brown
        'opacity': 0.7,
        'name': 'Mantle',
        'description': (
            "Mantle: Surrounding the core is a rocky mantle. Recent research suggests this mantle might even contain a layer of <br>" 
            "diamonds, formed from ancient carbon-rich material under immense pressure. The mantle is significantly thinner than <br>" 
            "Earth's, estimated to be only about 331 kilometers thick."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * MERCURY_RADIUS_AU
    
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
            name=f"Mercury: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Mercury: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

mercury_crust_info = (
            "SET MANUAL SCALE TO AT LEAST 0.002 AU TO VISUALIZE.\n\n"     
            "Mercury has a solid silicate crust that is heavily cratered, resembling Earth's Moon. The crust is likely quite thin \n" 
            "compared to Earth's. There's also a theory that a significant portion of Mercury's crust might be made of diamonds, \n" 
            "formed by billions of years of meteorite impacts on a graphite-rich surface. About 35 km thick."
)

def create_mercury_crust_shell(center_position=(0, 0, 0)):

    """Creates Mercury's crust shell using Mesh3d for better performance with improved hover."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 1.0,  # Crust: 100% of Mercury's radius
        'color': 'rgb(128, 128, 128)',   # Description: Dark Gray reflecting Mercury's rocky and heavily cratered surface.
        'opacity': 1.0,
        'name': 'Crust',
        'description': (
            "(Note: toggle off the crust layer in the legend to better see the interior structure.)<br><br>"
            "Mercury has a solid silicate crust that is heavily cratered, resembling Earth's Moon. The crust is likely quite thin <br>" 
            "compared to Earth's. There's also a theory that a significant portion of Mercury's crust might be made of diamonds, <br>" 
            "formed by billions of years of meteorite impacts on a graphite-rich surface. About 35 km thick."
        )
    }
    
    # Calculate radius in AU
    radius = layer_info['radius_fraction'] * MERCURY_RADIUS_AU
    
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
        name=f"Mercury: {layer_info['name']}",
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
    layer_name = f"Mercury: {layer_info['name']}"
    minimal_hover_texts = [layer_name] * len(x_hover)

    # Create hover trace with direct text assignment
    hover_trace = go.Scatter3d(
        x=x_hover, 
        y=y_hover, 
        z=z_hover,
        mode='markers',
        marker=dict(
            size=2,  # originally 5
            color='rgb(128, 128, 128)',   # Description: Dark Gray reflecting Mercury's rocky and heavily cratered surface.
            opacity=1.0,  # originally 0.8
            line=dict(  # Add a contrasting outline
                width=1,
                color='black'
            )
        ),
        name=f"Mercury: {layer_info['name']} (Info)",
        text=hover_texts,  # IMPORTANT: Matching length with coordinate arrays
        customdata=minimal_hover_texts,  # For "Object Names Only" mode
        hovertemplate='%{text}<extra></extra>',  # Use the standard hover template
        showlegend=False  # Don't show in legend since it's just for hover
    )

    return [surface_trace, hover_trace]

mercury_atmosphere_info = (
            "SET MANUAL SCALE TO AT LEAST 0.002 AU TO VISUALIZE.\n\n"     
            "Exosphere: Unlike Earth's substantial atmosphere, Mercury has an extremely thin exosphere. This exosphere is not \n" 
            "dense enough to trap heat or offer significant protection from space. It is composed mostly of oxygen, sodium, \n" 
            "hydrogen, helium, and potassium atoms that have been blasted off the surface by the solar wind and micrometeoroid impacts."
)

def create_mercury_atmosphere_shell(center_position=(0, 0, 0)):
    """Creates Mercury's atmosphere shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 2.0,  # Exosphere
        'color': 'rgb(150, 200, 255)',  # Light blue for atmosphere
        'opacity': 0.5,
        'name': 'Exosphere',
        'description': (
            "Exosphere: Unlike Earth's substantial atmosphere, Mercury has an extremely thin exosphere. This exosphere is not <br>" 
            "dense enough to trap heat or offer significant protection from space. It is composed mostly of oxygen, sodium, <br>" 
            "hydrogen, helium, and potassium atoms that have been blasted off the surface by the solar wind and micrometeoroid impacts.<br><br>"
            "Mercury has what is more accurately described as a tenuous exosphere rather than a substantial atmosphere like Earth's. <br>" 
            "This exosphere is extremely thin, and its atoms are so sparse they are more likely to collide with the surface than with <br>" 
            "each other. The extent of Mercury's exosphere is not well-defined by a pressure gradient as with a true atmosphere. Instead, <br>" 
            "it gradually fades out into space. However, we can consider how far certain exospheric components have been observed:<br>" 
            "* Sodium Tail: Due to solar radiation pressure, sodium atoms are pushed away from Mercury, forming a long, comet-like tail. <br>" 
            "  This tail has been detected extending to distances of over 24 million kilometers (approximately 10,000 Mercury radii) <br>" 
            "  from the planet. This is by far the most extended component of Mercury's exosphere.<br>" 
            "* Other Elements: Other elements like hydrogen, helium, oxygen, potassium, calcium, and magnesium are also present in the <br>" 
            "  exosphere. These are generally found much closer to the planet's surface, within a few Mercury radii. For instance, calcium <br>" 
            "  and magnesium have been observed in the tail but at distances less than 8 Mercury radii.<br>" 
            "In summary: While the bulk of Mercury's exospheric atoms are concentrated very close to the surface (within 1 Mercury radius), <br>" 
            "the sodium tail is a significant feature that extends incredibly far, up to 10,000 Mercury radii. The main body of the exosphere <br>" 
            "is very close to the surface, but the tenuous sodium tail stretches to an immense distance."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * MERCURY_RADIUS_AU
    
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
            name=f"Mercury: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Mercury: {layer_info['name']}"] * len(x),
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


mercury_sodium_tail_info = (
            "TO VISUALIZE CLOSE UP SET MANUAL SCALE TO AT LEAST 0.002 AU TO VISUALIZE.\n"
            "TO VISUALIZE THE COMPLETE TAIL INCLUDE VENUS IN THE PLOT OR SET MANUAL SCALE TO 1.0 AU\n\n" 

            "Sodium Tail: Mercury has a remarkable sodium tail that extends incredibly far into space - up to 10,000 Mercury radii \n"
            "(approximately 24 million kilometers or 2.4 million km). This tail is created when sodium atoms from Mercury's exosphere \n"
            "are pushed away by solar radiation pressure. The tail always points away from the Sun, similar to a comet's tail.\n\n"
            "The sodium tail is highly dynamic and can vary significantly based on Mercury's position in its orbit and solar activity. \n"
            "It's one of Mercury's most distinctive features and can be observed from Earth using specialized telescopes."
)

def create_mercury_sodium_tail(center_position=(0, 0, 0)):
    """Creates Mercury's sodium tail visualization extending away from the Sun."""
    
    # Define layer properties
    layer_info = {
        'name': 'Sodium Tail',
        'description': (
            "Sodium Tail: Mercury has a remarkable sodium tail that extends incredibly far into space - up to 10,000 Mercury radii <br>"
            "(approximately 24 million kilometers or 2.4 million km). This tail is created when sodium atoms from Mercury's exosphere <br>"
            "are pushed away by solar radiation pressure. The tail always points away from the Sun, similar to a comet's tail.<br><br>"
            "The sodium tail is highly dynamic and can vary significantly based on Mercury's position in its orbit and solar activity. <br>"
            "It's one of Mercury's most distinctive features and can be observed from Earth using specialized telescopes."
        )
    }
    
    # Sodium tail extends up to ~10,000 Mercury radii away from the Sun
    max_tail_length = 10000 * MERCURY_RADIUS_AU
    
    # Create a conical tail shape pointing away from the Sun
    # Sun is at origin (0,0,0), so tail points away from (0,0,0) relative to Mercury's position
    center_x, center_y, center_z = center_position
    
    # Calculate direction away from Sun (normalized)
    distance = math.sqrt(center_x**2 + center_y**2 + center_z**2)
    if distance > 0:
        dir_x = center_x / distance
        dir_y = center_y / distance
        dir_z = center_z / distance
    else:
        # If Mercury is at origin, default to +x direction
        dir_x, dir_y, dir_z = 1, 0, 0
    
    # Create tail as a cone of particles with varying density
    num_particles = 500
    tail_points_x = []
    tail_points_y = []
    tail_points_z = []
    
    for i in range(num_particles):
        # Distance along tail (0 to max_tail_length)
        tail_distance = (i / num_particles) * max_tail_length
        
        # Cone widens as it extends (opening angle ~5-10 degrees)
        max_radius = tail_distance * math.tan(math.radians(7))
        
        # Random position within cone cross-section
        theta = np.random.uniform(0, 2 * math.pi)
        r = np.random.uniform(0, max_radius)
        
        # Create perpendicular vectors to tail direction
        if abs(dir_z) < 0.9:
            perp1_x = -dir_y
            perp1_y = dir_x
            perp1_z = 0
        else:
            perp1_x = 1
            perp1_y = 0
            perp1_z = -dir_x / dir_z if dir_z != 0 else 0
        
        # Normalize perp1
        perp1_len = math.sqrt(perp1_x**2 + perp1_y**2 + perp1_z**2)
        if perp1_len > 0:
            perp1_x /= perp1_len
            perp1_y /= perp1_len
            perp1_z /= perp1_len
        
        # Cross product for second perpendicular
        perp2_x = dir_y * perp1_z - dir_z * perp1_y
        perp2_y = dir_z * perp1_x - dir_x * perp1_z
        perp2_z = dir_x * perp1_y - dir_y * perp1_x
        
        # Position in tail
        x = center_x + tail_distance * dir_x + r * (math.cos(theta) * perp1_x + math.sin(theta) * perp2_x)
        y = center_y + tail_distance * dir_y + r * (math.cos(theta) * perp1_y + math.sin(theta) * perp2_y)
        z = center_z + tail_distance * dir_z + r * (math.cos(theta) * perp1_z + math.sin(theta) * perp2_z)
        
        tail_points_x.append(x)
        tail_points_y.append(y)
        tail_points_z.append(z)
    
    # Create color gradient with alpha channel for fading effect
    # RGBA colors where alpha decreases with distance
    colors = []
    for i in range(num_particles):
        alpha = 0.6 * (1 - i/num_particles)**2  # Fades with distance
        # Ensure alpha is at least 0.001 to avoid scientific notation issues
        alpha = max(alpha, 0.001)
        colors.append(f'rgba(255, 200, 100, {alpha:.3f})')
    
    traces = [
        go.Scatter3d(
            x=tail_points_x,
            y=tail_points_y,
            z=tail_points_z,
            mode='markers',
            marker=dict(
                size=2.5,
                color=colors,  # Use RGBA colors for per-point opacity
            ),
            name=f"Mercury: {layer_info['name']}",
            text=[layer_info['description']] * len(tail_points_x),
            customdata=[f"Mercury: {layer_info['name']}"] * len(tail_points_x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

mercury_magnetosphere_info = (
            "SET MANUAL SCALE TO AT LEAST 0.002 AU TO VISUALIZE.\n\n" 

            "Magnetosphere: Mercury has a surprisingly active magnetosphere, given its small size and slow rotation. However, it is \n" 
            "significantly weaker and smaller than Earth's magnetosphere."
)

def create_mercury_magnetosphere_shell(center_position=(0, 0, 0)):
    """Creates Mercury's magnetosphere."""
    traces = []
    
    # Parameters for magnetosphere components (in Mercury radii)
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
    #    'inner_belt_distance': 1.5,  # Distance in Earth radii
    #    'outer_belt_distance': 4.5,  # Distance in Earth radii
    #    'belt_thickness': 0.5,
    }
    
    # Scale everything by Earth's radius in AU
    for key in params:
        params[key] *= MERCURY_RADIUS_AU
    
    # Create magnetosphere main shape
    x, y, z = create_magnetosphere_shape(params)
    
    # Unpack center position
    center_x, center_y, center_z = center_position
    
    # 1. Add the main magnetosphere structure
    x = np.array(x) + center_x
    y = np.array(y) + center_y
    z = np.array(z) + center_z
    
    magnetosphere_text = ["Magnetosphere: Mercury has a surprisingly active magnetosphere, given its small size and slow rotation. <br>" 
                          "However, it is significantly weaker and smaller than Earth's magnetosphere.<br>" 
                          "* Intrinsic Magnetic Field: Mercury generates an internal magnetic field, likely due to dynamo action in <br>" 
                          "  its partially liquid outer core. This was a significant discovery by Mariner 10 in the 1970s and has been <br>" 
                          "  further studied by the MESSENGER and BepiColombo missions.<br>" 
                          "* Interaction with the Solar Wind: This weak magnetic field is still strong enough to deflect the solar wind, <br>" 
                          "  creating a small magnetosphere around the planet. This magnetosphere has features similar to Earth's, including <br>" 
                          "  a bow shock, magnetopause, and magnetotail.<br>" 
                          "  Dynamic and Leaky: Due to its proximity to the Sun, Mercury's magnetosphere experiences a much stronger and more <br>" 
                          "  dynamic solar wind than Earth. This interaction can lead to magnetic reconnection events and a \"leakier\" <br>" 
                          "  magnetosphere, allowing more solar wind particles to reach the planet's surface and contribute to its exosphere.<br>" 
                          "* No Stable Radiation Belts: Unlike Earth's Van Allen radiation belts, Mercury's small and dynamic magnetosphere <br>" 
                          "  doesn't have stable regions for trapping high-energy particles for extended periods.<br><br>" 
                          "Estimating the dimensions of Mercury's magnetosphere in terms of Mercury radii (≈2440 km) involves <br>" 
                          "considering its interaction with the solar wind, which is quite dynamic. However, based on observations <br>" 
                          "from the MESSENGER and BepiColombo missions, we can provide some approximate ranges and typical values:<br>" 
                          "* Sunward Distance (to the Bow Shock): The bow shock is the outermost boundary where the supersonic solar <br>" 
                          "  wind is slowed and heated as it encounters Mercury's magnetosphere. This distance is highly variable <br>" 
                          "  depending on the solar wind conditions, but a typical sunward distance to the bow shock is estimated to be <br>" 
                          "  around 1.4 to 2.0 radii from the center of Mercury.<br>" 
                          "* Equatorial Radius (of the Magnetopause): The magnetopause is the boundary where Mercury's magnetic field <br>" 
                          "  pressure balances the solar wind pressure. In the equatorial plane (perpendicular to the magnetic poles), the <br>" 
                          "  magnetopause typically extends to about 1.1 to 1.5 radii from the center of Mercury. This is quite compressed <br>" 
                          "  due to the relatively weak magnetic field and strong solar wind pressure at Mercury's orbit.<br>" 
                          "* Polar Radius (of the Magnetopause): Along Mercury's magnetic poles, the magnetopause is closer to the planet than <br>" 
                          "  at the equator due to the field line geometry. Estimates for the distance to the magnetopause at the poles range <br>" 
                          "  from about 0.8 to 1.2 radii from the center. In some models, it can be very close to the surface.<br>" 
                          "* Tail Length (Magnetotail): The magnetotail is the region downstream of the planet, stretched out by the solar wind.<br>" 
                          "  Mercury's magnetotail is relatively short and dynamic compared to Earth's. Estimates for its typical length vary, <br>" 
                          "  but it's often considered to extend to around 10 to 30 radii downwind. However, it can be significantly longer or <br>" 
                          "  shorter depending on solar wind conditions and magnetic reconnection events.<br>" 
                          "* Tail Base Radius: The base of the magnetotail is the region just behind the planet where the magnetopause starts to <br>" 
                          "  be significantly stretched. The radius of this tail base in the equatorial plane is roughly comparable to the equatorial <br>" 
                          "  radius of the magnetopause, so we can estimate it to be around 1.1 to 1.5 radii.<br>" 
                          "* Tail End Radius: The \"end\" of Mercury's magnetotail isn't a sharply defined boundary. As the tail extends downwind, <br>" 
                          "  it gradually widens and becomes more turbulent, eventually merging with the interplanetary magnetic field. At the <br>" 
                          "  estimated lengths of 10 to 30 radii, the radius of the tail is expected to be larger than at the base, likely in the range <br>" 
                          "  of 2 to 5 radii, but this is highly variable and less well-defined."]
    
    magnetosphere_customdata = ['Mercury: Magnetosphere']

    traces.append(
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=2.0,
                color='rgb(180, 180, 255)', # Light blue for magnetic field
                opacity=0.2
            ),
            name='Mercury: Magnetosphere',
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
    bow_shock_standoff = 15 * MERCURY_RADIUS_AU
    bow_shock_width = 25 * MERCURY_RADIUS_AU
    
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
    
    bow_shock_text = ["Bow Shock: The bow shock is the outermost boundary where the supersonic solar wind is slowed and heated as <br>" 
                      "it encounters Mercury's magnetosphere. This distance is highly variable depending on the solar wind conditions, <br>" 
                      "but a typical sunward distance to the bow shock is estimated to be around 1.4 to 2.0 radii from the center of Mercury.<br>"
                      "The Bow Shock points towards the Sun along the X-axis. The XY plane is the ecliptic."]
    
    bow_shock_customdata = ['Mercury: Bow Shock']

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
            name='Mercury: Bow Shock',
            text=bow_shock_text * len(bow_shock_x),
            customdata=bow_shock_customdata * len(bow_shock_x),  # This was the line causing the error
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    )
        
    sun_traces = create_sun_direction_indicator(
        center_position=center_position, 
        shell_radius=100 * MERCURY_RADIUS_AU
    )
    for trace in sun_traces:
        traces.append(trace)

    return traces

mercury_hill_sphere_info = (
            "SET MANUAL SCALE TO AT LEAST 0.003 AU TO VISUALIZE.\n\n" 
            "Hill Sphere: Every celestial body has a Hill sphere (also known as the Roche sphere), which is the region around it \n" 
            "where its gravity is the dominant gravitational force. Mercury certainly has a Hill sphere, but its size depends on \n" 
            "its mass and its distance from the Sun. Being the closest planet to the Sun, the Sun's powerful gravity limits the \n" 
            "extent of Mercury's Hill sphere compared to planets farther out."
)

def create_mercury_hill_sphere_shell(center_position=(0, 0, 0)):
    """Creates Mercury's Hill sphere."""
    # Hill sphere radius in Mercury radii
    radius_fraction = 94.4  # Mercury's Hill sphere is about 90 Mercury radii
    
    # Calculate radius in AU
    radius_au = radius_fraction * MERCURY_RADIUS_AU
    
    # Create sphere points with fewer points for memory efficiency
    n_points = 30  # Reduced for large spheres
    x, y, z = create_sphere_points(radius_au, n_points=n_points)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    # Create hover text
    hover_text = ("Hill Sphere: Every celestial body has a Hill sphere (also known as the Roche sphere), which is the region around it <br>" 
                "where its gravity is the dominant gravitational force. Mercury certainly has a Hill sphere, but its size depends on <br>" 
                "its mass and its distance from the Sun. Being the closest planet to the Sun, the Sun's powerful gravity limits the <br>" 
                "extent of Mercury's Hill sphere compared to planets farther out.<br><br>" 
                "The Hill sphere is the region around a where its own gravity is the dominant force in attracting satellites. For <br>" 
                "a planet orbiting a star, it's the region where the planet's gravity is stronger than the star's tidal forces.<br><br>" 
                "The Hill Sphere radius can be described in words as follows: it is equal to the planet's average distance from the <br>" 
                "Sun (its orbital semi-major axis) multiplied by the cube root of the ratio between the planet's mass and three times <br>" 
                "the Sun's mass. In other words, you take how far the planet orbits out from the Sun, then scale that distance by the <br>" 
                "cube root of (planet mass ÷ [3 x solar mass]) to find the boundary within which the planet's gravity dominates over the Sun's.")
    
    hover_customdata = ["Hill Sphere"]

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
            name='Mercury: Hill Sphere',
            text=[hover_text] * len(x),
            customdata=['Mercury: Hill Sphere'] * len(x),
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