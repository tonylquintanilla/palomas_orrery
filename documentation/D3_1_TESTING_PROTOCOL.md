# D3.1 Sweep -- Testing Protocol

**Date:** May 23, 2026
**Tester:** Tony Quintanilla
**Mode:** Mode 5 (visual verification -- Tony leads)
**Files changed:** 15 `*_visualization_shells.py`

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

## Render 2: Earth (Batch 4 + Batch 5 Pattern B)

**Setup:** Render Earth. Set manual scale to at least 0.001 AU for
inner shells.

**Hover targets:**
- Any crust shell info marker (cross on the surface sphere) --
  this tests the Batch 4 legendgroup fix + Batch 5 prepend
- LEO shell info marker
- Geostationary Belt info marker
- Hill Sphere info marker

**Specific concerns:**
- Crust shell: does the legend entry now toggle BOTH the Mesh3d
  surface AND the cross info marker? (This is the Batch 4 fix.)
- LEO/GEO: these used `hover_text` variable, not `layer_info` --
  verify the prepend landed correctly.
- Earth had the most `\n` instances (74) -- check C carefully.

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
  note which ones.

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
