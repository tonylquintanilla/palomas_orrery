"""
patch_L540_1_reel_card_record.py -- records the ESCAPADE reel's two
rulings in the ledger and on Where We Are.

Built on 5aa6a013 at https://github.com/tonylquintanilla/palomas_orrery
(branch main), with gallery aba9df72 read for what the website does today.

RUN COMMAND
    Save this file in the orrery folder (palomas_orrery_for_github),
    open it in VS Code and click Run:

        python patch_L540_1_reel_card_record.py

    Success: one "ok" line per edit, "patch applied", then ledger_index.py
    and the document-caps check run, each printing "ok".
    Failure: an "ERROR:" or "ANCHOR FAIL" line, and NOTHING is written.
    Undo after a success: Discard Changes in GitHub Desktop.
    Once it has run, move it to the documentation folder.

What it changes:
    LEDGER_CONSOLIDATED.md: a new item, L-540 (a reel on a Featured card,
        ending with a link into the room on its scene), Tony's idea of
        2026-11-20, 12:47, for a later build; and a note on L-533
        (ESCAPADE) recording the brighter craft, his ruling and his look.
    documentation/WHERE_WE_ARE.md: the header, the "Changed since" box,
        the attention marks reset, and one Deferred line for L-540 (two
        older Deferred lines joined, so the page stays at its 130-line
        cap). Each edit is anchored at its own lines, so your notes
        elsewhere are kept.

Written November 20, 2026 with Anthropic's Claude Opus 5.5.
"""

import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

EDITS = [('LEDGER_CONSOLIDATED.md',
  'horizons-orbital-mechanics, Checking an Entry Against JPL.\n'
  '\n'
  '#### [L-529]',
  'horizons-orbital-mechanics, Checking an Entry Against JPL.\n'
  '\n'
  '#### [L-540] A reel on a Featured card, ending with a link into the '
  'room on its scene (gallery; an idea, for a later build)\n'
  '<!-- L:540 status:OPEN upd:2026-11-20 section:A flag: rice: -->\n'
  "- **Tony, 2026-11-20, 12:47**, after ESCAPADE's reel was posted on\n"
  '  Instagram: "I would like to use the reel you made because it has a\n'
  "  story. That's where a featured card shines and the visitor can then\n"
  '  go to the interactive. Maybe at the end we can embed a link to a\n'
  '  scene? If this is for a future build we can just put it in the\n'
  '  ledger."\n'
  '- **What the website does today, read 2026-11-20 at gallery aba9df7:**\n'
  '  no lobby card plays a video (`index.html` draws a picture and a\n'
  '  link; it has no <video> and no .mp4). The room reads no address\n'
  '  option that picks which bodies are ticked: its options (?exhibit=,\n'
  '  ?edge=, ?axes=, ?tick=, ?ruler=, ?halo=) choose the room and the '
  'look\n'
  '  of its ticks and axes. So a card can open the Solar System room only\n'
  '  on its usual view.\n'
  '- **Two pieces, then.** (1) A Featured card that plays a reel. The\n'
  "  first is ESCAPADE's, `escapade_reel_draft5.mp4` (42 s, about 2.5 MB,\n"
  '  Tony has the file), cut on Nov 20 from his recording of the room,\n'
  '  its captions the approved words of\n'
  '  `documentation/WORDS_L533_escapade_20261118.md`. (2) An address\n'
  '  option that opens the room with named bodies ticked, here\n'
  '  ESCAPADE-Blue, ESCAPADE-Gold and Earth-Sun L2, which the card links\n'
  "  to at the reel's end.\n"
  '**Gap:** a design talk on the card (where the video is kept, whether '
  'it\n'
  'plays by itself, where the link sits), then a gallery build.\n'
  "**Ref:** L-533 (ESCAPADE); L-363 and L-428 (the lobby's wide card and\n"
  'start card); interactive-exhibit (what a room opens on); the reel rule\n'
  'of Nov 17 (L-060).\n'
  '\n'
  '#### [L-529]'),
 ('LEDGER_CONSOLIDATED.md',
  '<!-- L:533 status:OPEN upd:2026-11-19 section:A flag: rice: -->',
  '<!-- L:533 status:OPEN upd:2026-11-20 section:A flag: rice: -->'),
 ('LEDGER_CONSOLIDATED.md',
  "**Gap:** the row under Mars, by L-534's rule once it is designed. The\n",
  '**Note:** (2026-11-20, the coordinating session, Claude Opus 5.5)\n'
  'THE CRAFT DRAWN BRIGHTER, for ESCAPADE\'s reel. Tony, 08:15: "Why '
  "don't\n"
  'we try basic changes first like brighter colors, teal instead of blue,\n'
  'maybe thicker lines for space craft symbols"; then "Yes" to\n'
  'ESCAPADE-Blue turquoise in both repositories (the CSS colour teal is\n'
  "darker than blue), ESCAPADE-Gold kept, and every spacecraft's open\n"
  'diamond outlined 2 pixels in its own colour on the website\n'
  '(`render_spacecraft.MARKER_OUTLINE_PX`; comets unchanged). Built by\n'
  'patch_L533_1 and _2_brighter_craft, pushed at orrery 9591db8 and\n'
  'gallery eed30d4. Tony\'s phone look, 10:53: "Looks good." The reel was\n'
  'posted on Instagram the same day; a reel on a lobby card is L-540.\n'
  "**Gap:** the row under Mars, by L-534's rule once it is designed. "
  'The\n'),
 ('documentation/WHERE_WE_ARE.md',
  'Last updated: November 19, 2026, night: the Lagrange points live and '
  "looked at; this round's cleanup ruled (Opus, coordinating session).\n",
  "Last updated: November 20, 2026, noon: ESCAPADE's reel posted; its "
  'craft drawn brighter; a reel on a lobby card recorded (Opus, '
  'coordinating session).\n'),
 ('documentation/WHERE_WE_ARE.md',
  "- Written at orrery 1c0688ca and gallery 0c832de1, with this patch's "
  'edits on your disk.\n',
  "- Written at orrery 5aa6a013 and gallery aba9df72, with this patch's "
  'edits on your disk.\n'),
 ('documentation/WHERE_WE_ARE.md',
  '> - The eight Lagrange points are live on the website and in the '
  'orrery, and your phone look passed every line. L4 and L5 sit just off '
  "the Moon's drawn orbit by geometry: JPL puts them at the Moon's "
  'distance now, 60 degrees either side, and the orbit is an ellipse '
  '(L-297 (the Lagrange points), closed).\n'
  "> - The orrery's colours live in their own drawing file now, "
  '`orrery_colors.py`; three skills updated, the protocol at v3.143, the '
  'skills page at Plugins (L-432 (the default goldenrod), L-537 (the '
  'skills page), closed).\n',
  "> - ESCAPADE's reel is posted. For it the craft are drawn brighter on "
  "both sites: ESCAPADE-Blue is turquoise, and every spacecraft's diamond "
  'has a thicker outline (L-533 (ESCAPADE)).\n'
  '> - Your idea of the reel on a Featured card, ending with a link into '
  'the room showing the twins, is recorded for a later build (L-540 (a '
  'reel on a Featured card)).\n'),
 ('documentation/WHERE_WE_ARE.md',
  '               destinations and encounters talk (L-534, L-529), then '
  'Uranus and Neptune. Io, Titan, Charon and Pluto come to standard in '
  'their folds.* << moved this session\n',
  '               destinations and encounters talk (L-534, L-529), then '
  'Uranus and Neptune. Io, Titan, Charon and Pluto come to standard in '
  'their folds.*\n'),
 ('documentation/WHERE_WE_ARE.md',
  "  b.   [beside] This round's cleanup, each ruled Nov 19 (the order is "
  "yours): every path to its last day, L-533 (ESCAPADE); the orbiters' "
  "hourly points, L-538 (the orbiters' printed error); every entry checked "
  "against JPL, L-539 (every entry checked); the period's swing in its "
  "sentence, L-536 (a moon's yearly change); the 24 in goldenrod, L-432 "
  '(the default goldenrod), at your desk. << new this session\n',
  "  b.   [beside] This round's cleanup, each ruled Nov 19 (the order is "
  "yours): every path to its last day, L-533 (ESCAPADE); the orbiters' "
  "hourly points, L-538 (the orbiters' printed error); every entry checked "
  "against JPL, L-539 (every entry checked); the period's swing in its "
  "sentence, L-536 (a moon's yearly change); the 24 in goldenrod, L-432 "
  '(the default goldenrod), at your desk.\n'),
 ('documentation/WHERE_WE_ARE.md',
  '## Settled  **>> UPDATED THIS SESSION**\n',
  '## Settled\n'),
 ('documentation/WHERE_WE_ARE.md',
  '## Signals  **>> UPDATED THIS SESSION**\n',
  '## Signals\n'),
 ('documentation/WHERE_WE_ARE.md',
  '## Waiting on you  **>> UPDATED THIS SESSION**\n',
  '## Waiting on you\n'),
 ('documentation/WHERE_WE_ARE.md',
  '## Where the details are  **>> UPDATED THIS SESSION**\n',
  '## Where the details are\n'),
 ('documentation/WHERE_WE_ARE.md',
  '- L-511 (the export carries the words): behind the check (Nov 3).\n',
  '- A reel on a Featured card, ending with a link that opens the room on '
  'its bodies: a gallery build of its own (Nov 20; L-540 (a reel on a '
  'Featured card)).\n'),
 ('documentation/WHERE_WE_ARE.md',
  '- L-462 (a shorter run); L-128 (the ice lines); L-500 (eyeballed '
  'numbers).\n',
  '- L-462 (a shorter run); L-128 (the ice lines); L-500 (eyeballed '
  'numbers); L-511 (the export carries the words), behind the check (Nov '
  '3).\n')]


def main():
    staged = {}
    for name, old, new in EDITS:
        path = os.path.join(HERE, name)
        if not os.path.exists(path):
            print("ERROR: %s not found next to this script. Is it in the "
                  "orrery folder? NOTHING was written." % name)
            sys.exit(1)
        if name not in staged:
            with open(path, 'rb') as f:
                raw = f.read()
            staged[name] = [raw.replace(b'\r\n', b'\n'), b'\r\n' in raw]
            if name == 'LEDGER_CONSOLIDATED.md' and b'[L-540]' in staged[name][0]:
                print("ERROR: the ledger already holds L-540 (has this "
                      "patch run before?). If so, there is nothing to do. "
                      "NOTHING was written.")
                sys.exit(1)
        text = staged[name][0]
        o, n = old.encode('ascii'), new.encode('ascii')
        c = text.count(o)
        if c != 1:
            print("ANCHOR FAIL: %s, expected 1 match, found %d: %r\n"
                  "If this patch already ran, there is nothing to do. "
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
    for tool in (["ledger_index.py"], ["doc_index.py", "--caps"]):
        r = subprocess.run([sys.executable] + tool, cwd=HERE,
                           capture_output=True, text=True)
        if r.returncode != 0:
            print((r.stdout or '')[-1500:] + (r.stderr or '')[-800:])
            print("ERROR: %s exited %d. The edits above are written; "
                  "tell the session what it printed." % (' '.join(tool),
                                                        r.returncode))
            sys.exit(1)
        print("ok   %s" % ' '.join(tool))


if __name__ == '__main__':
    main()
