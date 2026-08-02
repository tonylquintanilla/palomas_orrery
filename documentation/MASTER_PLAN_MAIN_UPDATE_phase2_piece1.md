# Master Plan Update — Phase 2 Piece 1 Landed

**Built on `373c6d8be9e0b5d06b0d5b445219e0d6d152fa13`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).**

Three targeted edits. Each shows the OLD text to find and the NEW text
to replace it with.

---

## Edit 1: §5a "Next Step" — detour status block (lines ~832-862)

### FIND (old):

```
Detour status as of 2026-07-31: design and ledger phases CLOSED; **scanner
Phase 1 (1a-1f) COMPLETE.**

Phase 1 built by Opus 5 across four sessions, orchestrated by Opus 4.6
(predesign) and reviewed by Opus 5 (predesign review caught four factual
errors in the orchestration draft). Final scanner state: Tier 1 171,
Tier 2 644, Tier 3 62, Tier 4 2 (879 findings / 116 files). Tier 1 is
132 baseline + 39 newly-visible temperature claims in climate modules
(tracked separately as L-175, same pattern as L-173). Phase 1 measured
arc: 145 -> 156 (1a) -> 156 (1b) -> 133 (1c) -> 132 (L-174) -> 171
(1d/1e/1f).

Also landed: build_pinned_values() citation-bleed flaw fixed (shared
predicate extracted, zero measured impact, defensive); No Shadow Constants
[CRITICAL] convention added to provenance-discipline v1.3; shadow
constants in comet_visualization_shells.py deleted and properly imported.

All nine cluster items (L-154-162) have their own ledger entries. L-162
closed (CENTER_BODY_RADII naming). L-163 role side closed; domain side
deferred into the cluster.

Still open under L-156: D8.5 (retire or keep Option A); Phases 2-4.

NEXT: L-157 and L-161 (the two Gemini cross-check sweeps -- shell-config
geometry and display-string sourcing) follow sequentially, not in
parallel. Then L-155/L-160 (Phase 3: pinning engine and test retirement).
Once the scanner work closes, resume L-154's own open design questions
(geometry-building approach, legend behavior, artifact sequencing --
captured in HANDOFF_gallery_feature_layer_L154_resume.md), then build
Artifact 2.
```

### REPLACE WITH:

```
Detour status as of 2026-08-01: design and ledger phases CLOSED;
**scanner Phase 1 (1a-1f) COMPLETE; Phase 2 Piece 1 (D4 scanner
mechanism) COMPLETE.**

Phase 1 built by Opus 5 across four sessions, orchestrated by Opus 4.6
(predesign) and reviewed by Opus 5. D8.5 (Option A retirement) closed as
a Phase 1 follow-on. Phase 1 measured arc (the instrument got honest):
145 -> 156 (1a) -> 156 (1b) -> 133 (1c) -> 132 (L-174) -> 171
(1d/1e/1f) -> 210 (D8.5).

Phase 2 Piece 1 (2026-08-01, Opus 5): scanner mechanism for the
V_CROSS_CHECKED (V2) rung. parse_cross_checks() parser, scoring
branches requiring source evidence AND two distinct checker annotations,
diagnostics subsection, test_cross_checked.py (16 tests). Five-model
competitive design review (GPT x2, Opus 5 x2, Fable 5) — the competitive
pattern produced genuine discovery (worksheet inventory error caught by
one reviewer only, a live false-positive regex hazard caught by another
only). Mechanism live, zero population until annotations written.

Also landed across Phase 1 + follow-ons: build_pinned_values()
citation-bleed flaw fixed; No Shadow Constants [CRITICAL] convention
added to provenance-discipline (now v1.4); shadow constants in
comet_visualization_shells.py deleted and properly imported; D8.5 Option A
retired (23 findings to Tier 1) and staleness credit removed (16 findings
to Tier 1).

Current scanner state at HEAD (373c6d8): Tier 1 210, Tier 2 605, Tier 3
62, Tier 4 2 (879 findings / 117 files).

All nine cluster items (L-154-162) have their own ledger entries. L-162
closed (CENTER_BODY_RADII naming). L-163 role side closed; domain side
deferred into the cluster.

Still open under L-156: Phase 2 Tracks 1-2, Phases 3-4.

NEXT: Phase 2 Track 1 -- complete the competitive pattern for the 15
files with April 2026 Gemini worksheets (Claude independently verifies
same claims, Tony compares, convergent claims get annotated by Opus 5).
Then Track 2 (new worksheets for uncovered files, starting with
celestial_objects.py). Then L-157/L-161 (source genuinely uncited
findings). Then L-155/L-160 (Phase 3: pinning engine and test
retirement). Once the scanner work closes, resume L-154's own open design
questions (geometry-building approach, legend behavior, artifact
sequencing -- captured in HANDOFF_gallery_feature_layer_L154_resume.md),
then build Artifact 2.
```

---

## Edit 2: §6 — provenance cluster status (lines ~899-926)

### FIND (old):

```
**L-154-162 — Provenance scoring model fix (the whole cluster).**
✓ Design CLOSED, ✓ ledger formalization CLOSED, ○ scanner build NOT
STARTED. Originally surfaced while scoping L-154's feature-rendering JS
layer, and still gates it. Design by Fable 5, reviewed by Sonnet 5
(amendments: D2, D5, D7 changed; L-161/L-162 added); broad-review pass by
Fable 5 (2026-07-26) caught two stale claims (L-154's resume handoff
wrongly asserted its resolver bug fixed; L-163's Gap text wrongly read
open) since corrected. All nine items now have their own ledger DETAIL
blocks (`LEDGER_CONSOLIDATED.md`, section W.Active) -- previously
handoff-only. The one open design fork (Vulnerability ladder: how the
scanner should treat cross-checked vs. merely-cited values) closed
2026-07-27 via a three-AI calibration round (Gemini 3.1 Pro, GPT 5.5,
Fable 5, Sonnet 5 synthesis, Tony's final call) -- full ladder, the
runtime-vs-frozen-literal rule for derived values, and the evidence base
behind it (four historical incidents from this project's own record, not
just the two the calibration worksheet opened with) are in L-156 and
L-158. Full detail also in `PREDESIGN_HANDOFF_provenance_scoring_and_gallery_scanner.md`,
`DESIGN_HANDOFF_provenance_scoring_and_pinning.md`,
`DESIGN_REVIEW_provenance_scoring_and_pinning.md`, and
`REVIEW_provenance_refactor_cluster_scoping.md`. Sequencing unchanged:
scoring fix (L-156) and in-scanner pinning (L-155/L-160) build first
(Opus 5); L-157 (shell config Gemini cross-check) and L-161 (display-
string Gemini sweep) follow, sequentially through the same Mode 7 relay
channel rather than as parallel threads -- both now require the
worksheet be drafted blind (no Claude-derived figures included), a
requirement added directly from a near-miss already caught once in this
project's own history. L-154 unblocks once the build closes.
```

### REPLACE WITH:

```
**L-154-162 — Provenance scoring model fix (the whole cluster).**
✓ Design CLOSED, ✓ ledger formalization CLOSED, ✓ scanner Phase 1
(1a-1f) COMPLETE, ✓ Phase 2 Piece 1 (D4 mechanism) COMPLETE, ○ Phase 2
Tracks 1-2 IN PROGRESS. Originally surfaced while scoping L-154's
feature-rendering JS layer, and still gates it. Design by Fable 5,
reviewed by Sonnet 5; broad-review by Fable 5 (2026-07-26). All nine
items have their own ledger DETAIL blocks. The vulnerability ladder fork
closed 2026-07-27 via three-AI calibration. Full detail in L-156, L-158,
and the design handoff / design review / predesign documents.

Scanner Phase 1 (1a-1f, Opus 5, 2026-07-29 through 2026-08-01): scoring
model rebuilt. D8.5 follow-on retired Option A and staleness credit.
Phase 1 measured arc: 145 -> 210 (the instrument got honest -- false
positives fixed first, then false negatives surfaced).

Phase 2 Piece 1 (D4, Opus 5, 2026-08-01): V_CROSS_CHECKED (V2) scanner
mechanism. Five-model competitive design review. V2 requires source
evidence AND two distinct checker annotations via competitive pattern.
Mechanism live, zero population. Phase 2 Tracks 1-2 (backfill) next.

Cross-check methodology updated: the competitive pattern (same worksheet
to two models independently, Tony compares) replaces the earlier
"blind-check" framing. Both models see the claims; the discipline is
independent sourcing, not blindness to the values. Gemini stays in the
cross-check role alongside Claude. GPT as tiebreaker on divergent claims.
L-154 unblocks once the scanner work closes.
```

---

## Edit 3: Closing summary (last ~12 lines of the file)

### FIND (old):

```
Base: orrery @ `17913aef` / gallery @ `22c947c9`.
Phase 0 closed. Phase 1a vocabulary delivered. A/B fork resolved: B′.
Phase 1b builder built, offline-verified (L-098), and Layer 2 live-Horizons
fully tested and closed -- L-149 and L-118 both DONE; L-150/L-151 still
decided, not built.
Next: write the feature-rendering JS layer (ring/shell/belt consumers) --
that's what actually stands between here and attempting Artifact 2
(Jupiter/Saturn) Mode 5. Independently, Layer 3 (nightly Task Scheduler) is
enabled and its core mechanism proven, but has a known intermittent
promotion-step failure under unattended execution (S3a addendum, July 24)
-- worth watching a few more nightly cycles before trusting it fully
hands-off.
Solar System Explorer live at palomasorrery.com/interactive.html.
```

### REPLACE WITH:

```
Base: orrery @ `373c6d8` / gallery @ `22c947c9`.
Phase 0 closed. Phase 1a vocabulary delivered. A/B fork resolved: B′.
Phase 1b builder built, offline-verified (L-098), and Layer 2 live-Horizons
fully tested and closed -- L-149 and L-118 both DONE; L-150/L-151 still
decided, not built.
Scanner detour: Phase 1 (1a-1f + D8.5) COMPLETE. Phase 2 Piece 1 (D4
scanner mechanism) COMPLETE -- V2 rung live, zero population. Phase 2
Track 1 NEXT: Claude's cross-check worksheets for April-worksheeted files,
Tony compares against Gemini's April results, Opus 5 inserts converged
annotations.
Next after scanner work: write the feature-rendering JS layer
(ring/shell/belt consumers) -- that's what stands between here and
attempting Artifact 2 (Jupiter/Saturn) Mode 5. Layer 3 (nightly Task
Scheduler) enabled with known intermittent promotion-step glitch (S3a
addendum, July 24).
Solar System Explorer live at palomasorrery.com/interactive.html.
```
