# The critical path -- where we are and what stands between here and the end

**Updated August 19, 2026.** Orrery at
`9ffb9b403a7d62090b30a9acf9adbc6180a6baec`, gallery at
`ff18d3e6fa31f70a8f525df471e751d046cf14fa`. Both confirmed by live
check. First written August 16 at `227f5b2d`; the structure below is
unchanged from that version. The figures moved, and one claim
reversed: the first dispatch has now gone out and come back.

**Lands in `documentation/` as `CRITICAL_PATH_SUMMARY.md`.** Section 5a
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
scale is measured: 110 claims scored, eight of them clean.

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
run end to end.** Of 110
verification claims, eight are clean, forty-eight need to go back to
whoever filled them in, twenty need a conversation, thirty-four are
noted without a route, and twenty-four are not reachable by the scanner
at all. That is not a discouraging result -- it is the first time the
number has been knowable. Before the checker existed, the same claims
were unexamined and looked fine.

The corpus grew from 102 and the clean count nearly tripled. Neither is
a change in the world: L-198 taught the scanner to read units it could
not previously see, so claims that were always there entered the corpus
and rows that had been mis-parsed resolved.

The pilot also found two things worth acting on that no reading had
caught. `ALFVEN_SURFACE_RADII` measures from the photosphere while its
sibling `PARKER_CLOSEST_RADII` measures from Sun centre -- two constants
in one file, same spacecraft, one solar radius apart, which is a
rendering defect rather than a documentation one if that shell draws
from centre (L-209). And `STREAMER_BELT_RADII` cites a paper
inverted: the cited 6 R_sun is that paper's FLOOR, and its actual
result is a lower bound three times larger (L-210).

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
updated August 18, dispatch result added August 19. Built on
`9ffb9b403a7d62090b30a9acf9adbc6180a6baec` at
https://github.com/tonylquintanilla/palomas_orrery, gallery at
`ff18d3e6fa31f70a8f525df471e751d046cf14fa`.*
