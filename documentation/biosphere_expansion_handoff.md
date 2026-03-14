# Paloma's Orrery -- Biosphere Expansion & Handoff Pipeline

## Session Handoff | February 28, 2026 | Claude Opus 4.6 + Gemini

*Original draft by Gemini. Updated by Claude with fixes and findings from Session 20.*

---

## The Vision & The Conflict

The goal is to expand Paloma's Orrery to visualize Earth Systems and the
Stockholm Resilience Centre (SRC) Planetary Boundaries (Extreme Heat,
Coral Bleaching, Forest Cover) using the forensic 3D "Black Spikes"
aesthetic.

**The Architectural Conflict:** The Web Gallery Initiative's golden rule
is "No download, no install, runs entirely in the browser using
Plotly.js." However, rendering planetary-scale forensic data (tens of
thousands of 3D polygons, heatmaps, and population circles) instantly
crashes mobile web browsers.


## The Solution: The "Teaser & Blockbuster" Pattern

We bifurcated the pipeline. A single Python generator now outputs two
distinct artifacts per scenario:

**The Teaser (Plotly JSON):** A highly optimized, down-sampled 2D
interactive map. Loads instantly in index.html, respects all Gallery
Studio curation, and provides the narrative hook. Now includes briefing
text and a hint directing users to the 3D Earth button.

**The Blockbuster (KMZ File):** The raw, millions-of-rows dataset
packaged into a hardware-accelerated 3D environment. Users access this
voluntarily via a green "3D Earth" floating button embedded in the web
gallery. All KML layers are merged into a single `doc.kml` with
toggleable folders in Google Earth's layer panel.


## Phase 1: The Coral Blueprint (Proof of Concept)

Completed previously.

Built `biosphere_coral_generator.py` integrating NOAA CoastWatch ERDDAP
data. Validated that using Python's `zipfile` to compress KMLs into a
single `.kmz` archive crushes file sizes (e.g., 13,500 polygons down to
~500 KB), making them highly optimized for web delivery.


## Phase 2: Retrofitting the Extreme Heatwaves

Before expanding into new biosphere data, we executed a strategic pause
to retrofit the existing 27 Extreme Heatwave scenarios into the new
pipeline.


### 1. Repository Standardization

Defined strict asset paths across the two repositories:

**The Kitchen (Orrery Repo):** `earth_system_generator.py` outputs
the bundled `.kmz` and `.html` teaser into the local `data/` folder.
Raw KML/PNG files are preserved here for the desktop Python orrery.

**The Dining Room (Gallery Repo):** The finished `.kmz` files must
be manually moved to `gallery/assets/` so they can be referenced via
the correct relative path (`gallery/assets/`).

**CRITICAL PATH LESSON (Session 20):** `index.html` is served from
the repository root (`palomasorrery.com/`). The JavaScript builds a
relative path as `assets/<filename>`, which the browser resolves as
`palomasorrery.com/assets/` -- a 404. The KMZ files live at
`palomasorrery.com/gallery/assets/`. Fix: the JS path must be
`gallery/assets/<filename>`, not just `assets/<filename>`.


### 2. The Generator Overhaul (earth_system_generator.py)

Upgraded the heatwave generator from a "Local Asset Creator" to a
"Web Asset Factory":

**Plotly Integration:** Added `generate_plotly_teaser()` to build a
2D mapbox map using the ERA5 cache. Now includes `briefing` and
`description` parameters. Renders the first paragraph of the
briefing as a bottom-left annotation (200 char max, semi-transparent
background, white text) plus a hint: "Click 3D Earth for full
visualization in Google Earth."

**The Packager:** `package_and_cleanup()` now implements a merged
KML approach. Instead of writing multiple separate KML files into
the KMZ (which caused Google Earth to only load the first one), it:

1. Reads all KML files
2. Extracts `<Document>` body from each using regex
3. Wraps each body in a `<Folder>` with the layer name (Spikes,
   Heatmap, Impact)
4. Generates a single `doc.kml` containing all folders
5. Writes only `doc.kml` + PNG assets to the KMZ

Result: single-document KMZ with toggleable folders in Google
Earth's layer panel.

**No-Delete Policy (Session 20 fix):** The original "Janitor" logic
deleted raw KML/PNG files after packaging into KMZ. This made them
unavailable for the desktop Python orrery. Fix: removed `os.remove()`
loop. KMZ and raw files now coexist in `data/`. Added `import re`
for the KML merge regex.


### 3. Wiring the Web Bridge

Successfully bridged the Studio tools and the Web Gallery.

**gallery_studio.py:** Added a "3D Handoff (Google Earth)" text
entry field. The tool saves the KMZ filename and injects
`layout['_kmz_handoff']` into the exported JSON payload.

**Underscore Survival (Session 20 fix):** `gallery_studio.py` strips
all underscore-prefixed keys from Plotly JSON at three locations
(lines 1628, 2386, 3954). This killed `_kmz_handoff` before it
reached the exported HTML. Gemini recommended dropping the
underscore; we instead whitelisted `_kmz_handoff` through all three
filters, following the existing `_encyclopedia` pattern. This
preserves the convention that underscore marks non-Plotly keys and
avoids Plotly.js console warnings.

**index.html:** The green "3D Earth" floating button dynamically
appears when `figDict.layout._kmz_handoff` is detected. Session 20
fixes:

- **Button positioning:** Moved Share and 3D Earth buttons from
  `right: 12px` (which obscured the Plotly legend/colorbar) to
  `left: 62px` (just right of hamburger menu).

- **Mapbox zoom controls:** Zoom buttons appeared but didn't work
  on mapbox plots because `zoom2D()` operates on xaxis/yaxis
  ranges, not `mapbox.zoom`. Fix: detect `figDict.layout.mapbox`
  and hide zoom controls entirely (mapbox has built-in
  scroll/pinch zoom).

- **Mobile intent URL:** Desktop gets a standard download link.
  Mobile devices get `googleearth://url=<absoluteURL>` which
  prompts the OS to open Google Earth directly. Still needs
  real-device testing.

- **KMZ path fix:** Changed relative path from `assets/` to
  `gallery/assets/` to match actual file location relative to
  the page served from root.

**_gitattributes:** Added explicit binary markers to prevent Git's
`* text=auto` from corrupting binary KMZ files:

```
*.kmz binary
*.kml binary
*.png binary
```


## Workflow Summary

```
earth_system_generator.py
    |
    +--> data/<id>_teaser.html     (Plotly 2D map with briefing)
    +--> data/<id>_blockbuster.kmz (Merged single-doc KMZ)
    +--> data/<id>_spikes.kml      (Raw, preserved for desktop)
    +--> data/<id>_heatmap.kml     (Raw, preserved for desktop)
    +--> data/<id>_impact.kml      (Raw, preserved for desktop)
    +--> data/<id>_*.png           (Legends/intel, preserved)
    |
    v
gallery_studio.py (apply Green preset, set KMZ handoff link)
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


## Files Modified (Session 20)

| File | Changes |
|------|---------|
| `index.html` (~2,200 lines) | Button positioning (left: 62px), mapbox zoom detection, KMZ path fix (gallery/assets/), mobile intent URL |
| `earth_system_generator.py` (~850 lines) | Briefing annotation in teaser, no-delete policy, merged KML approach in package_and_cleanup(), added `import re` |
| `gallery_studio.py` (~4,500 lines) | Whitelisted `_kmz_handoff` through three underscore filters |
| `_gitattributes` | Binary markers for KMZ/KML/PNG |


## KMZ Structure

Before (broken): 7 files (3 KMLs + 4 PNGs). Google Earth only
loaded the first KML.

After (working): 5 files (1 merged `doc.kml` + 4 PNGs). All layers
appear as toggleable folders in Google Earth's layer panel.


## Next Steps & Decisions

### Step 1: Batch Process & Deployment

Run `earth_system_generator.py` to batch-convert the remaining 26
heatwave scenarios into Teasers and Blockbusters. Process the Teasers
through `gallery_studio.py` (applying the "Green" dark-mode preset)
and assign their corresponding KMZ links. Run `json_converter.py`
and push the updated `gallery/` and `gallery/assets/` folders to
GitHub.

### Step 2: Mobile UX Testing

Once the button is live on GitHub Pages, test the OS intercept on
iOS Safari and Android Chrome. The `googleearth://url=` intent
scheme should prompt the mobile OS to open the Google Earth app
directly. If iOS Safari stubbornly downloads to the Files app, we
may need a UI tooltip instructing iOS users, or investigate whether
the intent URL requires Google Earth to be pre-installed.

### Step 3: Expand the Boundaries

With the Heatwave pipeline modernized and serving as the gold
standard, resume building generators for the remaining planetary
boundaries. Next target: Land-System Change (Forest Cover / Amazon
Tipping Point) using Global Forest Watch data.


## Technical Lessons Learned

- **Single KML per KMZ:** Google Earth only reliably reads the first
  KML in a multi-file KMZ. NetworkLink wrappers inside KMZ don't
  resolve relative paths. Solution: merge all KML content into one
  `doc.kml` with `<Folder>` elements per layer.

- **Underscore keys in Plotly:** `gallery_studio.py` strips
  underscore-prefixed layout keys to avoid polluting Plotly JSON.
  Custom keys like `_kmz_handoff` must be explicitly whitelisted,
  following the `_encyclopedia` pattern.

- **Preserve raw files:** Desktop orrery needs the raw KML/PNG
  files in `data/`. Never delete source files after KMZ packaging.

- **Relative paths from root:** When `index.html` is served from
  the repository root, all asset paths must include the full
  subdirectory path (`gallery/assets/`), not just the relative
  path from the gallery folder.

- **Git binary markers:** Without explicit binary markers in
  `.gitattributes`, Git's `text=auto` can corrupt KMZ files
  (which are ZIP archives).

- **Mapbox != standard 2D:** Plotly mapbox plots use a completely
  different zoom/pan API from standard 2D axes. Zoom controls
  built for xaxis/yaxis ranges won't work -- either adapt to
  `mapbox.zoom` or hide controls (mapbox has native touch zoom).


---

| Question | Decision | Rationale |
|----------|----------|-----------|
| Delete raw files after KMZ? | No | Desktop orrery needs them in data/ |
| Underscore convention | Keep `_kmz_handoff`, whitelist | Consistent with `_encyclopedia` pattern |
| Button position | Left side (left: 62px) | Right side obscures legend/colorbar |
| Multi-KML in KMZ | Merge into single doc.kml | Google Earth only loads first KML file |
| Mobile KMZ handoff | googleearth:// intent URL | Direct app launch vs download-to-Files |
| KMZ path in JS | gallery/assets/ | index.html served from root, not gallery/ |

---

*"I am more comfortable working with you."* -- Tony, on bringing
Gemini's fixes to Claude for implementation, February 28

*"Data Preservation is Climate Action. Sharing is Astronomy Action."*
