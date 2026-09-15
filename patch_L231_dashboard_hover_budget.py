"""Add the hover budget checker to the dashboard, indented under the runner.

Target: palomas_orrery_dashboard.py  (orrery repo root)
Built against orrery 409a0e73e174a2bc6680be428132db0811351292.
Handle: L-231 follow-up.  2026-09-15, with Anthropic's Claude Opus 5.

PAIRS WITH patch_L231_hover_budget_checker.py in the GALLERY repo, which
creates the suite and adds it to the maintenance runner. Apply that one
too, or this button points at a file that does not exist.

WHERE IT GOES
-------------
Indented, in Gallery & Web, between the Artifact 1 Assembler Pin and Cache
Siblings. The indent means what it has meant since Tony's ruling of
2026-08-12: the maintenance runner above already covers this tool, and the
individual entry stays launchable so the automation's contents remain
visible instead of disappearing behind one button. Its neighbours in that
group are the other things the runner runs, and it is placed with the
gating ones rather than with report-only Cache Siblings.

The button runs documentation/run_hover_budget.py, a Python wrapper,
because the dashboard launches Python and the suite itself is Node -- the
same shape as the Artifact 1 pin.

UNDO
----
Nothing is written unless the fingerprint matches. To undo: in GitHub
Desktop, right-click palomas_orrery_dashboard.py in Changes and Discard
Changes.
"""

import hashlib
import os
import sys

TARGET = "palomas_orrery_dashboard.py"
BASE_FP = "16f8634dec5919dcf528a0dace798f07"

ANCHOR = b'        ("Cache Siblings",'

ENTRY = b'''        ("Hover Budget",
        os.path.join("documentation", "run_hover_budget.py"),
        "Counts the LINES in every hover the renderers produce -- 78 of "
        "them, across the composed Earth room, Earth's features on their "
        "own, and the two ringed planets -- and prints the longest ten so "
        "the offender is named rather than implied. It GATES the gallery "
        "runner. It exists because its sibling checks hover WIDTH, no line "
        "over 90 characters, and on 2026-09-15 a 32-line bow shock hover "
        "passed that comfortably while the box ran off the bottom of the "
        "phone: a hover can be perfectly narrow and still overflow. The "
        "ceiling is a RATCHET -- lower it when the worst hover comes down, "
        "never raise it to admit a new one, which is how the old ones "
        "reached 32. The suite is Node; this is the Python wrapper the "
        "dashboard needs, the same shape as the Artifact 1 pin. Runs from "
        "the gallery repo ROOT.",
        GALLERY_REPO_DIR,
        True,
        None,
        True),
        ("Cache Siblings",'''


def main():
    if not os.path.isfile(TARGET):
        print("FAILURE: %s not found. Run this from the orrery repo root."
              % TARGET)
        print("NOTHING was written.")
        return 1

    with open(TARGET, "rb") as handle:
        data = handle.read()

    actual = hashlib.md5(data.replace(b"\r\n", b"\n")).hexdigest()
    if actual != BASE_FP:
        print("FAILURE: BASE MOVED.")
        print("  expected content md5 %s" % BASE_FP)
        print("  found                %s" % actual)
        print("NOTHING was written.")
        return 1

    if b"Hover Budget" in data:
        print("FAILURE: the entry is already there. NOTHING was written.")
        return 1

    is_crlf = data.count(b"\r\n") > 0

    def fit(block):
        return block.replace(b"\n", b"\r\n") if is_crlf else block

    count = data.count(fit(ANCHOR))
    if count != 1:
        print("FAILURE: expected 1 match for the Cache Siblings anchor, got %d."
              % count)
        print("NOTHING was written.")
        return 1

    data = data.replace(fit(ANCHOR), fit(ENTRY))

    with open(TARGET, "wb") as handle:
        handle.write(data)

    print("OK: %s written (%s)." % (TARGET, "CRLF" if is_crlf else "LF"))
    print("    Hover Budget added, indented, in Gallery & Web,")
    print("    between the Artifact 1 Assembler Pin and Cache Siblings.")
    print()
    print("Next: open the dashboard and check the button is there and")
    print("      indented with its neighbours, then press it.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
