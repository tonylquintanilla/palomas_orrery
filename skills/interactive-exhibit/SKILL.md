---
name: interactive-exhibit
description: How an interactive exhibit (a room in interactive.html such as ?exhibit=sun) is designed, built, verified and carded for the Paloma's Orrery gallery. Covers the exhibit switch and boot path, the assembler driver spec, the JS feature handoff, the shared chrome (drawer, nav cluster, frame zoom, i-panel, HUD, consent gate, back link), what is per-body, the served-data provenance contract, what a room opens on (the arrival block) and the shell-key stamp the renderers apply, the drawer order, who may write data/objects_config.json, the Mode 5 phone sequence, and carding an exhibit through Studio. Use when adding or changing an exhibit (Earth, Jupiter, the stars), touching sun* chrome in interactive.html, deciding what an exhibit may render, or editing the served words with store_writer or exhibit_store_editor. Not for propagation math (gallery-assembler), the nightly builder (gallery-cache-builder), or the Studio/converter chain (gallery-pipeline). Do not use for projects other than Paloma's Orrery.
fires_when: adding or changing an exhibit in interactive.html; any edit to the Sun's chrome (drawer, nav cluster, frame zoom, i-panel, HUD, consent, back link); "Earth interactive", "?exhibit=", "new room in interactive.html"; deciding what numbers an exhibit may render and where they come from; what a room opens on (arrival block, drawn, moon); meta.shell_key and the trace stamp; editing the served words with store_writer or exhibit_store_editor; the Solar System room's drawer, its group rows, its two Resets, the Reset in every room's top bar, Home's order and its framing; Go To fitting a body's whole orbit and the orbit line in a body's hover; the count line's place; a bare interactive.html link and the Explorer's address; testing a room headlessly (tools/headless); carding an exhibit in Studio; choosing a feature's info link (NASA or Wikipedia); a served number's citation and its source_note; the Typed facts check (smoke_typed_facts.js); a feature drawn as stored dots (the Hills cloud, Earth's radiation belts); the i panel's source list and its links (source_list.js); the order a room's drawer lists its shells in, where each begins (drawer_order.js, the Drawer order check); a spacecraft's path in the Solar System room (its positions file, solid and dashed, its text box); whether the website and the orrery agree on an object; the planets ticked with a spacecraft (companions); the i panel's words one sentence to a bullet; a comet on an open path in the Solar System room; the drawer's groups one JPL class to a row; JPL's terms in the words a visitor reads; a comet's companions; the drawer's Find a body box; the direction arrows on the orbits; the grid chip's AU note and the triad's frame note; the i button's first-visit note and hovers without a pointer line; the one text box for a tap and Go To (text_box.js); a group found by its find words; the i panel's Report a problem link
---

# Interactive Exhibit

Read this file in 9 parts: lines 1-141, 142-161, 162-403, 404-501, 502-740, 741-973, 974-1187, 1188-1379, 1380-1487.

Skill version: 1.28 | 2026-10-28, with Anthropic's Claude Opus 5.5, at
palomas_orrery @ b2fcc1bb and gallery @ acbf206b. v1.28 (L-443, carrying
L-497, L-496 and L-458) corrects four sentences the gallery's builds of
2026-10-27 made wrong, each one a session following it would act on:
a group IS found by a word such as "comet" (L-496); the streamer belt
is drawn on its own row, not with the corona (L-497, 6b); Plotly's own
hover box is off in every room, so a marker tap opens the page's text
box (L-497, 6a), in the Phone first sequence and The touch path; and a
tap on a marker opens the text box, not only naming its row (the
anatomy table's drawer row). And it records three things new to the
gallery: `gallery/text_box.js`, the one text box's words one sentence
to a bullet; the `find` words on the drawer's rows; and the "Report a
problem" link in every room's i panel (L-458). Riding the same bump
(L-501): a body the served cache does not hold yet turns the Solar
System figures check red as well as Cache in step. Each fact was read
from the gallery's code at acbf206b before it was written.
Earlier: 1.27 | 2026-10-27, with Anthropic's Claude Opus 5.5, at
palomas_orrery @ 8d334e7 and gallery @ 7d422e5. v1.27 (L-443, carrying
L-493, L-494 and L-495) records the night of 2026-10-26. It corrects a
wrong sentence: no website hover ends with a pointer to the i panel any
more, and a first visit gets a note under the i button (Tony's option
C, L-494). A comet ticks a companion planet: on an open path the
farthest its path has reached so far (Tony: "so far"), on a closed
orbit the farthest its orbit reaches, by its aphelion; no asteroid or
dwarf planet ticks one (Tony: "only spacecraft and comets"). A group's
class is explained first in each member's text box and panel. And the
Find a body box, the grid chip's AU note, the whole triad opening the
frame note, the orbit line wrapped at 60, the direction arrows, and a
candidate for the headless recipe.
Earlier: 1.26 | 2026-10-26, with Anthropic's Claude Opus 5.5, at
palomas_orrery @ 5398439 and gallery @ 9223cd1. v1.26 (L-443, slice 2,
build B part 2) adds the fourteen comets on open paths to the Solar
System room, drawn from served positions as a spacecraft is, from a year
before perihelion to a year after today (the span ruling of 2026-10-24),
with no companions; splits every drawer group that gathered several of
JPL's classes into a row per class, the asteroids in their places among
the planets (Tony, 2026-10-26: "Split with asteroids in the correct
order among the planets"); and records his rule on JPL's words: "We
should keep these correct words and explain them when they should be
explained." The orbit line now reads "Orbit: perihelion q AU, its
closest to the Sun, to aphelion Q AU, its farthest." A name the orrery
keys with an underscore is shown with JPL's space.
Older entries are in documentation/SKILL_HISTORIES.md, moved there
on 2026-10-05 (L-418), 2026-10-10 (L-429), 2026-10-14 (L-431),
2026-10-16 (L-421), 2026-10-17 (L-452), 2026-10-20 (L-456),
2026-10-21 (L-460), 2026-10-22 (L-434, L-443), 2026-10-24
(L-477, L-482), 2026-10-25 (L-443, twice), 2026-10-26 (L-443),
2026-10-27 (L-443) and 2026-10-28 (L-443).

## Contents

Generated from this file's headings. skills_index.py --check fails
if this list and the headings disagree (L-418).

- What an exhibit is, and what this skill is not
- The anatomy of an exhibit (the Sun, read at fc8d9fb3; two rows corrected at 1.1)
- Rules
  - Design before code [QUALITY]
  - One chrome, many rooms [QUALITY]
  - Provenance is part of the build [CRITICAL]
  - What a room opens on is SERVED, not coded [QUALITY]
  - The Solar System room's drawer: bodies, not shells [QUALITY]
  - A room's drawer lists its shells where each begins [QUALITY]
  - A shell trace carries its key [CRITICAL]
  - Only two tools write the served config [QUALITY]
  - One check reads the file the browser fetches [CRITICAL]
  - Logic that needs no browser lives in its own file [QUALITY]
  - Never mutate a plot from inside a Plotly event handler [CRITICAL]
  - Scene text is scenery [QUALITY]
  - The frame zoom and the grid agree [QUALITY]
  - Aspect is read, not assumed [QUALITY]
  - Hover text gives km AND AU [QUALITY]
  - Phone first, and the conditions are stated [QUALITY]
  - The touch path is not the mouse path [QUALITY]
  - Hover text is written for the visitor [QUALITY]
  - A feature's info link: NASA if specific, else Wikipedia [QUALITY]
- Adding an exhibit: the order
- Field notes
- Install and verify

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
| `EXHIBIT` switch: `?exhibit=` lower-cased, default `solar-system` since 2026-10-22 (L-443, stage 10; until then `solar-system-explorer`); `EX = EXHIBITS[EXHIBIT]` is the room, and a key that is no room opens the Explorer, whose card links to `EXPLORER_EXHIBIT`, `solar-system-explorer` | interactive.html, `const EXHIBITS` | shared; a new room adds one ROW to `EXHIBITS` -- title, sceneTitle, pngName, halfRangeAu, driver, infoHtml, compose (since Earth step 3, L-291; at fc8d9fb3 it was one `EXHIBIT === "<key>"` branch per room) |
| `body.sun-exhibit` class and `.sun-chrome` show/hide rule, added for EVERY room | `applySunChrome()`, CSS | shared; the name stays `sun` until the rename (L-309) -- at fc8d9fb3 this row read per-body `body.<key>-exhibit` |
| Assembler modules list and the DRIVER: `assemble_scene({domain, content_type, objects, center, epoch}, Catalog(objects_config), CacheReader(coverage_index))` | `SUN_ASSEMBLER_MODULES`, `SUN_DRIVER` | shared code; per-body spec (`objects`, `center`) |
| Data read at boot: `data/solar-system/coverage_index.json`, `data/objects_config.json` | `initSunExhibit()` | shared |
| Feature handoff: `GalleryFeatures.buildFeatureTraces(features, positions, {sceneHalfRangeAu})`; anything larger than the frame goes to the drawer, not dropped | feature_renderers.js | shared |
| Arrival frame: measure every trace once (`sunTraceExtentAu`), half-range = 1.1 x the largest visible, floored at the body's constant (`SUN_HALF_RANGE_AU` 0.25) | initSunExhibit | mechanism shared; the floor and what is visible on arrival are per-body rulings |
| Layout builder: aspect 1:1:1 unless the body's physics says otherwise (the Sun's shells are spheres); axes state their unit; `tick0` 0 and `dtick` from `sunGridDtick(span)` | `buildSunLayout()` | per-body values, shared rules |
| Drawer replacing the legend: rows from `legendgroup`, `legendonly` hides, Reset in every room (L-477, L-482: the Solar System room's puts back its served opening and folds its groups, `ssReset`; the Sun's and Earth's put back their arrival, `sunReset`), focus row. A row's whole left end -- edge, box and colour dot, the full row height, about 65 px -- ticks and unticks; rows are at least 44 px tall; the name or GO on an UNTICKED shell ticks it and then frames it (L-318 round 3, amending L-267's G2 in that one case; GO still never hides anything). Since L-429 (Tony, 2026-10-10: "For uniformity rename the Go buttons in all rooms to Go To and center") the button reads GO TO and sits in the true middle of every room's row: the row is a three-column grid, the left end and the name in the first, Go To in the second, the room button (Solar System room) in the third; a long name wraps onto more lines rather than being cut. Naming a DRAWN shell also opens its hover text as a text box: on the desktop and a landscape phone a scene annotation pinned to its info marker with an arrow; on a portrait phone (`sunPhonePortrait()`) a page annotation centred in the view with no arrow, same text and width (L-318 round 5). Since v1.28 (L-497, 6a) it is the ONE text box: a tap on a marker in the picture opens the same box with that marker's words, and on a desktop a mouse resting on a marker opens it and moving off closes a box the pointer opened (`plotly_hover`, `plotly_unhover`, deferred out of Plotly's event); Plotly's own hover box is off (below, One text box). A tap in the scene, on the box, or on the backdrop closes it; the backdrop also closes the drawer; unticking closes it too (L-318) | `buildSunDrawer`, `sunApplyVisibility`, `sunFocusOn`, `sunLabelShow`, `sunLabelInstall`, `sunLabelRefresh`, `sunPhonePortrait`; knobs `SUN_LABEL_WRAP_CHARS` (34), `SUN_LABEL_PHONE_X` / `_Y` (0.5), `SUN_LABEL_FONT_PX` (12) | shared |
| Nav cluster: + / - / Home = FRAME zoom (range and dtick change together; the grid re-labels), plus four arrow buttons that turn the camera by a step scaled to the live eye distance, so a tap moves the same slice of screen at any zoom (L-310); on a portrait phone 768 px or narrower the arrow cross, Home with it, moves apart from + and - into its own holder, and the in-frame title stays (L-316). WHICH corner is set only by the `.nav-cross-apart` CSS rule in `nav_cluster.js` -- top right since round 4, after a round at the bottom left -- and the method that moves it, `crossApart(on)`, says nothing about the corner, so the next move is one CSS edit. The open drawer hides the cluster and the holder both. The page decides WHEN: `navPlaceCross()` asks `sunPhonePortrait()`, the same test the text box uses | gallery/nav_cluster.js (`crossApart`, `.nav-cross-apart`), `navFrameZoom`, `navHome`, `navCameraStep`, `navPlaceCross`, `sunPhonePortrait` | shared |
| Click deferral: `plotly_click` -> `setTimeout(0)` -> focus | initSunExhibit | shared, CRITICAL (L-278) |
| i-panel follows the focus; curated link per feature stamped into trace `meta` by `stampLink`; its last line, in every room, is "About Paloma's Orrery", opening the lobby's About card at index.html#about (L-475), and closing the card steps back to the room that opened it (L-480, index.html's `aboutFromRoom`). Under every focused feature, in every room, a "Report a problem" link with a line beside it (v1.28, L-458, talk D's approved words): it opens the guest book's Google Form with its message box already written, "Problem report -- <room> room, <feature>", two prompts, and "Page: <the room's address>"; the form's address and the box's field were read from the form's public page (`REPORT_FORM`), so no second form and no account. `tools/guestbook_updater.py` shows a message beginning "Problem report" to Tony as a report, private, never offered for the lobby | `renderSunInfo`, feature_renderers.js; `REPORT_FORM`, `REPORT_WORDS`, `sunReportMessage`, `sunReportLink` | shared mechanism; per-body copy and links |
| Frame HUD: camera-following triad, Aries glyph with the frame note and its source, grid chip. A tap or hover anywhere on the triad opens the frame note, not on the Aries glyph alone; the grid chip opens a note on what an AU is, its kilometres the served KM_PER_AU (IAU 2012 Resolution B2), its words resting on the IAU's Measuring the Universe page, both linked (v1.27, L-495) | `sunHud*`, `sunAuNote*`, `#sun-au-note` | shared; reads the camera, never calls Plotly |
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
- **The citation is the orrery's, served like the number** (v1.16,
  L-421 part 3; Tony's option A, 2026-10-16: "Yes, A as ruled"). The
  orrery's export (schema 7) carries each row's `source`: its own
  `# Source:` text with continuations joined; for a citation that reads
  "as <ROW>.", that row's citation followed by the rest; for a derived
  row with none, its inputs' citations, in the order its `inputs` lists
  them, marked `source_inherited`. `tools/mirror_constants.py` writes it
  into the linked entry's `source`, as it writes the value, and the
  Config mirror check (`tools/check_constants_links.py --mirror`)
  compares the two word for word and fails on a difference. So a
  citation beside a served number is never edited in the gallery: it
  changes in `constants_new.py`. A row with no citation on either side
  is named as declared; a citation only the website keeps, beside a row
  with none, is named and left alone; an export older than schema 7 is
  refused by name.
- **A `source_note` holds only a drawing choice** (v1.17, L-452;
  Tony, 2026-10-16: "Wording that is relevant to the citation should be
  moved to the store. Notes should be dropped unless they are drawing
  choices."). Wording that bears on a citation -- a locator, an
  edition, an address, what the cited value is -- lives in the store,
  on the row: in its `# Source:` text when it is part of the citation,
  otherwise in the row's other comment lines (`# Note:`, `# Read:`,
  `# Corrected:`, `# Also:`), which no visitor sees. Words written for
  the store -- "this row", "this file", "here", a figure count, the
  history of a correction, our own check -- never go in `# Source:`,
  because a visitor reads it word for word (L-450). A claim a visitor
  reads keeps a citation the visitor can see (Tony, 2026-10-17: "why
  drop the source?"): where a hover's sentence rests on a source the
  number's own citation does not carry, that source joins the row's
  `# Source:`, as the geostationary ring's NASA page did. The note is a
  served WORD: `tools/store_writer.py` and the exhibit store editor
  write it, and the mirror never touches it. The store writer refuses a
  linked entry's `source`, which is the mirror's. The i panel prints the
  citation on its Source line and the note after it, after a dash. It
  carries no project words: no names, no dates of rulings. A hover
  carries neither (Tony's split of 2026-09-15). These are three of the
  five principles in provenance-discipline, What a Visitor Reads,
  which hold every word a visitor reads in either instrument.
- **The i panel lists its sources, one to a line, every address a
  link** (v1.18, L-456; Tony from his phone, 2026-10-20: "need
  hyperlinks" and "need some kind of itemization for readability").
  Under the link out, "Source:" or "Sources:" and a bulleted list: each
  citation after its label in bold where it has one, the website's
  note after a dash, and every `http://` or `https://` address in it a
  link that opens in a new tab, long addresses wrapping on the phone.
  A renderer that GATHERS citations -- `withGatheredSource()`,
  `withShellWords()`, the exosphere's fade, Earth's four drawn guides
  -- serves them as a list, `source_items` ({label, text, note}),
  beside the joined `source` line, and `stampLink()` carries it into
  the trace's meta. The joined line stays exactly as it was, because
  every other check reads it. The list is never split out of the
  joined line: one citation can hold "; " itself. A citation the
  orrery's export built from other rows' citations (a derived row's
  `source_inherited`) arrives already joined and stays one bullet until
  the export serves it as a list. `gallery/source_list.js` decides what
  the list holds (`panelSources`) and where an address ends
  (`pieces`): a sentence's full stop or comma is not the address's, a
  closing bracket is only when the address opened one. A DOI written
  without its address stays text; its address belongs on the row's
  Source line in the orrery (provenance-discipline 2.32). The gallery
  run's "Source list" check (`documentation/smoke_source_list.js`)
  names, for every feature in the Sun and Earth rooms, how many
  citations it lists and how many carry a link.
- **Scattered dots are the orrery's stored drawing** (v1.17, L-330;
  the rule L-434 set for the Hills cloud). Earth's two radiation belts
  are dots scattered at random along dipole field lines (r = L
  cos^2 latitude; Koskinen and Kilpua 2022, sec. 1.2.1), between each
  belt's measured edges and thickest at its measured peak (Tony,
  2026-10-17: both belts curved, "Yes, random"). The orrery places
  them once, from a seed (`van_allen_belt_sampler.py`), and
  `export_drawings.py` writes `data/drawings/van_allen_belts.json`: in
  Earth radii, in Earth's body frame (z the spin axis), each dot with
  its weight and its belt. The website draws the dots as given, scaled
  by Earth's served radius and turned to the served pole, and places
  none itself. The fade is a declared drawing choice and the hover says
  so: drawn to show the shape, not measured. A shape that is a few
  numbers and a formula (a sphere, a ring) is not stored; the website
  computes it from the served rows.
  THE STORED DRAWINGS at gallery d7195704 with the L-434 patches, each
  `data/drawings/<name>.json`, named by its feature's `drawing.dots`:
  the Sun's corona (`sun_corona`), its zodiacal dust cloud
  (`zodiacal_dust`), the Hills cloud (`hills_cloud`), the outer Oort
  cloud (`outer_oort_cloud`) and the galactic tide (`galactic_tide`);
  Earth's radiation belts (`van_allen_belts`) and its exosphere
  (`earth_exosphere`). The tide and the outer cloud joined on
  2026-10-22 (L-434): placed once from seed 434 by the orrery's
  `galactic_tide_sampler.py` and `outer_oort_sampler.py`, each checked
  at its rows' edges where it is placed, the website's own generators
  for them gone. The tide's cone is not stored: two numbers and a
  formula, the website works it out from the served rows. The streamer
  band is not stored either: a grid set by about twenty served numbers.
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
- Text CLAIMS the page makes about ITSELF -- a room's own i-panel
  copy, the frame note -- carry their source in the page itself,
  because the assembler does not pass through the provenance scanner.
  The frame note's NAIF citation is the form.
- **A fact about one feature is served with that feature's words,
  never typed in a renderer** (v1.12, L-421). Code may type a sentence
  only when it is about the picture: a drawing choice ("drawn round",
  "our choice for the picture"), a frame limit, or how to use the
  page. A sentence about nature, about a paper, or naming a source --
  which particles a belt holds, how far a paper plots its model, the
  paper's name -- is served on the feature's row with its source, and
  the renderer prints what it is given. Where such a fact has no
  served row, the fix is a served row, not a typed line. The first
  case is Earth's inner belt: its "trapped protons" is the served
  `flux_peak_of`, beside the belts' other words. The rest found in the
  Earth and Sun rooms on 2026-10-06 are listed in
  documentation/MANIFEST_L421_typed_facts_20261006.md.
- **The typed-fact rule is checked, and the check gates** (v1.16,
  L-421 part 2). `documentation/smoke_typed_facts.js`, the gallery
  run's "Typed facts" row, builds the Sun and Earth rooms three times:
  as served, with every served word masked, and with every served
  number scaled. A sentence that survives the masking is typed. It
  passes only when the sentence is on the check's ALLOWED list (each
  with its class: about the picture, a frame limit, how to use the
  page, a number's label), and a number's own line passes when at most
  a few typed words sit beside the number. Each room's description in
  `interactive.html` is read the same way. The check prints its OPEN
  list without failing: sentences found on its first run and waiting
  for Tony's ruling (L-451). Adding a sentence to ALLOWED is a ruling,
  and the row prints the list in full so an addition is seen. The
  served words it masks are read from ONE home, `tools/store_writer.py`
  (`WORD_FIELDS`, `BELT_WORD_LISTS`, `SERVED_WORDS_PATCHED`,
  `SERVED_SETTINGS`); a served string under a feature in none of them
  is reported by name, never passed by silence. A new served word field
  is added there first.
- Where a value is unknowable or stylized (a dipole azimuth, the
  streamer belt's warp), the hover says so; silence reads as precision
  the model lacks (Show the Envelope of the Unknowable).
- **A hover prints a unit it is served; it never converts a served
  number to print it** (v1.5, L-345). The orrery's export serves each
  length row's value in km, AU, Earth radii and solar radii as `"in"`
  (schema 6), each worked out from the row's full digits and rounded
  once (provenance-discipline 2.22, Rule 3), and the mirror copies it
  onto the served node. A served number is already rounded, so
  multiplying or dividing it to print another unit is the rounded
  intermediate Rule 4 forbids -- the chromosphere read 0.00467 AU that
  way where its full digits give 0.00466. The page still converts
  freely to DRAW, where a rounded number moves nothing a visitor can
  see. A figure count is READ from the served entry, never recounted
  in the browser. A node with no `"in"` (an unvisited slice) prints as
  it did before.
- **The AU in brackets prints three figures, or the served count if
  that is fewer -- unless cutting to three would round a TIE** (v1.6,
  Tony's ruling of 2026-09-28). Three figures is Rule 7's one named
  format exception, a comparison aid kept short. But the served value is
  already rounded, and where the digits a cut to three would drop are
  exactly a 5 (5, 50, 500 ...) the page cannot know which way the full
  value leaned. There the served digits print in full. This is Rule 7's
  main rule -- print the declared count -- with the exception stepping
  aside, not a new exception. The inner core's 0.000008165 AU is the
  case. `auServed()` and `auTie()` in `feature_renderers.js` do it, and
  `documentation/smoke_display_figures.js` works the same test by its
  own arithmetic and NAMES each served tie in its report, so a new one
  is seen rather than only passed.
- **A slot measured in another unit is written from its row's `"in"`**
  (v1.6). A pointer names the row a number comes from, in the unit its
  source gives it, even where the slot is drawn in another unit --
  Earth's geostationary ring is drawn in Earth radii and points at the
  kilometre row. `tools/mirror_constants.py` writes such a slot from the
  row's `"in"` entry for the slot's unit: value, figures and print count
  as served. Nothing is multiplied in the gallery. A pointer is never
  aimed at a conversion name (`# Conversion:` in `constants_new.py`,
  orrery patch D20): those are not exported, and the export lists each
  one under not_exported with the row it is served through.
- **A shell may serve a `radius_note`** (v1.6): one sentence printed
  under its radius line, where the number needs a sentence to be read
  rightly. The crust is the case: drawn at Earth's mean radius, a little
  less than the one Earth radius used as the unit, which is equatorial
  (Tony's approved words, 2026-09-28). It is served words, so a change
  reaches a visitor only after the cache is rebuilt. Neither the mirror
  nor `store_writer` writes it; a patch does, as pointers are written.
- **A computed distance prints by the larger of two errors** (v1.7,
  L-398; provenance-discipline 2.23, A Computed Position Prints What
  Its Errors Earn). A body's distance in the Solar System room is
  worked out in the browser, so no row gives its count. The drift comes
  from the served cache's trust block; JPL's own accuracy is served on
  the body's entry in `data/objects_config.json` as
  `"position_accuracy"`, a link to its group's DE430 row (1 km, 100 km
  or 10,000 km, the PLACE JPL's words report to), written by the mirror
  like any other link. The page uses half a unit of that place as the
  error, takes the larger, and prints the Report test's place, never
  finer than whole kilometres. A body with no `position_accuracy`
  prints by drift and adds Tony's sentence of 2026-10-01, "JPL's own
  uncertainty for this position is not yet included." -- printed
  exactly when the link is absent, so the words and the data cannot
  disagree. The room's driver reads the link from the config, as it
  reads the rooms section; a change to it reaches a visitor on the push
  alone, with no cache rebuild.
- **A body's words and link come from the orrery's object list** (v1.8,
  L-395; Tony's rulings of 2026-10-01). On an object in
  `data/objects_config.json`, `name`, `horizons_id`, `id_type` where the
  list states one, `description` and `info_url` are COPIES written by
  `tools/mirror_objects.py` from `data/objects_export.json`, which
  `tools/pull_objects_export.py` fetches at the orrery's HEAD SHA; never
  by hand, and the Objects mirror check fails on a hand edit. An object
  is linked when its slug equals a `'key'` on an entry in the orrery's
  `celestial_objects.py`; every drawer row of the Solar System room
  must be linked. The room's info panel shows the row's own `about`
  where the room serves one (Pluto's barycentre sentence), otherwise
  the `description`, and links `info_url`; the hover does not carry
  either. A changed `horizons_id` reaches the served cache only when
  the builder runs, so Cache in step fails until it has (Apophis,
  2026-10-01).
- **A body's orbital period is the orrery's, printed as served**
  (v1.15, L-431 build 3; Tony's rulings of 2026-10-11, section 2 item 6:
  "periods are basic data, for all bodies and should be part of the
  hover text"). The object's `period` block in
  `data/objects_config.json` is a COPY written by
  `tools/mirror_objects.py` from the orrery's export (schema 2), never
  by hand: `kind` (`fetched`, `typed`, `none`), `center` and
  `center_label`, `fetched` (the date), and `years` and `days` each as
  value, figure count and the orrery's printed text. The page prints
  the served text, never a recount (`SolarSystemFigures.periodLine`,
  shared by the Solar System room's body hovers and the Earth room's
  Sun Direction). Three forms, and nothing else: "Orbital period: N
  years (M days), around <centre>, from JPL Horizons, fetched <date>.";
  "Orbital period: N years (M days). Typed value, not fetched from
  JPL." -- printed, marked, so the website and the orrery agree; and
  "Orbital period: not yet fetched from JPL." A body with no block (the
  Sun) prints no line; a fetched period served with no centre prints no
  line and the room says why in its warnings. The block is read from the
  config by the room's driver, so a change reaches a visitor on the
  push alone. An object without a `'key'` in the orrery's list (the
  Moon, today) has no period to serve.
- **The orbit is drawn around the period's centre** (v1.15, L-431 build
  3). Where a body's period is around the solar system's barycentre,
  the served cache carries `drawn_orbit`, the body's elements around it
  at the date of its Sun-centred ones; the room draws that ellipse,
  moved by `render_orbits.drawn_orbit_offset` to where the barycentre
  sits seen from the Sun, and draws no perturbation lines for it.
  The orbit's info marker names that centre. Without a `drawn_orbit`
  the room draws from the Sun-centred elements, as the orrery does, and
  its warnings say the builder has not run. It is cache data, so it
  needs the builder; `tools/check_cache_in_step.py` fails until it has
  run.
- **The website and the orrery agree on every object both draw, or the
  difference is written down** (v1.24, L-484; Tony, 2026-10-24: "we
  should add to the skill a check that the website and the orrery agree
  or we have a documented exception"). For each object both instruments
  draw they agree on its JPL record, its name, its dates and its words,
  or the difference is a documented exception. The check that holds this
  is not built: it is to find every disagreement and name it, object by
  object, fail on an undocumented one and print a documented one every
  run with its reason. Its first known findings are C/2025 K1's record
  (L-470, fixed) and the orrery's typed dates for each path and comet,
  which L-476 replaces with the path plan's. Until it is built, a build
  that serves an object compares the two by hand and says what it found.
- The Artifact Bounds the Audit, and The Braid orders it: the new
  exhibit's pointers are the slice; a provenance gap found elsewhere
  while building it is recorded, one ledger row per CLASS, not chased.
  This is the same discipline the orrery reached retroactively, applied
  to the assembler as it is built (Tony, 2026-09-06).

### What a room opens on is SERVED, not coded [QUALITY]
Each room's object in `data/objects_config.json` carries an `arrival`
block: `drawn`, a list of shell KEYS, and `moon`, true or false.
`GalleryArrival.applyArrival` in `gallery/arrival.js` applies it before
the opening view is measured, so the view fits what is drawn. With no
block the page behaves as it did before arrival blocks existed --
nothing is hidden.

Tony's ruling, 2026-09-17, and it supersedes two earlier rulings of his
own (the Sun's 0.25 AU arrival of 2026-08-29 and L-291's eight-shell
Earth arrival): a room opens on "the surface shell plus frame elements
like sun direction, axes, terminator", and the Moon starts "with its box
not selected". There is NO floor under the opening view.

THE ARRIVAL BLOCK IS THE ONE PART OF A ROOM'S DATA THE PAGE READS
DIRECTLY. Everything else a room draws comes from the served cache under
`data/solar-system/`, which the cache builder writes. So a change to
`drawn` or `moon` reaches a visitor on the PUSH ALONE, while a change to
a shell's words does not reach them until the cache has been rebuilt.
Say which when telling anyone what a change will do.

**A ROOM THAT IS NOT ONE BODY keeps its settings in the config's
top-level `"rooms"` section** (v1.7; Tony's ruling of 2026-09-30,
"confirmed as recommended", L-392), keyed by the room's `?exhibit=` key.
The Solar System room's entry holds `arrival` -- `drawn`, the slugs
ticked on opening, and `highlight`, the row highlighted and named on the
closed drawer's handle -- and `drawer.rows`, its rows by slug in order
outward from the Sun (a served `see_more` is not read since v1.22,
L-477, and the drawer check fails on one). Since v1.21 a row may
be a GROUP row, `group` and `label`, and a body row names its group in
`in` (the next section). A row may carry the
WORDS a visitor sees for it: `label`, the name shown when it is not the
served name; `about`, a sentence for the text box and the panel; and
`source_note`, what the Horizons id in the source line is. Pluto's row
is the case: label "Pluto", Tony's barycentre sentence, and "the
Pluto-Charon barycenter". The page reads this section directly, so a
change reaches a visitor on the push alone. The cache builder and the
assembler read only `"objects"` and ignore it -- checked before the
section was added, and the reason it could be added without touching
them. Other readers have joined since, so do not repeat the older claim
that EVERY reader ignores it: `tools/mirror_objects.py` reads its rows
(v1.8, L-395), and `tools/store_writer.py`, `tools/exhibit_store_editor.py`
and their two suites read it (v1.9, L-404).

WHAT MAY BE EDITED IN A ROOMS-SECTION ROOM (v1.9, L-404): its arrival's
`drawn` and `highlight`, through the store writer, and nothing else in
the section. Each must name a drawer row other than the Sun, which is
the fixed centre and always drawn; the writer refuses anything else,
because the page would warn about it and highlight nothing. The editor's
room list is `store_writer.room_ids()`: the body rooms by slug, then the
section's rooms by key, so a room added in EITHER place appears with
nothing else to change. Until 2026-10-01 the list read only `objects`,
and the Solar System room, built the day before, could not be chosen at
all -- found by Tony at the editor. A row's own words (`label`, `about`,
`source_note`) are not in the allow list; a change to them comes as a
patch, and whether the editor should take them is Tony's question.

### The Solar System room's drawer: bodies, not shells [QUALITY]
v1.9, L-363 step 3b. It is the SAME drawer as the Sun's and Earth's --
One chrome, many rooms -- with four things added for a room whose rows
are bodies. A room gets them by handing `drawer` (its served rows and
opening) back from its `compose`; the page then sets `ssDrawer`, and the
`ss*` functions above `buildSunDrawer` do the work. In the Sun and Earth
rooms `ssDrawer` is null and every branch that asks is skipped. Each
decision is made in `gallery/solar_system_drawer.js`, checked by
`documentation/smoke_solar_system_drawer.js` (a gating checker that
breaks the file three ways first); the page only touches the DOM and
Plotly.

- **The Sun's row is fixed**: no tick box, no GO, never unticked by
  Reset. It still highlights and opens. The Sun's trace group is
  `center` (the assembler's centre marker), not its slug.
- **A row opens, and a room is one tap away.** Tapping a name
  highlights the row and opens it; a second tap closes it. Ticking a
  body opens its row too (Tony, 2026-09-30). A body whose slug is a key
  in `EXHIBITS` shows "Enter the <name> room" on its OWN row, to the
  right of Go To, always and on every screen, so one tap enters the
  room (L-429; Tony, 2026-10-10: "so the visitor does not need to tap
  the row to see the button then tap again"; and "Go To, takes them
  the orbit and hovertext. if there is a room, it opens the room. in
  that order"). The Sun's row keeps Go To's space, hidden, so its
  button lines up. A body with no room opens to "No room or
  cards yet": under the row upright, on the name's line with the phone
  sideways (Tony, 2026-10-03). Both are read from the page's own table,
  so the next room lights its row by itself.
- **No See more** (v1.22, L-477; Tony, 2026-10-24: "No "see more" Let
  that be permanent."). He found the referents mixed: "See more/fewer
  rows all/none celestial objects" -- See more acted on the list, All /
  none on the picture, and a group row's name and box did one each. So
  each control acts on one thing: every group is always listed, folded
  shut, and nothing behind a button.
- **One body at a time, and Reset** (v1.22, L-477; Tony: "change
  all/none to "Reset" that resets the view to the starting view when
  the visitor wants a fresh start," and "The starting view is unticked.
  The visitor tries some objects. A Reset button can bring back the
  original unticked list. "All" is very confusing with too many orbits
  all at once. It is better for the visitor to develop the view."). In
  this room the top bar's button reads Reset (`WORDS.reset`; `ssReset`,
  through `ssHome(gd, true)`): what the room opened on, ticked, in its
  opening order, its highlighted row named, every group folded, the
  opening frame and angle, the drawer closed. Inside an open group, once
  one of its bodies is ticked, "Reset <group>" unticks them all and no
  other (`groupReset`, `groupResetOffered`; `ssGroupReset`). Nothing
  ticks many bodies at once, save a spacecraft or a comet and its
  companions (v1.25 and v1.27, below). Since v1.23 the Sun and Earth rooms have
  the same button (L-482; Tony, 2026-10-24: "Yes all rooms should use
  the same Reset button and no 'see more'"). There it puts back the
  room's arrival: every shell ticked or unticked as the room opened,
  recorded once at boot from the drawer as the served arrival block left
  it (`sunOpening`, `sunOpeningState`), so the opening has one
  definition and Reset never reads the block a second time; then the
  text box closes and Home runs, the opening frame and angle with the
  drawer closed (`sunReset`). It replaced All / none, which ticked or
  unticked every shell. No room has a See more.
- **Home remembers the tick order**, for the open tab only: the last
  body ticked that is still ticked, at the opening angle, drawer closed,
  falling back through the order. With nothing ticked it puts back the
  room's SERVED opening -- the one time Home changes what is drawn.
  Reset differs: it puts back the opening whatever is ticked, and folds
  every group shut; Home keeps the ticks.
- **Selecting moves nothing.** A tap on a body in the picture
  highlights its row and opens its hover; a name tap highlights and
  opens the row. Only GO moves the view. (These, the Sun's missing GO,
  Home's served opening and the opening frame below were Claude's calls
  inside the build; Tony confirmed all five on 2026-10-02.)
- **Rows are found by the group they name** (`data-k`), never by their
  place in the list: opened rows, group rows and a group's Reset sit
  between them. `renderSunDrawer` does this for every room.
- **Groups fold open** (v1.21, L-443; Tony, 2026-10-22, at the mock-up:
  "B. this is the right view. the "room" would only apply if the
  object has additional features beyond the symbol such as future moon
  shells, or spacecraft encounters, or comet perihelion encounters, or
  asteroid near earth encounters, etc."). A served row `{group, label}`
  gathers the body rows that name it in `in`, listed after it. It is
  always listed (since v1.22, L-477). A tap anywhere on its row folds it
  open or shut and moves nothing; where a body row has its tick box it
  has its fold arrow (`groupArrow`); folded, its bodies hide, open, they
  show indented under it. It ticks nothing: until v1.22 its box ticked
  every body in it, and a thumb reaching for its name landed there
  (Tony's phone look of 2026-10-23). Its line counts its bodies, and how
  many are ticked. A group is never a body: it is not counted, ticked,
  or offered a room.
  `"order": "a"` lists its bodies by their served semi-major axis,
  nearest first (`orderGroups`, from each body's `a_au`, which the
  driver now hands the page); without it they keep the served order,
  the comets' by first apparition. Each group is JPL's own class for
  its bodies (the Small-Body Database's orbit class), not a judgement,
  and one class to a row (v1.26; Tony, 2026-10-26: "Split with asteroids
  in the correct order among the planets"). The rows, in the drawer's
  order: after the Sun, Encke-type comets (ETc), Jupiter-family comets
  (JFc), Halley-type comets (HTC), Comets (COM), Hyperbolic comets (HYP)
  and Interstellar objects (the IAU's "I" numbers; JPL gives HYP, and
  HYA for 'Oumuamua); Aten asteroids (ATE) after Venus; Spacecraft after
  Earth; Apollo (APO) and Amor (AMO) asteroids after the Spacecraft;
  Main asteroid belt (MBA) after Mars; Jupiter Trojans (TJN) after
  Jupiter; Centaurs (CEN) after Saturn; Trans-Neptunian objects (TNO)
  after Pluto. A comet group without "order": "a" lists its bodies by
  designation, which is the order they were found. The classes were
  read live for every body on 2026-10-26
  (documentation/CHECK_L443_drawer_classes_20261026.md); no body sat in
  the wrong group, and two groups had gathered several classes. This supersedes the
  front-door design's line that a group's bodies appear only in the
  group's room (2026-09-29): a group may still get a room, with a cloud
  drawn, when it has more than its bodies to show. The logic is in
  `gallery/solar_system_drawer.js` (`rowsFromServed`, `rowVisible`,
  `groupCount`, `groupArrow`, `groupReset`, `groupResetOffered`,
  `orderGroups`); the page's part is `ssBuildRows`, `ssGroupReset`,
  `ssFold`. Checked by the drawer check's sections 4 and 6, with seven
  planted faults, and walked headlessly (`walk_solar_system_drawer.js`,
  sections 1, 6, 11, 15 and 16).
- **Every comet is drawn from its elements of today** (v1.21; Tony's
  ruling of 2026-10-22, "Yes"). A comet anchored at perihelion
  (`overrides.comet.anchor: "Tp"`) is trusted only for a span around
  that date: Encke's had ended in May 2025 and Halley's in February
  2024, which is why neither was in the drawer. Anchored at today, the
  marker is where the comet is now, and the ellipse is today's orbit.
  The builder keeps the perihelion path, held by its offline tests on a
  copy of the config; a comet's own room can show the perihelion orbit
  later.
- **The front door** (v1.21, stage 10; Tony's ruling of 2026-10-01): a
  bare `interactive.html` opens this room. The Explorer's card links to
  `interactive.html?exhibit=solar-system-explorer`, and
  `tools/json_converter.py`'s scene list reads the page's
  `EXPLORER_EXHIBIT` to offer it.
- **The count line** (L-472, Tony's ruling of 2026-10-23; its place
  L-478, 2026-10-24). Zooming in stays a cutout in every room. When
  ticked bodies lie outside the view, one line says how many, never
  which: "1 ticked body is outside this view", "N ticked bodies are
  outside this view" (`outsideCount`, `WORDS.outside`; `ssOutsideUpdate`,
  called at the end of every frame change). A body is outside when its
  marker is past the box on any axis. Hidden at zero. It sits at the
  lower left, above the drawer's handle, a page element of its own
  (`#ss-outside`, class `sun-chrome`); until L-478 it sat above the grid
  chip and covered the Aries mark. It steps aside with the HUD while the
  drawer is open.
- **The orbit line** (v1.22, L-479; Tony, 2026-10-24: "It would also
  give an intuitive sense of the eccentricity," then "Yes" to one short
  line). Every body on a closed orbit ends its hover with "Orbit:
  perihelion q AU, its closest to the Sun, to aphelion Q AU, its
  farthest." (the words since v1.26; JPL's terms kept and explained,
  below), perihelion a(1 - e) and aphelion a(1 + e) from its
  served Sun-centred elements (the driver passes `e` beside `a_au`),
  never typed: `SolarSystemFigures.orbitLine`. Three significant
  figures, the length of the AU in brackets on the shell hovers (a
  comparison aid kept short, Tony's ruling of 2026-09-28), never finer
  than the Report test's place for the error the body's distance line
  uses. An open orbit prints no line and the room's notes say why.
  Checked by the figures check's part 6, with three planted faults, which
  prints every body's line. The line is wrapped at 60 characters like
  every other bullet (v1.27, L-495): it was the one left unwrapped, and
  Halley's ran 88, so the box Plotly opens on a tap came out wider than
  a phone's view and was cut on both sides (Tony: "The hover tapping the
  object overruns its box").
- **The spacecraft** (v1.24, L-443 build B, 2026-10-25). A group row,
  Spacecraft, right after Earth's row (Tony, 2026-10-24), the twelve in
  launch order, each with the label a visitor reads where the orrery's
  name is shorthand (OSIRIS-APEX, Parker Solar Probe, Solar Orbiter,
  Psyche spacecraft, Europa Clipper). A spacecraft is drawn from its
  served positions file (`positions/<slug>.json`), which the page
  fetches for the room's own rows before the driver runs
  (`solarSystemPositionFiles`, the room's `servedPositions: true`) and
  hands to the assembler through the CacheReader as `POS_JSON`; the
  assembler opens no file. `gallery/assembler/render_spacecraft.py`
  splits the path at the minute shown: solid behind, dashed ahead --
  JPL's predicted part, never a line extended -- the two
  meeting at the marker, the orrery's diamond-open, in the orrery's
  colours. The marker is worked out on the parabola through the three
  served points nearest the minute, and its error is that parabola's
  distance from the straight chord between the two points either side;
  near today the builder serves a point a day. The text box, Tony's
  words of 2026-10-25: the distance to the place that error earns, never
  finer than whole kilometres (`SolarSystemFigures.pathDistanceLine`);
  the sentence that JPL's own uncertainty is not yet included, always,
  since a spacecraft's is not served; and "Its path is solid where it
  has already flown, and dashed where JPL's predicted path takes it next,
  as far as <the served path's last day>." No period line and no orbit
  line. Its source line (`spacecraftSourceLine`) names the Horizons id,
  the span drawn, the day retrieved and the plan's step. The panel shows
  the orrery's description and link, as for any body. A row the served
  cache does not hold yet -- before the builder has served a new body,
  or when its first fetch failed -- is named in the room's notes and left
  out, rather than stopping the room. The gallery run is red on it twice
  until the builder serves it, both correct, one cause: Cache in step,
  and the Solar System figures check ("<slug>: the served cache has no
  as_of_today or trust"; v1.28, found adding 2026 ED138, L-501). Checked by the figures check's
  part 7 (three worked cases, two planted faults, every served
  spacecraft) and walked headlessly (`walk_solar_system_drawer.js`,
  section 20, shown failing once on a predicted part drawn solid).
  "Predicted" is JPL's own word, by Tony's ruling of 2026-10-25 ("use
  the word JPL uses"): Juno's data sheet calls its part after
  2026-09-23 "a planning prediction"; Voyager 1's speaks of "a new
  solution and prediction".
- **A spacecraft's companions** (v1.25, L-443; Tony, 2026-10-25: "in
  addition to the default inner planets, add the farthest planet orbit
  that the object has reached ... This gives perspective to a spacecraft
  plot," then "Maybe flyby planets too," and "Yes" to the rule). Ticking a
  spacecraft, or Go To on one not ticked, also ticks among the drawer's
  top-level body rows -- the planets and Pluto, the rows no group
  gathers, so no list of planets is typed -- every one its path plan
  names as a flyby, arrival or departure (matched by any name the row
  goes by: Pluto by its label), and the farthest whose perihelion
  a(1 - e) its path goes beyond, Pluto the last. The path is the whole
  one drawn, predicted part included; its reach is the farthest served
  point from the Sun, worked out by the driver (`path_reach_au`, beside
  `path_events`), never typed. The logic is
  `SolarSystemDrawer.companions`; compose works each spacecraft's out and
  hands them to the drawer (`drawer.companions`); `ssTickCompanions`
  ticks them before the spacecraft in Home's order, so the handle names
  the spacecraft. They are ordinary ticks: unticking the spacecraft
  leaves them, and Reset puts the room back as it opened. A plan's name
  no row goes by (the Moon) is reported by the logic and ticks nothing.
  A comet ticks companions by the same logic, reached by a different
  rule (A comet's companions, below).
  Voyager 1: Jupiter, Saturn, Pluto; Voyager 2: Jupiter to Neptune and
  Pluto; Juno, Lucy, JUICE and Europa Clipper: Jupiter. Checked by the
  drawer check's section 7 (seven cases, two breaks) and walked
  (section 20: Juno, and Voyager 1 by Go To).
- **The comets on open paths** (v1.26, L-443, slice 2, build B part
  2). Fourteen comets whose orbit is open, or too near open for an
  ellipse to mean anything -- ten hyperbolic comets, the three
  interstellar objects and piece C of C/2025 K1 -- carry `open_path`,
  marked in the orrery's object list and copied by the mirror. Each is
  fetched by its own path plan, as a spacecraft is (horizons-orbital-
  mechanics, How a Path's Events Are Found; gallery-cache-builder, A
  Spacecraft Is Fetched by Its Plan), and drawn the same way: solid
  behind the minute shown, dashed after, meeting at the comet's diamond,
  through the same `render_spacecraft.py` with the comet's symbol
  (`symbol_for`). The span is Tony's ruling of 2026-10-24: a year before
  its perihelion to a year after today, inside JPL's data. Its driver
  kind is `comet_path`. The text box, Tony's words of 2026-10-26
  (documentation/WORDS_L443_comets_20261026.md): the distance line and
  its note, as a spacecraft's; "Its path is solid where it has already
  travelled, and dashed where JPL predicts it will go, as far as <the
  last day>."; and "It is drawn from a year before its perihelion to a
  year after today, or less where JPL's path stops sooner; those two
  years are our choice for the picture." The source line names no "as
  far as JPL's data runs" and says the points are closer together around
  its perihelion. No period and no orbit line; its companions are the
  bullet after next (until v1.27 this said it had none). The room's
  second list has a bullet for them. Walked (section 21: the groups'
  places, West, C/2025 K1's name, Go To on 3I/ATLAS, Reset).
- **A name keyed with an underscore** (v1.26). The orrery keys the four
  pieces of C/2025 K1 as "C/2025_K1", "C/2025_K1-B" and so on; the
  room's driver shows every served name with a space where it has an
  underscore, and looks nothing up by name.
- **A comet's companions** (v1.27, L-443 and L-495). A comet ticks a
  companion planet as a spacecraft does, by the same logic
  (`SolarSystemDrawer.companions`), and no other kind of body does
  (Tony, 2026-10-26: "Not every body, not minor planets, only spacecraft
  and comets"); an asteroid or a dwarf planet ticks nothing with it. A
  comet on an OPEN PATH ticks the farthest planet whose perihelion its
  path has passed SO FAR, up to the minute shown: its dashed year ahead
  is a drawing choice, not JPL's plan, so it does not count (Tony: "so
  far"; `_path_reach_au` with the moment shown, in the room's driver).
  West, McNaught, 'Oumuamua and 2I/Borisov bring Pluto; 3I/ATLAS
  Saturn; the rest Jupiter. A comet on a CLOSED ORBIT ticks the farthest
  planet its orbit reaches, judged by its aphelion a(1 + e) from the
  served elements, since its whole orbit is drawn (`closedComet` in the
  room's compose): Ikeya-Seki, Halley, Hale-Bopp and the other long
  orbits bring Pluto; Churyumov-Gerasimenko and Schaumasse Jupiter;
  Encke, Tempel 2 and Howell Mars, already ticked.
- **The Find a body box** (v1.27, L-493; Tony, 2026-10-26: "as we create
  more objects in the website, could we add a search window to find the
  right row?"). At the top of the Solar System room's drawer. It matches
  a body's four names: the drawer's label, the orrery's name, JPL's name
  (`horizons_name`, copied by the objects mirror from the orrery's
  export) and the Horizons id where that id is a designation, not a bare
  number. It ignores capitals, spaces and punctuation, and matches part
  of a name. A group with a match opens and says how many of its bodies
  show ("1 of 10 shown"); a body found only by JPL's name or its id says
  which, under its name ("JPL's name: ATLAS (C/2025 K1)"). The clear
  button or Reset empties the box. The logic is the drawer file's FIND
  (`searchKey`, `searchNames`, `searchHits`, `searchVisible`,
  `searchGroupCount`, `searchVia`); checked by the drawer check, with two
  planted breaks, and walked.
  A GROUP IS FOUND TOO (v1.28, L-496; Tony's ruling of 2026-10-27,
  "results list matching groups closed, with counts; choosing one opens
  it; a single match opens directly"). It matches the group row's label
  and its `find` words, served on the row in the rooms section: JPL's
  class code and plain words ("comet" on the five comet groups; "HYA",
  "comet" and "interstellar" on the interstellar objects; "asteroid" on
  the asteroid groups, with "near-Earth" on Aten, Apollo and Amor;
  "probe" and "mission" on the spacecraft; "CEN" on the centaurs; "TNO"
  and "Kuiper belt" on the trans-Neptunian objects). A body row may
  serve `find` too: the eight planets serve "planet", which is no row's
  label, and Pluto serves none. Several groups matching are listed
  closed, each with its count ("n bodies"), and the count line names
  groups ("6 groups match"); choosing one clears the box and unfolds it,
  ticking nothing; one group alone, with no body found outside it, opens
  whole ("probe" opens the twelve spacecraft). The box still reads "Find
  a body". The logic is the drawer file's GROUPS FOUND (`searchHits`
  returns `listed` and `opened`; `searchOpen`; `WORDS.listed`,
  `WORDS.found`), checked by the drawer check's section 8b with two
  planted breaks. The `find` words were written by hand into
  `data/objects_config.json`; neither `tools/store_writer.py` nor the
  exhibit store editor takes them, as they take no other word of a
  rooms-section row (`label`, `about`, `source_note`).
- **The direction arrows** (v1.27, L-495; Tony, 2026-10-26: "a small
  directional arrow right on the orbit line near the objects showing the
  direction of travel of objects. This is to make clear what the orbit
  is"). A flat arrowhead in the orbit's own plane, on each drawn body's
  orbit or path, its tip five arrowhead lengths ahead of the body (Tony
  chose the style and the distance from renders of the real room). Its
  direction is never typed: an orbit is served in order of true anomaly
  (`render_orbits.sweep_conic`), which grows the way the body moves, and
  a path in time order, so the arrow points from each point to the
  next; Halley and Ikeya-Seki point clockwise. Its size is a fraction of
  the view's width, so it keeps its size on screen, and it is placed
  again at every frame change, outside the Plotly event (L-278). It is
  not drawn when its tip falls outside the view, or when the line is too
  short for it at that scale. It sits in its body's legend group with
  no hover. `gallery/direction_arrows.js`, checked by the gallery run's
  Direction arrows check (`documentation/smoke_direction_arrows.js`: six
  worked cases, and the real file broken three ways first), which
  gates; the orrery's dashboard has its button.

**FRAMING, Tony's ruling of 2026-10-02** ("B but with a buffer of
20%"): the room frames on how far each body is from the Sun NOW, not
on its whole orbit, and the farthest body ticked sets the frame. Two
parameters on the room's `EXHIBITS` row carry it, `frameOnPosition:
true` and `frameMargin: 1.2`; `sunGroupRadius` then returns the
position marker's distance (`sunPositionRadius`) and `sunFrameMargin()`
the 20%. The opening view, Home and GO follow the same rule, and the
opening has no 1.2 AU minimum. The Sun and Earth rooms keep framing
whole shapes at 10%. Part of a stretched orbit runs past the box and is
CUT OFF at its edge until the visitor zooms out: gl-plot3d clips each
trace to the axis ranges (`clipToBounds`, on by default, read from the
Plotly 2.35.2 bundle). Put to Tony with each body's numbers, after a
first summary that said the two framings differ only for stretched
orbits -- wrong: in a square box they also differ wherever a body sits
toward a corner, by about a third for Jupiter under the tightest rule.

**GO TO FITS THE WHOLE ORBIT, Tony's ruling of 2026-10-24** (L-479,
"Let's try B1", a trial his phone look settles). Sedna, ticked, was
framed about 99 AU out while its orbit reaches about 1,000 AU, so its
orbit was cut with the body in view, and the count line said nothing.
Go To now fits the body's whole drawn group -- its orbit -- at the same
20% (`ssGo` passes `whole` to `sunApplyVisibility`, `sunFocusOn`,
`sunFrameOn` and `sunGroupRadius`, which then measures the group's
traces as the Sun and Earth rooms do), and opens its text box as
before; one tap on the picture closes the box. Ticking, Home and Reset
still frame on where the bodies are now. A zoom-out tap never makes a
view smaller, even one Go To set past the buttons' 5,000 AU cap
(`navFrameZoom`). A spacecraft's Go To fits its whole drawn path, flown
and predicted, the same way (v1.24), and so does a comet's open path
(v1.26).

### A room's drawer lists its shells where each begins [QUALITY]
v1.19, L-460. Tony's ruling of 2026-10-20: in every room each shell
takes its place in the drawer at the distance where it begins,
"basically when we reach that shell's distance, that is its place in
the order." And on 2026-10-21, looking at the list: "the order goes by
the distance of the nearest part of the feature. if the visualization
is displayed according to the sourced distance data, then they are
correct. this is not a visual judgement."

So the order is READ, never typed. `gallery/drawer_order.js`
(`DrawerOrder.plan`) reads it from the room's served rows when the page
opens, before anything is cut to the view, and `buildSunDrawer` lists
the legend groups in that order. A new shell takes its place with
nothing else to change. The Solar System room is not ordered here: its
rows are bodies, served outward from the Sun (the section above), and
the page never calls the file for it.

WHERE A SHELL BEGINS is the first of these its served row has, each
the nearest part of the feature as it is drawn:
1. `inner_radius`, the row's own inner edge (the Hills cloud, the
   clumps, the tide, Earth's exosphere);
2. `drawing.dots`, a stored drawing: its nearest dot as drawn (the
   corona, the zodiacal dust cloud, Earth's radiation belts);
3. `standoff`, a surface fitted to the solar wind, at its nose (the
   magnetopause, the bow shock);
4. `drawn_radius`, a shell drawn at a distance other than the one it
   reports, where it is drawn (the Roche limit: drawn at its formula's
   full answer, 3.45 solar radii, where its row reports 3);
5. `radius`, a sphere or a ring;
6. `range.low`, a band at its near end;
7. a shape in `FRAME_SHAPES` (the galactic plane): a reference across
   the frame, not a region, so it has no distance and keeps its place;
8. otherwise the nearest point the page drew.
Lengths are compared in AU, converted as the renderers convert them:
km by the served KM_PER_AU, solar and Earth radii by the body radius
the shell's own group serves.

`drawn_radius` is read only on a row that also reports a `radius`
(L-460, 2026-10-22): Earth's magnetotail carries `drawn_radius` for its
WIDTH about its axis, 30 Earth radii, and reports no `radius`, so it
is placed by the nearest point drawn, where it begins at 30.6.

A ROW OPENS ITS OWN WORDS (L-468, 2026-10-22). Naming a row opens the
info cross of the row's OWN feature, not the first cross the group
holds. `GalleryFeatures.labelTraceIndex(traces, indices)` makes the pick and
`sunLabelMarker` in `interactive.html` asks it; the gallery run's
"Label words" check (`documentation/smoke_label_words.js`) holds every
shell row in both rooms to it, with a planted fault. Tony's phone look
of 2026-10-21 found the corona's row opening the belt's old words.
ONE ROW, ONE THING (v1.28, L-497, 6b; Tony, 2026-10-27, "Yes"). No
member in either room is served `drawn_with` another now: the streamer
belt, which was, has its own row again, directly under the corona's,
with its own cross, hover and Go To box, placed by its own nearest edge
(`range.low`, HELMET_CUSP_LOW_RADII, 2 solar radii), with no typed
order. The corona's hover points at the belt's row in one sentence.
This reverses Tony's ruling of 2026-10-04 (one name, one checkbox).
The renderers still honour `drawn_with` if a member serves it -- its
traces join the host's row and yield to the host's cross -- but the
Label words check now fails on a shell row holding more than one info
cross and on a Sun room with no row of the belt's own; its self-test
plants the old join on a copy of the config.

TIES AND PLACES:
- A drawing whose nearest dot lies at or under its body's surface
  begins AT the surface, and sorts after every shell drawn at the
  surface or inside it.
- Two shells that begin at the same distance keep their present order
  (the config's).
- A row that is not a shell -- the centre body, the Moon, the axis, the
  Sun direction, the terminator, a frame shape -- keeps its place in
  the list, and the shells fill the other places in order.
- A shell whose distance cannot be read keeps its place and is named in
  the room's notes. It is never guessed.

THE ORDER IS ONLY AS RIGHT AS THE DRAWING. Tony's rule makes the
drawing the measure, so a drawing that starts where no row says puts
its row in the wrong place, and no order check can see it. The corona
was the case: its dots began at the Sun's surface, under the
chromosphere, so the drawer listed the corona first. The paper its dots
follow puts the base of the corona 3,000 km above the surface (Mann et
al. 2023); the drawing was moved there, and the drawer now lists the
chromosphere first. So the order rests on the gallery run's Drawn ends
check, which holds every drawing's ends to its rows
(provenance-discipline, What a Visitor Reads, principle 4).

THE CHECKS. The gallery run's "Drawer order" row
(`documentation/smoke_drawer_order.js`) builds the Sun and Earth rooms
with the real renderers and holds the page's order to one it works out
from the same rows by its own arithmetic, each stored drawing's nearest
dot read from its file; first it moves the Roche limit's edge and
breaks its own file, and must go red on both. It prints both rooms'
order every run. `tools/headless/walk_drawer_order.js` boots the real
page and compares the drawer's rows, with the same planted fault
(Claude-only, the headless recipe below). The order as first shipped:
gallery `documentation/DRAWER_ORDER_L460_20261021.md`.

### A shell trace carries its key [CRITICAL]
`gallery/feature_renderers.js` stamps `meta.shell_key` on every trace
belonging to a served shell -- the key it sits under in the object's
features, not its display name. `stampShell()` does it at nine sites,
and `stampLink()` carries an existing key across so the two stamps
cannot overwrite each other in either order.

The arrival rule tells three kinds of trace apart by that stamp: a
SERVED SHELL carries a key and is drawn only if `drawn` names it; the
MOON is legend group `moon`; a FRAME ELEMENT carries no key and is
always drawn.

A FRAME ELEMENT THE RENDERERS DRAW (v1.20, L-465) says so: every trace
of it carries `meta.frame_element: true` and no shell key. The Sun's
rotation axis is the first, drawn by `renderRotationAxis` in
`gallery/feature_renderers.js` from the orientation block's served
words (the period and tilt rows with their sentences, `words.axis`,
`words.not_animated`), first in the list so the drawer keeps it after
the body. Earth's guides are built by `gallery/earth_geometry.js` and
never pass through the renderers. `smoke_arrival.js` sets marked
traces aside from the stamp check and FAILS on one that carries a key,
because the arrival rule would then hide a guide that says it is
always drawn. A guide the renderers draw unmarked fails the stamp
check, as before.

THAT IS WHY THIS IS CRITICAL. A shell trace that loses its stamp reads
as a frame element and is DRAWN -- the failure is a room opening on more
than it should, which no compiler and no page error will mention.
`documentation/smoke_arrival.js` therefore checks that EVERY trace the
feature renderers build carries a key, and names by legend group any
that does not. Add a renderer, or a branch inside one, and stamp it.

Before 2026-09-18 a shell was found by the END of its legend group name,
which was a second reading of the label formula the renderers build. Two
readings of one formula is how they come to disagree. There is one way
of matching now; do not add a second.

### Only two tools write the served config [QUALITY]
`data/objects_config.json` is hand-formatted and a person reads its
diffs, so nothing rewrites it wholesale. Two tools edit it IN PLACE,
sharing one scanner (`tools/mirror_constants.py`'s `parse_with_spans`)
so they cannot come to disagree about the file's layout:

- `tools/mirror_constants.py` writes the NUMBERS and, since v1.16,
  their CITATIONS (`source`), pulled from the
  orrery's export. A number changes in `constants_new.py`, never here.
- `tools/store_writer.py` writes the WORDS and the arrival settings, and
  `tools/exhibit_store_editor.py` is the window over it.

WHAT THE WRITER MAY TOUCH IS AN ALLOW LIST BUILT BY READING THE CONFIG,
not a list of exceptions -- 204 paths at gallery `d9d7a48f`: a served
shell's six words, a belt's parallel words, and `drawn` and `moon`; and
since v1.9 a rooms-section room's `drawn` and `highlight` (above). The
first design was a refusal list of six field names, and Claude Fable 5.1
found on 2026-09-18 that it would happily change a room's `slug` to
"earthx" or a shell's `color` to "zzz". A refusal list has to anticipate
every way of being wrong; an allow list only has to know what is right.
Keep it that way.

A SERVED SHELL IS A MEMBER CARRYING A DISPLAY `name`. That is the rule
`tools/check_cache_in_step.py` counts by and the set the renderers
stamp, so the editor's list, that check's count and what a visitor can
tick all mean one thing. A plain walk of the config gives 22 for Earth
where the renderers draw 16; the name rule gives 18 for the Sun and 14
for Earth.

EARTH'S TWO RADIATION BELTS ARE THE EXCEPTION AND ALWAYS WILL BE while
they are served as they are. Their names, descriptions, abouts and links
are PARALLEL LISTS under one group key rather than a member each, so
they have no per-belt key: both carry the feature key
`van_allen_belts`, they tick together as one arrival choice, and they
serve no note and no source. Earth's word list therefore holds 16 rows
against 15 tick boxes. The counts differ ON PURPOSE; a change that makes
them match has probably dropped the belts from one list.

### One check reads the file the browser fetches [CRITICAL]
On 2026-09-17 both rooms broke on the live site -- the Sun showing 9
drawer rows instead of 18 -- while eleven checks passed. Every one of
them built its scene from the config or from a recorded fixture, and
none read the served cache, which is the file the browser fetches
(L-336).

So: for anything a visitor sees, ask WHICH FILE THE BROWSER ACTUALLY
FETCHES, and make one check read that file. Two exist now and both gate
the gallery runner. `tools/check_cache_in_step.py` compares the served
cache against the config it was built from. `gallery_maintenance_run.py
--live` fetches the served page's files and compares them with the
working copy; its list is eleven files as of `d9d7a48f`, and a new file
the page fetches by name is added to `SERVED_FILES` in the same push
that adds it (L-339).

### Logic that needs no browser lives in its own file [QUALITY]
Tony's ruling, 2026-09-18 (L-338). His reason first, because it is his:
to limit the growing size of `interactive.html`. The second reason is
that a check can then reach the logic as a FILE --
`documentation/smoke_arrival.js` used to test the arrival function by
cutting the text between two comment lines out of the page, which is a
check whose subject is a substring and which stops being true the moment
a comment line moves.

It is not a call for a general reorganisation. Logic moves out WHEN A
BUILD ALREADY TOUCHES IT. `gallery/arrival.js` is the first instance:
118 lines left the page, the smoke check now requires the file, and a
visitor saw no difference. `gallery/solar_system_figures.js` is the
second (L-398, 2026-10-01): the Solar System room's distance figures,
checked by `documentation/smoke_solar_system_figures.js`, which breaks
the real file three ways before trusting a pass. A file the page loads
by a script tag joins `SERVED_FILES` in `gallery_maintenance_run.py` in
the same patch.

ONE SCOPE QUESTION IS OPEN and Tony should settle it the first time it
matters: his reason covers bulk that is not logic at all -- a long block
of styling, say -- and the testability reason says nothing about that.
Ask rather than assume.

ONE FLOOR OVER, the same rule applies to a Tkinter tool: everything in
`tools/exhibit_store_editor.py` above the window class runs without Tk,
and its suite exercises it there. Logic that needs no WINDOW must be
reachable without one, or the only way to test it is to open it and
look.

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
on screen; sentences unbroken); a MARKER tap (the page's one text box
opens on the first tap, the same box naming the row opens: left-aligned,
a sentence to a bullet, the feature's colour on its border; a tap on
empty space closes it); the i panel's "Report a problem" link opens the
form with the note started; the HUD note (hover on desktop, tap on
phone); Gallery button then browser back; then landscape; then desktop,
where a mouse resting on a marker opens the same box and moving off
closes it. Report each
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
the pinned label. Plotly's OWN hover box is off in every room since
v1.28 (L-497, 6a; below, One text box): a marker tap opens the page's
text box instead, so this rule reaches only a room that turns Plotly's
box back on.

**One text box, for a tap and for Go To** (v1.28, L-497, 6a; Tony,
2026-10-27: "why not have one hover box for both methods?", then
"Confirmed"). Every room shows a feature's words in one box, the
page's, whether the visitor taps the feature, rests a mouse on it, or
names its row. Plotly's own box is switched off by `hovermode: false`
in `buildSunLayout`'s scene; read from plotly.js 2.35.2, gl3d/scene.js,
that gates only the box (`Fx.loneHover`), so `plotly_click` and the
hover events still fire. A tap is deferred out of the event (L-278) and
opens `sunLabelShow` with the marker's words; in the Sun and Earth
rooms the camera still frames the shell, in the Solar System room it
moves nothing. The box is left-aligned, its border the feature's colour
at 2 px. Its WORDS are decided by `gallery/text_box.js`
(`GalleryTextBox.bullets`), a file of its own by L-338, loaded by a
script tag and so on the live check's file list: a soft break becomes a space, the
first line is the title in bold, a line already opening with a bullet
stays, a line opening "=" carries on the line before it as one bullet,
every other line is cut into its sentences by the i panel's own cut
(`GallerySources.sentences`), one to a bullet, and empty lines go;
nothing else is added or dropped. The check is the gallery run's Hover
budget row (`documentation/smoke_hover_budget.js`): five worked cases
for the file, the page loading it and turning Plotly's box off, and a
copy of the file with its sentence cut taken out, which must fail; it
measures the phone's boxes bulleted. (The file's own header names a
`documentation/smoke_text_box.js`, which does not exist at acbf206b.)

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
Citations, equations and served caveats live in the i panel (L-231);
the hover is the glance. Reworded hovers go to Tony before they ship.
(L-331; the orrery's own hovers follow under orrery-coding-conventions
and L-321.)

**No website hover ends with a pointer to the i panel** (v1.27, L-494;
Tony's option C of 2026-10-26, from four drawn on a design canvas: "Or
remove the sentence everywhere and just add the banner"). Until then the
Sun and Earth rooms' hovers each ended with one pointer line (L-231),
and the Solar System room's did not. Now none does. A visitor's first
visit is greeted instead by a note under the i button, "More information
and the sources for everything you see are here.", with a Got it
button; Got it, or a tap on the i button, puts it away for good in that
browser. The Hover budget check fails on a hover that still ends with
the old sentence. The orrery's own hovers keep their pointer line
(orrery-coding-conventions 1.12).

**A group's class is explained first** (v1.27, L-443; Tony's "Approved"
of 2026-10-26 to documentation/WORDS_L443_glosses_20261026.md). A drawer
group row serves an `about`: what its JPL or IAU class name means, in
plain words. It is the first bullet in the text box and the i panel of
every body in the group, before the body's own words
(`classAbout` in the room's compose). The class name stays JPL's; the
`about` is its gloss, by the rule below.

**Readability, Tony's three asks of 2026-10-24** (v1.23, L-481; built at
gallery 96173b8 and approved on his phone look the same day). In the
Solar System room each line of a body's hover after its name is a
bullet, written `&#8226;`, because Plotly 2.35.2 converts only eight
named entities. Every source line that names JPL Horizons carries its
address, https://ssd.jpl.nasa.gov/horizons/, which the i panel makes a
link (`gallery/source_list.js`). Each room's closing paragraph, "Part
of Paloma's Orrery", is a bulleted list, one sentence to a bullet, and
reads "named for the creator's daughter".

**JPL's terms, kept and explained** (v1.26, L-443; Tony, 2026-10-26:
"I don't want to drop JPL's words, Ellipse, Predicted, hyperbolic,
perihelion, aphelion, etc. We should keep these correct words and
explain them when they should be explained."). Plain words are not
simpler words. A term JPL uses is the correct word and stays;
where a visitor first meets it, the same sentence says what it means:
"perihelion q AU, its closest to the Sun"; "hyperbolic orbits, open
curves rather than ellipses". Explain a term once, where it is met, not
every time it recurs. Replacing JPL's word with a paraphrase is the
failure this rule exists to stop: the visitor loses the word they would
search for.

**The i panel, one sentence to a bullet** (v1.25, L-487; Tony,
2026-10-25: "put bullets on all sentences for readability including the
source paragraph," for all objects). A focused feature's description,
its notes, its detail and each of its citations are lists, a sentence to
a line, every web address a link; a citation's label sits on its first
sentence and the website's note after its last. The words are cut where
the room shows them (`GallerySources.sentences`, `sourceBullets`;
`sunSentenceList`), never where they are stored: a body's description is
the orrery's own. A sentence does not end at a common abbreviation,
initials ("J.", "U.S."), a Roman numeral ("II.") or a journal's
abbreviated name in a citation ("Celest. Mech. Dyn. Astron."), whose
words are capitalised. Checked by the Source list check's part 5, which
cuts every served text and names any piece that starts with a small
letter or loses text, with two breaks; and walked (section 20).

### A feature's info link: NASA if specific, else Wikipedia [QUALITY]
Every drawn feature carries exactly one link, its `info_url` in
`data/objects_config.json` (Earth's two belts carry the parallel list
`info_urls`), and the i panel shows it as "Read more at NASA" or "Read
more at Wikipedia". Tony's rule of 2026-09-02, until v1.10 only on the
ledger (L-265):
- A NASA page where one is SPECIFIC to the feature. A hub page about
  the Sun, the atmosphere or the solar system in general does not
  count.
- Otherwise the feature's English Wikipedia article.
- One exception, by his word: the corona shells take Wikipedia's "Solar
  corona", because NASA's only corona page is Space Place, written for
  children.
- Every link is a URL a search or fetch returned live on the day it was
  chosen. None is recalled.
WHY A LINK AND NOT PROSE (Tony, 2026-08-30): paragraphs written for the
panel would be claims crossing to the website, where nothing scores
them again. A link moves that burden to NASA or Wikipedia, who maintain
the page. The words a room does serve -- `description`, `about`,
`note` -- follow the hover rule above, and any number in them carries
its source.
A redrawn feature keeps its link while the page still describes what is
drawn: the galactic tide kept Wikipedia's "Galactic tide" when it was
redrawn in the galaxy's plane (L-406). Choosing the link is method and
needs no ruling; whether a feature is drawn at all is Tony's.

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
   and fails on a hover that still ends with the old sentence pointing at
   the i panel (since v1.27, L-494; until then it checked that each hover
   carried that pointer). It builds the Earth
   scene, Jupiter and Saturn; at b375cfe1 it does NOT build the Sun
   room, and four Sun hovers missed the move to the panel because of it
   (L-331). A checker passes on what it does not look at: when adding a
   room, add it to this suite before trusting its green.

   **THE HEADLESS RECIPE** (v1.9, L-405; first used for L-363 step 3b).
   The stand-in scene above, made concrete, in `tools/headless/` in the
   gallery repo. Claude-only: Tony never runs it and the maintenance run
   does not. jsdom is not in the gallery; `npm install jsdom@24` in a
   scratch folder and run with `NODE_PATH=<scratch>/node_modules`.
   - `run_room_driver.py <DRIVER> <EPOCH> <out.json>` runs a room's REAL
     driver in plain CPython on the served cache, handing it the Solar
     System room's spacecraft positions files as the page does (v1.24). The driver is ordinary
     Python over `gallery/assembler/`; only Pyodide is missing.
   - `page_harness.js` boots the REAL `interactive.html` in jsdom with
     the real gallery files, that payload, and a stand-in Plotly that
     records restyles and relayouts. It measures the chrome's MECHANISM
     -- rows, ticks, focus, frames, Home -- and nothing a visitor sees.
   - `compare_rooms.js <before> <after> <room> <payload>`: when SHARED
     chrome changes, drive every other room the same way in the old and
     the new copy -- every row's box in turn, the top bar's button
     twice, Home -- and require the two to be identical. "Both rooms are Mode 5 targets"
     (One chrome, many rooms) still holds; this makes the first pass
     cheap and exact.
   - `walk_shell_reset.js <root> <sun|earth> <payload>` (L-482): reads
     what the room opened on from the traces as first plotted, moves
     every tick, the frame, the camera and the text box away from it,
     presses Reset twice, and holds each result to that opening. Run
     against the page from before L-482 it fails 20 checks of 33 in
     each room.
   - A walk per room (`walk_solar_system_drawer.js`) checks each step
     against values worked out in the walk itself, not by the page's own
     helpers, and is run once against a deliberately broken copy to show
     it can fail. It fixes its own opening, so a change to what the room
     opens on does not break it.
   - A CANDIDATE, not yet a file in either repository (v1.27, L-495):
     real pictures before a build. On the night of 2026-10-26 the
     direction arrows' styles and distances were rendered in the
     sandbox's Chromium from the real page, with the pinned Plotly bundle
     and the room's payload handed to the page in place of Pyodide, and
     Tony chose from those renders before anything was built. It shows
     what a visitor would see, which jsdom cannot; it is still not the
     phone. Until it is a file, say in the handoff that it was used and
     how.
   The page's CDN scripts are refused by the harness's loader, which
   serves the stand-in Plotly instead. Say in the handoff what was run
   this way and that the phone has not seen it.
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

- 2026-09-17, L-334: Tony ruled the config is EDITED IN PLACE with the
  mirror's scanner, not dumped through `json.dump`. The manifest had
  proposed accepting a one-time reformat of all 929 lines; the mirror
  already edits in place, and two writers with two layouts would fight.
- 2026-09-18, L-334: not every shell is served with all six words --
  the Sun's core has no `note`. A form that shows a field it can never
  save is a trap, so the writer ADDS a missing word using the mirror's
  own insertion. 23 of the 192 shell-and-field combinations in the real
  config are additions.
- 2026-09-18, L-334: a check that could not fail. The writer's suite
  asserted that refusing `value` produced a message MENTIONING "value"
  -- and "value" is in the path, so emptying the refusal list left the
  suite green. It now asserts the reason. Found by emptying the list on
  purpose, which is the only way that class of hole is ever found.
- 2026-09-18, L-334: the stamp check had a blind spot of its own. It
  built Earth's features without the Sun direction, so the magnetopause
  and the bow shock drew nothing and two of Earth's sixteen shells were
  never examined. A check that examines less than it appears to is the
  same failure as a check that cannot fail.
- 2026-09-19, L-334: two copies of the editor lived in the gallery for
  a day -- `tools/exhibit_store_editor.py` from the patch and a stray
  at the repo root, saved from a file handed over for reading. They
  were byte-identical, which is exactly the trap. Deleted.
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
its loaded copy reads 1.3 before exhibit work. 1.9 was cut in the
session that wrote it, which loaded 1.8; the next session confirms its
loaded copy reads 1.9 before exhibit work. 1.13 was cut in a session
that loaded 1.12; the next session confirms its loaded copy reads 1.13
before exhibit work. 1.14 followed in the same session, after 1.13 was
installed; the next session confirms its loaded copy reads 1.14.
1.16 was cut in a session that loaded 1.15; the next session confirms
its loaded copy reads 1.16 before exhibit work. 1.17 was cut in a
session that loaded 1.16; the next session confirms its loaded copy
reads 1.17 before exhibit work. 1.19 was cut in a session that loaded
1.18; the next session confirms its loaded copy reads 1.19 before
exhibit work. 1.20 was cut in a session that loaded 1.19; the next
session confirms its loaded copy reads 1.20 before exhibit work. 1.21
was cut in a session that loaded 1.20; the next session confirms its
loaded copy reads 1.21 before exhibit work. 1.22 was cut in a session
that loaded 1.21; the next session confirms its loaded copy reads 1.22
before exhibit work. 1.23 was cut in a session that loaded 1.22, and
the session of 2026-10-25 confirmed its loaded copy read 1.23. 1.24 was
cut in that session; the next session confirms its loaded copy reads
1.24 before exhibit work. 1.25 and 1.26 were cut in the sessions of
2026-10-25 and 2026-10-26, each from the repo's copy. 1.27 was cut on
2026-10-27 in a Claude Code session, which reads the skills as files in
the repo, so its loaded copy of 1.26 was the repo's own; a session that
loads the account's copy confirms it reads 1.27 before exhibit work.
1.28 was cut on 2026-10-28 in a Claude Code session, from the repo's
copy of 1.27; a session that loads the account's copy confirms it reads
1.28 before exhibit work.
