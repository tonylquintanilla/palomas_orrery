# L-156 cleanup — paste-ready replacement

This replaces the entire L-156 entry (from `#### [L-156]` through the
`---` separator before `#### [L-157]`). The content is the same; the
structure is reorganized from a chronological build log into a reference
document that a future session can scan without reading 400 lines of
narrative.

The Opus 5 ledger note (LEDGER_NOTE_L156_phase1_d_e_f.md Block 1) is
already pasted at HEAD. This cleanup folds it in and adds the
build_pinned_values() fix (which landed after that note was written).

---

#### [L-156] Provenance scanner scoring model fix — criticality (category-based) + vulnerability recalibration + comprehensive sweep
<!-- L:156 status:OPEN upd:2026-07-31 section:W.Active flag: rice:5/4/80/3 -->

**What.** `provenance_scanner.py`'s scoring mis-prioritized the data this
cluster depends on: foundational constants (`SUN_RADIUS_KM`,
`KM_PER_AU`, `CENTER_BODY_RADII`) scored low because criticality was
resolved by direct-import-count, so a constant consumed indirectly (via a
derived dict) scored as if barely used.

**Scanner state at HEAD (post-Phase-1, `b813aa6`):** Tier 1 171, Tier 2
644, Tier 3 62, Tier 4 2, total 879 across 116 files. Tier 1 is
132 baseline + 39 newly-visible temperature claims (tracked separately as
L-175).

### Decided constraints (design handoff + design review + Tony)

These are settled. Future builds work within them.

**Criticality.** Two categories: MEASURED (C=5) and RELATIONAL (C=4). Not
consumer-count-based. Ring geometry in MEASURED (Tony: "the rings are
better defined"). Orbital period and radius share the top tier (Tony:
"these are fundamental data"). Explicit `undetermined` sentinel for
unclassifiable items, with its own banner.

**Role-veto amendment (ratified 2026-07-29).** Role overrides name match
when the module's functional role is non-narrative. Without it,
`HUB_THRESHOLD`, `MAX_DATA_AGE_DAYS`, and
`PERFRAME_INDICATOR_RADIUS_FACTOR` all scored MEASURED through generic
stems.

**Vulnerability ladder (D3, decided 2026-07-27).** Four rungs via
three-AI calibration (Gemini 3.1 Pro, GPT 5.5, Fable 5), Sonnet 5
synthesis. V1 FETCHED (live pipeline). V2 CROSS-CHECKED (never
auto-promotable to V1; requires structured, dated annotation with
blind-check field). V3 SOURCED (cited but unchecked, merged with stale
per Tony). V4 RECALLED (no citation). Derived values inherit weakest
input's rung once derivation logic clears one cross-check; a hardcoded
literal inherits nothing (plain V3).

**Tier-1 exit.** Permanent banner, never auto-exit gate, at any threshold
(D7, design review 3c, Tony confirmed). The only hard exit-code gate is
L-155's pinning checks (Phase 3). Errata:
`documentation/HANDOFF_phase1_1d_to_1f.md` at HEAD still describes a
deferred exit-gate flip — this is wrong; superseded by the design review
and `AS_BUILT_L156_phase1d_e_f.md`.

**Tier labels.** Tier 1 keeps "FIX NOW" (action directive, not status
claim — Tony accepted). Tiers 2/3/4 neutral score-band names: REVIEW,
LOW PRIORITY, LOWEST PRIORITY.

**Block inheritance.** Strict containment, narrowest block wins (Tony
confirmed via 1c build). No outward fallback — if a block is uncited,
strings inside it stay uncited even if a parent block is cited. This
keeps L-173's findings visible.

**No Shadow Constants [CRITICAL].** provenance-discipline v1.3. Local
copies of `constants_new.py` values must be deleted and replaced with
proper imports. Never cite-to-clear a structural problem.

### Phase 1 build history (1a–1f: COMPLETE)

**1a (2026-07-29).** Landed D1 (MEASURED/RELATIONAL), D2 (`undetermined`
sentinel), D3 (V-ladder scoring), D8.3 (magnetosphere vocabulary), D8.4
(comet un-grandfathering), role-veto amendment. Tier 1 145 → 156 (growth
is correct — raising criticality promotes previously-buried uncited
facts). 5 undetermined. 781 total.

**1b (2026-07-29).** V-ladder scoring applied across all findings. Tier 1
156 (unchanged — invariant held). Tier 2 181 → 563, Tier 3 430 → 60,
Tier 4 14 → 2. 781 conserved.

**1c (2026-07-30).** Citation-block inheritance via AST walk
(`build_citation_block_table()`, `resolve_block_citation()`). Tier 1
156 → 133. 23 shell_configs.py findings moved Tier 1 → Tier 2 (21
SHELL_CONFIGS, 2 CUSTOM_SHELLS). 18 genuinely uncited findings left
untouched (tracked as L-173). Design departure: strict containment chosen
over narrowest-cited-containing, making L-173 findings visible by rule
rather than by accident of the data.

**L-174 (1c consequence, 2026-07-30).** Citations pitched one block too
far out for the resolver to see (ring_params line 959). Fixed by
repeating citation at entry level. Tier 1 133 → 132. Permanent diagnostic
added (`SHADOWED_STRINGS`, `DEEP_CITATIONS`).

**1d (2026-07-31, Opus 5).** Three pieces:
- **Piece 1 (shadow-constant detector):** built as dedicated
  `scan_shadow_constants()` + `build_cited_constant_names()`, diverging
  from the predesign's Option A amendment. Three measured reasons: Option A
  only inspects display strings (shadow constants are function-local
  assignments the scanner never extracts); amending it would demote 9
  unrelated findings toward Tier 1; value-only matching gives 77 hits vs
  2 for name+value. Option A untouched; D8.5 still open.
- **Piece 2 (citation-form recognition, Gap item 7):** author-year
  parenthetical pattern added to SOURCE_PATTERNS, both `(Author et al.,
  YYYY)` and `(Author et al.)` forms. Measured: 13 findings Tier 1 →
  Tier 2, population conserved.
- **Piece 3 (temperature units, L-078(d)):** temperature alternatives
  added to NUMERIC_CLAIM_RE. Tier 1 +61 (96 total new findings). Largest
  tier-moving change in Phase 1. All real uncited temperature claims in
  climate modules. Tracked as L-175.

**1e (2026-07-31, Opus 5).** Tier-1 banner (bordered, informational, no
exit code). Tier labels neutralized (2/3/4); Tier 1 keeps "FIX NOW".
Code carries a comment naming design review 3c and the superseded
document.

**1f (2026-07-31, Opus 5).** Shadow constants deleted in
`comet_visualization_shells.py` (lines 492-493, 602). `SUN_RADIUS_KM`
and `SOLAR_RADIUS_AU` imported through shim. Runtime-verified
value-preserving. Fire-then-silence test: 1d detected 3 shadow constants,
1f silenced them.

**build_pinned_values() bleed fix (2026-07-31, Opus 5 follow-on).**
Extracted shared `constant_has_own_citation()` predicate routed through
both `build_pinned_values()` and `build_cited_constant_names()` —
eliminates the 10-line window bleed where uncited constants could inherit
a neighbor's citation. Measured impact: zero (all 34 constants in
`constants_new.py` already carry own citations), but defensive against
future additions. test_provenance_1d.py 15 → 20 (5 predicate tests
added). `test_both_pinned_builders_agree` asserts the two callers stay
synchronized.

**Phase 1 measured arc:** Tier 1: 145 → 156 (1a) → 156 (1b) → 133 (1c)
→ 132 (L-174) → 171 (1d/1e/1f, of which 132 → 119 from piece 2, offset
by +61 newly-visible from piece 3).

### Observations (not fixed, tracked)

**Em-dashes in comet_visualization_shells.py.** Three pre-existing
non-ASCII bytes (em-dashes), one inside a display string. Tony approved
fixing — separate edit, changes user-visible output.

**Patch scripts in repo root → documentation/.** Seven committed patch
scripts moved to `documentation/` to clear self-scan Tier-1 noise.
Complete.

### What remains open under L-156

**D8.5 (retire or keep Option A).** `build_pinned_values()` and Option A
scoring are still live. The bleed flaw is fixed but the mechanism itself
may not be worth keeping. Design question, not yet decided.

**Phase 2 (D4 cross-checked annotation backfill).** Next in the original
plan. Gated on Phase 1 (now complete).

**Phase 3.** L-155 (pinning engine), L-160 (retire
`test_constants_provenance.py`, gated on L-155), and MODULE_DOMAIN_MAP /
DOMAIN_LABELS import from `module_atlas.py` (L-163 review amendment).

**Phase 4.** L-157 / L-161 (Gemini cross-check sweeps), L-159
(disclosed-approximation enforcement).

### Ref

`provenance_scanner.py`; `constants_new.py`;
`data/provenance_exceptions.json`;
`documentation/provenance_audit_handoff_v1.md` (Arrokoth/Parker
precedent); `ADDENDUM_v23_design_session_narrative.md` (anchoring
near-miss); `HANDOFF_addendum_phase1_and_uranus_cleanup.md`,
`HANDOFF_provenance_phase1_v17.md` (Gemini cross-check itself wrong);
`MANIFEST_bow_shock_and_dipole_cone_v1.md` (blind-pass positive case);
`DESIGN_HANDOFF_provenance_scoring_and_pinning.md`;
`DESIGN_REVIEW_provenance_scoring_and_pinning.md`;
`documentation/AS_BUILT_L156_phase1c.md`;
`documentation/AS_BUILT_L156_phase1d_e_f.md`;
`documentation/PREDESIGN_HANDOFF_phase1_d_e_f_R1.md`;
`documentation/REVIEW_predesign_1d_1e_1f.md`;
`documentation/BUILD_phase_1c_prompt.md`;
`documentation/patch_phase1c_citation_inheritance.py`;
`documentation/patch_phase1_d_e_f.py`;
`documentation/patch_pinned_values_bleed.py`;
`test_provenance_1d.py`; `test_citation_inheritance.py`;
L-155; L-157; L-158; L-159; L-161; L-162; L-163; L-173; L-174; L-175.
