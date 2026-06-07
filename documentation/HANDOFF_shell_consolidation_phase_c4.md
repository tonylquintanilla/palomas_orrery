# Shell Consolidation -- Phase C4 Handoff

**Session:** May 18, 2026
**Executed by:** Anthropic's Claude Opus 4.6 (implementation) from manifest by Claude Opus 4.7 (audit)
**Integrator:** Tony Quintanilla

---

## Summary

Phase C4 migrated Saturn, Uranus, and Neptune -- the final three
planets -- to the unified config-driven dispatch. This completes the
planetary migration: 12 bodies now route through
`create_celestial_body_visualization()`. Only the Sun remains on the
old `create_sun_visualization()` path.

The headline change: `rotate_to_sunward()` gained its first real
`magnetic_tilt_deg` implementation -- an X-axis rotation before the
sunward Rodrigues rotation that tilts the magnetic dipole axis relative
to the rotation axis. Uranus (60 deg) is the first live consumer.
Neptune passes `magnetic_tilt_deg=0` because its internal 47-deg
region-specific tilt is already applied by the builder.

Additional non-mechanical fixes: Uranus magnetosphere gained its
missing info marker; Saturn ring tooltip copy-paste error (Jupiter
text) corrected during extraction; Saturn and Uranus radiation belt
double-offset bugs fixed; Neptune dead `create_neptune_field_lines`
stripped; Neptune radiation belt and FAC info marker position bugs
fixed.

---

## Files Delivered (6 files)

| File | Lines | Key changes this session |
|------|------:|------------------------|
| `orrery_rendering.py` | 328 | `magnetic_tilt_deg` X-axis rotation implemented in `rotate_to_sunward()` |
| `shell_configs.py` | 2,260 | +3 bodies sphere configs (16 total new); +3 bodies custom entries (10 total new); +imports for hover text strings from body modules |
| `planet_visualization.py` | 878 | Saturn/Uranus/Neptune dispatch blocks replaced with one-line delegations |
| `saturn_visualization_shells.py` | 1,188 | +imports (`rotate_to_sunward`, `create_info_marker`); magnetosphere sunward rotation; 6 sun indicators stripped; all info markers via helper; radiation belt double-offset fix |
| `uranus_visualization_shells.py` | 1,146 | +imports (`rotate_to_sunward`, `create_info_marker`); magnetosphere refactored (sunward rotation + `magnetic_tilt_deg=60` + info marker added); 5 sun indicators stripped; radiation belt dead code cleanup; all info markers via helper |
| `neptune_visualization_shells.py` | 1,702 | +imports (`rotate_to_sunward`, `create_info_marker`); magnetosphere sunward rotation (internal 47-deg preserved, `magnetic_tilt_deg=0`); dead `create_neptune_field_lines` stripped; 5 sun indicators stripped; radiation belt + FAC info marker position bugs fixed; all info markers via helper |

---

## Corrections Applied

1. **Saturn ring tooltip copy-paste error** -- source had Jupiter moon
   names (Metis, Adrastea) and Jupiter ring names (Amalthea Gossamer,
   Thebe Gossamer) in Saturn ring tooltips. Corrected to Saturn-specific
   content from per-ring `description` fields in the function body.

2. **Saturn radiation belt double-offset bug** -- center offset applied
   twice (pre-tilt and post-tilt). Stripped the pre-tilt offset block.
   Belts now in physically correct axial position.

3. **Uranus radiation belt dead code** -- three dead blocks stripped:
   pre-tilt offset, no-op variable recast, commented-out rotations.
   Same double-offset pattern as Saturn. Belts now in correct position.

4. **Neptune radiation belt info marker position bug** -- markers were
   placed at pre-rotation coordinates (`belt_x[0]` instead of
   `x_final[0]`). Relocated to post-rotation coordinates.

5. **Neptune FAC info marker position bug** -- same pattern as #4.
   `current_x[0]` -> `x_final[0]`.

6. **Uranus magnetosphere missing info marker** -- pre-existing
   omission (same pattern as Mars C1 item 14). Added via
   `create_info_marker()` with Ness et al. citation.

7. **Uranus magnetosphere missing `legendgroup`** -- source geometry
   trace had no `legendgroup`. Added so info marker groups properly.

---

## Verification Results

| Test | Result |
|------|--------|
| All 6 files compile | PASS |
| All 6 files LF | PASS |
| All 6 files ASCII | PASS |
| SHELL_CONFIGS: 12 bodies, 68 sphere configs | PASS |
| CUSTOM_SHELLS: 8 bodies, 21 custom entries | PASS |
| Saturn sphere builder smoke (6 shells, all return 2 traces) | PASS |
| Uranus sphere builder smoke (5 shells, all return 2 traces) | PASS |
| Neptune sphere builder smoke (5 shells, all return 2 traces) | PASS |
| Saturn custom trace counts (mag 2, torus 2, belts 12, rings 14) | PASS |
| Uranus custom trace counts (mag 2, belts 4, rings 22) | PASS |
| Neptune custom trace counts (mag 6, belts 12, rings 22) | PASS |
| Saturn magnetosphere rotation (180 deg test) | PASS |
| Uranus magnetosphere rotation (180 deg + magnetic_tilt=60) | PASS |
| Neptune magnetosphere rotation (180 deg, internal 47-deg preserved) | PASS |
| Saturn radiation belts NOT rotated | PASS |
| Uranus radiation belts NOT rotated | PASS |
| Neptune radiation belts NOT rotated | PASS |
| Saturn rings NOT rotated | PASS |
| Uranus rings NOT rotated | PASS |
| Neptune rings NOT rotated | PASS |
| Saturn Enceladus torus NOT rotated | PASS |
| Neptune dead function stripped | PASS |
| Uranus magnetic_tilt_deg=60 wired | PASS |
| magnetic_tilt_deg=0 is a no-op | PASS |
| magnetic_tilt_deg=90 unit test (Y->Z) | PASS |
| magnetic_tilt_deg=60 unit test | PASS |
| Combined magnetic_tilt + sunward rotation order | PASS |
| Old dispatch blocks removed (Saturn/Uranus/Neptune) | PASS |

## Mode 5 Visual Verification (Tony, May 18, 2026)

### Saturn

| Check | Result |
|-------|--------|
| Sphere shells (all 6, centered view) | PASS |
| Cloud layer solid mesh3d | PASS |
| Hill sphere at manual scale >= 0.6 AU | PASS |
| All 7 ring components render | PASS |
| Rings in equatorial plane (~27 deg tilt) | PASS |
| Ring info markers with ring-specific text | PASS |
| **Ring tooltip references Saturn (not Jupiter)** | **PASS -- copy-paste fix confirmed** |
| Rings toggle on/off via GUI checkbox | PASS |
| Magnetosphere renders as blue-purple cloud | PASS |
| Heliocentric: tail away from Sun | PASS |
| Flyto Saturn: tail still away from Sun | PASS |
| Magnetosphere info marker present | PASS |
| No bow shock (expected, deferred item 24) | PASS |
| Enceladus torus donut shape, equatorial | PASS |
| Enceladus torus NOT rotated | PASS |
| Enceladus torus info marker | PASS |
| 6 radiation belt components render | PASS |
| Belt info markers present | PASS |
| Belts NOT rotated | PASS |
| Belt position after double-offset fix | PASS -- accepted |
| ONE sun direction indicator per render | PASS |
| Heliocentric animation: shells not displayed | PASS |
| Saturn-centered animation: static shells, moons orbit | PASS |
| All 10 Saturn checkboxes have tooltips | PASS |
| Sphere shell hover text | TRUNCATED (pre-existing, item 27) |

### Uranus

| Check | Result |
|-------|--------|
| Sphere shells (all 5, centered view) | PASS |
| Cloud layer light blue mesh3d | PASS |
| Hill sphere at manual scale >= 0.6 AU | PASS |
| Magnetosphere renders as light blue cloud | PASS |
| Heliocentric: tail away from Sun | PASS (slight angle -- magnetic tilt) |
| Flyto Uranus: tail still away from Sun | PASS |
| **Visible asymmetry from magnetic_tilt_deg=60** | **PASS -- clearly tilted** |
| **Info marker present (NEW in C4)** | **PASS -- "60 degrees" + Ness et al.** |
| Tilt direction (sign convention) | Deferred to item 26 Gemini verification |
| 2 radiation belt components (Inner, Outer) | PASS |
| Belt info markers present | PASS |
| Belts NOT rotated | PASS |
| Belt position after dead-code cleanup | PASS -- accepted |
| 11 rings render | PASS |
| Rings in equatorial plane (~98 deg tilt) | PASS |
| Ring info markers present | PASS |
| Gossamer ring barely visible (pre-existing) | Noted (item 18) |
| ONE sun direction indicator per render | PASS |
| Animation same behavior as Saturn | PASS |
| All 8 Uranus checkboxes have tooltips | PASS |
| Sphere shell hover text | TRUNCATED (pre-existing, item 27) |

### Neptune

| Check | Result |
|-------|--------|
| Sphere shells (all 5, centered view) | PASS |
| Cloud layer blue mesh3d | PASS |
| Hill sphere at manual scale >= 1.0 AU | PASS |
| Magnetosphere renders as blue cloud | PASS |
| Heliocentric: tail away from Sun | PASS |
| Flyto Neptune: tail still away from Sun | PASS |
| Magnetosphere info marker present | PASS (truncated) |
| Magnetic poles visible (4 traces) | PASS |
| Magnetic pole drift in heliocentric | Accepted -- Phase D item 12 |
| Multiple belt regions render (inner, outer, cusp) | PASS |
| FAC render (dawn, dusk) | PASS |
| Belt/FAC info markers present | PASS (superimposed, item 28) |
| Belts NOT rotated | PASS |
| Main rings render (Galle, Le Verrier, Lassell, Arago, Adams) | PASS |
| Adams ring arcs visible | PASS |
| Rings in equatorial plane (~28 deg tilt) | PASS |
| Ring info markers present | PASS (Lassell/Arago superimposed, item 28) |
| ONE sun direction indicator per render | PASS |
| Animation same behavior as Saturn/Uranus | PASS |
| All 8 Neptune checkboxes have tooltips | PASS |
| Sphere shell hover text | TRUNCATED (pre-existing, item 27) |

### Regression

| Check | Result |
|-------|--------|
| Saturn rings same shape as pre-C4 | PASS |
| Uranus rings same shape as pre-C4 | PASS |
| Neptune rings same shape as pre-C4 | PASS |
| All rings on planetary equatorial plane | PASS |

### Decision points resolved

| Decision | Outcome |
|----------|---------|
| 5a. Uranus magnetic tilt direction | Magnitude correct. Sign convention deferred to item 26 (Gemini verification). One-character fix if needed. |
| 5b. Saturn/Uranus belt positions | Double-offset fix accepted. Positions physically correct. |
| 5c. Neptune pole drift | Acceptable for C4. Deferred to Phase D item 12. |

---

## Architecture Notes

### magnetic_tilt_deg implementation

Applied as an X-axis rotation in the default geometry frame BEFORE the
sunward Rodrigues rotation. This tilts the magnetic dipole axis
(originally aligned with Z) into the YZ plane by `magnetic_tilt_deg`
degrees while preserving the bow-shock-to-tail orientation on the X axis.
Mathematically equivalent to tilting about the actual sunward direction
AFTER the sunward rotation.

| Body | magnetic_tilt_deg | Notes |
|------|------------------:|-------|
| Mercury | 0 (default) | Aligned dipole |
| Venus | 0 (default) | No intrinsic field |
| Earth | 0 (Phase D: 11) | Visually subtle |
| Mars | 0 (default) | Crustal field |
| Jupiter | 0 (Phase D: 10) | Visually subtle |
| Saturn | 0 | Aligned dipole |
| **Uranus** | **60** | **First live use** |
| Neptune | 0 | Internal 47-deg handling preserved |

### Neptune magnetosphere: bounded scope decision

Neptune's magnetosphere builder applies its 47-degree tilt internally
via region-specific rotations (bow shock unrotated, internal field
tilted, tail partially tilted). The `rotate_to_sunward()` call uses
`magnetic_tilt_deg=0` to avoid double-tilting. The internal helper
`create_neptune_magnetic_poles` was NOT modified in C4 -- its 4 traces
(center, axis, north pole, south pole) stay in the body frame and
will visibly drift off the rotated envelope in heliocentric views.
Phase D fixes this when `sun_position` wiring revisits all call sites.

### shell_configs.py hover text pattern

C4 imports hover text strings from body shell modules rather than
inlining them (divergence from C1-C3 pattern). Three import blocks at
top of `shell_configs.py`:
- `from saturn_visualization_shells import saturn_core_info, ...`
- `from uranus_visualization_shells import uranus_core_info, ...`
- `from neptune_visualization_shells import neptune_core_info, ...`

Rationale: avoids duplicating 16 multi-line strings; keeps the body
module as authoritative source. Can be converted to inline if preferred.

### Rotation decisions (same precedent as C1-C3)

| Structure | Rotated? | Reason |
|-----------|----------|--------|
| Magnetosphere | Yes | Solar-wind-driven |
| Radiation belts | No | Axis-anchored |
| Enceladus torus | No | Equatorial, gravity-anchored |
| Ring system | No | Equatorial, gravity-anchored |

### Axial tilt vs magnetic tilt -- critical distinction

Two different rotations apply to gas/ice giant structures:

- **Axial tilt (obliquity):** planet's equatorial plane vs ecliptic.
  Applied INSIDE belt/ring/torus builders to place structures in the
  planet's actual equatorial plane. Examples: Saturn -26.73 deg,
  Uranus 97.77 deg. These rotations are PRESERVED -- they are
  physically correct and predate the consolidation.

- **Magnetic tilt (dipole offset):** magnetic dipole axis vs rotation
  axis. Applied via `rotate_to_sunward()` parameter. NEW in C4.
  Examples: Uranus 60 deg (live), Neptune 47 deg (internal handling).

These are independent rotations about different axes. Double-tilting
(applying magnetic tilt on top of internal axial tilt in a belt
builder) would be a physics error.

### Neptune Adams ring arcs

Neptune's ring_system CUSTOM_SHELLS entry contains the Adams ring arcs
(Courage, Liberte, Egalite 1, Egalite 2, Fraternite) as inline
geometry within the single `create_neptune_ring_system` builder. They
use custom angular longitude placement rather than `create_ring_points()`.
Confirmed: single CUSTOM_SHELLS entry, not separate entries per arc.

---

## Deferred Items

### Carried forward from Phase C3 (resolved by C4)

- ~~Phase C4: Saturn, Uranus, Neptune~~ **DONE**
- ~~Uranus magnetosphere missing info marker~~ **DONE** (correction #6)
- ~~Saturn 6 per-shell sun direction indicators (C3 #17)~~ **DONE** (stripped)
- ~~Uranus 5 per-shell sun direction indicators (C3 #18)~~ **DONE** (stripped)
- ~~Saturn cloud layer info marker visible when toggled off (C3 #19)~~ **DONE** (legendgroup linkage via unified dispatch)
- ~~Uranus cloud layer info marker visible when toggled off (C3 #20)~~ **DONE** (same)
- ~~Neptune cloud layer info marker visible when toggled off (C3 #21)~~ **DONE** (same)

### Carried forward (still open)

Items are grouped by target phase. Each carries enough context to act
on without chasing earlier handoffs.

#### Phase D items (Sun unification + cleanup sweep)

Phase D is the final consolidation phase: migrate the Sun to unified
dispatch, wire `sun_position` through all magnetosphere call sites,
clean up dead imports/functions/files, migrate asteroid belts, and
retire the old `create_planet_visualization()` function. After Phase D,
every body routes through a single dispatch and the old rendering path
is deleted.

1. **Sun unification.** The Sun is the last body on the old
   `create_sun_visualization()` dispatch path (2 call sites: ~line 4509
   in plot_objects, ~line 6144 in animate_objects). Migration pattern:
   add Sun sphere configs to SHELL_CONFIGS, add Sun custom entries
   (corona, Hills Cloud, Oort Cloud) to CUSTOM_SHELLS, replace both
   call sites with delegation to `create_celestial_body_visualization()`.
   After this, `create_sun_visualization()` can be deleted.

2. **Asteroid belt migration.** `asteroid_belt_visualization_shells.py`
   (4 components: Main Belt, Hilda, L4 Greeks, L5 Trojans) already
   converted to single info marker pattern (Step 2, May 2026). Not yet
   migrated to CUSTOM_SHELLS dispatch. These are called directly from
   `palomas_orrery.py`, not through `planet_visualization.py`. Phase D
   decides: migrate to CUSTOM_SHELLS (new dispatch path for non-body
   geometry), or leave as direct calls with a documented exception.

3. **Retire `create_planet_visualization()`.** After Sun migration, all
   bodies route through `create_celestial_body_visualization()`. The old
   function (~80 lines of if/elif dispatch) can be deleted along with
   its import chain. Currently has 0 remaining body blocks after C4
   (Saturn/Uranus/Neptune were the last), but the function frame and
   Sun path remain.

4. **`sun_position` wiring.** After C4, all 8 sunward-rotated
   magnetospheres (Mercury, Venus, Mars, Earth, Jupiter, Saturn, Uranus,
   Neptune) assume Sun at origin (`sun_position=(0,0,0)` default). This
   is correct in heliocentric views but wrong in body-centered views
   where the body is at origin and the Sun is offset. Fix: thread the
   Sun's actual position (already available in the ephemeris pipeline)
   through the unified dispatch into `rotate_to_sunward()` and
   `create_sun_direction_indicator()`. Both views then produce identical
   shell geometry. This also fixes:
   - Sun direction indicator pointing at center body instead of Sun
     in body-centered views (pre-existing since Phase A)
   - Mercury sodium tail orientation in Mercury-centered view (Phase A
     item 8)
   - Neptune magnetic poles drifting off the rotated envelope in
     heliocentric views (C4 item 21 below)

5. **`_info` import cleanup.** ~89 hover text string imports in
   `palomas_orrery.py`, ~87 dead imports in `palomas_orrery_helpers.py`,
   re-exports in `planet_visualization.py`. Three wiring paths: ~33
   inline CreateToolTip calls (Path A -- globals() lookup), direct
   imports (Path B), Sun/asteroid direct imports (Path C). One batch
   operation after all bodies are migrated. The C4 hover text import
   pattern (shell_configs.py imports from body modules) may simplify
   this -- tooltip text can be read from SHELL_CONFIGS/CUSTOM_SHELLS
   at GUI construction time.

6. **Archive dead shell files and functions.** After C4, all sphere
   shell functions in body shell files are unreachable from the dispatch
   (the unified builder reads from SHELL_CONFIGS). Custom geometry
   functions remain live (called via CUSTOM_SHELLS lazy import). Phase D
   decides per-function fate: selective deletion, file split (keep
   custom, archive sphere), or whole-file archive for bodies with no
   custom geometry. Affected files: all 12 migrated body shell modules.
   Also: `moon_visualization_shells.py` and `planet9_visualization_shells.py`
   are entirely dead since Phase B. Dead `fibonacci_sphere` code in
   12 crust/cloud_layer functions (tracked since Phase A item 9 / single
   info marker handoff) gets cleaned up here.

7. **Tooltip rewiring.** GUI tooltips currently reference function names
   and paths from the old dispatch. After migration, tooltip text should
   come from SHELL_CONFIGS (sphere shells) and CUSTOM_SHELLS (custom
   geometry) `tooltip` fields. This replaces the current globals()
   lookup chain.

8. **Venus/Mars/Saturn/Uranus/Neptune dead `create_sun_direction_indicator`
   imports.** Venus and Mars (since C1), Saturn, Uranus, and Neptune
   (since C4) still import `create_sun_direction_indicator` at module
   top even though their magnetosphere builders no longer call it. The
   import remains because their old sphere shell functions (now dead)
   still reference it. Removing the dead sphere functions (item 6)
   makes these imports unused; clean up in the same pass.

9. **`palomas_orrery_helpers.py` CRLF -> LF.** This file has Windows
   line endings. Convert when first modified during Phase D `_info`
   cleanup. Use Python binary mode (rb/wb) for the conversion.

10. **Double sun direction indicator in multi-body centered views.**
    Two related manifestations, same root cause (`sun_position` not
    wired, indicator deduplication missing):
    - **Moon in Earth-centered view** (C2 item 14): both Earth and Moon
      dispatch paths emit an indicator. Both point toward origin (the
      center body) rather than the Sun.
    - **Barycenter views** (C1 item 11): e.g. Pluto barycenter shows
      2 indicators. The barycenter rendering path in `palomas_orrery.py`
      may issue its own indicator call alongside the unified dispatch.
    Phase D `sun_position` wiring (item 4) fixes the direction. The
    double-indicator requires the dispatch to deduplicate: either track
    whether an indicator has already been emitted in the current render,
    or consolidate indicator emission to a single call after all body
    traces are built.

11. **Earth/Jupiter `magnetic_tilt_deg` wiring.** Earth's dipole is
    tilted ~11 deg from its rotation axis; Jupiter's ~10 deg. Both are
    visually subtle at those angles. Phase D's `sun_position` wiring
    (item 4) revisits every magnetosphere call site -- add
    `magnetic_tilt_deg=11` (Earth) and `magnetic_tilt_deg=10` (Jupiter)
    at that point. One parameter change per call site. The
    `rotate_to_sunward()` implementation is ready (tested in C4 for
    Uranus at 60 deg).

12. **Neptune magnetic poles `sun_position` extension.** C4 left
    `create_neptune_magnetic_poles` untouched (bounded scope). Its 4
    traces (magnetic center marker, axis line, north pole, south pole)
    stay in Neptune's body frame and visibly drift off the rotated
    magnetosphere envelope in heliocentric views where Neptune is not
    on the +X axis. Fix during Phase D `sun_position` wiring: extend
    the function signature with `sun_position=(0,0,0)`, wrap each
    pole trace's point assembly with a `_emit` helper that calls
    `rotate_to_sunward()`, update the call site in
    `create_neptune_magnetosphere()` to pass `sun_position`. ~30 lines
    of surgery.

13. **Neptune ring info marker rotation mismatch.** The ring geometry
    applies a compound rotation: X-axis (32 deg) then Y-axis (34 deg).
    The info marker placement uses `neptune_tilt = 28.32 deg` (X-axis
    only). The marker lands close to but not exactly on the ring
    geometry. Fix during Phase D: align the info marker rotation with
    the geometry rotation (apply both X and Y rotations to the marker
    position).

14. **Neptune `print()` debug statement.** Line ~766 in
    `create_neptune_magnetic_poles`: `print(f"Returning {len(traces)}
    magnetic field traces")`. Cosmetic. Remove during Phase D.

15. **Neptune function-local imports.** Each function in
    `neptune_visualization_shells.py` repeats `import numpy as np`,
    `import plotly.graph_objs as go`, etc. Harmless redundancy (Python
    caches imports), but unusual style. Clean up during Phase D
    module-level reorganization -- move all imports to module top.

#### Phase D items (lower priority / cosmetic)

16. **Venus Lower Atmosphere hover text.** Pre-existing `\n` where
    `<br>` should be in the source description ("...extends from the
    surface up to \n an altitude..."). Faithfully copied into
    `shell_configs.py` by auto-generation. Targeted fix: replace `\n`
    with `<br>` in the Venus atmosphere `hover_text` block. Origin:
    Phase C1 item 15.

17. **GEO info marker position.** Currently at `(geo_radius_au, 0, 0)`
    on the +X side of the equatorial ring. Could move to a spoke
    position for less overlap at high zoom. Cosmetic, not blocking.
    Origin: Phase C2 item 12.

18. **Uranus gossamer ring barely visible.** The Nu and Mu rings are
    extremely faint in the visualization. Pre-existing cosmetic issue,
    not a regression from any consolidation phase. Mode 5 review when
    desired. Origin: Phase C3 item 22.

19. **Manual axis dtick in orrery GUI.** The orrery GUI has manual
    scale (axis range) but no dtick override. Close-approach and flyby
    plots need both range and dtick to be readable (per protocol v3.13
    3D Axis Control Convention). Gallery Studio already has dtick
    fields; the orrery GUI does not. Add dtick control alongside the
    existing manual scale option. Origin: Phase C2 item 13.

#### Phase D or standalone items (features / enhancements)

20. **n_points as user-modifiable input.** `build_sphere_shell()`
    already reads `n_points` from config; the plumbing is: GUI control
    (slider/spinner) -> override value -> passed into builder, falling
    back to config default. Low visual density is a performance feature;
    higher density useful for screenshots. Low priority. Origin: Phase
    C1 item 12.

21. **Animation path for shells.** Current behavior: heliocentric
    animated plots don't show shells at all; body-centered animated
    plots show static shells at origin with satellites orbiting around
    them. Magnetosphere renders as static geometry alongside sphere
    shells. The C1-C4 delegations pass `animate=animate, frames=frames`
    through, preserving this behavior. Future animation refactor:
    (a) heliocentric could render shells at the body's animated
    position per frame, (b) body-centered could update shell orientation
    if solar wind direction changes over the animation period. Both
    require shells added to each animation frame at the correct position.
    Origin: Phase C1 item 13.

#### Phase E items (creative / Mode 7)

22. **Satellite internal structure shells.** Creative/Mode 7 work: new
    GUI elements, new `CENTER_BODY_RADII` entries, literature-sourced
    interior models. Candidates: Phobos, Deimos, Charon, Nix, Hydra,
    Kerberos, Styx, Dysnomia, Europa, Ganymede, Io, Callisto, Titan,
    Enceladus, Triton, possibly Miranda. Even satellites with limited
    data get minimum crust shell from known/estimated radius. Phase E
    can run parallel with Phase D. Origin: Phase B item 1.

23. **Earth ionosphere visualization.** Earth has no ionosphere shell
    function. Future editorial addition -- not a migration item. The
    ionosphere sits between the upper atmosphere and the magnetosphere
    and would be a new sphere shell config entry. Origin: Phase C2
    item 16.

24. **Jupiter bow shock visualization.** Jupiter's magnetosphere builder
    emits 1 geometry group (no bow shock), unlike Mercury/Venus/Mars/
    Earth which all emit magnetosphere + bow shock. Jupiter has the
    largest bow shock in the solar system (~80-100 R_J standoff).
    Consider adding bow shock to all gas giants simultaneously
    (Jupiter, Saturn, Uranus, Neptune) as an editorial enhancement
    after Phase D completes. Origin: Phase C2 item 17.

25. **Mars magnetosphere missing info marker.** Pre-existing omission
    from Step 2 (single info marker refactor). The magnetosphere
    geometry trace has `hoverinfo='skip'` but no cross marker was ever
    added. The `magnetosphere_text` variable exists in the source but
    is unused. Pattern: place a `create_info_marker()` at `x[0]` with
    color `'rgb(180, 180, 255)'` and legendgroup `'Mars: Induced
    Magnetosphere'`. TODO comment in `mars_visualization_shells.py`
    marks the location. Requires editorial confirmation of marker
    placement. Origin: Phase C1 item 14.

#### Cross-model verification

26. **CUSTOM_SHELLS tooltip factual verification.** The CUSTOM_SHELLS
    tooltip strings for Saturn (4 entries: magnetosphere, Enceladus
    torus, radiation belts, ring system), Uranus (3: magnetosphere,
    radiation belts, ring system), and Neptune (3: magnetosphere,
    radiation belts, ring system) were composed during C4
    implementation, not extracted verbatim from source. They contain
    physics claims — belt component counts, ring dimensions, magnetic
    tilt values, source citations — that derive partly from source
    code descriptions (fetched, trustworthy) and partly from the
    implementer's synthesis of manifest context (recalled, needs
    verification). This is the exact class of content where the
    fetched-vs-recalled convention applies.
    
    Recommended approach: targeted Mode 7 pass. Send the ~10 tooltip
    strings to Gemini for factual verification against authoritative
    sources (NASA fact sheets, Voyager 2 mission archive, Ness et al.
    1986/1989). Same pattern as the April 2026 provenance audit. Flag
    any claim that doesn't check out. Can run anytime before or during
    Phase D — independent of code work.

27. **Sphere shell info string `\n` -> `<br>` conversion.** All sphere
    shell hover text strings in Saturn, Uranus, and Neptune body
    modules use Python `\n` for line breaks. Plotly's `hovertemplate`
    renders `<br>` as line breaks but truncates or collapses text at
    `\n`. Result: hover text appears truncated for all sphere shells
    on these three bodies. Same class of issue as Venus (item 16).
    Pre-existing — the info strings are unchanged from source; C4
    imports them without modification. Fix: batch `\n` -> `<br>`
    replacement across all sphere shell info strings in Saturn, Uranus,
    Neptune, and Venus modules. Discovered during C4 Mode 5 visual
    verification, May 18, 2026.

28. **Neptune superimposed info markers.** Two cosmetic overlaps
    observed during C4 visual verification:
    - Radiation belt info markers: bug fix correctly moved markers
      from pre-rotation to post-rotation coordinates, but the belt
      regions are tightly packed around Neptune's offset dipole, so
      multiple markers land on top of each other. Individual belt
      components can still be isolated via legend toggle.
    - Lassell and Arago ring markers: these rings are physically
      adjacent (53,200-57,200 km and 57,200 km), so outer-radius
      markers overlap.
    Not blocking. Fix: space markers along different azimuths per
    component, or offset along the tilt axis. Low priority cosmetic.
    Discovered during C4 Mode 5 visual verification, May 18, 2026.

---

## Phase D Staging

Phase D is staged as three independently valuable sub-phases, each
testable before moving on. Same collegial manifest pattern as Phase C.

### D1: Sun migration (mechanical, one session)

The last body. Follows the exact pattern proven across 12 bodies in
C1-C4. Sun has sphere shells (photosphere, chromosphere, corona layers)
plus custom geometry (Hills Cloud, Outer Oort Cloud, Galactic Tide
boundary, density layers). Two call sites to replace
(`create_sun_visualization()` in plot_objects and animate_objects).

After D1, every body routes through the unified dispatch and
`create_sun_visualization()` can be deleted.

**Deferred items resolved:** 1 (Sun unification), 2 (asteroid belt
migration).

### D2: `sun_position` threading (narrow scope, one session)

Thread the Sun's actual position through the unified dispatch into
`rotate_to_sunward()` and `create_sun_direction_indicator()`. Narrow
scope: compute `sun_position` from the center body's known heliocentric
position at the two existing call sites in `palomas_orrery.py`
(heliocentric: `(0,0,0)`; body-centered: negate center body's
heliocentric coords). No new Horizons fetches, no pipeline
restructuring, no layout extraction.

While touching every magnetosphere call site, also:
- Wire `magnetic_tilt_deg=11` for Earth, `magnetic_tilt_deg=10` for Jupiter
- Extend Neptune's `create_neptune_magnetic_poles` with `sun_position`
  parameter and `_emit` helper (~30 lines)
- Resolve double sun direction indicator (deduplication logic)

After D2, body-centered views show correct magnetosphere orientation
and indicator direction for the first time. The six-month deferral
from Phase A item 6 is resolved.

**Deferred items resolved:** 4 (sun_position wiring), 10 (double
indicator), 11 (Earth/Jupiter magnetic_tilt_deg), 12 (Neptune pole
extension).

**Explicitly out of scope:** Rings 1-3 of the master plotting
consolidation handoff (layout extraction, finalization sequence,
render context). The broader consolidation of `plot_objects` /
`animate_objects` is a separate major refactor to be approached
carefully in its own planning conversation.

### D3: Cleanup sweep (no architectural changes)

Pure cleanup. No new features, no structural changes. Safe to defer
indefinitely if higher-priority work intervenes.

- Retire `create_planet_visualization()` (~80 lines, 0 remaining body
  blocks after C4)
- Clean up `_info` import chain (~89 + ~87 imports across two files)
- Archive dead sphere shell functions across 12 body modules
- Remove dead `create_sun_direction_indicator` imports (5 modules)
- Tooltip rewiring from globals() lookup to config fields
- `palomas_orrery_helpers.py` CRLF -> LF
- Neptune cosmetics (debug print, local imports, ring marker rotation)
- Venus hover text `\n` -> `<br>` fix

After D3, the codebase is clean: no dead code, no dead imports, no
legacy dispatch paths.

**Deferred items resolved:** 3, 5, 6, 7, 8, 9, 13, 14, 15, 16, 17,
18, 19.

### Deferred item cross-reference

| Item | Stage | Description |
|-----:|:-----:|-------------|
| 1 | D1 | Sun unification |
| 2 | D1 | Asteroid belt migration |
| 3 | D3 | Retire create_planet_visualization() |
| 4 | D2 | sun_position wiring |
| 5 | D3 | _info import cleanup |
| 6 | D3 | Archive dead shell files/functions |
| 7 | D3 | Tooltip rewiring |
| 8 | D3 | Dead create_sun_direction_indicator imports |
| 9 | D3 | palomas_orrery_helpers.py CRLF |
| 10 | D2 | Double sun direction indicator |
| 11 | D2 | Earth/Jupiter magnetic_tilt_deg |
| 12 | D2 | Neptune magnetic poles sun_position |
| 13 | D3 | Neptune ring info marker rotation |
| 14 | D3 | Neptune print() debug |
| 15 | D3 | Neptune function-local imports |
| 16 | D3 | Venus hover text |
| 17 | D3 | GEO info marker position |
| 18 | D3 | Uranus gossamer ring |
| 19 | D3 | Manual axis dtick in orrery GUI |
| 20 | -- | n_points GUI (standalone, low priority) |
| 21 | -- | Animation shell rendering (standalone) |
| 22 | E | Satellite internal structure shells |
| 23 | E | Earth ionosphere |
| 24 | E | Gas giant bow shocks |
| 25 | E | Mars magnetosphere info marker |
| 26 | Pre-D1 | CUSTOM_SHELLS tooltip factual verification (Mode 7/Gemini) |
| 27 | D3 | Sphere shell info string `\n` -> `<br>` (Saturn/Uranus/Neptune/Venus) |
| 28 | D3 | Neptune superimposed info markers (cosmetic) |

---

## Post-C4 State

| Component | Count |
|-----------|------:|
| Bodies in SHELL_CONFIGS | 12 |
| Total sphere shell configs | 68 |
| Bodies in CUSTOM_SHELLS | 8 |
| Total custom entries | 21 |
| Bodies still on old dispatch | 1 (Sun) |
| `rotate_to_sunward()` exercised by | 8 bodies |
| `create_ring_points()` used by | 3 bodies (Saturn, Uranus, Neptune) |
| `magnetic_tilt_deg` used live by | 1 (Uranus, 60 deg) |
| `magnetic_tilt_deg` eligible for Phase D | 2 (Earth 11, Jupiter 10) |
| `sun_position` wired | No (Phase D) |

---

## Credit

```
Module updated: May 2026 with Anthropic's Claude Opus 4.7
```

Applied to all delivered files. Opus 4.7 credited for Phase C4 manifest
(~3,100 lines) including `magnetic_tilt_deg` physics analysis, Neptune
bounded-scope decision, and complete extraction audit. Opus 4.6 for
implementation across all six files, all verification, and testing
protocol.

---

*Paloma's Orrery | palomasorrery.com*
*"Three Claudes, one Tony, zero orchestration framework." -- May 2026*
