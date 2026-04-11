# C/2025 K1 Fragment Implementation — Handoff v3
## March 28, 2026

---

## Status: DATA LAYER COMPLETE — PRESENTATION LAYER NEXT

All four fragment trajectories (A/parent, B, C, D) fetch, plot, and display correctly.
Colors are distinct, Fragment C (gold/bound) stands out, comet tails suppressed on fragments.
Next session focuses on encounter-scale rendering quality and the Go: Breakup preset.

---

## Changes Applied (11 total across 3 files)

### celestial_objects.py (6 changes)
1. Parent K1 `id` changed from `'C/2025 K1'` to `'90004912'` (numeric SPK-ID)
2. Parent K1 `id_type` changed from `'smallbody'` to `'id'`
3. Parent K1 `mission_info` updated with breakup narrative + `<br>` line breaks
4. Three fragment entries added (K1-B, K1-C, K1-D) with `show_tails: False`
5. Fragment `mission_info` strings use `<br>` for line breaks
6. Fragment entries use designation IDs (C/2025 K1-B etc.) with `id_type: 'smallbody'`

### constants_new.py (3 changes)
1. Fragment colors added to `color_map`: B=rgb(0,200,220) teal, C=rgb(255,215,0) gold, D=rgb(100,180,255) sky blue
2. Fragment orbital periods added (all `None`)
3. Fragment info text entries added with full scientific descriptions

### palomas_orrery.py (4 changes)
1. Three fragment IntVar declarations added (after comet_2025k1_var)
2. Static `is_comet` check: `id_type in ['smallbody', 'id']` + `show_tails` guard
3. Animation `is_comet` check: same fix (also fixed pre-existing `'orbital'`-only bug to include `'trajectory'`)
4. Fragment checkboxes added to UI (indented under parent K1, with tooltips)

---

## Issues Found and Fixed During Testing

### Issue 1: JPL Ambiguity (FIXED)
- `C/2025 K1` as smallbody designation became ambiguous when JPL added fragment records
- **Fix**: Changed parent to numeric SPK-ID `90004912` with `id_type: 'id'`
- **Lesson**: When JPL adds fragments/variants, the parent designation becomes ambiguous. Use numeric SPK-ID. This would have broken even without our changes.

### Issue 2: Comet tails not rendering for parent (FIXED)
- `is_comet` check required `id_type == 'smallbody'`, excluded parent after switching to `id_type: 'id'`
- **Fix**: Changed to `id_type in ['smallbody', 'id']`
- Also fixed pre-existing bug: animation path only checked `'orbital'` not `['orbital', 'trajectory']`

### Issue 3: Hover text overflow (FIXED)
- Long `mission_info` strings ran off hover box edge
- **Fix**: Added `<br>` tags between sentences in `mission_info` strings
- **Root cause**: `visualization_utils.py` line 578 inserts `mission_info` raw — no `\n` to `<br>` conversion

### Issue 4: "Bad dates" cache update warnings (PRE-EXISTING, NOT FIXED)
- Cache manager tries to extend already-current data, produces harmless warnings
- Not caused by our changes, not blocking

### Issue 5: AstropyDeprecationWarning for id_type='id' (PRE-EXISTING)
- `astroquery` warns `id_type='id'` deprecated in favor of `None`
- Still functional, will need updating when astroquery removes old API

---

## Test Results

| Test | Status | Notes |
|------|--------|-------|
| Pre-test: Horizons IDs | PASS | All fragment designations resolve as smallbody |
| Test 1: Clean launch | PASS | No errors, [CENTER MENU] reached |
| Test 2: Fragment checkboxes | PASS | All three visible, indented, tooltips work |
| Test 3: Parent K1 still works | PASS | After SPK-ID, id_type, and is_comet fixes |
| Test 4: Single fragment fetch | PASS | Correct color (teal), no tails |
| Test 5: All fragments together | PASS | Four traces, correct colors, parent-only tails |
| Test 6: Zoom verification | PASS | D > B > C ordering correct. Rendering issues at encounter scale (see below) |
| Test 7: Color distinction | PASS | Gold C stands out, all colors readable on dark background |
| Test 8: Animation guard | PENDING | Not yet tested |

---

## Encounter-Scale Rendering Issues (Observed in Test 6)

At fly-to zoom scale (~0.1 AU view cube), two rendering problems were identified:

### 1. Osculating orbit visibility
- The analytical Keplerian/hyperbolic conics are rendered with fixed angular resolution
- At encounter scale, the visible portion of the arc contains too few points
- For 2 of 4 fragments, the osculating orbit is NOT VISIBLE in the fly-to view
- For the other 2, only fragmentary dots appear — not informative
- **Need**: Higher angular resolution OR continuous line rendering (`mode='lines'`)
- **Location**: Likely in `idealized_orbits.py` or the Keplerian orbit plotting code

### 2. Trajectory point density
- Trajectory traces use 51 points over 317 days (~6 day spacing)
- At encounter scale, individual points are visible but the line connecting them looks continuous (yellow plotted period)
- The white trajectory trace (full mission) may appear discontinuous
- **Need**: Adaptive point density — tighter time step in the perihelion region
- **Pattern**: Same adaptive resolution from spacecraft encounter work (curvature scale = pi * dist_km / v_kms)

### 3. Comet tail particle scale
- Green coma/tail particles are sized for solar system scale
- At fly-to scale they dominate the view, obscuring the fragment geometry
- Not a blocker — tail viz can be toggled off in legend — but worth noting for curation

---

## Next Session: Presentation Layer

### Priority 1: Osculating orbit rendering at encounter scale
- Make analytical conics render as continuous lines with enough resolution for any zoom level
- Check how the Keplerian orbit trace is generated — mode, point count, angular range
- May need to increase default angular resolution or add zoom-adaptive point generation

### Priority 2: Trajectory point density for perihelion region
- Adaptive fetch resolution for fragments around perihelion
- The encounter resolution formula already exists: curvature_scale = pi * dist_km / v_kms
- At perihelion (q=0.334 AU, v=72.9 km/s): step ~ pi * 50M km / 72.9 ~ 2.2M km spacing
- This translates to roughly 30-minute to 1-hour time steps near perihelion

### Priority 3: Go: Breakup preset
- Button alongside "Go: Perihelion" in the checkbox area
- Sets date range to perihelion window (Oct 7 - Nov 30?)
- Sets scale to encounter cube (~0.005-0.01 AU half-width)
- Centers on parent K1 position
- Same implementation pattern as existing Go: Perihelion presets

### Priority 4: Gallery Studio curation for portrait
- Fly-to green checkboxes already exist in Studio (rediscovered during session!)
- Check the green box on parent K1 trace
- Export portrait mode for iOS
- Fly-to button appears in gallery viewer, survives updatemenus stripping

---

## Data Summary

### Fragment Orbital Properties (from JPL Horizons)
| Property | Parent/A | Fragment B | Fragment C | Fragment D |
|----------|----------|------------|------------|------------|
| SPK-ID | 90004912 | 90004913 | 90004914 | 90004915 |
| Horizons ID | 90004912 | C/2025 K1-B | C/2025 K1-C | C/2025 K1-D |
| id_type | id | smallbody | smallbody | smallbody |
| e | 1.00026 | 1.00203 | 0.99999 | 1.00246 |
| QR (AU) | 0.3342 | 0.3358 | 0.3339 | 0.3363 |
| Tp (UTC) | 10:33:16 | 10:51:34 | 10:33:26 | 10:55:34 |
| Non-grav | A1/A2/A3 | none | none | none |
| Obs count | 2395 | 278 | 158 | 107 |
| JPL soln | #31 | #13 | #14 | #5 |
| Bound? | Hyperbolic | Hyperbolic | **ELLIPTICAL** | Hyperbolic |
| Color | cyan | teal | **gold** | sky blue |

### Separation Timeline
| Date | B-A (km) | C-A (km) | D-A (km) |
|------|----------|----------|----------|
| Oct 7 (pre-perihelion) | 308,513 | 72,857 | 408,123 |
| Oct 8 (perihelion) | 282,993 | 67,049 | 374,456 |
| Nov 25 (cluster minimum) | 69,874 | 11,063 | 85,816 |
| Jan 15 | 310,379 | 47,806 | 386,927 |
| Mar 21 | 729,588 | 111,322 | 910,797 |

### Convergence Analysis
- Osculating models never converge to zero separation
- Minimum cluster size: ~Nov 25 (max pairwise distance 96,381 km)
- Tightest pair (A-C): 10,718 km on Nov 28 (less than Earth diameter)
- Widest pair (B-D): 17,684 km on Nov 27
- Non-convergence due to: parent has non-grav forces modeled, fragments don't
- Convergence date (~Nov 25) is AFTER actual breakup (~Oct 16) — backward extrapolation artifact

### Key Science
- Breakup ~Oct 16, 2025 (8 days post-perihelion at 0.33 AU, inside Mercury's orbit)
- Hubble Space Telescope observations Nov 2025, published Icarus Feb 2026 (Auburn University)
- Fragment C unique: e=0.99999, still gravitationally bound while siblings escape
- Fragment C return period ~13 million years
- Chemically unusual: extreme depletion of carbon-bearing species (ground-based)
- Four smooth Keplerian-like curves with no discontinuities at breakup moment

---

## Comet Structure Notes (for future reference)

### show_tails flag
- Fragments have `'show_tails': False` in celestial_objects.py
- Guards added to both static (line ~5539) and animation (line ~6817) is_comet checks
- Pattern: `obj.get('show_tails', True)` — defaults to True, only fragments suppress

### Sun-at-origin assumption (NOT FIXED — future work)
- `comet_visualization_shells.py` lines 490, 658, 799 compute sun direction as `position / |position|`
- `center_object_name` parameter accepted but never used (dead code)
- Tails point wrong direction when center != Sun
- Not a problem for heliocentric fragment visualization

### Parent K1 not in HISTORICAL_TAIL_DATA
- Console shows: `[COMET VIZ] C/2025_K1 not in database, using default parameters`
- Works fine with defaults but could be improved with K1-specific tail properties
- Low priority — the comet has fragmented, so accurate tail viz is less critical

---

## Lessons Learned This Session

- **JPL fragment ambiguity**: When JPL adds fragment records, parent designation becomes ambiguous. Use numeric SPK-ID. This is an external change that can break existing code without any code changes on our end.
- **is_comet detection should not depend on id_type**: The `symbol == 'diamond'` is the real comet marker. `id_type` is about Horizons query format, not object identity.
- **Hover text line breaks**: Use `<br>` directly in `mission_info`, not `\n` — the pipeline doesn't convert.
- **Gallery Studio fly-to checkboxes already exist**: Green checkboxes per trace, up to 4 targets, generate compact navigation buttons that survive portrait mode. No new code needed for fly-to in portrait.
- **Osculating orbits need zoom-adaptive rendering**: Fixed angular resolution doesn't work at encounter scale. Need either higher default resolution or adaptive point generation.
- **The fly-to view reveals rendering assumptions**: Features designed for solar-system scale (comet particles, point spacing, osculating orbit resolution) break down at encounter scale. Each zoom level has its own rendering requirements.
