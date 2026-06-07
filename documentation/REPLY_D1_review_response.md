# Phase D1 Review Reply -- Response to Audit Review

**From:** Tony Quintanilla (integrator) + Claude Opus 4.6 (implementation partner)
**To:** Claude (manifest author)
**Date:** May 18, 2026

---

## Review accepted with all corrections

The audit review identified three corrections and four clarifications.
All verified against source code. Accepted in full.

---

## Corrections incorporated

### Correction 1: Config field names are `hover_text` and `tooltip`

Confirmed. Every SHELL_CONFIGS sphere shell entry uses:
- `'hover_text'`: Plotly hover text (`<br>` line breaks), sourced from
  `*_info_hover` strings in the body module
- `'tooltip'`: Tkinter GUI tooltip (`\n` line breaks), sourced from
  `*_info` strings in the body module

Both fields go into each SHELL_CONFIGS entry. The `*_info` strings
continue to exist in `solar_visualization_shells.py` for backward-compat
imports by `palomas_orrery.py` (cleanup is deferred item 5 in D3).

The prompt's Q3 reference to `info_string` was wrong. Corrected.

### Correction 2: Heliopause uses `solar_wind_*` naming

Confirmed. The heliopause shell function (`create_sun_heliopause_shell`,
line 1084) reads `solar_wind_info_hover` for Plotly hover (line 1105).
The GUI tooltip at `palomas_orrery.py:7973` uses `solar_wind_info`.
Constants `heliopause_info` and `heliopause_info_hover` do not exist.

The trace is named `'Solar Wind Heliopause'` in source. Preserve this
naming. The SHELL_CONFIGS key is `'heliopause'` (matching the
`sun_shell_vars` key), with `'name': 'Solar Wind Heliopause'`.

### Correction 3: Key-to-display-name mappings must be explicit

Two specific risks identified:

**`'gravitational'`:** The `sun_shell_vars` key is `'gravitational'`
(`palomas_orrery.py:2492`). The SHELL_CONFIGS key must be
`'gravitational'` -- not `'gravitational_influence'`. The display name
goes in `'name': "Sun's Gravitational Influence"` (matching the trace's
`name=` argument in source at line 978).

**`'inner_oort_limit'`:** The `sun_shell_vars` key is
`'inner_oort_limit'` (`palomas_orrery.py:2499`). The info strings use
the swapped order: `inner_limit_oort_info` and
`inner_limit_oort_info_hover`. The SHELL_CONFIGS key must be
`'inner_oort_limit'` (matching the shell_vars key after prefix-strip).
The info strings are referenced by their actual names regardless of
key ordering.

---

## Clarifications incorporated

### A: CUSTOM_SHELLS tooltip convention

Confirmed. CUSTOM_SHELLS entries use inline `'tooltip'` strings with
`\n` line breaks. No `'hover_text'` field -- Plotly hover text lives
inside the builder functions (already present: `hills_hover`,
`clumpy_hover`, `tide_hover`). Follow the Jupiter pattern exactly.

### B: Display names from source `name=` arguments

Extract `'name'` field values from the `go.Scatter3d(name=...)` calls
inside each source function. Do not invent display names.

### C: Dead Oort functions are broken, not just unused

Confirmed. `create_enhanced_oort_cloud_visualization()` (line 1625)
tries `x_hills, y_hills, z_hills = create_sun_hills_cloud_torus()` --
but that function returns `[shell_trace, info_trace]`, not coordinate
tuples. Would crash with `ValueError` if called. Same pattern at
line 1644 with `create_sun_outer_oort_clumpy()`. Strengthens the strip
case: not just dead but broken.

### D: Q1 `center_position` is mandatory, not a recommendation

Accepted. The unified dispatch calls custom builders as
`builder(center_position)` (`planet_visualization.py:609`). Without
the parameter, the switchover phase would pass a tuple as `inner_radius`
and crash or produce garbage.

**Decision:** Add `center_position=(0,0,0)` as the first parameter to
all three custom functions in D1. The current no-arg callers
(`create_sun_visualization()` at `planet_visualization.py` lines
322/325/328) continue to work unchanged because the parameter has a
default value. This is a forward-compatible change that prevents the
switchover phase from needing to revisit `solar_visualization_shells.py`.

---

## Sidebar: Deferred item 26 timing

The review correctly identifies that "Pre-D1" is ambiguous for item 26
(CUSTOM_SHELLS tooltip factual verification via Mode 7/Gemini). Since
D1 is now extraction-only with no behavior change, the tooltip text is
unchanged and no more exposed than before. Move item 26 to D3 -- the
tooltip verification can run anytime before or during D3 and is
independent of code work. This matches the original intent: "Can run
anytime before or during Phase D."

---

## Complete key-to-source mapping for manifest author

To prevent any ambiguity, here is the explicit mapping for all 15
sphere shells and 3 custom entries. All verified against source.

### Sphere shells: `sun_shell_vars` key -> SHELL_CONFIGS key -> function -> info strings

| shell_vars key | SHELL_CONFIGS key | Function | `hover_text` source | `tooltip` source | `name` (from trace) |
|---------------|------------------|----------|--------------------|-----------------|--------------------|
| `core` | `core` | `create_sun_core_shell` | `core_info_hover` | `core_info` | `Sun: Core` |
| `radiative` | `radiative` | `create_sun_radiative_shell` | `radiative_zone_info_hover` | `radiative_zone_info` | `Sun: Radiative Zone` |
| `photosphere` | `photosphere` | `create_sun_photosphere_shell` | `photosphere_info_hover` | `photosphere_info` | `Sun: Photosphere` |
| `chromosphere` | `chromosphere` | `create_sun_chromosphere_shell` | `chromosphere_info_hover` | `chromosphere_info` | `Sun: Chromosphere` |
| `inner_corona` | `inner_corona` | `create_sun_inner_corona_shell` | `inner_corona_info_hover` | `inner_corona_info` | `Sun: Inner Corona` |
| `streamer_belt` | `streamer_belt` | `create_sun_streamer_belt_shell` | `streamer_belt_info_hover` | `streamer_belt_info` | `Sun: Streamer Belt (Visible Corona)` |
| `roche_limit` | `roche_limit` | `create_sun_roche_limit_shell` | `roche_limit_info_hover` | `roche_limit_info` | `Sun: Roche Limit (Comets)` |
| `alfven_surface` | `alfven_surface` | `create_sun_alfven_surface_shell` | `alfven_surface_info_hover` | `alfven_surface_info` | `Sun: Alfven Surface` |
| `outer_corona` | `outer_corona` | `create_sun_outer_corona_shell` | `outer_corona_info_hover` | `outer_corona_info` | `Sun: Outer Corona` |
| `termination_shock` | `termination_shock` | `create_sun_termination_shock_shell` | `termination_shock_info_hover` | `termination_shock_info` | `Solar Wind Termination Shock` |
| `heliopause` | `heliopause` | `create_sun_heliopause_shell` | `solar_wind_info_hover` | `solar_wind_info` | `Solar Wind Heliopause` |
| `inner_oort_limit` | `inner_oort_limit` | `create_sun_inner_oort_limit_shell` | `inner_limit_oort_info_hover` | `inner_limit_oort_info` | `Inner Limit of Oort Cloud` |
| `inner_oort` | `inner_oort` | `create_sun_inner_oort_shell` | `inner_oort_info_hover` | `inner_oort_info` | `Inner Oort Cloud` |
| `outer_oort` | `outer_oort` | `create_sun_outer_oort_shell` | `outer_oort_info_hover` | `outer_oort_info` | `Outer Oort Cloud` |
| `gravitational` | `gravitational` | `create_sun_gravitational_shell` | `gravitational_influence_info_hover` | `gravitational_influence_info` | `Sun's Gravitational Influence` |

### Custom entries: `sun_shell_vars` key -> CUSTOM_SHELLS key -> builder -> tooltip (inline)

| shell_vars key | CUSTOM_SHELLS key | Builder path | Inline tooltip source |
|---------------|------------------|-------------|----------------------|
| `hills_cloud_torus` | `hills_cloud_torus` | `solar_visualization_shells.create_sun_hills_cloud_torus` | Write inline, matching Jupiter pattern |
| `outer_oort_clumpy` | `outer_oort_clumpy` | `solar_visualization_shells.create_sun_outer_oort_clumpy` | Write inline, matching Jupiter pattern |
| `galactic_tide` | `galactic_tide` | `solar_visualization_shells.create_sun_galactic_tide` | Write inline, matching Jupiter pattern |

### Keys that silently skip in unified dispatch (out of D1 scope)

| shell_vars key | Reason |
|---------------|--------|
| `main_belt` | Asteroid belt, handled by existing `create_sun_visualization()` |
| `hildas` | Asteroid belt, handled by existing `create_sun_visualization()` |
| `trojans_greeks` | Asteroid belt, handled by existing `create_sun_visualization()` |
| `trojans_trojans` | Asteroid belt, handled by existing `create_sun_visualization()` |
| `corona_from_distance` | Separate rendering path, handled by `create_sun_corona_from_distance()` |

---

## Summary of decisions

1. **All three corrections accepted.** Field names, heliopause naming,
   and key-to-display mappings corrected.
2. **All four clarifications accepted.** CUSTOM_SHELLS tooltip
   convention, display name extraction, dead code crash confirmation,
   and mandatory `center_position` parameter.
3. **Item 26 moved from Pre-D1 to D3.** No timing pressure since D1
   is extraction-only.
4. **D1 scope unchanged.** Two files, no call site changes, no behavior
   changes. Extraction + dead code cleanup + `center_position` parameter
   addition.

Proceed with the manifest.

---

## Attached context

- D1 prompt (v2, with corrections above)
- C4 handoff (self-contained, 28 deferred items)
- `solar_visualization_shells.py` (source for extraction)
- `shell_configs.py` (insertion target)

---

*"Three Claudes, one Tony, zero orchestration framework." -- May 2026*
