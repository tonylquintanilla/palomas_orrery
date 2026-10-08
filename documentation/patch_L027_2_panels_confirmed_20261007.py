#!/usr/bin/env python3
"""
patch_L027_2_panels_confirmed_20261007.py -- ORRERY repo. Records
Tony's two rulings of 2026-10-07: the panels' grey is confirmed (L-027),
and the phone's galactic-plane question waits for the design talk
(L-408).

Built on orrery 8653ef1b at
https://github.com/tonylquintanilla/palomas_orrery (gallery not read or
changed). No code changes: records only.

L-027 stays OPEN for one check only a later session can make: that its
loaded copy of the agentic-pre-test skill reads 1.3. A reinstall is not
visible to the session that made it, so this one cannot make it.

HOW TO RUN IT
    Save this file in the ORRERY repo ROOT, open it in VS Code and click
    Run. Then follow the NEXT steps it prints.

WHAT CHANGES
    LEDGER_CONSOLIDATED.md   a header stamp; L-027's status date and Gap;
        one line on L-408. Matched only at those lines.
    documentation/HANDOFF_L420_galactic_plane_20261006.md   one Where We
        Are line and one Next session line.

TESTED on a copy of 8653ef1b: every edit landed; the maintenance run
passed every gating checker; a second run refused and wrote nothing.

SUCCESS looks like: one "ok" line per edit, then "patch applied".
FAILURE looks like: one ANCHOR FAIL: or ERROR: line, and NOTHING is
written. Undo is Discard Changes in GitHub Desktop.

Written October 7, 2026 with Anthropic's Claude Opus 5.5.
"""

import os

ROOT_MARKERS = ("palomas_orrery.py", "LEDGER_CONSOLIDATED.md")
NEXT = ["1. Move this script into documentation/ first.",
        "2. Run orrery_maintenance_run.py.",
        "3. Commit and push."]

EDITS = {
  "LEDGER_CONSOLIDATED.md": [
    ("header stamp",
     ("(L-395: the Horizons check designed and tested by hand; Encke's list\n"
      "entry ruled), built on 12693a53.\n"),
     "(L-395: the Horizons check designed and tested by hand; Encke's list\n"
     "entry ruled), built on 12693a53.\n"
     "Module updated: October 7, 2026 with Anthropic's Claude Opus 5.5\n"
     "(L-027: the panels' grey confirmed; L-408 waits for the design talk),\n"
     "built on 8653ef1b.\n"),
    ("L-027 date",
     "<!-- L:027 status:OPEN upd:2026-10-06 section:D.Structural flag: rice:3/2/75/2 -->\n",
     "<!-- L:027 status:OPEN upd:2026-10-07 section:D.Structural flag: rice:3/2/75/2 -->\n"),
    ("L-027 panels confirmed",
     ("**Gap:** Tony's look at the panels on Windows (back to the grey of\n"
      "January to June, a shade darker than Windows' own); the next session\n"
      "confirms its loaded copy of agentic-pre-test reads 1.3. A run on a\n"
      "Mac would settle the last system; macOS has not been tried since\n"
      "Tony's test.\n"),
     ("- **The panels' grey confirmed, 2026-10-07.** Tony: \"gray90 is\n"
      "  confirmed.\"\n"
      "- **A run on a Mac, struck as a condition for closing.** gray90 is a\n"
      "  colour name Tk knows on every system, it is the grey Tony ran on\n"
      "  macOS while it held from January to June, and the headless\n"
      "  pre-test now fails if a one-system colour name returns. A Mac run\n"
      "  is still welcome; nothing waits on it.\n"
      "**Gap:** a later session confirms its loaded copy of agentic-pre-test\n"
      "reads 1.3, then closes this item. The session that bumped it loaded\n"
      "1.2 and cannot see the reinstall.\n")),
    ("L-408 awaits the design talk",
     ("**Gap:** the Sun slice's eighth item (L-412): Tony's design decision\n"
      "on whether the phone draws the galactic plane, Sgr A*, and the tide's\n"
      "cone and brightness; then the gallery build.\n"),
     ("- **2026-10-07:** Tony, on the phone's question: \"awaits the design\n"
      "  talk.\"\n"
      "**Gap:** the Sun slice's eighth item (L-412): Tony's design decision,\n"
      "at the design talk, on whether the phone draws the galactic plane,\n"
      "Sgr A*, and the tide's cone and brightness; then the gallery build.\n")),
  ],
  "documentation/HANDOFF_L420_galactic_plane_20261006.md": [
    ("Where We Are: panels done",
     ("- Needs Tony: a look at the panels on Windows, a shade darker than\n"
      "  before; and, when convenient, a run on a Mac.\n"),
     ("- Needs Tony: a look at the panels on Windows, a shade darker than\n"
      "  before; and, when convenient, a run on a Mac.\n"
      "- Done (2026-10-07): the panels' grey confirmed. The phone's\n"
      "  galactic-plane question waits for the design talk.\n")),
    ("Next session: L-027",
     ("- Close L-027 on Tony's run and look; confirm agentic-pre-test 1.3\n"
      "  loaded.\n"),
     ("- Confirm the loaded agentic-pre-test reads 1.3, then close L-027;\n"
      "  Tony confirmed the panels 2026-10-07.\n")),
  ],
}


def read_lf(path):
    with open(path, "rb") as handle:
        raw = handle.read()
    return raw.decode("utf-8").replace("\r\n", "\n"), b"\r\n" in raw


def main():
    if os.path.basename(os.getcwd()) == "documentation":
        raise SystemExit("ERROR: run this from the repo ROOT, not from "
                         "documentation/. NOTHING was written.")
    for marker in ROOT_MARKERS:
        if not os.path.isfile(marker):
            raise SystemExit("ERROR: %s is not here, so this is not the "
                             "orrery root. NOTHING was written." % marker)
    results = []
    for path in sorted(EDITS):
        if not os.path.isfile(path):
            raise SystemExit("ERROR: %s is not here. NOTHING was written." % path)
        text, crlf = read_lf(path)
        done = []
        for label, old, new in EDITS[path]:
            found = text.count(old)
            if found != 1:
                raise SystemExit("ANCHOR FAIL (%s): expected 1 match in %s, "
                                 "found %d. Has this patch already run? "
                                 "NOTHING was written." % (label, path, found))
            text = text.replace(old, new)
            done.append(label)
        results.append((path, text, done, crlf))
    for path, text, done, crlf in results:
        with open(path, "wb") as handle:
            handle.write(text.encode("utf-8"))
        if crlf:
            print("note: %s was CRLF in the working copy; written LF" % path)
        for label in done:
            print("ok  %-56s %s" % (path, label))
    print("")
    print("patch applied")
    print("")
    print("NEXT:")
    for line in NEXT:
        print("  " + line)


if __name__ == "__main__":
    main()
