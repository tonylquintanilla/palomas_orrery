"""
patch_L540_3_record_correction.py -- corrects L-540 and records the two
Featured cards, after patch_L540_1.

Built on 5aa6a013 at https://github.com/tonylquintanilla/palomas_orrery
(branch main), with gallery aba9df72 read for what the website does today.

RUN COMMAND
    Save this file in the orrery folder (palomas_orrery_for_github),
    open it in VS Code and click Run:

        python patch_L540_3_record_correction.py

    Success: one "ok" line per edit, "patch applied", then ledger_index.py
    and the document-caps check run, each printing "ok".
    Failure: an "ERROR:" or "ANCHOR FAIL" line, and NOTHING is written.
    Undo after a success: Discard Changes in GitHub Desktop.
    Once it has run, move it to the documentation folder.

Run patch_L540_1_reel_card_record.py first; this one edits what it wrote.

What it changes:
    LEDGER_CONSOLIDATED.md: L-540's title and body. The first record
        said the room could not open on chosen bodies; it can (?show=,
        L-518) and the gallery editor makes scene cards (L-519). It now
        records Tony's 12:50 and 13:01 rulings (the reel's link and
        ESCAPADE's scene side by side in Featured), the website change
        in patch_L540_2, and the two cards as his to make.
    documentation/WHERE_WE_ARE.md: the box's second line; the Deferred
        line for L-540 removed, and a "Needs you now" line for the two
        cards added in its place, so the page stays at its cap.

Written November 20, 2026 with Anthropic's Claude Opus 5.5.
"""

import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

EDITS = [('LEDGER_CONSOLIDATED.md',
  '#### [L-540] A reel on a Featured card, ending with a link into the '
  'room on its scene (gallery; an idea, for a later build)\n',
  '#### [L-540] A reel on a Featured card, beside a link into the room on '
  'its scene (gallery; the two cards Nov 20, a card that plays video an '
  'idea)\n'),
 ('LEDGER_CONSOLIDATED.md',
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
  'of Nov 17 (L-060).\n',
  '- **Corrected the same day (13:00, the coordinating session):** the\n'
  '  first record said the room could not open on chosen bodies. It can,\n'
  '  and has since Nov 8: the room writes the ticked rows into its own\n'
  '  address (?show=, with ?at= for the minute), and since Nov 9 the\n'
  "  gallery editor's New Scene window keeps such a link as a SCENE card,\n"
  '  which Featured can carry (L-518, L-519; gallery/scene_address.js,\n'
  "  tools/gallery_editor.py). The session's search had read only\n"
  '  interactive.html. A card that plays a video does not exist: the '
  'lobby\n'
  '  draws a picture and a link, with no <video>.\n'
  '- **Tony, 12:50:** "Alternatively I could post the Instagram reel in\n'
  '  Featured as a link." **13:01:** "That would be ideal", to two cards\n'
  "  side by side in Featured: the reel's link on Instagram, and\n"
  "  ESCAPADE's scene (ESCAPADE-Blue, ESCAPADE-Gold and Earth-Sun L2\n"
  "  ticked, opening at today's date).\n"
  '- **Built:** patch_L540_2_outside_link_card (gallery, index.html). A\n'
  '  card whose "live" address is another website\'s is read as a page\n'
  '  card: no "Interactive" label, and a tap opens it in a new tab. The\n'
  '  editor\'s "Live scene URL" field already takes any address.\n'
  '  **Tony-action (do):** in the gallery editor, a New Scene from the\n'
  "  room's shared link with the three rows ticked, Featured on; and a\n"
  "  card whose Live scene URL is the reel's Instagram address, Featured\n"
  "  on, with no drawer place, so it stays out of the room's drawer; then\n"
  '  Save All, push, and look on the phone.\n'
  "**Gap:** the two cards and Tony's look. A card that plays the reel on\n"
  'the lobby itself stays an idea, for a design talk if the link card\n'
  'falls short.\n'
  '**Ref:** L-533 (ESCAPADE); L-518 (the shared scene link); L-519 '
  '(Scenes\n'
  "in Featured); L-363 and L-428 (the lobby's wide card and start card);\n"
  'the reel rule of Nov 17 (L-060).\n'),
 ('documentation/WHERE_WE_ARE.md',
  '> - Your idea of the reel on a Featured card, ending with a link into '
  'the room showing the twins, is recorded for a later build (L-540 (a '
  'reel on a Featured card)).\n',
  "> - The reel's link and ESCAPADE's scene go side by side in Featured; "
  'the website now opens an outside link in a new tab, with no '
  '"Interactive" label (L-540 (a reel on a Featured card)).\n'),
 ('documentation/WHERE_WE_ARE.md',
  '- A reel on a Featured card, ending with a link that opens the room on '
  'its bodies: a gallery build of its own (Nov 20; L-540 (a reel on a '
  'Featured card)).\n',
  ''),
 ('documentation/WHERE_WE_ARE.md',
  '> - *(do) Renew palomasorrery.com at Porkbun by 13 Feb 2027 (L-516).*\n',
  '> - *(do) Renew palomasorrery.com at Porkbun by 13 Feb 2027 (L-516).*\n'
  "> - *(do) In the gallery editor: a New Scene from the room's shared "
  'link with ESCAPADE-Blue, ESCAPADE-Gold and Earth-Sun L2 ticked, and a '
  "card whose Live scene URL is the reel's Instagram address; both "
  'Featured, then Save All, push, and look on your phone (L-540 (a reel on '
  'a Featured card)).*\n')]


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
            if name == 'LEDGER_CONSOLIDATED.md' and b'[L-540]' not in staged[name][0]:
                print("ERROR: the ledger has no L-540 yet. Run "
                      "patch_L540_1_reel_card_record.py first, then this "
                      "one. NOTHING was written.")
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
