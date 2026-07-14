# Build request: Phase 2 Solar System Assembler

**To:** Claude Opus (per the master plan's model assignment — primary implementer)
**From:** Tony Quintanilla, relayed via Claude Sonnet 5 (Mode 7 collegial relay)
**Attached:** `PHASE2_SYNTHESIS_MANIFEST_v2.md`, `PHASE2_ASSEMBLER_DESIGN_HANDOFF_v0.3.md`,
`MASTER_PLAN_INTERACTIVE_GALLERY.md` (v12)

## Where this sits in the relay

Design is closed. This went through: initial handoff (v0.1) → Opus review →
extensive follow-up design conversation → handoff v0.2 → two independent
build manifests (Fable, GPT — competitive cross-check) → synthesis v1 →
two second-pass reviews → synthesis v2, incorporating both. Every open
design question got resolved or explicitly scoped out along the way — v0.3
Sections 8-9 and v2 Section 0 have the full record if you want the reasoning,
not just the conclusions. **This is a build request, not another design
pass.** `PHASE2_SYNTHESIS_MANIFEST_v2.md` is the executable contract.

## Session base — re-pin, standard discipline

Orrery HEAD `e1b2c7fca222a3490671b9c3521c5a672a07b53e`, gallery HEAD
`e864fd426a6bcffc478fe5ed9452a4dfc9159766`. Re-verify both via `git
ls-remote` before starting. If either has moved, check whether the delta
touches `data/objects_config.json`, the served cache schema, or
`tools/gallery_cache_builder.py` — those are the files v2's prerequisite
gates (Section 4) depend on. If nothing material changed, proceed and note
the new SHA in your relay back. If something did change, that's Gate 0's
job — inspect before building on top of it.

## What to actually do

1. **Read `PHASE2_SYNTHESIS_MANIFEST_v2.md` in full.** It's the contract:
   architecture (§2), scene spec/date resolution (§3), the four prerequisite
   gates F1-F4 plus L-086 (§4), mean elements as new-but-settled scope (§5),
   the seven golden artifacts (§6), hover/invariant/layer-order detail (§7),
   the L-080 harness (§8), and what's explicitly out of scope (§10).
2. **Resolve the prerequisite gates before the artifacts they block** —
   this isn't optional sequencing, it's structural: F1 before artifact 2
   (feature params move to `objects_config.json`; builder derives
   `feature_configs.json` instead of writing it empty), F3 before artifact
   4 (Halley needs a real `--first-build` on top of the already-added
   config entry), F2 before artifact 7 (two-step: add `event_link` to the
   schema, then wire the builder pass-through), F4 and L-086 before shipping
   anything publicly (plotly wheel deployed; attribution credit in place).
   Builder changes follow the full Layer discipline in the
   gallery-cache-builder skill — offline suite from a clean checkout
   (count-assertion bumps included, per that skill's own field note),
   `--dry-run`, then a real build.
3. **Build the seven artifacts in order** (§6), each against its Mode-5
   acceptance gate: harness structural checks pass in CPython, the page
   renders via Pyodide with no console errors, and Tony's visual
   confirmation — which beats all claims, per this project's standing rule.
   **Feature rendering stays JavaScript** (§2, §4 correction) — the Python
   assembler resolves and reports which features apply with what
   parameters; it does not generate feature Plotly traces itself. This was
   a real merge error caught and reversed mid-relay — worth internalizing
   why (§0 of v2), not just complying with the rule.
4. **L-080 co-evolves, starting at artifact 1** — this isn't a phase to
   front-load or postpone; each confirmed artifact both advances the
   assembler and hands the harness its next golden fingerprint (§8).
5. **For staging/session breakdown**, both original manifests (also in
   `documentation/`: `PHASE2_ASSEMBLER_BUILD_MANIFEST_v1.md` from Fable,
   `PHASE2_SOLAR_SYSTEM_ASSEMBLER_BUILD_MANIFEST_v1.md` from GPT) have
   staging content that's still structurally valid — apply v2's
   corrections on top (features-in-JS not Python, F2's two-step nature,
   mean elements as real scope) rather than following either verbatim.
6. **Route Section 9's open items back rather than deciding them
   unilaterally** — harness tolerance, comet perihelion-marker default-on
   (genuinely a Mode 5 call, don't pre-empt it), page naming, F1's exact
   config shape.
7. **Come back in stages, not as one unsupervised build.** Per this
   project's standing discipline: agentic-pre-test protocol before
   delivering any complete file (throwaway-copy rule, py_compile, headless
   smoke test); ASCII-only and LF line endings; credit line on touched
   modules; Mode 5 is the close gate per artifact, not a final review at
   the very end. A natural checkpoint is after artifact 1 (floor case +
   first L-080 fingerprint) — surface that before continuing through the
   rest, the same way this whole relay has worked in checked stages rather
   than one long unsupervised pass.

## Conventions in force (same project, same rules)

- Tag claims `[verified @<sha>]` vs. `[carried]`.
- Fetched-not-recalled: pull actual files at the SHA you're working from.
- Tony and Sonnet are the orchestrators on this relay; this build report
  comes back through that same channel.
- If you find an implementation-blocking defect in the cache builder's
  fetching logic beyond what F1-F4 already describe, route it back as its
  own decision rather than silently fixing it — per v2 §3's scope note on
  builder changes.

## Relay format on the way back

Per v2's own §Ref/final-relay expectations: final SHAs (both repos), files
added/modified, commands run, unit/integration/builder-regression results,
artifact-by-artifact status, Mode 5 evidence, any manifest deviations and
why, open risks, ledger recommendations.

---
Prompt written July 2026 by Claude Sonnet 5 for Tony Quintanilla's Mode 7 relay.
