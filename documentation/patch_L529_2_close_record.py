"""
patch_L529_2_close_record.py -- closes the first encounter's part of the
coordinating session of Nov 20 and 21 (Claude Fable 5.2): Tony's phone
look and the player's patch on L-529, the Nov 20 rulings on L-534 and
L-533, one open question on L-541, the design record's clock corrected,
and Where We Are.

Built on 39070a959e1d at https://github.com/tonylquintanilla/palomas_orrery
(branch main), with gallery 5a7df273 read for what was pushed, and
Tony's run record documentation/WHERE_WE_ARE_11-20-26_2039_run_record.md
read first.

RUN COMMAND
    Save this file in the orrery folder (palomas_orrery_for_github),
    open it in VS Code and click Run:

        python patch_L529_2_close_record.py

    Success: one "ok" line per edit, "patch applied", then ledger_index.py
    and the document-caps check run, each printing "ok".
    Failure: an "ERROR:" or "ANCHOR FAIL" line, and NOTHING is written.
    Undo after a success: Discard Changes in GitHub Desktop.
    Once it has run, move it to the documentation folder.

    RUN IT BEFORE the Links fold's Claude Code session (L-540) writes its
    own closing records: both edit Where We Are. If it prints ANCHOR FAIL
    on documentation/WHERE_WE_ARE.md, that session got there first; tell
    the coordinating session, which rebuilds this on the new page.

What it changes (20 edits, 3 files; no code):
    LEDGER_CONSOLIDATED.md
      L-529 (guided encounters): Tony's phone look of Nov 20, 21:40, in
        his words; the player's patch and his "Yes it does" of Nov 21;
        what the coordinating session checked on his disk; what it got
        wrong; the Gap rewritten for slice 2. Still OPEN.
      L-534 (missions by destination): his Nov 20 rulings, and what they
        change of Nov 15's. Still OPEN.
      L-533 (ESCAPADE): the flyby dates answered, "The path ends at
        Mars. That is enough for now.", the L2 loiter an encounter.
      L-541 (a plan's clock): one wider question, marked not verified.
      Each item's stamp moves to 2026-11-21.
    documentation/DESIGN_encounters_20261120.md: the plan's times are on
        JPL's clock, not UTC as first written; a closing line.
    documentation/WHERE_WE_ARE.md: the header; one line each in "Changed
        since", "Do next" and "Needs you now"; the road's stage 15; one
        Deferred line; the Signals date line; the marks reset. No line
        is added: the page stands at its cap of 130 above the marker.
        Nothing below the marker is touched.

NOT in this patch: the skill text the encounter's build owes
(interactive-exhibit, gallery-cache-builder, and one rule each for
safe-file-editing and horizons-orbital-mechanics). It is written in one
bump with the Links fold's, after that build closes, so the skills are
reinstalled once.

Tested on a copy of the orrery at 39070a95: 20 edits applied, a second
run refused, ledger_index.py and doc_index.py --caps both passed, Where
We Are still 130 lines above the marker.

Written November 21, 2026 with Anthropic's Claude Fable 5.2.
"""

import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

EDITS = [('LEDGER_CONSOLIDATED.md',
  '<!-- L:529 status:OPEN upd:2026-11-20 section:A flag: rice: -->',
  '<!-- L:529 status:OPEN upd:2026-11-21 section:A flag: rice: -->'),
 ('LEDGER_CONSOLIDATED.md',
  "**Gap:** Tony's phone look at slice 1, after the push. Slice 2: the two\n"
  'close passes, escape speed beside the speed, NASA\'s "powered Earth\n'
  'flybys" through the orrery\'s words. The L2 loiter as an encounter. How\n'
  'a completed encounter is asked again if JPL replaces a prediction with\n'
  'a measurement.\n',
  "- **TONY'S PHONE LOOK, 2026-11-20, 21:40**, with a picture of the\n"
  '  encounter playing (website f918d74b, orrery df034699; his run record\n'
  '  `documentation/WHERE_WE_ARE_11-20-26_2039_run_record.md`): "Two\n'
  '  issues: 1) the Pause button is difficult to activate while Play is not\n'
  '  an issue. 2) make the play bar oval around the bar opacity 0. Works\n'
  '  great! Thanks."\n'
  "- **THE PLAYER'S PATCH, the same night:** `patch_L529_1_player_press.py`\n"
  '  (gallery, pushed at 7dbcc903; the coordinating session, Claude Fable\n'
  '  5.2). The button answers the press (pointerdown), not the click that\n'
  '  follows it; a second press inside 350 ms is the same press; the\n'
  '  button is 44 px tall; the oval around the player is clear. The\n'
  '  reading it was built on was not measured on a phone: while it plays\n'
  "  the page is busy drawing, a phone's click comes late, and a second\n"
  '  tap then started it again. Tested on a copy of the pushed page, 12\n'
  "  checks, 5 of them failing on the page as pushed. Tony's run record,\n"
  '  beside "press Play and Pause several times": "-- correct"; and\n'
  '  2026-11-21, 12:02, asked whether Pause takes on the first tap: "Yes\n'
  '  it does." Slice 1 is LIVE AND LOOKED AT.\n'
  "- **VERIFIED AGAINST CLAIMED, by the coordinating session on Tony's\n"
  '  disk before the push (Nov 20, 20:35):** no non-ASCII byte in the\n'
  '  three new code files or the three changed page files it read; each\n'
  "  twin's box carries its served description, which names Mars; the\n"
  "  card file held the encounter's card and one scene; the one change to\n"
  "  orrery code was the dashboard's button. Taken from the build's\n"
  '  report and not checked again: the seven planted faults and the\n'
  '  walk.\n'
  '- **WHAT THE COORDINATING SESSION GOT WRONG, kept for the next brief.**\n'
  "  The brief and the design record said the plan's times are UTC; they\n"
  "  are on JPL's clock (the build caught it; L-541 (a plan's clock)).\n"
  "  The voice call said the plan holds an encounter's window; it does\n"
  "  not (the design record's 3.2). The slice ran to about 670,000\n"
  "  tokens by the build's own estimate: one brief held the package, the\n"
  "  scene, the row, Find and the editor. Slice 2's brief keeps each\n"
  '  session inside one part of the site.\n'
  '**Gap:** slice 2, its talk first: the two close passes and how the\n'
  'visitor moves between the three views; escape speed beside the speed\n'
  'in the close views; NASA\'s "powered Earth flybys" through the\n'
  "orrery's words; the words on each card. The L2 loiter as an encounter\n"
  '(Tony, Nov 20), its view its own question. How a completed encounter\n'
  'is asked again if JPL replaces a prediction with a measurement. The\n'
  "skill text owed: the build's eleven rules above, at\n"
  "interactive-exhibit's next bump, written together with the Links\n"
  "fold's (L-540 (a reel on a Featured card)) so Tony reinstalls once.\n"),
 ('LEDGER_CONSOLIDATED.md',
  '<!-- L:534 status:OPEN upd:2026-11-18 section:A flag: rice: -->',
  '<!-- L:534 status:OPEN upd:2026-11-21 section:A flag: rice: -->'),
 ('LEDGER_CONSOLIDATED.md',
  '**Gap:** the design round, with L-529 (guided encounters), after the\n'
  'Lagrange points (L-297); ESCAPADE (L-533) the worked example.\n',
  "- **Tony's rulings, 2026-11-20**, by voice and then in chat with the\n"
  '  coordinating session (Claude Fable 5.2); the whole talk is\n'
  '  `documentation/DESIGN_encounters_20261120.md`. From the voice\n'
  '  transcript, fillers removed: "maybe this is just a type of\n'
  '  encounter, not a different kind of visualization"; "perhaps we\n'
  '  should just build completed encounters at this time." Typed, 14:46,\n'
  '  on what the page says of ESCAPADE\'s destination: "The path ends at\n'
  '  Mars. That is enough for now."\n'
  '  - WHAT THIS CHANGES. The Nov 15 rulings above, a row under Mars and\n'
  '    the second of the "three paths", wait. Nothing new sits under\n'
  '    Mars for ESCAPADE until it arrives, September 2027 by the plan.\n'
  '    They are not withdrawn: his words were "for now".\n'
  "  - The first encounter, ESCAPADE's Earth flybys, was built under\n"
  '    L-529 (guided encounters) and is live.\n'
  "**Gap:** waits behind L-529's encounters. To ask Tony when an arrival\n"
  'is next to be shown: whether a destination appears only as that\n'
  "arrival's encounter, or the Nov 15 row comes back.\n"),
 ('LEDGER_CONSOLIDATED.md',
  '<!-- L:533 status:OPEN upd:2026-11-20 section:A flag: rice: -->',
  '<!-- L:533 status:OPEN upd:2026-11-21 section:A flag: rice: -->'),
 ('LEDGER_CONSOLIDATED.md',
  "**Gap:** the row under Mars, by L-534's rule once it is designed. The\n"
  "box's last day: its build, as ruled Nov 19.",
  '- **2026-11-20 and 21, THE FLYBY DATES, THE DESTINATION, THE LOITER.**\n'
  '  Tony\'s miss of Nov 18, "The only thing I miss are the dates of\n'
  '  flybys", is answered by the first encounter, ESCAPADE\'s Earth\n'
  '  flybys, live Nov 20 and looked at on his phone ("Works great!"):\n'
  '  each pass carries its date, and the Encounters fold under Earth\n'
  '  prints both (L-529 (guided encounters)). His other miss, the\n'
  '  destination, Nov 20, 14:46: "The path ends at Mars. That is enough\n'
  '  for now." Ruled in the same message: "there is also the L2 loiter\n'
  '  as an encounter"; it is built after the flybys\' slice 2, and its\n'
  '  view is its own question.\n'
  '**Gap:** the row under Mars waits (L-534 (missions by destination),\n'
  "Nov 20). The box's last day: its build, as ruled Nov 19."),
 ('LEDGER_CONSOLIDATED.md',
  '<!-- L:541 status:OPEN upd:2026-11-20 section:A flag: rice: -->',
  '<!-- L:541 status:OPEN upd:2026-11-21 section:A flag: rice: -->'),
 ('LEDGER_CONSOLIDATED.md',
  "**Gap:** a ruling on each: convert, or name JPL's clock where it is\n",
  '- **A WIDER QUESTION, NOT VERIFIED** (the coordinating session, Claude\n'
  '  Fable 5.2, 2026-11-20; from a search of the code, not a trace).\n'
  "  Every served position carries JPL's date, on JPL's clock, and the\n"
  "  live rooms appear to place a body by the visitor's UTC minute\n"
  '  against those dates with no conversion: the search found no TDB\n'
  "  handling in `gallery/assembler/` or in the page's clock, and\n"
  '  `resolver.py` turns an ISO UTC time into a Julian date as it stands.\n'
  '  If that is so, every body in a live room is drawn 69 seconds from\n'
  '  the minute its title shows. To trace end to end before anything\n'
  '  changes: what the builder stamps, what the page asks for, and\n'
  "  whether any box prints finer than 69 seconds of its body's motion.\n"
  "**Gap:** a ruling on each: convert, or name JPL's clock where it is\n"),
 ('documentation/DESIGN_encounters_20261120.md',
  'worked out from JPL by `path_plan.py`; times are UTC; distances are\n'
  "from the body's centre.\n",
  "worked out from JPL by `path_plan.py`; times are on JPL's clock, TDB,\n"
  "69 seconds ahead of UTC; distances are from the body's centre.\n"
  '(Corrected Nov 21: this line first said UTC. The build caught it and\n'
  'the encounter converts; L-541.)\n'),
 ('documentation/DESIGN_encounters_20261120.md',
  'The close moves these rulings to L-534, L-529 and L-533 by patch. The\n'
  "builder's brief is written when its session is next.\n",
  'The close moves these rulings to L-534, L-529 and L-533 by patch. The\n'
  "builder's brief is written when its session is next.\n"
  '\n'
  'Done, Nov 20 and 21: slice 1 was built from\n'
  '`COORD_L529_encounter_escapade_earth_brief_20261120.md`, pushed, and\n'
  'looked at on Tony\'s phone ("Works great!"); the rulings are on L-529,\n'
  "L-534 and L-533 by `patch_L529_2_close_record.py`. Section 8's list\n"
  "is slice 2's talk.\n"),
 ('documentation/WHERE_WE_ARE.md',
  'Last updated: November 21, 2026, morning: link cards, every address in '
  'the i panels a link, the editor laid out as the website, and an Outside '
  'Links room (Opus, coordinating session).\n'
  "- Written at orrery 08656fdc and gallery 5a7df273, with this patch's "
  'edits on your disk.\n',
  "Last updated: November 21, 2026, midday: the first encounter's close, "
  'your phone look recorded and the Nov 20 rulings on the ledger (Fable, '
  'coordinating session).\n'
  "- Written at orrery 39070a95 and gallery 5a7df273, with this patch's "
  'edits on your disk.\n'),
 ('documentation/WHERE_WE_ARE.md',
  "> - The first encounter is built: ESCAPADE's Earth flybys play hour by "
  'hour, from 18 October to 14 November, with both twins, the Moon and '
  'Earth-Sun L2 moving and each pass dated; it opens from an Encounters fold '
  "under Earth's row (L-529 (guided encounters)).\n",
  "> - The first encounter is live and looked at: ESCAPADE's Earth flybys "
  "play hour by hour from the Encounters fold under Earth's row, each pass "
  'dated; your look of Nov 20, "Works great!", and Pause takes on the first '
  "tap since the player's patch (L-529 (guided encounters)).\n"),
 ('documentation/WHERE_WE_ARE.md',
  "> **Do next:** *Your phone look at ESCAPADE's Earth flybys after the push "
  "(L-529 (guided encounters)); beside it, this round's cleanup (the road, "
  'line b).*\n',
  "> **Do next:** *The Links fold's build, in progress (L-540 (a reel on a "
  "Featured card)); then the encounter's slice 2, its talk first (L-529 "
  "(guided encounters)); beside it, this round's cleanup (the road, line b), "
  'whose briefs are not written yet.*\n'),
 ('documentation/WHERE_WE_ARE.md',
  '> - *(do) Push both and look at the encounter on your phone (L-529 '
  '(guided encounters)); then remake the ESCAPADE scene in the gallery '
  "editor, kept in the Solar System room (L-542 (a scene's room)).*\n",
  '> - *(do) If you still want it, remake the ESCAPADE scene in the gallery '
  "editor, kept in the Solar System room (L-542 (a scene's room)).*\n"),
 ('documentation/WHERE_WE_ARE.md',
  '## The road  **>> UPDATED THIS SESSION**\n',
  '## The road\n'),
 ('documentation/WHERE_WE_ARE.md',
  'Nov 20 (L-529 (guided encounters)) << new this session; then Uranus and '
  'Neptune.',
  'Nov 20, on your phone look (L-529 (guided encounters)); then Uranus and '
  'Neptune.'),
 ('documentation/WHERE_WE_ARE.md',
  '## Deferred\n',
  '## Deferred  **>> UPDATED THIS SESSION**\n'),
 ('documentation/WHERE_WE_ARE.md',
  "- ESCAPADE's loops near L2 show only in a view centred on Earth, and the "
  "website draws a planned path around the Sun alone: with Earth's fold, "
  'where SOHO, Gaia and JWST need it too (Nov 18; L-533 (ESCAPADE)).\n',
  "- ESCAPADE's year near L2 is an encounter of its own, after the flybys' "
  'slice 2; its view is an open question, since its loops show only around '
  'Earth and not as NASA draws them (Nov 20; L-529 (guided encounters)). A '
  'planned path drawn around Earth, which SOHO, Gaia and JWST need too, '
  "stays with Earth's fold (Nov 18; L-533 (ESCAPADE)).\n"),
 ('documentation/WHERE_WE_ARE.md',
  "- This page's date and the ledger's newest stamp: both Nov 20. Agree.\n",
  "- This page's date and the ledger's newest stamp: both Nov 21. Agree.\n"),
 ('documentation/WHERE_WE_ARE.md',
  '## Waiting on you  **>> UPDATED THIS SESSION**\n',
  '## Waiting on you\n')]


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
        text = staged[name][0]
        o, n = old.encode('ascii'), new.encode('ascii')
        if text.count(n) >= 1 and o in n and text.count(o) == text.count(n):
            print("ERROR: %s already holds this change (has the patch run "
                  "before?). NOTHING was written." % name)
            sys.exit(1)
        c = text.count(o)
        if c != 1:
            print("ANCHOR FAIL: %s, expected 1 match, found %d: %r\n"
                  "If this patch already ran, there is nothing to do. "
                  "NOTHING was written." % (name, c, old[:70]))
            sys.exit(1)
        staged[name][0] = text.replace(o, n)
        print("ok   %s: %s" % (name, old.strip().splitlines()[0][:58]))
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
