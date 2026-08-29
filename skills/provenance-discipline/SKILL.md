---
name: provenance-discipline
description: Provenance and citation discipline for the Paloma's Orrery project. Use whenever running or discussing provenance_scanner.py, reading PROVENANCE_AUDIT.md, clearing Tier-1 findings, adding or reviewing # Source: citations, editing provenance_exceptions.json, embedding constants or numeric/factual claims in orrery display strings or data modules, or preparing a GitHub push (the gate is Tier-1 = 0 on the active build path, and it binds at EXPORT from the orrery). Also use when composing on-layer or user-facing factual text for any orrery visualization. Do not use for projects other than Paloma's Orrery.
fires_when: Scanner runs, audits, citations, constants, pre-push (Tier-1 = 0 on the active build path)
---

# Provenance Discipline

Skill version: 2.10 | Cut from palomas_orrery @ 071a0a65 (v2.10),
earlier @ a263f73d (v2.9), @ 7f4a2f9f (v2.8), @ 3faa72a0 (v2.7),
@ f603be3 (v2.6), @ 731066f (v2.5), @ 6b99ace (v2.2),
@ 00219d9 (v2.1), @ eb77c83 (v2.0), @ cdcdb4b (v1.9)
| August 29, 2026
v2.10 adds The Store Carries the Verified Figure [CRITICAL] under
Report to the Figures You Have, which governed REPORTING and left
the stored value uncovered. Founding case: RADIATIVE_ZONE_AU held
0.7 beside its own comment saying it rounded 0.713 -- the store
recording that it was rounding, and rounding anyway, in a value
drawn on a public page. The rule is narrowed in the same breath
against the two cases it would damage: a pick from a range stays
a declared choice, and a visibility stylization promotes when the
physical value becomes drawable rather than for want of digits.
Tony's ruling, 2026-08-29, and the reason it is a SKILL rule and
not a decision: it resolves the same way next month, for a
different constant, in a different file. Handle L-258.
v2.9 moves the gate UPSTREAM, from serving to export, on Tony's
ruling of 2026-08-28. 2.8 put it where the harm lands; 2.9 puts it
where a check can still run. `provenance_scanner.py` exists only in
the orrery repo, and `gallery_cache_builder.py` lives in the gallery
repo and scores nothing, so a gate at serving sits downstream of the
last checker in existence and across a repository boundary. The WHY
is unchanged and the WHERE is separated from it explicitly, so the
gate cannot drift back on the reasoning that publication is where a
visitor is harmed. One section rewritten, nothing else touched.
v2.8 adds nine sections and revises four passages, from Tony's
rulings of 2026-08-27 and the two independent Mode 7 reviews of the
same date. The Gate Binds at SERVING [CRITICAL] moves the binding
point from drawing to publication. The Access Standard [CRITICAL]
makes reachability a precondition of a citation -- no paywalls.
The Status Line [CRITICAL] has each value declare its own provenance
state so the scanner reads instead of inferring. Measured Is the
Goal, Declared Is the Fallback [CRITICAL] carries the range rule.
The Exhibit Requirement [CRITICAL] makes a verdict without a
quotation UNVERIFIED. A Cross-Check Retires With Its Value or Its
Citation [CRITICAL], Observations Are Sourced Facts [CRITICAL],
Uncited Goes to the Ledger [QUALITY], and Examples Go Stale Like
Values [QUALITY] complete the set. Revised: the exhibit's reader,
Gemini's book access (demoted to lead generation), the
two-annotation criterion for V_CROSS_CHECKED (retired -- it measures
concurrence), and one stale worked example. Handle L-256.
v2.7 adds three sections from Tony's rulings of 2026-08-26, each of
them a gap this skill had rather than a refinement of something it
said. One Value, One Home [CRITICAL] states positively what No Shadow
Constants only prohibited, and extends it to prose and to dead code.
Report to the Figures You Have [QUALITY] had no home in any skill.
A Breadcrumb Must Not Cite [CRITICAL] records why an honest
"pending sourcing" note cannot carry its own references (L-253).
Founding case for the first two: Earth's four interior hover strings
typed their boundary figures for months beside a radius_fraction that
disagreed with them by up to 297 km, and nothing here covered it.
v2.6 adds The Two-Dispatch Rule [CRITICAL] under Model Roles in the
Competitive Pattern -- L-217, after a Mode 7 review prompt asked two
model legs to answer Part A before reading Part B, which neither could
do and neither answer could be distinguished on.
Source: project_instructions_v3_29.md Part 3 (Provenance Audit, Fetched vs
Recalled) + food insecurity build handoff + scanner source at HEAD. v1.1
adds the report domain-classification mechanics, the Review-Repair
Protocol (promoted from documentation/provenance_audit_handoff_v4.md),
and field notes from the F1 provenance-cleanup groundwork session (July
2026): the by-file/by-file-type report breakdown, a self-referential
scanning quirk, and a stale-audit-doc near-miss. v1.2 updates the
role-driven-inclusion bullet for L-163 Phase 3: a coverage gap is
resolved by tagging the module's own docstring, since ROLE_MAP is now a
regenerated mirror rather than a hand-maintained dict. MODULE_DOMAIN_MAP
and classify_domain() are unaffected and remain hand-maintained. v1.3
adds No Shadow Constants [CRITICAL]: local copies of constants_new.py
values must be deleted and replaced with proper imports -- a frozen copy
bypasses the citation chain and drifts silently, same failure class as
citing over recalled data. v1.4 rewrites Review-Repair Protocol step 2:
cross-checking is the competitive pattern (same worksheet, independent
models, Tony compares), not one model reviewing another's output.
v1.5 adds Model Roles (tested roles for Claude, GPT, Gemini, Fable in
the competitive pattern -- emerged from the Mars and constants_new.py
cross-check sessions, August 2026), two worksheet types (value
verification vs citation verification), the Cross-checked annotation
format, and the Batch Worksheet Workflow. v1.6 adds two rounds to that
workflow (blind source lookup and the Fable consistency audit), the
model-credit convention, the retirement of the `# Verified:` stamp
format, Geometry Constants as First-Class Claims, and three field notes
-- all earned in the L-156 Phase 2 Batch 1 cross-check and the Fable
shell-consistency audit, August 3-4, 2026. v1.8 adds Worksheet First,
Annotation Second (an annotation naming a worksheet that does not exist
is cite-to-clear in the annotation's own format) and the field note that
an evidence artifact is filed as received -- both earned August 10, 2026,
when a recovered worksheet proved an annotation true that the session had
already talked itself into calling fabricated.
v1.9 narrows The Goal State to the ACTIVE BUILD PATH gate Tony
ratified 2026-08-05 (L-184), keeping global Tier-1 = 0 as the
stated destination rather than the firing rule. The skill had
carried the retired global gate for a week; caught by Fable's
document-layer claim audit, finding F1, August 11, 2026.

v2.0 (August 12, 2026) replaced the annotation grammar: checker first,
optional ` -- <source>` clause, and the retired source-first order now
REFUSED as `legacy_source_first` rather than reconstructed. The old
order was ambiguous by construction -- a source carrying its own
publication year ate the check date, so the model name landed outside
the checker identity and two annotations by two DIFFERENT models read
as one checker written twice. All 134 lines were migrated. The
store-binding check lives in skills_index.py, which asserts that every
annotation example in every SKILL.md parses as the scanner reads it --
placed there because it runs at the moment a skill changes, which is
the moment the drift is introduced.

v2.1 (August 13, 2026) extends Worksheet First, Annotation Second with
two clauses about what the worksheet has to CONTAIN, and specifies the
worksheet table schema and verdict vocabulary at the prompt so the
evidence arrives usable. Earned August 12-13: two annotations in
constants_new.py credited a worksheet for checks it explicitly did not
perform, and one cited worksheet was prose a tool cannot read. Tony's
ruling -- we do not have to accept and interpret incomplete or
malformed answers -- is the second clause, and the session that
produced the evidence can be reopened to finish the job.

v2.2 (August 13, 2026) defines DERIVED, which v2.1 listed in the
verdict vocabulary without ever saying what it meant, and separates
two things the send-back rule had run together. A row that is
INCOMPLETE goes back to its originator. A row that is COMPLETE and
disagrees with the code is a FINDING and comes to conversation,
because the disagreement may be a convention mismatch rather than an
error in either place. Earned August 13 on the Eris and Pluto Hill
sphere rows, where checkers computing at semimajor axis disagreed
with code computing at perihelion and nobody had done bad
arithmetic. Tony's rulings: PARTIAL and APPROX return
unconditionally, and an adjudication is recorded with its reason so
the next run does not re-raise it.

The resident protocol carries the two governing principles as CRITICAL
gates: Fetched-vs-Recalled (a citation is a provenance claim that must be
TRUE; source-then-cite, never cite-to-clear) and Show the Envelope of the
Unknowable. This skill carries the working procedures and the scanner's
mechanics. If this skill and the resident gates ever seem to disagree, the
gates win -- flag it.


v2.4 (August 17, 2026) carries three changes, all earned the same day.
The annotation grammar now accepts a `.jsonl` or `.json` worksheet
reference as well as `.md` (L-204). The `.md` condition did two jobs:
it required the parenthetical to name a FILE rather than free prose,
which is the anti-gaming half of L-186 and does not move, and it
pinned the only worksheet format that existed in August 2026. The JSON
return format (L-202) landed 2026-08-17, and a returned verdict could
then be built, carried, filled, checked and routed -- and refused by
that one condition when somebody wrote it back into the code. Found by
an integration test, not by a reading. The Resolved Leg section is new
(L-200): a record-only leg saying which returned verdict caused an
edit. And The Visibility Convention is new (L-203), promoting a
one-off ruling about the request builder into the general rule it was
always an instance of.

v2.5 (August 18, 2026) adds Extend a Boundary Before Adding a Path,
the rule an external review proposed on 2026-08-18 and Tony adopted
the same day. It lives here rather than in the resident protocol
because it fires while a provenance feature is being designed, which
is when this skill loads. L-207, the citation prompt, was the first
item checked against it rather than assumed to pass.

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

A clean audit can rest on honest
removals: "Tier-1 = 0" does not imply "every claim sourced" -- it can mean
unsourceable claims were correctly stripped pending real sourcing. Record
which. The scanner must stay maintainable with accepted false positives,
not require regular manual intervention.


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

## Clearing a Flagged Claim (the only two moves)

1. Cite to where the data ACTUALLY came from, or
2. REMOVE the claim and NOTE the gap.

Never cite-to-clear. A # Source: over recalled data passes the check while
asserting a provenance that does not exist -- wrong-but-cited is worse than
uncited, because the citation suppresses the suspicion that would catch it.
A blank with a flag is honest; an unsourced assertion is not.


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
end are all in the store and all correct for their rows -- the helmet
cusp takes the top so the drawn cusp does not understate the helmet,
the gravitational influence takes the midpoint, the core takes the low
end. The rule is that **the pick is a declared choice and its reason
lives on the row.**

This supersedes the weaker Batch 1 convention -- best-sourced single
value in code, range in the description -- for any row where the range
is genuinely the sourced object. The weaker form leaves the range in
prose, where it cannot be interpolated and drifts from the number beside
it.

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

**Inside a dict, the status line attaches to the DICT when its entries
share one kind and one source**, and an entry that differs carries its
own line, which overrides. This does not reopen the per-value ruling of
2026-08-13: that ruling addressed annotations sitting inside a
thirty-line proximity window, where a parser cannot distinguish group
intent from accident. A status line on a dict is structurally scoped,
not merely near.

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

## Review-Repair Protocol for Cross-Checked Annotations

**No model is its own verifier.** Clearing findings and earning
Cross-checked annotations is a multi-model competitive process, not
something any single AI does solo:

1. **Claude (orchestrating instance) preps a worksheet prompt.** Group
   claims by file, present each as a numbered claim with its current
   value and citation, and flag anything suspicious. The prompt is
   SHA-anchored (`built on <SHA> at <URL>`), includes the source code
   being checked, and specifies the job type (see Worksheet Types below).
   The prompt states the table schema and the verdict vocabulary
   explicitly -- an unspecified format is how eight of them happened.
   Claude does NOT propose corrected values -- only what needs checking.
2. **Tony sends the same prompt to Claude, GPT, and/or Gemini
   independently.** Same prompt, independent answers. Tony compares.
   Convergence builds confidence; divergence flags where to dig. This
   is NOT one model reviewing another's output -- all work from the
   original claims, not from each other.
3. **Claude (orchestrating instance) compares the worksheets** and
   produces a convergence/divergence report. Tony decides on
   divergences.
4. **Claude builds a transactional patch** with the confirmed fixes
   and Cross-checked annotations.

**Why the worksheet format matters for every checker.** The same
"fetched not recalled" rule that governs Claude's citations governs all
cross-checkers. A known failure mode is fabricating authority from
training memory when the output format allows ungrounded narrative. The
structured worksheet does not -- it forces primary source citations per
cell. Constrain the format, and the discipline follows.

### Model Roles in the Competitive Pattern

Tested and validated in the Mars and constants_new.py cross-check
sessions (August 2026). These are demonstrated strengths, not
assumptions.

| Model | Demonstrated strength | Use for |
|-------|----------------------|---------|
| Claude (Opus) | Derivations, citation-shape errors (catches when a source cannot contain the claim as written), honest about limitations (marks UNVERIFIED rather than bluffing) | Primary checker: papers, web sources, derivations, structural analysis |
| GPT | Papers with DOIs, explicit derivations with worked math, thorough web sourcing, catches date/year errors in citations | Primary checker: independent of Claude, complementary source selection |
| Gemini | Domain knowledge, structural/philosophical dialogue. Book content is LEAD GENERATION only -- see the demotion below | Domain review, tiebreaker when primaries diverge |
| Fable | Large-context comprehensive review, far-reaching audits across many files, pattern recognition at scale | Cross-codebase audits, manifest generation, bulk review when scope exceeds a bounded session |

**Default two-leg pattern:** Claude + GPT independently. Covers papers,
web sources, derivations, NASA/JPL data.

**Gemini escalation:** When either primary leg marks items UNVERIFIED
due to book citations, or when Claude and GPT diverge on domain-knowledge
questions. Also effective as a third independent leg when sent the same
prompt (tested: all three models received the same constants_new.py
remaining-items prompt; complementary coverage emerged naturally).

**Fable escalation:** When the scope of review exceeds what a bounded
session can hold -- auditing an entire manifest, reviewing cross-file
consistency, or pattern-matching across the full codebase. Not for
per-claim worksheet work (Opus handles that), but for the architectural
view that requires seeing everything at once.

**Demoted 2026-08-27: Gemini's book access is LEAD GENERATION, not a
clearing route.** This skill previously recorded that Gemini could
"open the books" -- reaching Carroll & Ostlie and Golub & Pasachoff
content neither Claude nor GPT could -- and routed book citations to
it. Under The Access Standard that is a model's ACCOUNT of a book, not
the book. It has the same standing as any other free-form model query:
useful for finding where a claim lives, never citable on its own.

The pilot supports the demotion independently. The Gemini leg returned
a quotation on 1 percent of 92 rows and a locator on 28 percent.

Book citations now route to RE-HOMING first -- find an accessible
authority carrying the same result -- and to Tony's Scholar or Books
queue only when none exists.

### The Two-Dispatch Rule [CRITICAL]

When a prompt carries Claude's own proposal AND asks the reviewer for an
independent derivation, the two halves go out as TWO PHYSICAL
DISPATCHES: Part A alone, answer collected, then Part B. A single
document that instructs a model to answer one half before reading the
other is a check that cannot fail -- both halves arrive in one context,
the model cannot comply, and nothing in any answer distinguishes a
reviewer who complied from one who could not.

Stating the instruction anyway is WORSE than omitting it, because the
instruction makes the prompt look controlled. If two dispatches are not
worth the round trip, drop the claim and ask only for critique.

(Origin, L-217, 2026-08-19. The L-214 review prompt asked both legs for
Part A before Part B. Fable disclosed that the ordering was unexecutable
and named it as a check that cannot fail. GPT's answer corroborated it
without meaning to: its Part A opens "my prediction before consulting
the measured result is" and then states the measured result to the
digit. The prompt was authored in the session that dispatched it, so the
resident CRITICAL gate never fired on its own author.)

### Worksheet Types

Two types, same format, same competitive pattern, different job:

**Value verification:** "Is this number right?" The checker independently
researches each claim against primary sources, without seeing what the
other checker found. Catches wrong values behind correct-looking
citations. Used for shell modules (Mars was the first: bow shock 1.5
should have been 1.64, Hill sphere 324.5 should have been 320).

**Citation verification:** "Does the cited source actually contain this
value?" The checker goes to the stated source and confirms the value
appears there at the stated precision. Catches citations that point at
sources that don't contain the claimed value -- right number, wrong
provenance. Used for constants_new.py (IAU B3 cited for Mars/Saturn/
Uranus/Neptune radii it doesn't define; heliopause arithmetic used 123
AU where the source says 121.6).

Both types use the same worksheet table format:

| # | Claim/Constant | Code value | Your value | Source | Value correct? | Citation correct? | Notes |

**State this schema IN THE PROMPT, with the verdict vocabulary.** Eight
different column layouts exist across the worksheets on disk because no
prompt ever specified one, and a tool that must read them all needs a
header-role registry to do it. That is the consumer paying for a
producer that was never pinned.

A verdict cell carries EXACTLY ONE of these tokens and nothing else,
with the reasoning in Notes. **The tokens are scoped to their column.**

    Value correct?     YES  NO  APPROX  UNVERIFIED
    Citation correct?  YES  NO  PARTIAL  DERIVED  UNSOURCED  UNVERIFIED

Two verdicts per row, never conflated. `Value correct?` asks whether
the number is right; `Citation correct?` asks whether the named source
publishes it. A right number under a wrong authority is value-YES and
citation-NO, and that split is the whole reason for two columns.

**The scoping is the substance, not the formatting.** APPROX qualifies
a VALUE -- the number is right to a stated tolerance. PARTIAL qualifies
a CITATION -- the source supports some of what is claimed. They were
commissioned that way and they are not synonyms; listing all of them on
one flat line lost the distinction, and a checker reading the flat list
cannot tell which word answers which question.

UNSOURCED belongs to the citation column: the named source does not
publish this value at all, as against NO, which is the source
publishing a DIFFERENT value. Both send the row to conversation; the
distinction survives because it changes the repair.

**Vocabulary version.** A worksheet states which vocabulary it was
written against, on its own line near the top:

    Vocabulary: v2 (2026-08-13)

Seventeen worksheets on disk predate any settled vocabulary and carry
no such line. A tool reads the line rather than guessing from a date,
and an absent line means pre-v2 -- which is a fact about the file, not
a defect in it.

`Code value` is what the checker read from the code at the prompt's
SHA. It is not redundant with `Your value`: comparing it against the
code NOW detects a value edited after its check, which no diff-based
tool can see once the edit is committed.

PARTIAL means the claim is genuinely half-right -- a source that
publishes the value at lower precision than the code carries.
A checker that STOPPED BEFORE FINISHING writes UNVERIFIED, and the
Notes say what blocked it: a context limit, a paywalled paper, a
conversation that ended. An honest UNVERIFIED is a usable answer; a
PARTIAL standing in for one is not.

DERIVED answers the CITATION question, not the value question. It
means no source publishes this number because the number is computed,
so there is no citation for that column to be right about. It can
pair with any value verdict, including NO. Reading it as a third
member of the PARTIAL/APPROX family is the error to avoid: those two
qualify a value, DERIVED describes where one came from.

A DERIVED row is COMPLETE when it names its inputs, shows the
arithmetic, and the arithmetic closes. Then L-158 governs: the
derivation logic has cleared its own check, and the value inherits
the rung of its WEAKEST INPUT. That is not a completed check on its
own -- it hands the question to the premise. Worked example, the
Moon's Hill sphere in lunar radii: 60,000 / 1737.4 = 34.53 closes
exactly, and the 60,000 km premise under it reads APPROX and
UNSOURCED, so the derived figure is worth precisely that and no
more. A DERIVED row showing no work is incomplete and goes back.

The distinction matters because the same file can need both: a shell
module's display text needs value verification while its `# Source:`
comments need citation verification.

### Quoting a Worksheet Is Transcription, Not Interpretation [CRITICAL]

A verdict token decides. Prose informs. Any tool reporting on a
worksheet may QUOTE what the checker wrote, and may never READ that
prose to decide anything.

The rule exists because of what the alternative turned out to be. Asked
who consults the Notes column, the answer was: nothing. The checker
reads Notes only to work out which row is about which value, and never
reports a word of it. So "the reason goes in Notes" meant the reason
went nowhere -- a record that cannot fail, because nothing opens it.

Quoting is safe when four properties hold. Two of them were being
violated in the L-192 checker's first report, which is how the rule got
written:

1. **Verbatim and DELIMITED.** The quoted cell is visibly separated
   from the tool's own words. Without this they fuse: a real finding
   read `reads NO -- wrong authority -- wrong authority for a value
   that may still be right`, half checker and half template, and no
   reader can tell which half is evidence.
2. **Untruncated**, or cut only at a mechanical limit with an explicit
   marker. A live finding cut mid-word at forty characters --
   `'Partial. Main interaction/loss claims ma'` -- reads as a
   transcription and is not one.
3. **Keyed to the MATCHED row only.** No row, no quote. A tool that
   goes hunting for a nearby note when the match failed has crossed
   into interpretation.
4. **Never fed to a decision.** No verdict, no routing, and no score
   reads quoted prose. If removing the quoting changes any outcome, the
   rule is already broken.

A compound cell -- a recognized token followed by prose -- classifies
by the token, is FLAGGED as compound, and its remainder rides the
quoting path verbatim. Reading the token and discarding the rest is the
tool deciding a qualification does not matter, which is interpretation
by omission.

### Cross-Checked Annotation Format [CRITICAL]

The checker comes FIRST. The grammar is fixed:

```
# Cross-checked: <checker> <ISO date>[ -- <source>] (<worksheet>)
```

The parenthetical names a worksheet FILE. Accepted formats are `.md`,
`.jsonl` and `.json` (L-204, 2026-08-17); anything that is not a
filename -- free prose, a bare word, a description of where the
evidence lives -- is refused as `unsupported_reference_format`. The
shape rule is the anti-gaming half of L-186 and does not move. The
format list widened when the JSON worksheet format landed (L-202),
because a return that can be checked and routed and then not cited is
a loop with no last inch.

```python
# Source: Vignes et al. 2000, GRL 27, 49 -- subsolar bow shock 1.64 R_M
# Cross-checked: Claude 2026-08-01 -- Vignes et al. 2000 (worksheet_claude_mars_visualization.md)
# Cross-checked: GPT 2026-08-01 -- Vignes et al. 2000 (track1_gpt_independent_worksheet_mars_visualization.md)
```

**Checker, then date, then the source it checked, then the worksheet.**
The checker names who did the work. The ISO date is the check date. The
optional ` -- <source>` clause names the authority that was checked.
The parenthetical points to the evidence on disk.

**Why the checker leads (L-186, 2026-08-12).** It used to trail, and the
source led. The parser reads the first four-digit year on the line as the
check date and everything before it as the checker -- so a source carrying
its own publication year ate the date, and the checker name landed after
it and never entered the identity at all. Two annotations by two DIFFERENT
models then read as one checker written twice: `duplicate_identity`, and
the claim scored V3 with the reason "cross-check incomplete (1/2 models)"
while both legs had in fact been done. Nineteen units were in that state.
Putting the checker first makes the parser's rule TRUE rather than
accidental, and adds no heuristic anywhere.

A line in the retired order is now REFUSED as `legacy_source_first`, not
repaired. The parser cannot tell a publication year from a check year, so
it declines to try.

The source clause is optional. `# Cross-checked: Gemini 2026-04-15
(worksheet.md)` is complete.

#### The Resolved Leg [QUALITY]

A record-only leg naming the worksheet row whose verdict caused an
edit, and the ledger handle that authorized it (L-200, 2026-08-17):

```
# Resolved: worksheet_pilot.jsonl constants_new.py::ROCHE_LIMIT_RADII::c1 -- citation refuted, Source replaced (L-204)
```

Without it, an annotation edited in response to a verdict is
indistinguishable from an unexplained edit, and the only record of
which is which lives in a handoff.

**It cites the KEY, never the row number.** `row_id` is assigned by
position when a request is rendered and renumbers whenever the corpus
changes. `module.py::enclosing::label::cN` is stable. This is the same
failure the ledger already records for per-handoff item numbers.

**It is deliberately invisible to the request.** The leg is not in the
builder's `CONTEXT_LEGS`, so a row dispatched a second time cannot see
what the last one concluded. A context leg would anchor a second
reader the way a Claude-derived figure anchors Gemini.

**The checker checks LINKAGE, not meaning.** Three existence facts: the
leg parses, it names a worksheet row that exists, and that row's
citation verdict was one requiring an edit. A leg pointing at a row
that does not exist is refused -- an edit attributed to a verdict
nobody can find is an unexplained edit wearing a citation. Whether the
edit was the RIGHT one stays with a reader.

#### Worksheet First, Annotation Second [CRITICAL]

If no worksheet file exists on disk, the annotation does not get written.
Save the exchange as a `.md` in `documentation/` first, then write the
annotation against the real filename.

The parenthetical is a PATH, and a path that resolves to nothing asserts
an audit trail that cannot be walked. That is cite-to-clear wearing the
annotation format -- and it is worse than a bare `# Source:` line,
because the annotation's whole promise is that the evidence is on disk.

Two failure shapes, and they need different fixes:
- The check happened but was never filed. Recoverable: find the exchange,
  file it as received, repoint the annotation. Eight annotations in
  `constants_new.py` were in this state and were repaired on August 10
  once Tony recovered the worksheet.
- The check never happened. Not recoverable by filing anything. Strip the
  annotation, and re-run the claim through the workflow.

Do not write the annotation planning to file the worksheet afterwards.
The gap between the two is where the first shape comes from.

**The worksheet has to SAY THE THING.** Existence is clause one, not the
whole rule. An annotation names a checker who verified THIS value; the
worksheet must record that check, for that value, with a verdict that
amounts to a completed one.

Two live failures, both found August 13, 2026, and both the same shape:

- `BENNU_RADIUS_KM` -- worksheet row G10 reads UNVERIFIED, "Not
  checked." The annotation credits Claude with a cross-check against
  Nolan et al.
- `ARROKOTH_RADIUS_KM` -- the worksheet said the OLD value was wrong.
  The value was then corrected against Keane et al. 2022, a paper the
  worksheet never opened, and the annotation still credits the
  worksheet.

**A worksheet that says a value is WRONG is not a worksheet that says
the replacement is RIGHT.** Those are different claims resting on
different evidence. The correction is the moment this enters: someone
fixes a value against a new source, and the existing annotation rides
along unchanged. Re-check the annotation whenever the value under it
moves.

**Incomplete or malformed evidence is sent back, not interpreted.**
[Tony's ruling, August 13, 2026.] If a worksheet is prose a tool
cannot read, or a row shows no work, the answer is a better worksheet
-- not a cleverer parser and not a charitable reading.

**PARTIAL and APPROX return to the originator for completion.**
[Tony's ruling, August 13, 2026.] Unconditionally, and without first
asking why the row is qualified. Neither token earns a leg toward the
cross-checked rung, and neither is interpreted into one.

The move that makes this cheap: **reopen the session that produced it.**
Conversations persist and can be continued. The session holds the
research context, so asking it to finish costs a fraction of starting
over, and the addendum lands in the format the tools expect. Measured
the first time this was tried: of seventeen unresolved rows, nine
closed, including one that had blocked on nobody opening the cited fact
sheet.

Ask for a NEW file rather than an edit. The original worksheet is the
record of what was known on its date, and rewriting it makes it assert
something it did not say at the time.

#### A Complete Row That Disagrees Is a Finding [CRITICAL]

Send-back fires on incompleteness. It does NOT fire on disagreement.
A row that names its inputs and shows its arithmetic has already
given everything needed to settle the question; returning it asks for
what we already hold and discards a usable finding.

So a mismatch between a value and its own evidence is reported LOUDLY
and routed to conversation. No tool assigns the cause. Three outcomes
are live and none of them is the default:

- CONVENTION MISMATCH. Both derivations are arithmetically correct
  and answer different questions. Nobody is wrong; the code has to
  say which question it answers.
- THE CODE'S NUMBER IS WRONG. The worksheet wins; the value changes.
- THE WORKSHEET'S DERIVATION IS WRONG. The code wins.

**Every outcome is confirmed in conversation unless the rule is
already stated** [Tony's ruling, August 13, 2026]. A stated rule
settles the next occurrence without a second conversation, which is
the whole reason for writing it down.

The Hill sphere is the worked example, and it is a convention
mismatch. The standard Hill radius carries an eccentricity factor,
a(1-e)(m/3M)^(1/3), so what it returns is the PERIHELION Hill radius.
Checkers computing at semimajor axis dropped the (1-e) and got a
larger number: for Eris at e~0.44 that is 14.2 Mkm against 8.0 Mkm,
which reads as a gross error and is not one.

**The adjudication is recorded with its reason, in the place the next
reader will hit it.** Two shapes already work in this codebase:

- For a convention, the reader-facing text. Eris's shell text now
  states both figures and says the shell draws perihelion, so the
  next checker who computes 14.3 Mkm reads the answer before raising
  it.
- For a changed value, a `# Corrected:` line in the comment block
  saying what moved and why. Pluto's block carries one recording that
  radius_fraction 4685 drew a 5.57 Mkm shell under text claiming
  5.99 Mkm.

A verdict with no reason is not an adjudication. It is the same run
repeated later by somebody who does not know it already happened.

For derived values where the source is a computation, not a lookup:
```python
# Source: Derived from NASA NSSDCA Mars Fact Sheet (a, GM_Mars)
#         via standard Hill approximation, Claude Opus 5 2026-08-01
```

For a value that is a declared drawing choice rather than a
measurement, name the choice and its reason on the row:
```python
# Declared: top of the sourced 2-4 R_sun range, so the drawn cusp
#           does not understate the closed-field helmet
```

(The chromosphere-at-1.1 example that stood here until 2026-08-27 was
retired in the code on 2026-08-16, when that shell was promoted to the
physical 1.002875. See Examples Go Stale Like Values.)

**Retired 2026-08-27: two annotations no longer earn V_CROSS_CHECKED.**
The scanner required two `# Cross-checked:` lines with distinct
(identity, reference) pairs. That measures CONCURRENCE, and concurrence
is what failed on `ALFVEN_SURFACE_RADII`: two legs agreed on a wrong
value and the dissenting leg was the one carrying evidence. The rung
stays, and stays deliberately earned rather than gated; what earns it
is an EXHIBIT fetched and read, per The Exhibit Requirement. Both
independent Mode 7 reviewers reached this conclusion separately on
2026-08-27. The scanner change is a build with its own handle.

### The Exhibit Requirement [CRITICAL]

**A verdict without a quotation is UNVERIFIED, whatever the verdict
says.**

A leg that read the document can quote it. A leg that recalled restates
the citation it was given. That difference is a property of the RETURN,
not of the claim, so detecting it needs no domain knowledge and no
second opinion.

The worksheet schema gains two required fields:

- **quote** -- verbatim text from the named source containing the claim.
- **locator** -- where in the document: DOI, bibcode, section, table,
  page, or a resolvable URL.

State both IN THE PROMPT alongside the verdict vocabulary, and say that
a row without them will be recorded UNVERIFIED regardless of its verdict
token. A missing exhibit is not weighed, not averaged against another
leg, and not read as weak agreement. It is silence, and silence is the
correct output for a leg that did not read the source.

**The quotation is a routing aid and a recall tripwire. It is NOT the
clearance.** It tells us which document and where to look, and a leg
that cannot produce one is the leg that was recalling.

**The evidence of record is the source text READ IN CONTEXT**, with the
locator and the retrieval date written into the worksheet. This is
Fetched vs Recalled applied one layer up -- to verification itself
rather than to values.

**Division of labour.** Claude fetches anything reachable directly:
arXiv, NASA ADS, agency documents, open journals. Tony fetches only what
Claude bounces off -- paywalled pages, Google Scholar, Google Books. That
queue should be short, and re-homing under The Access Standard is what
keeps it short.

**Leg counts.**

- **Citation verification: ONE leg with an exhibit is sufficient**,
  because the exhibit is then fetched and read rather than believed.
- **Value verification: TWO legs**, and only where a value must be FOUND
  rather than confirmed -- no source at all, or a citation check
  returned refuted and a replacement is needed.
- A leg returning no exhibit does not reduce the count. It contributes
  nothing.

**Measured, not assumed** (pilot returns at `6ceb3f76`, 138 rows):

| leg | rows | carried a quotation | carried a locator |
|---|---|---|---|
| Claude Opus 5 | 23 | 78% | 100% |
| GPT | 23 | 60% | 73% |
| Gemini | 92 | 1% | 28% |

The leg with no exhibits is the leg that confirmed `ALFVEN_SURFACE_RADII`
at 18.8 four times over, once describing it as a heliocentric distance
when it is an altitude. Its own notes field reads "Recollection of the
Parker Solar Probe 8th encounter results." Two legs concurring would
have kept the wrong number; the exhibit test separates them without
anyone knowing the answer in advance.

**Two limits, stated so they are not read past.** This is one dispatch.
It shows quote-presence separates a reading leg from a recalling leg; it
does NOT show quote-presence predicts correctness row by row inside a
single leg. And it makes Claude the verifier of record, which
concentrates trust in the component that has actually been failing. The
mitigation is partial and real: the document is present in the window
rather than recalled, and its URL and date go into the worksheet so
anyone can re-open it. What Tony can still catch is whether the document
is REAL and is the RIGHT one -- which is the fabrication failure this
project has suffered. What he cannot catch is a misreading of a real
paper.

**Enforcement is a build, not prose.** This section states the rule. A
checker that refuses a row lacking `quote` or `locator` is a separate
item and needs its own handle, because a rule stated only in a skill is
a check that fires when somebody remembers it.

(Tony's ruling, 2026-08-27, on the failure he has actually seen: models
guessing and inventing. "Silence is better." Reader and clearance
revised the same evening: "Honestly I don't intend to go looking for
quote text. Better would be links that I can go fetch for you to read.")

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

### Batch Worksheet Workflow

For scaling the competitive pattern across many modules:

1. **Claude prepares worksheet prompts** (one per file, SHA-anchored,
   with the file's claims extracted from the scanner findings).
2. **Tony sends each prompt to Claude + GPT independently.** Multiple
   file prompts can go in one session per model.
3. **Tony uploads both worksheets; Claude compares** and produces the
   convergence/divergence report per file.
4. **Tony decides on divergences.** Unresolved divergences go to Gemini
   or GPT as tiebreaker.
5. **Claude builds a transactional patch** (fixes + annotations) per
   file or per batch.
6. **Gemini gets targeted prompts** only for items both primaries
   marked UNVERIFIED (typically book citations).
7. **Blind source lookup**, when models converge suspiciously or diverge
   in a way that smells like anchoring. Every earlier round shows each
   model the value already in the code, which invites confirming it. So
   run a round with the expected value REMOVED: present the claim text
   only, and ask each model to source it cold. Batch 1 ran 8 items this
   way; 4 reached a primary source and 4 came back honestly unsourced --
   and it is what caught Mercury's sodium tail at 10,000 R_M (observed
   range is ~120 to ~1,400) and re-attributed Eris's 875 K core.
   A "NOT FOUND" from a blind round is a RESULT, not a failed round: it
   is how a claim earns removal rather than a softer citation.
8. **Fable consistency audit**, after the patches land. Full-codebase
   pass checking visualization CONSTANTS against display TEXT, and
   mapping every duplicated value for the single-source-of-truth
   migration (L-181). This catches what the per-claim worksheet
   structurally cannot: the worksheet asks "is this claim right?", never
   "does the geometry still agree with it?" Batch 1 corrected text and
   citations across five modules and left six `radius_fraction` values
   drawing the pre-patch physics. Prompt:
   `documentation/PROMPT_fable_shell_consistency_audit.md`; report:
   `documentation/FABLE_shell_consistency_audit_report.md`.

This keeps Gemini's book-access strength aimed where it matters rather
than diluted across routine web-checkable claims.

### Model Credit in Annotations [PRACTICE]

Name the model that produced each check in the `# Cross-checked:` line.
This is not vanity -- it is the record of WHICH LEG found the finding,
and it is the only way to see afterwards whether the legs were actually
independent.

```python
# Source: Hauck et al. 2013, JGR Planets 118:1204 -- core radius 2020 +/- 30 km
# Cross-checked: GPT 2026-08-03 -- Hauck et al. 2013 (batch1_blind_source_lookup_gpt.md)
# Cross-checked: Gemini 2026-08-03 -- Hauck et al. 2013 (batch1_tier2_cross_check_gemini.md)
```

**Two Claude passes are ONE leg, not two.** Same training data, same
priors, correlated errors. The same holds for two passes of any single
model. Two `# Cross-checked:` lines satisfy the scanner's V2 scoring
mechanically, but they only mean what they say if the identities differ.
Before writing the second line, check that the worksheet it names was
produced by a different model than the first.

And before citing any worksheet, confirm it exists on disk and contains
the finding. A parenthetical pointing at a plausible filename is the
citation-layer version of cite-to-clear.

Full multi-session history of this protocol (numbered Tier-1 items closed
via web_search + Gemini cross-check): `documentation/HANDOFF_provenance_
phase1_v17.md` and related handoffs. The originating rationale:
`documentation/provenance_audit_handoff_v4.md`.

## Scanner Mechanics (not obvious from the output)

- Flags by NUMERIC token (number + unit) via NUMERIC_CLAIM_RE. The unit
  vocabulary covers physical units (AU, km, deg, K, masses, radii, time
  units...) AND humanitarian units (people, persons, percent, %).
- A citation must sit WITHIN the LOOKBACK WINDOW of the flagged token and
  use the `# Source:` comment form. In-string "Source:" prose and distant
  comments do NOT count. A real citation outside the window, or in the
  wrong form, reads as uncited.
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

**THE SCOPE BOUNDARY, and it must be stated in the same breath.**
MEASURED values migrate. DECLARED DRAWING PARAMETERS do not:
`n_points`, `marker_size`, `opacity`, `mesh_resolution`, an angular
marker step. Those stay where they are drawn. That is L-240's split, and
without it "only store" reads as hauling 25 and 3.4 into
`constants_new.py`, which buries the values that matter under the ones
that do not.

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

## Report to the Figures You Have [QUALITY]

**Compute at full precision. Report to the significant figures the least
precise input supports.** The two halves are separate and a careless
reader can make them contradict each other, so they are stated together.

Rounding a derived constant in code introduces error AND creates a
rounded second store of a value that lives elsewhere, so the derivation
stays symbolic:

```python
EARTH_INNER_CORE_RADII = EARTH_INNER_CORE_KM / EARTH_EQUATORIAL_RADIUS_KM
# Derived: 1221.5 / 6378.1366 = 0.19151 -- 5 significant figures, set
# Derived+: by the numerator. Report no more than that.
```

Significant figures govern REPORTING: every quotient stated in a
comment, a hover string or a tooltip, with the figure count named beside
it so the next reader does not re-derive it.

**A subtraction is governed by decimal PLACES, not significant figures.**
`6371.0 - 660` is good to units, so 5711 and not 5711.0.

The failure this catches is quiet. Stating `0.8953994` when the inputs
support `0.8954` is not a small error in the last digits -- it is six
digits the value was never entitled to, and it reads as a measurement.
(Tony's ruling, 2026-08-26, after exactly that appeared in a table.)

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

## No Shadow Constants [CRITICAL]

Modules must not carry local copies of values that exist in constants_new.py. Import through the established shim (planet_visualization_utilities) or directly from constants_new.py. A local literal that numerically matches a tracked constant is a frozen copy -- it won't follow if the source value updates, and it bypasses the scanner's citation chain even when the number is correct today.

This is the code-side complement to the scanner's build_pinned_values() check: the scanner can flag a suspicious match, but the standing rule is that these should never be introduced in the first place. When found, delete the local definition and replace it with a proper import -- do not add a # Source: comment to the local copy, because that would cite-to-clear a structural problem rather than fix it.

Known precedent (FIXED in L-156 1f; kept as history): comet_visualization_shells.py lines 492-493 once hardcoded SUN_RADIUS_KM and KM_PER_AU despite KM_PER_AU already being imported, with line 602 deriving SUN_RADIUS_AU from the two local copies. Those lines now carry the fix comment recording the removal -- a reader sent to find shadow constants there will find the repair, not the defect. Same failure class as the close_approach_data.py stale-copy bug that originally motivated test_constants_provenance.py.

### A Breadcrumb Must Not Cite [CRITICAL]

Citations attach at BLOCK level over a thirty-line lookback, and
`SOURCE_PATTERNS` counts `# Source:`, `# Ref:`, a bare `https://` URL,
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

## Field Notes

- **A missing annotation is not missing verification.** The absence of a
  `# Cross-checked:` line means no ANNOTATION. It does not mean no work.
  Verification lands in several places the annotation grammar does not
  count: a `Resolved:` leg naming the returned verdict that caused an
  edit, a `Record:` leg pointing at a source record in `documentation/`,
  a `Review-note:` block carrying an independent read, and a convergence
  report filed after a dispatch. A row can carry all four and still show
  no cross-check. Before reporting a value as unverified, read the
  block's other legs and look for its source record. Say which claim is
  being made -- "carries no cross-check annotation" and "has not been
  verified" are different statements, and the first said carelessly is
  heard as the second. (Origin, 2026-08-27: a session reported seven of
  the Sun's constants as lacking cross-checks in a way that read as
  unverified. Two of the seven were the most-worked rows in the file --
  `ALFVEN_SURFACE_RADII` had a three-model pilot dispatch behind it, and
  `HELMET_CUSP_RADII` rested on a paper Tony retrieved from NASA ADS
  himself. The annotations were absent because the earlier legs had been
  correctly stripped, which is A Cross-Check Retires working, not a gap.)

- **An evidence artifact is filed AS RECEIVED.** House style -- ASCII
  rules, naming conventions, header blocks -- applies to code and to
  documents we author. It does NOT apply to a document whose entire value
  is that someone else wrote it. A session took Tony's uploaded Gemini
  worksheet, converted its LaTeX to ASCII, stripped the markdown escaping,
  added a header block and a provenance note it wrote itself, and filed
  the result labelled as the Gemini worksheet. Tony caught it: "you have
  created a parallel unsourced worksheet not made by gemini." The corpus
  settled the question -- the existing GPT worksheet carries 115
  non-ASCII bytes and the earlier Gemini one 37, so there was no
  consistency to fix, only an assumed one. Reformatting an evidence file
  destroys the property that makes it evidence.
- **Unverified and true is still unverified -- do not over-confess.** Asked
  whether it had fabricated a `(Gemini worksheet)` annotation, a session
  gave an accurate account of its method (it had pattern-matched an
  adjacent annotation's shape without checking), then concluded from that
  the CONTENT was fabricated, called it cite-to-clear, and offered to
  strip the annotation. The recovered worksheet proved all three
  specifics it believed it had invented were true. Acting on the
  self-report would have deleted a real citation. Separate the two
  findings: the METHOD was wrong and is worth fixing; whether the CONTENT
  is wrong is a different question with its own evidence. An
  over-confession is as much a calibration failure as a denial, and it is
  more persuasive because it sounds like rigor.
- **Three wrong-paper citations survived into Batch 1 files**, each
  plausible enough to pass a reading. Mercury's crust cited "Pei" -- a
  mis-parsed GIVEN name read as a surname, so the author did not exist.
  Mercury's crust cited Sori 2018 for 35 km when Sori 2018 gives 26 --
  the cited paper REFUTED the value it was cited for. Eris's core cited
  Glein et al. for 875 K; Glein is a real author of a real paper on
  methane isotope geochemistry, but that paper does not contain 875 K,
  which comes from a different 2023 Science Advances paper. Three
  distinct ways to be wrong while looking right: a name that is not a
  name, a source that contradicts you, and a real author cited for
  someone else's number.
- A citation can be self-contradictory and still read as authoritative.
  Saturn's Hill sphere carries `# Source: ... ~91 million km / ~151
  Saturn radii confirmed` -- but 91 Mkm is ~1,510 R_S, so the two halves
  of the "confirmed" pair are a factor of ten apart, and neither matches
  the drawn value. The word "confirmed" over an internally inconsistent
  pair is cite-to-clear caught in the wild.
- **Verify the anchor SHA exists before trusting a document built on it.**
  An outbound prompt arrived anchored to a commit that was not in the
  repo -- it had been written but not pushed. The "does not exist"
  reading was correct at the moment of the check and resolved on push:
  the SHA round trip working exactly as designed, with the one failure
  mode honest and visible. Two repos in play makes this routine rather
  than exotic -- a HEAD that looks wrong may be the OTHER repo's HEAD.
  Check both before concluding anything.

- The scanner took ~10 sessions and multiple Gemini cross-checks to
  harden -- treat scanner changes as shared-CI changes with family-wide
  ripple (extending the unit vocabulary once exposed a pre-existing
  Tier-1 in star_notes.py that had been invisible).
- Fingerprint truncation was a prior scanner bug (fixed); if suppression
  behaves oddly, check fingerprints before assuming a data problem.
- Naive sums of source files can contradict the source's own published
  totals (overlapping units double-count). Transcribe headline figures;
  never compute them from parts unless the source says the parts sum.
  The full discipline for human-cost data is in earth-system-pipeline.
- Derive from known quantities; don't estimate manually.
- **The scanner scans itself, so editing provenance_scanner.py nudges its
  own self-scan numbers.** Adding a new module-level dict or descriptive
  string constant to the scanner (e.g. MODULE_DOMAIN_MAP, DOMAIN_LABELS)
  gets picked up as a claim-shaped unit in provenance_scanner.py's own
  audit entry, same as in any other file. This is correct behavior, not a
  bug -- but before assuming a total-findings delta after a scanner change
  means a real citation gap appeared somewhere in the project, check
  whether the scanner's own new code is the source of the delta first.
  (Observed July 2026: a report-formatting-only change to
  provenance_scanner.py shifted its total findings by +2, both new,
  correctly landing in the no-action tiers -- verified by diffing the
  before/after audit line by line, not by trusting the summary count.)
- **Multiple copies of PROVENANCE_AUDIT.md can exist and silently
  diverge -- verify which one you're reading.** The committed root-level
  file can go stale relative to a fresh scan (a small drift was observed
  directly: a committed doc claimed a different Tier-1 count than an
  immediate live re-run). Separately, an archived copy can sit elsewhere
  in the repo (e.g. under documentation/) dated months earlier. `cd`-ing
  into a subdirectory mid-session and not verifying `pwd` before reading
  "PROVENANCE_AUDIT.md" again is enough to silently read the wrong copy
  and draw a confidently wrong conclusion from it -- a real, self-caught
  near-miss this session. When precision matters (triage, before-citing
  a count), prefer a fresh live scan over any committed copy, and confirm
  the working directory before reading a same-named file a second time.

