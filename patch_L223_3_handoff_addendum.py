"""L-223 patch 3 of 3 -- amend the filed handoff.

Built on 2dae4fe86d27d0c2740bbc89d571963a3ebe0dfd at
https://github.com/tonylquintanilla/palomas_orrery (branch main).

WHAT THIS DOES

Appends one section to documentation/HANDOFF_20260821_L214_built.md
and rewrites its Tony-action rollup. The handoff was written and filed
while the session was still running, so three things happened after it
was written and none of them are in it.

The one that matters is a CARRIED OBLIGATION. safe-file-editing went
1.6 to 1.7 mid-session. A mid-session skill bump cannot be verified
from inside the session that makes it -- the loaded copy appears bound
when the conversation starts, and this session's still reads 1.6. So
the next session confirms its loaded copy reads 1.7 before doing patch
work. If that sentence is not in the handoff it is not anywhere, and
the gate that would catch it has already fired and passed.

The other two: L-223 exists, and both of the handoff's (do) items are
discharged. A future session reading an un-amended rollup would redo
work that is already pushed.

WHY AMEND RATHER THAN WRITE A SECOND HANDOFF

One session, one record. Two handoffs for one session is how item
numbers get rebased and items leak at the rebase, which this project
has already paid for once.

WHY A PATCH RATHER THAN AN EDIT

Because of L-223 itself. A document edit is a patch, the same as a
code edit. This script is the rule using itself.

HOW TO RUN IT

Save it to the repo root, open it in VS Code, press Run. It takes no
arguments. It writes nothing on any failure.

Written August 21, 2026 with Anthropic's Claude Opus 5 (L-223).
"""

import hashlib
import os
import sys

PATH = os.path.join('documentation', 'HANDOFF_20260821_L214_built.md')
FINGERPRINT = '4b1e4530561de56e73f7bece066029cb'

ROLLUP_OLD = """## 8. Tony-action rollup

- **Tony-action (do):** file the L-214 ledger block, re-index, commit,
  push.
- **Tony-action (do):** file this handoff to `documentation/`.
- **Tony-action (decide):** whether the reconciliation queue or the
  L-060 ENSO design round comes next. Both are ready to start; neither
  is blocked.
"""

ROLLUP_NEW = """## 8. Tony-action rollup

Both (do) items below were DISCHARGED later the same session, at
`d424c459` and `2dae4fe8`. They are left here as the record of what
was asked, struck rather than deleted. Nothing in this rollup is
outstanding except the decision.

- ~~**Tony-action (do):** file the L-214 ledger block, re-index,
  commit, push.~~ Done at `d424c459`. The indexer moved the closed
  block into its bucket itself; a second run reported no consistency
  problems.
- ~~**Tony-action (do):** file this handoff to `documentation/`.~~
  Done.
- **Tony-action (decide):** whether the reconciliation queue or the
  L-060 ENSO design round comes next. Both are ready to start; neither
  is blocked. STILL OPEN.

---

## 9. Addendum -- what happened after this handoff was written

The handoff above was written mid-session. Three things followed.

### The carried obligation, and it is the only one

**`safe-file-editing` went 1.6 -> 1.7 at `2dae4fe8` (L-223). The
session that bumped it loaded 1.6. The NEXT session confirms its
loaded copy reads 1.7 before doing patch work.**

This cannot be discharged from inside the session that made it. The
skill copy a conversation loads appears to be bound when the
conversation starts, so a reinstall lands in the account and stays
invisible to the running session. Tony reinstalled it and said so;
that is an assertion standing in for a check Claude cannot perform,
which is exactly the case the protocol declines to clear on. The
manifest in `PROJECT_INSTRUCTIONS.md` reads 1.7 and the repo copy
reads 1.7 -- both verified at HEAD. The account copy is the one that
stays honestly unverified until a load happens against it.

Section 2 of this handoff says nothing is owed. That was true when it
was written and is superseded by this line.

### L-223 -- a paste into the ledger is an unverified transfer

A paste into `LEDGER_CONSOLIDATED.md` showed no effect for about a
minute, then completed correctly. Tony checked for duplicates from the
repeated attempts and found none, and noticed the spinner resolved on
refocus. The mechanism was never verified and the ledger block says so
plainly.

The finding is not the delay. It is that no participant in the
clipboard chain owns reporting the outcome, so a dropped paste and a
successful one leave the same evidence. Tony caught it only because he
was comparing the paste against the copy.

Promoted the same day, Tony's ruling: `safe-file-editing` 1.7 adds *A
Paste Is An Unverified Transfer*. A document edit is delivered as a
patch script, the same as a code edit -- prose, markdown and the
ledger included. The rule is written around what a paste is rather
than around any editor, so it outlives this particular stall.

### What landed after `c214da50`

- `d424c459` -- the L-214 ledger block, merged, repaired and
  re-indexed. The merge had carried three defects, all mechanical: a
  metadata comment with markdown backticks pasted into it, half the
  old Gap surviving as an orphan, and two Ref blocks. All three fixed;
  every reference from both Ref blocks preserved.
- `2dae4fe8` -- `safe-file-editing` 1.7, the L-223 block, and the
  regenerated skill manifest.

Three patch scripts, all archived to `documentation/`:
`patch_L214_3_...` was built and never needed (the paste completed),
`patch_L223_1_safe_file_editing_paste_rule.py` and
`patch_L223_2_ledger_paste_instance.py` both ran clean.

### Verification at `2dae4fe8`

Re-pulled and read at HEAD rather than trusting the run reports: the
L-214 block's metadata parses as DONE / 2026-08-21 / C with one Ref
block and no Gap; L-223 is present and its index row reads DONE; the
skill file reads 1.7 and carries the new section; the manifest row
reads 1.7. The maintenance run passed 11 of 11 gating checkers, and
Tier-1 held at 292 across every patch in this session.
"""


def die(reason):
    print('')
    print('STOPPED. %s' % reason)
    print('Nothing was written.')
    sys.exit(1)


def main():
    if not os.path.isdir('documentation'):
        die('no documentation/ directory here. Run this from the '
            'palomas_orrery repo root.')
    if not os.path.exists(PATH):
        die('%s not found.' % PATH)

    with open(PATH, 'rb') as handle:
        raw = handle.read()
    if b'\r\n' in raw:
        die('%s has CRLF line endings; this patch expects LF.' % PATH)
    text = raw.decode('utf-8')

    actual = hashlib.md5(text.encode('utf-8')).hexdigest()
    if actual != FINGERPRINT:
        die('%s does not match the file this patch was written '
            'against.\n  expected md5 %s\n  found        %s'
            % (PATH, FINGERPRINT, actual))

    if '## 9. Addendum' in text:
        die('the handoff already carries an addendum. Nothing to do.')

    found = text.count(ROLLUP_OLD)
    if found != 1:
        die('the rollup anchor matched %d times, expected exactly 1.'
            % found)

    for char in ROLLUP_NEW:
        if ord(char) > 127:
            die('non-ASCII character %r in the new text.' % char)

    out = text.replace(ROLLUP_OLD, ROLLUP_NEW, 1)
    if out == text:
        die('the file came out identical to its input.')

    with open(PATH, 'wb') as handle:
        handle.write(out.encode('utf-8'))

    print('%s amended.' % PATH)
    print('  rollup: both (do) items struck as discharged; the '
          '(decide) left open.')
    print('  added:  section 9, the addendum.')
    print('')
    print('THE LINE THAT MATTERS, now in the handoff where the next '
          'session will read it:')
    print('  safe-file-editing went 1.6 -> 1.7 at 2dae4fe8; the '
          'session that bumped it loaded 1.6; the next session '
          'confirms its loaded copy reads 1.7 before patch work.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
