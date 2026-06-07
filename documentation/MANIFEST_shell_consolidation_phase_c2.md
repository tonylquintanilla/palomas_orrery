# MANIFEST: Shell Consolidation Step 3 -- Phase C2 (Earth)

**Project:** Paloma's Orrery | Plotting Consolidation Step 3
**Date:** May 15, 2026
**Source prompt:** `PROMPT_shell_consolidation_for_opus_v4.md` (Earth-only)
**Phase C1 handoff:** `HANDOFF_shell_consolidation_phase_c1.md` (May 15, 2026)
**Manifest by:** Anthropic's Claude Opus 4.7 (audit)
**For execution by:** Anthropic's Claude Opus 4.6 (implementation) + Tony (integrator)

---

## 1. Phase C2 Scope and Execution Model

### What Phase C2 delivers

Earth is the eighth body migrated to the unified config-driven dispatch and the most complex single-body migration. The work is a clear extension of the Phase C1 Venus/Mars pattern, with one notable expansion: Earth's magnetosphere builder emits FOUR trace groups (magnetosphere, bow shock, Inner Radiation Belt, Outer Radiation Belt) instead of two or three, and the Van Allen radiation belts are intentionally fused inside the magnetosphere builder per Tony's decision.

After Phase C2:

- **Earth** renders via `SHELL_CONFIGS['Earth']` (8 sphere shells, including mesh3d crust) and `CUSTOM_SHELLS['Earth']` (3 entries: magnetosphere, leo, geostationary_belt).
- The Earth magnetosphere builder gets `rotate_to_sunward()` calls added for the magnetosphere and bow shock geometry. The Van Allen radiation belts are NOT rotated (geomagnetic-axis-anchored, same precedent as Mars crustal fields).
- Four old-style info markers in the magnetosphere builder (magnetosphere, bow shock, inner belt, outer belt) are replaced with `create_info_marker()` calls.
- Two old-style info markers in LEO and GEO builders are replaced.
- Three per-shell `create_sun_direction_indicator` calls are removed (upper_atmosphere, magnetosphere, hill_sphere). The unified dispatch handles one indicator per body.
- Earth's dispatch block in `planet_visualization.py` is replaced with a one-line delegation.

After Phase C2:

| Component | Before C2 | After C2 |
|---|:---:|:---:|
| Bodies in SHELL_CONFIGS | 7 | 8 |
| Total sphere shell configs | 38 | 46 |
| Bodies in CUSTOM_SHELLS | 3 | 4 |
| Total custom entries | 4 | 7 |
| Bodies still on old dispatch | 6 | 5 |

Five bodies remain on the old dispatch path after C2 (Jupiter, Saturn, Uranus, Neptune, Sun). Phase C3 tackles Jupiter; C4 finishes the gas giants.

### What Phase C2 explicitly does NOT do

- Does NOT split Van Allen belts into separate CUSTOM_SHELLS entries. Tony's decision: fuse them inside the magnetosphere builder (Option A), matching Mars's crustal-fields precedent. One CUSTOM_SHELLS entry = one builder; the builder is free to emit multiple trace groups.
- Does NOT add new GUI toggles. Earth's existing `earth_magnetosphere_var` controls all four magnetosphere-related trace groups (status quo preserved).
- Does NOT add an ionosphere shell. There is no `create_earth_ionosphere_shell` function in the source. The `create_earth_upper_atmosphere_shell` covers the thermosphere/exosphere region. Earth has 8 sphere shells, not 9.
- Does NOT rewire Earth's tooltip wiring. Earth uses Path A (inline `CreateToolTip` calls in `palomas_orrery.py`). Phase D handles tooltip wiring cleanup as a batch operation. The `_info` strings in `earth_visualization_shells.py` remain.
- Does NOT modify `earth_visualization_shells.py` sphere shell functions. They become unreachable from the dispatch but stay in place; their custom geometry siblings (magnetosphere, LEO, geostationary_belt) still live in the same file. Phase D decides per-function fate.
- Does NOT touch `palomas_orrery.py`. Earth's GUI checkboxes and shell_vars wiring continue working through the unified dispatch (which iterates `shell_vars` for the body).
- Does NOT retire `create_planet_visualization()`. Five bodies still use it (Jupiter, Saturn, Uranus, Neptune, plus Sun via separate function). Phase D retires it.

### Execution order (canonical)

C2 has five top-level sections, executed in this order. Each section is atomic. Run the syntax check at the end of each section before starting the next.

1. **Pre-flight verification** (Section 2)
2. **Earth sphere configs** (Section 3) -- auto-generation script + insertion
3. **Earth magnetosphere refactor** (Section 4) -- the most substantive code change in C2
4. **LEO + GEO refactor + CUSTOM_SHELLS entries + delegation** (Section 5)
5. **Verification plan** (Section 6)

If any step fails its syntax check, STOP and resolve before proceeding.

### Why this order matters

Section 3 (sphere shells) is mechanical and matches the Phase C1 pattern -- a confidence-building first section. Section 4 (magnetosphere) is the largest single code change: adds rotation, replaces 4 info markers, removes 1 sun indicator call, plus the CUSTOM_SHELLS entry. Doing it alone makes it easier to verify visually (turn on just Magnetosphere, see if rotation works). Section 5 finishes off the simpler LEO and GEO builders plus the delegation edit; these are quick once the magnetosphere pattern is settled.

If context pressure builds, implementing Claude can stop after any section -- the codebase remains functional at each section boundary. Section 3 alone leaves Earth's sphere shells in SHELL_CONFIGS but Earth's dispatch still uses the old path (custom geometry not yet refactored). Section 4 alone makes the magnetosphere render correctly through the new path but still requires the old dispatch block to be replaced in Section 5.

A clean session boundary exists between Section 4 and Section 5: after Section 4, write a partial handoff describing what's still needed.

---

## 2. Pre-flight Verification

### 2.1 Confirm Phase A+B+C1 are in place

```bash
python3 -c "
from orrery_rendering import build_sphere_shell, create_info_marker, rotate_to_sunward
from shell_configs import SHELL_CONFIGS, CUSTOM_SHELLS

# Phase A+B+C1 baseline
expected_sphere = {'Mercury', 'Moon', 'Planet 9', 'Pluto', 'Eris', 'Venus', 'Mars'}
expected_custom = {'Mercury', 'Venus', 'Mars'}

for body in expected_sphere:
    assert body in SHELL_CONFIGS, 'Phase A/B/C1 body %s missing from SHELL_CONFIGS' % body
for body in expected_custom:
    assert body in CUSTOM_SHELLS, 'Phase C1 custom body %s missing from CUSTOM_SHELLS' % body

# Spot checks
assert 'Earth' not in SHELL_CONFIGS, 'Earth already present - re-run?'
assert 'Earth' not in CUSTOM_SHELLS, 'Earth already in CUSTOM_SHELLS - re-run?'

print('Phase A+B+C1 baseline OK')
print('SHELL_CONFIGS:', sorted(SHELL_CONFIGS.keys()))
print('CUSTOM_SHELLS:', sorted(CUSTOM_SHELLS.keys()))
"
```

If anything fails, STOP -- Phase C2 assumes Phase A+B+C1 are complete and consistent.

### 2.2 Confirm source file is post-Step-2

```bash
grep "Module updated" /path/to/earth_visualization_shells.py
# Expected: "May 2026 with Anthropic's Claude Opus 4.7"

grep -c "hoverinfo='skip'" /path/to/earth_visualization_shells.py
# Expected: at least 11 (one per geometry trace including the 4 inside magnetosphere)

file /path/to/earth_visualization_shells.py
# Expected: ASCII text, no CRLF
```

If the file lacks the May 2026 credit, the `hoverinfo='skip'` markers, or has CRLF endings, STOP -- the file is not the post-Step-2 baseline.

### 2.3 Confirm Earth's structure matches expectations

```bash
grep -c "^def create_" /path/to/earth_visualization_shells.py
# Expected: 11

grep "^def create_" /path/to/earth_visualization_shells.py
# Expected order:
#   create_earth_inner_core_shell
#   create_earth_outer_core_shell
#   create_earth_lower_mantle_shell
#   create_earth_upper_mantle_shell
#   create_earth_crust_shell
#   create_earth_atmosphere_shell
#   create_earth_upper_atmosphere_shell
#   create_earth_magnetosphere_shell
#   create_earth_leo_shell
#   create_earth_geostationary_belt_shell
#   create_earth_hill_sphere_shell
```

If function count or names differ, STOP. The v4 prompt's inventory had errors that have been corrected; the manifest assumes the actual 11 functions in the actual order.

### 2.4 Confirm CENTER_BODY_RADII has Earth

```bash
python3 -c "
from constants_new import CENTER_BODY_RADII, KM_PER_AU
print('Earth radius: %.2f km = %.4e AU' % (CENTER_BODY_RADII['Earth'], CENTER_BODY_RADII['Earth']/KM_PER_AU))
"
# Expected: ~6378.14 km = ~4.2635e-05 AU
```

If Earth is missing from `CENTER_BODY_RADII`, STOP -- `build_sphere_shell` requires it.

### 2.5 Confirm Earth's dispatch block is present in planet_visualization.py

```bash
grep -n "if planet_name == 'Earth':" /path/to/planet_visualization.py
# Expected: one occurrence, returning a multi-line if/elif chain

sed -n '/if planet_name == .Earth.:/,/^    if planet_name == /p' /path/to/planet_visualization.py | head -25
# Expected: 11 shell-toggle if-statements (inner_core through geostationary_belt)
```

The dispatch block has all 11 shell toggles. Phase C2 replaces it with a one-line delegation.

### 2.6 Backup files Phase C2 will touch

Before any edits:

```
shell_configs.py                    -> shell_configs.py.phaseC2_backup
planet_visualization.py             -> planet_visualization.py.phaseC2_backup
earth_visualization_shells.py       -> earth_visualization_shells.py.phaseC2_backup
```

Three files. No changes to `palomas_orrery.py` in C2 -- the dispatch routes everything through the existing `shell_vars` dict.

### 2.7 Line ending and ASCII verification

```bash
for f in shell_configs.py planet_visualization.py earth_visualization_shells.py; do
    file "$f" | grep -q CRLF && echo "FAIL: $f CRLF" || echo "OK LF: $f"
done

python3 -c "
for f in ['shell_configs.py', 'planet_visualization.py', 'earth_visualization_shells.py']:
    with open(f, 'rb') as fh:
        content = fh.read().decode('utf-8', errors='replace')
    issues = sum(1 for c in content if ord(c) > 127)
    print('%-45s %s' % (f, 'OK ASCII' if not issues else 'FAIL: %d non-ASCII' % issues))
"
```

All three files must be LF and ASCII. Phase C1 cleaned the global ASCII state; if Earth's file has Unicode characters, clean them per the Phase C1 Section 3 method before proceeding.

---

## 3. Earth Sphere Configs

Earth has 8 sphere shells. Six are standard (`layer_info` dict pattern), one is mesh3d (crust), and one uses the local-variable pattern (Hill sphere). Same auto-generation approach as Phase C1: read source, generate config block, manual review before insertion.

### 3.1 Auto-generation script

Save as `generate_phase_c2_earth_configs.py` and run from the project directory:

```python
# generate_phase_c2_earth_configs.py
# Run this and review output before inserting into shell_configs.py.
# Standardizations applied:
#   - Hill sphere n_points: 30 -> 20 (matches C1 precedent)
#   - Crust geometry_type: 'mesh3d', mesh_resolution: 24
import re

N_POINTS_HILL_SPHERE = 20
GEOMETRY_TYPE_CRUST = 'mesh3d'
MESH_RESOLUTION = 24

BODY = 'Earth'
PATH = 'earth_visualization_shells.py'

# Order matches the GUI checkbox order and the body's natural physical structure
SHELLS = [
    ('inner_core',       'create_earth_inner_core_shell',       'earth_inner_core_info'),
    ('outer_core',       'create_earth_outer_core_shell',       'earth_outer_core_info'),
    ('lower_mantle',     'create_earth_lower_mantle_shell',     'earth_lower_mantle_info'),
    ('upper_mantle',     'create_earth_upper_mantle_shell',     'earth_upper_mantle_info'),
    ('crust',            'create_earth_crust_shell',            'earth_crust_info'),
    ('atmosphere',       'create_earth_atmosphere_shell',       'earth_atmosphere_info'),
    ('upper_atmosphere', 'create_earth_upper_atmosphere_shell', 'earth_upper_atmosphere_info'),
    ('hill_sphere',      'create_earth_hill_sphere_shell',      'earth_hill_sphere_info'),
]


def get_func_body(lines, fname):
    defs = []
    for i, line in enumerate(lines):
        m = re.match(r'def\s+(\w+)\s*\(', line)
        if m and not line.startswith(' '):
            defs.append((i, m.group(1)))
    for idx, (start, name) in enumerate(defs):
        if name == fname:
            end = defs[idx + 1][0] if idx + 1 < len(defs) else len(lines)
            return ''.join(lines[start:end])
    return ''


def extract_scalar(body_src, field):
    m = re.search(rf"'{field}'\s*:\s*([\d.eE+-]+|'[^']*')", body_src)
    return m.group(1).strip("'") if m else None


def extract_multiline(body_src, field):
    m = re.search(rf"'{field}'\s*:\s*\(\s*\n(.*?)\n\s*\)\s*[,\}}]", body_src, re.DOTALL)
    return m.group(1) if m else None


def extract_info_string(full_src, var_name):
    """Match both `var = (\\n    "..."` and `var = ("..."` patterns."""
    pat = re.compile(
        rf'^{var_name}\s*=\s*\(\s*(?:\n)?(.*?)\n\s*\)\s*$',
        re.DOTALL | re.MULTILINE,
    )
    m = pat.search(full_src)
    return m.group(1) if m else None


def extract_hover_text_var(body_src):
    """For Hill sphere style: hover_text = (\\n    "..."\\n)."""
    m = re.search(r'hover_text\s*=\s*\(\s*\n?(.*?)\n\s*\)\s*$', body_src, re.DOTALL | re.MULTILINE)
    return m.group(1) if m else None


def extract_local_radius_fraction(body_src):
    m = re.search(r'^\s*radius_fraction\s*=\s*([\d.eE+-]+)', body_src, re.MULTILINE)
    return m.group(1) if m else None


def extract_marker_size(body_src):
    """Inline Scatter3d marker size for the geometry trace (not the info marker)."""
    # First go.Scatter3d call's marker size
    m = re.search(r"go\.Scatter3d\([^)]*?\bmarker=dict\(\s*\n?\s*size\s*=\s*([\d.]+)", body_src, re.DOTALL)
    return m.group(1) if m else None


with open(PATH) as f:
    full_src = f.read()
with open(PATH) as f:
    all_lines = f.readlines()

out = ["    '%s': {\n" % BODY]

for shell_name, fn_name, info_var in SHELLS:
    body_src = get_func_body(all_lines, fn_name)

    rf = extract_scalar(body_src, 'radius_fraction')
    op = extract_scalar(body_src, 'opacity')
    color = extract_scalar(body_src, 'color')
    name = extract_scalar(body_src, 'name')
    description = extract_multiline(body_src, 'description')

    np_call = re.search(r"create_sphere_points\([^,]+,\s*n_points\s*=\s*(\d+)", body_src)
    np_val = int(np_call.group(1)) if np_call else None

    ms_val = extract_marker_size(body_src)

    is_mesh3d = 'go.Mesh3d' in body_src
    is_hill_sphere = (shell_name == 'hill_sphere')

    # Hill sphere uses local-variable pattern
    if rf is None and is_hill_sphere:
        rf = extract_local_radius_fraction(body_src)
        op = '0.25'
        name = 'Hill Sphere'
        description = extract_hover_text_var(body_src)
        ms_val = ms_val or '1.0'
        # Hill sphere color from inline marker
        color_inline = re.search(r"color='(rgb\([^']+\))'", body_src)
        if color_inline:
            color = color_inline.group(1)

    tooltip = extract_info_string(full_src, info_var)

    out.append(f"\n        '{shell_name}': {{\n")
    out.append(f"            'name': '{name}',\n")
    out.append(f"            'radius_fraction': {rf},\n")
    out.append(f"            'color': '{color}',\n")
    out.append(f"            'opacity': {op},\n")

    if is_mesh3d:
        out.append(f"            'geometry_type': 'mesh3d',\n")
        out.append(f"            'mesh_resolution': {MESH_RESOLUTION},\n")
    else:
        effective_np = N_POINTS_HILL_SPHERE if is_hill_sphere else np_val
        out.append(f"            'n_points': {effective_np},\n")
        out.append(f"            'marker_size': {ms_val},\n")

    if description:
        out.append(f"            'hover_text': (\n")
        for line in description.split('\n'):
            stripped = line.lstrip()
            if stripped:
                out.append(f"                {stripped}\n")
        out.append(f"            ),\n")
    else:
        out.append(f"            'hover_text': '',  # MISSING -- investigate\n")

    if tooltip:
        out.append(f"            'tooltip': (\n")
        for line in tooltip.split('\n'):
            stripped = line.lstrip()
            if stripped:
                out.append(f"                {stripped}\n")
        out.append(f"            ),\n")
    else:
        out.append(f"            'tooltip': '',  # MISSING -- investigate\n")

    out.append(f"        }},\n")

out.append("    },\n")

print('# Generated by generate_phase_c2_earth_configs.py')
print('# Review carefully before inserting into shell_configs.py')
print('# Place inside SHELL_CONFIGS dict after the Mars block.')
print()
print(f"    # ============================================================")
print(f"    # Earth")
print(f"    # ============================================================")
print(f"    # Source: USGS Interior of the Earth, NASA Earth Fact Sheet,")
print(f"    #         NOAA / NCEI (atmosphere boundaries), NASA Goddard,")
print(f"    #         NASA Van Allen Probes, NASA Solar System Dynamics.")
print(f"    # Verified: April 2026 provenance audit.")
print(''.join(out))
```

Run with:

```bash
python3 generate_phase_c2_earth_configs.py > phase_c2_earth_configs.txt
```

Review the output before insertion.

### 3.2 Expected values (verification reference)

The generated config should produce these values. If anything differs, STOP and investigate:

| Shell | radius_fraction | color | opacity | n_points / mesh_resolution | marker_size | name |
|---|---:|---|---:|:---:|---:|---|
| `inner_core` | 0.19 | rgb(255, 180, 140) | 1.0 | 25 | 4.0 | 'Inner Core' |
| `outer_core` | 0.55 | rgb(255, 140, 0) | 0.8 | 25 | 3.7 | 'Outer Core' |
| `lower_mantle` | 0.85 | rgb(230, 100, 20) | 0.7 | 25 | 3.4 | 'Lower Mantle' |
| `upper_mantle` | 0.98 | rgb(205, 85, 85) | 0.6 | 25 | 3.1 | 'Upper Mantle' |
| `crust` (mesh3d) | 1.0 | rgb(70, 120, 160) | 1.0 | 24 (mesh_res) | -- | 'Crust' |
| `atmosphere` | 1.05 | rgb(150, 200, 255) | 0.5 | 20 | 2.5 | 'Lower Atmosphere' |
| `upper_atmosphere` | 1.25 | rgb(100, 150, 255) | 0.3 | 20 | 2.0 | 'Upper Atmosphere' |
| `hill_sphere` | 235 | rgb(0, 255, 0) | 0.25 | 20 (was 30) | 1.0 | 'Hill Sphere' |

Notes:

1. **`atmosphere` internal name is `'Lower Atmosphere'`** -- matches Venus/Mars precedent (Phase C1 preserved 'Lower Atmosphere' from source for both). The legend will render as `"Earth: Lower Atmosphere"`. The GUI checkbox label is independent (`"-- Atmosphere"`); preserved unchanged. Tony already confirmed: preserve source values; the GUI label is what's user-visible in the checkbox panel.

2. **Hill sphere n_points: 30 -> 20** standardization, consistent with the C1 fix applied to Mercury/Venus/Mars/Planet 9 Hill spheres.

3. **Crust color `rgb(70, 120, 160)`** -- ocean blue (Earth-from-space convention). Mesh3d will render as a solid blue sphere. This is the source value; preserve.

4. **All apostrophes inside strings should be straight ASCII** (`'`), not curly Unicode. Verify in generated output.

### 3.3 Manual review checklist before inserting

Per-block, verify:

- `radius_fraction` is a float (or large int 235 for Hill sphere).
- `color` is in `'rgb(R, G, B)'` format with quoted string.
- `opacity` is a float between 0 and 1.
- Crust entry has `geometry_type='mesh3d'` and `mesh_resolution=24` (NO `n_points`, NO `marker_size`).
- All other entries have `n_points` and `marker_size`.
- Hover text contains `<br>` line breaks (HTML).
- Tooltip contains `\n` line breaks (Tkinter).
- All inner strings are ASCII -- look for em-dashes, smart quotes, degree signs.
- Hill sphere `n_points=20` (NOT 30 from source).

If any block looks wrong, STOP and resolve with Tony before inserting.

### 3.4 Insert configs into shell_configs.py

Locate the closing of the Mars block in `shell_configs.py` (the last body in SHELL_CONFIGS). The structure is:

```python
    'Mars': {
        # ... shells ...
        'hill_sphere': {
            ...
        },
    },

    # Other bodies added in Phases C, D
}
```

Insert the Earth config block BEFORE the `# Other bodies added in Phases C, D` comment. Match indentation exactly (4 spaces for top-level body keys, 8 for shell keys). The comment can stay as-is; Phase C2 adds one body, leaving Jupiter/Saturn/Uranus/Neptune/Sun for C3-D.

### 3.5 Verification after Section 3

```bash
python3 -m py_compile shell_configs.py

python3 -c "
from shell_configs import SHELL_CONFIGS
assert 'Earth' in SHELL_CONFIGS, 'Earth missing'
earth = SHELL_CONFIGS['Earth']
expected = {'inner_core', 'outer_core', 'lower_mantle', 'upper_mantle',
            'crust', 'atmosphere', 'upper_atmosphere', 'hill_sphere'}
assert set(earth.keys()) == expected, 'Earth shell keys: %s' % sorted(earth.keys())
assert earth['inner_core']['radius_fraction'] == 0.19
assert earth['hill_sphere']['radius_fraction'] == 235
assert earth['hill_sphere']['n_points'] == 20
assert earth['crust']['geometry_type'] == 'mesh3d'
assert earth['atmosphere']['name'] == 'Lower Atmosphere'

# Static smoke test - all sphere shells build without error
from orrery_rendering import build_sphere_shell
for shell_name, cfg in earth.items():
    traces = build_sphere_shell(cfg, 'Earth', (0, 0, 0))
    assert len(traces) == 2

print('Earth sphere configs verified')
"
```

If any assertion fails, STOP and fix before proceeding to Section 4.

---

## 4. Earth Magnetosphere Refactor

This is the most substantive code change in C2. The Earth magnetosphere builder currently:

1. Generates magnetosphere geometry with default `-X` sunward (no rotation).
2. Generates bow shock geometry with default `-X` sunward (no rotation).
3. Generates two Van Allen radiation belt traces using `params['inner_belt_distance']` and `params['outer_belt_distance']` -- toroidal/loop geometry around Earth's rotational axis (NOT solar-wind-anchored).
4. Calls `create_sun_direction_indicator` once at the end.
5. Uses old-style info markers (size=6, white outline, width=1) for all four trace groups.

After refactor:

1. Magnetosphere geometry: `rotate_to_sunward()` applied.
2. Bow shock geometry: `rotate_to_sunward()` applied.
3. Van Allen belts: unchanged (geomagnetic-axis-anchored, like Mars crustal fields).
4. Per-shell sun direction indicator call removed.
5. All four info markers use `create_info_marker()` (size=8, red outline, width=2).

### 4.1 Behavioral change to expect

In heliocentric views, Earth typically sits near +X (e.g. at perihelion in January). Sun-direction-from-Earth is then near `-X`, which matches the default geometry orientation, so rotation is near-identity. In flyto views centered on Earth from arbitrary angles, the magnetosphere geometry currently points wrong; after C2 it will rotate to face the actual Sun.

This is a **fix**, not a regression. The C1 Venus/Mars work established the same pattern. Tony's Mode 5 visual check on Earth flyto views is the key verification.

### 4.2 Import additions at top of file

In `earth_visualization_shells.py`, find the existing import block (after the module docstring and standard imports). Add:

```python
from orrery_rendering import rotate_to_sunward, create_info_marker
```

Place this near the existing imports. The `from shared_utilities import create_sun_direction_indicator` import stays for now -- it's still used by Earth's `upper_atmosphere` and `hill_sphere` sphere shell functions (which we're NOT modifying). Phase D removes the import along with the dead sphere functions.

### 4.3 Apply sunward rotation to magnetosphere geometry

Locate the magnetosphere trace setup. Currently (around lines 660-669):

```python
    # Create magnetosphere main shape
    x, y, z = create_magnetosphere_shape(params)
    
    # Unpack center position
    center_x, center_y, center_z = center_position
    
    # 1. Add the main magnetosphere structure
    x = np.array(x) + center_x
    y = np.array(y) + center_y
    z = np.array(z) + center_z
```

Replace with:

```python
    # Create magnetosphere main shape (generated with -X as sunward)
    x, y, z = create_magnetosphere_shape(params)
    
    # Unpack center position
    center_x, center_y, center_z = center_position
    
    # 1. Add the main magnetosphere structure
    # Rotate to actual sunward direction, then offset to center position
    x, y, z = np.array(x), np.array(y), np.array(z)
    x, y, z = rotate_to_sunward(x, y, z, center_position=center_position)
    x = x + center_x
    y = y + center_y
    z = z + center_z
```

Pattern matches Phase C1 Venus/Mars exactly.

### 4.4 Replace magnetosphere info marker

Currently (around lines 692-706):

```python
    # Info marker at first point on magnetosphere structure
    traces.append(
        go.Scatter3d(
            x=[x[0]], y=[y[0]], z=[z[0]],
            mode='markers',
            marker=dict(size=6, color='rgb(180, 180, 255)', opacity=0.9,
                        symbol='cross', line=dict(color='white', width=1)),
            name='',
            legendgroup='Earth: Magnetosphere',
            text=magnetosphere_text,
            customdata=magnetosphere_customdata,
            hovertemplate='%{text}<extra></extra>',
            showlegend=False
        )
    )
```

Replace with:

```python
    # Info marker at first point on magnetosphere structure
    traces.append(create_info_marker(
        x[0], y[0], z[0],
        'rgb(180, 180, 255)', magnetosphere_text[0], 'Earth: Magnetosphere'
    ))
```

Note: `magnetosphere_text` is a list of one string in the source. `create_info_marker()` takes a string, so pass `magnetosphere_text[0]`.

### 4.5 Apply sunward rotation to bow shock geometry

Currently (around lines 740-743, immediately after bow shock geometry generation):

```python
    # Apply center position offset
    bow_shock_x = np.array(bow_shock_x) + center_x
    bow_shock_y = np.array(bow_shock_y) + center_y
    bow_shock_z = np.array(bow_shock_z) + center_z
```

Replace with:

```python
    # Apply rotation to sunward direction, then offset to center position
    bow_shock_x = np.array(bow_shock_x)
    bow_shock_y = np.array(bow_shock_y)
    bow_shock_z = np.array(bow_shock_z)
    bow_shock_x, bow_shock_y, bow_shock_z = rotate_to_sunward(
        bow_shock_x, bow_shock_y, bow_shock_z, center_position=center_position
    )
    bow_shock_x = bow_shock_x + center_x
    bow_shock_y = bow_shock_y + center_y
    bow_shock_z = bow_shock_z + center_z
```

### 4.6 Replace bow shock info marker

Currently (around lines 765-779):

```python
    # Info marker at first point on bow shock structure
    traces.append(
        go.Scatter3d(
            x=[bow_shock_x[0]], y=[bow_shock_y[0]], z=[bow_shock_z[0]],
            mode='markers',
            marker=dict(size=6, color='rgb(255, 200, 150)', opacity=0.9,
                        symbol='cross', line=dict(color='white', width=1)),
            name='',
            legendgroup='Earth: Bow Shock',
            text=bow_shock_text,
            customdata=bow_shock_customdata,
            hovertemplate='%{text}<extra></extra>',
            showlegend=False
        )
    )
```

Replace with:

```python
    # Info marker at first point on bow shock structure
    traces.append(create_info_marker(
        bow_shock_x[0], bow_shock_y[0], bow_shock_z[0],
        'rgb(255, 200, 150)', bow_shock_text[0], 'Earth: Bow Shock'
    ))
```

### 4.7 Van Allen radiation belt info markers

**Important: do NOT rotate the radiation belts.** They are geomagnetic-axis-anchored, not solar-wind-anchored. Mars's crustal fields are the analogous pattern from Phase C1 -- they stayed unrotated. The belt geometry generation loop (around lines 797-822) wraps around Earth's rotational axis using `cos(angle)`/`sin(angle)` -- preserve this entirely.

For each of the two belt info markers (inside the `for i, belt_distance in enumerate(belt_distances):` loop), the current code is (around lines 848-862, for each belt):

```python
        # Info marker for this belt
        traces.append(
            go.Scatter3d(
                x=[belt_x[0]], y=[belt_y[0]], z=[belt_z[0]],
                mode='markers',
                marker=dict(size=6, color=belt_colors[i], opacity=0.9,
                            symbol='cross', line=dict(color='white', width=1)),
                name='',
                legendgroup=belt_names[i],
                text=belt_text,
                customdata=belt_customdata,
                hovertemplate='%{text}<extra></extra>',
                showlegend=False
            )
        )
```

Replace with:

```python
        # Info marker for this belt
        traces.append(create_info_marker(
            belt_x[0], belt_y[0], belt_z[0],
            belt_colors[i], belt_text[0], belt_names[i]
        ))
```

This appears once in the source but executes twice (once per belt) because it's inside the belt loop. The `belt_text` variable is a list of one string (set at the top of each loop iteration); pass `belt_text[0]`.

### 4.8 Remove the per-shell sun direction indicator call

Currently (around lines 863-868, immediately before `return traces`):

```python
    sun_traces = create_sun_direction_indicator(
        center_position=center_position, 
        shell_radius=100 * EARTH_RADIUS_AU
    )
    for trace in sun_traces:
        traces.append(trace)

    return traces
```

Replace with:

```python
    return traces
```

The unified dispatch now issues one indicator per body at the outermost active shell radius.

### 4.9 Add Earth magnetosphere CUSTOM_SHELLS entry

In `shell_configs.py`, locate the `CUSTOM_SHELLS = {` dict. After the Mars block (Phase C1's last addition), add:

```python

    # ============================================================
    # Earth
    # ============================================================
    # Source: NASA Goddard Space Flight Center -- Magnetosphere overview;
    #         NASA Van Allen Probes (radiation belts, 2012-2019);
    #         NASA Heliophysics. Earth's magnetosphere extends ~10 R_E
    #         sunward, magnetotail ~100 R_E. Bow shock standoff ~15 R_E.
    #         Inner radiation belt ~1.5 R_E (protons), outer ~4.5 R_E (electrons).
    # Verified: April 2026 provenance audit.
    'Earth': {

        'magnetosphere': {
            'builder': 'earth_visualization_shells.create_earth_magnetosphere_shell',
            'tooltip': (
                "SET MANUAL SCALE TO AT LEAST 0.01 AU TO VISUALIZE.\n\n"
                "Earth's magnetosphere extends about 10 Earth radii on the Sun-facing side\n"
                "and stretches into a long magnetotail on the night side. It protects Earth\n"
                "from solar radiation and cosmic rays, making complex life possible.\n\n"
                "Bow Shock: The boundary where the supersonic solar wind is first slowed\n"
                "by Earth's magnetic field, typically located about 15 Earth radii upstream\n"
                "from Earth on the Sun-facing side.\n\n"
                "Inner Van Allen Belt: Region of trapped charged particles (mainly protons)\n"
                "extending from about 1,000 km to 6,000 km above Earth's surface.\n"
                "Outer Van Allen Belt: Region of trapped charged particles (mainly electrons)\n"
                "extending from about 13,000 km to 60,000 km above Earth's surface.\n\n"
                "The same builder produces all four traces (separate legend entries):\n"
                "Magnetosphere, Bow Shock, Inner Radiation Belt, Outer Radiation Belt."
            ),
        },

    },

```

The tooltip text mirrors the source's `earth_magnetosphere_info` string (which is what Earth's GUI checkbox currently uses), with one added paragraph noting the four-trace structure.

**Don't close the CUSTOM_SHELLS dict yet** -- Section 5 adds two more entries (leo, geostationary_belt). After Section 5, the closing `}` for Earth's block in CUSTOM_SHELLS will follow geostationary_belt.

Working snippet for visualization (the full Earth CUSTOM_SHELLS block after Section 5):

```python
    'Earth': {
        'magnetosphere': { ... },        # Section 4
        'leo': { ... },                  # Section 5
        'geostationary_belt': { ... },   # Section 5
    },
```

### 4.10 Verification after Section 4

```bash
python3 -m py_compile shell_configs.py earth_visualization_shells.py

python3 -c "
# Verify Earth magnetosphere builder still works
import importlib
mod = importlib.import_module('earth_visualization_shells')
traces = mod.create_earth_magnetosphere_shell((0, 0, 0))
# Expected: 4 geometry traces + 4 info markers = 8 traces
# No sun indicator suffix any more
assert len(traces) == 8, 'Expected 8 traces, got %d' % len(traces)

# Verify CUSTOM_SHELLS has Earth's magnetosphere
from shell_configs import CUSTOM_SHELLS
assert 'Earth' in CUSTOM_SHELLS
assert 'magnetosphere' in CUSTOM_SHELLS['Earth']
assert CUSTOM_SHELLS['Earth']['magnetosphere']['builder'].endswith('create_earth_magnetosphere_shell')

print('Section 4 verification PASS')
"
```

If this fails, debug before proceeding to Section 5.

---

## 5. Earth LEO + GEO + Delegation

Three smaller tasks finish C2: refactor the LEO and geostationary belt info markers, add their CUSTOM_SHELLS entries, and replace Earth's dispatch block.

### 5.1 LEO info marker refactor

In `earth_visualization_shells.py`, `create_earth_leo_shell` currently has an old-style info marker (around lines 983-994):

```python
    r_info = np.max(z)  # LEO outer extent
    traces.append(go.Scatter3d(
        x=[center_x], y=[center_y], z=[center_z + r_info],
        mode='markers',
        marker=dict(size=6, color='rgb(255, 248, 220)', opacity=0.9,
                    symbol='cross', line=dict(color='white', width=1)),
        name='',
        legendgroup='Earth: Low Earth Orbit (LEO)',
        text=[hover_text],
        customdata=['Earth: Low Earth Orbit (LEO)'],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    ))
```

Replace with:

```python
    # Info marker at LEO outer extent on the north pole
    r_info = np.max(z) - center_z  # LEO outer extent above center
    traces.append(create_info_marker(
        center_x, center_y, center_z + r_info,
        'rgb(255, 248, 220)', hover_text, 'Earth: Low Earth Orbit (LEO)'
    ))
```

Notes:

1. `hover_text` in LEO is already a plain string (not a list), so pass directly.
2. The `r_info = np.max(z)` calculation pre-refactor took the max of the *already-offset* z values. Post-refactor, the `center_z` offset is applied again inside `create_info_marker`. Subtract `center_z` from `np.max(z)` to get the body-frame radius, then `create_info_marker` re-adds it. Cleaner expression of the same intent.
3. LEO doesn't have a per-shell `create_sun_direction_indicator` call -- nothing to remove.

### 5.2 GEO info marker refactor

In `create_earth_geostationary_belt_shell`, the info marker is at the GEO ring at phi=0 (around lines 1094-1105):

```python
    # Info marker on GEO ring at phi=0
    traces.append(go.Scatter3d(
        x=[center_x + geo_radius_au], y=[center_y], z=[center_z],
        mode='markers',
        marker=dict(size=6, color='rgb(220, 220, 255)', opacity=0.9,
                    symbol='cross', line=dict(color='white', width=1)),
        name='',
        legendgroup='Earth: Geostationary Belt (GEO)',
        text=[hover_text],
        customdata=['Earth: Geostationary Belt (GEO)'],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    ))
```

Replace with:

```python
    # Info marker on GEO ring at phi=0
    traces.append(create_info_marker(
        center_x + geo_radius_au, center_y, center_z,
        'rgb(220, 220, 255)', hover_text, 'Earth: Geostationary Belt (GEO)'
    ))
```

GEO also has no per-shell sun indicator call -- nothing to remove. Both `np.max(z) - center_z` in LEO and the `center_x + geo_radius_au` position in GEO are pre-offset; pass to `create_info_marker` directly.

### 5.3 Add LEO and GEO to CUSTOM_SHELLS

Inside Earth's block in CUSTOM_SHELLS (which currently has only `'magnetosphere'` after Section 4), add two more entries. Keep the order matching natural reading: magnetosphere first (covers protective shield), then LEO (low altitude, visible to eye), then GEO (high altitude, infrastructure).

After Earth's `'magnetosphere'` block, add:

```python

        'leo': {
            'builder': 'earth_visualization_shells.create_earth_leo_shell',
            'tooltip': (
                "SET MANUAL SCALE TO 0.003 AU TO VISUALIZE.\n\n"
                "Low Earth Orbit (LEO) is the region from roughly 200 km to 2,000 km altitude\n"
                "(1.03 to 1.31 Earth radii), where satellites orbit at all inclinations.\n\n"
                "Unlike geostationary orbit, LEO satellites travel at all angles relative to the equator --\n"
                "forming a true shell around Earth rather than a ring. A LEO satellite completes\n"
                "one orbit in 90-120 minutes and crosses the sky in about 6 minutes.\n\n"
                "Notable LEO residents:\n"
                "  * ISS: ~400 km altitude, 51.6 deg inclination\n"
                "  * Starlink: ~550 km altitude, multiple inclination shells\n"
                "  * Hubble Space Telescope: ~540 km altitude\n"
                "  * Most Earth observation and weather satellites\n\n"
                "There are currently ~11,000 active satellites in LEO, with Starlink alone\n"
                "operating nearly 7,000. The total debris population (defunct satellites, rocket\n"
                "bodies, fragments >10 cm) exceeds 35,000 tracked objects.\n\n"
                "The bright moving 'stars' visible at dusk and dawn are LEO objects --\n"
                "most commonly Starlink trains. GEO satellites at 35,786 km are too faint\n"
                "and too slow to see with the naked eye."
            ),
        },

        'geostationary_belt': {
            'builder': 'earth_visualization_shells.create_earth_geostationary_belt_shell',
            'tooltip': (
                "SET MANUAL SCALE TO 0.003 AU TO VISUALIZE.\n\n"
                "The geostationary belt (GEO) is a ring of orbital space at 42,164 km from Earth's center\n"
                "(35,786 km altitude), where satellites orbit at exactly Earth's rotation rate\n"
                "and appear stationary over a fixed point on the equator.\n\n"
                "Approximately 550 active geostationary satellites currently occupy this belt --\n"
                "carrying TV broadcasts, weather imagery, GPS augmentation, and communications\n"
                "for roughly half the world's population.\n\n"
                "On April 13, 2029, asteroid Apophis will pass Earth at 38,013 km -- roughly 4,150 km\n"
                "INSIDE this belt. The closest operational satellites will be about 4,000 km away\n"
                "as it passes through. No impact risk to satellites is expected, but the flyby\n"
                "will be detectable from geostationary platforms as it transits the sky."
            ),
        },
```

The tooltip text is sourced verbatim from `earth_leo_shell_info` and `earth_geostationary_belt_info` in `earth_visualization_shells.py`.

**Important**: the shell key in the CUSTOM_SHELLS registry must match the post-prefix-strip name from `shell_vars`. The dispatch strips the `earth_` prefix, so:
- `earth_leo` -> `leo`
- `earth_geostationary_belt` -> `geostationary_belt`
- `earth_magnetosphere` -> `magnetosphere`

All three keys above use the bare post-prefix-strip names. Verify against the GUI vars in `palomas_orrery.py` (`earth_leo_var`, `earth_geostationary_belt_var`, `earth_magnetosphere_var`) -- the names match.

After all three entries, close Earth's CUSTOM_SHELLS block with `},`.

### 5.4 Earth delegation in planet_visualization.py

Find the Earth dispatch block in `create_planet_visualization()` (currently around lines 689-712):

```python
    if planet_name == 'Earth':
        if shell_vars['earth_inner_core'].get() == 1:
            traces.extend(create_earth_inner_core_shell(center_position))
        if shell_vars['earth_outer_core'].get() == 1:
            traces.extend(create_earth_outer_core_shell(center_position))
        if shell_vars['earth_lower_mantle'].get() == 1:
            traces.extend(create_earth_lower_mantle_shell(center_position))
        if shell_vars['earth_upper_mantle'].get() == 1:
            traces.extend(create_earth_upper_mantle_shell(center_position))
        if shell_vars['earth_crust'].get() == 1:
            traces.extend(create_earth_crust_shell(center_position))
        if shell_vars['earth_atmosphere'].get() == 1:
            traces.extend(create_earth_atmosphere_shell(center_position))
        if shell_vars['earth_upper_atmosphere'].get() == 1:
            traces.extend(create_earth_upper_atmosphere_shell(center_position))
        if shell_vars['earth_magnetosphere'].get() == 1:
            traces.extend(create_earth_magnetosphere_shell(center_position))
        if shell_vars['earth_hill_sphere'].get() == 1:
            traces.extend(create_earth_hill_sphere_shell(center_position))
        if shell_vars['earth_geostationary_belt'].get() == 1:
            traces.extend(create_earth_geostationary_belt_shell(center_position))
        if shell_vars['earth_leo'].get() == 1:
            traces.extend(create_earth_leo_shell(center_position))
```

Replace with:

```python
    if planet_name == 'Earth':
        # Step 3 Phase C2: delegate to unified config-driven dispatch.
        # Custom geometry: earth_magnetosphere -> CUSTOM_SHELLS['Earth']['magnetosphere']
        # which lazy-imports and emits magnetosphere + bow shock + 2 Van Allen belt traces.
        # earth_leo and earth_geostationary_belt also lazy-imported via CUSTOM_SHELLS.
        return create_celestial_body_visualization(
            fig, planet_name, shell_vars,
            animate=animate, frames=frames,
            center_position=center_position,
            object_type='Earth',
            center_object='Earth',
        )
```

### 5.5 Bottom-up edit order

Apply edits in this order within each file to prevent line-number drift:

**In `earth_visualization_shells.py`** (top-down, since exact-string `str_replace` is location-independent):

1. Add import (top of file).
2. Section 5.2: GEO info marker (~line 1094).
3. Section 5.1: LEO info marker (~line 983).
4. Section 4.7: Van Allen belt info markers (~line 848).
5. Section 4.8: Remove sun indicator (~line 863).
6. Section 4.6: Bow shock info marker (~line 765).
7. Section 4.5: Bow shock rotation (~line 740).
8. Section 4.4: Magnetosphere info marker (~line 692).
9. Section 4.3: Magnetosphere rotation (~line 660).

**Note**: this is bottom-up by line number, even though the visual flow above goes top-down conceptually. `str_replace` is content-matching, so order strictly speaking doesn't matter -- but bottom-up is the documented discipline.

**In `shell_configs.py`**: just inserts (no replacements). Order doesn't matter -- both are appended to existing blocks.

**In `planet_visualization.py`**: single `str_replace` for the Earth dispatch block.

### 5.6 Final verification after Section 5

```bash
python3 -m py_compile shell_configs.py planet_visualization.py earth_visualization_shells.py

python3 -c "
from shell_configs import SHELL_CONFIGS, CUSTOM_SHELLS

# Earth in both registries
assert 'Earth' in SHELL_CONFIGS and 'Earth' in CUSTOM_SHELLS

# 8 sphere shells
assert len(SHELL_CONFIGS['Earth']) == 8

# 3 custom shells
assert len(CUSTOM_SHELLS['Earth']) == 3, 'Got %d custom shells' % len(CUSTOM_SHELLS['Earth'])
expected_custom = {'magnetosphere', 'leo', 'geostationary_belt'}
assert set(CUSTOM_SHELLS['Earth'].keys()) == expected_custom

# Smoke test: import via builder strings
import importlib
for name, entry in CUSTOM_SHELLS['Earth'].items():
    module_name, func_name = entry['builder'].rsplit('.', 1)
    mod = importlib.import_module(module_name)
    func = getattr(mod, func_name)
    traces = func((0, 0, 0))
    assert len(traces) > 0, '%s returned no traces' % name

# Verify dispatch is in place
import planet_visualization
import inspect
src = inspect.getsource(planet_visualization.create_planet_visualization)
# After C2: Earth block should be the one-line delegation, not 11 if-statements
assert 'create_earth_inner_core_shell(center_position)' not in src, \
    'Old Earth dispatch still present'

print('Section 5 verification PASS')
print('Earth: 8 sphere + 3 custom shells in registries')
"
```

If any assertion fails, STOP and debug.

---

## 6. Verification Plan

### 6.1 Static checks

```bash
# All touched files compile
python3 -m py_compile shell_configs.py planet_visualization.py earth_visualization_shells.py

# All touched files are LF
for f in shell_configs.py planet_visualization.py earth_visualization_shells.py; do
    file "$f" | grep -q CRLF && echo "FAIL: $f CRLF" || echo "OK: $f"
done

# All touched files are ASCII
python3 -c "
for f in ['shell_configs.py', 'planet_visualization.py', 'earth_visualization_shells.py']:
    with open(f, 'rb') as fh:
        content = fh.read().decode('utf-8', errors='replace')
    issues = sum(1 for c in content if ord(c) > 127)
    print('%-45s %s' % (f, 'OK' if not issues else 'FAIL: %d non-ASCII' % issues))
"
```

### 6.2 Comprehensive import smoke test

```bash
python3 -c "
from orrery_rendering import build_sphere_shell, create_info_marker, rotate_to_sunward
from shell_configs import SHELL_CONFIGS, CUSTOM_SHELLS
from planet_visualization import create_celestial_body_visualization, create_planet_visualization

# All Phase A+B+C1+C2 bodies in SHELL_CONFIGS
expected_sphere = {'Mercury', 'Moon', 'Planet 9', 'Pluto', 'Eris', 'Venus', 'Mars', 'Earth'}
assert set(SHELL_CONFIGS.keys()) == expected_sphere, \
    'Sphere mismatch: %s' % sorted(SHELL_CONFIGS.keys())

# Custom bodies
expected_custom = {'Mercury', 'Venus', 'Mars', 'Earth'}
assert set(CUSTOM_SHELLS.keys()) == expected_custom

# Earth counts
assert len(SHELL_CONFIGS['Earth']) == 8
assert len(CUSTOM_SHELLS['Earth']) == 3

print('Phase C2 imports and counts PASS')
"
```

### 6.3 Sphere builder smoke test

```bash
python3 -c "
from orrery_rendering import build_sphere_shell
from shell_configs import SHELL_CONFIGS

# Build every Earth sphere shell
for shell_name, cfg in SHELL_CONFIGS['Earth'].items():
    traces = build_sphere_shell(cfg, 'Earth', (0, 0, 0))
    assert len(traces) == 2, 'Earth/%s expected 2 traces, got %d' % (shell_name, len(traces))

print('Earth sphere builder smoke test PASS')
"
```

### 6.4 Custom geometry smoke test

```bash
python3 -c "
import importlib

# Earth magnetosphere: 4 geometry traces + 4 info markers = 8 traces
mod = importlib.import_module('earth_visualization_shells')
traces = mod.create_earth_magnetosphere_shell((0, 0, 0))
assert len(traces) == 8, 'magnetosphere: expected 8 traces, got %d' % len(traces)

# Earth LEO: 1 geometry + 1 info marker = 2 traces
traces = mod.create_earth_leo_shell((0, 0, 0))
assert len(traces) == 2, 'LEO: expected 2 traces, got %d' % len(traces)

# Earth GEO: 1 geometry + 1 info marker = 2 traces
traces = mod.create_earth_geostationary_belt_shell((0, 0, 0))
assert len(traces) == 2, 'GEO: expected 2 traces, got %d' % len(traces)

print('Earth custom geometry smoke test PASS')
"
```

### 6.5 Sunward rotation correctness

The key behavioral test: Earth magnetosphere now rotates with `center_position`. Verify the geometry actually changes for an off-axis Earth.

```bash
python3 -c "
import importlib
import numpy as np

mod = importlib.import_module('earth_visualization_shells')

# Render with Earth at origin (no rotation needed)
traces_origin = mod.create_earth_magnetosphere_shell((0, 0, 0))

# Render with Earth at (-1.0, 0.0, 0.0): sunward from Earth = +X (opposite of default -X)
# Magnetosphere geometry should be 180-deg rotated
traces_off = mod.create_earth_magnetosphere_shell((-1.0, 0.0, 0.0))

# First trace is the magnetosphere geometry
origin_x = traces_origin[0].x
off_x = np.array(traces_off[0].x) - (-1.0)  # Remove offset

# After 180-deg rotation, x should be negated
assert np.allclose(off_x, -np.array(origin_x), atol=1e-9), \
    'Magnetosphere not rotating: x not negated for Earth at -X'

print('Sunward rotation correctness PASS')
"
```

This test exercises both the rotation logic (in `orrery_rendering.rotate_to_sunward`) and the Earth-specific rotation call.

### 6.6 Indicator de-duplication check (visual, manual)

Switch center to Earth in the orrery GUI. Enable shells incrementally:

| Toggle on | Expected | Notes |
|---|---|---|
| Inner core only | One indicator at body-centered view -> hidden; flyto -> appears once | Indicator suppressed at origin |
| All sphere shells | Same as above | Indicator scales to outermost (Hill sphere) |
| Magnetosphere only | One indicator | Was previously emitted by magnetosphere builder; now from dispatch |
| All shells + magnetosphere + LEO + GEO | One indicator total | The headline test -- multiple custom shells, still single indicator |

If multiple indicators appear, the per-shell call wasn't removed from a builder. Re-check Section 4.8.

### 6.7 GUI tooltip regression check

Hover the GUI checkboxes for all 11 Earth shell controls. Tooltips should still display correctly, sourced from the inline `CreateToolTip(earth_*_checkbutton, earth_*_info)` calls in `palomas_orrery.py`. The `*_info` strings remain in `earth_visualization_shells.py` (C2 doesn't remove them). Phase D switches this to read from configs.

### 6.8 Animation regression check

Per the Phase C1 handoff item 13, animated plots have specific Earth shell behavior:

- **Heliocentric animated plot**: shells do NOT display.
- **Body-centered animated plot (Earth-centered)**: all shells render as static geometry at origin; orbiting bodies animate around them.

Verify both behaviors are unchanged after C2.

### 6.9 Mode 5 visual verification items for Tony

This is the headline section -- C2's biggest behavioral change is the magnetosphere rotation.

**Earth sphere shells**:

1. Each sphere shell renders at the expected radius fraction. Inner core (0.19) is small and orange-red; outer core (0.55) wraps it; lower mantle (0.85) is a thick layer; upper mantle (0.98) is just below crust; crust (1.0) is a solid blue mesh3d sphere.
2. Crust mesh3d should render as a solid surface (no dot grid), matching the Phase A/B/C1 pattern for crusts. Color rgb(70, 120, 160) -- ocean blue.
3. Atmosphere (1.05) is a thin pale-blue layer just outside the crust.
4. Upper atmosphere (1.25) is a slightly thicker pale-blue layer.
5. Hill sphere (235 R_E) is a large green sparse sphere; requires manual scale >= 0.02 AU to visualize.
6. Each shell has ONE cross info marker at the north pole (new style: size=8, red outline). Hover shows full text.
7. Indicator: ONE per Earth render. Suppressed if Earth is the center body and the view is at origin.

**Earth magnetosphere -- the new rotation behavior**:

8. **Heliocentric view (default)**: Earth at +X (~1 AU). Sun direction from Earth = -X = default geometry orientation. Rotation is near-identity. Magnetosphere should look visually identical to pre-C2: bow shock on the -X side (sunward), magnetotail on the +X side (anti-sunward).

9. **Earth-centered view (flyto)**: With Earth at origin, the Sun is now at the position where Earth used to be in the heliocentric frame. Rotation should reorient the bow shock to face the Sun (which is at the offset). The Phase C1 handoff item 10 notes that the sun indicator is currently suppressed in body-centered views (Phase D `sun_position` wiring fixes this), so until that fix the visual cue for "where is the Sun" in centered view is the magnetosphere itself: bow shock points toward where the Sun is in the body frame.

10. **Heliocentric with Earth at non-+X position** (e.g. animate to a different orbit position, or change reference frame): magnetosphere rotates to face the Sun. Before C2 this was wrong -- bow shock would point along -X regardless of Earth's position. After C2 it should always face the Sun.

11. Magnetosphere trace renders with light blue color (rgb(180, 180, 255)), opacity 0.2, size 2.0 dots.
12. Bow shock trace renders with orange (rgb(255, 200, 150)), opacity 0.2, size 1.5 dots.
13. Inner Van Allen belt: red (rgb(255, 100, 100)) toroidal ring at ~1.5 R_E.
14. Outer Van Allen belt: blue (rgb(100, 200, 255)) toroidal ring at ~4.5 R_E.
15. Van Allen belts do NOT rotate (geomagnetic-axis-anchored). They stay aligned with the +Z axis regardless of where the Sun is. Confirm in a flyto view: bow shock faces Sun, but belts wrap around Earth's rotational axis.
16. All four trace groups have info markers (new style).

**Earth LEO and GEO**:

17. LEO renders as a sparse spherical scatter shell between 1.03 and 1.31 R_E. Color rgb(255, 248, 220) (warm white). 300 points. One info marker at north pole. Note: deterministic via `np.random.seed(7)` -- should look the same every render.
18. GEO renders as a sparse ring at 6.62 R_E in the equatorial plane. 240 points. Color rgb(220, 220, 255) (cool silver). One info marker at the +X side of the ring.
19. Apophis 2029 close approach: per the source comment, Apophis passes at 38,013 km, inside the GEO ring at 42,164 km. The GEO ring visualization sets the spatial context for this.

**Regression**:

20. Mercury, Moon, Planet 9, Pluto, Eris, Venus, Mars all render unchanged (Phase A/B/C1 work).
21. Jupiter, Saturn, Uranus, Neptune still render via the old dispatch path (C3/C4 work).
22. Sun still renders via `create_sun_visualization()` (Phase D).

### 6.10 File size baseline (informational)

Save a static Earth-centered plot with all shells enabled. Compare to pre-C2 baseline. Expected: similar or smaller. The bulk of the size optimization from Step 2 (single info marker per shell) is already in place; C2 makes architectural changes, not size changes.

### 6.11 Phase E preview (informational)

After C2, Earth has 11 shell renderings (8 sphere + 4 magnetosphere subgroups -- including Van Allen belts -- plus LEO and GEO = 11 visible legend entries when all toggled on, plus 1 sun indicator = 12 traces total at the planet level). This sets the high-water mark for a single body's visual density until Phase E satellite shells are added (which would add Moon's full interior shells, plus L1-L5 Lagrange overlays, plus possibly ISS/Hubble individual markers).

---

## 7. Decision Log and Open Items

### Decisions made by this manifest

1. **Magnetosphere structure: Option A (fused)**. Earth's `create_earth_magnetosphere_shell` continues to emit four trace groups from one builder. One CUSTOM_SHELLS entry, matching Mars's crustal-fields precedent. No new GUI toggles. Tony's decision.

2. **Magnetosphere rotation: added**. Earth's magnetosphere and bow shock now use `rotate_to_sunward()`, matching the Phase C1 Venus/Mars pattern. This is a behavior fix, not a regression: heliocentric view at Earth's typical +X position is near-identity (no visible change), but flyto/off-axis views now point correctly. Tony's decision; key Mode 5 verification item.

3. **Van Allen belts: not rotated**. Geomagnetic-axis-anchored. Same precedent as Mars crustal fields (unrotated despite being inside the magnetosphere builder).

4. **`atmosphere` internal name: `'Lower Atmosphere'` preserved**. Matches Venus/Mars precedent from Phase C1 (which also preserved `'Lower Atmosphere'` from their sources). The legend will render `"Earth: Lower Atmosphere"`. The GUI checkbox label remains `"-- Atmosphere"` (independent of config name). Tony's decision: preserve source.

5. **Hill sphere n_points: 30 -> 20**. Standardization, consistent with Mercury/Venus/Mars/Planet 9 fixes from Phases A-C1.

6. **No ionosphere shell added**. Doesn't exist in source. The conceptual "ionosphere region" is part of the upper_atmosphere shell (which covers thermosphere/exosphere). Earth has 8 sphere shells.

7. **Per-shell sun indicator calls removed**: upper_atmosphere, magnetosphere, hill_sphere. Unified dispatch issues one per body. The dead `create_sun_direction_indicator` import remains for Phase D cleanup (still used by the now-unreachable sphere shell functions).

8. **`earth_*_info` strings retained in source file**. Tooltips still wired via Path A (inline `CreateToolTip` calls in `palomas_orrery.py`). Phase D batch-rewires to read from config tooltips.

9. **CUSTOM_SHELLS keys use bare post-prefix names**: `magnetosphere`, `leo`, `geostationary_belt`. Matches the dispatch's prefix-strip behavior (`earth_*` -> bare names).

10. **Auto-generation script for sphere configs**: continued from C1, validated for Earth's 8 shells. Hill sphere's local-variable pattern handled the same way as Mercury/Venus/Mars/Planet 9.

### Open items for future phases

1. **`sun_position` wiring through magnetosphere builders** -- Phase B item 6, Phase C1 deferred item 10, persists. After C2, Earth/Venus/Mars magnetospheres rotate assuming Sun at origin. In a body-centered view, this means the indicator (which is suppressed at origin) and the rotation reference are inconsistent. Phase D threads actual Sun position through both `rotate_to_sunward` and `create_sun_direction_indicator`.

2. **Mars magnetosphere missing info marker** -- Phase C1 item 14, still open. C2 doesn't fix this (still requires Mars-specific editorial decision).

3. **Dead sphere shell functions in `earth_visualization_shells.py`** -- after C2, the 8 sphere shell functions are unreachable. Custom geometry siblings (magnetosphere, LEO, GEO) still live in the same file. Phase D decides per-function fate (selective deletion vs. file split vs. whole-file archive with custom geometry moved to its own module).

4. **Phase C3 prep**: Jupiter is next. New patterns to plan for: rings, Io plasma torus, gas giant cloud layers (mesh3d), radiation belts. Same mechanical approach: sphere shells via configs, custom geometry via CUSTOM_SHELLS, builder refactor for any local-rotation patterns.

5. **GEO info marker position** -- currently placed at `(geo_radius_au, 0, 0)` (the +X side of the ring). This is in the equatorial plane, which means it overlaps the actual GEO ring at high zoom. Tony's call whether to move it to a "spoke" position (e.g. `(geo_radius_au * cos(15deg), geo_radius_au * sin(15deg), 0)`) or leave as-is. Cosmetic, not blocking.

### Risks and mitigations

| Risk | Mitigation |
|---|---|
| Auto-generation script produces malformed Earth config | Section 3.3 manual review checklist |
| Magnetosphere rotation breaks heliocentric view | Section 4.1 documents expected near-identity behavior; Section 6.9 item 8 is the explicit visual check |
| Van Allen belts accidentally rotated | Section 4.7 explicit "do NOT rotate" note; Section 6.9 item 15 visual check |
| LEO/GEO info marker position wrong | Section 5.1 + 5.2 explicit coordinate notes; smoke test in 6.4 |
| Earth dispatch leaks back through old path | Section 5.6 explicit assertion that old dispatch is gone |
| Hill sphere n_points change causes visual density issue | Standardization is the same as C1; if visible, can revert per-body |
| Indicator double-firing | Section 6.6 manual check; Phase C1 already verified the dispatch handles this correctly |

### Implementation discipline (per protocol)

- Python binary mode (`rb`/`wb`) for all file reads/writes
- Bottom-up editing within `earth_visualization_shells.py` (Section 5.5 ordering)
- Exact-string matching with `str_replace`, never regex
- One section at a time; run syntax check before proceeding
- Credit line update: `Module updated: May 2026 with Anthropic's Claude Opus 4.7` on every modified file
- ASCII only -- verify with `grep -P '[^\x00-\x7F]'`
- If any source value can't be confirmed from project files, STOP and ask Tony

---

## 8. Phase C2 Summary

| Component | Change |
|---|---|
| Sphere shells added to SHELL_CONFIGS | 8 (Earth) |
| Custom shells added to CUSTOM_SHELLS | 3 (Earth: magnetosphere, leo, geostationary_belt) |
| Bodies on unified dispatch (after) | 8 |
| Sun direction indicator calls removed | 3 (in `earth_visualization_shells.py`) |
| Info markers updated to new style | 6 (4 in magnetosphere + 1 LEO + 1 GEO) |
| Rotation calls added | 2 (magnetosphere + bow shock) |
| Magnetic_tilt_deg parameter | Not used in C2 (Earth ~11 deg; small enough to defer to C4 Uranus/Neptune for the rotation step implementation) |
| sun_position parameter | Defaulted to (0,0,0); Phase D wires actual value |
| File archivable in D | No (`earth_visualization_shells.py` retains 3 custom-geometry functions) |
| Behavioral change | Magnetosphere/bow shock rotate to actual sunward direction (currently no rotation; fix in flyto views) |

After Phase C2:

- 8 bodies on unified dispatch (Mercury, Moon, Planet 9, Pluto, Eris, Venus, Mars, Earth)
- 5 bodies remaining on `create_planet_visualization` (Jupiter, Saturn, Uranus, Neptune; plus Sun via `create_sun_visualization`)
- 2 shell files fully dead from sphere-only bodies (Pluto, Eris) -- batch-archive in D
- 0 shell files fully dead from custom-geometry bodies (Venus, Mars, Earth) -- per-function archive in D
- 1 shared helper promoted, exercised across 4 magnetospheres (Mercury, Venus, Mars, Earth)
- `magnetic_tilt_deg` parameter still unused (Phase C4 Uranus/Neptune)
- `sun_position` parameter still defaulted (Phase D)

---

## 9. Workflow Provenance

This manifest:
- Audited by Anthropic's Claude Opus 4.7
- Following Phase C1 handoff (May 15, 2026) by Opus 4.6
- From prompt v4 by Tony Quintanilla + Anthropic's Claude Opus 4.6
- Five decision points confirmed by Tony + Opus 4.6 before drafting (A / Yes / No / preserve / yes)
- Following protocol v3.22 (collegial Mode 7)

To be executed by: Anthropic's Claude Opus 4.6 + Tony, in a separate session.

The Phase A/B/C1 manifests set the quality bar. C2 reuses that machinery on a single, more complex body. Particular care on Section 4 (magnetosphere refactor) because Earth's magnetosphere had no rotation before, so the visual change in flyto views is the most observable C2 outcome.

Implementing Claude: if Section 4 (magnetosphere) verifies cleanly but context starts pressuring before Section 5, stop and write a partial handoff. Phase C2 can be split across sessions at the Section 4/5 boundary -- the codebase remains functional with Earth's magnetosphere refactored and registered in CUSTOM_SHELLS, even if the dispatch still routes through the old if-block (which will then continue calling the refactored magnetosphere builder via its old path and produce correct output).

*Module updated: May 2026 with Anthropic's Claude Opus 4.7*
