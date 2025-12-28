import numpy as np
import math
import plotly.graph_objs as go
from planet_visualization_utilities import (NEPTUNE_RADIUS_AU, KM_PER_AU, create_sphere_points, rotate_points)
from saturn_visualization_shells import create_ring_points_saturn
from shared_utilities import create_sun_direction_indicator

# Neptune Shell Creation Functions

neptune_core_info = (
            "2.4 MB PER FRAME FOR HTML.\n\n"
            "Neptune core: At Neptune's center lies a relatively small, rocky core composed primarily of iron, nickel, and silicates. \n" 
            "Its mass is estimated to be about 1.2 times that of Earth. The pressure at the core is immense, reaching about 7 million \n" 
            "bars (700 GPa), and the temperature could be as high as 5,100  degC."
)

def create_neptune_core_shell(center_position=(0, 0, 0)):
    """Creates Neptune's core shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 0.25,  # Approximately 25% of Neptune's radius
        'color': 'rgb(255, 215, 0)',  # estimated black body color at about 5100 degC 
        'opacity': 1.0,
        'name': 'Core',
        'description': (
            "Neptune core: At Neptune's center lies a relatively small, rocky core composed primarily of iron, nickel, and silicates. <br>" 
            "Its mass is estimated to be about 1.2 times that of Earth. The pressure at the core is immense, reaching about 7 million <br>" 
            "bars (700 GPa), and the temperature could be as high as 5,100  degC.<br>" 
            "* While there isn't a single, precisely agreed-upon value for Neptune's core radius, estimates suggest that the rocky <br>" 
            "  core makes up a relatively small fraction of the planet's total radius."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * NEPTUNE_RADIUS_AU
    
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
            name=f"Neptune: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Neptune: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

neptune_mantle_info = (
            "2.1 MB PER FRAME FOR HTML.\n\n"
            "Mantle: Surrounding the core is a dense mantle made up of a hot, highly compressed fluid of water, methane, and ammonia. \n " 
            "This layer constitutes the majority of Neptune's mass, about 10 to 15 Earth masses. The high pressure and temperature create \n" 
            "an environment where these \"icy\" materials exist in exotic phases, possibly including ionic water and superionic water. \n" 
            "Some theories suggest that at great depths within the mantle, methane may decompose, forming diamond crystals that could \n" 
            "\"rain\" downwards."
)

def create_neptune_mantle_shell(center_position=(0, 0, 0)):
    """Creates Neptune's mantle shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 0.85,  # Up to about 85% of neptune's radius
        'color': 'rgb(255, 138, 18)',  # estimated black body color at about 2,000 K
        'opacity': 0.9,
        'name': 'mantle',
        'description': (
            "mantle: Surrounding the core is a dense mantle made up of a hot, highly compressed fluid of water, methane, and ammonia. <br> " 
            "This layer constitutes the majority of Neptune's mass, about 10 to 15 Earth masses. The high pressure and temperature create <br>" 
            "an environment where these \"icy\" materials exist in exotic phases, possibly including ionic water and superionic water. <br>" 
            "Some theories suggest that at great depths within the mantle, methane may decompose, forming diamond crystals that could <br>" 
            "\"rain\" downwards.<br>" 
            "* The mantle makes up a significant portion of the remaining interior. Models suggest it could extend out to approximately <br>" 
            "  80-85% of Neptune's total radius.<br>" 
            "* It's important to remember that this is still an estimate based on our current understanding of Neptune's interior. <br>" 
            "  The transition from the dense fluid mantle to the gaseous atmosphere is likely a gradual one.<br>" 
            "* The temperature within Neptune's mantle is incredibly high, ranging from approximately 2,000 K (around 1,700  degC) to <br>" 
            "  5,000 K (around 4,700  degC). It's important to understand that Neptune's mantle isn't a solid, icy layer like the name <br>" 
            "  \"ice giant\" might suggest. Instead, it's a hot, dense fluid composed primarily of water, methane, and ammonia under <br>" 
            "  immense pressure. This high pressure actually raises the freezing point of these substances significantly. So, even at <br>" 
            "  these high temperatures, they can exist in a fluid or even superionic state."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * NEPTUNE_RADIUS_AU
    
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
            name=f"Neptune: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Neptune: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

neptune_cloud_layer_info = (
            "USE MANUAL SCALED OF 0.005 AU TO VIEW CLOSELY."
            "4.6 MB PER FRAME FOR HTML.\n\n"
            "Atmosphere: Neptune's atmosphere is primarily composed of hydrogen (around 80%) and helium (around 19%), with a small \n" 
            "amount of methane (about 1.5%). It's the methane that absorbs red light and reflects blue light, giving Neptune its \n" 
            "characteristic vivid blue color. The atmosphere extends to great depths, gradually merging into the fluid mantle below.\n" 
            "* Cloud Layer: Within the troposphere, the lowest layer of the atmosphere, various cloud layers exist at different \n" 
            "  altitudes. The highest clouds are thought to be composed of methane ice. Below that, there may be clouds of ammonia \n" 
            "  and hydrogen sulfide, followed by ammonium sulfide and water ice clouds at even deeper levels. These clouds are often \n" 
            "  swept around the planet by incredibly strong winds, the fastest in the Solar System, reaching up to 2,100 kilometers \n" 
            "  per hour. Recent observations have shown surprising changes in Neptune's cloud cover, with a significant decrease in \n" 
            "  cloudiness possibly linked to the solar cycle."
)

def create_neptune_cloud_layer_shell(center_position=(0, 0, 0)):
    """Creates neptune's cloud layer shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 1.0,  # the top of the troposphere is actually 1.002
        'color': 'rgb(0, 128, 255)',  # optical
        'opacity': 1.0,
        'name': 'Cloud Layer',
        'description': (
            "Neptune Cloud Layer<br>" 
            "(Note: toggle off the cloud layer in the legend to better see the interior structure.)<br><br>"
            "Atmosphere: Neptune's atmosphere is primarily composed of hydrogen (around 80%) and helium (around 19%), with a small <br>" 
            "amount of methane (about 1.5%). It's the methane that absorbs red light and reflects blue light, giving Neptune its <br>" 
            "characteristic vivid blue color. The atmosphere extends to great depths, gradually merging into the fluid mantle below.<br>" 
            "* Cloud Layer: Within the troposphere, the lowest layer of the atmosphere, various cloud layers exist at different <br>" 
            "  altitudes. The highest clouds are thought to be composed of methane ice. Below that, there may be clouds of ammonia <br>" 
            "  and hydrogen sulfide, followed by ammonium sulfide and water ice clouds at even deeper levels. These clouds are often <br>" 
            "  swept around the planet by incredibly strong winds, the fastest in the Solar System, reaching up to 2,100 kilometers <br>" 
            "  per hour. Recent observations have shown surprising changes in Neptune's cloud cover, with a significant decrease in <br>" 
            "  cloudiness possibly linked to the solar cycle.<br>" 
            "* Based on available information, the troposphere extends to a pressure level of about 0.1 bar (10 kPa). The altitude <br>" 
            "  at which this pressure occurs is estimated to be around 50 to 80 kilometers above the 1-bar pressure level (which is <br>" 
            "  often considered the \"surface\" of gas giants). Therefore, the radius fraction at the top of Neptune's troposphere <br>" 
            "  is approximately 1.002 to 1.003 of Neptune's total radius (using the equatorial radius). In essence, when we talk <br>" 
            "  about the planet's radius, it's a defined level within its atmosphere. The troposphere extends a bit further out.<br>" 
            "* The predominant visual color of Neptune is a distinct blue. This is primarily due to the absorption of red and infrared <br>" 
            "  light by methane in its atmosphere. While the exact shade can vary slightly depending on viewing conditions and image <br>" 
            "  processing, a representative RGB value for Neptune's blue could be approximately: R: 0-63, G: 119-159, B: 135-253"
            )
    }
    
    # Calculate radius in AU
    radius = layer_info['radius_fraction'] * NEPTUNE_RADIUS_AU
    
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
        name=f"Neptune: {layer_info['name']}",
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
    layer_name = f"Neptune: {layer_info['name']}"
    minimal_hover_texts = [layer_name] * len(x_hover)

    # Create hover trace with direct text assignment
    hover_trace = go.Scatter3d(
        x=x_hover, 
        y=y_hover, 
        z=z_hover,
        mode='markers',
        marker=dict(
            size=2,  # originally 5
            color='rgb(0, 128, 255)',  # Layer color, originally 'white'
            opacity=1.0,  # originally 0.8
            line=dict(  # Add a contrasting outline
                width=1,
                color='black'
            )
        ),
        name=f"Neptune: {layer_info['name']} (Info)",
        text=hover_texts,  # IMPORTANT: Matching length with coordinate arrays
        customdata=minimal_hover_texts,  # For "Object Names Only" mode
        hovertemplate='%{text}<extra></extra>',  # Use the standard hover template
        showlegend=False  # Don't show in legend since it's just for hover
    )

    return [surface_trace, hover_trace]

neptune_upper_atmosphere_info = (
            "2.7 MB PER FRAME FOR HTML.\n\n"
            "Upper Atmosphere: Above the troposphere lies the stratosphere, where temperature increases with altitude. Higher still \n" 
            "is the thermosphere, characterized by lower pressures. The outermost layer is the exosphere, which gradually fades into space."
)

def create_neptune_upper_atmosphere_shell(center_position=(0, 0, 0)):
    """Creates Neptune's upper atmosphere shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 1.01,  # more like 1.008 and very approximate.
        'color': 'rgb(240, 245, 250)',  # optical pale blue
        'opacity': 0.5,
        'name': 'Upper Atmosphere',
        'description': (
            "Upper Atmosphere: Above the troposphere lies the stratosphere, where temperature increases with altitude. Higher still <br>" 
            "is the thermosphere, characterized by lower pressures. The outermost layer is the exosphere, which gradually fades into space.<br>" 
            "* No Solid Surface: Neptune is a gas giant, so its \"radius\" is defined at a specific pressure level (usually the 1-bar <br>" 
            "  level). The atmosphere extends far beyond this.<br>" 
            "* Gradual Transition: The thermosphere doesn't have a sharp upper boundary; it gradually fades into the exosphere. The <br>" 
            "  altitude where one ends and the other begins (the thermopause) varies.<br>" 
            "* Dynamic Conditions: The thermosphere's extent is influenced by solar activity and Neptune's magnetic field, causing it to <br>" 
            "  expand and contract.<br>" 
            "* Temperature: The upper atmospheres of Uranus and Neptune are known to be inexplicably hot, suggesting significant <br>" 
            "  energy input that could lead to a more extended thermosphere than expected based solely on solar heating.<br>" 
            "* Estimated Height: The thermosphere on Neptune likely extends a significant distance above the 1-bar radius.<br>" 
            "  * The thermosphere begins at pressures below 10^-^5 to 10^-^4 bars (1 to 10 Pa).<br>" 
            "  * Barometric Formula: We'll use a simplified version of the barometric formula, which relates pressure and altitude in <br>" 
            "    an atmosphere.<br>" 
            "    * The pressure at a certain altitude in an atmosphere is equal to the pressure at a reference altitude multiplied <br>" 
            "      by the natural exponential function raised to the power of the negative of the altitude difference divided by the <br>" 
            "      atmospheric scale height.<br>" 
            "    * This exponential relationship is fundamental to how pressure changes with altitude in an atmosphere.<br>" 
            "    * The negative sign indicates that pressure generally decreases as altitude increases.<br>" 
            "    * The atmospheric scale height is a characteristic distance for a particular atmosphere. It's the vertical distance <br>" 
            "      over which the pressure decreases by a factor of 'e'. It depends on the gravity and temperature of the atmosphere.<br>" 
            "  * The pressure level of 5 Pa is estimated to be at a radius fraction of approximately 1.008 of Neptune's radius (1-bar).<br>" 
            "  * The pressure level of 1 Pa is estimated to be at a radius fraction of approximately 1.0091 of Neptune's radius. This <br>" 
            "    is an estimate using a simplified model. At these very low pressures, the actual temperature profile and thus the scale <br>" 
            "    height can deviate from the average value used, potentially affecting the accuracy of this calculation.<br>" 
            "  * Isothermal Assumption: The simple barometric formula assumes a constant temperature with altitude, which is not entirely <br>" 
            "    accurate for Neptune's atmosphere, especially across different layers. However, it provides a reasonable approximation.<br>" 
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * NEPTUNE_RADIUS_AU
    
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
            name=f"Neptune: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Neptune: {layer_info['name']}"] * len(x),
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

neptune_magnetosphere_info = (
            "SELECT MANUAL SCALE OF AT LEAST 0.2 AU TO VISUALIZE.\n"
            "1.4 MB PER FRAME FOR HTML.\n\n"

            "Magnetosphere: Neptune possesses a significant and unusual magnetosphere. Unlike Earth's magnetic field, which is \n" 
            "roughly aligned with its rotational axis, Neptune's magnetic axis is tilted by about 47 degrees relative to its rotation \n" 
            "axis and offset from the planet's center by a considerable fraction of its radius. This creates a complex and dynamic \n" 
            "magnetic environment. The magnetosphere traps charged particles from the solar wind and accelerates them to high energies."                     
)

# Fixed create_neptune_magnetosphere function
def create_neptune_magnetosphere(center_position=(0, 0, 0)):
    """Creates Neptune's main magnetosphere structure with proper tilt and offset."""
    import numpy as np
    import plotly.graph_objs as go
    from planet_visualization_utilities import NEPTUNE_RADIUS_AU, create_magnetosphere_shape, rotate_points
    
    # Parameters for magnetosphere components (in Neptune radii)
    params = {
        # Compressed sunward side - Neptune's bow shock standoff distance
        'sunward_distance': 34,  # Based on Voyager 2 data, ~34 Neptune radii
        
        # Equatorial extension (wider than polar)
        'equatorial_radius': 40,  # Typical equatorial extension
        'polar_radius': 25,       # Polar extension is smaller
        
        # Magnetotail parameters
        'tail_length': 600,       # Neptune's tail extends far downstream
        'tail_base_radius': 60,   # Radius at the base of the tail, based on modeling
        'tail_end_radius': 120,   # Radius at the end of the tail, based on modeling
    }
    
    # Scale everything by Neptune's radius in AU
    for key in params:
        params[key] *= NEPTUNE_RADIUS_AU
    
    # Create magnetosphere main shape
    x, y, z = create_magnetosphere_shape(params)
    
    # Convert to numpy arrays for efficient rotation
    x = np.array(x)
    y = np.array(y)
    z = np.array(z)
    
    # Apply Neptune's magnetic field offset (0.55 Neptune radii, mostly northward)
    # The offset is applied before rotation to properly represent the field
    offset_distance = 0.55 * NEPTUNE_RADIUS_AU
    
    # Apply the offset primarily in the z-direction (northward)
    # with small components in x and y to match observations
    z = z + (0.5 * offset_distance)  # Major component of offset in z
    x = x + (0.2 * offset_distance)  # Minor component in x
    y = y + (0.1 * offset_distance)  # Minor component in y
    
    # Identify internal vs external magnetosphere regions
    bow_shock_mask = x < 0
    tail_mask = x > params['tail_length'] * 0.4  # Far tail
    internal_mask = ~(bow_shock_mask | tail_mask)
    
    # Store regions separately
    bow_shock_x = x[bow_shock_mask]
    bow_shock_y = y[bow_shock_mask]
    bow_shock_z = z[bow_shock_mask]
    
    tail_x = x[tail_mask]
    tail_y = y[tail_mask]
    tail_z = z[tail_mask]
    
    internal_x = x[internal_mask]
    internal_y = y[internal_mask]
    internal_z = z[internal_mask]
    
    # Apply Neptune's magnetic field rotations to internal magnetosphere only
    # First, tilt around the y-axis to implement the main magnetic axis tilt
    magnetic_tilt = np.radians(47)
    int_x1, int_y1, int_z1 = rotate_points(internal_x, internal_y, internal_z, magnetic_tilt, 'y')
    
    # Second rotation to match the observed orientation (around z-axis)
    azimuthal_angle = np.radians(60)  # Estimated angle based on Voyager data
    int_x2, int_y2, int_z2 = rotate_points(int_x1, int_y1, int_z1, azimuthal_angle, 'z')
    
    # For the tail region, apply a partial rotation to create a smooth transition
    tail_fraction = 0.3  # Partial effect of Neptune's field on tail
    tail_x1, tail_y1, tail_z1 = rotate_points(tail_x, tail_y, tail_z, magnetic_tilt * tail_fraction, 'y')
    tail_x2, tail_y2, tail_z2 = rotate_points(tail_x1, tail_y1, tail_z1, azimuthal_angle * tail_fraction, 'z')
    
    # Recombine the components
    x_final = np.concatenate([bow_shock_x, int_x2, tail_x2])
    y_final = np.concatenate([bow_shock_y, int_y2, tail_y2])
    z_final = np.concatenate([bow_shock_z, int_z2, tail_z2])
    
    # Unpack center position
    center_x, center_y, center_z = center_position
    
    # Apply center position offset to final coordinates
    x_final = x_final + center_x
    y_final = y_final + center_y
    z_final = z_final + center_z
    
    # Detailed description for hover information with explicit sun direction note
    magnetosphere_text = [
        "Neptune's Magnetosphere: Unlike other planets, Neptune's magnetic field is dramatically tilted (47 deg from its rotation axis) and <br>"
        "significantly offset from the planet's center by more than half a Neptune radius. This creates an extremely asymmetric magnetosphere <br>"
        "that varies greatly depending on Neptune's rotation.<br><br>"
        "In this scientifically accurate model:<br>"
        "- The bow shock faces the Sun (negative X-axis) as it would in reality, shaped by the solar wind<br>"
        "- The internal magnetosphere shows Neptune's unique magnetic field configuration with its 47 deg tilt and offset<br>"
        "- The magnetotail stretches away from the Sun but is influenced by Neptune's unusual field<br><br>"
        "This unusual magnetic environment was discovered by Voyager 2 during its 1989 flyby and makes Neptune's magnetosphere <br>"
        "one of the most complex and dynamic in our solar system."
    ] * len(x_final)
    
    magnetosphere_customdata = ['Neptune: Magnetosphere'] * len(x_final)
    
    # Create main magnetosphere trace
    traces = [
        go.Scatter3d(
            x=x_final, y=y_final, z=z_final,
            mode='markers',
            marker=dict(
                size=2.0,
                color='rgb(30, 136, 229)',  # More appropriate blue for Neptune
                opacity=0.3
            ),
            name='Neptune: Magnetosphere',
            text=magnetosphere_text,
            customdata=magnetosphere_customdata,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    sun_traces = create_sun_direction_indicator(
        center_position=center_position, 
        shell_radius=600 * NEPTUNE_RADIUS_AU
    )
    for trace in sun_traces:
        traces.append(trace)
    
    # Add magnetic poles and axis visualization - with error handling
    try:
        mag_poles_traces = create_neptune_magnetic_poles(center_position, offset_distance, magnetic_tilt, azimuthal_angle)
        if mag_poles_traces and len(mag_poles_traces) > 0:
            for trace in mag_poles_traces:
                traces.append(trace)
        else:
            print("Warning: create_neptune_magnetic_poles returned empty traces")
    except Exception as e:
        print(f"Error in magnetic poles visualization: {e}")
        # Create a simple fallback trace for the magnetic center
        fallback_trace = go.Scatter3d(
            x=[center_x + 0.2 * offset_distance],
            y=[center_y + 0.1 * offset_distance],
            z=[center_z + 0.5 * offset_distance],
            mode='markers',
            marker=dict(
                size=10,
                color='yellow',
                symbol='diamond'
            ),
            name='Neptune: Magnetic Field Center (fallback)',
            showlegend=True
        )
        traces.append(fallback_trace)
   
    return traces

def create_neptune_magnetic_poles(center_position, offset_distance, tilt, azimuth):
    """Creates a simplified visualization of Neptune's magnetic poles and axis."""
    import numpy as np
    
    center_x, center_y, center_z = center_position
    
    # Start with offset magnetic center
    mag_center_x = center_x + (0.2 * offset_distance)
    mag_center_y = center_y + (0.1 * offset_distance)
    mag_center_z = center_z + (0.5 * offset_distance)
    
    # Create axis points (north and south poles at 20 Neptune radii from magnetic center for better visibility)
    axis_length = 20 * NEPTUNE_RADIUS_AU
    
    # Initial axis points along z-axis - already as numpy arrays for rotate_points
    north_x = np.array([0])
    north_y = np.array([0])
    north_z = np.array([axis_length])
    
    south_x = np.array([0])
    south_y = np.array([0])
    south_z = np.array([-axis_length])
    
    # Apply tilts to match Neptune's magnetic field orientation
    # First y-axis tilt
    north_x, north_y, north_z = rotate_points(north_x, north_y, north_z, tilt, 'y')
    south_x, south_y, south_z = rotate_points(south_x, south_y, south_z, tilt, 'y')
    
    # Then z-axis rotation
    north_x, north_y, north_z = rotate_points(north_x, north_y, north_z, azimuth, 'z')
    south_x, south_y, south_z = rotate_points(south_x, south_y, south_z, azimuth, 'z')
    
    # Add to magnetic center offset (keeping as arrays)
    north_x = north_x[0] + mag_center_x  # Extract the single value from the array
    north_y = north_y[0] + mag_center_y
    north_z = north_z[0] + mag_center_z
    
    south_x = south_x[0] + mag_center_x
    south_y = south_y[0] + mag_center_y
    south_z = south_z[0] + mag_center_z
    
    traces = []
    
    # Create magnetic center marker
    mag_center_trace = go.Scatter3d(
        x=[mag_center_x],
        y=[mag_center_y],
        z=[mag_center_z],
        mode='markers',
        marker=dict(
            size=8,  # Larger for visibility
            color='yellow',
            symbol='diamond'
        ),
        name='Neptune: Magnetic Field Center',
        text=["Neptune's magnetic field center is offset by ~0.55 Neptune radii from the planet's center<br>"
              "Neptune has one of the most unusual magnetic fields in our solar system. Unlike Earth, where the magnetic field is <br>" 
              "roughly aligned with the rotation axis, Neptune's magnetic field is:<br>" 
              "* Tilted by approximately 47 degrees relative to its rotation axis.<br>" 
              "* Significantly offset from the planet's center by about 0.55 Neptune radii.<br>" 
              "This creates the seemingly contradictory visualization you're seeing, where:<br>" 
              "* The magnetosphere's bow shock and tail are oriented relative to the solar wind (with the bow shock facing the Sun <br>" 
              "  direction)<br>" 
              "* The magnetic axis (yellow dashed line) and poles (blue and red markers) appear misaligned with this overall <br>" 
              "  magnetosphere structure.<br>" 
              "* This unusual configuration creates a highly dynamic and complex magnetosphere that varies dramatically as Neptune <br>" 
              "  rotates. The magnetic field's significant tilt and offset cause it to \"wobble\" in space during Neptune's rotation, <br>" 
              "  creating unique interactions with the solar wind.<br>" 
              "* What you're seeing is scientifically accurate - Neptune's magnetic field is genuinely this unusual and asymmetric! <br>" 
              "  This configuration was discovered by Voyager 2 during its 1989 flyby and remains one of Neptune's most intriguing characteristics."],
        hovertemplate='%{text}<extra></extra>',
        showlegend=True
    )
    traces.append(mag_center_trace)
    
    # Create magnetic axis line
    axis_trace = go.Scatter3d(
        x=[north_x, mag_center_x, south_x],
        y=[north_y, mag_center_y, south_y],
        z=[north_z, mag_center_z, south_z],
        mode='lines',
        line=dict(
            color='yellow',
            width=6,  # Thicker for visibility
            dash='dash'
        ),
        name='Neptune: Magnetic Axis',
        text=["Neptune's magnetic axis is tilted 47 deg from its rotation axis"] * 3,
        hovertemplate='%{text}<extra></extra>',
        showlegend=True
    )
    traces.append(axis_trace)
    
    # Create north magnetic pole marker
    north_pole_trace = go.Scatter3d(
        x=[north_x],
        y=[north_y],
        z=[north_z],
        mode='markers',
        marker=dict(
            size=10,  # Larger for visibility
            color='blue',
            symbol='circle'
        ),
        name='Neptune: North Magnetic Pole',
        text=["Neptune's north magnetic pole"],
        hovertemplate='%{text}<extra></extra>',
        showlegend=True
    )
    traces.append(north_pole_trace)
    
    # Create south magnetic pole marker
    south_pole_trace = go.Scatter3d(
        x=[south_x],
        y=[south_y],
        z=[south_z],
        mode='markers',
        marker=dict(
            size=10,  # Larger for visibility
            color='red', 
            symbol='circle'
        ),
        name='Neptune: South Magnetic Pole',
        text=["Neptune's south magnetic pole"],
        hovertemplate='%{text}<extra></extra>',
        showlegend=True
    )
    traces.append(south_pole_trace)
    
    # Add debug prints to track the return value
    print(f"Returning {len(traces)} magnetic field traces")
    return traces

# THIS FUNCTION APPEARS OBSOLETE
def create_neptune_field_lines(mag_center_x, mag_center_y, mag_center_z, 
                            north_x, north_y, north_z, 
                            south_x, south_y, south_z,
                            neptune_radius, tilt, azimuth):
    """Creates a simple visualization of Neptune's magnetic field lines."""
    
    traces = []
    
    # Number of field lines to create
    n_lines = 8
    n_points = 40  # Points along each field line
    
    # Create field lines radiating from the poles
    for i in range(n_lines):
        angle = (i / n_lines) * 2 * np.pi
        
        # North pole field lines
        north_lines_x = []
        north_lines_y = []
        north_lines_z = []
        
        # South pole field lines
        south_lines_x = []
        south_lines_y = []
        south_lines_z = []
        
        # Create curved field lines from each pole
        for j in range(n_points):
            # Parameter from 0 to 1
            t = j / (n_points - 1)
            
            # For north pole: lines start at pole and curve toward equatorial plane
            radius_n = 5 * neptune_radius * t  # Distance from pole
            curve_factor_n = np.sin(np.pi * t)  # Curvature
            
            # For south pole: lines start at pole and curve toward equatorial plane
            radius_s = 5 * neptune_radius * t  # Distance from pole
            curve_factor_s = np.sin(np.pi * t)  # Curvature
            
            # Calculate positions with curvature
            # North pole lines
            n_x = north_x - radius_n * (0.5 + 0.5 * curve_factor_n * np.cos(angle))
            n_y = north_y + radius_n * (curve_factor_n * np.sin(angle))
            n_z = north_z - radius_n * (0.7 * curve_factor_n)
            
            # South pole lines
            s_x = south_x + radius_s * (0.5 + 0.5 * curve_factor_s * np.cos(angle + np.pi/n_lines))
            s_y = south_y + radius_s * (curve_factor_s * np.sin(angle + np.pi/n_lines))
            s_z = south_z + radius_s * (0.7 * curve_factor_s)
            
            north_lines_x.append(n_x)
            north_lines_y.append(n_y)
            north_lines_z.append(n_z)
            
            south_lines_x.append(s_x)
            south_lines_y.append(s_y)
            south_lines_z.append(s_z)
        
        # Create traces for these field lines
        north_line_trace = go.Scatter3d(
            x=north_lines_x,
            y=north_lines_y,
            z=north_lines_z,
            mode='lines',
            line=dict(
                color='rgba(100, 150, 255, 0.4)',
                width=2
            ),
            name='Neptune: Magnetic Field Line',
            showlegend=False,
            hoverinfo='none'
        )
        
        south_line_trace = go.Scatter3d(
            x=south_lines_x,
            y=south_lines_y,
            z=south_lines_z,
            mode='lines',
            line=dict(
                color='rgba(255, 100, 100, 0.4)',
                width=2
            ),
            name='Neptune: Magnetic Field Line',
            showlegend=False,
            hoverinfo='none'
        )
        
        traces.append(north_line_trace)
        traces.append(south_line_trace)
        
    return traces

neptune_radiation_belts_info = (
                "560 KB PER FRAME FOR HTML.\n\n"
                "Zones of trapped high-energy particles in neptune's magnetosphere"                     
)

def create_neptune_radiation_belts(center_position=(0, 0, 0)):
    """Creates Neptune's radiation belts with proper structure reflecting the complex magnetospheric environment."""
    # Belt names and descriptions based on current understanding
    belt_regions = [
        {
            'name': 'Proton-Rich Inner Belt',
            'distance': 1.8,  # Neptune radii from magnetic center
            'thickness': 0.5,  # Relative thickness
            'color': 'rgb(80, 180, 255)',  
            'opacity': 0.4,
            'description': "Neptune's innermost radiation belt is dominated by protons. Located approximately 1.2-2.5 Neptune <br>"
                          "radii from the center, it's influenced by Neptune's offset and tilted magnetic field. This region <br>"
                          "shows significant day/night asymmetry as Neptune rotates.<br><br>" 
                          "This implementation includes four distinct radiation regions: a proton-rich inner belt; a primary <br>" 
                          "electron belt; an outer plasma sheet region; a cusp region where solar wind particles directly enter.<br>" 
                          "* Adds field-aligned currents that represent important features in Neptune's magnetosphere, showing how <br>" 
                          "  charged particles flow along magnetic field lines.<br>" 
                          "* Creates more accurate geometric structures that reflect Neptune's complex magnetic environment: asymmetric <br>" 
                          "  shapes that account for the unusual magnetic field.<br>" 
                          "* Magnetotail stretching for the outer plasma sheet.<br>" 
                          "* Funnel-shaped polar cusps.<br>" 
                          "* Maintaining proper magnetic field geometry: 47 deg tilt from the rotation axis; 0.55 Neptune radii offset <br>" 
                          "  from the planet's center.<br>" 
                          "* Given the scarcity of direct measurements, this represents our best current understanding based on Voyager 2 <br>" 
                          "  data and subsequent scientific analysis."
        },
        {
            'name': 'Primary Electron Belt',
            'distance': 3.5,  # Neptune radii from magnetic center
            'thickness': 0.6,  # Relative thickness
            'color': 'rgb(120, 150, 230)',  
            'opacity': 0.35,
            'description': "Neptune's middle radiation region contains high-energy electrons. This belt shows notable <br>"
                          "variations in intensity with longitude due to Neptune's unusual magnetic field geometry. <br>"
                          "The trapped electron fluxes here are surprisingly intense, comparable to Earth's electron belts.<br><br>"
                          "This implementation includes four distinct radiation regions: a proton-rich inner belt; a primary <br>" 
                          "electron belt; an outer plasma sheet region; a cusp region where solar wind particles directly enter.<br>" 
                          "* Adds field-aligned currents that represent important features in Neptune's magnetosphere, showing how <br>" 
                          "  charged particles flow along magnetic field lines.<br>" 
                          "* Creates more accurate geometric structures that reflect Neptune's complex magnetic environment: asymmetric <br>" 
                          "  shapes that account for the unusual magnetic field.<br>" 
                          "* Magnetotail stretching for the outer plasma sheet.<br>" 
                          "* Funnel-shaped polar cusps.<br>" 
                          "* Maintaining proper magnetic field geometry: 47 deg tilt from the rotation axis; 0.55 Neptune radii offset <br>" 
                          "  from the planet's center.<br>" 
                          "* Given the scarcity of direct measurements, this represents our best current understanding based on Voyager 2 <br>" 
                          "  data and subsequent scientific analysis."                          
        },
        {
            'name': 'Outer Plasma Sheet',
            'distance': 6.0,  # Neptune radii from magnetic center
            'thickness': 0.8,  # Relative thickness
            'color': 'rgb(150, 130, 210)',  
            'opacity': 0.3,
            'description': "This transition region between the trapped radiation and the magnetotail contains a mix of charged <br>"
                          "particles. Its structure is highly dynamic and asymmetric, with its shape constantly changing as <br>"
                          "Neptune rotates and the solar wind conditions vary.<br><br>"
                          "This implementation includes four distinct radiation regions: a proton-rich inner belt; a primary <br>" 
                          "electron belt; an outer plasma sheet region; a cusp region where solar wind particles directly enter.<br>" 
                          "* Adds field-aligned currents that represent important features in Neptune's magnetosphere, showing how <br>" 
                          "  charged particles flow along magnetic field lines.<br>" 
                          "* Creates more accurate geometric structures that reflect Neptune's complex magnetic environment: asymmetric <br>" 
                          "  shapes that account for the unusual magnetic field.<br>" 
                          "* Magnetotail stretching for the outer plasma sheet.<br>" 
                          "* Funnel-shaped polar cusps.<br>" 
                          "* Maintaining proper magnetic field geometry: 47 deg tilt from the rotation axis; 0.55 Neptune radii offset <br>" 
                          "  from the planet's center.<br>" 
                          "* Given the scarcity of direct measurements, this represents our best current understanding based on Voyager 2 <br>" 
                          "  data and subsequent scientific analysis."
        },
        {
            'name': 'Cusp Region',
            'distance': 4.2,  # Neptune radii from magnetic center
            'thickness': 0.4,  # Relative thickness
            'color': 'rgb(200, 150, 180)',  
            'opacity': 0.25,
            'variable_offset': True,  # Special handling for cusp region
            'description': "The polar cusps represent funnel-shaped openings where solar wind particles can directly access <br>"
                          "Neptune's magnetosphere. Due to Neptune's tilted magnetic field, these regions demonstrate complex <br>"
                          "behavior and vary dramatically with the planet's rotation.<br><br>"
                          "This implementation includes four distinct radiation regions: a proton-rich inner belt; a primary <br>" 
                          "electron belt; an outer plasma sheet region; a cusp region where solar wind particles directly enter.<br>" 
                          "* Adds field-aligned currents that represent important features in Neptune's magnetosphere, showing how <br>" 
                          "  charged particles flow along magnetic field lines.<br>" 
                          "* Creates more accurate geometric structures that reflect Neptune's complex magnetic environment: asymmetric <br>" 
                          "  shapes that account for the unusual magnetic field.<br>" 
                          "* Magnetotail stretching for the outer plasma sheet.<br>" 
                          "* Funnel-shaped polar cusps.<br>" 
                          "* Maintaining proper magnetic field geometry: 47 deg tilt from the rotation axis; 0.55 Neptune radii offset <br>" 
                          "  from the planet's center.<br>" 
                          "* Given the scarcity of direct measurements, this represents our best current understanding based on Voyager 2 <br>" 
                          "  data and subsequent scientific analysis."
        }
    ]
    
    # Unpack center position
    center_x, center_y, center_z = center_position
    
    # Apply magnetic field offset (about 0.55 Neptune radii, offset from center)
    offset_distance = 0.55 * NEPTUNE_RADIUS_AU
    magnetic_center_x = center_x + (0.2 * offset_distance)
    magnetic_center_y = center_y + (0.1 * offset_distance)
    magnetic_center_z = center_z + (0.5 * offset_distance)
    
    # Neptune's magnetic axis tilt in radians (47 degrees from rotation axis)
    magnetic_tilt = np.radians(47)
    
    # Additional rotation to match the observed orientation
    azimuthal_angle = np.radians(60)  # Based on Voyager data
    
    traces = []
    
    for belt in belt_regions:
        belt_x = []
        belt_y = []
        belt_z = []
        
        n_points = 90  # More points for smoother appearance
        n_rings = 6    # More rings for better volume representation
        
        # Scale distances by Neptune's radius in AU
        belt_distance = belt['distance'] * NEPTUNE_RADIUS_AU
        belt_thickness = belt['thickness'] * NEPTUNE_RADIUS_AU
        
        for i_ring in range(n_rings):
            # Vary the radius slightly to create thickness
            radius_offset = (i_ring / (n_rings-1) - 0.5) * belt_thickness
            ring_radius = belt_distance + radius_offset
            
            for j in range(n_points):
                angle = (j / n_points) * 2 * np.pi
                
                # Create a belt around magnetic field axis
                x = ring_radius * np.cos(angle)
                y = ring_radius * np.sin(angle)
                
                # For the cusp region, create a more funnel-like shape
                if belt.get('variable_offset', False):
                    # Create funnel-like shape pointing in the magnetic field direction
                    z_scale = 0.4 * ring_radius * (1 + 0.5 * np.cos(angle))
                    z = z_scale * np.sin(angle)
                    
                    # Add distortion to create cusp-like features
                    if np.abs(np.sin(angle)) > 0.7:
                        z = z * 1.5
                else:
                    # For regular belts, add variation to create a more realistic shape
                    z_scale = 0.2 * ring_radius
                    z = z_scale * np.sin(2 * angle)
                    
                    # Add some longitudinal variation to reflect Neptune's complex field
                    variation = 0.15 * ring_radius * np.sin(3 * angle)
                    x += variation * np.cos(angle + np.pi/4)
                    y += variation * np.sin(angle + np.pi/4)
                
                belt_x.append(x)
                belt_y.append(y)
                belt_z.append(z)
        
        # Convert to numpy arrays for efficient rotation
        belt_x = np.array(belt_x)
        belt_y = np.array(belt_y)
        belt_z = np.array(belt_z)
        
        # First apply rotation around y-axis for magnetic tilt
        x_rotated1, y_rotated1, z_rotated1 = rotate_points(belt_x, belt_y, belt_z, magnetic_tilt, 'y')
        
        # Then apply rotation around z-axis for azimuthal orientation
        x_rotated2, y_rotated2, z_rotated2 = rotate_points(x_rotated1, y_rotated1, z_rotated1, azimuthal_angle, 'z')
        
        # Apply additional distortions for more complex shapes
        # For outer plasma sheet, create magnetotail-like extension
        if belt['name'] == 'Outer Plasma Sheet':
            # Apply a gradient to simulate magnetotail stretching
            stretch_factor = 1.0 + 0.8 * np.clip(-x_rotated2/belt_distance, 0, 1.5)
            x_rotated2 = x_rotated2 * stretch_factor
            
            # Add some flaring to the tail
            tail_factor = np.clip(-x_rotated2/belt_distance, 0, 1)
            y_rotated2 = y_rotated2 * (1 + 0.3 * tail_factor)
            z_rotated2 = z_rotated2 * (1 + 0.3 * tail_factor)
        
        # Apply magnetic center offset
        x_final = x_rotated2 + magnetic_center_x
        y_final = y_rotated2 + magnetic_center_y
        z_final = z_rotated2 + magnetic_center_z
        
        # Create hover information arrays
        belt_text = [belt['description']] * len(belt_x)
        belt_customdata = [f"Neptune: {belt['name']}"] * len(belt_x)
        
        # Create the trace
        traces.append(
            go.Scatter3d(
                x=x_final,
                y=y_final,
                z=z_final,
                mode='markers',
                marker=dict(
                    size=2.0,
                    color=belt['color'],
                    opacity=belt['opacity']
                ),
                name=f"Neptune: {belt['name']}",
                text=belt_text,
                customdata=belt_customdata,
                hovertemplate='%{text}<extra></extra>',
                showlegend=True
            )
        )
    
    # Add field-aligned current visualization connecting regions
    # These are important features in Neptune's dynamic magnetosphere
    current_traces = create_field_aligned_currents(magnetic_center_x, magnetic_center_y, magnetic_center_z, 
                                                 magnetic_tilt, azimuthal_angle)
    traces.extend(current_traces)
    
    sun_traces = create_sun_direction_indicator(
        center_position=center_position, 
        shell_radius= 6.0 * NEPTUNE_RADIUS_AU
    )
    for trace in sun_traces:
        traces.append(trace)

    return traces

def create_field_aligned_currents(mag_center_x, mag_center_y, mag_center_z, tilt, azimuth):
    """Creates visualization of field-aligned currents in Neptune's magnetosphere."""
    # These are electric currents that flow along magnetic field lines
    # and are important features of planetary magnetospheres
    
    traces = []
    
    # Define parameters for currents
    current_params = [
        {
            'start_radius': 2.0 * NEPTUNE_RADIUS_AU,
            'end_radius': 5.0 * NEPTUNE_RADIUS_AU,
            'angle_range': (np.pi/4, 3*np.pi/4),  # Angular sector for current
            'color': 'rgb(200, 200, 255)',
            'name': 'Dusk Field-Aligned Current',
            'description': ("Field-aligned currents are channels of charged particles flowing along magnetic field lines. <br>"
                           "In Neptune's complex magnetic environment, these currents connect different regions of the magnetosphere <br>"
                           "and play an important role in energy transfer. The dusk sector currents flow in the evening "
                           "side of the planet's magnetosphere.")
        },
        {
            'start_radius': 2.0 * NEPTUNE_RADIUS_AU,
            'end_radius': 5.0 * NEPTUNE_RADIUS_AU,
            'angle_range': (5*np.pi/4, 7*np.pi/4),  # Angular sector for current
            'color': 'rgb(200, 200, 255)',
            'name': 'Dawn Field-Aligned Current',
            'description': ("Field-aligned currents are channels of charged particles flowing along magnetic field lines. <br>"
                           "In Neptune's complex magnetic environment, these currents connect different regions of the magnetosphere <br>"
                           "and play an important role in energy transfer. The dawn sector currents flow in the morning "
                           "side of the planet's magnetosphere.")
        }
    ]
    
    for params in current_params:
        current_x = []
        current_y = []
        current_z = []
        
        # Number of field lines and points per line
        n_lines = 15
        n_points = 20
        
        for i in range(n_lines):
            # Vary the angle within the specified range
            angle_range = params['angle_range']
            angle = angle_range[0] + (angle_range[1] - angle_range[0]) * (i / (n_lines-1))
            
            # Create points along a curved field line
            for j in range(n_points):
                # Parametric position along the field line (0 to 1)
                t = j / (n_points-1)
                
                # Calculate radius that follows magnetic field line shape
                radius = params['start_radius'] + (params['end_radius'] - params['start_radius']) * t
                
                # Add curvature to field line
                angle_offset = 0.4 * np.sin(np.pi * t)  # Max 0.4 radians (~23 deg) curvature
                current_angle = angle + angle_offset
                
                # Calculate position
                x = radius * np.cos(current_angle)
                y = radius * np.sin(current_angle)
                z = radius * 0.5 * np.sin(np.pi * t)  # Add some z-variation
                
                current_x.append(x)
                current_y.append(y)
                current_z.append(z)
        
        # Convert to numpy arrays for rotation
        current_x = np.array(current_x)
        current_y = np.array(current_y)
        current_z = np.array(current_z)
        
        # Apply rotations to align with magnetic field
        # First apply rotation around y-axis for magnetic tilt
        x_rot1, y_rot1, z_rot1 = rotate_points(current_x, current_y, current_z, tilt, 'y')
        
        # Then apply rotation around z-axis for azimuthal orientation
        x_rot2, y_rot2, z_rot2 = rotate_points(x_rot1, y_rot1, z_rot1, azimuth, 'z')
        
        # Apply magnetic center offset
        x_final = x_rot2 + mag_center_x
        y_final = y_rot2 + mag_center_y
        z_final = z_rot2 + mag_center_z
        
        # Create hover text and customdata arrays for consistency with other traces
        hover_text = [params['description']] * len(current_x)
        custom_data = [f"Neptune: {params['name']}"] * len(current_x)
        
        # Create the trace with very small markers to create a line-like effect
        traces.append(
            go.Scatter3d(
                x=x_final,
                y=y_final,
                z=z_final,
                mode='markers',
                marker=dict(
                    size=1.0,
                    color=params['color'],
                    opacity=0.3
                ),
                name=f"Neptune: {params['name']}",
                text=hover_text,
                customdata=custom_data,
                hovertemplate='%{text}<extra></extra>',
                showlegend=True
            )
        )
    
    return traces
    
neptune_ring_system_info = (
                "22.2 MB PER FRAME FOR HTML.\n\n"

                "neptune has a system of 13 known rings. These rings are generally very narrow, dark (reflecting very little light, \n" 
                "similar to charcoal), and composed of dust and larger particles that are icy and darkened by rock. The rings are \n" 
                "grouped into two main systems:\n" 
                "* Inner Rings: Nine narrow, dark rings.\n" 
                "* Outer Rings: Two more distant rings, one of which is bluish and the other reddish.\n" 
                "While the main rings of neptune are narrow bands, there are also broader, more diffuse rings made of dust. These \n" 
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
                "  outer rings are likely fed by dust kicked off neptune' inner moons by micrometeoroid impacts.\n" 
                "* Visual Characteristics: The main rings are dark and difficult to see, requiring specific observation techniques. The \n" 
                "  outer rings are even fainter, with the Mu ring having a unique blue color.\n" 
                "In summary, while all are part of neptune' ring system, the significant differences in their composition, structure, and \n" 
                "likely origin make it accurate and informative to distinguish between the narrow, dark main rings and the broad, dusty, \n" 
                "and torus-like outer rings."                                           
)

def create_neptune_ring_system(center_position=(0, 0, 0)):
    """
    Creates a visualization of Neptune's ring system with proper alignment.
    
    Parameters:
        center_position (tuple): (x, y, z) position of Neptune's center
        
    Returns:
        list: A list of plotly traces representing Neptune's ring components
        
    Notes:
        Neptune's ring system requires specific transformations to correctly align
        with its axial tilt (28.32 deg) and pole orientation. Unlike Uranus (which has
        an extreme axial tilt of ~98 deg), Neptune's rings require a different approach.
        
        The transformation uses:
        1. Standard orbital element rotations for each ring
        2. Application of Neptune's pole direction (RA: 299.36 deg, Dec: 43.46 deg)
        3. Proper offsetting relative to Neptune's center
    """
    traces = []
    
    # Define Neptune's ring parameters in kilometers from Neptune's center
    # Then convert to Neptune radii, and finally to AU
    ring_params = {
        'galle_ring': {
            'inner_radius_km': 41900,  # Inner edge (in km from Neptune's center)
            'outer_radius_km': 42900,  # Outer edge (in km from Neptune's center)
            'thickness_km': 15,         # Approximate thickness
            'color': 'rgb(70, 70, 70)',  
            'opacity': 0.4,
            'name': 'Galle Ring (1989N3R)',
            'description': (
                "Galle Ring (1989N3R): Neptune's innermost ring, located about 41,900-42,900 km from Neptune's center.<br>" 
                "* Named after Johann Gottfried Galle, who discovered Neptune in 1846.<br>" 
                "* Faint, relatively broad ring approximately 2,000 km in width.<br>" 
                "* Composed primarily of dust particles, giving it a diffuse appearance.<br>" 
                "* Relatively uniform, lacking the clumpy structure seen in some of Neptune's other rings.<br>"
                "* Discovery: First detected by Voyager 2 during its 1989 flyby mission.<br><br>" 
                "Unlike Triton, Neptune's rings lie in Neptune's equatorial plane, as is typical for planetary ring systems. This is <br>" 
                "due to the physical processes that form and maintain rings - they tend to settle into the equatorial plane due to the <br>" 
                "planet's rotational bulge. The other regular satellites of Neptune (like Proteus, Larissa, Galatea, and Despina) orbit <br>" 
                "in Neptune's equatorial plane, aligned with the rings. These inner moons play an important role in shepherding and <br>" 
                "maintaining the ring structure, particularly:<br>" 
                "* Galatea: This moon helps confine the Adams Ring and its distinctive arcs through orbital resonances.<br>" 
                "* Despina: Located near the Le Verrier Ring, it may help maintain its structure.<br>" 
                "* This misalignment between Triton and the rings/regular moons provides strong evidence for Triton's capture hypothesis <br>" 
                "  - it was likely an independent Kuiper Belt Object (similar to Pluto) that was captured by Neptune's gravity rather than <br>" 
                "  forming alongside Neptune like the other moons.<br>" 
                "* The contrast between the orderly, equatorial system of rings and regular moons versus Triton's highly inclined <br>" 
                "  orbit represents two different formation mechanisms in the same planetary system."
            )
        },
        
        'leverrier_ring': {
            'inner_radius_km': 53200,  # Inner edge (in km from Neptune's center)
            'outer_radius_km': 53200,  # Outer edge (in km from Neptune's center)
            'thickness_km': 110,       # Approximate thickness
            'color': 'rgb(75, 75, 75)',  
            'opacity': 0.5,
            'name': 'Leverrier Ring (1989N2R)',
            'description': (
                "Leverrier Ring (1989N2R): A narrow, well-defined ring located about 53,200 km from Neptune's center.<br>" 
                "* Named after Urbain Le Verrier, who mathematically predicted Neptune's existence.<br>" 
                "* Approximately 110 km in width, much narrower than the Galle ring.<br>" 
                "* Higher density of material compared to the Galle ring, giving it a more defined appearance.<br>" 
                "* May have small embedded moonlets that help maintain its structure.<br>"
                "* Discovery: First detected by Voyager 2 during its 1989 flyby mission.<br><br>"
                "Unlike Triton, Neptune's rings lie in Neptune's equatorial plane, as is typical for planetary ring systems. This is <br>" 
                "due to the physical processes that form and maintain rings - they tend to settle into the equatorial plane due to the <br>" 
                "planet's rotational bulge. The other regular satellites of Neptune (like Proteus, Larissa, Galatea, and Despina) orbit <br>" 
                "in Neptune's equatorial plane, aligned with the rings. These inner moons play an important role in shepherding and <br>" 
                "maintaining the ring structure, particularly:<br>" 
                "* Galatea: This moon helps confine the Adams Ring and its distinctive arcs through orbital resonances.<br>" 
                "* Despina: Located near the Le Verrier Ring, it may help maintain its structure.<br>" 
                "* This misalignment between Triton and the rings/regular moons provides strong evidence for Triton's capture hypothesis <br>" 
                "  - it was likely an independent Kuiper Belt Object (similar to Pluto) that was captured by Neptune's gravity rather than <br>" 
                "  forming alongside Neptune like the other moons.<br>" 
                "* The contrast between the orderly, equatorial system of rings and regular moons versus Triton's highly inclined <br>" 
                "  orbit represents two different formation mechanisms in the same planetary system."
            )
        },
        
        'lassell_ring': {
            'inner_radius_km': 55400,  # Inner edge (in km from Neptune's center)
            'outer_radius_km': 57600,  # Outer edge (in km from Neptune's center)
            'thickness_km': 4000,      # Approximate thickness
            'color': 'rgb(70, 70, 75)',  
            'opacity': 0.3,
            'name': 'Lassell Ring',
            'description': (
                "Lassell Ring: A broad, faint plateau-like ring region extending from about 55,400 to 57,600 km from Neptune's center.<br>" 
                "* Named after William Lassell, who discovered Neptune's largest moon Triton.<br>" 
                "* Sometimes described as a 'plateau' rather than a distinct ring.<br>" 
                "* Very faint, with a width of approximately 4,000 km.<br>" 
                "* Has a more diffuse, dusty composition.<br>"
                "* Connects the Leverrier and Arago rings, forming part of a broader ring system structure.<br><br>"
                "Unlike Triton, Neptune's rings lie in Neptune's equatorial plane, as is typical for planetary ring systems. This is <br>" 
                "due to the physical processes that form and maintain rings - they tend to settle into the equatorial plane due to the <br>" 
                "planet's rotational bulge. The other regular satellites of Neptune (like Proteus, Larissa, Galatea, and Despina) orbit <br>" 
                "in Neptune's equatorial plane, aligned with the rings. These inner moons play an important role in shepherding and <br>" 
                "maintaining the ring structure, particularly:<br>" 
                "* Galatea: This moon helps confine the Adams Ring and its distinctive arcs through orbital resonances.<br>" 
                "* Despina: Located near the Le Verrier Ring, it may help maintain its structure.<br>" 
                "* This misalignment between Triton and the rings/regular moons provides strong evidence for Triton's capture hypothesis <br>" 
                "  - it was likely an independent Kuiper Belt Object (similar to Pluto) that was captured by Neptune's gravity rather than <br>" 
                "  forming alongside Neptune like the other moons.<br>" 
                "* The contrast between the orderly, equatorial system of rings and regular moons versus Triton's highly inclined <br>" 
                "  orbit represents two different formation mechanisms in the same planetary system."
            )
        },
        
        'arago_ring': {
            'inner_radius_km': 57600,  # Inner edge (in km from Neptune's center)
            'outer_radius_km': 57600,  # Outer edge (in km from Neptune's center)
            'thickness_km': 100,       # Approximate thickness
            'color': 'rgb(80, 80, 85)',  
            'opacity': 0.4,
            'name': 'Arago Ring',
            'description': (
                "Arago Ring: A narrow ring located at the outer edge of the Lassell Ring, about 57,600 km from Neptune's center.<br>" 
                "* Named after Francois Arago, a French mathematician, physicist, and astronomer.<br>" 
                "* Approximately 100 km in width.<br>" 
                "* Less prominent than the Leverrier and Adams rings.<br>" 
                "* Discovery: First observed by Voyager 2 in 1989, though initially not designated as a separate ring.<br><br>"
                "Unlike Triton, Neptune's rings lie in Neptune's equatorial plane, as is typical for planetary ring systems. This is <br>" 
                "due to the physical processes that form and maintain rings - they tend to settle into the equatorial plane due to the <br>" 
                "planet's rotational bulge. The other regular satellites of Neptune (like Proteus, Larissa, Galatea, and Despina) orbit <br>" 
                "in Neptune's equatorial plane, aligned with the rings. These inner moons play an important role in shepherding and <br>" 
                "maintaining the ring structure, particularly:<br>" 
                "* Galatea: This moon helps confine the Adams Ring and its distinctive arcs through orbital resonances.<br>" 
                "* Despina: Located near the Le Verrier Ring, it may help maintain its structure.<br>" 
                "* This misalignment between Triton and the rings/regular moons provides strong evidence for Triton's capture hypothesis <br>" 
                "  - it was likely an independent Kuiper Belt Object (similar to Pluto) that was captured by Neptune's gravity rather than <br>" 
                "  forming alongside Neptune like the other moons.<br>" 
                "* The contrast between the orderly, equatorial system of rings and regular moons versus Triton's highly inclined <br>" 
                "  orbit represents two different formation mechanisms in the same planetary system."
            )
        },
        
        'adams_ring': {
            'inner_radius_km': 62932,  # Inner edge (in km from Neptune's center)
            'outer_radius_km': 62932,  # Outer edge (in km from Neptune's center)
            'thickness_km': 50,        # Approximate thickness, variable
            'color': 'rgb(85, 85, 85)',  
            'opacity': 0.6,
            'name': 'Adams Ring (1989N1R)',
            'description': (
                "Adams Ring (1989N1R): Neptune's outermost and most prominent discrete ring, located about 62,930 km from Neptune's center.<br>" 
                "* Named after John Couch Adams, who independently predicted Neptune's existence around the same time as Le Verrier.<br>" 
                "* Has a variable width of approximately 35-50 km, but contains distinctive arc segments.<br>" 
                "* Contains five prominent arc segments (Courage, Liberte, Egalite 1 & 2, and Fraternite) that are denser than the rest of the ring.<br>" 
                "* These arcs are confined by gravitational resonances with the moon Galatea.<br>"
                "* Most studied of Neptune's rings, with observations from both Voyager 2 and Earth-based telescopes.<br>"
                "* Discovery: Its bright arcs were first detected from Earth in 1984, then confirmed by Voyager 2 in 1989.<br><br>"
                "Unlike Triton, Neptune's rings lie in Neptune's equatorial plane, as is typical for planetary ring systems. This is <br>" 
                "due to the physical processes that form and maintain rings - they tend to settle into the equatorial plane due to the <br>" 
                "planet's rotational bulge. The other regular satellites of Neptune (like Proteus, Larissa, Galatea, and Despina) orbit <br>" 
                "in Neptune's equatorial plane, aligned with the rings. These inner moons play an important role in shepherding and <br>" 
                "maintaining the ring structure, particularly:<br>" 
                "* Galatea: This moon helps confine the Adams Ring and its distinctive arcs through orbital resonances.<br>" 
                "* Despina: Located near the Le Verrier Ring, it may help maintain its structure.<br>" 
                "* This misalignment between Triton and the rings/regular moons provides strong evidence for Triton's capture hypothesis <br>" 
                "  - it was likely an independent Kuiper Belt Object (similar to Pluto) that was captured by Neptune's gravity rather than <br>" 
                "  forming alongside Neptune like the other moons.<br>" 
                "* The contrast between the orderly, equatorial system of rings and regular moons versus Triton's highly inclined <br>" 
                "  orbit represents two different formation mechanisms in the same planetary system."
            )
        },
        
        'adams_courage_arc': {
            'inner_radius_km': 62932,  # Inner edge (in km from Neptune's center)
            'outer_radius_km': 62932,  # Outer edge (in km from Neptune's center)
            'thickness_km': 50,        # Approximate thickness
            'arc_length': 4.0,         # Arc length in degrees
            'arc_center': 0,           # Center angle of the arc in degrees
            'color': 'rgb(200, 200, 200)',  
            'opacity': 0.7,
            'name': 'Courage Arc',
            'description': (
                "Courage Arc: The smallest and faintest of the five arcs in Neptune's Adams Ring.<br>" 
                "* Located within the Adams Ring at a distance of about 62,930 km from Neptune's center.<br>" 
                "* Spans approximately 1,000 km (4 deg of arc) along the ring.<br>" 
                "* Named after one of the three civic virtues from the motto of the French Republic.<br>"
                "* The least stable of the arcs, showing significant changes since its discovery.<br>"
                "* Discovery: First imaged by Voyager 2 in 1989.<br><br>"
                "Unlike Triton, Neptune's rings lie in Neptune's equatorial plane, as is typical for planetary ring systems. This is <br>" 
                "due to the physical processes that form and maintain rings - they tend to settle into the equatorial plane due to the <br>" 
                "planet's rotational bulge. The other regular satellites of Neptune (like Proteus, Larissa, Galatea, and Despina) orbit <br>" 
                "in Neptune's equatorial plane, aligned with the rings. These inner moons play an important role in shepherding and <br>" 
                "maintaining the ring structure, particularly:<br>" 
                "* Galatea: This moon helps confine the Adams Ring and its distinctive arcs through orbital resonances.<br>" 
                "* Despina: Located near the Le Verrier Ring, it may help maintain its structure.<br>" 
                "* This misalignment between Triton and the rings/regular moons provides strong evidence for Triton's capture hypothesis <br>" 
                "  - it was likely an independent Kuiper Belt Object (similar to Pluto) that was captured by Neptune's gravity rather than <br>" 
                "  forming alongside Neptune like the other moons.<br>" 
                "* The contrast between the orderly, equatorial system of rings and regular moons versus Triton's highly inclined <br>" 
                "  orbit represents two different formation mechanisms in the same planetary system."
            )
        },
        
        'adams_liberte_arc': {
            'inner_radius_km': 62932,  # Inner edge (in km from Neptune's center)
            'outer_radius_km': 62932,  # Outer edge (in km from Neptune's center)
            'thickness_km': 50,        # Approximate thickness
            'arc_length': 4.5,         # Arc length in degrees
            'arc_center': 8.0,         # Center angle of the arc in degrees
            'color': 'rgb(200, 200, 200)',  
            'opacity': 0.7,
            'name': 'Liberte Arc',
            'description': (
                "Liberte Arc: The second arc in Neptune's Adams Ring.<br>" 
                "* Located within the Adams Ring at a distance of about 62,930 km from Neptune's center.<br>" 
                "* Spans approximately 1,100 km (4.5 deg of arc) along the ring.<br>" 
                "* Named after 'Liberty' from the motto of the French Republic ('Liberty, Equality, Fraternity').<br>"
                "* Shows brightness variations along its length.<br>"
                "* Has shown evolutionary changes since its discovery, with variations in brightness and length.<br><br>"
                "Unlike Triton, Neptune's rings lie in Neptune's equatorial plane, as is typical for planetary ring systems. This is <br>" 
                "due to the physical processes that form and maintain rings - they tend to settle into the equatorial plane due to the <br>" 
                "planet's rotational bulge. The other regular satellites of Neptune (like Proteus, Larissa, Galatea, and Despina) orbit <br>" 
                "in Neptune's equatorial plane, aligned with the rings. These inner moons play an important role in shepherding and <br>" 
                "maintaining the ring structure, particularly:<br>" 
                "* Galatea: This moon helps confine the Adams Ring and its distinctive arcs through orbital resonances.<br>" 
                "* Despina: Located near the Le Verrier Ring, it may help maintain its structure.<br>" 
                "* This misalignment between Triton and the rings/regular moons provides strong evidence for Triton's capture hypothesis <br>" 
                "  - it was likely an independent Kuiper Belt Object (similar to Pluto) that was captured by Neptune's gravity rather than <br>" 
                "  forming alongside Neptune like the other moons.<br>" 
                "* The contrast between the orderly, equatorial system of rings and regular moons versus Triton's highly inclined <br>" 
                "  orbit represents two different formation mechanisms in the same planetary system."
            )
        },
        
        'adams_egalite1_arc': {
            'inner_radius_km': 62932,  # Inner edge (in km from Neptune's center)
            'outer_radius_km': 62932,  # Outer edge (in km from Neptune's center)
            'thickness_km': 50,        # Approximate thickness
            'arc_length': 4.2,         # Arc length in degrees
            'arc_center': 14.0,        # Center angle of the arc in degrees
            'color': 'rgb(200, 200, 200)',  
            'opacity': 0.7,
            'name': 'Egalite 1 Arc',
            'description': (
                "Egalite 1 Arc: One of two 'Equality' arcs in Neptune's Adams Ring.<br>" 
                "* Located within the Adams Ring at a distance of about 62,930 km from Neptune's center.<br>" 
                "* Spans approximately 1,000 km (4.2 deg of arc) along the ring.<br>" 
                "* Named after 'Equality' from the motto of the French Republic.<br>"
                "* Together with Egalite 2, forms a pair of similar arcs separated by a small gap.<br>"
                "* Has shown some changes in structure since the Voyager 2 observations.<br><br>"
                "Unlike Triton, Neptune's rings lie in Neptune's equatorial plane, as is typical for planetary ring systems. This is <br>" 
                "due to the physical processes that form and maintain rings - they tend to settle into the equatorial plane due to the <br>" 
                "planet's rotational bulge. The other regular satellites of Neptune (like Proteus, Larissa, Galatea, and Despina) orbit <br>" 
                "in Neptune's equatorial plane, aligned with the rings. These inner moons play an important role in shepherding and <br>" 
                "maintaining the ring structure, particularly:<br>" 
                "* Galatea: This moon helps confine the Adams Ring and its distinctive arcs through orbital resonances.<br>" 
                "* Despina: Located near the Le Verrier Ring, it may help maintain its structure.<br>" 
                "* This misalignment between Triton and the rings/regular moons provides strong evidence for Triton's capture hypothesis <br>" 
                "  - it was likely an independent Kuiper Belt Object (similar to Pluto) that was captured by Neptune's gravity rather than <br>" 
                "  forming alongside Neptune like the other moons.<br>" 
                "* The contrast between the orderly, equatorial system of rings and regular moons versus Triton's highly inclined <br>" 
                "  orbit represents two different formation mechanisms in the same planetary system."
            )
        },
        
        'adams_egalite2_arc': {
            'inner_radius_km': 62932,  # Inner edge (in km from Neptune's center)
            'outer_radius_km': 62932,  # Outer edge (in km from Neptune's center)
            'thickness_km': 50,        # Approximate thickness
            'arc_length': 4.0,         # Arc length in degrees
            'arc_center': 22.0,        # Center angle of the arc in degrees
            'color': 'rgb(200, 200, 200)',  
            'opacity': 0.7,
            'name': 'Egalite 2 Arc',
            'description': (
                "Egalite 2 Arc: The second 'Equality' arc in Neptune's Adams Ring.<br>" 
                "* Located within the Adams Ring at a distance of about 62,930 km from Neptune's center.<br>" 
                "* Spans approximately 1,000 km (4 deg of arc) along the ring.<br>" 
                "* Named after 'Equality' from the motto of the French Republic.<br>"
                "* Follows closely after Egalite 1, separated by a small gap.<br>"
                "* The pair of Egalite arcs may be maintained by resonances with nearby moons.<br><br>"
                "Unlike Triton, Neptune's rings lie in Neptune's equatorial plane, as is typical for planetary ring systems. This is <br>" 
                "due to the physical processes that form and maintain rings - they tend to settle into the equatorial plane due to the <br>" 
                "planet's rotational bulge. The other regular satellites of Neptune (like Proteus, Larissa, Galatea, and Despina) orbit <br>" 
                "in Neptune's equatorial plane, aligned with the rings. These inner moons play an important role in shepherding and <br>" 
                "maintaining the ring structure, particularly:<br>" 
                "* Galatea: This moon helps confine the Adams Ring and its distinctive arcs through orbital resonances.<br>" 
                "* Despina: Located near the Le Verrier Ring, it may help maintain its structure.<br>" 
                "* This misalignment between Triton and the rings/regular moons provides strong evidence for Triton's capture hypothesis <br>" 
                "  - it was likely an independent Kuiper Belt Object (similar to Pluto) that was captured by Neptune's gravity rather than <br>" 
                "  forming alongside Neptune like the other moons.<br>" 
                "* The contrast between the orderly, equatorial system of rings and regular moons versus Triton's highly inclined <br>" 
                "  orbit represents two different formation mechanisms in the same planetary system."
            )
        },
        
        'adams_fraternite_arc': {
            'inner_radius_km': 62932,  # Inner edge (in km from Neptune's center)
            'outer_radius_km': 62932,  # Outer edge (in km from Neptune's center)
            'thickness_km': 50,        # Approximate thickness
            'arc_length': 9.0,         # Arc length in degrees
            'arc_center': 40.0,        # Center angle of the arc in degrees
            'color': 'rgb(200, 200, 200)',  
            'opacity': 0.7,
            'name': 'Fraternite Arc',
            'description': (
                "Fraternite Arc: The longest and most prominent arc in Neptune's Adams Ring.<br>" 
                "* Located within the Adams Ring at a distance of about 62,930 km from Neptune's center.<br>" 
                "* Spans approximately 2,200 km (9 deg of arc) along the ring, making it the longest arc.<br>" 
                "* Named after 'Fraternity' from the motto of the French Republic.<br>"
                "* The brightest and most stable of Neptune's ring arcs.<br>"
                "* Discovery: It was the first arc detected from Earth-based observations in 1984.<br><br>"
                "Unlike Triton, Neptune's rings lie in Neptune's equatorial plane, as is typical for planetary ring systems. This is <br>" 
                "due to the physical processes that form and maintain rings - they tend to settle into the equatorial plane due to the <br>" 
                "planet's rotational bulge. The other regular satellites of Neptune (like Proteus, Larissa, Galatea, and Despina) orbit <br>" 
                "in Neptune's equatorial plane, aligned with the rings. These inner moons play an important role in shepherding and <br>" 
                "maintaining the ring structure, particularly:<br>" 
                "* Galatea: This moon helps confine the Adams Ring and its distinctive arcs through orbital resonances.<br>" 
                "* Despina: Located near the Le Verrier Ring, it may help maintain its structure.<br>" 
                "* This misalignment between Triton and the rings/regular moons provides strong evidence for Triton's capture hypothesis <br>" 
                "  - it was likely an independent Kuiper Belt Object (similar to Pluto) that was captured by Neptune's gravity rather than <br>" 
                "  forming alongside Neptune like the other moons.<br>" 
                "* The contrast between the orderly, equatorial system of rings and regular moons versus Triton's highly inclined <br>" 
                "  orbit represents two different formation mechanisms in the same planetary system."
            )
        },
        
        'unnamed_dusty_ring': {
            'inner_radius_km': 67500,  # Inner edge (in km from Neptune's center)
            'outer_radius_km': 73000,  # Outer edge (in km from Neptune's center) 
            'thickness_km': 2000,      # Approximate thickness
            'color': 'rgb(100, 150, 200)',  # Bluish tint for dusty ring
            'opacity': 0.1,
            'name': 'Outer Dusty Ring',
            'description': (
                "Outer Dusty Ring: A faint, diffuse ring extending beyond the Adams Ring.<br>" 
                "* Located approximately 67,500-73,000 km from Neptune's center.<br>" 
                "* Very faint and difficult to observe, composed primarily of microscopic dust particles.<br>" 
                "* May be fed by impacts on Neptune's small inner moons.<br>"
                "* Discovery: First hinted at in Voyager 2 data, later confirmed by Earth-based observations.<br><br>"
                "Unlike Triton, Neptune's rings lie in Neptune's equatorial plane, as is typical for planetary ring systems. This is <br>" 
                "due to the physical processes that form and maintain rings - they tend to settle into the equatorial plane due to the <br>" 
                "planet's rotational bulge. The other regular satellites of Neptune (like Proteus, Larissa, Galatea, and Despina) orbit <br>" 
                "in Neptune's equatorial plane, aligned with the rings. These inner moons play an important role in shepherding and <br>" 
                "maintaining the ring structure, particularly:<br>" 
                "* Galatea: This moon helps confine the Adams Ring and its distinctive arcs through orbital resonances.<br>" 
                "* Despina: Located near the Le Verrier Ring, it may help maintain its structure.<br>" 
                "* This misalignment between Triton and the rings/regular moons provides strong evidence for Triton's capture hypothesis <br>" 
                "  - it was likely an independent Kuiper Belt Object (similar to Pluto) that was captured by Neptune's gravity rather than <br>" 
                "  forming alongside Neptune like the other moons.<br>" 
                "* The contrast between the orderly, equatorial system of rings and regular moons versus Triton's highly inclined <br>" 
                "  orbit represents two different formation mechanisms in the same planetary system."
            )
        }
    }
    
    # Unpack center position
    center_x, center_y, center_z = center_position
    
    # Neptune's axial tilt in radians (28.32 degrees)
    neptune_tilt = np.radians(28.32)
    
    # Neptune's pole direction (J2000)
    pole_ra = np.radians(299.36)  # Right ascension in radians
    pole_dec = np.radians(43.46)  # Declination in radians
    
    # Create traces for each ring
    for ring_name, ring_info in ring_params.items():
        # Convert km to AU
        inner_radius_au = ring_info['inner_radius_km'] / KM_PER_AU
        outer_radius_au = ring_info['outer_radius_km'] / KM_PER_AU
        thickness_au = ring_info['thickness_km'] / KM_PER_AU
        
        # For arc segments, generate partial rings
        if 'arc_length' in ring_info and 'arc_center' in ring_info:
            # Create arc points
            arc_length = ring_info['arc_length']  # Arc length in degrees
            arc_center = ring_info['arc_center']  # Center angle of the arc in degrees
            
            # Calculate arc start and end angles
            arc_start = np.radians(arc_center - arc_length/2)
            arc_end = np.radians(arc_center + arc_length/2)
            
            # Generate points along the arc
            n_points = int(arc_length * 10)  # 10 points per degree for smoothness
            theta = np.linspace(arc_start, arc_end, n_points)
            
            # Generate radial points
            n_radial = 5  # Number of radial points
            
            x = []
            y = []
            z = []
            
            for r in np.linspace(inner_radius_au, outer_radius_au, n_radial):
                for t in theta:
                    x.append(r * np.cos(t))
                    y.append(r * np.sin(t))
                    z.append(0)  # Start in xy-plane
                    
                    # Add thickness in z-direction
                    for h in np.linspace(-thickness_au/2, thickness_au/2, 3):
                        if h != 0:  # Skip duplicate points
                            x.append(r * np.cos(t))
                            y.append(r * np.sin(t))
                            z.append(h)
            
        else:
            # Create complete ring points
            n_points = 100  # Fewer points for outer dusty rings to improve performance
            if 'dusty' in ring_name:
                n_points = 80
                
            # Create ring points
            x, y, z = create_ring_points_saturn(
                inner_radius_au, outer_radius_au, n_points, thickness_au
            )
        
        # Convert to numpy arrays for rotation
        x = np.array(x)
        y = np.array(y)
        z = np.array(z)
        
        # TRANSFORMATION APPROACH:
        # Neptune's pole is oriented at RA=299.36 deg, DEC=43.46 deg
        # We'll use a transformation sequence to correctly orient the rings
        
        # Step 1: Rotate around z-axis by the Right Ascension
    #    x_rot1, y_rot1, z_rot1 = rotate_points(x, y, z, pole_ra, 'z')
        
        # Step 2: Rotate around x-axis by (90 deg - Declination)
        # This aligns the z-axis with Neptune's pole
    #    x_rot2, y_rot2, z_rot2 = rotate_points(x_rot1, y_rot1, z_rot1, np.radians(90) - pole_dec, 'x')
        
        # Step 3: Apply final adjustment based on Neptune's specific orientation
        # This 25 deg rotation adjusts for the reference frame of Neptune's ring observations
    #    x_final, y_final, z_final = rotate_points(x_rot2, y_rot2, z_rot2, np.radians(25), 'z')

        # SIMPLIFIED TRANSFORMATION:
        # Instead of using RA/Dec-based transformations, we'll use a direct alignment
        # to match what we see in the image with Despina and Galatea's orbits
        
        # Transform ring coordinates to align with Neptune's equatorial plane
        # These angles were empirically determined to match the orbital plane of Despina and Galatea
        # First rotation: 32 deg around x-axis provides the primary tilt 
        tilt_angle = np.radians(32)
        x_rot1, y_rot1, z_rot1 = rotate_points(x, y, z, tilt_angle, 'x')

        # Second rotation: 34 deg around z-axis aligns with the final orientation
        final_orientation = np.radians(34)
        x_final, y_final, z_final = rotate_points(x_rot1, y_rot1, z_rot1, final_orientation, 'z')
        
        # Apply center position offset
        x_final = x_final + center_x
        y_final = y_final + center_y
        z_final = z_final + center_z
        
        # Create hover text
        text_array = [ring_info['description']] * len(x)
        
        # Add ring trace
        traces.append(
            go.Scatter3d(
                x=x_final,
                y=y_final,
                z=z_final,
                mode='markers',
                marker=dict(
                    size=1.5,  # Small markers for rings
                    color=ring_info['color'],
                    opacity=ring_info['opacity']
                ),
                name=f"Neptune: {ring_info['name']}",
                text=text_array,
                customdata=[f"Neptune: {ring_info['name']}"] * len(x),
                hovertemplate='%{text}<extra></extra>',
                showlegend=True
            )
        )
    
    sun_traces = create_sun_direction_indicator(
        center_position=center_position, 
        shell_radius=73000 / KM_PER_AU
    )
    for trace in sun_traces:
        traces.append(trace)

    return traces

neptune_hill_sphere_info = (
            "SELECT MANUAL SCALE OF AT LEAST 1.0 AU TO VISUALIZE.\n" 
            "1.3 MB PER FRAME FOR HTML.\n\n"

            "Neptune's Hill sphere is the region around the planet where its gravitational influence dominates over that of the Sun. \n" 
            "Any moon or other object orbiting Neptune within this sphere is more likely to remain bound to it rather than being pulled \n" 
            "away by the Sun's gravity. Neptune's Hill sphere extends to a staggering approximately 4685 times the radius of Neptune. \n" 
            "This vast gravitational influence allows Neptune to retain its large system of moons, including the distant and unusual \n" 
            "irregular satellites."                     
)

def create_neptune_hill_sphere_shell(center_position=(0, 0, 0)):
    """Creates neptune's Hill sphere shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 4685, 
        'color': 'rgb(0, 255, 0)',  # Green for Hill sphere
        'opacity': 0.25,
        'name': 'Hill Sphere',
        'description': (
            "SET MANUAL SCALE OF AT LEAST 0.3 AU TO VISUALIZE.<br><br>"
            "Neptune's Hill sphere is the region around the planet where its gravitational influence dominates over that of the Sun. <br>" 
            "Any moon or other object orbiting Neptune within this sphere is more likely to remain bound to it rather than being pulled <br>" 
            "away by the Sun's gravity. Neptune's Hill sphere extends to a staggering approximately 4685 times the radius of Neptune. <br>" 
            "This vast gravitational influence allows Neptune to retain its large system of moons, including the distant and unusual <br>" 
            "irregular satellites."          )
    }
        
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * NEPTUNE_RADIUS_AU
    
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
            name=f"Neptune: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Neptune: {layer_info['name']}"] * len(x),
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