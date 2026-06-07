# Encounter Export — Test D Handoff

**May 9, 2026 | Tony + Claude Opus 4.6 | Test D fixes + continuation plan**

---

## Session summary

Six targeted edits applied to `gallery_studio.py` (from uploaded working
copy — safe base). One snippet provided for `spacecraft_encounters.py`
(stale base in /mnt/project/, snippet only). All edits verified by Tony.

### Edits applied and confirmed

| # | What | File |
|---|------|------|
| 1 | Modebar stays visible in Orrery mode | gallery_studio.py |
| 2 | Reset Defaults moved to preset row (next to Orrery) | gallery_studio.py |
| 3 | plot_scale_au → editable Entry, pre-filled from extraction | gallery_studio.py |
| 4 | plot_days → editable Entry, H:MM format support (1:00, 0:30) | gallery_studio.py |
| 5 | v_kms extraction from Horizons encounter marker hover text | gallery_studio.py |
| 6 | Code gen: manual scale/plot_days override with fallback to extracted | gallery_studio.py |
| 7 | Fallback path: fractional days, adaptive fetch_step (1m/1h/6h) | spacecraft_encounters.py (snippet) |

### Test D results (3 exports)

| Export | Key finding |
|--------|-------------|
| encounter1 (original) | Target defaulted to Phobos (wrong), scale was adaptive, v_kms empty |
| encounter2 (after edits) | v_kms: 5.51 extracted correctly, scale editable, Mars-only select_also |
| encounter3 (H:MM test) | `plot_days: 60 / 1440,  # 1:00` — H:MM format confirmed working |

---

## Open items from Test D

### 1. Animated Horizons marker on static plot (medium priority)

**Problem:** When the orrery generates a static encounter plot, both
`Psyche Mars Gravitational Assist Static (Horizons)` and
`Psyche Mars Gravitational Assist Animated (Horizons)` markers appear.
On a static plot, the Animated marker is redundant — same position,
same data, duplicate legend entry.

Both also appear in `select_also` in the exported dict.

**Fix options (choose one):**

A. **Orrery-side** (`add_tagged_encounter_markers()` in
`spacecraft_encounters.py`): detect whether the current plot is static
or animated and only create the matching marker. The function knows
which trajectory traces were generated.

B. **Extractor-side** (`_extract_encounter_data()` in
`gallery_studio.py`): filter select_also to exclude Animated marker
traces when the source plot is static. Detection: if no trace named
`"...Animated..."` is visible (checked via trace_vars), skip it.

C. **Both:** orrery doesn't create it, extractor filters as belt-and-suspenders.

Recommendation: Option A is cleaner — fix at the source. The orrery
knows the render mode; the extractor shouldn't need to guess.

### 2. Target suggestion defaults to wrong object (minor)

**Problem:** Target suggestion picks the first item in `select_also`
that isn't Earth/Sun/spacecraft. For a Mars gravity assist, Mars is the
center body and gets filtered, so Phobos or another object wins.

**Fix:** Default target to the center body. User edits if needed.

In `_extract_encounter_data()`, after center detection, replace the
target suggestion block:

```python
# ---- Target suggestion ----
# Default to center body; user can change in dialog
if result.get('center'):
    result['target_suggestion'] = result['center']
else:
    for obj in deduped:
        if obj not in ('Earth', 'Sun', spacecraft_name):
            result['target_suggestion'] = obj
            break
```

---

## Remaining tests (E-H)

| Test | What | Key verification | Status |
|------|------|------------------|--------|
| E | Scale floor regression | Existing NH + Artemis encounters still render at their dict scales | Not started |
| F | Psyche Full Mission dates | Bug 6 fix — dates filled from celestial_objects.py | Not started |
| G | Date format resilience | Defensive parser handles unpadded dates like `2026-5-15 9:28` | Not started |
| H | Backward compatibility | Older HTML files (pre-deconfliction) still extract via generic name fallback | Not started |

### Test E: Scale floor regression

Run existing Go button encounters (New Horizons Pluto, Artemis I, any
others with explicit `plot_scale_au` in their dicts). Verify:
- Dict scale used (not overridden by adaptive)
- Console output confirms: `[ENCOUNTER PRESET] Adaptive resolution...scale=X`
  where X matches the dict value
- Plot geometry looks correct at the expected scale

### Test F: Psyche Full Mission dates

Export a full_mission type encounter for Psyche. Verify:
- `start_date` and `end_date` are pulled from `celestial_objects.py`
  (the Edit 6b import at lines 5076-5089 in current gallery_studio.py)
- If celestial_objects.py isn't importable from Studio's context,
  verify the fallback produces `# TODO: fill in` comments

### Test G: Date format resilience

In the Export Encounter dialog, enter dates in various formats:
- `2026-05-15 19:29:24` (standard) → should normalize fine
- `2026-5-15 9:28` (unpadded) → should normalize or warn
- `2026-05-15` (no time) → should normalize to `2026-05-15 00:00:00`

### Test H: Backward compatibility

Load an older HTML file (pre-trace-deconfliction, where the closest
plotted point is named `"Psyche Closest Plotted Point"` not
`"Psyche Closest Plotted Period Point"`). Verify:
- Center detection still works (falls through to generic name)
- Date and distance extraction still works
- Export produces a valid dict

---

## Quality of life: persistent file dialog paths

**Request:** Remember the last-used directory for each file dialog type
and pre-navigate there on next open. Persist across sessions via
`window_config.json`.

### Affected dialogs

| Dialog | Current default | Config key |
|--------|----------------|------------|
| Load HTML (source import) | OS default | `last_dir_load_html` |
| Export HTML (gallery output) | OS default | `last_dir_export_html` |
| Export Encounter (.py) | OS default | `last_dir_export_encounter` |
| Any other import/export in Studio | OS default | `last_dir_{operation}` |

### Implementation approach

1. On startup, read `window_config.json` for `last_dir_*` keys
2. Pass `initialdir=` to `filedialog.askopenfilename()` / `asksaveasfilename()`
3. After successful open/save, update `window_config.json` with the
   directory portion of the selected path
4. If the saved directory no longer exists, fall back to OS default

Pattern:
```python
def _get_last_dir(self, key):
    """Get last-used directory for a file dialog, or None."""
    d = self._window_config.get(key, '')
    return d if d and os.path.isdir(d) else None

def _set_last_dir(self, key, filepath):
    """Save directory of filepath for next dialog open."""
    self._window_config[key] = os.path.dirname(filepath)
    self._save_window_config()
```

Usage at each dialog site:
```python
path = filedialog.askopenfilename(
    initialdir=self._get_last_dir('last_dir_load_html'),
    filetypes=[("HTML files", "*.html"), ("All files", "*.*")]
)
if path:
    self._set_last_dir('last_dir_load_html', path)
    ...
```

Check: does Studio already load/save `window_config.json`? If so,
add keys to the existing mechanism. If not, add the read/write pair.

---

## Files modified this session

| File | Edits | Base |
|------|-------|------|
| gallery_studio.py | 6 targeted edits (all confirmed) + H:MM tooltip | Uploaded working copy (safe) |
| spacecraft_encounters.py | 1 snippet (fractional plot_days fallback) | Applied by Tony to working copy |

---

*Handoff v1.0 — May 9, 2026*
*Tony Quintanilla + Anthropic's Claude Opus 4.6*
