---
name: interactive-exhibit
description: How an interactive exhibit (a room in interactive.html such as ?exhibit=sun) is designed, built, verified and carded for the Paloma's Orrery gallery. Covers the exhibit switch and boot path, the assembler driver spec, the JS feature handoff, the shared chrome (drawer, nav cluster and frame zoom, i-panel, frame HUD, consent gate, back link), what is per-body, the served-data provenance contract (value / unit / source / orrery_constant pointer, checked by the live store-drift run), the Mode 5 sequence on the phone, and how the exhibit becomes a gallery card through Studio. Use when adding or changing an exhibit (Earth, Jupiter, the stars), when touching sun* chrome in interactive.html, or when deciding what an exhibit may render. Not for propagation math (gallery-assembler), the nightly data builder (gallery-cache-builder), or the Studio/converter chain for figure cards (gallery-pipeline). Do not use for projects other than Paloma's Orrery.
fires_when: adding or changing an exhibit in interactive.html; any edit to the Sun's chrome (drawer, nav cluster, frame zoom, i-panel, HUD, consent, back link); "Earth interactive", "?exhibit=", "new room in interactive.html"; deciding what numbers an exhibit may render and where they come from; carding an exhibit in Studio
---

# Interactive Exhibit

Skill version: 1.0 | Cut from gallery @ fc8d9fb3 (interactive.html,
feature_renderers.js, data/objects_config.json, gallery_maintenance_run.py,
tools/gallery_studio.py) and orrery @ a57e86b8 (LEDGER_CONSOLIDATED.md
L-260, L-267, L-278, L-282, L-288, L-289) | 2026-09-06
Written with Anthropic's Claude Fable 5.1 before the Earth exhibit, on
Tony's question "do we have a skill that defines how we build
interactives?" The answer was no; the Sun's pattern lived only as code
and as ledger history. Everything below was read from those files at
the pinned SHAs, not recalled.

## What an exhibit is, and what this skill is not

An exhibit is a ROOM in `interactive.html`, chosen by `?exhibit=<key>`.
It runs the shared `assembler` package in Pyodide against the served
cache (Python assembles the scene), and JavaScript draws the body's
features (`feature_renderers.js`). The Sun (`?exhibit=sun`) is the
worked example and the template; the Solar System Explorer is the
default room and predates the pattern.

Three neighbours own the layers beneath and beside this one:
- gallery-assembler: the propagation math, resolver, cache reader,
  trust system, golden artifacts, Mode 5 as MEASUREMENT, and the rule
  never to mutate a plot from inside a Plotly event handler.
- gallery-cache-builder: how `data/solar-system/` is produced nightly.
- gallery-pipeline: Studio -> json_converter -> index.html for FIGURE
  cards. An exhibit's card is the one place this skill touches Studio.

## The anatomy of an exhibit (the Sun, read at fc8d9fb3)

Named so a new exhibit can be checked piece by piece against the
template. "Shared" means one copy serves every room; "per-body" means
the new exhibit brings its own.

| Piece | Where | Shared or per-body |
|---|---|---|
| `EXHIBIT` switch: `?exhibit=` lower-cased, default `solar-system-explorer` | interactive.html, SUN EXHIBIT block | shared; a new room adds one `EXHIBIT === "<key>"` branch |
| `body.<key>-exhibit` class and `.<key>-chrome` show/hide rule | `applySunChrome()`, CSS | per-body class, shared mechanism |
| Assembler modules list and the DRIVER: `assemble_scene({domain, content_type, objects, center, epoch}, Catalog(objects_config), CacheReader(coverage_index))` | `SUN_ASSEMBLER_MODULES`, `SUN_DRIVER` | shared code; per-body spec (`objects`, `center`) |
| Data read at boot: `data/solar-system/coverage_index.json`, `data/objects_config.json` | `initSunExhibit()` | shared |
| Feature handoff: `GalleryFeatures.buildFeatureTraces(features, positions, {sceneHalfRangeAu})`; anything larger than the frame goes to the drawer, not dropped | feature_renderers.js | shared |
| Arrival frame: measure every trace once (`sunTraceExtentAu`), half-range = 1.1 x the largest visible, floored at the body's constant (`SUN_HALF_RANGE_AU` 0.25) | initSunExhibit | mechanism shared; the floor and what is visible on arrival are per-body rulings |
| Layout builder: aspect 1:1:1 unless the body's physics says otherwise (the Sun's shells are spheres); axes state their unit; `tick0` 0 and `dtick` from `sunGridDtick(span)` | `buildSunLayout()` | per-body values, shared rules |
| Drawer replacing the legend: rows from `legendgroup`, `legendonly` hides, All / none, focus row | `buildSunDrawer`, `sunApplyVisibility`, `sunFocusOn` | shared |
| Nav cluster: + / - / Home = FRAME zoom (range and dtick change together; the grid re-labels) | gallery/nav_cluster.js, `navFrameZoom`, `navHome` | shared |
| Click deferral: `plotly_click` -> `setTimeout(0)` -> focus | initSunExhibit | shared, CRITICAL (L-278) |
| i-panel follows the focus; curated link per feature stamped into trace `meta` by `stampLink` | `renderSunInfo`, feature_renderers.js | shared mechanism; per-body copy and links |
| Frame HUD: camera-following triad, Aries glyph with the frame note and its source, grid chip | `sunHud*` | shared; reads the camera, never calls Plotly |
| Consent gate and Pyodide load | `loadPyodideRuntime`, `CONSENT_KEY` | shared |
| Back link: "Gallery" steps back in history when the gallery is behind it | BACK TO THE GALLERY block | shared |

The naming carries a debt: most shared pieces are called `sun*` because
the Sun was first. The second exhibit is the moment to rename or
parametrize them, not to copy them under `earth*`. One drawer, one nav
cluster, one HUD, one i-panel; the body is a parameter.

## Rules

### Design before code [QUALITY]
An exhibit starts as a conversation with Tony, zero code: what is in
the arrival frame and what waits in the drawer; the half-range floor;
which of the body's features exist in the served entry today and which
must be added; what is Earth-specific (or Jupiter-specific) chrome, if
anything. Each round gets simpler. The Sun's arrival ruling (core
through outer corona, streamer belt in frame) is the shape of the
answer, not the answer.

### One chrome, many rooms [QUALITY]
Before adding a second room, grep interactive.html for `sun` inside the
shared pieces above and decide, piece by piece: rename, parametrize, or
leave (with a reason). A second copy of the drawer is the Parallel
Pipelines failure one page wide. When a shared piece changes, both
rooms are Mode 5 targets.

### Provenance is part of the build [CRITICAL]
The exhibit renders only what the served entry carries, and every
rendered NUMBER carries its provenance in the served data, not in the
page:

- In `data/objects_config.json`, a measured value sits as
  `{ "value": ..., "unit": ..., "source": "...",
  "orrery_constant": "constants_new.py::NAME" }`. The value is the
  orrery store's value; the pointer names it; the source is the
  published authority. Earth's `planet_radius` at fc8d9fb3 is the
  worked example (IERS 2010, `EARTH_EQUATORIAL_RADIUS_KM`).
- The live maintenance run (`gallery_maintenance_run.py --live`, Store
  drift) follows every pointer into the orrery store at orrery HEAD and
  reports MATCH, DRIFT, or NOT IN STORE, by name. A new exhibit's
  pointers must read MATCH before the exhibit is called done. NOT IN
  STORE is fixed by adding the constant to the store (`constants_new.py`
  is the single value home), never by removing the pointer; DRIFT is a
  finding on whichever side moved.
- Colours, opacities, marker sizes, display names and point counts are
  the DECLARED zone (master plan Section 7 decision 18): style, no
  source expected. Match the orrery's palette so the legend reads the
  same.
- Text CLAIMS the page makes -- the i-panel copy, the frame note --
  carry their source in the page itself, because the assembler does not
  pass through the provenance scanner. The frame note's NAIF citation
  is the form.
- Where a value is unknowable or stylized (a dipole azimuth, the
  streamer belt's warp), the hover says so; silence reads as precision
  the model lacks (Show the Envelope of the Unknowable).
- The Artifact Bounds the Audit, and The Braid orders it: the new
  exhibit's pointers are the slice; a provenance gap found elsewhere
  while building it is recorded, one ledger row per CLASS, not chased.
  This is the same discipline the orrery reached retroactively, applied
  to the assembler as it is built (Tony, 2026-09-06).

### Never mutate a plot from inside a Plotly event handler [CRITICAL]
A relayout from inside `plotly_click` re-enters the update machinery
and the page dies. Defer with `setTimeout(0)`. Full record:
gallery-assembler field note, L-278. Chrome that only READS (the HUD
reads the camera each animation frame) is exempt; anything that calls
`Plotly.*` from an event is not.

### Scene text is scenery [QUALITY]
Anything that must stay legible at every zoom and angle belongs in the
page, not the scene. Text drawn in the scene shrinks with distance, is
clipped at the box boundary, and floats for edges beside the camera
(L-289, first build, failed on the phone). Labels, chips, triads,
notes: page chrome.

### The frame zoom and the grid agree [QUALITY]
`+`, `-` and Home change the range AND the dtick together through one
rule (`sunGridDtick`). The arrival layout must set dtick by the same
rule, or Plotly picks its own and the grid chip disagrees with the grid
(L-289, 2026-09-06: 0.2 vs 0.1 AU on arrival). Mouse-wheel is camera
zoom and leaves the spacing alone by design.

### Aspect is read, not assumed [QUALITY]
Chrome that projects from the camera reads `aspectratio` from the full
layout. 1:1:1 is the Sun's choice, not a law (Tony: "sometimes the ticks
are not isometric").

### Hover text gives km AND AU [QUALITY]
Standing convention inherited from the orrery (orrery-coding-conventions).

### Phone first, and the conditions are stated [QUALITY]
Mode 5 runs portrait on Tony's phone before desktop. Sequence: arrival
frame (what is in view, grid = chip); rotate (triad follows; nothing
floats); + / - / Home (grid re-labels, chip follows); drawer (a hidden
shell draws and the view rescales to hold it); a shell tap (focus,
i-panel, link); the HUD note (hover on desktop, tap on phone); Gallery
button then browser back; then landscape; then desktop. Report each
trial with its conditions -- device, orientation, arrival or after
which action -- per gallery-assembler's Mode 5 as Measurement. A
headless run here measures the mechanism; only the phone measures
legibility. Three of five things built in the week of 2026-09-05
changed after Tony's eyes saw them.

### The touch path is not the mouse path [QUALITY]
Plotly fires no camera events during a touch rotation; chrome that
follows the camera reads it directly (`scene._scene.getCamera()`) once
per frame. Touch has no hover; anything that opens on hover opens on
tap and closes on a tap elsewhere. A `hidden` attribute loses to a more
specific display rule; write the hidden rule at least as specific.

## Adding an exhibit: the order

1. Design round with Tony (above). Record rulings in the ledger item
   before code.
2. Served data: confirm the body's entry in `data/objects_config.json`
   has every feature the design draws, each measured value with
   value / unit / source / orrery_constant; add what is missing to the
   STORE first, then to the entry; confirm the nightly builder covers
   the body (gallery-cache-builder) and `coverage_index.json` lists it.
3. Code: one `EXHIBIT === "<key>"` branch; a driver spec with the body
   as `objects` and `center`; the body's half-range floor; the layout
   builder's per-body values; i-panel copy with sources inline. Reuse
   the shared chrome by parameter, renaming `sun*` where the second
   user makes the name wrong.
4. Pre-test here: `node --check` on the page script; a stand-in scene
   for chrome that can run without Pyodide (the CDN is blocked in the
   sandbox, so the exhibit itself cannot start here -- say so in the
   handoff).
5. Push; `gallery_maintenance_run.py --live`; Store drift reads MATCH
   for the new pointers, by name.
6. Mode 5 on the phone, sequence above; fix; repeat.
7. Card: Studio -> New Interactive Card (L-288) -> pick the scene (the
   picker reads `EXHIBIT === "<key>"` literally from the page source, so
   the key must appear in that form) -> title, placard, sources -> lands
   in Storage -> the editor places it; featured if it belongs on the
   lobby.
8. Ledger: the exhibit's item closes on Tony's Mode 5, not on the push.

## Field notes

- 2026-09-02, L-278: `sunFocusOn` called from inside `plotly_click`
  killed the page with "Maximum call stack size exceeded" on a stack 25
  frames deep. Not recursion; a large array applied as arguments inside
  a half-finished replot. `setTimeout(0)` fixed it. Eight reads to
  attribute; three wrong readings from inferring conditions.
- 2026-09-05, L-289: tick values and axis names drawn as scatter3d text
  on all twelve box edges passed every headless check and failed the
  phone on three counts. Rebuilt as page chrome (triad, chip, note).
- 2026-09-06, L-289: four defects in the rebuild, all from the desktop
  and phone pass: `hidden` beaten by a class rule; grid colours read as
  a second key beside the triad (withdrawn); arrival dtick unset; touch
  rotation fires no camera events. None visible headless.
- 2026-09-05, L-282: the "Gallery" button was a plain link, so Safari's
  back walked into the exhibit from the lobby. history.back() when the
  gallery is behind.
- 2026-09-06, L-288: Studio authors the exhibit's card; the card is a
  placard with an Interactive tag and needs no picture (the lobby
  settled that on the phone).

## Install and verify

Author here: `skills/interactive-exhibit/SKILL.md` in the orrery repo.
Install to the account (Settings > Skills). Run `skills_index.py` so the
manifest in PROJECT_INSTRUCTIONS.md gains the row. Per Stale Skill =
Stop, the session that installs it cannot verify the install; the Earth
session confirms its loaded copy reads 1.0 before building.
