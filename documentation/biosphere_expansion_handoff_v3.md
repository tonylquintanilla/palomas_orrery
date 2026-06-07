# Paloma's Orrery -- Biosphere Expansion Handoff v3

## Session Handoff | March 19, 2026 | Claude Opus 4.6

*Updated from v2 (March 18) to capture the engine refactor, coral
bleaching implementation, and visual polish backlog from the
March 19 build session.*

---

## What Was Accomplished

### Step 1: Engine Refactor (Complete, Tested, Deployed)

Extracted the shared pipeline from `earth_system_generator.py` and
moved all heatwave-specific data into `scenarios_heatwaves.py`.

**`earth_system_generator.py`** (665 lines) -- The Engine:
- `run_scenario(scenario)` -- orchestrates fetch -> cards -> KML -> teaser -> KMZ
- `build_spikes_kml()` -- generalized; colors/heights from `thresholds['bands']`; `spike_stride` support
- `build_heatmap_kml()` -- generalized; contour levels/cmap from config
- `build_impact_kml()` -- generalized; `pop_radius_divisor` from config
- `generate_plotly_teaser()` -- generalized; colorscale/cmin/cmax/colorbar title from config
- `create_legend_card()` -- dynamic height, `legend_title` from config, per-scenario filename
- `create_intel_card()`, `create_pop_legend_card()` -- unchanged
- `package_and_cleanup()` -- unchanged (merged single-doc KMZ, no-delete)
- `MissionSelector` GUI -- imports from scenario modules, shows `[HEAT]`/`[CORA]` prefixes

**`scenarios_heatwaves.py`** (639 lines) -- Heatwave Plugin:
- `fetch_era5_heatwave()` -- standalone function (was GUI method)
- `HEATWAVE_THRESHOLDS` -- shared config with `legend_title`, `pop_radius_divisor`
- `SCENARIOS` list -- 27 scenario dicts, all verified

**Regression test:** Asian Heat Belt 2024 scenario run through full
pipeline: GUI -> generate -> Studio load -> json_converter -> gallery
viewer with 3D Earth button. All outputs match deployed gallery.

### Step 2: Coral Bleaching Implementation (Data Fetched, Pipeline Works, Visual Polish Pending)

**`scenarios_coral_bleaching.py`** (222 lines) -- Coral Plugin:
- `fetch_noaa_coral()` -- three-server fallback with local CSV cache
- `_parse_dhw_csv()` -- handles both variable names and lon conventions
- `CORAL_THRESHOLDS` -- DHW bands (4/8/12), `spike_stride: 200`, `pop_radius_divisor: 50000`
- Florida 2023 scenario with 4 population centers

**Data acquisition:** NOAA ERDDAP servers were all experiencing errors
(timeout, HTTP 500) during the session. Data was manually downloaded
from PacIOOS Hawaii ERDDAP web form and cached locally as
`data/florida_coral_2023_dhw.csv`. The fetch function now checks for
local CSV first, making future runs independent of server availability.

**Pipeline verified:** Teaser HTML and KMZ blockbuster both generate
successfully from cached data. Full pipeline through Studio and
gallery viewer not yet tested due to visual issues identified below.

### Gallery Studio Bug Fix

Landscape and Portrait presets were wiping the KMZ handoff field.
Fixed by stashing `var_kmz_link` before preset application and
restoring after. Same pattern the Original preset already used.

---

## Visual Polish Backlog (Next Session)

Both the teaser and blockbuster need visual refinement for the
coral use case. The heatwave visual design assumed coarse ERA5 grids
(~100 points); coral NOAA data is 0.05-degree resolution (~13,500
points). The density difference requires different visual treatment.

### Teaser Issues

1. **Marker density creates solid blob.** 13,585 scattermapbox markers
   at 0.05-degree spacing merge into what looks like a contour map.
   Individual markers are not visible. Options: stride the teaser data,
   reduce marker size, reduce opacity, or switch to a different trace
   type (e.g., densitymapbox, choroplethmapbox).

2. **Colorbar lacks threshold context.** The DHW colorbar shows a
   gradient from 0-16 but doesn't indicate the 4/8/12 breakpoints
   that define Warning/Significant/Severe/Mortality. Annotated tick
   marks or a custom discrete colorscale would make the data speak.

### Blockbuster (Google Earth) Issues

1. **Screen overlays overlap and are hard to read.** Intel card (25%
   width, top-left), risk legend (15%, bottom-right), and pop legend
   (15%, bottom-left) all render simultaneously. At the Florida Keys
   zoom level they crowd the viewport.

2. **Legends not clearly connected to their layers.** User doesn't
   know which legend belongs to which toggleable folder.

3. **Font too small on intel card.** The briefing text was sized for
   continental-scale views; at Keys zoom it's illegible.

### Design Direction (To Discuss)

The heatwave blockbuster was designed when it was the only narrative
vehicle. Now that the teaser carries the briefing text and the gallery
viewer provides the reading context, the blockbuster could be
simplified: fewer/smaller overlays, let the 3D data speak for itself.

For the teaser, consider whether the coral visualization should use
a different Plotly trace type than scattermapbox. A densitymapbox or
a gridded heatmap might better represent the continuous thermal field
at this resolution.

---

## ERDDAP Server Lessons

### Three Servers, Three Conventions

| Server | Dataset ID | Variable | Longitude | Status (Mar 19) |
|--------|-----------|----------|-----------|-----------------|
| coastwatch.noaa.gov | noaacrwdhwDaily | degree_heating_week | -180/180 | Timeout |
| coastwatch.pfeg.noaa.gov | NOAA_DHW | degree_heating_week | -180/180 | HTTP 500 |
| pae-paha.pacioos.hawaii.edu | dhw_5km | CRW_DHW | 0/360 | HTTP 500 (API), works (web form) |

### Data Preservation Pattern

The fetch function now implements: local CSV cache -> NOAA primary ->
NOAA Pacific -> PacIOOS Hawaii. Once data is cached locally, the
pipeline never depends on servers again. Manual download instructions
are displayed in the error dialog if all servers fail.

This is the "Data Preservation is Climate Action" pattern in code:
fetch once, cache forever, never lose the record.

### NOAA Infrastructure Context

NOAA's workforce was cut ~20% in early 2025. The CoastWatch West
Coast server still carries a stale government shutdown banner from
October 2025. Server reliability for research data products
(as opposed to life-safety weather forecasts) should be expected
to degrade. The local cache fallback is not optional -- it's the
primary data preservation mechanism.

---

## Key Files (Current State)

| File | Lines | Role | Status |
|------|-------|------|--------|
| `earth_system_generator.py` | 665 | Engine | Deployed, tested |
| `scenarios_heatwaves.py` | 639 | Heatwave configs + ERA5 fetch | Deployed, tested |
| `scenarios_coral_bleaching.py` | 222 | Coral configs + ERDDAP fetch | Deployed, visual polish pending |
| `gallery_studio.py` | 5077 | Preset KMZ fix applied | Deployed |
| `data/florida_coral_2023_dhw.csv` | 16263 | Cached NOAA DHW data | Local only |

---

## Implementation Plan (Remaining)

### Next: Visual Polish (Step 3 Continued)

Rethink teaser and blockbuster presentation for high-density coral
data. This is a Mode 5 (visual/aesthetic) session -- Tony leads,
Claude implements.

### Then: Gallery Pipeline Test (Step 3 Completion)

Once visuals are acceptable, run coral through:
Studio -> json_converter -> gallery viewer -> verify 3D Earth button

### Then: Additional Coral Scenarios (Step 4)

- Great Barrier Reef 2024 (fifth mass bleaching in eight years)
- Indian Ocean (Chagos / Maldives)
- Red Sea

Each requires a manual ERDDAP download if servers remain unreliable,
or will auto-fetch when servers recover. Same pattern: add scenario
dict to SCENARIOS list, cache the CSV, generate.

### Then: Phoenix March 2026 Heatwave (When ERA5 Data Available)

```python
{
    'scenario_id': 'phoenix_march_2026',
    'name': 'Phoenix March Inferno (March 2026)',
    'date': '2026-03-21',  # pick peak day once data settles
    'lat_range': range(37, 31, -1),
    'lon_range': range(-115, -109, 1),
    'focus_val_min': 22.0,
    ...
}
```

Earliest triple-digit day ever recorded. Earliest Extreme Heat
Warning ever issued. 20-30 degrees above average. ERA5 reanalysis
data typically available within 1-2 weeks of the event.

### Then: Next Boundary Type (Step 5)

Forest dieoff / Amazon tipping point using Global Forest Watch data.
Same pattern: `scenarios_forest_dieoff.py` with fetch function and
SCENARIOS list.

---

## Technical Lessons From This Session

- **Engine extraction before expansion:** Refactoring heatwaves first
  (with 27 known-good regression targets) proved the engine before
  adding coral. Lower risk than building both simultaneously.

- **Config-driven generalization:** `thresholds` dict carries all
  boundary-type differences (bands, colors, heights, stride, legend
  title, pop radius, contour settings). Engine never knows what it's
  rendering.

- **`spike_stride` for dense data:** NOAA 5km grid produces 100x more
  points than ERA5 2-degree grid. Stride 200 reduces to ~68 spikes
  for GE; heatmap still uses full resolution.

- **`pop_radius_divisor` for scale:** Heatwave megacities (32M) vs
  coral coastal towns (26K) need different circle scaling. Config
  handles it.

- **ERDDAP server diversity:** Same dataset, three hosts, three
  variable names, two longitude conventions. Code must handle all
  combinations. Local CSV cache is the ultimate fallback.

- **Legend per scenario:** Shared legend filename caused collisions
  when multiple boundary types were generated. Per-scenario filenames
  (`legend_risk_{scenario_id}.png`) and configurable `legend_title`
  solved both problems.

- **Preset KMZ wipe bug:** Gallery Studio presets reset all config
  fields including KMZ handoff. Fix: stash before preset, restore
  after. Same pattern Original preset already used.

- **Dense marine data needs different visual treatment:** The
  heatwave teaser/blockbuster design assumed sparse continental grids.
  Coral's 0.05-degree marine data requires rethinking marker density,
  overlay sizing, and possibly trace type.

---

## Decision Log (This Session)

| Question | Decision | Rationale |
|----------|----------|-----------|
| Refactor approach? | Agentic (Mode 2) | New files + heavily modified engine |
| Test heatwave regression how? | GUI + Studio + gallery pipeline | Full end-to-end validation |
| Coral spike density? | stride=200 (~68 spikes) | Visual match to heatwave density |
| ERDDAP servers down? | Manual download + local cache | Data preservation pattern |
| Coral teaser/blockbuster polish? | Deferred to next session | Mode 5 work needs fresh eyes |
| Phoenix March 2026? | Add when ERA5 available | ~1-2 weeks for reanalysis data |

---

*"The engine should be centralized and the scenarios connect to it,
whether it's land heating or ocean acidification and coral bleaching
or forest dieoff."* -- Tony, March 18, 2026

*"Data preservation is climate action."* -- Project philosophy,
validated by NOAA server failures during this session
