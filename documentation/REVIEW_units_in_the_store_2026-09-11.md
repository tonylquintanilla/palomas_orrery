# Review -- units in the store, and the orrery as producer

Built on orrery `2432db648f317387527a920aa0f3d40c2ed2f3df`
at https://github.com/tonylquintanilla/palomas_orrery
and gallery `9c056d1a27554a3b0afd27530ab9995c9929ff96`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io
(both confirmed as HEAD at the time of writing).

Tony Quintanilla, PE | Claude Fable 5.1 | 2026-09-11
Type: REVIEW of the Opus 5 design record of the same date. Zero code.

## What I read

Resident: PROJECT_INSTRUCTIONS.md v3.57 (the whole document is in
the Project, so The Artifact Bounds the Audit, The Braid, A Check That
Cannot Fail Is Not Passing, Check All Parallel Pipelines, Fetched vs
Recalled were all in front of me).

Installed skills, each checked against the manifest and matching:
provenance-discipline 2.11 (the Status Line, One Value One Home, A
Drawing Approximation Does Not Promote, DERIVED), interactive-exhibit
1.2 (Provenance is part of the build), gallery-assembler 1.3 (the
boundary section and the three modules), gallery-cache-builder 1.4
(the blast-radius and sibling-config sections). Not read:
gallery-pipeline; nothing here touches Studio.

Fetched at the orrery SHA: constants_new.py, to count things the
record did not. I did not re-run the drift check or the measurements.

## The verdict in one paragraph

The design holds. Rulings 1, 2, 5, 6 and 7 are not new judgments --
each one is a rule the provenance skill already carries, applied to
units, and I say below which rule. Two things I would change: the
export should cover the whole store, not the 53 pointed-at values,
and the arithmetic parser should be deleted rather than extended,
because ruling 6 removes the need for it entirely. Two things are
missing from the record: an orrery-side check that the export is not
older than the store, and the fact that the `# Unit:` walk and the
`# Status:` walk are the same walk. Answers to the seven questions
follow.

## 1. Attack ruling 2 (suffix as declaration)

Ruling 2 stands, and the reason is already written down. The Status
Line section of provenance-discipline 2.11 says: the declaration is
the only store, and inference is REMOVED rather than kept as a
fallback, because two sources of one property can disagree. A unit is
a property of a value exactly as a rung is. Keeping the suffix reader
as a cross-check is the fallback that rule forbids.

The migration-typo argument is weaker than it looks. A suffix
agreement check can only fire on constants that have a suffix. That
is the 42 values the check already handles correctly, and none of the
six the record names, and none of L-305's fifteen unless suffixes are
invented for them. So the cross-check protects the values least
likely to be wrong and nothing new.

What actually catches a typed-wrong unit line is different for the
two kinds of value, and both exist already: an expression is caught
by dimensional analysis (ruling 4); a bare literal is caught by the
consumer, because a magnetopause standoff served in the wrong unit is
off by a factor of thousands on an axis that states its unit, and
Mode 5 sees that.

One thing to add as a reading rule, not a scanner rule: a name that
carries a unit word must agree with its `# Unit:` line. A reader will
trust `_KM` over a comment. The scanner does not parse it; a reviewer
does not accept a diff where they disagree.

And the suffix reader gets one last job before it dies: it generates
the first draft of the `# Unit:` lines for the 42 it can read. That
is ruling 3's first step, done by the code being retired.

## 2. Does the export supersede the drift check

Neither disappears, and neither is the check it is today.

The value-by-value comparison exists to catch a hand-copy error.
When the copy is generated, that error class is gone by construction,
so a per-value comparison in the gallery is the hand copy's net kept
after the hand copy is gone. Retire it.

What replaces it is two NAME checks, not one hash:

- Gallery side: the served export's bytes equal the orrery's export at
  a recorded orrery SHA. That is the round trip. It is one hash, and
  it prints the SHA it compared against so it cannot go green by
  never resolving.
- Join side, wherever the join lives: every pointer in the gallery's
  config resolves to a row in the export, listed by name, and a
  pointer with no row FAILS. NOT IN STORE stops being a report line
  and becomes a failure. That is the check the current run cannot
  make -- it prints NOT IN STORE five times and stays green.

There is a third check the record does not mention and the design
needs. Ruling 7 says the export cannot go stale because the runner
keeps it current. That is true of the runner's output on the day the
runner runs. It is not true if the store is edited and pushed on a
day the runner does not run. The runner informs the push; it is not
a hook. So the export carries the hash of the constants_new.py bytes
it was generated from, and a checker in the orrery runner compares
that to the file on disk. Mismatch fails. Cheap, and it names what
moved.

## 3. The five non-top-level values

The Status Line rule already answers the mechanism: inside a dict, a
declaration attaches to the dict when its entries share one kind and
one source, and an entry that differs carries its own line. `# Unit:`
follows the same scoping. `planet_poles` is one dict, one kind
(measured), one unit (deg): one line on the dict.

The location is the real question, and One Value One Home already
answers it: measured values live in constants_new.py. `planet_poles`
in idealized_orbits.py is a measured dict living outside the store.
Two of its entries are served today. By The Braid that makes the
dict in scope now -- the whole dict is one CLASS, one move, not four.
The function default in create_sun_galactic_tide is a different case
and simpler: a default argument is a second store. It gets a named
constant and the default references it.

After those two moves the five NOT IN STORE become zero, and the
export covers them with no special case. I would rather do that than
teach the export generator to import arbitrary modules by pointer,
because a generator that can read any module makes any module a
home, which is the rule being defended.

Whether that slice goes before or after L-305's renderer is Tony's
(see 7).

## 4. Assembler or cache builder

The question sets up a choice that is not one. Both are needed and
they do different jobs.

The builder SERVES the export: it fetches the file from the orrery at
HEAD each nightly run, records the SHA it fetched from, and swaps it
into the generation with everything else. The export is a product of
the run, so it belongs INSIDE the swap directory, unlike
objects_config.json, which is read but never written. If the orrery is
unreachable, the run fails the way a Horizons failure fails; it does
not serve yesterday's export as today's.

The assembler JOINS: Catalog reads the served config and the served
export, and resolves each pointer to its value/unit/source at scene
time. That is a few lines of Python in a place that is already
unit-tested, and it keeps the served export byte-exact, which is what
makes the gallery-side hash check possible at all. A build-time merge
that writes a combined config would put the join in a place nobody
can verify without re-deriving it.

## 5. Dimensional analysis for the 57 bare literals

The honest answer is the one the record suspects: a bare literal has
no arithmetic to contradict it, so dimensional analysis checks
nothing about it directly. Provenance is its check.

But ruling 5 is a check, and the record does not say so. A paper that
prints coefficients AND a result printed from them gives you a
derivation to run. Jelinek prints the fit coefficients and the
standoff; the store's own expression reproduces 13.51 from them. If a
coefficient were mis-transcribed the derived standoff would disagree
with the printed one. That is a real check on the literals, it is
per-paper, and it is exactly what the tanh drop blocks for Shue. So
for L-305's fifteen: transcribe both the coefficients and the
printed result, derive one from the other, and the derivation row is
the check. A literal with no printed result behind it gets provenance
and nothing else, and saying so on the row is the honest state.

Second-order: a bare literal that feeds an expression is checked by
that expression's dimensions. The 57 are not all unconstrained;
count how many appear on the right-hand side of one of the 31.

## 6. tanh, if ruling 6 holds

The need does not vanish with the export. It vanishes with the
PARSER, and ruling 6 lets you delete the parser.

Once the orrery generates the export, the generator does not need to
read Python source to get values. It imports constants_new.py and
reads the names. Every expression evaluates the way Python evaluates
it; tanh is whatever the module imported. No whitelist, no silent
drop, no second interpreter of the store's arithmetic. I checked the
module at the SHA: it imports numpy and datetime and defines one
function. Import is safe.

The only text the generator reads is the comment grammar: `# Unit:`,
`# Source:`, `# Status:`. That is one parser instead of two, and it
is the one the scanner already owns.

The gallery-side parser, which exists only because no export
existed, goes with it. That is Check All Parallel Pipelines applied
to a checker: two readers of the store's arithmetic is two stores of
its rules.

## 7. Sequencing

L-305's renderer proceeds under today's architecture. The export is
not a gate on it. The Braid says so, and the record's own measurement
says the cost of waiting is real and the cost of not waiting is
bounded.

The bounded cost is: twelve of fifteen new values report NO UNIT
until the export lands. Record that as one ledger row for the class,
not fifteen. Do not extend the gallery's suffix table to make them
green; that is the held patch, and the record was right to hold it.

Two things do go into L-305 now, because they are cheap and the
export will require them anyway: `# Unit:` lines on the fifteen, and
the paper-result derivation rows from question 5. Neither touches the
gallery.

The five-value move from question 3 can go either side. My lean is
after, as its own small slice, because two of the five are the Sun's
and Earth's poles and a wrong move there puts a closed exhibit back
under Mode 5.

## Two things the record should add

**The export covers the whole store.** The record implies 53 rows,
which means the orrery must know what the gallery points at. That is
a second list, and it drifts. Export all 88 top-level assignments;
the gallery takes what its pointers name. The store is the
denominator, and it is closed at any SHA -- this is what The Artifact
Bounds the Audit calls the closed half. It also means "missing unit
fails" applies to 88 values, not 53, and 88 is one afternoon, most of
it generated by the retiring suffix reader.

**The `# Unit:` walk is the `# Status:` walk.** At the SHA, 2 of 88
assignments carry a `# Status:` line. The Status Line rule is
[CRITICAL] and says an unmarked value is unexamined. The migration
that visits each assignment to write a `# Unit:` line is the same
visit that writes its `# Status:`. Doing them as two walks is two
diffs over one file for one reason; doing them as one is the same
review once.

## Where the framing is wrong

One place. The record calls the export "a generated file" and calls
the drift check's new question "the SHA round trip." The round trip
confirms the gallery serves the bytes the orrery published. It does
not confirm the orrery published the bytes the store holds. Those are
two hops, and the record collapses them. The store-hash line on the
export (question 2, third check) is what makes the second hop
checkable.

Everything else I tried to break held.

Written September 2026 with Anthropic's Claude Fable 5.1.
