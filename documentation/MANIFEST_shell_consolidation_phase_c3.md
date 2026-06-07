# MANIFEST: Shell Consolidation Step 3 -- Phase C3 (Jupiter)

**Project:** Paloma's Orrery | Plotting Consolidation Step 3
**Date:** May 16, 2026
**Source prompt:** `PROMPT_shell_consolidation_for_opus_v5.md` (Jupiter-only)
**Phase C2 handoff:** `HANDOFF_shell_consolidation_phase_c2.md` (May 16, 2026)
**Manifest by:** Anthropic's Claude Opus 4.7 (audit)
**For execution by:** Anthropic's Claude Opus 4.6 (implementation) + Tony (integrator)

---

## 1. Phase C3 Scope and Execution Model

### What Phase C3 delivers

Jupiter is the first gas giant migration and the introduction of three new geometry patterns that Saturn, Uranus, and Neptune will reuse in Phase C4: ring system, plasma torus, and multi-belt radiation belts. Jupiter is also the body that triggers promotion of the shared ring-points helper to `orrery_rendering.py`.

After Phase C3:

- **Jupiter** renders via `SHELL_CONFIGS['Jupiter']` (6 sphere shells, including mesh3d cloud layer) and `CUSTOM_SHELLS['Jupiter']` (4 entries: magnetosphere, io_plasma_torus, radiation_belts, ring_system).
- `create_ring_points_saturn` is promoted to `orrery_rendering.create_ring_points()`. Saturn's `saturn_visualization_shells.py`, plus Uranus and Neptune shell files, are updated to import from the new location.
- The Jupiter magnetosphere builder gets `rotate_to_sunward()` applied to its single magnetosphere geometry trace (Jupiter has no bow shock in the source -- Tony decision: preserve the no-bow-shock status quo as Tony decision Q5/(b)).
- Nine old-style info markers (1 magnetosphere, 1 Io torus, 3 radiation belts, 4 rings) are replaced with `create_info_marker()`.
- Four per-shell `create_sun_direction_indicator` calls in the custom geometry builders are removed (magnetosphere, io_plasma_torus, radiation_belts, ring_system).
- Jupiter's dispatch block in `planet_visualization.py` is replaced with a one-line delegation.

After Phase C3:

| Component | Before C3 | After C3 |
|---|:---:|:---:|
| Bodies in SHELL_CONFIGS | 8 | 9 |
| Total sphere shell configs | 46 | 52 |
| Bodies in CUSTOM_SHELLS | 4 | 5 |
| Total custom entries | 7 | 11 |
| Helpers in `orrery_rendering.py` | 3 | 4 (add `create_ring_points`) |
| Bodies still on old dispatch | 5 | 4 |

Four bodies remain on the old dispatch path after C3 (Saturn, Uranus, Neptune; plus Sun via `create_sun_visualization`).

### What Phase C3 explicitly does NOT do

- Does NOT add a bow shock to Jupiter's magnetosphere. Tony decision Q5/(b): preserve no-bow-shock source structure. Editorial enhancement of Jupiter and gas giants' magnetospheres is post-C4 work.
- Does NOT change Jupiter's radiation belt geometry to track magnetic axis. The source generates belts in the equatorial plane (rotational axis aligned), matching Earth Van Allen / Mars crustal fields precedent. Tony decision Q2: keep unrotated. `magnetic_tilt_deg` parameter accepts a value but is not yet applied; Phase C4 considers wiring it for Uranus (60 deg) and Neptune (47 deg). For Jupiter (~10 deg) the default 0 is acceptable.
- Does NOT modify `jupiter_visualization_shells.py` sphere shell functions. They become unreachable from the dispatch but stay in place; custom geometry siblings still use the same file. Phase D decides per-function fate.
- Does NOT touch `palomas_orrery.py`. Jupiter's GUI checkboxes and shell_vars wiring continue working through the unified dispatch.
- Does NOT retire `create_planet_visualization()`. Four bodies still use it. Phase D retires it.
- Does NOT strip the commented-out sun indicator at line 857 in the magnetosphere section. Tony decision: leave alone (out of scope, mechanical purity).
- Does NOT change Jupiter's local `create_ring_points_jupiter` helper. It has a different algorithm than Saturn's (explicit 3-z-layer thickness vs. random z-jitter). It continues to live in `jupiter_visualization_shells.py` and continues to be called by `create_jupiter_ring_system`. Only Saturn's helper is promoted.

### Execution order (canonical)

C3 has six top-level sections. Each section is atomic. Run the syntax check at the end of each section before starting the next.

1. **Pre-flight verification** (Section 2)
2. **Promote `create_ring_points_saturn` to `orrery_rendering.py`** (Section 3) -- enables clean C4 inherit
3. **Jupiter sphere configs** (Section 4) -- auto-generation + insertion
4. **Jupiter custom geometry refactor** (Section 5) -- magnetosphere, Io torus, radiation belts, ring system. Subsections per builder.
5. **CUSTOM_SHELLS entries + delegation** (Section 6)
6. **Verification plan** (Section 7)

If any step fails its syntax check, STOP and resolve before proceeding.

### Why this order matters

Section 3 (the ring helper promotion) is independent of Jupiter's migration but logically C3 work because it sets up clean C4 inheritance. Doing it first means C4's Saturn/Uranus/Neptune ring sections can simply import from `orrery_rendering` and skip the cross-module-import hack.

Section 4 (sphere configs) is mechanical -- same auto-generation pattern as C1/C2. Done before Section 5 because Section 5's custom geometry refactor is the largest single change in C3.

Section 5 has four subsections (one per custom builder). Each can be a session-boundary stop point: 5.1 (magnetosphere) is the most involved; 5.2-5.4 (Io torus, radiation belts, ring system) are info-marker-replacement plus sun-indicator-removal.

Section 6 (registry entries + delegation) is the final mechanical step. Can be combined with Section 5's last subsection if context allows.

Clean session boundaries: end of Section 3, end of Section 4, after any subsection in Section 5.

---

## 2. Pre-flight Verification

### 2.1 Confirm Phase A+B+C1+C2 are in place

```bash
python3 -c "
from orrery_rendering import build_sphere_shell, create_info_marker, rotate_to_sunward
from shell_configs import SHELL_CONFIGS, CUSTOM_SHELLS

expected_sphere = {'Mercury', 'Moon', 'Planet 9', 'Pluto', 'Eris', 'Venus', 'Mars', 'Earth'}
expected_custom = {'Mercury', 'Venus', 'Mars', 'Earth'}

for body in expected_sphere:
    assert body in SHELL_CONFIGS, 'Phase A-C2 body %s missing from SHELL_CONFIGS' % body
for body in expected_custom:
    assert body in CUSTOM_SHELLS, 'Phase A-C2 custom body %s missing' % body

assert 'Jupiter' not in SHELL_CONFIGS, 'Jupiter already present - re-run?'
assert 'Jupiter' not in CUSTOM_SHELLS, 'Jupiter already in CUSTOM_SHELLS - re-run?'

# Phase D items still deferred
assert len(SHELL_CONFIGS) == 8, 'Expected 8 bodies in SHELL_CONFIGS, got %d' % len(SHELL_CONFIGS)
assert len(CUSTOM_SHELLS) == 4, 'Expected 4 bodies in CUSTOM_SHELLS, got %d' % len(CUSTOM_SHELLS)

print('Phase A-C2 baseline OK')
"
```

If anything fails, STOP -- Phase C3 assumes Phase A-C2 are complete.

### 2.2 Confirm `create_ring_points_saturn` exists in `saturn_visualization_shells.py`

```bash
grep -n "^def create_ring_points_saturn" saturn_visualization_shells.py
# Expected: one match around line 23
```

The helper that Phase C3 promotes. If missing, STOP -- Saturn source is unexpected state.

### 2.3 Confirm Jupiter source is post-Step-2

```bash
grep "Module updated" jupiter_visualization_shells.py | head -1
# Expected: "May 2026 with Anthropic's Claude Opus 4.7"

grep -c "hoverinfo='skip'" jupiter_visualization_shells.py
# Expected: at least 10 (one per geometry trace; sphere shells 6, magnetosphere 1, io torus 1, 3 belts, 4 rings = 15)

file jupiter_visualization_shells.py
# Expected: ASCII text, no CRLF

grep -c "^def create_" jupiter_visualization_shells.py
# Expected: 11 (1 helper + 6 sphere + 4 custom)
```

### 2.4 Confirm CENTER_BODY_RADII has Jupiter

```bash
python3 -c "
from constants_new import CENTER_BODY_RADII, KM_PER_AU
print('Jupiter: %.2f km = %.4e AU' % (CENTER_BODY_RADII['Jupiter'], CENTER_BODY_RADII['Jupiter']/KM_PER_AU))
"
# Expected: 71492.00 km = 4.7790e-04 AU (IAU 2015 nominal equatorial)
```

### 2.5 Confirm Jupiter's dispatch block is present in planet_visualization.py

```bash
grep -n "if planet_name == 'Jupiter':" planet_visualization.py
# Expected: one match around line 745

sed -n "/if planet_name == .Jupiter./,/^    if planet_name == /p" planet_visualization.py | head -25
# Expected: 10 if-statements (core through hill_sphere), then Saturn block
```

The dispatch block has 10 shell toggles. Phase C3 replaces it with a one-line delegation.

### 2.6 Backup files Phase C3 will touch

Before any edits:

```
shell_configs.py                    -> shell_configs.py.phaseC3_backup
planet_visualization.py             -> planet_visualization.py.phaseC3_backup
orrery_rendering.py                 -> orrery_rendering.py.phaseC3_backup
jupiter_visualization_shells.py     -> jupiter_visualization_shells.py.phaseC3_backup
saturn_visualization_shells.py      -> saturn_visualization_shells.py.phaseC3_backup
uranus_visualization_shells.py      -> uranus_visualization_shells.py.phaseC3_backup
neptune_visualization_shells.py     -> neptune_visualization_shells.py.phaseC3_backup
```

Seven files. The Saturn/Uranus/Neptune touch is light (one-line import update each) but they're modified, so backup.

### 2.7 Line ending and ASCII verification

```bash
for f in shell_configs.py planet_visualization.py orrery_rendering.py \
         jupiter_visualization_shells.py saturn_visualization_shells.py \
         uranus_visualization_shells.py neptune_visualization_shells.py; do
    file "$f" | grep -q CRLF && echo "FAIL: $f CRLF" || echo "OK LF: $f"
done

python3 -c "
files = ['shell_configs.py', 'planet_visualization.py', 'orrery_rendering.py',
         'jupiter_visualization_shells.py', 'saturn_visualization_shells.py',
         'uranus_visualization_shells.py', 'neptune_visualization_shells.py']
for f in files:
    with open(f, 'rb') as fh:
        content = fh.read().decode('utf-8', errors='replace')
    issues = sum(1 for c in content if ord(c) > 127)
    print('%-45s %s' % (f, 'OK ASCII' if not issues else 'FAIL: %d non-ASCII' % issues))
"
```

All seven files must be LF and ASCII. If any of the gas giant shell files (Saturn, Uranus, Neptune) report non-ASCII or CRLF, treat as a pre-C3 problem -- those files are touched but the touch is minimal (one import line). Apply the Phase C1 Section 3 ASCII cleanup method first if needed.

---

## 3. Promote `create_ring_points_saturn` to `orrery_rendering.py`

The helper currently lives in `saturn_visualization_shells.py` line 23 and is imported by Uranus (line 20) and Neptune (line 23). Promoting it to `orrery_rendering.py` gives C4 a clean inherit pattern and centralizes ring geometry alongside `build_sphere_shell`.

### 3.1 Why now (and not in C4)

C3 introduces the first ring CUSTOM_SHELLS entry (`'Jupiter': {'ring_system': ...}`). C4 adds three more (Saturn, Uranus, Neptune). Doing the promotion now means:

1. C3's Jupiter ring system can lazy-import from `orrery_rendering.create_ring_points` if we choose to converge Jupiter's local helper later (Phase D editorial work, not C3 scope).
2. C4's three subsections each have a clean import path with no cross-module gymnastics.
3. The dependency graph simplifies: `uranus_visualization_shells.py` no longer imports `saturn_visualization_shells.py`, breaking a circular-import risk.

Cost: three additional one-line edits (Saturn/Uranus/Neptune import updates) plus the helper code move.

### 3.2 Add `create_ring_points()` to `orrery_rendering.py`

Append to `orrery_rendering.py` (after `rotate_to_sunward()`):

```python
def create_ring_points(inner_radius, outer_radius, n_points, thickness=0):
    """Create points for a planetary ring with inner and outer radii.

    Promoted from saturn_visualization_shells.py in Phase C3 for use by
    Saturn, Uranus, and Neptune ring builders. Jupiter's ring builder
    (with a different algorithm using explicit z-layer thickness) keeps
    its local helper.

    Parameters:
        inner_radius (float): Inner radius of the ring in AU
        outer_radius (float): Outer radius of the ring in AU
        n_points (int): Number of angular points; radial sampling is n_points/10
        thickness (float): Thickness of the ring in z-direction (AU).
                           0.0 means flat ring (z=0 for all points).

    Returns:
        (x, y, z): tuple of flat numpy arrays of point coordinates
    """
    # Generate angular positions
    theta = np.linspace(0, 2 * np.pi, n_points)

    # Calculate radial positions (sparse radial sampling for ring visualization)
    r = np.linspace(inner_radius, outer_radius, int(n_points / 10))

    # Create a meshgrid for combinations
    theta_grid, r_grid = np.meshgrid(theta, r)

    # Convert to cartesian coordinates
    x = r_grid.flatten() * np.cos(theta_grid.flatten())
    y = r_grid.flatten() * np.sin(theta_grid.flatten())

    # Add some thickness in z-direction if specified
    if thickness > 0:
        z = np.random.uniform(-thickness / 2, thickness / 2, size=x.shape)
    else:
        z = np.zeros_like(x)

    return x, y, z
```

This is a verbatim copy of `create_ring_points_saturn` with two changes:
1. Renamed to `create_ring_points` (drop body-specific suffix)
2. Updated docstring to note the promotion provenance

### 3.3 Update `saturn_visualization_shells.py`

**Change 1**: Add at the top of the file (after existing imports):

```python
from orrery_rendering import create_ring_points
```

**Change 2**: Delete the local `create_ring_points_saturn` function definition (lines 23-37 approximately -- verify exact range by `grep`).

**Change 3**: Update the call site at line 1214 (approximately):

```python
        x, y, z = create_ring_points_saturn (inner_radius_au, outer_radius_au, n_points, thickness_au)
```

becomes:

```python
        x, y, z = create_ring_points(inner_radius_au, outer_radius_au, n_points, thickness_au)
```

(Note the extra space in `create_ring_points_saturn (` -- preserve clean call after rename.)

### 3.4 Update `uranus_visualization_shells.py`

**Change 1**: Update the import at line 20 (approximately):

```python
from saturn_visualization_shells import create_ring_points_saturn
```

becomes:

```python
from orrery_rendering import create_ring_points
```

**Change 2**: Update the call site at line 1029 (approximately):

```python
        x, y, z = create_ring_points_saturn (inner_radius_au, outer_radius_au, n_points, thickness_au)
```

becomes:

```python
        x, y, z = create_ring_points(inner_radius_au, outer_radius_au, n_points, thickness_au)
```

### 3.5 Update `neptune_visualization_shells.py`

**Change 1**: Update the import at line 23 (approximately):

```python
from saturn_visualization_shells import create_ring_points_saturn
```

becomes:

```python
from orrery_rendering import create_ring_points
```

**Change 2**: Update the call site at line 1678 (approximately):

```python
            x, y, z = create_ring_points_saturn(
                inner_radius_au, outer_radius_au, n_points, thickness_au
            )
```

becomes:

```python
            x, y, z = create_ring_points(
                inner_radius_au, outer_radius_au, n_points, thickness_au
            )
```

### 3.6 Verification after Section 3

```bash
python3 -m py_compile orrery_rendering.py saturn_visualization_shells.py \
    uranus_visualization_shells.py neptune_visualization_shells.py

# Verify the new helper works
python3 -c "
from orrery_rendering import create_ring_points
import numpy as np

# Standard call (matches saturn's main ring scenario)
x, y, z = create_ring_points(0.001, 0.002, 100, thickness=1e-7)
assert len(x) == len(y) == len(z)
assert x.shape == y.shape == z.shape
# Radial sampling = 100/10 = 10 radial * 100 angular = 1000 points
assert len(x) == 1000, 'Expected 1000 points, got %d' % len(x)
# All points between inner and outer radius (within tolerance)
r = np.sqrt(x**2 + y**2)
assert np.all(r >= 0.001 - 1e-12) and np.all(r <= 0.002 + 1e-12)
# Thickness check
assert np.all(np.abs(z) <= 1e-7 / 2)
print('create_ring_points smoke test PASS')
"

# Verify Saturn/Uranus/Neptune builders still work
python3 -c "
import importlib
for mod_name in ['saturn_visualization_shells', 'uranus_visualization_shells',
                  'neptune_visualization_shells']:
    mod = importlib.import_module(mod_name)
    # No cross-saturn imports
    src = open(mod.__file__).read()
    if mod_name != 'saturn_visualization_shells':
        assert 'create_ring_points_saturn' not in src, \
            'Lingering create_ring_points_saturn reference in %s' % mod_name
print('Cross-module import cleanup PASS')
"

# Ring system builders should still produce traces
python3 -c "
import importlib
mod = importlib.import_module('saturn_visualization_shells')
traces = mod.create_saturn_ring_system((0, 0, 0))
assert len(traces) > 0
print('Saturn ring_system smoke: %d traces' % len(traces))

mod = importlib.import_module('uranus_visualization_shells')
traces = mod.create_uranus_ring_system((0, 0, 0))
assert len(traces) > 0
print('Uranus ring_system smoke: %d traces' % len(traces))

mod = importlib.import_module('neptune_visualization_shells')
traces = mod.create_neptune_ring_system((0, 0, 0))
assert len(traces) > 0
print('Neptune ring_system smoke: %d traces' % len(traces))
"
```

All three gas giant ring builders must produce traces without error. Their dispatch path is still the old `create_planet_visualization()` -- C3 doesn't migrate them. C3 only migrates Jupiter and updates the ring helper plumbing.

If anything fails, STOP and debug before proceeding to Section 4.

---

## 4. Jupiter Sphere Configs

Jupiter has 6 sphere shells. Five are standard (`layer_info` dict pattern, `create_sphere_points`), one is mesh3d (cloud_layer). Hill sphere also uses `layer_info` dict (different from Earth/Moon's local-variable pattern).

### 4.1 Auto-generation script

Save as `generate_phase_c3_jupiter_configs.py` and run from the project directory:

```python
# generate_phase_c3_jupiter_configs.py
# Reads jupiter_visualization_shells.py and produces config blocks.
# No n_points standardization needed -- Step 2 already set Hill sphere to 20.
import re

N_POINTS_HILL_SPHERE = 20
GEOMETRY_TYPE_CLOUD = 'mesh3d'
MESH_RESOLUTION = 24

BODY = 'Jupiter'
PATH = 'jupiter_visualization_shells.py'

SHELLS = [
    ('core',              'create_jupiter_core_shell',              'jupiter_core_info'),
    ('metallic_hydrogen', 'create_jupiter_metallic_hydrogen_shell', 'jupiter_metallic_hydrogen_info'),
    ('molecular_hydrogen','create_jupiter_molecular_hydrogen_shell','jupiter_molecular_hydrogen_info'),
    ('cloud_layer',       'create_jupiter_cloud_layer_shell',       'jupiter_cloud_layer_info'),
    ('upper_atmosphere',  'create_jupiter_upper_atmosphere_shell',  'jupiter_upper_atmosphere_info'),
    ('hill_sphere',       'create_jupiter_hill_sphere_shell',       'jupiter_hill_sphere_info'),
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


def extract_marker_size(body_src):
    """Inline Scatter3d marker size for the geometry trace (not the info marker)."""
    m = re.search(r"go\.Scatter3d\([^)]*?\bmarker=dict\(\s*\n?\s*size\s*=\s*([\d.]+)",
                  body_src, re.DOTALL)
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
        # Hill sphere already 20 in source; no standardization needed
        effective_np = np_val
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

print('# Generated by generate_phase_c3_jupiter_configs.py')
print('# Review carefully before inserting into shell_configs.py')
print('# Place inside SHELL_CONFIGS dict after the Earth block.')
print()
print(f"    # ============================================================")
print(f"    # Jupiter")
print(f"    # ============================================================")
print(f"    # Source: NASA Juno Mission; Wahl et al. (2017) for core;")
print(f"    #         NASA Solar System Exploration; NASA Juno gravity science")
print(f"    #         (fuzzy core to ~60% R_J).")
print(f"    # Verified: April 2026 provenance audit via Gemini fact-check.")
print(''.join(out))
```

Run with:

```bash
python3 generate_phase_c3_jupiter_configs.py > phase_c3_jupiter_configs.txt
```

Review the output before insertion.

### 4.2 Expected values (verification reference)

The generated config should produce these values:

| Shell | radius_fraction | color | opacity | n_points / mesh_resolution | marker_size | name |
|---|---:|---|---:|:---:|---:|---|
| `core` | 0.1 | rgb(175, 175, 255) | 1.0 | 25 | 4.0 | 'Core' |
| `metallic_hydrogen` | 0.8 | rgb(225, 225, 255) | 0.9 | 25 | 3.5 | 'Metallic Hydrogen Layer' |
| `molecular_hydrogen` | 0.97 | rgb(255, 255, 200) | 0.5 | 25 | 3.0 | 'Molecular Hydrogen Layer' |
| `cloud_layer` (mesh3d) | 1.0 | rgb(255, 255, 235) | 1.0 | 24 (mesh_res) | -- | 'Cloud Layer' |
| `upper_atmosphere` | 1.1 | rgb(220, 240, 255) | 0.5 | 20 | 3.0 | 'Upper Atmosphere' |
| `hill_sphere` | 740 | rgb(0, 255, 0) | 0.25 | 20 | 2.0 | 'Hill Sphere' |

Notes:

1. **Hill sphere uses `layer_info` dict pattern** (like Mercury), not local-variable pattern (like Earth/Moon). All values are in the dict; n_points and marker_size are from the inline Scatter3d call. The auto-generation script handles both patterns.

2. **No n_points standardization needed** -- Step 2 already set Jupiter's Hill sphere to 20.

3. **`marker_size=2.0` for Hill sphere** -- preserved from source. Mercury/Moon Hill spheres use 1.0; Jupiter source has 2.0 explicitly. Preserve.

4. **`cloud_layer` (not `crust`)** -- gas giants have cloud layers, not crusts. Same mesh3d pattern as terrestrial crusts. Color rgb(255, 255, 235) (warm white -- Jupiter's actual cloud color).

5. **Layer names with "Layer" suffix** -- 'Metallic Hydrogen Layer', 'Molecular Hydrogen Layer' (source values). Verbose but distinct from terrestrial mantle/core nomenclature. Legend renders as "Jupiter: Metallic Hydrogen Layer".

### 4.3 Manual review checklist before inserting

Same as C2 Section 3.3. Per-block, verify:
- `radius_fraction` is a float (or large int 740 for Hill sphere).
- `color` is in `'rgb(R, G, B)'` format.
- `opacity` is a float between 0 and 1.
- Cloud layer has `geometry_type='mesh3d'` and `mesh_resolution=24` (NO n_points, NO marker_size).
- All other entries have n_points and marker_size.
- Hover text contains `<br>` line breaks.
- Tooltip contains `\n` line breaks.
- All apostrophes are ASCII.
- Hill sphere `n_points=20` and `marker_size=2.0`.

If any block looks wrong, STOP and resolve with Tony.

### 4.4 Insert configs into shell_configs.py

Locate the closing of the Earth block (Phase C2's last addition). The Jupiter block goes BEFORE the closing of `SHELL_CONFIGS`. Match indentation exactly.

### 4.5 Verification after Section 4

```bash
python3 -m py_compile shell_configs.py

python3 -c "
from shell_configs import SHELL_CONFIGS
assert 'Jupiter' in SHELL_CONFIGS
jupiter = SHELL_CONFIGS['Jupiter']
expected = {'core', 'metallic_hydrogen', 'molecular_hydrogen', 'cloud_layer',
            'upper_atmosphere', 'hill_sphere'}
assert set(jupiter.keys()) == expected, 'Jupiter shell keys: %s' % sorted(jupiter.keys())
assert jupiter['core']['radius_fraction'] == 0.1
assert jupiter['hill_sphere']['radius_fraction'] == 740
assert jupiter['hill_sphere']['n_points'] == 20
assert jupiter['hill_sphere']['marker_size'] == 2.0
assert jupiter['cloud_layer']['geometry_type'] == 'mesh3d'

from orrery_rendering import build_sphere_shell
for shell_name, cfg in jupiter.items():
    traces = build_sphere_shell(cfg, 'Jupiter', (0, 0, 0))
    assert len(traces) == 2

print('Jupiter sphere configs verified')
"
```

---

## 5. Jupiter Custom Geometry Refactor

Four custom builders to refactor. Each gets: (1) import additions if not already present, (2) sun indicator removal, (3) info marker style update, plus magnetosphere-specific work in 5.1.

### 5.1 Magnetosphere refactor

Jupiter's magnetosphere builder is the most substantive subsection.

**Current state** (lines 515-586 approximately):
- Generates magnetosphere geometry with default `-X` sunward (no rotation).
- Single geometry trace + single info marker (NO bow shock -- Tony Q5 decision: preserve).
- Per-shell `create_sun_direction_indicator` call at end.
- Old-style info marker (size=6, white outline).

**After refactor**:
- Magnetosphere geometry: `rotate_to_sunward()` applied.
- Info marker: `create_info_marker()` (size=8, red outline).
- Sun indicator call removed.
- Trace count unchanged: 2 traces total (1 geometry + 1 info marker).

#### 5.1.1 Import additions at top of file

In `jupiter_visualization_shells.py`, find the existing import block. Add:

```python
from orrery_rendering import rotate_to_sunward, create_info_marker
```

Place near the existing imports. The `from shared_utilities import create_sun_direction_indicator` import remains -- it's still used by Jupiter's `upper_atmosphere` and `hill_sphere` sphere shell functions (which become unreachable but stay in place). Phase D removes the import.

#### 5.1.2 Apply sunward rotation to magnetosphere geometry

Current source (lines 537-545 approximately):

```python
    # Create magnetosphere main shape
    x, y, z = create_magnetosphere_shape(params)
    
    # Unpack center position
    center_x, center_y, center_z = center_position
    
    # Apply center position offset
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
    
    # Rotate to actual sunward direction, then offset to center position
    x, y, z = np.array(x), np.array(y), np.array(z)
    x, y, z = rotate_to_sunward(x, y, z, center_position=center_position)
    x = x + center_x
    y = y + center_y
    z = z + center_z
```

Pattern matches Phase C2 Earth exactly.

#### 5.1.3 Replace magnetosphere info marker

Current source (lines 566-577 approximately):

```python
    traces.append(go.Scatter3d(
        x=[x[0]], y=[y[0]], z=[z[0]],
        mode='markers',
        marker=dict(size=6, color='rgb(200, 200, 255)', opacity=0.9,
                    symbol='cross', line=dict(color='white', width=1)),
        name='',
        legendgroup='Jupiter: Magnetosphere',
        text=[mag_desc],
        customdata=['Jupiter: Magnetosphere'],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    ))
```

Replace with:

```python
    traces.append(create_info_marker(
        x[0], y[0], z[0],
        'rgb(200, 200, 255)', mag_desc, 'Jupiter: Magnetosphere'
    ))
```

Note: `mag_desc` in the source is already a plain string (not a list -- see line 562). Pass directly.

#### 5.1.4 Remove the per-shell sun direction indicator call

Current source (lines 579-584 approximately):

```python
    sun_traces = create_sun_direction_indicator(
        center_position=center_position, 
        shell_radius=500 * JUPITER_RADIUS_AU
    )
    for trace in sun_traces:
        traces.append(trace)

    return traces
```

Replace with:

```python
    return traces
```

The unified dispatch handles indicator placement.

### 5.2 Io plasma torus refactor

Smaller subsection. Three changes: info marker update, sun indicator removal. (Rotation is NOT applied -- Tony Q3 decision: Io torus stays unrotated. Equatorially confined, not solar-wind-driven.)

#### 5.2.1 Replace Io torus info marker

Current source (lines 656-667 approximately, in `create_jupiter_io_plasma_torus`):

```python
    traces.append(go.Scatter3d(
        x=[io_torus_x[0]], y=[io_torus_y[0]], z=[io_torus_z[0]],
        mode='markers',
        marker=dict(size=6, color='rgb(255, 100, 100)', opacity=0.9,
                    symbol='cross', line=dict(color='white', width=1)),
        name='',
        legendgroup='Jupiter: Io Plasma Torus',
        text=[io_desc],
        customdata=['Jupiter: Io Plasma Torus'],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    ))
```

Replace with:

```python
    traces.append(create_info_marker(
        io_torus_x[0], io_torus_y[0], io_torus_z[0],
        'rgb(255, 100, 100)', io_desc, 'Jupiter: Io Plasma Torus'
    ))
```

#### 5.2.2 Remove per-shell sun indicator

Current source (lines 669-674 approximately):

```python
    sun_traces = create_sun_direction_indicator(
        center_position=center_position, 
        shell_radius=io_torus_distance
    )
    for trace in sun_traces:
        traces.append(trace)

    return traces
```

Replace with:

```python
    return traces
```

### 5.3 Radiation belts refactor

Three belts emitted by a single builder (Inner, Middle, Outer). One sun indicator at end. Three info markers inside the belt loop (one per belt).

Important: Jupiter's belts are coded around the rotational axis (equatorial plane with z-modulation). NOT rotated -- Tony Q2 decision matches Earth Van Allen / Mars crustal fields precedent.

#### 5.3.1 Replace per-belt info marker (inside the loop)

Current source (lines 761-774 approximately, inside `for i, belt_distance in enumerate(belt_distances):` loop):

```python
        traces.append(
            go.Scatter3d(
                x=[belt_x[0]], y=[belt_y[0]], z=[belt_z[0]],
                mode='markers',
                marker=dict(size=6, color=belt_colors[i], opacity=0.9,
                            symbol='cross', line=dict(color='white', width=1)),
                name='',
                legendgroup=belt_names[i],
                text=[belt_texts[i]],
                customdata=[belt_names[i]],
                hovertemplate='%{text}<extra></extra>',
                showlegend=False
            )
        )
```

Replace with:

```python
        traces.append(create_info_marker(
            belt_x[0], belt_y[0], belt_z[0],
            belt_colors[i], belt_texts[i], belt_names[i]
        ))
```

This appears once in the source but executes three times (once per belt) because it's inside the belt loop. The `belt_texts[i]` is a plain string (not wrapped in a list), so pass directly.

#### 5.3.2 Remove per-shell sun indicator

Current source (lines 776-781 approximately):

```python
    sun_traces = create_sun_direction_indicator(
        center_position=center_position, 
        shell_radius= 6.0 * JUPITER_RADIUS_AU
    )
    for trace in sun_traces:
        traces.append(trace)

    return traces
```

Replace with:

```python
    return traces
```

### 5.4 Ring system refactor

Four rings emitted by a single builder (Main, Halo, Amalthea Gossamer, Thebe Gossamer). One sun indicator at end. Four info markers inside the ring loop (one per ring).

Important: Jupiter's rings are equatorial. NOT rotated -- Tony Q4 decision: rings stay in body's equatorial plane regardless of Sun direction.

The ring builder uses `create_ring_points_jupiter` (the local helper). Per Tony decision Q1: Jupiter keeps its local helper. Don't change the ring point generation.

#### 5.4.1 Replace per-ring info marker (inside the loop)

Current source (lines 1009-1022 approximately, inside `for ring_name, ring_info in ring_params.items():` loop):

```python
        traces.append(
            go.Scatter3d(
                x=[ring_marker_x], y=[center_y], z=[center_z],
                mode='markers',
                marker=dict(size=6, color=ring_info['color'], opacity=0.9,
                            symbol='cross', line=dict(color='white', width=1)),
                name='',
                legendgroup=f"Jupiter: {ring_info['name']}",
                text=[ring_info['description']],
                customdata=[f"Jupiter: {ring_info['name']}"],
                hovertemplate='%{text}<extra></extra>',
                showlegend=False
            )
        )
```

Replace with:

```python
        traces.append(create_info_marker(
            ring_marker_x, center_y, center_z,
            ring_info['color'], ring_info['description'],
            f"Jupiter: {ring_info['name']}"
        ))
```

This appears once in the source but executes four times (once per ring). The `ring_info['description']` is a plain string (concatenated via `<br>` joins), pass directly.

#### 5.4.2 Remove per-shell sun indicator

Current source (lines 1024-1029 approximately):

```python
    sun_traces = create_sun_direction_indicator(
        center_position=center_position, 
        shell_radius=226000 / KM_PER_AU
    )
    for trace in sun_traces:
        traces.append(trace)

    return traces
```

Replace with:

```python
    return traces
```

### 5.5 Verification after Section 5

```bash
python3 -m py_compile jupiter_visualization_shells.py

python3 -c "
# Verify Jupiter custom builders still work
import importlib
mod = importlib.import_module('jupiter_visualization_shells')

# Magnetosphere: 1 geometry + 1 info marker = 2 traces
# (No bow shock per Tony Q5 decision)
traces = mod.create_jupiter_magnetosphere((0, 0, 0))
assert len(traces) == 2, 'magnetosphere: expected 2 traces (no bow shock), got %d' % len(traces)

# Io torus: 1 geometry + 1 info marker = 2 traces
traces = mod.create_jupiter_io_plasma_torus((0, 0, 0))
assert len(traces) == 2

# Radiation belts: 3 belts each with 1 geometry + 1 info marker = 6 traces
traces = mod.create_jupiter_radiation_belts((0, 0, 0))
assert len(traces) == 6, 'belts: expected 6 traces, got %d' % len(traces)

# Ring system: 4 rings each with 1 geometry + 1 info marker = 8 traces
traces = mod.create_jupiter_ring_system((0, 0, 0))
assert len(traces) == 8, 'rings: expected 8 traces, got %d' % len(traces)

print('Jupiter custom geometry verification PASS')
print('  magnetosphere: 2 traces (no bow shock per Tony Q5)')
print('  io_plasma_torus: 2 traces')
print('  radiation_belts: 6 traces (3 belts)')
print('  ring_system: 8 traces (4 rings)')
"
```

### 5.6 Verify rotation is applied to magnetosphere only

```bash
python3 -c "
import importlib
import numpy as np

mod = importlib.import_module('jupiter_visualization_shells')

# Magnetosphere at origin (no rotation)
traces_origin = mod.create_jupiter_magnetosphere((0, 0, 0))

# Magnetosphere at -X (180-degree rotation)
traces_off = mod.create_jupiter_magnetosphere((-1.0, 0.0, 0.0))

# First trace is the magnetosphere geometry
origin_x = np.array(traces_origin[0].x)
off_x = np.array(traces_off[0].x) - (-1.0)  # Remove offset

# After 180-degree rotation, x should be negated
assert np.allclose(off_x, -origin_x, atol=1e-9), \
    'Magnetosphere not rotating: x not negated for Jupiter at -X'

# Belts should NOT rotate -- verify Inner belt geometry unchanged
belts_origin = mod.create_jupiter_radiation_belts((0, 0, 0))
belts_off = mod.create_jupiter_radiation_belts((-1.0, 0.0, 0.0))

# First trace is Inner belt geometry
inner_origin_x = np.array(belts_origin[0].x)
inner_off_x = np.array(belts_off[0].x) - (-1.0)  # Remove offset only

# Belts should be unchanged (just offset, not rotated)
assert np.allclose(inner_off_x, inner_origin_x, atol=1e-9), \
    'Radiation belts unexpectedly rotated'

# Same for Io torus
torus_origin = mod.create_jupiter_io_plasma_torus((0, 0, 0))
torus_off = mod.create_jupiter_io_plasma_torus((-1.0, 0.0, 0.0))
torus_origin_x = np.array(torus_origin[0].x)
torus_off_x = np.array(torus_off[0].x) - (-1.0)
# Io torus uses random jitter (np.random) -- can't compare exactly, but
# the geometry shape (range of x values) should be the same
assert abs(torus_origin_x.max() - torus_off_x.max()) < 0.001, \
    'Io torus unexpectedly rotated'

# Same for Ring system - first ring's geometry
rings_origin = mod.create_jupiter_ring_system((0, 0, 0))
rings_off = mod.create_jupiter_ring_system((-1.0, 0.0, 0.0))
ring_origin_x = np.array(rings_origin[0].x)
ring_off_x = np.array(rings_off[0].x) - (-1.0)
# Ring uses Jupiter's ring helper with deterministic point distribution
# Same point pattern -> same x values
assert abs(ring_origin_x.max() - ring_off_x.max()) < 1e-6, \
    'Ring system unexpectedly rotated'

print('Rotation isolation PASS:')
print('  Magnetosphere: rotates (180 deg test)')
print('  Radiation belts: not rotated (unchanged)')
print('  Io torus: not rotated (unchanged shape)')
print('  Ring system: not rotated (unchanged shape)')
"
```

This is the headline correctness test for C3. Rotation applies to the magnetosphere only; belts, Io torus, and rings stay in Jupiter's body frame regardless of Sun direction.

If any assertion fails, STOP and debug before proceeding to Section 6.

---

## 6. CUSTOM_SHELLS Entries + Delegation

### 6.1 Add Jupiter to CUSTOM_SHELLS

In `shell_configs.py`, locate the `CUSTOM_SHELLS = {` dict. After the Earth block (Phase C2's last addition), add:

```python

    # ============================================================
    # Jupiter
    # ============================================================
    # Source: NASA Juno Mission; NASA Galileo Mission; NASA Voyager 1/2;
    #         Galileo plasma instrument data (Io torus);
    #         NASA Jupiter Magnetosphere Overview.
    # Verified: April 2026 provenance audit via Gemini fact-check.
    'Jupiter': {

        'magnetosphere': {
            'builder': 'jupiter_visualization_shells.create_jupiter_magnetosphere',
            'tooltip': (
                "SET MANUAL SCALE TO AT LEAST 0.5 AU TO VISUALIZE.\n"
                "1.3 MB PER FRAME FOR HTML.\n\n"
                "Jupiter's magnetosphere is the largest in the solar system, extending up to\n"
                "~100 Jupiter radii on the sunward side and forming a magnetotail stretching\n"
                "beyond Saturn's orbit in the opposite direction. It traps charged particles,\n"
                "creating intense radiation belts that would be lethal to humans.\n\n"
                "Note: This visualization shows only the magnetosphere envelope. The bow shock\n"
                "(at ~80-100 R_J standoff) is not yet rendered; it can be added editorially in\n"
                "a future enhancement to match the Mercury/Venus/Mars/Earth pattern."
            ),
        },

        'io_plasma_torus': {
            'builder': 'jupiter_visualization_shells.create_jupiter_io_plasma_torus',
            'tooltip': (
                "SET MANUAL SCALE TO AT LEAST 0.005 AU TO VISUALIZE.\n"
                "634 KB PER FRAME FOR HTML.\n\n"
                "Donut-shaped region of charged particles from Jupiter's moon Io.\n"
                "Volcanic eruptions on Io eject sulfur and oxygen ions that become trapped\n"
                "in Jupiter's magnetic field, forming this distinctive structure at Io's\n"
                "orbital distance (~5.9 R_J). The torus is one of the brightest features in\n"
                "Jupiter's magnetosphere when viewed in UV wavelengths."
            ),
        },

        'radiation_belts': {
            'builder': 'jupiter_visualization_shells.create_jupiter_radiation_belts',
            'tooltip': (
                "SET MANUAL SCALE TO AT LEAST 0.005 AU TO VISUALIZE.\n\n"
                "Jupiter has three distinct radiation belts (Inner, Middle, Outer) at\n"
                "approximately 1.5, 3.0, and 6.0 Jupiter radii. Together they form the\n"
                "most intense radiation environment in the solar system -- thousands of\n"
                "times more intense than Earth's Van Allen belts.\n\n"
                "These regions trap high-energy charged particles in Jupiter's powerful\n"
                "magnetic field. The Galileo orbiter, Juno, and other spacecraft must\n"
                "carefully manage their trajectories to avoid prolonged exposure.\n\n"
                "The same builder produces all three traces (separate legend entries):\n"
                "Inner Radiation Belt, Middle Radiation Belt, Outer Radiation Belt."
            ),
        },

        'ring_system': {
            'builder': 'jupiter_visualization_shells.create_jupiter_ring_system',
            'tooltip': (
                "SET MANUAL SCALE TO AT LEAST 0.003 AU TO VISUALIZE.\n\n"
                "Jupiter's ring system is faint and dusty, discovered by Voyager 1 in 1979.\n"
                "It consists of four components:\n"
                "  * Main Ring (122,500-129,000 km): bright thin ring, dust from Metis and Adrastea\n"
                "  * Halo Ring (100,000-122,500 km): faint torus inside the Main Ring\n"
                "  * Amalthea Gossamer Ring (129,000-182,000 km): very faint, dust from Amalthea\n"
                "  * Thebe Gossamer Ring (129,000-226,000 km): faintest, dust from Thebe\n\n"
                "The rings lie in Jupiter's equatorial plane and are composed of fine dust\n"
                "particles ejected from small inner moons by micrometeoroid impacts.\n\n"
                "The same builder produces all four ring traces (separate legend entries)."
            ),
        },

    },

```

CUSTOM_SHELLS keys use the bare post-prefix-strip names matching the GUI vars (`jupiter_magnetosphere`, `jupiter_io_plasma_torus`, `jupiter_radiation_belts`, `jupiter_ring_system` -- all four exist in `palomas_orrery.py`).

### 6.2 Jupiter delegation in planet_visualization.py

Find the Jupiter dispatch block (lines 745-765 approximately):

```python
    if planet_name == 'Jupiter':
        if shell_vars['jupiter_core'].get() == 1:
            traces.extend(create_jupiter_core_shell(center_position))
        if shell_vars['jupiter_metallic_hydrogen'].get() == 1:
            traces.extend(create_jupiter_metallic_hydrogen_shell(center_position))
        if shell_vars['jupiter_molecular_hydrogen'].get() == 1:
            traces.extend(create_jupiter_molecular_hydrogen_shell(center_position))
        if shell_vars['jupiter_cloud_layer'].get() == 1:
            traces.extend(create_jupiter_cloud_layer_shell(center_position))
        if shell_vars['jupiter_upper_atmosphere'].get() == 1:
            traces.extend(create_jupiter_upper_atmosphere_shell(center_position))
        if shell_vars['jupiter_ring_system'].get() == 1:
            traces.extend(create_jupiter_ring_system(center_position))
        if shell_vars['jupiter_radiation_belts'].get() == 1:
            traces.extend(create_jupiter_radiation_belts(center_position))
        if shell_vars['jupiter_io_plasma_torus'].get() == 1:
            traces.extend(create_jupiter_io_plasma_torus(center_position))
        if shell_vars['jupiter_magnetosphere'].get() == 1:
            traces.extend(create_jupiter_magnetosphere(center_position))
        if shell_vars['jupiter_hill_sphere'].get() == 1:
            traces.extend(create_jupiter_hill_sphere_shell(center_position))
```

Replace with:

```python
    if planet_name == 'Jupiter':
        # Step 3 Phase C3: delegate to unified config-driven dispatch.
        # Custom geometry: jupiter_magnetosphere, jupiter_io_plasma_torus,
        # jupiter_radiation_belts (3 belts), jupiter_ring_system (4 rings)
        # via CUSTOM_SHELLS lazy import.
        return create_celestial_body_visualization(
            fig, planet_name, shell_vars,
            animate=animate, frames=frames,
            center_position=center_position,
            object_type='Jupiter',
            center_object='Jupiter',
        )
```

### 6.3 Bottom-up edit order

Apply edits in this order within `jupiter_visualization_shells.py` to prevent line-number drift (highest line numbers first):

1. Section 5.4.2: Ring sun indicator removal (~line 1024)
2. Section 5.4.1: Ring info marker (~line 1009)
3. Section 5.3.2: Belt sun indicator removal (~line 776)
4. Section 5.3.1: Belt info marker (~line 761)
5. Section 5.2.2: Io torus sun indicator removal (~line 669)
6. Section 5.2.1: Io torus info marker (~line 656)
7. Section 5.1.4: Magnetosphere sun indicator removal (~line 579)
8. Section 5.1.3: Magnetosphere info marker (~line 566)
9. Section 5.1.2: Magnetosphere rotation (~line 537)
10. Section 5.1.1: Imports at top of file

Note that `str_replace` is content-matching (location-independent), so order is discipline not correctness.

### 6.4 Final verification after Section 6

```bash
python3 -m py_compile shell_configs.py planet_visualization.py jupiter_visualization_shells.py

python3 -c "
from shell_configs import SHELL_CONFIGS, CUSTOM_SHELLS

assert 'Jupiter' in SHELL_CONFIGS and 'Jupiter' in CUSTOM_SHELLS

# 6 sphere shells
assert len(SHELL_CONFIGS['Jupiter']) == 6

# 4 custom shells
assert len(CUSTOM_SHELLS['Jupiter']) == 4
expected_custom = {'magnetosphere', 'io_plasma_torus', 'radiation_belts', 'ring_system'}
assert set(CUSTOM_SHELLS['Jupiter'].keys()) == expected_custom

# Smoke test: import via builder strings
import importlib
for name, entry in CUSTOM_SHELLS['Jupiter'].items():
    module_name, func_name = entry['builder'].rsplit('.', 1)
    mod = importlib.import_module(module_name)
    func = getattr(mod, func_name)
    traces = func((0, 0, 0))
    assert len(traces) > 0, '%s returned no traces' % name

# Verify dispatch is in place
import inspect
import planet_visualization
src = inspect.getsource(planet_visualization.create_planet_visualization)
assert 'create_jupiter_core_shell(center_position)' not in src, \
    'Old Jupiter dispatch still present'

print('Section 6 verification PASS')
print('Jupiter: 6 sphere + 4 custom shells in registries')
"
```

---

## 7. Verification Plan

### 7.1 Static checks

```bash
python3 -m py_compile shell_configs.py planet_visualization.py orrery_rendering.py \
    jupiter_visualization_shells.py saturn_visualization_shells.py \
    uranus_visualization_shells.py neptune_visualization_shells.py

# All touched files LF and ASCII
for f in shell_configs.py planet_visualization.py orrery_rendering.py \
         jupiter_visualization_shells.py saturn_visualization_shells.py \
         uranus_visualization_shells.py neptune_visualization_shells.py; do
    file "$f" | grep -q CRLF && echo "FAIL: $f CRLF" || echo "OK LF: $f"
done

python3 -c "
files = ['shell_configs.py', 'planet_visualization.py', 'orrery_rendering.py',
         'jupiter_visualization_shells.py', 'saturn_visualization_shells.py',
         'uranus_visualization_shells.py', 'neptune_visualization_shells.py']
for f in files:
    with open(f, 'rb') as fh:
        content = fh.read().decode('utf-8', errors='replace')
    issues = sum(1 for c in content if ord(c) > 127)
    print('%-45s %s' % (f, 'OK' if not issues else 'FAIL: %d non-ASCII' % issues))
"
```

### 7.2 Comprehensive import smoke test

```bash
python3 -c "
from orrery_rendering import (build_sphere_shell, create_info_marker,
                                rotate_to_sunward, create_ring_points)
from shell_configs import SHELL_CONFIGS, CUSTOM_SHELLS

expected_sphere = {'Mercury', 'Moon', 'Planet 9', 'Pluto', 'Eris', 'Venus', 'Mars',
                   'Earth', 'Jupiter'}
expected_custom = {'Mercury', 'Venus', 'Mars', 'Earth', 'Jupiter'}

assert set(SHELL_CONFIGS.keys()) == expected_sphere, \
    'SHELL_CONFIGS mismatch: %s' % sorted(SHELL_CONFIGS.keys())
assert set(CUSTOM_SHELLS.keys()) == expected_custom, \
    'CUSTOM_SHELLS mismatch: %s' % sorted(CUSTOM_SHELLS.keys())

assert len(SHELL_CONFIGS['Jupiter']) == 6
assert len(CUSTOM_SHELLS['Jupiter']) == 4

print('Phase C3 imports and counts PASS')
"
```

### 7.3 Sphere builder smoke test

```bash
python3 -c "
from orrery_rendering import build_sphere_shell
from shell_configs import SHELL_CONFIGS

for shell_name, cfg in SHELL_CONFIGS['Jupiter'].items():
    traces = build_sphere_shell(cfg, 'Jupiter', (0, 0, 0))
    assert len(traces) == 2, 'Jupiter/%s expected 2 traces, got %d' % (shell_name, len(traces))

print('Jupiter sphere builder smoke test PASS')
"
```

### 7.4 Custom geometry trace count

```bash
python3 -c "
import importlib
mod = importlib.import_module('jupiter_visualization_shells')

trace_counts = {
    'create_jupiter_magnetosphere': 2,           # 1 geom + 1 marker (no bow shock)
    'create_jupiter_io_plasma_torus': 2,         # 1 geom + 1 marker
    'create_jupiter_radiation_belts': 6,         # 3 belts * (1 geom + 1 marker)
    'create_jupiter_ring_system': 8,             # 4 rings * (1 geom + 1 marker)
}

for fname, expected in trace_counts.items():
    func = getattr(mod, fname)
    traces = func((0, 0, 0))
    actual = len(traces)
    assert actual == expected, '%s: expected %d traces, got %d' % (fname, expected, actual)

print('Custom geometry trace counts PASS')
for fname, expected in trace_counts.items():
    print('  %s: %d' % (fname, expected))
"
```

### 7.5 Rotation isolation correctness

This is the headline correctness test. Magnetosphere rotates; belts/torus/rings do not.

```bash
python3 -c "
import importlib
import numpy as np

mod = importlib.import_module('jupiter_visualization_shells')

# Magnetosphere at +X (default sunward = -X = actual sunward) -- no rotation
# Magnetosphere at -X -- 180-degree rotation
mag_origin = mod.create_jupiter_magnetosphere((0, 0, 0))
mag_off = mod.create_jupiter_magnetosphere((-1.0, 0.0, 0.0))

# First trace is magnetosphere geometry
origin_x = np.array(mag_origin[0].x)
off_x = np.array(mag_off[0].x) - (-1.0)  # Remove offset
assert np.allclose(off_x, -origin_x, atol=1e-9), 'Magnetosphere rotation failed'
print('Magnetosphere rotation: PASS (180 deg test)')

# Belts: should NOT rotate
belts_origin = mod.create_jupiter_radiation_belts((0, 0, 0))
belts_off = mod.create_jupiter_radiation_belts((-1.0, 0.0, 0.0))
b_origin_x = np.array(belts_origin[0].x)
b_off_x = np.array(belts_off[0].x) - (-1.0)
assert np.allclose(b_off_x, b_origin_x, atol=1e-9), 'Belts unexpectedly rotated'
print('Radiation belts: PASS (not rotated)')

# Io torus: should NOT rotate (random jitter may differ between calls; check x range)
torus_origin = mod.create_jupiter_io_plasma_torus((0, 0, 0))
torus_off = mod.create_jupiter_io_plasma_torus((-1.0, 0.0, 0.0))
t_origin_xrange = np.array(torus_origin[0].x).max() - np.array(torus_origin[0].x).min()
t_off_xrange = (np.array(torus_off[0].x) - (-1.0)).max() - \
               (np.array(torus_off[0].x) - (-1.0)).min()
assert abs(t_origin_xrange - t_off_xrange) < 0.001, 'Io torus unexpectedly rotated'
print('Io plasma torus: PASS (not rotated)')

# Rings: should NOT rotate (deterministic points)
rings_origin = mod.create_jupiter_ring_system((0, 0, 0))
rings_off = mod.create_jupiter_ring_system((-1.0, 0.0, 0.0))
r_origin_x = np.array(rings_origin[0].x)
r_off_x = np.array(rings_off[0].x) - (-1.0)
# Allow small tolerance for random thickness variations
assert abs(r_origin_x.max() - r_off_x.max()) < 1e-6, 'Rings unexpectedly rotated'
print('Ring system: PASS (not rotated)')

print()
print('Rotation isolation overall: PASS')
"
```

### 7.6 Ring helper promotion sanity check

```bash
python3 -c "
from orrery_rendering import create_ring_points

# Verify saturn/uranus/neptune still produce traces
import importlib
saturn = importlib.import_module('saturn_visualization_shells')
uranus = importlib.import_module('uranus_visualization_shells')
neptune = importlib.import_module('neptune_visualization_shells')

# Saturn no longer has create_ring_points_saturn defined
assert not hasattr(saturn, 'create_ring_points_saturn'), \
    'create_ring_points_saturn still defined in saturn module'

# Uranus and Neptune no longer import from saturn
import sys
mod_names = ['uranus_visualization_shells', 'neptune_visualization_shells']
for n in mod_names:
    src = open(sys.modules[n].__file__).read()
    assert 'create_ring_points_saturn' not in src, \
        '%s still references create_ring_points_saturn' % n

# Verify all three ring builders still work
for name, mod in [('Saturn', saturn), ('Uranus', uranus), ('Neptune', neptune)]:
    func_name = 'create_%s_ring_system' % name.lower()
    func = getattr(mod, func_name)
    traces = func((0, 0, 0))
    assert len(traces) > 0, '%s ring system returned no traces' % name
    print('%s ring system: %d traces' % (name, len(traces)))

print('Ring helper promotion PASS')
"
```

### 7.7 GUI tooltip regression check

Hover the GUI checkboxes for all 10 Jupiter shell controls. Tooltips should still display correctly, sourced from `jupiter_*_info` strings via the existing wiring path. The `*_info` strings remain in `jupiter_visualization_shells.py` (C3 doesn't remove them). Phase D switches this to read from configs.

### 7.8 Animation regression check

Per Phase C2 handoff item 11:
- **Heliocentric animated plot**: shells do NOT display.
- **Body-centered animated plot (Jupiter-centered)**: all shells render as static geometry at origin.

Verify both behaviors are unchanged after C3.

### 7.9 Mode 5 visual verification items for Tony

**Ring helper promotion (regression)**:

1. Saturn rings render unchanged (Cassini Division, A/B/C/D rings, etc.). Run pre-C3 vs post-C3 Saturn-centered renders; should be visually identical.
2. Uranus rings render unchanged.
3. Neptune rings render unchanged (including the Adams ring arcs).

**Jupiter sphere shells**:

4. All 6 sphere shells render at correct radius fractions: core (0.1), metallic hydrogen (0.8), molecular hydrogen (0.97), cloud layer (1.0 solid mesh3d), upper atmosphere (1.1), hill sphere (740 -- requires manual scale >= 0.5 AU).
5. Cloud layer (mesh3d) renders as solid surface, color rgb(255, 255, 235) (warm white).
6. Each shell has one cross info marker (new style: size=8, red outline). Hover shows full text.
7. Sphere shells with the new naming: Metallic Hydrogen Layer, Molecular Hydrogen Layer (with "Layer" suffix from source).

**Jupiter magnetosphere -- the rotation behavior fix**:

8. **Heliocentric view (default)**: Jupiter at ~5.2 AU on the X axis (or current orbital position). Sun direction from Jupiter = sunward. Rotation is near-identity. Magnetosphere should look visually identical to pre-C3: tail points anti-sunward.
9. **Jupiter-centered view (flyto)**: With Jupiter at origin in the body frame, the magnetosphere geometry rotates to orient toward the Sun (which is at offset in body-centered coordinates). Before C3 it pointed -X regardless; after C3 it points toward actual Sun.
10. Note: Jupiter has no bow shock (Tony Q5 decision). The "magnetosphere envelope" is just the magnetopause. If a bow shock visualization is added in a future editorial pass, this is where it would land.

**Jupiter Io plasma torus**:

11. Donut-shaped scatter at Io's orbital radius (~5.9 R_J).
12. Color rgb(255, 100, 100) (reddish).
13. NOT rotated -- stays in Jupiter's equatorial plane regardless of flyto angle.
14. Info marker (new style) at first point.

**Jupiter radiation belts**:

15. Three distinct belts visible when toggled on: Inner (yellow), Middle (green), Outer (light blue).
16. Located at 1.5, 3.0, 6.0 R_J respectively in the equatorial plane with z-modulation.
17. NOT rotated -- belts stay axis-aligned regardless of flyto.
18. Each belt has its own info marker (new style) and toggleable legend entry under one GUI control.

**Jupiter ring system**:

19. Four rings visible: Main, Halo, Amalthea Gossamer, Thebe Gossamer.
20. All in equatorial plane.
21. NOT rotated.
22. Each ring has its own info marker on the +X side at outer radius.
23. Visual depth: Main Ring brightest, Halo Ring inside Main and thicker, Gossamer rings extending outward and very faint.

**Regression**:

24. Mercury through Earth (8 bodies) all render unchanged (Phase A-C2 work).
25. Saturn, Uranus, Neptune still render via old dispatch path (C4 work).
26. Sun still renders via `create_sun_visualization()` (Phase D).

### 7.10 File size baseline (informational)

Save a Jupiter-centered static plot with all shells enabled. Compare to pre-C3 baseline. Expected: similar (the bulk of size optimization happened in Step 2; C3 makes architectural changes).

---

## 8. Decision Log and Open Items

### Decisions made by this manifest

1. **Promote `create_ring_points_saturn` to `orrery_rendering.create_ring_points()`** in C3 (Tony Q1). Saturn/Uranus/Neptune imports updated to use the promoted helper. Jupiter's local `create_ring_points_jupiter` kept (different algorithm).

2. **Jupiter magnetosphere: no bow shock added** (Tony Q5/(b)). Preserve source structure. Future editorial enhancement may add bow shock to all gas giants simultaneously.

3. **Radiation belt rotation: keep unrotated** (Tony Q2). Source generates belts in equatorial plane around rotational axis. Matches Earth Van Allen / Mars crustal fields precedent. Physical accuracy (~10 deg tilt for Jupiter) deferred to potential Phase C4 magnetic_tilt_deg wiring.

4. **Io plasma torus: keep unrotated** (Tony Q3). Equatorial structure (Io's orbital plane = Jupiter's equatorial plane). Same precedent.

5. **Ring system: keep unrotated** (Tony Q4). Equatorial structure by physical definition.

6. **Commented-out sun indicator at line 857: leave alone**. Tony decision: out of scope, mechanical purity.

7. **No n_points standardization needed for Jupiter**. Step 2 already set Jupiter Hill sphere to 20.

8. **Jupiter Hill sphere `marker_size=2.0`** preserved from source (other Hill spheres use 1.0). Don't standardize without Tony review.

9. **CUSTOM_SHELLS one entry per builder**. Jupiter's 4 entries each map to one builder. Builders are free to emit multiple trace groups (Mars/Earth precedent).

10. **Auto-generation script for sphere configs**: continued from C1/C2, validated for Jupiter's 6 shells.

### Open items for future phases

1. **Jupiter bow shock visualization** -- Editorial enhancement, post-C4. Add to all gas giants simultaneously for consistency with Mercury/Venus/Mars/Earth precedent.

2. **`magnetic_tilt_deg` plumbing for radiation belts** -- Phase C4 may apply this for Uranus (60 deg) and Neptune (47 deg). Jupiter's ~10 deg tilt is small enough that the current axis-aligned belts are visually reasonable; revisit if C4 establishes the pattern.

3. **Jupiter local ring helper consolidation** -- Phase D editorial: could converge `create_ring_points_jupiter` and `create_ring_points` (Saturn-style) if visual review accepts the algorithmic difference.

4. **Dead sphere shell functions in `jupiter_visualization_shells.py`** -- 6 sphere functions unreachable after C3. Custom geometry siblings (magnetosphere, io_plasma_torus, radiation_belts, ring_system) still live. Phase D decides per-function fate.

5. **Phase C4 preview**: Saturn, Uranus, Neptune. New patterns to plan for: tilted ring planes (Uranus 98 deg, Neptune 28 deg pole tilts), Adams ring arcs (Neptune), Enceladus plasma torus (Saturn), magnetic_tilt_deg wiring (Uranus 60 deg dipole-vs-spin, Neptune 47 deg).

### Risks and mitigations

| Risk | Mitigation |
|---|---|
| Ring helper promotion breaks Saturn/Uranus/Neptune | Section 3.6 smoke test verifies all three ring builders still produce traces. Section 7.6 confirms cross-module imports are gone. |
| Saturn/Uranus/Neptune visual regression | Section 7.9 items 1-3: explicit visual comparison checklist. |
| Jupiter magnetosphere rotation breaks heliocentric view | Section 5.6 rotation isolation test; Section 7.9 item 8 visual verification. |
| Belts/torus/rings accidentally rotated | Section 5.6 explicit "NOT rotated" tests for all three; Section 7.9 items 13, 17, 21 visual checks. |
| Indicator double-firing | Section 7.9 (informal, similar to C2 verification). |
| Jupiter dispatch leaks back through old path | Section 6.4 explicit assertion that old dispatch is gone. |

### Implementation discipline (per protocol)

- Python binary mode (`rb`/`wb`) for all file reads/writes
- Bottom-up editing within `jupiter_visualization_shells.py` (Section 6.3 ordering)
- Exact-string matching with `str_replace`, never regex
- One section at a time; run syntax check before proceeding
- Credit line update: `Module updated: May 2026 with Anthropic's Claude Opus 4.7` on every modified file
- ASCII only -- verify with `grep -P '[^\x00-\x7F]'`
- If any source value can't be confirmed from project files, STOP and ask Tony

---

## 9. Phase C3 Summary

| Component | Change |
|---|---|
| Sphere shells added to SHELL_CONFIGS | 6 (Jupiter) |
| Custom shells added to CUSTOM_SHELLS | 4 (Jupiter: magnetosphere, io_plasma_torus, radiation_belts, ring_system) |
| Bodies on unified dispatch (after) | 9 |
| New helper in `orrery_rendering.py` | `create_ring_points()` (promoted from saturn) |
| Cross-module imports eliminated | 2 (uranus and neptune no longer import from saturn) |
| Sun direction indicator calls removed | 4 (magnetosphere, io_torus, radiation_belts, ring_system) |
| Info markers updated to new style | 9 (1 mag + 1 io_torus + 3 belts + 4 rings) |
| Rotation calls added | 1 (magnetosphere only -- belts/torus/rings unrotated) |
| Files modified | 7 (shell_configs, planet_visualization, orrery_rendering, jupiter shells, saturn shells, uranus shells, neptune shells) |
| Files archivable in D | 0 (`jupiter_visualization_shells.py` retains 4 custom-geometry functions) |
| Behavioral change | Magnetosphere rotates to actual sunward direction (was unrotated; fix in flyto) |

After Phase C3:
- 9 bodies on unified dispatch (Mercury, Moon, Planet 9, Pluto, Eris, Venus, Mars, Earth, Jupiter)
- 4 bodies remaining on `create_planet_visualization` (Saturn, Uranus, Neptune; plus Sun via `create_sun_visualization`)
- 2 shell files fully dead from sphere-only bodies (Pluto, Eris) -- batch-archive in D
- 0 shell files fully dead from custom-geometry bodies (Venus, Mars, Earth, Jupiter) -- per-function archive in D
- 4 helpers in `orrery_rendering.py`: `build_sphere_shell`, `create_info_marker`, `rotate_to_sunward`, `create_ring_points`
- `magnetic_tilt_deg` still unused (Phase C4 Uranus/Neptune)
- `sun_position` still defaulted (Phase D)

---

## 10. Workflow Provenance

This manifest:
- Audited by Anthropic's Claude Opus 4.7
- Following Phase C2 handoff (May 16, 2026) by Opus 4.6
- From prompt v5 by Tony Quintanilla + Anthropic's Claude Opus 4.6
- Five decision points confirmed by Tony before drafting (promote in C3 / no bow shock / cosmetic alone / auto-gen yes / 5-section structure)
- Following protocol v3.22 (collegial Mode 7)

To be executed by: Anthropic's Claude Opus 4.6 + Tony, in a separate session.

The Phase A/B/C1/C2 manifests set the quality bar. C3 reuses that machinery on a more complex body with four custom geometry types instead of three. Particular care on:

1. **Section 3** (ring helper promotion) -- the cross-module change touches Saturn/Uranus/Neptune. Run the regression test in Section 3.6 BEFORE proceeding to Section 4.
2. **Section 5** (custom geometry refactor) -- four subsections, ten line-number-sensitive edits, two new rotation/non-rotation patterns to establish for C4 inheritance.
3. **Section 7.5** (rotation isolation test) -- the headline correctness check. If this fails, something fundamental is wrong with how rotation got applied.

Implementing Claude: if Section 5 (custom geometry) verifies cleanly but context starts pressuring before Section 6, stop and write a partial handoff. C3 can be split at the Section 5/6 boundary -- the codebase remains functional (Jupiter custom geometry refactored and working through old dispatch path) until the delegation is added in Section 6.

*Module updated: May 2026 with Anthropic's Claude Opus 4.7*
