"""patch_L196_17_ledger_L199.py -- open L-199: how the protocol's own
length gets governed.

RUN COMMAND
-----------
Save this file into the palomas_orrery repo root (the same folder as
LEDGER_CONSOLIDATED.md), open it in VS Code, and click Run.

    python patch_L196_17_ledger_L199.py

Then run ledger_index.py to regenerate the index tables. This script
writes ONE detail block and never touches the generated index zone.

WHAT IT DOES
------------
Adds L-199 at the end of section A, status OPEN. The item is a proposal
with three parts, none of them built:

  1. A sizing section for the protocol itself, replacing the unstated
     850-line target with the test that actually decides what may
     leave: does this have a trigger somewhere else.
  2. A stated cap on how many version-history entries stay resident,
     and the ledger repair that has to happen first -- the appendix
     stops at v3.38 while the protocol carries v3.39 and v3.40, so the
     store relationship the protocol asserts is not currently true.
  3. One line in Part 5 naming LESSONS_ARCHIVE.md, which is invisible
     from the protocol today.

It also records the finding that the archive should NOT be reintegrated,
with the reading behind it, so the question does not have to be reopened
from memory.

PERMANENT vs DISPOSABLE
-----------------------
This script is disposable and one-shot. What it installs is permanent:
the L-199 block.

SAFETY
------
All-or-nothing, fingerprinted (CRLF-normalized), one anchor matched
exactly once, and the generated index zone must come out byte-identical.
Any mismatch aborts with nothing written.
"""

import hashlib
import os
import sys


ANCHOR = """**Ref:** L-192 (Break 5, the rule this makes true); L-186 (annotation
grammar); `documentation/FABLE_REVIEW_worksheet_schema.md` item 5.

## PENDING ACTION (Tony-side)
"""

NEW_BLOCK = """**Ref:** L-192 (Break 5, the rule this makes true); L-186 (annotation
grammar); `documentation/FABLE_REVIEW_worksheet_schema.md` item 5.

#### [L-199] Protocol length: govern the growth, not the number
<!-- L:199 status:OPEN upd:2026-08-17 section:A flag: rice:2/3/80/1 -->
- **The question, Tony 2026-08-17.** The protocol is 1021 lines against
  an earlier target of 850. It keeps growing and none of it is
  obviously disposable.
- **Measured @fb63e4b.** Preamble 38 (3.7%), Part 1 138 (13.5%), Part 2
  158 (15.5%), Part 3 gates and skills 296 (29.0%), Part 4 121 (11.8%),
  Part 5 268 (26.2%). Inside Part 5, **Version History alone is 129
  lines, 12.6% of the whole document**.
- **Length is not a reading problem.** 1021 lines is roughly 14,000
  tokens. The cost is SALIENCE, not capacity: the resident layer exists
  so the CRITICAL gates fire unprompted, and everything that is not a
  gate competes for that. This is the document-scale form of the rule
  Part 2 already states about the tiers -- if everything is critical,
  nothing is.
- **The test for what may leave is not "is it secondary".** It is
  **does this have a trigger somewhere else**. A skill fires on task
  match; the ledger is read at session start; a bare archive file has
  no trigger at all. That is why the v3.37 first cut, which moved all
  41 lessons out and left a pointer, was reversed the same day. The
  850 number came from Claude's own recommendation when context length
  genuinely constrained the work; it has outlived the condition that
  produced it and should be replaced by the test rather than re-tuned.
- **Applying the test, only one section passes.** Version History has a
  real trigger elsewhere -- the ledger appendix below is its store, and
  the protocol already says so. Quotables shapes voice, Part 4 shapes
  judgment, and the resident Lessons Archive is by construction the
  fourteen with no counterpart anywhere. Those have no trigger, but
  firing is not their job.
- **A store relationship that is currently false.** The protocol says
  the full version history lives in this ledger's appendix. The
  appendix carries v1.0 through **v3.38**; v3.39 and v3.40 exist ONLY
  in the protocol. Push those two down BEFORE trimming anything, or the
  trim deletes the only copy.
- **Also worth stating: 850 may be the wrong thing to measure.** It was
  set when the protocol was the only layer. Since v3.30 there are two,
  and the skills carry well over a thousand lines of procedure that
  used to live here. The number worth watching is what FRACTION of the
  resident document is gates, not its total.

**Proposal, three parts, none built.**
1. A short sizing section in the protocol -- roughly fifteen lines --
   carrying the trigger test, the gates-fraction measure, and a stated
   cap on resident version-history entries. It earns its lines by
   governing growth rather than adding to it; the document currently
   has no rule about itself, which is how it gained 200 lines with
   nothing objecting.
2. Copy v3.39 and v3.40 into the ledger appendix, then reduce
   v3.34-v3.39 in the protocol to a single pointer line, keeping the
   two most recent entries in full. Recovers roughly 95 lines, taking
   the protocol to about 925.
3. One line in Part 5 naming `documentation/LESSONS_ARCHIVE.md`. The
   file is invisible from the protocol today, which is the only real
   defect it has.

**Note: do NOT reintegrate the lessons archive.** Tony raised this on
the reasoning that nothing reads it. Checked by reading the file rather
than from memory: 27 entries, every one names where it still lives, and
all four homes that a first automated probe flagged as missing are in
fact present -- the probe was matching truncated strings. Reintegrating
would re-add 27 restatements of rules already stated where they fire,
grow the protocol by about 30 lines, and restore exactly the
duplication v3.37 removed. Nothing is stranded except the record of the
decision, and a record is supposed to sit still. The archive's own
header already sets the standard for reopening this: put a line back if
it turns out to be doing work its counterpart does not do, judged by
reading. None of the 27 met that bar on 2026-08-17.
**Note:** RICE is Claude's proposal, unratified.
**Tony-action (decide):** approve the sizing section's content before
it is written into the protocol -- it is a constitutional amendment,
not a build.
**Gap:** all three parts unbuilt. Part 2 must not run before the
appendix repair in the bullet above.
**Ref:** v3.37 (the reversed all-lessons cut, and why an archive has no
trigger); v3.30 (the two-layer split that moved procedure into skills);
`documentation/LESSONS_ARCHIVE.md`; the Protocol Version History
appendix at the end of this ledger.

## PENDING ACTION (Tony-side)
"""

TARGET = 'LEDGER_CONSOLIDATED.md'
FP = '732bdd2bd765a77bf457295b481b59da'
START_MARK = ('<!-- INDEX:START (generated by ledger_index.py -- '
              'do not edit this zone by hand) -->')
END_MARK = '<!-- INDEX:END -->'


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
    before = normalized(raw).decode('utf-8')

    count = before.count(ANCHOR)
    if count != 1:
        print('ANCHOR FAIL: expected 1 match, found %d.' % count)
        print('       Nothing written.')
        return 1
    if non_ascii_count(NEW_BLOCK):
        print('ERROR: the inserted block carries non-ASCII. Nothing '
              'written.')
        return 1

    text = before.replace(ANCHOR, NEW_BLOCK)

    for src in (text, before):
        if START_MARK not in src or END_MARK not in src:
            print('ERROR: index markers not found. Nothing written.')
            return 1
    if (text[text.index(START_MARK):text.index(END_MARK)]
            != before[before.index(START_MARK):before.index(END_MARK)]):
        print('ERROR: the generated index zone changed. Nothing written.')
        return 1

    out = text.encode('utf-8')
    if crlf:
        out = out.replace(b'\n', b'\r\n')
    with open(TARGET, 'wb') as handle:
        handle.write(out)

    print('ok  %-38s L-199 added (OPEN)' % TARGET)
    print('patch applied (%d bytes)' % len(out))
    print('')
    print('Next: run ledger_index.py to regenerate the index.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
