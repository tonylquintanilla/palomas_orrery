# Design -- The Solar System room as the gallery's front door

**Built on orrery `d4fdf78d2184368f3534b2464d34c86b31fac29b` at
https://github.com/tonylquintanilla/palomas_orrery and gallery
`63e657f7776f7d9b757845e4e0c3df23e3381f0b` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.** Both
read on 2026-09-29 from a fresh shallow clone of each `main`. The
handoff this follows (`HANDOFF_L363_...`, dated 2026-09-28) names gallery
`a484172f` as its head and says patch 6 was not yet run; the gallery has
moved since, and this session did not check whether patch 6 landed.
This session wrote nothing to either repository.

**Type: DESIGN SESSION (zero code).** A planning conversation with Tony.

**Companion to** the L-363 handoff (Half 2 of the room). This document
changes what Half 2 is: see section 8.

**Rules read this session:** interactive-exhibit 1.5 and
ledger-and-session-records 1.11, both matching the protocol's manifest.
The master plan was read at v33 (its head on `main`); the v34 restamp
that D20 will bring is not in it yet.

Written for Tony, who is not a programmer, and for the session that
builds from it. Plain speech throughout. Where a word is a project word,
it is explained the first time.

---

## 1. The idea in one paragraph

Today a visitor finds the gallery through a taxonomy of cards: doors,
rooms, cards. Tony's idea is to add a second way in that is more
intuitive: the solar system itself. The interactive Solar System room
becomes the front door. A visitor sees the Sun and Earth, opens a
drawer listing the planets, taps a row, and reaches that body's room
and cards. The taxonomy stays as the complete index; nothing is
removed. The room is an entry point for everything that belongs to a
body that JPL Horizons (the Jet Propulsion Laboratory's service for
where solar system bodies are) can place.

## 2. What was read, and what it showed

Read at the anchors above:

- **Shells are per-body.** In `data/objects_config.json` an object has
  features, and each feature holds named shells sized from the body's own
  radius. The Sun serves 18 shells, Earth 14 plus the two radiation
  belts. Each room's `arrival` block names which shells are drawn when it
  opens (Sun: `photosphere`; Earth: `crust`, Moon unticked).
- **Jupiter and Saturn have features but no arrival block.** The other
  entries (Moon, Io, Titan, Pluto, Charon, Apophis, Voyager 1, Encke,
  Halley) have no features.
- **No entry represents a group.** Every entry is one object with one
  centre. A group such as the main belt or the Jupiter Trojans has no
  single centre. Nothing in the config carries one today.
- **The Oort cloud is the model for a cloud.** Each Oort shape is served
  as a shape type (torus, clump field, tide field) plus sourced radii
  (value, unit, source) plus a `drawing` block declared as drawing
  choices, not measurements. The points are never stored: the browser
  generates them from a fixed seed, and the hover says the clumping is
  illustrative.
- **Ticking already reframes.** In `sunApplyVisibility`, every tick and
  every untick sets the frame to the outermost shell still shown, then
  frames it. It is not only the first tick.
- **Home today** (`navHome`) returns the camera to the default isometric
  angle, restores the range measured once when the room loaded, focuses
  the outermost shown shell and closes the drawer.
- **The rooms already fit 1.1 times the largest thing drawn.** The 10%
  margin needs no new setting.
- **The default room is set by one fallback.** `interactive.html` uses
  `solar-system-explorer` when no `?exhibit=` is given. The Explorer's
  card (`solar_system_explorer`, featured, in the `solar_system` door)
  has the bare live link `interactive.html`. The README also links the
  bare address. Every other room link already carries its key.
- **The master plan** already lists presets for encounters, comet
  perihelion and close approaches under the gallery page (Section 4a),
  and orders the planets' own rooms as Sun, Earth, then Jupiter and
  Saturn, leaving bodies after Saturn unordered.

Not read: how the orrery defines its group shells; how the cache holds
spacecraft; how far the assembler's dates reach. See section 6.

## 3. Settled: the room and its drawer

1. **What the room draws.** The room's scene is a clean orrery: symbols
   on orbits, hover text as today, no badges or rings. Everything about
   doors lives in the drawer.
2. **Opening.** The room opens with only the Sun and Earth drawn, the
   drawer closed, and Earth's row highlighted, so the drawer's handle
   reads "Earth". The view fits 1.1 times where Earth is. The aim is to
   arouse curiosity, not to show the whole system at once.
3. **The drawer.** Opening it shows ten rows: the Sun, Mercury, Venus,
   Earth, Mars, Jupiter, Saturn, Uranus, Neptune and Pluto. The nine
   non-Sun rows are always visible as the backbone. A "See more" button
   adds the groups back in place along the spine, in the order below.
   Any ticked row stays visible however the list is collapsed, so the
   drawer never hides something the scene shows.
4. **The full spine, outward from the Sun** (Tony's outline, with
   Uranus added and the stars, exoplanets and galactic center removed):
   Sun; comets (by apparition); Mercury; Venus; Earth system;
   space missions (by launch date); earth science; near-Earth
   asteroids; Mars system; main asteroid belt; Jupiter system; Trojan
   asteroids; Saturn system; asteroids; Uranus; Neptune system; Pluto
   system; trans-Neptunian objects. The exact position of "asteroids"
   and of each system row is to be confirmed at build time.
5. **Selecting and ticking are different acts.**
   - Tapping a body in the scene opens its hover text, as today, and
     highlights its drawer row. Nothing is drawn or removed.
   - The drawer's closed handle shows the highlighted body's name.
   - Tapping a highlighted row expands it: an "Enter the ... room"
     button, then any card titles. A body with nothing behind it says
     "No room or cards yet."
   - Ticking a row draws it and reframes the view. Everything ticks
     except the Sun, which is the fixed centre of the scene. The Sun's
     row still highlights, and its box offers "Enter the Sun room".
   - Ticking may open the row at the same time. This was assumed, not
     ruled; see section 6.
6. **Availability shows in the drawer.** A row shows small icons for
   "has a room" and "has cards". A row with no icons has nothing behind
   it. The list of what each body holds should be read from the exhibits
   and card metadata, so a new room or card lights up its row and
   nothing is kept in two places.
7. **Each thing has one address.** A row's link points at the same room
   or card the taxonomy points at, never a copy.

## 4. Settled: framing, zoom and Home

1. **Frame rule.** Ticking a row frames where that object is today
   (or a cloud's outer edge) times 1.1, the rooms' existing margin.
   Zoom is then free and nothing the frame chose limits it. A visitor
   can tick Sedna, see it at its current distance, and zoom out to see
   its whole orbit while everything else shrinks to dots.
2. **The frame is the largest extent among the ticked rows**, not the
   row's place in the list. A comet sits early in the list but its
   orbit is large; an eccentric object is framed at where it is now, not
   at its whole orbit.
3. **Home** returns to the current unzoomed isometric view of the last
   ticked object that is still ticked, at the default camera angle, with
   the drawer closed and that object's row highlighted. If that object is
   unticked, Home falls back to the one ticked before it. If everything
   is unticked, Home ticks Earth again and shows the opening Earth view.
   This is the one time Home changes what is drawn.
4. **Home and encounters.** If the last thing ticked is an encounter,
   Home returns to that encounter's opening view and stays at the flyby
   date. It never returns the room to now (section 5).

## 5. Settled: groups, rooms and encounters

### Scope

Only objects that JPL Horizons can place, and the shells and groups of
such objects, are in. Stars, exoplanets and the galactic center are out;
they stay reachable through their own doors in the gallery. "Earth
science" cards stay, listed under Earth's row, because they are linked to
Earth.

### Groups are rooms

- A group is a room like the Sun and Earth rooms, with its own view,
  drawer, hover text and info card, but a heliocentric scene.
- The room and the solar system drawer draw the same cloud from the same
  served data; the cloud is served once.
- **Jupiter Trojans** (the settled example):
  - In the solar system drawer: one row, "Jupiter Trojans". Ticking it
    draws both lobes in place, anchored to Jupiter's position.
  - In the Trojans room: opens on both lobes with the Jupiter symbol as
    anchor. Its drawer has two rows, a Greek camp and a Trojan camp,
    each with its own hover text and info card, and the notables listed
    under their own camp, unticked but available. As far as Tony and
    Claude know, the Greek camp leads Jupiter and the Trojan camp trails
    it. That must be checked against a source before it is served.
  - Notables appear only in the group room, never under the group row in
    the solar system drawer. The row's box says how many the room holds.
  - Which camp a body belongs to is sourced per body, not read from its
    name.
- **Clouds are shells.** They behave like the Sun room's shells: served
  with a key, off when the room opens, ticked by the visitor, translucent
  in the scene. Ticking stacks (Mars plus the belt plus Jupiter; Jupiter
  plus the Trojans).
- **A cloud is a portrait, not data.** Its points are generated from a
  seed, its hover says its proportions are approximate, and its extents
  are sourced or left out.

### Encounters

An encounter is a dated event, drawn at its date instead of now. It is
the first departure from "now".

- **One record, two listings.** An encounter is listed in the room of
  each body involved. The Psyche room lists three encounters (Mars,
  Phobos, the asteroid Psyche); the Mars room lists one; Apophis and
  Earth each list the same close approach; Voyager 1 lists Jupiter and
  Saturn. Either row opens the same view.
- **The target body's room centres the view.** No alternate centres for
  now. The Artemis II lunar flyby is listed in the Moon's room, centred
  on the Moon. The Earth room holds only the Earth-centred parts of the
  mission.
- **Ticking an encounter moves the whole room to the flyby date.**
  Everything drawn is at that one moment. The date line under the title
  shows the flyby date, so it says what the scene shows. Unticking
  returns the room to now.
- **Encounters do not stack.** Two would be at different dates, so
  ticking a second replaces the first. In the drawer they behave as a
  choice among options.
- **Each encounter carries its own opening view**: the date, the
  centring body, the range and the camera angle. The arrival block is
  the model.
- **Comets:** each apparition is a room, and its perihelion is the
  encounter that room opens on. Perihelia live only in the apparition
  room, since the Sun is the second body every time. The Sun room gets
  one row, "Comets at perihelion", which opens the comets group and its
  list by date.
- **Space missions** have their own drawer, listed by date (launch date,
  as the orrery orders spacecraft; to be confirmed).
- An encounter row can only exist where its target has a room. Where it
  has none yet, the encounter is reachable only from the Space missions
  drawer, and the row says "No room yet".

## 6. Open questions

Each is marked with who is likely to decide it. "Skill" means it is a
question of method that a skill should absorb; per the protocol, bring
Tony only what a skill cannot settle.

**A. Data layout**
1. Where does "Sun and Earth" get served? The room has no entry in
   `data/objects_config.json`; its choices live in the page's code. The
   arrival block is the model, and adding a room-level entry is likely
   method. Check interactive-exhibit 1.5 first. (Skill)
2. How does the orrery store its group shells (main belt, Trojans,
   notables)? Not read this session. It decides how a cloud is served.
   (Read first)
3. The list itself (spine order, groups, "See more") should be served
   data, not page code, or every new group means editing
   `interactive.html`. What shape? (Design, then skill)

**B. Groups and clouds**
4. How the main asteroid belt, near-Earth asteroids, and
   trans-Neptunian objects are drawn as clouds: shape, extents, sources.
   (Design round each; the Trojans set the pattern)
5. Sources for the Greek and Trojan camp assignment and the lobes'
   extent. Do not serve a number from memory. (Provenance skill)
6. Patroclus and Menoetius are a binary and sit on top of each other at
   this scale: one row for the pair, or two rows that say they overlap?
   (Tony)
7. On a phone with many bodies ticked, a tap may pick the wrong one.
   How much of this is mitigated by the drawer being the menu? (Mode 5)

**C. Positions and dates**
8. Pluto is served relative to the Pluto-Charon barycentre, and the
   assembler refuses by design to translate it into a Sun-centred
   scene. What does the row draw? (Skill: barycenter rule)
9. Each new body's own trust window must cover today, not only the
   cache's overall window (L-364: Halley's and Encke's did not). For
   encounters, the window must cover each encounter's date for every
   body in the scene, so the check is per apparition or per flyby.
   (Skill)
10. How far do the assembler's dates reach? A flyby of 1979 needs served
    positions for every body drawn at that date. The Explorer uses a
    Keplerian model; the new room uses the Horizons cache. Not read.
    (Read first)
11. How does the cache hold spacecraft? An encounter centred on a target
    body needs a record centred on it, and the assembler never
    translates between centres, so one mission may need several records.
    Not read. (Read first)
12. Zoom limits: do the + and - buttons reach hundreds of AU, and are
    orbit lines served and drawn at full length whatever the frame?
    Sedna would need a served orbit with its own trust window. (Read
    first)

**D. Interaction**
13. Ticking a row may also open it. This was assumed, not ruled. (Tony)
14. When Home falls back to the previously ticked object, the room needs
    to remember tick order. Nothing in the Sun room does that today.
    (Method)
15. How does a card say which body it is linked to? "Earth science"
    cards belong under Earth, and a card needs a field for that in the
    gallery metadata. (Skill: gallery-pipeline)
16. Order of the nine planet symbols. Only Pluto has a known blocker
    (question 8), so it goes last; the others can go in one batch and
    one cache rebuild. (Skill)

## 7. The swap

Tony's ruling, 2026-09-29: the new room becomes the default once the
nine planets are in, and it does not wait for the date picker. The
Explorer is not removed. It stays a card in the `solar_system` door, and
is reachable by going into the solar system room in the gallery, but not
from within the exhibit. The Explorer keeps a date picker (a Keplerian
model); the new room does not yet.

At the swap, in one commit:

- The Explorer's card `live` link changes from `interactive.html` to
  `interactive.html?exhibit=solar-system-explorer`.
- The page's fallback key changes from `solar-system-explorer` to
  `solar-system`.
- The README's bare `interactive.html` link is checked.
- Any existing bookmark to the bare address will now open the new room.
- The room's own card, "Solar System", already links
  `interactive.html?exhibit=solar-system`.

Other cards (for example the orbital construction card) stay in the
taxonomy and are not in this exhibit's drawer.

## 8. What this changes for Half 2 and the master plan

- **Half 2 of L-363 was "the other six planets".** It is now the room's
  drawer and rows as well: the nine symbols, the ten-row drawer with
  tick boxes, the Home rule and the opening view. Groups, comets,
  missions and encounters are later design rounds.
- **The handoff said comets (L-364), Voyager 1 (L-365) and the orbit
  info cross (L-366) are not Half 2.** They are still not Half 2, but
  this design makes comets and Voyager 1 part of the room's future, so
  those rows should say so.
- **Start conditions do not change.** Half 2 waits for L-322 Stage D.
  Confirm D20 has landed and the loaded skills read
  interactive-exhibit 1.5 and provenance-discipline 2.22 before any
  exhibit or provenance work.
- **Buildable soon:** the nine symbols, the ten-row drawer with ticks,
  the highlight and handle behaviour, the Home rule, the opening on Sun
  and Earth, and the swap. **Needs its own round:** every group,
  comets, missions, encounters, and the date reach.
- **A date picker and animation are long-term goals.** Nothing above
  should make them harder: membership never depends on the date, a
  row's facts are the same whatever it is, and the encounter mechanism
  already teaches the room to draw a moment other than now.
- The master plan restamps once per design build (L-296). Whether this
  document is a design build in that sense is for Tony.

## 9. For the ledger, and Tony-actions

**Ledger, one update to L-363 and no new class:** add this design, the
rulings in sections 3 to 5 and the swap in section 7; its Gap becomes
sections 6 and 8. File one item per class for the open questions
that are not L-363's: cloud shapes for the three remaining groups;
served-list layout; encounter data (dates, spacecraft records, target
centring); and cards linked to a body.

**Tony-actions:**

- (do) File this document in the orrery's `documentation/`.
- (do) Confirm whether patch 6 (the camera and site credit) landed; this
  session did not check.
- (decide) Patroclus and Menoetius: one row or two (question 6).
- (decide) Whether ticking also opens the row (question 13).
- (decide) Whether this counts as a design build for the master plan's
  restamp (section 8).
- (later) Mode 5 on his phone for the drawer, upright and sideways, with
  every visitor-facing word listed first.

---

Session written September 2026 with Anthropic's Claude Sonnet 5.5.
