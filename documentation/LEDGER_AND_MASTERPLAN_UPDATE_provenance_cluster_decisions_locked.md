# Ledger + Master Plan Update -- Provenance Cluster Decisions Locked

Tony Quintanilla, PE | Claude Sonnet 5 | July 29, 2026

**Built on:** orrery (palomas_orrery) @ `33cc7706d13e4671837dd8a7627c1e92b4d9d6ad`
at https://github.com/tonylquintanilla/palomas_orrery (branch main)

**Type:** DOCUMENTATION (zero code changes). This is the paste-in record of
the decisions made in chat this session plus one later finding (the
citation-window inheritance fix, folded into L-156/L-078 below), so the
decisions and the findings behind them live in the ledger and master plan,
not only in this conversation or in
`PRELIM_DESIGN_HANDOFF_provenance_cluster_completion_part2.md`.

**How to use this file:** Three sections below. Section 1 = paste into
existing `LEDGER_CONSOLIDATED.md` blocks (search for the anchor text given,
insert immediately after it). Section 2 = three new ledger items, paste
into `LEDGER_CONSOLIDATED.md` section `### W.Active` (or `### D.Structural`
for L-171) anywhere before the next `##` header, in any order. Section 3 =
paste into `MASTER_PLAN_INTERACTIVE_GALLERY.md` section 6. After all
pastes: run `ledger_index.py` to regenerate the index tables. Do not
hand-edit the `INDEX:START`/`INDEX:END` zone.

---

## Section 1 -- Notes and Gap rewrites on existing items

### [L-162] -- search for: `**Ref:** \`constants_new.py\`; \`DESIGN_REVIEW_provenance_scoring_and_pinning.md\``

Insert this **Note:** immediately before that `**Gap:**` line, and replace
the existing `**Gap:**`/`**Ref:**` lines with the versions below:

```
**Note (2026-07-29, decided by Tony):** Both scope gaps from
`HANDOFF_L162_scope_gaps.md` resolved. (1) Naming: plain form
(`MARS_RADIUS_KM`), not type-labeled -- matches the 12 existing live
aliases in `planet_visualization_utilities.py` and `CONCEPT_ALIASES`'s own
canonical-key convention. (2) Ownership: this item owns the
Sun/Earth/Jupiter literal-duplication fix in the same edit -- `L-156`'s Gap
line stands as written, needs no tightening. (3) Alias layer: re-point
`planet_visualization_utilities.py`'s 12 existing aliases
(`MARS_RADIUS_KM = CENTER_BODY_RADII['Mars']`, etc.) to import directly
from `constants_new.py` instead, explicitly superseding the unrecorded
"v3.20 Option B" comment (grepped: appears nowhere else in the repo or
ledger). Without this, 12 same-named cross-file pairs land invisible to
`find_cross_file_issues()`'s `CONCEPT_ALIASES` lookup -- L-162 would
silently recreate the duplication problem it exists to fix.
**Correction:** "15 remaining bodies" reads 14 everywhere in prior docs (18
dict keys - 3 done - Planet 9 excluded = 14); the named list was always
right, only the count label was off by one.

**Gap:** dedicated Sonnet-class session, Phase A (per
`PRELIM_DESIGN_HANDOFF_provenance_cluster_completion_part2.md` Phase A):
(1) 14 new plain-form named constants in `constants_new.py`, each keeping
its existing citation; (2) rewire `CENTER_BODY_RADII` to reference all 17
names (Sun/Earth/Jupiter included); (3) re-point
`planet_visualization_utilities.py`'s 12 aliases to import from
`constants_new.py`; (4) add `CONCEPT_ALIASES` entries for all 14 new names
-- hard requirement, not optional; (5) pre-flight grep for f-string
formatting of `CENTER_BODY_RADII[...]` (Sun/Jupiter values change int ->
float); (6) `py_compile` + ASCII/LF gate + credit line + as-built anchored
to push SHA. Must land before Phase 3 (pinning engine). Independent of
Phase 0 and Phase 1.
**Ref:** `constants_new.py`; `planet_visualization_utilities.py`;
`DESIGN_REVIEW_provenance_scoring_and_pinning.md` section 3a;
`HANDOFF_L162_scope_gaps.md`;
`PRELIM_DESIGN_HANDOFF_provenance_cluster_completion_part2.md` Phase A;
L-155; L-156; L-159 (Planet 9 case).
```

### [L-156] -- search for: `L-163 (naming precedent);`
### (this is the last line of L-156's existing `**Ref:**`)

Insert this **Note:** right after the existing Gap block (before `**Ref:**`):

```
**Note (2026-07-29, decided by Tony):** April 2026 constants verification
(Claude sourced, Gemini reviewed) accepted as sufficiently verified as-is
-- it caught two real errors (Arrokoth, Parker) and that's the working bar.
**Not** promoted to a formal `# Cross-checked:` V2 annotation now; that
annotation, if ever added, rides the regular Gemini sweep when it reaches
`constants_new.py` (same as any other file, via L-161's relay) -- not a
separate task, not a Phase 2 blocker. D6's pinning-engine staging premise
stands as originally written; Phase 2 is not gated on this question.
L-078(d)'s F/C bare-degree regex fix folds into this Phase 1 build (same
`NUMERIC_CLAIM_RE` edit as D8's magnetosphere vocabulary addition).
```

Then add a 5th Gap item (append to the existing numbered Gap list, after
item 4):

```
(5) widen `build_pinned_values()`/scoring so a bare numeric literal that
merely matches an already-cited pinned value is flagged
("possible frozen copy -- verify import") rather than silently granted
V_SOURCED. This is the actual fix that closes L-158's gap (see L-158's own
note) -- the inheritance-rule wording alone doesn't catch it. Two confirmed
live instances to fix alongside it: `comet_visualization_shells.py` lines
492-493 and 602 (see L-158).
(6) **Citation-window inheritance fix (verified 2026-07-29 -- independently
re-measured, exact match).** 66 of the 145 Tier-1 findings (46%) have a
real block-level `# Source:` citation the scanner's 60-line lookback simply
doesn't reach -- concentrated in `shell_configs.py` (41; one citation per
~170-line body block, gap 64-821 lines) and `jupiter_visualization_shells.py`
(1; a two-line miss). Root cause: `_extract_string_units` walks every
string constant independently with its own 60-line window, blind to any
enclosing dict's block citation -- and for `shell_configs.py` specifically,
`_make_dict_unit` never applies at all, since `SHELL_CONFIGS`/
`CUSTOM_SHELLS` are single top-level dicts whose values are nested dicts,
which `_make_dict_unit` explicitly skips. Fix: a string unit nested inside
a block-cited dict inherits that citation, but inheritance is not
clearance -- it lands at V3 SOURCED, same pattern as L-158's inheritance
rule. Must land before Phase 4's worksheets are drafted; it determines
which findings actually need Gemini. `idealized_orbits.py`'s 24 "beyond
window" findings do NOT get this treatment -- median gap 2418 lines,
genuinely distant citations, not the same phenomenon; they stay Tier-1 and
need the worksheet like any other genuinely uncited claim.
**Updated Tier prediction** (supersedes `PRELIM_DESIGN_HANDOFF_...part2.md`
section 3's table; total conserved at 764):

| | Live at HEAD | Predicted after Phase 1 |
|---|---:|---:|
| Tier 1 | 145 | **~103** |
| Tier 2 | 158 | **~532** |
| Tier 3 | 442 | ~110 |
| Tier 4 | 19 | ~19 |
```

### [L-158] -- search for: `**Gap:** build -- rides Phase 1 of L-156's scanner build; identify which`

Replace that entire **Gap:** paragraph (both its lines) with:

```
**Note (2026-07-29):** Verified live -- exactly four `# Derived:` comments
exist repo-wide, all in `constants_new.py` (lines ~100, 104, 126, 130):
`SOLAR_RADIUS_AU`, `LIGHT_MINUTES_PER_AU`, `CORE_AU`, `RADIATIVE_ZONE_AU`.
All four are genuine runtime formulas; zero frozen literals are annotated.
**The inversion:** this item's two-factor detector (comment + AST check)
can only catch a frozen copy that announces itself. The dangerous ones
don't -- `CENTER_BODY_RADII['Sun'] = 695700` is a frozen copy of
`SUN_RADIUS_KM` with no `# Derived:` comment anywhere near it, invisible to
the mechanism as specified. Same failure class as the
`close_approach_data.py` stale-copy bug that originally motivated
`test_constants_provenance.py`. Confirmed live in the wild:
`comet_visualization_shells.py` lines 492-493 (`SUN_RADIUS_KM = 695700.0`,
`KM_PER_AU = 149597870.7`, hardcoded, no `# Source:` nearby, despite
`KM_PER_AU` already being imported at line 42) and line 602
(`SUN_RADIUS_AU = 695700.0 / 149597870.7`). Neither shows as Tier-1 today
because `build_pinned_values()` treats any value match against an
already-cited `constants_new.py` constant as V_SOURCED, whether the match
is a real import or a bare hand-typed copy.
**Gap:** rides Phase 1 of L-156's scanner build (unchanged). Two concrete
pieces, not one: (1) widen `build_pinned_values()`/scoring per L-156's Gap
item 5 -- the actual fix; (2) separately, fix the two live instances
directly: delete the local shadow constants in
`comet_visualization_shells.py` lines 492-493 and 602, import
`SUN_RADIUS_KM` through the `planet_visualization_utilities` shim alongside
the existing `KM_PER_AU` import (line 42). Small, mechanical, no
dependency on (1) -- can land anytime.
```

### [L-154] -- search for: `**Gap:** wait on the cluster below; land the one-line resolver fix in the`

Insert this **Note:** immediately after that Gap paragraph (which ends
"...then build (Opus 5) + Mode 5 acceptance."):

```
**Note (2026-07-29, Tony's explicit sequencing call):** "the cluster
below" means the WHOLE thing, Phase 4 included -- not just Phases 1-3.
Once the scanner build ships, this item's own technical blocker (the
resolver bug, the pinning engine) is gone, and it would be defensible to
call L-154 "unblocked" at that point. Tony's call is stricter than
defensible: no interactive/Artifact-2 work resumes until both Gemini
worksheets (L-157, then L-161+L-078a) are also closed. Deliberate, not an
oversight -- avoid interleaving data-integrity work with visual-feature
work; finish one before starting the other. Do not read "Phase 3 shipped"
as a green light on its own.
```

### [L-078] -- search for: `**Gap:** step (1) done; report tooling (by-file, by-file-type) done. Remaining:`

Replace that entire **Gap:** paragraph with:

```
**Note (2026-07-29, verified live at HEAD):** Triage backlog is 145, not
104 (the July 16 figure) -- confirmed by a live scanner run against a
clean clone with the real exceptions file loaded. Every file besides
`shell_configs.py` matches the July 4/16 figures within +/-1; the entire
41-finding delta is `shell_configs.py` alone, newly in scanned scope from
L-163's role-widening.
**Correction (2026-07-29, same day, re-measured):** those 41 are NOT a real
citation gap -- see L-156 Gap item (6). `shell_configs.py` has a genuine
`# Source:` comment for every body block; the scanner's 60-line lookback
just doesn't reach it. Once L-156's inheritance fix lands, these 41 drop
out of Tier-1 (V3, not V1/V2 -- still worth a look, just not "uncited").
The genuinely uncited population -- the actual (a) triage target -- is the
paleoclimate family (32 across 5 files: `paleoclimate_wet_bulb_full.py`,
`paleoclimate_human_origins_full.py`, `paleoclimate_visualization_full.py`,
`paleoclimate_visualization.py`, `paleoclimate_dual_scale.py`) and the
sgr_a family (13 across 3: `sgr_a_grand_tour.py`,
`sgr_a_visualization_core.py`, `sgr_a_visualization_precession.py`), plus
`idealized_orbits.py`'s genuinely-distant remainder (24 -- real gap, not a
lookback artifact) and the rest of the July 4/16 baseline. All score
V4xC4=16 (uncited display strings), same object type as L-161's sweep, not
geometry -- so (a) still merges into L-161 rather than running separately;
only the starting file changes.
**(b) is DONE, closed as a side effect of L-163, and its old instruction is
now actively wrong.** The live audit has no role-coverage-gap section at
all (only the domain one) -- L-163 Phase 3's docstring tags classify
114/115 modules with `role_source == 'tag'`. "Add to ROLE_MAP or
narrative_files" does nothing since L-163 Phase 3: `ROLE_MAP` is a
regenerated mirror, overwritten by the next `module_atlas.py` run. One of
the four originally-named modules (`smoke_rotation_axis.py`) was also
deleted outright in L-163 Phase 1. The two files that DO still need a home
are domain-coverage-gap, not role -- see L-172.
**Gap:** (a) merge into L-161's Gemini relay, one worksheet per file,
covering that file's uncited (this item) and re-read (L-161) claims
together -- start with the paleoclimate family (32 findings, never
worksheeted) and the sgr_a family (13, never worksheeted), NOT
`shell_configs.py` (that's L-156's Phase 1 fix, not a worksheet target)
and not L-161's originally proposed `celestial_objects.py` either. (b)
DONE -- see Note above, no further action. (c)
near-miss vocabulary detector -- stays open, separate, own session after
this cluster, corpus tuning not started. (d) F/C bare-degree fix -- folds
into L-156's Phase 1 build.
```

---

## Section 2 -- Three new ledger items (paste as new blocks)

```
#### [L-170] Tier-1 exit-code flip -- capture so it doesn't float
<!-- L:170 status:OPEN upd:2026-07-29 section:W.Active flag: rice:2/2/90/0.5 -->
- **What.** D7 (`DESIGN_HANDOFF_provenance_scoring_and_pinning.md`) wired
  the Tier-1 nonzero exit code but switched it off, "recorded as its own
  small ledger item so the flip doesn't float." It floated -- no such item
  existed until this one. The console banner ships with Phase 1; the
  exit-code flip itself is a one-line change, thrown the first time a live
  run reaches Tier-1 = 0.
**Gap:** flip the exit code on when Tier-1 first reaches 0 in a real run.
Not gated on anything else in this cluster -- a "remember to do this later"
placeholder.
**Ref:** `DESIGN_HANDOFF_provenance_scoring_and_pinning.md` D7;
`PRELIM_DESIGN_HANDOFF_provenance_cluster_completion_part2.md` section 6
item 9; L-156 (Phase 1, banner).
```

```
#### [L-171] patch_ledger_index_retired_handles.py breaks L-163's zero-undetermined close
<!-- L:171 status:OPEN upd:2026-07-29 section:D.Structural flag: rice:1/1/90/0.5 -->
- **What.** Landed July 28 with no `Role:`/`Domain:` docstring tags.
  `classify_role('patch_ledger_index_retired_handles', ...)` returns
  `undetermined` -- confirmed by calling the live function directly.
  Breaks L-163 Phase 3b's "zero undetermined" close two days after it
  closed. Also a one-shot patch script, the exact class L-163 Phase 1
  archived.
**Gap:** add `Role:`/`Domain:` tags to its docstring, or archive it
alongside the seven already-archived one-shot scripts. Either closes this;
archiving is probably cleaner given the class match.
**Ref:** `patch_ledger_index_retired_handles.py`; `module_atlas.py`
(`classify_role`); L-163 (Phase 1, Phase 3b); `AS_BUILT_L163_phase1.md`.
```

```
#### [L-172] Phase 0 record-hygiene batch (provenance cluster prep)
<!-- L:172 status:OPEN upd:2026-07-29 section:W.Active flag: rice:3/2/95/1 -->
- **What.** Small, independent, unblocked corrections a later session
  would otherwise trust as-is. Bundled as one checklist since none
  individually needs its own future reference:
  1. `MODULE_DOMAIN_MAP` entries for `orrery_rendering.py` and
     `shell_configs.py` (both currently silent-defaulting to `orrery` in
     the domain-coverage-gap report).
  2. Fix the L-157/L-161 swap in
     `HANDOFF_gallery_feature_layer_L154_resume.md` section 3 -- it
     credits the shell-config ring/belt/atmosphere cross-check to
     "L-161"; that work is L-157's.
  3. Carry the 15 -> 14 correction into this ledger's own prose wherever
     "15 remaining bodies" still appears, and into master plan section 6
     (see Section 3 below).
  4. Reinstall `gallery-assembler` SKILL.md from the repo copy -- installed
     copy carries CRLF line endings (118 confirmed, 0 bare LF),
     byte-identical content otherwise; came from a Windows path that
     bypassed the LF gate.
  5. Correct `MASTER_PLAN_INTERACTIVE_GALLERY.md`'s path in any reused
     prompt template -- it lives at `documentation/MASTER_PLAN_...`, not
     repo root.
**Gap:** all five are mechanical, no design decision needed, no dependency
on Phases A/1/2/3. Land in the same session as L-164 (dep_trace.py ASCII
bytes) -- same shape of work.
**Ref:** `PRELIM_DESIGN_HANDOFF_provenance_cluster_completion_part2.md`
Tony-action rollup; L-163; L-164.
```

---

## Section 3 -- Master plan section 6 update

Search for the paragraph beginning `**L-154-162 -- Provenance scoring
model fix (the whole cluster).**` in `MASTER_PLAN_INTERACTIVE_GALLERY.md`
section 6. Append this paragraph immediately after it:

```
**Decisions locked 2026-07-29 (Tony).** All remaining open forks in the
cluster are resolved: L-162 naming (plain form) and scope (owns the
Sun/Earth/Jupiter fix too); the `planet_visualization_utilities.py` alias
layer (re-point to `constants_new.py`, superseding an unrecorded "v3.20
Option B"); Planet 9 excluded from pinning entirely; and the April 2026
constants verification accepted as sufficiently verified, with formal
annotation deferred to the regular Gemini sweep rather than treated as a
separate task or a Phase 2 blocker. A genuine gap was also found and
folded in: `L-158`'s frozen-literal detector is blind to copies that don't
self-announce (confirmed live in `comet_visualization_shells.py`), fixed
alongside the Phase 1 build. Three new prep items opened: `L-170`
(Tier-1 exit-code flip, previously undocumented despite D7 asking for it),
`L-171` (a `L-163` regression -- `patch_ledger_index_retired_handles.py`
landed untagged), `L-172` (a small record-hygiene batch). Nothing further
blocks a build session. **Correction:** "15 remaining bodies" reads 14
throughout this section (18 dict keys - 3 done - Planet 9 excluded = 14).

**Second correction, same day.** 66 of the cluster's 145 Tier-1 findings
turned out to be a scanner-mechanics artifact, not real citation gaps --
the scanner's 60-line lookback doesn't reach `shell_configs.py`'s
per-body-block citations (41 findings) or one two-line miss in
`jupiter_visualization_shells.py`. Fix folded into L-156's Phase 1 (string
units inherit their enclosing block's citation, landing at V3, not
automatic clearance). Post-Phase-1 Tier-1 is predicted at ~103, not 145 --
a reclassification, not new work. The Gemini worksheet L-078/L-161 sequence
now starts with the paleoclimate and sgr_a families instead of
`shell_configs.py`. Full detail: L-156 Gap item 6, L-078's note.
```

---

*Compiled July 2026 with Anthropic's Claude Sonnet 5, from decisions made
in chat plus independent verification against live HEAD.*
