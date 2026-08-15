# Handoff -- 2026-08-15 -- the checker made honest, the schema settled

**Built on `66cf0cbcf298787542ae9b7bf335273d7ffa67d1`; pushed at
`2a8f82366265fa87b7b0e761c479b1fdeb0f6e28`, then
`bdb56d8a5b0503c9afa3ff0511add2854064586e`, then
`f8b4356abe53c423e9730b2c70086f3fa5f1fcd7`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).**
Every SHA above was confirmed by a live `git ls-remote` and each pushed
file compared byte-for-byte against the tree the tests ran on. Gallery
repo untouched this session.

Lands in `documentation/`.

**Skill gate: clear, and nothing to carry forward.**
`ledger-and-session-records` loaded 1.6 against manifest 1.6 --
discharging the obligation the 2026-08-14 handoff left. `provenance-
discipline` loaded 2.3 and `agentic-pre-test` 1.2, both matching. No
skill was bumped mid-session, so the next session inherits no deferred
version check.

---

## What this session was

It opened as two rulings blocking dispatch and ended somewhere else.
The extractor ruling landed in the first hour. The second one -- eight
DRIFTED findings -- dissolved under two plain questions from Tony, and
what it dissolved into was a checker that had been reporting confident
wrong answers for three protocol versions.

By the end the dispatch errand is blocked on purpose, on a schema
decision, rather than by accident on two rulings.

---

## Tony's rulings, in order

1. **Freeze the extractor constants.** `INSTRUCTION_LOOKBACK = 30`,
   `INSTRUCTION_LOOKAHEAD = 25`, no retune. Measured: the drop set is
   identical for lookback 25 through 60 at every lookahead tested, so
   30 sits mid-plateau with nowhere better to move.
2. **The checker must tell a fix from a defect.**
3. **Send Haumea back for sourcing** -- 715 against the axes in its own
   comment, whose geometric mean is 779.5.
4. **Wire `is_compound` in now, not later**, AND open a ledger item.
   Tony's framing, which is the requirement the whole handle serves:
   *we need to know when values and citations are wrong or missing, and
   when they are not, reliably.*
5. **Four fields for the worksheet schema:** code value at time of
   check; value tri-state plus the number (or a range with its
   reduction rule); citation tri-state, separately; notes.
6. **Three hover states:** SOURCED, CONVENTION (a stated rule over
   stated inputs), ESTIMATE. Tony writes the estimates by hand and
   wants them as few as possible.
7. **Dispatch shape: one pre-printed row per (key, ordinal)**, code
   value filled in by the builder. Measured cost on the corpus: 53
   rows become 65.

---

## What landed in the repo

| At | What |
|---|---|
| `2a8f823` | Extractor freeze: `test_extractor_pins.py`, `documentation/worksheets/L192_extractor_pins.txt`, the `Extractor pins` row in `maintenance_run.py`, the freeze note above the constants. L2b's three outcomes and the compound-verdict handling. |
| `bdb56d8` | L-193 in the ledger. |
| `f8b4356` | Two corrections to claims written earlier the same day. |

**L2b now has three outcomes instead of one.** DRIFTED means the
worksheet confirmed that value and the code left it anyway -- the only
defect of the three. CORRECTED means the worksheet refuted it and the
code moved. UNCHECKED_MOVE means no value verdict exists, so neither
word is honest. All eight former DRIFTED rows are UNCHECKED_MOVE.

**`is_compound` is wired into `dispose_verdict`**, the one function both
the constant and string paths call. A compound clearing verdict emits
QUALIFIED_PASS and stops counting as clean. A compound refusal under a
citation column emits REFUSAL_UNCLASSIFIED instead of asserting which
of value or citation is at fault. Seven live rows moved.

The qualification decides WHETHER the tool may classify. It is never
read to decide WHAT the tool says. That would be a prose-parsed
convention, which is the failure class this project keeps meeting.

Tests went 51 -> 61. Twelve checkers pass.

---

## Open items

**Tony-action (do)**

1. Send `FABLE_PROMPT_worksheet_schema_review.md` -- already done this
   session; the reply is in
   `documentation/FABLE_REVIEW_worksheet_schema.md`. Listed only so the
   round trip is closed in writing.
2. File `L192_haumea_sourcing_sendback.md` into `documentation/` if it
   is not there yet. It carries the ruling and the exact question,
   including the instruction not to reopen the equatorial figure.

**Tony-action (decide)** -- all from Fable's review, none blocking the
builder

3. **Break 2, the qualitative rendered claim.**
   `mars_visualization_shells.py:518` says Mars lacks a stratosphere.
   GPT found it unsupported. It renders, so The Artifact Bounds the
   Audit puts it in scope, but field 2 wants a number and this claim
   has none. Either qualitative rendered claims are out of the
   worksheet system's scope and that gap is stated rather than silent,
   or field 2's object generalizes to "the number, OR the claim text
   quoted verbatim." Option (b) stays comparison-safe: the checker
   verifies the quote still appears byte-for-byte.
4. **Over-precision policy.** `compare()` rounds both sides to the
   coarser of the two displayed precisions and returns MATCH. That is
   deliberate and defended in its docstring, but it absorbs two
   opposite cases. Code coarser than the source is a benign display
   rounding. Code finer than the source is an unsupported digit. The
   direction is mechanically distinguishable -- `min(displayed_
   precision(raw), code_places)` currently discards which side was
   coarser -- so this is computable, not interpretive.
5. **Which citation leg field 3 verdicts.** `SUN_RADIUS_KM` carries
   `# Source:`, `# Ref:` and `# Also:`. One tri-state cannot split
   them.
6. **Cross-worksheet disagreement.** Two responders, same (key,
   ordinal), opposite tri-states. Reporting both and routing to
   conversation is safe. Choosing between them is not, and "one
   aggregated verdict per claim" is the natural next feature request.
7. **What UNKNOWN does.** It is a state, not a route. Whether it
   blocks, passes or parks is a policy ruling; the checker's default
   becomes policy by silence otherwise.
8. **The pluto 614/638 merge**, still open from yesterday. New
   evidence: both sites carry the identical claim signature (`0.04`,
   one instruction drop), and both are among the three live
   QUALIFIED_PASS rows.

**Claude-side, held on purpose**

The worksheet request builder is NOT started. It emits requests in the
current schema, and the schema is being re-cut. Building it now means
building against something Tony has already ruled will change. It
resumes once items 3 through 7 are settled.

---

## Verified against the corpus, not accepted on report

Fable's review was traced back to source before being endorsed. Three
Task 1 breaks confirmed real: `CHROMOSPHERE_RADII` does carry the L-180
drawn-value ruling in its own comment; `ROCHE_LIMIT_RADII` does have
three separable legs; `eris_hill_sphere_info` does report 3 of 4 claims
unaddressed.

One correction to it. The Earth over-precision example is spent --
`EARTH_EQUATORIAL_RADIUS_KM` was flagged PARTIAL and the addendum
resolved it, because the code now discloses that B3 rounds to 6378.1
and the full precision comes from IERS. The structural point about
`compare()` stands; the illustrative case does not.

**And one thing the review missed that makes the re-cut much cheaper.**
`worksheet_claude_constants_new_addendum.md` already carries this
header:

    | # | Constant | Code value | Your value | Source |
      Value correct? | Citation correct? | Notes |

That is the four fields, in the corpus, already parsed -- one of the
ten annotations reading a value column. The schema is not a proposal
with a worked example; it is a worked example being generalized. The
re-cut is "make the others look like the addendum."

---

## Process record: seven checks that could not fail

Every one was found by a person reading or by accident. None was found
by the system. Three were Claude's own, written the same day they were
caught.

1. `is_compound()` -- written to stop the tool discarding a human's
   qualification -- had zero call sites from the day it was written.
2. `CITATION_DEFECT` printed "wrong authority for a value that may
   still be right" beside `<<NO -- arithmetic error>>`, asserting the
   opposite of the truth next to correct evidence.
3. All eight L2b findings were labelled DRIFTED, the strongest of three
   readings, on no evidence.
4. The L2b patch was generated by diffing a tree that already had the
   extractor patch applied, so an unrelated edit rode along as hunk 3.
   Every ordering test came out byte-identical because they all
   compared against that same tree. Self-consistent, therefore green.
5. `patch_ledger_L193.py` carried a line-ending normalizer whose
   escapes were doubled. It replaced a four-character literal that
   appears in no file. It could not fail on a `.py` file, because the
   project mandates LF -- and it aborted on the first CRLF file it met.
6. L-193 stated that zero live claims sat on a qualified pass. Three
   do. The count came from grepping `WORKSHEET_CHECK.md`, which lists
   routed findings, for a finding recorded without a route.
7. The QUALIFIED_PASS message called `<<YES -- fully confirmed>>`
   "confirmed with a reservation" -- the tool characterizing prose it
   is forbidden to read, one size smaller than defect 2 and written
   while fixing it.

Tony's diagnosis, and it is the reason the schema work exists: a
provenance system whose own errors are visible only to careful reading
has the same failure shape as the uncited constant it exists to catch.

The errors are not spread evenly. Every one sits in a layer that
interprets a human's answer. None sits in a layer that compares two
values. Comparison has not misled us once.

---

*Prepared August 15, 2026 with Anthropic's Claude Opus 5. Built on
`f8b4356abe53c423e9730b2c70086f3fa5f1fcd7` at
https://github.com/tonylquintanilla/palomas_orrery.*
