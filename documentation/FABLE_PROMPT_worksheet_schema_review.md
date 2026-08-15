# Review request: the worksheet schema, and a checker that keeps
# hiding its own errors

**Built on `bdb56d8a5b0503c9afa3ff0511add2854064586e` at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Gallery repo not involved. Every number below was measured against
that commit on 2026-08-15; none is recalled.**

Prepared August 15, 2026 by Claude Opus 5. Tony Quintanilla is the
integrator and holds every decision here.

---

## Who you are writing for

Tony Quintanilla, PE, is a retired civil and environmental engineer,
an artist, and an anthropologist. He is not a professional software
developer and not a formally trained astronomer. He builds this
project through conversation with AI partners rather than by writing
code unassisted, and holds sole commit authority.

The codebase's structure and discipline are the product of that
collaboration, not evidence of personal programming fluency. Reading
the code cold will suggest a skilled programmer wrote it. Please do
not calibrate your reply to that impression. Unpack jargon on first
use.

What Tony owns personally is the workflow and the judgment: the
protocol, the ledger, the design decisions, and the integration calls
across models. His judgment window on any single question is tight,
so the useful reply is short and falsifiable rather than
comprehensive.

---

## The problem, stated plainly

The provenance system exists so the project never asserts a number it
has not verified. The concern is that the machinery built to enforce
that has become something we cannot ourselves confirm.

One session, 2026-08-15, surfaced seven defects in it. Four are
repaired at the commit named above; they are listed because HOW they
were found is the finding, not what they were:

1. `is_compound()` -- a guard written specifically to stop the tool
   discarding a human's qualification -- had zero call sites from the
   day it was written. Defined, unit-tested in isolation, never wired
   in.
2. A live finding printed `reads <<NO -- arithmetic error>> -- wrong
   authority for a value that may still be right`. The citation was
   correct and the value was wrong. The tool asserted the exact
   opposite of the truth, directly beside the correct quote.
3. All eight L2b findings were labelled DRIFTED, the strongest of
   three possible readings, on no evidence.
4. Three extractor constants were about to be treated as settled
   while ordinals derived from them were dispatched.
5. A key round-trip test minted keys from today's source and resolved
   them against today's source. It could not fail.
6. A banner announced `206 TIER-1 FINDINGS -- PUSH GATE NOT MET` and
   said two lines later that it affected nothing.
7. A ledger entry written the same day stated that zero claims sat on
   a qualified pass. Three do. The figure came from grepping the
   report, which lists routed findings, for a finding recorded without
   a route -- a green result to a question nobody had asked.

**None of the seven was found by the system. Every one was found by a
person reading, or by accident.** One was caught only because the same
prompt was sent twice by mistake on a phone with bad signal, and the
two runs disagreed. Two were caught because Tony asked a plain
question the tool's own output had not prompted -- "the citations are
correct, right?" 

That is the same failure shape as the uncited constant this whole
apparatus exists to catch: wrong, plausible, and invisible to every
check that ran.

---

## Where the defects are, and where they are not

They are not spread evenly. Every one of the six sits in the layer
that INTERPRETS a human's answer. None sits in the layer that
COMPARES two values.

Comparison has never misled us: does this file exist, does this value
equal that value, does this key still resolve, do these fourteen
numbers still drop out of the claim count. A failure there is a
mismatch, and a mismatch is loud.

Interpretation is where all six live: what did the checker mean by
NO, was this check good enough, is the value or the citation at
fault. A wrong answer there looks exactly like a right one.

---

## The measurements

At `bdb56d8`, over 104 cross-check annotations and 17 cited
worksheets:

**Which question the worksheet actually answered**

| Column the checker read | Annotations |
|---|---|
| `Citation correct?` only | 46 |
| A value verdict | 10 |
| A resolution column | 3 |
| No verdict column reached | 45 |

Ten of 104. The system verifies values, and ten annotations rest on a
worksheet column that asked about the value.

**Verdict cells carrying a token plus prose:** 61 of 355 (17%).
By class: UNREADABLE 17, CONFIRMED 15, REFUTED 12, DERIVED 7,
INCOMPLETE 6, ABSENT 4.

**What the checker currently reports** (104 annotations, 61 routed)

| Finding | Count |
|---|---|
| VALUE_VERDICT_ABSENT | 46 |
| UNMATCHED | 25 |
| NO_NUMERIC_CLAIM | 18 |
| INCOMPLETE_CHECK | 11 |
| CITATION_DEFECT | 10 |
| UNCHECKED_MOVE | 8 |
| REFUSAL_UNCLASSIFIED | 7 |
| UNREADABLE_VERDICT | 6 |
| CLAIMS_UNADDRESSED | 4 |
| DERIVED, QUALIFIED_PASS | 3 each |
| WORKSHEET_UNREADABLE, UNPAIRED_UNITS, MISMATCH, RANGE | 2 each |
| CHECK_NOT_PERFORMED | 1 |

Sixteen finding classes. That count is itself part of the question.

**What the refusals say**

| Cell text | Count | What it means |
|---|---|---|
| `NO` | 12 | ambiguous |
| `NO -- wrong authority` | 4 | citation wrong, value right |
| `NO -- does not follow from its own inputs` | 2 | value wrong |
| `NO -- arithmetic error` | 1 | citation right, value wrong |
| `NO SOURCE` | 1 | source publishes nothing |

Same token, same column, opposite meanings. The words that
disambiguate are exactly the words the classifier splits off at the
dash.

---

## The proposed schema

Tony's call: the worksheets do the real work, so they must produce
answers that need no interpretation. Four fields.

1. **Code value at time of check.** Already present in some
   worksheets; it is what makes a later change detectable at all.
2. **Value: RIGHT / WRONG / UNKNOWN**, plus the number. Where the
   sources give a range rather than a scalar, the cell carries the
   range AND the reduction rule -- "volumetric mean of 1050 x 840 x
   537 km" -- so the rule is in the worksheet rather than in a
   conversation.
3. **Citation: RIGHT / WRONG / UNKNOWN**, separately. These two come
   apart in real rows and no single column can hold both.
4. **Notes.** Every caveat, and the only place interpretation lives.

The checker's job then reduces to transcription and comparison. Most
of the interpretation layer deletes rather than gets repaired.

Downstream of this, and NOT what we are asking you to review: where
sources genuinely do not settle a value, the hover text states the
value, the source, and its status, in three states -- SOURCED,
CONVENTION (a stated rule over stated inputs), and ESTIMATE. Tony
writes those by hand and wants them as few as possible.

---

## What we are asking you to do

Two falsifiable tasks. Please do not tell us whether the architecture
is sound.

**Task 1. Break the schema.** Find a claim in this corpus that the
four fields cannot express unambiguously. One concrete row beats a
general concern. If a fifth field is genuinely required, we want to
know before the errand is dispatched, not after.

**Task 2. Find the remaining interpretation.** Assume the schema
lands. Identify every place the checker would still have to decide
what a human meant rather than compare two values. Those are the
places the next invisible defect will live.

**Please state your method before your findings.** A single review
run is one sample. On 2026-08-14 a review was accidentally sent twice:
run 1 agreed with the request, run 2 refuted it, and run 1 agreed
because it reached for the same line-window method the request had
used. Cross-model agreement confirms nothing when both sides share a
method. If you executed something, say what. If you reasoned from the
text, say that.

**Where you cannot check something, say so rather than reasoning
around it.** You have no independent repo access; everything you need
is either quoted above or reachable at the commit named at the top.

---

## Files worth reading at that commit

    worksheet_checker.py                        the checker
    documentation/worksheets/                   the 17 worksheets
    WORKSHEET_CHECK.md                          its current report
    LEDGER_CONSOLIDATED.md                      L-192, L-193

---

*Built on `bdb56d8a5b0503c9afa3ff0511add2854064586e` at
https://github.com/tonylquintanilla/palomas_orrery.*
