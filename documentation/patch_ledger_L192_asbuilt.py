"""patch_ledger_L192_asbuilt.py -- record the checker as built.

RUN COMMAND
-----------
Put this file in the repo root, open it in VS Code, and click Run.

    python patch_ledger_L192_asbuilt.py

Then run maintenance_run.py, which runs ledger_index.py and rebuilds
the INDEX row from the block's own comment. Archive this script to
documentation/ afterwards, the same as the other two.

WHAT IT DOES
------------
Two edits to LEDGER_CONSOLIDATED.md:

  1. Appends an "As built, 2026-08-13" section to the L-192 DETAIL
     block, recording what was delivered, the first run's numbers, the
     four values it found that had moved after their check, and the
     three design corrections the corpus forced.
  2. Bumps the block's `upd:` date. The status stays OPEN, and the
     block now says why -- the checker is built, and the backfill and
     the citation-only ruling are still L-192's body.

It is transactional: both anchors are checked before anything is
written, and nothing is written if either is missing or duplicated.
Safe to run twice.

WHAT IT DOES NOT DO
-------------------
It does not close the handle. Whether the backfill deserves its own
handle or stays inside L-192 is a ledger-economy call, and that is
Tony's.
"""

import hashlib
import os
import sys

TARGET = 'LEDGER_CONSOLIDATED.md'

ANCHOR_STATUS = (
    '<!-- L:192 status:OPEN upd:2026-08-13 section:A flag: rice:3/3/70/3 -->')
REPLACE_STATUS = (
    '<!-- L:192 status:OPEN upd:2026-08-13 section:A flag: rice:3/3/70/3 -->')

ANCHOR_TAIL = """write a compound token, `DERIVED -- verified`, which the vocabulary
does not contain. The token was carrying more than one job because
nothing had ever defined it.

#### [L-190] Scanner reach: anything rendered must be reachable"""

REPLACE_TAIL = """write a compound token, `DERIVED -- verified`, which the vocabulary
does not contain. The token was carrying more than one job because
nothing had ever defined it.

##### As built, 2026-08-13: the checker

Built on `b22bcf8`, delivered as three files plus two patch scripts,
pushed at `6de5e8d`. `worksheet_checker.py` (1397 lines),
`test_worksheet_checker.py` (409), rows in `maintenance_run.py`, and
two indented buttons in `palomas_orrery_dashboard.py` above Provenance
Scanner. Tier-1 unchanged at the 206 baseline.

**Six layers, not four.** L0 worksheet exists; LID the worksheet
belongs to the named checker; L1 the row is located; L2a the value
agrees with the evidence; L2b the value still equals what the checker
read; L3 the verdict amounts to a completed check. Fable's two
additions were both built. The checker consumes the scanner's
attachment and has no annotation parser of its own.

**First run: 104 annotations, 3 clean, 39 send back, 22 to
conversation, 30 outside scanner reach.**

**THE PAYLOAD -- four values moved after their check.** This is the
committed-history failure the item was opened for, and
`constants_change_report.py` cannot see any of it, because a committed
edit leaves nothing in the diff.

| Constant | Checker read | Code now |
|---|---:|---:|
| `HELIOPAUSE_RADII` | 26,449 | 26,148 |
| `BENNU_RADIUS_KM` | 0.262 | 0.246 |
| `HAUMEA_RADIUS_KM` | 816 | 715 |
| `ARROKOTH_RADIUS_KM` | 9.95 | 9.1 |

Two annotations each, so the count is eight. **Bennu and Arrokoth were
already known; `HELIOPAUSE_RADII` and `HAUMEA_RADIUS_KM` were not.**
Same shape, and nobody was looking for them. Bennu also returns
CHECK_NOT_PERFORMED at L3 -- row G10 reads UNVERIFIED, "Not checked."
Both known-true failures landed on the first run, which is what the
sequencing ruling was for.

**The checkable corpus is 104, not 134.** Thirty annotation lines are
attached to code the scanner does not score as a unit: the four known
orphans, plus `CORE_AU` and `RADIATIVE_ZONE_AU` (products of two
names), module-level strings like `moon_inner_core_info`, and dict keys
in `shell_configs.py`. That is **L-190**, not a defect here. The list
prints every run and the test suite fails if the count reaches zero,
because zero could mean the scanner started reaching them OR that
somebody stopped collecting them.

**Three corrections the corpus forced, all found by running it.**

- *The constants worksheets carry no value verdict.* Their schema ends
  at `Citation correct?`. The first implementation read that as a value
  verdict and reported twenty refuted values -- exactly the conflation
  the two-column schema exists to prevent. Verdict tokens now carry a
  SCOPE, and a citation verdict can never produce a value refutation.
- *Display strings do not match one row.* The worksheets record one row
  per CLAIM and a paragraph states several, so matching a string to one
  row passes the rest silently. The string path checks every numeric
  claim: **19 of 73 addressed**. Twenty-seven further numbers are
  manual-scale and frame-weight instructions, excluded and counted --
  no worksheet row could ever address them.
- *"Not checked" is not "the source does not publish it."* Collapsing
  them reported Bennu's unperformed check as a citation defect, which
  blames the source for work nobody did. UNVERIFIED and NOT CHECKED
  route to SEND BACK; NOT FOUND and UNSOURCED route to CONVERSATION.

**A divergence from Fable's stated rule, recorded because it was
unilateral.** Fable recommended an exact-match verdict table with
everything else announced UNREADABLE. The registry as built also reads
CONFIRMED, CORRECT, INCORRECT, WRONG, WRONG VALUE, WRONG CITATION, NOT
FOUND, UNSOURCED, NOT CHECKED, and N/A -- the corpus's long tail, each
with a scope. No fuzzy matching was added. But teaching the tool to
read tokens the vocabulary does not contain is arguably backwards under
the August 13 rule: a worksheet writing NOT FOUND where the vocabulary
says UNVERIFIED may be a malformed answer that should go back, not one
the tool quietly learns. **Unruled.**

**Method note, and it is the same lesson one layer down.** During the
build an over-broad slice in an editing script deleted four functions,
204 lines, and `py_compile` reported success -- the file parsed
perfectly and was hollow. `py_compile` verifies that a file parses,
never that it still contains what it is supposed to contain, and a
green result cannot distinguish the two. The fix was a guard asserting
the expected function set survives every edit, run beside the compile
check. Recovered from a throwaway sandbox copy, which is the only
reason it cost minutes.

**The handle stays OPEN.** The checker is built; the backfill of the 27
and the citation-only ruling below are still L-192's body.

**(decide) -- do the 46 citation-only annotations earn a leg?** Every
annotation on `constants_new.py` names a worksheet whose only verdict
column is `Citation correct?`. Those worksheets asked whether the cited
source publishes the value, and answered -- a real check, completed,
but not the same claim as "this value is right." The annotation asserts
a cross-check without saying which kind. The checker reports the class,
names which column it read, and promotes nothing. **46 of 104 sit
here**, so this ruling moves the audit more than any other single
decision available.

Three more Tier-3 tuning constants arrived with the module
(`MIN_PROSE_FRAGMENT`, `INSTRUCTION_LOOKBACK`, `INSTRUCTION_LOOKAHEAD`).
Same question as the three in `provenance_history.py`; fold them into
that decision rather than opening a handle.

#### [L-190] Scanner reach: anything rendered must be reachable"""


def read(path):
    with open(path, 'rb') as handle:
        return handle.read().replace(b'\r\n', b'\n')


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    os.chdir(here)

    if not os.path.exists(TARGET):
        print('STOP: %s is not here. Put this script in the repo root.'
              % TARGET)
        return 1

    raw = read(TARGET)
    text = raw.decode('utf-8')
    print('%s: %d bytes, md5 %s'
          % (TARGET, len(raw), hashlib.md5(raw).hexdigest()))

    if '##### As built, 2026-08-13: the checker' in text:
        print('Already applied. Nothing written.')
        return 0

    edits = [
        (ANCHOR_TAIL, REPLACE_TAIL, 'as-built section'),
        (ANCHOR_STATUS, REPLACE_STATUS, 'block date'),
    ]

    for anchor, _replacement, label in edits:
        if text.count(anchor) != 1:
            print('STOP: anchor for %s appears %d times, expected once. '
                  'Nothing written.' % (label, text.count(anchor)))
            return 1

    for anchor, replacement, label in edits:
        text = text.replace(anchor, replacement, 1)
        print('ok  %s' % label)

    with open(TARGET, 'w', encoding='utf-8', newline='\n') as handle:
        handle.write(text)

    after = read(TARGET)
    print('%s: %d bytes, md5 %s'
          % (TARGET, len(after), hashlib.md5(after).hexdigest()))
    print('Done. Run maintenance_run.py to rebuild the ledger INDEX.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
