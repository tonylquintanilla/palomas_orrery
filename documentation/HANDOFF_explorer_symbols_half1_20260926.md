# Handoff -- Symbols-only Solar System room, Half 1 (runs beside Stage D)

**Built on orrery `de4eadc58e3de746183515dff422aaab3943fe6a`
at https://github.com/tonylquintanilla/palomas_orrery
and gallery `42a17abe16eebe5f03c790ad2a8f39f918c1ba7b`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io.**
Both HEADs were read live with `git ls-remote` on 2026-09-26. The build
chat reads both again before it starts, and again before it hands Tony a
patch, because Stage D is being built in another chat at the same time.

**Type:** BUILD, preceded by a short design round with Tony (section 4).
**Supersedes:** nothing.
**Companion:** `documentation/BUILD_MANIFEST_L322_D_earth_pole_20260922.md`
(rev 3), the Stage D build running in parallel. This chat must not touch
the files that manifest edits (section 3).

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
- **Split in two halves, because of Stage D.** Stage D edits
  `data/objects_config.json` and `tools/gallery_cache_builder.py` and
  rebuilds the cache. Adding planets needs the same config file and a
  rebuild, so that part waits.
  - **Half 1 (this chat, now):** a new room in `interactive.html` under
    its own `?exhibit=` key, drawing only what the cache already serves.
  - **Half 2 (after Stage D pushes):** add Mercury, Venus, Mars, Uranus
    and Neptune to `data/objects_config.json`, rebuild the cache once
    with the builder Stage D changed, then Tony's Mode 5 on the phone.
    Only after that does the new room become the default.
- **The old Explorer stays the default throughout Half 1.** Visitors see
  no change until Tony accepts the new room.

Raised in the same conversation and NOT ruled: whether Jupiter's and
Saturn's rooms could also ship symbols-first (planet and moons, no rings
or belts), with the rings and belts as a second delivery. Do not act on
it.

## 2. What the cache serves today (read at gallery `42a17abe`)

`data/solar-system/coverage_index.json` lists 13 objects: sun, earth,
jupiter, saturn, moon, io, titan, pluto, charon, apophis, voyager_1,
encke, halley. In `data/objects_config.json` only sun, earth, jupiter and
saturn carry features. Missing planets: Mercury, Venus, Mars, Uranus,
Neptune (Half 2).

## 3. Boundaries for Half 1

Do NOT edit any of these. They belong to Stage D or to Half 2:
- `data/objects_config.json`
- `tools/gallery_cache_builder.py`
- anything under `data/solar-system/`
- `gallery/feature_renderers.js`
- `gallery/earth_geometry.js`
- anything in the orrery repo other than a ledger entry and this
  chat's own handoff

Stage D's manifest (rev 3) names no edit to `interactive.html`. Confirm
that against the manifest at the build chat's own base before starting.
If Stage D has pushed by then and changed `interactive.html`, build on
the new HEAD, not on `42a17abe`.

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

## 5. Where it fits in the code (read at gallery `42a17abe`)

- `interactive.html` line 1765, `const EXHIBITS`: one row per room with
  title, sceneTitle, pngName, halfRangeAu, driver, infoHtml, compose. A
  new room adds one row (interactive-exhibit, the anatomy table).
- `SUN_DRIVER` (line 1541) and `EARTH_DRIVER` (line 1619) are the
  templates. The Sun's calls `assemble_scene` with
  `"objects": ["sun"]` and `"center": "sun"`; a symbols-only room lists
  its objects there.
- Marker symbols and hover text follow orrery-coding-conventions (the
  marker symbol taxonomy and the AU convention in hover text) so the
  legend reads the same as the orrery's.

## 6. Ledger

This room has no handle. The build chat reads the ledger at its base,
proposes the next free handle to Tony, and cross-references L-286 (the
Explorer is eventually replaced as the braid reaches the planets) and
L-099 (the Phase 0 Explorer). Do not mint it without Tony's go-ahead.

## 7. Pushes

Two chats are building at once and Tony integrates both. Pushes go one
at a time. Before handing Tony a patch, re-read the gallery HEAD; if it
moved, rebuild the patch on the new HEAD rather than asking Tony to
apply it over a changed file.

---
Written September 2026 with Anthropic's Claude Opus 5.5.
