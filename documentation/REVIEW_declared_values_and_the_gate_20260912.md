# Review request -- a declared value, an unimplemented rule, and the push gate

Built on orrery `da6bcea17f4bb4335aa0717d33f6a2e771f05bef`
at https://github.com/tonylquintanilla/palomas_orrery
The gallery repo is at `1f44673faf2acd32340bfdd4b524b6c8af5dd376`
(https://github.com/tonylquintanilla/tonyquintanilla.github.io) and is
NOT involved in this question; nothing here is gallery-side.

Tony Quintanilla, PE | request written by Claude Opus 5 | 2026-09-12
Type: DESIGN REVIEW REQUEST (Mode 7, cooperative). Zero code wanted back.
Origin: L-305 Gap item 4, blocked mid-build.

## Before you start -- the rules this task runs under

You are reviewing work governed by a written protocol and a skills layer
you do not have resident. Fetch these at the orrery SHA above and read
them before answering:

- `PROJECT_INSTRUCTIONS.md` -- in particular A Check That Cannot Fail Is
  Not Passing, Procedural Criticality, The Braid, The Artifact Bounds
  the Audit, Method Belongs to the Skill, and Fetched vs Recalled
  Convention.
- `skills/provenance-discipline/SKILL.md` -- The Status Line, Measured
  Is the Goal and Declared Is the Fallback, A Breadcrumb Must Not Cite,
  The Access Standard, Uncited Goes to the Ledger.

**State in your reply which of those two files you actually read.** A
reply that does not name them is telling us it did not read them.

In the code, the three things this question turns on:

- `constants_new.py` -- the single value home. 88 top-level assignments
  at this SHA. The Earth exhibit block runs from about line 218.
- `provenance_scanner.py` -- `SOURCE_PATTERNS` and `has_citation` around
  lines 600-705; the vulnerability scoring block around lines 2370-2470;
  `CITATION_LOOKBACK_BLOCK` at line 1138.
- `PROVENANCE_AUDIT.md` -- the per-file table and the run history at the
  top.

The code you will read is polished and that says nothing about the
author's fluency. Tony Quintanilla is a retired civil and environmental
engineer, not a professional programmer; this codebase is the product of
two years of AI collaboration under the protocol above. He holds sole
commit authority and every judgment call. Unpack jargon on first use.
Write for him.

## The situation, measured today rather than recalled

Ledger item L-305 rebuilds Earth's magnetosphere on two published
models. Its Gap item 4 adds fifteen rows to `constants_new.py`: Shue et
al. (1998)'s eight magnetopause coefficients, Jelinek et al. (2012)'s
three bow shock parameters, a bow shock cut angle, and three DECLARED
model conditions -- the solar wind dynamic pressure, the north-south
magnetic field component, and the wind speed.

Those three conditions are not measurements. They are the conditions the
two fits are evaluated at, chosen here, and a separate ledger item
(L-314) replaces them with a live measured feed later.

The patch is written and tested. Everything else in it holds:

- The three constants-related gating checkers still pass unchanged --
  21 of 21 provenance tests, 19 of 19 cross-check annotation tests,
  20 of 20 citation-inheritance tests.
- The gallery's live store-drift verdicts were reproduced locally before
  and after, so the effect on the served side is measurable without
  pushing anything.

One thing does not hold. **`constants_new.py` goes from 0 Tier-1
provenance findings to 1.** The push gate for this project is Tier-1 = 0
on the active build path, so the patch is not deliverable as written.

### The finding

    EARTH_SOLAR_WIND_BZ_NT = 0.0
    scored V4 x C5 = 20, "No source citation (recalled)"

The scanner is RIGHT about this row. Zero nanotesla has no source. Shue's
own averages are plus or minus 4 nT, northward and southward taken
separately (p. 17,695); zero is a neutral midpoint chosen here so the
drawn shape shows the unloaded case. Putting a `# Source:` on it would be
citing a paper for a number the paper does not give, which this project
calls cite-to-clear and treats as worse than leaving it uncited.

### The part that is strange, and it is why this is a review and not a fix

The two rows beside it are in EXACTLY the same provenance state -- a
declared choice, no source, none owed:

    EARTH_SOLAR_WIND_PRESSURE_NPA = 2.0     scored V3, "Cited"
    EARTH_SOLAR_WIND_BZ_NT       = 0.0      scored V4, "No source citation"
    EARTH_SOLAR_WIND_SPEED_KM_S  = 400.0    scored V3, "Cited"

Two measurements, both run this session against the real scanner:

1. `has_citation()` returns False for all three rows' own annotation
   blocks. None of the three is cited by its own text.
2. Every author-year reference and page number was stripped from all
   three declared blocks and the tree re-scanned. Nothing moved. The two
   green rows stayed green and the red row stayed red.

So the two green rows are clearing on something that is not their own
annotation. **We did not determine what**, and we stopped looking rather
than keep pulling the thread. We are not asserting a mechanism, and we
would rather you did not assume one either; if you find it, say so.

What we are asserting is the shape: three rows in one provenance state,
two green and one red, and the red one is the row whose honesty is most
explicit.

### The rule that should have settled this, and does not run

`provenance-discipline` carries The Status Line, marked [CRITICAL]. It
says every value in `constants_new.py` declares its own provenance state
in a `# Status:` line; that `declared` is one of the three kinds; that
for a declared value "a source is not expected and its absence is not a
finding"; and that the declaration is the only store, with inference
REMOVED rather than kept as a fallback.

The scanner does not read `# Status:` lines. There is no parse of that
key anywhere in `provenance_scanner.py`. The inference the rule says to
remove is still what scores every constant in the file.

Two further measurements:

- **2 of 88** rows carry a `# Status:` line at this SHA. The L-305 patch
  adds 17 more, all in the same file. That is the entire exposure of
  making the scanner read them, today.
- `provenance_exceptions.json`, which the provenance skill's own
  description names as the place suppressions are recorded, **does not
  exist in the repository.**

## The three ways this can land

Stated as neutrally as we can manage. Tony has not ruled; that is what
your opinion is for.

**1. The scanner learns to read `# Status: declared`** and stops scoring
those rows as uncited measurements. This implements a rule that is
already written and already marked [CRITICAL]. The blast radius today is
19 rows in one file. The project's own field notes warn that scanner
changes are shared-CI changes with family-wide ripple, and that widening
the scanner's vocabulary once exposed a pre-existing finding in an
unrelated module.

**2. The rows land as written, Bz stays Tier-1**, and the push goes out
with the gate knowingly red until the larger units-and-export item
(L-322) reaches it. The cost is that a red gate becomes a thing the
project has decided to live with, which is how a gate stops meaning
anything.

**3. The three conditions do not become constants in this patch.** The
renderer holds them until L-314 supplies measured values with sources.
The cost is One Value One Home: three numbers the renderer draws with,
living in the renderer.

## Claude's lean, offered so you can attack it

Option 1, scoped as small as it will go: a row carrying
`# Status: declared` is not scored as an uncited measurement, and nothing
else changes. The reasoning is that this is not a new judgment -- it is
the written rule, and the alternative options each pay a real price to
avoid implementing something already decided. The exposure will never
again be as small as 19 rows in one file.

We are least confident about the risk in the paragraph below, and that is
the part we most want tested.

## The questions

1. **Is the lean wrong?** If option 2 or 3 is better, say why. In
   particular: is there an argument for 3 that we are underweighting,
   given that L-314 is genuinely scheduled rather than notional?

2. **Does option 1 create a check that cannot fail?** If `# Status:
   declared` suppresses a finding, then writing that line becomes a way
   to silence the scanner, and nothing reviews it. What would have to be
   true of the implementation for the suppression to stay honest -- and
   is there a form where a declared row still announces itself rather
   than simply going quiet?

3. **Attack the premise on Bz.** We say zero nT is unsourceable. Is
   there an accessible authority that publishes a nominal or reference
   Bz = 0 condition for magnetopause modelling, such that the row could
   carry a true citation and the whole question dissolves? The Access
   Standard applies: no paywalls.

4. **The two green rows.** Whatever is clearing them, is a scanner that
   reports two identical-state rows differently a bug to be fixed, a
   finding to be recorded by class, or evidence for a different option
   entirely? We are wary of designing around behaviour we did not
   characterise.

5. **Scope.** Does implementing The Status Line belong inside L-305,
   which is on the critical path and whose renderer is the next
   deliverable, or is it L-322's, which is explicitly NOT a gate on
   L-305? The Braid says bound the program to what the current artifact
   renders. The current artifact renders these three numbers.

6. **Is the missing `provenance_exceptions.json` a separate finding**
   worth a ledger row, or is its absence the correct state and the skill
   description stale?

## What we do NOT want back

- No patches, no diffs, no code. This is a design round.
- Do not propose ledger handles or write ledger blocks. Handles are
  issued in the orrery repo and a proposed one is usually already taken.
- Do not re-derive the measurements above. If you think one is wrong, say
  which and how you would check it.
- Do not reconstruct the mechanism behind the two green rows by guessing.
  Read the scanner or say you did not.

Prose is fine, and disagreement is the point of asking. Where you think
the framing here is itself wrong, say that first.

Written September 2026 with Anthropic's Claude Opus 5.
