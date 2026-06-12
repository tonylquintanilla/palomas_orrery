"""Phase 4 live-dispatch smoke test. Imports palomas_orrery (GUI builds
under xvfb; mainloop stubbed), drives the REAL checkbox vars, and asserts:
  1. Opt-in OFF: checked magnetosphere absent from collect specs and the
     center skip set; '(static plots only)' legend placeholder PRESENT.
  2. Opt-in ON: magnetosphere in specs and skip set; placeholder ABSENT;
     build_perframe_traces returns d7-rounded coords, stable trace count
     across sun positions, payload under the guardrail.
  3. Indicator clamp engages when axis_range < shell-scaled length.
  4. _parse_osc_epoch handles all three Horizons forms.
  5. Rounding leaves invisible dummy slots untouched.
Exercises the live dispatch (module-level functions + real tk vars), not
per-body builders in isolation.
"""
import sys, importlib.util
import numpy as np

import tkinter
tkinter.Misc.mainloop = lambda *a, **k: None

spec = importlib.util.spec_from_file_location('po', 'palomas_orrery.py')
po = importlib.util.module_from_spec(spec)
sys.modules['po'] = po
spec.loader.exec_module(po)
print('=== module imported; GUI built ===')

pm = po.get_planet_shell_vars_map()
earth_vars = pm['Earth']
mag_key = next(k for k in earth_vars if 'magnetosphere' in k)
earth_vars[mag_key].set(1)
print('checked:', mag_key)

import plotly.graph_objects as go

def specs_for(center):
    return po.collect_perframe_elements(center, ['Earth', 'Mars'])

def placeholder_present(center='Sun'):
    fig = go.Figure()
    po.add_static_only_legend_placeholders(fig, center)
    names = [t.name or '' for t in fig.data]
    return any('Magnetosphere' in n and 'static plots only' in n for n in names)

# --- 1. opt-in OFF ---
po.animate_magnetospheres_var.set(0)
s_off = specs_for('Sun')
assert not any(s['element'] == 'magnetosphere' for s in s_off), \
    'OFF: magnetosphere leaked into collect specs'
assert 'magnetosphere' not in po.get_center_engine_elements('Earth'), \
    'OFF: magnetosphere leaked into center skip set'
assert placeholder_present(), \
    'OFF: static-only placeholder missing (silent-absence bug)'
print('PASS 1: opt-in OFF gates all three consumers; placeholder present')

# --- 2. opt-in ON ---
po.animate_magnetospheres_var.set(1)
s_on = specs_for('Sun')
mag_specs = [s for s in s_on if s['element'] == 'magnetosphere']
assert any(s['body'] == 'Earth' for s in mag_specs), \
    'ON: Earth magnetosphere missing from collect specs'
assert 'magnetosphere' in po.get_center_engine_elements('Earth'), \
    'ON: magnetosphere missing from center skip set'
assert not placeholder_present(), \
    'ON: placeholder still present while engine animates the element'
ind_specs = [s for s in s_on if s['element'] == 'sun_direction_indicator']
assert ind_specs and all('axis_range' in s['indicator_kwargs']
                         for s in ind_specs), \
    'indicator kwargs missing axis_range hint'
print('PASS 2: opt-in ON activates engine path; placeholder retired; '
      'range hint threaded')

# --- 2b. build through the engine chokepoint: rounding + stability ---
spec_e = next(s for s in mag_specs if s['body'] == 'Earth')
pos = (0.55, -0.83, 0.0)
t1 = po.build_perframe_traces(spec_e, pos, (0.8, 0.5, 0.02), quiet=True)
t2 = po.build_perframe_traces(spec_e, pos, (-0.9, -0.3, -0.05), quiet=True)
assert len(t1) == len(t2), 'trace-count stability violated: %d vs %d' % (
    len(t1), len(t2))
import plotly.io as pio
kb = sum(len(pio.json.to_json_plotly(t)) for t in t1) / 1e3
for t in t1:
    for attr in ('x', 'y', 'z'):
        v = getattr(t, attr, None)
        if v is None or len(v) == 0:
            continue
        arr = np.asarray(v, dtype=float)
        fin = arr[np.isfinite(arr)]
        assert np.allclose(fin, np.round(fin, po.PERFRAME_COORD_DECIMALS),
                           rtol=0, atol=0), 'unrounded %s in %s' % (attr, t.name)
assert kb < 150, 'guardrail: %.1f KB/frame' % kb
print('PASS 2b: %d traces, stable count, all coords d%d-rounded, '
      '%.1f KB/frame (rounded bytes are what the guardrail sees)'
      % (len(t1), po.PERFRAME_COORD_DECIMALS, kb))

# --- 3. indicator clamp ---
from shared_utilities import create_sun_direction_indicator
import contextlib, io
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    tr = create_sun_direction_indicator(
        center_position=(0, 0, 0), sun_position=(1.0, 0, 0),
        shell_radius=0.02, axis_range=[-0.005, 0.005],
        object_type='Earth', center_object='Earth', body_name='Earth')
out = buf.getvalue()
assert 'Clamped to axis range' in out, 'clamp did not engage: %r' % out
line = next(t for t in tr if getattr(t, 'x', None) is not None
            and len(t.x) >= 2)
tip = max(abs(float(v)) for v in line.x if v is not None)
assert tip <= 0.005 + 1e-9, 'clamped tip %.5f exits the cube' % tip
with contextlib.redirect_stdout(io.StringIO()):
    tr2 = create_sun_direction_indicator(
        center_position=(0, 0, 0), sun_position=(1.0, 0, 0),
        shell_radius=0.02, axis_range=None,
        object_type='Earth', center_object='Earth', body_name='Earth')
line2 = next(t for t in tr2 if getattr(t, 'x', None) is not None
             and len(t.x) >= 2)
tip2 = max(abs(float(v)) for v in line2.x if v is not None)
assert abs(tip2 - 0.023) < 1e-9, 'no-range behavior changed: %.5f' % tip2
print('PASS 3: clamp engages (tip %.4f <= 0.005); no-range path '
      'byte-identical (1.15 x shell = %.4f)' % (tip, tip2))

# --- 4. epoch parser ---
from datetime import datetime
assert po._parse_osc_epoch('2026-06-10 12:32 osc.') == datetime(2026, 6, 10, 12, 32)
assert po._parse_osc_epoch('2026-01-10') == datetime(2026, 1, 10)
assert po._parse_osc_epoch('2026-06-10 12:32:05') == datetime(2026, 6, 10, 12, 32, 5)
assert po._parse_osc_epoch('garbage') is None
print('PASS 4: epoch parser handles all three Horizons forms; '
      'garbage -> None (loud fallback at call sites)')

# --- 5. dummies untouched ---
d = po._perframe_dummy_trace()
po._round_perframe_coords([d])
assert list(d.x) == [None], 'dummy payload mutated: %r' % (d.x,)
print('PASS 5: rounding skips invisible dummy slots (None payload exact)')

print('=== ALL SMOKE TESTS PASS ===')
