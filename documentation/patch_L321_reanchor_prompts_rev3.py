"""
patch_L321_reanchor_prompts_rev3.py

Moves the anchor of L321_slice1_prompts_rev3_20260912.md forward from
62ee5149 to f1bceefd, and records in the document why it moved.

HOW TO RUN
    Save this file into documentation/ -- the same folder as the .md it
    edits -- open it in VS Code, and click Run.
    Equivalent command line: python patch_L321_reanchor_prompts_rev3.py

WHY
    The three source files these prompts quote -- earth_visualization_
    shells.py, shell_configs.py, PROJECT_INSTRUCTIONS.md -- are byte-
    identical between 62ee5149 and f1bceefd, verified by md5 at both
    SHAs.  skills/provenance-discipline/SKILL.md is identical too, and
    reads 2.11 at both.  constants_new.py is NOT identical.

    L-325 (c0bb91a0) replaced EARTH_MAGNETOPAUSE_STANDOFF_RADII's
    sixteen-digit literal 10.251872972379905 with 10.25, and replaced
    EARTH_BOW_SHOCK_STANDOFF_RADII's expression with 13.51.

    Four claim rows in these prompts carry "[store value]" and the
    display strings interpolate their constants, so a checker sent to
    the old anchor resolves the two standoffs into exactly the form
    L-325 retired.  The rendered figure never changed -- ":.4g" prints
    10.25 and 13.51 from either form -- so this is about what a checker
    reads out of the STORE, not about what a visitor sees.

WHAT IT CHANGES -- three edits, all-or-nothing
    1. the common header block's SHA (the line pasted into each prompt)
    2. the file header's SHA
    3. a dated note recording the move and its reason

PERMANENT HALF
    None.  This script installs no capability; it corrects one document.
    It is one-shot -- the fingerprint below describes a tree that stops
    existing the moment it succeeds.  Leave it here in documentation/
    once it has run.

Written September 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

TARGET = "L321_slice1_prompts_rev3_20260912.md"

# md5 of the filed copy at orrery f1bceefd, which is byte-identical to
# the uploaded working copy.  The patch refuses to run against anything
# else.
FINGERPRINT = "78c5f3276768db8e313f737b354eadcd"

OLD_SHA = b"62ee5149e611e325455e56bb3b09486daeea0040"
NEW_SHA = b"f1bceefd05eeee0cac38fd519dd207314acb2383"

NOTE = b"""**Anchor moved forward 2026-09-13**, from `62ee5149` to the SHA above.
No prompt text changed. The reason is the store, not the strings: the
three files these prompts quote are byte-identical between those two
commits, and `constants_new.py` is not. L-325 (`c0bb91a0`) replaced the
magnetopause row's sixteen-digit literal with 10.25 and the bow shock
row's expression with 13.51. Four claim rows below carry `[store value]`
and the strings interpolate their constants, so a checker resolving them
at the old anchor would have read back the form that ruling retired. The
rendered figure is the same either way -- `:.4g` prints 10.25 and 13.51
from both forms -- so what moved is what a checker reads out of the
store, not what a visitor sees.

"""

# Bottom-up: highest line number first.
EDITS = [
    # 3. common header block, line 58 -- the SHA pasted into each prompt
    (b"> Built on `" + OLD_SHA + b"`",
     b"> Built on `" + NEW_SHA + b"`"),

    # 2. the dated note, inserted after the Supersedes paragraph
    (b"enumeration of the six strings still stands and is not repeated here.\n\n",
     b"enumeration of the six strings still stands and is not repeated here.\n\n" + NOTE),

    # 1. file header, line 3
    (b"Built on orrery `" + OLD_SHA + b"`",
     b"Built on orrery `" + NEW_SHA + b"`"),
]


def fail(msg):
    print("ERROR: " + msg)
    print("NOTHING was written. Undo is Discard Changes in GitHub Desktop.")
    sys.exit(1)


def main():
    if not os.path.exists(TARGET):
        fail("%s is not in this folder. Put this script in documentation/, "
             "beside the file it edits." % TARGET)

    with open(TARGET, "rb") as f:
        content = f.read()

    actual = hashlib.md5(content).hexdigest()
    if actual != FINGERPRINT:
        fail("%s is not the expected base.\n"
             "       expected md5 %s\n"
             "       found    md5 %s\n"
             "       The file has already been patched, or it differs from the\n"
             "       copy filed at orrery f1bceefd." % (TARGET, FINGERPRINT, actual))

    for old, new in EDITS:
        n = content.count(old)
        if n != 1:
            fail("ANCHOR FAIL -- expected 1 match, got %d: %r" % (n, old[:70]))
        content = content.replace(old, new)
        print("ok   %r" % old[:60])

    with open(TARGET, "wb") as f:
        f.write(content)

    print("patch applied (%d bytes)" % len(content))
    print("Next: confirm the two SHA lines read f1bceefd, then commit and push.")


if __name__ == "__main__":
    main()
