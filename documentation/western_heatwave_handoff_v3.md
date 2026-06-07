# Paloma's Orrery -- Western Heatwave Timeline Handoff v3

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

## What Was Accomplished

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

Six engine edits to `earth_system_generator.py`, all deployed:

1. **HTML tag stripping** in `create_intel_card()` (Issue 1)
2. **clampToGround** pin altitude in `build_spikes_kml()` (Issue 2)
3. **Continuous legend colorbar** in `create_legend_card()` (Issue 3)
4. **`pin_stations` parameter** on `build_spikes_kml()` signature (Issue 4)
5. **`pin_stations` early-return block** in `build_spikes_kml()` (Issue 4)
6. **`pin_stations` passthrough** in `run_scenario()` call (Issue 4)

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

## Issues Found and Fixed

### Issue 1: Intel Card Showing Raw HTML Tags (Fixed)

**Problem:** `create_intel_card()` in the engine uses `matplotlib.plt.text()`
which renders text literally. The briefing contained `<br>`, `<b>`, `<i>`
tags intended for the Plotly teaser (which interprets HTML). Intel card
showed raw tags.

**Fix:** Added HTML tag stripping in `create_intel_card()` before
`textwrap.fill()`:

```python
clean_briefing = re.sub(r'<[^>]+>', ' ', briefing).replace('  ', ' ').strip()
wrapped_briefing = textwrap.fill(clean_briefing, width=40)
```

Engine-side fix; protects all scenario modules. `re` already imported.

### Issue 2: KML Spikes Floating Above Surface (Fixed)

**Problem:** `build_spikes_kml()` uses `newpoint()` with `relativeToGround`
altitude mode. With `height_multiplier: 100000`, pins were floating at
500-2700km altitude, shifting dramatically in perspective during rotation.

**Root cause:** `newpoint()` creates placemark pins, not extruded polygons.
The `extrude=1` flag just draws a thin line from pin to ground. The height
lifts the pin icon off the surface.

**Fix:** Clamped pins to ground:

```python
# BEFORE:
pnt.coords = [(lon, lat, height)]
pnt.extrude = 1
pnt.altitudemode = simplekml.AltitudeMode.relativetoground

# AFTER:
pnt.coords = [(lon, lat, 0)]
pnt.altitudemode = simplekml.AltitudeMode.clamptoground
```

Engine-side fix; affects all scenarios. The height calculation code is
now dead but preserved for future Option B (true extruded polygon columns).

### Issue 3: Contour/Legend Color Mismatch (Fixed)

**Problem:** Contour heatmap uses `inferno_r` matplotlib colormap (0-35
range). Legend card uses discrete band patches with KML spike colors
(green/cyan/yellow/red/magenta). These are two independent color systems.
A pin showing 8.7F sat in an orange contour zone, but the legend said
orange = +25F.

**Root cause:** The legend was built for the KMZ spike layer colors, not
the contour colormap. This mismatch exists in ALL scenarios, not just
the Western heatwave -- it's less noticeable when data fills more of the
range.

**Fix:** Added `'legend_style': 'continuous'` option to engine's
`create_legend_card()`. When set, renders a matplotlib colorbar matching
the contour colormap instead of discrete band patches. Existing scenarios
without this key keep their discrete legends (backward compatible).

Engine change: `create_legend_card()` gains continuous colorbar path.
Scenario change: `WESTERN_HEATWAVE_THRESHOLDS['legend_style'] = 'continuous'`.

**Note:** To fix this for existing heatwave/coral scenarios, add
`'legend_style': 'continuous'` to their thresholds dict and regenerate.
Each scenario must be re-run through the pipeline.

### Issue 4: Grid Stride Pin Placement (Fixed)

**Problem:** `spike_stride: 200` (carried from coral scenario) produced
only 8 pins on March 21's 1683-point grid. Pins landed on arbitrary grid
cells in a diagonal line (sampling artifact), not at stations or population
centers. Pin values (8.7F) didn't correlate with narrative (15-20F above
normal).

**Root cause:** Stride samples every Nth grid point regardless of location.
The coral scenario needed stride to thin a dense ocean grid; the Western
heatwave needs pins at confirmed observation stations.

**Fix (three parts, all applied):**

Engine -- `build_spikes_kml()` gains `pin_stations` parameter with
early-return block:

```python
def build_spikes_kml(scenario_id, date, lats, lons, values, thresholds,
                     intel_path, legend_risk_path, pin_stations=None):
    ...
    if pin_stations:
        for station in pin_stations:
            label = f"{station['anomaly']:.1f}F"
            pnt = kml_spikes.newpoint(name=label)
            pnt.coords = [(station['lon'], station['lat'], 0)]
            pnt.altitudemode = simplekml.AltitudeMode.clamptoground
            pnt.description = station.get('note', '')
            pnt.style.iconstyle.scale = 0.6

        spikes_filename = os.path.join(DATA_DIR,
                          f"{date}_spikes_{scenario_id}.kml")
        kml_spikes.save(spikes_filename)
        return spikes_filename
```

Caller -- `run_scenario()` passes pin_stations:

```python
    spikes_filename = build_spikes_kml(scenario_id, date, lats, lons, values,
                                        thresholds, intel_path, legend_risk_path,
                                        pin_stations=scenario.get('pin_stations'))
```

Scenario -- `_make_scenario()` builds `pin_stations` from
`RECORD_STATIONS` filtered by date:

```python
    pin_stations = []
    for sid, station in RECORD_STATIONS.items():
        if station['first_date'] <= date_str:
            pin_stations.append({
                'name': sid.replace('_', ' '),
                'lat': station['lat'],
                'lon': station['lon'],
                'anomaly': station['anomaly'],
                'air_temp_f': station['air_temp_f'],
                'note': station.get('note', ''),
            })
```

**Deployment note:** The scenario-side `pin_stations` builder was
delivered but initially not applied to the deployed file. Without it,
`scenario.get('pin_stations')` returned `None` and the engine fell
through to the grid stride loop. Once the scenario file was updated
with the builder, all 5 snapshots showed correct station pins.

### Issue 5: Pin Design Decisions (Resolved)

Tony's decision after reviewing pin behavior:

1. **Plot ALL record-breaking pins including overlapping ones** -- the
   accumulation of records at the same location (e.g., Phoenix breaking
   its own record three times) IS the story
2. **Smaller pins** for readability -- `iconstyle.scale = 0.6`
3. **Intel card note** -- briefing text includes "Pins mark confirmed
   record-breaking observations"

The floor/dedup approach designed earlier was **not applied** -- Tony
chose to show all pins because the overlapping records at Phoenix, Las
Vegas, and Yuma tell the story of escalating severity.

### Issue 6: Pin Labels Should Show Absolute Temperature (Pending)

**Problem:** Pin labels show anomaly (e.g., "27.0F") which requires
interpretation. The anomaly is already conveyed by the contour map.
Users immediately understand absolute temperatures.

**Design decision:** Pins show absolute temperature; contour shows
anomaly. Each layer tells a different part of the story without
redundancy.

**Fix:** In engine `build_spikes_kml()` station pin block:

```python
# BEFORE:
            label = f"{station['anomaly']:.1f}F"

# AFTER:
            label = f"{station['air_temp_f']:.0f}F"
```

**Scientific note:** March "normal high" varies dramatically across
the region (Phoenix 78F, Denver 55F, Death Valley 86F). A 25F anomaly
means very different absolute conditions at different stations. The
contour map (anomaly) shows the heat dome pattern; the pins (absolute)
show what people actually experienced. Both are needed.

KMZ-only change -- regenerate KMZs, copy to `gallery/assets/`, push.
No teaser/json/metadata update needed.

### Issue 7: Intel Card Readability (Pending)

**Problem:** After HTML tag stripping (Issue 1), the intel card text
is a run-on block. The briefing has logical sections (title, details,
attribution, data provenance) that are collapsed into a wall of text.

**Fix:** Improve the HTML stripping to preserve line breaks. In engine
`create_intel_card()`:

```python
# BEFORE:
    clean_briefing = re.sub(r'<[^>]+>', ' ', briefing).replace('  ', ' ').strip()
    wrapped_briefing = textwrap.fill(clean_briefing, width=40)

# AFTER:
    # Convert <br> to newlines, then strip remaining HTML tags
    spaced = briefing.replace('<br>', '\n').replace('<BR>', '\n')
    clean_briefing = re.sub(r'<[^>]+>', '', spaced).strip()
    # Wrap each line independently so line breaks are preserved
    lines = clean_briefing.split('\n')
    wrapped_lines = []
    for line in lines:
        line = line.strip()
        if line:
            wrapped_lines.append(textwrap.fill(line, width=40))
    wrapped_briefing = '\n'.join(wrapped_lines)
```

Engine-side fix; preserves the structure the briefing HTML already has.
Each `<br>` becomes a real line break in the matplotlib text. Bold/italic
tags are stripped but visual grouping survives.

KMZ-only change -- regenerate KMZs, copy to `gallery/assets/`, push.

-----

## Files Delivered and Deployed

| File | Status | Notes |
|------|--------|-------|
| `scenarios_western_heatwave_march_2026.py` | Deployed | 5 snapshots, pin_stations, all pins shown |
| `earth_system_generator.py` | Deployed | All 6 engine edits applied |
| `western_heatwave_handoff_v1.md` | Superseded | Replaced by v2 |
| `western_heatwave_handoff_v2.md` | Superseded | Replaced by this v3 |

-----

## Pending Edits (KMZ-Only, No Full Pipeline Needed)

These edits only affect the KMZ output. After applying, regenerate
KMZs, copy to `gallery/assets/`, and push to GitHub. The gallery
viewer's 3D Earth button links to the KMZ by filename -- it will
serve the updated file without any teaser/json/metadata changes.

1. **Pin labels to absolute temperature** (Issue 6) -- one line in
   engine `build_spikes_kml()` station pin block
2. **Intel card line breaks** (Issue 7) -- replace HTML stripping
   logic in engine `create_intel_card()`

-----

## On the Horizon

- **ERA5 data swap** -- when ERA5 reanalysis becomes available for March
  2026 (~April 1-5), drop CSV files named `era5_western_2026-03-XX.csv`
  into `data/` directory. The fetch function will pick them up
  automatically. No code changes needed.
- **March 24+ snapshots** -- as the event continues, add new
  `SNAPSHOT_CONFIGS` entries + `RECORD_STATIONS` entries + extend
  `SCENARIOS` list. One dict per new date.
- **Unified KMZ timeline** -- single KMZ with dated folders (Option 2
  from earlier design discussion). The `run_scenario_timeline()` function
  was sketched but not implemented. Would wrap all 5 snapshots in a
  single file with toggleable folders in GE sidebar.
- **Continuous legend for existing scenarios** -- adding
  `'legend_style': 'continuous'` to `HEATWAVE_THRESHOLDS` and
  `CORAL_THRESHOLDS` + regenerating all scenarios would fix the
  contour/legend mismatch globally. Not urgent.
- **True 3D extruded columns (Option B)** -- replace `newpoint()` with
  `newpolygon()` for real 3D bars rising from surface, color-coded by
  band. Would be tied to contour map, not floating pins. Future feature,
  not urgent.
- **Intel card full HTML rendering** -- three options explored:
  (A) simulate formatting with multiple plt.text() calls,
  (B) render HTML to PNG via imgkit/weasyprint,
  (C) replace PNG with KML BalloonStyle HTML in a clickable placemark.
  Option C is cleanest -- GE natively renders HTML in description
  balloons, the briefing HTML already exists, no PNG generation needed.
  Tradeoff: click-to-see vs always-visible. Not critical.

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
  scenario. Preserve `<br>` as newlines before stripping other tags.
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
  the `pin_stations` builder in the deployed version. The engine was
  ready but receiving `None` for pin_stations, falling through to
  grid stride. Always check both sides of a contract.
- **Anomaly vs absolute: both needed, different layers.** Contour map
  shows anomaly (heat dome spatial pattern). Pins show absolute
  temperature (what people experienced). March normals vary 53-86F
  across the region, so a uniform anomaly means very different
  conditions at different stations.
- **KMZ-only updates skip the full pipeline.** The gallery viewer's
  3D Earth button links to the KMZ file by name. Replacing the KMZ
  in `gallery/assets/` and pushing to GitHub is sufficient -- no
  teaser, json_converter, or metadata update needed.

-----

*"The engine should be centralized and the scenarios connect to it,
whether it's land heating or ocean acidification and coral bleaching
or forest dieoff."* -- Tony, March 18, 2026

*"The contour map shows the overall pattern. Station figures tell the
local story."* -- Tony, March 22, 2026
