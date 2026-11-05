"""
patch_L508_1_code_prompts_section.py -- records only: the section on a
brief or prompt for a Claude Code session, carried on L-508 (a held
body's alarm) for ledger-and-session-records' next version; and
6AC4721 noted as kept on purpose on L-509 (obsolete code).

Built on orrery 79018c0cf0a59b2cf7ecb731cb7995021a953794 at
https://github.com/tonylquintanilla/palomas_orrery (branch main), read
live on Nov 4, 2026, evening. Written by the coordinating session
(Claude Opus 5.5).

Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\
gallery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\

WHAT IT CHANGES (one file)

    LEDGER_CONSOLIDATED.md
      L-508: two bullets above its Gap, for the records skill's next
        version: the section's content, as Tony said yes to it with a
        review's two changes; and the review count, a candidate only.
      L-509: one bullet above its Gap: 6AC4721 is kept on purpose.

    Checked only at the lines it edits, so your notes elsewhere never
    stop it. No status changes, so the ledger's index does not move.

RUN COMMAND

    Save this file in the orrery's root folder, open it in VS Code and
    click Run. (python patch_L508_1_code_prompts_section.py)

    Success: one "ok" line per edit, then "patch applied". Failure: one
    ERROR or ANCHOR FAIL line, and nothing is written. Undo is Discard
    Changes in GitHub Desktop.

Written November 4, 2026 with Anthropic's Claude Opus 5.5.
"""

import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
NAME = "LEDGER_CONSOLIDATED.md"

EDITS = [
    (b"""
**Gap:** the two skill versions above (method), then the build: the""",
     b"""
- **Also for ledger-and-session-records' next version, riding the same
  bump (2026-11-04): a section on the brief or prompt for a Claude Code
  session,** under Handoff Structure. Tony asked, 15:55, "Do you advise
  a skill for Code prompts?", and said yes (17:01) to a section in this
  skill rather than a new skill, with the two changes of a review by
  Claude Fable 5.1. Stated in full:
  - the anchor; where the rulings live, and that they win over any
    recommendation; the skills the task fires, with the report stating
    back which were read (L-290);
  - an inventory before any removal, and a stop if a removal reaches
    past its target;
  - stops between slices, each with Tony's look;
  - an irreversible step, such as deleting a file, is Tony's and comes
    last in the run order;
  - a ruling changed inside a prompt is recorded on its ledger item,
    and the prompt is saved verbatim.
  Two lines point at rules held elsewhere and do not restate them: the
  brief tells the session to run the protocol's start check
  (Session-Start Repo Pull); the report ends as Token Economy requires.
- **A candidate, not yet a rule: how many reviews a prompt gets.**
  Proposed: one independent review for a prompt that removes or
  rewrites code; a second only for work that cannot stop safely
  mid-way. Not adopted until measured (Mode 7: review for domain
  uncertainty, not routine). The case so far: L-512's slice (a) prompt
  (the orrery's fallbacks), reviewed six times on Nov 4. The reviews
  changed it before it ran: the animation's writer call, a test suite
  that would have skipped new tests, three more JPL calls without the
  fresh switch. Whether Code's own inventory would have found them is
  settled by A1's report. Until then a review is optional, and whoever
  asks for one says in one line why.
**Gap:** the two skill versions above (method), then the build: the"""),
    (b"""
**Gap:** a design talk (Where We Are, at the next design talk); then a""",
     b"""
- **6AC4721 is not obsolete** (Tony, Nov 4, morning): the entry is kept
  on purpose, as the record of how C/2026 A1 (MAPS) was drawn before
  JPL carried it. Its drawing after L-510 is L-512's part 1.
**Gap:** a design talk (Where We Are, at the next design talk); then a"""),
]


def main():
    if os.path.basename(ROOT) == "documentation":
        print("ERROR: run this from the orrery's root folder, not "
              "documentation/. NOTHING was written.")
        return 1
    path = os.path.join(ROOT, NAME)
    if not os.path.exists(path):
        print("ERROR: %s not found. Save the patch in the orrery's root "
              "folder. NOTHING was written." % NAME)
        return 1
    raw = open(path, "rb").read()
    lf = raw.replace(b"\r\n", b"\n")
    if (b"a section on the brief or prompt for a Claude Code" in lf
            or b"**6AC4721 is not obsolete**" in lf):
        print("ERROR: the ledger already holds this patch's lines: it has "
              "run. Nothing to do. NOTHING was written.")
        return 1
    for old, new in EDITS:
        n = lf.count(old)
        if n != 1:
            print("ANCHOR FAIL: %s: expected 1 match, found %d: %r. If this "
                  "patch already ran, there is nothing to do. NOTHING was "
                  "written." % (NAME, n, old[:60]))
            return 1
        if any(c > 127 for c in new):
            print("ERROR: inserted text holds non-ASCII. NOTHING was written.")
            return 1
        lf = lf.replace(old, new)
        print("ok  %s: %s" % (NAME, old.strip().splitlines()[0][:60]
                              .decode("ascii")))
    with open(path, "wb") as handle:
        handle.write(lf)
    if b"\r\n" in raw:
        print("note: %s was CRLF in the working copy; written LF" % NAME)
    print("patch applied (%d bytes, 1 file)" % len(lf))
    print()
    print("Do next: move this patch into documentation/, then commit and")
    print("push the orrery with your next commit. No maintenance run is")
    print("needed for it: no status or index line changes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
