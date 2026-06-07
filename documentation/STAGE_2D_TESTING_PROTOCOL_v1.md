# Stage 2 Item 2D -- Testing Protocol (v1, MAPS marker / ghost tail / hover text)

**Date:** May 26, 2026
**Tester:** Tony Quintanilla
**Mode:** Mode 5 (visual verification -- Tony leads)
**File changed:** `comet_visualization_shells.py` (3 edits)

---

## What changed

Three edits closing Stage 2 items 4, 5, 6 from the v11 handoff. All
in `comet_visualization_shells.py`, all MAPS-specific, all content
edits.

| Item | Function | Change |
|------|----------|--------|
| 4 | `create_maps_disintegration_marker` | symbol `diamond` -> `square-open`; `size` 8 -> 10; `line=dict(color='white', width=1)` removed |
| 5 | `create_maps_ghost_tail_trace` | segment `width` 3 -> 5 |
| 6 | post-disintegration block (lines 1747-1767) | info-trace hover header now reads "MAPS: Dust Trail (Remains)" / "MAPS: Ion Trail (Remains)" instead of "Dust Tail" / "Ion Tail" |

Smoke test passed (import + function exercise verified each change
landed at the value level). This protocol is the Mode 5 visual gate.

---

## Test structure

Two date scenarios in the orrery, one optional gallery check.

- **Scenario A** -- Pre-disintegration date. Renders active MAPS
  (nucleus + coma + active tails) plus the always-on disintegration
  marker + ghost tail. Tests items 4 and 5.
- **Scenario B** -- Post-disintegration date. Renders the headless
  ghost (no nucleus, no coma, scaled-down "Remains" trails) plus the
  disintegration marker + ghost tail. Tests items 4, 5, and 6.
- **Scenario C** (optional) -- Gallery portrait card. Tests that the
  Item 6 hover text update propagates through the gallery router.

The disintegration marker and ghost tail are added unconditionally
when MAPS is rendered (see lines 1729-1734), so they appear in both A
and B regardless of date.

---

# Scenario A: Pre-disintegration

**Setup:** Plot MAPS in heliocentric view at any date BEFORE
April 4, 2026 08:15 UTC. Suggested: April 3, 2026 (one day before).
Or use the "Go: Perihelion Prediction" preset if it sets a
pre-disintegration date.

**Expected legend entries (relevant subset):**
- `MAPS: Nucleus`
- `MAPS: Coma` (if within feature distance)
- `MAPS: Dust Tail`, `MAPS: Ion Tail` (if active)
- `MAPS: Disintegration` (always)
- `MAPS: Ghost Tail (April 4-6)` (always)

| # | Check | What to look for | Pass [ ] |
|---|-------|------------------|:--------:|
| A1 | Disintegration marker shape | Open green square (not a filled diamond) at the disintegration point | [ ] | -- correct
| A2 | Disintegration marker size | Visibly readable -- roughly comparable to the prior filled diamond, perhaps marginally smaller due to open vs filled | [ ] | -- correct
| A3 | Disintegration marker outline | Green outline (no white inner border) | [ ] | -- correct
| A4 | Distinguishable from nucleus | The active MAPS nucleus (filled diamond) and the disintegration marker (open square) are clearly different shapes side-by-side | [ ] | -- correct
| A5 | Ghost tail thickness | Ghost tail segments are visibly thicker than the underlying perihelion osculating orbit trace | [ ] | -- the color difference is slight. maybe change the ghost tail trace color to red for clarity. it has nothing to do with the actual tail color. 
| A6 | Ghost tail color/fade | Bright green at disintegration end, fading toward dispersal end (no regression from prior render) | [ ] | -- okay except this is very difficult to discern. maybe red would help.
| A7 | Ghost tail toggle | Clicking `MAPS: Ghost Tail (April 4-6)` in legend hides all 39 segments at once | [ ] | -- when i toggled off the ghost tail trace, there was a long lag. then i toggled it back on and all the traces toggled off at once! after a long lag the ghost tail rendered again but all the other traces remained off. this is unexpected behavior and should be addressed. i had to close and replot the visualization to proceed with testing. 
| A8 | Disintegration marker hover | Hovering shows full hover card starting with "MAPS: Disintegration" header (no regression) | [ ] | -- correct

---

# Scenario B: Post-disintegration

**Setup:** Plot MAPS in heliocentric view at any date ON OR AFTER
April 4, 2026 08:15 UTC. Suggested: April 5, 2026 (one day after).
Or use the "Go: Disintegration" preset if it sets a post-
disintegration date.

**Expected legend entries (relevant subset):**
- `MAPS: Nucleus (disintegrated April 4, 2026)` (placeholder, no marker)
- `MAPS: Dust Trail (Remains)` (scaled-down dust)
- `MAPS: Ion Trail (Remains)` (scaled-down ion)
- `MAPS: Disintegration` (always)
- `MAPS: Ghost Tail (April 4-6)` (always)
- No `MAPS: Coma` entry

| # | Check | What to look for | Pass [ ] |
|---|-------|------------------|:--------:|
| B1 | No nucleus marker rendered | The placeholder legend entry exists but no actual marker on plot | [ ] | -- correct
| B2 | Trail (Remains) legend labels | Legend shows `MAPS: Dust Trail (Remains)` and `MAPS: Ion Trail (Remains)` -- no regression from v10 | [ ] | -- correct, except that the hovertext markers are superimposed and require toggling on/off to see separately
| B3 | **Item 6 -- Dust Trail hover header** | Hovering over the dust trail info marker (the green `+` cross) shows hover card with header "MAPS: Dust Trail (Remains)" -- NOT "MAPS: Dust Tail" | [ ] | -- correct
| B4 | **Item 6 -- Ion Trail hover header** | Hovering over the ion trail info marker shows hover card with header "MAPS: Ion Trail (Remains)" -- NOT "MAPS: Ion Tail" | [ ] | -- correct
| B5 | Hover body description unchanged | Hover body still reads the active-tail physics text (this is intentional per scope question 2; flagged for separate consideration) | [ ] | -- correct
| B6 | Disintegration marker | Same as A1-A4 -- open green square, distinct from any other marker | [ ] | -- correct
| B7 | Ghost tail | Same as A5-A7 -- visibly thicker than the underlying osculating trace | [ ] | -- correct, except as noted above

---

# Scenario C (optional): Gallery portrait card -- please add this to deferred items. we should do a comprehensive studio editor review at some point. 

**Only run if you're planning a near-term gallery push.** This
confirms the gallery router picks up the Item 6 hover text change
correctly.

**Setup:**
1. Save the Scenario B render as HTML.
2. Load it in Gallery Studio with `route_hover_to_panel: true` in
   the studio config (default for portrait/mobile gallery exports).
3. Export the studio version.
4. Open the exported HTML in portrait orientation (mobile or
   narrow desktop window).
5. Click the dust trail info marker, then the ion trail info marker.

**Expected:** The info card's title field reads `MAPS: Dust Trail
(Remains)` / `MAPS: Ion Trail (Remains)` -- because the router's
`_parse_hover_html` re-derives the name from the first `<br>`-split
segment of `trace.text`, which now contains the "(Remains)" suffix.

| # | Check | Pass [ ] |
|---|-------|:--------:|
| C1 | Dust trail info card title shows "MAPS: Dust Trail (Remains)" | [ ] |
| C2 | Ion trail info card title shows "MAPS: Ion Trail (Remains)" | [ ] |

If C1 or C2 fails: the router log (`[ROUTING]` lines in browser
console or Python stdout) will show what was parsed. The most likely
explanation would be a stray "MAPS: Dust Tail" substring elsewhere
in the body text matching the `.replace()` -- the body content
inside `description` (lines 988-994 and 1141-1147) starts with
"Dust Tail (Type II) of MAPS" / "Ion Tail (Type I, Plasma Tail) of
MAPS", not "MAPS: Dust Tail" / "MAPS: Ion Tail", so the replace
should only hit the header. But verify if anomalous.

---

## Results template

```
Scenario A -- Pre-disintegration:
  A1 Marker shape (open green square):       [ ]
  A2 Marker size (readable):                 [ ]
  A3 Marker outline (green, no white):       [ ]
  A4 Distinct from nucleus diamond:          [ ]
  A5 Ghost tail thicker than osc orbit:      [ ]
  A6 Ghost tail color fade unchanged:        [ ]
  A7 Ghost tail toggles as one group:        [ ]
  A8 Disintegration hover unchanged:         [ ]

Scenario B -- Post-disintegration:
  B1 No nucleus marker rendered:             [ ]
  B2 Trail (Remains) legend labels:          [ ]
  B3 Dust hover header "(Remains)":          [ ]
  B4 Ion hover header "(Remains)":           [ ]
  B5 Hover body unchanged (intentional):     [ ]
  B6 Disintegration marker correct:          [ ]
  B7 Ghost tail correct:                     [ ]

Scenario C -- Gallery card (optional):
  C1 Dust card title "(Remains)":            [ ]
  C2 Ion card title "(Remains)":             [ ]

Notes / anomalies:
```

---

## After testing

If all checks pass:
1. Stage 2 item 2D is complete; the full Stage 2 queue is closed.
2. Update credit line in `comet_visualization_shells.py` module
   docstring to reflect this session's edit.
3. Regenerate `MODULE_ATLAS.md` (only the credit line / docstring
   changed for this file, so the atlas update is cosmetic).
4. Deploy to GitHub as the Stage 2 closeout commit (or bundle with
   any Stage 3 work if you'd rather).
5. Next session: Stage 3 cosmetic cleanup or Stage 4 bigger items
   per the v11 handoff Deferred Items.

If any check fails:
- A1-A4 failures: marker convention concerns -- compare side-by-side
  with the 2C.5b Neptune Magnetic Field Center marker for shape
  consistency.
- A5/B7 failures: ghost tail width regression -- check that line
  710 actually shows `width=5`.
- B3/B4 failures: the `tr.text` replace didn't land -- check the
  post-disintegration block (lines 1747-1772 after edit) is intact.
- C1/C2 failures: see Scenario C diagnostic notes above.

---

## What this protocol is NOT testing

- **Ghost tail rendering correctness:** verified in the April 2026
  MAPS session. This protocol verifies width only.
- **Disintegration marker placement:** verified in the April 2026
  MAPS session via Barker's equation. This protocol verifies symbol
  shape and size only.
- **Post-disintegration scaling factors:** unchanged from v10
  (`dust_scale=0.55`, `ion_scale=0.35`).
- **Sun Direction indicator on MAPS:** verified in the May 25 PM
  session (Comet Sun Direction follow-through).
- **Customdata field on source-side traces:** confirmed dead-letter
  per scope question 1 analysis; not testing because the gallery
  router overwrites it.

---

*"Tony's eyes win."* -- still.

*Module updated: May 2026 with Anthropic's Claude Opus 4.7*
*(Stage 2 item 2D: MAPS marker symbol / ghost tail width / Remains hover)*
