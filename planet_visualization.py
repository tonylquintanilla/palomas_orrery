"""
Celestial Body Visualization Module
==================================
Functions for creating layered visualizations of solar system bodies (Sun, planets) in 3D plots.
Each celestial body has individual shell components that can be toggled with selection variables.
"""

import math
import numpy as np
import plotly.graph_objs as go
from constants_new import (
    KM_PER_AU, LIGHT_MINUTES_PER_AU, KNOWN_ORBITAL_PERIODS,
    CENTER_BODY_RADII,
    # Sun information texts
    gravitational_influence_info_hover,
    outer_oort_info_hover,
    inner_oort_info_hover,
    inner_limit_oort_info_hover,
    solar_wind_info_hover,
    termination_shock_info_hover,
    outer_corona_info_hover,
    inner_corona_info_hover,
    chromosphere_info_hover,
    photosphere_info_hover,
    radiative_zone_info_hover,
    core_info_hover
)

#####################################
# Celestial Body Constants
#####################################

# Solar Constants
SOLAR_RADIUS_AU = 0.00465047  # Sun's radius in AU
CORE_AU = 0.00093               # Core in AU, approximately 0.2 Solar radii
RADIATIVE_ZONE_AU = 0.00325     # Radiative zone in AU, approximately 0.7 Solar radii
CHROMOSPHERE_RADII = 1.5    # Chromosphere extends to about 1.5 solar radii
INNER_CORONA_RADII = 3  # Inner corona extends to 2-3 solar radii
OUTER_CORONA_RADII = 50  # Outer corona extends up to 50 solar radii
TERMINATION_SHOCK_AU = 94  # Termination shock boundary in AU
HELIOPAUSE_RADII = 26449  # Heliopause at about 123 AU
INNER_LIMIT_OORT_CLOUD_AU = 2000  # Inner Oort cloud boundary in AU
INNER_OORT_CLOUD_AU = 20000  # Inner Oort cloud outer boundary in AU
OUTER_OORT_CLOUD_AU = 100000  # Outer Oort cloud boundary in AU
GRAVITATIONAL_INFLUENCE_AU = 126000  # Sun's gravitational influence in AU
# Constants
KM_PER_AU = 149597870.7  # Conversion factor from km to AU

# Mercury Constants
MERCURY_RADIUS_KM = 2440  # Mean radius in km
MERCURY_RADIUS_AU = MERCURY_RADIUS_KM / 149597870.7  # Convert to AU

# Venus Constants
VENUS_RADIUS_KM = 6052  # Mean radius in km
VENUS_RADIUS_AU = VENUS_RADIUS_KM / 149597870.7  # Convert to AU

# Earth Constants
EARTH_RADIUS_KM = 6371  # Mean radius in km
EARTH_RADIUS_AU = EARTH_RADIUS_KM / 149597870.7  # Convert to AU

# Mars Constants
MARS_RADIUS_KM = 3396.2  # JPL uses an equipotential virtual surface with a mean radius at the equator as the Mars datum. 
MARS_RADIUS_AU = MARS_RADIUS_KM / 149597870.7  # Convert to AU

# Jupiter Constants
JUPITER_RADIUS_KM = 71492  # Equatorial radius in km
JUPITER_RADIUS_AU = JUPITER_RADIUS_KM / 149597870.7  # Convert to AU

# Saturn Constants
SATURN_RADIUS_KM = 58232  # Equatorial radius in km
SATURN_RADIUS_AU = SATURN_RADIUS_KM / 149597870.7  # Convert to AU

#####################################
# Shared Utility Functions
#####################################


def rotate_points(x, y, z, angle, axis='x'):
    """
    Rotate points around a specified axis by the given angle.
    
    Parameters:
        x, y, z (arrays): Coordinates of points
        angle (float): Rotation angle in radians
        axis (str): Axis of rotation ('x', 'y', or 'z')
        
    Returns:
        tuple: (x_rotated, y_rotated, z_rotated)
    """
    # Create rotation matrices
    if axis == 'x':
        # Rotation around x-axis
        rot_matrix = np.array([
            [1, 0, 0],
            [0, np.cos(angle), -np.sin(angle)],
            [0, np.sin(angle), np.cos(angle)]
        ])
    elif axis == 'y':
        # Rotation around y-axis
        rot_matrix = np.array([
            [np.cos(angle), 0, np.sin(angle)],
            [0, 1, 0],
            [-np.sin(angle), 0, np.cos(angle)]
        ])
    elif axis == 'z':
        # Rotation around z-axis
        rot_matrix = np.array([
            [np.cos(angle), -np.sin(angle), 0],
            [np.sin(angle), np.cos(angle), 0],
            [0, 0, 1]
        ])
    
    # Stack coordinates into a single array
    points = np.vstack((x, y, z))
    
    # Apply rotation
    rotated_points = np.dot(rot_matrix, points)
    
    # Unpack results
    x_rotated = rotated_points[0, :]
    y_rotated = rotated_points[1, :]
    z_rotated = rotated_points[2, :]
    
    return x_rotated, y_rotated, z_rotated

def create_hover_markers_for_planet(center_position, radius, color, name, description, num_points=40):
    """
    Creates clean hover markers for a planet with proper hover text formatting.
    This is a helper function to ensure consistent hover behavior across static and animated views.
    """
    import math
    import numpy as np
    import plotly.graph_objects as go
    
    # Unpack center position
    center_x, center_y, center_z = center_position
    
    # Fibonacci sphere algorithm for even distribution
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
    fib_points = fibonacci_sphere(samples=num_points)
    
    # Scale and offset the points
    x_hover = [p[0] * radius + center_x for p in fib_points]
    y_hover = [p[1] * radius + center_y for p in fib_points]
    z_hover = [p[2] * radius + center_z for p in fib_points]
    
    # Create hover markers with clean hover text
    hover_trace = go.Scatter3d(
        x=x_hover, 
        y=y_hover, 
        z=z_hover,
        mode='markers',
        marker=dict(
            size=3,
            color=color,
            opacity=0.5
        ),
        name=f"{name} (Info)",
        text=[description] * len(x_hover),  # Array of identical description strings
        hoverinfo='text',  # Use only the text for hover
        showlegend=False
    )
    
    return hover_trace

# Revised create_celestial_body_visualization function for planet_visualization.py
# This ensures consistent animation support for all celestial bodies

def create_celestial_body_visualization(fig, body_name, shell_vars, animate=False, frames=None, center_position=(0, 0, 0)):
    """
    Unified function to create shell visualizations for any celestial body (Sun or planets).
    Ensures consistent animation support across all body types.
    
    Parameters:
        fig (plotly.graph_objects.Figure): The figure to add the visualization to
        body_name (str): Name of the celestial body ('Sun', 'Earth', 'Jupiter', etc.)
        shell_vars (dict): Dictionary of selection variables for each body's shells
        animate (bool): Whether this is for an animated plot
        frames (list, optional): List of frames for animation
        center_position (tuple): (x, y, z) position of the body's center
        
    Returns:
        plotly.graph_objects.Figure: The updated figure
    """
    print(f"\nCreating visualization for {body_name} (animate={animate})")
    
    # Create shell traces based on selected variables
    traces = []
    
    if body_name == 'Sun':
        # Handle Sun visualization with its specific shells
        for shell_name, var in shell_vars.items():
            if var.get() == 1:
                # Call the appropriate shell creation function based on name
                if shell_name == 'core' and var.get() == 1:
                    traces.extend(create_sun_core_shell())
                elif shell_name == 'radiative' and var.get() == 1:
                    traces.extend(create_sun_radiative_shell())
                elif shell_name == 'photosphere' and var.get() == 1:
                    traces.extend(create_sun_photosphere_shell())
                elif shell_name == 'chromosphere' and var.get() == 1:
                    traces.extend(create_sun_chromosphere_shell())
                elif shell_name == 'inner_corona' and var.get() == 1:
                    traces.extend(create_sun_inner_corona_shell())
                elif shell_name == 'outer_corona' and var.get() == 1:
                    traces.extend(create_sun_outer_corona_shell())
                elif shell_name == 'termination_shock' and var.get() == 1:
                    traces.extend(create_sun_termination_shock_shell())
                elif shell_name == 'heliopause' and var.get() == 1:
                    traces.extend(create_sun_heliopause_shell())
                elif shell_name == 'inner_oort_limit' and var.get() == 1:
                    traces.extend(create_sun_inner_oort_limit_shell())
                elif shell_name == 'inner_oort' and var.get() == 1:
                    traces.extend(create_sun_inner_oort_shell())
                elif shell_name == 'outer_oort' and var.get() == 1:
                    traces.extend(create_sun_outer_oort_shell())
                elif shell_name == 'gravitational' and var.get() == 1:
                    traces.extend(create_sun_gravitational_shell())
    
    elif body_name == 'Mercury':
        # Handle Mercury visualization with its specific shells
        for shell_name, var in shell_vars.items():
            if var.get() == 1:
                shell_type = shell_name.replace('mercury_', '')
                if shell_type == 'inner_core' and var.get() == 1:
                    traces.extend(create_mercury_inner_core_shell(center_position))
                elif shell_type == 'outer_core' and var.get() == 1:
                    traces.extend(create_mercury_outer_core_shell(center_position))
                elif shell_type == 'mantle' and var.get() == 1:
                    traces.extend(create_mercury_mantle_shell(center_position))
                elif shell_type == 'crust' and var.get() == 1:
                    traces.extend(create_mercury_crust_shell(center_position))
                elif shell_type == 'atmosphere' and var.get() == 1:
                    traces.extend(create_mercury_atmosphere_shell(center_position))
                elif shell_type == 'magnetosphere' and var.get() == 1:
                    traces.extend(create_mercury_magnetosphere_shell(center_position))
                elif shell_type == 'hill_sphere' and var.get() == 1:
                    traces.extend(create_mercury_hill_sphere_shell(center_position))

    elif body_name == 'Venus':
        # Handle Venus visualization with its specific shells
        for shell_name, var in shell_vars.items():
            if var.get() == 1:
                shell_type = shell_name.replace('venus_', '')
                if shell_type == 'core' and var.get() == 1:
                    traces.extend(create_venus_core_shell(center_position))
                elif shell_type == 'mantle' and var.get() == 1:
                    traces.extend(create_venus_mantle_shell(center_position))
                elif shell_type == 'crust' and var.get() == 1:
                    traces.extend(create_venus_crust_shell(center_position))
                elif shell_type == 'atmosphere' and var.get() == 1:
                    traces.extend(create_venus_atmosphere_shell(center_position))
                elif shell_type == 'upper_atmosphere' and var.get() == 1:
                    traces.extend(create_venus_upper_atmosphere_shell(center_position))
                elif shell_type == 'magnetosphere' and var.get() == 1:
                    traces.extend(create_venus_magnetosphere_shell(center_position))
                elif shell_type == 'hill_sphere' and var.get() == 1:
                    traces.extend(create_venus_hill_sphere_shell(center_position))

    elif body_name == 'Earth':
        # Handle Earth visualization with its specific shells
        for shell_name, var in shell_vars.items():
            if var.get() == 1:
                shell_type = shell_name.replace('earth_', '')
                if shell_type == 'inner_core' and var.get() == 1:
                    traces.extend(create_earth_inner_core_shell(center_position))
                elif shell_type == 'outer_core' and var.get() == 1:
                    traces.extend(create_earth_outer_core_shell(center_position))
                elif shell_type == 'lower_mantle' and var.get() == 1:
                    traces.extend(create_earth_lower_mantle_shell(center_position))
                elif shell_type == 'upper_mantle' and var.get() == 1:
                    traces.extend(create_earth_upper_mantle_shell(center_position))
                elif shell_type == 'crust' and var.get() == 1:
                    traces.extend(create_earth_crust_shell(center_position))
                elif shell_type == 'atmosphere' and var.get() == 1:
                    traces.extend(create_earth_atmosphere_shell(center_position))
                elif shell_type == 'upper_atmosphere' and var.get() == 1:
                    traces.extend(create_earth_upper_atmosphere_shell(center_position))
                elif shell_type == 'magnetosphere' and var.get() == 1:
                    traces.extend(create_earth_magnetosphere_shell(center_position))
                elif shell_type == 'hill_sphere' and var.get() == 1:
                    traces.extend(create_earth_hill_sphere_shell(center_position))
    
    elif body_name == 'Mars':
        # Handle Mars visualization with its specific shells
        for shell_name, var in shell_vars.items():
            if var.get() == 1:
                shell_type = shell_name.replace('mars_', '')
                if shell_type == 'inner_core' and var.get() == 1:
                    traces.extend(create_mars_inner_core_shell(center_position))
                elif shell_type == 'outer_core' and var.get() == 1:
                    traces.extend(create_mars_outer_core_shell(center_position))
                elif shell_type == 'mantle' and var.get() == 1:
                    traces.extend(create_mars_mantle_shell(center_position))
                elif shell_type == 'crust' and var.get() == 1:
                    traces.extend(create_mars_crust_shell(center_position))
                elif shell_type == 'atmosphere' and var.get() == 1:
                    traces.extend(create_mars_atmosphere_shell(center_position))
                elif shell_type == 'upper_atmosphere' and var.get() == 1:
                    traces.extend(create_mars_upper_atmosphere_shell(center_position))
                elif shell_type == 'hill_sphere' and var.get() == 1:
                    traces.extend(create_mars_hill_sphere_shell(center_position))

    elif body_name == 'Jupiter':
        # Handle Jupiter visualization with its specific shells
        for shell_name, var in shell_vars.items():
            if var.get() == 1:
                shell_type = shell_name.replace('jupiter_', '')
                if shell_type == 'core' and var.get() == 1:
                    traces.extend(create_jupiter_core_shell(center_position))
                elif shell_type == 'metallic_hydrogen' and var.get() == 1:
                    traces.extend(create_jupiter_metallic_hydrogen_shell(center_position))
                elif shell_type == 'molecular_hydrogen' and var.get() == 1:
                    traces.extend(create_jupiter_molecular_hydrogen_shell(center_position))
                elif shell_type == 'cloud_layer' and var.get() == 1:
                    traces.extend(create_jupiter_cloud_layer_shell(center_position))
                elif shell_type == 'upper_atmosphere' and var.get() == 1:
                    traces.extend(create_jupiter_upper_atmosphere_shell(center_position))
                elif shell_type == 'ring_system' and var.get() == 1:
                    traces.extend(create_jupiter_ring_system(center_position))
                elif shell_type == 'radiation_belts' and var.get() == 1:
                    traces.extend(create_jupiter_radiation_belts(center_position))
                elif shell_type == 'io_plasma_torus' and var.get() == 1:
                    traces.extend(create_jupiter_io_plasma_torus(center_position))
                elif shell_type == 'magnetosphere' and var.get() == 1:
                    traces.extend(create_jupiter_magnetosphere(center_position))
                elif shell_type == 'hill_sphere' and var.get() == 1:
                    traces.extend(create_jupiter_hill_sphere_shell(center_position))

    elif body_name == 'Saturn':
        # Handle Saturn visualization with its specific shells
        for shell_name, var in shell_vars.items():
            if var.get() == 1:
                shell_type = shell_name.replace('saturn_', '')
                if shell_type == 'core' and var.get() == 1:
                    traces.extend(create_saturn_core_shell(center_position))
                elif shell_type == 'metallic_hydrogen' and var.get() == 1:
                    traces.extend(create_saturn_metallic_hydrogen_shell(center_position))
                elif shell_type == 'molecular_hydrogen' and var.get() == 1:
                    traces.extend(create_saturn_molecular_hydrogen_shell(center_position))
                elif shell_type == 'cloud_layer' and var.get() == 1:
                    traces.extend(create_saturn_cloud_layer_shell(center_position))
                elif shell_type == 'upper_atmosphere' and var.get() == 1:
                    traces.extend(create_saturn_upper_atmosphere_shell(center_position))
                elif shell_type == 'ring_system' and var.get() == 1:
                    traces.extend(create_saturn_ring_system(center_position))
                elif shell_type == 'radiation_belts' and var.get() == 1:
                    traces.extend(create_saturn_radiation_belts(center_position))
                elif shell_type == 'io_plasma_torus' and var.get() == 1:
                    traces.extend(create_saturn_enceladus_plasma_torus(center_position))
                elif shell_type == 'magnetosphere' and var.get() == 1:
                    traces.extend(create_saturn_magnetosphere(center_position))
                elif shell_type == 'hill_sphere' and var.get() == 1:
                    traces.extend(create_saturn_hill_sphere_shell(center_position))

    else:
        print(f"Warning: No visualization available for {body_name}")
        return fig
    
    # Apply consistent animation handling for all bodies
    print(f"Created {len(traces)} traces for {body_name}")
    
    # Add traces to the figure
    for trace in traces:
        fig.add_trace(trace)
    
    # IMPORTANT: Skip adding to frames completely
    if animate and frames is not None:
        print(f"Animation mode: Added {len(traces)} traces to figure only (skipping frames)")
    
    return fig

def create_sphere_points(radius, n_points=50):
    """
    Create points for a sphere surface to represent celestial body layers.
    
    Parameters:
        radius (float): Radius of the sphere in AU
        n_points (int): Number of points to generate along each dimension
        
    Returns:
        tuple: (x, y, z) coordinates as flattened arrays
    """
    phi = np.linspace(0, 2*np.pi, n_points)
    theta = np.linspace(-np.pi/2, np.pi/2, n_points)
    phi, theta = np.meshgrid(phi, theta)

    x = radius * np.cos(theta) * np.cos(phi)
    y = radius * np.cos(theta) * np.sin(phi)
    z = radius * np.sin(theta)
    
    return x.flatten(), y.flatten(), z.flatten()

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


#####################################
# Sun Visualization Functions
#####################################

def create_sun_visualization(fig, sun_shell_vars, animate=False, frames=None):
    """
    Creates a visualization of the Sun's layers based on which shells are selected.
    
    Parameters:
        fig (plotly.graph_objects.Figure): The figure to add the Sun visualization to
        sun_shell_vars (dict): Dictionary of selection variables for each Sun shell
        animate (bool): Whether this is for an animated plot
        frames (list, optional): List of frames for animation
        
    Returns:
        plotly.graph_objects.Figure: The updated figure
    """
    # Create base traces for static visualization
    def create_layer_traces():
        traces = []
        
        # Add each selected shell based on the selection variables
        # Order from outermost to innermost
        if sun_shell_vars['gravitational'].get() == 1:
            traces.extend(create_sun_gravitational_shell())
            
        if sun_shell_vars['outer_oort'].get() == 1:
            traces.extend(create_sun_outer_oort_shell())
            
        if sun_shell_vars['inner_oort'].get() == 1:
            traces.extend(create_sun_inner_oort_shell())
            
        if sun_shell_vars['inner_oort_limit'].get() == 1:
            traces.extend(create_sun_inner_oort_limit_shell())
            
        if sun_shell_vars['heliopause'].get() == 1:
            traces.extend(create_sun_heliopause_shell())
            
        if sun_shell_vars['termination_shock'].get() == 1:
            traces.extend(create_sun_termination_shock_shell())
            
        if sun_shell_vars['outer_corona'].get() == 1:
            traces.extend(create_sun_outer_corona_shell())
            
        if sun_shell_vars['inner_corona'].get() == 1:
            traces.extend(create_sun_inner_corona_shell())
            
        if sun_shell_vars['chromosphere'].get() == 1:
            traces.extend(create_sun_chromosphere_shell())
            
        if sun_shell_vars['photosphere'].get() == 1:
            traces.extend(create_sun_photosphere_shell())
            
        if sun_shell_vars['radiative'].get() == 1:
            traces.extend(create_sun_radiative_shell())
            
        if sun_shell_vars['core'].get() == 1:
            traces.extend(create_sun_core_shell())
        
        return traces

    # Add base traces to figure
    traces = create_layer_traces()
    for trace in traces:
        fig.add_trace(trace)

    # If this is for animation, add the traces to each frame
    if animate and frames is not None:
        for frame in frames:
            frame_data = list(frame.data)  # Convert tuple to list if necessary
            frame_data.extend(traces)
            frame.data = frame_data

    return fig

# Individual Sun shell creation functions

def create_sun_gravitational_shell():
    """Creates the Sun's gravitational influence shell."""
    x, y, z = create_sphere_points(GRAVITATIONAL_INFLUENCE_AU, n_points=40)
    
    text_array = [gravitational_influence_info_hover for _ in range(len(x))]
    customdata_array = ["Sun's Gravitational Influence" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=1.0,
                color='rgb(102, 187, 106)', 
                opacity=0.2
            ),
            name='Sun\'s Gravitational Influence',
            text=text_array,             
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    ]
    
    return traces

def create_sun_outer_oort_shell():
    """Creates the Sun's outer Oort cloud shell."""
    x, y, z = create_sphere_points(OUTER_OORT_CLOUD_AU, n_points=40)
    
    text_array = [outer_oort_info_hover for _ in range(len(x))]
    customdata_array = ["Outer Oort Cloud" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=1.0,
                color='white',
                opacity=0.2
            ),
            name='Outer Oort Cloud',
            text=text_array,
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    ]
    
    return traces

def create_sun_inner_oort_shell():
    """Creates the Sun's inner Oort cloud shell."""
    x, y, z = create_sphere_points(INNER_OORT_CLOUD_AU, n_points=40)
    
    text_array = [inner_oort_info_hover for _ in range(len(x))]
    customdata_array = ["Inner Oort Cloud" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=1.0,
                color='white',
                opacity=0.3
            ),
            name='Inner Oort Cloud',
            text=text_array,
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    ]
    
    return traces

def create_sun_inner_oort_limit_shell():
    """Creates the inner limit of the Sun's Oort cloud shell."""
    x, y, z = create_sphere_points(INNER_LIMIT_OORT_CLOUD_AU, n_points=40)
    
    text_array = [inner_limit_oort_info_hover for _ in range(len(x))]
    customdata_array = ["Inner Limit of Oort Cloud" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=1.0,
                color='white',
                opacity=0.3
            ),
            name='Inner Limit of Oort Cloud',
            text=text_array,
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    ]
    
    return traces

def create_sun_heliopause_shell():
    """Creates the Sun's heliopause shell."""
    x, y, z = create_sphere_points(HELIOPAUSE_RADII * SOLAR_RADIUS_AU, n_points=40)
    
    text_array = [solar_wind_info_hover for _ in range(len(x))]
    customdata_array = ["Solar Wind Heliopause" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=0.5,
                color='rgb(135, 206, 250)',
                opacity=0.2
            ),
            name='Solar Wind Heliopause',
            text=text_array,
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    ]
    
    return traces

def create_sun_termination_shock_shell():
    """Creates the Sun's termination shock shell."""
    x, y, z = create_sphere_points(TERMINATION_SHOCK_AU, n_points=40)
    
    text_array = [termination_shock_info_hover for _ in range(len(x))]
    customdata_array = ["Solar Wind Termination Shock" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=0.5,
                color='rgb(240, 244, 255)',
                opacity=0.2
            ),
            name='Solar Wind Termination Shock',
            text=text_array,
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    ]
    
    return traces

def create_sun_outer_corona_shell():
    """Creates the Sun's outer corona shell."""
    x, y, z = create_sphere_points(OUTER_CORONA_RADII * SOLAR_RADIUS_AU, n_points=50)
    
    text_array = [outer_corona_info_hover for _ in range(len(x))]
    customdata_array = ["Sun: Outer Corona" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=0.75,
                color='rgb(25, 25, 112)',
                opacity=0.3
            ),
            name='Sun: Outer Corona',
            text=text_array,
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    ]
    
    return traces

def create_sun_inner_corona_shell():
    """Creates the Sun's inner corona shell."""
    x, y, z = create_sphere_points(INNER_CORONA_RADII * SOLAR_RADIUS_AU, n_points=60)
    
    text_array = [inner_corona_info_hover for _ in range(len(x))]
    customdata_array = ["Sun: Inner Corona" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=1,
                color='rgb(0, 0, 255)',
                opacity=0.09
            ),
            name='Sun: Inner Corona',
            text=text_array,
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    ]
    
    return traces

def create_sun_chromosphere_shell():
    """Creates the Sun's chromosphere shell."""
    x, y, z = create_sphere_points(CHROMOSPHERE_RADII * SOLAR_RADIUS_AU, n_points=60)
    
    text_array = [chromosphere_info_hover for _ in range(len(x))]
    customdata_array = ["Sun: Chromosphere" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=1.25,
                color='rgb(30, 144, 255)',
                opacity=0.10
            ),
            name='Sun: Chromosphere',
            text=text_array,
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    ]
    
    return traces

def create_sun_photosphere_shell():
    """Creates the Sun's photosphere shell."""
    x, y, z = create_sphere_points(SOLAR_RADIUS_AU, n_points=60)
    
    text_array = [photosphere_info_hover for _ in range(len(x))]
    customdata_array = ["Sun: Photosphere" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=7.0,
                color='rgb(255, 244, 214)',
                opacity=1.0
            ),
            name='Sun: Photosphere',
            text=text_array,
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    ]
    
    return traces

def create_sun_radiative_shell():
    """Creates the Sun's radiative zone shell."""
    x, y, z = create_sphere_points(RADIATIVE_ZONE_AU, n_points=60)
    
    text_array = [radiative_zone_info_hover for _ in range(len(x))]
    customdata_array = ["Sun: Radiative Zone" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=7,
                color='rgb(30, 144, 255)',
                opacity=1.0
            ),
            name='Sun: Radiative Zone',
            text=text_array,
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    ]
    
    return traces

def create_sun_core_shell():
    """Creates the Sun's core shell."""
    x, y, z = create_sphere_points(CORE_AU, n_points=60)
    
    text_array = [core_info_hover for _ in range(len(x))]
    customdata_array = ["Sun: Core" for _ in range(len(x))]
    
    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=10,
                color='rgb(70, 130, 180)',
                opacity=1.0
            ),
            name='Sun: Core',
            text=text_array,
            customdata=customdata_array,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        ),
    ]
    
    return traces

#####################################
# Planet Visualization Functions
#####################################

def create_planet_visualization(fig, planet_name, shell_vars, animate=False, frames=None, center_position=(0, 0, 0)):
    """
    Creates a visualization of a planet's layers based on which shells are selected.
    Works for both static plots and animations.
    
    Parameters:
        fig (plotly.graph_objects.Figure): The figure to add the visualization to
        planet_name (str): Name of the planet 
        shell_vars (dict): Dictionary of selection variables for each planet shell
        animate (bool): Whether this is for an animated plot
        frames (list, optional): List of frames for animation
        center_position (tuple): (x, y, z) position of the planet's center
        
    Returns:
        plotly.graph_objects.Figure: The updated figure
    """
    # Create base traces for static visualization
    traces = []
    
    # Create shell traces based on selected variables

    if planet_name == 'Mercury':
        if shell_vars['mercury_inner_core'].get() == 1:
            traces.extend(create_mercury_inner_core_shell(center_position))
        if shell_vars['mercury_outer_core'].get() == 1:
            traces.extend(create_mercury_outer_core_shell(center_position))
        if shell_vars['mercury_mantle'].get() == 1:
            traces.extend(create_mercury_mantle_shell(center_position))
        if shell_vars['mercury_crust'].get() == 1:
            traces.extend(create_mercury_crust_shell(center_position))
        if shell_vars['mercury_atmosphere'].get() == 1:
            traces.extend(create_mercury_atmosphere_shell(center_position))
        if shell_vars['mercury_magnetosphere'].get() == 1:
            traces.extend(create_mercury_magnetosphere_shell(center_position))
        if shell_vars['mercury_hill_sphere'].get() == 1:
            traces.extend(create_mercury_hill_sphere_shell(center_position))

    if planet_name == 'Venus':
        if shell_vars['venus_core'].get() == 1:
            traces.extend(create_venus_core_shell(center_position))
        if shell_vars['venus_mantle'].get() == 1:
            traces.extend(create_venus_mantle_shell(center_position))
        if shell_vars['venus_crust'].get() == 1:
            traces.extend(create_venus_crust_shell(center_position))
        if shell_vars['venus_atmosphere'].get() == 1:
            traces.extend(create_venus_atmosphere_shell(center_position))
        if shell_vars['venus_upper_atmosphere'].get() == 1:
            traces.extend(create_venus_upper_atmosphere_shell(center_position))
        if shell_vars['venus_magnetosphere'].get() == 1:
            traces.extend(create_venus_magnetosphere_shell(center_position))
        if shell_vars['venus_hill_sphere'].get() == 1:
            traces.extend(create_venus_hill_sphere_shell(center_position))

    if planet_name == 'Earth':
        if shell_vars['earth_inner_core'].get() == 1:
            traces.extend(create_earth_inner_core_shell(center_position))
        if shell_vars['earth_outer_core'].get() == 1:
            traces.extend(create_earth_outer_core_shell(center_position))
        if shell_vars['earth_lower_mantle'].get() == 1:
            traces.extend(create_earth_lower_mantle_shell(center_position))
        if shell_vars['earth_upper_mantle'].get() == 1:
            traces.extend(create_earth_upper_mantle_shell(center_position))
        if shell_vars['earth_crust'].get() == 1:
            traces.extend(create_earth_crust_shell(center_position))
        if shell_vars['earth_atmosphere'].get() == 1:
            traces.extend(create_earth_atmosphere_shell(center_position))
        if shell_vars['earth_upper_atmosphere'].get() == 1:
            traces.extend(create_earth_upper_atmosphere_shell(center_position))
        if shell_vars['earth_magnetosphere'].get() == 1:
            traces.extend(create_earth_magnetosphere_shell(center_position))
        if shell_vars['earth_hill_sphere'].get() == 1:
            traces.extend(create_earth_hill_sphere_shell(center_position))

    if planet_name == 'Mars':
        if shell_vars['mars_inner_core'].get() == 1:
            traces.extend(create_mars_inner_core_shell(center_position))
        if shell_vars['mars_outer_core'].get() == 1:
            traces.extend(create_mars_outer_core_shell(center_position))
        if shell_vars['mars_mantle'].get() == 1:
            traces.extend(create_mars_mantle_shell(center_position))
        if shell_vars['mars_crust'].get() == 1:
            traces.extend(create_mars_crust_shell(center_position))
        if shell_vars['mars_atmosphere'].get() == 1:
            traces.extend(create_mars_atmosphere_shell(center_position))
        if shell_vars['mars_upper_atmosphere'].get() == 1:
            traces.extend(create_mars_upper_atmosphere_shell(center_position))
        if shell_vars['mars_hill_sphere'].get() == 1:
            traces.extend(create_mars_hill_sphere_shell(center_position))

    if planet_name == 'Jupiter':
        if shell_vars['jupiter_core'].get() == 1:
            traces.extend(create_jupiter_core_shell(center_position))
        if shell_vars['jupiter_metallic_hydrogen'].get() == 1:
            traces.extend(create_jupiter_metallic_hydrogen_shell(center_position))
        if shell_vars['jupiter_molecular_hydrogen'].get() == 1:
            traces.extend(create_jupiter_molecular_hydrogen_shell(center_position))
        if shell_vars['jupiter_cloud_layer'].get() == 1:
            traces.extend(create_jupiter_cloud_layer_shell(center_position))
        if shell_vars['jupiter_upper_atmosphere'].get() == 1:
            traces.extend(create_jupiter_upper_atmosphere_shell(center_position))
        if shell_vars['jupiter_ring_system'].get() == 1:
            traces.extend(create_jupiter_ring_system(center_position))
        if shell_vars['jupiter_radiation_belts'].get() == 1:
            traces.extend(create_jupiter_radiation_belts(center_position))
        if shell_vars['jupiter_io_plasma_torus'].get() == 1:
            traces.extend(create_jupiter_io_plasma_torus(center_position))
        if shell_vars['jupiter_magnetosphere'].get() == 1:
            traces.extend(create_jupiter_magnetosphere(center_position))
        if shell_vars['jupiter_hill_sphere'].get() == 1:
            traces.extend(create_jupiter_hill_sphere_shell(center_position))

    if planet_name == 'Saturn':
        if shell_vars['saturn_core'].get() == 1:
            traces.extend(create_saturn_core_shell(center_position))
        if shell_vars['saturn_metallic_hydrogen'].get() == 1:
            traces.extend(create_saturn_metallic_hydrogen_shell(center_position))
        if shell_vars['saturn_molecular_hydrogen'].get() == 1:
            traces.extend(create_saturn_molecular_hydrogen_shell(center_position))
        if shell_vars['saturn_cloud_layer'].get() == 1:
            traces.extend(create_saturn_cloud_layer_shell(center_position))
        if shell_vars['saturn_upper_atmosphere'].get() == 1:
            traces.extend(create_saturn_upper_atmosphere_shell(center_position))
        if shell_vars['saturn_ring_system'].get() == 1:
            traces.extend(create_saturn_ring_system(center_position))
        if shell_vars['saturn_radiation_belts'].get() == 1:
            traces.extend(create_saturn_radiation_belts(center_position))
        if shell_vars['saturn_enceladus_plasma_torus'].get() == 1:
            traces.extend(create_saturn_enceladus_plasma_torus(center_position))
        if shell_vars['saturn_magnetosphere'].get() == 1:
            traces.extend(create_saturn_magnetosphere(center_position))
        if shell_vars['saturn_hill_sphere'].get() == 1:
            traces.extend(create_saturn_hill_sphere_shell(center_position))
    
    # Add base traces to figure for static visualization
    for trace in traces:
        fig.add_trace(trace)

    # If this is for animation, add the traces to each frame
    if animate and frames is not None:
        for frame in frames:
            frame_data = list(frame.data)  # Convert tuple to list if necessary
            frame_data.extend(traces)
            frame.data = frame_data

    return fig

def create_planet_shell_traces(planet_name, shell_vars, center_position=(0, 0, 0)):
    """
    Creates traces for planet shells without adding them to a figure.
    Useful for animations where traces need to be created for each frame.
    
    Parameters:
        planet_name (str): Name of the planet
        shell_vars (dict): Dictionary of selection variables for each planet shell
        center_position (tuple): (x, y, z) position of the planet's center
        
    Returns:
        list: List of plotly traces
    """
    traces = []
    
    # Get the prefix for this planet's shell variables
    prefix = planet_name.lower() + "_"
    
    # Check each shell variable and add corresponding traces if selected
    for shell_name, var in shell_vars.items():
        if var.get() == 1:
            # Extract the actual shell name without the planet prefix
            shell_type = shell_name.replace(prefix, "")
            
            # Dynamically call the appropriate shell creation function
            creation_func_name = f"create_{planet_name.lower()}_{shell_type}_shell"
            if creation_func_name in globals():
                creation_func = globals()[creation_func_name]
                new_traces = creation_func(center_position=center_position)
                traces.extend(new_traces)
            else:
                print(f"Warning: No creation function found for {shell_type} shell of {planet_name}")
    
    # Fix the hovertemplate for all traces
    for trace in traces:
        # Ensure proper customdata for hovering
        if hasattr(trace, 'customdata'):
            if isinstance(trace.customdata, list):
                # Make sure all customdata items reference the correct planet
                trace.customdata = [str(item).replace("Mercury", planet_name).replace("Venus", planet_name).replace("Earth", planet_name)
                                    .replace("Mars", planet_name).replace("Jupiter", planet_name).replace("Saturn", planet_name) 
                              if "Mercury" in str(item) or "Venus" in str(item) or "Earth" in str(item)
                                or "Mars" in str(item) or "Jupiter" in str(item) or "Saturn" in str(item) 
                              else str(item) for item in trace.customdata]
        
        # Set correct hovertemplate
        trace.hovertemplate = '%{text}<extra></extra>'
    
    return traces

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
    
    return traces

mercury_magnetosphere_info = (
            "SET MANUAL SCALE TO AT LEAST 0.01 AU TO VISUALIZE.\n\n" 

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
                      "but a typical sunward distance to the bow shock is estimated to be around 1.4 to 2.0 radii from the center of Mercury."]
    
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
        
    return traces

mercury_hill_sphere_info = (
            "SET MANUAL SCALE TO AT LEAST 0.02 AU TO VISUALIZE.\n\n" 
            "Hill Sphere: Every celestial body has a Hill sphere (also known as the Roche sphere), which is the region around it \n" 
            "where its gravity is the dominant gravitational force. Mercury certainly has a Hill sphere, but its size depends on \n" 
            "its mass and its distance from the Sun. Being the closest planet to the Sun, the Sun's powerful gravity limits the \n" 
            "extent of Mercury's Hill sphere compared to planets farther out."
)

def create_mercury_hill_sphere_shell(center_position=(0, 0, 0)):
    """Creates Mercury's Hill sphere."""
    # Hill sphere radius in Mercury radii
    radius_fraction = 72  # Mercury's Hill sphere is about 235 Mercury radii
    
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
    hover_text = ["Hill Sphere: Every celestial body has a Hill sphere (also known as the Roche sphere), which is the region around it <br>" 
                "where its gravity is the dominant gravitational force. Mercury certainly has a Hill sphere, but its size depends on <br>" 
                "its mass and its distance from the Sun. Being the closest planet to the Sun, the Sun's powerful gravity limits the <br>" 
                "extent of Mercury's Hill sphere compared to planets farther out.<br><br>" 
                "The Hill sphere is the region around a where its own gravity is the dominant force in attracting satellites. For <br>" 
                "a planet orbiting a star, it's the region where the planet's gravity is stronger than the star's tidal forces."]
    
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
                opacity=0.15
            ),
            name='Mercury: Hill Sphere',
            text=[hover_text] * len(x),
            customdata=['Mercury: Hill Sphere'] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

# Venus Shell Creation Functions

venus_core_info = (
            "Scientists infer that Venus has a central core, likely composed primarily of iron and nickel, similar to Earth's. \n" 
            "Its radius is estimated to be around 3,000 km. Due to the lack of a strong magnetic field, it's speculated that Venus's \n" 
            "core might be solid or only partially liquid, or that it lacks the internal convection that drives Earth's magnetic \n" 
            "field. The exact state and dynamics of Venus's core remain a topic of ongoing research."
)

def create_venus_core_shell(center_position=(0, 0, 0)):
    """Creates Venus's core shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 0.5,  # Inner core: 0-50% of Venus's radius
        'color': 'rgb(255, 180, 140)',  # Orange-red for hot iron core
        'opacity': 1.0,
        'name': 'Core',
        'description': (
            "Scientists infer that Venus has a central core, likely composed primarily of iron and nickel, similar to Earth's. <br>" 
            "Its radius is estimated to be around 3,000 km. Due to the lack of a strong magnetic field, it's speculated that Venus's <br>" 
            "core might be solid or only partially liquid, or that it lacks the internal convection that drives Earth's magnetic <br>" 
            "field. The exact state and dynamics of Venus's core remain a topic of ongoing research."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * VENUS_RADIUS_AU
    
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
            name=f"Venus: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Venus: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

venus_mantle_info = (
            "Surrounding the core is a mantle made of hot, dense silicate rock, much like Earth's mantle. It's believed that heat \n" 
            "generated by radioactive decay within Venus drives slow convection currents in the mantle. These currents are thought \n" 
            "to be responsible for the planet's volcanism and tectonic activity, albeit different from Earth's plate tectonics"
)

def create_venus_mantle_shell(center_position=(0, 0, 0)):
    """Creates Venus's mantle shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 0.98,  # Lower mantle: 50-98% of Venus's radius; actually it is nearly 100%, but representing as 98%
        'color': 'rgb(230, 100, 20)',  # Reddish-brown
        'opacity': 0.7,
        'name': 'Mantle',
        'description': (
            "Surrounding the core is a mantle made of hot, dense silicate rock, much like Earth's mantle. It's believed that heat <br>" 
            "generated by radioactive decay within Venus drives slow convection currents in the mantle. These currents are thought <br>" 
            "to be responsible for the planet's volcanism and tectonic activity, albeit different from Earth's plate tectonics"
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * VENUS_RADIUS_AU
    
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
            name=f"Venus: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Venus: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces
    
venus_crust_info = (
            "Venus has a crust primarily made of basalt rock, with an estimated thickness ranging from about 10 to 30 kilometers, \n" 
            "possibly thicker in the highland regions. Unlike Earth, Venus does not appear to have plate tectonics. Instead, its \n" 
            "surface is mostly a single, continuous plate. The heat from the mantle escapes through volcanic activity, which is \n" 
            "widespread across the planet, leading to periodic resurfacing events on a global scale."
)

def create_venus_crust_shell(center_position=(0, 0, 0)):
    """Creates Venus's crust shell using Mesh3d for better performance with improved hover."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 1.0,  # Crust: 100% of Venus's radius
        'color': 'rgb(255, 255, 224)',  
        'opacity': 1.0,
        'name': 'Crust',
        'description': (
            "Venus Crust<br>" 
            "(Note: toggle off the crust layer in the legend to better see the interior structure.)<br><br>"
            "Venus has a crust primarily made of basalt rock, with an estimated thickness ranging from about 10 to 30 kilometers, <br>" 
            "possibly thicker in the highland regions. Unlike Earth, Venus does not appear to have plate tectonics. Instead, its <br>" 
            "surface is mostly a single, continuous plate. The heat from the mantle escapes through volcanic activity, which is <br>" 
            "widespread across the planet, leading to periodic resurfacing events on a global scale."
        )
    }
    
    # Calculate radius in AU
    radius = layer_info['radius_fraction'] * VENUS_RADIUS_AU
    
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
        name=f"Venus: {layer_info['name']}",
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
    layer_name = f"Venus: {layer_info['name']}"
    minimal_hover_texts = [layer_name] * len(x_hover)

    # Create hover trace with direct text assignment
    hover_trace = go.Scatter3d(
        x=x_hover, 
        y=y_hover, 
        z=z_hover,
        mode='markers',
        marker=dict(
            size=2,  # originally 5
            color='rgb(255, 255, 224)',  # Layer color
            opacity=1.0,  # originally 0.8
            line=dict(  # Add a contrasting outline
                width=1,
                color='black'
            )
        ),
        name=f"Venus: {layer_info['name']} (Info)",
        text=hover_texts,  # IMPORTANT: Matching length with coordinate arrays
        customdata=minimal_hover_texts,  # For "Object Names Only" mode
        hovertemplate='%{text}<extra></extra>',  # Use the standard hover template
        showlegend=False  # Don't show in legend since it's just for hover
    )

    return [surface_trace, hover_trace]

venus_atmosphere_info = (
            "Venus boasts an extremely dense atmosphere, about 90 times the pressure of Earth's atmosphere at the surface. It is \n" 
            "composed primarily of carbon dioxide (about 96.5%) and nitrogen (about 3.5%), with trace amounts of other gases, \n" 
            "including sulfuric acid clouds that completely enshroud the planet. This thick, CO₂-rich atmosphere creates a runaway \n" 
            "greenhouse effect, making Venus the hottest planet in our solar system with surface temperatures around 464°C. The \n" 
            "upper atmosphere exhibits a phenomenon called \"super-rotation,\" where winds blow much faster than the planet's slow \n" 
            "rotation."
)

def create_venus_atmosphere_shell(center_position=(0, 0, 0)):
    """Creates Venus's lower atmosphere shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 1.02,  # Troposphere; actually only about 1% but displayed as 2% for visibility
        'color': 'rgb(150, 200, 255)',  # Light blue for atmosphere
        'opacity': 0.5,
        'name': 'Lower Atmosphere',
        'description': (
            "Venus boasts an extremely dense atmosphere, about 90 times the pressure of Earth's atmosphere at the surface. It is <br>" 
            "composed primarily of carbon dioxide (about 96.5%) and nitrogen (about 3.5%), with trace amounts of other gases, <br>" 
            "including sulfuric acid clouds that completely enshroud the planet. This thick, CO₂-rich atmosphere creates a runaway <br>" 
            "greenhouse effect, making Venus the hottest planet in our solar system with surface temperatures around 464°C. The <br>" 
            "upper atmosphere exhibits a phenomenon called \"super-rotation,\" where winds blow much faster than the planet's slow <br>" 
            "rotation.<br><br>"
            "The \"lower atmosphere\" of Venus is generally considered to be the troposphere, which extends from the surface up to \n" 
            "an altitude of approximately 60 kilometers. This region contains the dense, hot air and the main cloud layers."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * VENUS_RADIUS_AU
    
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
            name=f"Venus: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Venus: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

venus_upper_atmosphere_info = (
            "In summary, the upper atmosphere of Venus is a significant region:\n" 
            "* The mesosphere occupies roughly 1.5-1.6% of Venus's radius.\n" 
            "* The thermosphere extends to at least 3.3% of Venus's radius.\n" 
            "* The ionosphere spans a considerable range within the thermosphere and exosphere, potentially reaching about 8% or \n" 
            "  more of Venus's radius for significant charged particle densities. The exosphere gradually fades out into space."
)

def create_venus_upper_atmosphere_shell(center_position=(0, 0, 0)):
    """Creates Venus's upper atmosphere shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 1.08,  # Mesosphere, thermosphere, and exosphere
        'color': 'rgb(100, 150, 255)',  # Lighter blue
        'opacity': 0.3,
        'name': 'Upper Atmosphere',
        'description': (
            "The upper atmosphere of Venus is a complex and dynamic region extending far beyond the troposphere. It doesn't have the <br>" 
            "same distinct layers (stratosphere, mesosphere, thermosphere) as Earth's in the same way due to the very different thermal <br>" 
            "structure and composition. However, we can broadly consider the regions above the main cloud deck (around 70 km) as the <br>" 
            "upper atmosphere. Here's a look at some key parts of the upper atmosphere and their approximate extents:<br>" 
            "* Mesosphere (approximately 60 km to 90-100 km): Above the main cloud layers, the temperature starts to decrease with <br>" 
            "  altitude. This region is considered the mesosphere. It's a transition zone between the lower, rapidly rotating atmosphere <br>" 
            "  and the upper atmosphere where solar radiation plays a more dominant role. Extent in Venus radii: The top of this layer is <br>" 
            "  around 90-100 km. So, the mesosphere extends up to about 1.5-1.6% of Venus's radius.<br>" 
            "* Thermosphere (approximately 90-100 km to 200+ km): Above the mesosphere, the temperature increases significantly with <br>" 
            "  altitude due to the absorption of solar extreme ultraviolet (EUV) radiation. This is the thermosphere. Unlike Earth's <br>" 
            "  thermosphere, Venus's thermosphere is surprisingly cold, with average temperatures around 300 K (27°C), and even colder on <br>" 
            "  the night side (the \"cryosphere\" around 90-120 km can reach extremely low temperatures). This is due to efficient <br>" 
            "  radiative cooling by carbon dioxide. The thermosphere is also where significant day-night differences in temperature and <br>" 
            "  density occur due to Venus's slow rotation. A global circulation pattern moves hot air from the dayside to the nightside <br>" 
            "  at high altitudes. Extent in Venus radii: The thermosphere extends to at least 200 km, and potentially much higher, gradually <br>" 
            "  thinning into the exosphere. So, the thermosphere extends to at least 3.3% of Venus's radius.<br>" 
            "* Ionosphere (approximately 120 km to several hundred km): Within the thermosphere and extending into the exosphere lies the <br>" 
            "  ionosphere, a region where solar radiation has ionized the atmospheric gases, creating a layer of charged particles (ions <br>" 
            "  and electrons). Venus has a substantial ionosphere, with peak electron densities occurring around 120-140 km altitude. The <br>" 
            "  ionosphere plays a crucial role in interacting with the solar wind, as Venus lacks a strong global magnetic field.<br>" 
            "  * The solar wind directly impacts the ionosphere, leading to the formation of an induced magnetosphere.<br>" 
            "  * The nightside ionosphere is more variable and less dense than the dayside ionosphere, but it can extend to very high <br>" 
            "    altitudes, even forming a long, comet-like tail under certain solar wind conditions.<br>" 
            "  Extent in Venus radii: The main part of the ionosphere extends from about 120 km to several hundred kilometers. If we <br>" 
            "  consider an upper limit of, say, 500 km for a significant ionospheric density: So, the ionosphere can extend up to about 8.3% <br>" 
            "  of Venus's radius. However, the outermost fringes can be even more extended.<br>" 
            "* Exosphere (extends from where the atmosphere is very thin outwards into space): The uppermost layer of Venus's atmosphere <br>" 
            "  is the exosphere, where the gas density is so low that atoms and molecules can escape into space. The boundary between the <br>" 
            "  thermosphere and exosphere (the exobase) is not sharply defined but is generally considered to be above where collisions <br>" 
            "  between particles become infrequent. This is likely several hundred kilometers above the surface. The exosphere gradually <br>" 
            "  fades into space and interacts directly with the solar wind. Extent in Venus radii: The exosphere has no well-defined upper <br>" 
            "  limit. It extends outwards until the planet's gravity is no longer the dominant force.<br>" 
            "In summary, the upper atmosphere of Venus is a significant region:<br>" 
            "* The mesosphere occupies roughly 1.5-1.6% of Venus's radius.<br>" 
            "* The thermosphere extends to at least 3.3% of Venus's radius.<br>" 
            "* The ionosphere spans a considerable range within the thermosphere and exosphere, potentially reaching about 8% or more of <br>" 
            "  Venus's radius for significant charged particle densities.<br>" 
            "* The exosphere gradually fades out into space. It's important to remember that these are approximate extents, and the <br>" 
            "  boundaries between these regions are not always sharp and can vary with solar activity and other factors. The upper <br>" 
            "  atmosphere of Venus is a subject of ongoing research, and future missions will undoubtedly refine our understanding of <br>" 
            "  its structure and dynamics."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * VENUS_RADIUS_AU
    
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
            name=f"Venus: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Venus: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

venus_magnetosphere_info = (
            "SET MANUAL SCALE TO AT LEAST 0.01 AU TO VISUALIZE.\n\n" 

            "Venus has a very weak, induced magnetosphere. Unlike Earth's magnetic field, which is generated internally by its \n" 
            "liquid iron core, Venus's weak magnetosphere is formed by the interaction of the solar wind with the planet's \n" 
            "ionosphere (the upper layer of its atmosphere containing charged particles). This induced magnetosphere is not as \n" 
            "effective at deflecting charged particles from the Sun as Earth's strong magnetic field."
)

def create_venus_magnetosphere_shell(center_position=(0, 0, 0)):
    """Creates Venus's magnetosphere."""
    traces = []
    
    # Parameters for magnetosphere components (in Venus radii)
    params = {
        # Compressed sunward side
        'sunward_distance': 1.5,  # Compressed toward the sun
        
        # Equatorial extension (wider than polar)
        'equatorial_radius': 1.0,
        'polar_radius': 1.0,
        
        # Magnetotail parameters
        'tail_length': 60,  # Length of visible magnetotail
        'tail_base_radius': 1.5,  # Radius at the base of the tail
        'tail_end_radius': 30,  # Radius at the end of the tail
        
        # Radiation belts
    #    'inner_belt_distance': 1.5,  # Distance in Earth radii
    #    'outer_belt_distance': 4.5,  # Distance in Earth radii
    #    'belt_thickness': 0.5,
    }
    
    # Scale everything by Venus's radius in AU
    for key in params:
        params[key] *= VENUS_RADIUS_AU
    
    # Create magnetosphere main shape
    x, y, z = create_magnetosphere_shape(params)
    
    # Unpack center position
    center_x, center_y, center_z = center_position
    
    # 1. Add the main magnetosphere structure
    x = np.array(x) + center_x
    y = np.array(y) + center_y
    z = np.array(z) + center_z
    
    magnetosphere_text = ["Venus has a very weak, induced magnetosphere. Unlike Earth's magnetic field, which is generated internally by its <br>" 
            "liquid iron core, Venus's weak magnetosphere is formed by the interaction of the solar wind with the planet's <br>" 
            "ionosphere (the upper layer of its atmosphere containing charged particles). This induced magnetosphere is not as <br>" 
            "effective at deflecting charged particles from the Sun as Earth's strong magnetic field.<br><br>" 
            "The solar wind's magnetic field drapes around Venus, creating a comet-shaped magnetosphere with a bow shock on the <br>" 
            "sunward side and a long magnetotail extending away from the Sun. The extent of Venus's induced magnetosphere is highly <br>" 
            "variable and depends on the strength and direction of the solar wind.<br>" 
            "* Bow Shock: The bow shock, which is the outermost boundary where the supersonic solar wind is slowed and deflected by <br>" 
            "  Venus, typically stands off a few thousand kilometers above the dayside surface. At the subsolar point (the point <br>" 
            "  directly facing the Sun), it's often located around about 1.3 to 1.7 radii from the planet's center. However, this <br>" 
            "  distance can vary significantly with solar wind conditions.<br>" 
            "* Magnetopause: The magnetopause is the inner boundary of the magnetosphere, where the magnetic pressure of the induced <br>" 
            "  magnetosphere balances the pressure of the shocked solar wind. On the dayside, the magnetopause is typically found much <br>" 
            "  closer to the planet than the bow shock, often around 1.05 to 1.1 radii from the planet's center during solar minimum <br>" 
            "  conditions. It can be pushed closer to the planet during periods of high solar wind pressure.<br>" 
            "* Magnetotail: The magnetotail extends far downstream from Venus, in the anti-sunward direction. Its length is much more <br>" 
            "  variable and can stretch to many Venus radii. Some observations have suggested that the magnetotail can extend to at <br>" 
            "  least ∼45 radii and possibly even further during active solar wind conditions.<br>" 
            "  * Estimating the precise base radius and end radius of Venus's induced magnetotail is challenging due to its dynamic <br>" 
            "    nature and dependence on the ever-changing solar wind conditions. Unlike Earth's magnetotail, which is anchored by <br>" 
            "    a strong internal magnetic field, Venus's magnetotail is constantly being shaped and influenced by the solar wind <br>" 
            "    flow and the interplanetary magnetic field (IMF).<br>" 
            "    * Base Radius: The \"base\" of the magnetotail can be considered the region just behind Venus where the induced <br>" 
            "      magnetosphere forms a tail-like structure. This transition region is not a sharp boundary but rather a gradual <br>" 
            "      change in plasma and magnetic field characteristics. Near Venus, the magnetotail has a somewhat cylindrical or <br>" 
            "      lobed structure. Studies using Venus Express data have estimated the typical radius of the near-Venus magnetotail <br>" 
            "      to be around 1 to 1.5 Venus radii.<br>" 
            "    * End Radius (Length): The length of Venus's magnetotail is highly variable and can extend to significant distances <br>" 
            "      downstream. Recent flybys by spacecraft like Solar Orbiter have provided new insights into the far reaches of the <br>" 
            "      tail. Observations have detected the presence of the magnetotail and its boundaries (bow shock and induced <br>" 
            "      magnetospheric boundary) extending to at least 60 Venus radii (∼363,120 km) downstream. There is even some evidence <br>" 
            "      suggesting that under certain solar wind conditions, the tail might extend even further, possibly up to or beyond 100 <br>" 
            "      Venus radii. One study of Mariner 10 data suggested possible detection of the tail as far as ∼100 radii downstream. <br>" 
            "      * Dynamic Nature: The solar wind's pressure, speed, and the orientation of the IMF constantly buffet Venus's induced <br>" 
            "        magnetosphere, causing significant variations in its size and shape.<br>" 
            "      * Boundary Identification: Defining the exact outer boundary of the magnetotail can be challenging as the plasma <br>" 
            "        environment gradually transitions back to the solar wind.<br>" 
            "      * Limited Far-Tail Observations: While recent missions have provided valuable data, the far magnetotail of Venus has <br>" 
            "        not been as extensively sampled as Earth's.<br>" 
            "    * Estimating the width of Venus's magnetotail at distances of 45 to 60 Venus radii is challenging due to the <br>" 
            "      limited number of direct observations so far out in the tail. Most detailed studies have focused on the near-<br>" 
            "      Venus magnetotail (within ∼10 to 12 radii). However, recent flybys, particularly by Solar Orbiter, are providing <br>" 
            "      new insights.<br>" 
            "      * Overall Expansion: The induced magnetotail of Venus is known to flare or expand as it extends downstream from <br>" 
            "        the planet. This is a common feature of magnetotails formed by the interaction of the solar wind with a planetary <br>" 
            "        obstacle.<br>" 
            "      * Solar Orbiter Observations: A recent study based on Solar Orbiter flybys, which reached as far as 60 radii downstream, <br>" 
            "        suggests that the bow shock (the outer boundary) at this distance is about 15-20 radii in the lateral direction <br>" 
            "        (which would give a total width of roughly 30-40 radii if we assume some symmetry around the tail axis). The induced <br>" 
            "        magnetospheric boundary (IMB), which is inside the bow shock, was still detected at 20 radii downstream in this study, <br>" 
            "        but its width at larger distances was not specifically quantified.<br>" 
            "      * Earlier Estimates: Older studies based on Pioneer Venus Orbiter data, which primarily sampled the tail up to ∼12 radii, <br>" 
            "        found the tail to be about 4 radii wide and 3.2 radii high at that distance. Extrapolating this far out is difficult <br>" 
            "        due to the flaring. Therefore, a reasonable estimate for the width of Venus's magnetotail at 45 to 60 Venus radii <br>" 
            "        would likely be on the order of tens of Venus radii, possibly in the range of 20 to 40 radii or even wider, based on <br>" 
            "        the observed bow shock dimensions at that distance. The actual width can vary significantly depending on the solar <br>" 
            "        wind conditions (pressure, speed, IMF orientation). The shape of the tail might not be perfectly circular at these <br>" 
            "        large distances.<br>"
            "In summary, the extent of Venus's induced magnetosphere in terms of Venus radii is:<br>" 
            "* Dayside (from the center): Extends to roughly 1.3 - 1.7 radii at the bow shock and about 1.05 - 1.1 radii at the <br>" 
            "  magnetopause.<br>" 
            "* Nightside (magnetotail): Can extend to at least tens of Venus radii, with estimates reaching up to ∼45 radii or <br>" 
            "  more under certain solar wind conditions.<br>" 
            "The size and shape of Venus's induced magnetosphere are highly dynamic, constantly being shaped by the ever-changing <br>" 
            "solar wind."]
    
    magnetosphere_customdata = ['Venus: Magnetosphere']

    traces.append(
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=2.0,
                color='rgb(180, 180, 255)', # Light blue for magnetic field
                opacity=0.2
            ),
            name='Venus: Magnetosphere',
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
    bow_shock_standoff = 15 * VENUS_RADIUS_AU
    bow_shock_width = 25 * VENUS_RADIUS_AU
    
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
    
    bow_shock_text = ["Bow Shock: The bow shock, which is the outermost boundary where the supersonic solar wind is slowed and <br>" 
                      "deflected by Venus, typically stands off a few thousand kilometers above the dayside surface. At the subsolar <br>" 
                      "point (the point directly facing the Sun), it's often located around ∼0.3 to 0.7 radii above the surface, or <br>" 
                      "about 1.3 to 1.7 radii from the planet's center. However, this distance can vary significantly with solar wind <br>" 
                      "conditions."]
    
    bow_shock_customdata = ['Venus: Bow Shock']

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
            name='Venus: Bow Shock',
            text=bow_shock_text * len(bow_shock_x),
            customdata=bow_shock_customdata * len(bow_shock_x),  # This was the line causing the error
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    )
        
    return traces

venus_hill_sphere_info = (
            "SET MANUAL SCALE TO AT LEAST 0.02 AU TO VISUALIZE.\n\n" 
            "Venus's Hill Sphere is the region where its gravitational influence is dominant over the gravitational influence of \n" 
            "the Sun. The size of the Hill sphere depends on its mass and its distance from the Sun. Venus's Hill sphere extends \n" 
            "to approximately 1 million kilometers from the planet. Within this sphere, Venus's gravity is the primary force \n" 
            "attracting its own moons or any potential debris. However, Venus has no natural moons."
)

def create_venus_hill_sphere_shell(center_position=(0, 0, 0)):
    """Creates Venus's Hill sphere."""
    # Hill sphere radius in Venus radii
    radius_fraction = 166  # Venus's Hill sphere is about 1 million km or 166 Venus radii
    
    # Calculate radius in AU
    radius_au = radius_fraction * VENUS_RADIUS_AU
    
    # Create sphere points with fewer points for memory efficiency
    n_points = 30  # Reduced for large spheres
    x, y, z = create_sphere_points(radius_au, n_points=n_points)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    # Create hover text
    hover_text = "Venus's Hill Sphere (extends to ~166 Venus radii or about 1 million km)"
    
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
                opacity=0.15
            ),
            name='Venus: Hill Sphere',
            text=[hover_text] * len(x),
            customdata=['Venus: Hill Sphere'] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

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
                "from Earth on the Sun-facing side."]
    
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
    hover_text = "Earth's Hill Sphere (extends to ~235 Earth radii or about 1.5 million km)"
    
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
                opacity=0.15
            ),
            name='Earth: Hill Sphere',
            text=[hover_text] * len(x),
            customdata=['Earth: Hill Sphere'] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

# Mars Shell Creation Functions

mars_inner_core_info = (
            "A Solid Inner Core: Based on seismic data from the InSight lander, scientists have strong evidence that Mars \n" 
            "possesses a solid inner core. This inner core is primarily composed of iron and nickel, similar to Earth's."
)

def create_mars_inner_core_shell(center_position=(0, 0, 0)):
    """Creates Mars's inner core shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 0.5,  # Inner core: 0-50% of Mars's radius
        'color': 'rgb(255, 180, 140)',  # Orange-red for hot iron core
        'opacity': 1.0,
        'name': 'Inner Core',
        'description': (
            "A Solid Inner Core: Based on seismic data from the InSight lander, scientists have strong evidence that Mars <br>" 
            "possesses a solid inner core. This inner core is primarily composed of iron and nickel, similar to Earth's.<br><br>"
            "The differentiation into a solid inner core and a liquid outer core is primarily driven by:<br>"
            "* Temperature Gradient: The temperature increases significantly as you move towards the center of the planet. <br>" 
            "  The very high pressure at the center raises the melting point of the metallic core material. The inner core <br>" 
            "  is where the pressure exceeds the melting point at that temperature, forcing the metal into a solid state. <br>" 
            "  The outer core is still hot enough to be liquid at the prevailing pressures.<br>"
            "* Compositional Differences: The presence of lighter elements in the outer core also contributes to its lower <br>" 
            "  melting point compared to the purer iron-nickel of the inner core.<br>"
            "* Differences from Earth's Core:"
            "  * Size: Mars' core is proportionally larger relative to the planet's overall size compared to Earth's core.<br>"
            "  * Density: The lower overall density of Mars suggests that its core likely contains a higher percentage of <br>" 
            "    lighter elements than Earth's core.<br>" 
            "  * Lack of a Global Dynamo (Currently): Earth's liquid outer core is convecting, which, along with the planet's <br>" 
            "    rotation, generates our global magnetic field (the geodynamo). The fact that Mars currently lacks a global <br>" 
            "    magnetic field suggests that the convection in its liquid outer core is either absent, very weak, or organized <br>" 
            "    differently. This could be due to its smaller size, different cooling history, or the higher abundance of <br>" 
            "    lighter elements affecting its fluid dynamics.<br>" 
            "The precise composition and dynamics of these layers are still subjects of ongoing research and analysis of data.<br><br>" 
            "Past Magnetosphere: Scientists believe that early in its history, Mars did possess a global magnetic field, <br>" 
            "much like Earth's. This would have created a significant magnetosphere, deflecting much of the solar wind and <br>" 
            "cosmic radiation. However, unlike Earth, Mars lost its global magnetic field billions of years ago. The exact <br>" 
            "reasons are still being investigated, but theories involve the cooling and solidification of its iron core, which <br>" 
            "would have stopped the dynamo process that generates a global magnetic field. Today, Mars doesn't have a planet-wide <br>" 
            "magnetosphere generated by a global magnetic field. However, the Mars Global Surveyor mission discovered strong, <br>" 
            "localized magnetic fields embedded in certain regions of the Martian crust, particularly in the ancient southern <br>" 
            "highlands. These are remnants of the early global field. These localized fields can create small, localized <br>" 
            "magnetospheres, but they don't provide planet-wide protection like Earth's magnetosphere."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * MARS_RADIUS_AU
    
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
            name=f"Mars: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Mars: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

mars_outer_core_info = (
            "A Liquid Outer Core: Surrounding the solid inner core is believed to be a liquid outer core, also primarily \n" 
            "made of iron and nickel, but likely containing a significant amount of lighter elements like sulfur, oxygen, \n" 
            "or even hydrogen. The presence of these lighter elements would lower the melting point of the iron-nickel alloy, \n" 
            "allowing it to remain liquid despite the pressure."
)

def create_mars_outer_core_shell(center_position=(0, 0, 0)):
    """Creates Mars's outer core shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 0.8,  # Outer core: 50-80% of Mars's radius
        'color': 'rgb(255, 140, 0)',  # Deeper orange for liquid metal
        'opacity': 0.8,
        'name': 'Outer Core',
        'description': (
            "A Liquid Outer Core: Surrounding the solid inner core is believed to be a liquid outer core, also primarily <br>" 
            "made of iron and nickel, but likely containing a significant amount of lighter elements like sulfur, oxygen, <br>" 
            "or even hydrogen. The presence of these lighter elements would lower the melting point of the iron-nickel alloy, <br>" 
            "allowing it to remain liquid despite the pressure.<br><br>"
            "The differentiation into a solid inner core and a liquid outer core is primarily driven by:<br>"
            "* Temperature Gradient: The temperature increases significantly as you move towards the center of the planet. <br>" 
            "  The very high pressure at the center raises the melting point of the metallic core material. The inner core <br>" 
            "  is where the pressure exceeds the melting point at that temperature, forcing the metal into a solid state. <br>" 
            "  The outer core is still hot enough to be liquid at the prevailing pressures.<br>"
            "* Compositional Differences: The presence of lighter elements in the outer core also contributes to its lower <br>" 
            "  melting point compared to the purer iron-nickel of the inner core.<br>"
            "* Differences from Earth's Core:"
            "  * Size: Mars' core is proportionally larger relative to the planet's overall size compared to Earth's core.<br>"
            "  * Density: The lower overall density of Mars suggests that its core likely contains a higher percentage of <br>" 
            "    lighter elements than Earth's core.<br>" 
            "  * Lack of a Global Dynamo (Currently): Earth's liquid outer core is convecting, which, along with the planet's <br>" 
            "    rotation, generates our global magnetic field (the geodynamo). The fact that Mars currently lacks a global <br>" 
            "    magnetic field suggests that the convection in its liquid outer core is either absent, very weak, or organized <br>" 
            "    differently. This could be due to its smaller size, different cooling history, or the higher abundance of <br>" 
            "    lighter elements affecting its fluid dynamics.<br>" 
            "The precise composition and dynamics of these layers are still subjects of ongoing research and analysis of data."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * MARS_RADIUS_AU
    
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
            name=f"Mars: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Mars: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

mars_mantle_info = (
            "Mantle: Surrounding the core is a silicate mantle, similar to Earth's. It's composed of dense rocks rich in \n" 
            "elements like silicon, oxygen, iron, and magnesium."
)

def create_mars_mantle_shell(center_position=(0, 0, 0)):
    """Creates Mars's mantle shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 0.98,  # Upper mantle: 80-98% of Mars's radius
        'color': 'rgb(205, 85, 85)',  # Lighter reddish-brown
        'opacity': 0.6,
        'name': 'Mantle',
        'description': (
            "Mantle: Surrounding the core is a silicate mantle, similar to Earth's. It's composed of dense rocks rich in <br>" 
            "elements like silicon, oxygen, iron, and magnesium. While \"upper mantle\" isn't a formal layer name in the <br>" 
            "same way as Earth's, scientists do discuss different regions within the mantle based on mineral phase transitions <br>" 
            "that occur at different depths and pressures. For example, there might be an upper and lower transition zone <br>" 
            "within the mantle, similar in concept to Earth's, although the specific minerals and depths would differ due to <br>" 
            "Mars' unique composition and internal pressures."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * MARS_RADIUS_AU
    
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
            name=f"Mars: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Mars: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

mars_crust_info = (
            "Mars's crust: Mars has a crust, which is the outermost solid shell. Interestingly, recent findings from marsquakes \n" 
            "suggest that the Martian crust is significantly thicker than Earth's, perhaps averaging around 70 kilometers \n" 
            "(43 miles) or even thicker in some areas."
)

def create_mars_crust_shell(center_position=(0, 0, 0)):
    """Creates Mars's crust shell using Mesh3d for better performance with improved hover."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 1.0,  # Crust: 100% of Mars's radius
        'color': 'rgb(188, 39, 50)',  # Mars red
        'opacity': 1.0,
        'name': 'Crust',
        'description': (
            "Mars Crust<br>" 
            "(Note: toggle off the crust layer in the legend to better see the interior structure.)<br><br>" 
            "Mars has a crust, which is the outermost solid shell. Interestingly, recent findings from marsquakes <br>" 
            "suggest that the Martian crust is significantly thicker than Earth's, perhaps averaging around 70 kilometers <br>" 
            "(43 miles) or even thicker in some areas.<br><br>" 
            "Today, Mars doesn't have a planet-wide magnetosphere generated by a global magnetic field. However, the Mars Global <br>" 
            "Surveyor mission discovered strong, localized magnetic fields embedded in certain regions of the Martian crust, <br>" 
            "particularly in the ancient southern highlands. These are remnants of the early global field. These localized fields <br>" 
            "can create small, localized magnetospheres, but they don't provide planet-wide protection like Earth's magnetosphere."
        )
    }
    
    # Calculate radius in AU
    radius = layer_info['radius_fraction'] * MARS_RADIUS_AU
    
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
        name=f"Mars: {layer_info['name']}",
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
    layer_name = f"Mars: {layer_info['name']}"
    minimal_hover_texts = [layer_name] * len(x_hover)

    # Create hover trace with direct text assignment
    hover_trace = go.Scatter3d(
        x=x_hover, 
        y=y_hover, 
        z=z_hover,
        mode='markers',
        marker=dict(
            size=2,  # originally 5
            color='rgb(188, 39, 50)',  # Layer color, originally 'white'
            opacity=1.0,  # originally 0.8
            line=dict(  # Add a contrasting outline
                width=1,
                color='black'
            )
        ),
        name=f"Mars: {layer_info['name']} (Info)",
        text=hover_texts,  # IMPORTANT: Matching length with coordinate arrays
        customdata=minimal_hover_texts,  # For "Object Names Only" mode
        hovertemplate='%{text}<extra></extra>',  # Use the standard hover template
        showlegend=False  # Don't show in legend since it's just for hover
    )

    return [surface_trace, hover_trace]

mars_atmosphere_info = (
            "Atmosphere: Mars has a thin atmosphere, much less dense than Earth's. It's primarily composed of carbon dioxide \n" 
            "(about 95%), with small amounts of nitrogen, argon, and other gases."
)

def create_mars_atmosphere_shell(center_position=(0, 0, 0)):
    """Creates Mars's lower atmosphere shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 1.02,  # Troposphere
        'color': 'rgb(150, 200, 255)',  # Light blue for atmosphere
        'opacity': 0.5,
        'name': 'Lower Atmosphere',
        'description': (
            "Atmosphere: Mars has a thin atmosphere, much less dense than Earth's. It's primarily composed of carbon dioxide <br>" 
            "(about 95%), with small amounts of nitrogen, argon, and other gases.<br><br>" 
            "Scientists often divide the Martian atmosphere into layers based on temperature profiles, similar to Earth's <br>" 
            "atmosphere, although some layers are absent or behave differently:<br>" 
            "* Troposphere: This is the lowest layer, extending from the surface up to about 40-50 kilometers (25-31 miles). <br>" 
            "  Most of Mars' weather, like dust storms and convection, occurs here. The temperature generally decreases with altitude.<br>" 
            "* Mesosphere: Above the troposphere, extending from about 50 to 100 kilometers (31 to 62 miles). This layer has the <br>" 
            "  lowest temperatures in the Martian atmosphere as carbon dioxide efficiently radiates heat into space. Carbon dioxide <br>" 
            "  ice clouds have even been observed in the Martian mesosphere.<br>" 
            "* Thermosphere: Above the mesosphere, starting around 100 kilometers (62 miles) and extending to about 200 kilometers <br>" 
            "  (124 miles). This layer is heated by extreme ultraviolet radiation from the Sun, and temperatures increase with <br>" 
            "  altitude. However, it's still much colder than Earth's thermosphere."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * MARS_RADIUS_AU
    
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
            name=f"Mars: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Mars: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

mars_upper_atmosphere_info = (
            "Upper Atmosphere: Like Earth, Mars has upper atmospheric layers, including an ionosphere and exosphere, where \n" 
            "the atmosphere becomes very thin and interacts with solar radiation and the solar wind.\n\n" 
            "Exosphere: This is the outermost layer, starting above the thermosphere (around 200 km/124 miles) and gradually \n" 
            "thinning out into space. Atoms and molecules here are so far apart that they can escape the planet's gravity.\n\n" 
            "Interaction with Solar Wind: Without a global magnetosphere, the Martian atmosphere is directly exposed to the \n" 
            "solar wind, a stream of charged particles from the Sun. This interaction is believed to have played a significant \n" 
            "role in stripping away much of Mars' early, potentially thicker atmosphere and contributing to the loss of liquid \n" 
            "water on the surface. Unlike Earth, Mars lacks a stratosphere. On Earth, the stratosphere is characterized by a \n" 
            "temperature inversion due to the absorption of ultraviolet radiation by the ozone layer. Mars has a very thin \n" 
            "atmosphere and no significant ozone layer, so this distinct layer doesn't form."
)

def create_mars_upper_atmosphere_shell(center_position=(0, 0, 0)):
    """Creates Mars's upper atmosphere shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 1.06,  # Mesosphere, thermosphere, and exosphere
        'color': 'rgb(100, 150, 255)',  # Lighter blue
        'opacity': 0.3,
        'name': 'Upper Atmosphere',
        'description': (
            "Upper Atmosphere: Like Earth, Mars has upper atmospheric layers, including an ionosphere and exosphere, where <br>" 
            "the atmosphere becomes very thin and interacts with solar radiation and the solar wind.<br><br>" 
            "Exosphere: This is the outermost layer, starting above the thermosphere (around 200 km/124 miles) and gradually <br>" 
            "thinning out into space. Atoms and molecules here are so far apart that they can escape the planet's gravity.<br><br>" 
            "Interaction with Solar Wind: Without a global magnetosphere, the Martian atmosphere is directly exposed to the <br>" 
            "solar wind, a stream of charged particles from the Sun. This interaction is believed to have played a significant <br>" 
            "role in stripping away much of Mars' early, potentially thicker atmosphere and contributing to the loss of liquid <br>" 
            "water on the surface. Unlike Earth, Mars lacks a stratosphere. On Earth, the stratosphere is characterized by a <br>" 
            "temperature inversion due to the absorption of ultraviolet radiation by the ozone layer. Mars has a very thin <br>" 
            "atmosphere and no significant ozone layer, so this distinct layer doesn't form."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * MARS_RADIUS_AU
    
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
            name=f"Mars: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Mars: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

mars_hill_sphere_info = (
            "SET MANUAL SCALE TO AT LEAST 0.01 AU TO VISUALIZE.\n\n" 
            "Mars's Hill Sphere (extends to ~324.5 Mars radii or about 1.1 million km), which defines the region of its \n" 
            "gravitational influence and encompasses its two moons."
)

def create_mars_hill_sphere_shell(center_position=(0, 0, 0)):
    """Creates Mars's Hill sphere."""

    """Creates Mars's upper atmosphere shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 324.5,  
        'color': 'rgb(0, 255, 0)',  # Green for Hill sphere
        'opacity': 0.15,
        'name': 'Hill Sphere',
        'description': (
                "Mars's Hill Sphere (extends to ~324.5 Mars radii or about 1.1 million km), which defines the region of its <br>" 
                "gravitational influence and encompasses its two moons.<br><br>" 
                "* Definition: The Hill sphere (sometimes called the Roche sphere or gravitational sphere of influence) of a <br>" 
                "  celestial body is the region around it where its own gravity is the dominant force attracting satellites. <br>" 
                "  Essentially, it's the space where a moon or spacecraft would primarily orbit that body rather than the larger <br>" 
                "  body it orbits (in Mars' case, the Sun).<br>" 
                "* Mars' Hill Sphere: The size of a planet's Hill sphere depends on its mass and its distance from the Sun. <br>" 
                "  Mars, being less massive than Earth and farther from the Sun, has a Hill sphere with a radius of approximately <br>" 
                "  1.1 million kilometers (about 0.073 astronomical units).<br>" 
                "* Moons Within the Hill Sphere: Mars' two small moons, Phobos and Deimos, orbit well within Mars' Hill sphere, <br>" 
                "  which is why they are gravitationally bound to the planet and not the Sun.<br>" 
                "* Importance: The concept of the Hill sphere is crucial for understanding the stability of orbits around a planet. <br>" 
                "  Any object orbiting Mars within its Hill sphere is more likely to remain a satellite of Mars. If an object's <br>" 
                "  orbit extends beyond the Hill sphere, the Sun's gravity would become the dominant influence, potentially pulling <br>" 
                "the object into a heliocentric orbit."
        )
    }

    # Hill sphere radius in Mars radii
    radius_fraction = 324.5  # Mars's Hill sphere is about 324.5 Mars radii
    
    # Calculate radius in AU
    radius_au = radius_fraction * MARS_RADIUS_AU
    
    # Create sphere points with fewer points for memory efficiency
    n_points = 30  # Reduced for large spheres
    x, y, z = create_sphere_points(radius_au, n_points=n_points)
    
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
                size=1.0,
                color='rgb(0, 255, 0)',  # Green for Hill sphere
                opacity=0.15
            ),
            name=f"Mars: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Mars: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

# Jupiter Shell Creation Functions

jupiter_core_info = (
            "2.4 MB PER FRAME FOR HTML.\n\n"
            "Jupiter's core is believed to be a dense mixture of rock, metal, and hydrogen compounds.\n"
            "It may be up to 10 times the mass of Earth. Recent models suggest the core might be\n"
            "partially dissolved or 'fuzzy' rather than a distinct solid structure. Its temperature\n"
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
            name=f"Jupiter: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Jupiter: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

jupiter_metallic_hydrogen_info = (
            "2.1 MB PER FRAME FOR HTML.\n\n"
            "Under extreme pressure, hydrogen transitions to a metallic state in this layer.\n"
            "It behaves like an electrical conductor and is responsible for generating\n"
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
            name=f"Jupiter: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Jupiter: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

jupiter_molecular_hydrogen_info = (
            "2.5 MB PER FRAME FOR HTML.\n\n"
            "This layer consists of hydrogen in its molecular form. The transition from metallic\n"
            "to molecular hydrogen is gradual. This layer makes up the bulk of Jupiter's mass\n"
            "and is marked by decreasing temperature and pressure as you move outward. The temperature\n"
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
            name=f"Jupiter: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Jupiter: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

jupiter_cloud_layer_info = (
            "USE MANUAL SCALED OF 0.005 AU TO VIEW CLOSELY."
            "4.6 MB PER FRAME FOR HTML.\n\n"
            "Jupiter's visible cloud layer consists of bands of different colors, caused by\n"
            "variations in chemical composition and atmospheric dynamics. The clouds are primarily\n"
            "composed of ammonia, ammonium hydrosulfide, and water. The famous Great Red Spot\n"
            "is a massive storm system located in this layer. Temperature ranges from 120 K in\n" 
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
    layer_name = f"Jupiter: {layer_info['name']}"
    minimal_hover_texts = [layer_name] * len(x_hover)

    # Create hover trace with direct text assignment
    hover_trace = go.Scatter3d(
        x=x_hover, 
        y=y_hover, 
        z=z_hover,
        mode='markers',
        marker=dict(
            size=2,  # originally 5
            color='rgb(255, 255, 235)',  # Layer color, originally 'white'
            opacity=1.0,  # originally 0.8
            line=dict(  # Add a contrasting outline
                width=1,
                color='black'
            )
        ),
        name=f"Jupiter: {layer_info['name']} (Info)",
        text=hover_texts,  # IMPORTANT: Matching length with coordinate arrays
        customdata=minimal_hover_texts,  # For "Object Names Only" mode
        hovertemplate='%{text}<extra></extra>',  # Use the standard hover template
        showlegend=False  # Don't show in legend since it's just for hover
    )

    return [surface_trace, hover_trace]

jupiter_upper_atmosphere_info = (
            "2.7 MB PER FRAME FOR HTML.\n\n"
            "Jupiter's upper atmosphere includes the stratosphere and thermosphere.\n"
            "It's less dense than the cloud layer below and contains hydrocarbon haze\n"
            "produced by solar ultraviolet radiation. Aurora activity can be observed\n"
            "at Jupiter's poles, caused by interactions with its magnetic field. Temperature\n"
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
            name=f"Jupiter: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Jupiter: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

def create_jupiter_magnetosphere(center_position=(0, 0, 0)):
    """Creates Jupiter's main magnetosphere structure."""
    # Parameters for magnetosphere components (in Jupiter radii)
    params = {
        # Compressed sunward side
        'sunward_distance': 50,  # Compressed toward the sun
        
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
            name='Jupiter: Magnetosphere',
            text=["Jupiter's magnetosphere extends up to 100 Jupiter radii on the sunward side<br>"
                  "and forms a magnetotail stretching beyond Saturn's orbit in the opposite direction.<br>"
                  "It traps charged particles, creating intense radiation belts that would be lethal to humans."] * len(x),
            customdata=['Jupiter: Magnetosphere'] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

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
    io_text = ["Io plasma torus: A donut-shaped region of charged particles emanating from<br>"
              "Jupiter's moon Io due to volcanic activity. These particles become trapped<br>"
              "in Jupiter's magnetic field, forming this distinctive structure."] * len(io_torus_x)
    io_customdata = ['Jupiter: Io Plasma Torus'] * len(io_torus_x)
    
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
            text=io_text,
            customdata=io_customdata,
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

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
        belt_text = [belt_texts[i]] * len(belt_x)
        belt_customdata = [belt_names[i]] * len(belt_x)

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
                text=belt_text,
                customdata=belt_customdata,
                hovertemplate='%{text}<extra></extra>',
                showlegend=True
            )
        )
    
    return traces
    
def create_jupiter_hill_sphere_shell(center_position=(0, 0, 0)):
    """Creates Jupiter's Hill sphere shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 530,  # Jupiter's Hill sphere is about 530 Jupiter radii
        'color': 'rgb(0, 255, 0)',  # Green for Hill sphere
        'opacity': 0.3,
        'name': 'Hill Sphere',
        'description': (
            "SET MANUAL SCALE OF AT LEAST 0.3 AU TO VISUALIZE.<br><br>"
            "Jupiter's Hill Sphere (extends to ~530 Jupiter radii or about 0.25 AU)"
        )
    }
        
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * JUPITER_RADIUS_AU
    
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
            name=f"Jupiter: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Jupiter: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

jupiter_ring_system_info = (
                "22.2 MB PER FRAME FOR HTML.\n\n"

                "The main ring is reddish and composed of dust ejected from Jupiter's small inner moons,\n"
                "Metis and Adrastea, due to high-speed impacts by micrometeoroids.\n\n"

                "The Halo Ring is a faint, thick torus of material.\n"
                "The ring likely consists of fine dust particles pushed out of the main ring\n"
                "by electromagnetic forces from Jupiter's powerful magnetosphere.\n\n" 

                "The Amalthea Gossamer Ring is an extremely faint and wide ring.\n"
                "It is composed of dust particles ejected from Amalthea by micrometeoroid impacts.\n\n"   

                "The Thebe Gossamer Ring is another very faint and wide ring.\n"
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
        
        # Apply center position offset
        x = np.array(x) + center_x
        y = np.array(y) + center_y
        z = np.array(z) + center_z
        
        # Create a text list for hover information
        text_array = [ring_info['description'] for _ in range(len(x))]
        
        # Add ring trace
        traces.append(
            go.Scatter3d(
                x=x, y=y, z=z,
                mode='markers',
                marker=dict(
                    size=1.5,  # Small markers for rings
                    color=ring_info['color'],
                    opacity=ring_info['opacity']
                ),
                name=f"Jupiter: {ring_info['name']}",
                text=text_array,
                customdata=[f"Jupiter: {ring_info['name']}"] * len(x),
                hovertemplate='%{text}<extra></extra>',
                showlegend=True
            )
        )
    
    return traces

jupiter_magnetosphere_info = (
            "SELECT MANUAL SCALE OF AT LEAST 0.2 AU TO VISUALIZE.\n"
            "1.4 MB PER FRAME FOR HTML.\n\n"

            "Jupiter's magnetosphere extends up to 100 Jupiter radii on the sunward side\n"
            "and forms a magnetotail stretching beyond Saturn's orbit in the opposite direction.\n"
            "It traps charged particles, creating intense radiation belts that would be lethal to humans.\n\n"

            "Io plasma torus: A donut-shaped region of charged particles emanating from\n"
            "Jupiter's moon Io due to volcanic activity. These particles become trapped\n"
            "in Jupiter's magnetic field, forming this distinctive structure.\n\n"  

            "Inner radiation belt: Intense region of trapped high-energy particles near Jupiter\n"
            "Middle radiation belt: Region of trapped charged particles at intermediate distances from Jupiter\n"
            "Outer radiation belt: Extended region of trapped particles in Jupiter's outer magnetosphere"                      
)

def create_magnetosphere_shape(params):
    """
    Creates points for a magnetosphere with asymmetry, compressed on sunward side
    and extended on the tail side.
    
    Parameters:
        params (dict): Dictionary of shape parameters
        
    Returns:
        tuple: (x, y, z) coordinates as lists
    """
    x_coords = []
    y_coords = []
    z_coords = []
    
    # Number of points to generate (reduced for memory efficiency)
    n_phi = 20              # from 30 to 20
    n_theta = 20            # from 30 to 20
    n_tail_segments = 10    # from 20 to 10
    
    # 1. Generate sunward hemisphere (compressed, use an ellipsoid)
    for i_phi in range(int(n_phi/2)):
        phi = (i_phi / (n_phi-1)) * np.pi
        
        for i_theta in range(n_theta):
            theta = (i_theta / (n_theta-1)) * 2 * np.pi
            
            # Use ellipsoidal shaping - compress in x direction (sunward)
            x = -params['sunward_distance'] * np.cos(phi)  # Negative for sunward direction
            rho = np.sin(phi)
            y = params['equatorial_radius'] * rho * np.cos(theta)
            z = params['polar_radius'] * rho * np.sin(theta)
            
            x_coords.append(x)
            y_coords.append(y)
            z_coords.append(z)
    
    # 2. Generate magnetotail (anti-sunward direction, expands outward)
    for i in range(n_tail_segments + 1):
        fraction = i / n_tail_segments
        tail_x = fraction * params['tail_length']  # Positive for tail direction
        tail_radius = params['tail_base_radius'] + (params['tail_end_radius'] - params['tail_base_radius']) * fraction
        
        for i_theta in range(n_theta):
            theta = (i_theta / (n_theta-1)) * 2 * np.pi
            y = tail_radius * np.cos(theta)
            z = tail_radius * np.sin(theta)
            
            x_coords.append(tail_x)
            y_coords.append(y)
            z_coords.append(z)
    
    return x_coords, y_coords, z_coords

jupiter_hill_sphere_info = (
            "SELECT MANUAL SCALE OF AT LEAST 0.3 AU TO VISUALIZE.\n" 
            "1.3 MB PER FRAME FOR HTML.\n\n"
            "Jupiter's Hill Sphere (extends to ~530 Jupiter radii or about 0.25 AU)"                      
)

def create_jupiter_hill_sphere(center_position=(0, 0, 0)):
    """Creates Jupiter's Hill sphere."""
    # Hill sphere radius in Jupiter radii
    radius_fraction = 530  # Jupiter's Hill sphere is about 530 Jupiter radii
    
    # Calculate radius in AU
    radius_au = radius_fraction * JUPITER_RADIUS_AU
    
    # Create sphere points with fewer points for memory efficiency
    n_points = 30  # Reduced for large spheres
    x, y, z = create_sphere_points(radius_au, n_points=n_points)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    # Create hover text
    hover_text = "Jupiter's Hill Sphere (extends to ~530 Jupiter radii or about 0.25 AU)"
    
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
                opacity=0.3
            ),
            name='Jupiter: Hill Sphere',
            text=[hover_text] * len(x),
            customdata=['Jupiter: Hill Sphere'] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

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
            "  to a solid or liquid \"surface.\<br>" 
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
                opacity=0.3
            ),
            name='Saturn: Magnetosphere',
            text=["Saturn has a large magnetosphere, the region of space dominated by its magnetic field. Saturn's magnetic field is <br>" 
                  "unique because its magnetic axis is almost perfectly aligned with its rotational axis. The magnetosphere deflects <br>" 
                  "the solar wind and traps charged particles, leading to auroras at the poles. Material from Enceladus's plumes <br>" 
                  "contributes plasma to Saturn's magnetosphere and its E ring."] * len(x),
            customdata=['Saturn: Magnetosphere'] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces

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
    
    return traces

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
    
    return traces
    
def create_saturn_hill_sphere_shell(center_position=(0, 0, 0)):
    """Creates Saturn's Hill sphere shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 91,  # Saturn's Hill sphere is about 91 Saturn radii
        'color': 'rgb(0, 255, 0)',  # Green for Hill sphere
        'opacity': 0.3,
        'name': 'Hill Sphere',
        'description': (
            "SET MANUAL SCALE OF AT LEAST 0.3 AU TO VISUALIZE.<br><br>"
            "Saturn: Its Hill sphere, the region around the planet where its gravity dominates over the Sun's, has a radius of <br>" 
            "approximately 91 million kilometers (about 151 Saturn radii). This is smaller than Jupiter's Hill sphere due to <br>" 
            "Saturn's lower mass. The Hill sphere is crucial for determining the maximum distance at which a moon can stably orbit <br>" 
            "Saturn."
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
    
    return traces

saturn_magnetosphere_info = (
            "SELECT MANUAL SCALE OF AT LEAST 0.2 AU TO VISUALIZE.\n"
            "1.4 MB PER FRAME FOR HTML.\n\n"

            "Saturn has a large magnetosphere, the region of space dominated by its magnetic field. Saturn's magnetic field is \n" 
            "unique because its magnetic axis is almost perfectly aligned with its rotational axis. The magnetosphere deflects \n" 
            "the solar wind and traps charged particles, leading to auroras at the poles. Material from Enceladus's plumes \n" 
            "contributes plasma to Saturn's magnetosphere and its E ring."                      
)

def create_magnetosphere_shape(params):
    """
    Creates points for a magnetosphere with asymmetry, compressed on sunward side
    and extended on the tail side.
    
    Parameters:
        params (dict): Dictionary of shape parameters
        
    Returns:
        tuple: (x, y, z) coordinates as lists
    """
    x_coords = []
    y_coords = []
    z_coords = []
    
    # Number of points to generate (reduced for memory efficiency)
    n_phi = 20              # from 30 to 20
    n_theta = 20            # from 30 to 20
    n_tail_segments = 10    # from 20 to 10
    
    # 1. Generate sunward hemisphere (compressed, use an ellipsoid)
    for i_phi in range(int(n_phi/2)):
        phi = (i_phi / (n_phi-1)) * np.pi
        
        for i_theta in range(n_theta):
            theta = (i_theta / (n_theta-1)) * 2 * np.pi
            
            # Use ellipsoidal shaping - compress in x direction (sunward)
            x = -params['sunward_distance'] * np.cos(phi)  # Negative for sunward direction
            rho = np.sin(phi)
            y = params['equatorial_radius'] * rho * np.cos(theta)
            z = params['polar_radius'] * rho * np.sin(theta)
            
            x_coords.append(x)
            y_coords.append(y)
            z_coords.append(z)
    
    # 2. Generate magnetotail (anti-sunward direction, expands outward)
    for i in range(n_tail_segments + 1):
        fraction = i / n_tail_segments
        tail_x = fraction * params['tail_length']  # Positive for tail direction
        tail_radius = params['tail_base_radius'] + (params['tail_end_radius'] - params['tail_base_radius']) * fraction
        
        for i_theta in range(n_theta):
            theta = (i_theta / (n_theta-1)) * 2 * np.pi
            y = tail_radius * np.cos(theta)
            z = tail_radius * np.sin(theta)
            
            x_coords.append(tail_x)
            y_coords.append(y)
            z_coords.append(z)
    
    return x_coords, y_coords, z_coords

saturn_hill_sphere_info = (
            "SELECT MANUAL SCALE OF AT LEAST 0.3 AU TO VISUALIZE.\n" 
            "1.3 MB PER FRAME FOR HTML.\n\n"

            "Saturn: Its Hill sphere, the region around the planet where its gravity dominates over the Sun's, has a radius of \n" 
            "approximately 91 million kilometers (about 151 Saturn radii). This is smaller than Jupiter's Hill sphere due to \n" 
            "Saturn's lower mass. The Hill sphere is crucial for determining the maximum distance at which a moon can stably orbit \n" 
            "Saturn."                     
)

def create_saturn_hill_sphere(center_position=(0, 0, 0)):
    """Creates Saturn's Hill sphere."""
    # Hill sphere radius in Saturn radii
    radius_fraction = 91  # Saturn's Hill sphere is about 91 Saturn radii
    
    # Calculate radius in AU
    radius_au = radius_fraction * SATURN_RADIUS_AU
    
    # Create sphere points with fewer points for memory efficiency
    n_points = 30  # Reduced for large spheres
    x, y, z = create_sphere_points(radius_au, n_points=n_points)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    # Create hover text
    hover_text = "Saturn's Hill Sphere extends to ~91 Saturn radii."
    
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
                opacity=0.3
            ),
            name='Saturn: Hill Sphere',
            text=[hover_text] * len(x),
            customdata=['Saturn: Hill Sphere'] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces