# Prompt to Opus 5 — Review the Phase 1d/1e/1f Predesign

**Built on `9bb874d9f4e84aab1ffc38a7d9beccd934f05344`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).**

---

## Context

You are the designer and builder for Phase 1, sub-steps 1d/1e/1f of the
provenance scanner refactor (L-156). You built 1c successfully (see
`documentation/AS_BUILT_L156_phase1c.md` in the repo).

An Opus 4.6 session prepared a predesign handoff for your review
(attached below). It maps the scope, verifies the current state against
the live ledger, documents what's decided, and flags open questions. It
does not propose designs — that's your job.

Tony Quintanilla is the integrator. He mediates between sessions, holds
sole commit authority, and makes all judgment calls.

## What Tony is asking you to do right now

**Review and comment on the predesign — not build yet.**

Specifically:

1. **Verify the scope.** Does the predesign correctly capture what 1d,
   1e, and 1f require? Anything missing, mis-scoped, or contradictory
   relative to what you know from the 1c build?

2. **Flag problems.** Anything in the predesign that would cause trouble
   during the build — wrong assumptions, stale measurements, missing
   dependencies, ambiguous boundaries?

3. **Confirm or challenge the sequencing.** The predesign recommends 1f →
   1d → 1e. Does that order work from a builder's perspective? Would you
   prefer a different order, or do all three in a single pass?

4. **Note any design questions** you'd want resolved before building.
   The predesign surfaces one explicitly (1d piece 1: the detection
   mechanism for frozen copies). Are there others?

5. **Confirm the verification plan** (predesign section 8). Is it
   complete given the 1a/1b/1c precedent, or does this build need
   something additional?

Do not start building. Return your review to Tony; he'll bring it back
for integration before the build session starts.

## Two things from your own system card worth keeping in mind

Your system card (July 24, 2026) documents two tendencies that are worth
being aware of for this work:

**Self-verification loops.** In open-ended tasks, you've been observed
spending excessive time building verification pipelines at the expense of
the primary deliverable. For this build: the verification plan is already
defined (section 8 of the predesign). Deliver the patch first, then
verify per that plan. Don't build a verification framework.

**Scope over-engineering.** You tend to over-emphasize marginal edge
cases. For scanner regex changes, this could mean spending time on
corner-case patterns that never appear in the real corpus. The predesign's
scope boundaries (sections 3 and 6) are deliberate — work within them.
If you find a genuine gap, flag it for Tony rather than expanding scope
yourself.

Neither of these surfaced during your 1c build, which was clean and
well-bounded. These are notes for awareness, not warnings.

## One convention added since your last session

The provenance-discipline skill is being bumped to v1.3 (pending Tony's
push) with a new section:

> ## No Shadow Constants [CRITICAL]
>
> Modules must not carry local copies of values that exist in
> `constants_new.py`. Import through the established shim
> (`planet_visualization_utilities`) or directly from `constants_new.py`.
> A local literal that numerically matches a tracked constant is a frozen
> copy — it won't follow if the source value updates, and it bypasses
> the scanner's citation chain even when the number is correct today.
>
> This is the code-side complement to the scanner's
> `build_pinned_values()` check: the scanner can flag a suspicious match,
> but the standing rule is that these should never be introduced in the
> first place. When found, delete the local definition and replace it
> with a proper import — do not add a `# Source:` comment to the local
> copy, because that would cite-to-clear a structural problem rather
> than fix it.
>
> Known precedent: `comet_visualization_shells.py` lines 492-493
> (`SUN_RADIUS_KM`, `KM_PER_AU` hardcoded despite `KM_PER_AU` already
> being imported) and line 602 (`SUN_RADIUS_AU` computed from the two
> hardcoded values). Same failure class as the `close_approach_data.py`
> stale-copy bug that originally motivated `test_constants_provenance.py`.

This convention is the WHY behind 1d piece 1 (scanner enforcement) and
1f (code fix). Treat it as decided and binding.

## Reference documents to read from the repo

Before reviewing, pull and read these from live HEAD:

- `LEDGER_CONSOLIDATED.md` — entries L-156, L-158, L-078, L-173, L-174
- `documentation/DESIGN_HANDOFF_provenance_scoring_and_pinning.md`
- `documentation/DESIGN_REVIEW_provenance_scoring_and_pinning.md`
- `documentation/AS_BUILT_L156_phase1c.md`
- `skills/provenance-discipline/SKILL.md` (currently v1.2; v1.3 pending)
- `skills/safe-file-editing/SKILL.md`

## The predesign handoff follows below

[Attach: PREDESIGN_HANDOFF_phase1_d_e_f.md]

---

*Prompt drafted July 31, 2026 by Claude Opus 4.6 at Tony's request.*
