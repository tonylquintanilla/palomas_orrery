# Cross-Check Comparison Prompt — Mars Visualization

**Built on `8d7c6074c020123917716b47853880f3a5b492b8`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Verify fresh — this is stated, not assumed.**

---

## Your role

You are Claude Opus 4.6, orchestrating the cross-check comparison for
`mars_visualization_shells.py` — the first file in L-156 Phase 2
Track 1.

Two independent worksheets exist:
- **Gemini's leg (April 2026):** `documentation/worksheet_mars_visualization.md`
  in the repo. Read this now — it is safe to read; Claude's independent
  research is already complete.
- **Claude's leg (August 2026):** attached to this prompt (the uploaded
  file `worksheet_claude_mars_visualization.md`).

Your job: lay them side by side, compare claim by claim, and present
Tony with a convergence/divergence report so he can make the annotation
decisions.

Tony Quintanilla is the integrator. He compares, judges, and decides.
Divergences that can't be settled in discussion go to GPT as a
tiebreaker.

---

## What to do

1. **Verify HEAD.** Record the SHA.

2. **Read both worksheets.** Gemini's from the repo, Claude's from the
   upload.

3. **Compare claim by claim.** For each claim Claude verified (M1-M9):
   - Did Gemini check the same claim?
   - If yes: do the values agree? Do the sources agree or at least not
     conflict?
   - **Convergent:** both models independently found the same value
     from different (or overlapping) authoritative sources.
   - **Divergent:** the models disagree on the value, or one found an
     error the other didn't.
   - **Coverage gap:** one model checked something the other didn't.

4. **Present the comparison** as a table Tony can act on:

   | Claim | Gemini | Claude | Converge? | Notes |
   |-------|--------|--------|-----------|-------|

5. **Address Claude's four divergences (D1-D4).** Did Gemini's
   worksheet catch the same issues? If Gemini confirmed the values
   Claude flags as wrong, that's a divergence between the worksheets —
   flag it for Tony.

6. **Produce a recommendation** for each claim:
   - **Annotate:** both models agree, source evidence exists.
   - **Fix first:** the value in the code is wrong — correct it, then
     annotate.
   - **Discuss:** the models disagree and you can't resolve it from the
     evidence.
   - **GPT tiebreaker:** the models disagree, the evidence is
     ambiguous, send to GPT.

---

## Context

This is the competitive pattern from the provenance-discipline skill
(v1.4). The value comes from convergence (high confidence) or divergence
(investigate further). The scanner's V_CROSS_CHECKED (V2) rung requires
source evidence AND two distinct checker annotations. Only convergent,
sourced claims get annotated.

Claude's worksheet flagged a scope question: row-per-claim vs
row-per-finding. Tony needs to decide that before scaling to larger
files (Earth at 27 findings, info_dictionary at 124).

---

## Documents to read from the repo

- `documentation/worksheet_mars_visualization.md` — Gemini's April leg
- `mars_visualization_shells.py` — the source file with the claims
- `documentation/PREDESIGN_phase2_cross_checked_annotation_R2.md` —
  Phase 2 design context
- `skills/provenance-discipline/SKILL.md` — v1.4
- `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md` — project context
- `documentation/MASTER_PLAN_INTERACTIVE_GALLERY_SUMMARY.md` — current
  status

The Claude worksheet is uploaded, not in the repo.

---

*Comparison prompt prepared August 1, 2026 by Claude Opus 4.6.*
