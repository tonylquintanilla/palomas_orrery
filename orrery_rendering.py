"""
orrery_rendering.py - Rendering contract between plot_objects and animate_objects.

Owns the generic sphere shell builder and the centralized info marker factory,
both consumed by the unified shell dispatch and individual shell modules.
Layout extraction (build_orrery_layout, _build_scene_axes, _build_annotations)
and finalization (finalize_orrery_figure) will be added in Step 4 of the
plotting consolidation.

Key functions:
    create_info_marker() - single cross marker carrying hover text (universal)
    build_sphere_shell()  - generic sphere shell from config dict (Step 3, Phase A)

Consumed by: planet_visualization.py (dispatch loop),
             *_visualization_shells.py (custom geometry info markers)

Module updated: May 2026 with Anthropic's Claude Opus 4.7
May 27, 2026: Stage 3 info-marker standard sweep complete (Opus 4.7).
    create_info_marker docstring updated with completed-migration intent
    paragraph. The factory style is now the canonical info marker style
    across the codebase; old white-border inline patterns retired except
    for documented red-on-red exceptions.
"""

import numpy as np
import plotly.graph_objs as go

from constants_new import CENTER_BODY_RADII, KM_PER_AU
from planet_visualization_utilities import create_sphere_points


def create_info_marker(x, y, z, color, text, legendgroup, customdata=None):
    """Create a single info marker trace.

    Canonical info marker style for the orrery. Size 8, opacity 1.0,
    cross symbol, red border width 2. Centralizes the style so all info
    markers across the orrery are visually consistent and can be
    updated in one place.

    Migration status (May 27, 2026 -- Stage 3 sweep complete):
        All planetary and solar shell modules now use this style (either
        via this factory or via inline marker dicts that match it). The
        old "white border, size 6, opacity 0.9" inline pattern is fully
        retired except for a small set of documented red-on-red
        exceptions where a red fill would lose contrast against a red
        border. Each exception carries an inline comment explaining the
        rule. Modules audited and converted:
            asteroid_belt, earth, eris, jupiter, mars, moon, neptune,
            planet9, pluto, saturn, solar, uranus, venus.

        New info markers should call this factory directly. New inline
        marker dicts (when the factory isn't applicable) should match
        the style above. New red-on-red exceptions require an inline
        comment.

    Parameters:
        x, y, z (float): Position coordinates
        color (str): Marker fill color (rgb string)
        text (str): Hover text content
        legendgroup (str): Legend group to toggle with geometry
        customdata (str): Optional customdata value (defaults to legendgroup)

    Returns:
        plotly Scatter3d trace
    """
    return go.Scatter3d(
        x=[x], y=[y], z=[z],
        mode='markers',
        marker=dict(size=8, color=color, opacity=1.0,
                    symbol='cross', line=dict(color='red', width=2)),
        name='',
        legendgroup=legendgroup,
        text=[text],
        customdata=[customdata if customdata is not None else legendgroup],
        hovertemplate='%{text}<extra></extra>',
        hoverlabel=dict(font=dict(size=11)),
        showlegend=False
    )


def build_sphere_shell(config, body_name, center_position=(0, 0, 0)):
    """Generic sphere shell from config dict.

    Structurally enforces the single-info-marker pattern:
    one geometry trace with hoverinfo='skip' plus one cross marker
    at the north pole carrying the full hover text exactly once.

    Accepts either:
        config['radius_fraction'] - multiplied by body radius from CENTER_BODY_RADII
        config['radius_au']       - used directly (Sun shells)

    Required config keys:
        name              str    Display name (e.g. 'Inner Core')
        color             str    rgb(...) string
        opacity           float
        hover_text        str    info marker hover string (3D plot)
        radius_fraction OR radius_au  (one must be present)

    Required for scatter3d (default):
        marker_size       float  size of geometry markers

    Optional config keys:
        n_points          int    Sphere resolution (default 20)
        geometry_type     str    'scatter3d' (default, dot sphere) or
                                 'mesh3d' (triangulated solid surface)
        mesh_resolution   int    UV sphere resolution for mesh3d (default 24)

    Returns:
        list of two plotly traces: [geometry, info_marker]
    """
    # Resolve radius
    if 'radius_au' in config:
        radius_au = config['radius_au']
    elif 'radius_fraction' in config:
        body_radius_au = CENTER_BODY_RADII[body_name] / KM_PER_AU
        radius_au = config['radius_fraction'] * body_radius_au
    else:
        raise ValueError(
            "build_sphere_shell: config for %s/%s missing both "
            "'radius_fraction' and 'radius_au'" % (body_name, config.get('name', '?'))
        )

    center_x, center_y, center_z = center_position
    trace_name = "%s: %s" % (body_name, config['name'])
    geometry_type = config.get('geometry_type', 'scatter3d')

    if geometry_type == 'mesh3d':
        # Triangulated solid surface -- used for crusts and cloud layers.
        # Flat-shaded with full ambient light for uniform color (no specular/
        # diffuse shading that creates unrealistic lighting on small bodies).
        resolution = config.get('mesh_resolution', 24)

        phi = np.linspace(0, 2 * np.pi, resolution)
        theta = np.linspace(-np.pi / 2, np.pi / 2, resolution)
        phi, theta = np.meshgrid(phi, theta)

        x = radius_au * np.cos(theta) * np.cos(phi) + center_x
        y = radius_au * np.cos(theta) * np.sin(phi) + center_y
        z = radius_au * np.sin(theta) + center_z

        # Triangulate the UV grid
        indices = []
        for i in range(resolution - 1):
            for j in range(resolution - 1):
                p1 = i * resolution + j
                p2 = i * resolution + (j + 1)
                p3 = (i + 1) * resolution + j
                p4 = (i + 1) * resolution + (j + 1)
                indices.append([p1, p2, p4])
                indices.append([p1, p4, p3])

        shell_trace = go.Mesh3d(
            x=x.flatten(), y=y.flatten(), z=z.flatten(),
            i=[idx[0] for idx in indices],
            j=[idx[1] for idx in indices],
            k=[idx[2] for idx in indices],
            color=config['color'],
            opacity=config['opacity'],
            name=trace_name,
            legendgroup=trace_name,
            showlegend=True,
            hoverinfo='skip',
            flatshading=True,
            lighting=dict(
                ambient=1.0, diffuse=0.0, specular=0.0,
                roughness=1.0, fresnel=0.0
            ),
            lightposition=dict(x=0, y=0, z=10000)
        )

    else:
        # Default: Scatter3d dot sphere
        n_points = config.get('n_points', 20)
        x, y, z = create_sphere_points(radius_au, n_points=n_points)
        x = x + center_x
        y = y + center_y
        z = z + center_z

        shell_trace = go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=config['marker_size'],
                color=config['color'],
                opacity=config['opacity']
            ),
            name=trace_name,
            legendgroup=trace_name,
            hoverinfo='skip',
            showlegend=True
        )

    # Single info marker at north pole, 5% above radius
    # Rule 2 prepend: legend label as structural header so hover reads
    # "Body: Shell" then blank line then description (D3.1 follow-up,
    # May 2026 -- fills the dispatch-path blind spot that the per-body
    # sweep missed).
    r_info = radius_au * 1.05
    info_trace = create_info_marker(
        center_x, center_y, center_z + r_info,
        config['color'],
        "%s<br><br>%s" % (trace_name, config['hover_text']),
        trace_name
    )

    return [shell_trace, info_trace]


def rotate_to_sunward(px, py, pz, center_position=(0, 0, 0),
                     sun_position=(0, 0, 0), magnetic_tilt_deg=0):
    """Rotate points from default -X sunward to actual sunward direction.

    Default geometry generation convention: magnetosphere structures (bow
    shock, magnetotail, etc.) are generated with -X as the sunward direction
    and Z as the magnetic dipole axis (also = rotation axis when the two are
    aligned). For off-center views (body offset from origin) or body-centered
    views where the Sun is offset, this function rotates the geometry to
    point toward the actual sunward direction.

    When magnetic_tilt_deg > 0, an additional rotation about the bow-shock-to-
    tail axis (X axis in the default frame) is applied BEFORE the sunward
    rotation. This tilts the magnetic dipole axis (originally aligned with
    Z) into the YZ plane by magnetic_tilt_deg degrees, modeling the offset
    between the magnetic dipole and the rotation axis. The bow-shock-to-tail
    direction is preserved. This is mathematically equivalent to applying
    the tilt about the actual sunward direction AFTER the sunward rotation.

    Parameters:
        px, py, pz (np.ndarray): Point coordinates in default frame
        center_position (tuple): (x, y, z) AU position of the body's center
        sun_position (tuple): (x, y, z) AU position of the Sun.
                              Default (0, 0, 0) = Sun at origin (heliocentric).
                              Phase D wires actual Sun position from ephemeris.
        magnetic_tilt_deg (float): Angular offset between rotation axis and
                                    magnetic dipole axis (degrees).
                                    Default 0 = aligned dipoles (Mercury, Venus,
                                    Mars, Saturn, Jupiter, Neptune passes 0
                                    -- internal handling). Used live by Uranus
                                    (60 deg) as of Phase C4. Earth (~11 deg)
                                    and Jupiter (~10 deg) eligible for Phase D
                                    activation.

    Returns:
        (rx, ry, rz): rotated point arrays

    Module updated: May 2026 with Anthropic's Claude Opus 4.7
    """
    import math
    import numpy as np

    # Step 1: Magnetic tilt about the X axis (bow-shock-to-tail) BEFORE sunward
    # rotation. Tilts the magnetic dipole axis (originally Z) into the YZ
    # plane by magnetic_tilt_deg. Preserves bow-shock-to-tail orientation.
    if magnetic_tilt_deg != 0:
        angle_rad = math.radians(magnetic_tilt_deg)
        cos_t = math.cos(angle_rad)
        sin_t = math.sin(angle_rad)
        new_py = py * cos_t - pz * sin_t
        new_pz = py * sin_t + pz * cos_t
        py = new_py
        pz = new_pz

    # Step 2: Sunward rotation. Maps default -X to actual sunward direction
    # via Rodrigues rotation.
    center_x, center_y, center_z = center_position
    sun_x, sun_y, sun_z = sun_position

    # Vector from body center toward Sun
    dx, dy, dz = sun_x - center_x, sun_y - center_y, sun_z - center_z
    dist = math.sqrt(dx**2 + dy**2 + dz**2)

    if dist < 1e-12:
        # Body and Sun coincident (or both at origin): default -X convention
        return px, py, pz

    # Actual sunward unit vector
    sx, sy, sz = dx / dist, dy / dist, dz / dist

    # Default sunward direction (geometry convention: -X)
    fx, fy, fz = -1.0, 0.0, 0.0

    # Dot product (cosine of angle between default and actual sunward)
    dot = fx * sx + fy * sy + fz * sz

    if dot > 0.9999:
        # Already aligned
        return px, py, pz

    if dot < -0.9999:
        # Anti-parallel: 180 deg rotation around Z axis
        return -px, -py, pz

    # Cross product gives rotation axis
    ax = fy * sz - fz * sy
    ay = fz * sx - fx * sz
    az = fx * sy - fy * sx
    alen = math.sqrt(ax**2 + ay**2 + az**2)
    ax, ay, az = ax / alen, ay / alen, az / alen

    # Rodrigues' rotation formula
    angle = math.acos(max(-1.0, min(1.0, dot)))
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)

    rx = np.empty_like(px, dtype=float)
    ry = np.empty_like(py, dtype=float)
    rz = np.empty_like(pz, dtype=float)

    for i in range(len(px)):
        p = (float(px[i]), float(py[i]), float(pz[i]))
        # v*cos(a) + (k x v)*sin(a) + k*(k.v)*(1-cos(a))
        kdotv = ax * p[0] + ay * p[1] + az * p[2]
        rx[i] = p[0] * cos_a + (ay * p[2] - az * p[1]) * sin_a + ax * kdotv * (1 - cos_a)
        ry[i] = p[1] * cos_a + (az * p[0] - ax * p[2]) * sin_a + ay * kdotv * (1 - cos_a)
        rz[i] = p[2] * cos_a + (ax * p[1] - ay * p[0]) * sin_a + az * kdotv * (1 - cos_a)

    return rx, ry, rz


def create_ring_points(inner_radius, outer_radius, n_points, thickness=0):
    """Create points for a planetary ring with inner and outer radii.

    Promoted from saturn_visualization_shells.py in Phase C3 for use by
    Saturn, Uranus, and Neptune ring builders. Jupiter's ring builder
    (with a different algorithm using explicit z-layer thickness) keeps
    its local helper.

    Parameters:
        inner_radius (float): Inner radius of the ring in AU
        outer_radius (float): Outer radius of the ring in AU
        n_points (int): Number of angular points; radial sampling is n_points/10
        thickness (float): Thickness of the ring in z-direction (AU).
                           0.0 means flat ring (z=0 for all points).

    Returns:
        (x, y, z): tuple of flat numpy arrays of point coordinates
    """
    # Generate angular positions
    theta = np.linspace(0, 2 * np.pi, n_points)

    # Calculate radial positions (sparse radial sampling for ring visualization)
    r = np.linspace(inner_radius, outer_radius, int(n_points / 10))

    # Create a meshgrid for combinations
    theta_grid, r_grid = np.meshgrid(theta, r)

    # Convert to cartesian coordinates
    x = r_grid.flatten() * np.cos(theta_grid.flatten())
    y = r_grid.flatten() * np.sin(theta_grid.flatten())

    # Add some thickness in z-direction if specified
    if thickness > 0:
        z = np.random.uniform(-thickness / 2, thickness / 2, size=x.shape)
    else:
        z = np.zeros_like(x)

    return x, y, z
