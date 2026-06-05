"""
smoke_rotation_axis.py -- container smoke test for the rotation-axis primitive
(Movement 2, June 2026). Exercises the LIVE dispatch wiring: it resolves each
body's CUSTOM_SHELLS['<body>']['rotation_axis']['builder'] string and calls it
exactly as planet_visualization.py does (planet_name passed via the
needs_planet_name flag). No network, no GUI.

What this PROVES (container-checkable):
  * every CUSTOM_SHELLS rotation_axis entry resolves to the shared builder and
    sets needs_planet_name;
  * each body returns exactly 6 traces (pole line, 2 spin arcs, 2 cones, info marker);
  * the drawn axis line is parallel to the producer pole vector from
    create_planet_transformation_matrix (angle ~ 0 deg) -- i.e. the primitive
    consumes the pole faithfully;
  * the spin-arrow winding sign matches the explicit prograde/retrograde flag;
  * Planet 9 and Eris have NO rotation axis but DO carry the omitted-note.

What this does NOT prove (Mode-5 render, Tony's eyes):
  Both-ends arrows make the pole-direction / IAU-vs-RHR convention moot -- one
  rigid rotation drawn at both poles reads correctly from any side, so there is
  no "which end is north" risk left to validate. What remains for the render is
  ordinary legibility: per-body half_len_frac sizing (axis reaching the right
  outer structure without overwhelming the view), arc radius, and that the two
  arrows read as one spin. Interesting cases: Uranus (axis ~horizontal), Venus
  (~vertical), Earth (23.4 deg anchor), Sun (corona-scale).
"""
import importlib
import math
import numpy as np

from shell_configs import CUSTOM_SHELLS, SHELL_CONFIGS
from idealized_orbits import create_planet_transformation_matrix
from planet_visualization_utilities import PLANET_ROTATION, ROTATION_AXIS_OMITTED
import plotly.graph_objs as go

BODIES = ['Sun', 'Mercury', 'Venus', 'Earth', 'Moon', 'Mars',
          'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']

# NSSDCA obliquity-to-orbit + orbital inclination, for the printed eyeball column.
OBLIQ = {'Sun': 7.25, 'Mercury': 0.034, 'Venus': 177.4, 'Earth': 23.44,
         'Moon': 6.68, 'Mars': 25.19, 'Jupiter': 3.13, 'Saturn': 26.73,
         'Uranus': 97.77, 'Neptune': 28.32, 'Pluto': 122.53}


def resolve_builder(body):
    """Resolve the builder the same way the dispatch loop does."""
    entry = CUSTOM_SHELLS[body]['rotation_axis']
    assert entry.get('needs_planet_name') is True, '%s: needs_planet_name not set' % body
    module_path, func_name = entry['builder'].rsplit('.', 1)
    mod = importlib.import_module(module_path)
    return getattr(mod, func_name)


def axis_line(traces):
    for t in traces:
        if isinstance(t, go.Scatter3d) and t.mode == 'lines' and len(t.x) == 2:
            return np.array([[t.x[0], t.y[0], t.z[0]], [t.x[1], t.y[1], t.z[1]]])
    raise AssertionError('no pole-line trace found')


def all_arcs(traces):
    arcs = [np.column_stack([t.x, t.y, t.z]) for t in traces
            if isinstance(t, go.Scatter3d) and t.mode == 'lines' and len(t.x) > 5]
    if not arcs:
        raise AssertionError('no arc trace found')
    return arcs


def main():
    print('%-9s %3s %9s %9s  %-9s %s' %
          ('body', 'tr', 'axis_dev', 'ecl_tilt', 'obliq', 'sense'))
    failures = []
    for b in BODIES:
        builder = resolve_builder(b)
        traces = builder((0.0, 0.0, 0.0), planet_name=b)

        # (1) trace count
        if len(traces) != 6:
            failures.append('%s: %d traces (expected 6: line + 2 arcs + 2 cones + marker)' % (b, len(traces)))

        # (2) axis line parallel to producer pole (angle ~ 0)
        M = np.asarray(create_planet_transformation_matrix(b), float)
        pole = M[:, 2] / np.linalg.norm(M[:, 2])
        ln = axis_line(traces)
        d = ln[1] - ln[0]
        d = d / np.linalg.norm(d)
        dev = math.degrees(math.acos(min(1.0, abs(float(np.dot(d, pole))))))
        if dev > 1e-6:
            failures.append('%s: axis deviates %.3e deg from producer pole' % (b, dev))

        # (3) BOTH spin arrows present and sharing one 3-space sense (= one
        # angular-velocity vector); sign matches the prograde/retrograde flag.
        # Same-in-space is the invariant; opposite-on-screen follows from the
        # opposite viewpoints and is not container-checkable.
        want = -1.0 if PLANET_ROTATION[b]['sense'] == 'retrograde' else 1.0
        arcs = all_arcs(traces)
        if len(arcs) != 2:
            failures.append('%s: %d arcs (expected 2, one per pole)' % (b, len(arcs)))
        for ai, p in enumerate(arcs):
            wind = np.cross(p[1] - p[0], p[2] - p[1])
            got = float(np.sign(np.dot(wind, pole)))
            if got != want:
                failures.append('%s: arc %d winding sign %+d, expected %+d'
                                % (b, ai, got, want))

        ecl_tilt = math.degrees(math.acos(max(-1.0, min(1.0, pole[2]))))
        print('%-9s %3d %9.2e %9.2f  %-9.3f %s' %
              (b, len(traces), dev, ecl_tilt, OBLIQ[b], PLANET_ROTATION[b]['sense']))

    # (4) omitted bodies: no axis, but note present on the body hover
    print()
    for b in ['Planet 9', 'Eris']:
        if 'rotation_axis' in CUSTOM_SHELLS.get(b, {}):
            failures.append('%s: unexpectedly has a rotation_axis entry' % b)
        if b not in ROTATION_AXIS_OMITTED:
            failures.append('%s: missing from ROTATION_AXIS_OMITTED' % b)
        hover_blob = ''
        for shell in SHELL_CONFIGS.get(b, {}).values():
            hover_blob += shell.get('hover_text', '')
        if 'Rotation axis omitted' not in hover_blob:
            failures.append('%s: omitted-note not found in body hover_text' % b)
        else:
            print('%-9s omitted-note present in hover  OK' % b)

    # (5) LIVE RENDER PATH -- the check the first version of this test lacked.
    # Resolving the builder (above) proves the config + builder; it does NOT
    # prove the dispatch reaches the axis when a body is plotted. The axis is
    # BODY-triggered, so it must render even with ZERO shells checked. This is
    # the gap that let an unrendered axis pass a green smoke test once.
    print()
    from planet_visualization import create_celestial_body_visualization as _draw
    import plotly.graph_objs as _go
    for b in BODIES:
        fig = _go.Figure()
        _draw(fig, b, shell_vars={}, center_position=(0.0, 0.0, 0.0))
        axis = [t for t in fig.data
                if getattr(t, 'name', '') and 'Rotation Axis' in t.name]
        legend = [t for t in axis if getattr(t, 'showlegend', False)]
        if len(axis) != 6:
            failures.append('%s: render path produced %d axis traces (expected 6) '
                            'with no shells checked' % (b, len(axis)))
        if len(legend) != 1:
            failures.append('%s: %d legend entries (expected 1)' % (b, len(legend)))
    if not [f for f in failures if 'render path' in f or 'legend' in f]:
        print('render path: all 11 axes appear on body selection (0 shells checked), 1 legend each  OK')

    # (6) omitted bodies must NOT emit an axis via the render path either
    for b in ['Planet 9', 'Eris']:
        fig = _go.Figure()
        _draw(fig, b, shell_vars={}, center_position=(0.0, 0.0, 0.0))
        axis = [t for t in fig.data
                if getattr(t, 'name', '') and 'Rotation Axis' in t.name]
        if axis:
            failures.append('%s: render path emitted an axis (should be omitted)' % b)

    print()
    if failures:
        print('RESULT: FAIL')
        for f in failures:
            print('  - ' + f)
        raise SystemExit(1)
    print('RESULT: PASS  (11 axes wired + on-pole + correct sense + body-triggered; 2 omitted + noted)')
    print('Reminder: half_len_frac sizing and overall legibility are the Mode-5 render checks; '
          'both-ends arrows make the pole-convention question moot.')


if __name__ == '__main__':
    main()
