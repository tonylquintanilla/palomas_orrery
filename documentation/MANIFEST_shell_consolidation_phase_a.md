# MANIFEST: Shell Consolidation Step 3 — Phase A (Mercury POC)

**Project:** Paloma's Orrery | Plotting Consolidation Step 3
**Date:** May 13, 2026
**Source prompt:** `PROMPT_shell_consolidation_for_opus_v2.md`
**Manifest by:** Anthropic's Claude Opus 4.7 (audit)
**For execution by:** Anthropic's Claude Opus 4.6 (implementation) + Tony (integrator)

---

## 1. Phase A Scope and Execution Model

### What Phase A delivers

A working Mercury POC. After Phase A:

- Mercury renders via `SHELL_CONFIGS` and `build_sphere_shell()` (sphere shells) plus `CUSTOM_SHELLS` lazy-import (sodium tail, magnetosphere).
- All other bodies render via their existing dispatch paths in `create_planet_visualization()` — unchanged. The codebase is fully functional at every phase boundary.
- New files exist: `orrery_rendering.py`, `shell_configs.py`.
- New name `create_vernal_equinox_indicator` exists in `shared_utilities.py` alongside `create_sun_direction_indicator` (alias). The vernal equinox indicator fires ONCE per Mercury render (replacing 3 per-shell calls).
- `planet_visualization.py` converted to LF line endings.

### What Phase A explicitly does NOT do

- Does NOT refactor other planets. Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Moon, Pluto, Eris, Planet 9 continue using `create_planet_visualization()` blocks unchanged.
- Does NOT touch the Sun dispatch. `create_sun_visualization()` continues to work.
- Does NOT clean up the `_info` import chain. The 89 `_info` imports in `palomas_orrery.py` and 87 dead imports in `palomas_orrery_helpers.py` stay — they are consumed by `build_shell_checkboxes()` via `globals()` and that path is unchanged in Phase A.
- Does NOT update `build_shell_checkboxes()` in `celestial_objects.py`. Mercury's tooltips still come from `globals()` lookup of `mercury_*_info` strings, which still exist (deferred to Phase D).
- Does NOT remove the dead Mercury sphere shell functions from `mercury_visualization_shells.py`. They become unreachable from the dispatch path but the file is retired wholesale in a later phase.

### Why this minimal-blast-radius approach

Each phase must leave the codebase fully functional. The single info marker refactor proved that mechanical execution with tight blast radius is the most reliable model. Phase A proves the architecture on one body; Phases B/C/D mechanically apply the pattern.

### Execution order (canonical)

Execute the sections below in this order. Each section is atomic — finish it before starting the next. Run the syntax check listed at the end of each section.

1. Pre-flight verification (Section 2)
2. Create `orrery_rendering.py` (Section 3)
3. Create `shell_configs.py` (Section 4)
4. Modify `shared_utilities.py` (Section 5)
5. Modify `planet_visualization.py` (Section 6)
6. Modify `mercury_visualization_shells.py` (Section 7)
7. Run verification plan (Section 8)

If any step fails its syntax check, STOP and resolve before proceeding.

---

## 2. Pre-flight Verification

### 2.1 Confirm uploaded files reflect Step 2 state

Run:

```bash
grep -c "hoverinfo='skip'" /path/to/mercury_visualization_shells.py
# Expected: >= 8 (Step 2 single info marker conversions)

grep "Module updated:" /path/to/mercury_visualization_shells.py | head -1
# Expected: "Module updated: May 2026 with Anthropic's Claude Opus 4.7"
```

If either check fails, STOP — the uploaded file is not post-Step-2 and the manifest assumptions don't hold.

### 2.2 Backup files Phase A will touch

Before any edits, create archive copies:

```
mercury_visualization_shells.py     -> mercury_visualization_shells.py.phaseA_backup
planet_visualization.py             -> planet_visualization.py.phaseA_backup
shared_utilities.py                 -> shared_utilities.py.phaseA_backup
```

`orrery_rendering.py` and `shell_configs.py` are new files — no backup needed.

### 2.3 Line ending inventory

Confirm before starting:

| File | Expected | If different |
|------|----------|--------------|
| `mercury_visualization_shells.py` | LF | Stop, investigate |
| `planet_visualization.py` | CRLF | Will be converted to LF in Section 6 |
| `shared_utilities.py` | LF | Stop, investigate |
| `palomas_orrery.py` | LF | Stop, investigate |

Verify with `file <path>` on each.

### 2.4 Constants verification

```bash
grep "MERCURY_RADIUS_AU" /path/to/planet_visualization_utilities.py
# Expected: MERCURY_RADIUS_AU = MERCURY_RADIUS_KM / KM_PER_AU
```

`shell_configs.py` will import from `constants_new.py` (canonical) and resolve Mercury radius via `CENTER_BODY_RADII['Mercury'] / KM_PER_AU`. Verify this matches `MERCURY_RADIUS_AU` numerically — they should be identical since `planet_visualization_utilities.py` re-exports from `constants_new.py`.

---

## 3. NEW FILE — `orrery_rendering.py`

### 3.1 Purpose

Owns `build_sphere_shell()` for Phase A. Layout extraction (Ring 1) and finalization (Ring 2) functions are added in Step 4 — out of scope here. Phase A creates the module with only the builder so the file exists for Step 4 to extend.

### 3.2 Full file contents

Create the file with these exact contents. Use Python binary mode (`wb`), LF line endings, ASCII only.

```python
"""
orrery_rendering.py - Rendering contract between plot_objects and animate_objects.

Owns the generic sphere shell builder consumed by the unified shell dispatch.
Layout extraction (build_orrery_layout, _build_scene_axes, _build_annotations)
and finalization (finalize_orrery_figure) will be added in Step 4 of the
plotting consolidation. Phase A of Step 3 creates this module with only the
shell builder.

Key functions:
    build_sphere_shell() - generic sphere shell from config dict (Step 3, Phase A)

Consumed by: planet_visualization.py (dispatch loop)

Module updated: May 2026 with Anthropic's Claude Opus 4.7
"""

import plotly.graph_objs as go

from constants_new import CENTER_BODY_RADII, KM_PER_AU
from planet_visualization_utilities import create_sphere_points


def build_sphere_shell(config, body_name, center_position=(0, 0, 0)):
    """Generic sphere shell from config dict.

    Structurally enforces the single-info-marker pattern:
    one geometry trace with hoverinfo='skip' plus one cross marker
    at the north pole carrying the full hover text exactly once.

    Accepts either:
        config['radius_fraction'] - multiplied by body radius from CENTER_BODY_RADII
        config['radius_au']       - used directly (Sun shells)

    Required config keys:
        name              str    Display name (e.g. 'Inner Core')
        color             str    rgb(...) string
        opacity           float
        marker_size       float  size of geometry markers
        hover_text        str    info marker hover string (3D plot)
        radius_fraction OR radius_au  (one must be present)

    Optional config keys:
        n_points          int    Sphere resolution (default 20)

    Returns:
        list of two plotly Scatter3d traces: [geometry, info_marker]
    """
    # Resolve radius
    if 'radius_au' in config:
        radius_au = config['radius_au']
    elif 'radius_fraction' in config:
        body_radius_au = CENTER_BODY_RADII[body_name] / KM_PER_AU
        radius_au = config['radius_fraction'] * body_radius_au
    else:
        raise ValueError(
            "build_sphere_shell: config for %s/%s missing both "
            "'radius_fraction' and 'radius_au'" % (body_name, config.get('name', '?'))
        )

    n_points = config.get('n_points', 20)

    # Generate sphere geometry
    x, y, z = create_sphere_points(radius_au, n_points=n_points)
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z

    trace_name = "%s: %s" % (body_name, config['name'])

    # Geometry trace - visual only, no hover
    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(
            size=config['marker_size'],
            color=config['color'],
            opacity=config['opacity']
        ),
        name=trace_name,
        legendgroup=trace_name,
        hoverinfo='skip',
        showlegend=True
    )

    # Single info marker at north pole, 5% above radius
    r_info = radius_au * 1.05
    info_trace = go.Scatter3d(
        x=[center_x], y=[center_y], z=[center_z + r_info],
        mode='markers',
        marker=dict(size=6, color=config['color'], opacity=0.9,
                    symbol='cross', line=dict(color='white', width=1)),
        name='',
        legendgroup=trace_name,
        text=[config['hover_text']],
        customdata=[trace_name],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    )

    return [shell_trace, info_trace]
```

### 3.3 Verification

```bash
python3 -m py_compile orrery_rendering.py
# Expected: no output (syntax OK)

file orrery_rendering.py
# Expected: "ASCII text" (no CRLF)
```

---

## 4. NEW FILE — `shell_configs.py`

### 4.1 Purpose

Single data file for all sphere shell parameters and custom geometry registry. Phase A populates Mercury only; Phases B/C/D add other bodies.

### 4.2 File structure

Create the file with the structure below. Use Python binary mode (`wb`), LF line endings, ASCII only.

```python
"""
shell_configs.py - Shell configuration data for all celestial bodies.

Phase A (Mercury POC) - May 2026. Other bodies will be added in Phases B-D.

Two registries:

  SHELL_CONFIGS  - Sphere shell parameters (radius, color, opacity, hover text,
                   tooltip). Consumed by build_sphere_shell() in orrery_rendering.py.

  CUSTOM_SHELLS  - Non-sphere geometry (magnetospheres, rings, tails, belts).
                   Maps shell_name -> {'builder': 'module.function', 'tooltip': '...'}.
                   Lazy-imported at render time to address startup lag.

To add a new body:
    1. Verify its radius is in CENTER_BODY_RADII (constants_new.py)
    2. Add its sphere shell configs to SHELL_CONFIGS
    3. Add its custom geometry (if any) to CUSTOM_SHELLS
    4. Add its checkbox vars in palomas_orrery.py GUI section (or already exist)

Source citations are preserved as comments above each body block. The
provenance audit (April 2026) verified all values - do not modify.

Module updated: May 2026 with Anthropic's Claude Opus 4.7
"""

# ============================================================
# SHELL_CONFIGS: sphere shells handled by build_sphere_shell()
# ============================================================
# Keys are bare shell names (no body prefix), matching the post-prefix-strip
# keys produced by the unified dispatch in planet_visualization.py.

SHELL_CONFIGS = {

    # ============================================================
    # Mercury
    # ============================================================
    # Source: NASA MESSENGER Mission, Margot et al. (2012), Sori (2018)
    # Verified: April 2026 via Gemini fact-check
    'Mercury': {

        'inner_core': {
            'name': 'Inner Core',
            'radius_fraction': 0.41,
            'color': 'rgb(255, 180, 140)',
            'opacity': 1.0,
            'n_points': 25,
            'marker_size': 4.0,
            'hover_text': (
                "Inner Core: Mercury has a very large metallic core, unlike Earth's which is proportionally smaller.<br>"
                "Evidence suggests that Mercury has a solid inner core, similar to Earth's. It is estimated to be about <br>"
                "1,000 kilometers thick based on Messenger findings (2019)."
            ),
            'tooltip': (
                "Inner Core: Mercury has a very large metallic core, unlike Earth's which is proportionally smaller.\n"
                "Evidence suggests that Mercury has a solid inner core, similar to Earth's. It is estimated to be about \n"
                "1,000 kilometers thick based on Messenger findings (2019)."
            ),
        },

        'outer_core': {
            'name': 'Outer Core',
            'radius_fraction': 0.85,
            'color': 'rgb(255, 140, 0)',
            'opacity': 0.8,
            'n_points': 25,
            'marker_size': 3.7,
            'hover_text': (
                "Outer Core: Surrounding the solid inner core is a liquid metallic outer core. The movement of this molten iron <br>"
                "is thought to be the source of Mercury's weak magnetic field. About 1074 km thick."
            ),
            'tooltip': (
                "Outer Core: Surrounding the solid inner core is a liquid metallic outer core. The movement of this molten iron \n"
                "is thought to be the source of Mercury's weak magnetic field. About 1074 km thick."
            ),
        },

        'mantle': {
            'name': 'Mantle',
            'radius_fraction': 0.98,
            'color': 'rgb(230, 100, 20)',
            'opacity': 0.7,
            'n_points': 25,
            'marker_size': 3.4,
            'hover_text': (
                "Mantle: Surrounding the core is a rocky mantle. Recent research suggests this mantle might even contain a layer of <br>"
                "diamonds, formed from ancient carbon-rich material under immense pressure. The mantle is significantly thinner than <br>"
                "Earth's, estimated to be only about 331 kilometers thick."
            ),
            'tooltip': (
                "Mantle: Surrounding the core is a rocky mantle. Recent research suggests this mantle might even contain a layer of \n"
                "diamonds, formed from ancient carbon-rich material under immense pressure. The mantle is significantly thinner than \n"
                "Earth's, estimated to be only about 331 kilometers thick."
            ),
        },

        # NOTE: Mercury crust converted from Mesh3d to standard sphere shell per
        # Step 3 pre-decided decision. The Mesh3d flat-shading visual is not
        # preserved. Fibonacci sphere dead code in the original function is
        # eliminated by config-driven dispatch (function is no longer called).
        'crust': {
            'name': 'Crust',
            'radius_fraction': 1.0,
            'color': 'rgb(128, 128, 128)',
            'opacity': 1.0,
            'n_points': 20,
            'marker_size': 3.0,
            'hover_text': (
                "(Note: toggle off the crust layer in the legend to better see the interior structure.)<br><br>"
                "Mercury has a solid silicate crust that is heavily cratered, resembling Earth's Moon. The crust is likely quite thin <br>"
                "compared to Earth's. There's also a theory that a significant portion of Mercury's crust might be made of diamonds, <br>"
                "formed by billions of years of meteorite impacts on a graphite-rich surface. About 35 km thick."
            ),
            'tooltip': (
                "Mercury has a solid silicate crust that is heavily cratered, resembling Earth's Moon. The crust is likely quite thin \n"
                "compared to Earth's. There's also a theory that a significant portion of Mercury's crust might be made of diamonds, \n"
                "formed by billions of years of meteorite impacts on a graphite-rich surface. About 35 km thick."
            ),
        },

        'atmosphere': {
            'name': 'Exosphere',
            'radius_fraction': 2.0,
            'color': 'rgb(150, 200, 255)',
            'opacity': 0.5,
            'n_points': 20,
            'marker_size': 2.5,
            'hover_text': (
                "Exosphere: Unlike Earth's substantial atmosphere, Mercury has an extremely thin exosphere. This exosphere is not <br>"
                "dense enough to trap heat or offer significant protection from space. It is composed mostly of oxygen, sodium, <br>"
                "hydrogen, helium, and potassium atoms that have been blasted off the surface by the solar wind and micrometeoroid impacts.<br><br>"
                "Mercury has what is more accurately described as a tenuous exosphere rather than a substantial atmosphere like Earth's. <br>"
                "This exosphere is extremely thin, and its atoms are so sparse they are more likely to collide with the surface than with <br>"
                "each other. The extent of Mercury's exosphere is not well-defined by a pressure gradient as with a true atmosphere. Instead, <br>"
                "it gradually fades out into space. However, we can consider how far certain exospheric components have been observed:<br>"
                "* Sodium Tail: Due to solar radiation pressure, sodium atoms are pushed away from Mercury, forming a long, comet-like tail. <br>"
                "  This tail has been detected extending to distances of over 24 million kilometers (approximately 10,000 Mercury radii) <br>"
                "  from the planet. This is by far the most extended component of Mercury's exosphere.<br>"
                "* Other Elements: Other elements like hydrogen, helium, oxygen, potassium, calcium, and magnesium are also present in the <br>"
                "  exosphere. These are generally found much closer to the planet's surface, within a few Mercury radii. For instance, calcium <br>"
                "  and magnesium have been observed in the tail but at distances less than 8 Mercury radii.<br>"
                "In summary: While the bulk of Mercury's exospheric atoms are concentrated very close to the surface (within 1 Mercury radius), <br>"
                "the sodium tail is a significant feature that extends incredibly far, up to 10,000 Mercury radii. The main body of the exosphere <br>"
                "is very close to the surface, but the tenuous sodium tail stretches to an immense distance."
            ),
            'tooltip': (
                "Exosphere: Unlike Earth's substantial atmosphere, Mercury has an extremely thin exosphere. This exosphere is not \n"
                "dense enough to trap heat or offer significant protection from space. It is composed mostly of oxygen, sodium, \n"
                "hydrogen, helium, and potassium atoms that have been blasted off the surface by the solar wind and micrometeoroid impacts."
            ),
        },

        'hill_sphere': {
            'name': 'Hill Sphere',
            'radius_fraction': 94.4,
            'color': 'rgb(0, 255, 0)',
            'opacity': 0.25,
            'n_points': 30,
            'marker_size': 1.0,
            'hover_text': (
                "Hill Sphere: Every celestial body has a Hill sphere (also known as the Roche sphere), which is the region around it <br>"
                "where its gravity is the dominant gravitational force. Mercury certainly has a Hill sphere, but its size depends on <br>"
                "its mass and its distance from the Sun. Being the closest planet to the Sun, the Sun's powerful gravity limits the <br>"
                "extent of Mercury's Hill sphere compared to planets farther out.<br><br>"
                "The Hill sphere is the region around a where its own gravity is the dominant force in attracting satellites. For <br>"
                "a planet orbiting a star, it's the region where the planet's gravity is stronger than the star's tidal forces.<br><br>"
                "The Hill Sphere radius can be described in words as follows: it is equal to the planet's average distance from the <br>"
                "Sun (its orbital semi-major axis) multiplied by the cube root of the ratio between the planet's mass and three times <br>"
                "the Sun's mass. In other words, you take how far the planet orbits out from the Sun, then scale that distance by the <br>"
                "cube root of (planet mass / [3 x solar mass]) to find the boundary within which the planet's gravity dominates over the Sun's."
            ),
            'tooltip': (
                "SET MANUAL SCALE TO AT LEAST 0.005 AU TO VISUALIZE.\n\n"
                "Hill Sphere: Every celestial body has a Hill sphere (also known as the Roche sphere), which is the region around it \n"
                "where its gravity is the dominant gravitational force. Mercury's Hill sphere extends to about 94 Mercury radii."
            ),
        },

    },

    # Other bodies added in Phases B, C, D
}


# ============================================================
# CUSTOM_SHELLS: geometry that doesn't fit the sphere builder
# ============================================================
# Maps body_name -> shell_name -> {'builder': 'module.function', 'tooltip': '...'}
# Lazy-imported at render time. The builder function must accept
# center_position and return a list of plotly traces.

CUSTOM_SHELLS = {

    # ============================================================
    # Mercury
    # ============================================================
    'Mercury': {

        'sodium_tail': {
            'builder': 'mercury_visualization_shells.create_mercury_sodium_tail',
            'tooltip': (
                "TO VISUALIZE CLOSE UP SET MANUAL SCALE TO AT LEAST 0.002 AU TO VISUALIZE.\n"
                "TO VISUALIZE THE COMPLETE TAIL INCLUDE VENUS IN THE PLOT OR SET MANUAL SCALE TO 1.0 AU\n\n"
                "Sodium Tail: Mercury has a remarkable sodium tail that extends incredibly far into space - up to 10,000 Mercury radii \n"
                "(approximately 24 million kilometers). This tail is created when sodium atoms from Mercury's exosphere \n"
                "are pushed away by solar radiation pressure. The tail always points away from the Sun, similar to a comet's tail.\n\n"
                "The sodium tail is highly dynamic and can vary significantly based on Mercury's position in its orbit and solar activity. \n"
                "It's one of Mercury's most distinctive features and can be observed from Earth using specialized telescopes."
            ),
        },

        'magnetosphere': {
            'builder': 'mercury_visualization_shells.create_mercury_magnetosphere_shell',
            # Tooltip extracted from mercury_magnetosphere_info in
            # mercury_visualization_shells.py (line ~600). Implementing Claude
            # must copy the full string verbatim from the source file.
            'tooltip': (
                "<COPY FROM mercury_magnetosphere_info IN mercury_visualization_shells.py>"
            ),
        },

    },

    # Other bodies added in Phases C, D
}
```

### 4.3 Implementing Claude — tooltip extraction note

The Mercury `magnetosphere` entry above has a placeholder `tooltip` value. Open `mercury_visualization_shells.py`, locate `mercury_magnetosphere_info` (line ~600), and copy the full multi-line string verbatim into the placeholder. Replace `<br>` with `\n` in the GUI tooltip version (tooltips are tk Labels, not HTML).

The general rule for tooltip extraction:
- `hover_text` field → use the existing `description` string from each shell's `layer_info` dict (it already has `<br>` tags for HTML).
- `tooltip` field → use the existing `mercury_*_info` string (it uses `\n` for tk Labels).

For Mercury Phase A, I have transcribed the values directly from the project file. If Implementing Claude finds any discrepancy between the uploaded shell file and the values above, the uploaded file is authoritative.

### 4.4 Verification

```bash
python3 -m py_compile shell_configs.py
file shell_configs.py
# Expected: ASCII text, no CRLF

python3 -c "from shell_configs import SHELL_CONFIGS, CUSTOM_SHELLS; print(len(SHELL_CONFIGS['Mercury']), len(CUSTOM_SHELLS['Mercury']))"
# Expected: 6 2
```

---

## 5. MODIFY — `shared_utilities.py`

### 5.1 Strategy

Rename `create_sun_direction_indicator` to `create_vernal_equinox_indicator` AND keep the old name as a backward-compat alias. Other shell modules still call the old name; they will be cleaned up in Phases B/C/D. Phase A only needs the new name to exist so the unified dispatch can call it.

### 5.2 Edits

**Edit 1: Update module docstring (top of file)**

Find:
```python
"""
shared_utilities.py - Small shared helpers used across shell visualization modules.

Currently contains create_sun_direction_indicator(), which adds a visual
arrow showing the Sun's direction in body-centered plots. Used by most
planetary shell modules when the center body is not the Sun.

Module updated: April 2026 with Anthropic's Claude Opus 4.6
"""
```

Replace with:
```python
"""
shared_utilities.py - Small shared helpers used across shell visualization modules.

Contains create_vernal_equinox_indicator() (formerly create_sun_direction_indicator),
which adds a visual arrow showing the +X reference direction (vernal equinox /
First Point of Aries) in body-centered plots. The name was corrected in May 2026 -
the arrow points to the +X axis, not the Sun. The old name remains as an alias
for backward compatibility during the shell consolidation migration.

Module updated: May 2026 with Anthropic's Claude Opus 4.7
"""
```

**Edit 2: Add the new function name**

Find (line 15-16):
```python
def create_sun_direction_indicator(center_position=(0, 0, 0), axis_range=None, shell_radius=None,
                              object_type=None, center_object=None):
```

Replace with:
```python
def create_vernal_equinox_indicator(center_position=(0, 0, 0), axis_range=None, shell_radius=None,
                              object_type=None, center_object=None):
```

Then, at the END of the file (after the function body and its return statement), add:

```python


# ============================================================
# Backward compatibility alias
# ============================================================
# During the shell consolidation migration (Step 3, May 2026), shell modules
# still call create_sun_direction_indicator by its old name. This alias keeps
# them working until they are migrated to the unified dispatch (Phases B-D)
# or until the unreachable shell functions are archived. After Step 3 completes,
# this alias can be removed.

create_sun_direction_indicator = create_vernal_equinox_indicator
```

### 5.3 Update internal docstring

Inside the function body, find the existing docstring:
```python
    """
    Creates a visual indicator showing the direction to the Sun (along negative X-axis).
    ...
    """
```

Replace the first sentence with:
```python
    """
    Creates a visual indicator showing the +X reference direction (vernal equinox).
    Despite the historical name (sun direction), the arrow points along +X, which
    is the First Point of Aries in J2000 - not the time-varying direction to the Sun.
    ...
    """
```

Keep the rest of the docstring unchanged.

### 5.4 Verification

```bash
python3 -m py_compile shared_utilities.py
python3 -c "from shared_utilities import create_vernal_equinox_indicator, create_sun_direction_indicator; print(create_vernal_equinox_indicator is create_sun_direction_indicator)"
# Expected: True
```

---

## 6. MODIFY — `planet_visualization.py`

### 6.1 CRLF to LF conversion (do this FIRST)

The file is currently CRLF. Convert to LF before any other edits using Python binary mode:

```python
import os
path = '/path/to/planet_visualization.py'
with open(path, 'rb') as f:
    content = f.read()
content = content.replace(b'\r\n', b'\n')
with open(path, 'wb') as f:
    f.write(content)
```

Verify:
```bash
file planet_visualization.py
# Expected: ASCII text (no "with CRLF line terminators")
```

After this step, all subsequent edits to `planet_visualization.py` operate on LF content.

### 6.2 Add new imports at top of file

Find the existing imports block (lines ~1-30, before the from-module imports for shells). Add at the END of the imports section, before the first `from <body>_visualization_shells import` statement:

```python
# Shell consolidation imports (Step 3, Phase A)
from orrery_rendering import build_sphere_shell
from shell_configs import SHELL_CONFIGS, CUSTOM_SHELLS
from shared_utilities import create_vernal_equinox_indicator
import importlib
```

### 6.3 Refactor `create_celestial_body_visualization()` body

Locate the function definition (line 535 in the original CRLF file; line number will be slightly different post-CRLF conversion — use function-name grep to find it).

The current function body (lines 535 to ~870 in the original file) is the ~340-line if/elif chain over body_name with stale Mercury data.

Replace the ENTIRE function body (everything from the `def` line to the final `return fig` of this function) with:

```python
def create_celestial_body_visualization(fig, body_name, shell_vars, animate=False, frames=None,
                                        center_position=(0, 0, 0),
                                        object_type=None, center_object=None):
    """
    Unified config-driven dispatch for celestial body shell visualization.

    Looks up the body's shell configs in SHELL_CONFIGS (sphere shells) and
    CUSTOM_SHELLS (non-sphere geometry). Sphere shells route through
    build_sphere_shell(); custom shells are lazy-imported by registry entry.

    Issues ONE vernal equinox indicator per body at the outermost active
    shell radius, replacing the per-shell indicator calls that were
    duplicated across every shell function.

    Step 3 Phase A: only Mercury is fully wired through this function. Other
    bodies continue to render via create_planet_visualization() blocks until
    their Phase B/C/D migrations land.

    Parameters:
        fig (plotly.graph_objects.Figure): The figure to add traces to
        body_name (str): Body name as it appears in SHELL_CONFIGS keys
                         (e.g. 'Mercury', 'Pluto', 'Sun')
        shell_vars (dict): Maps shell var names to tk.IntVar.
                           Keys may be prefixed ('mercury_inner_core') or
                           bare ('inner_core') - prefix is stripped to match
                           config keys.
        animate (bool): Reserved for future animation hooks (unused in Phase A)
        frames (list): Reserved for future animation hooks (unused in Phase A)
        center_position (tuple): (x, y, z) AU position of the body's center
        object_type (str): Object type for vernal equinox indicator self-suppression
        center_object (str): Name of object at plot center (indicator self-suppress)

    Returns:
        plotly.graph_objects.Figure: The updated figure
    """
    configs = SHELL_CONFIGS.get(body_name, {})
    customs = CUSTOM_SHELLS.get(body_name, {})

    # Strip body prefix from shell_vars keys to match config keys.
    # 'mercury_inner_core' -> 'inner_core'; bare keys (Sun) pass through.
    # 'Planet 9' becomes 'planet9_'.
    body_prefix = body_name.lower().replace(' ', '') + '_'

    outermost_radius_au = 0.0

    for key, var in shell_vars.items():
        try:
            if var.get() != 1:
                continue
        except (AttributeError, TypeError):
            # var is not a tk.IntVar (e.g., plain int from tests)
            if not var:
                continue

        shell_name = key[len(body_prefix):] if key.startswith(body_prefix) else key

        if shell_name in configs:
            config = configs[shell_name]
            traces = build_sphere_shell(config, body_name, center_position)
            for t in traces:
                fig.add_trace(t)
            # Track outermost radius for indicator scaling
            if 'radius_au' in config:
                shell_r = config['radius_au']
            else:
                body_r = CENTER_BODY_RADII[body_name] / KM_PER_AU
                shell_r = config['radius_fraction'] * body_r
            outermost_radius_au = max(outermost_radius_au, shell_r)

        elif shell_name in customs:
            custom = customs[shell_name]
            module_path, func_name = custom['builder'].rsplit('.', 1)
            mod = importlib.import_module(module_path)
            builder = getattr(mod, func_name)
            traces = builder(center_position)
            for t in traces:
                fig.add_trace(t)

        # If shell_name is in neither registry, silently skip.
        # In Phase A this is expected for bodies that haven't migrated yet
        # (their dispatch is still in create_planet_visualization).

    # ONE vernal equinox indicator per body (replaces ~50 per-shell calls).
    # Uses outermost active shell radius for scaling. The function self-
    # suppresses based on object_type / center_object.
    if outermost_radius_au > 0:
        indicator_traces = create_vernal_equinox_indicator(
            center_position=center_position,
            shell_radius=outermost_radius_au,
            object_type=object_type if object_type is not None else body_name,
            center_object=center_object,
        )
        for t in indicator_traces:
            fig.add_trace(t)

    return fig
```

This requires `CENTER_BODY_RADII` and `KM_PER_AU` to be imported at top of `planet_visualization.py`. Verify the existing imports include `from constants_new import CENTER_BODY_RADII, KM_PER_AU`. If not, add it.

### 6.4 Update Mercury's block in `create_planet_visualization()`

Locate the function `create_planet_visualization()` (line 875 in original, body lower in post-CRLF-conversion file). Find Mercury's block — it's an `if planet_name == 'Mercury':` block followed by 8 `if shell_vars['mercury_*'].get() == 1:` checks (about 16 lines).

Replace the entire Mercury block (from `if planet_name == 'Mercury':` to the blank line before `if planet_name == 'Venus':`) with:

```python
    if planet_name == 'Mercury':
        # Step 3 Phase A: delegate to unified config-driven dispatch.
        # See create_celestial_body_visualization() for the new architecture.
        return create_celestial_body_visualization(
            fig, planet_name, shell_vars,
            animate=animate, frames=frames,
            center_position=center_position,
            object_type='Mercury',
            center_object='Mercury',
        )
```

Note the early `return` — this short-circuits the rest of the function for Mercury. The if/elif chain for other planets (Venus, Earth, Mars, etc.) is untouched.

### 6.5 Verification

```bash
python3 -m py_compile planet_visualization.py
file planet_visualization.py
# Expected: ASCII text (no CRLF)

python3 -c "from planet_visualization import create_celestial_body_visualization, create_planet_visualization; print('imports OK')"
# Expected: imports OK
```

---

## 7. MODIFY — `mercury_visualization_shells.py`

### 7.1 Strategy

Mercury's sodium_tail and magnetosphere functions are called via lazy-import from the new dispatch. They currently call `create_sun_direction_indicator` internally, which would duplicate the indicator (the new dispatch loop emits ONE indicator per body). Strip these internal calls.

Mercury's sphere shell functions (`create_mercury_inner_core_shell`, etc.) become unreachable from the dispatch path after Phase A — they're not called by anything in production. Leave them alone for now; they'll be archived in a later cleanup phase.

### 7.2 Edits — bottom-up (highest line numbers first)

There are 3 indicator call blocks in `mercury_visualization_shells.py`:
- Line ~875 — inside `create_mercury_hill_sphere_shell` (sphere shell — unreachable post-Phase-A, but strip for consistency)
- Line ~790 — inside `create_mercury_magnetosphere_shell` (custom — MUST strip)
- Line ~454 — inside `create_mercury_atmosphere_shell` (sphere shell — unreachable post-Phase-A, but strip for consistency)

Note: `create_mercury_sodium_tail` does NOT contain an indicator call (it was never added — sodium tail is far from origin), so no edit needed there.

**Edit 1: Strip indicator call from `create_mercury_hill_sphere_shell` (line ~875)**

Find:
```python
    sun_traces = create_sun_direction_indicator(
        center_position=center_position, 
        shell_radius=radius_au
    )
    for trace in sun_traces:
        traces.append(trace)        
```

Replace with:
```python
    # Phase A (May 2026): vernal equinox indicator emission moved to dispatch
    # loop in planet_visualization.py. One indicator per body, not per shell.
```

**Edit 2: Strip indicator call from `create_mercury_magnetosphere_shell` (line ~790)**

Find:
```python
    sun_traces = create_sun_direction_indicator(
        center_position=center_position, 
        shell_radius=...
    )
    for trace in sun_traces:
        traces.append(trace)
```

(The exact arguments may differ; locate by the function name and the `for trace in sun_traces:` loop pattern.)

Replace with:
```python
    # Phase A (May 2026): vernal equinox indicator emission moved to dispatch
    # loop in planet_visualization.py. One indicator per body, not per shell.
```

**Edit 3: Strip indicator call from `create_mercury_atmosphere_shell` (line ~454)**

Find:
```python
    sun_traces = create_sun_direction_indicator(
        center_position=center_position, 
        shell_radius=layer_radius
    )
    for trace in sun_traces:
        traces.append(trace)
```

Replace with:
```python
    # Phase A (May 2026): vernal equinox indicator emission moved to dispatch
    # loop in planet_visualization.py. One indicator per body, not per shell.
```

### 7.3 Implementation note for Implementing Claude

Edit bottom-up (Edit 1, then 2, then 3) so earlier edits don't shift the line numbers for later edits. Use Python binary mode (`rb`/`wb`) and exact-string replacement to avoid Unicode/whitespace corruption.

If the exact text doesn't match (e.g., trailing whitespace differs), use the function definition as an anchor and read the function body to find the precise indicator call block. Do NOT use regex.

### 7.4 Verification

```bash
python3 -m py_compile mercury_visualization_shells.py

grep -c "sun_traces = create_sun_direction_indicator" mercury_visualization_shells.py
# Expected: 0  (all three calls stripped)
```

---

## 8. Verification Plan

### 8.1 Static checks

```bash
# All new/modified files compile
python3 -m py_compile orrery_rendering.py shell_configs.py shared_utilities.py
python3 -m py_compile planet_visualization.py mercury_visualization_shells.py

# All target files are LF
for f in orrery_rendering.py shell_configs.py shared_utilities.py \
         planet_visualization.py mercury_visualization_shells.py; do
    file "$f" | grep -q CRLF && echo "FAIL: $f still CRLF" || echo "OK: $f"
done

# No new Unicode chars introduced
for f in orrery_rendering.py shell_configs.py; do
    if grep -P '[^\x00-\x7F]' "$f" > /dev/null; then
        echo "FAIL: $f contains non-ASCII"
    else
        echo "OK: $f ASCII clean"
    fi
done
```

### 8.2 Import smoke test

```bash
python3 -c "
from orrery_rendering import build_sphere_shell
from shell_configs import SHELL_CONFIGS, CUSTOM_SHELLS
from shared_utilities import create_vernal_equinox_indicator, create_sun_direction_indicator
from planet_visualization import create_celestial_body_visualization, create_planet_visualization

# Verify Mercury config completeness
mercury = SHELL_CONFIGS['Mercury']
assert set(mercury.keys()) == {'inner_core', 'outer_core', 'mantle', 'crust', 'atmosphere', 'hill_sphere'}, \
    'Mercury sphere keys mismatch: %s' % sorted(mercury.keys())
for shell_name, cfg in mercury.items():
    assert 'radius_fraction' in cfg or 'radius_au' in cfg, '%s missing radius' % shell_name
    for k in ('name', 'color', 'opacity', 'marker_size', 'hover_text', 'tooltip'):
        assert k in cfg, '%s missing %s' % (shell_name, k)

mercury_custom = CUSTOM_SHELLS['Mercury']
assert set(mercury_custom.keys()) == {'sodium_tail', 'magnetosphere'}, \
    'Mercury custom keys mismatch: %s' % sorted(mercury_custom.keys())

# Verify alias
assert create_sun_direction_indicator is create_vernal_equinox_indicator

print('All Phase A static checks PASS')
"
```

### 8.3 Functional check — Mercury renders via configs

Run the orrery, select Mercury as center body, enable all Mercury shells, generate a plot. Expected behavior:

| Check | Pass criterion |
|-------|----------------|
| Inner core renders | Orange sphere at r=0.41 of Mercury radius |
| Outer core renders | Deeper orange sphere at r=0.85 |
| Mantle renders | Reddish-brown sphere at r=0.98 |
| Crust renders | Gray sphere at r=1.0 (NOT Mesh3d - flat shading lost is expected) |
| Atmosphere/Exosphere | Light blue sphere at r=2.0 |
| Sodium tail | Yellow anti-sunward streak (lazy-imported, unchanged from Step 2) |
| Magnetosphere | Bow shock + magnetopause geometry (unchanged from Step 2) |
| Hill sphere | Green sparse sphere at r=94.4 |
| Hover labels | One info marker per shell, at north pole, with full hover text |
| Vernal equinox indicator | Appears ONCE, at +X direction, sized to outermost shell |

### 8.4 Functional check — other bodies unchanged

In the same orrery session, select Venus, Earth, Mars (one at a time) as center body. Expected: all shells render as they did before Phase A. The if/elif chain in `create_planet_visualization` is untouched for these bodies.

### 8.5 Indicator deduplication check

For Mercury, count the rendered vernal equinox arrow segments in the plot. Expected: exactly ONE indicator (3 traces: arrow, head, label) regardless of how many shells are active. Pre-Phase-A behavior: 3 indicator copies (one each from atmosphere, magnetosphere, hill_sphere).

### 8.6 File size baseline

Save a Mercury-only static plot to HTML. Record the file size. Expected: similar to or slightly smaller than the pre-Phase-A baseline. The big size savings come in Phases B/C/D when more bodies migrate. Phase A's value is architectural — proving the pattern works.

### 8.7 Mode 5 visual verification (Tony)

Items for Tony to eyeball:

1. Crust visual change — Mesh3d to Scatter3d. Surface will look like dots, not solid. This is expected. If unacceptable, revert to Mesh3d in build_sphere_shell (would need a `'geometry_type': 'mesh3d'` config option, which we deliberately omitted).
2. Info marker positions — all 6 sphere shells should have a single cross marker at the north pole 5% above the shell radius. Verify no duplicate hover targets.
3. Vernal equinox arrow scale — should match outermost active shell. With Hill Sphere on (r=94.4 Mercury radii) the arrow should be large. With Hill Sphere off, arrow should be sized to the next outermost active shell.

---

## 9. Patterned Outlines for Phases B, C, D

The Mercury template established in Phase A applies mechanically to all other bodies. The implementing Claude session for each phase follows the same eight steps; only the data values differ.

### Phase B — Archivable bodies (Pluto, Planet 9, Eris, Moon)

These bodies have ZERO custom geometry after Mesh3d crust conversion. After Phase B, their shell files are fully archivable.

For each body in order Pluto → Planet 9 → Eris → Moon:

1. Open `<body>_visualization_shells.py`, extract `layer_info` dict and `*_info` string for each sphere shell function. Build a SHELL_CONFIGS entry following the Mercury template in `shell_configs.py`.
2. For Mesh3d crust functions: extract `radius_fraction`, `color`, `opacity` from the Mesh3d block. Use `n_points=20`, `marker_size=3.0` as defaults. Strip the unreachable `fibonacci_sphere()` dead code by simply not migrating it — the new config-driven sphere builder doesn't use it.
3. Add the body's CUSTOM_SHELLS entry as `{}` (empty dict) or just omit — both work.
4. In `planet_visualization.py`, locate the body's block in `create_planet_visualization()`. Replace with the same one-line delegation pattern used for Mercury in Section 6.4.
5. Strip `sun_traces = create_sun_direction_indicator(...)` calls from any custom shell functions in the body's shell file. For Phase B bodies (no custom geometry), this means no edits are needed in the shell files — all sphere shell functions become unreachable, and their internal indicator calls don't fire.
6. Verify per Section 8 pattern.

Body-specific notes:

| Body | Shells | Notes |
|------|--------|-------|
| Pluto | core, mantle, crust, haze_layer, atmosphere, hill_sphere | Crust is Mesh3d - convert. No custom geometry. |
| Planet 9 | surface, hill_sphere | Surface is Mesh3d - convert. No custom geometry. Hill sphere uses absolute or theoretical radius - confirm. |
| Eris | core, mantle, crust, atmosphere, hill_sphere | Crust is Mesh3d - convert. No custom geometry. |
| Moon | inner_core, outer_core, mantle, crust, exosphere, hill_sphere | Crust is Mesh3d - convert. No custom geometry. |

After all four bodies migrate, their `<body>_visualization_shells.py` files can be moved to an `archive/` directory. Imports of these files in `planet_visualization.py` (lines ~90-170) can be removed at the same time.

Phase B is a clean stopping point. Tony can pause for any duration before starting Phase C.

### Phase C — Mixed bodies (Venus, Mars, Earth, Jupiter, Saturn, Uranus, Neptune)

The largest phase. Each body has sphere shells (migrate to SHELL_CONFIGS) plus custom geometry (CUSTOM_SHELLS lazy-import). Per-body, follow the Mercury template; strip indicator calls from custom geometry functions only.

Body order suggestion (simplest to most complex): Venus → Mars → Earth → Uranus → Neptune → Jupiter → Saturn.

Body-specific notes:

| Body | Sphere shells | Custom geometry | Indicator strip count |
|------|---------------|-----------------|------------------------|
| Venus | core, mantle, crust, atmosphere, upper_atmosphere, hill_sphere | magnetosphere (bow shock + magnetopause) | 1 per custom |
| Mars | inner_core, outer_core, mantle, crust, atmosphere, upper_atmosphere, hill_sphere | magnetosphere, crustal_fields | 2 per custom |
| Earth | inner_core, outer_core, lower_mantle, upper_mantle, crust, atmosphere, upper_atmosphere, hill_sphere | magnetosphere, van_allen_belts, leo, geostationary_belt | Several per custom |
| Jupiter | core, metallic_hydrogen, molecular_hydrogen, cloud_layer, upper_atmosphere, hill_sphere | rings, radiation_belts, io_plasma_torus, magnetosphere | |
| Saturn | core, metallic_hydrogen, molecular_hydrogen, cloud_layer, upper_atmosphere, hill_sphere | rings, radiation_belts, enceladus_plasma_torus, magnetosphere | |
| Uranus | core, mantle, cloud_layer, upper_atmosphere, hill_sphere | rings (97.77 deg tilt), radiation_belts, magnetosphere | |
| Neptune | core, mantle, cloud_layer, upper_atmosphere, hill_sphere | rings, radiation_belts, plasma, magnetosphere | |

Earth special note: 11 inline `CreateToolTip(earth_*_checkbutton, earth_*_info)` calls in `palomas_orrery.py` (Path A). These bypass `build_shell_checkboxes`. In Phase C they can be either:

(a) Left alone (the `earth_*_info` strings still exist in shell files until Phase D cleanup); OR
(b) Updated to read from `SHELL_CONFIGS['Earth'][shell]['tooltip']` directly.

Recommend (b) for consistency, but (a) is acceptable if Phase C is getting too large to chunk in one session.

Cloud_layer functions (Jupiter, Saturn, Uranus, Neptune) are Mesh3d like the crusts — same conversion treatment.

After Phase C, only Sun and asteroid belts remain to migrate, plus the `_info` import chain cleanup.

### Phase D — Sun + asteroid belts + cleanup

#### Sun migration

Sun has 15 sphere shells with absolute radii (AU), not radius_fraction. The `build_sphere_shell()` function already supports `radius_au` (defined in Phase A). Each Sun shell config uses `radius_au` instead of `radius_fraction`. Other fields identical to Mercury template.

Sun also has 3 custom geometry functions (Hills Cloud torus, Outer Oort clumpy, Galactic Tide) — CUSTOM_SHELLS entries.

Update `create_celestial_body_visualization()` to handle Sun's bare-key shell_vars without prefix stripping. The prefix-strip line in Section 6.3 already handles this gracefully: `key.startswith(body_prefix)` is False for Sun's bare keys, so `shell_name = key` (no change). Already correct in Phase A — no code change needed.

Retire `create_sun_visualization()`. Two call sites in `palomas_orrery.py`:

Line ~4509:
```python
fig = create_sun_visualization(fig, sun_shell_vars)
```
Replace with:
```python
fig = create_celestial_body_visualization(
    fig, 'Sun', sun_shell_vars,
    object_type='Sun', center_object=center_object_name,
)
```

Line ~6144: same pattern.

Then delete the body of `create_sun_visualization` in `planet_visualization.py` (keep the function as a one-line wrapper that delegates, OR remove entirely if no other callers).

#### Asteroid belts

Asteroid belts have no sphere shells — only 4 custom geometry functions (main belt, hildas, Greeks, Trojans). Add a CUSTOM_SHELLS entry under a body name like `'Asteroid Belts'`, or treat them as part of the Sun's CUSTOM_SHELLS. Tony's call. The current code has them under their own GUI section with direct imports — easiest path is to leave them as-is but register them in CUSTOM_SHELLS so the dispatch mechanism supports them when needed.

Asteroid belt inline tooltips (4 calls in `palomas_orrery.py`) get updated to read from CUSTOM_SHELLS like Earth's inline calls in Phase C.

#### Comets

Comets are runtime objects, not GUI-toggled shells. They don't fit either registry naturally. Leave the comet shell code alone — it's already invoked from `add_comet_tails_to_figure()` outside the body dispatch.

#### _info import chain cleanup

After all bodies are migrated:

1. **`palomas_orrery_helpers.py`**: Delete all 87 `_info` imports (lines ~53-158). These were never consumed - pure dead code. Convert file from CRLF to LF as part of this cleanup.
2. **`palomas_orrery.py`**: Delete the 89 `_info` imports (lines ~100-164). Replace with one line:
   ```python
   from shell_configs import SHELL_CONFIGS, CUSTOM_SHELLS
   ```
3. **`planet_visualization.py`**: Remove the `_info` items from each shell-file import statement (lines ~90-300). Keep the function imports. The shell file modules will eventually be archived (Phase B bodies) or pruned (Phase C/D bodies).
4. **`celestial_objects.py`**: Update `build_shell_checkboxes()` to read tooltips from `SHELL_CONFIGS` and `CUSTOM_SHELLS` instead of `globals()`:

   ```python
   def build_shell_checkboxes(body_name, parent_frame, vars_dict, tooltips_dict, tk_module, CreateToolTip):
       if body_name not in SHELL_DEFINITIONS:
           return None
       shells = SHELL_DEFINITIONS[body_name]
       body_prefix = body_name.lower().replace(' ', '')

       # NEW: read tooltips from configs, not globals
       sphere_configs = SHELL_CONFIGS.get(body_name, {})
       custom_configs = CUSTOM_SHELLS.get(body_name, {})

       shell_frame = tk_module.Frame(parent_frame)
       shell_frame.pack(padx=(20, 0), anchor='w')

       for shell in shells:
           var_name = "%s_%s_var" % (body_prefix, shell['var_suffix'])
           var = vars_dict.get(var_name)
           if var is None:
               continue
           # Look up tooltip in sphere configs, then custom configs, then fallback
           tooltip_text = (
               sphere_configs.get(shell['var_suffix'], {}).get('tooltip')
               or custom_configs.get(shell['var_suffix'], {}).get('tooltip')
               or "No information available"
           )
           cb = tk_module.Checkbutton(shell_frame, text=shell['label'], variable=var)
           cb.pack(anchor='w')
           CreateToolTip(cb, tooltip_text)

       return shell_frame
   ```
   The `tooltips_dict` parameter becomes unused — keep it in the signature for backward compatibility, or remove and update the 9 call sites in `palomas_orrery.py`.

5. **Inline CreateToolTip calls** (~33 sites in `palomas_orrery.py`): Update each to read from configs.

   Pattern - find:
   ```python
   CreateToolTip(earth_inner_core_checkbutton, earth_inner_core_info)
   ```
   Replace with:
   ```python
   CreateToolTip(earth_inner_core_checkbutton, SHELL_CONFIGS['Earth']['inner_core']['tooltip'])
   ```

   Same pattern for Sun (`SHELL_CONFIGS['Sun'][shell]['tooltip']`) and asteroid belts (`CUSTOM_SHELLS['Asteroid Belts'][shell]['tooltip']` or wherever they end up registered).

6. **Retire `create_planet_visualization()` and `create_sun_visualization()`**: After all bodies delegate in their if/elif blocks, every block becomes a one-line `return create_celestial_body_visualization(...)`. At that point the wrapper functions add no value. Update the 6 call sites in `palomas_orrery.py` to call `create_celestial_body_visualization` directly, then delete the two wrapper functions from `planet_visualization.py`.

7. **Retire the `create_sun_direction_indicator` alias**: After all shell files are migrated or archived, no callers of the old name remain. Delete the alias line at the bottom of `shared_utilities.py`.

8. **Archive Phase B bodies' shell files**: Move `pluto_visualization_shells.py`, `planet9_visualization_shells.py`, `eris_visualization_shells.py`, `moon_visualization_shells.py` to an `archive/` directory. Remove their imports from `planet_visualization.py`.

After Phase D, the codebase is fully consolidated: one dispatch function, one builder, one config file, no _info import chain, no per-shell indicator duplication.

---

## 10. Decision Log and Notes

### Decisions deferred to implementing Claude

1. **Tooltip text for Mercury magnetosphere** (Section 4.3). Manifest contains a placeholder; implementing Claude extracts the exact `mercury_magnetosphere_info` string from `mercury_visualization_shells.py` (line ~600) and substitutes it.

2. **CENTER_BODY_RADII import in planet_visualization.py** (Section 6.3). Add the import if not already present. Should already be there since other parts of the file use planet radii.

3. **Asteroid belt registration name** (Phase D). Tony's call: `'Asteroid Belts'` as its own SHELL_CONFIGS top-level key, or fold into `'Sun'` CUSTOM_SHELLS? Recommend top-level for symmetry with future Ceres/Vesta entries.

### Decisions made by this manifest

1. **build_sphere_shell location**: `orrery_rendering.py` not standalone. Matches the architecture spec.
2. **n_points default**: 20 (matches Step 2 default for boundary shells; interior shells use 25 per-config).
3. **Info marker placement**: north pole at `r * 1.05`. Locked in Step 2; carries forward unchanged.
4. **Backward-compat alias for create_sun_direction_indicator**: kept through all phases until the last shell file callers are migrated or archived. Removed in Phase D as the final cleanup step.
5. **Mercury sphere shells in mercury_visualization_shells.py left in place after Phase A**: become unreachable from dispatch but not deleted. Cleanup in Phase B (Mercury can't be archived since it has custom geometry).
6. **Mesh3d to Scatter3d conversion**: pre-decided in prompt. No `geometry_type` field in configs — the builder is sphere-only by design (structural enforcement of single info marker pattern).
7. **Indicator scale**: outermost active shell radius. If no sphere shells active (hypothetical edge case), no indicator emitted.

### Open items for future phases (NOT Phase A scope)

- **`create_sun_corona_from_distance()` in planet_visualization.py**: position-dependent corona scaling. Not in any registry. Phase D should evaluate whether it needs to migrate or stays as a special-case function.
- **`create_complete_comet_visualization()`**: orchestrator for comet runtime objects. Not part of the dispatch. Out of scope.
- **GUI checkbox vars**: `palomas_orrery.py` defines all `*_var` tk.IntVar instances at module scope. No changes needed — the new dispatch reads them the same way.

### Risks and mitigations

| Risk | Mitigation |
|------|-----------|
| Mercury crust visual regression (Mesh3d to Scatter3d) | Mode 5 visual check by Tony; revert path documented above |
| Other bodies break due to imports change | Phase A imports are additive; existing imports untouched |
| Indicator appears twice for Mercury | Section 7 strips all 3 internal calls; dispatch loop emits exactly one |
| CRLF reintroduction in planet_visualization.py | Verify with `file` after every edit pass |
| Mercury custom shells (sodium_tail, magnetosphere) silently broken by lazy import | Smoke test in Section 8.2 imports SHELL_CONFIGS and CUSTOM_SHELLS but does NOT call the builders (no GUI context) - the real test is Section 8.3 visual render |

### Implementation discipline (per protocol)

- Python binary mode (`rb`/`wb`) for all file reads/writes
- Bottom-up editing when modifying a file multiple times
- Exact-string matching, never regex
- One section at a time; run syntax check before proceeding
- Credit line update: `Module updated: May 2026 with Anthropic's Claude Opus 4.7` on every modified file
- ASCII only in all new files; verify with `grep -P '[^\x00-\x7F]'`
- If a value can't be confirmed from the uploaded files, STOP and ask Tony

---

## 11. Workflow Provenance

This manifest:
- Audited by Anthropic's Claude Opus 4.7
- From prompt v2 by Tony Quintanilla + Anthropic's Claude Opus 4.6
- Following protocol v3.22 (collegial Mode 7)

To be executed by: Anthropic's Claude Opus 4.6 + Tony, in a separate session.

The single info marker manifest set the quality bar. Aim for the same level of precision here: every conversion site identified, every value extracted exactly, every judgment call flagged.

*Module updated: May 2026 with Anthropic's Claude Opus 4.7*
