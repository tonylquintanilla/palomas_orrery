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
    
    # Single info marker at north pole, 5% above radius, replaces former fibonacci sphere
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




# ---------------------------------------------------------------------------
# Rotation-axis primitive (Movement 2, June 2026, Claude Opus 4.8).
# Shared builder for all shell bodies: spin-pole line + curved spin-direction
# arrow + one info marker. Direct consumer of the IAU pole vector from
# idealized_orbits.create_planet_transformation_matrix (the producer N15 built).
# Wired via CUSTOM_SHELLS['<body>']['rotation_axis'] with needs_planet_name=True;
# the dispatch passes planet_name so this one builder serves every body.
#
# Sourced rotation data below. Periods + obliquities: NASA NSSDCA Planetary Fact
# Sheet (D. R. Williams, NASA GSFC). Spin sense: NSSDCA signed rotation period +
# IAU WGCCRE prograde/retrograde W-dot convention (Archinal et al. 2018, Cel.
# Mech. Dyn. Astron. 130:22). Giants cross-checked to Voyager 2 (Uranus: Desch
# et al. 1986; Neptune: Lecacheux et al. 1993). Sun sidereal: Carrington (1863).
# half_len_frac is a Mode-5 knob: axis half-length as a multiple of body radius,
# sized to reach each body's outermost physical/field structure (Sun ~50 R_sun
# reaches the outer corona); excludes Hill sphere by construction.
# ---------------------------------------------------------------------------
PLANET_ROTATION = {
    'Sun':     {'period_str': '25.38 d sidereal (Carrington; differential 24.5-35 d)',
                'sense': 'prograde', 'obliquity_str': '7.25 deg to ecliptic',
                'note': 'Differential rotation; a gaseous body has no single solid-body day.',
                'half_len_frac': 50.0},
    'Mercury': {'period_str': '58.65 d (3:2 spin-orbit resonance)',
                'sense': 'prograde', 'obliquity_str': '0.034 deg',
                'note': 'Nearly upright; spin locked 3:2 to its orbit.',
                'half_len_frac': 2.0},
    'Venus':   {'period_str': '243.02 d (retrograde)',
                'sense': 'retrograde', 'obliquity_str': '177.4 deg',
                'note': 'Retrograde: spins backwards, axis points nearly south.',
                'half_len_frac': 2.0},
    'Earth':   {'period_str': '23.93 h',
                'sense': 'prograde', 'obliquity_str': '23.44 deg',
                'note': 'The familiar tilt that drives the seasons.',
                'half_len_frac': 3.0},
    'Moon':    {'period_str': '27.32 d (spin-orbit locked)',
                'sense': 'prograde', 'obliquity_str': '6.68 deg to orbit (1.54 deg to ecliptic)',
                'note': 'Tidally locked; J2000 mean pole (librates on the 18.6-yr node, a Cassini state).',
                'half_len_frac': 2.0},
    'Mars':    {'period_str': '24.62 h',
                'sense': 'prograde', 'obliquity_str': '25.19 deg',
                'note': 'Earth-like tilt, but no large moon to stabilize it.',
                'half_len_frac': 2.0},
    'Jupiter': {'period_str': '9.93 h (fastest spin of any planet)',
                'sense': 'prograde', 'obliquity_str': '3.13 deg',
                'note': 'Rapid spin visibly flattens the disk.',
                'half_len_frac': 2.5},
    'Saturn':  {'period_str': '10.66 h',
                'sense': 'prograde', 'obliquity_str': '26.73 deg',
                'note': "Tilt near Earth's; the rings share the equatorial plane.",
                'half_len_frac': 2.5},
    'Uranus':  {'period_str': '17.24 h (retrograde)',
                'sense': 'retrograde', 'obliquity_str': '97.77 deg',
                'note': 'Rolls on its side; axis lies nearly in the orbital plane.',
                'half_len_frac': 2.5},
    'Neptune': {'period_str': '16.11 h',
                'sense': 'prograde', 'obliquity_str': '28.32 deg',
                'note': 'Earth-like tilt despite its great distance.',
                'half_len_frac': 2.5},
    'Pluto':   {'period_str': '6.39 d (retrograde)',
                'sense': 'retrograde', 'obliquity_str': '122.53 deg',
                'note': 'High obliquity; tidally locked with Charon.',
                'half_len_frac': 2.0},
}

# Bodies deliberately WITHOUT a rotation axis -- the gap made visible (Fetched-vs-
# Recalled: do not invent unmeasured data). Note surfaced on the body hover.
ROTATION_AXIS_OMITTED = {
    'Planet 9': 'Rotation axis omitted: hypothetical body, no measured spin or pole.',
    'Eris': 'Rotation axis omitted: rotation contested (possibly tidally locked to '
            'Dysnomia); pole poorly constrained.',
}

_AXIS_COLOR = 'rgb(255, 209, 102)'  # warm gold, distinct from magnetosphere blues


def build_rotation_axis_traces(center_position=(0, 0, 0), planet_name=None,
                               sun_position=None):
    """Build the rotation-axis primitive for one body.

    Returns a list of plotly traces (6): a spin-pole line through the body
    center, a curved spin-direction arrow at EACH pole (arc + cone arrowhead),
    and one info marker carrying period/sense/obliquity in hover. The axis line
    is the IAU pole from the producer (create_planet_transformation_matrix), so
    this is a direct consumer of the pole vector. Spin SENSE comes from the
    explicit PLANET_ROTATION flag. Both arrows encode the same angular-velocity
    vector (identical circulation in 3-space), so the depiction does not depend
    on which end of the axis is "north" -- the IAU-pole vs angular-momentum-pole
    convention never surfaces. sun_position is accepted and ignored for
    dispatch-signature uniformity.

    Bodies with no sourced spin data return [] (no axis); the omission is noted
    on the body hover via ROTATION_AXIS_OMITTED.
    """
    info = PLANET_ROTATION.get(planet_name)
    if info is None:
        return []

    from idealized_orbits import create_planet_transformation_matrix  # lazy: heavy module

    cx, cy, cz = center_position
    center = np.array([cx, cy, cz], dtype=float)

    M = np.asarray(create_planet_transformation_matrix(planet_name), dtype=float)
    pole = M[:, 2] / np.linalg.norm(M[:, 2])   # spin pole, ecliptic frame
    e1 = M[:, 0] / np.linalg.norm(M[:, 0])      # equatorial-plane basis vectors
    e2 = M[:, 1] / np.linalg.norm(M[:, 1])

    body_r_au = CENTER_BODY_RADII.get(planet_name, 0.0) / KM_PER_AU
    half = info.get('half_len_frac', 2.0) * body_r_au
    if half <= 0:
        return []

    s = -1.0 if info.get('sense') == 'retrograde' else 1.0
    color = info.get('color', _AXIS_COLOR)
    legend = '%s: Rotation Axis' % planet_name

    traces = []

    # 1) pole line through the body center
    p_lo = center - half * pole
    p_hi = center + half * pole
    traces.append(go.Scatter3d(
        x=[p_lo[0], p_hi[0]], y=[p_lo[1], p_hi[1]], z=[p_lo[2], p_hi[2]],
        mode='lines', line=dict(color=color, width=4),
        name=legend, legendgroup=legend, showlegend=True, hoverinfo='skip'))

    # 2-3) curved spin-direction arrows at BOTH poles. Both arcs use the SAME
    # circulation in 3-space: every material point obeys v = omega x r, and a
    # point at the same perpendicular offset e1 has the same velocity at either
    # end, so the two arcs follow one angular-velocity vector -- not a flipped
    # sweep (that would draw a false counter-rotation). Viewed from opposite
    # poles the one circulation reads as mirror images on screen (e.g. Earth:
    # CCW from above the north pole, CW from below the south), which is how a
    # single rigid rotation actually looks. Drawing both ends makes the picture
    # independent of which end is labelled "north", so the IAU-pole vs
    # angular-momentum-pole convention never surfaces.
    arc_r = 0.28 * half
    sweep = np.radians(270.0)
    t = np.linspace(0.0, sweep, 60)
    cos_st = np.cos(s * t)[:, None]
    sin_st = np.sin(s * t)[:, None]
    tangent = s * (-np.sin(s * sweep) * e1 + np.cos(s * sweep) * e2)
    tangent = tangent / np.linalg.norm(tangent)
    for tip_sign in (1.0, -1.0):
        arc_at = center + tip_sign * half * pole
        arc = arc_at[None, :] + arc_r * (cos_st * e1[None, :] + sin_st * e2[None, :])
        traces.append(go.Scatter3d(
            x=arc[:, 0], y=arc[:, 1], z=arc[:, 2],
            mode='lines', line=dict(color=color, width=4),
            name=legend, legendgroup=legend, showlegend=False, hoverinfo='skip'))
        head = arc[-1]
        traces.append(go.Cone(
            x=[head[0]], y=[head[1]], z=[head[2]],
            u=[tangent[0]], v=[tangent[1]], w=[tangent[2]],
            sizemode='absolute', sizeref=arc_r * 0.5, anchor='tail',
            showscale=False, colorscale=[[0, color], [1, color]],
            name=legend, legendgroup=legend, showlegend=False, hoverinfo='skip'))

    # 4) single info marker at the north tip (hub of the spin ring)
    hover = ('<b>%s -- Rotation Axis</b><br>'
             'Sidereal rotation: %s<br>'
             'Direction: %s<br>'
             'Obliquity: %s<br>'
             '%s') % (planet_name, info['period_str'], info['sense'],
                      info['obliquity_str'], info['note'])
    traces.append(go.Scatter3d(
        x=[p_hi[0]], y=[p_hi[1]], z=[p_hi[2]], mode='markers',
        marker=dict(size=5, color=color, symbol='cross',
                    line=dict(color='white', width=1)),
        name=legend, legendgroup=legend, showlegend=False,
        text=[hover], hovertemplate='%{text}<extra></extra>'))

    return traces
