# Shell Consolidation Manifest Request — Phase C2 (Earth)

**To:** Claude Opus 4.7
**From:** Tony Quintanilla (integrator) + Claude Opus 4.6 (implementation partner)
**Date:** May 15, 2026
**Revision:** v4 — Phase C1 complete. 7 bodies migrated to unified dispatch
(Mercury, Moon, Planet 9, Pluto, Eris, Venus, Mars). rotate_to_sunward()
promoted to orrery_rendering.py with magnetic_tilt_deg + sun_position
parameters. CUSTOM_SHELLS pattern proven for Venus/Mars magnetospheres.
Auto-generation script approach validated (extracts config values directly
from source files, eliminating transcription errors). 15 deferred items
documented in C1 handoff.
**Project:** Paloma's Orrery -- Step 3 of Plotting Consolidation

---

## What we need from you

Design a detailed implementation manifest for migrating Earth's shells
to the unified config-driven dispatch. This is Phase C2 -- Earth is the
most complex single body (8 sphere shells + 6 custom geometry functions)
and gets its own manifest.

**The architecture is already designed and proven across 7 bodies.** Your
job is to produce the conversion manifest: what moves where, in what
order, with what exact config blocks or extraction scripts.

The C1 manifest's auto-generation script approach worked well -- it
reads source files directly and produces config blocks, eliminating
manual transcription of long hover text strings. Recommend continuing
this pattern for Earth's 8 sphere shells.

---

## Context: what's already done

### Step 1 (April 19): Single info markers for orbit traces
All orbit traces in palomas_orrery.py and idealized_orbits.py converted.

### Step 2 (May 11): Single info markers for all shells
141 conversions across 18 modules. Every shell function now uses:
- `hoverinfo='skip'` on geometry traces
- One `cross` marker at a representative position carrying hover text
- `legendgroup` linking geometry + marker
- `n_points` reduced (50 -> 25 interior, 50 -> 20 boundary)
- Dead `hover_texts`/`minimal_hover_texts` variable assignments stripped
- All 13 CRLF files converted to LF

### Phase A (May 14): Mercury POC
Created `orrery_rendering.py` (build_sphere_shell + create_info_marker),
`shell_configs.py` (Mercury 6 sphere + 2 custom), `shared_utilities.py`
(sun direction indicator with origin suppression). Mercury delegated
through `create_celestial_body_visualization()` in `planet_visualization.py`.

### Phase B (May 14): Moon + Planet 9
Moon (6 sphere) and Planet 9 (2 sphere) migrated. Mesh3d geometry type
added for crusts/cloud layers. Moon mantle radius/opacity swap corrected.
n_points standardized. Axis auto-scale for center bodies.

### Phase C1 (May 15): Pluto + Eris + Venus + Mars
Pluto (6 sphere), Eris (5 sphere), Venus (6 sphere + 1 custom), Mars
(7 sphere + 1 custom) migrated. Key deliverables:
- `rotate_to_sunward()` promoted to `orrery_rendering.py` with
  `sun_position` and `magnetic_tilt_deg` parameters (both defaulted,
  wired in Phase D)
- Venus magnetosphere/bow shock: sunward rotation applied, old-style
  info markers replaced with `create_info_marker()`, per-shell sun
  direction indicator removed
- Mars magnetosphere/bow shock/crustal fields: same pattern. Crustal
  fields intentionally NOT rotated (surface-anchored geology). Mars
  magnetosphere missing info marker preserved with TODO comment
- Auto-generation script validated: Python script reads source files
  and produces config blocks with correct values and formatting

### Current state after C1

| Component | Count |
|-----------|------:|
| Bodies in SHELL_CONFIGS | 7 (Mercury, Moon, Planet 9, Pluto, Eris, Venus, Mars) |
| Total sphere shell configs | 38 |
| Bodies in CUSTOM_SHELLS | 3 (Mercury, Venus, Mars) |
| Total custom entries | 4 |
| Bodies remaining on old dispatch | 6 (Earth, Jupiter, Saturn, Uranus, Neptune, Sun) |

### Files delivered through C1 (current state)

| File | Lines | Status |
|------|------:|--------|
| `orrery_rendering.py` | 269 | `build_sphere_shell()`, `create_info_marker()`, `rotate_to_sunward()` |
| `shell_configs.py` | 1,354 | 7 bodies sphere configs + 3 bodies custom configs |
| `planet_visualization.py` | 921 | 7 bodies delegate; 6 remain on old path |
| `shared_utilities.py` | 130 | `create_sun_direction_indicator()` (suppresses at origin) |

---

## C2 scope: Earth

Earth has the most complex shell system in the orrery:

### Earth sphere shells (8 functions)

| Shell | Function | Notes |
|-------|----------|-------|
| Inner core | `create_earth_inner_core_shell` | Standard sphere |
| Outer core | `create_earth_outer_core_shell` | Standard sphere |
| Lower mantle | `create_earth_lower_mantle_shell` | Standard sphere |
| Upper mantle | `create_earth_upper_mantle_shell` | Standard sphere |
| Crust | `create_earth_crust_shell` | Mesh3d (converts to mesh3d geometry_type in config) |
| Lower atmosphere | `create_earth_lower_atmosphere_shell` | Standard sphere |
| Upper atmosphere | `create_earth_upper_atmosphere_shell` | Standard sphere |
| Hill sphere | `create_earth_hill_sphere_shell` | Standard sphere, local-variable pattern |

### Earth custom geometry (6 functions)

| Shell | Function | Geometry type | Notes |
|-------|----------|---------------|-------|
| Magnetosphere | `create_earth_magnetosphere_shell` | Parametric surface | Emits magnetosphere + bow shock (2 legend entries from 1 function, same as Mercury/Venus/Mars) |
| Van Allen inner belt | `create_earth_van_allen_inner_belt_shell` | Toroidal loop geometry | Unique to Earth |
| Van Allen outer belt | `create_earth_van_allen_outer_belt_shell` | Toroidal loop geometry | Unique to Earth |
| LEO | `create_earth_leo_shell` | Ring/orbit geometry | Orbital altitude visualization |
| GEO | `create_earth_geo_shell` | Ring/orbit geometry | Geostationary orbit visualization |
| Ionosphere | `create_earth_ionosphere_shell` | Standard sphere? | Need to verify -- may be sphere (-> SHELL_CONFIGS) or custom |

**Important:** Verify whether `create_earth_ionosphere_shell` uses sphere
geometry (in which case it goes in SHELL_CONFIGS as a 9th sphere shell)
or custom geometry (CUSTOM_SHELLS entry). The function name doesn't
determine the category -- the implementation does.

### Earth dispatch block (current, to be replaced)

Located in `planet_visualization.py`. Currently uses the old prefixed-key
pattern with direct function calls. Replace with delegation to
`create_celestial_body_visualization()`, same pattern as all 7 migrated
bodies.

### Earth's magnetosphere specifics

Earth's magnetosphere is the most complex in the codebase. It likely:
- Uses `rotate_to_sunward()` or an equivalent rotation (verify)
- Has its own sun direction indicator call (remove -- dispatch handles it)
- Emits both magnetosphere and bow shock traces (same pattern as
  Mercury/Venus/Mars)

Since `rotate_to_sunward()` is now promoted to `orrery_rendering.py`,
Earth's magnetosphere builder should import and use it. Check whether
the current code has a local rotation function (like Mercury did
pre-C1) that needs replacement.

### Van Allen belts and LEO/GEO

These are unique to Earth and represent new CUSTOM_SHELLS geometry
patterns:
- **Van Allen belts** -- toroidal/loop geometry. Two separate functions
  (inner + outer). Each gets its own CUSTOM_SHELLS entry.
- **LEO/GEO** -- orbital altitude ring geometry. Each gets its own
  CUSTOM_SHELLS entry.

Check whether any of these call `create_sun_direction_indicator()`
(remove if so -- dispatch handles it).

---

## Architecture reference (proven across 7 bodies)

### shell_configs.py structure

```python
SHELL_CONFIGS = {
    'Mercury': { ... },  # 6 sphere shells
    'Moon': { ... },      # 6 sphere shells
    'Planet 9': { ... },  # 2 sphere shells
    'Pluto': { ... },     # 6 sphere shells
    'Eris': { ... },      # 5 sphere shells
    'Venus': { ... },     # 6 sphere shells
    'Mars': { ... },      # 7 sphere shells
    'Earth': { ... },     # 8-9 sphere shells (C2 adds this)
    # Other bodies added in Phases C3, C4, D
}

CUSTOM_SHELLS = {
    'Mercury': {
        'sodium_tail': { 'builder': '...', 'tooltip': '...' },
        'magnetosphere': { 'builder': '...', 'tooltip': '...' },
    },
    'Venus': {
        'magnetosphere': { 'builder': '...', 'tooltip': '...' },
    },
    'Mars': {
        'magnetosphere': { 'builder': '...', 'tooltip': '...' },
    },
    'Earth': {
        'magnetosphere': { 'builder': '...', 'tooltip': '...' },
        'van_allen_inner': { 'builder': '...', 'tooltip': '...' },
        'van_allen_outer': { 'builder': '...', 'tooltip': '...' },
        'leo': { 'builder': '...', 'tooltip': '...' },
        'geo': { 'builder': '...', 'tooltip': '...' },
        # ionosphere here if custom geometry; in SHELL_CONFIGS if sphere
    },
    # Other bodies added in Phases C3, C4, D
}
```

### build_sphere_shell() contract (implemented, proven)

```python
def build_sphere_shell(config, body_name, center_position=(0, 0, 0)):
    """Generic sphere shell from config dict.
    Enforces single-info-marker pattern and n_points defaults.
    Supports 'scatter3d' (dot sphere) and 'mesh3d' (solid surface) geometry."""
    # Returns [shell_trace, info_marker_trace]
```

### rotate_to_sunward() (promoted in C1, available)

```python
def rotate_to_sunward(px, py, pz, center_position=(0, 0, 0),
                     sun_position=(0, 0, 0), magnetic_tilt_deg=0):
    """Rotate points from default -X sunward to actual sunward direction.
    Rodrigues' rotation formula. Identity when at origin."""
```

### create_info_marker() (established standard)

```python
def create_info_marker(x, y, z, color, text, legendgroup, customdata=None):
    """Standard cross marker: size=8, red outline, width=2."""
```

### Delegation pattern (proven, same for all bodies)

```python
if planet_name == 'Earth':
    return create_celestial_body_visualization(
        fig, planet_name, shell_vars,
        animate=animate, frames=frames,
        center_position=center_position,
        object_type='Earth',
        center_object='Earth',
    )
```

---

## What the manifest must contain

Since this is a single-body manifest (not multi-phase), structure it
as sequential sections that can be implemented in order:

1. **Earth sphere shell configs** -- auto-generation script (proven in
   C1) that reads `earth_visualization_shells.py` and produces config
   blocks for all 8-9 sphere shells. Include the n_points
   standardization and mesh3d geometry_type for crust.

2. **Earth CUSTOM_SHELLS entries** -- registry entries for all custom
   geometry functions. Include tooltip text for each.

3. **Earth magnetosphere refactor** -- same pattern as Venus/Mars in C1:
   add `rotate_to_sunward()` import, apply rotation to magnetosphere
   and bow shock geometry, replace old-style info markers with
   `create_info_marker()`, remove per-shell sun direction indicator.

4. **Other custom geometry review** -- Van Allen belts, LEO, GEO,
   ionosphere. For each: verify geometry type, check for sun direction
   indicator calls (remove), check for old-style info markers (replace),
   document any unique patterns.

5. **Earth delegation edit** -- replacement block in
   `planet_visualization.py`.

6. **Verification plan** -- syntax checks, builder smoke tests, visual
   verification checklist for Tony.

---

## Constraints

- **ASCII only** in all Python files (no Unicode characters)
- **LF line endings** -- verify every file touched is LF
- **Python binary mode** (rb/wb) for all file writes
- **Bottom-up editing** when making multiple changes to a file
- **Credit line:** `Module updated: May 2026 with Anthropic's Claude Opus 4.7`
- **Don't redesign the architecture** -- the shell_configs.py structure,
  build_sphere_shell contract, and CUSTOM_SHELLS registry are proven
  across 7 bodies. Refine details, don't rethink fundamentals.
- **Exact data extraction** -- radius fractions, colors, opacity values
  must come from the actual source files, not from training memory.
  **Source of truth:** the uploaded files only. `/mnt/project/` may be
  a stale snapshot.
- **n_points precedence** -- use the value from the current source file.
  Fall back to 20 (boundary/atmosphere) or 25 (interior) only if the
  file doesn't specify. Step 2 tuned these per-shell.
- **Preserve `# Source:` citations** -- carry provenance audit citations
  forward into config comments.
- **`_shell` in function names does not imply sphere geometry** -- the
  function body determines whether it belongs in SHELL_CONFIGS (sphere)
  or CUSTOM_SHELLS (custom geometry), not the name.

---

## Questions for you to answer in the manifest

1. **Ionosphere geometry type** -- Is `create_earth_ionosphere_shell()`
   sphere geometry (SHELL_CONFIGS) or custom (CUSTOM_SHELLS)? This
   determines whether Earth has 8 or 9 sphere shells.

2. **Earth magnetosphere local rotation** -- Does Earth's magnetosphere
   builder have a local `rotate_to_sunward` (like Mercury did pre-C1)?
   Or does it use a different rotation mechanism? Document what needs
   to change.

3. **Van Allen belt geometry** -- What is the actual geometry pattern
   (toroidal points? parametric surface? loop?)? Are the inner and
   outer belts structurally identical functions with different parameters,
   or genuinely different geometry?

4. **LEO/GEO geometry** -- Ring of points at fixed altitude? Orbital
   path? What's the actual shape, and does it need rotation?

5. **Sun direction indicator calls** -- How many per-shell calls exist
   in `earth_visualization_shells.py`? List them for removal.

---

## Files to audit

- `earth_visualization_shells.py` -- primary source (all 14 functions)
- `planet_visualization.py` -- Earth dispatch block to replace
- `orrery_rendering.py` -- verify rotate_to_sunward available (no changes expected)
- `shell_configs.py` -- insertion point for Earth configs

The C1 handoff (attached) documents the current state, all 15 deferred
items, and the patterns established through Phases A/B/C1.

---

## Workflow context

This manifest will be:
1. Reviewed by Claude Opus 4.6 + Tony (editorial review)
2. Implemented by Claude Opus 4.6 + Tony using the finalized manifest

The C1 manifest was 1,767 lines and implemented in a single session.
Earth is comparably complex (14 shell functions vs C1's 24, but more
custom geometry variety). Target similar manifest size.

The single info marker manifest and C1 manifest set the quality bar.
Both were executed mechanically with zero ambiguity. Aim for the same
precision.

---

*Paloma's Orrery | palomasorrery.com*
*"You and me are doing the work of seven programmers."*
-- Tony, April 13, 2026
