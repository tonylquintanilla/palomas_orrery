# Phase C1 Testing Protocol

**Date:** May 15, 2026
**Test after:** All 6 modified files are in place (shell_configs.py,
planet_visualization.py, orrery_rendering.py, mercury_visualization_shells.py,
venus_visualization_shells.py, mars_visualization_shells.py) plus manual
edits to palomas_orrery.py (ASCII + credit line).

---

## 1. Syntax Check (command line)

```
python -m py_compile shell_configs.py
python -m py_compile planet_visualization.py
python -m py_compile orrery_rendering.py
python -m py_compile mercury_visualization_shells.py
python -m py_compile venus_visualization_shells.py
python -m py_compile mars_visualization_shells.py
python -m py_compile palomas_orrery.py
```

No output = all pass. Fix any errors before proceeding.

---

## 2. Import Smoke Test (command line)

```python
python -c "
from orrery_rendering import build_sphere_shell, create_info_marker, rotate_to_sunward
from shell_configs import SHELL_CONFIGS, CUSTOM_SHELLS
for body in ['Mercury', 'Moon', 'Planet 9', 'Pluto', 'Eris', 'Venus', 'Mars']:
    assert body in SHELL_CONFIGS, body + ' missing'
for body in ['Mercury', 'Venus', 'Mars']:
    assert body in CUSTOM_SHELLS, body + ' missing from CUSTOM_SHELLS'
print('Pluto:', len(SHELL_CONFIGS['Pluto']), '/ Eris:', len(SHELL_CONFIGS['Eris']),
      '/ Venus:', len(SHELL_CONFIGS['Venus']), '/ Mars:', len(SHELL_CONFIGS['Mars']))
print('PASS')
"
```

Expected: `Pluto: 6 / Eris: 5 / Venus: 6 / Mars: 7` then `PASS`.

---

## 3. Pluto Visual Verification

Launch orrery. Set center body to Pluto.

| # | Action | Expected |
|---|--------|----------|
| 1 | Enable all 6 Pluto shells | All render; legend shows Pluto: Core / Mantle / Crust / Haze Layer / Atmosphere / Hill Sphere |
| 2 | Check crust | Solid brownish mesh3d surface (rgb(83, 68, 55)), not dot sphere |
| 3 | Check mantle | Dot sphere at 0.99 body radius; thin visible gap between mantle and crust |
| 4 | Check mantle legend label | Says "Pluto: Mantle" (capitalized M, not lowercase) |
| 5 | Check haze layer | Thin blue dot sphere at 1.17 body radius |
| 6 | Check atmosphere | Dot sphere at 1.43 body radius |
| 7 | Check Hill sphere | Very large green sparse sphere (requires manual scale to see) |
| 8 | Hover info markers | Each shell has one cross marker at north pole; hover shows description text |
| 9 | Check Sun direction indicator | Body-centered: SUPPRESSED (correct -- Sun visible at origin; Phase D wires `sun_position` to fix). Barycenter-centered: appears (may show double -- pre-existing, see handoff item 11) |
| 10 | Auto scale | With Auto scaling on, axis range adapts to outermost active shell |

---

## 4. Eris Visual Verification

Set center body to Eris.

| # | Action | Expected |
|---|--------|----------|
| 1 | Enable all 5 Eris shells | All render; legend shows Core / Mantle / Crust / Atmosphere / Hill Sphere |
| 2 | Check crust | Off-white mesh3d solid surface (rgb(240, 240, 240)) |
| 3 | Check atmosphere | At 1.005 body radius -- very thin layer. Gap between crust and atmosphere may be visually imperceptible at default scale. This is correct (Eris atmosphere is transient, only at perihelion) |
| 4 | Check Hill sphere | Very large green sparse sphere (requires manual scale) |
| 5 | Hover info markers | One cross per shell |
| 6 | Sun direction indicator | Body-centered: SUPPRESSED (correct -- same as Pluto) |

---

## 5. Venus Visual Verification

Set center body to Venus.

| # | Action | Expected |
|---|--------|----------|
| 1 | Enable all 6 sphere shells | Core / Mantle / Crust / Lower Atmosphere / Upper Atmosphere / Hill Sphere all render |
| 2 | Check crust | Pale yellow mesh3d solid surface |
| 3 | Check atmosphere names | "Lower Atmosphere" and "Upper Atmosphere" (two distinct layers) |
| 4 | Check Hill sphere | Green sphere at 166 Venus radii (very large, needs manual scale) |
| 5 | Enable magnetosphere | Light blue particle cloud renders |
| 6 | Check bow shock | Orange paraboloid behind the magnetosphere |
| 7 | Magnetosphere info markers | Cross at first geometry point for BOTH magnetosphere and bow shock (size=8, red outline -- new style) |
| 8 | Flyto from outer system view | Bow shock faces Sun (rotation works) |
| 9 | Sun direction indicator | Body-centered: SUPPRESSED. Flyto/off-center: appears ONCE |

---

## 6. Mars Visual Verification

Set center body to Mars.

| # | Action | Expected |
|---|--------|----------|
| 1 | Enable all 7 sphere shells | Inner Core / Outer Core / Mantle / Crust / Atmosphere / Upper Atmosphere / Hill Sphere |
| 2 | Inner vs outer core | Differentiated colors: inner (rgb(255, 180, 140)) vs outer (rgb(255, 140, 0)) |
| 3 | Check crust | Red mesh3d solid surface (rgb(188, 39, 50)) |
| 4 | Enable magnetosphere | THREE legend entries appear: Magnetosphere, Bow Shock, Crustal Magnetic Fields |
| 5 | Magnetosphere trace | Light blue particle cloud |
| 6 | Bow shock | Orange paraboloid |
| 7 | Crustal fields | Purple dots concentrated in southern hemisphere |
| 8 | Mars magnetosphere info marker | ABSENT -- this is correct (preserved pre-existing omission). Bow shock and crustal fields DO have cross markers (new style) |
| 9 | Flyto from outer system | Bow shock rotates to face Sun; crustal fields stay surface-anchored (do NOT rotate) |
| 10 | Sun direction indicator | Body-centered: SUPPRESSED. Flyto/off-center: appears ONCE |

---

## 7. Animation Test

Pick any C1 body (Venus recommended -- has both sphere shells and
custom magnetosphere geometry).

| # | Action | Expected |
|---|--------|----------|
| 1 | Set up an animated plot with Venus visible | Venus orbital trace animates normally |
| 2 | Enable Venus sphere shells during animation | Shells render as static geometry on the plot (frame 1 overlay). They do NOT animate per-frame -- this is current expected behavior |
| 3 | Enable Venus magnetosphere during animation | Magnetosphere and bow shock render as static geometry |
| 4 | Verify animation controls still work | Play/pause/scrub unaffected by shell traces |
| 5 | Repeat with Mars if time permits | Same expectations: static shell overlay on animated orbital traces |

Note: shells rendering on frame 1 only is the pre-existing behavior,
preserved by the C1 delegation. Deeper animation integration (shells
updating position per frame) is a future refactor.

---

## 8. Regression Checks

| # | Action | Expected |
|---|--------|----------|
| 1 | Set center to Mercury, enable all shells + magnetosphere | Identical to Phase A/B -- all shells render, bow shock faces Sun |
| 2 | Set center to Moon, enable all shells | Identical to Phase B |
| 3 | Check Earth, Jupiter, Saturn, Uranus, Neptune | All render normally via old dispatch path (unchanged) |
| 4 | Hover GUI checkboxes for all C1 bodies | Tooltips display correctly |

---

## 9. If Something Fails

- Shell doesn't render: check shell_configs.py -- is the shell key
  spelled exactly as the GUI var suffix? (e.g. 'hill_sphere' not
  'hill_sphere_shell')
- Magnetosphere doesn't render: check CUSTOM_SHELLS entry -- builder
  path must be 'venus_visualization_shells.create_venus_magnetosphere_shell'
- Rotation wrong direction: check that rotate_to_sunward import is from
  orrery_rendering, not a stale local copy
- Sun indicator appears multiple times: check that magnetosphere builder
  no longer calls create_sun_direction_indicator()
- Tooltip missing: the _info strings are still in the shell files and
  still consumed via globals() -- Phase D migrates these

---

*Phase C1 testing protocol -- Paloma's Orrery*
