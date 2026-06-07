# Shell Consolidation — Phase B Handoff

**Session:** May 14, 2026
**Executed by:** Anthropic's Claude Opus 4.6 (implementation) from manifest by Claude Opus 4.7 (audit)
**Integrator:** Tony Quintanilla

---

## Summary

Phase B migrated Moon (6 sphere shells) and Planet 9 (2 sphere shells)
to the unified config-driven dispatch. Three bodies now route through
`create_celestial_body_visualization()`: Mercury, Moon, Planet 9. Ten
bodies remain on the old `create_planet_visualization()` path.

Additional work this session: mesh3d geometry support for crusts/cloud
layers, centralized info marker, sun direction indicator restoration,
magnetosphere sunward rotation, axis auto-scaling for center bodies,
Moon mantle radius correction, and n_points standardization.

---

## Files Delivered (5 total across Phases A+B this session)

| File | Lines | Key changes this session |
|------|------:|------------------------|
| `orrery_rendering.py` | 177 | `create_info_marker()`, `build_sphere_shell()` with mesh3d support |
| `shell_configs.py` | 500 | Mercury (6) + Moon (6) + Planet 9 (2) sphere configs, 2 Mercury custom entries |
| `shared_utilities.py` | 130 | Indicator points sunward, suppressed at origin |
| `planet_visualization.py` | 935 | Unified dispatch, Mercury/Moon/Planet 9 delegation, shell radius auto-scale attribute |
| `mercury_visualization_shells.py` | 454 | Dead functions removed, magnetosphere rotation, `create_info_marker()` |

**Manual edits by Tony in `palomas_orrery.py`:** Two 3-line insertions
for axis auto-scaling (static plot path ~line 4517, animation path
~line 6153). Pattern:
```python
                    # Auto-scale axis to shell radius for migrated bodies
                    if hasattr(fig, '_shell_outermost_radius_au') and scale_var.get() == 'Auto':
                        shell_r = fig._shell_outermost_radius_au * 2
                        axis_range = [-shell_r, shell_r]
```

---

## Corrections Applied

1. **Moon mantle radius/opacity swap** — Source had `radius_fraction=0.85`,
   `opacity=0.9655`. The description text and lunar geometry confirm the
   outer boundary is at 1677.4/1737.4 = 0.9655 of lunar radius. The
   inline source comment ("55-85% of Earth's radius") was a copy-paste
   from Earth. Corrected to `radius_fraction=0.9655, opacity=0.7`.

2. **n_points standardized** — Mercury Hill sphere 30->20, Planet 9 Hill
   sphere 50->20. Standard: interior shells n_points=25, boundary/
   atmosphere/Hill sphere n_points=20. No reason to deviate without a
   specific decision.

3. **Planet 9 Hill sphere NameError** — Source line 267 referenced
   undefined `radius` instead of `layer_radius`. Migration silently
   fixes this because `build_sphere_shell()` computes the radius from
   config. Builder smoke test confirms the trace builds without error.

---

## Mode 5 Visual Verification Results

| Test | Result |
|------|--------|
| Moon center, all 6 shells on | PASS - all render correctly |
| Moon mantle gap (corrected) | PASS - thin gap between mantle and crust |
| Moon crust mesh3d | PASS - solid grey surface |
| Moon info markers | PASS - one cross per shell, red outline |
| Moon legend: "Moon: Hill Sphere" | PASS - consistency fix from "Hill Sphere" |
| Mercury regression | PASS - all shells render |
| Other bodies unchanged | PASS - Venus, Earth, Mars render normally |
| Axis auto-scale (Moon center) | PASS - scales to shell radius |
| Planet 9 flyto surface | Not fully verified - flyto overrides axis range |
| Planet 9 Hill sphere visual | Deferred - builder smoke test confirms no crash |

---

## Deferred Items

### Carried forward from Phase A

1. **Phase C sub-phases (progressive complexity):**
   - **C1: Pluto + Eris + Venus + Mars** -- Pluto/Eris are Phase-B-
     equivalent (sphere-only, configs + delegation, files archivable
     in Phase D). Venus/Mars introduce first CUSTOM_SHELLS entries
     (magnetosphere/bow shock). Promote `rotate_to_sunward()` to
     `orrery_rendering.py` with `magnetic_tilt_deg=0` default +
     `sun_position` parameter (resolves deferred item 6).
   - **C2: Earth** -- most complex single body (14 shells). Benefits
     from C1 magnetosphere patterns being established.
   - **C3: Jupiter** -- first gas giant. Rings, Io torus, radiation
     belts, cloud_layer mesh3d.
   - **C4: Saturn, Uranus, Neptune** -- shared tilted-ring patterns.

   **Phase E (separate): Satellite internal structure shells.**
   Creative/Mode 7 work: new GUI elements, new `CENTER_BODY_RADII`
   entries, literature-sourced interior models. Candidates: Phobos,
   Deimos, Charon, Nix, Hydra, Kerberos, Styx, Dysnomia, Europa,
   Ganymede, Io, Callisto, Titan, Enceladus, Triton, possibly Miranda.
   Even satellites with limited data get minimum crust shell from
   known/estimated radius. Phase E can run parallel with Phase D.

2. **Retire `create_planet_visualization()`** — Phase D. 10 bodies still
   use it. Also retire `create_sun_visualization()` (2 call sites).

3. **Archive dead shell files** — Phase D. `moon_visualization_shells.py`,
   `planet9_visualization_shells.py` are fully dead after Phase B.
   Pluto/Eris files may also be archivable after C3 depending on
   satellite custom geometry decisions.

4. **`_info` import cleanup** — Phase D. One batch operation.

5. **`palomas_orrery_helpers.py` CRLF -> LF** — Phase D.

6. **`sun_position` parameter** — Magnetosphere rotation, sodium tail
   direction, and sun direction indicator all assume Sun at origin.
   Wrong in body-centered views. Thread `sun_position` through
   `rotate_to_sunward()` during C1 promotion. Resolved once, inherited
   by C2-D.

7. **Promote `rotate_to_sunward()` to `orrery_rendering.py`** — Phase C1.
   Promoted with `magnetic_tilt_deg=0` default (for Uranus at 60 deg
   in C4) and `sun_position` parameter (resolves item 6).

8. **Info marker style propagation** — Phase C/D custom geometry.

### New items discovered in Phase B

9. **Flyto axis range override** — The flyto view overrides axis range
   regardless of manual scale or auto-scale settings. This means
   Planet 9 shells (and potentially other bodies' shells in flyto
   views) cannot be visually verified at appropriate scale through the
   flyto mechanism. The flyto button's JavaScript needs to respect
   the target body's shell scale. Pre-existing behavior, not a Phase B
   regression.

10. **Planet 9 as center body** — Planet 9's `object_type='hypothetical'`
    excludes it from `can_be_horizons_center()`. It cannot be selected
    as a center body, so its shells only render through the flyto path.
    A "shell-only center" mode would allow centering on Planet 9 without
    requiring Horizons data — skip the ephemeris fetch, render only
    shells at origin. Touches the data pipeline, not shell architecture.

11. **Axis auto-scale for non-center bodies** — The `_shell_outermost_
    radius_au` attribute only flows back to `axis_range` in the center
    body rendering path. Non-center bodies (flyto) use the plot's
    orbital-scale axis range. This is correct for the plot as a whole
    but means individual body shells are at subpixel scale in the full
    view. Related to item 9 (flyto axis range).

---

## Architecture Notes

### Mesh3d geometry type

`build_sphere_shell()` supports `config['geometry_type']`:
- `'scatter3d'` (default) — dot sphere. Interior anatomy shells.
- `'mesh3d'` — triangulated UV solid surface, flat shading, full ambient
  light. Crusts and cloud layers. No marker_size needed.

All three migrated bodies use mesh3d for their crust/surface configs.
Phase C/D bodies should follow the same convention.

### n_points standard

| Shell type | n_points | Total dots |
|------------|:--------:|:----------:|
| Interior (core, mantle) | 25 | 625 |
| Boundary (atmosphere, Hill sphere) | 20 | 400 |

`n_points` is grid resolution per dimension. Total = n_points squared.

### Axis auto-scale

The unified dispatch stores `fig._shell_outermost_radius_au` after
rendering. `palomas_orrery.py` checks for this attribute and sets
`axis_range = [-2*r, 2*r]` when Auto scaling is active. Only fires
for migrated bodies in the center body path.

---

## Credit

```
Module updated: May 2026 with Anthropic's Claude Opus 4.7
```

Applied to all delivered files. Opus 4.7 credited for Phase A manifest,
Phase B manifest, and architectural design. Opus 4.6 for implementation
across both phases including mesh3d support, magnetosphere rotation,
indicator restoration, dead code removal, and axis auto-scaling.
