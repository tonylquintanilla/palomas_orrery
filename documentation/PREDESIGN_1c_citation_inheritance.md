# PREDESIGN -- Phase 1c, citation-window inheritance (L-156 Gap item 6)

Built on `657542feb3f30b3f262e368829dd4f124be64853`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

**Type:** PREDESIGN (zero code shipped; prototypes run in sandbox only)

**Companion:** ledger L-156 Gap item 6; Phase 1 sub-step plan (1a landed,
1b landed and verified live this session).

**Baseline re-established at HEAD:** 781 findings across 118 files.
Tier 1 = 156, Tier 2 = 563, Tier 3 = 60, Tier 4 = 2. Matches the 1b result
exactly. 1b verified genuinely wired before measuring: `V_CROSS_CHECKED`
defined, `V_SOURCED = 3`, the old `"Has source citation"` reason string
gone, `CRIT_ABSOLUTE_OVERRIDE` emptied -- each checked separately.

---

## Headline: the yield is 23-24, not 42

Every figure in the existing note is superseded. Measured structurally at
HEAD, **23 Tier-1 findings would inherit a block citation** -- all in
`shell_configs.py` -- plus **1 in `jupiter_visualization_shells.py`** if the
citation lookback is set to 14 or more (see item 4). Nothing else in the
repo yields a single inheriting finding at any nesting depth.

The other 18 of `shell_configs.py`'s 41 Tier-1 findings sit inside body
blocks that **have no citation at all**. They are not window misses. They
are genuine gaps, and finding them is the most useful thing this
measurement produced:

| block | uncited Tier-1 findings |
|---|---:|
| `SHELL_CONFIGS['Pluto']` | 10 |
| `SHELL_CONFIGS['Venus']` | 3 |
| `SHELL_CONFIGS['Eris']` | 2 |
| `SHELL_CONFIGS['Mars']` | 2 |
| `CUSTOM_SHELLS['Mercury']` | 1 |

8 of the file's 24 body blocks carry no citation. Its module docstring says
"Source citations are preserved as comments above each body block." That is
true of two-thirds of them.

**Consequence for the ledger's prediction:** Tier 1 goes 156 -> ~132, not
156 -> ~114. Tier 2 goes 563 -> ~587.

---

## 1. Reconciling 66 vs 42

Both numbers are mine, from the same message, and the note merged two things
I had reported separately.

- **66** = every Tier-1 finding with any preceding `# Source:` comment,
  measured with a narrow `#.*Source:` grep: `shell_configs.py` 41 +
  `idealized_orbits.py` 24 + `jupiter_visualization_shells.py` 1.
- **42** = the subset I judged to be genuine block-level citations,
  i.e. 66 minus `idealized_orbits.py`'s 24, which I excluded as too distant.

So the missing ~24 live in `idealized_orbits.py` and were excluded on
purpose. The note recorded the raw count in the total and the filtered count
in the breakdown.

Both are now obsolete for a second reason: I measured with `#.*Source:`,
but the scanner accepts a much wider pattern set (`has_citation` matches
URLs, `# NASA`, `Verified:`, `Ref:` and more). Re-measured with the
scanner's own patterns at HEAD, the distance picture is: **2 within the
60-line window, 108 beyond it, 46 with nothing above at all.** The "beyond"
population is 108, not 66 -- but that number is not actionable either, for
the reason in item 2.

## 2. Re-measured against the live 156 -- and distance is the wrong metric

Gap distributions for the candidate files overlap almost completely:

| file | n | 61-100 | 101-200 | 201-500 | 501-1000 | >1000 |
|---|---:|---:|---:|---:|---:|---:|
| `shell_configs.py` | 41 | 14 | 14 | 8 | 5 | 0 |
| `idealized_orbits.py` | 24 | 2 | 6 | 10 | 2 | 4 |

There is no distance threshold that separates "block-cited" from "happens to
have a citation somewhere above." A file with a citation every 200 lines
produces gaps indistinguishable from a file with one block citation per
170-line body block. **Widening the window is therefore not a smaller
version of the right fix -- it is a different and wrong fix**, and it would
falsely clear all 18 of the uncited-block findings above.

The right discriminator is structural containment: is the string inside a
dict block that carries its own citation? That is what the 23 figure
measures, and it is what item 7's mechanism must compute.

**Overlap with 1a's promotions:** none. All 11 of 1a's Tier-1 promotions
were constants and dicts; all 23 inheritance candidates are display strings.
The two sets are disjoint, so 1c's effect is additive to 1a's with no
interaction.

## 3. Both dicts are in scope

Confirmed -- and they are not symmetrical:

| dict | blocks | cited | uncited |
|---|---:|---:|---:|
| `SHELL_CONFIGS` | 13 | 9 | 4 |
| `CUSTOM_SHELLS` | 11 | 7 | 4 |

Both are module-level dicts of per-body nested dicts, both carry per-block
`# Source:` headers, and both contribute inheriting findings (22 from
`SHELL_CONFIGS`, 1 from `CUSTOM_SHELLS`). Any mechanism keyed to one dict
name would miss the other; keying on structure rather than name covers both
for free.

Note that a body can appear in **both** dicts with **different** citations:
`SHELL_CONFIGS['Jupiter']` cites line 1500 (NASA Solar System Exploration;
Juno gravity science) while `CUSTOM_SHELLS['Jupiter']` cites line 2331
(NASA Jupiter Magnetosphere Overview). These must not be merged or
cross-inherited -- see item 7's edge cases.

## 4. Jupiter's two-line miss -- confirmed, and more interesting than described

Still exactly 62 lines at HEAD, against a 60-line window. Two lines.

But the structure is not what the note implies. The finding at line 959 is
inside `ring_params`, a **function-local** dict assignment spanning lines
906-965 -- not a module-level dict. A module-level walk misses it entirely;
it only appears with `ast.walk` over all nesting depths. It also only
inherits when the citation lookback reaches 14 lines above the assignment
(the citation sits at 897, the assignment opens at 906).

The citation itself carries something no other citation in the repo does:

```
# Source: NASA Jupiter Ring Fact Sheet; Galileo spacecraft data
# Verified: April 2026 via Gemini fact-check
# Scope of the above citation: ring geometry only (inner/outer radius,
# thickness). Colors below are selected by the developer for visual
```

An **explicit scope declaration** limiting what the citation covers. I swept
for the convention: it is a one-off, the only instance in the repo. It is
nonetheless the honest model, and it constrains the mechanism -- naive
inheritance would apply a ring-geometry citation to values the comment
explicitly disclaims.

## 5. `idealized_orbits.py` -- the exclusion holds, for a better reason

It holds, but my original justification was wrong.

I justified it on distance (median gap 2405). Measured with the scanner's
full pattern set, the median is 266 and the minimum is 63 -- indistinguishable
from `shell_configs.py`. The distance argument does not survive.

The structural argument does, and decisively. The file has 11 cited blocks,
all of them one-line entries in a pole-orientation table at lines 57-67
(`'Sun': {...}` on a single line each). Its 24 Tier-1 findings are at lines
124, 139, 167, 181, 1406, 1465, 1476, 1589, 2385, 2431, 2453, 2479 and
beyond. **Zero fall inside any cited block.** They are module-level strings
and function-body strings elsewhere in a 7,418-line file, with no containing
citation of any kind.

So: excluded, confirmed, and now on a reason that a mechanism can actually
compute rather than a threshold someone has to judge.

## 6. Recurrence sweep

Five files exhibit the module-level "dict of per-body nested dicts with
block citations" shape:

| file | blocks | cited | inheriting Tier-1 |
|---|---:|---:|---:|
| `orbital_elements.py` | 120 | 44 | 0 |
| `shell_configs.py` | 24 | 16 | 23 |
| `idealized_orbits.py` | 11 | 11 | 0 |
| `comet_visualization_shells.py` | 25 | 3 | 0 |
| `planet_visualization_utilities.py` | 17 | 1 | 0 |

Extending the sweep to **all nesting depths** across every file in the repo
adds only `jupiter_visualization_shells.py`'s single finding, and only at
lookback >= 14. The shape recurs; the *problem* does not. `shell_configs.py`
is 23 of the 24 total.

That is worth knowing in both directions: the fix is narrow today, but four
other files already carry the structure, so the same gap will open the moment
any of them grows a hover string inside a cited block. Structural handling
now costs the same as a `shell_configs`-specific hack and does not need
revisiting later.

## 7. Mechanism -- recommendation and edge cases

**Recommend (b), the precomputed range table.**

`ast.walk` yields every `ast.Assign` at any depth in a single pass, so the
table is built without parent pointers and without threading state through
the existing extractor. For each dict-valued entry of any dict assignment,
record `(dict_name, key, block_start, block_end, citation_line,
citation_text)`. String units then range-check against it.

Option (a), parent tracking, requires annotating the AST or rewriting the
extraction walk to carry parents. It touches more of a file that is the
project's measurement instrument, for no additional capability. Its only
advantage would be resolving containment for constructs that are not
dict-in-dict, and there is no evidence any exist -- items 4 and 6 found the
population is exactly two shapes, both of which (b) handles.

The table is also *reviewable*: it can be printed and eyeballed before any
scoring changes, which matters for a change whose whole purpose is to stop
mis-stating provenance.

### Edge cases, with recommendations

**Blocks without their own citation -- no fallback to an enclosing block.**
This is the load-bearing one. Silent fallback would falsely clear all 18
Pluto/Venus/Eris/Mars/Mercury findings by inheriting the module docstring or
an outer citation. An uncited block must inherit nothing and stay V4.

**Nested blocks -- innermost citation wins.** A cited block inside a cited
block should resolve to the nearer one. Range-check should sort candidates
by span width and take the narrowest containing block.

**`CUSTOM_SHELLS` vs `SHELL_CONFIGS` for the same body -- no cross-dict
inheritance.** Confirmed live: Jupiter appears in both with different
citations. Each block's citation applies only within its own span. Because
(b) keys on line ranges rather than body names, this is automatic -- but it
should carry an explicit test, since a name-keyed implementation would get
it wrong and the bug would be invisible in the audit totals.

**Multi-line citations -- capture the whole comment run.** `has_citation`
matches per line, and for the Moon block it matches line 240, a
*continuation* line, not the `# Source:` head at 238. Recording only the
matched line would put a fragment in the report. The table should walk
upward from the matched line to the top of the contiguous comment run and
store the full text.

**Explicit scope declarations -- do not contradict them.** One instance
today (item 4). Recommend the mechanism detects a `Scope of the above
citation:` line within the captured run and, when present, declines to
inherit and flags the block for review instead. Inheriting past a comment
that says "colors below are developer-selected" would be the scanner
asserting provenance the author explicitly disclaimed -- the same failure
class as a `# Source:` over recalled data, pointed the other way.

**Citation lookback is a tunable and needs pinning.** 8 lines catches all 23
`shell_configs.py` findings; 14 is required for the Jupiter case. Recommend
a single named constant, set at 15, applied both above the block key and
above the enclosing assignment, with the value justified in a comment.

### Vulnerability level for inheriting strings

V3 SOURCED -- "cited, never independently cross-checked." Not V2, which
requires a blind dated cross-check annotation, and not V1. V3 x C_PUBLIC 4
= 12, landing them in Tier 2 alongside the rest of the re-read queue. This
needs no new rung and no change to 1b's ladder.

---

## A correction I owe

In the session that produced the original note I told Tony that
`shell_configs.py`'s Moon block was a case where the block citation
genuinely did not cover the claims -- that "a lunar-core seismology paper
does not source the Draper point."

That was wrong, and it was wrong because I read the first line of a
multi-line citation. The full block reads:

```
# Source: Weber et al. (2011), Science, "Seismic Detection of the Lunar Core";
#         NASA Moon Fact Sheet; Apollo Seismic Experiment reports;
#         NASA Solar System Dynamics (Hill sphere radius); Draper (1847).
# Verified: April 2026 provenance audit; all 5 flagged claims confirmed.
```

Draper (1847) is cited explicitly, and it is the correct source for the
Draper point. The block also carries its own verification note. My example
argued against over-inheritance using a case that is in fact well-cited.

The argument against naive inheritance still stands, but it stands on the
Jupiter scope declaration (item 4) and on the 18 uncited blocks (headline),
not on the Moon. The Moon block is evidence for the opposite conclusion:
these citations are careful, multi-source, and worth inheriting.

---

## Predicted effect, for checking against the build

| | at HEAD | after 1c |
|---|---:|---:|
| Tier 1 | 156 | ~132 |
| Tier 2 | 563 | ~587 |
| Tier 3 | 60 | 60 |
| Tier 4 | 2 | 2 |
| Total | 781 | 781 (conserved) |

Invariant worth asserting in the build: 1c changes vulnerability only, on a
population that is entirely display strings at C_PUBLIC = 4. Nothing can
enter Tier 1, and Tier 3/4 cannot move. Any deviation from that is a bug,
not a surprise.

Predict and compare on the same population -- these are post-suppression
audit figures; in-process scoring runs ~21 units higher.

---

*Predesign written July 2026 with Anthropic's Claude Opus 5.*
