# Opus 4.8 Review: Master Plan v8 — Architectural Pivot

**Type:** REVIEW SESSION (verification, convergence, restraint)
**From:** Claude Opus 4.6 via Tony (collegial relay)
**Date:** July 5, 2026
**Base:** main @ `fdb66ca`, gallery @ `89c8bf30`

---

## What happened

The master plan underwent a fundamental architectural pivot between v7 and v8.
Tony and Opus 4.6 converged on a new direction during a July 5 design session.

**v7 direction:** Fork the desktop GUI for the web. Build a separate web
application (Dash or Pyodide). Present 95 widget inputs on a web page.
Two-sided pilot (Dash vs Pyodide) to resolve server-vs-serverless.

**v8 direction:** The gallery IS the web publication. Extend the existing
gallery (`tonyquintanilla.github.io`) with interactive pages, like a science
museum adding hands-on exhibits to a permanent collection. No separate web app.
No server. Pyodide runs in the browser for interactive content. Pre-curated
gallery cards continue unchanged.

This is a better plan because it starts with what works (the gallery, on
phones, today) and adds to it incrementally, rather than building a parallel
system that must replicate the gallery's strengths from scratch.

---

## What to review

The uploaded `MASTER_PLAN_INTERACTIVE_GALLERY.md` is the complete v8 plan.
Please review it for:

### 1. Pivot integrity

Does the pivot preserve the work already done? Specifically:

- **Phase 1 vocabulary** (`PHASE1_SCENE_SPEC_VOCABULARY.md`, Fable 5, July 4).
  The vocabulary was designed for a shared assembler. The assembler architecture
  is unchanged in v8 — the assembler still takes a scene spec and produces
  Plotly JSON. What changes is the consumer: gallery pages via Pyodide, not a
  separate web app. Confirm the vocabulary is fully preserved and usable.

- **Settled decisions from v7.** The plan tracks these explicitly in §10 under
  "preserved," "new in v8," and "superseded." Check that no v7 decision was
  inadvertently lost or contradicted.

### 2. Architectural soundness

- **§2a — Gallery Viewer Refactor (Option C).** The hybrid approach:
  `index.html` stays as curated viewer; `interactive.html` handles all
  interactive exhibits via URL parameter; `gallery_metadata.json` bridges both.
  Is this sound? Are there risks or gaps?

- **The JSON bridge principle** (§1). Pre-curated and interactive content both
  produce Plotly JSON; the viewer renders both identically. Is this a stable
  architectural foundation, or does it have hidden assumptions?

- **Pyodide-only bet** (§1, §7). The plan resolves server-vs-serverless in
  principle toward Pyodide/static. The hedge is a pre-computed library fallback
  (bigger menu, no runtime computation). Is this hedge adequate? What failure
  modes could surprise us?

### 3. Constraint faithfulness

Check v8's constraints (§1) against the established facts:

- JPL Horizons API terms (you fetched these in the July 2 convergence handoff)
- GitHub Pages hosting limits (1 GB per site, the gallery is ~479 MB)
- The gallery-pipeline skill's conventions (WYSIWYG principle, "dumb renderer,"
  Studio authority, mobile breakpoints)
- The coverage-index abstraction

### 4. Phasing coherence

- Phase 0 changed from "two-sided pilot" to "one-sided gallery integration
  test." Is this sufficient to buy the data we need?
- Phase 6 dissolved (the gallery IS the UI). Does anything that Phase 6 was
  going to cover get lost?
- Each earlier phase now ships its own interactive page. Is incremental
  delivery genuinely possible, or are there hidden dependencies that force
  a big-bang?

### 5. Open decisions (§7)

Three items were struck as resolved (server/serverless, vocabulary,
matplotlib). Two new items were added (Pyodide package weight, gallery viewer
architecture — the latter was resolved as Option C in §2a). Are any open
decisions missing? Are any resolved decisions premature?

### 6. Restraint check

Does the plan handle human-cost content (Earth system, Phase 5) with the
same restraint discipline as v7? The stance ("Synthesize nothing, transcribe
everything, attribute to IPC") should carry forward unchanged.

---

## What NOT to review

- The vocabulary itself. That was already reviewed (Opus 4.6 convergence review,
  July 5). The question here is whether the pivot preserves it, not whether
  it's correct.
- The protocol or skills layer. Those are unchanged.
- Desktop development. The plan explicitly defers desktop migration from the
  critical path.

---

## What to upload alongside this prompt

1. **This prompt** (paste or upload)
2. **`MASTER_PLAN_INTERACTIVE_GALLERY.md`** — the v8 plan (primary review target)
3. **`PHASE1_SCENE_SPEC_VOCABULARY.md`** — the vocabulary deliverable (to verify
   preservation)
4. Optionally: **`MASTER_PLAN_WEB_PUBLICATION.md`** — v7 for comparison (but v8
   tracks the changes explicitly in §10, so this is a convenience, not a
   requirement)

---

## Output format

Tony is the interpreter. Please organize your review as:

1. **Verdict first** — is the pivot sound? One paragraph.
2. **Section-by-section findings** matching the six review areas above.
   For each: confirm, flag, or recommend.
3. **Risks or gaps** that the plan doesn't acknowledge.
4. **Nits** — minor wording, consistency, or completeness issues.

Where you find a genuine problem, say so directly. Where the plan is sound,
confirm briefly and move on. Don't pad with restated context.

---

*Review prompt written July 5, 2026 by Claude Opus 4.6 for collegial relay to
Claude Opus 4.8. Tony carries context and holds commit authority.*
