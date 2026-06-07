# D3.1 Sweep -- Testing Protocol (v2, post-runtime-fix)

**Date:** May 23, 2026
**Tester:** Tony Quintanilla
**Mode:** Mode 5 (visual verification -- Tony leads)
**Files changed:** 15 `*_visualization_shells.py`

---

## What changed since v1

The original protocol assumed all 15 files had been swept on May 22.
Runtime verification on May 23 found that `earth_visualization_shells.py`
was entirely skipped by Batches 4 and 5 in the May 22 session. The
Earth fix was applied in a separate session on May 23 -- 15 edits, all
runtime-verified.

**The 8-render protocol below is unchanged in structure.** What is new:

1. **All 15 files have passed runtime smoke testing.** Trace
   construction returns the expected hover headers and legendgroup
   wiring across 355 traces. The runtime test is necessary but not
   sufficient -- Mode 5 still owns layout, redundancy judgment, and
   any subjective visual issues.

2. **Render 2 (Earth) gets a known-double-header advisory** because
   the prepend introduces three cases where the legend label header
   sits above a prose lead-in that also names the feature. These are
   intentional and structurally correct; the question for Mode 5 is
   whether any of them look ugly.

3. **Runtime smoke testing is the new first-line gate.** Before any
   future sweep is delivered for Mode 5 verification, the constructor
   smoke test must pass. Compile-clean alone does not establish that
   a file has actually been modified.

---

## Pre-test: Drop files into working directory

Copy all 15 files into `palomas_orrery_for_github/`. Overwrite existing.
Confirm no import errors on launch before starting visual checks.

---

## What the sweep changed (what you're verifying)

1. **Rule 2 prepend:** Every info marker hover now starts with its
   legend label as a header, separated by a blank line (`<br><br>`)
   from the description body.

2. **Newline normalization:** All `\n` in hover strings replaced with
   `<br>`. Previously, some hovers truncated at the first `\n` in
   Plotly's HTML renderer.

3. **Legendgroup wiring (Batches 1-4):** Solar labels renamed to
   `"Sun: X"`, Neptune diamond hidden from legend, comet placeholders
   get explicit legendgroups, crust/cloud surface traces linked to
   their info markers, Moon Hill Sphere renamed.

---

## Test structure

Eight representative renders. Each tests a different batch or pattern.
For each render, check the four verification criteria, then mark
pass/fail. Stop and note any anomaly -- don't fix in place.

### The four checks (apply to every render)

| # | Check | What to look for |
|---|-------|------------------|
| A | **Header present** | Hover starts with the legend label (e.g., "Mercury: Magnetosphere") |
| B | **Blank line gap** | Visible blank line between header and description body |
| C | **No literal `\n`** | No truncated or garbled text where `\n` was |
| D | **Legend toggle** | Clicking the legend entry hides BOTH the geometry AND the info marker cross |

---

## Render 1: Mercury (Batch 5 Pattern A + \n normalization)

**Setup:** Render Mercury. Set manual scale to at least 0.002 AU.

**Hover targets:**
- Sodium Tail info marker (cross near tail origin)
- Magnetosphere info marker
- Bow Shock info marker

**Specific concern:** Mercury had `\n` in its config-dict description
strings (the `_info` tuples at the top of the file). These feed the
GUI tooltips, not the Plotly hover -- but verify the Plotly hovers
are clean regardless.

**Check A/B/C/D on each hover target.**

---

## Render 2: Earth (Batch 4 + Batch 5 -- runtime-fixed May 23)

**Status note:** Earth was fixed in a separate session on May 23 after
runtime verification revealed it had been skipped on May 22. All 15
edits (2 Batch 4 + 13 Batch 5) are runtime-verified. Spot-checks
confirm:

- Crust surface and info marker now share `legendgroup="Earth: Crust"`
  (Batch 4 toggle linkage works)
- All 11 builders produce info markers leading with
  `"Earth: <label><br><br>"`
- Magnetosphere builder produces all 4 expected info markers with
  correct headers (Magnetosphere, Bow Shock, Inner Radiation Belt,
  Outer Radiation Belt)

**Setup:** Render Earth. Set manual scale to at least 0.001 AU for
inner shells.

**Hover targets:**
- Any crust shell info marker (cross on the surface sphere) --
  this tests the Batch 4 legendgroup fix + Batch 5 prepend
- LEO shell info marker
- Geostationary Belt info marker
- Hill Sphere info marker
- Magnetosphere info marker (4 markers in this one builder:
  magnetosphere envelope, bow shock, inner Van Allen, outer Van Allen)

**Specific concerns:**
- Crust shell: does the legend entry now toggle BOTH the Mesh3d
  surface AND the cross info marker?
- LEO/GEO/Hill Sphere: these used `hover_text` variable, not
  `layer_info` -- verify the prepend landed correctly.
- Earth had the most `\n` instances (74) -- check C carefully.

**Earth-specific double-header advisory (intentional, evaluate for ugliness):**

The May 23 prepend introduces three cases where the legend label
header sits above a prose lead-in that also names the feature:

| Builder | Header | Prose lead-in | Verdict (Mode 5) |
|---------|--------|---------------|------------------|
| Crust | `Earth: Crust` | `Earth Crust` | ? |
| LEO | `Earth: Low Earth Orbit (LEO)` | `Low Earth Orbit (LEO)` | ? |
| GEO | `Earth: Geostationary Belt (GEO)` | `Geostationary Belt (GEO)` | ? |

These are structurally correct. The question is whether the redundancy
looks bad. If any of the three is ugly, the fix is to edit the
description prose to remove the redundancy -- a content change, not
a structural one.

The other 8 Earth hovers (inner core, outer core, lower mantle, upper
mantle, atmosphere, upper atmosphere, magnetosphere internals, Hill
Sphere) flow cleanly from header into prose with no name repetition.

**Check A/B/C/D on each hover target.**

---

## Render 3: Jupiter (Batch 5 Pattern C loops)

**Setup:** Render Jupiter.

**Hover targets:**
- Magnetosphere info marker
- Io Plasma Torus info marker
- Any radiation belt info marker (there are multiple per loop)
- Any ring info marker

**Specific concern:** Radiation belts and rings are loop-generated
(Pattern C). The prepend used `belt_names[i]` and
`f"Jupiter: {ring_info['name']}"` respectively. Verify the label
matches the actual legend entry for each.

**Check A/B/C/D on each hover target.**

---

## Render 4: Neptune (Batch 2 + Batch 5, items 44-46)

**Setup:** Render Neptune.

**Hover targets:**
- Magnetosphere info marker -- this was item 44 (`\n` truncation).
  The hover should now show the FULL description, not cut off.
- Magnetic Field Center diamond marker -- should show
  "Neptune: Magnetic Field Center" header. This diamond should
  NOT appear as a separate legend entry (Batch 2 fix).
- Any radiation belt info marker -- item 45
- Any FAC (field-aligned current) info marker -- item 46
- Any ring/arc info marker

**Specific concerns:**
- The Magnetosphere legend entry: clicking it should hide the
  envelope geometry, the diamond marker, AND the magnetosphere
  info marker cross (all share `legendgroup='Neptune: Magnetosphere'`).
- The diamond should be INVISIBLE in the legend sidebar but still
  visible in the plot and hoverable.

**Check A/B/C/D on each hover target.**

---

## Render 5: Solar / Oort Cloud (Batch 1 renames + Batch 5)

**Setup:** Render the Sun. You'll need various scales to see
different shells.

**Hover targets:**
- Any renamed shell: "Sun: Heliopause", "Sun: Termination Shock",
  "Sun: Gravitational Influence" (was "Sun's Gravitational Influence")
- Any Oort Cloud shell
- Hills Cloud (toroidal)
- Galactic Tide Region

**Specific concerns:**
- Legend entries should all read "Sun: X" (no "Solar Wind Heliopause",
  no "Sun's Gravitational Influence"). 9 renames in Batch 1.
- Solar had the most `\n` instances (388 in config dicts). Verify
  hovers are clean.
- The config-dict descriptions (with `\n`) feed GUI tooltips via
  `globals()`. Those tooltips are a separate rendering path -- if
  they look different from the Plotly hovers, that's expected (the
  config dicts were NOT changed, only the Plotly hover strings were).

**Check A/B/C/D on a sample of 3-4 hover targets.**

---

## Render 6: MAPS Comet (Batch 2 legendgroups + Batch 5)

**Setup:** Render MAPS. Since MAPS disintegrated, you'll see
placeholder legend entries for inactive features.

**Hover targets:**
- Disintegration diamond marker
- Ghost Tail info marker (cross on the debris arc)
- Nucleus placeholder (if visible -- disintegrated)

**Specific concerns:**
- Each inactive placeholder ("MAPS: Coma (inactive, >X AU)",
  "MAPS: Dust Tail (inactive, >X AU)", etc.) should now have an
  explicit `legendgroup`. Toggling one should NOT toggle others.
- The Disintegration marker hover should start with
  "MAPS: Disintegration" header.
- Ghost Tail hover already had a `<b>` header in the old code.
  It now has the legend label prepended BEFORE that bold header.
  Check that this doesn't look redundant or ugly. If it does,
  note it -- we can adjust.
- **Note for the runtime smoke test:** Ghost Tail's legendgroup
  uses snake_case (`maps_ghost_tail`) while the hover correctly
  uses the display name. The runtime test reports this as an R2
  miss, but it is intentional and not a real failure.

**Check A/B/C/D on each hover target.**

---

## Render 7: Moon (Batch 3 rename + Batch 5)

**Setup:** Render Moon. Set scale to ~0.001 AU.

**Hover targets:**
- Hill Sphere info marker -- legend should read "Moon: Hill Sphere"
  (was "Hill Sphere" before Batch 3)
- Any crust shell info marker (Batch 4 + Batch 5)

**Specific concern:** The rename was a single `trace_name` edit
that flows into both `name=` and `legendgroup=`. Verify the legend
sidebar shows "Moon: Hill Sphere", not "Hill Sphere".

**Check A/B/C/D.**

---

## Render 8: Asteroid Belt (Batch 5 -- category file)

**Setup:** Render with asteroid belt populations visible.

**Hover targets:**
- Main Asteroid Belt info marker
- Hilda Family info marker
- Jupiter Trojans (Greeks - L4) info marker

**Specific concern:** Category file -- no body prefix. The legend
label IS the population name ("Hilda Family", etc.). The prepend
should use that name as the header. Verify it doesn't say
"Asteroid Belt: Hilda Family" or similar -- just "Hilda Family".

**Check A/B/C/D.**

---

## Results template

```
Render 1 (Mercury):     A[ ] B[ ] C[ ] D[ ]  Notes:
Render 2 (Earth):        A[ ] B[ ] C[ ] D[ ]  Notes:
  Crust double-header:    looks OK [ ]  needs prose edit [ ]
  LEO double-header:      looks OK [ ]  needs prose edit [ ]
  GEO double-header:      looks OK [ ]  needs prose edit [ ]
Render 3 (Jupiter):      A[ ] B[ ] C[ ] D[ ]  Notes:
Render 4 (Neptune):      A[ ] B[ ] C[ ] D[ ]  Notes:
Render 5 (Solar):        A[ ] B[ ] C[ ] D[ ]  Notes:
Render 6 (MAPS):         A[ ] B[ ] C[ ] D[ ]  Notes:
Render 7 (Moon):         A[ ] B[ ] C[ ] D[ ]  Notes:
Render 8 (Asteroid):     A[ ] B[ ] C[ ] D[ ]  Notes:
```

---

## Edge cases to watch for (not render-specific)

- **Double headers:** Some descriptions already started with the
  feature name in prose (e.g., "Magnetosphere: Mercury has a
  surprisingly active..."). The prepend adds the legend label ABOVE
  that. The result is: `Mercury: Magnetosphere` (header) then blank
  line then `Magnetosphere: Mercury has a surprisingly active...`.
  This is intentional and correct -- the legend label header is
  structural, the prose lead-in is content. But if it looks bad,
  note which ones. (Earth's three specific cases are called out in
  Render 2; other bodies may have similar patterns.)

- **Very long hovers:** Some hovers (Mercury magnetosphere, solar
  shells) are extremely long. The prepended header should still be
  visible at the top without scrolling. If the hover box is so long
  it runs off-screen, note it.

- **Ghost Tail redundancy:** The ghost tail hover had an existing
  `<b>MAPS: Ghost Tail (debris arc)</b>` line. The prepend adds
  `MAPS: Ghost Tail (April 4-6)` above it. Two similar-looking
  headers. Note if this is ugly.

---

## After testing

If all 8 renders pass A/B/C/D: D3.1 is done. Deploy to GitHub.

If any fail: note the specific render, check letter, and what you
see. Screenshot if possible. We fix in the next session.

---

*"The script's Rule 2 check is a weak proxy. Real verification*
*is Mode 5 visual." -- D3.1 Mode 7 lesson*

*"Compile-only verification is the absence of a runtime test, not*
*a substitute for one." -- D3.1 runtime-fix lesson, May 23, 2026*
