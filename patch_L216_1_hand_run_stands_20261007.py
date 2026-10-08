#!/usr/bin/env python3
"""
patch_L216_1_hand_run_stands_20261007.py -- ORRERY repo. Records Tony's
two statements of 2026-10-07 on L-216: the daily hand run, with its four
checks, is his working practice, with no automation planned; and the
Daily Run now pauses OneDrive before the cache build. Sessions stop
proposing a schedule or a move off OneDrive.

Built on orrery 8653ef1b593aaf3835ecbcf2186b9e3e28a28089 at
https://github.com/tonylquintanilla/palomas_orrery. The gallery was read
at 4cfeca27 (daily_run.py and data/cache_swap_log.jsonl) and is not
changed. No
code changes: records only.

HOW TO RUN IT
    Save this file in the ORRERY repo ROOT (next to palomas_orrery.py),
    open it in VS Code and click Run (the command is
    python patch_L216_1_hand_run_stands_20261007.py). Then follow the
    NEXT steps it prints. It runs before or after today's other patches
    (patch_L027_2, patch_L418_2, patch_L412_1, patch_L001_1): it edits
    lines none of them touch.

WHAT CHANGES
    LEDGER_CONSOLIDATED.md   a header stamp; L-216's date; Tony's two
        statements, one note and a shorter Gap. Matched only at those
        lines (L-419).
    Permanent: the ledger lines. The script is spent once it has run.

TESTED on a copy of 8653ef1b: every edit landed; ledger_index.py --check
reported no consistency problems; a second run refused and wrote
nothing; the four patches above still found their anchors afterwards.

SUCCESS looks like: one "ok" line per edit, then "patch applied".
FAILURE looks like: one ANCHOR FAIL: or ERROR: line, and NOTHING is
written. Undo is Discard Changes in GitHub Desktop.

Written October 7, 2026 with Anthropic's Claude Fable 5.1.
"""

import os

LEDGER = "LEDGER_CONSOLIDATED.md"
ROOT_MARKERS = ("palomas_orrery.py", LEDGER)
NEXT = ["1. Move this script into documentation/.",
        "2. Run orrery_maintenance_run.py (it rebuilds the ledger's index).",
        "3. Commit and push."]

EDITS = [
    ("header stamp",
     "Review and RICE update Tony 6-21-2026\n",
     "Module updated: October 7, 2026 with Anthropic's Claude Fable 5.1\n"
     "(L-216: the daily hand run stands as Tony's practice, pausing OneDrive\n"
     "24 hours first; the swap retry proven twice in the log; a close for\n"
     "Tony to decide), built on 8653ef1b.\n"
     "Review and RICE update Tony 6-21-2026\n"),
    ("L-216 date",
     "<!-- L:216 status:OPEN upd:2026-10-04 section:A flag: rice:3/3/85/2 -->\n",
     "<!-- L:216 status:OPEN upd:2026-10-07 section:A flag: rice:3/3/85/2 -->\n"),
    ("L-216 Tony's words and Gap",
     "unproven. The empty \" (N)\" folders are a second, smaller symptom with the\n"
     "same suspected cause and no known harm. The move off OneDrive is Tony's\n"
     "and is UNDECIDED; the analysis, the inventory and what a move would need\n"
     "first are in the 2026-09-20 notes above.\n",
     "unproven. The empty \" (N)\" folders are a second, smaller symptom with the\n"
     "same suspected cause and no known harm.\n"
     "**Tony, 2026-10-07:** \"on the daily run it now includes four checks I\n"
     "run first thing. I don't plan on automating any time soon.\" And on\n"
     "the swap: \"the daily run now checks that one drive is paused before\n"
     "committing the cache build.\"\n"
     "Tony pauses for 24 hours, not two: \"2 hours can accidentally\n"
     "expire.\"\n"
     "**Note (2026-10-07):** so the hand run is the working practice, by\n"
     "choice, not a stopgap. The move off OneDrive and a restored schedule\n"
     "are NOT to be proposed again unless Tony raises them; the 2026-09-20\n"
     "analysis stays above for that day. The pause is part of the routine\n"
     "itself: gallery `daily_run.py` step 2 stops before the cache build,\n"
     "asks for OneDrive to be paused and records the time [verified @\n"
     "gallery 4cfeca27]. Its printed words still say two hours (\"Pause\n"
     "syncing > 2 hours\", and the expiry time it prints adds two hours),\n"
     "against Tony's 24; owed to the next gallery patch that opens the\n"
     "file: say 24 hours, or ask how long.\n"
     "**THE RETRY IS PROVEN (2026-10-07, read from the swap log at gallery\n"
     "4cfeca27).** `data/cache_swap_log.jsonl` holds 29 lines, all outcome\n"
     "`ok`, and TWO show `staging_to_live` taking 2 attempts: runs\n"
     "20261004T205153Z and 20261006T182032Z, both Tony's hand builds,\n"
     "both with OneDrive paused. So the lock recurred twice in three days\n"
     "at the rename it always catches, the retry absorbed it both times,\n"
     "and the pause does not prevent the lock -- the retry does. This is\n"
     "the evidence the 2026-09-20 build said would be the only kind there\n"
     "is. The 2026-09-21 Gap's \"until one appears the retry is unproven\"\n"
     "no longer holds.\n"
     "**Tony-action (decide):** whether this item CLOSES on that evidence.\n"
     "The fix works, the routine stands, the cause (a OneDrive or Windows\n"
     "lock on the live directory) is outside the project and is not being\n"
     "chased. If it closes, the two owed items stay named in L-351: the\n"
     "gallery-cache-builder skill's next version (the `[SWAP]` line, the\n"
     "run order, the empty \"(N)\" folders, and now the two proven retries)\n"
     "and the \"conflict copies\" wording still in four places (`.gitignore`,\n"
     "`check_cache_siblings.py`, the orrery dashboard,\n"
     "`L342_install_test_run_sequence.md`; all still there at HEAD).\n"
     "(The Fable 5.1 review of 2026-10-07 had counted the daily run as the\n"
     "project's largest standing claim on Tony's time; Tony's word is the\n"
     "answer to that.)\n"),
]


def main():
    if os.path.basename(os.getcwd()) == "documentation":
        raise SystemExit("ERROR: run this from the repo ROOT, not from "
                         "documentation/. NOTHING was written.")
    for marker in ROOT_MARKERS:
        if not os.path.isfile(marker):
            raise SystemExit("ERROR: %s is not here, so this is not the "
                             "orrery root. NOTHING was written." % marker)
    with open(LEDGER, "rb") as handle:
        raw = handle.read()
    crlf = b"\r\n" in raw
    text = raw.decode("utf-8").replace("\r\n", "\n")
    before = sum(1 for ch in text if ord(ch) > 127)
    done = []
    for label, old, new in EDITS:
        found = text.count(old)
        if found != 1:
            raise SystemExit("ANCHOR FAIL (%s): expected 1 match in %s, "
                             "found %d. Has this patch already run? "
                             "NOTHING was written." % (label, LEDGER, found))
        text = text.replace(old, new)
        done.append(label)
    if sum(1 for ch in text if ord(ch) > 127) > before:
        raise SystemExit("ERROR: %s would hold new non-ASCII text. "
                         "NOTHING was written." % LEDGER)
    with open(LEDGER, "wb") as handle:
        handle.write(text.encode("utf-8"))
    if crlf:
        print("note: %s was CRLF in the working copy; written LF" % LEDGER)
    for label in done:
        print("ok  %-24s %s" % (LEDGER, label))
    print("")
    print("patch applied")
    print("")
    print("NEXT:")
    for line in NEXT:
        print("  " + line)


if __name__ == "__main__":
    main()
