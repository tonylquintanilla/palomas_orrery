# Ledger note -- citation-predicate unification (paste-ready)

Built on `6ce6136f64282c9670b265c89228c210f8ffaa73`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

One block, appended to **L-156**. It closes the observation recorded in
the 1d/1e/1f as-built section 6. No new item needed -- this is a
follow-on inside Phase 1, not a distinct problem.

Run `ledger_index.py` afterward. Does not set `status:DONE`.

---

## Block 1 -- append inside L-156

```
Note (2026-07-31, citation predicate unified): Follow-on to the build note above,
closing the build_pinned_values() bleed flagged in the 1d/1e/1f as-built section
6. Prompt anchored 8bd7778d; HEAD moved to 6ce6136f mid-session (Tony's push of
the build prompt itself, one doc, 62 insertions) -- code identical across the
move, guard still valid. Delivered patch_pinned_values_bleed.py, uncommitted:
8 anchored edits across provenance_scanner.py and test_provenance_1d.py,
all-or-nothing across both, MD5 guard per file, idempotent refusal naming the
cause per file.

MEASURED IMPACT: NONE, and that was verified BEFORE building rather than
discovered after. Every one of the 34 numeric constants in constants_new.py
carries its own citation, so the 10-above/5-below window had nothing to bleed
ONTO -- there is no uncited numeric constant in the file for it to reach.
Compared directly at HEAD: build_pinned_values() returns 58 pinned values,
build_cited_constant_names() returns 34 names yielding the same 58 values, and
the two sets are IDENTICAL in both directions. The build prompt expected the
pinned set to shrink and some display strings to lose V_SOURCED and move toward
Tier 1; none of that happens, and the patch's own docstring says so up front so
the absence of a delta is not read as the patch having failed. Post-patch audit
verified identical to pre-patch once finding line numbers are normalised (the
only textual difference is provenance_scanner.py's own self-scan shifting by 4
lines, from the added credit line). Tier 1 171, Tier 2 646, Tier 3 62, Tier 4 2,
total 881 -- unchanged.

So this is a DEFENSIVE fix, not a corrective one. It is still worth having:
constants_new.py grows, and the first numeric constant added without its own
citation next to a cited one would enter the pinned set silently -- no error, no
finding, just slightly wrong scoring everywhere Option A fires.

DIVERGENCE from the prompt, in the direction of less duplication. The prompt
asks to replace build_pinned_values()'s logic with the same approach
build_cited_constant_names() uses. Copying it would have left TWO
implementations of one predicate in one file -- which is the actual defect here:
since the 1d build, two functions have been answering "does this constant carry
its own citation" by different rules, and whichever gets read next becomes "how
the scanner decides citation." So the shared logic was EXTRACTED instead:
constant_has_own_citation(lines_c, lineno, source_re) is now the single
implementation and both callers route through it. Same behaviour the prompt
asked for, one place to change it, and no way for the two to drift apart again.
test_both_pinned_builders_agree asserts the two callers keep producing the same
pinned set, so a future re-divergence fails a test instead of going unnoticed.
This is the "fix the producer, not the N consumers" rule applied to a predicate
rather than a value.

The rule itself is CONTIGUITY, not distance: a citation counts only if it sits
in a comment run physically touching the assignment, and a blank line ends the
run. Distance windows cannot work here -- any window wide enough to catch a real
citation is also wide enough to reach the next constant's. Both conventions in
the codebase are accepted, because both are in use: constants_new.py writes the
citation BELOW the assignment, the rest of the repo writes it above. Below is
checked first, since that is the convention of the file this predicate is
applied to most often.

Tests: test_provenance_1d.py 15 -> 20, the five additions covering
below-the-assignment, above-the-assignment, blank-line-ends-the-run (the bleed
case itself), preceding-code-ends-the-run, and the two-callers-agree invariant.
test_citation_inheritance.py 20/20 and test_constants_provenance.py 73/73
unchanged. py_compile, ASCII/LF gates, idempotency all pass from a clean clone.

D8.5 (retire or keep Option A) remains OPEN and is not made worse -- this fixes
Option A's input data, it does not decide Option A's future.

ALSO OBSERVED, floating item worth capturing rather than losing: the delivered
patch scripts now generate findings when committed, and this one lands in TIER 1.
patch_pinned_values_bleed.py's TARGETS dict -- two filenames mapped to MD5
hashes -- scores 20 (V4 RECALLED x C5 UNDETERMINED) because a dict of hashes has
no citation and no classifiable criticality. Seven patch scripts now sit in the
repo root where the scanner sweeps them; each new one adds to the count, and
this is the first to reach Tier 1 rather than Tier 2. Raised in
REVIEW_predesign_1d_1e_1f.md section 3.3 as a floating item and still
undecided. Tony-action (decide): move delivered patch scripts to a subdirectory
the scan skips, add them to data/provenance_exceptions.json, or accept the
growing self-scan population. Recommendation: a subdirectory -- these are
one-shot artifacts, not project source, and exceptions would need a new entry
per patch forever.

Add to Ref: patch_pinned_values_bleed.py; test_provenance_1d.py (now 20 tests).
```

---

## Rollup -- Tony-action

- **(do)** Run `patch_pinned_values_bleed.py` via VS Code's Run button.
  Expect 8 `ok` lines across 2 files.
- **(do)** Run `test_provenance_1d.py` (20), `test_citation_inheritance.py`
  (20), `test_constants_provenance.py` (73).
- **(do)** Run `provenance_scanner.py .`. Expect **no change** -- Tier 1
  171, Tier 2 646. That is the success condition here.
- **(do)** Paste Block 1 into L-156; run `ledger_index.py`.
- **(decide)** Where delivered patch scripts live, now that one has
  reached Tier 1 in the scanner's own audit.
- **(do)** Push; record `pushed at <SHA>`.

Still carried over and not yet done, from earlier sessions:
correct or supersede `HANDOFF_phase1_1d_to_1f.md` (wrong on 1e at HEAD);
stamp the provenance-discipline v1.3 SHA placeholder; the three open
decisions from the 1d/1e/1f as-built (piece 3's Tier-1 increase, the
Tier-1 "FIX NOW" label, the em-dashes in `comet_visualization_shells.py`).

---

*Ledger note written July 2026 with Anthropic's Claude Opus 5.*
