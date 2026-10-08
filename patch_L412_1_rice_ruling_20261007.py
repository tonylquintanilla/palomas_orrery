#!/usr/bin/env python3
"""
patch_L412_1_rice_ruling_20261007.py -- ORRERY repo. Records Tony's
ruling of 2026-10-07: an item inside an ordered list needs no RICE
score. The rule goes to ledger-and-session-records at its next version;
until then it is carried on L-351.

Built on orrery 8653ef1b593aaf3835ecbcf2186b9e3e28a28089 at
https://github.com/tonylquintanilla/palomas_orrery. The gallery is not
read or changed. No code changes: records only.

HOW TO RUN IT
    Save this file in the ORRERY repo ROOT (next to palomas_orrery.py),
    open it in VS Code and click Run (the command is
    python patch_L412_1_rice_ruling_20261007.py). Then follow the NEXT
    steps it prints.

    It runs before or after patch_L027_2 and patch_L418_2: the three
    edit different lines, and this one adds its header stamp above the
    "Review and RICE update" line, where the others do not look.

WHAT CHANGES
    LEDGER_CONSOLIDATED.md
        a header stamp;
        L-412: its date, and Tony's ruling on question (a); question (b),
            the proposed scores, stays open;
        L-351: its date, and its ledger-and-session-records line, which
            gains the RICE rule as owed to version 1.17 and drops the
            by-the-lines rule, which landed in 1.16 on 2026-10-05.
    Matched only at those lines (L-419). Your notes elsewhere in the
    ledger do not stop it.

    Permanent: the ledger lines. The script is spent once it has run;
    file it in documentation/.

TESTED on a copy of 8653ef1b: every edit landed; ledger_index.py --check
reported no consistency problems; a second run refused and wrote
nothing. Also tested on copies with patch_L027_2 and patch_L418_2
applied first, and with this patch applied before each of them: every
order ran clean.

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
     "(L-412: Tony's ruling, an item inside an ordered list needs no RICE\n"
     "score; carried to ledger-and-session-records 1.17 on L-351), built on\n"
     "8653ef1b.\n"
     "Review and RICE update Tony 6-21-2026\n"),
    ("L-412 date",
     "<!-- L:412 status:OPEN upd:2026-10-04 section:A flag: rice: -->\n",
     "<!-- L:412 status:OPEN upd:2026-10-07 section:A flag: rice: -->\n"),
    ("L-412 ruling on (a)",
     "  (L-131 and L-128 at 3/3/70/2; L-216 lowered or DEFERRED; L-228, L-241,\n"
     "  L-292 confirmed; L-252 re-scored).\n"
     "**Gap:** after L-413, work down the list from item 3.\n",
     "  (L-131 and L-128 at 3/3/70/2; L-216 lowered or DEFERRED; L-228, L-241,\n"
     "  L-292 confirmed; L-252 re-scored).\n"
     "- **Tony's ruling on (a), 2026-10-07:** an item inside an ordered\n"
     "  list -- this one, L-413, and any list like them -- needs no RICE\n"
     "  score. The list's order is its priority, under the master plan's\n"
     "  sequencing authority (L-221). An item outside a list keeps RICE,\n"
     "  and gets a coarse score when it is next opened. The rule is method\n"
     "  (Method Belongs to the Skill): it goes into ledger-and-session-\n"
     "  records at its next version, 1.17, which L-418's build cuts, and is\n"
     "  carried on L-351 until then. Question (b), the proposed scores, is\n"
     "  still open.\n"
     "**Gap:** after L-413, work down the list from item 3.\n"),
    ("L-351 date",
     "<!-- L:351 status:OPEN upd:2026-10-04 section:A flag: rice: -->\n",
     "<!-- L:351 status:OPEN upd:2026-10-07 section:A flag: rice: -->\n"),
    ("L-351 ledger skill line",
     "  - ledger-and-session-records: a patch checks files Tony annotates by\n"
     "    the lines it edits, never by a whole-file fingerprint (Tony,\n"
     "    2026-10-03); and Tony's documentation-folder practice (above).\n",
     "  - ledger-and-session-records, at 1.17 (L-418's build): an item\n"
     "    inside an ordered list needs no RICE score, the list's order being\n"
     "    its priority under the plan's sequencing authority; items outside\n"
     "    a list keep RICE (Tony, 2026-10-07, L-412). And Tony's\n"
     "    documentation-folder practice (above). The by-the-lines check of\n"
     "    Tony-annotated files landed at 1.16 on 2026-10-05 (L-419) and is\n"
     "    struck here.\n"),
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
