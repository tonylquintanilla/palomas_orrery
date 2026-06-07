# MANIFEST: Shell Consolidation Step 3 — Phase C1 (Pluto + Eris + Venus + Mars)

**Project:** Paloma's Orrery | Plotting Consolidation Step 3
**Date:** May 14, 2026
**Source prompt:** `PROMPT_shell_consolidation_for_opus_v3.md`
**Phase B handoff:** `HANDOFF_shell_consolidation_phase_b.md` (May 14, 2026)
**Manifest by:** Anthropic's Claude Opus 4.7 (audit)
**For execution by:** Anthropic's Claude Opus 4.6 (implementation) + Tony (integrator)

---

## 1. Phase C1 Scope and Execution Model

### What Phase C1 delivers

C1 migrates four bodies and introduces the first non-Mercury CUSTOM_SHELLS entries. Progressive complexity within the phase: start with Pluto/Eris (Phase-B-equivalent: sphere-only, files archivable), then Venus/Mars (introduce magnetosphere CUSTOM_SHELLS, force the `rotate_to_sunward()` promotion).

After Phase C1:

- **Pluto** renders via `SHELL_CONFIGS['Pluto']` (6 sphere shells, including mesh3d crust). No custom geometry.
- **Eris** renders via `SHELL_CONFIGS['Eris']` (5 sphere shells, including mesh3d crust). No custom geometry.
- **Venus** renders via `SHELL_CONFIGS['Venus']` (6 sphere shells, including mesh3d crust) + `CUSTOM_SHELLS['Venus']` (1 entry: magnetosphere — emits both magnetosphere and bow shock).
- **Mars** renders via `SHELL_CONFIGS['Mars']` (7 sphere shells, including mesh3d crust) + `CUSTOM_SHELLS['Mars']` (1 entry: magnetosphere — emits magnetosphere, bow shock, and crustal fields).
- `rotate_to_sunward()` promoted from `mercury_visualization_shells.py` to `orrery_rendering.py` with new parameters: `magnetic_tilt_deg=0` (default) and `sun_position=(0, 0, 0)` (default). Mercury's local copy deleted; Venus/Mars magnetosphere builders import the promoted version.
- `pluto_visualization_shells.py` and `eris_visualization_shells.py` become fully dead code paths. Not modified — batch-archived in Phase D.
- `venus_visualization_shells.py` and `mars_visualization_shells.py` retain only their custom geometry builders (`create_venus_magnetosphere_shell`, `create_mars_magnetosphere_shell`). Their sphere shell functions become unreachable. Per Phase B policy: leave the dead sphere functions in place; Phase D's batch cleanup decides per-file fate.
- ASCII cleanup applied to 3 files (one-character fixes).

After Phase C1, seven bodies route through the unified dispatch (Mercury, Moon, Planet 9, Pluto, Eris, Venus, Mars). Six bodies still use `create_planet_visualization()` (Earth, Jupiter, Saturn, Uranus, Neptune; plus Sun via separate `create_sun_visualization`).

### What Phase C1 explicitly does NOT do

- Does NOT modify `pluto_visualization_shells.py`, `eris_visualization_shells.py`. Files become entirely dead — batch-archive in Phase D.
- Does NOT touch the Mars magnetosphere "missing info marker" pre-existing bug (lines 645-658 in source). Mars magnetosphere builder emits the magnetosphere trace with `hoverinfo='skip'` but no separate info marker carrying its hover text. This is a Phase B / Step 2 omission, preserved as-is in Phase C1 because fixing it requires editorial decision on where to place the marker. Flagged for separate fix; not in C1 scope.
- Does NOT update the `_info` import chain. The `pluto_*_info`, `eris_*_info`, `venus_*_info`, `mars_*_info` strings continue to live in their source files and continue to be looked up via `globals()` in `build_shell_checkboxes`. Phase D handles all `_info` cleanup as one batch operation.
- Does NOT retire `create_planet_visualization()`. Six bodies still use it (Earth, Jupiter, Saturn, Uranus, Neptune, Sun). Phase D retires it.
- Does NOT touch `celestial_objects.py` or GUI tooltip wiring.
- Does NOT thread `sun_position` from the ephemeris pipeline yet. The `rotate_to_sunward()` promotion accepts `sun_position` as a parameter, but Phase C1 callers continue to default it to `(0, 0, 0)` (Sun-at-origin assumption). Wiring `sun_position` from the actual ephemeris is a Phase D change (item 6 from Phase B handoff). C1 sets up the parameter; Phase D plumbs it through.
- Does NOT add the Mars magnetosphere info marker (pre-existing omission).

### Execution order (canonical)

C1 has six top-level sections, executed in this order. Each section is atomic. Run the syntax check at the end of each section before starting the next. The body migrations within Section 4 should be done one at a time with visual verification between, but if context pressure builds, implementing Claude can stop after any body.

1. **Pre-flight verification** (Section 2)
2. **ASCII cleanup** (Section 3)
3. **Pluto + Eris configs + delegation** (Section 4) — purely mechanical, identical pattern to Phase B
4. **`rotate_to_sunward()` promotion** (Section 5) — new helper signature in `orrery_rendering.py`, Mercury updated to use the promoted version
5. **Venus + Mars: configs + custom geometry refactor + delegation** (Section 6)
6. **Verification plan** (Section 7)

If any step fails its syntax check, STOP and resolve before proceeding.

### Why this order matters

Sections 4 and 5 are independent and either could go first. Doing Pluto+Eris first (Section 4) lands the easy wins, confirms the Phase B pattern still works at scale, and produces visual artifacts Tony can verify before the more complex Section 6 work begins. Section 5 (the `rotate_to_sunward()` promotion) must complete before Section 6 because Venus/Mars magnetosphere builders need to import the promoted helper.

Section 3 (ASCII cleanup) goes early because it's trivial and removes a class of merge-conflict noise. It also gives implementing Claude a "warm-up" task to verify their bash/Python tooling is set up before touching the larger files.

---

## 2. Pre-flight Verification

### 2.1 Confirm Phase A+B are in place

```bash
python3 -c "
from orrery_rendering import build_sphere_shell, create_info_marker
from shell_configs import SHELL_CONFIGS, CUSTOM_SHELLS

# Phase A+B baseline
for body in ['Mercury', 'Moon', 'Planet 9']:
    assert body in SHELL_CONFIGS, 'Phase A/B body %s missing' % body
assert 'Mercury' in CUSTOM_SHELLS, 'Phase A CUSTOM_SHELLS Mercury missing'
assert len(SHELL_CONFIGS['Mercury']) == 6
assert len(SHELL_CONFIGS['Moon']) == 6
assert len(SHELL_CONFIGS['Planet 9']) == 2
assert len(CUSTOM_SHELLS['Mercury']) == 2

print('Phase A+B baseline OK')
"
```

If anything fails, STOP — Phase C1 assumes Phase A+B are complete and consistent.

### 2.2 Confirm source files are post-Step-2

```bash
for f in pluto_visualization_shells.py eris_visualization_shells.py \
         venus_visualization_shells.py mars_visualization_shells.py; do
    echo "=== $f ==="
    grep "Module updated" $f | head -1
    grep -c "hoverinfo='skip'" $f
done
```

Expected: all four files contain "May 2026 with Anthropic's Claude Opus 4.7" credit line and 5+ `hoverinfo='skip'` markers each (one per sphere shell after Step 2 refactor).

If any file lacks the May 2026 credit or `hoverinfo='skip'` markers, STOP — the file is not the post-Step-2 baseline.

### 2.3 Confirm CENTER_BODY_RADII entries exist

```bash
python3 -c "
from constants_new import CENTER_BODY_RADII, KM_PER_AU
for body in ['Pluto', 'Eris', 'Venus', 'Mars']:
    km = CENTER_BODY_RADII[body]
    au = km / KM_PER_AU
    print('%-10s %8.2f km = %.4e AU' % (body, km, au))
"
```

Expected:
```
Pluto       1188.30 km = 7.9433e-06 AU
Eris        1163.00 km = 7.7741e-06 AU
Venus       6051.80 km = 4.0454e-05 AU
Mars        3396.20 km = 2.2702e-05 AU
```

All four must be present and finite.

### 2.4 Confirm post-Phase-B dispatch state

```bash
grep -c "create_celestial_body_visualization" planet_visualization.py
# Expected: at least 7 (function def + 3 delegations from A/B + docstring mentions)

grep -n "if planet_name == '" planet_visualization.py | head -15
# Expected: Mercury, Venus, Earth, Moon, Mars, Jupiter, Saturn, Uranus, Neptune,
#           Pluto, Eris, Planet 9 -- with Mercury/Moon/Planet 9 already delegating
```

Mercury, Moon, Planet 9 should already be one-line delegations (post-Phase-B).

### 2.5 Backup files Phase C1 will touch

Before any edits:

```
shell_configs.py                    -> shell_configs.py.phaseC1_backup
planet_visualization.py             -> planet_visualization.py.phaseC1_backup
orrery_rendering.py                 -> orrery_rendering.py.phaseC1_backup
mercury_visualization_shells.py     -> mercury_visualization_shells.py.phaseC1_backup
venus_visualization_shells.py       -> venus_visualization_shells.py.phaseC1_backup
mars_visualization_shells.py        -> mars_visualization_shells.py.phaseC1_backup
palomas_orrery.py                   -> palomas_orrery.py.phaseC1_backup (for ASCII fix)
```

Six files. Pluto and Eris shell files NOT touched (per pre-decided policy).

### 2.6 Line ending inventory

| File | Expected | Action if different |
|------|----------|--------------------|
| `shell_configs.py` | LF | Stop, investigate |
| `planet_visualization.py` | LF | Stop, investigate (Phase A converted) |
| `orrery_rendering.py` | LF | Stop, investigate (Phase A created) |
| `mercury_visualization_shells.py` | LF | Stop, investigate |
| `venus_visualization_shells.py` | LF | Stop, investigate |
| `mars_visualization_shells.py` | LF | Stop, investigate |
| `palomas_orrery.py` | LF | Stop, investigate |

Verify all with `file <path>`. None should report "CRLF line terminators". (`palomas_orrery_helpers.py` is CRLF but not touched in C1 — that's Phase D.)

---

## 3. ASCII Cleanup

Three files contain non-ASCII characters from Phase A/B comment text. The protocol requires ASCII only in Python files. Six total character fixes.

### 3.1 The seven characters

```bash
python3 << 'EOF'
import re
files = [
    'orrery_rendering.py',
    'planet_visualization.py',
    'palomas_orrery.py',
]
for f in files:
    print(f"\n=== {f} ===")
    with open(f, 'rb') as fh:
        content = fh.read()
    text = content.decode('utf-8', errors='replace')
    for i, c in enumerate(text):
        if ord(c) > 127:
            line = text[:i].count('\n') + 1
            print(f"  Line {line}: U+{ord(c):04X} ({c!r})")
EOF
```

Expected output:

```
=== orrery_rendering.py ===
  Line 105: U+2014 ('—')

=== planet_visualization.py ===
  Line 633: U+2014 ('—')

=== palomas_orrery.py ===
  Line 42: U+2192 ('→')
  Line 295: U+00B0 ('°')
  Line 1628: U+2014 ('—')
  Line 1974: U+2192 ('→')
  Line 1974: U+2192 ('→')
```

(`palomas_orrery.py` line 1974 has two `→` characters; the regex prints each occurrence.)

### 3.2 Substitutions

| Character | Unicode | Replace with |
|-----------|---------|--------------|
| `—` (em-dash) | U+2014 | `--` (two ASCII hyphens) |
| `→` (right arrow) | U+2192 | `->` |
| `°` (degree sign) | U+00B0 | ` deg` (space + word) |

### 3.3 Mechanical method (Python binary mode)

```python
# Run this once for each file:
import os
for filename in ['orrery_rendering.py', 'planet_visualization.py', 'palomas_orrery.py']:
    with open(filename, 'rb') as f:
        content = f.read()
    original_len = len(content)
    content = content.replace(b'\xe2\x80\x94', b'--')      # em-dash
    content = content.replace(b'\xe2\x86\x92', b'->')      # right arrow
    content = content.replace(b'\xc2\xb0', b' deg')        # degree sign
    if len(content) != original_len:
        with open(filename, 'wb') as f:
            f.write(content)
        print(f'{filename}: cleaned ({original_len} -> {len(content)} bytes)')
    else:
        print(f'{filename}: already clean')
```

The byte sequences are the UTF-8 encodings of those code points. Python binary mode is mandatory (per protocol) to avoid breaking other multi-byte characters or line endings.

### 3.4 Verification

```bash
python3 -c "
import re
for f in ['orrery_rendering.py', 'planet_visualization.py', 'palomas_orrery.py']:
    with open(f, 'rb') as fh:
        content = fh.read().decode('utf-8', errors='replace')
    issues = [(i, c) for i, c in enumerate(content) if ord(c) > 127]
    print('%-40s %s' % (f, 'OK' if not issues else 'FAIL: %d non-ASCII' % len(issues)))
"
```

All three files should now report OK. After the cleanup, also confirm syntax:

```bash
python3 -m py_compile orrery_rendering.py planet_visualization.py palomas_orrery.py
```

No output = success.

---

## 4. Pluto + Eris: Configs + Delegation

This section is mechanically identical to Phase B's Moon and Planet 9 migrations. Two bodies, sphere-only, no custom geometry. Just data extraction and delegation.

### 4.1 Strategy

For each body:
1. Extract sphere shell config values from the source file's `layer_info` dict.
2. Insert config block in `shell_configs.py` after the Phase B blocks.
3. Replace the body's if-block in `planet_visualization.py` with a one-line delegation.
4. Run syntax check; visual verification after both bodies are done.

### 4.2 Auto-generation script (recommended approach)

Given the volume of hover text (Pluto descriptions average 2,000+ chars each), manually transcribing config blocks is error-prone. Instead, run this extraction script ONCE to generate the config blocks, then verify the output before inserting:

```python
# generate_phase_c1_pluto_eris_configs.py
# Run this and review output before inserting into shell_configs.py
import re

# Edits to apply during transcription
N_POINTS_HILL_SPHERE = 20  # Standard from Phase B; source uses 20 for Pluto/Eris already
GEOMETRY_TYPE_CRUST = 'mesh3d'
MESH_RESOLUTION = 24

BODIES = {
    'Pluto': {
        'path': 'pluto_visualization_shells.py',
        'shells': [
            ('core',         'create_pluto_core_shell',         'pluto_core_info'),
            ('mantle',       'create_pluto_mantle_shell',       'pluto_mantle_info'),
            ('crust',        'create_pluto_crust_shell',        'pluto_crust_info'),
            ('haze_layer',   'create_pluto_haze_layer_shell',   'pluto_haze_layer_info'),
            ('atmosphere',   'create_pluto_atmosphere_shell',   'pluto_atmosphere_info'),
            ('hill_sphere',  'create_pluto_hill_sphere_shell',  'pluto_hill_sphere_info'),
        ],
    },
    'Eris': {
        'path': 'eris_visualization_shells.py',
        'shells': [
            ('core',         'create_eris_core_shell',         'eris_core_info'),
            ('mantle',       'create_eris_mantle_shell',       'eris_mantle_info'),
            ('crust',        'create_eris_crust_shell',        'eris_crust_info'),
            ('atmosphere',   'create_eris_atmosphere_shell',   'eris_atmosphere_info'),
            ('hill_sphere',  'create_eris_hill_sphere_shell',  'eris_hill_sphere_info'),
        ],
    },
}


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
    pat = re.compile(rf'^{var_name}\s*=\s*\(\s*\n(.*?)\n\)\s*$', re.DOTALL | re.MULTILINE)
    m = pat.search(full_src)
    return m.group(1) if m else None


def extract_hover_text_var(body_src):
    """For Hill spheres which use a local hover_text variable instead of description."""
    m = re.search(r'hover_text\s*=\s*\(\s*\n(.*?)\n\s*\)\s*$', body_src, re.DOTALL | re.MULTILINE)
    return m.group(1) if m else None


def extract_local_radius_fraction(body_src):
    """Hill spheres set radius_fraction as local variable."""
    m = re.search(r'^\s*radius_fraction\s*=\s*([\d.eE+-]+)', body_src, re.MULTILINE)
    return m.group(1) if m else None


def build_config_block(body_name, shells_spec):
    out = ["    '%s': {\n" % body_name]
    with open(BODIES[body_name]['path']) as f:
        full_src = f.read()
        all_lines = full_src.splitlines(keepends=True)

    for shell_name, fn_name, info_var in shells_spec:
        body_src = get_func_body(all_lines, fn_name)

        rf = extract_scalar(body_src, 'radius_fraction')
        op = extract_scalar(body_src, 'opacity')
        color = extract_scalar(body_src, 'color')
        name = extract_scalar(body_src, 'name')
        description = extract_multiline(body_src, 'description')

        np_call = re.search(r"create_sphere_points\([^,]+,\s*n_points\s*=\s*(\d+)", body_src)
        np_val = int(np_call.group(1)) if np_call else None

        ms_inline = re.search(r"marker=dict\(\s*\n?\s*size\s*=\s*([\d.]+)", body_src)
        ms_val = ms_inline.group(1) if ms_inline else None

        is_mesh3d = 'go.Mesh3d' in body_src
        is_hill_sphere = (shell_name == 'hill_sphere')

        # Hill sphere uses local-variable pattern (no layer_info dict)
        if rf is None and is_hill_sphere:
            rf = extract_local_radius_fraction(body_src)
            op = '0.25'  # Source values
            # Hill sphere color, name fixed by convention
            name = 'Hill Sphere'
            description = extract_hover_text_var(body_src)
            # marker_size from the geometry trace (size=2.0 in source for Pluto/Eris)
            ms_val = ms_val or '2.0'

        # Normalize lowercase 'mantle' (Pluto source has lowercase) to 'Mantle'
        if name == 'mantle':
            name = 'Mantle'

        tooltip = extract_info_string(full_src, info_var)

        # Format block
        out.append(f"\n        '{shell_name}': {{\n")
        out.append(f"            'name': '{name}',\n")
        out.append(f"            'radius_fraction': {rf},\n")
        out.append(f"            'color': '{color}',\n")
        out.append(f"            'opacity': {op},\n")

        if is_mesh3d:
            out.append(f"            'geometry_type': 'mesh3d',\n")
            out.append(f"            'mesh_resolution': {MESH_RESOLUTION},\n")
        else:
            # Apply n_points standardization for Hill sphere
            effective_np = N_POINTS_HILL_SPHERE if is_hill_sphere else np_val
            out.append(f"            'n_points': {effective_np},\n")
            out.append(f"            'marker_size': {ms_val},\n")

        # hover_text
        out.append(f"            'hover_text': (\n")
        # Description is already a concatenation of "..." strings with leading whitespace.
        # Reduce leading whitespace to 16 spaces.
        for line in description.split('\n'):
            stripped = line.lstrip()
            if stripped:
                out.append(f"                {stripped}\n")
        out.append(f"            ),\n")

        # tooltip
        out.append(f"            'tooltip': (\n")
        for line in tooltip.split('\n'):
            stripped = line.lstrip()
            if stripped:
                out.append(f"                {stripped}\n")
        out.append(f"            ),\n")

        out.append(f"        }},\n")

    out.append("    },\n")
    return ''.join(out)


print('# Generated by generate_phase_c1_pluto_eris_configs.py')
print('# Review carefully before inserting into shell_configs.py')
print()
for body_name in ['Pluto', 'Eris']:
    print(f"\n    # ============================================================")
    print(f"    # {body_name}")
    print(f"    # ============================================================")
    print(build_config_block(body_name, BODIES[body_name]['shells']))
```

Save as `generate_phase_c1_pluto_eris_configs.py` and run from the project directory:

```bash
python3 generate_phase_c1_pluto_eris_configs.py > phase_c1_pluto_eris_configs.txt
```

Review the output. Each config block follows the Phase B template (name / radius_fraction / color / opacity / [geometry_type+mesh_resolution OR n_points+marker_size] / hover_text / tooltip).

### 4.3 Manual review checklist before inserting

Per-block, verify:

- `radius_fraction` is a float (or large int for Hill spheres). Pluto: 0.70, 0.99, 1.0, 1.17, 1.43, 4685. Eris: 0.60, 0.66, 1.0, 1.005, 6965.
- `color` is in `'rgb(R, G, B)'` format with quoted string.
- `opacity` is a float between 0 and 1.
- Crust entries have `geometry_type='mesh3d'` and `mesh_resolution=24` (NO `n_points`, NO `marker_size`).
- All other entries have `n_points` (25 for interior, 20 for boundary/atmosphere/Hill sphere) and `marker_size`.
- Hover text contains `<br>` line breaks (HTML). Tooltip contains `\n` line breaks (Tkinter).
- All apostrophes inside strings are straight ASCII (`'`), not curly Unicode.
- The Pluto mantle's `'name'` field reads `'Mantle'` (capitalized) — the source has lowercase `'mantle'`, normalized in the script. This is a cosmetic fix.

If any block looks wrong, STOP and resolve with Tony before inserting.

### 4.4 Insert configs into shell_configs.py

Locate the closing of the Phase B Planet 9 block in `shell_configs.py`. The structure is:

```python
    'Planet 9': {
        # ... shells ...
    },

    # Other bodies added in Phases B, C, D
}
```

Insert the Pluto and Eris config blocks BEFORE the `# Other bodies added in Phases B, C, D` comment. Match indentation exactly (4 spaces for top-level body keys, 8 for shell keys). Update the comment to read `# Other bodies added in Phases C, D` after insertion.

After insertion, verify:

```bash
python3 -c "
from shell_configs import SHELL_CONFIGS
for body in ['Mercury', 'Moon', 'Planet 9', 'Pluto', 'Eris']:
    assert body in SHELL_CONFIGS, '%s missing' % body
print('Pluto shells:', sorted(SHELL_CONFIGS['Pluto'].keys()))
print('Eris shells:', sorted(SHELL_CONFIGS['Eris'].keys()))
print('Pluto shell count:', len(SHELL_CONFIGS['Pluto']))  # 6
print('Eris shell count:', len(SHELL_CONFIGS['Eris']))    # 5
# Spot-check values
assert SHELL_CONFIGS['Pluto']['core']['radius_fraction'] == 0.70
assert SHELL_CONFIGS['Pluto']['hill_sphere']['radius_fraction'] == 4685
assert SHELL_CONFIGS['Pluto']['crust']['geometry_type'] == 'mesh3d'
assert SHELL_CONFIGS['Eris']['atmosphere']['radius_fraction'] == 1.005
assert SHELL_CONFIGS['Eris']['hill_sphere']['radius_fraction'] == 6965
print('All Pluto/Eris configs verified')
"
```

### 4.5 Delegation edits in planet_visualization.py

Find the Pluto if-block in `create_planet_visualization()`. Current source:

```python
    if planet_name == 'Pluto':
        if shell_vars['pluto_core'].get() == 1:
            traces.extend(create_pluto_core_shell(center_position))
        if shell_vars['pluto_mantle'].get() == 1:
            traces.extend(create_pluto_mantle_shell(center_position))
        if shell_vars['pluto_crust'].get() == 1:
            traces.extend(create_pluto_crust_shell(center_position))
        if shell_vars['pluto_haze_layer'].get() == 1:
            traces.extend(create_pluto_haze_layer_shell(center_position))
        if shell_vars['pluto_atmosphere'].get() == 1:
            traces.extend(create_pluto_atmosphere_shell(center_position))
        if shell_vars['pluto_hill_sphere'].get() == 1:
            traces.extend(create_pluto_hill_sphere_shell(center_position))
```

Replace with:

```python
    if planet_name == 'Pluto':
        # Step 3 Phase C1: delegate to unified config-driven dispatch.
        # Same pattern as Mercury (Phase A), Moon/Planet 9 (Phase B).
        return create_celestial_body_visualization(
            fig, planet_name, shell_vars,
            animate=animate, frames=frames,
            center_position=center_position,
            object_type='Pluto',
            center_object='Pluto',
        )
```

Find the Eris if-block. Current source:

```python
    if planet_name == 'Eris':
        if shell_vars['eris_core'].get() == 1:
            traces.extend(create_eris_core_shell(center_position))
        if shell_vars['eris_mantle'].get() == 1:
            traces.extend(create_eris_mantle_shell(center_position))
        if shell_vars['eris_crust'].get() == 1:
            traces.extend(create_eris_crust_shell(center_position))
        if shell_vars['eris_atmosphere'].get() == 1:
            traces.extend(create_eris_atmosphere_shell(center_position))
        if shell_vars['eris_hill_sphere'].get() == 1:
            traces.extend(create_eris_hill_sphere_shell(center_position))
```

Replace with:

```python
    if planet_name == 'Eris':
        # Step 3 Phase C1: delegate to unified config-driven dispatch.
        # Same pattern as Mercury (Phase A), Moon/Planet 9 (Phase B).
        return create_celestial_body_visualization(
            fig, planet_name, shell_vars,
            animate=animate, frames=frames,
            center_position=center_position,
            object_type='Eris',
            center_object='Eris',
        )
```

### 4.6 Bottom-up edit order

If applying both edits in one pass: do Eris first (higher line number in the file, currently ~847), then Pluto (currently ~833). Both edits use exact-string `str_replace`, so line numbers don't drift — bottom-up is a discipline matter, not a correctness one. The order is convention.

### 4.7 Syntax check after Section 4

```bash
python3 -m py_compile shell_configs.py planet_visualization.py
# No output = success
```

### 4.8 Mode 5 visual verification for Pluto + Eris

Stop here and run the orrery before proceeding to Section 5. Verify:

| Check | Pass criterion |
|-------|----------------|
| Pluto center, all 6 shells | All render via unified dispatch; legend shows Pluto: Core/Mantle/Crust/Haze Layer/Atmosphere/Hill Sphere |
| Pluto crust mesh3d | Brownish solid surface (color rgb(83, 68, 55)) |
| Pluto mantle now labeled 'Mantle' | Capitalized (cosmetic fix from source lowercase) |
| Eris center, all 5 shells | All render via unified dispatch |
| Eris crust mesh3d | Off-white solid surface |
| Info markers | One cross per shell at north pole, new style (size=8, red outline) |
| Sun direction indicator | Appears ONCE per body |
| Mercury/Moon/Planet 9 regression | All still render correctly |

If any check fails, STOP and debug before proceeding to Section 5.

---

## 5. Promote `rotate_to_sunward()` to `orrery_rendering.py`

This section promotes the helper from Mercury-local to a shared utility in `orrery_rendering.py`, with two new parameters that resolve Phase B's deferred item 6 (`sun_position` threading) and prepare for Phase C4's tilted magnetospheres (Uranus 60 deg).

### 5.1 Why promote now

Phase B's `rotate_to_sunward()` lives as a nested function inside Mercury's magnetosphere builder. Venus and Mars magnetosphere migrations (Section 6) will use the same logic — copying the nested function three times invites drift. Promote once, import everywhere.

Two new parameters:

- `sun_position=(0, 0, 0)`: where the Sun actually is in plot coordinates. Current Phase A/B code assumes Sun at origin (heliocentric view). In a body-centered view (e.g. Mars-centered with the Sun offset), the magnetosphere should still rotate to face the actual Sun, not the origin. Defaulting to `(0, 0, 0)` preserves Phase A behavior; Phase D will wire actual Sun position from the ephemeris.
- `magnetic_tilt_deg=0`: angular offset between rotation axis and magnetic axis. Mercury, Venus, Mars have approximately aligned dipoles (small tilt). Earth has ~11 deg, Saturn ~0, Jupiter ~10, Uranus ~60, Neptune ~47. Phase C1 only needs tilt=0 (Venus, Mars), but adding the parameter from the start avoids a second refactor.

### 5.2 Promoted function specification

Add to `orrery_rendering.py` (immediately after `build_sphere_shell()` definition):

```python
def rotate_to_sunward(px, py, pz, center_position=(0, 0, 0),
                     sun_position=(0, 0, 0), magnetic_tilt_deg=0):
    """Rotate points from default -X sunward to actual sunward direction.

    Default geometry generation convention: magnetosphere structures (bow
    shock, magnetotail, etc.) are generated with -X as the sunward direction.
    For off-center views (body offset from origin) or body-centered views
    where the Sun is offset, this function rotates the geometry to point
    toward the actual sunward direction.

    Parameters:
        px, py, pz (np.ndarray): Point coordinates in default frame
        center_position (tuple): (x, y, z) AU position of the body's center
        sun_position (tuple): (x, y, z) AU position of the Sun.
                              Default (0, 0, 0) = Sun at origin (heliocentric).
                              Phase D wires actual Sun position from ephemeris.
        magnetic_tilt_deg (float): Angular offset between rotation axis and
                                    magnetic dipole axis (degrees).
                                    Default 0 = aligned dipoles (Mercury, Venus,
                                    Mars). Earth ~11, Saturn ~0, Jupiter ~10,
                                    Uranus ~60, Neptune ~47.
                                    Currently a placeholder for Phase C4
                                    (Uranus, Neptune); not applied in Phase C1.

    Returns:
        (rx, ry, rz): rotated point arrays
    """
    import math
    import numpy as np

    center_x, center_y, center_z = center_position
    sun_x, sun_y, sun_z = sun_position

    # Vector from body center toward Sun
    dx, dy, dz = sun_x - center_x, sun_y - center_y, sun_z - center_z
    dist = math.sqrt(dx**2 + dy**2 + dz**2)

    if dist < 1e-12:
        # Body and Sun coincident (or both at origin): default -X convention
        return px, py, pz

    # Actual sunward unit vector
    sx, sy, sz = dx / dist, dy / dist, dz / dist

    # Default sunward direction (geometry convention: -X)
    fx, fy, fz = -1.0, 0.0, 0.0

    # Dot product (cosine of angle between default and actual sunward)
    dot = fx * sx + fy * sy + fz * sz

    if dot > 0.9999:
        # Already aligned
        return px, py, pz

    if dot < -0.9999:
        # Anti-parallel: 180 deg rotation around Z axis
        return -px, -py, pz

    # Cross product gives rotation axis
    ax = fy * sz - fz * sy
    ay = fz * sx - fx * sz
    az = fx * sy - fy * sx
    alen = math.sqrt(ax**2 + ay**2 + az**2)
    ax, ay, az = ax / alen, ay / alen, az / alen

    # Rodrigues' rotation formula
    angle = math.acos(max(-1.0, min(1.0, dot)))
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)

    rx = np.empty_like(px, dtype=float)
    ry = np.empty_like(py, dtype=float)
    rz = np.empty_like(pz, dtype=float)

    for i in range(len(px)):
        p = (float(px[i]), float(py[i]), float(pz[i]))
        # v*cos(a) + (k x v)*sin(a) + k*(k.v)*(1-cos(a))
        kdotv = ax * p[0] + ay * p[1] + az * p[2]
        rx[i] = p[0] * cos_a + (ay * p[2] - az * p[1]) * sin_a + ax * kdotv * (1 - cos_a)
        ry[i] = p[1] * cos_a + (az * p[0] - ax * p[2]) * sin_a + ay * kdotv * (1 - cos_a)
        rz[i] = p[2] * cos_a + (ax * p[1] - ay * p[0]) * sin_a + az * kdotv * (1 - cos_a)

    # NOTE: magnetic_tilt_deg parameter reserved for Phase C4 (Uranus, Neptune).
    # Not applied in C1 (Mercury/Venus/Mars all have ~0 tilt). Phase C4 will
    # add a second rotation about the planet's rotation axis by this angle
    # to model the dipole offset.

    return rx, ry, rz
```

Notes on the design:

- Parameters added as kwargs with safe defaults: existing Mercury call site (no kwargs passed) gets identical behavior.
- `magnetic_tilt_deg` accepted but not yet applied — documented as Phase C4 placeholder. Adding it now means Venus/Mars callers in C1 can pass `magnetic_tilt_deg=0` explicitly if desired, and the API doesn't need expansion later.
- Imports (`math`, `numpy as np`) moved inside the function for clean module-level dependencies. The module already imports both at the top, so this is just a robustness measure for callers that import `rotate_to_sunward` independently.

### 5.3 Update Mercury to use the promoted helper

In `mercury_visualization_shells.py`, find the local `rotate_to_sunward` function definition (currently around line 230, nested inside `create_mercury_magnetosphere_shell`). Two changes:

**Change 1**: At the top of the file (after `from planet_visualization_utilities import ...`), add:

```python
from orrery_rendering import rotate_to_sunward
```

**Change 2**: Delete the entire nested function definition (lines 224-279 in current source — verify by grep first). The block to delete starts:

```python
    # Compute sunward rotation
    # The geometry is generated with -X as sunward. If Mercury is off-center,
    # rotate to point the bow shock toward the Sun at origin.
    center_x, center_y, center_z = center_position
    dist = math.sqrt(center_x**2 + center_y**2 + center_z**2)
    
    def rotate_to_sunward(px, py, pz):
        """Rotate points from default -X sunward to actual sunward direction."""
        if dist < 1e-12:
            # At origin - no rotation needed, -X is the convention
            return px, py, pz
        # ... (entire nested function body) ...
        return rx, ry, rz
```

And ends with the closing `return rx, ry, rz` of the nested function. Delete the whole block including the `center_x, center_y, center_z = center_position` and `dist = math.sqrt(...)` lines, since those are now computed inside the promoted function.

**Change 3**: Update the call sites. The local function was called with three args:

```python
x, y, z = rotate_to_sunward(x, y, z)
```

and

```python
bow_shock_x, bow_shock_y, bow_shock_z = rotate_to_sunward(
    bow_shock_x, bow_shock_y, bow_shock_z
)
```

Update both to pass `center_position`:

```python
x, y, z = rotate_to_sunward(x, y, z, center_position=center_position)
```

```python
bow_shock_x, bow_shock_y, bow_shock_z = rotate_to_sunward(
    bow_shock_x, bow_shock_y, bow_shock_z, center_position=center_position
)
```

Note: Mercury still doesn't pass `sun_position` — the default `(0, 0, 0)` preserves Phase A behavior (Sun-at-origin assumption). Phase D will wire actual Sun position.

**Change 4**: Mercury also has unpacking for `center_x, center_y, center_z = center_position` later in the function (around line 311) for offset application. Verify this remains after the nested-function deletion — it's needed to offset the rotated coordinates to the body center:

```python
x = x + center_x
y = y + center_y
z = z + center_z
```

If the deletion accidentally removed those lines, restore them. The pattern is:
1. Generate geometry in default frame
2. Rotate to sunward
3. Offset by center position

### 5.4 Verification after promotion

```bash
python3 -m py_compile orrery_rendering.py mercury_visualization_shells.py

python3 -c "
from orrery_rendering import rotate_to_sunward
import numpy as np
# Identity case (sun at origin, body at origin): no rotation
x = np.array([1.0, 0.0, -1.0])
y = np.array([0.0, 1.0, 0.0])
z = np.array([0.0, 0.0, 0.0])
rx, ry, rz = rotate_to_sunward(x, y, z)
assert np.allclose(rx, x) and np.allclose(ry, y) and np.allclose(rz, z)
print('Identity case: PASS')

# Anti-parallel case (body in +X, sun at origin): 180 deg rotation
rx, ry, rz = rotate_to_sunward(x, y, z, center_position=(1.0, 0.0, 0.0))
assert np.allclose(rx, -x) and np.allclose(ry, -y) and np.allclose(rz, z)
print('Anti-parallel case: PASS')

print('rotate_to_sunward smoke test PASS')
"
```

Also run Mercury visual regression:

| Check | Pass criterion |
|-------|----------------|
| Mercury center, magnetosphere on | Renders identically to Phase A (default -X convention applies) |
| Mercury flyto with magnetosphere | Bow shock still faces Sun (rotation works through promoted helper) |
| Mercury info markers | Unchanged |
| Sodium tail | Unchanged (this isn't rotated; pre-existing limitation) |

If Mercury regressions fail, the promotion broke something — debug before proceeding to Section 6.

---

## 6. Venus + Mars: Configs + Custom Geometry + Delegation

Largest section. Venus has 6 sphere shells + 1 custom builder (which emits 2 trace groups). Mars has 7 sphere shells + 1 custom builder (which emits 3 trace groups).

### 6.1 Strategy

For each body (Venus first, then Mars):
1. Extract sphere shell config values (same auto-generation approach as Section 4).
2. Insert config block in `shell_configs.py`.
3. Refactor the custom geometry builder in its shell file: import `rotate_to_sunward` and `create_info_marker` from `orrery_rendering`, apply sunward rotation, replace old-style info markers with `create_info_marker()` calls, remove the per-shell `create_sun_direction_indicator` call.
4. Add CUSTOM_SHELLS registry entry in `shell_configs.py`.
5. Replace the body's if-block in `planet_visualization.py` with a one-line delegation.
6. Run syntax check; visual verification after Venus, then again after Mars.

### 6.2 Auto-generation script for Venus + Mars sphere configs

The same approach as Section 4.2, extended:

```python
# generate_phase_c1_venus_mars_configs.py
# Same machinery as generate_phase_c1_pluto_eris_configs.py
# but for Venus (6 sphere shells) + Mars (7 sphere shells).

# Standardization to apply:
# - Venus Hill sphere n_points: 30 -> 20 (matches Phase B Mercury/Planet 9 fix)
# - Mars Hill sphere n_points: 30 -> 20 (same)

BODIES = {
    'Venus': {
        'path': 'venus_visualization_shells.py',
        'shells': [
            ('core',             'create_venus_core_shell',             'venus_core_info'),
            ('mantle',           'create_venus_mantle_shell',           'venus_mantle_info'),
            ('crust',            'create_venus_crust_shell',            'venus_crust_info'),
            ('atmosphere',       'create_venus_atmosphere_shell',       'venus_atmosphere_info'),
            ('upper_atmosphere', 'create_venus_upper_atmosphere_shell', 'venus_upper_atmosphere_info'),
            ('hill_sphere',      'create_venus_hill_sphere_shell',      'venus_hill_sphere_info'),
        ],
    },
    'Mars': {
        'path': 'mars_visualization_shells.py',
        'shells': [
            ('inner_core',       'create_mars_inner_core_shell',       'mars_inner_core_info'),
            ('outer_core',       'create_mars_outer_core_shell',       'mars_outer_core_info'),
            ('mantle',           'create_mars_mantle_shell',           'mars_mantle_info'),
            ('crust',            'create_mars_crust_shell',            'mars_crust_info'),
            ('atmosphere',       'create_mars_atmosphere_shell',       'mars_atmosphere_info'),
            ('upper_atmosphere', 'create_mars_upper_atmosphere_shell', 'mars_upper_atmosphere_info'),
            ('hill_sphere',      'create_mars_hill_sphere_shell',      'mars_hill_sphere_info'),
        ],
    },
}

# (rest of the script identical to Section 4.2)
```

Run, review, insert into `shell_configs.py` after the Eris block.

### 6.3 Manual review checklist before inserting

Same as Section 4.3, plus:

- Venus Hill sphere: source `n_points=30`, script outputs 20 (standardization). Confirm in generated output.
- Mars Hill sphere: source `n_points=30`, script outputs 20. Confirm.
- Venus mantle: name='Mantle' (source has 'Mantle', no normalization needed).
- Venus atmosphere name='Lower Atmosphere' (source value, preserved). Tony's call whether to rename to 'Atmosphere' for consistency with Mercury/Pluto/Eris naming — recommend preserving as-is; the source distinguishes lower vs upper atmosphere which is meaningful.
- Mars uses `radius_fraction=0.5` for inner_core and `radius_fraction=0.8` for outer_core. Same convention as Mercury.

### 6.4 Venus magnetosphere refactor

In `venus_visualization_shells.py`, find `create_venus_magnetosphere_shell()` (currently around line 514).

#### 6.4.1 Import additions at top of file

Add to the existing import block:

```python
from orrery_rendering import rotate_to_sunward, create_info_marker
```

Place this near the existing imports. If the file currently imports from `shared_utilities` (line 19 area: `from shared_utilities import create_sun_direction_indicator`), keep that for backward compatibility — but the magnetosphere function will no longer call it.

#### 6.4.2 Apply sunward rotation to magnetosphere geometry

Current source (around line 542-551):

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

Update to:

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

#### 6.4.3 Apply sunward rotation to bow shock geometry

Current source (around line 683-686):

```python
    # Apply center position offset
    bow_shock_x = np.array(bow_shock_x) + center_x
    bow_shock_y = np.array(bow_shock_y) + center_y
    bow_shock_z = np.array(bow_shock_z) + center_z
```

Update to:

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

#### 6.4.4 Replace old-style info markers with create_info_marker()

Current Venus magnetosphere info marker (around line 641-654):

```python
    traces.append(
        go.Scatter3d(
            x=[x[0]], y=[y[0]], z=[z[0]],
            mode='markers',
            marker=dict(size=6, color='rgb(180, 180, 255)', opacity=0.9,
                        symbol='cross', line=dict(color='white', width=1)),
            name='',
            legendgroup='Venus: Magnetosphere',
            text=magnetosphere_text,
            customdata=magnetosphere_customdata,
            hovertemplate='%{text}<extra></extra>',
            showlegend=False
        )
    )
```

Replace with:

```python
    traces.append(create_info_marker(
        x[0], y[0], z[0],
        'rgb(180, 180, 255)', magnetosphere_text[0], 'Venus: Magnetosphere'
    ))
```

Note: `magnetosphere_text` in the source is a list of one string (`[...]`). `create_info_marker()` expects a string, so pass `magnetosphere_text[0]`.

Similarly for the bow shock info marker (around line 715-728):

```python
    traces.append(
        go.Scatter3d(
            x=[bow_shock_x[0]], y=[bow_shock_y[0]], z=[bow_shock_z[0]],
            mode='markers',
            marker=dict(size=6, color='rgb(255, 200, 150)', opacity=0.9,
                        symbol='cross', line=dict(color='white', width=1)),
            name='',
            legendgroup='Venus: Bow Shock',
            text=bow_shock_text,
            customdata=bow_shock_customdata,
            hovertemplate='%{text}<extra></extra>',
            showlegend=False
        )
    )
```

Replace with:

```python
    traces.append(create_info_marker(
        bow_shock_x[0], bow_shock_y[0], bow_shock_z[0],
        'rgb(255, 200, 150)', bow_shock_text[0], 'Venus: Bow Shock'
    ))
```

#### 6.4.5 Remove the per-shell sun direction indicator call

Current source (around line 730-735):

```python
    sun_traces = create_sun_direction_indicator(
        center_position=center_position, 
        shell_radius=60 * VENUS_RADIUS_AU
    )
    for trace in sun_traces:
        traces.append(trace)

    return traces
```

Replace with:

```python
    return traces
```

(Delete the entire `sun_traces = ...` block. The unified dispatch now issues one indicator per body in `create_celestial_body_visualization()`.)

### 6.5 Mars magnetosphere refactor

Mars magnetosphere is more complex — it emits THREE trace groups (magnetosphere, bow shock, crustal magnetic fields). Apply the same pattern to all three, with one important note: the crustal fields are random-seed-generated positions on the surface, intentionally NOT rotated to face the Sun (they're crustal anomalies frozen in the planetary body frame). Only magnetosphere and bow shock get the sunward rotation.

#### 6.5.1 Import additions at top of file

Same as Venus — add to `mars_visualization_shells.py`:

```python
from orrery_rendering import rotate_to_sunward, create_info_marker
```

#### 6.5.2 Apply sunward rotation to magnetosphere geometry

Current source (around line 620-629):

```python
    # Create magnetosphere main shape - reusing Earth's function but with Mars parameters
    x, y, z = create_magnetosphere_shape(params)
    
    # Unpack center position
    center_x, center_y, center_z = center_position
    
    # 1. Add the main induced magnetosphere structure
    x = np.array(x) + center_x
    y = np.array(y) + center_y
    z = np.array(z) + center_z
```

Update to:

```python
    # Create magnetosphere main shape (generated with -X as sunward)
    x, y, z = create_magnetosphere_shape(params)
    
    # Unpack center position
    center_x, center_y, center_z = center_position
    
    # 1. Add the main induced magnetosphere structure
    # Rotate to actual sunward direction, then offset to center position
    x, y, z = np.array(x), np.array(y), np.array(z)
    x, y, z = rotate_to_sunward(x, y, z, center_position=center_position)
    x = x + center_x
    y = y + center_y
    z = z + center_z
```

#### 6.5.3 Apply sunward rotation to bow shock

Current source (around line 688-691):

```python
    # Apply center position offset
    bow_shock_x = np.array(bow_shock_x) + center_x
    bow_shock_y = np.array(bow_shock_y) + center_y
    bow_shock_z = np.array(bow_shock_z) + center_z
```

Update to:

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

#### 6.5.4 Do NOT rotate the crustal magnetic fields

The crustal fields (around lines 735-832) are placed at random positions on Mars's surface using `np.random.seed(42)`. They represent magnetized rock in the southern hemisphere — features frozen in the planetary body frame. They should NOT rotate to face the Sun. Leave the crustal field generation block unchanged.

#### 6.5.5 Mars magnetosphere missing info marker

The source Mars magnetosphere trace (around lines 645-659) has this critical structural issue:

```python
    traces.append(
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=1.5,
                color='rgb(180, 180, 255)', # Light blue for magnetic field
                opacity=0.2
            ),
            name='Mars: Induced Magnetosphere',
            hoverinfo='skip',
            hovertemplate='%{text}<extra></extra>',
            showlegend=True
        )
    )
```

Note:
1. `hoverinfo='skip'` AND `hovertemplate='%{text}<extra></extra>'` — the template is dead code because hover is skipped.
2. No info marker follows this trace. `magnetosphere_text` is defined but never displayed.
3. No `legendgroup` is set, so the trace can't be cleanly toggled with a marker.

This is a pre-existing Step 2 omission. Phase C1 preserves the behavior (no marker) but adds `legendgroup` for consistency. Update the magnetosphere trace to:

```python
    traces.append(
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=1.5,
                color='rgb(180, 180, 255)',
                opacity=0.2
            ),
            name='Mars: Induced Magnetosphere',
            legendgroup='Mars: Induced Magnetosphere',
            hoverinfo='skip',
            showlegend=True
        )
    )
    # NOTE: Mars magnetosphere has no info marker (pre-existing Step 2 omission).
    # The hover_text exists as `magnetosphere_text` but is unused. Flagged in
    # the C1 handoff for separate fix; preserved as-is to avoid editorial
    # decisions in a mechanical refactor.
    # TODO: add create_info_marker call here in a future cleanup pass.
```

(Removed the dead `hovertemplate` parameter.)

#### 6.5.6 Replace bow shock info marker

Current (around line 720-733):

```python
    traces.append(
        go.Scatter3d(
            x=[bow_shock_x[0]], y=[bow_shock_y[0]], z=[bow_shock_z[0]],
            mode='markers',
            marker=dict(size=6, color='rgb(255, 200, 150)', opacity=0.9,
                        symbol='cross', line=dict(color='white', width=1)),
            name='',
            legendgroup='Mars: Bow Shock',
            text=bow_shock_text,
            customdata=bow_shock_customdata,
            hovertemplate='%{text}<extra></extra>',
            showlegend=False
        )
    )
```

Replace with:

```python
    traces.append(create_info_marker(
        bow_shock_x[0], bow_shock_y[0], bow_shock_z[0],
        'rgb(255, 200, 150)', bow_shock_text[0], 'Mars: Bow Shock'
    ))
```

#### 6.5.7 Replace crustal fields info marker

Current (around line 819-832, inside the `if i == 0:` block):

```python
            traces.append(
                go.Scatter3d(
                    x=[field_x[0]], y=[field_y[0]], z=[field_z[0]],
                    mode='markers',
                    marker=dict(size=6, color='rgb(255, 100, 255)', opacity=0.9,
                                symbol='cross', line=dict(color='white', width=1)),
                    name='',
                    legendgroup='Mars: Crustal Magnetic Fields',
                    text=crustal_field_text,
                    customdata=crustal_field_customdata,
                    hovertemplate='%{text}<extra></extra>',
                    showlegend=False
                )
            )
```

Replace with:

```python
            traces.append(create_info_marker(
                field_x[0], field_y[0], field_z[0],
                'rgb(255, 100, 255)', crustal_field_text[0],
                'Mars: Crustal Magnetic Fields'
            ))
```

(Keep the `if i == 0:` wrapper so the marker is only added once.)

#### 6.5.8 Remove the per-shell sun direction indicator call

Current source (around line 834-839):

```python
    sun_traces = create_sun_direction_indicator(
        center_position=center_position, 
        shell_radius=10 * MARS_RADIUS_AU
    )
    for trace in sun_traces:
        traces.append(trace)

    return traces
```

Replace with:

```python
    return traces
```

### 6.6 Add CUSTOM_SHELLS entries to shell_configs.py

After the Pluto/Eris sphere config blocks (added in Section 4), and within the `CUSTOM_SHELLS = {` dict, add Venus and Mars entries. Find the `CUSTOM_SHELLS` block (starts after `SHELL_CONFIGS` closing brace).

Insert after Mercury's CUSTOM_SHELLS block:

```python

    # ============================================================
    # Venus
    # ============================================================
    # Source: ESA Venus Express: Magnetosphere; NASA Pioneer Venus Results;
    #         induced magnetosphere, bow shock 1.3-1.7 Rv, comet-shaped tail.
    # Verified: April 2026 provenance audit.
    'Venus': {

        'magnetosphere': {
            'builder': 'venus_visualization_shells.create_venus_magnetosphere_shell',
            'tooltip': (
                "SET MANUAL SCALE TO AT LEAST 0.005 AU TO VISUALIZE.\n\n"
                "Venus has a very weak, induced magnetosphere. Unlike Earth's magnetic field, which is generated internally by its \n"
                "liquid iron core, Venus's weak magnetosphere is formed by the interaction of the solar wind with the planet's \n"
                "ionosphere (the upper layer of its atmosphere containing charged particles). This induced magnetosphere is not as \n"
                "effective at deflecting charged particles from the Sun as Earth's strong magnetic field.\n\n"
                "The same builder also produces the bow shock trace (separate legend entry)."
            ),
        },

    },

    # ============================================================
    # Mars
    # ============================================================
    # Source: NASA MAVEN; NASA Solar System Exploration;
    #         induced magnetosphere, bow shock 1.5 Rm, crustal magnetic fields
    #         (Acuna et al. 1999 -- MGS MAG/ER discovery).
    # Verified: April 2026 provenance audit via Gemini fact-check.
    'Mars': {

        'magnetosphere': {
            'builder': 'mars_visualization_shells.create_mars_magnetosphere_shell',
            'tooltip': (
                "SET MANUAL SCALE TO AT LEAST 0.005 AU TO VISUALIZE.\n\n"
                "Unlike Earth, Mars lacks a global magnetic field generated by its core. Instead, it has:\n"
                "1. Induced Magnetosphere: Created by the interaction between the solar wind and Mars' ionosphere.\n"
                "2. Bow Shock: Forms where the solar wind first encounters Mars' atmosphere/ionosphere (~1.5 Mars radii).\n"
                "3. Crustal Magnetic Fields: Localized 'mini-magnetospheres' from magnetized regions in Mars' crust.\n\n"
                "The same builder produces all three traces (separate legend entries)."
            ),
        },

    },

```

Note: per Phase A's pattern with Mercury, ONE CUSTOM_SHELLS entry maps to one builder function, but the builder is free to return multiple trace groups (legend entries). The CUSTOM_SHELLS dict isn't a 1:1 map to legend entries.

### 6.7 Verify Venus and Mars custom geometry via dispatch

The `create_celestial_body_visualization` dispatch iterates `shell_vars` and looks up each shell name in SHELL_CONFIGS first, then CUSTOM_SHELLS. For Venus, the GUI passes `venus_magnetosphere` as the var name. The dispatch strips the `venus_` prefix, yielding `magnetosphere`, which finds Venus's CUSTOM_SHELLS entry and lazy-imports the builder.

Verify after insertion:

```bash
python3 -c "
from shell_configs import SHELL_CONFIGS, CUSTOM_SHELLS

# Venus sphere shells
assert 'Venus' in SHELL_CONFIGS
venus = SHELL_CONFIGS['Venus']
assert set(venus.keys()) == {'core', 'mantle', 'crust', 'atmosphere', 'upper_atmosphere', 'hill_sphere'}, \
    'Venus sphere keys: %s' % sorted(venus.keys())
assert venus['crust']['geometry_type'] == 'mesh3d'

# Venus custom
assert 'Venus' in CUSTOM_SHELLS
assert 'magnetosphere' in CUSTOM_SHELLS['Venus']
assert CUSTOM_SHELLS['Venus']['magnetosphere']['builder'].endswith('create_venus_magnetosphere_shell')

# Mars sphere shells
assert 'Mars' in SHELL_CONFIGS
mars = SHELL_CONFIGS['Mars']
assert set(mars.keys()) == {'inner_core', 'outer_core', 'mantle', 'crust', 'atmosphere', 'upper_atmosphere', 'hill_sphere'}, \
    'Mars sphere keys: %s' % sorted(mars.keys())
assert mars['crust']['geometry_type'] == 'mesh3d'

# Mars custom
assert 'Mars' in CUSTOM_SHELLS
assert 'magnetosphere' in CUSTOM_SHELLS['Mars']

print('Venus/Mars configs verified')
"
```

### 6.8 Delegation edits in planet_visualization.py

Find the Venus if-block (currently lines 680-694):

```python
    if planet_name == 'Venus':
        if shell_vars['venus_core'].get() == 1:
            traces.extend(create_venus_core_shell(center_position))
        if shell_vars['venus_mantle'].get() == 1:
            traces.extend(create_venus_mantle_shell(center_position))
        if shell_vars['venus_crust'].get() == 1:
            traces.extend(create_venus_crust_shell(center_position))
        if shell_vars['venus_atmosphere'].get() == 1:
            traces.extend(create_venus_atmosphere_shell(center_position))
        if shell_vars['venus_upper_atmosphere'].get() == 1:
            traces.extend(create_venus_upper_atmosphere_shell(center_position))
        if shell_vars['venus_magnetosphere'].get() == 1:
            traces.extend(create_venus_magnetosphere_shell(center_position))
        if shell_vars['venus_hill_sphere'].get() == 1:
            traces.extend(create_venus_hill_sphere_shell(center_position))
```

Replace with:

```python
    if planet_name == 'Venus':
        # Step 3 Phase C1: delegate to unified config-driven dispatch.
        # Custom geometry: venus_magnetosphere -> CUSTOM_SHELLS['Venus']['magnetosphere']
        # which lazy-imports and emits both magnetosphere and bow shock traces.
        return create_celestial_body_visualization(
            fig, planet_name, shell_vars,
            animate=animate, frames=frames,
            center_position=center_position,
            object_type='Venus',
            center_object='Venus',
        )
```

Find the Mars if-block (currently lines 734-750):

```python
    if planet_name == 'Mars':
        if shell_vars['mars_inner_core'].get() == 1:
            traces.extend(create_mars_inner_core_shell(center_position))
        if shell_vars['mars_outer_core'].get() == 1:
            traces.extend(create_mars_outer_core_shell(center_position))
        if shell_vars['mars_mantle'].get() == 1:
            traces.extend(create_mars_mantle_shell(center_position))
        if shell_vars['mars_crust'].get() == 1:
            traces.extend(create_mars_crust_shell(center_position))
        if shell_vars['mars_atmosphere'].get() == 1:
            traces.extend(create_mars_atmosphere_shell(center_position))
        if shell_vars['mars_upper_atmosphere'].get() == 1:
            traces.extend(create_mars_upper_atmosphere_shell(center_position))
        if shell_vars['mars_magnetosphere'].get() == 1:
            traces.extend(create_mars_magnetosphere_shell(center_position))
        if shell_vars['mars_hill_sphere'].get() == 1:
            traces.extend(create_mars_hill_sphere_shell(center_position))
```

Replace with:

```python
    if planet_name == 'Mars':
        # Step 3 Phase C1: delegate to unified config-driven dispatch.
        # Custom geometry: mars_magnetosphere -> CUSTOM_SHELLS['Mars']['magnetosphere']
        # which lazy-imports and emits magnetosphere, bow shock, and crustal fields.
        return create_celestial_body_visualization(
            fig, planet_name, shell_vars,
            animate=animate, frames=frames,
            center_position=center_position,
            object_type='Mars',
            center_object='Mars',
        )
```

### 6.9 Bottom-up edit order

Mars (line ~734) is higher than Venus (line ~680). Apply Mars first, then Venus.

### 6.10 Syntax checks after Section 6

```bash
python3 -m py_compile shell_configs.py planet_visualization.py \
    venus_visualization_shells.py mars_visualization_shells.py orrery_rendering.py \
    mercury_visualization_shells.py
```

No output = success.

### 6.11 Mode 5 visual verification for Venus + Mars

Run the orrery after each body's migration. Don't batch them — Mars's crustal fields are visually distinctive and you want to catch regressions before moving on.

Venus checks:

| Check | Pass criterion |
|-------|----------------|
| Venus center, all sphere shells on | All 6 render via unified dispatch |
| Venus crust mesh3d | Pale yellow solid surface |
| Venus magnetosphere on (centered) | Light blue particle cloud renders; bow shock orange paraboloid behind |
| Venus magnetosphere info markers | Cross at first geometry point for each (size=8, red outline) |
| Venus flyto from outer system | Bow shock faces Sun (rotation works) |
| Sun direction indicator | Appears ONCE per render |

Mars checks:

| Check | Pass criterion |
|-------|----------------|
| Mars center, all sphere shells on | All 7 render via unified dispatch |
| Mars crust mesh3d | Red-orange solid surface (rgb(188, 39, 50)) |
| Mars magnetosphere on (centered) | Three legend entries: Magnetosphere, Bow Shock, Crustal Magnetic Fields |
| Mars crustal fields | Purple dots in southern hemisphere (np.random.seed=42 reproducible) |
| Mars magnetosphere flyto | Bow shock rotates to face Sun; crustal fields stay surface-anchored |
| Mars magnetosphere info marker | ABSENT (pre-existing Step 2 omission, preserved) |
| Mars bow shock info marker | Cross at first geometry point (new style) |
| Mars crustal fields info marker | Cross at first crustal-field point (new style) |
| Sun direction indicator | Appears ONCE per render |

Pluto/Eris/Mercury/Moon/Planet 9 regression check:

| Check | Pass criterion |
|-------|----------------|
| Switch center to Mercury, render all shells | No change from Phase A |
| Switch center to Pluto, render all shells | Renders as established in Section 4 |
| Switch center to Eris, render all shells | Renders as established in Section 4 |

---

## 7. Verification Plan

### 7.1 Static checks

```bash
# All touched files compile
python3 -m py_compile shell_configs.py planet_visualization.py orrery_rendering.py \
    mercury_visualization_shells.py venus_visualization_shells.py \
    mars_visualization_shells.py palomas_orrery.py

# All touched files are LF
for f in shell_configs.py planet_visualization.py orrery_rendering.py \
         mercury_visualization_shells.py venus_visualization_shells.py \
         mars_visualization_shells.py palomas_orrery.py; do
    file "$f" | grep -q CRLF && echo "FAIL: $f CRLF" || echo "OK: $f"
done

# All touched files are ASCII
python3 -c "
import sys
for f in ['shell_configs.py', 'planet_visualization.py', 'orrery_rendering.py',
         'mercury_visualization_shells.py', 'venus_visualization_shells.py',
         'mars_visualization_shells.py', 'palomas_orrery.py']:
    with open(f, 'rb') as fh:
        content = fh.read().decode('utf-8', errors='replace')
    issues = sum(1 for c in content if ord(c) > 127)
    print('%-45s %s' % (f, 'OK' if not issues else 'FAIL: %d non-ASCII' % issues))
"
```

### 7.2 Import smoke test

```bash
python3 -c "
from orrery_rendering import build_sphere_shell, create_info_marker, rotate_to_sunward
from shell_configs import SHELL_CONFIGS, CUSTOM_SHELLS
from planet_visualization import create_celestial_body_visualization, create_planet_visualization

# All Phase A+B+C1 bodies present
for body in ['Mercury', 'Moon', 'Planet 9', 'Pluto', 'Eris', 'Venus', 'Mars']:
    assert body in SHELL_CONFIGS, '%s missing from SHELL_CONFIGS' % body

# CUSTOM_SHELLS bodies
for body in ['Mercury', 'Venus', 'Mars']:
    assert body in CUSTOM_SHELLS, '%s missing from CUSTOM_SHELLS' % body

# Counts
assert len(SHELL_CONFIGS['Pluto']) == 6
assert len(SHELL_CONFIGS['Eris']) == 5
assert len(SHELL_CONFIGS['Venus']) == 6
assert len(SHELL_CONFIGS['Mars']) == 7
assert len(CUSTOM_SHELLS['Venus']) == 1
assert len(CUSTOM_SHELLS['Mars']) == 1

print('All Phase C1 imports and counts PASS')
"
```

### 7.3 Builder smoke test (sphere shells only)

```bash
python3 -c "
from orrery_rendering import build_sphere_shell
from shell_configs import SHELL_CONFIGS

for body in ['Pluto', 'Eris', 'Venus', 'Mars']:
    for shell_name, cfg in SHELL_CONFIGS[body].items():
        traces = build_sphere_shell(cfg, body, (0, 0, 0))
        assert len(traces) == 2, '%s/%s expected 2 traces, got %d' % (body, shell_name, len(traces))

print('Sphere builder smoke test PASS')
"
```

### 7.4 Custom geometry smoke test

```bash
python3 -c "
import importlib

# Venus magnetosphere
mod = importlib.import_module('venus_visualization_shells')
traces = mod.create_venus_magnetosphere_shell((0, 0, 0))
assert len(traces) >= 4  # 2 geometry traces + 2 info markers (magnetosphere + bow shock)

# Mars magnetosphere
mod = importlib.import_module('mars_visualization_shells')
traces = mod.create_mars_magnetosphere_shell((0, 0, 0))
# Mars: magnetosphere (1 trace, no info marker) + bow shock (2 traces) + crustal fields (7*1 + 1 marker = 8 traces)
# Total: 1 + 2 + 8 = 11 traces
assert len(traces) >= 10

print('Custom geometry smoke test PASS')
"
```

### 7.5 rotate_to_sunward correctness

```bash
python3 -c "
import numpy as np
from orrery_rendering import rotate_to_sunward

# Body at +X 1.0 AU, Sun at origin: sunward = -X
# Default geometry generated with -X as sunward should not rotate
x = np.array([-1.0, -0.5, 0.0])  # 'sunward' arrow in default frame
y = np.array([0.0, 0.0, 0.0])
z = np.array([0.0, 0.0, 0.0])
rx, ry, rz = rotate_to_sunward(x, y, z, center_position=(1.0, 0.0, 0.0))
# Sun at origin, body at (1,0,0): actual sunward = (-1,0,0) = default. No rotation.
assert np.allclose(rx, x) and np.allclose(ry, y) and np.allclose(rz, z), \
    'Expected no rotation when default and actual sunward align'

# Body at -X 1.0 AU: actual sunward = +X (opposite of default). 180 deg.
rx, ry, rz = rotate_to_sunward(x, y, z, center_position=(-1.0, 0.0, 0.0))
assert np.allclose(rx, -x), 'Expected x to flip'
assert np.allclose(ry, -y), 'Expected y to flip'
assert np.allclose(rz, z), 'Expected z unchanged for 180 rotation about Z'

# sun_position parameter: body at origin, sun at (1,0,0). Actual sunward = +X.
# Same 180 deg rotation as before.
rx, ry, rz = rotate_to_sunward(x, y, z, center_position=(0, 0, 0), sun_position=(1.0, 0.0, 0.0))
assert np.allclose(rx, -x), 'sun_position parameter: expected 180 rotation'

print('rotate_to_sunward correctness PASS')
"
```

### 7.6 Indicator de-duplication check

Switch center to each migrated body in turn. Enable all shells. Confirm:

- Exactly one Sun direction indicator per render (legend shows "Sun Direction" once)
- For body-centered views, indicator is suppressed (Sun is visible at origin, no arrow needed)
- For flyto/off-center views, indicator scales to outermost active shell

### 7.7 GUI tooltip regression check

Hover the GUI checkboxes for all C1 body shells. Tooltips should display correctly, sourced from `pluto_*_info`, `eris_*_info`, `venus_*_info`, `mars_*_info` strings via the `globals()` lookup in `build_shell_checkboxes`. The `_info` strings are still defined in their shell files (Phase C1 does NOT remove them). Phase D will switch to reading from configs.

### 7.8 Axis auto-scale check

For each migrated body when centered, enable Auto scaling and verify the axis range adapts to the outermost active shell radius. Same pattern as Phase B for Moon.

### 7.9 Mode 5 visual verification items for Tony

Per body, focus on:

**Pluto**:
- Crust solid surface renders cleanly (brownish, rgb(83, 68, 55))
- Mantle dot sphere at 0.99 of body radius (very close to crust — thin visible gap)
- Haze layer thin blue dot sphere at 1.17
- Atmosphere thicker dot sphere at 1.43 (still small in absolute AU)
- Hill sphere green sparse sphere requires manual scale (per tooltip)
- Verify the lowercase-to-capitalized 'Mantle' normalization is acceptable

**Eris**:
- Crust off-white solid surface (rgb(240, 240, 240))
- Atmosphere at 1.005 — very thin layer (Eris has transient atmosphere only at perihelion). Tiny gap between crust and atmosphere may be visually imperceptible at default scale. This is correct physics.
- Hill sphere green sparse sphere (very large, requires manual scale)

**Venus**:
- Crust pale yellow mesh3d
- Atmosphere/upper_atmosphere both pastel blue with different opacity
- Magnetosphere light blue cloud + bow shock orange paraboloid behind
- In flyto view: bow shock faces Sun, magnetotail trails away (rotation works)
- Hill sphere at 166 Vr — very large green sphere

**Mars**:
- Inner core / outer core differentiated colors (rgb(255, 180, 140) inner, rgb(255, 140, 0) outer)
- Crust red mesh3d (rgb(188, 39, 50))
- Three magnetosphere components visible: magnetosphere (light blue), bow shock (orange), crustal fields (purple in southern hemisphere)
- Mars magnetosphere has NO info marker (preserved pre-existing omission). Bow shock and crustal fields DO have markers (new style).

### 7.10 File size baseline (informational)

Save a static plot for each newly migrated body. Compare to pre-C1 baselines if available. Expected: similar or smaller (info marker consolidation already done in Step 2; C1 doesn't add new size optimizations).

---

## 8. Decision Log and Open Items

### Decisions made by this manifest

1. **Pluto mantle name normalized to 'Mantle'** (source has lowercase `'mantle'`). Cosmetic consistency fix. Pass-through if Tony prefers preserving lowercase.

2. **Venus Hill sphere n_points: 30 -> 20.** Matches Phase B Mercury/Planet 9 standardization pattern.

3. **Mars Hill sphere n_points: 30 -> 20.** Same standardization.

4. **Venus atmosphere name kept as 'Lower Atmosphere'.** The source distinguishes lower vs upper atmosphere meaningfully. Renaming for consistency with other bodies would lose information.

5. **Mars magnetosphere missing info marker preserved.** This is a pre-existing Step 2 omission, not a C1 regression. Adding a marker requires editorial decisions (where to place it, what hover text to display — `magnetosphere_text` is the existing source but never displayed). Flagged for separate fix; preserving as-is to keep C1 mechanical.

6. **`rotate_to_sunward()` promoted with `magnetic_tilt_deg=0` placeholder.** Tilt parameter accepted but not yet applied. Phase C4 (Uranus, Neptune) is the natural place to wire actual tilt rotation. Documenting the parameter from the start prevents an API expansion later.

7. **`sun_position` defaults to `(0, 0, 0)`.** Phase C1 callers continue to assume Sun-at-origin. Phase D wires actual Sun position from the ephemeris pipeline. The parameter exists in the API so the wiring is additive, not breaking.

8. **Crustal fields NOT rotated to sunward.** They're surface-anchored magnetic anomalies in the planetary body frame. Source already treats them this way; the C1 refactor preserves the distinction.

9. **CUSTOM_SHELLS one entry per builder, not per legend group.** Venus's magnetosphere builder emits 2 legend groups (magnetosphere, bow shock) but registers as 1 CUSTOM_SHELLS entry. Mars emits 3 legend groups (magnetosphere, bow shock, crustal fields) as 1 entry. This matches Mercury's Phase A precedent.

10. **`venus_visualization_shells.py` and `mars_visualization_shells.py` retain dead sphere functions.** Their custom geometry functions are still used; sphere shell functions become unreachable but stay in place. Phase D decides per-file fate (selective deletion of dead functions vs. whole-file split).

11. **Pluto and Eris shell files left untouched.** Both become entirely dead — batch-archived in Phase D. No edits in C1.

12. **ASCII cleanup applied in C1 (not deferred).** Seven characters across three files. Small enough to include without overhead.

13. **No GUI changes in C1.** All four bodies already have full `build_shell_checkboxes` wiring and `tk.IntVar` definitions. No Phase E plumbing needed.

### Open items for future phases

- **Mars magnetosphere info marker**: separate editorial fix outside C1 scope. Decide position (first geometry point? centroid? a specific named point along the magnetotail?) and finalize hover text.
- **Phase D sun_position wiring**: when callers move from `create_planet_visualization` to `create_celestial_body_visualization` directly, pass the actual Sun ephemeris position. Default `(0, 0, 0)` works in heliocentric views; matters for body-centered views with Sun offset.
- **Phase C4 magnetic_tilt_deg application**: implement the second rotation in `rotate_to_sunward` when Uranus's 60-deg dipole tilt is migrated.
- **Pluto Hill sphere `_info` tooltip prefix size warning**: source contains "4.6 MB PER FRAME FOR HTML" which is stale (post-Step-2 size is much smaller). Cosmetic; can be updated when Pluto shell file is archived.
- **Crust mesh3d visual policy**: Tony's call whether the mesh3d solid-surface look should propagate to ALL crusts in C2-D, or revert to dot spheres for outer planets (Jupiter, Saturn, etc. don't have "crusts" — they'd use cloud_layer mesh3d instead).

### Risks and mitigations

| Risk | Mitigation |
|------|-----------|
| Pluto/Eris auto-generation script produces malformed output | Section 4.3 manual review checklist before insertion |
| `rotate_to_sunward` promotion breaks Mercury | Section 5.4 explicit smoke test + Mercury visual regression |
| Venus/Mars magnetosphere refactor introduces wrong rotation direction | Section 7.5 unit test; Section 7.9 visual verification (flyto bow shock direction) |
| Mars crustal fields accidentally rotated | Section 6.5.4 explicit "do not rotate" note; visual check that southern hemisphere distribution unchanged |
| n_points standardization changes Venus/Mars Hill sphere visual density | Pre-decided per Phase B; minor cosmetic change |
| Body prefix collision in dispatch (e.g. Venus's 'core' shell vs Mercury's 'core') | Already tested: dispatch is per-body; SHELL_CONFIGS[body][shell] is scoped |
| ASCII cleanup breaks UTF-8 multi-byte sequences elsewhere | Python binary mode + only replacing known byte sequences (em-dash, arrow, degree) |
| Lazy import for Venus/Mars CUSTOM_SHELLS fails silently | Section 7.4 explicit smoke test that calls the builder via importlib |

### Implementation discipline (per protocol)

- Python binary mode (`rb`/`wb`) for all file reads/writes
- Bottom-up editing when multiple edits to same file (Section 4.6, 6.9)
- Exact-string matching with `str_replace`, never regex
- One section at a time; run syntax check before proceeding
- Credit line update: `Module updated: May 2026 with Anthropic's Claude Opus 4.7` on every modified file. Update existing credit lines on `mercury_visualization_shells.py`, `venus_visualization_shells.py`, `mars_visualization_shells.py`, `orrery_rendering.py`, `planet_visualization.py`, `shell_configs.py`.
- ASCII only — verify after each section's edits with `grep -P '[^\x00-\x7F]'`
- If any source value can't be confirmed from the project files, STOP and ask Tony

---

## 9. Phase C1 Summary

| Body | Sphere shells | Custom shells | Lines changed | File archivable in D |
|------|:-------------:|:-------------:|:-------------:|:-------------------:|
| Pluto | 6 | 0 | ~12 (delegation only) | Yes |
| Eris | 5 | 0 | ~12 (delegation only) | Yes |
| Venus | 6 | 1 | ~60 (delegation + magnetosphere refactor) | No (magnetosphere only) |
| Mars | 7 | 1 | ~80 (delegation + magnetosphere refactor) | No (magnetosphere only) |

Total: 24 sphere shell configs + 2 CUSTOM_SHELLS entries + 1 helper promotion + 1 ASCII cleanup pass + 4 delegations.

After Phase C1:
- 7 bodies on unified dispatch (Mercury, Moon, Planet 9, Pluto, Eris, Venus, Mars)
- 6 bodies still on `create_planet_visualization` (Earth, Jupiter, Saturn, Uranus, Neptune, Sun)
- 2 shell files fully dead (Pluto, Eris) — batch-archive in D
- 1 shared helper promoted (`rotate_to_sunward`) — ready for C2's Earth magnetosphere and beyond
- `sun_position` parameter threaded into the helper — Phase D wires the actual value

---

## 10. Workflow Provenance

This manifest:
- Audited by Anthropic's Claude Opus 4.7
- Following Phase B handoff (May 14, 2026) by Opus 4.6
- From prompt v3 by Tony Quintanilla + Anthropic's Claude Opus 4.6 (revised May 14, 2026)
- Following protocol v3.22 (collegial Mode 7)

To be executed by: Anthropic's Claude Opus 4.6 + Tony, in a separate session.

The Phase A+B manifests set the quality bar. Phase C1 expands scope (4 bodies, custom geometry, helper promotion) — aim for the same precision per body.

Implementing Claude: if Section 4 (Pluto/Eris) verifies cleanly but context starts pressuring before Section 5/6, stop and write a partial handoff. Phase C1 can be split across sessions at the Section 4/5 boundary without functional regression (the codebase remains fully functional with Pluto/Eris on unified dispatch and Venus/Mars on the old path).

*Module updated: May 2026 with Anthropic's Claude Opus 4.7*
