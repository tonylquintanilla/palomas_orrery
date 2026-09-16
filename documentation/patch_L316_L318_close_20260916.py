#!/usr/bin/env python3
"""
patch_L316_L318_close_20260916.py -- ORRERY repo, LEDGER_CONSOLIDATED.md only.

Run: save this file in the ORRERY repo root (next to LEDGER_CONSOLIDATED.md),
open it in VS Code and click Run.  Or:  python patch_L316_L318_close_20260916.py
Then:  python ledger_index.py LEDGER_CONSOLIDATED.md  TWICE
       (the first run prints four [auto-fix] lines while it files the two
       closed items into section C; the second prints OK: 329 blocks)

Built on orrery 85c308cfbb773782901ff94d00f9cd0638082e06
at https://github.com/tonylquintanilla/palomas_orrery
(gallery at 72a49552aa6ba4b21c2f58e3c5fe53f7d198590c
at https://github.com/tonylquintanilla/tonyquintanilla.github.io).

WHAT IT DOES, all on Tony's rulings of 2026-09-16, evening:
  - L-316 CLOSED ("done. just needs updating").
  - L-318 CLOSED ("done. just needs updating").
  - L-334: question 1 ruled -- the editor does not change numbers
    ("yes. L-334."); questions 2 to 5 are settled at the start of the
    build session.
  - L-322 and L-334: the order recorded where the next session reads it.
    Tony: L-322 "might be priority 1 actually. get the number right
    first." Then the editor. L-333 waits ("the master plan is the
    critical one"). Jupiter's room behind all of it.

FAILURE: a single ERROR: or ANCHOR FAIL line, and NOTHING is written.
Undo is Discard Changes in GitHub Desktop.
"""
import hashlib
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
TARGET = 'LEDGER_CONSOLIDATED.md'
EXPECTED = '66b09137032d26c28d504ff8fc75eb16'
ZONE = (b'<!-- INDEX:START', b'<!-- INDEX:END -->')

EDITS = [

(b"""exhibits' served store), built on bfc1706b.
Review and RICE update Tony 6-21-2026
""",
b"""exhibits' served store), built on bfc1706b.
Module updated: September 16, 2026 with Anthropic's Claude Opus 5
(L-316 and L-318 closed on Tony's word; L-334 question 1 ruled, numbers
locked; the order for the next sessions recorded on L-322 and L-334:
L-322 first, then the editor), built on 85c308cf.
Review and RICE update Tony 6-21-2026
"""),

# ---- L-316 close
(b"""<!-- L:316 status:OPEN upd:2026-09-16 section:A flag: rice:3/2/80/1 -->
""",
b"""<!-- L:316 status:DONE upd:2026-09-16 section:A flag: rice:3/2/80/1 -->
"""),
(b"""**Gap:** desktop, not yet looked at on its own: title and cross exactly as
before -- this also covers L-310's desktop check. The 2026-09-16 look
covered the desktop's mouse hover, not the title and the cross.
  **Tony-action (decide):** after that look, close L-316.
""",
b"""- **CLOSED 2026-09-16, Tony's ruling:** "done. just needs updating."
  Four rounds on the phone, the cross back at the top right since round
  4 in the corner one CSS rule names, and both rooms passed on
  2026-09-16 with the cross in place. The desktop title-and-cross look
  the Gap asked for is folded into the ordinary desktop Mode 5 that
  every room build runs; nothing here waits on it. The chrome as it
  stands is in interactive-exhibit 1.3 (L-332).
"""),

# ---- L-318 close
(b"""<!-- L:318 status:OPEN upd:2026-09-16 section:A flag: rice:3/2/70/2 -->
""",
b"""<!-- L:318 status:DONE upd:2026-09-16 section:A flag: rice:3/2/70/2 -->
"""),
(b"""**Gap:** none left here once L-331 and L-332 carry the two loose ends.
  **Tony-action (decide):** close L-318.
""",
b"""- **CLOSED 2026-09-16, Tony's ruling:** "done. just needs updating."
  Six rounds on the phone; the two loose ends live where the Gap said
  they would -- the hover wording and the ceiling on L-331, the skill
  on L-332 (1.3 shipped). Tony's Mode 5 of both rooms at gallery
  `bbf46429`, with the drawer, the text box and the tap as this item
  left them: "correct."
"""),

# ---- L-334 question 1 ruled, order recorded
(b"""**Gap:** the five design questions above, in conversation; then the
build, in this order: the arrival block and its page reader (3), the
editor over prose and links (1, 2, 5), the measure and the checks
button (4).
  **Tony-action (decide):** the five questions, starting with 1 --
  whether numbers are locked.
""",
b"""- **Question 1 RULED, Tony, 2026-09-16:** yes, numbers are locked.
  Values, units and `orrery_constant` pointers are displayed and not
  editable; a number changes in the orrery and comes through the
  pipeline. Words, links and the arrival settings are the editor's.
  Questions 2 to 5 are settled at the start of the build session, on
  Tony's word, before any code.
- **Order, Tony, 2026-09-16:** L-322 comes FIRST -- "get the number right
  first" -- because the editor's locked numbers show what Store drift
  reads, and 13 of its 70 pointers cannot be examined until the unit
  field lands. Then this item. L-333 waits; Jupiter's room behind all
  of it. The next session starts fresh on L-322's design round.
**Gap:** L-322 first; then questions 2 to 5 in conversation; then the
build, in this order: the arrival block and its page reader (3), the
editor over prose and links (2, 5), the measure and the checks button
(4).
  **Tony-action (decide):** questions 2 to 5, at the start of the build
  session.
"""),

# ---- L-322 priority
(b"""**Tony-action (decide) 2026-09-14: (d) is prioritised** within the item.
It is unruled, so the first session on this item is a design round
settling (a) through (e), not a patch.
""",
b"""**Tony-action (decide) 2026-09-14: (d) is prioritised** within the item.
It is unruled, so the first session on this item is a design round
settling (a) through (e), not a patch.
**Tony, 2026-09-16: this item is priority 1** -- "get the number right
first" -- ahead of L-334, the exhibits' store editor, whose locked
numbers would display what this item makes checkable. At gallery
`72a49552` against orrery `85c308cf` the live run still reads 70
pointers, 56 match, 0 drift, 1 unit mismatch, 13 not examined: the same
13 named in ruling 3's (a), plus the six magnetosphere and belt-edge
constants whose names declare no unit. The next session opens here,
with the design round, fresh.
"""),
]


def main():
    path = os.path.join(ROOT, TARGET)
    if not os.path.exists(path):
        print(f'ERROR: {TARGET} not found next to this script. NOTHING was written.')
        return 1
    raw = open(path, 'rb').read()
    was_crlf = b'\r\n' in raw
    content = raw.replace(b'\r\n', b'\n')
    a = content.index(ZONE[0])
    b = content.index(ZONE[1]) + len(ZONE[1])
    actual = hashlib.md5(content[:a] + content[b:]).hexdigest()
    if actual != EXPECTED:
        print(f'ERROR: {TARGET} is not the file this patch was built against')
        print(f'       expected {EXPECTED}, found {actual}{" [CRLF]" if was_crlf else ""}')
        print('       (the INDEX zone is excluded from this comparison)')
        print('       NOTHING was written. Undo is Discard Changes in GitHub Desktop.')
        return 1
    new = content
    for old, repl in EDITS:
        n = new.count(old)
        if n != 1:
            print(f'ANCHOR FAIL: expected 1 match, found {n}: {old[:70]!r}')
            print('NOTHING was written. Undo is Discard Changes in GitHub Desktop.')
            return 1
        new = new.replace(old, repl)
    if any(c > 127 for c in new):
        print('ERROR: the result would hold non-ASCII bytes. NOTHING was written.')
        return 1
    out = new.replace(b'\n', b'\r\n') if was_crlf else new
    with open(path, 'wb') as f:
        f.write(out)
    print(f'ok  {TARGET}  ({len(out)} bytes{", CRLF preserved" if was_crlf else ""})')
    print('closed: L-316, L-318;  L-334 question 1 ruled;  order recorded on L-322 and L-334')
    print('patch applied. NEXT: python ledger_index.py LEDGER_CONSOLIDATED.md TWICE '
          '(first run files the two closed items; second run: OK: 329 blocks)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
