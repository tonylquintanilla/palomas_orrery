<!-- Doc-Kind: hand | Brief for the L-414 build session: the provenance scanner's citation window (a late Source line missed, a neighbour's citation credited, declared rows scored uncited) and the gate-path figure printed by name; cuts provenance-discipline 2.28. Written October 9, 2026. -->
# Handoff: L-414 (the scanner's window), the build brief

Built on orrery aa46bb102a351984ba800cbfbd0d801853110b9f at
https://github.com/tonylquintanilla/palomas_orrery ("L418_5 testing
close", 2026-10-09 15:02 CDT). Gallery at 5ec4739b at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, not
touched. Written by the Fable 5.1 coordination session of October 9,
which read the repo at HEAD and wrote no patch.

- Type: BUILD, one patch: `provenance_scanner.py` and its tests,
  provenance-discipline 2.27 -> 2.28, the protocol's version entry,
  the ledger, Tony's page, a handoff.
- Why now: Tony confirmed on 2026-10-09 that this item moves ahead of
  the Oort cloud build (L-421, the typed facts). The planted-fault run
  of 2026-10-09 showed the push gate ("Tier-1 = 0 on the active build
  path") passing a row whose Source line had been removed. The Oort
  cloud build adds sourced rows and relies on that gate.
- Tony is away from his machine while this session builds. Build and
  test on throwaway copies; ask him nothing that needs his machine
  until the patch is ready. He runs it when he is back.
- Skills this session fires: provenance-discipline 2.27 (read by the
  plan at its top, every part; this session cuts 2.28),
  safe-file-editing 1.13, agentic-pre-test 1.3,
  ledger-and-session-records 1.18. In the first reply, read back the
  version line of each loaded copy. The protocol is
  PROJECT_INSTRUCTIONS.md v3.86 (twelve manifest rows).

## Read this first

- *The scanner's citation context is a fixed window: 30 lines back,
  15 lines ahead. Three measured faults come from that one choice.
  Fix the mechanism, not the three symptoms.*
- *Every fix is shown FAILING on a planted copy before it is trusted
  passing. The planted-fault run already wrote the test cases.*
- *Run the fixed scanner on a copy of the whole tree BEFORE writing
  the patch, and name what moves. Crediting a neighbour's citation
  less generously may surface rows the gate has been passing for
  weeks. That list is a finding for Tony, not a reason to soften the
  fix.*
- *One Session, One Bump: provenance-discipline goes to 2.28 and
  nothing else is bumped.*

## 1. The three faults, as measured

All three are on L-414 in the ledger, with the measurements. In one
place:

1. **A row's own late Source line is missed.** EARTH_MEAN_RADIUS_KM's
   `# Source:` sits 16 lines below the assignment, after a Figures
   block that grew; `get_context_block(..., lookback=30, lookahead=15)`
   stops at 15. Measured at cbde99dc: not in context at 15, in it at
   16. (October 4.)
2. **A neighbour's citation is credited.** With
   EARTH_THERMOPAUSE_ALTITUDE_KM's Source lines removed, the scanner
   still scored it "Cited, not independently cross-checked", because
   the stratopause row's Source and Ref lines a few lines above fell
   inside the 30-line look-back. Removing those too made both rows
   Tier-1 (296 to 298). (October 9, planted fault F1.)
3. **Declared rows are scored uncited.** EARTH_SOLAR_WIND_PRESSURE_NPA,
   `_BZ_NT` and `_SPEED_KM_S` carry `# Status: declared pending` and a
   `# Declared:` reason; the scanner does not count a declared status
   as provenance, and its name rules call them MEASURED. (October 4.)

Faults 1 and 2 are one fault seen from two sides: a window measured
in lines does not know where one row's comment block ends and the
next begins. In constants_new.py the rows sit close, so the window
reaches past a row's own block in both directions.

## 2. The method question, and whose it is

The ledger records this as method, provenance-discipline's to settle,
not Tony's (Method Belongs to the Skill). The session proposes, builds
and writes the rule into 2.28; it brings Tony a case only if the rule
cannot express it.

The shape to try first, because it answers all three with one idea: a
row's citation context is its ATTACHED COMMENT RUN, the comment lines
contiguous with the assignment above and below it, ending at the
first blank line or the next assignment, not a fixed number of lines
in either direction. Then:

- a Source line anywhere in the row's own run is the row's, however
  far below the assignment the Figures block pushed it (fault 1);
- a neighbour's run is never read, so a neighbour's citation cannot be
  credited (fault 2);
- a `# Status: declared ...` line with a `# Declared:` reason in the
  run is provenance of its own kind, reported as DECLARED by name, and
  never Tier-1 (fault 3). The three solar-wind rows then leave the
  count and appear in the audit under their own heading.

Where the fixed window and a section-header citation disagree (the
look-back exists "for section-header citations", the docstring says),
keep whichever the recognition pins require, and say in the handoff
which cases the pins cover. The 27 recognition pins (1d/1e) must still
hold; a pin that breaks is a design question, not a test to edit.

Display strings and data modules outside constants_new.py have their
own context rules (the extractor's LOOKBACK 30 / LOOKAHEAD 25 is a
different mechanism, pinned separately). Leave them alone unless the
fix cannot avoid them; if it cannot, say so before building.

## 3. Discovery before the patch

Before anything is written for delivery:

1. Clone HEAD to a throwaway directory. Run the scanner as it is and
   keep PROVENANCE_AUDIT.md and the count (296 at aa46bb1, whole tree;
   4 in constants_new.py).
2. Apply the fix on the copy. Run again. Produce, BY NAME:
   - rows that left Tier-1 (expected: the four on L-414, at least);
   - rows that entered Tier-1 (any row that was being credited by a
     neighbour), with their file and whether they are on the active
     build path (the objects export and constants_export.json say
     which rows are served);
   - rows now reported DECLARED.
3. If rows entered Tier-1 on the active build path, STOP and record
   them, one ledger row per class (The Braid), before building the
   patch. They need a real source or removal with the gap noted, and
   that is remediation in slices, not this session's. The gate must
   then be stated honestly: it fails on those rows until they are
   sourced. Do not add exceptions to pass them.
4. The planted tests, each shown failing before the fix and passing
   after it, on copies: EARTH_THERMOPAUSE_ALTITUDE_KM with its Source
   lines removed becomes Tier-1 (the F1 case); EARTH_MEAN_RADIUS_KM
   with its Source 16 lines down is cited; the three declared rows are
   DECLARED and not Tier-1; a row whose only citation is its
   neighbour's is Tier-1.

## 4. The gate-path figure, by name

Tony's page (Signals) says: "No tool yet prints the number on the
gate path alone; that is owed to L-414." The scanner prints "296
TIER-1 FINDINGS IN THE SCANNED TREE" and names nothing, which the
protocol's own text calls out (A Report Names Its Items). In the same
build:

- the scanner's summary prints the Tier-1 count ON THE ACTIVE BUILD
  PATH beside the whole-tree count, and names each gate-path row
  (file and name), so the maintenance run's last lines say whether
  the push gate holds and why;
- the run history (`data/provenance_history.json`) records the
  gate-path names, not only a count, so a run that clears one and
  gains one is visible (the count-delta failure, fourth move under A
  Check That Cannot Fail Is Not Passing).

If the "active build path" set is not already defined in one place
the scanner can read, say where it comes from (the exports are the
natural source) and record that choice in the skill.

## 5. provenance-discipline 2.28

- The rule: a row's citation context is its attached comment run; a
  declared status with a reason is provenance of its own kind; the
  gate-path figure is printed by name. Short, where the scanner
  mechanics section already lives. Field notes carry the two
  measurements (October 4 and October 9) as the founding cases.
- The L-252 paragraph (the checker's four outcomes) already rode 2.27
  and is in provenance-cross-check 1.0; nothing is owed from it here.
- The three-entry rule: the oldest version entry moves to
  documentation/SKILL_HISTORIES.md.
- skills_index.py's --check must pass with the read plan regenerated;
  "Skill headers" counts 12.
- The protocol gains v3.87 (one skill bump, one version), and the
  manifest row comes from skills_index.py, not by hand.
- L-351 (what each skill is owed): strike what landed.

## 6. The patch and the tests

- One patch, `patch_L414_1_scanner_window_20261009.py`, from the
  orrery repo root, following safe-file-editing: single-match anchors
  on the lines it edits, binary-mode, LF, ASCII. Tony's own notes in
  the ledger and on his page are not fingerprinted.
- agentic-pre-test on throwaway copies: py_compile; the maintenance
  run on the copy with every gating checker passing and the scanner's
  new summary lines shown; a second run of the patch refuses and
  writes nothing; a CRLF copy behaves the same.
- The patch prints Tony's steps: run from the repo root (VS Code,
  Run); run orrery_maintenance_run.py; move the script into
  documentation/; commit and push; reinstall provenance-discipline
  from its ZIP (Settings > Skills), the ZIP kept out of the repo.

## 7. At the close

- The ledger: L-414 gains the fix, the discovery lists by name, and
  its Gap closes or names the slice that is left; any rows that
  entered Tier-1 get their class row; L-351 struck; a header stamp.
- Tony's page, by section, every handle labelled, nothing below the
  marker: the box says what the scanner now catches and what the
  gate-path count reads; Signals carries the new figure by name;
  Settled gains the context rule in one line.
- The handoff: `documentation/HANDOFF_L414_scanner_window_20261009.md`,
  anchored on aa46bb1 and on HEAD at the close.
- The obligation that travels: the next session confirms its loaded
  provenance-discipline reads 2.28 before provenance work. A reinstall
  during a session may or may not be visible to it; say what this
  session's own listing showed, as a data point.

## 8. Not this session

- L-425 (citation location checks), levels 1 to 3 and the quote line:
  Tony has not ruled; nothing from it rides here.
- L-424 and L-426 (the worksheet checker): a different checker, its
  own session.
- Sourcing any row that the fixed scanner newly reports: recorded,
  not chased.

Brief written October 9, 2026, with Anthropic's Claude Fable 5.1.
