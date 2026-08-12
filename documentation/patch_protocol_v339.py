"""Protocol v3.39 -- A Check That Cannot Fail Is Not Passing [CRITICAL].

RUN COMMAND
-----------
Save this file into the palomas_orrery repo ROOT, open it in VS Code, and
click Run.

    python patch_protocol_v339.py

WHAT IT DOES
------------
Adds one CRITICAL gate to Part 3 of PROJECT_INSTRUCTIONS.md, immediately
after Verify Execution, Not Appearance, and records v3.39 in the version
history.

WHY IT IS A GATE AND NOT A LESSON
---------------------------------
It fired three times in one session, 2026-08-12, in three unrelated
layers, and each time the failure looked exactly like success:

  - The skill layer. provenance-discipline taught an annotation format
    whose own worked example provenance_scanner.py could not read. The
    scanner reported no problem, because a line it cannot parse produces
    no record and no complaint. Nineteen completed two-model cross-checks
    were scored and reported as half-done for a week.

  - test_constants_provenance.py. It pinned 55 values in a file nothing
    ran, so its verdict reached nobody for ten days. A test whose result
    is never read has the same value as no test.

  - constants_change_report.py, twice. First: a changed line in a shape
    its regexes did not match was skipped in silence, so an unreadable
    edit reported clean. Second, and the one Tony found by asking what
    tells us git is working: `git diff <rev> -- <path>` exits 0 with no
    output when the path is untracked or absent, so "no changes" printed
    identically whether the file was clean, untracked, or gone.

The common shape is not a bug in any of them. It is that PASSING and NOT
RUNNING produce the same output, so no amount of reading the result can
tell them apart.

SAFETY
------
Transactional: both anchors must match exactly once or nothing is
written. LF-normalized fingerprint, binary-mode I/O, CRLF preserved.

WHAT SUCCESS LOOKS LIKE
-----------------------
Two `ok` lines, then `patch applied`.

AFTER RUNNING
-------------
Run maintenance_run.py, then commit. skills_index.py rewrites only the
manifest zone, so it will not disturb this edit.
"""

import hashlib
import os
import sys

PROTOCOL = 'PROJECT_INSTRUCTIONS.md'
BASE_MD5 = 'f88e315134d2d7ca1be6c78584172528'

EDITS = []

# ---- 1. the gate itself ----------------------------------------------
EDITS.append(('Part 3: the new CRITICAL gate',
b"""When the render disagrees with the code reading, the render wins. This is
the same lesson as Check All Parallel Pipelines, one step upstream:
confirm which path is LIVE before editing anything.

Check All Parallel Pipelines [CRITICAL]""",
b"""When the render disagrees with the code reading, the render wins. This is
the same lesson as Check All Parallel Pipelines, one step upstream:
confirm which path is LIVE before editing anything.

A Check That Cannot Fail Is Not Passing [CRITICAL]
Companion to the gate above, aimed one layer further out. That one asks
whether the code you edited is the code that runs. This one asks whether
the CHECK you are trusting can produce a failure at all.

A green result answers two questions at once and does not say which:
did this pass, or did it never run? Those look identical on screen. A
test file nobody executes, a parser that silently skips what it cannot
read, a diff against a path the tool does not track -- each reports
exactly what a real pass reports.

So the test is not "did it pass." It is: WHAT WOULD MAKE THIS FAIL, and
does the passing output prove that path was live?

Three moves, in order of how often they are the answer:
- Make success carry evidence. Print what was compared, against what,
  and how many things were examined. "No changes since <sha> <subject>"
  cannot print unless the revision resolved; "no changes" alone can
  print for any reason at all.
- Make the blind spot announce. Anything the check could not read is
  reported and fails the run -- never dropped. Silence about something
  unexamined is the failure mode, not a tidy output.
- Put the check where it runs. A check in a store nobody opens is a
  check that cannot fail, no matter how correct it is. Prefer the tool
  already in the routine over the file that has to be remembered.

The confirming question, and it is Tony's: what tells us it is working?
If the only answer is that it did not complain, that is not an answer.

(Origin, August 12, 2026: three instances in one session, in three
unrelated layers -- a skill whose own example the parser could not read,
a 55-pin test file nothing executed for ten days, and a git diff that
exits 0 with empty output for an untracked path. Each was found by a
different route and none was found by reading a passing result.)

Check All Parallel Pipelines [CRITICAL]""")) 

# ---- 2. version history ----------------------------------------------
EDITS.append(('version history: v3.39',
b"""Functional for Claude, readable for human, signal preserved.""",
b"""v3.39 (August 12, 2026): One change. "A Check That Cannot Fail Is Not
Passing" added to Part 3 as a CRITICAL gate, immediately after Verify
Execution, Not Appearance, which it extends: that gate asks whether the
edited code is the code that runs, this one asks whether the check being
trusted can produce a failure at all. Origin was three instances in a
single session, each in a different layer and each indistinguishable
from a pass -- the provenance-discipline skill teaching an annotation
format its own parser could not read, test_constants_provenance.py
pinning 55 values in a file no routine executed, and
constants_change_report.py reporting clean both for an edit shape it
could not parse and for a path git does not track. The gate's three
moves are: make success carry evidence, make the blind spot announce,
and put the check where it actually runs. Tony's confirming question --
what tells us it is working -- is the one that found the third instance.

Functional for Claude, readable for human, signal preserved.""")) 


def fingerprint(data):
    """MD5 over LF-normalized content -- line endings are not content."""
    return hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, PROTOCOL)
    if not os.path.exists(path):
        print('ERROR: %s not found. Run this from the repo root.' % PROTOCOL)
        sys.exit(1)

    with open(path, 'rb') as handle:
        data = handle.read()

    got = fingerprint(data)
    if got != BASE_MD5:
        print('ERROR: base moved for %s' % PROTOCOL)
        print('       expected %s' % BASE_MD5)
        print('       got      %s' % got)
        print('Nothing written.')
        sys.exit(1)

    is_crlf = data.count(b'\r\n') > 0
    if is_crlf:
        print('note: %s uses CRLF; anchors translated to match.' % PROTOCOL)

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

    # The header carries version AND date; both move together, or the
    # document says v3.39 was issued on the day v3.38 was.
    header_old = b'| v3.38 | August 11, 2026'
    header_new = b'| v3.39 | August 12, 2026'
    if is_crlf:
        header_old = header_old.replace(b'\n', b'\r\n')
        header_new = header_new.replace(b'\n', b'\r\n')
    if data.count(header_old) != 1:
        print('ANCHOR FAIL (header): expected 1 match, found %d.'
              % data.count(header_old))
        print('Nothing written.')
        sys.exit(1)
    data = data.replace(header_old, header_new)
    print('  ok  header bumped to v3.39, August 12, 2026')

    with open(path, 'wb') as handle:
        handle.write(data)

    print()
    print('patch applied -- %s, %d bytes' % (PROTOCOL, len(data)))
    print()
    print('NEXT: run maintenance_run.py, then commit.')


if __name__ == '__main__':
    main()
