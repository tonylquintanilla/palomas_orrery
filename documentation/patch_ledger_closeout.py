# -*- coding: utf-8 -*-
"""patch_ledger_closeout.py -- close L-178 and L-182 at the pushed SHA,
and record the L-176 scope boundary.

Built on 06daa8b825c93d8968a46a1edb2f5083610ef665
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

HOW TO RUN
    Save in the REPO ROOT, open in VS Code, click Run.
    CRLF is normalized automatically. On any failure nothing is
    written and the script says so plainly.

AFTER RUNNING: run ledger_index.py -- it migrates the two closed items
    into section C and regenerates the index.
"""

import os
import sys

TARGET = 'LEDGER_CONSOLIDATED.md'
ENCODING_GATE = 'utf-8'

EDITS = [
    ('CLOSE-4', 'L-182 Gap -> closed, record pushed SHA',
     b"**Gap:** Patches built and smoke-tested (render moves 1,102,067 km ->\n1,084,067 km). Awaiting Tony's run and push; close on SHA record.",
     b'**Closed 2026-08-05 at `06daa8b825c93d8968a46a1edb2f5083610ef665`.** Both\npatches run and pushed; Mode 5 confirmed by Tony -- the Mars Hill shell is\nvisibly smaller and the hover reads 1.08 Mkm. Every live and dead copy now\nreads 319.2 R_Mars. [verified @06daa8b]'),
    ('CLOSE-3', 'L-182 -> DONE, section C',
     b'<!-- L:182 status:PENDING-GATE upd:2026-08-05 section:A flag: rice:3/4/100/1 -->',
     b'<!-- L:182 status:DONE upd:2026-08-05 section:C flag: rice:3/4/100/1 -->'),
    ('CLOSE-2', 'L-178 Gap -> closed, record pushed SHA',
     b"**Gap:** Patch built and smoke-tested; awaiting Tony's run and push.",
     b'**Closed 2026-08-05 at `06daa8b825c93d8968a46a1edb2f5083610ef665`.** Patch\nrun and pushed; Mode 5 confirmed by Tony -- GEO hover reads 42,164 km /\n0.000282 AU and the LEO band sits on its declared 200/2000 km altitude\nbounds. Shadow constants removed; mean-vs-equatorial no longer arises here.\n[verified @06daa8b]'),
    ('CLOSE-1', 'L-178 -> DONE, section C',
     b'<!-- L:178 status:PENDING-GATE upd:2026-08-05 section:A flag: rice:3/3/40/2 -->',
     b'<!-- L:178 status:DONE upd:2026-08-05 section:C flag: rice:3/3/40/2 -->'),
    ('CLOSE-0', 'L-176 scope-boundary note',
     b'**Gap:** Design the text format, decide whether to include the physical\nvalue alongside the illustrated value for stylized shells. Build after\nL-181 constant layer or in parallel.',
     b"**Note (2026-08-05):** Scope boundary, so the item is not oversold later.\nIllustrated dimensions catch CONSTANT-VS-TEXT drift -- the Batch 1 class,\nwhere Mercury's rf 0.85 drew 2,074 km under text claiming 2,020. They do\nNOT catch a value that is internally consistent but unsourced: Mars's Hill\nsphere drew exactly the 324.5 R_Mars its text claimed, and both were wrong\n(L-182). Drift is visible in the render; wrong-but-consistent needs the\nprovenance cross-check. The two mechanisms are complementary, not\nsubstitutes.\n**Gap:** Design the text format, decide whether to include the physical\nvalue alongside the illustrated value for stylized shells. Build after\nL-181 constant layer or in parallel."),
]


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(root, TARGET)
    if not os.path.exists(path):
        print("ERROR: %s not found. Save this in the repo root." % TARGET)
        print("       NOTHING WAS WRITTEN.")
        return 1
    with open(path, 'rb') as f:
        data = f.read()
    norm = 0
    if b'\r\n' in data:
        norm = data.count(b'\r\n')
        data = data.replace(b'\r\n', b'\n')
        print("fix CRLF     %s: normalized %d line endings to LF" % (TARGET, norm))

    for eid, label, old, new in EDITS:
        c = data.count(old)
        if c != 1:
            print("ANCHOR FAIL: %s (%s) matched %d, expected 1." % (eid, label, c))
            print("             NOTHING WAS WRITTEN. The file is unchanged.")
            print("             Fix the cause, then RE-RUN this script.")
            return 1
    for eid, label, old, new in EDITS:
        data = data.replace(old, new, 1)
        print("ok  %-10s %s" % (eid, label))
    try:
        data.decode(ENCODING_GATE)
    except UnicodeDecodeError as exc:
        print("ERROR: result not valid UTF-8 (%s). NOTHING WAS WRITTEN." % exc)
        return 1
    with open(path, 'wb') as f:
        f.write(data)
    print("")
    print("patch applied%s" % (" (+%d CRLF normalized)" % norm if norm else ""))
    return 0


if __name__ == '__main__':
    sys.exit(main())
