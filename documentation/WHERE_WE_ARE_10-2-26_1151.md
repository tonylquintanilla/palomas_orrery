<!-- Doc-Kind: hand | Where the project is and where it is going, in plain words. One file, rewritten in place; read it at the end of every session. -->
# Where We Are

Last updated: October 2, 2026
- Written at orrery b3cfc780 and gallery cfc53490, plus this session's
  two patches.

> **READ THIS FIRST**
>
> **Changed this session:**
> - The Exhibit Store Editor now lists every room, the Solar System
>   room included, and can set what it opens on.
> - The Solar System room's drawer is built: See more, rows that open
>   with a way into the Sun and Earth rooms, and Home remembering what
>   you ticked. Not yet on the website.
> - Your ruling: the room frames where each body is now, plus 20%,
>   not its whole orbit. You also confirmed five smaller calls I had
>   made in the build.
> - The two skills are updated for this work, with a new rule on when
>   a skill gets a new version.
> - The last session's two skill reinstalls are confirmed.
>
> **Do next:**
> - *You check the drawer on your phone, then the desktop.*
>
> **Needs you now:**
> - *Read the room's two new info paragraphs and say if they are right.*
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

## The goal

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
  unticked, a tap on a body finding its row, and Home remembering.
- The room will frame where each body is now, plus 20%. Pluto's orbit
  runs past the edge until you zoom out.
- Each body's info panel shows a description and a NASA link.
- Those words and links come from the orrery's own object list. The
  website keeps copies, written by a tool, and a check fails if anyone
  edits them by hand.
- The editor can set what any room opens on. It cannot yet change the
  words on the Solar System room's rows, such as Pluto's sentence.
- The rest of the orrery's objects are not connected yet.

## The next three steps  **>> UPDATED THIS SESSION**

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
- Choosing a date, and animation, your idea of October 1.
  - The range would follow only the bodies you tick.
  - Talked through once the drawer is built.
- The full check of the orrery's object list against JPL Horizons.
  - Its first run lists what disagrees; simple errors get fixed and
    listed, the rest come to you.
- Whether the editor should also edit the words on the Solar System
  room's rows, such as Pluto's sentence.
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

  2. Move this script into documentation/; commit and push. --
  3. Reinstall interactive-exhibit and ledger-and-session-records
     from skills/ in Settings > Skills.
  4. Replace the Project's instructions in claude.ai with the new
     PROJECT_INSTRUCTIONS.md.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 