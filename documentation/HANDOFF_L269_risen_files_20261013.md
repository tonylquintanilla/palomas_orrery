<!-- Doc-Kind: hand | Session record: the maintenance run's summary names every file whose Tier-1 rose since the scanner's previous run (L-269), redelivered on top of L-437. -->
# The maintenance run names the files whose Tier-1 rose (L-269)

Built on orrery ab96681 ("L431 close") at
https://github.com/tonylquintanilla/palomas_orrery (main). The gallery
is not touched.
Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`;
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.
Written October 13, 2026 with Anthropic's Claude Opus 5.5.
Patch: `patch_L269_5_risen_files_20261013.py`.

## 1. Why, and why a second patch

Tony's run record of 2026-10-13: "i was expecting the module class
breakdown." The maintenance run's summary quoted only the scanner's
GATE PATH line, so two things printed only on the scanner's own screen:
the whole-tree Tier-1 by kind of code, and the files whose Tier-1 rose
since the scanner's previous run.

The first patch, `patch_L269_1_scanner_breakdown_20261013.py`, did both
and was built on 70202e3b. L-437 (the Tier-1 total split by domain) ran
first and put the split on the scanner's row, so the first patch
refuses and would repeat the split if re-anchored. The coordination
session ordered the redelivery: "drop the breakdown half, keep the half
that names each file whose count rose, one patch, planted faults shown
caught." It is also deleted, not filed: its name repeats
`documentation/patch_L269_1_ledger_blocks_and_protocol_v3_49.py`.

## 2. What changed

Under the scanner's verdict in the summary, read from the scanner's own
run-history lines:

    Provenance scanner          0 TIER-1 -- the push gate holds; Whole
                                tree, Tier-1: 280: orrery 116, ...
      No file's Tier-1 count rose since the previous run.

or, when a file rose,

      Tier-1 rose since the previous run in 1 file(s):
      - patch_L436_1_idea_20261013.py: 0 -> 1

If the scanner printed no run history, the line says NOT READ.

New checker `test_maintenance_report.py`, "Maintenance report (L-269)"
in the run and "Maintenance Report" on the dashboard. It runs the
runner's real main() on the scanner's output recorded at ab96681, in
three versions, after three planted faults are each caught by name:

    planted                                          caught as
    the summary no longer prints the rise lines      RISE LINE NOT PRINTED
    a risen file counted but not named               RISEN FILE NOT NAMED
    missing run-history lines passed over in         MISSING RISE NOT ANNOUNCED
      silence

GATING AND REPORT-ONLY in the runner's docstring no longer names a
count. It read twenty-five while the run had twenty-six; three sessions
added rows on 2026-10-13, and the headline already counts from the
table.

## 3. Tested

- The checker: 3 of 3 planted faults caught, then a clean pass.
- The maintenance run on a clean clone of ab96681 with the patch
  applied: every gating checker passed, and the rise line printed under
  the scanner's.
- The patch on a clean clone gives these files byte for byte; a second
  run refuses; on a copy with Windows line endings and a note added, it
  writes LF and keeps the note.

## 4. For Tony

- (do) Delete `patch_L269_1_scanner_breakdown_20261013.py` from the root
  folder; it is superseded.
- (do) Run `patch_L269_5_risen_files_20261013.py` (VS Code, Run), then
  `orrery_maintenance_run.py`.
- (do) Move it, and `patch_L431_9_close_20261013.py`, into
  `documentation/`; commit and push.

If the dashboard session's patch lands after this one, its parity check
may ask for a one-line description for the Maintenance Report button;
that session said it would.

No skill or protocol version changes.
