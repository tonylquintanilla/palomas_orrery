# Ledger note -- L-156 Phase 1d / 1e / 1f (paste-ready)

Built on `e29841f88fcc4b0f4d02681df1e0ec06b13a08c6`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

Two blocks. Block 1 appends to **L-156**. Block 2 is a NEW item,
**L-175**, holding the newly-visible temperature claims -- paste it only
if you take option 1+2 from the as-built section 2; if you defer piece 3
instead, skip Block 2 and say so in Block 1.

Run `ledger_index.py` afterward. Neither block sets `status:DONE`.

---

## Block 1 -- append inside L-156

```
Note (2026-07-31, 1d/1e/1f BUILT): Built on e29841f8; prompt anchor matched live
HEAD, no drift. Two deliverables, uncommitted: patch_phase1_d_e_f.py (16 anchored
edits across provenance_scanner.py and comet_visualization_shells.py,
all-or-nothing across BOTH files, MD5 guard per file, idempotent refusal naming
the cause per file) and test_provenance_1d.py (15 tests, roughly half negative).
MEASURED, clean clone: Tier 1 132 -> 171, Tier 2 588 -> 645, Tier 3 61 -> 62,
Tier 4 2 unchanged, total 783 -> 880. Tier 1 went UP by 39, the only step in
Phase 1 that does; the cause is isolated and is piece 3, see below.

PER-PIECE ISOLATION (measured separately rather than attributing one diff to
three causes): piece 2 alone (citation forms) Tier 1 132 -> 119, population
conserved at 783 -- behaves exactly as designed and lands near the ~15 ceiling
measured during the review. Piece 3 alone (F/C units) Tier 1 132 -> 193, total
783 -> 879. Piece 3 is the largest tier-moving change in Phase 1, larger than
1b. The R1 predesign calls it "small, bounded, no design question"; measured, it
is none of those. The regex is not over-matching -- plain degrees/deg still
resolve as angles, bare "98.6 F" and "21 C" are deliberately unmatched, and only
explicit degC/degF/degrees C/deg C/degrees Celsius forms fire. These are real
uncited temperature claims in public-facing climate narrative that the scanner
has been blind to since it was written; 96 of them, concentrated in
paleoclimate_wet_bulb_full.py (16 -> 51 findings),
paleoclimate_human_origins_full.py (11 -> 32), paleoclimate_visualization_full.py
(7 -> 28) and paleoclimate_dual_scale.py (2 -> 9). L-078(d) asked for exactly
this. Tony-action (decide): ship as built, ship and track the new population
separately as L-175, or defer piece 3 to its own sub-step. Builder
recommendation: ship plus track -- deferring buys a smaller number by keeping
the scanner deliberately blind, the one option that makes the audit less true
than it is now. Note these modules carry human-cost content where the
earth-system-pipeline restraint discipline applies, which argues for sourcing
them, not for leaving them unseen.

DIVERGENCE from the R1 predesign on 1d piece 1, flagged not resolved. R1 asks
for it as an amendment to score_unit()'s Option A. Built instead as a dedicated
detector, for three measured reasons. (a) Option A cannot see the problem: it
inspects display strings only, while all three confirmed shadow constants are
function-local numeric assignments -- and extract_units_from_file walks
ast.iter_child_nodes, so it reads TOP-LEVEL assignments only. The scanner
produces no unit at all at lines 492/493/602, so there is no score to amend.
(b) Amending Option A would push findings the wrong way: it currently fires on
18 display strings, 9 of them in modules importing nothing from constants_new.py
or the shim, so requiring an import would demote those 9 to V_RECALLED and move
them toward Tier 1 -- on a build already carrying piece 3's increase, for
strings unrelated to shadow constants. (c) Value-only matching is unusable: 77
repo-wide candidates on value alone, almost all coincidental round numbers
(0.5, 2.2, 10.0), versus exactly 2 on NAME AND VALUE together -- the confirmed
instances and nothing else. The scanner's own docstring already warns about this
failure mode for Option A. So: scan_shadow_constants() walks every assignment at
any depth, matches name+value for 'direct' and pinned-literal expressions with a
magnitude floor for 'derived', reports as a diagnostic, and leaves Option A's
scoring untouched. D8.5's retirement question stays open and is not made worse.

FIRE-THEN-SILENCE, the test the revised sequencing existed for: built in two
stages so the detector could be proven against real code before 1f removed the
evidence. Stage 1 (1d only) reported 3 shadow constants -- SUN_RADIUS_KM 492
direct, KM_PER_AU 493 direct, SUN_RADIUS_AU 602 derived. Stage 2 (+1f) reported
none and the audit section is empty. Detector fires, fix lands, detector goes
quiet.

1e: Tier-1 banner is bordered, prints when Tier-1 findings exist, and the exit
code is UNTOUCHED. The code carries a comment naming design review 3c and
naming HANDOFF_phase1_1d_to_1f.md as the superseded source, so a future session
does not revive the deferred flip from that document. Tier labels 2/3/4 are now
neutral score bands (REVIEW / LOW PRIORITY / LOWEST PRIORITY); Tier 1 keeps
"FIX NOW" as an action directive rather than a status claim -- Tony-action
(decide) if you want all four neutral, one line.

1f: value-preserving, verified at runtime -- the imported SUN_RADIUS_KM,
KM_PER_AU and SOLAR_RADIUS_AU equal both constants_new.py's values and the
deleted literals. SUN_RADIUS_AU kept as a local alias of SOLAR_RADIUS_AU so
downstream uses at 608-609 need no edit; it tracks the import instead of
freezing a value. The local KM_PER_AU had been SHADOWING the module-level import
for that whole function, so this is a scoping fix as well as a provenance one.
Grep for further shadow constants in the file found none beyond the three.

ALSO FOUND, not fixed. (1) comet_visualization_shells.py already violates the
ASCII-only convention: three em-dashes, 9 bytes, at offsets ~13951 (inside a
user-facing display string) and ~24506 (a comment). Pre-existing. The patch's
ASCII gate was corrected to assert no NEW non-ASCII rather than failing on the
file, and it reports the pre-existing count. Fixing them changes a display
string -- Tony-action (decide). (2) build_pinned_values() has a citation-bleed
flaw: a flat window of 10 lines above and 5 below, so in a densely packed file a
constant with no citation of its own picks up a neighbour's. The new
build_cited_constant_names() avoids it by reading only the contiguous comment
run touching the assignment, in EITHER direction -- constants_new.py writes its
citations BELOW the assignment, the rest of the codebase above. build_pinned_
values() itself is unchanged, since altering it would shift the pinned set and
Option A's behaviour; worth an item if Option A is kept. (3) A negative test
caught a real bug mid-build: the first build_cited_constant_names() walked
upward only, and test_uncited_constant_is_not_a_shadow_source failed -- which is
how the below-the-assignment convention surfaced. The test was written to catch
a false positive and found a false negative instead.

Gap items (5), (7) and L-078(d): BUILT. 1e: BUILT. 1f: BUILT. All awaiting
Tony's run and push. Still open in L-156: D8.5 (retire or keep Option A).

Add to Ref: patch_phase1_d_e_f.py; test_provenance_1d.py;
documentation/AS_BUILT_L156_phase1_d_e_f.md;
documentation/PREDESIGN_HANDOFF_phase1_d_e_f_R1.md;
documentation/REVIEW_predesign_1d_1e_1f.md.
```

---

## Block 2 -- NEW item L-175 (paste only if shipping piece 3)

```
#### [L-175] Newly-visible temperature claims in the climate modules
<!-- L:175 status:OPEN upd:2026-07-31 section:W.Active flag: rice:3/4/85/3 -->

What. L-156 Phase 1d piece 3 (L-078(d)) taught NUMERIC_CLAIM_RE to recognise
Fahrenheit and Celsius. The scanner had been blind to temperature values since
it was written, so 96 real claims became visible at once, 61 of them Tier 1.
They are not new gaps -- they are gaps that were always there and could not be
counted. Tier 1 132 -> 193 measured with piece 3 in isolation.

Where. Concentrated in four modules (findings before -> after):
paleoclimate_wet_bulb_full.py 16 -> 51; paleoclimate_human_origins_full.py
11 -> 32; paleoclimate_visualization_full.py 7 -> 28; paleoclimate_dual_scale.py
2 -> 9. Remainder scattered across shell modules carrying deg C in hover text.

Why it is its own item, not part of L-156. Same reasoning that separated L-173
from L-174: mixing "the scanner learned to see" with "the scanner was scoring
wrong" makes the Phase 1 arc unreadable. L-156's Tier-1 trend should be legible
as 156 -> 132 across 1a-1c plus this step change, not as a single number that
went up for unexplained reasons.

What it needs. Real sourcing, like L-173 -- most likely a Gemini worksheet
covering the wet-bulb and paleoclimate temperature series. NOT a scoring change,
and specifically not a widened citation window: these values are uncited because
nobody cited them, not because the scanner cannot find the citation.

Restraint note. These modules carry human-cost content -- heat mortality
thresholds, survivability limits. The earth-system-pipeline skill's restraint
discipline applies to any text produced while sourcing them. The 31 degC and
35 degC survivability limits are the motivating instances for L-156 Gap item 7
as well, and are correctly cited at their definitions (Vecellio et al.;
Sherwood & Huber) -- piece 2 now recognises those. What remains uncited is the
surrounding narrative, not the thresholds themselves.

Tony-action (decide) before this item is real: whether to ship piece 3 at all
(as-built section 2 gives three options). If piece 3 is deferred instead, close
this item unopened and record the deferral in L-156.

Ref: L-156 (Phase 1d piece 3), L-078(d), L-173 (the same shape for
shell_configs.py), documentation/AS_BUILT_L156_phase1_d_e_f.md,
skills/earth-system-pipeline/SKILL.md.
```

---

## Rollup -- Tony-action

- **(decide)** Ship piece 3 as built, ship and track as L-175, or defer.
  This decides whether Block 2 gets pasted.
- **(decide)** Tier 1 label: keep "FIX NOW" or neutralise all four.
- **(decide)** The three em-dashes in `comet_visualization_shells.py`.
- **(do)** Paste Block 1 into L-156; Block 2 as a new item if shipping.
- **(do)** Run `ledger_index.py`.
- **(do)** Correct or supersede `HANDOFF_phase1_1d_to_1f.md` (still wrong
  on 1e at HEAD -- carried over from the review, not yet done).
- **(do)** Stamp the provenance-discipline v1.3 SHA placeholder.
- **(do)** Push; record `pushed at <SHA>` on the as-built.

---

*Ledger note written July 2026 with Anthropic's Claude Opus 5.*
