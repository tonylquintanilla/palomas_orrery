# Artemis II Implementation Handoff — April 4, 2026
**Session summary:** Bug fixes, architectural improvements, encounter time derivation.
**Protocol version:** v3.17

---

## Session Accomplishments

### 1. Date Clamping — Five-Layer Fix (Complete)
Artemis II's 9-day ephemeris window exposed five independent Horizons query paths, none of which clamped dates to the object's `start_date`/`end_date`. All five now fixed:

| Layer | File | Fix |
|-------|------|-----|
| Cache fetch (cache-miss) | `palomas_orrery.py` ~4067 | Already in from prior session |
| Cache fetch (gap-fill) | `palomas_orrery.py` ~4119 | `eff_start`/`eff_end` clamp |
| Cache fetch passthrough | `palomas_orrery.py` ~4204 | `fetch_requests` now passed to `update_orbit_paths_incrementally()` |
| Full fetch function | `orbit_data_manager.py` | `obj_end_window` clamp inside `fetch_complete_orbit_path()` |
| Plot-time trajectory | `palomas_orrery_helpers.py` | `fetch_trajectory()` gains `start_date`/`end_date` params; filters epochs before Horizons query |

**Key insight:** The parallel pipeline architecture meant fixes to cache fetch didn't propagate to plot-time fetch. Artemis II was the first object with an ephemeris window narrow enough to expose all five gaps simultaneously.

### 2. UTC → TDB Alignment (`orbit_data_manager.py`)
- Added `utc_to_tdb(dt)` utility (69 second offset)
- Applied to Horizons epoch strings in `fetch_orbit_path()` (strftime now `%Y-%m-%d %H:%M`)
- Also added to `spacecraft_encounters.py` for `resolve_encounter_time()` queries
- **Note:** `fetch_trajectory()` passes JD epochs — timescale handled implicitly, no `utc_to_tdb` needed there

### 3. Artemis II Ephemeris Boundaries (`celestial_objects.py`)
```python
'start_date': datetime(2026, 4, 2, 2, 5),   # was 2,0 -- 5 min buffer for TDB boundary
'end_date':   datetime(2026, 4, 10, 23, 50), # was Apr 11 -- Horizons ends 23:56 TD
```
OEM header: `Orion_OEM_20260401_0335.V0.1  2026-Apr-02 01:59  2026-Apr-10 23:59`

### 4. `get_date_from_gui()` / `get_end_date_from_gui()` Empty Field Fix (`palomas_orrery.py`)
- Both functions now use `safe_int()` helper — empty fields default to current date (year/month/day) or 0 (hour/minute)
- Duplicate `get_end_date_from_gui()` at line ~7762 still uses old pattern with try/except fallback — **still needs updating**

### 5. Window Config Periodic Save (`palomas_orrery.py`)
- Added `periodic_config_save()` called every 5 minutes via `root.after(300000, ...)`
- Fixes config not saving when VS Code terminal is killed (bypasses `on_closing`)
- Also fixed `CONFIG_FILE` path to use `os.path.dirname(os.path.abspath(__file__))` instead of `os.getcwd()`

### 6. Auto-Scale Fix for Non-Sun Centers (`palomas_orrery.py`)
- `calculate_axis_range_from_orbits()`: elliptical orbit branch now uses distance-from-center when `center_object_name != 'Sun'`
- Moon-centered Artemis II plot now scales to ~0.004 AU instead of ~1.3 AU
- Applies to any non-Sun center plot (Phobos, Charon, any moon encounter)

### 7. Encounter Time Derivation Architecture (`spacecraft_encounters.py`)
Complete architectural overhaul of encounter time resolution:

**New `date_source` convention** (documented in module header):
- `'authoritative'` — fixed event time, never derive (TLI burn, reentry, historical missions)
- `'horizons'` — derive from Horizons trajectory data via two-pass search
- `'planning'` — try Horizons derivation, fall back to hardcoded
- absent — treated as `'authoritative'` (all legacy encounters safe)

**New `resolve_encounter_time()` function:**
- Pass 1: coarse 1h search over full mission window (`start_date` to `end_date`)
- Pass 2: fine 1m search in ±90 min window around coarse minimum
- Uses `objects` list for body ID lookup (no hardcoded BODY_IDS dict)
- Returns `{date, dist_au, dist_km}` or None on failure

**Artemis II encounters updated:**
- Earth Departure (TLI): `'date_source': 'authoritative'`
- Lunar Closest Approach: `'date_source': 'horizons'`
- Reentry & Splashdown: `'date_source': 'authoritative'`

**Result from this session:**
```
[RESOLVE] Deriving Moon closest approach for -1024 over 2026-04-02 to 2026-04-10
[RESOLVE] Coarse minimum: 2026-04-06 23:05 UTC (0.000055 AU)
[RESOLVE] Fine minimum: 2026-04-06 23:03:59 UTC (0.0000555 AU = 8,301 km)
[RESOLVE] [horizons] Using derived time for Lunar Closest Approach: 2026-04-06 23:03:59
```
**Actual closest approach: Apr 6 23:04 UTC, 8,301 km** (vs. planning estimate Apr 7 23:06, 8,900 km — ~24 hours earlier)

### 8. RA/Dec Hover Text Wrap Fix (`celestial_coordinates.py`)
Precision/source note moved to its own line:
```python
return (f"Right Ascension: {ra_string}<br>"
        f"  (apparent, {precision_note}{source_note})<br>"
        f"Declination: {dec_string}<br>"
        f"  (apparent, {precision_note}{source_note})")
```

---

## Open Issues

### 1. HypOsc Epoch Should Use Derived Closest Approach Time
**Problem:** Moon-centered full mission plot fetches osculating elements at GUI epoch (Apr 2 02:00), giving `q=83,203 km`. Go: Lunar Closest Approach uses Apr 7 23:06 (planning estimate), giving correct `q=8,318 km`. Now that `resolve_encounter_time()` gives us Apr 6 23:04, the HypOsc fetch should use that time.

**Fix location:** `osculating_cache_manager.py` and the HypOsc pipeline in `palomas_orrery.py`. When a spacecraft has a `derive_from_horizons`/`horizons` encounter for the current center body, use the derived closest approach time as the HypOsc epoch rather than the GUI date.

**Priority:** Medium — the Go button works correctly, full mission plot shows wrong osculating geometry.

### 2. Duplicate `get_end_date_from_gui()` at line ~7762
Still uses bare `int()` calls with `try/except` fallback (returns `start + 365 days` on error). Should be updated to match the `safe_int()` pattern at line ~7560. The live definition is 7762 (last wins in Python).

### 3. `fetch_trajectory()` Call Sites — Animation Path
Lines 6121, 6137, 6486, 9752 don't yet pass `start_date`/`end_date` to `fetch_trajectory()`. Normal plot (lines 3503, 4916) are fixed. Animation path relies on `fetch_complete_orbit_path()` end-window clamp in `orbit_data_manager.py` — functional but doesn't clamp start date.

### 4. Animation Pipeline Regression Test
No systematic testing of animation with recent changes:
- Osculating orbit rendering (apsidal markers)
- Encounter markers in animation context
- K1 fragment trajectories (4 fragments, separate colors)
- Earth orbital shells (GEO/LEO) in animation
- The `obj_end_window` clamp behavior for tight-window objects

**Recommended:** Agentic review pass first (read animation pipeline, map touch points against recent changes, produce risk map), then Mode 5 visual testing.

### 5. CAD API Returns 400 for Artemis II
```
[CAD] Network error: HTTP Error 400: Bad Request
```
JPL's Close Approach Database doesn't support spacecraft IDs (-1024). Expected behavior — not a bug, but worth a graceful skip with a specific message rather than generic network error.

### 6. Moon-Centered HypOsc Elements Fail at GUI Epoch
```
[Horizons Error] No ephemeris prior to A.D. 2026-APR-02 01:58:32.3050 TD
```
The HypOsc fetch uses the GUI epoch (02:00 UTC → before 01:58:32 TD boundary). Fix: apply `utc_to_tdb()` to the HypOsc epoch query, same as other Horizons queries. Or better: use derived closest approach time (see Issue 1).

---

## New Standing Conventions

### Session Start File Check
When there are open issues from a handoff, Claude derives a specific file list from "Completed and Delivered" and "Open Issues" and asks Tony to confirm they're current before analyzing any code. Prevents analyzing stale project files.

### `date_source` for Spacecraft Encounters
All new encounters should include `date_source` field. Rule of thumb:
- Event time (burn, reentry, deployment) → `'authoritative'`
- Proximity minimum with OEM data in Horizons → `'horizons'`  
- Future planned encounter → `'planning'`

---

## Files Modified This Session
- `palomas_orrery.py` — date clamping, fetch_requests passthrough, safe_int, window config, auto-scale, fetch_trajectory call sites
- `orbit_data_manager.py` — utc_to_tdb, fetch_complete_orbit_path clamp, strftime %H:%M
- `palomas_orrery_helpers.py` — fetch_trajectory date clamping
- `spacecraft_encounters.py` — resolve_encounter_time(), date_source convention, Artemis II encounter entries
- `celestial_objects.py` — Artemis II start_date/end_date boundaries
- `celestial_coordinates.py` — RA/Dec hover text wrap

---

## Key Insights This Session

**"Peeling the onion"** — Artemis II's tight ephemeris window exposed five independent Horizons query paths that had never needed to agree on date bounds before. Each fix revealed the next layer. The root cause was the parallel pipeline architecture; the stress test was the first object whose ephemeris window fit entirely inside a normal GUI date range.

**UTC vs TDB** — The 69-second offset matters only for tight-window missions at their boundaries. `fetch_trajectory()` passes JD epochs (timescale implicit); `fetch_orbit_path()` passes formatted strings (timescale ambiguous — fixed with `utc_to_tdb()`). Two fetch paths handle timescales differently by accident rather than design — worth documenting.

**Encounter time derivation is data-driven** — Planning estimates can be hours off from actual trajectory data. `resolve_encounter_time()` gives self-correcting encounter times for any mission with Horizons OEM data. Artemis II: planning said Apr 7 23:06, Horizons says Apr 6 23:04 (~24 hours earlier, 599 km closer).

**Auto-scale was Sun-centric by legacy** — The `calculate_axis_range_from_orbits()` function used heliocentric aphelion for all objects, which was correct when Sun was always the center. Non-Sun centers (Moon, Phobos, etc.) now use distance-from-center instead.

---

## Submission Project
Separate handoff: `submission_project_handoff.md` (updated with Claude's observation, April 4, 2026).
Three documents planned: academic submission, pygame/wargaming community piece, Anthropic letter.
Ready for dedicated drafting session.

---

*Session conducted April 4, 2026*
*Claude (Anthropic, claude-sonnet-4-6)*
*Module credit: spacecraft_encounters.py updated April 4, 2026 with Anthropic's Claude 4.6*
