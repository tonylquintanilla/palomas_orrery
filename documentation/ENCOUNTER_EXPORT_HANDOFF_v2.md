# Encounter Export — Handoff v2

**May 10, 2026 | Tony + Claude Opus 4.6 | Tests E partial + cleanup**

---

## Cumulative status

### Prior session (May 9 — Tests A-D)

Seven edits applied to `gallery_studio.py`, one snippet to
`spacecraft_encounters.py`. All confirmed.

| # | What | File |
|---|------|------|
| 1 | Modebar stays visible in Orrery mode | gallery_studio.py |
| 2 | Reset Defaults moved to preset row (next to Orrery) | gallery_studio.py |
| 3 | plot_scale_au -> editable Entry, pre-filled from extraction | gallery_studio.py |
| 4 | plot_days -> editable Entry, H:MM format support (1:00, 0:30) | gallery_studio.py |
| 5 | v_kms extraction from Horizons encounter marker hover text | gallery_studio.py |
| 6 | Code gen: manual scale/plot_days override with fallback to extracted | gallery_studio.py |
| 7 | Fallback path: fractional days, adaptive fetch_step (1m/1h/6h) | spacecraft_encounters.py |

### This session (May 10)

| # | What | File | Status |
|---|------|------|--------|
| 8 | Target suggestion defaults to center body | gallery_studio.py | Applied by Tony |
| 9 | Persistent file dialog paths (studio_config.json) | gallery_studio.py | Applied by Tony |
| 10 | STUDIO_PREFS_FILE anchored to script directory | gallery_studio.py | Snippet provided |
| 11 | Remove 2 Animated encounter dicts | spacecraft_encounters.py | Snippet provided |
| 12 | Rename "Mars GA Static" -> "Mars Gravitational Assist" | spacecraft_encounters.py | Snippet provided |
| 13 | Remove render_mode key from Mars GA dict | spacecraft_encounters.py | Snippet provided |
| 14 | Remove render_mode parameter + filter from add_tagged_encounter_markers | spacecraft_encounters.py | Snippet provided |

---

## Design decisions made this session

### Animation encounters removed from Go button architecture

The Go button always calls `plot_objects()` — there is no routing to
`animate_objects()`. The "Animated" encounter dicts had no operational
distinction from their "Static" counterparts. Keeping them added
confusion (duplicate markers, duplicate legend entries) without function.

**Decision:** Remove Animated dicts entirely. One dict per encounter
event. Animation support in the preset system deferred until the
animation pipeline is refactored (frame-differential rendering to reduce
memory duplication).

**Result:** Psyche encounters go from 4 dicts to 2:
- Mars Gravitational Assist (was "Mars GA Static")
- Flyby of Phobos (unchanged)

The `render_mode` key is eliminated from the codebase.

### Closeup scale priority fix (found in Test E)

The adaptive path was ignoring `plot_scale_au_closeup`, picking the
wide-field `plot_scale_au` instead. Fixed to prefer closeup:

```
plot_scale = enc.get('plot_scale_au_closeup') or enc.get('plot_scale_au') or resolution['plot_scale_au']
```

NH Pluto now renders at 0.002 AU (closeup) instead of 0.5 AU (wide).
Applied by Tony before second Test E run.

### studio_config.json path anchoring

`STUDIO_PREFS_FILE` uses a bare relative path, which would drop the
file wherever CWD happens to be. Since Studio lives in
`tonyquintanilla.github.io/tools/` (separate repo from the orrery),
it must be anchored to the script directory:

```python
STUDIO_PREFS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'studio_config.json')
```

---

## Test results

| Test | What | Result | Notes |
|------|------|--------|-------|
| E | Scale floor regression | **Pass** | NH Pluto: 0.002 AU (closeup). Artemis II: 0.0003 AU. Both from dict. |
| F | Psyche Full Mission dates | Not started | |
| G | Date format resilience | Not started | |
| H | Backward compatibility | Not started | |

---

## Remaining tests

### Test F: Psyche Full Mission dates

Export a full_mission type encounter for Psyche. Verify:
- `start_date` and `end_date` pulled from `celestial_objects.py`
- If celestial_objects.py isn't importable from Studio's context,
  verify the fallback produces `# TODO: fill in` comments

### Test G: Date format resilience

In the Export Encounter dialog, enter dates in various formats:
- `2026-05-15 19:29:24` (standard) -> should normalize fine
- `2026-5-15 9:28` (unpadded) -> should normalize or warn
- `2026-05-15` (no time) -> should normalize to `2026-05-15 00:00:00`

### Test H: Backward compatibility

Load an older HTML file (pre-trace-deconfliction, where the closest
plotted point is named `"Psyche Closest Plotted Point"` not
`"Psyche Closest Plotted Period Point"`). Verify:
- Center detection still works (falls through to generic name)
- Date and distance extraction still works
- Export produces a valid dict

---

## Pending snippets (not yet applied by Tony)

### spacecraft_encounters.py — 6 edits, bottom-up

All line numbers from uploaded file (1571 lines).

**Edit 6 (line ~1297):** Remove render_mode filter block.
```
DELETE these 4 lines:
            # ---- render_mode filter ----
            enc_mode = enc.get('render_mode')
            if enc_mode and render_mode and enc_mode != render_mode:
                continue
```

**Edit 5 (line 1238):** Remove render_mode parameter.
```
old:                                  render_mode=None):
new:                                  ):
```

**Edit 4 (line 306):** Rename label.
```
old:            'label': 'Mars Gravitational Assist Static',
new:            'label': 'Mars Gravitational Assist',
```

**Edit 3 (line 302):** Remove render_mode key.
```
DELETE this line:
            'render_mode': 'static',
```

**Edit 2 (lines 317-338):** Delete entire Mars GA Animated dict block
(comment header + dict + trailing blank line).

**Edit 1 (lines 340-361):** Delete entire Flyby of Phobos Animated dict
block (comment header + dict + trailing blank line).

Note: Edits 1 and 2 are both deletions of adjacent blocks. If applying
together, delete lines 317-361 (both blocks).

### gallery_studio.py — 1 edit

**STUDIO_PREFS_FILE anchoring (line ~3150):**
```
old:     STUDIO_PREFS_FILE = 'studio_config.json'
new:     STUDIO_PREFS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'studio_config.json')
```

---

## Future work (deferred, not blocking)

### Animation pipeline refactor

Current `animate_objects` duplicates every trace in every frame.
Memory-heavy for complex plots. The right approach is
frame-differential rendering: static geometry shared across frames,
only moving traces (spacecraft positions, position markers) vary
per frame. This is a separate design conversation.

Once refactored, the preset system can learn to route Go button
clicks to `animate_objects()` via an `animated: true` key. Not
before.

### Animated encounter marker on static plots (resolved)

Original problem: both Static and Animated Horizons markers appeared
on static plots. Resolved by removing Animated dicts entirely.
No code change needed in the marker creation pipeline.

---

## Files modified across both sessions

| File | Edits | Base |
|------|-------|------|
| gallery_studio.py | 9 applied + 1 pending | Uploaded working copy (safe) |
| spacecraft_encounters.py | 1 applied + 6 pending | Uploaded working copy |

---

*Handoff v2.0 -- May 10, 2026*
*Tony Quintanilla + Anthropic's Claude Opus 4.6*
