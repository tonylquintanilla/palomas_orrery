<!-- Doc-Kind: hand | Session record for L-437: the provenance scanner's whole-tree Tier-1 total now prints with its domain split everywhere it prints, and a module's domain is read from its own docstring tag (the hand list retired). Build session, one patch. -->
# L-437: the Tier-1 total prints with its domains (build record)

Built on orrery 70202e3bff79136fe6561aab60d42f57b193eda9 at
https://github.com/tonylquintanilla/palomas_orrery ("maintenance").
The gallery is not touched.
Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`;
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.
Written October 13, 2026 with Anthropic's Claude Opus 5.5.

- Type: BUILD. One patch, `patch_L437_1_tier1_by_domain_20261013.py`,
  saved in the orrery's root folder.
- Brief: `documentation/HANDOFF_L437_tier1_by_domain_brief_20261013.md`
  (cut at 400a9615), read after
  `documentation/HANDOFF_scaffolding_sessions_coordination_20261013.md`.
- Ledger: L-437 opened by this patch, status OPEN until Tony's run.
- Skills loaded and checked against the manifest at 70202e3b:
  provenance-discipline 2.28, safe-file-editing 1.13, agentic-pre-test
  1.3, ledger-and-session-records 1.20. All four matched.

## 1. What Tony asked

Tony, 2026-10-12: "the provenance checker is still reporting 288 tier 1
items. Can we separate this into meaningful groups, like orrery, earth
science and stars in the checker report?"

After this patch the scanner's last block reads, on the tree at
70202e3b:

    GATE PATH: 0 TIER-1 -- the push gate holds
    ...
    Whole tree, Tier-1: 281: orrery 116, Earth System 149, stars 13, utilities 2, unclassified 1.

The same line opens the audit's Priority Summary, closes its Gate Path
section, sits in the run history, and is the second half of the
maintenance run's Provenance scanner row.

## 2. Measured at HEAD, before building

- Whole tree 281 Tier-1; gate path 0. (The brief's 280 was at
  400a9615. The 281st is `patch_L436_1_idea_20261013.py`, which sits
  unrun in the root and is scanned there.)
- By the scanner's hand list, MODULE_DOMAIN_MAP: orrery 118, Earth
  System 149, stars 12, utilities 2.
- By each module's docstring Domain: tag: orrery 116, Earth System 149,
  stars 13, utilities 2, and 1 in a file with no tag.
- The two homes disagreed on 14 files with findings:
  - `data_acquisition.py`: tagged stars; its one Tier-1 was counted as
    orrery.
  - `patch_L436_1_idea_20261013.py`: no tag; its one Tier-1 was counted
    as orrery.
  - twelve dev tools filed as orrery, with 38 findings between them,
    all Tier 3: `test_orbit_markers.py`, `test_position_digits.py`,
    `worksheet_checker.py`, `orrery_maintenance_run.py`,
    `doc_index.py`, `worksheet_request_builder.py`,
    `export_constants.py`, `export_drawings.py`, `export_objects.py`,
    `test_dimensions.py`, `worksheet_key_aliases.py`,
    `worksheet_keys.py`.
- Eighteen files with findings were in no hand-list entry and printed
  as the "Domain coverage gap".
- Every root module carries a Domain: tag except the unrun L-436 patch,
  and only the six words are in use (orrery 51, dev_tools 47, stars 27,
  earth_science 19, utilities 7, gallery 1).

## 3. What the patch changes

- `provenance_scanner.py`. MODULE_DOMAIN_MAP is gone. classify_domain()
  reads the module's own Domain: tag through
  module_atlas.classify_domain(), the reader the atlas uses, and is
  given the file's path in the scanned tree. A file with no tag, or a
  tag outside the six, is counted as UNCLASSIFIED: its own row in
  Findings by File Type, shown at zero when clean, and named in the
  "Domain coverage gap" note with its reason. When there is no gap the
  note says how many files it checked. The whole-tree total prints with
  its split on the console, in the Priority Summary and in the Gate
  Path section, all from one count, tier1_by_domain(). If the domains
  ever failed to sum to the total, the line would say so in capitals
  rather than print a split that does not add up. In passing: a stray
  closing line of the August Task 2a stamp, which had drifted below the
  L-414 stamp, is put back under Task 2a.
- `provenance_history.py`. Each run record gains `tier1_by_domain`
  beside `domain_counts`. compare() names each domain whose Tier-1
  count moved; the console prints the split and the move after the
  Tier-1 delta; the Run History table gains a "T1 by domain" column.
  A record from before L-437 reads "--" and is called not comparable,
  never zero.
- `orrery_maintenance_run.py`. The Provenance scanner row's hint is now
  two lines, the GATE PATH verdict first and the whole-tree line after
  it, joined by "; ". A hint may be a tuple, read by a new
  verdict_from(); a line it names that the output lacks prints as
  missing. New gating row "Domain Split".
- `test_domain_split.py`, new (described in section 4).
- `palomas_orrery_dashboard.py`. A "Domain Split" button under the
  orrery's checkers, before Drawings Export, named what the run prints.
- `skills/provenance-discipline/SKILL.md` 2.28 -> 2.29 (section 6), its
  v2.26 entry moved to `documentation/SKILL_HISTORIES.md`; in
  `references/field-notes.md` one example that named the hand list as
  current now names it as retired.
- `PROJECT_INSTRUCTIONS.md` v3.95; v3.92 moved to
  `documentation/PROJECT_INSTRUCTIONS_HISTORY.md` PART 1.
- `LEDGER_CONSOLIDATED.md`: the L-437 block at the end of section A, one
  stamp line above "Review and RICE update".
- `documentation/WHERE_WE_ARE.md`: the Signals line only. The page
  stays at 130 lines above the run-record marker.
- This handoff, new.

Report-only. No finding moves between tiers.

## 4. The checker, and the planted faults

`test_domain_split.py`, row and button "Domain Split", last line
"DOMAIN SPLIT:". It writes small made-up modules to a temporary folder,
each with one uncited figure the scanner scores Tier-1, scans them
there, and reads the result. Nothing in the project folder is written.

Six checks:
1. The tag is the domain: a file named `data_acquisition.py`, tagged
   stars, is filed as stars; MODULE_DOMAIN_MAP no longer exists.
2. A file with no tag and one tagged "astro" are counted as
   unclassified and named, each with its reason; neither is counted
   as orrery.
3. The console line, the audit's Priority Summary line, the run
   history's tier1_by_domain and the Tier 1 column of Findings by File
   Type give the same split, and it sums to the total.
4. One file retagged from orrery to stars between two scans: the total
   stays 4, the printed line changes, and the history prints "Tier-1
   MOVED by domain: orrery 2 -> 1, stars 1 -> 2".
5. The maintenance run's scanner row quotes the GATE PATH line first
   and the whole-tree line after it, and says when the second is
   missing; the Domain Split row is named what it prints.
6. The run record keeps domain_counts (all tiers) and tier1_by_domain
   (Tier 1) as two fields; a record without the split is not
   comparable.

Six faults, each planted in memory by swapping one function, and each
counted as caught only by a check that passes on the real code (the
checker's first draft counted a fault as caught by a check that failed
anyway; that is fixed):

    F1 the hand list back                  by check_tag_is_the_domain
    F2 untagged defaulted to orrery        by check_untagged_is_named_not_defaulted
    F3 the total without its split         by check_four_places_agree
    F4 history without tier1_by_domain     by check_four_places_agree
    F5 history blind to domains            by check_a_move_at_equal_total_shows
    F6 the row quotes the gate only        by check_maintenance_row_quotes_both

The brief's planted cases map onto these: data_acquisition.py filed by
its tag (check 1, F1; and the real file, section 5); a file with no
tag named in the gap (check 2, F2; and the real L-436 patch, section
5); the four places agreeing with the table (check 3, F3, F4); a move
at an unchanged total changing the line (check 4, F5).

## 5. The pre-test

Run on throwaway copies of 70202e3b with the patch applied; the
deliverable is never edited by the pre-test. Results in section 9.

## 6. The skill, and L-425

provenance-discipline goes to 2.29, one version, with protocol v3.95
in the same patch; the maintenance run rewrites the Skill Manifest.
Report Domain Classification is rewritten: the tag is the store, the
hand list is gone, the gap note names untagged files. Scanner
Mechanics gains one bullet: the total prints with its split
everywhere, and tier1_by_domain is Tier-1 while domain_counts is all
tiers.

The brief asked which happened with L-425. At 70202e3b
provenance-discipline reads 2.28 and no L-425 patch is in the repo, so
this build bumps it. If the L-425 session also bumps
provenance-discipline before this patch runs, the second patch to run
refuses on the version line; that session re-anchors on the new HEAD
and makes its version 2.30. Nothing is hand-edited.

## 7. Notes for the parallel sessions

- `patch_L436_1_idea_20261013.py` will refuse at 70202e3b on its ledger
  header anchor: it expects the stamp built on c9722520 to be the last
  one before "Review and RICE update", and two stamps have been added
  since. Its other four anchors match. That patch is its own session's
  to redeliver; this patch does not depend on it, and the two touch
  different lines of the page.
- The maintenance run's GATING AND REPORT-ONLY paragraph still says
  twenty-five gating checkers. This patch makes it twenty-six, the
  dashboard-labels patch adds a parity row and L-425 adds rows. This
  patch does not edit that sentence, so no patch refuses on it; the
  one that runs last restates the count.
- Row and button share one name, "Domain Split", in title case, as the
  dashboard rule asks. The dashboard button is inserted by finding the
  `test_drawings_export.py` entry, not by its label, so the labels
  build can rename that button first without this patch refusing.

## 8. Recorded, not edited here

- L-183 says "the remaining unmapped-root-modules question still rides
  with this item." L-437 answers it: no module is mapped by hand any
  more.
- L-163's deferred Domain half, retiring MODULE_DOMAIN_MAP, is done.
- `add_docstrings.py` line 823 names MODULE_DOMAIN_MAP in a comment
  about where its suggestions came from. It is history, and not
  edited.
- Older documents in `documentation/` name MODULE_DOMAIN_MAP as
  current. They are dated records.

## 9. The pre-test, as run

All on throwaway clones of 70202e3b, in the sandbox, Python 3.12 under
a virtual display.
- The patch applied: 69 edits in 11 files and 2 new files. The tree it
  produced is byte for byte the build copy this session worked in.
- The maintenance run on that copy: 26 of 26 gating checkers passed.
  Domain Split: "PASS -- 6 of 6 planted faults caught". Scanner row
  run: 16 of 16 pins hold. The Provenance scanner row read "0 TIER-1
  -- the push gate holds; Whole tree, Tier-1: 281: orrery 116, Earth
  System 149, stars 13, utilities 2, unclassified 1." It rewrote the
  Skill Manifest to provenance-discipline 2.29 and the skill's read
  plan.
- A second scanner run printed "Tier-1 by domain: orrery 116, Earth
  System 149, stars 13, utilities 2, unclassified 1" and "no domain's
  Tier-1 count moved"; the first run after the patch says the previous
  record predates L-437, as it should.
- The real audit, against the committed one at 70202e3b:
  `data_acquisition.py` reads stars (orrery before);
  `patch_L436_1_idea_20261013.py` reads unclassified and is the one
  file in the coverage-gap note; `orrery_maintenance_run.py` reads
  dev_tools. Stars: 12 files and 13 Tier-1 (11 and 12 before).
- This patch, while it sits in the root, adds no finding of its own.
  The atlas lists it under "Patch scripts awaiting archive", as its
  `Role: patch` tag says.
- Run a second time, the patch refuses and writes nothing ("this patch
  looks as though it has already run"). On a copy where another
  session had renamed the Drawings Export button, renamed a maintenance
  row, added a ledger stamp and marked the Signals heading, with three
  files turned CRLF, it applied, reported the three, and wrote them LF.
- The dashboard on a copy under a virtual display: "Dashboard ready",
  no traceback, closed by the 25-second timeout.
- ASCII and LF: 0 non-ASCII bytes and 0 CRLF in all 14 files.
- Not a finding: the sandbox's first baseline run at HEAD failed Reset
  completeness and Orbit markers because matplotlib was not installed
  there. With it installed, both pass.

## 10. Tony's actions, all of them

- (do) Run `patch_L437_1_tier1_by_domain_20261013.py` from the orrery's
  root folder (VS Code, Run).
- (do) Run `orrery_maintenance_run.py`. Read the Provenance scanner
  row: the gate line, then "Whole tree, Tier-1: 281: orrery 116, Earth
  System 149, stars 13, utilities 2, unclassified 1." (280 and no
  unclassified once patch_L436_1 is filed in `documentation/`; this
  patch adds no Tier-1 of its own while it sits in the root). Read
  Domain Split: 6 of 6 faults caught.
- (do) Reinstall provenance-discipline 2.29 (Settings > Skills); copy
  PROJECT_INSTRUCTIONS.md (v3.95) to the Project's instructions and to
  `documentation/project_instructions_v3_95.md`.
- (do) Move this patch into `documentation/`; commit and push.
- The next session confirms its loaded provenance-discipline reads
  2.29 before provenance work.
- (decide) Nothing.

Session record written October 2026 with Anthropic's Claude Opus 5.5.
