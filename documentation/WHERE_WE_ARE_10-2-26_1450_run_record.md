<!-- Doc-Kind: hand | Where the project is and where it is going, in plain words. One file, rewritten in place; read it at the end of every session. -->
# Where We Are

Last updated: October 2, 2026 -- **Tony**: see notes -- 10-2-26 14:33
- Written at orrery b3cfc780 and gallery cfc53490, plus this session's
  two patches.

> **READ THIS FIRST**
>
> **Changed this session:**
> - The Exhibit Store Editor now lists every room, the Solar System
>   room included, and can set what it opens on.
> - The Solar System room's drawer is built: See more, rows that open
>   with a way into the Sun and Earth rooms, and Home remembering what
>   you ticked. Not yet on the website. -- it is on the website
> - Your ruling: the room frames where each body is now, plus 20%,
>   not its whole orbit. You also confirmed five smaller calls I had
>   made in the build. 
> - The two skills are updated for this work, with a new rule on when
>   a skill gets a new version.
> - The last session's two skill reinstalls are confirmed.
>
> **Do next:**
> - *You check the drawer on your phone, then the desktop.* -- confirmed on phone
>
> **Needs you now:**
> - *Read the room's two new info paragraphs and say if they are right.* -- yes, as noted
> - *At your machine: two gallery patches, the editor ticks, one orrery
>   patch, then reinstall two skills and the Project's instructions.
>   Each patch prints what to do next.*

How to read the marks:
- *Italic* lines are the must-reads.
- **>> UPDATED THIS SESSION** beside a heading means that section
  changed in the latest session.
- "<< new this session" beside a road stage marks a change to the road.
- Sections without a mark are as they were.
- The marks are cleared and reset at every session's update, so they
  always mean "new since you last read this."

## The goal -- making great progress

- Paloma's Orrery on the web.
- The website does what the desktop orrery does, in the browser, from
  data fetched from JPL each night, so a visitor never waits on JPL.
- Anyone can open it, with nothing to install.
- Built from the same code and the same checked numbers as the desktop
  orrery.
- The one real limit: the browser can show only the dates the saved
  data covers.
- Within that range, a visitor will be able to choose a date, and
  perhaps play time forward.

## The road

  1. [done]   The Sun's room is live on the website.
  2. [done]   Earth's room is live, with every number traced to its source.
  3. [done]   The numbers come from one place: the orrery feeds the
              website, and nothing is typed twice.
  4. [NOW]    *The Solar System room becomes a second way in: all the
              planets, a drawer to pick them, and a way into each
              body's own room.*
  5. [next]   The Sun's numbers get the same checking Earth's got.
  6. [next]   The Solar System room's card becomes the top featured
              card in the lobby. A bare interactive.html link opens
              the Solar System room, and the Explorer gets its own
              address.
  7. [later]  The rest of the orrery's objects come to the website --
              dwarf planets, asteroids, moons -- through the same
              connection that now carries the room's eleven bodies,
              checked against JPL Horizons.
  8. [later]  Encounters: comets and spacecraft shown at the dates
              that matter.
  9. [later]  The planets get their details -- layers, rings, magnetic
              fields -- Jupiter and Saturn first.
 10. [goal]   The website does what the desktop orrery does, from data
              fetched from JPL each night, with a date to choose and
              time to play within the range the data covers.

## Right now  **>> UPDATED THIS SESSION**

- The Solar System room shows the Sun, all eight planets, Pluto and
  the asteroid Apophis, where they are when you open it.
- It opens on Earth alone until you tick more in the editor.
- The drawer's new behaviours are built and tested here, not yet on
  the website: See more, rows that open, the Sun's row that cannot be
  unticked, a tap on a body finding its row, and Home remembering. -- partially? see notes
- The room will frame where each body is now, plus 20%. Pluto's orbit
  runs past the edge until you zoom out.
- Each body's info panel shows a description and a NASA link.
- Those words and links come from the orrery's own object list. The
  website keeps copies, written by a tool, and a check fails if anyone
  edits them by hand. 
- The editor can set what any room opens on. It cannot yet change the
  words on the Solar System room's rows, such as Pluto's sentence.
- The rest of the orrery's objects are not connected yet.

## The next three steps  **>> UPDATED THIS SESSION** -- yes, thanks

1. *You check the drawer on your phone, then the desktop.*
   - Tick and untick bodies, open rows, See more, Enter the Sun room,
     tap a body in the picture, and Home.
2. Whatever your phone shows gets fixed.
3. The Sun's numbers get the same checking Earth's got.

## Waiting on you  **>> UPDATED THIS SESSION**

Now:
- *The room's two new info paragraphs: right, or reword?*
- *Gallery: run the two patches, in either order. Then open the editor,
  pick solar-system, tick Mercury, Venus and Mars, Save. Then the
  maintenance run, commit and push.*
  - Nothing needs a cache rebuild.
- *Orrery: run the skills-and-ledger patch, then the maintenance run,
  commit and push. Then reinstall interactive-exhibit and
  ledger-and-session-records in Settings > Skills, and replace the
  Project's instructions with the new PROJECT_INSTRUCTIONS.md.*

At the next design talk:
- Nothing new.

Not urgent:
- Choosing a date, and animation, your idea of October 1. -- #3
  - The range would follow only the bodies you tick.
  - Talked through once the drawer is built.
- The full check of the orrery's object list against JPL Horizons. -- #1
  - Its first run lists what disagrees; simple errors get fixed and
    listed, the rest come to you.
- Whether the editor should also edit the words on the Solar System
  room's rows, such as Pluto's sentence. -- #2
  - Today a change to them comes as a patch from a session.

## Where the details are  **>> UPDATED THIS SESSION**

- Every item, done and open: `LEDGER_CONSOLIDATED.md`
  - This session: L-404, L-405 and L-363.
- The reasoning behind the order:
  `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md`
- The latest session record: L-404 and the newest note on L-363, in the
  ledger. This session wrote no separate handoff.

===============================================================================

**Tony**: Run record: 

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/patch_L405_skills_and_ledger_20261002.py
ok  LEDGER_CONSOLIDATED.md             header stamp
ok  LEDGER_CONSOLIDATED.md             L-405 and L-404 opened
ok  LEDGER_CONSOLIDATED.md             L-363 step 3b note
ok  PROJECT_INSTRUCTIONS.md            header v3.77
ok  PROJECT_INSTRUCTIONS.md            cut from b3cfc780
ok  PROJECT_INSTRUCTIONS.md            version history: v3.77 entry
ok  PROJECT_INSTRUCTIONS.md            version history: v3.74 moved down
ok  documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1: v3.74 received
ok  skills/interactive-exhibit/SKILL.md version line 1.8 -> 1.9, with the v1.9 paragraph
ok  skills/interactive-exhibit/SKILL.md rooms section: the wrong sentence corrected; what is editable there
ok  skills/interactive-exhibit/SKILL.md new rule: the Solar System room's drawer, and its framing
ok  skills/interactive-exhibit/SKILL.md writer allow list: the rooms section joins it
ok  skills/interactive-exhibit/SKILL.md step 4: the headless recipe
ok  skills/interactive-exhibit/SKILL.md install: 1.9 obligation
ok  skills/interactive-exhibit/SKILL.md fires_when: the body drawer and the headless recipe
ok  skills/ledger-and-session-records/SKILL.md version line 1.13 -> 1.14
ok  skills/ledger-and-session-records/SKILL.md v1.14 paragraph in the header
ok  skills/ledger-and-session-records/SKILL.md new rule: a wrong sentence in a skill, bump now or carry it
ok  documentation/WHERE_WE_ARE.md      rewritten

Stamps updated: interactive-exhibit 1.9, ledger-and-session-records
1.14, the protocol's header (v3.77, cut from b3cfc780), the
ledger's header, Where We Are's date.

patch applied

NEXT:
  1. python orrery_maintenance_run.py -- it rebuilds the ledger's
     index and the protocol's skill manifest (1.8 -> 1.9,
     1.13 -> 1.14).

======================================================================
MAINTENANCE RUN -- generators, then checkers (L-188)
======================================================================
  Provenance scan is current (last run 20261002T034537Z, 0 day(s) ago).

GENERATORS -- regenerate every time; a no-op when nothing moved
----------------------------------------------------------------------
  Ledger index                 1.2s  rewrote LEDGER_CONSOLIDATED.md
  Skill manifest               0.1s  rewrote PROJECT_INSTRUCTIONS.md
  Constants export             1.7s  unchanged (1 checked, not written)
  Objects export               0.1s  unchanged (1 checked, not written)
  Module atlas                 7.8s  rewrote MODULE_ATLAS.md, MODULE_INDEX.md
  Data inventory               6.0s  rewrote DATA_INVENTORY.md
  Exact rows report            1.6s  unchanged (1 checked, not written) -- 8 of
                                     24 exact rows printed at 19 lines (9 orrery,
                                     10 gallery); 8 drawn only, 0 not followed, 0
                                     map entries broken
  Document index               0.1s  unchanged (1 checked, not written)

CHECKERS -- verdict informs the push call
----------------------------------------------------------------------
  Constants change             0.2s  No changes to constants_new.py since HEAD.
  Constants relations          0.2s  21 of 21 provenance tests passed against
                                     constants_new.py. No constants have drifted.
  Derived figures              0.8s  No figure count exceeds its inputs: 29
                                     derived row(s) read, 17 judged OK -- 17 OK,
                                     12 NOT YET MIGRATED, 1 NO DERIVED LINE, 1
                                     UNMARKED CONVERSION; 15 conversion(s)
                                     checked.
  Constants export check       1.2s  Export matches the store: sha256
                                     089a5baf0101 on both sides; 79 rows re-read,
                                     66 not exported, 26 tokens; 172 conversions
                                     re-computed, 10 of 10 worked cases hold.
  Objects export check         0.1s  pass
  Exact rows by the count      1.3s  PASSING -- 8 printed exact rows each state a
                                     count; 9 orrery lines print through
                                     exact_text(); 10 gallery lines are served
                                     the count
  Dimensions                   1.4s  No unit contradicts its arithmetic: 44
                                     derived row(s) read -- 32 OK, 9 NO UNIT, 3
                                     NOT CHECKABLE.
  Cross-check annotations      0.1s  19 of 19 cross-check annotation tests
                                     passed.
  Citation inheritance         0.1s  20 of 20 citation-inheritance tests passed.
  Status lines                 0.1s  All 81 status lines in constants_new.py are
                                     well formed; 61 rows carry none.
  Row shape                    0.1s  All 145 row shapes in constants_new.py fit
                                     the assignment's own line.
  Scanner recognition 1d/1e    0.3s  27 of 27 recognition pins hold: real
                                     citations recognized, fake ones refused.
  Reset completeness          26.2s  PASS -- all 309 IntVars + 3 StringVars + 10
                                     entries reset to startup defaults; date set
                                     to now.
  Orbit cache                  2.1s  All 6 orbit cache tests passed: cache loads,
                                     old formats convert, corrupted entries are
                                     dropped.
  Earth pole of date           0.3s  all 14 checks passed (geometry, ERFA,
                                     fallback, cache, hover, transform).
  Worksheet checker            9.2s  76 of 114 routed, 8 clean
  Worksheet checker tests     18.5s  All 136 checks passed
  Worksheet key round trip     1.1s  RESULT: 52 sites minted 52 distinct keys,
                                     all resolved; 52 pinned keys still resolve;
                                     1 retired keys confirmed gone.
  Builder marker join         26.8s  All 76 checks passed
  Extractor pins               0.5s  RESULT: 29 string sites carry the pinned 73
                                     claims and 14 instruction drops, at LOOKBACK
                                     30 / LOOKAHEAD 25, extractor version 2.
  Provenance scanner          12.2s  296 TIER-1 FINDINGS IN THE SCANNED TREE

======================================================================
  19 of 19 gating checkers passed -- 121.6s total
  2 report-only, exit 0 whatever they find:
    Worksheet checker           76 of 114 routed, 8 clean
    Provenance scanner          296 TIER-1 FINDINGS IN THE SCANNED TREE
======================================================================

FILES WRITTEN THIS RUN
----------------------------------------------------------------------
  2033 file(s) examined, 9 written, 0 created, 0 removed, 3 rewritten identically
    written   DATA_INVENTORY.md
    written   LEDGER_CONSOLIDATED.md
    written   MODULE_ATLAS.md
    written   MODULE_INDEX.md
    written   PROJECT_INSTRUCTIONS.md
    written   PROVENANCE_AUDIT.md
    written   WORKSHEET_CHECK.md
    written   data/provenance_history.json
    written   documentation/prompts/citation_review.jsonl
    rewritten with identical bytes, no action needed:
      data/worksheet_check_state.json
      data/worksheet_routed.json
      test_output/test_orbit_paths.json
    20 file(s) over 2 MB compared by size and mtime only

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>

  2. Move this script into documentation/; commit and push. -- f7ad52dbf9f8bef81fdcb35ea7c3a442fc5f6fb2
  3. Reinstall interactive-exhibit and ledger-and-session-records
     from skills/ in Settings > Skills. -- done
  4. Replace the Project's instructions in claude.ai with the new
     PROJECT_INSTRUCTIONS.md. -- v3.77
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 

=================================================================================

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/patch_L363_9_room_step3b_drawer_20261002.py
ok  gallery_maintenance_run.py   CHECKERS: Solar System drawer
ok  gallery_maintenance_run.py   SERVED_FILES: solar_system_drawer.js
ok  interactive.html             header: step 3b update line
ok  interactive.html             script tag: solar_system_drawer.js
ok  interactive.html             CSS: fixed Sun row, opened rows, See more
ok  interactive.html             info panel: the two paragraphs say what the drawer does
ok  interactive.html             compose: hands the served rows to the drawer
ok  interactive.html             navHome: the Solar System room has its own Home
ok  interactive.html             scene tap: the Solar System room highlights without moving
ok  interactive.html             init: the body drawer is set up before the rows are built
ok  interactive.html             drawer section: points at the body drawer
ok  interactive.html             the body drawer: ssDrawer and the ss* functions
ok  interactive.html             buildSunDrawer: each row names its group; the body drawer wires its own
ok  interactive.html             buildSunDrawer: the See more button
ok  interactive.html             renderSunDrawer: rows matched by the group they name
ok  interactive.html             sunApplyVisibility: an optional group to frame on
ok  interactive.html             sunApplyVisibility: frames on frameIdx when given
ok  interactive.html             All / none: the Solar System room's own
ok  interactive.html             the room frames on where its bodies are now, at 20%
ok  interactive.html             sunGroupRadius: a body's distance now, in the Solar System room
ok  interactive.html             sunPositionRadius and sunFrameMargin
ok  interactive.html             sunFrameOn: the room's margin
ok  interactive.html             the opening frame follows the same rule
ok  documentation/smoke_solar_system_drawer.js created
ok  gallery/solar_system_drawer.js created
ok  tools/headless/compare_rooms.js created
ok  tools/headless/page_harness.js created
ok  tools/headless/run_room_driver.py created
ok  tools/headless/walk_solar_system_drawer.js created

Stamp updated: interactive.html's header (October 2, 2026).

patch applied

NEXT:
  1. python gallery_maintenance_run.py. The new checker, "Solar
     System drawer", should pass and name the rows it read.

======================================================================
  gallery maintenance run -- OFFLINE (before a commit)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

GENERATORS -- rewritten every time; a no-op when nothing moved
  PASS Module atlas              1.8s  rewrote MODULE_ATLAS.md,
                                    MODULE_INDEX.md
  PASS Constants export pull     0.8s  rewrote data/constants_export.sha
  PASS Config mirror             0.1s  no change to
                                    data/objects_config.json
  PASS Objects export pull       0.5s  rewrote data/objects_export.sha
  PASS Objects mirror            0.1s  no change to
                                    data/objects_config.json

CHECKERS -- the verdict informs the push call
  PASS Cache builder suite      16.7s  PASS (229 checks, 0 failures)
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
  PASS Store writer suite        5.7s  All 251 store-writer checks
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
  PASS Objects mirror suite      0.1s  MIRROR OBJECTS SUITE: pass
  PASS Objects mirror check      0.1s  OBJECTS MIRROR: pass
  PASS Config mirror check       0.1s  Every served link holds the
                                    export's value, unit and figure
                                    count; 74 link(s) compared, store
                                    089a5baf0101.
  PASS Pointer join              0.1s  Every link is accounted for: 98
                                    link(s) against orrery f7ad52db,
                                    20 fallback named; read check: 43
                                    of 43 measured rows reached carry
                                    a read.
  PASS Cache in step             0.1s  The served cache holds the
                                    config's 19 object(s) and their
                                    features exactly: 4 object(s) with
                                    35 named shell(s), in both cache
                                    files.
  PASS Feature renderers         0.8s  === ALL CHECKS PASSED ===
  PASS Page framing              0.1s  === ALL CHECKS PASSED ===
  PASS Sun shells                0.2s  ALL CHECKS PASSED
  PASS Earth scene geometry      0.2s  === ALL CHECKS PASSED ===
  PASS Hover budget              0.1s  === ALL CHECKS PASSED ===
  PASS Arrival                   0.2s  Arrival: both rooms open on the
                                    right things; every shell trace
                                    carries its key; the fallback with
                                    no arrival block is unchanged.
  PASS Display figures           0.2s  === PASS: 57 hover(s) and 296
                                    number(s) examined; 13 graded, 7
                                    graded by line, 44 held to the
                                    fixture ===
  PASS Solar System figures      0.1s  === PASS: 6 worked cases, 11
                                    drawer rows matched to their
                                    accuracy rows, 10 served
                                    distances; Uranus, Neptune and
                                    Pluto print to JPL's ten-thousands
                                    place ===
  PASS Solar System drawer       0.1s  === PASS: the Sun is never ticked,
                                    See more hides only what is not
                                    ticked, Home falls back through
                                    the order, All / none leaves the
                                    Sun, rooms are offered only where
                                    they exist, and the page asks this
                                    file ===
  PASS Guest book                0.1s  === GUEST BOOK: all 8 checks
                                    passed
  PASS Guest book updater        0.2s  === GUEST BOOK UPDATER: all 43
                                    checks passed (6 scripted runs,
                                    self-test first)
  PASS Daily run steps           0.1s  === DAILY RUN: all 3 step scripts
                                    found
  PASS Artifact 1 assembler      0.2s  === ALL CHECKS PASSED -- 5
                                    verdicts and T3's feature set
                                    match the 2026-08-31 pin ===
  PASS Cache siblings            0.1s  RESULT: 1 directory in data/ the
                                    builder did not make: solar-system
                                    (1). Check whether they belong
                                    there; the newer .gitignore rules
                                    keep the known conflict-copy
                                    shapes out of git but do not
                                    remove anything.

======================================================================
  23 of 23 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Cache siblings         RESULT: 1 directory in data/ the builder
  last swap 2026-10-02T16:40:49.432964+00:00: succeeded first time
======================================================================

  After you push: python gallery_maintenance_run.py --live

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  2. Move this script into documentation/; commit and push.
     No cache rebuild is needed: nothing served changed. -- 3ed967777e6f8dba45972287565406dd495cefe4
  3. python gallery_maintenance_run.py --live -- the new file
     should read SERVED and match.

======================================================================
  gallery maintenance run -- LIVE (after a push)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

LIVE -- what the deployed site actually serves

  fetching 15 files from https://palomasorrery.com/
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
    SERVED   gallery/solar_system_figures.js                matches the working copy
    SERVED   gallery/solar_system_drawer.js                 matches the working copy
    SERVED   data/objects_config.json                       matches the working copy
    SERVED   gallery/guestbook.js                           matches the working copy
    SERVED   data/guestbook.json                            matches the working copy

  PASS Served reachability       3.5s  all 15 files served and
                                    byte-identical to the working copy

  orrery export pinned at f7ad52db

  PASS Export freshness          0.4s  the served export is the orrery's
                                    at f7ad52db, byte for byte

  orrery HEAD f7ad52db
  examining 24 of 98 links; the other 74 are served from the export
    NOT IN STORE  create_sun_galactic_tide default not a top-level constant in the store
                  /objects/0/features/oort_cloud/galactic_tide/typical_radius
    NOT IN STORE  planet_poles['Sun']              not a top-level constant in the store
                  /objects/0/features/orientation
    NOT IN STORE  planet_poles['Jupiter']          not a top-level constant in the store
                  /objects/2/features/orientation/pole
    NOT IN STORE  planet_poles['Saturn']           not a top-level constant in the store
                  /objects/3/features/orientation/pole
  24 pointers: 20 match, 0 DRIFT, 0 UNIT MISMATCH, 4 could not be examined.

  PASS Store drift               1.1s  24 pointers against orrery
                                    f7ad52db -- 20 match, 0 DRIFT, 0
                                    UNIT MISMATCH, 4 could not be
                                    examined.

======================================================================
  2 of 2 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Store drift            24 pointers against orrery f7ad52db --
  last swap 2026-10-02T16:40:49.432964+00:00: succeeded first time
======================================================================

  Offline pass: python gallery_maintenance_run.py

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  4. Your phone, then the desktop, in the Solar System room.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> 

==================================================================================

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/patch_L404_1_rooms_in_store_editor_20261001.py
ok  tools/exhibit_store_editor.py        docstring: what it edits, for a rooms-section room
ok  tools/exhibit_store_editor.py        docstring: the room list, and the stamp
ok  tools/exhibit_store_editor.py        ROOM_WORDS_NOTE
ok  tools/exhibit_store_editor.py        rooms() lists every room
ok  tools/exhibit_store_editor.py        arrival_state reads a rooms-section room
ok  tools/exhibit_store_editor.py        highlight_state
ok  tools/exhibit_store_editor.py        arrival_changes takes a highlight
ok  tools/exhibit_store_editor.py        arrival_changes writes a changed highlight
ok  tools/exhibit_store_editor.py        room picker wide enough for solar-system
ok  tools/exhibit_store_editor.py        shell list heading can change per room
ok  tools/exhibit_store_editor.py        _load_room: a room with no shells clears the form and says why
ok  tools/exhibit_store_editor.py        tick heading per kind of room
ok  tools/exhibit_store_editor.py        the highlighted-row picker
ok  tools/exhibit_store_editor.py        _save passes the highlight
    tools/exhibit_store_editor.py: stamp and description updated in its docstring
ok  tools/store_writer.py                docstring: the three kinds of value
ok  tools/store_writer.py                docstring: the editable surface gains the rooms section
ok  tools/store_writer.py                docstring: two kinds of room, and the stamp
ok  tools/store_writer.py                ROOMS and CENTRE_ROW
ok  tools/store_writer.py                editable_paths docstring
ok  tools/store_writer.py                editable_paths reads the rooms section; section_rooms, room_ids, is_section_room
ok  tools/store_writer.py                plan: rooms-section drawn and highlight name a row other than the Sun
ok  tools/store_writer.py                _slug_at knows the rooms section
ok  tools/store_writer.py                refusal message names the highlight
ok  tools/store_writer.py                arrival_choices: a rooms-section room ticks its rows
ok  tools/store_writer.py                _row_choices; arrival_paths knows the rooms section
    tools/store_writer.py: stamp and description updated in its docstring
ok  tools/test_exhibit_store_editor.py   docstring: check 10
ok  tools/test_exhibit_store_editor.py   docstring: stamp
ok  tools/test_exhibit_store_editor.py   check 10: the room list; a section room has no shell rows
ok  tools/test_exhibit_store_editor.py   check 10: a section room's ticks and highlight
ok  tools/test_exhibit_store_editor.py   window walk: a room with no shells
    tools/test_exhibit_store_editor.py: stamp and description updated in its docstring
ok  tools/test_store_writer.py           docstring: check 9
ok  tools/test_store_writer.py           docstring: stamp
ok  tools/test_store_writer.py           fixture: a second body and a rooms section
ok  tools/test_store_writer.py           fixture paths for the room
ok  tools/test_store_writer.py           allow-list count includes the room's two
ok  tools/test_store_writer.py           check 9 on the fixture
ok  tools/test_store_writer.py           check 9 on the real config
ok  tools/test_store_writer.py           the allow-list line names every room
ok  tools/test_store_writer.py           closing line mentions the rooms section
    tools/test_store_writer.py: stamp and description updated in its docstring

patch applied

NOT CHANGED HERE, and now out of date in one sentence: the
interactive-exhibit skill (orrery repo) says the cache builder,
the assembler and every check read only "objects". The store
writer now reads "rooms" too. Recorded on L-404 for the skill's
next version.

NEXT:
  1. Open tools/exhibit_store_editor.py and click Run. Pick
     solar-system, tick Mercury, Venus and Mars, and Save. -- done
  2. python gallery_maintenance_run.py. The Store writer suite
     and the Store editor suite both pass and name solar-system.

======================================================================
  gallery maintenance run -- OFFLINE (before a commit)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

GENERATORS -- rewritten every time; a no-op when nothing moved
  PASS Module atlas              1.0s  rewrote MODULE_ATLAS.md,
                                    MODULE_INDEX.md
  PASS Constants export pull     0.7s  no change to
                                    data/constants_export.json,
                                    data/constants_export.sha
  PASS Config mirror             0.1s  no change to
                                    data/objects_config.json
  PASS Objects export pull       0.7s  no change to
                                    data/objects_export.json,
                                    data/objects_export.sha
  PASS Objects mirror            0.1s  no change to
                                    data/objects_config.json

CHECKERS -- the verdict informs the push call
  PASS Cache builder suite      11.9s  PASS (229 checks, 0 failures)
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
  PASS Store writer suite        5.1s  All 289 store-writer checks
                                    passed: an allow list that lets
                                    through only a shell's words, a
                                    belt's words and the arrival
                                    settings, the rooms section's
                                    included; a no-edit round trip;
                                    one line per change; empty words
                                    handled; a refused batch writing
                                    nothing; awkward text; and the
                                    shell list matching the cache
                                    check's rule.
  PASS Store editor suite        0.1s  All 269 store-editor checks
                                    passed: every box the form offers
                                    is one the writer allows; the word
                                    list and the tick list differ by
                                    the belts, on purpose; nothing
                                    typed saves nothing; the save
                                    message does not promise a visitor
                                    sees what they cannot yet; and a
                                    red Cache in step is explained
                                    rather than just shown.
  PASS Objects mirror suite      0.1s  MIRROR OBJECTS SUITE: pass
  PASS Objects mirror check      0.1s  OBJECTS MIRROR: pass
  PASS Config mirror check       0.1s  Every served link holds the
                                    export's value, unit and figure
                                    count; 74 link(s) compared, store
                                    089a5baf0101.
  PASS Pointer join              0.1s  Every link is accounted for: 98
                                    link(s) against orrery f7ad52db,
                                    20 fallback named; read check: 43
                                    of 43 measured rows reached carry
                                    a read.
  PASS Cache in step             0.1s  The served cache holds the
                                    config's 19 object(s) and their
                                    features exactly: 4 object(s) with
                                    35 named shell(s), in both cache
                                    files.
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
  PASS Solar System figures      0.1s  === PASS: 6 worked cases, 11
                                    drawer rows matched to their
                                    accuracy rows, 10 served
                                    distances; Uranus, Neptune and
                                    Pluto print to JPL's ten-thousands
                                    place ===
  PASS Solar System drawer       0.1s  === PASS: the Sun is never ticked,
                                    See more hides only what is not
                                    ticked, Home falls back through
                                    the order, All / none leaves the
                                    Sun, rooms are offered only where
                                    they exist, and the page asks this
                                    file ===
  PASS Guest book                0.1s  === GUEST BOOK: all 8 checks
                                    passed
  PASS Guest book updater        0.2s  === GUEST BOOK UPDATER: all 43
                                    checks passed (6 scripted runs,
                                    self-test first)
  PASS Daily run steps           0.1s  === DAILY RUN: all 3 step scripts
                                    found
  PASS Artifact 1 assembler      0.2s  === ALL CHECKS PASSED -- 5
                                    verdicts and T3's feature set
                                    match the 2026-08-31 pin ===
  PASS Cache siblings            0.1s  RESULT: 1 directory in data/ the
                                    builder did not make: solar-system
                                    (1). Check whether they belong
                                    there; the newer .gitignore rules
                                    keep the known conflict-copy
                                    shapes out of git but do not
                                    remove anything.

======================================================================
  23 of 23 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Cache siblings         RESULT: 1 directory in data/ the builder
  last swap 2026-10-02T16:40:49.432964+00:00: succeeded first time
======================================================================

  After you push: python gallery_maintenance_run.py --live

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  3. Move this script into documentation/; commit and push. The
     opening view reaches the site on the push alone: no cache
     rebuild is needed for it. -- 555150f1e84f230334b1e214364377b122c642a2
PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> 

-- gallery moved to 0ffa451838dd5753710b3ec77d0d6f2f052f3d96
-- orrery moved to 
===============================================================================

Yes. Two of the three patches change what you see, so they need your eyes. The editor needs a quick look, and the Solar System room needs the full phone check.

Report anything odd with its conditions: which device, which way up, and what you had just done.

**1. The editor, at your desktop, before you push**
- Open the editor and confirm the room list shows sun, earth and solar-system. -- yes
- Pick solar-system. The middle panel should explain that the rows' words aren't edited here, and nothing from the previous room should be left on screen. -- yes
- On the right there should be ten bodies to tick (no Sun), with Apophis marked as a See more row, plus the "Highlighted row" picker. -- yes

**2. The Solar System room, on your phone held upright, after the push**
- **Opening:** the four inner planets are drawn, the view holds Mars with a little room to spare, and the closed drawer's handle names Earth. -- yes.
- **The Sun's row:** it has no box and no GO. Tapping it opens "Enter the Sun room", and that link takes you into the Sun's room. -- yes. great idea! thanks. and earth too. 
- **Ticking:** tick Jupiter. The view widens to hold it, and Jupiter's row opens saying "No room or cards yet". The drawer stays open. -- yes
- **Pluto:** tick Pluto. You'll see Pluto itself, with its orbit cut off at the box edge on the far side. Press − to see the whole orbit. This is your 20% ruling, so judge whether it looks right. -- yes, and the - sign shows the whole orbit.
- **Name taps:** tap a name. The row opens and the view should not move. Tap it again and the row closes. -- correct. suggestion, when a row highlights, could we move the highlighted row to the top of the scene list?
- **See more:** pressing it shows Apophis, and the button changes to "See fewer". Tick Apophis, then press See fewer: Apophis stays, because it's ticked. -- yes
- **Tap a body in the picture:** its hover text opens and its row is highlighted, while the view stays put. -- yes
- **GO:** GO on an unticked body ticks it, closes the drawer and opens its text box. -- yes. suggestion, add an arrow pointer from the text box to the object.
- **Home:** it returns to the last body you ticked. -- yes 
Untick that body and press Home again: it falls back to the one before. -- no, previous ticks do not register. let's discuss. one option might be that a second Home tap returns to the original view. 
Untick everything and press Home: the four inner planets come back. -- yes
- **Opened rows on a small screen:** with a row open, check the drawer still fits and scrolls, and that the "Enter" button is easy to hit. -- not clear
- **The i-panel:** read the two new paragraphs in place. -- could you break paragraphs into bulleted lists for readabiliy?
- Then do the same holding the phone sideways, then on the desktop. -- correct

**3. The Sun and Earth rooms, quickly, because their drawer code is shared**
- Tick and untick a few rows, use GO on one, try All / none, and press Home.
- They should behave exactly as before. My headless comparison says they do, but only your eyes can see it. -- correct

The ledger keeps the Solar System room's item open until this check is done. The Sun's numbers wait until after it. -- looks great. 