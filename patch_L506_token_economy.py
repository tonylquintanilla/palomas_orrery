"""patch_L506_token_economy.py -- Token Economy becomes a rule of the protocol (v3.121).

Paloma's Orrery, orrery repository (palomas_orrery). L-506, opened here.

WHAT IT DOES, in one commit's worth of edits:
  - PROJECT_INSTRUCTIONS.md: header to v3.121 / November 2, 2026, anchor to
    fd3551cc; a new section, Token Economy [QUALITY], in Part 2 after Method
    Belongs to the Skill; two rows in the Anti-Patterns table; the v3.121
    version-history entry; the v3.118 entry moved out (the three-entry rule).
  - documentation/PROJECT_INSTRUCTIONS_HISTORY.md: the v3.118 entry appended
    to PART 1, word for word, with its moved-down note.
  - documentation/project_instructions_v3_121.md: the versioned copy, written
    new, byte-identical to the live protocol after the edits.
  - CLAUDE.md (the Code door): a skill is read in full when its rules govern
    the work and in parts otherwise; the report ends with the token count.
  - LEDGER_CONSOLIDATED.md: L-506 opened at the top of section A.
  - documentation/WHERE_WE_ARE.md: one Settled line and one box line; the cap
    of 130 lines above the marker is checked by this script.

Tony's ruling of 2026-11-02, 09:24 and 09:29 Chicago, in the coordinating
session: "I would like to make part of our protocol token economy", and, on
the measured half (a token count in every Code report and run record), "yes".

HOW TO RUN. Save this file in the ROOT of the orrery folder,
  C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\
open it in VS Code and click Run (or: python patch_L506_token_economy.py from
that folder). It refuses, writing nothing, if any file is not the version it
was built against (orrery fd3551cc, plus the Where We Are placed by the
coordinating session this morning) or if run from another folder. Undo is
Discard Changes in GitHub Desktop.

AFTER IT RUNS: the numbered steps it prints (ledger_index.py, then commit
and push, then the paste into the Project's instructions).

Built 2026-11-02 against orrery fd3551cc with Anthropic's Claude Fable 5.1.
"""
import hashlib
import os
import sys

if not (os.path.isfile("PROJECT_INSTRUCTIONS.md") and os.path.isfile("CLAUDE.md")
        and os.path.isdir("documentation") and os.path.isdir("skills")):
    print("ERROR: run this from the orrery folder's root (PROJECT_INSTRUCTIONS.md, CLAUDE.md, documentation\\ and skills\\ beside it); you are in " + os.getcwd())
    print("NOTHING was written.")
    sys.exit(1)

PROTO = "PROJECT_INSTRUCTIONS.md"
HIST = os.path.join("documentation", "PROJECT_INSTRUCTIONS_HISTORY.md")
COPY = os.path.join("documentation", "project_instructions_v3_121.md")
DOOR = "CLAUDE.md"
LEDGER = "LEDGER_CONSOLIDATED.md"
WWA = os.path.join("documentation", "WHERE_WE_ARE.md")

GUARDS = {
    PROTO: "e72cae906bc2d4de2cb9e197aca74d79",
    HIST: "821f61aa3509d834f28e9ce0e94bd569",
    DOOR: "53d844941eb081282a8da0ab756bc205",
    LEDGER: "d2d126459375918b055ff63bc69053d6",   # outside the INDEX zone
    WWA: "8fc8e810c0f26aa905c90d8dd5a6b3ee",
}


def fail(msg):
    print("ERROR: " + msg)
    print("NOTHING was written. Undo, if ever needed, is Discard Changes in GitHub Desktop.")
    sys.exit(1)


def load(path):
    raw = open(path, "rb").read()
    was_crlf = b"\r\n" in raw
    lf = raw.replace(b"\r\n", b"\n")
    body = lf
    if path == LEDGER:
        a = lf.index(b"<!-- INDEX:START")
        e = lf.index(b"<!-- INDEX:END -->") + len(b"<!-- INDEX:END -->")
        body = lf[:a] + lf[e:]
    got = hashlib.md5(body).hexdigest()
    if got != GUARDS[path]:
        fail(path + " is not the file this patch was built against: md5 " + got + ", expected " + GUARDS[path] +
             ". Pull origin first if GitHub Desktop shows a number. For WHERE_WE_ARE.md the expected copy is the one the "
             "coordinating session placed on Nov 2 at 09:15 (7,100 bytes).")
    return lf, was_crlf


def apply(text, edits, path):
    for i, (old, new) in enumerate(edits, 1):
        n = text.count(old)
        if n != 1:
            fail("ANCHOR FAIL in %s, edit %d: expected 1 match, found %d: %r" % (path, i, n, old[:70]))
        if any(b > 127 for b in new):
            fail("the patch's own inserted text is not ASCII (%s, edit %d)" % (path, i))
        text = text.replace(old, new)
    return text


if os.path.exists(COPY):
    fail(COPY + " already exists. It is written by this patch; if it is a copy saved from elsewhere, delete it and run again.")

files = {p: load(p) for p in GUARDS}

# ---------------------------------------------------------------------------
# PROJECT_INSTRUCTIONS.md
# ---------------------------------------------------------------------------
proto = files[PROTO][0]

# The v3.118 entry leaves the resident protocol, word for word.
start = proto.index(b"v3.118 (October 29, 2026): No rule changed in this document. FOUR")
end = proto.index(b"Functional for Claude, readable for human, signal preserved.")
v118 = proto[start:end]
if v118.count(b"\nv3.") != 0:
    fail("the v3.118 block does not end where expected")
proto = proto[:start] + proto[end:]

TOKEN_ECONOMY = b"""Token Economy [QUALITY]
Companion to Method Belongs to the Skill, one axis over: that rule
governs who decides; this one governs what the work may cost. Tokens
are not free, and the price charged does not carry their outside
costs: the emissions behind the electricity and the chips, the water,
the grid capacity built for the load, and the demand the habit
creates. "Data preservation is climate action" does not stop at the
data. (Tony, November 2, 2026: "I am becoming very concerned about the
environmental cost of token generation ... I would like to make part
of our protocol token economy.")

The rule is one sentence: SPEND TOKENS WHERE THEY BUY VERIFICATION OR
A DECISION, NOWHERE ELSE. Its instances:
- THE SMALLEST INSTRUMENT that produces verifiable work. A snippet or
  a patch before a Code session; a Code session before a brief and a
  session; one model before a relay to three. The choice is said in
  one line, so it can be questioned. (Founding case, November 2: a
  176-line brief written for a Code session to change one marker
  symbol, dropped when Tony asked for the patch that was the right
  instrument from the start.)
- NO SPECULATIVE DOCUMENTS. A brief is written when its session is
  next, not in case; a design record when the talk has happened.
- READ WHAT THE JOB FIRES, IN THE PARTS THE JOB NEEDS. A skill whose
  rules govern the work at hand is read in full; a skill loaded for
  its version line or for one section is read in those parts, by its
  read plan. The Stale Skill check needs the version line and the
  manifest row, both in the first lines.
- TOOL OUTPUT STAYS OUT OF THE CONVERSATION UNLESS IT IS READ. A
  folder listing or a log is sliced for the line wanted, never loaded
  whole to read one size.
- RECORDS AT THE LENGTH THE READER NEEDS. A handoff states a decision
  in a sentence and points at the ledger for the rest; it does not
  restate what the ledger holds. Plain speech (the Register Rule) is
  not length: one plain sentence beats three compressed ones and
  three plain ones alike.
- CROSS-MODEL REVIEW FOR DOMAIN UNCERTAINTY, not for routine (Mode
  7's own "When NOT to use").
- MEASURED, OR IT IS A WISH. A Code session's report ends with its
  token count as its environment prints it (Claude Code's /cost
  output: input and output tokens, by model), and Tony writes the
  count in his run record beside the commit. A session whose
  environment prints no count says so and gives the sizes of what it
  read and wrote. A rule nobody measures is the check that cannot
  fail. (Tony's ruling, November 2, 2026, on the measured half:
  "yes".)

[QUALITY] on this document's own promotion test: a session that
overspends delivers a result that is correct and costly, which is
recoverable, and the count in the run record is what makes the
overspend visible. The tier moves up when a failure shows it was
load-bearing. L-506.



PART 4: FOUNDATION
"""

V3_121 = b"""v3.121 (November 2, 2026): ONE rule added to this document: Token
Economy [QUALITY], in Part 2 after Method Belongs to the Skill, with
two rows in the Anti-Patterns table. No skill bump. TOKENS SPENT WHERE
THEY BUY VERIFICATION OR A DECISION, AND COUNTED.

WHAT PROMPTED IT. Tony, Nov 2, 09:24 Chicago, in the coordinating
session (Claude Fable 5.1, orrery fd3551cc and gallery b7ddf775 read
live), after it had written a 176-line brief for a Code session to
change one marker symbol and dropped it when he asked for a patch
instead: "I am becoming very concerned about the environmental cost
of token generation ... I would like to make part of our protocol
token economy." Asked whether the rule should carry a measured half,
a token count in every Code report and run record: "yes" (09:29).

WHAT CHANGED. The section's one sentence and its seven instances: the
smallest instrument; no speculative documents; a skill read in the
parts the job needs; tool output sliced, not loaded; records at the
reader's length; cross-model review for domain uncertainty; and the
count, as Claude Code prints it, in the report and in the run record.
The orrery's CLAUDE.md, the Code door, amends two sentences to match:
a skill is read in full when its rules govern the work and in parts
otherwise, and the report ends with the count. L-506 opens for it.
ledger-and-session-records carries the shape of the count in the
report and the run record at its next version, the records session's.

THE OBLIGATION TRAVELS. The Project's instructions on claude.ai read
v3.120 until Tony pastes this version in; a chat session reads the
Project page, so the rule reaches chat sessions only then. No skill
changed; nothing to reinstall.

The header stamp and the SHA anchor move with this entry.

Version history: v3.118 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

v3.120 (November 1, 2026): No rule changed in this document. ONE
"""

proto = apply(proto, [
    (b"Tony Quintanilla, PE | Claude | v3.120 | November 1, 2026\n",
     b"Tony Quintanilla, PE | Claude | v3.121 | November 2, 2026\n"),
    (b"Cut from 6a434ed8 at https://github.com/tonylquintanilla/palomas_orrery\n",
     b"Cut from fd3551cc at https://github.com/tonylquintanilla/palomas_orrery\n"),
    (b"absorb. L-256.)\n\n\n\nPART 4: FOUNDATION\n",
     b"absorb. L-256.)\n\n\n\n" + TOKEN_ECONOMY),
    (b"Review only the in-context files  Confident wrong conclusions  ls the uploads dir; read the whole set first\n",
     b"Review only the in-context files  Confident wrong conclusions  ls the uploads dir; read the whole set first\n"
     b"Code session for a snippet-sized change  Tokens buy nothing verifiable  Patch or snippet; the smallest instrument\n"
     b"Write a brief before its session is next  Dropped when the shape changes  Write it when the session is next\n"),
    (b"v3.120 (November 1, 2026): No rule changed in this document. ONE\n", V3_121),
], PROTO)

# ---------------------------------------------------------------------------
# PROJECT_INSTRUCTIONS_HISTORY.md: the v3.118 entry appended to PART 1.
# ---------------------------------------------------------------------------
hist = files[HIST][0]
hist = apply(hist, [
    (b"(Moved down from the resident protocol on 2026-11-01 when\nv3.120 made a fourth entry.)\n\n"
     b"================================================================\nPART 2 -- LESSONS REMOVED FROM THE PROTOCOL AT v3.37\n",
     b"(Moved down from the resident protocol on 2026-11-01 when\nv3.120 made a fourth entry.)\n\n"
     + v118.rstrip(b"\n") + b"\n\n(Moved down from the resident protocol on 2026-11-02 when\nv3.121 made a fourth entry.)\n\n"
     b"================================================================\nPART 2 -- LESSONS REMOVED FROM THE PROTOCOL AT v3.37\n"),
], HIST)

# ---------------------------------------------------------------------------
# CLAUDE.md, the Code door.
# ---------------------------------------------------------------------------
door = files[DOOR][0]
door = apply(door, [
    (b"in PROJECT_INSTRUCTIONS.md (the protocol) and in skills/ (the skills).\n"
     b"Added October 26, 2026, by Tony's ruling of that night, on the first\n"
     b"Code session.",
     b"in PROJECT_INSTRUCTIONS.md (the protocol) and in skills/ (the skills).\n"
     b"Added October 26, 2026, by Tony's ruling of that night, on the first\n"
     b"Code session; amended November 2, 2026 for the protocol's Token\n"
     b"Economy (v3.121, L-506)."),
    (b"in PROJECT_INSTRUCTIONS.md says which skill fires on which work. Read\n"
     b"each one the job fires, in full, before the work, and open your first\n"
     b"report by naming the skills you read and the version line each one\n"
     b"carries.",
     b"in PROJECT_INSTRUCTIONS.md says which skill fires on which work. Read\n"
     b"each one the job fires before the work: in full when its rules govern\n"
     b"the work; in the parts its read plan names when it is loaded for its\n"
     b"version line or one section (the protocol's Token Economy). Open your\n"
     b"first report by naming the skills you read and the version line each\n"
     b"one carries."),
    (b"  into his run record; then his run order (what to look at, what to\n"
     b"  commit), then the Tony-action rollup.\n",
     b"  into his run record; then the session's token count as Claude Code\n"
     b"  prints it (the /cost output: input and output tokens, by model),\n"
     b"  which Tony writes in his run record beside the commit (the\n"
     b"  protocol's Token Economy, L-506); then his run order (what to look\n"
     b"  at, what to commit), then the Tony-action rollup.\n"),
], DOOR)

# ---------------------------------------------------------------------------
# LEDGER_CONSOLIDATED.md: L-506 at the top of section A.
# ---------------------------------------------------------------------------
L506 = b"""#### [L-506] Token economy: tokens spent where they buy verification or a decision, and counted (protocol, every session)
<!-- L:506 status:OPEN upd:2026-11-02 section:A flag: rice: -->
- **Opened 2026-11-02** by the coordinating session (Claude Fable 5.1,
  orrery fd3551cc and gallery b7ddf775 read live), on Tony's ruling of
  09:24 Chicago: "I am becoming very concerned about the environmental
  cost of token generation ... I would like to make part of our
  protocol token economy." On the measured half, a token count in every
  Code report and run record, 09:29: "yes".
- **Protocol v3.121:** the section Token Economy [QUALITY] in Part 2
  after Method Belongs to the Skill (one sentence, seven instances: the
  smallest instrument, no speculative documents, a skill read in the
  parts the job needs, tool output sliced, records at the reader's
  length, cross-model review for domain uncertainty, the count); two
  Anti-Patterns rows; CLAUDE.md's reading sentence and report sentence
  amended to match. Delivered as `patch_L506_token_economy.py`.
- **Founding case,** the same morning: a 176-line brief written for a
  gallery Code session to change one marker symbol (L-505, the x
  marks), dropped when Tony asked for the patch that was the right
  instrument; and a 166,000-character folder listing pulled into the
  session twice to read two file sizes.
- **Tony-action (do):** after this patch is pushed, paste the repo's
  PROJECT_INSTRUCTIONS.md (v3.121) into the Orrery Project's
  instructions on claude.ai; no skill changed, nothing to reinstall.
**Gap:** ledger-and-session-records' next version (the records
session's) carries the count's place in a Code report and in the run
record, and what a chat session, which prints no count, reports
instead (the sizes of what it read and wrote). The first Code report
with a count is the proof the rule runs.
**Ref:** `HANDOFF_coordination_20261102_morning.md`; the protocol's
v3.121 entry; L-505.

"""
ledger = files[LEDGER][0]
ledger = apply(ledger, [
    (b"## A. ACTIVE SEPARATE TRACKS (not orrery-refactor backlog; cross-referenced)\n\n#### [L-505]",
     b"## A. ACTIVE SEPARATE TRACKS (not orrery-refactor backlog; cross-referenced)\n\n" + L506 + b"#### [L-505]"),
], LEDGER)

# ---------------------------------------------------------------------------
# WHERE_WE_ARE.md: by section, nothing below the marker.
# ---------------------------------------------------------------------------
wwa = files[WWA][0]
wwa = apply(wwa, [
    (b"Last updated: November 2, 2026, morning: the coordinating session (the ticks' ruling restored; the x correction next).\n",
     b"Last updated: November 2, 2026, morning: the coordinating session (the ticks' ruling restored; the x patch; token economy).\n"),
    (b"> - Nov 2: neither night fired by 14:34 UTC; you ran both by hand.\n",
     b"> - Nov 2: neither night fired by 14:34 UTC; you ran both by hand.\n"
     b"> - Token economy is in the protocol (v3.121): paste it into the Project.\n"),
    (b"Standing rulings. A line leaves after a few weeks, once it is habit.\n",
     b"Standing rulings. A line leaves after a few weeks, once it is habit.\n"
     b"- Tokens are spent where they buy verification or a decision: the\n"
     b"  smallest instrument, no document before its session, a skill read in\n"
     b"  the parts the job needs, and a token count in every Code report (Nov 2).\n"),
    (b"- The main belt: random dots in JPL's orbits' spread, not one date's (Oct 28).\n"
     b"- A new body's words carry no orbit numbers; its hover prints them (Oct 28).\n",
     b"- The main belt: random dots in JPL's spread; a new body's hover prints its orbit numbers (Oct 28).\n"),
    (b"- L-490 (the legacy list): who besides you and Paloma holds the accounts.\n"
     b"- L-499 (kinds of session): the protocol's Mode 7 text (Oct 27).\n",
     b"- L-490 (the legacy list): who holds the accounts; L-499 (kinds of session), Oct 27.\n"),
    (b"- The belt's cloud: a row first in its group, ticked like a body (Oct 29).\n", b""),
    (b"2. Choosing a date, and animation.\n3. The website's", b"2. The website's"),
    (b"- Today: `HANDOFF_coordination_20261102_morning.md` (the lost ruling,\n"
     b"  the lesson, the nights of Nov 2); the design record's section 6; L-505.\n",
     b"- Today: `HANDOFF_coordination_20261102_morning.md` (the lost ruling,\n"
     b"  the lesson, the nights); the design record's section 6; L-505; L-506.\n"),
], WWA)
marker = wwa.index(b"--- Your run record below this line")
above = wwa[:marker].count(b"\n")
if above > 130:
    fail("WHERE_WE_ARE.md would have %d lines above the marker; the cap is 130" % above)

# ---------------------------------------------------------------------------
# Write, all or nothing having been checked.
# ---------------------------------------------------------------------------
out = [(PROTO, proto), (HIST, hist), (DOOR, door), (LEDGER, ledger), (WWA, wwa)]
counts = {PROTO: 5, HIST: 1, DOOR: 3, LEDGER: 1, WWA: 8}
for path, text in out:
    open(path, "wb").write(text)
    print("ok %s (%d edits)%s" % (path, counts[path], "; was CRLF in the working copy, written LF" if files[path][1] else ""))
open(COPY, "wb").write(proto)
print("ok %s (new; the versioned copy, %d bytes)" % (COPY, len(proto)))
print("Where We Are: %d lines above the marker (cap 130); nothing below it touched." % above)
print("patch applied")
print("")
print("Next, in this order:")
print("  1. Run ledger_index.py (VS Code, Run) from this folder: it rebuilds the ledger's index with L-506.")
print("  2. GitHub Desktop: commit and push the orrery, everything in the change list together")
print("     (this patch's six files, the index, the design record, the morning handoff; move this")
print("     script into documentation\\ for the next commit).")
print("  3. Paste the repo's PROJECT_INSTRUCTIONS.md (v3.121) into the Orrery Project's instructions")
print("     on claude.ai. Chat sessions read that page; the rule reaches them only then.")
print("  4. The next Code session's report ends with its token count; write it in the run record.")
