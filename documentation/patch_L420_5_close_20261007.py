#!/usr/bin/env python3
"""
patch_L420_5_close_20261007.py -- ORRERY repo. Closes L-420, the
galactic plane in the orrery, on Tony's look at patch_L420_4.

Built on orrery 12693a53 at
https://github.com/tonylquintanilla/palomas_orrery (gallery not read or
changed). No code changes: records only.

HOW TO RUN IT
    Save this file in the ORRERY repo ROOT, open it in VS Code and click
    Run. Then follow the NEXT steps it prints.

WHAT CHANGES
    LEDGER_CONSOLIDATED.md
        a header stamp;
        L-420: Tony's run and look recorded, one earlier claim corrected,
        the cone's keeping recorded, status DONE, and the WHOLE block
        moved to the end of section C (closed). It is found by its own
        heading, so any notes you wrote inside it move with it; only its
        status line and its Gap line must be as this patch expects.
    documentation/HANDOFF_L420_galactic_plane_20261006.md
        a closing section, two lines for the next Where We Are, and its
        Next session list. Matched only at those lines.

TESTED on a copy of 12693a53: every edit landed; ledger_index.py and
orrery_maintenance_run.py then ran with every gating checker passing;
L-420 shows in the index's closed table; a second run refused and wrote
nothing.

SUCCESS looks like: one "ok" line per edit, then "patch applied".
FAILURE looks like: one ERROR: or ANCHOR FAIL: line, and NOTHING is
written. Undo is Discard Changes in GitHub Desktop.

Written October 7, 2026 with Anthropic's Claude Opus 5.5.
"""

import os

ROOT_MARKERS = ("palomas_orrery.py", "LEDGER_CONSOLIDATED.md")
LEDGER = "LEDGER_CONSOLIDATED.md"
HANDOFF = "documentation/HANDOFF_L420_galactic_plane_20261006.md"

NEXT = ["1. Move this script into documentation/ FIRST, so the maintenance",
        "   run does not count it (it did in your last two runs).",
        "2. Run orrery_maintenance_run.py; the ledger index moves L-420 to",
        "   the closed table.",
        "3. Commit and push."]

STAMP_OLD = ("(L-420 after Tony's look: the circles' hovers, the brighter tide and\n"
             "its cone; L-408 told the orrery has them), built on fbd223ee.\n")
STAMP_NEW = STAMP_OLD + (
    "Module updated: October 7, 2026 with Anthropic's Claude Opus 5.5\n"
    "(L-420 closed on Tony's look), built on 12693a53.\n")

META_OLD = "<!-- L:420 status:OPEN upd:2026-10-06 section:A flag: rice: -->\n"
META_NEW = "<!-- L:420 status:DONE upd:2026-10-07 section:C flag: rice: -->\n"

HEAD_OLD = ("#### [L-420] The galactic plane in the Celestial Grid, the galactic "
            "centre in the star background (orrery, sky)\n")
HEAD_NEW = ("#### [L-420] The galactic plane in the Celestial Grid, the galactic "
            "centre in the star background (orrery, sky, DONE 2026-10-07)\n")

GAP_OLD = ("**Gap:** Tony runs patch_L420_4 and the maintenance run, pushes, and\n"
           "looks (Mode 5): the tide from the side with the violet circle edge-on,\n"
           "the cone's faintness, the three crosses' places and colours. Then\n"
           "close.\n")
GAP_NEW = (
    "- **Run and pushed at 12693a53, 2026-10-07.** Tony's look: \"correct\";\n"
    "  \"images look great at 5000. the X is clearly visible even without\n"
    "  the cone.\"\n"
    "- **Corrected: the tide's X.** The bullet above said a brighter tide\n"
    "  alone would not show an X. Tony's render shows it does. Most likely\n"
    "  because the points are spread evenly in distance from the Sun, so\n"
    "  they crowd near it, where the layers at 45 degrees read as an X. The\n"
    "  flat sketch spread them too evenly to show it. The render wins.\n"
    "- **The cone stays.** Tony: \"I think the cone is useful to illustrate\n"
    "  the tidal influence as physics.\"\n"
    "- **Loose ends, where they went.** The phone's question: L-408, whose\n"
    "  Gap names the galactic plane, Sgr A*, and the tide's cone and\n"
    "  brightness (checked at 12693a53). The 297 in Tony's run was again\n"
    "  this item's patch script in the repo root; the pushed tree scans\n"
    "  296. This closing patch's NEXT moves the script before the run.\n"
    "- **Closed 2026-10-07.**\n"
    "**Gap:** none. (Was: Tony's run and look at patch_L420_4.)\n")

C_END_OLD = "(ANCHOR_ONLY); L-396.\n## D. RECONCILED LEDGER -- OPEN\n"

HO_EDITS = [
    ("closing section",
     "## Tony-actions\n",
     ("## Closed, 2026-10-07\n"
      "\n"
      "- Pushed at 12693a53. Tony's look: \"correct\"; \"images look great at\n"
      "  5000. the X is clearly visible even without the cone.\"\n"
      "- The points alone show the X, which the sketch had said they would\n"
      "  not. The cone stays: \"I think the cone is useful to illustrate the\n"
      "  tidal influence as physics.\"\n"
      "- L-420 closed by `patch_L420_5_close_20261007.py`. The phone's\n"
      "  question stays on L-408.\n"
      "\n"
      "## Tony-actions\n")),
    ("Where We Are lines",
     ("- Needs Tony: a look at the tide from the side, and a design decision\n"
      "  on whether the phone gets the galactic plane, Sgr A* and the cone\n"
      "  (L-408).\n"),
     ("- Needs Tony: a look at the tide from the side, and a design decision\n"
      "  on whether the phone gets the galactic plane, Sgr A* and the cone\n"
      "  (L-408).\n"
      "- Changed (2026-10-07): the galactic plane work in the orrery is\n"
      "  finished. The tide shows its X, and the cone marks where the tide\n"
      "  works hardest. Your look on the tide is done.\n"
      "- Still waiting: the phone's design decision (L-408).\n")),
    ("Next session",
     ("- Close L-420 on Tony's look at patch_L420_4, or adjust what he\n"
      "  names.\n"),
     "- L-420 closed 2026-10-07.\n"),
]


def read_lf(path):
    with open(path, "rb") as handle:
        raw = handle.read()
    return raw.decode("utf-8").replace("\r\n", "\n"), b"\r\n" in raw


def fail(message):
    raise SystemExit(message + " NOTHING was written.")


def one(text, old, label, path):
    found = text.count(old)
    if found != 1:
        hint = " Has this patch already run?" if found == 0 else ""
        fail("ANCHOR FAIL (%s): expected 1 match in %s, found %d.%s"
             % (label, path, found, hint))


def main():
    if os.path.basename(os.getcwd()) == "documentation":
        fail("ERROR: run this from the repo ROOT, not from documentation/.")
    for marker in ROOT_MARKERS:
        if not os.path.isfile(marker):
            fail("ERROR: %s is not here, so this is not the orrery root." % marker)
    if not os.path.isfile(HANDOFF):
        fail("ERROR: %s is not here." % HANDOFF)

    done = []
    ledger, ledger_crlf = read_lf(LEDGER)

    one(ledger, STAMP_OLD, "header stamp", LEDGER)
    ledger = ledger.replace(STAMP_OLD, STAMP_NEW)
    done.append((LEDGER, "header stamp"))

    # L-420's block: from its heading to the next heading of any level.
    one(ledger, HEAD_OLD, "L-420 heading", LEDGER)
    start = ledger.index(HEAD_OLD)
    ends = [i for i in (ledger.find("\n#### [L-", start + 1),
                        ledger.find("\n### ", start + 1),
                        ledger.find("\n## ", start + 1)) if i != -1]
    end = min(ends) + 1
    block = ledger[start:end]
    for old, label in ((META_OLD, "L-420 status line"), (GAP_OLD, "L-420 Gap")):
        one(block, old, label, LEDGER + " (inside L-420)")
    closed = (block.replace(HEAD_OLD, HEAD_NEW).replace(META_OLD, META_NEW)
              .replace(GAP_OLD, GAP_NEW)).rstrip("\n") + "\n"
    ledger = ledger[:start] + ledger[end:]
    one(ledger, C_END_OLD, "end of section C", LEDGER)
    ledger = ledger.replace(
        C_END_OLD,
        "(ANCHOR_ONLY); L-396.\n\n" + closed + "\n## D. RECONCILED LEDGER -- OPEN\n")
    done.append((LEDGER, "L-420 closed and moved to section C"))

    handoff, handoff_crlf = read_lf(HANDOFF)
    for label, old, new in HO_EDITS:
        one(handoff, old, label, HANDOFF)
        handoff = handoff.replace(old, new)
        done.append((HANDOFF, label))

    for path, text, crlf in ((LEDGER, ledger, ledger_crlf),
                             (HANDOFF, handoff, handoff_crlf)):
        with open(path, "wb") as handle:
            handle.write(text.encode("utf-8"))
        if crlf:
            print("note: %s was CRLF in the working copy; written LF" % path)
    for path, label in done:
        print("ok  %-56s %s" % (path, label))
    print("")
    print("patch applied")
    print("")
    print("NEXT:")
    for line in NEXT:
        print("  " + line)


if __name__ == "__main__":
    main()
