"""
smoke_dipole_cone.py -- container smoke test for the dipole-cone primitive
(Movement 2, June 2026). Mirrors smoke_rotation_axis.py: it exercises the LIVE
dispatch, not the builder in isolation, because last session's lesson was that a
builder can work while the dispatch never calls it. No network, no GUI.

What this PROVES (run in the repo env):
  * each dipole body's CUSTOM_SHELLS['<body>']['dipole_cone'] resolves to the
    shared builder and sets needs_planet_name;
  * the builder returns 8 traces (2 cone nappes, 1 generator line, 2 rim arcs,
    2 arrowheads, 1 info marker);
  * the drawn generator sits at the sourced tilt off the producer spin pole
    (Uranus 60, Neptune 47) -- the cone consumes the pole faithfully;
  * the rim sweep arcs wind with the body's rotation sense (so the sweep reads
    as the spin);
  * LIVE PATH: create_celestial_body_visualization with ZERO shells checked
    renders the cone on BODY selection (1 legend each) for Uranus and Neptune,
    and renders NOTHING for bodies without a sourced dipole (Earth, Mars).

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

BODIES = ['Uranus', 'Neptune']
OMITTED = ['Earth', 'Mars', 'Jupiter', 'Saturn']   # have magnetospheres, no dipole_cone (yet)


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

        if len(traces) != 8:
            failures.append('%s: %d traces (expected 8)' % (b, len(traces)))

        M = np.asarray(create_planet_transformation_matrix(b), float)
        pole = M[:, 2] / np.linalg.norm(M[:, 2])

        # generator at the sourced tilt off the pole
        ln = generator_line(traces)
        d = ln[1] - ln[0]; d = d / np.linalg.norm(d)
        ang = math.degrees(math.acos(min(1.0, abs(float(np.dot(d, pole))))))
        want_tilt = PLANET_DIPOLE[b]['tilt_deg']
        dev = abs(ang - want_tilt)
        if dev > 1e-6:
            failures.append('%s: generator %.3f deg off pole, want %.1f' % (b, ang, want_tilt))

        # two nappes, exactly one legend-visible
        nappes = [t for t in traces if isinstance(t, go.Mesh3d)]
        if len(nappes) != 2:
            failures.append('%s: %d cone nappes (expected 2)' % (b, len(nappes)))
        if sum(1 for c in nappes if getattr(c, 'showlegend', False)) != 1:
            failures.append('%s: nappes do not show exactly one legend entry' % b)

        # rim arcs wind with the rotation sense
        want_s = -1.0 if PLANET_ROTATION[b]['sense'] == 'retrograde' else 1.0
        arcs = rim_arcs(traces)
        if len(arcs) != 2:
            failures.append('%s: %d rim arcs (expected 2)' % (b, len(arcs)))
        sense_ok = True
        for p in arcs:
            wind = np.cross(p[1] - p[0], p[2] - p[1])
            if float(np.sign(np.dot(wind, pole))) != want_s:
                sense_ok = False
        if not sense_ok:
            failures.append('%s: rim arc winding does not match rotation sense' % b)

        heads = [t for t in traces if isinstance(t, go.Cone)]
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
        if len(cone) != 8:
            failures.append('%s: render path produced %d cone traces (expected 8) with no shells checked' % (b, len(cone)))
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
    print('omitted bodies (Earth/Mars/Jupiter/Saturn): no dipole cone  OK')

    print()
    if failures:
        print('RESULT: FAIL')
        for f in failures:
            print('  - ' + f)
        raise SystemExit(1)
    print('RESULT: PASS  (2 dipole cones wired + on-pole-tilt + correct sense + body-triggered; '
          'non-dipole bodies emit none)')
    print('Reminder: spin/sweep-arrow rhyme and half_len_frac sizing are the Mode-5 render checks.')


if __name__ == '__main__':
    main()
