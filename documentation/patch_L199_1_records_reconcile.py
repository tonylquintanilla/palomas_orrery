"""patch_L199_1_records_reconcile.py -- L-199, and L-200 through L-205.

SUPERSEDES patch_L204_2_ledger_reconcile.py. Delete that file and run
this one instead; it contains every edit that one made, plus the
records restructure. If you already RAN it, this aborts on the
fingerprint check and says so.

RUN COMMAND
-----------
Save this file into the palomas_orrery repo root (the same folder as
LEDGER_CONSOLIDATED.md), open it in VS Code, and click Run.

    python patch_L199_1_records_reconcile.py

Then, and this part is not optional:

    python ledger_index.py

Success prints one `ok` line per file and then `patch applied`. Failure
prints a single ERROR, ANCHOR FAIL or SPAN FAIL line and writes NOTHING.

WHAT IT DOES
------------
Two jobs that both edit LEDGER_CONSOLIDATED.md, which is why they are
one patch: two scripts fingerprinting the same file would abort the
second by construction.

JOB ONE -- the ledger was five handles behind the code.

  L-200  the Resolved leg and its linkage check     -> DONE
  L-201  request selection                          -> DONE
  L-202  JSON worksheet format                      -> DONE
  L-203  the visibility convention, in the skill    -> new, DONE
  L-204  the worksheet reference may be JSON        -> new, DONE
  L-205  the runner's verdict lines carry evidence  -> new, DONE
  L-206  worksheet return filenames                 -> new, OPEN
  L-207  the citation prompt                        -> new, OPEN

Only the block bodies are edited. The index table near the top is
GENERATED, so `ledger_index.py` rebuilds it from these blocks and moves
each newly-DONE block into its closed bucket.

JOB TWO -- L-199, the records restructure, per Tony's ruling 2026-08-18.

  documentation/LESSONS_ARCHIVE.md  is RENAMED
  documentation/PROJECT_INSTRUCTIONS_HISTORY.md

and now carries TWO records rather than one:

  PART 1  the protocol's version history, v1.0 through v3.38, moved out
          of the ledger's Appendix, which is deleted and replaced by a
          pointer.
  PART 2  the twenty-seven lessons removed at v3.37, kept verbatim.

The protocol document keeps the THREE most recent entries -- v3.39,
v3.40 and the new v3.41 -- and v3.34 through v3.38 come out. They are
not copied anywhere, because they are already in the Appendix that
becomes PART 1. Every entry lives in exactly ONE place, and the rule
that keeps it that way is stated in the protocol: when a fourth entry
is added, the oldest moves down.

L-199's own block warned that v3.39 and v3.40 exist ONLY in the
protocol and that trimming before pushing them down would delete the
only copy. This patch does not trim them -- they are two of the three
that stay resident.

THE HEADER. Two defects, both fixed.

  1. The repo copy read `v3.40 | August 16, 2026`. The copy installed
     in the Claude UI read `v3.40 | August 17, 2026`. Same version, two
     dates, two stores, one of them hand-edited. v3.41 supersedes both
     rather than quietly picking a winner, and the v3.41 entry records
     that the disagreement existed.
  2. The protocol carried no anchor, while its own CRITICAL gate
     requires every document leaving a live session to open with one.
     A relay partner handed this file -- their ONLY source for who they
     are writing for -- had no way to know which repo state it
     describes. It now names the SHA it was cut from, both repos, and
     where the full history lives.

WHAT IS PERMANENT AND WHAT IS NOT
---------------------------------
This script is disposable and one-shot. Permanent: the six ledger
blocks, the renamed history file, the trimmed protocol, and the header.

AFTER RUNNING
-------------
1. python ledger_index.py     (rebuilds the index; moves closed blocks)
2. python maintenance_run.py  (all 13 rows)
3. In GitHub Desktop the rename shows as one file deleted and one
   added, which is normal -- git records renames by content, not by a
   rename operation.
4. Archive this script to documentation/.

Module created: August 18, 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys


FINGERPRINTS = {
    'LEDGER_CONSOLIDATED.md': '661bc628836b60ce34cc7a6e812266e2',
    'PROJECT_INSTRUCTIONS.md': 'dc1ad34f77d38713c9a01d4976663e5d',
    os.path.join('documentation',
                 'LESSONS_ARCHIVE.md'): 'b85d2632a839cd777caf0c1d9b3a2d0f',
}

ANCHOR_SHA = 'b65ac115fc0f820e8270c0807249813c67bde7bc'
REPO_URL = 'https://github.com/tonylquintanilla/palomas_orrery'

OLD_ARCHIVE = os.path.join('documentation', 'LESSONS_ARCHIVE.md')
NEW_HISTORY = os.path.join('documentation',
                           'PROJECT_INSTRUCTIONS_HISTORY.md')


# ---- L-200: closed ---------------------------------------------------

L200_STATUS_OLD = """<!-- L:200 status:OPEN upd:2026-08-17 section:A flag: rice:2/3/85/1 -->"""
L200_STATUS_NEW = """<!-- L:200 status:DONE upd:2026-08-18 section:C flag: rice:2/3/85/1 -->"""

L200_TAIL_OLD = """**Note:** RICE is Claude's proposal, unratified.
**Gap:** unbuilt. Fields depend on nothing outstanding -- reader count
was removed from its critical path 2026-08-17.
**Ref:** L-192 (Break 5); L-196 (the ratchet it must not trip); L-201."""

L200_TAIL_NEW = """- **As built, 2026-08-18** (`patch_L204_1`, shipped with L-204 because
  both touch the annotation grammar and the checker that reads it).
  The grammar lives in `provenance_scanner.parse_resolved`, beside the
  cross-check grammar rather than in a second copy; the linkage layer
  lives in `worksheet_checker.check_resolved`, where the worksheets are
  already loaded. Four ways to fail, all mutation-proven: the leg does
  not parse, the worksheet is not on disk, no row carries the key, or
  the row's citation verdict cleared and so warrants no edit. A fifth
  fires when the named worksheet has no citation-verdict column at all,
  which only a markdown return can produce -- the JSON reader
  synthesizes every column whether the return carried it or not.
- **The count prints on every run, including zero.** "0 Resolved
  leg(s) examined: 0 linked, 0 with a linkage problem." A section that
  says nothing when there is nothing cannot be told from one that never
  ran.
- **One interpretation, made by Claude and NOT yet ruled.** The design
  above wrote `<batch>` as the first token. It shipped as the worksheet
  FILENAME, because a batch name does not determine what the returned
  file is called, and "names a worksheet row that exists" is only
  mechanically checkable against a file on disk. Overrule if the batch
  was meant literally.
**Note:** RICE is Claude's proposal, unratified.
**Ref:** L-192 (Break 5); L-196 (the ratchet it must not trip); L-201;
L-204 (shipped in the same patch); `documentation/patch_L204_1`."""


# ---- L-201: closed ---------------------------------------------------

L201_STATUS_OLD = """<!-- L:201 status:OPEN upd:2026-08-17 section:A flag: rice:2/3/90/1 -->"""
L201_STATUS_NEW = """<!-- L:201 status:DONE upd:2026-08-18 section:C flag: rice:2/3/90/1 -->"""

L201_TAIL_OLD = """**Note:** RICE is Claude's proposal, unratified.
**Gap:** unbuilt. Full detail in
`documentation/DESIGN_20260817_worksheet_selection.md`.
**Ref:** L-196; L-200; L-202."""

L201_TAIL_NEW = """- **As built, 2026-08-17** (`patch_L201_1`, with L-202). Three named
  selections shipped rather than the two planned: `all`,
  `constants_new` (23 of 100 rows), and `sendbacks`, which reads the
  checker-written key list. Builder tests went 41 -> 61.
- **Reachable without the terminal, 2026-08-18** (`patch_L201_2`). The
  builder is a Developer Tools card on the dashboard, un-indented
  because the maintenance runner does not cover it, and marked
  interactive so it opens in its own console. Its card and its module
  docstring both name the three prompts in order and both say that the
  selection prompt DEFAULTS TO 1 -- pressing Enter there produces a
  100-row request that looks exactly like a working tool. The
  docstring's old RUNNING IT block said the tool asks one question and
  writes one file; it asks three and writes two, and had not moved with
  either this item or L-202.
- **Four runner-covered checkers were missing from the dashboard** and
  were added in the same patch, against the 2026-08-12 ruling that a
  tool the runner covers stays visible as its own card. The indented
  group now matches `maintenance_run.py` row for row AND in execution
  order, verified by reading the runner's own GENERATORS and CHECKERS
  lists rather than by eye.
**Note:** RICE is Claude's proposal, unratified.
**Ref:** L-196; L-200; L-202; `documentation/patch_L201_1`,
`documentation/patch_L201_2`;
`documentation/DESIGN_20260817_worksheet_selection.md`."""


# ---- L-202: closed ---------------------------------------------------

L202_STATUS_OLD = """<!-- L:202 status:OPEN upd:2026-08-17 section:A flag: rice:2/3/75/2 -->"""
L202_STATUS_NEW = """<!-- L:202 status:DONE upd:2026-08-18 section:C flag: rice:2/3/75/2 -->"""

L202_TAIL_OLD = """**Note:** RICE is Claude's proposal, unratified.
**Gap:** unbuilt. Needs a checker-side JSON reader as well as a builder
-side emitter.
**Ref:** L-201; L-192 (L2b, the layer the hash protects from
misattribution)."""

L202_TAIL_NEW = """- **As built, 2026-08-17** (`patch_L201_1` emitter, `patch_L202_1`
  reader). The request is written as JSON Lines beside the markdown,
  each row carrying an eight-character hash over its do-not-edit
  fields. The checker reads a returned `.jsonl` into the same Table the
  markdown parser produces, so every existing layer runs unchanged. A
  new layer LH routes back any row whose hash is wrong
  (`ROW_MODIFIED`) or absent (`ROW_HASH_MISSING`); a markdown table has
  no integrity map and reads NOT APPLICABLE rather than pass. Checker
  tests went 69 -> 105.
- **The defect this format left behind, found the same day.** A
  returned `.jsonl` could be checked and routed and then NOT cited: the
  annotation grammar refused a reference that did not end in `.md`.
  Leg 6 of the loop -- turning a verdict into an annotation -- had no
  last inch. Found by building a simulated JSON return and running the
  checker, not by reading the code. Closed under L-204.
**Note:** RICE is Claude's proposal, unratified.
**Ref:** L-201; L-192 (L2b, the layer the hash protects from
misattribution); L-204 (the grammar this format required)."""


# ---- L-203, L-204, L-205: new blocks --------------------------------

# Anchored on the heading alone, which is unique in the file. The
# L-202 Ref line above it has ALREADY been rewritten by an earlier edit
# in this same run, so quoting its original text here would look for
# bytes this script removed two edits ago -- edits apply in sequence to
# one accumulating buffer, not each to the original file.
NEW_BLOCKS_ANCHOR = """## PENDING ACTION (Tony-side)"""

NEW_BLOCKS = """#### [L-203] The visibility convention -- give it a home in the skill
<!-- L:203 status:DONE upd:2026-08-18 section:C flag: rice:2/3/85/1 -->
- **The convention.** A failure that prints where the responder reads
  it gets an ANNOTATION; a failure that appears nowhere gets a
  REFUSAL. Visibility decides, not severity.
- **Where it came from.** L-196 left one question open as Claude's
  call: should a mismatched continuation marker refuse rather than
  report? It reports. The distinction drawn was that a mismatch prints
  into the worksheet where the responder reads it, while an unmarked
  continuation appears nowhere. Tony's ruling 2026-08-17: settle it as
  a CONVENTION rather than a one-off, because the same distinction
  governs every future case of the same shape.
- **It had a record and no home.** Recorded in
  `documentation/DECISIONS_20260817_pilot_design.md`, which nothing
  loads at the moment of need. That is the same failure shape as a
  lesson filed in an archive with no trigger.
- **As built, 2026-08-18** (`patch_L204_1`). Written into
  `skills/provenance-discipline/SKILL.md` next to the annotation
  grammar, marked CRITICAL, with the generalization stated: before
  choosing between reporting and refusing, ask where the report lands
  and who reads it -- if it lands in a log nobody opens or a file the
  next session will not load, reporting is silence wearing the costume
  of diligence. Skill 2.3 -> 2.4. No tool behaviour changed.
- **The obligation this creates.** A mid-session reinstall cannot be
  verified from inside the session that makes it, so the NEXT session
  confirms its own loaded copy reads 2.4 before doing provenance work.
**Note:** RICE is Claude's proposal, unratified.
**Ref:** L-196 (where the question arose); L-186 (the annotation
grammar it sits beside); `documentation/patch_L204_1`.

#### [L-204] The worksheet reference may be JSON
<!-- L:204 status:DONE upd:2026-08-18 section:C flag: rice:2/3/95/1 -->
- **The defect.** `provenance_scanner.parse_cross_checks` required the
  parenthetical worksheet reference to end in `.md`. A line citing a
  `.jsonl` return was refused with the code `non_markdown_reference`,
  earned nothing, and was reported as a diagnostic. So a verdict could
  be built, carried, filled, returned, checked and routed -- and then
  refused when somebody wrote it back into the code. Leg 6 of the loop
  had no last inch, and the pilot could not dispatch.
- **Found by an integration test, not a reading.** A simulated JSON
  return was built, a constant annotated to cite it, and the checker
  run; it listed the worksheet as UNCITED. Reading the code would not
  have produced this.
- **The condition did two jobs, and only one of them moved.** It
  required the reference to name a FILE rather than free prose, which
  is the anti-gaming half of L-186 and stays. It also pinned the only
  worksheet format that existed in August 2026, which stopped being
  true on 2026-08-17 when L-202 landed.
- **Tony's ruling, 2026-08-18:** widen the extension set, taking
  Claude's recommendation over the two alternatives. Rendering
  accepted JSON returns into markdown for citation was rejected
  because it leaves two stores of one return, free to drift, with the
  integrity hash in only one of them; a hand-written markdown
  companion adds the same drift plus manual work per return.
- **As built** (`patch_L204_1`). One condition in one function, plus
  the three wordings that would otherwise have become false -- the
  docstring's code list, its prose, and the report's own explanation
  of what earns V2. `non_markdown_reference` became
  `unsupported_reference_format`, which is what the rule now says.
  `WORKSHEET_REFERENCE_SUFFIXES` is defined once in the scanner and a
  test pins the checker's `JSON_SUFFIXES` against it, so a fourth
  format added in one place fails loudly instead of drifting in two.
- **The skill's examples are checked now too.** `skills_index.py`
  already parsed `# Cross-checked:` examples in skill files; it parses
  `# Resolved:` examples the same way. A skill teaching a leg its own
  parser refuses is the L-186 defect in a second grammar.
**Note:** RICE is Claude's proposal, unratified.
**Ref:** L-186 (the shape rule that did not move); L-202 (the format
that required this); L-200 (shipped in the same patch);
`documentation/patch_L204_1`.

#### [L-205] The runner's verdict lines carry evidence
<!-- L:205 status:DONE upd:2026-08-18 section:C flag: rice:2/3/90/1 -->
- **Two defects, both raised by Tony, both the same shape as L-197 and
  neither fixed by it.**
- **One: the summary counted report-only tools as passing.** Eleven of
  thirteen checkers are pass/fail. Two -- `worksheet_checker.py` and
  `provenance_scanner.py` -- exit 0 whatever they find, and exit 1
  only when they could not run. The summary said "All 13 checkers
  passed" above a row reporting 289 Tier-1 findings. Both statements
  true; read together they tell someone scanning for a verdict that
  there is nothing to act on. A line that reads the same whether the
  scanner found 289 or 0 cannot inform, because it cannot move.
- **Two: four verdict lines could not move either.** Constants
  relations, Cross-check annotations, Citation inheritance and Scanner
  recognition each ended in a fixed sentence. Tony's question --
  "Real citations recognized, fake ones refused: is this intent or
  result?" -- has the answer that it is a result, since it prints only
  after the failure branch has returned, but a result that reads
  identically whether 27 tests ran or two. Each file already printed
  the count two lines earlier; the runner quotes the LAST line.
- **As built, 2026-08-18** (`patch_L188_1`, `patch_L188_2`). CHECKERS
  rows gained an optional fourth field marking a tool report-only, set
  on exactly two; the summary counts the gating eleven in its headline
  and quotes the two report-only verdicts underneath, in both the
  passing and failing branches, because the scanner's count is what the
  push call turns on. The four fixed lines now carry `N of N`, keeping
  the words that say what was checked -- a bare count trades one
  blindness for another. Proven by mutation: deleting one test from
  each suite makes the lines read 18, 19, 26, 17.
- **Fixed in passing.** `test_provenance_1d.py` carried a comment
  saying the runner trims a verdict to 44 characters. Measured: 44 is
  the WRAP width and `wrapped()` deliberately gives a verdict no
  ellipsis. The wrong note argued directly against the change being
  made, so it was corrected rather than left to mislead.
- **Still not fixed, and inherited from L-197.** Eleven of thirteen
  rows resolve their verdict by last line, so any of them can be
  displaced the moment something prints later. Giving every row a hint
  substring is the general cure and was not attempted.
- **Process note.** The first cut of `patch_L188_1` compiled cleanly
  and died on the run: widening the results tuple broke a
  failure-detail loop that unpacked a fixed width. `py_compile` cannot
  see a tuple width, which is the resident gate restated in a new
  place.
**Note:** RICE is Claude's proposal, unratified.
**Ref:** L-188 (the runner); L-197 (the same defect class, earlier
instance); `documentation/patch_L188_1`, `documentation/patch_L188_2`.

#### [L-206] Worksheet return filenames carry model and session
<!-- L:206 status:OPEN upd:2026-08-18 section:A flag: rice:2/3/85/1 -->
- **The requirement, Tony 2026-08-18.** Beyond tracking, the filename
  must identify the originating MODEL and SESSION.
- **The shape, confirmed 2026-08-18.**
  `worksheet_<model>_<batch>_<YYYYMMDD>.jsonl`, e.g.
  `worksheet_claude-opus-5_pilot_constants_new_20260818.jsonl`.
  Underscores separate fields; hyphens live INSIDE a field. Parse from
  both ends -- literal `worksheet`, then model, then the date last --
  so the batch keeps the underscores it already has.
- **Session is the date, with a trailing letter when a day repeats**
  (`_20260818b`). Not hypothetical: 2026-08-18 alone would have needed
  it.
- **The model field carries the VERSION; the annotation identity does
  not.** The scanner compares checker identity as a plain string and
  says so -- "Gemini" and "Gemini Pro" count as two checkers. Live
  annotations read bare `Claude` (43), `GPT` (52), `Gemini` (13). If
  Opus and Fable both answer a row, two legs arrive and V2 grants
  cross-checked on what may be one family's shared misreading. Version
  in the FILENAME and bare identity in the annotation keeps two Claude
  legs scoring as ONE identity -- conservative and correct -- while the
  file still records which two Claudes. No migration of 134
  annotations.
- **Two supporting pieces, unbuilt.** The request prints the EXPECTED
  return filename in its header, since the builder cannot name a return
  and the request is the only place the convention reaches the reader.
  And the checker REPORTS on names rather than refusing them: 34
  historical worksheets predate this, and a checker that refuses the
  corpus it exists to check is useless.
**Note:** RICE is Claude's proposal, unratified.
**Gap:** unbuilt. Blocks nothing, but a return filed before it lands
will need renaming -- and a rename breaks every `# Resolved:` leg
pointing at it, so name the pilot's return by hand at dispatch time.
**Ref:** L-200 (the leg that cites the filename); L-186; L-192.

#### [L-207] The citation prompt -- the checker asks the fuzzy question
<!-- L:207 status:OPEN upd:2026-08-18 section:A flag: rice:3/3/85/1 -->
- **The gap, measured 2026-08-18.** The citation half of a return has
  no route out of the file. `ROLE_SOURCE` -- the responder's own cited
  source -- is mapped in the header registry and read NOWHERE.
  `ROLE_CITATION_VERDICT` is read in exactly two places: an unreachable
  third branch of `read_verdict` (unreachable for JSON, which always
  synthesizes a value column) and L-200's linkage check, which only
  fires on a row a `# Resolved:` leg already names. So both halves of
  the citation question are parsed into the Table and stop there.
- **This is NOT a defect in the split.** The 2026-08-17 ruling assigned
  the citation comparison to a reader BECAUSE it is a language
  judgement rather than a numerical one, and the mechanical checker
  correctly stays at numbers. What was never built is the leg that
  carries the material to that reader.
- **Tony's design, 2026-08-18.** The checker does two things in one
  run: (1) the numerical check exactly as now, and (2) writes a
  CONSISTENT JSON prompt asking Claude the citation question.
- **Why a prompt rather than a worklist.** A worklist is data; a prompt
  is a request, and a request inherits the discipline the builder
  already has -- keyed rows, a hash over the do-not-edit fields, a SHA
  anchor, and generation rather than typing. Same SHA plus same returns
  gives the same prompt, which is what makes a citation review EVIDENCE
  rather than an opinion, re-runnable against another model and
  comparable across sessions. Same rule as L-201: a selection is code,
  not typing.
- **It respects the existing boundary.** The checker stays read-only
  over the corpus and writes reports; it already writes
  `data/worksheet_routed.json`. No writer moves behind that line.
- **Each row carries:** key, claim, code value, the code's current
  `# Source:` authority, the context legs (`# See:`, `# Derived:`,
  `# Note:`) so a misplaced authority is distinguishable from an absent
  one, the responder's cited source, the worksheet and checker it came
  from, and a row hash.
- **Ruled 2026-08-18: the prompt SHOWS the responder's citation
  verdict.** It makes the review a comparison rather than a
  re-derivation, and disagreement between the responder's verdict and
  the reviewer's is the lazy-responder canary -- measured per row,
  with no separate mechanism invented for it. The cost is stated
  rather than hidden: seeing a verdict before judging anchors, and the
  only mitigations are field order and an instruction saying the review
  is independent and that disagreement is a finding, not an error.
  Structural blindness would be stronger and was traded away
  deliberately.
- **On complexity.** This passes the extend-don't-add test: it is an
  EMITTER over the Table the checker already builds, reusing
  `row_hash` and the report writer. No new verdict semantics, no new
  layer, no second parse.
- **It is not strictly blocking for the pilot.** Twenty-three rows can
  be read by hand. It is blocking for the pilot to produce evidence of
  the kind this project trades in, and it does not scale to 110.
**Note:** RICE is Claude's proposal, unratified.
**Gap:** unbuilt. Full detail in
`documentation/DESIGN_20260818_citation_prompt.md`.
**Ref:** L-192 (the checker); L-200 (the leg that records what a
verdict caused); L-202 (the JSON schema it reads).

## PENDING ACTION (Tony-side)"""


# ---- L-199: the handle this restructure belongs to -------------------

L199_TAIL_OLD = """**Gap:** all three parts unbuilt. Part 2 must not run before the
appendix repair in the bullet above.
**Ref:** v3.37 (the reversed all-lessons cut, and why an archive has no
trigger); v3.30 (the two-layer split that moved procedure into skills);
`documentation/LESSONS_ARCHIVE.md`; the Protocol Version History
appendix at the end of this ledger."""

L199_TAIL_NEW = """- **Tony's ruling, 2026-08-18, and it changes part 2.** The store for
  the version history is NOT this ledger's appendix. The appendix moves
  out into `documentation/PROJECT_INSTRUCTIONS_HISTORY.md`, which is
  `LESSONS_ARCHIVE.md` renamed and now carrying two records: the
  version history as PART 1, the v3.37 lessons record verbatim as
  PART 2. Both are kept -- the lessons record is not displaced by the
  history arriving beside it. The ledger keeps a pointer.
- **As built, 2026-08-18** (`patch_L199_1`). Parts 2 and 3 of the
  proposal landed, part 1 did not.
  - The appendix repair the bullet above insisted on is satisfied
    WITHOUT copying anything: v3.39 and v3.40 are two of the three
    entries that STAY resident, so the trim never reaches them.
    v3.34-v3.38 come out of the protocol and are not copied, because
    they are already inside the appendix that became PART 1. Every
    entry lives in exactly one place.
  - The rule that keeps it that way is now stated in the protocol:
    three most recent resident, and a fourth pushes the oldest down.
    That is the stated cap part 1 asked for, arriving as one line
    rather than as a sizing section.
  - Part 3 landed too: Part 5 names the file, which is the only real
    defect the archive had.
  - The header gained an anchor and a corrected date. The repo copy
    read August 16 and the copy installed in the Claude UI read
    August 17 under the SAME version number -- two stores of one
    document, one of them hand-edited. v3.41 supersedes both.
- **Remaining, and it is part 1 alone.** A short sizing section
  carrying the trigger test and the gates-fraction measure. The cap it
  was to contain now exists; what is still missing is the reasoning
  that governs the next thing wanting to move in.
**Gap:** part 1 unbuilt. Parts 2 and 3 landed 2026-08-18.
**Ref:** v3.37 (the reversed all-lessons cut, and why an archive has no
trigger); v3.30 (the two-layer split that moved procedure into skills);
`documentation/PROJECT_INSTRUCTIONS_HISTORY.md`;
`documentation/patch_L199_1`."""


L199_REF_OLD = """3. One line in Part 5 naming `documentation/LESSONS_ARCHIVE.md`. The"""
L199_REF_NEW = """3. One line in Part 5 naming the archive file (now
   `documentation/PROJECT_INSTRUCTIONS_HISTORY.md`). The"""


# ---- the appendix leaves the ledger ----------------------------------

APPENDIX_HEAD = '## Appendix: Protocol Version History'

APPENDIX_POINTER = """## Appendix: Protocol Version History -- MOVED

Moved 2026-08-18 to `documentation/PROJECT_INSTRUCTIONS_HISTORY.md`,
PART 1, per Tony's ruling under L-199. That file carries the full
history from v1.0 and, as PART 2, the twenty-seven lessons removed from
the protocol at v3.37.

The protocol document keeps the three most recent entries resident; a
fourth pushes the oldest down into PART 1. Every entry lives in exactly
one place, so there is nothing here to keep in step.
"""


# ---- the protocol ----------------------------------------------------

HEADER_OLD = """PROJECT INSTRUCTIONS
Tony Quintanilla, PE | Claude | v3.40 | August 16, 2026"""

HEADER_NEW = """PROJECT INSTRUCTIONS
Tony Quintanilla, PE | Claude | v3.41 | August 18, 2026

Cut from b65ac115 at https://github.com/tonylquintanilla/palomas_orrery
(branch main). Gallery repo: tonyquintanilla/tonyquintanilla.github.io.
Full version history and the v3.37 lessons record:
documentation/PROJECT_INSTRUCTIONS_HISTORY.md

The anchor names the state this document was CUT FROM, not a promise
that the repo still sits there. It is here because this file's own
CRITICAL gate requires it of any document leaving a live session, and
a relay partner reading this has no other way to know what it
describes."""


VERSION_INTRO_OLD = """Version History
The full version history (v1.0 through current) lives in
LEDGER_CONSOLIDATED.md, Protocol Version History appendix -- the ledger is
the change log for the protocol and the skills layer. Recent entries:"""

VERSION_INTRO_NEW = """Version History
The THREE most recent entries live here. Everything older lives in
documentation/PROJECT_INSTRUCTIONS_HISTORY.md, PART 1 -- which also
carries, as PART 2, the twenty-seven lessons removed at v3.37.

The rule is mechanical, and it is what stops this section growing back:
when a fourth entry is added, the oldest of the four moves down into
that file. An entry lives in exactly one place, never both."""


LESSONS_POINTER_OLD = """The PROCESS and PHILOSOPHICAL lessons below exist in only one place.
Twenty-seven others were removed on August 11, 2026, each a restatement of a
rule already stated where it fires; documentation/LESSONS_ARCHIVE.md lists
them against the place each still lives. That file is a record, not a store."""

LESSONS_POINTER_NEW = """The PROCESS and PHILOSOPHICAL lessons below exist in only one place.
Twenty-seven others were removed on August 11, 2026, each a restatement of a
rule already stated where it fires;
documentation/PROJECT_INSTRUCTIONS_HISTORY.md, PART 2, lists them against
the place each still lives. That file is a record, not a store."""


V341_ANCHOR = """v3.39 (August 12, 2026): One change. \"A Check That Cannot Fail Is Not"""

V341_ENTRY = """v3.41 (August 18, 2026): Records restructure and a skill bump.
No rule changed. (1) The version history left this document: v1.0-v3.38
now live in documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1, the
file that was LESSONS_ARCHIVE.md and still carries the v3.37 lessons
record verbatim as PART 2. The ledger's appendix is replaced by a
pointer. Three entries stay resident and a fourth pushes the oldest
down, which is the cap L-199 asked for; its part 1, a sizing section,
is still unbuilt. (2) The header gained an anchor and lost a
contradiction -- the repo copy read August 16 and the copy installed in
the Claude UI read August 17 under the SAME version, two stores with
nothing watching them the way Stale Skill = Stop watches the skills.
(3) provenance-discipline 2.3 -> 2.4 (L-203, L-204): the visibility
convention got a home, and the annotation grammar now accepts a .jsonl
or .json worksheet reference, because a returned verdict could be
checked and routed and then refused when written back into the code.
The reinstall cannot be verified from inside the session that makes it,
so the NEXT session confirms its loaded copy reads 2.4 before doing
provenance work.

v3.39 (August 12, 2026): One change. \"A Check That Cannot Fail Is Not"""


V334_CUT_START = """v3.34 (August 5, 2026): Two amendments, both from the Fable skills-layer review."""
V334_CUT_END = """v3.41 (August 18, 2026): Records restructure and a skill bump."""


LEDGER_EDITS = [
    (L200_STATUS_OLD, L200_STATUS_NEW),
    (L200_TAIL_OLD, L200_TAIL_NEW),
    (L201_STATUS_OLD, L201_STATUS_NEW),
    (L201_TAIL_OLD, L201_TAIL_NEW),
    (L202_STATUS_OLD, L202_STATUS_NEW),
    (L202_TAIL_OLD, L202_TAIL_NEW),
    (L199_REF_OLD, L199_REF_NEW),
    (L199_TAIL_OLD, L199_TAIL_NEW),
    (NEW_BLOCKS_ANCHOR, NEW_BLOCKS),
]

PROTOCOL_EDITS = [
    (HEADER_OLD, HEADER_NEW),
    (VERSION_INTRO_OLD, VERSION_INTRO_NEW),
    (LESSONS_POINTER_OLD, LESSONS_POINTER_NEW),
    (V341_ANCHOR, V341_ENTRY),
]


HISTORY_HEADER = """PROJECT INSTRUCTIONS -- HISTORY

Cut from %s at %s (branch main).
Assembled 2026-08-18 under L-199, from two records that were previously
in two different files.

THIS FILE IS A RECORD, NOT A STORE OF RULES. Nothing in it fires. No
session needs to read it to work correctly; it exists so that a
question about how the protocol got here can be answered by reading
rather than from memory.

  PART 1  The protocol's version history, v1.0 through v3.38. Moved
          here from the Appendix at the end of LEDGER_CONSOLIDATED.md,
          which now holds a pointer. The protocol document keeps the
          THREE most recent entries resident and a fourth pushes the
          oldest down into PART 1, so every entry lives in exactly one
          place and there is nothing here to keep in step.

  PART 2  The twenty-seven lessons removed from the protocol at v3.37,
          kept verbatim, each naming where the same instruction is
          still stated. This file used to be called LESSONS_ARCHIVE.md
          and was exactly this record; the rename adds the history
          beside it and takes nothing away.

Why they sit together. Both answer the same kind of question -- what
the protocol used to say and why it stopped saying it -- and neither
has a trigger, which is precisely why neither belongs in the resident
document. Keeping them in one file makes that shared property visible
instead of leaving two triggerless records in two places.

================================================================
PART 1 -- PROTOCOL VERSION HISTORY (v1.0 through v3.38)
================================================================

""" % (ANCHOR_SHA, REPO_URL)

HISTORY_PART2 = """

================================================================
PART 2 -- LESSONS REMOVED FROM THE PROTOCOL AT v3.37
================================================================

"""


# ============================================================
# HARNESS
# ============================================================

def fingerprint(data):
    """Content fingerprint: line endings normalized before hashing."""
    return hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()


def non_ascii(text):
    return [c for c in text if ord(c) > 127]


def apply_edits(name, text, edits):
    """Every anchor must match exactly once, in an accumulating buffer.

    Edits apply in sequence to ONE buffer, not each to the original, so
    an anchor quoting text an earlier edit already rewrote will find
    nothing. That is a real failure and it aborts.
    """
    for old, new in edits:
        if non_ascii(new):
            raise SystemExit('ERROR: %s -- edit would insert non-ASCII. '
                             'Nothing written.' % name)
        count = text.count(old)
        if count != 1:
            print('ANCHOR FAIL: %s -- expected 1 match, found %d for:'
                  % (name, count))
            print('   %s' % old.splitlines()[0][:70])
            raise SystemExit('Nothing written.')
        text = text.replace(old, new)
    return text


def cut_span(name, text, start_marker, end_marker, replacement=''):
    """Remove start_marker .. end_marker (end kept), both unique.

    Used where a literal anchor would be forty lines long. The two
    assertions -- each marker unique, start before end -- make this
    exactly as checkable as a literal, and a good deal easier to read.
    """
    if text.count(start_marker) != 1:
        print('SPAN FAIL: %s -- start marker matched %d times:'
              % (name, text.count(start_marker)))
        print('   %s' % start_marker.splitlines()[0][:70])
        raise SystemExit('Nothing written.')
    if end_marker is not None and text.count(end_marker) != 1:
        print('SPAN FAIL: %s -- end marker matched %d times:'
              % (name, text.count(end_marker)))
        print('   %s' % end_marker.splitlines()[0][:70])
        raise SystemExit('Nothing written.')
    start = text.index(start_marker)
    end = len(text) if end_marker is None else text.index(end_marker)
    if end < start:
        print('SPAN FAIL: %s -- end marker precedes start marker.' % name)
        raise SystemExit('Nothing written.')
    removed = text[start:end]
    return text[:start] + replacement + text[end:], removed


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    os.chdir(here)

    # ---- gate: every file present and unmoved ------------------------
    raw = {}
    for name, want in FINGERPRINTS.items():
        if not os.path.isfile(name):
            print('ERROR: %s not found. Run this from the repo root.' % name)
            return 1
        with open(name, 'rb') as handle:
            data = handle.read()
        seen = fingerprint(data)
        if seen != want:
            print('ERROR: %s has moved. Expected %s, found %s.'
                  % (name, want, seen))
            print('       Nothing written. Built against %s.' % ANCHOR_SHA)
            print('       If you already ran '
                  'patch_L204_2_ledger_reconcile.py, say so -- this needs')
            print('       re-cutting against that tree.')
            return 1
        raw[name] = data

    if os.path.exists(NEW_HISTORY):
        print('ERROR: %s already exists. Nothing written.' % NEW_HISTORY)
        return 1

    crlf = {name: data.count(b'\r\n') > 0 for name, data in raw.items()}
    text = {name: data.decode('utf-8').replace('\r\n', '\n')
            for name, data in raw.items()}

    # ---- the ledger: blocks, then the appendix leaves ----------------
    ledger = apply_edits('LEDGER_CONSOLIDATED.md',
                         text['LEDGER_CONSOLIDATED.md'], LEDGER_EDITS)
    ledger, appendix = cut_span('LEDGER_CONSOLIDATED.md', ledger,
                                APPENDIX_HEAD, None, APPENDIX_POINTER)

    # Drop the appendix's own heading; PART 1 supplies the heading now.
    if not appendix.startswith(APPENDIX_HEAD):
        print('SPAN FAIL: the extracted appendix does not begin with its '
              'own heading. Nothing written.')
        return 1
    appendix_body = appendix[len(APPENDIX_HEAD):].lstrip('\n')
    if 'v3.38 (August 11, 2026)' not in appendix_body:
        print('ERROR: the extracted appendix does not contain v3.38, so it '
              'is not the history this patch expects. Nothing written.')
        return 1
    if 'v3.39' in appendix_body or 'v3.40 (' in appendix_body:
        print('ERROR: the appendix already carries v3.39/v3.40; this patch '
              'assumes it does not. Nothing written.')
        return 1

    # ---- the protocol: header, pointers, new entry, then the trim ----
    protocol = apply_edits('PROJECT_INSTRUCTIONS.md',
                           text['PROJECT_INSTRUCTIONS.md'], PROTOCOL_EDITS)
    protocol, dropped = cut_span('PROJECT_INSTRUCTIONS.md', protocol,
                                 V334_CUT_START, V334_CUT_END)
    for tag in ('v3.34', 'v3.35', 'v3.36', 'v3.37', 'v3.38'):
        if tag not in dropped:
            print('ERROR: the trim did not remove %s. Nothing written.' % tag)
            return 1
        if tag + ' (' in protocol:
            print('ERROR: %s survives in the protocol after the trim. '
                  'Nothing written.' % tag)
            return 1
    for tag in ('v3.39 (', 'v3.40 (', 'v3.41 ('):
        if tag not in protocol:
            print('ERROR: %s is missing from the protocol after the trim. '
                  'Nothing written.' % tag)
            return 1
        if tag not in ('v3.41 (',) and tag.rstrip(' (') in appendix_body:
            print('ERROR: %s is in BOTH stores. Nothing written.' % tag)
            return 1

    # ---- the history file --------------------------------------------
    lessons = text[OLD_ARCHIVE]
    if non_ascii(HISTORY_HEADER) or non_ascii(HISTORY_PART2):
        print('ERROR: composed header is not ASCII. Nothing written.')
        return 1
    history = HISTORY_HEADER + appendix_body.rstrip('\n') \
        + HISTORY_PART2 + lessons.lstrip('\n')

    # ---- write, only now that every check has passed ------------------
    def out(name, body):
        data = body.encode('utf-8')
        if crlf.get(name):
            data = data.replace(b'\n', b'\r\n')
        with open(name, 'wb') as handle:
            handle.write(data)

    out('LEDGER_CONSOLIDATED.md', ledger)
    print('ok  LEDGER_CONSOLIDATED.md (%d edits, appendix moved out)'
          % len(LEDGER_EDITS))

    out('PROJECT_INSTRUCTIONS.md', protocol)
    print('ok  PROJECT_INSTRUCTIONS.md (%d edits, v3.34-v3.38 trimmed)'
          % len(PROTOCOL_EDITS))

    crlf[NEW_HISTORY] = crlf.get(OLD_ARCHIVE, False)
    out(NEW_HISTORY, history)
    os.remove(OLD_ARCHIVE)
    print('ok  %s -> %s' % (OLD_ARCHIVE, NEW_HISTORY))

    print('patch applied')
    print('')
    print('  protocol   %d lines (was %d)'
          % (protocol.count('\n') + 1,
             text['PROJECT_INSTRUCTIONS.md'].count('\n') + 1))
    print('  history    %d lines' % (history.count('\n') + 1))
    print('  ledger     %d lines (was %d)'
          % (ledger.count('\n') + 1,
             text['LEDGER_CONSOLIDATED.md'].count('\n') + 1))
    print('')
    print('NOW RUN: python ledger_index.py')
    print('  It rebuilds the index table and moves the six newly-DONE')
    print('  blocks into their closed buckets. Skipping it leaves the')
    print('  table advertising three OPEN items that are not.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
