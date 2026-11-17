"""
patch_L060_4_session_close_20261117.py -- closes the El Nino session
(L-060): the page is live, the night's flag is fixed, and Where We Are
moves on to ESCAPADE.

Built on orrery f8a12290 at
https://github.com/tonylquintanilla/palomas_orrery (branch main) and
gallery 20e13fd1 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, read
Nov 17, 2026. Written by the coordinating session (Claude Opus 5.5)
under safe-file-editing 1.14 and ledger-and-session-records 1.23.

WHAT IT CHANGES (two files)

    LEDGER_CONSOLIDATED.md, L-060: a dated note (the page live, Tony's
      run record "all green", the title-flag fix of f8a1229 and its
      lesson); the last Gap marked superseded and a new one; the done
      Tony-action marked done. Then it runs ledger_index.py.
    documentation/WHERE_WE_ARE.md, by section, above the run-record
      marker only: the header, the box, road stage 15, and the marks
      reset on Settled, Signals and Where the details are.

    Each edit is checked at the line it replaces; your notes elsewhere
    are left alone. A file that already holds the result is reported
    and left alone. Nothing is written unless every edit finds its line.

RUN COMMAND

    Save in the orrery's root folder, open in VS Code, click Run.
    (python patch_L060_4_session_close_20261117.py)

    Success: "ok" lines, then "patch applied". Failure: one ERROR or
    ANCHOR FAIL line, and nothing is written.

Written November 17, 2026 with Anthropic's Claude Opus 5.5.
"""

import os
import subprocess
import sys

LEDGER = "LEDGER_CONSOLIDATED.md"
PAGE = os.path.join("documentation", "WHERE_WE_ARE.md")
MARKER = b"--- Your run record below this line"


def b(s):
    return s.encode("ascii")


NOTE = (
    "- **2026-11-17, LIVE** (the coordinating session, Claude Opus 5.5).\n"
    "  The page went live with Tony's push: website daa627b0, his pull at\n"
    "  20e13fd1. His run record, documentation/WHERE_WE_ARE_11-16-26_1231_\n"
    "  run_record.md: \"all green\".\n"
    "  - THE NIGHT'S FLAG, FIXED at f8a1229 (patch_L060_3). The orrery's\n"
    "    night of Nov 17 (c69b53b) titled itself EL NINO DUE while its El\n"
    "    Nino check row said CURRENT: night_title_flags() read every\n"
    "    row's verdict, and the El Nino check suite's own pass line names\n"
    "    EL NINO DUE. Each flag is now read from its own row only\n"
    "    (NIGHT_TITLE_FLAGS pairs 'El Nino check' with 'EL NINO DUE'). The\n"
    "    suite gains the night of Nov 17 itself as a case, 22 checks,\n"
    "    shown to fail on the old code. It runs from the dashboard's\n"
    "    existing \"El Nino Check Suite\" button; nothing new to add.\n"
    "  - The lesson: the suite tested the check's row alone, so it could\n"
    "    not see one row's words landing in another's flag. A check needs\n"
    "    an input shaped like the real night, every row together.\n"
)

NEW_GAP = (
    "**Gap (replaces the one above, 2026-11-17, close):** Tony's Mode 5\n"
    "look at the live page on his phone; the orrery's next night title\n"
    "must not start with EL NINO DUE while its El Nino check row says\n"
    "CURRENT. Then ESCAPADE's path (L-533).\n"
)

REF = ("**Ref:** ENSO_chart_spec.md v2 (design spec, this session); "
       "cross-ref L-001")

# (label, start of the line to replace, its whole new text with newline)
# A new text of None with an insert-before string is an insertion.
LEDGER_EDITS = [
    ("L-060: the Gap of Nov 17 marked superseded",
     "**Gap (replaces the one above, 2026-11-17):** Tony's phone look and his",
     "**Gap (superseded below, 2026-11-17):** Tony's phone look and his\n"),
    ("L-060: the done Tony-action marked done",
     "- Tony-action (do): read the preview on the phone; then commit and push",
     "- Tony-action (do), done Nov 17: read the preview on the phone; then commit and push\n"),
]
LEDGER_INSERT = ("L-060: the close note and new Gap", REF, NOTE + NEW_GAP)

PAGE_EDITS = [
    ("header: date",
     "Last updated: November 17, 2026: El Nino's page built",
     "Last updated: November 17, 2026: El Nino's page live, and the night's flag fixed (coordinating session, Opus).\n"),
    ("header: SHAs",
     "- Written at orrery 20a9c155 and gallery 1c5fe516",
     "- Written at orrery f8a12290 and gallery 20e13fd1, with this patch's edits on your disk.\n"),
    ("box: the page",
     "> - El Nino's page is built: five steps",
     "> - El Nino's page is live: the lobby's Featured card opens it, and the dashboard's Earth System group rebuilds it (L-060 (El Nino)).\n"),
    ("box: the night",
     "> - The night now checks NOAA:",
     "> - The night's \"EL NINO DUE\" title is fixed: it is read from the El Nino check's own row only. The night of Nov 17 said it by mistake; its row said CURRENT.\n"),
    ("box: do next",
     "> **Do next:** *Your phone look at El Nino's page",
     "> **Do next:** *ESCAPADE's path (L-533 (ESCAPADE)).*\n"),
    ("box: needs you now",
     "> - *(do) Read El Nino's preview on your phone",
     "> - *(do) Your phone look at the live El Nino page (the list in today's chat). Tomorrow, the orrery's night title should not start with \"EL NINO DUE\"; if it does, tell the next session.*\n"),
    ("road: stage 15",
     "               page (L-060 (El Nino)) built Nov 17, live on your push; then",
     "               page (L-060 (El Nino)) live Nov 17; next,\n"),
    ("marks: Settled",
     "## Settled  **>> UPDATED THIS SESSION**",
     "## Settled\n"),
    ("marks: Signals",
     "## Signals  **>> UPDATED THIS SESSION**",
     "## Signals\n"),
    ("marks: Where the details are",
     "## Where the details are  **>> UPDATED THIS SESSION**",
     "## Where the details are\n"),
]


def line_at(top, start):
    """(start index, end index) of the one line of top beginning with
    start, or None if there is not exactly one."""
    hits = []
    pos = 0
    while True:
        i = top.find(b"\n" + start, pos)
        if i < 0:
            break
        hits.append(i + 1)
        pos = i + 1
    if top.startswith(start):
        hits.insert(0, 0)
    if len(hits) != 1:
        return None
    s = hits[0]
    e = top.find(b"\n", s)
    return s, (len(top) if e < 0 else e + 1)


def plan(path, edits, insert=None, top_only=False):
    if not os.path.exists(path):
        print("ERROR: %s not found. Run this from the orrery's root folder "
              "(palomas_orrery_for_github). Nothing was written." % path)
        return False, None
    raw = open(path, "rb").read()
    text = raw.replace(b"\r\n", b"\n")
    if top_only:
        if text.count(MARKER) != 1:
            print("ERROR: the run-record marker is not on %s once. Nothing "
                  "was written." % path)
            return False, None
        top, marker, bottom = text.partition(MARKER)
    else:
        top, marker, bottom = text, b"", b""

    news = [b(new) for _, _, new in edits]
    if insert:
        news.append(b(insert[2]))
    if all(top.count(n) == 1 for n in news):
        print("already there, identical: %s" % path)
        return True, None

    for label, start, new in edits:
        span = line_at(top, b(start))
        if span is None:
            print("ANCHOR FAIL: %s in %s -- expected one line starting "
                  "with its text. Nothing was written." % (label, path))
            return False, None
        top = top[:span[0]] + b(new) + top[span[1]:]
        print("ok %s" % label)
    if insert:
        label, before, text_in = insert
        n = top.count(b(before))
        if n != 1:
            print("ANCHOR FAIL: %s in %s -- expected its anchor once, found "
                  "%d. Nothing was written." % (label, path, n))
            return False, None
        top = top.replace(b(before), b(text_in) + b(before))
        print("ok %s" % label)

    if any(c > 127 for n in news for c in n):
        print("ERROR: this patch's own text would add non-ASCII bytes to "
              "%s. Nothing was written." % path)
        return False, None
    if top_only and top.count(b"\n") > 130:
        print("ERROR: %s would stand over 130 lines above its marker (%d). "
              "Nothing was written." % (path, top.count(b"\n")))
        return False, None
    if b"\r\n" in raw:
        print("note: %s was CRLF in the working copy; written LF" % path)
    return True, top + marker + bottom


def main():
    if os.path.basename(os.getcwd()).lower() == "documentation":
        print("ERROR: run this from the orrery's root folder, not from "
              "documentation\\. Nothing was written.")
        return 1
    ok, led = plan(LEDGER, LEDGER_EDITS, insert=LEDGER_INSERT)
    if not ok:
        return 1
    ok, page = plan(PAGE, PAGE_EDITS, top_only=True)
    if not ok:
        return 1
    if led is None and page is None:
        print("Nothing to do.")
        return 0
    if led is not None:
        with open(LEDGER, "wb") as f:
            f.write(led)
        print("ok %s written" % LEDGER)
    if page is not None:
        with open(PAGE, "wb") as f:
            f.write(page)
        print("ok %s written" % PAGE)
    if led is not None:
        print("Running ledger_index.py ...")
        r = subprocess.run([sys.executable, "ledger_index.py"],
                           capture_output=True, text=True)
        for line in (r.stdout + r.stderr).strip().splitlines()[-6:]:
            print("  " + line)
        if r.returncode != 0:
            print("ERROR: ledger_index.py exited %d. The edits above are "
                  "written; Discard Changes in GitHub Desktop undoes them. "
                  "Paste these lines to the session." % r.returncode)
            return 1
        print("ok ledger_index.py")
    print("patch applied")
    print("")
    print("Do next:")
    print("  1. (do) Move this file into documentation\\.")
    print("  2. (do) In GitHub Desktop (orrery): commit and push the ledger,")
    print("     Where We Are and this file. Not while the night is running.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
