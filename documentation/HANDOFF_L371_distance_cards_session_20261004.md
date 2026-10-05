<!-- Doc-Kind: hand | Session record: L-371's distance cards built, the Sun slice ordered. -->
# Handoff: the Sun's distance cards (L-371), and the Sun slice ordered

Built on orrery 17ef66607cbe63ac5ed7bdbff15397fbe546ae42 at
https://github.com/tonylquintanilla/palomas_orrery; pushed through
e38b86adb7d1b32696b759b3c8222f3742aa2bd4. Gallery
52659e04 at https://github.com/tonylquintanilla/tonyquintanilla.github.io;
pushed through ba68819937bae6089d104c9a370a0b84c8a87925 (the lobby
card's separate session also pushed in between, at d4b408e6).
The close patches below land after these, on orrery
d7f2a59440b49461a742a301777a67dc9bf49097 and gallery
ac81e7ce6257cfd6811df7d031f94ac3109d480c, where the lobby-card session's
records and license patches had landed first.

- Type: BUILD.
- Supersedes: `documentation/HANDOFF_L406_L407_L371_session_20261003.md`
  as the latest record. That file also holds this session's run records,
  which Tony appended to it.
- Session date: 2026-10-04. (Rows and credit lines were first stamped
  2026-10-03 by mistake; the close patches correct them.)

## What was done [verified @ orrery e38b86ad, gallery ba688199]

1. **patch_L371_1 (orrery).** The Sun's distance rows, each with its
   source opened this session, its figure count and its read line:
   termination shock 94.01 AU (Stone et al. 2005), heliopause 121 AU
   (Gurnett et al. 2013, p. 1489), the Oort cloud's two edges as range
   rows (NASA's facts page) drawn at 2,000 and 100,000 AU, the inner
   cloud's 20,000 AU (Portegies Zwart et al. 2021, sec. 2.2), the Sun's
   Hill radius 0.65 pc (the same paper), the helmet cusp's 2-4 as two
   rows, the Alfven surface, corona and Roche limit with units and
   counts. The unsourced 100,000-200,000 AU row removed; the outer
   corona's unfound citation removed. A pc token, KM_PER_PARSEC,
   `constants_rows.row_text()`, every orrery hover line that states
   these distances printed from its row, three relation tests, and
   exact_rows_report.py made to see `row_text()`.
2. **patch_L371_2 (orrery).** ROCHE_LIMIT_DRAWN_RADII, Tony's option B.
3. **patch_L371_3 (gallery).** The Sun's links, Tony's notes with their
   numbers from served range rows, `drawn_radius`, a far shell's
   "Radius: <n> AU", served counts on the Oort shapes and the streamer
   band, the Sun shells check, a re-recorded hover fixture.
4. Runs: orrery 20 of 20; gallery 23 of 23 after `daily_run.py`. Tony
   approved both wording files. On the phone: "Beautiful", and the
   Alfven surface at 0.092 AU inside the outer corona at 0.23 AU.

## Tony's rulings

- The Roche limit is drawn at 3.45 on both sites, described as "about
  3": at 3 it would sit on the inner corona, and which is further out
  is not known. An interim until fuzzy boundaries (L-410).
- The leading-1 shortcut is not adopted. The uncertainty test of
  2026-09-28 stands, so 100,000 AU prints as 10,000,000,000,000 km.
  Tony: "I don't want to violate my own rule!"
- Fuzzy boundaries are their own item, the outer corona first and
  designed with the dust cloud (L-410, L-131). The dust cloud joins the
  Sun's slice.
- The Sun's slice is the ordered list on L-412. The scattered disk
  (L-136) goes to the Solar System room.

## Discrepancies surfaced

- The orrery patch said the scanner would report 296 serious findings;
  Tony's machine reported 297. Tony's tree was already at 297, and the
  one new file flagged was the patch script itself in the root folder.
  Carried on L-371 as method for the next skill version.
- L-385 was offered as "one line" for this close and is not: the axis
  length and the shells switched on both set the width. Recorded on
  L-385; the Sun slice's next item.
- EXACT_ROWS_PRINTED.md lists 11 gallery pointers to exact Sun rows as
  not followed. The site prints them by the served count, but the check
  cannot yet confirm it. L-371's Gap.
- The previous handoff cited Figs. 3 and 4 for the 0.65 pc; it is
  Figs. 2 and 3. Duncan, Quinn and Tremaine's abstract does not print
  20,000 AU, so the row cites Portegies Zwart sec. 2.2 instead.

## Checked against the other session before closing

- The lobby-card session had taken L-409 (the licenses), so this
  session's new items are L-410, L-411 and L-412.
- It had rewritten Where We Are; this close merges both sessions into
  the page rather than replacing its words.
- Its drawer-fix patch, patch_L363_14, ran after its records patch and
  was not on the ledger; this close adds that note to L-363 from Tony's
  run record.
- No file this close edits had been touched by the other session
  besides those two.

## The close patches

- `patch_L371_4_session_close_orrery_20261004.py`: the ledger (L-371,
  L-385, L-386, L-228, L-241, L-131, L-136, L-128 and L-363 updated; L-209,
  L-224, L-227, L-229 closed; L-410, L-411, L-412 opened), this
  handoff, Where We Are, and the date corrections in ten orrery files.
- `patch_L371_5_dates_gallery_20261004.py`: the date corrections in
  three gallery files' comments. No hover or served value changes.

## Tony-actions, rolled up

- (do) Run the orrery close patch, then orrery_maintenance_run.py
  (every gating check passes), move the script into documentation/,
  commit and push.
- (do) Run the gallery close patch, then gallery_maintenance_run.py
  (23 of 23; no cache rebuild is needed, since no served value
  changes), move the script into documentation/, commit and push.

## Skills

- No skill changed this session, so there is no load to confirm next
  session.
- Carried to the next versions (on L-371): provenance-discipline's
  range-rule example names the removed range row; and a patch's
  "what the run should say" should predict the scanner's change, not
  its total.

## Next session

First, Earth's list (the section below). Then start at L-412 item 3,
the orrery's opening view of the Sun (L-385):
read the Sun's autoscale with its default shells and propose to Tony
before building. Then item 4, L-228: Claude reads Cranmer et al. (2007)
itself. Beside the list, L-371's own Gap.

## Next session also: Earth's list, for a ledger update

On 2026-10-04 Tony asked for the same sweep for Earth that L-412 is for
the Sun, to be recorded on the ledger next session. Do it
early: first read L-305 and L-292 against the code, so the list starts
accurate, then write it as one ledger item in the shape of L-412.

The sweep, as given to Tony:

- **Possibly finished but still open; read first.**
  - L-305, the magnetosphere on a sourced model: the Shue and Jelinek
    shapes are in both instruments, but its open list is long.
  - L-292, the shells the orrery does not draw: an exosphere shell
    naming the geocorona now exists; the other two may not.
  - L-383, the magnetosphere tooltip copy: if that SHELL_CONFIGS text
    is never shown (orrery-coding-conventions calls the tooltip field
    dead data), the copy goes.
- **Small, the Earth room reaches them.**
  - L-369, Earth's obliquity typed in four places outside the store.
  - L-350, the magnetotail's observed extent served and shown nowhere:
    Tony decides print it or stop serving it.
  - L-349 then L-383, the inner belt's "where the measured particle
    flux peaks": Tony's wording ruling, then the copy.
  - L-389, the atmosphere shells from the equatorial radius against the
    crust at the mean radius: Tony noted it "depends on the source".
  - L-379, the recorded Earth scene payload, aging: recapture it.
  - L-382, Tony's look at the magnetosphere's cost per animation frame.
- **Design talks first.**
  - L-231 then L-330, the belts tilted with the magnetic field, then
    their shape.
  - L-375, the eccentric dipole offset (depends on an unmodelled
    rotation phase).
  - L-356, IGRF-14 as a re-sourcing of the coefficient rows.
  - L-321, the orrery's 36 Earth hover strings into the provenance
    braid.
  - L-297 and L-294, the Lagrange points and Earth's heliocentric view,
    behind Tony's ruling on the Explorer room.
  - L-314 after L-305, live solar wind for the magnetosphere.
  - L-374 and L-061, precession over time and the seasonal roll:
    recorded ideas.
- **Not the Earth room:** L-001, L-060 (the Earth System climate
  track), L-157, L-173, L-186, L-252 (the cross-check programme), L-177
  (Mercury), L-347, L-348, L-360, L-367 (general checks).

Tony orders the list when it is put to him; the order above is the
sweep's, not his.

Session written October 2026 with Anthropic's Claude Opus 5.5.

======================================================================

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/patch_L413_1_ledger_sweep_and_earth_list_20261004.py
ok  documentation/WHERE_WE_ARE.md  rewritten whole
ok  LEDGER_CONSOLIDATED.md         L-409: status line
ok  LEDGER_CONSOLIDATED.md         L-409: closed on the sidebar check
ok  LEDGER_CONSOLIDATED.md         L-407: status line
ok  LEDGER_CONSOLIDATED.md         L-407: closed on the load check
ok  LEDGER_CONSOLIDATED.md         L-350: status line
ok  LEDGER_CONSOLIDATED.md         L-350: closed, the hover prints it
ok  LEDGER_CONSOLIDATED.md         L-406: status line
ok  LEDGER_CONSOLIDATED.md         L-406: closed, the look is L-408's
ok  LEDGER_CONSOLIDATED.md         L-305: status line
ok  LEDGER_CONSOLIDATED.md         L-305: closed, loose ends re-homed
ok  LEDGER_CONSOLIDATED.md         L-234: status line
ok  LEDGER_CONSOLIDATED.md         L-234: closed, the Earth half is served
ok  LEDGER_CONSOLIDATED.md         L-383: status line
ok  LEDGER_CONSOLIDATED.md         L-383: folded into L-181
ok  LEDGER_CONSOLIDATED.md         L-228: status line
ok  LEDGER_CONSOLIDATED.md         L-228: the (do) struck
ok  LEDGER_CONSOLIDATED.md         L-408: status line
ok  LEDGER_CONSOLIDATED.md         L-408: the Gap made current
ok  LEDGER_CONSOLIDATED.md         L-412: status line
ok  LEDGER_CONSOLIDATED.md         L-412: Earth's list first
ok  LEDGER_CONSOLIDATED.md         L-216: the stray folder deleted
ok  LEDGER_CONSOLIDATED.md         L-363: status line
ok  LEDGER_CONSOLIDATED.md         L-363: lobby checker re-homed
ok  LEDGER_CONSOLIDATED.md         L-363: two decides struck, GO arrow ruled, Gap rewritten
ok  LEDGER_CONSOLIDATED.md         L-363: Gap
ok  LEDGER_CONSOLIDATED.md         L-411: status line
ok  LEDGER_CONSOLIDATED.md         L-411: the credit line
ok  LEDGER_CONSOLIDATED.md         L-136: status line
ok  LEDGER_CONSOLIDATED.md         L-136: scattered disk vs fuzzy boundaries
ok  LEDGER_CONSOLIDATED.md         L-300: status line
ok  LEDGER_CONSOLIDATED.md         L-300: path corrected, placed
ok  LEDGER_CONSOLIDATED.md         L-396: status line
ok  LEDGER_CONSOLIDATED.md         L-396: the stamp the check would read
ok  LEDGER_CONSOLIDATED.md         L-351: status line
ok  LEDGER_CONSOLIDATED.md         L-351: the one place for owed skill sentences
ok  LEDGER_CONSOLIDATED.md         L-314: status line
ok  LEDGER_CONSOLIDATED.md         L-314: carries the aberration
ok  LEDGER_CONSOLIDATED.md         L-181: status line
ok  LEDGER_CONSOLIDATED.md         L-181: L-383 folded in
ok  LEDGER_CONSOLIDATED.md         L-292: status line
ok  LEDGER_CONSOLIDATED.md         L-292: the orrery half stands
ok  LEDGER_CONSOLIDATED.md         L-369: status line
ok  LEDGER_CONSOLIDATED.md         L-369: line numbers at HEAD
ok  LEDGER_CONSOLIDATED.md         L-131: status line
ok  LEDGER_CONSOLIDATED.md         L-131: in the active slice
ok  LEDGER_CONSOLIDATED.md         L-128: status line
ok  LEDGER_CONSOLIDATED.md         L-386: status line
ok  LEDGER_CONSOLIDATED.md         L-241: status line
ok  LEDGER_CONSOLIDATED.md         L-308: status line
ok  LEDGER_CONSOLIDATED.md         L-308: DEFERRED with its trigger
ok  LEDGER_CONSOLIDATED.md         L-375: status line
ok  LEDGER_CONSOLIDATED.md         L-375: the dipole cone on the website
ok  LEDGER_CONSOLIDATED.md         L-367: status line
ok  LEDGER_CONSOLIDATED.md         L-367: lobby code re-homed
ok  LEDGER_CONSOLIDATED.md         L-330: status line
ok  LEDGER_CONSOLIDATED.md         L-330: unblocked
ok  LEDGER_CONSOLIDATED.md         L-413 and L-414: opened
ok  LEDGER_CONSOLIDATED.md         header stamp
ok  LEDGER_CONSOLIDATED.md         L-415: opened
ok  LEDGER_CONSOLIDATED.md         L-133: status line
ok  LEDGER_CONSOLIDATED.md         L-133: the 22 files named
ok  PROJECT_INSTRUCTIONS.md        header and anchor
ok  PROJECT_INSTRUCTIONS.md        v3.80 entry
ok  PROJECT_INSTRUCTIONS.md        v3.77 moved down
ok  documentation/PROJECT_INSTRUCTIONS_HISTORY.md v3.77 received
ok  skills/safe-file-editing/SKILL.md version line
ok  skills/safe-file-editing/SKILL.md date and v1.12 paragraph
ok  skills/safe-file-editing/SKILL.md Line Endings: write LF, except committed CRLF
ok  skills/safe-file-editing/SKILL.md Guard section: patches and generators agree
ok  skills/safe-file-editing/SKILL.md Compare Content: write LF
ok  skills/safe-file-editing/SKILL.md Compare Content: code
ok  skills/safe-file-editing/SKILL.md Compare Content: the corrected paragraph
ok  documentation/HANDOFF_L413_ledger_sweep_and_earth_list_20261004.md created

Stamps updated: the ledger's header (October 4, built on 41c1ca7a);
safe-file-editing's version line, cut-from list, date and v1.12
paragraph; the protocol's header, anchor and v3.80 entry; Where We
Are's date and SHAs.

patch applied

NEXT:
  1. Run orrery_maintenance_run.py. Every gating check passes; the
     Ledger index step moves seven closed items to section C, and
     the Skill manifest step writes 1.12 into the protocol.

======================================================================
MAINTENANCE RUN -- generators, then checkers (L-188)
======================================================================
  Provenance scan is current (last run 20261005T011351Z, 0 day(s) ago).

GENERATORS -- regenerate every time; a no-op when nothing moved
----------------------------------------------------------------------
  Ledger index                 1.4s  rewrote LEDGER_CONSOLIDATED.md
  Skill manifest               0.2s  rewrote PROJECT_INSTRUCTIONS.md
  Constants export             0.8s  unchanged (1 checked, not written)
  Objects export               0.1s  unchanged (1 checked, not written)
  Module atlas                 6.9s  rewrote MODULE_ATLAS.md, MODULE_INDEX.md
  Data inventory               5.2s  rewrote DATA_INVENTORY.md
  Exact rows report            1.8s  unchanged (1 checked, not written) -- 13 of
                                     34 exact rows printed at 42 lines (32
                                     orrery, 10 gallery); 8 drawn only, 11 not
                                     followed, 0 map entries broken
  Document index               0.1s  unchanged (1 checked, not written)

CHECKERS -- verdict informs the push call
----------------------------------------------------------------------
  Constants change             0.2s  No changes to constants_new.py since HEAD.
  Constants relations          0.2s  25 of 25 provenance tests passed against
                                     constants_new.py. No constants have drifted.
  Derived figures              0.8s  No figure count exceeds its inputs: 34
                                     derived row(s) read, 24 judged OK -- 24 OK,
                                     10 NOT YET MIGRATED, 1 NO DERIVED LINE, 1
                                     UNMARKED CONVERSION; 18 conversion(s)
                                     checked.
  Constants export check       1.3s  Export matches the store: sha256
                                     9ecbd38ff122 on both sides; 101 rows
                                     re-read, 56 not exported, 27 tokens; 310
                                     conversions re-computed, 10 of 10 worked
                                     cases hold.
  Objects export check         0.1s  pass
  Skill headers                0.2s  11 skills parsed, no consistency problems.
  Exact rows by the count      1.6s  PASSING -- 13 printed exact rows each state
                                     a count; 32 orrery lines print through
                                     exact_text() or row_text(); 10 gallery lines
                                     are served the count
  Dimensions                   1.8s  No unit contradicts its arithmetic: 52
                                     derived row(s) read -- 40 OK, 9 NO UNIT, 3
                                     NOT CHECKABLE.
  Cross-check annotations      0.3s  19 of 19 cross-check annotation tests
                                     passed.
  Citation inheritance         0.2s  20 of 20 citation-inheritance tests passed.
  Status lines                 0.2s  All 101 status lines in constants_new.py are
                                     well formed; 53 rows carry none.
  Row shape                    0.1s  All 157 row shapes in constants_new.py fit
                                     the assignment's own line.
  Scanner recognition 1d/1e    0.4s  27 of 27 recognition pins hold: real
                                     citations recognized, fake ones refused.
  Reset completeness          24.1s  PASS -- all 309 IntVars + 3 StringVars + 10
                                     entries reset to startup defaults; date set
                                     to now.
  Orbit cache                  2.4s  All 6 orbit cache tests passed: cache loads,
                                     old formats convert, corrupted entries are
                                     dropped.
  Earth pole of date           0.3s  all 14 checks passed (geometry, ERFA,
                                     fallback, cache, hover, transform).
  Worksheet checker           10.1s  74 of 110 routed, 8 clean
  Worksheet checker tests     15.9s  All 135 checks passed
  Worksheet key round trip     1.1s  RESULT: 52 sites minted 52 distinct keys,
                                     all resolved; 52 pinned keys still resolve;
                                     1 retired keys confirmed gone.
  Builder marker join         24.4s  All 76 checks passed
  Extractor pins               0.5s  RESULT: 29 string sites carry the pinned 73
                                     claims and 14 instruction drops, at LOOKBACK
                                     30 / LOOKAHEAD 25, extractor version 2.
  Provenance scanner          12.0s  298 TIER-1 FINDINGS IN THE SCANNED TREE

======================================================================
  20 of 20 gating checkers passed -- 114.8s total
  2 report-only, exit 0 whatever they find:
    Worksheet checker           74 of 110 routed, 8 clean
    Provenance scanner          298 TIER-1 FINDINGS IN THE SCANNED TREE
======================================================================

FILES WRITTEN THIS RUN
----------------------------------------------------------------------
  2059 file(s) examined, 9 written, 0 created, 0 removed, 3 rewritten identically
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

  2. Move this script into documentation/; commit and push.
  3. Reinstall safe-file-editing (Settings > Skills) from
     skills/safe-file-editing/SKILL.md, and replace the Project's
     instructions with PROJECT_INSTRUCTIONS.md (v3.80).
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 

===============================================================================

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/patch_L133_1_crlf_sweep_20261004.py
ok  .gitignore                                   line endings: CRLF -> LF
ok  LEDGER_CONSOLIDATED.md                       L-133: status line
ok  LEDGER_CONSOLIDATED.md                       L-133: done
ok  LEDGER_CONSOLIDATED.md                       L-415: L-133 done the same session
ok  LEDGER_CONSOLIDATED.md                       header stamp
ok  catalog_selection.py                         line endings: CRLF -> LF
ok  create_cache_backups.py                      line endings: CRLF -> LF
ok  data_acquisition.py                          line endings: CRLF -> LF
ok  data_acquisition_distance.py                 line endings: CRLF -> LF
ok  data_processing.py                           line endings: CRLF -> LF
ok  documentation/HANDOFF_L413_ledger_sweep_and_earth_list_20261004.md item 5
ok  documentation/HANDOFF_L413_ledger_sweep_and_earth_list_20261004.md tony-actions
ok  documentation/WHERE_WE_ARE.md                changed this session
ok  documentation/WHERE_WE_ARE.md                waiting on you: the 22 files done
ok  documentation/WHERE_WE_ARE.md                where the details are
ok  formatting_utils.py                          line endings: CRLF -> LF
ok  hr_diagram_apparent_magnitude.py             line endings: CRLF -> LF
ok  hr_diagram_distance.py                       line endings: CRLF -> LF
ok  messier_object_data_handler.py               line endings: CRLF -> LF
ok  object_type_analyzer.py                      line endings: CRLF -> LF
ok  planetarium_apparent_magnitude.py            line endings: CRLF -> LF
ok  planetarium_distance.py                      line endings: CRLF -> LF
ok  report_manager.py                            line endings: CRLF -> LF
ok  shutdown_handler.py                          line endings: CRLF -> LF
ok  star_notes.py                                line endings: CRLF -> LF
ok  star_properties.py                           line endings: CRLF -> LF
ok  star_properties.py                           line 63 comment: two curly quote pairs made ASCII
ok  stellar_data_patches.py                      line endings: CRLF -> LF
ok  stellar_parameters.py                        line endings: CRLF -> LF
ok  visualization_2d.py                          line endings: CRLF -> LF
ok  visualization_3d.py                          line endings: CRLF -> LF
ok  visualization_core.py                        line endings: CRLF -> LF

All 21 Python files compile.
Stamps updated: the ledger's header (L-133 closed).

patch applied

NEXT:
  1. Run orrery_maintenance_run.py. Every gating check passes.
  2. Move this script into documentation/; commit and push on its
     own. Every line of the 22 files shows as changed: expected.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 
