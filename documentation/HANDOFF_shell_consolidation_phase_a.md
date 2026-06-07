# Shell Consolidation — Phase A Handoff

**Session:** May 13-14, 2026
**Executed by:** Anthropic's Claude Opus 4.6 (implementation) from manifest by Claude Opus 4.7 (audit)
**Integrator:** Tony Quintanilla

---

## Summary

Phase A (Mercury POC) of the shell consolidation is complete. Two new
modules (`orrery_rendering.py`, `shell_configs.py`) establish the
config-driven dispatch architecture. Mercury is fully migrated: 6
sphere shells route through `build_sphere_shell()` (including mesh3d
solid surface for crusts), 2 custom geometry shells lazy-import via
`CUSTOM_SHELLS`, and 6 dead shell functions have been removed. The sun
direction indicator was restored to its original purpose (pointing
toward the Sun) and the magnetosphere/bow shock geometry now rotates
to face the Sun in off-center views.

**Net line change:** 870 + 1164 + 174 = 2,208 lines in -> 454 + 921 + 130 + 177 + 220 = 1,902 lines out. 306 lines removed despite adding two new modules.

---

## Files Delivered (5)

| File | Lines | Status | Key change |
|------|------:|--------|------------|
| `orrery_rendering.py` | 177 | NEW | `create_info_marker()` + `build_sphere_shell()` (scatter3d + mesh3d) |
| `shell_configs.py` | 220 | NEW | Mercury: 6 sphere configs + 2 custom shell entries |
| `shared_utilities.py` | 130 | Modified | Indicator points sunward; suppressed at origin |
| `planet_visualization.py` | 921 | Modified | CRLF->LF, unified dispatch, Mercury delegation |
| `mercury_visualization_shells.py` | 454 | Modified | Dead functions removed, magnetosphere rotation added |

---

## Architecture Established

### Config-driven dispatch (`planet_visualization.py`)

`create_celestial_body_visualization()` is the unified entry point:
1. Strips body prefix from shell_vars keys (`mercury_inner_core` -> `inner_core`)
2. Looks up `SHELL_CONFIGS` -> `build_sphere_shell()` for sphere shells
3. Looks up `CUSTOM_SHELLS` -> lazy import for custom geometry
4. Issues one sun direction indicator per body at outermost active shell radius

Mercury delegates through this function. All other bodies still route
through `create_planet_visualization()` (untouched) until their Phase
B/C/D migrations.

### Centralized info marker (`orrery_rendering.py`)

`create_info_marker(x, y, z, color, text, legendgroup)` — one function,
one place to change marker style. Currently: size=8, cross symbol,
red outline width=2. Used by:
- `build_sphere_shell()` (north pole markers)
- `mercury_visualization_shells.py` (sodium tail, magnetosphere, bow shock)
- `shared_utilities.py` (sun direction indicator tip)

### Sun direction indicator (`shared_utilities.py`)

Restored to original purpose — arrow points from body toward the Sun:
- Off-center (flyto view): computes sunward direction from center_position toward origin
- At origin (body-centered): suppressed (Sun visible in plot; coordinate text box handles reference frame)
- Sun shells: suppressed
- Legend: "Sun Direction"
- Hover: shows distance to Sun in AU

Backward-compat alias `create_vernal_equinox_indicator` retained.

### Magnetosphere sunward rotation (`mercury_visualization_shells.py`)

`rotate_to_sunward()` (local to magnetosphere function) applies Rodrigues'
rotation to orient both magnetosphere and bow shock geometry. At origin:
identity (default -X convention). Off-center: bow shock faces Sun,
magnetotail trails away. Same directional logic the sodium tail already
used for its particle cone.

### Mesh3d geometry support (`orrery_rendering.py`)

`build_sphere_shell()` supports two geometry types via `config['geometry_type']`:

- `'scatter3d'` (default) — dot sphere using `create_sphere_points()`.
  Used for interior anatomy shells. Requires `marker_size` and `n_points`.
- `'mesh3d'` — triangulated UV solid surface with flat shading and full
  ambient light. Used for crusts and cloud layers. Requires
  `mesh_resolution` (default 24). No `marker_size` needed.

Both types enforce the single-info-marker pattern identically: geometry
has `hoverinfo='skip'`, one cross marker at north pole. Mercury's crust
uses `'mesh3d'` — the solid surface visual from the original function is
preserved through the config-driven dispatch.

**Phase B/C/D implication:** Every body's crust config should use
`'geometry_type': 'mesh3d'`. Gas giant cloud_layer configs should also
use `'mesh3d'`. All other shells use the default `'scatter3d'`.

---

## Deferred Items

### Phase B/C/D scope (revised from original consolidation plan)

1. **Phase B — Moon + Planet 9** (all-sphere, no satellites, no custom
   geometry). Pluto and Eris deferred from Phase B: both have satellites
   (Charon + 4 small moons; Dysnomia) that need internal structure
   shells created with data sourced from Horizons. Pluto and Eris move
   to a later phase once satellite shell data is ready.

2. **Retire `create_planet_visualization()`** — Phase D, once all body
   blocks delegate to the unified dispatch. Currently 3 remaining call
   sites (Venus+ blocks at lines ~4516, ~4605, ~4618 in plot_objects,
   ~6152 in animate_objects).

3. **Retire `create_sun_visualization()`** — Phase D. 2 call sites
   (lines ~4509, ~6144).

4. **`_info` import cleanup** — Phase D. ~89 imports in `palomas_orrery.py`,
   ~87 dead imports in `palomas_orrery_helpers.py`, re-exports in
   `planet_visualization.py`. Three wiring paths: ~33 inline
   CreateToolTip calls (Path A), globals() lookup (Path B),
   Sun/asteroid direct imports (Path C).

5. **`palomas_orrery_helpers.py` CRLF -> LF** — when first modified
   (Phase D `_info` cleanup).

### Discovered during Phase A (new items)

6. **`sun_position` parameter for body-centered view** — Currently the
   magnetosphere rotation, sodium tail direction, and sun direction
   indicator all assume the Sun is at the origin. This is correct in
   heliocentric (flyto) views but not in body-centered views where the
   body is at origin and the Sun is at an offset position. Fix: thread
   `sun_position` (from the ephemeris pipeline) through the dispatch
   function and custom geometry builders. Both views would then produce
   identical shell geometry. Natural fit for Phase D when the callers
   are updated to call the unified dispatch directly — the ephemeris
   data is already available at the call sites.

7. **Magnetosphere rotation for other bodies** — The `rotate_to_sunward()`
   helper is local to `mercury_visualization_shells.py`. Venus, Earth,
   Mars, Jupiter, Saturn, Uranus, and Neptune all have magnetosphere
   functions with the same hardcoded -X orientation. During Phase C
   migration, promote `rotate_to_sunward()` to `orrery_rendering.py`
   and apply to all magnetosphere builders. Check flyto views for each.

8. **Sodium tail orientation (Mercury-centered)** — In the Mercury-
   centered view, the sodium tail points along +X (default when
   center_position is origin) rather than dynamically anti-sunward.
   This is the same body-centered framing issue as item 6. Fixed by
   `sun_position` parameter.

9. **Dead `fibonacci_sphere` code in other bodies' crust functions** —
   12 modules have dead fibonacci_sphere locals inside their crust/
   cloud_layer functions (see HANDOFF_single_info_marker_refactor.md).
   Phase B bodies (Moon, Planet 9) are left untouched — their shell
   files become entirely dead and will be batch-archived in Phase D.
   Phase C bodies' fibonacci_sphere code becomes unreachable when their
   sphere shells migrate to `build_sphere_shell()` and should be
   stripped during migration (matching Mercury's Phase A precedent).

10. **Info marker style propagation** — The `create_info_marker()` style
    (size=8, red outline) currently only applies to Mercury's shells and
    the sun direction indicator. All other bodies still have the old
    style (size=6, white outline) from Step 2. During Phase B/C/D,
    custom geometry functions are updated to import `create_info_marker()`
    (as Mercury's were in this session). Sphere shells get the new style
    automatically via `build_sphere_shell()`.

---

## Phase B Decisions (pre-resolved)

Answers to questions raised by Opus 4.7 during Phase B manifest planning.
These are decided — do not re-open.

1. **Indicator function name in the dispatch:**
   `create_sun_direction_indicator` is the canonical name. Import and
   call sites in `planet_visualization.py` use this name. The alias
   `create_vernal_equinox_indicator` exists in `shared_utilities.py`
   for backward compatibility only.

2. **Detail level:** Full mechanical detail, same as Phase A. Complete
   config blocks with values transcribed from source files, exact
   before/after snippets, per-body verification sections.

3. **Dead-function policy:** Option (b) — leave Phase B shell files
   (`moon_visualization_shells.py`, `planet9_visualization_shells.py`)
   untouched. They become entirely dead after migration. Batch-archive
   whole files in Phase D. Do NOT edit them during Phase B.

4. **`_info` import pruning:** Defer to Phase D. One batch cleanup,
   not a per-body trickle. Keeps Phase B mechanical.

5. **Mesh3d crust visual:** Crusts use `'geometry_type': 'mesh3d'` in
   configs. The solid surface visual is preserved. No Scatter3d dot
   conversion for crusts. This applies to Moon and Planet 9 in Phase B,
   and all other bodies in subsequent phases.

6. **Verification cadence:** One body at a time with a visual check
   after each migration.

7. **Source data freshness:** `/mnt/project/` files are confirmed current
   for Phase B bodies (Step 2 credit lines and `hoverinfo='skip'` markers
   verified). No uploads needed.

---

## Mode 5 Visual Verification Results

| Test | Result |
|------|--------|
| Mercury center, all shells on | PASS - all 8 shells render |
| Info markers (cross at north pole) | PASS - one per shell |
| Crust Mesh3d via config | PASS - solid surface restored via `geometry_type: 'mesh3d'` |
| Sun direction indicator (center) | PASS - suppressed at origin |
| Sun direction indicator (flyto) | PASS - points toward Sun |
| Magnetosphere orientation (flyto) | PASS - bow shock faces Sun |
| Other bodies unchanged | PASS - Venus, Earth, Sun render normally |
| GUI tooltips | Not yet tested (globals() path unchanged) |

---

## Protocol Notes

- **Info marker convention updated**: size=8, cross symbol, `line=dict(color='red', width=2)`. Routed through `create_info_marker()` in `orrery_rendering.py`. Update protocol v3.23 marker standard.

- **Indicator restored**: "Sun Direction" replaces "Vernal Equinox Direction (+X)". The coordinate text box handles reference frame education; the arrow does what's useful.

- **Mesh3d for crusts/cloud layers**: `build_sphere_shell()` accepts `geometry_type: 'mesh3d'` for solid surfaces. Preserves visual quality of crust rendering through the config-driven dispatch. Use for all body crusts and gas giant cloud layers.

- **Collegial Mode 7**: Opus 4.7 wrote the prompt review + Phase A manifest (1,178 lines). Opus 4.6 reviewed, identified issues (dispatch chain analysis, tooltip count correction), resolved with Tony, executed implementation. Tony carried context and made all design decisions.

---

## Credit

```
Module updated: May 2026 with Anthropic's Claude Opus 4.7
```

Applied to all 5 delivered files. Opus 4.7 credited for the manifest
and architectural design; Opus 4.6 for implementation, dead code
removal, magnetosphere rotation, indicator restoration, and mesh3d
geometry support.
