<!-- Doc-Kind: hand | The master plan's dated history, moved out of the plan on 2026-10-14: the critical path's session record, August 23 to September 29, 2026, and the plan's lineage. A record; not updated. -->
# MASTER PLAN HISTORY -- Paloma's Orrery Interactive Gallery

Cut from orrery 9248845ca8516dcee3498f07c554e6a24426c23c at
https://github.com/tonylquintanilla/palomas_orrery (branch main), by
patch_L442_1_master_plan_restamp_20261014.py. Written October 14, 2026
with Anthropic's Claude Opus 5.5.

THIS FILE IS A RECORD, NOT A PLAN. Nothing in it says what is next.
It holds the dated history that used to sit inside
`documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md`, moved out word for
word when the plan became strategy only (Tony's rulings of 2026-10-13
and 2026-10-14, L-442). It is no longer updated. What came after is in
the ledger and on the road in `documentation/WHERE_WE_ARE.md`. Like the
plan's two retired companions, it is a dated record, not a versioned
copy of the plan; git holds the plan's earlier versions.

  PART 1  The critical path's session record, from Section 5a: the
          "You are here" table of 2026-08-23 and the dated subsections
          2026-08-25 to 2026-09-29.
  PART 2  The plan's lineage, formerly its Section 10: the sessions it
          drew from and what each version added, through v19
          (2026-08-23).

================================================================
PART 1 -- THE CRITICAL PATH'S SESSION RECORD (from Section 5a)
================================================================

### You are here -- read 2026-08-23 at orrery `38923c1`, gallery `493a0bd`

| | State |
|---|---|
| Phase 0, stack | DONE. Pyodide + Plotly proven, B' resolved, 2.1-3.3 s cold start on iPhone. |
| Phase 1a, vocabulary | COMPLETE. |
| Phase 1b, serving | DONE. 12 objects served. Saturn's 7 rings, Jupiter's 4 rings and radiation belts, Earth's atmosphere and Van Allen belts all present in `feature_configs.json` with full parameters. |
| Artifact 1, Earth | LOCKED (`artifact_1_earth_alone.json`). Proved propagation, the harness and the acceptance loop -- on an ORBIT. Exercised no features, which is how the feature path stayed broken unnoticed. |
| L-207, citation prompt | BUILT August 18. The checker emits `documentation/prompts/citation_review.jsonl` every run -- 53 rows, one per key, carrying what the code cites and what each responder concluded. Closes the last leg of the loop: the citation half of a return now reaches a reader. |
| Segment 1, orrery | IN PROGRESS, and **no longer a gate** (the braid, 2026-08-22). Track 0 has no open rulings. Re-measured at `38923c1` from `WORKSHEET_CHECK.md`: 105 annotations scored, **8 clean**, 47 SEND BACK, 19 CONVERSATION, 31 noted, 22 not scanner-reachable; 292 Tier-1 findings tree-wide. (v18 reported 110/8/48/20/34/24, read on 2026-08-19.) The corpus grew and the clean count tripled because L-198 taught the scanner units it could not read -- coverage, not regression. Dispatch machinery COMPLETE as of August 18; 8 of the 9 August-16 blockers closed, the 9th (ordinal context window) deliberately unexercised by the pilot. **The first dispatch went out and returned on August 18**: 23 rows to three models, 69 answered rows, zero format defects, all three trap rows unsprung. Findings at L-209, L-210, L-211; evidence in `documentation/PILOT_CONVERGENCE_20260819.md`. |
| Segment 2, transport | DESIGNED, not built. |
| Segment 3, assembler draw | NOT STARTED, and **now the next work**. Verified at gallery `493a0bd`: `resolver.py:133` still reduces the feature dict to its keys (`tuple(rec.get("features") or ())`), `models.py:91` still types the field `Tuple[str, ...]` to match, and NOTHING in the gallery repo reads `feature_configs.json` -- only the builder writes it. |
| Segment 4, Artifact 2 | Gated on segment 3 and on segment 1's thirty-number slice. Not on the general audit. |

### 2026-08-25 -- two changes, and a property the plan never named

Appended, not merged. The tables above were read on 2026-08-23 and two
of their rows are now wrong; they are named at the end of this
subsection rather than edited here.

**One. Artifacts reopen, and the ladder has a second axis.** Tony's
ruling, 2026-08-25. The seven golden artifacts are seven PROPAGATION
shapes -- conic, planetocentric, mean elements, spacecraft arc,
barycentric binary. That ladder is complete and unchanged. What the
orrery DRAWS is a different axis entirely: interiors, atmospheres,
magnetospheres, belts, tori, rings, comae, solar shells, Hill spheres.
Nothing in the five segments or the seven artifacts sequences that axis,
and nobody ever decided that some of it would be shown interactive-side
and some not. L-100 carried that as an inherited default from the
Phase-1b cost framing of 2026-07-08; it was never a ruling and is now
closed. Tony: "it is not my intent. The general intent is to redo the
orrery in the assembler. Part by part."

The consequence that arrives first: the resolver requests EVERY feature
key the cache carries for an object, and a golden record hashes
`feature_keys`, `trace_role_counts` and `legend_groups`. So adding a
feature family to a body FAILS every locked artifact containing it.
Under part-by-part that is the normal event, not an edge case, and
re-locking is normal rather than a failure. L-234 carries the work;
Artifact 1's Sun half is DONE, its Earth half is open.

**Two. A property this plan has been folding into provenance, and
should not.** Segment 1 reads "one store for feature constants,
provenance carried as data." Those are two independent properties and
only the second has ever had measurement, tooling or a place in the
order.

  PROVENANCE asks: is this value sourced?
  SINGULARITY asks: is there ONE of it?

A value can hold either without the other, and on 2026-08-25 one clean
example of each turned up:

`KM_PER_AU` is cited about as well as anything in the tree -- IAU 2012
Resolution B2, exact definition, two independent cross-checks recorded.
It also existed as thirteen literal copies across seven live modules,
one of them under a different name (`AU_KM`), plus three more names
aliasing the import. Perfect provenance, five names, sixteen sites.

S4714's semi-major axis is the inverse. Three stores held it: the
catalog said 520.0 and two consumer modules overwrote it to 800.0 at
import time, so which value a render used depended on import order. A
live path saw neither override, so the same star was drawn two ways --
and each view's prose was correct for its own value, one reporting 8.2%
of light speed at periapsis and the other 10%. The number drawn was
unsourced; the citation on file described the number that was not drawn.

**Why the audit could not see either.** The scanner scores literal
assignments. A second copy of a correctly-cited value is not a finding,
and a runtime dict mutation is not an assignment at all. So a Tier-1
count says nothing about how many places a value lives. Neither does the
drift checker: `constants_change_report.py` watches ONE file, so "No
changes to constants_new.py" was true and silent while a value moved
from 520 to 800 in a store it does not read. L-245 widens that check's
window in time; this widens it in space.

**Where this sits in the order: NOT on the path to Artifact 2.** Nothing
in it touches Saturn's rings or Jupiter's belts. It is recorded here so
it is visible, and it is explicitly not a gate -- the same reasoning the
braid ruling applied to the general audit on 2026-08-22. Handles: L-243
(the AU factor, closed 2026-08-25), L-244 (the class sweep, a Fable
candidate), L-246 (S4714, structural half closed), and the migration of
eight cited scalars out of `sgr_a_star_data.py` into `constants_new.py`.
The S-star catalog itself does NOT migrate as it stands -- it mixes
orbital elements with hex colours and prose, and needs L-240's
measured-versus-declared split first.

**Two rows above are stale and are deliberately left standing.**
"Segment 3, assembler draw: NOT STARTED" -- the Sun is now complete in
the assembler, 19 shells, Mode 5 passed on 2026-08-24 and 2026-08-25.
"Artifact 1, Earth: LOCKED" -- reopened by the ruling above, and its
golden record is stale in four fields (L-237). Re-measuring those rows
belongs to a pass that reads the repo, not to this append; a table
re-stated from memory is how the 105 / 107 / 110 drift happened in this
document.

### 2026-08-29 -- the Sun ships, and four things shipping it found

Measured at orrery `688561ef` and gallery `ac9a5c7b`, both confirmed
against the live remote. The row above is now stale in a second
direction and this subsection re-measures it rather than editing the
table from memory.

**Segment 3 is DONE for the Sun, and segment 5 has begun.** The Sun
exhibit is live at `interactive.html?exhibit=sun`, unlinked from the
landing page, carrying inline credit. It runs the shared assembler
package in Pyodide against the served cache and hands the feature
report to `feature_renderers.js` -- architecture B', Section 3a's
Python-assembles / JavaScript-draws split, working end to end in a
visitor's browser for the first time. Mode 5 accepted.

It is a SECOND exhibit on the page that has been public since July,
reached by the `?exhibit=` parameter Section 2a designed for exactly
this. The Solar System Explorer is untouched and still the default.

**The shell count is 18, not 19.** Measured through the real renderer
at `ac9a5c7b`: 18 drawable shells, 18 named traces plus 18
info-marker companions. The 2026-08-25 append says 19. Corrected
here rather than restated.

**Four defects surfaced, three of which nothing could have caught
earlier.** GitHub Pages served no `.py` file in the repo at all --
Jekyll runs by default and there was no `.nojekyll`, so the whole
assembler directory 404'd while working perfectly over a local
server. Fixed at gallery `833daa9a`. The scene axes were pinned, so
the legend could not move the frame and a visitor toggling the
heliopause saw nothing happen. And `feature_renderers.js` sent a
shell's GEOMETRY to the legend without its info marker, so nine
markers were being drawn between 94 AU and 150,000 AU, hoverable,
with nothing around them -- invisible only because the pinned axes
fell inside them. That one predates the Sun exhibit and was surfaced
by fixing the second: the protocol's own lesson about an invisible
thing surfacing its neighbours.

**The fourth is SEGMENT 2, and it stops being theoretical.** The
session corrected `RADIATIVE_ZONE_AU` in the orrery, pushed, and
re-ran the cache builder -- and the site went on serving 0.7 for
hours. The builder passes feature constants THROUGH from
`data/objects_config.json`, a hand copy in the gallery repo. It has
never read `constants_new.py`. Fetch-and-import was RATIFIED
2026-08-08 (Section 7, decision 12) and never built, so the two
repos have no mechanism connecting them at all.

The value reached the site by a hand patch to `objects_config.json`.
That is not a workaround, it is the current architecture.

**So segment 2 is repositioned.** It is described in this section as
protection against a correct orrery drifting from its copy LATER.
That is too weak. Under the export gate (provenance-discipline 2.9)
the boundary the gate names is a human copy with no check on it, so
the transport is the gate's MISSING ENFORCEMENT POINT. The
2026-08-28 handoff predicted this in the abstract; it failed in its
first real test the following day. It does not gate the next
exhibit, and it should be built before the ladder gets long enough
that hand-copying many bodies becomes routine.

**Handles owed, not minted here.** L-258 (the significant-figures
rule and its two constants) has no ledger entry; the Sun exhibit has
no handle at all; and `provenance-discipline` went 2.9 -> 2.10 in a
session that cannot verify its own reinstall. The ledger carries
status authority (L-221), so those are ledger edits and this section
records them rather than asserting around them.

### 2026-09-03 -- the Sun GUI is complete on desktop, the phone pass
names three defects, and the order to Jupiter

Measured at orrery `def557e6` and gallery `98cc99bd`, both confirmed
against the live remotes. Appended, not merged, in the shape of the
August 25 and 29 subsections above.

**What shipped between August 29 and today.** The Sun room's GUI
(L-267) in three stages: A, the drawer replacing the legend and the
portrait defect fixed (gallery `2ed12564`); B, the mockup ported --
row split with a GO, focus label on the drawer handle, cross-marker
navigation (`e0edd16c`), and the click-hang it exposed fixed by
deferring the focus call one tick (`6fd6baaf`, recorded portably as
L-278 and as a field note in gallery-assembler 1.2); C, the i panel
following the focus with the shell's swatch, name and one link out
(`0edf4bf4`), the i button wired for the Sun path at all -- it had
been decoration since Stage A (`42a906f6`) -- and panel and drawer
sharing the height, 40/60 (`6cfaf318`, `98cc99bd`). The 22 curated
links (L-265) are served with zero placeholders. Mode 5 passed on
desktop for every trial, including the hover-seize from the
2026-08-30 study, which did not reproduce on the live page. The wing
is designed and recorded in L-282 (the lobby: three subject doors,
Solar System, Earth System, Stars, each blending static cards with
live scenes), L-286 (rooms in four levels, breadcrumb), L-287 (the
editor and room tree), L-281 (guest book), L-283 (theme) and L-284
(retire the social export). L-280 (door, hall, two rooms) was retired
2026-09-04: there is no separate interactive wing; live scenes are
cards inside their subject's rooms. Nothing of it is built.

**The phone pass ran today, and it is not a pass.** Tony, on a phone,
2026-09-03, Mode 5. Three findings, in his order:

- The Plotly modebar is missing, so there is no way to reset the
  scene. This is the gallery's own rule, not a Sun defect:
  `interactive.html` hides the modebar below 768 px (CSS at line 548
  and `displayModeBar: window.innerWidth > 768` at lines 1070 and
  1497, measured at `98cc99bd`). On the desktop the modebar was the
  reset; on the phone nothing replaced it.
- The two-finger zoom gesture does not work in the 3D scene.
- Landscape works.

The static gallery already solved both. `index.html` at the same SHA
carries `zoomIn`, `zoomOut`, `panReset` and `resetStandalone` buttons
(lines 1572 to 1625) with `touchstart` handlers, and Gallery Studio
draws the same `+` / `-` pair (`tools/gallery_studio.py` lines 2447
and 2473). Tony's ruling: land on ONE control set that works for both
the static gallery and the interactive wing. The Sun room is the
first room, so whatever it gets, the hall's chrome inherits; that is
why this is step 1 and not a finishing item.

These findings are Mode 5 results and belong in the ledger, which
carries status authority (L-221). L-260 still reads "mobile is
untested" and L-267 still reads "the phone pass is what remains"; both
are now wrong in the same direction and are owed an amendment. This
section records that and does not assert around it.

**The order, confirmed by Tony 2026-09-03.** Braided so each step
feeds the next; the general audit and the constants work continue
beside it and gate nothing here.

1. **Sun room: phone controls.** Reset and zoom on a phone, one
   control set shared with the static gallery. Then the phone pass
   again. This is what stands between the first room and complete.
2. **The lobby, its rooms and the editor (L-282, L-286, L-287),
   designed 2026-09-04, portrait first.** In build order: the editor
   and room tree first (L-287), so cards can be placed and Tony can
   remodel; then the lobby screen with three doors, What's New and the
   guest book (L-282); then the four-level drill-down and the
   short-name breadcrumb (L-286). Until this exists the Sun room is a
   URL nobody can find. The chrome from step 1 is what the rooms copy.
   [Until v23 this step read "The hall (L-280)": a door card, a hall
   listing interactive rooms, two rooms. Retired 2026-09-04 -- doors
   are by subject and blend static with live, so a hall had no job
   left; its What's New and guest book moved into the lobby.]
3. **Earth into the assembler.** The next body. Three items travel
   together: Earth's shells and belts drawn through
   `feature_renderers.js`, which also exercises the belt path Jupiter
   will need; the Earth slice of L-268's collapsed-feature
   remediation; and L-237, Artifact 1's stale golden record, which
   reopens anyway the moment Earth grows features.
4. **Segment 2, the transport, built alongside Earth.** Earth would
   be the second body whose constants reach the gallery by hand-editing
   `objects_config.json`. The August 29 subsection said the transport
   should land before hand-copying becomes routine. Two bodies is
   where it becomes routine.
5. **Jupiter and Saturn.** Segment 1 sliced to the thirty measured
   numbers, then segment 4 locks Artifact 2, and the premade Solar
   System Explorer room starts being replaced by interactive planets
   as L-286 rules (carried there from L-280).

Off the path and clustered: L-284 (retire the social export) with
L-254 (dead sphere-shell builders), both orrery-side, worked the next
time the orrery side is open for other reasons. Tony's ruling,
2026-09-03.

**One thing this plan never carried and now does.** The body order for
the assembler -- Sun, Earth, Jupiter and Saturn -- had lived in
conversation and in memory. The five segments sequence propagation
shapes and provenance slices; the August 25 subsection named the
drawn-feature axis and said nothing sequences it. The list above is
the first place the order is written down. Bodies after Saturn are
not ordered here; that is a ruling for when Saturn is on screen.

**Rows in the 2026-08-23 table that are now stale, by name.**
"Segment 3, assembler draw: NOT STARTED" -- done for the Sun, and
its GUI is complete on desktop. "Artifact 1, Earth: LOCKED" --
reopened, and now step 3. "Segment 4, Artifact 2: gated on segment
3" -- segment 3 is no longer the gate; steps 1 to 4 above are. Left
standing for the same reason the August 25 append gave: the table is
re-stated only by a pass that reads the repo.

### 2026-09-05 -- L-287 is live, and the lobby, the sweep and the
twelve-edge labels are built and waiting for the phone

Measured at orrery `9652a43d` and gallery `503fa387`, both confirmed
against the live remotes at session start; neither moved during the
session, because Tony was away from his machine. Appended, not merged.

**What shipped on 2026-09-04/05 (the machine session).** Step 2's
first item, the editor and room tree (L-287), is DONE and live at
gallery `503fa387`: `gallery_config.json` and `gallery_metadata.json`
are schema version 2 (a room tree; one card per exhibit with two file
slots, shape, live, featured, sources); 105 cards, none in storage;
`tools/gallery_editor.py` rewritten; `index.html` carries a reader
SHIM that maps rooms onto the old category menu so the schema could
ship before the lobby. Two corrections to the design record travelled
with it: 38 landscape/portrait pairs, not 33; seven consumers of the
metadata, not five (`gallery_cleanup.py`, which deletes orphans, and
`gallery_json_fixer.py`).

**What was built on 2026-09-05 (the away session), none of it run.**
Four gallery patches and two orrery patches wait at the repo roots;
every one guards on the bytes it was built against and refuses
otherwise. The record of each is in the ledger; the plan's interest
is what they do to the order.

- **Step 2's second item, the lobby (L-282), is built.** Rulings by
  phone: the section is FEATURED, from the existing flag, no dated
  feed; live cards read INTERACTIVE; empty rooms read UNDER
  CONSTRUCTION; doors above Featured. A door tap opens the existing
  menu at that door until step 2's third item, the rooms and
  breadcrumb (L-286), replaces it. So the hamburger and the shim
  survive one more step, and L-286 retires both.
- **The room-shape rule (L-286) is built for 2D plots ahead of the
  rooms it was written for.** The lobby's counts surfaced that the
  shim still filtered cards by mode, hiding every landscape-only card
  on a phone, against L-287's own rule. Tony: "no squeezed
  landscape" -- landscape on the phone stays; portrait sweeps. The
  filter is lifted and the sweep built in one patch, because showing
  the cards without the sweep would have shown them compressed.
- **L-289 (the Sun's axis labels on the phone) is designed and
  built.** Tony's design, replacing the top-view/back-view idea:
  labels on all twelve edges of the box, tick values and axis names,
  thinned by count, no label at a vertex, the name on an unlabeled
  line, no dimming. The page owns the ticks. This is chrome the
  future rooms inherit, which is why it belongs beside step 1's nav
  cluster rather than in a finishing list.

**What this does to the order.** Nothing moves. Step 2 is two of
three items built and one designed-not-started (L-286's drill-down and
breadcrumb). Step 3, Earth into the assembler, is unchanged and still
next after step 2. The guest book (L-281) and the theme (L-283) stay
where the September 3 list left them.

**The gate on all of it is one phone pass.** The lobby, the sweep and
the edge labels were each exercised in a headless browser here --
lobby and sweep on the real page with Plotly served locally, the edge
labels in a stand-in scene because the Sun page's Pyodide cannot load
in the sandbox -- with no script errors. What a headless run cannot
say is how any of it reads in a hand. The sweep intercepts the plot's
own drag layer, which L-286 already said needs a real phone before the
rule is trusted. Until Tony's pass, every one of these is a claim.

**One measurement worth keeping.** The mode filter hid 49 of 105
exhibits from phone visitors: Solar System showed 31 of 39, Earth
System 22 of 57, Stars 3 of 9. It had been in force since the
Desktop/Mobile toggle was added and nobody had counted, because the
menu counted only what it showed. The lobby counts what exists, and
that is how it surfaced.

### 2026-09-06 -- the phone passed the lobby and the sweep, failed the
edge labels, and the labels were rebuilt as chrome

Measured at orrery `a57e86b8` and gallery `fc8d9fb3`, both confirmed
against the live remotes. Two Mode 5 rounds since the 2026-09-05
subsection: the phone on 2026-09-05, the desktop and the phone on
2026-09-06. Appended, not merged.

**What passed.** The lobby (L-282): doors, a door tap, a Featured card,
Home. The sweep (L-286): a landscape-only 2D card in portrait sweeps
and swipes; the drag handoff this plan and the ledger both said needed
a real thumb has had one. The back link: fixed the same day (the
Sun's "Gallery" button had been a plain link, so Safari's own back
walked into the Sun) and confirmed on both devices.

**What failed, and why the failure is the useful part.** The
twelve-edge axis labels (L-289) were drawn as text INSIDE the scene.
On the phone they shrank with distance, vanished on zoom-out, were
sliced at the box boundary, and floated on nothing for edges beside
the camera. Tony: "this may be worse than the plotly labels." He was
right, and the lesson is not about labels. Anything drawn in the scene
behaves as scenery; anything that must stay legible at every zoom and
angle belongs in the page. The rebuild followed that line: one chip
naming the uniform grid spacing, a corner triad that turns with the
camera, the First Point of Aries at the x tip with a note that the
frame is the J2000 ecliptic (verified in the renderer before it was
written, sourced to NAIF). A second pass found four defects in the
rebuild -- the note would not close, the coloured grid read as a
second key, arrival spacing disagreed with the chip, the triad did not
follow a touch rotation -- and a fix for all four is delivered and
waiting for the phone.

**What this does to the order.** Nothing moves. Step 2 is still two of
three items built (editor, lobby) and one designed-not-started
(L-286's rooms page, drill-down and breadcrumb, which also retires the
hamburger and the shim). L-289 is Sun-room chrome and rides beside
step 1. Step 3, Earth into the assembler, is next after step 2 and
opens as a DESIGN conversation in the next session -- what Earth's
room shows on arrival, what it inherits from the Sun (the drawer, the
frame zoom, the HUD are all reusable now), what is Earth-specific, and
what the assembler must serve that it does not serve today.

**Two rules this round confirmed, in the plan's own words.** The tree
is the order: the lobby's menu and Featured grid now follow the room
tree in `gallery_config.json`, so the editor's order IS the visitor's
order and no new field was added. And the phone is the gate: three of
the five things built since 2026-09-05 changed after Tony's eyes saw
them, and none of the changes could have come from the headless
renders that preceded them.

**Recorded, not planned.** Tony is checking the sweep's exceptions
systematically with `tools/sweep_report.py`, which names every card by
class. The old-card cleanup is his, in the editor, separate from any
step here. L-290 (relay anchors must name the protocol and skills) is
a process item from a parallel Sonnet session and waits on his ruling.

### 2026-09-06 (evening) -- the Sun's axis question closes, and Earth
is designed

Measured at orrery `50cbd2df` and gallery `90615b9f`, both confirmed
against the live remotes. Appended, not merged.

**The Sun's chrome is finished.** L-289 is CLOSED on Tony's Mode 5.
Patch 4 passed all five trials on the phone in both orientations, and
then the triad turned out to read as 90 degrees off the grid while
being provably correct -- an orthographic triad beside a perspective
box, with every axis title empty and the grid uniform white, so nothing
in the render could corroborate it. Two more rounds fixed that: box
edges coloured per axis (right on desktop, off the sides of a portrait
frame on the phone), then three coloured lines through the origin.
Tony: "This works. It's a bit unusual but it is correct and one can't
make a mistake!" That is three Mode 5 rounds on one piece of chrome,
and none of the three failures was visible headless.

**Earth is designed, zero code.** The full record is
`documentation/PREDESIGN_earth_exhibit_20260906.md` in the gallery
repo; L-291 is the handle. The exhibit is Earth's shells plus the
Moon, arriving at LOW EARTH ORBIT -- Tony's framing was "what we see
from the ISS" -- with eight shells lit and everything from the Van
Allen belts outward waiting in the drawer. Four things were added
during the round: the Sun's direction (not optional, since the
magnetosphere is compressed sunward and rotated to face it), the axis
and equator, Earth-Moon Lagrange points, and an exosphere shell that
does not exist yet.

**Two rulings from that round worth carrying into every later exhibit.**
A Lagrange point belongs to the FRAME THAT DEFINES IT -- so Earth-Moon
here and Sun-Earth held for a heliocentric view, one rule with no
case-by-case exceptions. And sunlight is GEOMETRY, not a lighting
model: the terminator is a great circle perpendicular to the Sun
direction, computed rather than shaded, because a shading model on
Earth alone would break one-chrome-many-rooms and would be a rendering
effect with nothing to source.

**What the round found that nobody was looking for.** The Moon's
osculating elements carry a measured trust window of 3.37 days against
Earth's 365, and NOTHING IN THE SERVING PATH ENFORCES IT -- the
resolver gates on the cache's global served_window, which is built only
from heliocentric objects, and the Moon is parent-relative. The Sun
exhibit never met this because it draws no orbits at all. Earth is the
first exhibit to exercise the assembler's propagation path, and that is
a property of step 3 the plan had not named.

**A backlog item became an exhibit.** Tony's question about why one
year rather than one lunar month led to the lunar standstill: the
Moon's orbit is nearly circular, so what separates two drawn ellipses
is the drift of the tilt direction, which comes full circle in 18.6
years. Four dated orbits fanning apart is a room of its own (L-293),
and the orrery already does the same trick for comets at perihelion.

**What this does to the order.** Nothing moves. Step 3, Earth into the
assembler, has had its design conversation and is now blocked on ONE
Tony-action: installing the `interactive-exhibit` skill to the account,
since a session can read the repo copy but cannot load it. Step 2's
remaining item (L-286's rooms page) is unchanged.

### 2026-09-07/08 -- Earth's data lands on both sides, and the served
card found four defects in the pipeline that serves it

Measured at orrery `af4c604e` and gallery `700b426d`, both confirmed
against the live remotes at close. Appended, not merged.

**The gate fired.** The session loaded `ledger-and-session-records`
1.10 and `interactive-exhibit` 1.0, matching the manifest -- the check
the 2026-09-06 session could not perform from inside itself. L-290
and L-296 closed on it.

**Step 2, orrery side, in four patches, each Mode-5'd.** Twenty-one
constants entered `constants_new.py` with fetched sources (IERS 2010
TN36; IADC-02-01 Rev. 3; Baker et al. 2018; JGR 2025; Shue et al.
1998; Lugaz et al. 2016; Baliukin et al. 2019). Every Earth shell
literal that now had a store name was migrated onto it -- Tony's
ruling: one store, one source of truth, the orrery side not deferred.
Two values moved when sourced: the bow shock 15 -> 12.5 R_E (a
citation saying 11-14 cannot sit under a 15) and LEO's edges by 7 km
(the old figures were mean-radius sums). The atmosphere shells stopped
drawing at visibility fractions and drew their sourced boundaries,
as the chromosphere already did (L-295 closed). Every live Earth hover
now ends in a Source line scoped to what it sources -- Tony's ruling,
and the rule waits for orrery-coding-conventions 1.8 (L-299).

**Step 2, gallery side, in one patch of seven files.** Earth's served
entry in the measured shape, nine groups, 24 pointers MATCH by name on
the live run. The six files beside the config were each found by a
check: the drift checker did not know Earth radii; the renderers did
not know `R_earth`, `km` or `planet_radius`; the builder's validator
threw on measured belts; two test files pinned the old shape. The
Earth groups draw in the Explorer room today, sources in the hover,
which answers Tony's question of whether the assembler carries the
sourcing the orrery now shows: it does, when the served row is
measured and the renderer reads it.

**Lagrange points sized and deferred (L-297).** Serving them from
Horizons is a fourth serving shape in the builder plus an assembler
branch plus one nightly -- a session of its own. Computing them from
the Moon's marker was rejected: an approximation of a value that can
be fetched. Tony ruled defer now, Horizons later.

**Four defects the served card surfaced, all Tony's finds, all fixed
the same day.** The converter wrote to `tools/gallery/` when run from
`tools/` (L-288). Portrait's routed hover drew an opaque grey box
because Plotly replaces a zero-opacity label background with grey
(L-288). Served 3D cards did not rotate until a modebar button was
pressed, because the sweep relayouted `dragmode` after every render
(L-286). The landscape+portrait pairing Tony's workflow relies on
had been lost at L-287 and three pairs were stranded as one-file
cards (L-301). And the info card closed itself on the tap that
opened it (L-302). Each Plotly behaviour was read out of the shipped
bundle; the field notes wait for gallery-assembler 1.3 (L-304).

**One design question raised, not ruled (L-303).** Tony prefers a
card per orientation; the current model is one card with two slots,
and the viewer no longer filters by device, so the two halves have to
be ruled together.

**What this does to the order.** Nothing moves. Step 3 -- the Earth
branch in `interactive.html`, the GEO ring and magnetosphere
renderers, the terminator, the Moon's trust-window arc, the chrome by
parameter -- is next and is unblocked. Handoff:
`documentation/HANDOFF_earth_step3_20260908.md` in the orrery repo
[this read "gallery repo" until v29; the file was only ever in the
orrery].

### 2026-09-08 evening -- a design round splits step 3, and the
magnetosphere turns out not to be sourced

Measured at orrery `20750034` and gallery `700b426d`, both confirmed
against the live remotes. Zero code. Appended, not merged.

**The gate fired and discharged v3.54's carried obligation.** The
session loaded `ledger-and-session-records` 1.10 against a manifest
expecting 1.10 -- the check the 2026-09-06 session could not perform
from inside itself.

**One hover requirement unwound two constants.** The L-291 handoff
asked only that the magnetosphere hover say the tail is drawn to 100
radii against a real one past 1,000. Reading the code to write it
found that the orrery's magnetopause is a half ellipsoid with typed
axes, its bow shock a conic with an eccentricity typed at the call
site and a sweep cap the code itself labels a Mode-5 knob, and its
11 degree tilt unsupported by the models that would replace it.
Farris & Russell, cited in the store as the bow shock's model form,
is a standoff-distance relation and not a shape at all.

**Tony's ruling: approximations are not promoted** (L-306). The
seven drawn numbers stay where they are until a sourced model
replaces the shape they belong to.

**The model taken is Jelinek et al. 2012** -- one functional form
for both boundaries -- with Lin et al. 2010 recorded as the better
physics deferred on portability, since the same mathematics has to
live in Python and JavaScript and stay identical, and ten
coefficients cannot be checked by eye. Tony's framing decided it:
a layperson's learning tool, not a research tool. The tail is drawn
with its extent sourced, the geocorona pattern, because Jelinek is a
dayside fit and its paraboloid extrapolated downtail is the error
class just ruled out.

**Step 3 splits rather than waits** (L-291). Eleven sourced features
proceed; the magnetosphere is absent and named. Orrery and assembler
move together on L-305 -- the braid -- because the standoff constant
is quoted to the visitor in two hover strings today.

**The card model is ruled** (L-303): one card per orientation, and
the viewer rule is one line, not the old device model -- on a phone,
hide a landscape card that has a portrait sibling. The merge was
L-287's, not Tony's. The editor work the alternative required
evaporates with the ruling. The surviving static population is the
16:9 2D Earth science and star cards, which is also why export-age
reporting is deferred on priority and not because the assembler
absorbs it (L-307).

**What this does to the order.** Nothing moves. Step 3 is next and
is unblocked on six of its seven items. Handoff:
`documentation/HANDOFF_earth_step3_20260908.md` in the orrery repo
["gallery repo" until v29], superseded in part by this round.

### 2026-09-09/10 -- Earth ships, and its card finds a gap in the handoff

Measured at orrery `1ee1cc61` and gallery `57fd93c6`, both confirmed
against the live remotes. Appended, not merged.

**Step 3 built, then three Mode 5 rounds** (L-291). `?exhibit=earth`
became the second row of an `EXHIBITS` table the shared chrome reads,
and `gallery/earth_geometry.js` composes the room: the served shells,
the axis and equator from the served pole, the Sun line and terminator
as geometry rather than lighting, the GEO ring, and the Moon on its
trusted arc. Running the assembler corrected the step-3 handoff three
times: Earth is the CENTER and not an object, the Moon's trust window
is read from the record, and a belt beyond the frame goes to the
drawer. Tony read the Moon's woven arc as points too far apart in
time. That was L-168 -- solar mean motion applied to a planetocentric
orbit, caught in July, designed, and left open until the first moon
rendered. Fixed at source.

**The card was made twice.** The first Earth card was a copy of the
static Earth-and-Moon portrait with a live URL added, because the
Studio button was not found. The copy kept the portrait's pairing
tag, so the lobby's Featured rule hid it on the desktop while the
phone showed it. The handoff written that night said the card step
had not started; its session never read the metadata. A review the
next morning did, replayed the viewer's rule against it, and Tony
rebuilt the card in Studio. Mode 5 on the lobby, desktop and phone,
closed L-291 and L-303 (one card per orientation).

**Loose ends became a rule.** Three unfinished tasks were riding
inside items that had closed or were about to, one of them behind a
pointer to an item that never mentioned it. They went to L-311 (the
rotation period), L-312 (the editor's copy defect and two titles),
L-237 (a planetocentric test) and L-288 (the Studio button and the
editor's unchecked save). ledger-and-session-records 1.11 makes
re-homing part of closing; interactive-exhibit 1.1 corrects the
places that still described one branch per room. Protocol v3.56.

**What this does to the order.** Step 3 of the 2026-09-03 order,
Earth into the assembler, bundled three items. The room is done.
L-237, Artifact 1's golden record, is still open and now also carries
the planetocentric test. L-268 does not record whether Earth's slice
was discharged by step 2's rebuild of the served entry; that is for
L-268's next session to settle. Step 4, the transport, was not built
alongside Earth and still stands before step 5, Jupiter and Saturn.
Tony's next track is the L-310 camera-step design round -- shared
chrome, zero code -- taken beside the order, not as a step in it.
Handoff: `documentation/HANDOFF_earth_close_20260910.md` in the
orrery repo.

### 2026-09-10 (evening) -- the rooms' chrome after the phone, and the orrery's hover text joins the braid

Measured at orrery `b2c77350` and gallery `9c056d1a`, both confirmed
against the live remotes. Appended, not merged.

**L-305's paper read landed, corrected.** The Jelinek 2012 read and
Tony's split -- Shue (1998) for the magnetopause, Jelinek for the bow
shock -- are in the ledger. The session's design record could not be
pasted as written: its new item took a handle L-310 had already used,
and its replacement Gap dropped two open lines. The solar-wind item
became L-314, and why three chained patches refused became L-315.
L-305's build is unchanged in the order: read Shue's flaring
coefficients, then the port.

**The camera-step track closed and grew four items** (L-310, L-316,
L-317, L-318, L-320). The arrows passed Mode 5. The phone look that
closed them moved the cross to the top right with the title kept,
carried the orrery's two-standards marker outline into the gallery,
started every marker five degrees off the pole, and added a label that
opens when a shell is named in the drawer, pinned to its marker with an
arrow. Twice the fix already existed in the orrery and the interactive
had never received it (L-317, L-320); the first build of L-317 went the
wrong way until Tony said so.

**The orrery's hover text joins the braid** (L-321). The gallery's hover
text is built from served, provenance-checked rows; the orrery's is
fuller hand-written prose. Tony ruled against carrying the prose over:
accuracy over fullness, the orrery must be as correct as the
interactive, and the slice starts with Earth. Discovery at orrery
`b2c77350`: 36 display strings, none Tier 1, all cited but not
independently cross-checked.

**What this does to the order.** The five segments do not move. The
braid gains an orrery slice for Earth's hover text, worked beside the
delivery work and not in front of it: discovery is done, a design round
for the cross-check is next. L-305's build and L-318's last question (a
marker tap's own hover box still drops its pointer mid-screen) are the
Earth room's open data and chrome items; L-316's desktop look and
L-319's call are Tony's. Handoff:
`documentation/HANDOFF_L316_L321_20260910.md` in the orrery repo.

### 2026-09-11 -- units become a field, and the orrery becomes a producer

**A narrow question opened a wide one** (L-305 Gap item 3 -> L-322). The
gallery's store-drift check reads each constant's unit from a SUFFIX on
its name and knows four. L-305 is about to serve fifteen values of which
twelve are not lengths, so twelve would report NO UNIT -- printed,
counted as unexaminable, and NOT a failure, because only DRIFT fails.
The run would have gone green with twelve of fifteen unchecked.

**Tony's ruling: a unit is a field, not a literal in a name.** In
engineering he has always used units, not literals. `# Unit:` becomes a
fifteenth comment key in the store; the suffix reader is retired rather
than kept as a cross-check, because two declarations of one fact can
disagree. And the deeper move: the orrery EXPORTS its values, the
gallery stops parsing orrery source, and the join with gallery
presentation happens in the ASSEMBLER rather than mixed into
`data/objects_config.json`. `constants_new.py` becomes physical values
only, so every line in it has a unit and a blank is an error.

**What made the export architecture reachable rather than aspirational:**
nothing generates `objects_config.json` today -- it is hand-maintained,
and the gallery's per-value check is the net under that hand copy.
`orrery_maintenance_run.py` already runs five GENERATORS and fourteen
CHECKERS, so the export is a sixth generator on rails that exist, and
`doc_index.py`'s own comment already carries Tony's ruling that a
generator beats a checker because it fixes the producer.

**One review round with Claude Fable 5.1.** All nine rulings held. It
caught a two-hop error -- the export is the gallery serving what the
orrery published AND the orrery publishing what the store holds, and the
record had collapsed them -- and it contributed the whole-store export
and the one-walk migration. Two of its own numbers were wrong and are
corrected in the record.

**What this does to the order.** Nothing moves. L-322 is NOT a gate on
L-305, whose renderer proceeds under today's architecture; the bounded
cost is twelve values reporting NO UNIT, recorded as one class row. Two
cheap things go into L-305 now because the export will require them
anyway: a `# Unit:` line on each new constant, and the bow shock
standoff written as an expression rather than a typed number. Record:
`documentation/DESIGN_unit_field_and_export_rev2_20260911.md`.

### 2026-09-12 -- the magnetosphere gets its models, and a Note turns out to be a store

**L-305 Gap item 4 landed** (pushed at `5b88007f`). Earth's magnetopause
is now Shue et al. (1998) and its bow shock is Jelinek et al. (2012),
carried by fifteen new rows in `constants_new.py` -- eight Shue
coefficients, Jelinek's R0 / eps / lambda, a bow shock cut angle, and
three declared solar wind conditions pointing at L-314. Both standoffs
are superseded and derived rather than typed. Every row written carries
a `# Unit:` line and a `# Status:` line.

**A patch may not leave its own output untrue, and that is the ruling
worth carrying.** The new bow shock figure made a cited hover sentence
arithmetically false: it told the visitor the value was drawn at the
midpoint of Lugaz's 11 to 14 Earth radii, and 13.51 is Jelinek at 2 nPa,
not a midpoint of anything. Tony's ruling split the work. The DELETIONS
and the attribution corrections travelled with the patch, because the
new number is what made those sentences false. The REWRITE -- the
validity ranges, the frame note, the gap between the two models -- stays
with item 7, after L-321's verdicts. Nothing new was said; four
sentences left and two attributions moved.

**`test_status_lines.py` shipped and is in the maintenance run.** It
enforces the Status Line grammar on every row that carries one: a
measured row carries a rung and a real `# Source:`; a declared row
carries neither a rung nor a citation on the status line itself; a
pending row names a handle; a derived row names inputs that exist. Rows
without a status line are reported and counted, not gated -- that walk
is L-322's. All eight failing rules were negative-tested before
delivery. Two rulings came out of building it: a scanner change to read
status lines belongs to L-322 with the one walk, not in front of L-305;
and a declared row MAY cite, because `INNER_CORONA_RADII` cites the
paper that states its convention.

**The belts opened a class, and it is not the one we thought.** Three
figures for the outer radiation belt reach a visitor: the drawn torus at
the flux peak, a hover saying 3 to 7 Earth radii, a tooltip saying
13,000 to 60,000 km. A Fable review corrected our diagnosis: the span IS
in the store, as prose in each row's `# Note:`, where nothing can
interpolate it and nothing can check it. **A Note became a store** --
and it had already drifted inside a single row, since the outer belt's
own Source cites Baker at 3 to 6.5 Earth radii while its Note two lines
below says L = 3 to 7. Tony's reframe closed it: units convert and
significant figures already govern them, so the frame is a convention,
not a design question. What the viewer must be told is which STATE each
number is in -- measured, an envelope with no sharp edge, or a
stylization. A radiation belt has no edge; we store the envelope with
its sources or we state the absence, and we do not pick a winner out of
a range. L-323 carries it; the magnetotail extent joined the slice.

**L-314 gained its sampling decision.** A nightly spot value is the
wrong sampler for a coronal mass ejection -- a shock compresses the
magnetosphere for hours, and a once-a-day build most likely misses the
event worth showing, leaving the viewer a quiet magnetosphere on the day
of a severe storm. The builder takes the day's ENVELOPE instead: minimum,
maximum and mean of each input and of both derived standoffs. What makes
it worth a viewer's attention, measured against the stored coefficients:
geostationary orbit sits at 6.6 Earth radii and the exhibit already
serves it, and at 10 nPa with Bz at -20 nT the magnetopause stands off
at 6.32 -- inside the satellites. Pressure alone barely does it; the
exponent is -1/6.6, so a tenfold jump moves the nose 29 per cent.
Southward field is what lets the boundary in. What it may not say is
that a CME caused it: that is an analysis, and Kp and the G-scale are
what is measured and publishable.

**Next.** L-305 items 6 (the gallery config, carrying three retired
claims), 5 (the port), 7 (the hovers, after L-321's verdicts), 8 (store
drift, then Mode 5 on the phone first). L-323's design record and
revision 3 prompts are owed and the 2026-09-11 prompts must not be sent
as they stand. Handoff:
`documentation/HANDOFF_L305_L323_20260912.md`.

### 2026-09-15/16 -- the magnetosphere is drawn, and the phone chrome settles

**Earth's magnetosphere reached the exhibit on 2026-09-15** (L-305 items
5 and 6b; `HANDOFF_L231_L305_magnetosphere_and_belts_20260915.md`). The
research had been done on the tenth and eleventh; nobody had served the
coefficients or written the code that turns them into a shape. Both
surfaces are now drawn from eleven served rows with no number typed into
the renderer, and the magnetopause stops at 120 degrees from the nose --
the furthest the authors plot their own model, declared, not measured.
The same session put Earth's belts in its equatorial plane (L-231): the
geostationary ring is drawn there at 6.6 Earth radii, inside an outer
belt served as spanning 3 to 7, and the ecliptic had put the two 23.4
degrees apart in one picture. Earth's dipole tilt became a store row,
quoted in the belt hover with its epoch. And the hover became the
glance: every citation, equation and served caveat moved to the i panel,
with one pointer line under each hover.

**That session's lesson: a checker exists for the failure you already
had.** Three checks passed while the thing they guarded was broken -- a
line-width rule on a hover that ran off the phone, a scene checker on a
month-old fixture, a "Source:" leg true only because the fixture had no
sources. It showed again on 2026-09-16: the new hover budget suite never
builds the Sun room, and four Sun hovers had missed the move to the panel
(L-331).

**The phone chrome settled on 2026-09-15/16, on Tony's Mode 5 each
round.** The drawer row got a finger-sized selection target, and a name
tap on an unticked shell now ticks it (L-318 round 3, amending L-267's
G2). Text boxes stopped breaking mid-sentence: a break that only keeps a
desktop line short is now soft, and the phone rejoins it (round 4). On a
portrait phone the text box lost its arrow and moved to the middle of the
view, where a tall box fits (round 5). With the box mid-view, the arrow
cross went back to the top right (L-316 round 4). And a phone tap now
reaches a shell's marker instead of its dots, which Plotly had let win
the tap (round 6) -- Tony: "always opens on first tap." Rounds 5 and 6
apply to a portrait phone only, on Tony's word; the desktop is as it was.

**The two instruments now disagree about Jupiter's belts** (L-231): the
gallery's shared belt renderer moved Jupiter's too, and the orrery's
Jupiter builder was not touched. No room shows Jupiter yet, and Tony
ruled that it can wait for Jupiter's room.

**Tony's standing rule of 2026-09-16: no compressed language in hover
text.** What the protocol asks of Claude's replies to Tony, the hovers now
owe the visitor (L-331).

**Next.** L-332 (the interactive-exhibit skill), then L-331 (the visitor
text, the four Sun hovers, and a plain-language pass over the hovers --
the Sun room is live, so it should be correct), Tony's calls on closing
L-316 and L-318, then L-330 (the belts' shape) and L-322. Handoff:
`documentation/HANDOFF_L316_L318_phone_chrome_20260916.md`.

### 2026-09-17 to 22 -- the store becomes the producer, and Earth is the first closed slice

**The orrery now EXPORTS its numbers and the gallery stops reading
orrery source** (L-322, gallery half deployed 2026-09-17). The gallery
pulls `data/constants_export.json`, the mirror writes each served number
from it with its unit and figure count, and two checks replace the old
drift check: Export freshness and the Pointer join. Two checks built
that week found the served cache out of step with the config (L-336)
and the live check not reading every file the browser fetches (L-339).

**Then the store was walked, one body at a time, Earth first.** Every
Earth row now carries a unit, a status and a figure count, and every
measured row a record of who opened its source and checked it (the
`# Read:` field). Stage C1, the 29 rows with nothing declared, landed on
2026-09-19; Claude Fable 5.1's review of it found a hover that was wrong
on the live site, the geocorona's, and the fix led to the figure rules
being rebuilt (L-342). Stage C2, the 28 magnetosphere rows, landed on
2026-09-22:

- The two standoffs are computed again rather than typed, and Shue's
  published uncertainties decide their figures: the magnetopause reads
  10.3 Earth radii where it read 10.25, the bow shock 13.5 where it read
  13.51. Each hover now says how far real crossings typically fall from
  the model.
- Earth's dipole tilt is computed from IGRF-13's coefficients: 9.4105
  degrees for 2020. The 9.6 it replaced was in no epoch of the model,
  and the drift the old note gave was ten times too small.
- The outer belt is drawn at the halfway point of its measured band,
  and the hover says that is a choice, not a measured peak.
- Earth became the store's first CLOSED SLICE: from now on a missing
  field on an Earth row fails the orrery's maintenance run, and the
  gallery fails a measured row behind a served number that nobody has
  recorded reading.

**Tony's rule behind the figure work, 2026-09-21:** "when it comes to a
decision, what is the basis? the basis should be in the skill not
arbitrary." provenance-discipline went from 2.14 to 2.17 in four days;
the last two were written down before the build that needed them, and
the questions they absorbed stopped reaching Tony.

**The swap stopped depending on Tony noticing** (L-216, 2026-09-20):
each rename retries, a failed swap puts the old cache back, and every
run writes a line to a tracked swap log. C2-b was the first build on it;
the swap worked on the first try, which proves nothing either way.

**The build's lesson: a check has to be visible where it is read.** The
new read check ran and passed on Tony's machine, and his screen showed
nothing of it, because the maintenance run prints only a check's last
line. A pass with the check and a pass without it looked the same. Its
counts now ride on that line (gallery `386a44ff`).

**Next.** Stage D of L-322 -- Earth's pole moves from
`idealized_orbits.py` into the store, because it draws a closed room's
axis. Before the next body, the conversion question on L-345: a km and AU
row per shell, or the export converting from full digits. Then the Sun's
slice, since its room is live, and after it the order of 2026-09-03
resumes with Jupiter and Saturn. The classes C2 found are L-343 to
L-361, recorded and not chased.

### 2026-09-23 to 28 -- Stage D closes, and a value in another unit stops being a row

**L-322 Stage D is finished.** It was the last stage of making the
orrery the producer of the numbers Earth's room prints. Recorded in
`documentation/HANDOFF_L322_D_print_counts_orrery_done_20260928.md` and
the handoffs before it:

- Earth's pole moved into the store and is worked out from Horizons for
  the date the room shows, with the tilt of that date in the hover.
- An exact number -- a definition or a declared drawing choice --
  prints the digits it was defined with, not a width chosen on the
  line. The declared solar wind pressure prints 2 nPa, not 2.0.
- The finishing check, "Exact rows by the count", passes with the
  gallery beside the orrery.

**Then the question held since Stage C2 was decided (L-345).** Tony,
2026-09-28: "follow the single source of truth principle ... compute
all conversions instead of duplicating." Each quantity is one row, in
the unit its best source gives it. Its value in any other unit is
worked out from that row's full digits and rounded once, with a figure
count taken from the source row alone (provenance-discipline 2.22). It
was built in four patches, all on 2026-09-28:

- orrery D19: the export serves every length row's value in each
  length unit, as `"in"`;
- orrery D19a: kilometre rows for the tops of the lower and upper
  atmosphere, so the gallery had rows to point at;
- one gallery patch: the page prints every kilometre and AU line from
  `"in"` and never converts a served number itself;
- orrery D20: the fifteen rows that were another row in a different
  unit became names computed from that row, marked `# Conversion:`, and
  a check fails on any new one that is not marked.

Fourteen hover lines changed for visitors, each to the count its source
supports (the list is
`documentation/PREBUILD_L345_gallery_hover_changes_20260928.md`): the bow shock's 86,200 km became 86,000 km, the
chromosphere's radius became 1.003 solar radii.

**Earth's crust is drawn at the mean radius** (Tony, 2026-09-28), the
sphere the interior layers are measured against, in both the orrery and
the gallery. The Earth radius as a unit stays the equatorial one, as
the IAU recommends. The difference is about 7 km, invisible at any
zoom; the hover says why.

**The build's lesson: a pull that cannot fail.** In a sandbox that
could not reach GitHub, the gallery's export pull reported "no change"
and the mirror then rewrote the config from an older export on disk.
It has not happened on Tony's machine. Recorded as its own class on
the ledger, under A Check That Cannot Fail Is Not Passing.

**Next.** The Sun's slice (L-371, L-386), then Jupiter and Saturn as
Artifact 2 -- the order in the executive summary. The orrery's own
hovers still print most converted values by a width chosen on the line
(L-352, L-387); that class waits for the orrery's display work.

### 2026-09-29 -- the Solar System room becomes the front door, and the order changes

**A design session made the room the gallery's front door.** Zero
code, recorded in
`documentation/DESIGN_solar_system_room_front_door_20260929.md`. Until
now the gallery had one way in, the card taxonomy of doors, rooms and
cards. Tony's idea is a second, more intuitive one: the solar system
itself. The taxonomy stays the complete index; nothing is removed. The
rulings, in short:

- The scene stays a clean orrery. Everything about where to go next
  lives in the drawer.
- The room opens on the Sun and Earth, the drawer closed and Earth's
  row highlighted, the view fitting 1.1 times Earth's distance. The aim
  is curiosity, not the whole system at once.
- The drawer opens on ten rows: the Sun, the eight planets and Pluto.
  "See more" adds the groups in place along the spine, outward from the
  Sun.
- Tapping a body selects it and highlights its row; ticking a row draws
  it and reframes the view. Everything ticks except the Sun.
- Groups (the main belt, the Trojans, near-Earth asteroids,
  trans-Neptunian objects) become rooms with a cloud, served once and
  drawn like a shell. Encounters draw the whole room at their date.
  Only what JPL Horizons can place is in scope.
- The swap: the room becomes the default once its nine bodies are in,
  without waiting for a date picker. The Explorer stays a card.

**Three strands met the same day.** Stage D had finished and patch D20
had landed (orrery `e5c3f92a`), which opened the gate the room's second
half had waited on. Patch 6 had finished the first half (gallery
`f46cf299`). And the design had changed what the second half is. Two
sessions, Claude Fable 5.1 and Claude Opus 5.5, reviewed the three
records against both repositories independently and agreed on the
substance. The filed result is
`documentation/HANDOFF_L363_three_strands_integrated_20260929.md`.

**The order changed, on Tony's ruling.** v34 put the room's second
half third, beside the Sun's slice and Artifact 2, when the room had no
purpose beyond itself. As the front door it sends visitors into the
other rooms, and the Sun room still prints numbers typed into the
gallery rather than served from the export (L-371). Three options went
to Tony: the second half next, swap included; the v34 order; or the
second half next with the swap held until the Sun's slice closes. Tony,
2026-09-29: "C. Confirmed as recommended." So the room is built and
accepted now, and becomes the default only when every room it leads
into prints served numbers.

**One constraint travels with the order.** The second half adds object
entries to `data/objects_config.json`; the Sun's slice rewrites the
Sun's served values in the same file through the gallery's mirror. Both
end in a cache rebuild. They are never in progress at once: one is
pushed and live-checked before the other starts.

**After the Sun, a direction in outline** (Tony, 2026-09-29, L-395).
"In the original orrery the shells came late." The gallery grows the
same way: symbols with positions from Horizons and osculating orbits
first, moons with them; then encounters; then shells and slices. The
objects come from the orrery's own dictionary, `celestial_objects.py`,
exported the way the constants are, so the gallery stops keeping a
hand-copied list; already the two copies disagree on Apophis's ID.
And because the dictionary itself can go stale, the check reaches past
it to JPL Horizons. Jupiter and Saturn's Artifact 2, v34's next step,
now falls in the shells phase. The details are that design round's.

**This restamp is at Tony's direction.** The design asked whether it
counted as a design build for the plan's restamp (L-296); Tony answered
by asking for the plan to reflect the ruling.

**Next.** The second half of L-363, from the integrated handoff's
section 4, step 1: a short design round, the five planets and one cache
rebuild, the drawer, and Tony's Mode 5. Then the Sun's slice, then the
swap, then the design round for the orrery's objects (L-395).


================================================================
PART 2 -- THE LINEAGE (formerly Section 10)
================================================================

## Section 10 -- Lineage

This plan draws from seventeen sessions across three Claude models + two pivots:

- **Fable 5 survey** (July 2, 2026): Four-front survey. L-079 as keystone.
  Five publication options. Six code proposals (L-079-L-084).
- **Fable 5 L-079 deep dive** (July 2, 2026): Five S-options, four M-options,
  three phasing strategies, repricing map.
- **Opus 4.8 convergence handoff** (July 2, 2026): Fetched JPL/GitHub terms.
  Converged site-never-fetches, three-tier cache, envelope-declaring GUI.
- **Opus 4.8 review of v2** (July 3, 2026): Verified shared-layer boundary.
  Caught `celestial_objects.py` seam.
- **Fable 5 review of v2** (July 3, 2026): Found `palomas_orrery_helpers.py`
  seam. Named assembly-duplication tension. Redefined gate as scene equivalence.
- **Opus 4.6 + Tony convergence** (July 3, 2026): Resolved option (b) -- shared
  assembler. Fork decision. Four domains identified.
- **Opus 4.8 review of v3.1** (July 3, 2026): Named server-vs-serverless
  decision. Two-substrate model. Cache-through-index from day one.
- **Fable 5 review of v4** (July 3, 2026): Star PKL cache provenance. Module
  corrections. Phase 7 drift window -> per-domain migration tails. Vocabulary
  waterfall -> just-in-time. Two-sided pilot. Animation envelope. Scene
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
  (resolved: two WYSIWYG pipelines, not a shared core -- each studio previews
  through its own viewer).
- **Opus 4.8 review of v8** (July 5, 2026): Confirmed pivot integrity,
  vocabulary preservation, constraint faithfulness, phasing coherence, and
  restraint carryover. Flagged second-renderer tension (resolved by
  two-studio WYSIWYG model). Flagged Pyodide cold-start acceptance criteria
  (resolved: gallery already serves 30 MB+ files, Pyodide is within norms).
  Verified `graph_objects` coupling makes full plotly package unavoidable in
  Pyodide. Confirmed 148 gallery entries vs "330+" claim. Provided headroom
  math (479+130+31=640 MB, but orbit/star caches are gitignored -- not in
  either repo). Nits accepted.
- **Opus 4.6 + Tony data serving exploration** (July 5, 2026): Discovered
  orbit cache and star cache are both gitignored -- not served by either repo.
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
  as Phase 0 deliverable -- `interactive.html` deployed to
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
  family (A, A', A'' relocate it; only engine reuse eliminates it). Verified
  plotly wheel is 9.9 MB (not 15), import is 0.06 s native (lazy in plotly 6),
  dead JS bundles are 19.5 MB of 43.2 MB uncompressed. Built and tested slim
  B' wheel: 3.9 MB, fully functional for `go.Scatter3d` + `fig.to_json()`.
  Recommended B' with A retained for frozen pedagogical demos (two-tier model).
  OQ-i through OQ-v for Phase 2 start. (`AB_FORK_ANALYSIS.md`, built on
  `873c6cd` / `827d0b3` -- **that file is in NEITHER repo as of
  2026-08-23**, and no near-match name exists. The lineage entry stays
  because the analysis happened and its results are recorded above; the
  gap is noted rather than the citation quietly dropped.)
- **B' cold-start measurement** (July 6, 2026): `measure_plotly.html` deployed,
  timed on iPhone Safari WiFi. Stock plotly from PyPI: 2.1-3.3 s total cold
  start. `import plotly.graph_objects` = 57-59 ms. WASM multiplier ~1:1.
  Acceptance threshold <=15 s -- passed at one-seventh. A/B fork resolved: B'.
  Phase 0 closed.

**Decisions made (cumulative):**

*Preserved from v7:*
- Site never fetches Horizons (Section 1)
- Three-tier cache, all offline (Section 1)
- GUI declares the envelope, including content type (Section 1)
- Assemblers read cache through index abstraction from day one (Section 1)
- Coverage index is solar system concept; other domains declare bounds simply (Section 1)
- One shared assembler per domain (Section 3)
- Assembler is new code; original code archived (Section 3)
- Four visualization domains recognized (Section 4)
- Star data is fully cached, 101 ly / mag 9, Gaia + Hipparcos (Section 4b)
- Other domain vocabularies designed just-in-time (Section 5)
- Animation presets as curated tier-2 exports (Section 1/Section 5)
- Phase 1 vocabulary complete (Fable, Jul 4)
- Animation/static consolidation verified (Phase 1)
- Scene spec is JSON-serializable from day one (Phase 1)
- DD/OQ rulings deferred to Phase 2 start (Phase 1)

*New in v8 -- the pivot:*
- Gallery is the web publication, not a separate app (Section 2)
- Science museum model: curated permanent collection + interactive exhibits (Section 2)
- Incremental delivery: each interactive page ships independently (Section 2)
- JSON bridge: pre-curated and interactive content produce the same artifact (Section 1)
- Pyodide for client-side computation; no server (Section 1)
- Desktop migration deferred from critical path (Section 2)
- Matplotlib question dissolved -- gallery is Plotly (Section 7)
- Phase 6 dissolved -- gallery IS the UI (Section 5)
- Server-vs-serverless resolved in principle: serverless/Pyodide (Section 7)
- Gallery viewer: Option C hybrid -- two pages, `index.html` + `interactive.html` (Section 2a)

*New in v9:*
- Phase 0 proven: Pyodide v314.0.2 + NumPy + Plotly.js on static GitHub Pages (Section 5)
- Server/serverless resolved in practice: Pyodide (Section 7 #1)
- A/B architecture fork resolved: B' (Section 5, Section 7 #10, measurement: 2.1-3.3 s)
- Two-tier model: frozen A exhibits + data-backed B' exhibits (Section 1, Section 5)
- F2 canonical per-object storage adopted (Section 3a)
- Three trace types: actual positions, osculating at epoch, mean elements (Section 3a)
- Two data types to serve: osculating elements + position vectors (Section 3a)
- Two classes for rolling cache + spacecraft write-once (Section 3a)
- Phase 1b inserted: data serving pipeline (Section 5)
- Consent gate for Pyodide loading (Section 5, Section 7 #10)
- L-086 attribution gate ruled: JPL-only with inline credit passes (Section 5)
- `interactive.html` deployed as first exhibit (Section 2a)
- `orbit_paths.json` and `orbit_cache/` added to `.gitignore` (Section 3a)
- URL parameter scheme: `?exhibit=` (Section 2a)
- Slim self-hosted plotly wheel (~3.9 MB) in Phase 1b serving home (Section 5, Section 7 #10)

*New in v10:*
- Phase 1b design converged v0.4, three-model review (Section 3a, Section 5)
- OQ-E resolved: H2 subfolder in gallery repo (474 MB used, 526 MB headroom,
  ~72 MB all-phase data needs) (Section 3a)
- 14 settled schema decisions: osculating center, parent position files,
  trajectory_of, presets self-contained, subtract-don't-requery, unit-is-data,
  feature rendering always JS, validation invariants, grid nesting (Section 3a)
- Coverage index schema v0.3 with 8 validation invariants (Section 3a)
- Feature rendering architecture: three-context split (Section 3a)
- OQ-B/C/F/G settled; OQ-A/D positioned; OQ-E pending CORS check (Section 3a)
- Fable access extended to July 12, 2026 (Section 5a)
- Phase 1b deliverables refined: coverage index, feature configs, export
  script with invariant assertions (Section 5)

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
- Mean elements (Section 3a's original "three trace types," never implemented in
  Phase 1b) completed for planets + a curated comet list (Halley,
  Ikeya-Seki), porting the orrery's existing name-keyed lookup mechanism.
  Satellites/moons explicitly excluded -- their mean-element source data
  lacks secular-rate terms and is inconsistently dated/sourced; flagged as
  an orrery-side cleanup candidate, independent of this build.
- Section 3a's "feature rendering always JS" reaffirmed after a synthesis draft
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
- New failure class recorded (see Section 6): a correction reaching one copy
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

*New in v18 (August 13, 2026):*
- **Track 1 tooling advanced on three fronts; no rendering code touched
  and no Track 0 or Track 2 work moved.** L-186 closed, L-188 closed,
  L-189 closed, L-192's scanner half built. The plan's phase structure
  is unchanged; this entry records what the provenance layer now does
  that it did not do on August 7.
- **L-186 closed, and it was never a data question.** The six
  `duplicate_identity` findings carried through three handoffs as
  "each needs a look at the source" were all the parser misreading
  correct annotations. The retired annotation grammar put a free-text
  source before the check date, so a source carrying its own
  publication year ate the date and the model name landed outside the
  checker identity -- two annotations by two DIFFERENT models read as
  one checker written twice. Measured: 54 of 134 annotation lines
  codebase-wide were affected. The fix was the grammar, not the six
  sites: checker first, optional source clause, retired order REFUSED
  rather than reconstructed. All 134 lines migrated.
- **L-188 closed. `maintenance_run.py` runs four generators and twelve
  checkers in about 40 seconds.** Its first pass confirmed its own
  premise by finding two red test files nobody had executed -- one
  asserting an unannotated corpus since roughly August 3, the other
  failing 6 of 73 against values deliberately corrected on August 2.
  Neither was detectable before, because neither file was in any
  routine.
- **55 pinned constant literals retired; `constants_change_report.py`
  replaces them and stores no numbers.** It asks git what changed in
  `constants_new.py` since the last commit and reads both values out of
  the diff -- so it covers constants that do not exist yet. 18
  structural tests kept (derivations, orderings, cross-consistency,
  completeness); none holds a copy of a measured value.
- **Protocol v3.39: "A Check That Cannot Fail Is Not Passing"
  [CRITICAL].** Companion to Verify Execution, Not Appearance, one
  layer out: that gate asks whether the code you edited is the code
  that runs; this one asks whether the CHECK you are trusting can
  produce a failure at all. Three instances in one session, each in a
  different layer and each indistinguishable from a pass. The three
  moves: make success carry evidence, make the blind spot announce, put
  the check where it runs.
- **L-192's scanner half built (August 12-13): cross-check credit now
  requires ATTACHMENT.** The scanner counted any annotation inside a
  30-line window. That window is correct for a citation -- a section
  header naming IAU Resolution B3 legitimately covers the constants
  beneath it -- and wrong for an annotation, which names one checker
  who verified one value on one date. The deciding case:
  `INNER_LIMIT_OORT_CLOUD_AU` wore the cross-checked rung on
  annotations belonging to the heliopause constant three lines above,
  while the worksheets those annotations name read UNVERIFIED and
  PARTIAL for the Oort value. The window was converting a recorded
  non-verification into a top rung.
- **Audit movement: the cross-checked rung fell from 77 to 50.**
  Nothing got worse; 50 was always the true number. Four orphan
  annotations are reported -- two section headers in `constants_new.py`
  written to cover a group, which the codebase has no grammar to
  express.
- **Ruled: per-value annotations, not block-scope grammar.** A parser
  cannot distinguish group intent from proximity, because in bytes they
  are identical. The reason to prefer per-value is the Oort case: a
  block annotation reading "everything below checked" would have
  papered over two UNVERIFIED worksheet rows inside its own scope.
- **A number was wrong twice before it was caught, and the method note
  matters more than the number.** Fable's written attachment rule and
  its own measurement script disagreed; the independent verification
  leg reproduced the error, because it implemented the same prose and
  read it the same wrong way, and the agreement was reported as
  confirmation. Cross-AI independence protects against a shared model,
  not a shared specification. Correct split: 50 keep, 27 drop.
- **L-192's checker itself is designed and reviewed, not built.**
  Pre-design and Fable's review both anchored `00219d9`; verdict sound
  with changes. Four layers, each with a named failure: worksheet
  exists, row located, value agrees, verdict read. Three additions
  accepted -- an identity-consistency check (the worksheet filename
  must carry the checker token; 134 of 134 pass today), a
  drift-since-check against the tier2 schema's `Code value` column
  (reaches 72 of 134), and DERIVED split out of QUALIFIED. Fable
  proposed treating DERIVED as closed-by-derivation, citing L-158;
  L-158 rules the opposite and the convention wins.
- **Ruling changed: the checker joins `maintenance_run.py`.** The
  earlier ruling kept it out on cost grounds. The cost was never the 34
  markdown files -- it was one more block of output to read before
  every push. One line carrying a denominator answers that, findings to
  the audit, report-only. It does not gate pushes.
- **A standing move, new: reopen the session that produced the
  evidence.** Tony's ruling -- we do not have to accept and interpret
  incomplete or malformed answers. Two cited worksheets were unusable,
  one prose a tool cannot read and one carrying seventeen unresolved
  rows, and the design was drifting toward a parser clever enough to
  cope. Going back to the originating conversation closed nine of
  seventeen rows, settled the Mercury radius that had been open eleven
  days, and surfaced two annotations crediting a worksheet for checks
  it explicitly did not perform. Now carried in
  provenance-discipline v2.3.

*New in v19 (August 23, 2026, implementing the 2026-08-22 ruling):*
- **The braid: provenance stops being a gate and becomes a per-artifact
  slice** (Tony's ruling, 2026-08-22). Step one of the critical path had
  8 clean rows of 105 and 292 Tier-1 findings tree-wide, and a full
  session on 2026-08-22 went to ONE solar shell that is not in Artifact 2
  and does not block it. A precondition that does not terminate is not a
  plan. Priority becomes what the NEXT ARTIFACT renders -- for Artifact 2,
  thirty measured numbers. The five segments of Section 5a do not move;
  the order they are worked in does, and segment 3 goes first.
- **The load-bearing half is the render.** Ring provenance today is text
  checked against text. Once the assembler draws, a wrong ring radius is
  something Tony's eyes can catch -- and the resident gate already says
  the render wins when it disagrees with a code reading. Building the
  rendering layer is what gives the provenance work something to be
  checked against. Rings can be drawn without being fingerprinted;
  BUILDING and LOCKING are separable and v18 conflated them.
- **A full-document sweep, not a section edit.** Every numeric and status
  claim in this file was measured against HEAD rather than read forward,
  and 63 file references were resolved against both repos. Twenty-nine
  items had moved. The pattern in them is worth more than the list: five
  ledger items the plan called open had closed (L-087, L-108, L-120,
  L-151, L-162), one stated REASON was false while its conclusion held
  (the helpers seam), two size figures disagreed inside one document, and
  two questions the plan told a future session to resolve by looking were
  answered by looking.
- **The skill-version list is deleted, not updated** (Tony's ruling,
  2026-08-23). The closing block restated ten skill versions by hand and
  five had drifted, provenance-discipline worst at 1.8 against an actual
  2.6. It is a second store for a value the protocol's generated Skill
  Manifest already owns, and Stale Skill = Stop compares against that
  manifest, not against this document. Fix the producer, not N consumers.
- **An unmatched code fence removed.** The file carried five ``` markers,
  an odd count; the last opened a block that never closed.
- **The document is now pure ASCII.** 22 U+2032 PRIME and one U+2033
  DOUBLE PRIME, all in the B-prime architecture name, became ASCII `'`
  and `''`. The first v19 patch reported them and declined to sweep
  them, reading the encoding gate as scoped to delivered code. Tony's
  ruling, 2026-08-23: a patch already holding a file open fixes
  incidental non-ASCII, and markdown is not an exception to Stamp What
  You Change. Section 5a already spelled the name `B'`, so this makes
  the document self-consistent rather than imposing a new convention.
- **Authorship dates corrected.** The first v19 patch stamped itself
  2026-08-22 throughout and ran on the 23rd. Ruling dates were right and
  stand; the eight authorship and measurement dates moved. Recorded
  rather than quietly fixed, because a document about anchors being true
  is the wrong place to be casual about which day something happened.
- **Two consequences recorded rather than resolved here.** L-225 has no
  ledger entry although the design note and the session queue both cite
  it; and L-154 is ledger-BLOCKED while this plan now makes it the first
  work. The plan carries sequencing authority and the ledger carries
  status authority (L-221), so both are ledger edits.

---

