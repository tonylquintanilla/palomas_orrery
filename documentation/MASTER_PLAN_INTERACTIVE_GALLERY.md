# MASTER PLAN: Paloma's Orrery Interactive Gallery

**Status:** Draft v9 — Phase 0 proven; data serving framed.
**Base:** orrery @ `6368c87`, gallery @ `a85a4fa`
**Date begun:** July 3, 2026
**Last updated:** July 6, 2026
**Participants:** Tony Quintanilla, Claude Opus 4.6, Claude Opus 4.8, Claude Fable 5

**Pivot (v8):** The gallery is no longer a stepping stone to a separate web
application. The gallery IS the web publication — growing interactive
controls incrementally, like a science museum adding hands-on exhibits to a
permanent collection.

---

## §1 — Architectural Constraints (settled)

These are not options. They are facts that constrain every downstream decision.

**The site never fetches Horizons.** JPL terms require one request at a time and
prohibit website embedding (NASA CORS policy). The cache is the entire served
surface.

**Three-tier cache, all offline-populated (orrery domain):**

- Tier 1 — Scheduled standard catalog. Sequential batch job refreshes a fixed
  set of object/center pairs, rolling the date window forward. Size-stable.
- Tier 2 — Curated specials, define-once. Encounters, perihelia, close
  approaches. Write-once/read-forever. Fetched by Tony via the desktop app.
- Tier 3 — User requests, manually curated. Tony produces and caches offline;
  the user is notified when ready. Whether fulfilled requests persist in the
  shared cache is a dial Tony sets (see §7).

**The gallery is the delivery platform.** The existing gallery on GitHub Pages
(`tonyquintanilla.github.io`) is a working static site that already renders
Plotly 3D figures on every device including phones. It has navigation,
narrative sections, categories, and a curator's workflow (Gallery Studio). The
web publication extends this — it does not replace it.

**The JSON bridge.** Pre-curated gallery cards and interactive gallery pages both
produce the same artifact: Plotly JSON. One path is pre-baked by Tony on the
desktop, shipped as a `.json` file. The other path is assembled live in the
browser from user selections via Pyodide. The gallery viewer renders both
identically. This is the unifying architectural principle.

**The GUI declares the envelope.** A cache miss is something the UI will not let
you request — not a runtime error, not a silent wrong plot. Coverage is a
visible, honest boundary. The coverage index tells the interactive page which
combinations are available; the page shows only those options.

**Pyodide for client-side computation.** When a user selects planets and dates
and the assembler runs, it runs in their browser via Pyodide (Python compiled
to WebAssembly). No server. The gallery stays a static site on GitHub Pages.
Pyodide loads from CDN, the assembler and orbit cache are static files in the
repo. If Phase 0 reveals Pyodide is unacceptable (cold-start too slow, package
too large), the fallback path is a pre-computed library only — a bigger menu,
no runtime computation on the web.

**Assemblers read cache through the coverage-index abstraction from day one** —
never by opening data files directly — so cache restructuring cannot break
the assemblers. The coverage index is a **solar system concept** where the
envelope is complex (object/center/date-range matrix). Other domains declare
their bounds simply: stars state distance and magnitude limits, orbital
parameters are always available, Earth system lists available scenarios.

**GitHub Pages hosting.** The gallery is ~436 MB against Pages' 1 GB ceiling,
with ~588 MB of headroom (post-cleanup, July 2026). The largest remaining
files are pre-refactoring exports that will shrink further when re-exported
with the current slimmer plotting functions. Headroom is shared between
gallery growth, cache data, and the Pyodide assembler code. A separate Pages
project site (each gets its own 1 GB) is an option if space tightens. R2
graduation for large files (star cache, orbit cache) is a dial.

---

## §2 — Gallery Extension Architecture (replaces v7 "Fork Decision")

**The gallery grows interactive; the desktop stays as-is.**

The desktop tkinter app continues as the power-user creation tool — live
Horizons, animation export, KML/KMZ, Gallery Studio. The web publication is
the gallery gaining new interactive pages, not a fork of the desktop GUI.

**The science museum model.** The gallery is the exhibit hall. Pre-curated cards
(today's content) are the permanent collection — beautiful, informative, no
computation required to view. Interactive pages are the hands-on science center
— the user walks up, makes selections, and sees the result. The curated
collection loads instantly (pre-computed JSON). The interactive exhibits load
after Pyodide initializes (5-15 seconds on first visit, cached after).

**Incremental delivery.** Each interactive page is a shippable increment:
"This week, planet selection and dates for static solar system views. Next
month, comet encounter presets. Later, star visualization with magnitude and
distance controls." Every step is useful on its own. No big-bang deployment.

**What this replaces.** The v7 plan called for forking the desktop GUI into a
web GUI (Dash or Pyodide), presenting 95 widget inputs on a web page, and
resolving a server-vs-serverless decision via a two-sided pilot. That approach
asked the wrong question — "how do we shrink the desktop onto a phone" — when
the right question was "what does a phone user want?" The answer is what the
gallery already does, plus the ability to change what's plotted.

**Shared computation layer — verified at HEAD (`d6c8c42`, unchanged at
`fdb66ca`):**

Six modules are import-clean (zero tkinter references): `idealized_orbits.py`,
`planet_visualization.py`, `visualization_utils.py`, `orbit_data_manager.py`,
`constants_new.py`, `shell_configs.py`.

**Two named seams (same as v7):**

1. `celestial_objects.py` — data half (`OBJECT_DEFINITIONS`) is import-clean.
   Selection/instance half is tk-shaped. The gallery imports the data; it
   supplies its own selection-state injection.

2. `palomas_orrery_helpers.py` — imports tkinter directly and carries
   computation the assembler will want. Fix: split computation from GUI helpers
   (L-087).

**Desktop migration is deferred, not abandoned.** Over time, the desktop could
refactor to use the shared assembler, unifying both paths. But this is an
efficiency improvement, not a web publication blocker. The critical path is:
assembler → gallery interactive page → ship it.

---

## §2a — Gallery Viewer Refactor (Option C — Hybrid)

**Two pages, not one; not N.**

`index.html` stays as-is — the "dumb renderer" that loads pre-computed JSON
and calls `Plotly.newPlot()`. It continues to serve curated cards with zero
changes to the existing pipeline (Studio → converter → viewer). The WYSIWYG
principle is untouched for curated content.

A single new `interactive.html` handles all interactive exhibits. The exhibit
is selected via URL parameter (`?exhibit=solar-system-explorer`). Each exhibit
is a "mode" within the page — a different control panel and assembler
configuration — not a separate HTML file. Two pages total for the entire
gallery.

**`gallery_metadata.json` is the bridge.** It gains a `type` field per entry:

```json
{ "type": "curated",     "file": "gallery/halley_perihelion.json", ... }
{ "type": "interactive", "exhibit": "solar-system-explorer", "label": "Solar System Explorer", ... }
```

Curated entries link to `index.html` (the existing viewer). Interactive entries
link to `interactive.html?exhibit=<exhibit>`. The gallery landing page reads
`gallery_metadata.json` and renders both types as cards — curated cards show
categories and thumbnails, interactive cards show an "Explore" badge and link
to the interactive page. The landing page could be `index.html` itself (adding
a section for interactive cards) or a lightweight `gallery.html` that links to
both. Resolve in Phase 0.

**Why this works:**

- **The existing pipeline is untouched.** Studio, the converter, the viewer —
  all continue to work exactly as they do today. No regression risk on 330+
  curated cards.
- **Interactive complexity is isolated.** Pyodide loading, control panels,
  assembler calls, coverage-index queries — all live in `interactive.html`.
  The curated viewer never loads Pyodide.
- **Editors develop separately.** Tony can refine the curated viewer and the
  interactive page on independent tracks. A bug in one cannot break the other.
- **Navigation is seamless.** Both pages share CSS and a common nav header.
  The user moves between curated and interactive content without feeling a
  seam.

**`interactive.html` responsibilities:**

1. Load the common gallery CSS and navigation header
2. Read the `exhibit` URL parameter → select the appropriate control panel
3. Lazy-load Pyodide (from CDN) + the assembler module + domain cache files
4. Render the control panel (planet toggles, date picker, presets, etc.)
5. On user selection: build a scene spec (JSON) → call the assembler via
   Pyodide → receive Plotly JSON → `Plotly.newPlot()`
6. Show loading state during Pyodide initialization ("Loading computation
   engine..." with progress)
7. Query the coverage index to determine available options — the envelope
   drives what controls are enabled

**Pyodide loading strategy:**

- **Lazy on first interactive visit.** Pyodide does not load until the user
  navigates to `interactive.html`. Curated content never triggers it.
- **Cached after first load.** The browser caches Pyodide's WASM and packages.
  Subsequent visits load in 1-2 seconds, not 10-15.
- **Honest about cold-start.** The page shows a loading indicator with a brief
  explanation: "Loading the computation engine for the first time. This takes
  about 10 seconds. Future visits will be faster."
- **Graceful degradation.** If Pyodide fails to load (old browser, blocked CDN),
  the page shows pre-computed default views and explains that interactive
  features require a modern browser.

**Mobile considerations (from gallery-pipeline skill):**

- 768px breakpoint separates phone from tablet (existing convention)
- Control panels collapse to a bottom drawer on mobile (tap to expand)
- Interactive Plotly figures use the same mobile conventions as curated: hide
  modebar, pinch-zoom, `100dvh` for iOS Safari
- Preset buttons are touch-friendly (minimum 44px tap targets)

**First artifact deployed:** `interactive.html` at gallery repo root alongside
`index.html`, serving the Solar System Explorer exhibit. Pyodide v314.0.2.
Created `300ac30c`, updated `a85a4fa` (July 6, 2026).

**Design inspirations (from research):**

- **NASA Eyes on the Solar System** — minimal controls overlaying 3D content;
  "if you can see it, you can click on it"; browser-native, real data
- **Exploratorium** — "you don't look at exhibits, you play with them"; the
  interactive page IS the exhibit, not a settings panel
- **teamLab / ArtScience Museum** — art + science + immersion; the dark space
  palette and glowing accents match the gallery's existing aesthetic
- **ViewSpace (STScI)** — interactive astronomy content that teaches while
  being beautiful; every exhibit carries context (the info panel)

---

## §3 — The Shared Assembler Architecture (settled)

**One shared assembler per domain, called by Pyodide in the browser.**

**The pattern — three stages:**

1. **Harvest.** The gallery page reads user selections (JavaScript) and builds
   a scene spec — a plain JSON document describing what to render.
2. **Assemble.** Pyodide calls the shared assembler (Python) with the spec plus
   cached data (through the coverage-index abstraction). No tkinter, no network
   calls. Produces a Plotly figure as JSON.
3. **Display.** JavaScript calls `Plotly.newPlot()` with the JSON. Same path
   the pre-curated cards already use.

**The assembler is new code.** The original desktop code is the recipe reference.
The assembler is written fresh against the scene-spec vocabulary (delivered by
Fable 5, July 4 2026), calling the shared computation engines. The original
code is archived for reference or reconstruction.

**Scene-spec vocabulary: DELIVERED.** `PHASE1_SCENE_SPEC_VOCABULARY.md` (Fable 5,
`fdb66ca`). Shared skeleton (5 fields) + solar system payload (9 field groups)
+ exhaustive mapping table (95 active `.get()` reads) + coverage index Protocol
class. Eight design decisions and six open questions deferred to the Phase 0 →
Phase 2 transition.

**The hybrid delivery model.** Pre-curated content ships as static JSON files
(fast, no Pyodide needed). Interactive content triggers Pyodide for on-demand
assembly. A gallery page can offer both: the curated card loads instantly; an
"Explore" button activates the interactive controls and initializes Pyodide.
The loading cost only appears when the user chooses to go beyond the curated
content.

**Per-domain assembler development** follows the same sequence as v7 (solar
system first, then stars, hybrid, Earth system) but each assembler's first
consumer is a gallery interactive page, not a separate web application.

---

## §3a — Data Serving Architecture (framed — Phase 1b)

**What Phase 0 proved.** The Solar System Explorer prototype computes
Keplerian orbits from mean orbital elements embedded in `orbital_elements.py`,
with no served data at all. This proves the Keplerian trace needs zero cache.
But the elements embedded in the codebase are manually maintained and some are
old (Saturn: epoch 2003, Pluto: epoch 1989). The desktop has better data —
fresh osculating elements in `osculating_cache_manager.py` and position
vectors in `orbit_paths.json` — accumulated over months of plotting.

**The data serving architecture is the pipeline that bridges Tony's desktop
caches to the browser.**

**Three trace types (from the desktop codebase, verified in gallery JSON):**

- **Actual positions** — Horizons ephemeris, x/y/z at dated time steps. Covers
  only the selected date range. Critical for precision at encounters, perihelia,
  close approaches, and date-range sweeps. This is the rolling cache data.
- **Osculating orbit at epoch** — complete Keplerian conic from instantaneous
  elements (6 numbers + epoch per object). Critical for moons, where it's the
  only way to see the full orbit shape. Also important for comets near
  perihelion. The divergence from the mean orbit IS the perturbation lesson.
- **Mean elements** — long-term average from `orbital_elements.py`. Ships with
  the codebase; no serving needed. Toggled off by default. Accurate for planet
  shapes; poor for close-approach detail.

**Two data types to serve (mean elements ship free):**

1. **Osculating elements per object** — tiny (a handful of numbers each). Could
   ride in the coverage index or a small sidecar file. The assembler computes
   the complete Keplerian conic from these.
2. **Position vectors over date ranges** — the rolling cache, the real volume.
   Per-object canonical files (F2 storage: ~157 positional objects, not 1,501
   pairs; canonical file count may be slightly higher due to barycenters).
   ~36 MB for the full catalog (Fable estimate, from 130.4 MB monolith).

**What works analytically vs what requires cache — two classes for the rolling
cache, plus a write-once category:**

- **Planets, asteroids, comets** — analytical orbits sufficient at solar-system
  scale. Presets override with cached data for close approaches and perihelia
  (Tier-2 curated data, write-once).
- **Moons** — cache required. Constant perturbations and non-heliocentric
  mechanics make analytical orbits insufficient. The rolling batch is primarily
  moons.
- **Spacecraft** — actual position arcs only, write-once (completed missions
  never change). Elements not typically applicable. Outside the rolling batch.

**Barycenters:** Pluto-Charon and Orcus-Vanth have barycenters outside the
primary body. The coverage index needs a `stored_center` field per object.

**F2 canonical storage (settled).** Per-object files, not per-pair. The old
pair-based `orbit_paths.json` (130.4 MB, 1,501 entries) is archived locally,
gitignored, and still used by the desktop code. The web cache is a derived
projection: an export script reads the desktop cache, extracts one canonical
trajectory per object (heliocentric for planets/asteroids/comets, parent-
relative for moons, arc-natural for spacecraft), and writes web-format files.
The precision rule: store moons parent-relative to preserve significance in
float64.

**Serving home is a configuration value.** The file layout and index schema
is the real architectural decision. Fable's H1 (dedicated `palomas-orrery-data`
repo, orphan-branch publish, zero history growth) is the leading candidate.
CORS verification needed before locking: does a project site under the custom
domain (`palomasorrery.com/<repo>/`) share the gallery's origin? Probable
answer: yes (same-origin under user-site custom domain), but confirm
empirically — not a blocker, a five-minute check.

**Star cache:** 31 MB pickle → `.npz` for v1 (NumPy stable in Pyodide; Parquet
held as optimization). Deferred to Phase 3.

**Open questions (carry to Phase 1b / Phase 2 transition):**

- OQ-A: Web catalog scope — all 157 positional objects or a curated first
  tranche?
- OQ-B: Window policy — sliding, accumulating, or split (accumulate
  heliocentric, slide moons)?
- OQ-C: Update cadence — monthly batch + 90-day forward padding as starting
  point.
- OQ-D: Moon step size — 6h gives ~7 points per Io orbit (hexagonal). Inner
  moons may want 2h. Per-object `step_hours` in the index.
- OQ-E: Serving home — dedicated repo (H1) vs gallery subfolder (H2) vs R2
  (H3). CORS check first.
- OQ-F: Canonical frame for each class — settled in principle (helio / parent-
  relative / arc-natural); implementation details at build time.
- OQ-G: Wire format — JSON for v1 (debuggability during assembler development).

**Source:** Fable 5 broad analysis (`DATA_SERVING_BROAD_ANALYSIS.md`, July 5,
2026, built on `993dfd5` / `a6420bc`). Reviewed and refined by Opus 4.6 + Tony
(July 6, 2026). 4.8 review confirmed source faithfulness (July 6, 2026).

---

## §4 — Four Visualization Domains

The domains are unchanged from v7. What changes is how each reaches the web.

### §4a — Solar System (the main build)

**Desktop GUI:** `palomas_orrery.py` (11,110 lines at HEAD). `plot_objects` and
`animate_objects` are the orchestration functions.

**Computation engines:** `idealized_orbits.py`, `planet_visualization.py`,
`visualization_utils.py`, `orbit_data_manager.py`, `shell_configs.py`,
`celestial_objects.py`, `constants_new.py`, plus shell visualization modules,
`spacecraft_encounters.py`, `close_approach_data.py`, `exoplanet_orbits.py`,
`star_sphere_builder.py`, `apsidal_markers.py`.

**Gallery interactive page:** Planet selection buttons, center body selector,
date picker. Initially static only. Presets for encounters, comet perihelion,
close approaches. Animation presets added later (curated tier-2 exports). The
vocabulary's 95 mapped inputs narrow to the 10-15 most useful for exploration;
the rest are set by preset defaults.

**Cache model:** Three-tier (§1). Coverage index drives the envelope.

### §4b — Stars

**Desktop GUI:** `star_visualization_gui.py` with HR diagram and planetarium
pipeline scripts.

**Data:** Gaia + Hipparcos, 101 ly distance, magnitude 9. Fully cached in PKL.
Cannot be casually regenerated. Wire format decision (pickle → Parquet/JSON)
needed for Pyodide (see §7).

**Gallery interactive page:** Distance and magnitude sliders, visualization
type selector, spectral class filters, star search. Rich controls — this
domain is naturally interactive and phone-friendly (2D HR diagrams render well
on small screens).

### §4c — Orbital Parameters (educational showcase)

**Desktop GUI:** `orbital_param_viz.py`. Eccentricity slider demo.

**Computation engines:** Pure geometry — `idealized_orbits.py`,
`constants_new.py`, `apsidal_markers.py`. No data fetching.

**Gallery interactive page:** The eccentricity slider is the Phase 0 test
case. Lightest domain, pure geometry, no cache files. Teaches the Keplerian
language the rest of the orrery speaks. Converts from matplotlib to Plotly
for the gallery (no matplotlib in the browser).

### §4d — Earth System

**Generators:** `earth_system_generator.py`, `food_insecurity_generator.py`.
Scenario modules for heatwaves, coral bleaching, food insecurity.

**Output:** Mixed — KMZ files for Google Earth + Plotly teasers.

**Gallery interactive page:** Scenario selector. KMZ download links with
Plotly teasers (the pattern that works today). Future: Plotly choropleth or
map library for browser-native rendering. The KMZ rendering question resolves
when this domain's interactive page is built.

**Stance carries forward:** "Synthesize nothing, transcribe everything,
attribute to IPC." "Data Preservation is Climate Action."

### §4e — Cross-Domain Integration

- **Celestial sphere** (`star_sphere_builder.py`): Adds star traces to orrery
  figures. Called by the solar system assembler.
- **Exoplanet orbits** (`exoplanet_orbits.py`): Bridges solar system and star
  domains. Phase 4 (hybrid).
- **Sgr A* Grand Tour** (`sgr_a_grand_tour.py`): Self-contained visualization.
  Phase 4 (hybrid).

---

## §5 — Phased Approach

**The gallery gains one interactive page per phase.** Each phase ships a
working increment. Tony's render remains the close authority (Mode 5).

**Delta-log discipline throughout:** any orchestration change to the desktop
during the build gets a ledger tag ("assembler-must-inherit").

### Phase 0 — Gallery Integration Test

**✓ DONE** (July 6, 2026). `interactive.html` deployed to
`palomasorrery.com/interactive.html` (created `300ac30c`, updated `a85a4fa`).
Pyodide v314.0.2 + NumPy computing Keplerian orbits from mean elements,
rendered by Plotly.js. Tested on desktop Chrome and iPhone Safari. Zero
server, zero data files — pure computation from embedded orbital elements.

**Stack proven:** Python computation runs in the browser on a static GitHub
Pages site. Server/serverless decision resolved: Pyodide.

**Consent gate:** First-time visitors see an explicit opt-in explaining Pyodide
("a Python computation engine that runs entirely in your browser via
WebAssembly. No data leaves your device"). Choice persisted in localStorage;
returning visitors go straight to loading. Resolves the user-trust concern
about unnamed downloads.

**Lessons:** Pyodide v314.0.2 loads in ~4-10 seconds depending on connection
(cached after first visit). The lightweight approach (Python/NumPy computes
math, JavaScript builds Plotly figure) avoids loading the full `plotly` Python
package — dramatically faster than loading plotly in Pyodide.

**Architecture A vs B fork (deferred to Phase 2 start).** Phase 0 proved
architecture A: Python computes arrays via NumPy, JavaScript builds Plotly
traces and calls `Plotly.newPlot()`. This is a different architecture than
Phase 2 specifies: architecture B, where a Python assembler calls the shared
computation engines (`idealized_orbits.py`, `planet_visualization.py`) via
`plotly.graph_objects` and emits complete Plotly JSON. A is lighter and faster
(no plotly in Pyodide). B reuses the desktop engines — which was the purpose
of the shared assembler (L-079). Phase 0 de-risked A; it did not de-risk B.
The decision gate is Phase 2 start, with an explicit plotly-in-Pyodide
cold-start measurement. Phase 1b (data serving pipeline) is the same
regardless of A or B. See §7 #10.

### Phase 1a — Shared Spec Skeleton + Solar System Vocabulary

**✓ COMPLETE.** `PHASE1_SCENE_SPEC_VOCABULARY.md` (Fable 5, July 4, 2026,
built on `fdb66ca`). Shared skeleton (5 fields) + solar system payload
(9 field groups) + exhaustive mapping table (95 active `.get()` reads) +
content-type distinction (proves one assembler replaces both orchestrators)
+ coverage index Protocol class. Serializability settled yes.

Eight design decisions (DD-1 through DD-8) and six open questions (OQ-1
through OQ-6) deferred to Phase 0 → Phase 2 transition.

Remaining gate items: seam gate-check and scene-equivalence criteria at
Phase 2 start.

### Phase 1b — Data Serving Pipeline

**Build the bridge from Tony's desktop caches to the browser.** The desktop
has accumulated months of osculating elements and position vectors from
Horizons. Phase 1b makes this data available to the interactive gallery.

Deliverables:
1. **Export script** — reads desktop caches (osculating elements from
   `osculating_cache_manager.py` + position vectors from `orbit_paths.json`),
   writes per-object canonical files in web-servable format (F2 storage).
2. **Coverage index** — JSON manifest listing available objects, their
   availability class, date coverage, step size, stored center, and osculating
   elements. The assembler (or the JS figure builder, depending on A/B fork)
   reads this to know what it can offer.
3. **Serving home** — resolve OQ-E (CORS check first), set up the serving
   destination, deploy the first web cache (planets as proof of pipeline).
4. **Resolve OQ-A through OQ-G** — scope, window policy, cadence, moon step
   size, format.

Requires: Fable analysis (delivered), gitignore updates (done @ `6368c87`).
Gate: export script runs, web cache deployed, interactive page can fetch it.

### Phase 2 — Solar System Assembler + First Interactive Page

Build the solar system assembler: scene spec → Plotly figure JSON. Written
against the Phase 1 vocabulary, calling the shared computation engines.

Build the first solar system interactive gallery page: planet selection
buttons, center body, date picker. Static scenes only. Presets for encounters,
comet perihelion, close approaches. Each preset is a pre-filled scene spec that
the user can view as-is or modify.

Requires: helpers split (L-087), Phase 1b data pipeline, A/B architecture
decision (§7 #10 — measure plotly-in-Pyodide cold-start).

Gate: scene equivalence (Mode 5) + the gallery page ships.

### Phase 3 — Star Assembler + Interactive Page

Design the star vocabulary (just-in-time, informed by Phase 2 lessons). Build
the star assembler. Resolve the star cache wire format — pickle → Parquet or
JSON for browser delivery.

Build the star interactive gallery page: distance and magnitude controls, HR
diagram and planetarium view selectors, spectral class filters.

Gate: scene equivalence + Mode 5 + the page ships.

### Phase 4 — Hybrid: Exoplanets + Sgr A*

Cross-domain gallery pages. Depends on the solar system assembler.

Gate: scene equivalence + Mode 5 + pages ship.

### Phase 5 — Earth System

Resolve the KMZ rendering question. Build the Earth system interactive gallery
page: scenario selector with Plotly teasers and KMZ download links. Future:
browser-native map rendering. 4.8 for restraint discipline on human-cost
content.

Gate: Mode 5 + the page ships.

### Phase 6 — Dissolves

In the v7 plan, Phase 6 was "Web UI." In the gallery-extension model, there is
no separate web UI to build — the gallery IS the UI. Each earlier phase ships
its own interactive page. What remains is refinement: navigation coherence
across all interactive pages, mobile responsive polish, the "suite-design
conversation" about what the whole interactive gallery feels like (L-096).
This is continuous work, not a gated phase.

---

## §5a — Execution Map: Dependencies & Model Assignments

### Dependency Chain

```
PREP (independent, can start now)
  ✓ LICENSE moved to root
  ✓ Section W ledger entries
  ○ Attribution page ─────────── 4.8 ──→ needed before public pages
  ○ Helpers split ────────────── 4.6 ──→ needed before Phase 2

PHASE 0 ✓ DONE ──── PHASE 1a ✓ COMPLETE ──── PHASE 1b
Stack proven         Vocabulary delivered       Data serving pipeline
Arch A proven        (Fable, Jul 4)             Export script + coverage
(Jul 6)                                         index + serving home
                          │
                     ┌────┴────┐
                  A/B DECISION
                  Measure plotly-in-Pyodide
                     └────┬────┘
                          │
                     PHASE 2 ◄── Phase 1b + helpers split + A/B decision
                     Solar system assembler (if B)
                     or enhanced JS builder (if A)
                     + interactive page
                          │
                     PHASE 3
                     Star assembler + star cache format
                          │
                     PHASE 4
                     Hybrid domains
                          │
                     PHASE 5 ◄── 4.8 restraint discipline
                     Earth system
```

**Critical path:** Phase 1b → A/B decision → Phase 2 → domain pages.
(Phase 0 and Phase 1a complete.)

**Secondary dependencies:**
- Helpers split → Phase 2 (computation functions freed from tkinter)
- Attribution page → any publicly reachable interactive page
- Star cache wire format → Phase 3 (Pyodide needs non-pickle format)
- A/B architecture decision → Phase 2 (measure plotly-in-Pyodide cold-start)

### Model Assignments

**Fable 5** — Phase 1a vocabulary delivered. Data serving analysis delivered.
Fable access expired July 7, 2026.

**Opus 4.8** — verification, convergence, restraint. Attribution page (fetch
license terms). Vocabulary DD/OQ review at Phase 2 start. Phase 5 restraint
discipline on human-cost content. v9 draft review (completed July 6, 2026:
caught gallery SHA provenance, gitignore claim, A/B fork, OQ-10 overclaim).

**Opus 4.6** — daily conversational partner, iterative build. Phase 1b data
serving pipeline, helpers split, all assembler and interactive page builds.

### Next Step

Phase 1b: design and build the data serving pipeline. Export script, coverage
index, serving home. Resolve OQ-A through OQ-G.

---

## §6 — Prep Work

**L-080 — Smoke-test harness.** Spec for scene equivalence (Phase 1 criteria).
Deferred to Phase 2 start.

**LICENSE to repo root.** ✓ Done. `LICENSE.md` at repo root at HEAD (`7b25eb9`).

**Attribution page.** ○ Not started. Data sources: JPL Horizons, JPL SBDB/CAD,
Copernicus CDS / ERA5 / ERA5T, NOAA Coral Reef Watch, IPC and FEWS NET, HDX,
OCHA FTS, SIMBAD (CDS), Gaia (ESA), Hipparcos, NSIDC, Mauna Loa CO₂ (NOAA
GML/Scripps), HOT program. Provider citation strings need fetching (4.8 task —
fetched not recalled). Copernicus and IPC terms most likely to constrain
hosting. Not a Phase 0 blocker if page kept unlisted; required before any
publicly reachable interactive page.

**L-068 residuals** (L-066, L-016, L-014) — Desktop cleanup. Not web blockers.

**`palomas_orrery_helpers.py` split** — ○ Not started. Separate computation
from tkinter GUI helpers. Computation the assembler needs:
`calculate_planet9_position_on_orbit`, `rotate_points2`,
`calculate_axis_range`. Required before Phase 2.

---

## §7 — Open Decisions

1. ~~**Server vs serverless.**~~ **Resolved: Pyodide.** Phase 0 proved the
   stack (July 6, 2026): Pyodide v314.0.2 loads in ~4 seconds on WiFi,
   computes Keplerian orbits via NumPy, renders via Plotly.js. Works on
   desktop Chrome and iPhone Safari. Consent gate addresses user-trust
   concern about unnamed downloads.
2. ~~**Scene-spec vocabulary design.**~~ **Delivered** (Fable 5, July 4).
   DD/OQ rulings at Phase 2 start.
3. **Data serving file layout and index schema.** Per-object canonical files
   (F2 settled). Coverage index format, availability classes, `stored_center`
   field. Resolved in Phase 1b.
4. **Tier-1 rolling cache scope and window.** OQ-A (which objects), OQ-B
   (window policy), OQ-C (cadence), OQ-D (moon step size). Resolved in
   Phase 1b.
5. **Tier-3 persistence:** on or off. A dial.
6. **Serving home.** CORS check determines whether a dedicated repo (H1)
   shares origin with the gallery under the custom domain. Five-minute
   check; probable answer is yes (same-origin). Resolved in Phase 1b.
7. **Earth system KMZ rendering on the web:** downloads with teasers, Plotly
   choropleth, or map library.
8. **Star cache wire format:** PKL → Parquet/JSON for Pyodide. Resolved in
   Phase 3.
9. ~~**Matplotlib in Phase 0.**~~ **Dissolved.** The gallery is Plotly. The
   eccentricity demo converts to Plotly as part of Phase 0 — not a separate
   decision.
10. **Pyodide package weight + cold-start.** **Resolved for the lightweight
    path** (architecture A: NumPy in Pyodide, JS builds figure). Pyodide
    v314.0.2 loads in ~4-10 seconds; consent gate gives users an explicit
    choice; returning visitors skip consent (localStorage). **Open for the
    assembler path** (architecture B: plotly loaded in Pyodide). The shared
    computation engines are deeply `graph_objects`-based (88 `go.*` usages
    in `idealized_orbits.py` alone) — if Phase 2 reuses them, the full
    `plotly` Python package must load in Pyodide, and that cold-start is
    unmeasured. **Decision gate:** measure plotly-in-Pyodide cold-start at
    Phase 2 start. If acceptable, B (shared engines). If not, A (JS figure
    builder, vocabulary and coverage index still apply). Phase 1b is the
    same regardless.
11. ~~**Gallery viewer architecture for interactive pages.**~~ **Resolved:
    Option C (hybrid).** `index.html` stays as curated viewer. Single
    `interactive.html` handles all interactive exhibits via URL parameter.
    `gallery_metadata.json` bridges both. See §2a.

---

## §8 — Vision Opportunities

*Captured in `LEDGER_CONSOLIDATED.md`. Several already carry L-numbers.*

**Arriving naturally with the gallery-extension model:**

- **Option E unified front end** (L-091) — the gallery IS the front end now.
  This vision item is realized by the architecture, not deferred.
- **Gallery generators as spec-producers** — already true for pre-curated
  cards; interactive pages extend it.
- **Embeddable scenes for educators** (L-092) — a gallery page with preset
  parameters in the URL hash is an embeddable exhibit. Arrives nearly for free
  once interactive pages exist.
- **Educational guided explorations** (L-093) — the narrative sections plus
  interactive pages plus presets = a guided tour.

**Still deferred:**
- Preset authoring (L-046)
- Community cache as commons (L-094)
- PWA / offline for classrooms (L-095)
- What the interactive gallery *feels* like (L-096 — suite-design conversation)

---

## §9 — What This Plan Does NOT Cover

Desktop development continues on its own track. The gallery extension is
additive. The Instagram pipeline is independent. The existing ledger is
unaffected. Desktop-to-assembler migration (refactoring the desktop to use
the shared assembler) is deferred — valuable for codebase unification but
not on the critical path for the gallery.

---

## §10 — Lineage

This plan draws from fifteen sessions across three Claude models + two pivots:

- **Fable 5 survey** (July 2, 2026): Four-front survey. L-079 as keystone.
  Five publication options. Six code proposals (L-079–L-084).
- **Fable 5 L-079 deep dive** (July 2, 2026): Five S-options, four M-options,
  three phasing strategies, repricing map.
- **Opus 4.8 convergence handoff** (July 2, 2026): Fetched JPL/GitHub terms.
  Converged site-never-fetches, three-tier cache, envelope-declaring GUI.
- **Opus 4.8 review of v2** (July 3, 2026): Verified shared-layer boundary.
  Caught `celestial_objects.py` seam.
- **Fable 5 review of v2** (July 3, 2026): Found `palomas_orrery_helpers.py`
  seam. Named assembly-duplication tension. Redefined gate as scene equivalence.
- **Opus 4.6 + Tony convergence** (July 3, 2026): Resolved option (b) — shared
  assembler. Fork decision. Four domains identified.
- **Opus 4.8 review of v3.1** (July 3, 2026): Named server-vs-serverless
  decision. Two-substrate model. Cache-through-index from day one.
- **Fable 5 review of v4** (July 3, 2026): Star PKL cache provenance. Module
  corrections. Phase 7 drift window → per-domain migration tails. Vocabulary
  waterfall → just-in-time. Two-sided pilot. Animation envelope. Scene
  equivalence criteria. Coverage index as solar system concept.
- **Opus 4.6 execution review** (July 4, 2026): Verified prep work status.
  Mapped dependency chain and critical path. Assigned models to phases.
  Identified Fable access window. Surfaced matplotlib question. Produced
  interactive dependency chart.
- **Opus 4.6 Fable prompt** (July 4, 2026): Drafted task prompt for Phase 1
  vocabulary design. Reviewed by Opus 4.8 (9 points accepted).
- **Fable 5 vocabulary design** (July 4, 2026): Produced
  `PHASE1_SCENE_SPEC_VOCABULARY.md`. Proved animation/static consolidation.
  Coverage index Protocol class. Eight DDs, six OQs.
- **Opus 4.6 convergence review** (July 5, 2026): Reviewed Fable deliverable.
  DD/OQ rulings deferred to Phase 2 start. Phase 1 marked complete.
- **Opus 4.6 + Tony architectural pivot** (July 5, 2026): Gallery-extension
  model replaces fork-the-desktop model. Science museum metaphor. JSON bridge
  as unifying principle. Phase 0 simplifies to one-sided Pyodide test inside
  gallery. Matplotlib question dissolved (gallery is Plotly). Phase 6
  dissolved (gallery IS the UI). Server-vs-serverless resolved in principle
  (Pyodide/static). Desktop migration deferred from critical path. Gallery
  viewer architecture settled (Option C: two pages). New open decisions:
  Pyodide weight, data serving architecture, second-renderer question
  (resolved: two WYSIWYG pipelines, not a shared core — each studio previews
  through its own viewer).
- **Opus 4.8 review of v8** (July 5, 2026): Confirmed pivot integrity,
  vocabulary preservation, constraint faithfulness, phasing coherence, and
  restraint carryover. Flagged second-renderer tension (resolved by
  two-studio WYSIWYG model). Flagged Pyodide cold-start acceptance criteria
  (resolved: gallery already serves 30 MB+ files, Pyodide is within norms).
  Verified `graph_objects` coupling makes full plotly package unavoidable in
  Pyodide. Confirmed 148 gallery entries vs "330+" claim. Provided headroom
  math (479+130+31=640 MB, but orbit/star caches are gitignored — not in
  either repo). Nits accepted.
- **Opus 4.6 + Tony data serving exploration** (July 5, 2026): Discovered
  orbit cache and star cache are both gitignored — not served by either repo.
  Surfaced planet/satellite split (planets have analytical fallback, satellites
  don't). Explored per-pair splitting, curated subset, orrery Pages, Releases,
  R2, and hybrid approaches. Identified rolling cache date-range question.
  Referred to Fable 5 for broad-first analysis.
- **Fable 5 data serving analysis** (July 5, 2026): Broad-first analysis of
  data serving architecture. Five reframing findings: F2 canonical per-object
  storage collapses 1,501 pairs to ~157 objects; restructured cache ~36 MB
  (not 130.4 MB). Three-class split (analytic-capable / elements-degrading /
  trajectory-is-the-data), refined to two classes + write-once in Tony's
  convergence. Three hybrid approaches (H1-H3). Serving home identified as
  configuration value, not architecture. Seven open questions (OQ-A through
  OQ-G). Six verification items.
  (`DATA_SERVING_BROAD_ANALYSIS.md`, built on `993dfd5` / `a6420bc`.)
- **Opus 4.6 + Tony convergence and build** (July 6, 2026): Reviewed Fable
  analysis; adopted F2, three trace types, two-class model (analytic vs
  cache-required, plus spacecraft write-once). Built Solar System Explorer
  as Phase 0 deliverable — `interactive.html` deployed to
  `palomasorrery.com/interactive.html` (created `300ac30c`, updated
  `a85a4fa`). Pyodide v314.0.2, mean element Keplerian computation,
  consent gate. Tested on desktop Chrome and iPhone Safari. Phase 0 proven.
  Phase 1b (data serving pipeline) identified as the gap between vocabulary
  (Phase 1a) and assembler (Phase 2). Gitignore updated for orbit cache
  files (`6368c87`).
- **Opus 4.8 review of v9 draft** (July 6, 2026): Caught gallery SHA
  provenance error (draft cited `a6420bc` where `interactive.html` did not
  yet exist; correct provenance is `300ac30c` / `a85a4fa`). Caught gitignore
  "done" claim ahead of repo (subsequently pushed at `6368c87`). Named the
  architecture A vs B fork: Phase 0 proved A (numpy + JS figure builder)
  while Phase 2 specifies B (Python assembler with `graph_objects`). Flagged
  OQ-10 overclaimed for the B path. Recommended: name the fork, defer
  decision to Phase 2 start with measurement gate. All findings accepted.

**Decisions made (cumulative):**

*Preserved from v7:*
- Site never fetches Horizons (§1)
- Three-tier cache, all offline (§1)
- GUI declares the envelope, including content type (§1)
- Assemblers read cache through index abstraction from day one (§1)
- Coverage index is solar system concept; other domains declare bounds simply (§1)
- One shared assembler per domain (§3)
- Assembler is new code; original code archived (§3)
- Four visualization domains recognized (§4)
- Star data is fully cached, 101 ly / mag 9, Gaia + Hipparcos (§4b)
- Other domain vocabularies designed just-in-time (§5)
- Animation presets as curated tier-2 exports (§1/§5)
- Phase 1 vocabulary complete (Fable, Jul 4)
- Animation/static consolidation verified (Phase 1)
- Scene spec is JSON-serializable from day one (Phase 1)
- DD/OQ rulings deferred to Phase 2 start (Phase 1)

*New in v8 — the pivot:*
- Gallery is the web publication, not a separate app (§2)
- Science museum model: curated permanent collection + interactive exhibits (§2)
- Incremental delivery: each interactive page ships independently (§2)
- JSON bridge: pre-curated and interactive content produce the same artifact (§1)
- Pyodide for client-side computation; no server (§1)
- Desktop migration deferred from critical path (§2)
- Matplotlib question dissolved — gallery is Plotly (§7)
- Phase 6 dissolved — gallery IS the UI (§5)
- Server-vs-serverless resolved in principle: serverless/Pyodide (§7)
- Gallery viewer: Option C hybrid — two pages, `index.html` + `interactive.html` (§2a)

*New in v9:*
- Phase 0 proven: Pyodide v314.0.2 + NumPy + Plotly.js on static GitHub Pages (§5)
- Server/serverless resolved in practice: Pyodide (§7 #1)
- Architecture A vs B fork named; decision deferred to Phase 2 start (§5, §7 #10)
- F2 canonical per-object storage adopted (§3a)
- Three trace types: actual positions, osculating at epoch, mean elements (§3a)
- Two data types to serve: osculating elements + position vectors (§3a)
- Two classes for rolling cache + spacecraft write-once (§3a)
- Phase 1b inserted: data serving pipeline (§5)
- Consent gate for Pyodide loading (§5, §7 #10)
- Pyodide cold-start acceptable for lightweight path; unmeasured for assembler path (§7 #10)
- `interactive.html` deployed as first exhibit (§2a)
- `orbit_paths.json` and `orbit_cache/` added to `.gitignore` (§3a)
- URL parameter scheme: `?exhibit=` (§2a)

*Superseded:*
- ~~Web GUI is a fork, not a replacement~~ → gallery extension (§2)
- ~~Phase 0 is two-sided pilot: Dash + Pyodide~~ → one-sided gallery test (§5)
- ~~Two hosting substrates~~ → one: GitHub Pages, static (§1)
- ~~Per-domain desktop migration tails~~ → deferred, not on critical path (§2)

---

Base: orrery @ `6368c87` / gallery @ `a85a4fa`. Phase 0 proven. Phase 1a
vocabulary delivered. Phase 1b (data serving pipeline) is the next design
track. A/B architecture fork deferred to Phase 2 start. Solar System
Explorer live at palomasorrery.com/interactive.html.
