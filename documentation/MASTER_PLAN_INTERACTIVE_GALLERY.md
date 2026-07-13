# MASTER PLAN: Paloma's Orrery Interactive Gallery

**Status:** v11 -- Phase 1b BUILT + DEPLOYED (v0.4 fetch-fresh). Live dry-run gate passed 2026-07-11; offline suite green from a clean clone (L-114 config fix + L-117 mock fix); served cache live at gallery data/solar-system/. Close pending only the backup action (L-106).
**Base:** orrery @ `ca5c052`, gallery @ `4b086a6` (remediated builder pending re-push)
**Date begun:** July 3, 2026
**Last updated:** July 9, 2026
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
repo. **Phase 0 confirmed Pyodide is acceptable** (2.1-3.3 s cold-start on
iPhone WiFi, including plotly via micropip). The B′ architecture (shared
desktop engines running in Pyodide) is the Phase 2 path. Frozen pedagogical
demos (like the Phase 0 Solar System Explorer) stay on the lightweight A path
(NumPy only, JS figure builder) — a two-tier model.

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
both. Resolved: `interactive.html` deployed alongside `index.html`; landing
page integration deferred to Phase 2.

**Why this works:**

- **The existing pipeline is untouched.** Studio, the converter, the viewer —
  all continue to work exactly as they do today. No regression risk on 148
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

## §3 — The Shared Assembler Architecture (settled — architecture B′)

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
- **Spacecraft** — actual position arcs. NOT write-once (OQ-B): the flown arc
  is a coarse glide backbone + daily densification inside known flyby windows,
  Douglas-Peucker-thinned, and each nightly run appends today's point.
  Elements not applicable.

**Barycenters:** Pluto-Charon and Orcus-Vanth have barycenters outside the
primary body. The coverage index needs a `stored_center` field per object.

**F2 canonical storage (settled).** Per-object files, not per-pair. The old
pair-based `orbit_paths.json` (130.4 MB, 1,501 entries) is archived locally,
gitignored, and still used by the desktop code. The web cache is a derived
projection -- but NOT by reading the desktop cache (the v0.4 fetch-fresh pivot).
A standalone nightly builder fetches FRESH from Horizons per object with the
explicit canonical center (heliocentric for planets/asteroids/comets, parent-
relative for moons, arc-natural for spacecraft) into a purpose-built gallery
cache, so provenance is guaranteed by construction; the legacy desktop cache is
no longer read.
The precision rule: store moons parent-relative to preserve significance in
float64.

**Serving home is a subdirectory of the gallery repo.** The `data/` directory
in `tonyquintanilla.github.io` serves at `palomasorrery.com/data/`. Same
origin by construction — no CORS question. Gallery measured at 474 MB with
526 MB headroom against the 1 GB GitHub Pages soft limit; all-phase data
needs are ~72 MB (14% of remaining). Pre-heavy gallery JSONs are cullable
via L-074 if headroom tightens. The coverage index's `generated` timestamp
is the provenance anchor for the data (the data files don't carry their own
version history).

**Star cache:** 31 MB pickle → `.npz` for v1 (NumPy stable in Pyodide; Parquet
held as optimization). Deferred to Phase 3.

**Open questions — status after Phase 1b design convergence (v0.3):**

- OQ-A: Web catalog scope — curated first tranche (9 test objects); full
  catalog scales via export run, not schema change. **Positioned.**
- OQ-B: Window policy — v0.4 provisional leading edge -- nightly overwrite
  `[today-7d, today]`, freeze older past; `horizon=0` for non-spacecraft (the
  conic covers the future); spacecraft fetch the flown arc once then append
  today nightly (NOT write-once). **Settled (v0.4).**
- OQ-C: Update cadence — NIGHTLY batch (v0.3 pivot), no forward padding --
  `horizon=0`, the conic covers the future. **Settled (v0.4).**
- OQ-D: Moon step size — 6h default; per-object `step_hours` from day one.
  Io may want 2h. Mode 5 decides. **Positioned, Mode 5.**
- OQ-E: Serving home — H2 subfolder in gallery repo (`data/`). Gallery
  measured at 474 MB, 526 MB headroom, all-phase data needs ~72 MB. No
  CORS question (same repo, same origin). **Settled.**
- OQ-F: Canonical frame — helio / parent-relative / arc-natural. The v4 model correction
  RETIRED subtraction (catastrophic cancellation + aliasing); osculating-primary
  now. The builder fetches FRESH from Horizons at each object's canonical center
  (it DOES re-query); no co-sampling for the orbit. **Settled (v0.4).**
- OQ-G: Wire format — JSON for v1, column-oriented. **Settled.**

**Schema decisions settled in v0.3 (three-model convergence):**

> **v0.4 / v4 reconciliation note (July 9):** the SUBTRACTION / parent-
> composition model in some bullets below was RETIRED by the July-8 v4 model
> correction. Moons now render from their OWN osculating conic (osculating-
> primary), fetched FRESH per object; parents no longer compose moon orbits.
> Where a bullet conflicts with osculating-primary + fetch-fresh,
> GALLERY_DATA_SOURCE_HANDOFF v0.4 and the shipped gallery_cache_builder.py are
> authoritative. Full section-3a rewrite tracked as L-108.

- Osculating elements carry explicit `center` field (prevents Charon@9 class
  errors). One orbit shape per object, no `valid_until` (science museum, not
  mission planning).
- Moons render from their OWN osculating conic in the parent-relative frame
  (osculating-primary); no parent-position composition for the orbit
  (superseded the cache-exact composition model -- see the note above).
- `trajectory_of` field for barycenter substitution (Pluto's trajectory is
  the barycenter's; schema says so explicitly).
- Presets are self-contained (no frame composition, no dependency on other
  objects' rolling cache).
- Unit is data: km for positions (float64 significance for moons), AU for
  osculating elements (by field name). Assembler reads `unit` field, never
  assumes.
- Provenance source: hybrid string/structured object (Horizons-derived data
  carries `{query_target, center, epoch, retrieved}` for re-verification).
- Feature rendering: always JS in interactive layer (both A and B′). Python
  assembler handles orbits only. Feature configs in separate
  `feature_configs.json`. Three-context table: static gallery (pre-baked) /
  interactive A (JS everything) / interactive B′ (Python orbits + JS
  features).
- 8 validation invariants the export script asserts before emitting the index.
- 9 test objects covering every schema class and edge case.

**Source:** Fable 5 broad analysis (`DATA_SERVING_BROAD_ANALYSIS.md`, July 5,
2026, built on `993dfd5` / `a6420bc`). Reviewed and refined by Opus 4.6 + Tony
(July 6, 2026). 4.8 review confirmed source faithfulness (July 6, 2026).
Phase 1b design handoff v0.3 (`PHASE1B_DATA_SERVING_DESIGN_HANDOFF.md`,
July 7, 2026): Opus 4.6 + Tony → 4.8 review → Fable 5 review → convergence.

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

**Architecture A vs B fork — RESOLVED: B′.** Phase 0 proved architecture A
(Python/NumPy computes arrays, JS builds Plotly traces). Fable 5 identified
that A creates a parallel rendering pipeline — convention duplication across
Python and JavaScript for the life of the project (the protocol's own anti-
pattern). A B′ measurement page (`measure_plotly.html`) timed the full
plotly-in-Pyodide cold-start on iPhone Safari WiFi:

- Pyodide runtime: 929-959 ms
- NumPy: 141-146 ms
- micropip + plotly install: 507 ms - 1.8 s
- `import plotly.graph_objects`: 57-59 ms
- Build figure + `to_json()`: 448-449 ms
- **Total: 2.1-3.3 s** (acceptance threshold was ≤15 s)

Fable verified plotly 6 imports lazy (0.06 s native); the WASM multiplier is
~1:1. The feared cold-start cost dissolved. B′ uses a slim self-hosted wheel
(~3.9 MB, stripped of dead JS bundles and Jupyter extras) from the Phase 1b
serving home — no PyPI runtime dependency.

**Two-tier model:** frozen pedagogical demos (Phase 0 Solar System Explorer,
eccentricity demo) stay on A — instant-loading, convention-light, no sync tax
because frozen exhibits don't change. Data-backed catalog exhibits (Phase 2+)
take B′ — shared desktop engines, one codebase, scene equivalence by
construction.

**Attribution gate (L-086):** `interactive.html` is publicly reachable with
inline "Data: JPL/NASA" credit. Ruled sufficient pending L-086: a JPL-only
exhibit with inline credit passes. Page kept unlinked from landing page until
L-086 lands.

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

**Fetch fresh from Horizons, serve to the browser.** Phase 1b builds a
purpose-built gallery cache in the gallery repo, populated nightly from
JPL Horizons with an explicit center per object -- the legacy desktop cache
is no longer read (provenance by construction). It makes this data
available to the interactive gallery.

**Design converged: v0.4** (v0.3 July 7 + the fetch-fresh / nightly amendments, July 8-9). Three-model review: Opus 4.6 +
Tony drafted schema → 4.8 caught osculating-center gap, parent dependency,
validation invariants → Fable 5 caught invariant self-contradiction,
`stored_center` overload, grid nesting → Opus 4.6 + Tony converged.
Full design in `PHASE1B_DATA_SERVING_DESIGN_HANDOFF.md v0.3`.

Deliverables:
1. **Export script** — fetches FRESH from Horizons per object with the explicit canonical
   center (v0.4 fetch-fresh pivot -- the legacy desktop cache is no longer
   read), validates on write (Guard v2 MONITOR + structural invariants), then
   stages -> atomic-swaps -> commits per-object canonical files in web-servable
   format (F2 storage). Built as `tools/gallery_cache_builder.py`.
2. **Coverage index** — JSON manifest (schema v0.3) listing available objects,
   availability class, date coverage, step size, osculating elements with
   explicit center, `trajectory_of` for barycenter substitution, feature
   slugs. The assembler reads this to know what it can offer.
3. **Feature configs** — separate `feature_configs.json` with renderer +
   params for JS feature renderers (interactive layer only; static gallery
   pre-bakes features).
4. **Serving home** — OQ-E resolved (H2): the cache lives in the GALLERY repo `data/`
   subfolder -- same repo, same origin, NO CORS question (the dedicated
   `palomas-orrery-data` repo, option H1, was superseded). Deploy first web cache.
   The slim plotly wheel (~3.9 MB, B′) also lives here.

Requires: Fable analysis (delivered), design handoff (converged v0.4),
gitignore updates (done @ `6368c87`).
Pre-build: diff `f1ede52..a56e036` for source file changes.
Gate: export script runs, web cache deployed to `data/`, interactive page
can fetch it.

### Phase 2 — Solar System Assembler + First Interactive Page

Build the solar system assembler: scene spec → Plotly figure JSON. Written
against the Phase 1 vocabulary, calling the shared computation engines.

Build the first solar system interactive gallery page: planet selection
buttons, center body, date picker. Static scenes only. Presets for encounters,
comet perihelion, close approaches. Each preset is a pre-filled scene spec that
the user can view as-is or modify.

Requires: helpers split (L-087), Phase 1b data pipeline. Architecture B′
confirmed (measurement passed July 6, 2026 — 2.1-3.3 s on iPhone).

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
B′ measured: PASS                               index + serving home
(Jul 6)                                         + slim plotly wheel
                          │
                     PHASE 2 ◄── Phase 1b + helpers split
                     Solar system assembler (B′)
                     Shared engines in Pyodide
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

**Critical path:** Phase 1b → Phase 2 → domain pages.
(Phase 0, Phase 1a complete. A/B fork resolved: B′.)

**Secondary dependencies:**
- Helpers split → Phase 2 (computation functions freed from tkinter)
- Attribution page → any publicly reachable interactive page
- Star cache wire format → Phase 3 (Pyodide needs non-pickle format)
- ~~A/B architecture decision~~ → resolved: B′ (July 6, 2026)

### Model Assignments

**Fable 5** — Phase 1a vocabulary delivered. Data serving analysis delivered.
Phase 1b design review (July 7, 2026: caught invariant #4 self-contradiction,
`stored_center` overload, grid nesting). Fable access extended to July 12,
2026. Available for: provenance Tier-1 triage, Phase 2 broad-first design.

**Opus 4.8** — verification, convergence, restraint. Phase 1b design review
(July 7, 2026: caught osculating center gap, validation invariants, parent
dependency). Attribution page (fetch license terms). Vocabulary DD/OQ review
at Phase 2 start. Phase 5 restraint discipline on human-cost content.

**Opus 4.6** — daily conversational partner, iterative build. Phase 1b design
led and converged. Phase 1b build (CORS check, export script, coverage index).
Helpers split, all assembler and interactive page builds.

### Next Step

Phase 1b build UNDERWAY. The standalone `gallery_cache_builder.py` +
`objects_config.json` + an offline smoke test are built and offline-verified
(47 checks, py_compile clean; provenance to orrery `4e2629c`). NEXT: live dry-
runs on Tony's hardware (manifest v2 S10 -- voyager_1 ephemeris start, encke
solution-Tp + Mode-5 Tp match), first full build, schedule nightly + backup.

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
10. ~~**Pyodide package weight + cold-start.**~~ **Resolved: B′.** Measured
    on iPhone Safari WiFi (July 6, 2026): Pyodide v314.0.2 + NumPy +
    micropip + plotly (stock wheel from PyPI) = **2.1-3.3 s total cold
    start**. `import plotly.graph_objects` = 57-59 ms (plotly 6 lazy-loads;
    WASM multiplier ~1:1). B′ uses a slim self-hosted wheel (~3.9 MB,
    stripped of dead JS bundles and Jupyter extras per Fable's strip spec)
    from the Phase 1b serving home — no PyPI dependency. Two-tier model:
    frozen A exhibits (instant, convention-light) + data-backed B′ exhibits
    (shared engines, one codebase). Fable's convention-duplication analysis
    confirmed A's parallel-pipeline cost outweighs B′'s cold-start cost for
    a solo developer at Phase 2 scale. OQ-i through OQ-v (from Fable A/B
    analysis) carry to Phase 2 start.
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

This plan draws from seventeen sessions across three Claude models + two pivots:

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
- **Fable 5 A/B architecture analysis** (July 6, 2026): Convention-duplication
  inventory at Phase 2 scale. Proved duplication is conserved across the A
  family (A, A′, A″ relocate it; only engine reuse eliminates it). Verified
  plotly wheel is 9.9 MB (not 15), import is 0.06 s native (lazy in plotly 6),
  dead JS bundles are 19.5 MB of 43.2 MB uncompressed. Built and tested slim
  B′ wheel: 3.9 MB, fully functional for `go.Scatter3d` + `fig.to_json()`.
  Recommended B′ with A retained for frozen pedagogical demos (two-tier model).
  OQ-i through OQ-v for Phase 2 start. (`AB_FORK_ANALYSIS.md`, built on
  `873c6cd` / `827d0b3`.)
- **B′ cold-start measurement** (July 6, 2026): `measure_plotly.html` deployed,
  timed on iPhone Safari WiFi. Stock plotly from PyPI: 2.1-3.3 s total cold
  start. `import plotly.graph_objects` = 57-59 ms. WASM multiplier ~1:1.
  Acceptance threshold ≤15 s — passed at one-seventh. A/B fork resolved: B′.
  Phase 0 closed.

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

*New in v10:*
- Phase 1b design converged v0.4, three-model review (§3a, §5)
- OQ-E resolved: H2 subfolder in gallery repo (474 MB used, 526 MB headroom,
  ~72 MB all-phase data needs) (§3a)
- 14 settled schema decisions: osculating center, parent position files,
  trajectory_of, presets self-contained, subtract-don't-requery, unit-is-data,
  feature rendering always JS, validation invariants, grid nesting (§3a)
- Coverage index schema v0.3 with 8 validation invariants (§3a)
- Feature rendering architecture: three-context split (§3a)
- OQ-B/C/F/G settled; OQ-A/D positioned; OQ-E pending CORS check (§3a)
- Fable access extended to July 12, 2026 (§5a)
- Phase 1b deliverables refined: coverage index, feature configs, export
  script with invariant assertions (§5)

*New in v11 (July 9, 2026):*
- Phase 1b BUILD: standalone `gallery_cache_builder.py` + `objects_config.json`
  + offline test, offline-verified (47 checks); live gate pending (L-098).
- SUBTRACTION model retired (v4 correction): osculating-primary; the builder
  fetches FRESH from Horizons, does NOT read the desktop cache (section 3a, 5).
- Cadence corrected to NIGHTLY (was monthly); `horizon=0`, no forward padding;
  provisional leading edge; spacecraft fetch-once + append-nightly (OQ-B/C).
- Serving home = gallery repo `data/` subfolder (H2), not the dedicated H1 repo.
- Guard v2 is a MONITOR (warn + keep), not a reject.
- Copy-provenance sync register (L-107); master-plan reconciliation (L-108;
  section-3a schema block partial -- authoritative pointer added).
- Design converged v0.4; docs GALLERY_DATA_SOURCE_HANDOFF v0.4 / GALLERY_BUILDER_MANIFEST v2 / GALLERY_BUILD_HANDOFF v0.1.

*New in v9:*
- Phase 0 proven: Pyodide v314.0.2 + NumPy + Plotly.js on static GitHub Pages (§5)
- Server/serverless resolved in practice: Pyodide (§7 #1)
- A/B architecture fork resolved: B′ (§5, §7 #10, measurement: 2.1-3.3 s)
- Two-tier model: frozen A exhibits + data-backed B′ exhibits (§1, §5)
- F2 canonical per-object storage adopted (§3a)
- Three trace types: actual positions, osculating at epoch, mean elements (§3a)
- Two data types to serve: osculating elements + position vectors (§3a)
- Two classes for rolling cache + spacecraft write-once (§3a)
- Phase 1b inserted: data serving pipeline (§5)
- Consent gate for Pyodide loading (§5, §7 #10)
- L-086 attribution gate ruled: JPL-only with inline credit passes (§5)
- `interactive.html` deployed as first exhibit (§2a)
- `orbit_paths.json` and `orbit_cache/` added to `.gitignore` (§3a)
- URL parameter scheme: `?exhibit=` (§2a)
- Slim self-hosted plotly wheel (~3.9 MB) in Phase 1b serving home (§5, §7 #10)

*Superseded:*
- ~~Export script reads the desktop cache~~ -> fetch fresh from Horizons (v0.4)
- ~~Subtraction / parent-composition for moon frames~~ -> osculating-primary (v4)
- ~~Monthly cadence + 90-day forward padding~~ -> nightly, horizon=0 (v0.4)
- ~~Web GUI is a fork, not a replacement~~ → gallery extension (§2)
- ~~Phase 0 is two-sided pilot: Dash + Pyodide~~ → one-sided gallery test (§5)
- ~~Two hosting substrates~~ → one: GitHub Pages, static (§1)
- ~~Per-domain desktop migration tails~~ → deferred, not on critical path (§2)

---

## §11 — Protocol & Skills Review (from Phase 0)

Phase 0 stress-tested the protocol across three models in a single day.
Detailed findings in `PROTOCOL_SKILLS_REVIEW_PHASE0.md`. Summary:

**New lessons for protocol v3.32 consideration:**
- "Measure before analyzing" — when an architectural fork hinges on a
  measurable quantity, build the measurement before the analysis.
- Frozen artifacts don't accrue sync tax — refines the parallel-pipeline
  anti-pattern.
- Consent gate as a UX pattern for unfamiliar technology.
- Provenance markers (*(est.)*, *(fetched)*) belong in relay prompts too.

**Skill updates needed:**
- `gallery-pipeline` v1.1: Option C viewer, consent gate, two-tier model,
  `interactive.html` conventions, `?exhibit=` parameter.
- Decide: separate `pyodide-interactive` skill or extend `gallery-pipeline`.

**What worked:** SHA round-trip caught real provenance errors; three-model
relay produced genuine error correction; "each round simpler" held (feared
B cost: 15-25 s → measured 2.1 s). **What to improve:** re-pull SHAs at
draft time (not just session start); mark estimates as *(est.)* in relay
prompts.

---

Base: orrery @ `ca5c052` / gallery @ `4b086a6` (remediated builder pending re-push).
Phase 0 closed. Phase 1a vocabulary delivered. A/B fork resolved: B′.
Phase 1b design converged v0.4; builder built + offline-verified (L-098).
Next: live dry-runs + first build. Solar System Explorer live at
palomasorrery.com/interactive.html.
