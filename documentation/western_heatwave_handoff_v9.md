# Paloma's Orrery -- Western Heatwave Timeline Handoff v9 (Final)

## Session Handoff | March 22 - April 3, 2026 | Claude Opus 4.6

-----

## Context

A 1-in-500-year heat event unfolded across North America (March
14-30, 2026). World Weather Attribution classified it as "virtually
impossible" without human-induced climate change. Yale Climate
Connections called it "one of the six most astonishing weather
events of the century." March 2026 was confirmed as the warmest
March on record for the United States, beating 2012 by half a
degree Fahrenheit. It was also the warmest November-through-March
period in recorded US history.

The event had a two-pulse structure driven by an omega block -- the
strongest mid-tropospheric ridge ever observed in the southwestern
US in March (500mb heights at 3.5-4 standard deviations above
normal). Pulse 1 (March 14-22) crested with 14 states breaking
all-time March records. Pulse 2 (March 24-27) crested harder in
the southern corridor: Oklahoma 106F, Texas 108F, Kansas 104F
(breaking its own 5-day-old record). The dome's final eastward
reach touched Chicago (81F daily record, March 30) before a cold
front ended the event.

Final tally: 17 states with all-time March records broken, 1,500+
station records, 37 confirmed record-breaking stations tracked.

The scenario module tells the complete story as a 9-snapshot
timeline, all on ERA5 reanalysis data:

| Date     | Label           | CSI | Stations | Grid    | Data Source |
|----------|-----------------|-----|----------|---------|-------------|
| March 14 | The Spark       | 2   | 3        | 1,075   | ERA5        |
| March 17 | The Pivot       | 3   | 6        | 1,075   | ERA5        |
| March 18 | Records Fall    | 4   | 9        | 1,075   | ERA5        |
| March 20 | The Peak        | 5   | 12       | 1,075   | ERA5        |
| March 21 | Eastward Surge  | 5   | 23       | 3,825   | ERA5        |
| March 22 | The Crest       | 5   | 27       | 24,341  | ERA5        |
| March 25 | Round Two       | 5   | 31       | 24,341  | ERA5        |
| March 26 | Pulse 2 Crests  | 5   | 36       | 24,341  | ERA5        |
| March 30 | The Reach       | 4   | 37       | 24,341  | ERA5        |

CSI = Climate Shift Index (1-5 scale, how much more likely due to
climate change).

Grid progression: 1,075 pts (Southwest, Mar 14-20) -> 3,825 pts
(Plains, Mar 21) -> 24,341 pts (continental, Mar 22-30).

All 9 snapshots are on ERA5 reanalysis. No synthetic data remains.

-----

## What Was Accomplished (Sessions 1-2, March 22-23)

### Scenario Module (Complete, Tested, Deployed)

**`scenarios_western_heatwave_march_2026.py`** (~700+ lines):

- `SNAPSHOT_CONFIGS` -- date-parameterized configuration driving anomaly
  magnitude, spatial extent, station activation, and CSI level
- `RECORD_STATIONS` -- 15 confirmed observation stations with `first_date`
  gating (stations accumulate as the event progresses)
- `fetch_western_heatwave()` -- shared fetch function: tries ERA5 CSV
  cache first, falls back to realistic synthetic grid
- `_build_synthetic_field()` -- Gaussian baseline + RBF station spikes +
  smoothing + re-pinning for exact station values
- `_build_briefing()` -- HTML briefing for annotation/intel card
- `_build_encyclopedia()` -- rich "i" card content organized by
  planetary boundaries (see Session 3 below)
- `_make_scenario()` -- factory builds scenario dict with `pin_stations`,
  `briefing`, and `encyclopedia` all filtered/built by date
- `SCENARIOS` -- list of 5 scenario dicts, ready for engine
- `generate_all()` -- batch runs all 5 through the pipeline
- `validate_snapshots()` -- tests data layer without engine dependency
- CLI: `--validate` (data only) or `--generate-all` (full pipeline)

### Engine Integration (Complete)

Added import to `earth_system_generator.py` `MissionSelector`:

```python
from scenarios_western_heatwave_march_2026 import SCENARIOS as WESTERN_SCENARIOS
self.all_scenarios.extend(WESTERN_SCENARIOS)
```

All 5 snapshots appear in GUI as `[HEAT] Western Heat Dome Mar XX - Label`.

### Engine Edits (All Applied and Verified)

Eight engine edits to `earth_system_generator.py`, all deployed:

1. **HTML tag stripping** in `create_intel_card()` (Issue 1)
2. **clampToGround** pin altitude in `build_spikes_kml()` (Issue 2)
3. **Continuous legend colorbar** in `create_legend_card()` (Issue 3)
4. **`pin_stations` parameter** on `build_spikes_kml()` signature (Issue 4)
5. **`pin_stations` early-return block** in `build_spikes_kml()` (Issue 4)
6. **`pin_stations` passthrough** in `run_scenario()` call (Issue 4)
7. **Pin labels to absolute temperature** in `build_spikes_kml()` (Issue 6)
8. **Intel card line breaks** in `create_intel_card()` (Issue 7)

### Full Pipeline Verified

- Phase 1: Data validation (`--validate`) -- all 5 snapshots pass
- Phase 2: Single snapshot through engine -- March 20 "The Peak" verified
- Phase 3: Visual progression -- March 14 vs March 20 side-by-side confirmed
- Phase 4: Full batch -- all 5 KMZs + teasers generated
- Phase 5: Gallery integration -- teaser through json_converter, gallery
  viewer, and Google Earth 3D button all verified
- Station pins verified in GE: accumulating records across all 5 snapshots,
  smaller pin icons (scale 0.6), clamped to ground, with anomaly + note

-----

## What Was Accomplished (Session 3, March 23)

### Gen-Mobile Preset (Complete, Deployed)

**`gallery_studio.py`** -- three edits:

1. `GEN_MOBILE_CONFIG` dict: green background (#2d6a2d), no title,
   annotations on with mobile briefing, no legend, tight margins
   (20 all around), colorbar on, modebar on, landscape output,
   encyclopedia embedded
2. "Gen-Mobile" button in preset row
3. `_apply_gen_mobile_preset()` method with save/restore of KMZ link
   and custom title (same pattern as `_apply_generator_preset()`)

### Mobile Briefing Pipeline (Complete, Deployed)

**Design (Option C -- engine auto-generates, scenario can override):**

The engine auto-generates a shortened mobile briefing from the full
briefing by keeping title + first narrative paragraph and dropping
attribution, station records, and source lines. Any scenario module
can override by providing a `mobile_briefing` key in its scenario dict.
The Western heatwave scenarios use the auto-generated version (title +
detail is sufficient).

**Implementation across two files:**

`earth_system_generator.py`:

- `_build_auto_mobile_briefing()` helper: normalizes `<br><br>` and
  `\n\n` as paragraph breaks, keeps first two paragraphs (title +
  narrative), drops the rest. Returns briefing unchanged if already
  <= 2 paragraphs.
- `generate_plotly_teaser()` gains `mobile_briefing=""` parameter.
  Embeds `_mobile_briefing` in layout dict using scenario's custom
  version if provided, else auto-generated from full briefing.
- `run_scenario()` passes `mobile_briefing` through to teaser generator.

`gallery_studio.py`:

- `use_mobile_briefing` config key added to all four preset configs
  (DEFAULT, CLEAN, GENERATOR: False; GEN_MOBILE: True)
- GEN_MOBILE_CONFIG changed: `show_annotations: True` (was False),
  `use_mobile_briefing: True` (new)
- Annotation processing block: when `use_mobile_briefing` is checked,
  strips leading `<b>title</b>` line (gallery viewer has its own
  title bar) and swaps annotation text from `_mobile_briefing`.
  Targets bottom-left annotation (y <= 0.05 in paper coordinates).
- "Use mobile briefing" checkbox in Annotations section with tooltip
- `_get_config_from_gui` and `_apply_config_to_gui` updated
- `_mobile_briefing` preserved in all three layout export paths
  (landscape, portrait, preview) alongside `_kmz_handoff`,
  `_encyclopedia`, etc.

### Info Card WYSIWYG Fix (Complete, Deployed)

**Problem:** In portrait mode, tapping a map point triggered both
Plotly hovertext AND the gallery viewer's info card. The info card
was redundant (showed "Object" + the same anomaly value). The gallery
viewer was pre-empting Studio's decision -- it wired the click handler
unconditionally for all portrait plots, regardless of whether Studio
had enabled `route_hover_to_panel`.

**Root cause:** Two independent info card systems existed:
- Studio's `route_hover_to_panel` controls standalone HTML exports
- Gallery viewer's `index.html` had its own portrait click handler
  that fired unconditionally, ignoring Studio's routing decision

**Principle applied:** The gallery viewer should not pre-empt or
supersede Studio. Where decisions can be made by Studio, the viewer
should be silent or neutral.

**Fix:** `index.html` portrait click handler now checks for
`_hover_mode` in the layout before wiring the info card:

```javascript
// BEFORE:
if (currentMode === 'portrait') {
    plotlyGraph.on('plotly_click', function(data) {

// AFTER:
if (currentMode === 'portrait' && figDict.layout && figDict.layout._hover_mode) {
    plotlyGraph.on('plotly_click', function(data) {
```

If Studio didn't set `route_hover_to_panel` (which embeds `_hover_mode`
in the layout), the viewer stays silent. No new layout flags needed --
uses the existing `_hover_mode` contract.

### Encyclopedia "i" Card Pipeline (Complete, Delivered)

**Concept:** The trimmed mobile briefing loses context. The encyclopedia
"i" card recovers it -- and goes deeper. Each snapshot gets a rich,
scrollable card connecting the heat event to planetary boundary science.
The gallery shows what happened; the "i" card explains why it matters.

**Content structure (five sections per snapshot):**

1. **What Happened** -- the meteorological event, specific to that date
2. **Climate Attribution** -- CSI level, WWA findings, what the numbers
   mean scientifically
3. **Earth System Context** -- connections to planetary boundaries,
   organized by boundary group. Each snapshot emphasizes different
   boundaries as the event escalates:
   - March 14: Climate change + freshwater (snowpack timing)
   - March 17: + biosphere integrity (false-spring crop risk)
   - March 18: + land system change (fire preconditioning, urban heat)
   - March 20: All boundaries active + novel entities (energy feedback)
   - March 21: Eastward cascade -- wheat belt, expanded fire risk
4. **Record-Breaking Stations** -- accumulated to date, matching pins
5. **Data & Sources** -- provenance, attribution references, planetary
   boundaries framework citations

**Implementation across four files:**

`scenarios_western_heatwave_march_2026.py`:

- `_build_encyclopedia(date_str, config)` function: builds station list
  from `RECORD_STATIONS` with `first_date` gating (same as pins),
  assembles header + narrative body + stations + sources. Five date-
  specific entries with escalating Earth System Context sections.
- `encyclopedia` key added to scenario dict via `_make_scenario()`
- Entry sizes: 2.0K (Mar 14) -> 3.7K (Mar 21) chars, growing with
  the event

`earth_system_generator.py`:

- `generate_plotly_teaser()` gains `encyclopedia=""` parameter
- Scattermapbox trace gains `name=title` (required for encyclopedia
  hover/click lookup by trace name)
- Embeds as `_encyclopedia` dict keyed to trace name in layout
- `run_scenario()` passes `encyclopedia` through

`gallery_studio.py`:

- `GEN_MOBILE_CONFIG`: `embed_encyclopedia: True` (was False)
- Studio's existing `embed_encyclopedia` checkbox and `_encyclopedia`
  preserve paths handle the rest -- no other Studio changes needed

`index.html`:

- `encBody.textContent` changed to `encBody.innerHTML` -- enables
  HTML-formatted encyclopedia entries (bold headers, line breaks,
  italic boundary labels). Backward compatible: plain text orrery
  entries render identically through innerHTML.
- Single-entry auto-show: when `_encyclopedia` has exactly one key,
  the "i" button appears immediately without requiring hover/tap
  first. Multi-trace orrery plots still show on hover per-trace.
  Earth system teasers (single trace) show "i" on load.

-----

## What Was Accomplished (Session 4, March 24)

### ERA5 CDS API Integration (Complete, Tested, Deployed)

**Problem:** The scenario module had a TODO placeholder for ERA5 API
fetch. The original assumption was that ERA5 data wouldn't be
available until ~April 1-5. Research revealed that ERA5T (near-real-
time) data is available with only a ~5 day lag. As of March 24,
data through March 19 06:00 UTC was available.

**Design: Three-tier fetch strategy built into `_try_era5_fetch()`:**

1. **Tier 1: CSV cache** -- `era5_western_2026-03-XX.csv` in `data/`.
   Instant load. Created automatically by Tier 2 on first success.
2. **Tier 2: CDS API fetch** -- downloads from Copernicus Climate
   Data Store, computes anomaly, caches as CSV. Requires `cdsapi` +
   `netCDF4` packages and a `.cdsapirc` key file.
3. **Tier 3: Synthetic fallback** -- Gaussian baseline + RBF station
   spikes. Always works, no dependencies. Unchanged from v6.

**Anomaly computation (Option 1 -- fetch both, self-contained):**

- Fetches hourly 2m temperature for the event day (all 24 hours)
- Fetches hourly 2m temperature for the same day-of-month across
  1991-2020 (30 years x 24 hours) as climatology baseline
- Computes daily max for event day and climatology independently
- Anomaly = (event daily max - climatology daily max mean) * 9/5
  (Kelvin difference converted to Fahrenheit)
- Clips negative anomalies to 0

**Caching architecture:**

- Event data: `data/era5_raw_2026-03-XX.nc` (NetCDF, raw download)
- Climatology: `data/era5_clim_march_dayXX.nc` (one per day-of-month,
  reusable across years -- one-time download)
- Anomaly CSV: `data/era5_western_2026-03-XX.csv` (final product,
  loaded by Tier 1 on subsequent runs)

**Graceful degradation:**

- `cdsapi` or `netCDF4` not installed: prints install instructions,
  falls through to synthetic
- `.cdsapirc` missing or invalid: prints setup URL, falls through
- CDS API returns 403 (license not accepted): prints license URL,
  falls through
- CDS API returns 400 (data not yet available): falls through
- Network failure: falls through
- Any exception during anomaly computation: prints traceback,
  falls through

**Implementation: four new functions in scenario module:**

- `_load_era5_csv_cache()` -- Tier 1 CSV reader (refactored from
  original `_try_era5_fetch`)
- `_save_era5_csv_cache()` -- writes anomaly CSV after successful
  CDS fetch
- `_fetch_era5_from_cds()` -- Tier 2: CDS API calls, anomaly
  computation, CSV caching
- `_try_era5_fetch()` -- three-tier orchestrator (replaces TODO)

**Dependencies (Tony's machine only -- not required for synthetic):**

- `pip install cdsapi netCDF4` (installed and verified)
- CDS account (free): https://cds.climate.copernicus.eu/
- API key in `~/.cdsapirc` (created at `C:\Users\tonyq\.cdsapirc`)
- ERA5 license accepted on CDS dataset page

### Full Pipeline Verified with ERA5

- Single snapshot test: March 14 "The Spark" -- ERA5 fetched from
  CDS, climatology downloaded (one-time), anomaly computed, CSV
  cached, pipeline completed with real reanalysis data
- Full batch test (`generate_all()`): March 14, 17, 18 loaded from
  ERA5; March 20, 21 fell back to synthetic (data not yet available,
  latest available was March 19 06:00 UTC). All 5 completed
  successfully.
- Subsequent run for March 14: loaded from CSV cache (instant),
  no CDS API call needed

### Text Updates

- Module docstring: updated data source description to reflect
  ERA5T 5-day lag (was "~April 1-5")
- Briefing footer: "ERA5 reanalysis (if available) or preliminary
  synthetic" (was "Preliminary synthetic. ERA5 reanalysis ~April 2026")
- Encyclopedia Data & Sources: "ERA5 reanalysis via CDS API when
  available" (was "ERA5 reanalysis expected ~April 2026")

### Snapshot Expansion (Complete, Tested, Deployed)

**March 21 enriched** -- station data and grid expanded:

- Denver corrected: 86F (was 85F), new all-time March record
- Albuquerque corrected: 91F (was 88F), NM state March record
- 8 new Plains stations added for March 21: Burlington CO (96F),
  Phillipsburg KS (101F), Hitchcock IA (97F), Cambridge NE (99F),
  Vermilion SD (97F), Luverne MN (88F), Harrisonville MO (97F),
  Carlsbad NM (100F)
- Grid expanded: (25-50 lat, -125 to -88 lon) -- Mexico to Canada,
  Pacific to Mississippi Valley. Grid grows from 1,075 to 3,825 pts
  (synthetic) or ~15,000 pts (ERA5)
- March 21 ERA5 re-fetched with expanded grid (old cache deleted)
- Population centers list expanded: added Kansas City, Oklahoma City,
  Lubbock TX, St. Louis

**March 22 "The Crest" added** (Snapshot 6):

- 4 new stations: St. Louis MO (88F), Springfield MO (90F),
  Kansas City MO (92F), North Platte NE (92F)
- Full briefing, description, and encyclopedia entries
- Encyclopedia highlights: Chanute KS 78F swing in 4 days, Sierra
  Nevada snowmelt, spring phenology 20-30 days early, Arizona
  airshow 400+ heat illness cases
- Currently synthetic; ERA5 expected ~March 27

**March 25 "Round Two" added** (Snapshot 7):

- 4 new stations: Denver pulse 2 (87F -- breaks own record again),
  Lubbock TX (100F), Las Vegas pulse 2 (98F), Albuquerque pulse 2
  (94F)
- Full briefing, description, and encyclopedia entries
- Encyclopedia highlights: two-pulse ratchet structure, cities
  breaking their own freshly-set records within days, energy system
  feedback (peaking plants can't go offline between pulses)
- Currently synthetic; ERA5 expected ~March 30

**Validation results (all 7 snapshots):**

| Date | Label | Grid | Stations | Max Anomaly |
|------|-------|------|----------|-------------|
| Mar 14 | The Spark | 1,075 pts | 3 | 17.8F |
| Mar 17 | The Pivot | 1,075 pts | 6 | 23.1F |
| Mar 18 | Records Fall | 1,075 pts | 9 | 25.6F |
| Mar 20 | The Peak | 1,075 pts | 12 | 32.8F |
| Mar 21 | Eastward Surge | 3,825 pts | 23 | 46.0F |
| Mar 22 | The Crest | 3,825 pts | 27 | 46.0F |
| Mar 25 | Round Two | 3,825 pts | 31 | 46.0F |

### March 21 Deployed to Gallery

March 21 "Eastward Surge" with expanded ERA5 grid deployed to
palomasorrery.com and posted to Instagram (@palomas_orrery).
The ERA5 data shows the full continental-scale heat dome reaching
from Pacific coast through the Central Plains. Google Earth view
with station pins posted as part of the March 14-17-18-20-21
build-up series.

-----

## What Was Accomplished (Session 5, March 26-28)

### March 22 ERA5 Upgrade (Complete)

ERA5T data became available for March 22. Re-running the generator
automatically fetched ERA5 for March 22 with the expanded grid.
The ERA5 contour revealed the anomaly field extended well beyond
the original -88 longitude boundary -- 33-34F anomalies visible
in Appalachia. This triggered the grid expansion to continental
scale.

### Continental Grid Expansion (Complete)

**Problem:** ERA5 data showed the heat dome anomaly extending to
the Appalachians and beyond, but the grid was clipped at -88
(then -80) longitude.

**Solution:** Extended `grid_lon_range` to (-125.0, -65.0) for
March 22, 25, and 26 -- Pacific to Atlantic, full continental
coverage. Tony made the initial -65 edit manually after observing
the ERA5 data.

**Grid progression across the event:**
- March 14-20: (-125, -104) -- Southwest focus, 1,075 pts
- March 21: (-125, -88) -- Plains expansion, 3,825 pts
- March 22-26: (-125, -65) -- Continental, 6,171 pts

### March 26 "Pulse 2 Crests" Added (Snapshot 8)

**5 new stations confirmed from Yale Climate Connections day-by-day
tally (updated March 27):**

- Beaver OK: 106F (OK state March record, broke 104F from 1971)
- Rio Grande City TX: 108F (ties TX all-time March, 1954/1902)
- Ashland KS: 104F (KS state March record AGAIN, broke 101F from
  5 days earlier on Mar 21)
- Carlsbad NM: 103F (NM state March record for third time: 100F
  Mar 21 -> 102F Mar 22 -> 103F Mar 26)
- Morrisonville IL: 94F (ties IL state March record from 1929)

Total: 17 states with all-time March records, 36 stations across
8 snapshots.

### Encyclopedia Enrichment (Complete)

**March 26 encyclopedia entry includes three new sections beyond
the standard planetary boundaries format:**

1. **"The Meteorological Engine"** -- explains the omega block
   mechanism driving the event:
   - Jet stream buckles into omega shape; high-pressure ridge
     flanked by low-pressure troughs that lock it in place
   - 500mb geopotential heights at 3.5-4 standard deviations
     above normal -- strongest March ridge ever observed in SW US
   - Adiabatic compression: subsiding air heats as it descends,
     suppresses cloud formation, creates self-reinforcing feedback
   - Two-pulse structure is one persistent blocking pattern with
     internal oscillation, not two separate events
   - Eastward creep reflects ridge axis slowly migrating

2. **"Anomaly vs Records"** -- explains the question Tony raised:
   why does the ERA5 contour show 34F anomaly in Appalachia but
   no station pins east of St. Louis?
   - Anomaly = departure from local daily normal (continental)
   - Record = exceeding all-time March maximum (concentrated)
   - SE and Appalachia have high existing March ceilings from
     historical subtropical surges
   - Interior West/Plains have low March ceilings (normally cold)
   - Both readings are true: anomaly says "whole continent is
     abnormally hot"; pins say "these places exceeded anything
     ever measured"

3. **Refined climate attribution** -- blocking is natural
   atmospheric dynamics; climate change provides the elevated
   baseline (1.3C warmer floor). WWA: 4.7-7.2F added by
   anthropogenic warming. Both necessary; neither sufficient alone.

### Formal Data Attribution (Complete)

**Data & Sources block in `_build_encyclopedia()` upgraded with
Copernicus-required attribution language. Applies to all 8
snapshots automatically.**

Content (shared across all encyclopedia entries):
- "Modified Copernicus Climate Change Service (C3S) information
  [2026]" -- license-required phrase for processed ERA5 data
- Hersbach et al. (2020) citation
- ECMWF disclaimer
- NWS Preliminary Record Event Reports; NOAA NCEI
- WWA rapid analysis (March 20, 2026)
- Climate Central CSI
- Rockstrom et al. (2009), Richardson et al. (2023)
- "Visualization engine: Paloma's Orrery Earth System Generator"

Gemini (Mode 7) provided the attribution language and the
"modified" qualifier rationale.

-----

## What Was Accomplished (Session 6, April 3)

### March 30 "The Reach" Added (Final Snapshot 9)

**The capstone.** Chicago hit 81F at O'Hare on March 30, breaking
the March 30 daily record of 79F from 1986. The heat dome that
started in the Arizona desert on March 14 reached the Great Lakes
sixteen days later. A cold front and thunderstorms followed,
ending the event.

- 1 new station: Chicago IL (81F, +32F anomaly)
- CSI drops to 4 (dome weakening) -- narratively right
- Full capstone encyclopedia entry with "The Final Tally" and
  "Looking Forward" sections

**March 30 encyclopedia entry includes:**
- "The Final Tally" -- 17 states, 1,500+ records, warmest March
  on record (beating 2012 by ~0.5F), warmest Nov-Mar ever, "one
  of six most astonishing weather events of the century"
- Daniel Swain (Weather West) insight: event comparable to June
  2021 PNW heat dome by statistical anomaly metrics, but occurred
  3 months earlier when atmosphere has thermodynamic disadvantage
  (shorter days, weaker sun, snow cover present)
- "Looking Forward" section connecting to El Nino 2026-27,
  depleted snowpack as initial conditions for summer, 13,658
  wildfires / 1.4M acres burned before fire season began

### All 9 Snapshots Upgraded to ERA5 (Complete)

Re-ran `generate_all()` on April 3. ERA5T data was available for
all dates through March 30. Results:
- March 25: ERA5 loaded from cache (previously fetched)
- March 26: ERA5 fetched from CDS, 24,341 points
- March 30: ERA5 fetched from CDS, 24,341 points
- All 9 snapshots now on real reanalysis data
- No synthetic data remains in any snapshot

### Module Credit (Standing Requirement)

Module updated: April 3, 2026 with Anthropic's Claude 4.6

-----

## Issues Found and Fixed (All Sessions)

### Issue 1: Intel Card Showing Raw HTML Tags (Fixed)

**Problem:** `create_intel_card()` uses `matplotlib.plt.text()` which
renders text literally. The briefing contained HTML tags intended for
the Plotly teaser.

**Fix:** HTML tag stripping with `<br>` -> `\n\n` conversion for
visual separation, then `re.sub(r'<[^>]+>', '', ...)` for remaining
tags. Each line wrapped independently to preserve structure.

### Issue 2: KML Spikes Floating Above Surface (Fixed)

**Problem:** `newpoint()` with `relativeToGround` + height_multiplier
lifted pins to 500-2700km altitude.

**Fix:** Clamped to ground: `coords = [(lon, lat, 0)]`,
`altitudemode = clampToGround`.

### Issue 3: Contour/Legend Color Mismatch (Fixed)

**Problem:** Contour heatmap uses `inferno_r` colormap; legend card
used independent KML spike colors.

**Fix:** `'legend_style': 'continuous'` option renders matplotlib
colorbar matching the contour colormap. Backward compatible.

### Issue 4: Grid Stride Pin Placement (Fixed)

**Problem:** `spike_stride: 200` produced 8 pins on diagonal line.

**Fix:** `pin_stations` parameter on `build_spikes_kml()` with
early-return block. Stations placed by lat/lon from confirmed records.

### Issue 5: Pin Design Decisions (Resolved)

Plot ALL overlapping pins (accumulation is the story), smaller scale
(0.6), include note in briefing.

### Issue 6: Pin Labels to Absolute Temperature (Fixed)

**Problem:** Pin labels showed anomaly, redundant with contour map.

**Fix:** `label = f"{station['air_temp_f']:.0f}F"` -- pins show what
people experienced; contour shows the heat dome pattern.

### Issue 7: Intel Card Line Breaks (Fixed)

**Problem:** After HTML stripping, briefing was a wall of text.

**Fix:** Convert `<br>` to `\n\n` before stripping, wrap each line
independently. Structure preserved.

### Issue 8: Info Card Duplication in Portrait Mode (Fixed)

**Problem:** Gallery viewer wired portrait click handler
unconditionally, duplicating Plotly hovertext with a redundant info
card showing "Object" + anomaly value.

**Fix:** Guard portrait click handler on `_hover_mode` in layout.
Gallery viewer respects Studio's routing decision. WYSIWYG principle:
viewer should not pre-empt or supersede Studio.

### Issue 9: ERA5 License Not Accepted (Fixed, Session 4)

**Problem:** First CDS API call returned 403 Forbidden with
"required licences not accepted."

**Fix:** Accepted license at CDS dataset page. The error message
from `_fetch_era5_from_cds()` included the direct URL to the
license page. Subsequent fetch succeeded.

-----

## Files Delivered and Deployed

| File | Status | Notes |
|------|--------|-------|
| `scenarios_western_heatwave_march_2026.py` | Delivered (v5, final) | 9 snapshots, 37 stations, continental grid, all ERA5, formal attribution |
| `earth_system_generator.py` | Delivered | 8 engine edits + mobile briefing + encyclopedia pipeline |
| `gallery_studio.py` | Delivered | Gen-Mobile preset, mobile briefing, encyclopedia enabled |
| `index.html` | Delivered | WYSIWYG fix + innerHTML + single-entry auto-show |
| `western_heatwave_handoff_v1-v8.md` | Superseded | Replaced by this v9 (final) |

-----

## On the Horizon (Future Enhancements)

The Western Heatwave March 2026 scenario is complete. The following
are optional enhancements, not active work items.

- **Anomaly-vs-records clarification in earlier snapshots** --
  the March 26 and 30 encyclopedia entries explain this distinction.
  Consider adding a shorter version to March 22 "The Crest" where
  the continental ERA5 data first reveals the eastward extent.
- **Snowpack visualization** -- Colorado snowpack at historic lows
  (25% of normal in south, 50% in north), Denver Stage 1 drought
  restrictions declared. A separate freshwater/cryosphere boundary
  visualization would complement the temperature anomaly story.
- **Encyclopedia for existing scenarios** -- the `_build_encyclopedia`
  pattern can be adapted for `scenarios_heatwaves.py` and
  `scenarios_coral_bleaching.py`.
- **Unified KMZ timeline** -- single KMZ with dated folders. Would
  wrap all 9 snapshots in a single file with toggleable folders in
  GE sidebar.
- **CDS API key rotation** -- Tony's API key was briefly exposed in
  chat. Recommend regenerating on CDS profile page.
- **ERA5 cache invalidation automation** -- when expanding grid
  extents, old cached files must be deleted before re-run. Pattern
  is documented but could be automated (detect grid mismatch
  between config and cached CSV extent).
- **NOAA April 8 official summary** -- NOAA releases monthly US
  climate summary on April 8. May contain official confirmation
  of warmest March on record and additional statistics worth
  adding to the March 30 encyclopedia entry.

-----

## Key Lessons

- **`newpoint()` creates placemark pins, not extruded polygons.**
  The `polystyle` properties on a point are ignored by GE. For actual
  3D extrusions, use `newpolygon()` with a footprint.
- **Two color systems must agree.** Contour colormap (matplotlib) and
  legend bands (KML spike colors) were independent. The continuous
  colorbar legend resolves this by matching the contour exactly.
- **`spike_stride` is grid-density-dependent.** A stride tuned for a
  dense ocean grid (coral, stride 200) produces nearly empty results on
  a coarser land grid (1683 points). Station pins are the right approach
  for scenarios with confirmed observations.
- **HTML briefing text goes to two consumers.** Plotly teaser renders
  HTML; matplotlib intel card renders plain text. Strip tags at the
  engine (protects all modules) rather than maintaining dual text per
  scenario. Preserve `<br>` as double newlines before stripping other
  tags for visual separation.
- **Developing scenarios are structurally different.** Historical
  scenarios are static; this one accumulates data over time. The
  `first_date` gating on stations and the parameterized snapshot configs
  handle this cleanly -- each snapshot is a frozen moment, but the
  SCENARIOS list grows as the event progresses.
- **Overlapping pins tell the story.** Phoenix breaking its own record
  three times in a week is more powerful than showing just the final
  number. The accumulation is the narrative.
- **Verify the deployed file, not the working copy.** The engine edits
  were applied but the scenario file's `_make_scenario()` was missing
  the `pin_stations` builder in the deployed version. Always check
  both sides of a contract.
- **Anomaly vs absolute: both needed, different layers.** Contour map
  shows anomaly (heat dome spatial pattern). Pins show absolute
  temperature (what people experienced). March normals vary 53-86F
  across the region.
- **KMZ-only updates skip the full pipeline.** The gallery viewer's
  3D Earth button links to the KMZ file by name. Replacing the KMZ
  in `gallery/assets/` and pushing to GitHub is sufficient.
- **Presets should preserve scenario-specific settings.** The
  Gen-Mobile preset must save/restore the KMZ link and custom title
  rather than blanking them. Presets set general layout; scenario-
  specific data (KMZ links, trace visibility) should survive preset
  application.
- **Auto-generate mobile briefing, allow override.** Rather than
  requiring every scenario module to maintain dual briefings, the
  engine auto-generates a mobile version (title + first narrative
  paragraph). Scenarios can override with a `mobile_briefing` key.
  Single source of truth for the detail text.
- **WYSIWYG: viewer should not pre-empt Studio.** The gallery viewer
  (`index.html`) should be silent or neutral where decisions can be
  made by Studio. The info card duplication happened because the
  viewer had its own unconditional portrait click handler, ignoring
  whether Studio had enabled hover routing. Fix: check `_hover_mode`
  in layout -- if Studio didn't set it, the viewer stays silent.
- **Two independent info card systems existed.** Studio's
  `route_hover_to_panel` controlled standalone exports. The gallery
  viewer had its own system. The WYSIWYG principle unified them:
  the viewer now respects Studio's `_hover_mode` flag.
- **Strip redundant annotation title on mobile.** The gallery viewer
  already shows a title bar. The briefing annotation's `<b>title</b>`
  line is redundant in mobile context. Studio strips it during the
  mobile briefing swap (regex: `^<b>[^<]*</b>(\s*<br\s*/?>)*`).
- **Encyclopedia is where the gallery owns the narrative.** The data
  shows what happened. The "i" card explains why it happened and what
  it means. Leaning into attribution science and planetary boundary
  connections is where the project's "data preservation is climate
  action" philosophy gets its teeth.
- **Separate encyclopedia source from briefing.** The briefing serves
  the annotation (short, visual). The encyclopedia serves the "i"
  card (deep, scrollable). Different consumers, different content,
  different authoring. The encyclopedia has its own builder function
  and its own key in the scenario dict.
- **Organize Earth System Context by planetary boundaries.** Climate
  change, freshwater change, biosphere integrity, land system change,
  novel entities -- each boundary gets its own subsection. Not every
  boundary appears in every snapshot; they accumulate as the event
  escalates, building a cumulative narrative of interconnected stress.
- **Single-entry encyclopedia auto-shows "i" button.** Multi-trace
  orrery plots show "i" on hover (content varies per trace). Single-
  trace earth system teasers show "i" immediately on load -- the user
  should not need to tap a data point to discover the content exists.
- **innerHTML for encyclopedia body.** The orrery's plain text entries
  render identically through innerHTML. Earth system entries get HTML
  formatting (bold headers, italic boundary labels, line breaks).
  One-line change, backward compatible.
- **ERA5T is 5 days behind, not months.** The original assumption
  (~April 1-5 for March data) was based on final ERA5, not near-
  real-time ERA5T. ERA5T updates daily with ~5-day lag. This changes
  the developing scenario workflow: real data is available almost
  in real time, not weeks later.
- **Three-tier fetch is the right pattern for developing scenarios.**
  CSV cache (instant) -> CDS API (automatic) -> synthetic (always
  works). Each tier catches a different failure mode. The synthetic
  fallback means the pipeline never breaks, even without network
  access or API credentials.
- **Climatology is the expensive one-time cost.** The event day
  download is small (1 day x 24 hours x grid). The climatology
  download is large (30 years x 24 hours x grid) but only happens
  once per day-of-month. After that, it's cached and reusable.
- **`.cdsapirc` lives in user home, not project directory.** API
  keys should not end up in version control. The `cdsapi` package
  reads from `~/.cdsapirc` by default. On Windows: `C:\Users\{username}\.cdsapirc`.
- **Windows dotfile creation:** `notepad %USERPROFILE%\.cdsapirc`
  works from Command Prompt. Watch for Windows silently appending
  `.txt` -- verify with `dir %USERPROFILE%\.cdsapirc*`.
- **CDS license acceptance is a one-time manual step.** The API
  returns 403 until the user accepts the dataset's terms on the
  CDS web interface. The error message includes the direct URL.
  Build error messages that help the user fix the problem.
- **Grid expansion requires cache invalidation.** When expanding
  `grid_lat_range` / `grid_lon_range` in SNAPSHOT_CONFIGS, the old
  ERA5 cached files (CSV, raw NC, climatology NC) must be deleted
  so the CDS API re-fetches with the new extent. The three-tier
  fetch will load stale small-grid data from cache if old files
  remain. Pattern: delete `era5_western_*.csv`, `era5_raw_*.nc`,
  and `era5_clim_march_day*.nc` for affected dates before re-run.
- **Expanding grid doesn't break existing snapshots.** Earlier
  snapshots (Mar 14-20) keep their original smaller grid; only
  Mar 21+ use the expanded extent. Each snapshot's config drives
  its own grid independently.
- **"Modified Copernicus" is a license requirement, not courtesy.**
  The pipeline computes anomalies from raw ERA5 temperature data
  (not just reposting their maps). Copernicus license requires the
  phrase "modified Copernicus Climate Change Service information"
  when data has been processed. The encyclopedia "i" card is the
  right place for this attribution -- it's discoverable, contextual,
  and lives next to the data it describes.
- **Mode 7 for non-code domains.** Gemini provided the formal
  attribution language (Copernicus license requirements, citation
  format, "modified" qualifier). Claude implements it in the
  encyclopedia builder. Tony integrates. Same pattern as Sgr A*
  physics validation and git co-author attribution.
- **Anomaly vs records: complementary, not competing.** Anomaly
  (departure from daily normal) shows continental-scale event
  extent. Records (exceeding all-time March maximum) show where
  the anomaly exceeds the historical ceiling. The SE/Appalachia
  have high existing March ceilings (subtropical history); the
  interior West/Plains have low ceilings (normally cold in March).
  Both layers are necessary: the contour field says "the whole
  continent is abnormally hot"; the pins say "these places
  exceeded anything ever measured."
- **Let the data drive the grid.** Tony observed the ERA5 anomaly
  extending past the grid boundary and said "extend as needed."
  The grid expanded three times (Southwest -> Plains -> continental)
  as the event revealed itself through real data. This is the
  developing-scenario workflow: start focused, expand as the data
  demands.
- **The omega block is the engine.** Understanding the mechanism
  (jet stream buckles into omega shape, ridge locks in place,
  subsiding air heats adiabatically, two-pulse structure is
  internal oscillation not two events) elevates the encyclopedia
  from "what happened" to "why it happened." The mechanism also
  explains why the eastward creep occurs: the ridge axis migrates,
  pulling subtropical air progressively further east.
- **Blocking is natural; magnitude is anthropogenic.** The omega
  block pattern exists in the historical record -- it's standard
  atmospheric dynamics. Climate change doesn't create the blocking;
  it raises the floor. Every blocking event now starts from a
  1.3C warmer baseline. WWA: 4.7-7.2F added by anthropogenic
  warming. Both necessary; neither sufficient alone. This nuance
  matters for attribution credibility.

-----

*"The engine should be centralized and the scenarios connect to it,
whether it's land heating or ocean acidification and coral bleaching
or forest dieoff."* -- Tony, March 18, 2026

*"The contour map shows the overall pattern. Station figures tell the
local story."* -- Tony, March 22, 2026

*"The viewer should not pre-empt or supersede Studio. Where decisions
can be made by Studio, the viewer should be silent or neutral."*
-- Tony, March 23, 2026

*"This is where we own the content. It's not just data, it's also a
narrative. And we lean into the attribution science where objections
are most likely to arise."* -- Tony, March 23, 2026

*"The automatic approach is better if it's feasible."*
-- Tony, March 24, 2026, on building ERA5 fetch into the module

*"Extend as needed. The base map includes the entire US, why not
add more record breaking points as it goes east?"*
-- Tony, March 25, 2026, on expanding the grid beyond the
original Western US boundary

*"I'm seeing an anomaly of nearly 33F all the way to the east side
of our boundary. Maybe we should just extend the range across the
continent."* -- Tony, March 28, 2026, after ERA5 revealed the
continental scale of the event

*"What is the underlying meteorological condition driving the extreme
heat? Can we elucidate that?"* -- Tony, March 28, 2026, the question
that led to the omega block encyclopedia entry

*"Hi Claude it is now April 3rd. Could we build a final scenario
showing the completed second wave? Chicago hit a record too!"*
-- Tony, April 3, 2026, closing the arc

-----

## Summary

Nine snapshots. Sixteen days. Arizona desert to Great Lakes.
37 stations. 17 state records. 1,500+ station records. The
warmest March in recorded US history.

All on ERA5 reanalysis. No synthetic data remaining. Three-tier
fetch pipeline (CSV cache -> CDS API -> synthetic fallback)
proven across 6 sessions. Formal Copernicus attribution in every
encyclopedia entry. Omega block mechanism elucidated. Anomaly vs
records distinction documented. Continental grid driven by what
the data actually showed.

This is the first developing scenario captured in real time by
the Earth System pipeline. Data preservation is climate action.
