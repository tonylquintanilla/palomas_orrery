"""Ledger capture for the 2026-08-12 session.

RUN COMMAND
-----------
Save this file into the palomas_orrery repo ROOT, open it in VS Code, and
click Run.

    python patch_ledger_20260812.py

Then run ledger_index.py (or maintenance_run.py, which calls it) so the
INDEX zone and the section-C migration catch up.

WHAT IT DOES
------------
Three ledger edits, one transaction.

1. L-188 CLOSED. The maintenance runner shipped, and so did the dashboard
   wiring. Its open (decide) is resolved and one of its written
   constraints is corrected: it said the runner "must REPLACE the
   individual entries, not join them," and Tony ruled on 2026-08-12 to
   INDENT them under the runner instead. That satisfies what the
   constraint protected -- a ninth peer entry reproduces the
   eight-judgement-calls problem, but an indented child is not a peer --
   while keeping every tool launchable and, his reason, visible, so what
   the automation covers stays known.

2. L-186 EXTENDED. Its annotation half closed earlier today. This records
   the second half: the 55 pinned literals retired, replaced by
   constants_change_report.py, and the worksheet evidence chain moved to
   documentation/worksheets/.

3. L-192 OPENED for the worksheet checker, with the escalation conditions
   that decide when it runs.

WHY L-192 IS ITS OWN HANDLE
---------------------------
It is the only check that reaches COMMITTED history. The change reporter
compares the working tree against the last commit, so a value corrupted
and committed weeks ago is not a pending change and it has nothing to
notice. The worksheet checker reads a value against the evidence its own
annotation names, which does not depend on when the value moved.

SAFETY
------
Transactional: all three anchors must match exactly once or nothing is
written. LF-normalized fingerprint, binary-mode I/O, CRLF preserved.

WHAT SUCCESS LOOKS LIKE
-----------------------
Three `ok` lines, then `patch applied`. Any `ANCHOR FAIL` means nothing
was written.
"""

import hashlib
import os
import sys

LEDGER = 'LEDGER_CONSOLIDATED.md'
BASE_MD5 = 'abdcdccbcc543a25c1e2035a69ee1a9a'

EDITS = []

# ---- 1. L-188: close, and correct the replace-vs-indent constraint ----
EDITS.append(('L-188: closed, indent ruling recorded',
b"""#### [L-188] Maintenance runner -- one command, the whole suite
<!-- L:188 status:OPEN upd:2026-08-07 section:A flag: rice:3/3/70/2 -->""",
b"""#### [L-188] Maintenance runner -- one command, the whole suite
<!-- L:188 status:DONE upd:2026-08-12 section:C flag: rice:3/3/70/2 -->
- **CLOSED 2026-08-12.** `maintenance_run.py` shipped at `cfff5b5`, and
  the dashboard wiring with it. Four generators, then eight checkers,
  then one summary; about 30 seconds on Tony's machine. It reports and
  continues rather than stopping at the first failure (Tony's ruling:
  he pastes the output back, so the whole picture in one pass is worth
  more than an early exit), and it REGENERATES by default rather than
  offering a check-only mode -- "a regenerate step may be missed."
  Generated files are fingerprinted before and after, so the summary
  names the ones that actually moved.
- **The staleness check now has its caller.** `is_overdue()` and
  `overdue_lines()` are read FIRST, before anything else runs. That
  ordering is load-bearing: the runner runs the scanner, so asking
  afterwards whether the scanner is overdue would always read fresh and
  the check could never fire.
- **The (decide) dissolved rather than resolving.** It asked: dashboard
  entry, or script run before every push? Both. The script is the
  artifact; the dashboard entry launches it.
- **CORRECTION to the constraint below.** This item says the runner
  "must REPLACE the individual entries, not join them." Tony ruled
  2026-08-12 to INDENT them beneath it instead. That satisfies what the
  constraint was protecting -- the fear was a ninth PEER entry, one more
  equal choice among nine, and an indented child is not a peer, so the
  one-action default survives. His reason for keeping them: staying
  visible is how the automation's contents remain known instead of
  disappearing behind one button. Developer Tools now reads MAINTENANCE
  RUN with eleven tools indented under it, in execution order, scanner
  last so its verdict reads last. The five tools the runner does not
  cover stay unindented as peers.
- **Found by running it, first pass:** the test suite had been red since
  roughly August 3 (`test_cross_checked.py` asserting an unannotated
  corpus that stopped being unannotated in early August) and
  `test_constants_provenance.py` was failing 6 of 73. Neither was
  detectable before, because neither file was in any routine. That is
  the item's own premise confirming itself on first use.
- **Known gap, not urgent:** the runner prints a checker's full output
  only on failure, so the scanner's run-to-run delta -- the lines that
  say WHY a Tier-1 count moved -- never reaches the screen on a clean
  run. That delta is worth seeing every time.""")) 

# ---- 2. L-186: record the second half ---------------------------------
EDITS.append(('L-186: pins retired, worksheets relocated',
b"""- **The store-binding test is the durable part.** `test_cross_checked.py`
  now reads `skills/provenance-discipline/SKILL.md` off disk and asserts
  every annotation example in it parses to the fields the skill says it
  carries. Cause (c) cannot recur silently.""",
b"""- **The store-binding test is the durable part.** It now lives in
  `skills_index.py` rather than the test suite: every annotation example
  in every SKILL.md must parse as `provenance_scanner.py` reads it.
  Placed there deliberately, because that tool runs at the moment a skill
  changes, which is the moment the drift gets introduced. Tony's fact,
  2026-08-12: "I don't independently run tests like that unless you ask
  during the build" -- so a check living in the suite is a check that
  does not run. Cause (c) cannot recur silently.
- **SECOND HALF, 2026-08-12: the 55 pinned literals are retired.**
  `test_constants_provenance.py` held its own copy of 55 measured values,
  which is the same two-store defect one layer over: every correction
  needed a synchronized hand-edit in two files, enforced by nothing. The
  August 2 batch corrected six constants and updated no pins, and the
  tests then failed correctly for ten days describing sourced values as
  "drifted." The pins also carried unaudited citations -- the scanner
  extracts claims only from narrative-role files and that one is
  `Role: devtool` -- and at least one was FALSE:
  `test_chromosphere_radii` attributed ~1.5 R_sun to Carroll & Ostlie
  Ch. 11, the same chapter the August check read as ~2000 km (~1.003
  R_sun). Wrong-but-cited in a file nothing audits.
- **18 tests remain and they are a different kind:** derivations,
  orderings, cross-consistency, completeness. None holds a copy of a
  measured value, so none goes stale when a value is corrected.
- **Replaced by `constants_change_report.py`**, which stores no numbers.
  Tony's framing: "What I don't think we should do is create a second
  dictionary. Can we create a diff that would alert us to drift or
  intentional revision?" It asks git what changed in `constants_new.py`
  since the last commit and reads both values out of the diff. A
  deliberate correction moves the number AND its comment block;
  corruption moves the number alone. It also covers constants that do
  not exist yet -- a value added next month is reported the first time it
  moves, with nobody writing a test. Wired into the runner as the first
  checker.
- **Both of its blind spots announce** (Tony: "such a gap should announce
  and we would track it down"). Two values changed in one block with one
  comment edit reports AMBIGUOUS and credits neither; a changed line
  carrying a digit that matches no shape it reads is listed as NOT
  CHECKED. Exit 0 means everything was read and everything documented.
- **The worksheet evidence chain moved to `documentation/worksheets/`**
  (34 files: prompts sent, worksheets returned, cited or not). Tony's
  reasoning: these stopped being archive the moment a tool started
  reading them. `data/` was considered and set aside -- it means what the
  application produces and consumes. The 134 annotations name bare
  filenames, never paths, so nothing in any source module changed. Nine
  worksheets are cited by no annotation; those are NOT orphans, they
  cover files the provenance sweep has not reached yet.""")) 

# ---- 3. L-192: the worksheet checker ----------------------------------
EDITS.append(('L-192: worksheet checker opened',
b"""#### [L-190] Scanner reach: anything rendered must be reachable""",
b"""#### [L-192] Worksheet checker -- verify a value against its own evidence
<!-- L:192 status:OPEN upd:2026-08-12 section:A flag: rice:3/3/70/3 -->
- **What it does:** for a constant carrying `# Cross-checked:` lines,
  open the `.md` each line names in `documentation/worksheets/` and
  confirm the worksheet exists and states the value. The skill already
  requires this of a human -- "before citing any worksheet, confirm it
  exists on disk and contains the finding" -- with no tool behind it.
- **Why it is a separate handle from `constants_change_report.py`.** The
  change reporter compares the working tree against the last commit, so
  it is a pre-commit reader: a value corrupted and committed three weeks
  ago is history, not a pending change, and there is nothing in the diff
  for it to notice. This one reads a value against the evidence its own
  annotation names, which does not depend on WHEN the value moved. It is
  the only planned check that reaches committed history.
- **Not routine, and not arbitrary either** (Tony, 2026-08-12). The cost
  is reading up to 34 markdown files, so it does not belong in
  `maintenance_run.py`. Four trigger conditions, each an observable
  state rather than a judgement call, to be written into
  `provenance-discipline`:
  1. `constants_change_report.py` flags a value -- moved alone,
     ambiguous, or unparsed. SCOPED to those names, so the expensive
     pass runs over two or three constants rather than all of them. The
     cheap check names the expensive one and bounds it.
  2. A cross-check batch lands. New `# Cross-checked:` lines were just
     written; verify each names a worksheet that exists and states the
     value. This replaces the amendment once planned for step 5 of the
     Batch Worksheet Workflow (update the pins), which is moot now the
     pins are retired.
  3. A worksheet is added, renamed, or removed in
     `documentation/worksheets/`. Annotations pointing at it may now
     dangle. Mechanically detectable from the same git diff.
  4. Before a gallery build -- the moment a value stops being local and
     becomes published.
- **An uncited worksheet is PENDING WORK, not a defect** (Tony,
  2026-08-12): the provenance sweep is incomplete, and the nine
  currently uncited worksheets cover files not yet annotated. The
  checker must not report them as orphans.
- **Ref:** L-186 (the annotation grammar and the pin retirement it
  replaces); L-188 (the runner it deliberately stays out of); L-156
  Phase 2 (the cross-check batches that produced the worksheets).

#### [L-190] Scanner reach: anything rendered must be reachable""")) 


def fingerprint(data):
    """MD5 over LF-normalized content -- line endings are not content."""
    return hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, LEDGER)
    if not os.path.exists(path):
        print('ERROR: %s not found. Run this from the repo root.' % LEDGER)
        sys.exit(1)

    with open(path, 'rb') as handle:
        data = handle.read()

    got = fingerprint(data)
    if got != BASE_MD5:
        print('ERROR: base moved for %s' % LEDGER)
        print('       expected %s' % BASE_MD5)
        print('       got      %s' % got)
        print('Nothing written.')
        sys.exit(1)

    is_crlf = data.count(b'\r\n') > 0
    if is_crlf:
        print('note: %s uses CRLF; anchors translated to match.' % LEDGER)

    for label, old, new in EDITS:
        if is_crlf:
            old = old.replace(b'\n', b'\r\n')
            new = new.replace(b'\n', b'\r\n')
        count = data.count(old)
        if count != 1:
            print('ANCHOR FAIL (%s): expected 1 match, found %d.'
                  % (label, count))
            print('Nothing written.')
            sys.exit(1)
        data = data.replace(old, new)
        print('  ok  %s' % label)

    with open(path, 'wb') as handle:
        handle.write(data)

    print()
    print('patch applied -- %s, %d bytes' % (LEDGER, len(data)))
    print()
    print('NEXT: run maintenance_run.py (it calls ledger_index.py, which')
    print('      rebuilds the INDEX and migrates L-188 to section C),')
    print('      then commit.')


if __name__ == '__main__':
    main()
