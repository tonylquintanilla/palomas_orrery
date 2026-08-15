# Mode 7 Review -- The Request Builder (L-192, producer half)

**Built on `305b2697648590e4a75551c73743abc98bd20c66`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
HEAD verified live by `git ls-remote` at the time of writing,
August 14, 2026. The gallery repo
(https://github.com/tonylquintanilla/tonyquintanilla.github.io,
`c2202dcc2c4ed210160ce6033b70346aef194b68`) is not in scope and is
untouched.**

**Type:** Mode 7 design review (collegial relay). Nothing is built. No
code expected back -- a critique of the design, and rulings on four
open forks.

**Prepared:** August 14, 2026 by Claude Opus 5, for Fable 5. Tony
Quintanilla is the integrator and holds final judgment.

**Continues from** your review of the worksheet checker itself
(`documentation/FABLE_REVIEW_L192_worksheet_checker.md`, anchored
`6de5e8d`), which is built, corrected, and pushed. Your five rulings
stand except ruling 5, which Tony overturned on measurement -- the
verdict vocabulary settled at seven tokens rather than twenty-seven.

---

## Who you are writing for

Tony Quintanilla, PE, is a retired civil and environmental engineer, an
artist, and an anthropologist. He is not a professional software
developer and not a formally trained astronomer. He builds this project
as a "vibe coder" -- through conversation with AI partners rather than
writing code unassisted -- and holds sole commit authority.

**The codebase is not evidence of his personal programming skill.** Its
structure and discipline are the product of iterative collaboration.
Reading the code cold you would infer a skilled programmer wrote it;
that inference is wrong. Unpack jargon on first use and do not assume
command-line fluency -- he runs Python from VS Code's Run button and
uses GitHub Desktop.

What he owns personally is the workflow: the protocol, the ledger, the
design rulings, and the orchestration across models. Every ruling cited
in this document is his.

**On his reading load, which is a constraint and not a courtesy.** Lead
with the ruling in one plain sentence, put evidence after it, and do
not stack a finding, a recommendation, an uncertainty and a question
into one breath.

---

## Where this sits

The checker is built and running. It reads every cross-check annotation
attached to a scored value and asks, in six layers, whether the
worksheet the annotation names actually says what the annotation
claims. It is report-only and writes no annotations.

The checker is the CONSUMER. This document is about the PRODUCER: the
requests that go back to the checking models (Claude, GPT, Gemini) to
fill the gaps the checker found.

Your largest observation last round was that the requests must not
leave before the instruments that make them succeed exist, or round two
happens by construction. This design is that instrument. It is the last
thing between the current report and dispatch.

---

## Ground truth, measured at the anchor

Reproducible from the repo at the SHA above. Method is deliberately
withheld -- please re-derive rather than reconcile, as you did last
round, and report differences rather than resolving them.

Current checker run:

| | Count |
|---|---:|
| Annotations attached to a scored unit | 104 |
| Clean -- every layer passed | 3 |
| Routed to SEND BACK | 41 |
| Routed to CONVERSATION | 20 |
| Noted, no route | 40 |
| Annotation lines the scanner does not score | 30 |

Findings by class, counted over the report's tables (128 rows; one
annotation can carry several findings):

| Class | Count |
|---|---:|
| VALUE_VERDICT_ABSENT | 25 |
| UNMATCHED | 25 |
| CITATION_DEFECT | 17 |
| DRIFTED | 8 |
| DERIVED | 3 |
| UNREADABLE_VERDICT | 2 |
| WORKSHEET_UNREADABLE | 2 |
| INCOMPLETE_CHECK | 2 |
| RANGE | 2 |
| MISMATCH | 1 |
| CLAIMS_UNADDRESSED | 1 |

Three facts this session established, and they are what the design
rests on:

- **24 of the 25 UNMATCHED findings are display-string claims, not
  constants.** Only `CHROMOSPHERE_PHYSICAL_KM` is a constant. Constants
  match today by name; what has no row is prose.
- **The 25 UNMATCHED rows are 19 distinct code sites.** Several sites
  carry two annotations, one per checker.
- **Four of those 19 sites duplicate another site's prose.** The
  module-level `*_info` string and the shell function's `description`
  hold the same text, differing in `\n` versus `<br>`: `pluto` 41/61,
  136/155, 400/423, and `venus` 43/62. So the errand is **15 distinct
  bodies of prose**, not 25 requests.

---

## What Tony has already ruled, this session

Do not relitigate these. Argue them only if you think one is wrong in a
way that breaks the design.

1. **Keys are tool-issued and shipped pre-filled.** The builder emits a
   request table with the key column already populated, one row per
   claim needing an answer. Checkers fill the evidence and verdict
   columns only. They do not invent keys.
2. **Duplicated prose gets one row keyed to both sites.** Not one row
   per site. Four checkers researching the same paragraph twice is the
   waste this errand cannot afford.

Two consequences worth stating, because they close questions you might
otherwise raise:

- **The blind-lookup independence objection is nearly empty here.** A
  pre-filled row must show the prose so the checker knows which claim it
  is answering, and for a display string the number is INSIDE the prose
  -- "about 1,700 km" is both the claim and the value. Only one of the
  nineteen sites is a constant, where withholding would be possible.
- **The worksheet's own anchor SHA carries the code value.** L2b (drift
  since the check) reads against the commit the request was cut from,
  which is your ruling 3 from last round applied at the producer end.

---

## The design

Four pieces, intended as one build pass.

**1. `worksheet_request_builder.py`.** Reads the checker's UNMATCHED and
CLAIMS_UNADDRESSED output, dedupes by prose, and emits a request file
per dispatch batch: key column pre-filled, evidence columns empty. A
separate module rather than a mode inside the checker, so the
read-only boundary stays where you put it -- the checker judges, the
builder asks. Run-button invocation, no command-line flags.

**2. A key rule in `worksheet_checker.py`.** Exact key match ahead of
the four existing L1 rules (name, prose containment, code-value
equality). A row carrying two keys resolves to both sites. A key that
resolves to nothing announces as KEY_STALE and does NOT fall through to
the fuzzy rules, because falling through would hide a rename behind a
lucky prose hit.

**3. Header lines in every emitted file.** The vocabulary version line
(skill 2.3's column-scoped seven tokens) and the worksheet's own anchor
SHA.

**4. Tests**, including one that fails if a stale key silently matches.

### The key format

```
pluto_visualization_shells.py::create_pluto_core_shell::description::c1
pluto_visualization_shells.py::pluto_core_info::c1
constants_new.py::CHROMOSPHERE_PHYSICAL_KM
```

Module, enclosing name, label, claim ordinal. Two exclusions are
deliberate:

- **No line number.** Edits shift them and a worksheet is a fixed
  record.
- **No code value.** A key containing the value would break under
  exactly the drift the checker exists to detect -- the pointer would
  move with the thing it is supposed to outlive.

The enclosing name is what disambiguates. `pluto_visualization_shells.py`
carries five separate `description` fields; each sits inside its own
`create_*_shell()` function, so the function name separates them.

**Uniqueness, measured:** across the 53 distinct annotated sites the
current report names, this rule produces 53 distinct keys and zero
collisions.

**And a stated limit on that measurement, because it is the shape of
failure that bit us last round.** I computed the enclosing name with my
own regular expression, not with the checker's existing `anchor_label`
function. If both implement the same misreading, the agreement is
confirmation of a shared misreading rather than of correctness. The 53
also excludes the 3 clean annotations and the 30 lines outside scanner
reach, so it is not the full corpus.

---

## Open forks

These are genuine. Argue them; do not pick the one that sounds tidiest.

### Fork A -- The claim ordinal moves when the prose does

`::c2` means "the second numeric claim in this string." Edit the
paragraph to introduce a number ahead of it and `c2` silently
re-points to a different claim.

My belief is that this surfaces as a drift finding rather than a clean
false pass, because the value at the new position will not match the
worksheet's recorded value. But it surfaces as the WRONG finding: the
report says the value drifted when the truth is that the key stopped
meaning what it meant. A wrong diagnosis sends the wrong errand.

Every alternative I can see has its own defect. Keying on the number
itself breaks under precisely the drift we are trying to catch. Keying
on surrounding words breaks under copy-editing, which is routine in
display prose. Keying on a content hash makes a typo fix indistinguishable
from a claim change.

I do not have a good answer. This is the fork I most want a second
opinion on. If your answer is "accept the defect and detect it," say
what the detector is.

### Fork B -- A rename makes keys permanently unfixable

The key names an enclosing function. Rename `create_pluto_core_shell`
and every key pointing into it goes stale at once.

The bind is that neither end can be repaired. The code should be
renameable -- forbidding renames to protect a citation scheme is
backwards. And the worksheet must not be edited, because this project's
standing rule is that a worksheet is the record of what was known on its
date; editing it to match today's code is the same failure class as
citing over recalled data.

So the evidence stays good while the pointer dies. An alias map
(`old_name -> new_name`, maintained where?) is the obvious patch and I
am not confident it is the right one -- it is a second store that can
drift from the first, which is the failure class this whole protocol
exists to kill.

### Fork C -- What counts as "the same claim" for the dedupe

Tony ruled that duplicated prose gets one row. The builder therefore
needs a rule for when two strings are the same claim.

I merged on a longest-shared-run threshold of 120 characters after
normalising away `<br>`, `\n`, quotes and whitespace. **That threshold
is a number I picked.** It produced four pairs, all of which look
correct on inspection, and two near-pairs it declined to merge
(`pluto` 614/638 and `venus` 339/437) which also look correct.

The asymmetry matters. A false merge drops a distinct claim from the
errand and nothing announces -- the row exists, so no gap is reported.
A false split costs duplicated research and is visible.

State the rule in a form an implementation you did not write could be
tested against, and name the case you are unsure about.

### Fork D -- Two table schemas, permanently

Pre-filled requests introduce a ninth column schema while the eighteen
existing worksheets keep their eight. Grandfathering is the honest
answer, and it means the checker's header registry never simplifies --
it grows.

Is there a shape that converges? Or is a permanently bimodal registry
simply the correct cost of not rewriting historical records?

---

## Two things deliberately NOT sent to you

Stated so you can object if you think either belongs in the errand.

- **Key uniqueness across the full corpus** is a measurement, not a
  judgment. I ran it over the 53 sites the report names and stated its
  limits above.
- **Whether the builder imports the checker or parses its report** is a
  decision, not a fork. Import. A tool that parses its own sibling's
  output breaks silently when the output format moves, and this project
  has already paid for that once.

---

## What to send back

Tony will paste your response into a fresh session. Open with the same
anchor line this document carries.

Then, in this order:

1. **Your one-sentence verdict on the producer design as a whole** --
   sound, sound-with-changes, or wrong in a way that needs restating.
2. The four forks, each with a recommendation and its reasoning. Say
   plainly where you are uncertain rather than picking to be decisive.
3. Anything the design MISSES -- a failure mode it cannot detect, a
   piece that should exist, an assumption that will not hold.
4. Any second questions, listed separately at the end rather than woven
   in.

Two standing constraints, either of which you may argue against
explicitly:

- **The artifact bounds the audit.** Scope is what the code contains at
  this commit. An audit whose denominator grows whenever someone thinks
  of something never closes, and an audit that never closes stops being
  read.
- **Ledger economy.** Do not propose four new handles. Say plainly if
  this is one item.

**One request specific to you, and it is the same one as last time
because the lesson keeps earning its place.** Where you state a rule in
this response, state it in a form you would be willing to have tested
against an implementation you did not write. If a rule has a case you
are unsure about, name the case. Two implementations agreeing does not
confirm correctness when both were derived from the same prose read the
same wrong way -- that is how a wrong number reached Tony twice before
it was caught, and it is why the ground-truth section above withholds
method.

---

*Review document prepared August 2026 with Anthropic's Claude Opus 5,
built on `305b2697648590e4a75551c73743abc98bd20c66` at
https://github.com/tonylquintanilla/palomas_orrery. Gallery at
`c2202dcc2c4ed210160ce6033b70346aef194b68` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io --
untouched by this session.*
