"""Ledger patch -- Tony's report-not-reject rationale into L-214, the
legs_of docstring folded into L-214's Gap, and L-219 opened.

RUN COMMAND:  python patch_L214_2_rationale_and_L219.py

Save this file into the SAME FOLDER as LEDGER_CONSOLIDATED.md (the repo
root), open it in VS Code, and click Run.

Built on 5859e15097b92bbb5ebd9ebb7a8fe78fdea85aac at
https://github.com/tonylquintanilla/palomas_orrery (branch main).

WHAT IT DOES
  Edit 1 -- adds Tony's rationale for report-not-reject to L-214, using
            the Corrected drift as its worked example, and folds the
            one-word legs_of docstring fix into L-214's Gap.
  Edit 2 -- inserts L-219 (patch-script naming cannot express a
            cross-handle run order) at the end of section A.

WHY THE DOCSTRING IS NOT ITS OWN HANDLE
  It is one word inside legs_of, and the L-214 build rewrites that
  function. A separate item would be closed as a side effect of L-214
  and then need reconciling. Folded into the Gap it is captured and
  closes with the work that touches it. Claude's judgment, stated here
  so it can be overruled.

AFTER IT RUNS
  Run ledger_index.py the same way, to regenerate the index tables.

WHAT IS PERMANENT
  The script is disposable; the ledger blocks it writes are not.
  Archive this file to documentation/ once it has run.

SUCCESS   one 'ok' line per edit, then 'patch applied (N bytes)'.
FAILURE   a single 'ERROR:' or 'ANCHOR FAIL' line; nothing is written.
"""

import hashlib
import os
import sys

TARGET = 'LEDGER_CONSOLIDATED.md'
BASE_FP = '623e9b23fbf36012a1637b6643b269c9'   # content md5, CRLF-normalized

GAP_OLD = b"""**Gap:** the BUILD. Design is settled and nothing is built. In order:
generic label detection separated from policy; one home for the
vocabulary with the scanner and the checker importing rather than
compiling their own; `Note` admitted to context; `# Review-note:`
added as withheld free-form; the moon line rehomed; the four odd
labels fixed at source; the 12-line marker sweep. Re-dispatching the
affected rows afterwards is still a separate decision, because a
second dispatch of a row this project has already argued about in
writing is not an independent leg.
"""

GAP_NEW = b"""- **WHY REPORT RATHER THAN REJECT -- Tony's rationale, 2026-08-19,
  recorded because it is the argument and not just the ruling.** A
  reported label is one this project can then READ and decide about:
  alias it, or unify it under a single label the way `Note` was
  unified. A rejected label forecloses that -- the run stops and the
  decision never gets made. The reading step is where the judgment
  lives, and reporting is what delivers material to it.
- **The `Corrected` drift is the worked example** [verified
  @2f0aabe]. Corpus-wide the label appears in FOUR spellings with no
  validator behind any of them: `# Corrected:` (7), `# Corrected
  2026-08-02:` (5), `# Corrected 2026-08-05:` (1), `# Corrected in
  Phase B:` (1). Three of the four would classify as unknown under the
  new design, while a human reading them sees an obvious record leg.
  That is exactly the case reporting is for: the reader sees all four,
  and then decides between aliasing the dated forms and unifying them
  on one label. Rejecting would have stopped the run and produced no
  decision. Note also that this drift happened in the two record
  labels that have no compiled pattern -- the two nothing was
  watching.
**Gap:** the BUILD. Design is settled and nothing is built. In order:
generic label detection separated from policy; one home for the
vocabulary with the scanner and the checker importing rather than
compiling their own; `Note` admitted to context; `# Review-note:`
added as withheld free-form; the moon line rehomed; the four odd
labels fixed at source; the 12-line marker sweep. Deciding the form of
`Removed` and `Corrected` is part of the build, not a precondition of
it -- there is no agreed form to register yet. One word also changes
while the file is open: `legs_of`'s docstring says of malformed
continuation markers that "their text is reported and NOT joined,"
where the code appends only a message naming the label; the accurate
sentence is "their label is reported and their text is NOT joined."
Re-dispatching the affected rows afterwards is still a separate
decision, because a second dispatch of a row this project has already
argued about in writing is not an independent leg.
"""

SECTION_A_END_OLD = b"""announced); L-214.

## PENDING ACTION (Tony-side)
"""

SECTION_A_END_NEW = b"""announced); L-214.

#### [L-219] Patch-script naming cannot express a cross-handle run order
<!-- L:219 status:OPEN upd:2026-08-19 section:A flag: rice:2/2/85/1 -->
- **Recorded 2026-08-19, from the 2026-08-19 handoff's own error log,
  where it was named as a real gap and explicitly noted as not yet
  having an item.** Two patches were delivered with a cross-handle
  dependency -- `patch_L209_2` had to run AFTER `patch_L213_3` -- but
  the `safe-file-editing` sequence number is scoped to its own ledger
  handle, so alphabetical sort order contradicted run order. Only the
  prose carried the real sequence.
- **What saved it, and why that is not enough.** The base fingerprint
  guard caught the out-of-order run and wrote nothing, which is the
  guard working. But an abort tells you the order was wrong without
  telling you what the right order was, and the convention's own
  promise is that "sort order is then run order."
- **The convention as written cannot express this.** `patch_<handle>_
  <n>_<what>.py` numbers within one handle. Nothing in the filename
  ranks two handles against each other. Options not yet weighed: a
  session-scoped prefix ahead of the handle; a single script spanning
  both handles when the dependency is real; or accepting the limit and
  requiring the dependency in the docstring of the LATER script, where
  the person about to run it will see it.
**Note:** RICE is Claude's proposal, unratified.
**Gap:** pick one of the three and write it into `safe-file-editing`,
which would be 1.5.
**Tony-action (decide):** which option.
**Ref:** `skills/safe-file-editing/SKILL.md` "Naming and Archiving a
Patch Script"; `documentation/patch_L209_2_alfven_migration.py` and
`documentation/patch_L213_3_cache_line_and_close.py` (the pair that
exposed it); HANDOFF_20260819_alfven_and_the_swap.md, error 4.

## PENDING ACTION (Tony-side)
"""

EDITS = [
    ('L-214 rationale + docstring folded into Gap', GAP_OLD, GAP_NEW),
    ('L-219 inserted', SECTION_A_END_OLD, SECTION_A_END_NEW),
]


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, TARGET)
    if not os.path.exists(path):
        print('ERROR: %s not found next to this script.' % TARGET)
        return 1

    with open(path, 'rb') as handle:
        data = handle.read()

    fp = hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()
    if fp != BASE_FP:
        print('ERROR: BASE MOVED. expected %s, found %s' % (BASE_FP, fp))
        print('       Nothing written. Reconcile before re-running.')
        return 1
    print('base fingerprint %s' % fp)

    is_crlf = data.count(b'\r\n') > 0
    print('line endings: %s' % ('CRLF' if is_crlf else 'LF'))

    staged = data
    for name, old, new in EDITS:
        if is_crlf:
            old = old.replace(b'\n', b'\r\n')
            new = new.replace(b'\n', b'\r\n')
        count = staged.count(old)
        if count != 1:
            print('ANCHOR FAIL: %s -- expected 1 match, found %d'
                  % (name, count))
            print('             Nothing written.')
            return 1
        staged = staged.replace(old, new)
        print('ok  %s' % name)

    if staged.count(b'#### [L-219]') != 1:
        print('ANCHOR FAIL: L-219 header count is %d, expected 1'
              % staged.count(b'#### [L-219]'))
        return 1

    with open(path, 'wb') as handle:
        handle.write(staged)
    print('patch applied (%d bytes)' % len(staged))
    print('')
    print('NEXT: run ledger_index.py the same way to rebuild the index.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
