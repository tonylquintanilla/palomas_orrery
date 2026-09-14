"""
patch_L321_handoff_bump_first.py

Two amendments to the L-321 handoff, closing the session.

HOW TO RUN
    Save into documentation/, open in VS Code, click Run.
    Equivalent: python patch_L321_handoff_bump_first.py

WHY
    1. The Gemini Flash 3.8 returns were never filed in the repo. The
       handoff cites that leg, and the 2.12 roster note rests on it, so
       the handoff has to say the evidence is not on disk and why that
       is acceptable here: a CAPABILITY claim is re-testable in one
       question, unlike a citation claim, which cannot be re-derived and
       must be filed.
    2. The 2.12 bump becomes the NEXT session's first action, ahead of
       item 7. That is v3.55's ordering -- a bump taken before the build
       it serves is verified by the gate rather than promised in a
       handoff.

PERMANENT HALF
    None. One-shot. Leave the script in documentation/ once run.

Written September 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

TARGET = "HANDOFF_L321_crosscheck_round_20260913.md"
FINGERPRINT = "37865a92f4d99a4b52f50a8e7a430d06"

EDITS = [
    (b"""5. **Gemini Flash 3.8 returned nothing usable** and said so plainly: it
   cannot fetch, so every Source cell reads WALLED. Gemini 3.1 Pro
   Extended Thinking, sent later, fetched three PDFs successfully.
""",
     b"""5. **Gemini Flash 3.8 returned nothing usable** and said so plainly: it
   cannot fetch, so every Source cell reads WALLED. Gemini 3.1 Pro
   Extended Thinking, sent later, fetched three PDFs successfully.
   **The Flash returns are NOT filed in this repo** -- only the Pro
   ones are. That is deliberate and it is the one place this session
   leaves a claim without its artifact. The reason it is acceptable
   here and would not be for a citation: a CAPABILITY claim is
   re-testable in a single question, which is what the pre-flight rule
   in the 2.12 draft asks for, whereas a citation claim cannot be
   re-derived and has to be on disk. If the roster note is ever
   doubted, re-run the pre-flight rather than looking for the file.
""",
    ),
    (b"""2. **Bump `provenance-discipline` to 2.12.** Nothing blocks it now.
""",
     b"""2. **Bump `provenance-discipline` to 2.12 -- the NEXT SESSION'S FIRST
   ACTION, ahead of item 7.** Nothing blocks it now, and the ordering
   is v3.55's: a bump taken before the build it serves is checked by
   the stale-skill gate against a matching manifest, instead of
   travelling as a promise. It was not taken in this session because
   the context was nearly spent, and a rushed edit to a 1712-line
   CRITICAL skill is how a bad rule ships. Note 3 of the draft was
   FALSE when written and was falsified four hours later in the same
   session; the draft-then-review gap is what caught it, which is the
   argument for the gap and against writing straight into the skill.
""",
    ),
]


def fail(msg):
    print("ERROR: " + msg)
    print("NOTHING was written. Undo is Discard Changes in GitHub Desktop.")
    sys.exit(1)


def main():
    if not os.path.exists(TARGET):
        fail("%s is not in this folder. Put this script in documentation/." % TARGET)

    with open(TARGET, "rb") as f:
        content = f.read()

    actual = hashlib.md5(content).hexdigest()
    if actual != FINGERPRINT:
        fail("%s is not the expected base.\n"
             "       expected md5 %s\n       found    md5 %s"
             % (TARGET, FINGERPRINT, actual))

    for old, new in EDITS:
        n = content.count(old)
        if n != 1:
            fail("ANCHOR FAIL -- expected 1 match, got %d:\n       %r" % (n, old[:70]))
        content = content.replace(old, new)
        print("ok   %r" % old[:56])

    try:
        content.decode("ascii")
    except UnicodeDecodeError:
        fail("result is not ASCII.")
    if b"\r" in content:
        fail("result contains CR; line endings must stay LF.")

    with open(TARGET, "wb") as f:
        f.write(content)

    print("patch applied (%d bytes)" % len(content))
    print("Next: commit and push.")


if __name__ == "__main__":
    main()
