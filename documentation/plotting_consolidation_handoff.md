# Plotting Consolidation Handoff

## Paloma's Orrery | May 12, 2026 | Claude Opus 4.6

-----

## Purpose

This document maps the complete plotting pipeline in palomas_orrery.py,
identifies every function shared between plot_objects and animate_objects,
catalogs their divergences, and lays out a phased consolidation plan.
Companion to the Architecture & Maintainability Session handoff (April 13,
2026). This is a design document -- no code ships with it.

### Design Principles

1. **Architectural simplicity**: fewer modules where it makes sense.
   One new module, not two. Data consolidation into one config file.
2. **Memory efficiency**: the single-info-marker pattern and reduced
   n_points from the solar shell refactor (v3.18) become structural
   defaults, not conventions to remember.

-----

## The Problem

`plot_objects()` (lines 3605-5445) and `animate_objects()` (lines 5446-7163)
are two ~1,800-line functions that independently implement the same pipeline:

```
Setup -> Fetch -> Build Traces -> Layout -> Finalize -> Show
```

They diverged when animate_objects was created and have been maintained
independently since. Every session that touches one risks missing the other.
This is the project's dominant bug class.

Known active divergences (as of April 14, 2026):

| What | plot_objects | animate_objects |
|------|-------------|-----------------|
| Website links | GitHub Page + Web Site (2 annotations) | Missing both |
| NASA link text | "NASA" | "Search: NASA" |
| Coordinate box | Refined exoplanet sub-bullets with indents | Flat ternary, no sub-bullets |
| Coordinate box y position | y=0.80 | y=0.7 |
| dtick on axes | Not set (Plotly default) | Not set (Plotly default) |
| Finishing step order | URL, camera, flyto, comet tails, show | Hover toggle, camera, flyto, URL, show |
| Hover toggle call location | Line 4485 (inside trace building) | Line 7127 (in finalization) |

-----

## Pipeline Anatomy

### Phase 1: Setup (Ring 3 -- hardest to unify)

Both pipelines do nearly identical center-body detection, osculating element
pre-fetch, SKIP list construction, and exoplanet mode detection. The first
~80 lines of each are near word-for-word identical.

**plot_objects setup** (lines 3609-3830):

| Step | What | Lines |
|------|------|-------|
| Osculating pre-fetch | Build active_planetary_params from Horizons | 3609-3720 |
| Center body detection | center_object_name, center_id, center_id_type | 3617-3832 |
| SKIP list | SKIP_HORIZONS_PREFETCH list for TNO moons | 3650 |
| Exoplanet mode detect | is_exoplanet_mode flag | 3753 |
| Date/interval setup | get_date_from_gui, get_interval_settings | 3774-3800 |

**animate_objects setup** (lines 5452-5595, approximate):

| Step | What |
|------|------|
| Osculating pre-fetch | Same pattern, same SKIP list |
| Center body detection | Same pattern |
| Date/frame setup | create_animation_dates (different from plot) |
| Exoplanet mode detect | Same pattern |

These are candidates for `render_context.py` (Option C from architecture
session) but are NOT part of Ring 1. Documented here for completeness.

### Phase 2: Trace Building (Ring 3 -- genuinely different)

This is where the pipelines legitimately differ. plot_objects builds one
set of traces for a single date. animate_objects builds initial traces plus
N frames with per-frame position updates.

Shared trace-building functions (called by both):

| Function | Module | What it does |
|----------|--------|--------------|
| create_celestial_body_visualization() | planet_visualization.py | Shell traces for any body |
| create_planet_visualization() | planet_visualization.py | Planet-specific shell routing |
| create_sun_visualization() | planet_visualization.py | Sun shell routing |
| create_sun_corona_from_distance() | planet_visualization.py | Distance-positioned corona |
| plot_idealized_orbits() | idealized_orbits.py | Keplerian orbit ellipses |
| add_comet_tails_to_figure() | comet_visualization_shells.py | Ion + dust tail traces |
| format_detailed_hover_text() | visualization_utils.py | Full hover string builder |
| add_celestial_sphere_traces() | star_sphere_builder.py | Stars + grid (already unified!) |

Functions called only by plot_objects:

| Function | Module | Why animate doesn't call it |
|----------|--------|-----------------------------|
| _add_close_approach_extras() | palomas_orrery.py | CAD perigee + hyperbolic osc (static only) |
| _add_perihelion_osculating_orbit() | palomas_orrery.py | Perihelion osc arcs (static only) |
| _add_spacecraft_encounter_markers() | palomas_orrery.py | Tagged encounter markers (static only) |
| plot_exoplanet_orbits() | exoplanet_orbits.py | Exoplanet system rendering |
| plot_binary_host_stars() | exoplanet_orbits.py | Binary star visualization |

These are legitimately static-only features. Not candidates for unification.

### Phase 3: Layout (Ring 1 -- extract first)

Both pipelines call `fig.update_layout()` with a large dict containing
scene axes, colors, title, legend, margins, and annotations. This is where
the divergences listed above live. The layout dict is ~150 lines in each
pipeline and structurally identical.

**What goes into build_orrery_layout():**

```
Inputs:
    axis_range          -- [min, max] AU
    title_text          -- formatted title string
    is_exoplanet_mode   -- bool (changes coordinate box text)
    is_animation        -- bool (adds Play/Pause updatemenus)

Returns:
    Complete dict for fig.update_layout()

Contains:
    Scene dict:
        xaxis, yaxis, zaxis (range, dtick, background, grid, title)
        aspectmode, camera, domain
    Colors: paper_bgcolor, plot_bgcolor, title_font_color, font_color
    Title: title_text
    Legend: font, position, anchor
    Margins: l=75, r=50, t=80, b=50
    Annotations list:
        Coordinate system box (exoplanet-aware)
        "Paloma's Orrery GitHub Page" link
        "Paloma's Orrery Web Site" link
        "JPL Horizons" link
        "NASA" link
        Legend instruction text
    Updatemenus (animation only):
        Play/Pause buttons
```

**3D axis improvements land here:**

```python
def _build_scene_axes(axis_range):
    """Build scene axis dicts with auto-calculated dtick."""
    from visualization_utils import _calculate_grid_dtick

    span = axis_range[1] - axis_range[0]
    dtick = _calculate_grid_dtick(span)

    # Scale-aware title suffix
    dtick_km = dtick * 149597870.7
    suffix = ""
    if dtick < 0.01:
        suffix = f" (grid: {dtick_km:,.0f} km)"
    elif dtick < 0.1:
        suffix = f" (grid: {dtick_km / 1e6:.1f}M km)"

    template = dict(
        range=list(axis_range), dtick=dtick,
        backgroundcolor='black', gridcolor='gray',
        showbackground=True, showgrid=True
    )
    return {
        'xaxis': {**template, 'title': f'X (AU){suffix}'},
        'yaxis': {**template, 'title': f'Y (AU){suffix}'},
        'zaxis': {**template, 'title': f'Z (AU){suffix}'},
    }
```

Written once. Both pipelines get readable grids at every scale. Studio
override still works on top (operates on exported HTML, not this function).

### Phase 4: Finalization (Ring 2 -- extract second)

After the layout is set, both pipelines call the same finishing functions
in slightly different order. This is the second extraction target.

**plot_objects finishing sequence** (lines 5351-5417):

```
1. add_url_buttons(fig, objects, selected_objects)
2. add_look_at_object_buttons(fig, positions, center_object_name)
3. add_fly_to_object_buttons(fig, positions, center_object_name)
4. [comet tails loop]
5. show_figure_safely(fig, default_name)
6. Store _last_plotted_fig, _last_plot_name
```

Note: add_hover_toggle_buttons is called earlier (line 4485) inside the
trace-building section, not in finalization.

**animate_objects finishing sequence** (lines 7127-7145):

```
1. add_hover_toggle_buttons(fig)
2. add_look_at_object_buttons(fig, initial_positions, center_object_name)
3. add_fly_to_object_buttons(fig, initial_positions, center_object_name)
4. add_url_buttons(fig, objects, selected_objects)
5. show_animation_safely(fig, default_name)
6. Store _last_plotted_fig, _last_plot_name
```

**Proposed finalize_orrery_figure():**

```
Inputs:
    fig, positions, center_object_name, objects,
    selected_objects, is_animation

Sequence (canonical order):
    1. add_hover_toggle_buttons(fig)
    2. add_look_at_object_buttons(fig, positions, center_object_name)
    3. add_fly_to_object_buttons(fig, positions, center_object_name)
    4. add_url_buttons(fig, objects, selected_objects)
    5. return fig   (caller handles show/save)
```

Comet tails stay outside -- they're trace-building, not finalization.
The hover toggle call in plot_objects (line 4485) should move to
finalization for consistency.

**Where these functions live today:**

| Function | Current home | Stays or moves? |
|----------|-------------|-----------------|
| add_hover_toggle_buttons() | visualization_utils.py | Stays, called from new module |
| add_camera_center_button() | visualization_utils.py | Stays, called from new module |
| add_look_at_object_buttons() | visualization_utils.py | Stays, called from new module |
| add_fly_to_object_buttons() | visualization_utils.py | Stays, called from new module |
| _calculate_grid_dtick() | visualization_utils.py | Stays, imported by new module |
| add_url_buttons() | palomas_orrery_helpers.py | Stays, called from new module |
| get_default_camera() | palomas_orrery_helpers.py | Stays, imported by new module |
| show_figure_safely() | shutdown_handler.py | Stays, caller's responsibility |
| show_animation_safely() | palomas_orrery_helpers.py | Stays, caller's responsibility |

Nothing moves. The new module imports and orchestrates.

-----

## One New Module: orrery_rendering.py

### Why one module, not two

The original plan proposed `orrery_layout.py` (~200 lines) and
`shell_builder.py` (~100 lines). But both answer the same question:
"what does the visual output look like?" Layout handles figure-level
presentation; the shell builder handles trace-level geometry. Same
concern, different scale. One ~300-line module is simpler to find,
simpler to import, and one fewer file in an 80+ module codebase.

Contrast with `star_sphere_builder.py`, which justifiably owns an
entire subsystem (JSON cache, file I/O, build, load, render).
The generic shell builder is one function consuming config dicts --
it doesn't warrant its own file.

### What it owns

```python
# orrery_rendering.py
#
# ROLE: Rendering contract between plot_objects and animate_objects
# CONSUMERS: palomas_orrery.py (plot_objects, animate_objects)
# DEPENDS ON: visualization_utils.py, palomas_orrery_helpers.py

# --- Layout ---
def build_orrery_layout(axis_range, title_text, is_exoplanet_mode,
                        is_animation=False):
    """Single authoritative layout dict for all orrery figures."""

def _build_scene_axes(axis_range):
    """Axis dicts with auto-dtick and scale-aware titles."""

def _build_annotations(is_exoplanet_mode):
    """Canonical annotation list (coordinate box, links, legend hint)."""

# --- Finalization ---
def finalize_orrery_figure(fig, positions, center_object_name,
                           objects, selected_objects):
    """Post-layout checklist: hover toggle, camera, flyto, URL buttons."""

# --- Shell Builder ---
def build_sphere_shell(config, body_name, center_position=(0, 0, 0)):
    """Generic efficient sphere shell from config dict.
    Enforces single-info-marker pattern and n_points=20 by default."""
```

### What it does NOT own

- Data fetching (stays in palomas_orrery.py / helpers)
- Trace building (stays in respective modules)
- GUI state reading (caller passes values, not tk variables)
- File save/show (caller's responsibility)
- Custom geometry (magnetospheres, rings, tails, toruses, belts)
- Shell config data (lives in shell_configs.py)

### How it differs from palomas_orrery_helpers.py

| | palomas_orrery_helpers.py | orrery_rendering.py |
|---|--------------------------|---------------------|
| Organizing principle | "Stuff pulled out of the monolith" | "Contract between two pipelines" |
| Contents | Trajectory fetch, orbit backup, camera, URL buttons, Planet 9 | Layout, annotations, finalization, shell builder |
| Purpose | Reduce file size | Eliminate a bug class + enforce efficiency |
| Dependencies | astroquery, plotly, orbit_data_manager, idealized_orbits, 105 _info imports | visualization_utils (dtick), plotly (types only) |
| Who calls it | palomas_orrery.py only | Both plot_objects AND animate_objects |

-----

## One Config File: shell_configs.py

### Why one file for all bodies

Currently 15 separate shell files define the same data (radius, color,
opacity, hover text) in 15 different places using 15 copies of the same
code pattern. The data is what varies per body -- the code is identical.

One config file means:

- Adding a new body (Charon, Titan, Enceladus, Ceres) is adding a dict
  entry, not creating a new module
- All shell parameters are visible in one place for comparison
- GUI tooltip text (_info strings) lives with the data it describes
- The 105-line _info import chain in palomas_orrery.py disappears

### Structure

```python
"""
Shell configuration data for all celestial bodies.

Config dicts are consumed by build_sphere_shell() in orrery_rendering.py.
Custom geometry shells (magnetospheres, rings, tails, belts) keep their
functions in their original files -- only sphere shells are config-driven.

To add a new body (e.g., Charon, Titan):
    1. Add its radius to CENTER_BODY_RADII in constants_new.py
    2. Add its shell configs to SHELL_CONFIGS below
    3. Add checkbox vars in palomas_orrery.py GUI section
    4. The builder handles everything else
"""

from constants_new import CENTER_BODY_RADII, KM_PER_AU

def _radius_au(body_name):
    """Get body radius in AU from the constants table."""
    return CENTER_BODY_RADII[body_name] / KM_PER_AU


SHELL_CONFIGS = {

    'Mercury': {
        'inner_core': {
            'name': 'Inner Core',
            'radius_fraction': 0.41,
            'color': 'rgb(255, 180, 140)',
            'opacity': 1.0,
            'n_points': 25,              # Solid interior
            'marker_size': 4.0,
            'hover_text': (
                "Inner Core: Mercury has a very large metallic "
                "core...<br>"
                "Estimated ~1,000 km thick (Messenger, 2019)."
            ),
            'tooltip': (
                "Inner Core: Mercury has a very large metallic "
                "core.\nEstimated ~1,000 km thick (Messenger, 2019)."
            ),
        },
        'outer_core': { ... },
        'mantle': { ... },
        'crust': { ... },
        'hill_sphere': {
            'name': 'Hill Sphere',
            'radius_fraction': 89,       # 89 body radii
            'color': 'rgb(100, 100, 255)',
            'opacity': 0.15,
            'n_points': 20,              # Outer boundary
            'marker_size': 3.0,
            'hover_text': "...",
            'tooltip': "SET MANUAL SCALE TO AT LEAST 0.005 AU...",
        },
    },

    'Pluto': {
        'core': { ... },
        'mantle': { ... },
        'crust': { ... },
        'haze_layer': { ... },
        'atmosphere': { ... },
        'hill_sphere': { ... },
    },
    # Pluto has no custom geometry -- fully config-driven

    'Sun': {
        'core': {
            'name': 'Core',
            'radius_au': 0.00093,        # Absolute, not fraction
            'color': 'rgb(255, 200, 50)',
            'opacity': 1.0,
            'n_points': 25,
            'marker_size': 4.0,
            'hover_text': "...",
            'tooltip': "...",
        },
        # ... through gravitational_influence (14 sphere shells)
    },

    # Future bodies -- add entries here
    # 'Charon': { ... },
    # 'Titan': { ... },
    # 'Enceladus': { ... },
    # 'Ceres': { ... },
}


# ============================================================
# CUSTOM_SHELLS: geometry that doesn't fit the sphere builder
# ============================================================
# Maps body_name -> shell_name -> 'module.function' string.
# Lazy-imported at render time (addresses startup lag).

CUSTOM_SHELLS = {
    'Mercury': {
        'atmosphere': 'mercury_visualization_shells.create_mercury_atmosphere_shell',
        'sodium_tail': 'mercury_visualization_shells.create_mercury_sodium_tail',
        'magnetosphere': 'mercury_visualization_shells.create_mercury_magnetosphere_shell',
    },
    'Venus': {
        'atmosphere': 'venus_visualization_shells.create_venus_atmosphere_shell',
        'upper_atmosphere': 'venus_visualization_shells.create_venus_upper_atmosphere_shell',
        'magnetosphere': 'venus_visualization_shells.create_venus_magnetosphere_shell',
    },
    'Earth': {
        'magnetosphere': 'earth_visualization_shells.create_earth_magnetosphere_shell',
        'leo': 'earth_visualization_shells.create_earth_leo_shell',
        'geostationary_belt': 'earth_visualization_shells.create_earth_geostationary_belt_shell',
    },
    'Mars': {
        'magnetosphere': 'mars_visualization_shells.create_mars_magnetosphere_shell',
    },
    'Jupiter': {
        'ring_system': 'jupiter_visualization_shells.create_jupiter_ring_system',
        'radiation_belts': 'jupiter_visualization_shells.create_jupiter_radiation_belts',
        'io_plasma_torus': 'jupiter_visualization_shells.create_jupiter_io_plasma_torus',
        'magnetosphere': 'jupiter_visualization_shells.create_jupiter_magnetosphere',
    },
    'Saturn': {
        'ring_system': 'saturn_visualization_shells.create_saturn_ring_system',
        'radiation_belts': 'saturn_visualization_shells.create_saturn_radiation_belts',
        'magnetosphere': 'saturn_visualization_shells.create_saturn_magnetosphere',
    },
    'Uranus': {
        'ring_system': 'uranus_visualization_shells.create_uranus_ring_system',
        'radiation_belts': 'uranus_visualization_shells.create_uranus_radiation_belts',
        'magnetosphere': 'uranus_visualization_shells.create_uranus_magnetosphere',
    },
    'Neptune': {
        'ring_system': 'neptune_visualization_shells.create_neptune_ring_system',
        'radiation_belts': 'neptune_visualization_shells.create_neptune_radiation_belts',
        'magnetosphere': 'neptune_visualization_shells.create_neptune_magnetosphere',
    },
    'Sun': {
        'hills_cloud_torus': 'solar_visualization_shells.create_sun_hills_cloud_torus',
        'outer_oort_clumpy': 'solar_visualization_shells.create_sun_outer_oort_clumpy',
        'galactic_tide': 'solar_visualization_shells.create_sun_galactic_tide',
    },
    # Asteroid belts are handled separately (not per-body shells)
    # Comet tails are handled separately (per-object, not per-body)
}
```

### What This Replaces

**The if/elif dispatch chain in planet_visualization.py** (lines 562-870+):

Currently ~340 lines of:
```python
if body_name == 'Mercury':
    if shell_name == 'inner_core':
        traces.extend(create_mercury_inner_core_shell(center_position))
    elif shell_name == 'outer_core':
        ...
elif body_name == 'Venus':
    ...
```

Becomes:
```python
def create_celestial_body_visualization(fig, body_name, shell_vars,
                                         center_position=(0, 0, 0)):
    from orrery_rendering import build_sphere_shell
    from shell_configs import SHELL_CONFIGS, CUSTOM_SHELLS

    configs = SHELL_CONFIGS.get(body_name, {})
    customs = CUSTOM_SHELLS.get(body_name, {})

    for shell_name, var in shell_vars.items():
        if var.get() != 1:
            continue

        if shell_name in configs:
            traces = build_sphere_shell(
                configs[shell_name], body_name, center_position
            )
            for t in traces:
                fig.add_trace(t)

        elif shell_name in customs:
            # Lazy import + call
            module_path, func_name = customs[shell_name].rsplit('.', 1)
            import importlib
            mod = importlib.import_module(module_path)
            builder = getattr(mod, func_name)
            for t in builder(center_position):
                fig.add_trace(t)

    return fig
```

~20 lines replaces ~340 lines. Lazy import of custom shell modules
also addresses startup lag (architecture session Lever 2).

**The 105 _info string import chain:**

Currently: shell files export _info strings -> planet_visualization.py
re-exports -> palomas_orrery.py imports 105 -> palomas_orrery_helpers.py
imports another 105 -> used as GUI tooltip text.

With config: tooltip text is the 'tooltip' field in SHELL_CONFIGS.
GUI reads directly from config:

```python
tooltip_text = SHELL_CONFIGS['Mercury']['inner_core']['tooltip']
```

~210 lines of imports across two files disappear.

-----

## Memory Efficiency: The Numbers

### Per-Shell Savings

Old pattern (n_points=50): 2,500 geometry points, each carrying full
hover text (~250 chars). New pattern (n_points=20): 400 geometry points
(no text) + 1 info marker (text once).

| Component | Old pattern | New pattern | Savings |
|-----------|-------------|-------------|---------|
| Geometry points | 2,500 x,y,z | 400 x,y,z | 84% |
| Hover text | 2,500 copies (~625 KB) | 1 copy (~250 bytes) | 99.96% |
| customdata | 2,500 copies | 1 copy | 99.96% |
| Info marker | N/A | 1 point + text | +negligible |

### Plot-Level Savings

Earth with 7 sphere shells visible:
- Old: 17,500 points + 17,500 text copies = ~4.4 MB hover text
- New: 2,800 points + 7 text copies = ~1.8 KB hover text

Jupiter with 5 sphere shells visible:
- Old: 12,500 points + 12,500 text copies = ~3.1 MB hover text
- New: 2,000 points + 5 text copies = ~1.3 KB hover text

Solar shells already demonstrated: 45 MB -> 3.5 MB (v3.18).

### Structural Enforcement

```python
def build_sphere_shell(config, body_name, center_position=(0, 0, 0)):
    n = config.get('n_points', 20)          # Default 20, not 50
    # ... geometry ...
    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        hoverinfo='skip',                    # Always skip
        ...
    )
    info_trace = go.Scatter3d(
        x=[cx], y=[cy], z=[cz + r * 1.05],  # Always one marker
        marker=dict(symbol='cross', ...),
        text=[config['hover_text']],          # Always one copy
        ...
    )
    return [shell_trace, info_trace]
```

You cannot create a shell with 2,500 copies of hover text because
the function doesn't offer that option. The single-info-marker pattern
becomes structural, not a convention to remember.

-----

## Existing Unified Functions (Already Done Right)

| Function | Module | Unified when |
|----------|--------|-------------|
| add_celestial_sphere_traces() | star_sphere_builder.py | v3.19 (renderer refactor) |
| format_detailed_hover_text() | visualization_utils.py | Original design |
| add_hover_toggle_buttons() | visualization_utils.py | Original design |
| add_look_at_object_buttons() | visualization_utils.py | Original design |
| add_fly_to_object_buttons() | visualization_utils.py | Original design |
| plot_idealized_orbits() | idealized_orbits.py | Original design |
| _calculate_grid_dtick() | visualization_utils.py | v3.11 |

The star_sphere_builder.py refactor (v3.19) is the direct precedent.

-----

## Implementation Plan (SUPERSEDED -- see Revised Implementation Order below)

*The session ordering below was the original plan from April 14. It has
been replaced by the Revised Implementation Order (April 19) which starts
with measurable wins rather than the riskiest structural change. The
session content descriptions remain accurate as design reference.*

### Session A: orrery_rendering.py -- Layout + 3D Auto-Dtick

**Scope:** Create module with layout functions. Wire into both pipelines.

1. Create orrery_rendering.py with build_orrery_layout(), _build_scene_axes(),
   _build_annotations()
2. plot_objects calls it (replacing inline layout dict)
3. Reconcile annotation differences (add missing links, adopt better text)
4. animate_objects calls the same function
5. Visual verification + agentic pre-test

**Deliverables:** orrery_rendering.py (new), palomas_orrery.py (modified)
**Risk:** Low. Pure data extraction.
**Payoff:** Auto-dtick everywhere. Website links in animations. Coordinate
box unified. Annotation divergence eliminated permanently.

### Session B: Finalization Sequence

**Scope:** Add finalize_orrery_figure() to orrery_rendering.py.

1. Move hover toggle call in plot_objects to finalization
2. Establish canonical call order
3. Both pipelines call finalize_orrery_figure()
4. Visual verification

**Risk:** Low-medium. Call order might affect button positions.

### Session C: shell_configs.py + build_sphere_shell() + Mercury POC

**Scope:** Create config file. Add builder to orrery_rendering.py.
Convert Mercury's 5 sphere shells. Verify visual + file size.

1. Create shell_configs.py with Mercury sphere configs
2. Add build_sphere_shell() to orrery_rendering.py
3. Update planet_visualization.py routing for Mercury
4. Keep sodium tail + magnetosphere as custom entries
5. Visual verification + file size comparison

**Risk:** Medium. Must verify geometry matches + size improves.

### Session D+: Shell Migration (Incremental)

One planet per session, adding to shell_configs.py.
Order: Pluto (all spheres) -> Moon -> Planet 9 -> Eris ->
Venus -> Mars -> Jupiter -> Saturn -> Uranus -> Neptune ->
Solar -> Earth.

Simplest first. Bodies with zero custom geometry (Pluto, Planet 9)
have their shell files fully archivable after migration.

### Session E: _info Import Chain Cleanup

After all sphere shells migrated:
- Remove _info exports from shell files
- Remove ~105 _info imports from palomas_orrery.py
- Remove ~105 _info imports from palomas_orrery_helpers.py
- GUI reads 'tooltip' from SHELL_CONFIGS directly
- Startup lag improves (shell files no longer eagerly imported)

### Session F: Ring 3 -- Render Context (When Ready)

Extract shared setup logic. Not scheduled. Deserves its own planning.

-----

## File Impact Summary

| File | Current lines | After consolidation |
|------|--------------|---------------------|
| palomas_orrery.py | 9,938 | -~300 (layout) -~210 (_info imports) |
| palomas_orrery_helpers.py | 916 | -~105 (_info imports) |
| planet_visualization.py | 1,164 | -~340 (if/elif -> ~20 lines) |
| orrery_rendering.py | 0 (new) | ~300 |
| shell_configs.py | 0 (new) | ~600 |
| mercury_visualization_shells.py | 752 | ~250 (custom only) |
| pluto_visualization_shells.py | 537 | 0 (archivable) |
| planet9_visualization_shells.py | 267 | 0 (archivable) |
| moon_visualization_shells.py | 496 | ~60 (if any custom; Moon may be archivable) |
| save_utils.py | 893 | No change (Object Encyclopedia added May 2026) |
| idealized_orbits.py | 7,370 | Category 2 satellite markers (deferred) |

**Net module count change:** +2 new, eventually -2 to -5 archivable.

-----

## Decision Log

| Question | Decision | Rationale |
|----------|----------|-----------|
| One module or two? | One: orrery_rendering.py | Same concern (visual output). Fewer files. |
| Separate config file? | Yes: shell_configs.py | Data vs code. Different change frequency. |
| One config or per-planet? | One file, all bodies | See all parameters together. One place to add new bodies. |
| Where do tooltips go? | 'tooltip' field in config | Eliminates 210-line import chain. Data with data. |
| Default n_points? | 20 outer, 25 inner | Matches solar refactor. 84% point reduction. |
| Enforce info marker? | Structurally | Builder only produces skip+cross. Cannot create N hover copies. |
| Custom shell registry? | CUSTOM_SHELLS dict, lazy import | Extensible. Addresses startup lag. No if/elif chain. |
| Migration order? | Simplest -> most complex | Pluto/Moon first (archivable). Earth last (3 custom types). |
| Full pipeline unification? | Deferred | Ring 1+2 first. Ring 3 deserves own session. |

-----

## Developer Tools Foundation (April 14, 2026)

Before starting the plotting consolidation, the following tools were
built to give Tony visibility into the codebase:

- **module_atlas.py** generates MODULE_ATLAS.md -- 99 modules, 785
  functions, 86K lines mapped with docstrings, public functions,
  bidirectional dependencies, and role tags. Upload to Claude sessions
  as a prompt artifact for codebase-aware conversation.
- **add_docstrings.py** batch-inserted standardized module docstrings
  across 42 modules that were missing or had thin descriptions.
- **dep_trace.py** updated to import role classifications from
  module_atlas.py (single source of truth) and show module descriptions
  in the interactive HTML graph on click.
- **Module Docstring Standard** formalized in protocol v3.20.

These tools exist so Tony can follow along as Claude works through
the consolidation sessions. "You have a perfect grip. My grip is ...
difficult." The atlas is the shared reference that closes that gap.

-----

*"Can we import some of this new code instead of adding more bloat?"*
-- Tony, on the renderer refactor, April 13, 2026

*"You and me are doing the work of seven programmers."*
-- Tony, April 13, 2026

*Module updated: May 2026 with Anthropic's Claude Opus 4.6*

-----

## Idealized Orbit Hover Bloat (April 16, 2026)

**Discovered during gallery link icon work.** Mercury-only static plot
was 442 KB. Root cause: `idealized_orbits.py` duplicates the full
perturbation description (text + customdata) on every orbit point.

**Quantified impact (Mercury only, 2 orbit traces):**

| Field | Per point | Points | Total |
|-------|-----------|--------|-------|
| text (Keplerian) | 521 chars | 360 | 189 KB |
| customdata (Keplerian) | ~600 chars (JSON struct) | 360 | ~200 KB |
| text (Mean) | ~260 chars | 360 | ~95 KB |
| customdata (Mean) | ~300 chars (JSON struct) | 360 | ~100 KB |

**Per planet:** ~300 KB of hover text bloat (text + customdata combined).
**8-planet solar system:** ~2.4 MB of pure bloat, hidden in multi-MB files.

**This is NOT new behavior.** The bloat has been there since idealized
orbits were added. It was invisible at full-system scale. The Mercury-only
test plot made it visible (bloat = 98% of file size).

**Fix: Single info marker pattern (established v3.18)**

Apply to `idealized_orbits.py`:
- Geometry traces (Keplerian/Mean orbit lines): `hoverinfo='skip'`,
  no text, no customdata on the 360 line points
- One cross (+) marker at a representative orbit position (e.g., the
  point opposite perihelion for visual clarity) carrying the full hover
  text exactly once

This is the same pattern already applied to solar shells and the MAPS
ghost tail. The fix belongs in Ring 2 of the plotting consolidation
(idealized orbit refactor) since `idealized_orbits.py` is one of the
modules being restructured.

**Also applies to:** Actual orbit traces in `palomas_orrery.py`
(`plot_objects` and `animate_objects`). These have simpler hover text
("Mercury Orbit" repeated 51 times) -- less bloat per point but same
pattern violation. Should be `hoverinfo='skip'` with one info marker.

**Priority:** Medium. Not a regression, but a quality-of-life fix that
reduces every gallery JSON proportionally. Fix during Ring 2 work.

## Session 0: Single Info Markers for Orbit Traces (April 19, 2026)

**Completed.** Applied single info marker pattern to all Category 1
orbit traces. Mercury-only plot dropped from 442 KB to 71 KB (84%
reduction). 8-planet savings estimated ~2.4 MB.

### Files Modified

**idealized_orbits.py** (3 traces converted):
- Mean orbit (`add_mean_orbit_trace`): white cross at midpoint,
  `legendgroup`, `visible='legendonly'` on both traces
- Elliptical Keplerian orbit (`plot_idealized_orbits`): planet-color
  cross at index `len//4` (90 deg past perihelion, clear of apsidal
  markers)
- Hyperbolic Keplerian orbit (`plot_idealized_orbits`): planet-color
  cross at midpoint of arc

**palomas_orrery.py** (4 traces converted):
- Cached orbit paths (pre-loaded from orbit_paths.json)
- Special fetch actual orbits (`plot_actual_orbits`, special path)
- Normal mode actual orbits (`plot_actual_orbits`, normal path) --
  Orcus/Vanth detailed hover preserved on single marker
- Plotted Period trajectory (yellow trace, `plot_objects`)
- Full Mission trajectory (`animate_objects`)

**save_utils.py** (4 text updates + 2 fixes):
- Dialog radio button: "~10 KB" to "~10 KB + plot data"
- `wraplength=280` on both HTML radio buttons
- Window height 200 to 230 (buttons no longer truncated)
- `tk.StringVar(master=format_window, ...)` fixes default selection
  (only top radio button selected on open)
- Docstring and console print updated to match
- Credit line added

### Info Marker Standard (Established)

```python
marker=dict(size=8, color=trace_color, symbol='cross',
            opacity=1.0, line=dict(color='white', width=2))
```

- size=8 for visibility
- color matches parent trace
- cross (+) per marker symbol convention
- opacity=1.0 (orbit markers sit on lines, not surfaces)
- white outline width=2 for contrast against dark background
- `legendgroup` links geometry + marker (toggle together)
- `showlegend=False` on marker (no legend clutter)

Existing shell info markers (solar shells, MAPS ghost tail) stay at
opacity=0.9 / width=1 until those modules are touched during shell
consolidation.

### Placement Convention

- Keplerian elliptical: index `len(x) // 4` (90 deg past perihelion,
  avoids apsidal markers at 0 and 180)
- Hyperbolic: index `len(x) // 4` (midpoint of arc)
- Mean orbit: index `3 * len(x_mean) // 4  # 270 deg,` (no apsidal markers present and avoids Keplerian marker)
- Actual orbit / trajectory: index `len(x) // 2` (midpoint)

### Category 2: Satellite Orbit Traces (Deferred)

26 instances of `text=[...] * len(x)` remain in `idealized_orbits.py`
satellite orbit functions: Mars moons (Phobos, Deimos), Jupiter moons
(8), Saturn moons (13), Uranus moons (7), Neptune moons (8), Pluto
moons (5). Plus 1 analytical orbit trace in `palomas_orrery.py`.

Same pattern fix applies. Lower priority because satellite traces are
only visible when centered on a parent body. Good candidates for the
shell consolidation phase -- same "duplicated code across many
functions" problem.

-----

## Post-Handoff Context (May 2026)

### save_utils.py -- Object Encyclopedia

Since Session 0, `save_utils.py` grew from ~700 to 893 lines with the
addition of the Object Encyclopedia overlay (May 2026). New functions
`_extract_encyclopedia()` and `_build_encyclopedia_overlay()` inject
interactive encyclopedia cards into every orrery HTML output. Not
directly blocking the consolidation, but any session that touches
save_utils.py should know it has grown and has new dependencies on
figure trace metadata.

### palomas_orrery.py line count delta

The file shrank from 10,211 (April 14) to 9,938 (May 12) -- a
273-line reduction from Session 0 orbit marker work and other
maintenance. All absolute line references in this handoff have been
updated to match the May 12 codebase snapshot.

-----

## Revised Implementation Order (April 19, 2026; status updated May 12, 2026)

Original handoff ordered sessions A-F starting with the hardest
structural change (layout extraction). Revised order starts with
the easiest measurable wins and builds toward structural changes:

### 1. Single markers for orbit traces -- DONE (Session 0, April 19)
Category 1 complete (6 orbit trace types in palomas_orrery.py +
idealized_orbits.py). Category 2 (satellite orbits) completed in
step 2.

### 2. Single markers for all shells -- DONE (May 11)
141 conversions across 18 modules. All `text=[X] * len(Y)` patterns
eliminated from every shell file, orbit_data_manager.py, and
idealized_orbits.py (Category 2 satellite traces). CRLF → LF on
all 13 Windows-origin files. n_points reduced (50 → 25 interior,
50 → 20 boundary). Estimated 9-13 MB savings per fully-rendered
export. Dead fibonacci_sphere code in crust/cloud_layer functions
deferred to shell architecture refactor. Mode 5 visual verification
items documented in `HANDOFF_single_info_marker_refactor.md`.

Three-model workflow: Opus 4.7 (manifest), Sonnet 4.6
(implementation), Tony (2 manual conversions + integrator).

### 3. Consolidate shell rendering (was Sessions C-E) -- NOT STARTED
Now that every shell uses the single info marker pattern, extract
`build_sphere_shell()` and `shell_configs.py`. The pattern is
already proven in every file; centralizing is a clean data migration.
`_info` import chain cleanup (210 lines) happens here.

### 4. Consolidate plot rendering (was Sessions A-B) -- NOT STARTED
`orrery_rendering.py`, layout extraction, finalization sequence.
Riskiest structural change, but by now the data flowing through
both pipelines is already lean. Any regression is easier to spot
because exports are small enough to inspect.

### 5. Render context extraction (was Session F) -- NOT STARTED
Ring 3 -- shared setup logic. Not scheduled. Deserves own planning.

**Rationale:** Each step delivers a measurable size reduction that
can be verified before moving on. If we pause between any two steps,
the project is still better off. The original order started with
risk; the revised order starts with reward.

-----

*Module updated: May 2026 with Anthropic's Claude Opus 4.6*