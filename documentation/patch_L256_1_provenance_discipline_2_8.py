"""
patch_L256_1_provenance_discipline_2_8.py

Bumps skills/provenance-discipline/SKILL.md from v2.7 to v2.8.

Built on palomas_orrery @ 7f4a2f9f046bc00ad9e418367b42beffaff89e7b
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

WHAT THIS DOES
  Merges two drafts into one bump:
    (a) documentation/DRAFT_provenance_discipline_2_8_sections.md, the
        five sections written at 6ceb3f76 and approved 2026-08-27; and
    (b) the four sections and three revisions ruled later the same
        evening (status line, access standard, measured-is-the-goal
        with the range rule, examples-go-stale).

  Nine sections inserted, four passages revised, header bumped.
  THIRTEEN edits, all-or-nothing.

WHAT THIS DOES NOT DO
  It does not touch skills_index.py, PROJECT_INSTRUCTIONS.md, or the
  ledger. Those are the other three links of the chain and land in a
  separate patch, because a failure in one should not roll back the
  other.

SAFETY
  - MD5 guard on the target, computed after normalizing line endings
    (a Windows checkout may hold CRLF; the repo is LF).
  - Every anchor asserted UNIQUE before any write.
  - All edits applied in memory; the file is written once, at the end,
    only if every post-condition passes.
  - Original line-ending style is preserved on write.
  - A .bak copy is written beside the file before the change.

HOW TO RUN
  Open this file in VS Code and press Run, with the repo root as the
  working directory. It takes no arguments and asks no questions.

Module updated: August 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import shutil
import sys

TARGET = os.path.join("skills", "provenance-discipline", "SKILL.md")

# MD5 of the v2.7 file with line endings normalized to LF.
EXPECTED_MD5 = "c89b90b20900dc14460ec0ee6ddc895b"

BASE_SHA = "7f4a2f9f046bc00ad9e418367b42beffaff89e7b"


# ---------------------------------------------------------------- edits

# Each entry is (label, anchor, replacement).
# The anchor must appear EXACTLY ONCE. Replacement contains the anchor
# where the edit is an insertion rather than a substitution.

EDITS = []


# --- E1 -- header: version line and the v2.8 "adds" paragraph --------

EDITS.append((
    "E1 header version block",
    "Skill version: 2.7 | Cut from palomas_orrery @ 3faa72a0 (v2.7),\n"
    "earlier @ f603be3 (v2.6), @ 731066f (v2.5), @ 6b99ace (v2.2),\n"
    "@ 00219d9 (v2.1), @ eb77c83 (v2.0), @ cdcdb4b (v1.9) | August 26, 2026\n",

    "Skill version: 2.8 | Cut from palomas_orrery @ 7f4a2f9f (v2.8),\n"
    "earlier @ 3faa72a0 (v2.7), @ f603be3 (v2.6), @ 731066f (v2.5),\n"
    "@ 6b99ace (v2.2), @ 00219d9 (v2.1), @ eb77c83 (v2.0),\n"
    "@ cdcdb4b (v1.9) | August 27, 2026\n"
    "v2.8 adds nine sections and revises four passages, from Tony's\n"
    "rulings of 2026-08-27 and the two independent Mode 7 reviews of the\n"
    "same date. The Gate Binds at SERVING [CRITICAL] moves the binding\n"
    "point from drawing to publication. The Access Standard [CRITICAL]\n"
    "makes reachability a precondition of a citation -- no paywalls.\n"
    "The Status Line [CRITICAL] has each value declare its own provenance\n"
    "state so the scanner reads instead of inferring. Measured Is the\n"
    "Goal, Declared Is the Fallback [CRITICAL] carries the range rule.\n"
    "The Exhibit Requirement [CRITICAL] makes a verdict without a\n"
    "quotation UNVERIFIED. A Cross-Check Retires With Its Value or Its\n"
    "Citation [CRITICAL], Observations Are Sourced Facts [CRITICAL],\n"
    "Uncited Goes to the Ledger [QUALITY], and Examples Go Stale Like\n"
    "Values [QUALITY] complete the set. Revised: the exhibit's reader,\n"
    "Gemini's book access (demoted to lead generation), the\n"
    "two-annotation criterion for V_CROSS_CHECKED (retired -- it measures\n"
    "concurrence), and one stale worked example. Handle L-256.\n",
))


# --- E2 -- The Gate Binds at SERVING, after The Goal State ------------

GATE_SERVING = """
## The Gate Binds at SERVING [CRITICAL]

Provenance binds where a claim reaches a reader, not where it is drawn.

Drawing a shell locally gates nothing. It costs an afternoon to undo and
nobody outside the room sees it. SERVING it to the interactive gallery
is different: a visitor takes what the site shows as true, and there is
no point downstream of the orrery where a wrong radius is caught -- not
the builder, not the resolver, not the browser. None of them knows what
a correct ring radius is.

So each rendering step closes its own provenance slice BEFORE it ships,
and the slice is bounded by what that step serves.

This EXTENDS the earlier line that the asymmetry "governs what an
artifact may LOCK, not what may be BUILT." That sentence was about
fingerprinted golden artifacts and is not withdrawn. Publication is the
sharper boundary.

The braid is intact: the audit stays bounded by the current artifact,
stays countable, and stays off the critical path as a gate. What moved
is where it binds.

**What the provenance leg requires, and what it does not.** It requires
Tier-1 = 0 on what is served -- cited, and TRUE. It does NOT require a
cross-check. A cited claim that has not been cross-checked scores 15,
which is Tier 2 REVIEW, and Tier 2 has never gated a push. Cross-checked
is a higher rung earned deliberately, not a condition of clearing
Tier 1.

(Tony's ruling, 2026-08-27. Worked case: the Sun's served features carry
111 numeric values -- 85 declared drawing parameters, 26 measured sites
holding 19 distinct values. Each measured field carries both a `source`
string and an `orrery_constant` pointer, and nine of nine served numbers
checked matched the store constant they name. That is a closed slice.)

"""

EDITS.append((
    "E2 insert The Gate Binds at SERVING",
    "## Clearing a Flagged Claim (the only two moves)\n",
    GATE_SERVING + "## Clearing a Flagged Claim (the only two moves)\n",
))


# --- E3 -- Access Standard, Uncited-to-Ledger, Measured-Is-The-Goal,
#           Status Line: after the two moves, before Geometry Constants

BLOCK_AFTER_TWO_MOVES = """
## The Access Standard [CRITICAL]

**A citation clears only if its text can be reached and read. No
paywalls.**

Three routes, in order of preference:

1. **Open full text** -- arXiv, NASA ADS scans, publisher open access,
   agency documents, IAU and IERS publications.
2. **A free abstract**, when the claim is stated in it.
3. **A Google Scholar or Books snippet** showing the sentence in
   context.

A source reachable only behind a paywall FAILS, whatever its authority.
Books and papers are held to the same test.

**A snippet must carry the qualifier, not just the number.** Snippets
truncate, and the truncation is how `ALFVEN_SURFACE_RADII` went wrong:
the figure was right and the missing words were "above the photosphere."
A snippet showing a figure without the condition attached to it does not
clear the claim.

**When a source fails access, re-home the citation to an accessible
authority carrying the same result. Delete only when none exists.** Most
failures are re-homeable, because the values that reach this store are
standard results that open sources also carry. PREM is the model: the
1981 paper is walled, the tabulation is open in several places, and the
value survives with a new citation.

**Prefer an accessible non-book authority.** Claude cannot reach Scholar
or Books, so every surviving book citation lands in Tony's manual queue.
Re-homing removes it from that queue. Minimising the queue is the point.

**Scope: prospective, at the serving gate, per slice.** This does not
trigger a sweep of every existing citation. Each body's values meet the
standard when that body reaches its ladder step. A retroactive pass has
no denominator and becomes the gate the braid was ruled to end.

**Why access rather than authority.** Two consequences, and the second
is the one worth keeping. A citation nobody in the loop can open is
functionally the retired `# Verified:` stamp -- it stops the next reader
from looking while recording nothing checkable. And every source string
the served hover shows a visitor becomes one the visitor can open.

(Tony's ruling, 2026-08-27: "If we can't access from an open paper, an
abstract or a google scholar search with context then the citation
fails. No paywalls. I don't have access to a research library.")

## Uncited Goes to the Ledger, Not the Bin [QUALITY]

When a claim outside the current slice has no citation, the disposition
is a DOCUMENTED LEDGER ROW for later sourcing -- not deletion.

Fetched-vs-Recalled's third branch (remove the claim and note the gap)
governs a claim that cannot be sourced against any authority. It does
not govern a claim nobody has sourced YET. Those are different states
and treating them alike destroys content that is merely waiting its
turn.

Per the braid: ONE ledger row per CLASS, never one per instance, so the
backlog grows by kinds rather than by counts.

**Before recording anything as uncited, check whether it is cited
ELSEWHERE in the same file.** The scanner reads a fixed lookback window,
so a real citation two hundred lines away reads as absent. A run of bare
string globals can sit far below the Source comments that cover them,
and the remedy there is to ATTACH the existing citation, not to drop the
sentence.

(Tony's ruling, 2026-08-27: "not eliminated -- documented for citation,
just not today." Worked case: `solar_visualization_shells.py` carries 26
Source blocks, 22 of which already name their store constant, while six
display-string findings 250 lines below them read as uncited. Tree-wide
the display-string class is 284 Tier-1 findings holding 553 claims,
which is why it is recorded by class and worked in slices.)

## Measured Is the Goal, Declared Is the Fallback [CRITICAL]

**A declared value is a placeholder for a measured one wherever a
measured one exists, and it is promoted as soon as it can be.**

The worked precedent is in the file. `CHROMOSPHERE_PHYSICAL_RADII` drew
at 1.1 solar radii as a visibility stylization for years; on 2026-08-16
it was promoted to the physical 1.002875 and the stylization retired.
That is the move, and it is the default direction of travel.

**Two kinds of declared, and mixing them makes the backlog
uncountable.**

- **declared pending** -- a fallback standing in for a value that
  exists and has not been sourced or promoted yet. Carries a ledger
  handle. It is backlog.
- **declared** -- a pure drawing choice, or a pick from a range that
  the source gives as a range on purpose. It never promotes, because
  there is nothing to promote to. It is not backlog.

Without the split, "declared" is a bucket mixing things that must move
with things that never will, and the remainder cannot be counted.

```
# Status: declared 2026-08-28 -- top of measured 2-4 range
# Status: declared pending 2026-08-28 -- L-2xx
```

### When the source gives a range

**Store the range as data, derive the drawn value from it by a stated
rule, and let display text interpolate the range rather than restate the
drawn value as a measurement.**

This is L-179's mechanism, generalised. `GRAVITATIONAL_INFLUENCE_AU` and
`GRAVITATIONAL_INFLUENCE_RANGE_AU` are the existing pair: the range
carries the citation and the access standard, the drawn number is a
declared midpoint, and the hover shows the envelope.

The rule is NOT which end of the range to draw. Top, midpoint and low
end are all in the store and all correct for their rows -- the helmet
cusp takes the top so the drawn cusp does not understate the helmet,
the gravitational influence takes the midpoint, the core takes the low
end. The rule is that **the pick is a declared choice and its reason
lives on the row.**

This supersedes the weaker Batch 1 convention -- best-sourced single
value in code, range in the description -- for any row where the range
is genuinely the sourced object. The weaker form leaves the range in
prose, where it cannot be interpolated and drifts from the number beside
it.

## The Status Line [CRITICAL]

**Every value in `constants_new.py` declares its own provenance state.
The scanner reads that declaration instead of inferring one.**

One line, immediately below the assignment, using the existing `+`
continuation convention:

```
# Status: <kind> <rung> <ISO date> [-- <pointer>]
```

`<kind>` is one of three, and they are the registry zones:

- **measured** -- a published value. Carries a rung.
- **declared** -- a drawing choice or a pick from a range. No rung; a
  source is not expected and its absence is not a finding.
- **derived** -- computed from other constants. No rung. Names its
  inputs and is never cleared on its own; checking it means checking
  them.

`<rung>` applies to measured values only and is one of the four the
scanner already defines: `V_FETCHED`, `V_CROSS_CHECKED`, `V_SOURCED`,
`V_RECALLED`.

The ISO date is when the status was last confirmed under the standard in
force. **No status line at all means the pass has not reached this
value** -- which is different from a value that was examined and found
wanting, and the scanner reports it as unexamined rather than passing
it.

The optional pointer names a worksheet, a source record, or a ledger
handle.

```python
HELMET_CUSP_RADII = 4.0
# Status: measured V_SOURCED 2026-08-28 -- abstract, open

CHROMOSPHERE_PHYSICAL_KM = 2000.0
# Status: measured V_SOURCED -- access untested (textbook)

SOLAR_RADIUS_AU = SUN_RADIUS_KM / KM_PER_AU
# Status: derived -- inherits SUN_RADIUS_KM, KM_PER_AU
```

**The status line must not be citable.** It carries no source text, no
agency name, no author-year, and no URL. Those live in `# Source:` and
in the worksheet. A status line that names an authority becomes a
citation for the value beside it, which is the failure A Breadcrumb Must
Not Cite already covers.

**The declaration is the only store, and inference is REMOVED rather
than kept as a fallback.** If a value declares `V_SOURCED` and the
scanner also infers a rung from a nearby comment, the two can disagree,
and that is One Value, One Home violated on a property instead of on a
number. Deleting the inference is what this section buys: the
thirty-line lookback crediting a neighbour's annotation, `# Verified:`
matching the citation pattern, a bare URL in a breadcrumb scoring as a
source, and orphan section-header annotations all trace to the scanner
guessing.

**Inside a dict, the status line attaches to the DICT when its entries
share one kind and one source**, and an entry that differs carries its
own line, which overrides. This does not reopen the per-value ruling of
2026-08-13: that ruling addressed annotations sitting inside a
thirty-line proximity window, where a parser cannot distinguish group
intent from accident. A status line on a dict is structurally scoped,
not merely near.

"""

EDITS.append((
    "E3 insert Access Standard, Uncited-to-Ledger, Measured-Is-Goal, Status Line",
    "### Geometry Constants Are First-Class Claims\n",
    BLOCK_AFTER_TWO_MOVES + "### Geometry Constants Are First-Class Claims\n",
))


# --- E4 -- Model Roles table: Gemini row ------------------------------

EDITS.append((
    "E4 Model Roles Gemini row",
    "| Gemini | Book citations (can access book content web search cannot "
    "reach), domain knowledge, structural/philosophical dialogue | "
    "Book-citation verification, domain review, tiebreaker when primaries "
    "diverge |",

    "| Gemini | Domain knowledge, structural/philosophical dialogue. Book "
    "content is LEAD GENERATION only -- see the demotion below | Domain "
    "review, tiebreaker when primaries diverge |",
))


# --- E5 -- Gemini "can open the books" paragraph ----------------------

EDITS.append((
    "E5 demote Gemini book access",
    "**Key finding (August 2026):** Gemini can \"open the books.\" It\n"
    "demonstrated access to Carroll & Ostlie and Golub & Pasachoff content\n"
    "that neither Claude nor GPT could reach via web search. This is a real,\n"
    "tested capability -- not assumed from marketing. Use Gemini specifically\n"
    "for book-citation verification and domain claims that rest on textbook\n"
    "authority.\n",

    "**Demoted 2026-08-27: Gemini's book access is LEAD GENERATION, not a\n"
    "clearing route.** This skill previously recorded that Gemini could\n"
    "\"open the books\" -- reaching Carroll & Ostlie and Golub & Pasachoff\n"
    "content neither Claude nor GPT could -- and routed book citations to\n"
    "it. Under The Access Standard that is a model's ACCOUNT of a book, not\n"
    "the book. It has the same standing as any other free-form model query:\n"
    "useful for finding where a claim lives, never citable on its own.\n"
    "\n"
    "The pilot supports the demotion independently. The Gemini leg returned\n"
    "a quotation on 1 percent of 92 rows and a locator on 28 percent.\n"
    "\n"
    "Book citations now route to RE-HOMING first -- find an accessible\n"
    "authority carrying the same result -- and to Tony's Scholar or Books\n"
    "queue only when none exists.\n",
))


# --- E6 -- Exhibit Requirement + Cross-Check Retires, before the
#           retired-stamp section --------------------------------------

EXHIBIT_AND_RETIRE = """### The Exhibit Requirement [CRITICAL]

**A verdict without a quotation is UNVERIFIED, whatever the verdict
says.**

A leg that read the document can quote it. A leg that recalled restates
the citation it was given. That difference is a property of the RETURN,
not of the claim, so detecting it needs no domain knowledge and no
second opinion.

The worksheet schema gains two required fields:

- **quote** -- verbatim text from the named source containing the claim.
- **locator** -- where in the document: DOI, bibcode, section, table,
  page, or a resolvable URL.

State both IN THE PROMPT alongside the verdict vocabulary, and say that
a row without them will be recorded UNVERIFIED regardless of its verdict
token. A missing exhibit is not weighed, not averaged against another
leg, and not read as weak agreement. It is silence, and silence is the
correct output for a leg that did not read the source.

**The quotation is a routing aid and a recall tripwire. It is NOT the
clearance.** It tells us which document and where to look, and a leg
that cannot produce one is the leg that was recalling.

**The evidence of record is the source text READ IN CONTEXT**, with the
locator and the retrieval date written into the worksheet. This is
Fetched vs Recalled applied one layer up -- to verification itself
rather than to values.

**Division of labour.** Claude fetches anything reachable directly:
arXiv, NASA ADS, agency documents, open journals. Tony fetches only what
Claude bounces off -- paywalled pages, Google Scholar, Google Books. That
queue should be short, and re-homing under The Access Standard is what
keeps it short.

**Leg counts.**

- **Citation verification: ONE leg with an exhibit is sufficient**,
  because the exhibit is then fetched and read rather than believed.
- **Value verification: TWO legs**, and only where a value must be FOUND
  rather than confirmed -- no source at all, or a citation check
  returned refuted and a replacement is needed.
- A leg returning no exhibit does not reduce the count. It contributes
  nothing.

**Measured, not assumed** (pilot returns at `6ceb3f76`, 138 rows):

| leg | rows | carried a quotation | carried a locator |
|---|---|---|---|
| Claude Opus 5 | 23 | 78% | 100% |
| GPT | 23 | 60% | 73% |
| Gemini | 92 | 1% | 28% |

The leg with no exhibits is the leg that confirmed `ALFVEN_SURFACE_RADII`
at 18.8 four times over, once describing it as a heliocentric distance
when it is an altitude. Its own notes field reads "Recollection of the
Parker Solar Probe 8th encounter results." Two legs concurring would
have kept the wrong number; the exhibit test separates them without
anyone knowing the answer in advance.

**Two limits, stated so they are not read past.** This is one dispatch.
It shows quote-presence separates a reading leg from a recalling leg; it
does NOT show quote-presence predicts correctness row by row inside a
single leg. And it makes Claude the verifier of record, which
concentrates trust in the component that has actually been failing. The
mitigation is partial and real: the document is present in the window
rather than recalled, and its URL and date go into the worksheet so
anyone can re-open it. What Tony can still catch is whether the document
is REAL and is the RIGHT one -- which is the fabrication failure this
project has suffered. What he cannot catch is a misreading of a real
paper.

**Enforcement is a build, not prose.** This section states the rule. A
checker that refuses a row lacking `quote` or `locator` is a separate
item and needs its own handle, because a rule stated only in a skill is
a check that fires when somebody remembers it.

(Tony's ruling, 2026-08-27, on the failure he has actually seen: models
guessing and inventing. "Silence is better." Reader and clearance
revised the same evening: "Honestly I don't intend to go looking for
quote text. Better would be links that I can go fetch for you to read.")

### A Cross-Check Retires With Its Value or Its Citation [CRITICAL]

A `# Cross-checked:` leg certifies one value against one citation on one
date. When either the value or the citation is replaced, the leg is
STRIPPED in the same patch, and the reason is recorded in the block.

Two ways this fires, and the store carries a worked case of each:

- **The value moved.** `ALFVEN_SURFACE_RADII` went 18.8 to 19.7 on
  2026-08-19 because 18.8 was an altitude used as a heliocentric radius.
  The two legs dated 2026-08-02 had certified 18.8 and were stripped
  with it: a check of the old value is not a check of the new one.
- **The citation went.** `HELMET_CUSP_RADII` held its value while its
  entire citation stack was removed on 2026-08-20 after an independent
  nine-source read. Its two legs went with the citations: a cross-check
  of a citation that no longer exists grants credit for nothing.

Leaving the leg standing is cite-to-clear wearing a checker's name. It
passes the scanner while certifying something that is no longer in the
file.

Record the removal in the block with its reasoning, because a removal
leaves no trace otherwise and the next reader should not have to
re-derive why a constant is uncited.

"""

EDITS.append((
    "E6 insert Exhibit Requirement and Cross-Check Retires",
    "### Retired: `# Verified: April 2026 via Gemini fact-check`\n",
    EXHIBIT_AND_RETIRE + "### Retired: `# Verified: April 2026 via Gemini fact-check`\n",
))


# --- E7 -- replace the stale chromosphere worked example --------------

EDITS.append((
    "E7 replace stale chromosphere example",
    "For visualization boundaries where the value is a display choice, not\n"
    "a measured constant:\n"
    "```python\n"
    "# Visualization shell radius (physical chromosphere extends ~2000 km\n"
    "# above photosphere = ~1.003 R_sun; drawn at 1.1 for visibility)\n"
    "```\n",

    "For a value that is a declared drawing choice rather than a\n"
    "measurement, name the choice and its reason on the row:\n"
    "```python\n"
    "# Declared: top of the sourced 2-4 R_sun range, so the drawn cusp\n"
    "#           does not understate the closed-field helmet\n"
    "```\n"
    "\n"
    "(The chromosphere-at-1.1 example that stood here until 2026-08-27 was\n"
    "retired in the code on 2026-08-16, when that shell was promoted to the\n"
    "physical 1.002875. See Examples Go Stale Like Values.)\n",
))


# --- E8 -- retire the two-annotation criterion ------------------------

EDITS.append((
    "E8 retire two-annotation criterion",
    "The scanner requires two `# Cross-checked:` lines with distinct\n"
    "(identity, reference) pairs for V2 scoring. Same source from different\n"
    "worksheets counts as two independent checks.\n",

    "**Retired 2026-08-27: two annotations no longer earn V_CROSS_CHECKED.**\n"
    "The scanner required two `# Cross-checked:` lines with distinct\n"
    "(identity, reference) pairs. That measures CONCURRENCE, and concurrence\n"
    "is what failed on `ALFVEN_SURFACE_RADII`: two legs agreed on a wrong\n"
    "value and the dissenting leg was the one carrying evidence. The rung\n"
    "stays, and stays deliberately earned rather than gated; what earns it\n"
    "is an EXHIBIT fetched and read, per The Exhibit Requirement. Both\n"
    "independent Mode 7 reviewers reached this conclusion separately on\n"
    "2026-08-27. The scanner change is a build with its own handle.\n",
))


# --- E9 -- Observations Are Sourced Facts, after One Value One Home ---

OBSERVATIONS = """## Observations Are Sourced Facts, and They Migrate [CRITICAL]

An observed event figure is a measured value with a source, and its home
is `constants_new.py` like any other.

A disintegration radius, a spacecraft's closest approach, a crossing
distance, a perihelion -- these read as narrative rather than as
constants, so they get typed into prose and stay there. They are
observations of the physical world with an authority behind them, and
One Value, One Home applies to them without exception.

The scope boundary is unchanged: MEASURED values migrate, DECLARED
drawing parameters stay where they are drawn.

The practical consequence is an ordering one. A citation cannot move
into the store ahead of the value it cites, because a citation with no
value beside it has nowhere to sit. So the migration is: value first,
then its source line, then the prose references the constant.

(Tony's ruling, 2026-08-27. Founding case: MAPS C/2026 A1's
disintegration at 8.33 R_sun is cited to SOHO/CCOR-1 observations at
`solar_visualization_shells.py` line 1226, and the figure itself lives
only in display strings.)

"""

EDITS.append((
    "E9 insert Observations Are Sourced Facts",
    "## Report to the Figures You Have [QUALITY]\n",
    OBSERVATIONS + "## Report to the Figures You Have [QUALITY]\n",
))


# --- E10 -- Examples Go Stale, before Field Notes ---------------------

EXAMPLES_STALE = """## Examples Go Stale Like Values [QUALITY]

**A worked example in a skill is a claim about the codebase, and it
decays the same way a constant does.**

This skill taught the chromosphere drawn at 1.1 solar radii as its model
of a declared visualization boundary, for eleven days after the code
promoted that exact value to the physical figure. A skill loads every
session and is normative, so a stale example there is worse than a stale
line in a plan document: it teaches the retired state as the pattern. A
session read it and reported the retired value to Tony as current.

When a bump touches a section, re-read its examples against the file.
When a value moves, grep the skills for it in the same patch. This is
The Correction Does Not Travel, applied to the skill layer.

"""

EDITS.append((
    "E10 insert Examples Go Stale Like Values",
    "## Field Notes\n",
    EXAMPLES_STALE + "## Field Notes\n",
))


# --- E11 -- field note: a missing annotation is not missing verification

FIELD_NOTE = """- **A missing annotation is not missing verification.** The absence of a
  `# Cross-checked:` line means no ANNOTATION. It does not mean no work.
  Verification lands in several places the annotation grammar does not
  count: a `Resolved:` leg naming the returned verdict that caused an
  edit, a `Record:` leg pointing at a source record in `documentation/`,
  a `Review-note:` block carrying an independent read, and a convergence
  report filed after a dispatch. A row can carry all four and still show
  no cross-check. Before reporting a value as unverified, read the
  block's other legs and look for its source record. Say which claim is
  being made -- "carries no cross-check annotation" and "has not been
  verified" are different statements, and the first said carelessly is
  heard as the second. (Origin, 2026-08-27: a session reported seven of
  the Sun's constants as lacking cross-checks in a way that read as
  unverified. Two of the seven were the most-worked rows in the file --
  `ALFVEN_SURFACE_RADII` had a three-model pilot dispatch behind it, and
  `HELMET_CUSP_RADII` rested on a paper Tony retrieved from NASA ADS
  himself. The annotations were absent because the earlier legs had been
  correctly stripped, which is A Cross-Check Retires working, not a gap.)

"""

EDITS.append((
    "E11 insert missing-annotation field note",
    "- **An evidence artifact is filed AS RECEIVED.**",
    FIELD_NOTE + "- **An evidence artifact is filed AS RECEIVED.**",
))


# --- E12 -- refresh the retired-stamp census --------------------------

EDITS.append((
    "E12 refresh retired-stamp census",
    "Census at `1e60c783`: 42 remaining -- shell_configs.py 14, earth 13,\n"
    "jupiter 9, comet 6.",

    "Census re-measured at `7f4a2f9f` (2026-08-27): 42 remaining --\n"
    "shell_configs.py 14, earth 13, jupiter 9, comet 6. Unchanged since\n"
    "`1e60c783`. Disposal is not a separate deletion patch: the status\n"
    "pass REPLACES each stamp with a real `# Status:` line as it passes\n"
    "through, which records what the stamp was actually worth instead of\n"
    "leaving a blank.",
))


# --- E13 -- point the description line at the new gate ----------------

EDITS.append((
    "E13 front-matter description",
    "or preparing a GitHub push (the gate is Tier-1 = 0 on the active "
    "build path).",

    "or preparing a GitHub push (the gate is Tier-1 = 0 on the active "
    "build path, and it binds at SERVING).",
))


# ---------------------------------------------------------------- apply

def main():
    if not os.path.isfile(TARGET):
        print("FAIL: %s not found." % TARGET)
        print("Run this from the repository root (the folder holding "
              "skills/ and constants_new.py).")
        return 1

    raw = open(TARGET, "rb").read()

    # Detect and normalize line endings. Windows checkouts may be CRLF.
    had_crlf = b"\r\n" in raw
    norm = raw.replace(b"\r\n", b"\n")

    actual_md5 = hashlib.md5(norm).hexdigest()
    if actual_md5 != EXPECTED_MD5:
        print("FAIL: fingerprint mismatch. Nothing was written.")
        print("  expected (v2.7, LF-normalized): %s" % EXPECTED_MD5)
        print("  actual:                         %s" % actual_md5)
        print("  line endings on disk: %s" % ("CRLF" if had_crlf else "LF"))
        print("The file is not the v2.7 this patch was built against.")
        print("Re-pull skills/provenance-discipline/SKILL.md at %s."
              % BASE_SHA[:8])
        return 1

    try:
        text = norm.decode("ascii")
    except UnicodeDecodeError as exc:
        print("FAIL: target is not pure ASCII (%s). Nothing was written."
              % exc)
        return 1

    print("Fingerprint OK. Target is v2.7, %d lines, %s on disk."
          % (text.count("\n"), "CRLF" if had_crlf else "LF"))
    print("Applying %d edits...\n" % len(EDITS))

    # Pass 1: every anchor must appear exactly once. No writes yet.
    for label, anchor, _repl in EDITS:
        n = text.count(anchor)
        if n != 1:
            print("FAIL: anchor for %s appears %d times (need exactly 1)."
                  % (label, n))
            print("Nothing was written.")
            return 1
    print("All %d anchors unique.\n" % len(EDITS))

    # Pass 2: apply in memory.
    for label, anchor, repl in EDITS:
        text = text.replace(anchor, repl, 1)
        print("  applied  %s" % label)

    # Post-conditions. Each one can fail.
    print("")
    checks = [
        ("version line reads 2.8",
         "Skill version: 2.8 | Cut from palomas_orrery @ 7f4a2f9f" in text),
        ("no 2.7 version line remains",
         "Skill version: 2.7" not in text),
        ("The Gate Binds at SERVING present",
         "## The Gate Binds at SERVING [CRITICAL]" in text),
        ("The Access Standard present",
         "## The Access Standard [CRITICAL]" in text),
        ("The Status Line present",
         "## The Status Line [CRITICAL]" in text),
        ("Measured Is the Goal present",
         "## Measured Is the Goal, Declared Is the Fallback [CRITICAL]" in text),
        ("Uncited Goes to the Ledger present",
         "## Uncited Goes to the Ledger, Not the Bin [QUALITY]" in text),
        ("Observations Are Sourced Facts present",
         "## Observations Are Sourced Facts, and They Migrate [CRITICAL]" in text),
        ("The Exhibit Requirement present",
         "### The Exhibit Requirement [CRITICAL]" in text),
        ("A Cross-Check Retires present",
         "### A Cross-Check Retires With Its Value or Its Citation [CRITICAL]"
         in text),
        ("Examples Go Stale present",
         "## Examples Go Stale Like Values [QUALITY]" in text),
        ("stale chromosphere-at-1.1 example gone",
         "drawn at 1.1 for visibility" not in text),
        ("two-annotation criterion retired",
         "Retired 2026-08-27: two annotations no longer earn" in text),
        ("Gemini book access demoted",
         'Gemini can "open the books."' not in text),
        ("output is pure ASCII", all(ord(c) < 128 for c in text)),
        ("Field Notes still last major section",
         text.rindex("## Field Notes") > text.rindex("## Examples Go Stale")),
    ]

    failed = [name for name, ok in checks if not ok]
    for name, ok in checks:
        print("  %-42s %s" % (name, "OK" if ok else "FAIL"))

    if failed:
        print("\nFAIL: %d post-condition(s) failed. Nothing was written."
              % len(failed))
        return 1

    # Write. Backup first; restore original line-ending style.
    shutil.copy2(TARGET, TARGET + ".bak")
    out = text.encode("ascii")
    if had_crlf:
        out = out.replace(b"\n", b"\r\n")
    with open(TARGET, "wb") as fh:
        fh.write(out)

    print("\nWROTE %s" % TARGET)
    print("  backup: %s.bak" % TARGET)
    print("  %d lines -> %d lines" % (norm.count(b"\n"), text.count("\n")))
    print("")
    print("NEXT, in order:")
    print("  1. Run skills_index.py to regenerate the Skill Manifest.")
    print("  2. Run the second patch for PROJECT_INSTRUCTIONS.md and the")
    print("     ledger (protocol v3.45 entry, routing line, L-256 rows).")
    print("  3. Run maintenance_run.py -- all checkers must pass.")
    print("  4. Commit and push, then reinstall the skill to your account")
    print("     profile (Settings > Skills).")
    print("")
    print("  The reinstall CANNOT be confirmed from inside this session.")
    print("  The handoff records it as an obligation: provenance-discipline")
    print("  went to 2.8; this session loaded 2.7; the NEXT session confirms")
    print("  its loaded copy reads 2.8 before doing provenance work.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
