# Predesign Handoff -- Phase 1, sub-steps 1d / 1e / 1f (L-156)

Tony Quintanilla, PE | Claude Opus 4.6 (orchestration) | July 31, 2026

**Revision 1** — incorporates corrections from Opus 5's review
(`REVIEW_predesign_1d_1e_1f.md`). Four factual errors in the original
predesign are corrected below; changes marked **[R1]** at point of fix.

**Built on `4b6b5c121745a6d69cf2d0cfdf8a07ff37e0245a`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Verify fresh — this is stated, not assumed.**

Gallery repo not touched by this work. Pin for the record only if needed
at build time.

**Type:** PREDESIGN HANDOFF (zero code). Ground-truth verification, scope
definition, and measurements for the Opus 5 design/build session.

**Companion:** `documentation/AS_BUILT_L156_phase1c.md` (built on `cf061d7`);
`documentation/DESIGN_HANDOFF_provenance_scoring_and_pinning.md` (Fable 5);
`documentation/DESIGN_REVIEW_provenance_scoring_and_pinning.md` (Sonnet 5);
`REVIEW_predesign_1d_1e_1f.md` (Opus 5's review of the v0 predesign).

**Supersedes:** the v0 predesign (`PREDESIGN_HANDOFF_phase1_d_e_f.md`),
which contained four factual errors corrected here.

---

## 0. Who does what

**Opus 5** is the designer and builder for 1d, 1e, 1f. This document
prepares the ground: verified scope, current measurements, decided
constraints, open questions. Design calls and build execution belong to
Opus 5, within the boundaries documented here.

**Tony** mediates, reviews, and holds sole commit authority.

**This document (Opus 4.6)** is orchestration only. It does not propose
design alternatives or resolve open questions — it surfaces them.

---

## 1. Current scanner state (verified against ledger, not re-measured)

These are the last measured counts, from 1c + L-174, recorded in the
ledger at HEAD:

| Tier | Count | Note |
|------|------:|------|
| 1    |   132 | after 1c (133) and L-174 fix (-1) |
| 2    |   587 | after 1c (586) and L-174 fix (+1) |
| 3    |    61 | 60 real + 1 self-scan artifact (CITATION_LOOKBACK_BLOCK) |
| 4    |     2 | |
| Total|   782 | 781 real + 1 self-scan artifact |

**Builder obligation:** re-measure from a fresh scan at session-start
HEAD before any prediction is trusted. The numbers above are carried from
the ledger; they are not independently verified in this session. Note:
committed patch scripts from 1c/L-174 sitting in the repo tree will be
picked up by the self-scan, inflating the total slightly — check whether
the delta is from those files before chasing it.

---

## 2. What 1a, 1b, 1c already landed

For Opus 5's orientation — what the scanner already does that this build
extends:

**1a (criticality + V-ladder + undetermined sentinel).** Landed D1
(MEASURED/RELATIONAL categories), D2 (explicit `undetermined` outcome with
banner), D3 (four-rung V-ladder: V1 FETCHED, V2 CROSS-CHECKED, V3 SOURCED,
V4 RECALLED), D8.3 (magnetosphere unit vocabulary), D8.4 (comet
un-grandfathering). Also landed the role-veto amendment (role overrides
name match when the module's functional role is non-narrative).

**[R1] Correction: `build_pinned_values()` and Option A are still live.**
The v0 predesign said "Option A / `build_pinned_values` retired in 1a."
This is wrong. `build_pinned_values()` is live at line 1409, called at
1872. Option A's scoring logic is active at lines 1563-1577: it grants
`V_SOURCED` to uncited display strings whose numeric claims all match
pinned constant values. The design handoff's D8.5 said to retire it, but
the 1a build did not do so. This is the mechanism 1d piece 1 amends —
not a new build.

**1b (V-ladder scoring integration).** Applied the decided V scores across
all findings. Tier 2 expanded from 181 to 563; Tier 3 compressed from
430 to 60; Tier 4 from 14 to 2. Tier 1 held at 156 (highest reachable
score on the changed path = 15, below the Tier-1 floor of 16). Total 781
conserved.

**1c (citation-block inheritance).** `build_citation_block_table()` and
`resolve_block_citation()` — block-level citation inheritance via AST
walk over all `ast.Assign` at any nesting depth. Strict containment:
narrowest containing block, cited or not, stop there. 23 findings moved
from Tier 1 to Tier 2 (all in `shell_configs.py`). 18 genuinely uncited
findings (L-173) left untouched.

**L-174 (citation-level-mismatch diagnostic).** Fixed the one live
mis-scored finding (`ring_params` line 959) by adding repeat citations at
entry level. Added `SHADOWED_STRINGS` and `DEEP_CITATIONS` diagnostics.
Tier 1 133 -> 132.

---

## 3. The three sub-steps, scope verified against the live ledger

### 3a. Sub-step 1d — three pieces, all scanner recognition work

**Piece 1: frozen-copy detector (L-156 Gap item 5, also L-158 piece 1).**

**[R1] Corrected framing:** `build_pinned_values()` is live and Option A
is actively scoring. The current behavior: Option A grants `V_SOURCED`
to any uncited display string whose numeric claims all match values from
`constants_new.py` — whether the match comes from a real import or a
hand-typed copy. The fix: amend this logic so that a bare literal
matching a pinned value is flagged "possible frozen copy — verify import"
instead of silently credited, when the module does not actually import
the matching constant by name.

Two confirmed live instances (verified in L-158's ledger note):

- `comet_visualization_shells.py` lines 492-493: `SUN_RADIUS_KM =
  695700.0` and `KM_PER_AU = 149597870.7` hardcoded locally, despite
  `KM_PER_AU` already being imported at line 42.
- `comet_visualization_shells.py` line 602: `SUN_RADIUS_AU = 695700.0 /
  149597870.7` — a derived value computed from the two hardcoded copies.

**Design question for Opus 5:** The mechanism already exists — amend
`score_unit()`'s Option A block (lines 1563-1577) and/or
`build_pinned_values()` to distinguish "matches AND is imported" from
"matches but is a bare copy." The AST can show whether a module imports
the constant's name; a value match without a name import is the flag.

**Piece 2: citation-form recognition gap (L-156 Gap item 7).**

`has_citation()` / `SOURCE_PATTERNS` only recognizes three citation
forms: `# Source:` keyword, `# Verified:` keyword, or a URL. A bare
author-year parenthetical is not recognized.

**[R1] Corrected pattern scope:** the live code carries BOTH forms:

- **With year:** `(Vecellio et al., 2022)`, `(Sherwood & Huber, 2010)` —
  in display strings and inline comments deeper in the file.
- **Without year:** `(Vecellio et al.)`, `(Sherwood & Huber)` — at the
  constant-definition level (lines 137-138 of
  `paleoclimate_wet_bulb_full.py`). These are the scanner's motivating
  instances for this piece.

The regex must handle both forms. The v0 predesign proposed matching
only `(Author et al. YYYY)`, which would miss the no-year forms —
exactly the motivating instances.

**False-positive warning (from Opus 5's review, confirmed concrete):** a
naive parenthetical pattern immediately matches `(May 2026)` — a date
in a comment, not a citation. The pattern needs explicit exclusions for
month names and similar non-citation parentheticals.

**[R1] Corrected measurement:** Opus 5 measured ~15 findings affected
(8 with years, 7 without), not the ~54 carried from the ledger. The
ledger already flagged that estimate as unreproducible. This is worth
doing on correctness grounds, but it is NOT the largest remaining
Tier-1 reducer as the v0 predesign suggested.

**Piece 3: L-078(d) — bare-degree F/C values.**

`NUMERIC_CLAIM_RE` doesn't recognize bare Fahrenheit/Celsius temperature
values as numeric claims. Per L-078's own text, this folds into 1d's
regex work — the same `NUMERIC_CLAIM_RE` pattern being edited for the
magnetosphere vocabulary (already landed in 1a) now gets `°F`, `°C`,
`degrees F`, `degrees C`, and similar suffixes.

Small, bounded, no design question — extend the existing unit vocabulary.

### 3b. Sub-step 1e — two pieces, console output and labeling

**Piece 1: Tier-1 banner.**

The scanner must print a prominent, bordered console banner when Tier-1
findings exist: something like `"132 Tier-1 findings — push gate NOT
met"`. This is purely informational — it does NOT gate the exit code.

**Decided (design review, section 3c, Tony confirmed):** Tier-1 NEVER
gets an auto-exit gate, at any threshold, ever. Not the deferred-flip
Fable proposed, not a baseline-ratchet. The banner is the brake (Tony
runs via VS Code's Run button and reads the console). The only hard
exit-code gate in the entire scanner is L-155's pinning checks (Phase 3,
not this build).

**[R1] Warning:** `documentation/HANDOFF_phase1_1d_to_1f.md` at HEAD
still describes the deferred exit-gate flip as the plan for 1e. That
document reflects Fable 5's original D7 design, which the design review
§3c explicitly superseded: "never an auto-exit gate, at any threshold,
ever." The predesign (this document) and the design review are
authoritative; the handoff at HEAD is wrong on this point. The builder
must follow the design review, not the handoff.

**Piece 2: Tier-2 label lie.**

The current Tier-2 tier label hardcodes "ALL ACCEPTED RESIDUALS — no
action required" into the tier NAME, plus a static April 2026 note. Any
new finding landing in Tier 2 gets auto-narrated as already-reviewed by
the report template itself.

**Decided (design handoff D7, design review confirmed):** tiers get
neutral score-band names only (e.g. "Tier 2 (10-15): REVIEW").
Accepted-residual status is per-finding information, marked individually
using what's already in `data/provenance_exceptions.json` and the
Accepted Residuals report block. The blanket tier-level claim is deleted.

This MUST land with or after 1d's scoring changes (per the design
handoff: D3, D4, and the label fix are one build unit — the V-ladder
recalibration repopulates Tier 2 with genuinely-open items; the blanket
label would mislabel every one of them).

### 3c. Sub-step 1f — one piece, mechanical code fix

**Delete shadow constants in `comet_visualization_shells.py` and import
properly.** Scope (Tony's decision, this session):

- Delete line 492: `SUN_RADIUS_KM = 695700.0`
- Delete line 493: `KM_PER_AU = 149597870.7`
- Delete line 602: `SUN_RADIUS_AU = 695700.0 / 149597870.7`
- Import `SUN_RADIUS_KM` through the `planet_visualization_utilities`
  shim, alongside the existing `KM_PER_AU` import at line 42.
- **[R1]** Import `SOLAR_RADIUS_AU` (not `SUN_RADIUS_AU` — that name
  does not exist in `constants_new.py`; the constant is
  `SOLAR_RADIUS_AU` at line 103). Replace all downstream references to
  the deleted local `SUN_RADIUS_AU` with `SOLAR_RADIUS_AU`.

**Broader scope (Tony's standing instruction, also decided this
session):** this is not limited to these three lines. The standing rule
is: NO local copies of constants that exist in `constants_new.py`,
anywhere in the repo. The two known instances above are confirmed; the
builder should grep for any others in the build-target file
(`comet_visualization_shells.py`) before treating the edit as complete.
A repo-wide sweep for other files carrying shadow constants is OUT OF
SCOPE for 1f but should be noted as a future item if any are found.

**Independence:** 1f has no dependency on 1d or 1e. It can land in any
order. BUT — see sequencing (section 7).

---

## 4. New convention: No Shadow Constants [CRITICAL]

Added to `provenance-discipline` skill v1.3, now pushed at HEAD
(`4b6b5c12`). The skill version line's SHA placeholder (`<SHA after
push>`) should be stamped with `4b6b5c12` when next editing the file.

> **No Shadow Constants [CRITICAL]**
>
> Modules must not carry local copies of values that exist in
> `constants_new.py`. Import through the established shim
> (`planet_visualization_utilities`) or directly from `constants_new.py`.
> A local literal that numerically matches a tracked constant is a frozen
> copy — it won't follow if the source value updates, and it bypasses
> the scanner's citation chain even when the number is correct today.
>
> When found, delete the local definition and replace it with a proper
> import — do not add a `# Source:` comment to the local copy, because
> that would cite-to-clear a structural problem rather than fix it.

This convention is the WHY behind 1d piece 1 (scanner enforcement) and
1f (code fix). Treat it as decided and binding.

---

## 5. Decided constraints (not open for redesign)

These are settled by the design handoff, design review, and Tony's direct
decisions. Opus 5 builds within them:

- **V-ladder:** V1 FETCHED, V2 CROSS-CHECKED (never auto-promotable to
  V1), V3 SOURCED (merged with STALE), V4 RECALLED. Four rungs. Decided
  via three-AI calibration round, closed 2026-07-27.
- **Criticality categories:** MEASURED (C=5), RELATIONAL (C=4), with
  `undetermined` sentinel for anything unclassifiable. Role-veto
  amendment live.
- **Tier-1 exit:** permanent banner, never auto-exit. Pinning checks
  (Phase 3) are the only hard exit gate.
- **Tier-2 labels:** neutral score-band names only. Per-finding
  accepted-residual marking.
- **Block inheritance:** strict containment, narrowest block wins.
  Decided by Tony (1c as-built section 4).
- **No Shadow Constants [CRITICAL]:** convention above. Delete and
  import; never cite-to-clear a structural problem.
- **`build_pinned_values()` / Option A still live:** amend, don't
  rebuild. The mechanism exists; 1d piece 1 changes what it does when
  a match lacks a corresponding import.
- **Scanner scans itself:** expect self-scan artifacts. Any new
  module-level constant added to `provenance_scanner.py` will appear in
  its own audit entry. Check self-scan deltas first before assuming a
  real gap appeared.
- **ASCII-only, LF-only** in all Python deliverables. Bottom-up edit
  ordering. Binary-mode I/O for patch scripts. Standard conventions per
  safe-file-editing skill v1.1.

---

## 6. What this build does NOT cover

- **L-173 (18 genuinely uncited shell_configs findings):** need real
  sourcing via Gemini worksheet, not a scoring change. Parked for Phase 4.
- **L-155 (pinning engine):** Phase 3, not this build.
- **L-160 (retire test_constants_provenance.py):** Phase 3, conditional
  on L-155 landing first.
- **L-157, L-161 (Gemini sweeps):** Phase 4.
- **L-159 (disclosed-approximation enforcement):** deferred to its own
  design pass.
- **Repo-wide shadow-constant sweep beyond comet_visualization_shells.py:**
  out of scope for 1f; note as future item if found.
- **D4 cross-checked annotation backfill:** Phase 2, not this build.
- **D5 CENTER_BODY_RADII de-dup:** already DONE (L-162, closed 2026-07-29).
- **Retiring `build_pinned_values()` / Option A:** the design handoff's
  D8.5 says to retire it, but this has not happened. Whether to retire
  it now or amend it is a design question for this session. The v0
  predesign's error of calling it "retired" does not make retirement the
  right move — that's Opus 5's call, within the constraint that the
  frozen-copy detection must work.

---

## 7. Sequencing

**[R1] Corrected from v0.** The v0 predesign recommended 1f → 1d → 1e.
Opus 5's review identified a problem: 1f deletes the only two live
instances that 1d piece 1's frozen-copy detector is meant to catch. If
1f lands first, the detector has nothing to fire on during testing.

**Revised sequencing:**

1. **1d first** (largest, shifts tier counts). Build the frozen-copy
   detector (piece 1), the citation-form recognition (piece 2), and the
   F/C vocabulary (piece 3). Run the scanner. Watch the frozen-copy
   detector fire on `comet_visualization_shells.py` lines 492-493 —
   that's the strongest available test.

2. **1f second.** Delete the shadow constants. Re-run the scanner. The
   frozen-copy findings from 1d should disappear — confirming both the
   detector and the fix.

3. **1e last** (console output, depends on understanding the final tier
   distribution). The banner text references the Tier-1 count; the label
   fix references Tier-2 semantics. Both read better after 1d's tier
   shifts have settled.

**Opus 5's review also recommended splitting into two build sessions**
rather than one, so a single audit diff doesn't have to be attributed to
four causes at once. Tony's call.

---

## 8. Verification expectations

Per the established pattern from 1a/1b/1c:

- **Base-file guard:** `EXPECTED_MD5` on `provenance_scanner.py` (for
  1d/1e) and `comet_visualization_shells.py` (for 1f), verified before
  any edit.
- **Anchored transactional patch:** bottom-up, each anchor verified to
  match exactly once, all-or-nothing, binary mode.
- **Before/after scanner run:** full audit diff reviewed line by line,
  self-scan delta checked first. The diff is the proof, not the summary
  count.
- **Regression suites:** `test_constants_provenance.py` (73/73),
  `test_citation_inheritance.py` (20/20 after L-174), both unchanged.
- **py_compile** on all deliverables and patched targets.
- **ASCII/LF gates** on all deliverables and results.
- **Idempotency check:** re-running refuses cleanly with cause named.
- **Agentic pre-test:** `provenance_scanner.py` is a devtool with no Tk
  surface, so the xvfb GUI leg does not apply. A live scan on the real
  repo plus the regression suites is the runtime-equivalent leg, on a
  throwaway clone (same as 1c's as-built section 6).

---

## 9. Errata in the document chain

Collected here so the builder knows which documents at HEAD are wrong on
which points, and doesn't have to rediscover them:

1. **`documentation/HANDOFF_phase1_1d_to_1f.md` at HEAD** describes 1e
   as including a deferred nonzero exit-gate flip. **Wrong.** Design
   review §3c explicitly supersedes: "never an auto-exit gate, at any
   threshold, ever." The authoritative sources are the design review and
   this predesign.

2. **The design handoff's D8.5** says to retire `build_pinned_values()`
   / Option A. **Not done** as of HEAD. The mechanism is live and
   actively scoring. Whether to retire it now or amend it is a design
   question for this session.

3. **`provenance-discipline/SKILL.md` v1.3** at HEAD has `<SHA after
   push>` as the SHA placeholder in the version line. Should be stamped
   `4b6b5c12` when next editing the file.

---

## 10. Reference documents

Read these before designing. The ledger entries (L-156, L-158, L-078)
are the authoritative scope; the design documents carry the reasoning.

| Document | What it carries |
|----------|-----------------|
| L-156 in LEDGER_CONSOLIDATED.md | Full gap list, all notes from 1a/1b/1c, decided constraints |
| L-158 in LEDGER_CONSOLIDATED.md | Derived-constant inheritance rule, shadow-constant instances |
| L-078 in LEDGER_CONSOLIDATED.md | Sub-item (d): F/C bare-degree fix |
| L-173 in LEDGER_CONSOLIDATED.md | The 18 genuinely uncited findings (NOT in scope) |
| L-174 in LEDGER_CONSOLIDATED.md | Citation-level-mismatch diagnostic (context for block inheritance) |
| DESIGN_HANDOFF_provenance_scoring_and_pinning.md | D1-D10, original design (partially superseded — see errata) |
| DESIGN_REVIEW_provenance_scoring_and_pinning.md | Amendments: D2 replaced, D5 expanded, D7 corrected |
| AS_BUILT_L156_phase1c.md | What 1c delivered, the mechanisms, the design departure |
| REVIEW_predesign_1d_1e_1f.md | Opus 5's review of the v0 predesign (source of corrections) |
| HANDOFF_phase1_1d_to_1f.md | Sonnet 5's orchestration prompt (CAUTION: wrong on 1e, see errata) |
| provenance-discipline SKILL.md | v1.3 at HEAD: includes No Shadow Constants [CRITICAL] |
| safe-file-editing SKILL.md | v1.1: editing discipline, patch conventions |
| project_instructions (resident protocol) | v3.32: SHA round trip, agentic pre-test, all CRITICAL gates |

---

## 11. Tony-action items from this predesign

- **(decide)** Review this revised predesign and confirm scope before
  handing to Opus 5.
- **(decide)** Whether 1d/1e/1f run as one Opus 5 session or two (Opus 5
  recommended splitting). Section 7 gives the sequencing either way.

---

*Predesign handoff written July 31, 2026 with Anthropic's Claude Opus 4.6.
Revision 1 incorporates corrections from Opus 5's review.
Zero code written or proposed. Repo read-only throughout.*
