"""Correct two statements that are not true.

Both were written yesterday by me and both assert something the corpus
contradicts.

1. LEDGER_CONSOLIDATED.md, L-193, says zero live claims sit on a
   qualified YES. There are three. The figure came from grepping
   WORKSHEET_CHECK.md, which lists routed findings only, and
   QUALIFIED_PASS is recorded without a route. So the grep was
   answering a different question than the one asked of it -- a green
   result that could not have shown the three.

2. worksheet_checker.py describes a compound clearing verdict as
   "confirmed with a reservation". Two of the three are reservations
   ("YES -- but see F2"). The third is "YES -- fully confirmed", which
   is emphasis, not a reservation. The message asserts a reading of
   prose the tool is not entitled to read -- the same shape as the
   "wrong authority" sentence removed the same day, one layer smaller.
   It now says the cell carries more than the token and leaves the
   reading to whoever opens it.

Two files, two edits, each asserting exactly one match before anything
is written. Both are planned before either is written. Line endings are
read from each file and preserved, so the ledger's CRLF stays CRLF.

Run it from the repo root with the Run button, then run
ledger_index.py and maintenance_run.py.

Written August 2026 with Anthropic's Claude Opus 5 (L-193).
"""

import hashlib
import os
import sys

OLD_LEDGER = """  clean. Zero live claims currently sit on a qualified YES, which is
  why the guard has a unit test rather than a corpus pin.
"""

NEW_LEDGER = """  clean. THREE live claims sit on a qualified YES: MOON_RADIUS_KM,
  and the pluto_hill_sphere_info / description pair that is also the
  614/638 merge candidate. The entry first said zero, from a grep of
  WORKSHEET_CHECK.md -- which lists routed findings, and this one is
  recorded without a route. The grep answered a question nobody asked
  and returned a clean-looking number for it.
- **One of the three is a false positive, and it is kept.** "YES --
  fully confirmed" is compound in structure and emphatic in meaning,
  not qualified. The guard cannot tell those apart without reading
  prose, which it is forbidden to do, so it flags the shape and a
  person reads the words. One unnecessary look per two real catches is
  the right side to err on; the wrong side is silent.
"""

OLD_CODE = """                       '%s reads %s -- confirmed with a reservation%s'
"""

NEW_CODE = """                       '%s reads %s -- a pass carrying more than its '
                       'token; read the cell%s'
"""

JOBS = [
    ('LEDGER_CONSOLIDATED.md', OLD_LEDGER, NEW_LEDGER),
    ('worksheet_checker.py', OLD_CODE, NEW_CODE),
]


def dominant_eol(raw):
    """The line ending this file already uses, as text."""
    return '\r\n' if raw.count(b'\r\n') else '\n'


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    os.chdir(root)

    for name, _old, _new in JOBS:
        if not os.path.exists(name):
            print('ABORT: %s not found. Run this from the repo root.' % name)
            return 1

    planned = []
    for name, old, new in JOBS:
        with open(name, 'rb') as handle:
            raw = handle.read()
        text = raw.decode('utf-8')
        eol = dominant_eol(raw)
        want_new = new.replace('\n', eol)
        want_old = old.replace('\n', eol)

        if want_new in text:
            planned.append((name, 'already', None, eol))
            continue

        count = text.count(want_old)
        if count != 1:
            print('ABORT: %s matched the old text %d times, expected 1.'
                  % (name, count))
            print('Line endings read as %s.'
                  % ('CRLF' if eol == '\r\n' else 'LF'))
            print('Nothing was written, in either file.')
            return 1
        planned.append((name, 'apply', text.replace(want_old, want_new), eol))

    for name, action, payload, eol in planned:
        label = 'CRLF' if eol == '\r\n' else 'LF'
        if action == 'already':
            print('  already   %s (%s)' % (name, label))
            continue
        with open(name, 'wb') as handle:
            handle.write(payload.encode('utf-8'))
        with open(name, 'rb') as handle:
            digest = hashlib.md5(handle.read()).hexdigest()
        print('  corrected %s (%s endings preserved)  -> %s'
              % (name, label, digest))

    if all(action == 'already' for _n, action, _p, _e in planned):
        print('Nothing to do. Both corrections are already in place.')
        return 0

    print()
    print('Done. Next: ledger_index.py, then maintenance_run.py.')
    print('Worksheet checker tests should still read 61 passed.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
