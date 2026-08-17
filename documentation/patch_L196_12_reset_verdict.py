"""patch_L196_12_reset_verdict.py -- stop the Reset completeness row
reporting an atexit message as its verdict.

RUN COMMAND
-----------
Save this file into the palomas_orrery repo root (the same folder as
test_reset_completeness.py), open it in VS Code, and click Run.

    python patch_L196_12_reset_verdict.py

WHAT WAS WRONG, AND IT IS NOT WHAT ORBIT CACHE HAD
--------------------------------------------------
test_reset_completeness.py already prints a good verdict:

    PASS -- all 47 IntVars + 6 StringVars + 9 entries reset to startup
    defaults; date set to now.

The problem is what comes AFTER it. The test imports palomas_orrery,
which constructs a PlotlyShutdownHandler, which registers an atexit
cleanup. When the interpreter shuts down -- after sys.exit(0), after
the verdict -- that handler prints:

    Cleaning up visualization resources...
    Cleanup complete.

maintenance_run.py takes the LAST non-blank line of stdout, so it read
the atexit message. The verdict was correct, printed, and buried by two
lines of housekeeping from a module the test only imports.

So this is a different defect from test_orbit_cache.py, where no
verdict reached stdout at all. Here the verdict exists; the runner was
looking in a place a later print could occupy.

WHAT IT DOES
------------
Uses the mechanism maintenance_run.py already has for exactly this. A
CHECKERS row can name a hint substring, and the FIRST line carrying it
becomes the verdict -- position-independent, so nothing printed later
can displace it. The provenance scanner already uses this because it
ends on a banner rather than its verdict.

Two edits to test_reset_completeness.py put a stable prefix on both
outcomes, matching the existing 'WORKSHEET CHECK:' house style:

    RESET COMPLETENESS: PASS -- all 47 IntVars ...
    RESET COMPLETENESS: FAIL -- 3 var(s) not reset to startup default:

Two edits to maintenance_run.py: one gives the row that hint, and one
stops the displayed verdict from repeating it. 'Reset completeness ...
RESET COMPLETENESS: PASS' spends the column on the label twice; the
prefix is stripped for display only where the hint actually starts the
line, so the scanner's mid-line 'TIER-1 FINDINGS' is untouched and the
worksheet checker row loses its redundant 'WORKSHEET CHECK:' too. The prefix is
on BOTH lines so a failing run still shows its reason next to
'FAILED (exit 1)' rather than dropping to a bare exit code.

WHAT THIS DOES NOT FIX
----------------------
Eleven of thirteen checker rows still resolve their verdict by last
line, which means any of them can be displaced the same way by a print
that arrives later. Giving every row a hint is the general fix and is
not attempted here.

PERMANENT vs DISPOSABLE
-----------------------
This script is disposable and one-shot. What it installs is permanent:
the prefixed verdict lines and the hint on the CHECKERS row.

SAFETY
------
All-or-nothing, fingerprinted (CRLF-normalized), every anchor matched
exactly once. Any mismatch aborts with nothing written. Each file's own
line endings are preserved.

Success: one 'ok' line per file, then 'patch applied (N bytes)'.
Failure: a single 'ERROR:' or 'ANCHOR FAIL' line; nothing is written.
"""

import hashlib
import os
import sys


OLD_FAIL = '''    print(f"\\nFAIL -- {len(failures)} var(s) not reset to startup default:")
'''

NEW_FAIL = '''    print(f"\\nRESET COMPLETENESS: FAIL -- {len(failures)} var(s) not "
          f"reset to startup default:")
'''

OLD_PASS = '''print(f"\\nPASS -- all {len(intvars)} IntVars + {len(strvars)} StringVars + "
      f"{len(entries)} entries reset to startup defaults; date set to now.")
'''

NEW_PASS = '''# The prefix is what maintenance_run.py matches on. Without it the runner
# falls back to the last line of stdout, which is the atexit cleanup
# message from the PlotlyShutdownHandler that importing palomas_orrery
# registers -- printed after this one, and not a verdict.
print(f"\\nRESET COMPLETENESS: PASS -- all {len(intvars)} IntVars + "
      f"{len(strvars)} StringVars + {len(entries)} entries reset to "
      f"startup defaults; date set to now.")
'''

OLD_STRIP = """        verdict = line_containing(output, hint) if hint else ''
"""
NEW_STRIP = """        verdict = line_containing(output, hint) if hint else ''
        # The row already carries the label; a verdict that opens by
        # repeating the hint spends the column on it twice. Stripped only
        # when the hint is a genuine prefix, so a hint matched mid-line
        # (the scanner's 'TIER-1 FINDINGS') is left exactly as printed.
        if hint and verdict.startswith(hint):
            verdict = verdict[len(hint):].strip()
"""

OLD_ROW = ("    ('Reset completeness', "
           "['test_reset_completeness.py'], None),\n")
NEW_ROW = ("    ('Reset completeness', ['test_reset_completeness.py'],\n"
           "     'RESET COMPLETENESS:'),\n")

EDITS = {
    'maintenance_run.py': {
        'fp': 'b5b105da3e3d3f984d4387ea3bc0330e',
        'edits': [
            (OLD_ROW, NEW_ROW),
            (OLD_STRIP, NEW_STRIP),
        ],
    },
    'test_reset_completeness.py': {
        'fp': '70236cbdbdd57c48d1f61dd5b2cee805',
        'edits': [
            (OLD_PASS, NEW_PASS),
            (OLD_FAIL, NEW_FAIL),
        ],
    },
}


def normalized(data):
    return data.replace(b'\r\n', b'\n')


def non_ascii_count(data):
    return sum(1 for byte in data if byte > 127)


def main():
    if not os.path.isfile('test_reset_completeness.py'):
        print('ERROR: run this from the palomas_orrery repo root '
              '(the folder holding test_reset_completeness.py).')
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
            print('       Nothing written. If this patch has already run, '
                  'that is the expected abort -- it is one-shot.')
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
    print('Next: run maintenance_run.py -- the Reset completeness row '
          'should name the vars it checked.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
