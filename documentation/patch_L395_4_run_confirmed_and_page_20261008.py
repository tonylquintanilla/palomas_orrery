#!/usr/bin/env python3
"""
patch_L395_4_run_confirmed_and_page_20261008.py -- ORRERY repo. Records
Tony's run of the Horizons design patch on L-395 (the Horizons check),
and edits Where We Are by section for what the build waits on.

Built on orrery 3b36b3bf7fb7f0b040e9246b87359a8f112a1c88 at
https://github.com/tonylquintanilla/palomas_orrery (gallery
ab66aba70a5874b033742a8428070b5889484490 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io; not
touched by this patch).

HOW TO RUN IT
    Save this file in the ORRERY repo's root folder (the one with
    palomas_orrery.py), open it in VS Code, click Run. It asks nothing.
    The same as: python patch_L395_4_run_confirmed_and_page_20261008.py
    It refuses to run from documentation/. Then follow the NEXT steps
    it prints.

WHAT CHANGES
    LEDGER_CONSOLIDATED.md -- L-395 (the Horizons check): its date, and
        one line recording Tony's run of patch_L395_3 from his own run
        record; the header stamp. Nothing else in the ledger.
    documentation/WHERE_WE_ARE.md -- edited by section, never whole
        (ledger-and-session-records 1.17): the header's date line; road
        stage 8; one line under Waiting on you > Decisions. Nothing
        below the run-record marker is touched.

HOW IT CHECKS ITS BASE
    Each file is checked only at the lines this patch edits; each anchor
    must appear exactly once. Your notes anywhere else are kept.

SUCCESS looks like one "ok" line per edit, then "patch applied".
FAILURE looks like one ERROR: or ANCHOR FAIL: line, and NOTHING is
written. Undo is Discard Changes in GitHub Desktop.

Written October 8, 2026 with Anthropic's Claude Opus 5.5.
"""
import os

LEDGER = "LEDGER_CONSOLIDATED.md"
PAGE = "documentation/WHERE_WE_ARE.md"

EDITS = {
    LEDGER: [
        ("header stamp",
         "36176d50.\nReview and RICE update Tony 6-21-2026\n",
         "36176d50.\n"
         "Module updated: October 8, 2026 with Anthropic's Claude Opus 5.5\n"
         "(L-395: Tony's run of the Horizons design patch recorded from his\n"
         "run record), built on 3b36b3bf.\n"
         "Review and RICE update Tony 6-21-2026\n"),
        ("L-395 date",
         "<!-- L:395 status:OPEN upd:2026-10-07 section:A flag: rice: -->",
         "<!-- L:395 status:OPEN upd:2026-10-08 section:A flag: rice: -->"),
        ("L-395 Tony's run",
         "- (decide) At the build: whether Halley is keyed and checked too; and\n"
         "  Encke's description and link.\n",
         "- (decide) At the build: whether Halley is keyed and checked too; and\n"
         "  Encke's description and link.\n"
         "- **Tony's run of patch_L395_3, 2026-10-07** [his run record, written\n"
         "  at the foot of\n"
         "  `documentation/HANDOFF_L395_horizons_check_design_20261005.md`]:\n"
         "  all four ledger edits and both new files ok; the maintenance run\n"
         "  20 of 20 gating; pushed at 8653ef1b. A second run on 2026-10-08,\n"
         "  from a leftover copy in the orrery root, refused as designed and\n"
         "  wrote nothing; the leftover is deleted by hand.\n"),
    ],
    PAGE: [
        ("header date",
         "Last updated: October 8, 2026, end of the typed facts session.\n"
         "- Written at orrery 36176d50 and gallery ab66aba7, before your run of\n"
         "  this closing patch.\n",
         "Last updated: October 8, 2026, after the Horizons design's close.\n"
         "- Written at orrery 3b36b3bf and gallery ab66aba7, before your run of\n"
         "  patch_L395_4.\n"),
        ("road stage 8",
         "  8.   [next]  The served objects are checked against JPL Horizons.\n"
         "               Designed; build next.\n",
         "  8.   [next]  The served objects are checked against JPL Horizons.\n"
         "               Designed and recorded; build next, with Encke added\n"
         "               to the orrery's list. << new this session\n"),
        ("decisions: the Horizons build",
         "Decisions, one at a time:\n",
         "Decisions, one at a time:\n"
         "- At the Horizons check's build, L-395 (the Horizons check): whether\n"
         "  Halley is checked too, and Encke's description and link.\n"),
    ],
}

MARKER = "--- Your run record below this line"


def main():
    if os.path.basename(os.getcwd()) == "documentation":
        raise SystemExit("ERROR: run this from the ORRERY repo ROOT, next to "
                         "palomas_orrery.py -- not from documentation/. "
                         "NOTHING was written.")
    if not os.path.isfile("palomas_orrery.py"):
        raise SystemExit("ERROR: palomas_orrery.py is not here, so this is "
                         "not the orrery root. NOTHING was written.")
    results = []
    for path, edits in EDITS.items():
        with open(path, "rb") as handle:
            raw = handle.read()
        was_crlf = b"\r\n" in raw
        text = raw.replace(b"\r\n", b"\n").decode("utf-8")
        before = sum(1 for ch in text if ord(ch) > 127)
        cut = text.find(MARKER) if path == PAGE else -1
        if path == PAGE and cut < 0:
            raise SystemExit("ANCHOR FAIL: the run-record marker is not in %s. "
                             "NOTHING was written." % path)
        done = []
        for label, old, new in edits:
            count = text.count(old)
            if count != 1:
                raise SystemExit("ANCHOR FAIL (%s): expected 1 match in %s, "
                                 "found %d. NOTHING was written."
                                 % (label, path, count))
            if path == PAGE and text.find(old) > cut:
                raise SystemExit("ERROR (%s): the anchor is below the run-record "
                                 "marker. NOTHING was written." % label)
            text = text.replace(old, new)
            done.append(label)
        if sum(1 for ch in text if ord(ch) > 127) > before:
            raise SystemExit("ERROR: %s would hold new non-ASCII text. "
                             "NOTHING was written." % path)
        if path == PAGE:
            above = text[:text.find(MARKER)].count("\n")
            if above > 130:
                raise SystemExit("ERROR: %s would have %d lines above the "
                                 "marker; the cap is 130. NOTHING was written."
                                 % (path, above))
        results.append((path, text, done, was_crlf))
    for path, text, done, was_crlf in results:
        with open(path, "wb") as handle:
            handle.write(text.encode("utf-8"))
        for label in done:
            print("ok  %-30s %s" % (path.split("/")[-1], label))
        if was_crlf:
            print("note: %s was CRLF in the working copy; written LF" % path)
    print("")
    print("patch applied")
    print("")
    print("NEXT:")
    print("  1. Run orrery_maintenance_run.py -- it rebuilds the ledger's index.")
    print("  2. Move this script into documentation/; commit and push.")


if __name__ == "__main__":
    main()
