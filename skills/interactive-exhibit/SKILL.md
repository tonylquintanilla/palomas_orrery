---
name: interactive-exhibit
description: How an interactive exhibit (a room in interactive.html such as ?exhibit=sun) is designed, built, verified and carded for the Paloma's Orrery gallery. Covers the exhibit switch and boot path, the assembler driver spec, the JS feature handoff, the shared chrome (drawer, nav cluster and frame zoom, i-panel, frame HUD, consent gate, back link), what is per-body, the served-data provenance contract (value / unit / source / orrery_constant pointer, checked by the live store-drift run), the Mode 5 sequence on the phone, and how the exhibit becomes a gallery card through Studio. Use when adding or changing an exhibit (Earth, Jupiter, the stars), when touching sun* chrome in interactive.html, or when deciding what an exhibit may render. Not for propagation math (gallery-assembler), the nightly data builder (gallery-cache-builder), or the Studio/converter chain for figure cards (gallery-pipeline). Do not use for projects other than Paloma's Orrery.
fires_when: adding or changing an exhibit in interactive.html; any edit to the Sun's chrome (drawer, nav cluster, frame zoom, i-panel, HUD, consent, back link); "Earth interactive", "?exhibit=", "new room in interactive.html"; deciding what numbers an exhibit may render and where they come from; carding an exhibit in Studio
---

# Interactive Exhibit

Skill version: 1.3 | Cut from gallery @ b375cfe1 (interactive.html,
gallery/nav_cluster.js, gallery/feature_renderers.js,
documentation/smoke_hover_budget.js) and orrery @ d99d8db1
(LEDGER_CONSOLIDATED.md L-316, L-318, L-331, L-332) | 2026-09-16, with
Anthropic's Claude Opus 5
v1.3 (L-332) carries the phone chrome as six rounds on Tony's phone left
it on 2026-09-15/16 (L-316 rounds 3 and 4, L-318 rounds 3 to 6). The
arrow cross's corner is set by one CSS rule and the method that moves it
says nothing about the corner; a drawer row has a finger-sized selection
target and GO on an unticked shell ticks it, amending L-267's G2 in that
one case; a line break inside a sentence is soft and the phone rejoins
it; on a portrait phone the text box has no arrow and sits mid-view; and
a phone tap reaches a shell's marker rather than its dots, through a
second Plotly rule read from v2.35.2. Step 4 gains the hover budget
suite. One new rule: hover text is written for the visitor -- Tony's
standing rule of 2026-09-16, the Register Rule pointed at what a visitor
reads (L-331). Version 1.2 described the chrome as rounds 1 and 2 left
it, which was five rounds stale when this was cut.
Earlier: v1.2 (L-316, L-318) records what the chrome gained after Tony's phone:
the nav cluster's four arrow buttons and their portrait placement, the
drawer label, and two Plotly rules the build found by reading v2.35.2's
source rather than recalling it -- a scene relayout carries the live
camera, and a hover box keeps its pointer only when it fits to one side.
Earlier: v1.1 (L-291) corrects what Earth step 3 made untrue and adds what its
close taught about carding. The page picks a room from an `EXHIBITS`
table now, not an `EXHIBIT === "<key>"` branch, and four places still
said branch: the anatomy's switch and class rows, step 3, and step
7's picker. Step 3 gains the driver rule the build found by running
the resolver; step 7 gains the check for an existing card and the
order Studio forces; the rename paragraph points at L-309, which
deferred it; one field note.
Earlier: v1.0 cut from gallery @ fc8d9fb3 (interactive.html,
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

## The anatomy of an exhibit (the Sun, read at fc8d9fb3; two rows corrected at 1.1)

Named so a new exhibit can be checked piece by piece against the
template. "Shared" means one copy serves every room; "per-body" means
the new exhibit brings its own.

| Piece | Where | Shared or per-body |
|---|---|---|
| `EXHIBIT` switch: `?exhibit=` lower-cased, default `solar-system-explorer`; `EX = EXHIBITS[EXHIBIT]` is the room | interactive.html, `const EXHIBITS` | shared; a new room adds one ROW to `EXHIBITS` -- title, sceneTitle, pngName, halfRangeAu, driver, infoHtml, compose (since Earth step 3, L-291; at fc8d9fb3 it was one `EXHIBIT === "<key>"` branch per room) |
| `body.sun-exhibit` class and `.sun-chrome` show/hide rule, added for EVERY room | `applySunChrome()`, CSS | shared; the name stays `sun` until the rename (L-309) -- at fc8d9fb3 this row read per-body `body.<key>-exhibit` |
| Assembler modules list and the DRIVER: `assemble_scene({domain, content_type, objects, center, epoch}, Catalog(objects_config), CacheReader(coverage_index))` | `SUN_ASSEMBLER_MODULES`, `SUN_DRIVER` | shared code; per-body spec (`objects`, `center`) |
| Data read at boot: `data/solar-system/coverage_index.json`, `data/objects_config.json` | `initSunExhibit()` | shared |
| Feature handoff: `GalleryFeatures.buildFeatureTraces(features, positions, {sceneHalfRangeAu})`; anything larger than the frame goes to the drawer, not dropped | feature_renderers.js | shared |
| Arrival frame: measure every trace once (`sunTraceExtentAu`), half-range = 1.1 x the largest visible, floored at the body's constant (`SUN_HALF_RANGE_AU` 0.25) | initSunExhibit | mechanism shared; the floor and what is visible on arrival are per-body rulings |
| Layout builder: aspect 1:1:1 unless the body's physics says otherwise (the Sun's shells are spheres); axes state their unit; `tick0` 0 and `dtick` from `sunGridDtick(span)` | `buildSunLayout()` | per-body values, shared rules |
| Drawer replacing the legend: rows from `legendgroup`, `legendonly` hides, All / none, focus row. A row's whole left end -- edge, box and colour dot, the full row height, about 65 px -- ticks and unticks; rows are at least 44 px tall; the name or GO on an UNTICKED shell ticks it and then frames it (L-318 round 3, amending L-267's G2 in that one case; GO still never hides anything). Naming a DRAWN shell also opens its hover text as a text box: on the desktop and a landscape phone a scene annotation pinned to its info marker with an arrow; on a portrait phone (`sunPhonePortrait()`) a page annotation centred in the view with no arrow, same text and width (L-318 round 5). A tap in the scene, on the box, or on the backdrop closes it; the backdrop also closes the drawer; unticking closes it too (L-318) | `buildSunDrawer`, `sunApplyVisibility`, `sunFocusOn`, `sunLabelShow`, `sunLabelInstall`, `sunPhonePortrait`; knobs `SUN_LABEL_WRAP_CHARS` (34), `SUN_LABEL_PHONE_X` / `_Y` (0.5), `SUN_LABEL_FONT_PX` (12) | shared |
| Nav cluster: + / - / Home = FRAME zoom (range and dtick change together; the grid re-labels), plus four arrow buttons that turn the camera by a step scaled to the live eye distance, so a tap moves the same slice of screen at any zoom (L-310); on a portrait phone 768 px or narrower the arrow cross, Home with it, moves apart from + and - into its own holder, and the in-frame title stays (L-316). WHICH corner is set only by the `.nav-cross-apart` CSS rule in `nav_cluster.js` -- top right since round 4, after a round at the bottom left -- and the method that moves it, `crossApart(on)`, says nothing about the corner, so the next move is one CSS edit. The open drawer hides the cluster and the holder both. The page decides WHEN: `navPlaceCross()` asks `sunPhonePortrait()`, the same test the text box uses | gallery/nav_cluster.js (`crossApart`, `.nav-cross-apart`), `navFrameZoom`, `navHome`, `navCameraStep`, `navPlaceCross`, `sunPhonePortrait` | shared |
| Click deferral: `plotly_click` -> `setTimeout(0)` -> focus | initSunExhibit | shared, CRITICAL (L-278) |
| i-panel follows the focus; curated link per feature stamped into trace `meta` by `stampLink` | `renderSunInfo`, feature_renderers.js | shared mechanism; per-body copy and links |
| Frame HUD: camera-following triad, Aries glyph with the frame note and its source, grid chip | `sunHud*` | shared; reads the camera, never calls Plotly |
| Consent gate and Pyodide load | `loadPyodideRuntime`, `CONSENT_KEY` | shared |
| Back link: "Gallery" steps back in history when the gallery is behind it | BACK TO THE GALLERY block | shared |

The naming carries a debt: most shared pieces are called `sun*` because
the Sun was first. The rule is to rename or parametrize them, never to
copy them under `earth*`. One drawer, one nav cluster, one HUD, one
i-panel; the body is a parameter. Earth, the second room, PARAMETRIZED
through the `EXHIBITS` table and kept the names: a rename touches about
a hundred identifiers in a working room for no change a visitor sees,
and would put the Sun back under Mode 5. It is deferred to the third
room or a free session, with the names to reach for (L-309).

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
floats); + / - / Home and the four arrows (grid re-labels, chip follows;
a tap turns the same slice of screen at any zoom); drawer (the row's
left end ticks on the first try; a hidden shell draws and the view
rescales to hold it; GO on an unticked shell ticks and frames it); a
shell NAME (focus, the i-panel, and its text box -- mid-view with no
arrow on a portrait phone, pinned to the marker elsewhere; the whole box
on screen; sentences unbroken); a MARKER tap (opens on the first tap; a
tap on empty space closes the box); the HUD note (hover on desktop, tap
on phone); Gallery button then browser back; then landscape; then
desktop, where the text box and the tap are as they were. Report each
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

**A scene relayout must carry the live camera.** A 3D replot re-applies
the camera stored in the layout (`gl3d/scene.js`, `setViewport`), and a
touch rotation never updates that stored copy. So any `Plotly.relayout`
touching the scene -- opening a label, changing margins -- sends
`scene.camera`, read live, alongside whatever it came to change.
Otherwise the view snaps back to wherever the last mouse event left it.
(L-318, read from plotly.js v2.35.2.)

**A hover box keeps its pointer only when it fits to one side.** Plotly
puts the label to the right of its point if it fits, else to the left if
it fits, else centres it OVER the point with no pointer at all and nudges
it back on screen (`fx/hover.js`). So a wide hover string on a narrow
phone loses the line tying it to its marker, and whether it does depends
on where the marker sits, not on how much room there is. Wrap narrower,
or pin a scene annotation, which always points. (L-318.) Since round 5
the portrait phone's text box is a page annotation with no arrow at all,
on Tony's word ("very useful but not indispensable"); the desktop keeps
the pinned label. Plotly's OWN hover box on a marker tap still follows
this rule and Tony saw no problem with it once taps landed.

**A line break inside a sentence is soft.** Hover text is wrapped twice
-- at `HOVER_WIDTH` (70) for the desktop box and again at
`SUN_LABEL_WRAP_CHARS` (34) for the phone's text box -- so a hard `<br>`
that only keeps a desktop line short leaves an orphan word on the phone.
Write it as `GalleryFeatures.SOFT_BR` (`<br soft>`): Plotly draws it as
a break, because its text splitter reads a tag's name only up to the
first space (`src/lib/svg_text_utils.js`), and the phone's wrapper turns
it back into a space. A hard `<br>` stays for paragraph and list breaks.
`documentation/smoke_hover_budget.js` fails on a hard break inside a
sentence. (L-318 round 4.)

**A 3D tap takes the nearest drawn point from EVERY trace.** gl-plot3d
picks the point nearest the finger within `pickRadius` (10 px, set in
`src/plots/gl3d/scene.js`) across all traces, and only afterwards does
scene.js drop a pick whose trace has hoverinfo `skip` -- so a shell's
text-less dots win over its one info marker. On a portrait phone only,
`sunTapPicking(gd)` makes text-less traces draw nothing into the pick
buffer and widens the search to `SUN_PICK_RADIUS_PX` (22). It reaches
into `gd._fullLayout.scene._scene` (`glplot.pickRadius`, `glplot.update`,
each object's `drawPick`), is re-applied after every plot, and does
nothing if those are not where 2.35.2 keeps them. The desktop is
untouched: "the mouse pointer is fine enough to pick out the marker"
(Tony). (L-318 round 6; Tony: "always opens on first tap.")

### Hover text is written for the visitor [QUALITY]
Tony's standing rule, 2026-09-16: "In general we should avoid compressed
language in the hovertext." It is the protocol's Register Rule -- which
governs how Claude writes to Tony -- applied to what a visitor reads.
A hover names the thing and says it plainly. Project vocabulary
("served", "sourced", "drawing choice", "trusted arc", "L shell") and
capitalised labels ("DECLARED", "A DRAWING LIMIT", "FROZEN") are
compression: a visitor has not been through the conversation that gave
them meaning. The rule changes the WORDS, not the facts or the caveats.
A caveat stays beside its number, in words a visitor can use -- "It is
not a measured distance" rather than "DECLARED -- ... Not a measurement."
Citations, equations and served caveats live in the i panel, with one
pointer line under each hover (L-231); the hover is the glance. Reworded
hovers go to Tony before they ship. (L-331; the orrery's own hovers
follow under orrery-coding-conventions 1.9 and L-321.)

## Adding an exhibit: the order

1. Design round with Tony (above). Record rulings in the ledger item
   before code.
2. Served data: confirm the body's entry in `data/objects_config.json`
   has every feature the design draws, each measured value with
   value / unit / source / orrery_constant; add what is missing to the
   STORE first, then to the entry; confirm the nightly builder covers
   the body (gallery-cache-builder) and `coverage_index.json` lists it.
3. Code: one row in `EXHIBITS`; a driver spec whose `center` is the
   body; the body's half-range floor; the layout builder's per-body
   values; i-panel copy with sources inline. What goes in `objects` is
   whatever the resolver accepts against that centre -- RUN it, do not
   infer it. The Sun room passes `["sun"]`. Earth as an object is
   rejected, because the cache stores it relative to the Sun, so the
   Earth room passes `["moon"]` and Earth's own shells arrive by the
   centre-features path (L-291). Reuse the shared chrome by parameter
   (L-309 on names).
4. Pre-test here: `node --check` on the page script; a stand-in scene
   for chrome that can run without Pyodide (the CDN is blocked in the
   sandbox, so the exhibit itself cannot start here -- say so in the
   handoff); and `documentation/smoke_hover_budget.js`, given
   `interactive.html` as well as the renderers, which counts each
   hover's lines (soft breaks count; hard breaks inside sentences fail),
   holds every hover under `CEILING` (17, a ratchet that only comes
   down), measures the phone's text boxes with the page's own wrapper,
   and checks that each hover points at the i panel. It builds the Earth
   scene, Jupiter and Saturn; at b375cfe1 it does NOT build the Sun
   room, and four Sun hovers missed the move to the panel because of it
   (L-331). A checker passes on what it does not look at: when adding a
   room, add it to this suite before trusting its green.
5. Push; `gallery_maintenance_run.py --live`; Store drift reads MATCH
   for the new pointers, by name.
6. Mode 5 on the phone, sequence above; fix; repeat.
7. Card. FIRST read `gallery/gallery_metadata.json` for a card whose
   `live` already opens `interactive.html?exhibit=<key>`: Studio
   refuses a second one, and a card made some other way may already
   exist. Then Studio -> New Interactive Card (L-288) -> pick the scene
   (`live_scene_urls()` in `tools/json_converter.py` reads the keys of
   the page's `EXHIBITS` table, and the older branch form too) ->
   title, placard, sources -> it lands in Storage -> in the editor,
   File > Reload from disk (an open editor does not see Studio's
   write, and its Save All would write over it) -> place it; featured
   if it belongs on the lobby. Never make an exhibit card with the
   editor's Copy Card to Room: the copy keeps the source card's
   pairing tag (field note 2026-09-10).
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
- 2026-09-10, L-291 step 7: the first Earth card was a COPY -- Copy
  Card to Room on the static Earth-and-Moon portrait, then a live URL
  -- made because the Studio button was not found. It kept the
  portrait's `sibling` stamp, file and size, and index.html's Featured
  rule (a 9:16 card yields to a featured sibling) dropped it from the
  DESKTOP lobby while the phone showed it. The handoff written the
  night before said step 7 had not started: its session never read the
  metadata. A replay of the viewer's rule against the served metadata
  predicted both screens before Tony looked, and was right. Fixed by
  delete, then Studio, then the editor, in that order. The editor's
  Reload from disk existed and was not found either (L-288, L-312).
- 2026-09-15, L-318 round 3: a drawer row had two targets, an 18 px box
  and a name that did what GO did, and Tony's finger kept landing on
  the name of an unticked shell -- the camera moved and nothing drew, a
  tap that read as doing nothing. Measured in the page before any
  design: every pixel around the box belonged to the name. A one-target
  row with no box was proposed and withdrawn once Tony described his
  use (tick several, then go to one). Measure before you describe.
- 2026-09-15, L-318 round 4: Tony read the orphan words as unnecessary
  line breaks. Right about the words; measuring showed they cost one or
  two lines per box, and the box's WIDTH was the real height. Line
  counts written into the patch's notes before the run disagreed with
  the run on every row and were corrected before delivery.
- 2026-09-15/16, L-318 rounds 5 and 6: Plotly sometimes drew no arrow
  to a mid-screen box, and why was not pinned down; the arrow was
  removed on the phone instead. The tap fix went the other way -- the
  cause was read from Plotly's source first and worked on the first
  phone test. Three of five rounds changed something after Tony's eyes;
  the sandbox has no WebGL and no phone, and cannot see any of it.

## Install and verify

Author here: `skills/interactive-exhibit/SKILL.md` in the orrery repo.
Install to the account (Settings > Skills). Run `skills_index.py` so the
manifest in PROJECT_INSTRUCTIONS.md carries the version. Per Stale Skill
= Stop, the session that installs a version cannot verify the install.
1.0 was confirmed by the Earth sessions; 1.1 and 1.2 by the sessions
that followed their pushes. The first session after 1.3's push confirms
its loaded copy reads 1.3 before exhibit work.
