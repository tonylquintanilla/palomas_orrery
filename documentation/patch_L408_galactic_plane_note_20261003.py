#!/usr/bin/env python3
"""
patch_L408_galactic_plane_note_20261003.py -- ORRERY repo. Records
Tony's last request of the session: a Galactic Plane toggle in the Sun
room, for the next session to build (L-408).

RUN IT AFTER patch_L371_session_close_20261003.py AND ITS MAINTENANCE
RUN. It was built on the files those two leave, from orrery
fd508f9c7794e3a51b22a4e1e3aa3a54c3e339ef
at https://github.com/tonylquintanilla/palomas_orrery
(gallery 52659e04b38dd773aa14b6e6e9e1a533bff114e7
at https://github.com/tonylquintanilla/tonyquintanilla.github.io;
not touched).

WHAT CHANGES
    LEDGER_CONSOLIDATED.md   L-408 opened: the toggle, as Tony
        confirmed it -- one row "Galactic Plane", off by default; a
        faint ring in the galaxy's plane at 100,000 AU and the galactic
        pole axis; from the tide's own pole rows, no new numbers; words
        to Tony before the build.
    documentation/HANDOFF_L406_L407_L371_session_20261003.md   the
        toggle added as item 2 of section 4.
    documentation/WHERE_WE_ARE.md   the toggle in "Do next" and in the
        next three steps.

No code changes.

HOW TO RUN IT
    Save this file in the ORRERY repo ROOT (next to palomas_orrery.py),
    open it in VS Code and click Run. The same as:
        python patch_L408_galactic_plane_note_20261003.py

SUCCESS looks like: one "ok" line per edit, then "patch applied".
FAILURE looks like: one ERROR: or ANCHOR FAIL: line, and NOTHING is
written. Undo is Discard Changes in GitHub Desktop.

Written October 3, 2026 with Anthropic's Claude Opus 5.5.
"""

import hashlib
import os

BASE = {'LEDGER_CONSOLIDATED.md': 'b5406cf114c24e7af6da0838265271ab',
 'documentation/HANDOFF_L406_L407_L371_session_20261003.md': '0e14d53bf5c190bfb7bd0b5105b80b58',
 'documentation/WHERE_WE_ARE.md': '8d29dd2f80cf5f4bf71ebebf34741c9b'}

EDITS = {'LEDGER_CONSOLIDATED.md': [('L-408 new item',
                             "#### [L-407] A skill's header is checked as "
                             'YAML (orrery, skills)\n',
                             '#### [L-408] A Galactic Plane toggle in the '
                             "Sun room (gallery, the Sun's slice)\n"
                             '<!-- L:408 status:OPEN upd:2026-10-03 '
                             'section:A flag: rice: -->\n'
                             '- **Asked 2026-10-03** by Tony, looking for '
                             "the galactic tide's X on\n"
                             '  the phone and not finding it at the angle he '
                             'had: "Could we toggle on\n'
                             '  the galactic plane and axis?" Claude agreed '
                             'it earns its place: it\n'
                             "  makes the tide's tilt legible at a glance, "
                             'and teaches on its own\n'
                             '  that the solar system is tipped steeply '
                             'against the galaxy.\n'
                             '- **The design Tony confirmed ("Yes '
                             'please"):** one new row in the\n'
                             '  Oort Cloud group, "Galactic Plane", off by '
                             'default; a faint ring in\n'
                             "  the galaxy's plane at the tide's outer edge "
                             '(`OUTER_OORT_CLOUD_AU`,\n'
                             '  100,000 AU) and a line along the galactic '
                             'pole axis through the Sun;\n'
                             '  no new numbers -- it reads the same two pole '
                             'rows the tide reads\n'
                             '  (`GALACTIC_NORTH_POLE_RA_J2000_DEG`, '
                             '`_DEC_J2000_DEG`), so the ring\n'
                             '  and the tide cannot disagree; hover and info '
                             'panel words to Tony\n'
                             '  before the build. Left out for now: the '
                             "direction to the galaxy's\n"
                             '  centre, which needs one more sourced '
                             'number.\n'
                             "**Gap:** Build it next session, with the Sun's "
                             'distance cards (L-371):\n'
                             'gallery first; whether the orrery gets the '
                             'same toggle is asked then.\n'
                             '**Ref:** L-406; gallery '
                             '`gallery/feature_renderers.js`,\n'
                             '`data/objects_config.json`.\n'
                             '\n'
                             "#### [L-407] A skill's header is checked as "
                             'YAML (orrery, skills)\n')],
 'documentation/HANDOFF_L406_L407_L371_session_20261003.md': [('section 4: '
                                                               'the Galactic '
                                                               'Plane toggle',
                                                               "2. **Tony's "
                                                               'Mode 5 look '
                                                               'at the '
                                                               'tide**, if '
                                                               'not done:',
                                                               '2. **The '
                                                               'Galactic '
                                                               'Plane toggle '
                                                               '(L-408)**, '
                                                               'added at the '
                                                               "session's "
                                                               'end\n'
                                                               "   at Tony's "
                                                               'request: a '
                                                               'ring in the '
                                                               "galaxy's "
                                                               'plane at '
                                                               '100,000 AU '
                                                               'and\n'
                                                               '   the '
                                                               'galactic '
                                                               'pole axis, '
                                                               'one row, off '
                                                               'by default, '
                                                               'from the '
                                                               "tide's own\n"
                                                               '   pole '
                                                               'rows. Words '
                                                               'to Tony '
                                                               'before the '
                                                               'build. It '
                                                               'will also '
                                                               'make item 3\n'
                                                               '   easy.\n'
                                                               "3. **Tony's "
                                                               'Mode 5 look '
                                                               'at the '
                                                               'tide**, if '
                                                               'not done:'),
                                                              ('section 4: '
                                                               'renumbered',
                                                               '3. The '
                                                               "drawer's "
                                                               'small fixes '
                                                               'and the Home '
                                                               'design talk, '
                                                               'as the',
                                                               '4. The '
                                                               "drawer's "
                                                               'small fixes '
                                                               'and the Home '
                                                               'design talk, '
                                                               'as the')],
 'documentation/WHERE_WE_ARE.md': [('next steps: the Galactic Plane',
                                    "2. The drawer's small fixes: the info "
                                    "panel's bullet lists, the 1.1",
                                    '2. *A Galactic Plane toggle in the Sun '
                                    'room, your idea:* a faint ring\n'
                                    "   in the galaxy's plane and the "
                                    "galaxy's pole axis, so the tide's\n"
                                    '   tilt and its X can be seen at a '
                                    'glance.\n'
                                    "3. The drawer's small fixes: the info "
                                    "panel's bullet lists, the 1.1"),
                                   ('next steps: Home folded into step 3',
                                    '3. What Home should do, settled in '
                                    'conversation, then built.',
                                    '   Then what Home should do, settled in '
                                    'conversation and built.'),
                                   ('do next: the toggle too',
                                    "> - *Build the Sun's distance cards so "
                                    'every number prints at its\n'
                                    ">   source's figures.*\n",
                                    "> - *Build the Sun's distance cards so "
                                    'every number prints at its\n'
                                    ">   source's figures.*\n"
                                    '> - *Then the Galactic Plane toggle you '
                                    'asked for.*\n')]}


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
    for path in {}:
        if os.path.exists(path):
            raise SystemExit("ERROR: %s already exists. If this patch already "
                             "ran, it has nothing left to do. NOTHING was "
                             "written." % path)
    results = []
    for path in sorted(EDITS):
        with open(path, "rb") as handle:
            raw = handle.read()
        got = fingerprint(raw)
        if got != BASE[path]:
            raise SystemExit(
                "ERROR: %s is not the file this patch was built against.\n"
                "       expected %s, found %s. It has changed since\n"
                "       what patch_L371_session_close and its\n"
                "       maintenance run leave, or this patch has already run.\n"
                "       (Line endings are excluded, so they are not the cause.)\n"
                "       NOTHING was written." % (path, BASE[path], got))
        nl = "\r\n" if b"\r\n" in raw else "\n"
        text = raw.decode("utf-8").replace("\r\n", "\n")
        done = []
        for label, old, new in EDITS[path]:
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
    for path, content in sorted({}.items()):
        with open(path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(content)
        print("ok  %s created" % path)
    print("")
    print("patch applied")
    print("")
    print("NEXT:")
    print("  1. Run orrery_maintenance_run.py (VS Code, Run). It adds")
    print("     L-408 to the ledger's index. Expect 20 of 20.")
    print("  2. Move this script into documentation/; commit and push --")
    print("     in the same commit as the closing patch is fine.")

if __name__ == "__main__":
    main()
