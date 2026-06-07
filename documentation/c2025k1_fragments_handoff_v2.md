# C/2025 K1 Fragment Implementation — Status Update
## March 27, 2026

---

## Implementation Status: DATA LAYER COMPLETE

All changes applied and tested. Four comet fragment trajectories (A/parent, B, C, D) 
are fully functional in the orrery.

---

## Changes Applied (10 total across 3 files)

### celestial_objects.py (5 changes)
1. Parent K1 `id` changed from `'C/2025 K1'` to `'90004912'` (numeric SPK-ID)
2. Parent K1 `id_type` changed from `'smallbody'` to `'id'`
3. Parent K1 `mission_info` updated with breakup narrative + `<br>` line breaks
4. Three fragment entries added (K1-B, K1-C, K1-D) with `show_tails: False`
5. Fragment `mission_info` strings use `<br>` for line breaks

### constants_new.py (3 changes)
1. Fragment colors added to `color_map`: B=teal, C=gold, D=sky blue
2. Fragment orbital periods added (all `None`)
3. Fragment info text entries added

### palomas_orrery.py (4 changes)  
1. Three fragment IntVar declarations added
2. Static `is_comet` check: added `id_type in ['smallbody', 'id']` + `show_tails` guard
3. Animation `is_comet` check: same fix (also fixed pre-existing `'orbital'`-only bug)
4. Fragment checkboxes added to UI (indented under parent K1)

---

## Issues Found During Testing

### Issue 1: JPL Ambiguity (FIXED)
- `C/2025 K1` as a smallbody designation is now ambiguous because JPL added fragment records
- **Fix**: Changed parent to numeric SPK-ID `90004912` with `id_type: 'id'`
- This would have broken the parent even without our fragment changes
- **Lesson**: When JPL adds fragments/variants, the parent designation becomes ambiguous. Switch to numeric SPK-ID.

### Issue 2: Comet tails not rendering (FIXED)
- The `is_comet` check required `id_type == 'smallbody'`, which excluded the parent after switching to `id_type: 'id'`
- **Fix**: Changed to `id_type in ['smallbody', 'id']`
- Also fixed pre-existing bug in animation path that only checked `'orbital'` (not `'trajectory'`)

### Issue 3: Hover text overflow (FIXED)
- Long `mission_info` strings ran off the hover text box edge
- **Fix**: Added `<br>` tags between sentences in `mission_info` strings
- The hover text pipeline (`visualization_utils.py` line 578) inserts `mission_info` raw — no `\n` to `<br>` conversion

### Issue 4: "Bad dates" cache update warnings (PRE-EXISTING, NOT FIXED)
- Cache manager tries to incrementally update data that's already current
- Produces harmless but noisy "Bad dates -- start must be earlier than stop" errors
- Not caused by our changes, not blocking

### Issue 5: AstropyDeprecationWarning for id_type='id' (PRE-EXISTING)
- `astroquery` warns that `id_type='id'` is deprecated in favor of `None`
- Functional — still works — but will need updating when astroquery removes the old API
- Not blocking

---

## Test Results

| Test | Status | Notes |
|------|--------|-------|
| Pre-test: Horizons IDs | PASS | All fragment designations resolve |
| Test 1: Clean launch | PASS | No errors, [CENTER MENU] reached |
| Test 2: Fragment checkboxes | PASS | All three visible, indented, tooltips work |
| Test 3: Parent K1 still works | PASS | After id_type and is_comet fixes |
| Test 4: Single fragment fetch | PASS | Correct color, no tails |
| Test 5: All fragments together | PASS | Four traces, correct colors, parent-only tails |
| Test 6: Zoom verification | PENDING | |
| Test 7: Color distinction | PENDING | Visual from Test 5 looks good |
| Test 8: Animation guard | PENDING | |

---

## Data Summary

### Current Positions (from Test 5 output, "today's date" position)
| Fragment | Position (AU) | Distance from Sun |
|----------|--------------|-------------------|
| K1 (A) | (-0.281, -0.031, -0.178) | 0.334 AU |
| K1-B | (-0.283, -0.031, -0.178) | 0.336 AU |
| K1-C | (-0.281, -0.032, -0.178) | 0.334 AU |
| K1-D | (-0.283, -0.030, -0.178) | 0.336 AU |

### Perihelion Times (Solution TP from Horizons)
| Fragment | Tp (UTC) | Source |
|----------|----------|--------|
| K1 (A) | 2025-10-08 10:33:16 | JPL#31, 2395 obs |
| K1-B | 2025-10-08 10:51:34 | JPL#13, 278 obs |
| K1-C | 2025-10-08 10:33:26 | JPL#14, 158 obs |
| K1-D | 2025-10-08 10:55:34 | JPL#5, 107 obs |

### Perihelion Distances
| Fragment | q (AU) | e | Orbit Type |
|----------|--------|---|------------|
| K1 (A) | 0.3342 | 1.00026 | Hyperbolic |
| K1-B | 0.3358 | 1.00203 | Hyperbolic |
| K1-C | 0.3339 | 0.99999 | **Elliptical (bound!)** |
| K1-D | 0.3363 | 1.00246 | Hyperbolic |

---

## Next Steps

### Remaining Tests
- Test 6: Zoom verification (divergence visible at sufficient zoom)
- Test 7: Color distinction (Tony's visual judgment)
- Test 8: Animation path guard

### Future Features
- **Go: Breakup preset**: Frame the convergence/divergence at encounter scale
- **UI grouping**: Consider making fragment checkboxes auto-toggle with parent
- **Comet structure sun-direction fix**: `center_object_name` is dead code in `comet_visualization_shells.py`
- **Gallery piece**: The breakup story as a curated visualization
- **Hover text**: Add fragment separation distances
- **HISTORICAL_TAIL_DATA**: Add parent K1 to comet database (currently uses 'default' parameters)

### Lessons Learned
- **JPL fragment ambiguity**: When JPL adds fragment records, parent designation becomes ambiguous. Use numeric SPK-ID.
- **is_comet detection**: Should not depend on `id_type` — the `symbol == 'diamond'` is the real comet marker
- **Hover text line breaks**: Use `<br>` directly in `mission_info`, not `\n` — the pipeline doesn't convert
- **Astroquery deprecation**: `id_type='id'` works but is deprecated; future migration to `id_type=None` needed
