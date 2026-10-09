<!-- Doc-Kind: hand | Brief for the testing session after the provenance split (L-418): the four skill tests A3 to A6, a planted-fault run that measures what checks a citation's location record, and a feasibility count for storing a verbatim quote beside each sourced row. Written October 8, 2026. -->
# Handoff: the testing session after the split (L-418), the brief

Built on orrery 1e30953 (full: see `git log`, "L418_4 close", 2026-10-08
22:21 CDT) at https://github.com/tonylquintanilla/palomas_orrery.
Gallery at b50f8bd at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, not
touched. Written by the Fable 5.1 coordination session of October 8,
which read both repos at HEAD and wrote no patch.

- Type: TESTING, records-only at the close. The session edits no
  deliverable file. Every run happens on a throwaway copy.
- Companion to `documentation/TESTING_PROTOCOL_provenance_skills_20261008.md`
  (the protocol this brief carries out) and
  `documentation/HANDOFF_L418_split_build_20261008.md` (the build's
  record). Where this brief adds to the protocol, it says so.
- Skills this session fires: provenance-discipline 2.27 (read by the
  plan at its top, every part), provenance-cross-check 1.0 (expected
  to fire in test A4 and NOT in A5), ledger-and-session-records 1.18
  (the close), safe-file-editing 1.13 (the records patch),
  agentic-pre-test 1.3 (the throwaway rule for the planted-fault
  run). In the first reply, read back the version line of each loaded
  copy, and list both new skill folders with their reference files
  (tests A1 and A2, repeated in a fresh session, as the split's
  handoff asks).
- The protocol is PROJECT_INSTRUCTIONS.md v3.86. Its manifest has
  twelve rows; a loaded version that differs from its row is a stop,
  not a note.

## Read this first

- *Three parts, in order: the skill tests (A3 to A6), the
  planted-fault run, and a count for the quote idea. The third
  measures; it builds nothing.*
- *Tony decides L-425 (citation location checks) AFTER this session,
  on the planted-fault results. Do not ask him to decide it first.*
- *Nothing in this session is run on Tony's machine. The maintenance
  run goes on a throwaway clone, as the split session did.*
- *The close writes results into the ledger by name, not by count.*

## Part 1 -- the skill tests A3 to A6

Run them as the testing protocol says, each with its pass and fail
stated. Two notes from the coordination session:

- **A6 (the read plan) is a test of reading the FILE, not of loading
  the skill.** A loaded skill arrives whole in one block, so a session
  that "loads provenance-discipline" never exercises the plan. Test
  A6 by reading `skills/provenance-discipline/SKILL.md` from the
  throwaway clone with the file reader, and say which parts the plan
  named and which were read, in order.
- **A3 (the figures pointer) needs a real figures task.** Use a
  throwaway copy of constants_new.py and a row that exists, so the
  task is ordinary; the question is only whether
  `references/figures.md` was opened before the line was written.
  Say plainly afterwards whether it was.

Record each as PASS or FAIL with one sentence of evidence. If A3 to A6
all pass, L-418 (splitting provenance-discipline) closes at this
session's close, as the split's handoff says.

## Part 2 -- the planted-fault run

### Why

Section B2 of the testing protocol is a table of what checks each
kind of broken citation record. It was written by reading the code.
That is a claim about what runs, not a measurement, and the protocol's
own gate (Verify Execution, Not Appearance) says the run wins over the
reading. This part turns the table into a result.

### How

1. Clone HEAD into a throwaway directory. Run
   `orrery_maintenance_run.py` on it UNPLANTED first and keep the full
   output. This is the baseline; every later comparison is against it,
   so a fault that "fires" is a line that was not there before.
2. Plant the seven faults below, each on a DIFFERENT row of
   `constants_new.py`, each recorded as: row name, line number, the
   line before, the line after. Choose rows on the active build path
   (the Sun and Earth rooms' served rows are the safest choice; the
   objects export names them).
3. Run `orrery_maintenance_run.py` again, and `test_status_lines.py`,
   `worksheet_checker.py` and `provenance_scanner.py` on their own as
   well, so a message the summary hides is still seen.
4. For each fault, record: which checker named it (file and the
   printed line, verbatim), whether that checker gates the push or is
   report-only, and whether the SUMMARY line changed. A fault that
   changes a count but names nothing is recorded as "count only"; that
   is a finding under A Report Names Its Items, not a pass.

### The seven faults, and what the table predicts

| # | Fault planted | The table predicts |
|---|---|---|
| F1 | A `# Source:` line removed from a row marked V_SOURCED | Caught twice: the scanner (Tier-1, gates on the build path) and test_status_lines.py rule 4 (gates) |
| F2 | A `# Access:` line removed | Nothing |
| F3 | A `# Read:` line's record file renamed to one that does not exist in documentation/ | Nothing |
| F4 | A `# Cross-checked:` line's worksheet renamed to one that does not exist | worksheet_checker.py layer L0, report-only |
| F5 | A `# Access:` address changed to a dead one (a page that does not exist on a real site) | Nothing; no check opens addresses |
| F6 | A `# Read:` locator changed to the wrong place (Table 2 to Table 7, or page 4 to page 40) | Nothing; no tool reads the document |
| F7 | A row's VALUE changed, on a row whose worksheet verdict is CONFIRMED, with every comment line left as it was | worksheet_checker.py reports DRIFTED, routed to conversation |

F7 is the one the table does not list. It tests the value side of the
same record: whether a number can drift away from the citation that
still sits beside it. It also exercises L-424 (the checker's one word
for two cases): if the checker prints UNCHECKED_MOVE instead of
DRIFTED, say which of the two cases it was, from the checker's own
line.

### What a result looks like

A table with one row per fault: predicted, observed, the checker's
verbatim line or "silent", gating or report-only. Then one sentence
per fault where observed differs from predicted. The expected shape
is three caught (F1, F4, F7) and four silent (F2, F3, F5, F6). If that
is what happens, the table was right and L-425's three options stand
as written. If not, say what the table got wrong before anything else
is built on it.

The planted copy is deleted at the end. Nothing from it is delivered.

## Part 3 -- the quote idea, measured and not built

Tony's question, October 8: "can we require an exact quote of the
cited number in context and stored?" That is the Exhibit Requirement
in provenance-cross-check (a verdict without a quotation is
UNVERIFIED) moved one layer down, from the worksheet to the row
itself. What it would give L-425 is a FOURTH level, the only one that
reaches the protocol's failure 4 (the page opens but does not say the
number):

- Offline, no internet: a check that the stored quote contains the
  row's number as the source prints it. A quote that does not contain
  the number fails; a row with no quote is reported by name.
- Online, on Tony's machine with the link check (level 3): a check
  that the page at the `# Access:` address still contains the quote.
  A quote that is not on the page is either a changed page or an
  invented quote, and both are findings.

The honest limit, to be stated when this reaches Tony: a quote can be
invented as easily as a citation. The offline check cannot tell a
real quote from an invented one that happens to contain the number.
Only the online check can, so a `# Quote:` line is worth storing only
if level 3 is built and run. Stored and never checked, it is a check
that cannot fail. And Tony's ruling of August 27 stands: he does not
read quotes himself; a quote is for the tool, and the link beside it
is for him.

This session MEASURES whether the idea is buildable, and does not
build it or write a rule. The count is bounded (The Artifact Bounds
the Audit) to the rows the Sun and Earth rooms serve; the export
names them. For those rows:

- How many have a `# Read:` locator at all, and how many of the
  locators name a sentence or a page (quotable) against a table or
  figure (where the "quote" would be a table row or a caption).
- Pick five whose `# Access:` addresses are on sites this sandbox can
  reach (arXiv, NASA, ADS, open journals). For each, fetch the page,
  find the number, and write the verbatim sentence or table line that
  contains it, with the locator. Report each as: quote found, number
  not on the page at that locator, or site unreachable from here.
  "Unreachable" is a limit of the sandbox, and the protocol already
  says level 3 runs on Tony's machine; record it, do not work around
  it.
- Where the quote is a unit conversion away from the stored value
  (the paper says km, the row stores AU), say so; that is the case
  where "contains the number" needs the source-form number, which the
  conversion lines already carry.

Report the counts and the five tries by name. Then write ONE design
question for Tony on L-425, with the numbers beside it: whether a
`# Quote:` line becomes a fourth level, where it lives (beside
`# Read:` in constants_new.py, or in the record file the `# Read:`
line names), and whether it is required of new rows only or
backfilled for the served slice. Do not answer it for him.

## At the close

- The ledger: L-418 (splitting provenance-discipline) closes if A3 to
  A6 passed, with the four results in its block. L-425 (citation
  location checks) gains the planted-fault table, by name, and the
  quote count, with the one design question above; its Tony-action
  (decide) now reads "which of the levels to build, on the measured
  results". L-424 (the checker's one word) gains F7's observation if
  it bears on it.
- Tony's page, by section: the READ THIS FIRST box says what the run
  found, in sentences; "Needs you now" carries the L-425 decision with
  the result beside it; nothing below the marker. Every handle
  labelled.
- The handoff: `documentation/HANDOFF_L418_testing_20261008.md` (or
  the date it closes), anchored on 1e30953 and on HEAD at the close.
- The records patch, tested on throwaway copies alone and a second
  time over, with Tony's steps printed: run from the orrery repo root
  (VS Code, Run), then `orrery_maintenance_run.py`, move the script
  into documentation/, commit and push.

## What this session does not do

- It does not build any of L-425's levels, and does not write a
  `# Quote:` rule into any skill.
- It does not change `constants_new.py`, `provenance_scanner.py`,
  `test_status_lines.py` or `worksheet_checker.py` in the repo. Every
  planted line lives on the throwaway copy and dies with it.
- It does not ask Tony to run anything until the records patch at the
  close.

## Tony-actions, before and after

- (do, before) None. The session starts fresh from this brief.
- (do, after) Run the records patch, the maintenance run, push; move
  this brief and the handoff into documentation/.
- (decide, after) L-425: which levels to build, with the planted-fault
  table in hand; and the quote question, with the count in hand.
- (decide, after) L-424, if F7 showed the one-word case.

Brief written October 8, 2026, with Anthropic's Claude Fable 5.1.
