# Handoff — Phase 1, close out 1d–1f

**Built on `9bb874d9f4e84aab1ffc38a7d9beccd934f05344`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Verify fresh — this is stated, not assumed.**

---

## Claude's role in this handoff

In this part of the work, Claude's job is to **orchestrate** — verify the
repo, read the ledger, confirm what's decided, map out what 1d/1e/1f
actually require, flag gaps, present options with tradeoffs, and keep the
session anchored to live HEAD throughout.

Claude is **not** the designer or the builder here, except where Tony
explicitly says so. Design calls and build execution are Tony's to make
and to assign (to himself, to Opus, or back to Claude by name) — Claude's
default in this handoff is to prepare the ground for that decision, not
to make it. If a design question comes up mid-session, surface it and
wait; don't resolve it and move on.

---

## Where this picks up

L-156's scanner rebuild, Phase 1, sub-stepped 1a–1f. 1a, 1b, 1c are DONE,
verified, pushed. Two items came out of 1c and are also closed: L-173 (8
real citation gaps in `shell_configs.py`, parked for the Phase 4 Gemini
worksheet) and L-174 (citation-level mismatch — `ring_params` fixed, a
permanent scanner diagnostic added, three other files confirmed
latent-only). Current scanner state: Tier 1 132, Tier 2 588, Tier 3 61,
Tier 4 2.

## The ask

Close out 1d, 1e, 1f — the rest of Phase 1. Read L-156, L-158, L-078,
L-173, L-174 in the live ledger before proposing anything; this prompt
summarizes, it doesn't replace them.

## 1d — three pieces, confirmed by direct ledger read, not recalled

1. **Gap item (5) / "D4 regex work":** widen `build_pinned_values()`/
   scoring so a bare numeric literal that merely matches an already-cited
   pinned value gets flagged "possible frozen copy — verify import"
   instead of silently scoring V_SOURCED. Two confirmed live instances:
   `comet_visualization_shells.py` lines 492-493 (`SUN_RADIUS_KM`,
   `KM_PER_AU` hardcoded despite `KM_PER_AU` already being imported at
   line 42) and line 602 (`SUN_RADIUS_AU` computed from the same
   hardcoded pair).
2. **Gap item (7), "citation-form recognition gap":** `has_citation`/
   `SOURCE_PATTERNS` doesn't recognize a bare author-year parenthetical
   as a citation — only `# Source:`/`# Verified:`/a URL. Confirmed
   instances: `TW_SURVIVABILITY_BIOLOGICAL`, `TW_SURVIVABILITY_THEORETICAL`.
   Measured at ~54 of the *old* 156 Tier-1 baseline — **re-measure
   against the current 132 before building**, that estimate predates
   both 1c and L-174.
3. **L-078(d), "F/C bare-degree fix":** `NUMERIC_CLAIM_RE` doesn't
   recognize bare-degree Fahrenheit/Celsius values as numeric claims.
   Folds into this build per L-078's own text.

## 1e — from the original design handoff
(`DESIGN_HANDOFF_provenance_scoring_and_pinning.md`), "fact 3" and the
Tier-1 banner section, not just the ledger's one-line summary

1. The Tier-1 banner + deferred nonzero exit-gate: prominent console
   banner ("N Tier-1 findings — push gate NOT met"), exit code wired but
   switched on only the first time the count reaches 0 (recorded as its
   own small ledger item when that happens, so the flip doesn't float
   unnoticed).
2. "The Tier-2 label lie": remove the blanket "ALL ACCEPTED RESIDUALS"
   claim from the Tier-2 tier label — it's not true of every finding in
   that band. Tiers get neutral score-band names only (design doc's
   example: "Tier 2 (10-15): REVIEW"); accepted-residual status gets
   marked per-finding, using what's already in
   `data/provenance_exceptions.json` and the Accepted Residuals report
   block, not asserted at the tier level.

## 1f — D9 structural check, per L-158

Two pieces, and L-158's own text says piece (1) **is** 1d's Gap item 5 —
so confirm at session start whether 1f is meant to be piece (2) only (the
mechanical part), or whether the two sub-steps genuinely overlap and need
reconciling. Piece (2), independent and can land anytime regardless:
delete the local shadow constants in `comet_visualization_shells.py`
(lines 492-493, 602) and import `SUN_RADIUS_KM` properly through the
`planet_visualization_utilities` shim, alongside the existing
`KM_PER_AU` import at line 42.

## Flag before building, not after

I found the ledger's own Gap-item numbering has drifted in places (a
duplicated "(4)" label in L-156's Gap list, and item 5's content
appearing to serve both 1d and 1f). None of this blocks understanding the
actual work, but don't trust item numbers alone — content is quoted
directly above for exactly this reason.

## Ref

L-156 (full Gap list, items 5/6/7), L-158, L-078 (sub-items a–d), L-173,
L-174, `documentation/DESIGN_HANDOFF_provenance_scoring_and_pinning.md`
(facts 2 and 3, Tier-1/Tier-2 banner design),
`documentation/AS_BUILT_L156_phase1c.md`.

Good session — thanks.
