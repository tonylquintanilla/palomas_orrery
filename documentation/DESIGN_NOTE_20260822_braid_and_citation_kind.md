# Design note -- 2026-08-22: the braid, the third part of a citation, and three dispatch fields

**Built on `96707590ba445c58066787aef03299174a8f158b` at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Gallery at `22771cac`. Written August 22, 2026 with Anthropic's
Claude Opus 5.**

This document exists because three things were settled in conversation
on 2026-08-22 and lived nowhere else. Each is a RULING with its
reasoning attached, not a status report. The mechanical work they
imply -- the Section 5a revision, the skill bumps, the builder change
-- is deliberately NOT done here: those are better done fresh against
a clean read, and each is easier once this exists.

A later session can reconstruct WHAT was decided from the ledger. It
cannot reconstruct WHY. That is what this file carries.

---

## 1. The braid -- provenance is scoped to the artifact, not a gate

**Tony's ruling, 2026-08-22. Requires a Section 5a revision to
`MASTER_PLAN_INTERACTIVE_GALLERY.md`; the readable summary follows.**

### The problem, stated as a number

Step one of the critical path is "make the orrery right." Of 107
verification claims, 8 are clean. The scanner reports 292 Tier-1
findings tree-wide. On 2026-08-22 a full session went to ONE solar
shell -- the streamer belt -- which is not in Artifact 2 and does not
block it.

At that rate the prefix does not terminate. **A precondition that does
not terminate is not a plan.** Nothing ships while it runs, and the
audit's denominator grows whenever anyone thinks of something -- which
is the exact tell the existing rule names.

### The rule that already contained the answer

`PROJECT_INSTRUCTIONS.md` Part 3, "The Artifact Bounds the Audit":
scope is what the orrery RENDERS. Closed at any commit, open over
time. That rule bounds WHICH values are in scope.

The braid extends it by one word. **Priority is what the NEXT ARTIFACT
renders.** Artifact 2 is Jupiter and Saturn with rings and radiation
belts: seven Saturn rings, four Jupiter rings, the belts. That is a
countable slice with an end, and finishing it ships something.

The general audit does not stop. It stops being a GATE.

### Step three comes first, and this is the load-bearing part

Two lines in `resolver.py` discard every ring radius one step before
anything could use them, and there is no browser code that draws a
ring at all. That work depends on NOTHING -- the data is already in
the served cache, including all seven of Saturn's rings and all four
of Jupiter's with their belts and parameters.

The master plan holds step three back to avoid locking unverified
numbers into a fingerprinted reference artifact. That reasoning is
sound and it conflates two separable things: BUILDING the rendering
layer, and LOCKING Artifact 2. Rings can be drawn without being
fingerprinted.

Doing it in that order pays for itself, and the argument is this
project's own:

> Right now the ring provenance is an audit of numbers nobody can see
> -- text checked against text. That is precisely the mode that
> produced three separate failures on 2026-08-22 (Section 2 below).
> Once the assembler draws, a wrong ring radius becomes something
> Tony's EYES can catch. The resident gate says the render is ground
> truth and the render wins when it disagrees with a code reading.
> Step three is what gives the provenance work a render to be checked
> against.

### The resulting order

1. Step three -- the rendering layer. Rings on screen, unfingerprinted.
2. Artifact 2's provenance slice -- the rings and belts, and only those.
3. Lock Artifact 2.
4. Ship.

The five steps of Section 5a DO NOT MOVE. They were confirmed
unchanged on 2026-08-16 and 2026-08-22 did not change them. What
changes is that step one stops being a gate and becomes a per-artifact
slice. That is a change to the SHAPE of the work, which is what
Section 5a is for -- hence a 5a edit rather than a ledger ruling about
execution.

---

## 2. A citation has three parts, not two: value, source, and KIND

**Proposed for `provenance-discipline`. Promotion is Tony's judgment;
recorded here with the case that produced it.**

### The case

DeForest, Howard & McComas (2014), ApJ 787:124 states that the Alfven
surface lies at least 15 solar radii up in the streamer belt and 12
over the polar coronal holes. On 2026-08-22 that figure was read at
source, corrected from a wrong 17/12.5 (Section 3), and landed on
`ALFVEN_SURFACE_RADII` as a supporting leg.

**It would score `confirmed` under every check this project owns.**
The value is right. The paper states it. The position is findable.
The identifier resolves. A clean row by every existing measure.

**And drawing a shell at 15 R_sun would still have been wrong.** The
paper says plainly that the streamer figure is set by the
coronagraph's FIELD OF VIEW and the polar one by the NOISE FLOOR. They
are instrumental floors. The number is real; the boundary is not.

Nothing in the annotation grammar or the verdict vocabulary can
express that difference. The visualization decision turned entirely on
it, and no worksheet return could have surfaced it.

### The rule

The annotations already carry VALUE and SOURCE. **KIND is what tells
you what you are allowed to DRAW.**

Four kinds, the same set now used in the dispatch fields:
- `MEASURED` -- directly observed, reported as the quantity claimed
- `INFERRED` -- derived from a light curve, an orbit, or a model
- `STATED` -- asserted in a source without derivation shown
- `NOT FOUND` -- no source states it; remove and note the gap

### Two live instances the same day

`HELMET_CUSP_RADII = 4.0` is cited to Suess & Nerney (2004), which
STATES 2-4 R_sun as established background -- the paper's own result
is an analytic stagnation-flow model. Correctly cited, and `STATED`
rather than `MEASURED`. That is why the rendered pinch is drawn SOFT
rather than sharp: a modelled boundary does not earn a knife edge.

The same paper's fast/slow wind identification is marked in its own
abstract as a reasonable ASSUMPTION. So the streamer band draws the
brightness boundary -- a coronagraph observation, uncontested -- and
attributes what it DIVIDES to Suess & Nerney as an interpretation.
Slow-wind origin is unsettled in the field. Drawing a claim asserts it
harder than writing it does.

### Why not promoted today

One rule, two instances, one session. Promotion is Tony's judgment and
one occurrence is an anecdote. Recorded here so the next instance has
something to be the second of.

---

## 3. Three dispatch fields, each answering a specific failure

**Designed 2026-08-22 for L-225 and then withdrawn with its wrapper
(Section 4). The fields survive; only the carrier changed.**

The existing dispatch already requires a resolvable identifier and a
locatable position. "Chapter 1" is not a position -- Golub & Pasachoff
was removed on 2026-08-20 for exactly that, the one return in nine
with no findable location. These three are ADDITIONS, and each traces
to a failure on 2026-08-22.

**`VERSION` -- which text was read.** The arXiv ABSTRACT METADATA at
arxiv.org/abs/1404.3235 says 12.5 and 17 solar radii. The accepted
manuscript served as the PDF under the SAME identifier says 12 and 15,
three times: abstract, Section 5, Section 6. NASA ADS and Cranmer et
al. 2016 both carry 12 and 15. This project repeated 17 across four
documents, including into live code, because two separate reads both
quoted the listing page. **A resolvable identifier is necessary and
not sufficient.** Agreement between two reads of one wrong page is not
verification.

**`METHOD` -- searched or recalled.** Some models search; some answer
from training and format the result identically. Gemini has scholar
search. The field is cheap and it separates two things that look the
same on the page.

**`LOW_CONFIDENCE` -- what the model would not bet on.** On 2026-08-22
a model asked for citations returned a list mixing one real item (a
NASA blog, carrying NO formal citation format) with a fabricated paper
attributed to a named author at a named institution, in flawless
academic format, carrying invented precision -- "4-6 hours" where the
real source says "several hours". **Formatting ran INVERSE to truth.**
A model asked to name its own soft spots sometimes does, and the cost
of asking is one line.

### The other half of the same lesson

Free-form chat with an external model is for LEAD GENERATION, and its
output is a SEARCH PLAN, never citable. On 2026-08-22 the same
free-form exchange that produced the fabrication also named Raymond,
Gibson and Jones -- and two of three pointed at genuinely useful work
despite wrong titles. Both halves are true and neither cancels the
other.

Recorded for completeness: a model asked to AUDIT the fabrication
produced a new one in the same reply, inventing the lineage "Koutchmy
& Livshits (via Suess & Nerney)". Those are independent lines to the
same morphology. Merging them destroys the redundancy that gives the
claim its weight -- the prose form of the failure the twenty
citation-inheritance tests guard against in code.

---

## 4. L-225 -- deferred, with its shape settled

**Reaffirmed 2026-08-22. This is the approach, not a workaround.**

The MAPS disintegration radius, 8.33 R_sun, is typed into
`comet_visualization_shells.py` and carries a model fact-check as its
only leg. The figure is PLAUSIBLE -- from 8.33 R_sun to a 1.23 R_sun
perihelion is roughly four hours at these speeds, matching the
NASA/LASCO statement that the nucleus was destroyed several hours
before closest approach -- but plausible is not sourced.

**The dispatch loop cannot reach it.** `comet_visualization_shells.py`
appears ten times in `PROVENANCE_AUDIT.md` and ZERO times in
`WORKSHEET_CHECK.md`. The scanner sees its claims; the worksheet
corpus does not include it. No row, no key, no row hash, nothing the
checker could route a return into.

Two ways to fix that were considered. Extending the worksheet corpus
to reach the comet module treats the symptom. **Tony's ruling: migrate
the values into `constants_new.py`, where the builder ALREADY reaches.**
`MAPS_DISINTEGRATION_RADII` and its siblings become constants; then
`worksheet_request_builder.build()` slices them as rows with hashes,
the ratchet applies, and the verdict writes back as an annotation the
scanner accepts.

**Fix the producer, not the corpus.** The shadow constant is the
defect; the unreachable row is a consequence. This is the same
migration L-181 and L-191 already track, so it is the next instance of
scheduled work rather than new work.

`patch_L225_1_dispatch_request.py` is WITHDRAWN -- a hand-written
markdown prompt is the wrong carrier for a row that is about to become
a proper one. Its four questions survive intact: perihelion distance
as the control, disintegration distance with an explicit warning not
to answer it with the perihelion, hours before perihelion, and the
kind of each.

**The perihelion is the control question and must stay in.** We know
it -- 0.005729 AU, 1.232 R_sun -- and it is exactly the quantity a
free-form answer collapsed the disintegration distance into on
2026-08-22. A leg that misses it has told us what its other answers
are worth.

Part A goes out BLIND. The prompt must not contain 8.33. That is the
two-dispatch rule and this is its case.

---

## 5. What this note does NOT do

Deliberately, and each for the same reason -- better done fresh
against a clean read than at the end of a long session:

- **The Section 5a revision.** 5a starts at line 796 of a 118 KB
  document. It is the sequencing authority for the whole project and
  the edit must reconcile the braid against every ruling 5a already
  carries. Section 1 above is the argument that edit needs.
- **The `provenance-discipline` bump** for the KIND rule (Section 2).
  One rule, two instances, one session.
- **The builder change** for L-225 (Section 4).
- **The handoff.** This note is not a handoff and does not replace one.

---

## References

L-224 (the streamer band, whose build surfaced all of this); L-210
(the withdrawn 4-6 R_sun range); L-209 (the Alfven surface and the
DeForest rehoming); L-221 (the master plan as sequencing authority --
this note is the first revision made under it); L-225 (deferred, above);
L-181 and L-191 (the shadow-constant migrations this joins);
`documentation/SOURCE_suess_nerney_2004_helmet_extent_20260821.md`;
`MASTER_PLAN_INTERACTIVE_GALLERY.md` Section 5a;
`documentation/MASTER_PLAN_CRITICAL_PATH_SUMMARY.md`;
`PROJECT_INSTRUCTIONS.md` Part 3 -- "The Artifact Bounds the Audit",
"Verify Execution, Not Appearance", "A Check That Cannot Fail Is Not
Passing", "Fetched vs Recalled".
