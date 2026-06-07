# Encounter Export — Handoff v3

**May 10, 2026 | Tony + Claude Opus 4.6 | Tests E-H complete**

---

## Cumulative status

### Session 1 (May 9 — Tests A-D)

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

### Session 2 (May 10 — Tests E-H + fixes)

| # | What | File | Status |
|---|------|------|--------|
| 8 | Target suggestion defaults to center body | gallery_studio.py | Applied |
| 9 | Persistent file dialog paths (studio_config.json) | gallery_studio.py | Applied |
| 10 | STUDIO_PREFS_FILE anchored to script directory | gallery_studio.py | Applied |
| 11 | Remove 2 Animated encounter dicts | spacecraft_encounters.py | Applied |
| 12 | Rename "Mars GA Static" -> "Mars Gravitational Assist" | spacecraft_encounters.py | Applied |
| 13 | Remove render_mode key from Mars GA dict | spacecraft_encounters.py | Applied |
| 14 | Remove render_mode parameter + filter from add_tagged_encounter_markers | spacecraft_encounters.py | Applied |
| 15 | Remove render_mode from _add_spacecraft_encounter_markers wrapper + both call sites | palomas_orrery.py | Applied |
| 16 | Written-date-format parser for title dates ("October 14, 2023" format) | gallery_studio.py | Applied |
| 17 | Normalize Psyche Mars GA date to 2026-05-15 19:29:00 | spacecraft_encounters.py | Applied |
| 18 | Remove TODO comments from Psyche plot_days | spacecraft_encounters.py | Applied |
| 19 | Fix double space in Psyche Mars GA note | spacecraft_encounters.py | Applied |
| 20 | Persistent save directory (window_config.json) | save_utils.py + palomas_orrery.py | Applied |

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

The `render_mode` key is eliminated from the codebase: removed from
`spacecraft_encounters.py` (parameter + filter block),
`palomas_orrery.py` (wrapper function signature + both call sites).

### Closeup scale priority fix (found in Test E)

The adaptive path was ignoring `plot_scale_au_closeup`, picking the
wide-field `plot_scale_au` instead. Fixed to prefer closeup:

```
plot_scale = enc.get('plot_scale_au_closeup') or enc.get('plot_scale_au') or resolution['plot_scale_au']
```

NH Pluto now renders at 0.002 AU (closeup) instead of 0.5 AU (wide).

### Written-date-format parser (found in Test F)

The orrery writes titles in `"Month DD, YYYY HH:MM"` format
("October 14, 2023 00:00") but the Studio date extraction regex
only matched `YYYY-MM-DD`. Added two fallback patterns:

1. `"Month DD, YYYY HH:MM"` -> parse with `%B %d, %Y %H:%M`
2. `"Month DD, YYYY"` (no time) -> parse with `%B %d, %Y`

Both normalize to `YYYY-MM-DD` for the `date_range` field.

### Encounter marker traces belong in select_also

When exporting a full_mission dict, the extraction includes encounter
marker trace names (e.g. `'Psyche Mars Gravitational Assist (Horizons)'`)
in `select_also`. These are not celestial objects but they are functional:
the preset selects them so encounter markers appear alongside orbital
close approach markers for comparison. This is intentional, not noise.

The existing Psyche full mission dict in `spacecraft_encounters.py`
predates the encounter markers and does not include them. Leaving as-is
for now; will update when encounter dicts are next revised.

### Persistent save directory for orrery

Studio already persists file dialog paths in `studio_config.json`.
The orrery's `save_utils.py` remembered the last save directory
within a session but reset on restart.

**Fix:** Added `set_last_save_directory()` / `get_last_save_directory()`
to `save_utils.py`. The orrery reads from `window_config.json` at
startup and writes back on exit. No new config files — piggybacks on
the existing window config save/load cycle.

### studio_config.json path anchoring

`STUDIO_PREFS_FILE` uses `os.path.join(os.path.dirname(os.path.abspath(__file__)), ...)` 
so the config file stays next to the script regardless of CWD.

---

## Test results

| Test | What | Result | Notes |
|------|------|--------|-------|
| A-D | Prior session | **Pass** | Psyche Phobos flyby, Mars GA, round-trip |
| E | Scale floor regression | **Pass** | NH Pluto: 0.002 AU (closeup). Artemis II: 0.0003 AU. |
| F | Psyche Full Mission dates | **Pass** | After written-date-format fix. Dates: 2023-10-14 to 2029-06-26. |
| G | Date format resilience | **Pass** | All 3 formats normalized: standard, unpadded, date-only. |
| H | Backward compatibility | **Pass** | Old trace name "Psyche Closest Plotted Point" extracts correctly. |

---

## Psyche encounter cleanup (applied this session)

- Mars GA date normalized: `'2026-5-15 9:28:00'` -> `'2026-05-15 19:29:00'`
  (matches Horizons-derived closest approach; old value was 10 hours off)
- Both `# TODO: adjust` comments removed from `plot_days`
- Double space fixed in Mars GA note
- `'status': 'ongoing'` — correct for now (encounter is May 15, 2026);
  flip to `'completed'` afterward
- Neither encounter has `center_closeup` / `plot_days_closeup` /
  `plot_scale_au_closeup` — deferred, will add when Go buttons are revised

---

## Files modified across both sessions

| File | Edits | |
|------|-------|-|
| gallery_studio.py | 10 (9 prior + 1 date parser) | |
| spacecraft_encounters.py | 10 (1 prior + 6 render_mode + 3 cleanup) | |
| palomas_orrery.py | 4 (3 render_mode + 1 save dir) | |
| save_utils.py | 1 (save dir getter/setter) | |

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

### Encounter closeup variants for Psyche

Add `center_closeup`, `plot_days_closeup`, `plot_scale_au_closeup`
to both Psyche encounter dicts for dual wide/close Go button views.
Deferred until Go button UI is revised.

### Full mission select_also update

The Psyche full mission dict's `select_also` could include encounter
marker trace names for automatic comparison view. Deferred — will
update when encounter dicts are next revised.

---

*Handoff v3.0 -- May 10, 2026*
*Tony Quintanilla + Anthropic's Claude Opus 4.6*
