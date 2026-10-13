<!-- Doc-Kind: hand | Brief for the DESIGN session that scopes how the rest of the orrery's objects come to the website as plotted positions (stage 11 of the road). Tony, 2026-10-13: "I am anxious to add the symbols to the gallery too so visitors can at least plot positions." Design before code: the session measures, proposes the slices and the mechanism, and builds the first slice only after Tony's word. -->
# Brief: the orrery's objects come to the website (L-438, stage 11)

Built on orrery 28e1b7d1 at
https://github.com/tonylquintanilla/palomas_orrery and gallery
924977a3 at https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Pin each at HEAD when the session starts; this work touches both.
Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`;
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.
Written October 13, 2026 with Anthropic's Claude Fable 5.1, in the
coordination session of October 12 and 13.

- Type: DESIGN SESSION brief (zero code until Tony's word), then the
  first slice's build in the same session if the design settles.
- Ledger: opens L-438 at the session's close. Stage 11 on the road:
  "The rest of the orrery's objects come to the website." Tony's note
  of 2026-10-10 on L-433: "then add the symbols for most if not all
  the orrery's objects list."
- Order: after L-431 build 3 (the period on the website), which
  settles what every served object carries. This session can be
  briefed now and started once build 3 is pushed.

## 0. Before building

- Pull both repositories at HEAD and pin each SHA.
- Skills this task fires: gallery-cache-builder (the nightly builder
  fetches each served object; objects_config; the serving cache),
  interactive-exhibit (the Solar System room's drawer, what a body's
  row carries, the words-and-link contract), gallery-assembler (how a
  position is propagated and what the served window allows),
  horizons-orbital-mechanics (ids, record pinning, a comet's record
  number), provenance-discipline (a served description's numbers are
  sourced or come out; the gate binds at export), ledger-and-session-
  records. Confirm each against the manifest at HEAD.
- Read `export_objects.py`'s rule: an orrery entry is exported when it
  carries a `'key'` equal to the website's slug, and "an entry gains a
  key when the website starts serving it, and not before."

## 1. What Tony wants, and what is there

Tony, 2026-10-13: "I am anxious to add the symbols to the gallery too
so visitors can at least plot positions." The symbol is the marker at
a body's position in the Solar System room; "plot positions" is the
room's existing job, done today for 19 served objects, 13 of them
keyed to the orrery's list.

Measured at HEAD:
- The orrery's `celestial_objects.py` holds 182 entries: 71 orbital
  (planets, dwarf planets, asteroids, comets, TNOs), 48 satellites, 39
  trajectories (spacecraft), 10 Lagrange points, 7 barycentres, 1
  hypothetical (Planet 9), 1 fixed, and 16 exoplanet-system entries
  (which are the stars' domain and out of scope here).
- The website serves 19: the Sun, 8 planets, the Moon, Io, Titan,
  Pluto's barycentre, Pluto, Charon, Apophis, Voyager 1, Encke,
  Halley. Each is a row in `data/objects_config.json` with a slug, a
  Horizons id, a centre, a frame, a trace policy, a position-accuracy
  row, a sourced description and an info link; the nightly builder
  fetches its positions and the room draws them.
- What one new object costs today: a `'key'` on its orrery entry; a
  config row written through the mirror (never by hand); a nightly
  fetch (one Horizons query per object per build, with the pause
  between); a sourced description (the gate binds at export: a number
  in a served description is sourced or comes out); a drawer row in
  the room. The room's drawer lists every served body; 19 rows fit a
  phone, and 160 do not.

## 2. The questions the design session answers (with Tony, one at a time)

1. **Which objects, in what slices.** Not all 166 at once (The Braid:
   one countable slice, then the next). Recommended first slice: the
   orrery's remaining orbital bodies a visitor would look for, the
   dwarf planets and the named asteroids and comets the orrery already
   draws, about 30; then the spacecraft; then the satellites by
   planet; the Lagrange points last or not at all. Tony chooses the
   slices and their order. A class he excludes is recorded, not
   chased.
2. **How the drawer holds more than a phone can show.** Today's drawer
   is one list. Options to bring with a mock-up: groups that fold
   (planets, dwarf planets, asteroids, comets, spacecraft, moons by
   planet), a search box, or "All / none" per group. Mode 5; Tony
   judges on the phone. The drawer's rules (Go To in the middle, the
   room button to its right, names that wrap) stand.
3. **The nightly cost.** 160 more objects is 160 more Horizons queries
   per build. Options: fetch all nightly (the builder's pause makes
   this minutes, not seconds; measure); fetch the planets nightly and
   the rest on a longer cycle; or fetch on demand. Recommended: measure
   one build with 30 added before deciding.
4. **Descriptions and links.** Each served object needs a sourced
   description and an info link, by the words-and-link contract. The
   orrery's `mission_info` text is the source for most; a number in it
   is sourced or comes out before export. This is the slow part and
   the honest one; the design session counts how many of the first
   slice's descriptions carry a number.
5. **Comets and record pinning.** A periodic comet's record number
   moves (horizons-orbital-mechanics, Checking an Entry Against JPL);
   each added comet is pinned the way Encke and Halley are.

## 3. What is settled already (no re-asking)

- The orrery is the one definition of each object; the website copies
  through the export and the mirror, never by hand (interactive-
  exhibit; L-395).
- A served value's provenance closes before it leaves the orrery (The
  Gate Binds at EXPORT).
- The Horizons check confirms each served object against JPL on its
  cycle; each added object joins that list.
- The room's drawer conventions (Go To, the room button, wrapping
  names) and Home's order.

## 4. Build notes for the first slice (once Tony has chosen it)

- Orrery patch: `'key'` fields on the chosen entries; descriptions
  checked for unsourced numbers; `export_objects.py` unchanged in
  rule. Gallery patch: the mirror carries the new rows; the config
  gains their centre, frame, trace policy and accuracy row (the
  accuracy row by the orrery's DE430 groups or "none stated" for a
  small body until its own uncertainty is fetched, L-399); the drawer
  shows them by the chosen grouping. Then the Daily Run builds the
  cache; a visitor sees the bodies on the next push after that.
- Planted faults: a keyed entry with no description; a served
  description with an unsourced number; a config row written by hand
  (the mirror check); a body drawn with no accuracy row and no "none
  stated" words.
- The look: the drawer on the phone, upright and sideways; three new
  bodies hovered; one comet's orbit drawn.
- Skills: interactive-exhibit (the drawer's grouping, if built) and
  gallery-cache-builder (the fetch cadence, if changed). One version
  each, under One Session, One Bump.

## 5. For Tony, one at a time, in the design session

- (decide) The slices and their order (question 1).
- (decide, at a mock-up) How the drawer holds them (question 2).
- (decide, after a measurement) The nightly cadence (question 3).
- (decide, recorded, not urgent) Whether Lagrange points and the
  exoplanet entries are ever served.

## 6. Tony's actions, all of them

- (do) Start this session after L-431 build 3 is pushed.
- (decide) The items in section 5.
- (do) Run the first slice's two patches and the Daily Run; look on
  the phone; push.

Brief written October 2026 with Anthropic's Claude Fable 5.1.
