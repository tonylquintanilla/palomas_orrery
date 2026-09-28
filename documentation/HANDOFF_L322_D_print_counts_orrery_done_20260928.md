# Handoff -- L-322 Stage D: exact rows print by their counts (orrery done); the gallery half and the Sun room are next

**Built on orrery `0e3d05fd498f1ae8b49ec5dba58503f6bf448576` at
https://github.com/tonylquintanilla/palomas_orrery; pushed at
`a7868eee04575abeeae303a6ca6a700890e835f1`. Gallery read at
`2df02f3baead894ff40922bcadef9cb84c49fa07` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io; this
session pushed nothing to the gallery.** Both HEADs read live with
`git ls-remote` on 2026-09-28.

**Type: BUILD.** The next session builds one gallery patch and runs no
design round first, unless it finds something below to be wrong.

**Supersedes** `HANDOFF_L322_D_gallery_patch3_done_20260926.md` for what
remains; that handoff stays the record of gallery patch 3 and D13, and
its section 4 ledger rows are still owed (section 5 below). **Companion
record:** `documentation/RUN_RECORD_L322_D13_20260926.md`. Despite its
name it now holds Tony's runs of D14, D15, D16 and D17 as well; the
next session starts its own run record.

**Rules this work ran under:** protocol v3.69 at the start, v3.71 at
the end. provenance-discipline: this session LOADED 2.19 and shipped
2.20 (D14) and then 2.21 (D16, Claude Fable 5.1's recommendation). A
reinstall cannot be verified from inside the session that makes it, so
**the next session confirms its loaded copy reads 2.21 before any
provenance, constants_new.py or print-count work.** 2.21 is the version
the gallery patch below is built to. Other skills unchanged:
interactive-exhibit 1.4, gallery-cache-builder 1.6, gallery-assembler
1.3, safe-file-editing 1.11, agentic-pre-test 1.2,
ledger-and-session-records 1.11. This session shipped two versions of
one skill, which the ledger skill's ONE SESSION, ONE BUMP rule says not
to do; the v3.71 protocol entry says so openly.

Written for Tony, a retired professional engineer who is not a
programmer, and for the session that builds the gallery half.

---

## 1. What was built, and how each piece was verified

All four are orrery patches. Tony ran each from the orrery root,
followed it with the orrery maintenance run, and pushed.

- **D14, provenance-discipline 2.19 -> 2.20.** Rule 2 now says where a
  trailing ".0" comes from: Python, by three routes (a decimal point is
  typed to make a float; division always returns a float; a float
  printed with no format always shows ".0"). None of them is a
  statement about significant figures, so a count is never read from a
  literal, a printed value or the export. Checked by running Python 3
  and Node. Rule 7's exact row was brought into line with D15's code.
- **D15, manifest section 6's orrery half.** The seven exact rows a
  display prints state a print count on their `# Figures:` line,
  directly after `exact --`: the LEO edge 4, the LEO floor 3, the outer
  belt peak 2, the solar wind pressure 1, Bz 1, the two cut angles 3.
  `constants_rows.py` reads the count and refuses one larger than the
  number's digits, one too small to write it in full, and anything but
  1 on a zero. The export serves it as `"prints"` (schema 5). The
  orrery's eight printing lines print through `exact_text()`; their
  text did not change, checked byte for byte through the live builders.
  `exact_rows_report.py --check` is a new pass/fail checker in the
  maintenance run, "Exact rows by the count", with a dashboard button.
  In passing: `test_constants_export.py` now compares `uncertainty`,
  which it had not since schema 4, and the maintenance run's own
  docstring count of gating checkers was corrected.
- **D16, provenance-discipline 2.20 -> 2.21, and protocol v3.71.** A
  sum or difference scaled by an exact row keeps its decimal place,
  carried through the scaling, not its figure count. The case: the top
  of the chromosphere, 695,700 km (exact) + about 2,000 km (one figure)
  is good to thousands; divided by the exact solar radius it is good to
  thousandths, 1.003 solar radii. Counted by fewest figures it would
  have been 1.00, and the export would then have drawn the chromosphere
  on the photosphere. Wikipedia's Significant figures page, the skill's
  reference, names this as its unit-conversion exception (8 inches to
  "20. cm"); checked by fetching the page. Fable's eight edits went in
  unchanged plus one sentence: a single measured value scaled by an
  exact row stays under fewest figures for now.
- **D17, the chromosphere rows and the checker.** `SUN_RADIUS_KM` is
  exact, "prints 4" (the IAU 2015 nominal radius, 6.957 x 10^5 km).
  `CHROMOSPHERE_PHYSICAL_KM` has one figure. `CHROMOSPHERE_TOP_KM` is
  new, 698,000 km at three figures. `CHROMOSPHERE_PHYSICAL_RADII` is
  the sum over the radius and counts to 4 figures, 1.003.
  `test_derived_figures.py` applies the scaling rule and prints the
  place it kept; five new built-in rows test it, two of them refused
  on purpose, and every existing row's verdict was unchanged. The
  orrery's chromosphere hover reads "1.003 solar radii" (was 1.002875)
  and "roughly 0.3%" of the radius (was 0.29%). `exact_rows_report.py`
  lists the gallery's three `SUN_RADIUS_KM` pointers as DRAWN: the Sun
  room uses the row only to turn solar radii into kilometres.

**State after D17, from Tony's run:** 19 of 20 checkers pass. The one
failure is "Exact rows by the count", and it is correct: it names the
Earth room's eleven gallery prints, which the gallery does not yet serve
a count for. It clears when the gallery patch below lands and the orrery
maintenance run is run again.

## 2. Rulings this session (Tony, 2026-09-27 and 2026-09-28)

- Each exact row prints the digits it was defined or chosen with; the
  counts in section 1 follow. Decided as the skill's rule, not case by
  case.
- The trailing ".0" is Python's: checked, and written into the skill.
- The checker also refuses a count too small to write the number in
  full, and a declared construction prints the digits of the value its
  rule gives (4.5 prints two). Approved on the condition that the code,
  the provenance rules and the significant-figure rules agree; they
  were compared line by line before D15 and D16 shipped.
- The crust's hover reads "Radius: 1 Earth radius", not "1.0000 Earth
  radii". One Earth radius is the equatorial radius of IERS Conventions
  (2010), a definition, so the crust's 1 is exact.
- The chromosphere prints 1.003 solar radii (Fable's recommendation,
  2.21). The kilometre line gets its own row, 698,000 km, and the
  Sun's radius is exact and prints 4.

## 3. What remains: ONE gallery patch, rebuilt

Gallery patch 4 was built and tested in this session
(`patch_L322_D_p4_gallery_print_counts_20260927.py`) but **must not be
run as it is.** It was built before D17. Simulated on the gallery at
`2df02f3b` with D17's export: the mirror step writes four Sun links as
well as Earth's (the three `sun_radius` nodes become exact with prints
4, and the chromosphere radius becomes 1.003 with figures 4), so the
patch's "mirror changes nothing" promise is false; and the display
smoke check fails, because the chromosphere's hover changes against the
recorded fixture. So the next session builds **one** gallery patch that
carries patch 4's work and the Sun room's, and records one new fixture.

**Patch 4's work, to carry forward unchanged** (Tony can give the
session the file; everything in it was tested on 2026-09-27):

- `tools/mirror_constants.py` copies `"prints"`; the definition case
  (the crust's 1 by definition) writes `"prints": 1`.
  `tools/test_mirror_constants.py` gains case 19.
- `gallery/feature_renderers.js`: `servedFigures()` returns an exact
  node's `prints`; an exact ROW (a node with its own `orrery_constant`)
  served with no count is printed in full and reported as a warning,
  never given a width. The LEO altitude and the belts print by the
  count. The Earth "Radius:" line is singular at exactly 1.
- `documentation/smoke_display_figures.js`: the LEO rule reads the
  count, the magnetopause and bow shock are graded on their new lines,
  and two self-test ways are added (the page reads a served count; the
  page reports an exact row served without one).
- Visible changes in the Earth room: "Bz 0 nT, dynamic pressure 2 nPa",
  "at dynamic pressure 2 nPa", "Radius: 1 Earth radius". Nothing else.

**The Sun room's work, new:**

- The Sun's "Radius:" line (in `feature_renderers.js`, the `r_sun`
  branch that prints `cfg.radius.value` raw) prints by the served count
  where one is served, and exactly as today where none is. Most Sun
  shells serve no count, and `fmtServed`'s fallback would give them a
  fixed width such as "19.7000"; that must not happen. Singular at
  exactly 1: "1 solar radius".
- The chromosphere's kilometre line prints from `CHROMOSPHERE_TOP_KM`,
  698,000 km, three figures, not from 1.003 x 695,700 (which would
  print "697,800 km" at four figures). This needs a served pointer on
  the chromosphere entry, which only the mirror or `store_writer` may
  write (interactive-exhibit skill); the session decides the node's
  name. Check the AU in brackets: computed from the full digits it is
  0.00466; computed from the rounded served 698,000 it would be
  0.00467. Rule 4 says the first.
- Expected visible changes in the Sun room: the chromosphere reads
  "Radius: 1.003 solar radii" and "= 698,000 km"; the photosphere
  reads "Radius: 1 solar radius". The session lists every changed
  hover, today and after, before building (manifest section 6, step 5),
  and Tony checks them on his phone.

**Order of Tony's runs after the patch:** cache build by hand, the
gallery maintenance run (the mirror step should then change nothing),
commit and push, the phone check, then the orrery maintenance run, where
"Exact rows by the count" should pass.

**Finished means** the orrery's "Exact rows by the count" passes with
the gallery beside it, and the gallery's maintenance run passes 17 of 17
with the new fixture.

## 4. Things noticed, for the ledger (one row per class)

New this session:

- **Sun room radii printed with no count.** The `r_sun` hover branch
  prints served values raw; the chromosphere and the photosphere are
  fixed by the patch above, and the others (such as the Alfven surface,
  19.7) stay raw until their rows carry counts.
- **The orrery's solar hover prints AU at fixed widths** (`:.5f` on
  `SOLAR_RADIUS_AU`, which has no `# Figures:` line yet). Part of L-352's
  class; the chromosphere's AU happens to match its count.
- **2.21 leaves a single measured value scaled by an exact row under
  fewest figures.** If a future row needs the reference page's full
  unit-conversion exception, the rule is widened then, deliberately.
- **ONE SESSION, ONE BUMP was bent**: this session shipped 2.20 and
  landed 2.21. Recorded in the v3.71 entry; noted so it is not repeated
  by habit.

Still owed from the previous handoff, section 4, none of it filed yet
(checked against `LEDGER_CONSOLIDATED.md` at `a7868eee`): the four new
rows (Jupiter's unsourced belt thickness; the recorded Earth scene
overlaid piece by piece; the magnetotail hover at the 17-line ceiling;
no Wikipedia article for the magnetotail), and the closures of L-311
(DONE), L-325 (close, superseded by L-322) and L-342 (close). Its
carried list stands as written there.

The highest handle in the ledger at `a7868eee` is L-367 (the other
chat's L-363 to L-367 were filed), so the next free handle is L-368.
Re-read the ledger index before assigning one.

## 5. For the next session

- Confirm the loaded provenance-discipline reads **2.21**, and the
  other skills match the manifest.
- File the ledger rows of section 4 and of the previous handoff, and
  the three closures, in one ledger patch, before or beside the gallery
  patch. Tony-actions are "do" steps the patch prints, not hand edits.
- Build the one gallery patch of section 3 on the gallery's HEAD at the
  time; its files may have moved.

## 6. Tony-actions

- (do) File this handoff in the orrery's `documentation/`.
- (do) Delete the second copy of
  `patch_L322_D_17_chromosphere_rows_20260928.py` in the orrery root;
  the copy in `documentation/` is the record.
- (do) Keep `patch_L322_D_p4_gallery_print_counts_20260927.py` from this
  chat's downloads, unrun, and give it to the next session as the
  source of patch 4's work. Do not run it.
- (decide) The Sun's Auto view, carried from the previous two handoffs.

---

Session written September 2026 with Anthropic's Claude Opus 5.5.

==========================================================================

The ledger patch is ready. It is larger than the handoff suggested, and here is why.

While checking which rows were owed, I found that nothing from Stage D had ever been filed in `LEDGER_CONSOLIDATED.md`. Five handoffs and the Stage D manifest each carried a list "for the ledger" and passed it on to the next session. That is how items get lost, so this patch files all of them at once:

- **18 new items, L-368 to L-385.** Each covers one kind of problem. One of them is L-385, the Sun's Auto view decision you've been carrying for four handoffs. It now has a home in the ledger.
- **A line added to six existing items.** These are cases where the new finding is the same kind of problem as one already recorded. For example, the gallery cache builder's own copy of the AU conversion joins L-243, which already tracks those copies.
- **A status note on L-322** saying where Stage D stands.
- **L-311, L-325 and L-342 closed**, per your rulings of 2026-09-22.

Where I could check a claim against the repositories today, the ledger text marks it as verified. Where the claim is carried over from a handoff, it says so. The script lists every new item by name at its top.

I tested it on a copy of the orrery. It applied cleanly. `ledger_index.py` then moved the three closed items to the archive section and indexed all 18 new ones. A second run refuses and writes nothing, as it should.

**To run it:** put the file in the orrery root, click Run, then run `ledger_index.py` and the orrery maintenance run. The maintenance run should still show 19 of 20 passing. The one failure is "Exact rows by the count," and it clears only when the gallery patch lands. Then move the script into `documentation/`, commit, push, and tell me the new orrery SHA. After that I'll turn to the gallery patch.

===========================================================================

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/patch_L322_D_18_ledger_stage_d_rows_20260928.py
ok  LEDGER_CONSOLIDATED.md   <!-- L:360 status:OPEN upd:2026-09-22 section:A flag: ri
ok  LEDGER_CONSOLIDATED.md   **Gap:** Have the budget also measure hovers
ok  LEDGER_CONSOLIDATED.md   <!-- L:352 status:OPEN upd:2026-09-22 section:A flag: ri
ok  LEDGER_CONSOLIDATED.md   **Gap:** Design the helper, then sweep
ok  LEDGER_CONSOLIDATED.md   <!-- L:351 status:OPEN upd:2026-09-22 section:A flag: ri
ok  LEDGER_CONSOLIDATED.md   **Gap:** Each lands with its store's next bump.
ok  LEDGER_CONSOLIDATED.md   <!-- L:350 status:OPEN upd:2026-09-22 section:A flag: ri
ok  LEDGER_CONSOLIDATED.md   **Gap:** Decide whether the magnetotail hover should pri
ok  LEDGER_CONSOLIDATED.md   <!-- L:345 status:OPEN upd:2026-09-22 section:A flag: ri
ok  LEDGER_CONSOLIDATED.md   **Gap:** The decision above, then the next slice builds 
ok  LEDGER_CONSOLIDATED.md   <!-- L:342 status:OPEN upd:2026-09-22 section:A flag:! r
ok  LEDGER_CONSOLIDATED.md   - **Ref:** `gallery/feature_renderers.js`;
ok  LEDGER_CONSOLIDATED.md   <!-- L:325 status:OPEN upd:2026-09-22 section:A flag: ri
ok  LEDGER_CONSOLIDATED.md   **Ref:** L-305, L-314, L-322, `constants_new.py`,
ok  LEDGER_CONSOLIDATED.md   <!-- L:322 status:OPEN upd:2026-09-22 section:A flag: ri
ok  LEDGER_CONSOLIDATED.md   **Ref:** L-305, L-306 (approximations are not promoted),
ok  LEDGER_CONSOLIDATED.md   <!-- L:311 status:OPEN upd:2026-09-10 section:A flag: ri
ok  LEDGER_CONSOLIDATED.md   **Ref:** L-291 (step 3 record), L-292 (not this), proven
ok  LEDGER_CONSOLIDATED.md   <!-- L:243 status:OPEN upd:2026-08-25 section:A flag: ri
ok  LEDGER_CONSOLIDATED.md   routed to L-244.
ok  LEDGER_CONSOLIDATED.md   #### [L-367] No checker opens a new room (checks, galler

patch applied (21 edits)

NEXT:
  1. python ledger_index.py   (moves L-311, L-325, L-342 to C)

CONSISTENCY PROBLEMS:
  - [auto-fix] L-342: status DONE, tagged 'A', but not physically inside any track's own span, so the general archive -- correct tag is 'C'
  - [auto-fix] L-342: belongs in closed bucket 'C' but is not physically located in its destination heading
  - [auto-fix] L-311: status DONE, tagged 'A', but not physically inside any track's own span, so the general archive -- correct tag is 'C'
  - [auto-fix] L-311: belongs in closed bucket 'C' but is not physically located in its destination heading
  - [auto-fix] L-325: status DONE, tagged 'A', but not physically inside any track's own span, so the general archive -- correct tag is 'C'
  - [auto-fix] L-325: belongs in closed bucket 'C' but is not physically located in its destination heading
Retagged 3 block(s) to their correct closed bucket; physically moved 3 block(s) into their bucket's destination heading.
Index regenerated (233 live items) in C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\LEDGER_CONSOLIDATED.md.

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>

OK: 380 L-blocks parsed, no consistency problems.
Index regenerated (233 live items) in C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\LEDGER_CONSOLIDATED.md.

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>

  2. python orrery_maintenance_run.py
     Expect 19 of 20 as before: 'Exact rows by the count'
     still fails until the gallery patch lands.

======================================================================
MAINTENANCE RUN -- generators, then checkers (L-188)
======================================================================
  Provenance scan is current (last run 20260928T200218Z, 0 day(s) ago).

GENERATORS -- regenerate every time; a no-op when nothing moved
----------------------------------------------------------------------
  Ledger index                 0.9s  unchanged (1 of 1 rewritten, content
                                     identical)
  Skill manifest               0.1s  unchanged (1 of 1 rewritten, content
                                     identical)
  Constants export             1.2s  unchanged (1 checked, not written)
  Module atlas                 6.1s  rewrote MODULE_ATLAS.md, MODULE_INDEX.md
  Data inventory               4.3s  unchanged (1 of 1 rewritten, content
                                     identical)
  Exact rows report            1.3s  unchanged (1 checked, not written) -- 8 of
                                     21 exact rows printed at 19 lines (9 orrery,
                                     10 gallery); 5 drawn only, 0 not followed, 0
                                     map entries broken
  Document index               0.1s  unchanged (1 checked, not written)

CHECKERS -- verdict informs the push call
----------------------------------------------------------------------
  Constants change             0.2s  No changes to constants_new.py since HEAD.
  Constants relations          0.2s  21 of 21 provenance tests passed against
                                     constants_new.py. No constants have drifted.
  Derived figures              0.6s  No figure count exceeds its inputs: 42
                                     derived row(s) read, 30 judged OK -- 30 OK,
                                     12 NOT YET MIGRATED, 1 NO DERIVED LINE.
  Constants export check       1.0s  Export matches the store: sha256
                                     278aa6650315 on both sides; 89 rows re-read,
                                     51 not exported, 26 tokens.
  Exact rows by the count      1.2s  FAILED (exit 1) -- FAILING -- 0 row(s)
                                     with...
  Dimensions                   1.1s  No unit contradicts its arithmetic: 42
                                     derived row(s) read -- 30 OK, 9 NO UNIT, 3
                                     NOT CHECKABLE.
  Cross-check annotations      0.1s  19 of 19 cross-check annotation tests
                                     passed.
  Citation inheritance         0.1s  20 of 20 citation-inheritance tests passed.
  Status lines                 0.1s  All 91 status lines in constants_new.py are
                                     well formed; 46 rows carry none.
  Row shape                    0.1s  All 140 row shapes in constants_new.py fit
                                     the assignment's own line.
  Scanner recognition 1d/1e    0.2s  27 of 27 recognition pins hold: real
                                     citations recognized, fake ones refused.
  Reset completeness          17.9s  PASS -- all 309 IntVars + 3 StringVars + 10
                                     entries reset to startup defaults; date set
                                     to now.
  Orbit cache                  1.8s  All 6 orbit cache tests passed: cache loads,
                                     old formats convert, corrupted entries are
                                     dropped.
  Earth pole of date           0.3s  all 14 checks passed (geometry, ERFA,
                                     fallback, cache, hover, transform).
  Worksheet checker            8.9s  76 of 114 routed, 8 clean
  Worksheet checker tests     14.3s  All 136 checks passed
  Worksheet key round trip     0.9s  RESULT: 52 sites minted 52 distinct keys,
                                     all resolved; 52 pinned keys still resolve;
                                     1 retired keys confirmed gone.
  Builder marker join         20.4s  All 76 checks passed
  Extractor pins               0.4s  RESULT: 29 string sites carry the pinned 73
                                     claims and 14 instruction drops, at LOOKBACK
                                     30 / LOOKAHEAD 25, extractor version 2.
  Provenance scanner           9.9s  296 TIER-1 FINDINGS IN THE SCANNED TREE

======================================================================
  1 of 20 checkers FAILED -- 93.6s total
  Exact rows by the count
  2 report-only, exit 0 whatever they find:
    Worksheet checker           76 of 114 routed, 8 clean
    Provenance scanner          296 TIER-1 FINDINGS IN THE SCANNED TREE
======================================================================

FILES WRITTEN THIS RUN
----------------------------------------------------------------------
  1996 file(s) examined, 5 written, 0 created, 0 removed, 7 rewritten identically
    written   MODULE_ATLAS.md
    written   MODULE_INDEX.md
    written   PROVENANCE_AUDIT.md
    written   data/provenance_history.json
    written   documentation/prompts/citation_review.jsonl
    rewritten with identical bytes, no action needed:
      DATA_INVENTORY.md
      LEDGER_CONSOLIDATED.md
      PROJECT_INSTRUCTIONS.md
      WORKSHEET_CHECK.md
      data/worksheet_check_state.json
      data/worksheet_routed.json
      test_output/test_orbit_paths.json
    20 file(s) over 2 MB compared by size and mtime only

----------------------------------------------------------------------
Exact rows by the count -- FAILED (exit 1) -- FAILING -- 0 row(s) with...
----------------------------------------------------------------------
EXACT ROWS PRINTED: 8 of 21 exact rows printed at 19 lines (9 orrery, 10 gallery); 5 drawn only, 0 not followed, 0 map entries broken
  FAIL EARTH_LEO_UPPER_ALTITUDE_KM: gallery gallery/feature_renderers.js line 2022, served prints None, the row states 4
  FAIL EARTH_LEO_LOWER_ALTITUDE_KM: gallery gallery/feature_renderers.js line 2022, served prints None, the row states 3
  FAIL EARTH_VAN_ALLEN_OUTER_RADII: gallery gallery/feature_renderers.js line 1130, served prints None, the row states 2
  FAIL EARTH_VAN_ALLEN_OUTER_RADII: gallery gallery/feature_renderers.js line 1137, served prints None, the row states 2
  FAIL EARTH_VAN_ALLEN_OUTER_RADII: gallery gallery/feature_renderers.js line 1140, served prints None, the row states 2
  FAIL EARTH_VAN_ALLEN_OUTER_RADII: gallery gallery/feature_renderers.js line 1143, served prints None, the row states 2
  FAIL EARTH_SOLAR_WIND_PRESSURE_NPA: gallery gallery/feature_renderers.js line 2278, served prints None, the row states 1
  FAIL EARTH_SOLAR_WIND_PRESSURE_NPA: gallery gallery/feature_renderers.js line 2489, served prints None, the row states 1
  FAIL EARTH_SOLAR_WIND_BZ_NT: gallery gallery/feature_renderers.js line 2277, served prints None, the row states 1
  FAIL EARTH_MAGNETOPAUSE_CUT_ANGLE_DEG: gallery gallery/feature_renderers.js line 2280, served prints None, the row states 3
  FAIL EARTH_BOW_SHOCK_CUT_ANGLE_DEG: gallery gallery/feature_renderers.js line 2491, served prints None, the row states 3
EXACT ROWS BY THE COUNT: FAILING -- 0 row(s) with no count, 0 orrery print(s) by a width, 11 gallery print(s) not served the count

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>

  3. Move this script into documentation/. Commit and push.
  4. Tell Claude the new orrery SHA.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 
