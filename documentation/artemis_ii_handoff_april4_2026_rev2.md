# Artemis II Implementation Handoff — April 4, 2026 (rev. 2)
**Session summary:** Bug fixes, architectural improvements, encounter time derivation. Rev. 2 adds HypOsc epoch fix, utc_to_tdb propagation, and resolve_encounter_time caching.
**Protocol version:** v3.17

---

## Session Accomplishments

### 1–8. (unchanged from rev. 1)
*(All items from the original handoff remain complete as documented.)*

### 9. HypOsc Epoch Fix — Spacecraft Encounter Fallback (`palomas_orrery.py`)
**Problem:** Full mission Moon-centered plot showed `q=83,203 km` (elements fetched at GUI epoch Apr 2 02:00). Go button showed correct `q=8,318 km` (elements at Apr 7 23:06 planning estimate).

**Fix:** Added "Capability C-pre" block in `_add_close_approach_extras()`, between the CAD block (Capability B) and the HypOsc call (Capability C). When `best_approach is None` and the object is a spacecraft (`id_type='id'`), the block:
1. Looks up encounters tagged `date_source='horizons'` whose `target` matches the current center body
2. Calls `resolve_encounter_time()` to derive the actual closest approach time from Horizons
3. Converts the datetime to JD and synthesizes a minimal `approach` dict with `'jd'` key
4. Passes it to `plot_hyperbolic_osculating_orbit()` — which already knew how to use it

**Result:** Full mission plot now fetches elements at `2026-04-06 23:03:59`, giving `q=9,600 km` — physically correct osculating geometry at closest approach. (Small residual vs. 8,301 km is expected: osculating elements describe an instantaneous conic, not a precision propagated trajectory.)

**Guard:** Only fires when `best_approach is None` AND `id_type == 'id'`. Zero impact on asteroid/comet paths.

### 10. UTC → TDB Fix for HypOsc Epoch Query (`osculating_cache_manager.py`)
**Problem:** `fetch_osculating_elements()` formatted the epoch as `date.strftime('%Y-%m-%d')` — date only, midnight UTC. For Artemis II at the GUI epoch (`02:00 UTC → 01:58:51 TDB`), this landed just before the ephemeris start, producing a Horizons boundary error before the C-pre fallback could fire.

**Fix:** Replace the `date_str` line with:
```python
try:
    from orbit_data_manager import utc_to_tdb
    date_str = utc_to_tdb(date).strftime('%Y-%m-%d %H:%M')
except Exception:
    date_str = date.strftime('%Y-%m-%d')  # fallback: date-only, no TDB
```
Consistent with `orbit_data_manager.py` which already applied `utc_to_tdb()` to orbit path fetches.

### 11. `resolve_encounter_time()` Session Cache (`spacecraft_encounters.py`)
**Problem:** `resolve_encounter_time()` was called twice per Moon-centered Artemis II plot — once by the C-pre HypOsc block, once by `add_tagged_encounter_markers()`. Four Horizons queries (coarse + fine, twice) for the same result.

**Fix:** Two changes:
- Cache check at top of `resolve_encounter_time()`: if `'_resolved'` key exists on `enc`, return it immediately
- Store result on `enc['_resolved']` before returning

`enc` is the original dict from `SPACECRAFT_ENCOUNTERS` — shared by both callers within a session. First caller populates; second caller hits cache. Resets naturally on restart (in-memory only — correct for live mission data).

**Result:** Four Horizons queries → two per plot. Log will show `[RESOLVE] Using cached result for Lunar Closest Approach` on the second call.

---

## Open Issues

### ~~1. HypOsc Epoch Should Use Derived Closest Approach Time~~ ✓ Fixed (Accomplishment 9)

### 2. Duplicate `get_end_date_from_gui()` at line ~7762
Still uses bare `int()` calls with `try/except` fallback (returns `start + 365 days` on error). Should be updated to match the `safe_int()` pattern at line ~7560. The live definition is at ~7762 (last wins in Python).

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
JPL's Close Approach Database doesn't support spacecraft IDs (-1024). Expected behavior — not a bug, but worth a graceful skip with a specific message rather than generic network error.

### ~~6. Moon-Centered HypOsc Elements Fail at GUI Epoch~~ ✓ Fixed (Accomplishment 10)

### ~~7. `resolve_encounter_time()` Called Twice — Double Horizons Round-Trip~~ ✓ Fixed (Accomplishment 11)

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

**Rev. 1:**
- `palomas_orrery.py` — date clamping, fetch_requests passthrough, safe_int, window config, auto-scale, fetch_trajectory call sites
- `orbit_data_manager.py` — utc_to_tdb, fetch_complete_orbit_path clamp, strftime %H:%M
- `palomas_orrery_helpers.py` — fetch_trajectory date clamping
- `spacecraft_encounters.py` — resolve_encounter_time(), date_source convention, Artemis II encounter entries
- `celestial_objects.py` — Artemis II start_date/end_date boundaries
- `celestial_coordinates.py` — RA/Dec hover text wrap

**Rev. 2:**
- `palomas_orrery.py` — Capability C-pre block (HypOsc spacecraft encounter epoch fallback)
- `osculating_cache_manager.py` — utc_to_tdb applied to HypOsc epoch query
- `spacecraft_encounters.py` — resolve_encounter_time() session cache (_resolved key)

---

## Key Insights This Session

**"Peeling the onion"** — Artemis II's tight ephemeris window exposed five independent Horizons query paths that had never needed to agree on date bounds before. Each fix revealed the next layer. The root cause was the parallel pipeline architecture; the stress test was the first object whose ephemeris window fit entirely inside a normal GUI date range.

**UTC vs TDB** — The 69-second offset matters only for tight-window missions at their boundaries. `fetch_trajectory()` passes JD epochs (timescale implicit); `fetch_orbit_path()` passes formatted strings (timescale ambiguous — fixed with `utc_to_tdb()`). Two fetch paths handle timescales differently by accident rather than design — worth documenting.

**Encounter time derivation is data-driven** — Planning estimates can be hours off from actual trajectory data. `resolve_encounter_time()` gives self-correcting encounter times for any mission with Horizons OEM data. Artemis II: planning said Apr 7 23:06, Horizons says Apr 6 23:04 (~24 hours earlier, 599 km closer).

**Auto-scale was Sun-centric by legacy** — The `calculate_axis_range_from_orbits()` function used heliocentric aphelion for all objects, which was correct when Sun was always the center. Non-Sun centers (Moon, Phobos, etc.) now use distance-from-center instead.

**HypOsc epoch is data-driven, not GUI-driven** — For spacecraft with Horizons OEM data, the osculating element epoch should always be the derived closest approach time, not the GUI date. The CAD `approach['jd']` path in `idealized_orbits.py` already supported this — the C-pre block just needed to feed it the right epoch from `resolve_encounter_time()` instead of from the CAD API.

**utc_to_tdb belongs at every Horizons string boundary** — Any code that formats a datetime as a string for a Horizons query needs `utc_to_tdb()` applied first. The 69-second offset is invisible until a mission's ephemeris window is tight enough that midnight UTC lands before the TDB boundary. Pattern: `utc_to_tdb(date).strftime('%Y-%m-%d %H:%M')`.

**In-memory caching on the enc dict** — For derived values that are expensive (two Horizons queries) but stable within a session, caching directly on the source dict (`enc['_resolved']`) is simpler than a separate cache structure. Resets on restart, which is correct for live mission data.

---

## Submission Project
Separate handoff: `submission_project_handoff.md` (updated with Claude's observation, April 4, 2026).
Three documents planned: academic submission, pygame/wargaming community piece, Anthropic letter.
Ready for dedicated drafting session.

---

*Session conducted April 4, 2026*
*Claude (Anthropic, claude-sonnet-4-6)*
*Module credit: spacecraft_encounters.py, osculating_cache_manager.py, palomas_orrery.py updated April 4, 2026 with Anthropic's Claude 4.6*
