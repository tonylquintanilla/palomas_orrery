"""
patch_L540_7_close_record.py -- closes the coordinating session of Nov
18-21: records tonight's L-540 work (link cards, the links check, the
editor laid out as the website, the Outside Links room) in the ledger
and on Where We Are.

Built on 08656fdc at https://github.com/tonylquintanilla/palomas_orrery
(branch main), with gallery 5a7df273 read for what was pushed.

RUN COMMAND
    Save this file in the orrery folder (palomas_orrery_for_github),
    open it in VS Code and click Run:

        python patch_L540_7_close_record.py

    Success: one "ok" line per edit, "patch applied", then ledger_index.py
    and the document-caps check run, each printing "ok".
    Failure: an "ERROR:" or "ANCHOR FAIL" line, and NOTHING is written.
    Undo after a success: Discard Changes in GitHub Desktop.
    Once it has run, move it to the documentation folder.

What it changes:
    LEDGER_CONSOLIDATED.md: L-540's last part rewritten from "Built:" to
        its Ref: the correction of 19:30 (the editor could not make a
        link card), Tony's rulings of 22:27 and 23:28 to 23:32, the
        three website patches and what each did, his do-steps, and the
        skill text owed at gallery-pipeline's next bump. Still OPEN,
        for his do-steps and phone look.
    documentation/WHERE_WE_ARE.md: the header, one line in "Changed
        since you last read this", and the L-540 line in "Needs you now"
        replaced by the Outside Links step. Each edit is anchored at its
        own lines, so your notes and the run record are kept.

Written November 21, 2026 with Anthropic's Claude Opus 5.5.
"""

import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

EDITS = [('LEDGER_CONSOLIDATED.md',
  '<!-- L:540 status:OPEN upd:2026-11-20 section:A flag: rice: -->',
  '<!-- L:540 status:OPEN upd:2026-11-21 section:A flag: rice: -->'),
 ('LEDGER_CONSOLIDATED.md',
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
  'the reel rule of Nov 17 (L-060).\n',
  '- **Built:** patch_L540_2_outside_link_card (gallery, index.html). A\n'
  '  card whose "live" address is another website\'s is read as a page\n'
  '  card: no "Interactive" label, and a tap opens it in a new tab.\n'
  '- **Corrected, 19:30:** the editor could not make that card. Tony: '
  '"the\n'
  '  instagram link does not save in the editor." New Scene takes only\n'
  '  room links, as built, and the editor had no command for a card that\n'
  '  is only a link; its "Live scene URL" field takes any address, but\n'
  '  only on a card that exists. The session had said otherwise without\n'
  "  reading the editor. The reel's card was made by\n"
  '  patch_L540_4_reel_link_card (id escapade_reel, Featured, room\n'
  "  solar_system, no drawer place; its address read from Tony's\n"
  '  screenshot, Df-TOOvjork).\n'
  '- **Tony, 22:27:** "I would prefer a new link card command in the\n'
  "  editor. also ... could you check that all url's in the info panels\n"
  "  have live links not just typed url's? for example, the new Escapade\n"
  '  encounters." Built by patch_L540_5_link_cards_and_links, pushed at\n'
  '  gallery 96c4ca97. Card > New Link Card... in the gallery editor (its\n'
  '  logic tools/link_card.py: the address cleaned of the sharing marks a\n'
  "  site adds, each named; the website's own address refused, with New\n"
  '  Scene named; an address already on a card refused), checked by\n'
  '  tools/test_link_card.py, the gallery run\'s new "Link cards" row, '
  'whose\n'
  "  self-test breaks it two ways first. THE LINKS CHECK: the room's i\n"
  '  panel already linked every address (sunAppendLinked, L-456); two\n'
  "  places did not, both ESCAPADE's encounter: its i panel's source line\n"
  "  (gallery/encounter.js, infoHtml) and a lobby card's source line with\n"
  '  words around its address (index.html, sourcesHtml). Both now cut\n'
  '  addresses by gallery/source_list.js. No page shows an address '
  'outside\n'
  "  a link; the hover and the text box are Plotly's and cannot hold one.\n"
  "  Fixed in passing: New Scene's Save raised an error after making the\n"
  '  scene, so its status line never said so.\n'
  "- **Tony, 23:28 to 23:32:** the editor follows the website's "
  'structure,\n'
  '  "not in a drawer" at the top as "Lobby only"; "a new group for\n'
  "  'Outside Links' like Instagram reels, or maybe other outside links\n"
  '  that are of special interest"; and, asked whether that is a room\n'
  "  visitors see in the website's menu or a group only in the editor:\n"
  '  "Both." Built by patch_L540_6_editor_follows_website, pushed at\n'
  "  gallery 5a7df273: the Solar System door's first group is Lobby only,\n"
  "  open; each drawer row's cards sit in the website's folds (Scenes,\n"
  '  Encounters, Saved pictures), a fold drawn only when it has cards; '
  'New\n'
  '  Link Card puts a card in the room outside_links when it exists, else\n'
  '  in Storage like any new card (Tony, 23:23: "the old place to put new\n'
  '  card that had not been assigned was \'storage\'"). Storage is never\n'
  '  served (L-287), so a card that should show waits there until moved.\n'
  '  Each patch was tested with the editor driven on a virtual screen.\n'
  '  **Tony-action (do):** in the gallery editor, with nothing selected,\n'
  '  Room > New Room..., "Outside Links" for both names (the key is then\n'
  "  outside_links); move the reel's card (Solar System, Lobby only) to "
  'it\n'
  "  with Move to Room...; remake ESCAPADE's scene with New Scene, kept "
  'in\n'
  '  the Solar System room (L-542); Save All, push, and look on the '
  'phone.\n'
  "**Gap:** Tony's do-steps and phone look. The gallery-pipeline skill\n"
  "gains link cards, the Outside Links room and the editor's layout at "
  'its\n'
  'next bump (method, not a ruling). A card that plays the reel on the\n'
  'lobby itself stays an idea, for a design talk if the link card falls\n'
  'short.\n'
  '**Ref:** L-533 (ESCAPADE); L-518 (the shared scene link); L-519 '
  '(Scenes\n'
  "in Featured); L-542 (a scene's room); L-456 (the i panel's links);\n"
  "L-287 (Storage is never served); L-363 and L-428 (the lobby's wide "
  'card\n'
  'and start card); the reel rule of Nov 17 (L-060).\n'),
 ('documentation/WHERE_WE_ARE.md',
  'Last updated: November 20, 2026, evening: the first encounter, '
  "ESCAPADE's Earth flybys, built in the website (Opus, Claude Code).\n"
  "- Written at orrery 74b63fcc and gallery 886610eb, with this session's "
  'edits on your disk.\n',
  'Last updated: November 21, 2026, morning: link cards, every address in '
  'the i panels a link, the editor laid out as the website, and an Outside '
  'Links room (Opus, coordinating session).\n'
  "- Written at orrery 08656fdc and gallery 5a7df273, with this patch's "
  'edits on your disk.\n'),
 ('documentation/WHERE_WE_ARE.md',
  "> - Two items recorded, not fixed: three places read or print a plan's "
  "time, which is on JPL's clock, as UTC (L-541 (a plan's clock)); the "
  'gallery editor let your scene into the Earth room, which the Scene '
  "cards check refuses (L-542 (a scene's room)).\n",
  "> - Two items recorded, not fixed: three places read or print a plan's "
  "time, which is on JPL's clock, as UTC (L-541 (a plan's clock)); the "
  'gallery editor let your scene into the Earth room, which the Scene '
  "cards check refuses (L-542 (a scene's room)).\n"
  '> - The gallery editor has New Link Card, every web address in the i '
  'panels is a link, and its Solar System section is laid out as the '
  "website's: Lobby only first, then each row's Scenes, Encounters and "
  'Saved pictures (L-540 (a reel on a Featured card)).\n'),
 ('documentation/WHERE_WE_ARE.md',
  "> - *(do) In the gallery editor: a New Scene from the room's shared "
  'link with ESCAPADE-Blue, ESCAPADE-Gold and Earth-Sun L2 ticked, and a '
  "card whose Live scene URL is the reel's Instagram address; both "
  'Featured, then Save All, push, and look on your phone (L-540 (a reel on '
  'a Featured card)).*\n',
  '> - *(do) In the gallery editor: New Room... "Outside Links" with '
  "nothing selected, then move the reel's card into it (Move to Room...); "
  'Save All, push, and look on your phone (L-540 (a reel on a Featured '
  'card)).*\n')]


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
            if name == 'LEDGER_CONSOLIDATED.md' and b'Built by patch_L540_6' in staged[name][0]:
                print("ERROR: L-540 already records patch_L540_6 (has this "
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
