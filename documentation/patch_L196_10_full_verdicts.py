"""patch_L196_10_full_verdicts.py -- finish the sentences the maintenance
runner was cutting off, and name the 1d/1e dashboard card for what it
checks.

RUN COMMAND
-----------
Save this file into the palomas_orrery repo root (the same folder as
maintenance_run.py), open it in VS Code, and click Run.

    python patch_L196_10_full_verdicts.py

BASE
----
This is built on the tree AFTER patch_L196_9_launch_tooltips.py has run,
which is the working copy on Tony's disk and is one push ahead of repo
HEAD 5840145. Running it on an un-patched tree aborts with nothing
written.

WHAT IT DOES
------------
1. maintenance_run.py -- verdicts wrap instead of truncating.

   Five checker rows ended in "..." because a verdict longer than 44
   characters was cut. The full sentence now continues on indented
   lines under the same column:

       Worksheet key round trip     0.7s  RESULT: 52 sites minted 52
                                          distinct keys, all resolved;
                                          55 pinned keys still resolve;
                                          3 retired keys confirmed gone.

   Widening the column instead would have pushed the longest verdict
   past 160 characters and wrapped it in the console anyway, where the
   wrap point lands wherever the window happens to end. This wraps at a
   word boundary at a width the file controls. Generator rows go
   through the same path, so they cannot truncate either.

   fit() stays in the file. It is still used for the short verdict
   appended to a FAILED row, where 30 characters is the intent rather
   than an accident.

2. palomas_orrery_dashboard.py -- the card reading "Test Provenance
   1d/1e" becomes "Test Scanner Recognition", with a description that
   says what the test proves and why half of it is written backwards.
   "1d/1e" is a ledger sub-step; it named the work to whoever did it
   and nothing to anyone reading the dashboard later.

PERMANENT vs DISPOSABLE
-----------------------
This script is disposable and one-shot. What it installs is permanent:
the wrapped() and print_row() helpers, their use by both row printers,
and the renamed dashboard card.

SAFETY
------
All-or-nothing. Both files are fingerprinted (CRLF-normalized) before
anything is written, and every anchor must match exactly once. Any
mismatch aborts the whole run with nothing written. Each file's own
line endings are preserved.

Success: one 'ok' line per file, then 'patch applied (N bytes)'.
Failure: a single 'ERROR:' or 'ANCHOR FAIL' line; nothing is written.
"""

import hashlib
import os
import sys


OLD_FIT = '''def fit(text, width=44):
    """Trim to width on a word boundary rather than mid-word."""
'''

NEW_FIT = '''NOTE_WIDTH = 44
NOTE_INDENT = 37        # matches '  %-25s %6.1fs  ' below


def wrapped(text, width=NOTE_WIDTH):
    """The whole sentence across as many lines as it needs.

    A verdict is the one line of a tool's output anybody reads, so it
    does not get an ellipsis. A single token longer than the width --
    a file path, usually -- overhangs rather than being cut in half.
    """
    lines = []
    current = ''
    for word in (text or '').split():
        candidate = word if not current else current + ' ' + word
        if len(candidate) > width and current:
            lines.append(current)
            current = word
        else:
            current = candidate
    if current:
        lines.append(current)
    return lines or ['']


def print_row(label, seconds, note):
    """One tool's row: label, elapsed, and its verdict in full."""
    lines = wrapped(note)
    print('  %-25s %6.1fs  %s' % (label, seconds, lines[0]))
    for extra in lines[1:]:
        print(' ' * NOTE_INDENT + extra)


def fit(text, width=44):
    """Trim to width on a word boundary rather than mid-word."""
'''

OLD_GEN_ROW = """        print('  %-25s %6.1fs  %s' % (label, seconds, note))
        results.append((label, rc, seconds, note, output, False))
"""

NEW_GEN_ROW = """        print_row(label, seconds, note)
        results.append((label, rc, seconds, note, output, False))
"""

OLD_CHK_ROW = """            note = fit(verdict or last_meaningful_line(output)) or 'passed'
        else:
            note = 'FAILED (exit %d)' % rc
            if verdict:
                note += ' -- ' + fit(verdict, 30)
        print('  %-25s %6.1fs  %s' % (label, seconds, note))
        results.append((label, rc, seconds, note, output, True))
"""

NEW_CHK_ROW = """            note = (verdict or last_meaningful_line(output)) or 'passed'
        else:
            note = 'FAILED (exit %d)' % rc
            if verdict:
                note += ' -- ' + fit(verdict, 30)
        print_row(label, seconds, note)
        results.append((label, rc, seconds, note, output, True))
"""

OLD_CARD = '''        ("Test Provenance 1d/1e",
         "test_provenance_1d.py",
         "Pass/fail regression tests for the Phase 1d/1e scanner mechanisms.",
'''

NEW_CARD = '''        ("Test Scanner Recognition",
         "test_provenance_1d.py",
         "Proves the provenance scanner still recognizes a real citation "
         "and still refuses a fake one. Covers shadow constants (a local "
         "copy of a value already defined and cited in constants_new.py), "
         "author-year forms like (Nolan et al. 2013), F/C units, and tier "
         "labels. Half the tests are written backwards on purpose: a regex "
         "that is too loose clears findings by matching what it should "
         "not, and the Tier-1 count then falls, which looks like progress. "
         "Ledger L-156, sub-steps 1d and 1e.",
'''

EDITS = {
    'maintenance_run.py': {
        'fp': '2546401bf4cee534e3e928a292211bf4',
        'edits': [
            (OLD_FIT, NEW_FIT),
            (OLD_GEN_ROW, NEW_GEN_ROW),
            (OLD_CHK_ROW, NEW_CHK_ROW),
        ],
    },
    'palomas_orrery_dashboard.py': {
        'fp': '36254ca641035c1ee97d94d81e41b8da',
        'edits': [
            (OLD_CARD, NEW_CARD),
        ],
    },
}


def normalized(data):
    return data.replace(b'\r\n', b'\n')


def non_ascii_count(data):
    return sum(1 for byte in data if byte > 127)


def main():
    if not os.path.isfile('maintenance_run.py'):
        print('ERROR: run this from the palomas_orrery repo root '
              '(the folder holding maintenance_run.py).')
        return 1

    staged = []
    total = 0
    notes = []

    for name in sorted(EDITS):
        spec = EDITS[name]
        if not os.path.isfile(name):
            print('ERROR: %s not found.' % name)
            return 1

        with open(name, 'rb') as handle:
            raw = handle.read()

        fp = hashlib.md5(normalized(raw)).hexdigest()
        if fp != spec['fp']:
            print('ERROR: %s does not match the base this patch was built '
                  'against.' % name)
            print('       expected %s' % spec['fp'])
            print('       found    %s' % fp)
            print('       Nothing written. This patch expects the tree '
                  'AFTER patch_L196_9 has run.')
            return 1

        crlf = b'\r\n' in raw
        text = normalized(raw).decode('utf-8')

        for old, new in spec['edits']:
            count = text.count(old)
            if count != 1:
                print('ANCHOR FAIL: %s -- expected 1 match, found %d.'
                      % (name, count))
                print('       anchor starts: %r' % old[:70])
                print('       Nothing written.')
                return 1
            inserted = non_ascii_count(new.encode('utf-8'))
            if inserted:
                print('ERROR: %s -- an inserted block carries %d non-ASCII '
                      'byte(s). Nothing written.' % (name, inserted))
                return 1
            text = text.replace(old, new)

        out = text.encode('utf-8')
        pre_existing = non_ascii_count(out)
        if pre_existing:
            notes.append('note: %s still holds %d non-ASCII byte(s) this '
                         'patch did not reach' % (name, pre_existing))
        if crlf:
            out = out.replace(b'\n', b'\r\n')
        staged.append((name, out, len(spec['edits'])))
        total += len(out)

    for name, out, count in staged:
        with open(name, 'wb') as handle:
            handle.write(out)
        print('ok  %-34s %d edit(s)' % (name, count))

    for note in notes:
        print(note)
    print('patch applied (%d bytes)' % total)
    print('')
    print('Next: run maintenance_run.py -- no row should end in "...".')
    return 0


if __name__ == '__main__':
    sys.exit(main())
