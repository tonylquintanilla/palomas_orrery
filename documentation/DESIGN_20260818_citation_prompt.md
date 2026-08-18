# Design note -- the citation prompt (L-207)

**Built on `b65ac115fc0f820e8270c0807249813c67bde7bc` at
https://github.com/tonylquintanilla/palomas_orrery (branch main);
gallery at `ff18d3e6fa31f70a8f525df471e751d046cf14fa`.** Both confirmed
by live `git ls-remote`.

Type: **DESIGN.** Nothing here is built. Ledger handle L-207.

Lands in `documentation/`. Companion to the L-207 block, which is the
trigger; this is the detail.

---

## The gap, measured

The citation half of a returned worksheet has no route out of the file.

Measured at HEAD, not read:

- `ROLE_SOURCE` -- the responder's own cited source, the thing a
  reviewer would compare against the code's `# Source:` line -- is
  mapped in `HEADER_ROLES` and consumed **nowhere**.
- `ROLE_CITATION_VERDICT` is consumed in exactly two places. One is the
  third branch of `read_verdict`, which is unreachable for a JSON
  return because the JSON schema always synthesizes a value column and
  the first column present wins. The other is L-200's linkage check,
  which fires only on a row that a `# Resolved:` leg already names --
  so it can confirm a review happened but cannot be the input to one.

Both halves are parsed into the Table and stop there.

**This is not a defect in the split.** The 2026-08-17 ruling put the
citation comparison with a reader precisely because it is a language
judgement rather than a numerical one, and the mechanical checker
correctly stays at numbers. What was never built is the leg that
carries the material to that reader.

The consequence, if nothing is built: the pilot's 23 rows return, the
numerical half routes, and the fuzzy half sits in a file nobody has
asked anybody to read.

---

## The design, Tony's, 2026-08-18

**The checker does two things in one run.**

1. The numerical check exactly as it does today. Unchanged.
2. A **consistent JSON prompt** asking Claude the citation question.

### Why a prompt rather than a worklist

A worklist is data. A prompt is a request, and a request inherits the
discipline the request builder already has: keyed rows, a hash over the
do-not-edit fields, a SHA anchor, and generation rather than typing.

"Consistent" is the load-bearing word in Tony's phrasing. Same SHA plus
same returns must give the same prompt. That is what makes a Claude
citation review **evidence** rather than an opinion -- re-runnable
against a different model, comparable across sessions, and
reproducible by anyone who runs the tool.

It is the same rule L-201 already applies to selections: a selection is
code, not typing, and the test is not whether the answer is right but
whether anyone can check it later.

### Why it does not move the read-only boundary

The checker is read-only over the corpus and writes reports. It already
writes `data/worksheet_routed.json`. A generated prompt is another
report-shaped output, not a writer behind the corpus boundary.

---

## What a row carries

Everything a reviewer needs to answer "does this citation support this
claim," and nothing that would make the answer unverifiable later.

| Field | Why |
|---|---|
| `key` | `module.py::enclosing::label::cN`. Stable; `row_id` is positional and renumbers. |
| `claim` | what the code asserts |
| `code_value` | the number as the code holds it |
| `code_source` | the authority currently on the `# Source:` line |
| `context_legs` | `# See:`, `# Derived:`, `# Note:` |
| `responder_source` | what the responder actually cited |
| `responder_citation_verdict` | their verdict on the citation |
| `worksheet` | the filename the row came from |
| `checker` | the identity that filled it |
| `hash` | over the do-not-edit fields, as in the request |

**The context legs are not decoration.** They are what distinguishes a
citation that is WRONG from one that is merely MISPLACED. The pilot
already predicts a row of exactly that shape:
`EARTH_EQUATORIAL_RADIUS_KM` is cited to IAU B3, which publishes
6378.1, while the third decimal comes from IERS -- and the block says
so in a `# Note:`. Without the legs a reviewer sees a mismatch; with
them, a Shape A swap.

---

## The one decision, and it was ruled

**Does the prompt show the responder's own citation verdict?**

Ruled 2026-08-18: **yes.**

*The case for showing it.* The review becomes a comparison rather than
a re-derivation, and disagreement between the responder's verdict and
the reviewer's is the **lazy-responder canary** -- the open question
from the August dispatch review -- measured per row, on real rows, with
no separate mechanism invented for it. A responder who pattern-matched
the columns produces citation verdicts that do not survive a reading,
and this is what surfaces that.

*The cost, stated rather than buried.* Seeing a verdict before judging
anchors. Structural blindness would be stronger and was traded away
deliberately. The mitigations are weaker than structure and are
therefore named explicitly:

- the responder's verdict sits in its OWN field, last, not woven into
  the prose a reviewer reads first;
- the prompt states that the review is independent, and that
  disagreement is a FINDING rather than an error to be reconciled away.

This is the same shape as the Mode 7 rule about not handing Gemini
Claude-derived figures. The difference is that here the anchor is the
measurement being taken, so it has to be visible rather than absent.

---

## What it does NOT do

- **No routing change.** The numerical routing is untouched.
- **No new verdict semantics.** The prompt asks a question; it does not
  score an answer.
- **No promotion into provenance.** A returned citation review does not
  become a `# Cross-checked:` leg by itself. What lands in the code is
  an edit, and what records it is a `# Resolved:` leg (L-200), which
  the checker already verifies for linkage.
- **No second parse.** It is an emitter over the Table the checker
  already builds.

---

## On complexity, which is the live objection

An external review on 2026-08-18 made the point that the verification
infrastructure now has a larger state space than a person can hold, and
proposed a rule: **every new provenance feature should first ask
whether it can be expressed by extending an existing data boundary
rather than adding another checking path.**

That rule is right, and this design was checked against it rather than
merely assumed to pass. L-207 adds an EMITTER over an existing
abstraction. It reuses the Table, `row_hash`, and the report writer. It
adds no layer, no verdict class, and no second reader of the corpus.
The precedent is the JSON adapter itself, which converted JSON into the
same Table rather than creating a second checker.

The honest cost: the checker gains a second artifact type, and two
outputs are more surface than one.

**And the balance question underneath it.** The same review argued the
infrastructure phase has succeeded enough that it should start paying
rent -- that the project now has more epistemic infrastructure than
epistemic coverage, with Tier-1 at 289 and rising as the scanner's
reach improves.

That is correct, and it is the reason to build this ONE thing and then
stop. Without it the pilot's fuzzy half cannot be read at all, so it is
not more polish -- it is the leg that makes the machinery usable
against the backlog. After it, the default question should stop being
"what does the provenance system need next" and become "which
outstanding claim can this now settle."

Stated as a test rather than an intention: the next provenance feature
after L-207 should be one that an actual RUN exposed the need for, not
one a design conversation invented.

---

## Sequencing

**It is not strictly blocking for the pilot.** Twenty-three rows can be
read by hand, and the material is in the returned file either way.

It IS blocking for the pilot to produce evidence of the kind this
project trades in -- reproducible, keyed, re-runnable -- and it does not
scale to 110 rows by hand.

Both orders are defensible:

- **Build first, then dispatch.** The pilot then tests the whole loop
  including the fuzzy half, which is what the pilot is for.
- **Dispatch first, read by hand, then build.** The build is informed
  by a real return rather than an imagined one, which is the standard
  this project applies everywhere else.

The second has a specific advantage worth weighing: the field list
above is a prediction about what a reviewer will need, and one real
return would replace that prediction with a measurement.

---

*Prepared August 18, 2026 with Anthropic's Claude Opus 5. Built on
`b65ac115fc0f820e8270c0807249813c67bde7bc`.*
