#!/usr/bin/env python3
"""
patch_L422_1_skill_1_17_and_tonys_page_20261007.py -- ORRERY repo. Closes
the Fable 5.1 ledger-sweep session of October 4 to 7, 2026: it writes
Tony's rulings of October 7 into ledger-and-session-records 1.17, records
the bump in the protocol (v3.85), puts Where We Are into the shape Tony
confirmed, and writes the session's handoff.

Built on orrery 8653ef1b593aaf3835ecbcf2186b9e3e28a28089 at
https://github.com/tonylquintanilla/palomas_orrery. The gallery was read
at 4cfeca27 (the swap log, for the page's Signals) and is not changed.
No code changes: records, a skill and a page.

RUN THIS ONE LAST
    Run it AFTER the other five patches of October 7 (patch_L027_2,
    patch_L418_2, patch_L412_1, patch_L001_1, patch_L216_1). It rewrites
    Where We Are whole, this once, because the page's shape changed; if
    patch_L418_2 or patch_L001_1 ran after it, their edits to the page
    would be lost. So it checks that all five have run and refuses,
    naming the one that has not, if any is missing.

HOW TO RUN IT
    Save this file in the ORRERY repo ROOT (next to palomas_orrery.py),
    open it in VS Code and click Run (the command is
    python patch_L422_1_skill_1_17_and_tonys_page_20261007.py). Then
    follow the NEXT steps it prints.

WHAT CHANGES
    skills/ledger-and-session-records/SKILL.md   version 1.17: the
        Where We Are section rewritten (the page's shape, the run-record
        zone, patches edit by section, labels on handles, the check to
        build); the RICE bullet gains the ordered-list rule; Where a File
        Goes gains which repository and "flat"; the v1.14 entry moves to
        SKILL_HISTORIES.md by the three-entry rule.
    documentation/SKILL_HISTORIES.md   the moved v1.14 entry.
    PROJECT_INSTRUCTIONS.md   header stamp v3.85 and the SHA anchor; the
        v3.85 entry; v3.82 moves down. The manifest table is NOT edited
        here: orrery_maintenance_run.py regenerates it (skills_index.py).
    documentation/PROJECT_INSTRUCTIONS_HISTORY.md   the moved v3.82 entry.
    LEDGER_CONSOLIDATED.md   a header stamp; L-422 opened (the bump);
        L-351's ledger-skill line (nothing owed now); L-412 (the rule
        landed); L-396 (the check gains the cap). Matched only at those
        lines (L-419).
    documentation/WHERE_WE_ARE.md   rewritten whole in the new shape. The
        page it replaces is copied, every line, into this session's
        handoff first, so nothing you wrote on it is lost.
    documentation/HANDOFF_L422_fable_sweep_close_20261007.md   new.

TESTED on a copy of 8653ef1b with the five patches applied first: every
edit landed; ledger_index.py --check reported no consistency problems;
skills_index.py --check passed with the manifest reading 1.17; a second
run refused and wrote nothing; and it refused, writing nothing, on a
copy where one of the five had not run.

SUCCESS looks like: one "ok" line per edit, a line saying how many lines
of the old page were carried, then "patch applied".
FAILURE looks like: one ERROR: or ANCHOR FAIL: line, and NOTHING is
written. Undo is Discard Changes in GitHub Desktop.

Written October 7, 2026 with Anthropic's Claude Fable 5.1.
"""

import os

ROOT_MARKERS = ("palomas_orrery.py", "LEDGER_CONSOLIDATED.md")
LEDGER = "LEDGER_CONSOLIDATED.md"
SKILL = "skills/ledger-and-session-records/SKILL.md"
SKILL_HIST = "documentation/SKILL_HISTORIES.md"
PROTO = "PROJECT_INSTRUCTIONS.md"
PROTO_HIST = "documentation/PROJECT_INSTRUCTIONS_HISTORY.md"
WWA = "documentation/WHERE_WE_ARE.md"
HANDOFF = "documentation/HANDOFF_L422_fable_sweep_close_20261007.md"

NEXT = ["1. Move this script into documentation/.",
        "2. Run orrery_maintenance_run.py. Its Skill manifest step rewrites",
        "   the protocol's table to read ledger-and-session-records 1.17;",
        "   its Ledger index step moves L-071 and L-077 to the closed",
        "   section (from the Earth System patch; expected).",
        "3. Commit and push.",
        "4. Reinstall ledger-and-session-records (1.17) from skills/ in",
        "   Settings > Skills, and replace the Project's instructions with",
        "   PROJECT_INSTRUCTIONS.md, now v3.85.",
        "5. Paste today's run record below the marker at the end of Where",
        "   We Are, as you do, and save your timestamped copy."]

# ---------------------------------------------------------------------
# The five patches that must have run first, each known by a line it
# alone writes. The L-418_2 line is the one it REMOVES from the page.
# ---------------------------------------------------------------------
PRIOR = [
    ("patch_L027_2", LEDGER,
     "(L-027: the panels' grey confirmed; L-408 waits for the design talk),",
     True),
    ("patch_L412_1", LEDGER,
     "(L-412: Tony's ruling, an item inside an ordered list needs no RICE",
     True),
    ("patch_L001_1", LEDGER,
     "(L-001: the Earth System track ruled central and behind the website",
     True),
    ("patch_L216_1", LEDGER,
     "(L-216: the daily hand run stands as Tony's practice, pausing OneDrive",
     True),
    ("patch_L418_2", WWA,
     "Last updated: October 6, 2026, end of the Earth website session.",
     False),
]

# ---------------------------------------------------------------------
# SKILL.md
# ---------------------------------------------------------------------
SKILL_VERSION_OLD_START = "Skill version: 1.16 | 2026-10-05"
SKILL_VERSION_OLD_END = "sorted it as method, so the skill answers it now.\n"
SKILL_MOVED_START = "Earlier: 1.14 | Cut from palomas_orrery @ b3cfc780"
SKILL_POINTER = ("Older entries are in documentation/SKILL_HISTORIES.md, moved there\n"
                 "on 2026-10-05 (L-418).\n")

SKILL_VERSION_NEW_HEAD = (
    "Skill version: 1.17 | 2026-10-07, with Anthropic's Claude Fable 5.1, at\n"
    "palomas_orrery @ 8653ef1b. v1.17 (L-422) carries four of Tony's rulings\n"
    "from one session. Under Where We Are -- Tony's page: the page's new\n"
    "shape (each fact once; the box is the page; Settled; Signals), a\n"
    "run-record zone at its end that no patch edits and that the close\n"
    "reads from his timestamped copy, patches editing the page by section,\n"
    "every ledger handle on the page carrying a short label, and the check\n"
    "to build (date, and a cap of 130 lines above the marker). Under Ledger\n"
    "Block Format: an item inside an ordered list needs no RICE score\n"
    "(L-412). Under Where a File Goes: which repository a record goes to,\n"
    "and that documentation/ stays flat.\n"
)
SKILL_POINTER_NEW = ("Older entries are in documentation/SKILL_HISTORIES.md, moved there\n"
                     "on 2026-10-05 (L-418) and 2026-10-07 (L-422).\n")

SKILL_HIST_ANCHOR = ("forest for the trees.\"\n"
                     "\n"
                     "## gallery-cache-builder\n")

WWA_SECTION_START = "### Where We Are -- Tony's page [QUALITY]"
WWA_SECTION_END = "## Ledger Block Format"
WWA_SECTION_NEW = """### Where We Are -- Tony's page [QUALITY]

`documentation/WHERE_WE_ARE.md` is the one document written for Tony
rather than for the work (v1.13, L-396). It is not a rung in the status
ordering and it is not another zoom of the master plan: the ledger still
wins on status and the plan on sequencing. It restates both in plain
words, for a reader who cannot hold the detail. Tony, 2026-09-30: "i
struggle to keep the big picture. it's the old dilemma of loosing the
forest for the trees." The plan's summary and critical path had been
tried for that job and had not really helped, by his account: they are
written for the work, and they move only at design builds.

- ONE file, edited IN PLACE, never versioned. Git holds the history.
  Old changes drop off the page; the ledger and git keep them.
- Updated at the END OF EVERY SESSION that changed the picture, inside
  that session's ledger patch, so it moves in the same transaction and
  costs Tony no extra run. A session with no patch that still changed
  the picture delivers a small one.
- A PATCH EDITS THE PAGE BY SECTION, AT EACH SECTION'S OWN ANCHOR
  (v1.17, L-422), never by rewriting the whole page. Two sessions
  closing the same day then each change their own lines and neither
  loses the other's. The failure this prevents: patch_L418_2, built on
  fbd223ee before the Horizons design session, rewrote the page whole
  and left it saying that design round was still ahead after it had
  happened. A whole-page rewrite is the exception, for a change of the
  page's SHAPE, and it copies every line of the page it replaces into
  the session's handoff first.
- THE RUN-RECORD ZONE (v1.17; Tony, 2026-10-07: "I use the where we are
  to record the run record and rename it with a time stamp."). The
  page ends with the marker line `--- Your run record below this line`,
  and everything under it is Tony's. He pastes the patch output and the
  test checklist there and answers each line in place ("-- yes", "--
  not clear", "-- let's discuss"), then saves the whole page as a
  timestamped copy, `documentation/WHERE_WE_ARE_<m-d-yy>_<hhmm>_run_record.md`,
  flat beside the live page (no subfolder: "I already mix handoffs,
  patches, design documents. Subfolders are more steps and also I scan
  the files to see what the recent changes were."). Three rules
  follow. No patch edits below the marker. The length cap counts only
  the lines above it. And a session's close READS HIS LATEST COPY
  before it writes anything: his verdicts there are the primary record
  of his rulings, so the ledger quotes them from the copy and names the
  copy, instead of re-pasting them into the handoff. His "-- not
  clear" and "-- let's discuss" lines are the open design items in his
  own words and go onto the page's design-talk list verbatim, with the
  date. Once read, the close empties the live zone; the copy is the
  record.
- TONY ANNOTATES THIS PAGE, THE HANDOFFS AND THE LEDGER, and a patch
  never refuses his notes (L-419; Tony, 2026-10-03, and 2026-10-05: "i
  am using our handoffs or the where we are as run records"). So a
  patch checks each of the three only at the lines it edits -- an
  anchor that must match there -- never by a fingerprint of the whole
  file. `documentation/patch_L413_4_session_close_20261005.py` is the
  worked example of carrying his notes; the failure it answers:
  patch_L413_3 fingerprinted the whole page and refused on two "--
  done" marks; Tony, "i though annotations would not be refused."
- A FIXED SHAPE that does not grow (v1.17 shape, L-422; Tony:
  "Confirmed"). EACH FACT APPEARS ONCE. In order: the header (the date,
  and the SHAs it was written at); the READ THIS FIRST box, which IS
  the page -- changed since you last read this, do next, needs you now;
  one line on the marks; THE ROAD, one numbered line per stage, the
  done stages folded into one line, marked [done], [NOW], [next],
  [later] or [goal]; SETTLED, one dated line per standing ruling from
  the last few sessions so a session does not re-raise it, each line
  leaving after a few weeks once it is habit; SIGNALS, three numbers
  READ FROM FILES when the page is written, never typed from memory --
  the last cache build and whether a rename needed a retry (gallery
  `data/cache_swap_log.jsonl`), the Tier-1 count on the files the push
  gate watches (`PROVENANCE_AUDIT.md`; until a tool prints the
  gate-path figure the line says so), and the page's own date against
  the ledger's newest stamp; WAITING ON YOU, split into at the next
  design talk, decisions one at a time, and not urgent in his order --
  the "now" half lives in the box; WHERE THE DETAILS ARE, last and
  short; then the marker and the run-record zone. The sections this
  replaced -- the goal, right now, the next three steps, six lines on
  the marks -- each repeated something the box or the road already
  said. About 110 lines above the marker; the check below holds it.
- ATTENTION MARKS, cleared and reset at every update so that they
  always mean "new since you last read this": **>> UPDATED THIS
  SESSION** beside a changed section's heading; "<< new this session"
  or "<< moved this session" beside a road stage; and *italics* on the
  must-reads -- the one next step, anything that needs Tony now, and
  the [NOW] stage. Tony: "attention is a human limitation."
- PLAIN WORDS IN SHORT BULLETS, one idea per bullet, no paragraphs.
  Tony, 2026-09-30: "the wall of text even a paragraph is an obstacle."
  A LEDGER HANDLE ON THIS PAGE ALWAYS CARRIES A SHORT LABEL IN
  PARENTHESES -- "L-421 (the typed facts)", never a bare L-421 --
  wherever it appears (Tony, 2026-10-07: "all ledger L-xxx items
  should have a brief parenthetical label"). Prefer the plain name in
  the body, and the handle where he will go and look the item up. The
  same holds in handoffs and in chat: a handle is the name of a thing,
  and only one of us can read it (the Register Rule). The Register
  Rule applies in full: this page is in the chat's register, not the
  reference register of this skill.
- At the end of a TURN that changes the picture, Claude's reply closes
  with two or three bullets under "Where this leaves us", in the page's
  own words. The page itself moves at session end.
- THE CHECK, recorded on L-396 and not yet built (v1.17 form): the
  orrery maintenance run fails when the page's "Last updated" date is
  older than the ledger's newest header stamp, OR when more than 130
  lines stand above the run-record marker. It targets the exact
  filename `WHERE_WE_ARE.md`, so a timestamped copy cannot stand in for
  the page; the doc indexer knows a copy by its `_run_record` ending.
  An unchecked store drifts, as the plan's two companions did for a
  month (L-333, L-362). Until the check is built, this rule is the only
  thing keeping the page current and short.

"""

RICE_OLD = ("- RICE: rice:R/I/C/E with / separators (decimals allowed).\n"
            "  Score = R x I x (C/100) / E. Scored items sort to the top of their\n"
            "  section descending; unscored show --.\n")
RICE_NEW = RICE_OLD + (
    "  AN ITEM INSIDE AN ORDERED LIST NEEDS NO RICE SCORE (v1.17; Tony's\n"
    "  ruling of 2026-10-07, L-412). A list such as the Sun's slice (L-412)\n"
    "  or Earth's list (L-413) IS the priority, under the master plan's\n"
    "  sequencing authority (L-221), and a score beside it would only\n"
    "  disagree with it. An item outside any list keeps RICE, and gets a\n"
    "  coarse score when it is next opened rather than at creation. The\n"
    "  index shows -- for the unscored; for list items that is expected.\n")

FILE_GOES_OLD = ("- handoffs, as-builts, manifests, design reviews, spent patch scripts,\n"
                 "  archived protocol copies                      -> documentation/\n"
                 "\n")
FILE_GOES_NEW = FILE_GOES_OLD + (
    "WHICH REPOSITORY, AND NO SUBFOLDERS (v1.17, L-422). Tony's practice,\n"
    "stated 2026-09-22: \"my practice is to put all documentation in the\n"
    "orrery documentation/ folder. i reserve the gallery documentation/\n"
    "folder for the patch files.\" So every RECORD -- a handoff, a\n"
    "manifest, a design note, a session record, a timestamped run-record\n"
    "copy of Where We Are -- goes to the ORRERY's documentation/, whichever\n"
    "repository the work touched; a spent GALLERY patch script goes to the\n"
    "gallery's documentation/. The gallery's documentation/ also holds the\n"
    "tool inputs its maintenance run reads (smoke suites, fixtures,\n"
    "recorded payloads): those are inputs by the test above and stay where\n"
    "the code reads them. And documentation/ stays FLAT. Tony, 2026-10-07,\n"
    "declining a run_records/ folder: \"I already mix handoffs, patches,\n"
    "design documents. Subfolders are more steps and also I scan the files\n"
    "to see what the recent changes were.\" A file's name carries its kind;\n"
    "the folder does not.\n"
    "\n")

# ---------------------------------------------------------------------
# PROJECT_INSTRUCTIONS.md
# ---------------------------------------------------------------------
PROTO_HEAD_OLD = "Tony Quintanilla, PE | Claude | v3.84 | October 6, 2026\n"
PROTO_HEAD_NEW = "Tony Quintanilla, PE | Claude | v3.85 | October 7, 2026\n"
PROTO_CUT_OLD = "Cut from e7073fce at https://github.com/tonylquintanilla/palomas_orrery\n"
PROTO_CUT_NEW = "Cut from 8653ef1b at https://github.com/tonylquintanilla/palomas_orrery\n"
PROTO_V384_START = "v3.84 (October 6, 2026): No rule changed in this document. ONE\n"
PROTO_V382_START = "v3.82 (October 5, 2026): No rule changed in this document. ONE\n"
PROTO_TAIL = "Functional for Claude, readable for human, signal preserved.\n"

PROTO_V385 = """v3.85 (October 7, 2026): No rule changed in this document. ONE
skill bump, one version (L-422): ledger-and-session-records 1.16 ->
1.17. TONY'S PAGE IS EDITED BY SECTION, AND ITS END IS HIS.

WHAT PROMPTED IT. The Fable 5.1 ledger sweep of October 4 to 7 read
Where We Are and found the same facts in four sections, and found that
a closing patch built before a parallel session had rewritten the page
whole and erased that session's lines. Tony then said how he uses the
page: "I use the where we are to record the run record and rename it
with a time stamp." His timestamped copies hold the patch output and
his verdict beside each test line -- the primary record of his rulings.

WHAT CHANGED. ledger-and-session-records, under Where We Are -- Tony's
page: each fact once, the READ THIS FIRST box is the page, Settled and
Signals added; a patch edits the page by section, never whole; the page
ends with a marker, and below it is Tony's run-record zone, which no
patch edits and which the close reads from his latest timestamped copy;
every ledger handle on the page carries a short label ("all ledger
L-xxx items should have a brief parenthetical label"); the check to
build is the date and a cap of 130 lines above the marker. Under Ledger
Block Format: an item inside an ordered list needs no RICE score, his
ruling of the same day (L-412). Under Where a File Goes: records go to
the orrery's documentation/, flat, no subfolders ("Subfolders are more
steps and also I scan the files to see what the recent changes were").
The skill's v1.14 entry moved to documentation/SKILL_HISTORIES.md, by
the three-entry rule. Where We Are itself was rewritten in the new
shape, this once, the page it replaced copied into the handoff.

THE OBLIGATION TRAVELS. A reinstall during a session is not visible to
that session. The next session confirms its loaded copy reads
ledger-and-session-records 1.17 before any ledger, handoff or
session-record work.

The header stamp and the SHA anchor move with this entry.

Version history: v3.82 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

"""

PROTO_HIST_ANCHOR = ("(Moved down from the resident protocol on 2026-10-06 when\n"
                     "v3.84 made a fourth entry.)\n"
                     "\n"
                     "================================================================\n"
                     "PART 2 -- LESSONS REMOVED FROM THE PROTOCOL AT v3.37\n")
PROTO_HIST_MOVED_NOTE = ("(Moved down from the resident protocol on 2026-10-07 when\n"
                         "v3.85 made a fourth entry.)\n"
                         "\n")

# ---------------------------------------------------------------------
# LEDGER_CONSOLIDATED.md
# ---------------------------------------------------------------------
LEDGER_EDITS = [
    ("header stamp",
     "Review and RICE update Tony 6-21-2026\n",
     "Module updated: October 7, 2026 with Anthropic's Claude Fable 5.1\n"
     "(L-422 opened: ledger-and-session-records 1.17, protocol v3.85; Where\n"
     "We Are in the shape Tony confirmed, with his run-record zone; L-412's\n"
     "rule landed; L-396's check gains the cap), built on 8653ef1b, after\n"
     "the day's five patches.\n"
     "Review and RICE update Tony 6-21-2026\n"),
    ("L-422 opened",
     "#### [L-421] Facts typed in the Earth and Sun rooms' code, not served with their sources (gallery, words)\n",
     "#### [L-422] ledger-and-session-records 1.17: Tony's page by section, the run-record zone, labels on handles, RICE for lists, where a record goes (skills, documentation)\n"
     "<!-- L:422 status:OPEN upd:2026-10-07 section:A flag: rice: -->\n"
     "- **Built 2026-10-07** (Fable 5.1 ledger-sweep session) by\n"
     "  `documentation/patch_L422_1_skill_1_17_and_tonys_page_20261007.py`,\n"
     "  from four of Tony's rulings that day, each method and so a skill rule\n"
     "  (Method Belongs to the Skill):\n"
     "  - **The page's shape.** Tony: \"Confirmed.\" Each fact once; the READ\n"
     "    THIS FIRST box is the page; the done road stages fold into one\n"
     "    line; SETTLED and SIGNALS added; the goal, right now, the next\n"
     "    three steps and the marks legend cut as repeats. The mock he read\n"
     "    became the page, written whole this once because the shape\n"
     "    changed; from here a patch edits the page by section.\n"
     "  - **The run-record zone.** Tony: \"I use the where we are to record\n"
     "    the run record and rename it with a time stamp.\" The page ends\n"
     "    with a marker; below it is his; no patch edits it; the cap\n"
     "    excludes it; the close reads his latest timestamped copy and names\n"
     "    it. No subfolder for the copies: \"I already mix handoffs,\n"
     "    patches, design documents. Subfolders are more steps and also I\n"
     "    scan the files to see what the recent changes were.\"\n"
     "  - **Labels on handles.** Tony: \"all ledger L-xxx items should have\n"
     "    a brief parenthetical label.\" On the page, in handoffs, in chat.\n"
     "  - **RICE for list items** (L-412, ruled 2026-10-07): no score inside\n"
     "    an ordered list; carried on L-351 for a day, now landed.\n"
     "  - **Where a record goes** (Tony, 2026-09-22, carried on L-351 since):\n"
     "    the orrery's documentation/ for all documentation, the gallery's\n"
     "    for its patch files and the tool inputs its run reads; flat.\n"
     "- **In the same commit:** protocol v3.85 (the entry; v3.82 moved to\n"
     "  PROJECT_INSTRUCTIONS_HISTORY.md); the skill's v1.14 entry moved to\n"
     "  SKILL_HISTORIES.md by the three-entry rule (L-418);\n"
     "  documentation/WHERE_WE_ARE.md in the new shape, the page it replaced\n"
     "  copied into this session's handoff; the handoff itself.\n"
     "- **This bump takes 1.17.** L-418's split build, which expected to cut\n"
     "  the ledger skill at 1.17, cuts it at 1.18. L-412 and L-351 say so.\n"
     "- **The obligation travels.** This session's installed copy was bound\n"
     "  at 1.14 when the conversation began (before the 1.16 push), and it\n"
     "  read 1.16 from the repo at HEAD. The next session confirms its\n"
     "  loaded copy reads 1.17 before any ledger, handoff or session-record\n"
     "  work.\n"
     "- **Tony-action (do):** reinstall ledger-and-session-records (1.17)\n"
     "  from skills/ in Settings > Skills; replace the Project's instructions\n"
     "  with PROJECT_INSTRUCTIONS.md, now v3.85.\n"
     "**Gap:** the loaded-copy confirmation above; then CLOSE. The check\n"
     "(date and cap) is L-396's to build, not this item's.\n"
     "**Ref:** `skills/ledger-and-session-records/SKILL.md`;\n"
     "`documentation/WHERE_WE_ARE.md`;\n"
     "`documentation/HANDOFF_L422_fable_sweep_close_20261007.md`;\n"
     "`documentation/LEDGER_SWEEP_review_20261007.md`; L-396, L-412, L-351,\n"
     "L-418, L-419.\n"
     "\n"
     "#### [L-421] Facts typed in the Earth and Sun rooms' code, not served with their sources (gallery, words)\n"),
    ("L-351 ledger skill line",
     "  - ledger-and-session-records, at 1.17 (L-418's build): an item\n"
     "    inside an ordered list needs no RICE score, the list's order being\n"
     "    its priority under the plan's sequencing authority; items outside\n"
     "    a list keep RICE (Tony, 2026-10-07, L-412). And Tony's\n"
     "    documentation-folder practice (above). The by-the-lines check of\n"
     "    Tony-annotated files landed at 1.16 on 2026-10-05 (L-419) and is\n"
     "    struck here.\n",
     "  - ledger-and-session-records: nothing owed. The RICE rule for list\n"
     "    items (L-412) and Tony's documentation-folder practice (above)\n"
     "    landed at 1.17 on 2026-10-07 (L-422), with the Where We Are rules\n"
     "    of that day. L-418's split cuts this skill at 1.18.\n"),
    ("L-412 rule landed",
     "  carried on L-351 until then. Question (b), the proposed scores, is\n"
     "  still open.\n"
     "**Gap:** after L-413, work down the list from item 3.\n",
     "  carried on L-351 until then. Question (b), the proposed scores, is\n"
     "  still open.\n"
     "- **2026-10-07, later the same day:** the rule landed in\n"
     "  ledger-and-session-records 1.17 (L-422), not at L-418's build.\n"
     "  Question (b) is still open.\n"
     "**Gap:** after L-413, work down the list from item 3.\n"),
    ("L-396 date",
     "<!-- L:396 status:OPEN upd:2026-10-04 section:A flag: rice: -->\n",
     "<!-- L:396 status:OPEN upd:2026-10-07 section:A flag: rice: -->\n"),
    ("L-396 the check gains the cap",
     "**Gap:** the check above, or a ruling that the skill rule is enough.\n",
     "- **2026-10-07 (Fable 5.1 sweep): the page's shape changed, and the\n"
     "  check gains a second half.** Tony confirmed the redesign -- each\n"
     "  fact once, Settled, Signals, and a run-record zone at the end that\n"
     "  is his, which he saves as a timestamped copy. ledger-and-session-\n"
     "  records 1.17 writes it down (L-422). The check to build: the page's\n"
     "  date older than the ledger's newest stamp, OR more than 130 lines\n"
     "  above the run-record marker; it targets WHERE_WE_ARE.md by exact\n"
     "  name, never the timestamped copies. The doc indexer should know a\n"
     "  copy by its `_run_record` ending instead of listing it as the page.\n"
     "**Gap:** build the check (date and cap), or rule that the skill rule\n"
     "is enough. L-422 holds the shape; this item holds the check.\n"),
]

# ---------------------------------------------------------------------
# documentation/WHERE_WE_ARE.md -- the new page
# ---------------------------------------------------------------------
WWA_NEW = """<!-- Doc-Kind: hand | Where the project is and where it is going, in plain words. One file, edited by section; Tony's run record sits below the marker at the end and no patch edits it. -->
# Where We Are

Last updated: October 7, 2026, end of the Fable ledger sweep.
- Written at orrery 8653ef1b and gallery 4cfeca27, after the day's five
  patches and before your run of this closing one.

> **READ THIS FIRST**
>
> **Changed since you last read this:**
> - This page has a new shape, the one you confirmed: each fact once,
>   this box is the page, and the end of the page is yours. Paste your
>   run record below the marker at the bottom, as you do.
> - The Horizons check is designed, in one session with its own file.
>   What it checks, what counts as agreement, where it runs: settled.
>   The build is next.
> - The Earth System work is ordered: central, but behind the orrery
>   website; the gallery cards stand in meanwhile. The 2026 heat-dome
>   items close, because the event is over.
> - The daily hand run stands: four checks, first thing, no automating
>   for now. Daily Run pauses OneDrive for 24 hours, not 2.
> - The swap log proves the retry fix: two of your hand builds needed a
>   second attempt and both succeeded. "Took 2 attempts" is normal.
> - Items inside an ordered list need no RICE score; the rest keep it.
>   That rule, and this page's rules, are in the ledger skill, now 1.17.
>
> **Do next:** *the typed facts, in a fresh session, from the plan.*
>
> **Needs you now:**
> - *Run orrery_maintenance_run.py and push. Reinstall the ledger skill
>   (1.17) and replace the Project's instructions with v3.85.*

*Italic* lines are the must-reads. Marks reset at every update.

## The road  **>> UPDATED THIS SESSION**

  1-4. [done]  The Sun, Earth and Solar System rooms are live; the orrery
               feeds the website and nothing is typed twice.
  5.   [NOW]   *Earth's old items are finished, in your order.* The
               website patch is live; the typed facts are the last part.
  6.   [next]  The 17 facts typed in the Earth and Sun rooms' code move
               into the served data, with their sources.
  7.   [next]  The Sun's numbers get the checking Earth's got.
  8.   [next]  The served objects are checked against JPL Horizons.
               Designed; build next. << moved this session
  9.   [next]  The website's checks get a short list of their own.
 10.   [next]  A bare interactive.html link opens the Solar System room;
               the Explorer gets its own address.
 11.   [later] The rest of the orrery's objects come to the website.
 12.   [later] Encounters: comets and spacecraft at the dates that matter.
 13.   [later] The planets get their details, Jupiter and Saturn first.
 14.   [later] The Earth System layers; the gallery's cards meanwhile.
 15.   [goal]  The website does what the desktop orrery does, with a date
               to choose, within the range the data covers.

## Settled  **>> UPDATED THIS SESSION**

Standing rulings. A line leaves after a few weeks, once it is habit.
- The daily hand run stays a hand run. (Oct 7)
- OneDrive: pause 24 hours before a build; the retry absorbs the lock
  either way. Empty "solar-system (N)" folders are harmless; delete by
  hand. (Oct 7)
- Items in an ordered list carry no RICE score. (Oct 7)
- Every ledger handle on this page carries a short label. (Oct 7)
- Code types only words about our picture; facts are served. (Oct 6)

## Signals  **>> UPDATED THIS SESSION**

Read from files when this page was written, not typed from memory.
- Last cache build: 20261007T143110Z, ok, one attempt. Last retry: the
  Oct 6 18:20 hand build, two attempts, ok.
- Tier-1 findings, whole tree: 296, unchanged since Oct 6. No tool yet
  prints the number on the gate path alone; that is owed on the
  provenance-discipline bump.
- This page's date and the ledger's newest stamp: both Oct 7. Agree.

## Waiting on you  **>> UPDATED THIS SESSION**

At the next design talk:
- The fuzzy outer corona, with the dust cloud; the exosphere the same way.
- Moving the highlighted row to the top of the list.
- GO's arrow, only if the text box stays centred.
- Earth's design talks, the belts' shape first.

Decisions, one at a time:
- Whether L-216 (the swap retry) closes. Recommended: yes.
- The handful of RICE scores the sweep proposes.
- Whether the gallery-checks list becomes a ledger item before building.
- L-027 (the panel colour) closes once its confirming patch has run.

Not urgent, in your order:
1. Whether the editor also edits the Solar System room's rows.
2. Choosing a date, and animation.
3. The scattered disk, with the Kuiper belt. Not the fuzzy-boundary idea.

## Where the details are  **>> UPDATED THIS SESSION**

- Every item: `LEDGER_CONSOLIDATED.md`. This session: L-422 (the ledger
  skill at 1.17 and this page), L-001 (the Earth System track), L-071
  and L-077 (the 2026 heat domes, closed), L-216 (the swap retry and
  the hand run), L-412 (the RICE ruling), L-395 (the Horizons check,
  designed). Open for build: L-421 (the typed facts), L-418 (splitting
  provenance-discipline).
- This session's record:
  `documentation/HANDOFF_L422_fable_sweep_close_20261007.md`
- The sweep's report: `documentation/LEDGER_SWEEP_review_20261007.md`
- The typed facts plan: `documentation/MANIFEST_L421_typed_facts_20261006.md`
- The Horizons check design:
  `documentation/DESIGN_L395_horizons_check_20261007.md`
- The reasoning behind the order:
  `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md`

--- Your run record below this line. No patch edits it; the length cap
--- stops here; the close reads your timestamped copy and clears this.

**Tony**: Run record:
"""

# ---------------------------------------------------------------------
# The handoff
# ---------------------------------------------------------------------
HANDOFF_TEXT = """<!-- Doc-Kind: hand | Session record: the Fable 5.1 ledger sweep of October 4 to 7, 2026 -- the sweep's two reports, Tony's five rulings and their patches, the swap-log evidence, Where We Are redesigned, ledger-and-session-records 1.17, protocol v3.85. -->
# Handoff: the Fable ledger sweep, October 4 to 7, 2026

Built on orrery 8653ef1b593aaf3835ecbcf2186b9e3e28a28089 at
https://github.com/tonylquintanilla/palomas_orrery; the gallery read at
4cfeca27 at https://github.com/tonylquintanilla/tonyquintanilla.github.io
and not changed. Orrery pushed at: Tony's run record carries it. This
record is carried by `patch_L422_1_skill_1_17_and_tonys_page_20261007.py`.
Type: DOCUMENTATION (one skill version, one protocol entry, one page;
no code). Written October 7, 2026, with Anthropic's Claude Fable 5.1.

## What this session was

A review session beside the Opus sessions working Earth's list. Tony
asked for a sweep of LEDGER_CONSOLIDATED.md (closes, RICE, grouping,
errors) on October 4, an update of it on October 7, and then ruled on
five of the things it raised. The session wrote no code.

## Opening checks [verified @ orrery 8653ef1b]

- The installed copies of ledger-and-session-records (1.14) and
  safe-file-editing (1.11) in this conversation were bound before the
  pushes that took them to 1.16 and 1.13; the session read both skills
  from the repo at HEAD and said so. The October 6 and 7 sessions had
  already verified the account installs current, so no action fell to
  Tony from the mismatch.
- The ledger indexer's --check was clean at both anchors (cbde99dc on
  October 4; 8653ef1b on October 7).

## Done, verified

- `documentation/LEDGER_SWEEP_review_20261004.md` (in the repo; cited
  by L-413) and `documentation/LEDGER_SWEEP_review_20261007.md`: the
  sweep and its update. Nearly every proposal of the first landed by
  the second (17 closes, L-413 and L-421 opened, the header stamps,
  L-351 made the one place for what skills are owed). One correction
  in the second: it first said L-351 had not been made that place; it
  had, on October 4.
- The swap log read at gallery 4cfeca27: 29 lines, all ok; runs
  20261004T205153Z and 20261006T182032Z show staging_to_live taking two
  attempts, both Tony's hand builds with OneDrive paused. The L-216
  retry is PROVEN; the lock recurs even when paused; the retry absorbs
  it. The empty "solar-system (N)" folders are not a retry remnant.
- Tony's rulings of October 7, each in its own records-only patch,
  tested on copies of 8653ef1b alone and in both orders with the two
  Opus patches of the day:
  - `patch_L412_1_rice_ruling_20261007.py`: an item inside an ordered
    list needs no RICE score; items outside keep it (L-412 (a)).
  - `patch_L001_1_earth_system_track_20261007.py`: the Earth System
    track is central and behind the website build, the gallery's cards
    serving meanwhile; L-071 and L-077 (the 2026 heat domes) close,
    "the event is over"; the road gains stage 14.
  - `patch_L216_1_hand_run_stands_20261007.py`: the daily hand run with
    its four checks stands; Daily Run pauses OneDrive 24 hours; no
    schedule or move off OneDrive to be proposed again.
- This closing patch: ledger-and-session-records 1.17 (the Where We Are
  rules, RICE for lists, which repository a record goes to, flat);
  protocol v3.85; Where We Are in the new shape; L-422 opened.

## Tony's words that became rules (L-422)

- "I use the where we are to record the run record and rename it with
  a time stamp." -> the run-record zone, and the close reads his copy.
- "Confirmed, but no subfolder. I already mix handoffs, patches, design
  documents. Subfolders are more steps and also I scan the files to see
  what the recent changes were." -> documentation/ stays flat.
- "all ledger L-xxx items should have a brief parenthetical label."
- "Why don't you update the skill and add your own Where We Are
  updating with this Fable session." -> this patch, not the Horizons
  session's.

## Discrepancies surfaced, not resolved here

- `daily_run.py` (gallery) still says the OneDrive pause lasts 2 hours
  (lines 155 and 166); Tony pauses 24. One-line fix, owed on L-216.
- "Conflict copies" wording stands in four places (gallery .gitignore,
  check_cache_siblings.py, the orrery dashboard,
  L342_install_test_run_sequence.md) after the cause was ruled out.
- The scanner prints a whole-tree Tier-1 count (296) and no gate-path
  figure; the page's Signals say so. Owed on the provenance-discipline
  bump (L-414, L-351).
- patch_L418_2 was built on fbd223ee, before the Horizons design
  session, and rewrote the page whole; this patch's page takes the
  design round as done. The pattern is the founding case of the
  edit-by-section rule.

## Open decisions for Tony (rollup)

- **(decide)** Whether L-216 (the swap retry) closes. Recommended yes:
  the retry is proven and the hand run is ruled.
- **(decide)** L-412 question (b): the handful of RICE scores the sweep
  proposes (L-131 and L-128 at 3/3/70/2; L-228, L-241, L-292 confirmed;
  L-252 re-scored).
- **(decide)** Whether the gallery-checks list (L-235, L-237, L-262,
  L-367, L-378, L-357, L-379, L-360, L-380, L-388) becomes one ledger
  item before it is built. Road stage 9 has no handle today.
- **(decide)** L-027 (the panel colour) closes once patch_L027_2 has
  run; its last gap was discharged by the October 6 skills sweep.
- **(do)** Reinstall ledger-and-session-records (1.17); replace the
  Project's instructions with PROJECT_INSTRUCTIONS.md v3.85.
- **(do)** Move the day's six patch scripts into documentation/.

## The obligation that travels

The next session confirms its loaded copy of ledger-and-session-records
reads 1.17 before any ledger, handoff or session-record work. A
reinstall during a session is not visible to that session.

## Next-session scoping

In the order the sweep's report gives: (1) the typed facts (L-421)
in a fresh session from `MANIFEST_L421_typed_facts_20261006.md`; it
also confirms interactive-exhibit 1.12 and carries the `_declared`
"1.1 times" fix in the gallery's objects_config; (2) the
provenance-discipline bump carrying L-414 and L-351; (3) the Sun's
list from item 3 (L-385, L-228, L-411); (4) the Horizons check build
(L-395) from `DESIGN_L395_horizons_check_20261007.md`; (5) the
gallery-checks list as a ledger item, then its build.

## The page this patch replaced

Every line of `documentation/WHERE_WE_ARE.md` as it stood when this
patch ran, after the day's five patches and with any note Tony had
written on it. Kept here because the rewrite was whole (a change of
shape); from now on patches edit the page by section.

{OLD_PAGE}
"""


def read_lf(path):
    with open(path, "rb") as handle:
        raw = handle.read()
    return raw.decode("utf-8").replace("\r\n", "\n"), b"\r\n" in raw


def need(text, old, label, path, want=1):
    found = text.count(old)
    if found != want:
        raise SystemExit("ANCHOR FAIL (%s): expected %d match(es) in %s, "
                         "found %d. Has this patch already run? NOTHING "
                         "was written." % (label, want, path, found))


def ascii_guard(before_text, after_text, path):
    before = sum(1 for ch in before_text if ord(ch) > 127)
    after = sum(1 for ch in after_text if ord(ch) > 127)
    if after > before:
        raise SystemExit("ERROR: %s would hold new non-ASCII text. NOTHING "
                         "was written." % path)


def main():
    if os.path.basename(os.getcwd()) == "documentation":
        raise SystemExit("ERROR: run this from the repo ROOT, not from "
                         "documentation/. NOTHING was written.")
    for marker in ROOT_MARKERS:
        if not os.path.isfile(marker):
            raise SystemExit("ERROR: %s is not here, so this is not the "
                             "orrery root. NOTHING was written." % marker)
    for path in (LEDGER, SKILL, SKILL_HIST, PROTO, PROTO_HIST, WWA):
        if not os.path.isfile(path):
            raise SystemExit("ERROR: %s is not here. NOTHING was written."
                             % path)
    if os.path.exists(HANDOFF):
        raise SystemExit("ERROR: %s already exists. If this patch already "
                         "ran, it has nothing left to do. NOTHING was "
                         "written." % HANDOFF)

    # The five patches of the day must have run first.
    for name, path, line, must_be_present in PRIOR:
        text, _ = read_lf(path)
        present = line in text
        if present != must_be_present:
            raise SystemExit("ERROR: %s has not run yet (its mark on %s is "
                             "%s). Run it first; this patch rewrites Where "
                             "We Are whole and goes LAST. NOTHING was "
                             "written." % (name, path,
                                           "missing" if must_be_present
                                           else "still there"))

    writes = []

    # ---- SKILL.md
    skill, skill_crlf = read_lf(SKILL)
    orig_skill = skill
    need(skill, SKILL_VERSION_OLD_START, "skill version head", SKILL)
    need(skill, SKILL_VERSION_OLD_END, "skill version tail", SKILL)
    need(skill, SKILL_MOVED_START, "skill v1.14 entry", SKILL)
    need(skill, SKILL_POINTER, "skill history pointer", SKILL)
    a = skill.index(SKILL_VERSION_OLD_START)
    c = skill.index(SKILL_MOVED_START)
    b = skill.index(SKILL_VERSION_OLD_END) + len(SKILL_VERSION_OLD_END)
    if not (a < c < b):
        raise SystemExit("ERROR: the skill's version block is not in the "
                         "order this patch expects. NOTHING was written.")
    kept = skill[a:c].replace("Skill version: 1.16 |", "Earlier: 1.16 |", 1)
    moved = skill[c:b].replace(SKILL_POINTER, "", 1)
    new_block = SKILL_VERSION_NEW_HEAD + kept + SKILL_POINTER_NEW
    skill = skill[:a] + new_block + skill[b:]
    need(skill, WWA_SECTION_START, "skill Where We Are heading", SKILL)
    need(skill, WWA_SECTION_END, "skill Ledger Block Format heading", SKILL)
    w0 = skill.index(WWA_SECTION_START)
    w1 = skill.index(WWA_SECTION_END)
    if not w0 < w1:
        raise SystemExit("ERROR: the skill's sections are not in the order "
                         "this patch expects. NOTHING was written.")
    skill = skill[:w0] + WWA_SECTION_NEW + skill[w1:]
    need(skill, RICE_OLD, "skill RICE bullet", SKILL)
    skill = skill.replace(RICE_OLD, RICE_NEW, 1)
    need(skill, FILE_GOES_OLD, "skill Where a File Goes list", SKILL)
    skill = skill.replace(FILE_GOES_OLD, FILE_GOES_NEW, 1)
    ascii_guard(orig_skill, skill, SKILL)
    writes.append((SKILL, skill, ["version 1.17", "Where We Are section",
                                  "RICE bullet", "Where a File Goes"],
                   skill_crlf))

    # ---- SKILL_HISTORIES.md
    hist, hist_crlf = read_lf(SKILL_HIST)
    need(hist, SKILL_HIST_ANCHOR, "skill histories anchor", SKILL_HIST)
    moved_entry = (
        "forest for the trees.\"\n"
        "\n"
        "The skill's v1.14 entry, moved here word for word on 2026-10-07 when\n"
        "v1.17 made a fourth entry (L-422):\n"
        + moved +
        "\n"
        "## gallery-cache-builder\n")
    hist2 = hist.replace(SKILL_HIST_ANCHOR, moved_entry, 1)
    ascii_guard(hist, hist2, SKILL_HIST)
    writes.append((SKILL_HIST, hist2, ["v1.14 entry moved in"], hist_crlf))

    # ---- PROJECT_INSTRUCTIONS.md
    proto, proto_crlf = read_lf(PROTO)
    orig_proto = proto
    for label, old in (("protocol header", PROTO_HEAD_OLD),
                       ("protocol anchor", PROTO_CUT_OLD),
                       ("protocol v3.84 entry", PROTO_V384_START),
                       ("protocol v3.82 entry", PROTO_V382_START),
                       ("protocol tail", PROTO_TAIL)):
        need(proto, old, label, PROTO)
    s82 = proto.index(PROTO_V382_START)
    e82 = proto.index(PROTO_TAIL)
    if not s82 < e82:
        raise SystemExit("ERROR: the protocol's version history is not in "
                         "the order this patch expects. NOTHING was written.")
    v382 = proto[s82:e82]
    proto = proto[:s82] + proto[e82:]
    proto = proto.replace(PROTO_HEAD_OLD, PROTO_HEAD_NEW, 1)
    proto = proto.replace(PROTO_CUT_OLD, PROTO_CUT_NEW, 1)
    proto = proto.replace(PROTO_V384_START, PROTO_V385 + PROTO_V384_START, 1)
    ascii_guard(orig_proto, proto, PROTO)
    writes.append((PROTO, proto, ["header v3.85 and anchor",
                                  "v3.85 entry", "v3.82 moved down"],
                   proto_crlf))

    # ---- PROJECT_INSTRUCTIONS_HISTORY.md
    phist, phist_crlf = read_lf(PROTO_HIST)
    need(phist, PROTO_HIST_ANCHOR, "protocol history anchor", PROTO_HIST)
    insert = (PROTO_HIST_ANCHOR[:PROTO_HIST_ANCHOR.index("=====")]
              + v382.rstrip("\n") + "\n\n" + PROTO_HIST_MOVED_NOTE
              + PROTO_HIST_ANCHOR[PROTO_HIST_ANCHOR.index("====="):])
    phist2 = phist.replace(PROTO_HIST_ANCHOR, insert, 1)
    ascii_guard(phist, phist2, PROTO_HIST)
    writes.append((PROTO_HIST, phist2, ["v3.82 entry moved in"], phist_crlf))

    # ---- LEDGER_CONSOLIDATED.md
    ledger, ledger_crlf = read_lf(LEDGER)
    orig_ledger = ledger
    done = []
    for label, old, new in LEDGER_EDITS:
        need(ledger, old, label, LEDGER)
        ledger = ledger.replace(old, new, 1)
        done.append(label)
    ascii_guard(orig_ledger, ledger, LEDGER)
    writes.append((LEDGER, ledger, done, ledger_crlf))

    # ---- WHERE_WE_ARE.md and the handoff
    page, page_crlf = read_lf(WWA)
    if "# Where We Are" not in page:
        raise SystemExit("ERROR: %s does not read as Where We Are. NOTHING "
                         "was written." % WWA)
    if "--- Your run record below this line" in page:
        raise SystemExit("ERROR: %s already has the run-record marker, so "
                         "this patch has already run. NOTHING was written."
                         % WWA)
    old_lines = page.rstrip("\n").split("\n")
    carried = "\n".join("    " + line for line in old_lines)
    handoff = HANDOFF_TEXT.replace("{OLD_PAGE}", carried)
    ascii_guard(page, WWA_NEW, WWA)
    ascii_guard(page, handoff, HANDOFF)
    writes.append((WWA, WWA_NEW, ["rewritten whole in the new shape"],
                   page_crlf))
    writes.append((HANDOFF, handoff, ["created"], False))

    for path, text, labels, was_crlf in writes:
        with open(path, "wb") as handle:
            handle.write(text.encode("utf-8"))
        for label in labels:
            print("ok  %-52s %s" % (path, label))
        if was_crlf:
            print("note: %s was CRLF in the working copy; written LF" % path)
    print("")
    print("carried %d line(s) of the old Where We Are into the handoff"
          % len(old_lines))
    print("")
    print("patch applied")
    print("")
    print("NEXT:")
    for line in NEXT:
        print("  " + line)


if __name__ == "__main__":
    main()
