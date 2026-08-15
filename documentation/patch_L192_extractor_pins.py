"""Wire the extractor pin test into the runner; record the freeze.

Two edits, two files:

  maintenance_run.py      one CHECKERS row, after the key round trip
  worksheet_checker.py    a note above the frozen constants naming the
                          ruling and the pin file that enforces it

Each edit asserts EXACTLY ONE match for its anchor before anything is
written, and both are planned before either is written, so a drifted
second file cannot leave the first one half-patched. Re-running is
safe: a file already carrying the edit reports 'already' and is left
alone.

No whole-file fingerprint guard, deliberately. A two-anchor insertion
does not need the file to be byte-identical to 66cf0cb, and an MD5
gate would abort on any unrelated local edit. The anchor count is the
guard; the resulting hash is printed as evidence of what was written.

Run it from the repo root with the Run button. It prints what it did
and changes nothing else.

Written August 2026 with Anthropic's Claude Opus 5 (L-192).
"""

import hashlib
import os
import sys

RUNNER_ANCHOR = (
    "    ('Worksheet key round trip', ['test_worksheet_keys.py'], None),\n")
RUNNER_ADDITION = (
    "    ('Extractor pins', ['test_extractor_pins.py'], None),\n")

CHECKER_ANCHOR = (
    "# Tight and directional on purpose. The instruction phrase sits right\n")
CHECKER_ADDITION = (
    "# FROZEN by Tony 2026-08-14 and pinned. Measured over the L-192\n"
    "# corpus, the drop set is identical for lookback 25 through 60 at\n"
    "# every lookahead tested; 30 sits mid-plateau. These values decide\n"
    "# which numbers count as claims, and the ::cN ordinal in every\n"
    "# issued key counts claims AFTER this filter runs -- so retuning\n"
    "# either one re-points ordinals corpus-wide with no prose edit at\n"
    "# all. test_extractor_pins.py asserts them against\n"
    "# documentation/worksheets/L192_extractor_pins.txt on every run.\n"
    "#\n")


def normalized(path):
    with open(path, 'rb') as handle:
        return handle.read().replace(b'\r\n', b'\n')


def fingerprint(path):
    return hashlib.md5(normalized(path)).hexdigest()


def plan(path, anchor, before, after, sentinel):
    """(action, new_bytes) without writing anything."""
    text = normalized(path).decode('utf-8')
    if sentinel in text:
        return 'already', None
    count = text.count(anchor)
    if count != 1:
        return 'drifted: %d matches for the anchor, expected 1' % count, None
    return 'apply', text.replace(anchor, before + anchor + after).encode('utf-8')


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    os.chdir(root)

    jobs = [
        ('maintenance_run.py', RUNNER_ANCHOR, '', RUNNER_ADDITION,
         "'Extractor pins'"),
        ('worksheet_checker.py', CHECKER_ANCHOR, CHECKER_ADDITION, '',
         'FROZEN by Tony 2026-08-14'),
    ]

    for name, _anchor, _before, _after, _sentinel in jobs:
        if not os.path.exists(name):
            print('ABORT: %s not found. Run this from the repo root.' % name)
            return 1

    results = []
    for name, anchor, before, after, sentinel in jobs:
        action, payload = plan(name, anchor, before, after, sentinel)
        if action.startswith('drifted'):
            print('ABORT: %s %s' % (name, action))
            print('Nothing was written, in either file. The anchor this')
            print('patch inserts against is not where it was when the')
            print('patch was written.')
            return 1
        results.append((name, action, payload))

    for name, action, payload in results:
        if action == 'already':
            print('  already   %s  (%s)' % (name, fingerprint(name)))
            continue
        with open(name, 'wb') as handle:
            handle.write(payload)
        print('  patched   %s  -> %s' % (name, fingerprint(name)))

    if all(action == 'already' for _n, action, _p in results):
        print('Nothing to do. Both edits are already in place.')
        return 0

    print()
    print('Done. Next: run test_extractor_pins.py once on its own, then')
    print('maintenance_run.py, and confirm the Extractor pins row appears.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
