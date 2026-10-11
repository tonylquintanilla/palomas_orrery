<!-- Doc-Kind: hand | Where the project is and where it is going, in plain words. One file, edited by section; Tony's run record sits below the marker at the end and no patch edits it. -->
# Where We Are

Last updated: October 10, 2026, at the lobby's third round.
- Written at orrery a6678b0 and gallery cb9038c, before your runs.

> **READ THIS FIRST**
>
> **Changed since you last read this:**
> - L-429 (the room button on the row): Go To sits in the middle of
>   every room's list, the room button after it; long names wrap.
> - Artifact 1 passes again; the Daily Run no longer pauses OneDrive.
>   L-428 (the lobby's way in) is closed.
>
> **Do next:** *as you confirmed: the typed facts (the inner Oort
> cloud, then the check); the Horizons check build; the Sun's list
> from item 3.*
>
> **Needs you now:**
> - *Gallery: run patch_L429_3, the maintenance run, push; look on the
>   phone. Orrery: run patch_L429_4, the maintenance run, push.*
> - Upload interactive-exhibit (1.14) and gallery-cache-builder (1.8);
>   the Project's instructions to v3.89.
> - *Decide L-425 (citation location checks): which checks to build,
>   on the run's results (on L-425 and in the handoff).*

*Italic* lines are the must-reads. Marks reset at every update.

## The road

  1-4. [done]  The Sun, Earth and Solar System rooms are live; the orrery
               feeds the website and nothing is typed twice.
  5.   [NOW]   *Earth's old items are finished, in your order.* The
               website patch and Earth's typed facts are live.
  6.   [next]  The typed facts: 15 of 17 served. Left: the inner Oort
               cloud, redrawn tilted, and the check.
  7.   [next]  The Sun's numbers get the checking Earth's got.
  8.   [next]  The served objects are checked against JPL Horizons.
               Designed and recorded; build next, with Encke added
               and Halley checked too.
  9.   [next]  The website's checks, in the order you confirmed:
               L-423 (the website's checks).
 10.   [next]  A bare interactive.html link opens the Solar System room;
               the Explorer gets its own address.
 11.   [later] The rest of the orrery's objects come to the website.
 12.   [later] Encounters: comets and spacecraft at the dates that matter.
 13.   [later] The planets get their details, Jupiter and Saturn first.
 14.   [later] The Earth System layers; the gallery's cards meanwhile.
 15.   [goal]  The website does what the desktop orrery does, with a date
               to choose, within the range the data covers.
-- a couple of things to keep in mind. before we close the sun and earth rooms, i would like to implement fuzzy boundaries. and in the last session we found something important. the orbital periods dictionary is hand maintained and instead should be fetched from Horizons along with the other osculating data. however, there is a wrinkle: the center body for the data matters: the sun or the solar barycenter. we should also implement this because it matters for orbital periods, especially highly perturbed ones. 
-- the near term goal is to complete the sun and earth room thoroughly as a template for other body rooms. then add the symbols for most if not all the orrery's objects list. then we can decide on priorities. the "golden artifacts" are one path, but not the only one. I would be inclined to work on the inner planets after that. and we should not forget the earth science part. 


## Settled  **>> UPDATED THIS SESSION**

Standing rulings. A line leaves after a few weeks, once it is habit.
- The lobby opens on the Solar System room, then the subjects. Every
  room's list: Go To in the middle, then the room's button. (Oct 10)
- A row's sources come only from its own comment block. (Oct 9)
- Small fixes owed to a skill ride the version a session is already
  making; a change to a checker gets its own session. (Oct 8)
- A long skill gets its reading plan at its next version, not in a
  bump of its own. (Oct 8)
- The galactic tide keeps its cone, to show its pull as physics. (Oct 7)
- No colour or other name that only one system knows. The panels'
  grey is one name, gray90. (Oct 6)
- The daily hand run stays a hand run. (Oct 7)
- OneDrive: no pause before a build; the retry is sufficient, and the
  swap log shows any retry. Empty "solar-system (N)" folders are
  harmless; delete by hand. (Oct 8, Oct 10)
- An object's words in the list carry no numbers unless they come
  from the store. (Oct 8)
- Items in an ordered list carry no RICE score. (Oct 7)
- Every ledger handle on this page carries a short label. (Oct 7)
- Code types only words about our picture; facts are served. (Oct 6)
- The inner Oort cloud is redrawn from the 2025 paper now, as part of
  the Sun's slice, not deferred. (Oct 6)
-- something to keep in mind. the color dictionary is a drawing choice and kept by hand. the default color is often goldenrod, but we should switch it up to avoid clashing with nearby objects. small, but it matter for the render. 
-- since we are using cowork, the location of the local files should be included in the handoff header along with the github info. this has already been added to the skill. 
-- another cowork glitch: if i have already downloaded a design document or handoff to documentations/ and the patch creates it again, the patch will refuse. i have to go back and delete the download, then the patch runs. 
-- add new checks to the dashboard. this should be part of the skill. 


## Signals  **>> UPDATED THIS SESSION**

Read from files when this page was written, not typed from memory.
- Last cache build: 20261010T135737Z, ok, no retry.
- Tier-1 on the gate path: 0, by name, in PROVENANCE_AUDIT.md at
  a6678b0. Whole tree: 293.
- This page's date and the ledger's newest stamp: both Oct 10. Agree.

## Waiting on you

At the next design talk:
- The fuzzy outer corona, with the dust cloud; the exosphere the same way.
- Moving the highlighted row to the top of the list.
- GO's arrow, only if the text box stays centred.
- Earth's design talks, the belts' shape first.
- Whether the phone's Sun room gets the galactic plane, its poles,
  Sgr A* and the tide's cone: L-408 (the galactic plane on the phone).
  You: "awaits the design talk." (Oct 7) -- yes. it awaited only for implementation not in principle. 
- The inner Oort cloud's tilted disk: its words, and whether its outer
  edge moves from 20,000 au to the paper's 10,000. -- i think this is settled. and we opted for a fuzzy boundary. please check.

Decisions, one at a time:
- L-424 (the checker's one word for two cases): whether the
  checker itself prints two different words. -- unclear

Not urgent, in your order:
1. Whether the editor also edits the Solar System room's rows.
2. Choosing a date, and animation.
3. The scattered disk, with the Kuiper belt. Not the fuzzy-boundary idea. -- we should decide this. i lean yes. 

## Where the details are  **>> UPDATED THIS SESSION**

- The lobby, the room button: L-428, L-429; `HANDOFF_L429_round3_20261010.md`
- Scanner window: L-414 (the scanner's window), L-427 (rows a neighbour
  had credited); `documentation/HANDOFF_L414_scanner_window_20261009.md`
- The Oct 8 decisions: `documentation/HANDOFF_decisions_20261008.md`.
  The new list: L-423 (the website's checks).
- Every item: `LEDGER_CONSOLIDATED.md`. The Fable sweep: L-422 (the ledger
  skill at 1.17 and this page), L-001 (the Earth System track), L-071
  and L-077 (the 2026 heat domes, closed), L-216 (the swap retry and
  the hand run), L-412 (the RICE ruling), L-395 (the Horizons check,
  designed). Open for build: L-421 (the typed facts).
- The typed facts: plan
  `documentation/MANIFEST_L421_typed_facts_20261006.md`; record
  `documentation/HANDOFF_L421_typed_facts_20261008.md`
- The Horizons check design:
  `documentation/DESIGN_L395_horizons_check_20261007.md`
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

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

**Session: OPEN: 10-10-26 1749: Opus: L-421 orrery build session**

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/patch_L395_7_records_20261010.py
ok  LEDGER_CONSOLIDATED.md                           header stamp
ok  LEDGER_CONSOLIDATED.md                           L-414 closed
ok  LEDGER_CONSOLIDATED.md                           L-414 status
ok  LEDGER_CONSOLIDATED.md                           L-395 date
ok  LEDGER_CONSOLIDATED.md                           L-395 the build and its first live run
ok  LEDGER_CONSOLIDATED.md                           L-395 Ref
ok  palomas_orrery_dashboard.py                      stamp
ok  palomas_orrery_dashboard.py                      Daily Run: words
ok  palomas_orrery_dashboard.py                      Daily Run: the Horizons Check button
ok  palomas_orrery_dashboard.py                      cache builder: the routine without the pause
ok  palomas_orrery_dashboard.py                      Daily Run group: the maintenance run is step 4
ok  palomas_orrery_dashboard.py                      offline runner names the two Horizons rows
ok  palomas_orrery_dashboard.py                      Objects Export: the two new fields
ok  palomas_orrery_dashboard.py                      Daily Run Steps: four scripts
ok  palomas_orrery_dashboard.py                      gallery checks: the two Horizons buttons
ok  skills/ledger-and-session-records/SKILL.md       version line 1.19
ok  skills/ledger-and-session-records/SKILL.md       the v1.16 entry moves out
ok  skills/ledger-and-session-records/SKILL.md       older-entries line
ok  skills/ledger-and-session-records/SKILL.md       contents: the new heading
ok  skills/ledger-and-session-records/SKILL.md       Tony's Local Folders
ok  skills/horizons-orbital-mechanics/SKILL.md       version line 1.2
ok  skills/horizons-orbital-mechanics/SKILL.md       pinning: Encke's pin in the list
ok  skills/horizons-orbital-mechanics/SKILL.md       Checking an Entry Against JPL
ok  PROJECT_INSTRUCTIONS.md                          header stamp
ok  PROJECT_INSTRUCTIONS.md                          SHA anchor
ok  PROJECT_INSTRUCTIONS.md                          v3.90 entry
ok  PROJECT_INSTRUCTIONS.md                          v3.87 moves out
ok  documentation/PROJECT_INSTRUCTIONS_HISTORY.md    receives v3.87
ok  documentation/SKILL_HISTORIES.md                 receives the ledger skill's v1.16 entry
ok  documentation/WHERE_WE_ARE.md                    date line
ok  documentation/WHERE_WE_ARE.md                    the box
ok  documentation/WHERE_WE_ARE.md                    road stage 8
ok  documentation/WHERE_WE_ARE.md                    settled: the comets' names
ok  documentation/WHERE_WE_ARE.md                    signals
ok  documentation/WHERE_WE_ARE.md                    where the details are
ok  documentation/WHERE_WE_ARE.md                    where the details are: the Horizons check
ok  documentation/WHERE_WE_ARE.md                    where the details are: the build record
ok  v3.87 moved to the history, word for word
ok  ledger-and-session-records v1.16 moved, word for word
ok  documentation/HANDOFF_L395_horizons_check_build_20261010.md created
note: WHERE_WE_ARE.md has 130 lines above the run-record marker (the cap is 130)
stamps updated: the ledger header; both skills' version lines; PROJECT_INSTRUCTIONS.md header and anchor; the dashboard's docstring; WHERE_WE_ARE.md date line
patch applied: 37 edits in 8 files, and the build record.

NEXT:
  1. Run orrery_maintenance_run.py -- it writes both skills' manifest rows and the ledger skill's read plan, and rebuilds the ledger's index. Expect 21 of 21.

======================================================================
MAINTENANCE RUN -- generators, then checkers (L-188)
======================================================================
  Provenance scan is current (last run 20261010T213809Z, 1 day(s) ago).

GENERATORS -- regenerate every time; a no-op when nothing moved
----------------------------------------------------------------------
  Ledger index                 1.3s  rewrote LEDGER_CONSOLIDATED.md
  Skill manifest               0.2s  rewrote PROJECT_INSTRUCTIONS.md
  Constants export             0.7s  rewrote data/constants_export.json
  Objects export               0.1s  unchanged (1 checked, not written)
  Module atlas                 6.2s  rewrote MODULE_ATLAS.md, MODULE_INDEX.md
  Data inventory               4.3s  rewrote DATA_INVENTORY.md
  Exact rows report            1.7s  rewrote EXACT_ROWS_PRINTED.md -- 13 of 38
                                     exact rows printed at 43 lines (33 orrery,
                                     10 gallery); 8 drawn only, 11 not followed,
                                     0 map entries broken
  Document index               0.1s  unchanged (1 checked, not written)

CHECKERS -- verdict informs the push call
----------------------------------------------------------------------
  Constants change             0.3s  0 removal verdict(s) cross-checked against
                                     the 176 name(s) the working copy assigns
  Constants relations          0.2s  25 of 25 provenance tests passed against
                                     constants_new.py. No constants have drifted.
  Derived figures              0.8s  No figure count exceeds its inputs: 36
                                     derived row(s) read, 26 judged OK -- 26 OK,
                                     10 NOT YET MIGRATED, 1 NO DERIVED LINE, 1
                                     UNMARKED CONVERSION; 18 conversion(s)
                                     checked.
  Constants export check       1.6s  Export matches the store: sha256
                                     9d79d8797a22 on both sides; 120 rows
                                     re-read, 56 not exported, 29 tokens; 315
                                     conversions re-computed, 10 of 10 worked
                                     cases hold.
  Objects export check         0.1s  pass
  Skill headers                0.2s  12 skills parsed, no consistency problems.
  Exact rows by the count      1.8s  PASSING -- 13 printed exact rows each state
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
  Scanner recognition 1d/1e    0.4s  27 of 27 recognition pins hold: real
                                     citations recognized, fake ones refused.
  Scanner row run (L-414)      0.4s  16 of 16 pins hold -- each row reads its own
                                     comment run, declared rows are named, the
                                     gate path is read by name.
  Reset completeness          15.9s  PASS -- all 311 IntVars + 3 StringVars + 10
                                     entries reset to startup defaults; date set
                                     to now.
  Orbit cache                  1.7s  All 6 orbit cache tests passed: cache loads,
                                     old formats convert, corrupted entries are
                                     dropped.
  Earth pole of date           0.3s  all 14 checks passed (geometry, ERFA,
                                     fallback, cache, hover, transform).
  Hills cloud sampler (L-421)    0.5s  PASS -- 4 of 4 planted faults caught; the
                                     real rows pass, the dots' plane tilted 34.1
                                     deg
  Worksheet checker            9.2s  74 of 110 routed, 8 clean
  Worksheet checker tests     14.8s  All 135 checks passed
  Worksheet key round trip     1.0s  RESULT: 52 sites minted 52 distinct keys,
                                     all resolved; 52 pinned keys still resolve;
                                     1 retired keys confirmed gone.
  Builder marker join         19.9s  All 76 checks passed
  Extractor pins               0.4s  RESULT: 29 string sites carry the pinned 73
                                     claims and 14 instruction drops, at LOOKBACK
                                     30 / LOOKAHEAD 25, extractor version 2.
  Provenance scanner           9.6s  0 TIER-1 -- the push gate holds

======================================================================
  22 of 22 gating checkers passed -- 95.4s total
  2 report-only, exit 0 whatever they find:
    Worksheet checker           74 of 110 routed, 8 clean
    Provenance scanner          0 TIER-1 -- the push gate holds
======================================================================

FILES WRITTEN THIS RUN
----------------------------------------------------------------------
  2156 file(s) examined, 13 written, 0 created, 0 removed, 3 rewritten identically
    written   DATA_INVENTORY.md
    written   EXACT_ROWS_PRINTED.md
    written   LEDGER_CONSOLIDATED.md
    written   MODULE_ATLAS.md
    written   MODULE_INDEX.md
    written   PROJECT_INSTRUCTIONS.md
    written   PROVENANCE_AUDIT.md
    written   WORKSHEET_CHECK.md
    written   data/constants_export.json
    written   data/provenance_history.json
    written   documentation/prompts/citation_review.jsonl
    written   module_atlas.py
    written   skills/ledger-and-session-records/SKILL.md
    rewritten with identical bytes, no action needed:
      data/worksheet_check_state.json
      data/worksheet_routed.json
      test_output/test_orbit_paths.json
    20 file(s) over 2 MB compared by size and mtime only

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>

  2. Move this script into documentation/; commit and push. -- 9f1547821a1957544f0ae94a77cc64c5a3ab4114
  3. Upload the two skills' SKILL.md (Settings > Skills): ledger-and-session-records and horizons-orbital-mechanics; and replace the Project's instructions with PROJECT_INSTRUCTIONS.md (now v3.90). -- done
  4. The Mode 5 look at Encke and Halley in the orrery window, when you like: four checks in the build record. 
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 

These are the four checks from last session's build record (section 6 of documentation/HANDOFF_L395_horizons_check_build_20261010.md):

1. **The checkbox and its tooltip.** Under Comets, just below Halley, there is a new checkbox: "Encke (1786-present, periodic)". Hover over it. The tooltip should read "Horizons: 2P/Encke. A short-period comet whose dust trail is the source of the Taurid meteor showers." and "Perihelion: October 22, 2023". -- correct. could you reorder to put Encke at the top of the list? i order the comets by date of first apparition by this Horizons Id. 

2. **Encke draws.** Tick only Encke, centre on the Sun, set today's date, and plot. You should see its marker, its orbit and its tail. The marker is goldenrod, the default colour, because Encke has no colour of its own yet. Giving it one is a one-line change in constants_new.py, if you want it. -- correct. there is a color dictionary, which is mostly a drawing choice to distinguish objects commonly drawn together. 

3. **Its perihelion button.** Under Encke, use "Go: Perihelion". The view should jump to Encke's October 2023 perihelion. This one needs the internet, so it couldn't be tested in the sandbox. -- correct. the only missing data is the orbital period, which is available from Horizons. this information is in it's own dictionary. please discuss best approaches going forward. 

4. **Halley's hover.** Plot Halley and hover over it. It should show its new words and a link to NASA's 1P/Halley page. -- correct

===============================================================================

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/patch_L421_5_oort_orrery_20261010.py
ok  constants_new.py                   line 2389
ok  constants_new.py                   line 2355
ok  constants_new.py                   line 150
ok  constants_tokens.py                line 247
ok  constants_tokens.py                line 89
ok  idealized_orbits.py                line 3306
ok  idealized_orbits.py                line 33
ok  orrery_maintenance_run.py          line 275
ok  orrery_maintenance_run.py          line 159
ok  orrery_maintenance_run.py          line 89
ok  palomas_orrery.py                  line 9196
ok  palomas_orrery.py                  line 64
ok  solar_visualization_shells.py      line 1709
ok  solar_visualization_shells.py      line 1695
ok  solar_visualization_shells.py      line 1642
ok  solar_visualization_shells.py      line 1600
ok  solar_visualization_shells.py      line 1589
ok  solar_visualization_shells.py      line 1569
ok  solar_visualization_shells.py      line 1559
ok  solar_visualization_shells.py      line 1550
ok  solar_visualization_shells.py      line 1543
ok  solar_visualization_shells.py      line 1532
ok  solar_visualization_shells.py      line 1495
ok  solar_visualization_shells.py      line 1486
ok  solar_visualization_shells.py      line 612
ok  solar_visualization_shells.py      line 598
ok  solar_visualization_shells.py      line 579
ok  solar_visualization_shells.py      line 556
ok  solar_visualization_shells.py      line 301
ok  solar_visualization_shells.py      line 272
ok  solar_visualization_shells.py      line 242
ok  solar_visualization_shells.py      line 230
ok  solar_visualization_shells.py      line 221
ok  solar_visualization_shells.py      line 211
ok  solar_visualization_shells.py      line 175
ok  solar_visualization_shells.py      line 116
ok  solar_visualization_shells.py      line 98
ok  solar_visualization_shells.py      line 15
ok  solar_visualization_shells.py      line 4
ok  LEDGER_CONSOLIDATED.md             line 1253
ok  LEDGER_CONSOLIDATED.md             line 1187
ok  LEDGER_CONSOLIDATED.md             line 1120
ok  LEDGER_CONSOLIDATED.md             line 1065
ok  LEDGER_CONSOLIDATED.md             line 332
ok  documentation/WHERE_WE_ARE.md      line 110
ok  documentation/WHERE_WE_ARE.md      line 92
ok  documentation/WHERE_WE_ARE.md      line 82
ok  documentation/WHERE_WE_ARE.md      line 74
ok  documentation/WHERE_WE_ARE.md      line 54
ok  documentation/WHERE_WE_ARE.md      line 35
ok  documentation/WHERE_WE_ARE.md      line 10
ok  documentation/WHERE_WE_ARE.md      line 3
ok  pole_frames.py                     created
ok  hills_cloud_sampler.py             created
ok  test_hills_cloud_sampler.py        created
ok  documentation/L421_fig3_reading_20261010.py created
ok  documentation/HANDOFF_L421_oort_orrery_20261010.md created
note: WHERE_WE_ARE.md has 129 lines above the run-record marker (the cap is 130)
stamps updated: the ledger header; module docstrings of constants_new.py, constants_tokens.py, idealized_orbits.py, solar_visualization_shells.py, palomas_orrery.py, orrery_maintenance_run.py; WHERE_WE_ARE.md date line
patch applied: 52 edits in 8 files, and 5 new files.

NEXT:
  1. Run hills_cloud_sampler.py if you like: it prints the drawn tilt (about 34 degrees), the arms, and three checks ending "PASS". -- is this a one-time use script?

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/hills_cloud_sampler.py
Hills cloud, as drawn: 600 orbits, 3600 dots
Judged on a larger sample (4000 orbits, 24000 dots):
  plane through the dots: tilted 34.1 deg to the ecliptic (the paper: about 30)
  the orbits' own tilts: mean 40.8 deg, spread 16.3 deg
  arm 1 (omega_G 70-180 deg): toward ecliptic longitude 22, latitude -8 deg
  arm 2 (omega_G 250-360 deg): toward ecliptic longitude 203, latitude 6 deg
  dots inside the inner edge: 12%; beyond the band's near end: 20%
  frame: Sgr A* at galactic longitude -0.44, latitude -0.05 deg
  reading: 67% of Fig. 3's dots inside its caption's ranges
PASS: frame, reading and tilt
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 

  2. Run orrery_maintenance_run.py. Expect "22 of 22 gating checkers passed" and "GATE PATH: 0 TIER-1 -- the push gate holds". The whole tree's Tier-1 count goes from 293 to 292: the shells module's docstring now names a paper, so the scanner reads its numbers as cited (the build record, section 5). -- done
  3. Look in the orrery window: centre on the Sun, tick the Hills Cloud (tilted disk), -- correct
  4. the clumpy outer Oort cloud, -- correct
  5. the galactic tide and -- correct
  6. the Inner Oort Cloud sphere; plot and turn it.  -- correct
  7. Three checks in documentation/HANDOFF_L421_oort_orrery_20261010.md, section 7.

**Tony:** -- correct
## 7. Mode 5, Tony's look in the orrery window

Centre on the Sun; under the Sun's shells tick Hills Cloud (tilted
disk), the clumpy outer Oort cloud, the galactic tide and the Inner
Oort Cloud sphere; plot, and turn it.
1. The Hills cloud is a disk tipped against the planets' plane, its
   dots thickest along two opposite arms near the ecliptic.
2. The clumps and the tide begin thin inside the Inner Oort Cloud
   sphere (20,000 au) and are full outside it.
3. The hovers read as in section 8.
Looks wrong? The frame is the suspect first: the galactic pole rows
and the node row.

  8. Move this script (and patch_L395_7, if still in the root) into documentation/; commit and push. -- 9f1547821a1957544f0ae94a77cc64c5a3ab4114
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 

Where this leaves us

The orrery draws the inner Oort cloud from the paper; the website follows in the next session, together with the galactic plane (L-408).
Still open after that: the typed facts’ check, and whether each served number’s citation in the gallery config matches its row in the constants file.

**Follow up**
Everything in your run record checks out. Both patches ran and all 22 checks passed, every look you made came back correct, and your push is on GitHub at 9f15478.

**Is hills_cloud_sampler.py one-time?** No, it's permanent. The orrery calls it every time it draws the Hills cloud. Running it directly is optional: it only prints the checks. Only the patch scripts are one-time.

**Encke to the top of the comet list:** yes. That's a small change, and it goes in the next patch. That patch also records your verdicts from this run record.

**The orbital period, which is what you asked to discuss.** The orrery gets periods today from one hand-typed table, `KNOWN_ORBITAL_PERIODS` in constants_new.py. It has about 150 entries. Some were copied from Horizons with a date, some are rounded or marked "estimate", and none carries a source. A typed period also goes stale: JPL re-solved Encke's orbit twice this month.

There is a second route already in the code. When the orrery fetches an object's orbit from Horizons, it gets the semi-major axis, which is the orbit's average distance from the Sun. Kepler's third law turns that into a period. The orrery already does this for some objects; it just checks the table first.

Three ways forward:

1. **Type Encke's period into the table from Horizons, as Halley's was.** This takes minutes. But it adds one more typed number that drifts.
2. **Work the period out from the fetched orbit whenever there is one, and keep the table only as a fallback for when the orrery is offline.** No comet with fetched elements needs a typed period, and each one follows JPL's newest solution automatically. The cost is a change to the few places in palomas_orrery.py that read the table, and testing them.
3. **Give each object its period in its own entry in the orrery's object list, with a source,** the way the JPL names went in this session. The website's daily Horizons check could then confirm it. This is the most work, but it makes periods ready for the website.

I recommend **2**. It fixes Encke and every other comet with fetched elements at once, and it replaces typed numbers with JPL's own. The rest of the table would be recorded as one ledger item for a later cleanup, not chased now. Option 3 can follow when the website needs periods.

Which way do you want to go?

=========================================================

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/patch_L431_1_close_20261011.py
ok  palomas_orrery.py                  line 10009
ok  palomas_orrery.py                  line 10003
ok  palomas_orrery.py                  line 68
ok  LEDGER_CONSOLIDATED.md             line 2230
ok  LEDGER_CONSOLIDATED.md             line 2225
ok  LEDGER_CONSOLIDATED.md             line 1923
ok  LEDGER_CONSOLIDATED.md             line 1356
ok  LEDGER_CONSOLIDATED.md             line 1341
ok  LEDGER_CONSOLIDATED.md             line 1211
ok  LEDGER_CONSOLIDATED.md             line 338
ok  documentation/WHERE_WE_ARE.md      line 110
ok  documentation/WHERE_WE_ARE.md      line 92
ok  documentation/WHERE_WE_ARE.md      line 86
ok  documentation/WHERE_WE_ARE.md      line 77
ok  documentation/WHERE_WE_ARE.md      line 71
ok  documentation/WHERE_WE_ARE.md      line 58
ok  documentation/WHERE_WE_ARE.md      line 40
ok  documentation/WHERE_WE_ARE.md      line 33
ok  documentation/WHERE_WE_ARE.md      line 9
ok  documentation/WHERE_WE_ARE.md      line 3
ok  documentation/HANDOFF_L421_oort_orrery_20261010.md line 305
ok  documentation/DESIGN_L431_orbital_periods_20261011.md created
note: WHERE_WE_ARE.md has 129 lines above the run-record marker (the cap is 130)
stamps updated: the ledger header; the module docstring of palomas_orrery.py; WHERE_WE_ARE.md date line
patch applied: 21 edits in 4 files, and 1 new file.

NEXT:
  1. Run orrery_maintenance_run.py. Expect "22 of 22 gating checkers passed" and "GATE PATH: 0 TIER-1 -- the push gate holds". It rebuilds the ledger index with L-431.

======================================================================
MAINTENANCE RUN -- generators, then checkers (L-188)
======================================================================
  Provenance scan is current (last run 20261011T012535Z, 0 day(s) ago).

GENERATORS -- regenerate every time; a no-op when nothing moved
----------------------------------------------------------------------
  Ledger index                 1.8s  rewrote LEDGER_CONSOLIDATED.md
  Skill manifest               0.4s  unchanged (1 of 1 rewritten, content
                                     identical)
  Constants export             1.0s  unchanged (1 checked, not written)
  Objects export               0.1s  unchanged (1 checked, not written)
  Module atlas                 8.8s  rewrote MODULE_ATLAS.md, MODULE_INDEX.md
  Data inventory               5.6s  rewrote DATA_INVENTORY.md
  Exact rows report            2.8s  rewrote EXACT_ROWS_PRINTED.md -- 13 of 38
                                     exact rows printed at 43 lines (33 orrery,
                                     10 gallery); 8 drawn only, 11 not followed,
                                     0 map entries broken
  Document index               0.2s  unchanged (1 checked, not written)

CHECKERS -- verdict informs the push call
----------------------------------------------------------------------
  Constants change             0.3s  No changes to constants_new.py since HEAD.
  Constants relations          0.3s  25 of 25 provenance tests passed against
                                     constants_new.py. No constants have drifted.
  Derived figures              0.8s  No figure count exceeds its inputs: 36
                                     derived row(s) read, 26 judged OK -- 26 OK,
                                     10 NOT YET MIGRATED, 1 NO DERIVED LINE, 1
                                     UNMARKED CONVERSION; 18 conversion(s)
                                     checked.
  Constants export check       1.4s  Export matches the store: sha256
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
  Dimensions                   1.2s  No unit contradicts its arithmetic: 54
                                     derived row(s) read -- 42 OK, 9 NO UNIT, 3
                                     NOT CHECKABLE.
  Cross-check annotations      0.1s  19 of 19 cross-check annotation tests
                                     passed.
  Citation inheritance         0.1s  20 of 20 citation-inheritance tests passed.
  Status lines                 0.1s  All 119 status lines in constants_new.py are
                                     well formed; 54 rows carry none.
  Row shape                    0.1s  All 176 row shapes in constants_new.py fit
                                     the assignment's own line.
  Scanner recognition 1d/1e    0.3s  27 of 27 recognition pins hold: real
                                     citations recognized, fake ones refused.
  Scanner row run (L-414)      0.3s  16 of 16 pins hold -- each row reads its own
                                     comment run, declared rows are named, the
                                     gate path is read by name.
  Reset completeness          31.8s  PASS -- all 311 IntVars + 3 StringVars + 10
                                     entries reset to startup defaults; date set
                                     to now.
  Orbit cache                  3.1s  All 6 orbit cache tests passed: cache loads,
                                     old formats convert, corrupted entries are
                                     dropped.
  Earth pole of date           0.4s  all 14 checks passed (geometry, ERFA,
                                     fallback, cache, hover, transform).
  Hills cloud sampler (L-421)    0.8s  PASS -- 4 of 4 planted faults caught; the
                                     real rows pass, the dots' plane tilted 34.1
                                     deg
  Worksheet checker           10.7s  74 of 110 routed, 8 clean
  Worksheet checker tests     22.2s  All 135 checks passed
  Worksheet key round trip     1.4s  RESULT: 52 sites minted 52 distinct keys,
                                     all resolved; 52 pinned keys still resolve;
                                     1 retired keys confirmed gone.
  Builder marker join         33.4s  All 76 checks passed
  Extractor pins               0.6s  RESULT: 29 string sites carry the pinned 73
                                     claims and 14 instruction drops, at LOOKBACK
                                     30 / LOOKAHEAD 25, extractor version 2.
  Provenance scanner          14.2s  0 TIER-1 -- the push gate holds

======================================================================
  22 of 22 gating checkers passed -- 146.3s total
  2 report-only, exit 0 whatever they find:
    Worksheet checker           74 of 110 routed, 8 clean
    Provenance scanner          0 TIER-1 -- the push gate holds
======================================================================

FILES WRITTEN THIS RUN
----------------------------------------------------------------------
  2161 file(s) examined, 10 written, 0 created, 0 removed, 4 rewritten identically
    written   DATA_INVENTORY.md
    written   EXACT_ROWS_PRINTED.md
    written   LEDGER_CONSOLIDATED.md
    written   MODULE_ATLAS.md
    written   MODULE_INDEX.md
    written   PROVENANCE_AUDIT.md
    written   WORKSHEET_CHECK.md
    written   data/provenance_history.json
    written   documentation/WHERE_WE_ARE_10-10-26_2019_run_record.md
    written   documentation/prompts/citation_review.jsonl
    rewritten with identical bytes, no action needed:
      PROJECT_INSTRUCTIONS.md
      data/worksheet_check_state.json
      data/worksheet_routed.json
      test_output/test_orbit_paths.json
    20 file(s) over 2 MB compared by size and mtime only

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>

  2. If you like, open the orrery window: Encke is now the first comet. -- done. looks great. 
  3. Move this script, and patch_L395_5_horizons_name_and_encke_20261010.py (still in the root), into documentation/. If you saved last night's annotated run record as a timestamped copy, it goes in this commit too. Commit and push. -- d3c4c3854277c25ab8d494c95521f7958e0384d1
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 

=================================================================================

======================================================================
  DAILY RUN -- Sunday October 11, 2026  08:42
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io
======================================================================
Daily Run steps, from C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io:
  1. Guest book updater                 tools\guestbook_updater.py  found
  2. Horizons check                     tools\horizons_check.py  found
  3. Cache builder                      tools\gallery_cache_builder.py  found
  4. Gallery maintenance run, offline   gallery_maintenance_run.py  found
=== DAILY RUN: all 4 step scripts found
Last cache build: 2026-10-10 22:11 UTC, ok, 0 days ago.

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
Checked data/objects_export.json, pulled from orrery 32619f8d.
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
[done] run 20261011T134230Z (nightly): 19 objects

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
  PASS Module atlas              1.7s  rewrote MODULE_ATLAS.md,
                                    MODULE_INDEX.md
  PASS Constants export pull     1.1s  rewrote
                                    data/constants_export.json,
                                    data/constants_export.sha
  PASS Config mirror             0.1s  no change to
                                    data/objects_config.json
  PASS Objects export pull       0.6s  rewrote data/objects_export.sha
  PASS Objects mirror            0.1s  no change to
                                    data/objects_config.json

CHECKERS -- the verdict informs the push call
  PASS Cache builder suite      17.6s  PASS (229 checks, 0 failures)
  PASS Pole of date              0.3s  POLE OF DATE: all 11 checks passed
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
  PASS Store writer suite        9.5s  All 322 store-writer checks
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
  PASS Store editor suite        0.1s  All 305 store-editor checks
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
                                    9d79d8797a22.
  PASS Horizons check suite      0.3s  HORIZONS CHECK SUITE: pass
  PASS Horizons confirmations    0.1s  HORIZONS CONFIRMATIONS: pass -- 13
                                    of 13 confirmed within 30 days
  PASS Pointer join              0.1s  Every link is accounted for: 108
                                    link(s) against orrery 9f154782, 4
                                    fallback named; read check: 43 of
                                    43 measured rows reached carry a
                                    read.
  PASS Cache in step             0.1s  The served cache holds the
                                    config's 19 object(s) and their
                                    features exactly: 4 object(s) with
                                    35 named shell(s), in both cache
                                    files.
  PASS Collapsed features        0.1s  33 stored as themselves, 16
                                    collapsed, 0 unclassified.
  PASS Feature renderers         1.5s  === ALL CHECKS PASSED ===
  PASS Page framing              0.2s  === ALL CHECKS PASSED ===
  PASS Sun shells                0.2s  ALL CHECKS PASSED
  PASS Earth scene geometry      0.2s  === ALL CHECKS PASSED ===
  PASS Hover budget              0.2s  === ALL CHECKS PASSED ===
  PASS Arrival                   0.3s  Arrival: both rooms open on the
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
  26 of 26 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Cache siblings         RESULT: no sibling directories and
  last swap 2026-10-11T13:43:06.145694+00:00: succeeded first time
======================================================================

  After you push: python gallery_maintenance_run.py --live

======================================================================
  DAILY RUN -- summary
======================================================================
  Guest book updater           ok
  Horizons check               ok
  Cache builder                ok
  Maintenance run, offline     ok

  NEXT:
    1. GitHub Desktop: look at the change list, then commit and push. -- fd17abf1cf99169289acfeb0a45f84365265c255
    2. Then the dashboard's Gallery Maintenance Run -- live, AFTER a push.

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

  PASS Served reachability       2.0s  all 15 files served and
                                    byte-identical to the working copy

  orrery export pinned at 9f154782

  PASS Export freshness          0.1s  the served export is the orrery's
                                    at 9f154782, byte for byte

  orrery HEAD 9f154782
  examining 7 of 108 links; the other 101 are served from the export
    NOT IN STORE  planet_poles['Sun']              not a top-level constant in the store
                  /objects/0/features/orientation
    NOT IN STORE  planet_poles['Jupiter']          not a top-level constant in the store
                  /objects/2/features/orientation/pole
    NOT IN STORE  planet_poles['Saturn']           not a top-level constant in the store
                  /objects/3/features/orientation/pole
  7 pointers: 4 match, 0 DRIFT, 0 UNIT MISMATCH, 3 could not be examined.

  PASS Store drift               1.1s  7 pointers against orrery 9f154782
                                    -- 4 match, 0 DRIFT, 0 UNIT
                                    MISMATCH, 3 could not be examined.

======================================================================
  2 of 2 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Store drift            7 pointers against orrery 9f154782 -- 4
  last swap 2026-10-11T13:43:06.145694+00:00: succeeded first time
======================================================================

  Offline pass: python gallery_maintenance_run.py

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

======================================================================

**Opus:**

Where it lands. Four places in the orrery read a period today, and all four would use the fetched one first:

the period shown in an object’s hover;
the period in the orbital parameters window;
the warning about how many orbits a date range covers;
the period worked out when a position is fetched.

The website is not affected. Its export script reads the table only to print a check, not to serve data.

What changes for each object. The period arrives the next time its orbit is fetched or refreshed from Horizons. Until then, the hand-typed table still answers. Objects the orrery never fetches keep their table value. The table’s unsourced entries become one ledger item, to be cleaned up later.

Yes. The project already has the rule for this: a worked-out number prints only as many digits as its errors allow, judged by the larger error. That is how the Solar System room prints distances. A period has two errors, and which one is larger depends on the object.

1. How well JPL knows the orbit. JPL’s small-body database publishes a one-sigma uncertainty for each object’s period. As read today, through a summary that I’d re-read exactly in the build:

Encke: period about 1,210 days, uncertainty 0.00011 days, roughly ten seconds. That supports eight figures.
Sedna: period about 4,630,000 days, uncertainty 1,900 days, roughly five years. That supports three figures in days, about 12,700 years.

2. How much the fetched period itself moves. Horizons gives the period of the orbit at the plotted date, and the planets keep changing it. For Encke that is under a day: your file showed 1,206.3 days for this October, against 3.30485 years (1,207.1 days) at the record’s 2023 date. So eight figures would claim far more than the next return will show. Encke really earns about four figures: 3.303 years, or 1,206 days.

For a distant body like Sedna, there’s an extra effect. The Sun itself wobbles around the solar system’s centre of mass, which makes a period measured from the Sun swing much more. The period measured from that centre of mass, the barycentre, is the steadier one. I’d measure both rather than guess the gap.

So the rule: print to the larger of the two errors, with each unit (days, years) placed separately. In the build:

the first error comes from JPL’s published uncertainty;
the second comes from comparing the period on two dates a year apart. For a distant object, that comparison would also use the barycentre.

For planets and moons, JPL’s database publishes no uncertainty, so the second error alone sets the digits.

This extends an existing rule rather than making a new one, so it goes into the provenance skill and the build follows it. Build it this way? -- for discussion

The Sun-based figure swings by 2,000 years in eight years because the Sun itself circles the barycentre, pulled mostly by Jupiter. Sedna doesn’t feel that wobble. The barycentre figure is steady, and it is the real one: about 11,390 years. JPL’s published uncertainty for Sedna’s orbit, about 5 years, then decides the digits, so four figures.

Encke is the opposite case. It orbits close in, so the Sun-based period is the right one. What limits it is the planets’ pull, which moves it by about a day over a few years: 1,206 days, or 3.303 years.

So the rule now has two parts:

Which centre. Ask Horizons for the period from both the Sun and the barycentre, a year apart, and use whichever moves less.
How many digits. Print to the larger of two errors: how much that period moved in a year, and JPL’s published uncertainty for the orbit, where one exists. Days and years are each printed to their own digits.

That means four or five extra Horizons questions each time an object’s orbit is refreshed, plus a change to the provenance skill, plus the four places in the orrery that read a period.

The orbital-period work is written up, and the session’s close is in one patch, patch_L431_1_close_20261011.py. The one thing to do: run it from the orrery folder, then the maintenance run (expect 22 of 22), then commit and push. I ran both on a copy here and both passed.

What the patch does:

Comet list: Encke moves to the top of the list, so it runs oldest first.
Your looks: the Encke and Halley checks and the Hills cloud checks are recorded in the ledger as correct. So is your note that a colour is a drawing choice.
New ledger item: L-431 (orbital periods from JPL) is opened with your rulings. It also notes that none of the 132 periods typed by hand in the orrery’s table cite a source.
Design record: DESIGN_L431_orbital_periods_20261011.md holds JPL’s numbers and the questions for the next session.

The main finding. For a distant body, the period depends on what you measure it around. I fetched JPL’s numbers for a year ago and today:

Sedna: measured around the Sun, its period went from 12,917 years to 12,547 years in that one year. Measured around the solar system’s centre of mass, it stayed at 11,390 years, changing by only 7 days.
Encke: the opposite. Around the Sun it changed by a third of a day; around the centre of mass, by almost 8 days.

Proposed rule, for you to rule on next session: -- for discussion

Which centre: use the one whose period changes less over a year.
How many digits: print only what the larger of two uncertainties allows. One is JPL’s own stated uncertainty; the other is how much the period moves in a year. Encke would read “3.303 years” and Sedna “11,390 years”.

A related question for the next session. The orrery draws Sedna’s orbit from its elements around the Sun, so the drawn orbit’s size moves from year to year the same way the period does.

Where this leaves us

The Hills cloud and Encke are done and looked at.
Next session starts with the orbital periods design talk, as you asked.
The website’s side of the inner Oort cloud comes after that.

==================================================================

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/patch_L431_2_run_record_notes_20261011.py
ok  palomas_orrery_dashboard.py        line 1184
ok  palomas_orrery_dashboard.py        line 1132
ok  palomas_orrery_dashboard.py        line 171
ok  LEDGER_CONSOLIDATED.md             line 22028
ok  LEDGER_CONSOLIDATED.md             line 22016
ok  LEDGER_CONSOLIDATED.md             line 20057
ok  LEDGER_CONSOLIDATED.md             line 20036
ok  LEDGER_CONSOLIDATED.md             line 3552
ok  LEDGER_CONSOLIDATED.md             line 3466
ok  LEDGER_CONSOLIDATED.md             line 2296
ok  LEDGER_CONSOLIDATED.md             line 1652
ok  LEDGER_CONSOLIDATED.md             line 1628
ok  LEDGER_CONSOLIDATED.md             line 1403
ok  LEDGER_CONSOLIDATED.md             line 1370
ok  LEDGER_CONSOLIDATED.md             line 1180
ok  LEDGER_CONSOLIDATED.md             line 1157
ok  LEDGER_CONSOLIDATED.md             line 1148
ok  LEDGER_CONSOLIDATED.md             line 1077
ok  LEDGER_CONSOLIDATED.md             line 342
ok  documentation/WHERE_WE_ARE.md      line 113
ok  documentation/WHERE_WE_ARE.md      line 105
ok  documentation/WHERE_WE_ARE.md      line 96
ok  documentation/WHERE_WE_ARE.md      line 91
ok  documentation/WHERE_WE_ARE.md      line 81
ok  documentation/WHERE_WE_ARE.md      line 74
ok  documentation/WHERE_WE_ARE.md      line 66
ok  documentation/WHERE_WE_ARE.md      line 57
ok  documentation/WHERE_WE_ARE.md      line 46
ok  documentation/WHERE_WE_ARE.md      line 36
ok  documentation/WHERE_WE_ARE.md      line 20
ok  documentation/WHERE_WE_ARE.md      line 9
ok  documentation/WHERE_WE_ARE.md      line 3
ok  documentation/DESIGN_L431_orbital_periods_20261011.md line 9
ok  documentation/HANDOFF_L421_oort_orrery_20261010.md line 328
note: WHERE_WE_ARE.md has 129 lines above the run-record marker (the cap is 130)
stamps updated: the ledger header; the module docstring of palomas_orrery_dashboard.py; WHERE_WE_ARE.md date line
patch applied: 34 edits in 5 files.

NEXT:
  1. Run orrery_maintenance_run.py. Expect "22 of 22 gating checkers passed" and "GATE PATH: 0 TIER-1 -- the push gate holds". It rebuilds the ledger index with L-432 and L-433.

======================================================================
MAINTENANCE RUN -- generators, then checkers (L-188)
======================================================================
  Provenance scan is current (last run 20261011T134721Z, 0 day(s) ago).

GENERATORS -- regenerate every time; a no-op when nothing moved
----------------------------------------------------------------------
  Ledger index                 1.8s  rewrote LEDGER_CONSOLIDATED.md
  Skill manifest               0.2s  unchanged (1 of 1 rewritten, content
                                     identical)
  Constants export             2.2s  unchanged (1 checked, not written)
  Objects export               0.2s  unchanged (1 checked, not written)
  Module atlas                 8.5s  rewrote MODULE_ATLAS.md, MODULE_INDEX.md
  Data inventory               5.4s  rewrote DATA_INVENTORY.md
  Exact rows report            2.4s  unchanged (1 checked, not written) -- 13 of
                                     38 exact rows printed at 43 lines (33
                                     orrery, 10 gallery); 8 drawn only, 11 not
                                     followed, 0 map entries broken
  Document index               0.2s  unchanged (1 checked, not written)

CHECKERS -- verdict informs the push call
----------------------------------------------------------------------
  Constants change             0.3s  No changes to constants_new.py since HEAD.
  Constants relations          0.3s  25 of 25 provenance tests passed against
                                     constants_new.py. No constants have drifted.
  Derived figures              0.9s  No figure count exceeds its inputs: 36
                                     derived row(s) read, 26 judged OK -- 26 OK,
                                     10 NOT YET MIGRATED, 1 NO DERIVED LINE, 1
                                     UNMARKED CONVERSION; 18 conversion(s)
                                     checked.
  Constants export check       1.6s  Export matches the store: sha256
                                     9d79d8797a22 on both sides; 120 rows
                                     re-read, 56 not exported, 29 tokens; 315
                                     conversions re-computed, 10 of 10 worked
                                     cases hold.
  Objects export check         0.1s  pass
  Skill headers                0.2s  12 skills parsed, no consistency problems.
  Exact rows by the count      1.8s  PASSING -- 13 printed exact rows each state
                                     a count; 33 orrery lines print through
                                     exact_text() or row_text(); 10 gallery lines
                                     are served the count
  Dimensions                   1.3s  No unit contradicts its arithmetic: 54
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
  Reset completeness          24.2s  PASS -- all 311 IntVars + 3 StringVars + 10
                                     entries reset to startup defaults; date set
                                     to now.
  Orbit cache                  2.2s  All 6 orbit cache tests passed: cache loads,
                                     old formats convert, corrupted entries are
                                     dropped.
  Earth pole of date           0.4s  all 14 checks passed (geometry, ERFA,
                                     fallback, cache, hover, transform).
  Hills cloud sampler (L-421)    0.5s  PASS -- 4 of 4 planted faults caught; the
                                     real rows pass, the dots' plane tilted 34.1
                                     deg
  Worksheet checker           10.0s  74 of 110 routed, 8 clean
  Worksheet checker tests     16.9s  All 135 checks passed
  Worksheet key round trip     1.1s  RESULT: 52 sites minted 52 distinct keys,
                                     all resolved; 52 pinned keys still resolve;
                                     1 retired keys confirmed gone.
  Builder marker join         23.5s  All 76 checks passed
  Extractor pins               0.5s  RESULT: 29 string sites carry the pinned 73
                                     claims and 14 instruction drops, at LOOKBACK
                                     30 / LOOKAHEAD 25, extractor version 2.
  Provenance scanner          10.8s  0 TIER-1 -- the push gate holds

======================================================================
  22 of 22 gating checkers passed -- 118.6s total
  2 report-only, exit 0 whatever they find:
    Worksheet checker           74 of 110 routed, 8 clean
    Provenance scanner          0 TIER-1 -- the push gate holds
======================================================================

FILES WRITTEN THIS RUN
----------------------------------------------------------------------
  2162 file(s) examined, 9 written, 0 created, 0 removed, 4 rewritten identically
    written   DATA_INVENTORY.md
    written   LEDGER_CONSOLIDATED.md
    written   MODULE_ATLAS.md
    written   MODULE_INDEX.md
    written   PROVENANCE_AUDIT.md
    written   WORKSHEET_CHECK.md
    written   data/provenance_history.json
    written   documentation/WHERE_WE_ARE_10-10-26_2019_run_record.md
    written   documentation/prompts/citation_review.jsonl
    rewritten with identical bytes, no action needed:
      PROJECT_INSTRUCTIONS.md
      data/worksheet_check_state.json
      data/worksheet_routed.json
      test_output/test_orbit_paths.json
    20 file(s) over 2 MB compared by size and mtime only

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>

  2. If you like, open the dashboard: Test Hills Cloud Sampler and Test Scanner Row Run are under the orrery checks; each should end on PASS.
  3. Move this script into documentation/; commit and push. -- 
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

