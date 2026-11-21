"""
patch_L540_2_outside_link_card.py -- a lobby card that links to another website (L-540)

Built on aba9df72 at https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch main).
L-540 (a reel on a Featured card), Tony's rulings of 2026-11-20: 12:50,
"Alternatively I could post the Instagram reel in Featured as a link",
and 13:01, "That would be ideal", to the reel's link and ESCAPADE's
scene side by side in Featured.

RUN COMMAND
    Save this file in the website (tonyquintanilla.github.io) folder, open it in VS Code and click
    Run:

        python patch_L540_2_outside_link_card.py

    Success: one "ok" line per edit, then "patch applied".
    Failure: an "ERROR:" or "ANCHOR FAIL" line, and NOTHING is written.
    Undo after a success: Discard Changes in GitHub Desktop.
    Once it has run, move it to the documentation folder.

What it changes:
    index.html: a card whose "live" address is another website's opens
        it in a new tab and carries no "Interactive" label. The page
        reads it live, so it shows as soon as the push is served.

Written November 20, 2026 with Anthropic's Claude Opus 5.5.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

EDITS = [('index.html',
  '         download and no iPhone download tips; a .kmz still downloads\n'
  '         from gallery/assets/. -->\n',
  '         download and no iPhone download tips; a .kmz still downloads\n'
  '         from gallery/assets/.\n'
  "     Updated: November 20, 2026 with Anthropic's Claude Opus 5.5 "
  '(L-540,\n'
  '       a reel on a Featured card)\n'
  '       - A card whose "live" address is another website\'s '
  "(ESCAPADE's\n"
  '         reel on Instagram) is read as a page card: no "Interactive"\n'
  '         label, and a tap opens it in a new tab, so the lobby stays\n'
  "         where it was. Tony's ruling of 2026-11-20: the reel's link "
  'and\n'
  "         ESCAPADE's scene side by side in Featured. -->\n"),
 ('index.html',
  '            for (var i = 0; i < vizs.length; i++) {\n'
  '                vizLookup[vizs[i].id] = vizs[i];\n'
  '            }\n',
  '            for (var i = 0; i < vizs.length; i++) {\n'
  "                // L-540: a card whose address is another website's (a "
  'reel\n'
  '                // on Instagram) is a page, not a room: no '
  '"Interactive"\n'
  '                // label, and it opens in a new tab '
  '(loadVisualization).\n'
  "                if (/^https?:\\/\\//i.test(vizs[i].live || '')) {\n"
  '                    vizs[i].page = true;\n'
  '                    vizs[i].outside = true;\n'
  '                }\n'
  '                vizLookup[vizs[i].id] = vizs[i];\n'
  '            }\n'),
 ('index.html',
  '            if (viz.live) {                 // a live card opens its '
  'scene (L-287)\n'
  '                window.location.href = viz.live;\n',
  '            if (viz.live) {                 // a live card opens its '
  'scene (L-287)\n'
  "                if (viz.outside) {          // another website's page: "
  'a new tab (L-540)\n'
  "                    window.open(viz.live, '_blank', 'noopener');\n"
  '                    return;\n'
  '                }\n'
  '                window.location.href = viz.live;\n')]


def main():
    staged = {}
    for name, old, new in EDITS:
        path = os.path.join(HERE, name)
        if not os.path.exists(path):
            print("ERROR: %s not found next to this script. Is it in the "
                  "website (tonyquintanilla.github.io) folder? NOTHING was written." % name)
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
