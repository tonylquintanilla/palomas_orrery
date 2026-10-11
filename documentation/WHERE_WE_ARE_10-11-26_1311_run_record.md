<!-- Doc-Kind: hand | Where the project is and where it is going, in plain words. One file, edited by section; Tony's run record sits below the marker at the end and no patch edits it. -->
# Where We Are

Last updated: October 11, 2026, after your notes in the run record.
- Written at orrery 6fc3648 and gallery fd17abf.

> **READ THIS FIRST**
>
> **Changed since you last read this:**
> - Your notes in the run record are in the ledger, each on its item.
>   Your order after the Sun and Earth rooms: L-433 (the road after).
> - Two checks had no dashboard button; both have one now.
> - Objects that fall to the default goldenrod are listed: L-432
>   (default colours). Encke first.
> - Orbital periods are written up: L-431 (orbital periods).
>
> **Do next:** *the orbital periods design talk, then its build, as you
> asked: `DESIGN_L431_orbital_periods_20261011.md`, section 7.*
>
> **Needs you now:**
> - *Orrery: run patch_L431_2, then the maintenance run (22 of 22),
>   push.*
> - *Decide L-425 (citation location checks): which checks to build,
>   on the run's results (on L-425 and in the handoff).*

*Italic* lines are the must-reads. Marks reset at every update.

## The road  **>> UPDATED THIS SESSION**

  1-4. [done]  The Sun, Earth and Solar System rooms are live; the orrery
               feeds the website and nothing is typed twice.
  5.   [NOW]   *Earth's old items are finished, in your order.* The
               website patch and Earth's typed facts are live.
  6.   [next]  The typed facts: the inner Oort cloud is drawn in the
               orrery; the website next, then the check.
  6a.  [next]  *Orbital periods from JPL for every body, printed by
               their errors: design talk first.*
  7.   [next]  The Sun's numbers get the checking Earth's got.
  8.   [done]  The served objects are checked against JPL Horizons
               every day, in the Daily Run.
  9.   [next]  The website's checks, in the order you confirmed:
               L-423 (the website's checks).
 10.   [next]  A bare interactive.html link opens the Solar System room;
               the Explorer gets its own address.
 11.   [later] The rest of the orrery's objects come to the website.
 12.   [later] Encounters: comets and spacecraft at the dates that matter.
 13.   [later] The planets get their details, Jupiter and Saturn first;
               you lean to the inner planets (L-433). << new this session
 14.   [later] The Earth System layers; the gallery's cards meanwhile.
 15.   [goal]  The website does what the desktop orrery does, with a date
               to choose, within the range the data covers.

## Settled  **>> UPDATED THIS SESSION**

Standing rulings. A line leaves after a few weeks, once it is habit.
- Orbital periods: JPL's own (PR), for every body that has one; the
  hover shows it, not the typed table; digits by the errors. (Oct 10)
- Comets listed by first apparition, oldest first. A colour is a
  drawing choice, to tell apart bodies drawn together; switch it up
  from the default goldenrod. (Oct 10)
- Fuzzy boundaries come before the Sun and Earth rooms close. Every
  new check gets its dashboard button. (Oct 10)
- The Hills cloud follows the paper: drawn from its Fig. 3, described
  from its text, everything cited. Full to 10,000 AU. (Oct 10)
- The lobby opens on the Solar System room, then the subjects. Every
  room's list: Go To in the middle, then the room's button. (Oct 10)
- Website names: Halley and Encke; JPL's "1P/Halley" stays in the list. (Oct 10)
- A row's sources come only from its own comment block. (Oct 9)
- Small fixes owed to a skill ride the version a session is already
  making; a change to a checker gets its own session. (Oct 8)
- No colour or other name that only one system knows. The panels'
  grey is one name, gray90. (Oct 6)
- OneDrive: no pause before a build; the retry is sufficient, and the
  swap log shows any retry. Empty "solar-system (N)" folders are
  harmless; delete by hand. (Oct 8, Oct 10)

## Signals  **>> UPDATED THIS SESSION**

Read from files when this page was written, not typed from memory.
- Last cache build: 20261011T134230Z, ok, no retry.
- Tier-1 on the gate path: 0, by name, in PROVENANCE_AUDIT.md at
  6fc3648 (your run of 2026-10-11). Whole tree: 292.
- This page's date and the ledger's newest stamp: both Oct 11. Agree.

## Waiting on you  **>> UPDATED THIS SESSION**

At the next design talk:
- *Orbital periods first (L-431): which centre, the drawn ellipse,
  the typed table, the apsidal markers.*
- Your order after the Sun and Earth rooms (L-433), in your words of
  Oct 10; the road changes when you confirm it.
- L-424 (the checker's one word for two cases): you marked it
  "unclear" (Oct 10). I explain it in plain words, then you decide.
- The scattered disk, with the Kuiper belt (L-136): "we should
  decide this. i lean yes." (Oct 10)
- The fuzzy outer corona, with the dust cloud; the exosphere the same way.
- Moving the highlighted row to the top of the list.
- GO's arrow, only if the text box stays centred.
- Earth's design talks, the belts' shape first.
- The tide's cone and brightness on the phone: L-408 (the galactic
  plane on the phone). The rest is ruled; it waits only on the build.

Not urgent, in your order:
1. Whether the editor also edits the Solar System room's rows.
2. Choosing a date, and animation.

## Where the details are  **>> UPDATED THIS SESSION**

- Every item: `LEDGER_CONSOLIDATED.md`. Open for build: L-421 (the
  typed facts), its website side.
- Orbital periods: design
  `documentation/DESIGN_L431_orbital_periods_20261011.md`
- Your notes of Oct 10: `WHERE_WE_ARE_10-10-26_2019_run_record.md`
- The typed facts: plan
  `documentation/MANIFEST_L421_typed_facts_20261006.md`; record
  `documentation/HANDOFF_L421_typed_facts_20261008.md`
- The inner Oort cloud: design
  `documentation/DESIGN_L421_inner_oort_tilt_20261009.md`; record
  `documentation/HANDOFF_L421_oort_orrery_20261010.md`
- The Horizons check: design
  `documentation/DESIGN_L395_horizons_check_20261007.md`; record
  `documentation/HANDOFF_L395_horizons_check_build_20261010.md`
- The split's tests and the citation checks: L-418 (splitting
  provenance-discipline, closed), L-425 (citation location checks),
  L-426 (the checker's small-number comparison); record
  `documentation/HANDOFF_L418_testing_20261009.md`
- The reasoning behind the order:
  `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md`

--- Your run record below this line. No patch edits it; the length cap
--- stops here; the close reads your timestamped copy and clears this.

**Tony**: Run record:

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/patch_L395_4_run_confirmed_and_page_20261008.py
ok  LEDGER_CONSOLIDATED.md         header stamp
ok  LEDGER_CONSOLIDATED.md         L-395 date
ok  LEDGER_CONSOLIDATED.md         L-395 Tony's run
ok  WHERE_WE_ARE.md                header date
ok  WHERE_WE_ARE.md                road stage 8
ok  WHERE_WE_ARE.md                decisions: the Horizons build

patch applied

NEXT:
  1. Run orrery_maintenance_run.py -- it rebuilds the ledger's index.
  2. Move this script into documentation/; commit and push.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

**Session: OPEN: 10-11-26 1026: Opus: Session build with repository management**

Where the drawing files go. Each repository gets the file in the same place:

Orrery: data/drawings/hills_cloud.json. The orrery’s maintenance run writes it, next to where it already writes data/constants_export.json. A checker re-draws the cloud from the constants file and fails if the stored dots don’t match.
Gallery: data/drawings/hills_cloud.json. The gallery’s maintenance run pulls it from your orrery push and checks its fingerprint against the orrery’s copy, the same way it already pulls data/constants_export.json.
What the browser loads: the cache builder copies the file into the served cache with the Sun’s other features. So, like a change of words, a new drawing reaches visitors only after a cache rebuild.

The new ledger item will cover giving the website stored drawings for the other scattered-dot shells: the streamer band, the outer cloud’s clumps and the galactic tide, plus any fuzzy boundary drawn as thinning dots. It will carry the rule from earlier: store a shape when it needs random dots or a model, and compute it when it’s a few numbers and a formula. It will point to L-239, which has to come first for the clumps and the tide, L-410 (fuzzy boundaries) and L-224 (the streamer band).

The orrery patch is in your orrery folder: patch_L421_6_drawings_export_20261011.py. It makes the orrery write the Hills cloud’s dots to data/drawings/hills_cloud.json and adds the check that guards that file.

Your steps:

In VS Code, open the patch from the orrery folder and click Run. You should see an ok line for every edit, then “patch applied: 4 file(s) edited, 2 created.”
Run orrery_maintenance_run.py. You should see three things:
“Drawings export ... rewrote data/drawings/hills_cloud.json”
“Drawings export check ... PASS -- 3 of 3 planted faults caught”
“23 of 23 gating checkers passed”, and on the provenance scanner’s line, “0 TIER-1 -- the push gate holds”

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/patch_L421_6_drawings_export_20261011.py
ok  hills_cloud_sampler.py             edit 1 of 6
ok  hills_cloud_sampler.py             edit 2 of 6
ok  hills_cloud_sampler.py             edit 3 of 6
ok  hills_cloud_sampler.py             edit 4 of 6
ok  hills_cloud_sampler.py             edit 5 of 6
ok  hills_cloud_sampler.py             edit 6 of 6
ok  solar_visualization_shells.py      edit 1 of 3
ok  solar_visualization_shells.py      edit 2 of 3
ok  solar_visualization_shells.py      edit 3 of 3
ok  orrery_maintenance_run.py          edit 1 of 6
ok  orrery_maintenance_run.py          edit 2 of 6
ok  orrery_maintenance_run.py          edit 3 of 6
ok  orrery_maintenance_run.py          edit 4 of 6
ok  orrery_maintenance_run.py          edit 5 of 6
ok  orrery_maintenance_run.py          edit 6 of 6
ok  palomas_orrery_dashboard.py        edit 1 of 3
ok  palomas_orrery_dashboard.py        edit 2 of 3
ok  palomas_orrery_dashboard.py        edit 3 of 3
ok  export_drawings.py                 created
ok  test_drawings_export.py            created

stamps updated: module docstrings of hills_cloud_sampler.py, solar_visualization_shells.py, orrery_maintenance_run.py, palomas_orrery_dashboard.py
patch applied: 4 file(s) edited, 2 created.

NEXT:
  1. Run orrery_maintenance_run.py. Expect "Drawings export ... rewrote data/drawings/hills_cloud.json",
     "Drawings export check ... PASS -- 3 of 3 planted faults caught",
     "23 of 23 gating checkers passed" and, on the provenance scanner's line,
     "0 TIER-1 -- the push gate holds".

======================================================================
MAINTENANCE RUN -- generators, then checkers (L-188)
======================================================================
  Provenance scan is current (last run 20261011T141323Z, 0 day(s) ago).

GENERATORS -- regenerate every time; a no-op when nothing moved
----------------------------------------------------------------------
  Ledger index                 2.3s  unchanged (1 of 1 rewritten, content
                                     identical)
  Skill manifest               0.2s  unchanged (1 of 1 rewritten, content
                                     identical)
  Constants export             1.1s  unchanged (1 checked, not written)
  Objects export               0.1s  unchanged (1 checked, not written)
  Drawings export              0.3s  rewrote data/drawings/hills_cloud.json
  Module atlas                 8.2s  rewrote MODULE_ATLAS.md, MODULE_INDEX.md
  Data inventory               5.6s  rewrote DATA_INVENTORY.md
  Exact rows report            2.0s  rewrote EXACT_ROWS_PRINTED.md -- 13 of 38
                                     exact rows printed at 43 lines (33 orrery,
                                     10 gallery); 8 drawn only, 11 not followed,
                                     0 map entries broken
  Document index               0.1s  unchanged (1 checked, not written)

CHECKERS -- verdict informs the push call
----------------------------------------------------------------------
  Constants change             0.3s  No changes to constants_new.py since HEAD.
  Constants relations          0.3s  25 of 25 provenance tests passed against
                                     constants_new.py. No constants have drifted.
  Derived figures              1.1s  No figure count exceeds its inputs: 36
                                     derived row(s) read, 26 judged OK -- 26 OK,
                                     10 NOT YET MIGRATED, 1 NO DERIVED LINE, 1
                                     UNMARKED CONVERSION; 18 conversion(s)
                                     checked.
  Constants export check       1.9s  Export matches the store: sha256
                                     9d79d8797a22 on both sides; 120 rows
                                     re-read, 56 not exported, 29 tokens; 315
                                     conversions re-computed, 10 of 10 worked
                                     cases hold.
  Objects export check         0.1s  pass
  Skill headers                0.2s  12 skills parsed, no consistency problems.
  Exact rows by the count      2.9s  PASSING -- 13 printed exact rows each state
                                     a count; 33 orrery lines print through
                                     exact_text() or row_text(); 10 gallery lines
                                     are served the count
  Dimensions                   2.3s  No unit contradicts its arithmetic: 54
                                     derived row(s) read -- 42 OK, 9 NO UNIT, 3
                                     NOT CHECKABLE.
  Cross-check annotations      0.2s  19 of 19 cross-check annotation tests
                                     passed.
  Citation inheritance         0.2s  20 of 20 citation-inheritance tests passed.
  Status lines                 0.1s  All 119 status lines in constants_new.py are
                                     well formed; 54 rows carry none.
  Row shape                    0.1s  All 176 row shapes in constants_new.py fit
                                     the assignment's own line.
  Scanner recognition 1d/1e    0.3s  27 of 27 recognition pins hold: real
                                     citations recognized, fake ones refused.
  Scanner row run (L-414)      0.3s  16 of 16 pins hold -- each row reads its own
                                     comment run, declared rows are named, the
                                     gate path is read by name.
  Reset completeness          17.9s  PASS -- all 311 IntVars + 3 StringVars + 10
                                     entries reset to startup defaults; date set
                                     to now.
  Orbit cache                  2.3s  All 6 orbit cache tests passed: cache loads,
                                     old formats convert, corrupted entries are
                                     dropped.
  Earth pole of date           0.6s  all 14 checks passed (geometry, ERFA,
                                     fallback, cache, hover, transform).
  Hills cloud sampler (L-421)    0.7s  PASS -- 4 of 4 planted faults caught; the
                                     real rows pass, the dots' plane tilted 34.1
                                     deg
  Drawings export check        0.7s  PASS -- 3 of 3 planted faults caught;
                                     hills_cloud 3600 dots, tilt 30.9 deg, sha256
                                     a51e93118069
  Worksheet checker           10.1s  74 of 110 routed, 8 clean
  Worksheet checker tests     17.4s  All 135 checks passed
  Worksheet key round trip     1.2s  RESULT: 52 sites minted 52 distinct keys,
                                     all resolved; 52 pinned keys still resolve;
                                     1 retired keys confirmed gone.
  Builder marker join         20.6s  All 76 checks passed
  Extractor pins               0.4s  RESULT: 29 string sites carry the pinned 73
                                     claims and 14 instruction drops, at LOOKBACK
                                     30 / LOOKAHEAD 25, extractor version 2.
  Provenance scanner           8.7s  0 TIER-1 -- the push gate holds

======================================================================
  23 of 23 gating checkers passed -- 110.5s total
  2 report-only, exit 0 whatever they find:
    Worksheet checker           74 of 110 routed, 8 clean
    Provenance scanner          0 TIER-1 -- the push gate holds
======================================================================

FILES WRITTEN THIS RUN
----------------------------------------------------------------------
  2168 file(s) examined, 9 written, 2 created, 1 removed, 5 rewritten identically
    written   DATA_INVENTORY.md
    written   EXACT_ROWS_PRINTED.md
    written   MODULE_ATLAS.md
    written   MODULE_INDEX.md
    written   PROVENANCE_AUDIT.md
    written   WORKSHEET_CHECK.md
    written   data/provenance_history.json
    written   documentation/prompts/citation_review.jsonl
    written   module_atlas.py
    created   data/drawings/hills_cloud.json
    created   documentation/patch_L421_6_drawings_export_20261011.py
    removed   patch_L421_6_drawings_export_20261011.py
    rewritten with identical bytes, no action needed:
      LEDGER_CONSOLIDATED.md
      PROJECT_INSTRUCTIONS.md
      data/worksheet_check_state.json
      data/worksheet_routed.json
      test_output/test_orbit_paths.json
    20 file(s) over 2 MB compared by size and mtime only

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>

  2. Move this script into documentation/; commit and push. The commit
     includes the new file data/drawings/hills_cloud.json. -- 
  3. Tell Claude the pushed SHA; the website half builds on it.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 

Move the patch script into documentation/, then commit and push. The commit includes the new drawing file.

One thing you’ll see in the orrery window: the Hills cloud now draws the same dots on every plot instead of fresh random ones each time. Those are the dots the website will draw. The tilt of this particular set comes out at 30.9 degrees, against the paper’s “about 30”.

Where this leaves us

The orrery is ready to hand its Hills cloud dots to the website, once you’ve run the patch and pushed.
The website half comes next: the redrawn Hills cloud, the band from 10,000 to 20,000 AU, the words, and the Galactic Plane row.

Going ahead with the website half. First the two remaining skills it needs.

Now the gallery's current Sun Oort cloud block and how its renderer fills served words.

Baseline: the gallery's offline maintenance run passes 26 of 26 here. Now the remaining code I need to read before building.

I have what I need. Building the gallery side now, starting with the tool that pulls the drawing from the orrery.

Now the renderer. Let me see its export list and the module-level state it keeps.

Now the renderer edits: the Hills cloud from served dots, the band for the clumps and the tide, and the galactic plane.

Now the served config. Let me view the raw text of the Oort cloud block.

The config settles under the mirror. Now a quick render of the Sun's features to read the new hovers.

Now the page: fetch the drawings the Sun's features name, before the room is drawn.

Twenty-odd builds in that suite each need the stand-in. Simpler to wrap the builder once in the suite's mocks.

The builder's offline suite passes, 232 checks including the three new ones. Now the gallery checker for the drawings.

Now I'll simulate the cache rebuild on a throwaway copy, the way the builder copies features verbatim, and run the gallery's full offline maintenance run against it.

Now the Sun shells check: its counts and its Oort cloud tests need to describe the new drawing.

The Sun shells check passes, 46 checks. Next, the display figures check: re-record its fixture of unchanged hovers, then confirm only the Oort cloud's hovers moved.

Exactly the expected hovers changed and nothing else. Now the siblings report, which named `data/drawings/` as unknown.

27 of 27 pass on the simulated rebuild. Let me confirm the hover budget actually measured the new Sun hovers, and see the line counts.

Hover budget passes; the new Sun hovers sit below the ten longest. Next, the headless room test: boot the real page with the Sun room and check the chrome.

The real Sun room boots headless: 3,600 served dots, filled words, and the Galactic Plane row ticks on. One more case: the drawing missing from the served cache must cost only that shape.

Missing drawing: reported twice, only the Hills cloud absent, room ready. Now the brief's typed-facts survey, run on the room before and after. Let me read its method.

The link answers and still places the north galactic pole in Coma Berenices. Now packaging the gallery patch. First, which committed files are LF.

All committed LF. Building the patch from the differences against the repository's committed copies.

Testing the gallery patch the same four ways as the orrery's.

Now I'll simulate your step 1 on that patched copy, with the drawing pulled but the cache not yet rebuilt, to see exactly which lines go red.

27 of 27 on the patched copy. Saving the gallery patch into your gallery folder.

Both patches are in your folders. Before you run them, one thing to confirm.

The website half is built and both patches are in your folders: `patch_L421_6_drawings_export_20261011.py` in the orrery folder and `patch_L421_7_oort_gallery_20261011.py` in the gallery folder.

**One thing to confirm before it ships.** The orrery session changed one clause in the Hills cloud's panel note so it describes what's actually drawn. Your confirmed note said the orbits are "picked within the ranges the model gives." It now reads:

> "Drawn as dots along orbits **picked where the model's orbits lie (its Fig. 3)**, so the tilt and the two arms come out of the orbits. How stretched the orbits are is chosen for the picture: the model shows it only as a plot. The dots thin out between 10,000 and 20,000 AU."

Is that wording all right?

**What changes on the website**
- **The Hills cloud** is drawn from the orrery's own 3,600 dots. The dots on your phone are exactly the ones in the orrery window. Its hover and panel use your confirmed words, and the tilt and the band's two ends are filled in from the constants file.
- **The outer cloud's clumps and the galactic tide** now start thin at 10,000 AU and are full by 20,000 AU, the same way the orrery draws them.
- **The Galactic Plane row** is new and starts unticked. It draws a faint violet ring in the galaxy's plane, a line through the Sun to both galactic poles, and a marker for the direction of Sagittarius A*. Its panel says the galaxy's plane and the planets' plane meet at 60 degrees, worked out from the stored pole.
- I also fixed the Solar System room's note from "1.1 times" to "1.2 times", which was owed since October 4.

**Your steps, in order**
1. **Orrery:** run the patch, then `orrery_maintenance_run.py` (expect 23 of 23), then commit and push.
2. **Gallery:** run the patch.
3. Open `tools/pull_drawings.py` and click Run. It copies the dots from your orrery push.
4. Run the Daily Run. Expect "27 of 27 gating checkers passed", including a new "Drawings" line that passes.
5. Commit and push, then run the live maintenance run from the dashboard.
6. **The phone look.** Close the Home Screen clip's tab first, then open the Sun room upright:
   - Tick the Hills cloud and use Go To. You should see a disk tipped against the planets' plane, with the dots thickest along two opposite arms.
   - Tap its name. The text box should show three distances and "about 30 degrees".
   - Tick the clumps, then the tide. Both should start thin inside the Inner Oort Cloud sphere.
   - Tick Galactic Plane and turn the view until the ring is edge-on. Tap a pole marker, then open the i panel, which should say "60 degrees".

**How I checked it:** on copies of both repositories, the patches ran cleanly, a second time, and with Windows line endings. The gallery's maintenance run passed 27 of 27 after a simulated cache rebuild. The real Sun room page started with no errors and drew all 3,600 served dots, and ticking the Galactic Plane row drew it. The plane through the website's dots tilts 30.9 degrees, worked out twice by separate arithmetic. Without the drawing file, only the Hills cloud is missing and the page says why. Two things I couldn't run here: JPL's servers, so the real cache rebuild is yours, and a phone.

I'll do the closing records once you've looked: the ledger, your page, the new ledger item for the other dot shells, the dashboard buttons for the two new gallery tools, and ledger-and-session-records 1.20.

**Where this leaves us**
- Both halves of the inner Oort cloud are built and waiting for you to run them, with one clause to confirm.
- The closing records follow your phone look.

The check flagged uncommitted changes in my working copies here again. I deleted the throwaway test copies, and I'm deliberately not committing or pushing the rest.

What's left are my working copies of the orrery and the gallery. They hold the same changes as your two patches, and I keep them as the reference for the closing records. You hold commit authority on both repositories, so nothing reaches GitHub except through your runs and your pushes in GitHub Desktop.

Nothing has changed for you. The one open question is still whether the panel-note wording "picked where the model's orbits lie (its Fig. 3)" is all right.



