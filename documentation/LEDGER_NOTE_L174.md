# Ledger note -- L-174, citation level mismatch (paste-ready)

Built on `b31200934bc6bfe0e697c4f8cb5f9a1d1ffa1931`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

Three blocks. Block 1 is a NEW item, L-174 (next free handle -- `L:999`
in the ledger is a template placeholder in the RICE documentation, not a
real item). Blocks 2 and 3 are one-line notes appended to L-156 and
L-173. Run `ledger_index.py` afterward to regenerate the index zone.

---

## Block 1 -- NEW item L-174

```
#### [L-174] Citation level mismatch -- citations pitched one block too far out
<!-- L:174 status:OPEN upd:2026-07-30 section:W.Active flag: rice:2/3/90/2 -->

What. Phase 1c (L-156 Gap item 6) resolves a display string's citation by
structural containment: the string inherits from the NARROWEST dict block
containing it, and an uncited block inherits nothing. The strictness is
deliberate -- outward search would silently clear the genuinely uncited blocks
tracked as L-173. The cost is that a citation written one level further out
than the resolver reads is invisible to it.

The generalization, which predicts both the successes and the failures: a
citation must sit at the SAME DEPTH as the narrowest block the table records.
build_citation_block_table records depth 1 (the assignment) and depth 2 (its
direct dict-valued entries), and nothing deeper. shell_configs.py works
because its citations sit at depth 2 and its strings at depth 3, so the
narrowest recorded block is the cited depth-2 entry. jupiter_visualization_
shells.py's ring_params failed because its citation sits at depth 1 while its
strings sit inside depth-2 blocks -- four uncited per-ring dicts shadowing a
citation meant to cover all of them.

How found. Surfaced by a session investigating why line 959 was still Tier 1
after the ring_params citation was reworded to drop the "Scope of the above
citation:" marker (0fd7cf1 -> 4844044). Root cause diagnosis verified
independently at HEAD: all four ring entry blocks uncited, resolver returns
None for all four, SCOPE_DECLARED_BLOCKS empty so the scope-decline is not the
blocker, Tier 1 confirmed still 133.

Repo-wide sweep, verified independently. Four dicts carry the shape (a cited
assignment whose dict-valued entries have no citation of their own):

  jupiter_visualization_shells.py  ring_params            4 entries,  1 LIVE
  comet_visualization_shells.py    HISTORICAL_TAIL_DATA  15 entries,  0 live
  planet_visualization_utilities.py PLANET_ROTATION      11 entries,  0 live
  idealized_orbits.py              planet_poles          11 entries,  0 live

CORRECTION to the reporting session's figures, verified line by line:
HISTORICAL_TAIL_DATA has 15 dict-valued entries, not 13 (2 already cited);
planet_poles has 11, not 6 (5 already cited). More importantly, the claim that
comet_visualization_shells.py has LIVE impact does not hold. Howell (line 294)
and Tempel 2 (line 305) were reported as Tier 1 "No source citation
(recalled)"; both actually score V_SOURCED, score 12, Tier 2, "Cited, not
independently cross-checked". Cause: a DIFFERENT citation at line 276 (JPL
Small-Body Database) sits 18 and 29 lines above them, inside the flat 60-line
context window -- that file carries per-section citations through
HISTORICAL_TAIL_DATA, not only the one at line 85. Live mis-scored findings in
that file: zero. ring_params remains the only file with live impact, and the
only mis-scored finding in it is line 959. The reporting session flagged its
own uncertainty here and asked for confirmation before fixing; that was the
right call and it is why the error did not propagate into a data edit.

THREE-LEVEL CHECK (explicitly requested; answer is not a simple no). Three-
level nesting is not absent -- it is the DOMINANT shape: 140 dicts nested 3+
deep across the repo, 63 of them carrying claim-bearing strings, overwhelmingly
shell_configs.py (SHELL_CONFIGS['Jupiter']['core'] and similar). This cannot be
seen from build_citation_block_table's output, which stops at depth 2; it
required walking the source AST directly. That depth-2 ceiling is precisely WHY
Phase 1c works for shell_configs.py. Verified separately: NO dict nested 3+
deep anywhere in the repo carries its own citation, so nothing is misattributed
today. Latent risk retained: the resolver is structurally blind to a depth-3
citation, and if one is ever added its strings will silently inherit the
depth-2 citation instead -- "innermost wins" failing one level down, invisible
in the tier counts.

Fix, as built and verified. (a) DATA, ring_params only: a short repeat citation
above each of the four ring keys, pointing at the full citation above
ring_params. Measured on a clean clone: Tier 1 133 -> 132, Tier 2 586 -> 587,
exactly one finding moves (line 959), nothing enters, Tier 3/4 unchanged --
matching the original predesign headline. (b) MECHANISM, diagnostic only, zero
scoring effect: provenance_scanner.py now records SHADOWED_STRINGS (narrowest
containing block uncited while an outer one is cited) and DEEP_CITATIONS (a
dict 3+ deep carrying its own citation, currently zero), and reports both in a
new CITATION LEVEL MISMATCH audit section. Live run reports 17 shadowed strings
across the two remaining latent files; the deep-citation subsection correctly
renders zero times.

Deliberately NOT done: repeat citations for the three latent files. They carry
no live mis-scoring, the flat 60-line window covers them, and editing three
clean files to fix nothing is churn that can itself drift. The diagnostic
covers those three, every future instance, and the depth-3 case that no data
fix would catch. Same move already made for scope-limited citations in 1c:
decouple detection from resolution, keep the resolver strict, make the shape
visible rather than silently fine.

Explicitly rejected: loosening the resolver to search outward for a citation.
Measured during 1c -- it produces byte-identical audits at HEAD and would clear
all 18 L-173 findings the moment anyone adds a citation above SHELL_CONFIGS.
The strictness is the protection; this item exists to make its cost visible,
not to remove it.

Relationship to L-173. Adjacent, not nested. L-173 is sources MISSING. L-174 is
sources PRESENT but pitched at a level the resolver does not read. A shadowed
string is not an L-173 gap and must not be reported as one -- test_genuinely_
uncited_is_not_reported_as_shadowed pins that boundary, because collapsing the
two would make a missing source look like a formatting problem.

Tony-action (do). Run patch_L174_citation_level_mismatch.py via VS Code's Run
button; expect 15 ok lines across 3 files. Then test_citation_inheritance.py
(expect 20 passed) and provenance_scanner.py (expect Tier 1 132, Tier 2 587,
plus the new CITATION LEVEL MISMATCH section -- that section appearing is the
intended outcome, not a problem).

Tony-action (decide). Whether the 17 latent shadowed strings ever get repeat
citations, or stay monitored via the diagnostic indefinitely. Recommendation is
monitored; revisit only if one of those files is being edited for other
reasons, when the repeat costs nothing extra.

Gap. If a depth-3 citation ever appears, DEEP_CITATIONS will report it and
build_citation_block_table needs extending to record depth 3. Not built
speculatively for a population of zero.

Ref: provenance_scanner.py (build_citation_block_table, resolve_block_citation,
find_shadowing_block, _record_deep_citations); jupiter_visualization_shells.py
(ring_params); comet_visualization_shells.py (HISTORICAL_TAIL_DATA);
planet_visualization_utilities.py (PLANET_ROTATION); idealized_orbits.py
(planet_poles); test_citation_inheritance.py; L-156 Gap item 6; L-173;
documentation/AS_BUILT_L156_phase1c.md.
```

---

## Block 2 -- append inside L-156

```
Note (2026-07-30, 1c consequence tracked): The strict-containment decision
recorded above has a measured cost, now tracked as L-174. A citation written
above a dict ASSIGNMENT does not reach strings sitting inside that dict's
uncited entries -- the resolver stops at the narrowest block by design.
jupiter_visualization_shells.py's ring_params was the live instance (1
finding, line 959); fixed by repeating the citation at entry level, Tier 1
133 -> 132, closing the gap between the measured result and the predesign's
original headline prediction. Three other files carry the same shape with no
live impact. Also confirmed under L-174: the block table reads depth 1 and
depth 2 only, which is exactly why shell_configs.py inherits correctly
(citation at depth 2, strings at depth 3) -- and no depth-3 citation exists
anywhere in the repo, so nothing is misattributed. Gap item (6) remains DONE;
this is consequence, not reopening.
```

---

## Block 3 -- append inside L-173

```
Note (2026-07-30, boundary pinned): L-174 opened for a distinct failure --
citations PRESENT but written one block level too far out. These 18 findings
are the other kind: sources genuinely MISSING. The scanner's new shadowed-
string diagnostic deliberately does not report them (no cited ancestor block
exists), and test_genuinely_uncited_is_not_reported_as_shadowed fails if that
boundary ever blurs. Keeping the two apart matters: a shadowed string needs a
comment moved, an L-173 finding needs a source found.
```

---

## Rollup -- Tony-action

- **(do)** Run `patch_L174_citation_level_mismatch.py` (VS Code Run button).
- **(do)** Run `test_citation_inheritance.py` -- expect 20 passed.
- **(do)** Run `provenance_scanner.py .` -- expect Tier 1 132, Tier 2 587.
- **(do)** Paste Block 1 as a new L-174; Blocks 2 and 3 into L-156 and L-173.
- **(do)** Run `ledger_index.py`.
- **(do)** Still outstanding from the 1c session: regenerate the Skill
  Manifest via `skills_index.py` (`safe-file-editing` reads 1.0 in the
  protocol table, 1.1 in both repo and installed copies).
- **(decide)** Repeat citations for the 17 latent shadowed strings, or leave
  them monitored (recommendation: monitored).
- **(do)** After push, record `pushed at <SHA>`.

No block sets `status:DONE`, so nothing auto-archives to section C.

---

*Ledger note written July 2026 with Anthropic's Claude Opus 5.*
