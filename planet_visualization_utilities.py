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
    CENTER_BODY_RADII
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

# Moon Constants
MOON_RADIUS_KM = CENTER_BODY_RADII['Moon']
MOON_RADIUS_AU = MOON_RADIUS_KM / KM_PER_AU

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

def create_sun_direction_indicator_old(center_position=(0, 0, 0)):
    """Creates a visual indicator showing the direction to the Sun (along negative X-axis)."""
    center_x, center_y, center_z = center_position
    
    # Create a line pointing in the negative X direction (toward Sun)
    sun_direction_x = [center_x, center_x - 40 * NEPTUNE_RADIUS_AU]  # Line from planet toward Sun
    sun_direction_y = [center_y, center_y]
    sun_direction_z = [center_z, center_z]
    
    # Create the Sun direction indicator
    indicator_trace = go.Scatter3d(
        x=sun_direction_x,
        y=sun_direction_y,
        z=sun_direction_z,
        mode='lines+text',
        line=dict(
            color='yellow',
            width=3,
            dash='dash'
        ),
        text=['', 'Sun Direction'],  # Text at the end of the line
        textposition='middle right',
        textfont=dict(
            color='yellow',
            size=14,
        ),
        name='Sun Direction',
        showlegend=False,
        hoverinfo='none'
    )
    
    # Create a small sun symbol at the end of the line
    sun_symbol_trace = go.Scatter3d(
        x=[sun_direction_x[1]],
        y=[sun_direction_y[1]],
        z=[sun_direction_z[1]],
        mode='markers',
        marker=dict(
            size=6,
            color='yellow',
            symbol='circle',
            line=dict(
                color='orange',
                width=2
            )
        ),
        name='Sun Direction',
        hoverinfo='name',
        showlegend=False
    )
    
    # Create an informational hover point with explanation
    info_text = [
        "Direction to Sun: In the solar system, the Sun would be located in the negative X direction.<br><br>"
        "Neptune's magnetosphere orientation: This scientifically accurate visualization shows:<br>"
        "1. The bow shock facing the Sun, as it would in reality<br>"
        "2. Neptune's unique magnetic field (47° tilt, 0.55 radius offset)<br>"
        "3. A magnetotail that stretches away from the Sun but is influenced by Neptune's unusual field<br><br>"
        "This complex interaction creates a magnetosphere unlike any other in our solar system."
    ]
    
    info_trace = go.Scatter3d(
        x=[center_x - 5 * NEPTUNE_RADIUS_AU],  # Position the info point near the start of the line
        y=[center_y + 5 * NEPTUNE_RADIUS_AU],  # Offset from the line for visibility
        z=[center_z + 5 * NEPTUNE_RADIUS_AU],
        mode='markers',
        marker=dict(
            size=4,
            color='white',
            symbol='circle',
            opacity=0.7
        ),
        name='Neptune Magnetosphere Info',
        text=info_text,
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    )
    
    return [indicator_trace, sun_symbol_trace, info_trace]



