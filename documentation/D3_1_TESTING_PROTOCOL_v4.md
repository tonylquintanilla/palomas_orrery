# D3.1 Sweep -- Testing Protocol (v4, Sun Direction fix verification)

**Date:** May 25, 2026
**Tester:** Tony Quintanilla
**Mode:** Mode 5 (visual verification -- Tony leads)
**Files changed since v3 testing:** `planet_visualization.py` +
`shared_utilities.py` (3 edits total)

---

## What changed since v3

The May 25 session executed Mode 5 visual testing of v3 and found
two cross-cutting structural bugs in the Sun Direction indicator,
not 8+ independent bugs as Tony's notes initially suggested.

**Bug 1:** Sun Direction indicator suppressed when only custom shells
(magnetosphere, rings, radiation belts, LEO/GEO, plasma torus, FACs)
are selected. The dispatch loop tracked `outermost_radius_au` only in
the SHELL_CONFIGS branch.

**Bug 2:** Multi-body Sun Direction indicators all named "Sun Direction"
with the same legendgroup. Earth + Moon in barycenter view showed one
toggleable entry instead of two distinct ones.

Both were fixed in two files. Functional tests against the live
dispatch pass 4/4 scenarios + backward compatibility. **This protocol
is the Mode 5 verification gate** before deploying to GitHub and
proceeding to the remaining 6 items in the next session.

---

## Pre-test: Drop files into working directory

Copy these into `palomas_orrery_for_github/`. Overwrite existing.

| File | From | Notes |
|------|------|-------|
| `planet_visualization.py` | **May 25 session** | Bug 1 fallback + Bug 2 pass-through |
| `shared_utilities.py` | **May 25 session** | Bug 2 body_name parameter |

Confirm no import errors on launch before starting visual checks.

---

## Test structure

This is a **focused gate**, not a full re-run of the v3 8-render
protocol. The Sun Direction structural fix changes one specific aspect
of the dispatch -- whether and how the indicator appears -- across
every body with custom shells. The v3 protocol's other observations
(Rule 2 headers, double-headers, legendgroup toggles) were either
verified clean by Tony's notes or noted as content edits deferred to
the next session.

**Three test groups:**

1. **Group A -- Custom-only renders (Bug 1 fix).** For each body with
   custom shells, select ONLY the magnetosphere checkbox (and/or
   radiation belts / rings / LEO/GEO / plasma torus / FACs). Verify
   the Sun Direction indicator now appears. -- verified

2. **Group B -- Multi-body renders (Bug 2 fix).** Render Earth-Moon at
   the barycenter, with custom shells on both bodies. Verify two
   distinct Sun Direction indicators. -- verified

3. **Group C -- No-regression sanity (Scenarios 1 + 2 of the functional
   test, but with eyes).** Verify that body-centered renders still
   suppress the indicator correctly, and heliocentric sphere-shell
   renders still show one indicator. -- verified

---

## The single check (applied to every test)

| # | Check | What to look for |
|---|-------|------------------|
| S | **Sun Direction state** | Indicator present (line + cross) OR correctly absent; legend label correct |

Three possible states for each test:

| State | When correct |
|-------|--------------|
| 1 indicator, body-prefixed name | Heliocentric / barycenter view, body off-origin |
| 0 indicators (suppressed) | Body-centered view (body at origin = same as Sun position) |
| 2+ distinct indicators | Multi-body render in barycenter / other non-origin view |

---

# Group A: Custom-only renders (Bug 1 fix)

For each of the 8 bodies below, render the body in **heliocentric
view** (Sun at center, body offset). Select ONLY the listed custom
shell checkbox(es) -- no sphere shells (no core, mantle, crust,
atmosphere, hill_sphere).

**Expected result for every test in Group A:** 1 Sun Direction
indicator present, labelled `"<Body>: Sun Direction"`.

| # | Body | Custom shells to select | Pass [ ] |
|---|------|-------------------------|:--------:|
| A1 | Mercury | Magnetosphere | [ ] |
| A2 | Venus | Magnetosphere (+ Bow Shock) | [ ] |
| A3 | Earth | Magnetosphere | [ ] |
| A3a | Earth | LEO only | [ ] |
| A3b | Earth | Geostationary Belt only | [ ] |
| A4 | Mars | Magnetosphere (Induced) | [ ] |
| A5 | Jupiter | Magnetosphere | [ ] |
| A5a | Jupiter | Io Plasma Torus | [ ] |
| A5b | Jupiter | Radiation Belts | [ ] |
| A5c | Jupiter | Ring System | [ ] |
| A6 | Saturn | Magnetosphere | [ ] |
| A6a | Saturn | Plasma Torus | [ ] |
| A6b | Saturn | Radiation Belts | [ ] |
| A6c | Saturn | Ring System | [ ] |
| A7 | Uranus | Magnetosphere | [ ] |
| A7a | Uranus | Radiation Belts | [ ] |
| A7b | Uranus | Ring System | [ ] |
| A8 | Neptune | Magnetosphere | [ ] |
| A8a | Neptune | Radiation Belts | [ ] |
| A8b | Neptune | Ring/Arc System | [ ] |

**Notes for Group A:**

- The indicator scale will be approximately 100x body radius. For
  Earth this is ~0.005 AU (Bug 1 functional test confirmed). For
  Jupiter, scale is much larger (~7 million km). Visible, but smaller
  than the full magnetosphere extent. This is intentional -- the
  indicator is a direction marker, not a size marker.

- If the indicator does not appear: capture the body and shell
  selection, note "FAIL Group A row X." The fallback may need
  adjustment if a body's radius isn't in CENTER_BODY_RADII.

- If two indicators appear for a single body: there is a residual
  legacy call firing somewhere. Note which body and which shells were
  selected.

---

# Group B: Multi-body renders (Bug 2 fix)

## B1 -- Earth-Moon system at barycenter

**Setup:** Render the Earth-Moon system with the Earth-Moon
barycenter as the center object. Enable shells for both bodies:

- Earth: Magnetosphere
- Moon: Hill Sphere

**Expected:**

- **2 separate legend entries**: `"Earth: Sun Direction"` and
  `"Moon: Sun Direction"`.
- Each entry toggles independently (click "Earth: Sun Direction" --
  Earth's indicator hides, Moon's stays).
- Both indicators point toward the actual Sun position (not toward
  the barycenter).

**Specific checks:**

| Check | Pass [ ] |
|-------|:--------:|
| B1a | Two distinct legend entries with body-prefixed names | [ ] |
| B1b | Each toggles independently | [ ] |
| B1c | Each points outward from its body toward the Sun (not toward barycenter origin) | [ ] |

## B2 -- Earth alone in heliocentric view (cross-check from B1)

This is the same as Group A row A3 but worth re-running back-to-back
with B1 to compare legend labels.

**Expected:** Single legend entry `"Earth: Sun Direction"`.

| Check | Pass [ ] |
|-------|:--------:|
| B2 | Earth's solo legend entry matches Earth's name in B1 (consistent labeling) | [ ] |

---

# Group C: No-regression sanity

## C1 -- Body-centered view, body at origin

**Setup:** Render Earth, with Earth at the origin (body-centered
view). Select any shells.

**Expected:** **0 Sun Direction indicators** (suppressed because
`dist = 0`, no meaningful sunward direction).

| Check | Pass [ ] |
|-------|:--------:|
| C1 | No Sun Direction indicator in legend or plot | [ ] |

## C2 -- Heliocentric view, sphere shells only

**Setup:** Render Earth in heliocentric view (Sun at origin). Select
only sphere shells: Crust, Atmosphere, Hill Sphere. No magnetosphere.

**Expected:** **1 Sun Direction indicator**, labelled
`"Earth: Sun Direction"`. Scaled to outermost active sphere shell
(Hill Sphere if selected). No Bug 1 fallback triggered.

| Check | Pass [ ] |
|-------|:--------:|
| C2 | Single indicator, body-prefixed name, scaled to outermost sphere | [ ] |

## C3 -- Mixed sphere + custom shells

**Setup:** Render Earth in heliocentric view. Select Crust +
Magnetosphere together.

**Expected:** **1 Sun Direction indicator** (not 2), scaled to the
larger of the two -- in this case, the magnetosphere fallback OR the
Crust radius, whichever is larger. The dispatch picks one indicator
per body regardless of how many shells are selected.

| Check | Pass [ ] |
|-------|:--------:|
| C3 | Single indicator, not duplicated | [ ] |

## C4 -- Asteroid belt (no indicator expected, backward-compat) -- verified

**Setup:** Render the asteroid belt populations from any view.

**Expected:** **0 Sun Direction indicators** from any asteroid belt
population (Main Belt, Hilda, Trojans). These are heliocentric ring
populations -- the indicator is meaningless and correctly suppressed.

| Check | Pass [ ] |
|-------|:--------:|
| C4 | No "Sun Direction" or population-prefixed Sun Direction in asteroid belt renders | [ ] |

## C5 -- Comet render (indicator should still work)

**Setup:** Render an active comet (3I/ATLAS or any active comet, not
MAPS post-disintegration).

**Expected:** **1 Sun Direction indicator** for the comet, currently
labelled generic `"Sun Direction"` (backward-compat -- comet calls do
not yet pass body_name; this is a deferred enhancement). -- correct

| Check | Pass [ ] |
|-------|:--------:|
| C5 | Comet indicator present (label may be generic "Sun Direction") | [ ] |

---

## Results template

```
Group A -- Custom-only renders (8+ rows):
  A1 Mercury Magnetosphere:                [ ]
  A2 Venus Magnetosphere:                  [ ]
  A3 Earth Magnetosphere:                  [ ]
  A3a Earth LEO only:                      [ ]
  A3b Earth Geostationary only:            [ ]
  A4 Mars Magnetosphere (Induced):         [ ]
  A5 Jupiter Magnetosphere:                [ ]
  A5a Jupiter Io Plasma Torus:             [ ]
  A5b Jupiter Radiation Belts:             [ ]
  A5c Jupiter Ring System:                 [ ]
  A6 Saturn Magnetosphere:                 [ ]
  A6a Saturn Plasma Torus:                 [ ]
  A6b Saturn Radiation Belts:              [ ]
  A6c Saturn Ring System:                  [ ]
  A7 Uranus Magnetosphere:                 [ ]
  A7a Uranus Radiation Belts:              [ ]
  A7b Uranus Ring System:                  [ ]
  A8 Neptune Magnetosphere:                [ ]
  A8a Neptune Radiation Belts:             [ ]
  A8b Neptune Ring/Arc System:             [ ]

Group B -- Multi-body renders:
  B1a Two distinct legend entries:         [ ]
  B1b Toggles independently:               [ ]
  B1c Points toward actual Sun:            [ ]
  B2  Earth solo label matches B1 Earth:   [ ]

Group C -- No-regression sanity:
  C1 Body-centered: no indicator:          [ ]
  C2 Helio sphere only: 1 indicator:       [ ]
  C3 Mixed sphere+custom: 1 indicator:     [ ]
  C4 Asteroid belt: no indicators:         [ ]
  C5 Comet: indicator present:             [ ]

Notes / anomalies:
```

---

## After testing

If all checks pass:
1. The Sun Direction structural fix is complete.
2. Deploy intermediate state to GitHub (D3.1 sweep + dispatch-path fix
   + Sun Direction fix).
3. Proceed in next session to the 6 remaining items in the handoff
   queue:
   - Hover font size (`create_info_marker`)
   - Mars Induced Magnetosphere missing info marker
   - Neptune ring/arc markers superimposed
   - MAPS disintegration marker symbol (diamond -> square-open)
   - MAPS ghost tail width
   - MAPS post-disintegration hover text clarity

If any check fails: note the row, what was observed, screenshot if
possible. Diagnose in next session before deploying.

---

## What this protocol is NOT testing

- **Rule 2 headers:** verified by Tony's v3 testing already (all rows
  in v3 passed A/B/C/D except where deferred to content edits).
- **Double-headers:** marked "acceptable" by Tony in v3 protocol.
- **Hover overflow:** queued as item 1 in the next session (font size
  fix in `create_info_marker`).
- **Mars Induced Magnetosphere info marker:** queued as item 2.
- **Neptune ring/arc marker positions:** queued as item 3.
- **MAPS comet items:** queued as items 4-6.

These were intentionally separated from the Sun Direction gate so
that the structural fix can be verified or rejected in isolation. If
Sun Direction fails, the other items don't get tested. If it passes,
they become the next sub-batch.

---

*"The framing question collapses the scope."*
*-- Tony, May 25, 2026, on "do these heliocentric populations even*
*need a Sun Direction indicator?"*

*"It already does the right thing by accident."*
*-- D3.1 Sun Direction lesson, on the asteroid belt's 4 dead calls*

*"Tony's eyes win."* -- still.
