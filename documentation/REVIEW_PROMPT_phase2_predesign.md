# Competitive Review Prompt — Phase 2 Predesign

**Built on `d03f586196bc07e8c4cb6f8435e16ac85de194b9`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Verify fresh — this is stated, not assumed.**

---

## Your role

You are reviewing a predesign document for a provenance scanner build.
You have no prior context on this project beyond what this prompt
provides. Review independently — do not assume the design is correct
because it sounds confident. Flag problems, gaps, and things that won't
work. Also flag things that are well-designed. Be specific.

Tony Quintanilla is the integrator. He will compare your review against
an independent review from a different model. Convergence builds
confidence; divergence flags where to dig.

---

## Project context (minimum needed to review)

**Paloma's Orrery** is a Python/Plotly solar system visualization suite.
It includes a provenance scanner (`provenance_scanner.py`) that audits
every numeric claim in the codebase — hover text values, physical
constants, display strings — and scores each one on two axes:

- **Criticality** (C): how bad is it if the value is wrong? Scored 1-5.
- **Vulnerability** (V): how likely is it to be wrong? Scored 1-4.

The product C × V gives a tier: Tier 1 (16-20, "FIX NOW") through
Tier 4 (1-4, "LOWEST PRIORITY").

The vulnerability ladder has four rungs:
- **V1 FETCHED** — from a live authoritative pipeline at runtime
- **V2 CROSS_CHECKED** — independently verified by multiple models
  against primary sources (currently EMPTY — nothing sets this yet)
- **V3 SOURCED** — has a `# Source:` citation comment but never
  independently verified
- **V4 RECALLED** — no citation at all

Phase 1 (just completed) fixed the scanner's scoring model. Phase 2
activates the V2 rung by teaching the scanner to recognize a new
annotation form and backfilling it onto already-verified claims.

**The competitive pattern:** cross-checking means the same fact-check
worksheet goes to two AI models independently (same claims, independent
research, independent source citations). The project owner compares.
Convergence = confidence. Divergence = investigate further. This is
NOT one model grading another's output.

**Anti-gaming rule:** the project has a strict "never cite-to-clear"
principle. A `# Source:` comment must reflect real sourcing, not a
magic word to lower a score. The same applies to `# Cross-checked:` —
the annotation must include a traceable reference to the actual
verification document.

---

## The predesign to review

[Paste the full predesign document here]

---

## What to evaluate

1. **Scanner mechanism (Piece 1):**
   - Will the `has_cross_check()` function as described correctly
     recognize the annotation form? Are there edge cases that would
     produce false positives or false negatives?
   - Is the scoring change in `score_unit()` correctly ordered? Could
     a valid cross-check annotation fail to score V2, or could an
     invalid one succeed?
   - Does the anti-gaming rule (no parenthetical = no V2) actually
     work as described? Could it be circumvented?
   - Are the test cases sufficient? What's missing?

2. **Backfill plan (Piece 2):**
   - Is the Track 1 approach sound — completing the competitive
     pattern by having Claude independently verify the same claims
     Gemini already checked?
   - Are the file categorizations correct (which files have worksheets,
     which don't, which need sourcing first)?
   - Is anything missing from scope that should be in Phase 2?

3. **Integration risks:**
   - Could this change break existing scoring for files that don't
     have `# Cross-checked:` annotations?
   - The predesign says "population conservation" — total findings
     don't change, only tiers. Is that actually true given the
     described mechanism?
   - Does the self-scan issue (the scanner scans its own code) create
     any risk from the new function/constants?

4. **Anything else:**
   - Gaps, unstated assumptions, things that sound right but won't
     work in practice.

---

## How to respond

Structure your review as:

- **What's sound** — things you've checked and agree with
- **Concerns** — things that might not work, with specifics
- **Questions** — things you can't evaluate without more information
- **Suggestions** — improvements, not just problems

Be direct. A "looks good" without specifics is not useful. A specific
concern about an edge case is.

---

*Review prompt prepared August 1, 2026 by Claude Opus 4.6.*
