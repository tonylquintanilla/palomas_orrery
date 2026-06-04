"""
planet_visualization_utilities.py - Shared geometry helpers and body-radius aliases.

The shim layer between constants_new.py (pure numeric data) and the per-body
shell modules (mercury_visualization_shells.py, jupiter_visualization_shells.py,
etc.). Exposes convenience aliases like MERCURY_RADIUS_AU that shell modules
consume dozens of times, plus shared geometry functions (sphere point
generation, magnetosphere shaping, rotations) used across all planets.

Key functions:
    rotate_points(x, y, z, angle, axis) - rotate point cloud around an axis
    create_sphere_points(radius, n_points) - uniform sphere surface points
    create_magnetosphere_shape(params) - asymmetric magnetosphere geometry
    create_hover_markers_for_planet(center, radius, ...) - hover info trace

Consumed by: all *_visualization_shells.py modules, planet_visualization.py

Part of Paloma's Orrery - Data Preservation is Climate Action

Module updated: April 16, 2026 with Anthropic's Claude Opus 4.6
(provenance audit; solar/system constants now imported from constants_new.py
rather than redefined locally)

Module updated: April 17, 2026 with Anthropic's Claude Opus 4.7
(provenance audit; added SUN_RADIUS_KM re-export for comet_visualization_shells.py;
line endings normalized to LF)

Module updated: May 11, 2026 by Claude Opus 4.6 and 4.7 and Tony. (Sphere markers)

Module updated: June 2026 with Anthropic's Claude Opus 4.8
(shared create_bow_shock_shape extracted from 4 inline copies; conic-section model)
"""

import math
import numpy as np
import plotly.graph_objs as go
from constants_new import (
    KM_PER_AU, SUN_RADIUS_KM, LIGHT_MINUTES_PER_AU, KNOWN_ORBITAL_PERIODS,
    CENTER_BODY_RADII,
    # Solar structure
    SOLAR_RADIUS_AU, CORE_AU, RADIATIVE_ZONE_AU,
    # Solar atmosphere (in solar radii)
    CHROMOSPHERE_RADII, INNER_CORONA_RADII, OUTER_CORONA_RADII,
    STREAMER_BELT_RADII, ROCHE_LIMIT_RADII, ALFVEN_SURFACE_RADII,
    # Heliosphere and beyond
    TERMINATION_SHOCK_AU, HELIOPAUSE_RADII,
    INNER_LIMIT_OORT_CLOUD_AU, INNER_OORT_CLOUD_AU, OUTER_OORT_CLOUD_AU,
    GRAVITATIONAL_INFLUENCE_AU,
)

#####################################
# Body-radius aliases (derived from CENTER_BODY_RADII)
#####################################
# Shell modules consume these short names dozens of times each.
# Source of truth: CENTER_BODY_RADII in constants_new.py.
# See v3.20 protocol Option B: utility layer owns aliases, not constants_new.

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

# Eris Constants
# ERIS_RADIUS_KM = CENTER_BODY_RADII['Eris/Dysnomia']  # Equatorial radius in km
ERIS_RADIUS_KM = CENTER_BODY_RADII['Eris']  # Equatorial radius in km
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
    
    # Single info marker at north pole, 5% above radius — replaces former fibonacci sphere
    r_info = radius * 1.05

    hover_trace = go.Scatter3d(
        x=[center_x], y=[center_y], z=[center_z + r_info],
        mode='markers',
        marker=dict(size=6, color=color, opacity=0.9,
                    symbol='cross', line=dict(color='white', width=1)),
        name=f"{name} (Info)",
        legendgroup=f"{name} (Info)",
        text=[description],
        customdata=[name],
        hovertemplate='%{text}<extra></extra>',
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

# ============================================================================
# Bow shock shape generator (shared)
#
# Extracted June 2026 with Anthropic's Claude Opus 4.8 from the duplicated
# inline bow-shock blocks in mercury/venus/earth/mars _visualization_shells.py
# (four near-identical copies; see protocol "extract duplicated rendering into
# the source module"). Single source of truth for all planetary bow shocks.
#
# Geometry: surface of revolution about the -X (sunward) axis, nose sunward,
# flaring anti-sunward. Caller rotates to the real Sun direction via
# rotate_to_sunward() and offsets to center -- this function returns body-frame
# point clouds only, exactly as the original inline blocks did.
#
# Two shape modes:
#   eccentricity is None (DEFAULT) -> reproduces the original paraboloid
#       formula byte-for-byte: rho = width * (1 + sin(phi)) / 2. Used only as
#       the one-time extraction regression test (Earth legacy). NOT used in the
#       delivered render -- all bodies render via the conic path below.
#   eccentricity = e               -> standard conic-section model used
#       throughout the planetary bow-shock literature:
#           r(theta) = L / (1 + e*cos(theta)),  L = standoff * (1 + e)
#       focus at planet center, theta measured from the sunward (-X) axis.
#       (Trotignon et al. 2006; Edberg et al. 2008; Masters et al. 2008 /
#       Went et al. 2011; Simon Wedlund et al. 2022). Typical fitted
#       eccentricities are marginally hyperbolic: Mars e ~ 1.03-1.05,
#       Saturn e ~ 1.05, general e ~ 1.02-1.06. e = 1.05 is the illustrative
#       default. (A pure conic diverges far downstream -- Verigin et al. 2003 --
#       but is accurate from the nose through the terminator, the rendered
#       range.)
# ============================================================================

def create_bow_shock_shape(standoff, width, n_phi=30, n_theta=30,
                           eccentricity=None):
    """
    Generate body-frame point cloud for a bow shock surface of revolution.

    Parameters:
        standoff (float): subsolar nose distance from body center, in AU
                          (the physical, sourced quantity). Conic nose sits
                          exactly here.
        width (float): legacy paraboloid flank scale in AU. Used ONLY on the
                       paraboloid path (eccentricity=None). Ignored on the
                       conic path, where flank flare is set by eccentricity.
        n_phi, n_theta (int): grid resolution (legacy default 30x30).
        eccentricity (float or None): None -> legacy paraboloid (regression
                       test only); a float (typ. ~1.05) -> conic-section model
                       (the delivered shape).

    Returns:
        tuple: (x, y, z) lists in the body frame, nose toward -X.
    """
    import numpy as np

    bx, by, bz = [], [], []

    if eccentricity is None:
        # ---- Legacy paraboloid path: byte-for-byte the original formula ----
        for i_phi in range(n_phi):
            phi = (i_phi / (n_phi - 1)) * np.pi  # front half only
            x = -standoff * np.cos(phi)
            rho = width * (1 + np.sin(phi)) / 2
            for i_theta in range(n_theta):
                theta = (i_theta / (n_theta - 1)) * 2 * np.pi
                bx.append(x)
                by.append(rho * np.cos(theta))
                bz.append(rho * np.sin(theta))
        return bx, by, bz

    # ---- Conic-section path: r(a) = L / (1 + e*cos a), focus at center ----
    # 'a' is the polar angle from the sunward (-X) axis. a=0 -> nose at
    # r=L/(1+e)=standoff (sunward). Sweep a from 0 toward the asymptote to open
    # the flank; cap before the asymptote so the surface stays finite.
    e = float(eccentricity)
    L = standoff * (1.0 + e)  # so that r(0) = L/(1+e) = standoff exactly

    if e >= 1.0:
        a_asymptote = np.arccos(-1.0 / e)
        a_max = a_asymptote * 0.92  # MODE-5 KNOB: lower to cap flank flare
    else:
        a_max = np.pi  # ellipse: closes, no asymptote

    for i_phi in range(n_phi):
        a = (i_phi / (n_phi - 1)) * a_max
        r = L / (1.0 + e * np.cos(a))
        x = -r * np.cos(a)        # nose at -standoff (a=0)
        rho = r * np.sin(a)
        for i_theta in range(n_theta):
            theta = (i_theta / (n_theta - 1)) * 2 * np.pi
            bx.append(x)
            by.append(rho * np.cos(theta))
            bz.append(rho * np.sin(theta))

    return bx, by, bz


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
        "2. Neptune's unique magnetic field (47 deg tilt, 0.55 radius offset)<br>"
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



