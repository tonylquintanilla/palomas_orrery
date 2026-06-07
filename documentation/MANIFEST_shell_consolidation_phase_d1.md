# MANIFEST: Shell Consolidation Step 3 -- Phase D1 (Sun Config Extraction)

**Project:** Paloma's Orrery | Plotting Consolidation Step 3
**Date:** May 18, 2026
**Source prompt:** `PROMPT_shell_consolidation_D1.md`
**Phase C4 handoff:** `HANDOFF_shell_consolidation_phase_c4.md` (May 18, 2026)
**Decisions reply:** `REPLY_D1_review_response.md` (May 18, 2026, Tony + Opus 4.6)
**Manifest by:** Anthropic's Claude Opus 4.7 (audit + draft)
**For execution by:** Anthropic's Claude Opus 4.6 (implementation) + Tony (integrator)

---

## 1. Phase D1 Scope and Execution Model

### What Phase D1 delivers

Pure additive registration of Sun shell configurations into the unified
dispatch registries. Two files touched. No call sites changed. No
existing behavior modified.

| Component | Before D1 | After D1 |
|-----------|----------:|---------:|
| Bodies in SHELL_CONFIGS | 12 | 13 (+Sun) |
| Total sphere shell configs | 68 | 83 (+15) |
| Bodies in CUSTOM_SHELLS | 8 | 9 (+Sun) |
| Total custom entries | 21 | 24 (+3) |
| Bodies still on old dispatch | 1 (Sun) | 1 (Sun, registered but unused) |

The Sun continues to render through `create_sun_visualization()` after
D1. The newly registered SHELL_CONFIGS and CUSTOM_SHELLS entries are
dormant -- they exist but are not yet invoked by the unified dispatch.
A later phase (D2 or successor) replaces the two call sites in
`palomas_orrery.py` to activate them.

This separation is deliberate: D1 isolates the mechanical extraction
work from the call site / asteroid belt / animation path concerns,
each of which deserves its own design conversation.

### What Phase D1 explicitly does NOT do

- **Call site replacement** in `palomas_orrery.py` (lines 4508-4509,
  6148-6149). `create_sun_visualization()` stays alive.
- **Asteroid belt migration** (`main_belt`, `hildas`, `trojans_greeks`,
  `trojans_trojans`). Deferred to a successor phase.
- **`corona_from_distance`** rendering path. Untouched.
- **`sun_position` wiring**. The new custom Sun builders accept the
  `center_position` parameter but do not yet use it to translate
  geometry; this is forward-compat for D2.
- **`build_sphere_shell` or `create_celestial_body_visualization`
  changes**. The dispatch already supports `radius_au` directly --
  no rendering-layer edits needed.
- **`_info` import cleanup** in `palomas_orrery.py` and helpers.
  Tracked as deferred item 5 in C4 handoff, scoped to D3.
- **`create_planet_visualization()` retirement**. Tracked as deferred
  item 3 in C4 handoff, scoped to D3.

### Files touched

| File | Lines (before) | Lines (after est.) | Changes |
|------|---------------:|-------------------:|---------|
| `shell_configs.py` | 2,260 | ~2,650 | +`SHELL_CONFIGS['Sun']` (15 entries), +`CUSTOM_SHELLS['Sun']` (3 entries) |
| `solar_visualization_shells.py` | 1,759 | ~1,540 | Dead code stripped (~220 lines), 3 custom function signatures extended with `center_position=(0,0,0)`, duplicate import block removed |

### Files explicitly NOT touched

- `palomas_orrery.py` -- call sites and shell_vars dict unchanged
- `planet_visualization.py` -- `create_sun_visualization()` and
  `create_sun_corona_from_distance()` unchanged; dispatch unchanged
- `orrery_rendering.py` -- `build_sphere_shell()` already supports
  `radius_au` (line 89-90)

### Execution order (canonical)

D1 is a single session. Order within the session:

1. Pre-flight verification (Section 2)
2. Decide the legend-name policy (Section 3.0)
3. Generate Sun sphere config block via the auto-gen script (Section 3.2)
4. Build `SHELL_CONFIGS['Sun']` and insert into `shell_configs.py` (Section 3.3)
5. Build `CUSTOM_SHELLS['Sun']` and insert into `shell_configs.py` (Section 4)
6. Strip dead code in `solar_visualization_shells.py` (Section 5)
7. Add `center_position=(0,0,0)` parameter to 3 custom functions (Section 6)
8. Verification (Section 7)

Bottom-up editing within each file. Python binary mode for both files.


---

## 2. Pre-flight Verification

Run these checks against the current `/mnt/project/` snapshot before
making any edits. Each check has a specific assertion that must pass.

### 2.1 Confirm Phase C4 is in place

```bash
python3 -c "
from shell_configs import SHELL_CONFIGS, CUSTOM_SHELLS
expected_bodies = {
    'Mercury', 'Moon', 'Planet 9', 'Pluto', 'Eris',
    'Venus', 'Mars', 'Earth', 'Jupiter',
    'Saturn', 'Uranus', 'Neptune',
}
assert set(SHELL_CONFIGS.keys()) == expected_bodies, (
    'Expected 12 bodies pre-D1, got %s' % set(SHELL_CONFIGS.keys())
)
expected_custom = {'Mercury', 'Venus', 'Mars', 'Earth', 'Jupiter',
                   'Saturn', 'Uranus', 'Neptune'}
assert set(CUSTOM_SHELLS.keys()) == expected_custom, (
    'Expected 8 custom bodies pre-D1, got %s' % set(CUSTOM_SHELLS.keys())
)
print('Pre-D1 state: 12 SHELL_CONFIGS, 8 CUSTOM_SHELLS. PASS')
"
```

### 2.2 Confirm `build_sphere_shell` supports `radius_au`

```bash
grep -n "if 'radius_au' in config:" /mnt/project/orrery_rendering.py
```

Must return a hit at line 89 (or nearby). If absent, STOP and reread
the dispatch contract; the Sun configs rely on this path.

### 2.3 Confirm Sun sphere shell functions exist with expected names

```bash
python3 -c "
import solar_visualization_shells as m
expected = [
    'create_sun_core_shell', 'create_sun_radiative_shell',
    'create_sun_photosphere_shell', 'create_sun_chromosphere_shell',
    'create_sun_inner_corona_shell', 'create_sun_streamer_belt_shell',
    'create_sun_roche_limit_shell', 'create_sun_alfven_surface_shell',
    'create_sun_outer_corona_shell', 'create_sun_termination_shock_shell',
    'create_sun_heliopause_shell', 'create_sun_inner_oort_limit_shell',
    'create_sun_inner_oort_shell', 'create_sun_outer_oort_shell',
    'create_sun_gravitational_shell',
]
for fname in expected:
    assert hasattr(m, fname), 'Missing: %s' % fname
print('15 Sun sphere shell functions present. PASS')
"
```

### 2.4 Confirm 3 custom Sun functions exist

```bash
python3 -c "
import solar_visualization_shells as m
for fname in ('create_sun_hills_cloud_torus',
              'create_sun_outer_oort_clumpy',
              'create_sun_galactic_tide'):
    assert hasattr(m, fname), 'Missing: %s' % fname
print('3 custom Sun functions present. PASS')
"
```

### 2.5 Confirm `*_info_hover` strings present (including the
`solar_wind_*` aliases for heliopause)

```bash
python3 -c "
import solar_visualization_shells as m
required = [
    'core_info_hover', 'radiative_zone_info_hover',
    'photosphere_info_hover', 'chromosphere_info_hover',
    'inner_corona_info_hover', 'streamer_belt_info_hover',
    'roche_limit_info_hover', 'alfven_surface_info_hover',
    'outer_corona_info_hover', 'termination_shock_info_hover',
    'solar_wind_info_hover',  # used by heliopause -- NOT heliopause_info_hover
    'inner_limit_oort_info_hover',
    'inner_oort_info_hover', 'outer_oort_info_hover',
    'gravitational_influence_info_hover',
]
for s in required:
    assert hasattr(m, s), 'Missing: %s' % s
print('15 *_info_hover strings present (heliopause uses solar_wind_info_hover). PASS')
"
```

If any of these are missing, STOP. Do NOT invent strings from training
memory (fetched-vs-recalled rule).

### 2.6 Confirm `sun_shell_vars` bare-key dict shape

```bash
grep -n "'core':\|'radiative':\|'gravitational':\|'inner_oort_limit':" /mnt/project/palomas_orrery.py | head -10
```

Expect bare keys (no `sun_` prefix). If keys differ, the SHELL_CONFIGS
keys must adapt to match what `sun_shell_vars` actually contains.

### 2.7 Confirm `solar_wind_info` / `solar_wind_info_hover` are LIVE,
not dead

```bash
grep -n "solar_wind_info" /mnt/project/palomas_orrery.py
grep -n "solar_wind_info_hover" /mnt/project/solar_visualization_shells.py
```

Both must show usage (heliopause checkbutton tooltip in `palomas_orrery.py`;
text reference inside `create_sun_heliopause_shell` in
`solar_visualization_shells.py`). These constants are NOT in the dead
code list -- they ARE the heliopause's hover/tooltip strings under
legacy naming.

### 2.8 Backup files Phase D1 will touch

```bash
cp shell_configs.py shell_configs.py.pre_d1.bak
cp solar_visualization_shells.py solar_visualization_shells.py.pre_d1.bak
```

### 2.9 LF / ASCII baseline check

```bash
for f in shell_configs.py solar_visualization_shells.py; do
    if grep -lU $'\r' "$f"; then
        echo "WARN: $f has CRLF (pre-existing -- fix during edits via Python binary mode)"
    fi
    file "$f" | grep -q "ASCII" || echo "WARN: $f is not pure ASCII"
done
```

`palomas_orrery_helpers.py` is known CRLF (deferred item 9 in C4
handoff). It is NOT touched in D1.


---

## 3. Sun Sphere Config Extraction

### 3.0 Legend-name policy decision (OPEN QUESTION)

**This is the only open design question in D1. It must be resolved
before writing `SHELL_CONFIGS['Sun']`.**

The reply document's mapping table lists trace names verbatim from
source -- e.g. `Sun: Core`, `Solar Wind Heliopause`,
`"Sun's Gravitational Influence"`. The reply's clarification B says
to extract `'name'` field values from source `go.Scatter3d(name=...)`
calls without inventing.

The complication: `build_sphere_shell()` constructs the rendered trace
name as `"%s: %s" % (body_name, config['name'])`
(`orrery_rendering.py:101`). For Mercury, source had
`name='Mercury: Inner Core'` and config has `'name': 'Inner Core'` --
the dispatch adds the prefix back. If we put `'Sun: Core'` literally
into the config's `'name'` field, the dispatch produces
`"Sun: Sun: Core"` -- double prefix.

So the config `'name'` field must be the part AFTER `"Sun: "`. For
9 of the 15 Sun shells this is straightforward:

| Source trace name | Config `'name'` (clean) |
|-------------------|-------------------------|
| `Sun: Core` | `Core` |
| `Sun: Radiative Zone` | `Radiative Zone` |
| `Sun: Photosphere` | `Photosphere` |
| `Sun: Chromosphere` | `Chromosphere` |
| `Sun: Inner Corona` | `Inner Corona` |
| `Sun: Streamer Belt (Visible Corona)` | `Streamer Belt (Visible Corona)` |
| `Sun: Roche Limit (Comets)` | `Roche Limit (Comets)` |
| `Sun: Alfven Surface` | `Alfven Surface` |
| `Sun: Outer Corona` | `Outer Corona` |

For 6 shells, the source trace name does NOT follow the
`"Sun: <X>"` pattern:

| Source trace name | Eventual dispatch-rendered name if config name = . . . |
|-------------------|-------------------------------------------------------|
| `Solar Wind Termination Shock` | `Sun: Termination Shock` -- **rename** |
| `Solar Wind Heliopause` | `Sun: Heliopause` -- **rename** |
| `Inner Limit of Oort Cloud` | `Sun: Inner Limit of Oort Cloud` -- **prefix added** |
| `Inner Oort Cloud` | `Sun: Inner Oort Cloud` -- **prefix added** |
| `Outer Oort Cloud` | `Sun: Outer Oort Cloud` -- **prefix added** |
| `Sun's Gravitational Influence` | `Sun: Gravitational Influence` -- **possessive removed** |

Three options:

**Option A: Accept legend-name normalization at eventual switchover.**
Write the configs now with the clean `'name'` field. Source trace
names continue unchanged in D1 (because D1 doesn't activate the
configs). At switchover (D2 or successor), the 6 legend entries
change to the unified `"Sun: <X>"` pattern. Cost: a one-time legend
rename visible to users at switchover. Benefit: zero rendering-layer
changes; D1 stays additive.

**Option B: Add a `name_override` config field to
`build_sphere_shell()`.** Expand D1 scope to 3 files. If
`config.get('name_override')` is set, use it directly instead of
`"<body>: <config_name>"`. Preserves exact legend names. Cost: scope
creep, behavior change in shared rendering helper. Benefit: no
visible legend changes at switchover.

**Option C: Defer this decision.** Write Sun configs with the clean
`'name'` field (same content as Option A) AND add a TODO comment
flagging that switchover will change 6 legend entries. Surface for
Mode 5 review when the switchover phase happens.

**Recommendation: Option A.** The legend rename is editorial, not
visual. The new names are arguably more consistent: every body's
shells follow `"<Body>: <Shell>"`. The current source names are
inconsistent within the Sun module itself. D1 stays purely
mechanical, single file pair, no rendering-layer scope creep.

**Tony's call needed before manifest execution.** If Tony picks A,
proceed to 3.1 with clean `'name'` values. If B, the manifest
expands to include `orrery_rendering.py` edits (signature already
sketched at line 101). If C, proceed as in A but document the
TODOs in handoff for D2.

The remainder of this section assumes Option A.


### 3.1 Sun sphere config inventory (all 15)

Extracted from source via AST. Each row is the complete config dict
for that shell. All values verified against
`/mnt/project/solar_visualization_shells.py`. All trace names per
Option A (legend names normalize to `"Sun: <name>"` at switchover).

| Config key | `'name'` | `radius_au` formula | n_points | color | marker_size | opacity | hover_text source | tooltip source |
|------------|----------|---------------------|---------:|-------|------------:|--------:|-------------------|----------------|
| `core` | `Core` | `CORE_AU` | 25 | `rgb(70, 130, 180)` | 10 | 1.0 | `core_info_hover` | `core_info` |
| `radiative` | `Radiative Zone` | `RADIATIVE_ZONE_AU` | 25 | `rgb(30, 144, 255)` | 7 | 1.0 | `radiative_zone_info_hover` | `radiative_zone_info` |
| `photosphere` | `Photosphere` | `SOLAR_RADIUS_AU` | 25 | `rgb(255, 244, 214)` | 7.0 | 1.0 | `photosphere_info_hover` | `photosphere_info` |
| `chromosphere` | `Chromosphere` | `CHROMOSPHERE_RADII * SOLAR_RADIUS_AU` | 25 | `rgb(30, 144, 255)` | 3.0 | 0.5 | `chromosphere_info_hover` | `chromosphere_info` |
| `inner_corona` | `Inner Corona` | `INNER_CORONA_RADII * SOLAR_RADIUS_AU` | 20 | `rgb(0, 0, 255)` | 3.0 | 0.45 | `inner_corona_info_hover` | `inner_corona_info` |
| `streamer_belt` | `Streamer Belt (Visible Corona)` | `STREAMER_BELT_RADII * SOLAR_RADIUS_AU` | 20 | `rgb(255, 200, 80)` | 3.0 | 0.45 | `streamer_belt_info_hover` | `streamer_belt_info` |
| `roche_limit` | `Roche Limit (Comets)` | `ROCHE_LIMIT_RADII * SOLAR_RADIUS_AU` | 20 | `rgb(200, 60, 60)` | 3.0 | 0.5 | `roche_limit_info_hover` | `roche_limit_info` |
| `alfven_surface` | `Alfven Surface` | `ALFVEN_SURFACE_RADII * SOLAR_RADIUS_AU` | 20 | `rgb(0, 200, 200)` | 3.5 | 0.35 | `alfven_surface_info_hover` | `alfven_surface_info` |
| `outer_corona` | `Outer Corona` | `OUTER_CORONA_RADII * SOLAR_RADIUS_AU` | 20 | `rgb(25, 25, 112)` | 3.5 | 0.5 | `outer_corona_info_hover` | `outer_corona_info` |
| `termination_shock` | `Termination Shock` | `TERMINATION_SHOCK_AU` | 20 | `rgb(240, 244, 255)` | 3.0 | 0.4 | `termination_shock_info_hover` | `termination_shock_info` |
| `heliopause` | `Heliopause` | `HELIOPAUSE_RADII * SOLAR_RADIUS_AU` | 20 | `rgb(135, 206, 250)` | 3.0 | 0.4 | `solar_wind_info_hover` | `solar_wind_info` |
| `inner_oort_limit` | `Inner Limit of Oort Cloud` | `INNER_LIMIT_OORT_CLOUD_AU` | 20 | `white` | 3.0 | 0.35 | `inner_limit_oort_info_hover` | `inner_limit_oort_info` |
| `inner_oort` | `Inner Oort Cloud` | `INNER_OORT_CLOUD_AU` | 20 | `white` | 3.0 | 0.35 | `inner_oort_info_hover` | `inner_oort_info` |
| `outer_oort` | `Outer Oort Cloud` | `OUTER_OORT_CLOUD_AU` | 20 | `white` | 3.0 | 0.3 | `outer_oort_info_hover` | `outer_oort_info` |
| `gravitational` | `Gravitational Influence` | `GRAVITATIONAL_INFLUENCE_AU` | 20 | `rgb(102, 187, 106)` | 3.0 | 0.3 | `gravitational_influence_info_hover` | `gravitational_influence_info` |

**Notes on this table:**

- `radius_au` is the numeric value at runtime (`CORE_AU` evaluates to
  `0.2 * SOLAR_RADIUS_AU`). The auto-gen script (3.2) writes these as
  expressions referencing the imported constants.
- `chromosphere` and `inner_corona` happen to share color
  `rgb(30, 144, 255)` -- not a bug; verified in source.
- Three Oort shells use bare `'white'` (not `rgb(...)`) -- verified.
- `inner_oort_limit` SHELL_CONFIGS key matches the `sun_shell_vars`
  key (`'inner_oort_limit'`). Info strings are named
  `inner_limit_oort_info*` (order swapped) -- the manifest preserves
  this asymmetry.
- `heliopause` SHELL_CONFIGS key matches the `sun_shell_vars` key
  (`'heliopause'`). Info strings are named `solar_wind_info*`
  (legacy naming, used by the heliopause shell since its early days
  when it was conceptually labeled "Solar Wind Heliopause").
- `gravitational` (NOT `gravitational_influence`) matches the
  `sun_shell_vars` key. Display name is `Gravitational Influence`.


### 3.2 Auto-generation script for Sun sphere configs

Save as `generate_phase_d1_sun_configs.py`. The script reuses the
AST-walking pattern from C4 with Sun-specific adaptations:

- Uses `radius_au` (not `radius_fraction`); reads the radius argument
  from `create_sphere_points()` as a raw expression string.
- No `mesh3d` shells (Sun has no cloud layer).
- Maps source trace names to clean config names per Option A
  (`"Sun: <X>"` -> `"<X>"`; non-conforming names get editorial cleanup).

```python
# generate_phase_d1_sun_configs.py
"""Auto-generate Sun sphere config block for Phase D1 shell_configs.py.

Parses solar_visualization_shells.py via AST to extract each sphere
builder's radius expression, n_points, color, marker_size, and
opacity. Emits a SHELL_CONFIGS['Sun'] block.

Trace names follow Option A: clean 'name' values (the part after
'Sun: ' for prefixed shells; editorial cleanup for the 6 non-prefixed).
"""
import ast
import sys

BODY = 'Sun'
PATH = 'solar_visualization_shells.py'

# (shell_key, builder_function, hover_text_var, tooltip_var, clean_name)
SHELLS = [
    ('core',              'create_sun_core_shell',              'core_info_hover',                  'core_info',                  'Core'),
    ('radiative',         'create_sun_radiative_shell',         'radiative_zone_info_hover',        'radiative_zone_info',        'Radiative Zone'),
    ('photosphere',       'create_sun_photosphere_shell',       'photosphere_info_hover',           'photosphere_info',           'Photosphere'),
    ('chromosphere',      'create_sun_chromosphere_shell',      'chromosphere_info_hover',          'chromosphere_info',          'Chromosphere'),
    ('inner_corona',      'create_sun_inner_corona_shell',      'inner_corona_info_hover',          'inner_corona_info',          'Inner Corona'),
    ('streamer_belt',     'create_sun_streamer_belt_shell',     'streamer_belt_info_hover',         'streamer_belt_info',         'Streamer Belt (Visible Corona)'),
    ('roche_limit',       'create_sun_roche_limit_shell',       'roche_limit_info_hover',           'roche_limit_info',           'Roche Limit (Comets)'),
    ('alfven_surface',    'create_sun_alfven_surface_shell',    'alfven_surface_info_hover',        'alfven_surface_info',        'Alfven Surface'),
    ('outer_corona',      'create_sun_outer_corona_shell',      'outer_corona_info_hover',          'outer_corona_info',          'Outer Corona'),
    ('termination_shock', 'create_sun_termination_shock_shell', 'termination_shock_info_hover',     'termination_shock_info',     'Termination Shock'),
    ('heliopause',        'create_sun_heliopause_shell',        'solar_wind_info_hover',            'solar_wind_info',            'Heliopause'),
    ('inner_oort_limit',  'create_sun_inner_oort_limit_shell',  'inner_limit_oort_info_hover',      'inner_limit_oort_info',      'Inner Limit of Oort Cloud'),
    ('inner_oort',        'create_sun_inner_oort_shell',        'inner_oort_info_hover',            'inner_oort_info',            'Inner Oort Cloud'),
    ('outer_oort',        'create_sun_outer_oort_shell',        'outer_oort_info_hover',            'outer_oort_info',            'Outer Oort Cloud'),
    ('gravitational',     'create_sun_gravitational_shell',     'gravitational_influence_info_hover','gravitational_influence_info','Gravitational Influence'),
]

def get_func(tree, name):
    for n in tree.body:
        if isinstance(n, ast.FunctionDef) and n.name == name:
            return n
    raise KeyError(name)

def extract(func):
    """Returns (radius_expr_str, n_points, color, marker_size, opacity)."""
    radius_expr = n_points = color = size = opacity = None
    # First Scatter3d call -> the geometry trace
    for node in ast.walk(func):
        if isinstance(node, ast.Call):
            f = node.func
            if isinstance(f, ast.Name) and f.id == 'create_sphere_points':
                if node.args:
                    radius_expr = ast.unparse(node.args[0])
                for kw in node.keywords:
                    if kw.arg == 'n_points' and isinstance(kw.value, ast.Constant):
                        n_points = kw.value.value
    seen_scatter = False
    for node in ast.walk(func):
        if isinstance(node, ast.Call):
            f = node.func
            if isinstance(f, ast.Attribute) and f.attr == 'Scatter3d' and not seen_scatter:
                seen_scatter = True
                for kw in node.keywords:
                    if kw.arg == 'marker' and isinstance(kw.value, ast.Call):
                        for mk in kw.value.keywords:
                            if mk.arg == 'size' and isinstance(mk.value, ast.Constant):
                                size = mk.value.value
                            if mk.arg == 'color' and isinstance(mk.value, ast.Constant):
                                color = mk.value.value
                            if mk.arg == 'opacity' and isinstance(mk.value, ast.Constant):
                                opacity = mk.value.value
                break
    return radius_expr, n_points, color, size, opacity

def emit_block():
    src = open(PATH, 'rb').read().decode('utf-8')
    tree = ast.parse(src)

    print("    'Sun': {")
    print()
    for key, fname, hover_var, tooltip_var, clean_name in SHELLS:
        try:
            func = get_func(tree, fname)
        except KeyError:
            print("        # %s: FUNCTION NOT FOUND" % key, file=sys.stderr)
            continue
        radius_expr, n_points, color, size, opacity = extract(func)

        print("        '%s': {" % key)
        print("            'name': %r," % clean_name)
        print("            'radius_au': %s," % radius_expr)
        print("            'color': %r," % color)
        print("            'opacity': %r," % opacity)
        print("            'n_points': %d," % n_points)
        print("            'marker_size': %r," % size)
        print("            'hover_text': %s," % hover_var)
        print("            'tooltip': %s," % tooltip_var)
        print("        },")
        print()
    print("    },")

if __name__ == '__main__':
    emit_block()
```

Usage:

```bash
python3 generate_phase_d1_sun_configs.py > sun_block.txt
# Inspect sun_block.txt against the table in 3.1.
# The script emits expression references for radius_au (e.g.
# CORE_AU, CHROMOSPHERE_RADII * SOLAR_RADIUS_AU) -- these must
# resolve against shell_configs.py's existing imports.
```

The output is the source of truth. The 3.1 table is for human
cross-reference; the script's output wins if they disagree.

### 3.3 Imports to add at the top of `shell_configs.py`

`shell_configs.py` already imports many hover/tooltip symbols from
body modules (C4 added Saturn/Uranus/Neptune). Add Sun symbols:

```python
from solar_visualization_shells import (
    # hover_text (Plotly hover, <br> line breaks)
    core_info_hover, radiative_zone_info_hover,
    photosphere_info_hover, chromosphere_info_hover,
    inner_corona_info_hover, streamer_belt_info_hover,
    roche_limit_info_hover, alfven_surface_info_hover,
    outer_corona_info_hover, termination_shock_info_hover,
    solar_wind_info_hover,                      # heliopause hover (legacy name)
    inner_limit_oort_info_hover,                # inner_oort_limit hover (swapped naming)
    inner_oort_info_hover, outer_oort_info_hover,
    gravitational_influence_info_hover,
    # tooltip (Tk GUI, \n line breaks)
    core_info, radiative_zone_info, photosphere_info, chromosphere_info,
    inner_corona_info, streamer_belt_info, roche_limit_info, alfven_surface_info,
    outer_corona_info, termination_shock_info,
    solar_wind_info,                            # heliopause tooltip (legacy name)
    inner_limit_oort_info,                      # inner_oort_limit tooltip (swapped naming)
    inner_oort_info, outer_oort_info,
    gravitational_influence_info,
)
```

The constants `CORE_AU`, `RADIATIVE_ZONE_AU`, `SOLAR_RADIUS_AU`,
`CHROMOSPHERE_RADII`, etc. used in `radius_au` expressions must
also be importable. They live in `constants_new.py` and are
re-exported via `planet_visualization_utilities.py`. Add (or extend
the existing import in `shell_configs.py`):

```python
from planet_visualization_utilities import (
    SOLAR_RADIUS_AU, CORE_AU, RADIATIVE_ZONE_AU,
    CHROMOSPHERE_RADII, INNER_CORONA_RADII, OUTER_CORONA_RADII,
    STREAMER_BELT_RADII, ROCHE_LIMIT_RADII, ALFVEN_SURFACE_RADII,
    TERMINATION_SHOCK_AU, HELIOPAUSE_RADII,
    INNER_LIMIT_OORT_CLOUD_AU, INNER_OORT_CLOUD_AU, OUTER_OORT_CLOUD_AU,
    GRAVITATIONAL_INFLUENCE_AU,
)
```

If `shell_configs.py` already imports any of these symbols, deduplicate
rather than re-import. Run a quick grep before adding:

```bash
grep -n "^from planet_visualization_utilities\|^from solar_visualization_shells" /mnt/project/shell_configs.py
```

### 3.4 Insertion point in `shell_configs.py`

Insert the `'Sun': { ... }` block immediately after the last existing
body in `SHELL_CONFIGS` (which is Neptune from C4). Find the closing
brace of `'Neptune': {...}` and place the new block before the
top-level closing brace of `SHELL_CONFIGS = {...}`.

```bash
# Find the line: '},  # closes Neptune' or similar, just before SHELL_CONFIGS close
grep -n "^SHELL_CONFIGS\s*=\|^CUSTOM_SHELLS\s*=" /mnt/project/shell_configs.py
```

Use `str_replace` on the last `},` before the `CUSTOM_SHELLS = {`
definition. The new block is added as a peer to `'Neptune'`.


---

## 4. Sun CUSTOM_SHELLS Entry

Three custom geometry shells: `hills_cloud_torus`, `outer_oort_clumpy`,
`galactic_tide`. Schema matches Jupiter (`shell_configs.py:1775+`):
`'builder'` = single string `module.function`, `'tooltip'` = inline
string. NO `'hover_text'` field -- Plotly hover text lives inside the
builder functions (`hills_hover`, `clumpy_hover`, `tide_hover`).

### 4.1 Custom entries

```python
    'Sun': {

        'hills_cloud_torus': {
            'builder': 'solar_visualization_shells.create_sun_hills_cloud_torus',
            'tooltip': (
                "SET MANUAL SCALE TO AT LEAST 0.02 AU TO VISUALIZE.\n\n"
                "The Hills Cloud is the inner Oort Cloud region, more tightly\n"
                "gravitationally bound to the Sun than the outer spherical Oort\n"
                "Cloud. Modeled here as a toroidal (disk-like) structure shaped\n"
                "by galactic tidal forces, extending from approximately 2,000\n"
                "to 20,000 AU.\n\n"
                "Short-period comets (Halley-type, period < 200 years) are\n"
                "thought to originate predominantly from this region.\n\n"
                "Source: Hills (1981) AJ; Levison & Dones (2014) review."
            ),
        },

        'outer_oort_clumpy': {
            'builder': 'solar_visualization_shells.create_sun_outer_oort_clumpy',
            'tooltip': (
                "SET MANUAL SCALE TO AT LEAST 0.10 AU TO VISUALIZE.\n\n"
                "The Outer Oort Cloud is the spherical reservoir of long-period\n"
                "comets extending from ~20,000 AU to ~100,000 AU. This rendering\n"
                "models the cloud's clumpy, asymmetric structure -- comets are\n"
                "not uniformly distributed but clustered in gravitationally\n"
                "perturbed groups influenced by passing stars and galactic\n"
                "tides over the Sun's 4.6-billion-year history.\n\n"
                "Long-period comets (period > 200 years) originate here.\n\n"
                "Source: Oort (1950) BAN; Dones et al. (2004) review."
            ),
        },

        'galactic_tide': {
            'builder': 'solar_visualization_shells.create_sun_galactic_tide',
            'tooltip': (
                "SET MANUAL SCALE TO AT LEAST 0.05 AU TO VISUALIZE.\n\n"
                "Region where the Milky Way's gravitational tide influences\n"
                "Oort Cloud objects. Tidal forces from the galactic disk cause\n"
                "Oort comets to avoid the galactic plane, producing an\n"
                "asymmetric distribution centered at ~50,000 AU.\n\n"
                "Galactic tides are the dominant mechanism injecting\n"
                "long-period comets into the inner solar system.\n\n"
                "Source: Heisler & Tremaine (1986) Icarus."
            ),
        },

    },
```

**Editorial tooltip note:** the inline tooltip strings above are
COMPOSED for D1. They are recalled-not-fetched content per the
fetched-vs-recalled rule. Queue Mode 7/Gemini verification (deferred
item 26) before render. The text aims to match the existing
description style from C4 (Saturn/Uranus/Neptune tooltips) and the
inline `hills_hover` / `clumpy_hover` / `tide_hover` text inside
the source functions. If Tony prefers to use the module-level
`hills_cloud_torus_info`, `outer_oort_clumpy_info`, and
`galactic_tide_info` strings verbatim (defined at lines 107, 132,
157 of `solar_visualization_shells.py`), that is a one-edit swap.

### 4.2 Insertion point in `shell_configs.py`

Insert immediately after `'Neptune': {...}` block in the
`CUSTOM_SHELLS` dictionary (the second top-level dict in the file).
Find the closing brace of Neptune's CUSTOM_SHELLS block.

```bash
grep -n "^CUSTOM_SHELLS\s*=" /mnt/project/shell_configs.py
# Expected: 1619 (per pre-D1 snapshot; will shift after Section 3 insert).
```

Use `str_replace` on the last `},` before the file-level closing brace
of `CUSTOM_SHELLS`. The new `'Sun': { ... }` block is added as a peer
to `'Neptune'`.


---

## 5. Dead Code Cleanup in `solar_visualization_shells.py`

Six items to strip. All verified via `grep -rn` to confirm no callers
outside the file or only-dead callers within it.

### 5.1 Strip order (bottom-up to preserve line numbers above)

Strip in DECREASING line-number order:

**(a) `enhanced_oort_hover_text` string constant (lines 1736-1759)**

24 lines. Defined but never imported or referenced outside its own
definition. Use `str_replace` on the `enhanced_oort_hover_text = """`
opening triple-quote down through the closing `"""`.

**(b) `create_oort_cloud_density_visualization()` (lines 1682-1731)**

50 lines. Never called. Strip the entire function definition.

**(c) `create_enhanced_oort_cloud_visualization()` (lines 1617-1680)**

64 lines. Never called. Also note: this function attempts to unpack
`x, y, z` from `create_sun_hills_cloud_torus()`, `create_sun_outer_oort_clumpy()`,
and `create_sun_galactic_tide()` -- but those builders return
`[shell_trace, info_trace]` (lists of plotly traces, not coordinate
tuples). It would raise `ValueError` if called. Double-dead.

**(d) Duplicate import block (lines 1430-1431)**

```python
import plotly.graph_objs as go
from planet_visualization_utilities import create_sphere_points, SOLAR_RADIUS_AU
```

These are already imported at lines 18 (`import plotly.graph_objs as go`)
and 21 (`create_sphere_points`, `SOLAR_RADIUS_AU`). Strip these two
lines plus any blank line padding around them. Leaves the section
comment at 1422-1428 intact.

**(e) `create_corona_sphere()` (lines 932-942)**

11 lines (plus the preceding comment at line 931 `# In the
create_corona_sphere function, increase the number of points`).
12 lines total to strip. Never called. Note: this defines a sphere
helper that returns flat arrays -- pre-`create_sphere_points`
ancestor. Made redundant when `create_sphere_points` was promoted
to `planet_visualization_utilities.py`.

**(f) `create_sun_hover_text()` (lines 895-929)**

35 lines. Returns a dict of hover strings. The dict's content
duplicates information that is now in the `*_info_hover` strings.
Never called from anywhere. Strip.

### 5.2 Imports check after dead-code strip

After steps (b) and (c), check whether any imports used only by
those functions become unused. Run:

```bash
python3 -c "
import ast
src = open('solar_visualization_shells.py', 'rb').read().decode('utf-8')
tree = ast.parse(src)
imports = set()
for n in tree.body:
    if isinstance(n, ast.ImportFrom):
        for alias in n.names:
            imports.add(alias.asname or alias.name)
    elif isinstance(n, ast.Import):
        for alias in n.names:
            imports.add(alias.asname or alias.name.split('.')[0])
# Find each import's usage count in the post-strip body
import re
body_text = src
unused = []
for name in imports:
    # Crude but adequate -- count occurrences outside the import statement line
    if body_text.count(name) <= 1:
        unused.append(name)
print('Possibly-unused imports:', unused)
"
```

This is a check, not an instruction to strip. Removing imports that
become unused after the dead-code strip is fine; if anything looks
ambiguous, leave it (Phase D3 import cleanup catches everything).

### 5.3 Lines saved

Approximately:
- (a) 24 lines
- (b) 50 lines
- (c) 64 lines (plus its module-level `import` lines if any are
  duplicated -- check during edit)
- (d) 2 lines (+ adjacent blank line padding)
- (e) 12 lines (function + preceding comment)
- (f) 35 lines

**Total: ~187 lines stripped.** File shrinks from 1,759 to ~1,572 (plus
the 4 lines added in Section 6).

---

## 6. Custom Function `center_position` Parameter

### 6.1 Rationale

The unified dispatch invokes custom builders as `builder(center_position)`
(`planet_visualization.py:609`). The three Sun custom functions currently
have signatures:

```python
def create_sun_hills_cloud_torus(inner_radius=2000, outer_radius=20000, thickness_ratio=0.3)
def create_sun_outer_oort_clumpy(radius_min=20000, radius_max=100000, n_clumps=15)
def create_sun_galactic_tide(radius=50000, n_points=2000)
```

Without a `center_position` first parameter, the eventual switchover
phase will pass a position tuple as `inner_radius` / `radius_min` /
`radius`, crashing or rendering garbage.

Add `center_position=(0,0,0)` as the FIRST parameter to all three. The
default value `(0,0,0)` preserves current behavior for the three
existing no-arg callers in `create_sun_visualization()`
(`planet_visualization.py` lines 322, 325, 328). Grep confirms no
positional-arg callers exist anywhere in the codebase.

### 6.2 Three signature edits

Use `str_replace` (one per function), bottom-up:

**(a) `create_sun_galactic_tide` (line 1566)**

```python
# Before
def create_sun_galactic_tide(radius=50000, n_points=2000):

# After
def create_sun_galactic_tide(center_position=(0, 0, 0), radius=50000, n_points=2000):
```

**(b) `create_sun_outer_oort_clumpy` (line 1496)**

```python
# Before
def create_sun_outer_oort_clumpy(radius_min=20000, radius_max=100000, n_clumps=15):

# After
def create_sun_outer_oort_clumpy(center_position=(0, 0, 0), radius_min=20000, radius_max=100000, n_clumps=15):
```

**(c) `create_sun_hills_cloud_torus` (line 1433)**

```python
# Before
def create_sun_hills_cloud_torus(inner_radius=2000, outer_radius=20000, thickness_ratio=0.3):

# After
def create_sun_hills_cloud_torus(center_position=(0, 0, 0), inner_radius=2000, outer_radius=20000, thickness_ratio=0.3):
```

### 6.3 Body-of-function NOT modified

The parameter is accepted but NOT yet used inside the function body.
The three functions continue to generate geometry at the origin. This
is intentional:

- D1 is extraction only -- no behavior change.
- The eventual switchover phase wires `sun_position` through the
  dispatch and inside the function bodies, translating geometry by
  `center_position` and using `sun_position` where relevant (none
  of the three current functions need solar direction; the Sun
  doesn't point at itself).

Add a `# Phase D1: center_position accepted for interface uniformity;`
`# geometry translation deferred to switchover phase.` comment inside
each function body just below the signature, for breadcrumb purposes.

### 6.4 Docstring update

In each of the three docstrings, add a parameter line documenting
`center_position`:

```python
    Parameters:
    - center_position: Sun position tuple (default: (0, 0, 0)).
      Accepted for interface uniformity with the unified dispatch
      contract. Geometry is currently generated at the origin
      regardless; translation deferred to switchover phase.
    - inner_radius: ...  (existing parameter)
    - ...
```


---

## 7. Verification

### 7.1 Post-edit smoke tests

```bash
python3 -c "
from shell_configs import SHELL_CONFIGS, CUSTOM_SHELLS

# Sun in both registries
assert 'Sun' in SHELL_CONFIGS, 'Sun missing from SHELL_CONFIGS'
assert 'Sun' in CUSTOM_SHELLS, 'Sun missing from CUSTOM_SHELLS'

# 15 sphere shells
expected_sphere = {
    'core', 'radiative', 'photosphere', 'chromosphere', 'inner_corona',
    'streamer_belt', 'roche_limit', 'alfven_surface', 'outer_corona',
    'termination_shock', 'heliopause', 'inner_oort_limit', 'inner_oort',
    'outer_oort', 'gravitational',
}
actual_sphere = set(SHELL_CONFIGS['Sun'].keys())
missing = expected_sphere - actual_sphere
extra = actual_sphere - expected_sphere
assert not missing, 'Missing sphere shells: %s' % missing
assert not extra, 'Unexpected sphere shells: %s' % extra
print('Sun: 15 sphere shells. PASS')

# 3 custom entries
expected_custom = {'hills_cloud_torus', 'outer_oort_clumpy', 'galactic_tide'}
assert set(CUSTOM_SHELLS['Sun'].keys()) == expected_custom
print('Sun: 3 custom entries. PASS')

# Field presence in sphere configs
required_fields = {'name', 'radius_au', 'color', 'opacity', 'n_points',
                   'marker_size', 'hover_text', 'tooltip'}
for shell_name, cfg in SHELL_CONFIGS['Sun'].items():
    missing = required_fields - set(cfg.keys())
    assert not missing, 'Sun/%s missing fields: %s' % (shell_name, missing)
print('All Sun sphere shells have required fields. PASS')

# Custom entry shape (no hover_text, has builder + tooltip)
for shell_name, cfg in CUSTOM_SHELLS['Sun'].items():
    assert 'builder' in cfg, 'Sun/%s missing builder' % shell_name
    assert 'tooltip' in cfg, 'Sun/%s missing tooltip' % shell_name
    assert 'hover_text' not in cfg, 'Sun/%s has unexpected hover_text field' % shell_name
print('Sun custom entries match Jupiter schema. PASS')
"
```

### 7.2 Render parity (configs registered but unused)

The dispatch contract for `radius_au` is exercised; verify
`build_sphere_shell` produces 2 traces for each Sun sphere config:

```bash
python3 -c "
from shell_configs import SHELL_CONFIGS
from orrery_rendering import build_sphere_shell

for shell_name, cfg in SHELL_CONFIGS['Sun'].items():
    traces = build_sphere_shell(cfg, 'Sun', (0, 0, 0))
    assert len(traces) == 2, 'Sun/%s: expected 2 traces, got %d' % (
        shell_name, len(traces))
    # Trace name should be 'Sun: <config_name>'
    expected_prefix = 'Sun: '
    assert traces[0].name.startswith(expected_prefix), (
        'Sun/%s: trace name %r does not start with %r' % (
            shell_name, traces[0].name, expected_prefix))
print('All 15 Sun sphere builders produce 2 traces. PASS')
"
```

### 7.3 Custom function signatures

```bash
python3 -c "
import inspect
import solar_visualization_shells as m

for fname in ('create_sun_hills_cloud_torus',
              'create_sun_outer_oort_clumpy',
              'create_sun_galactic_tide'):
    sig = inspect.signature(getattr(m, fname))
    params = list(sig.parameters.values())
    assert params[0].name == 'center_position', (
        '%s: first param is %r, expected center_position' % (
            fname, params[0].name))
    assert params[0].default == (0, 0, 0), (
        '%s: center_position default is %r, expected (0, 0, 0)' % (
            fname, params[0].default))
    # Function still callable with no args (default value works)
    traces = getattr(m, fname)()
    assert len(traces) == 2, '%s: expected 2 traces, got %d' % (fname, len(traces))
    # And callable with center_position arg
    traces = getattr(m, fname)((1.0, 0.0, 0.0))
    assert len(traces) == 2, '%s with center_position: expected 2 traces' % fname
print('All 3 custom functions accept center_position. PASS')
"
```

Note: the second call (with `(1.0, 0.0, 0.0)`) passes a non-origin
position. Geometry will still generate at origin (Section 6.3) -- the
test only verifies the parameter is ACCEPTED, not used.

### 7.4 Dead code stripped

```bash
python3 -c "
import solar_visualization_shells as m
dead = ['create_corona_sphere', 'create_sun_hover_text',
        'create_enhanced_oort_cloud_visualization',
        'create_oort_cloud_density_visualization',
        'enhanced_oort_hover_text']
for d in dead:
    assert not hasattr(m, d), 'Dead item still present: %s' % d
print('All 5 dead items stripped. PASS')
"
```

### 7.5 Existing `create_sun_visualization()` still works

```bash
python3 -c "
from planet_visualization import create_sun_visualization
import plotly.graph_objects as go

# Mock shell_vars with all-off so we don't actually render the Sun
class MockVar:
    def get(self): return 0

shell_vars = {
    'core': MockVar(), 'radiative': MockVar(), 'photosphere': MockVar(),
    'chromosphere': MockVar(), 'inner_corona': MockVar(),
    'streamer_belt': MockVar(), 'roche_limit': MockVar(),
    'alfven_surface': MockVar(), 'outer_corona': MockVar(),
    'termination_shock': MockVar(), 'heliopause': MockVar(),
    'inner_oort_limit': MockVar(), 'inner_oort': MockVar(),
    'outer_oort': MockVar(), 'gravitational': MockVar(),
    'hills_cloud_torus': MockVar(), 'outer_oort_clumpy': MockVar(),
    'galactic_tide': MockVar(),
    'main_belt': MockVar(), 'hildas': MockVar(),
    'trojans_greeks': MockVar(), 'trojans_trojans': MockVar(),
    'corona_from_distance': MockVar(),
}
fig = go.Figure()
result = create_sun_visualization(fig, shell_vars)
assert result is not None
print('create_sun_visualization() still callable. PASS')
"
```

### 7.6 Pre-D1 + D1 totals

```bash
python3 -c "
from shell_configs import SHELL_CONFIGS, CUSTOM_SHELLS

# 13 bodies in SHELL_CONFIGS (12 from C4 + Sun)
assert len(SHELL_CONFIGS) == 13, 'Expected 13 bodies, got %d' % len(SHELL_CONFIGS)
print('SHELL_CONFIGS bodies: %d (expected 13)' % len(SHELL_CONFIGS))

# 83 sphere shell configs (68 from C4 + 15 from D1)
total_sphere = sum(len(v) for v in SHELL_CONFIGS.values())
assert total_sphere == 83, 'Expected 83 sphere configs, got %d' % total_sphere
print('Total sphere configs: %d (expected 83)' % total_sphere)

# 9 bodies in CUSTOM_SHELLS (8 from C4 + Sun)
assert len(CUSTOM_SHELLS) == 9, 'Expected 9 custom bodies, got %d' % len(CUSTOM_SHELLS)
print('CUSTOM_SHELLS bodies: %d (expected 9)' % len(CUSTOM_SHELLS))

# 24 custom entries (21 from C4 + 3 from D1)
total_custom = sum(len(v) for v in CUSTOM_SHELLS.values())
assert total_custom == 24, 'Expected 24 custom entries, got %d' % total_custom
print('Total custom entries: %d (expected 24)' % total_custom)
"
```

### 7.7 LF / ASCII

```bash
for f in shell_configs.py solar_visualization_shells.py; do
    if grep -lU $'\r' "$f"; then
        echo "FAIL: $f has CRLF"
        exit 1
    fi
    if ! file "$f" | grep -q "ASCII"; then
        echo "FAIL: $f is not ASCII"
        exit 1
    fi
done
echo "LF / ASCII: PASS"
```

### 7.8 Run provenance scanner

```bash
python3 provenance_scanner.py
```

Expected: 0 Tier-1 findings on the 2 touched files. Existing Tier-2
residuals accepted.

### 7.9 GUI smoke test (Tony)

Launch `palomas_orrery_dashboard.py` and confirm:
- GUI opens without errors
- Sun checkboxes (15 sphere + 3 custom + asteroid belt + corona_from_distance)
  appear unchanged
- Toggle each Sun shell on individually and verify it renders the
  same as pre-D1 (no behavior change -- the new configs are dormant)

D1 is registration-only. If anything looks different from pre-D1
renders, STOP and report -- something accidentally activated the
unified dispatch path.

---

## 8. Decision Log and Open Items

### 8.1 Decisions made during this manifest authoring

| # | Decision | Source |
|---|----------|--------|
| 1 | Two-file scope, no call site or dispatch changes | D1 prompt + review reply |
| 2 | Use `'hover_text'` and `'tooltip'` config field names (NOT `'info_string'`) | Reply correction 1 |
| 3 | Heliopause hover/tooltip sourced from `solar_wind_info_hover` / `solar_wind_info` (legacy naming) | Reply correction 2 |
| 4 | SHELL_CONFIGS key for gravitational shell is `'gravitational'`, display name is `'Gravitational Influence'` | Reply correction 3 |
| 5 | `inner_oort_limit` key with `inner_limit_oort_info*` strings (swapped naming preserved) | Reply correction 3 |
| 6 | CUSTOM_SHELLS Sun entries use inline `'tooltip'` strings (Jupiter pattern), no `'hover_text'` field | Reply clarification A |
| 7 | Custom function `center_position` added as MANDATORY change, not recommendation | Reply clarification D |
| 8 | Dead code strip includes `create_corona_sphere` and `create_sun_hover_text` (originally Q2 candidates), `create_enhanced_oort_cloud_visualization` and `create_oort_cloud_density_visualization` (double-dead -- would crash if called), `enhanced_oort_hover_text` string, and duplicate import block | Prompt Q2 + clarification C |
| 9 | Item 26 (CUSTOM_SHELLS tooltip Mode 7 verification) deferred to D3 | Reply sidebar |
| 10 | **Legend names normalize to `"Sun: <X>"` at switchover (Option A in Section 3.0)** | NEW -- surfaced during manifest drafting |
| 11 | Custom function `center_position` ACCEPTED but NOT yet used inside function bodies (geometry stays at origin in D1) | Section 6.3 |
| 12 | CUSTOM_SHELLS Sun tooltip text COMPOSED (recalled-not-fetched). Inline strings written; Mode 7 verification queued | Section 4.1 + item 26 |

### 8.2 OPEN QUESTION (requires Tony decision before execution)

**The legend-name policy decision (Section 3.0).** Three options:

- **Option A:** Accept legend rename at switchover. Configs use clean
  `'name'` values now. 6 legend entries change at switchover.
  Recommended by manifest author.
- **Option B:** Add `name_override` field to `build_sphere_shell`.
  Preserves exact legend names. Expands D1 scope to 3 files
  (`orrery_rendering.py`).
- **Option C:** Defer the decision. Use Option A internally, document
  TODOs for D2 to revisit.

The manifest assumes Option A throughout. If Tony picks B or C, the
manifest needs the following updates:

- **Option B:** add Section 3.5 with `build_sphere_shell` edits;
  add `name_override` field to each non-conforming SHELL_CONFIGS
  entry in Section 3.1 table; update 3.2 auto-gen script.
- **Option C:** add TODO comments in the 6 affected entries; add a
  Section 8.3 deferred item.

### 8.3 Items deferred to D2 / D3 / later

These are noted, not opened:

1. **D2:** Replace `create_sun_visualization()` call sites in
   `palomas_orrery.py` (lines 4508-4509, 6148-6149). After this,
   the registered Sun configs activate and `create_sun_visualization()`
   can be retired.
2. **D2:** Wire `sun_position` from ephemeris into custom Sun
   builders. Inside `create_sun_hills_cloud_torus` /
   `create_sun_outer_oort_clumpy` / `create_sun_galactic_tide`,
   apply `center_position` to translate generated geometry. (D1
   accepts the parameter; D2 wires its use.)
3. **D2 or successor:** Decide asteroid belt migration path. The
   4 belt keys (`main_belt`, `hildas`, `trojans_greeks`,
   `trojans_trojans`) currently dispatch through
   `create_sun_visualization()`. Migrate to CUSTOM_SHELLS or
   leave as a documented exception.
4. **D2 or successor:** `corona_from_distance` rendering path.
5. **D3:** `_info` import cleanup (deferred item 5 in C4 handoff).
6. **D3:** Tooltip rewiring (deferred item 7).
7. **D3:** Sun module credit-line update to reflect D1 changes.
   Currently reads "Module updated: May 2026 with Anthropic's
   Claude Opus 4.7" (from prior session); D1 will update the date
   line in the strip-and-edit pass.
8. **D3:** Mode 7 / Gemini verification of CUSTOM_SHELLS Sun
   tooltips (item 26 from C4 handoff, originally Pre-D1).
9. **Phase E:** If Option A taken, the 6 normalized legend names
   may warrant Mode 5 visual review.

---

## 9. Phase D1 Summary

### 9.1 Files modified

| File | Lines (before) | Lines (after est.) | Net | Changes |
|------|---------------:|-------------------:|----:|---------|
| `shell_configs.py` | 2,260 | ~2,650 | +390 | +Sun sphere configs (15), +Sun custom entries (3), +imports |
| `solar_visualization_shells.py` | 1,759 | ~1,576 | -183 | -187 lines dead code, +4 lines `center_position` params + breadcrumb comments |

Total: 2 files modified. Net change across both: +207 lines.

### 9.2 Post-D1 state

| Component | Value |
|-----------|------:|
| Bodies in SHELL_CONFIGS | 13 |
| Total sphere shell configs | 83 |
| Bodies in CUSTOM_SHELLS | 9 |
| Total custom entries | 24 |
| Bodies still on old dispatch | 1 (Sun -- configs registered but unused) |
| `rotate_to_sunward()` users | 8 (unchanged from C4) |
| `magnetic_tilt_deg` users | 1 (Uranus, unchanged from C4) |

### 9.3 Risk register

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| `name_override` decision (Option A/B/C) made wrong | Low | Medium (cosmetic legend rename at switchover) | Open question in Section 8.2 -- Tony decides before execution |
| Auto-gen script extracts incorrect color/size/opacity | Low | Medium (incorrect visual) | Section 3.1 table is cross-reference; verify script output matches |
| Heliopause hover/tooltip wired to wrong constant | Low | High (wrong text in tooltip) | Section 2.5 confirms `solar_wind_info_hover` exists; Section 3.1 explicitly lists it |
| Dead code strip removes something live | Low | High (function crash) | Each strip item has been grep-verified for callers; (c) is double-dead |
| Tooltip text Mode 7 verification not run | High | Medium (composed text may have factual errors) | Item 26 queued for D3; D1 doesn't render the new tooltips (configs dormant) |
| Custom builder `center_position` breaks existing callers | Low | High | Default value `(0,0,0)` preserves no-arg behavior; verified no positional callers exist |
| `shell_configs.py` import resolution fails | Low | High | Section 3.3 lists all required imports; verify against existing import block before adding |

### 9.4 Edit order within each file (canonical)

**`solar_visualization_shells.py`** (bottom-up):

1. Strip `enhanced_oort_hover_text` (1736-1759)
2. Strip `create_oort_cloud_density_visualization` (1682-1731)
3. Strip `create_enhanced_oort_cloud_visualization` (1617-1680)
4. Add `center_position=(0,0,0)` to `create_sun_galactic_tide` (line 1566), update docstring, add breadcrumb comment
5. Add `center_position=(0,0,0)` to `create_sun_outer_oort_clumpy` (line 1496), update docstring, add breadcrumb comment
6. Add `center_position=(0,0,0)` to `create_sun_hills_cloud_torus` (line 1433), update docstring, add breadcrumb comment
7. Strip duplicate import block (1430-1431)
8. Strip `create_corona_sphere` and preceding comment (931-942)
9. Strip `create_sun_hover_text` (895-929)
10. Update module docstring credit line to current date/model

**`shell_configs.py`** (insertions only, no strips):

1. Update imports at top (Section 3.3)
2. Insert `'Sun': { ... }` block at end of `SHELL_CONFIGS` (after `'Neptune'`)
3. Insert `'Sun': { ... }` block at end of `CUSTOM_SHELLS` (after `'Neptune'`)
4. Update module docstring credit line

---

## 10. Workflow Provenance

### 10.1 Authorship

- **Manifest author:** Anthropic's Claude Opus 4.7 (audit + draft)
- **Manifest input:** Tony Quintanilla + Claude Opus 4.6
  (PROMPT_shell_consolidation_D1.md, REPLY_D1_review_response.md,
  HANDOFF_shell_consolidation_phase_c4.md)
- **Source audit:** Claude Opus 4.7, reading `/mnt/project/` files at
  paths `solar_visualization_shells.py`, `shell_configs.py`,
  `planet_visualization.py`, `orrery_rendering.py`,
  `planet_visualization_utilities.py`, `constants_new.py`,
  `palomas_orrery.py`
- **Implementation:** Anthropic's Claude Opus 4.6 (in a separate
  session, executing this manifest after Tony's Option A/B/C decision)
- **Integration and verification:** Tony Quintanilla
- **Mode 7 adversarial review:** Gemini (for the 3 composed
  CUSTOM_SHELLS tooltip strings, queued via deferred item 26;
  scoped to D3)

### 10.2 Module credit line

Both touched files get:

```python
# Module updated: May 2026 with Anthropic's Claude Opus 4.7
```

Add to or update the module docstring at the top of each file.

### 10.3 Manifest version

This is the only Phase D1 manifest version. Companion documents:

- `PROMPT_shell_consolidation_D1.md` (Tony's prompt)
- `REPLY_D1_review_response.md` (Tony + Opus 4.6's reply to manifest
  author's pre-draft review)
- `HANDOFF_shell_consolidation_phase_c4.md` (immediate predecessor
  state)
- `MANIFEST_shell_consolidation_phase_d1.md` (this document)

After D1 completes, `HANDOFF_shell_consolidation_phase_d1.md` will
be authored by Opus 4.6.

### 10.4 References

- Phases A-C4: 12 bodies migrated to unified dispatch (Oct 2025 - May 18 2026)
- Phase D1 (this manifest): Sun config extraction, additive only
- Phase D2 (planned): call site replacement, `sun_position` wiring,
  asteroid belt decision
- Phase D3 (planned): cleanup sweep, imports, dead helper functions,
  Mode 7 verification

---

*Paloma's Orrery | palomasorrery.com*
*"Three Claudes, one Tony, zero orchestration framework." -- May 2026*

