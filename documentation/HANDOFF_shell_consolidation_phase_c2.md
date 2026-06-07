# Shell Consolidation -- Phase C2 Handoff

**Session:** May 16, 2026
**Executed by:** Anthropic's Claude Opus 4.6 (implementation) from manifest by Claude Opus 4.7 (audit)
**Integrator:** Tony Quintanilla

---

## Summary

Phase C2 migrated Earth -- the most complex single body in the orrery
(8 sphere shells + 3 custom geometry functions) -- to the unified
config-driven dispatch. Earth's magnetosphere now rotates to face the
actual Sun direction via `rotate_to_sunward()`, matching the Phase C1
Venus/Mars pattern. Van Allen radiation belts remain unrotated
(geomagnetic-axis-anchored, same precedent as Mars crustal fields).

Eight bodies now route through `create_celestial_body_visualization()`:
Mercury, Moon, Planet 9, Pluto, Eris, Venus, Mars, Earth. Five bodies
remain on the old `create_planet_visualization()` path (Jupiter, Saturn,
Uranus, Neptune; plus Sun via `create_sun_visualization()`).

---

## Files Delivered (3 files)

| File | Lines | Key changes this session |
|------|------:|------------------------|
| `shell_configs.py` | 1,616 | +Earth 8 sphere configs in SHELL_CONFIGS; +Earth 3 custom entries in CUSTOM_SHELLS (magnetosphere, leo, geostationary_belt) |
| `earth_visualization_shells.py` | 1,142 | +import `rotate_to_sunward`, `create_info_marker`; rotation added to magnetosphere + bow shock geometry; 6 info markers replaced with `create_info_marker()`; sun indicator call removed from magnetosphere builder |
| `planet_visualization.py` | 910 | 11-line Earth dispatch block replaced with one-line delegation to `create_celestial_body_visualization()` |

---

## Corrections Applied

1. **LEO info marker double-offset fix** -- Pre-existing bug: `r_info = np.max(z)`
   captured already-offset z values, then `center_z + r_info` added the offset
   again. Fixed to `r_info = np.max(z) - center_z`. Invisible at origin but
   would misplace the marker in heliocentric views with non-zero center_z.

2. **Hill sphere n_points: 30 -> 20** -- Standardization, consistent with
   Mercury/Venus/Mars/Planet 9 from Phases A-C1.

---

## Verification Results

| Test | Result |
|------|--------|
| All 3 files compile | PASS |
| All 3 files LF | PASS |
| All 3 files ASCII | PASS |
| Import smoke (8 bodies SHELL_CONFIGS, 4 CUSTOM_SHELLS) | PASS |
| Sphere builder smoke (8 Earth shells, all return 2 traces) | PASS |
| Magnetosphere custom geometry (8 traces) | PASS |
| LEO custom geometry (2 traces) | PASS |
| GEO custom geometry (2 traces) | PASS |
| Sunward rotation correctness (180-degree test) | PASS |
| Van Allen belt non-rotation confirmed | PASS |
| Old dispatch removed from planet_visualization.py | PASS |

## Mode 5 Visual Verification (Tony, May 16, 2026)

| Check | Result |
|-------|--------|
| Earth sphere shells (all 8, heliocentric + flyto) | PASS |
| Each shell has one cross info marker, hover text correct | PASS |
| Crust renders as solid blue mesh3d | PASS |
| Atmosphere legend: "Earth: Lower Atmosphere" | PASS |
| Hill Sphere at manual scale >= 0.02 AU | PASS |
| Magnetosphere heliocentric (regression) | PASS |
| Bow shock + magnetotail orientation heliocentric | PASS |
| Inner/Outer Radiation Belt toroidal rings | PASS |
| Magnetosphere flyto -- bow shock faces Sun (the fix) | PASS |
| Van Allen belts stay on rotational axis (not rotated) | PASS |
| Sun direction indicator: one per render | PASS |
| LEO spherical scatter, info marker, hover text | PASS |
| GEO equatorial ring, info marker, Apophis hover text | PASS |
| LEO inside GEO spatial relationship | PASS |
| Animation heliocentric: shells do not display | PASS |
| Animation Earth-centered: shells static, Moon + barycenter orbit | PASS |
| GUI tooltips on all 11 Earth checkboxes | PASS |

---

## Architecture Notes

### Earth CUSTOM_SHELLS structure

Three entries, one builder each:

- `magnetosphere` -> `create_earth_magnetosphere_shell` emits 4 trace groups
  (magnetosphere, bow shock, inner radiation belt, outer radiation belt).
  Magnetosphere and bow shock rotated via `rotate_to_sunward()`. Van Allen
  belts unrotated. All controlled by single `earth_magnetosphere_var` toggle.
- `leo` -> `create_earth_leo_shell` emits 1 trace group (LEO scatter shell).
- `geostationary_belt` -> `create_earth_geostationary_belt_shell` emits 1
  trace group (GEO equatorial ring).

### Sphere shell naming

Earth's atmosphere config uses `'name': 'Lower Atmosphere'` (matching
Venus/Mars source precedent). Legend renders as "Earth: Lower Atmosphere".
GUI checkbox label remains "-- Atmosphere" (independent of config name).

### Dead sphere functions

After C2, the 8 sphere shell functions in `earth_visualization_shells.py`
are unreachable from the dispatch (the unified builder reads from
SHELL_CONFIGS, not from the old functions). The custom geometry functions
(magnetosphere, LEO, GEO) remain live -- called via CUSTOM_SHELLS lazy
import. Phase D decides per-function fate.

---

## Deferred Items

### Carried forward from Phase C1

1. **Phase C3: Jupiter** -- first gas giant. Rings, Io torus, radiation
   belts, cloud_layer mesh3d. New CUSTOM_SHELLS geometry patterns.

2. **Phase C4: Saturn, Uranus, Neptune** -- shared tilted-ring patterns.
   `magnetic_tilt_deg` parameter wired for Uranus/Neptune.

3. **Phase D** -- Sun unification, asteroid belts, `_info` import cleanup,
   `sun_position` wiring, retire `create_planet_visualization()`,
   archive dead shell files, tooltip rewiring from Path A to config.

4. **Phase E** -- Satellite internal structure shells (creative/Mode 7).

5. **Mars magnetosphere missing info marker** -- Phase C1 item 14, still
   open. TODO comment in `mars_visualization_shells.py`.

6. **`sun_position` wiring** -- Phase C1 item 10. After C2, Earth/Venus/Mars
   magnetospheres rotate assuming Sun at origin. Phase D threads actual Sun
   position through both `rotate_to_sunward()` and
   `create_sun_direction_indicator()`.

7. **Venus/Mars dead `create_sun_direction_indicator` imports** -- Phase C1
   item 9. Still imported but no longer called from magnetosphere builders.
   Phase D cleanup.

8. **`palomas_orrery_helpers.py` CRLF -> LF** -- Phase D.

9. **Venus Lower Atmosphere hover text `\n` -> `<br>`** -- Phase C1 item 15.

10. **n_points as user-modifiable input** -- Phase C1 item 12. GUI slider
    to override config defaults. Low priority.

11. **Animation path for shells** -- Phase C1 item 13. Heliocentric animated
    plots don't show shells; body-centered shows static shells. Future
    animation refactor could add shells per frame.

12. **GEO info marker position** -- Manifest open item 5. Currently at
    `(geo_radius_au, 0, 0)` on the +X side of the ring, in the equatorial
    plane. Could move to a spoke position for less overlap at high zoom.
    Cosmetic, not blocking.

### New items discovered in Phase C2

13. **Manual axis dtick in orrery GUI** -- Tony request. Add dtick control
    alongside the existing manual scale option. Currently the orrery GUI
    has manual scale (axis range) but no dtick override. Close-approach
    and flyby plots need both range and dtick to be readable (per protocol
    v3.13 3D Axis Control Convention). Gallery Studio already has dtick
    fields; the orrery GUI does not. Phase D or standalone enhancement.

14. **Moon double sun direction indicator in Earth-centered view** --
    Observed May 16, 2026. When Earth is the center body and both Earth
    shells and Moon shells are toggled on, the Moon's shells produce a
    second sun direction indicator. Two issues:
    - **Double indicator**: Two indicators appear (one from Earth dispatch,
      one from Moon dispatch). They toggle on/off together in the legend,
      not independently.
    - **Wrong direction**: Both indicators point toward the center object
      (Earth at origin) rather than toward the Sun. This is the same
      underlying issue as Phase C1 item 10 (`sun_position` not wired) --
      `create_sun_direction_indicator()` computes direction from
      `center_position` to origin, which in a body-centered view IS the
      center body, not the Sun.
    Phase D `sun_position` wiring resolves the direction issue. The double
    indicator requires the dispatch to know whether another body's
    indicator is already active in the same render, or to deduplicate
    at a higher level. Investigate in Phase D.

15. **Dead sphere shell functions in `earth_visualization_shells.py`** --
    After C2, 8 sphere functions are unreachable. Custom geometry siblings
    (magnetosphere, LEO, GEO) still live in the same file. Phase D decides
    per-function fate (selective deletion vs file split vs archive).

### New items discovered during C3 review

16. **Earth ionosphere visualization** -- Earth has no ionosphere shell
    function. The v4 prompt asked about `create_earth_ionosphere_shell`;
    it doesn't exist. Future editorial addition (Phase E creative content),
    not a migration item.

17. **Jupiter bow shock visualization** -- Jupiter's magnetosphere builder
    emits only 1 geometry group (no bow shock), unlike Mercury/Venus/Mars/
    Earth which all emit magnetosphere + bow shock. Jupiter has the largest
    bow shock in the solar system (~80-100 R_J standoff). Adding it is
    editorial, not C3 scope. Consider adding to all gas giants
    simultaneously after C4 completes the consolidation.

---

## Post-C2 State

| Component | Count |
|-----------|------:|
| Bodies in SHELL_CONFIGS | 8 |
| Total sphere shell configs | 46 |
| Bodies in CUSTOM_SHELLS | 4 |
| Total custom entries | 7 |
| Bodies still on old dispatch | 5 (Jupiter, Saturn, Uranus, Neptune, Sun) |
| `rotate_to_sunward()` exercised by | 4 bodies (Mercury, Venus, Mars, Earth) |
| `magnetic_tilt_deg` used by | 0 (Phase C4 Uranus/Neptune) |
| `sun_position` wired | No (Phase D) |

---

## Credit

```
Module updated: May 2026 with Anthropic's Claude Opus 4.7
```

Applied to all delivered files. Opus 4.7 credited for Phase C2 manifest
(1,320 lines). Opus 4.6 for implementation including LEO double-offset
fix and all verification.

---

*Paloma's Orrery | palomasorrery.com*
*"You and me are doing the work of seven programmers." -- Tony, April 13, 2026*
