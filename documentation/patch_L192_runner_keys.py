"""Wire the worksheet key round trip into the maintenance runner (L-192).

Domain: dev_tools

WHY THIS PATCH EXISTS

test_worksheet_keys.py pins 53 keys minted at 305b269 and resolves
them against current source. Pinned keys are the only thing that can
notice a rename -- a round trip that mints from today's source and
resolves against today's source agrees with itself no matter what the
source says, which is how the first version of that test passed a
mutation it should have failed.

But a test nobody runs cannot fail either, whatever it checks. That is
not hypothetical here: test_constants_provenance.py pinned 55 values
in a file no routine executed for ten days, and it is one of the three
instances that produced the v3.39 gate. Adding the file without adding
the row would reproduce it exactly.

WHAT IT CHANGES

One row appended to CHECKERS in maintenance_run.py, immediately after
the worksheet checker's own tests, so the key round trip runs in the
same sweep that runs everything else. No hint string: the test ends on
a pass/fail summary and returns a non-zero exit on any failure, which
is what the runner reads when the hint is None.

HOW TO RUN IT

Open this file in VS Code and press Run. It prints what it found
before it writes anything, and writes nothing at all if any check
fails. Safe to run twice -- the second run stops at the
already-applied check rather than adding a duplicate row.

WHAT IT REFUSES TO DO

- If maintenance_run.py is not the file this was built against, it
  stops and prints both fingerprints. The comparison ignores line
  endings, because a Windows working copy can hold CRLF where the repo
  holds LF and that is not a content difference.
- If the anchor row is missing or appears more than once, it stops.
  One match or nothing.
- It writes to a temporary file and renames it into place, so an
  interruption cannot leave a half-written runner.

Patch written August 2026 with Anthropic's Claude Opus 5, built on
305b2697648590e4a75551c73743abc98bd20c66 at
https://github.com/tonylquintanilla/palomas_orrery.
"""

import hashlib
import os
import sys

TARGET = 'maintenance_run.py'

# Fingerprint of the file this patch was built against, with line
# endings normalized. Content, not raw bytes -- see the docstring.
EXPECTED_FINGERPRINT = '3251a4f61b0712566ed731f55adde049'

ANCHOR = (b"    ('Worksheet checker tests', "
          b"['test_worksheet_checker.py'], None),")

NEW_ROW = (b"    ('Worksheet key round trip', "
           b"['test_worksheet_keys.py'], None),")

ALREADY = b"test_worksheet_keys.py"


def fingerprint(data):
    return hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()


def main():
    project_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(project_dir, TARGET)

    print('=' * 70)
    print('PATCH: worksheet key round trip -> maintenance runner (L-192)')
    print('=' * 70)

    if not os.path.exists(path):
        print('  STOPPED: %s not found next to this script.' % TARGET)
        print('  Put this patch in the repo root and run it again.')
        return 1

    with open(path, 'rb') as handle:
        data = handle.read()

    found = fingerprint(data)
    print('  Fingerprint expected: %s' % EXPECTED_FINGERPRINT)
    print('  Fingerprint found:    %s' % found)

    if ALREADY in data:
        print('  STOPPED: %s is already in the runner. Nothing to do.'
              % ALREADY.decode())
        return 0

    if found != EXPECTED_FINGERPRINT:
        print('  STOPPED: this is not the file the patch was built against.')
        print('  Nothing was written. Either the runner changed since')
        print('  305b269, or an earlier edit landed. Reconcile before')
        print('  patching -- do not edit this fingerprint to make it pass.')
        return 1

    matches = data.count(ANCHOR)
    print('  Anchor matches:       %d (need exactly 1)' % matches)
    if matches != 1:
        print('  STOPPED: nothing written.')
        return 1

    # Match the file's own line ending. A Windows working copy can
    # hold CRLF; inserting a bare LF would leave one mixed line, which
    # git normalizes away and nobody would ever see -- but "nobody
    # sees it" is not a reason to write it.
    newline = b'\r\n' if data.count(b'\r\n') > data.count(b'\n') // 2 else b'\n'
    print('  Line ending:          %r' % newline)
    patched = data.replace(ANCHOR, ANCHOR + newline + NEW_ROW)

    # Write beside the target and rename into place, so an interrupted
    # run cannot leave the runner half written.
    temporary = path + '.patch_tmp'
    with open(temporary, 'wb') as handle:
        handle.write(patched)
    os.replace(temporary, path)

    print('  WROTE: one row added after the worksheet checker tests.')
    print()
    print('  Next: press Run on maintenance_run.py and confirm a row')
    print('  reading "Worksheet key round trip" appears and passes.')
    print('  A row that does not appear is the failure this patch was')
    print('  meant to prevent, not a cosmetic problem.')
    print('=' * 70)
    return 0


if __name__ == '__main__':
    sys.exit(main())
