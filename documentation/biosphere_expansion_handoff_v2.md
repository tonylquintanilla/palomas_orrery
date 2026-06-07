# Paloma's Orrery -- Biosphere Expansion Handoff v2

## Session Handoff | March 18, 2026 | Claude Opus 4.6

*Updated from v1 (Feb 28 - Mar 2) to incorporate architecture decisions
from the March 18 planning session.*

---

## Architecture Decision: The Unified Engine

### The Problem

`biosphere_coral_generator.py` was built as a standalone proof of
concept before the pipeline matured in Sessions 20-21. It works, but
duplicates logic that `earth_system_generator.py` already handles
(KML building, KMZ merging, Plotly teaser generation, packaging).
As we add more planetary boundaries (forest dieoff, etc.), parallel
standalone generators will diverge and create maintenance debt.

### The Decision

**Centralize the engine. Scenarios plug into it.**

One shared pipeline in `earth_system_generator.py` handles all
common work. Each planetary boundary type provides only a fetch
function and a list of scenario config dicts. The engine never
knows or cares whether it's rendering ocean heat or forest loss.

### Module Structure

```
earth_system_generator.py          — The Engine (shared pipeline)
scenarios_heatwaves.py             — Heatwave scenario configs + ERA5 fetch
scenarios_coral_bleaching.py       — Coral scenario configs + NOAA ERDDAP fetch
scenarios_forest_dieoff.py         — (Future) Forest configs + Global Forest Watch fetch
```

### What Lives in the Engine (`earth_system_generator.py`)

- `run_scenario(scenario)` — Orchestrates: fetch → blockbuster → teaser
- `generate_teaser(scenario)` — Plotly 2D map from (lat, lon, value).
  ESRI World Topo basemap, colorscale from config, briefing annotation
  (200 char max, semi-transparent), hint text, `_kmz_handoff` key,
  HTML export.
- `generate_blockbuster(scenario)` — Three KML layers from (lat, lon,
  value) using threshold config. Contour PNG, spike extrusions,
  population circles. Writes raw KMLs to `data/`. Merges into single
  `doc.kml`. Packages KMZ. No deletions.
- `get_color_and_height(value, thresholds)` — Generic: takes value +
  threshold config, returns KML color and extrusion height.
- `create_circle_polygon(lat, lon, radius_km)` — Already generic.
- `merge_kml_to_doc(kml_files)` — Regex merge from Session 20.
- `package_kmz(scenario_id)` — ZIP bundling, no-delete policy.

This also ensures a **uniform visual look across all planetary
boundary topics** — consistent basemaps, annotation style, button
behavior, and gallery integration.

### What Lives in Each Scenario Module

Each module provides exactly two things:

1. **A fetch function** — `fetch_noaa_coral(scenario)`,
   `fetch_era5_heatwave(scenario)`, etc. Takes a scenario dict,
   populates `lats`, `lons`, `values`.

2. **A SCENARIOS list** — Config dicts for each event.

### The Scenario Config Contract

```python
scenario = {
    # Identity
    'scenario_id': 'florida_coral_2023',
    'name': 'Florida & Cuba Mass Bleaching',
    'boundary_type': 'coral_bleaching',

    # Data (populated by the fetch function)
    'lats': [],
    'lons': [],
    'values': [],           # Generic — DHW for coral, temp anomaly for heat

    # Geography
    'lat_bounds': (22.0, 27.0),
    'lon_bounds': (-84.0, -76.0),

    # Human impact layer
    'populations': [
        {'name': 'Miami Metro', 'lat': 25.76, 'lon': -80.19, 'pop': 6100000},
        {'name': 'Key West', 'lat': 24.5551, 'lon': -81.78, 'pop': 26000},
        {'name': 'Havana', 'lat': 23.1136, 'lon': -82.3666, 'pop': 2100000},
        {'name': 'Nassau', 'lat': 25.0443, 'lon': -77.3504, 'pop': 275000},
    ],

    # Visual thresholds (drives spike colors and heights)
    'thresholds': {
        'unit_label': 'Degree Heating Weeks (DHW)',
        'min_display': 0,
        'spike_floor': 4,
        'bands': [
            (4,  'ff00a5ff', 'Warning'),
            (8,  'ff0000ff', 'Significant Bleaching'),
            (12, 'ff800080', 'Severe Mass Bleaching'),
            (float('inf'), 'ff000000', 'Systemic Mortality'),
        ],
        'height_multiplier': 1000,
        'colorscale': 'YlOrRd',
        'cmax': 16,
    },

    # Narrative
    'briefing': 'August 2023: Sea surface temperatures off Florida...',
    'description': 'Peak thermal stress during the worst Caribbean...',

    # Fetch function (each module provides its own)
    'fetch': fetch_noaa_coral,
}
```

### How You Run It

```python
from earth_system_generator import run_scenario
from scenarios_coral_bleaching import SCENARIOS

run_scenario(SCENARIOS[0])  # Florida 2023

# Or batch all heatwaves
from scenarios_heatwaves import SCENARIOS as HEAT_SCENARIOS
for s in HEAT_SCENARIOS:
    run_scenario(s)
```


---

## Implementation Plan

### Step 1: Extract the Engine (Heatwave Refactor)

Pull the generic pipeline functions out of `earth_system_generator.py`
into clean engine functions. Move heatwave-specific code (ERA5 fetch,
27 scenario definitions, temperature threshold bands) into
`scenarios_heatwaves.py`.

**Success criterion:** Running the heatwave batch through the new
structure produces identical outputs to what's already deployed in
the gallery.

### Step 2: Validate Against Deployed Gallery

Run 1-2 heatwave scenarios through the refactored pipeline. Diff
outputs against what's live on GitHub Pages. Teaser HTML, KMZ
structure, and merged `doc.kml` should be functionally identical.
This is the regression test.

### Step 3: Add `scenarios_coral_bleaching.py`

Write `fetch_noaa_coral()` and the Florida 2023 scenario dict. Run
through the engine. Teaser gets ESRI basemap, YlOrRd colorscale,
briefing annotation, `_kmz_handoff` key automatically. Blockbuster
produces properly merged KMZ with three toggleable folders.

**Test scenario:** Florida & Cuba Mass Bleaching, 2023-08-25.

### Step 4: Curate Additional Coral Scenarios (Phase 2)

Expand beyond Florida 2023:
- Great Barrier Reef 2024 (fifth mass bleaching in eight years)
- Indian Ocean (Chagos / Maldives)
- Red Sea

Each tells a different story about reef vulnerability. Curatorial
decision as much as technical.

### Step 5: Expand to Next Boundary Type

With heatwaves and coral running through the same engine, add
Land-System Change (Forest Cover / Amazon Tipping Point) using
Global Forest Watch data. Same pattern: fetch function + SCENARIOS
list in `scenarios_forest_dieoff.py`.


---

## Status of Prior Work

### Completed (Pre-Session)

- 27 heatwave scenarios processed through gallery pipeline and
  deployed to GitHub Pages
- `biosphere_coral_generator.py` validates NOAA ERDDAP fetch,
  DHW spike coloring, KMZ packaging (proof of concept)
- Sessions 20-21 fixes all implemented: merged KML, no-delete,
  ESRI basemap, YlOrRd colorscale, `_kmz_handoff` whitelisting,
  button positioning, mapbox zoom handling, KMZ path fix,
  `.gitattributes` binary markers

### Not Yet Started

- Engine extraction from `earth_system_generator.py` (Step 1)
- `scenarios_heatwaves.py` module (Step 1)
- `scenarios_coral_bleaching.py` module (Step 3)


---

## Key Files

| File | Role |
|------|------|
| `earth_system_generator.py` | Engine (to be refactored) |
| `scenarios_heatwaves.py` | New: heatwave configs + ERA5 fetch |
| `scenarios_coral_bleaching.py` | New: coral configs + ERDDAP fetch |
| `biosphere_coral_generator.py` | Legacy POC (fetch logic reused, rest retired) |
| `gallery_studio.py` | Green preset, KMZ handoff field |
| `json_converter.py` | HTML → JSON, `_kmz_handoff` passthrough |
| `index.html` | 3D Earth button, mobile intent URL |


---

## Technical Lessons Carried Forward

All lessons from v1 handoff remain valid. Additional from this session:

- **Centralize before expanding:** Don't build parallel generators.
  Extract the engine from the first working implementation, validate
  it, then add new data sources as plugins.

- **Refactor heatwaves first:** Lower risk — 27 known-good scenarios
  to regression test against. Coral becomes "just add a fetch function"
  once the engine is proven.

- **Scenario config as contract:** The engine and scenario modules
  communicate through a well-defined dict structure. If a new
  boundary type needs something the config doesn't support, extend
  the config — don't fork the engine.


---

## Workflow Summary (Unchanged from v1)

```
earth_system_generator.py (engine)
    + scenarios_heatwaves.py (or scenarios_coral_bleaching.py)
    |
    +--> data/<id>_teaser.html     (Plotly 2D map with briefing)
    +--> data/<id>_blockbuster.kmz (Merged single-doc KMZ)
    +--> data/<id>_spikes.kml      (Raw, preserved for desktop)
    +--> data/<id>_heatmap.kml     (Raw, preserved for desktop)
    +--> data/<id>_impact.kml      (Raw, preserved for desktop)
    +--> data/<id>_*.png           (Legends/intel, preserved)
    |
    v
gallery_studio.py (Green preset, KMZ handoff link)
    |
    v
json_converter.py (HTML -> JSON, _kmz_handoff passes through)
    |
    v
Manual moves:
    teaser HTML  --> images/ folder --> gallery studio pipeline
    KMZ file     --> gallery/assets/
    |
    v
index.html (green 3D Earth button, mobile intent URL)
    |
    v
GitHub Pages (tonyquintanilla.github.io)
```


---

## Decision Log

| Question | Decision | Rationale |
|----------|----------|-----------|
| Standalone coral generator vs unified engine? | Unified engine | Prevents divergence, ensures consistent look |
| Refactor order? | Heatwaves first, then coral | Regression test against 27 known-good scenarios |
| Module structure? | Engine + scenario modules | Clean separation of concerns |
| Engine location? | `earth_system_generator.py` | Already has most of the logic |
| Coral generator fate? | Fetch logic reused, rest retired | Engine handles KML/KMZ/Plotly |
| Scenario communication? | Config dict contract | Extensible without forking engine |

---

*"The engine should be centralized and the scenarios connect to it,
whether it's land heating or ocean acidification and coral bleaching
or forest dieoff."* -- Tony, March 18, 2026
