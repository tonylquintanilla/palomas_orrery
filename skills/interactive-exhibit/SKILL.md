---
name: interactive-exhibit
description: How an interactive exhibit (a room in interactive.html such as ?exhibit=earth) is designed, built, verified and carded for the Paloma's Orrery gallery. Covers the exhibit switch and boot path, the assembler driver spec, the JS feature handoff, the shared chrome (drawer, nav cluster, frame zoom, i-panel, HUD, consent gate, back link), what is per-body, the served-data provenance contract, what a room opens on (the arrival block) and the shell-key stamp the renderers apply, the drawer order, who may write data/objects_config.json, the Mode 5 phone sequence, and carding an exhibit through Studio. Use when adding or changing an exhibit (Earth, Jupiter, the stars), touching sun* chrome in interactive.html, deciding what an exhibit may render, or editing the served words with store_writer or exhibit_store_editor. Not for propagation math (gallery-assembler), the nightly builder (gallery-cache-builder), or the Studio/converter chain (gallery-pipeline). Do not use for projects other than Paloma's Orrery.
fires_when: a room or exhibit in interactive.html (?exhibit=); its drawer and chrome (nav cluster, frame zoom, i panel, HUD, text box, consent, back link); the served words and numbers a room prints and where they come from (store_writer, exhibit_store_editor, objects_config.json); what a room opens on; testing a room (the gallery run's checks, tools/headless); carding an exhibit in Studio
---

# Interactive Exhibit

Read this file in 3 parts: lines 1-261, 262-519, 520-738.

Skill version: 1.41 | 2026-11-11, with Anthropic's Claude Opus 5.5, at
palomas_orrery @ 87fb472e and gallery @ e21b6746 (the session's bases;
Tony's checkpoint pushes since). v1.41 (L-522, document caps, step 2)
SPLITS THE SKILL: the rules stay here; what interactive.html does now
moved whole, in its own words, into the gallery's
INTERACTIVE_AS_BUILT.md, changed in the commit that changes the page and
held to the code by the gallery run's As-built names row
(tools/check_as_built_names.py). Each of the six long sections leaves
one rule and a pointer, the Provenance rule keeping its rules for new
work; the anatomy table, the text box, the readability asks and the
headless recipe moved with them; the install confirmations went to
documentation/SKILL_HISTORIES.md; fires_when is cut to the phrases that
make the skill fire. Every old line was accounted for by script: found
once in the skill, the reference or the history, or listed with its
reason. SEPARATELY, A CORRECTION (L-523, Tony's word of 2026-11-11):
"Touch has no hover" was wrong for a 3D scene. Plotly sends a finger's
tap 5 px off or more as plotly_hover, so a finger's hover after its tap
is that tap and opens what a click opens (gallery/tap_hover.js, the
gallery run's Tap hover row); and the widened pick is any finger's, in
either orientation (Tony: "Yes, any finger").
Earlier: 1.40 | 2026-11-10, with Anthropic's Claude Opus 5.5, at
palomas_orrery @ b3ce81f8 and gallery @ cea21af1. v1.40 (L-515, one nested
tree, step 2b; Tony's rulings 13 to 20 of 2026-11-09, with L-514 rulings 1
and 4) makes the Solar System room ONE PICTURE AND ONE DRAWER. Each body
something is fetched around folds open, behind an arrow at the start of
its name, to what circles it and, for a centre serving features of its own
(Earth, Jupiter, Saturn), its own shells and guides, together by distance;
a moon is drawn at its planet's place by ADDING the planet's position to
the moon's own JPL elements around it (gallery/assembler/compose_children.py);
ticking a moon ticks its planet; a moon's box is the Moon's pattern, its
distance from its planet, and past its checked span one sentence saying
so. Centre on, on every centre in the tree (the Sun too), moves the view
in the page so the body sits in the middle, on its own served opening,
the whole drawing shifted so the middle is the scene's origin in 64-bit
numbers (gallery/view_centre.js; the 32-bit error measured: Pluto's system
121 km at 35.6 AU); the axis lines cross there and the frame note says so;
Go To on a moon puts its planet at the middle; Home and Reset return to
the Sun's view; the trail is the path down the tree. The Earth room folds
into the root: ?exhibit=earth opens it centred on Earth, its row and driver
OBSOLETE and kept; a fold is drawn, and its stored drawings fetched, the
first time it is needed. The Pluto row reads "Pluto system", the
barycentre the open white square. Jupiter's and Saturn's openings (the
symbol alone) are served arrival blocks, which the store writer can now add
(add_arrival). And L-518's received note on Reset's frame. Read from the
gallery's code with this session's edits before it was written.
Earlier: 1.39 | 2026-11-09, evening, with Anthropic's Claude Opus
5.5, at palomas_orrery @ 09fb6934 and gallery @ 66c9f698. v1.39 (L-519,
Featured's rethink, part 2) adds PLACES, Tony's design of 2026-11-09,
14:53 to 15:00 ("I should be able to put the ED138 scene next to the
ED138 body", "can we put it next to more than one body", "B so I can
decide what goes where") and his go-ahead that evening, with the Sun's
shells and the belt's cloud as places ("Yes we can add them"). A card's
drawer_row is one place or a list; a place may be any row the Solar
System room's drawer lists -- a body, a group, one of the Sun's shells by
its served shell key, or the belt's cloud by its drawing's name -- and a
planet's features will be places the same way once the root draws them
as rows. The card is one record shown in each place, counted once; Back
returns to the fold it was opened from; a scene sits in a Scenes fold
under each row it names, under the Sun when it names none. The gallery
editor's Solar System door lists the room's own drawer, in the website's
order, and a card's form has Places in the drawer, Add place... and
Remove place (tools/drawer_places.py; the gallery run's Drawer places
row). And Tony's phone look of the same afternoon: Find shows a scene
whose name holds a body's name beside the body. Read from the gallery's
code with this session's edits before it was written.
Older entries are in documentation/SKILL_HISTORIES.md, moved there on
2026-10-05 (L-418), 2026-10-10 (L-429), 2026-10-14 (L-431), 2026-10-16
(L-421), 2026-10-17 (L-452), 2026-10-20 (L-456), 2026-10-21 (L-460),
2026-10-22 (L-434, L-443), 2026-10-24 (L-477, L-482), 2026-10-25 (L-443,
twice), 2026-10-26 (L-443), 2026-10-27 (L-443), 2026-10-28 (L-443),
2026-10-29 (L-503), 2026-11-02 (L-507), 2026-11-05 (L-507) and
2026-11-06 (L-513) and 2026-11-07 (L-515, three times) and 2026-11-08
(L-517, L-518) and 2026-11-09 (L-519, twice) and 2026-11-10 (L-515)
and 2026-11-11 (L-522).

## Contents

Generated from this file's headings. skills_index.py --check fails
if this list and the headings disagree (L-418).

- What an exhibit is, and what this skill is not
- Rules
  - Design before code [QUALITY]
  - One chrome, many rooms [QUALITY]
  - Provenance is part of the build [CRITICAL]
  - What a room opens on is SERVED, not coded [QUALITY]
  - One drawer for every centre [QUALITY]
  - One picture: the folds and the view's middle [QUALITY]
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

This skill holds the rules. What the page does now, which function or
file does it and in what order, is the gallery's `INTERACTIVE_AS_BUILT.md`,
at its root beside `interactive.html` (L-522): a session reads the
section for the part it changes, and changes that page in the commit
that changes the page's code. The gallery run's "As-built names" row
holds its code names to the code.

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

The naming carries a debt: most shared pieces are called `sun*` because
the Sun was first. The rule is to rename or parametrize them, never to
copy them under `earth*`. One drawer, one nav cluster, one HUD, one
i-panel; the body is a parameter. Earth, the second room, PARAMETRIZED
through the `EXHIBITS` table and kept the names: a rename touches about
a hundred identifiers in a working room for no change a visitor sees,
and would put the Sun back under Mode 5. It is deferred to the third
room or a free session, with the names to reach for (L-309).
The pieces one by one, and which are shared: the gallery's `INTERACTIVE_AS_BUILT.md`,
The anatomy of an exhibit.

### Provenance is part of the build [CRITICAL]
An exhibit renders only what its served entry carries, and every
number a visitor reads carries its provenance in the served data, not
in the page. A served number, its citation and a body's words are
copies the orrery's tools write; each changes in the orrery, never by
hand in the gallery. Its rules for new work:
- A fact about a feature is served with that feature's words, never
  typed in a renderer; the Typed facts check gates it.
- A served note (`source_note`) holds only a drawing choice; wording
  that bears on a citation goes on the store's row.
- A hover prints a unit it is served and never converts a served
  number to print it.
- A pointer is never aimed at a conversion name; a slot drawn in
  another unit is written from its row's served units, and nothing is
  multiplied in the gallery.
- A computed distance prints by the larger of two errors.
- Scattered dots are the orrery's stored drawing; the website draws
  them as given and places none itself.
- An exhibit is done when Store drift reads MATCH for its pointers, by
  name. NOT IN STORE is fixed by adding the constant to the store,
  never by removing the pointer.
- Where the website and the orrery both draw an object, they agree, or
  the difference is written down.
- A provenance gap found elsewhere is recorded, one ledger row per
  class, not chased.
What the page does, and where: the gallery's `INTERACTIVE_AS_BUILT.md`,
Provenance is part of the build.

### What a room opens on is SERVED, not coded [QUALITY]
What a room opens on is served: a body's `arrival` block in
`data/objects_config.json`, or a room's entry in the config's `"rooms"`
section, never code. With no block nothing is hidden, and there is no
floor under the opening view. The page reads both directly, so a
change to them reaches a visitor on the push alone, while a shell's
words wait for the cache to be rebuilt; say which when telling anyone
what a change will do. Past the served window a room draws the last
day its data covers and says so; it never goes blank, and the
resolver's gate is not moved. A shared link carries the rows ticked
and the minute shown; Reset still puts back the room's own opening.
What the page does, and where: the gallery's `INTERACTIVE_AS_BUILT.md`,
What a room opens on is SERVED, not coded.

### One drawer for every centre [QUALITY]
The rooms are one tree: the Solar System room is its root, and a body
with something served around it is a centre. Every centre's drawer is
built by one builder from one plan, the centre's fixed row first; a
new centre adds a compose row to `EXHIBITS`, never a second drawer.
Which bodies are centres, and which objects are a centre's children,
is read from the config, never typed. Each centre's Reset puts back
what that centre opened on and never touches its fixed row.
What the page does, and where: the gallery's `INTERACTIVE_AS_BUILT.md`,
One drawer for every centre.

### One picture: the folds and the view's middle [QUALITY]
The root is one picture as well as one drawer. What is fetched around
a body folds under that body's row, read from the config's
`center_slug`, never typed. A moon is drawn at its planet's place by
ADDING the planet's position to the moon's own elements, never by the
retired subtraction. Before a centred view is drawn, the whole drawing
is shifted so the middle is the scene's origin, in 64-bit numbers,
because a phone's WebGL holds 32-bit floats. A fold is drawn, and its
stored drawings fetched, the first time it is needed.
What the page does, and where: the gallery's `INTERACTIVE_AS_BUILT.md`,
One picture: the folds and the view's middle.

### The Solar System room's drawer: bodies, not shells [QUALITY]
It is the same drawer as every room's. The decisions rows of bodies
need are made in `gallery/solar_system_drawer.js` and checked there;
the page only touches the DOM and Plotly. Each control acts on one
thing: every group is always listed, folded shut, and there is no See
more, by Tony's ruling that it be permanent. Nothing ticks many bodies
at once, save a spacecraft or a comet and its companions. Selecting
moves nothing; only Go To moves the view. Each group is JPL's own
class for its bodies, one class to a row. The room frames on where
each body is now, with a buffer of 20 percent, and Go To fits the body's whole
orbit.
What the page does, and where: the gallery's `INTERACTIVE_AS_BUILT.md`,
The Solar System room's drawer: bodies, not shells.

### A room's drawer lists its shells where each begins [QUALITY]
Each shell takes its place in the drawer at the distance where its
nearest part begins. The order is READ from the served rows by
`gallery/drawer_order.js`, never typed, so a new shell takes its place
with nothing else to change. A shell whose distance cannot be read
keeps its place and is named in the room's notes; it is never guessed.
The order is only as right as the drawing, so it rests on the Drawn
ends check. Naming a row opens its own feature's words, and one row is
one thing.
What the page does, and where: the gallery's `INTERACTIVE_AS_BUILT.md`,
A room's drawer lists its shells where each begins.

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

The Earth room's Sun line, how it follows the ticks: the gallery's `INTERACTIVE_AS_BUILT.md`,
The Earth room's Sun line.

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

A centre gets its opening (`add_arrival`): the gallery's `INTERACTIVE_AS_BUILT.md`,
A centre gets its opening.

AN OBJECT'S PARENT IS ITS FETCHED CENTRE (v1.33, L-515 step 1; Tony's
ruling 6 of 2026-11-07: "What is the fetched center should rule."). The
writer's allow list holds `/objects/<i>/parent` for every object that
has one, and the one value it accepts there is that object's own
`center_slug`; any other is refused, saying the fetched centre rules
the tree. The root (the Sun, served around itself) keeps its null parent
and is not offered. The gallery run's Tree parents check
(`tools/check_tree_parents.py`, gates) holds the whole config to it:
every parent its center_slug, one root, every parent an object the
config lists, four faults planted first. It found Pluto and Charon,
both served around pluto_barycenter, filed under the Sun and Pluto;
the two were written through the writer. The coverage index copies each
parent, so Cache in step is red until the builder has run (gallery-
cache-builder, A config change is not deployed until the cache is
rebuilt). Nothing the page draws reads `parent`: the drawer reads the
tree from the config's center_slug (`centresOf`, `childrenOf`).

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
per frame. In a 3D scene a finger's TAP can arrive as a hover: Plotly
sends a pick as `plotly_click` only under 5 px from the finger, else as
`plotly_hover`, so a finger's hover that follows its tap is that tap
and opens what a click opens, once per press (L-523). A finger never
rests, so anything that opens on a mouse's hover opens on a tap and
closes on a tap elsewhere. A `hidden` attribute loses to a more
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

One text box, for a tap and for Go To: the gallery's `INTERACTIVE_AS_BUILT.md`,
One text box.

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
text-less dots win over its one info marker. For a finger or a pen, in
either orientation (Tony's ruling of 2026-11-11, "Yes, any finger";
until then a portrait phone only), `sunTapPicking(gd)` makes text-less
traces draw nothing into the pick
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

Readability, Tony's three asks of 2026-10-24: the gallery's `INTERACTIVE_AS_BUILT.md`,
Readability.

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

The i panel, one sentence to a bullet: the gallery's `INTERACTIVE_AS_BUILT.md`,
The i panel, one sentence to a bullet.

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

   **THE HEADLESS RECIPE** (Claude-only, `tools/headless/` in the
   gallery repo): the gallery's `INTERACTIVE_AS_BUILT.md`, The headless recipe.

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
Earlier installs and their confirmations, 1.0 to 1.40:
documentation/SKILL_HISTORIES.md, under interactive-exhibit.
1.41 was cut on 2026-11-11 in the Claude Code session for L-522 step 2,
through the python_work door, from the repo's copy of 1.40; a session
that loads the account's copy confirms it reads 1.41 before exhibit
work.
