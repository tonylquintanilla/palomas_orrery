"""patch_L196_11_orbit_cache_verdict.py -- give test_orbit_cache.py a
closing line that says whether it passed.

RUN COMMAND
-----------
Save this file into the palomas_orrery repo root (the same folder as
test_orbit_cache.py), open it in VS Code, and click Run.

    python patch_L196_11_orbit_cache_verdict.py

BASE
----
Built on the tree AFTER patch_L196_9 and patch_L196_10 have run. The
file this patch edits is untouched by either, so the fingerprint below
matches repo HEAD 5840145 as well; the ordering note is about the
maintenance output you will be reading afterwards, not about the bytes.

WHAT WAS WRONG
--------------
The file ended in unittest.main(), which writes its verdict -- OK, or
FAILED with a count -- to STDERR. maintenance_run.py reads STDOUT and
takes the last non-blank line as the verdict. The last thing this file
put on stdout was a print inside tearDown that fires once per test:

    Test files saved in: C:\\...\\test_output

So the Orbit cache row has been reporting a directory path as its
verdict since the runner was built. It went green whether or not
anything passed, because a path prints either way. That is the shape
the resident protocol calls a check that cannot fail.

WHAT IT DOES
------------
Runs the suite explicitly, reads the result object, and closes on a
sentence naming what passing means:

    All 6 orbit cache tests passed: cache loads, old formats convert,
    corrupted entries are dropped.

On failure it prints the count and exits 1. That exit code is the part
worth being careful about -- unittest.main() sets it for free, and a
hand-rolled runner that forgets it would leave the row permanently
green, which is the same defect one layer down. The failure path is
mutation-tested before delivery.

The per-test tearDown print stays. It is useful when inspecting the
output directory, and it is no longer the last line.

PERMANENT vs DISPOSABLE
-----------------------
This script is disposable and one-shot. What it installs is permanent:
the explicit runner, the verdict line, and the non-zero exit on
failure.

SAFETY
------
All-or-nothing, fingerprinted (CRLF-normalized), one anchor, exact
match required. Any mismatch aborts with nothing written. The file's
own line endings are preserved.

Success: one 'ok' line, then 'patch applied (N bytes)'.
Failure: a single 'ERROR:' or 'ANCHOR FAIL' line; nothing is written.
"""

import hashlib
import os
import sys


OLD_TAIL = '''if __name__ == "__main__":
    print(f"Test output will be created in: ./test_output/")
    print("Running tests in isolated environment...")
    
    # Create test output directory if it doesn't exist
    test_output_dir = os.path.join(os.path.dirname(__file__), "test_output")
    if not os.path.exists(test_output_dir):
        os.makedirs(test_output_dir)
        print(f"Created test output directory: {test_output_dir}")
    
    # Run tests
    unittest.main()
'''

NEW_TAIL = '''def main():
    """Run the suite and close on a verdict, not on a directory path.

    unittest.main() writes OK / FAILED to stderr, and maintenance_run.py
    reads the last line of stdout. That left the Orbit cache row quoting
    the tearDown print -- a path, which appears whether the tests passed
    or not. Running the suite here lets the result be read and stated.
    """
    print("Test output will be created in: ./test_output/")
    print("Running tests in isolated environment...")

    test_output_dir = os.path.join(os.path.dirname(__file__), "test_output")
    if not os.path.exists(test_output_dir):
        os.makedirs(test_output_dir)
        print("Created test output directory: %s" % test_output_dir)

    suite = unittest.TestLoader().loadTestsFromTestCase(TestOrbitCache)
    result = unittest.TextTestRunner(verbosity=2).run(suite)

    total = result.testsRun
    bad = len(result.failures) + len(result.errors)
    if bad:
        # Non-zero exit is what maintenance_run.py reads. unittest.main()
        # set it for free; forgetting it here would leave this row green
        # forever, which is the defect this patch exists to remove.
        print("\\n%d of %d orbit cache tests FAILED." % (bad, total))
        return 1
    print("\\nAll %d orbit cache tests passed: cache loads, old formats "
          "convert, corrupted entries are dropped." % total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
'''

EDITS = {
    'test_orbit_cache.py': {
        'fp': 'd5992fde679726d9e4941a229d3be247',
        'edits': [
            (OLD_TAIL, NEW_TAIL),
        ],
    },
}


def normalized(data):
    return data.replace(b'\r\n', b'\n')


def non_ascii_count(data):
    return sum(1 for byte in data if byte > 127)


def main():
    if not os.path.isfile('test_orbit_cache.py'):
        print('ERROR: run this from the palomas_orrery repo root '
              '(the folder holding test_orbit_cache.py).')
        return 1

    staged = []
    total = 0
    notes = []

    for name in sorted(EDITS):
        spec = EDITS[name]
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
    print('Next: run maintenance_run.py -- the Orbit cache row should now '
          'name what passed.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
