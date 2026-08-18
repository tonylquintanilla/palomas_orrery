"""patch_L188_2_verdict_lines_carry_counts.py -- L-188.

RUN COMMAND
-----------
Save this file into the palomas_orrery repo root (the same folder as
maintenance_run.py), open it in VS Code, and click Run.

    python patch_L188_2_verdict_lines_carry_counts.py

Success prints one `ok` line per file and then `patch applied`. Failure
prints a single ERROR or ANCHOR FAIL line and writes NOTHING.

WHAT IT DOES
------------
Four test files, one change each: the last line each one prints -- the
line the maintenance runner quotes as that tool's verdict -- now says
how many tests it ran.

THE DEFECT. Nine of the thirteen checker rows already carry evidence:
"All 6 orbit cache tests passed", "52 sites minted 52 distinct keys",
"68 of 110 routed". Four did not:

    Constants relations       All provenance tests passed. No constants
                              have drifted.
    Cross-check annotations   All cross-check annotation tests passed.
    Citation inheritance      All citation-inheritance tests passed.
    Scanner recognition 1d/1e Real citations recognized, fake ones
                              refused.

Each is a RESULT, not a statement of intent -- every one prints after
the failure branch has already returned 1, so none of them can appear
over a failing run. What none of them can do is move. The 1d/1e line
reads the same whether 27 tests ran or two, so it cannot tell you that
the suite shrank, and a suite that quietly shrinks is the check that
stops being able to fail.

Each file already computes the number and prints it two lines earlier
as "Results: N passed, 0 failed, N total". The evidence existed; it
just was not on the line the runner reads, because the runner quotes
the LAST non-blank line. This moves the count onto that line and keeps
the words that say what was checked -- a bare count would trade one
kind of blindness for another.

AFTER THE PATCH the four rows read:

    Constants relations       18 of 18 provenance tests passed against
                              constants_new.py. No constants have drifted.
    Cross-check annotations   19 of 19 cross-check annotation tests passed.
    Citation inheritance      20 of 20 citation-inheritance tests passed.
    Scanner recognition 1d/1e 27 of 27 recognition pins hold: real
                              citations recognized, fake ones refused.

FIXED IN PASSING, AND REPORTED
------------------------------
test_provenance_1d.py carried a comment saying the runner "trims it to
44 characters, so the verdict goes last and stays one short line."
Measured at HEAD, that is wrong: `print_row` calls `wrapped()`, whose
docstring says a verdict "does not get an ellipsis" and runs across as
many lines as it needs. 44 is the WRAP width, not a trim. The comment
would have discouraged exactly the edit this patch makes, so it is
corrected in the same edit rather than left to mislead the next reader.

WHAT IS PERMANENT AND WHAT IS NOT
---------------------------------
This script is disposable and one-shot. Permanent: the four verdict
lines and the corrected comment.

AFTER RUNNING
-------------
1. python maintenance_run.py     (four rows should now carry numbers)
2. Archive this script to documentation/. Until you do it sits in the
   repo root as a .py file and the scanner scores its FINGERPRINTS dict
   as one Tier-1 finding, which is why the count reads one above the
   codebase's own between running this and archiving it.

Module created: August 18, 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys


FINGERPRINTS = {
    'test_constants_provenance.py': 'ad99574d4251585cf6c4dc3519dda0f8',
    'test_cross_checked.py': '244d299d9c6d7593f6f6f6532d00249e',
    'test_citation_inheritance.py': '940bc7186e97424e11aae43a72f4a2f9',
    'test_provenance_1d.py': 'a991aacfa9e86f85cab74405c6ae8438',
}


PLAN = [
    ('test_constants_provenance.py', [
        ('''    print("\\nAll provenance tests passed. No constants have drifted.")
    return 0''',
         '''    # The runner quotes the LAST non-blank line as this tool's
    # verdict, so the count belongs here rather than only in the
    # Results line above. A verdict that cannot move cannot report a
    # suite that shrank.
    print(f"\\n{passed} of {len(tests)} provenance tests passed against "
          f"constants_new.py. No constants have drifted.")
    return 0'''),
    ]),

    ('test_cross_checked.py', [
        ('''    print("\\nAll cross-check annotation tests passed.")
    return 0''',
         '''    # The runner quotes the LAST non-blank line as this tool's
    # verdict, so the count belongs here rather than only in the
    # Results line above.
    print(f"\\n{passed} of {len(TESTS)} cross-check annotation tests "
          f"passed.")
    return 0'''),
    ]),

    ('test_citation_inheritance.py', [
        ('''    print("\\nAll citation-inheritance tests passed.")
    return 0''',
         '''    # The runner quotes the LAST non-blank line as this tool's
    # verdict, so the count belongs here rather than only in the
    # Results line above.
    print(f"\\n{passed} of {len(TESTS)} citation-inheritance tests "
          f"passed.")
    return 0'''),
    ]),

    ('test_provenance_1d.py', [
        ('''    # The runner quotes the LAST non-blank line and trims it to 44
    # characters, so the verdict goes last and stays one short line.
    print("\\nReal citations recognized, fake ones refused.")
    return 0''',
         '''    # The runner quotes the LAST non-blank line as this tool's
    # verdict, so it goes last and carries the count.
    #
    # It does NOT trim. An earlier version of this comment said the
    # runner cut the line at 44 characters; measured at HEAD, print_row
    # calls wrapped(), which runs a verdict across as many lines as it
    # needs and deliberately gives it no ellipsis. 44 is the wrap
    # width. The wrong version of this note would have argued against
    # adding the count, which is why it is corrected rather than left.
    print(f"\\n{passed} of {len(TESTS)} recognition pins hold: real "
          f"citations recognized, fake ones refused.")
    return 0'''),
    ]),
]


def fingerprint(data):
    """Content fingerprint: line endings normalized before hashing."""
    return hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()


def non_ascii(data):
    return [b for b in data if b > 127]


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    os.chdir(here)

    for name, _edits in PLAN:
        if not os.path.isfile(name):
            print('ERROR: %s not found. Run this from the repo root.' % name)
            return 1
        with open(name, 'rb') as handle:
            data = handle.read()
        seen = fingerprint(data)
        want = FINGERPRINTS[name]
        if seen != want:
            print('ERROR: %s has moved. Expected %s, found %s.'
                  % (name, want, seen))
            print('       Nothing written. Built against '
                  '24f445a7575b8599787d47ddee3472071fcfe373.')
            return 1

    staged = {}
    notes = []
    for name, edits in PLAN:
        with open(name, 'rb') as handle:
            data = handle.read()
        is_crlf = data.count(b'\r\n') > 0
        content = data
        for old, new in edits:
            old_b = old.encode('utf-8')
            new_b = new.encode('utf-8')
            if non_ascii(new_b):
                print('ERROR: this patch would insert non-ASCII bytes into '
                      '%s. Nothing written.' % name)
                return 1
            if is_crlf:
                old_b = old_b.replace(b'\n', b'\r\n')
                new_b = new_b.replace(b'\n', b'\r\n')
            count = content.count(old_b)
            if count != 1:
                print('ANCHOR FAIL: %s -- expected 1 match, found %d for:'
                      % (name, count))
                print('   %s' % old.splitlines()[0][:70])
                print('Nothing written.')
                return 1
            content = content.replace(old_b, new_b)
        left = non_ascii(content)
        if left:
            notes.append('note: %s still holds %d non-ASCII byte(s) this '
                         'patch did not reach' % (name, len(left)))
        staged[name] = content

    for name, edits in PLAN:
        with open(name, 'wb') as handle:
            handle.write(staged[name])
        print('ok  %s (%d edit)' % (name, len(edits)))

    for note in notes:
        print(note)
    print('patch applied (%d files)' % len(PLAN))
    print('')
    print('Next: python maintenance_run.py -- Constants relations,')
    print('      Cross-check annotations, Citation inheritance and')
    print('      Scanner recognition should each carry a count now.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
