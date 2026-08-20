# HANDOFF 2026-08-19 (evening) -- L-214 designed, not built

**Built on `5859e15097b92bbb5ebd9ebb7a8fe78fdea85aac` at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Gallery unchanged at `8a4aa41268ed9efadea9ad6b40fabe880ce8bef8` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.**

One patch was delivered after that anchor was read and is expected to
land in the commit carrying this file:
`patch_L214_2_rationale_and_L219.py`. **Confirm HEAD, then confirm it
ran** -- L-219 should be in the ledger index table and L-214's Gap
should mention the `legs_of` docstring. If HEAD is not what this file
expects, reconcile before building.

Readable cold. Nothing below assumes the reader was present.

---

## Carried obligations

**1. Confirm the loaded `gallery-cache-builder` reads 1.4 before doing
builder work.** [CRITICAL, Stale Skill = Stop.] This session bumped it
1.3 -> 1.4 and Tony reinstalled it to the account profile, but a
mid-session reinstall cannot be verified from inside the session that
makes it. The manifest in `PROJECT_INSTRUCTIONS.md` was regenerated and
says 1.4, and the repo copy at HEAD says 1.4. Check your own loaded copy
against the manifest at load time.

**2. Archive `patch_L214_2_rationale_and_L219.py` to `documentation/`**
once run. The maintenance run does this automatically; confirm rather
than assume.

**3. Do not run the gallery builder with `--commit` while L-216 is
open.** Unchanged from the previous handoff. The discard-and-re-run
recovery depends on nothing reaching the remote until Tony commits by
hand. That rule now lives in `gallery-cache-builder` 1.4.

---

## What the next session does

**Build L-214.** The design is settled and nothing is built. That is the
whole of the next session's scheduled work, and it is bigger than the
item's title suggests -- Tony ruled that the registry work stays inside
L-214 rather than splitting out.

Read L-214 in the ledger first; it now carries the full design. Then
`documentation/L214_REVIEW_RECONCILIATION_20260819.md` for why the
design is what it is, and `documentation/L214_MEASUREMENT_20260819.md`
for the numbers under it.

The build, in order, and the ORDER IS A CONSTRAINT not a preference:

1. Separate generic label DETECTION from policy. `LEG_RE` is currently
   built FROM the policy sets, which is why "not in our vocabulary" and
   "not a labelled line" are the same condition.
2. One home for the vocabulary. The scanner and the checker import it
   rather than compiling their own patterns.
3. `Note` admitted to CONTEXT.
4. `# Review-note:` added as withheld free-form.
5. The moon line rehomed to `# Review-note:` -- BEFORE or in the same
   transaction as step 7. Sequenced later there is a window where it
   carries valid `Note+:` markers and travels cleanly on the next
   moon-row dispatch.
6. The four odd labels fixed at source.
7. The marker sweep: 12 lines at 8 sites, not 10 at 6.

**Then the reconciliation, which has not moved in two sessions.** Four
of the five ranked rows are still open: `STREAMER_BELT_RADII`,
`EARTH_EQUATORIAL_RADIUS_KM`, `HAUMEA_RADIUS_KM`, `BENNU_RADIUS_KM`.
Read `documentation/PILOT_CONVERGENCE_20260819.md` Part 6 first.

---

## What happened this session

**L-214 went from three undecided options to a settled design, via a
Mode 7 review.** Claude proposed a six-part structure. Two review legs
-- Claude Fable 5 and GPT -- read the same two documents, and both
disagreed with the proposal in the same place for the same reason.

**The root cause was one layer below where the proposal was working.**
Both legs: the leg regex is built from the policy sets, so a label
nobody has classified and a label deliberately withheld exit through
the identical branch. Detect any `# Label:` line generically first, then
classify. The invariant both proposed: every syntactically labelled line
attached to a claim finishes the builder in ONE NAMED DISPOSITION.

**Transport and grammar are two axes, not one list.** GPT's framing;
Fable reached the same two-by-two and called the empty cell a fourth
state. Travels-or-withheld crossed with validated-or-free. The empty
cell is withheld-and-free-form, which is what the moon line needed.

**Tony's rulings.** The free-form record label is `# Review-note:`.
Unclassified text is WITHHELD from the request and surfaced to Tony and
Claude before dispatch -- correcting Claude's earlier reading, which had
routed it to the outside responder. The registry work stays in L-214.

**Why report rather than reject, in Tony's own argument.** A reported
label can then be READ and decided about -- aliased, or unified under
one label the way `Note` was. A rejected label forecloses that: the run
stops and the decision never gets made. The reading step is where the
judgment lives.

**The `Corrected` drift is that argument's worked example.** Corpus-wide
the label appears in four spellings with no validator behind any of
them: `# Corrected:` (7), `# Corrected 2026-08-02:` (5), `# Corrected
2026-08-05:` (1), `# Corrected in Phase B:` (1). Three of four would
classify as unknown. It drifted in the two record labels that have no
compiled pattern -- `Removed` and `Corrected` -- which is to say, in the
two nothing was watching.

**The record set is two enforced labels plus two conventions, not
four.** `CROSS_CHECK_LINE_RE` and `RESOLVED_LINE_RE` are compiled in
`provenance_scanner.py`, case-INsensitive. `worksheet_keys.py` names
neither and its `LEG_RE` is case-SENSITIVE. Claude's proposed
`RECORD_LEGS` of four was inventing two of them. Deciding the form for
`Removed` and `Corrected` is part of the build, not a precondition.

**L-217 opened, and it is a defect in this session's own work.** The
review prompt asked each leg to answer Part A before reading Part B, to
prevent anchoring. Fable's disclosure: the prompt arrives as one
document in one context, so a model cannot comply, and nothing in any
answer distinguishes a reviewer who complied from one who could not.
GPT's A3 corroborates -- it opens "my prediction before consulting the
measured result" and then states the measured result to the digit. A
check that cannot fail, in the dispatch layer, authored this session.

**L-218 opened.** 22 `# Cross-checked:` lines attach to no unit. The
measurement announced the number and parked it; Fable called that a
finding living in a footnote.

**L-219 opened.** The patch-script naming convention cannot express a
cross-handle run order -- carried from the previous handoff's error log,
where it was named as a gap and noted as having no item.

**`gallery-cache-builder` 1.3 -> 1.4.** The discard-and-re-run recovery
rule from L-216, with its three safety conditions.

---

## Key documents

| Document | What it answers |
|---|---|
| `PROJECT_INSTRUCTIONS` v3.41 (resident) | How this project works. |
| `LEDGER_CONSOLIDATED.md` L-214 | The settled design. Start here. |
| `documentation/L214_REVIEW_RECONCILIATION_20260819.md` | Why the design is what it is. |
| `documentation/L214_MEASUREMENT_20260819.md` | The 12 dropped lines and the marker-sweep counts. |
| `documentation/REVIEW_PROMPT_L214_20260819.md` | The prompt that carried the L-217 defect. |
| `documentation/PILOT_CONVERGENCE_20260819.md` | The reconciliation queue. |
| `documentation/patch_L214_1_design_settled_and_two_items.py` | As-run. |
| `documentation/patch_L216_2_cache_builder_skill_1_4.py` | As-run. |

Skills that fire on this work: `provenance-discipline` (2.5),
`safe-file-editing` (1.4), `ledger-and-session-records` (1.7),
`orrery-coding-conventions` (1.4), `gallery-cache-builder` (1.4).
Compare each against the manifest at load.

---

## Errors and process failures, recorded

**1. Claude collided with a live project term.** It used "unknown" to
mean an unrecognised comment label. UNKNOWN is L-211, the verdict token
for "checked, could not determine." Tony's response was that the issues
were too unclear to judge.

**2. Claude asked Tony to make line-level technical judgments three
times before being told to stop.** Tony: "what i am looking for are
structural solutions rather than parsing and judging technical language,
which is not my expertise -- that is what we have the worksheets for."
Every ask before that point had been shaped as a choice between
implementation details.

**3. Claude recommended moving the moon line under `# Resolved:` and
then found, by reading, that `# Resolved:` carries a strict linkage
grammar a free-form note fails.** The defect was disclosed to the
reviewers rather than quietly patched, which is why the two-axis
structure surfaced at all.

**4. Claude's marker sweep undercounted its own steps.** Ten lines, when
relabelling the odd spellings brings the count to twelve. Fable
predicted it; re-running the project's own tooling confirmed it exactly.
Fable's reading: a migration whose own manifest undercounts its steps is
evidence the six items were derived separately rather than integrated as
one change.

**5. Claude asked two empty questions.** "Run it, or read it first?" and
one earlier of the same shape. Tony: "unclear." Neither offered a real
choice.

**6. The review prompt contained a check that cannot fail.** Now L-217.

**Not an error, recorded because it shaped the session.** The Mode 7
review changed the design substantially and both legs earned their
place. Fable disclosed unprompted that it was running in-project and
therefore partially contaminated; its review was still the sharper of
the two. That is worth knowing and is not an argument for relaxing the
fresh-chat rule.

---

## Tony-action rollup

- **(do)** Run `patch_L214_2_rationale_and_L219.py`, then
  `ledger_index.py`. Confirm the archive.
- **(decide)** L-219: which of three options for expressing a
  cross-handle run order.
- **(decide)** L-217: whether the two-dispatch protocol becomes standing
  practice, and which skill hosts it.
- **(decide)** L-211 UNKNOWN verdict token: designed, unbuilt, unchanged
  this session.

---

## What NOT to do

**Do not treat any responder claim as a verdict.** Unchanged.

**Do not re-dispatch the affected rows reflexively after building
L-214.** A second dispatch of a row this project has already argued
about in writing is not an independent leg.

**Do not run the gallery builder with `--commit` while L-216 is open.**

**Do not build L-214 out of order.** The moon line leaves `Note` before
or with the marker sweep, not after it.

---

*Written August 19, 2026 with Anthropic's Claude Opus 5. Built on
`5859e15097b92bbb5ebd9ebb7a8fe78fdea85aac`; gallery at
`8a4aa41268ed9efadea9ad6b40fabe880ce8bef8`.*
