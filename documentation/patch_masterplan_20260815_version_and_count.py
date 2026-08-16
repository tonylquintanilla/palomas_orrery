"""
patch_masterplan_20260815_version_and_count.py

Corrects two stale facts in the master plan and its readable summary,
both verified against repo HEAD 253bcdd on 2026-08-15:

  1. provenance-discipline is at v2.3, not v2.1.
  2. maintenance_run.py runs four generators and TWELVE checkers,
     not eight. (GENERATORS has 4 entries, CHECKERS has 12.)

Also adds one dated correction note to the SUMMARY only, because that
document carries a top-level "Built on 00219d9" anchor and would
otherwise hold two facts from a later commit under it. The plan has no
top-level anchor, so it gets the two factual edits and nothing else.
Delete edits marked [NOTE] below if you would rather not have it.

Deliberately NOT changed: "about 40 seconds" in both documents. Four
checkers were added since that was measured, so the number is now
unverified rather than known-wrong. Run maintenance_run.py to get the
real figure.

Run:
    Save into the palomas_orrery repo root, open in VS Code, click Run.
    Or: python patch_masterplan_20260815_version_and_count.py

Success: one "ok" line per edit, then "patch applied" per file.
Failure: a single ERROR or ANCHOR FAIL line; nothing is written.

Written August 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

SUMMARY = os.path.join('documentation',
                       'MASTER_PLAN_INTERACTIVE_GALLERY_SUMMARY.md')
PLAN = os.path.join('documentation', 'MASTER_PLAN_INTERACTIVE_GALLERY.md')

# Content fingerprints at 253bcdd, CRLF-normalized before hashing.
BASE = {
    SUMMARY: '2fec4af7617b17c3b0d7213bf7ba5c8b',
    PLAN: '621ce923c3e916ce2b89a07ee60f4945',
}

NOTE = (
    b'https://github.com/tonylquintanilla/tonyquintanilla.github.io.\n'
    b'\n'
    b'Two facts were refreshed 2026-08-15 at 253bcdd: the\n'
    b'provenance-discipline version and the maintenance_run.py checker\n'
    b'count. Everything else here still describes 00219d9 -- notably\n'
    b"L-192's status, which has moved.\n"
)

# (path, [(old, new, label)]) -- bottom-up within each file.
EDITS = [
    (SUMMARY, [
        (b'and eight checkers in one command',
         b'and twelve checkers in one command',
         'summary ~460  checker count 8 -> 12'),
        (b'provenance-discipline is at v2.1.',
         b'provenance-discipline is at v2.3.',
         'summary ~438  skill version 2.1 -> 2.3'),
        (b'https://github.com/tonylquintanilla/tonyquintanilla.github.io.\n',
         NOTE,
         'summary ~7    [NOTE] dated correction under the anchor'),
    ]),
    (PLAN, [
        (b'provenance-discipline v2.1.',
         b'provenance-discipline v2.3.',
         'plan ~1953    skill version 2.1 -> 2.3'),
        (b'four generators and eight\n  checkers',
         b'four generators and twelve\n  checkers',
         'plan ~1880    checker count 8 -> 12'),
    ]),
]


def fingerprint(data):
    return hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()


def main():
    staged = []

    for path, edits in EDITS:
        if not os.path.exists(path):
            print('ERROR: not found: %s' % path)
            print('       run this from the palomas_orrery repo root.')
            return 1

        with open(path, 'rb') as handle:
            data = handle.read()

        got = fingerprint(data)
        if got != BASE[path]:
            print('ERROR: base moved: %s' % path)
            print('       expected %s' % BASE[path])
            print('       found    %s' % got)
            print('       nothing written. Re-pull or re-anchor.')
            return 1

        crlf = data.count(b'\r\n') > 0
        for old, new, label in edits:
            if crlf:
                old = old.replace(b'\n', b'\r\n')
                new = new.replace(b'\n', b'\r\n')
            count = data.count(old)
            if count != 1:
                print('ANCHOR FAIL (%d matches): %s' % (count, label))
                print('       nothing written.')
                return 1
            data = data.replace(old, new)
            print('  ok  %s' % label)

        staged.append((path, data))

    for path, data in staged:
        with open(path, 'wb') as handle:
            handle.write(data)
        print('patch applied: %s (%d bytes)' % (path, len(data)))

    return 0


if __name__ == '__main__':
    sys.exit(main())
