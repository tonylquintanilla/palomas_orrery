# UNKNOWN -- the verdict for "I looked and could not determine"

**Built on `eae95f5a119906968634d57a9fab8964e815466e` at
https://github.com/tonylquintanilla/palomas_orrery (branch main).**

Type: **DESIGN, HELD.** Ruled and not built. Tony's ruling,
2026-08-18: hold, and let the pilot returns show whether the hole is
real.

Lands in `documentation/`.

---

## Why a held design gets written down at all

Two reasons, and neither is bookkeeping.

The first is that this is the first feature declined under the rule
adopted the same day. `provenance-discipline` 2.5 says the next
provenance feature should be one an actual RUN exposed the need for,
not one a design conversation invented. UNKNOWN was invented in a
design conversation. If the rule is going to bite, it has to bite on
something that looked worth building -- otherwise it is decoration.

The second is that a hold decays into a forget. The design is
finished; only the evidence is missing. Written down with its trigger
attached, it becomes a thing the returns can switch on. Left in a
conversation, it becomes a thing somebody re-derives in six weeks
having lost the reasoning.

---

## The hole

The vocabulary today carries two words for a check that did not
produce a confirmation:

- `unverified` -> `V_ABSENT` -> "nobody performed the check" ->
  **SEND BACK**
- `unsourced` -> `V_SOURCE_ABSENT` -> "somebody looked and the source
  does not publish it" -> **CONVERSATION**

There is no word for *I looked and could not determine*. The cases
that produce it are ordinary: a paywalled edition, two authorities
that disagree, a source whose stated precision cannot settle the digit
in question, a citation naming a document with several revisions.

A responder in that position has two options today and both misreport.
Writing `unverified` asserts that nobody looked, which is false, and
routes the row back to the person who already looked. Leaving the cell
blank routes it back as an empty verdict, which reads as a skipped
row.

**The precedent for splitting is four lines above where UNKNOWN would
go.** `unverified` and `unsourced` were separated because collapsing
them reported the Bennu row -- "Not checked" -- as a citation defect,
which blames the source for work that was never done. UNKNOWN folded
into `unverified` is that same error mirrored: it blames the responder
for work that WAS done.

---

## The rulings, if it is built

These are settled, so that a later session does not re-litigate them
if the trigger fires. What is NOT settled is whether it gets built.

**1. It routes CONVERSATION, never SEND BACK.** Sending it back asks
the same responder to repeat a search that already failed. A human
decides whether to try a different authority, accept a documented gap,
or remove the claim.

**2. It requires a note, and this is the load-bearing rule.** UNKNOWN
is the cheapest possible answer -- twenty-three of them costs nothing
and looks like diligence. So UNKNOWN with an empty notes cell is not
UNKNOWN; it routes SEND BACK as an incomplete row. The check is
PRESENCE, not prose-reading, so it stays inside what this tool is
permitted to do. And it inverts the incentive: UNKNOWN becomes more
work than a real answer rather than less.

**3. It earns no rung.** Obvious, and worth writing down precisely
because it is the token most likely to be reached for at scale.

**4. Two or more INDEPENDENT UNKNOWNs on one key stop being about the
responders and start being about the claim.** That is the mechanical
detection of the condition Fetched-vs-Recalled already names as its
third branch: a claim that cannot be sourced gets removed and the gap
noted. The report names a candidate. It never removes anything.

Point 4 costs almost nothing to compute, and that is not a
coincidence: L-207 already groups responder legs under one key in
`citation_prompt_rows`. Counting independent UNKNOWNs per key is a
count over a structure that now exists, which is what
"extend a boundary before adding a path" asks for.

---

## The trigger, pre-registered

Written before the returns arrive, which is the only time a threshold
is worth anything. Same discipline as
`PILOT_EXPECTED_DISPOSITIONS_20260817.md`, and for the same reason: a
threshold chosen after seeing the data is not a threshold.

**What counts as evidence the hole is real.** A returned row is
UNKNOWN-in-disguise when either:

- the verdict reads `unverified` (V_ABSENT) AND the notes cell is
  non-empty and describes a search that was performed; or
- the verdict is unreadable (V_UNREADABLE) and the token hedges rather
  than answering -- "unclear", "cannot determine", "ambiguous",
  "conflicting sources".

Both are mechanically findable in `WORKSHEET_CHECK.md` once the
returns are checked. Neither requires reading prose to decide the
route; the reading is done by a person, once, over a handful of rows.

**The threshold. Two or more such rows across the three returns and
UNKNOWN gets built. Zero or one and it does not.**

**And the outcome that must be recorded either way.** If the count
comes back zero, this file gets a line saying the prediction failed
and the token was not built. That line is the whole point of writing
the threshold down. A held design that quietly gets built anyway, or
quietly gets forgotten, teaches nothing about whether the rule works.

---

## What was dispatched

Three requests, all at
`eae95f5a119906968634d57a9fab8964e815466e`, selection 2
(`constants_new`), 23 rows each, identical row content and identical
row hashes -- the hash is over key, claim and code value and does not
touch the batch label:

- `REQUEST_constants_new_pilot_claude.jsonl` (+ `.md` fallback)
- `REQUEST_constants_new_pilot_gpt.jsonl` (+ `.md` fallback)
- `REQUEST_constants_new_pilot_gemini.jsonl` (+ `.md` fallback)

Three independent responders on identical rows is what makes ruling 4
measurable at all. It also makes the pilot a competitive-pattern run
in the Mode 7 sense: agreement across three confirms rather than
validates, since shared training can produce shared misreadings.

**A first-run observation, measured rather than predicted.** The
requests are written into `documentation/worksheets/`, which is the
directory the checker scans as its corpus. The checker therefore loads
them, lists them as uncited worksheets, and verifies their integrity
blocks -- `23 row hash(es) verified: 23 ok`. Routing was unchanged and
no annotation matched a request row, because matching is keyed to the
filename an annotation cites. Harmless, and the hash verification is a
free consistency check on what goes out. Noted here because it was
found by running the thing rather than by reading it, and because a
later session seeing REQUEST files in the corpus directory should not
have to re-derive that it is fine.

---

Written August 18, 2026 with Anthropic's Claude Opus 5.
