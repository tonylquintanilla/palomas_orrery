# The critical path -- where we are and what stands between here and the end

**August 16, 2026.** Orrery at `227f5b2d6763baa384c090a911c2c5ced64f4a4d`,
gallery at `3d10739b097e2b63395cf58742873cf378210e68`. Both confirmed by
live check.

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
scale is now measured: 102 claims scored, three of them clean.

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

**Step one is in progress and the backlog is now visible.** Of 102
verification claims, three are clean, forty need to go back to whoever
filled them in, nineteen need a conversation, and forty are recorded
without a route. That is not a discouraging result -- it is the first
time the number has been knowable at all. Before the checker existed,
the same 102 claims were unexamined and looked fine.

**Step two is designed, not built.**

**Step three has not been started.** It is the smallest piece of work
standing between the project and a Saturn that renders.

---

## What would change the picture

An independent review by two models in August found nine structural
problems in the dispatch machinery before a single questionnaire went
out. Both reviewers, working blind, said do not send it yet. One of the
nine has since been closed by a design decision that removed the
question rather than answering it.

That is the pattern the project runs on and it is working: find the
problem while it is still cheap, in conversation, rather than after it
has been baked into a hundred worksheets and a fingerprinted artifact.

---

*Prepared August 16, 2026 with Anthropic's Claude Opus 5. Built on
`227f5b2d6763baa384c090a911c2c5ced64f4a4d` at
https://github.com/tonylquintanilla/palomas_orrery, gallery at
`3d10739b097e2b63395cf58742873cf378210e68`.*
