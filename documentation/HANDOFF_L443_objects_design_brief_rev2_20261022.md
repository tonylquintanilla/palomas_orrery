<!-- Doc-Kind: hand | Brief, revision 2, for the DESIGN session that scopes how the rest of the orrery's objects come to the website (L-443, stage 11), then builds the first slice in the same session if the design settles. Carries Tony's three rulings of October 22 (the objects go next; slice 1 by kind; barycentres and the drawn orbit's centre are settled by existing rules) and takes the Solar System room's drawer and stage 10 with it. Supersedes HANDOFF_L438_objects_to_website_brief_20261013.md, which stays as the record. -->
# Brief, revision 2: the orrery's objects come to the website (L-443, stage 11)

Read at orrery 1c591cf ("cleanup", 2026-10-22 00:16) at
https://github.com/tonylquintanilla/palomas_orrery and gallery 90cefa5
at https://github.com/tonylquintanilla/tonyquintanilla.github.io.
**This session starts AFTER the L-434 build session (the tide and the
clumps stored) has closed and pushed**, never beside it: both touch
`feature_renderers.js`, `objects_config.json`, `export_drawings.py`,
the ledger and Where We Are. Pin both repositories at HEAD when the
session starts; read `HANDOFF_L434_*` and Where We Are first.
Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Written October 22, 2026 by Anthropic's Claude Fable 5.1, in a
coordination session, for a Claude Opus session. Revision 2 of the
brief of October 13 (`HANDOFF_L438_objects_to_website_brief_20261013.md`;
the handle is L-443, since L-438 was retired before the item opened).
Companion: `HANDOFF_road_ruling_objects_next_20261022.md` (the ruling
that this goes next, and the deferred list).

- Type: DESIGN SESSION brief (zero code until Tony's word), then the
  first slice's build in the same session if the design settles.
- Tony is likely at his machine; he can look at a mock-up on his phone
  and run patches.

## 0. Before building

- Pull both repositories at HEAD and pin each SHA.
- Skills this task fires: gallery-cache-builder 1.11 (the nightly
  builder fetches each served object; objects_config; the serving
  cache), interactive-exhibit 1.19 (the Solar System room's drawer,
  what a body's row carries, the words-and-link contract, the drawer
  order), gallery-assembler 1.3 (how a position is propagated and what
  the served window allows), horizons-orbital-mechanics 1.8 (ids,
  record pinning, a comet's record number, the two-centre test),
  provenance-discipline 2.33 (a served description's numbers are
  sourced or come out; the gate binds at export), ledger-and-session-
  records 1.21. Confirm each against the manifest at HEAD; the L-434
  session may have bumped one (its handoff says).
- Read `export_objects.py`'s rule: an orrery entry is exported when it
  carries a `'key'` equal to the website's slug, and "an entry gains a
  key when the website starts serving it, and not before."

## 1. What Tony wants, and what is there

Tony, 2026-10-13: "I am anxious to add the symbols to the gallery too
so visitors can at least plot positions." 2026-10-22: "I am anxious to
add the symbols to the website. We could keep going with this backlog
but we may be at diminishing returns and could defer some items." The
symbol is the marker at a body's position in the Solar System room;
"plot positions" is the room's existing job, done today for 19 served
objects, 13 of them keyed to the orrery's list.

Measured at orrery 1c591cf: `celestial_objects.py` holds 71 orbital
entries (planets, dwarf planets, asteroids, comets, trans-Neptunian
objects), 47 satellites, 38 trajectories (spacecraft), 10 Lagrange
points, 6 barycentres, Planet 9, 1 fixed, and 16 exoplanet-system
entries (the stars' domain, out of scope). The website serves 19: the
Sun, 8 planets, the Moon, Io, Titan, Pluto's barycentre, Pluto, Charon,
Apophis, Voyager 1, Encke, Halley.

What one new object costs today: a `'key'` on its orrery entry; a
config row written through the mirror (never by hand); a nightly fetch
(one Horizons query per object per build, with the pause between); a
sourced description (a number in a served description is sourced or
comes out); a drawer row in the room. The drawer lists every served
body; 19 rows fit a phone, and 160 do not.

## 2. Settled on October 22 (Tony's rulings; no re-asking)

1. **The objects go next.** After L-434, this item, with the deferred
   list behind it (`HANDOFF_road_ruling_objects_next_20261022.md`).
   "Yes, and let's keep the deferred list prominent so we can come
   back to it."
2. **Slice 1, by kind** ("Yes that's reasonable"): the orbital bodies
   a visitor would look for that the orrery already draws and the
   website does not: the dwarf planets (Ceres, Haumea, Makemake, Eris,
   Gonggong, Quaoar, Orcus, Sedna and the other trans-Neptunian
   objects), the named asteroids (Vesta, Psyche, Bennu, Eros, Ryugu,
   Itokawa, the Lucy targets, the near-Earth bodies) and the comets
   (Hale-Bopp, Hyakutake, Churyumov, NEOWISE, Tsuchinshan-ATLAS, MAPS,
   3I/ATLAS and the rest), about fifty after the 19 served are taken
   out of the 71. Then slice 2, the spacecraft; slice 3, the moons by
   planet; the Lagrange points last or never (recorded, not chased).
   The session COUNTS slice 1 exactly from the dictionary at HEAD and
   may propose splitting it in two if the description count (section
   3, question 4) makes one evening impossible; the split is Tony's
   to confirm, the kinds are not.
3. **Barycentres are settled by two existing rules** ("Agreed as
   settled"), so the session lists the pairs rather than asking body
   by body:
   - In a Sun-centred room a body is served by the record the orrery's
     dictionary gives for its motion about the Sun: a small body's
     `helio_id` (the small-body solution; Eris, Haumea, Makemake,
     Gonggong, Quaoar, Orcus all carry one), or a planet's barycentre
     record as Pluto's 9 is. The body-centre records (920...) are for a
     body's own future room, not this one (the assembler never
     translates between centres).
   - The Barycenter Rule (orrery-coding-conventions): the shared centre
     is drawn, and the symbol's words say "marks the shared centre",
     only when it lies outside the primary; mass ratio is the
     gatekeeper. By the known ratios: Orcus-Vanth and
     Patroclus-Menoetius outside, like Pluto-Charon; Eris, Haumea,
     Makemake, Gonggong, Quaoar inside, so the symbol is the body with
     no sentence. The session confirms each ratio from an open source
     before the words are written, and lists the pairs with their
     sources. The barycentre's own period around the Sun (L-443's
     Pluto loose end) applies to the same pairs.
4. **The drawn orbit's centre is settled by the two-centre test**
   (horizons-orbital-mechanics 1.8, L-431): the period and the drawn
   ellipse are taken around the Sun or the solar system's barycentre,
   whichever moves less over a year, chosen at the period fetch and
   saved with the record; the website follows through the export and
   the "Cache in step" check. The symbol's position stays about the
   Sun; the ellipse is shifted so its focus sits at the barycentre.
   The session reports which centre each new body chose; nothing goes
   to Tony.

And from the October 13 brief, still settled: the orrery is the one
definition of each object (L-395); provenance closes before export;
the Horizons check confirms each served object on its cycle, and each
added object joins its list; the drawer's conventions (Go To in the
middle, the room button to its right, names that wrap), Home's order,
and now the drawer order by where each shell begins (L-460).

## 3. The questions the design session answers, one at a time

1. **The drawer, and stage 10, together.** Today's drawer is one list;
   slice 1 alone takes it past what a phone shows. And stage 10 on the
   road (a bare `interactive.html` link opens the Solar System room;
   the Explorer gets its own address) makes this room the front door.
   Tony's ruling of October 22: these are one design, not a drawer
   built twice. Options to bring WITH A MOCK-UP for his phone (Mode
   5): groups that fold (planets, dwarf planets, asteroids, comets,
   spacecraft, moons by planet), "All / none" per group, a search box,
   or See more by group as today's See more does by distance. The
   drawer's standing rules hold: the Solar System room's rows run
   outward from the Sun by body (L-363, kept on October 20); the
   highlighted row scrolls into view; Go To's arrow. Say what stage 10
   changes in the page's boot path and the gallery's lobby card, and
   whether it ships with slice 1 or after.
2. **The nightly cost.** Fifty more objects is fifty more Horizons
   queries per build, with the builder's pause between. Options: fetch
   all nightly (measure one build with slice 1 added before deciding);
   fetch the planets nightly and the rest on a longer cycle; fetch on
   demand. Recommended: measure first, and say the minutes. If a
   longer cycle is chosen, the served window and the trust cap follow
   (gallery-assembler, gallery-cache-builder).
3. **Descriptions and links.** Each served object needs a sourced
   description and an info link, by the words-and-link contract. The
   orrery's `mission_info` text is the source for most; a number in it
   is sourced or comes out before export (provenance-discipline 2.33,
   and an agency page that names no source is read one layer down).
   This is the slow part and the honest one: COUNT how many of slice
   1's descriptions carry a number before the build starts, and say
   it. If the count makes one evening impossible, propose the split
   (section 2, ruling 2). The words come to Tony as a list before they
   ship.
4. **Comets and record pinning.** A periodic comet's record number
   moves (horizons-orbital-mechanics, Checking an Entry Against JPL);
   each added comet is pinned the way Encke and Halley are. MAPS and
   3I/ATLAS get their live check once served (L-443's loose end).
5. **The loose ends on L-443**, taken with the slice they touch: the
   served objects with no `'key'` (moon, io, titan, pluto, charon,
   voyager_1) get a key, a period and a Horizons check when their
   slice comes (the moons' and the spacecraft's); the fields the list
   lacks (a moon's parent, a clean kind) are added when the slice
   that needs them opens, not before; the display-name rename waits
   for names to stop being keys.

## 4. Build notes for slice 1 (after Tony's word on questions 1 to 3)

- Orrery patch: `'key'` fields on the chosen entries; descriptions
  checked for unsourced numbers (the count from question 3, each
  sourced or removed, the words listed for Tony); `export_objects.py`
  unchanged in rule; the period fetch runs the two-centre test for
  each new body at the maintenance run (it asks JPL; the sandbox
  cannot, so Tony's run is the live test, as L-395's was).
- Gallery patch: the mirror carries the new rows; the config gains
  their centre, frame, trace policy and accuracy row (the accuracy row
  by the orrery's DE430 groups, or "none stated" for a small body
  until its own uncertainty is fetched, L-399; a small body's 3-sigma
  comes with its position query, `VEC_TABLE='2xr'`, as the orrery's
  hover already does, L-401); the drawer shows them by the chosen
  grouping; the pairs with a shared centre outside the primary get
  Pluto's sentence, the others none.
- Planted faults: a keyed entry with no description; a served
  description with an unsourced number; a config row written by hand
  (the mirror check); a body drawn with no accuracy row and no "none
  stated" words; a comet served by a record number that moved; a
  drawer row out of its group.
- Then the Daily Run builds the cache (the first build with slice 1 is
  the measurement for question 2); a visitor sees the bodies on the
  next push after that. The live run after the push.
- The look: the drawer on the phone, upright and sideways; three new
  bodies hovered (one with Pluto's sentence, one without, one comet);
  one comet's orbit drawn; Sedna's ellipse around the barycentre.
- Skills: interactive-exhibit (the drawer's grouping, and stage 10 if
  built) and gallery-cache-builder (the fetch cadence, if changed). One
  version each, under One Session, One Bump, each with its protocol
  entry and the reinstall obligation.

## 5. For Tony, one at a time, in the design session

- (decide, at a mock-up) How the drawer holds them, and whether stage
  10 ships with slice 1 (question 1).
- (decide, after a measurement) The nightly cadence (question 2).
- (decide, after the count) Whether slice 1 splits in two (question 3).
- (decide, recorded, not urgent) Whether Lagrange points and the
  exoplanet entries are ever served.
- (approve) The words list: slice 1's descriptions, and the
  shared-centre sentences.

## 6. Tony's actions, all of them

- (do) Start this session after the L-434 session has closed and
  pushed.
- (decide) The items in section 5.
- (do) Run slice 1's two patches, the maintenance run and the Daily
  Run; look on the phone; push; the live run.

## 7. At the close

- A design record `DESIGN_L443_objects_rulings_<date>.md` (the
  rulings in Tony's words, the mock-up chosen, the measurement, the
  count, the pairs with their mass ratios and sources, which centre
  each body chose).
- The handoff, the ledger (L-443; the loose ends re-homed by slice;
  L-461 built or scheduled with it), Where We Are (stage 11 [NOW];
  the Deferred section unchanged unless an item was picked up), the
  skill bumps if any.
- "Where this leaves us", two or three lines in Where We Are's words.

Brief written October 22, 2026 with Anthropic's Claude Fable 5.1.
