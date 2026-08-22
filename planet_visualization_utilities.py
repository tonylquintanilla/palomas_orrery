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

Module updated: July 2026 with Anthropic's Claude Sonnet 5 (L-162: nine
radius aliases -- Mercury, Venus, Moon, Mars, Saturn, Uranus, Neptune,
Pluto, Eris -- now imported directly from constants_new.py instead of
re-derived from CENTER_BODY_RADII; same values, same names)

Module updated: August 2026 with Anthropic's Claude Opus 5 (L-224:
create_streamer_band_shape -- helmet-and-stalk band geometry for the
solar streamer belt, per-point alpha so the stalk has no visible edge)

Role: rendering
Domain: orrery
"""

import math
import numpy as np
import plotly.graph_objs as go
from constants_new import (
    KM_PER_AU, SUN_RADIUS_KM, LIGHT_MINUTES_PER_AU, KNOWN_ORBITAL_PERIODS,
    CENTER_BODY_RADII,
    # L-162 (2026-07-29): named directly in constants_new.py now; these
    # nine no longer derive from a CENTER_BODY_RADII lookup below.
    MERCURY_RADIUS_KM, VENUS_RADIUS_KM, MOON_RADIUS_KM, MARS_RADIUS_KM,
    SATURN_RADIUS_KM, URANUS_RADIUS_KM, NEPTUNE_RADIUS_KM, PLUTO_RADIUS_KM,
    ERIS_RADIUS_KM,
    # Unit conversions
    AU_PER_LIGHT_YEAR,
    # Solar structure
    SOLAR_RADIUS_AU, CORE_AU, RADIATIVE_ZONE_AU,
    # Solar atmosphere (in solar radii)
    INNER_CORONA_RADII, OUTER_CORONA_RADII,
    CHROMOSPHERE_PHYSICAL_KM, CHROMOSPHERE_PHYSICAL_RADII,
    HELMET_CUSP_RADII, ROCHE_LIMIT_RADII, ALFVEN_SURFACE_RADII,
    # Heliosphere and beyond
    TERMINATION_SHOCK_AU, HELIOPAUSE_RADII,
    INNER_LIMIT_OORT_CLOUD_AU, INNER_OORT_CLOUD_AU, OUTER_OORT_CLOUD_AU,
    GRAVITATIONAL_INFLUENCE_AU, GRAVITATIONAL_INFLUENCE_RANGE_AU,
)

#####################################
# Body-radius aliases (derived from CENTER_BODY_RADII)
#####################################
# Shell modules consume these short names dozens of times each.
# Source of truth: CENTER_BODY_RADII in constants_new.py.
# See v3.20 protocol Option B: utility layer owns aliases, not constants_new.
# UPDATE (L-162, 2026-07-29): for the nine bodies below whose local alias
# name exactly matched a name now defined in constants_new.py (Mercury,
# Venus, Moon, Mars, Saturn, Uranus, Neptune, Pluto, Eris), that name is
# imported directly above instead of re-derived from CENTER_BODY_RADII --
# same value, one less lookup, and no more same-named pair invisible to
# provenance_scanner.py's CONCEPT_ALIASES check. Earth, Jupiter, Planet 9
# keep their original alias name (EARTH_RADIUS_KM etc., not the same
# string as constants_new.py's EARTH_EQUATORIAL_RADIUS_KM) and are
# unaffected -- outside L-162's scope.

# Mercury Constants (MERCURY_RADIUS_KM imported directly above; see L-162)
MERCURY_RADIUS_AU = MERCURY_RADIUS_KM / KM_PER_AU

# Venus Constants (VENUS_RADIUS_KM imported directly above; see L-162)
VENUS_RADIUS_AU = VENUS_RADIUS_KM / KM_PER_AU

# Earth Constants
EARTH_RADIUS_KM = CENTER_BODY_RADII['Earth']
EARTH_RADIUS_AU = EARTH_RADIUS_KM / KM_PER_AU

# Moon Constants (MOON_RADIUS_KM imported directly above; see L-162)
MOON_RADIUS_AU = MOON_RADIUS_KM / KM_PER_AU

# Mars Constants (MARS_RADIUS_KM imported directly above; see L-162)
# JPL uses an equipotential virtual surface with a mean radius at the
# equator as the Mars datum.
MARS_RADIUS_AU = MARS_RADIUS_KM / KM_PER_AU  # Convert to AU

# Jupiter Constants
JUPITER_RADIUS_KM = CENTER_BODY_RADII['Jupiter']  # Equatorial radius in km
JUPITER_RADIUS_AU = JUPITER_RADIUS_KM / KM_PER_AU  # Convert to AU

# Saturn Constants (SATURN_RADIUS_KM imported directly above; see L-162)
SATURN_RADIUS_AU = SATURN_RADIUS_KM / KM_PER_AU  # Convert to AU

# Uranus Constants (URANUS_RADIUS_KM imported directly above; see L-162)
URANUS_RADIUS_AU = URANUS_RADIUS_KM / KM_PER_AU  # Convert to AU

# Neptune Constants (NEPTUNE_RADIUS_KM imported directly above; see L-162)
NEPTUNE_RADIUS_AU = NEPTUNE_RADIUS_KM / KM_PER_AU  # Convert to AU

# Pluto Constants (PLUTO_RADIUS_KM imported directly above; see L-162)
PLUTO_RADIUS_AU = PLUTO_RADIUS_KM / KM_PER_AU  # Convert to AU

# Eris Constants (ERIS_RADIUS_KM imported directly above; see L-162)
# ERIS_RADIUS_KM = CENTER_BODY_RADII['Eris/Dysnomia']  # Equatorial radius in km -- historical, kept for context
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

def create_magnetosphere_shape(params, n_phi=20, n_theta=20,
                               n_tail_segments=10):
    """
    Creates points for a magnetosphere with asymmetry, compressed on sunward side
    and extended on the tail side.

    Parameters:
        params (dict): Dictionary of shape parameters
        n_phi (int): Sunward-hemisphere polar resolution (default 20 --
            the pre-promotion literal; callers passing nothing render
            byte-identical output). Phase 4: promoted to a keyword so
            per-frame callers can request reduced density if a future
            budget requires it (measured June 2026: full resolution plus
            7-decimal coordinate rounding already fits the per-frame
            budget, so the defaults are also the per-frame values).
        n_theta (int): Azimuthal resolution (default 20).
        n_tail_segments (int): Magnetotail axial segments (default 10).

    Returns:
        tuple: (x, y, z) coordinates as lists
    """
    x_coords = []
    y_coords = []
    z_coords = []
    
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


# ---------------------------------------------------------------------------
# Magnetic dipole-cone primitive (Movement 2).
# Module section added: June 2026 with Anthropic's Claude Opus 4.8.
#
# A body's magnetic dipole is fixed in the body frame at a tilt from the spin
# axis, but the planet's rotation carries it around the spin axis -- so over one
# rotation the dipole axis sweeps a cone (half-angle = the dipole tilt) about the
# spin pole. PLANET_DIPOLE carries only the dipole-specific data; sense and
# half_len_frac are read from PLANET_ROTATION so the cone shares the rotation
# axis's sense and scale (single source of truth, no drift).
#
# azimuth_deg is the roll of the single drawn generator and is ARBITRARY by
# construction: the rotation phase is not modeled, and the period uncertainty
# smears the inertial azimuth around the full circle since Voyager, so the
# instantaneous azimuth is unrecoverable, not merely unmodeled. The cone shows
# the whole sweep so no single azimuth is claimed; the lone generator carries a
# sweep arrow to read as motion rather than a fixed position. The dipole's
# physical center offset (magnitude sourced, direction not) is DEFERRED -- apex
# stays at center until the direction is sourced (Mode-7), per Fetched-vs-Recalled.
#
# Only bodies with a sourced dipole tilt appear. Others are omitted, the gap left
# visible rather than guessed (Earth ~11 deg, Jupiter ~10 deg, Saturn <1 deg,
# Mercury ~0 deg: deferred pending sourced tilt + sense, their own entries later).
# ---------------------------------------------------------------------------
# Movement 2, dipole cluster (L-009 / L-006). Tilts, offsets, and sources are
# peer-reviewed mission data (Gemini de-novo, June 2026); the recalled values
# are retired. offset_fraction shifts the cone apex by that fraction of the body
# radius northward along the IAU spin pole (axial approximation -- offset_note
# discloses the real geometry). Mercury and Saturn are tilt ~ 0: the cone
# collapses to the spin axis (the honest envelope of a zero-tilt dipole), so the
# builder renders the offset axis line + info marker, not a faked wider cone.
# Cone tilt values are rounded to 0.1 deg (cone projection cannot honor finer);
# the exact source figure rides in 'note'. Uranus/Neptune omit offset_fraction
# (-> 0.0) and offset_note (-> "deferred"), rendering unchanged.
# Module updated: June 2026 with Anthropic's Claude Opus 4.8.
PLANET_DIPOLE = {
    'Mercury': {'tilt_deg': 0.0, 'azimuth_deg': 0.0, 'offset_fraction': 0.19,
                'offset_note': 'Center offset: 0.19 +/- 0.01 R_M northward, axial '
                               '(~480 km); no measurable equatorial offset',
                'note': 'Tilt is statistically indistinguishable from zero '
                        '(< 1 deg); modeled as a purely axial offset dipole -- '
                        'the envelope of a zero-tilt dipole is the axis line itself',
                'source': 'Anderson et al. 2011, MESSENGER (Science 333, 1859)'},
    'Earth':   {'tilt_deg': 9.6, 'azimuth_deg': 0.0, 'offset_fraction': 0.085,
                'offset_note': 'Center offset: ~0.085 R_E northward, axial '
                               'approximation (~540 km); the true center is also '
                               'displaced laterally toward ~22 N, 140 E '
                               '(secular variation, unmodeled here)',
                'note': 'Tilt ~9.6 deg for epoch 2020-2025 (IGRF-13); slowly '
                        'decreasing ~0.05 deg/decade',
                'source': 'Alken et al. 2021, IGRF-13 (Earth Planets Space 73, 49)'},
    'Jupiter': {'tilt_deg': 10.3, 'azimuth_deg': 0.0, 'offset_fraction': 0.12,
                'offset_note': 'Center offset: ~0.12 R_J, axial approximation; the '
                               'true shift is toward the N hemisphere and the '
                               'System III active longitude (rotation phase '
                               'unmodeled)',
                'note': 'Tilt ~10.3 deg: the JRM33 close-in dipole is 10.31 deg '
                        '(Connerney 2022); the planet-wide integrated dipole '
                        'reads ~9.6 deg',
                'source': 'Connerney et al. 2022, JRM33 (JGR Planets 127(2))'},
    'Saturn':  {'tilt_deg': 0.0, 'azimuth_deg': 0.0, 'offset_fraction': 0.045,
                'offset_note': 'Center offset: ~0.045 R_S northward, axial '
                               '(midpoint of measured 0.04-0.05 R_S); no '
                               'measurable equatorial offset',
                'note': 'Tilt < 0.01 deg -- the magnetic and spin axes are '
                        'co-axial. Deep helium-rain differential rotation acts as '
                        'an axisymmetric filter (the Cowling-theorem paradox)',
                'source': 'Dougherty et al. 2018, Cassini Grand Finale (Science 362)'},
    'Uranus':  {'tilt_deg': 60.0, 'azimuth_deg': 35.0,
                'source': 'Ness et al. 1986, Voyager 2 magnetometer (Science 233, 85)'},
    'Neptune': {'tilt_deg': 47.0, 'azimuth_deg': 35.0,
                'source': 'Ness et al. 1989, Voyager 2 (Science 246, 1473)'},
}

_DIPOLE_COLOR = 'rgb(255, 93, 210)'  # magenta; distinct from rotation-axis gold and field blues


def build_dipole_cone_traces(center_position=(0, 0, 0), planet_name=None,
                             sun_position=None):
    """Build the magnetic dipole-cone primitive for one body (Movement 2).

    Draws the cone the body-fixed dipole sweeps about the spin axis as the planet
    rotates: a double nappe (the dipole is two-ended), half-angle = the dipole
    tilt, hung on the IAU spin pole from create_planet_transformation_matrix.
    Adds ONE instantaneous dipole generator with a sweep arrow at each tip; the
    arrow rides the cone RIM (a circle about the SPIN axis) with the same sense
    and absolute arrowhead size as the rotation-axis spin arrow, so the dipole's
    sweep reads as the same rotation. The drawn azimuth is arbitrary by
    construction; the cone is the honest object and the generator asserts motion,
    not a fixed position.

    Pole frame, Sun-independent: sits square to the rings and radiation belts and
    does NOT track the Sun-leaned magnetosphere envelope (a different frame --
    the envelope's tilt is a roll about the Sun-line). The apex is offset
    northward along the spin pole by offset_fraction * body_radius (axial
    approximation; offset_note in PLANET_DIPOLE discloses the real geometry).
    Bodies that omit offset_fraction (Uranus/Neptune) keep apex at center.

    Near-zero tilt (Mercury, Saturn): the cone half-angle -> 0, so the nappe rim
    and the sweep-arc radius both collapse onto the spin axis. The honest object
    is then the axis line itself (Show the Envelope of the Unknowable -- a faked
    wider cone would be the cite-over-recalled failure class), so for tilt below
    _TILT_EPS_DEG the builder emits only the generator line (= offset spin axis)
    and the info marker, skipping the degenerate nappes and sweep arrows.

    Returns up to 8 traces for a tilted dipole (2 cone nappes, 1 generator line,
    2 rim arcs, 2 arrowheads, 1 info marker); 2 traces (generator line + info
    marker) for a near-zero-tilt body; or [] for bodies with no sourced dipole
    tilt (intentional omission, not a failure). sun_position is accepted and
    ignored for dispatch-signature uniformity with the other shared builders.

    Module updated: June 2026 with Anthropic's Claude Opus 4.8.
    """
    dip = PLANET_DIPOLE.get(planet_name)
    rot = PLANET_ROTATION.get(planet_name)
    if dip is None or rot is None:
        return []

    from idealized_orbits import create_planet_transformation_matrix  # lazy: heavy module

    cx, cy, cz = center_position
    center = np.array([cx, cy, cz], dtype=float)

    M = np.asarray(create_planet_transformation_matrix(planet_name), dtype=float)
    pole = M[:, 2] / np.linalg.norm(M[:, 2])      # IAU north pole (verified northward)
    e1 = M[:, 0] / np.linalg.norm(M[:, 0])
    e2 = M[:, 1] / np.linalg.norm(M[:, 1])

    body_r_au = CENTER_BODY_RADII.get(planet_name, 0.0) / KM_PER_AU
    half = rot.get('half_len_frac', 2.5) * body_r_au
    if half <= 0:
        return []

    # Dipole-center offset: shift the apex northward along the spin pole by
    # offset_fraction of the body radius. Axial approximation; the lateral and
    # phase-locked components are unmodeled (disclosed in offset_note).
    offset_frac = dip.get('offset_fraction', 0.0)
    apex = center + (offset_frac * body_r_au) * pole

    s = -1.0 if rot.get('sense') == 'retrograde' else 1.0
    theta = math.radians(dip['tilt_deg'])
    az = math.radians(dip.get('azimuth_deg', 0.0))
    color = _DIPOLE_COLOR
    legend = '%s: Dipole Cone' % planet_name

    cos_t, sin_t = math.cos(theta), math.sin(theta)
    dip_dir = cos_t * pole + sin_t * (math.cos(az) * e1 + math.sin(az) * e2)

    # Degenerate gate: below this tilt the cone is visually a line; render the
    # axis, not a surface. (Saturn < 0.01 deg, Mercury < 1 deg.)
    _TILT_EPS_DEG = 0.5
    degenerate = dip['tilt_deg'] < _TILT_EPS_DEG

    traces = []

    if not degenerate:
        # 1-2) double-nappe cone, apex at apex, rim at +/- half*cos_t along pole
        n_phi = 72
        phis = np.linspace(0.0, 2.0 * np.pi, n_phi, endpoint=False)
        radial = (np.cos(phis)[:, None] * e1[None, :]
                  + np.sin(phis)[:, None] * e2[None, :])
        for nap_i, nap_sign in enumerate((1.0, -1.0)):
            ring = apex + (nap_sign * half * cos_t) * pole + (half * sin_t) * radial
            xs = np.concatenate([[apex[0]], ring[:, 0]])
            ys = np.concatenate([[apex[1]], ring[:, 1]])
            zs = np.concatenate([[apex[2]], ring[:, 2]])
            ii = [0] * n_phi
            jj = [1 + m for m in range(n_phi)]
            kk = [1 + ((m + 1) % n_phi) for m in range(n_phi)]
            traces.append(go.Mesh3d(
                x=xs, y=ys, z=zs, i=ii, j=jj, k=kk, color=color, opacity=0.16,
                flatshading=True, showscale=False, hoverinfo='skip',
                name=legend, legendgroup=legend, showlegend=(nap_i == 0)))

    # generator: full line through both magnetic poles, hung on the apex. For a
    # degenerate body this IS the (offset) spin axis, and it carries the legend
    # entry since there is no nappe to.
    g_lo = apex - half * dip_dir
    g_hi = apex + half * dip_dir
    traces.append(go.Scatter3d(
        x=[g_lo[0], g_hi[0]], y=[g_lo[1], g_hi[1]], z=[g_lo[2], g_hi[2]],
        mode='lines', line=dict(color=color, width=5),
        name=legend, legendgroup=legend,
        showlegend=degenerate, hoverinfo='skip'))

    if not degenerate:
        # sweep arrow at each tip: arc of the cone RIM (a circle about the SPIN
        # axis) + a cone arrowhead, same sense and absolute size as the
        # rotation-axis spin arrow, so the dipole's sweep reads as the spin.
        arc_r = 0.28 * half      # rotation-axis arc scale -> matching arrowhead sizeref
        sizeref = arc_r * 0.5
        rim_r = half * sin_t
        span = math.radians(90.0)
        tau = np.linspace(0.0, span, 40)
        for tip_sign, start_az in ((1.0, az), (-1.0, az + math.pi)):
            rim_center = apex + (tip_sign * half * cos_t) * pole
            phi = start_az + s * tau
            pts = rim_center + rim_r * (np.cos(phi)[:, None] * e1[None, :]
                                        + np.sin(phi)[:, None] * e2[None, :])
            traces.append(go.Scatter3d(
                x=pts[:, 0], y=pts[:, 1], z=pts[:, 2], mode='lines',
                line=dict(color=color, width=4),
                name=legend, legendgroup=legend, showlegend=False, hoverinfo='skip'))
            pe = float(phi[-1])
            tangent = s * (-math.sin(pe) * e1 + math.cos(pe) * e2)
            tangent = tangent / np.linalg.norm(tangent)
            traces.append(go.Cone(
                x=[pts[-1, 0]], y=[pts[-1, 1]], z=[pts[-1, 2]],
                u=[tangent[0]], v=[tangent[1]], w=[tangent[2]],
                sizemode='absolute', sizeref=sizeref, anchor='tail', showscale=False,
                colorscale=[[0, color], [1, color]],
                name=legend, legendgroup=legend, showlegend=False, hoverinfo='skip'))

    # single info marker at the +tip (single-info-marker convention). Per-body
    # hover: tilt at 0.1-deg resolution, offset disclosure, and the sourced note
    # (Jupiter dual-reading, Saturn midpoint/Cowling, Mercury/Saturn degeneracy).
    tip = apex + half * dip_dir
    lines = ['<b>%s -- Magnetic Dipole Cone</b>' % planet_name]
    if degenerate:
        lines.append('Dipole tilt: ~%.1f deg -- magnetic axis is co-axial with '
                     'the spin pole to within measurement' % dip['tilt_deg'])
    else:
        lines.append('Dipole tilt: ~%.1f deg from the spin axis' % dip['tilt_deg'])
        lines.append('Swept about the spin axis once per rotation (sense: %s)'
                     % rot.get('sense'))
        lines.append('Drawn axis is ONE arbitrary instant; the cone is the honest sweep')
    if 'offset_note' in dip:
        lines.append(dip['offset_note'])
    elif offset_frac > 0:
        lines.append('Center offset: ~%.3f body radii northward (axial)' % offset_frac)
    else:
        lines.append('Center offset deferred (apex at center)')
    if 'note' in dip:
        lines.append(dip['note'])
    lines.append('Source: %s' % dip['source'])
    hover = '<br>'.join(lines)
    traces.append(go.Scatter3d(
        x=[tip[0]], y=[tip[1]], z=[tip[2]], mode='markers',
        marker=dict(size=5, color=color, symbol='cross',
                    line=dict(color='white', width=1)),
        name=legend, legendgroup=legend, showlegend=False,
        text=[hover], hovertemplate='%{text}<extra></extra>'))

    return traces


# =========================================================================
# Streamer band geometry (L-224)
# =========================================================================
# Shared shape generator, same contract as create_magnetosphere_shape and
# create_bow_shock_shape above: a params dict in, body-frame point arrays
# out, and the CALLER does placement, scaling and trace construction.
# Placed here rather than inline in solar_visualization_shells.py for the
# reason create_bow_shock_shape was extracted from four inline copies in
# June 2026 -- shaped geometry has one home.
#
# It returns FIVE arrays where its siblings return three. The extra two
# are per-point alpha and marker size, and they are the whole point: the
# streamer stalk has no outer edge, so it must dissolve rather than stop,
# and Plotly's marker.opacity is a scalar while marker.color and
# marker.size accept per-point arrays. Fading through a colour array is
# therefore the only way to draw an edgeless object in one trace.
#
# Units are SOLAR RADII throughout. The caller scales to AU.

STREAMER_BAND_DEFAULTS = {
    # --- radial structure -------------------------------------------
    'base_radius': 1.0,        # photosphere; the band starts at the surface
    'cusp_radius': 4.0,        # the pinch -- where closed loops open
    'fade_radius': 19.7,       # alpha reaches ZERO here (Alfven surface)
    'outer_radius': 20.0,      # last generated point, already invisible
    # --- the silhouette ---------------------------------------------
    'base_half_width_deg': 38.0,   # arcade footprint along the neutral line
    'cusp_half_width_deg': 9.0,    # the narrowest point
    'helmet_exponent': 1.7,        # >1 stays wide, then pinches near the cusp
    'stalk_taper': 0.45,           # further narrowing of the stalk, fractional
    'fade_exponent': 1.8,          # >1 dissolves; 1.0 smears
    # --- the warp (ONE configuration, near solar minimum) ------------
    'warp_amp_deg': 15.0,      # neutral-line tilt off the equator
    'warp_lobes': 2,           # two-lobe warp: the ballerina skirt
    # --- sampling ----------------------------------------------------
    'n_radial_helmet': 12,
    'n_radial_stalk': 30,
    'n_lon': 32,
    'n_lat': 5,
    'jitter': 0.42,            # fraction of local spacing; kills ring artifacts
    'seed': 20260822,          # seeded so the render is reproducible
    # --- appearance ---------------------------------------------------
    'max_alpha': 0.55,
    'base_marker_size': 3.2,
    'tip_marker_size': 1.4,
}


def create_streamer_band_shape(params=None):
    """Point cloud for a helmet-and-stalk streamer band (L-224).

    The streamer belt is not a shell and has no single radius. Below the
    cusp it is a closed magnetic arcade over the neutral line -- wide,
    dense, and bounded. Above the cusp it is an open stalk along the
    current sheet, which thins into the slow solar wind and has no outer
    edge at all. This generator draws both as ONE object whose character
    changes with radius, which is what they are.

    Returns
    -------
    (xs, ys, zs, alphas, sizes) : five equal-length lists
        Positions in SOLAR RADII in the body frame; per-point alpha in
        [0, max_alpha]; per-point marker size. Feed alphas into an rgba
        colour array and sizes into marker.size -- see
        solar_visualization_shells.create_sun_streamer_band.

    Two invariants worth knowing before changing anything here.

    NO VISIBLE EDGE, BY CONSTRUCTION. Alpha is evaluated at each point's
    OWN jittered radius, never at the radius of the shell it was sampled
    from. That is deliberate: with per-shell alpha, a point jittered
    outward past fade_radius would carry a non-zero alpha from inside it
    and draw a stray edge. Evaluating per point makes that impossible
    rather than unlikely. Points continue to outer_radius with alpha
    already at zero, so the array has a terminus and the screen does not.

    REPRODUCIBLE. Jitter comes from a seeded RandomState, not the global
    one, so two runs give byte-identical geometry. The sibling Oort
    builders in solar_visualization_shells.py use unseeded np.random and
    do re-roll every render; that is their existing behaviour, not a
    pattern to copy for anything a reference artifact will fingerprint.
    """
    import math

    p = dict(STREAMER_BAND_DEFAULTS)
    if params:
        p.update(params)

    base_r, cusp_r = float(p['base_radius']), float(p['cusp_radius'])
    fade_r, out_r = float(p['fade_radius']), float(p['outer_radius'])
    base_w = math.radians(float(p['base_half_width_deg']))
    cusp_w = math.radians(float(p['cusp_half_width_deg']))
    warp = math.radians(float(p['warp_amp_deg']))
    lobes = int(p['warp_lobes'])
    helm_e, fade_e = float(p['helmet_exponent']), float(p['fade_exponent'])
    taper, a_max = float(p['stalk_taper']), float(p['max_alpha'])
    s0, s1 = float(p['base_marker_size']), float(p['tip_marker_size'])
    jit = float(p['jitter'])
    n_h, n_s = int(p['n_radial_helmet']), int(p['n_radial_stalk'])
    rs = np.random.RandomState(int(p['seed']))

    span = max(1e-9, fade_r - cusp_r)

    def _fade_fraction(r):
        return min(1.0, max(0.0, (r - cusp_r) / span))

    def alpha_at(r):
        if r <= cusp_r:
            return a_max
        return a_max * (1.0 - _fade_fraction(r)) ** fade_e

    def size_at(r):
        if r <= cusp_r:
            return s0
        return s0 + (s1 - s0) * _fade_fraction(r)

    d_h = (cusp_r - base_r) / max(1, n_h - 1)
    d_s = (out_r - cusp_r) / max(1, n_s - 1)
    shells = ([(r, True) for r in np.linspace(base_r, cusp_r, n_h)] +
              [(r, False) for r in np.linspace(cusp_r, out_r, n_s)[1:]])

    xs, ys, zs, alphas, sizes = [], [], [], [], []
    for r_shell, in_helmet in shells:
        if in_helmet:
            t = 0.0 if cusp_r == base_r else (r_shell - base_r) / (cusp_r - base_r)
            t = min(1.0, max(0.0, t))
            half_w = cusp_w + (base_w - cusp_w) * (1.0 - t) ** helm_e
            n_lon, n_lat, step = int(p['n_lon']), int(p['n_lat']), d_h
        else:
            u = min(1.0, max(0.0,
                             (r_shell - cusp_r) / max(1e-9, out_r - cusp_r)))
            half_w = cusp_w * (1.0 - taper * u)
            # Density thins outward as well as alpha. Opacity alone reads
            # as a uniform sheet turned down; thinning reads as a sheet
            # coming apart, which is what actually happens.
            n_lon = max(10, int(round(int(p['n_lon']) * (1.0 - 0.70 * u))))
            n_lat = max(3, int(round(int(p['n_lat']) * (1.0 - 0.45 * u))))
            step = d_s
        lat_jit = half_w * jit / max(1, n_lat - 1)
        for lon in np.linspace(0.0, 2 * math.pi, n_lon, endpoint=False):
            # The neutral line is warped, not flat. This is the ballerina
            # skirt at its origin, in ONE configuration near solar minimum.
            lam0 = warp * math.sin(lobes * lon)
            for off in np.linspace(-half_w, half_w, n_lat):
                r_pt = min(out_r, max(base_r,
                                      r_shell + jit * step * rs.uniform(-1.0, 1.0)))
                lam = lam0 + off + lat_jit * rs.uniform(-1.0, 1.0)
                cos_lam = math.cos(lam)
                xs.append(r_pt * cos_lam * math.cos(lon))
                ys.append(r_pt * cos_lam * math.sin(lon))
                zs.append(r_pt * math.sin(lam))
                alphas.append(round(alpha_at(r_pt), 4))
                sizes.append(round(size_at(r_pt), 3))

    return xs, ys, zs, alphas, sizes
