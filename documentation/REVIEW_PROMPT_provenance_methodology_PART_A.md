# Mode 7 review request -- PART A of 2 -- provenance, golden artifacts, and the braided build order

**Built on orrery `2d7f3258d1383cf752b206fa6875ee312e8f2f78` at
https://github.com/tonylquintanilla/palomas_orrery (branch main), gallery
`1a67b00d73813a1387ff1de7b77f8175c39c0f1e` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch
main). Both confirmed against the live remote on 2026-08-27.**

You have no repository access. Every figure below was measured against
those two commits by the session that wrote this document; where a
figure is an estimate it says so. Tony will supply any file you ask for
by name.

**This is Part A. It is being sent alone, on purpose.** A Part B exists
and carries a proposal from the Claude session that produced this
request. You will not see it until your answer to Part A is on record.
Do not ask for it. If you find yourself reasoning about "what they
probably want," answer the question in front of you instead.

---

## 1. Who you are writing for

Tony Quintanilla, PE, is a retired civil and environmental engineer, an
artist, and an anthropologist. He is NOT a professional software
developer and NOT a formally trained astronomer. He builds this project
by conversation with AI partners rather than by writing code unassisted,
and he holds sole commit authority and final judgment throughout.

The codebase is not evidence of his personal programming skill. Its
structure and discipline are products of that collaboration. You will
read code that implies a skilled programmer wrote it; do not let that
substitute for this framing.

What Tony owns personally is the workflow: the protocol, the master
plan, design handoffs, build oversight, the ledger, and the
cross-model relay you are currently part of. He is a git novice working
through GitHub Desktop, and he runs Python by opening a file in VS Code
and pressing Run. Recommendations that assume command-line fluency, CI
systems, pre-commit hooks, or a second developer will not be
implementable. Say so plainly if your best answer needs one anyway.

**He is one person, working evenings.** Any recommendation whose cost is
"review 553 claims" is not a recommendation. Cost is a first-class part
of your answer.

## 2. What the project is

`palomas_orrery` is a Python solar-system and stellar visualization
suite, roughly 150 modules, that queries JPL Horizons live and renders
with Plotly. A companion gallery repo publishes to palomasorrery.com.

The current program of work is putting the orrery INTO the browser: a
nightly builder fetches ephemerides from Horizons and writes a served
cache into the gallery repo; an assembler running under Pyodide reads
that cache and produces Plotly JSON; the page renders it. No server.

**One structural fact drives everything below.** Ephemerides are
re-fetched nightly, so a bad position cannot survive to morning --
provenance by construction. FEATURE CONSTANTS are different. Ring radii,
shell boundaries, belt distances and interior boundaries originate as
numbers in the orrery's Python and reach the gallery by being copied.
Horizons is never consulted for them. Nothing downstream -- not the
builder, not the resolver, not the browser -- knows what a correct value
is. An error in the orrery becomes a permanent, silent error on the
published site.

Three mechanisms exist because of that fact, and they are what you are
asked to review.

## 3. The three mechanisms, as they stand today

### 3a. The provenance scanner and its tiers

`provenance_scanner.py` walks the tree, extracts numeric and factual
claims, and scores each as VULNERABILITY x CRITICALITY. Tier 1 is the
top band and is a push gate: **Tier-1 = 0 on the active build path**,
where the path is computed from the import graph rather than listed by
hand.

Clearing a Tier-1 finding has exactly two moves: cite it to where the
data actually came from, or remove the claim and record the gap. A
citation must be TRUE, not merely present.

There is a higher rung, V_CROSS_CHECKED, requiring source evidence plus
two distinct checker annotations produced by a competitive pattern (the
same worksheet sent to independent models, compared by Tony). It has
been live since 2026-08-01. Population as of 2026-08-13: 50 rows
tree-wide. It is not a gate.

Annotations use a fixed grammar, one per value:

    # Cross-checked: <checker> <ISO date> -- <source> (<worksheet file>)

Measured at HEAD:

- 292 Tier-1 findings tree-wide.
- Of those, **284 are display strings holding 553 individual claims** --
  hover text, tooltips, info panels. Largest concentrations: four
  paleoclimate modules at 225 claims, `shell_configs.py` at 98,
  `idealized_orbits.py` at 49.
- **44 legacy `# Verified: April 2026 via Gemini fact-check` stamps**
  remain, in `shell_configs.py` (14), `earth_visualization_shells.py`
  (13), `jupiter_visualization_shells.py` (9),
  `comet_visualization_shells.py` (6). That stamp format was RETIRED
  after it was found unreliable -- it recorded that a model looked and
  nothing else. The founding case: a Hill sphere reading 9.4 million km
  against a correct 14.3, a 34% error, sitting under a verification
  stamp. Some stamped values were re-checked; most were not.

### 3b. The dispatch loop

For values needing verification, a request builder emits a JSONL
worksheet, Tony carries it to two or three models in fresh chats, the
returns come back as JSONL, a checker validates and routes them, and
accepted results are written back as annotations.

One full dispatch has run, on 2026-08-18: 23 rows to three legs, 69
answered rows, zero format defects. Its convergence report is
`documentation/PILOT_CONVERGENCE_20260819.md`.

**A measurement from those returns, offered without interpretation.**
Each return has a free-text `source` and `notes` field. Counting how
many returns contained a verbatim quotation from the cited document, and
how many contained a locator (DOI, bibcode, section, table, URL):

| leg | rows | contained a quotation | contained a locator |
|---|---|---|---|
| Claude Opus 5 | 23 | 78% | 100% |
| GPT | 23 | 60% | 73% |
| Gemini | 92 (four passes) | 1% | 28% |

On one row -- the Alfven surface radius -- the two legs carrying no
quotations both confirmed the existing value, and the leg carrying
quotations found it wrong. The existing value was an altitude above the
photosphere being used as a distance from Sun centre. One of the
confirming returns describes it in its own notes as a recollection.

Make of that what you will, including nothing.

### 3c. Golden artifacts

A "golden artifact" is a stored record of one assembled scene: fourteen
fields including object list, centre, trace counts by role, legend
groups, feature keys, coordinate bounds, and sampled positions to nine
decimal places. Its stated purposes are (1) to catch a position landing
slightly wrong, which draws a plausible picture, and (2) to prove that
the same assembly computed in Pyodide and in CPython agrees, which is
the central claim of running Python in the browser.

Seven were planned, sequencing five propagation shapes. **One exists**
-- Earth alone -- and three findings about the machinery were measured
this week:

- The harness test fingerprints today's assembly and compares it to
  itself, so it has printed OK every run since July without ever opening
  the stored file.
- A working comparison could not stay green for one day: three of the
  fourteen fields change on every nightly build by design (a timestamp,
  and bounds that move in the seventh decimal when elements refresh).
  `position_samples` carries a 0.001 tolerance; `coordinate_bounds`
  holds the same kind of quantity and is compared exactly.
- The one stored artifact is already failing for a legitimate reason:
  it recorded Earth's two feature families and the scene now carries
  eight, because the Sun was added to the assembler and it is the
  scene's centre.

### 3d. The build order being reviewed

A ruling on 2026-08-22 established that provenance is NOT a global gate
in front of the build; it is bounded to what the current artifact
renders, so it terminates and can be sized. A ruling on 2026-08-27
extended it: **the provenance gate binds at SERVING, not at drawing.**
Drawing locally costs an afternoon to undo. Publishing is different,
because a visitor takes what the site shows as true.

A seventeen-step rendering ladder was then written, ordering what a
visitor sees -- Sun, Earth's shells, a GUI conversation, the remaining
Earth shells, the inner planets, Jupiter and Saturn, and onward to
moons, spacecraft, comets and asteroids. Each step is meant to carry
three things IN STEP rather than as blocking preparation: the render,
its own provenance slice, and its golden artifact.

Draft in `documentation/DRAFT_rendering_ladder_section.md` at this SHA.
**It is deliberately WITHHELD from the master plan pending this
review.** The patch that would write it in exists and has not been run.
Your G5 answer arrives before the ladder lands, not after, so treat it
as consequential rather than as commentary on a settled decision.

Worked example of a slice, for step 1 (the Sun): the served
configuration carries 111 numeric values, of which 85 are declared
drawing parameters and 26 sites hold 19 distinct measured values. Every
measured field carries both a source string and a pointer to its store
constant; nine of nine sampled numbers matched the store. Eight of the
seventeen named constants behind them carry a cross-check annotation.

## 4. The failure mode this is all defending against

Tony's own statement, 2026-08-27, when asked what he has actually seen go
wrong: **models guessing and inventing.** Not arithmetic errors --
confident fabrication. Wrong papers cited. Values recalled from press
releases and presented as read from journals. A verification stamp over
a 34% error.

His stated preference: **"Silence is better."** An honest blank with a
recorded gap beats a plausible unsourced value, because a citation
suppresses the suspicion that would otherwise catch the error.

A second failure mode, from the same record: **a correction that reaches
one copy of a value is worse than no correction**, because the next
consistency pass harmonizes toward the uncorrected copy. Measured
instances at this SHA include a spacecraft approach distance corrected in
the constants store on 2026-04-15 and still wrong in prose at seven
sites across two modules, and a shell radius changed on 2026-08-22 and
still wrong at four sites across two other modules.

## 5. What we are asking you for

Answer as an independent reviewer. Do not reconcile with what you think
the project wants to hear; where you think the current design is wrong,
say so.

**G1. Verified information served to the renderer and to the reader.**
What is the minimum mechanism that gives real confidence a published
value is correct? Distinguish, if it matters, between a value being
SOURCED, being CONSISTENT across every place it appears, and being
CORRECT.

**G2. Simplify citation and verification.** The current design has
tiers, rungs, a two-move clearing rule, an annotation grammar, worksheet
types, and a multi-model dispatch loop. What can be deleted outright?
What is carrying its weight? Be specific about which of the 553
display-string claims, if any, are worth the cost of the current
treatment.

**G3. Simplify the golden artifact.** Given the three findings in 3c,
should this mechanism be repaired, reduced, or replaced? What is the
smallest thing that still catches a slightly-wrong position and still
proves browser-and-desktop agreement?

**G4. Simplify Tony's judgment calls.** He is the sole integrator and
the bottleneck. Which decisions currently reaching him should not, and
what rule or check would absorb them? Conversely, name anything he is
NOT being asked that he should be.

**G5. Review the braided step-by-step order.** Is "render plus
provenance slice plus golden artifact, one body at a time, gated at
publication" sound? Name its failure modes. In particular: what breaks
when step 12 changes something step 4 already published?

## 6. Answer format

Please return:

1. **Verdict per goal** (G1-G5), each opening with one plain sentence
   before any elaboration.
2. **Delete list** -- specific mechanisms you would remove, with what
   is lost.
3. **Keep list** -- what must not be simplified away, and why.
4. **Cost estimate** for anything you propose adding, in evenings of
   one person's work.
5. **What you could not assess** without seeing a file, named
   explicitly. Say "I do not know" rather than inferring. An
   unsupported guess in an answer about preventing unsupported guesses
   will be treated as a finding about the answer.

Files available on request, by name: `provenance_scanner.py`,
`constants_new.py`, `PROVENANCE_AUDIT.md`,
`PILOT_CONVERGENCE_20260819.md`, the pilot worksheets, the assembler's
golden-artifact harness, `DRAFT_rendering_ladder_section.md`, the
`provenance-discipline` skill, and the project protocol.
