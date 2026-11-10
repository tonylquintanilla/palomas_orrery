<!-- Doc-Kind: hand | The brief for one Claude Code session on the orrery: L-522 (document caps), step 1, the mechanism. Communication; written once, read by its session. -->
# Brief: document caps, step 1 (orrery)

Built on orrery d03908908a0e0028ff146f5b2e7f8bf6a316cf0e at
https://github.com/tonylquintanilla/palomas_orrery
and gallery e0e94b8566860bdd595daa6baf8f7727dddaf668 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io
(both branch main, read 2026-11-10, 12:25 Chicago). The ledger item,
L-522 (document caps), and this brief are in Tony's next orrery push;
the session reads them in the folder in front of it. Nightly bot
commits since are expected.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: BUILD, a Claude Code session in the ORRERY repository, through the
python_work door. The gallery is not touched. Written November 10, 2026
with Anthropic's Claude Fable 5.2, the coordinating session, after
Tony's rulings of 09:42 to 12:21 Chicago.

## What step 1 is, in one paragraph

The project's working documents only grow. Tony ruled a length cap on
each one, and that a session which adds to a document at its cap moves
something out first. Step 1 builds the part that makes this hold: one
short page that lists each document's cap and where its old lines go,
and one row in the maintenance run that prints any document over its
cap, by name. Every cap starts at the document's size at the end of
this session, so nothing can grow from that day and nothing is red.
Nothing is reduced in this step. The reductions are steps 2 to 6, each
its own session.

## Start

1. The orrery's CLAUDE.md, from its first step.
2. L-522 (document caps) in `LEDGER_CONSOLIDATED.md`, in full. Then
   `documentation/DESIGN_document_caps_rulings_20261110.md`. The
   review's measurements are in
   `documentation/REVIEW_fundamental_documents_20261110.md`; read it
   only where this brief sends you.
3. Skills: ledger-and-session-records (1.22, in full: this session
   changes it); safe-file-editing (1.14); agentic-pre-test (1.3). A
   copy that disagrees with the manifest: stop and say so.
4. L-522 carries one open decision of Tony's: all the caps on one page,
   or each cap in its document's own first lines. This brief is written
   for the one page. If the ledger shows he chose the first lines, stop
   and tell him the brief needs its second section rewritten.
5. Ask Tony ONE thing before building: this session changes the records
   skill. May it edit that SKILL.md, run `skills_index.py`, and add one
   protocol version entry (the records skill's binding rule)?

## The job, in three parts, with a stop and a report after each

**Part 1: the page and the check.**
- A new root document, `DOCUMENT_CAPS.md`, hand-written, with its
  Doc-Kind line. It holds the three rules in plain words (L-522 states
  them) and one table: document, cap in lines, overflow home. It is
  written for Tony to read and to change a number in. Keep it under
  60 lines.
- The rows, and each one's home:
  - `PROJECT_INSTRUCTIONS.md` ->
    `documentation/PROJECT_INSTRUCTIONS_HISTORY.md`
  - each of the twelve `skills/<name>/SKILL.md` ->
    `documentation/SKILL_HISTORIES.md`
  - `documentation/WHERE_WE_ARE.md` -> git only. Its cap is the 130
    lines above its run-record marker that the records skill already
    rules; the count stops at the marker.
  - `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md` ->
    `documentation/MASTER_PLAN_HISTORY.md`
  - `README.md`, `CLAUDE.md` and `DOCUMENT_CAPS.md` itself -> git only
  - `LEDGER_CONSOLIDATED.md`: listed with NO cap until step 4 gives it
    a place for closed items. The check prints its size and says so.
- Every other cap is the document's line count at the end of this
  session, after this session's own edits to it.
- The check reads the page and prints, for every row, the document, its
  lines now, its cap and its home. The run's row is named "Document
  caps". It is red, and names the document, when: a document is over
  its cap; a row's file is not found; a `SKILL.md` exists under
  `skills/` with no row; a row cannot be read. A count is never printed
  without the names (A Report Names Its Items).
- `doc_index.py` already reads the root's documents and is already in
  the run. Whether the check lives there or beside it is method: say
  which and why. One tool, not two. The dashboard has a parity check
  (`test_dashboard_parity.py`); a new row must satisfy it.
- Show that the check can fail (A Check That Cannot Fail Is Not
  Passing): on a throwaway copy, add lines to a capped document, remove
  a row's file, and add a skill folder with no row. The report prints
  the three red results.

**Part 2: the rule where a session will meet it.**
- `CLAUDE.md`, in its section "What a Code session writes, and what it
  does not", one or two lines: before adding to a document listed in
  `DOCUMENT_CAPS.md`, read
  its row; at its cap, move something out first, to its home; a session
  never raises a cap.
- The records skill (`skills/ledger-and-session-records/SKILL.md`),
  1.22 to 1.23. Its Where We Are section ends with a bullet that begins
  "THE CHECK, recorded on L-396 and not yet built". Replace that bullet
  with what is now built and a pointer to `DOCUMENT_CAPS.md`. Only the
  130-line half of L-396's check is built here. The date half compares
  the page with the ledger's header stamps, which step 4 removes; it
  stays on L-396, and the bullet says so.
- Pay where you touch, in this session first: the records skill ends no
  longer than the 807 lines it began with, and `CLAUDE.md` no longer
  than its 100 plus the lines added here. If the three-entry rule moves
  a version entry down, that is the room.
- `skills_index.py`, the protocol's version entry and the manifest, by
  the binding rule. The protocol's row on the page takes the protocol's
  size after that entry.

**Part 3: the two stray CLAUDE.md files.**
- Claude Code loads a CLAUDE.md it finds in a subfolder when a session
  reads a file in that folder. Two sit under `documentation/`:
  - `documentation/CLAUDE.md`, a Claude Code handoff of February 2026.
    It names protocol v3.9 and says to work in a sandbox and never touch
    the repository folder. Every session that reads Where We Are has it
    loaded.
  - `documentation/python_work_door/CLAUDE.md`, the canonical copy of
    the door in the parent folder.
- Rename both so neither is named CLAUDE.md where it sits. Use
  `git mv`, so the history follows. The names are method; say them. The
  February file is a record: its words are not edited.
- The door's own text says where its canonical copy lives. Correct that
  sentence in the canonical copy. The copy in Tony's `python_work`
  folder is outside this repository and is his to replace: a
  **Tony-action (do)**, with the exact file to copy and the name it
  must have there.
- Live references to the old paths are few: L-499 (the kinds of
  session) and Where We Are's last section name the door's folder,
  which does not change. Do not edit handoffs, spent patches or run
  records to match; they are history.

## Out of scope

- No document is shortened beyond what Part 2 asks.
- No cap line is written into any skill's header or any document's
  first lines.
- The website's `README.md` and `CLAUDE.md` get their rows from a
  website session. Note on L-522 that the website's CLAUDE.md is owed
  the cap rule, and the Token Economy lines of November 2 it never
  received.
- The 500-line warning, the contents lists and the read plans in
  `skills_index.py` stay as they are.

## Checks

- The orrery maintenance run, whole: the new row green, and no row red
  that was green at the base. Name any row red at the base.
- `ledger_index.py --check` and `skills_index.py --check` after the
  records.
- The three red results of Part 1, from the throwaway copy.

## Close

- L-522: step 1 done, what was built, the caps as set (the table, by
  name), and what is owed. L-396: its 130-line half built.
- Where We Are, by section, within its 130 lines: the road's line d,
  Do next, Needs you now.
- The final report, in the form CLAUDE.md's "How to report to Tony"
  sets: every file changed; the caps table; the Tony-action rollup (the
  commit and push, the door's copy, the records skill's reinstall, the
  protocol's paste); the token count as the environment prints it.
- A consequence to state plainly to Tony in the report: from this
  session on, the Mars session is the first that will have to move old
  lines out of interactive-exhibit before adding new ones. Its home for
  now is `documentation/SKILL_HISTORIES.md`, and its version notes and
  "until v1.x" remarks are what moves.
- Commit and push are Tony's.
