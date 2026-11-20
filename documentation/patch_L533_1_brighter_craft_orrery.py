"""
patch_L533_1_brighter_craft_orrery.py -- brighter ESCAPADE craft (L-533)

Built on 78fc16e1 at https://github.com/tonylquintanilla/palomas_orrery (branch main).
L-533 (ESCAPADE's path), Tony's ruling of 2026-11-20, 08:34 Chicago, for
the ESCAPADE reel: "brighter colors, teal instead of blue, maybe thicker
lines for space craft symbols" -- then "Yes" to turquoise for
ESCAPADE-Blue in both repositories, ESCAPADE-Gold kept, and a 2-pixel
outline on every spacecraft's open diamond on the website.

RUN COMMAND
    Save this file in the orrery (palomas_orrery_for_github) folder, open it in VS Code and click
    Run:

        python patch_L533_1_brighter_craft_orrery.py

    Success: one "ok" line per edit, then "patch applied".
    Failure: an "ERROR:" or "ANCHOR FAIL" line, and NOTHING is written.
    Undo after a success: Discard Changes in GitHub Desktop.
    Once it has run, move it to the documentation folder.

What it changes:
    orrery_colors.py: ESCAPADE-Blue drawn turquoise, not blue; Gold kept.

Written November 20, 2026 with Anthropic's Claude Opus 5.5.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

EDITS = [('orrery_colors.py',
  'they show, the two L3 lines gone, as JPL has no L3, L-297.)\n',
  'they show, the two L3 lines gone, as JPL has no L3, L-297.)\n'
  "Module updated: November 20, 2026 with Anthropic's Claude Opus 5.5 "
  '(L-533,\n'
  "the ESCAPADE reel: ESCAPADE-Blue turquoise, the website's too, by "
  "Tony's\n"
  'ruling of 2026-11-20; ESCAPADE-Gold kept.)\n'),
 ('orrery_colors.py',
  "        'ESCAPADE-Blue': 'blue',   # ESCAPADE: placeholder, Tony's eye\n"
  "        'ESCAPADE-Gold': 'gold',   # ESCAPADE: placeholder, Tony's "
  'eye\n',
  "        'ESCAPADE-Blue': 'turquoise',   # Tony, 2026-11-20: teal, "
  'brighter than blue\n'
  "        'ESCAPADE-Gold': 'gold',   # Tony, 2026-11-20: kept\n")]


def main():
    staged = {}
    for name, old, new in EDITS:
        path = os.path.join(HERE, name)
        if not os.path.exists(path):
            print("ERROR: %s not found next to this script. Is it in the "
                  "orrery (palomas_orrery_for_github) folder? NOTHING was written." % name)
            sys.exit(1)
        if name not in staged:
            with open(path, 'rb') as f:
                raw = f.read()
            staged[name] = [raw.replace(b'\r\n', b'\n'), b'\r\n' in raw]
        text = staged[name][0]
        o, n = old.encode('ascii'), new.encode('ascii')
        if text.count(n) == 1 and text.count(o) == 0:
            print("ERROR: %s already holds this change (has the patch run "
                  "before?). NOTHING was written." % name)
            sys.exit(1)
        c = text.count(o)
        if c != 1:
            print("ANCHOR FAIL: %s, expected 1 match, found %d: %r\n"
                  "NOTHING was written." % (name, c, old[:70]))
            sys.exit(1)
        staged[name][0] = text.replace(o, n)
        print("ok   %s: %s" % (name, old.strip().splitlines()[0][:60]))
    for name, (text, was_crlf) in staged.items():
        with open(os.path.join(HERE, name), 'wb') as f:
            f.write(text)
        if was_crlf:
            print("note: %s was CRLF in the working copy; written LF" % name)
    print("patch applied (%d edits, %d files)" % (len(EDITS), len(staged)))


if __name__ == '__main__':
    main()
