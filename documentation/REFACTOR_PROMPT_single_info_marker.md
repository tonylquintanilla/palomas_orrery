# Single Info Marker Refactor — Opus 4.7 Prompt

## Objective

Refactor all **uniform geometry** traces in Paloma's Orrery to use the **single info marker pattern**. This eliminates duplicated hover text on multi-point visual traces (shells, osculating ellipses, particle clouds), replacing N copies of identical text with `hoverinfo='skip'` on the geometry and one cross (+) marker carrying the text exactly once.

**Do NOT touch trajectory data** — Horizons ephemeris traces where each point has unique date/distance/velocity hover text. Those stay as-is.

## Decision Rule

**Convert** if the trace duplicates identical text across all points:
```python
# BEFORE — same string repeated N times (CONVERT THIS)
text=[hover_text] * len(x)
customdata=[hover_text] * len(x)
```

**Leave alone** if each point has unique text (dates, positions, velocities):
```python
# TRAJECTORY — unique per point (DO NOT TOUCH)
text=[f"Date: {d}<br>Dist: {r:.3f} AU" for d, r in zip(dates, distances)]
```

**Also leave alone**: Single-point markers — `text=[hover_text]` without `* len(...)` — are correct as-is. They already carry one hover string for one point.

### Discovery — patterns the primary grep misses

The literal `text=[x] * len(y)` catches ~95 instances. Three equivalent patterns produce the same duplication but use different syntax:

**Pattern A — Multi-line string with `* len(x)` on a separate line:**
Saturn magnetosphere (~line 625-629), and similar in jupiter/neptune/uranus. The `text=[` opens, a multi-line concatenated string spans several lines, then `] * len(x)` closes. A single-line grep misses the split.

**Pattern B — Intermediate variable with list comprehension:**
```python
text_array = [ring_info['description'] for _ in range(len(x))]
...
text=text_array,
```
Used in ring generation functions (Saturn, Jupiter, Neptune, Uranus). Same duplication, different syntax.

**Pattern C — `hover_text` list built outside the trace, then passed in:**
```python
hover_text = [f"{name} Orbit"] * len(path['x'])
...
text=hover_text,
customdata=hover_text,
```
orbit_data_manager.py lines ~1575, 1578, 1613. The `text=` line itself looks clean.

**Pattern D — 1-element list variable multiplied at the trace line:**
```python
magnetosphere_text = ["Earth's magnetosphere extends about 10 Earth radii..."]  # 1-element list
magnetosphere_customdata = ['Earth: Magnetosphere']                              # 1-element list
...
text=magnetosphere_text * len(x),         # [item] * N — same duplication
customdata=magnetosphere_customdata * len(x),
```
No `[` immediately after `text=`, so the primary grep misses it. Used systematically for magnetospheres, bow shocks, plasma tori, radiation belts, and crustal field traces across most inner planets.

**Discovery strategy**: After the primary grep, also search for any list variable that flows into a `text=` parameter where the list was constructed with `* len(...)` or `for _ in range(len(...))` anywhere in the same function. The per-module counts below include all four patterns (~129 total).

**Verification grep** (run after manifest is complete to confirm nothing was missed):
```bash
# Pattern A/B/C/D — any duplication that flows into a trace
grep -nE "text=\[.*\] \* (len|n_points)|customdata=\[.*\] \* (len|n_points)" *.py
grep -nE "text=[a-z_]+ \* len\(|customdata=[a-z_]+ \* len\(" *.py
grep -nE "_text = \[|_customdata = \[|text_array = \[|hover_text = \[|hover_customdata = \[" *.py

# False-positive filter — exclude lines+text label trick
grep -nE "mode=['\"]lines\+text['\"]" *.py
```

## The Pattern

### BEFORE (anti-pattern — duplicates text on every geometry point):
```python
def create_earth_outer_core_shell(center_position=(0, 0, 0)):
    layer_radius = 0.55 * EARTH_RADIUS_AU
    x, y, z = create_sphere_points(layer_radius, n_points=50)
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z

    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(size=4.0, color='rgb(255, 140, 0)', opacity=0.8),
            name="Earth: Outer Core",
            text=[description] * len(x),          # <-- 50 copies
            customdata=["Earth: Outer Core"] * len(x),  # <-- 50 copies
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    ]
    return traces
```

### AFTER (single info marker pattern):
```python
def create_earth_outer_core_shell(center_position=(0, 0, 0)):
    layer_radius = 0.55 * EARTH_RADIUS_AU
    x, y, z = create_sphere_points(layer_radius, n_points=20)  # reduced from 50
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    r_info = layer_radius * 1.05  # north pole, 5% above shell

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(size=4.0, color='rgb(255, 140, 0)', opacity=0.8),
        name="Earth: Outer Core",
        legendgroup="Earth: Outer Core",
        hoverinfo='skip',                         # <-- no hover on geometry
        showlegend=True
    )
    info_trace = go.Scatter3d(
        x=[center_x], y=[center_y], z=[center_z + r_info],
        mode='markers',
        marker=dict(size=6, color='rgb(255, 140, 0)', opacity=0.9,
                    symbol='cross', line=dict(color='white', width=1)),
        name='',
        legendgroup="Earth: Outer Core",           # <-- toggles with shell
        text=[description],
        customdata=["Earth: Outer Core"],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    )
    return [shell_trace, info_trace]
```

### OSCULATING ORBIT ELLIPSE (line trace variant):
```python
# BEFORE
fig.add_trace(go.Scatter3d(
    x=x_final, y=y_final, z=z_final,
    mode='lines',
    line=dict(color=color, width=2, dash='dash'),
    name=f'{name} Osculating Orbit (Epoch: {epoch})',
    text=[hover_text_osc] * len(x_final),       # <-- 360+ copies
    customdata=[hover_text_osc] * len(x_final),
    hovertemplate='%{text}<extra></extra>',
    showlegend=True
))

# AFTER — geometry trace + info marker
orbit_name = f'{name} Osculating Orbit (Epoch: {epoch})'
fig.add_trace(go.Scatter3d(
    x=x_final, y=y_final, z=z_final,
    mode='lines',
    line=dict(color=color, width=2, dash='dash'),
    name=orbit_name,
    legendgroup=orbit_name,
    hoverinfo='skip',
    showlegend=True
))
# Info marker at a visually clear point (avoid perihelion crowding)
info_idx = min(len(x_final) // 2, len(x_final) - 1)  # midpoint of arc
fig.add_trace(go.Scatter3d(
    x=[x_final[info_idx]], y=[y_final[info_idx]], z=[z_final[info_idx]],
    mode='markers',
    marker=dict(size=6, color=color, opacity=0.9,
                symbol='cross', line=dict(color='white', width=1)),
    name='',
    legendgroup=orbit_name,
    text=[hover_text_osc],
    customdata=[orbit_name],
    hovertemplate='%{text}<extra></extra>',
    showlegend=False
))
```

## Source Files

The project files at `/mnt/project/` are confirmed current as of this session. Use them as the authoritative base for all line references and code inspection. No uploads supersede them for this task.

## Scope — ~129 instances across 19 modules

### Priority 1: Shell modules (14 unconverted + 2 partially converted)

| Module | Instances | Notes |
|--------|-----------|-------|
| earth_visualization_shells.py | 13 | Has center_position offset. +4 Pattern D: magnetosphere, bow shock, Van Allen belts loop (runs 2x) |
| saturn_visualization_shells.py | 9 | Includes magnetosphere (Pattern A), ring traces (Pattern B), Enceladus plasma torus + plasma belts loop (Pattern C) |
| mars_visualization_shells.py | 9 | Has center_position offset. +3 Pattern D: magnetosphere, bow shock, crustal fields |
| mercury_visualization_shells.py | 8-9 | Has center_position offset. +2-3 Pattern D: magnetosphere, bow shock, possibly Hill Sphere |
| jupiter_visualization_shells.py | ~9 | Ring traces (Pattern B), Io plasma torus (Pattern C), radiation belts loop (Pattern C) |
| neptune_visualization_shells.py | ~8 | Ring traces (Pattern B), magnetosphere + belts loop + plasma hover (Pattern C/D) |
| venus_visualization_shells.py | 7 | Has center_position offset. +2 Pattern D: magnetosphere, bow shock |
| moon_visualization_shells.py | 5 | Has center_position offset. Uses existing two-trace structure (surface_trace + hover_trace) — conversion = reduce hover_trace from 50 fibonacci points to 1 info marker |
| uranus_visualization_shells.py | ~6 | Ring traces (Pattern B), belts loop (Pattern C) |
| comet_visualization_shells.py | 5 | Ghost tail done — coma, dust tail, ion tail, anti-tail remain |
| pluto_visualization_shells.py | 5 | |
| eris_visualization_shells.py | 4 | |
| asteroid_belt_visualization_shells.py | 4 | Pattern C: Main Belt, Hilda Family, Jupiter Trojans L4 (Greeks), L5 (Trojans). Particle-cloud traces — use representative-point-within-cloud rule |
| solar_visualization_shells.py | 4 | Oort Cloud section only — inner shells already done |
| planet9_visualization_shells.py | 1 | |

### Priority 2: Orbit generators

| Module | Instances | Notes |
|--------|-----------|-------|
| idealized_orbits.py | 24 | LARGEST — osculating ellipses, rotation transforms. Must distinguish uniform from trajectory. Some `text=[label] * len(x)` are simple labels, not long descriptions — still convert but lower impact |
| orbit_data_manager.py | 3 | Pattern C — hover_text list built outside trace at lines ~1575, 1578, 1613 |

### Priority 3: Singletons

| Module | Instances | Notes |
|--------|-----------|-------|
| shared_utilities.py | 1 | |
| planet_visualization_utilities.py | 1 | |
| palomas_orrery.py | 1 | |

## Conversion Rules

1. **Shell geometry traces**: Add `hoverinfo='skip'`, remove `text=` and `customdata=` arrays, add `legendgroup=`
2. **Info marker position** (by geometry type):
   - **Sphere shells**: north pole at `r * 1.05` (z-axis, above ecliptic plane)
   - **Sphere shells with `center_position` offset**: `(center_x, center_y, center_z + r * 1.05)`
   - **Rings** (Saturn, Jupiter, Neptune, Uranus): place marker ON the ring at a fixed azimuth (phi=0), at the outer radius, rotated through the planet's axial tilt if applicable. Do NOT use north-pole-at-r*1.05 — that puts the marker in empty space far from ring geometry
   - **Thick particle shells** (Earth LEO, Hill Sphere): use the OUTER radius of the radial distribution * 1.05, not the inner radius
   - **Magnetosphere** (Saturn): pick a representative point on the dayside/bow-shock direction, not a geometric north pole — the magnetosphere is asymmetric
   - **Line traces** (osculating orbits, arcs): midpoint of arc or index chosen to avoid crowded regions (perihelion, close-approach)
   - **Particle clouds** (coma, tails): representative position within the cloud extent
3. **Info marker style**: `symbol='cross'`, `size=6`, `opacity=0.9`, `line=dict(color='white', width=1)` — match the shell/trace color for the marker fill
4. **legendgroup**: Both geometry trace and info marker share the same legendgroup string so they toggle together. The geometry trace has `showlegend=True`, the info marker has `showlegend=False`
5. **n_points reduction**:
   - **Boundary/atmosphere shells** (Oort Cloud, heliopause, magnetosphere, Hill Sphere): reduce to `n_points=20`
   - **Interior anatomy shells** (planet cores, mantles, crusts): reduce to `n_points=25` — surface texture reads better at slightly higher density
   - Do NOT change n_points on traces already at 20-25
   - **Escape hatch**: If a shell at 20-25 points might be visually too sparse at orrery scale, flag the case in the manifest with a recommendation rather than reducing blindly. This is a visual judgment the operator will make after rendering
6. **Return value**: Functions that returned `[trace]` now return `[shell_trace, info_trace]`. Callers in shell modules extend these into trace lists — this is safe. For `idealized_orbits.py` and `orbit_data_manager.py`, the pattern is `fig.add_trace()` — add a second `fig.add_trace()` for the info marker. Verify any caller patterns in `palomas_orrery.py` that wrap shell function returns
7. **customdata on info marker**: Use the trace name string (for legend identification in downstream tools), NOT the full hover text. For `shared_utilities.py` and `planet_visualization_utilities.py` where the original has no `customdata=` duplication, the info marker can carry only the name string or omit customdata
8. **Credit line**: Update the module docstring credit to: `Module updated: May 2026 with Anthropic's Claude Opus 4.7`

## Reference Implementations (already converted)

Study these files for the established pattern:
- `solar_visualization_shells.py` — lines 960-1000 (inner shells, canonical example)
- `comet_visualization_shells.py` — ghost tail section (line trace variant with legendgroup)
- `star_sphere_builder.py` — coordinate grid markers use cross symbol

## What NOT to Change

- **Trajectory traces** with per-point unique data (dates, distances, velocities)
- **Body position markers** (single-point markers for planets, moons, spacecraft) — these already have exactly one hover text
- **Star background dots** (`hoverinfo='skip'` already, unless Star Names toggle is on)
- **Coordinate grid traces** in star_sphere_builder.py (already converted)
- **Lines+text label traces**: `mode='lines+text'` with `text=[''] * (N-1) + [label]` puts a single visible label at the end of a line (orbital_param_viz.py has 4 of these). The text array contains unique values per position even though most are empty. Leave alone. Hover behavior here is controlled by `hovertemplate`, not by the text array
- **Any trace where removing per-point hover would lose unique information**

## Encoding

- Use Python binary mode (rb/wb) for all file edits to preserve line endings (some files are CRLF, some LF)
- ASCII only in code — no Unicode characters (degree symbol = `deg`, not `°`)
- Edit bottom-up (highest line numbers first) if making multiple manual edits

## Deliverable

Do NOT return complete refactored files. Return a **manifest with targeted snippets** for each module.

### Per-module manifest format:

```
### module_name.py (N instances converted)

#### 1. function_name() — line ~NNN
BEFORE:
```python
text=[hover_text] * len(x),
customdata=["Label"] * len(x),
hovertemplate='%{text}<extra></extra>',
showlegend=True
```

AFTER (replace the trace creation block at line ~NNN):
```python
legendgroup="Label",
hoverinfo='skip',
showlegend=True
```

ADD after the geometry trace:
```python
info_trace = go.Scatter3d(
    x=[center_x], y=[center_y], z=[center_z + r_info],
    ...
)
```

ALSO CHANGE (if applicable):
- n_points=50 -> n_points=20 (line ~NNN)
- Return value: was [trace], now [shell_trace, info_trace]

JUDGMENT CALL (if any): "Short label, low impact, but converted for pattern consistency"
```

### Final summary:
- Total instances converted vs skipped
- Instances skipped with reason (trajectory data, ambiguous, etc.)
- Estimated file size impact per module (points x hover-text-length x 2 for text+customdata, before vs after)
- Estimated aggregate savings on a fully-rendered all-shells-on orrery HTML export
- Any functions where the conversion is non-obvious or risky

### Rules for snippets:
- Include enough surrounding context (function name, nearby landmarks) to locate the edit unambiguously
- Use approximate line numbers (the base file may have shifted)
- Flag any case where the return value changes shape (list length) — callers may need updating
- If a function has a center_position parameter, show the info marker coordinates explicitly — this is the most error-prone part
