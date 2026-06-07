# Shell Consolidation Manifest Request -- Phase C3 (Jupiter)

**To:** Claude Opus 4.7
**From:** Tony Quintanilla (integrator) + Claude Opus 4.6 (implementation partner)
**Date:** May 16, 2026
**Revision:** v5 -- Phase C2 complete. 8 bodies migrated to unified dispatch
(Mercury, Moon, Planet 9, Pluto, Eris, Venus, Mars, Earth). Earth
magnetosphere rotation verified. Van Allen belt non-rotation precedent
established. LEO/GEO ring CUSTOM_SHELLS pattern proven. Auto-generation
script approach validated across all phases. 15 deferred items documented
in C2 handoff.
**Project:** Paloma's Orrery -- Step 3 of Plotting Consolidation

---

## What we need from you

Design a detailed implementation manifest for migrating Jupiter's shells
to the unified config-driven dispatch. This is Phase C3 -- Jupiter is the
first gas giant and introduces new CUSTOM_SHELLS geometry patterns (rings,
Io plasma torus, radiation belts) that Saturn/Uranus/Neptune will reuse
in Phase C4.

**The architecture is already designed and proven across 8 bodies.** Your
job is to produce the conversion manifest: what moves where, in what
order, with what exact config blocks or extraction scripts.

The auto-generation script approach has been validated across all prior
phases -- it reads source files directly and produces config blocks,
eliminating manual transcription. Continue this pattern for Jupiter's
6 sphere shells.

---

## Context: what's already done

### Steps 1-2 (April-May): Single info markers
All orbit traces and shell functions converted to single info marker
pattern. `hoverinfo='skip'` on geometry, one cross marker per object.

### Phases A-C2 (May 14-16): 8 bodies migrated
Mercury (POC), Moon, Planet 9, Pluto, Eris, Venus, Mars, Earth all
route through `create_celestial_body_visualization()`. Key deliverables
across these phases:
- `rotate_to_sunward()` in `orrery_rendering.py` with `sun_position`
  and `magnetic_tilt_deg` parameters (both defaulted, wired in Phase D)
- CUSTOM_SHELLS pattern proven for: Mercury sodium tail, Mercury/Venus/
  Mars/Earth magnetospheres, Earth LEO, Earth GEO
- Van Allen belt / Mars crustal fields precedent: geomagnetic/surface-
  anchored geometry is NOT rotated by `rotate_to_sunward()`
- Auto-generation script produces config blocks from source files

### Current state after C2

| Component | Count |
|-----------|------:|
| Bodies in SHELL_CONFIGS | 8 |
| Total sphere shell configs | 46 |
| Bodies in CUSTOM_SHELLS | 4 (Mercury, Venus, Mars, Earth) |
| Total custom entries | 7 |
| Bodies remaining on old dispatch | 5 (Jupiter, Saturn, Uranus, Neptune, Sun) |

### Files delivered through C2 (current state)

| File | Lines | Status |
|------|------:|--------|
| `orrery_rendering.py` | 269 | `build_sphere_shell()`, `create_info_marker()`, `rotate_to_sunward()` |
| `shell_configs.py` | 1,616 | 8 bodies sphere configs + 4 bodies custom configs |
| `planet_visualization.py` | 910 | 8 bodies delegate; 5 remain on old path |
| `shared_utilities.py` | 130 | `create_sun_direction_indicator()` (suppresses at origin) |

---

## C3 scope: Jupiter

Jupiter is the first gas giant and introduces geometry patterns that
Saturn, Uranus, and Neptune will reuse in Phase C4.

### Jupiter functions (11 total in jupiter_visualization_shells.py, 1,049 lines)

**Sphere-category (6 functions -> SHELL_CONFIGS):**

| Shell | Function | Geometry | Notes |
|-------|----------|----------|-------|
| Core | `create_jupiter_core_shell` | scatter3d sphere | Standard |
| Metallic hydrogen | `create_jupiter_metallic_hydrogen_shell` | scatter3d sphere | Standard |
| Molecular hydrogen | `create_jupiter_molecular_hydrogen_shell` | scatter3d sphere | Standard |
| Cloud layer | `create_jupiter_cloud_layer_shell` | mesh3d | Same as Earth/Moon/Pluto crust |
| Upper atmosphere | `create_jupiter_upper_atmosphere_shell` | scatter3d sphere | Has sun indicator (remove) |
| Hill sphere | `create_jupiter_hill_sphere_shell` | scatter3d sphere | Local-variable pattern; has sun indicator (remove) |

**Custom-category (5 functions -> CUSTOM_SHELLS):**

| Shell | Function | Geometry | Notes |
|-------|----------|----------|-------|
| Magnetosphere | `create_jupiter_magnetosphere` | Parametric surface via `create_magnetosphere_shape` | Same pattern as Mercury/Venus/Mars/Earth. Has sun indicator (remove) |
| Io plasma torus | `create_jupiter_io_plasma_torus` | Parametric torus (custom trig) | Unique to Jupiter. Has sun indicator (remove) |
| Radiation belts | `create_jupiter_radiation_belts` | Parametric loops (custom trig) | Similar to Earth Van Allen belts. Has sun indicator (remove) |
| Ring system | `create_jupiter_ring_system` | Ring geometry via `create_ring_points_jupiter` | Helper function at top of file. Has sun indicator (remove) |
| (helper) | `create_ring_points_jupiter` | N/A | Ring point generator, not a shell function |

**Sun direction indicator calls: 6** (in upper_atmosphere, magnetosphere,
io_plasma_torus, radiation_belts, hill_sphere, ring_system). All to be
removed -- dispatch handles this.

### Jupiter dispatch block (current, to be replaced)

10 shell_vars toggles in `planet_visualization.py`. Replace with
delegation to `create_celestial_body_visualization()`.

### Key design questions for C3

Jupiter introduces patterns C4 will reuse. The decisions made here
set precedent:

1. **Ring system geometry** -- Does `create_ring_points_jupiter` stay
   as a local helper or promote to a shared utility? Saturn, Uranus,
   Neptune all have ring systems. If the geometry logic is identical
   (just different radii/colors), a shared ring builder could serve
   all four. If Jupiter's rings are structurally unique, keep it local.

2. **Io plasma torus** -- Unique to Jupiter. Verify geometry type
   (toroidal? parametric surface? scatter points?). Gets its own
   CUSTOM_SHELLS entry.

3. **Radiation belts** -- Similar to Earth Van Allen belts? Same
   rotation question: should Jupiter's radiation belts rotate with
   the magnetosphere (they're magnetically trapped, unlike Earth's
   geomagnetic-axis-anchored Van Allen belts)? Or should they stay
   unrotated like Earth's? This is a physics question -- Jupiter's
   magnetic axis is tilted ~10 degrees from rotational axis, and the
   radiation belts follow the magnetic field. Document the decision.

4. **Magnetosphere rotation** -- Jupiter has the largest magnetosphere
   in the solar system (~100 R_J sunward). Apply `rotate_to_sunward()`
   same as Earth/Venus/Mars. `magnetic_tilt_deg` parameter exists but
   is defaulted to 0 -- Phase C4 will wire it for Uranus (60 deg) and
   Neptune (47 deg). For Jupiter (~10 deg tilt) the default is
   acceptable for now. Flag for future refinement if needed.

5. **Ring rotation** -- Rings are equatorial structures. They should
   NOT rotate with `rotate_to_sunward()`. Same precedent as Van Allen
   belts / Mars crustal fields: geometry anchored to the body's
   rotation, not the solar wind.

---

## Architecture reference (proven across 8 bodies)

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
    'Earth': { ... },     # 8 sphere shells
    'Jupiter': { ... },   # 6 sphere shells (C3 adds this)
}

CUSTOM_SHELLS = {
    'Mercury': { 'sodium_tail': {...}, 'magnetosphere': {...} },
    'Venus': { 'magnetosphere': {...} },
    'Mars': { 'magnetosphere': {...} },
    'Earth': { 'magnetosphere': {...}, 'leo': {...}, 'geostationary_belt': {...} },
    'Jupiter': {
        'magnetosphere': {...},
        'io_plasma_torus': {...},
        'radiation_belts': {...},
        'ring_system': {...},
    },
}
```

### Proven contracts (no changes expected)

- `build_sphere_shell(config, body_name, center_position)` -- returns [shell_trace, info_marker]
- `create_info_marker(x, y, z, color, text, legendgroup, customdata)` -- standard cross marker
- `rotate_to_sunward(px, py, pz, center_position, sun_position, magnetic_tilt_deg)` -- Rodrigues rotation

### Delegation pattern (same for all bodies)

```python
if planet_name == 'Jupiter':
    return create_celestial_body_visualization(
        fig, planet_name, shell_vars,
        animate=animate, frames=frames,
        center_position=center_position,
        object_type='Jupiter',
        center_object='Jupiter',
    )
```

---

## What the manifest must contain

Structure as sequential sections (same as C2):

1. **Jupiter sphere shell configs** -- auto-generation script that reads
   `jupiter_visualization_shells.py` and produces config blocks for all
   6 sphere shells. Include n_points standardization and mesh3d for
   cloud layer.

2. **Jupiter CUSTOM_SHELLS entries** -- registry entries for all 4 custom
   geometry functions (magnetosphere, io_plasma_torus, radiation_belts,
   ring_system). Include tooltip text.

3. **Jupiter magnetosphere refactor** -- same pattern as Earth/Venus/Mars:
   apply `rotate_to_sunward()`, replace old-style info markers with
   `create_info_marker()`, remove per-shell sun direction indicator.

4. **Other custom geometry review** -- Io torus, radiation belts, ring
   system. For each: verify geometry type, check for sun direction
   indicator calls (remove), check for old-style info markers (replace
   with `create_info_marker()`), document rotation decisions, note
   any patterns C4 will reuse.

5. **Jupiter delegation edit** -- replacement block in
   `planet_visualization.py`.

6. **Verification plan** -- syntax checks, builder smoke tests, visual
   verification checklist.

---

## Constraints

- **ASCII only** in all Python files
- **LF line endings** -- verify every file touched
- **Python binary mode** (rb/wb) for all file writes
- **Bottom-up editing** when making multiple changes to a file
- **Credit line:** `Module updated: May 2026 with Anthropic's Claude Opus 4.7`
- **Don't redesign the architecture** -- proven across 8 bodies
- **Exact data extraction** from source files, not training memory
- **n_points precedence** -- use value from current source file; fall
  back to 20 (boundary) or 25 (interior) only if not specified
- **Preserve `# Source:` citations** from provenance audit
- **`_shell` in function names does not imply sphere geometry**
- **Document C4 precedents** -- decisions about rings, radiation belts,
  and torus geometry will be reused for Saturn/Uranus/Neptune

---

## Questions for you to answer in the manifest

1. **Ring system helper** -- Should `create_ring_points_jupiter` promote
   to a shared utility for C4 reuse, or stay local? Check whether
   Saturn/Uranus/Neptune ring functions use similar geometry.

2. **Radiation belt rotation** -- Should Jupiter's radiation belts rotate
   with `rotate_to_sunward()` or stay unrotated? Earth's Van Allen belts
   stay unrotated (geomagnetic-axis-anchored). Jupiter's radiation
   environment is different -- the belts are magnetically trapped in
   Jupiter's tilted dipole field. What's physically correct?

3. **Io plasma torus rotation** -- The torus orbits at Io's orbital
   radius (~5.9 R_J) in Jupiter's equatorial plane. Should it rotate
   with the magnetosphere? It's magnetically confined but equatorially
   distributed.

4. **Ring rotation** -- Confirm rings should NOT rotate (equatorial
   structure, not solar-wind-driven).

5. **Magnetosphere trace structure** -- Does Jupiter's magnetosphere
   emit the same 2-group pattern as Earth (magnetosphere + bow shock)?
   Or does it have additional components?

6. **Sun direction indicator calls** -- Confirm count and locations for
   removal (expected: 6 calls across upper_atmosphere, magnetosphere,
   io_plasma_torus, radiation_belts, hill_sphere, ring_system).

---

## Files to audit

- `jupiter_visualization_shells.py` -- primary source (11 functions, 1,049 lines)
- `planet_visualization.py` -- Jupiter dispatch block to replace
- `orrery_rendering.py` -- verify `rotate_to_sunward` available (no changes expected)
- `shell_configs.py` -- insertion point for Jupiter configs
- `saturn_visualization_shells.py` -- check ring helper for C4 comparison
- `uranus_visualization_shells.py` -- check ring helper for C4 comparison
- `neptune_visualization_shells.py` -- check ring helper for C4 comparison

---

## Workflow context

This manifest will be:
1. Reviewed by Claude Opus 4.6 + Tony (editorial review)
2. Implemented by Claude Opus 4.6 + Tony using the finalized manifest

The C2 manifest was 1,320 lines and implemented in a single session
with zero blockers. Jupiter has comparable complexity (11 functions
vs Earth's 11, but more custom geometry variety). Target similar
manifest size.

The C2 handoff (attached) documents the current state, all 15 deferred
items, and the patterns established through Phases A-C2.

---

*Paloma's Orrery | palomasorrery.com*
*"You and me are doing the work of seven programmers." -- Tony, April 13, 2026*
