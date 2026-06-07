# Paloma's Orrery -- Western Heatwave Timeline Handoff v1

## Session Handoff | March 22, 2026 | Claude Opus 4.6

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

### Testing Protocol (Phases 1-5 Complete)

- Phase 1: Data validation (`--validate`) -- all 5 snapshots pass
- Phase 2: Single snapshot through engine -- March 20 "The Peak" verified
- Phase 3: Visual progression -- March 14 vs March 20 side-by-side confirmed
- Phase 4: Full batch -- all 5 KMZs + teasers generated
- Phase 5: Gallery integration -- teaser through json_converter verified

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

### Issue 4: Grid Stride Pin Placement (In Progress)

**Problem:** `spike_stride: 200` (carried from coral scenario) produced
only 8 pins on March 21's 1683-point grid. Pins landed on arbitrary grid
cells in a diagonal line (sampling artifact), not at stations or population
centers. Pin values (8.7F) didn't correlate with narrative (15-20F above
normal).

**Root cause:** Stride samples every Nth grid point regardless of location.
The coral scenario needed stride to thin a dense ocean grid; the Western
heatwave needs pins at confirmed observation stations.

**Solution designed (not yet implemented):**

**Engine edit** -- `build_spikes_kml()` gains `pin_stations` parameter:

```python
def build_spikes_kml(scenario_id, date, lats, lons, values, thresholds,
                     intel_path, legend_risk_path, pin_stations=None):
```

With early-return block:

```python
    if pin_stations:
        for station in pin_stations:
            label = f"{station['anomaly']:.1f}F"
            pnt = kml_spikes.newpoint(name=label)
            pnt.coords = [(station['lon'], station['lat'], 0)]
            pnt.altitudemode = simplekml.AltitudeMode.clamptoground
            pnt.description = station.get('note', '')

        spikes_filename = os.path.join(DATA_DIR,
                          f"{date}_spikes_{scenario_id}.kml")
        kml_spikes.save(spikes_filename)
        return spikes_filename
```

**Caller edit** -- `run_scenario()` passes pin_stations:

```python
    spikes_filename = build_spikes_kml(scenario_id, date, lats, lons, values,
                                        thresholds, intel_path, legend_risk_path,
                                        pin_stations=scenario.get('pin_stations'))
```

**Scenario edit** -- `_make_scenario()` already builds `pin_stations`
from `RECORD_STATIONS` filtered by date (implemented in scenario file,
delivered this session).

### Issue 5: Pin Density and Duplicates (Design Complete, Not Implemented)

**Problem:** Without filtering, March 21 has 15 pins including duplicates
at same lat/lon (e.g., Phoenix has "early 17F", "record 23F", and
"peak 27F" -- three pins stacked on each other).

**Solution designed:**

Apply 20F anomaly floor + deduplicate by location (keep highest anomaly
per lat/lon). This produces:

| Date     | Pins | Result                                          |
|----------|------|-------------------------------------------------|
| March 14 | 0    | Contour only (story hasn't broken yet)          |
| March 17 | 2    | Las Vegas 22F, Tucson 21F                       |
| March 18 | 4    | + Phoenix record 23F, Death Valley 22F          |
| March 20 | 6    | + Martinez Lake 32F, Yuma 27F, Phoenix peak 27F |
| March 21 | 9    | + Denver 30F, SLC 25F, Albuquerque 25F          |

**Implementation:** In `_make_scenario()`, after building `pin_stations`:

```python
    # Filter by anomaly floor
    pin_floor = 20.0
    filtered = [p for p in pin_stations if p['anomaly'] >= pin_floor]

    # Deduplicate: keep highest anomaly per location
    by_loc = {}
    for p in filtered:
        key = (p['lat'], p['lon'])
        if key not in by_loc or p['anomaly'] > by_loc[key]['anomaly']:
            by_loc[key] = p
    pin_stations = sorted(by_loc.values(), key=lambda x: -x['anomaly'])
```

**Not yet applied.** Tony to decide on floor value and implement.

-----

## Files Delivered

| File | Status | Notes |
|------|--------|-------|
| `scenarios_western_heatwave_march_2026.py` | Delivered | 5 snapshots, pin_stations built, floor/dedup not yet applied |
| `earth_system_generator.py` | Tony applied edits locally | HTML strip, clampToGround, continuous legend |

-----

## Pending Engine Edits (Not Yet Applied)

These two edits enable station pin mode in the KMZ spike layer:

1. **`run_scenario()`** -- add `pin_stations=scenario.get('pin_stations')`
   to `build_spikes_kml()` call (line 82-83)

2. **`build_spikes_kml()`** -- add `pin_stations=None` parameter +
   early-return station pin block (after screen overlays, before grid
   stride loop)

Code for both edits is in Issue 4 section above.

-----

## On the Horizon

- **Apply pin_stations engine edits** and regenerate to verify station
  pins appear correctly in GE
- **Apply 20F floor + dedup** in `_make_scenario()` and verify pin
  counts match the design table (0/2/4/6/9)
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
  HTML; matplotlib intel card renders plain text. Either strip tags at
  the consumer (engine fix, protects all modules) or provide separate
  text (per-module burden). Engine fix is better.
- **Developing scenarios are structurally different.** Historical
  scenarios are static; this one accumulates data over time. The
  `first_date` gating on stations and the parameterized snapshot configs
  handle this cleanly -- each snapshot is a frozen moment, but the
  SCENARIOS list grows as the event progresses.
- **Floor + dedup is cleaner than stride for curated pins.** Grid stride
  is a spatial sampling strategy; floor + dedup is a significance filter.
  For a developing story with confirmed records, significance wins.

-----

*"The engine should be centralized and the scenarios connect to it,
whether it's land heating or ocean acidification and coral bleaching
or forest dieoff."* -- Tony, March 18, 2026

*"The contour map shows the overall pattern. Station figures tell the
local story."* -- Tony, March 22, 2026
