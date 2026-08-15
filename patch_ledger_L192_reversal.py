"""Bring L-192 back in line with the code, and record two rulings.

Three edits, all in LEDGER_CONSOLIDATED.md.

1. The `upd:` date moves to 2026-08-15.

2. The entry says the checker's cost "does not belong in
   maintenance_run.py" and its Ref line calls L-188 "the runner it
   deliberately stays out of". The checker has been a row in that
   runner since 2026-08-14 and finishes in under seven seconds. This
   is the stale-erratum class: a document outliving its truth, sitting
   in the entry that describes the tool. The reversal is recorded
   rather than overwritten, because why the original call was made and
   what changed is the part worth reading once.

3. Two rulings from 2026-08-15 added: the four-field worksheet schema,
   and the per-(key, ordinal) dispatch shape. Without them the next
   session reads an entry whose dispatch is blocked by two rulings
   that have both been made.

Each edit asserts exactly one match before anything is written, and all
three are planned before any is written. Line endings are read from the
file and preserved, so the ledger's CRLF stays CRLF.

Run it from the repo root with the Run button, then run
ledger_index.py.

Written August 2026 with Anthropic's Claude Opus 5 (L-192).
"""

import hashlib
import os
import sys

LEDGER = 'LEDGER_CONSOLIDATED.md'

OLD_META = """<!-- L:192 status:OPEN upd:2026-08-13 section:A flag: rice:3/3/70/3 -->
"""
NEW_META = """<!-- L:192 status:OPEN upd:2026-08-15 section:A flag: rice:3/3/70/3 -->
"""

OLD_COST = """- **Not routine, and not arbitrary either** (Tony, 2026-08-12). The cost
  is reading up to 34 markdown files, so it does not belong in
  `maintenance_run.py`. Four trigger conditions, each an observable
  state rather than a judgement call, to be written into
  `provenance-discipline`:
"""
NEW_COST = """- **Not routine, and not arbitrary either** (Tony, 2026-08-12). The cost
  was estimated at reading up to 34 markdown files, so it did not belong
  in `maintenance_run.py`. Four trigger conditions, each an observable
  state rather than a judgement call, to be written into
  `provenance-discipline`:
"""

OLD_REF = """- **Ref:** L-186 (the annotation grammar and the pin retirement it
  replaces); L-188 (the runner it deliberately stays out of); L-156
  Phase 2 (the cross-check batches that produced the worksheets).
"""
NEW_REF = """- **REVERSED 2026-08-14: it is a row in the runner.** The estimate above
  was never measured. Measured, the pass reads 35 worksheets and 104
  annotations in under seven seconds, which is a fifth of the reset
  check already in the table. The trigger conditions are not wrong --
  they are the right list for a scoped, expensive pass -- they were
  written against a cost that turned out not to exist. Recorded rather
  than deleted: a check nobody runs cannot fail, and four conditions
  that must be noticed by a human are four chances not to notice.
  Putting it where the routine already runs is what made 2026-08-15's
  findings visible at all.
- **The schema is settled** (Tony, 2026-08-15). Four fields: code value
  at time of check; value RIGHT/WRONG/UNKNOWN plus the number, or a
  range with its reduction rule stated in the cell; citation
  RIGHT/WRONG/UNKNOWN, separately, because the two come apart in real
  rows; notes, the only place interpretation lives. Not a proposal --
  `worksheet_claude_constants_new_addendum.md` already carries this
  header and already parses. The re-cut is "make the others look like
  the addendum."
- **Dispatch shape: one pre-printed row per (key, ordinal)** (Tony,
  2026-08-15), with field 1 filled in by the builder so the responder
  fills only verdicts and notes. Measured on the corpus: 53 rows become
  65. It is what makes Roche's three provenance legs and Eris's four
  claims expressible at all, it deletes `match_row()` and the 25
  UNMATCHED findings that fuzzy binding produced, and a later ordinal
  shift stops matching its pre-printed value loudly instead of binding
  to the wrong claim silently.
- **Sequencing, not yet ruled.** The checker simplification the schema
  permits -- deleting `match_row()`, a strict fail-loud verdict grammar
  -- is gated on the re-cut, not the reverse: fuzzy matching cannot be
  removed while 104 annotations still depend on it. Either both formats
  stay readable through the transition or the re-cut is atomic.
  **Tony-action (decide).**
- **Ref:** L-186 (the annotation grammar and the pin retirement it
  replaces); L-188 (the runner it now runs in); L-193 (qualified
  verdicts, and the interpretation layer this schema is meant to
  delete); L-156 Phase 2 (the cross-check batches that produced the
  worksheets); `documentation/HANDOFF_20260815_checker_honesty.md` and
  `documentation/FABLE_REVIEW_worksheet_schema.md`.
"""

JOBS = [
    ('upd date', OLD_META, NEW_META),
    ('cost estimate', OLD_COST, NEW_COST),
    ('reversal, schema, dispatch shape', OLD_REF, NEW_REF),
]


def dominant_eol(raw):
    """The line ending this file already uses, as text."""
    return '\r\n' if raw.count(b'\r\n') else '\n'


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    os.chdir(root)

    if not os.path.exists(LEDGER):
        print('ABORT: %s not found. Run this from the repo root.' % LEDGER)
        return 1

    with open(LEDGER, 'rb') as handle:
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
        print('Nothing to do. All three edits are already in place.')
        return 0

    with open(LEDGER, 'wb') as handle:
        handle.write(text.encode('utf-8'))
    with open(LEDGER, 'rb') as handle:
        digest = hashlib.md5(handle.read()).hexdigest()
    print('  wrote     %s (%s endings preserved)  -> %s'
          % (LEDGER, label, digest))
    print()
    print('Done. Next: ledger_index.py, then maintenance_run.py.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
