# Handoff -- L-345: conversions are served and the gallery prints them; orrery patch D20 is next

**Built on orrery `807e9dd535211b2bdb91263b49988e1494c308a8` at
https://github.com/tonylquintanilla/palomas_orrery; pushed at
`2a7d26b9fc200a1ceae6afb3af541e5d60c33f54`. Gallery built on
`2df02f3baead894ff40922bcadef9cb84c49fa07` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io; pushed at
`52da593c50d28803297cebe261fd2be13470c8c3`.** Both HEADs read live with
`git ls-remote` on 2026-09-28. The pushed files of both patches were
compared with the trees this session tested, and they are identical.

**Type: BUILD.** The next session builds orrery patch D20. One small
design question is inside it (section 4, item 3: the orrery crust
hover's words), and Tony answers it before the patch ships.

**Supersedes** `HANDOFF_L345_D19_done_gallery_next_20260928.md` for what
remains; that file stays the record of D18 and D19.
**Companion records:** `documentation/PREBUILD_L345_gallery_hover_changes_20260928.md`
(the before-and-after list, filed by D19a);
`documentation/DESIGN_L345_conversions_computed_20260928.md` and
`documentation/RULING_L345_conversion_count_rule_20260928.md`.
Tony's run records are in
`HANDOFF_L322_D_print_counts_orrery_done_20260928.md`.

**Rules this work ran under:** protocol v3.72. Loaded and confirmed at
session start: provenance-discipline 2.22 and interactive-exhibit 1.5
(the obligation the last handoff carried is discharged), and every other
skill matching the manifest. No skill changed this session; D20 carries
two bumps (section 4, item 6).

Written for Tony, a retired professional engineer who is not a
programmer, and for the session that builds next.

---

## 1. What was built, and how each piece was verified

- **Orrery patch D19a (orrery `b61d1982`).** Two new rows, each Earth's
  equatorial radius plus an altitude the store already held:
  `EARTH_STRATOPAUSE_RADIUS_KM`, 6428 km at 4 figures, and
  `EARTH_THERMOPAUSE_RADIUS_KM`, 6980 km at 3. The export serves them in
  Earth radii as 1.0078 and 1.094. `test_constants_export.py` pins both
  (10 pins, was 8). The ledger records the order on L-345. Tony's
  maintenance run: 19 of 20, the one failure the expected "Exact rows by
  the count".
- **The gallery patch (gallery `7b230cf` and `52da593c`),**
  `patch_L345_gallery_conversions_served_20260928.py`. It carried all of
  gallery patch 4's work, and patch 4 itself was never run.
  - The mirror copies the export's `"in"` onto each served node, and
    writes a slot measured in another unit from its row's `"in"` entry
    for that unit. Nothing is converted in the gallery. Mirror suite
    case 20; shown failing when the mirror ignores `"in"`.
  - Eleven pointers moved off conversion rows onto the rows they come
    from. The two standoffs' `standoff_km` and `standoff_au` nodes were
    removed; the standoff serves both through `"in"` now.
  - The crust points at `EARTH_MEAN_RADIUS_KM` (section 2) and serves
    Tony's approved sentence as a new field, `radius_note`.
  - `feature_renderers.js` prints every km and AU line from `"in"`
    where a node serves it. The AU stays at three figures, except where
    cutting a served value would round a tie (section 2). The Sun's
    radius line prints by a served count and is singular at 1.
  - `smoke_display_figures.js` works the expected lines from `"in"` by
    its own arithmetic, grades the new lines, names each served AU tie in
    its report, and gained two self-test ways to go red. Shown failing
    when the tie rule or the served units are broken. New fixture:
    `documentation/fixture_hovers_L345_on_2df02f3b.json`.
  - The patch also writes `data/constants_export.json` and `.sha` at
    orrery `b61d1982`, so the config and the export it was made from
    travel together (finding in section 5).
  - Every Earth and Sun hover was diffed before and after: exactly the
    approved lines changed, nothing else in any room.
- **Tony's runs:** gallery maintenance run 19 of 19; phone check of both
  rooms "correct"; orrery maintenance run 18 of 18 gating checkers, with
  "Exact rows by the count" PASSING. (The patch's steps said "20 of 20";
  two of the twenty are report-only, so 18 of 18 is the right count.)

## 2. Rulings this session

- **The order (Tony, "confirmed as recommended"):** D19a, then the
  gallery patch, then D20, so every visible change reached one phone
  check.
- **The three-figure AU line and a tie (Tony, 2026-09-28):** where
  cutting a served, already-rounded AU value to three figures would
  round a tie -- the dropped digits exactly a 5 -- the page prints the
  served digits in full. Today that is the inner core, 0.000008165 AU.
  Checked against the skills in chat: it is Rule 7's main rule, not a
  new exception; what the skills lack is a sentence saying when the
  exception steps aside (section 4, item 6).
- **The crust is drawn at Earth's mean radius (Tony, 2026-09-28: "let's
  just do it now").** Reasons agreed in chat: a sphere at the mean
  radius stays nearer sea level everywhere than one at the equatorial
  radius, and the interior layers come from PREM, whose surface is the
  6,371 km sphere -- the store's own upper-mantle row says "24.4 km
  below the mean radius". The Earth radius as a UNIT stays equatorial:
  Prsa et al. (2016), AJ 152:41, on IAU 2015 Resolution B3, reads an
  unqualified terrestrial radius as the equatorial one. Tony, on why:
  it is a drawing choice, because we draw a sphere, not the flattened
  shape.
- **The crust's words (Tony, "approved"):** "This is Earth's mean
  radius: the radius of a ball with the same volume as the smooth,
  slightly flattened shape fitted to sea level. The Earth radius used as
  a unit here is the equatorial radius, as the International
  Astronomical Union recommends, so the mean radius is a little less
  than one. The ground itself rises and falls from this by kilometres."
- **The mean radius keeps its 7 figures.** 6,371.000 km is the radius of
  the ball with the reference ellipsoid's volume; recomputed from the
  ellipsoid's axes it agrees within a metre either way. The figures
  describe the model, and the hover says so.
- **Wait for D20 (Tony):** until D20, the orrery draws the crust at
  6,378 km while the gallery draws it at 6,371 km. Invisible at that
  scale, and no check compares the two.

## 3. The two questions Tony asked at the close

**Does D20 close Earth's slice?** Earth's slice closed earlier, in the
sense the export uses: `closed_slices` has been `["EARTH"]`, every
`EARTH_` row visited and gated. L-322 Stage D's finishing condition
(its Gap of 2026-09-28) was met by the gallery patch: "Exact rows by the
count" passes with the gallery beside the orrery, and the gallery run
passes. D20 finishes L-345, the conversion work. What stays open on
Earth after it is recorded classes, not the slice: chiefly the orrery's
own Earth hovers, which format numbers by a width chosen at each line
(L-352, L-387) and which no checker reads.

**Does it close the Sun's slice?** No. That is its own build, and the
next body after Earth under L-322's Gap. Today `closed_slices` is Earth
only; 14 of the Sun room's links point at rows with no `# Unit:` line
and are not exported, so the mirror leaves them as hand-typed values
(L-371, L-386). The Sun's slice walks each of those rows once, re-homes
each conversion row to the unit its source gives (L-386), and only then
closes. The chromosphere is already done, which is a start.

## 4. What D20 builds

1. **The rows.** The 13 conversion rows stop being rows:
   `EARTH_INNER_CORE_RADII`, `EARTH_OUTER_CORE_RADII`,
   `EARTH_LOWER_MANTLE_RADII`, `EARTH_UPPER_MANTLE_RADII`,
   `EARTH_GEOSTATIONARY_RADII`, `EARTH_LEO_INNER_RADII`,
   `EARTH_LEO_OUTER_RADII`, `EARTH_HILL_SPHERE_RADII`,
   `EARTH_MAGNETOPAUSE_STANDOFF_KM`, `EARTH_MAGNETOPAUSE_STANDOFF_AU`,
   `EARTH_BOW_SHOCK_STANDOFF_KM`, `EARTH_BOW_SHOCK_STANDOFF_AU`, and
   `CHROMOSPHERE_PHYSICAL_RADII` (re-written as
   `CHROMOSPHERE_TOP_KM / SUN_RADIUS_KM`). Also
   `EARTH_STRATOPAUSE_RADII` and `EARTH_THERMOPAUSE_RADII`, re-written as
   their new kilometre rows divided by `EARTH_EQUATORIAL_RADIUS_KM`.
   Each keeps its name and `# Unit:` line, loses `# Figures:` and
   `# Status:`, and gains a marker the reader recognizes, naming its
   source row. The export lists it under not_exported with that reason;
   the closed-slice gate skips it. **Measured at gallery `52da593c`: no
   gallery pointer names any of these fifteen**, so the gallery is not
   touched.
2. **The check that can fail.** `test_derived_figures.py` gains Rule 8's
   widening: a row that is one row scaled only by exact rows, and is not
   marked as a conversion, fails by name. Show it failing before
   trusting it.
3. **The orrery's crust moves to the mean radius.** In `shell_configs.py`
   Earth's crust `radius_fraction` is 1.0 today; it becomes the mean
   radius over the equatorial, computed from the two rows, not typed.
   The crust's hover says "Source (radius): IERS Conventions (2010) ...
   equatorial radius" and must change. **Its new words go to Tony before
   the patch ships**; the gallery's approved sentence is the obvious
   start. In `constants_new.py`, the FRAME NOTE above
   `EARTH_MEAN_RADIUS_KM` (about 7 km between the drawn surface and
   PREM's) and that row's own note ("NOT the radius the orrery draws
   to") must be rewritten, and the L-249 comment beside the crust's
   `info_polar_deg` ("about 31 km") becomes 24.4 km. Mode 5 in the
   orrery: Tony's eye on the Earth interior.
4. **Hold every other orrery hover byte for byte,** with the pre-delivery
   test (agentic-pre-test), because this is display code. One orrery
   hover prints a conversion name by its count: the Sun's chromosphere,
   `CHROMOSPHERE_PHYSICAL_RADII` at 1.003; after it loses its
   `# Figures:` line it needs a count, and the computed count is 4, the
   same. No other conversion name is printed through `figures_of()` or
   `_declared()` (measured at `807e9dd5`; re-measure at `2a7d26b9`).
5. **The master plan restamps to v34** with an executive summary at the
   top, written from the current state; section 5a stays the critical
   path, brought current; both companion files get a short retirement
   line; L-333 and L-362 close pointing at v34 (Tony's ruling of
   2026-09-28, recorded in the superseded handoff, section 2).
6. **Two skill bumps, one commit, one protocol entry (v3.73),** under the
   binding rule; v3.70 moves down to the history file.
   - **ledger-and-session-records 1.11 -> 1.12:** The Document Stack --
     the plan is one document at two zooms, executive summary and body,
     with the critical path inside the body; the summary is rewritten at
     every restamp.
   - **interactive-exhibit 1.5 -> 1.6:** under Provenance is part of the
     build, (a) where cutting a served AU to three figures would round a
     tie, the served digits print in full, and the hover check names
     each case; (b) the mirror serves a slot measured in another unit
     from its row's `"in"`; (c) a shell may serve a `radius_note`, a
     sentence under its radius line where the number needs one to be
     read rightly. Tony was told (a) would be written here.
   - Check first that no other session has bumped either skill since
     `2a7d26b9`.

## 5. For the ledger, one row per class, filed by D20

- **L-345 closes** when D20 lands: the gallery prints from `"in"`
  (gallery `52da593c`) and the store holds no conversion rows.
- **L-333 and L-362 close** with the plan's v34.
- **L-322** gains a note: Stage D's finishing condition met at orrery
  `2a7d26b9` and gallery `52da593c`; its Gap's point (2) is done
  (L-345 decided and built); point (3), the Sun's slice, is next.
- **New row -- the pull that cannot fail.** In the gallery maintenance
  run, "Constants export pull" reported PASS "no change" in this
  session's sandbox when it could not reach GitHub at all (an N-A inside
  it), and "Config mirror" then rewrote the config from the older export
  still on disk: 36 fields written backwards and 5 links refused. Tony's
  runs reach GitHub, so it has not happened there, and the gallery patch
  shipped its export to rule it out this time. The class: a generator
  whose failure prints as success, followed by a writer that trusts it.
  (A Check That Cannot Fail Is Not Passing.)
- **The crust ruling** is recorded on L-345's closing note, with the
  orrery crust move that completes it.
- **L-387** gains a line: the orrery prints the LEO edges as "1.03 to
  1.31 Earth radii" (`earth_visualization_shells.py`, `.2f`), shorter
  than the gallery's served count. Same value, a width chosen on the
  line.

## 6. For the next session

- Confirm the loaded skills match the manifest.
- Re-anchor both repositories.
- Build section 4, in the order given; bring Tony the orrery crust
  hover's words before delivery.

## 7. Tony-actions

- (do) File this handoff in the orrery's `documentation/`.
- (do) File the unrun `patch_L322_D_p4_gallery_print_counts_20260927.py`
  in the gallery's `documentation/`, as a record; the gallery patch
  carried its work.
- (decide, in the D20 session) The orrery crust hover's new words.
- (decide, still open) The Sun's Auto view, L-385.

---

Session written September 2026 with Anthropic's Claude Opus 5.5.

========================================================================

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/patch_L322_D_20_L345_conversions_retired_20260928.py
ok    constants_new.py: edit 1
ok    constants_new.py: edit 2
ok    constants_new.py: edit 3
ok    constants_new.py: edit 4
ok    constants_new.py: edit 5
ok    constants_new.py: edit 6
ok    constants_new.py: edit 7
ok    constants_new.py: edit 8
ok    constants_new.py: edit 9
ok    constants_new.py: edit 10
ok    constants_new.py: edit 11
ok    constants_new.py: edit 12
ok    constants_new.py: edit 13
ok    constants_new.py: edit 14
ok    constants_new.py: edit 15
ok    constants_new.py: edit 16
ok    constants_rows.py: edit 1
ok    constants_rows.py: edit 2
ok    constants_rows.py: edit 3
ok    constants_rows.py: edit 4
ok    constants_rows.py: edit 5
ok    constants_rows.py: edit 6
ok    export_constants.py: edit 1
ok    export_constants.py: edit 2
ok    export_constants.py: edit 3
ok    export_constants.py: edit 4
ok    export_constants.py: edit 5
ok    export_constants.py: edit 6
ok    test_constants_export.py: edit 1
ok    test_constants_export.py: edit 2
ok    test_constants_export.py: edit 3
ok    test_constants_export.py: edit 4
ok    test_constants_export.py: edit 5
ok    test_derived_figures.py: edit 1
ok    test_derived_figures.py: edit 2
ok    test_derived_figures.py: edit 3
ok    test_derived_figures.py: edit 4
ok    test_derived_figures.py: edit 5
ok    test_derived_figures.py: edit 6
ok    test_derived_figures.py: edit 7
ok    test_derived_figures.py: edit 8
ok    test_derived_figures.py: edit 9
ok    test_derived_figures.py: edit 10
ok    test_derived_figures.py: edit 11
ok    test_derived_figures.py: edit 12
ok    test_derived_figures.py: edit 13
ok    test_derived_figures.py: edit 14
ok    test_derived_figures.py: edit 15
ok    test_derived_figures.py: edit 16
ok    test_derived_figures.py: edit 17
ok    test_derived_figures.py: edit 18
ok    test_derived_figures.py: edit 19
ok    test_derived_figures.py: edit 20
ok    test_derived_figures.py: edit 21
ok    test_derived_figures.py: edit 22
ok    test_derived_figures.py: edit 23
ok    test_derived_figures.py: edit 24
ok    shell_configs.py: edit 1
ok    shell_configs.py: edit 2
ok    shell_configs.py: edit 3
ok    shell_configs.py: edit 4
ok    shell_configs.py: edit 5
ok    solar_visualization_shells.py: edit 1
ok    solar_visualization_shells.py: edit 2
ok    solar_visualization_shells.py: edit 3
ok    LEDGER_CONSOLIDATED.md: edit 1
ok    LEDGER_CONSOLIDATED.md: edit 2
ok    LEDGER_CONSOLIDATED.md: edit 3
ok    LEDGER_CONSOLIDATED.md: edit 4
ok    LEDGER_CONSOLIDATED.md: edit 5
ok    LEDGER_CONSOLIDATED.md: edit 6
ok    LEDGER_CONSOLIDATED.md: edit 7
ok    LEDGER_CONSOLIDATED.md: edit 8
ok    LEDGER_CONSOLIDATED.md: edit 9
ok    PROJECT_INSTRUCTIONS.md: edit 1
ok    PROJECT_INSTRUCTIONS.md: edit 2
ok    PROJECT_INSTRUCTIONS.md: edit 3
ok    documentation/PROJECT_INSTRUCTIONS_HISTORY.md: edit 1
ok    documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md: edit 1
ok    documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md: edit 2
ok    documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md: edit 3
ok    documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md: edit 4
ok    documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md: edit 5
ok    documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md: edit 6
ok    documentation/MASTER_PLAN_INTERACTIVE_GALLERY_SUMMARY.md: edit 1
ok    documentation/MASTER_PLAN_CRITICAL_PATH_SUMMARY.md: edit 1
ok    skills/ledger-and-session-records/SKILL.md: edit 1
ok    skills/ledger-and-session-records/SKILL.md: edit 2
ok    skills/ledger-and-session-records/SKILL.md: edit 3
ok    skills/interactive-exhibit/SKILL.md: edit 1
ok    skills/interactive-exhibit/SKILL.md: edit 2
ok    documentation/HANDOFF_L345_D20_done_20260928.md: new, 9868 bytes
ok    documentation/project_instructions_v3_73.md: new, 71885 bytes
PATCH APPLIED: 15 files changed, 2 new.

NEXT STEPS, in this order:

  1. (do) Run the orrery maintenance run (orrery_maintenance_run.py).
     It rewrites data/constants_export.json (76 rows exported, was 91),
     the ledger index and the skill manifest. Expect every checker to
     pass. "Derived figures" should end "... 29 derived row(s) read, 17
     judged OK -- ... 1 UNMARKED CONVERSION; 15 conversion(s) checked."
     The one UNMARKED CONVERSION is the Sun's SOLAR_RADIUS_AU, a named
     gap, not a failure. "Constants export check" should end "... 76
     rows re-read, 66 not exported, 26 tokens; 160 conversions
     re-computed, 10 of 10 worked cases hold."

======================================================================
MAINTENANCE RUN -- generators, then checkers (L-188)
======================================================================
  Provenance scan is current (last run 20260929T033343Z, 0 day(s) ago).

GENERATORS -- regenerate every time; a no-op when nothing moved
----------------------------------------------------------------------
  Ledger index                 0.9s  rewrote LEDGER_CONSOLIDATED.md
  Skill manifest               0.1s  rewrote PROJECT_INSTRUCTIONS.md
  Constants export             0.6s  rewrote data/constants_export.json
  Module atlas                 6.2s  rewrote MODULE_ATLAS.md, MODULE_INDEX.md
  Data inventory               4.2s  rewrote DATA_INVENTORY.md
  Exact rows report            1.3s  rewrote EXACT_ROWS_PRINTED.md -- 8 of 21
                                     exact rows printed at 19 lines (9 orrery, 10
                                     gallery); 5 drawn only, 0 not followed, 0
                                     map entries broken
  Document index               0.1s  unchanged (1 checked, not written)

CHECKERS -- verdict informs the push call
----------------------------------------------------------------------
  Constants change             0.3s  5 derived line(s): 5 changed, 0 added, 0
                                     removed
  Constants relations          0.2s  21 of 21 provenance tests passed against
                                     constants_new.py. No constants have drifted.
  Derived figures              0.8s  No figure count exceeds its inputs: 29
                                     derived row(s) read, 17 judged OK -- 17 OK,
                                     12 NOT YET MIGRATED, 1 NO DERIVED LINE, 1
                                     UNMARKED CONVERSION; 15 conversion(s)
                                     checked.
  Constants export check       1.0s  Export matches the store: sha256
                                     b6d8bfdb21f6 on both sides; 76 rows re-read,
                                     66 not exported, 26 tokens; 160 conversions
                                     re-computed, 10 of 10 worked cases hold.
  Exact rows by the count      1.1s  PASSING -- 8 printed exact rows each state a
                                     count; 9 orrery lines print through
                                     exact_text(); 10 gallery lines are served
                                     the count
  Dimensions                   1.0s  No unit contradicts its arithmetic: 44
                                     derived row(s) read -- 32 OK, 9 NO UNIT, 3
                                     NOT CHECKABLE.
  Cross-check annotations      0.1s  19 of 19 cross-check annotation tests
                                     passed.
  Citation inheritance         0.1s  20 of 20 citation-inheritance tests passed.
  Status lines                 0.1s  All 78 status lines in constants_new.py are
                                     well formed; 61 rows carry none.
  Row shape                    0.1s  All 142 row shapes in constants_new.py fit
                                     the assignment's own line.
  Scanner recognition 1d/1e    0.2s  27 of 27 recognition pins hold: real
                                     citations recognized, fake ones refused.
  Reset completeness          18.0s  PASS -- all 309 IntVars + 3 StringVars + 10
                                     entries reset to startup defaults; date set
                                     to now.
  Orbit cache                  1.7s  All 6 orbit cache tests passed: cache loads,
                                     old formats convert, corrupted entries are
                                     dropped.
  Earth pole of date           0.3s  all 14 checks passed (geometry, ERFA,
                                     fallback, cache, hover, transform).
  Worksheet checker            8.1s  76 of 114 routed, 8 clean
  Worksheet checker tests     14.7s  All 136 checks passed
  Worksheet key round trip     0.9s  RESULT: 52 sites minted 52 distinct keys,
                                     all resolved; 52 pinned keys still resolve;
                                     1 retired keys confirmed gone.
  Builder marker join         19.9s  All 76 checks passed
  Extractor pins               0.4s  RESULT: 29 string sites carry the pinned 73
                                     claims and 14 instruction drops, at LOOKBACK
                                     30 / LOOKAHEAD 25, extractor version 2.
  Provenance scanner           9.7s  296 TIER-1 FINDINGS IN THE SCANNED TREE

======================================================================
  18 of 18 gating checkers passed -- 92.2s total
  2 report-only, exit 0 whatever they find:
    Worksheet checker           76 of 114 routed, 8 clean
    Provenance scanner          296 TIER-1 FINDINGS IN THE SCANNED TREE
======================================================================

FILES WRITTEN THIS RUN
----------------------------------------------------------------------
  2008 file(s) examined, 11 written, 0 created, 0 removed, 3 rewritten identically
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
    rewritten with identical bytes, no action needed:
      data/worksheet_check_state.json
      data/worksheet_routed.json
      test_output/test_orbit_paths.json
    20 file(s) over 2 MB compared by size and mtime only

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>

  2. (do) Open the orrery and look at Earth's interior (Mode 5). The
     crust should look the same; its hover should end with the new
     paragraph about the mean radius, 6,371.000 km. -- correct
  3. (do) Move this script into documentation/. Commit everything and
     push.
  4. (do) Reinstall ledger-and-session-records and interactive-exhibit
     from skills/ to Settings > Skills.

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 
