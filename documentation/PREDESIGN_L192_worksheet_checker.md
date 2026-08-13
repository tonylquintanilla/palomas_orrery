# Pre-Design -- The Worksheet Checker (L-192)

**Built on `00219d9852c65d653ae49855d3138050dd8f76dd`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
HEAD verified live at the time of writing, August 12, 2026.
The gallery repo is not in scope.**

**Type:** Mode 7 pre-design review (collegial relay). Nothing is built.
No code expected back -- a critique of the design, and rulings on the
open forks at the end.

**Prepared:** August 12, 2026 by Claude Opus 5, for Fable 5.
Tony Quintanilla is the integrator and holds final judgment.

**Continues from** the annotation-attachment review you returned earlier
today, which is now built and pushed. Your ruling stands: the scanner
narrowed, and this checker consumes its attachment rather than computing
a second one.

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
CLI fluency -- he runs Python from VS Code's Run button and uses GitHub
Desktop.

What he owns personally is the workflow: the protocol, the ledger, the
design rulings, and the orchestration across models. Every ruling cited
in this document is his.

**On his reading load, which is a constraint and not a courtesy.** He
has stated plainly that he is limited in what he can read and absorb.
Lead with the ruling in one plain sentence, put evidence after it, and
do not stack a finding, a recommendation, an uncertainty and a question
into one breath.

---

## What the checker is for

**One sentence: it confirms that an annotation's claim of evidence is
true.**

A cross-check annotation asserts that a named checker verified a
specific value against primary sources on a date, and wrote the check
down in a named worksheet. Everything in that sentence is currently
taken on faith. The scanner parses the annotation's shape and, since
this morning, confirms it is attached to the right value -- but nothing
has ever opened the worksheet.

**Why it matters more than it sounds.** This project's standing rule is
that wrong-but-cited is worse than uncited, because a citation
suppresses the suspicion that would catch the error. An annotation is a
citation with a checker's name on it, so it suppresses harder. Two live
examples found in the last twenty-four hours, both by accident:

- `INNER_LIMIT_OORT_CLOUD_AU` wore a top-rung badge while the two
  worksheets its annotations named read UNVERIFIED and PARTIAL for that
  very value. (Fixed at the scoring layer this morning; the annotations
  were misattached. But nothing would have caught it if they had been
  correctly attached and the worksheet still said UNVERIFIED.)
- `test_constants_provenance.py` attributed a solar chromosphere figure
  to a textbook chapter that says something different. It stood for four
  months because that file's role puts it outside the scanner's claim
  extraction.

**And the structural reason it is the last check standing.** The other
provenance tools are pre-commit readers or structural tests.
`constants_change_report.py` asks git what moved since the last commit,
which means a value corrupted and committed three weeks ago has nothing
in the diff to notice. The structural tests assert derivations and
orderings, never a measured value. The worksheet checker is the only
planned check that reaches committed history, because the worksheet is a
fixed record: it said what it said, whatever happened to the code
afterwards.

---

## Ground truth, measured at the anchor

Do not take these on faith either -- they are reproducible from the repo
at the SHA above -- but they are what the design rests on.

- **134 live annotations** across nine root modules. All 134 parse under
  the L-186 checker-first grammar.
- **18 distinct worksheets named. Zero dangling** -- every named file
  exists in `documentation/worksheets/`.
- 34 files in that directory: 18 cited, 9 uncited worksheets, 7 prompt
  files. An uncited worksheet is **pending work, not a defect** (Tony's
  ruling): the provenance sweep is incomplete and those cover files not
  yet annotated.
- **The worksheets are not one artifact.** At least eight distinct
  column schemas appear, e.g.
  `| # | Constant | Value | Cited source | Citation correct? | Notes |`,
  `| # | Claim in code | Code value | Your value | Your source | Match? | Notes |`,
  `| # | Claim | Value |`,
  `| # | Source to check | Topic | What the source says | Resolution |`,
  plus several one-off tables. Two files escape the leading hash as
  `\#`.
- **A verdict column is nearly universal among CITED worksheets: 133 of
  134 annotations name a worksheet that carries one.** Only one does
  not. This is the fact that makes the design tractable, and it was not
  obvious from the raw file survey -- 13 of the 34 files have no verdict
  column, but they are almost all uncited or prompt templates.
- **Verdict vocabulary is consistent with a long tail.** Across all
  verdict columns: YES 271, NO 47, APPROX 41, PARTIAL 37, DERIVED 27,
  CONFIRMED 24, WRONG 17, UNVERIFIED 16, and roughly seventeen further
  tokens appearing once or twice each (free text, em-dashes, sentence
  fragments).

---

## What it consumes

The scanner now exposes, per unit, the annotations attached to that
unit's own statement. So the checker's input is a tuple assembled
without any new parsing:

    (module, unit name, unit value, checker identity, check date,
     worksheet filename)

One definition of attachment, in the producer, consumed here. That was
your ruling and it is why this design has no annotation parser of its
own.

---

## Proposed design: four layers, each with a defined failure

The governing constraint is a protocol gate adopted yesterday: **a check
that cannot fail is not passing.** The test is not "did it pass" but
"what would make this fail, and does the passing output prove that path
was live?" So each layer below names its failure explicitly, and
anything the layer could not read is reported rather than skipped.

**L0 -- The worksheet exists.** Binary. Currently zero failures across
134 annotations, which is worth stating plainly: this layer passes on
day one. It can still fail -- a rename, a move, a filename mangled by a
bulk migration -- and the bulk migration is not hypothetical, since 134
annotation lines were mechanically rewritten yesterday.

**L1 -- The row is located.** Find the row in the worksheet that is
about this value. This is the hard layer and it is the first open fork
below. Failure state: UNMATCHED, reported with the unit name and the
worksheet, never silently passed over.

**L2 -- The value agrees.** Compare the unit's value against the row's
value cell under numeric normalisation (thousands separators, unicode
minus and multiplication signs, scientific notation, rounding to fewer
significant figures, unit suffixes). Failure state: MISMATCH.

This is the strongest finding the tool can produce, because it means the
code and its own recorded evidence disagree about a number. It should be
loud.

**L3 -- The verdict is read.** Classify the row's verdict cell. Failure
state: an annotation asserting a completed check over a row that records
the check as not completed. That is the Oort case, and it is the reason
the tool exists.

Proposed classification, subject to fork 2:

| Class | Tokens | Meaning |
|---|---|---|
| CONFIRMED | YES, CONFIRMED | counts as a completed leg |
| QUALIFIED | PARTIAL, APPROX, DERIVED | open question |
| REFUTED | NO, WRONG | the worksheet contradicts the code |
| ABSENT | UNVERIFIED, UNSOURCED, NEEDS... | examined, not confirmed |
| UNREADABLE | everything else | announces, does not pass |

**Reporting the denominator.** Every run states how many of the 134
annotations reached each layer. "128 of 134 classified; 6 UNMATCHED" is
the honest output shape. A bare "no problems found" is the output shape
this project has learned to distrust, because it is what a check that
never ran also prints.

**Where it runs.** Not in `maintenance_run.py` -- the ledger already
settles this, on cost grounds, since it reads 34 markdown files. Four
escalation conditions are already written into the L-192 ledger block.
Fork 4 asks whether that is enough.

---

## Open forks

These are genuine. Argue them; do not pick the one that sounds tidiest.

### Fork 1 -- How is a row matched to a value?

Eight schemas, and the identifier column is variously "Constant",
"Claim in code", "Claim", "Topic", "Question", or "Source to check". Its
cell content may be a backticked constant name, a prose description of a
rendered feature, or a section reference.

Three approaches, and I do not have a confident preference:

- **(a) Header-role mapping.** A table of known header names to roles
  (identifier / code value / source / verdict). Unrecognised header sets
  announce and the worksheet is reported unreadable. Precise where it
  works; the failure mode is that it works for constants and does poorly
  on the display-string worksheets, where the "claim" is prose.
- **(b) Identifier-free search.** Scan every row for a cell containing
  the unit's name OR a normalised form of its value; take the best
  match. Robust to schema variation, but it weakens L2 into circularity
  -- you find the row BY the value and then check that the row states
  the value.
- **(c) Require a machine-readable key going forward.** Grandfather the
  18 existing worksheets under (a) or (b), and specify that future
  worksheet prompts emit a key column. Solves it permanently, does
  nothing for the corpus that exists, and adds a rule to the prompt
  templates.

Which, and does (c) belong alongside whichever of (a)/(b) wins?

### Fork 2 -- What counts as a completed check?

QUALIFIED is the whole question. PARTIAL (37 occurrences) and APPROX
(41) plainly mean something was verified and something was not. DERIVED
(27) is different in kind: a derived value was never measured, so
"checked" means the derivation was confirmed, not the number.

Does a QUALIFIED row earn a leg toward the cross-checked rung? If not,
what does the tool say about the 100-odd rows that carry one -- are they
findings, or a queue?

Tony has this flagged as his decision. Your job is to frame it well
enough that he can rule, and to say if you think DERIVED needs splitting
out from the other two.

### Fork 3 -- May the checker WRITE?

There is a backfill waiting: 27 units lost the cross-checked rung this
morning, and their evidence sits in worksheet rows. Writing those
annotations by hand is slow and error-prone; a tool that reads the row
and emits the annotation is the obvious labour saving.

The obvious objection is that a tool which both judges evidence and
writes citations can satisfy itself. That is close to the failure this
whole layer exists to prevent.

Options: strictly read-only, with backfill done by hand; a separate tool
that consumes the checker's output; or one tool with a `--propose` mode
that emits a patch script for human review and never edits in place.
Note that the third is how this project already delivers edits, which
cuts both ways.

### Fork 4 -- What makes it run?

The ledger's four escalation conditions are events, and one of them is
wired: `constants_change_report.py` names the worksheets to re-check
when a value moves. The other three depend on somebody remembering.

Tony's own fact, which killed an earlier design: "I don't independently
run tests like that unless you ask during the build." A check in a file
nobody opens is a check that cannot fail. The store-binding check landed
in `skills_index.py` for exactly this reason -- it runs at the moment
the drift is introduced.

So: is there a moment-of-introduction hook for this one? It cannot go in
the maintenance runner on cost grounds. Is the cost argument still right
if the tool caches per-worksheet parse results and only re-reads files
whose modification time or content hash moved?

### Fork 5 -- What does it do about the nine uncited worksheets?

They are pending work, not orphans (Tony). They represent sweeps that
were run and never wired into the code. Listing them every run makes the
output a nag; never listing them loses them. Is there a shape between?

---

## What to send back

Tony will paste your response into a fresh session. Open with the same
anchor line this document carries.

Then, in this order:

1. **Your one-sentence verdict on the design as a whole** -- sound,
   sound-with-changes, or wrong in a way that needs restating.
2. The five forks, each with a recommendation and its reasoning. Say
   plainly where you are uncertain rather than picking to be decisive.
3. Anything the design MISSES -- a failure mode it cannot detect, a
   layer that should exist, an assumption that will not hold.
4. Any second questions, listed separately at the end rather than woven
   in.

Two constraints from this project's standing rules, either of which you
may argue against explicitly:

- **The artifact bounds the audit.** Scope is what the code contains at
  this commit. An audit whose denominator grows whenever someone thinks
  of something never closes, and an audit that never closes stops being
  read.
- **Ledger economy.** Do not propose four new handles. Say plainly if
  this is one item.

**One request specific to you, and it is not routine.** Earlier today
your written attachment rule and your own measurement script disagreed
-- the prose said the entry line, the script used the literal's line one
row below. My independent verification reproduced the error, because it
implemented the same prose and read it the same wrong way, and I
reported that agreement to Tony as confirmation. It was confirmation of
a shared misreading. The number went to him wrong twice before it was
caught.

That is not a complaint; it was caught, and the outcome was better for
your review existing. But it is the reason for this: **where you state a
rule in this response, state it in a form you would be willing to have
tested against an implementation you did not write.** If a rule has a
case you are unsure about, name the case.

---

*Pre-design prepared August 2026 with Anthropic's Claude Opus 5, built
on `00219d9852c65d653ae49855d3138050dd8f76dd` at
https://github.com/tonylquintanilla/palomas_orrery*
