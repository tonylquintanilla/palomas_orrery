"""Bring the 2026-08-15 handoff up to date with the last push.

The handoff was written at `f8b4356` and one more push followed it. Four
edits to documentation/HANDOFF_20260815_checker_honesty.md:

1. The anchor gains `7ef3d67`.
2. The L-192 ledger correction is added to the What Landed table. It is
   real work, not a record of the handoff: the entry had been telling
   readers the checker deliberately stays out of the runner it has been
   running in since 2026-08-14.
3. Both (do) items are marked CLOSED rather than deleted. All five
   session documents are filed at `7ef3d67`, confirmed by clone.
4. A ninth open item is added -- the transition sequencing decide. It
   went into L-192 and was never in the handoff, which is the one gap
   between the two documents.

Each edit asserts exactly one match before anything is written, and all
four are planned before any is written. Line endings are read from the
file and preserved.

Run it from the repo root with the Run button.

Written August 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

DOC = os.path.join('documentation', 'HANDOFF_20260815_checker_honesty.md')

OLD_ANCHOR = """`bdb56d8a5b0503c9afa3ff0511add2854064586e`, then
`f8b4356abe53c423e9730b2c70086f3fa5f1fcd7`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).**
"""
NEW_ANCHOR = """`bdb56d8a5b0503c9afa3ff0511add2854064586e`, then
`f8b4356abe53c423e9730b2c70086f3fa5f1fcd7`, then
`7ef3d67c0d5439bef760b6fadb2a3ebe019360c6`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).**
"""

OLD_TABLE = """| `f8b4356` | Two corrections to claims written earlier the same day. |
"""
NEW_TABLE = """| `f8b4356` | Two corrections to claims written earlier the same day. |
| `7ef3d67` | L-192 brought back in line with the code, plus the schema and dispatch-shape rulings. All five of this session's documents filed in `documentation/`. |

**The L-192 edit was not bookkeeping.** The entry said the checker's
cost "does not belong in `maintenance_run.py`" and its Ref line called
L-188 "the runner it deliberately stays out of". It has been a row in
that runner since 2026-08-14, finishing in under seven seconds -- a
fifth of the reset check already in the table. The estimate behind the
original call was never measured. The reversal is recorded rather than
overwritten: the trigger conditions are the right list for a scoped
expensive pass, and they were written against a cost that turned out
not to exist.

That entry described the tool this session spent the day repairing, and
it had been misdescribing it for two days. Same class as the seven
below.
"""

OLD_DO = """1. Send `FABLE_PROMPT_worksheet_schema_review.md` -- already done this
   session; the reply is in
   `documentation/FABLE_REVIEW_worksheet_schema.md`. Listed only so the
   round trip is closed in writing.
2. File `L192_haumea_sourcing_sendback.md` into `documentation/` if it
   is not there yet. It carries the ruling and the exact question,
   including the instruction not to reopen the equatorial figure.
"""
NEW_DO = """1. CLOSED. `FABLE_PROMPT_worksheet_schema_review.md` was sent and the
   reply is filed at `documentation/FABLE_REVIEW_worksheet_schema.md`.
   Kept in the record so the round trip is closed in writing rather
   than by absence.
2. CLOSED. `L192_haumea_sourcing_sendback.md` is filed in
   `documentation/` at `7ef3d67`, confirmed by clone. It carries the
   ruling and the exact question, including the instruction not to
   reopen the equatorial figure.
"""

OLD_ITEM8 = """8. **The pluto 614/638 merge**, still open from yesterday. New
   evidence: both sites carry the identical claim signature (`0.04`,
   one instruction drop), and both are among the three live
   QUALIFIED_PASS rows.
"""
NEW_ITEM8 = """8. **The pluto 614/638 merge**, still open from yesterday. New
   evidence: both sites carry the identical claim signature (`0.04`,
   one instruction drop), and both are among the three live
   QUALIFIED_PASS rows.
9. **Transition sequencing.** The checker simplification the schema
   permits -- deleting `match_row()`, a strict fail-loud verdict
   grammar -- is gated on the re-cut, not the reverse: fuzzy matching
   cannot be removed while 104 annotations still depend on it. Either
   both formats stay readable through the transition, or the re-cut is
   atomic. This is in L-192 as of `7ef3d67`; it is listed here because
   a decide that lives in only one of the two documents is how an item
   goes missing.
"""

JOBS = [
    ('anchor', OLD_ANCHOR, NEW_ANCHOR),
    ('what landed', OLD_TABLE, NEW_TABLE),
    ('do items closed', OLD_DO, NEW_DO),
    ('sequencing decide', OLD_ITEM8, NEW_ITEM8),
]


def dominant_eol(raw):
    """The line ending this file already uses, as text."""
    return '\r\n' if raw.count(b'\r\n') else '\n'


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    os.chdir(root)

    if not os.path.exists(DOC):
        print('ABORT: %s not found. Run this from the repo root.' % DOC)
        return 1

    with open(DOC, 'rb') as handle:
        raw = handle.read()
    text = raw.decode('utf-8')
    eol = dominant_eol(raw)
    label = 'CRLF' if eol == '\r\n' else 'LF'

    planned = []
    for name, old, new in JOBS:
        want_old = old.replace('\n', eol)
        want_new = new.replace('\n', eol)
        if want_new in text:
            planned.append((name, 'already'))
            continue
        count = text.count(want_old)
        if count != 1:
            print('ABORT: %r matched %d times, expected 1.' % (name, count))
            print('Line endings read as %s.' % label)
            print('Nothing was written. No edit from this patch has been')
            print('applied, including the ones that matched.')
            return 1
        text = text.replace(want_old, want_new)
        planned.append((name, 'apply'))

    for name, action in planned:
        print('  %-9s %s' % (action, name))

    if all(action == 'already' for _n, action in planned):
        print('Nothing to do. All four edits are already in place.')
        return 0

    with open(DOC, 'wb') as handle:
        handle.write(text.encode('utf-8'))
    with open(DOC, 'rb') as handle:
        digest = hashlib.md5(handle.read()).hexdigest()
    print('  wrote     %s (%s endings preserved)  -> %s'
          % (DOC, label, digest))
    print()
    print('Done. Commit and push; nothing else needs to run.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
