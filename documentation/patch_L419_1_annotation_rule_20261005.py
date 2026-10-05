#!/usr/bin/env python3
"""
patch_L419_1_annotation_rule_20261005.py -- ORRERY repo. Writes Tony's
rule into ledger-and-session-records 1.16: a patch checks Where We Are,
a handoff or the ledger only at the lines it edits (L-419).

Built on orrery d9f47a875 at
https://github.com/tonylquintanilla/palomas_orrery PLUS
patch_L413_4_session_close_20261005.py, which must run FIRST: this one
edits lines that patch writes. (gallery ed48d078 not read or changed.)

HOW TO RUN IT
    After patch_L413_4 has run, save this file in the ORRERY repo ROOT,
    open it in VS Code and click Run. Then follow the NEXT steps.

WHAT CHANGES
    skills/ledger-and-session-records/SKILL.md   1.16: the rule, under
        Where We Are -- Tony's page; its v1.13 entry moves out by the
        three-entry rule.
    documentation/SKILL_HISTORIES.md   receives that v1.13 entry.
    PROJECT_INSTRUCTIONS.md   v3.82: header, anchor, entry; v3.79 moves
        down.
    documentation/PROJECT_INSTRUCTIONS_HISTORY.md   receives v3.79.
    LEDGER_CONSOLIDATED.md, documentation/WHERE_WE_ARE.md and this
        session's handoff   a few lines each, matched ONLY at those lines,
        as the new rule says. Your notes anywhere else in them never stop
        this patch.

TESTED on a copy of d9f47a87 with patch_L413_4 run first: every edit
landed; Skill headers passes, the contents list included;
orrery_maintenance_run.py passed every gating checker.

SUCCESS looks like: one "ok" line per edit, then "patch applied".
FAILURE looks like: one ERROR: or ANCHOR FAIL: line, and NOTHING is
written. Undo is Discard Changes in GitHub Desktop.

Written October 5, 2026 with Anthropic's Claude Opus 5.5.
"""

import hashlib
import os

REPO = "orrery"
ROOT_MARKERS = ("palomas_orrery.py", "LEDGER_CONSOLIDATED.md")
ZONED = {"PROJECT_INSTRUCTIONS.md": ("<!-- SKILL-MANIFEST:START",
                                     "<!-- SKILL-MANIFEST:END -->")}
NEXT = ["1. Move this script into documentation/.",
        "2. Run orrery_maintenance_run.py; every gating checker passes.",
        "3. Commit and push.",
        "4. Reinstall ledger-and-session-records in Settings > Skills, and",
        "   replace the Project's instructions with PROJECT_INSTRUCTIONS.md",
        "   (v3.82)."]

BASE = {
    'PROJECT_INSTRUCTIONS.md': '357dcb515983c3a423268dcd4560f8d8',
    'documentation/PROJECT_INSTRUCTIONS_HISTORY.md': '5208f3c485ed9f3cac2a8a60efe02c96',
    'documentation/SKILL_HISTORIES.md': 'e1e09da4957186a6d965560e58c85203',
    'skills/ledger-and-session-records/SKILL.md': 'aa7aab7f1bc86238a1eba9bce325857b',
}

ANCHOR_ONLY = ('LEDGER_CONSOLIDATED.md', 'documentation/HANDOFF_L413_earth_orrery_patch_20261005.md', 'documentation/WHERE_WE_ARE.md',)

EDITS = {
  'LEDGER_CONSOLIDATED.md': [
    ('header stamp',
      ("L-416 and L-417 closed after Tony's runs; L-419 opened), built on\n"
      'd9f47a87.\n'),
      ("L-416 and L-417 closed after Tony's runs; L-419 opened), built on\n"
      'd9f47a87.\n'
      "Module updated: October 5, 2026 with Anthropic's Claude Opus 5.5\n"
      '(L-419: the annotation rule written into ledger-and-session-records\n'
      "1.16, protocol v3.82), built on patch_L413_4's tree over d9f47a87.\n"),
      1),
    ('L-419 written into the skill',
      ('**Gap:** write the rule into ledger-and-session-records (Where We Are,\n'
      "handoffs, the ledger) -- Tony's word on when.\n"),
      ('- **Written into the skill, 2026-10-05,** on Tony\'s word: "yes because\n'
      '  I am using our handoffs or the where we are as run records." Also\n'
      '  Tony: "I remember that I did annotate the where we are early in the\n'
      '  session so the patch found it that way."\n'
      '  `patch_L419_1_annotation_rule_20261005.py`: ledger-and-session-records\n'
      "  1.16, under Where We Are -- Tony's page; protocol v3.82.\n"
      '**Gap:** Tony runs the patch, reinstalls the skill and replaces the\n'
      "Project's instructions; the next session confirms its loaded copy\n"
      'reads 1.16.\n'),
      1),
  ],
  'PROJECT_INSTRUCTIONS.md': [
    ('header stamp',
      'Tony Quintanilla, PE | Claude | v3.81 | October 5, 2026\n',
      'Tony Quintanilla, PE | Claude | v3.82 | October 5, 2026\n',
      1),
    ('SHA anchor',
      'Cut from 72e3b558 at https://github.com/tonylquintanilla/palomas_orrery\n',
      'Cut from d9f47a87 at https://github.com/tonylquintanilla/palomas_orrery\n',
      1),
    ('v3.82 entry',
      'v3.81 (October 5, 2026): No rule changed in this document. SIX\n',
      ('v3.82 (October 5, 2026): No rule changed in this document. ONE\n'
      'skill bump, one version (L-419): ledger-and-session-records 1.15 ->\n'
      "1.16. A PATCH NEVER REFUSES TONY'S NOTES.\n"
      '\n'
      "WHAT PROMPTED IT. The session's closing patch, patch_L413_3, guarded\n"
      'documentation/WHERE_WE_ARE.md by a fingerprint of the whole file and\n'
      'refused: Tony had marked two lines "-- done" and dated the header.\n'
      'Tony: "i though annotations would not be refused." His rule of\n'
      '2026-10-03 had said exactly that, but it lived only in one earlier\n'
      "patch's code, so a later session did not have it. Asked whether it goes\n"
      'into the skill now or later: "yes because I am using our handoffs or\n'
      'the where we are as run records."\n'
      '\n'
      'WHAT CHANGED. ledger-and-session-records, under Where We Are: a patch\n'
      'checks Where We Are, a handoff or the ledger only at the lines it\n'
      'edits, never by a whole-file fingerprint; a rewrite of Where We Are\n'
      "first copies every line Tony changed into the session's handoff and\n"
      'prints them. patch_L413_4 is the worked example. Its v1.13 entry moved\n'
      'to documentation/SKILL_HISTORIES.md, by the three-entry rule.\n'
      '\n'
      'THE OBLIGATION TRAVELS. A reinstall during a session is not visible to\n'
      'that session. The next session confirms its loaded copy reads\n'
      'ledger-and-session-records 1.16, along with the five other skills\n'
      'v3.81 named.\n'
      '\n'
      'The header stamp and the SHA anchor move with this entry.\n'
      '\n'
      'Version history: v3.79 moves down to\n'
      'documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three\n'
      'resident.\n'
      '\n'
      'v3.81 (October 5, 2026): No rule changed in this document. SIX\n'),
      1),
    ('v3.79 moves down',
      ('v3.79 (October 2, 2026): No rule changed in this document. TWO\n'
      'skill bumps, one version each (L-407): earth-system-pipeline 1.1 ->\n'
      "1.2 and provenance-discipline 2.24 -> 2.25. A SKILL'S HEADER IS READ\n"
      'AS YAML.\n'
      '\n'
      'WHAT PROMPTED IT. Settings refused interactive-exhibit 1.10 with\n'
      '"malformed YAML frontmatter": patch_L406_1 had put new fires_when words\n'
      'on a line of their own; patch_L406_3, pushed at 81e19ef, put them back\n'
      'on one line, still 1.10. skills_index.py had read the same header by its\n'
      'own looser rules and built the manifest without complaint, and as a\n'
      'generator its exit code did not count, so the maintenance run passed 19\n'
      "of 19 on a skill that could not be installed. Tony's word, 2026-10-02:\n"
      'do L-407 now.\n'
      '\n'
      'WHAT CHANGED. skills_index.py reads every header as YAML, with PyYAML\n'
      'where installed and built-in rules otherwise, names which, and fails on\n'
      'a header YAML refuses, one with no name or description as text, or a\n'
      'value YAML silently cuts short at " #". orrery_maintenance_run.py runs\n'
      'it with --check as the checker Skill headers. The check found two more:\n'
      'earth-system-pipeline\'s description held ": ", which YAML refuses; and\n'
      'provenance-discipline\'s held "# Source:", so YAML read only its first\n'
      '200 characters, and the installed skill has been chosen by that cut\n'
      'description. Both descriptions are now quoted. No rule in any skill\n'
      'changed.\n'
      '\n'
      'THE OBLIGATION TRAVELS. This session loaded interactive-exhibit 1.9,\n'
      'earth-system-pipeline 1.1 and provenance-discipline 2.24. The next\n'
      'session confirms its loaded copies read 1.10, 1.2 and 2.25, and that\n'
      'provenance-discipline\'s description no longer ends at "adding or\n'
      'reviewing".\n'
      '\n'
      'The header stamp and the SHA anchor move with this entry.\n'
      '\n'
      'Version history: v3.76 moves down to\n'
      'documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three\n'
      'resident.\n'
      '\n'),
      '',
      1),
  ],
  'documentation/HANDOFF_L413_earth_orrery_patch_20261005.md': [
    ('the decision taken',
      ('(decide)\n'
      '- L-419: when to write the annotation rule into\n'
      '  ledger-and-session-records (one more reinstall).'),
      ('- Run patch_L419_1, reinstall ledger-and-session-records (1.16), and\n'
      "  replace the Project's instructions with v3.82. Tony's word on\n"
      '  L-419, 2026-10-05: write the rule now.'),
      1),
  ],
  'documentation/PROJECT_INSTRUCTIONS_HISTORY.md': [
    ('v3.79 received',
      ('v3.81 made a fourth entry.)\n'
      '\n'
      '================================================================\n'
      'PART 2'),
      ('v3.81 made a fourth entry.)\n'
      '\n'
      'v3.79 (October 2, 2026): No rule changed in this document. TWO\n'
      'skill bumps, one version each (L-407): earth-system-pipeline 1.1 ->\n'
      "1.2 and provenance-discipline 2.24 -> 2.25. A SKILL'S HEADER IS READ\n"
      'AS YAML.\n'
      '\n'
      'WHAT PROMPTED IT. Settings refused interactive-exhibit 1.10 with\n'
      '"malformed YAML frontmatter": patch_L406_1 had put new fires_when words\n'
      'on a line of their own; patch_L406_3, pushed at 81e19ef, put them back\n'
      'on one line, still 1.10. skills_index.py had read the same header by its\n'
      'own looser rules and built the manifest without complaint, and as a\n'
      'generator its exit code did not count, so the maintenance run passed 19\n'
      "of 19 on a skill that could not be installed. Tony's word, 2026-10-02:\n"
      'do L-407 now.\n'
      '\n'
      'WHAT CHANGED. skills_index.py reads every header as YAML, with PyYAML\n'
      'where installed and built-in rules otherwise, names which, and fails on\n'
      'a header YAML refuses, one with no name or description as text, or a\n'
      'value YAML silently cuts short at " #". orrery_maintenance_run.py runs\n'
      'it with --check as the checker Skill headers. The check found two more:\n'
      'earth-system-pipeline\'s description held ": ", which YAML refuses; and\n'
      'provenance-discipline\'s held "# Source:", so YAML read only its first\n'
      '200 characters, and the installed skill has been chosen by that cut\n'
      'description. Both descriptions are now quoted. No rule in any skill\n'
      'changed.\n'
      '\n'
      'THE OBLIGATION TRAVELS. This session loaded interactive-exhibit 1.9,\n'
      'earth-system-pipeline 1.1 and provenance-discipline 2.24. The next\n'
      'session confirms its loaded copies read 1.10, 1.2 and 2.25, and that\n'
      'provenance-discipline\'s description no longer ends at "adding or\n'
      'reviewing".\n'
      '\n'
      'The header stamp and the SHA anchor move with this entry.\n'
      '\n'
      'Version history: v3.76 moves down to\n'
      'documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three\n'
      'resident.\n'
      '\n'
      '(Moved down from the resident protocol on 2026-10-05 when\n'
      'v3.82 made a fourth entry.)\n'
      '\n'
      '================================================================\n'
      'PART 2'),
      1),
  ],
  'documentation/SKILL_HISTORIES.md': [
    ('ledger skill: v1.13 received',
      ('\n'
      '## gallery-cache-builder\n'),
      ('\n'
      "v1.13 (L-396; 2026-09-30, with Anthropic's Claude Opus 5.5) adds Where\n"
      'We Are to The Document Stack: `documentation/WHERE_WE_ARE.md`, one page\n'
      'written for Tony rather than for the work, rewritten in place inside\n'
      "every session's ledger patch, with this session's changes marked and\n"
      'the must-reads in italics. Tony, 2026-09-30: "i struggle to keep the\n'
      'big picture. it\'s the old dilemma of loosing the forest for the trees."\n'
      '\n'
      '## gallery-cache-builder\n'),
      1),
  ],
  'documentation/WHERE_WE_ARE.md': [
    ('changed this session: the rule',
      ('> - The check of the object list against JPL Horizons has its own\n'
      '>   handoff, for a fresh session.\n'),
      ('> - The check of the object list against JPL Horizons has its own\n'
      '>   handoff, for a fresh session.\n'
      '> - Your notes in this page, the handoffs and the ledger are protected\n'
      '>   by a written rule now: a patch checks only the lines it edits.\n'),
      1),
    ('needs you now',
      '> - *Whether to write the annotation rule into the ledger skill now.*\n',
      ('> - *Run the skill patch, reinstall ledger-and-session-records, and\n'
      ">   replace the Project's instructions with v3.82.*\n"),
      1),
    ('waiting on you, now',
      ('- Whether the rule "a patch checks a document you annotate only at the\n'
      '  lines it edits" goes into the ledger skill now, at the cost of one\n'
      '  more reinstall, or with the next skill change.\n'),
      ('- Run patch_L419_1, reinstall ledger-and-session-records, and replace\n'
      "  the Project's instructions with PROJECT_INSTRUCTIONS.md, now v3.82.\n"),
      1),
  ],
  'skills/ledger-and-session-records/SKILL.md': [
    ('v1.16 entry',
      'Skill version: 1.15 | ',
      ("Skill version: 1.16 | 2026-10-05, with Anthropic's Claude Opus 5.5, at\n"
      'palomas_orrery @ d9f47a87. v1.16 (L-419) adds one rule under Where We\n'
      "Are -- Tony's page: a patch checks a document Tony annotates (this\n"
      'page, the handoffs, the ledger) only at the lines it edits, and a\n'
      'rewrite of the page carries his notes into the handoff first. The\n'
      "rule had lived only in one patch's code and was broken the same day.\n"
      'Earlier: 1.15 | '),
      1),
    ('v1.13 moves to SKILL_HISTORIES.md',
      ("v1.13 (L-396; 2026-09-30, with Anthropic's Claude Opus 5.5) adds Where\n"
      'We Are to The Document Stack: `documentation/WHERE_WE_ARE.md`, one page\n'
      'written for Tony rather than for the work, rewritten in place inside\n'
      "every session's ledger patch, with this session's changes marked and\n"
      'the must-reads in italics. Tony, 2026-09-30: "i struggle to keep the\n'
      'big picture. it\'s the old dilemma of loosing the forest for the trees."\n'),
      '',
      1),
    ('the annotation rule (L-419)',
      '  the picture delivers a small one. The patch writes the whole file.\n',
      ('  the picture delivers a small one. The patch writes the whole file.\n'
      '- TONY ANNOTATES THIS PAGE, THE HANDOFFS AND THE LEDGER, and a patch\n'
      '  never refuses his notes (L-419; Tony, 2026-10-03, and 2026-10-05: "i\n'
      '  am using our handoffs or the where we are as run records"). He writes\n'
      '  run records, pushed SHAs and comments into them. So a patch checks\n'
      '  each of the three only at the lines it edits -- an anchor that must\n'
      '  match there -- never by a fingerprint of the whole file. A rewrite of\n'
      '  this page, which writes the whole file, first finds every line that\n'
      '  differs from the copy the patch was built on, copies those lines word\n'
      "  for word into the session's handoff, prints them, and refuses only if\n"
      '  the file is not the page it replaces.\n'
      '  `documentation/patch_L413_4_session_close_20261005.py` is the worked\n'
      '  example. The failure this prevents: patch_L413_3 fingerprinted the\n'
      '  whole page and refused on two "-- done" marks; Tony, "i though\n'
      '  annotations would not be refused."\n'),
      1),
  ],
}


def md5(text):
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def read_lf(path):
    with open(path, "rb") as handle:
        raw = handle.read()
    return raw.decode("utf-8").replace("\r\n", "\n"), b"\r\n" in raw


def outside_zone(path, text):
    if path not in ZONED:
        return text
    start, end = ZONED[path]
    a = text.index(start)
    b = text.index(end) + len(end)
    return text[:a] + text[b:]


def main():
    if os.path.basename(os.getcwd()) == "documentation":
        raise SystemExit("ERROR: run this from the repo ROOT, not from "
                         "documentation/. NOTHING was written.")
    for marker in ROOT_MARKERS:
        if not os.path.isfile(marker):
            raise SystemExit("ERROR: %s is not here, so this is not the %s "
                             "root. NOTHING was written." % (marker, REPO))
    results = []
    for path in sorted(EDITS):
        if not os.path.isfile(path):
            raise SystemExit("ERROR: %s is not here. Run patch_L413_4 first. "
                             "NOTHING was written." % path)
        text, was_crlf = read_lf(path)
        if path not in ANCHOR_ONLY and md5(outside_zone(path, text)) != BASE[path]:
            raise SystemExit(
                "ERROR: %s is not the file this patch was built against\n"
                "       (d9f47a87), or this patch has already run.\n"
                "       (Line endings are excluded, so they are not the cause.)\n"
                "       NOTHING was written." % path)
        done = []
        for label, old, new, want in EDITS[path]:
            found = text.count(old)
            if found != want:
                hint = (" Has patch_L413_4 run? Or has this patch already run?"
                        if path in ANCHOR_ONLY else "")
                raise SystemExit("ANCHOR FAIL (%s): expected %d match(es) in "
                                 "%s, found %d.%s NOTHING was written."
                                 % (label, want, path, found, hint))
            text = text.replace(old, new)
            done.append(label)
        results.append((path, text, done, was_crlf))
    for path, text, done, was_crlf in results:
        with open(path, "wb") as handle:
            handle.write(text.encode("utf-8"))
        for label in done:
            print("ok  %-58s %s" % (path, label))
        if was_crlf:
            print("note: %s was CRLF in the working copy; written LF" % path)
    print("")
    print("patch applied")
    print("")
    print("NEXT:")
    for line in NEXT:
        print("  " + line)


if __name__ == "__main__":
    main()
