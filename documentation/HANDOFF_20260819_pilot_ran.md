# HANDOFF 2026-08-19 -- the pilot ran

**Built on `9ffb9b403a7d62090b30a9acf9adbc6180a6baec` at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Gallery at `ff18d3e6fa31f70a8f525df471e751d046cf14fa` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.**

Two patches were delivered after that anchor was read and are expected
to land in the commit that carries this file:
`patch_L209_1_pilot_findings.py` (three ledger items) and
`patch_L209_2_plan_docs_post_pilot.py` (the three planning documents).
**Confirm HEAD, then confirm those two ran** -- L-209, L-210 and L-211
should be in the ledger index table, and
`documentation/CRITICAL_PATH_SUMMARY.md` should open with August 19.
If HEAD is not what this file expects, reconcile before building.

Readable cold. Nothing below assumes the reader was present.

---

## What the next session does

**Review the returned worksheets, reconcile the differences, and
decide what the gaps mean.** Tony's framing, and it is per-row
judgment work rather than a build.

The material is seven JSON Lines files in
`documentation/worksheets/`. Three are the legs of record, dispatched
at `eae95f5a` on 2026-08-18 to three models in fresh chats:

    worksheet_gemini_constants_new_20260818.jsonl
    worksheet_gpt_constants_new_20260818.jsonl
    worksheet_claude_constants_new_20260818.jsonl

Three more are Gemini runs in continuation threads, kept as
context-sensitivity evidence and NOT legs:
`..._from0415`, `..._from0602`, `..._from0802`. A fourth Gemini thread
was sought and not found, which is recorded rather than rounded away.

Read `documentation/PILOT_CONVERGENCE_20260819.md` FIRST. It is the
analysis of all of this, written while the returns were fresh, and it
is organized so a cold reader can work from it: headline scored, trap
rows, convergent findings, divergences, what the pilot measured about
the loop, and what it does not decide.

**The reconciliation is 13 rows.** Ten of the 23 came back clean on
both axes from all three legs and need nothing. The other 13 each need
a decision of one of four kinds: change the value, swap the citation,
annotate as-is because the responder is wrong, or record the row as
unresolvable. `PILOT_CONVERGENCE_20260819.md` Part 6 lists the five
carrying a recommendation strong enough to act on, in priority order.

**Nothing has been written back into the code yet.** No
`# Cross-checked:` annotation cites any of these worksheets. The pilot
was scoped to end at re-verification in code, so on a strict reading
it is not finished; whether to call it finished is one of the open
rulings below.

---

## Key documents, and what each is for

Read in this order if starting cold.

| Document | What it answers |
|---|---|
| `PROJECT_INSTRUCTIONS` v3.41 (resident) | How this project works. The modes, the CRITICAL gates, the skill manifest. |
| `documentation/PILOT_CONVERGENCE_20260819.md` | What the pilot found. **Start here for the next session's work.** |
| `documentation/PILOT_EXPECTED_DISPOSITIONS_20260817.md` | What was predicted before dispatch. Read alongside the above; the pairing is what makes either one evidence. |
| `documentation/CRITICAL_PATH_SUMMARY.md` | How far to the end. Readable. |
| `MASTER_PLAN_INTERACTIVE_GALLERY.md` Section 5a | The shape of the work. Reference version; 5a wins if sections disagree. |
| `MASTER_PLAN_INTERACTIVE_GALLERY_SUMMARY.md` | What is tracked right now. |
| `LEDGER_CONSOLIDATED.md` | In-flight record. L-209, L-210, L-211 are this session's; L-206 and L-195 are the live neighbours. |
| `documentation/DESIGN_20260818_unknown_verdict.md` | The UNKNOWN design and its pre-registered trigger, which fired. |
| `documentation/DESIGN_20260818_citation_prompt.md` | The L-207 design, now built. |
| `documentation/worksheets/PROMPT_dispatch_jsonl_request.md` | The reusable dispatch prompt. Use it verbatim for any future dispatch. |
| `documentation/patch_L207_1_citation_prompt.py` | The as-run build of L-207, archived. |

Skills that fire on this work: `provenance-discipline` (2.5),
`safe-file-editing` (1.4), `ledger-and-session-records` (1.6). Compare
each against the manifest at load; the Stale Skill = Stop gate is
CRITICAL and one of the obligations below depends on it.

---

## What happened this session

**L-207 built and closed.** The checker now emits
`documentation/prompts/citation_review.jsonl` on every run: 53 rows,
one per key, carrying what the code cites, what each responder cited,
and what each responder concluded, with empty answer fields for a
reviewer. The leg parser moved from the request builder into
`worksheet_keys.py` so one parser serves both readers, with an
identity pin in the builder's tests that goes red if it is ever
forked. Proved behaviour-neutral: the same 23-row request builds
byte-identical before and after the move.

**The pilot dispatched and returned.** 23 rows, three models, 69
answered rows. Across all of them: zero unparseable lines, zero
missing or modified row hashes, zero duplicate keys, zero empty answer
fields, zero tokens outside the vocabulary. The JSON format needed no
fallback and the `.md` fallback was never used.

**The prediction held.** 13 clears predicted; 17, 10 and 11 measured.
All three trap rows failed to spring, which is the pilot's primary
result: the artifact conveys what it was built to convey.

**The UNKNOWN trigger fired**, seven rows against a pre-registered
threshold of two -- and the returns named the pattern the design note
had missed. Every instance is a print book no responder can open:
Carroll & Ostlie, Golub & Pasachoff, Murray & Dermott. The missing
verdict is not scattered; it concentrates wherever the authority is a
book. That is L-211, and the finding underneath it is that three
constants in this slice need a human with library access rather than a
better token.

**`provenance-discipline` went 2.4 to 2.5**, adding Extend a Boundary
Before Adding a Path -- the rule an external review proposed on
2026-08-18 and Tony adopted. L-207 was the first item checked against
it rather than assumed to pass.

---

## Carried obligations

**1. Confirm the loaded `provenance-discipline` reads 2.5 before doing
provenance work.** [CRITICAL, Stale Skill = Stop.] This session loaded
2.4, bumped the skill to 2.5, and cannot verify its own reinstall from
inside itself. A separate fresh chat reported loading 2.5 on
2026-08-18, which is the first independent confirmation, but the
session that does provenance work must check its own loaded copy.

**2. The dispatch-hygiene rule is not in any skill yet.** It belongs
in `provenance-discipline`'s Batch Worksheet Workflow, which would be
2.6. It was deliberately NOT bumped this session, to avoid stacking a
second unverifiable reinstall on top of the first. Discharge
obligation 1 first, then add it. The rule: **a dispatch goes to a new
chat OUTSIDE any project.** A new chat inside the Paloma's Orrery
project inherits memory naming the pilot's trap rows, which turns
row-checking into trap-hunting and makes the leg unreproducible by
anyone lacking that memory store. It currently lives only in
`PROMPT_dispatch_jsonl_request.md`.

**3. Archive the two patch scripts** to `documentation/` once run,
per the naming-and-archiving convention.

**4. The dispatch prompt exists in two directories** --
`documentation/` and `documentation/worksheets/`. Keep the
`worksheets/` copy, which the checker classifies as a prompt file, and
delete the other. Two stores of one document is the drift pattern this
project has a rule about.

---

## Open rulings carried forward

**Whether a VISUALIZATION BOUNDARY is verdictable at all.** All three
legs declined to confirm `INNER_CORONA_RADII` and split on what kind
of thing it is: GPT refuses the value at 1.5 R_sun per the 2023
middle-corona consensus, Claude calls it a defensible drawing
convention that nests with the 6 R_sun streamer shell, Gemini declines
to answer. This is the artifact-bounds question arriving as a
worksheet row rather than as an argument. Tony's call.

**Whether Gemini stays a leg of record.** It cleared 17 of 23 with the
shortest notes in the batch and confirmed both rows the other two
refused. That is the profile
`PILOT_EXPECTED_DISPOSITIONS_20260817.md` warns about: agreement
rather than checking.

**Whether the pilot counts as finished** with nothing yet annotated
into the code.

**Whether the return filenames should be renamed.** See the errors
section -- this one has a deadline, because a rename after annotation
breaks every `# Resolved:` leg pointing at the file.

---

## Errors and process failures, recorded

Both are Claude's, and they stay in the record rather than being
quietly overwritten.

**1. The filenames diverge from the convention L-206 already ruled.**
L-206 specifies `worksheet_<model>_<batch>_<YYYYMMDD>.jsonl` with the
model field carrying the VERSION, its own example being
`worksheet_claude-opus-5_pilot_constants_new_20260818.jsonl`. What was
recommended and used is `worksheet_gemini_constants_new_20260818.jsonl`
-- bare model, no version, and the selection where L-206 wrote batch.
Claude proposed the name from first principles without checking the
ledger item that had already ruled it, which is the failure the
ledger exists to prevent. Nothing is broken: no annotation cites these
files yet, so a rename is currently free. It stops being free the
moment the first `# Cross-checked:` leg names one. **Decide before
annotating.** Either rename the seven files to the L-206 shape, or
amend L-206 to what was used and say why.

**2. The encoding gate was applied backwards, and Tony caught it.**
Asked to patch the ledger, Claude found 123 pre-existing non-ASCII
characters, scoped the gate to inserted text only, and reported them
as untouched. The `safe-file-editing` skill's Fix In Passing, Report
It says the opposite where three conditions hold -- convention already
ruled, file already fingerprinted and being edited, substitution
mechanical -- and all three held. Tony's correction: "I thought that
we decided to fix ascii errors and report in the skill instead of not
fix and report?" The patch was rewritten to sweep and report both
halves. The rule was in the loaded skill and was not applied.

**Not an error, recorded because it shaped the day.** Two Claude
dispatches returned nothing during an Anthropic platform incident --
degraded performance across multiple models, open from 16:20 UTC on
2026-08-18. The second attempt reused the crashed thread, which was
the wrong move for an unrelated reason. A report describing three
clean dispatches would misstate a day that took five attempts across
two providers plus an in-project refusal.

---

## What NOT to do

**Do not build anything in the provenance system before the
reconciliation.** L-211 is approved and specified, and it is still
downstream of this: the rule adopted this week says the next feature
should be one a run exposed. A run just exposed thirteen rows needing
judgment. Judgment first.

**Do not treat any responder claim as a verdict.** Every finding in
the convergence report is a claim by a model. Several are sharply
argued and at least two look right, but the value in the code changes
when Tony decides it changes.

**Do not re-litigate the four UNKNOWN rulings.** They are settled in
`DESIGN_20260818_unknown_verdict.md` and restated in L-211.

---

*Written August 19, 2026 with Anthropic's Claude Opus 5. Built on
`9ffb9b403a7d62090b30a9acf9adbc6180a6baec`; gallery at
`ff18d3e6fa31f70a8f525df471e751d046cf14fa`.*
