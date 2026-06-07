# Non-Destructive Routing Refactor - Handoff

## Session 1 (Design): March 9, 2026 | Claude Opus 4.6
## Session 2 (Implementation): March 9, 2026 | Claude Opus 4.6

---

## Status: PHASE 1 COMPLETE -- Non-destructive routing shipped and tested.

Phase 2 (generalized "Strip suppressed data" UI) is designed but
deferred. May or may not be needed -- the main WYSIWYG objective
is accomplished.

---

## Context

Gallery Studio's hover routing pipeline was destructive:
`apply_config()` blanked `trace['text']` and stashed the original in
`trace['_original_text']`. This meant a gallery export with routing ON
had permanently blanked hover text. Reloading the export and turning
routing back ON produced empty card content (names only, no body)
because the text was already gone.

This was discovered during testing of the Apophis Closest Approach plot.
The status log correctly shows the file loads and route is toggled, but
the card shows only trace names because customdata was parsed from
blank text.

### Root Cause

The routing block in `apply_config()` (around line 1056) does:
```
trace['_original_text'] = text_list   # stash
trace['text'] = ['' for _ in text_list]  # blank
```

On export, both the blanked `text` and the stashed `_original_text`
are serialized into the HTML. On reload, `_do_load()` pops
`_original_text` back into `text`. This works for ONE round-trip.

But if the source file was itself a gallery export where routing had
already blanked the text in a prior cycle, `_original_text` contains
blank strings. The restore recovers blanks. The hover data is
permanently lost.

### Current Mitigations (shipped this session)

1. Route hover checkbox resets to OFF on gallery export reload
2. Status log warns when blank `_original_text` is detected:
   "WARNING: N traces had blank hover stash -- reload from raw
   orrery source for full hover"
3. `_hoverMode` JS variable injected as string literal instead of
   reading from Plotly layout DOM (Plotly strips underscore keys)
4. Updated tooltips on Load, Reload, Export, Preview, Reset,
   Portrait/Landscape/Original presets, and Route hover checkbox

---

## Architecture: Non-Destructive Routing (IMPLEMENTED)

### Core Principle

**Keep all data in the export by default. Display only what's selected.
Stripping is an explicit, opt-in, destructive optimization step.**

This mirrors the existing trace visibility pattern:
- Visibility toggles are non-destructive (traces hidden but present)
- "Strip hidden" is the explicit destructive step (traces removed)

### Design

**Non-destructive (default export):**

- Routing ON: `apply_config()` still parses hover text into
  `trace['customdata']` for the card. But `trace['text']` is NOT
  blanked. The original hover text stays in the data.
- Tooltip suppression moves to JS: when routing is active, the JS
  hides the Plotly tooltip (via transparent hoverlabel or CSS) and
  shows the info card instead. The data is all there; only the
  display changes.
- Reload gives full round-trip. Toggle routing OFF and hover text
  works immediately. Toggle ON and card has full content.
- `_original_text` stash is no longer needed.

**Destructive (opt-in "Strip suppressed"):**

- Generalize "Strip hidden traces" to "Strip suppressed data":
  - Strip hidden traces (existing behavior)
  - Strip hover text when routing is ON (blank text, remove
    _original_text -- current behavior becomes opt-in)
  - Potentially: strip hidden annotations, strip disabled legend, etc.
- One checkbox or a small "Strip" section in the GUI
- On export with stripping: bake in the destructive transforms,
  record what was stripped in `_studio_config`

**Reload of stripped file:**

- Detect stripped state from `_studio_config` flags
- Grey out / disable controls for stripped content
- Status log: "Hover text was stripped -- reload from raw source
  for full hover data"
- Route checkbox disabled (greyed out) if hover text was stripped
- Prevents the confusing scenario of turning route ON with no data

### Implementation Plan

#### Phase 1: Non-destructive routing

Files: `gallery_studio.py`

1. **Routing block in `apply_config()`** (~line 1056):
   - Keep the customdata parsing (hover -> structured card data)
   - STOP blanking `trace['text']`
   - STOP stashing `_original_text`
   - Still set `layout['_hover_mode']` for the JS

2. **JS tooltip suppression** (infocard_js in `build_gallery_html`
   and `build_social_html`):
   - When routing is active: make hoverlabel fully transparent
     (already partially done -- `hoverlabel.bgcolor/bordercolor/font`
     set to transparent). Verify this fully suppresses the tooltip
     including the arrow pointer.
   - The card handler already reads customdata on click -- no change
   - Test: hover shows nothing, click shows full card

3. **Remove `_original_text` restore from `_do_load()`**:
   - No longer needed since text is never blanked
   - Remove the blank-stash detection warning (no longer applicable)

4. **Test matrix** (all 6 hover/routing combos):

   |                | Route OFF        | Route ON              |
   |----------------|------------------|-----------------------|
   | Default hover  | Full tooltip     | No tooltip, full card |
   | Names only     | Name tooltip     | No tooltip, name card |
   | No hover       | Nothing          | Nothing               |

   Plus round-trip: export -> reload -> re-export with different
   settings -> verify all combinations work.

#### Phase 2: Generalized stripping

Files: `gallery_studio.py`

1. **Rename "Strip hidden" to "Strip suppressed data"** or add a
   separate strip section with checkboxes:
   - [ ] Strip hidden traces (existing)
   - [ ] Strip routed hover text (new)

2. **Record strip state in `_studio_config`**:
   ```python
   '_stripped': {
       'hidden_traces': True,  # traces physically removed
       'hover_text': True,     # text blanked by routing
   }
   ```

3. **Detect on reload**:
   - Read `_stripped` from `_studio_config`
   - Disable relevant controls (grey out route checkbox if hover
     text was stripped)
   - Status log warning

4. **UI for greyed-out state**:
   - Tkinter: `state='disabled'` on checkbuttons/entries
   - Tooltip explains why: "Hover text was stripped in this export.
     Reload from raw orrery source to enable routing."

### Considerations

**File size:** Keeping full hover text in exports means larger files.
For the Apophis plot with 15 traces, the text data is modest. For
plots with thousands of orbit points (e.g., 600-point Apophis
osculating orbit), each point has hover text -- could add significant
size. The strip option addresses this for users who care about size.

**Plotly tooltip suppression reliability:** The current transparent
hoverlabel approach (bgcolor, bordercolor, font all rgba(0,0,0,0))
was verified to suppress the visual tooltip but may still show a
tiny arrow pointer in some Plotly versions. Need to test with the
actual Apophis plot. If the pointer persists, may need
`hoverinfo='skip'` on routed traces (but this kills click detection
in some Plotly 3D versions -- the exact issue that led to the
current approach).

**Hover mode interaction:** With non-destructive routing, the
hover_mode block (which runs AFTER routing in `apply_config`) would
see the original text still in `trace['text']`. Currently the
`names_only` mode replaces text with trace names. This is fine for
tooltip display but the card should still show full content from
customdata. The JS card handler already respects `_hover_mode`
independently of the tooltip -- verify this still works correctly.

**Animation frames:** The routing block also processes animation
frames. Same pattern applies: stop blanking frame trace text.

**`build_social_html` parity:** The portrait/social builder has its
own layout_for_json filter and _hover_mode preservation. Both
builders need the same changes.

---

## Files Modified This Session

**`gallery_studio.py`** (4739 -> 4830 lines):

- Added `scrolledtext` import
- Added Status Log widget in col_3d (below 3D Scene section):
  `ScrolledText`, dark theme, 10 lines, timestamps
- Added `_log_status(msg)` method: timestamps, appends to log,
  syncs with status bar
- Replaced all 18 `status_var.set()` calls with `_log_status()`
- Added trace visibility change logging (per-checkbox callbacks)
- Added featured trace change logging (per-checkbox callbacks)
- Added Select All / Select None logging
- Added config-diff logging on Preview/Export (`_prev_config`
  snapshot comparison, reports up to 5 changed keys)
- Fixed pre-existing em dash (line 4535) to ASCII `--`
- Force `route_hover` OFF on gallery export reload
- Blank `_original_text` stash detection with status log warning
- `_hoverMode` JS injection as string literal (not DOM read)
- Updated tooltips on 9 controls (Load, Reload, Preview, Export,
  Reset, Portrait Preset, Landscape Preset, Original, Route hover)

---

## Standing Decisions

| Question | Decision | Rationale |
|----------|----------|-----------|
| Routing destructiveness | Make non-destructive (Phase 1) | Round-trip editing is core Studio promise |
| Stripping | Opt-in, generalized (Phase 2) | Matches existing trace strip pattern |
| Greyed-out controls | Yes, for stripped content | Prevents confusing silent failures |
| `_original_text` | Remove once Phase 1 ships | No longer needed if text isn't blanked |
| JS tooltip suppression | Transparent hoverlabel + CSS | Already partially implemented |
| File size concern | Strip option addresses it | Non-destructive = larger but editable |

---

## Key Code Locations

| What | Where | Line (approx) |
|------|-------|---------------|
| Routing block (blanks text) | `apply_config()` | ~1056 |
| `_original_text` stash | routing block | ~1109 |
| `_original_text` restore | `_do_load()` | ~4635 |
| Infocard JS injection | `build_gallery_html()` | ~2290 |
| `_hoverMode` JS literal | infocard_js string concat | ~2394 |
| Hover mode block | `apply_config()` | ~1160 |
| `layout_for_json` filter | `build_gallery_html()` | ~1800 |
| Portrait builder filter | `build_social_html()` | ~2605 |
| `_studio_config` embed | `apply_config()` | ~1543 |
| Blank stash detection | `_do_load()` | ~4638 |
| Status Log widget | `_build_config_sections()` | ~3917 |

---

## Lessons Learned

- Plotly's `newPlot()` may strip underscore-prefixed layout keys.
  Don't rely on `_plotDiv.layout._custom_key` surviving render.
  Inject values as JS literals instead.

- Destructive transforms in a round-trip pipeline create data loss
  that compounds across cycles. The safe pattern: keep data intact
  by default, strip explicitly on request.

- "Source file = raw data. Gallery file = curated artifact" is
  correct but insufficient. The curated artifact should be fully
  re-editable, not just re-displayable. That's the Studio promise.

- Status log with timestamps is immediately useful for debugging
  session workflows. Config-diff logging catches the "what changed?"
  question before it becomes "what broke?"

---

*"Keep all the information in the export, but only display what's
been selected."* -- Tony, the design insight that unifies
non-destructive editing with explicit stripping, March 9, 2026

---

## Session 2: Implementation (March 9, 2026)

### What Was Done

Phase 1 implemented and tested. Eight targeted changes to
`gallery_studio.py`, applied bottom-up:

1. **Routing section comment** (~line 1050): updated to describe
   non-destructive approach.

2. **Main routing block** (~line 1098): removed `_original_text`
   stash and `trace['text']` blanking. Customdata parsing retained.
   `hovertemplate` and `hoverinfo` still set for event detection.

3. **Animation frames routing** (~line 1126): same pattern -- removed
   stash and blanking, kept customdata parsing.

4. **Hoverlabel config** (~line 1253): moved routing check outside
   the portrait-only guard. Transparent hoverlabel now applies to all
   output formats when routing is active (required because text is no
   longer blanked -- tooltip suppression comes from hoverlabel, not
   from empty text).

5. **Load button tooltip** (~line 3025): simplified, removed data-loss
   warnings about blank stash.

6. **Reload button tooltip** (~line 3039): simplified, removed
   `_original_text` recovery language.

7. **Route hover checkbox tooltip** (~line 3761): updated from
   "destructive" to "non-destructive" description.

8. **`_do_load()` restore block** (~line 4627): simplified. Removed
   blank-stash detection. Kept backward-compat `_original_text`
   restore for older exports (pop and restore if present). Simplified
   status messages.

### What Was NOT Changed

- **Hover mode block** (lines 1156-1202): unchanged. Its text
  modifications are tooltip-display concerns, separate from routing.
- **`build_gallery_html()`**: no changes needed.
- **`build_social_html()`**: no changes needed.
- **JS card handler**: unchanged -- already reads customdata, already
  respects `_hoverMode`.
- **Portrait/Landscape preset tooltips**: left as-is.

### Test Results

Full 6-cell matrix tested, plus round-trip:

|                | Route OFF        | Route ON              |
|----------------|------------------|-----------------------|
| Default hover  | Full tooltip OK  | No tooltip, full card OK |
| Names only     | Name tooltip OK  | No tooltip, name card OK |
| No hover       | Nothing OK       | Nothing OK            |

Round-trip: export -> reload -> text intact -> re-export with
different settings (added dtick 0.0005 AU) -> identical results.

### Known Issue: Grey Arrow Pointer

Route ON + Default hover shows an unusually large grey arrow pointer.
This is the Plotly tooltip arrow -- the tooltip box is invisible
(transparent hoverlabel) but the arrow SVG element still renders.
It's large because the full hover HTML creates a big invisible box.

With Names only the arrow is normal-sized (short text = small box).
With No hover the arrow doesn't appear (text blanked by hover_mode).

**Diagnosed fix (not yet applied):** Change routing block's
`hovertemplate` from `'%{text}<extra></extra>'` to `'<extra></extra>'`.
This removes the text reference from the template so no tooltip box
(and no arrow) renders, while still firing hover/click events. The
text data stays intact in `trace['text']` -- just not referenced by
the template when routing is active.

This is a cosmetic issue, not a data integrity issue. Can be fixed
in a future session if desired.

### Files Modified

**`gallery_studio.py`** (~4,830 lines, 8 changes):
- Routing block: removed `_original_text` stash + text blanking
- Animation frames: same removal
- Hoverlabel: routing check moved outside portrait guard
- `_do_load()`: simplified restore, backward compat for old exports
- 3 tooltip updates (Load, Reload, Route hover checkbox)
- Routing section comment updated

---

## Standing Decisions (Updated)

| Question | Decision | Status |
|----------|----------|--------|
| Routing destructiveness | Non-destructive (Phase 1) | **SHIPPED** |
| Stripping | Opt-in, generalized (Phase 2) | Designed, deferred |
| Greyed-out controls | Yes, for stripped content (Phase 2) | Deferred |
| `_original_text` | Backward compat only -- new exports don't write it | **SHIPPED** |
| JS tooltip suppression | Transparent hoverlabel | **SHIPPED** |
| Grey arrow pointer | Fix with `<extra></extra>` template | Diagnosed, deferred |
| File size concern | Strip option would address (Phase 2) | Deferred |
| Overall WYSIWYG objective | Accomplished | **DONE** |

---

## Lessons Learned (Session 2)

- Transparent hoverlabel suppresses the tooltip box but not the arrow
  pointer. The arrow is a separate SVG element. To fully suppress,
  use an empty hovertemplate (`'<extra></extra>'`) that references
  no data fields.

- The hover_mode block runs AFTER routing and sets its own
  hovertemplate. This means `names_only` and `none` modes override
  the routing template. For `default` mode, routing's template
  survives. This interaction is correct but must be understood when
  changing either block.

- Non-destructive routing + transparent hoverlabel is the clean
  separation: data layer (keep everything) vs display layer (show
  selectively). The previous approach conflated data and display
  by using text blanking for visual suppression.

- Backward compatibility for older exports is simple: pop
  `_original_text` and restore if present. No version flags needed.
  New exports just don't write the stash.

---

*"The main objective, WYSIWYG, is accomplished."*
-- Tony, confirming Phase 1 success, March 9, 2026
