# Paloma's Orrery

An astronomical visualization suite that transforms NASA/JPL/ESA data into
interactive 3D and 2D visualizations of the solar system, the stellar
neighborhood, the Galactic Center, and Earth's climate system.

**See it without installing anything:** [palomasorrery.com](https://palomasorrery.com/)

## About This Project

Paloma's Orrery is a personal tool, built first and foremost for its author's
own exploration and learning. Tony Quintanilla -- a retired civil and
environmental engineer -- develops it through conversational AI collaboration,
and named it for his daughter. The project began in September 2024 and has
grown alongside the AI models that help build it.

It turns out that few people want to run 90,000 lines of Python themselves --
and that's fine. The [web gallery](https://palomasorrery.com/) is how the
project's value reaches everyone else: curated, interactive visualizations in
the browser, no install required. This repository is for the other kind of
reader -- a future development session, an AI collaborator picking up the
project, or the occasional contributor who wants to engage with the mechanics
rather than just the output. This README is written for that reader.

**Philosophy:** Data Preservation is Climate Action. Scientific accuracy
first, visual beauty always.

Created by Tony Quintanilla with assistance from Anthropic Claude, OpenAI
ChatGPT, Google Gemini, and DeepSeek AI assistants.

**Resources:**

- [Web Gallery](https://palomasorrery.com/) -- interactive visualizations in your browser
- [GitHub Repository](https://github.com/tonylquintanilla/palomas_orrery)
- [Instagram: @palomas_orrery](https://www.instagram.com/palomas_orrery/)
- [Video Tutorials](https://www.youtube.com/@tony_quintanilla/featured)
- Contact: <tonyquintanilla@gmail.com>

## Table of Contents

1. [Getting Started](#getting-started)
2. [Python Compatibility and Dependencies](#python-compatibility-and-dependencies)
3. [Repository Organization](#repository-organization)
4. [What It Does](#what-it-does)
5. [Using the Desktop App](#using-the-desktop-app)
6. [Architecture](#architecture)
7. [Earth System Visualization](#earth-system-visualization)
8. [Galactic Center Visualization](#galactic-center-visualization)
9. [Social Media Export](#social-media-export)
10. [Web Gallery](#web-gallery)
11. [Data Files and Caches](#data-files-and-caches)
12. [Data Sources and Provenance](#data-sources-and-provenance)
13. [Contributing](#contributing)
14. [License](#license)
15. [Contact](#contact)

## Getting Started

The active, maintained way to run Paloma's Orrery is from source. The
codebase is cross-platform: Python 3.11-3.13 on Windows, macOS, and Linux
(cross-platform compatibility achieved January 2026).

### 1. Clone the repository

```bash
git clone https://github.com/tonylquintanilla/palomas_orrery.git
cd palomas_orrery
```

### 2. Get the data files -- they are NOT in the repo

The repository contains code and documentation. The large data stores --
stellar catalogs (~300 MB of Gaia/Hipparcos VOTables and PKL caches) and the
orbit path cache (~94 MB) -- are gitignored. Two ways to seed them:

- **From a release:** download the latest release ZIP from the
  [Releases page](https://github.com/tonylquintanilla/palomas_orrery/releases)
  and copy its `data/` and `star_data/` folders into your clone. This gives
  you a fully populated cache out of the box.
- **Through use:** the app fetches and caches data on demand (JPL Horizons
  for orbits, VizieR for stellar catalogs). First plots are slower; the cache
  grows as you explore. See [DATA_INVENTORY.md](DATA_INVENTORY.md) for what a
  mature local data store looks like.

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

On Ubuntu 24.04+/Debian 12+, first install the system Tk packages and add
the PEP 668 flag:

```bash
sudo apt install python3-tk python3-pil.imagetk
pip install -r requirements.txt --break-system-packages
```

(Fedora: `python3-tkinter python3-pillow-tk`. Arch: `tk python-pillow`.
On macOS use `python3`/`pip3`.)

### 4. Run

```bash
python palomas_orrery.py            # main solar system GUI
python palomas_orrery_dashboard.py  # central launcher for all tools
```

First launch may take 30-60 seconds while caches load. Select objects, click
Plot, and the visualization opens in your browser.

Minor cosmetic GUI issues may appear on some Linux window managers (slightly
clipped buttons, text overflow); all functionality works and the
browser-rendered visualizations are unaffected.

### Staying up to date

```bash
git pull
```

That's it -- Python files and documentation update; your local `data/` and
`star_data/` are preserved (they're not in the repo). If you originally
downloaded a ZIP rather than cloning, convert the folder to a git checkout
once:

```bash
git init
git remote add origin https://github.com/tonylquintanilla/palomas_orrery.git
git fetch origin
git reset --hard origin/main
```

Double-click update scripts (`_UPDATE_CODE.bat`, `update_code.sh`,
`update_code.desktop`) and pre-built standalone executables (on the Releases
page) exist but are not the actively maintained path -- the source repo and
the web gallery are.

## Python Compatibility and Dependencies

The short version: **use Python 3.13** (3.11-3.13 supported), and don't
upgrade kaleido. The long version, maintained in full in
[requirements.txt](requirements.txt), is worth knowing:

- **kaleido is pinned at 0.2.1** (exact pin, not a minimum). Kaleido 1.0+
  changed its API: it requires Plotly 6.1.1+ and a separately installed
  Chrome, where 0.2.1 bundles Chromium and just works. The pin holds until a
  deliberate Plotly 6.x migration. Kaleido is used only for static PNG export
  (`social_media_export.py`, `earth_system_generator.py` KML legends) -- the
  web gallery pipeline never touches it and runs entirely in-browser via
  Plotly.js.
- **Plotly stays on 5.x** for kaleido 0.2.1 compatibility. The upgrade path
  (Plotly 6.x + kaleido 1.0+ + `plotly_get_chrome`) is documented in
  requirements.txt for when Python 3.14 becomes necessary or Plotly 5.x
  reaches end of life.
- **Python 3.14 is not yet supported.** kaleido 0.2.1 does not build on it,
  customtkinter (dormant since Feb 2024) uses deprecated patterns likely to
  break, and astropy's 3.14 wheels are still in progress. requirements.txt
  carries the specific GitHub issues to monitor.
- **customtkinter** powers the themed GUI and appears to be an inactive
  project -- a known risk, monitored, with no action needed while on
  Python <= 3.13.

Core stack: numpy, pandas, scipy, astropy, astroquery (JPL Horizons, SIMBAD,
Gaia), plotly, matplotlib, pillow, customtkinter, simplekml (Google Earth
output), requests/beautifulsoup4 (climate APIs), openpyxl/lxml (humanitarian
data spreadsheets).

## Repository Organization

### Layout

```
palomas_orrery/                  # this repo
|- *.py                          # ~121 Python modules, all at root
|- README.md, LICENSE.md         # you are here
|- MODULE_INDEX.md               # what every module does (generated)
|- MODULE_ATLAS.md               # full architecture atlas (generated)
|- LEDGER_CONSOLIDATED.md        # running work ledger and change log
|- PROVENANCE_AUDIT.md           # citation audit (generated)
|- DATA_INVENTORY.md             # local data store inventory
|- ADDING_OBJECTS_GUIDE.md       # how to add a new celestial object
|- requirements.txt              # annotated dependency spec
|- documentation/                # deep-dive docs, design manifests, handoffs,
|                                #   and archived prior README versions
|- skills/                       # versioned AI-collaboration skill files
|- docs/                         # generated architecture pages
|- data/, star_data/             # local data (large files gitignored)
|- reports/                      # generated analysis reports
```

### Key documents for a developer session

| Document | What it's for |
|----------|---------------|
| [MODULE_INDEX.md](MODULE_INDEX.md) | Every module, grouped by role, described from its own docstring. Start here to find where something lives. |
| [MODULE_ATLAS.md](MODULE_ATLAS.md) | The deep version: dependencies, consumers, public functions per module. Built for AI-assisted codebase queries. Both files are regenerated together by `module_atlas.py` -- their counts are the canonical measure of project scale. |
| [LEDGER_CONSOLIDATED.md](LEDGER_CONSOLIDATED.md) | The running ledger: open items, decisions, protocol version history. The project's institutional memory. |
| [ADDING_OBJECTS_GUIDE.md](ADDING_OBJECTS_GUIDE.md) | Step-by-step for adding new celestial objects. |
| [documentation/ORBITAL_MECHANICS_README_v3_3.md](documentation/ORBITAL_MECHANICS_README_v3_3.md) | Orbital mechanics conventions: osculating vs mean elements, solution-level TP, frames, epochs. |
| [PROVENANCE_AUDIT.md](PROVENANCE_AUDIT.md) | Citation audit of every numeric claim in the codebase (see [Data Sources and Provenance](#data-sources-and-provenance)). |
| [documentation/climate_readme.md](documentation/climate_readme.md) | Climate data hub documentation. |
| [documentation/wet_bulb_temperature_readme.md](documentation/wet_bulb_temperature_readme.md) | Forensic heat wave analysis documentation. |
| [documentation/social_media_readme.md](documentation/social_media_readme.md) | 9:16 portrait export documentation. |
| [documentation/web_gallery_handoff.md](documentation/web_gallery_handoff.md) | Web gallery technical documentation. |

The `documentation/` folder also holds design manifests, test protocols, and
session handoffs -- the working papers of the AI-collaboration process. The
`skills/` folder holds versioned skill files that encode project conventions
for AI development sessions.

### Two repositories, siblings on disk

The project spans two public repos, kept as sibling folders in the same
parent directory (not nested):

- **`palomas_orrery`** (this repo) -- the desktop application.
- **[`tonyquintanilla.github.io`](https://github.com/tonyquintanilla/tonyquintanilla.github.io)**
  -- the web gallery: the `index.html` viewer, the published JSON
  visualization data, and the gallery tooling (`tools/gallery_studio.py`,
  `tools/json_converter.py`, `tools/gallery_editor.py`).

GitHub Pages requires its own repository; the split also keeps the app repo
clean. `gallery_studio.py` imports `social_media_export.py` and
`constants_new.py` from the orrery repo by walking up the directory tree --
which is why the sibling layout matters.

## What It Does

**Solar system:**

- Real-time planetary and spacecraft positions from JPL Horizons; 100+
  objects with osculating orbital elements
- Comet visualization with dual dust/ion tails, date-gated disintegration
  states, ghost tail arcs, and fragment tracking (C/2025 K1 breakup with four
  independent trajectories)
- Pluto-Charon true barycentric binary; TNO satellite systems
  (Eris/Dysnomia, Haumea/Hi'iaka/Namaka, Makemake/MK2)
- Planetary and solar interior shells, ring systems, radiation belts;
  seven near-Sun corona shells with optimized two-trace rendering
- Earth orbital infrastructure: GEO belt (42,164 km) and LEO shell; close
  approach visualization via the JPL CAD API (Apophis 2029 passes 4,150 km
  inside the GEO ring)
- Spacecraft Mission Explorer: tagged encounter database with adaptive
  resolution (New Horizons at Jupiter/Pluto/Arrokoth, Artemis II lunar
  closest approach); two-layer trajectory rendering (full mission + plotted
  period)
- Lagrange points, apsidal markers, exoplanet systems (TRAPPIST-1, TOI-1338,
  Kepler-16 with binary star mechanics)
- Animation system with static shell optimization; unified save system
  (CDN ~10 KB / offline ~5 MB HTML, PNG)
- Object Encyclopedia: reference info cards embedded in every HTML export,
  sourced from `info_dictionary.py`

**Stellar and galactic:**

- Stellar neighborhood mapping: 123,000+ stars from combined Gaia DR3 and
  Hipparcos catalogs; HR diagrams; 3D star maps
- Galactic Center: S-stars orbiting Sagittarius A* with Schwarzschild
  precession (Newton vs Einstein comparison), phases from real GRAVITY
  Collaboration periapsis measurements

**Earth system:**

- Climate data preservation hub: CO2 (Mauna Loa), temperature (NASA GISS),
  Arctic sea ice (NSIDC), sea level (NOAA), ocean pH
- Paleoclimate records spanning 540 million years
- Forensic Heat Wave Analysis: 3D KML layers for Google Earth Pro
  visualizing wet-bulb temperature extremes, 1948 to present

**Publishing:**

- Web gallery at [palomasorrery.com](https://palomasorrery.com/)
- Social media export: 9:16 portrait HTML for Instagram Reels and YouTube
  Shorts

## Using the Desktop App

The main GUI (`palomas_orrery.py`) works checkbox-first: select objects,
set a date range and center body, click Plot for a static visualization or
use the animation controls for time evolution. Plots open in the browser;
a save dialog offers CDN HTML, offline HTML, or PNG.

Center-body options include heliocentric, barycentric, any planet, the
Pluto-Charon barycenter, and TNO-centered views. Spacecraft trajectories
render in two layers (full mission plus the plotted period). Shell
checkboxes toggle planetary interiors, atmospheres, rings, and the solar
corona layers.

Other entry points:

```bash
python palomas_orrery_dashboard.py     # central launcher, live output
python star_visualization_gui.py       # stellar neighborhood and HR diagrams
python earth_system_visualization_gui.py  # climate data hub
python sgr_a_grand_tour.py             # Galactic Center dashboard
```

Windows users can also double-click `START_HERE.bat` or `_run_dashboard.bat`.

## Architecture

### Design philosophy

- **Accuracy first:** established astronomical methods throughout
- **Visual clarity:** complex data presented intuitively
- **Offline capability:** works without internet once caches are seeded
- **Cross-platform:** Windows, macOS, Linux

### Data pipeline

1. **Acquisition:** JPL Horizons, VizieR, SIMBAD, climate APIs
2. **Caching:** local storage with validation, atomic saves, and backups
3. **Processing:** coordinate transforms, orbital calculations
4. **Visualization:** interactive Plotly HTML
5. **Export:** CDN or offline HTML, PNG, 9:16 social view, KML/KMZ
6. **Gallery:** JSON extraction, GitHub Pages deployment at palomasorrery.com

Position data flows through five parallel pipelines (static plot, animation,
social export, gallery curation, JSON conversion) -- a change to something
like hover text can touch all five, each with its own path. This is the
project's central maintenance discipline: fixes must be checked across every
consumer.

### Development complexity

Paloma's Orrery is not enterprise software. Commercial codebases are orders
of magnitude larger, maintained by teams of hundreds over decades. But for a
project built by a single developer without formal CS training, using
conversational AI collaboration, the system has grown to a scale worth
noting: 121 Python modules and roughly 92,000 non-blank lines as of July
2026 ([MODULE_ATLAS.md](MODULE_ATLAS.md) carries the authoritative current
counts -- it's regenerated mechanically, so trust it over any number
hardcoded here), five parallel position pipelines, 1,000+ cached orbital
trajectories across multiple center bodies, and a full publishing pipeline
from desktop app through curation studio to browser gallery.

The domain punishes plausible-looking errors: an orbit plotted in the
equatorial frame when the data is ecliptic appears rotated by 23.4 degrees,
and nothing errors out. The system handles osculating elements,
Schwarzschild precession, binary mass ratios, and the distinction between
ephemeris data, calculated Keplerian elements, and cached approximations.
Visual verification catches physics errors that code review misses.

What makes it interesting is the complexity-to-team-size ratio. This is the
kind of system that would traditionally need a small team of specialists.
Conversational AI collaboration compresses that: the developer provides
vision, domain knowledge, and judgment; AI partners handle implementation,
pattern recognition, and documentation. The conversation is the development
environment, and accumulated context across months of sessions shapes every
decision.

## Earth System Visualization

Access the Earth System Hub from the main interface:

**Current monitoring (1958-present):** atmospheric CO2 (Mauna Loa),
global temperature anomalies (NASA GISS), Arctic sea ice extent (NSIDC),
global mean sea level (NOAA).

**Paleoclimate records:** 800,000-year ice core CO2 (EPICA Dome C),
5-million-year benthic stack (LR04), 12,000-year Holocene reconstruction
(Temp12k), 540-million-year Phanerozoic temperatures.

**Forensic Heat Wave Analysis:** `earth_system_generator.py` produces 3D
KML layers (Spikes, Heatmap, Impact) for
[Google Earth Pro](https://www.google.com/earth/versions/#earth-pro)
(free desktop app, required for viewing), covering 27+ historical and
modern events from NYC 1948 to the Western Heat Dome of March 2026. The
metric is wet-bulb temperature against biological limits (31 degC). See
[documentation/wet_bulb_temperature_readme.md](documentation/wet_bulb_temperature_readme.md).

Full climate documentation:
[documentation/climate_readme.md](documentation/climate_readme.md).

## Galactic Center Visualization

The Galactic Center modules visualize S-stars orbiting Sagittarius A*:
S2, S62, S4711, and S4714 -- the stars with the most extreme known orbits.
General relativity precesses their orbits into rosette patterns; the
visualizations compare Newtonian and Einsteinian predictions, with orbital
phases calculated from actual GRAVITY Collaboration periapsis measurements.

| Module | Purpose |
|--------|---------|
| `sgr_a_star_data.py` | S-star catalog: orbital parameters and physical properties |
| `sgr_a_visualization_core.py` | Static orbit visualization |
| `sgr_a_visualization_animation.py` | Animated motion (Kepler's Second Law) |
| `sgr_a_visualization_precession.py` | Schwarzschild precession, Newton vs Einstein |
| `sgr_a_grand_tour.py` | Complete dashboard with mode switching and zoom |

Each module runs standalone: `python sgr_a_grand_tour.py`.

## Social Media Export

Export any visualization as a 9:16 portrait HTML file for Instagram Reels
and YouTube Shorts. The social view splits the screen into a 3D scene (top
60%) and a persistent info panel (bottom 40%) showing the data normally
hidden in hover tooltips. Click **Social Media Export** in the GUI, choose
objects and a save location, then record the browser at 1080x1920 -- the
layout is locked to 9:16 with invisible margins, no cropping needed.
Animation playback, camera preservation, and trace selection are supported.

See [documentation/social_media_readme.md](documentation/social_media_readme.md).

## Web Gallery

Browse interactive visualizations at
[palomasorrery.com](https://palomasorrery.com/) -- no download, no install,
no Python. Tap a link and explore.

**How it works:** the desktop app exports visualizations as HTML. A
converter extracts the Plotly figure data into lightweight JSON files. The
gallery viewer -- a single-page HTML/CSS/JS app hosted on GitHub Pages --
loads them with Plotly.js from CDN. Every visualization gets its own direct
link (e.g., `palomasorrery.com/#earth-birthday-2025`).

**Features:** dark space theme matching the desktop aesthetic; desktop
(landscape) and mobile (portrait) modes with auto-detection;
category-grouped navigation; floating info cards and 3D zoom buttons on
mobile; fly-to buttons for curated close-up views; pan/zoom D-pad with
reset; custom domain with HTTPS.

**Pipeline:**

```
Desktop App -> save_plot() -> HTML export
    -> gallery_studio.py -> per-plot curation (optional)
    -> json_converter.py -> JSON + gallery_metadata.json
    -> gallery_editor.py -> titles, categories, ordering
    -> GitHub Pages (index.html) -> palomasorrery.com
```

The tools live in the website repo's `tools/` folder; `gallery_config.json`
is the single source of truth for category definitions across all of them.
See [documentation/web_gallery_handoff.md](documentation/web_gallery_handoff.md)
for the full technical documentation.

## Data Files and Caches

The large data stores are local and gitignored -- generated through use or
seeded from a release. [DATA_INVENTORY.md](DATA_INVENTORY.md) tracks the
live local state; approximate scale:

| Store | Contents | Size |
|-------|----------|------|
| `star_data/` | Gaia/Hipparcos VOTables, star property PKLs (123,000+ stars) | ~330 MB |
| `data/orbit_paths.json` | Time-indexed positions, 1,000+ objects, multiple frames | ~94 MB |
| `data/osculating_cache.json` | JPL Horizons orbital elements, epoch-tracked, center-body aware keys | <1 MB |
| `data/close_approach_cache.json` | JPL CAD flyby data | <1 MB |
| `data/` (climate) | CO2, temperature, ice, sea level, ocean pH, paleoclimate | ~35 MB |
| `data/` (heat wave) | ERA5 weather caches, generated KML/KMZ layers | ~175 MB |

Cache safety is a first-class concern: automatic backups on startup, atomic
saves, and a size-reduction check that blocks any save that would shrink a
cache (a symptom of data loss, not of a smaller dataset).

Small configuration files (`orrery_config.json`, `window_config.json`,
`satellite_ephemerides.json`, cache metadata) and generated reports
(`reports/`) live alongside the caches.

## Data Sources and Provenance

**Sources:** JPL Horizons (planetary and spacecraft ephemerides), ESA Gaia
DR3 and Hipparcos via VizieR (stellar catalogs), SIMBAD (object
identification), GRAVITY Collaboration (S-star orbits), Scripps CO2
Program, NASA GISS, NSIDC, NOAA, Copernicus/ERA5, BCO-DMO (climate and
ocean data), SOHO/LASCO (coronal observations).

**Citation discipline:** every numeric claim in the codebase -- constants,
data dictionaries, display strings -- is audited for provenance. A scanner
(`provenance_scanner.py`) classifies each value by vulnerability (fetched
from an authoritative pipeline, cited to a source, stale, or recalled
without citation) and criticality (from cosmetic to public-facing to
propagating), and the project maintains a standing gate: no push while any
finding sits in the highest-risk tier. Values that cannot be sourced are
removed and the gap noted, rather than cited loosely. The current audit is
[PROVENANCE_AUDIT.md](PROVENANCE_AUDIT.md).

## Contributing

This project is maintained by a single developer but welcomes community
input. Areas of interest: additional spacecraft mission data, solar system
structure visualizations, stellar classification improvements, exoplanet
systems, performance optimization, cross-platform testing, documentation,
and climate data integration.

Suggestions are welcome: <tonyquintanilla@gmail.com>. For bug reports,
include your Python version, steps to reproduce, and any error messages.

## License

MIT License

Copyright (c) 2025-2026 Tony Quintanilla

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Contact

**Author:** Tony Quintanilla
**Email:** <tonyquintanilla@gmail.com>
**GitHub:** [github.com/tonylquintanilla/palomas_orrery](https://github.com/tonylquintanilla/palomas_orrery)
**Website:** [palomasorrery.com](https://palomasorrery.com/)
**Instagram:** [@palomas_orrery](https://www.instagram.com/palomas_orrery/)
**YouTube:** [Paloma's Orrery](https://www.youtube.com/@tony_quintanilla/featured)

**Last Updated:** July 2026 (developer-focused README rewrite; documentation
reorganization into `documentation/`; generated MODULE_INDEX/MODULE_ATLAS
tooling; provenance audit refresh; continued gallery pipeline development.
Prior milestone: v2.9.0, May 2026 -- Object Encyclopedia in all HTML output,
MAPS disintegration visualization, solar shell optimization, C/2025 K1
fragment tracking, Artemis II mission, dashboard launcher)

---

**Acknowledgments:**

- [NASA JPL Horizons System](https://ssd.jpl.nasa.gov/horizons/) for planetary ephemerides
- [ESA Gaia Mission](https://www.cosmos.esa.int/web/gaia) for stellar data
- [VizieR catalog service](https://vizier.cds.unistra.fr/) (CDS, Strasbourg)
- [SIMBAD astronomical database](https://simbad.u-strasbg.fr/simbad/)
- [Scripps CO2 Program](https://scrippsco2.ucsd.edu/) for Mauna Loa data
- [Copernicus Climate Data Store](https://cds.climate.copernicus.eu/) for ERA5 reanalysis data
- [SOHO/LASCO](https://soho.nascom.nasa.gov/) coronagraph observations (ESA/NASA)
- [GRAVITY Collaboration](https://www.mpe.mpg.de/ir/gravity) for S-star orbital data
- [Astropy](https://www.astropy.org/) and [Astroquery](https://astroquery.readthedocs.io/) development teams
- [Plotly](https://plotly.com/) visualization library
- AI coding assistants: [Anthropic Claude](https://www.anthropic.com/claude), [OpenAI ChatGPT](https://openai.com/chatgpt), [Google Gemini](https://gemini.google.com/)
- Cross-platform compatibility (Windows, macOS & Linux) achieved January 2026
- README updated: July 2026 with Anthropic's Claude Fable 5
