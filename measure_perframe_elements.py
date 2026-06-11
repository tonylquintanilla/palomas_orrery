"""
measure_perframe_elements.py - Byte budget table for the per-frame animation engine.

Measures the serialized (JSON) cost of each per-frame engine candidate by
calling the LIVE builders, then projects per-animation cost at 29 and 60
frames. This is the Decision-5(a) gate data for animation Phase 3: an
element earns per-frame status only if its measured cost fits the budget
(reference: Phase-1 savings ~4.2-4.5 MB per animation).

Reduced-resolution variants are measured LIVE, not projected: the harness
copies the relevant shells module to a temp file, patches the density
literals (binary replace, throwaway copy only -- the repo file is never
touched), and imports the patched copy under a distinct module name. The
bow-shock conic needs no patching at all: the shared builder
create_bow_shock_shape is already parameterized (n_phi/n_theta).

Usage:
    python measure_perframe_elements.py

Key functions:
    measure(traces) - serialized KB of a builder's trace list
    patched_earth_module() - import earth shells with density literals patched
    main() - print the budget table

Consumed by: ANIMATION_ENGINE_DESIGN (Phase 3 Session A), Phase 3 follow-on
resolution sweep.

Module updated: June 2026 with Anthropic's Claude Fable 5
"""

import importlib.util
import os
import sys
import tempfile

import plotly.io as pio

KB = 1e3
FRAMES_29 = 29
FRAMES_60 = 60


def measure(traces):
    """Serialized size in KB of a list of plotly traces (the per-frame cost)."""
    return sum(len(pio.json.to_json_plotly(t)) for t in traces) / KB


def row(name, traces):
    kb = measure(traces)
    print('%-52s %3d traces %8.1f KB/frame %6.2f MB @29f %6.2f MB @60f'
          % (name, len(traces), kb, kb * FRAMES_29 / 1e3, kb * FRAMES_60 / 1e3))
    return kb


def patched_earth_module():
    """Import a throwaway copy of earth_visualization_shells with reduced
    density: belts 80x5 -> 40x3; the bow-shock call gains n_phi=15,
    n_theta=15. The envelope (create_magnetosphere_shape, a shared producer
    with internal density) is left as-is -- its parameter promotion is the
    one remaining producer change of the resolution sweep."""
    with open('earth_visualization_shells.py', 'rb') as f:
        src = f.read()
    assert src.count(b'n_points = 80') == 1, 'belt n_points literal moved'
    assert src.count(b'n_rings = 5') == 1, 'belt n_rings literal moved'
    patched = (src.replace(b'n_points = 80', b'n_points = 40')
                  .replace(b'n_rings = 5', b'n_rings = 3')
                  .replace(b'width=bow_shock_width, eccentricity=1.05',
                           b'width=bow_shock_width, eccentricity=1.05, '
                           b'n_phi=15, n_theta=15'))
    assert patched != src, 'patch did not bite'
    tmp = tempfile.NamedTemporaryFile(suffix='.py', prefix='earth_reduced_',
                                      delete=False)
    tmp.write(patched)
    tmp.close()
    spec = importlib.util.spec_from_file_location('earth_reduced', tmp.name)
    mod = importlib.util.module_from_spec(spec)
    sys.modules['earth_reduced'] = mod
    spec.loader.exec_module(mod)
    return mod


def main():
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) or '.')
    import plotly.graph_objects as go
    from planet_visualization_utilities import (
        build_rotation_axis_traces, build_dipole_cone_traces,
        create_bow_shock_shape)
    from planet_visualization import create_sun_direction_indicator
    from mercury_visualization_shells import create_mercury_sodium_tail
    from earth_visualization_shells import (
        create_earth_magnetosphere_shell, EARTH_RADIUS_AU)

    origin = (0, 0, 0)
    sunpos = (1.0, 0.0, 0.0)

    print('PER-FRAME ENGINE BUDGET TABLE (live builders, serialized JSON)')
    print('Reference: Phase-1 savings ~4.2-4.5 MB/animation; frames are now')
    print('~1-3 KB each. Costs scale linearly with frame count.')
    print('-' * 104)

    print('FIRST-CUT PRIMITIVES (committed per-frame):')
    row('Rotation axis (Uranus)',
        build_rotation_axis_traces(origin, planet_name='Uranus'))
    row('Rotation axis (Earth)',
        build_rotation_axis_traces(origin, planet_name='Earth'))
    row('Dipole cone (Uranus)',
        build_dipole_cone_traces(origin, planet_name='Uranus'))
    row('Dipole cone (Neptune)',
        build_dipole_cone_traces(origin, planet_name='Neptune'))
    try:
        row('Sun direction indicator (Earth-sized shell)',
            create_sun_direction_indicator(
                center_position=origin, sun_position=sunpos,
                shell_radius=0.0043, object_type='Earth',
                center_object='Sun', body_name='Earth'))
    except TypeError as e:
        print('Sun direction indicator: signature differs (%s) -- measure in'
              ' Session B with the live dispatch' % e)

    print('SUN-DIRECTION CUSTOMS (committed per-frame; particle counts shown):')
    row('Mercury sodium tail (500 particles, as-is)',
        create_mercury_sodium_tail(center_position=origin, sun_position=sunpos))

    print('MEASURED FOLLOW-ON (reduced-resolution shells; gate 5a):')
    row('Earth magnetosphere FULL (belts 80x5, shock 30x30)',
        create_earth_magnetosphere_shell(center_position=origin,
                                         sun_position=sunpos))
    for n in (30, 20, 15):
        x, y, z = create_bow_shock_shape(
            15 * EARTH_RADIUS_AU, width=25 * EARTH_RADIUS_AU,
            eccentricity=1.05, n_phi=n, n_theta=n)
        row('Bow shock conic alone (%dx%d, %d pts)' % (n, n, len(x)),
            [go.Scatter3d(x=x, y=y, z=z, mode='lines')])
    mod = patched_earth_module()
    row('Earth magnetosphere REDUCED (belts 40x3, shock 15x15)',
        mod.create_earth_magnetosphere_shell(center_position=origin,
                                             sun_position=sunpos))

    print('-' * 104)
    print('NOT YET MEASURABLE HERE: comet tails (add_comet_tails_to_figure is')
    print('fig-mutating, not trace-returning; measure after the Session-C')
    print('trace-returning refactor). Envelope reduction pending the')
    print('create_magnetosphere_shape producer promotion. Ring systems:')
    print('measured follow-on with shells.')


if __name__ == '__main__':
    main()
