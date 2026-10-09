#!/usr/bin/env python3
"""
patch_L418_4_close_20261008.py -- the close of the split session (L-418).

HOW TO RUN: save this file in the orrery folder (the one holding
LEDGER_CONSOLIDATED.md), open it in VS Code and click Run. From a
terminal: python patch_L418_4_close_20261008.py. It asks nothing.

WHAT IT DOES. Records Tony's run of patch_L418_3 and the push, read from
his run record of 2026-10-08
(documentation/WHERE_WE_ARE_10-8-26_1406_run_record.md); opens one ledger
item for the citation-location checks (the decision in
documentation/TESTING_PROTOCOL_provenance_skills_20261008.md, section
B4); notes on L-351 two things the next bumps owe; updates Where We Are
by section (the box, the decisions list, the details); and adds an
"After the run" section to the session's handoff. Nothing below the
run-record marker is touched.

Every edit is anchored on lines this session wrote or owns; a line
changed first by someone else makes the patch stop with ANCHOR FAIL and
write nothing. A second run refuses. Undo is Discard Changes in GitHub
Desktop.

SUCCESS: one "ok" line per edit, then "patch applied".

Built on orrery e5cc4bb21cdb69afe1393d394df704700f50f716 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Written October 8, 2026 with Anthropic's Claude Opus 5.5.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent
BASE = 'e5cc4bb2'
TODAY = '2026-10-08'
LEDGER = 'LEDGER_CONSOLIDATED.md'
WWA = 'documentation/WHERE_WE_ARE.md'
HANDOFF = 'documentation/HANDOFF_L418_split_build_20261008.md'
MARKER = '--- Your run record below this line.'
DONE_MARK = 'patch_L418_4 (the close)'


class Refuse(Exception):
    pass


def read_lf(rel):
    path = ROOT / rel
    if not path.is_file():
        raise Refuse(f"ERROR: {rel} not found. Run this from the orrery folder.")
    text = path.read_bytes().decode('utf-8')
    if '\r\n' in text:
        print(f"note: {rel} was CRLF in the working copy; it is written LF")
    return text.replace('\r\n', '\n')


def edit(text, old, new, rel, label):
    n = text.count(old)
    if n != 1:
        raise Refuse(f"ANCHOR FAIL: {rel}: {label}: expected 1 match, found "
                     f"{n}.\n  anchor starts: {old[:90]!r}")
    print(f"ok  {rel:48s} {label}")
    return text.replace(old, new)


def block_span(ledger, n):
    m = re.search(r'^#### \[L-%d\][^\n]*\n' % n, ledger, re.M)
    if not m:
        raise Refuse(f"ANCHOR FAIL: {LEDGER}: item L-{n} not found.")
    nxt = re.compile(r'^(#### \[L-|## )', re.M).search(ledger, m.end())
    return m.start(), (nxt.start() if nxt else len(ledger))


def block_edit(ledger, n, old, new, label):
    a, b = block_span(ledger, n)
    blk = ledger[a:b]
    if blk.count(old) != 1:
        raise Refuse(f"ANCHOR FAIL: {LEDGER}: L-{n}: {label}: expected 1 "
                     f"match inside the item, found {blk.count(old)}.")
    print(f"ok  {LEDGER:48s} L-{n}: {label}")
    return ledger[:a] + blk.replace(old, new) + ledger[b:]


def touch_meta(ledger, n):
    a, b = block_span(ledger, n)
    blk = ledger[a:b]
    m = re.search(r'(<!-- L:%d status:\S+ upd:)(\S+)( )' % n, blk)
    if not m:
        raise Refuse(f"ANCHOR FAIL: {LEDGER}: L-{n}: metadata line not found.")
    blk = blk[:m.start(2)] + TODAY + blk[m.end(2):]
    print(f"ok  {LEDGER:48s} L-{n}: date")
    return ledger[:a] + blk + ledger[b:]


# ------------------------------------------------------------------
# THE LEDGER
# ------------------------------------------------------------------

L418_OLD_GAP = """\
**Gap:** Tony runs the patch and orrery_maintenance_run.py, pushes,
installs three skills (provenance-discipline, provenance-cross-check,
ledger-and-session-records) and replaces the Project's instructions with
PROJECT_INSTRUCTIONS.md v3.86. The next session confirms its loaded
copies read 2.27, 1.0 and 1.18, finds both skills' reference files,
and on its first figures task says whether it opened the figures
reference file first; then this item closes.
"""

L418_RUN = """\
- **2026-10-08, run and pushed** (Tony's run record,
  `documentation/WHERE_WE_ARE_10-8-26_1406_run_record.md`). The patch
  wrote all 13 files. Its last check failed on its first run, on two
  untracked `SKILL.md.bak` files sitting in the orrery-coding-conventions
  and safe-file-editing folders on Tony's machine: a stray file in a
  skill folder would ride into an install. Tony deleted them; the
  maintenance run then passed 20 of 20, Skill headers 12 skills. Pushed
  at ea2c0e16. Tony installed the three skills and replaced the
  Project's instructions ("done"); pushed at e5cc4bb2.
- **2026-10-08, the installed copies read in the same session.** After
  the install, this session's mounted skills showed
  provenance-discipline 2.27, provenance-cross-check 1.0 and
  ledger-and-session-records 1.18, with all three reference files: tests
  A1 and A2 of the testing protocol. The protocol's Stale Skill gate says
  a mid-session install cannot be seen; this one could. Recorded on
  L-351 for the protocol's next bump; the gate's rule stands until then.
- **2026-10-08, the testing protocol:**
  `documentation/TESTING_PROTOCOL_provenance_skills_20261008.md`. Part
  A tests that the skills load and fire; Part B measures what checks a
  citation's location record today (L-%(n)d).
- **Two skill ZIPs were committed into `skills/`** (682c5395),
  `provenance-cross-check.zip` and `provenance-discipline.zip`. They are
  not skill folders, so the check passes, but each goes stale the next
  time its skill changes. Recommended: delete them; the install is done.
**Gap:** the next fresh session runs tests A3 to A6 of the testing
protocol and says what it found; then this item closes.
"""


def new_item(n):
    return """\
#### [L-%(n)d] A citation's location record is checked only in part (provenance tooling)
<!-- L:%(n)d status:OPEN upd:%(t)s section:A flag: rice: -->
- **Measured 2026-10-08** at orrery %(b)s, for Tony's question: "how
  do we ensure that a citation's location record is correct and not
  broken or missing. is this check included in the scanner?" The answer
  is no: the scanner checks that a citation sits near a number, not
  where it points. The full table is section B of
  `documentation/TESTING_PROTOCOL_provenance_skills_20261008.md`.
- What is checked: a missing Source line (scanner, Tier-1, gates the
  push); a V_SOURCED row with no Source line (test_status_lines.py,
  gates); a worksheet named in a Cross-checked line and missing
  (worksheet_checker.py layer L0, report-only).
- What is not: a missing Access line (20 of 61 sourced or cross-checked
  rows in constants_new.py have none, among them KM_PER_AU and
  SUN_RADIUS_KM); a missing Read line (4 of 61); a record file named on
  a Read line and missing (17 named, all present today); a web address
  that no longer opens (40 distinct addresses, never tested); and
  whether the page says the number, which no tool can check.
- **Three levels proposed, cheapest first:** (1) every file a citation
  names exists, failing the run; (2) every sourced row carries an Access
  line with an address and a date, reported by name first and failing
  only after Tony rules which rows are excused; (3) a link check that
  visits each address, run on Tony's machine, report-only. (1) and (2)
  would be rules in test_status_lines.py, which the maintenance run
  already has.
  **Tony-action (decide):** which to build. Recommended: (1) and (2)
  together in one session; (3) later, as its own small tool.
**Gap:** Tony's decision above.
**Ref:** `documentation/TESTING_PROTOCOL_provenance_skills_20261008.md`;
`provenance_scanner.py`; `test_status_lines.py`; `worksheet_checker.py`;
L-418.

""" % {'n': n, 't': TODAY, 'b': BASE}


def build_ledger(ledger):
    n = max(int(x) for x in re.findall(r'^#### \[L-(\d+)\]', ledger, re.M)) + 1
    ledger = block_edit(ledger, 418, L418_OLD_GAP, L418_RUN % {'n': n},
                        'run and push recorded; Gap: the four tests')
    ledger = touch_meta(ledger, 418)
    a, b = block_span(ledger, 418)
    ledger = ledger[:b] + new_item(n) + ledger[b:]
    print(f"ok  {LEDGER:48s} L-{n}: opened, citation location checks")
    ledger = block_edit(
        ledger, 351,
        "  the project instructions in its context refresh.\n",
        "  the project instructions in its context refresh.\n"
        "  **Counter-case, 2026-10-08 (L-418):** skills installed during the\n"
        "  split session appeared in that same session's mounted skills, new\n"
        "  versions and reference files both. So \"cannot be verified from\n"
        "  inside the session\" is not always true; the next protocol bump\n"
        "  should say it MAY appear, and that a session which sees the new\n"
        "  copy may read it, while the next-session confirmation stays.\n",
        'the protocol: a mid-session install was seen')
    ledger = block_edit(
        ledger, 351,
        "    reference-file conventions; nothing is owed.\n",
        "    reference-file conventions. Owed (found 2026-10-08): who empties\n"
        "    the run-record zone. The skill says both \"no patch edits below\n"
        "    the marker\" and \"once read, the close empties the live zone\".\n",
        'ledger-and-session-records: the run-record zone')
    ledger = touch_meta(ledger, 351)
    ledger = edit(
        ledger, "Review and RICE update Tony 6-21-2026\n",
        "Module updated: October 8, 2026 with Anthropic's Claude Opus 5.5\n"
        "(L-418: the split run and pushed, the installed copies read; L-%d\n"
        "opened, citation location checks; L-351 two owed notes), built on\n"
        "%s.\n"
        "Review and RICE update Tony 6-21-2026\n" % (n, BASE),
        LEDGER, 'header stamp')
    return ledger, n


# ------------------------------------------------------------------
# WHERE WE ARE: by section, nothing below the marker
# ------------------------------------------------------------------

def build_wwa(wwa, n):
    if wwa.count(MARKER) != 1:
        raise Refuse(f"ANCHOR FAIL: {WWA}: the run-record marker was not found once.")
    cut = wwa.index(MARKER)
    top, tail = wwa[:cut], wwa[cut:]
    top = edit(top,
               "Last updated: October 8, 2026, after the provenance split's build.\n"
               "- Written at orrery b0b3df82 and gallery ab66aba7, before your run of\n"
               "  patch_L418_3.\n",
               "Last updated: October 8, 2026, at the provenance split's close.\n"
               "- Written at orrery %s and gallery ab66aba7, before your run of\n"
               "  patch_L418_4.\n" % BASE, WWA, 'header')
    a = top.find("> **Changed since you last read this:**\n")
    b = top.find("> **Do next:**", a)
    if a < 0 or b < 0:
        raise Refuse(f"ANCHOR FAIL: {WWA}: the box's two headings were not found.")
    top = (top[:a] +
           "> **Changed since you last read this:**\n"
           "> - The provenance split ran, all 20 checks pass, and the three\n"
           ">   skills are installed. This session could already see them:\n"
           ">   2.27, 1.0 and 1.18, with their reference files.\n"
           "> - A testing protocol for the new skills is in documentation/.\n"
           ">   Four of its tests need a fresh session.\n"
           "> - Nothing checks where a citation points: not a missing access\n"
           ">   line, not a dead link. L-%d (citation location checks) has the\n"
           ">   measurements and three options.\n"
           ">\n" % n + top[b:])
    print(f"ok  {WWA:48s} box: changed since you last read this")
    top = edit(top,
               "> **Do next:** *the split session (running now) finishes first. Then,\n"
               "> as you confirmed:",
               "> **Do next:** *a fresh session runs the split's four tests\n"
               "> (A3 to A6 in the testing protocol). Then, as you confirmed:",
               WWA, 'box: do next')
    a = top.find("> **Needs you now:**\n")
    b = top.find("\n*Italic* lines are the must-reads.", a)
    if a < 0 or b < 0:
        raise Refuse(f"ANCHOR FAIL: {WWA}: 'Needs you now' was not found.")
    old = top[a:b]
    for done in ("Run patch_L418_3", "Run patch_L412_2_decisions_20261008.py"):
        if done not in old:
            raise Refuse(f"ANCHOR FAIL: {WWA}: 'Needs you now' no longer holds "
                         f"the line for {done}; it was edited since.")
    top = (top[:a] +
           "> **Needs you now:**\n"
           "> - *Run patch_L418_4, then orrery_maintenance_run.py, and push.*\n"
           "> - *Decide L-%d (citation location checks): which of its three\n"
           ">   checks to build. Recommended: the first two together.*\n"
           "> - Optional: delete the two ZIPs in skills/; they go stale.\n" % n
           + top[b:])
    print(f"ok  {WWA:48s} box: needs you now (the three done lines out)")
    top = edit(top,
               "Decisions, one at a time:\n- None waiting. All were ruled on Oct 8.\n",
               "Decisions, one at a time:\n"
               "- L-424 (the checker's one word for two cases): whether the\n"
               "  checker itself prints two different words.\n",
               WWA, 'decisions: L-424')
    top = edit(top,
               "- The provenance split: L-418 (splitting provenance-discipline),\n"
               "  built and waiting on your run; record\n"
               "  `documentation/HANDOFF_L418_split_build_20261008.md`\n",
               "- The provenance split: L-418 (splitting provenance-discipline),\n"
               "  run and pushed; record\n"
               "  `documentation/HANDOFF_L418_split_build_20261008.md`; tests\n"
               "  `documentation/TESTING_PROTOCOL_provenance_skills_20261008.md`\n",
               WWA, 'where the details are: the split')
    return top + tail


# ------------------------------------------------------------------
# THE HANDOFF: an "After the run" section
# ------------------------------------------------------------------

def build_handoff(h, n):
    if DONE_MARK in h:
        raise Refuse(f"ERROR: {HANDOFF} already has the close; this patch has "
                     f"already run.")
    return edit(h, "\nSession record written October 2026 with Anthropic's Claude Opus 5.5.\n",
                """
## After the run, %(t)s -- %(m)s

Pushed at e5cc4bb21cdb69afe1393d394df704700f50f716 at
https://github.com/tonylquintanilla/palomas_orrery.

- Tony's run, from his run record
  (`documentation/WHERE_WE_ARE_10-8-26_1406_run_record.md`): all 13
  files written. The new check failed once, on two untracked
  `SKILL.md.bak` files in the orrery-coding-conventions and
  safe-file-editing folders on his machine. He deleted them, and the
  maintenance run passed 20 of 20, Skill headers 12. Pushed at
  ea2c0e16; skills installed; the Project's instructions replaced;
  pushed at e5cc4bb2.
- After the install, this session's mounted skills read
  provenance-discipline 2.27, provenance-cross-check 1.0 and
  ledger-and-session-records 1.18, with the three reference files.
  Tests A1 and A2 pass. The protocol says a mid-session install cannot
  be seen; this one was. Recorded on L-351.
- Delivered: `documentation/TESTING_PROTOCOL_provenance_skills_20261008.md`.
- Opened: L-%(n)d (citation location checks), Tony to decide which to
  build.
- Two skill ZIPs were committed into skills/ (682c5395). Harmless to the
  check; recommended for deletion, because they go stale.
- Next session: tests A3 to A6. Then L-418 closes.

Tony-actions now: (do) run patch_L418_4, the maintenance run, push;
(decide) L-%(n)d; (decide) L-424; optional (do) delete the two ZIPs.

Session record written October 2026 with Anthropic's Claude Opus 5.5.
""" % {'t': TODAY, 'm': DONE_MARK, 'n': n}, HANDOFF, 'after the run')


def main():
    print(f"patch_L418_4 -- built on orrery {BASE}\n")
    try:
        ledger = read_lf(LEDGER)
        wwa = read_lf(WWA)
        h = read_lf(HANDOFF)
        if DONE_MARK in h:
            raise Refuse("ERROR: this patch has already run. NOTHING was written.")
        ledger, n = build_ledger(ledger)
        wwa = build_wwa(wwa, n)
        h = build_handoff(h, n)
        out = {LEDGER: ledger, WWA: wwa, HANDOFF: h}
        for rel, text in out.items():
            bad = [c for c in text if ord(c) > 127]
            if bad:
                raise Refuse(f"ERROR: {rel} would hold non-ASCII characters.")
    except Refuse as exc:
        print(f"\n{exc}\nNOTHING was written.")
        sys.exit(1)
    for rel, text in out.items():
        with open(ROOT / rel, 'w', encoding='utf-8', newline='') as f:
            f.write(text)
    print("\npatch applied")
    print("\nNEXT:\n  1. Run orrery_maintenance_run.py -- it rebuilds the ledger's index.\n"
          "  2. Move this script into documentation/; commit and push.\n"
          "  3. Start a fresh session for tests A3 to A6 of\n"
          "     documentation/TESTING_PROTOCOL_provenance_skills_20261008.md.")


if __name__ == '__main__':
    main()
