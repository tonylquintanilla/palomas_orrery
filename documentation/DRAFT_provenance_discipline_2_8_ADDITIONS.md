# DRAFT -- additions and revisions for provenance-discipline 2.8

**Written 2026-08-27 with Anthropic's Claude Opus 5.** Orrery
`7f4a2f9f046bc00ad9e418367b42beffaff89e7b` at
https://github.com/tonylquintanilla/palomas_orrery (branch main),
gallery `1a67b00d73813a1387ff1de7b77f8175c39c0f1e` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io. Both
confirmed against the live remote.

**Companion to `documentation/DRAFT_provenance_discipline_2_8_sections.md`**
(five sections, written at `6ceb3f76`). This file carries what tonight's
rulings ADD, plus two REVISIONS to sections in that draft. Merge both
into one bump.

**This is a draft to read, not a patch.** Nothing is written into
`skills/provenance-discipline/SKILL.md` yet. The bump runs the four-link
chain -- SKILL.md, `skills_index.py`, the manifest zone, a protocol
version entry -- and cannot be verified from inside the session that
makes it, so it lands as a carried obligation for the next one.

---

# PART 1 -- NEW SECTIONS

## The Status Line [CRITICAL]

**Every value in `constants_new.py` declares its own provenance state.
The scanner reads that declaration instead of inferring one.**

One line, immediately below the assignment, using the existing `+`
continuation convention:

```
# Status: <kind> <rung> <ISO date> [-- <pointer>]
```

`<kind>` is one of three, and they are decision 18's zones:

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
HELMET_CUSP_RADII = 4.0
# Status: measured V_SOURCED 2026-08-28 -- abstract, open

CHROMOSPHERE_PHYSICAL_KM = 2000.0
# Status: measured V_SOURCED -- access untested (textbook)

SOLAR_RADIUS_AU = SUN_RADIUS_KM / KM_PER_AU
# Status: derived -- inherits SUN_RADIUS_KM, KM_PER_AU
```

**The status line must not be citable.** It carries no source text, no
agency name, no author-year, and no URL. Those live in `# Source:` and
in the worksheet. A status line that names an authority becomes a
citation for the value beside it, which is the same failure as A
Breadcrumb Must Not Cite one section over.

**The declaration is the only store, and inference is removed rather
than kept as a fallback.** If a value declares `V_SOURCED` and the
scanner also infers a rung from a nearby comment, the two can disagree,
and that is One Value, One Home violated on a property instead of on a
number. Deleting the inference is what this section buys: the thirty-line
lookback crediting a neighbour's annotation, `# Verified:` matching the
citation pattern, a bare URL in a breadcrumb scoring as a source, and
orphan section-header annotations all trace to the scanner guessing.

**Inside a dict, the status line attaches to the dict when its entries
share one kind and one source**, and an entry that differs carries its
own line, which overrides. This does not reopen the v18 per-value ruling:
that ruling addressed annotations sitting inside a thirty-line proximity
window, where a parser cannot distinguish group intent from accident. A
status line on a dict is structurally scoped, not merely near. Recorded
as a decision made under the skill's own authority rather than referred
up; veto it if the reasoning does not hold.

---

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

**When a source fails access, re-home the citation to an accessible
authority carrying the same result. Delete only when none exists.** Most
failures are re-homeable, because the values that end up in this file are
standard results that open sources also carry. `PREM` is the model: the
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

---

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

This is L-179's mechanism, generalised. `GRAVITATIONAL_INFLUENCE_AU` and
`GRAVITATIONAL_INFLUENCE_RANGE_AU` are the existing pair: the range
carries the citation and the access standard, the drawn number is a
declared midpoint, and the hover shows the envelope.

The rule is NOT which end of the range to draw. Top, midpoint and low
end are all in the file and all correct for their rows -- the helmet cusp
takes the top so the drawn cusp does not understate the helmet, the
gravitational influence takes the midpoint, the core takes the low end.
The rule is that **the pick is a declared choice and its reason lives on
the row.**

This supersedes the weaker Batch 1 convention -- best-sourced single
value in code, range in the description -- for any row where the range
is genuinely the sourced object. The weaker form leaves the range in
prose, where it cannot be interpolated and drifts from the number beside
it.

Rows this reaches today: `CORE_AU`, `INNER_CORONA_RADII`,
`HELMET_CUSP_RADII`, `INNER_LIMIT_OORT_CLOUD_AU`. It is a structural
change to four rows and therefore implementation work, scheduled by the
braid -- not part of a status pass, which changes no values.

---

## Examples Go Stale Like Values [QUALITY]

**A worked example in a skill is a claim about the codebase and decays
the same way a constant does.**

This skill taught the chromosphere drawn at 1.1 solar radii as its model
of a declared visualization boundary, for eleven days after the code
promoted that exact value to the physical figure. A skill loads every
session and is normative, so a stale example there is worse than a stale
line in a plan document: it teaches the retired state as the pattern.

When a bump touches a section, re-read its examples against the file.
When a value moves, grep the skills for it in the same patch -- this is
The Correction Does Not Travel, applied to the skill layer.

---

# PART 2 -- REVISIONS TO THE `6ceb3f76` DRAFT

## Revise: The Exhibit Requirement

Two changes. The rule survives; the reader and the clearance move.

**The quotation is a routing aid and a recall tripwire, not the
clearance.** The `6ceb3f76` draft has Tony reading the returned quote
and judging whether the claim is in it. He has ruled that he will not:
"Honestly I don't intend to go looking for quote text. Better would be
links that I can go fetch for you to read."

So the quotation keeps both jobs it does well -- it tells us which
document and where to look, and a leg that cannot produce one is the leg
that was recalling, which is exactly what the pilot measured. It stops
being the evidence of record.

**The evidence of record is the source text read in context**, with the
locator and the retrieval date written into the worksheet. This is
Fetched vs Recalled applied one layer up, to verification itself rather
than to values.

**Division of labour.** Claude fetches anything reachable directly --
arXiv, ADS, agency documents, open journals. Tony fetches only what
Claude bounces off: paywalled pages, Scholar, Books. That queue should
be short, and re-homing under the Access Standard is what keeps it short.

**The one-leg rule survives, with a different reason.** Citation
verification takes one leg carrying an exhibit, because the exhibit is
then fetched and read rather than believed. Value verification keeps two
legs. A leg returning no exhibit still contributes nothing.

**The residual, stated rather than hidden.** This makes Claude the
verifier of record, concentrating trust in the component that has
actually been failing. The mitigation is partial and real: the document
is present in the window rather than recalled, and its URL and date go
into the worksheet so anyone can re-open it. What Tony can still catch is
whether the document is real and is the right one -- which IS the
fabrication failure this project has suffered. What he cannot catch is a
misreading of a real paper.

## Revise: Model Roles in the Competitive Pattern

**Gemini's book access becomes lead generation, not a clearing route.**

The current table records that Gemini can open Carroll & Ostlie and
Golub & Pasachoff where Claude and GPT cannot, and routes book citations
to it. Under the Access Standard that is a model's account of a book,
not the book. It has the same standing as any other free-form model
query: useful for finding where a claim lives, never citable on its own.

The pilot supports the demotion independently -- the Gemini leg returned
a quotation on 1% of 92 rows and a locator on 28%.

Book citations now route to re-homing first, and to Tony's Scholar or
Books queue only when no accessible authority carries the result.

## Retire: the two-annotation criterion for V_CROSS_CHECKED

The scanner requires two `# Cross-checked:` lines with distinct
(identity, reference) pairs. That measures CONCURRENCE, and concurrence
is what failed on `ALFVEN_SURFACE_RADII`: two legs agreed on a wrong
value and the dissenting leg was the one carrying evidence.

The rung stays, and stays deliberately earned rather than gated. What
earns it becomes evidence -- an exhibit fetched and read -- rather than
a second model agreeing. Both independent reviewers reached this
conclusion separately on 2026-08-27.

---

# WHAT THIS DOES NOT COVER

**The checker that enforces any of it.** A rule stated only in a skill
fires when somebody remembers it. The worksheet schema gaining required
`quote` and `locator` fields, the status-line parser, and the scanner's
inference removal are three builds with their own handles.

**The status pass itself.** Beta on the Sun's nineteen plus one dict,
then the whole store, both status-only. Value changes are implementation
and the braid schedules them.

*Prepared 2026-08-27 with Anthropic's Claude Opus 5.*
