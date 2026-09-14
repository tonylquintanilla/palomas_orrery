"""
patch_L321_correct_link_lesson.py

Corrects a lesson that this session's own last hour falsified, in the
two documents that carry it.

HOW TO RUN
    Save this file into documentation/ -- the same folder as the two
    .md files it edits -- open it in VS Code, and click Run.
    Equivalent command line: python patch_L321_correct_link_lesson.py

WHY
    Both files state that a URL lost in a clipboard paste "cannot be
    recovered afterwards". Twenty addresses were recovered, from GPT 6
    Medium's own exported markdown, after Tony declined the
    recommendation to delete the authored copies as redundant.

    The corrected rule is stronger than the one it replaces: a paste and
    an export are different artifacts that fail differently, so keep the
    checker's authored file and treat any transcription as derived from
    it.

WHAT IT CHANGES
    HANDOFF_L321_crosscheck_round_20260913.md
      1. the link lesson, rewritten
      2. a new lesson on keeping the redundant artifact
      3. the deferred "seven sources never opened" narrows to three,
         since worksheet 3's six now carry addresses

    DRAFT_provenance_discipline_2_12_field_notes_20260913.md
      4. note 3 rewritten to match, with the operator half named so it
         lands in the Mode 7 reminder rather than only in the prompt

    Transactional across BOTH files: each is fingerprinted and every
    anchor is checked before anything is written. If any check fails,
    neither file is touched.

PERMANENT HALF
    None. One-shot. Leave the script in documentation/ once run.

Written September 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

HANDOFF = "HANDOFF_L321_crosscheck_round_20260913.md"
DRAFT = "DRAFT_provenance_discipline_2_12_field_notes_20260913.md"

FINGERPRINTS = {
    HANDOFF: "84ff90307f5fb68579a6f86007c469e4",
    DRAFT: "be2612492dc9ec018815f4c1d738c802",
}

EDITS = {
    HANDOFF: [
        # 1 + 2. the link lesson, and the one that follows from how it was found
        (b"""- **A link is an object, not text.** It dies in the clipboard and
  cannot be recovered afterwards.
""",
         b"""- **A link is an object, not text -- but the export is not the paste.**
  A hyperlink copied out of a chat arrives as a chip carrying no
  address, and the loss is silent. It is recoverable, from the file the
  checker itself exported, because a paste and an export fail
  differently. Ask for bare URLs in a code block AND keep the authored
  file; treat any transcription as derived from it.
- **A redundant artifact was the only copy of something.** Claude
  recommended deleting all six raw GPT copies as duplicates. Tony
  declined, on the argument that the checker's own files are the actual
  record. One of them held twenty addresses, including all four
  DISCOVERY-row sources. Redundancy looked like clutter right up to the
  moment it was the only copy.
"""),
        # 3. the deferred list narrows
        (b"""- **Seven of GPT's sources were never opened**, named at the end of the
  source-recovery finding: Maiti and Ramachandran (2023), the
  University of Minnesota page, Y. X. Li et al. (2023), Selesnick et
  al. (2014), Li et al. (2015), Shi et al. (2020), Urbar et al. (2019),
  Ingale et al., Kumar and Pulkkinen (2025). None is load-bearing now
  that three open sources state the extents.
""",
         b"""- **Three of GPT's sources remain without an address**, all from
  worksheets 1 and 2, which exported with no links at all: Urbar et al.
  (2019), Ingale et al., and Kumar and Pulkkinen (2025). The six named
  in the source-recovery finding for worksheet 3 -- Maiti and
  Ramachandran (2023), the University of Minnesota page, Y. X. Li et
  al. (2023), Selesnick et al. (2014), Li et al. (2015) and Shi et al.
  (2020) -- now carry URLs, recovered at `7bd5b1e8`. None of the three
  is load-bearing.
"""),
    ],
    DRAFT: [
        # 4. note 3 rewritten
        (b"""> Ask for bare URLs inside a code block. A hyperlink pasted out of a
> chat interface arrives as a chip carrying no address, and the loss is
> silent: source names and access words survive, addresses do not.
>
> It is not recoverable after the fact. A checker asked to reprint them
> has nothing left to reprint.
>
> (L-321, 2026-09-13. Three returns lost every URL in transfer. The
> analysis was sound and unusable, because an access word with no
> address is an assertion about a read rather than a record of one.)
""",
         b"""> Ask for bare URLs inside a code block. A hyperlink pasted out of a
> chat interface arrives as a chip carrying no address, and the loss is
> silent: source names and access words survive, addresses do not. A
> checker asked afterwards to reprint them has nothing left to reprint.
>
> But the paste is not the only artifact. KEEP THE FILE THE CHECKER
> EXPORTED. An export preserves addresses a paste destroys, so the
> authored file is the record and any transcription is derived from it;
> where the two disagree, the authored file wins. Downloading it is an
> operator action and belongs in the Mode 7 reminder, not only in the
> prompt.
>
> (L-321, 2026-09-13. Three returns lost every URL in transfer and the
> checker could not recover them. Twenty addresses came back anyway,
> out of its own exported markdown, after the recommendation to delete
> the authored copies as redundant was declined. One of those addresses
> matched, character for character, a URL an independent search pass
> had reached without seeing it.)
"""),
    ],
}


def fail(msg):
    print("ERROR: " + msg)
    print("NOTHING was written to either file. Undo is Discard Changes "
          "in GitHub Desktop.")
    sys.exit(1)


def main():
    staged = {}

    for path, edits in EDITS.items():
        if not os.path.exists(path):
            fail("%s is not in this folder. Put this script in "
                 "documentation/, beside the files it edits." % path)
        with open(path, "rb") as f:
            content = f.read()
        actual = hashlib.md5(content).hexdigest()
        if actual != FINGERPRINTS[path]:
            fail("%s is not the expected base.\n"
                 "       expected md5 %s\n       found    md5 %s"
                 % (path, FINGERPRINTS[path], actual))
        for old, new in edits:
            n = content.count(old)
            if n != 1:
                fail("ANCHOR FAIL in %s -- expected 1 match, got %d:\n       %r"
                     % (path, n, old[:70]))
            content = content.replace(old, new)
        try:
            content.decode("ascii")
        except UnicodeDecodeError:
            fail("%s result is not ASCII." % path)
        if b"\r" in content:
            fail("%s result contains CR; line endings must stay LF." % path)
        staged[path] = content
        print("ok   %s (%d edits checked)" % (path, len(edits)))

    for path, content in staged.items():
        with open(path, "wb") as f:
            f.write(content)
        print("written  %s (%d bytes)" % (path, len(content)))

    print("Next: commit and push.")


if __name__ == "__main__":
    main()
