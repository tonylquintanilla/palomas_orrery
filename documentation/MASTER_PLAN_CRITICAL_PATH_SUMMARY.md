# The critical path -- where we are and what stands between here and the end

**Updated August 20, 2026.** Orrery at
`79729c98fd6bec8703fcc3bbc0806e6ee5226770`, gallery at
`109162bbb8d291bce615d888557498a9342d4642`. Both confirmed by live
check. First written August 16 at `227f5b2d`; the structure below is
unchanged from that version -- the five steps have not moved, only
our position along them.

Two things changed on August 20. The reconciliation queue that had
been open for two sessions is CLOSED: four rows decided, three
values changed, one held. And a claim this document carried about
`STREAMER_BELT_RADII` turned out to be wrong and is corrected below
-- it had travelled here from a session reading rather than from a
source.

**Lands in `documentation/` as `MASTER_PLAN_CRITICAL_PATH_SUMMARY.md`.** Section 5a
of the master plan and the readable snapshot both cite it by that exact
name, so it belongs in the repo before either is pushed.

Companion to `MASTER_PLAN_INTERACTIVE_GALLERY.md` Section 5a, which is
the reference version. This is the readable one.

The three documents divide like this. Section 5a is the shape of the
work. This file answers "how far to the end." The readable snapshot,
`MASTER_PLAN_INTERACTIVE_GALLERY_SUMMARY.md`, answers "what is being
tracked right now."

---

## The end goal

The Python orrery, running inside the browser, drawing the interactive
gallery.

Not a JavaScript rewrite of the orrery. The same Python, the same
computation engines, the same conventions -- delivered to a visitor's
browser through Pyodide, on a static site with no server. That was
settled and measured in July: a full cold start on an iPhone takes two
to three seconds against a threshold of fifteen.

The static gallery that exists today does not go away. It becomes the
pedagogical exhibit layer, and the interactive pages grow alongside it.

---

## The one fact that organizes everything else

**The assembler creates no data. It imports.**

There is no point downstream of the orrery where a wrong number can be
caught. Not in the nightly builder, not in the assembler, not in the
browser. Nobody down there knows what a correct ring radius is.

That single fact splits the project's data into two kinds that behave
completely differently.

**Positions look after themselves.** Every night, the builder asks JPL
Horizons directly for where each object is. A bad value cannot survive
until morning. Nothing to audit, nothing to verify, no human in the
loop.

**Everything else does not.** Saturn's ring radii, Jupiter's radiation
belt distances, atmospheric shell boundaries -- these begin as numbers
written into the orrery's Python and travel to the gallery by being
copied. Horizons is never consulted for them. If a number is wrong in
the orrery, it is wrong in the gallery, permanently, and nothing will
ever notice.

This is why the provenance work comes first. It is not a detour and it
is not a parallel project. Its target is the orrery, so that importing
from the orrery blind is a safe thing to do.

---

## The path

The pipeline runs one direction, and the work follows it.

    the orrery  ->  transport  ->  nightly builder  ->  served cache
                                                            |
                        the gallery  <-  the assembler  <---+

**One. Make the orrery right.** One home for every feature constant,
each carrying its source as data rather than as a comment somebody has
to trust. Then the verification batches, of which the gas giants are
the one Saturn and Jupiter need.

The checker, the worksheet builder and the dispatch loop are the
machinery of this step, not a step of their own. They exist because
reconciling worksheets against the code by hand does not scale, and the
scale is measured: 107 claims scored, eight of them clean.

That machinery was finished and unused for one day. A request can be
built for a chosen slice of rows, carried out as JSON, returned,
checked, routed, and written back into the code as an annotation the
scanner accepts. The last inch closed on August 18: until then a
returned verdict could be checked and routed and then refused when
somebody tried to cite it, because the annotation grammar accepted only
a markdown reference.

**The first dispatch went out the same day and came back.** Twenty-three
rows from `constants_new.py` to three models in fresh chats. Sixty-nine
answered rows, and across all of them: no unparseable line, no missing
or modified row hash, no duplicate key, no empty answer field, no token
outside the vocabulary. The JSON format needed no fallback. The loop
works.

What it found is in
`documentation/PILOT_CONVERGENCE_20260819.md`. The headline: a
prediction of 13 clear rows, written six days before dispatch, drew 17,
10 and 11 from the three legs. All three planted trap rows failed to
spring, which means the artifact conveys what it was built to convey.
Ten rows came back clean from all three models independently, and six
were flagged by all three.

**Two. Make the copy faithful.** A correct orrery is not enough while
the gallery's copy of its constants is maintained by hand. The transport
design is settled; it has not been built.

**Three. Teach the assembler to draw.** This one is independent of the
first two and could be done tomorrow -- the data is already sitting in
the served cache. Two lines in the resolver currently throw away every
ring radius one step before anything could use them, and there is no
browser code that draws a ring at all.

Fixing it today would put Saturn's rings on screen immediately. They
would just be rings drawn from unverified numbers, which is exactly what
should not be locked into a reference artifact.

**Four. Lock Artifact 2.** Jupiter and Saturn with rings and radiation
belts, fingerprinted as the reference build. It needs all three of the
above: sourced values, a faithful copy, and something that can actually
render them.

**Five. Ship, then repeat.** The first interactive solar system page,
then stars, then exoplanets and the galactic centre, then the Earth
system. Each phase ships a working page rather than waiting for the
whole thing.

---

## Where we actually are

**Done and holding.** The browser stack is proven. The scene vocabulary
is written. The nightly data pipeline runs and serves twelve objects --
including, already, all seven of Saturn's rings and all four of
Jupiter's, with their radiation belts, complete with parameters.

**Artifact 1 is locked.** Earth, alone, orbiting. It proved the
propagation maths, the reference-artifact machinery and the acceptance
process all work.

It also drew no features at all, which is how the feature path stayed
broken without anyone noticing.

**Step one is in progress, the backlog is visible, and the loop has now
run end to end.** Of 107
verification claims, eight are clean, forty-eight need to go back to
whoever filled them in, nineteen need a conversation, thirty-two are
noted without a route, and twenty-two are not reachable by the scanner
at all. That is not a discouraging result -- it is the first time the
number has been knowable. Before the checker existed, the same claims
were unexamined and looked fine.

**And on August 20 the loop closed for the first time.** The four
rows the pilot ranked as worth acting on had sat undecided for two
sessions. All four are now decided, and the shape of the decisions is
the useful part: `EARTH_EQUATORIAL_RADIUS_KM` moved to IERS
precision because its source line credited a resolution that does
not publish that many digits; `BENNU_RADIUS_KM` moved to the
OSIRIS-REx figure, which supersedes the pre-encounter radar value the
row carried; `HAUMEA_RADIUS_KM` moved to the 2017 occultation, the
only direct measurement, with the competing solution named in the
row; and `STREAMER_BELT_RADII` HELD, because the number was never
the problem. Three of the four kept their value or changed it by
less than a part in ten thousand. What changed was what the code
claims about where its numbers came from.

**Three of those four turned on material the request builder had
been dropping** (L-214). The rows carried `# Note:` lines answering
the exact question the responders spent a dispatch re-deriving, and
the builder silently withheld them because the label was outside its
vocabulary. So one of the pilot's most useful results is a
measurement of its own instrument. L-214 is designed and unbuilt,
and it is the next scheduled work.

The values were confirmed against primary sources by an independent
read rather than by asking a second model whether ours were right --
a blind read can disagree, and a confirmation request mostly cannot.
It disagreed twice.

The corpus grew from 102 and the clean count nearly tripled. Neither is
a change in the world: L-198 taught the scanner to read units it could
not previously see, so claims that were always there entered the corpus
and rows that had been mis-parsed resolved.

The pilot also found two things worth acting on that no reading had
caught. `ALFVEN_SURFACE_RADII` measures from the photosphere while its
sibling `PARKER_CLOSEST_RADII` measures from Sun centre -- two constants
in one file, same spacecraft, one solar radius apart, which is a
rendering defect rather than a documentation one if that shell draws
from centre (L-209). And `STREAMER_BELT_RADII` carried a citation that
did not support the claim attached to it (L-210).

**That second sentence used to say something sharper and it was
wrong.** Until August 20 this file reported that the row cited its
paper INVERTED -- that the cited 6 R_sun was the paper's floor being
used as a ceiling. That was a session reading, written down here as
though it were a finding. An independent source read on August 20
found otherwise: DeForest, Howard & McComas (2014) uses 6 R_sun as
the threshold at which inbound wave motion first became detectable,
which is neither a floor nor a ceiling on streamer extent, and that
paper's streamer-belt result is an Alfven surface at 17 R_sun or
more -- a result that belongs to `ALFVEN_SURFACE_RADII`, not here.
The companion citation did not carry the row either: Golub &
Pasachoff bound coronal structure at roughly 5-10 R_sun and state no
4-6 R_sun streamer range at all. So the 4-6 range in the code was
sourced to nothing. The value held at 6.0 as a declared drawing
choice, both citations were repaired, and the range was withdrawn
with a note saying why.

It is worth leaving that visible rather than quietly restating it.
A wrong claim in a summary document outlives the conversation it
came from, because the next reader has nothing else to check it
against.

**Step two is designed, not built.**

**Step three has not been started.** It is the smallest piece of work
standing between the project and a Saturn that renders.

---

## What would change the picture

An independent review by two models in August found nine structural
problems in the dispatch machinery before a single questionnaire went
out. Both reviewers, working blind, said do not send it yet. Eight are
now closed -- the first of them by a design decision that removed the
question rather than answering it. The ninth, a truncated ordinal
context window, is deliberately not exercised by the pilot, because
constants carry no ordinals and shipping a known-defective presentation
into the first dispatch would confound the thing being tested.

That is the pattern the project runs on and it is working: find the
problem while it is still cheap, in conversation, rather than after it
has been baked into a hundred worksheets and a fingerprinted artifact.

---

*Prepared August 16, 2026 with Anthropic's Claude Opus 5; figures
updated August 18, dispatch result added August 19, reconciliation
closed and the streamer-belt claim corrected August 20. Built on
`79729c98fd6bec8703fcc3bbc0806e6ee5226770` at
https://github.com/tonylquintanilla/palomas_orrery, gallery at
`109162bbb8d291bce615d888557498a9342d4642`.*
