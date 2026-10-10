---
name: provenance-discipline
description: "Provenance and citation discipline for the Paloma's Orrery project. Use whenever running or discussing provenance_scanner.py, reading PROVENANCE_AUDIT.md, clearing Tier-1 findings, adding or reviewing # Source: citations, editing provenance_exceptions.json, embedding constants or numeric/factual claims in orrery display strings or data modules, or preparing a GitHub push (the gate is Tier-1 = 0 on the active build path, and it binds at EXPORT from the orrery). Also use when composing on-layer or user-facing factual text for any orrery visualization. Do not use for projects other than Paloma's Orrery."
fires_when: Scanner runs, audits, citations, constants, pre-push (Tier-1 = 0 on the active build path)
---

# Provenance Discipline

Read this file in 5 parts: lines 1-301, 302-605, 606-863, 864-1151, 1152-1305.

Skill version: 2.28 | 2026-10-09, with Anthropic's Claude Opus 5.5, at
palomas_orrery @ aa46bb10. v2.28 (L-414) settles how the scanner reads
a row, under Scanner Mechanics and The Goal State. A row in
constants_new.py is read through its own comment run, not a window of
30 lines back and 15 ahead: the window missed EARTH_MEAN_RADIUS_KM's own
Source line 16 lines down (2026-10-04), and credited the stratopause
row's Source to the thermopause row when a planted-fault run removed
the thermopause's own (2026-10-09). A declared row with its reason
written down is its own kind, named and never Tier-1. The gate-path
figure is read from the two exports and printed by name, on the
console, in the audit and in the run history. The two measurements are
field notes. Riding this version: The Status Line says what the
scanner now reads, and A Breadcrumb Must Not Cite says where the window
still applies.
Earlier: 2.27 | 2026-10-08, with Anthropic's Claude Opus 5.5, at
palomas_orrery @ b0b3df82. v2.27 (L-418) splits the skill, and no rule is
reworded. The relay procedure, the Review-Repair Protocol, is now the
skill provenance-cross-check. Rules 1 to 8 of the figure count moved to
references/figures.md and the field notes to references/field-notes.md,
each opened when its pointer says; the withdrawn derived-row rule moved
to documentation/SKILL_HISTORIES.md. Every moved section is word for
word apart from the edits the build patch lists. The file opens with a
read plan, written by skills_index.py, because one read does not show
it whole: the design session's viewer showed 16,000 characters, from
the start and the end, and this session's reader showed lines 1 to
1,106 and said it had stopped (2026-10-08). Riding this version: the
range rule's examples name rows that exist, and a patch predicts the
scanner's change rather than its total (both L-371); Rule 1 names the
conversion marker and Rule 8 records the widening as built (L-390); and
the examples in The Status Line and Report to the Figures You Have name
rows as they now stand.
Earlier: 2.26 | 2026-10-05, with Anthropic's Claude Opus 5.5, at
palomas_orrery @ 72e3b558. v2.26 (L-418) changes no rule. A contents
list now opens the skill, generated from its headings, and
skills_index.py --check fails if the two disagree. Version history
older than the two entries below moved to
documentation/SKILL_HISTORIES.md. Both because a plain read of a
long file shows its start and end and leaves out its middle, where
the rules are (Tony, 2026-10-05).
The sections are also put in order of what must fire: the critical
rules first, then the quality rules, then those with no tier, then the
two long procedures, Report to the Figures You Have and the
Review-Repair Protocol for Cross-Checked Annotations, and the field
notes last. Every section's text is unchanged.
Older entries are in documentation/SKILL_HISTORIES.md, moved there
on 2026-10-05 and 2026-10-08 (L-418) and 2026-10-09 (L-414).

## Contents

Generated from this file's headings. skills_index.py --check fails
if this list and the headings disagree (L-418).

- The Visibility Convention [CRITICAL]
- The Gate Binds at EXPORT [CRITICAL]
- The Access Standard [CRITICAL]
- Measured Is the Goal, Declared Is the Fallback [CRITICAL]
  - When the source gives a range
- A Drawing Approximation Does Not Promote [CRITICAL]
- The Status Line [CRITICAL]
  - The Unit Field
  - The Read Field
  - Geometry Constants Are First-Class Claims
- One Value, One Home [CRITICAL]
- Observations Are Sourced Facts, and They Migrate [CRITICAL]
- No Shadow Constants [CRITICAL]
  - A Breadcrumb Must Not Cite [CRITICAL]
- Extend a Boundary Before Adding a Path [QUALITY]
- Uncited Goes to the Ledger, Not the Bin [QUALITY]
- A Computed Position Prints What Its Errors Earn [QUALITY]
  - An Accuracy Stated in Words Is Stored as the Place It Reports To
- A Simple Error a Check Finds Is Fixed and Reported [QUALITY]
- Examples Go Stale Like Values [QUALITY]
- The Goal State
- Clearing a Flagged Claim (the only two moves)
- Scanner Mechanics (not obvious from the output)
- Report Domain Classification (Findings by File / File Type)
- Fetched vs Recalled -- the working procedure
- Composed vs Transcribed On-Layer Text
- Report to the Figures You Have [QUALITY]
  - The Store Carries the Verified Figure [CRITICAL]
- Cross-Checked Lines in the Store
  - A Cross-Check Retires With Its Value or Its Citation [CRITICAL]
  - Retired: `# Verified: April 2026 via Gemini fact-check`
- Field Notes

Kept outside this file and opened when needed: `references/figures.md`
holds The Figure Count Is a Declared Field, Rules 1 to 8, and
`references/field-notes.md` the field notes. Sending a value to other
models for a check is the skill provenance-cross-check.

## The Visibility Convention [CRITICAL]

**A failure that prints where the responder reads it gets an
ANNOTATION. A failure that appears nowhere gets a REFUSAL. Visibility
decides, not severity.**

The case that produced it: the request builder joins a citation
continued onto a marked line, and two things can go wrong. A
continuation marker whose label does not match the leg above it is
REPORTED -- the mismatch prints into the worksheet, where the person
filling the row will see it and can say so. A continuation line
carrying no marker at all REFUSES the whole build, because nothing
about it reaches any reader: the text is silently dropped and the
worksheet that results looks complete.

Severity would have ranked these the other way round. A label mismatch
is the louder defect on its face. What matters instead is whether the
system can be told about the failure by somebody who sees it, because
a defect with a reader has a correction path and a defect with no
reader does not.

The rule generalizes past the builder. Before choosing between
reporting a problem and refusing to proceed, ask where the report
lands and who reads it. If the honest answer is that it lands in a log
nobody opens, or in a file the next session will not load, then
reporting is silence wearing the costume of diligence, and the correct
behaviour is to refuse.

(Tony's ruling, 2026-08-17, settling an L-196 question as a convention
rather than a one-off, because the same distinction governs every
future case of the same shape.)

## The Gate Binds at EXPORT [CRITICAL]

**A value's provenance closes before it LEAVES THE ORRERY. Not before it
is drawn, and not before it is published.**

Three points, and they are not the same point.

**Why the gate exists: SERVING.** A visitor takes what the site shows as
true. There is no place downstream of the orrery where a wrong radius is
caught -- not the builder, not the resolver, not the browser. None of
them knows what a correct ring radius is.

**Where the gate FIRES: EXPORT.** The orrery is the last place a check
can run. `provenance_scanner.py` lives in the orrery repo and scans the
orrery tree. `gallery_cache_builder.py` lives in the GALLERY repo and
scores nothing -- it mentions provenance twice, once in a docstring
recording where its copied constants came from and once in a warning
string. The two repositories do not share a checker. So a gate placed at
publication sits downstream of the last instrument in existence, and a
gate nothing can enforce is A Check That Cannot Fail Is Not Passing
wearing a different hat.

**What is still free: DRAWING.** A local render gates nothing. It costs
an afternoon to undo and nobody outside the room sees it.

So the rule in operational form: **a body's slice closes before its
values enter `objects_config.json` and the served cache** -- not
afterwards, and not before the page goes live. A body cannot be added to
the served set and cleared later.

The property this buys is easier to state than the one it replaces. The
cache becomes, by construction, a set of values whose provenance was
closed at the moment they entered it. "Everything served has been
checked" is a claim about a boundary crossing, which happens once and
can be gated. "Everything published has been checked" is a claim about
an accumulating set, which has to be re-established on every build.

**A consequence, recorded because it changes a priority.**
`objects_config.json` is maintained BY HAND in the gallery repo. So the
export boundary this gate names is, today, a human copy with no check on
it at all. That makes the cross-repo transport (master plan segment 2)
the gate's missing enforcement point rather than a defence against
later drift, which is higher than the plan currently places it.

This EXTENDS the earlier line that the asymmetry "governs what an
artifact may LOCK, not what may be BUILT." That sentence was about
fingerprinted golden artifacts and is not withdrawn.

The braid is intact: the audit stays bounded by the current artifact,
stays countable, and stays off the critical path as a gate. What moved
is where it binds.

(Tony's rulings. 2026-08-27, the principle: the gate binds where a
claim reaches a reader, not where it is drawn. 2026-08-28, the
placement: "I think provenance should be settled before it leaves the
orrery to the gallery cache. There is no provenance checker in the
gallery." The second corrects the first without withdrawing it.)

**What the provenance leg requires, and what it does not.** It requires
Tier-1 = 0 on what is served -- cited, and TRUE. It does NOT require a
cross-check. A cited claim that has not been cross-checked scores 15,
which is Tier 2 REVIEW, and Tier 2 has never gated a push. Cross-checked
is a higher rung earned deliberately, not a condition of clearing
Tier 1.

(Tony's ruling, 2026-08-27. Worked case: the Sun's served features carry
111 numeric values -- 85 declared drawing parameters, 26 measured sites
holding 19 distinct values. Each measured field carries both a `source`
string and an `orrery_constant` pointer, and nine of nine served numbers
checked matched the store constant they name. That is a closed slice.)

## The Access Standard [CRITICAL]

**A citation clears only if its text can be reached and read. No
paywalls.**

Three routes, in order of preference:

1. **Open full text** -- arXiv, NASA ADS scans, publisher open access,
   agency documents, IAU and IERS publications.
2. **A free abstract**, when the claim is stated in it.
3. **A Google Scholar or Books snippet** showing the sentence in
   context.

A source reachable only behind a paywall FAILS, whatever its authority.
Books and papers are held to the same test.

**A snippet must carry the qualifier, not just the number.** Snippets
truncate, and the truncation is how `ALFVEN_SURFACE_RADII` went wrong:
the figure was right and the missing words were "above the photosphere."
A snippet showing a figure without the condition attached to it does not
clear the claim.

**A source names what was OPENED, not what it cites.** The Source cell
records the document the checker opened. Not the paper that document
cites for the claim, and not what the checker believes the document to
be.

The failure is invisible without a second fetch: right URL, right
access word, right figure, wrong attribution. A row can be entirely
correct about the literature and still send the next session to a paper
nobody read.

So the row quotes the TITLE AND AUTHOR LIST AS PRINTED in the document
opened. One field, mechanical, and it fails visibly when a checker is
reconstructing from memory instead of reading a title page. Where the
figure is background the document passes on from earlier work, that
earlier work is recorded as the next layer down, not as the source.

(L-321, 2026-09-13. A checker returned two correct extents and named
Usanova 2014 and Ganushkina 2011. The PDFs at those URLs are Meredith
et al. 2014 and Li, Tu et al. 2024, each citing the named paper in its
introduction. Two of three load-bearing rows; the third had opened a
paper that cites the one it was asked to check.)

**When a source fails access, re-home the citation to an accessible
authority carrying the same result. Delete only when none exists.** Most
failures are re-homeable, because the values that reach this store are
standard results that open sources also carry. PREM is the model: the
1981 paper is walled, the tabulation is open in several places, and the
value survives with a new citation.

**Prefer an accessible non-book authority.** Claude cannot reach Scholar
or Books, so every surviving book citation lands in Tony's manual queue.
Re-homing removes it from that queue. Minimising the queue is the point.

**Scope: prospective, at the serving gate, per slice.** This does not
trigger a sweep of every existing citation. Each body's values meet the
standard when that body reaches its ladder step. A retroactive pass has
no denominator and becomes the gate the braid was ruled to end.

**Why access rather than authority.** Two consequences, and the second
is the one worth keeping. A citation nobody in the loop can open is
functionally the retired `# Verified:` stamp -- it stops the next reader
from looking while recording nothing checkable. And every source string
the served hover shows a visitor becomes one the visitor can open.

(Tony's ruling, 2026-08-27: "If we can't access from an open paper, an
abstract or a google scholar search with context then the citation
fails. No paywalls. I don't have access to a research library.")

## Measured Is the Goal, Declared Is the Fallback [CRITICAL]

**A declared value is a placeholder for a measured one wherever a
measured one exists, and it is promoted as soon as it can be.**

The worked precedent is in the file. `CHROMOSPHERE_PHYSICAL_RADII` drew
at 1.1 solar radii as a visibility stylization for years; on 2026-08-16
it was promoted to the physical 1.002875 and the stylization retired.
That is the move, and it is the default direction of travel.

**Two kinds of declared, and mixing them makes the backlog
uncountable.**

- **declared pending** -- a fallback standing in for a value that
  exists and has not been sourced or promoted yet. Carries a ledger
  handle. It is backlog.
- **declared** -- a pure drawing choice, or a pick from a range that
  the source gives as a range on purpose. It never promotes, because
  there is nothing to promote to. It is not backlog.

Without the split, "declared" is a bucket mixing things that must move
with things that never will, and the remainder cannot be counted.

```
# Status: declared 2026-08-28 -- top of measured 2-4 range
# Status: declared pending 2026-08-28 -- L-2xx
```

### When the source gives a range

**Store the range as data, derive the drawn value from it by a stated
rule, and let display text interpolate the range rather than restate the
drawn value as a measurement.**

This is L-179's mechanism, generalised. `HELMET_CUSP_LOW_RADII` and
`HELMET_CUSP_HIGH_RADII` are a worked pair: the two rows carry the
source, the access and the read, and the drawn `HELMET_CUSP_RADII` is
a declared construction over them, the top of the range. (Until v2.27
the example here was the gravitational influence, whose range rows
are gone: it is now the Sun's Hill radius, one calculated value.)

The rule is NOT which end of the range to draw. Top, midpoint and low
end are all in the store and all correct for their rows -- the helmet
cusp takes the top so the drawn cusp does not understate the helmet,
Earth's outer-belt peak takes the midpoint, the core takes the low
end. The rule is that **the pick is a declared choice and its reason
lives on the row.**

**Where nothing in the source favours an end, the pick is the
midpoint** (v2.18). That is the construction the outer belt's peak
already uses. An end is picked only for a
reason the row states, as the helmet cusp's top and the core's low end
do. So the question "which point in the range" is answered by this
section and does not go to Tony; a reason to leave the midpoint is
written on the row, where the next reader can check it. (Tony,
2026-09-23, on the magnetotail's flare, which Slavin et al. (1983)
place at 100 to 120 Earth radii: "I thought the midpoint
interpolation is in the skill." It was the practice and not the rule;
it is the rule now.)

This supersedes the weaker Batch 1 convention -- best-sourced single
value in code, range in the description -- for any row where the range
is genuinely the sourced object. The weaker form leaves the range in
prose, where it cannot be interpolated and drifts from the number beside
it.

A pick typed as a literal with its range in `# Declared:` prose does
not meet this section, however well the prose cites (v2.17): the range
is rows, the pick is an expression over them -- a declared
construction, Rule 2 -- and the display shows the range from those
rows. Earth's outer-belt peak, typed 4.5 with its L = 4 to 5 band in
prose and the band typed again as literal text in the orrery's own
hover, was the corrected case at L-322 C2.

## A Drawing Approximation Does Not Promote [CRITICAL]

**A number typed into a renderer because the RESULT LOOKED RIGHT is not
a constant waiting for a home. It does not promote. It is replaced, or
it stays where it is.**

This bounds the section above. That one governs a DECLARED value --
something the store already holds, standing in for a measured value
that exists. This one governs a number that was never a value at all:
a shape parameter chosen by eye, an axis ratio that made the render
read well, a sweep cap whose only justification is that the flank
stopped flaring where somebody liked it.

Moving such a number into `constants_new.py` and attaching a plausible
citation is WORSE than leaving it in the renderer, and the reason is
mechanical. The store is the thing the drift checker follows, the
thing the hover quotes to a visitor, and the thing a later session
trusts without re-deriving. Promotion launders the approximation
through all three. It is the same failure as a `# Source:` over
recalled data, one layer over -- the promotion suppresses the
suspicion that would have caught it.

**Three outcomes, and promote-as-is is not among them.**

- **Source the SHAPE it belongs to and recompute.** The number was a
  parameter of a model nobody had chosen. Choose the model, cite it,
  and the parameter comes with it or is derived from it.
- **Draw the sourced range and say so** -- the geocorona pattern. Where
  the honest object is an extent rather than an edge, draw the sourced
  figure and let the hover state what it is.
- **Remove it and note the absence.** The remove-and-note rule,
  unchanged.

**The tell:** a value whose only provenance is that a previous session
accepted the render. Mode 5 is the acceptance gate for a VISUALIZATION.
It is not a source for a NUMBER, and a value that passed it has been
looked at, not measured.

**Two things this does not forbid**, and both matter or the rule
overreaches. A DECLARED pick that stands for a physical size -- a
pick from a sourced range with its reason on the row -- stays legal
and lives in constants_new.py. (Until v2.18 this sentence also listed
opacity and point count as staying "in the store"; they are rendering
settings, and One Value, One Home's Three Kinds of Drawing Number keeps
them in the drawing code.) And a visibility stylization still promotes when the
physical value becomes drawable, which is the chromosphere precedent
and the direction the section above sets. The line is whether there is
a real value the number is standing in FOR. A stylization stands in for
a measurement. An eyeballed shape parameter stands in for nothing.

(Tony's ruling, 2026-09-08, on Earth's magnetosphere: "We are not
promoting Mode 5 approximations," and "not promoting approximations or
rounded numbers." Seven drawn numbers in that one renderer had no store
name and every one of them was a candidate. The rebuild on a cited
model is L-305; this rule is what stopped the shortcut. It is a SKILL
rule and not a decision because it resolves the same way next month,
for a different body, in a different file.)

## The Status Line [CRITICAL]

**Every value in `constants_new.py` declares its own provenance state.
The scanner reads that declaration instead of inferring one.**

One line, immediately below the assignment, using the existing `+`
continuation convention:

```
# Status: <kind> <rung> <ISO date> [-- <pointer>]
```

`<kind>` is one of three, and they are the registry zones:

- **measured** -- a published value. Carries a rung.
- **declared** -- a drawing choice or a pick from a range. No rung; a
  source is not expected and its absence is not a finding.
- **derived** -- computed from other constants. No rung. Names its
  inputs and is never cleared on its own; checking it means checking
  them.

`<rung>` applies to measured values only and is one of the four the
scanner already defines: `V_FETCHED`, `V_CROSS_CHECKED`, `V_SOURCED`,
`V_RECALLED`.

The ISO date is when the status was last confirmed under the standard in
force. **No status line at all means the pass has not reached this
value** -- which is different from a value that was examined and found
wanting, and the scanner reports it as unexamined rather than passing
it.

The optional pointer names a worksheet, a source record, or a ledger
handle.

```python
HELMET_CUSP_HIGH_RADII = 4
# Status: measured V_SOURCED 2026-10-04 -- abstract, open

EARTH_MAGNETOPAUSE_SHUE_A1_RADII = 10.22
# Status: measured V_SOURCED 2026-09-11 -- open full text

EARTH_GEOSTATIONARY_RADIUS_KM = (EARTH_GM_KM3_S2 / EARTH_ROTATION_RATE_RAD_S ** 2) ** (1.0 / 3.0)
# Status: derived -- inherits EARTH_GM_KM3_S2, EARTH_ROTATION_RATE_RAD_S
```

**The status line must not be citable.** It carries no source text, no
agency name, no author-year, and no URL. Those live in `# Source:` and
in the worksheet. A status line that names an authority becomes a
citation for the value beside it, which is the failure A Breadcrumb Must
Not Cite already covers.

**The declaration is the only store, and inference is REMOVED rather
than kept as a fallback.** If a value declares `V_SOURCED` and the
scanner also infers a rung from a nearby comment, the two can disagree,
and that is One Value, One Home violated on a property instead of on a
number. Deleting the inference is what this section buys: the
thirty-line lookback crediting a neighbour's annotation, `# Verified:`
matching the citation pattern, a bare URL in a breadcrumb scoring as a
source, and orphan section-header annotations all trace to the scanner
guessing.

As built at v2.28 (L-414): the scanner reads each row's own comment
run, so the thirty-line lookback no longer reaches a neighbour, and it
reads the declared kind (Scanner Mechanics). It does not yet read a
measured row's rung: a measured row still scores by whether its own run
carries a citation.

### The Unit Field

**A unit is a declared field beside the value, `# Unit:`, never a
suffix on the name.** Two declarations of one fact can disagree, so the
suffix is dropped as a declaration once the field exists. The token
names the QUANTITY, which is what makes comparison possible: `deg`
rather than `dimensionless` for an angle, `l_shell` rather than
`dimensionless` for a McIlwain L, because 105 degrees is not
interchangeable with 105 of anything else. `dimensionless` names no
quantity and retires as a token.

**`constants_tokens.py` owns the token table.** One entry per token,
carrying its dimension -- an astropy unit string, or the words `named
number` for a quantity with no physical dimension that is still a named
thing, which is what `l_shell` is -- and, for a unit defined by a value
in the store, the row that defines it. A retired token is not simply
absent: `RETIRED_TOKENS` holds it with the reason, so a checker meeting
`dimensionless` on a row says what is wrong with it instead of saying
the token is unknown. A token in neither table is a failure. That file
replaces two pieces of the gallery that did this job by inference,
`SCALAR_UNITS` and the suffix reader.

The migration is walked by body, Earth first, and each row is visited
ONCE: `# Unit:`, `# Status:`, `# Figures:` (below) and, where the row is
in scope, `# Read:` (below) are all written at that single visit.

(Tony's rulings, 2026-09-11 and 2026-09-14, recorded on L-322 and until
this version living only there. In engineering he has always used
units, not literals.)

**Inside a dict, the status line attaches to the DICT when its entries
share one kind and one source**, and an entry that differs carries its
own line, which overrides. This does not reopen the per-value ruling of
2026-08-13: that ruling addressed annotations sitting inside a
thirty-line proximity window, where a parser cannot distinguish group
intent from accident. A status line on a dict is structurally scoped,
not merely near.

### The Read Field

**A typed-in number can be checked by a person or a model reading the
source against it, and `# Read:` records that this happened.** One line
beside the value, in the same comment block as `# Unit:`, `# Status:`
and `# Figures:`:

```
# Read: <page or table>, <date>, <reader>
```

```python
EARTH_MAGNETOPAUSE_SHUE_A1_RADII = 10.22
# Read: Table 1 "After Fit", p. 17,698, 2026-09-11, Claude Fable 5.1
```

**Scope: a measured row whose value is DRAWN in a published exhibit,
and any row that feeds one.** Not every row in the store. A declared
drawing choice has nothing to read against, and a measured row nobody
draws is outside the bound, by The Artifact Bounds the Audit.

**Who does the reading is decided by ACCESS, not by importance.** The
scope of 2026-09-11 said the check applies "where critical" and never
defined the word. Tony's ruling, 2026-09-19:

> what I meant by critical is where your own search tools cannot read a
> needed source but I can.

He glossed "need" in the same message: a number is in the store and
needs a source. So the question is never how important the number is.
An unimportant number behind a wall only Tony can open still goes to
him, and a load-bearing number the builder can open never does.

Three branches, and a row takes whichever applies:

- **The builder can open the source.** The builder reads it against the
  row and writes the line, naming ITSELF as the reader. A model's read
  is a real read, recorded as a model's.
- **The builder cannot open it and Tony can.** The row goes on a
  reading list for him: one file, one row per constant, with the link,
  where to look in it, and the number he should expect to see. That
  list is Tony's WHOLE share of the reading -- nothing else in a slice
  walk asks him to read a source -- and it is a file he opens at his
  machine, never a list in chat. His line carries his name and the date
  he read.
- **Neither can open it.** The citation fails The Access Standard.
  Re-home it to an open authority carrying the same value, or remove
  the claim and note the gap.

**A read counts only if the source was actually OPENED.** The line
records what was opened, with the title as printed and the table or
page, under The Access Standard's rule that a source names what was
opened rather than what it cites. A read reconstructed from training is
worse than no read, because the line stops the next reader from looking
while recording nothing that was checked. This is a `# Source:` over
recalled data, one layer out.

**No line at all means the row has not been read**, the way a missing
`# Status:` means the pass has not reached the value. Inside a closed
slice a missing line on an in-scope row FAILS; outside one it is named
as not yet migrated.

(Tony's rulings, 2026-09-11 and 2026-09-19, on L-322 ruling (b),
confirmed point by point on 2026-09-19 before this section was written.
The fourteen magnetosphere rows already carry a dated per-row record in
`documentation/L305_gap1_read_record_20260911.md`, a model's read of
Tony's PDFs; their lines name the model.)

### Geometry Constants Are First-Class Claims

A `radius_fraction` in `shell_configs.py` is a provenance claim exactly as
much as a number in a display string. It asserts a physical size; it is
just written in units of body radii instead of km.

**When a cross-check corrects a display value, the constant moves in the
SAME patch.** Not deferred, not a follow-up. Batch 1 moved Mercury's outer
core text from 2,074 km to Hauck's 2,020 km and left `radius_fraction` at
0.85 -- so the shell kept drawing 2,074 km while the hover asserted 2,020.
Six shells across four bodies were in that state, and every offline test
passed the whole time.

**The scanner cannot catch this.** It flags numeric tokens in display
strings; `radius_fraction` is a dict constant with no unit attached, so it
is invisible to `NUMERIC_CLAIM_RE`. There is no scanner fix that would
help -- the constant is not wrong in isolation, it is wrong RELATIVE to a
string somewhere else in the file. That relation is what the Fable
consistency audit checks (workflow step 8), and it is the only thing that
does.

Record the derivation in the comment, so the next reader can re-run it:

```python
'radius_fraction': 0.828,  # 2,020 km / 2,439.7 km (Hauck et al. 2013)
```

## One Value, One Home [CRITICAL]

**A numeric value has exactly one home -- `constants_new.py`, with its
source. Everything else references it: the drawing, the hover string,
the tooltip, the comment. A number typed anywhere else is a second
store, whether or not it currently agrees.**

This is the POSITIVE form of the section below, and the difference is
not stylistic. No Shadow Constants forbids copying a value that ALREADY
lives in `constants_new.py`. It says nothing about where a value's first
home is when a new feature introduces one, and a new feature is exactly
where the second store gets created.

**Prose counts.** A hover string that types `1,220 km` is a store. Build
the sentence so the number interpolates:

```python
f"The inner core is {EARTH_INNER_CORE_KM:,.1f} km in radius."
```

Two strings that both interpolate the same constant cannot disagree
numerically, which is why prose duplication and value duplication are
different problems -- the first is L-191, the second is this rule.

**Dead code counts.** A literal in a function nothing calls is still a
store, and it reads as authoritative to whoever finds it next. Wire it
or delete it; do not leave it because it cannot run. (L-254.)

**THE SCOPE BOUNDARY, and it must be stated in the same breath:
THREE KINDS OF DRAWING NUMBER** (v2.18, Tony's ruling of 2026-09-22).
Every number a drawing uses is one of three kinds, and each kind has
one home.

- **A PHYSICAL value** -- a size, an edge, a distance, a cut angle, a
  width -- lives in `constants_new.py`. A measured one is sourced. A
  decided one is declared, with its reason and the range it was picked
  from on the row (When the Source Gives a Range).
- **An EYEBALLED value** -- a physical value chosen because the render
  looked right, usually before the sourcing rules existed -- does not
  promote (A Drawing Approximation Does Not Promote). It is replaced by
  one of that section's three outcomes as the braid reaches it, and a
  published room is reached first.
- **A RENDERING SETTING** -- `n_points`, `n_rings`, `marker_size`,
  marker type, `opacity`, colour, font, `mesh_resolution`, an angular
  marker step -- makes no claim about the object. It stays in the
  drawing code where it is drawn. Tony: "these are defined in the code
  not in constants new."

**The test between the first kind and the third: does changing the
number move WHERE something is drawn, or only change HOW it looks?**
Earth's radiation-belt thickness of 0.5 Earth radii was the case that
needed the test. It looks like a drawing setting, but it moves where the
rings sit, so it is physical; with no recorded origin it is eyeballed,
and Stage D replaces it by the belts' served edges. A point count only
makes the same ring smoother.

Two notes on the third kind. A colour is a rendering setting, but a
hover sentence saying what colour the object IS is a claim and needs a
source like any other. And two rendering settings were still in
`constants_new.py` when this was written, `DEFAULT_MARKER_SIZE` and
`CENTER_MARKER_SIZE`; they are one ledger class and move to the drawing
code when their files are next touched.

This is L-240's split, sharpened. Without it "only store" reads as
hauling 25 and 3.4 into `constants_new.py`, which buries the values
that matter under the ones that do not.

**IN TIME: forward-going on every file touched.** The standing backlog
carries the sweep -- L-181 is the parent, with L-243, L-244 and L-248 as
open slices. This rule does NOT open a repo-wide sweep on the day it is
adopted; that is the denominator that grows whenever someone thinks of
something. (The Braid, resident protocol Part 3.)

(Tony's ruling, 2026-08-26, stated as general and confirmed with the
boundary above in the same exchange.)

## Observations Are Sourced Facts, and They Migrate [CRITICAL]

An observed event figure is a measured value with a source, and its home
is `constants_new.py` like any other.

A disintegration radius, a spacecraft's closest approach, a crossing
distance, a perihelion -- these read as narrative rather than as
constants, so they get typed into prose and stay there. They are
observations of the physical world with an authority behind them, and
One Value, One Home applies to them without exception.

The scope boundary is unchanged: MEASURED values migrate, DECLARED
drawing parameters stay where they are drawn.

The practical consequence is an ordering one. A citation cannot move
into the store ahead of the value it cites, because a citation with no
value beside it has nowhere to sit. So the migration is: value first,
then its source line, then the prose references the constant.

(Tony's ruling, 2026-08-27. Founding case: MAPS C/2026 A1's
disintegration at 8.33 R_sun is cited to SOHO/CCOR-1 observations at
`solar_visualization_shells.py` line 1226, and the figure itself lives
only in display strings.)

## No Shadow Constants [CRITICAL]

Modules must not carry local copies of values that exist in constants_new.py. Import through the established shim (planet_visualization_utilities) or directly from constants_new.py. A local literal that numerically matches a tracked constant is a frozen copy -- it won't follow if the source value updates, and it bypasses the scanner's citation chain even when the number is correct today.

This is the code-side complement to the scanner's build_pinned_values() check: the scanner can flag a suspicious match, but the standing rule is that these should never be introduced in the first place. When found, delete the local definition and replace it with a proper import -- do not add a # Source: comment to the local copy, because that would cite-to-clear a structural problem rather than fix it.

Known precedent (FIXED in L-156 1f; kept as history): comet_visualization_shells.py lines 492-493 once hardcoded SUN_RADIUS_KM and KM_PER_AU despite KM_PER_AU already being imported, with line 602 deriving SUN_RADIUS_AU from the two local copies. Those lines now carry the fix comment recording the removal -- a reader sent to find shadow constants there will find the repair, not the defect. Same failure class as the close_approach_data.py stale-copy bug that originally motivated test_constants_provenance.py.

### A Breadcrumb Must Not Cite [CRITICAL]

Citations attach at BLOCK level over a thirty-line lookback (in
`constants_new.py`, since v2.28, over the row's own comment run
instead), and `SOURCE_PATTERNS` counts `# Source:`, `# Ref:`, a bare `https://` URL,
`doi`, `arXiv` and agency names (IAU, JPL, NASA, ESA, NIST, NOAA...) as
citations. All of that is in the section above. The consequence is not
obvious and it bites in one specific place.

**An honest "unsourced, pending research" note cannot carry its own
candidate references.** Put the papers next to the value and the scanner
reads them as that value's citation, and the unit ends up looking better
sourced than it is -- which is the wrong-but-cited failure, rebuilt
deliberately by someone trying to be careful.

So the code carries a HANDLE and nothing else:

```python
# Review-note: two figures for this boundary's variation, and the
# Review-note+: papers that may support them, are held in L-253 --
# Review-note+: unsourced, unused, deliberately not restated here.
```

The figures, the DOIs and where each actually came from live in the
ledger row, which is searchable by handle, holds "pending sourcing" as a
native state, is RICE-scorable against everything else, and sits outside
the audit entirely. The trail is preserved at zero cost to the
denominator.

(Tony's ruling, 2026-08-26. Founding case L-253: `EARTH_D660_DEPTH_KM`
carried a real, correctly transcribed reference to Ishii et al. 2019 --
true of the 660 km depth, and not the source of either figure in the
note beneath it. That paper is about the discontinuity's sharpness.)

## Extend a Boundary Before Adding a Path [QUALITY]

**Before building a new provenance feature, ask whether it can be
expressed by extending a data boundary that already exists, rather
than by adding another checking path.**

The reason is a measurement rather than a preference. By August 2026
the verification infrastructure had a larger state space than a person
can hold in mind at once, and the project had more epistemic
INFRASTRUCTURE than epistemic COVERAGE: Tier-1 findings stood at 289
and were rising, because every improvement to the scanner's reach
exposed claims that had been invisible rather than sound. Machinery
that grows faster than the coverage it produces stops being read, and
a check nobody reads is a check that cannot fail.

Three shapes the extension usually takes, in the order to try them:

- AN EMITTER over a structure the run already builds. L-207's citation
  prompt reads the Table the checker assembles for its numerical
  layers and writes a second artifact from it -- no second parse, no
  new verdict class, no routing change.
- AN ADAPTER converting a new input into the structure the existing
  layers already read. The JSON worksheet reader (L-202) is the
  precedent: it synthesizes the same Table the markdown parser
  produces, so match, integrity, drift and verdict all ran unchanged
  against a format that did not exist when they were written. The
  alternative -- a second checker for JSON returns -- is the parallel
  pipeline this project has a rule about.
- A FIELD on a record that already travels. Cheaper than a new record,
  and it arrives everywhere that record already goes.

The rule does NOT forbid a new path. It requires that the question be
asked out loud and the answer written down, because the failure mode
is not one bad decision. It is a dozen locally reasonable ones, each
adding a layer nobody would have approved as a whole.

State the honest cost of the extension too. L-207 gives the checker a
second artifact type, and two outputs are more surface than one. That
was weighed and accepted; what it avoided was a second reader of the
corpus.

**And the test that comes after.** Once the machinery can answer the
question it was built for, the default question stops being "what does
the provenance system need next" and becomes "which outstanding claim
can this now settle." Stated so it can fail: the next provenance
feature should be one an actual RUN exposed the need for, not one a
design conversation invented.

(Proposed by an external review, 2026-08-18, and adopted by Tony the
same day. Marked QUALITY rather than CRITICAL because no failure has
yet shown it load-bearing -- it was adopted from a prediction, and the
tiers move on evidence.)

## Uncited Goes to the Ledger, Not the Bin [QUALITY]

When a claim outside the current slice has no citation, the disposition
is a DOCUMENTED LEDGER ROW for later sourcing -- not deletion.

Fetched-vs-Recalled's third branch (remove the claim and note the gap)
governs a claim that cannot be sourced against any authority. It does
not govern a claim nobody has sourced YET. Those are different states
and treating them alike destroys content that is merely waiting its
turn.

Per the braid: ONE ledger row per CLASS, never one per instance, so the
backlog grows by kinds rather than by counts.

**Before recording anything as uncited, check whether it is cited
ELSEWHERE in the same file.** The scanner reads a fixed lookback window,
so a real citation two hundred lines away reads as absent. A run of bare
string globals can sit far below the Source comments that cover them,
and the remedy there is to ATTACH the existing citation, not to drop the
sentence.

(Tony's ruling, 2026-08-27: "not eliminated -- documented for citation,
just not today." Worked case: `solar_visualization_shells.py` carries 26
Source blocks, 22 of which already name their store constant, while six
display-string findings 250 lines below them read as uncited. Tree-wide
the display-string class is 284 Tier-1 findings holding 553 claims,
which is why it is recorded by class and worked in slices.)

## A Computed Position Prints What Its Errors Earn [QUALITY]

A position worked out at display time -- a planet's distance from the
Sun, propagated in the browser from served elements to the minute the
room was opened -- is not a store row and has no `# Figures:` line. Its
count comes from its errors, and two of them bound it:

- **Drift.** How far the worked-out position may have moved from what
  JPL Horizons itself would give: the builder's measured rate, in
  degrees per day, times the days since the elements' date, taken as a
  distance at the body's distance.
- **The source's own accuracy.** How well JPL knows where the body is
  at all. A store row per group, served to the page on the object's
  entry.

**The display prints to the Report test's place (The ceiling, Report)
for the LARGER of the two**, each unit placed by its own error, never
finer than a floor the display states (whole kilometres in the Solar
System room), and never fewer than one figure. Tony's ruling,
2026-10-01: "use whichever is larger". Drift alone measures how well
the page reproduces Horizons, not how well Horizons knows the planet,
and it printed Pluto's distance to ten figures where JPL knows it to
several thousand kilometres. A body with no source-accuracy row yet
prints by its drift and SAYS so in the display, in words the display's
owner approved, and the words appear exactly when the row is absent so
the two cannot disagree. The asteroids are that case until each body's
own uncertainty is fetched (L-399).

This applies to every computed position a display prints, in the
gallery and the orrery. The Solar System room is the first built
(gallery/solar_system_figures.js, checked by
documentation/smoke_solar_system_figures.js, gallery repo). The
orrery's own position hovers are one ledger class, recorded and not
chased (The Braid).

### An Accuracy Stated in Words Is Stored as the Place It Reports To

Some sources state an accuracy only in words. JPL's 2014 ephemeris
report (Folkner et al., IPN Progress Report 42-196, abstract) says the
terrestrial planets' orbit uncertainties are "a few hundred meters",
Jupiter and Saturn are known to "tens of kilometers", and Uranus,
Neptune and Pluto to "several thousand kilometers". There is no number
to store, and choosing one -- 3,000 km, say -- puts in the store a
value the source never printed: a `# Source:` over a number nobody
measured, one layer out.

**Store the place.** Run the Report test over every value the words can
mean. Where they all give one place, that is the row. Where the words
could give two, take the coarser -- the tie rule of The ceiling,
extended -- so the row never claims finer than the words allow.

- "a few hundred meters": 0.2 to 0.999 km all report to whole
  kilometres -> 1 km.
- "tens of kilometers": 10 to 15 km report to tens, 16 to 99 km to
  hundreds -> 100 km.
- "several thousand kilometers": 2,000 to 9,999 km all report to
  ten-thousands -> 10,000 km.

The tempting reading is the place the words NAME -- thousands for
"several thousand". It claims +/- 500 km where every value the words
allow is nearer +/- 5,000, a factor of ten finer than the source. That
was the session plan of 2026-10-01; this rule replaced it the same
day, and Tony confirmed it.

**The row.** Value: one unit of the place, in the unit the source
names. `# Status: declared` -- the pick of the place is ours by this
rule; the words are the source's -- with a reason that names no
authority. `# Figures: exact -- declared construction:`, naming the
words and the range checked, and no print count unless a display
prints the row. `# Read:`, `# Source:` and `# Ref:` as for any row the
source was opened for. The three DE430 rows in `constants_new.py` are
the worked case.

**The display uses half a unit of the place** as the source's error,
which by the Report test gives back exactly that place; the larger of
that and the drift then sets the print, as above.

(Tony's ruling of the larger error, 2026-10-01; this method confirmed
by him "as recommended" the same day, L-398. Built by orrery patch
patch_L398_1_accuracy_rows_and_skills_20261001.py.)

## A Simple Error a Check Finds Is Fixed and Reported [QUALITY]

Tony's ruling, 2026-10-01 (L-395): "simple errors such as the Apophis
naming discrepancy should be fixed and reported." A check that finds
one does not stop at listing it.

**Simple** means one right answer, settled by an outside source or by
the file's own evident intent, with no drawing or modelling choice in
it: a link to a search page where the body's own page exists, a stray
space inside a quotation, a missing full stop, a field written twice, a
document example that no longer says what the code does.

**Fixed** means in the same patch as the work that found it. **Reported**
means the patch's output and the session record name each fix by what
it changed, so nothing is corrected silently.

**Not simple, so it comes to Tony:** two right answers (Apophis is both
99942 and 2004 MN4; the one-definition rule then decides it, and the
patch says so), anything that changes what is drawn or how, and removing
words a person wrote with a meaning in them. The objects mirror refuses
to delete a person's words for the same reason.

**A number in a served description** is sourced or comes out, because a
description has no place for a `# Source:`. It stays when a page the
project trusts states it and the read is recorded in the ledger
(Apophis's 2029, NASA's Apophis Facts page, read 2026-10-01); otherwise
it is removed (the Pluto-Charon barycentre's 6.39 days).

**Beside The Braid.** The Braid governs findings OUTSIDE the slice being
worked: recorded, one row per class, not chased. This governs findings
INSIDE it. A discovery run that exists to list -- the first Horizons
cross-check -- still lists, apart from the simple errors, which it
fixes and names.

## Examples Go Stale Like Values [QUALITY]

**A worked example in a skill is a claim about the codebase, and it
decays the same way a constant does.**

This skill taught the chromosphere drawn at 1.1 solar radii as its model
of a declared visualization boundary, for eleven days after the code
promoted that exact value to the physical figure. A skill loads every
session and is normative, so a stale example there is worse than a stale
line in a plan document: it teaches the retired state as the pattern. A
session read it and reported the retired value to Tony as current.

When a bump touches a section, re-read its examples against the file.
When a value moves, grep the skills for it in the same patch. This is
The Correction Does Not Travel, applied to the skill layer.

## The Goal State

**The push gate is Tier-1 = 0 ON THE ACTIVE BUILD PATH** -- the
files the project is currently building. As of August 2026 that is
the interactive gallery build path (Tony ratified 2026-08-05;
recorded in L-184). The scope MOVES with the work: when
Earth-science visualization work resumes, those files become the
gated path in turn.

**Global Tier-1 = 0 is the destination, not the current gate.** It
was suspended, not retired. At 206 Tier-1 findings a global gate
blocks every push forever, and a rule nobody can obey stops being
read as a rule at all. The global number is approached by clearing
paths as they go active -- which is why the gate is written
active-path rather than pinned to one named path.

Do not enforce the global form on a push outside the active path,
and do not read a bare "Tier-1 = 0" anywhere in this project as
the global form unless it says so. (Tony's ruling 2026-08-11, on
Fable audit finding F1: this skill and the protocol's manifest row
carried the global gate for a week after the ratification narrowed
it, while Tony pushed five times in one evening against it. A gate
that is routinely and correctly ignored is worse than a wrong
number -- it teaches the reader to ignore gates.)

**Where the path is read from (v2.28, L-414).** The active build path
is what leaves the orrery, read from the two files the maintenance run
rewrites before the scanner runs: `data/constants_export.json` (its
rows: the constants_new.py rows the website is served) and
`data/objects_export.json` (its objects: the celestial_objects.py
entries it serves). That is The Gate Binds at EXPORT made countable,
and it settles where L-184 left the path undefined: no import walk and
no hand list. An exported row computed from other rows is not scored
itself; its inputs are, where they are typed. A file-by-file measure,
such as L-184's Artifact-2 list, is not what the figure counts. When the
exports grow, the path grows with them, by construction.

A clean audit can rest on honest
removals: "Tier-1 = 0" does not imply "every claim sourced" -- it can mean
unsourceable claims were correctly stripped pending real sourcing. Record
which. The scanner must stay maintainable with accepted false positives,
not require regular manual intervention.


## Clearing a Flagged Claim (the only two moves)

1. Cite to where the data ACTUALLY came from, or
2. REMOVE the claim and NOTE the gap.

Never cite-to-clear. A # Source: over recalled data passes the check while
asserting a provenance that does not exist -- wrong-but-cited is worse than
uncited, because the citation suppresses the suspicion that would catch it.
A blank with a flag is honest; an unsourced assertion is not.


## Scanner Mechanics (not obvious from the output)

- Flags by NUMERIC token (number + unit) via NUMERIC_CLAIM_RE. The unit
  vocabulary covers physical units (AU, km, deg, K, masses, radii, time
  units...) AND humanitarian units (people, persons, percent, %).
- **A row in `constants_new.py` is read through its OWN COMMENT RUN**
  (v2.28, L-414): the comment lines directly below the assignment, up
  to the first blank line or line of code, and a run directly above it
  only when a blank line, or the top of the file, fences that run off
  from the code before it. A run wedged between two packed rows belongs
  to the row above, because this file writes citations below. Nothing
  is read across a blank line. So a row's own Source line counts however
  far down its Figures block pushes it, and a neighbour's never counts.
  The shadow detector's own-citation predicate reads the same run, so
  the two cannot disagree. A section-header citation does not cover the
  rows under it; each row carries its own, as The Status Line requires.
- **Everywhere else the window still applies.** A display string, or a
  constant in another module, is cited only by a `# Source:`-form
  comment WITHIN the LOOKBACK WINDOW of the flagged token, or by its
  enclosing block's citation. In-string "Source:" prose and distant
  comments do NOT count. A real citation outside the window, or in the
  wrong form, reads as uncited. The string extractor's window is pinned
  separately, in test_extractor_pins.py.
- **A declared row is not scored** (v2.28, L-414). A `# Status:
  declared` line, or `declared pending`, in a row's own run, with the
  reason written down, makes the row DECLARED: no rung, no tier, never
  Tier-1, named under Declared Rows in the audit. The reason is a
  `# Declared:` line, or the words after `--` on the Status line itself,
  which is where the Status Line grammar puts a pointer and where this
  skill's own example writes one. A bare ledger handle there is not a
  reason. A row that says declared and gives no reason is scored as any
  other row and named as reasonless. Worked cases: the three solar-wind
  rows (a `# Declared:` line) and M3_PER_KM3 (the Status line).
- **The gate-path figure is printed by name** (v2.28, L-414). Every run
  ends with a GATE PATH line: the Tier-1 findings on what leaves the
  orrery (The Goal State says where that is read from), each named by
  file and row, with what was examined to reach the figure. The
  maintenance run's summary quotes that line. An export the scanner
  cannot read makes the figure UNKNOWN, never 0, and an exported row it
  did not score is named as a blind spot. The run history records the
  names, so one finding cleared and another gained shows at an equal
  count. Its pins are test_row_run.py.
- File inclusion is role-driven (L-078): a module's display strings are
  extracted when its module_atlas.py ROLE_MAP role is in NARRATIVE_ROLES
  ({data, scenario, rendering, rendering/shells, computation}), OR its
  name is in the legacy narrative_files allow-list, OR it is a
  *_visualization_shells file. The allow-list is additive (a safety net)
  until ROLE_MAP is complete. A coverage-gap check reports modules the
  gate cannot classify -- resolve those by adding the Role:/Domain: tag to
  the module's own docstring, not by editing the scanner and not by
  hand-adding a ROLE_MAP entry (since L-163 Phase 3, ROLE_MAP is a
  generated mirror of those tags; the next module_atlas.py run overwrites
  anything hand-added).
- Loads data/provenance_exceptions.json for accepted residuals
  (suppression checks both context_text and raw_value). Run from a tree
  WITHOUT that file (e.g. a bare /mnt/project/ snapshot) and the count
  OVER-REPORTS. The confirming re-run is Tony-side, where the exceptions
  file lives.
- False positives get provenance_exceptions.json entries, not code
  workarounds.
- **A patch predicts the scanner's CHANGE, not its total** (v2.27,
  L-371). Where a patch says what the run should print, it states how
  the Tier-1 count, and the findings it names, should move. The total
  differs between machines -- the sandbox and Tony's differed by one
  on 2026-10-04 -- and the patch script is itself scanned while it
  sits in the root folder, until it is moved to documentation/.

## Report Domain Classification (Findings by File / File Type)

Since July 2026, `PROVENANCE_AUDIT.md` breaks findings down two ways ahead
of the per-tier detail: **Findings by File** (every file with a finding,
tier counts, sorted worst-first) and **Findings by File Type** (the same
data rolled up by subject-matter domain).

Domain is a *report-only* grouping -- it answers "what part of the project
is this," not "what does this module do" (that's module_atlas.py's
ROLE_MAP, a different axis entirely; a module's functional role and its
domain are independent). Domain classification never affects which files
get scanned or how a finding scores.

Six domains: **orrery** (solar system bodies, orbital mechanics, core
app -- also the default catch-all), **earth_science**, **gallery**,
**stars** (stellar neighborhood, exoplanets, HR/planetarium), **utilities**
(genuinely cross-domain shared helpers), **dev_tools** (audit,
diagnostics, one-shot infra). The last two didn't exist before this round
-- they were split out, with the four-domain original (orrery, earth
science, gallery, stars) proving too coarse for files that don't belong to
any single subject-matter area.

Mechanics: `MODULE_DOMAIN_MAP` (a module-name-to-domain dict) plus
`classify_domain()` in provenance_scanner.py. Unmapped files default to
`orrery` and are tracked and surfaced in a "Domain coverage gap" note in
the report -- mirroring the existing ROLE_MAP coverage-gap pattern -- so a
new file with findings doesn't silently drift into the wrong bucket
forever. Extend `MODULE_DOMAIN_MAP` directly (not a heuristic) when a new
file needs a home; explicit mapping was chosen over name-pattern guessing
because domain assignment involves real judgment calls (several file
categorizations were confirmed with Tony directly rather than inferred).

**Gallery will usually read near-zero.** The gallery ASSEMBLER pipeline
(resolver.py, cache_reader.py, gallery_studio.py, json_converter.py,
render_orbits.py, etc.) lives in the separate tonyquintanilla.github.io
repo, entirely outside this scanner's reach. Only gallery-adjacent files
that live IN the palomas_orrery repo (currently just social_media_export.py)
can ever populate that domain here. Do not read a 0 there as "gallery has
no provenance debt" -- it means "gallery isn't scanned from here."

## Fetched vs Recalled -- the working procedure

Data from authoritative pipelines: trusted. Data from Claude's training
memory: verify or source -- and there is a THIRD branch: if a claim cannot
be sourced against an authority, REMOVE it and note the gap. Never embed
lookup tables from training memory. Tony's professional default: prefer
removing an unsourceable claim over citing it incorrectly.

Where a value is genuinely UNKNOWABLE (fixed by an input the model cannot
recover -- a rotation phase, an instantaneous azimuth): show the ENVELOPE
of possibilities as the honest object, and SAY SO in the hover where a
shape is approximate. Faking an unknowable value is the same failure
class as citing over recalled data. (Full treatment: resident protocol,
Show the Envelope.)

## Composed vs Transcribed On-Layer Text

For user-facing factual sentences (KMZ framing text, cards, briefings),
split by how the words get authority:
- TRANSCRIBED tier: the source's own words, lifted and attributed. Safe
  by construction.
- COMPOSED tier: sentences we write because no single source line says
  them. These get the strict treatment: BUILD the sentence in generator
  code with every numeric token carrying a `# Source:` comment within the
  scanner's lookback -- never pasted as a finished string into a template,
  and never living only inside an output artifact (a .kmz) where the
  scanner cannot see it. It must be scanner-visible at the construction
  site and clear by TRUE sourcing. A composed sentence that cannot be
  sourced does not ship.

## Report to the Figures You Have [QUALITY]

**Compute at full precision. Report to the significant figures the least
precise input supports.** The two halves are separate and a careless
reader can make them contradict each other, so they are stated together.

Rounding a derived constant in code introduces error AND creates a
rounded second store of a value that lives elsewhere, so the derivation
stays symbolic:

```python
EARTH_GEOSTATIONARY_RADIUS_KM = (EARTH_GM_KM3_S2 / EARTH_ROTATION_RATE_RAD_S ** 2) ** (1.0 / 3.0)
# Figures: 7 -- set by EARTH_ROTATION_RATE_RAD_S (7.292115e-5, 7)
# Derived: (398600.4418 / 7.292115e-5^2)^(1/3) = 42164.17 km
```

Significant figures govern REPORTING: every quotient stated in a
comment, a hover string or a tooltip carries no more figures than the
row's `# Figures:` line declares. The count is a field, not prose, so
the next reader does not re-derive it and a checker can read it;
`references/figures.md` says how the field is written and counted.

**A subtraction is governed by decimal PLACES, not significant figures.**
`6371.0 - 660` is good to TENS, because its 660 km input is good to
tens, so 5710 and not 5711.

The failure this catches is quiet. Stating `0.8953994` when the inputs
support `0.8954` is not a small error in the last digits -- it is six
digits the value was never entitled to, and it reads as a measurement.
(Tony's ruling, 2026-08-26, after exactly that appeared in a table.)

**Before writing or checking a `# Figures:` line, deriving a value, or
printing a number in a display, read `references/figures.md`.** It
holds The Figure Count Is a Declared Field: Rules 1 to 8, the declared
construction, The ceiling and its Report test, and the print count of
an exact row. Its checker, `test_derived_figures.py`, judges the
declarations on derived rows even in a session that never opened the
file. It does not judge measured rows or what a display prints; those
depend on this pointer being followed (L-418).

### The Store Carries the Verified Figure [CRITICAL]

**Where a source gives a verified figure more precise than the stored
value, the store carries the verified figure. Rounding happens at the
reporting step, never at rest.**

The section above governs how many figures a hover, tooltip or comment
STATES. This governs what the store HOLDS, and the answer is every
figure the source supports.

A rounded value at rest is a second, less precise store of a number that
already exists -- the same failure as a shadow constant, one digit at a
time. It also reads as a measurement to everything downstream: the
served cache copies it, the assembler draws it, and no layer below the
orrery knows it was rounded.

**The tell is a value whose own comment names a figure more precise than
the value beside it.**

```python
RADIATIVE_ZONE_AU = 0.7 * SOLAR_RADIUS_AU
# Visualization boundary; rounds the helioseismic tachocline at ~0.713
```

The store recorded that it was rounding, and rounded anyway. Held from
first writing until 2026-08-29, in a value drawn on a public page.

**How many figures is set by the source's uncertainty, not by taste.**
0.713 +/- 0.003 supports three decimal places. Adopting a later,
tighter figure from a different work is not a precision improvement --
it changes which work the row cites, and that is a re-sourcing with its
own access check.

**Two neighbouring cases are NOT this one**, and applying this rule to
them would be wrong:

- **A pick from a range** is a declared choice and stays one. The range
  carries the citation; the pick carries its reason. Adding digits to a
  midpoint does not make it measured.
- **A visibility stylization** promotes on its own terms, when the
  physical value becomes drawable -- not because it had too few digits.
  The chromosphere's 1.1 went to 1.002875 for that reason, on
  2026-08-16.

The question this rule answers is method, not judgement: it resolves the
same way next month, for a different constant, in a different file. It
does not go to Tony. (His ruling, 2026-08-29, sending exactly that
question back: "we established the rule that significant figures where
verified should be used.")

## Cross-Checked Lines in the Store

The procedure for sending a value to other models for an independent
check -- the worksheet prompt, the verdicts that come back, and the
`# Cross-checked:` and `# Resolved:` lines that record them -- is the
skill provenance-cross-check. Load it when preparing a cross-check or a
relay prompt, or adjudicating a return. The two rules below stay here
because they fire on ordinary edits: whenever a value or a citation
that carries a cross-check is changed.

### A Cross-Check Retires With Its Value or Its Citation [CRITICAL]

A `# Cross-checked:` leg certifies one value against one citation on one
date. When either the value or the citation is replaced, the leg is
STRIPPED in the same patch, and the reason is recorded in the block.

Two ways this fires, and the store carries a worked case of each:

- **The value moved.** `ALFVEN_SURFACE_RADII` went 18.8 to 19.7 on
  2026-08-19 because 18.8 was an altitude used as a heliocentric radius.
  The two legs dated 2026-08-02 had certified 18.8 and were stripped
  with it: a check of the old value is not a check of the new one.
- **The citation went.** `HELMET_CUSP_RADII` held its value while its
  entire citation stack was removed on 2026-08-20 after an independent
  nine-source read. Its two legs went with the citations: a cross-check
  of a citation that no longer exists grants credit for nothing.

Leaving the leg standing is cite-to-clear wearing a checker's name. It
passes the scanner while certifying something that is no longer in the
file.

Record the removal in the block with its reasoning, because a removal
leaves no trace otherwise and the next reader should not have to
re-derive why a constant is uncited.

### Retired: `# Verified: April 2026 via Gemini fact-check`

This format is RETIRED. Do not add it; replace it on sight during a
cross-check batch. It records that a model looked, and nothing else --
no authority, no worksheet, no date that means anything, nothing a later
session can re-check. A `# Cross-checked:` line carries all four: the
authoritative source (not the model's name in the source position), the
model that ran the check, the worksheet on disk, and the ISO check date.

The stamp is worse than absent, because it stops the next reader from
looking. A `# Verified: April 2026` line sat over Eris's Hill sphere
while it read 9.4 Mkm against a correct ~14.3 Mkm -- a 34% error under a
verification stamp.

Census re-measured at `7f4a2f9f` (2026-08-27): 42 remaining --
shell_configs.py 14, earth 13, jupiter 9, comet 6. Unchanged since
`1e60c783`. Disposal is not a separate deletion patch: the status
pass REPLACES each stamp with a real `# Status:` line as it passes
through, which records what the stamp was actually worth instead of
leaving a blank. Zero in the five Batch 1 modules and zero in Mars,
which were cleared as those batches landed. (Two came out of
shell_configs.py with the Mercury and Moon body headers in the geometry
follow-up, from 16.) The rest clear in Batch 2.

## Field Notes

The field notes are lessons, not rules, and they are in
`references/field-notes.md`. Read them when a scanner count or an audit
result surprises you, or before reporting a value as unverified.
