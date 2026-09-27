# Handoff -- Symbols-only Solar System room, Half 1 (runs beside Stage D) -- rev 2

**Built on orrery `de4eadc58e3de746183515dff422aaab3943fe6a`
at https://github.com/tonylquintanilla/palomas_orrery
and gallery `42a17abe16eebe5f03c790ad2a8f39f918c1ba7b`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io.**
Both HEADs were read live with `git ls-remote` on 2026-09-26. The build
chat reads both again before it starts, and again before it hands Tony a
patch, because Stage D is being built in another chat at the same time.

**Re-anchored for rev 2 on 2026-09-26:** orrery
`907436a80ebf1c6d4b0dbcc0fc7da2ceed721ed6` and gallery
`a5c35f5fcde47b3648040a5aec8724d58416d2d4`, both read live. Between the
rev 1 anchors and these, Stage D shipped gallery patch 3 and orrery D13,
and two other lines of work (L-286, rooms in levels, and L-289, the grid
numbers) edited `interactive.html`. Rev 1 was filed unchanged in
`documentation/` at `907436a8`; this revision replaces it. What changed
is listed in section 8.

**Type:** BUILD, preceded by a short design round with Tony (section 4).
**Supersedes:** nothing.
**Companion:** `documentation/HANDOFF_L322_D_gallery_patch3_done_20260926.md`,
Stage D's latest handoff. What remains of Stage D is section 6 of
`documentation/BUILD_MANIFEST_L322_D_earth_pole_20260922.md` (rev 3): how
exact rows print. This chat must not touch the files that work edits
(section 3).

**Rules this work runs under.** Inside Tony's Project the protocol (v3.68)
and the skills load on their own. This task fires interactive-exhibit
1.4, gallery-assembler 1.3, orrery-coding-conventions 1.9,
safe-file-editing 1.11 and ledger-and-session-records 1.11. If the build
edits any Python file in the assembler package, agentic-pre-test 1.2
fires too. Check each loaded version against the Skill Manifest in
`PROJECT_INSTRUCTIONS.md` (Stale Skill = Stop). In the first reply, state
which of these skill files were actually read.

## 1. What Tony decided on 2026-09-26

- **Rebuild the Solar System Explorer as a symbols-only room on the
  assembler.** Bodies are drawn as their symbols with their orbits. No
  shells, rings or belts. This is how the orrery itself grew: the object
  symbols came first and the shells came later.
- **Why it is worth doing.** The current Explorer is the default room of
  `interactive.html`. It draws orbits from mean elements copied out of
  `orbital_elements.py` (the `PLANET DATA` block near line 954), and some
  of those are old; the master plan's Section 3a names Saturn's epoch as
  2003 and Pluto's as 1989. The new room reads the nightly cache, which
  fetches from Horizons every night, so positions need no sourcing work.
  It also becomes the top level of L-286 (rooms in four levels), where
  tapping a planet opens that planet's room, and it retires the
  Explorer's separate JavaScript drawing path.
- **Split in two halves, because of Stage D.** Stage D's remaining work,
  manifest section 6, has the mirror write a print count into
  `data/objects_config.json` and then rebuild the cache. Adding planets
  needs the same config file and a rebuild, so that part waits.
  - **Half 1 (this chat, now):** a new room in `interactive.html` under
    its own `?exhibit=` key, drawing only what the cache already serves.
  - **Half 2 (after Stage D's section 6 pushes):** add Mercury, Venus,
    Mars, Uranus and Neptune to `data/objects_config.json`, rebuild the
    cache once, then Tony's Mode 5 on the phone.
    Only after that does the new room become the default.
- **The old Explorer stays the default throughout Half 1.** Visitors see
  no change until Tony accepts the new room.

Raised in the same conversation and NOT ruled: whether Jupiter's and
Saturn's rooms could also ship symbols-first (planet and moons, no rings
or belts), with the rings and belts as a second delivery. Do not act on
it.

## 2. What the cache serves today (read at gallery `42a17abe`; the
nightly runs since then changed no object list)

`data/solar-system/coverage_index.json` lists 13 objects: sun, earth,
jupiter, saturn, moon, io, titan, pluto, charon, apophis, voyager_1,
encke, halley. In `data/objects_config.json` only sun, earth, jupiter and
saturn carry features. Missing planets: Mercury, Venus, Mars, Uranus,
Neptune (Half 2).

## 3. Boundaries for Half 1

Do NOT edit any of these. They belong to Stage D's section 6 or to
Half 2:
- `data/objects_config.json` (section 6's mirror writes print counts
  into it; Half 2 adds the five planets)
- `gallery/feature_renderers.js` (section 6 changes `fmtServed`, which
  prints the served numbers)
- `constants_new.py`, `tools/mirror_constants.py`, and the orrery's
  hover f-strings (section 6)
- anything under `data/solar-system/` (the cache build writes it)
- `tools/gallery_cache_builder.py` and `gallery/earth_geometry.js`
  (Stage D's earlier patches; nothing in Half 1 needs them)
- anything in the orrery repo other than a ledger entry and this
  chat's own handoff

Stage D's latest handoff says section 6 should not need
`interactive.html`. **But `interactive.html` is not quiet.** On
2026-09-26 the L-289 grid-number patches edited it three times, and
L-286's chain patch put "Paloma's Orrery | Solar : Earth" in every
room's top bar. Re-read the gallery HEAD before building and before
handing Tony a patch; if `interactive.html` moved, rebuild the patch on
the new HEAD.

Do NOT change the default room. `?exhibit=` with no value, or
`solar-system-explorer`, must still load the old Explorer.

## 4. Questions to settle with Tony before building, one at a time

The protocol says to iterate open design in conversation before
building. These are open:
1. **The room's key and title.** For example `?exhibit=solar-system`.
2. **Which served objects appear.** At a scale that holds Saturn's
   orbit, the Moon, Io, Titan and Charon sit on top of their planets.
   Tony decides whether they are in the drawer, drawn, or left out.
3. **Date.** Today only, or a date control. If a date control, it must
   stay inside the cache's served window (gallery-assembler covers the
   window gating).
4. **How the shells are kept out.** The assembler returns features for
   the four bodies that have them. Whether the room's `compose` drops
   them, or an arrival block draws none of them, is method: settle it
   from interactive-exhibit (the arrival block section) and bring Tony
   only a case the skill does not cover.

## 5. Where it fits in the code (read at gallery `a5c35f5f`)

Line numbers moved by about 25 since rev 1 and will move again; find
each by its name.

- `interactive.html` line 1790, `const EXHIBITS`: one row per room with
  title, sceneTitle, pngName, halfRangeAu, driver, infoHtml, compose. A
  new room adds one row (interactive-exhibit, the anatomy table).
- `SUN_DRIVER` (line 1566) and `EARTH_DRIVER` (line 1644) are the
  templates. The Sun's calls `assemble_scene` with
  `"objects": ["sun"]` and `"center": "sun"`; a symbols-only room lists
  its objects there.
- **The grid numbers (L-289, new since rev 1).** `axisTickFont()` (line
  2308) sets 12 px in #9a9a9a, and every axis number ends in " AU" and
  is written out in full, on the Explorer's layout (line 1473) and the
  shared room layout (line 2190). A new room built through the shared
  room layout inherits both; confirm that rather than copy the settings.
- **The top-bar chain (L-286, new since rev 1).** The top bar reads the
  chain, such as "Solar : Earth", from the gallery card whose live link
  opens the room, and from `gallery_config.json`. The new room has no
  card yet. Check what its top bar shows with no card, and tell Tony
  before Mode 5; a card for it is Half 2's business, after Tony accepts
  the room.
- Marker symbols and hover text follow orrery-coding-conventions (the
  marker symbol taxonomy and the AU convention in hover text) so the
  legend reads the same as the orrery's.

## 6. Ledger

This room has no handle. Stage D's latest handoff gives L-363 as the
next free handle at orrery `62e93856`, and Stage D may take handles
first. The build chat re-reads the ledger index at its base, proposes
the next free handle to Tony, and cross-references L-286 (the
Explorer is eventually replaced as the braid reaches the planets) and
L-099 (the Phase 0 Explorer). Do not mint it without Tony's go-ahead.

## 7. Pushes

Two chats are building at once and Tony integrates both. Pushes go one
at a time. Before handing Tony a patch, re-read the gallery HEAD; if it
moved, rebuild the patch on the new HEAD rather than asking Tony to
apply it over a changed file.

## 8. What changed in rev 2

- New anchors (top of file).
- Stage D is down to manifest section 6. Half 2 now waits on section 6's
  push. The boundary list names section 6's files.
- `interactive.html` has other active work (L-286 and L-289), so it is
  the file to re-read before patching.
- The new room should inherit the L-289 grid numbers and must be checked
  against the L-286 top-bar chain.
- Line numbers updated; the handle hint is L-363.

Unchanged: Tony's rulings of 2026-09-26, the four open questions, and
the rule that the old Explorer stays the default.

---
Written September 2026 with Anthropic's Claude Opus 5.5.
