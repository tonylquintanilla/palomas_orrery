# Stage 3 sweep -- Testing Protocol (v1)

**Date:** May 27, 2026
**Tester:** Tony Quintanilla
**Mode:** Mode 5 (visual verification -- Tony leads)
**Files changed:** 14 (all 13 `*_visualization_shells.py` + `orrery_rendering.py`)

---

## What changed

73 info-marker conversions, 8 documented red-on-red preserves,
2 ring marker geometry fixes (Saturn, Uranus), 14 dormant
`create_sun_direction_indicator` call blocks deleted (+ 6 now-dead
imports removed), 1 `n_points=50 -> 25` normalization (Planet 9 hill
sphere), 1 docstring update (`create_info_marker` migration intent).

| Change | Sites |
|------|-------|
| Info marker style: `size 6->8, opacity 0.9/0.95->1.0, white border w=1 -> red border w=2` | 73 |
| Info marker preserved (red-on-red exception, old pattern + inline comment) | 8 |
| Ring info marker geometry fix (Neptune 2C pattern) | 2 (Saturn, Uranus) |
| Dormant `sun_traces` call block deleted | 14 |
| Dead `create_sun_direction_indicator` import removed | 6 |
| `n_points=50 -> 25` normalization | 1 (Planet 9 hill sphere) |
| `create_info_marker` migration-intent docstring update | 1 (orrery_rendering.py) |

Container-side gates passed in the session: `py_compile` on every
edited file, import test on every edited module, functional
exercise of every marker-producing function including all 8
preserved exceptions, ring marker position uniqueness check
(7/7 Saturn, 11/11 Uranus -- previously 1/1 each). This protocol
is the Mode 5 gate that compile + execute cannot perform.

---

## Test structure

Three scenarios covering breadth, depth, and the new geometry fix.

- **Scenario A** -- Representative breadth pass. One render per
  category (terrestrial, gas giant, ice giant, dwarf, Sun). Spot-
  checks the standard, the preserves, and the warm-tone Mode 5
  flags. Most efficient way to catch a systematic error.
- **Scenario B** -- Ring marker fix verification. Saturn alone,
  then Uranus alone. Catches the geometry fix.
- **Scenario C** -- Dormant call cleanup verification. Plot any of
  the 6 affected bodies and confirm nothing changed (no missing
  trace, no missing legend entry).

The 8 preserved exceptions are exercised inside Scenario A
because each lives in a body that's already in the breadth pass.

---

# Scenario A: Representative breadth pass

**Setup:** Plot each of the 6 bodies in heliocentric view with all
shells visible (default checkbox state if it shows everything;
otherwise click "select all shells").

The orange-red shells in the inner bodies are where the warm-tone
Mode 5 flags live. The preserves are also here.

| Body | Bodies you'll see info markers on | Mode 5 flag layers | Preserved layers |
|------|-----------------------------------|--------------------|------------------|
| **Earth** | inner core, outer core, lower mantle, upper mantle, crust, upper atmosphere, ionosphere, magnetosphere, hill sphere + radiation belts | inner core orange-red, lower mantle reddish-brown, upper mantle reddish-brown | **radiation belt (1 of 2)** |
| **Mars** | inner core, outer core, mantle, crust, atmosphere, upper atmosphere, hill sphere | inner core orange-red, mantle reddish-brown | **crust (Mars red)** |
| **Jupiter** | core through hill sphere + rings | Amalthea ring `rgb(180, 120, 100)` | none |
| **Moon** | inner core, outer core, mantle, crust, exosphere, hill sphere | inner core red-orange | **outer core (charcoal red)** |
| **Pluto** | core through hill sphere | none (cores are the preserves) | **core, mantle** |
| **Sun** | core through gravitational shell + Roche limit + Alfven + Streamer Belt | none | **Roche limit** |

(Eris and Venus also have preserved/flagged layers; if Earth/Mars
look fine you can probably skip them. If anything looks off in
Earth or Mars, also check Eris + Venus.)

**Generic checks (apply to every shell in every render):**

| # | Check | What to look for | Pass [ ] |
|---|-------|------------------|:--------:|
| A1 | Info marker presence | One cross marker per shell, at the "top" position (north pole of sphere shells, edge of ring shells) | [ ] |
| A2 | Info marker size | Visibly larger than before (size 8 vs old size 6 -- roughly 1.5x area) | [ ] |
| A3 | Info marker border | Red outline (not white) on all standardized markers | [ ] |
| A4 | Info marker hover | Hover card shows shell name + full description, no regression | [ ] |
| A5 | Geometry trace toggle | Toggling a shell from legend hides BOTH the geometry points AND its info marker (legendgroup preserved) | [ ] |
| A6 | Marker visible against fill | Red border is visible against the marker's own fill color (the standardization purpose) | [ ] |

**Mode 5 specific checks for each render:**

| # | Check | What to look for | Pass [ ] |
|---|-------|------------------|:--------:|
| AE1 | Earth inner_core (orange-red `rgb(255, 180, 140)`) | Red border reads cleanly against the orange-red fill | [ ] |
| AE2 | Earth lower_mantle (reddish-brown `rgb(230, 100, 20)`) | Red border reads cleanly | [ ] |
| AE3 | Earth upper_mantle (reddish-brown `rgb(205, 85, 85)`) | Red border reads cleanly | [ ] |
| AE4 | **Earth radiation belts** | Two belt traces, each with its own info marker. The inner belt (`rgb(255, 100, 100)`) keeps the OLD style (smaller size 6, white border). The outer belt (`rgb(100, 200, 255)`) also keeps the old style -- they share the loop. Hover still shows belt name + description | [ ] |
| AM1 | Mars inner_core (orange-red) | Red border reads cleanly | [ ] |
| AM2 | Mars mantle (reddish-brown `rgb(205, 85, 85)`) | Red border reads cleanly | [ ] |
| AM3 | **Mars crust (Mars red `rgb(188, 39, 50)`)** | Marker is the OLD style (smaller size 6, white border, opacity 0.9). White border reads cleanly against Mars red fill | [ ] |
| AJ1 | Jupiter Amalthea ring (`rgb(180, 120, 100)`) | Red border reads cleanly | [ ] |
| AMo1 | Moon inner_core (red-orange `rgb(255, 100, 0)`) | Red border reads cleanly | [ ] |
| AMo2 | **Moon outer_core (charcoal red `rgb(255, 50, 0)`)** | Marker is the OLD style. White border reads cleanly against charcoal red fill | [ ] |
| AP1 | **Pluto core (`rgb(255, 56, 0)`)** | Marker is the OLD style. White border reads cleanly | [ ] |
| AP2 | **Pluto mantle (`rgb(150, 0, 0)`)** | Marker is the OLD style. White border reads cleanly | [ ] |
| AS1 | **Sun Roche limit (`rgb(200, 60, 60)`)** | Marker is the OLD style. White border reads cleanly. This is the closest case to true red in the sweep -- if any preserve looks marginal it'll be this one | [ ] |

**Optional:**

| # | Check | What to look for | Pass [ ] |
|---|-------|------------------|:--------:|
| AV | Venus inner_core, mantle | Red border on warm-tone fills -- not a preserve, similar to Earth/Mars warm tones | [ ] |
| AE-extra | Eris core (`rgb(187, 63, 63)`), mantle (`rgb(150, 0, 0)`) | Both OLD style preserves. White border reads cleanly | [ ] |

---

# Scenario B: Ring marker fix verification

The previous code computed ring marker position as a degenerate
rotation of `(outer_radius, 0, 0)`. Saturn used X-rotation alone
(no-op), Uranus did X then Y (radius-independent result).
Net effect on screen: all ring info markers collapsed to the
same point (or near-same point) instead of sitting on each
ring's outer edge.

The container-side check confirmed the FIX produces distinct
positions for each ring (7/7 Saturn, 11/11 Uranus). The visual
check confirms the positions look right -- markers actually on
the rings.

## Scenario B1 -- Saturn

**Setup:** Plot Saturn in saturnocentric or heliocentric view
with the ring system enabled. Tilt view (drag) to look at the
ring plane from above and from the side.

**Expected legend entries (relevant subset):**
- `Saturn: D Ring`, `Saturn: C Ring`, `Saturn: B Ring`,
  `Saturn: Cassini Division`, `Saturn: A Ring`, `Saturn: F Ring`,
  `Saturn: G Ring`, `Saturn: E Ring` (7-8 ring legend entries
  depending on what's modeled)

| # | Check | What to look for | Pass [ ] |
|---|-------|------------------|:--------:|
| B1.1 | Distinct ring marker positions | Each ring has its info marker at a DIFFERENT radial distance -- visibly spread out along the ring plane, not stacked on one point | [ ] |
| B1.2 | Markers on the rings | Each ring's info marker sits ON or AT THE OUTER EDGE of its own ring, not floating off-plane or at origin | [ ] |
| B1.3 | Tilt preserved | The ring system is tilted (Saturn's 26.7 deg axial tilt). Markers tilt WITH the rings -- viewing from the side, markers lie in the ring plane, not a flat horizontal plane | [ ] |
| B1.4 | Each marker hovers its own ring | Hovering a marker shows that ring's name + description, no cross-contamination | [ ] |
| B1.5 | Legend toggle | Toggling one ring hides both its trace AND its marker | [ ] |

## Scenario B2 -- Uranus

**Setup:** Plot Uranus in uranicentric or heliocentric view with
the ring system enabled. Uranus rotates nearly on its side (97 deg
tilt), so the rings are nearly perpendicular to the ecliptic.

| # | Check | What to look for | Pass [ ] |
|---|-------|------------------|:--------:|
| B2.1 | Distinct ring marker positions | 11 ring markers at 11 distinct positions along the ring plane | [ ] |
| B2.2 | Markers on the rings | Each marker sits on or at the outer edge of its own ring | [ ] |
| B2.3 | Extreme tilt preserved | Ring system perpendicular to ecliptic; markers tilt WITH the rings (this is the more demanding test because Uranus had the TWO-rotation degenerate computation) | [ ] |
| B2.4 | Each marker hovers its own ring | Hover correctness, no cross-contamination | [ ] |
| B2.5 | Legend toggle | Per-ring toggle hides trace + marker | [ ] |

---

# Scenario C: Dormant call cleanup verification

14 dormant `sun_traces = create_sun_direction_indicator(...)` blocks
were deleted across 6 files. Each was suppressed at runtime
(dist=0 from `center_position=(0, 0, 0)` triggers the function's
own empty-return branch). So deletion should be a no-op visually.

**This is the verification that the v9 handoff's "zero behavior
change" claim was correct.**

**Affected files and shells:**

| File | Deleted from |
|------|-------|
| asteroid_belt | Main Belt, Hildas, Trojan Greeks, Trojan Trojans (4) |
| earth | upper_atmosphere, hill_sphere (2) |
| jupiter | upper_atmosphere, hill_sphere (2) |
| mars | upper_atmosphere, hill_sphere (2) |
| saturn | upper_atmosphere, hill_sphere (2) |
| venus | upper_atmosphere, hill_sphere (2) |

**Setup:** Plot each of these 6 bodies in heliocentric view with
all shells visible. Look at the upper_atmosphere and hill_sphere
shells specifically.

| # | Check | What to look for | Pass [ ] |
|---|-------|------------------|:--------:|
| C1 | No missing sun direction indicator | Compare to a body NOT in the affected list (e.g. neptune, uranus, pluto). The upper_atmosphere and hill_sphere shells should look the same on affected and unaffected bodies -- no missing yellow arrow / direction line | [ ] |
| C2 | No regression on shells themselves | The actual shell geometry (sphere of points) renders correctly with hover info | [ ] |
| C3 | Asteroid belt looks unchanged | Main belt + Hildas + Trojans still render with their density distributions, no missing direction indicator | [ ] |
| C4 | Magnetosphere on Earth unchanged | Earth's magnetosphere DOES get a sun direction indicator (active call at the dispatch level, not removed by this sweep). Confirm it's still there | [ ] |

**Note on C4:** Earth's magnetosphere has a `sun_traces` call at
the old line 867 that was NOT in v9's dormant list and was NOT
deleted by this sweep (out-of-scope decision flagged at the
start of the session). It should continue to render its sun
direction indicator. If Mode 5 wants this revisited, file as a
separate Stage 4 item.

---

# Scenario D (optional, low-risk): Planet 9 hill sphere

`n_points` was normalized from 50 (high resolution, anomalous)
to 25 (modal convention across the codebase). The Planet 9 hill
sphere will look very slightly less smooth.

**Only run if you're curious or skeptical.** No structural
correctness implications.

| # | Check | What to look for | Pass [ ] |
|---|-------|------------------|:--------:|
| D1 | Planet 9 hill sphere still recognizable as a sphere | Slightly less smooth than before; still clearly a sphere | [ ] |
| D2 | Geometry still renders | No crashes, hill sphere still has its info marker | [ ] |

---

# Scenario E (optional): create_info_marker docstring

`orrery_rendering.py` `create_info_marker` docstring was updated
with a migration-intent paragraph. No functional change.

**Only relevant if you're going to read the source for
documentation review.**

| # | Check | What to look for | Pass [ ] |
|---|-------|------------------|:--------:|
| E1 | Docstring describes accomplished state | "All planetary and solar shell modules now use this style..." | [ ] |
| E2 | Module list accurate | 13 modules listed: asteroid_belt, earth, eris, jupiter, mars, moon, neptune, planet9, pluto, saturn, solar, uranus, venus | [ ] |
| E3 | Exception rule documented | "New red-on-red exceptions require an inline comment." | [ ] |

---

## Results template

```
Scenario A -- Breadth pass:
  Generic checks (apply to every shell in every render)
    A1 Info marker presence:                   [ ]
    A2 Info marker size visibly larger:        [ ]
    A3 Red border on standardized markers:     [ ]
    A4 Hover card no regression:               [ ]
    A5 Legend toggle hides both:               [ ]
    A6 Marker visible against fill (general):  [ ]

  Earth specifics
    AE1 inner_core orange-red red border:      [ ]
    AE2 lower_mantle reddish-brown red border: [ ]
    AE3 upper_mantle reddish-brown red border: [ ]
    AE4 radiation belt loop preserved old:     [ ]

  Mars specifics
    AM1 inner_core orange-red red border:      [ ]
    AM2 mantle reddish-brown red border:       [ ]
    AM3 crust preserved old (Mars red):        [ ]

  Jupiter specifics
    AJ1 Amalthea ring red border:              [ ]

  Moon specifics
    AMo1 inner_core red-orange red border:     [ ]
    AMo2 outer_core preserved old (charcoal):  [ ]

  Pluto specifics
    AP1 core preserved old:                    [ ]
    AP2 mantle preserved old:                  [ ]

  Sun specifics
    AS1 Roche limit preserved old:             [ ]

  Optional
    AV  Venus warm tones:                      [ ]
    AE-extra  Eris core + mantle preserved:    [ ]

Scenario B -- Ring marker fix:
  Saturn (B1)
    B1.1 Distinct positions on rings:          [ ]
    B1.2 Markers on the rings:                 [ ]
    B1.3 Tilt preserved:                       [ ]
    B1.4 Hover correctness per ring:           [ ]
    B1.5 Legend toggle:                        [ ]
  Uranus (B2)
    B2.1 Distinct positions on rings:          [ ]
    B2.2 Markers on the rings:                 [ ]
    B2.3 Extreme tilt preserved:               [ ]
    B2.4 Hover correctness per ring:           [ ]
    B2.5 Legend toggle:                        [ ]

Scenario C -- Dormant cleanup:
  C1 No missing sun direction indicator:       [ ]
  C2 No regression on shells:                  [ ]
  C3 Asteroid belt unchanged:                  [ ]
  C4 Earth magnetosphere sun indicator kept:   [ ]

Scenario D (optional) -- Planet 9 normalization:
  D1 Hill sphere still recognizable:           [ ]
  D2 Geometry still renders:                   [ ]

Scenario E (optional) -- Docstring:
  E1 Migration-intent paragraph present:       [ ]
  E2 Module list accurate:                     [ ]
  E3 Exception rule documented:                [ ]

Notes / anomalies / Mode 5 reversal candidates:
```

---

## After testing

**If all checks pass:**
1. Stage 3 sweep is complete; 14 files ready to deploy.
2. Suggested commit message (one line):
   `Stage 3 sweep (D3.1 v13): info marker standard + Sun Direction cleanup + ring marker fix. 73 conversions, 8 exceptions, 14 dormant calls + 6 imports removed, Saturn/Uranus ring placement fixed.`
3. Regenerate `MODULE_ATLAS.md` (credit-line changes on 14 modules).
4. Run `provenance_scanner.py` -- no source citations touched, expecting clean.
5. Write handoff v13 documenting the session and the
   "preserve-via-inline-comment" technique.
6. Next session entry: Stage 4 from v12 deferred list
   (`idealized_orbits.py:7331` color fix, center body no-shells
   edge case, Jupiter/Saturn bow shocks, Shell Resolution GUI,
   Studio editor comprehensive review).

**If any Mode 5 check fails (warm-tone contrast):**

The reversal is one line per site. Locate the marker dict
(grep for the unique fill color), change:

```python
marker=dict(size=8, color='<the fill>', opacity=1.0,
            symbol='cross', line=dict(color='red', width=2)),
```

back to:

```python
marker=dict(size=6, color='<the fill>', opacity=0.9,
            symbol='cross', line=dict(color='white', width=1)),
```

Add a comment noting the Mode 5 reversal:

```python
# NOTE: red-on-red exception (Mode 5 reversal May 28, 2026) --
# <fill color> reads muddy against a red border.
```

**If any Scenario B (ring) check fails:**
- Distinct positions but wrong plane: tilt/rotation logic wasn't
  the only thing wrong. Check that `x_final, y_final, z_final`
  is in scope at the marker call site (it should be -- the
  ring trace immediately above uses it).
- Single position (regression to old behavior): the
  `str_replace` didn't land. Check Saturn line ~1170 area and
  Uranus line ~1060 area for the new code.

**If any Scenario C (dormant cleanup) check fails:**
- Missing direction indicator on upper_atmosphere or
  hill_sphere of an affected body: the v9 "zero behavior
  change" claim was wrong. Restore the deleted block from
  `/mnt/project/<file>` (the project snapshot still has it).
  This would be a significant finding -- file as a lesson.

---

## What this protocol is NOT testing

- **Per-marker color of every individual conversion** -- the
  factory pattern is uniform; spot-check via Scenario A.
- **The `n_points=20/25/50` convention itself** -- only Planet 9
  was an outlier; the rest of the codebase is unchanged.
- **The `create_info_marker` factory function** -- already in
  use across the codebase since v3.18 (April 2026). Sweep only
  added the docstring paragraph.
- **`palomas_orrery.py` GUI behavior** -- no edits to GUI code
  in this sweep. Standard regression "does the dashboard still
  launch and plot" is sufficient.
- **Studio source vs export distinction** -- no Studio edits.

---

*"Tony's eyes win."*

*Module updated: May 27, 2026 with Anthropic's Claude Opus 4.7*
*(Stage 3 sweep test protocol v1: 73 conversions, 8 preserves,*
*2 ring fixes, 14 dormant deletions, 1 normalization)*
