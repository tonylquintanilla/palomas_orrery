"""patch_L192_runner.py -- wire the worksheet checker into the runner.

RUN COMMAND
-----------
Put this file in the repo root, open it in VS Code, and click Run.

    python patch_L192_runner.py

WHAT IT DOES
------------
Two edits to maintenance_run.py, applied bottom-up so the first edit
cannot shift the line the second one is looking for:

  1. Adds two CHECKERS rows -- the worksheet checker and its tests.
     The checker gets a verdict hint, because its summary line is not
     its last line and the denominator is the number worth reading.
  2. Adds one line to the module docstring saying what the new checker
     does and that it is report-only.

It is transactional. The file is fingerprinted before anything is
written; if any anchor is missing the script stops and writes nothing,
so a half-applied file is not a state this can produce. Line endings
are normalised to LF and the output is ASCII only.

Safe to run twice: it detects work already done and says so.
"""

import hashlib
import os
import sys

TARGET = 'maintenance_run.py'
EXPECT_MD5 = '487dee8cb5a208873d9ead99dc7eb5ca'  # maintenance_run.py at b22bcf8

ANCHOR_CHECKERS = (
    "    ('Provenance scanner', ['provenance_scanner.py'], "
    "'TIER-1 FINDINGS'),\n]")
REPLACE_CHECKERS = (
    "    ('Provenance scanner', ['provenance_scanner.py'], "
    "'TIER-1 FINDINGS'),\n"
    "    ('Worksheet checker', ['worksheet_checker.py'], "
    "'WORKSHEET CHECK:'),\n"
    "    ('Worksheet checker tests', ['test_worksheet_checker.py'], None),\n"
    "]")

ANCHOR_DOC = (
    "Constants change runs first among them: it reads the git diff for\n"
    "constants_new.py and reports any value that moved without its provenance\n"
    "moving too. It replaced 55 hand-pinned literals on 2026-08-12 and stores\n"
    "no numbers of its own.\n")
REPLACE_DOC = (
    "Constants change runs first among them: it reads the git diff for\n"
    "constants_new.py and reports any value that moved without its provenance\n"
    "moving too. It replaced 55 hand-pinned literals on 2026-08-12 and stores\n"
    "no numbers of its own.\n"
    "\n"
    "The worksheet checker runs last. It opens the worksheet each cross-check\n"
    "annotation names and reports whether that worksheet records the check the\n"
    "annotation claims. It is REPORT-ONLY: it exits 0 whatever it finds, and\n"
    "exits 1 only when it could not run. Its one summary line carries a\n"
    "denominator, so the number moves when something moves; findings go to\n"
    "WORKSHEET_CHECK.md.\n")


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
    print('%s: %d bytes, md5 %s' % (TARGET, len(raw),
                                    hashlib.md5(raw).hexdigest()))

    actual = hashlib.md5(raw).hexdigest()
    if actual != EXPECT_MD5:
        print('NOTE: %s does not match the copy this patch was built '
              'against (expected %s). The anchor checks below still '
              'decide whether it is safe.' % (TARGET, EXPECT_MD5))

    if "('Worksheet checker'," in text:
        print('Already applied -- the runner already lists the worksheet '
              'checker. Nothing written.')
        return 0

    edits = [(ANCHOR_DOC, REPLACE_DOC, 'docstring note'),
             (ANCHOR_CHECKERS, REPLACE_CHECKERS, 'CHECKERS rows')]

    for anchor, _replacement, label in edits:
        if text.count(anchor) != 1:
            print('STOP: anchor for %s appears %d times, expected once. '
                  'Nothing written.' % (label, text.count(anchor)))
            return 1

    # Bottom-up: the CHECKERS table sits below the docstring, so it is
    # replaced first and the docstring edit cannot move it.
    for anchor, replacement, label in reversed(edits):
        text = text.replace(anchor, replacement, 1)
        print('ok  %s' % label)

    with open(TARGET, 'w', encoding='utf-8', newline='\n') as handle:
        handle.write(text)

    after = read(TARGET)
    print('%s: %d bytes, md5 %s' % (TARGET, len(after),
                                    hashlib.md5(after).hexdigest()))
    print('Done. Run maintenance_run.py to see the new rows.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
