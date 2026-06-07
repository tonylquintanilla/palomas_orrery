# Shell Consolidation Manifest Request

**To:** Claude Opus 4.7
**From:** Tony Quintanilla (integrator) + Claude Opus 4.6 (implementation partner)
**Date:** May 12, 2026
**Project:** Paloma's Orrery — Step 3 of Plotting Consolidation

---

## What we need from you

Design a detailed implementation manifest for consolidating the planetary
shell system. This is the same role you played for the single info marker
refactor — audit the codebase, identify every conversion site, produce
reusable templates, flag judgment calls, and deliver a manifest that a
different Claude instance can execute mechanically with Tony.

**The architecture is already designed.** The plotting consolidation
handoff (included below) specifies `shell_configs.py`, `build_sphere_shell()`,
and the `CUSTOM_SHELLS` lazy-import registry. Your job is NOT to redesign
the architecture — it's to produce the conversion manifest: what moves
where, in what order, with what exact before/after snippets.

---

## Context: what's already done

### Step 1 (April 19): Single info markers for orbit traces
All orbit traces in palomas_orrery.py and idealized_orbits.py converted.

### Step 2 (May 11): Single info markers for all shells
141 conversions across 18 modules. Every shell function now uses:
- `hoverinfo='skip'` on geometry traces
- One `cross` marker at a representative position carrying hover text
- `legendgroup` linking geometry + marker
- `n_points` reduced (50 → 25 interior, 50 → 20 boundary)
- Dead `hover_texts`/`minimal_hover_texts` variable assignments stripped
- All 13 CRLF files converted to LF

**Residual dead code** (deferred to this step): `fibonacci_sphere()` and
associated `x_hover`/`y_hover`/`z_hover` locals in 12 crust/cloud_layer
functions. Now unreachable — should be stripped during migration.

### What Step 3 must accomplish

1. **Create `shell_configs.py`** — one data file containing all sphere
   shell parameters (radius, color, opacity, n_points, hover text,
   tooltip text) for every body. Plus a `CUSTOM_SHELLS` registry mapping
   non-sphere geometry to lazy-imported functions.

2. **Create `build_sphere_shell()`** — one function (in `orrery_rendering.py`
   or standalone) that takes a config dict + body name + center position
   and returns `[geometry_trace, info_marker_trace]`. Structurally
   enforces the single info marker pattern — you cannot create N hover
   copies because the function doesn't offer that option.

3. **Replace the dispatch chain** in `planet_visualization.py` — the
   ~300-line if/elif body routing becomes ~20 lines: look up config,
   call builder for sphere shells, lazy-import for custom geometry.

4. **Clean up the `_info` import chain** — ~89 imports in
   `palomas_orrery.py`, ~87 dead imports in `palomas_orrery_helpers.py`,
   re-exports in `planet_visualization.py`. Three tooltip wiring paths
   must all be updated: Earth inline calls (Path A), dynamic `globals()`
   lookup via `build_shell_checkboxes` in `celestial_objects.py` (Path B),
   and direct solar/asteroid imports (Path C). After migration, tooltips
   read from `SHELL_CONFIGS` and `CUSTOM_SHELLS` instead.

5. **Retire fully-archivable shell files** — bodies with zero custom
   geometry (Pluto, Planet 9, Eris, Moon) have their shell files become
   archivable after all their data moves to configs.

6. **Confirm LF line endings** — all shell files were converted from
   CRLF to LF in Step 2. Verify no regressions on any file touched.

---

## Current codebase inventory

### Shell files (15 modules, all post-Step-2 refactor)

| Module | Lines | Sphere funcs | Custom geometry | Archivable? |
|--------|------:|:------------:|-----------------|:-----------:|
| planet9_visualization_shells.py | 295 | 2 (incl. Mesh3d surface → sphere) | None | Yes |
| eris_visualization_shells.py | 479 | 5 (incl. Mesh3d crust → sphere) | None | Yes |
| pluto_visualization_shells.py | 576 | 6 (incl. Mesh3d crust → sphere) | None | Yes |
| moon_visualization_shells.py | 524 | 6 (incl. Mesh3d crust → sphere) | None | Yes |
| asteroid_belt_visualization_shells.py | 510 | 0 | 4 belt/cloud functions | No (all custom) |
| venus_visualization_shells.py | 726 | 5 (incl. crust → sphere) | magnetosphere/bow shock | No |
| mercury_visualization_shells.py | 780 | 6 (incl. crust → sphere) | sodium tail, magnetosphere | No |
| mars_visualization_shells.py | 836 | 6 (incl. crust → sphere) | magnetosphere, crustal fields | No |
| jupiter_visualization_shells.py | 939 | 6 (incl. cloud_layer → sphere) | rings, radiation belts, Io torus, magnetosphere | No |
| saturn_visualization_shells.py | 1,179 | 6 (incl. cloud_layer → sphere) | rings, radiation belts, Enceladus torus, magnetosphere | No |
| earth_visualization_shells.py | 1,029 | 8 (incl. crust → sphere) | magnetosphere, Van Allen, LEO, GEO | No |
| uranus_visualization_shells.py | 1,138 | 5 (incl. cloud_layer → sphere) | rings, radiation belts, magnetosphere | No |
| neptune_visualization_shells.py | 1,757 | 6 (incl. cloud_layer → sphere) | rings, radiation belts, plasma, magnetosphere | No |
| solar_visualization_shells.py | 1,748 | 15 | Hills Cloud torus, Oort clumpy, Galactic Tide | No |
| comet_visualization_shells.py | 2,003 | 0 | coma, tails, ghost tail, mini-jets | No (all custom) |

Note: `create_sun_direction_indicator()` is called inside virtually
every shell function (~50 calls across all bodies, both sphere and
custom). This consolidation will de-duplicate it to one call per body
in the dispatch loop, and rename it to `create_vernal_equinox_indicator()`
(it draws the +X reference direction, not the Sun direction). See
"Pre-decided" in the judgment calls section.

### Consumer files

| Module | Lines | Role |
|--------|------:|------|
| planet_visualization.py | 1,164 | Dispatch routing + re-exports _info strings |
| celestial_objects.py | ~1,490 | SHELL_DEFINITIONS dict + `build_shell_checkboxes()` — central tooltip wiring |
| palomas_orrery.py | 9,938 | ~89 _info imports (lines ~100-164), consumed dynamically via `globals()` by `build_shell_checkboxes`, plus 11 inline Earth CreateToolTip calls |
| palomas_orrery_helpers.py | 916 | ~87 _info imports (lines ~53-158), ALL DEAD — never consumed |
| constants_new.py | 719 | CENTER_BODY_RADII dict (line 241), KM_PER_AU (line 47) |
| shared_utilities.py | ~160 | `create_sun_direction_indicator()` — rename + de-duplicate target |

### The _info import chain (what gets eliminated)

```
Shell files define:
  pluto_core_info = "Pluto's core is believed..."     # tooltip (GUI)
  layer_info['description'] = "Core: Pluto's core..." # hover text (3D plot)

planet_visualization.py re-exports:
  from pluto_visualization_shells import (..., pluto_core_info, ...)

palomas_orrery.py consumes:
  from planet_visualization import (..., pluto_core_info, ...)

palomas_orrery_helpers.py imports but NEVER USES:
  from planet_visualization import (..., pluto_core_info, ...)
  # These ~87 imports are completely dead code
```

### Tooltip wiring — three paths (all must be updated)

**Path A — Earth inline (11 calls, lines ~8021-8092):**
```python
CreateToolTip(earth_inner_core_checkbutton, earth_inner_core_info)
```
Earth bypasses `build_shell_checkboxes` (special "Earth System
Visualization" case). These 11 `_info` references are by name.

**Path B — most planets, dynamic via `globals()` (78 tooltips):**
```python
# palomas_orrery.py line ~8004:
build_shell_checkboxes('Mercury', celestial_frame, globals(), globals(), tk, CreateToolTip)

# celestial_objects.py line ~1482:
tooltip_name = f"{body_prefix}_{shell['var_suffix']}_info"
tooltip_text = tooltips_dict.get(tooltip_name, "No information available")
```
The `_info` imports in `palomas_orrery.py` exist ONLY to put those
strings into `globals()`. A grep won't find named references — that's
why they look "unused." This is the critical wiring path.

**Path C — Sun and asteroid belts, direct import (lines ~209-246):**
```python
from solar_visualization_shells import (core_info, radiative_zone_info, ...)
from asteroid_belt_visualization_shells import (main_belt_info, ...)
```
Bypasses the `planet_visualization.py` re-export chain entirely.

### Dispatch chain in planet_visualization.py (lines 535-860)

```python
def create_celestial_body_visualization(fig, body_name, shell_vars,
                                        animate=False, frames=None,
                                        center_position=(0, 0, 0)):
    if body_name == 'Sun':
        # ~40 lines of if shell_name == 'core': create_sun_core_shell(...)
    elif body_name == 'Mercury':
        # ~20 lines
    elif body_name == 'Venus':
        # ~20 lines
    # ... repeat for all 14 bodies ...
    elif body_name == 'Planet 9':
        # ~10 lines
```

Each body's block does the same thing: check which shell checkboxes are
active, call the corresponding `create_*_shell()` function, add traces
to fig. The only variation is the function names and shell names.

### Shell function anatomy (typical sphere shell, post-Step-2)

Each sphere shell function follows this pattern:

```python
pluto_core_info = (
    "Pluto's core is believed to consist primarily of..."
)  # GUI tooltip — used by CreateToolTip

def create_pluto_core_shell(center_position=(0, 0, 0)):
    layer_info = {
        'name': 'Core',
        'radius_fraction': 0.52,
        'color': 'rgb(139, 90, 43)',
        'opacity': 1.0,
        'marker_size': 4.0,
        'description': (
            "Core: Pluto's core is believed..."  # hover text for 3D
        ),
    }
    # ~30 lines: compute radius in AU, generate sphere points,
    # create geometry trace with hoverinfo='skip',
    # create info marker at north pole with description,
    # return traces list
```

The data (`layer_info` dict) varies per shell. The code is identical
across all ~80 sphere shell functions. That's why it consolidates.

---

## Architecture design (from plotting consolidation handoff)

### shell_configs.py structure

```python
SHELL_CONFIGS = {
    'Mercury': {
        'inner_core': {
            'name': 'Inner Core',
            'radius_fraction': 0.41,
            'color': 'rgb(255, 180, 140)',
            'opacity': 1.0,
            'n_points': 25,
            'marker_size': 4.0,
            'hover_text': "Inner Core: Mercury has a very large...",
            'tooltip': "Inner Core: Mercury has a very large...\n...",
        },
        'outer_core': { ... },
        # ... all sphere shells for Mercury
    },
    'Pluto': { ... },
    # ... all bodies
}

CUSTOM_SHELLS = {
    'Mercury': {
        'sodium_tail': {
            'builder': 'mercury_visualization_shells.create_mercury_sodium_tail',
            'tooltip': "Mercury's sodium tail extends anti-sunward...",
        },
        'magnetosphere': {
            'builder': 'mercury_visualization_shells.create_mercury_magnetosphere_shell',
            'tooltip': "Mercury has a weak but detectable...",
        },
    },
    # ... all bodies with custom geometry
}
```

### build_sphere_shell() contract

```python
def build_sphere_shell(config, body_name, center_position=(0, 0, 0)):
    """Generic sphere shell from config dict.
    Enforces single-info-marker pattern and n_points defaults."""
    n = config.get('n_points', 20)
    # ... generate sphere geometry ...
    shell_trace = go.Scatter3d(
        ..., hoverinfo='skip', ...  # ALWAYS skip
    )
    info_trace = go.Scatter3d(
        x=[cx], y=[cy], z=[cz + r * 1.05],  # ALWAYS one marker
        marker=dict(symbol='cross', ...),
        text=[config['hover_text']],          # ALWAYS one copy
    )
    return [shell_trace, info_trace]
```

### Replacement dispatch (~20 lines replaces ~300, plus indicator de-duplication)

```python
def create_celestial_body_visualization(fig, body_name, shell_vars,
                                        center_position=(0, 0, 0),
                                        object_type=None, center_object=None):
    from orrery_rendering import build_sphere_shell
    from shell_configs import SHELL_CONFIGS, CUSTOM_SHELLS
    from shared_utilities import create_vernal_equinox_indicator

    configs = SHELL_CONFIGS.get(body_name, {})
    customs = CUSTOM_SHELLS.get(body_name, {})

    outermost_radius = 0
    for shell_name, var in shell_vars.items():
        if var.get() != 1:
            continue
        if shell_name in configs:
            traces = build_sphere_shell(
                configs[shell_name], body_name, center_position
            )
            outermost_radius = max(outermost_radius,
                configs[shell_name].get('radius_fraction', 0))
            for t in traces:
                fig.add_trace(t)
        elif shell_name in customs:
            custom = customs[shell_name]
            module_path, func_name = custom['builder'].rsplit('.', 1)
            import importlib
            mod = importlib.import_module(module_path)
            builder = getattr(mod, func_name)
            for t in builder(center_position):
                fig.add_trace(t)

    # ONE indicator per body (replaces ~50 per-shell calls)
    indicator = create_vernal_equinox_indicator(
        center_position, shell_radius=outermost_radius,
        object_type=object_type, center_object=center_object)
    for t in indicator:
        fig.add_trace(t)

    return fig
```

---

## What the manifest must contain

Structure the manifest in four phases. Each phase must leave the
codebase fully functional — Tony can pause between any two phases.

### Phase A: Infrastructure + Mercury POC

Create the new modules, prove the pattern on one body.

- `orrery_rendering.py` — create with `build_sphere_shell()`. Layout
  functions will be added in Step 4; for now it owns only the shell
  builder. Make this sequencing explicit.
- `shell_configs.py` — create with Mercury's 6 sphere shell configs
  (5 standard + crust converted from Mesh3d to standard sphere) plus
  Mercury's `CUSTOM_SHELLS` entries (sodium tail, magnetosphere).
  Note: Mercury atmosphere calls `create_sun_direction_indicator()`
  after the sphere traces — flag how to handle the add-on.
- Mercury's dispatch block in `planet_visualization.py` — replace with
  config-driven routing.
- Verification: Mercury visual comparison before/after.

### Phase B: Archivable bodies (Pluto, Planet 9, Eris, Moon)

All become sphere-only after Mesh3d crusts are converted to standard
sphere shells. Add configs (including crust as sphere config), remove
dispatch blocks, strip dead `fibonacci_sphere()` code. Shell files
become fully archivable. Clean stopping point.

### Phase C: Mixed bodies (Venus, Mars, Earth, Jupiter, Saturn, Uranus, Neptune)

Sphere configs migrate, custom geometry gets `CUSTOM_SHELLS` entries.
Largest phase, mechanically repetitive after Phase A proves the pattern.

### Phase D: Solar + asteroid belts + cleanup

- Sun (absolute radii in AU, not radius_fraction — the one structural
  variation in the config format).
- Asteroid belts (all custom geometry — registry entries only).
- Comets (all custom geometry — registry entries only).
- `_info` import chain cleanup across four files:
  - `palomas_orrery_helpers.py`: ~87 dead imports (lines ~53-158) — pure delete.
  - `planet_visualization.py`: remove re-export imports.
  - `palomas_orrery.py`: ~89 imports (lines ~100-164) — replace with
    one `from shell_configs import SHELL_CONFIGS, CUSTOM_SHELLS`.
  - `celestial_objects.py`: update `build_shell_checkboxes()` to read
    tooltips from `SHELL_CONFIGS`/`CUSTOM_SHELLS` instead of `globals()`.
- Three tooltip wiring paths must all be updated (see "Tooltip wiring"
  section below).

### Required content per phase

Following the pattern from MANIFEST_single_info_marker.md:

1. **Complete shell config extraction** — for every sphere shell function
   in the phase's scope, extract the exact `layer_info` dict values
   (radius_fraction, color, opacity, n_points, marker_size, description)
   and the `_info` tooltip string into the `SHELL_CONFIGS` format. This
   is a data migration — the values must be exact, not approximated.

2. **CUSTOM_SHELLS registry** — for every non-sphere function in scope,
   map the shell checkbox name to the `module.function` string for lazy
   import.

3. **build_sphere_shell() implementation** (Phase A only) — the complete
   function, handling all variations found across the 80+ sphere functions.
   Flag any sphere shells that don't fit the standard pattern.

4. **planet_visualization.py changes** — per-phase dispatch block
   replacements and import changes.

5. **CRLF verification** — confirm every file touched is LF. Flag any
   that have CRLF (should be none post-Step-2, but verify).

6. **Dead code cleanup + Mesh3d conversion** — strip the unreachable
   `fibonacci_sphere()` and associated `x_hover`/`y_hover`/`z_hover`
   locals from crust/cloud_layer functions. Convert Mesh3d crusts and
   cloud_layers to standard Scatter3d sphere shells handled by
   `build_sphere_shell()` (decision: Mesh3d flat-shading visual
   not worth preserving; see judgment calls section).

7. **Judgment calls flagged inline** — where the standard pattern doesn't
   fit cleanly, flag it for Tony's decision. Examples:
   - Solar shells have absolute radii (AU) not radius_fraction — how
     does the config handle both?
   - Any shell that uses non-standard marker placement

   **Pre-decided (do not re-open):**
   - Mesh3d crust/cloud_layer shells → convert to standard Scatter3d
     sphere shells via `build_sphere_shell()`. The Mesh3d flat-shading
     visual effect is not worth preserving. Strip the dead
     `fibonacci_sphere()` code as part of this conversion. This makes
     Pluto, Planet 9, Eris, and Moon fully archivable.
   - Vernal equinox indicator: rename + de-duplicate. The function
     `create_sun_direction_indicator()` is misnamed — it draws a +X
     reference direction (vernal equinox / First Point of Aries), not
     the Sun direction. (The Sun's direction would require date-dependent
     computation; shells are static geometry.) Currently every shell
     function calls it independently (~50 duplicate calls across all
     bodies, both sphere and custom). Consolidate to ONE call per body
     in the dispatch loop, after all shells are built. The function
     already self-suppresses based on `object_type` and `center_object`.
     Rename to `create_vernal_equinox_indicator()` in `shared_utilities.py`;
     remove all per-shell `sun_traces = create_sun_direction_indicator(...)`
     calls from every shell file. The dispatch loop passes scale from
     the outermost active shell. Net: ~50 call sites → 1, plus accurate
     naming.

8. **Verification plan** — how the implementing session confirms each
   body's migration is correct (syntax check, visual verification items).

---

## Constraints

- **ASCII only** in all Python files (no Unicode characters)
- **LF line endings** — all shell files were converted to LF in Step 2.
  Confirm every file touched in this refactor is LF. Flag any that
  reverted or were missed.
- **Python binary mode** (rb/wb) for all file writes
- **Bottom-up editing** when making multiple changes to a file
- **Credit line:** `Module updated: May 2026 with Anthropic's Claude Opus 4.7`
- **Don't redesign the architecture** — the shell_configs.py structure,
  build_sphere_shell contract, and CUSTOM_SHELLS registry are Tony's
  approved design. Refine details, don't rethink fundamentals.
- **Exact data extraction** — radius fractions, colors, opacity values
  must come from the actual source files, not from training memory.
  **Source of truth:** the uploaded files only. `/mnt/project/` may be
  a stale snapshot. If a value can't be confirmed from an uploaded file,
  flag it for Tony rather than guessing.
- **n_points precedence** — use the value from the current (uploaded)
  shell file. Fall back to 20 (boundary/atmosphere) or 25 (interior)
  only if the file doesn't specify. Step 2 tuned these per-shell.
- **Preserve `# Source:` citations** — shell modules carry inline source
  citations (e.g. `# Source: NASA MESSENGER; Sori (2018)`). When
  migrating data to `shell_configs.py`, carry these citations forward
  as comments above or alongside the config entries. The provenance
  audit (April 2026) verified all shell constants — don't lose that work.
- **Line references are approximate** — `palomas_orrery.py` is ~9,938
  lines and shifts between sessions. Use function/pattern grep rather
  than absolute line numbers when navigating.

---

## Files to audit

All 15 `*_visualization_shells.py` files plus:
- `planet_visualization.py` (dispatch chain + re-exports)
- `celestial_objects.py` (SHELL_DEFINITIONS dict, `build_shell_checkboxes()` — central tooltip wiring point, see tooltip wiring section below)
- `palomas_orrery.py` (import chain + CreateToolTip usage)
- `palomas_orrery_helpers.py` (dead import chain)
- `shared_utilities.py` (`create_sun_direction_indicator()` → rename + de-duplicate)
- `constants_new.py` (CENTER_BODY_RADII, KM_PER_AU)

---

## Workflow context

This manifest will be:
1. Reviewed by Claude Opus 4.6 + Tony (line-by-line editorial)
2. Returned to you (Opus 4.7) for finalization with feedback
3. Implemented by Claude Opus 4.6 + Tony using the finalized manifest

The manifest should be structured in four phases (A/B/C/D) with clear
boundaries so each phase can be implemented in a separate session without
context overflow. The info marker manifest (2,342 lines) hit context
limits during implementation — this refactor is larger, so phasing is
essential.

**Manifest sizing strategy:** Produce Phase A in full mechanical detail
(Mercury POC — complete before/after snippets, exact config blocks,
builder implementation). For Phases B/C/D, produce patterned outlines:
"follow the Mercury template for Pluto" with body-specific notes where
the pattern varies. The implementing Claude session will extract the
actual data values from the uploaded shell files. This keeps the total
manifest under ~1,500 lines and avoids carrying 80+ config blocks
verbatim through two review passes.

Tony will keep archived versions of existing files before each phase.

The single info marker manifest set the quality bar. That manifest was
executed mechanically with zero ambiguity. Aim for the same level of
precision here.

---

*Paloma's Orrery | palomasorrery.com*
*"Can we import some of this new code instead of adding more bloat?"*
— Tony, on the renderer refactor, April 13, 2026
