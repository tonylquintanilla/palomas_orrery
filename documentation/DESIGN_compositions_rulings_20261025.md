<!-- Doc-Kind: hand | Design record of the Oct 25 evening talk: a composition (a curated view within a room, authored in the editor, served as data, with an interpretation in the i panel). Opens a new ledger item, next free handle; zero code. -->
# Design record: compositions, the curatorial layer

Tony Quintanilla, PE | Claude Fable 5.1 (coordinating session, talk only) | October 25, 2026, evening

Built on orrery 0c27f47ad631efbfc611a80404095649025687d6 at
https://github.com/tonylquintanilla/palomas_orrery (branch main) and
gallery b1a4ce6c7fc72b17571a13e18ab11df98b86485b at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch main),
the last SHAs this session read live (the morning of Oct 25). Build B
of slice 2 ran the same day and pushed past both; the protocol is at
v3.112. The next session reads HEAD before building on this record. No
code was changed in this session.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: DESIGN SESSION record (zero code). Opens a new ledger item, with
the next free handle, for a records patch to create. Companion to
L-486 (a view carried into a room), L-483 (a comet room), and the build
B session's finding of Oct 25 that Voyager's crossing of the
termination shock and heliopause conflicts with the Solar System room's
rule that a body's shells live in its own room.

## 1. What prompted it

Build B (Opus, Oct 25) proposed drawing the Sun's far shells with
Voyager's path, found it broke the room rule, and parked it for a
design talk. Tony, in this talk: "The difference is that the objects
list in the orrery is basically flat. We can combine any object and
feature. In the website the room structure is not flat. Thoughts?"

Then: "What's new here is the curatorial element. Up to now it's all
general rules for all rooms. Specific curatorial decisions by room is a
new approach. Perhaps this could be part of gallery editor." His two
examples, in his words:
1. "solar system room, spacecraft, voyager 1 room: object + sun, earth,
   mars, Jupiter, Saturn, Uranus, Neptune, Pluto."
2. "sun room, major planets + Pluto, voyager 1 and 2 room: earth, mars,
   Jupiter, Saturn, Uranus, Pluto, f corona, Alfven surface,
   termination shock, heliopause."

## 2. The principle

The orrery is flat because its user is its author: Tony composes any
objects and features at one scale and judges them on a desktop. The
website is not flat because its user is a visitor on a phone, who
cannot compose from two hundred checkboxes. Rooms are the curation.
So the orrery is the composer's instrument and the website is the
gallery of compositions; the question is which composition a feature
belongs to, not which body owns it.

Two layers, kept distinct:
- GENERAL RULES, as now, for every room: how a drawer orders itself,
  how a view frames, what a hover may say, where a drawing starts and
  stops. These stay method, in the skills.
- COMPOSITIONS, new: what is drawn together and why, chosen by the
  author, room by room. These are curation, Tony's, and are data.

## 3. Tony's rulings, Oct 25

**C1. The shape.** Put to Tony and confirmed ("Yes"): a composition is a
named selection from what its host room can draw, authored in the
editor, served as data, with its own address.

**C2. An interpretation.** Tony: "and a way to explain what it shows,
an interpretation. Maybe in the info panel." Each composition carries
words that say what the view shows and why it matters, in the i panel,
beside the sources that back it.

**C3. A spacecraft is a story.** Tony: "spacecraft are not just missions
they are stories, why there were made, what they find, etc. they weave
together the astronomy and the human exploration. And yes we can source
that story from nasa, esa, etc." So a composition built around a
spacecraft tells why it was sent, what it found, and what its path
crossed, with the astronomy and the exploration in one account; and
the story is sourced, not recalled. The provenance rules already in
force cover it: a claim about what a mission found is a factual claim,
cited to the agency's page; an agency summary that names no source is a
lead, read one layer down (Tony's ruling of Oct 21); any number in the
story is a served number; and a claim that cannot be sourced is left
out with the gap noted, never written from memory. This is the
protocol's Scientific Storytelling principle given a place to live on
the website.

## 4. What follows from the rulings (Claude's reading, for the design talk)

- **Data, not code.** A composition is a served list: its host room,
  the keys it ticks (bodies, shells, paths), the frame it opens on, a
  title, and the interpretation. It is read the way the arrival block
  is read today. No room is built in code for it.
- **The editor writes it.** The exhibit store editor (the form that
  edits the served words through store_writer, under its allow list)
  gains a section for compositions: pick the host room, tick from its
  drawable set, set the opening frame, write the words. The same
  checks that guard the served words guard these: the Typed facts and
  Typed numbers checks on the interpretation, the source list in the
  i panel, and a cache check that a composition names only keys the
  cache serves, failing by name when it does not.
- **A composition picks only from what its host room can draw.** This
  is where the work is. Example 1 costs almost nothing: the Solar
  System room draws every item in it once slice 2 is live. Example 2
  needs the Sun room to draw planets and paths, which today only the
  Solar System room does. The renderers exist; the growth is wiring,
  and it is a build. Start with example 1.
- **Words.** "Room" stays the code-level thing with its renderers and
  drawer (Sun, Earth, Solar System). A composition gets its own noun
  ("view" or "scene": Tony's choice) and its own address, so a gallery
  card can open it as a card opens a room now.
- **The room rule is restated, not broken.** "A body's shells live in
  its own room" becomes: the general rules say how a thing is drawn;
  a composition says what is drawn together. A shell may be listed in
  more than one composition; the drawing is stored once and every
  composition reads the same served rows, so there is no double
  maintenance.
- **L-486 is largely answered.** A composition is a carried view that
  the author composed once, on purpose, instead of one a visitor
  assembles at the wrong scale.
- **L-483 (the comet room) becomes the second composition**, hosted in
  the Solar System room once it draws the comet and its pieces, rather
  than a room of its own.
- **Voyager at the heliopause** (the build B finding) becomes the first
  composition that needs the Sun's far shells in the Solar System room,
  or the planets and paths in the Sun room: which host is Tony's
  curatorial call, with the gap list in hand.

## 5. Sequence

After slice 2. Discovery first (The Braid): one list of what each room
can draw today against what the first few compositions need, so the
gap is countable before anything is built. Then the editor's section
and the served shape, with example 1 as the first composition. Then the
Sun room's growth, if example 2 still wants it.

## 6. Tony-action rollup

- **(do)** Commit this record with your next push; the next records
  patch opens the item from it.
- **(decide)** The noun: "view", "scene", or another word.
- **(decide)** The first composition to build, example 1 recommended.

Written October 25, 2026 with Anthropic's Claude Fable 5.1.
