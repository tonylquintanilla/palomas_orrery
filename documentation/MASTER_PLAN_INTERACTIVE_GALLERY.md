<!-- Doc-Kind: hand | The strategy for the interactive gallery: what the website is for, how it is built, and where the work goes over months. The order of the work is the road on WHERE_WE_ARE.md; status is the ledger's. -->
# MASTER PLAN: Paloma's Orrery Interactive Gallery

## Executive summary -- v36, October 14, 2026

Built on orrery `9248845ca8516dcee3498f07c554e6a24426c23c` at
https://github.com/tonylquintanilla/palomas_orrery and gallery
`86ef2df6313f956f5c9e49611e6a2bdd0e95da29` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, read live
on 2026-10-14. This summary is rewritten at every restamp, never
carried forward.

**What this plan is, and what it is not.** It is the strategy for the
interactive gallery at palomasorrery.com: what the website is for, how
it is built, and where the work goes over months. It does not say what
is next. The order of the work lives in one place only, the road on
`documentation/WHERE_WE_ARE.md`. What is done, and what was ruled, is
the ledger's. Read this plan when a decision changes direction, when a
new kind of work opens, or at a restamp. (Tony's ruling, 2026-10-13.)

**Seven kinds of document** (Tony, 2026-10-13; the full statement, with
when each is read, is in the skill ledger-and-session-records):
1. Strategy: this plan. Where the work goes over months.
2. Tactics: Where We Are, and the road on it. What is next, in order.
3. Communication: briefs, design records, manifests, handoffs, review
   prompts and Tony's run records. Each carries work from one session,
   person or model to another.
4. Logistics: the ledger. Every job's history and the open work
   orders. Never a schedule.
5. The field manual: the protocol and the skills. How we work together.
6. Reference: generated documents read for the current state, such as
   the module atlas and the provenance audit.
7. The work: the code builds. The render is its ground truth; the SHA
   is its state.

**The end goal** (Section 5a). The website does what the desktop
orrery does, for anyone, with nothing to install, and with a date to
choose within the range the data covers.

**Where the work stands, by the five segments of Section 5a.**
- Segment 3, the website draws: done. Three rooms are live: the Sun
  (2026-08-29), Earth (2026-09-10), and the Solar System room, the
  gallery's front door. Each was accepted on Tony's phone and desktop.
- Segment 2, the numbers reach the website without a hand copy: done.
  The orrery exports its constants and its objects, and the website
  pulls both. The newest are the orbital periods: JPL's own, in the
  orrery and on the website since 2026-10-14.
- Segment 1, the orrery's numbers are right: worked room by room, never
  as one sweep. Earth is the first closed slice (2026-09-22). The Sun's
  is open.
- Segment 5, shipping: the three rooms are shipped. The Solar System
  room becomes the page a bare link opens once every room it leads
  into prints only served numbers.
- Segment 4, Jupiter and Saturn's golden artifact: no longer next. It
  falls in the shells phase, after the orrery's objects reach the
  website.

**The direction** (Tony, 2026-10-10 and 2026-10-12; L-433). Section
5a, The direction, has the paragraph. In short: finish the Sun and
Earth rooms, with the Solar System room's features, as the template
for every body's room; bring the rest of the orrery's objects to the
website; then the inner planets' rooms, with the Earth System layers
beside them.

**Signals, read from files.** Last cache build: 20261014T225537Z,
swapped in first time (gallery `data/cache_swap_log.jsonl`). Tier-1 on
what leaves the orrery: 0 (`PROVENANCE_AUDIT.md`). Whole tree: 280:
orrery 116, Earth System 149, stars 13, utilities 2.

**How to read the rest.** Sections 1 to 4 are the architecture.
Section 5 is the phases. Section 5a is the shape of the work: the end
goal, one pipeline in one direction, the five segments, the braid and
the direction. Section 6 is the prep work and Section 7 the
architectural decisions, both with their history. The plan's dated
history moved out on 2026-10-14 to
`documentation/MASTER_PLAN_HISTORY.md`: the critical path's session
record from August 23 to September 29, 2026, and the lineage (formerly
Section 10). The status block below is the running record the
restamps kept from July to v35; it is not updated.

---

**Status:** v35 -- Phase 2 (solar system assembler) BUILD UNDERWAY;
**the first feature-bearing exhibit is LIVE AND COMPLETE.** The Sun
ships at `palomasorrery.com/interactive.html?exhibit=sun`, unlinked
from the landing page, Mode 5 accepted 2026-08-29 (gallery
`ac9a5c7b`). Its GUI (L-267) is complete on desktop as of 2026-09-03
(gallery `98cc99bd`): a drawer replaces the legend, cross markers and
rows move the camera, and the i panel follows the focus and carries
each shell's curated link (L-265, DONE). The phone pass is DONE as of
2026-09-06, and the frame HUD with it (L-289, closed on Tony's Mode
5). **The second exhibit, EARTH, is LIVE AND COMPLETE** (L-291, closed
2026-09-10 on Tony's Mode 5): `interactive.html?exhibit=earth`,
shells plus the Moon, arriving at low Earth orbit -- eleven sourced
features, the axis, the Sun line and terminator, and the Moon on its
trusted arc -- with its card featured in the lobby (gallery
`57fd93c6`). Its magnetosphere, absent and named at launch, has been
drawn from the store since 2026-09-15 -- Shue's magnetopause and
Jelinek's bow shock (L-305). **Since 2026-09-22 Earth is the first
CLOSED SLICE of the store** (L-322 Stage C2): every number its room
prints comes from `constants_new.py` at the figure count its row
declares, and every measured row behind a served number records who
read its source. Earth made the rooms a TABLE, `EXHIBITS` in
`interactive.html`, one row per room, and it found L-168, the
planetocentric mean-motion bug, on the first moon it drew.
**The braid, ruled 2026-08-22:** provenance stops being a GATE and
becomes a per-artifact slice, and the rendering layer is worked first.
The five segments of Section 5a do NOT move; the order they are worked
in does. Argument in
`documentation/DESIGN_NOTE_20260822_braid_and_citation_kind.md`
Section 1. Design
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
July 21-22); L-120 (F3, Halley in the served index) DONE 2026-07-27;
L-119, L-121 and L-122 still OPEN.
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
**Next: the order lives on the road on `documentation/WHERE_WE_ARE.md`
(v36, Tony's ruling of 2026-10-13; until v36 this line named Section
5a's newest subsection).** The five-step order dated 2026-09-03 -- the Sun room's phone
controls, the lobby with its rooms and editor (L-282, L-286, L-287;
the hall, L-280, was retired 2026-09-04), Earth into the assembler, the
transport (segment 2) built alongside Earth, then Jupiter and Saturn --
stands in its own subsection as it was written. The paragraph that stood here until v22 said the
feature-rendering JS layer was "never written" and was the gate before
Artifact 2. That layer is `feature_renderers.js`; it shipped with the
Sun exhibit on 2026-08-29 and has drawn 18 shells on the live page
since. The sentence outlived the fact by five days and two plan
versions -- The Correction Does Not Travel, on this document's own
front page. Alongside the order, the trust system's consumption side is tracked as L-166
(F1b: per-object trust enforcement in the resolver + soft-edge date-picker
UX -- a deliberate golden-fingerprint re-open when it lands; the per-object
trust blocks are already served nightly, dormant). Independently: Layer 3 (nightly Task Scheduler) is RETIRED as of
2026-08-10 (Tony). The task is DISABLED, not deleted, and the builder now
runs manually with Tony committing the result himself. His reasoning: the
build cannot run without his machine on anyway, so the schedule created an
appearance of automation the setup could not deliver -- three nights were
missed in the week before the ruling and the failure was silent. Running
it by hand also dissolves the surprise behind the August 10 gallery
incident, because a build in flight is no longer something he can walk
into unaware. First manual build ran clean end to end on 2026-08-11
(gallery `d5437f0`).
The layer's history is kept because it becomes live again the moment the
build runs unattended by ANY mechanism, including a GitHub Action: its
core mechanism was proven -- unattended trigger, Horizons fetch, and data
assembly all confirmed working end to end -- but the final promotion step
had a known intermittent failure under the scheduler's execution context
(see S3a addendum, July 24).
**Base:** orrery @ `38923c1`, gallery @ `493a0bd` -- v19 was BUILT on
those and PUSHED at orrery `f504c06` / gallery `02aefc0` on 2026-08-23.
(Both bases confirmed against the live remote, not carried forward.
Design ratified at orrery
`c10a424` / gallery `e864fd42`; Artifact 1 built+pushed at orrery
`6fc52b9a` / gallery `f89d83c4`; v18 stood at orrery `ee0da47c` /
gallery `61a78c00`. F1a (M2) fully closed: L-149 and L-118 both DONE,
Layer 2 Steps 1-5 passed live. Layer 3 RETIRED 2026-08-10 -- the v18
text here read "enabled with a known open issue", contradicting its own
header forty lines below. L-151 (gallery-assembler skill) DONE
2026-07-27; L-150 (multi-orbit binaries) still decided, not yet built.)
**Date begun:** July 3, 2026
**Last updated:** October 14, 2026 (v36: a DOCUMENTATION build, L-442,
at Tony's direction. The plan becomes strategy only, on his ruling of
2026-10-13: the road on Where We Are carries the order and the ledger
the status. The executive summary is rewritten; Section 5a keeps the
shape and gains The direction (L-433); the dated history of the
critical path and the lineage (Section 10) move to
`documentation/MASTER_PLAN_HISTORY.md`, on Tony's ruling of 2026-10-14;
Sections 6 and 7 get one pass against the ledger; with Anthropic's
Claude Opus 5.5. v35, September 29, 2026: a DESIGN BUILD, L-363. The
Solar System room becomes the gallery's front door (the design session
of 2026-09-29), and the order changes on Tony's ruling C: the room's
second half through his Mode 5 first, then the Sun's slice, then the
swap that makes the room the default. After the Sun, in outline: the
orrery's objects rebuilt in the gallery from its own dictionary and
checked against Horizons, then encounters, then shells and slices. The
executive summary is rewritten and Section 5a gains the 2026-09-29
subsection; with Anthropic's Claude Opus 5.5, from a review Claude
Fable 5.1 did in parallel. v34, September 28, 2026: a DESIGN BUILD, L-345,
which finished L-322 Stage D. A value in another unit is computed from
its one source row and never stored as a second row: the orrery
exports each row's value in every length unit as "in" (patch D19),
the gallery prints from it (gallery `52da593c`), and the store's
fifteen conversion rows became names computed from their rows (patch
D20). Earth's crust is drawn at the mean radius. The plan gains an
executive summary and absorbs its two companions, which are retired;
Section 5a gains the 2026-09-23 to 28 subsection; with Anthropic's
Claude Opus 5.5.)
**Participants:** Tony Quintanilla, Claude Opus 4.6, Claude Opus 4.8,
Claude Opus 5, Claude Opus 5.5, Claude Fable 5, Claude Fable 5.1,
Claude Sonnet 5, Claude Sonnet 5.5, GPT

**Pivot (v8):** The gallery is no longer a stepping stone to a separate web
application. The gallery IS the web publication -- growing interactive
controls incrementally, like a science museum adding hands-on exhibits to a
permanent collection.

---

## Section 1 -- Architectural Constraints (settled)

These are not options. They are facts that constrain every downstream decision.

**The site never fetches Horizons.** JPL terms require one request at a time and
prohibit website embedding (NASA CORS policy). The cache is the entire served
surface.

**Three-tier cache, all offline-populated (orrery domain):**

- Tier 1 -- Scheduled standard catalog. Sequential batch job refreshes a fixed
  set of object/center pairs, rolling the date window forward. Size-stable.
- Tier 2 -- Curated specials, define-once. Encounters, perihelia, close
  approaches. Write-once/read-forever. Fetched by Tony via the desktop app.
- Tier 3 -- User requests, manually curated. Tony produces and caches offline;
  the user is notified when ready. Whether fulfilled requests persist in the
  shared cache is a dial Tony sets (see Section 7).

**The gallery is the delivery platform.** The existing gallery on GitHub Pages
(`tonyquintanilla.github.io`) is a working static site that already renders
Plotly 3D figures on every device including phones. It has navigation,
narrative sections, categories, and a curator's workflow (Gallery Studio). The
web publication extends this -- it does not replace it.

**The JSON bridge.** Pre-curated gallery cards and interactive gallery pages both
produce the same artifact: Plotly JSON. One path is pre-baked by Tony on the
desktop, shipped as a `.json` file. The other path is assembled live in the
browser from user selections via Pyodide. The gallery viewer renders both
identically. This is the unifying architectural principle.

**The GUI declares the envelope.** A cache miss is something the UI will not let
you request -- not a runtime error, not a silent wrong plot. Coverage is a
visible, honest boundary. The coverage index tells the interactive page which
combinations are available; the page shows only those options.

**Pyodide for client-side computation.** When a user selects planets and dates
and the assembler runs, it runs in their browser via Pyodide (Python compiled
to WebAssembly). No server. The gallery stays a static site on GitHub Pages.
Pyodide loads from CDN, the assembler and orbit cache are static files in the
repo. **Phase 0 confirmed Pyodide is acceptable** (2.1-3.3 s cold-start on
iPhone WiFi, including plotly via micropip). The B' architecture (shared
desktop engines running in Pyodide) is the Phase 2 path. Frozen pedagogical
demos (like the Phase 0 Solar System Explorer) stay on the lightweight A path
(NumPy only, JS figure builder) -- a two-tier model.

**Assemblers read cache through the coverage-index abstraction from day one** --
never by opening data files directly -- so cache restructuring cannot break
the assemblers. The coverage index is a **solar system concept** where the
envelope is complex (object/center/date-range matrix). Other domains declare
their bounds simply: stars state distance and magnitude limits, orbital
parameters are always available, Earth system lists available scenarios.

**GitHub Pages hosting.** The gallery is 439 MB against Pages' 1 GB ceiling,
with ~585 MB of headroom (measured at gallery `493a0bd`, 2026-08-23;
~436 MB post-cleanup in July 2026). This is the document's ONE size
figure -- Section 3a used to carry a second, disagreeing one. The largest remaining
files are pre-refactoring exports that will shrink further when re-exported
with the current slimmer plotting functions. Headroom is shared between
gallery growth, cache data, and the Pyodide assembler code. A separate Pages
project site (each gets its own 1 GB) is an option if space tightens. R2
graduation for large files (star cache, orbit cache) is a dial.

---

## Section 2 -- Gallery Extension Architecture (replaces v7 "Fork Decision")

**The gallery grows interactive; the desktop stays as-is.**

The desktop tkinter app continues as the power-user creation tool -- live
Horizons, animation export, KML/KMZ, Gallery Studio. The web publication is
the gallery gaining new interactive pages, not a fork of the desktop GUI.

**The science museum model.** The gallery is the exhibit hall. Pre-curated cards
(today's content) are the permanent collection -- beautiful, informative, no
computation required to view. Interactive pages are the hands-on science center
-- the user walks up, makes selections, and sees the result. The curated
collection loads instantly (pre-computed JSON). The interactive exhibits load
after Pyodide initializes (5-15 seconds on first visit, cached after).

**Incremental delivery.** Each interactive page is a shippable increment:
"This week, planet selection and dates for static solar system views. Next
month, comet encounter presets. Later, star visualization with magnitude and
distance controls." Every step is useful on its own. No big-bang deployment.

**What this replaces.** The v7 plan called for forking the desktop GUI into a
web GUI (Dash or Pyodide), presenting 95 widget inputs on a web page, and
resolving a server-vs-serverless decision via a two-sided pilot. That approach
asked the wrong question -- "how do we shrink the desktop onto a phone" -- when
the right question was "what does a phone user want?" The answer is what the
gallery already does, plus the ability to change what's plotted.

**Shared computation layer -- verified at HEAD (`d6c8c42`, unchanged at
`fdb66ca`):**

Six modules are import-clean (zero tkinter references): `idealized_orbits.py`,
`planet_visualization.py`, `visualization_utils.py`, `orbit_data_manager.py`,
`constants_new.py`, `shell_configs.py`.

**Two named seams (same as v7):**

1. `celestial_objects.py` -- data half (`OBJECT_DEFINITIONS`) is import-clean.
   Selection/instance half is tk-shaped. The gallery imports the data; it
   supplies its own selection-state injection.

2. `palomas_orrery_helpers.py` -- carries computation the assembler will
   want. **L-087 CLOSED 2026-07-15 and the file no longer imports tkinter
   at all** (measured at `38923c1`: zero references; all three functions
   the assembler needs are present). The seam survives in a different
   shape: three modules in its TRANSITIVE import closure still import
   tkinter -- `osculating_cache_manager`, `save_utils`, `shutdown_handler`.
   So the constraint is real and the reason v18 gave for it was not.

**Desktop migration is deferred, not abandoned.** Over time, the desktop could
refactor to use the shared assembler, unifying both paths. But this is an
efficiency improvement, not a web publication blocker. The critical path is:
assembler -> gallery interactive page -> ship it.

---

## Section 2a -- Gallery Viewer Refactor (Option C -- Hybrid)

**Two pages, not one; not N.**

`index.html` stays as-is -- the "dumb renderer" that loads pre-computed JSON
and calls `Plotly.newPlot()`. It continues to serve curated cards with zero
changes to the existing pipeline (Studio -> converter -> viewer). The WYSIWYG
principle is untouched for curated content.

A single new `interactive.html` handles all interactive exhibits. The exhibit
is selected via URL parameter (`?exhibit=solar-system-explorer`). Each exhibit
is a "mode" within the page -- a different control panel and assembler
configuration -- not a separate HTML file. Two pages total for the entire
gallery.

**`gallery_metadata.json` is the bridge.** It gains a `type` field per entry:

```json
{ "type": "curated",     "file": "gallery/halley_perihelion.json", ... }
{ "type": "interactive", "exhibit": "solar-system-explorer", "label": "Solar System Explorer", ... }
```

Curated entries link to `index.html` (the existing viewer). Interactive entries
link to `interactive.html?exhibit=<exhibit>`. The gallery landing page reads
`gallery_metadata.json` and renders both types as cards -- curated cards show
categories and thumbnails, interactive cards show an "Explore" badge and link
to the interactive page. The landing page could be `index.html` itself (adding
a section for interactive cards) or a lightweight `gallery.html` that links to
both. Resolved: `interactive.html` deployed alongside `index.html`; landing
page integration deferred to Phase 2.

**Why this works:**

- **The existing pipeline is untouched.** Studio, the converter, the viewer --
  all continue to work exactly as they do today. No regression risk on 148
  curated cards.
- **Interactive complexity is isolated.** Pyodide loading, control panels,
  assembler calls, coverage-index queries -- all live in `interactive.html`.
  The curated viewer never loads Pyodide.
- **Editors develop separately.** Tony can refine the curated viewer and the
  interactive page on independent tracks. A bug in one cannot break the other.
- **Navigation is seamless.** Both pages share CSS and a common nav header.
  The user moves between curated and interactive content without feeling a
  seam.

**`interactive.html` responsibilities:**

1. Load the common gallery CSS and navigation header
2. Read the `exhibit` URL parameter -> select the appropriate control panel
3. Lazy-load Pyodide (from CDN) + the assembler module + domain cache files
4. Render the control panel (planet toggles, date picker, presets, etc.)
5. On user selection: build a scene spec (JSON) -> call the assembler via
   Pyodide -> receive Plotly JSON -> `Plotly.newPlot()`
6. Show loading state during Pyodide initialization ("Loading computation
   engine..." with progress)
7. Query the coverage index to determine available options -- the envelope
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

- **NASA Eyes on the Solar System** -- minimal controls overlaying 3D content;
  "if you can see it, you can click on it"; browser-native, real data
- **Exploratorium** -- "you don't look at exhibits, you play with them"; the
  interactive page IS the exhibit, not a settings panel
- **teamLab / ArtScience Museum** -- art + science + immersion; the dark space
  palette and glowing accents match the gallery's existing aesthetic
- **ViewSpace (STScI)** -- interactive astronomy content that teaches while
  being beautiful; every exhibit carries context (the info panel)

---

## Section 3 -- The Shared Assembler Architecture (settled -- architecture B')

**One shared assembler per domain, called by Pyodide in the browser.**

**The pattern -- three stages:**

1. **Harvest.** The gallery page reads user selections (JavaScript) and builds
   a scene spec -- a plain JSON document describing what to render.
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
class. Eight design decisions and six open questions deferred to the Phase 0 ->
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

## Section 3a -- Data Serving Architecture (framed -- Phase 1b)

**What Phase 0 proved.** The Solar System Explorer prototype computes
Keplerian orbits from mean orbital elements embedded in `orbital_elements.py`,
with no served data at all. This proves the Keplerian trace needs zero cache.
But the elements embedded in the codebase are manually maintained and some are
old (Saturn: epoch 2003, Pluto: epoch 1989). The desktop has better data --
fresh osculating elements in `osculating_cache_manager.py` and position
vectors in `orbit_paths.json` -- accumulated over months of plotting.

**The data serving architecture is the pipeline that bridges Tony's desktop
caches to the browser.**

**Three trace types (from the desktop codebase, verified in gallery JSON):**

- **Actual positions** -- Horizons ephemeris, x/y/z at dated time steps. Covers
  only the selected date range. Critical for precision at encounters, perihelia,
  close approaches, and date-range sweeps. This is the rolling cache data.
- **Osculating orbit at epoch** -- complete Keplerian conic from instantaneous
  elements (6 numbers + epoch per object). Critical for moons, where it's the
  only way to see the full orbit shape. Also important for comets near
  perihelion. The divergence from the mean orbit IS the perturbation lesson.
- **Mean elements** -- long-term average from `orbital_elements.py`. Ships with
  the codebase; no serving needed. Toggled off by default. Accurate for planet
  shapes; poor for close-approach detail.

**Two data types to serve (mean elements ship free):**

1. **Osculating elements per object** -- tiny (a handful of numbers each). Could
   ride in the coverage index or a small sidecar file. The assembler computes
   the complete Keplerian conic from these.
2. **Position vectors over date ranges** -- the rolling cache, the real volume.
   Per-object canonical files (F2 storage: ~157 positional objects, not 1,501
   pairs; canonical file count may be slightly higher due to barycenters).
   ~36 MB for the full catalog (Fable estimate, from 130.4 MB monolith).

**What works analytically vs what requires cache -- two classes for the rolling
cache, plus a write-once category:**

- **Planets, asteroids, comets** -- analytical orbits sufficient at solar-system
  scale. Presets override with cached data for close approaches and perihelia
  (Tier-2 curated data, write-once).
- **Moons** -- cache required. Constant perturbations and non-heliocentric
  mechanics make analytical orbits insufficient. The rolling batch is primarily
  moons.
- **Spacecraft** -- actual position arcs. NOT write-once (OQ-B): the flown arc
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
origin by construction -- no CORS question. Gallery size and headroom are
stated ONCE, in Section 1, and measured there; all-phase data needs are
~72 MB. Pre-heavy gallery JSONs are cullable
via L-074 if headroom tightens. The coverage index's `generated` timestamp
is the provenance anchor for the data (the data files don't carry their own
version history).

**Star cache:** 31 MB pickle -> `.npz` for v1 (NumPy stable in Pyodide; Parquet
held as optimization). Deferred to Phase 3.

**Open questions -- status after Phase 1b design convergence (v0.3):**

- OQ-A: Web catalog scope -- curated first tranche (9 test objects); full
  catalog scales via export run, not schema change. **Positioned.**
- OQ-B: Window policy -- v0.4 provisional leading edge -- nightly overwrite
  `[today-7d, today]`, freeze older past; `horizon=0` for non-spacecraft (the
  conic covers the future); spacecraft fetch the flown arc once then append
  today nightly (NOT write-once). **Settled (v0.4).**
- OQ-C: Update cadence -- NIGHTLY batch (v0.3 pivot), no forward padding --
  `horizon=0`, the conic covers the future. **Settled (v0.4).**

> **Addendum (July 24) -- Layer 3 operational config and a known failure
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

- OQ-D: Moon step size -- 6h default; per-object `step_hours` from day one.
  Io may want 2h. Mode 5 decides. **Positioned, Mode 5.**
- OQ-E: Serving home -- H2 subfolder in gallery repo (`data/`). Gallery
  size and headroom per Section 1; all-phase data needs ~72 MB. No
  CORS question (same repo, same origin). **Settled.**
- OQ-F: Canonical frame -- helio / parent-relative / arc-natural. The v4 model correction
  RETIRED subtraction (catastrophic cancellation + aliasing); osculating-primary
  now. The builder fetches FRESH from Horizons at each object's canonical center
  (it DOES re-query); no co-sampling for the orbit. **Settled (v0.4).**
- OQ-G: Wire format -- JSON for v1, column-oriented. **Settled.**

**Schema decisions settled in v0.3 (three-model convergence):**

> **v0.4 / v4 reconciliation note (July 9):** the SUBTRACTION / parent-
> composition model in some bullets below was RETIRED by the July-8 v4 model
> correction. Moons now render from their OWN osculating conic (osculating-
> primary), fetched FRESH per object; parents no longer compose moon orbits.
> Where a bullet conflicts with osculating-primary + fetch-fresh,
> GALLERY_DATA_SOURCE_HANDOFF v0.4 and the shipped gallery_cache_builder.py are
> authoritative. The full section-3a rewrite was tracked as L-108, which
> CLOSED 2026-07-12.

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
- Feature rendering: always JS in interactive layer (both A and B'). Python
  assembler handles orbits only. Feature configs in separate
  `feature_configs.json`. Three-context table: static gallery (pre-baked) /
  interactive A (JS everything) / interactive B' (Python orbits + JS
  features).
- 8 validation invariants the export script asserts before emitting the index.
- 9 test objects covering every schema class and edge case.

**Source:** Fable 5 broad analysis (`DATA_SERVING_BROAD_ANALYSIS.md`, July 5,
2026, built on `993dfd5` / `a6420bc`). Reviewed and refined by Opus 4.6 + Tony
(July 6, 2026). 4.8 review confirmed source faithfulness (July 6, 2026).
Phase 1b design handoff v0.3 (`PHASE1B_DATA_SERVING_DESIGN_HANDOFF.md`,
July 7, 2026): Opus 4.6 + Tony -> 4.8 review -> Fable 5 review -> convergence.

---

## Section 4 -- Four Visualization Domains

The domains are unchanged from v7. What changes is how each reaches the web.

### Section 4a -- Solar System (the main build)

**Desktop GUI:** `palomas_orrery.py` (11,092 lines at `38923c1`). `plot_objects` and
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

**Cache model:** Three-tier (Section 1). Coverage index drives the envelope.

### Section 4b -- Stars

**Desktop GUI:** `star_visualization_gui.py` with HR diagram and planetarium
pipeline scripts.

**Data:** Gaia + Hipparcos, 101 ly distance, magnitude 9. Fully cached in PKL.
Cannot be casually regenerated. Wire format decision (pickle -> Parquet/JSON)
needed for Pyodide (see Section 7).

**Gallery interactive page:** Distance and magnitude sliders, visualization
type selector, spectral class filters, star search. Rich controls -- this
domain is naturally interactive and phone-friendly (2D HR diagrams render well
on small screens).

### Section 4c -- Orbital Parameters (educational showcase)

**Desktop GUI:** `orbital_param_viz.py`. Eccentricity slider demo.

**Computation engines:** Pure geometry -- `idealized_orbits.py`,
`constants_new.py`, `apsidal_markers.py`. No data fetching.

**Gallery interactive page:** The eccentricity slider is the Phase 0 test
case. Lightest domain, pure geometry, no cache files. Teaches the Keplerian
language the rest of the orrery speaks. Converts from matplotlib to Plotly
for the gallery (no matplotlib in the browser).

### Section 4d -- Earth System

**Generators:** `earth_system_generator.py`, `food_insecurity_generator.py`.
Scenario modules for heatwaves, coral bleaching, food insecurity.

**Output:** Mixed -- KMZ files for Google Earth + Plotly teasers.

**Gallery interactive page:** Scenario selector. KMZ download links with
Plotly teasers (the pattern that works today). Future: Plotly choropleth or
map library for browser-native rendering. The KMZ rendering question resolves
when this domain's interactive page is built.

**Stance carries forward:** "Synthesize nothing, transcribe everything,
attribute to IPC." "Data Preservation is Climate Action."

### Section 4e -- Cross-Domain Integration

- **Celestial sphere** (`star_sphere_builder.py`): Adds star traces to orrery
  figures. Called by the solar system assembler.
- **Exoplanet orbits** (`exoplanet_orbits.py`): Bridges solar system and star
  domains. Phase 4 (hybrid).
- **Sgr A* Grand Tour** (`sgr_a_grand_tour.py`): Self-contained visualization.
  Phase 4 (hybrid).

---

## Section 5 -- Phased Approach

**The gallery gains one interactive page per phase.** Each phase ships a
working increment. Tony's render remains the close authority (Mode 5).

**Delta-log discipline throughout:** any orchestration change to the desktop
during the build gets a ledger tag ("assembler-must-inherit").

### Phase 0 -- Gallery Integration Test

**[x] DONE** (July 6, 2026). `interactive.html` deployed to
`palomasorrery.com/interactive.html` (created `300ac30c`, updated `a85a4fa`).
Pyodide v314.0.2 + NumPy computing Keplerian orbits from mean elements,
rendered by Plotly.js. Tested on desktop Chrome and iPhone Safari. Zero
server, zero data files -- pure computation from embedded orbital elements.

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
package -- dramatically faster than loading plotly in Pyodide.

**Architecture A vs B fork -- RESOLVED: B'.** Phase 0 proved architecture A
(Python/NumPy computes arrays, JS builds Plotly traces). Fable 5 identified
that A creates a parallel rendering pipeline -- convention duplication across
Python and JavaScript for the life of the project (the protocol's own anti-
pattern). A B' measurement page (`measure_plotly.html`) timed the full
plotly-in-Pyodide cold-start on iPhone Safari WiFi:

- Pyodide runtime: 929-959 ms
- NumPy: 141-146 ms
- micropip + plotly install: 507 ms - 1.8 s
- `import plotly.graph_objects`: 57-59 ms
- Build figure + `to_json()`: 448-449 ms
- **Total: 2.1-3.3 s** (acceptance threshold was <=15 s)

Fable verified plotly 6 imports lazy (0.06 s native); the WASM multiplier is
~1:1. The feared cold-start cost dissolved. B' uses a slim self-hosted wheel
(~3.9 MB, stripped of dead JS bundles and Jupyter extras) from the Phase 1b
serving home -- no PyPI runtime dependency.

**Two-tier model:** frozen pedagogical demos (Phase 0 Solar System Explorer,
eccentricity demo) stay on A -- instant-loading, convention-light, no sync tax
because frozen exhibits don't change. Data-backed catalog exhibits (Phase 2+)
take B' -- shared desktop engines, one codebase, scene equivalence by
construction.

**Attribution gate (L-086):** `interactive.html` is publicly reachable with
inline "Data: JPL/NASA" credit. Ruled sufficient pending L-086: a JPL-only
exhibit with inline credit passes. Page kept unlinked from landing page until
L-086 lands.

### Phase 1a -- Shared Spec Skeleton + Solar System Vocabulary

**[x] COMPLETE.** `PHASE1_SCENE_SPEC_VOCABULARY.md` (Fable 5, July 4, 2026,
built on `fdb66ca`). Shared skeleton (5 fields) + solar system payload
(9 field groups) + exhaustive mapping table (95 active `.get()` reads) +
content-type distinction (proves one assembler replaces both orchestrators)
+ coverage index Protocol class. Serializability settled yes.

Eight design decisions (DD-1 through DD-8) and six open questions (OQ-1
through OQ-6) deferred to Phase 0 -> Phase 2 transition.

Remaining gate items: seam gate-check and scene-equivalence criteria at
Phase 2 start.

### Phase 1b -- Data Serving Pipeline

**Fetch fresh from Horizons, serve to the browser.** Phase 1b builds a
purpose-built gallery cache in the gallery repo, populated nightly from
JPL Horizons with an explicit center per object -- the legacy desktop cache
is no longer read (provenance by construction). It makes this data
available to the interactive gallery.

**Design converged: v0.4** (v0.3 July 7 + the fetch-fresh / nightly amendments, July 8-9). Three-model review: Opus 4.6 +
Tony drafted schema -> 4.8 caught osculating-center gap, parent dependency,
validation invariants -> Fable 5 caught invariant self-contradiction,
`stored_center` overload, grid nesting -> Opus 4.6 + Tony converged.
Full design in `PHASE1B_DATA_SERVING_DESIGN_HANDOFF.md v0.3`.

Deliverables:
1. **Export script** -- fetches FRESH from Horizons per object with the explicit canonical
   center (v0.4 fetch-fresh pivot -- the legacy desktop cache is no longer
   read), validates on write (Guard v2 MONITOR + structural invariants), then
   stages -> atomic-swaps -> commits per-object canonical files in web-servable
   format (F2 storage). Built as `tools/gallery_cache_builder.py`.
2. **Coverage index** -- JSON manifest (schema v0.3) listing available objects,
   availability class, date coverage, step size, osculating elements with
   explicit center, `trajectory_of` for barycenter substitution, feature
   slugs. The assembler reads this to know what it can offer.
3. **Feature configs** -- separate `feature_configs.json` with renderer +
   params for JS feature renderers (interactive layer only; static gallery
   pre-bakes features).
4. **Serving home** -- OQ-E resolved (H2): the cache lives in the GALLERY repo `data/`
   subfolder -- same repo, same origin, NO CORS question (the dedicated
   `palomas-orrery-data` repo, option H1, was superseded). Deploy first web cache.
   The slim plotly wheel (~3.9 MB, B') also lives here.

Requires: Fable analysis (delivered), design handoff (converged v0.4),
gitignore updates (done @ `6368c87`).
Pre-build: diff `f1ede52..a56e036` for source file changes.
Gate: export script runs, web cache deployed to `data/`, interactive page
can fetch it.

### Phase 2 -- Solar System Assembler + First Interactive Page

Build the solar system assembler: scene spec -> Plotly figure JSON. Written
against the Phase 1 vocabulary, calling the shared computation engines.

Build the first solar system interactive gallery page: planet selection
buttons, center body, date picker. Static scenes only. Presets for encounters,
comet perihelion, close approaches. Each preset is a pre-filled scene spec that
the user can view as-is or modify.

Requires: Phase 1b data pipeline (done). The helpers split (L-087) is
DISCHARGED -- closed 2026-07-15; see Section 2, seam 2, for what
remains transitively. Architecture B'
confirmed (measurement passed July 6, 2026 -- 2.1-3.3 s on iPhone).


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

**Narrowed 2026-08-22 by the braid (Section 5a).** Track 1's exit
condition above reads "Batch 2 gas giants verified", which is Jupiter,
Saturn, Uranus and Neptune. What Artifact 2 needs is a SUBSET of that:
Saturn's rings, Jupiter's rings, and Jupiter's belts. Uranus and Neptune
are not in Artifact 2 and do not gate it. The table is left as written
because it is the record of the August ruling; the scope that applies to
Artifact 2 is the one in Section 5a.

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

### Phase 3 -- Star Assembler + Interactive Page

Design the star vocabulary (just-in-time, informed by Phase 2 lessons). Build
the star assembler. Resolve the star cache wire format -- pickle -> Parquet or
JSON for browser delivery.

Build the star interactive gallery page: distance and magnitude controls, HR
diagram and planetarium view selectors, spectral class filters.

Gate: scene equivalence + Mode 5 + the page ships.

### Phase 4 -- Hybrid: Exoplanets + Sgr A*

Cross-domain gallery pages. Depends on the solar system assembler.

Gate: scene equivalence + Mode 5 + pages ship.

### Phase 5 -- Earth System

Resolve the KMZ rendering question. Build the Earth system interactive gallery
page: scenario selector with Plotly teasers and KMZ download links. Future:
browser-native map rendering. 4.8 for restraint discipline on human-cost
content.

Gate: Mode 5 + the page ships.

### Phase 6 -- Dissolves

In the v7 plan, Phase 6 was "Web UI." In the gallery-extension model, there is
no separate web UI to build -- the gallery IS the UI. Each earlier phase ships
its own interactive page. What remains is refinement: navigation coherence
across all interactive pages, mobile responsive polish, the "suite-design
conversation" about what the whole interactive gallery feels like (L-096).
This is continuous work, not a gated phase.

---

## Section 5a -- The Critical Path

**Since v36 (2026-10-14) this section is the SHAPE of the work, not
its order.** The order lives on the road on
`documentation/WHERE_WE_ARE.md`, and the status in the ledger (Tony's
ruling of 2026-10-13, L-442). Its dated subsections, 2026-08-23 to
2026-09-29, moved word for word to `documentation/MASTER_PLAN_HISTORY.md`
PART 1. `MASTER_PLAN_CRITICAL_PATH_SUMMARY.md`, its readable companion
since August 16, was retired as a dated record at v34 (L-333, L-362).

**Rewritten 2026-08-16 at `227f5b2`.** The previous 5a was an execution
map with model assignments and a dependency chain. It had drifted: it
called Artifact 2 BLOCKED, which Section 6 had already amended on
August 8; it reported scanner and skill-version figures two weeks stale;
and its NEXT named work that L-192 superseded. More importantly it
described the provenance refactor as though that were the path, when the
refactor is one segment of it.

**Amended 2026-08-23 at `38923c1`, implementing the braid ruled
2026-08-22.** Provenance stops being
a GATE and becomes a per-artifact slice, and segment 3 is worked first.
The five segments below do NOT move: they are the SHAPE of the work and
they were confirmed unchanged on 2026-08-16. What moved is the order
they are worked in and the scope segment 1 must reach before an artifact
can lock. The argument, with its reasoning, is in
`documentation/DESIGN_NOTE_20260822_braid_and_citation_kind.md`
Section 1; the short form is that a precondition which does not
terminate is not a plan.

This section is the spine of the strategy. Detail lives in Sections 5,
6 and 7; history of every ruling stays in Section 6. When 5a and
another section disagree, 5a is the one that was rewritten last --
reconcile, do not guess. The order of the next jobs is not this
section's: it is the road's.

### The end goal

**The Python orrery, running in the browser under Pyodide, serving the
interactive gallery.** Not a translation of the orrery into JavaScript
-- the same computation engines, the same conventions, one codebase.
Architecture B' (Section 5, Phase 0). The static gallery it replaces
stays as the pedagogical exhibit layer.

### One pipeline, one direction

The single most important structural fact, and the one the earlier 5a
obscured: **the assembler creates no data.** It imports. There is no
point downstream of the orrery at which a wrong constant can be caught.

```
    ORRERY                the source of truth for feature constants
      |                   (ring radii, belt distances, shell bounds)
      |  transport        currently a HAND COPY into
      v                   gallery/data/objects_config.json
    CACHE BUILDER         nightly; fetches ephemerides FRESH from
      |                   Horizons; passes feature constants THROUGH
      v
    SERVED CACHE          coverage_index.json, feature_configs.json,
      |                   positions/  (in the gallery repo, same origin)
      v
    ASSEMBLER             resolver -> render_* -> Plotly figure JSON
      |
      v
    INTERACTIVE GALLERY   Pyodide + Plotly.js, static GitHub Pages
```

**The two data kinds behave differently and only one is
self-correcting.**

*Ephemerides* are re-fetched from Horizons every night. Provenance by
construction; a bad value cannot survive a rebuild. Nothing to audit.

*Feature constants* originate in the orrery's Python and reach the
gallery by copy. The builder does not know what a correct ring radius
is. Neither does the resolver, the renderer, or the browser. Horizons is
never consulted for them. **An error in the orrery becomes an error in
the gallery, permanently and silently.**

That asymmetry is why the provenance work exists and why its target is
the ORRERY. Until v19 this paragraph drew a second conclusion from it --
that the refactor must PRECEDE the assembler work rather than run beside
it -- and the 2026-08-22 ruling withdrew that conclusion.

The asymmetry governs what an artifact may LOCK, not what may be BUILT.
A fingerprinted artifact freezes its values, so it must not be locked on
unsourced ones. Drawing a ring freezes nothing.

And the order pays for itself, because the render is this project's own
ground truth. Ring provenance today is an audit of numbers nobody can
see -- text checked against text, which is precisely the mode that
produced three separate failures on 2026-08-22. Segment 3 is what
gives the provenance work a render to be checked against.

**One clause here was too strong and is corrected 2026-08-29.** It
read that a wrong ring radius "becomes something Tony's EYES can
catch." The GEOMETRY catches gross errors -- a wrong frame, a factor
of two, a body in the wrong place. It does not catch a few percent.
Fable's review of 2026-08-27 said so, and this project then produced
the case: `RADIATIVE_ZONE_AU` moved 0.7 -> 0.713, a 1.9 percent
change in a drawn radius, invisible at any zoom.

It WAS caught on the render, which is why the argument survives --
but by READING THE HOVER TEXT, not by seeing the shell. That is the
mechanism worth naming, because it is the one to design for: the
hover carries the value, the units and the source, so drawing a
feature puts its provenance in front of a reader for the first time.
The Alfven case Fable cited -- one solar radius in fifteen -- would
have been caught the same way and by nothing else.

### The path -- the five segments

What depends on what. The segments are numbered by DEPENDENCY, not by
the order they are worked in -- that is the subsection after this one,
and since 2026-08-22 the two are different.

**Segment 1 -- Make the orrery right.** Track 0 (L-181): one store for
feature constants, provenance carried as data, display text derived.
Track 1 (L-156): the provenance batches. The worksheet checker, the
request builder, the key rule and the dispatch loop (L-192) are the
MACHINERY of Track 1, not a phase of their own -- they are how the
annotations get reconciled at scale instead of by hand.

**Scoped per artifact, since 2026-08-22.** This segment as a whole does
not gate anything. What gates Artifact 2 is the slice Artifact 2
RENDERS, and that slice is countable, which is the whole point of
scoping it this way. Measured in the served cache at gallery
`493a0bd`: Saturn's seven rings carry `inner_radius_km` and
`outer_radius_km`; Jupiter's four rings add `thickness_km`; the belts
carry `belt_distances` (three values) and `belt_thickness`. **Thirty
measured numbers.** `n_rings` and `n_points` are drawing parameters --
DECLARED under Section 7 decision 18, and not findings.

The general audit does not stop. It stops being a gate. This is "The
Artifact Bounds the Audit" (PROJECT_INSTRUCTIONS.md, Part 3) extended by
one word: that rule bounds WHICH values are in scope, and this bounds
which are in scope NEXT.

**Segment 2 -- Make the transport faithful.** Track 0's cross-repo
transport (vendored pull, design endorsed August 8). A correct orrery is
not sufficient while `objects_config.json` is maintained by hand;
the copy can drift from a source that is right.

**Segment 3 -- Make the assembler draw.** Independent of segments 1 and
2 in the sense that it could be done today and would render immediately
-- the data is already served. `resolver.py:133` reduces a feature dict
to its keys (`tuple(rec.get("features") or ())`) with `models.py:91`
typing the field to match, so parameters are discarded one step before
anything could use them. Then L-154: the client feature renderers.
Nothing in the gallery repo currently reads `feature_configs.json`.

**Segment 4 -- Lock Artifact 2.** A golden artifact is fingerprinted, so
locking one on values that are not yet sourced means redoing the lock
rather than editing a number (Tony, August 2026). And an artifact
defined as *Jupiter and Saturn with rings and radiation belts* cannot be
Mode 5 accepted while nothing renders them.

One precision, measured 2026-08-23: **Saturn has no radiation belts** in
the served cache or in `objects_config.json`. Only Jupiter's are served.
The phrase above reads as though both bodies have them.

**Segment 5 -- Ship the Phase 2 page**, then Phase 3 stars, Phase 4
exoplanets and Sgr A*, Phase 5 Earth system. Phase 6 dissolves into
continuous refinement (Section 5).

### The order of execution -- the braid, ruled 2026-08-22

The five segments above are the SHAPE: what depends on what. They are
unchanged. This is the ORDER they are worked in, which is not the same
thing and which the braid changed.

1. **Segment 3** -- the rendering layer. Two lines in `resolver.py` plus
   a type, then the client feature renderers (L-154). Saturn on screen,
   unfingerprinted. This depends on NOTHING: the data is already served.
2. **Segment 1, sliced to Artifact 2** -- the thirty measured numbers
   above, and only those.
3. **Segment 4** -- lock Artifact 2.
4. **Segment 5** -- ship.

Segment 2 (the transport) is not in that list because it is not on the
path to Artifact 2 rendering; it is what stops a correct orrery drifting
from its copy afterwards.

**A consequence recorded at the time:** L-154 was BLOCKED in the ledger,
and this order unblocked it. The ledger made that edit; L-154 closed
DONE on 2026-08-24. (Until v36 this paragraph also said the plan
carries sequencing authority. Since 2026-10-13 the road on Where We
Are does, and the ledger keeps status: L-442.)

### The direction, after the Sun and Earth rooms

Tony's direction of 2026-10-10, confirmed on 2026-10-12 (L-433). The
Sun and Earth rooms are finished first, and "the Sun and Earth rooms"
includes the Solar System room's features: the fuzzy boundaries and
the scattered disk sit inside that work, not after it. Finished, they
are the template for every body's room. The rest of the orrery's
objects then come to the website as plotted positions. Then the inner
planets get their rooms, Mercury, Venus and Mars, from the template,
with Jupiter and Saturn after them; the Earth System layers are built
beside the planets' rooms, not after them. Encounters and the golden
artifacts stay paths to choose from then, not fixed steps. The checks
that keep the work honest are cleared beside the rooms, so nothing is
in front of them when they close. The end of the road is the website
doing what the desktop orrery does, with a date to choose, within the
range the data covers.

### Where the order and the history are

- The order of the work: the road on `documentation/WHERE_WE_ARE.md`.
- What is done, and what was ruled: `LEDGER_CONSOLIDATED.md`.
- This section is the shape of the work; its dated account, August 23
  to September 29, 2026, is `documentation/MASTER_PLAN_HISTORY.md`
  PART 1.

### What this section deliberately does not carry

Model assignments, per-item dependency chains and RICE scores. Those
belong in the ledger, which is the in-flight record; a plan that
duplicates them goes stale between sessions and then contradicts them.
Nor the order of the next jobs, which is the road's on Where We Are,
nor a dated account of sessions, which since 2026-10-14 is
`documentation/MASTER_PLAN_HISTORY.md` (L-442).
The August 5, 7 and 8 rulings that produced the track order stay in
Section 6 as history.

---

## Section 6 -- Prep Work

**L-080 -- Smoke-test harness.** Spec for scene equivalence (Phase 1 criteria).
Deferred to Phase 2 start.

**LICENSE to repo root.** [x] Done. `LICENSE.md` at repo root at HEAD (`7b25eb9`).

**Attribution page.** [ ] Not started. Data sources: JPL Horizons, JPL SBDB/CAD,
Copernicus CDS / ERA5 / ERA5T, NOAA Coral Reef Watch, IPC and FEWS NET, HDX,
OCHA FTS, SIMBAD (CDS), Gaia (ESA), Hipparcos, NSIDC, Mauna Loa CO2 (NOAA
GML/Scripps), HOT program. Provider citation strings need fetching (4.8 task --
fetched not recalled). Copernicus and IPC terms most likely to constrain
hosting. Not a Phase 0 blocker if page kept unlisted; required before any
publicly reachable interactive page.

**L-068 residuals** (L-066, L-016, L-014) -- Desktop cleanup. Not web blockers.

**`palomas_orrery_helpers.py` split** -- [x] **DONE 2026-07-15 (L-087).**
Verified at `38923c1`: the file holds zero tkinter references, and all
three functions the assembler needs are present --
`calculate_planet9_position_on_orbit`, `rotate_points2`,
`calculate_axis_range`. Residual, not a re-open: three modules in its
transitive import closure still import tkinter
(`osculating_cache_manager`, `save_utils`, `shutdown_handler`).

**L-162 -- CENTER_BODY_RADII de-duplication.** [x] **DONE 2026-07-29.**
The description below is preserved as the scope that was executed; it
read "[ ] Not started" through v18. Promote 15
remaining bodies (Mercury, Venus, Moon, Mars, Phobos, Saturn, Uranus,
Neptune, Pluto, Bennu, Eris, Haumea, Makemake, Arrokoth -- Planet 9
excluded, speculative not measured) to named constants in
`constants_new.py`, matching Sun/Earth/Jupiter's existing pattern. Values
already Gemini-verified (April 2026) -- this is restructuring, not
re-verification. Independent, can start now. Best landed before the
provenance scanner's Phase 3 pinning engine is built (L-155/156), so
pinning references named constants directly rather than needing dict-path
extraction for 15 of 18 bodies.

**L-154-162 -- Provenance scoring model fix (the whole cluster).**
[x] Design CLOSED, [x] ledger formalization CLOSED, [x] scanner Phase 1
(1a-1f) COMPLETE, [x] Phase 2 Piece 1 (D4 mechanism) COMPLETE,
[x] Phase 2 Track 1 Batch 1 COMPLETE, [ ] Phase 2 Track 1 Batch 2 NEXT.
AMENDED v17 (Tony, 2026-08-07): Track 0 (constant layer scaffolding)
now precedes the batches. The August 5 wording is preserved below as
history -- batches still precede the artifact, but they no longer come
first. See Phase 2 track structure in Section 5.
AMENDED AGAIN 2026-08-08 (Tony): Artifact 2 is no longer BLOCKED; it
becomes step 2. The migration proves the registry structure on Jupiter
first, because Jupiter's served data is complete and correct and so gives
the transport a real acceptance test. Artifact 2's remaining values are
then cross-checked INTO that proven structure, which is the same work the
Batch 2 gate was asking for, sequenced so it lands somewhere. The two
August wordings below are preserved as history, not withdrawn.
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
L-154 unblocks once the scanner work closes. **Superseded 2026-08-22 by
the braid (Section 5a):** L-154 is the rendering layer and is now the
FIRST work, not work waiting on the scanner. Its ledger status then
read BLOCKED; the ledger is the status authority, so that edit belonged
there and not here. (The ledger made it: L-154 closed DONE on
2026-08-24. Corrected at v36.)

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

Build progress, 2026-07-29: 1b landed. Built on ac07419, pushed at bf36743 -- verified via remote HEAD match and via reason-string re-execution (post-patch audit carries the new "cited, not independently cross-checked"/"date-sensitive" reasons 565 times, the old "has source citation"/"potentially stale" text zero times). Tier 1 held exactly at 156 (the invariant L-156 predicted: the highest score reachable on the changed path is 15, one below the Tier-1 floor of 16). Tier 2 rose 181->563 and Tier 3 fell 430->60 as the former V_STALE population merged into V_SOURCED; Tier 4 fell 14->2; total conserved at 781. One 1a follow-up landed alongside: CRIT_ABSOLUTE_OVERRIDE emptied now that Phase A left CENTER_BODY_RADII with only the Planet 9 raw literal. 1c (citation-window inheritance, ~42-unit Tier-1 reduction) is next.

Build progress, 2026-07-30: 1c predesign verified. Opus 5's predesign for the citation-window inheritance fix (L-156 Gap item 6) was independently re-verified against live HEAD (657542f) rather than accepted on its tables -- every headline figure held except one internal table split (22/1 -> 21/2, same total). The predesign corrected its own earlier estimate: yield is 23 inheriting findings, not 42, and surfaced 18 genuine uncited-block gaps in shell_configs.py now tracked as L-173. idealized_orbits.py's exclusion was re-confirmed on a structural basis (zero findings inside its one cited block) rather than the original, incorrect distance argument. Approved to build directly; no design round needed. Full detail: L-156's Note this date, L-173, PREDESIGN_1c_citation_inheritance.md.

**L-163 -- Module role/domain classification redesign (ROLE_MAP + MODULE_DOMAIN_MAP).**
[x] Role-side CLOSED, all 4 phases (Opus 5 + Sonnet 5, July 24-26 2026).
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
(Done since: L-437 retired MODULE_DOMAIN_MAP on 2026-10-13; the scanner
reads each module's own Domain: tag. Corrected at v36.)

---

## Section 7 -- Open Decisions

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
8. **Star cache wire format:** PKL -> Parquet/JSON for Pyodide. Resolved in
   Phase 3.
9. ~~**Matplotlib in Phase 0.**~~ **Dissolved.** The gallery is Plotly. The
   eccentricity demo converts to Plotly as part of Phase 0 -- not a separate
   decision.
10. ~~**Pyodide package weight + cold-start.**~~ **Resolved: B'.** Measured
    on iPhone Safari WiFi (July 6, 2026): Pyodide v314.0.2 + NumPy +
    micropip + plotly (stock wheel from PyPI) = **2.1-3.3 s total cold
    start**. `import plotly.graph_objects` = 57-59 ms (plotly 6 lazy-loads;
    WASM multiplier ~1:1). B' uses a slim self-hosted wheel (~3.9 MB,
    stripped of dead JS bundles and Jupyter extras per Fable's strip spec)
    from the Phase 1b serving home -- no PyPI dependency. Two-tier model:
    frozen A exhibits (instant, convention-light) + data-backed B' exhibits
    (shared engines, one codebase). Fable's convention-duplication analysis
    confirmed A's parallel-pipeline cost outweighs the B' cold-start cost for
    a solo developer at Phase 2 scale. OQ-i through OQ-v (from Fable A/B
    analysis) carry to Phase 2 start.
11. ~~**Gallery viewer architecture for interactive pages.**~~ **Resolved:
    Option C (hybrid).** `index.html` stays as curated viewer. Single
    `interactive.html` handles all interactive exhibits via URL parameter.
    `gallery_metadata.json` bridges both. See Section 2a.

12. **How feature data crosses the repo boundary.** **RATIFIED 2026-08-08
    (Tony).** **fetch-and-import.** The builder resolves the
    orrery HEAD SHA, fetches `constants_new.py` as text at that SHA,
    imports it, reads the feature values and their sources, validates,
    and writes into the staging cache under existing atomic-swap
    semantics. Python evaluates all derivation natively. Tony's workflow
    does not change: edit a constant, commit, push. Endorsed by Fable 5
    round 2 as "round 1's vendored pull with the exporter removed -- same
    fallback property, same SHA recording, same quarantine semantics,
    strictly fewer moving parts, and zero hand steps."
    **Superseded in part, recorded at v36:** L-322 (its ruling 6) built
    the JSON export after all -- `export_constants.py` writes
    `data/constants_export.json` (2026-09-16), and the gallery pulls it;
    that is the route numbers take today. The paragraph below is the
    reasoning as ruled on 2026-08-08.
    Two earlier candidates are retired: exporting to a JSON artifact
    (rests on a generation step and a run trigger that do not exist), and
    reading the file with Python's `ast` module without executing it
    (fights the store's design -- 6 of 49 top-level assignments are
    derived rather than literal, and at least one contains a constructor
    call `ast.literal_eval` cannot evaluate at all).
    **Count correction, 2026-08-11.** Measured at HEAD: 49 assignments, 6
    derived. The plan read 7 of 45. The 45-to-49 gap is exactly the four
    L-179/L-180 additions, so that half was stale rather than wrong. The
    constructor-call count was left as an open question -- the plan said
    two, that measurement found one -- with the instruction to resolve it
    by looking, not by patching.
    **Resolved by looking, 2026-08-23 at `38923c1`: TWO is right.**
    `constants_new.py` holds 48 top-level assignments; the six arithmetic
    derivations are unchanged; and TWO assignments contain constructor
    calls -- `HORIZONS_MAX_DATE = datetime(...)` at line 141, and
    `stellar_class_labels` at line 902, which holds twelve `dict()` calls
    inside a list of label specifications. The August 11 count missed the
    second because it looked only inside the derived expressions. The
    argument against `ast` is unaffected either way; one non-evaluable
    constructor is as fatal to it as two.
    Trust argument, recorded because future sessions will re-ask it: the
    builder, the orrery GUI, and every patch script Tony runs already
    come from the same two repos under the same account, so importing one
    more file from it adds NO NEW TRUST ROOT. A raw fetch at a full
    40-character SHA is content-addressed, so there is no window in which
    what was checked and what was imported can differ.
    **Two conditions attach to the ratification (Tony, 2026-08-08).**
    (a) A data-only rule for `constants_new.py` plus a pre-import gate,
    because import executes top-level code. The gate is roughly ten lines
    and checks two structural properties before the file runs: that every
    import is on an allowlist, and that no dictionary has a duplicate key.
    The duplicate-key check is the one capability fetch-and-import
    otherwise loses, since after import Python has already silently kept
    the last duplicate. (b) The fallback when GitHub is unreachable must
    be OBSERVED at build time, not inherited from a reviewer's claim. It
    falls back to the last committed copy and never writes empty features.
    Feasibility confirmed at ratification: `constants_new.py` imports only
    numpy and datetime, nothing orrery-internal, so the fetch really is
    ONE file with no dependency tree. (The numpy import is dead -- present
    since April 5 2025 with zero uses across all 46 commits -- and comes
    out when the migration next touches the file.)
13. **Generator shape and run cadence.** DISSOLVED by decision 12. There
    is no generation step -- "generation" is Tony editing the store.
    (Since 2026-09-16 there is one: `export_constants.py`, run by the
    orrery maintenance run, L-322. Recorded at v36.)
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
16. **Pilot slice inside Track 0.** **RULED 2026-08-08 (Tony): Jupiter
    first, structure before values.** Prove the registry structure on
    Jupiter, where the served data is already complete and correct so the
    transport gets a real acceptance test. Then cross-check Artifact 2's
    remaining values, writing them into the proven structure. Then
    complete the migration and resolve what surfaces. The recommendation
    below is what Tony ruled on, and it stands as written except for one
    number: it says Jupiter has 5 entries, and the August 10 session
    counted 4 ring entries.
    **Confirmed 2026-08-23: FOUR.** `main_ring`, `halo_ring`,
    `amalthea_gossamer`, `thebe_gossamer` -- identical in
    `objects_config.json` and in the served `feature_configs.json` at
    gallery `493a0bd`. The "5 entries" in the recommendation below is
    wrong and is left in place because it is a quotation of what was
    ruled on.
    Fable round 2
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
17. **Where description interpolation happens.** **RULED 2026-08-08
    (Tony): BUILDER SIDE.** The served cache holds pre-interpolated final
    strings. Tony's reason is not the one Fable argued: it is that the
    orrery and the assembler cannot diverge if only one of them ever
    composes the sentence. Accepted cost, stated at the time: the cache
    holds finished strings, so rephrasing anything requires a rebuild.
    Fable's supporting arguments also hold -- it keeps the assembler dumb,
    keeps the failure surface at build time where quarantine already
    exists, and means a template error is caught at build rather than in a
    user's browser. The alternative (cache holds templates plus values,
    assembler interpolates at render time) is retired.

18. **Shape of a registry entry.** **RULED 2026-08-08 (Tony): three
    zones.** Every entry separates:
    - **MEASURED** -- a published value, carrying value, unit, AND source.
      Not a bare number with the unit baked into the key name. Tony's
      reasoning: published values arrive in mixed units regardless, so a
      conversion step is needed for uniform display text no matter what
      is stored. Storage stays heterogeneous; conversion happens at the
      display step. This DELETED an earlier Claude recommendation for a
      per-feature unit convention.
    - **DECLARED** -- a developer style choice (color, opacity). No source
      is expected, and its absence is not a finding.
    - **DERIVED display text** -- NOT stored. Built by interpolation from
      the other two, at the builder, per decision 17.
    Two structural constraints follow. Everything measured must sit at
    MODULE SCOPE, readable without executing anything -- this is what
    makes L-181 the PRECONDITION for L-190 rather than more work for it,
    since a value inside a draw function cannot be walked by a static
    pass, which is exactly why the scanner cannot see `belt_distances`
    today. And there is ONE not-yet-sourced state, not two: the orrery is
    the source, so if the orrery does not offer a value there is nothing
    to render and no field to fill. A not-yet-sourced field means a value
    that IS rendered but has no recorded provenance. Distinguishable from
    absent; never an empty field.
    `CHROMOSPHERE_RADIUS_LINE` is the working precedent for the derived
    zone: two values stored in different units feeding one sentence that
    emits solar radii, AU, and km.
    One question stays open and is better answered against Jupiter's ring
    entries than in the abstract: should EVERY measured field be
    range-capable? The evidence that it might -- Jupiter's main ring
    `description` says the thickness is about 30 to 300 km while
    `thickness_km` says 30, so the prose is more accurate than the data
    beside it.
    (Answered as method since: provenance-discipline, When the source
    gives a range -- the range is stored as rows and the drawn value is
    a declared construction over them. Recorded at v36.)

---

## Section 8 -- Vision Opportunities

*Captured in `LEDGER_CONSOLIDATED.md`. Several already carry L-numbers.*

**Arriving naturally with the gallery-extension model:**

- **Option E unified front end** (L-091) -- the gallery IS the front end now.
  This vision item is realized by the architecture, not deferred.
- **Gallery generators as spec-producers** -- already true for pre-curated
  cards; interactive pages extend it.
- **Embeddable scenes for educators** (L-092) -- a gallery page with preset
  parameters in the URL hash is an embeddable exhibit. Arrives nearly for free
  once interactive pages exist.
- **Educational guided explorations** (L-093) -- the narrative sections plus
  interactive pages plus presets = a guided tour.

**Still deferred:**
- Preset authoring (L-046)
- Community cache as commons (L-094)
- PWA / offline for classrooms (L-095)
- What the interactive gallery *feels* like (L-096 -- suite-design conversation)

---

## Section 9 -- What This Plan Does NOT Cover

Desktop development continues on its own track. The gallery extension is
additive. The Instagram pipeline is independent. The existing ledger is
unaffected. Desktop-to-assembler migration (refactoring the desktop to use
the shared assembler) is deferred -- valuable for codebase unification but
not on the critical path for the gallery.

---

## Section 10 -- Lineage

Moved on 2026-10-14, word for word, to
`documentation/MASTER_PLAN_HISTORY.md` PART 2 (Tony's ruling of
2026-10-14, L-442). It was last added to at v19, 2026-08-23.

---

## Section 11 -- Protocol & Skills Review (from Phase 0)

Phase 0 stress-tested the protocol across three models in a single day.
Detailed findings in `PROTOCOL_SKILLS_REVIEW_PHASE0.md`. Summary:

**New lessons for protocol v3.32 consideration:**
- "Measure before analyzing" -- when an architectural fork hinges on a
  measurable quantity, build the measurement before the analysis.
- Frozen artifacts don't accrue sync tax -- refines the parallel-pipeline
  anti-pattern.
- Consent gate as a UX pattern for unfamiliar technology.
- Provenance markers (*(est.)*, *(fetched)*) belong in relay prompts too.

**Skill updates needed:**
- `gallery-pipeline` v1.1: Option C viewer, consent gate, two-tier model,
  `interactive.html` conventions, `?exhibit=` parameter. **LANDED** -- the
  skill is at 1.2.
- Decide: separate `pyodide-interactive` skill or extend `gallery-pipeline`.
  Still open.

**What worked:** SHA round-trip caught real provenance errors; three-model
relay produced genuine error correction; "each round simpler" held (feared
B cost: 15-25 s -> measured 2.1 s). **What to improve:** re-pull SHAs at
draft time (not just session start); mark estimates as *(est.)* in relay
prompts.

---

Base: orrery @ `38923c1` / gallery @ `493a0bd` -- v19 built on those,
pushed at orrery `f504c06` / gallery `02aefc0` on 2026-08-23. (All
confirmed against the live remote; v17-v18 stood at orrery `ee0da47` /
gallery `61a78c0`;
v16 was orrery `4b82384` / gallery `e7e8c5e`; v15 was orrery
`b59cb72` / gallery `22c947c9`).
Phase 0 closed. Phase 1a vocabulary delivered. A/B fork resolved: B'.
Phase 1b builder built, offline-verified (L-098), and Layer 2 live-Horizons
fully tested and closed -- L-149 and L-118 both DONE; L-151 DONE
2026-07-27; L-150 still decided, not built.
Scanner detour: Phase 1 (1a-1f + D8.5) COMPLETE. Phase 2 Piece 1 (D4
scanner mechanism) COMPLETE -- V2 rung live, zero population. Phase 2
Track 1 Batch 1 COMPLETE -- three-model competitive cross-check of 5 shell
modules + Mars, geometry follow-up, Fable consistency audit. Phase 2
Track 1 Batch 2 (gas giants: jupiter, saturn, uranus, neptune) is NO
LONGER the gate before Artifact 2 -- the braid narrowed that gate on
2026-08-22 to the slice Artifact 2 renders (Section 5a). Push gate for
this phase:
Tier-1 = 0 ON THE INTERACTIVE BUILD PATH, with the path computed from
the import graph rather than listed by hand. The gate gets built
before the batches it scopes.
New structural items from Fable audit: L-176 (illustrated dimensions in
hover text), L-177 (Mercury Hill sphere convention), L-178-180
(Earth/solar inconsistencies), L-181 (single-source-of-truth constant
layer).

SKILL AND PROTOCOL VERSIONS ARE NOT RESTATED HERE. This block used to
carry ten of them by hand; five had drifted by 2026-08-23 and nothing
watched them. The authority is the generated Skill Manifest in
`PROJECT_INSTRUCTIONS.md`, Part 3 -- rebuilt by `skills_index.py`, and
the copy Stale Skill = Stop actually compares a loaded skill against.
Read it there. (Tony's ruling, 2026-08-23: fix the producer, not N
consumers.)
NEXT is not restated here; it drifted the same way the skill versions
did. Until v22 this line said the feature-rendering JS layer was still
to be written, five days after it shipped with the Sun exhibit. The
order lives on the road on `documentation/WHERE_WE_ARE.md`, and only
there (Tony's ruling of 2026-10-13; until v36 this line named Section
5a, dated 2026-09-03; the same fix-the-producer ruling as the
paragraph above). Layer 3 (nightly Task
Scheduler) RETIRED 2026-08-10 -- task disabled not deleted, builder run
manually, first manual build clean 2026-08-11. The known intermittent
promotion-step glitch (S3a addendum, July 24) is moot while manual and
returns with the schedule if it ever does.
Solar System Explorer live at palomasorrery.com/interactive.html.
