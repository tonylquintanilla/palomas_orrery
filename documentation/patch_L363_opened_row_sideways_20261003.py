#!/usr/bin/env python3
"""
patch_L363_opened_row_sideways_20261003.py -- ORRERY repo. Records
Tony's Mode 5 look at an opened drawer row with the phone sideways, and
his ruling on the fix (L-363). Nothing is built; the fix goes in with
the drawer's small fixes.

Built on orrery 4246a1a4df81fdae0430c4cfc4e553618803e999
at https://github.com/tonylquintanilla/palomas_orrery
(gallery 52659e04b38dd773aa14b6e6e9e1a533bff114e7
at https://github.com/tonylquintanilla/tonyquintanilla.github.io;
not touched).

WHAT CHANGES
    LEDGER_CONSOLIDATED.md   L-363: what Tony saw (an opened row does
        not fit the drawer sideways), why (the drawer is at most 40% of
        the picture's height, and nothing scrolls an opened row into
        view), and his ruling -- sideways, the Enter button on the
        name's line; an opened row scrolled into view as the backup.
    documentation/HANDOFF_L406_L407_L371_session_20261003.md   section
        4, item 3: the look done, the fix chosen.
    documentation/WHERE_WE_ARE.md   "Right now" and the next steps.

No code changes.

WHY TWO FILES ARE CHECKED BY THEIR ANCHORS ONLY
    Tony writes his own notes into the handoff and into Where We Are
    (run records, SHAs, comments), so those two files differ from the
    pushed copy on his machine. The first copy of this patch checked
    them whole and refused, correctly, on his notes. Now the ledger is
    still checked whole; the two notes files are checked by their
    anchors -- each must be found exactly once -- and the patch refuses
    if its own text is already there.

HOW TO RUN IT
    Save this file in the ORRERY repo ROOT (next to palomas_orrery.py),
    open it in VS Code and click Run. The same as:
        python patch_L363_opened_row_sideways_20261003.py

SUCCESS looks like: one "ok" line per edit, then "patch applied".
FAILURE looks like: one ERROR: or ANCHOR FAIL: line, and NOTHING is
written. Undo is Discard Changes in GitHub Desktop.

Written October 3, 2026 with Anthropic's Claude Opus 5.5.
"""

import hashlib
import os

BASE = {'LEDGER_CONSOLIDATED.md': '461ecf600e4000a7caaae84b00b45e76', 'documentation/HANDOFF_L406_L407_L371_session_20261003.md': None, 'documentation/WHERE_WE_ARE.md': None}

EDITS = {'LEDGER_CONSOLIDATED.md': [('L-363: an opened row sideways', '<!-- L:363 status:OPEN upd:2026-10-03 section:A flag: rice: -->\n- **2026-10-03, Home settled (Tony, from his phone).**', '<!-- L:363 status:OPEN upd:2026-10-03 section:A flag: rice: -->\n- **2026-10-03, an opened row with the phone sideways (Tony\'s Mode 5).**\n  The look the 2026-10-02 handoff left open ("not clear"). Sideways, the\n  drawer -- at most 40% of the picture\'s height (`.sun-drawer`\n  max-height) -- shows about a row and a half, so an opened row, its\n  name line plus "Enter the <n> room", does not fit: Earth\'s name line\n  is cut off at the top (Tony\'s screenshot, 4 Oct 2026 01:06 UTC). No\n  code scrolls an opened row into view. Tony\'s ruling, of three ways:\n  - **Option 3, chosen ("yes, 3"):** sideways, the Enter button sits on\n    the name\'s line, between the name and GO, so an opened row stays\n    one line tall.\n  - **Option 2, as the backup:** opening a row scrolls it fully into\n    view, upright too. Tony: "even 2 is not enough for landscape view.\n    although it is almost enough. so, as a backup, yes."\n  - Option 1, a taller drawer sideways, not chosen.\n  Built with the drawer\'s small fixes. What counts as sideways is the\n  build\'s to propose from the page\'s own phone test\n  (`sunPhonePortrait`), and Tony judges it at Mode 5.\n- **2026-10-03, a patch must allow Tony\'s notes.** The first copy of\n  the patch recording the ruling above refused on Tony\'s machine: it\n  checked the handoff whole, and Tony had written his run record and\n  the pushed SHA into it, as he does. Tony: \"wait, so i can\'t annotate\n  the documentation??\" He can; the patch was wrong. Carried to the\n  next ledger-and-session-records version (A Wrong Sentence in a\n  Skill: Carry It): a patch checks the files Tony writes notes into --\n  handoffs, Where We Are -- by the lines it edits, each found exactly\n  once, and refuses if its own text is already there; whole-file\n  fingerprints stay for files only patches and generators write.\n- **2026-10-03, Home settled (Tony, from his phone).**')], 'documentation/HANDOFF_L406_L407_L371_session_20261003.md': [('section 4: the opened-row fix', "3. The drawer's small fixes, as the 2026-10-02 handoff lists them,\n   and Home as Tony settled it from his phone on 2026-10-03 (L-363).\n", "3. The drawer's small fixes, as the 2026-10-02 handoff lists them,\n   and Home as Tony settled it from his phone on 2026-10-03 (L-363).\n   Tony's second look at an opened row is done: sideways it does not\n   fit, and he chose the fix -- the Enter button on the name's line,\n   and an opened row scrolled into view as a backup (L-363).\n")], 'documentation/WHERE_WE_ARE.md': [('next steps: the opened-row fix', '   that should say 1.2, and your second look at an opened row.\n', "   that should say 1.2, and an opened row made to fit with the phone\n   sideways: its Enter button on the name's line, as you chose.\n"), ('right now: the opened row', '  shows no visible change when it falls back to an earlier body.\n', '  shows no visible change when it falls back to an earlier body, and\n  with the phone sideways an opened row does not fit in the drawer.\n')]}


def fingerprint(raw):
    return hashlib.md5(raw.replace(b"\r\n", b"\n")).hexdigest()


def main():
    if os.path.basename(os.getcwd()) == "documentation":
        raise SystemExit("ERROR: run this from the ORRERY repo ROOT, next to "
                         "palomas_orrery.py -- not from documentation/. "
                         "NOTHING was written.")
    if not os.path.isfile("palomas_orrery.py"):
        raise SystemExit("ERROR: palomas_orrery.py is not here, so this is "
                         "not the orrery root. NOTHING was written.")
    results = []
    for path in sorted(EDITS):
        with open(path, "rb") as handle:
            raw = handle.read()
        got = fingerprint(raw)
        if BASE[path] is not None and got != BASE[path]:
            raise SystemExit(
                "ERROR: %s is not the file this patch was built against.\n"
                "       expected %s, found %s. It has changed since\n"
                "       4246a1a4, or this patch has already run.\n"
                "       (Line endings are excluded, so they are not the cause.)\n"
                "       NOTHING was written." % (path, BASE[path], got))
        nl = "\r\n" if b"\r\n" in raw else "\n"
        text = raw.decode("utf-8").replace("\r\n", "\n")
        done = []
        for label, old, new in EDITS[path]:
            if BASE[path] is None and new in text:
                raise SystemExit("ERROR: %s already carries this patch's text "
                                 "(%s), so the patch has already run. NOTHING "
                                 "was written." % (path, label))
            if text.count(old) != 1:
                raise SystemExit("ANCHOR FAIL (%s): expected 1 match in %s, "
                                 "found %d. NOTHING was written."
                                 % (label, path, text.count(old)))
            text = text.replace(old, new)
            done.append(label)
        if any(ord(ch) > 127 for ch in text):
            raise SystemExit("ERROR: %s would hold non-ASCII text. NOTHING "
                             "was written." % path)
        results.append((path, text.replace("\n", nl), done))
    for path, text, done in results:
        with open(path, "wb") as handle:
            handle.write(text.encode("utf-8"))
        for label in done:
            print("ok  %-40s %s" % (path, label))
    print("")
    print("patch applied")
    print("")
    print("NEXT:")
    print("  1. Run orrery_maintenance_run.py (VS Code, Run). Expect 20 of 20.")
    print("  2. Move this script into documentation/; commit and push.")


if __name__ == "__main__":
    main()
