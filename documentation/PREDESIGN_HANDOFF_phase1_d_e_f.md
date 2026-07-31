# Predesign Handoff -- Phase 1, sub-steps 1d / 1e / 1f (L-156)

Tony Quintanilla, PE | Claude Opus 4.6 (orchestration) | July 31, 2026

**Built on `9bb874d9f4e84aab1ffc38a7d9beccd934f05344`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Verify fresh -- this is stated, not assumed.**

Gallery repo not touched by this work. Pin for the record only if needed
at build time.

**Type:** PREDESIGN HANDOFF (zero code). Ground-truth verification, scope
definition, and measurements for the Opus 5 design/build session.

**Companion:** `documentation/AS_BUILT_L156_phase1c.md` (built on `cf061d7`);
`documentation/DESIGN_HANDOFF_provenance_scoring_and_pinning.md` (Fable 5);
`documentation/DESIGN_REVIEW_provenance_scoring_and_pinning.md` (Sonnet 5).

**Supersedes:** nothing. This is the first predesign for 1d-1f.

---

## 0. Who does what

**Opus 5** is the designer and builder for 1d, 1e, 1f. This document
prepares the ground: verified scope, current measurements, decided
constraints, open questions. Design calls and build execution belong to
Opus 5, within the boundaries documented here.

**Tony** mediates, reviews, and holds sole commit authority.

**This document (Opus 4.6)** is orchestration only. It does not propose
design alternatives or resolve open questions -- it surfaces them.

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
the ledger; they are not independently verified in this session.

---

## 2. What 1a, 1b, 1c already landed

For Opus 5's orientation -- what the scanner already does that this build
extends:

**1a (criticality + V-ladder + undetermined sentinel).** Landed D1
(MEASURED/RELATIONAL categories), D2 (explicit `undetermined` outcome with
banner), D3 (four-rung V-ladder: V1 FETCHED, V2 CROSS-CHECKED, V3 SOURCED,
V4 RECALLED), D8.3 (magnetosphere unit vocabulary), D8.4 (comet
un-grandfathering), D8.5 (Option A / `build_pinned_values` retired for
string scoring). Also landed the role-veto amendment (role overrides name
match when the module's functional role is non-narrative).

**1b (V-ladder scoring integration).** Applied the decided V scores across
all findings. Tier 2 expanded from 181 to 563; Tier 3 compressed from
430 to 60; Tier 4 from 14 to 2. Tier 1 held at 156 (highest reachable
score on the changed path = 15, below the Tier-1 floor of 16). Total 781
conserved.

**1c (citation-block inheritance).** `build_citation_block_table()` and
`resolve_block_citation()` -- block-level citation inheritance via AST
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

### 3a. Sub-step 1d -- three pieces, all scanner recognition work

**Piece 1: frozen-copy detector (L-156 Gap item 5, also L-158 piece 1).**

Current behavior: `build_pinned_values()` was retired in 1a (Option A
removed). But the scoring path still silently grants V_SOURCED to a bare
numeric literal that happens to match a cited constant in
`constants_new.py`, whether the match comes from a real import or a
hand-typed copy. The fix: flag these as "possible frozen copy -- verify
import" instead of silently crediting them.

Two confirmed live instances (verified in L-158's ledger note, not
re-verified this session):

- `comet_visualization_shells.py` lines 492-493: `SUN_RADIUS_KM =
  695700.0` and `KM_PER_AU = 149597870.7` hardcoded locally, despite
  `KM_PER_AU` already being imported at line 42.
- `comet_visualization_shells.py` line 602: `SUN_RADIUS_AU = 695700.0 /
  149597870.7` -- a derived value computed from the two hardcoded copies.

These are the instances that motivated the new **No Shadow Constants
[CRITICAL]** convention (provenance-discipline v1.3, added this session
July 31 2026 -- see section 4 below). 1f fixes them mechanically; this
piece makes the scanner catch the PATTERN going forward.

**Design question for Opus 5:** What is the detection mechanism? The
retired `build_pinned_values()` used to maintain a lookup table of
known constant values for matching. The scanner needs a way to
distinguish "this literal matches a known constant AND is properly
imported" from "this literal matches a known constant but is a bare
hand-typed copy." The AST can show whether a module imports the
constant's name; a value match without a name import is the flag.

**Piece 2: citation-form recognition gap (L-156 Gap item 7).**

`has_citation()` / `SOURCE_PATTERNS` only recognizes three citation
forms: `# Source:` keyword, `# Verified:` keyword, or a URL. A bare
author-year parenthetical such as `# empirical limit (Vecellio et al.
2022)` matches nothing.

Confirmed live instances (from the L-156 ledger note, 1a session):
`TW_SURVIVABILITY_BIOLOGICAL` and `TW_SURVIVABILITY_THEORETICAL` are
genuinely, correctly cited with real references (Vecellio et al. 2022;
Sherwood & Huber 2010) and still score V4 RECALLED. The scanner accusing
a cited value of being uncited is cite-to-clear's mirror image.

**Measurement requirement:** the ledger estimates ~54 of the old 156
Tier-1 findings would be affected, but explicitly notes this could not be
independently reproduced (a quick approximation got 19 with a looser
pattern, different per-file split). The estimate predates 1b, 1c, and
L-174. **Re-measure against the current 132 before building.** This may
be Phase 1's single largest remaining Tier-1 reducer.

**Design scope:** add a new pattern to `SOURCE_PATTERNS` that recognizes
`(Author et al. YYYY)` and `(Author & Author YYYY)` forms within the
existing lookback window. The pattern must be tight enough to avoid false
positives on parenthetical content that is not a citation.

**Piece 3: L-078(d) -- bare-degree F/C values.**

`NUMERIC_CLAIM_RE` doesn't recognize bare Fahrenheit/Celsius temperature
values as numeric claims. Per L-078's own text, this folds into 1d's
regex work -- the same `NUMERIC_CLAIM_RE` pattern being edited for the
magnetosphere vocabulary (already landed in 1a) now gets `°F`, `°C`,
`degrees F`, `degrees C`, and similar suffixes.

Small, bounded, no design question -- extend the existing unit vocabulary.

### 3b. Sub-step 1e -- two pieces, console output and labeling

**Piece 1: Tier-1 banner.**

The scanner must print a prominent, bordered console banner when Tier-1
findings exist: something like `"132 Tier-1 findings -- push gate NOT
met"`. This is purely informational -- it does NOT gate the exit code.

**Decided (design review, section 3c, Tony confirmed):** Tier-1 NEVER
gets an auto-exit gate, at any threshold, ever. Not the deferred-flip
Fable proposed, not a baseline-ratchet. The banner is the brake (Tony
runs via VS Code's Run button and reads the console). The only hard
exit-code gate in the entire scanner is L-155's pinning checks (Phase 3,
not this build).

**Piece 2: Tier-2 label lie.**

The current Tier-2 tier label hardcodes "ALL ACCEPTED RESIDUALS -- no
action required" into the tier NAME, plus a static April 2026 note. Any
new finding landing in Tier 2 gets auto-narrated as already-reviewed by
the report template itself.

**Decided (design handoff D7, design review confirmed):** tiers get
neutral score-band names only (e.g. "Tier 2 (10-15): REVIEW").
Accepted-residual status is per-finding information, marked individually
using what's already in `data/provenance_exceptions.json` and the
Accepted Residuals report block. The blanket tier-level claim is deleted.

This MUST land with or after 1d's scoring changes (per the design
handoff: D3, D4, and the label fix are one build unit -- the V-ladder
recalibration repopulates Tier 2 with genuinely-open items; the blanket
label would mislabel every one of them).

### 3c. Sub-step 1f -- one piece, mechanical code fix

**Delete shadow constants in `comet_visualization_shells.py` and import
properly.** Scope (Tony's decision, this session):

- Delete line 492: `SUN_RADIUS_KM = 695700.0`
- Delete line 493: `KM_PER_AU = 149597870.7`
- Delete line 602: `SUN_RADIUS_AU = 695700.0 / 149597870.7`
- Import `SUN_RADIUS_KM` through the `planet_visualization_utilities`
  shim, alongside the existing `KM_PER_AU` import at line 42.
- Replace all downstream references to the deleted local variables with
  the imported names. `SUN_RADIUS_AU` is already a named constant in
  `constants_new.py` (one of the four `# Derived:` values verified in
  L-158) -- import it rather than recomputing locally.

**Broader scope (Tony's standing instruction, also decided this
session):** this is not limited to these three lines. The standing rule
is: NO local copies of constants that exist in `constants_new.py`,
anywhere in the repo. The two known instances above are confirmed; the
builder should grep for any others in the build-target file
(`comet_visualization_shells.py`) before treating the edit as complete.
A repo-wide sweep for other files carrying shadow constants is OUT OF
SCOPE for 1f but should be noted as a future item if any are found.

**Independence:** 1f has no dependency on 1d or 1e. It can land in any
order. The code fix is the same whether or not the scanner has been
updated to flag frozen copies.

---

## 4. New convention: No Shadow Constants [CRITICAL]

Added to `provenance-discipline` skill this session (v1.3, pending
Tony's push). Opus 5 should treat this as a decided, binding convention:

> Modules must not carry local copies of values that exist in
> `constants_new.py`. Import through the established shim
> (`planet_visualization_utilities`) or directly from `constants_new.py`.
> A local literal that numerically matches a tracked constant is a frozen
> copy -- it won't follow if the source value updates, and it bypasses
> the scanner's citation chain even when the number is correct today.
>
> When found, delete the local definition and replace it with a proper
> import -- do not add a `# Source:` comment to the local copy, because
> that would cite-to-clear a structural problem rather than fix it.

This convention is the WHY behind 1d piece 1 (the scanner enforcement)
and 1f (the code fix). The scanner change makes it detectable; the code
fix resolves the known instances; the convention prevents new ones.

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

---

## 7. Sequencing recommendation

No hard dependency forces an order among 1d, 1e, 1f -- they are
independent scoring, labeling, and code changes respectively, recomputed
fresh each scan. That said, a natural ordering exists:

1. **1f first** (smallest, no scanner change, fastest to verify). Fixes
   the known shadow constants. Quick win, clears the mechanical debt.

2. **1d next** (largest, shifts tier counts). The regex/recognition
   changes will move findings between tiers. Needs before/after
   measurement. Piece 2 (citation-form recognition) may be the single
   largest remaining Tier-1 reducer -- re-measure before building.

3. **1e last** (console output, depends on understanding the final tier
   distribution). The banner text references the Tier-1 count; the label
   fix references Tier-2 semantics. Both read better after 1d's tier
   shifts have settled.

**Or: all three in one session.** They are independent enough to land
together if Opus 5 prefers. The ordering above is a recommendation, not
a gate.

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

## 9. Reference documents

Read these before designing. The ledger entries (L-156, L-158, L-078)
are the authoritative scope; the design documents carry the reasoning.

| Document | What it carries |
|----------|-----------------|
| L-156 in LEDGER_CONSOLIDATED.md | Full gap list, all notes from 1a/1b/1c, decided constraints |
| L-158 in LEDGER_CONSOLIDATED.md | Derived-constant inheritance rule, shadow-constant instances |
| L-078 in LEDGER_CONSOLIDATED.md | Sub-item (d): F/C bare-degree fix |
| L-173 in LEDGER_CONSOLIDATED.md | The 18 genuinely uncited findings (NOT in scope) |
| L-174 in LEDGER_CONSOLIDATED.md | Citation-level-mismatch diagnostic (context for block inheritance) |
| DESIGN_HANDOFF_provenance_scoring_and_pinning.md | D1-D10, original design (partially superseded) |
| DESIGN_REVIEW_provenance_scoring_and_pinning.md | Amendments: D2 replaced, D5 expanded, D7 corrected |
| AS_BUILT_L156_phase1c.md | What 1c delivered, the mechanisms, the design departure |
| provenance-discipline SKILL.md | v1.3 (pending push): includes No Shadow Constants [CRITICAL] |
| safe-file-editing SKILL.md | v1.1: editing discipline, patch conventions |
| project_instructions (resident protocol) | v3.32: SHA round trip, agentic pre-test, all CRITICAL gates |

---

## 10. Tony-action items from this predesign

- **(do)** Push provenance-discipline v1.3 (No Shadow Constants section +
  version block update, both drafted this session). Record pushed SHA.
- **(decide)** Review this predesign and confirm scope before handing to
  Opus 5.
- **(decide)** Whether 1d/1e/1f run as one Opus 5 session or are split.
  Recommendation: one session, ordering per section 7.

---

*Predesign handoff written July 31, 2026 with Anthropic's Claude Opus 4.6.
Zero code written or proposed. Repo read-only throughout.*
