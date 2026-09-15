# Run and test sequence, 2026-09-15

Nine patches. Orrery first, then gallery, because the gallery's drift check
reads the orrery's pushed HEAD.

Two patches are **withdrawn**. Delete them without running:
`patch_L330_belt_plane_ledger_item.py` and
`patch_L231_belt_plane_amendment.py`.

Two are **already in** from earlier tonight and need nothing:
`patch_L305_l_shell_scalar_unit.py` (gallery) and
`patch_L305_item6b_magnetopause_cut_angle.py` (orrery).

---

## Step 0 — before anything

In BOTH repositories:

```
git status --porcelain
```

Expect nothing. If `data/objects_config.json` shows as modified in the
gallery, that is the local drift that made the Earth scene checker report
three white outlines instead of four at the start of tonight. Fix it with:

```
git checkout -- data/objects_config.json
```

Every patch below fingerprints its target and refuses on a mismatch, so a
dirty file will stop the sequence rather than corrupt it. That is the guard
working, not a failure.

---

## Part 1 — the orrery

Run from the orrery repo root, in this order.

### 1. The ledger

```
python patch_L231_L305_L330_belt_plane_ruling.py
python ledger_index.py
```

Expect: three places updated, and ONE more block than the last run
reported. No consistency problems.

### 2. The dipole tilt into the store

```
python patch_L231_dipole_tilt_to_store.py
python -c "import constants_new as c; print(c.EARTH_DIPOLE_TILT_DEG)"
python -c "import planet_visualization_utilities as p; print(p.PLANET_DIPOLE['Earth']['tilt_deg'])"
```

Expect: both print `9.6`. If the second one raises an ImportError, the
import line did not land — stop and say so.

### 3. The belts into Earth's equatorial plane

```
python patch_L231_belt_plane_orrery.py
python -m py_compile earth_visualization_shells.py
```

Expect: three changes reported, and a silent compile.

### 4. Orrery checks

```
python provenance_scanner.py
python test_status_lines.py
```

Expect: Tier-1 does NOT rise, and no file's Tier-1 count rises. The new
store row will likely add ONE Tier-2 finding, the same as the cut-angle row
did — cited, not independently cross-checked.

### 5. Render it — this is the Mode 5 call

Open Earth with the belts, the magnetosphere and the geostationary ring
switched on. Three things to look for:

- Both belts now lie in the same plane as the equator and the
  geostationary ring, rather than 23 degrees off it.
- Both belts are flat. The old saddle lifted each ring by a fifth of its
  radius, twice per circuit — nearly a full Earth radius up and down on the
  outer belt.
- The magnetopause is upright inside the bow shock, not leaning. It used to
  lean 11 degrees while the bow shock did not.

If any of that looks wrong, stop before pushing.

### 6. Push the orrery

```
git add -A && git commit && git push
git ls-remote origin HEAD
```

Note the new SHA. The gallery's drift check will read it.

---

## Part 2 — the gallery

Run from the gallery repo root, in this order. **The order is enforced by
fingerprints** — each patch expects the tree the previous one left.

### 7. The served surface rows

```
python patch_L305_item6b_served_surface_rows.py
python gallery_maintenance_run.py
```

Expect: 11 rows added, and the Earth scene UNCHANGED at 18 drawer groups.
This patch adds no names, so it must not move the picture at all.

### 8. The magnetosphere drawing code

```
python patch_L305_item5_magnetosphere_render.py
node documentation/smoke_earth_geometry.js gallery/feature_renderers.js gallery/earth_geometry.js
```

Expect: ALL CHECKS PASSED, 20 drawer groups, no warnings, nothing named
absent, and ten new legs about the two surfaces.

### 9. The fixture sync

```
python patch_L305_item5_fixture_sync.py
node documentation/smoke_earth_geometry.js gallery/feature_renderers.js gallery/earth_geometry.js
```

Expect: ALL CHECKS PASSED, and the border leg listing twenty markers —
sixteen red and four white.

### 10. The belts into Earth's equatorial plane

```
python patch_L231_belt_plane_gallery.py
node documentation/smoke_earth_geometry.js gallery/feature_renderers.js gallery/earth_geometry.js
```

Expect: ALL CHECKS PASSED, with ten more legs — each belt shares a plane
with the equator and the geostationary ring, each is flat, each hover names
the drawn width as a choice and gives the sourced span.

### 11. Serve and quote the tilt

```
python patch_L231_serve_and_quote_tilt.py
node documentation/smoke_earth_geometry.js gallery/feature_renderers.js gallery/earth_geometry.js
```

Expect: ALL CHECKS PASSED, including one leg per belt confirming the hover
carries 9.6 degrees with its model and epoch.

### 12. The full offline run

```
python gallery_maintenance_run.py
```

Expect: all six gating checkers pass.

**Note:** the Earth scene geometry checker may still report the white
outline finding if that turns out to be a real disagreement rather than
local drift. It gates. If it fires, Step 0 is the first thing to re-check.

### 13. Push the gallery

```
git add -A && git commit && git push
python gallery_maintenance_run.py --live
```

Expect, and this is a prediction stated before the run:

```
70 pointers: 56 match, 0 DRIFT, 1 UNIT MISMATCH, 13 could not be examined.
```

The one unit mismatch is `EARTH_VAN_ALLEN_OUTER_RADII` — its name declares
Earth radii and the config says L shell. That is the true state of the row
and it clears when L-322 teaches the checker to read the store's own
`# Unit:` line. The thirteen unexamined are four belt edges, the four Shue
and Jelinek coefficients with no unit suffix in their names, the four
planet poles and the galactic tide default.

If the match count is anything other than 56, stop and read the list rather
than assuming it is the same cause.

### 14. Look at the page

Open the Earth exhibit. Two things are new in the drawer:

- **Magnetopause** and **Bow Shock**. Both are far larger than the arrival
  frame, so they wait in the drawer rather than being lit on arrival. Turn
  them on together. The bow shock ends wider and shorter than the
  magnetopause; that is correct and is two papers' drawing limits, not a
  fact about the two boundaries.
- The belts are now in the same plane as the geostationary ring.

---

## If something stops

Every patch writes nothing unless its fingerprint matches, so a failure
leaves the tree exactly as it was. The message names the file and says what
it expected. Send it over and I will look.

## What is still open after all this

- **L-330**, the belt's shape: rings at the peaks versus the region between
  the served edges. Needs your eye on the plane fix first.
- **L-322**, teaching the maintenance checker to read units from the
  store's own comment line rather than from constant names. That clears
  five of the thirteen unexamined pointers and the one unit mismatch.
- **L-305 item 6b** remainder and the handoff edits from the start of the
  session.
