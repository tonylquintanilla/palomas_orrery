# Shell Consolidation Manifest Request -- Phase C4 (Saturn + Uranus + Neptune)

**To:** Claude Opus 4.7
**From:** Tony Quintanilla (integrator) + Claude Opus 4.6 (implementation partner)
**Date:** May 16, 2026
**Revision:** v6 -- Phase C3 complete. 9 bodies migrated to unified dispatch
(Mercury, Moon, Planet 9, Pluto, Eris, Venus, Mars, Earth, Jupiter).
Ring helper `create_ring_points()` promoted to `orrery_rendering.py`.
Saturn/Uranus/Neptune already import from `orrery_rendering`. 22 deferred
items documented in C3 handoff.
**Project:** Paloma's Orrery -- Step 3 of Plotting Consolidation

---

## What we need from you

Design a detailed implementation manifest for migrating Saturn, Uranus,
and Neptune to the unified config-driven dispatch. This is Phase C4 --
the final migration phase before Phase D cleanup.

These three bodies share structural patterns (gas/ice giant interiors,
ring systems, magnetospheres, radiation belts) but Neptune has unique
complexity (magnetic pole visualization, field-aligned currents inside
the radiation belt builder, Adams ring arcs with named features).

**The architecture is proven across 9 bodies.** Ring helper is already
promoted. `magnetic_tilt_deg` parameter exists in `rotate_to_sunward()`
but has never been wired -- C4 is where it gets its first real use for
Uranus (60 deg) and Neptune (47 deg).

---

## Context: what's already done

### Phases A-C3 (May 14-16): 9 bodies migrated

All prior phases complete. Key C4-relevant deliverables:
- `create_ring_points()` in `orrery_rendering.py` (promoted from Saturn
  in C3). Saturn, Uranus, Neptune already import from `orrery_rendering`.
- `rotate_to_sunward()` with `magnetic_tilt_deg` parameter (defaulted
  to 0, never used). C4 wires it for Uranus/Neptune.
- CUSTOM_SHELLS pattern proven for magnetospheres (5 bodies), plasma
  tori (Jupiter), radiation belts (Jupiter), ring systems (Jupiter).
- Rotation precedent: magnetosphere rotates; rings, belts, torus do NOT.

### Current state after C3

| Component | Count |
|-----------|------:|
| Bodies in SHELL_CONFIGS | 9 |
| Total sphere shell configs | 52 |
| Bodies in CUSTOM_SHELLS | 5 |
| Total custom entries | 11 |
| Bodies remaining on old dispatch | 4 (Saturn, Uranus, Neptune, Sun) |

### Files delivered through C3 (current state)

| File | Lines | Status |
|------|------:|--------|
| `orrery_rendering.py` | 309 | `build_sphere_shell()`, `create_info_marker()`, `rotate_to_sunward()`, `create_ring_points()` |
| `shell_configs.py` | 1,840 | 9 bodies sphere + 5 bodies custom |
| `planet_visualization.py` | 901 | 9 bodies delegate; 4 remain on old path |

---

## C4 scope: Saturn + Uranus + Neptune

### Saturn (10 functions, 10 GUI toggles, 1,251 lines)

**Sphere-category (6 functions -> SHELL_CONFIGS):**

| Shell | Function | Geometry |
|-------|----------|----------|
| Core | `create_saturn_core_shell` | scatter3d sphere |
| Metallic hydrogen | `create_saturn_metallic_hydrogen_shell` | scatter3d sphere |
| Molecular hydrogen | `create_saturn_molecular_hydrogen_shell` | scatter3d sphere |
| Cloud layer | `create_saturn_cloud_layer_shell` | mesh3d |
| Upper atmosphere | `create_saturn_upper_atmosphere_shell` | scatter3d sphere (has sun indicator) |
| Hill sphere | `create_saturn_hill_sphere_shell` | scatter3d sphere (has sun indicator) |

**Custom-category (4 functions -> CUSTOM_SHELLS):**

| Shell | Function | Traces | Notes |
|-------|----------|-------:|-------|
| Magnetosphere | `create_saturn_magnetosphere` | 2 | Same as Jupiter: 1 group, no bow shock. Has sun indicator |
| Enceladus plasma torus | `create_saturn_enceladus_plasma_torus` | 2 | Same pattern as Jupiter Io torus. Has sun indicator |
| Radiation belts | `create_saturn_radiation_belts` | 12 | 6 belt components x 2 traces each. Has sun indicator |
| Ring system | `create_saturn_ring_system` | 14 | 7 ring components x 2 traces. Uses `create_ring_points()`. Has sun indicator |

**Sun indicators: 6** (upper_atmosphere, hill_sphere, magnetosphere,
enceladus_torus, radiation_belts, ring_system).

---

### Uranus (8 functions, 8 GUI toggles, 1,178 lines)

**Sphere-category (5 functions -> SHELL_CONFIGS):**

| Shell | Function | Geometry |
|-------|----------|----------|
| Core | `create_uranus_core_shell` | scatter3d sphere |
| Mantle | `create_uranus_mantle_shell` | scatter3d sphere |
| Cloud layer | `create_uranus_cloud_layer_shell` | mesh3d |
| Upper atmosphere | `create_uranus_upper_atmosphere_shell` | scatter3d sphere (has sun indicator) |
| Hill sphere | `create_uranus_hill_sphere_shell` | scatter3d sphere (has sun indicator) |

**Custom-category (3 functions -> CUSTOM_SHELLS):**

| Shell | Function | Traces | Notes |
|-------|----------|-------:|-------|
| Magnetosphere | `create_uranus_magnetosphere` | 1 | **Missing info marker** (pre-existing). Has sun indicator |
| Radiation belts | `create_uranus_radiation_belts` | 4 | 2 belts x 2 traces. Has sun indicator |
| Ring system | `create_uranus_ring_system` | 22 | 11 rings x 2 traces. Uses `create_ring_points()`. Has sun indicator |

**Sun indicators: 5** (upper_atmosphere, hill_sphere, magnetosphere,
radiation_belts, ring_system).

**`magnetic_tilt_deg`: 60 degrees** -- Uranus's magnetic axis is tilted
~60 degrees from its rotational axis, which is itself tilted ~98 degrees
from orbital plane. The `magnetic_tilt_deg` parameter in
`rotate_to_sunward()` was designed for this case.

---

### Neptune (11 functions, 8 GUI toggles, 1,844 lines)

**Sphere-category (5 functions -> SHELL_CONFIGS):**

| Shell | Function | Geometry |
|-------|----------|----------|
| Core | `create_neptune_core_shell` | scatter3d sphere |
| Mantle | `create_neptune_mantle_shell` | scatter3d sphere |
| Cloud layer | `create_neptune_cloud_layer_shell` | mesh3d |
| Upper atmosphere | `create_neptune_upper_atmosphere_shell` | scatter3d sphere (has sun indicator) |
| Hill sphere | `create_neptune_hill_sphere_shell` | scatter3d sphere (has sun indicator) |

**Custom-category (3 dispatch-visible functions -> CUSTOM_SHELLS):**

| Shell | Function | Traces | Notes |
|-------|----------|-------:|-------|
| Magnetosphere | `create_neptune_magnetosphere` | 6 | 1 magnetosphere + 1 info marker + 4 magnetic pole/axis traces. **Most complex magnetosphere.** Has sun indicator |
| Radiation belts | `create_neptune_radiation_belts` | 12 | 3 belts + cusp region + 2 field-aligned currents (FAC), each x 2 traces. Calls `create_field_aligned_currents()` internally. Has sun indicator |
| Ring system | `create_neptune_ring_system` | 22 | Multiple rings including Adams ring arcs (Liberte, Egalite, Fraternite, Courage). Uses `create_ring_points()`. Has sun indicator |

**Helper functions (3, NOT in dispatch, called from custom builders):**

| Function | Called from | Role |
|----------|-------------|------|
| `create_neptune_magnetic_poles` | `create_neptune_magnetosphere` | Generates magnetic axis, pole markers, field center |
| `create_field_aligned_currents` | `create_neptune_radiation_belts` | Generates dawn/dusk FAC traces |
| `create_neptune_field_lines` | **Nowhere -- dead code** | Defined but never called |

**Sun indicators: 5** (upper_atmosphere, hill_sphere, magnetosphere,
radiation_belts, ring_system).

**`magnetic_tilt_deg`: 47 degrees** -- Neptune's magnetic axis is tilted
~47 degrees from its rotational axis, with the magnetic center offset
from the geometric center by ~0.55 Neptune radii.

---

## Key design questions for C4

### Q1: `magnetic_tilt_deg` wiring

The parameter exists in `rotate_to_sunward()` but the C1 note says:
"Phase C4 will add a second rotation about the planet's rotation axis
by this angle to model the dipole offset."

Verify: is the current implementation in `rotate_to_sunward()` correct
for applying magnetic tilt, or does it need modification? The Rodrigues
rotation formula rotates geometry to face the Sun -- the tilt should
rotate the magnetosphere shape by the dipole offset angle relative to
the rotational axis AFTER the sunward rotation.

Uranus = 60 deg, Neptune = 47 deg. Saturn and Jupiter have small tilts
(~0 and ~10 deg) that we're defaulting to 0.

### Q2: Uranus magnetosphere missing info marker

`create_uranus_magnetosphere` emits only 1 trace (geometry, no info
marker). Same pre-existing omission as Mars magnetosphere (C1 item 14).
Add an info marker (same pattern as all other bodies), or preserve
the omission with a TODO? My recommendation: add the marker -- C4 is
the last chance before Phase D.

### Q3: Neptune magnetosphere complexity

Neptune's magnetosphere emits 6 traces including magnetic poles, axis
line, and field center marker. These are physically meaningful
(Neptune's offset dipole is a major feature). How should these interact
with `rotate_to_sunward()` and `magnetic_tilt_deg`?

Specifically: the magnetic poles and axis should tilt by
`magnetic_tilt_deg` (they represent the magnetic dipole orientation).
The magnetosphere envelope should rotate sunward AND tilt. Are these
the same rotation or two separate rotations?

### Q4: Neptune dead `create_neptune_field_lines`

Defined at line 770 but never called. Leave as dead code, or strip it?
My recommendation: leave it (out of scope, cosmetic).

### Q5: Neptune Adams ring arcs

Neptune's ring system includes the Adams ring arcs (Liberte, Egalite,
Fraternite, Courage) -- named features at specific orbital longitudes.
These use custom inline geometry rather than `create_ring_points()`.
Confirm they go in CUSTOM_SHELLS as part of the `ring_system` builder
(not separate entries).

### Q6: Saturn radiation belt count

Saturn emits 12 traces from `create_saturn_radiation_belts`. Verify
the actual belt/component names and whether any use for-loops where
info marker replacements would execute N times.

### Q7: Rotation decisions for C4 bodies

Confirm same precedent as C3:
- Magnetospheres: rotate (with `magnetic_tilt_deg` for Uranus/Neptune)
- Rings: NOT rotated (equatorial)
- Radiation belts: NOT rotated (axis-anchored)
- Enceladus torus: NOT rotated (equatorial)

### Q8: Session structure

Three bodies in one manifest. Should the manifest be structured by
body (all Saturn, then all Uranus, then all Neptune) or by operation
(all sphere configs, then all magnetosphere refactors, then all
delegations)? C1 used by-body (Pluto, Eris, Venus, Mars in sequence).
Same pattern recommended.

---

## Architecture reference

Same as C3. No changes to any contracts expected.

### Delegation pattern (same for all bodies)

```python
if planet_name == 'Saturn':
    return create_celestial_body_visualization(
        fig, planet_name, shell_vars,
        animate=animate, frames=frames,
        center_position=center_position,
        object_type='Saturn',
        center_object='Saturn',
    )
```

---

## Constraints

- **ASCII only** in all Python files
- **LF line endings** -- verify every file touched
- **Python binary mode** (rb/wb) for all file writes
- **Bottom-up editing** when making multiple changes to a file
- **Credit line:** `Module updated: May 2026 with Anthropic's Claude Opus 4.7`
- **Don't redesign the architecture** -- proven across 9 bodies
- **Exact data extraction** from source files, not training memory
- **n_points precedence** -- use value from current source file
- **Preserve `# Source:` citations** from provenance audit
- **Document `magnetic_tilt_deg` implementation clearly** -- this is the
  first real use of the parameter and sets precedent for any future
  body with a tilted dipole

---

## Files to audit

- `saturn_visualization_shells.py` -- 10 functions, 1,251 lines
- `uranus_visualization_shells.py` -- 8 functions, 1,178 lines
- `neptune_visualization_shells.py` -- 11 functions, 1,844 lines
- `planet_visualization.py` -- 3 dispatch blocks to replace
- `orrery_rendering.py` -- `rotate_to_sunward()` may need modification
  for `magnetic_tilt_deg` (Q1)
- `shell_configs.py` -- insertion point for 3 bodies' configs

---

## Workflow context

This manifest will be:
1. Reviewed by Claude Opus 4.6 + Tony (editorial review)
2. Implemented by Claude Opus 4.6 + Tony

C4 is the largest phase by body count (3 bodies, ~28 functions, ~4,273
lines of source). Consider splitting into session boundaries:
- Session 1: Saturn (most similar to Jupiter, establishes ice giant pattern)
- Session 2: Uranus + Neptune (magnetic tilt wiring, Neptune complexity)

Or all three in one session if the manifest is sufficiently mechanical.

The C3 handoff (attached) documents the current state and all 22
deferred items. Items 17-22 are pre-existing issues in these exact
three bodies that C4 migration resolves.

---

*Paloma's Orrery | palomasorrery.com*
*"You and me are doing the work of seven programmers." -- Tony, April 13, 2026*
