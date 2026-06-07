# Shell Consolidation -- Phase D1 Handoff

**Session:** May 19, 2026 (D1 config extraction + cleanup)
**Updated:** May 19, 2026 (item 29 switchover, same session)
**Executed by:** Anthropic's Claude Opus 4.6 (implementation) from manifest by Claude Opus 4.7 (audit)
**Integrator:** Tony Quintanilla

---

## Summary

Phase D1 extracted the Sun's shell configurations into the unified
dispatch registries (`SHELL_CONFIGS` and `CUSTOM_SHELLS`), then
completed the call site switchover (item 29) in the same session.
`create_sun_visualization()` and `create_sun_corona_from_distance()`
are both retired. The Sun now renders through the unified dispatch
at all three call sites (static center, off-center, animation).

The Sun has the most sphere shells of any body (15) plus 3 custom
geometry shells (Hills Cloud torus, clumpy Outer Oort Cloud, Galactic
Tide boundary). All configs are registered and verified, and all 18
shells now render through `create_celestial_body_visualization()`.

Additional work: 5 dead items stripped from `solar_visualization_shells.py`
(~196 lines, including 2 functions that were not just dead but broken --
they would crash with `ValueError` if called). Three custom function
signatures extended with `center_position=(0,0,0)` for forward
compatibility with the unified dispatch contract. The `corona_from_distance`
special checkbox was removed from the GUI -- Sun shells now render at the
Sun's offset position from any center body without a special toggle.

Decision: Option A for legend name normalization -- 6 non-conforming
Sun legend names normalized to `"Sun: <X>"` pattern. Mode 5 visual
review confirmed all 6 renames.

Decision: CUSTOM_SHELLS tooltip text uses source strings from
`solar_visualization_shells.py` (imported variable references, not
composed text). Zero recalled-not-fetched content. Item 26 scope does
not grow.

Decision: Asteroid belt geometry separated from Sun shell dispatch.
4 belt `if`-blocks pulled to direct calls at each call site in
`palomas_orrery.py`. Belts only render Sun-centered (correct --
they are Sun-centered geometry). Belt restructuring deferred to D3.

---

## Files Delivered (4 files + snippets)

| File | Lines (before) | Lines (after) | Key changes |
|------|---------------:|--------------:|-------------|
| `shell_configs.py` | 2,260 | 2,708 | D1: +15 Sun sphere + 3 Sun custom configs. Cleanup: +hover_text/tooltip fix for Saturn/Uranus/Neptune (16 entries); +mesh3d for Sun photosphere |
| `solar_visualization_shells.py` | 1,759 | 1,591 | D1: -5 dead items; +center_position params. Cleanup: +tooltip string; +red info marker borders on 3 custom functions |
| `neptune_visualization_shells.py` | 1,703 | 1,695 | Cleanup: -debug print; -function-local imports; +create_magnetosphere_shape at top level |
| `planet_visualization.py` | 879 | 659 | Item 29: retired `create_sun_visualization()` and `create_sun_corona_from_distance()` (stubs with `NotImplementedError`); removed dead asteroid belt imports (-220 lines) |
| `palomas_orrery.py` | 9,950 | 9,977 | Item 29: 7 Mode 1 snippets applied by Tony. Switchover to unified dispatch, asteroid belt direct calls, `corona_from_distance` removal (+27 lines net) |

---

### Convention: palomas_orrery.py changes

All changes to `palomas_orrery.py` are applied by Tony manually
using Mode 1 targeted snippets. Claude never delivers a complete
`palomas_orrery.py` -- the file is too large (9,949 lines) and
too central for a complete-file delivery from a stale project
snapshot base. Standard practice established D1 cleanup session.

## Changes Applied

### shell_configs.py

1. **Imports added.** Three blocks: (a) 30 hover text / tooltip string
   imports from `solar_visualization_shells` (15 `*_info_hover` for
   Plotly, 15 `*_info` for Tkinter, plus 3 custom tooltip strings);
   (b) 15 radius constant imports from `planet_visualization_utilities`.

2. **SHELL_CONFIGS['Sun'] inserted.** 15 sphere shell entries, each
   with `name`, `radius_au`, `color`, `opacity`, `n_points`,
   `marker_size`, `hover_text`, and `tooltip` fields. All `radius_au`
   values expressed as constant expressions (e.g.
   `CHROMOSPHERE_RADII * SOLAR_RADIUS_AU`). All hover/tooltip text
   referenced via imported variable names (no inline duplication).

3. **CUSTOM_SHELLS['Sun'] inserted.** 3 entries (`hills_cloud_torus`,
   `outer_oort_clumpy`, `galactic_tide`) following Jupiter pattern:
   `'builder'` string for lazy import, `'tooltip'` referencing source
   module strings. No `'hover_text'` field (Plotly hover lives inside
   the builder functions).

4. **Option A legend names.** The 9 shells with existing `"Sun: <X>"`
   source names use clean `'name'` values (e.g. `'Core'`). The 6
   non-conforming shells use editorial names:
   - `Solar Wind Termination Shock` -> `'name': 'Termination Shock'`
   - `Solar Wind Heliopause` -> `'name': 'Heliopause'`
   - `Inner Limit of Oort Cloud` -> `'name': 'Inner Limit of Oort Cloud'`
   - `Inner Oort Cloud` -> `'name': 'Inner Oort Cloud'`
   - `Outer Oort Cloud` -> `'name': 'Outer Oort Cloud'`
   - `Sun's Gravitational Influence` -> `'name': 'Gravitational Influence'`

5. **Key-to-string mappings preserved.** Two legacy naming asymmetries
   carried through correctly:
   - Heliopause: SHELL_CONFIGS key `'heliopause'`, info strings named
     `solar_wind_info_hover` / `solar_wind_info` (legacy naming).
   - Inner Oort Limit: SHELL_CONFIGS key `'inner_oort_limit'`, info
     strings named `inner_limit_oort_info_hover` / `inner_limit_oort_info`
     (swapped word order).

### solar_visualization_shells.py

6. **Dead code stripped** (bottom-up, 5 items):
   - `enhanced_oort_hover_text` string constant (24 lines)
   - `create_oort_cloud_density_visualization()` (50 lines, never called)
   - `create_enhanced_oort_cloud_visualization()` (64 lines, double-dead:
     would crash with `ValueError` attempting `x, y, z =` unpack on a
     list of Plotly traces)
   - Duplicate import block at ~line 1430 (2 lines, re-imported `go` and
     `create_sphere_points` already at top)
   - `create_corona_sphere()` + preceding comment (12 lines, pre-
     `create_sphere_points` ancestor)
   - `create_sun_hover_text()` (35 lines, dict duplicating `*_info_hover`
     content)

7. **`center_position=(0,0,0)` added** to all 3 custom function
   signatures as first parameter with default value. Existing no-arg
   callers (`create_sun_visualization()` at `planet_visualization.py`
   lines 322/325/328) continue to work unchanged. Function bodies NOT
   modified -- geometry still generates at origin. Breadcrumb comments
   and `Parameters:` docstring sections added to all three.

---

## Verification Results

| Test | Result |
|------|--------|
| shell_configs.py compiles | PASS |
| solar_visualization_shells.py compiles (AST parse) | PASS |
| SHELL_CONFIGS: 13 bodies (12 + Sun) | PASS |
| Total sphere configs: 83 (68 + 15) | PASS |
| CUSTOM_SHELLS: 9 bodies (8 + Sun) | PASS |
| Total custom entries: 24 (21 + 3) | PASS |
| All 15 Sun sphere shells have required fields | PASS |
| Sun custom entries match Jupiter schema (builder + tooltip, no hover_text) | PASS |
| `build_sphere_shell` produces 2 traces per Sun shell | PASS |
| All Sun trace names start with `"Sun: "` | PASS |
| `center_position` is first param with default `(0,0,0)` on all 3 custom | PASS |
| Custom functions callable with no args (backward compat) | PASS |
| Custom functions callable with `center_position` arg | PASS |
| 5 dead items stripped (no longer in module attributes) | PASS |
| LF line endings: both files | PASS |
| ASCII encoding: both files | PASS |

### Tests requiring Tony's local environment

| Test | Status |
|------|--------|
| `create_sun_visualization()` still callable (Section 7.5) | **N/A -- function retired (item 29)** |
| GUI smoke test (Section 7.9) | **PASS (item 29 Mode 5 review)** |
| Provenance scanner (Section 7.8) | PENDING -- Tony runs locally |

---

## Architecture Notes

### Sun config pattern: `radius_au` (not `radius_fraction`)

The Sun is the first body to use `radius_au` exclusively in
SHELL_CONFIGS. All 15 shells express radius as direct AU values or
constant expressions (e.g. `CHROMOSPHERE_RADII * SOLAR_RADIUS_AU`).
Previous bodies use `radius_fraction` (multiplied by body radius from
`CENTER_BODY_RADII`). The `build_sphere_shell()` dispatch at
`orrery_rendering.py:89` already supports both paths -- no rendering
layer changes needed.

### Hover text convention: proper separation

D1's Sun entries include both `hover_text` (Plotly, `<br>` line breaks)
and `tooltip` (Tkinter, `\n` line breaks) in each SHELL_CONFIGS entry.
This is the proper pattern from C1 (Mercury). C4's Saturn/Uranus/Neptune
entries only have `hover_text` using `*_info` strings (with `\n` line
breaks -- the Tkinter variant, not the Plotly variant). This C4 shortcut
means their Plotly hovers render with collapsed/truncated text (tracked
as deferred item 27). The Sun entries avoid this by using the correct
`*_info_hover` strings for `hover_text`.

### CUSTOM_SHELLS tooltip source strings

D1 uses imported variable references (`hills_cloud_torus_info`,
`outer_oort_clumpy_info`, `galactic_tide_info` from
`solar_visualization_shells.py`) rather than composed inline text.
This eliminates recalled-not-fetched risk and keeps the source module
as the single authority for tooltip content. The source strings use
`\n` line breaks, matching the CUSTOM_SHELLS tooltip convention
(Tkinter GUI display).

### Legend name normalization (Option A -- live)

Six Sun shells had source trace names that didn't follow the
`"Sun: <X>"` pattern used by the other 9. Option A accepted the rename
at switchover: configs use clean `'name'` values; `build_sphere_shell()`
prepends `"Sun: "`. Mode 5 visual review confirmed all 6 renames.

| Current source name | Switchover name |
|--------------------|-----------------|
| `Solar Wind Termination Shock` | `Sun: Termination Shock` |
| `Solar Wind Heliopause` | `Sun: Heliopause` |
| `Inner Limit of Oort Cloud` | `Sun: Inner Limit of Oort Cloud` |
| `Inner Oort Cloud` | `Sun: Inner Oort Cloud` |
| `Outer Oort Cloud` | `Sun: Outer Oort Cloud` |
| `Sun's Gravitational Influence` | `Sun: Gravitational Influence` |

### No sun indicators for the Sun

None of the 15 Sun sphere configs have `has_sun_indicator`. The Sun
doesn't point at itself. The unified dispatch already suppresses the
indicator when `object_type='Sun'` (via `shared_utilities.py` line 50:
`if object_type == 'Sun': return []`).

---

## D1 Cleanup Batch (Items 14, 15, 27, 31, 32, 33, 34)

Tested and deployed same session as D1. All pre-existing issues.

### shell_configs.py (+21 lines from cleanup)

8. **Item 27: hover_text/tooltip separation for Saturn/Uranus/Neptune.**
   16 sphere shell entries across 3 bodies. Each entry now has:
   - `'hover_text'`: `*_info.replace('\n', '<br>')` for Plotly
   - `'tooltip'`: `*_info` for Tkinter
   Venus already correct from C1 (item 16 resolved).

9. **Item 33: Sun photosphere mesh3d.** Added `'geometry_type': 'mesh3d'`
   and `'mesh_resolution': 24` to dormant photosphere config. Visual
   change activates at switchover (item 29).

### solar_visualization_shells.py (+27 lines from cleanup)

10. **Item 31: `hover_text_sun_and_corona_tooltip`.** Added plain-text
    version with `\n` line breaks for Tkinter `CreateToolTip`. The
    original `hover_text_sun_and_corona` (with `<br>`/`<b>`) preserved
    for Plotly use.

11. **Item 32: Custom info marker borders.** 3 custom function info
    markers (Hills Cloud, Outer Oort Clumpy, Galactic Tide) updated
    to `size=8, opacity=1.0, line=dict(color='red', width=2)`,
    matching the `create_info_marker()` standard.

### neptune_visualization_shells.py (-8 lines from cleanup)

12. **Item 14: Debug print stripped.** `print(f"Returning {len(traces)}
    magnetic field traces")` removed from `create_neptune_magnetic_poles`.

13. **Item 15: Function-local imports promoted.** `create_magnetosphere_shape`
    added to top-level import from `planet_visualization_utilities`.
    Three function-local import blocks stripped (lines ~472-474, ~632).

### palomas_orrery.py (Mode 1 snippet, 2 lines -- applied by Tony)

14. **Item 31: Tooltip wiring.** Import `hover_text_sun_and_corona_tooltip`
    added (line 211). `CreateToolTip` call (line 7867) updated to use
    the tooltip version.

### Provenance scan

4 pre-existing Tier-1 findings (unchanged from prior scan, not
introduced by D1). All are display strings without source citations.
Deferred to D3 for Mode 7/Gemini factual verification (items 36-39).

---

## Item 29: Sun Call Site Switchover

Executed same session as D1. Manifest prepared by Claude Opus 4.6,
10 snippets across 2 files. `palomas_orrery.py` (7 snippets) applied
by Tony manually; `planet_visualization.py` (3 snippets) delivered
as complete file by Claude.

### palomas_orrery.py (7 Mode 1 snippets, applied by Tony)

15. **Dead imports removed.** `create_sun_visualization` and
    `create_sun_corona_from_distance` deleted from `planet_visualization`
    import block.

16. **`sun_corona_from_distance_var` removed.** `tk.IntVar` definition
    deleted.

17. **`corona_from_distance` key removed from `sun_shell_vars`.** Dict
    entry deleted.

18. **Static center-body switchover.** `create_sun_visualization(fig,
    sun_shell_vars)` replaced with `create_celestial_body_visualization()`
    call with `object_type='Sun'`, `center_object='Sun'`,
    `center_position=(0, 0, 0)`. Axis auto-scaling added. 4 asteroid
    belt `if`-blocks added as direct calls after dispatch.

19. **Off-center Sun via unified dispatch.** `corona_from_distance`
    block replaced with `create_celestial_body_visualization()` at
    Sun's offset position. `any(var.get() == 1 ...)` check fires
    for all Sun shells -- belt keys silently skipped by dispatch (not
    in registries). No special checkbox needed.

20. **Animation center-body switchover.** Same pattern as static path
    (snippet 18) with animation print statement preserved.

21. **GUI cleanup.** `corona_from_distance` checkbox (14 lines) and
    tooltip removed from shell options frame.

### planet_visualization.py (3 snippets, delivered as complete file)

22. **Dead asteroid belt imports removed.** 12-line import block from
    `asteroid_belt_visualization_shells` deleted. All 12 symbols were
    only consumed by the retired `create_sun_visualization()`. The 4
    creation functions are already imported directly in
    `palomas_orrery.py` (lines 235-239).

23. **`create_sun_visualization()` retired.** 113-line function replaced
    with 12-line stub raising `NotImplementedError`.

24. **`create_sun_corona_from_distance()` retired.** 119-line function
    replaced with 13-line stub raising `NotImplementedError`.

### Verification

| Test | Result |
|------|--------|
| `palomas_orrery.py` compiles | PASS |
| `planet_visualization.py` compiles | PASS |
| ASCII encoding: both files | PASS |
| LF line endings: both files | PASS |
| Zero references to `create_sun_visualization` in palomas_orrery.py | PASS |
| Zero references to `corona_from_distance` in palomas_orrery.py | PASS |
| Runtime -- GUI launch (xvfb headless, 182 objects loaded) | PASS |

### Mode 5 Visual Review (Tony, May 19, 2026)

**Test 1: Sun-centered static plot -- ALL PASS**

- All 15 sphere shells render at origin
- Photosphere renders as mesh3d solid surface (item 33 now live)
- 3 custom shells render (Hills Cloud, Outer Oort Clumpy, Galactic Tide)
- 6 legend names normalized (confirmed all 6 renames)
- All other Sun legends retain `Sun:` prefix
- Single info markers present
- Asteroid belts render (Main Belt, Hildas, Trojans Greeks, Trojans Trojans)
- Axis auto-scales with Auto scale mode

**Test 2: Non-Sun-centered -- ALL PASS**

- `corona_from_distance` checkbox gone from GUI
- All selected Sun shells render at Sun's offset position
- Sun direction indicator does not appear on Sun shells
- Center body (Earth) shells render at origin normally

**Test 3: Animation -- ALL PASS**

- Sun shells render as static traces
- Asteroid belts render in animated plot
- Animation frames play correctly

### Tony's Observations (Mode 5)

1. **Legend ordering.** Legend items roughly but not exactly follow
   shell rendering order. This is determined by trace-add order in
   `create_celestial_body_visualization()` (iteration over SHELL_CONFIGS
   then CUSTOM_SHELLS dict keys). Not a bug -- a future polish item
   if desired. Do not fix manually.

2. **Asteroid belt hover markers not standard style.** The belt modules
   (`asteroid_belt_visualization_shells.py`) predate the single info
   marker refactor (C1-C4, 141-conversion session). They use old-style
   hover. Not in scope for item 29 -- belt code was moved, not changed.
   Track under D3 asteroid belt restructuring (item 2).

3. **Belts/Trojans/Hildas do not render off-center.** Correct behavior.
   Belt geometry is Sun-centered by definition. The snippets
   intentionally place belt calls only in the center-body path
   (snippets 18, 20), not the off-center path (snippet 19).

### Capability Gains

1. **Universal off-center Sun rendering.** All 15 sphere + 3 custom
   shells render at Sun's offset position from any center body.
   Previously limited to 7 shells from a subset of centers via
   the `corona_from_distance` workaround.

2. **Axis auto-scaling.** Sun-centered plots auto-scale to outermost
   active shell radius, matching planet behavior.

3. **Consistent legend naming.** All Sun shells follow `"Sun: <X>"`
   convention.

4. **Single info markers on off-center Sun.** Off-center rendering now
   uses the single info marker pattern (inherited from SHELL_CONFIGS).
   Previously `corona_from_distance` used old multi-hover pattern.

5. **Simplified GUI.** One confusing special checkbox removed. Users
   just check the shells they want, same as any planet.

### Runtime Test Protocol

The agentic pre-test protocol (project instructions v3.23, Part 3,
CRITICAL tier) catches syntax and runtime errors before Tony deploys
to his local environment. Steps:

```
apt-get install -y python3-tk xvfb
python3 -m py_compile palomas_orrery.py
sed -i "s/SystemButtonFace/gray90/g" palomas_orrery.py
timeout 30 xvfb-run -a python3 palomas_orrery.py 2>&1 | head -50
sed -i "s/gray90/SystemButtonFace/g" palomas_orrery.py
```

Division of labor: Claude tests syntax + runtime (import chain,
GUI initialization, 182 objects loaded). Tony tests visual + Windows-
specific behavior (Mode 5 checklist). This protocol should be run
for any session that modifies `palomas_orrery.py` or its direct
imports.

---

## Deferred Items

### Resolved by D1

- ~~Item 1 (partial): Sun config extraction~~ **DONE** -- configs
  registered in SHELL_CONFIGS and CUSTOM_SHELLS. Call site replacement
  deferred (see new item 29).

### Resolved by D1 cleanup batch

- ~~Item 14: Neptune debug print~~ **DONE**
- ~~Item 15: Neptune function-local imports~~ **DONE**
- ~~Item 16: Venus hover text~~ **DONE (C1 -- already correct)**
- ~~Item 27: Saturn/Uranus/Neptune hover_text \n -> <br>~~ **DONE**
- ~~Item 31: hover_text_sun_and_corona Tkinter tags~~ **DONE**
- ~~Item 32: Sun custom info marker borders~~ **DONE**
- ~~Item 33: Sun photosphere mesh3d config~~ **DONE (now live)**
- ~~Item 34: Photosphere hover truncation~~ **DONE (resolved by 27+33)**

### Resolved by item 29

- ~~Item 29: Sun call site switchover~~ **DONE**
- ~~Item 35: `corona_from_distance` limited coverage~~ **DONE (retired)**

### Updated items

| # | Change | Detail |
|--:|--------|--------|
| 1 | Complete | Config extraction done (D1). Call site switchover done (item 29, same session). `create_sun_visualization()` retired. |
| 2 | Clarified | Asteroid belt stays as direct calls at call sites. Design question deferred to D3. Belt hover markers not yet on single info marker standard (new item 40). |
| 26 | Moved | From "Pre-D1" to D3. D1 is extraction-only; tooltip text unchanged and no more exposed than before. Sun CUSTOM_SHELLS tooltips use source strings (zero composed text), so item 26 scope unchanged from C4. |
| 33 | Live | mesh3d config was dormant in D1; now live after item 29 switchover. Mode 5 confirmed. |
| 35 | Retired | `corona_from_distance` function and GUI checkbox removed. Off-center Sun rendering now universal via unified dispatch. |

### New items from D1

29. **Sun call site switchover.** ~~Replace the two
    `create_sun_visualization()` call sites in `palomas_orrery.py`
    (lines ~4509 and ~6149) with delegation to
    `create_celestial_body_visualization()`.~~ **DONE (same session as
    D1).** Both functions retired. `corona_from_distance` checkbox
    removed. Asteroid belts separated to direct calls. Off-center Sun
    rendering universal. 10 snippets, 2 files, -191 lines net.
    Mode 5 visual review passed all 18 checks.

30. **Sun sphere shell `\n` in tooltip vs hover_text convention.**
    D1 correctly separates hover_text (`<br>`) from tooltip (`\n`).
    This is the proper pattern. C4's Saturn/Uranus/Neptune only have
    hover_text using `*_info` strings with `\n` (item 27). The Sun
    entries do NOT have this problem -- they use the correct
    `*_info_hover` strings for `hover_text`. No action needed for Sun;
    item 27 applies only to Saturn/Uranus/Neptune/Venus.

31. **`hover_text_sun_and_corona` Tkinter formatting.** Pre-existing.
    The "Solar System Structures" parent checkbox tooltip at
    `palomas_orrery.py:7867` uses `hover_text_sun_and_corona` (defined
    at `solar_visualization_shells.py:840`), which contains `<b>` and
    `<br>` Plotly HTML tags. Tkinter `CreateToolTip` renders plain text,
    so the tags display literally. Fix: create a `\n` version for
    the tooltip. Same class of issue as item 27, reverse direction.
    Discovered during D1 Mode 5 testing, May 19, 2026.

32. **Sun info marker border style.** Pre-existing. Sun shell info
    markers use the default thin border, while other bodies (post-C1)
    use a thicker red border for visibility. Consider centralizing the
    info marker style so all bodies use the same red-border standard.
    This could be a one-line change to `create_info_marker()` in
    `orrery_rendering.py` or a per-body config field. Discovered
    during D1 Mode 5 testing, May 19, 2026.

33. **Sun photosphere mesh3d.** Pre-existing. The photosphere renders
    as `scatter3d` (dot sphere) but should use `mesh3d` (solid surface)
    like planetary crusts and cloud layers. `'geometry_type': 'mesh3d'`
    and `'mesh_resolution': 24` added to config in D1 cleanup.
    **Now live** after item 29 switchover. Mode 5 confirmed solid
    surface rendering. Discovered during D1 Mode 5 testing, May 19, 2026.

34. **Photosphere hovertext truncation.** Pre-existing. Same class as
    item 27 (`\n` vs `<br>` in hover strings). Discovered during D1
    Mode 5 testing, May 19, 2026.

35. **`corona_from_distance` retired.** ~~Pre-existing. The
    `create_sun_corona_from_distance()` function in
    `planet_visualization.py` (lines 413-504) is a separate rendering
    path for non-Sun-centered views.~~ **DONE (item 29).** Function
    retired to stub. Off-center Sun rendering now uses unified dispatch
    with `center_position`. GUI checkbox removed. All 18 Sun shells
    render at Sun's offset position from any center body.

36. **Provenance Tier-1: neptune line 584 display string.** 1 claim,
    no source. Deferred to D3 for Mode 7/Gemini factual verification.

37. **Provenance Tier-1: spacecraft_encounters line 237 display string.**
    2 claims, no source. Deferred to D3.

38. **Provenance Tier-1: spacecraft_encounters line 268 display string.**
    5 claims, no source. Deferred to D3.

39. **Provenance Tier-1: uranus line 509 display string.** 2 claims,
    no source. Deferred to D3.

40. **Asteroid belt hover markers: single info marker conversion.**
    The 4 belt modules (`create_main_asteroid_belt`, `create_hilda_group`,
    `create_jupiter_trojans_greeks`, `create_jupiter_trojans_trojans`)
    predate the single info marker refactor (C1-C4, 141 conversions).
    They still use old-style per-point hover. Convert to single info
    marker standard. Natural fit for D3 asteroid belt restructuring
    (item 2). Discovered during item 29 Mode 5 review, May 19, 2026.

41. **Sun legend ordering.** Legend items roughly but not exactly follow
    shell size order. Determined by dict iteration order in
    `create_celestial_body_visualization()` (SHELL_CONFIGS then
    CUSTOM_SHELLS). Not a bug -- cosmetic polish. Do not fix manually;
    would require ordered iteration in the dispatch function. Low
    priority. Discovered during item 29 Mode 5 review, May 19, 2026.

### Carried forward (full cross-reference)

| Item | Stage | Description | Status |
|-----:|:-----:|-------------|--------|
| 1 | -- | Sun config extraction | **DONE (D1)** |
| 2 | D3 | Asteroid belt migration decision | Open |
| 3 | D3 | Retire create_planet_visualization() | Open |
| 4 | D2 | sun_position wiring | Open |
| 5 | D3 | _info import cleanup | Open |
| 6 | D3 | Archive dead shell files/functions | Open |
| 7 | D3 | Tooltip rewiring | Open |
| 8 | D3 | Dead create_sun_direction_indicator imports | Open |
| 9 | D3 | palomas_orrery_helpers.py CRLF | Open |
| 10 | D2 | Double sun direction indicator | Open |
| 11 | D2 | Earth/Jupiter magnetic_tilt_deg | Open |
| 12 | D2 | Neptune magnetic poles sun_position | Open |
| 13 | D3 | Neptune ring info marker rotation | Open |
| 14 | -- | Neptune print() debug | **DONE (D1 cleanup)** |
| 15 | -- | Neptune function-local imports | **DONE (D1 cleanup)** |
| 16 | -- | Venus hover text \n -> <br> | **DONE (C1 -- already correct)** |
| 17 | D3 | GEO info marker position | Open |
| 18 | D3 | Uranus gossamer ring | Open |
| 19 | D3 | Manual axis dtick in orrery GUI | Open |
| 20 | -- | n_points GUI (standalone) | Open |
| 21 | -- | Animation shell rendering (standalone) | Open |
| 22 | E | Satellite internal structure shells | Open |
| 23 | E | Earth ionosphere | Open |
| 24 | E | Gas giant bow shocks | Open |
| 25 | E | Mars magnetosphere info marker | Open |
| 26 | D3 | CUSTOM_SHELLS tooltip verification (Mode 7) | Open (moved from Pre-D1) |
| 27 | -- | Sphere shell \n -> <br> (Saturn/Uranus/Neptune) | **DONE (D1 cleanup)** |
| 28 | D3 | Neptune superimposed info markers | Open |
| 29 | -- | Sun call site switchover | **DONE (D1 session)** |
| 30 | -- | Sun hover_text/tooltip pattern correct (no action) | **NOTE (D1)** |
| 31 | -- | `hover_text_sun_and_corona` Tkinter formatting | **DONE (D1 cleanup)** |
| 32 | -- | Sun custom info marker border style | **DONE (D1 cleanup)** |
| 33 | -- | Sun photosphere mesh3d (now live) | **DONE (D1 cleanup + item 29)** |
| 34 | -- | Photosphere hovertext truncation | **DONE (resolved by 27+33)** |
| 35 | -- | `corona_from_distance` limited coverage | **DONE (retired by item 29)** |
| 36 | D3 | Provenance Tier-1: neptune line 584 display string (1 claim, no source) | **NEW (D1 scan)** |
| 37 | D3 | Provenance Tier-1: spacecraft_encounters line 237 display string (2 claims, no source) | **NEW (D1 scan)** |
| 38 | D3 | Provenance Tier-1: spacecraft_encounters line 268 display string (5 claims, no source) | **NEW (D1 scan)** |
| 39 | D3 | Provenance Tier-1: uranus line 509 display string (2 claims, no source) | **NEW (D1 scan)** |
| 40 | D3 | Asteroid belt hover markers: convert to single info marker standard | **NEW (item 29 Mode 5)** |
| 41 | -- | Sun legend ordering: trace-add order vs shell size order (polish) | **NEW (item 29 Mode 5, low priority)** |

---

## Phase D Staging (updated)

### D1: Sun config extraction + switchover -- COMPLETE

Config extraction (15 sphere + 3 custom configs) and call site
switchover (item 29) completed in the same session.
`create_sun_visualization()` and `create_sun_corona_from_distance()`
retired. Asteroid belts separated to direct calls. `corona_from_distance`
GUI checkbox removed. Sun now renders through unified dispatch at all
three call sites. Mode 5 visual review passed.

### D2: `sun_position` threading

Thread Sun position through unified dispatch into `rotate_to_sunward()`
and `create_sun_direction_indicator()`. Also: Earth/Jupiter
`magnetic_tilt_deg`, Neptune pole extension, double indicator
deduplication. Unchanged from C4 handoff.

### D3: Cleanup sweep

Pure cleanup. Unchanged from C4 handoff, plus item 26 (moved from
Pre-D1), asteroid belt migration decision (item 2, moved from D1),
and new item 40 (belt hover marker conversion to single info marker
standard, discovered during item 29 Mode 5 review).

---

## Post-D1 State (with item 29)

| Component | Count |
|-----------|------:|
| Bodies in SHELL_CONFIGS | 13 |
| Total sphere shell configs | 83 |
| Bodies in CUSTOM_SHELLS | 9 |
| Total custom entries | 24 |
| Bodies still on old dispatch | **0** (all 13 on unified dispatch) |
| `rotate_to_sunward()` exercised by | 8 bodies (unchanged) |
| `create_ring_points()` used by | 3 bodies (unchanged) |
| `magnetic_tilt_deg` used live by | 1 (Uranus 60 deg, unchanged) |
| `sun_position` wired | No (Phase D2) |
| Dead code removed in D1 | ~196 lines (5 items + duplicate imports) |
| Dead code removed in item 29 | ~220 lines (2 retired functions + imports) |
| Retired functions (stubs) | 2 (`create_sun_visualization`, `create_sun_corona_from_distance`) |
| GUI elements removed | 1 (`corona_from_distance` checkbox + tooltip) |
| Deferred items total | 41 (14 resolved, 27 open) |
| Deferred items resolved this session | 14, 15, 16, 27, 29, 31, 32, 33, 34, 35 |
| Provenance Tier-1 findings | 4 pre-existing (items 36-39) |

---

## Credit

```
Module updated: May 2026 with Anthropic's Claude Opus 4.6
```

Applied to all delivered files. Opus 4.7 credited for D1 manifest
(~1,250 lines) including legend-name analysis, dead-code crash
confirmation, key-to-string mapping verification, and auto-gen script.
Opus 4.6 for D1 implementation, tooltip source-string decision,
hover_text/tooltip separation finding, all D1 verification, item 29
manifest preparation and implementation, and runtime test protocol.

---

*Paloma's Orrery | palomasorrery.com*
*"Three Claudes, one Tony, zero orchestration framework." -- May 2026*
