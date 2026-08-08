# MASTER PLAN: Paloma's Orrery Interactive Gallery

**Status:** v17 -- Phase 2 (solar system assembler) BUILD UNDERWAY. Design
handoff v0.1 -> v0.3 resolved every open question (Pluto/Charon composition,
Apophis close-encounter scope, OQ-4/closeup-shape routing). Competitive
manifest cross-check (Fable + GPT independent builds) completed two rounds
of mutual review; synthesis v2 incorporates both.
7 golden artifacts settled: Earth, Jupiter/Saturn, Moon/Io/Titan, Halley/Encke,
Voyager 1, Pluto/Charon, Halley+event_link. **Artifact 1 (Earth alone)
CLOSED** -- L-080 harness live, golden fingerprint `abbd01094852b57f`
locked, Mode 5 confirmed. F1-F4 (+ F6, non-blocking) now have ledger
handles: L-118 (F1), L-119 (F2), L-120 (F3), L-121 (F4), L-122 (F6) --
L-118 (F1) now DONE (feature_configs.json serves real ported values,
served_window populated, both proven live over --first-build AND --nightly
July 21-22); L-119/L-120/L-121/L-122 still OPEN, none built yet.
F1's own design handoff (PHASE2_F1_FEATURE_SERVING_DESIGN_HANDOFF_v0.4.md)
CONVERGED July 16, 2026, via the same competitive cross-check pattern as
Phase 2's assembler design (Fable + GPT independent manifests, comparative
review, reconciled into PHASE2_F1_BUILD_MANIFEST_v2.md) -- catching a real,
high-impact bug (planetocentric mean-motion in `propagate_marker`) GPT's
manifest missed entirely. Purpose: the existing text reads as
"handled"; this makes the caught-vs-fixed distinction explicit and
points to the handle. (Distinct from L-166, the trust-consumption item
referenced later in this section, and from L-167, an unrelated
rendering-conventions item.) See "New in v14" below.
F1a (M2, trust/served_window) fully closed July 21-22: L-149 built, tested
offline (138/138) AND live -- Layer 2 Steps 1-5 all passed (five dry-runs,
--first-build, --nightly, resolver date-picker, fetch-cost note). L-118
closed in the same session.
**Next: F1's data layer is done, but nothing renders it yet.** A repo-wide
search (Python and JS/HTML) for anything consuming `ring_system`,
`van_allen_belts`, `atmosphere_shell`, or `radiation_belts` found nothing.
Artifact 1 (Earth)'s own acceptance test confirms this by design: features
dispatch as data only, with "JavaScript rendering them" as the intended
next step -- and that JS was never written. Writing that feature-rendering
layer is the real next gate before Artifact 2 (Jupiter/Saturn) can attempt
Mode 5. Alongside it, the trust system's consumption side is now tracked as L-166
(F1b: per-object trust enforcement in the resolver + soft-edge date-picker
UX -- a deliberate golden-fingerprint re-open when it lands; the per-object
trust blocks are already served nightly, dormant). Independently: Layer 3 (nightly Task Scheduler) is ENABLED and its
core mechanism is proven -- unattended trigger, Horizons fetch, and data
assembly all confirmed working end to end -- but the final promotion step
has a known intermittent failure under the scheduler's execution context
(see S3a addendum, July 24). Watch a few more cycles before trusting it
fully hands-off.
**Base:** orrery @ `c10a424`, gallery @ `e864fd42` (design ratified here;
Artifact 1 built+pushed at orrery `6fc52b9a` / gallery `f89d83c4`; current
HEAD orrery `ee0da47c` / gallery `61a78c00` -- F1a (M2) fully closed: L-149
and L-118 both DONE, Layer 2 Steps 1-5 passed live; Layer 3 enabled with a
known open issue; L-150 (multi-orbit binaries) and L-151 (gallery-assembler
skill) still decided, not yet built)
**Date begun:** July 3, 2026
**Last updated:** August 7, 2026
**Participants:** Tony Quintanilla, Claude Opus 4.6, Claude Opus 4.8,
Claude Opus 5, Claude Fable 5, Claude Sonnet 5, GPT

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
code is archived for reference or reconstruction. The relationship with the
desktop orrery is inheritance of knowledge, not inheritance of machinery: orbital
mechanics, Horizons conventions, the established visual language (single-info-
marker pattern, AU-hover convention, barycenter-outside-primary rule) all carry
over and already show up verbatim in assembler code (render_orbits.py's info
marker matches the orrery's pattern exactly). What does NOT carry over is the
orrery's live-Horizons access -- Pyodide in the browser has no network, so the
assembler must cache a recipe once and reconstruct it later without help. Nearly
everything that has no orrery equivalent -- the staging/atomic-swap machinery,
client-side Kepler propagation, and trust measurement itself (there is no orrery
concept of "how long can we trust this snapshot," because the orrery is never
working from a snapshot) -- exists specifically because of that one constraint.
This is why the interactive gallery is worth building at all: it does something
the orrery structurally cannot -- make the project usable by anyone, without the
Python barrier.

**Rule:** new objects are authored in celestial_objects.py FIRST, then ported to
objects_config.json. Never invented fresh in the assembler. (Encke, added to the
assembler for M1/M2 comet-path testing ahead of the orrery -- confirmed absent
from celestial_objects.py as of July 20 -- is the known, deliberate exception;
closing that gap will double as a live test of the porting pipeline.) 

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

> **Addendum (July 24) — Layer 3 operational config and a known failure
> mode.** For reproducibility: Windows Task Scheduler, account `tonyq`,
> "Run whether user is logged on or not" (needs the real account password
> -- confirmed a Windows Hello PIN cannot be used for this option). Action:
> `python.exe tools/gallery_cache_builder.py --nightly --commit`, start-in
> = repo root. Concurrency: "Do not start a new instance." Daily trigger,
> time chosen for when the machine is reliably on and logged in.
>
> Known failure mode, not yet root-caused: the atomic swap (move old data
> aside, move new data in) can fail to complete its second half specifically
> under the scheduler's batch-logon execution context, even though the same
> swap has never failed running interactively. The Horizons fetch and full
> data assembly complete correctly -- a complete, valid, correctly-computed
> `coverage_index.json` was found sitting in an unpromoted `.staging_*`
> folder from a run that otherwise looked like a total failure -- only the
> final promotion into the live `data/solar-system` path doesn't land. The
> visible symptom: `data/solar-system` sits empty locally, which git reports
> as a mass deletion of every served file, indistinguishable at a glance
> from a real accidental deletion. This already happened once -- committed
> and pushed as "automatic," reverted after the fact.
>
> **The rule this establishes:** never commit a mass deletion under
> `data/solar-system` as a first response. Run the builder again first --
> its own startup recovery is built to detect and clean up exactly this
> crashed-mid-swap state, and a successful rerun makes the phantom deletion
> disappear from git's view on its own. Only investigate further if
> rerunning does NOT clear it. Suspected but unconfirmed cause: the same
> OneDrive file-lock pattern seen (and safely self-healed) in every
> interactive run this week, possibly behaving differently under the
> scheduler's account context.

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

> **Addendum (July 20):** OQ-F's frame list above is missing a fourth, real case
> -- barycenter-relative (Pluto/Charon; future Orcus/Vanth, Patroclus/Menoetius).
> The "fetch FRESH at each object's own center, no composition" ruling already
> covers it correctly: a near-equal-mass binary needing both a wide (heliocentric)
> and close (barycentric) view means TWO independent fetches, never one derived
> from the other -- same principle that retired subtraction for moons, extended
> to binary pairs. "Pluto/Charon two-view" already names this correctly: two
> self-contained scenes, not one composed scene.

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


**Track structure (added v17, Tony's ruling, August 2026 session).** Phase 2
runs in three tracks, in this order. The ordering is C-then-B-then-A in
the shorthand of the August 6-7 design session: scaffolding, then
provenance batches, then the artifact.

| Track | What | Exit condition |
|---|---|---|
| **0** | Constant layer scaffolding (L-181) | One store, provenance carried as data, display text derived, cross-repo transport working end to end |
| **1** | Provenance batches (L-156) | Batch 2 gas giants verified, on the Track 0 scaffolding |
| **2** | Artifact 2 (Jupiter/Saturn) | Golden artifact locked on verified, sourced, derived values |

**Why this order.** A golden artifact is fingerprinted. Locking one on
values that are not yet sourced and derived means redoing the lock later,
not editing a number. Scaffolding first is the cheaper order, not the
slower one. (Tony, August 2026 session.)

**This supersedes the August 5 instruction** that all provenance batches
clear before Artifact 2 proceeds. That instruction is not withdrawn --
batches still precede the artifact -- but Track 0 now precedes the
batches. Recorded as a deliberate reversal, not a drift.

**Numbering note.** "Track 0" rather than renumbering, because Section 6
already refers to "Phase 2 Track 1, Batch 1 / Batch 2" and existing
handoffs cite those numbers. Renumbering would rebase item numbers across
documents -- the leak class the ledger already carries a lesson about.
Zero means "before Track 1" and touches nothing.

**What Track 0 collapses.** Three questions stop needing separate
answers under this order: the 17 citation-level mismatches ride with the
scaffolding rather than getting 17 comment repeats; Batch 2's annotations
write into whatever citation form Track 0 establishes rather than a form
Track 0 would then migrate; and L-179/L-180 become the first thing Track
0 fixes rather than a gate standing in front of it.

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

**Opus 4.8 and Opus 5** — verification, convergence, restraint. Phase 1b design review
(July 7, 2026: caught osculating center gap, validation invariants, parent
dependency). Attribution page (fetch license terms). Vocabulary DD/OQ review
at Phase 2 start. Phase 5 restraint discipline on human-cost content.

**Sonnet 5** — predesign discovery for L-154 (the resolver bug, the
physical-radius source question) that surfaced the provenance scoring
problem; independent design review of Fable 5's provenance fix (verified
every factual claim by rerunning the tool and regrepping both repos rather
than trusting the summary -- caught the Tier-2 flood size, the
CENTER_BODY_RADII visibility gap, and two design refinements). Requested
and synthesized Fable 5's broad review-and-scoping pass on the whole
cluster (2026-07-26), which independently caught the unfixed resolver bug
still asserted as "fixed" in L-154's own resume handoff, and a false
"Phase 4 done" gap in L-163. Formalized all nine items (L-154 through
L-162) into the ledger as their own DETAIL blocks -- previously they
existed only in handoff documents -- and closed out L-114/L-120 in the
same pass, all independently re-verified against live HEAD
(`ledger_index.py --check`: clean, 160 blocks). Orchestrated and
synthesized the D3 vulnerability-ladder calibration across three
independent AI reviews (Gemini 3.1 Pro, GPT 5.5, Fable 5); Tony closed
the one remaining fork (2026-07-27). Also handling L-162 (CENTER_BODY_RADII
cleanup) as a dedicated prep session.

### Next Step

Phase 1b DONE. Nightly cache builder live; M2 (F1a trust/served_window)
tested and closed (2026-07-21) -- see documentation/TESTING_PROTOCOL.md
addendum. Phase 2 Artifact 1 (Earth) built and Mode-5 accepted; Artifact 2
(Jupiter/Saturn, rings + radiation belts) is next in the artifact order but
BLOCKED: the client-side feature-rendering JS layer it needs (L-154) is
gated behind a provenance/scoring detour that opened while scoping it (see
§6 for the full dependency chain).

Detour status as of 2026-08-01: design and ledger phases CLOSED;
**scanner Phase 1 (1a-1f) COMPLETE; Phase 2 Piece 1 (D4 scanner
mechanism) COMPLETE.**

Phase 1 built by Opus 5 across four sessions, orchestrated by Opus 4.6
(predesign) and reviewed by Opus 5. D8.5 (Option A retirement) closed as
a Phase 1 follow-on. Phase 1 measured arc (the instrument got honest):
145 -> 156 (1a) -> 156 (1b) -> 133 (1c) -> 132 (L-174) -> 171
(1d/1e/1f) -> 210 (D8.5).

Phase 2 Piece 1 (2026-08-01, Opus 5): scanner mechanism for the
V_CROSS_CHECKED (V2) rung. parse_cross_checks() parser, scoring
branches requiring source evidence AND two distinct checker annotations,
diagnostics subsection, test_cross_checked.py (16 tests). Five-model
competitive design review (GPT x2, Opus 5 x2, Fable 5) — the competitive
pattern produced genuine discovery (worksheet inventory error caught by
one reviewer only, a live false-positive regex hazard caught by another
only). Mechanism live, zero population until annotations written.

Also landed across Phase 1 + follow-ons: build_pinned_values()
citation-bleed flaw fixed; No Shadow Constants [CRITICAL] convention
added to provenance-discipline (now v1.4); shadow constants in
comet_visualization_shells.py deleted and properly imported; D8.5 Option A
retired (23 findings to Tier 1) and staleness credit removed (16 findings
to Tier 1).

Current scanner state at HEAD (373c6d8): Tier 1 210, Tier 2 605, Tier 3
62, Tier 4 2 (879 findings / 117 files).

All nine cluster items (L-154-162) have their own ledger entries. L-162
closed (CENTER_BODY_RADII naming). L-163 role side closed; domain side
deferred into the cluster.

Still open under L-156: Phase 2 Tracks 1-2, Phases 3-4.

NEXT: Phase 2 Track 1 -- complete the competitive pattern for the 15
files with April 2026 Gemini worksheets (Claude independently verifies
same claims, Tony compares, convergent claims get annotated by Opus 5).
Then Track 2 (new worksheets for uncovered files, starting with
celestial_objects.py). Then L-157/L-161 (source genuinely uncited
findings). Then L-155/L-160 (Phase 3: pinning engine and test
retirement). Once the scanner work closes, resume L-154's own open design
questions (geometry-building approach, legend behavior, artifact
sequencing -- captured in HANDOFF_gallery_feature_layer_L154_resume.md),
then build Artifact 2.

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

**L-162 — CENTER_BODY_RADII de-duplication.** ○ Not started, scoped, now
with its own ledger entry (previously design-doc only). Promote 15
remaining bodies (Mercury, Venus, Moon, Mars, Phobos, Saturn, Uranus,
Neptune, Pluto, Bennu, Eris, Haumea, Makemake, Arrokoth -- Planet 9
excluded, speculative not measured) to named constants in
`constants_new.py`, matching Sun/Earth/Jupiter's existing pattern. Values
already Gemini-verified (April 2026) -- this is restructuring, not
re-verification. Independent, can start now. Best landed before the
provenance scanner's Phase 3 pinning engine is built (L-155/156), so
pinning references named constants directly rather than needing dict-path
extraction for 15 of 18 bodies.

**L-154-162 — Provenance scoring model fix (the whole cluster).**
✓ Design CLOSED, ✓ ledger formalization CLOSED, ✓ scanner Phase 1
(1a-1f) COMPLETE, ✓ Phase 2 Piece 1 (D4 mechanism) COMPLETE,
✓ Phase 2 Track 1 Batch 1 COMPLETE, ○ Phase 2 Track 1 Batch 2 NEXT.
AMENDED v17 (Tony, 2026-08-07): Track 0 (constant layer scaffolding)
now precedes the batches. The August 5 wording is preserved below as
history -- batches still precede the artifact, but they no longer come
first. See Phase 2 track structure in Section 5.
Batch 2 is the stated gate before Artifact 2 (Tony, 2026-08-05):
all provenance batches clear before the Jupiter/Saturn artifact
proceeds.
Originally surfaced while scoping L-154's feature-rendering JS layer,
and still gates it. Design by Fable 5, reviewed by Sonnet 5;
broad-review by Fable 5 (2026-07-26). All nine items have their own
ledger DETAIL blocks. The vulnerability ladder fork closed 2026-07-27
via three-AI calibration. Full detail in L-156, L-158, and the design
handoff / design review / predesign documents.

Scanner Phase 1 (1a-1f, Opus 5, 2026-07-29 through 2026-08-01): scoring
model rebuilt. D8.5 follow-on retired Option A and staleness credit.
Phase 1 measured arc: 145 -> 210 (the instrument got honest -- false
positives fixed first, then false negatives surfaced).

Phase 2 Piece 1 (D4, Opus 5, 2026-08-01): V_CROSS_CHECKED (V2) scanner
mechanism. Five-model competitive design review. V2 requires source
evidence AND two distinct checker annotations via competitive pattern.
Mechanism live, zero population. Phase 2 Tracks 1-2 (backfill) next.

Phase 2 Track 1 Batch 1 (Claude Opus 4.6 orchestration + Opus 5 build +
Fable 5 audit, 2026-08-03 through 2026-08-04): Three-model competitive
cross-check of moon, eris, mercury, venus, pluto visualization shells +
Mars retroactive. Four verification rounds: Tier 1 sourcing, Tier 2
cross-check, follow-up, blind source lookup. 56 claims verified via
row-per-claim worksheets using Claude Opus 5, GPT-5.6 Thinking, and
Gemini independently. Results: 13 value fixes, 17 citation corrections,
3 fabricated/wrong-paper citations caught. Conventions established for
Hill sphere documentation and visualization constants. Geometry
follow-up: Fable 5 full-codebase consistency audit (16 files, ~17,600
lines) discovered radius_fraction constants not updated to match
corrected text, `<br>` in _info strings, 124 dead tooltip fields, and
up to six independent storage locations per physical value. Opus 5
built geometry + text patches (47 edits, 7 scripts). Provenance-neutral
(Tier 1: 207 -> 207). New structural items opened: L-176 (illustrated
dimensions), L-177 (Mercury Hill sphere convention), L-178-180
(Earth/solar), L-181 (single-source-of-truth constant layer).

August 4-5 cycle (Claude Opus 5 orchestration + Fable 5 skills-layer
review; landed at `2becfbf`, recorded here at `4b82384`): two ledger
items closed and the record layer brought current. L-182 -- the Mars
Hill sphere corrected to 319.2 R_Mars across all seven copies, module
and live config alike, Mode 5 confirmed. L-178 -- both EARTH_RADIUS_KM
shadow constants removed from `earth_visualization_shells.py`, so the
conversion now runs straight through KM_PER_AU; the GEO belt moved
42,212 -> 42,165 km and the LEO band now renders on its own declared
200/2000 km bounds. (The ledger title says "shadow constants" but the
affected code is LEO/GEO band geometry -- no umbra is involved.)
Protocol v3.34 ratified, with two amendments: the GitHub Desktop /
Run-button preference restated as a preference where practical rather
than a prohibition, and Stale Skill = Stop [CRITICAL] added, halting a
session outright when a loaded skill's version disagrees with its
manifest row. All ten skills bumped and reconciled across their three
stores (repo `skills/`, the generated manifest table, the account
install), with `skills_index.py` now printing what the manifest was
advertising before it overwrites it. Ledger appendix caught up with the
v3.32, v3.33 and v3.34 entries, having stopped at v3.31.

L-182 names a failure class worth carrying forward: a correction that
reaches one copy of a two-copy pair is WORSE than no correction at all.
The August 1 cross-check derived the right Mars value, but its patch
targeted the shell module only; `shell_configs.py` never received it,
and the August 4 consistency pass then harmonized the module UP toward
the uncorrected copy, erasing the fix entirely. The rule that follows:
enumerate every consumer in the same patch, and state which copy is
authoritative AND why, citing the worksheet -- never infer authority
from which copy happens to be live.

Cross-check methodology updated: the competitive pattern (same worksheet
to two models independently, Tony compares) replaces the earlier
"blind-check" framing. Both models see the claims; the discipline is
independent sourcing, not blindness to the values. Gemini stays in the
cross-check role alongside Claude. GPT as tiebreaker on divergent claims.
L-154 unblocks once the scanner work closes.

**Decisions locked 2026-07-29 (Tony).** All remaining open forks in the
cluster are resolved: L-162 naming (plain form) and scope (owns the
Sun/Earth/Jupiter fix too); the `planet_visualization_utilities.py` alias
layer (re-point to `constants_new.py`, superseding an unrecorded "v3.20
Option B"); Planet 9 excluded from pinning entirely; and the April 2026
constants verification accepted as sufficiently verified, with formal
annotation deferred to the regular Gemini sweep rather than treated as a
separate task or a Phase 2 blocker. A genuine gap was also found and
folded in: `L-158`'s frozen-literal detector is blind to copies that don't
self-announce (confirmed live in `comet_visualization_shells.py`), fixed
alongside the Phase 1 build. Three new prep items opened: `L-170`
(Tier-1 exit-code flip, previously undocumented despite D7 asking for it),
`L-171` (a `L-163` regression -- `patch_ledger_index_retired_handles.py`
landed untagged), `L-172` (a small record-hygiene batch). Nothing further
blocks a build session. **Correction:** "15 remaining bodies" reads 14
throughout this section (18 dict keys - 3 done - Planet 9 excluded = 14).

**Second correction, same day.** 66 of the cluster's 145 Tier-1 findings
turned out to be a scanner-mechanics artifact, not real citation gaps --
the scanner's 60-line lookback doesn't reach `shell_configs.py`'s
per-body-block citations (41 findings) or one two-line miss in
`jupiter_visualization_shells.py`. Fix folded into L-156's Phase 1 (string
units inherit their enclosing block's citation, landing at V3, not
automatic clearance). Post-Phase-1 Tier-1 is predicted at ~103, not 145 --
a reclassification, not new work. The Gemini worksheet L-078/L-161 sequence
now starts with the paleoclimate and sgr_a families instead of
`shell_configs.py`. Full detail: L-156 Gap item 6, L-078's note.

**Build progress, 2026-07-29: 1a landed.** Phase 1 is sub-stepped 1a-1f
for clean attribution (each step gets its own audit diff before the next
starts). 1a (D1/D2 criticality classification) is built and verified
against live HEAD `bdaaa0c`: Tier 1 rose to 156 (up from 145) -- correct,
not a regression; raising criticality can promote a previously-buried
uncited fact into Tier 1 for the first time. Two things surfaced during
the build: a role-veto amendment (ratified -- prevents devtool/gui/cache
config from misfiring as physical facts) and a third recognition gap,
distinct from the citation-window issue above -- the scanner doesn't
recognize a bare author-year citation as a citation at all, only
`# Source:`-style keywords. This makes 1d (not yet built) look like
Phase 1's largest single Tier-1 reducer, and undercuts starting the
Gemini worksheet with paleoclimate -- several of those findings are
already correctly cited. 1b is next (not 1d pulled forward -- reordering
doesn't change the final Phase 1 outcome, only invalidates predictions
already on record for no gain). Full detail: L-156's Note, this same
date.

Build progress, 2026-07-29: 1b landed. Built on ac07419, pushed at bf36743 — verified via remote HEAD match and via reason-string re-execution (post-patch audit carries the new "cited, not independently cross-checked"/"date-sensitive" reasons 565 times, the old "has source citation"/"potentially stale" text zero times). Tier 1 held exactly at 156 (the invariant L-156 predicted: the highest score reachable on the changed path is 15, one below the Tier-1 floor of 16). Tier 2 rose 181→563 and Tier 3 fell 430→60 as the former V_STALE population merged into V_SOURCED; Tier 4 fell 14→2; total conserved at 781. One 1a follow-up landed alongside: CRIT_ABSOLUTE_OVERRIDE emptied now that Phase A left CENTER_BODY_RADII with only the Planet 9 raw literal. 1c (citation-window inheritance, ~42-unit Tier-1 reduction) is next.

Build progress, 2026-07-30: 1c predesign verified. Opus 5's predesign for the citation-window inheritance fix (L-156 Gap item 6) was independently re-verified against live HEAD (657542f) rather than accepted on its tables -- every headline figure held except one internal table split (22/1 -> 21/2, same total). The predesign corrected its own earlier estimate: yield is 23 inheriting findings, not 42, and surfaced 18 genuine uncited-block gaps in shell_configs.py now tracked as L-173. idealized_orbits.py's exclusion was re-confirmed on a structural basis (zero findings inside its one cited block) rather than the original, incorrect distance argument. Approved to build directly; no design round needed. Full detail: L-156's Note this date, L-173, PREDESIGN_1c_citation_inheritance.md.

**L-163 — Module role/domain classification redesign (ROLE_MAP + MODULE_DOMAIN_MAP).**
✓ Role-side CLOSED, all 4 phases (Opus 5 + Sonnet 5, July 24-26 2026).
Design (Sonnet 5) reviewed by Fable 5, both confirmed build-ready; full
detail in ROLE_DOMAIN_CLASSIFICATION_HANDOFF.md and
AS_BUILT_L163_phase1.md through AS_BUILT_L163_phase4.md. ROLE_MAP
retired as a hand-maintained dict -- mechanically regenerated from an
explicit Role:/Domain: line in each module's own docstring
(ledger_index.py's INDEX-zone pattern, extended).

Phase 1: 7 one-time/superseded modules archived (root count 121 ->
114); ROLE_MAP's 7 ghost entries deleted (94 -> 87). Phase 2: all
orrery + gallery modules tagged, independently re-confirmed against
live HEAD. Phase 3/3a/3b: classifier code shipped and verified --
114/114 orrery + 24/24 gallery modules classify with role_source ==
'tag', zero undetermined, zero tag leakage across all 141 .py files in
both repos. Phase 4: ledger-and-session-records (-> 1.4) and
provenance-discipline (-> 1.2) rewritten off the retired hand-maintained
ROLE_MAP language; Skill Manifest and ledger index regenerated.

MODULE_DOMAIN_MAP retirement (the Domain half of this item's title) is
NOT part of the above -- deliberately deferred to the L-156 cluster,
which cites this item's coverage-gap pattern as its own precedent.

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

12. **How feature data crosses the repo boundary.** RECOMMENDED, not yet
    ratified: **fetch-and-import.** The nightly builder resolves the
    orrery HEAD SHA, fetches `constants_new.py` as text at that SHA,
    imports it, reads the feature values and their sources, validates,
    and writes into the staging cache under existing atomic-swap
    semantics. Python evaluates all derivation natively. Tony's workflow
    does not change: edit a constant, commit, push. Endorsed by Fable 5
    round 2 as "round 1's vendored pull with the exporter removed -- same
    fallback property, same SHA recording, same quarantine semantics,
    strictly fewer moving parts, and zero hand steps."
    Two earlier candidates are retired: exporting to a JSON artifact
    (rests on a generation step and a run trigger that do not exist), and
    reading the file with Python's `ast` module without executing it
    (fights the store's design -- 7 of 45 top-level assignments are
    derived rather than literal, and two contain constructor calls
    `ast.literal_eval` cannot evaluate at all).
    Trust argument, recorded because future sessions will re-ask it: the
    builder, the orrery GUI, and every patch script Tony runs already
    come from the same two repos under the same account, so importing one
    more file from it adds NO NEW TRUST ROOT. A raw fetch at a full
    40-character SHA is content-addressed, so there is no window in which
    what was checked and what was imported can differ.
13. **Generator shape and run cadence.** DISSOLVED by decision 12. There
    is no generation step -- "generation" is Tony editing the store.
    Kept as a record because two sessions built on the opposite
    assumption: `export_orbit_cache.py` is a DORMANT Phase 1b seeding
    tool. Nothing imports or calls it on any automated path; all four
    tooling maps classify it `dev_tools`; the gallery references it only
    as a historical porting source at orrery `4e2629c`. One live pointer
    remains -- `palomas_orrery_dashboard.py` line 253 advertises it in
    the launcher menu (Fable round 2). That entry, and the exporter's own
    `feature_configs.json` output, belong in a retirement note so no
    future session reads them as live.
14. ~~**L-179 and L-180 values.**~~ **RESOLVED 2026-08-07, pushed at
    `17dab34`.** Tony ruled 150,000 AU (the midpoint of the published
    100,000-200,000 AU range) and 1.1 solar radii as the DRAWN
    chromosphere shell, with the physical ~2,000 km extent stated
    alongside it. Both were closed by derivation rather than
    replacement: the ranges are stored as data
    (`GRAVITATIONAL_INFLUENCE_RANGE_AU`, `CHROMOSPHERE_PHYSICAL_KM`),
    the light-year figure derives from existing primaries, and one
    shared fragment per fact feeds every display site, so no number is
    typed. The divergent class was then enumerated rather than assumed:
    a check across all 157 Python files and 35 store constants found
    exactly three sites -- the two in L-179 and one in L-180 -- and
    reads zero after the patch. Track 0's first step is complete.
15. **Validation layers.** Four checks, each catching a class the others
    miss. (a) Source presence -- abort, not warn. (b) Unit-sanity RANGE
    checking: shape and source-presence validation both PASS on a value
    whose units changed, and only magnitude bounds catch a km-to-AU slip.
    (c) Cross-field invariant on ring geometry. **Use `inner <= outer`,
    NOT `inner < outer`.** Fable recommended strict less-than and stated
    it catches nothing spurious today; verified against the store, strict
    `<` would fire on 8 Neptune entries where inner and outer are
    deliberately equal -- narrow ringlets modelled at a single radius
    (Le Verrier at 53,200 km; six Adams arcs at 62,932 km). `inner >
    outer` is genuinely zero. A check that fires spuriously on day one is
    one people learn to ignore. (d) Nightly value-diff against last
    night's committed copy, logging every changed value with old, new,
    and both orrery SHAs -- the only guard that sees CHANGE itself, which
    is the L-182 failure family.
16. **Pilot slice inside Track 0.** OPEN, Tony decides. Fable round 2
    recommends migrating ONE body first (Jupiter, 5 entries) through the
    full Track 0 treatment and building the transport end-to-end against
    it, then scaling to the remaining 29 rings -- which under fetch-and-import
    needs zero transport rework, since new entries flow through
    untouched. The argument: the transport cannot be tested against
    today's store at all, because no `source` fields exist for
    abort-on-missing-source to act on, so "transport after Track 0"
    really means "first end-to-end test after all 33 ring entries move"
    --
    the largest possible batch before the first proof. A pilot gives
    Tony's acceptance test ("this should be minor if the architecture is
    right") its first data point at one-seventh the exposure, and
    Jupiter's descriptions contain the resistant-prose cases. Cost: two
    passes over the migration tooling instead of one.
17. **Where description interpolation happens.** OPEN. The served cache
    can hold templates plus values, with the assembler interpolating at
    render time; or pre-interpolated final strings, with the builder
    interpolating at build time. Fable recommends builder-side: it keeps
    the assembler dumb, keeps the failure surface at build time where
    quarantine already exists, and means a template error is caught
    nightly rather than in a user's browser. Either answer works, but it
    decides the cache schema, so it is decided before the schema is
    written.

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

*New in v12 (July 14, 2026):*
- Phase 2 design closed: PHASE2_ASSEMBLER_DESIGN_HANDOFF v0.1 -> v0.3.
  Pluto/Charon "composition" question dissolved -- existing orrery code,
  not new architecture. Apophis close-encounter dropped from scope --
  needs a desktop preset feature (L-046/L-104 track) that doesn't exist
  yet; replaced with a smaller artifact (Halley + event_link).
- Competitive cross-check: Claude Fable 5 and GPT each independently built
  a full manifest from the handoff. Fable's deeper builder-layer
  verification found four real gates (F1-F4) GPT's manifest didn't reach;
  GPT's cleaner module architecture and AssemblyContext proposal improved
  on Fable's version. Both completed a second-pass review of the merged
  synthesis (PHASE2_SYNTHESIS_MANIFEST v1 -> v2).
- AssemblyContext (immutable, frozen post-resolution) and view_id (closed
  enum for Pluto's two views, avoids reopening OQ-4) ratified as new
  architecture.
- Date resolution settled: served schema is one osculating-elements
  snapshot per object, not a position range (Voyager excepted) --
  propagate via Kepler's equation from M0_deg/epoch_jd, bounded by the
  served_window field (currently null at HEAD; small builder change
  needed to populate it).
- Mean elements (§3a's original "three trace types," never implemented in
  Phase 1b) completed for planets + a curated comet list (Halley,
  Ikeya-Seki), porting the orrery's existing name-keyed lookup mechanism.
  Satellites/moons explicitly excluded -- their mean-element source data
  lacks secular-rate terms and is inconsistently dated/sourced; flagged as
  an orrery-side cleanup candidate, independent of this build.
- §3a's "feature rendering always JS" reaffirmed after a synthesis draft
  briefly (and incorrectly) merged in a Python-renders-features proposal --
  caught in second-pass review, reversed.
- Four builder-layer gates found via direct code/cache verification: F1
  (feature_configs.json served empty every build -- silent data-loss trap
  for hand-authored params), F2 (event_link hardcoded None in the builder,
  AND absent from objects_config.json's schema -- two-step fix), F3
  (Halley configured but not yet in the served index -- needs a
  --first-build), F4 (slim plotly wheel not yet deployed anywhere in the
  gallery repo -- ships-nothing gate). L-086 (attribution) reconfirmed as
  a ship-gate for the new page, same as interactive.html.

*New in v13 (July 15, 2026):*
- Artifact 1 (Earth alone) BUILT and CLOSED: `gallery/assembler/` package
  (Opus 4.8, Mode 7 relay), position engine validated against Earth's
  as_of_today to machine precision, L-080 golden fingerprint
  `abbd01094852b57f` locked, Mode 5 confirmed. Full inventory and
  verification in PHASE2_ARTIFACT1_AS_BUILT.md. Served only from Tony's
  local machine (`python -m http.server`) -- GitHub Pages deployment is
  gated on F4, not on Artifact 1 itself.
- F1-F4 (+ F6, non-blocking) ledgerized for the first time: L-118 (F1),
  L-119 (F2), L-120 (F3), L-121 (F4), L-122 (F6) -- previously tracked
  only in this document and the synthesis manifest, not the ledger.
- Ledger tooling upgrade (`ledger_index.py`): the web-publication track's
  closed bucket (`W.Done`) now has its own physical destination heading in
  the DETAIL record (`### W.Done`), mirroring the general `## C.
  RECONCILED LEDGER`; the tool auto-reconciles both tag and physical
  placement for any DONE item, no Gap-phrase trigger needed. Corrected
  several items stranded or mistagged since Phase 1b: L-098, L-106, L-108
  (general C archive), L-026, L-085, L-099 (W.Done).
- Section 9 of the artifact-1 as-built mislabeled artifact 3 as
  "Mars+Jupiter+Saturn / mean elements begin" -- this document's own
  7-artifact list (above) is correct: artifact 3 is Moon/Io/Titan; mean
  elements begin at artifact 4 (Halley/Encke). Flagged; not yet corrected
  in the as-built itself.
- F1's config-shape decision closed: feature params go INLINE in
  `objects_config.json`, per-object, not a sibling file -- a second file
  is the exact two-files-must-stay-in-sync failure shape behind L-114 and
  the Halley offline-suite miss. Separately, the params themselves are
  PORTED, not hand-authored: `shell_configs.py` (`SHELL_CONFIGS`/
  `CUSTOM_SHELLS`) and the `*_visualization_shells.py` generators already
  hold provenance-audited values for every existing shell (Earth's
  atmosphere layers, Van Allen belts, etc.). Simple sphere shells port as
  direct numeric copies; custom geometry (e.g. Van Allen belts'
  procedural torus generation) needs its small generation algorithm
  ported to JS alongside its params, not just the numbers -- the same
  distinction will recur for rings and comet comae/tails later. Both
  corrected in L-118.  

*New in v14 (July 16, 2026):*
- F1 design handoff progressed v0.1 -> v0.4 (served_window/trust schema for
  the per-object trust measurement), CONVERGED. Same competitive
  cross-check pattern as Phase 2's assembler design: Claude Fable 5 (v1)
  and GPT (v0.1) each independently built a manifest from the converged
  handoff. Comparative review (Claude Sonnet 5, re-verified live against
  HEAD rather than trusting either manifest's word) found Fable's manifest
  caught a real, high-impact bug GPT's missed entirely: `propagate_marker`
  (`gallery/assembler/render_orbits.py`) derives mean motion as
  `n = K_GAUSS / a**1.5` with `K_GAUSS = sqrt(GM_sun)` -- correct for
  heliocentric bodies, wrong by ~3 orders of magnitude for planetocentric
  ones (moon, io, titan, charon). Verified by direct arithmetic: the
  Moon's real sidereal period is 27.3 days; the unfixed formula computes
  ~68 minutes.
- Schema-naming question (the manifest's FLAG-1) resolved by recovering
  the actual settled v0.2 decision from this session's own working files,
  unreachable by either AI: served config fields mirror the orrery's own
  source dict shapes exactly (`atmosphere`/`upper_atmosphere`,
  `inner_belt_distance`/`outer_belt_distance`/`belt_thickness` with no
  invented unit suffix, ring keys copied near-verbatim from each source's
  own `ring_params` dict).
- Partial-measurement-failure semantics (FLAG-3) resolved by Tony's direct
  call: if any participating object's trust measurement fails, the global
  `served_window` is served `null` (with a warning), not computed as a
  minimum over survivors only -- a wrong-but-present bound is invisible to
  the resolver; null is visibly degraded.
- `PHASE2_F1_BUILD_MANIFEST_v2.md` reconciled from Fable's manifest as
  base (the mean-motion fix built in), GPT's stop-condition list and
  implementation-report template grafted in, schema section rewritten to
  the recovered settled convention.
- Tangential citation-provenance finding surfaced while rewriting the
  ring/belt sections: Jupiter's existing `ring_params` citation ("NASA
  Jupiter Ring Fact Sheet") was being read, per the project's own "unit of
  provenance" convention, as also covering ring COLOR values -- Tony
  judged this an overstatement; ring/belt colors across the codebase are
  developer/AI aesthetic picks, inconsistent in method, not measured.
  Resolved at the provenance-scanner + report level rather than per-file
  edits: L-124 (deferred wishlist for a real color-accuracy pass, NASA/
  Cassini sourcing captured for later) and L-125 (the scanner and
  `PROVENANCE_AUDIT.md` now carry a standing disclosure that color values
  are excluded from citable claims project-wide -- documentation only, no
  scoring change, tier counts unchanged at 673/102/155/396/20).
- Manifest handed to Opus for the actual F1 build July 16, 2026
  (`OPUS_BUILD_PROMPT_F1_v1.md`); orrery re-pinned `13acfcf4`, gallery
  unchanged `953c650e`.

- **Sonnet 5 + Tony, Layer 2 live-Horizons testing** (July 20, 2026): M2 (F1a
  trust/served_window) verified against real Horizons for 5 objects. Surfaced
  and resolved: Pluto's category-based trust-participation bug (L-149, decided:
  key off canonical_frame); the general multi-orbit requirement for near-equal-
  mass binaries (L-150); confirmed no test coverage of participant-set
  membership existed before tonight. Design discussion clarified the orrery/
  assembler boundary and corrected an initial mis-framing of the fix as
  requiring frame composition -- it doesn't; independent per-center fetch was
  already the settled v0.4 principle. gallery-assembler skill decided (L-151).   

- **Sonnet 5 + Tony, F1a (M2) full closure** (July 21-22, 2026): L-149 fix
  proven end to end -- offline suite grew to 138/138 (4 new checks, including
  a forced-failure test proving Pluto's exclusion isn't vacuous), then
  confirmed on real Horizons data across a full --first-build AND --nightly
  (Apophis controls the global served_window at 323.55 days; Pluto/Charon
  measured but correctly take no part). Step 4 confirmed the existing
  resolver reads the newly-populated field correctly both directions.
  L-118 closed the same session: feature_configs.json confirmed serving
  real ported values (Earth atmosphere/Van Allen, Jupiter rings/radiation
  belts, Saturn's 7-ring system) instead of the empty stub. Both L-118 and
  L-149 flipped to DONE. Testing record consolidated into a clean
  M2_TESTING_PROTOCOL_ADDENDUM.md. New finding, not yet ledgerized: the
  feature-rendering JS side of F1 doesn't exist anywhere in the repo --
  data is served correctly but nothing draws it, so Artifact 2
  (Jupiter/Saturn) is blocked on that rendering work, not on data, going
  into the next session.

*New in v15 (August 4, 2026):*
- L-156 Phase 2 Track 1 Batch 1 COMPLETE. Three-model competitive
  cross-check (Claude Opus 5, GPT-5.6 Thinking, Gemini) of five shell
  visualization modules (moon, eris, mercury, venus, pluto) plus Mars
  retroactive corrections. Four verification rounds: Tier 1 sourcing,
  Tier 2 cross-check, follow-up, blind source lookup. 56 claims verified,
  13 value fixes, 17 citation corrections. Conventions established for
  Hill sphere (perihelion distance, system mass for binaries),
  visualization constants (best-sourced single value for code, range in
  description), and retired "Verified: April 2026" annotation format.
- Fable 5 full-codebase consistency audit across all 15 shell modules +
  shell_configs.py (~17,600 lines). Discovered: (a) Batch 1 corrected
  display text but left radius_fraction geometry constants at old values;
  (b) 95 of 126 module _info strings use `<br>` tags rendered literally
  by the Tk GUI; (c) 124 dead `tooltip` fields in SHELL_CONFIGS/CUSTOM_SHELLS;
  (d) up to six independent storage locations for one physical value;
  (e) Saturn (fully migrated to the reference pattern) carried the audit's
  worst finding -- proving the pattern alone doesn't prevent drift.
- Opus 5 geometry + text follow-up: 7 patch scripts, 47 edits. Geometry
  corrections for Mercury, Moon, Venus, Eris (radius_fraction to match
  cross-checked values). `<br>` -> `\n` for moon, eris, pluto, mars.
  Mercury mantle diamond claim removed. Stale headers corrected. Mars
  dead copies updated. Opus 5 self-flagged its own Batch 1 error:
  Mercury Hill sphere rf 94.4 matches neither perihelion (71.85) nor
  semi-major (90.45) convention -- tracked as L-177.
- Six new L-items from the audit: L-176 (illustrated dimensions in shell
  hover text -- make the render self-documenting), L-177 (Mercury Hill
  sphere convention error), L-178 (Earth shadow constants), L-179 (solar
  gravitational influence 150k vs 126k AU), L-180 (solar chromosphere
  three extents), L-181 (single-source-of-truth constant layer design --
  the structural fix for the dual-pipeline drift the audit surfaced).
- Scanner state: Tier 1 207 -> 207 (provenance-neutral). Batch 2 (gas
  giants) is next, directly unblocking Artifact 2.
- Re-measured at `4b82384` on 2026-08-05 by a live scanner run, not
  carried: 877 findings across 118 files -- Tier 1 206, Tier 2 581,
  Tier 3 88, Tier 4 2. The 207/580/117 figures above were measured
  before the August 4-5 patches landed; one finding moved Tier 1 ->
  Tier 2. Recorded as a reminder that a number quoted in a handoff
  can predate that handoff's own anchor.

*New in v17 (August 7, 2026):*
- **Phase 2 track structure added, and Tony's ordering ruling recorded.**
  Track 0 (constant layer scaffolding) precedes Track 1 (provenance
  batches) precedes Track 2 (Artifact 2). Reasoning: a golden artifact is
  fingerprinted, so locking one on unsourced values means redoing the
  lock. Supersedes the August 5 "clear all batches first" instruction,
  which is preserved as history rather than deleted.
- **L-181 promoted out of Prep Work into a phase track.** As reframed on
  August 6-7 it carries one store, a citation-form migration, derivation
  across five restatement surfaces, a generator, a cross-repo transport,
  and a load-time validation pass. That is phase-scale work, and leaving
  it in Section 6 was why the August 6-7 design session kept expanding --
  implementation questions were being answered against no scope boundary.
- **Six open decisions added to Section 7** (12-17): transport form,
  generator shape (dissolved), the L-179/L-180 values, validation layers,
  pilot-slice sequencing, and the interpolation locus.
- **Two Fable 5 design reviews, August 2026** (round 1 at orrery
  `ee0da47c`, round 2 at `754f46b`; zero code in either). Architecture
  endorsed in round 1; transport endorsed in round 2. All findings from
  both rounds independently verified by Claude Opus 5 at the review
  anchors before being recorded.
- **Round 1 findings the predesign handoff missed:**
  `spectral_subclass_temps` is an uncited physical claim inside the store
  itself, so the convention must apply at home before it is enforced
  outward; `KNOWN_ORBITAL_PERIODS` carries the key `'Phobos'` twice (133
  keys, one duplicate, same value today) -- Python silently keeps the
  last, which is the argument for a validation pass; the module-level
  `*_info` tooltip strings are a FIFTH restatement surface (Uranus
  restates 25,559 km nine times and does arithmetic in prose), and had
  derivation covered dict descriptions but not these, the `*_info`
  strings would have become the surviving duplicate -- L-182's exact
  shape, which the build was on course to recreate; and the gallery
  constant enumeration missed four sites including three BARE literals
  `149597870.7` inline in `gallery_studio.py`.
- **The transport question was reopened after round 1 by Tony
  questioning three premises this session supplied and never checked.**
  (1) "The exporter" was written as though pointing at something live; it
  is dormant. (2) The store's 7 derived constants were written up as a
  complication; they are the store's own stated principle working, and
  `SOLAR_RADIUS_AU` alone has 11 consumers. (3) The claim that the
  gallery could not execute the file was never tested; `constants_new.py`
  imports only numpy and `datetime`, and the builder already hard-depends
  on numpy through astroquery. Each error was Claude reading code and
  treating that as knowing the system. Removing the premises produced
  fetch-and-import, which is simpler than everything that preceded it.
- **Round 2 findings.** `numpy` and `timedelta` are imported by
  `constants_new.py` and never used -- Track 0 should drop both, making
  the store stdlib-only and removing the version-skew surface between the
  two environments. A pre-import gate is recommended: parse the fetched
  file with `ast` and check exactly two structural properties -- imports
  on an allowlist, and no duplicate dict keys -- then hand off to import
  for everything else. That recovers the one capability fetch-and-import
  loses, since after import Python has already silently kept the last
  duplicate and the Phobos class becomes invisible. Track 0 should also
  define a single-name contract, `FEATURE_REGISTRY`, that the builder
  reads and nothing else; every rename or regrouping inside the store
  then stays internal, and the only breaking change left is renaming the
  registry itself.
- **Correction to a round 2 recommendation, verified against the store.**
  Fable recommended a strict `inner_radius_km < outer_radius_km`
  invariant and stated it catches nothing spurious today. It would fire
  on 8 Neptune entries where inner and outer are deliberately equal --
  narrow ringlets modelled at a single radius. Use `inner <= outer`. The
  directional claim holds: `inner > outer` is genuinely zero across all
  33 ring pairs.

**Count corrected 2026-08-07.** An earlier "37 entries" figure appeared
once in this document, unsourced, alongside "33 ring pairs" elsewhere.
Enumerated by AST walk at `9b4f278`: 33 ring entries -- Jupiter 4,
Saturn 7, Uranus 11, Neptune 11. Jupiter is 4, not 5. Separately, the
radiation belt and plasma torus geometry is roughly 22 more physical
values in four different shapes, held as bare literals in function
bodies and counted in neither figure. See L-181 and L-190.
- **Coupling requirement recorded as a Track 0 exit criterion in L-181**
  rather than as its own ledger item, per Tony: do not multiply handles.
- Scanner console now prints the per-domain split under each tier line,
  and `MODULE_DOMAIN_MAP` covers `orrery_rendering` and `shell_configs`
  explicitly (L-184, Task 2a, landed `5a56473`). Domain coverage-gap note
  cleared; totals unchanged at 877 / 117 files / 206-581-88-2.
- Ledger items opened this cycle: L-184 (build-path gate), L-185
  (assembler source discipline), L-186 (cross-check annotation issues),
  L-187 (info_dictionary numeric-overlap enumeration).

*New in v16 (August 5, 2026):*
- L-178 and L-182 CLOSED, both Mode 5 confirmed by Tony. Mars Hill
  sphere corrected to 319.2 R_Mars across all seven copies (L-182);
  Earth LEO/GEO band geometry freed of its two duplicate
  EARTH_RADIUS_KM shadow constants (L-178).
- New failure class recorded (see §6): a correction reaching one copy
  of a two-copy pair is worse than no correction, because the next
  consistency pass harmonizes toward the uncorrected copy.
- Protocol v3.34 plus the ten-skill reconciliation across three stores.
  Amendments: the git-GUI preference ruling, and Stale Skill = Stop
  [CRITICAL].
- **The push gate changes for this phase (Tony ratified 2026-08-05).**
  "Tier-1 = 0" becomes **"Tier-1 = 0 on the interactive build path."**
  The global gate was unreachable in practice: of 206 Tier-1 findings
  measured at `4b82384`, 105 sit in the Earth System domain, a
  subsystem Artifact 2 never touches. A gate nobody can reach stops
  functioning as a gate. The path is NAMED explicitly and COMPUTED
  rather than listed -- build-path membership is derived by walking the
  import graph from a small set of declared orrery-side entry points,
  which `dep_trace.py` already does, because a third hand-maintained
  module map would be a third store that drifts. The Earth System
  remainder gets its own L-item and its own schedule; deferring it does
  not endanger the interactive build.
- The gate is built BEFORE the batches it scopes (Tony's correction,
  2026-08-05). Deferring the definition of a gate to a later L-item is
  the same category error as deferring the gate.
- Scanner re-measured at `4b82384` by a live run, not carried: 877
  findings across 118 files -- Tier 1 206, Tier 2 581, Tier 3 88,
  Tier 4 2. Domain split of Tier 1: Earth System 105, orrery 91,
  stars 9, utilities 1, dev tools 0, gallery 0.
- Artifact-2 path measurement at the same SHA, per file:
  `shell_configs.py` 23 Tier-1, `idealized_orbits.py` 26,
  `planet_visualization_utilities.py` 4,
  `saturn_visualization_shells.py` 1,
  `uranus_visualization_shells.py` 1, `orrery_rendering.py` 1,
  `jupiter_visualization_shells.py` 0,
  `neptune_visualization_shells.py` 0 -- 56 across the named files.
  Two consequences worth stating plainly: the gas giant shells are
  ALREADY nearly clean, so Batch 2's job on those four files is VALUE
  VERIFICATION rather than Tier-1 clearance; and Artifact 2 is
  therefore not blocked by scanner debt in the shells themselves.
- Batch 2 (gas giants) is the stated gate before Artifact 2 -- all
  provenance batches clear first (Tony, 2026-08-05).
- L-176 scope boundary recorded so the item is not oversold later:
  illustrated dimensions catch CONSTANT-VS-TEXT drift, not values that
  are internally consistent but wrong. Mars drew exactly the 324.5
  R_Mars its text claimed, and both were wrong. Complementary to the
  provenance cross-check, not a substitute for it.
- Domain coverage gap confirmed live: `orrery_rendering.py` and
  `shell_configs.py` carry findings but have no MODULE_DOMAIN_MAP entry
  and silently default to `orrery`. Both are on the Artifact-2 path, so
  the single most important file in the gate would otherwise land in
  the pile by accident. Fix in the same pass that adds the domain split
  to the console output. Naming note for whoever greps for it: the
  audit's section is titled "Findings by File Type", not "Findings by
  Domain".

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

Base: orrery @ `ee0da47` / gallery @ `61a78c0` (v17; v16 was orrery
`4b82384` / gallery `e7e8c5e`; v15 was orrery
`b59cb72` / gallery `22c947c9`).
Phase 0 closed. Phase 1a vocabulary delivered. A/B fork resolved: B′.
Phase 1b builder built, offline-verified (L-098), and Layer 2 live-Horizons
fully tested and closed -- L-149 and L-118 both DONE; L-150/L-151 still
decided, not built.
Scanner detour: Phase 1 (1a-1f + D8.5) COMPLETE. Phase 2 Piece 1 (D4
scanner mechanism) COMPLETE -- V2 rung live, zero population. Phase 2
Track 1 Batch 1 COMPLETE -- three-model competitive cross-check of 5 shell
modules + Mars, geometry follow-up, Fable consistency audit. Phase 2
Track 1 Batch 2 NEXT: gas giants (jupiter, saturn, uranus, neptune)
-- and the stated gate before Artifact 2. Push gate for this phase:
Tier-1 = 0 ON THE INTERACTIVE BUILD PATH, with the path computed from
the import graph rather than listed by hand. The gate gets built
before the batches it scopes.
New structural items from Fable audit: L-176 (illustrated dimensions in
hover text), L-177 (Mercury Hill sphere convention), L-178-180
(Earth/solar inconsistencies), L-181 (single-source-of-truth constant
layer). Skill updates LANDED 2026-08-05: all ten skills bumped and reconciled
across repo, manifest, and account install --
orrery-coding-conventions 1.3, provenance-discipline 1.7,
ledger-and-session-records 1.5, safe-file-editing 1.2,
agentic-pre-test 1.2, gallery-pipeline 1.2, gallery-assembler 1.1,
gallery-cache-builder 1.2, horizons-orbital-mechanics 1.1,
earth-system-pipeline 1.1. Protocol at v3.34.
Next after scanner work: write the feature-rendering JS layer
(ring/shell/belt consumers) -- that's what stands between here and
attempting Artifact 2 (Jupiter/Saturn) Mode 5. Layer 3 (nightly Task
Scheduler) enabled with known intermittent promotion-step glitch (S3a
addendum, July 24).
Solar System Explorer live at palomasorrery.com/interactive.html.
```
