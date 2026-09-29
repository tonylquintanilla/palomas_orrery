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

===================================================================

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/patch_L363_5_short_scene_titles_20260927.py
  ok  interactive.html: the page's Updated stamp
  ok  interactive.html: the Sun room's title: 'The Sun'
  ok  interactive.html: the Earth room's title: 'Earth'
  ok  interactive.html: the Solar System room's title: 'The Solar System'
  ok  interactive.html: the title may centre between the zoom buttons and the cross
  ok  interactive.html: the fit tries the gap before moving below
  ok  interactive.html is the file that was tested, and ASCII
  wrote interactive.html (177332 bytes)

patch applied to 1 file

Stamps updated: the 'Updated' line at the top of interactive.html.

WHAT TO DO NEXT, in this order:

  1. Move THIS script into the GALLERY's documentation/ folder.
  2. Run the gallery maintenance run:
         python gallery_maintenance_run.py
     Expect 17 of 17, as before.

======================================================================
  gallery maintenance run -- OFFLINE (before a commit)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

GENERATORS -- rewritten every time; a no-op when nothing moved
  PASS Module atlas              0.9s  rewrote MODULE_ATLAS.md,
                                    MODULE_INDEX.md
  PASS Constants export pull     0.7s  rewrote data/constants_export.sha
  PASS Config mirror             0.1s  no change to
                                    data/objects_config.json

CHECKERS -- the verdict informs the push call
  PASS Cache builder suite       9.8s  PASS (210 checks, 0 failures)
  PASS Pole of date              0.2s  POLE OF DATE: all 11 checks passed
                                    (frame angle, orrery, ERFA, block
                                    checker, and each shown able to
                                    fail).
  PASS Mirror suite              0.1s  All 64 mirror checks passed:
                                    served, spelling, relabel refused
                                    and accepted, conflict refused,
                                    definition as exactly 1, fallback
                                    and absent named, no-slot refused,
                                    five shapes, formatting kept,
                                    idempotent, report writes nothing,
                                    uncertainty written as served,
                                    Earth's pole served, print count
                                    written as served, "in" written as
                                    served and a slot served in
                                    another unit from it.
  PASS Store writer suite        3.9s  All 251 store-writer checks
                                    passed: an allow list that lets
                                    through only a shell's words, a
                                    belt's words and the arrival
                                    settings; a no-edit round trip;
                                    one line per change; empty words
                                    handled; a refused batch writing
                                    nothing; awkward text; and the
                                    shell list matching the cache
                                    check's rule.
  PASS Store editor suite        0.1s  All 252 store-editor checks
                                    passed: every box the form offers
                                    is one the writer allows; the word
                                    list and the tick list differ by
                                    the belts, on purpose; nothing
                                    typed saves nothing; the save
                                    message does not promise a visitor
                                    sees what they cannot yet; and a
                                    red Cache in step is explained
                                    rather than just shown.
  PASS Config mirror check       0.1s  Every served link holds the
                                    export's value, unit and figure
                                    count; 65 link(s) compared, store
                                    eacb85b01d2c.
  PASS Pointer join              0.1s  Every link is accounted for: 89
                                    link(s) against orrery 2a7d26b9,
                                    20 fallback named; read check: 43
                                    of 43 measured rows reached carry
                                    a read.
  PASS Cache in step             0.1s  The served cache holds the
                                    config's features exactly: 4
                                    object(s), 35 named shell(s), in
                                    both cache files.
  PASS Feature renderers         0.1s  === ALL CHECKS PASSED ===
  PASS Page framing              0.1s  === ALL CHECKS PASSED ===
  PASS Sun shells                0.1s  ALL CHECKS PASSED
  PASS Earth scene geometry      0.1s  === ALL CHECKS PASSED ===
  PASS Hover budget              0.1s  === ALL CHECKS PASSED ===
  PASS Arrival                   0.2s  Arrival: both rooms open on the
                                    right things; every shell trace
                                    carries its key; the fallback with
                                    no arrival block is unchanged.
  PASS Display figures           0.2s  === PASS: 57 hover(s) and 296
                                    number(s) examined; 13 graded, 7
                                    graded by line, 44 held to the
                                    fixture ===
  PASS Guest book                0.1s  === GUEST BOOK: all 8 checks
                                    passed
  PASS Guest book updater        0.2s  === GUEST BOOK UPDATER: all 43
                                    checks passed (6 scripted runs,
                                    self-test first)
  PASS Daily run steps           0.1s  === DAILY RUN: all 3 step scripts
                                    found
  PASS Artifact 1 assembler      0.1s  === ALL CHECKS PASSED -- 5
                                    verdicts and T3's feature set
                                    match the 2026-08-31 pin ===
  PASS Cache siblings            0.1s  RESULT: no sibling directories and
                                    nothing in data/ the builder did
                                    not make.

======================================================================
  19 of 19 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Cache siblings         RESULT: no sibling directories and
  last swap 2026-09-29T03:22:10.391361+00:00: succeeded first time
======================================================================

  After you push: python gallery_maintenance_run.py --live

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  3. Commit and push. Then: python gallery_maintenance_run.py --live

======================================================================
  gallery maintenance run -- LIVE (after a push)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

LIVE -- what the deployed site actually serves

  fetching 13 files from https://palomasorrery.com/
    SERVED   interactive.html                               matches the working copy
    SERVED   gallery/feature_renderers.js                   matches the working copy
    SERVED   gallery/earth_geometry.js                      matches the working copy
    SERVED   gallery/assembler/resolver.py                  matches the working copy
    SERVED   gallery/assembler/__init__.py                  matches the working copy
    SERVED   data/solar-system/coverage_index.json          matches (the working copy is CRLF)
    SERVED   data/solar-system/feature_configs.json         matches (the working copy is CRLF)
    SERVED   data/solar-system/positions/voyager_1.json     matches the working copy
    SERVED   gallery/arrival.js                             matches the working copy
    SERVED   gallery/nav_cluster.js                         matches the working copy
    SERVED   data/objects_config.json                       matches the working copy
    SERVED   gallery/guestbook.js                           matches the working copy
    SERVED   data/guestbook.json                            matches the working copy

  PASS Served reachability       2.0s  all 13 files served and
                                    byte-identical to the working copy

  orrery export pinned at 2a7d26b9

  PASS Export freshness          0.2s  the served export is the orrery's
                                    at 2a7d26b9, byte for byte

  orrery HEAD 2a7d26b9
  examining 24 of 89 links; the other 65 are served from the export
    NOT IN STORE  create_sun_galactic_tide default not a top-level constant in the store
                  /objects/0/features/oort_cloud/galactic_tide/typical_radius
    NOT IN STORE  planet_poles['Sun']              not a top-level constant in the store
                  /objects/0/features/orientation
    NOT IN STORE  planet_poles['Jupiter']          not a top-level constant in the store
                  /objects/2/features/orientation/pole
    NOT IN STORE  planet_poles['Saturn']           not a top-level constant in the store
                  /objects/3/features/orientation/pole
  24 pointers: 20 match, 0 DRIFT, 0 UNIT MISMATCH, 4 could not be examined.

  PASS Store drift               0.8s  24 pointers against orrery
                                    2a7d26b9 -- 20 match, 0 DRIFT, 0
                                    UNIT MISMATCH, 4 could not be
                                    examined.

======================================================================
  2 of 2 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Store drift            24 pointers against orrery 2a7d26b9 --
  last swap 2026-09-29T03:22:10.391361+00:00: succeeded first time
======================================================================

  Offline pass: python gallery_maintenance_run.py

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  4. After about ten minutes, on your phone, upright, open all three
     rooms: the Sun, Earth, and the Solar System. For each, note
     whether the title and its line sit at the top or below the
     arrow buttons. -- all correct. 
  5. Tell Claude the new gallery SHA and what you saw. -- a484172fc17ec73ed801fbeab8eae2ebf0c945e1

TONY-ACTION ROLLUP for this patch:
  (do)     steps 1 to 5 above.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> 

