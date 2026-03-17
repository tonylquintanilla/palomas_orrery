# Spacecraft Mission Explorer -- Handoff Document

**Project:** Paloma's Orrery
**Sessions:** March 11-15, 2026
**Status:** Stage A complete. Stage B complete and verified. Adaptive resolution IMPLEMENTED and verified. Position marker, center body hover, additive presets -- all verified. Ready to expand to more spacecraft.
**Supersedes:** Pairwise encounter computation approach (abandoned -- date grid mismatch)
**Related:** `apophis_handoff.md` (CAD API pattern), `spacecraft_encounter_integration.md` (retired pairwise design)

---

## The Insight

Every spacecraft encounter we care about is *already known*. New Horizons at Pluto:
July 14, 2015 11:49:57 UTC, 12,472 km. These are famous, well-documented moments from
NASA mission pages, press releases, and JPL's own Horizons system notes.

The original pairwise computation approach tried to *discover* encounters from trajectory
data. This failed because spacecraft and target have different date grids (different
`dates_list` time steps), so ISO string matching finds zero overlaps. The fix isn't
better matching -- it's recognizing that we already have the data.

**Three authoritative epoch sources, one visual language:**

| System | Object type | Epoch source | Position source |
|--------|-------------|--------------|-----------------|
| CAD API | Small body -> planet | JPL CAD database | Horizons at CAD JD |
| Perihelion | Comet -> Sun | Tp from elements | Horizons at Tp |
| **Mission Explorer** | **Spacecraft -> any** | **Tagged dict** | **Horizons at tagged date** |

Same pattern: authoritative epoch + Horizons position fetch = precision marker.

---

## Stage A: COMPLETE (March 12, 2026)

### What Was Built

**New module: `spacecraft_encounters.py`**

Contains:
- `SPACECRAFT_ENCOUNTERS` dict: tagged encounter data for New Horizons (test case)
- `SPACECRAFT_FULL_MISSION` dict: full mission presets with `fetch_step` field
- `get_encounters_for_spacecraft(name)` -> list of encounter dicts
- `get_encounters_in_date_range(name, start, end)` -> filtered list
- `get_full_mission_preset(name)` -> full mission preset dict or None
- `get_encounter_preset(name, index)` -> encounter close-up preset with adaptive resolution
- `_calculate_encounter_resolution(enc)` -> derives cube scale, fetch step, time window from geometry
- `_snap_to_horizons_step(ideal_step_sec)` -> maps ideal step to Horizons-compatible string
- `add_tagged_encounter_markers(fig, ...)` -> integration function called from palomas_orrery.py
- `add_tagged_encounter_marker(fig, encounter, position, ...)` -> places single marker
- `fetch_position_at_encounter(encounter, center_id, spacecraft_id)` -> Horizons position at tagged epoch
- `_format_encounter_hover(encounter, spacecraft_name)` -> full hover text with resolution_note support
- `_wrap_text(text, width)` -> word-wrap for hover tooltips

**Modified: `palomas_orrery.py`**

Replaced `_add_spacecraft_encounter_markers()` (the pairwise version, ~150 lines) with a
~40-line delegator that imports from `spacecraft_encounters.py`. Same function name, same
signature -- both Pipeline call sites unchanged. Graceful fallback if module not found.

### Encounter Dict Structure

```python
{
    'target': 'Pluto',               # Target body name (must match objects list)
    'date': '2015-07-14 11:49:57',   # UTC datetime string (authoritative epoch)
    'type': 'flyby',                 # flyby | gravity_assist | orbit_insertion | etc.
    'dist_km': 12472,                # Known closest approach distance (km)
    'dist_au': 12472 / AU_KM,        # Also in AU (per hover text convention)
    'v_kms': 13.78,                  # Relative velocity at encounter (km/s, target-relative)
    'v_helio_kms': 14.52,            # Heliocentric velocity at encounter (km/s, Sun-relative)
    'label': 'Pluto Flyby',          # Display label for GUI and marker
    'note': 'First spacecraft...',   # Educational note for hover text (encounter-specific)
    'resolution_note': '...',        # Optional: transparency about trajectory precision
    'status': 'completed',           # completed | planned | canceled
    'source': 'NASA/JPL',            # Data attribution
    'center': 'Sun',                 # Suggested center body (heliocentric view)
    'select_also': ['Pluto'],        # Objects to auto-select
    'plot_days': 28,                 # Heliocentric view window (days)
    'plot_scale_au': 0.5,            # Heliocentric view scale (AU), None for auto
    'center_closeup': 'Pluto',       # Target-centered view (None = use 'center' fallback)
    'plot_days_closeup': 14,         # Fallback only; adaptive resolution supersedes
    'plot_scale_au_closeup': 0.002,  # Fallback only; adaptive resolution supersedes
}
```

### New Horizons Encounters (Test Case)

| Encounter | Date (UTC) | Distance | v (target) | v (Sun) | Type |
|-----------|-----------|----------|------------|---------|------|
| Jupiter Gravity Assist | 2007-02-28 05:43:40 | 2,305,000 km (0.01541 AU) | 21.22 km/s | 23.00 km/s | gravity_assist |
| Pluto Flyby | 2015-07-14 11:49:57 | 12,472 km (0.0000834 AU) | 13.78 km/s | 14.52 km/s | flyby |
| Arrokoth Flyby | 2019-01-01 05:33:22 | 3,538 km (0.0000237 AU) | 14.43 km/s | 13.87 km/s | flyby |

### Marker Visual Language

- White square-open marker at spacecraft's heliocentric position at encounter epoch
- Hover text includes: label, date, distance (AU + km), both velocities with reference frame labels, encounter type, educational note (word-wrapped at ~50 chars), resolution note (when present), data source
- Legend entry: `"{SC Name} {label}"` e.g. "New Horizons Pluto Flyby"
- Console log: `[ENCOUNTER] New Horizons Pluto Flyby: 12,472 km (0.0000834 AU), 13.78 km/s ...`
- Visual language: open squares = positions/events in space (consistent with CAD and apsidal markers); filled symbols = objects

### Velocity Narrative (Key Lesson)

The hover text tells the velocity story in the correct reference frame. For Jupiter GA:

> Fastest launch ever: 16.26 km/s Earth-relative, combining with Earth's orbital
> velocity to ~43 km/s heliocentric (velocities add as vectors, not scalars). The
> Sun's gravity steadily slowed it to ~19 km/s by Jupiter. The gravity assist added
> ~4 km/s, boosting speed to ~23 km/s -- partially recovering what the Sun took.

The full heliocentric velocity arc: 43 -> 19 -> 23 -> 14.5 -> 13.9 km/s. Each encounter
marker shows both target-relative and Sun-relative velocities explicitly labeled.

### Stage A Test Results

| Test | Setup | Result |
|------|-------|--------|
| 1. NH + Pluto (canonical) | Sun-centered, 2015 | White diamond marker, hover correct, console log correct |
| 2. NH + Jupiter (gravity assist) | Sun-centered, 2006-2008 | Marker near Jupiter, velocity narrative verified |
| 3. All three encounters | Sun-centered, 2006-2020 | Three markers along full mission trajectory |
| 4. Encounter outside plotted period | Sun-centered, 2020-2025 | Markers appear on full mission trace (by design) |
| 6. Closest approach OFF | Same as Test 1, markers OFF | No encounter markers, clean legend |

**Design decision (Test 4):** Encounter markers appear whenever the encounter falls within
the full mission date range, even if outside the plotted period window. The full mission
trace is visible, and the markers provide context. User can toggle off in legend.

---

## Stage B: COMPLETE AND VERIFIED (March 12-14, 2026)

### What Was Built

**GUI Go buttons** under each spacecraft checkbox (always visible, educational):

```
[ ] New Horizons (2006-01-19 to 2029-12-31)
      [Go: Full Mission]  [Go: Jupiter Gravity Assist]  [Go: Pluto Flyby]
      [Go: Arrokoth Flyby]
```

3-column grid layout, indented 25px under the checkbox. Number of buttons varies per
spacecraft (determined by entries in `SPACECRAFT_ENCOUNTERS` and `SPACECRAFT_FULL_MISSION`).
Wraps to next row at 3 columns for compactness with future missions.

### Preset Behavior (Adaptive Resolution)

Each Go button applies its preset additively -- ensures preset objects are checked but preserves
any additional objects the user has already selected (satellites, extra planets, etc.).
Encounter presets derive scale, fetch step, and time window from encounter geometry.
Full Mission restores `6h` default interval.

| Button | Center | Date Range | Scale (AU) | Step | select_also |
|--------|--------|-----------|------------|------|-------------|
| Full Mission | Sun | 2006-01-20 to 2020-01-01 | Auto | 6h | Earth, Jupiter, Pluto, Arrokoth |
| Jupiter GA | Jupiter | ~15 days around 2007-02-28 | 0.0616 | 3h | Jupiter |
| Pluto Flyby | Pluto | ~3 hrs around 2015-07-14 11:49 | 0.000334 | 1m | Pluto |
| Arrokoth Flyby | Arrokoth | ~49 min around 2019-01-01 05:33 | 0.0000946 | 1m | Arrokoth |

### Key Implementation Details

**`spacecraft_encounters.py` changes:**
1. **`_calculate_encounter_resolution(enc)`**: Derives all preset values from `dist_km` and `v_kms`:
   - Cube scale: `dist_km * 4 / AU_KM`
   - Arc resolution: `pi * dist_km / v_kms / 30` -> snap to Horizons step
   - Time window: `dist_km * 8 / v_kms * 1.5` (cube crossing with margin)
   - Minimum 10 minute window
2. **`_snap_to_horizons_step()`**: Maps ideal step to `1m/5m/10m/30m/1h/2h/3h/6h`
   (3h tier added during implementation -- Jupiter GA ideal step of 11,373 sec falls
   between 2h and 6h thresholds; without 3h tier it snapped to 6h)
3. **`get_encounter_preset()`** rewritten: Uses adaptive resolution when `v_kms` available,
   falls back to whole-day logic with manual dict values when missing. Returns `fetch_step`
   field and full datetime strings with hours/minutes.
4. **`SPACECRAFT_FULL_MISSION`** now includes `fetch_step: '6h'` -- restores default
   interval when returning from fine-grained encounter views.
5. **`resolution_note`** field on Pluto and Arrokoth encounters: transparency about
   trajectory precision in hover text.
6. **Arrokoth dict fixed**: `date` -> `'05:33:22'` (JPL authoritative), `center_closeup`
   -> `'Arrokoth'`, fallback values updated.

**`palomas_orrery.py` changes:**
1. **`_apply_mission_preset()`** enhanced:
   - Parses both `'%Y-%m-%d'` and `'%Y-%m-%d %H:%M:%S'` datetime formats
   - Fills hour/minute GUI widgets (was hardcoded to 0)
   - Uses `total_seconds() / 86400` with `max(1, ...)` for sub-day `days_to_plot`
   - Sets `trajectory_interval_entry` to preset's `fetch_step` before triggering plot
   - **Additive presets** -- ensures preset objects are checked, preserves user selections
   - **Clears `_was_checked` shadow flag** only for previous center body
   - **Stores encounter epoch** in `_encounter_plot_date[0]` for position marker override
2. **Go button layout**: 3-column grid (`grid()` with `sticky='w'`) instead of horizontal
   `pack(side='left')`. Prevents button truncation in narrow left pane.
3. **Tooltip bug fixed**: `distance_au` -> `dist_au`. Tooltips now include adaptive
   resolution info (step + window) and encounter type.
4. **Full Mission tooltip** includes `select_also` object names.

### Stage B Verification Results (March 14, 2026)

| Test | Result | Notes |
|------|--------|-------|
| 1. Full Mission button | PASS | Center=Sun, dates correct, Auto scale, all objects checked, 3 encounter markers |
| 2. Jupiter GA button | PASS | Center=Jupiter, ~15 day window, 3h step, smooth curved trajectory |
| 3. Pluto Flyby button | PASS | Center=Pluto, ~3 hr window, 1m step, encounter marker on trajectory |
| 4. Arrokoth Flyby button | PASS | Center=Arrokoth, ~49 min window, 1m step, encounter marker visible |
| 5. Sequential: Full -> Pluto -> Arrokoth -> Full | PASS | Each preset overrides cleanly, no leftover state |
| 6. Tooltips | PASS | All buttons show encounter details + resolution info |
| 7. Closest Approach OFF | PASS | No encounter markers; re-enable restores them |

### Bugs Found and Fixed During Verification

1. **Carryover traces from previous center body.** `on_center_change()` has a shadow/restore
   mechanism -- when an object stops being the center, it restores the checkbox if
   `_was_checked` is True. The uncheck-all loop cleared checkboxes but left `_was_checked`
   set. Fix: clear `_was_checked = False` on all objects during uncheck-all.

2. **Go button truncation.** 4 horizontal buttons (~546px) exceeded the left pane width
   (~417px available). Fix: switched from `pack(side='left')` to 3-column `grid()` layout.

3. **Tooltip bug.** `enc.get('distance_au', '?')` referenced a nonexistent key; correct
   key is `dist_au`. Fix: use `enc.get('dist_au', 0)` with formatted display.

---

## Adaptive Encounter Resolution -- IMPLEMENTED (March 14, 2026)

### The Design

Everything derives from two numbers already in the encounter dict: **`dist_km`** (the
authoritative flyby distance) and **`v_kms`** (the encounter velocity).

**Calculation chain:**

```
1. CUBE SCALE (framing):
   cube_half_width_km = dist_km * 4
   plot_scale_au = cube_half_width_km / 149597870.7

2. ARC RESOLUTION (curvature):
   arc_length_km = pi * dist_km          # semicircle through perijove
   arc_time_sec = arc_length_km / v_kms   # time to traverse the curve
   ideal_step_sec = arc_time_sec / 30     # target ~30 points through arc

3. SNAP TO HORIZONS STEP:
   if step < 120:      '1m'
   elif step < 300:    '5m'
   elif step < 600:    '10m'
   elif step < 1800:   '30m'
   elif step < 5400:   '1h'
   elif step < 10800:  '2h'
   elif step < 18000:  '3h'     # Added during implementation for Jupiter GA
   else:               '6h'

4. TIME WINDOW (context):
   cube_diameter_km = cube_half_width_km * 2
   crossing_time_sec = cube_diameter_km / v_kms
   window_sec = crossing_time_sec * 1.5   # margin for approach/departure
   window_sec = max(window_sec, 600)      # minimum 10 minutes
   start = encounter_epoch - window/2
   end = encounter_epoch + window/2
```

**Key insight: two different length scales.** The cube is sized to *frame* the encounter
(4x flyby distance). But the *resolution* is driven by the curvature -- the arc length
through the closest approach region (~pi * dist_km). For distant gravity assists like
Jupiter, the cube is large but the curve is tight. Using cube diameter for resolution
would give 6h steps; using curvature gives 3h steps -- the difference between a chord
and an arc.

### Verified Results for New Horizons Encounters

| Encounter | dist_km | Scale (AU) | Step | Window | Verified |
|-----------|---------|-----------|------|--------|----------|
| Arrokoth | 3,538 | 0.0000946 | 1m | 49 min | PASS -- encounter marker on trajectory curve |
| Pluto | 12,472 | 0.000334 | 1m | 3.0 hrs | PASS -- smooth approach/departure visible |
| Jupiter GA | 2,305,000 | 0.0616 | 3h | 15.1 days | PASS -- curved arc visible at perijove |
| Full Mission | -- | Auto | 6h | 2006-2020 | PASS -- overview unchanged |

### Post-Plot Interval Restore: SOLVED

Full Mission preset explicitly carries `fetch_step: '6h'`. Clicking it after any
fine-grained encounter view restores the default trajectory interval. No separate
restore mechanism needed. Each preset is self-contained.

### 3h Tier Addition

The original snap table jumped from 2h (threshold 10,800 sec) to 6h. Jupiter GA's ideal
step of 11,373 sec fell just above the 2h threshold and snapped to 6h, giving ~60 points
over 15 days. Adding a 3h tier (threshold 18,000 sec) gives Jupiter ~120 points -- better
arc resolution at perijove. The 3h step is a valid Horizons interval.

---

## Arrokoth Close-Approach Resolution (March 13, 2026)

### The Discovery

**Arrokoth CAN be a Horizons center.** The `center_id: 2486958` field in
`celestial_objects.py` already solves this. The object `id` is `'2014 MU69'`
(designation, can't be a center), but `center_id` is `'2486958'` (numeric, the SWRI
mission trajectory solution NavSBE_2014MU69_od159). When the orrery sets Arrokoth as
center body, line ~3236 of `palomas_orrery.py` picks up the `center_id` and passes
`500@2486958` to Horizons. This works -- Horizons returns NH's position relative to
Arrokoth using the New Horizons navigation team's own reconstructed trajectory.

**Verified by Tony:** Manual plotting with Arrokoth as center body, scale 0.00003 AU,
produces correct encounter geometry showing NH ~23 micro-AU (~3,500 km) from Arrokoth
at the flyby epoch.

### What Horizons Provides for Arrokoth

| Data type | Available? | Resolution | Notes |
|-----------|-----------|------------|-------|
| Vector table (position/velocity) | Yes | Down to 1 minute | KM-S units, ecliptic J2000 |
| Osculating elements | **No** | N/A | Not available for mission s/c solutions |
| Trajectory coverage | 1993-Dec-25 to 2034-Jan-08 | - | NavSBE_2014MU69_od159 from SWRI |

**Key finding from Horizons header:** The authoritative flyby time is 05:34:31 TDB
(05:33:22 UTC), distance 3,537.7 km. Our tagged epoch updated from 05:33:00 to 05:33:22.

---

## Non-Osculating Encounter Pattern (General Solution)

For encounters where the target body:
- Has a `center_id` in `celestial_objects.py` (can be a Horizons center)
- But Horizons provides vectors only, no osculating elements
- So no Keplerian orbit arc refinement between plotted trajectory points

**The pattern:**
1. Set `center_closeup` to the target body name (the `center_id` mechanism handles
   the Horizons query)
2. Adaptive resolution derives scale and step from encounter geometry
3. Add a `resolution_note` to the encounter dict explaining the trajectory sampling
   limitation -- this appears in the hover text for transparency
4. The encounter marker itself is precise (fetched at the authoritative epoch from
   Horizons vectors at 1-minute resolution)

**Bodies this applies to:** Arrokoth (2486958), and potentially other mission targets
with SWRI/JPL reconstructed trajectories but no osculating element solutions.

---

## What Already Exists (reusable)

| Component | Status | Reuse |
|-----------|--------|-------|
| `spacecraft_encounters.py` | Working (all stages) | Data + markers + presets + adaptive resolution |
| `SPACECRAFT_ENCOUNTERS` dict | NH complete (3 encounters) | Expand to other missions |
| `SPACECRAFT_FULL_MISSION` dict | NH complete | Expand to other missions |
| `_calculate_encounter_resolution()` | Working | Auto-derives presets for any encounter with `v_kms` |
| `_add_spacecraft_encounter_markers()` in palomas_orrery.py | Working delegator | Both pipelines wired |
| `create_mission_checkbutton()` + Go buttons | Working (3-col grid) | Auto-generates for any spacecraft with encounters |
| `_apply_mission_preset()` | Working (adaptive) | Generic -- works for any spacecraft/encounter |
| `APSIDAL_TERMINOLOGY` small body terms | Integrated | Bennu, Ryugu, Arrokoth, etc. |
| `mission_info` in hover text | Working | Closest Plotted Point shows it |
| Fly-to buttons | Working | Pattern for view configuration |

## What Was Retired

| Component | Reason |
|-----------|--------|
| `_add_spacecraft_encounter_markers()` pairwise version (~150 lines) | Replaced by tagged delegator |
| `compute_pairwise_encounter()` (never integrated) | Abandoned approach |
| `add_encounter_marker()` pairwise version (never integrated) | Abandoned approach |
| `ENCOUNTER_THRESHOLD_AU` (never integrated) | No longer needed |
| `spacecraft_encounter_integration.md` | Retired design doc |
| "Arrokoth can't be a Horizons center" assumption | **Corrected** -- center_id 2486958 works |
| Manual `plot_days_closeup` / `plot_scale_au_closeup` as primary values | **Superseded** by adaptive resolution (kept as fallback) |
| "Buttons are additive -- never uncheck" principle | **Replaced** -- each preset is a fresh view |
| "Each preset is a fresh view" uncheck-all | **Replaced** -- additive presets preserve user selections (March 15) |
| `diamond-open` encounter marker symbol | **Replaced** -- `square-open` for consistent visual language (March 15) |
| `hoverinfo='skip'` on non-Sun center bodies | **Replaced** -- full hover from INFO encyclopedia (March 15) |
| Horizontal button layout (`pack(side='left')`) | **Replaced** -- 3-column grid prevents truncation |

---

## Steps 1 and 2 (from original session) -- COMPLETED

**Step 1: mission_info in hover text** -- Working. The Plotted Period "Closest Plotted
Point" for New Horizons now shows the italic mission_info text in hover.

**Step 2: Small body apsidal terms** -- Integrated. Bennu, Ryugu, Arrokoth, Patroclus,
Apophis, Dinkinesh added to APSIDAL_TERMINOLOGY dict.

---

## Session March 15, 2026: Position Marker, Center Hover, Additive Presets

### Issues Identified (from NH Jupiter GA visualization)

1. **NH position marker outside encounter cube.** The "current position" marker
   plots at the GUI start date (window start), not the encounter epoch. At 0.06 AU
   cube scale, the window-start position is outside the visible volume.

2. **Center body (Jupiter) has no hover text.** Sun gets full hover via
   `hover_text_sun` and `hovertemplate`. Non-Sun center bodies get `hoverinfo='skip'`.

3. **Encounter marker overlaps object marker.** Both used `diamond-open` symbol,
   making them indistinguishable at encounter scale.

4. **Go button wipes user selections.** Satellites (Io, Europa, etc.) are unchecked
   by the preset's "fresh view" uncheck-all. Shells survive because they use separate
   variables, but object checkboxes don't.

### Fixes Implemented

**Edit 1-4: Encounter position marker override (`_encounter_plot_date`)**

- Module-level `_encounter_plot_date = [None]` (list wrapper for mutability)
- `get_encounter_preset()` now returns `'encounter_date'` (authoritative epoch string)
- `_apply_mission_preset()` stores encounter epoch in `_encounter_plot_date[0]`
- `plot_objects()` overrides `date_obj` from `_encounter_plot_date` when set, then
  clears it (one-shot). Position markers land at closest approach, not window edge.
- Trajectory window stays centered (approach + departure preserved).

**Edit 5: Center body hover text from INFO encyclopedia**

- Non-Sun center bodies now get `hovertemplate='%{text}<extra></extra>'` + `customdata`
  (same pattern as Sun)
- Hover text built from `INFO` dict: bold name + "(center body)" + first line summary
- Mercury's leading `***` scale advice stripped from hover
- `hoverinfo='skip'` removed

**Edit 6: Encounter marker symbol → `square-open`**

- Consistent visual language: open squares = positions/events, filled symbols = objects
- Matches CAD markers and apsidal markers

**Edit 7: Additive presets**

- Removed blanket uncheck-all from `_apply_mission_preset()`
- Only clears `_was_checked` for the previous center body (prevents shadow restore)
- Preset ensures its objects are checked; user's existing selections survive
- Both encounter and full mission presets are additive
- Users can add satellites, extra planets, then press Go without losing them

### Design Decision: Separating Position Marker from Fetch Window

The GUI start date serves double duty: it drives the trajectory fetch window AND
the position marker date. For encounter presets, the fetch window must start before
the encounter (to show the approach), but the marker should be at the encounter epoch.

Rather than restructuring the GUI, a module-level `_encounter_plot_date` override
decouples them cleanly. One-shot usage (cleared after `plot_objects`) means only
encounter-triggered plots are affected. Manual plots continue using the GUI date.

---

## Missions to Expand (next)

All spacecraft currently in the orrery's objects list:

| Spacecraft | # Encounters | Key Events |
|------------|-------------|------------|
| New Horizons | 3 | Jupiter GA, Pluto, Arrokoth -- **DONE** |
| Voyager 1 | 2 | Jupiter, Saturn |
| Voyager 2 | 4 | Jupiter, Saturn, Uranus, Neptune (Grand Tour!) |
| Cassini | 5+ | Venus x2, Jupiter, Saturn insertion, Grand Finale |
| Juno | 2+ | Earth GA, Jupiter insertion |
| OSIRIS-REx | 4 | Earth GA, Bennu arrival, TAG, sample return |
| OSIRIS-APEX | 1 | Apophis 2029 [PLANNED] |
| Lucy | 7 | Dinkinesh, Donaldjohanson, 4 Trojans, Patroclus |
| Rosetta | 4+ | Mars, Lutetia, 67P orbit, Philae landing |
| BepiColombo | 5+ | Earth, Venus x2, Mercury flybys, orbit insertion |
| Akatsuki | 2 | Venus orbit insertion (failed 2010, success 2015) |
| Parker Solar Probe | 1+ | Venus GAs, closest solar approaches |
| SOHO | 1 | L1 halo orbit |
| Europa Clipper | 1+ | Mars GA, Europa flybys [PLANNED] |

**Suggested next:** Voyager 2 (Grand Tour, 4 encounters) -- natural second test case.
Different character than NH: multiple gravity assists, the 176-year alignment story.

---

## Side Fix: Encyclopedia "i" Button in Gallery (March 13, 2026)

During this session, a gallery bug was also identified and fixed. The encyclopedia
"i" info button worked in Studio preview and standalone export but disappeared in
the web gallery.

**Root cause:** Classic parallel pipeline bug. `build_gallery_html()` strips all
underscore-prefixed layout keys, then adds back specific exemptions (`_studio`,
`_kmz_handoff`, `_hover_mode`, etc.). `_encyclopedia` was missing from the exemption
list. The preview path (`_preview_as_gallery()`) already had the exemption, which is
why the preview worked but the export didn't.

**Fix (2 files):**
- `gallery_studio.py`: Added `_encyclopedia` to `layout_for_json` preservation list
  in `build_gallery_html()` (one-liner, same pattern as other preserved keys)
- `index.html`: Added encyclopedia CSS, HTML elements, JS state/functions, and
  plotly_click/plotly_hover event wiring. "i" button positioned below Share button
  (desktop: `fixed; top: 92px; left: 62px`; mobile: flows into toolbar flexbox).
  Encyclopedia overlay uses `position: fixed` for full-viewport coverage.

**Lesson:** When adding new underscore-prefixed layout keys that need to survive into
the gallery, add preservation lines in BOTH `build_gallery_html()` AND
`_preview_as_gallery()`. The preview path had it; the export path didn't. Check both.

---

## Future Directions (Beyond Stage A+B)

**New missions to add:** Europa Clipper (49 Europa flybys!), JUICE (ESA Jupiter),
Dragonfly (Titan rotorcraft, 2030s), MMX (Mars moons).

**Historical missions:** Apollo 8 lunar orbit (Dec 24, 1968), Apollo 11 landing
(Jul 20, 1969), Apollo 13 free-return (Apr 1970). May require analytical trajectories
where Horizons data is unavailable.

**"Boring" gravity assists are fascinating:** Europa Clipper flies to Mars and comes
BACK to Earth just to fly out again. Every gravity assist tells a story about why
orbital mechanics requires patience and cleverness.

---

## Quotables

*"We already know when every encounter happened. The computation was solving a problem
that doesn't exist."* -- The tagged data insight

*"A checkbox adds a thing. A button takes you somewhere."* -- On the Go button design

*"Seeing the encounter list IS the education. The student doesn't need to click
anything to learn that Voyager 2 visited four planets."* -- On permanent sub-items

*"Three authoritative sources, one visual language."* -- CAD / Tp / Tagged dict unification

*"The GUI is the curriculum."* -- On permanent encounter sub-items as education

*"Even 'boring' Earth gravity assists are fascinating. Europa Clipper flies to Mars
and comes BACK to Earth just to fly out again?"* -- Tony, on why every encounter matters

*"The button creates a preset that can be modified, not a fixed locked view."* -- Tony, on Go button behavior

*"Everything is interesting."* -- Tony, on gravity assists

*"43 -> 19 -> 23 -> 14.5 -> 13.9. The Sun is relentless and Jupiter is the one friend along the way."* -- The velocity arc

*"Velocities add as vectors, not scalars."* -- On why 16 + 30 != 46

*"Arrokoth CAN be a Horizons center."* -- Correcting the assumption, March 13, 2026

*"We're not calculating the distance ourselves. Horizons is doing it."* -- On the center_id data flow

*"The velocity change IS the encounter."* -- On why constant velocity assumption fails for gravity assists

*"Denser dots visually communicate 'this is where the action happened.'"* -- On oversampling at peak velocity as a feature

*"The cube frames the encounter. The curvature drives the resolution."* -- The two-length-scale insight, March 14, 2026

*"Is this what they call 'software engineering' as distinct from 'coding'?"* -- Tony, after the zero-code design session

*"The approach trajectory is half the story."* -- On why the position marker fix needs to preserve the full window

*"Open squares for positions, filled symbols for objects."* -- The marker visual language

---

## Key Lessons

- **Reference frames matter in hover text.** The user sees heliocentric velocities in the plot. Notes must use the same frame or explicitly label both.
- **Vector velocity addition.** 16.26 km/s Earth-relative + ~30 km/s Earth orbital velocity = ~43 km/s heliocentric (not 46 -- vectors, not scalars).
- **Plotly hover wrapping.** `<br>` inside `<i>` tags may not render as line breaks in all Plotly versions. Fix: close and reopen `<i>` around each `<br>` (`</i><br><i>`).
- **Python module caching.** Editing a module file doesn't take effect until the importing process restarts. Restart the orrery after updating `spacecraft_encounters.py`.
- **Full mission context is valuable.** Encounter markers appearing on the full mission trace (even outside the plotted period) provide useful context rather than clutter.
- **Closure capture in loops.** `def make_enc_cmd(sc=name, ei=idx)` pattern required to capture loop variables correctly in Tkinter button callbacks. Without default args, all buttons would fire the last loop iteration's values.
- **Arrokoth CAN be a Horizons center via center_id 2486958.** The `center_id` pattern in `celestial_objects.py` solves small body centering. SWRI mission trajectory solution (NavSBE_2014MU69_od159) provides vectors down to 1-minute resolution. Osculating elements are NOT available.
- **Symmetric axis ranges are the constraint.** Manual scale N creates `[-N, N]` centered on the center body (origin). Target-centering via `center_id` solves this by putting the encounter at origin.
- **Parallel pipeline bugs.** Preview path and export path can diverge silently. Always check both paths when adding underscore-key exemptions.
- **Two length scales for encounter resolution.** Cube scale (dist_km x 4) frames the view. Curvature scale (pi x dist_km / v_kms) drives the fetch step. Using cube diameter for resolution gives too-coarse steps for distant encounters.
- **3h Horizons step tier.** Jupiter GA ideal step (11,373 sec) falls between 2h and 6h thresholds. Without a 3h tier, it snaps to 6h. The snap table needs granularity in the 3-5 hour range.
- **Horizons step format.** Accepts `{number}{unit}`: `1m`, `5m`, `10m`, `30m`, `1h`, `2h`, `3h`, `6h`, `1d`. API-only, not web interface.
- **Orbital vs trajectory fetch pipelines.** `orbital_points_entry` routes to orbital objects; `trajectory_interval_entry` routes to trajectory objects. No conflict.
- **Peak velocity for resolution, not average.** Using `v_kms` ensures the fastest part of the trajectory is smooth. Slower approach/departure are oversampled, which is visually informative.
- **Design before implementation.** The adaptive resolution design took one full session of conversation to resolve. Building first would have locked in the wrong formula.
- **Shadow/restore mechanism on center change.** `on_center_change()` restores the previous center's checkbox via `_was_checked` flag. Preset uncheck-all must clear this flag to prevent carryover. The fix: `obj['_was_checked'] = False` in the uncheck loop.
- **Each preset is a fresh view.** The "never unchecks" additive principle was wrong for encounter presets. Users see each Go button as a new plot. Unchecking everything first eliminates irrelevant objects, reduces fetch time, and cleans the legend.
- **Additive presets win.** The "fresh view" uncheck-all was itself wrong. Users want to add satellites, extra planets, then press Go. The preset should *ensure* its objects are checked, not *replace* everything. Shells already survived (separate variables); making object checkboxes survive too is consistent.
- **Position marker date != fetch window start.** The GUI start date drives both the trajectory fetch window and the position marker. For encounters, the marker should be at the encounter epoch but the trajectory needs the full approach window. Module-level one-shot override (`_encounter_plot_date`) decouples them without restructuring the GUI.
- **Center bodies deserve hover text.** Sun had full encyclopedia hover; non-Sun centers had `hoverinfo='skip'`. The INFO dict already has encyclopedia text for every planet -- reuse it.
- **Open squares = positions/events in space.** Consistent marker visual language across CAD markers, apsidal markers, and encounter markers. Filled symbols = objects. Prevents confusion when markers overlap at encounter scale.
- **Button layout for variable spacecraft.** Horizontal `pack(side='left')` truncates when buttons exceed pane width. Grid layout with column wrapping (3 columns) handles any number of encounters compactly.

---

**Prepared by:** Tony (with Claude)
**Sessions:** March 11-15, 2026
**Next:** Expand to Voyager 2 (Grand Tour). Then Voyager 1, Cassini, Juno. The adaptive resolution formula scales to all encounters -- just add `dist_km` and `v_kms` to the encounter dict.
