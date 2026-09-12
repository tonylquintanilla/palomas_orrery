# Review reply -- a declared value, an unimplemented rule, and the push gate

Reviewed against orrery `da6bcea17f4bb4335aa0717d33f6a2e771f05bef`
at https://github.com/tonylquintanilla/palomas_orrery
Gallery repo not read; nothing here is gallery-side.

Tony Quintanilla, PE | reply written by Claude Fable 5.1, inside the
Paloma's Orrery Project (protocol and skills resident) | 2026-09-12
Type: DESIGN REVIEW REPLY (Mode 7, cooperative). No code, no diffs,
no ledger handles proposed.

## What I read, and how

- `PROJECT_INSTRUCTIONS.md` v3.57 -- resident in the Project, and
  fetched at the SHA above to confirm the stamp matches. The sections
  the request names, plus A Report Names Its Items.
- `skills/provenance-discipline/SKILL.md` 2.11 -- the installed copy.
  It matches the manifest row (2.11), and I diffed it against the repo
  copy at the SHA: byte-identical after line-ending normalisation. The
  Status Line, Measured Is the Goal, A Breadcrumb Must Not Cite, The
  Access Standard, Uncited Goes to the Ledger, and Scanner Mechanics.
- `provenance_scanner.py` at the SHA: `SOURCE_PATTERNS` and
  `has_citation` (lines ~610-705), `get_context_block` (~1460), the
  constant extractor (~1750-1775), `score_unit` (~2364-2470),
  `load_exceptions` and `is_suppressed` (~2610-2665), and the scan loop
  where suppression is applied (~2775-2785).
- `constants_new.py` at the SHA (the 2 status lines are at 425 and 479).
- `data/provenance_exceptions.json` at the SHA.

Not read: the L-305 patch itself (it is not in the repo), and
`PROVENANCE_AUDIT.md`. Where I reason about the patch's row layout I say
so and give the test that would confirm it.

## Two premises in the request are wrong, and both change the answer

**1. The exceptions file exists.** It is at
`data/provenance_exceptions.json`, not the repo root, and the scanner
loads it from `data/` (`load_exceptions`, line ~2616). The skill's
Scanner Mechanics section says `data/` too. Question 6 dissolves as
asked -- but reading the file and its matcher produced a different
finding, under question 6 below, and it matters for option choice.

**2. "The blast radius today is 19 rows" undercounts what the written
rule does.** The Status Line says two things the lean does not carry:
a row with NO status line is reported as *unexamined*, not passed; and
inference is *removed*, not kept as a fallback. Implemented as written,
the rule turns 86 of 88 rows in `constants_new.py` into "unexamined"
today. So the smallest possible option 1 -- read `# Status: declared`,
change nothing else -- is one third of the rule, with inference kept as
the fallback the rule explicitly forbids. That does not sink option 1.
It means option 1 is not "implementing something already decided"; it
is landing a partial mechanism, and the protocol's own lesson on
central factories says a partial mechanism with no stated migration
plan is the dangerous state. The fix is to state the plan. See
question 1.

## The two green rows -- mechanism, read from the code

The request measured `has_citation()` against each row's own
annotation block and got False for all three. That measurement is
correct and it is not what the scanner scores.

`score_unit` sets `cited = has_citation(unit.context_text)`. For a
constant, `context_text` is built by `get_context_block` with
`lookback=30, lookahead=15`: thirty lines above the assignment and
fifteen below, as one flat string. The row's own annotation
(`attached_text`) is used only for cross-check credit (L-192), never
for the source half. So a constant reads "Cited" if ANY line in the
forty-five lines around it matches any `SOURCE_PATTERNS` entry.

That explains the stripping test exactly. Removing every author-year
and page number from the three declared blocks moved nothing because
the clearing citations were never in those blocks.

Where they are, deduced from the geometry the request describes (three
declared rows in a row, Bz in the middle):

- `PRESSURE`, first of the three, is within 30 lines of the sourced
  rows above it (the cut angle, Jelinek's parameters). It clears from
  above.
- `Bz`, in the middle, is red. Its 30-line lookback covers
  `PRESSURE`'s whole block, so `PRESSURE`'s block contains no
  pattern match -- which is also why `PRESSURE` cannot be clearing on
  its own text. Bz's 15-line lookahead stops inside `SPEED`'s block.
- `SPEED`, last of the three, is within 15 lines of whatever sourced
  row follows the declared block. Its 30-line lookback reaches only
  `Bz` and `PRESSURE`, which we know are pattern-free. It clears from
  below.

Bz sits in the dead zone: more than 30 lines from the citation above,
more than 15 from the citation below. One row further in either
direction and it would be green for the same reason its neighbours are.

The one assumption in that deduction is block length (that `PRESSURE`'s
block fits inside Bz's 30-line lookback). Two confirming tests, either
one is enough: print `unit.context_text` for the three units and look
for the pattern hit; or, on a throwaway copy, pad 31 blank lines above
`PRESSURE` and 16 below `SPEED` and re-scan -- both green rows should
go red.

This is the founding case of a sentence the skill already carries: the
Status Line section lists "the thirty-line lookback crediting a
neighbour's annotation" as the first inference the rule exists to
delete. The behaviour is now characterised, by reading, so the request's
worry about designing around something uncharacterised is retired.

## The questions

### 1. Is the lean wrong?

No. Option 1, with two amendments.

**Amendment A -- state the migration intent.** The scanner change is:
a row carrying `# Status:` is scored from that line; a row without one
is scored by the existing inference, unchanged. That is the
"migrate-in-scope, defer-with-tracked-backlog" branch from the
protocol's central-factory lesson, and the deferred part -- 86
unexamined rows, and the removal of inference once they are examined --
is recorded as ONE ledger row by class, not 86 rows. That is The Braid:
bound the program to what the current artifact adds (the 17 rows this
patch writes status lines for, plus the 2 that exist), and let the rest
be backlog with a denominator.

**Amendment B -- the change carries evidence.** The run summary prints
how many rows were scored from a status line and how many by
inference, with the status-line rows named by kind. See question 2.

On option 3: it is underweighted in the other direction. The three
conditions are not drawing knobs. A Drawing Approximation Does Not
Promote protects a number typed in because the result looked right;
these are inputs to a cited model, they have physical meaning, and
L-314 exists precisely because a measured value for each one exists.
That makes them *declared pending* in the skill's vocabulary, which is
backlog with a handle -- and backlog belongs in the store where the
handle can sit on the row. L-314 being real is the argument FOR putting
them in `constants_new.py` now: when the feed lands, the promotion is
a one-row edit from `declared pending` to `measured V_FETCHED`, with
the renderer untouched. Option 3 would make L-314 a renderer change
plus a store addition instead.

On option 2: the request's own reason stands, and there is a sharper
one. The gate binds at export. A store file that is knowingly red makes
every later export check ambiguous -- "did this pass, or is this the
known one?" -- which is the two-questions-one-answer failure named in
A Check That Cannot Fail. Option 2 is acceptable only as a one-push
fallback if Tony rules the scanner change does not land first, and then
the red finding is NAMED in the handoff, not suppressed (see 6).

### 2. Does option 1 create a check that cannot fail?

As "declared goes quiet," yes. As "declared announces itself," no. The
difference is four properties of the implementation, and the request
should ask for all four:

- **Declared rows are reported, by name.** The audit gets a section
  "Declared (n)" followed by the row names and dates -- the
  MODULE_ATLAS shape from A Report Names Its Items. A reader who sees
  `EARTH_SOLAR_WIND_BZ_NT` under Declared can ask whether it belongs
  there. A reader who sees nothing cannot.
- **Declared plus a citation is a finding.** If a `# Status: declared`
  row's attached block also matches `SOURCE_PATTERNS`, that is a
  contradiction (either the source clears the value or it is declared;
  the skill already says the status line must not be citable). Report
  it. This is the honest form of the Bz row's own logic: cite-to-clear
  is the thing being guarded against, and a declared row that also
  cites is exactly that.
- **`declared pending` without a pointer is a finding.** The skill
  splits the two kinds so the backlog is countable; a pending row with
  no handle is uncountable and should say so.
- **The summary names which path scored each row.** "88 rows: 19 from
  status lines (16 measured, 3 declared pending), 69 by inference."
  That line cannot print unless the parse ran. "0 Tier-1" alone can
  print for any reason at all. This is the first move under A Check
  That Cannot Fail (make success carry evidence) and it is also what
  makes the deferred inference removal visible every run instead of
  forgotten.

With those four, writing `# Status: declared` is not a silencer. It is
a claim that lands in a named list a reader sees every run, that is
contradicted if the row also cites, and that is dated.

### 3. Attack the premise on Bz

I looked. The only thing Shue et al. 1998 says about zero is that the
1997 model's dependence of r0 on Bz changes slope at Bz = 0 nT (p.
17,693 -- seen in a scanned copy surfaced through a ResearchGate
listing, which is not an Access Standard route). That is a property of
the 1997 piecewise fit. The 1998 tanh form the patch uses has nothing
special at zero. I found no accessible authority publishing Bz = 0 as a
nominal or reference condition for evaluating the model.

So the premise holds: do not cite. The row is `declared pending`, with
L-314 as its pointer, and its reason in plain words -- "neutral case
chosen here; the model's own averages are about 4 nT northward and
southward taken separately." Two cautions on the wording. The
author-year pattern in `SOURCE_PATTERNS` needs parentheses with "et
al." or a year beside a surname; a reason written as prose without that
form does not clear the row by accident, but a reason that names the
paper's page belongs in the ledger row, not on the constant (A
Breadcrumb Must Not Cite). And once the scanner reads status lines, a
declared row that DID match the pattern would be the contradiction
finding under question 2, which is the right outcome.

### 4. The two green rows

Neither a scanner bug nor a new option. The scanner is doing what it
was written to do -- and what it was written to do is the inference the
skill has already ruled removed. Two rows in one provenance state
scored differently is the Status Line rule's own failure case appearing
in the wild, one push before the rule is implemented. It is evidence
for option 1, and it is the sentence to put in the ledger row's body,
because it is the clearest demonstration the project has that a green
constant in this file currently means "a citation is within forty-five
lines," which says nothing about the constant.

Record it by class, not by instance: the class is "constants scored by
window inference," and its instance count is every row without a
status line.

### 5. Scope

The scanner change is not L-305's. L-305 is a renderer on the critical
path; a scanner change is shared CI with family-wide ripple, per the
skill's own field notes. But The Braid does not put it in L-322 either
-- it says bound it to what the current artifact renders, and the
current artifact renders these three numbers plus fourteen sourced
ones, all of which get status lines in this patch.

So: its own bounded item, or a named sub-item of L-322, landed as a
SEPARATE commit BEFORE the L-305 patch. This is the v3.55 ordering --
take the change that the build depends on first, so the build lands
against a gate that can read it, and nothing travels as an obligation.
The L-305 patch then goes out green for a reason the audit can print.

The cost is serialisation: one bounded scanner change stands in front
of the renderer. That is the one ruling this reply leaves with Tony.
If he rules it does not land this week, option 2 for one push, with
the Tier-1 finding named in the handoff by row and reason.

### 6. The missing exceptions file

Not missing. What reading it found instead:

Suppression matches a fingerprint (first 40 characters) as a substring
of `unit.context_text + unit.raw_value`, per file. For a constant,
`context_text` is the 45-line window. A suppression entry aimed at the
Bz row -- fingerprint `EARTH_SOLAR_WIND_BZ_NT = 0.0` -- would therefore
also match every unit whose window contains that line: `PRESSURE`,
`SPEED`, and any row within 30 lines below or 15 above. Suppressed
units are dropped from `all_units` before reporting, so those
neighbours would vanish from the audit with no line saying so.

The mechanism was built for display strings, where the fingerprint is
the string's own content. On a dense constants file it over-suppresses
invisibly. That is a check that cannot fail, of the "blind spot does
not announce" kind, and it is why the exceptions file is NOT a fourth
option here even though the skill says false positives go there.

That is worth one ledger row, by class: "the exceptions matcher is
window-scoped and unsafe for constants." The skill description is not
stale; the tool is narrower than the description implies, and the
narrowing should be written where it fires.

## Where the request's framing is itself wrong, stated first as asked

The request presents option 1 as the cheap implementation of a
finished decision and the other two as paying a price to avoid it. The
measured picture is: option 1 is a partial implementation that must
declare its own backlog; the green rows are its founding case rather
than an unknown; the exceptions route the skill would normally offer is
unsafe for this file; and the three values are `declared pending`, not
`declared`, which is what makes option 3 wrong rather than merely
untidy. The lean survives all of that. The framing did not.

Written September 2026 with Anthropic's Claude Fable 5.1.
