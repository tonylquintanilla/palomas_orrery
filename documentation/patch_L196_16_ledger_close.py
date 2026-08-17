"""patch_L196_16_ledger_close.py -- write the ledger record for the work
completed 2026-08-16 and 2026-08-17.

RUN COMMAND
-----------
Save this file into the palomas_orrery repo root (the same folder as
LEDGER_CONSOLIDATED.md), open it in VS Code, and click Run.

    python patch_L196_16_ledger_close.py

Then run ledger_index.py -- from the dashboard or VS Code -- to
regenerate the index tables and migrate the three DONE items into the
closed archive. This script writes DETAIL BLOCKS ONLY and never touches
the generated index zone.

WHAT IT DOES
------------
Three new detail blocks at the end of section A, and two Gap edits on
existing items.

  L-196  Citation continuations: mark, join, refuse. Blocker 1 of the
         August dispatch review, closed.
  L-197  Maintenance runner output: say what passed. Four rows were
         reporting side effects as verdicts.
  L-198  Claim vocabulary: the units the scanner could not see. Ten
         annotated sites produced zero worksheet rows.

  L-195  Gap narrowed. The continuation half is done under L-196; the
         six Shape A swaps remain.
  L-192  As-built appended for the 2026-08-16/17 sessions.

ON THE PATCH FILENAMES
----------------------
Every patch script from these two sessions is named patch_L196_N. That
was a running sequence, not a claim that all of it belongs to one
handle -- scripts 9 through 12 are runner output (L-197) and 14 is the
claim vocabulary (L-198). The names are left as they are, because they
are already archived and pushed under those names and renaming them
would break the only link between the scripts and the run order. This
paragraph is the map. (Recorded rather than corrected: an archive that
gets renamed is not an archive.)

PERMANENT vs DISPOSABLE
-----------------------
This script is disposable and one-shot. What it installs is permanent:
the three ledger blocks and the two Gap revisions.

SAFETY
------
All-or-nothing, fingerprinted (CRLF-normalized), each anchor matched
exactly once. Any mismatch aborts with nothing written. The file's own
line endings are preserved.

Success: one 'ok' line, then 'patch applied (N bytes)'.
Failure: a single 'ERROR:' or 'ANCHOR FAIL' line; nothing is written.
"""

import hashlib
import os
import sys


ANCHOR = """**Ref:** L-192 (Break 5, the rule this makes true); L-186 (annotation
grammar); `documentation/FABLE_REVIEW_worksheet_schema.md` item 5.

## PENDING ACTION (Tony-side)
"""

NEW_BLOCKS = """**Ref:** L-192 (Break 5, the rule this makes true); L-186 (annotation
grammar); `documentation/FABLE_REVIEW_worksheet_schema.md` item 5.

#### [L-196] Citation continuations: mark, join, refuse
<!-- L:196 status:DONE upd:2026-08-17 section:A flag: rice:3/4/90/2 -->
- **The defect.** A `# Source:` citation too long for one line
  continued on a second, indented line. The request builder matched
  labeled lines only, so that second line was invisible: the worksheet
  quoted half a citation and asked a person to verdict it. Found by
  Fable 5 and GPT 5.6 Sol reviewing the dispatch packet blind, both
  independently saying do not send -- blocker 1 of nine.
- **The shape, per Tony's ruling 2026-08-16.** Neither reviewer's
  proposal. An explicit continuation marker naming the leg it
  continues, then a builder that joins on it, then a builder that
  refuses on any unmarked continuation. Leg-specific (`# Source+:`) so
  that a `Ref+` sitting under a `Source:` is a mismatch a tool can
  name; a generic marker would have nothing to compare against.
- **Marked in two stages**, per the ruling that all sites be covered
  rather than only the in-scope ones: a loud failure only works as a
  ratchet if nothing pre-existing trips it. Stage 1 marked 96 lines in
  the 7 corpus files (`patch_L196_1`); the chromosphere retirement
  marked 6 more; stage 2 marked 152 lines across 18 files
  (`patch_L196_13`). 135 citation-leg continuations repo-wide.
- **Scope correction.** The 2026-08-16 handoff records stage 2 as 235
  lines / 117 runs / 23 files. That figure does not reproduce. The
  detector used was validated by returning stage 1's answer set exactly
  -- 48 runs, 96 lines, the same line numbers -- and gives 154 lines /
  87 runs / 19 files. Counting tails under non-citation labels as well
  gives 217 / 111 / 27, which is not the recorded figure either. The
  likeliest reading is that 235/117/23 predates the ruling scoping the
  work to citation legs only. Repo total is therefore **135, not 165**.
- **One run deliberately unmarked.** `test_citation_inheritance.py`
  lines 122-123, inside the `MULTILINE_CITATION` fixture. That fixture
  proves the scanner captures a whole multi-line run and asserts on
  text from its first and third lines specifically to catch truncation
  at the top and in the middle. Marking it would convert the repo's
  only test of the unmarked padded shape into a test of the marked
  shape, removing that coverage. It is a fixture and will never carry
  cross-check annotations.
- **The join** (`patch_L196_8`). `legs_of()` joins a marked
  continuation onto the leg above it, reports a mismatched or orphaned
  marker rather than joining it to the wrong authority, and counts the
  lines that joined so a run that joins nothing says so. 153
  continuation lines now reach the worksheet that previously reached
  nobody.
- **The refusal** (`patch_L196_15`). An unmarked continuation is
  returned and `main()` refuses to write, listing every offending site
  and line. Scoped to the CLAIM CORPUS, not the tree: a file enters the
  corpus the moment it gains a `# Cross-checked:` line, and the refusal
  fires at the next build, still before any worksheet is made from it.
  Whole-tree scanning would buy only earlier notice, at the cost of a
  permanent exemption list headed by the fixture above.
  **Tony's ruling, 2026-08-17.**
- **A mismatched marker still reports rather than refusing.** The
  distinction is visibility: a mismatch already prints a line into the
  worksheet, where the person filling it in reads it. An unmarked
  continuation appears nowhere. Silent gets the refusal; visible gets
  the annotation.
**Note:** RICE is Claude's proposal, unratified.
**Note:** a rule that could not fail was caught here and is worth the
line. The detector has two parts -- padded lines are continuation,
unpadded labelled lines are labels. Deleting the padding rule left all
41 tests passing, because the label pattern happened to allow only one
space after the `#` and was already rejecting padded lines by itself.
The label pattern was loosened so the padding rule decides the case it
is documented as deciding, and the mutation now goes red. Found by a
mutation that was expected to break something and did not.
**Ref:** L-195 (the citation-leg errand this is half of); L-192 (the
checker and dispatch loop); `documentation/patch_L196_1..3`, `_8`,
`_13`, `_15`; `test_worksheet_request_builder.py` (new, 41 checks);
`documentation/HANDOFF_20260816_review_and_chromosphere.md` and its
addendum.

#### [L-197] Maintenance runner output: say what passed
<!-- L:197 status:DONE upd:2026-08-17 section:A flag: rice:2/3/90/1 -->
- **The defect.** Four of thirteen checker rows told the reader
  nothing. `Provenance 1d/1e ... All Phase 1d/1e tests passed` named a
  ledger sub-step twice. `Orbit cache ... Test files saved in: C:\\...`
  and `Reset completeness ... Cleanup complete.` reported side effects
  as verdicts. Five more rows ended in `...` because the note was
  truncated at 44 characters. Raised by Tony, 2026-08-17.
- **Three different causes**, worth separating because the fix differed
  each time.
  1. `test_orbit_cache.py` ended in `unittest.main()`, which writes OK
     or FAILED to STDERR. The runner reads stdout, so the last stdout
     line was a `tearDown` print firing once per test. It went green
     whether or not anything passed, because a path prints either way
     (`patch_L196_11`).
  2. `test_reset_completeness.py` printed a correct verdict and then
     got buried: importing `palomas_orrery` registers a
     `PlotlyShutdownHandler` atexit cleanup whose two lines arrive
     after `sys.exit(0)`. Fixed by giving the row a hint substring, the
     mechanism already in the runner for the scanner, which is
     position-independent (`patch_L196_12`).
  3. Truncation. Verdicts now wrap onto indented continuation lines
     instead of ending in an ellipsis. Wrapping rather than widening,
     because the longest verdict runs past 160 characters and a wider
     column hands the wrap point to whatever width the console happens
     to be (`patch_L196_10`).
- **Also landed:** hover text on all 41 dashboard Launch buttons naming
  the repo and file each one runs -- `Orrery: palomas_orrery.py`,
  `Gallery: tools/gallery_studio.py`, and args included, which is the
  only thing distinguishing the two `earth_system_controller.py` cards
  (`patch_L196_9`). The `Test Provenance 1d/1e` card became `Test
  Scanner Recognition` with a description saying what passing means.
**Note:** the general defect is NOT fixed. Eleven of thirteen rows
still resolve their verdict by last line, so any of them can be
displaced the same way the moment something prints later. Giving every
row a hint is the general cure and was not attempted.
**Note:** RICE is Claude's proposal, unratified.
**Ref:** L-188 (the runner); `documentation/patch_L196_9..12`.

#### [L-198] Claim vocabulary: the units the scanner could not see
<!-- L:198 status:DONE upd:2026-08-17 section:A flag: rice:3/4/85/1 -->
- **The defect.** Ten annotated sites were in the claim corpus and
  produced ZERO worksheet rows. The checker routed them; the builder
  never asked about them. Found while testing whether the pending
  dispatch already covered the SEND BACK backlog.
- **The cause, and it was not what was first guessed.** A first reading
  attributed it to ranges, from one site, without checking. Wrong. The
  scanner matches a number immediately followed by a unit from a fixed
  list. That list held `AU`, `km`, `solar radii` and `Earth radii` but
  not per-body radii (`Mars radii`, `lunar radii`), not the spelled-out
  `kilometers`, and it could not see across an intervening word, so
  `1.08 million km` failed where `1.08 km` passed. At all ten sites the
  only match was the display instruction, correctly dropped.
- **A second defect in the same pattern.** It ended `%)\\b`. A word
  boundary after a percent sign requires a word character next to it,
  so `96% of the sunlight` matched nothing while `96%x` matched. Every
  percentage followed by a space or a period was invisible.
- **Measured before the change, whole tree:** 728 matches gained, 16
  lost, and every one of the 16 a false positive -- percent-encoded
  URLs (`sstr=2024%20PT5` read as the claim `2024%`) and Python `%s`
  placeholders. No real claim lost. Precision and coverage both
  improved.
- **Consequences.** Scanner Tier-1 **206 -> 289**, risen in 23 files.
  Not a regression: those 83 findings are unsourced numeric claims that
  were not being counted because the scanner could not see the number.
  The push gate reads Tier-1 on the ACTIVE BUILD PATH, not the tree
  total. Checker 59 of 102 routed / 3 clean -> 68 of 110 / 8 clean.
  Dispatch **64 rows over 42 sites -> 100 rows over 52 sites**.
- **Why now.** `EXTRACTOR_VERSION` went 1 -> 2 because the `::cN`
  ordinal counts claims AFTER this filter, so a string that gains a
  claim ahead of an existing one re-points it -- Mars's bow shock, where
  `15` was claim 1 and is now claim 2. No worksheet has ever been
  issued, none of the 35 on disk carries a key, and not one pinned key
  carries an ordinal, so re-pointing cost nothing today and would have
  cost a reissue after the first dispatch. **Tony's ruling,
  2026-08-17**, taken after the risk was measured rather than asserted.
- **Six of the ten sites now get asked about**: Mars magnetosphere
  (2 and 1.6 Mars radii), Mars Hill sphere (319.2 Mars radii, 1.08
  million km), Mercury sodium tail (1,400 Mercury radii, 3.4 million
  km), Moon Hill sphere (60,000 kilometers, 34.53 lunar radii), Venus
  Hill sphere (1 million kilometers), Eris crust (96% albedo -- reached
  by the percent fix, not the unit fix). The other four carry no number
  but the display instruction and are correctly absent.
**Note:** RICE is Claude's proposal, unratified.
**Note:** the first false-positive sweep reported zero differences
because it loaded the old scanner from the wrong path and compared the
pattern against itself -- a clean result that could not have been
anything else. Caught because zero contradicted a count taken a minute
earlier; the rerun asserts the two patterns differ before comparing.
**Ref:** L-156 (the scanner recognition work this widens); L-192 (the
dispatch corpus it grows); `documentation/patch_L196_14`;
`documentation/worksheets/L192_extractor_pins.txt` (regenerated).

## PENDING ACTION (Tony-side)
"""

OLD_195_GAP = """**Gap:** enumerate the 20 blocks, identify the ones whose authority is
not in Source, move it, and re-run the checker. Do this before the
first dispatch that relies on the Break 5 rule.
"""

NEW_195_GAP = """**Gap:** the six Shape A swaps in `constants_new.py` (roughly lines
195-277), where a `# Source:` line names an event rather than an
authority. Shape A was ruled 2026-08-16; the swaps are not built. Do
this before the first dispatch that relies on the Break 5 rule.
**Note, 2026-08-17:** the continuation half of this errand is DONE
under L-196 -- the scan that made 20 a floor broke blocks on unlabeled
continuation comments, and every citation-leg continuation in the repo
is now marked, joined and ratcheted. What remains here is the authority
placement itself.
"""

EDITS = [
    (ANCHOR, NEW_BLOCKS),
    (OLD_195_GAP, NEW_195_GAP),
]

TARGET = 'LEDGER_CONSOLIDATED.md'
FP = '678f862cff5fa147df718dc86f7b5784'


def normalized(data):
    return data.replace(b'\r\n', b'\n')


def non_ascii_count(text):
    return sum(1 for ch in text if ord(ch) > 127)


def main():
    if not os.path.isfile(TARGET):
        print('ERROR: run this from the palomas_orrery repo root '
              '(the folder holding %s).' % TARGET)
        return 1

    with open(TARGET, 'rb') as handle:
        raw = handle.read()

    fp = hashlib.md5(normalized(raw)).hexdigest()
    if fp != FP:
        print('ERROR: %s does not match the base this patch was built '
              'against.' % TARGET)
        print('       expected %s' % FP)
        print('       found    %s' % fp)
        print('       Nothing written. If this patch has already run, '
              'that is the expected abort -- it is one-shot.')
        return 1

    crlf = b'\r\n' in raw
    text = normalized(raw).decode('utf-8')

    for old, new in EDITS:
        count = text.count(old)
        if count != 1:
            print('ANCHOR FAIL: expected 1 match, found %d.' % count)
            print('       anchor starts: %r' % old[:70])
            print('       Nothing written.')
            return 1
        if non_ascii_count(new):
            print('ERROR: an inserted block carries non-ASCII. Nothing '
                  'written.')
            return 1
        text = text.replace(old, new)

    # The index zone is generated by ledger_index.py. This patch writes
    # detail blocks only, so the zone must come out byte-identical.
    start_mark = ('<!-- INDEX:START (generated by ledger_index.py -- '
                  'do not edit this zone by hand) -->')
    end_mark = '<!-- INDEX:END -->'
    before = normalized(raw).decode('utf-8')
    for src in (text, before):
        if start_mark not in src or end_mark not in src:
            print('ERROR: index markers not found. Nothing written.')
            return 1
    if (text[text.index(start_mark):text.index(end_mark)]
            != before[before.index(start_mark):before.index(end_mark)]):
        print('ERROR: the generated index zone changed. Nothing written.')
        return 1

    out = text.encode('utf-8')
    if crlf:
        out = out.replace(b'\n', b'\r\n')
    with open(TARGET, 'wb') as handle:
        handle.write(out)

    print('ok  %-38s 3 new blocks, 1 Gap revised' % TARGET)
    print('patch applied (%d bytes)' % len(out))
    print('')
    print('Next: run ledger_index.py to regenerate the index and migrate '
          'L-196, L-197 and L-198 into the closed archive.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
