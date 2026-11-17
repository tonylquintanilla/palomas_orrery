"""
patch_L060_2_el_nino_words_20261116.py -- records for the El Nino page's
shape and words, Nov 16 afternoon and evening (the coordinating
session, Claude Opus 5.5). Records only; no code.

Built on orrery 13ff1feb8ce29107ad20e37354b260df69f1017c at
https://github.com/tonylquintanilla/palomas_orrery (branch main) and
gallery 1c5fe516cebaa7b239d34c7573f66a0f6099cc90 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, and
checked against your local ledger, which matched GitHub. Written under
ledger-and-session-records 1.23 and safe-file-editing 1.14.

Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\
and gallery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\

WHAT IT CHANGES (one file)

    LEDGER_CONSOLIDATED.md, L-060 (El Nino): a second dated note for
    Nov 16 with your rulings of the afternoon and evening (the walk;
    step 2 in the scientists' words; RONI alone; step 3's sentence on
    other agencies on three conditions; step 5 on NOAA alone), what
    the build takes from the two reviews, and a new Gap. The morning's
    Gap is marked superseded. Then it runs ledger_index.py.

    Where We Are is not edited: its Do next (El Nino's brief, then its
    Code session) still holds, and it stands at its 130-line cap.

RUN COMMAND

    Save in the orrery's root folder, open in VS Code, click Run.
    (python patch_L060_2_el_nino_words_20261116.py)

    Success: one "ok" line per edit, the index tool's last lines, then
    "patch applied". A second run says "already there". Failure: one
    ERROR or ANCHOR FAIL line, and nothing is written.

Written November 16, 2026 with Anthropic's Claude Opus 5.5.
"""

import os
import subprocess
import sys

LEDGER = "LEDGER_CONSOLIDATED.md"
MARKER = b"--- Your run record below this line"


def b(s):
    return s.encode("ascii")


NOTE = '- **2026-11-16, afternoon and evening: THE PAGE\'S SHAPE AND WORDS,\n  AFTER TWO OUTSIDE REVIEWS** (the same coordinating session, Claude\n  Opus 5.5, from Tony\'s phone). In Tony\'s words:\n  - 12:45, "i think A": the page is a walk in five steps (what El Nino\n    is; since 1950 in one line; this year so far; what NOAA expects;\n    why the whole planet feels it), not chart-first. The mockup is the\n    claude.ai artifact "El Nino page mockup",\n    https://claude.ai/artifact/8dr1qD8XGuKSiEJLR4eFv3, board A.\n  - 15:54, "Yes": step 2 rests on the scientists\' own words (van\n    Oldenborgh and others 2021, quoted and cited), not a paraphrase.\n  - 16:09: Tony asked for a Mode 7 review, not being expert enough to\n    judge how to present the science. Two legs: Gemini, then GPT, the\n    second on the revised words. Reviews:\n    documentation/REVIEW_L060_gemini_worksheet_20261116.md and\n    documentation/REVIEW_L060_gpt_worksheet_20261116.md. Gemini\'s leg:\n    four quotations not in their sources and wrong ONI figures; GPT\'s\n    quotations held up, and it found two errors in the revised words.\n  - 16:56, "we decided to use noaa for our authority so we will stay\n    with that decision": RONI alone on the chart; the older ONI is not\n    drawn (RONI official from February 1, 2026; NOAA keeps the ONI\n    files for continuity, NWS Public Information Statement 26-05).\n  - 19:00, "Yes", on Claude Fable\'s recommendation of 18:17 relayed by\n    Tony: step 3 keeps one sentence naming other agencies\' records\n    only to say they are not this page\'s record (Japan\'s agency on\n    NINO.3 for a single month; the WMO\'s forecast), on three\n    conditions: no outside figures on the page; "other agencies", not\n    "the news"; the WMO\'s statement called a forecast. Both agencies\n    appear only in the sources line. Step 5 rests on NOAA alone (a 2\n    to 3 month delay of global temperature, climate.gov), within the\n    NOAA-only ruling.\n  - For the build, from the reviews: read NOAA\'s files fresh, never\n    through a cache (a web fetch served RONI.ascii.txt ending at JAS\n    2026 on the day the file held ASO 2026 +1.97); RONI.ascii.txt is\n    NOAA\'s own named file for the index (PNS 26-05); step 4\'s chances\n    come from roni/probabilities/; NOAA\'s ~60% is stated with its own\n    threshold (+2.5 or more) and date, never as the chance of passing\n    +2.40; the page\'s promise to redraw after each monthly update (the\n    second Thursday) is the build\'s to keep.\n**Gap (replaces the one above, 2026-11-16 evening):** the brief for El\nNino\'s Code session, written from the mockup\'s words, the two reviews\nand what still holds of the June spec; then the build, Tony\'s phone\nlook, and his reading of every word before it goes live. Then\nESCAPADE\'s path (L-533).\n'

LEDGER_EDITS = [
    ("L-060: the morning's Gap marked superseded",
     b("**Gap (replaces the one above, 2026-11-16):** the brief for El Nino's\n"),
     b("**Gap (superseded below, 2026-11-16 evening):** the brief for El Nino's\n")),
    ("L-060: the evening note and new Gap",
     b("**Ref:** ENSO_chart_spec.md v2 (design spec, this session); "
       "cross-ref L-001"),
     b(NOTE) + b("**Ref:** ENSO_chart_spec.md v2 (design spec, this "
                 "session); cross-ref L-001")),
]


def whole_line(top, start_text):
    """The full line of top that starts with start_text, with its newline."""
    i = top.find(b"\n" + start_text)
    if i < 0 or top.find(b"\n" + start_text, i + 1) >= 0:
        return None
    j = top.find(b"\n", i + 1)
    return top[i + 1:j + 1]


def plan(path, edits, top_only=False):
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

    def done(old, new):
        if new is None:
            return whole_line(top, old) is None and top.count(old) == 0
        return top.count(new) == 1

    if all(done(old, new) for _, old, new in edits):
        print("already there, identical: %s" % path)
        return True, None
    for label, old, new in edits:
        if new is None:
            line = whole_line(top, old)
            if line is None:
                print("ANCHOR FAIL: %s in %s -- expected its line once. "
                      "Nothing was written." % (label, path))
                return False, None
            top = top.replace(line, b"")
            print("ok %s" % label)
            continue
        n = top.count(old)
        if n != 1:
            print("ANCHOR FAIL: %s in %s -- expected its text once, found "
                  "%d. Nothing was written." % (label, path, n))
            return False, None
        top = top.replace(old, new)
        print("ok %s" % label)
    out = top + marker + bottom
    added = b"".join(new for _, _, new in edits if new)
    if any(c > 127 for c in added):
        print("ERROR: this patch's own text would add non-ASCII bytes to "
              "%s. Nothing was written." % path)
        return False, None
    if top_only and top.count(b"\n") > 130:
        print("ERROR: %s would stand over 130 lines above its marker (%d). "
              "Nothing was written." % (path, top.count(b"\n")))
        return False, None
    if b"\r\n" in raw:
        print("note: %s was CRLF in the working copy; written LF" % path)
    return True, out



def main():
    if os.path.basename(os.getcwd()).lower() == "documentation":
        print("ERROR: run this from the orrery's root folder, not from "
              "documentation\\. Nothing was written.")
        return 1
    ok, led = plan(LEDGER, LEDGER_EDITS)
    if not ok:
        return 1
    if led is None:
        print("Nothing to do.")
        return 0
    with open(LEDGER, "wb") as f:
        f.write(led)
    print("ok %s (%d edits)" % (LEDGER, len(LEDGER_EDITS)))
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
    print("  2. (do) In GitHub Desktop (orrery): commit and push the ledger, "
          "this file, the GPT prompt and worksheet, and the two reviews "
          "(the Gemini prompt and worksheet are already pushed). Not while "
          "the website's night is running.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
