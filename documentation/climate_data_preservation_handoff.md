# Climate Data Preservation Handoff
## February 18, 2026

---

## Context

US federal science agencies (NOAA, NASA, NSF-funded institutions like NCAR)
face potential disruption of data access under current administration policies.
Paloma's Orrery already caches climate data locally as part of its Earth
System Visualization module. This session's goal: expand cached datasets to
cover critical gaps before access may be restricted.

**Philosophy:** Data Preservation is Climate Action. Cached data serves as
insurance against potential future restrictions or defunding of scientific
data services.

---

## Completed This Session: Gallery Pipeline Improvements

### Problem

Gallery Studio exports standalone HTML with interactive controls (annotation
toggle button, pan/zoom nav arrows) embedded in the HTML wrapper. But
`json_converter.py` extracts only Plotly `data` and `layout`, discarding
the wrapper. The gallery viewer (`index.html`) never saw these controls.
Two features affected:

1. **Annotation toggle** -- "Show Labels / Hide Labels" button for toggling
   dense annotations on mobile-friendly views
2. **Nav controls** -- Pan/zoom D-pad arrows selected in Studio's Chrome
   section appeared in preview but disappeared in the gallery

### Solution

Bridged the pipeline gap: `json_converter.py` now detects both features
in the source HTML and preserves signals in the JSON output that the
gallery viewer already knows how to read. Added the annotation toggle
button to the gallery viewer as a new interactive control.

### Files Changed

| File | What Changed |
|------|-------------|
| `gallery_studio.py` | New `annotation_toggle_button` config option. When enabled, processed annotations are preserved in `layout['_toggle_annotations']` even if `show_annotations` is False. Button CSS/HTML/JS injected into standalone HTML exports via `build_gallery_html()`. New "Embed toggle button" checkbox in Annotations GUI section. Also: `_parse_hover_html` moved in from `social_media_export.py`, eliminating cross-directory import dependency. |
| `json_converter.py` | New `_extract_toggle_annotations()` function finds `var _annStored = [...]` in source HTML using bracket-matching. Saves as top-level `toggle_annotations` key in gallery JSON output. Also detects studio nav controls (`class="nav-controls"` + `function panPlot`) and sets `layout._studio_nav = true` in JSON so the gallery viewer shows pan/zoom arrows instead of simple zoom buttons. |
| `index.html` | CSS for `.ann-toggle` button matching existing gallery control styling (backdrop blur, border, transitions). Button HTML between zoom controls and pan controls. JS: `doToggleAnnotations()` using `Plotly.relayout()` to swap annotations. Uses `touchstart` + `mousedown` (same pattern as zoom/pan) for iOS WebGL compatibility. Button state resets on viz load and home navigation. On mobile (<=1024px), button moves into toolbar via JS (same pattern as nav/share buttons) to avoid overlap. |

### How It Works

**Annotation toggle:**
1. In Gallery Studio, check "Embed toggle button" in the Annotations section
2. Export HTML -- the button and stored annotations are embedded
3. Run `json_converter.py` -- extracts `toggle_annotations` into the JSON
4. Gallery viewer detects the key and shows the button
5. Viewer taps to toggle -- `Plotly.relayout()` swaps annotations on/off

**Nav controls (pan/zoom arrows):**
1. In Gallery Studio, check "Show nav arrows" in the Chrome section
2. Export HTML -- pan/zoom D-pad is embedded in the HTML wrapper
3. Run `json_converter.py` -- detects nav controls in HTML, sets
   `layout._studio_nav = true` in the JSON
4. Gallery viewer reads the flag and shows pan/zoom D-pad instead of
   simple +/- zoom buttons

### Pipeline Pattern

Both features follow the same pipeline bridge pattern:

```
Gallery Studio (HTML wrapper) -> json_converter (detects & preserves) -> index.html (reads & renders)
```

The standalone HTML embeds controls directly. The converter detects
them in the source HTML and signals the gallery viewer via JSON keys.
The viewer already had the rendering code -- it just needed the signal.

### Design Decisions

- Toggle button position: `top: 94px; right: 12px` on desktop (below
  share button). On mobile, moves into toolbar flex row between nav
  and share buttons.
- Initial annotation state respects `show_annotations` setting -- can
  start hidden (phone-first) or visible (desktop-first)
- Annotations are processed (footer strip, transparency, font scaling)
  before being stored, so toggle shows the curated version
- `_toggle_annotations` uses underscore prefix convention so it gets
  stripped from Plotly layout serialization but survives in the pipeline
- Nav detection uses content signatures (`class="nav-controls"` +
  `function panPlot`) rather than config file lookup -- more robust,
  works even if config is missing

### Testing

Verified on: desktop browser (landscape), iPhone Safari, iPhone Chrome,
iPhone Home Screen (PWA mode). The toolbar flow prevents overlap on all
mobile configurations. Nav controls verified in standalone HTML preview
and gallery viewer after re-running json_converter.

---

## What We Already Have

The project caches these datasets in `data/` as JSON files:

| Dataset | Source | File | Status |
|---------|--------|------|--------|
| CO2 monthly | NOAA GML (Mauna Loa/Scripps) | co2_mauna_loa_monthly.json | Cached |
| Global temperature | NASA GISS | temperature_giss_monthly.json | Cached |
| Arctic sea ice extent | NSIDC | arctic_ice_extent_monthly.json | Cached |
| Sea level (GMSL) | NASA | sea_level_gmsl_monthly.json | Cached |
| Ocean pH | BCO-DMO/HOT | ocean_ph_hot_monthly.json | Cached |
| Paleoclimate LR04 | Lisiecki & Raymo | paleoclimate data | Cached |
| EPICA CO2 | ice core | paleoclimate data | Cached |

Fetch code is in:
- `/mnt/project/fetch_climate_data.py` -- current monitoring data
- `/mnt/project/fetch_paleoclimate_data.py` -- ice core / deep time data
- `/mnt/project/climate_cache_manager.py` -- cache validation and backup
- `/mnt/project/energy_imbalance.py` -- may have ocean heat content logic

Visualization code:
- `/mnt/project/earth_system_visualization_gui.py` -- main Earth System hub
- `/mnt/project/earth_system_controller.py` -- coordinates visualizations
- `/mnt/project/earth_system_generator.py` -- generates plots
- `/mnt/project/paleoclimate_visualization.py` -- deep time plots
- `/mnt/project/paleoclimate_visualization_full.py` -- extended paleo
- `/mnt/project/paleoclimate_wet_bulb_full.py` -- wet bulb analysis
- `/mnt/project/paleoclimate_human_origins_full.py` -- human origins overlay
- `/mnt/project/paleoclimate_dual_scale.py` -- dual axis paleo plots

Gallery pipeline:
- `/mnt/project/gallery_studio.py` -- interactive HTML export tool
- `/mnt/project/json_converter.py` -- HTML to gallery JSON converter
- `/mnt/project/index.html` -- gallery viewer (GitHub Pages)

---

## What We Need to Add

### Priority 1: Methane (CH4) -- Monthly Global Average

**Why:** Second most important greenhouse gas. Politically contentious.
NOAA GML hosts it in the same format as CO2.

**Source:** NOAA Global Monitoring Laboratory
- URL: `https://gml.noaa.gov/webdata/ccgg/trends/ch4/ch4_mm_gl.txt`
- Format: Text file, same structure as CO2 (comment lines starting with #,
  then year/month/value columns)

**Output:** `data/ch4_global_monthly.json`

**Pattern to follow:** `fetch_climate_data.py` already fetches CO2 from the
same NOAA GML server. The methane fetch should mirror that pattern exactly --
same error handling, same JSON output structure, same cache validation.

### Priority 2: Ocean Heat Content

**Why:** The real energy imbalance metric. Oceans absorb 90%+ of excess
heat. Shows the warming signal with less noise than surface temperature.

**Source:** NOAA NCEI (National Centers for Environmental Information)
- URL: `https://www.ncei.noaa.gov/access/global-ocean-heat-content/`
- Data: Ocean heat content anomaly, 0-700m and 0-2000m depth
- Format: May require checking -- could be text, CSV, or NetCDF
- Alternative: Cheng et al. (IAP) dataset at
  `http://www.ocean.iap.ac.cn/pages/dataService/dataService.html`

**Output:** `data/ocean_heat_content_monthly.json`

**Note:** Check `energy_imbalance.py` first -- there may already be partial
logic for this. If so, extend rather than duplicate.

---

## Secondary Targets (if time permits)

| Dataset | Source | Why |
|---------|--------|-----|
| Antarctic ice extent | NSIDC | Complete the picture (we only have Arctic) |
| EPICA deuterium (temp proxy) | Ice core | Pairs with existing EPICA CO2 |
| Vostok ice core | 420K years CO2+temp | Classic deep time dataset |
| CO2 daily (Keeling Curve) | NOAA GML | Seasonal biosphere breathing |
| GRACE ice mass | NASA | Greenland/Antarctic ice sheet loss |

---

## Implementation Approach

1. **Check existing code first** -- read `fetch_climate_data.py` and
   `energy_imbalance.py` to understand current patterns
2. **Methane first** -- simplest, mirrors existing CO2 fetch exactly
3. **Ocean heat content second** -- may need more investigation for
   the right data format and URL
4. **Add to Earth System visualization** -- new plot types for methane
   and ocean heat content in the existing GUI
5. **Cache and validate** -- same pattern as existing climate cache manager
6. **Gallery-ready** -- save HTML via `show_and_save`, curate in Studio
   with annotation toggle enabled for mobile-friendly viewing

### Code Patterns

All climate fetch functions follow this pattern:
```python
def fetch_DATASET():
    """Fetch DATASET from SOURCE."""
    url = "https://..."
    cache_file = "data/DATASET.json"

    # Check cache first
    if os.path.exists(cache_file):
        # Return cached if recent enough
        ...

    # Fetch from source
    response = requests.get(url)
    # Parse text/CSV format
    # Convert to JSON structure: {dates: [...], values: [...], metadata: {...}}
    # Save to cache file
    # Return data
```

### Visualization Patterns

Earth System plots use Plotly with the existing generator pattern:
```python
# In earth_system_generator.py
def generate_DATASET_plot():
    data = fetch_DATASET()
    fig = go.Figure()
    fig.add_trace(go.Scatter(...))
    # Standard formatting
    return fig
```

---

## Technical Notes

- **ASCII only** in Python files (no Unicode symbols)
- **LF line endings** preferred
- Climate data URLs may change -- document the source URL in comments
- JSON cache structure should include metadata (source URL, fetch date,
  units, description) for provenance
- Test that fetch works before building visualization
- The `show_and_save` function in `save_utils.py` handles HTML export
  for gallery pipeline
- Use "Embed toggle button" in Gallery Studio for climate plots with
  dense annotations -- lets phone users toggle labels on demand

---

## Urgency Note

NCAR is being restructured. NOAA GML data access could change. NASA GISS
has been targeted before. The data itself is scientifically irreplaceable
in terms of continuity -- these are decades-long measurement records.
Cache now, visualize after.

---

*"Data Preservation is Climate Action."* -- Paloma's Orrery project principle
