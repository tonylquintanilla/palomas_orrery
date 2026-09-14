# Review request: are more rules the right repair?

Built on orrery `773e5c2d084f8e269abc5700d33928e530902b29`
at https://github.com/tonylquintanilla/palomas_orrery
Gallery at `eab070a94e53296c05b384eb342085884ef56341`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io

Tony Quintanilla, PE | request drafted by Claude Opus 5 | 2026-09-14
Handles: L-305, L-321, L-322, L-323.

## Before you start

Read these four files at the SHA above and say in your reply which of them
you actually read. A reply that does not name them is telling us it did
not read them.

- `PROJECT_INSTRUCTIONS.md` -- the whole of Part 2 and Part 3. The
  sections that bear directly on this question are Procedural
  Criticality, Method Belongs to the Skill, The Braid, A Check That
  Cannot Fail Is Not Passing, and A Report Names Its Items.
- `skills/provenance-discipline/SKILL.md` -- Report to the Figures You
  Have, The Store Carries the Verified Figure, The Status Line, and The
  Access Standard.
- `skills/ledger-and-session-records/SKILL.md` -- whatever it says about
  reading an item before building one part of it.
- `skills/orrery-coding-conventions/SKILL.md` -- the hover text and range
  conventions.

**If you have already reviewed part of tonight's session in this
conversation, say so.** The provenance skill records that a checker
which has seen the round's answer is not independent for a rerun. An
opinion from inside the session is still useful; it is just a different
thing from a fresh read, and we would rather know which one this is.

## Who this is for

Tony Quintanilla is a retired civil and environmental engineer, an artist
and an anthropologist. He is not a professional programmer and not a
trained astronomer. The polish of the code you are about to read is the
product of AI collaboration and says nothing about his fluency, so please
unpack technical terms on first use rather than assuming they land. He
holds sole commit authority and every integration judgment call.

## The question

Tonight three problems were caught by Tony or by a reviewer rather than
by the session that made them. Claude proposed writing new rules into the
skills. Tony's objection, in his words: "are more rules the answer? We
already have complex rules. Shouldn't model reasoning cover this?"

That is the question. Not whether the three problems were real -- they
were, and they are fixed. Whether the REPAIR is a rule, and if not, what
it is instead.

This matters beyond tonight because the skill layer is already 1,886
lines in one file and every skill loads at the start of a session. A rule
that does not earn its place makes the rules that do harder to see, which
is the Procedural Criticality argument applied to the skills rather than
to the checks.

## The three problems, with evidence you can check

**1. Significant figures.** Claude wrote a helper that converts a distance
in Earth radii into an altitude in kilometres, rounding every figure to
two significant figures. Two was a rule Claude chose. The store already
says what to report per row: `EARTH_BOW_SHOCK_STANDOFF_RADII` in
`constants_new.py` carries `REPORT 13.51` in its own `# Derived+:` lines,
and the string that prints it uses `:.4g`. Meredith et al. (2014) states
the outer belt as 3 to 7 Earth radii, one figure each, and the uniform
rule printed 13,000 and 38,000 km off those. The relevant skill section,
Report to the Figures You Have, was loaded at the time. Tony caught it by
asking whether the figure count came from the sources.

**2. L-305 item 5.** The session built item 7 of an eight-part ledger
item and never read item 5, which is open and which says: port Shue
(magnetopause) and Jelinek (bow shock) into the renderer, and DROP
`magnetic_tilt_deg=11`. Consequences: Claude described the drawn shape
parameters as settled when item 5 retires them; Claude recommended giving
the dipole tilt a store row when its own plan says to drop it; and
`EARTH_BOW_SHOCK_JELINEK_LAMBDA` (line 606) and
`EARTH_BOW_SHOCK_CUT_ANGLE_DEG` (line 618) sit in the store with no
consumer anywhere in the codebase, which nobody had noticed. Tony caught
this by saying the eccentricity had been fixed to a real number and
asking for a review.

**3. A sourceless sentence in served text.** Claude wrote a hover
sentence saying a second published fit puts the magnetopause farther out
by less than the drawn fit's own scatter, naming neither the fit nor a
source. It carries no numeral, so the provenance scanner cannot see it:
the scanner flags number-plus-unit tokens in display strings. A reviewer
caught it by reading.

**The contrast worth weighing.** The same session's own pre-test caught
two Tier-1 provenance findings that Claude had introduced, and fixed both
before delivery. A check that can fail, running automatically, worked.
The three above had no such check.

## What Claude proposed, and the case against it

Claude's split:

- Problem 1 gets NO rule. The rule already exists and was loaded; a
  second copy is the same rule louder. The repair is L-322(d), the open
  item that would make the row's REPORT instruction machine-readable so a
  check can fail instead of a reader remembering.
- Problem 2 gets NO rule but a TOOL change: `ledger_index.py` knows the
  item structure and does not surface it. If looking up L-305 printed all
  eight parts with their statuses, reading to the edge of item 7 and
  stopping would not have been possible.
- Problem 3 gets a rule, because it is an environment fact rather than a
  reminder: a factual sentence with no numeral is invisible to the
  scanner, to the status lines, and to every check the project has. That
  is learned by watching one get through, not derived by a careful
  reader.

Claude's proposed test for any new rule: **would a careful reader with
full attention still get this wrong?** If no, it is an attention failure
and a rule is the wrong instrument. If yes, it is knowledge that cannot
be derived -- an environment fact, a past failure, one of Tony's rulings
-- which is what skills are for.

The case against that split, stated as strongly as we can make it:

- The test may be unfalsifiable in practice. Every miss looks like an
  attention failure after the fact, because the information was always
  somewhere. Applied consistently it would forbid nearly every rule in
  the skills, including ones that demonstrably work.
- "Model reasoning should cover this" may be wishful. The protocol's own
  Hassabis section says today's systems are jagged, and the same session
  that held 1,886 lines of skill missed a line four rows from where it
  was typing. If jaggedness is the permanent condition, rules that
  compensate for it are doing their job even when they restate something.
- Tool changes and open ledger items are slower than a rule. L-322(d) is
  not scheduled. A rule lands tonight. There is a real argument for the
  rule as the interim and the tool as the fix.
- Against all three: the miss rate may be a function of session length
  and context pressure rather than of what is written down, in which case
  neither rules nor tools help and the answer is shorter sessions or a
  second reader -- which is what caught all three tonight.

## What would be a useful answer

Not a vote. Tony is deciding, and he has said he cannot tell which way
this goes.

- Whether the three problems are actually one kind or three, and what
  that implies. Claude sorted them three ways; that may be
  over-classification.
- Whether the proposed test is sound, or whether it should be replaced.
  If you would replace it, say with what.
- Whether there is a fourth repair neither of us named. Shorter sessions,
  a standing second-reader step, a checkpoint at a particular moment, a
  smaller skill layer -- anything.
- If you do think a rule is right for any of the three, say which skill
  it belongs in and what it should say, in the voice those skills use.
- What you would NOT do, and why. A recommendation to add nothing is a
  complete answer if that is what you conclude.

Please be direct about where Claude's reasoning is self-serving. Claude
proposed the test that exempts two of its own three misses from
rule-writing, and that is worth saying plainly if it is what you see.

Written September 2026 with Anthropic's Claude Opus 5.
