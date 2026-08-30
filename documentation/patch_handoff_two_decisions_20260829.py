"""
patch_handoff_two_decisions_20260829.py

Two paragraphs into the 2026-08-29 night handoff, both from the
conversation that followed it.

Built on orrery `a555b0bc7f2e183ef6114ebed1c5bc93018b5c73` at
https://github.com/tonylquintanilla/palomas_orrery (branch main),
gallery `80759493dd03f7005eb9c4baae6448756893f884` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Both confirmed against the live remote 2026-08-29.

ONE file, two edits.


WHY

Tony asked what L-262 and L-256 were about, was given a fuller answer
than the handoff carries, and asked whether that answer was in the
handoff. Most of it was. Two things were not.

**The timing argument for L-262 is new**, and it is the one that would
have been lost. Portrait mobile means editing `interactive.html`
anyway, so extracting the framing helpers in the same pass costs one
Mode 5 instead of two. Neither item says that on its own; it only
appears when they sit side by side, which is exactly the kind of
observation a handoff exists to carry.

**The denominator behind L-256 is in the ledger but not the handoff.**
160 of roughly 236 statusable items live inside dictionaries, so a beta
without one proves the format for about a third of the store. That is
the whole reason the question exists, and a handoff reader would
otherwise see two candidate dicts and no reason to care which.

What is deliberately NOT added: an explanation of what
`smoke_framing.js` does. A handoff names the decision and points at the
block. Restating the file is the file's job.


AFTER RUNNING IT

Nothing to regenerate. Commit it.


HOW TO RUN IT

Drop this file into the ORRERY repo root and press Run.

Prepared August 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

REPO_ROOT_FALLBACK = r"C:\Users\tonyq\Documents\GitHub\palomas_orrery"
PROBE = "constants_new.py"

HANDOFF = os.path.join("documentation",
                       "HANDOFF_20260829_night_sun_finished.md")
HANDOFF_MD5 = "c90838a80cc980c32717187eaa26092b"

EDITS = [
    (
        "L-262 gains the timing argument",

        "since the test broke precisely because it read a copy of logic that\n"
        "lives inline in the page. It touches `interactive.html`, which is live.\n",

        "since the test broke precisely because it read a copy of logic that\n"
        "lives inline in the page. It touches `interactive.html`, which is live.\n"
        "\n"
        "There is a timing argument that neither item carries on its own.\n"
        "Portrait mobile means editing `interactive.html` anyway. Extracting\n"
        "the framing helpers in the same pass costs ONE Mode 5 rather than\n"
        "two, and Mode 5 is the step that cannot be delegated, so it is the\n"
        "scarce one. If portrait goes first and this waits, that saving is\n"
        "gone.\n",
    ),
    (
        "L-256 gains the denominator that makes the question matter",

        "`spectral_subclass_temps` (9 entries, and Fable already flagged it as an\n"
        "uncited physical claim inside the store) or `CENTER_BODY_RADII` (18\n"
        "well-sourced radii). Open since 2026-08-27 and the single thing blocking\n"
        "the item.\n",

        "`spectral_subclass_temps` (9 entries, and Fable already flagged it as an\n"
        "uncited physical claim inside the store) or `CENTER_BODY_RADII` (18\n"
        "well-sourced radii). Open since 2026-08-27 and the single thing blocking\n"
        "the item.\n"
        "\n"
        "Why a dict has to be in the beta at all, measured at `7f4a2f9f` and\n"
        "recorded in L-256: the store holds 67 top-level assignments, and its\n"
        "three dicts hold 160 entries between them. Of roughly 236 statusable\n"
        "items, 160 sit inside dicts. A beta of scalars alone proves the\n"
        "format for about a third of the store and says nothing about the\n"
        "shape most of it is actually in.\n"
        "\n"
        "The two candidates differ in what the beta would be FOR.\n"
        "`spectral_subclass_temps` is smaller and carries a real finding, so\n"
        "the beta would prove the format and clear something at the same\n"
        "time -- and the convention ought to hold at home before it is\n"
        "enforced on anything downstream. `CENTER_BODY_RADII` is larger,\n"
        "already well sourced from the April 2026 verification and the L-162\n"
        "promotion, and on the active build path; it would exercise the\n"
        "format on easy cases with more of them.\n",
    ),
]


def find_repo_root():
    here = os.path.dirname(os.path.abspath(__file__))
    for label, folder in (("beside this script", here),
                          ("working directory", os.getcwd()),
                          ("fallback path", REPO_ROOT_FALLBACK)):
        if os.path.isfile(os.path.join(folder, PROBE)):
            print("found %s in the %s" % (PROBE, label))
            return folder
    return None


def main():
    print("patch_handoff_two_decisions_20260829.py")
    root = find_repo_root()
    if root is None:
        print("REFUSED: could not find %s. Move this script into the ORRERY"
              % PROBE)
        print("         repo root and run it again.")
        return 1

    path = os.path.join(root, HANDOFF)
    print("")
    print("target :", HANDOFF)
    if not os.path.isfile(path):
        print("REFUSED: no such file.")
        return 1
    with open(path, "rb") as handle:
        raw = handle.read()

    # Guard on LF-normalised content, style preserved on write --
    # safe-file-editing 1.9, Compare Content, Not Bytes.
    was_crlf = b"\r\n" in raw
    content = raw.replace(b"\r\n", b"\n") if was_crlf else raw
    actual = hashlib.md5(content).hexdigest()
    print("md5    : %s (expected %s)%s"
          % (actual, HANDOFF_MD5, "   [CRLF]" if was_crlf else ""))
    if actual != HANDOFF_MD5:
        print("REFUSED: the handoff is not in the state this patch expects.")
        print("         Nothing written.")
        return 1

    text = content.decode("utf-8")
    for label, old, _new in EDITS:
        count = text.count(old)
        print("  anchor x%d  %s" % (count, label))
        if count != 1:
            print("REFUSED: anchor matched %d times, expected 1." % count)
            print("         Nothing written.")
            return 1
    for _label, old, new in EDITS:
        text = text.replace(old, new, 1)

    out = text.encode("utf-8")
    before = sum(1 for byte in raw if byte > 127)
    after = sum(1 for byte in out if byte > 127)
    print("  non-ascii bytes: %d -> %d" % (before, after))
    if after != before:
        print("REFUSED: the patch introduced non-ASCII text.")
        return 1

    final = out.replace(b"\n", b"\r\n") if was_crlf else out
    with open(path + ".bak", "wb") as handle:
        handle.write(raw)
    with open(path, "wb") as handle:
        handle.write(final)
    print("")
    print("WROTE   %s  (%d -> %d bytes%s)"
          % (HANDOFF, len(raw), len(final), ", CRLF" if was_crlf else ""))
    print("")
    print("Nothing to regenerate. Commit it.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
