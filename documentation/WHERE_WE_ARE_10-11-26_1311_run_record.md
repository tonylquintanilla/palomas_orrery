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
     includes the new file data/drawings/hills_cloud.json. -- 1bbd9fe160471cbd3c3a036e4b750c314bf88c88
  3. Tell Claude the pushed SHA; the website half builds on it.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 

Move the patch script into documentation/, then commit and push. The commit includes the new drawing file.

One thing you’ll see in the orrery window: the Hills cloud now draws the same dots on every plot instead of fresh random ones each time. Those are the dots the website will draw. The tilt of this particular set comes out at 30.9 degrees, against the paper’s “about 30”. -- correct and beautiful.

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

Is that wording all right? -- correct

**What changes on the website**
- **The Hills cloud** is drawn from the orrery's own 3,600 dots. The dots on your phone are exactly the ones in the orrery window. Its hover and panel use your confirmed words, and the tilt and the band's two ends are filled in from the constants file.
- **The outer cloud's clumps and the galactic tide** now start thin at 10,000 AU and are full by 20,000 AU, the same way the orrery draws them.
- **The Galactic Plane row** is new and starts unticked. It draws a faint violet ring in the galaxy's plane, a line through the Sun to both galactic poles, and a marker for the direction of Sagittarius A*. Its panel says the galaxy's plane and the planets' plane meet at 60 degrees, worked out from the stored pole.
- I also fixed the Solar System room's note from "1.1 times" to "1.2 times", which was owed since October 4.

**Your steps, in order**
1. **Orrery:** run the patch, then `orrery_maintenance_run.py` (expect 23 of 23), then commit and push. -- done. 
2. **Gallery:** run the patch.

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/patch_L421_7_oort_gallery_20261011.py
ok  data/objects_config.json                       11 edit(s)
ok  gallery/feature_renderers.js                   24 edit(s)
ok  interactive.html                               3 edit(s)
ok  tools/gallery_cache_builder.py                 3 edit(s)
ok  tools/test_gallery_cache_builder_offline.py    9 edit(s)
ok  gallery_maintenance_run.py                     4 edit(s)
ok  documentation/check_cache_siblings.py          6 edit(s)
ok  documentation/smoke_sun_shells.js              13 edit(s)
ok  documentation/smoke_display_figures.js         4 edit(s)
ok  documentation/smoke_arrival.js                 1 edit(s)
ok  documentation/smoke_hover_budget.js            1 edit(s)
ok  tools/pull_drawings.py                         created
ok  tools/check_drawings.py                        created
ok  documentation/fixture_hovers_L421_3_on_fd17abf1.json created

stamps updated: module headers of gallery/feature_renderers.js, interactive.html, tools/gallery_cache_builder.py, tools/test_gallery_cache_builder_offline.py, gallery_maintenance_run.py, documentation/check_cache_siblings.py, documentation/smoke_display_figures.js
patch applied: 11 file(s) edited, 3 created.

NEXT, in this order (the orrery patch must be run and pushed first):
  1. Open tools/pull_drawings.py and click Run. It brings the Hills cloud's
     dots from your orrery push. Expect: "Pulled drawings from orrery
     <sha>: hills_cloud (3600 dots); rewrote hills_cloud."
  2. Run the Daily Run (guest book, Horizons check, cache builder, then the
     maintenance run). Expect "27 of 27 gating checkers passed"; the new
     "Drawings" line reads "DRAWINGS: PASS -- 3 of 3 planted faults caught".
  3. Move this script into documentation/; in GitHub Desktop look at the
     change list (no pile of deletions), commit and push.
  4. After the push: the dashboard's Gallery Maintenance Run -- live.
  5. The phone look: the steps are in the handoff Claude gives you.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> 

3. Open `tools/pull_drawings.py` and click Run. It copies the dots from your orrery push. -- please add this and any other new checks to the dashboard.

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\tools> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/tools/pull_drawings.py
Pulled drawings from orrery 1bbd9fe1: hills_cloud (3600 dots); rewrote hills_cloud. The SHA is in data/drawings/pulled_at.sha.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\tools> 

4. Run the Daily Run. Expect "27 of 27 gating checkers passed", including a new "Drawings" line that passes.

======================================================================
  DAILY RUN -- Sunday October 11, 2026  13:38
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io
======================================================================
Daily Run steps, from C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io:
  1. Guest book updater                 tools\guestbook_updater.py  found
  2. Horizons check                     tools\horizons_check.py  found
  3. Cache builder                      tools\gallery_cache_builder.py  found
  4. Gallery maintenance run, offline   gallery_maintenance_run.py  found
=== DAILY RUN: all 4 step scripts found
Last cache build: 2026-10-11 13:43 UTC, ok, 0 days ago.

======================================================================
  DAILY RUN step 1 of 4: Guest book updater
======================================================================
======================================================================
  guest book updater -- C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io
======================================================================
1 entry in the guest book; 171 gallery pages a link may point at.

Fetching the form's responses...
No new messages.

w write, r reply, x remove, p pin/unpin, f form address, s sheet address, q finish > q

======================================================================
  approved 0, declined 0, waiting 0; the guest book now has 1 entry
  No change to data/guestbook.json.
======================================================================

======================================================================
  DAILY RUN step 2 of 4: Horizons check
======================================================================
======================================================================
  HORIZONS CHECK -- 2026-10-11
======================================================================
Checked data/objects_export.json, pulled from orrery 9f154782.
Examined 13 entries: 0 due, 0 queries asked of JPL.

  sun                not due (confirmed on 2026-10-10, 1 day ago)
  mercury            not due (confirmed on 2026-10-10, 1 day ago)
  venus              not due (confirmed on 2026-10-10, 1 day ago)
  earth              not due (confirmed on 2026-10-10, 1 day ago)
  mars               not due (confirmed on 2026-10-10, 1 day ago)
  jupiter            not due (confirmed on 2026-10-10, 1 day ago)
  saturn             not due (confirmed on 2026-10-10, 1 day ago)
  uranus             not due (confirmed on 2026-10-10, 1 day ago)
  neptune            not due (confirmed on 2026-10-10, 1 day ago)
  pluto_barycenter   not due (confirmed on 2026-10-10, 1 day ago)
  apophis            not due (confirmed on 2026-10-10, 1 day ago)
  halley             not due (confirmed on 2026-10-10, 1 day ago)
  encke              not due (confirmed on 2026-10-10, 1 day ago)

HORIZONS CHECK: PASS -- 0 checked today, 13 not due

======================================================================
  DAILY RUN step 3 of 4: Cache builder
======================================================================
[RECOVER] removed retained data\solar-system.prev (cleared read-only on 6 entries)
[sweep] no sibling directories present
[POLE] earth: pole of 2026-10-11 served (RA 0.70066, Dec 89.85003 deg); tilt 23.43807 deg
[SWAP] the new cache is in place; every rename worked on the first try. Recorded in data/cache_swap_log.jsonl
[warn] sun: features-only entry; no Horizons fetch
[done] run 20261011T183843Z (nightly): 19 objects

----------------------------------------------------------------------
WHAT TO DO NEXT, before you commit anything:

  1. Run the gallery maintenance run, from this same folder:
         python gallery_maintenance_run.py
     Every gating checker should pass. Its LAST line reads the
     swap log back and should agree with the [SWAP] line above.
  2. In GitHub Desktop, look at the change list. A good build
     shows changed and added files and NO pile of deletions.
  3. Commit and push.
  4. After the push, check what the live site serves:
         python gallery_maintenance_run.py --live

TONY-ACTION ROLLUP for this run:
  (do)     steps 1 to 4 above, in that order.
----------------------------------------------------------------------

The builder's next steps start with the maintenance run.
The Daily Run runs it now.

======================================================================
  DAILY RUN step 4 of 4: Gallery maintenance run, offline
======================================================================
======================================================================
  gallery maintenance run -- OFFLINE (before a commit)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

GENERATORS -- rewritten every time; a no-op when nothing moved
  PASS Module atlas              1.8s  rewrote MODULE_ATLAS.md,
                                    MODULE_INDEX.md
  PASS Constants export pull     1.0s  rewrote data/constants_export.sha
  PASS Config mirror             0.1s  no change to
                                    data/objects_config.json
  PASS Objects export pull       0.7s  rewrote data/objects_export.sha
  PASS Objects mirror            0.2s  no change to
                                    data/objects_config.json
  PASS Drawings pull             0.7s  no change to
                                    data/drawings/hills_cloud.json,
                                    data/drawings/pulled_at.sha

CHECKERS -- the verdict informs the push call
  FAIL Cache builder suite      17.9s  FAIL (233 checks, 1 failures)
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
  PASS Store writer suite        9.9s  All 329 store-writer checks
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
  PASS Store editor suite        0.2s  All 312 store-editor checks
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
                                    count; 112 link(s) compared, store
                                    9d79d8797a22.
  PASS Horizons check suite      0.3s  HORIZONS CHECK SUITE: pass
  PASS Horizons confirmations    0.1s  HORIZONS CONFIRMATIONS: pass -- 13
                                    of 13 confirmed within 30 days
  PASS Pointer join              0.1s  Every link is accounted for: 119
                                    link(s) against orrery 1bbd9fe1, 4
                                    fallback named; read check: 43 of
                                    43 measured rows reached carry a
                                    read.
  PASS Cache in step             0.1s  The served cache holds the
                                    config's 19 object(s) and their
                                    features exactly: 4 object(s) with
                                    36 named shell(s), in both cache
                                    files.
  PASS Drawings                  0.2s  DRAWINGS: PASS -- 3 of 3 planted
                                    faults caught; pulled at orrery
                                    1bbd9fe1; hills_cloud 3600 dots,
                                    tilt 30.9 deg, sha256 a51e93118069
  PASS Collapsed features        0.1s  34 stored as themselves, 16
                                    collapsed, 0 unclassified.
  PASS Feature renderers         0.9s  === ALL CHECKS PASSED ===
  PASS Page framing              0.1s  === ALL CHECKS PASSED ===
  PASS Sun shells                0.2s  ALL CHECKS PASSED
  PASS Earth scene geometry      0.2s  === ALL CHECKS PASSED ===
  PASS Hover budget              0.2s  === ALL CHECKS PASSED ===
  PASS Arrival                   0.2s  Arrival: both rooms open on the
                                    right things; every shell trace
                                    carries its key; the fallback with
                                    no arrival block is unchanged.
  PASS Display figures           0.2s  === PASS: 61 hover(s) and 318
                                    number(s) examined; 13 graded, 7
                                    graded by line, 48 held to the
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
  PASS Guest book updater        0.4s  === GUEST BOOK UPDATER: all 43
                                    checks passed (6 scripted runs,
                                    self-test first)
  PASS Daily run steps           0.1s  === DAILY RUN: all 4 step scripts
                                    found
  PASS Artifact 1 assembler      0.3s  === ALL CHECKS PASSED -- 5
                                    verdicts and T3's feature set
                                    match the 2026-08-31 pin ===
  PASS Cache siblings            0.1s  RESULT: no sibling directories and
                                    nothing in data/ the builder did
                                    not make.

======================================================================
  1 of 27 gating checkers FAILED
  Cache builder suite
  1 report-only -- these do not gate, whatever they exit with:
    PASS Cache siblings         RESULT: no sibling directories and
  last swap 2026-10-11T18:38:49.683340+00:00: succeeded first time
======================================================================

----------------------------------------------------------------------
Cache builder suite -- FAIL (233 checks, 1 failures)
----------------------------------------------------------------------
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[SWAP] the new cache is in place; every rename worked on the first try. Recorded in data/cache_swap_log.jsonl
[warn] sun: features-only entry; no Horizons fetch
[warn] voyager_1: DP thin glide 2549 -> 2 points (tol=0.02 AU)
[done] run 20260709T000000Z (first-build): 19 objects
 FAIL L-421: every named drawing served byte for byte (hills_cloud)
  ok  L-421: the run manifest lists the drawings served ({'hills_cloud': 3})
  ok  first-build structural validation passes (pass)
  ok  clean fakes -> no guard warnings
  ok  every configured object served (19 of 19)
  ok  attribution present
  ok  served_window field present
  ok  earth has parity/addition field 'name'
  ok  earth has parity/addition field 'horizons_id'
  ok  earth has parity/addition field 'category'
  ok  earth has parity/addition field 'availability'
  ok  earth has parity/addition field 'parent'
  ok  earth has parity/addition field 'stored_center'
  ok  earth has parity/addition field 'canonical_frame'
  ok  earth has parity/addition field 'trajectory_of'
  ok  earth has parity/addition field 'osculating'
  ok  earth has parity/addition field 'positions'
  ok  earth has parity/addition field 'presets'
  ok  earth has parity/addition field 'features'
  ok  earth has parity/addition field 'orbit_type'
  ok  earth has parity/addition field 'as_of_today'
  ok  earth has parity/addition field 'event_link'
  ok  earth.osculating has 'center'
  ok  earth.osculating has 'epoch_jd'
  ok  earth.osculating has 'a_au'
  ok  earth.osculating has 'e'
  ok  earth.osculating has 'i_deg'
  ok  earth.osculating has 'node_deg'
  ok  earth.osculating has 'peri_deg'
  ok  earth.osculating has 'M0_deg'
  ok  earth.osculating has 'source'
  ok  voyager_1: osculating null, positions present
  ok  voyager_1 position file on disk
  ok  position file unit km
  ok  B-3: serving_base + scene_features restored for v0.6 parity
  ok  B-3: positions block carries step_hours
  ok  earth.pole_of_date served for the build's date (2026-07-09)
  ok  earth.pole_of_date passes the #P checker (no problems)
  ok  earth tilt of date is the geometry's on the served inputs (23.438152565955857 deg)
  ok  frame_constants serves KM_PER_AU and EARTH_OBLIQUITY_J2000_DEG from the export (EARTH_OBLIQUITY_J2000_DEG, KM_PER_AU)
  ok  no other object carries pole_of_date (none)
  ok  #P aborts a build whose served tilt is not its inputs' (#P earth: tilt 23.438153565955858 is not what its inputs giv)
  ok  earth as_of_today is km-scale (|r|=1.5e+08)
  ok  encke serves Tp_jd + solution_Tp_jd
  ok  encke orbit_type elliptical (e<1)
  ok  halley serves Tp_jd + solution_Tp_jd
  ok  halley orbit_type elliptical (e<1)
  ok  pluto/charon centered on pluto_barycenter
  ok  raw vectors written
  ok  elements JSONL history written
  ok  run manifest written
  ok  M1: feature_configs schema_version present
  ok  M1: feature_configs has all 12 object slugs
  ok  M1: every served feature entry is a dict (no lists survive)
  ok  M1: earth serves group 'earth_interior'
  ok  M1: earth serves group 'earth_atmosphere'
  ok  M1: earth serves group 'earth_exosphere'
  ok  M1: earth serves group 'earth_orbital_zones'
  ok  M1: earth serves group 'earth_geostationary'
  ok  M1: earth serves group 'earth_magnetosphere'
  ok  M1: earth serves group 'van_allen_belts'
  ok  M1: earth serves group 'hill_sphere'
  ok  M1: earth serves group 'orientation'
  ok  M1: earth inner_belt_distance is a measured entry in R_earth with source and pointer
  ok  M1: earth earth_atmosphere has lower_atmosphere + upper_atmosphere
  ok  M1: the pre-L-291 atmosphere_shell group is gone (no second home)
  ok  M1: jupiter has radiation_belts and NOT magnetosphere
  ok  M1: jupiter ring_system has all four ring slugs
  ok  M1: saturn ring_system has all seven ring slugs
  ok  M1: encke/halley present with empty {}
  ok  M1: inverted ring (inner >= outer) ABORTS
  ok  M1: malformed color string ABORTS
  ok  M1: malformed colors-list entry ABORTS
  ok  M1/L-238: interior shell (radius_fraction 0.19) PASSES
  ok  M1/L-238: radius_fraction 0.0 and -0.5 both ABORT
  ok  M1: a surviving features list (post-migration) ABORTS in derive_served
  ok  M2: sun serves a trust block
  ok  M2/L-256: sun (frame origin) trust method == not_applicable
  ok  M2/L-256: sun (frame origin) serves no trust window
  ok  M2: earth serves a trust block
  ok  M2: earth trust method == two_body_rate_v1
  ok  M2: earth has a finite positive window_days
  ok  M2: jupiter serves a trust block
  ok  M2: jupiter trust method == two_body_rate_v1
  ok  M2: jupiter has a finite positive window_days
  ok  M2: saturn serves a trust block
  ok  M2: saturn trust method == two_body_rate_v1
  ok  M2: saturn has a finite positive window_days
  ok  M2: mercury serves a trust block
  ok  M2: mercury trust method == two_body_rate_v1
  ok  M2: mercury has a finite positive window_days
  ok  M2: venus serves a trust block
  ok  M2: venus trust method == two_body_rate_v1
  ok  M2: venus has a finite positive window_days
  ok  M2: mars serves a trust block
  ok  M2: mars trust method == two_body_rate_v1
  ok  M2: mars has a finite positive window_days
  ok  M2: uranus serves a trust block
  ok  M2: uranus trust method == two_body_rate_v1
  ok  M2: uranus has a finite positive window_days
  ok  M2: neptune serves a trust block
  ok  M2: neptune trust method == two_body_rate_v1
  ok  M2: neptune has a finite positive window_days
  ok  M2: moon serves a trust block
  ok  M2: moon trust method == two_body_rate_v1
  ok  M2: moon has a finite positive window_days
  ok  M2: io serves a trust block
  ok  M2: io trust method == two_body_rate_v1
  ok  M2: io has a finite positive window_days
  ok  M2: titan serves a trust block
  ok  M2: titan trust method == two_body_rate_v1
  ok  M2: titan has a finite positive window_days
  ok  M2: pluto_barycenter serves a trust block
  ok  M2: pluto_barycenter trust method == two_body_rate_v1
  ok  M2: pluto_barycenter has a finite positive window_days
  ok  M2: pluto serves a trust block
  ok  M2: pluto trust method == two_body_rate_v1
  ok  M2: pluto has a finite positive window_days
  ok  M2: charon serves a trust block
  ok  M2: charon trust method == two_body_rate_v1
  ok  M2: charon has a finite positive window_days
  ok  M2: apophis serves a trust block
  ok  M2: apophis trust method == two_body_rate_v1
  ok  M2: apophis has a finite positive window_days
  ok  M2: voyager_1 serves a trust block
  ok  M2: voyager_1 trust method == fetched_positions
  ok  M2: voyager_1 trust window is null
  ok  M2: encke serves a trust block
  ok  M2: encke trust method == two_body_rate_v1
  ok  M2: encke has a finite positive window_days
  ok  M2: halley serves a trust block
  ok  M2: halley trust method == two_body_rate_v1
  ok  M2: halley has a finite positive window_days
  ok  M2: top-level served_window is non-null
  ok  M2: served_window brackets as_of (start < as_of < end)
  ok  M2: earth's window == its period cap (planet, cap=P)
  ok  M2: moon's window == P/8 (moon cap)
  ok  M2: halley's window == P/2 (comet cap)
  ok  L-363: the heliocentric participants are read from the config (12: earth, jupiter, saturn, mercury, venus, mars, uranus, neptune, pluto_barycenter, apophis, encke, halley)
  ok  L-149: served_window half-width == min of heliocentric participants
  ok  L-149: pluto's own window is smaller than the controlling one (sanity -- proves the exclusion is doing real work, not vacuously true)
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[SWAP] the new cache is in place; every rename worked on the first try. Recorded in data/cache_swap_log.jsonl
[warn] sun: features-only entry; no Horizons fetch
[warn] jupiter: trust measurement failed (simulated check-vector outage); served null window
[warn] voyager_1: DP thin glide 2549 -> 2 points (tol=0.02 AU)
[warn] served_window: null -- trust measurement missing/failed for ['jupiter'] (FLAG-3: null-on-any-failure is the conservative default)
[done] run 20260709T000000Z (first-build): 19 objects
  ok  M2: forced check-vector failure -> jupiter trust carries 'error'
  ok  M2: forced check-vector failure -> served_window null (FLAG-3, exercised)
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[SWAP] the new cache is in place; every rename worked on the first try. Recorded in data/cache_swap_log.jsonl
[warn] sun: features-only entry; no Horizons fetch
[warn] pluto: trust measurement failed (simulated check-vector outage); served null window
[warn] voyager_1: DP thin glide 2549 -> 2 points (tol=0.02 AU)
[done] run 20260709T000000Z (first-build): 19 objects
  ok  L-149: forced pluto check-vector failure -> pluto trust carries 'error'
  ok  L-149: forced pluto check-vector failure -> served_window STAYS non-null (pluto excluded from participation, so its failure can't gate the site)
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg

----------------------------------------------------------------------
THE CACHE SWAP COULD NOT FINISH, AND THERE WAS NO PREVIOUS
CACHE TO PUT BACK.

The new data was built and it passed every check. The step that
renames the new folder into place was refused 0 time(s) by
Windows. data/solar-system does not exist right now because it
did not exist before this run either.

WHAT TO DO: run the builder again. Nothing was committed or
pushed.

The new data is kept at
  C:\Users\tonyq\AppData\Local\Temp\tmp9iapagkz\data\.staging_solar-system_20260709T000000Z
This run was recorded in data/cache_swap_log.jsonl
----------------------------------------------------------------------

[ABORT] fail: swap raised: simulated: file lock during promotion (e.g. OneDrive) -- no commit; there was no previous cache to put back
  ok  L-173: swap raising is caught, not propagated as an uncaught exception
  ok  L-173: swap failure -> commit never attempted (committed stays False)
  ok  L-173: swap failure leaves out_dir exactly as atomic_swap_dir left it -- missing, not half-written -- so next run's recover_incomplete_swap() restores cleanly from .prev, not from a hand-patched state
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[SWAP] the new cache is in place; every rename worked on the first try. Recorded in data/cache_swap_log.jsonl
[ABORT] fail: post-swap verification: promoted generated='2000-01-01T00:00:00+00:00' does not match this run's '2026-07-09T00:00:00+00:00' -- stale data landed instead of this run's build -- no commit
  ok  L-173: post-swap content mismatch caught even though the swap call itself did not raise
  ok  L-173: post-swap mismatch -> commit never attempted
  ok  L-173: unlike the raised-exception case, the (bad) promoted data is left in place here, not deleted -- verify_promoted_data only refuses to commit it
  ok  L-216: a rename refused twice then allowed -> the run still passes
  ok  L-216: the NEW generation is live after the retry
  ok  L-216: the run left exactly ONE line in the tracked swap log (found 1)
  ok  L-216: the swap log says ok
  ok  L-216: the swap log says 3 attempts -- a line with more than one attempt and outcome ok is a failure this build absorbed (3)
  ok  L-216: the builder SAYS a refusal was absorbed, and on which rename, on the screen the build ran from
  ok  L-216: the maintenance run reads the same thing back from the log ('last swap 2026-07-09T00:00:00+00:00: succeeded after a refused rename -- staging_to_live took 3 attempts -- a refusal this build absorbed')
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[SWAP] the new cache is in place; every rename worked on the first try. Recorded in data/cache_swap_log.jsonl
[warn] sun: features-only entry; no Horizons fetch
[warn] voyager_1: DP thin glide 2549 -> 2 points (tol=0.02 AU)
[done] run 20260709T000000Z (first-build): 19 objects
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[SWAP] staging_to_live refused on attempt 1 of 6 ([Errno 13] simulated: Access is denied); waiting 0s
[SWAP] staging_to_live refused on attempt 2 of 6 ([Errno 13] simulated: Access is denied); waiting 0s
[SWAP] staging_to_live refused on attempt 3 of 6 ([Errno 13] simulated: Access is denied); waiting 0s
[SWAP] staging_to_live refused on attempt 4 of 6 ([Errno 13] simulated: Access is denied); waiting 0s
[SWAP] staging_to_live refused on attempt 5 of 6 ([Errno 13] simulated: Access is denied); waiting 0s
[SWAP] staging_to_live refused on attempt 6 of 6 ([Errno 13] simulated: Access is denied); giving up

----------------------------------------------------------------------
THE CACHE SWAP COULD NOT FINISH. THE OLD CACHE IS BACK IN PLACE.

The new data was built and it passed every check. The step that
renames the new folder into place was refused 6 time(s) by
Windows. This is the file lock recorded as L-216.

NOTHING WAS LOST. data/solar-system holds the generation that
was there before this run, so GitHub Desktop will NOT show a
pile of deletions. Nothing was committed and nothing was
pushed, so the live site is unaffected.

WHAT TO DO: run the builder again. The lock is usually brief.

The new data is kept at
  C:\Users\tonyq\AppData\Local\Temp\tmpjdlvfq9w\data\.staging_solar-system_20260709T000000Z
This run was recorded in data/cache_swap_log.jsonl
----------------------------------------------------------------------

[ABORT] fail: swap raised: staging_to_live refused on all 6 attempts ([Errno 13] simulated: Access is denied) -- no commit; the previous cache was put back
  ok  L-216: the swap fails -> the OLD generation is live again, byte for byte
  ok  L-216: the roll-back consumed .prev rather than leaving a second copy behind
  ok  L-216: the new generation is KEPT at its staging path
  ok  L-216: a rolled-back run never commits
  ok  L-216: the swap log says rolled_back ('rolled_back')
  ok  L-216: the log records every attempt that was made
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[SWAP] the new cache is in place; every rename worked on the first try. Recorded in data/cache_swap_log.jsonl
[warn] sun: features-only entry; no Horizons fetch
[warn] voyager_1: DP thin glide 2549 -> 2 points (tol=0.02 AU)
[done] run 20260709T000000Z (first-build): 19 objects
  ok  L-216: both refused -> the live directory is missing
  ok  L-216: the previous generation is still on disk in .prev
  ok  L-216: the plain-words block is printed, and it says not to commit the deletions
  ok  L-216: it names BOTH hand recoveries -- discard and re-run, or rename the staging folder
  ok  L-216: it never says 'will self-heal' without saying what Tony does
  ok  L-216: the swap log says failed ('failed')
  ok  L-216: a failed swap never commits
  ok  L-216: a clean swap says so too -- success carries evidence instead of silence
  ok  L-216: and the maintenance run agrees, reading the log
  ok  L-216: the first build wrote a swap log line to compare the dry run against (found 1)
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[dry-run] validated; wrote nothing outside C:\Users\tonyq\AppData\Local\Temp\tmpyph61etu\data\.staging_solar-system_earth_20260709T000000Z
  ok  L-216: a dry run leaves the swap log untouched
  ok  L-216: a refusal absorbed on an EARLIER rename is reported, not read as 'succeeded first time' ('last swap t: succeeded after a refused rename -- live_to_prev took 3 attempts -- a refusal this build absorbed')
  ok  L-421: data/drawings/ is a known folder, its conflict copy a stray (['drawings'], ['123-solar-system', 'drawings (1)', 'solar-system (1)'])
  ok  L-216: the sibling report NAMES the folders the builder did not make (['123-solar-system', 'solar-system (1)'])
  ok  L-216: a builder-made sibling is still classed as the builder's
  ok  L-216: the live cache and .prev are not reported as strays
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[SWAP] the new cache is in place; every rename worked on the first try. Recorded in data/cache_swap_log.jsonl
[warn] sun: features-only entry; no Horizons fetch
[done] run 20260709T000000Z (nightly): 19 objects
  ok  nightly structural validation passes
  ok  nightly did not shrink earth
  ok  frozen past point unchanged byte-for-byte
  ok  guard: clean charon point -> no warning
  ok  guard: 35.7 AU point -> exactly one warning
  ok  guard: outer-bound trip tagged likely-contamination
  ok  guard KEPT the point (monitor, not reject)
  ok  guard: spacecraft |r|>200 AU -> sanity warning
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[SWAP] the new cache is in place; every rename worked on the first try. Recorded in data/cache_swap_log.jsonl
[warn] sun: features-only entry; no Horizons fetch
[warn] voyager_1: DP thin glide 2549 -> 2 points (tol=0.02 AU)
[done] run 20260709T000000Z (first-build): 19 objects
[RECOVER] restoring C:\Users\tonyq\AppData\Local\Temp\tmp649bji9p\data\solar-system from C:\Users\tonyq\AppData\Local\Temp\tmp649bji9p\data\solar-system.prev (crash mid-swap)
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[SWAP] the new cache is in place; every rename worked on the first try. Recorded in data/cache_swap_log.jsonl
[warn] sun: features-only entry; no Horizons fetch
[done] run 20260709T000000Z (nightly): 19 objects
  ok  A-1/N1: nightly recovered the whole generation from .prev after a crash
  ok  A-1: archive not thinned by recovery (6302 >= 6302)
  ok  A-1: recovered nightly validates
[sweep] no sibling directories present
[ABORT] fail: nightly run but no live raw archive (possible unrecovered crash) -- refusing to build a thin cache
  ok  A-1: nightly with no generation ABORTS instead of committing thin

----------------------------------------------------------------------
WHAT TO DO NEXT, before you commit anything:

  1. Run the gallery maintenance run, from this same folder:
         python gallery_maintenance_run.py
     Every gating checker should pass. Its LAST line reads the
     swap log back and should agree with the [SWAP] line above.
  2. In GitHub Desktop, look at the change list. A good build
     shows changed and added files and NO pile of deletions.
  3. Commit and push.
  4. After the push, check what the live site serves:
         python gallery_maintenance_run.py --live

TONY-ACTION ROLLUP for this run:
  (do)     steps 1 to 4 above, in that order.
----------------------------------------------------------------------
  ok  A-2: main() exits nonzero on structural abort
  ok  A-2: main() exits 0 on pass
  ok  L-216: a good hand run ends by printing its next steps
  ok  L-216: the maintenance run comes BEFORE the commit in those steps (maintenance at 188, commit at 477)
  ok  L-216: the live check comes AFTER the push
  ok  L-216: a failed run does NOT print the next steps -- a failure prints its own advice
  ok  L-216: a dry run does NOT print them -- it changed nothing
  ok  L-216: a --commit run does NOT print them -- it has already committed, so 'before you commit' would be wrong
  ok  A-4: majorbody/id -> None
  ok  A-4: smallbody/None pass through unchanged
  ok  DP: straight line -> 2 endpoints
  ok  DP: keeps the bend
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[SWAP] the new cache is in place; every rename worked on the first try. Recorded in data/cache_swap_log.jsonl
[warn] sun: features-only entry; no Horizons fetch
[warn] voyager_1: DP thin glide 2549 -> 2 points (tol=0.02 AU)
[done] run 20260709T000000Z (first-build): 19 objects
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[SWAP] the new cache is in place; every rename worked on the first try. Recorded in data/cache_swap_log.jsonl
[warn] sun: features-only entry; no Horizons fetch
[warn] titan: FETCH FAILED (simulated Horizons outage); served last-good orbit, as_of_today nulled
[done] run 20260709T000000Z (nightly): 19 objects
  ok  A-3: failed Titan still SERVED (not vanished)
  ok  A-3: Titan conic served from last-good
  ok  A-3: Titan as_of_today NULLED (no stale marker)
  ok  A-3: run validates with a stale object
[sweep] no sibling directories present
[POLE] earth: pole of date NOT served (simulated Horizons outage) -- the page draws the frame's year-2000 axis and says so
[SWAP] the new cache is in place; every rename worked on the first try. Recorded in data/cache_swap_log.jsonl
[warn] sun: features-only entry; no Horizons fetch
[warn] voyager_1: DP thin glide 2549 -> 2 points (tol=0.02 AU)
[warn] earth: pole of date NOT served (simulated Horizons outage) -- the page draws the frame's year-2000 axis and says so
[done] run 20260709T000000Z (first-build): 19 objects
  ok  pole fetch fails: the build still validates (pass)
  ok  pole fetch fails: Earth served, orbit kept, pole_of_date null
  ok  pole fetch fails: the run manifest says so (not served (fetch failed))
  ok  N4/#B3: correct km conversion passes
  ok  N4/#B3: un-converted (AU-valued) served point ABORTS
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[SWAP] the new cache is in place; every rename worked on the first try. Recorded in data/cache_swap_log.jsonl
[warn] sun: features-only entry; no Horizons fetch
[warn] voyager_1: DP thin glide 2549 -> 2 points (tol=0.02 AU)
[done] run 20260709T000000Z (first-build): 19 objects
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[ABORT] fail: N3 object(s) dropped from a served set: ['titan']
  ok  N3: dropping a served object (titan) ABORTS the publication
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[SWAP] the new cache is in place; every rename worked on the first try. Recorded in data/cache_swap_log.jsonl
[warn] sun: features-only entry; no Horizons fetch
[warn] voyager_1: DP thin glide 2549 -> 2 points (tol=0.02 AU)
[done] run 20260709T000000Z (first-build): 19 objects
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[SWAP] the new cache is in place; every rename worked on the first try. Recorded in data/cache_swap_log.jsonl
[warn] sun: features-only entry; no Horizons fetch
[warn] encke: FETCH FAILED (solution-TP request_failed for encke); served last-good orbit, as_of_today nulled
[warn] halley: FETCH FAILED (solution-TP request_failed for halley); served last-good orbit, as_of_today nulled
[warn] served_window: null -- trust measurement missing/failed for ['encke', 'halley'] (FLAG-3: null-on-any-failure is the conservative default)
[done] run 20260709T000000Z (nightly): 19 objects
[master (root-commit) 5f63f61] data: nightly 2026-07-10
 1 file changed, 1 insertion(+)
 create mode 100644 data/f.txt
fatal: No configured push destination.
Either specify the URL from the command-line or configure a remote repository using

    git remote add <name> <url>

and then push using the remote name

    git push <name>

  ok  N5: solution-TP request failure serves last-good (not silent today-anchor)
[commit] PUSH FAILED (Command '['git', '-C', 'C:\\Users\\tonyq\\AppData\\Local\\Temp\\tmp14_yeqy5', 'push']' returned non-zero exit status 128.) -- committed locally only; remote is STALE
  ok  N2: local commit succeeds but no-remote push is NOT reported as pushed
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[SWAP] the new cache is in place; every rename worked on the first try. Recorded in data/cache_swap_log.jsonl
[warn] sun: features-only entry; no Horizons fetch
[warn] voyager_1: DP thin glide 2549 -> 2 points (tol=0.02 AU)
[done] run 20260709T000000Z (first-build): 19 objects
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[dry-run] validated; wrote nothing outside C:\Users\tonyq\AppData\Local\Temp\tmprufz76fv\data\.staging_solar-system_earth_20260709T000000Z
  ok  P2-2: --dry-run --object clears N3 + no-raw against an existing generation
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[dry-run] validated; wrote nothing outside C:\Users\tonyq\AppData\Local\Temp\tmpfp8xb12z\data\.staging_solar-system_earth_20260709T000000Z
  ok  P2-2: --dry-run --object works on a clean machine (no raw archive)
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-03 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[SWAP] the new cache is in place; every rename worked on the first try. Recorded in data/cache_swap_log.jsonl
[warn] sun: features-only entry; no Horizons fetch
[warn] voyager_1: DP thin glide 2548 -> 2 points (tol=0.02 AU)
[done] run 20260703T000000Z (first-build): 19 objects
  ok  P2-1: spacecraft first-build passes #T (arc ends today, not a stale stride point)
  ok  P2-1: spacecraft as_of_today is fresh regardless of stride phase
  ok  #B3: correct per-component conversion passes
  ok  #B3: swapped axes (magnitude-preserving) ABORTS component-wise
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[SWAP] the new cache is in place; every rename worked on the first try. Recorded in data/cache_swap_log.jsonl
[warn] sun: features-only entry; no Horizons fetch
[warn] voyager_1: DP thin glide 2549 -> 2 points (tol=0.02 AU)
[done] run 20260709T000000Z (first-build): 19 objects
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[SWAP] the new cache is in place; every rename worked on the first try. Recorded in data/cache_swap_log.jsonl
[warn] sun: features-only entry; no Horizons fetch
[warn] encke: FETCH FAILED (solution-TP request_failed for encke); served last-good orbit, as_of_today nulled
[warn] halley: FETCH FAILED (solution-TP request_failed for halley); served last-good orbit, as_of_today nulled
[warn] served_window: null -- trust measurement missing/failed for ['encke', 'halley'] (FLAG-3: null-on-any-failure is the conservative default)
[done] run 20260709T000000Z (nightly): 19 objects
  ok  P2-9: stale comet carries its comet block forward (not nulled)
  ok  L-274: run id with Z parses from the name (name)
  ok  L-274: run id WITHOUT Z parses -- the run_id=None fallback shape
  ok  L-274: an interposed object slug does not defeat the parser (L-148)
  ok  L-274: an unparseable name returns None so the caller falls back
  ok  L-274: a well-shaped but impossible date is refused, not accepted
[sweep] reaped 2 sibling(s) older than 3 day(s):
           .staging_solar-system_20260810T120000Z
           solar-system.quarantine_20260820T120000Z
[sweep] kept 1 recent sibling(s) as autopsies: solar-system.quarantine_20260901T120000Z
  ok  L-274: a 12-day-old quarantine is reaped even though mtime is now
  ok  L-274: a stale .staging sibling is reaped on the same rule
  ok  L-274: a same-day quarantine is KEPT as an autopsy (A-11)
  ok  L-274: the live served directory is never a sweep target
[sweep] no sibling directories present
[POLE] earth: pole of 2026-07-09 served (RA 0.71925, Dec 89.85021 deg); tilt 23.43815 deg
[ABORT] drawing 'hills_cloud' is named by a served feature but C:\Users\tonyq\AppData\Local\Temp\tmpkgvi3jo4\data\drawings\hills_cloud.json is missing -- run the gallery maintenance run first (it pulls the drawing from the orrery), then this builder -- no swap, no commit; staging kept at C:\Users\tonyq\AppData\Local\Temp\tmpkgvi3jo4\data\.staging_solar-system_20260709T000000Z
  ok  L-421: a missing named drawing ABORTs the build by name (fail: drawing 'hills_cloud' is named by a served feature but C:\Users\tonyq\AppData\Local\)

FAIL (233 checks, 1 failures)

  After you push: python gallery_maintenance_run.py --live

======================================================================
  DAILY RUN -- summary
======================================================================
  Guest book updater           ok
  Horizons check               ok
  Cache builder                ok
  Maintenance run, offline     reported a problem (exit 1)

  Look at: Maintenance run, offline -- scroll up to its own report.
  NEXT:
    1. GitHub Desktop: look at the change list, then commit and push.
    2. Then the dashboard's Gallery Maintenance Run -- live, AFTER a push.
======================================================================

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

5. Commit and push, -- e5a3d13f64ea493d8b5142e2d05e40030d483ac8
6. then run the live maintenance run from the dashboard.

======================================================================
MAINTENANCE RUN -- generators, then checkers (L-188)
======================================================================
  Provenance scan is current (last run 20261011T182057Z, 0 day(s) ago).

GENERATORS -- regenerate every time; a no-op when nothing moved
----------------------------------------------------------------------
  Ledger index                 1.3s  unchanged (1 of 1 rewritten, content
                                     identical)
  Skill manifest               0.2s  unchanged (1 of 1 rewritten, content
                                     identical)
  Constants export             0.8s  unchanged (1 checked, not written)
  Objects export               0.1s  unchanged (1 checked, not written)
  Drawings export              0.3s  unchanged (1 checked, not written)
  Module atlas                 5.9s  rewrote MODULE_ATLAS.md, MODULE_INDEX.md
  Data inventory               4.4s  rewrote DATA_INVENTORY.md
  Exact rows report            1.7s  rewrote EXACT_ROWS_PRINTED.md -- 13 of 38
                                     exact rows printed at 43 lines (33 orrery,
                                     10 gallery); 8 drawn only, 14 not followed,
                                     0 map entries broken
  Document index               0.2s  unchanged (1 checked, not written)

CHECKERS -- verdict informs the push call
----------------------------------------------------------------------
  Constants change             0.4s  No changes to constants_new.py since HEAD.
  Constants relations          0.4s  25 of 25 provenance tests passed against
                                     constants_new.py. No constants have drifted.
  Derived figures              1.2s  No figure count exceeds its inputs: 36
                                     derived row(s) read, 26 judged OK -- 26 OK,
                                     10 NOT YET MIGRATED, 1 NO DERIVED LINE, 1
                                     UNMARKED CONVERSION; 18 conversion(s)
                                     checked.
  Constants export check       2.3s  Export matches the store: sha256
                                     9d79d8797a22 on both sides; 120 rows
                                     re-read, 56 not exported, 29 tokens; 315
                                     conversions re-computed, 10 of 10 worked
                                     cases hold.
  Objects export check         0.1s  pass
  Skill headers                0.2s  12 skills parsed, no consistency problems.
  Exact rows by the count      1.9s  PASSING -- 13 printed exact rows each state
                                     a count; 33 orrery lines print through
                                     exact_text() or row_text(); 10 gallery lines
                                     are served the count
  Dimensions                   1.3s  No unit contradicts its arithmetic: 54
                                     derived row(s) read -- 42 OK, 9 NO UNIT, 3
                                     NOT CHECKABLE.
  Cross-check annotations      0.1s  19 of 19 cross-check annotation tests
                                     passed.
  Citation inheritance         0.1s  20 of 20 citation-inheritance tests passed.
  Status lines                 0.1s  All 119 status lines in constants_new.py are
                                     well formed; 54 rows carry none.
  Row shape                    0.1s  All 176 row shapes in constants_new.py fit
                                     the assignment's own line.
  Scanner recognition 1d/1e    0.2s  27 of 27 recognition pins hold: real
                                     citations recognized, fake ones refused.
  Scanner row run (L-414)      0.2s  16 of 16 pins hold -- each row reads its own
                                     comment run, declared rows are named, the
                                     gate path is read by name.
  Reset completeness          13.5s  PASS -- all 311 IntVars + 3 StringVars + 10
                                     entries reset to startup defaults; date set
                                     to now.
  Orbit cache                  1.9s  All 6 orbit cache tests passed: cache loads,
                                     old formats convert, corrupted entries are
                                     dropped.
  Earth pole of date           0.3s  all 14 checks passed (geometry, ERFA,
                                     fallback, cache, hover, transform).
  Hills cloud sampler (L-421)    0.5s  PASS -- 4 of 4 planted faults caught; the
                                     real rows pass, the dots' plane tilted 34.1
                                     deg
  Drawings export check        0.5s  PASS -- 3 of 3 planted faults caught;
                                     hills_cloud 3600 dots, tilt 30.9 deg, sha256
                                     a51e93118069
  Worksheet checker            9.5s  74 of 110 routed, 8 clean
  Worksheet checker tests     17.3s  All 135 checks passed
  Worksheet key round trip     1.0s  RESULT: 52 sites minted 52 distinct keys,
                                     all resolved; 52 pinned keys still resolve;
                                     1 retired keys confirmed gone.
  Builder marker join         20.9s  All 76 checks passed
  Extractor pins               0.5s  RESULT: 29 string sites carry the pinned 73
                                     claims and 14 instruction drops, at LOOKBACK
                                     30 / LOOKAHEAD 25, extractor version 2.
  Provenance scanner          11.8s  0 TIER-1 -- the push gate holds

======================================================================
  23 of 23 gating checkers passed -- 101.5s total
  2 report-only, exit 0 whatever they find:
    Worksheet checker           74 of 110 routed, 8 clean
    Provenance scanner          0 TIER-1 -- the push gate holds
======================================================================

FILES WRITTEN THIS RUN
----------------------------------------------------------------------
  2168 file(s) examined, 7 written, 0 created, 0 removed, 6 rewritten identically
    written   DATA_INVENTORY.md
    written   EXACT_ROWS_PRINTED.md
    written   MODULE_ATLAS.md
    written   MODULE_INDEX.md
    written   PROVENANCE_AUDIT.md
    written   data/provenance_history.json
    written   documentation/prompts/citation_review.jsonl
    rewritten with identical bytes, no action needed:
      LEDGER_CONSOLIDATED.md
      PROJECT_INSTRUCTIONS.md
      WORKSHEET_CHECK.md
      data/worksheet_check_state.json
      data/worksheet_routed.json
      test_output/test_orbit_paths.json
    20 file(s) over 2 MB compared by size and mtime only

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>

7. **The phone look.** Close the Home Screen clip's tab first, then open the Sun room upright:
   - Tick the Hills cloud and use Go To. You should see a disk tipped against the planets' plane, with the dots thickest along two opposite arms. -- correct
   - Tap its name. The text box should show three distances and "about 30 degrees". -- correct
   - Tick the clumps, then the tide. Both should start thin inside the Inner Oort Cloud sphere. -- correct
   - Tick Galactic Plane and turn the view until the ring is edge-on. Tap a pole marker, then open the i panel, which should say "60 degrees". -- correct

**How I checked it:** on copies of both repositories, the patches ran cleanly, a second time, and with Windows line endings. The gallery's maintenance run passed 27 of 27 after a simulated cache rebuild. The real Sun room page started with no errors and drew all 3,600 served dots, and ticking the Galactic Plane row drew it. The plane through the website's dots tilts 30.9 degrees, worked out twice by separate arithmetic. Without the drawing file, only the Hills cloud is missing and the page says why. Two things I couldn't run here: JPL's servers, so the real cache rebuild is yours, and a phone.

I'll do the closing records once you've looked: the ledger, your page, the new ledger item for the other dot shells, the dashboard buttons for the two new gallery tools, and ledger-and-session-records 1.20.

**Where this leaves us**
- Both halves of the inner Oort cloud are built and waiting for you to run them, with one clause to confirm.
- The closing records follow your phone look.

The check flagged uncommitted changes in my working copies here again. I deleted the throwaway test copies, and I'm deliberately not committing or pushing the rest.

What's left are my working copies of the orrery and the gallery. They hold the same changes as your two patches, and I keep them as the reference for the closing records. You hold commit authority on both repositories, so nothing reaches GitHub except through your runs and your pushes in GitHub Desktop.

Nothing has changed for you. The one open question is still whether the panel-note wording "picked where the model's orbits lie (its Fig. 3)" is all right.

===========================================================

One check failed on your machine. Let me read the rest of the record before saying why.

First I'll reproduce your failure here by giving the stand-in Windows line endings, as text mode does on your machine.

234 checks pass. Packaging this as the gallery patch, then testing it.

Gallery fix saved. Now the orrery closing records. First the ledger items this session touches.

Now the parts of the ledger skill this version changes.

I'll leave the run-record zone question owed on L-351, as it stands, and keep this version to the rule you named. Now the dashboard's gallery buttons.

Whole tree reads 292 Tier-1, gate path 0. Now I'll write the closing edits as one list, apply them to my copy, and build the patch from that same list.

Now the ledger edits. First the exact text at each anchor.

Now your page, edited by section.

Now the build record, with both folders in its header.

Now the close patch itself: the edit list, the new record, and a step that renumbers the new item if the other session took 434 first.

Now testing it on a clean copy of the orrery at your push, then the full maintenance run there.

132 lines above the marker, over your 130 cap. I'll drop the oldest settled line (gray90, Oct 6, a habit now) and fold the two "needs you" bullets into one.

129 lines. Now the full maintenance run on that copy: it rewrites the skill's read plan, its manifest row and the ledger's index.

The close is ready, and both patches are saved in your folders.

The one red line in your Daily Run (26 of 27) was a mistake in my check, not in the website. On Windows the check saved its practice copy of the drawing with Windows line endings. The cache builder then correctly served it with plain line endings, so the two copies didn't match byte for byte. The gallery patch fixes the check and adds a new one that confirms a drawing saved with Windows line endings still comes out right.

**Your steps, in order:**

1. **Gallery folder:**
   1. Run `patch_L421_8_suite_line_endings_20261011.py`.

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/patch_L421_8_suite_line_endings_20261011.py
ok  tools/test_gallery_cache_builder_offline.py    4 edit(s)

stamps updated: the module header of tools/test_gallery_cache_builder_offline.py
patch applied: 1 file(s) edited, 0 created.

NEXT:
  1. Run gallery_maintenance_run.py. Expect "Cache builder suite ... PASS (234
     checks, 0 failures)" and "27 of 27 gating checkers passed".

======================================================================
  gallery maintenance run -- OFFLINE (before a commit)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

GENERATORS -- rewritten every time; a no-op when nothing moved
  PASS Module atlas              1.3s  rewrote MODULE_ATLAS.md,
                                    MODULE_INDEX.md
  PASS Constants export pull     0.8s  no change to
                                    data/constants_export.json,
                                    data/constants_export.sha
  PASS Config mirror             0.1s  no change to
                                    data/objects_config.json
  PASS Objects export pull       0.6s  no change to
                                    data/objects_export.json,
                                    data/objects_export.sha
  PASS Objects mirror            0.1s  no change to
                                    data/objects_config.json
  PASS Drawings pull             0.6s  no change to
                                    data/drawings/hills_cloud.json,
                                    data/drawings/pulled_at.sha

CHECKERS -- the verdict informs the push call
  PASS Cache builder suite      15.8s  PASS (234 checks, 0 failures)
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
  PASS Store writer suite        8.5s  All 329 store-writer checks
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
  PASS Store editor suite        0.2s  All 312 store-editor checks
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
                                    count; 112 link(s) compared, store
                                    9d79d8797a22.
  PASS Horizons check suite      0.3s  HORIZONS CHECK SUITE: pass
  PASS Horizons confirmations    0.1s  HORIZONS CONFIRMATIONS: pass -- 13
                                    of 13 confirmed within 30 days
  PASS Pointer join              0.1s  Every link is accounted for: 119
                                    link(s) against orrery 1bbd9fe1, 4
                                    fallback named; read check: 43 of
                                    43 measured rows reached carry a
                                    read.
  PASS Cache in step             0.1s  The served cache holds the
                                    config's 19 object(s) and their
                                    features exactly: 4 object(s) with
                                    36 named shell(s), in both cache
                                    files.
  PASS Drawings                  0.2s  DRAWINGS: PASS -- 3 of 3 planted
                                    faults caught; pulled at orrery
                                    1bbd9fe1; hills_cloud 3600 dots,
                                    tilt 30.9 deg, sha256 a51e93118069
  PASS Collapsed features        0.1s  34 stored as themselves, 16
                                    collapsed, 0 unclassified.
  PASS Feature renderers         1.0s  === ALL CHECKS PASSED ===
  PASS Page framing              0.2s  === ALL CHECKS PASSED ===
  PASS Sun shells                0.3s  ALL CHECKS PASSED
  PASS Earth scene geometry      0.2s  === ALL CHECKS PASSED ===
  PASS Hover budget              0.2s  === ALL CHECKS PASSED ===
  PASS Arrival                   0.2s  Arrival: both rooms open on the
                                    right things; every shell trace
                                    carries its key; the fallback with
                                    no arrival block is unchanged.
  PASS Display figures           0.2s  === PASS: 61 hover(s) and 318
                                    number(s) examined; 13 graded, 7
                                    graded by line, 48 held to the
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
  PASS Guest book updater        0.3s  === GUEST BOOK UPDATER: all 43
                                    checks passed (6 scripted runs,
                                    self-test first)
  PASS Daily run steps           0.1s  === DAILY RUN: all 4 step scripts
                                    found
  PASS Artifact 1 assembler      0.2s  === ALL CHECKS PASSED -- 5
                                    verdicts and T3's feature set
                                    match the 2026-08-31 pin ===
  PASS Cache siblings            0.1s  RESULT: no sibling directories and
                                    nothing in data/ the builder did
                                    not make.

======================================================================
  27 of 27 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Cache siblings         RESULT: no sibling directories and
  last swap 2026-10-11T18:38:49.683340+00:00: succeeded first time
======================================================================

  After you push: python gallery_maintenance_run.py --live

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  2. Move this script, and patch_L421_7_oort_gallery_20261011.py if it is
     still in the root, into documentation/; commit and push. -- e3536c8732d7b62faa5c09515e4b7f1d1c10af9c
  3. After the push: the dashboard's Gallery Maintenance Run -- live.

======================================================================
  gallery maintenance run -- LIVE (after a push)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

LIVE -- what the deployed site actually serves

  fetching 16 files from https://palomasorrery.com/
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
    SERVED   data/solar-system/drawings/hills_cloud.json    matches the working copy

  PASS Served reachability       3.7s  all 16 files served and
                                    byte-identical to the working copy

  orrery export pinned at 1bbd9fe1

  PASS Export freshness          0.1s  the served export is the orrery's
                                    at 1bbd9fe1, byte for byte

  orrery HEAD 1bbd9fe1
  examining 7 of 119 links; the other 112 are served from the export
    NOT IN STORE  planet_poles['Sun']              not a top-level constant in the store
                  /objects/0/features/orientation
    NOT IN STORE  planet_poles['Jupiter']          not a top-level constant in the store
                  /objects/2/features/orientation/pole
    NOT IN STORE  planet_poles['Saturn']           not a top-level constant in the store
                  /objects/3/features/orientation/pole
  7 pointers: 4 match, 0 DRIFT, 0 UNIT MISMATCH, 3 could not be examined.

  PASS Store drift               1.2s  7 pointers against orrery 1bbd9fe1
                                    -- 4 match, 0 DRIFT, 0 UNIT
                                    MISMATCH, 3 could not be examined.

======================================================================
  2 of 2 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Store drift            7 pointers against orrery 1bbd9fe1 -- 4
  last swap 2026-10-11T18:38:49.683340+00:00: succeeded first time
======================================================================

  Offline pass: python gallery_maintenance_run.py

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> 

   2. Run `gallery_maintenance_run.py`. You should see "234 checks" and "27 of 27".
   3. Move that patch and `patch_L421_7` into `documentation/`.
   4. Commit and push, then do the live run.
2. **Orrery folder:**
   1. Run `patch_L421_9_close_20261011.py`.

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/patch_L421_9_close_20261011.py
ok  skills/ledger-and-session-records/SKILL.md     version line 1.20
ok  skills/ledger-and-session-records/SKILL.md     the v1.17 entry moves out
ok  skills/ledger-and-session-records/SKILL.md     Anchor Requirement: the folders line
ok  skills/ledger-and-session-records/SKILL.md     Tony's Local Folders: the header
ok  skills/ledger-and-session-records/SKILL.md     Handoff Structure: the folders bullet
ok  documentation/SKILL_HISTORIES.md               receives the ledger skill's v1.17 entry
ok  PROJECT_INSTRUCTIONS.md                        header stamp
ok  PROJECT_INSTRUCTIONS.md                        SHA anchor
ok  PROJECT_INSTRUCTIONS.md                        v3.91 entry
ok  PROJECT_INSTRUCTIONS.md                        v3.88 moves out
ok  documentation/PROJECT_INSTRUCTIONS_HISTORY.md  receives v3.88
ok  palomas_orrery_dashboard.py                    stamp
ok  palomas_orrery_dashboard.py                    gallery: Drawings Check and Drawings Pull
ok  palomas_orrery_dashboard.py                    offline runner's description names both
ok  palomas_orrery_dashboard.py                    offline runner's description: the drawings check
ok  LEDGER_CONSOLIDATED.md                         header stamp
ok  LEDGER_CONSOLIDATED.md                         L-421: the website half
ok  LEDGER_CONSOLIDATED.md                         L-421: Ref
ok  LEDGER_CONSOLIDATED.md                         L-434 opened
ok  LEDGER_CONSOLIDATED.md                         L-408 closed
ok  LEDGER_CONSOLIDATED.md                         L-408: built and looked at
ok  LEDGER_CONSOLIDATED.md                         L-412 receives the tide question
ok  LEDGER_CONSOLIDATED.md                         L-412 date
ok  LEDGER_CONSOLIDATED.md                         L-363 (b) fixed
ok  LEDGER_CONSOLIDATED.md                         L-363 date
ok  LEDGER_CONSOLIDATED.md                         L-239: the Hills cloud seeded
ok  LEDGER_CONSOLIDATED.md                         L-239 date
ok  LEDGER_CONSOLIDATED.md                         L-351: the folders rule landed at 1.20
ok  LEDGER_CONSOLIDATED.md                         L-416: the gallery two
ok  documentation/WHERE_WE_ARE.md                  date line
ok  documentation/WHERE_WE_ARE.md                  written at
ok  documentation/WHERE_WE_ARE.md                  the box: last close's line
ok  documentation/WHERE_WE_ARE.md                  the box: last close's line
ok  documentation/WHERE_WE_ARE.md                  the box: last close's line
ok  documentation/WHERE_WE_ARE.md                  the box: last close's line
ok  documentation/WHERE_WE_ARE.md                  the box: last close's line
ok  documentation/WHERE_WE_ARE.md                  the box: changed
ok  documentation/WHERE_WE_ARE.md                  the box: needs you
ok  documentation/WHERE_WE_ARE.md                  road stage 6
ok  documentation/WHERE_WE_ARE.md                  road: last close's mark
ok  documentation/WHERE_WE_ARE.md                  settled: stored drawings
ok  documentation/WHERE_WE_ARE.md                  settled: a habit now
ok  documentation/WHERE_WE_ARE.md                  settled: a habit now
ok  documentation/WHERE_WE_ARE.md                  signals: cache build
ok  documentation/WHERE_WE_ARE.md                  signals: Tier-1
ok  documentation/WHERE_WE_ARE.md                  waiting: the tide question
ok  documentation/WHERE_WE_ARE.md                  where the details are: open for build
ok  documentation/WHERE_WE_ARE.md                  where the details are: the website record
ok  documentation/HANDOFF_L421_oort_gallery_20261011.md created
note: WHERE_WE_ARE.md has 129 lines above the run-record marker (the cap is 130)
the new item is L-434
stamps updated: the ledger header; the skill's version line; PROJECT_INSTRUCTIONS.md header and anchor; the dashboard's docstring; WHERE_WE_ARE.md date line
patch applied: 48 edits in 7 files, and the build record.

NEXT:
  1. Run orrery_maintenance_run.py. Expect "23 of 23 gating checkers
     passed" and "0 TIER-1 -- the push gate holds". It rewrites the
     skill's read plan, its manifest row (1.20) and the ledger's index.
  2. Move this script, and patch_L421_6 if it is still in the root, into
     documentation/; commit and push.
  3. Upload skills/ledger-and-session-records/SKILL.md (Settings > Skills),
     and replace the Project's instructions with PROJECT_INSTRUCTIONS.md
     (now v3.91).
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 

   2. Run `orrery_maintenance_run.py`. You should see "23 of 23".

======================================================================
MAINTENANCE RUN -- generators, then checkers (L-188)
======================================================================
  Provenance scan is current (last run 20261011T184520Z, 0 day(s) ago).

GENERATORS -- regenerate every time; a no-op when nothing moved
----------------------------------------------------------------------
  Ledger index                 2.3s  rewrote LEDGER_CONSOLIDATED.md
  Skill manifest               0.3s  rewrote PROJECT_INSTRUCTIONS.md
  Constants export             1.2s  unchanged (1 checked, not written)
  Objects export               0.1s  unchanged (1 checked, not written)
  Drawings export              0.6s  unchanged (1 checked, not written)
  Module atlas                10.4s  rewrote MODULE_ATLAS.md, MODULE_INDEX.md
  Data inventory               6.3s  rewrote DATA_INVENTORY.md
  Exact rows report            2.6s  unchanged (1 checked, not written) -- 13 of
                                     38 exact rows printed at 43 lines (33
                                     orrery, 10 gallery); 8 drawn only, 14 not
                                     followed, 0 map entries broken
  Document index               0.2s  unchanged (1 checked, not written)

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
  Constants export check       2.0s  Export matches the store: sha256
                                     9d79d8797a22 on both sides; 120 rows
                                     re-read, 56 not exported, 29 tokens; 315
                                     conversions re-computed, 10 of 10 worked
                                     cases hold.
  Objects export check         0.2s  pass
  Skill headers                0.3s  12 skills parsed, no consistency problems.
  Exact rows by the count      2.3s  PASSING -- 13 printed exact rows each state
                                     a count; 33 orrery lines print through
                                     exact_text() or row_text(); 10 gallery lines
                                     are served the count
  Dimensions                   1.6s  No unit contradicts its arithmetic: 54
                                     derived row(s) read -- 42 OK, 9 NO UNIT, 3
                                     NOT CHECKABLE.
  Cross-check annotations      0.2s  19 of 19 cross-check annotation tests
                                     passed.
  Citation inheritance         0.2s  20 of 20 citation-inheritance tests passed.
  Status lines                 0.1s  All 119 status lines in constants_new.py are
                                     well formed; 54 rows carry none.
  Row shape                    0.1s  All 176 row shapes in constants_new.py fit
                                     the assignment's own line.
  Scanner recognition 1d/1e    0.4s  27 of 27 recognition pins hold: real
                                     citations recognized, fake ones refused.
  Scanner row run (L-414)      0.4s  16 of 16 pins hold -- each row reads its own
                                     comment run, declared rows are named, the
                                     gate path is read by name.
  Reset completeness          28.2s  PASS -- all 311 IntVars + 3 StringVars + 10
                                     entries reset to startup defaults; date set
                                     to now.
  Orbit cache                  3.4s  All 6 orbit cache tests passed: cache loads,
                                     old formats convert, corrupted entries are
                                     dropped.
  Earth pole of date           0.5s  all 14 checks passed (geometry, ERFA,
                                     fallback, cache, hover, transform).
  Hills cloud sampler (L-421)    0.7s  PASS -- 4 of 4 planted faults caught; the
                                     real rows pass, the dots' plane tilted 34.1
                                     deg
  Drawings export check        0.6s  PASS -- 3 of 3 planted faults caught;
                                     hills_cloud 3600 dots, tilt 30.9 deg, sha256
                                     a51e93118069
  Worksheet checker           12.6s  74 of 110 routed, 8 clean
  Worksheet checker tests     22.3s  All 135 checks passed
  Worksheet key round trip     1.5s  RESULT: 52 sites minted 52 distinct keys,
                                     all resolved; 52 pinned keys still resolve;
                                     1 retired keys confirmed gone.
  Builder marker join         32.5s  All 76 checks passed
  Extractor pins               0.6s  RESULT: 29 string sites carry the pinned 73
                                     claims and 14 instruction drops, at LOOKBACK
                                     30 / LOOKAHEAD 25, extractor version 2.
  Provenance scanner          15.1s  0 TIER-1 -- the push gate holds

======================================================================
  23 of 23 gating checkers passed -- 151.4s total
  2 report-only, exit 0 whatever they find:
    Worksheet checker           74 of 110 routed, 8 clean
    Provenance scanner          0 TIER-1 -- the push gate holds
======================================================================

FILES WRITTEN THIS RUN
----------------------------------------------------------------------
  2170 file(s) examined, 9 written, 0 created, 0 removed, 4 rewritten identically
    written   DATA_INVENTORY.md
    written   LEDGER_CONSOLIDATED.md
    written   MODULE_ATLAS.md
    written   MODULE_INDEX.md
    written   PROJECT_INSTRUCTIONS.md
    written   PROVENANCE_AUDIT.md
    written   WORKSHEET_CHECK.md
    written   data/provenance_history.json
    written   skills/ledger-and-session-records/SKILL.md
    rewritten with identical bytes, no action needed:
      data/worksheet_check_state.json
      data/worksheet_routed.json
      documentation/prompts/citation_review.jsonl
      test_output/test_orbit_paths.json
    20 file(s) over 2 MB compared by size and mtime only

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>

   3. Move the patch, and `patch_L421_6` if it's still in the main folder, into `documentation/`.
   4. Commit and push. -- f7c6f41d1b6a0931fd0c369c30c8e8867712b214
3. **Settings:**
   - Upload `skills/ledger-and-session-records/SKILL.md`, which is now version 1.20, in Settings > Skills. -- done
   - Replace the Project instructions with `PROJECT_INSTRUCTIONS.md`, which is now v3.91. -- done

**Where this leaves us:**
- The website now draws the Hills cloud from the orrery's own 3,600 dots. The clumps and the galactic tide fade in between 10,000 and 20,000 AU. The galactic plane is live, and the galactic plane task (L-408) is done.
- The dashboard has two new buttons in the gallery group, "Drawings Pull" and "Drawings Check", beside the orrery's two drawing buttons.
- New ledger item L-434 covers storing drawings for the other dotted shapes: the streamer band, the clumps and the tide.
- From now on, every handoff, brief and design record names your two local folders at the top. Today's build record does this already.
- The next session should confirm that it loaded version 1.20 of the ledger-and-session-records skill before it does any ledger or handoff work.

The build record is `documentation/HANDOFF_L421_oort_gallery_20261011.md`. The orrery patch writes it into the repo.

I'm not committing or pushing, and nothing is lost by leaving it that way. The uncommitted changes are on my test copy of the orrery in the session workspace, where I tried the close patch before handing it to you. That copy isn't your repository, and you're the only one who commits and pushes.

The real changes reach GitHub when you run `patch_L421_9_close_20261011.py` in your orrery folder and push it yourself.



