<!-- Doc-Kind: hand | A design-review prompt carried to a reviewer model: the website's room system as one nested tree (L-515). Communication; written once, read by its receiver. -->
# Design review request: one nested tree in place of isolated rooms (L-515)

Built on orrery 27f6f5bdc34616f2eecd19e290a51a0eaa059c08 at
https://github.com/tonylquintanilla/palomas_orrery (branch main)
and gallery ae68a93aa1ba6fac94e0b16d19247f6e3f2c0c29 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch main).

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: DESIGN REVIEW (zero code). Written November 7, 2026 with
Anthropic's Claude Opus 5.5, the coordinating session, for Tony
Quintanilla to carry to a reviewer model.

The rules this work runs under. If you can fetch GitHub (Claude, GPT),
also fetch these, from the orrery at the SHA above:
- `PROJECT_INSTRUCTIONS.md` (the protocol; read its Part 4 section "The
  Orrery and the Assembler" and Part 3's Fetched vs Recalled at least);
- `skills/interactive-exhibit/SKILL.md` (1.32: rooms, drawer, arrival,
  text boxes);
- `skills/gallery-assembler/SKILL.md` (1.3: centres, propagation, the
  orrery/assembler boundary);
- `skills/gallery-cache-builder/SKILL.md` (1.18: what the nightly build
  fetches and serves);
- `skills/horizons-orbital-mechanics/SKILL.md` (1.18: JPL centres, path
  plans, encounters).
If you work from an imported snapshot of the orrery (Gemini), the same
files are in it at those paths; say the date of your import. A gallery
import does not contain them.

PLEASE BEGIN YOUR RETURN by listing which of those files you actually
read. A return that does not name them will be read as not having read
them.

## Who this is for

Tony Quintanilla, PE, is a retired civil and environmental engineer, an
artist and an anthropologist. He is not a programmer or an astronomer.
He builds this project through conversation with AI partners and holds
every design decision. The code's quality is the product of that
collaboration, not evidence of his programming skill. Write your return
in plain words: lead each finding with one plain sentence, one idea per
sentence, and explain any technical term the first time you use it.

## The project in two sentences

Paloma's Orrery has two instruments. The ORRERY is a desktop Python
program that asks JPL Horizons (NASA/JPL's ephemeris service) for
positions live, around any centre. The WEBSITE (palomasorrery.com) has
no live connection: a nightly build fetches JPL's answers into a served
cache, and the page works positions out in the browser from those
answers.

## What the website does today

- `interactive.html` holds a table of ROOMS, `const EXHIBITS`, chosen by
  `?exhibit=<key>`: the Solar System room (the default, Sun-centred),
  the Sun room and the Earth room. Each room defines its own drawer
  (the list of things a visitor ticks) and its own features.
- The Solar System room's drawer is served in
  `data/objects_config.json`, under `rooms.solar-system.drawer.rows`
  (113 rows): the Sun, comet groups by JPL class, Mercury, Venus, the
  Aten group, Earth, Spacecraft, and so outward. A planet's row offers
  "Enter the <name> room" when a room exists.
- Every object in `data/objects_config.json` names a `parent`: "sun"
  for 97, none for the Sun, Earth for the Moon, Jupiter for Io, Saturn
  for Titan, Pluto for Charon.
- Each body's features are served under that body (`features`): the
  Sun's sun_structures, solar_atmosphere, solar_wind (its members are
  the Termination Shock and the Heliopause), oort_cloud, orientation,
  hill_sphere; Earth's earth_interior, earth_atmosphere,
  earth_exosphere, earth_orbital_zones, earth_geostationary,
  earth_magnetosphere, van_allen_belts, hill_sphere, orientation. The
  main asteroid belt's cloud is the exception: a drawing named on the
  Solar System room's row, not on a body.
- The Moon is served around Earth (`canonical_center` "@399"); the Earth
  room draws it with its full text box (`gallery/earth_geometry.js`,
  `moonBox`).
- A fixed design principle: the website never moves a position from one
  centre to another by SUBTRACTING two JPL answers. It was tried and
  retired for catastrophic cancellation (the protocol, "The Orrery and
  the Assembler").

## The problem Tony named (Nov 7, 00:17 Chicago)

"The model we are using is that of isolated room with their defined
features. A solar system room, a sun room, an earth room, next a mars
room, etc. the problem is that they are isolated and their features
cannot be shared. I think what we need is a nested system much like the
orrery's flat objects list." His tree: Solar system; Sun (shells;
comets by type); Mercury (shells); Venus (shells; asteroids); Earth
(shells; Moon, with its shells; space missions by type; asteroids by
type); Mars (shells; Phobos; Deimos); Asteroid belt (belt cloud; named
asteroids); ... TNOs; Termination shock; Heliopause; ... Gravitational
influence.

## The design as ruled so far (Nov 7, Tony's words quoted)

These rulings are in the orrery ledger's L-515 in Tony's working copy;
the newest are not yet pushed, so they are given in full here.

1. One page, one tree. Two kinds of "under": an ORBITING child (the
   Moon, Phobos) is fetched from JPL around its parent; a NEIGHBOURHOOD
   child (the Atens under Venus, missions under Earth) still goes around
   the Sun and is only placed there for the visitor.
2. CENTRE and FOCUS are different acts. Centre: a body at the middle,
   everything drawn fetched around it. Focus: the camera moved to a body
   in the view it is in (Go To, today). True centres are the Sun, each
   parent with satellites, and later the encounters for their dates; any
   other body is focused on, not centred. Arbitrary centring stays the
   orrery's. Tony: "Yes that is what I mean. Focus is valuable for small
   details, for example comet features, flybys, possibly moons."
3. Once a body is the centre, the drawer lists its branch only, with a
   trail line at the top ("Solar system > Mars") whose first part
   returns to the Sun. A parent's row offers "Centre on <name>". Tony:
   "A."
4. An encounter is a dated node under the body met, also listed under
   the visitor; its row opens the body met as centre at the encounter's
   own dates; leaving returns to today. A visitor choosing any date is a
   separate, later feature. Worked case, read from the served config:
   the Psyche spacecraft's path plan (`psyche_spacecraft`, made
   2026-11-04) names a Mars flyby, closest 2026-05-15 19:29 UTC at
   8000.4 km, window 17:03 to 21:54 UTC; JPL's data for the craft ends
   2029-02-24, before the arrival at 16 Psyche. Tony: "Yes ... Date
   Selection is not needed for this."
5. Every feature keeps its body as its centre. Seen from a view where
   its body is not the centre, it is carried to its body's place by
   ADDING the body's position (a shape moved with its body, not two
   answers subtracted).
6. Lagrange points: one group per pair, under the pair's smaller body,
   listed also under the larger; each drawn in the centre JPL serves it
   around. Ledger L-297 records JPL serving the Earth-Moon points as
   targets 3011 to 3015 around Earth (sizing record:
   `documentation/SIZING_earth_moon_lagrange_20260907.md`, orrery).
   Tony: "Good."
7. Mix and match: from any centre a visitor may tick anything in that
   centre's branch together; from the Sun, the root, everything mixes
   (Voyager 1's path with the Heliopause).
8. A third viewing act, LOOK TOWARD: the camera at the centre, pointed
   at a body drawn there, as the orrery's `add_look_at_object_buttons`
   (`visualization_utils.py`) does. Case: Earth as centre on the March
   equinox, looking toward the Sun, looks along the first point of
   Aries -- a little off the website's x axis, which is the J2000
   ecliptic's, by the precession of the equinoxes since 2000. Tony:
   "Yes."
9. Proposed build order, not yet ruled: (1) the tree in the served data,
   each object's parent and kind of child; (2) the page: one drawer from
   the tree, the trail line, "Centre on", with the Sun and Earth as the
   first centres and today's room addresses still opening them; (3) Mars
   as the first new centre, with Phobos and Deimos (ledger L-514, the
   Mars room, whose four rulings stand); (4) encounters, with the
   historical missions' slice 2 (ledger L-507).

## What we ask of you

Review the design above against the code and data at the two SHAs, for
GAPS and ISSUES. In particular:

- Is anything in the rulings inconsistent with another ruling, or with
  how the code actually works today? Name the file and function.
- Rule 5 and rule 7 rest on ADDING a parent's position to a child's
  parent-centred answer being sound where subtracting is not. Is that
  right for what the page draws, given that each position is worked out
  in the browser from served elements with its own drift error
  (`gallery/assembler/render_orbits.py`, the trust block in the served
  cache)? Where would it show visibly wrong?
- What does the tree need from the nightly build that it does not serve
  today (`tools/gallery_cache_builder.py`; ledger L-297 says it serves
  three shapes: osculating elements, a spacecraft positions arc, and
  features only)? Which centres need new fetches?
- Which existing pieces does each build step touch, and is the order
  safe: does step 2 keep every existing room working for a visitor?
- What has the design not decided that a builder would have to guess?
  (For example: a neighbourhood child's place when its group sits
  between two parents; how a bookmark of a centre is written; what the
  page shows when a centre's data has not been built yet.)
- Anything else you would flag, including a simpler shape we missed.

Please do not redesign the whole system. Where you disagree with a
ruling, say why in a sentence and leave the decision to Tony. Mark each
finding as one of: VERIFIED (you read it in the code or data, with the
file and the function or key), INFERRED (your reasoning, not checked),
or QUESTION (only Tony can decide it). Separate a question about HOW the
work is done (a method a rule could settle) from one about WHAT the
project should be (Tony's).

## Return format

1. The rule files you read, by path.
2. Findings, most important first, one to a numbered item: a plain
   sentence; then VERIFIED, INFERRED or QUESTION; then the file and the
   function or key where it applies.
3. Your view of the build order in one short paragraph.
4. Nothing else. No rewritten design, no code.
