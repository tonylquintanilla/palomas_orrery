# DRAFT -- The Rendering Ladder

**Written 2026-08-27 with Anthropic's Claude Opus 5.** Orrery
`6ceb3f76c665a678d34a623aa47cb1cc0b427574`, gallery
`1a67b00d73813a1387ff1de7b77f8175c39c0f1e`. Both read from the live
remote. Every figure below was measured against those two commits, not
carried from a prior document.

**This is a draft for Tony to read, not a patch.** It is written to drop
into `MASTER_PLAN_INTERACTIVE_GALLERY.md` as a new Section 5b and, in
condensed form, into `MASTER_PLAN_CRITICAL_PATH_SUMMARY.md`'s path
section. Nothing has been written into either document yet.

---

## Why this section exists

The master plan sequences two ladders and admits, in its own
2026-08-25 append, that it does not sequence a third:

> "Nothing in the five segments or the seven artifacts sequences that
> axis, and nobody ever decided that some of it would be shown
> interactive-side and some not."

The five segments sequence the PLUMBING -- store, transport, renderer,
lock, ship. The seven golden artifacts sequence the PROPAGATION MATHS --
conic, planetocentric, mean elements, spacecraft arc, barycentric
binary. Neither says what a visitor SEES, or in what order.

This section is that third ladder. Tony's ruling, 2026-08-27: build it in
the order the orrery was built in -- the Sun and its shells, then the
inner planets, then the outer planets, and onward -- because that order
is already known to teach well.

## Two rulings that govern every stage

**One. The provenance gate binds at SERVING, not at drawing.** (Tony,
2026-08-27.) The critical path summary currently says the asymmetry
"governs what an artifact may LOCK, not what may be BUILT." That sentence
was written about fingerprinted golden artifacts and it is not withdrawn.
It is extended: the sharper line is publication. Drawing a shell locally
costs nothing and can be undone in an afternoon. Serving it to the
gallery is different, because a visitor takes what the site shows as
true and there is no downstream point at which a wrong radius is caught.

So each stage carries its own provenance slice, and that slice closes
before the stage ships. The braid is intact -- the audit is still bounded
by what is being built, still countable, still not a precondition that
never terminates. What moved is where it binds.

**Two. The golden fingerprint rides IN STEP, never as a prep that
blocks.** (Tony, 2026-08-27.) Each stage cuts or re-cuts its record as
part of the stage. A stage that legitimately changes the scene changes
the record, and that is a normal event rather than a failure -- the same
thing ruled on 2026-08-25 about artifacts reopening.

What the fingerprint is FOR, stated once because it has been misread as
a template: it records fourteen facts about an assembly -- object,
centre, trace counts by role, coordinate bounds and sampled positions to
nine decimal places -- so that two things can be checked that no render
can show. A position landing three-tenths of a percent from where it
belongs draws a perfectly plausible picture. And the same fourteen facts
computed in Pyodide and in CPython, compared, are the only available
proof that the browser and the desktop run the same maths, which is the
central claim of the B' architecture. It is a precision instrument for
what sits below the threshold of sight. It is not a template, nothing is
instantiated from it, and it never ships.

## Two measurements that set the starting line

**The page that ships today renders nothing from the cache.** Measured at
gallery `1a67b00d`: `interactive.html` contains zero references to
`coverage_index.json`, `feature_configs.json`, or the `data/solar-system`
tree. Its orbits come from eight sets of Keplerian elements hardcoded in
the HTML, computed by a small NumPy routine under Pyodide and drawn by
Plotly.js. That is the Phase 0 demonstration of July 6, and the plan
deliberately froze it on the A path. The nightly build therefore reaches
no visitor.

**The assembler HAS run in a browser, on a page nobody can reach.**
`gallery/solar_system_earth_test.html` and `solar_system_earth_test2.html`
load the assembler package into Pyodide, fetch the coverage index and
`objects_config.json`, assemble a scene and render it. Their own headers
call them throwaway dev pages and they require the folder be served over
HTTP. So the B' path is proven in a browser and has never been given an
exhibit.

This reframes what the first stage is. It is not "build a rendering
system." It is closer to "promote a working dev page to a real exhibit,
and give it something worth showing."

## Why the served catalogue is not the viewing catalogue

The cache holds thirteen objects, measured at gallery `1a67b00d`:
apophis, charon, earth, encke, halley, io, jupiter, moon, pluto, saturn,
sun, titan, voyager_1. (The master plan's status table still says
twelve; the Sun made it thirteen on 2026-08-25.)

Those thirteen were chosen for SCHEMA COVERAGE. OQ-A calls them a
"curated first tranche"; Section 3a calls them "9 test objects covering
every schema class and edge case." The set spans seven storage and
propagation shapes -- heliocentric planet, parent-relative moon,
barycentric binary, spacecraft arc, comet with perihelion time,
near-Earth asteroid, frame origin -- with one or two objects each. The
set exists to prove the schema holds every kind of thing.

**A coverage set and a viewing set are different sets, chosen by
different criteria.** A coverage set wants one of each kind; one moon is
enough to prove moons work. A viewing set wants completeness inside a
familiar frame, because a solar system missing Mercury, Venus, Mars,
Uranus and Neptune does not read as a solar system -- it reads as
broken. All five of those are absent from the cache today.

Nobody has ever chosen a viewing set. That is what the ladder below
does, and it is why the stages have a data dependency the existing plan
documents do not state.

The addition is cheap by design: OQ-A already rules that the full
catalogue "scales via export run, not schema change." A planet is one
entry in `objects_config.json` -- thirteen keys, mostly boilerplate,
plus its feature families -- and a `--first-build` run.

---

## The ladder

**Tony's ruling, 2026-08-27, and explicitly provisional: "Along these
lines, not a final ruling. We should revisit the scheme at each major
junction."** The seventeen steps below are recorded as given. They are
finer than the four-stage draft they replace, and the finer slicing is
the point -- an earlier version of this section grouped the inner
planets into one stage, which hides that looking at the Sun and looking
at Earth are two separate acts of judgment.

Each step that SERVES carries its own provenance slice, closed first.
Each cuts or re-cuts its fingerprint as part of the step.

| # | Step | Notes |
|---|---|---|
| 1 | Render the Sun as is, and look | Already built: 19 shells, Mode 5 passed 2026-08-24 and 25. Local render, not a publication. |
| 2 | Render Earth's existing shells, complete with provenance | Atmosphere shell and Van Allen belts. Interior boundaries closed orrery-side 2026-08-26 (L-249). |
| 3 | Decide the GUI harness for the user | **A conversation, not a build.** Placed here deliberately: look first, then design the controls. |
| 4 | The remaining Earth shells | Provenance and golden artifact extended as part of the step. |
| 5 | Mercury, Venus, Mars | Three cache entries plus a `--first-build`. Provenance and fingerprint per body. |
| 6 | Jupiter and Saturn -- Artifact 2 | The ring renderer lands here. Thirty measured numbers already counted in Section 5a. |
| 7 | Uranus and Neptune | Twenty-two further ring entries, uncounted. |
| 8 | Pluto barycentre, and Pluto | The wide heliocentric view. |
| 9 | The Moon | First planetocentric body. |
| 10 | The moons of Mars | Phobos and Deimos. |
| 11 | Major moons of Jupiter and Saturn | |
| 12 | Major moons of Uranus and Neptune | |
| 13 | The Pluto-Charon barycentric system | The close view. Distinct from step 8 -- see below. |
| 14 | Selected space missions | |
| 15 | Selected comets | |
| 16 | Selected asteroids | |
| 17 | Review and reassess | |

**Three notes on the list, recorded rather than resolved.**

*Steps 8 and 13 are two views, not a duplication.* Step 8 is Pluto seen
heliocentrically, where its trajectory is the barycentre's. Step 13 is
the close barycentric pair. That is the "Pluto/Charon two-view" the plan
already settled in its 2026-07-20 addendum: a near-equal-mass binary
needing both a wide and a close view means TWO independent fetches, never
one derived from the other. Splitting them across the ladder matches the
design.

*Step 6 as dictated reads "Jupiter and Mars."* Mars is at step 5 and
Saturn is otherwise absent, so it is read here as Jupiter and Saturn.
Flagged rather than silently corrected.

*Step 1 renders the Sun "as is," and step 2 says "complete with
provenance" only of Earth.* Under the serving gate that is consistent --
a local render is not a publication and gates nothing. What it leaves
open is WHEN the Sun's nineteen values close: before the Sun is served,
certainly, but the list does not say whether that happens at step 1,
alongside step 2, or at step 3 when the exhibit takes shape. Worth
settling at the first junction.

## What this changes about the other two ladders

The five segments are unchanged. This ladder says what a visitor sees;
the segments say what has to be built underneath, and none of that moves.

**The seven golden artifacts stop being a parallel track.** That is the
consequence of the interweaving ruled on 2026-08-27: render, provenance
and fingerprint advance together at each step, so an artifact is cut or
extended as part of the step that renders it rather than scheduled
against it. Artifact 1 is discharged across steps 2 and 4, Artifact 2 is
step 6, and the rest arrive where their bodies do.

The seven are not withdrawn, because they still name the propagation
shapes that have to be proved. What is worth noticing is that the
viewing order traverses those shapes in nearly the order the artifact
ladder already had them: heliocentric conics through step 8,
planetocentric motion from step 9, the barycentric pair at 13, a flown
spacecraft arc at 14, comets at 15. That is not a coincidence. The
orrery was built in this order for the same reasons, and the propagation
ladder was derived from it.

Segment 2, the cross-repo transport, is still designed and unbuilt, and
is still not on the path to a first render. It becomes more important as
stages accumulate, because it is what stops a correct orrery drifting
from its hand-maintained copy.

## What is left open

Two questions, both smaller than the drafting note they replace. An
earlier version of this section said the three ladders interleaved
awkwardly and that nobody had ruled on it. Tony ruled it on 2026-08-27,
in the ladder itself, by folding provenance and the fingerprint into
each step. That paragraph is withdrawn rather than deleted, because it
described a real gap for about an hour.

**When the Sun's nineteen values close.** Step 1 renders the Sun as is,
and only step 2 says "complete with provenance." Under the serving gate
that is consistent, since a local render is not a publication. It is
still unsaid whether the Sun's slice closes at step 1, alongside step 2,
or at step 3 when the exhibit takes shape.

**The exhibit page has no design.** "Promote the dev page" is a
description of a code path, not of what the page looks like or what a
visitor can change on it. That is step 3, and it is a conversation.

## One carried fix, ruled and not yet built

**`compare()` treats two position-like fields inconsistently** (Tony
confirmed 2026-08-27, for later rather than now). `position_samples`
carries a 0.001 tolerance so small numerical drift is not a difference.
`coordinate_bounds` holds the same kind of quantity in the same units
and is compared exactly, to nine decimal places. The nightly refreshes
Earth's osculating elements every run, the bounds move in the seventh
decimal, and the comparison calls it a failure. This is one of three
fields guaranteeing a golden record cannot stay green for a day, which
is the underlying reason nobody noticed the check was comparing nothing.
Fix: extend the existing tolerance to the bounds, or state a separate
one. One line.

On the nine decimal places themselves: they are comparison keys, not
reported values, so the significant-figures rule does not bind -- the
rounding is a determinism device that strips floating-point noise so the
same computation yields the same string on a different machine. But the
harness rounds to fixed DECIMAL PLACES, which across quantities of
different magnitude yields nine significant figures for one coordinate
and five for another in the same record. Presented unlabelled where a
reader sees them, they invite being read as measurements.
