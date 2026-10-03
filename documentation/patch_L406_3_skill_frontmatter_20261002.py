#!/usr/bin/env python3
"""
patch_L406_3_skill_frontmatter_20261002.py -- ORRERY repo. Fixes the
header of skills/interactive-exhibit/SKILL.md, which Settings refused
with "malformed YAML frontmatter" when Tony reinstalled it after
patch_L406_1.

Built on orrery 94ff6c68d452af26024fbfd3d0741b0f4729cddd
at https://github.com/tonylquintanilla/palomas_orrery
(gallery 0ffa451838dd5753710b3ec77d0d6f2f052f3d96
at https://github.com/tonylquintanilla/tonyquintanilla.github.io;
not touched).

WHAT WENT WRONG. patch_L406_1 put the new words of the skill's
fires_when line ("choosing a feature's info link (NASA or Wikipedia)")
on a line of their own. In YAML, the format of the block between the
two --- lines, a bare second line reads as a broken key, so the
uploader refused the whole file. Claude's mistake: the header was read
cut off at 80 characters and taken to be wrapped. Nothing in the
maintenance run checks the header as YAML; that is recorded as L-407.

WHAT CHANGES
    skills/interactive-exhibit/SKILL.md   the words back on the one
        fires_when line, and one sentence in the version note saying
        so. The version stays 1.10: the broken copy never loaded.
    LEDGER_CONSOLIDATED.md   L-406 records the failure and this fix;
        L-407 opened for the class (no check parses a skill's header,
        and earth-system-pipeline has an older fault of the same kind,
        left alone for now).

Checked here by parsing every skill's header with a YAML reader:
interactive-exhibit now parses, with its name and description.

HOW TO RUN IT
    Save this file in the ORRERY repo ROOT (next to palomas_orrery.py),
    open it in VS Code and click Run. The same as:
        python patch_L406_3_skill_frontmatter_20261002.py

SUCCESS looks like: one "ok" line per edit, then "patch applied".
FAILURE looks like: one ERROR: or ANCHOR FAIL: line, and NOTHING is
written. Undo is Discard Changes in GitHub Desktop.

Written October 2, 2026 with Anthropic's Claude Opus 5.5.
"""

import hashlib
import os

BASE = {'LEDGER_CONSOLIDATED.md': '9d6165103fb23cfe876146cab9564815',
 'skills/interactive-exhibit/SKILL.md': '696a1ad5fe5a2549ebb706584bd45d90'}

EDITS = {'LEDGER_CONSOLIDATED.md': [('L-406: the install failure and its fix',
                             "- **Fixed in passing, reported:** the Sun's "
                             '`_comment` in\n'
                             '  `data/objects_config.json` said the custom '
                             'geometry is "NOT here";\n'
                             '  all four shapes have been there since '
                             'L-234.\n'
                             '**Gap:** Tony: run patch 1, run '
                             '`orrery_maintenance_run.py`, commit and\n'
                             'push the orrery;',
                             "- **Fixed in passing, reported:** the Sun's "
                             '`_comment` in\n'
                             '  `data/objects_config.json` said the custom '
                             'geometry is "NOT here";\n'
                             '  all four shapes have been there since '
                             'L-234.\n'
                             '- **Patch 1 ran and was pushed at orrery '
                             '94ff6c68, 19 of 19 gating.**\n'
                             '  The reinstall of interactive-exhibit 1.10 '
                             'then FAILED: Settings\n'
                             '  refused the file with "malformed YAML '
                             'frontmatter". Claude\'s patch\n'
                             '  put the new fires_when words on a line of '
                             'their own, and YAML reads a\n'
                             '  bare second line as a broken key. Nothing in '
                             'the run could see it:\n'
                             '  skills_index.py rebuilt the manifest from '
                             'the same header without\n'
                             '  complaint (L-407). Fixed by '
                             '`patch_L406_3_skill_frontmatter_20261002.py`,\n'
                             '  which puts the words back on the one line; '
                             'checked by parsing every\n'
                             "  skill's header as YAML. The version stays "
                             '1.10, since 1.10 never\n'
                             '  loaded anywhere.\n'
                             '**Gap:** Tony: run patch 3, run '
                             '`orrery_maintenance_run.py`, commit and\n'
                             'push the orrery, and reinstall '
                             'interactive-exhibit 1.10;'),
                            ('L-407 new item',
                             '#### [L-406] The galactic tide drawn in the '
                             "galaxy's plane (orrery + gallery, the Sun's "
                             'slice)\n',
                             "#### [L-407] A skill's header is not checked "
                             'as YAML (orrery, skills)\n'
                             '<!-- L:407 status:OPEN upd:2026-10-02 '
                             'section:A flag: rice: -->\n'
                             '- **Found 2026-10-02** when Settings refused '
                             'interactive-exhibit 1.10\n'
                             '  with "malformed YAML frontmatter" (L-406). '
                             '`skills_index.py` reads\n'
                             "  each skill's header to build the manifest, "
                             'and read the broken one\n'
                             '  without complaint, so the maintenance run '
                             'passed a skill that could\n'
                             '  not be installed: a check that cannot fail '
                             'on the one fault the\n'
                             '  install step enforces.\n'
                             '- **The same check finds a second, older '
                             'case:**\n'
                             '  `skills/earth-system-pipeline/SKILL.md` has '
                             '": " inside its\n'
                             '  description ("displacement): the restraint '
                             'discipline"), which strict\n'
                             '  YAML refuses. Its installed copy matches the '
                             'repo, so Settings\n'
                             '  accepted it once, under whatever parser it '
                             'had then. It loads today;\n'
                             '  a reinstall may fail. Left as it is, since '
                             'changing it means a\n'
                             '  reinstall of a skill nothing else is '
                             'touching.\n'
                             '**Gap:** Make `skills_index.py` parse each '
                             'header as YAML and fail the\n'
                             'run, naming the skill, when one does not parse '
                             'or lacks name and\n'
                             "description; fix earth-system-pipeline's "
                             'description in the same patch\n'
                             "(quote it), with Tony's reinstall.\n"
                             '**Ref:** L-406; `skills_index.py`; '
                             '`skills/*/SKILL.md`.\n'
                             '\n'
                             '#### [L-406] The galactic tide drawn in the '
                             "galaxy's plane (orrery + gallery, the Sun's "
                             'slice)\n')],
 'skills/interactive-exhibit/SKILL.md': [('fires_when back on one line',
                                          'carding an exhibit in Studio;\n'
                                          "choosing a feature's info link "
                                          '(NASA or Wikipedia)\n'
                                          '---\n',
                                          'carding an exhibit in Studio; '
                                          "choosing a feature's info link "
                                          '(NASA or Wikipedia)\n'
                                          '---\n'),
                                         ('version note: header re-joined',
                                          'written; the hover and the '
                                          'drawing were covered and the link '
                                          'was not.\n'
                                          'Earlier: 1.9 |',
                                          'written; the hover and the '
                                          'drawing were covered and the link '
                                          'was not.\n'
                                          'The same day Settings refused the '
                                          'first copy ("malformed YAML\n'
                                          'frontmatter"): the new fires_when '
                                          'words sat on a line of their '
                                          'own.\n'
                                          'They are back on the one line, '
                                          'and the version stays 1.10, which '
                                          'never\n'
                                          'loaded anywhere (L-406, L-407).\n'
                                          'Earlier: 1.9 |')]}


def fingerprint(raw):
    return hashlib.md5(raw.replace(b"\r\n", b"\n")).hexdigest()


def main():
    if os.path.basename(os.getcwd()) == "documentation":
        raise SystemExit("ERROR: run this from the ORRERY repo ROOT, next to "
                         "palomas_orrery.py -- not from documentation/. "
                         "NOTHING was written.")
    if not os.path.isfile("palomas_orrery.py"):
        raise SystemExit("ERROR: palomas_orrery.py is not here, so this is "
                         "not the orrery root. NOTHING was written.")
    results = []
    for path in sorted(EDITS):
        with open(path, "rb") as handle:
            raw = handle.read()
        got = fingerprint(raw)
        if got != BASE[path]:
            raise SystemExit(
                "ERROR: %s is not the file this patch was built against.\n"
                "       expected %s, found %s. It has changed since\n"
                "       94ff6c68, or this patch has already run.\n"
                "       (Line endings are excluded, so they are not the cause.)\n"
                "       NOTHING was written." % (path, BASE[path], got))
        nl = "\r\n" if b"\r\n" in raw else "\n"
        text = raw.decode("utf-8").replace("\r\n", "\n")
        done = []
        for label, old, new in EDITS[path]:
            if text.count(old) != 1:
                raise SystemExit("ANCHOR FAIL (%s): expected 1 match in %s, "
                                 "found %d. NOTHING was written."
                                 % (label, path, text.count(old)))
            text = text.replace(old, new)
            done.append(label)
        results.append((path, text.replace("\n", nl), done))
    for path, text, done in results:
        with open(path, "wb") as handle:
            handle.write(text.encode("utf-8"))
        for label in done:
            print("ok  %-46s %s" % (path, label))
    print("")
    print("patch applied")
    print("")
    print("NEXT:")
    print("  1. Run orrery_maintenance_run.py (VS Code, Run). Expect 19 of")
    print("     19 gating checkers.")
    print("  2. Move this script into documentation/; commit and push.")
    print("  3. Settings > Skills: upload skills/interactive-exhibit/SKILL.md")
    print("     again. It should now be accepted as 1.10.")
    print("  4. Replace the Project's instructions with PROJECT_INSTRUCTIONS.md")
    print("     v3.78 (unchanged by this patch).")
    print("  5. Then the gallery patch, patch_L406_2, as its notes say.")

if __name__ == "__main__":
    main()
