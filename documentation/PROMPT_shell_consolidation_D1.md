# Shell Consolidation Manifest Request -- Phase D1 (Sun Config Extraction)

**To:** Claude (audit role)
**From:** Tony Quintanilla (integrator) + Claude Opus 4.6 (implementation partner)
**Date:** May 18, 2026
**Revision:** Phase C4 complete. 12 bodies migrated to unified dispatch.
Sun is the last body on the old `create_sun_visualization()` path.
Ring helper, magnetic tilt, and all custom geometry patterns are proven.
C4 handoff (attached) is self-contained with full deferred item inventory.
**Project:** Paloma's Orrery -- Step 3 of Plotting Consolidation

---

## What we need from you

Design a detailed implementation manifest for extracting the Sun's shell
configurations into `shell_configs.py` (SHELL_CONFIGS and CUSTOM_SHELLS).
This is Phase D1 -- **config extraction only, no call site changes.**

`create_sun_visualization()` stays alive. Its two call sites in
`palomas_orrery.py` (lines 4508-4509, 6148-6149) are unchanged. The
asteroid belt functions, the `corona_from_distance` path, and the
animation frame-handling logic are all untouched.

D1 is purely additive: Sun configs go into `shell_configs.py`, verified
to produce identical traces. No behavior change. The switchover --
replacing call sites, resolving asteroid belt wiring, verifying the
animation path, and retiring `create_sun_visualization()` -- moves to
a later phase where those dependencies get their own design conversation
and explicit testing.

This follows the project's incremental approach: extract, test, reassess.
Same pattern that worked across C1-C4.

**The architecture is proven across 12 bodies.** This extraction is
mechanical for the sphere shells and custom geometry.

---

## Context: what's already done

### Phases A-C4 (May 14-18): 12 bodies migrated

All prior phases complete. Key D1-relevant state:
- `build_sphere_shell()` in `orrery_rendering.py` handles all sphere
  geometry variants (scatter3d and mesh3d) with config-driven dispatch.
- `create_info_marker()` standardizes all info markers.
- CUSTOM_SHELLS lazy-import pattern proven for magnetospheres, plasma
  tori, radiation belts, ring systems across 8 bodies.

### Current state after C4

| Component | Count |
|-----------|------:|
| Bodies in SHELL_CONFIGS | 12 |
| Total sphere shell configs | 68 |
| Bodies in CUSTOM_SHELLS | 8 |
| Total custom entries | 21 |
| Bodies still on old dispatch | 1 (Sun) |

### Files to touch in D1

| File | Current lines | Role in D1 |
|------|------:|------------|
| `solar_visualization_shells.py` | 1,760 | Source for extraction (15 sphere + 3 custom functions); dead code cleanup |
| `shell_configs.py` | 2,260 | Insert Sun sphere configs + custom entries |

**Files NOT touched in D1:**
- `planet_visualization.py` -- `create_sun_visualization()` stays alive
- `palomas_orrery.py` -- call sites unchanged
- `orrery_rendering.py` -- no changes expected

---

## D1 scope: Sun config extraction

### Sphere-category (15 functions -> SHELL_CONFIGS['Sun'])

| Shell | Function | Geometry | n_points | Radius source |
|-------|----------|----------|------:|---------------|
| Core | `create_sun_core_shell` | scatter3d | 25 | `CORE_AU` (direct AU) |
| Radiative Zone | `create_sun_radiative_shell` | scatter3d | 25 | `RADIATIVE_ZONE_AU` (direct AU) |
| Photosphere | `create_sun_photosphere_shell` | scatter3d | 25 | `SOLAR_RADIUS_AU` (direct AU) |
| Chromosphere | `create_sun_chromosphere_shell` | scatter3d | 25 | `CHROMOSPHERE_RADII * SOLAR_RADIUS_AU` |
| Inner Corona | `create_sun_inner_corona_shell` | scatter3d | 20 | `INNER_CORONA_RADII * SOLAR_RADIUS_AU` |
| Streamer Belt | `create_sun_streamer_belt_shell` | scatter3d | 20 | `STREAMER_BELT_RADII * SOLAR_RADIUS_AU` |
| Roche Limit | `create_sun_roche_limit_shell` | scatter3d | 20 | `ROCHE_LIMIT_RADII * SOLAR_RADIUS_AU` |
| Alfven Surface | `create_sun_alfven_surface_shell` | scatter3d | 20 | `ALFVEN_SURFACE_RADII * SOLAR_RADIUS_AU` |
| Outer Corona (F-corona) | `create_sun_outer_corona_shell` | scatter3d | 20 | `OUTER_CORONA_RADII * SOLAR_RADIUS_AU` |
| Termination Shock | `create_sun_termination_shock_shell` | scatter3d | 20 | `TERMINATION_SHOCK_AU` (direct AU) |
| Heliopause | `create_sun_heliopause_shell` | scatter3d | 20 | `HELIOPAUSE_RADII * SOLAR_RADIUS_AU` |
| Inner Oort Limit | `create_sun_inner_oort_limit_shell` | scatter3d | 20 | `INNER_LIMIT_OORT_CLOUD_AU` (direct AU) |
| Inner Oort Cloud | `create_sun_inner_oort_shell` | scatter3d | 20 | `INNER_OORT_CLOUD_AU` (direct AU) |
| Outer Oort Cloud | `create_sun_outer_oort_shell` | scatter3d | 20 | `OUTER_OORT_CLOUD_AU` (direct AU) |
| Gravitational Influence | `create_sun_gravitational_shell` | scatter3d | 20 | `GRAVITATIONAL_INFLUENCE_AU` (direct AU) |

**Radius convention note:** The Sun's shells use two patterns:
- Direct AU values (core, radiative, photosphere, termination shock,
  Oort cloud shells, gravitational influence).
- Multiplier * SOLAR_RADIUS_AU (chromosphere, coronas, heliopause).

Recommend expressing all as `radius_au` in the config with the product
pre-computed where needed. The Sun doesn't use `CENTER_BODY_RADII` the
same way planets do (its radius IS SOLAR_RADIUS_AU, and many shells
are far larger than the body itself).

**No sun indicators.** None of the Sun shell functions have
`has_sun_indicator` -- the Sun doesn't point at itself.

### Custom-category (3 functions -> CUSTOM_SHELLS['Sun'])

| Shell | Function | Traces | Notes |
|-------|----------|-------:|-------|
| Hills Cloud Torus | `create_sun_hills_cloud_torus` | 2 | Toroidal structure, random noise. Default params: inner=2000, outer=20000, thickness=0.3 |
| Outer Oort Clumpy | `create_sun_outer_oort_clumpy` | 2 | Clumped random points. Default params: radius_min=20000, radius_max=100000, n_clumps=15 |
| Galactic Tide | `create_sun_galactic_tide` | 2 | Asymmetric distribution. Default params: radius=50000, n_points=2000 |

All three already return `[shell_trace, info_trace]` lists with
`hoverinfo='skip'` on geometry and cross info markers. They use default
parameters in the function signature.

**Signature note:** These functions DON'T accept `center_position` --
they always generate geometry at the origin (the Sun is always at
`(0,0,0)`). The planet custom builders accept `center_position` as
their first argument. See Q1 below.

### Explicitly out of scope for D1

- **Asteroid belt entries** (4 keys in `sun_shell_vars`): `main_belt`,
  `hildas`, `trojans_greeks`, `trojans_trojans`. These are dispatched
  by the existing `create_sun_visualization()` which stays alive.
  Design question deferred to a later phase.

- **`corona_from_distance`** (`create_sun_corona_from_distance()` in
  `planet_visualization.py`, lines 413-504): separate rendering path
  for non-Sun-centered views. Called from a different code path in
  `palomas_orrery.py` (line 4645). Unchanged by D1.

- **Call site replacement**: the two `create_sun_visualization()` call
  sites in `palomas_orrery.py` (lines 4508-4509, 6148-6149) are
  unchanged. `create_sun_visualization()` stays alive.

- **Animation frame handling**: the second call site is inside the
  animation path with frame-specific logic. Untouched in D1.

---

## Design questions for D1

### Q1: Custom function signatures -- no `center_position` parameter

The three custom Sun functions have different signatures than the planet
custom builders. Planet custom builders accept `center_position` as
their first argument (called by the unified dispatch as
`builder(center_position)`).

The Sun custom functions have their own parameter signatures:
- `create_sun_hills_cloud_torus(inner_radius=2000, outer_radius=20000, thickness_ratio=0.3)`
- `create_sun_outer_oort_clumpy(radius_min=20000, radius_max=100000, n_clumps=15)`
- `create_sun_galactic_tide(radius=50000, n_points=2000)`

Since D1 is extraction only (no call site changes), the CUSTOM_SHELLS
entries are registered but not yet called by the unified dispatch. The
signature mismatch doesn't break anything in D1. However, the manifest
should document the mismatch and recommend adding
`center_position=(0,0,0)` as the first parameter to all three functions
for interface uniformity, so the switchover phase doesn't need to
revisit it. This is a one-line change per function that's safe to make
now.

### Q2: Dead code in solar_visualization_shells.py

The following are defined but never called from anywhere:

| Item | Lines | Type |
|------|------:|------|
| `create_corona_sphere()` | 932-942 | Function |
| `create_sun_hover_text()` | 895-929 | Function |
| `create_enhanced_oort_cloud_visualization()` | 1617-1680 | Function |
| `create_oort_cloud_density_visualization()` | 1682-1731 | Function |
| `enhanced_oort_hover_text` | 1736-1759 | String constant |

Also a duplicate import block at line 1430-1431 (re-imports `go` and
`create_sphere_points` that are already imported at lines 17 and 21).

Strip in D1. We're touching the file, same precedent as C4 (Neptune
dead `create_neptune_field_lines` stripped). Dead code is dead code.

### Q3: Duplicate `_info` / `_info_hover` string pairs

`solar_visualization_shells.py` defines most hover text strings twice:
- `*_info` versions with `\n` line breaks (used by Tkinter GUI tooltips,
  imported by `palomas_orrery.py` for `CreateToolTip()`)
- `*_info_hover` versions with `<br>` line breaks (used by Plotly hover
  text inside the shell functions)

Both sets are actively used -- NOT dead code. For the SHELL_CONFIGS
extraction, the `_info_hover` strings are the ones that go into the
`info_string` config field (Plotly hover text). The `_info` strings
stay in the module for GUI tooltip imports.

Confirm this is correctly understood.

### Q4: sun_shell_vars key naming -- no body prefix

Sun's `sun_shell_vars` keys use bare names: `'core'`, `'radiative'`,
`'photosphere'`, etc. (not `'sun_core'`, `'sun_radiative'`).

The unified dispatch's prefix-stripping logic:
```python
body_prefix = body_name.lower().replace(' ', '') + '_'  # -> 'sun_'
shell_name = key[len(body_prefix):] if key.startswith(body_prefix) else key
```

Since the keys don't start with `'sun_'`, they pass through unchanged.
The SHELL_CONFIGS and CUSTOM_SHELLS keys for Sun must use the same bare
names: `'core'`, `'radiative'`, `'hills_cloud_torus'`, etc.

Confirm this is correctly handled. (It should work as-is, but the
manifest should verify against the dispatch code.)

### Q5: Session structure

One session. The sphere shell extraction is highly mechanical (same
pattern 15 times), the custom entries follow the established pattern,
and the dead code cleanup is straightforward. No call site changes, no
behavior changes, no testing complexity beyond verifying the configs
match the source functions.

---

## Architecture reference

Same as C4. No changes to any contracts. The unified dispatch at
`planet_visualization.py` line 533 is unchanged. The Sun configs are
registered but not yet called by the dispatch -- that switchover is
a separate phase.

---

## Constraints

- **ASCII only** in all Python files
- **LF line endings** -- verify every file touched
- **Python binary mode** (rb/wb) for all file writes
- **Bottom-up editing** when making multiple changes to a file
- **Credit line:** `Module updated: May 2026 with Anthropic's Claude [model]`
- **Don't redesign the architecture** -- proven across 12 bodies
- **Exact data extraction** from source files, not training memory
- **n_points precedence** -- use value from current source file
- **Preserve `# Source:` citations** from provenance audit
- **No behavior changes** -- D1 is purely additive

---

## Files to audit

- `solar_visualization_shells.py` -- 15 sphere + 3 custom functions +
  dead code inventory, 1,760 lines. Source for all config extraction.
- `shell_configs.py` -- insertion point for Sun configs + custom entries,
  2,260 lines. Verify `build_sphere_shell` handles Sun's `radius_au`
  direct-AU pattern (it should -- this is how some Planet 9 and Pluto
  shells work too).

---

## Deliverables

Two files:
1. `shell_configs.py` -- with Sun entries added (SHELL_CONFIGS['Sun']
   and CUSTOM_SHELLS['Sun'])
2. `solar_visualization_shells.py` -- dead code stripped, custom function
   signatures updated per Q1 recommendation (if accepted), duplicate
   imports removed

---

## Workflow context

This manifest will be:
1. Reviewed by implementation partner + Tony (editorial review)
2. Implemented by implementation partner + Tony

D1 is the smallest phase by scope: 2 files, no call site changes, no
behavior changes. Purely additive config extraction with dead code
cleanup.

The C4 handoff (attached) documents the current state, all 28 deferred
items, and the D1/D2/D3 staging plan. D1's narrow scope (extraction
only) was a deliberate scoping decision -- the switchover, asteroid
belt wiring, and animation path verification are separate conversations
that follow after D1 is tested and verified.

---

*Paloma's Orrery | palomasorrery.com*
*"Three Claudes, one Tony, zero orchestration framework." -- May 2026*
