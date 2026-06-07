# Shell Consolidation Manifest Request

**To:** Claude Opus 4.7
**From:** Tony Quintanilla (integrator) + Claude Opus 4.6 (implementation partner)
**Date:** May 14, 2026
**Revision:** v3 — incorporates Opus 4.7 review feedback (dispatch chain
analysis, Sun unification, corrected tooltip counts, CRLF inventory,
naming convention caveat). Resolved by Tony + Opus 4.6.
v3: Phase B complete. Phase C sub-phased (C1-C4) by progressive
complexity. Satellites split to Phase E (creative/Mode 7). Pluto/Eris
collapsed into C1 with Venus/Mars. rotate_to_sunward() promoted in C1
with magnetic_tilt_deg + sun_position parameters.
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

3. **Replace the dispatch chain** in `planet_visualization.py` — retire
   both `create_planet_visualization()` (4 call sites) and
   `create_sun_visualization()` (2 call sites). The refactored
   `create_celestial_body_visualization()` becomes the single entry
   point for all bodies including Sun. The ~600-line if/elif routing
   across the three functions becomes ~20 lines: strip body prefix
   from shell_vars keys, look up config, call builder for sphere
   shells, lazy-import for custom geometry.

4. **Clean up the `_info` import chain** — ~89 imports in
   `palomas_orrery.py`, ~87 dead imports in `palomas_orrery_helpers.py`,
   re-exports in `planet_visualization.py`. Two tooltip wiring paths
   must be updated: inline CreateToolTip calls (Path A, ~33 sites
   across Earth, Sun, and asteroid belts) and dynamic `globals()`
   lookup via `build_shell_checkboxes` in `celestial_objects.py`
   (Path B, 78 tooltips). The Sun/asteroid direct imports (Path C)
   are consumed by Path A's inline calls and are deleted together.
   After migration, tooltips read from `SHELL_CONFIGS` and
   `CUSTOM_SHELLS` instead.

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

| Module | Lines | Role | Line endings |
|--------|------:|------|:------------:|
| planet_visualization.py | 1,164 | Dispatch routing + re-exports _info strings | CRLF (convert) |
| celestial_objects.py | ~1,490 | SHELL_DEFINITIONS dict + `build_shell_checkboxes()` — central tooltip wiring | LF |
| palomas_orrery.py | 9,938 | ~89 _info imports (lines ~100-164), consumed dynamically via `globals()` by `build_shell_checkboxes`, plus ~33 inline CreateToolTip calls (Earth 11, Sun 13, asteroids 4, heliosphere 5) | LF |
| palomas_orrery_helpers.py | 916 | ~87 _info imports (lines ~53-158), ALL DEAD — never consumed | CRLF (convert) |
| constants_new.py | 719 | CENTER_BODY_RADII dict (line 241), KM_PER_AU (line 47) | LF |
| shared_utilities.py | ~160 | `create_sun_direction_indicator()` — rename + de-duplicate target | LF |

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

### Tooltip wiring — two paths plus one import source (all must be updated)

**Path A — inline CreateToolTip calls (~33 sites, lines ~7870-8092):**
```python
CreateToolTip(earth_inner_core_checkbutton, earth_inner_core_info)
CreateToolTip(sun_core_checkbutton, core_info)
CreateToolTip(asteroid_belt_main_checkbutton, main_belt_info)
```
Earth (11 calls), Sun (13 calls), and asteroid belts (4 calls) all
bypass `build_shell_checkboxes` and wire tooltips inline by name.
Sun and asteroid belt `_info` strings are imported directly from their
shell files (Path C below), but the consumption pattern is the same
as Earth — inline `CreateToolTip(widget, name_info)` calls. After
migration, all ~33 read from `SHELL_CONFIGS`/`CUSTOM_SHELLS` instead
of imported `_info` variables.

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

**Path C — Sun and asteroid belt import source (lines ~209-246):**
```python
from solar_visualization_shells import (core_info, radiative_zone_info, ...)
from asteroid_belt_visualization_shells import (main_belt_info, ...)
```
These imports bypass the `planet_visualization.py` re-export chain.
The imported strings are consumed by the inline calls described in
Path A above. After migration, these imports are deleted along with
the Path A call sites — both are replaced by reads from configs.

### Dispatch chains in planet_visualization.py

There are TWO dispatch functions plus a Sun-specific function:

**`create_celestial_body_visualization()`** (line 535) — uses bare
shell keys (`'core'`, `'inner_core'`), iterates `shell_vars.items()`.
This matches the config-driven architecture. **But it has no actual
callers** — imported at line 101 of `palomas_orrery.py` and line 54
of helpers, but never called. Mercury block is also stale (missing
`sodium_tail`).

**`create_planet_visualization()`** (line 875) — uses prefixed keys
(`'mercury_inner_core'`), direct dict lookups. **This is what's
actually called** by `plot_objects` (lines ~4516, ~4605, ~4618) and
`animate_objects` (line ~6152).

**`create_sun_visualization()`** (line 301) — Sun-specific routing,
called at lines ~4509 and ~6144.

**Resolution (pre-decided):** Refactor `create_celestial_body_visualization`
as the unified config-driven entry point for ALL bodies including Sun.
Retire both `create_planet_visualization` and `create_sun_visualization`.
Redirect their 6 call sites (4 planet + 2 Sun) to the unified function.

The `shell_vars` dicts in `palomas_orrery.py` use prefixed keys
(e.g. `'mercury_inner_core'`). The dispatch function strips the body
prefix to match config keys:
```python
body_prefix = body_name.lower().replace(' ', '')  # 'Planet 9' -> 'planet9'
for key, var in shell_vars.items():
    shell_name = key.replace(f'{body_prefix}_', '', 1)  # 'mercury_inner_core' -> 'inner_core'
    ...
```

Sun shell_vars already use bare keys (`'core'`, `'radiative'`), so
the prefix strip is a no-op for Sun — no special casing needed.

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
    Enforces single-info-marker pattern and n_points defaults.
    Accepts either radius_fraction (planets) or radius_au (Sun)."""
    n = config.get('n_points', 20)
    # Radius: fraction of body radius, or absolute AU for Sun
    if 'radius_au' in config:
        r = config['radius_au']
    else:
        body_radius = CENTER_BODY_RADII[body_name] / KM_PER_AU
        r = body_radius * config['radius_fraction']
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

### Replacement dispatch (~20 lines replaces ~600, plus indicator de-duplication)

```python
def create_celestial_body_visualization(fig, body_name, shell_vars,
                                        center_position=(0, 0, 0),
                                        object_type=None, center_object=None):
    from orrery_rendering import build_sphere_shell
    from shell_configs import SHELL_CONFIGS, CUSTOM_SHELLS
    from shared_utilities import create_vernal_equinox_indicator

    configs = SHELL_CONFIGS.get(body_name, {})
    customs = CUSTOM_SHELLS.get(body_name, {})

    # Strip body prefix from shell_vars keys to match config keys
    # e.g. 'mercury_inner_core' -> 'inner_core'; Sun's bare keys pass through
    body_prefix = body_name.lower().replace(' ', '') + '_'
    
    outermost_radius = 0
    for key, var in shell_vars.items():
        if var.get() != 1:
            continue
        shell_name = key[len(body_prefix):] if key.startswith(body_prefix) else key
        if shell_name in configs:
            traces = build_sphere_shell(
                configs[shell_name], body_name, center_position
            )
            outermost_radius = max(outermost_radius,
                configs[shell_name].get('radius_fraction',
                configs[shell_name].get('radius_au', 0)))
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

### Phase B: Moon + Planet 9 (COMPLETE)

Moon (6 sphere shells) and Planet 9 (2 sphere shells) migrated to
unified dispatch. Mesh3d geometry type added for crusts/cloud layers.
Moon mantle radius/opacity swap corrected. n_points standardized.
Pluto and Eris deferred -- need satellite internal structure shells.

### Phase C: Mixed bodies (existing shells only)

Sphere configs migrate, custom geometry gets `CUSTOM_SHELLS` entries.
Satellite internal structure shells are deferred to Phase E (separate
creative/Mode 7 work stream). Phase C is pure mechanical refactoring
with verifiable before/after for every shell. Ordered by progressive
complexity -- each sub-phase introduces one new pattern.

**C1: Pluto + Eris + Venus + Mars** -- Pluto and Eris are sphere-only
(Phase-B-equivalent: configs + delegation, shell files archivable in
Phase D). Venus and Mars introduce the first `CUSTOM_SHELLS` entries
(magnetosphere/bow shock). Promote `rotate_to_sunward()` from Mercury-
local to `orrery_rendering.py` with `magnetic_tilt_deg=0` default and
`sun_position` parameter (resolves deferred item 6 for all future
bodies). Venus has no moons. Mars has Phobos and Deimos (satellite
shells deferred to Phase E).

**C2: Earth** -- most complex single body. 14 shell conversions: 6
standard sphere + crust + magnetosphere/bow shock + Van Allen belts
(loop geometry) + LEO + GEO (ring geometry) + Hill sphere. Stand-alone
because of the complexity. Benefits from C1 establishing the
magnetosphere CUSTOM_SHELLS pattern and `rotate_to_sunward()` signature.
Moon already migrated in Phase B.

**C3: Jupiter** -- first gas giant. Sphere shells + cloud_layer +
magnetosphere + Io torus + radiation belts + rings as `CUSTOM_SHELLS`.
Cloud_layer uses mesh3d geometry type. Galilean moon shells deferred
to Phase E.

**C4: Saturn, Uranus, Neptune** -- share ring/belt patterns from C3.
Saturn sphere shells + cloud_layer + magnetosphere + Enceladus torus +
radiation belts + tilted rings (`rotate_points`). Uranus at 97.77 deg
tilt (double `rotate_points`). Neptune with tilted rings + plasma.
Satellite shells (Titan, Enceladus, Triton, Miranda) deferred to
Phase E.

### Phase D: Solar + asteroid belts + cleanup

- Sun folds into the unified `create_celestial_body_visualization()`
  dispatch — one function handles all bodies. Sun configs use
  `radius_au` instead of `radius_fraction`; `build_sphere_shell()`
  checks which key is present and computes accordingly (see builder
  contract above). `create_sun_visualization()` is retired; its 2
  call sites (lines ~4509, ~6144) redirect to the unified function.
- Asteroid belts (all custom geometry — registry entries only).
- Comets (all custom geometry — registry entries only).
- `_info` import chain cleanup across four files:
  - `palomas_orrery_helpers.py`: ~87 dead imports (lines ~53-158) — pure delete.
  - `planet_visualization.py`: remove re-export imports.
  - `palomas_orrery.py`: ~89 imports (lines ~100-164) — replace with
    one `from shell_configs import SHELL_CONFIGS, CUSTOM_SHELLS`.
  - `celestial_objects.py`: update `build_shell_checkboxes()` to read
    tooltips from `SHELL_CONFIGS`/`CUSTOM_SHELLS` instead of `globals()`.
- Two tooltip wiring paths must be updated (see "Tooltip wiring"
  section above): Path A (~33 inline CreateToolTip calls) and
  Path B (`build_shell_checkboxes` globals lookup). Path C imports
  are deleted as part of Path A cleanup.
- Archive dead shell files: `moon_visualization_shells.py`,
  `planet9_visualization_shells.py`. Pluto and Eris shell files may
  also be archivable if their satellites' custom geometry (if any)
  is housed elsewhere.
- `sun_position` parameter: thread Sun's position through dispatch and
  custom geometry builders so body-centered views orient magnetospheres,
  tails, and the sun direction indicator correctly.
- Retire `create_planet_visualization()` and `create_sun_visualization()`.
- `palomas_orrery_helpers.py` CRLF -> LF.

### Phase E: Satellite internal structure shells (creative/Mode 7)

New `SHELL_CONFIGS` entries for major satellites, created alongside
their parent system. This is creative work (no "before" to compare
against) requiring Mode 7 literature review for interior structure
models. Even satellites with limited interior data get at minimum a
crust shell from known/estimated radius.

Each satellite requires new plumbing: `CENTER_BODY_RADII` entry,
`SHELL_DEFINITIONS` entry, GUI checkbox wiring (`tk.IntVar`s,
`build_shell_checkboxes` call), and the actual shell configs. Data
sourced from Horizons (physical radii) + literature (interior models).

Satellite candidates by system:
- Mars: Phobos, Deimos (crust-only from known radii)
- Pluto: Charon (full interior from New Horizons), Nix, Hydra,
  Kerberos, Styx (crust-only)
- Eris: Dysnomia (crust-only)
- Jupiter: Europa, Ganymede, Io, Callisto (all well-characterized)
- Saturn: Titan, Enceladus (both well-characterized)
- Uranus: possibly Miranda (limited data)
- Neptune: Triton (retrograde capture, nitrogen geysers)

Phase E can run in parallel with Phase D since they don't touch the
same code paths. Each major moon (Europa, Titan, etc.) could be its
own session given the scientific depth involved.

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
   - Any shell that uses non-standard marker placement

   **Pre-decided (do not re-open):**
   - Sun folds into unified dispatch. `build_sphere_shell()` accepts
     either `radius_fraction` (planets — multiplied by body radius) or
     `radius_au` (Sun — used directly). `create_sun_visualization()` is
     retired; its 2 call sites redirect to `create_celestial_body_visualization()`.
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
  reverted or were missed. Note: `planet_visualization.py` and
  `palomas_orrery_helpers.py` are still CRLF (they were not shell files
  and were not touched in Step 2). Convert them to LF as part of this
  refactor since both are heavily modified. Use Python binary mode for
  the conversion.
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
- **`_shell` in function names does not imply sphere geometry** — many
  custom-geometry functions are named `create_*_magnetosphere_shell()`
  or `create_*_bow_shock_shell()` even though they produce non-sphere
  geometry. The function body determines whether it belongs in
  `SHELL_CONFIGS` (sphere) or `CUSTOM_SHELLS` (custom geometry), not
  the name.

---

## Files to audit

All 15 `*_visualization_shells.py` files plus:
- `planet_visualization.py` (dispatch chain + re-exports)
- `celestial_objects.py` (SHELL_DEFINITIONS dict, `build_shell_checkboxes()` — central tooltip wiring point, see tooltip wiring section above)
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
