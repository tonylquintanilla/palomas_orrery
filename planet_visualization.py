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
MERCURY_RADIUS_KM = CENTER_BODY_RADII['Mercury']        
MERCURY_RADIUS_AU = MERCURY_RADIUS_KM / KM_PER_AU

# Venus Constants
VENUS_RADIUS_KM = CENTER_BODY_RADII['Venus']
VENUS_RADIUS_AU = VENUS_RADIUS_KM / KM_PER_AU

# Earth Constants
EARTH_RADIUS_KM = CENTER_BODY_RADII['Earth']
EARTH_RADIUS_AU = EARTH_RADIUS_KM / KM_PER_AU

# Mars Constants
MARS_RADIUS_KM = CENTER_BODY_RADII['Mars']  # JPL uses an equipotential virtual surface with a mean radius at the equator as the Mars datum. 
MARS_RADIUS_AU = MARS_RADIUS_KM / KM_PER_AU  # Convert to AU

# Jupiter Constants
JUPITER_RADIUS_KM = CENTER_BODY_RADII['Jupiter']  # Equatorial radius in km
JUPITER_RADIUS_AU = JUPITER_RADIUS_KM / KM_PER_AU  # Convert to AU

# Saturn Constants
SATURN_RADIUS_KM = CENTER_BODY_RADII['Saturn']  # Equatorial radius in km
SATURN_RADIUS_AU = SATURN_RADIUS_KM / KM_PER_AU  # Convert to AU

# Uranus Constants
URANUS_RADIUS_KM = CENTER_BODY_RADII['Uranus']  # Equatorial radius in km
URANUS_RADIUS_AU = URANUS_RADIUS_KM / KM_PER_AU  # Convert to AU

# Neptune Constants
NEPTUNE_RADIUS_KM = CENTER_BODY_RADII['Neptune']  # Equatorial radius in km
NEPTUNE_RADIUS_AU = NEPTUNE_RADIUS_KM / KM_PER_AU  # Convert to AU

# Pluto Constants
PLUTO_RADIUS_KM = CENTER_BODY_RADII['Pluto']  # Equatorial radius in km
PLUTO_RADIUS_AU = PLUTO_RADIUS_KM / KM_PER_AU  # Convert to AU

# Eris/Dysnomia Constants
ERIS_RADIUS_KM = CENTER_BODY_RADII['Eris/Dysnomia']  # Equatorial radius in km
ERIS_RADIUS_AU = ERIS_RADIUS_KM / KM_PER_AU  # Convert to AU

# Planet 9 Constants
PLANET9_RADIUS_KM = CENTER_BODY_RADII['Planet 9']  # Equatorial radius in km
PLANET9_RADIUS_AU = PLANET9_RADIUS_KM / KM_PER_AU  # Convert to AU

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
    
    # Initialize shell_type to avoid undefined variable errors
#    shell_type = ""

    # Create shell traces based on selected variables
    traces = []
    
    if body_name == 'Sun':
        # Handle Sun visualization with its specific shells
        for shell_name, var in shell_vars.items():
            if var.get() == 1:
                # Call the appropriate shell creation function based on name
                if shell_name == 'core':
                    traces.extend(create_sun_core_shell())
                elif shell_name == 'radiative':
                    traces.extend(create_sun_radiative_shell())
                elif shell_name == 'photosphere':
                    traces.extend(create_sun_photosphere_shell())
                elif shell_name == 'chromosphere':
                    traces.extend(create_sun_chromosphere_shell())
                elif shell_name == 'inner_corona':
                    traces.extend(create_sun_inner_corona_shell())
                elif shell_name == 'outer_corona':
                    traces.extend(create_sun_outer_corona_shell())
                elif shell_name == 'termination_shock':
                    traces.extend(create_sun_termination_shock_shell())
                elif shell_name == 'heliopause':
                    traces.extend(create_sun_heliopause_shell())
                elif shell_name == 'inner_oort_limit':
                    traces.extend(create_sun_inner_oort_limit_shell())
                elif shell_name == 'inner_oort':
                    traces.extend(create_sun_inner_oort_shell())
                elif shell_name == 'outer_oort':
                    traces.extend(create_sun_outer_oort_shell())
                elif shell_name == 'gravitational':
                    traces.extend(create_sun_gravitational_shell())
    
    elif body_name == 'Mercury':
        # Handle Mercury visualization with its specific shells
        for shell_name, var in shell_vars.items():
            if var.get() == 1:
    #            shell_type = shell_name.replace('mercury_', '')
                if shell_name == 'inner_core':
                    traces.extend(create_mercury_inner_core_shell(center_position))
                elif shell_name == 'outer_core':
                    traces.extend(create_mercury_outer_core_shell(center_position))
                elif shell_name == 'mantle':
                    traces.extend(create_mercury_mantle_shell(center_position))
                elif shell_name == 'crust':
                    traces.extend(create_mercury_crust_shell(center_position))
                elif shell_name == 'atmosphere':
                    traces.extend(create_mercury_atmosphere_shell(center_position))
                elif shell_name == 'magnetosphere':
                    traces.extend(create_mercury_magnetosphere_shell(center_position))
                elif shell_name == 'hill_sphere':
                    traces.extend(create_mercury_hill_sphere_shell(center_position))

    elif body_name == 'Venus':
        # Handle Venus visualization with its specific shells
        for shell_name, var in shell_vars.items():
            if var.get() == 1:
    #            shell_name = shell_name.replace('venus_', '')
                if shell_name == 'core':
                    traces.extend(create_venus_core_shell(center_position))
                elif shell_name == 'mantle':
                    traces.extend(create_venus_mantle_shell(center_position))
                elif shell_name == 'crust':
                    traces.extend(create_venus_crust_shell(center_position))
                elif shell_name == 'atmosphere':
                    traces.extend(create_venus_atmosphere_shell(center_position))
                elif shell_name == 'upper_atmosphere':
                    traces.extend(create_venus_upper_atmosphere_shell(center_position))
                elif shell_name == 'magnetosphere':
                    traces.extend(create_venus_magnetosphere_shell(center_position))
                elif shell_name == 'hill_sphere':
                    traces.extend(create_venus_hill_sphere_shell(center_position))

    elif body_name == 'Earth':
        # Handle Earth visualization with its specific shells
        for shell_name, var in shell_vars.items():
            if var.get() == 1:
    #            shell_name = shell_name.replace('earth_', '')
                if shell_name == 'inner_core':
                    traces.extend(create_earth_inner_core_shell(center_position))
                elif shell_name == 'outer_core':
                    traces.extend(create_earth_outer_core_shell(center_position))
                elif shell_name == 'lower_mantle':
                    traces.extend(create_earth_lower_mantle_shell(center_position))
                elif shell_name == 'upper_mantle':
                    traces.extend(create_earth_upper_mantle_shell(center_position))
                elif shell_name == 'crust':
                    traces.extend(create_earth_crust_shell(center_position))
                elif shell_name == 'atmosphere':
                    traces.extend(create_earth_atmosphere_shell(center_position))
                elif shell_name == 'upper_atmosphere':
                    traces.extend(create_earth_upper_atmosphere_shell(center_position))
                elif shell_name == 'magnetosphere':
                    traces.extend(create_earth_magnetosphere_shell(center_position))
                elif shell_name == 'hill_sphere':
                    traces.extend(create_earth_hill_sphere_shell(center_position))
    
    elif body_name == 'Mars':
        # Handle Mars visualization with its specific shells
        for shell_name, var in shell_vars.items():
            if var.get() == 1:
    #            shell_name = shell_name.replace('mars_', '')
                if shell_name == 'inner_core':
                    traces.extend(create_mars_inner_core_shell(center_position))
                elif shell_name == 'outer_core':
                    traces.extend(create_mars_outer_core_shell(center_position))
                elif shell_name == 'mantle':
                    traces.extend(create_mars_mantle_shell(center_position))
                elif shell_name == 'crust':
                    traces.extend(create_mars_crust_shell(center_position))
                elif shell_name == 'atmosphere':
                    traces.extend(create_mars_atmosphere_shell(center_position))
                elif shell_name == 'upper_atmosphere':
                    traces.extend(create_mars_upper_atmosphere_shell(center_position))
                elif shell_name == 'hill_sphere':
                    traces.extend(create_mars_hill_sphere_shell(center_position))

    elif body_name == 'Jupiter':
        # Handle Jupiter visualization with its specific shells
        for shell_name, var in shell_vars.items():
            if var.get() == 1:
    #            shell_name = shell_name.replace('jupiter_', '')
                if shell_name == 'core':
                    traces.extend(create_jupiter_core_shell(center_position))
                elif shell_name == 'metallic_hydrogen':
                    traces.extend(create_jupiter_metallic_hydrogen_shell(center_position))
                elif shell_name == 'molecular_hydrogen':
                    traces.extend(create_jupiter_molecular_hydrogen_shell(center_position))
                elif shell_name == 'cloud_layer':
                    traces.extend(create_jupiter_cloud_layer_shell(center_position))
                elif shell_name == 'upper_atmosphere':
                    traces.extend(create_jupiter_upper_atmosphere_shell(center_position))
                elif shell_name == 'ring_system':
                    traces.extend(create_jupiter_ring_system(center_position))
                elif shell_name == 'radiation_belts':
                    traces.extend(create_jupiter_radiation_belts(center_position))
                elif shell_name == 'io_plasma_torus':
                    traces.extend(create_jupiter_io_plasma_torus(center_position))
                elif shell_name == 'magnetosphere':
                    traces.extend(create_jupiter_magnetosphere(center_position))
                elif shell_name == 'hill_sphere':
                    traces.extend(create_jupiter_hill_sphere_shell(center_position))

    elif body_name == 'Saturn':
        # Handle Saturn visualization with its specific shells
        for shell_name, var in shell_vars.items():
            if var.get() == 1:
    #            shell_name = shell_name.replace('saturn_', '')
                if shell_name == 'core':
                    traces.extend(create_saturn_core_shell(center_position))
                elif shell_name == 'metallic_hydrogen':
                    traces.extend(create_saturn_metallic_hydrogen_shell(center_position))
                elif shell_name == 'molecular_hydrogen':
                    traces.extend(create_saturn_molecular_hydrogen_shell(center_position))
                elif shell_name == 'cloud_layer':
                    traces.extend(create_saturn_cloud_layer_shell(center_position))
                elif shell_name == 'upper_atmosphere':
                    traces.extend(create_saturn_upper_atmosphere_shell(center_position))
                elif shell_name == 'ring_system':
                    traces.extend(create_saturn_ring_system(center_position))
                elif shell_name == 'radiation_belts':
                    traces.extend(create_saturn_radiation_belts(center_position))
                elif shell_name == 'io_plasma_torus':
                    traces.extend(create_saturn_enceladus_plasma_torus(center_position))
                elif shell_name == 'magnetosphere':
                    traces.extend(create_saturn_magnetosphere(center_position))
                elif shell_name == 'hill_sphere':
                    traces.extend(create_saturn_hill_sphere_shell(center_position))

    elif body_name == 'Uranus':
        # Handle uranus visualization with its specific shells
        for shell_name, var in shell_vars.items():
            if var.get() == 1:
    #            shell_name = shell_name.replace('uranus_', '')
                if shell_name == 'core':
                    traces.extend(create_uranus_core_shell(center_position))
                elif shell_name == 'mantle':
                    traces.extend(create_uranus_mantel_shell(center_position))
                elif shell_name == 'cloud_layer':
                    traces.extend(create_uranus_cloud_layer_shell(center_position))
                elif shell_name == 'upper_atmosphere':
                    traces.extend(create_uranus_upper_atmosphere_shell(center_position))
                elif shell_name == 'ring_system':
                    traces.extend(create_uranus_ring_system(center_position))
                elif shell_name == 'radiation_belts':
                    traces.extend(create_uranus_radiation_belts(center_position))
                elif shell_name == 'magnetosphere':
                    traces.extend(create_uranus_magnetosphere(center_position))
                elif shell_name == 'hill_sphere':
                    traces.extend(create_uranus_hill_sphere_shell(center_position))

    elif body_name == 'Neptune':
        # Handle Neptune visualization with its specific shells
        for shell_name, var in shell_vars.items():
            if var.get() == 1:
    #            shell_name = shell_name.replace('neptune_', '')
                if shell_name == 'core':
                    traces.extend(create_neptune_core_shell(center_position))
                elif shell_name == 'mantle':
                    traces.extend(create_neptune_mantel_shell(center_position))
                elif shell_name == 'cloud_layer':
                    traces.extend(create_neptune_cloud_layer_shell(center_position))
                elif shell_name == 'upper_atmosphere':
                    traces.extend(create_neptune_upper_atmosphere_shell(center_position))
                elif shell_name == 'ring_system':
                    traces.extend(create_neptune_ring_system(center_position))
                elif shell_name == 'radiation_belts':
                    traces.extend(create_neptune_radiation_belts(center_position))
                elif shell_name == 'magnetosphere':
                    traces.extend(create_neptune_magnetosphere(center_position))
                elif shell_name == 'hill_sphere':
                    traces.extend(create_neptune_hill_sphere_shell(center_position))

    elif body_name == 'Pluto':
        # Handle Pluto visualization with its specific shells
        for shell_name, var in shell_vars.items():
            if var.get() == 1:
    #            shell_name = shell_name.replace('pluto_', '')
                if shell_name == 'core':
                    traces.extend(create_pluto_core_shell(center_position))
                elif shell_name == 'mantle':
                    traces.extend(create_pluto_mantel_shell(center_position))
                elif shell_name == 'crust':
                    traces.extend(create_pluto_crust_shell(center_position))
                elif shell_name == 'haze_layer':
                    traces.extend(create_pluto_haze_layer_shell(center_position))
                elif shell_name == 'atmosphere':
                    traces.extend(create_pluto_atmosphere_shell(center_position))
                elif shell_name == 'hill_sphere':
                    traces.extend(create_pluto_hill_sphere_shell(center_position))

    elif body_name == 'Eris/Dysnomia':
        # Handle eris visualization with its specific shells
        for shell_name, var in shell_vars.items():
            if var.get() == 1:
    #            shell_name = shell_name.replace('eris_', '')
                if shell_name == 'core':
                    traces.extend(create_eris_core_shell(center_position))
                elif shell_name == 'mantle':
                    traces.extend(create_eris_mantel_shell(center_position))
                elif shell_name == 'crust':
                    traces.extend(create_eris_crust_shell(center_position))
                elif shell_name == 'atmosphere':
                    traces.extend(create_eris_atmosphere_shell(center_position))
                elif shell_name == 'hill_sphere':
                    traces.extend(create_eris_hill_sphere_shell(center_position))

    elif body_name == 'Planet 9':
        # Handle Planet 9 visualization with its specific shells
        for shell_name, var in shell_vars.items():
            if var.get() == 1:
    #            shell_name = shell_name.replace('planet9_', '')
                if shell_name == 'surface':
                    traces.extend(create_planet9_surface_shell(center_position))
                elif shell_name == 'hill_sphere':
                    traces.extend(create_planet9_hill_sphere_shell(center_position))

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

    if planet_name == 'Uranus':
        if shell_vars['uranus_core'].get() == 1:
            traces.extend(create_uranus_core_shell(center_position))
        if shell_vars['uranus_mantel'].get() == 1:
            traces.extend(create_uranus_mantel_shell(center_position))
        if shell_vars['uranus_cloud_layer'].get() == 1:
            traces.extend(create_uranus_cloud_layer_shell(center_position))
        if shell_vars['uranus_upper_atmosphere'].get() == 1:
            traces.extend(create_uranus_upper_atmosphere_shell(center_position))
        if shell_vars['uranus_ring_system'].get() == 1:
            traces.extend(create_uranus_ring_system(center_position))
        if shell_vars['uranus_radiation_belts'].get() == 1:
            traces.extend(create_uranus_radiation_belts(center_position))
        if shell_vars['uranus_magnetosphere'].get() == 1:
            traces.extend(create_uranus_magnetosphere(center_position))
        if shell_vars['uranus_hill_sphere'].get() == 1:
            traces.extend(create_uranus_hill_sphere_shell(center_position))

    if planet_name == 'Neptune':
        if shell_vars['neptune_core'].get() == 1:
            traces.extend(create_neptune_core_shell(center_position))
        if shell_vars['neptune_mantel'].get() == 1:
            traces.extend(create_neptune_mantel_shell(center_position))
        if shell_vars['neptune_cloud_layer'].get() == 1:
            traces.extend(create_neptune_cloud_layer_shell(center_position))
        if shell_vars['neptune_upper_atmosphere'].get() == 1:
            traces.extend(create_neptune_upper_atmosphere_shell(center_position))
        if shell_vars['neptune_ring_system'].get() == 1:
            traces.extend(create_neptune_ring_system(center_position))
        if shell_vars['neptune_radiation_belts'].get() == 1:
            traces.extend(create_neptune_radiation_belts(center_position))
        if shell_vars['neptune_magnetosphere'].get() == 1:
            traces.extend(create_neptune_magnetosphere(center_position))
        if shell_vars['neptune_hill_sphere'].get() == 1:
            traces.extend(create_neptune_hill_sphere_shell(center_position))

    if planet_name == 'Pluto':
        if shell_vars['pluto_core'].get() == 1:
            traces.extend(create_pluto_core_shell(center_position))
        if shell_vars['pluto_mantel'].get() == 1:
            traces.extend(create_pluto_mantel_shell(center_position))
        if shell_vars['pluto_crust'].get() == 1:
            traces.extend(create_pluto_crust_shell(center_position))
        if shell_vars['pluto_haze_layer'].get() == 1:
            traces.extend(create_pluto_haze_layer_shell(center_position))
        if shell_vars['pluto_atmosphere'].get() == 1:
            traces.extend(create_pluto_atmosphere_shell(center_position))
        if shell_vars['pluto_hill_sphere'].get() == 1:
            traces.extend(create_pluto_hill_sphere_shell(center_position))

    if planet_name == 'Eris/Dysnomia':
        if shell_vars['eris_core'].get() == 1:
            traces.extend(create_eris_core_shell(center_position))
        if shell_vars['eris_mantel'].get() == 1:
            traces.extend(create_eris_mantel_shell(center_position))
        if shell_vars['eris_crust'].get() == 1:
            traces.extend(create_eris_crust_shell(center_position))
        if shell_vars['eris_atmosphere'].get() == 1:
            traces.extend(create_eris_atmosphere_shell(center_position))
        if shell_vars['eris_hill_sphere'].get() == 1:
            traces.extend(create_eris_hill_sphere_shell(center_position))

    if planet_name == 'Planet 9':
        if shell_vars['planet9_surface'].get() == 1:
            traces.extend(create_planet9_surface_shell(center_position))
        if shell_vars['planet9_hill_sphere'].get() == 1:
            traces.extend(create_planet9_hill_sphere_shell(center_position))
    
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
                                    .replace("Uranus", planet_name).replace("Neptune", planet_name).replace("Pluto", planet_name)
                                    .replace("Eris/Dysnomia", planet_name).replace("Planet 9", planet_name)
                            if "Mercury" in str(item) or "Venus" in str(item) or "Earth" in str(item) or "Mars" in str(item)
                                or "Jupiter" in str(item) or "Saturn" in str(item) or "Uranus" in str(item) or "Neptune" in str(item)
                                or "Pluto" in str(item) or "Eris/Dysnomia" in str(item) or "Planet 9" in str(item)
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
    radius_fraction = 90  # Mercury's Hill sphere is about 235 Mercury radii
    
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
    hover_text = ("Venus's Hill Sphere (extends to ~166 Venus radii or about 1 million km)<br><br>" 
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
                "the object into a heliocentric orbit.<br><br>"
                "The Hill sphere is the region around a where its own gravity is the dominant force in attracting satellites. For <br>" 
                "a planet orbiting a star, it's the region where the planet's gravity is stronger than the star's tidal forces.<br><br>" 
                "The Hill Sphere radius can be described in words as follows: it is equal to the planet's average distance from the <br>" 
                "Sun (its orbital semi-major axis) multiplied by the cube root of the ratio between the planet's mass and three times <br>" 
                "the Sun's mass. In other words, you take how far the planet orbits out from the Sun, then scale that distance by the <br>" 
                "cube root of (planet mass ÷ [3 x solar mass]) to find the boundary within which the planet's gravity dominates over the Sun's."               
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

jupiter_io_plasma_torus_info = ("634 KB PER FRAME FOR HTML.\n\n"
              "Donut-shaped region of charged particles from Jupiter's moon Io")

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

jupiter_radiation_belts_info = (
            "560 KB PER FRAME FOR HTML.\n\n"
            "Zones of trapped high-energy particles in Jupiter's magnetosphere"                     
)

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
    
jupiter_hill_sphere_info = (
            "SELECT MANUAL SCALE OF AT LEAST 0.3 AU TO VISUALIZE.\n" 
            "1.3 MB PER FRAME FOR HTML.\n\n"
            "Jupiter's Hill Sphere (extends to ~530 Jupiter radii or about 0.25 AU)"                      
)

def create_jupiter_hill_sphere_shell(center_position=(0, 0, 0)):
    """Creates Jupiter's Hill sphere shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 750,  
        'color': 'rgb(0, 255, 0)',  # Green for Hill sphere
        'opacity': 0.3,
        'name': 'Hill Sphere',
        'description': (
            "SET MANUAL SCALE OF AT LEAST 0.3 AU TO VISUALIZE.<br><br>"
            "Jupiter's Hill Sphere (extends to ~750 Jupiter radii)<br><br>"
                "The Hill sphere is the region around a where its own gravity is the dominant force in attracting satellites. For <br>" 
                "a planet orbiting a star, it's the region where the planet's gravity is stronger than the star's tidal forces.<br><br>" 
                "The Hill Sphere radius can be described in words as follows: it is equal to the planet's average distance from the <br>" 
                "Sun (its orbital semi-major axis) multiplied by the cube root of the ratio between the planet's mass and three times <br>" 
                "the Sun's mass. In other words, you take how far the planet orbits out from the Sun, then scale that distance by the <br>" 
                "cube root of (planet mass ÷ [3 x solar mass]) to find the boundary within which the planet's gravity dominates over the Sun's."            
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
    
    return traces
    
saturn_hill_sphere_info = (
            "SELECT MANUAL SCALE OF AT LEAST 0.3 AU TO VISUALIZE.\n" 
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

# Uranus Shell Creation Functions

uranus_core_info = (
            "2.4 MB PER FRAME FOR HTML.\n\n"
            "Uranus core: Scientists believe Uranus has a relatively small, rocky core. This core is likely composed of silicate and \n" 
            "metallic iron-nickel. It's estimated to have a mass roughly equivalent to that of Earth. Temperatures near the core can \n" 
            "reach incredibly high values, around 4982°C (5255 K) degrees Celsius."
)

def create_uranus_core_shell(center_position=(0, 0, 0)):
    """Creates Uranus's core shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 0.2,  # Approximately 20% of Uranus's radius
        'color': 'rgb(255, 215, 0)',  # estimated black body color at about 4982°C (5255 K)
        'opacity': 1.0,
        'name': 'Core',
        'description': (
            "Uranus core: Scientists believe Uranus has a relatively small, rocky core. This core is likely composed of silicate and <br>" 
            "metallic iron-nickel. It's estimated to have a mass roughly equivalent to that of Earth. Temperatures near the core can <br>" 
            "reach incredibly high values, around 4982°C (5255 K) degrees Celsius."
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

uranus_mantel_info = (
            "2.1 MB PER FRAME FOR HTML.\n\n"
            "Mantel: Surrounding the rocky core is a dense fluid layer often referred to as an \"icy mantle.\" This layer makes up the \n" 
            "majority (80% or more) of the planet's mass. It's not ice in the traditional sense but rather a hot, dense fluid \n" 
            "containing water, ammonia, and methane under immense pressure. These are sometimes referred to as \"ices\" by planetary \n" 
            "scientists. This mantle is electrically conductive and is thought to be the region where Uranus' unusual magnetic field \n" 
            "is generated."
)

def create_uranus_mantel_shell(center_position=(0, 0, 0)):
    """Creates Uranus's matel shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 0.7,  # Up to about 70% of Uranus's radius
        'color': 'rgb(255, 138, 18)',  # estimated black body color at about 2,000 K
        'opacity': 0.9,
        'name': 'Mantel',
        'description': (
            "Mantel: Surrounding the rocky core is a dense fluid layer often referred to as an \"icy mantle.\" This layer makes up the <br>" 
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
            "  fraction of Uranus' radius at the 1 bar level: Fraction = 25,609 km / 25,559 km ≈ 1.002."
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
            "Atmosphere: Uranus has a thick atmosphere primarily composed of Hydrogen (H₂): Making up about 83% of the atmosphere; \n" 
            "Helium (He): Constituting around 15%; Methane (CH₄): Present in smaller amounts, around 2.3%. This methane absorbs red \n" 
            "light, giving Uranus its characteristic blue-green hue. Trace amounts: Water (H₂O) and ammonia (NH₃) are also present \n" 
            "in small quantities. Other hydrocarbons like ethane, acetylene, and methyl acetylene exist in trace amounts, formed by \n" 
            "the breakdown of methane by sunlight. The atmosphere lacks the prominent banding seen on Jupiter and Saturn but does \n" 
            "experience extremely cold temperatures, reaching as low as 49 Kelvin (-224 °C), making it the coldest planetary \n" 
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
            "Atmosphere: Uranus has a thick atmosphere primarily composed of Hydrogen (H₂): Making up about 83% of the atmosphere; <br>" 
            "Helium (He): Constituting around 15%; Methane (CH₄): Present in smaller amounts, around 2.3%. This methane absorbs red <br>" 
            "light, giving Uranus its characteristic blue-green hue. Trace amounts: Water (H₂O) and ammonia (NH₃) are also present <br>" 
            "in small quantities. Other hydrocarbons like ethane, acetylene, and methyl acetylene exist in trace amounts, formed by <br>" 
            "the breakdown of methane by sunlight. The atmosphere lacks the prominent banding seen on Jupiter and Saturn but does <br>" 
            "experience extremely cold temperatures, reaching as low as 49 Kelvin (-224 °C), making it the coldest planetary <br>" 
            "atmosphere in our solar system. The atmosphere is layered into a troposphere, stratosphere, and thermosphere.<br>" 
            "* The altitude of the top of Uranus' thermosphere is not as sharply defined as the tropopause. The thermosphere <br>" 
            "  gradually transitions into the exosphere. The stratosphere extends up to about 4,000 kilometers above the 1 bar <br>" 
            "  level. The thermosphere and exosphere then extend from this altitude outwards. Some sources suggest the thermosphere <br>" 
            "  can reach as high as two Uranus radii from the planet's center.<br>" 
            "* Top of Stratosphere (approximate lower bound of Thermosphere): Radius at 1 bar level: ≈ 25,559 km; Altitude of <br>" 
            "  stratopause: ≈ 4,000 km; Equivalent radius: 25,559 km + 4,000 km = 29,559 kilometers; Fraction of Uranus' radius <br>" 
            "  (at 1 bar): 29,559 km / 25,559 km ≈ 1.157.<br>" 
            "* Outer Extent of Thermosphere/Exosphere (approximate upper bound): Radius at 1 bar level: ≈ 25,559 km; Two Uranus radii <br>" 
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
    
    return traces

uranus_magnetosphere_info = (
            "SELECT MANUAL SCALE OF AT LEAST 0.02 AU TO VISUALIZE.\n"
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
            "considerable distance from the planet.<BR>" 
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
    compound rotation approach due to the planet's extreme axial tilt (97.77°).

    The transformation uses these key elements:
    1. A 105° rotation around the X-axis followed by a 105° rotation around the Y-axis
    (empirically determined to match satellite orbit alignment)
    2. Converting point coordinates to NumPy arrays before rotation
    3. Applying center position offset to the final coordinates after both rotations

    This approach ensures that all components of the Uranian system (rings, satellites, 
    radiation belts) share the same reference frame, correctly representing the planet's
    unique orientation in space.

    NOTE: The 105° value, rather than the nominal 97.77° axial tilt, accounts for the 
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
    
    return traces

uranus_hill_sphere_info = (
            "SELECT MANUAL SCALE OF AT LEAST 0.5 AU TO VISUALIZE.\n" 
            "1.3 MB PER FRAME FOR HTML.\n\n"

            "The Hill sphere (also known as the Roche sphere) represents the region around a celestial body where its own gravity \n" 
            "is the dominant force attracting satellites. Uranus has a Hill radius around 7.02×10⁷ km, which corresponds to about \n" 
            "2 770 Uranus radii (mean radius ≈25 360 km). This means that any moon or other object orbiting Uranus within this \n" 
            "sphere is primarily gravitationally bound to the planet. The major moons and rings of Uranus lie well within its Hill \n" 
            "sphere."                     
)

def create_uranus_hill_sphere_shell(center_position=(0, 0, 0)):
    """Creates Uranus's Hill sphere shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 2770, 
        'color': 'rgb(0, 255, 0)',  # Green for Hill sphere
        'opacity': 0.3,
        'name': 'Hill Sphere',
        'description': (
            "SET MANUAL SCALE OF AT LEAST 0.3 AU TO VISUALIZE.<br><br>"
    "The Hill sphere (also known as the Roche sphere) represents the region around a celestial body where its own gravity <br>" 
    "is the dominant force attracting satellites. Uranus has a Hill radius around 7.02x10⁷ km, which corresponds to about <br>" 
    "2 770 Uranus radii (mean radius ≈25 360 km). This means that any moon or other object orbiting Uranus within this <br>" 
    "sphere is primarily gravitationally bound to the planet. The major moons and rings of Uranus lie well within its Hill Sphere<br><br>" 
                "The Hill sphere is the region around a where its own gravity is the dominant force in attracting satellites. For <br>" 
                "a planet orbiting a star, it's the region where the planet's gravity is stronger than the star's tidal forces.<br><br>" 
                "The Hill Sphere radius can be described in words as follows: it is equal to the planet's average distance from the <br>" 
                "Sun (its orbital semi-major axis) multiplied by the cube root of the ratio between the planet's mass and three times <br>" 
                "the Sun's mass. In other words, you take how far the planet orbits out from the Sun, then scale that distance by the <br>" 
                "cube root of (planet mass ÷ [3 x solar mass]) to find the boundary within which the planet's gravity dominates over the Sun's."
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
    
    return traces

# Neptune Shell Creation Functions

neptune_core_info = (
            "2.4 MB PER FRAME FOR HTML.\n\n"
            "Neptune core: At Neptune's center lies a relatively small, rocky core composed primarily of iron, nickel, and silicates. \n" 
            "Its mass is estimated to be about 1.2 times that of Earth. The pressure at the core is immense, reaching about 7 million \n" 
            "bars (700 GPa), and the temperature could be as high as 5,100 °C."
)

def create_neptune_core_shell(center_position=(0, 0, 0)):
    """Creates Neptune's core shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 0.25,  # Approximately 25% of Neptune's radius
        'color': 'rgb(255, 215, 0)',  # estimated black body color at about 5100°C 
        'opacity': 1.0,
        'name': 'Core',
        'description': (
            "Neptune core: At Neptune's center lies a relatively small, rocky core composed primarily of iron, nickel, and silicates. <br>" 
            "Its mass is estimated to be about 1.2 times that of Earth. The pressure at the core is immense, reaching about 7 million <br>" 
            "bars (700 GPa), and the temperature could be as high as 5,100 °C.<br>" 
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

neptune_mantel_info = (
            "2.1 MB PER FRAME FOR HTML.\n\n"
            "Mantel: Surrounding the core is a dense mantle made up of a hot, highly compressed fluid of water, methane, and ammonia. \n " 
            "This layer constitutes the majority of Neptune's mass, about 10 to 15 Earth masses. The high pressure and temperature create \n" 
            "an environment where these \"icy\" materials exist in exotic phases, possibly including ionic water and superionic water. \n" 
            "Some theories suggest that at great depths within the mantle, methane may decompose, forming diamond crystals that could \n" 
            "\"rain\" downwards."
)

def create_neptune_mantel_shell(center_position=(0, 0, 0)):
    """Creates Neptune's mantel shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 0.85,  # Up to about 85% of neptune's radius
        'color': 'rgb(255, 138, 18)',  # estimated black body color at about 2,000 K
        'opacity': 0.9,
        'name': 'Mantel',
        'description': (
            "Mantel: Surrounding the core is a dense mantle made up of a hot, highly compressed fluid of water, methane, and ammonia. <br> " 
            "This layer constitutes the majority of Neptune's mass, about 10 to 15 Earth masses. The high pressure and temperature create <br>" 
            "an environment where these \"icy\" materials exist in exotic phases, possibly including ionic water and superionic water. <br>" 
            "Some theories suggest that at great depths within the mantle, methane may decompose, forming diamond crystals that could <br>" 
            "\"rain\" downwards.<br>" 
            "* The mantle makes up a significant portion of the remaining interior. Models suggest it could extend out to approximately <br>" 
            "  80-85% of Neptune's total radius.<br>" 
            "* It's important to remember that this is still an estimate based on our current understanding of Neptune's interior. <br>" 
            "  The transition from the dense fluid mantle to the gaseous atmosphere is likely a gradual one.<br>" 
            "* The temperature within Neptune's mantle is incredibly high, ranging from approximately 2,000 K (around 1,700 °C) to <br>" 
            "  5,000 K (around 4,700 °C). It's important to understand that Neptune's mantle isn't a solid, icy layer like the name <br>" 
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
            "  * The thermosphere begins at pressures below 10⁻⁵ to 10⁻⁴ bars (1 to 10 Pa).<br>" 
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
    
    return traces

neptune_magnetosphere_info = (
            "SELECT MANUAL SCALE OF AT LEAST 0.2 AU TO VISUALIZE.\n"
            "1.4 MB PER FRAME FOR HTML.\n\n"

            "Magnetosphere: Neptune possesses a significant and unusual magnetosphere. Unlike Earth's magnetic field, which is \n" 
            "roughly aligned with its rotational axis, Neptune's magnetic axis is tilted by about 47 degrees relative to its rotation \n" 
            "axis and offset from the planet's center by a considerable fraction of its radius. This creates a complex and dynamic \n" 
            "magnetic environment. The magnetosphere traps charged particles from the solar wind and accelerates them to high energies."                     
)

def create_neptune_magnetosphere(center_position=(0, 0, 0)):
    """Creates Neptune's main magnetosphere structure with proper tilt and offset."""
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
    
    # Implement Neptune's magnetic field offset (0.55 Neptune radii, mostly northward)
    # The offset is applied before rotation to properly represent the field
    offset_distance = 0.55 * NEPTUNE_RADIUS_AU
    
    # Apply the offset primarily in the z-direction (northward)
    # with small components in x and y to match observations
    z = z + (0.5 * offset_distance)  # Major component of offset in z
    x = x + (0.2 * offset_distance)  # Minor component in x
    y = y + (0.1 * offset_distance)  # Minor component in y
    
    # Implement Neptune's magnetic axis tilt (47 degrees relative to rotation axis)
    # First, tilt around the y-axis to implement the main magnetic axis tilt
    magnetic_tilt = np.radians(47)
    x_tilted1, y_tilted1, z_tilted1 = rotate_points(x, y, z, magnetic_tilt, 'y')
    
    # Second rotation to match the observed orientation (around z-axis)
    azimuthal_angle = np.radians(60)  # Estimated angle based on Voyager data
    x_tilted2, y_tilted2, z_tilted2 = rotate_points(x_tilted1, y_tilted1, z_tilted1, azimuthal_angle, 'z')
    
    # Unpack center position
    center_x, center_y, center_z = center_position
    
    # Apply center position offset to final coordinates
    x_final = x_tilted2 + center_x
    y_final = y_tilted2 + center_y
    z_final = z_tilted2 + center_z
    
    # Detailed description for hover information
    magnetosphere_text = [
        "Neptune's Magnetosphere: Unlike other planets, Neptune's magnetic field is dramatically tilted (47° from its rotation axis) and "
        "significantly offset from the planet's center by more than half a Neptune radius. This creates an extremely asymmetric magnetosphere "
        "that varies greatly depending on Neptune's rotation. The magnetosphere extends about 34-40 Neptune radii sunward and stretches into "
        "a long tail in the opposite direction. It deflects the solar wind and contains trapped charged particles that produce aurora near "
        "Neptune's magnetic poles. This uniquely complex magnetic environment was studied by Voyager 2 during its 1989 flyby."
    ] * len(x_final)
    
    magnetosphere_customdata = ['Neptune: Magnetosphere'] * len(x_final)
    
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
    
    # Add a trace to visualize the magnetic axis and poles
    # This helps users understand the tilt and offset
#    magnetic_poles = create_neptune_magnetic_poles(center_position, offset_distance, magnetic_tilt, azimuthal_angle)
#    traces.extend(magnetic_poles)
    
    return traces

"""
def create_neptune_magnetic_poles(center_position, offset_distance, tilt, azimuth):
    
#    Creates visualization elements for Neptune's magnetic poles and axis.
    
#    Parameters:
#        center_position (tuple): Planet center coordinates
#        offset_distance (float): Offset of magnetic field center in AU
#        tilt (float): Main magnetic tilt angle in radians
#        azimuth (float): Azimuthal orientation angle in radians
        
#    Returns:
#        list: Plotly traces for magnetic poles and axis
    
    center_x, center_y, center_z = center_position
    
    # Start with offset magnetic center
    mag_center_x = center_x + (0.2 * offset_distance)
    mag_center_y = center_y + (0.1 * offset_distance)
    mag_center_z = center_z + (0.5 * offset_distance)
    
    # Create axis points (north and south poles at 15 Neptune radii from magnetic center)
    axis_length = 15 * NEPTUNE_RADIUS_AU
    
    # Initial axis points along z-axis
    north_x, north_y, north_z = 0, 0, axis_length
    south_x, south_y, south_z = 0, 0, -axis_length
    
    # Apply tilts to match Neptune's magnetic field orientation
    # First y-axis tilt
    north_x, north_y, north_z = rotate_points(north_x, north_y, north_z, tilt, 'y')
    south_x, south_y, south_z = rotate_points(south_x, south_y, south_z, tilt, 'y')
    
    # Then z-axis rotation
    north_x, north_y, north_z = rotate_points(north_x, north_y, north_z, azimuth, 'z')
    south_x, south_y, south_z = rotate_points(south_x, south_y, south_z, azimuth, 'z')
    
    # Add to magnetic center offset
    north_x += mag_center_x
    north_y += mag_center_y 
    north_z += mag_center_z
    
    south_x += mag_center_x
    south_y += mag_center_y
    south_z += mag_center_z
    
    # Create magnetic center marker
    mag_center_trace = go.Scatter3d(
        x=[mag_center_x],
        y=[mag_center_y],
        z=[mag_center_z],
        mode='markers',
        marker=dict(
            size=5,
            color='yellow',
            symbol='diamond'
        ),
        name='Neptune: Magnetic Field Center',
        text=["Neptune's magnetic field center is offset by ~0.55 Neptune radii from the planet's center"],
        hoverinfo='text',
        showlegend=True
    )
    
    # Create magnetic axis line
    axis_trace = go.Scatter3d(
        x=[north_x, south_x],
        y=[north_y, south_y],
        z=[north_z, south_z],
        mode='lines',
        line=dict(
            color='yellow',
            width=4,
            dash='dot'
        ),
        name='Neptune: Magnetic Axis',
        text=["Neptune's magnetic axis is tilted 47° from its rotation axis"],
        hoverinfo='text',
        showlegend=True
    )
    
    # Create north and south magnetic poles
    north_pole_trace = go.Scatter3d(
        x=[north_x],
        y=[north_y],
        z=[north_z],
        mode='markers',
        marker=dict(
            size=4,
            color='blue',
            symbol='circle'
        ),
        name='Neptune: North Magnetic Pole',
        text=["Neptune's north magnetic pole"],
        hoverinfo='text',
        showlegend=True
    )
    
    south_pole_trace = go.Scatter3d(
        x=[south_x],
        y=[south_y],
        z=[south_z],
        mode='markers',
        marker=dict(
            size=4,
            color='red',
            symbol='circle'
        ),
        name='Neptune: South Magnetic Pole',
        text=["Neptune's south magnetic pole"],
        hoverinfo='text',
        showlegend=True
    )
    
    return [mag_center_trace, axis_trace, north_pole_trace, south_pole_trace]
"""

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
                          "* Maintaining proper magnetic field geometry: 47° tilt from the rotation axis; 0.55 Neptune radii offset <br>" 
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
                          "* Maintaining proper magnetic field geometry: 47° tilt from the rotation axis; 0.55 Neptune radii offset <br>" 
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
                          "* Maintaining proper magnetic field geometry: 47° tilt from the rotation axis; 0.55 Neptune radii offset <br>" 
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
                          "* Maintaining proper magnetic field geometry: 47° tilt from the rotation axis; 0.55 Neptune radii offset <br>" 
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
                angle_offset = 0.4 * np.sin(np.pi * t)  # Max 0.4 radians (~23°) curvature
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
        with its axial tilt (28.32°) and pole orientation. Unlike Uranus (which has
        an extreme axial tilt of ~98°), Neptune's rings require a different approach.
        
        The transformation uses:
        1. Standard orbital element rotations for each ring
        2. Application of Neptune's pole direction (RA: 299.36°, Dec: 43.46°)
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
                "* Named after François Arago, a French mathematician, physicist, and astronomer.<br>" 
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
                "* Contains five prominent arc segments (Courage, Liberté, Egalité 1 & 2, and Fraternité) that are denser than the rest of the ring.<br>" 
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
                "* Spans approximately 1,000 km (4° of arc) along the ring.<br>" 
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
            'name': 'Liberté Arc',
            'description': (
                "Liberté Arc: The second arc in Neptune's Adams Ring.<br>" 
                "* Located within the Adams Ring at a distance of about 62,930 km from Neptune's center.<br>" 
                "* Spans approximately 1,100 km (4.5° of arc) along the ring.<br>" 
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
            'name': 'Égalité 1 Arc',
            'description': (
                "Égalité 1 Arc: One of two 'Equality' arcs in Neptune's Adams Ring.<br>" 
                "* Located within the Adams Ring at a distance of about 62,930 km from Neptune's center.<br>" 
                "* Spans approximately 1,000 km (4.2° of arc) along the ring.<br>" 
                "* Named after 'Equality' from the motto of the French Republic.<br>"
                "* Together with Égalité 2, forms a pair of similar arcs separated by a small gap.<br>"
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
            'name': 'Égalité 2 Arc',
            'description': (
                "Égalité 2 Arc: The second 'Equality' arc in Neptune's Adams Ring.<br>" 
                "* Located within the Adams Ring at a distance of about 62,930 km from Neptune's center.<br>" 
                "* Spans approximately 1,000 km (4° of arc) along the ring.<br>" 
                "* Named after 'Equality' from the motto of the French Republic.<br>"
                "* Follows closely after Égalité 1, separated by a small gap.<br>"
                "* The pair of Égalité arcs may be maintained by resonances with nearby moons.<br><br>"
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
            'name': 'Fraternité Arc',
            'description': (
                "Fraternité Arc: The longest and most prominent arc in Neptune's Adams Ring.<br>" 
                "* Located within the Adams Ring at a distance of about 62,930 km from Neptune's center.<br>" 
                "* Spans approximately 2,200 km (9° of arc) along the ring, making it the longest arc.<br>" 
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
        # Neptune's pole is oriented at RA=299.36°, DEC=43.46°
        # We'll use a transformation sequence to correctly orient the rings
        
        # Step 1: Rotate around z-axis by the Right Ascension
    #    x_rot1, y_rot1, z_rot1 = rotate_points(x, y, z, pole_ra, 'z')
        
        # Step 2: Rotate around x-axis by (90° - Declination)
        # This aligns the z-axis with Neptune's pole
    #    x_rot2, y_rot2, z_rot2 = rotate_points(x_rot1, y_rot1, z_rot1, np.radians(90) - pole_dec, 'x')
        
        # Step 3: Apply final adjustment based on Neptune's specific orientation
        # This 25° rotation adjusts for the reference frame of Neptune's ring observations
    #    x_final, y_final, z_final = rotate_points(x_rot2, y_rot2, z_rot2, np.radians(25), 'z')

        # SIMPLIFIED TRANSFORMATION:
        # Instead of using RA/Dec-based transformations, we'll use a direct alignment
        # to match what we see in the image with Despina and Galatea's orbits
        
        # Transform ring coordinates to align with Neptune's equatorial plane
        # These angles were empirically determined to match the orbital plane of Despina and Galatea
        # First rotation: 32° around x-axis provides the primary tilt 
        tilt_angle = np.radians(32)
        x_rot1, y_rot1, z_rot1 = rotate_points(x, y, z, tilt_angle, 'x')

        # Second rotation: 34° around z-axis aligns with the final orientation
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
        'opacity': 0.3,
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
    
    return traces

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

pluto_mantel_info = (
            "2.1 MB PER FRAME FOR HTML.\n\n"
            "Mantel: Surrounding the rocky core is a mantle made of water ice. There's a compelling theory that a subsurface ocean \n" 
            "of liquid water, possibly mixed with ammonia, exists at the boundary between the core and the ice mantle. This ocean \n" 
            "could be 100 to 180 km thick. The presence of this ocean is supported by geological features observed on Pluto's surface."
)

def create_pluto_mantel_shell(center_position=(0, 0, 0)):
    """Creates pluto's mantel shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 0.99,  
        'color': 'rgb(150, 0, 0)',  # These still represent red but with a lower intensity,  
        'opacity': 0.9,
        'name': 'Mantel',
        'description': (
            "Mantel: Surrounding the rocky core is a mantle made of water ice. There's a compelling theory that a subsurface ocean <br>" 
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
    
    return traces

pluto_hill_sphere_info = (
            "SELECT MANUAL SCALE OF AT LEAST 1.0 AU TO VISUALIZE.\n" 
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
        'opacity': 0.3,
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
    
    return traces

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

eris_mantel_info = (
            "2.1 MB PER FRAME FOR HTML.\n\n"
            "Mantle: Surrounding the rocky core is a substantial mantle made of water ice. Unlike Pluto's ice shell, Eris's ice \n" 
            "mantle is thought to be convecting. This means that the warmer ice closer to the core rises, while the colder ice near \n" 
            "the surface sinks, a process that helps dissipate the internal heat generated by the core. The thickness of this ice \n" 
            "shell is estimated to be around 100 kilometers. There is currently no evidence to suggest the presence of a subsurface \n" 
            "ocean within Eris."
)

def create_eris_mantel_shell(center_position=(0, 0, 0)):
    """Creates Eris's mantle shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 0.66,  
        'color': 'rgb(150, 0, 0)',  # These still represent red but with a lower intensity,  
        'opacity': 0.9,
        'name': 'Mantel',
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
    
    return traces

eris_hill_sphere_info = (
            "SELECT MANUAL SCALE OF AT LEAST 1.0 AU TO VISUALIZE.\n" 
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
        'opacity': 0.3,
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
    
    return traces

# Planet 9

planet9_surface_info = (
            "USE MANUAL SCALED OF 0.005 AU TO VIEW CLOSELY."
            "4.6 MB PER FRAME FOR HTML.\n\n"
            "The estimation of Planet Nine's radius being between 3 and 4 Earth radii, with a specific estimate of around 3.7 Earth \n" 
            "radii (or 23,500 - 24,000 km), appears in several scientific discussions. This size estimate is often linked to the \n" 
            "assumption that Planet Nine is likely an ice giant, similar in composition to Uranus and Neptune, but potentially a \n" 
            "smaller version."
)

def create_planet9_surface_shell(center_position=(0, 0, 0)):
    """Creates eris's cloud layer shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 1.0,  # the top of the troposphere is actually 1.002
        'color': 'rgb(83, 68, 55)',  # optical brownish
        'opacity': 1.0,
        'name': 'Crust',
        'description': (
            "Planet 9 Surface<br>" 
            "(Note: toggle off the cloud layer in the legend to better see the interior structure.)<br><br>"
            "The estimation of Planet Nine's radius being between 3 and 4 Earth radii, with a specific estimate of around 3.7 Earth <br>" 
            "radii (or 23,500 - 24,000 km), appears in several scientific discussions. This size estimate is often linked to the <br>" 
            "assumption that Planet Nine is likely an ice giant, similar in composition to Uranus and Neptune, but potentially a <br>" 
            "smaller version.<br>" 
            "* Mass and Density Relationship: For a given mass, the radius of a planet is strongly influenced by its density.<br>" 
            "* Terrestrial Planets: Terrestrial planets (like Earth, Mars, Venus, Mercury) are primarily composed of rock and metal, <br>" 
            "  making them quite dense. If Planet Nine were a terrestrial planet with 5-10 times the mass of Earth, its radius would <br>" 
            "  likely be significantly smaller than 3-4 Earth radii due to its high density.<br>" 
            "* Gas Giants: Gas giants (like Jupiter and Saturn) are composed mostly of hydrogen and helium, making them very large and <br>" 
            "  not very dense. A planet with several Earth masses composed primarily of these light gases would have a much larger radius <br>" 
            "  than 3-4 Earth radii.<br>" 
            "* Ice Giants: Ice giants (like Uranus and Neptune) have a composition that includes heavier elements like oxygen, carbon, <br>" 
            "  nitrogen, and sulfur, often in the form of water, methane, and ammonia ices, along with a significant amount of hydrogen and <br>" 
            "  helium. This composition results in densities higher than gas giants but lower than terrestrial planets.<br>" 
            "The 3-4 Earth radii estimate, particularly the 3.7 Earth radii figure, comes from models that assume Planet Nine has a mass <br>" 
            "around 5-10 Earth masses and an internal composition similar to Uranus and Neptune. These models predict that such a planet <br>" 
            "would have a larger radius than Earth due to its significant mass, but not as large as a pure gas giant with the same mass due <br>" 
            "to the presence of heavier \"ice\" materials. Therefore, the estimated radius of 3-4 Earth radii strongly suggests that Planet <br>" 
            "Nine, if it exists, is likely an ice giant or a sub-Neptune type of planet, rather than a rocky terrestrial planet or a large <br>" 
            "gas giant. This is also consistent with theories about how a planet could have formed or been captured in the distant outer <br>" 
            "solar system."
            )
    }
    
    # Calculate radius in AU
    radius = layer_info['radius_fraction'] * PLANET9_RADIUS_AU
    
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
        name=f"Planet 9: {layer_info['name']}",
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
    layer_name = f"Planet 9: {layer_info['name']}"
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
        name=f"Planet 9: {layer_info['name']} (Info)",
        text=hover_texts,  # IMPORTANT: Matching length with coordinate arrays
        customdata=minimal_hover_texts,  # For "Object Names Only" mode
        hovertemplate='%{text}<extra></extra>',  # Use the standard hover template
        showlegend=False  # Don't show in legend since it's just for hover
    )

    return [surface_trace, hover_trace]

planet9_hill_sphere_info = (
            "SELECT MANUAL SCALE OF AT LEAST 8 AU TO VISUALIZE PLANET 9 CENTERED OR 800 AU HELIOCENTRIC.\n" 
            "1.3 MB PER FRAME FOR HTML.\n\n"

            "Hill Sphere: Planet 9's Hill sphere, or Roche sphere, is the region around it where its gravitational influence dominates \n" 
            "over the Sun's. The radius of Planet 9's Hill sphere is very large, approximately 7.6 AU."                     
)

def create_planet9_hill_sphere_shell(center_position=(0, 0, 0)):
    """Creates Planet 9's Hill sphere shell."""
    # Define layer properties
    layer_info = {
        'radius_fraction': 48000, # this is estimated based on the modeled data
        'color': 'rgb(0, 255, 0)',  # Green for Hill sphere
        'opacity': 0.3,
        'name': 'Hill Sphere',
        'description': (
            "SELECT MANUAL SCALE OF AT LEAST 8 AU TO VISUALIZE PLANET 9 CENTERED OR 800 AU HELIOCENTRIC.<br><br>"
            "Hill Sphere: Planet 9's Hill sphere, or Roche sphere, is the region around it where its gravitational influence dominates <br><br>" 
            "over the Sun's. The radius of Planet 9's Hill sphere is very large, approximately 7.6 AU.<br>" 
            "To arrive at the Hill sphere estimate of 7.6 AU, we made the following key assumptions about Planet Nine: <br>" 
            "* Semi-major axis (a): We assumed a semi-major axis of 600 AU. This value is within the range of 500-700 AU suggested <br>" 
            "  by some studies, including those considering the IRAS/AKARI observations. The semi-major axis is the average distance <br>" 
            "  of the planet from the Sun and has a direct linear relationship with the Hill sphere radius. A larger semi-major axis <br>" 
            "  leads to a larger Hill sphere.<br>" 
            "* Eccentricity (e): We assumed an eccentricity of 0.30. This value aligns with estimates that suggest a highly elliptical <br>" 
            "  orbit for Planet Nine, consistent with a perihelion around 280 AU and an aphelion around 1120 AU. The eccentricity <br>" 
            "  affects the Hill sphere radius because the formula uses the distance to the Sun at the perihelion. A higher eccentricity <br>" 
            "  would result in a smaller Hill sphere radius.<br>" 
            "* Mass of Planet Nine (m): We assumed a mass of 6 times the mass of Earth. This is within the generally accepted range of <br>" 
            "  a few to ten Earth masses, and close to some refined estimates. The mass of Planet Nine has a cubic root relationship <br>" 
            "  with the Hill sphere radius, meaning a larger mass leads to a larger Hill sphere, but the effect is less pronounced than <br>" 
            "  that of the semi-major axis.<br>" 
            "* Mass of the Sun (M): We used the standard value for the mass of the Sun. This is a well-established constant.<br>" 
            "* In summary: the region where Planet 9's gravity is strong enough to hold onto its own moons despite the Sun's pull is <br>" 
            "  what the Hill sphere represents. To estimate the radius of this safe zone, we take Planet Nine's average distance from <br>" 
            "  the Sun, which we're assuming to be 600 AU (that's 600 times the distance between the Earth and the Sun). Because <br>" 
            "  Planet Nine's orbit isn't a perfect circle but more of an oval shape (we call this eccentricity, and we're assuming <br>" 
            "  it's 0.30), the closest it gets to the Sun is a bit less than this average. To account for this, we consider the distance <br>" 
            "  at its closest approach, which is roughly its average distance multiplied by (one minus the eccentricity), <br>" 
            "  so 600AU×(1−0.30)=600AU×0.70=420AU. This closest distance is important because the Sun's gravity is strongest there, <br>" 
            "  making it harder for Planet Nine to hold onto moons. Now, we also need to consider how strong Planet Nine's gravity is <br>" 
            "  compared to the Sun's. We're assuming Planet Nine has a mass of 6 times the mass of the Earth. The Sun, of course, is <br>" 
            "  vastly more massive.<br>" 
            "* The full equation for calculating the Hill sphere radius is: r_Hill = a x (m/(3 x M))^(1/3). Where: a is the semi-major <br>" 
            "  axis of Eris's orbit around the Sun; m is the mass of Eris; M is the mass of the Sun."        
            )
    }
        
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * PLANET9_RADIUS_AU
    
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
            name=f"Planet 9: {layer_info['name']}",
            text=[layer_info['description']] * len(x),
            customdata=[f"Planet 9: {layer_info['name']}"] * len(x),
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    
    return traces