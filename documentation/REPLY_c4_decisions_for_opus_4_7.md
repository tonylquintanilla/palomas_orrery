# Phase C4 Decision Confirmation -- Reply to Opus 4.7

**From:** Tony Quintanilla (integrator) + Claude Opus 4.6 (implementation partner)
**To:** Claude Opus 4.7 (manifest author)
**Date:** May 17, 2026

---

## Decisions confirmed

### Q1/Q3: magnetic_tilt_deg -- implement for Uranus, not Neptune

Agree with recommendation (b) for Neptune: keep Neptune's internal
tilt/offset rotation, pass `magnetic_tilt_deg=0` to `rotate_to_sunward()`.
Neptune's source code already handles bow shock/tail region-specific
rotation and the 0.55 R_N dipole offset. Double-tilting would be a
physics error.

**Uranus: implement `magnetic_tilt_deg=60` now.** Tony's decision: this
is fundamental to the shell structure, not a deferral. The
`rotate_to_sunward()` placeholder code needs to be implemented --
add a second Rodrigues rotation about the planet's rotation axis by
`magnetic_tilt_deg` degrees AFTER the sunward rotation. This is a real
code change to `orrery_rendering.py`.

**Earth (11 deg) and Jupiter (10 deg): defer to Phase D.** Visually
subtle at those angles. Phase D already revisits every body file for
`sun_position` wiring -- adding `magnetic_tilt_deg` is a one-parameter
change per call site at that point.

Saturn: `magnetic_tilt_deg=0` (its dipole is essentially aligned with
the rotation axis).

### Saturn ring tooltip -- fix the copy-paste error

Confirmed. The tooltip text references Jupiter's moons (Metis, Adrastea)
and Jupiter ring names (Amalthea Gossamer, Thebe Gossamer). Fix during
extraction. Use the per-ring `description` fields from the function body,
which have correct Saturn-specific text.

### Uranus radiation belt dead offset -- clean up

Strip the silently-overwritten first offset assignment. The correct
offset is applied later after tilt. Remove the dead lines.

### Q2: Uranus missing info marker -- add it

Same pre-existing omission as Mars (C1 item 14). Add the marker using
`create_info_marker()`, standard pattern.

### Q4: Neptune dead `create_neptune_field_lines` -- strip it

Changed from "leave" to "strip." We're touching the file anyway, dead
code is dead code. Remove the function definition.

### Q5: Adams ring arcs -- confirmed inside ring_system builder

Single CUSTOM_SHELLS entry for `ring_system`. The arcs use custom
inline geometry at specific orbital longitudes. Not separate entries.

### Q6: Saturn radiation belt count -- manifest must document

12 traces = 6 components x 2. Document the component names and
flag any for-loop info marker replacements.

### Q7: Rotation decisions -- same as C3 with one clarification

- Magnetospheres: rotate via `rotate_to_sunward()`. Uranus gets
  `magnetic_tilt_deg=60`. Neptune passes 0 (internal handling).
  Saturn passes 0 (aligned dipole).
- Rings: NOT rotated (equatorial)
- Radiation belts: NOT rotated (axis-anchored)
- Enceladus torus: NOT rotated (equatorial)

**Critical clarification -- axial tilt vs magnetic tilt:**
Saturn/Uranus radiation belt builders apply axial tilt (obliquity)
internally to place belts in the planet's actual equatorial plane.
This is physically correct and must be PRESERVED -- it is not the
same rotation as `magnetic_tilt_deg`. The manifest must clearly
distinguish:
- Axial tilt (obliquity, e.g. Saturn -26.73 deg): planet's equatorial
  plane vs ecliptic. Applied inside belt/ring/torus builders. KEEP.
- Magnetic tilt (dipole offset, e.g. Uranus 60 deg): magnetic dipole
  axis vs rotation axis. Applied via `rotate_to_sunward()`. NEW.

### Q8: Session structure -- by body

Saturn first (most similar to Jupiter), then Uranus + Neptune.

---

## Summary of non-standard decisions for C4

These deviate from the "strictly mechanical" pattern of C1-C3:

1. **`rotate_to_sunward()` code change** -- implement the
   `magnetic_tilt_deg` rotation. Small addition to Rodrigues formula
   in `orrery_rendering.py`. First real modification of this function
   since Phase A.

2. **Uranus info marker addition** -- adding content that didn't exist
   before. Editorial, not mechanical. But matches the pattern of every
   other body.

3. **Saturn ring tooltip correction** -- fixing pre-existing copy-paste
   error from Jupiter. Content fix, not mechanical.

4. **Neptune dead function removal** -- `create_neptune_field_lines`
   stripped.

5. **Uranus dead offset cleanup** -- cosmetic code cleanup.

Everything else is mechanical conversion following the proven 9-body
pattern.

---

## Attached context

- C3 handoff (22 deferred items)
- v6 prompt (unchanged)
- `saturn_visualization_shells.py`
- `uranus_visualization_shells.py`
- `neptune_visualization_shells.py`
- `orrery_rendering.py` (for `rotate_to_sunward()` audit)

Proceed with the manifest draft.

---

*"Three Claudes, one Tony, zero orchestration framework." -- May 2026*
