#!/usr/bin/env python3
"""
patch_L413_5_parallel_sessions_20261005.py -- ORRERY repo. Writes the
three rules for running Earth's website patch and the Horizons design
round as two sessions at once into both handoffs.

Built on orrery be67ca39c5866aa91a8cd140c987add9c007e1aa at
https://github.com/tonylquintanilla/palomas_orrery (gallery
ed48d078ceb639f5f98f13f4c6abc129f722c566 not read or changed).

HOW TO RUN IT
    Save this file in the ORRERY repo ROOT, open it in VS Code and click
    Run. Then follow the NEXT steps.

WHAT CHANGES
    documentation/HANDOFF_L413_earth_orrery_patch_20261005.md   a section,
        "Running beside the Horizons session", and the ledger skill's
        expected version corrected to 1.16.
    documentation/HANDOFF_L395_horizons_check_design_20261005.md   a
        section, "Running beside the website session".
    Both matched only at the lines changed (L-419), so your notes
    elsewhere in either handoff never stop this patch.

SUCCESS looks like: one "ok" line per edit, then "patch applied".
FAILURE looks like: one ERROR: or ANCHOR FAIL: line, and NOTHING is
written. Undo is Discard Changes in GitHub Desktop.

Written October 5, 2026 with Anthropic's Claude Opus 5.5.
"""

import os

ROOT_MARKERS = ("palomas_orrery.py", "LEDGER_CONSOLIDATED.md")
NEXT = ["1. Move this script into documentation/.",
        "2. Commit and push. No maintenance run is needed: only two",
        "   handoffs changed.",
        "3. Start the two sessions, each from its handoff."]

EDITS = {
  'documentation/HANDOFF_L395_horizons_check_design_20261005.md': [
    ('the parallel run',
      '## Tony-actions\n',
      ('## Running beside the website session (Tony, 2026-10-05)\n'
      '\n'
      "Tony asked that this design round and Earth's website patch run as two\n"
      "sessions at once. The website session's handoff,\n"
      '`documentation/HANDOFF_L413_earth_orrery_patch_20261005.md`, carries the\n'
      'same three rules.\n'
      '\n'
      '- DO NOT REWRITE WHERE WE ARE. The website session owns the page this\n'
      "  round. Put this session's updates for the page in this session's\n"
      '  handoff, under a heading saying so; the next rewrite picks them up.\n'
      "- THE OPENING CHECKS ARE THE WEBSITE SESSION'S. This session reads the\n"
      "  version of each skill it loads and compares it with the protocol's\n"
      '  manifest, as always, but leaves closing L-369, L-418 and L-419 to the\n'
      '  website session. In the ledger it edits only L-395, and any item it\n'
      '  opens.\n'
      '- PULL AGAIN BEFORE ANY PATCH. Both sessions start from orrery\n'
      '  be67ca39. Before building a patch, re-read HEAD, build on whatever the\n'
      '  website session has pushed, and name that commit. Ledger edits match\n'
      "  only the lines they change (L-419), so the two sessions' ledger\n"
      '  patches apply in either order.\n'
      '- A design round is conversation first. Tony carries two threads; one\n'
      '  question at a time.\n'
      '\n'
      '## Tony-actions\n'),
      1),
  ],
  'documentation/HANDOFF_L413_earth_orrery_patch_20261005.md': [
    ('next session: the versions and the parallel run',
      ('- Confirms its loaded copies read provenance-discipline 2.26,\n'
      '  interactive-exhibit 1.11, safe-file-editing 1.13,\n'
      '  orrery-coding-conventions 1.10, ledger-and-session-records 1.15 and\n'
      '  gallery-cache-builder 1.7, each opening with its contents list.\n'
      '- Then the website patch above, or the Horizons design round, in\n'
      "  Tony's order.\n"),
      ('- Confirms its loaded copies read provenance-discipline 2.26,\n'
      '  interactive-exhibit 1.11, safe-file-editing 1.13,\n'
      '  orrery-coding-conventions 1.10, ledger-and-session-records 1.16 and\n'
      '  gallery-cache-builder 1.7, each opening with its contents list.\n'
      '  (1.16, not 1.15: patch_L419_1 bumped the ledger skill after this\n'
      '  record was written.)\n'
      '- Then the website patch above.\n'
      '\n'
      '## Running beside the Horizons session (Tony, 2026-10-05)\n'
      '\n'
      'Tony asked that the website patch and the Horizons design round run as\n'
      'two sessions at once. They touch different things; three rules cover\n'
      "the overlap. The Horizons session's handoff carries the same three.\n"
      '\n'
      '- THIS SESSION OWNS WHERE WE ARE this round. It is the only one that\n'
      '  rewrites the page. The Horizons session leaves the page alone and\n'
      "  puts its updates in its own handoff; this session's rewrite, or the\n"
      '  next one after it, picks them up from there.\n'
      '- THIS SESSION DOES THE OPENING CHECKS: it confirms the reinstalled\n'
      "  skills' versions above, closes L-418 and L-419 when they read right,\n"
      "  and closes L-369 on Tony's look at the coordinate box, 2026-10-05:\n"
      '  the "Ecliptic Coordinates (J2000)" box showed the new teal-circle\n'
      '  line, and Tony wrote "beautiful".\n'
      '- PULL AGAIN BEFORE THE FINAL PATCH. Both sessions start from orrery\n'
      '  be67ca39. Before building its last patch, each re-reads HEAD, builds\n'
      '  on whatever the other has pushed, and names that commit. Ledger\n'
      '  edits match only the lines they change (L-419), so two ledger patches\n'
      '  apply in either order; each touches only its own items.\n'
      '- One cost Tony carries: two threads to bring results between. A\n'
      '  session that finds itself asking Tony for more than one thing at a\n'
      '  time waits for the other to finish.\n'),
      1),
  ],
}


def main():
    if os.path.basename(os.getcwd()) == "documentation":
        raise SystemExit("ERROR: run this from the repo ROOT, not from "
                         "documentation/. NOTHING was written.")
    for marker in ROOT_MARKERS:
        if not os.path.isfile(marker):
            raise SystemExit("ERROR: %s is not here, so this is not the "
                             "orrery root. NOTHING was written." % marker)
    results = []
    for path in sorted(EDITS):
        with open(path, "rb") as handle:
            raw = handle.read()
        text = raw.decode("utf-8").replace("\r\n", "\n")
        for label, old, new, want in EDITS[path]:
            found = text.count(old)
            if found != want:
                raise SystemExit("ANCHOR FAIL (%s): expected %d match(es) in "
                                 "%s, found %d. Has this patch already run? "
                                 "NOTHING was written."
                                 % (label, want, path, found))
            text = text.replace(old, new)
            results.append((path, label))
        EDITS[path] = text
    for path in sorted(EDITS):
        with open(path, "wb") as handle:
            handle.write(EDITS[path].encode("utf-8"))
    for path, label in results:
        print("ok  %-60s %s" % (path, label))
    print("")
    print("patch applied")
    print("")
    print("NEXT:")
    for line in NEXT:
        print("  " + line)


if __name__ == "__main__":
    main()
