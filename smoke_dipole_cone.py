"""
smoke_dipole_cone.py -- container smoke test for the dipole-cone primitive
(Movement 2, June 2026). Mirrors smoke_rotation_axis.py: it exercises the LIVE
dispatch, not the builder in isolation, because last session's lesson was that a
builder can work while the dispatch never calls it. No network, no GUI.

What this PROVES (run in the repo env):
  * each dipole body's CUSTOM_SHELLS['<body>']['dipole_cone'] resolves to the
    shared builder and sets needs_planet_name;
  * a tilted body returns 8 traces (2 cone nappes, 1 generator line, 2 rim arcs,
    2 arrowheads, 1 info marker); a near-zero-tilt body (Mercury, Saturn) returns
    2 (generator line = offset spin axis + info marker), the collapsed cone and
    sweep arcs omitted -- the honest envelope of a zero-tilt dipole is the line;
  * the drawn generator sits at the sourced tilt off the producer spin pole
    (Earth 9.6, Jupiter 10.3, Uranus 60, Neptune 47; Mercury/Saturn ~0) -- the
    cone consumes the pole faithfully;
  * the rim sweep arcs (tilted bodies) wind with the body's rotation sense (so
    the sweep reads as the spin);
  * LIVE PATH: create_celestial_body_visualization with ZERO shells checked
    renders the cone on BODY selection (1 legend each) for all six dipole bodies,
    and renders NOTHING for bodies without a sourced dipole (Mars).

What this does NOT prove (Mode-5 render, Tony's eyes):
  Whether the magenta sweep arrow and the gold spin arrow read as one rotation
  at scale, per-body half_len_frac sizing, and overall legibility. The cone is
  pole-frame and Sun-independent by construction; there is no azimuth convention
  left to validate (it is arbitrary and the cone shows the whole sweep).
"""
import importlib
import math
import numpy as np

from shell_configs import CUSTOM_SHELLS, SHELL_CONFIGS
from idealized_orbits import create_planet_transformation_matrix
from planet_visualization_utilities import PLANET_DIPOLE, PLANET_ROTATION
import plotly.graph_objs as go

BODIES = ['Mercury', 'Earth', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
OMITTED = ['Mars']   # has a magnetosphere but no sourced dipole tilt -> no dipole_cone

_TILT_EPS_DEG = 0.5   # below this the cone collapses to the spin axis (Mercury, Saturn)


def is_degenerate(body):
    return PLANET_DIPOLE[body]['tilt_deg'] < _TILT_EPS_DEG


def resolve_builder(body):
    entry = CUSTOM_SHELLS[body]['dipole_cone']
    assert entry.get('needs_planet_name') is True, '%s: needs_planet_name not set' % body
    module_path, func_name = entry['builder'].rsplit('.', 1)
    return getattr(importlib.import_module(module_path), func_name)


def generator_line(traces):
    for t in traces:
        if isinstance(t, go.Scatter3d) and t.mode == 'lines' and len(t.x) == 2:
            return np.array([[t.x[0], t.y[0], t.z[0]], [t.x[1], t.y[1], t.z[1]]])
    raise AssertionError('no generator line found')


def rim_arcs(traces):
    return [np.column_stack([t.x, t.y, t.z]) for t in traces
            if isinstance(t, go.Scatter3d) and t.mode == 'lines' and len(t.x) > 5]


def main():
    print('%-9s %3s %9s %9s  %s' % ('body', 'tr', 'tilt_dev', 'sense_ok', 'src'))
    failures = []
    for b in BODIES:
        builder = resolve_builder(b)
        traces = builder((0.0, 0.0, 0.0), planet_name=b)

        deg = is_degenerate(b)
        want_traces = 2 if deg else 8   # degenerate: generator line + info marker only
        if len(traces) != want_traces:
            failures.append('%s: %d traces (expected %d)' % (b, len(traces), want_traces))

        M = np.asarray(create_planet_transformation_matrix(b), float)
        pole = M[:, 2] / np.linalg.norm(M[:, 2])

        # generator at the sourced tilt off the pole (for a degenerate body the
        # generator IS the spin axis, want_tilt ~ 0)
        ln = generator_line(traces)
        d = ln[1] - ln[0]; d = d / np.linalg.norm(d)
        ang = math.degrees(math.acos(min(1.0, abs(float(np.dot(d, pole))))))
        want_tilt = PLANET_DIPOLE[b]['tilt_deg']
        dev = abs(ang - want_tilt)
        if dev > 1e-6:
            failures.append('%s: generator %.3f deg off pole, want %.1f' % (b, ang, want_tilt))

        nappes = [t for t in traces if isinstance(t, go.Mesh3d)]
        arcs = rim_arcs(traces)
        heads = [t for t in traces if isinstance(t, go.Cone)]
        sense_ok = True

        if deg:
            # collapsed cone: no nappes, no sweep arcs/heads; the generator line
            # (= offset spin axis) carries the single legend entry
            if nappes:
                failures.append('%s: %d cone nappes (expected 0, tilt ~ 0)' % (b, len(nappes)))
            if arcs:
                failures.append('%s: %d rim arcs (expected 0, tilt ~ 0)' % (b, len(arcs)))
            if heads:
                failures.append('%s: %d arrowheads (expected 0, tilt ~ 0)' % (b, len(heads)))
            gen_legend = [t for t in traces if isinstance(t, go.Scatter3d)
                          and t.mode == 'lines' and getattr(t, 'showlegend', False)]
            if len(gen_legend) != 1:
                failures.append('%s: generator does not carry exactly one legend entry' % b)
        else:
            # two nappes, exactly one legend-visible
            if len(nappes) != 2:
                failures.append('%s: %d cone nappes (expected 2)' % (b, len(nappes)))
            if sum(1 for c in nappes if getattr(c, 'showlegend', False)) != 1:
                failures.append('%s: nappes do not show exactly one legend entry' % b)
            # rim arcs wind with the rotation sense
            want_s = -1.0 if PLANET_ROTATION[b]['sense'] == 'retrograde' else 1.0
            if len(arcs) != 2:
                failures.append('%s: %d rim arcs (expected 2)' % (b, len(arcs)))
            for p in arcs:
                wind = np.cross(p[1] - p[0], p[2] - p[1])
                if float(np.sign(np.dot(wind, pole))) != want_s:
                    sense_ok = False
            if not sense_ok:
                failures.append('%s: rim arc winding does not match rotation sense' % b)
            if len(heads) != 2:
                failures.append('%s: %d arrowheads (expected 2)' % (b, len(heads)))

        print('%-9s %3d %9.2e %9s  %s' % (b, len(traces), dev, sense_ok, PLANET_DIPOLE[b]['source'][:28]))

    # LIVE RENDER PATH -- the check the builder-in-isolation test cannot make.
    print()
    from planet_visualization import create_celestial_body_visualization as draw
    for b in BODIES:
        fig = go.Figure()
        draw(fig, b, shell_vars={}, center_position=(0.0, 0.0, 0.0))
        cone = [t for t in fig.data if getattr(t, 'name', '') and 'Dipole Cone' in t.name]
        legend = [t for t in cone if getattr(t, 'showlegend', False)]
        want_cone = 2 if is_degenerate(b) else 8
        if len(cone) != want_cone:
            failures.append('%s: render path produced %d cone traces (expected %d) with no shells checked' % (b, len(cone), want_cone))
        if len(legend) != 1:
            failures.append('%s: %d legend entries (expected 1)' % (b, len(legend)))
    if not [f for f in failures if 'render path' in f or 'legend' in f]:
        print('render path: dipole cone appears on body selection (0 shells), 1 legend each  OK')

    # bodies without a sourced dipole must emit NO cone, via builder and via dispatch
    for b in OMITTED:
        if 'dipole_cone' in CUSTOM_SHELLS.get(b, {}):
            failures.append('%s: unexpectedly has a dipole_cone entry' % b)
        fig = go.Figure()
        draw(fig, b, shell_vars={}, center_position=(0.0, 0.0, 0.0))
        if [t for t in fig.data if getattr(t, 'name', '') and 'Dipole Cone' in t.name]:
            failures.append('%s: render path emitted a dipole cone (should be omitted)' % b)
    print('omitted body (Mars): no dipole cone  OK')

    print()
    if failures:
        print('RESULT: FAIL')
        for f in failures:
            print('  - ' + f)
        raise SystemExit(1)
    print('RESULT: PASS  (6 dipole cones wired: 4 tilted [Earth, Jupiter, Uranus, '
          'Neptune] + 2 degenerate axis-only [Mercury, Saturn]; on-pole-tilt + '
          'correct sense + body-triggered; non-dipole bodies emit none)')
    print('Reminder: spin/sweep-arrow rhyme and half_len_frac sizing are the Mode-5 render checks.')


if __name__ == '__main__':
    main()
