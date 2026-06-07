# Paloma's Orrery -- Western Heatwave Timeline Handoff v5

## Session Handoff | March 22-23, 2026 | Claude Opus 4.6

-----

## Context

A 1-in-500-year heat event is unfolding across Western North America
(March 14-21+, 2026). World Weather Attribution classified it as
"virtually impossible" without human-induced climate change. This is
the first *developing* scenario in the Earth System pipeline -- not
historical, but being captured as it happens.

The scenario module tells the story as a 5-snapshot timeline:

| Date     | Label          | CSI | Stations | Max Anomaly |
|----------|----------------|-----|----------|-------------|
| March 14 | The Spark      | 2   | 3        | 17.8F       |
| March 17 | The Pivot      | 3   | 6        | 23.1F       |
| March 18 | Records Fall   | 4   | 9        | 25.6F       |
| March 20 | The Peak       | 5   | 12       | 32.8F       |
| March 21 | Eastward Surge | 5   | 15       | 32.0F       |

CSI = Climate Shift Index (1-5 scale, how much more likely due to
climate change).

-----

## What Was Accomplished (Sessions 1-2, March 22-23)

### Scenario Module (Complete, Tested, Deployed)

**`scenarios_western_heatwave_march_2026.py`** (~700 lines):

- `SNAPSHOT_CONFIGS` -- date-parameterized configuration driving anomaly
  magnitude, spatial extent, station activation, and CSI level
- `RECORD_STATIONS` -- 15 confirmed observation stations with `first_date`
  gating (stations accumulate as the event progresses)
- `fetch_western_heatwave()` -- shared fetch function: tries ERA5 CSV
  cache first, falls back to realistic synthetic grid
- `_build_synthetic_field()` -- Gaussian baseline + RBF station spikes +
  smoothing + re-pinning for exact station values
- `_make_scenario()` -- factory builds scenario dict with `pin_stations`
  list filtered by date from `RECORD_STATIONS`
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
   (20 all around), colorbar on, modebar on, landscape output
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

-----

## Files Delivered and Deployed

| File | Status | Notes |
|------|--------|-------|
| `scenarios_western_heatwave_march_2026.py` | Deployed | 5 snapshots, pin_stations |
| `earth_system_generator.py` | Deployed | 8 engine edits + mobile briefing pipeline |
| `gallery_studio.py` | Deployed | Gen-Mobile preset, mobile briefing, use_mobile_briefing |
| `index.html` | Deployed | WYSIWYG info card fix |
| `western_heatwave_handoff_v1-v4.md` | Superseded | Replaced by this v5 |

-----

## On the Horizon

- **ERA5 data swap** -- when ERA5 reanalysis becomes available for
  March 2026 (~April 1-5), drop CSV files named
  `era5_western_2026-03-XX.csv` into `data/` directory. The fetch
  function will pick them up automatically. No code changes needed.
- **March 24+ snapshots** -- as the event continues, add new
  `SNAPSHOT_CONFIGS` entries + `RECORD_STATIONS` entries + extend
  `SCENARIOS` list. One dict per new date.
- **Unified KMZ timeline** -- single KMZ with dated folders (Option 2
  from earlier design discussion). Would wrap all 5 snapshots in a
  single file with toggleable folders in GE sidebar.
- **Continuous legend for existing scenarios** -- adding
  `'legend_style': 'continuous'` to `HEATWAVE_THRESHOLDS` and
  `CORAL_THRESHOLDS` + regenerating all scenarios would fix the
  contour/legend mismatch globally. Not urgent.
- **True 3D extruded columns (Option B)** -- replace `newpoint()` with
  `newpolygon()` for real 3D bars rising from surface, color-coded by
  band. Would be tied to contour map, not floating pins. Future feature.
- **Intel card full HTML rendering** -- Option C (KML BalloonStyle
  HTML in a clickable placemark) is cleanest long-term. GE natively
  renders HTML in description balloons. Not critical.

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

-----

*"The engine should be centralized and the scenarios connect to it,
whether it's land heating or ocean acidification and coral bleaching
or forest dieoff."* -- Tony, March 18, 2026

*"The contour map shows the overall pattern. Station figures tell the
local story."* -- Tony, March 22, 2026

*"The viewer should not pre-empt or supersede Studio. Where decisions
can be made by Studio, the viewer should be silent or neutral."*
-- Tony, March 23, 2026
