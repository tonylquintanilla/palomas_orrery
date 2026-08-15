"""Add L-193 to the ledger: qualified verdicts and the two-axis report.

One insertion, after the L-191 entry and before the PENDING ACTION
heading. Asserts exactly one match for its anchor before writing, and
reports 'already' if the handle is present.

Run it from the repo root with the Run button, then run
ledger_index.py to rebuild the index.

Written August 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

LEDGER = 'LEDGER_CONSOLIDATED.md'
SENTINEL = 'L:193'

ANCHOR = """the dead tooltip decision); L-190 (tooling reach); L-182 (the silent
drift class Earth sits in).

## PENDING ACTION (Tony-side)
"""

ENTRY = """the dead tooltip decision); L-190 (tooling reach); L-182 (the silent
drift class Earth sits in).

#### [L-193] Qualified verdicts -- the token is not the whole answer
<!-- L:193 status:OPEN upd:2026-08-15 section:A flag: rice:3/4/80/2 -->
- **Tony's framing, 2026-08-15, and it is the requirement the whole
  handle serves:** we need to know when values and citations are wrong
  or missing, and when they are not, RELIABLY. Two axes, three states
  each, and "cannot tell" is a legitimate state that must be said out
  loud rather than resolved by picking the likelier reading.
- **The defect.** `classify_verdict` reads the leading token of a
  verdict cell and splits the rest off at the dash. `is_compound` was
  written to flag a cell carrying a token PLUS prose, so the
  qualification would reach a reader instead of being trimmed -- and it
  had ZERO call sites in `worksheet_checker.py` from the day it was
  written. Defined, unit-tested in isolation, never wired in. A guard
  that cannot fire is the v3.39 class, one layer out: it is not that
  the check passed, it is that the check never ran.
- **Measured, 2026-08-15:** 61 of 355 verdict cells in the corpus are
  compound (17%). By class: 17 UNREADABLE, 15 CONFIRMED, 12 REFUTED,
  7 DERIVED, 6 INCOMPLETE, 4 ABSENT.
- **The 15 CONFIRMED are the dangerous ones.** `dispose_verdict`
  returns early on a clearing verdict with no finding recorded, so it
  is the ONE branch where a qualification vanishes -- every other class
  already quotes the whole cell into its finding. "YES -- to 2 decimal
  places" and a bare "YES" were the same row, and the first one is not
  clean. Zero live claims currently sit on a qualified YES, which is
  why the guard has a unit test rather than a corpus pin.
- **The 12 REFUTED are the loud ones, and they were reported wrong.**
  In this corpus `NO -- wrong authority` means the value is fine and
  the source is not, while `NO -- arithmetic error` means the source is
  fine and the value is not. Same token, same column, opposite
  meanings. The tool printed the first reading over both: a live
  finding read `reads <<NO -- arithmetic error>> -- wrong authority for
  a value that may still be right`, asserting the opposite of the
  truth directly beside the correct quote.
- **Done 2026-08-15, in the same patch as the L2b change:** compound
  clearing verdicts emit QUALIFIED_PASS and stop counting as clean;
  compound refusals under a citation column emit
  REFUSAL_UNCLASSIFIED and state that the fault cannot be assigned
  here. Seven live rows moved off CITATION_DEFECT. The qualification
  decides WHETHER the tool may classify; it is never read to decide
  WHAT the tool says, which would be a prose-parsed convention.
- **What stays open, and why the handle does not close.** The corpus
  still has one column doing two jobs. 46 annotations name worksheets
  whose only verdict column is `Citation correct?`, so the value
  question has no machine-readable answer anywhere in them. Reporting
  that honestly is done; giving it an answer is the re-cut, and it
  belongs with the dispatch errand.
**Gap:** the two-axis report -- value state and citation state named
separately for every claim, with UNKNOWN as a first-class value on
each. VALUE_VERDICT_ABSENT and REFUSAL_UNCLASSIFIED are the first two
pieces of it.
**Ref:** L-192 (the checker and the dispatch errand); L-184 (the
active-build-path push gate); protocol v3.39 "A Check That Cannot Fail
Is Not Passing"; `patch_L192_verdict_aware_L2b.py`.

## PENDING ACTION (Tony-side)
"""


def normalized(path):
    with open(path, 'rb') as handle:
        return handle.read().replace(b'\\r\\n', b'\\n')


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    os.chdir(root)

    if not os.path.exists(LEDGER):
        print('ABORT: %s not found. Run this from the repo root.' % LEDGER)
        return 1

    text = normalized(LEDGER).decode('utf-8')

    if SENTINEL in text:
        print('  already   %s carries L-193.' % LEDGER)
        print('Nothing to do.')
        return 0

    count = text.count(ANCHOR)
    if count != 1:
        print('ABORT: the anchor matched %d times, expected 1.' % count)
        print('Nothing was written. The ledger is not the one this')
        print('entry was written against.')
        return 1

    with open(LEDGER, 'wb') as handle:
        handle.write(text.replace(ANCHOR, ENTRY).encode('utf-8'))
    print('  added     L-193 to %s  -> %s'
          % (LEDGER, hashlib.md5(normalized(LEDGER)).hexdigest()))
    print()
    print('Done. Next: run ledger_index.py to rebuild the index.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
