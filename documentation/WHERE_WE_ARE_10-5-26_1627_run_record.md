<!-- Doc-Kind: hand | Where the project is and where it is going, in plain words. One file, rewritten in place; read it at the end of every session. -->
# Where We Are

Last updated: October 4, 2026, end of the day's third session. -- **Tony**: notes 10/5/26 -- 
- Written at orrery 41c1ca7a and gallery e7ef96eb.
- This session was a ledger sweep: no code changed. A Fable session
  ran its own sweep beside it, and both were checked against the code.

> **READ THIS FIRST**
>
> **Changed this session:**
> - Earth's old items are now one ordered list, in the order you
>   confirmed. They come before the rest of the Sun's list.
> - Seven ledger items closed because their work was already done: the
>   licenses, the skill-header check, the galactic tide, the
>   magnetotail's length, Earth's magnetosphere model, Earth in the
>   website's builder, and the magnetosphere's unused tooltip copy.
> - The four Earth numbers the scanner calls uncited are cited. The
>   scanner looks one line short of one source, and doesn't count a
>   written "declared" reason. That is now its own item.
> - Your notes on this page are in the ledger, so they survive this
>   rewrite.
> - Patches now convert Windows line endings to the standard LF and say
>   so, as you remembered the rule. The patch skill had said both.
> - The 22 older files stored with Windows line endings are converted
>   to LF, in a commit of their own. That item is off the backlog.
>
> **Do next:**
> - *Your ruling on the inner belt's wording, then Earth's orrery
>   patch.*
>
> **Needs you now:** -- done
> - *Run the ledger patch, then the maintenance run, and push.*
> - *Reinstall the patch skill and update the Project's instructions.*

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
- Saved data covering one orbit of each body is enough, as you decided.
- Within that range, a visitor will be able to choose a date, and
  perhaps play time forward.

## The road  **>> UPDATED THIS SESSION**

  1. [done]   The Sun's room is live on the website.
  2. [done]   Earth's room is live, with every number traced to its source.
  3. [done]   The numbers come from one place: the orrery feeds the
              website, and nothing is typed twice.
  4. [done]   The Solar System room becomes a second way in: all the
              planets, a drawer to pick them, and a way into each
              body's own room.
  5. [NOW]    *Earth's old items are finished, in the order you
              confirmed.* << new this session: the first of the
              room-by-room ledger cleanups you asked for. Each room's
              old items are grouped by the files the work opens, and
              only what the room shows is in scope.
  6. [next]   The Sun's numbers get the same checking Earth's got: the
              Sun's list, from its opening view. << moved this session:
              after Earth's list. The distance cards are done.
  7. [next]   The website's checks get a short list of their own, so a
              new room or a moved front door can't break unnoticed.
              << new this session.
  8. [next]   A bare interactive.html link opens the Solar System room,
              and the Explorer gets its own address. The lobby's wide
              Solar System card, its first half, is done.
  9. [later]  The rest of the orrery's objects come to the website --
              dwarf planets, asteroids, moons -- through the same
              connection that now carries the room's eleven bodies,
              checked against JPL Horizons.
 10. [later]  Encounters: comets and spacecraft shown at the dates
              that matter.
 11. [later]  The planets get their details -- layers, rings, magnetic
              fields -- Jupiter and Saturn first.
 12. [goal]   The website does what the desktop orrery does, from data
              fetched from JPL each night, with a date to choose and
              time to play within the range the data covers.

## Right now  **>> UPDATED THIS SESSION**

- Earth's magnetosphere is drawn from published models in both the
  orrery and the website.
  - One question was never answered: because Earth moves along its
    orbit, the solar wind hits it slightly from the side, so the nose
    should turn about 4 degrees. Neither drawing does, and neither says
    so. It now waits with live solar wind, which sets that angle.
- The website draws Earth's geocorona, its faint hydrogen halo. The
  orrery only mentions it in a hover; drawing it is Earth's list, item 1.
- The website's magnetotail hover already prints the 220 Earth radii
  the spacecraft reached.
- The website does not draw Earth's magnetic dipole cone; the orrery
  does. Whether the website should is now a design question.
- On the Sun: the distance cards are built on both sites, and the
  Roche limit is drawn at 3.45 solar radii, described as "about 3".
- The ledger holds 241 open items after the seven closes.

## The next three steps  **>> UPDATED THIS SESSION**

1. *Your ruling on the inner belt's wording.*
   - It says "where the measured particle flux peaks".
   - Once you rule, the new wording travels in both patches below.
2. Earth's orrery patch, then your look on the screen.
   - The geocorona drawn as its own shell.
   - Earth's tilt read from the stored number in five places.
   - The atmosphere shells measured from the same radius as the crust.
3. Earth's website patch, then your look on the phone.
   - The inner belt's wording.
   - The saved Earth test scene re-recorded from today's data.
   - The collapsed-features check added to the maintenance run. It
     passes today, so it cannot block a push.

## Waiting on you  **>> UPDATED THIS SESSION**

Now: -- done
- Run the ledger patch, then orrery_maintenance_run.py, and push.
- Reinstall safe-file-editing in Settings > Skills, and replace the
  Project's instructions with PROJECT_INSTRUCTIONS.md, now v3.80.

At the next design talk:
- The fuzzy outer corona, designed together with the dust cloud.
- Moving the highlighted row to the top of the list.
- GO's arrow, only if the text box stays in the centre, as you ruled.
  If it can't, no arrow.
- Earth's design talks, the belts' shape first.

Decisions from the Fable sweep, one at a time when you're ready:
- Whether items inside an ordered list need RICE scores at all.
- A handful of scores it proposes.

Not urgent, in your order:
1. The full check of the orrery's object list against JPL Horizons.
2. Whether the editor should also edit the words on the Solar System
   room's rows.
3. Choosing a date, and animation.
4. The scattered disk, with the Kuiper belt in the Solar System room.
   It is not the fuzzy boundary idea: the disk is a population of icy
   bodies, the fuzzy boundary is a way of drawing an edge. When the
   disk is designed, its edges would likely be drawn that way.

## Where the details are  **>> UPDATED THIS SESSION**

- Every item, done and open: `LEDGER_CONSOLIDATED.md`
  - This session: L-413 (Earth's list), L-414 (the scanner's window),
    L-415 (line endings), L-133 (the 22 older files, converted and closed).
    Closed: L-409, L-407, L-350, L-406, L-305, L-234, L-383.
  - The Sun's list: L-412.
- The reasoning behind the order:
  `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md`
- The latest session records:
  `documentation/HANDOFF_L413_ledger_sweep_and_earth_list_20261004.md`,
  and Fable's sweep, `documentation/LEDGER_SWEEP_review_20261004.md`

  =============================================================================

**Tony**: Run record: 

  Thanks, Tony. It was a good session. Everything is in the six patches below; nothing has changed on either site yet.

**One change from the plan: I didn't build the website patch**
- It needs a choice I shouldn't make for you. Your approved words for the inner belt say "protons", which is true of that belt only, and the website draws every belt with the same code. How that code tells the belts apart is a design question.
- It also needs a careful read of the website's tests, which pin hover text word for word. That's better done in a session at your machine.
- So its plan is written into this session's handoff, ready for next time.

**The closing patch, `patch_L413_3`**
- Opens L-416, L-417 and L-418.
- Records your rulings on the inner belt, the geocorona, Earth's tilt, the exosphere and the Horizons check.
- Closes L-389 on your reading.
- Rewrites Where We Are, and adds two handoffs: this session's record, and one for the Horizons design round.

**Tested together on a fresh copy**
- All five orrery patches ran in order.
- The maintenance run passed all 20 checks, and the scanner read 296.

**When you're back at your machine**
1. Orrery: run `patch_L413_2`, 
   
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/patch_L413_2_earth_orrery_20261005.py
ok  constants_new.py               frame note: what Tony ruled on 2026-09-28
ok  constants_new.py               LEO inner edge: why the equatorial radius
ok  constants_new.py               LEO outer edge: stale note replaced
ok  constants_new.py               stratopause: why the equatorial radius
ok  constants_new.py               thermopause: why the equatorial radius
ok  constants_new.py               geocorona row: the orrery now draws it
ok  constants_new.py               docstring credit
ok  coordinate_system_guide.py     the tilt in words (L-369)
ok  coordinate_system_guide.py     docstring credit
ok  earth_visualization_shells.py  imports: the atmosphere rows and row_text
ok  earth_visualization_shells.py  upper atmosphere tooltip: the hover's words; geocorona info added
ok  earth_visualization_shells.py  inner belt words (L-349, Tony 2026-10-05)
ok  earth_visualization_shells.py  docstring credit
ok  palomas_orrery.py              import the geocorona tooltip
ok  palomas_orrery.py              geocorona var
ok  palomas_orrery.py              geocorona in earth_shell_vars
ok  palomas_orrery.py              geocorona checkbox
ok  palomas_orrery.py              two plot hovers: the tilt in words (L-369)
ok  palomas_orrery.py              Celestial Sphere tooltip: the tilt in words (L-369)
ok  palomas_orrery.py              docstring credit
ok  shell_configs.py               import the two Earth info strings
ok  shell_configs.py               upper atmosphere hover from its info string; geocorona shell added
ok  shell_configs.py               inner belt words in the magnetosphere tooltip (L-349)
ok  shell_configs.py               docstring credit
ok  star_sphere_builder.py         the frame angle from the store (L-369)
ok  star_sphere_builder.py         its uses
ok  star_sphere_builder.py         docstring credit

patch applied

NEXT:
  1. Move this script into documentation/ FIRST. While it sits in
     the root folder the provenance scanner counts it as findings. -- done for all patches except L413_3
  2. Run orrery_maintenance_run.py (VS Code, Run). Expect every
     gating checker to pass and the scanner to read 296. The
     Constants export step rewrites data/constants_export.json:
     its fingerprint moves because of the notes; no value moves.

======================================================================
MAINTENANCE RUN -- generators, then checkers (L-188)
======================================================================
  Provenance scan is current (last run 20261005T161059Z, 0 day(s) ago).

GENERATORS -- regenerate every time; a no-op when nothing moved
----------------------------------------------------------------------
  Ledger index                 1.2s  unchanged (1 of 1 rewritten, content
                                     identical)
  Skill manifest               0.2s  rewrote PROJECT_INSTRUCTIONS.md
  Constants export             1.3s  rewrote data/constants_export.json
  Objects export               0.1s  unchanged (1 checked, not written)
  Module atlas                 6.3s  rewrote MODULE_ATLAS.md, MODULE_INDEX.md
  Data inventory               5.0s  rewrote DATA_INVENTORY.md
  Exact rows report            1.8s  rewrote EXACT_ROWS_PRINTED.md -- 13 of 34
                                     exact rows printed at 42 lines (32 orrery,
                                     10 gallery); 8 drawn only, 11 not followed,
                                     0 map entries broken
  Document index               0.1s  unchanged (1 checked, not written)

CHECKERS -- verdict informs the push call
----------------------------------------------------------------------
  Constants change             0.4s  7 of the changed line(s) are module
                                     docstring text (base 124 line(s); working
                                     131 line(s)).
  Constants relations          0.2s  25 of 25 provenance tests passed against
                                     constants_new.py. No constants have drifted.
  Derived figures              0.8s  No figure count exceeds its inputs: 34
                                     derived row(s) read, 24 judged OK -- 24 OK,
                                     10 NOT YET MIGRATED, 1 NO DERIVED LINE, 1
                                     UNMARKED CONVERSION; 18 conversion(s)
                                     checked.
  Constants export check       1.4s  Export matches the store: sha256
                                     9f52e44ed5c4 on both sides; 101 rows
                                     re-read, 56 not exported, 27 tokens; 310
                                     conversions re-computed, 10 of 10 worked
                                     cases hold.
  Objects export check         0.1s  pass
  Skill headers                0.2s  11 skills parsed, no consistency problems.
  Exact rows by the count      1.6s  PASSING -- 13 printed exact rows each state
                                     a count; 32 orrery lines print through
                                     exact_text() or row_text(); 10 gallery lines
                                     are served the count
  Dimensions                   1.2s  No unit contradicts its arithmetic: 52
                                     derived row(s) read -- 40 OK, 9 NO UNIT, 3
                                     NOT CHECKABLE.
  Cross-check annotations      0.1s  19 of 19 cross-check annotation tests
                                     passed.
  Citation inheritance         0.1s  20 of 20 citation-inheritance tests passed.
  Status lines                 0.1s  All 101 status lines in constants_new.py are
                                     well formed; 53 rows carry none.
  Row shape                    0.1s  All 157 row shapes in constants_new.py fit
                                     the assignment's own line.
  Scanner recognition 1d/1e    0.3s  27 of 27 recognition pins hold: real
                                     citations recognized, fake ones refused.
  Reset completeness          21.2s  PASS -- all 310 IntVars + 3 StringVars + 10
                                     entries reset to startup defaults; date set
                                     to now.
  Orbit cache                  1.7s  All 6 orbit cache tests passed: cache loads,
                                     old formats convert, corrupted entries are
                                     dropped.
  Earth pole of date           0.3s  all 14 checks passed (geometry, ERFA,
                                     fallback, cache, hover, transform).
  Worksheet checker            8.8s  74 of 110 routed, 8 clean
  Worksheet checker tests     14.0s  All 135 checks passed
  Worksheet key round trip     0.8s  RESULT: 52 sites minted 52 distinct keys,
                                     all resolved; 52 pinned keys still resolve;
                                     1 retired keys confirmed gone.
  Builder marker join         17.4s  All 76 checks passed
  Extractor pins               0.4s  RESULT: 29 string sites carry the pinned 73
                                     claims and 14 instruction drops, at LOOKBACK
                                     30 / LOOKAHEAD 25, extractor version 2.
  Provenance scanner           8.4s  296 TIER-1 FINDINGS IN THE SCANNED TREE

======================================================================
  20 of 20 gating checkers passed -- 95.5s total
  2 report-only, exit 0 whatever they find:
    Worksheet checker           74 of 110 routed, 8 clean
    Provenance scanner          296 TIER-1 FINDINGS IN THE SCANNED TREE
======================================================================

FILES WRITTEN THIS RUN
----------------------------------------------------------------------
  2067 file(s) examined, 10 written, 0 created, 0 removed, 4 rewritten identically
    written   DATA_INVENTORY.md
    written   EXACT_ROWS_PRINTED.md
    written   MODULE_ATLAS.md
    written   MODULE_INDEX.md
    written   PROJECT_INSTRUCTIONS.md
    written   PROVENANCE_AUDIT.md
    written   WORKSHEET_CHECK.md
    written   data/constants_export.json
    written   data/provenance_history.json
    written   documentation/prompts/citation_review.jsonl
    rewritten with identical bytes, no action needed:
      LEDGER_CONSOLIDATED.md
      data/worksheet_check_state.json
      data/worksheet_routed.json
      test_output/test_orbit_paths.json
    20 file(s) over 2 MB compared by size and mtime only

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>

  3. Open the orrery and look (Mode 5): Earth with Exosphere
     (Geocorona) ticked, zoomed out past the Moon; its hover; the
     Upper Atmosphere tooltip; the coordinate hover's teal line;
     the inner belt's hover (tick Magnetosphere). -- unclear what the hover teal line refers to. otherwise correct. 
  4. Commit and push.
  5. Then the gallery patch, which Claude builds after the push. -- unclear, what "after the push" means since i already have the patch. 
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 

2. `patch_L416_1`, 
   
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/patch_L416_1_dashboard_buttons_20261005.py
ok  palomas_orrery_dashboard.py    Arrival
ok  palomas_orrery_dashboard.py    Daily Run Steps, Display Figures, Earth Scene Geometry, Feature Renderers
ok  palomas_orrery_dashboard.py    Gallery Module Atlas
ok  palomas_orrery_dashboard.py    Page Framing
ok  palomas_orrery_dashboard.py    Pole of Date, Solar System Drawer
ok  palomas_orrery_dashboard.py    Sun Shells
ok  palomas_orrery_dashboard.py    Test Skill Headers
ok  palomas_orrery_dashboard.py    offline runner's description: the drawer, and every check has a button
ok  palomas_orrery_dashboard.py    offline runner's description: last sentence
ok  palomas_orrery_dashboard.py    docstring credit

patch applied

NEXT:
  1. Move this script into documentation/ before any maintenance
     run: in the root folder the provenance scanner counts it.
  2. Open the dashboard and look: the eleven new buttons, each in
     alphabetical place. The seven Node ones work once the gallery
     patch, patch_L416_2, has run; before that each reports the
     missing wrapper. -- please check. i cannot tell mode 5. 
  3. Commit and push, with the Earth patch or on its own.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 

3. `patch_L417_1`, 
   
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/patch_L417_1_skill_install_limits_20261005.py
ok  skills_index.py                docstring: what the check covers
ok  skills_index.py                docstring: credit
ok  skills_index.py                the documented limits, with their source
ok  skills_index.py                description_value and check_install_limits
ok  skills_index.py                called from parse_skill

patch applied

NEXT:
  1. Move this script into documentation/ before the maintenance
     run: in the root folder the provenance scanner counts it.
  2. Run orrery_maintenance_run.py. Skill headers should pass; its
     full output lists the five long skills as warnings.
  3. Commit and push, with the other orrery patches or on its own.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 

4.  `patch_L418_1`, 
   
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/patch_L418_1_skill_contents_and_histories_20261005.py
ok  skills/gallery-cache-builder/SKILL.md            rewritten whole
ok  skills/interactive-exhibit/SKILL.md              rewritten whole
ok  skills/ledger-and-session-records/SKILL.md       rewritten whole
ok  skills/orrery-coding-conventions/SKILL.md        rewritten whole
ok  skills/provenance-discipline/SKILL.md            rewritten whole
ok  skills/safe-file-editing/SKILL.md                rewritten whole
ok  PROJECT_INSTRUCTIONS.md                          header stamp
ok  PROJECT_INSTRUCTIONS.md                          SHA anchor
ok  PROJECT_INSTRUCTIONS.md                          v3.81 entry
ok  PROJECT_INSTRUCTIONS.md                          v3.78 moves down
ok  documentation/PROJECT_INSTRUCTIONS_HISTORY.md    v3.78 received
ok  skills_index.py                                  docstring: the contents rule
ok  skills_index.py                                  docstring: credit
ok  skills_index.py                                  skill_headings and check_contents
ok  skills_index.py                                  called from parse_skill
ok  documentation/SKILL_HISTORIES.md                 created

patch applied

NEXT:
  1. Move this script into documentation/ before the maintenance
     run: in the root folder the provenance scanner counts it.
  2. Run orrery_maintenance_run.py. Every gating checker passes. Its
     Skill manifest step writes the six new versions into the
     protocol; that is expected.
  3. Commit and push, with the other orrery patches.
  4. Reinstall the six skills in Settings > Skills from skills/:
     provenance-discipline, interactive-exhibit, safe-file-editing,
     orrery-coding-conventions, ledger-and-session-records,
     gallery-cache-builder. Then replace the Project's instructions
     with PROJECT_INSTRUCTIONS.md (v3.81). -- done
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 

5. then `patch_L413_3`.

-- refused. I am not sure why. i did not modify where we are. i copied it for this run record. also, i though annotations would not be refused. thanks.

6. Move all five into `documentation/`, run `orrery_maintenance_run.py`, look at Earth and the dashboard, then commit and push. -- d9f47a875fcd8ac5f793bb4dc397f2baf9108f9f
7. Gallery: run `patch_L416_2`, try the Sun Shells button, then commit and push.

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/patch_L416_2_offline_check_wrapper_20261005.py
ok  documentation\run_offline_check.py created

patch applied

NEXT:
  1. Try one from the dashboard: Gallery -- checks and data,
     Sun Shells. It should end "Sun shells -- PASSED (exit 0)".
  2. Run Gallery Maintenance Run -- offline. Nothing in it changes;
     every check should pass as before.

======================================================================
  gallery maintenance run -- OFFLINE (before a commit)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

GENERATORS -- rewritten every time; a no-op when nothing moved
  PASS Module atlas              1.3s  rewrote MODULE_ATLAS.md,
                                    MODULE_INDEX.md
  PASS Constants export pull     1.0s  rewrote
                                    data/constants_export.json,
                                    data/constants_export.sha
  PASS Config mirror             0.1s  no change to
                                    data/objects_config.json
  PASS Objects export pull       0.6s  rewrote data/objects_export.sha
  PASS Objects mirror            0.1s  no change to
                                    data/objects_config.json

CHECKERS -- the verdict informs the push call
  PASS Cache builder suite      14.2s  PASS (229 checks, 0 failures)
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
  PASS Store writer suite        5.7s  All 289 store-writer checks
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
  PASS Store editor suite        0.1s  All 272 store-editor checks
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
                                    count; 101 link(s) compared, store
                                    9f52e44ed5c4.
  PASS Pointer join              0.1s  Every link is accounted for: 108
                                    link(s) against orrery d9f47a87, 4
                                    fallback named; read check: 43 of
                                    43 measured rows reached carry a
                                    read.
  PASS Cache in step             0.1s  The served cache holds the
                                    config's 19 object(s) and their
                                    features exactly: 4 object(s) with
                                    35 named shell(s), in both cache
                                    files.
  PASS Feature renderers         0.8s  === ALL CHECKS PASSED ===
  PASS Page framing              0.1s  === ALL CHECKS PASSED ===
  PASS Sun shells                0.2s  ALL CHECKS PASSED
  PASS Earth scene geometry      0.2s  === ALL CHECKS PASSED ===
  PASS Hover budget              0.2s  === ALL CHECKS PASSED ===
  PASS Arrival                   0.2s  Arrival: both rooms open on the
                                    right things; every shell trace
                                    carries its key; the fallback with
                                    no arrival block is unchanged.
  PASS Display figures           0.2s  === PASS: 57 hover(s) and 307
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
                                    ticked, the handle names the last
                                    body ticked, All / none leaves the
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
  last swap 2026-10-05T16:01:39.168352+00:00: succeeded first time
======================================================================

  After you push: python gallery_maintenance_run.py --live

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  3. Move this script into documentation/; commit and push. -- ed48d078ceb639f5f98f13f4c6abc129f722c566
PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> 

8.  Reinstall the six skills, and replace the Project's instructions with v3.81. -- done 

Where this leaves us:
- Earth's orrery patch, the dashboard buttons and the skill changes wait on your runs.
- Next is the Earth website patch or the Horizons design round, in the order you choose. Each has its plan written down.

================================================================================================================================

Done. The rule is now written into the ledger skill, which goes to version 1.16. That also explains the refusal: your early-session notes are exactly what the old check tripped on.

**What the rule says**
- You write run records, pushed SHAs and comments into Where We Are, the handoffs and the ledger.
- So a patch checks those three only at the lines it edits, never with a fingerprint of the whole file.
- When a patch rewrites Where We Are, it first copies every line you changed into the session's handoff, word for word, and prints them.
- `patch_L413_4` is named in the skill as the worked example.

**What else the patch does**
- Protocol v3.82 gets a short entry, and v3.79 moves to the history file.
- The skill's oldest version entry moves to the skill histories file, by the three-entry rule written earlier today.
- It updates a few lines in the ledger, Where We Are and today's handoff, matched only at those lines, as the new rule says.

**Tested on a copy of your push**
- Run before `patch_L413_4`, it refuses and says to run that one first.
- Run after it, with a note of mine added to Where We Are, it worked and the note survived.
- A second run refuses and writes nothing.
- The maintenance run passed all 20 checks.

**Your steps**
1. Delete `patch_L413_3` from the root folder. -- done
2. Run `patch_L413_4`, 
   
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/patch_L413_4_session_close_20261005.py
ok  LEDGER_CONSOLIDATED.md                                     header stamp
ok  LEDGER_CONSOLIDATED.md                                     L-416, L-417, L-418 opened
ok  LEDGER_CONSOLIDATED.md                                     L-413 progress
ok  LEDGER_CONSOLIDATED.md                                     L-349 status
ok  LEDGER_CONSOLIDATED.md                                     L-349 ruling
ok  LEDGER_CONSOLIDATED.md                                     L-389 closed
ok  LEDGER_CONSOLIDATED.md                                     L-389 reading
ok  LEDGER_CONSOLIDATED.md                                     L-292 status
ok  LEDGER_CONSOLIDATED.md                                     L-292 built
ok  LEDGER_CONSOLIDATED.md                                     L-369 status
ok  LEDGER_CONSOLIDATED.md                                     L-369 built
ok  LEDGER_CONSOLIDATED.md                                     L-410 status
ok  LEDGER_CONSOLIDATED.md                                     L-410 exosphere
ok  LEDGER_CONSOLIDATED.md                                     L-395 status
ok  LEDGER_CONSOLIDATED.md                                     L-395 moved up
ok  LEDGER_CONSOLIDATED.md                                     L-300 status
ok  LEDGER_CONSOLIDATED.md                                     L-300 its button
ok  documentation/WHERE_WE_ARE.md                              rewritten whole
ok  documentation/HANDOFF_L413_earth_orrery_patch_20261005.md  created
ok  documentation/HANDOFF_L395_horizons_check_design_20261005.md created

carried 0 line(s) of yours from Where We Are into the handoff

patch applied

NEXT:
  1. Move this script into documentation/, and delete patch_L413_3
     from the root folder (it wrote nothing).
  2. Run orrery_maintenance_run.py. Every gating checker passes; its
     Ledger index step moves L-389, L-416 and L-417 to the closed
     section.
  3. Commit and push.
  4. When convenient: the teal-circle line, in the "Ecliptic
     Coordinates (J2000)" box at the plot's left.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 

3. then `patch_L419_1`.

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/patch_L419_1_annotation_rule_20261005.py
ok  LEDGER_CONSOLIDATED.md                                     header stamp
ok  LEDGER_CONSOLIDATED.md                                     L-419 written into the skill
ok  PROJECT_INSTRUCTIONS.md                                    header stamp
ok  PROJECT_INSTRUCTIONS.md                                    SHA anchor
ok  PROJECT_INSTRUCTIONS.md                                    v3.82 entry
ok  PROJECT_INSTRUCTIONS.md                                    v3.79 moves down
ok  documentation/HANDOFF_L413_earth_orrery_patch_20261005.md  the decision taken
ok  documentation/PROJECT_INSTRUCTIONS_HISTORY.md              v3.79 received
ok  documentation/SKILL_HISTORIES.md                           ledger skill: v1.13 received
ok  documentation/WHERE_WE_ARE.md                              changed this session: the rule
ok  documentation/WHERE_WE_ARE.md                              needs you now
ok  documentation/WHERE_WE_ARE.md                              waiting on you, now
ok  skills/ledger-and-session-records/SKILL.md                 v1.16 entry
ok  skills/ledger-and-session-records/SKILL.md                 v1.13 moves to SKILL_HISTORIES.md
ok  skills/ledger-and-session-records/SKILL.md                 the annotation rule (L-419)

patch applied

NEXT:
  1. Move this script into documentation/.
  2. Run orrery_maintenance_run.py; every gating checker passes.
  3. Commit and push.
  4. Reinstall ledger-and-session-records in Settings > Skills, and
     replace the Project's instructions with PROJECT_INSTRUCTIONS.md
     (v3.82).
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 

4. Move both into `documentation/`, run `orrery_maintenance_run.py`, 

======================================================================
MAINTENANCE RUN -- generators, then checkers (L-188)
======================================================================
  Provenance scan is current (last run 20261005T213703Z, 0 day(s) ago).

GENERATORS -- regenerate every time; a no-op when nothing moved
----------------------------------------------------------------------
  Ledger index                 1.9s  rewrote LEDGER_CONSOLIDATED.md
  Skill manifest               0.2s  rewrote PROJECT_INSTRUCTIONS.md
  Constants export             0.8s  unchanged (1 checked, not written)
  Objects export               0.1s  unchanged (1 checked, not written)
  Module atlas                 7.9s  rewrote MODULE_ATLAS.md, MODULE_INDEX.md
  Data inventory               5.3s  rewrote DATA_INVENTORY.md
  Exact rows report            1.6s  unchanged (1 checked, not written) -- 13 of
                                     34 exact rows printed at 42 lines (32
                                     orrery, 10 gallery); 8 drawn only, 11 not
                                     followed, 0 map entries broken
  Document index               0.1s  unchanged (1 checked, not written)

CHECKERS -- verdict informs the push call
----------------------------------------------------------------------
  Constants change             0.2s  No changes to constants_new.py since HEAD.
  Constants relations          0.2s  25 of 25 provenance tests passed against
                                     constants_new.py. No constants have drifted.
  Derived figures              0.9s  No figure count exceeds its inputs: 34
                                     derived row(s) read, 24 judged OK -- 24 OK,
                                     10 NOT YET MIGRATED, 1 NO DERIVED LINE, 1
                                     UNMARKED CONVERSION; 18 conversion(s)
                                     checked.
  Constants export check       1.3s  Export matches the store: sha256
                                     9f52e44ed5c4 on both sides; 101 rows
                                     re-read, 56 not exported, 27 tokens; 310
                                     conversions re-computed, 10 of 10 worked
                                     cases hold.
  Objects export check         0.1s  pass
  Skill headers                0.2s  11 skills parsed, no consistency problems.
  Exact rows by the count      1.7s  PASSING -- 13 printed exact rows each state
                                     a count; 32 orrery lines print through
                                     exact_text() or row_text(); 10 gallery lines
                                     are served the count
  Dimensions                   1.2s  No unit contradicts its arithmetic: 52
                                     derived row(s) read -- 40 OK, 9 NO UNIT, 3
                                     NOT CHECKABLE.
  Cross-check annotations      0.1s  19 of 19 cross-check annotation tests
                                     passed.
  Citation inheritance         0.1s  20 of 20 citation-inheritance tests passed.
  Status lines                 0.1s  All 101 status lines in constants_new.py are
                                     well formed; 53 rows carry none.
  Row shape                    0.1s  All 157 row shapes in constants_new.py fit
                                     the assignment's own line.
  Scanner recognition 1d/1e    0.3s  27 of 27 recognition pins hold: real
                                     citations recognized, fake ones refused.
  Reset completeness          19.4s  PASS -- all 310 IntVars + 3 StringVars + 10
                                     entries reset to startup defaults; date set
                                     to now.
  Orbit cache                  2.3s  All 6 orbit cache tests passed: cache loads,
                                     old formats convert, corrupted entries are
                                     dropped.
  Earth pole of date           0.4s  all 14 checks passed (geometry, ERFA,
                                     fallback, cache, hover, transform).
  Worksheet checker           11.0s  74 of 110 routed, 8 clean
  Worksheet checker tests     19.2s  All 135 checks passed
  Worksheet key round trip     1.0s  RESULT: 52 sites minted 52 distinct keys,
                                     all resolved; 52 pinned keys still resolve;
                                     1 retired keys confirmed gone.
  Builder marker join         27.9s  All 76 checks passed
  Extractor pins               0.5s  RESULT: 29 string sites carry the pinned 73
                                     claims and 14 instruction drops, at LOOKBACK
                                     30 / LOOKAHEAD 25, extractor version 2.
  Provenance scanner          13.8s  296 TIER-1 FINDINGS IN THE SCANNED TREE

======================================================================
  20 of 20 gating checkers passed -- 120.4s total
  2 report-only, exit 0 whatever they find:
    Worksheet checker           74 of 110 routed, 8 clean
    Provenance scanner          296 TIER-1 FINDINGS IN THE SCANNED TREE
======================================================================

FILES WRITTEN THIS RUN
----------------------------------------------------------------------
  2072 file(s) examined, 10 written, 1 created, 0 removed, 3 rewritten identically
    written   DATA_INVENTORY.md
    written   LEDGER_CONSOLIDATED.md
    written   MODULE_ATLAS.md
    written   MODULE_INDEX.md
    written   PROJECT_INSTRUCTIONS.md
    written   PROVENANCE_AUDIT.md
    written   WORKSHEET_CHECK.md
    written   data/provenance_history.json
    written   documentation/WHERE_WE_ARE_10-5-26_1627_run_record.md
    written   documentation/prompts/citation_review.jsonl
    created   documentation/project_instructions_v3_82.md
    rewritten with identical bytes, no action needed:
      data/worksheet_check_state.json
      data/worksheet_routed.json
      test_output/test_orbit_paths.json
    20 file(s) over 2 MB compared by size and mtime only

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>

then commit and push. -- 
5. Reinstall ledger-and-session-records, and replace the Project's instructions with v3.82. -- done

Where this leaves us:
- Today's session closes once these two patches are pushed.
- The next session confirms the reinstalled skills load at their new versions, then takes Earth's website patch or the Horizons design round, in your order.
