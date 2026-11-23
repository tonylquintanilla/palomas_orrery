"""
patch_L539_5_talk_forward.py -- two things said after the close patch
was placed, Nov 22, 2026, 21:19: Tony's "yes" to holding the talk on
L-549 (four moons JPL cannot place) ahead of the encounter's slice 2,
and a correction to what the close said about Haumea's moons.

Built on 811cf44f at https://github.com/tonylquintanilla/palomas_orrery
(branch main) WITH patch_L539_4_session_close.py run on top. Written
by the coordinating session (Claude Fable 5.2) under safe-file-editing
1.14 and ledger-and-session-records 1.23, the copies it loaded.

Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\
gallery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\

RUN COMMAND
    Run patch_L539_4_session_close.py FIRST. Then, with this file in
    the orrery folder (palomas_orrery_for_github), open it in VS Code
    and click Run:

        python patch_L539_5_talk_forward.py

    Success: one "ok" line per edit, "patch applied", then two tools,
    each printing "ok": ledger_index.py and doc_index.py --caps.
    Failure: an "ERROR:" or "ANCHOR FAIL" line, and NOTHING is written.
    Undo after a success: Discard Changes in GitHub Desktop.
    Once it has run, move it to the documentation folder.

WHY A SECOND PATCH
    A delivered patch is never replaced (safe-file-editing): the close
    patch was already in Tony's folder when he answered, so these go in
    the next numbered one.

WHAT IT CHANGES (no code, no skill, no protocol)
    LEDGER_CONSOLIDATED.md
        L-549 (four moons JPL cannot place): the close said a typed
        value gave the orbit's "two ends". Wrong: an end marker's place
        is geometry on JPL's ellipse; the typed value is the period its
        DATE is worked out from. Corrected in view, with Tony's
        question. And his "yes": the talk moves ahead of the
        encounter's slice 2.
        L-539 (every entry checked): the words that twice made Tony
        think a Lagrange point's path was not drawn, and the rule.
    documentation/WHERE_WE_ARE.md, above the marker: two "Changed"
        lines, "Do next" (the talk in the order), the talk's own line.
        Still 129 lines.
    documentation/PROMPT_coordinator_start_20261122_4.md: the same
        corrections, the talk in the order, two lessons.

Tested on a fresh copy of the orrery at 811cf44f with the close patch
run: every edit applied, both tools passed; run without the close
patch, and run twice, it refused and wrote nothing.

Written November 22, 2026 with Anthropic's Claude Fable 5.2.
"""

import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

EDITS = [('LEDGER_CONSOLIDATED.md',
  '  from JPL." and "JPL states no accuracy for this position". So one\n'
  '  picture names two sources for one orbit: JPL for the curve, from\n'
  '  February, for an id JPL has since dropped, and a typed value for its\n'
  '  two ends. All four end markers carry one date, 2026-11-23, the day\n'
  "  of the plot; an orbit's nearest and farthest points cannot share a\n"
  '  day. Recorded, not diagnosed.\n',
  '  from JPL." and "JPL states no accuracy for this position".\n'
  '- CORRECTED the same evening, on Tony\'s question, 21:19: "This would be\n'
  '  geometry from the Keplerian orbit not actual positions right?" Yes.\n'
  "  An end marker's PLACE is geometry: the nearest and farthest points\n"
  "  of the same ellipse the curve draws, from JPL's elements of\n"
  '  February. The typed value is the PERIOD its DATE is worked out from\n'
  '  (orbital_period.py, date_note_lines: "The hover lines a computed\n'
  '  date carries"). This entry first said "a typed value for its two\n'
  '  ends", which was wrong (patch_L539_4_session_close.py; corrected by\n'
  '  patch_L539_5_talk_forward.py). What stands: the curve says JPL,\n'
  '  from February, for an id JPL has since dropped; and all four end\n'
  '  markers print one date, 2026-11-23, the day of the plot, where a\n'
  '  moon reaches its nearest and farthest points half a period apart.\n'
  '  The date is the open matter, not the place. Recorded, not diagnosed.\n'
  '- **Tony, 2026-11-22, 21:19: "yes"**, to the coordinating session\'s\n'
  '  thought: "the orbit that says \'JPL\' for a body JPL has dropped is\n'
  '  the kind of label this project exists to prevent. I would bring the\n'
  "  L-549 talk forward, ahead of the encounter's slice 2, and not leave\n"
  '  it behind the builds." The talk is held before the encounter\'s slice\n'
  "  2 (L-529); the order is the road's, on Where We Are.\n"),
 ('LEDGER_CONSOLIDATED.md',
  'say, with the look above in hand; whether Vanth comes off its lists.\n'
  '- **Tony-action (decide):** at the next design talk.\n',
  'say, with the look above in hand; whether Vanth comes off its lists.\n'
  "- **Tony-action (decide):** at its talk, ahead of the encounter's\n"
  '  slice 2 (his "yes", 2026-11-22).\n'),
 ('LEDGER_CONSOLIDATED.md',
  "  eye. Lines 10 to 14, Haumea's two moons, are on L-549 (four moons\n"
  '  JPL cannot place).\n',
  "  eye. Lines 10 to 14, Haumea's two moons, are on L-549 (four moons\n"
  '  JPL cannot place).\n'
  '- THE SAME WORDS CONFUSED TWICE. The session\'s report said "The panel\n'
  '  asked JPL for the Moon\'s orbit only, never for L1\'s"; Tony, 21:19:\n'
  '  "I don\'t follow the issue of not drawing the L orbits." Nothing is\n'
  "  undrawn: a point's path is drawn from JPL's positions, as before.\n"
  '  What is no longer asked is its osculating elements, the six numbers\n'
  '  that describe an ellipse, which a point does not have. A report to\n'
  '  Tony says "elements" and glosses it, never "orbit", for what the\n'
  '  skip removes.\n'),
 ('documentation/WHERE_WE_ARE.md',
  'plays, your "-- yes", and the point is asked for no orbit (L-512 '
  '(fallbacks when JPL cannot answer)).\n',
  'plays, your "-- yes". Its path is drawn from JPL\'s positions, as before; '
  'JPL is no longer asked for the numbers that describe an ellipse, which a '
  'point does not have (L-512 (fallbacks when JPL cannot answer)).\n'),
 ('documentation/WHERE_WE_ARE.md',
  'JPL\'s, of Feb 2; its two end markers say "typed value, not fetched from '
  'JPL"; neither moon has a marker of its own. That is for our talk (L-549 '
  '(four moons JPL cannot place)).\n',
  "JPL's, of Feb 2, though JPL has since dropped both moons; the dates on "
  'its two end markers both show the day of the plot; neither moon has a '
  'marker of its own. Your "yes": that talk moves ahead of the encounter\'s '
  'slice 2 (L-549 (four moons JPL cannot place)).\n'),
 ('documentation/WHERE_WE_ARE.md',
  "then L-538 (the orbiters' printed error); then the encounter's slice 2, "
  'its talk first (L-529 (guided encounters)). Your "Yes" of Nov 22 to this '
  'order.*',
  "then L-538 (the orbiters' printed error); then the talk on L-549 (four "
  'moons JPL cannot place), put ahead on Nov 22, your "yes"; then the '
  "encounter's slice 2, its talk first (L-529 (guided encounters)).*"),
 ('documentation/WHERE_WE_ARE.md',
  'comes off its skip lists. Your look of Nov 22: the orbits say JPL, their '
  'end markers say typed, and neither moon has its own marker (Nov 22; L-549 '
  '(four moons JPL cannot place)).\n',
  'comes off its skip lists. Ahead of the encounter\'s slice 2, your "yes". '
  "Your look: the orbits say JPL, of Feb 2; their end markers' dates both "
  "show the plot's day; neither moon has its own marker (Nov 22; L-549 (four "
  'moons JPL cannot place)).\n'),
 ('documentation/PROMPT_coordinator_start_20261122_4.md',
  '  animation with a Lagrange point plays, and the point is asked for no\n'
  '  orbit.\n',
  "  animation with a Lagrange point plays. Its path is drawn from JPL's\n"
  '  positions as before; what JPL is no longer asked for is its\n'
  '  osculating elements, which a point does not have.\n'),
 ('documentation/PROMPT_coordinator_start_20261122_4.md',
  '  since dropped; its two end markers say "typed value, not fetched\n'
  '  from JPL", all four dated the day of the plot; neither moon has a\n'
  '  marker of its own.\n',
  '  since dropped. Its two end markers are geometry on that ellipse;\n'
  '  their dates are worked out from a typed period ("typed value, not\n'
  '  fetched from JPL") and all four show the day of the plot. Neither\n'
  '  moon has a marker of its own.\n'),
 ('documentation/PROMPT_coordinator_start_20261122_4.md',
  "- Then L-538 (the orbiters' printed error), then the encounter's slice\n"
  '  2, its talk first (L-529).\n',
  "- Then L-538 (the orbiters' printed error); then the talk on L-549\n"
  '  (the four moons), put ahead of the encounter on Nov 22: Tony, 21:19,\n'
  '  "yes". Then the encounter\'s slice 2, its talk first (L-529).\n'),
 ('documentation/PROMPT_coordinator_start_20261122_4.md',
  '  push copy), L-545 (whether the walks join the gallery run), L-548 (a\n'
  '  missing id_type), and at a talk L-549 (the four moons).\n',
  '  push copy), L-545 (whether the walks join the gallery run) and L-548\n'
  '  (a missing id_type).\n'),
 ('documentation/PROMPT_coordinator_start_20261122_4.md',
  "  markers' words, and the orbit's own words said JPL.\n",
  "  markers' words, and the orbit's own words said JPL.\n"
  "- Twice in one day a report made Tony think a Lagrange point's path\n"
  '  was not drawn. Say "elements", with its gloss (the numbers that\n'
  '  describe an ellipse), for what the skip removes; never "orbit".\n'
  '  Tony: "I don\'t follow the issue of not drawing the L orbits."\n'
  "- This session's first reading of the end markers was wrong: it took\n"
  '  "typed value" for the markers\' places. Tony\'s question set it\n'
  "  right, and the code's own docstring settled it. Read the function\n"
  '  that writes a hover line before saying what the line means.\n')]


def main():
    staged = {}
    for name, old, new in EDITS:
        path = os.path.join(HERE, *name.split('/'))
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
        c = text.count(o)
        if c != 1:
            print("ANCHOR FAIL: %s, expected 1 match, found %d: %r\n"
                  "If this patch already ran, there is nothing to do. If "
                  "patch_L539_4_session_close.py has not run, run it first. "
                  "Otherwise the file moved since this was built: tell the "
                  "session. NOTHING was written." % (name, c, old[:70]))
            sys.exit(1)
        staged[name][0] = text.replace(o, n)
        print("ok   %s: %s" % (name, (old.strip().splitlines()
                                      or ['(end)'])[0][:52]))
    for name, (text, was_crlf) in staged.items():
        with open(os.path.join(HERE, *name.split('/')), 'wb') as f:
            f.write(text)
        if was_crlf:
            print("note: %s was CRLF in the working copy; written LF" % name)
    print("patch applied (%d edits, %d files)" % (len(EDITS), len(staged)))
    for tool in (["ledger_index.py"], ["doc_index.py", "--caps"]):
        r = subprocess.run([sys.executable] + tool, cwd=HERE,
                           capture_output=True, text=True)
        if r.returncode != 0:
            print((r.stdout or '')[-1800:] + (r.stderr or '')[-800:])
            print("ERROR: %s exited %d. The edits above are written; "
                  "Discard Changes in GitHub Desktop undoes them. Tell "
                  "the session what it printed." % (' '.join(tool),
                                                    r.returncode))
            sys.exit(1)
        print("ok   %s" % ' '.join(tool))
    print("")
    print("Do next: move this file and patch_L539_4_session_close.py into")
    print("documentation; commit and push the orrery; start the next")
    print("coordinating session with")
    print("documentation/PROMPT_coordinator_start_20261122_4.md, pasted")
    print("from below its line.")

if __name__ == '__main__':
    main()
