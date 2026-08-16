# Review request -- the worksheet dispatch loop, before it is used for the first time

**Built on `a872205d17ee5298d1bdc86c614b43506e82b22c` at
https://github.com/tonylquintanilla/palomas_orrery (branch main).**
Companion gallery repo, not involved here, at `30b6968` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.

Prepared for independent review by Claude Fable 5 and by GPT. You are
each receiving the same document and neither of you sees the other's
answer. Tony compares them. Please do not try to guess what the other
reviewer will say.

Any file referenced below can be read directly at:

    https://raw.githubusercontent.com/tonylquintanilla/palomas_orrery/a872205d17ee5298d1bdc86c614b43506e82b22c/<path>

If you cannot fetch URLs, say so once at the top of your reply and work
from the descriptions here. That is a legitimate answer and it changes
how Tony weighs your findings; it is not a failing.

---

## 1. Who you are writing for

**Tony Quintanilla, PE**, is a retired civil and environmental
engineer, an artist, and an anthropologist. He is not a professional
software developer and not a formally trained astronomer. He builds
this project by conversation with AI partners rather than by writing
code unassisted, and he holds sole commit authority and final judgment
on every decision.

The codebase you are about to read is not evidence of his personal
programming skill. Its structure, its docstrings and its engineering
discipline are the product of iterative collaboration with Claude. If
you read the code and infer a skilled programmer wrote it, that
inference will be wrong in a way that matters -- please do not
calibrate your explanations to it.

What Tony does own and drive personally is the workflow: the
conversation itself, the project protocol, master planning, design
manifests, build oversight, as-built verification, the ledger, and the
orchestration across models that produced this document. That is a
different axis from coding fluency. He is directing this review, not
receiving it passively.

Practical consequences for how you write:

- **Unpack jargon on first use.** Do not assume a programmer's or an
  astronomer's vocabulary lands.
- **Lead each finding with the claim in one plain sentence.** Detail
  after.
- **He works through the VS Code Run button and GitHub Desktop.** If
  you propose an operation, say plainly what it does and what could go
  wrong before proposing it. He is a git novice by his own description;
  commit and push are his known operations.
- **Do not compress a recommendation into an aphorism.** Say what
  happened.

---

## 2. What the project is

**Paloma's Orrery** is a Python solar-system and stellar
visualization suite, around 118 modules, published at
palomasorrery.com. It draws planets, moons, spacecraft trajectories,
magnetospheres, atmospheric shells, and stellar neighbourhoods, mostly
as interactive 3D Plotly figures. Every one of those drawings rests on
numbers -- a radius, a shell boundary, a bow-shock standoff distance --
and every one of those numbers is a factual claim about the world.

The project's governing rule about those numbers is called
**fetched-not-recalled**: a value may not be embedded because a
language model remembered it. It must come from a real source and
carry a citation, or be removed and the gap noted. A citation is
itself a claim about provenance, and it has to be true. Citing a source
merely to make a checker go quiet -- "cite-to-clear" -- is treated as
worse than leaving the value uncited, because the citation suppresses
the suspicion that would otherwise catch the error.

That rule has real teeth because it has failed before. Three
wrong-paper citations survived into a previously "verified" batch:
one cited an author who did not exist (a given name mis-parsed as a
surname), one cited a paper that *refuted* the value it was cited for,
and one cited a real author for a number that appears in a different
paper entirely. All three read as authoritative.

---

## 3. What is under review

A four-stage loop that has been built but never run end to end.

**Stage 1 -- the annotation.** A constant or a display string in the
source carries comment lines beneath it:

```python
TERMINATION_SHOCK_AU = 94
# Source: Voyager 1 crossed at 94 AU (Dec 2004)
# Ref: Stone et al. (2005), Science 309:2017
# Cross-checked: Claude 2026-08-02 -- Stone et al. (worksheet_claude_constants_new.md)
```

The `# Cross-checked:` line asserts four things at once: a named model
verified this value, against a named source, on a date, and wrote the
check down in a named worksheet file. Until recently nothing ever
opened that worksheet to see whether it said what the annotation claims.

**Stage 2 -- the request builder** (`worksheet_request_builder.py`,
312 lines, new as of 2026-08-15). Reads the annotated corpus and emits
a blank questionnaire, `documentation/worksheets/REQUEST_<batch>.md`.
It currently emits **65 rows over 65 distinct keys**, drawn from seven
files: `constants_new.py` 24, `pluto_visualization_shells.py` 18,
`venus_visualization_shells.py` 14, `eris_` 4, `mars_` 2, `mercury_`
2, `moon_` 1.

Each row carries a stable **key** of the form
`module.py::enclosing::label::cN` -- file, enclosing function, the
label of the thing being asserted, and for a prose string an ordinal
naming which numeric claim inside it. The builder mints keys; the
checker resolves them; they share `worksheet_keys.py` so a key cannot
be born unresolvable.

The response table has nine columns:

```
| # | Key | Claim | Code value | Your value | Source | Value correct? | Citation correct? | Notes |
```

The first four are pre-filled and the responder is told not to edit
them. Four fields are for the responder. Above the table, each row's
citation legs are printed as read-only prose.

**Stage 3 -- the responder.** An external model (you, or Gemini, or a
fresh Claude instance) fills in the blanks and returns the file. Tony
saves it into `documentation/worksheets/`.

**Stage 4 -- the checker** (`worksheet_checker.py`, 1650 lines,
69 tests). Reads the returned worksheets, finds the row about each
annotated value, and reports disagreements in `WORKSHEET_CHECK.md`.
Six layers, each with its own failure: the named worksheet exists; it
belongs to the named checker; the row is located; the code's value
agrees with the row's evidence; the code's value still equals what the
checker read then; the row's verdict amounts to a completed check.

Two deliberate constraints on the checker, both already ruled:

- **It does not write.** No propose mode. A tool that both judges
  evidence and writes citations can satisfy itself; the risk is not
  forgery, it is a row-matching bug writing annotations against the
  wrong rows and the same matcher later confirming them.
- **It does not gate the push.** Report-only.

And two dispositions it distinguishes: **SEND BACK** fires on an
*incomplete* row and returns it to whoever filled it in. **CONVERSATION**
fires on a *complete* row that disagrees with the code, because three
outcomes are live -- convention mismatch, the code is wrong, the
worksheet is wrong -- and no tool assigns the cause.

The verdict vocabulary is deliberately narrow. Seven tokens only:
`yes`/`confirmed`/`correct`, `partial`/`approx`/`approximate`, `no`,
`unverified`, `unsourced`, `derived`. Anything else reads as
UNREADABLE and goes back. A cell holding a token *plus* a
qualification is reported as unclassified rather than guessed at.

---

## 4. Two findings already on the table

State plainly whether you think each is right, wrong, or right for the
wrong reason. Both were found today; neither has been fixed.

### Finding A -- six citations name an event, not an authority (ledger item L-195)

Across the repo, 333 comment blocks carry a `# Source:` line and 19 of
those also carry a `# Ref:` or `# Also:` leg. Thirteen of the 19 are in
the 65-row dispatch. In six of the thirteen, the `# Source:` line does
not name a citable authority at all:

| Constant | Value | `# Source:` says | Authority, sitting in `# Ref:` |
|---|---|---|---|
| `STREAMER_BELT_RADII` | 6.0 | Eclipse observations; helmet streamers extend 4-6 R_sun | Golub & Pasachoff (2010); DeForest et al. (2014), ApJ 787:124 |
| `ROCHE_LIMIT_RADII` | 3.45 | Fluid Roche limit formula: d = 2.44 * R * (rho_sun/rho_comet)^(1/3) | Murray & Dermott, *Solar System Dynamics* (1999), Sec. 4.6 |
| `ALFVEN_SURFACE_RADII` | 18.8 | Parker Solar Probe first crossing, April 28, 2021 | Kasper et al. (2021), Phys. Rev. Lett. 127:255101 |
| `TERMINATION_SHOCK_AU` | 94 | Voyager 1 crossed at 94 AU (Dec 2004) | Stone et al. (2005), Science 309:2017 |
| `HELIOPAUSE_RADII` | 26148 | Voyager 1 crossed heliopause at ~121.6 AU (Aug 2012) | Gurnett et al. (2013), Science 341:1489 |
| `PARKER_CLOSEST_RADII` | 9.86 | Parker Solar Probe perihelion 22, Dec 24, 2024 | https://parkersolarprobe.jhuapl.edu/The-Mission/index.php |

This matters because Tony ruled on 2026-08-15 that the "Citation
correct?" field verdicts the `# Source:` line **only**; `# Ref:` and
`# Also:` are shown as context and never judged. So under the current
schema a responder would be asked to judge "Voyager 1 crossed at 94
AU" as the citation for the value 94 -- which is asking whether the
claim supports itself -- while Stone et al. goes unchecked.

The evidence is mechanical rather than interpretive. Each of these
blocks carries `# Cross-checked:` lines recording what the August 2
checkers verified against, and in all six they name the **Ref**-line
source (Stone, Gurnett, Kasper, Golub & Pasachoff). In the seven clean
rows the same test passes the other way: the checkers named exactly
what the Source line says (IAU B2, IAU B3, IERS, NIST/SI).

Two repair shapes are on the table:

- **Shape A -- swap.** `# Source: Stone et al. (2005), Science
  309:2017`, with the crossing narrative demoted to a `# See:` leg.
  `See` is already a recognised context leg, so the responder still
  reads the narrative; the verdicted line becomes a bare authority.
- **Shape B -- merge.** Paper and event on one Source line, joined by
  ` -- `.

Claude recommended Shape A. Argue for whichever you think is right,
including a third option.

### Finding B -- 45 of the 65 rows show the responder a truncated citation

This is larger than Finding A and was found while writing this
document. The builder extracts a citation leg by matching a comment
line that starts with a label. It does not join continuation lines. So
wherever a `# Source:` runs onto a second comment line, the second line
is silently dropped from what the responder is shown -- and that is the
exact text the "Citation correct?" field verdicts.

33 annotated sites are affected, producing **45 of the 65 dispatch
rows**: `pluto_` 18, `venus_` 14, `constants_new.py` 5, `eris_` 4,
`mercury_` 2, `mars_` 1, `moon_` 1.

The dropped tail is frequently the load-bearing part:

| Site | Shown to responder | Silently dropped |
|---|---|---|
| `mercury_visualization_shells.py:254` | NASA MESSENGER Mission; Winslow et al. 2013 -- magnetopause subsolar | 1.45 R_M and bow shock 1.96 R_M (the values used in the geometry below) |
| `mars_visualization_shells.py:599` | NASA MAVEN Mission; Mars Global Surveyor (crustal magnetic fields); | Vignes et al. 2000, GRL 27 (MPB 1.29 R_M, bow shock 1.64 R_M) |
| `pluto_visualization_shells.py:638` | Derived from JPL SSD Pluto-Charon system GM (869.3 + 106.1 km^3/s^2) | at perihelion 29.66 AU: ~5.99 Mkm (0.04 AU) = 5041 Pluto radii |
| `eris_visualization_shells.py:478` | Derived from JPL SSD Eris system mass 1.66e22 kg (Eris + Dysnomia by | construction from Dysnomia's orbit) via the standard Hill approximation, |
| `constants_new.py:173` | Carroll & Ostlie, An Introduction to Modern Astrophysics, | Ch. 11 -- chromosphere extends ~2000 km above the photosphere |

Note the fourth row: the fragment shown to the responder ends
mid-parenthesis, and it is what they would be asked to verdict.

The apparent fix is small -- teach the leg extractor to append an
unlabeled continuation comment to the leg above it. Please say whether
you think that is the right fix, whether it is complete, and what it
would break. In particular: an unlabeled indented comment is also how
`# Note:` bodies and free prose wrap, so a naive join may swallow text
that was never part of the citation.

---

## 5. Where we would like you to go beyond those two

This is the broad-reach part, and it is why the review is happening
now: **the loop has never been run**. Once 65 questions go out to
external models and come back, the answers become evidence that
future sessions build on. A structural flaw found now costs a
conversation; found later it costs the credibility of every worksheet
in the corpus.

The prompts below are seeds, not a checklist. Findings outside them
are welcome and are the main thing being asked for.

1. **What would make this loop report a false clean?** The project's
   governing test is: *a check that cannot fail is not passing.* A
   responder who copies each pre-filled Code value into "Your value"
   and types `confirmed` sixty-five times produces a perfectly green
   report having verified nothing. Is there anything in the design
   that would catch that? Should there be, and what?

2. **Is the citation question answerable as scoped?** The responder is
   asked to verdict the `# Source:` line while the `# Ref:` line sits
   above the table as unverdicted context. Does that separation
   survive contact with an actual responder, or does it invite them to
   answer about the wrong thing?

3. **Who should answer these 65 rows?** The question was built by
   Claude. The project's own rule is that a model checking its own
   output is not verification. Does that disqualify a Claude
   responder here, and does the same reasoning apply to you reviewing
   a Claude-written prompt?

4. **Ordinal stability.** A prose display string that states several
   numbers gets one row per numeric claim, numbered in the order the
   scanner finds them. If someone edits the string between dispatch
   and return, do the ordinals still mean what they meant? What does
   that failure look like from the checker's side, and would anyone
   notice?

5. **Two row-matching regimes at once.** A new "rule 0" binds a row by
   its key and deliberately does not fall through to the four older
   fuzzy prose-matching rules; a returned worksheet without a Key
   column still uses the fuzzy rules, and roughly 104 existing
   annotations bind that way. Is there a case where the two regimes
   bind the same claim to different rows?

6. **Compound answers.** One response field asks for a verdict *and*
   a number, or a range *and* the rule used to reduce it -- while the
   checker refuses to interpret any cell holding a token plus a
   qualification. Is that self-consistent?

7. **Is 65 the right target?** The provenance scanner currently
   reports 206 Tier-1 findings across the project. These 65 rows are
   the *annotated* sites -- places where someone already claimed a
   check was done. Clearing them verifies past claims; it does not
   reduce 206. Is verifying old claims the right first use of external
   reviewer effort, or should the first dispatch be pointed at
   unsourced values instead?

8. **A value that is deliberately not physical.** `CHROMOSPHERE_RADII
   = 1.1` is a drawing decision, not a measurement -- the physical
   chromosphere sits at about 1.003 solar radii and 1.1 was chosen so
   the shell is visible at orrery scale. It has no `# Source:` line, so
   the builder currently instructs the responder to answer "Citation
   correct? NO". Is that right? How should a system that audits
   factual claims treat a number that is honestly an aesthetic choice?

9. **The seven-token vocabulary.** Deliberately narrow, after
   measuring that a twenty-token registry was mostly words invented at
   the keyboard. Is anything genuinely missing, or is the narrowness
   load-bearing?

10. **Anything structural we have not asked about.** Including "this
    whole approach is wrong, and here is the shape of a better one."
    Say so directly if you think it.

---

## 6. How to reply

Please structure it so Tony can carry it back into a working session
without a follow-up question.

- **Open with a one-paragraph verdict.** Is the loop sound enough to
  run, or not, and what is the single thing you would change first.
- **Then numbered findings.** For each: a one-sentence claim in plain
  language, then the evidence, then what you recommend. Mark each
  **BLOCKING** (do not dispatch until fixed), **SHOULD FIX** (fix
  soon, does not block), or **CONSIDER** (a judgment call for Tony).
- **Separate what you verified from what you reasoned about.** If you
  read a file at the SHA above, say which. If you are reasoning from
  the description in this document, say that. This distinction is more
  useful here than confidence language.
- **Say plainly where you disagree with Findings A and B.** Agreement
  is a real answer; so is "A is right but the recommended shape is
  wrong."
- **Do not soften a structural objection into a suggestion.** If
  something is broken, the word is broken.

If you find nothing beyond A and B, say that plainly rather than
generating findings to fill the section. An honest short review is
more useful than a long one.

---

*Prepared August 15, 2026 with Anthropic's Claude Opus 5. Built on
`a872205d17ee5298d1bdc86c614b43506e82b22c` at
https://github.com/tonylquintanilla/palomas_orrery.*
