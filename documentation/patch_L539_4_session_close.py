"""
patch_L539_4_session_close.py -- the close of the coordinating session
of Nov 22, 2026, evening (the skills bump, v3.145).

Built on 811cf44f at https://github.com/tonylquintanilla/palomas_orrery
(branch main), with gallery e6af10ea at
https://github.com/tonylquintanilla/tonyquintanilla.github.io read for
its swap log. Written by the coordinating session (Claude Fable 5.2)
under safe-file-editing 1.14 and ledger-and-session-records 1.23, the
copies this session loaded.

Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\
gallery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\

RUN COMMAND
    This file is in the orrery folder (palomas_orrery_for_github). Open
    it in VS Code and click Run:

        python patch_L539_4_session_close.py

    Success: one "ok" line per edit, "patch applied", "wrote" for the
    new prompt file, then two tools, each printing "ok": ledger_index.py
    and doc_index.py --caps.
    Failure: an "ERROR:" or "ANCHOR FAIL" line, and NOTHING is written.
    Undo after a success: Discard Changes in GitHub Desktop.
    Once it has run, move it to the documentation folder.

WHAT IT CHANGES (no code, no skill, no protocol)
    LEDGER_CONSOLIDATED.md
        L-539 (every entry checked): Tony's look, lines 8 to 14, done,
        in his words; the bump run, pushed at 811cf44f, reinstalled and
        pasted, from his run record of 19:37.
        L-512 (fallbacks when JPL cannot answer): the animation and the
        window, "not run" by the build, are seen since.
        L-549 (four moons JPL cannot place): what his look showed, in
        his words, and what his saved picture holds.
    documentation/WHERE_WE_ARE.md, above the marker only: the header,
        the three "Changed" lines, "Do next", "Needs you now" (the look
        and the reinstall leave; the next session's start arrives),
        the two road marks cleared, Signals re-read, the four moons'
        talk line. 129 lines above the marker, cap 130.
    documentation/PROMPT_coordinator_start_20261122_4.md: NEW, the
        next coordinating session's starting prompt. This patch places
        it; it is not handed over any other way.

AFTER IT RUNS
    1. (do) Move this file into the documentation folder.
    2. (do) Commit and push the orrery, not while a night is running.
       Your updated run record of 13:15 and your two saved pictures go
       with it if they are in the folder.
    3. (do) Start the next coordinating session with
       documentation/PROMPT_coordinator_start_20261122_4.md, pasted
       from below its line.

Tested on a fresh copy of the orrery at 811cf44f: every edit applied,
both tools passed, and a second run refused and wrote nothing.

Written November 22, 2026 with Anthropic's Claude Fable 5.2.
"""

import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

EDITS = [('LEDGER_CONSOLIDATED.md',
  "- **Tony-action (do):** the checklist's lines 8 to 14, in that run\n"
  '  record: one short animation with the Moon and Earth-Moon L1 ticked,\n'
  "  which no session ran; then Haumea with Hi'iaka and Namaka, a look for\n"
  "  L-549's talk.\n",
  "- TONY'S LOOK, LINES 8 TO 14, DONE Nov 22, evening (the same run\n"
  '  record, his copy as he updated it at 20:37, with two saved\n'
  '  pictures; read by the coordinating session (Claude Fable 5.2)).\n'
  '  Line 8, one animation with the Moon and Earth-Moon L1 ticked around\n'
  '  Earth: "-- yes". Its panel read "[ANIMATION PRE-FETCH] Checking\n'
  '  osculating elements for 1 objects", the Moon alone, and "Final\n'
  '  coverage: 29/29 epochs" for 3011. The record was searched: its only\n'
  '  two "Required masses not defined" are the checklist\'s own lines, and\n'
  '  it holds no traceback. His saved animation\n'
  '  (Earth_system_animation_20261123_0223_earth_moon_eml1.html) names\n'
  "  Earth-Moon L1 in 30 traces and frames. L-512's Part D is seen by\n"
  "  eye. Lines 10 to 14, Haumea's two moons, are on L-549 (four moons\n"
  '  JPL cannot place).\n'),
 ('LEDGER_CONSOLIDATED.md',
  '- **Tony-action (do):** reinstall five skills (Plugins, in the\n'
  '  claude.ai sidebar): horizons-orbital-mechanics, gallery-assembler,\n'
  '  interactive-exhibit, gallery-cache-builder, safe-file-editing; and\n'
  "  paste PROJECT_INSTRUCTIONS.md, v3.145, into the Project's\n"
  '  instructions.\n',
  "- RUN, PUSHED, REINSTALLED AND PASTED, Nov 22 (Tony's run record\n"
  '  documentation/WHERE_WE_ARE_11-22-26_1937_run_record.md): the patch\n'
  '  printed "patch applied (68 edits, 10 files)" and four tools "ok";\n'
  '  the push, "-- 811cf44f8c973a3c2dc847561b02b4139d4513d4"; the five\n'
  '  skills\' reinstall, "-- done"; the paste, "-- v3.145 uploaded".\n'
  '  The coordinating session (Claude Fable 5.2) read\n'
  "  GitHub's HEAD at 811cf44f with the five versions in it, and saw\n"
  "  v3.145 in the Project's instructions when its context was re-read.\n"
  '  The reinstall cannot be checked from the session that wrote the\n'
  '  bump; Tony asked, "should we start a new coordinator due to the new\n'
  '  skills?", and the answer was yes.\n'),
 ('LEDGER_CONSOLIDATED.md',
  'tests. Not run: the animation (its edit is the same line), and the\n'
  '  window by eye.\n',
  'tests. Not run: the animation (its edit is the same line), and the\n'
  '  window by eye. BOTH SEEN SINCE by Tony, Nov 22: the still picture\n'
  '  and the animation, the Lagrange point drawn and asked for no\n'
  '  elements (L-539 (every entry checked), his look).\n'),
 ('LEDGER_CONSOLIDATED.md',
  "**Gap:** a talk with Tony: what Hi'iaka and Namaka should draw now, and\n"
  'say; whether Vanth comes off its lists.\n',
  "- **TONY'S LOOK, Nov 22, evening** (lines 10 to 14 of the checklist in\n"
  '  documentation/WHERE_WE_ARE_11-22-26_1315_run_record.md, his copy as\n'
  '  updated at 20:37; his saved picture\n'
  '  solar_system_20261123_0228_huamea.html, read by\n'
  '  the coordinating session (Claude Fable 5.2)). Centred on Haumea,\n'
  '  both moons ticked. A box offered to update saved orbits: "-- yes".\n'
  '  An orbit for each: "-- yes". A marker for each: "-- no, only the\n'
  '  orbit and the apsidal markers". The source: "-- keplerian from typed\n'
  '  values not jpl". Error text: "-- no jpl accuracy is cited".\n'
  '- WHAT THE SAVED PICTURE HOLDS, read from the file. Neither moon has a\n'
  '  marker of its own. Each orbit is the trace "Osculating Orbit", whose\n'
  '  info marker reads "Epoch: 2026-02-02 osc." and "Osculating orbit\n'
  '  from JPL Horizons satellite ephemeris solution". Each periapsis and\n'
  '  apoapsis marker reads "From a typed period: typed value, not fetched\n'
  '  from JPL." and "JPL states no accuracy for this position". So one\n'
  '  picture names two sources for one orbit: JPL for the curve, from\n'
  '  February, for an id JPL has since dropped, and a typed value for its\n'
  '  two ends. All four end markers carry one date, 2026-11-23, the day\n'
  "  of the plot; an orbit's nearest and farthest points cannot share a\n"
  '  day. Recorded, not diagnosed.\n'
  "- Seen in the same file and not placed on an item: Haumea's i-panel\n"
  '  words read "Horizons: 2003 EL61. A dwarf planet known for its\n'
  '  elongated shape and fast rotation." and its hover reads "Horizons:\n'
  '  136108 Haumea. A dwarf planet with rings": two stores of words for\n'
  '  one body in one picture.\n'
  "**Gap:** a talk with Tony: what Hi'iaka and Namaka should draw now, and\n"
  'say, with the look above in hand; whether Vanth comes off its lists.\n'),
 ('documentation/WHERE_WE_ARE.md',
  'Last updated: November 22, 2026, evening: the skills bump, v3.145, is '
  'written; you reinstall five skills and paste the protocol (Claude Fable '
  '5.2).\n'
  '- Written on orrery 849bf462 and gallery e6af10ea, both pushed; both '
  'nights of Nov 22 clean.\n',
  "Last updated: November 22, 2026, night: this coordinating session's "
  'close. The skills bump, v3.145, is pushed and you reinstalled; your look '
  "in the orrery's window is done (Claude Fable 5.2).\n"
  '- Written on orrery 811cf44f and gallery e6af10ea, both pushed; both '
  'nights of Nov 22 clean.\n'),
 ('documentation/WHERE_WE_ARE.md',
  "> - The orrery's Horizons check now also covers the 56 entries the "
  'website does not serve: the moons, the spacecraft, the barycentres. Each '
  'is held to the name and kind JPL gives its id, as the two L3 entries were '
  'not. You looked at the list and accepted it: "The 14 words are accepted." '
  '(L-539 (every entry checked)).\n'
  "> - JPL has no object at all for four moons: Xiangliu, Hi'iaka, Namaka, "
  "MK2. Hi'iaka's and Namaka's orbits are still drawn from JPL's elements of "
  "Feb 2, labelled as JPL's. That is for a talk, below (L-549 (four moons "
  'JPL cannot place)).\n'
  '> - The Lagrange points no longer ask JPL for orbits or close approaches '
  'they cannot have; the drawing is unchanged (L-512 (fallbacks when JPL '
  'cannot answer)). Nothing the website reads changed.\n',
  '> - Five skills now carry the rules three builds had left on the ledger: '
  'protocol v3.145, pushed at 811cf44f. You reinstalled them and pasted the '
  'protocol; the next session checks that its copies are the new ones (L-539 '
  "(every entry checked), L-541 (a plan's clock)).\n"
  "> - Your look in the orrery's window is done. The animation with "
  'Earth-Moon L1 plays, your "-- yes", and the point is asked for no orbit '
  '(L-512 (fallbacks when JPL cannot answer)).\n'
  "> - Haumea's two moons, from your look: each orbit is drawn and says it "
  'is JPL\'s, of Feb 2; its two end markers say "typed value, not fetched '
  'from JPL"; neither moon has a marker of its own. That is for our talk '
  '(L-549 (four moons JPL cannot place)).\n'),
 ('documentation/WHERE_WE_ARE.md',
  '*The skills bump (v3.145) is written, Nov 22. Next, once you have '
  'reinstalled: L-544 (L4 and L5 tie), in the website; then',
  '*A new coordinating session first checks that its five skills are the new '
  'versions, then takes up L-544 (L4 and L5 tie), in the website; then'),
 ('documentation/WHERE_WE_ARE.md',
  "> - *(do) Finish the look in the orrery's window, lines 8 to 14 of the "
  'checklist in your run record `WHERE_WE_ARE_11-22-26_1315_run_record.md`: '
  'one short animation with the Moon and Earth-Moon L1 ticked, with no '
  '"Required masses not defined" in the panel; then Haumea with Hi\'iaka and '
  'Namaka, for our talk (L-539 (every entry checked), L-549 (four moons JPL '
  'cannot place)).*\n'
  '> - *(do) Reinstall five skills (Plugins, in the claude.ai sidebar): '
  'horizons-orbital-mechanics, gallery-assembler, interactive-exhibit, '
  'gallery-cache-builder, safe-file-editing. Then paste '
  "`PROJECT_INSTRUCTIONS.md`, now v3.145, into the Project's instructions. "
  'The website builds wait for this (L-539 (every entry checked), L-541 (a '
  "plan's clock)).*\n",
  '> - *(do) Start the next coordinating session with '
  '`documentation/PROMPT_coordinator_start_20261122_4.md`, pasted from below '
  'its line. The website builds wait for its check of the skills.*\n'),
 ('documentation/WHERE_WE_ARE.md',
  'then steps 5 and 6.  << moved this session\n',
  'then steps 5 and 6.\n'),
 ('documentation/WHERE_WE_ARE.md',
  'at your desk.  << moved this session\n',
  'at your desk.\n'),
 ('documentation/WHERE_WE_ARE.md',
  '## Settled  **>> UPDATED THIS SESSION**\n',
  '## Settled\n'),
 ('documentation/WHERE_WE_ARE.md',
  '- Last cache build: 20261122T034324Z, ok, no retry on the swap (the '
  "website's swap log at 5a7c96f8, read Nov 22).\n",
  '- Last cache build: 20261122T194726Z, ok, no retry on the swap (the '
  "website's swap log at e6af10ea, read Nov 22).\n"),
 ('documentation/WHERE_WE_ARE.md',
  "(PROVENANCE_AUDIT.md, generated Nov 22 by this session's run, read Nov "
  '22).\n',
  '(PROVENANCE_AUDIT.md, generated Nov 22, read Nov 22 at 811cf44f).\n'),
 ('documentation/WHERE_WE_ARE.md',
  'comes off its skip lists (Nov 22; L-549 (four moons JPL cannot place)).\n',
  'comes off its skip lists. Your look of Nov 22: the orbits say JPL, their '
  'end markers say typed, and neither moon has its own marker (Nov 22; L-549 '
  '(four moons JPL cannot place)).\n')]

PROMPT_PATH = 'documentation/PROMPT_coordinator_start_20261122_4.md'
PROMPT_TEXT = ('<!-- Doc-Kind: hand | A starting prompt for the next coordinating session, '
 'written at the close of the one before it. -->\n'
 '# Starting prompt: the next coordinating session\n'
 '\n'
 'Built on orrery 811cf44f at\n'
 'https://github.com/tonylquintanilla/palomas_orrery (branch main) and\n'
 'gallery e6af10ea at\n'
 'https://github.com/tonylquintanilla/tonyquintanilla.github.io, with\n'
 'patch_L539_4_session_close.py on top. Written Nov 22, 2026 by the\n'
 'coordinating session of that evening (Claude Fable 5.2).\n'
 '\n'
 "Tony's local folders: orrery\n"
 'C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\\n'
 'gallery\n'
 'C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\\n'
 '\n'
 'Paste everything below the line into a new chat in the Orrery Project.\n'
 '\n'
 '---\n'
 '\n'
 "You are the coordinating session for Paloma's Orrery. The Project\n"
 'instructions and the skills are resident; follow them.\n'
 '\n'
 'Start the usual way:\n'
 '\n'
 "1. Pull both repositories at HEAD and record the SHAs. The orrery's\n"
 "   HEAD should hold the last session's close: the protocol reads\n"
 '   v3.145, documentation/PROMPT_coordinator_start_20261122_4.md exists,\n'
 "   and L-539 on the ledger says Tony's look, lines 8 to 14, is done. If\n"
 '   not, patch_L539_4_session_close.py was not run or not pushed; say so\n'
 '   before anything else.\n'
 '2. THE FIRST DUTY, before any other work. Five skills were bumped on\n'
 '   Nov 22 and Tony reinstalled them ("-- done"); no session has checked.\n'
 '   Load each from the account and compare its version line with the\n'
 "   protocol's manifest: horizons-orbital-mechanics 1.20,\n"
 '   gallery-cache-builder 1.21, gallery-assembler 1.5,\n'
 '   interactive-exhibit 1.45, safe-file-editing 1.15. The version line\n'
 '   and the manifest row are in the first lines; read no more of a skill\n'
 '   the work does not fire (Token Economy). A mismatch is Stale Skill =\n'
 '   Stop: tell Tony which skill, and which version loaded.\n'
 "3. Read documentation/WHERE_WE_ARE.md, then Tony's newest run-record\n"
 '   copy (documentation/WHERE_WE_ARE_*_run_record.md) for his notes.\n'
 '4. Read the night records in BOTH repositories. The orrery: its Horizons\n'
 '   check row reads NOTHING DUE until Nov 25, when 90 served identities\n'
 '   renew together, about 7 minutes of a 15-minute limit; a title that\n'
 '   starts JPL DIFFERS or NEW JPL NAME is the first thing to tell Tony.\n'
 "   NOAA's next El Nino update is expected 10 December 2026. The website:\n"
 '   59 rows, Room clock among them.\n'
 '\n'
 'Where things stand:\n'
 '\n'
 '- The skills bump is done: protocol v3.145, pushed at orrery 811cf44f.\n'
 "  The rules of three builds (the encounter, the rooms' clock, every\n"
 '  entry checked against JPL) are in five skills. Nothing in the\n'
 "  website's way remains but the check in step 2.\n"
 "- Tony's look in the orrery's window is done (L-539, L-512). The\n"
 '  animation with a Lagrange point plays, and the point is asked for no\n'
 '  orbit.\n'
 "- Haumea's two moons, from the same look (L-549, for a talk): each\n"
 "  orbit is drawn and labelled as JPL's, of Feb 2, for an id JPL has\n"
 '  since dropped; its two end markers say "typed value, not fetched\n'
 '  from JPL", all four dated the day of the plot; neither moon has a\n'
 '  marker of its own.\n'
 '\n'
 'Next, in this order:\n'
 '\n'
 "- L-544 (L4 and L5 tie), in the website: a tie-break in the drawer's\n"
 '  order where two distances agree to the digits a box prints, in the\n'
 "  page and in the gallery editor's tree. Method, not a ruling, and\n"
 '  small. Choose the smallest instrument and say why in one line (Token\n'
 '  Economy). Whatever changes the page runs both walks and names any\n'
 "  new row's dashboard button (interactive-exhibit 1.45, Phone first).\n"
 "- Then the protocol's reduction, step 3 of L-522 (document caps), in\n"
 '  its own Fable session, BEFORE L-538: Tony, Nov 22, 15:07, "Yes". He\n'
 '  starts it with documentation/HANDOFF_document_upkeep_20261116.md and\n'
 '  L-522; this session writes it no brief. Not beside a build.\n'
 "- Then L-538 (the orbiters' printed error), then the encounter's slice\n"
 '  2, its talk first (L-529).\n'
 "- Then step 4 of L-522, the ledger's closed items moved out by a tool,\n"
 '  at the next gap between builds; steps 5 and 6 the same way.\n'
 "- Waiting on Tony, on Where We Are: L-543 (the gallery's checks from a\n"
 '  push copy), L-545 (whether the walks join the gallery run), L-548 (a\n'
 '  missing id_type), and at a talk L-549 (the four moons).\n'
 '- Open on L-541, for an orrery session and a builder session: the\n'
 '  builder asks daily points 9 seconds before UTC midnight; its keys\n'
 "  and plan windows are read as UTC; the orrery's whole-second 69.\n"
 "- L-550 (a website check's dashboard button) closes at this session's\n"
 '  close, once interactive-exhibit 1.45 has loaded from the account.\n'
 '\n'
 'Lessons from the last session worth carrying:\n'
 '\n'
 '- A five-skill bump at the caps filled a session. What made it safe: a\n'
 '  builder script sliced every moved passage out of the pushed file, so\n'
 '  "word for word" was mechanical, and it counted each file against its\n'
 '  cap before the patch was written.\n'
 '- The caps forced two origin passages down to a sentence each.\n'
 '  gallery-cache-builder and horizons-orbital-mechanics have no plain\n'
 '  history left; their next bump costs a rule unless they are split\n'
 "  first (L-522, for step 3's close).\n"
 "- Before placing a patch, stage Tony's disk copies of the files it\n"
 '  edits and compare them with the pushed commit. Identical copies are\n'
 '  the proof the patch will run for him.\n'
 '- Reading a placed file back can fail once ("upload failed", then\n'
 '  "hardlinked") and succeed half a minute later. Wait and retry once\n'
 '  before doubting the placement.\n'
 '- A session cannot load a skill reinstalled during it. A bump is a\n'
 "  session's last job; the work that needs the new skill is the next\n"
 "  session's first.\n"
 "- Tony's look found what no check could: one picture giving two\n"
 "  sources for one orbit. Read his saved picture's file, not only his\n"
 '  answers; his "-- keplerian from typed values not jpl" was the end\n'
 "  markers' words, and the orbit's own words said JPL.\n"
 '\n'
 'Ask Tony one thing to begin: whether to go ahead with L-544 (L4 and\n'
 "L5 tie) as the session's work.\n")


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
                  "patch_L539_3_skills_bump.py has not run, run it first. "
                  "Otherwise the file moved since this was built: tell the "
                  "session. NOTHING was written." % (name, c, old[:70]))
            sys.exit(1)
        staged[name][0] = text.replace(o, n)
        print("ok   %s: %s" % (name, (old.strip().splitlines()
                                      or ['(end)'])[0][:52]))
    ppath = os.path.join(HERE, *PROMPT_PATH.split('/'))
    pbytes = PROMPT_TEXT.encode('ascii')
    write_prompt = True
    if os.path.exists(ppath):
        with open(ppath, 'rb') as f:
            have = f.read().replace(b'\r\n', b'\n')
        if have == pbytes:
            write_prompt = False
        else:
            print("ERROR: %s already exists and differs from the one this "
                  "patch places. Likely a copy saved by hand: delete it and "
                  "run again. NOTHING was written." % PROMPT_PATH)
            sys.exit(1)
    for name, (text, was_crlf) in staged.items():
        with open(os.path.join(HERE, *name.split('/')), 'wb') as f:
            f.write(text)
        if was_crlf:
            print("note: %s was CRLF in the working copy; written LF" % name)
    print("patch applied (%d edits, %d files)" % (len(EDITS), len(staged)))
    if write_prompt:
        with open(ppath, 'wb') as f:
            f.write(pbytes)
        print("wrote %s (%d bytes)" % (PROMPT_PATH, len(pbytes)))
    else:
        print("already there, identical: %s" % PROMPT_PATH)
    print("stamps updated: Where We Are's header (811cf44f)")
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
    print("Do next: move this file into documentation; commit and push")
    print("the orrery; start the next coordinating session with")
    print("documentation/PROMPT_coordinator_start_20261122_4.md, pasted")
    print("from below its line.")


if __name__ == '__main__':
    main()
