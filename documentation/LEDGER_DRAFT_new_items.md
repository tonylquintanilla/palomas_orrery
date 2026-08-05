# Ledger Entries — Draft for Review

**Session:** August 4, 2026 | Claude Opus 4.6 (orchestration)
**After push, fill in the SHA.**

---

## L-156 Update (Phase 2 status)

Add to the L-156 detail block, after the Phase 1 build history:

```
### Phase 2: Cross-check sweep (OPEN)

**Batch 1 (COMPLETE, 5 bodies + Mars retroactive).** Three-model
competitive cross-check of moon, eris, mercury, venus, pluto
visualization shells. 34 scanner findings, 56 claims verified. 13 value
fixes, 17 citation corrections (including 3 fabricated/wrong-paper
citations). Conventions established for Hill sphere (perihelion distance,
system mass for binaries), visualization constants (best-sourced single
value for code, range in description), and retired "Verified: April 2026"
annotation format. Mars cross-checked as precedent.

**Batch 1 geometry follow-up (COMPLETE).** Fable audit
(`FABLE_shell_consistency_audit_report.md`, `679c2f4`) discovered
radius_fraction geometry constants were not updated to match the
corrected display text values — shells rendered at old sizes while hover
text claimed new ones. Also found: `<br>` in _info strings rendering
as literal markup in GUI tooltips; 124 dead `tooltip` fields in
SHELL_CONFIGS/CUSTOM_SHELLS; up to six independent storage locations per
physical value. Opus 5 built 7 geometry+text patch scripts (47 edits).
`<br>` → `\n` converted for moon, eris, pluto, mars. Mercury mantle
diamond claim removed. Stale headers corrected. Provenance-neutral
(Tier 1: 207 → 207).

**Batch 2 (NEXT): Gas giants** — jupiter (18 findings), saturn (10),
uranus (24), neptune (26). Plus Saturn Hill sphere three-way
inconsistency, Jupiter/Saturn "not yet rendered" false claims, `<br>`
conversion for jupiter/saturn/uranus/neptune/planet9/solar. See
handoff_batch1_complete.md for template improvements.

**Ref:** ASBUILT_batch1_cross_check_patches.md,
ASBUILT_geometry_and_br_fix.md, FABLE_shell_consistency_audit_report.md,
PROMPT_fable_shell_consistency_audit.md,
PROMPT_opus5_geometry_and_br_fix.md
```

---

## New L-items (L-176 through L-181)

### L-176

```
#### [L-176] Shell hover text: add illustrated dimensions (radius_fraction → km)
<!-- L:176 status:OPEN upd:2026-08-04 section:A flag: rice:4/3/70/3 -->
- Fable audit surfaced that radius_fraction geometry constants are
  invisible to the user and verifiable only by manual computation. Add to
  each shell's hover text: "<shell name> illustrated between _ and _
  radii, a thickness of _ km". Gives the user full information and makes
  any stylization (e.g. Mercury crust drawn at 89 km vs physical 26 km)
  explicitly visible rather than silently present.
- Should derive from the radius_fraction at render time, not from a
  second typed literal — single source of truth.
- Natural companion to the single-source-of-truth constant layer
  (L-181): once constants are defined, the illustrated-dimension text
  can reference them.
**Gap:** Design the text format, decide whether to include the physical
value alongside the illustrated value for stylized shells. Build after
L-181 constant layer or in parallel.
**Ref:** FABLE_shell_consistency_audit_report.md findings #2-#12,
L-156 Phase 2.
```

### L-177

```
#### [L-177] Mercury Hill sphere radius_fraction convention error (Opus 5 self-flag)
<!-- L:177 status:OPEN upd:2026-08-04 section:A flag: rice:4/4/50/2 -->
- Opus 5 flagged its own Batch 1 work: Mercury Hill sphere
  radius_fraction is 94.4 R_M (230,308 km), but the citation says
  "perihelion convention." Perihelion gives 71.85 R_M; semi-major gives
  90.45 R_M. 94.4 matches neither — wrong-but-cited, the exact failure
  class the provenance discipline is designed to prevent.
- Fable couldn't catch it because Mercury's Hill text is qualitative
  (no number for the constant to contradict).
- Fix depends on which convention Tony picks. One-line change once
  decided.
**Gap:** Tony decision: perihelion (71.85) or semi-major (90.45)?
Perihelion is the project convention for Eris and Pluto.
**Ref:** ASBUILT_geometry_and_br_fix.md, Batch 1 worksheets.
```

### L-178

```
#### [L-178] Earth shadow constants — EARTH_RADIUS_KM duplicate + mean vs equatorial mixing
<!-- L:178 status:OPEN upd:2026-08-04 section:A flag: rice:3/3/40/2 -->
- Fable findings #33-36. `earth_visualization_shells.py` defines
  `EARTH_RADIUS_KM = 6371.0` twice (lines 907, 1019). This is the mean
  radius; constants_new.py has equatorial 6378.137 and polar 6356.752
  but no mean radius. The derivation of AU_PER_KM mixes the
  equatorial-based EARTH_RADIUS_AU with the mean 6371 denominator —
  a built-in ~0.11% error.
- Also: GEO scatter comment claims "±0.0002 AU (~30 km at GEO)" but the
  code computes ±0.0002 × EARTH_RADIUS_AU ≈ ±1.3 km. And GEO hover
  text is missing the AU equivalent (standing convention gap).
- No Shadow Constants gate (provenance-discipline v1.3) applies to the
  local EARTH_RADIUS_KM.
**Gap:** Add mean radius to constants_new.py or switch to equatorial.
Fix the GEO scatter comment. Add AU to GEO hover.
**Ref:** FABLE_shell_consistency_audit_report.md findings #33-37.
```

### L-179

```
#### [L-179] Solar gravitational influence — 150,000 vs 126,000 AU mismatch
<!-- L:179 status:OPEN upd:2026-08-04 section:A flag: rice:4/3/40/3 -->
- Fable findings #29-30. constants_new.py defines
  GRAVITATIONAL_INFLUENCE_AU = 150,000 (with an honest note: 100k-200k
  range). solar_visualization_shells.py citations at lines 50 and 174
  both claim the constant is 126,000. Display text says 126,000 AU.
  Shell renders at 150,000 AU. Classic dual-pipeline drift — someone
  moved one copy.
- Three-model cross-check needed to decide the correct value.
**Gap:** Resolve which value is authoritative. Update the loser.
**Ref:** FABLE_shell_consistency_audit_report.md findings #29-30.
```

### L-180

```
#### [L-180] Solar chromosphere — three inconsistent extents in one shell
<!-- L:180 status:OPEN upd:2026-08-04 section:A flag: rice:3/3/30/2 -->
- Fable finding #31. Chromosphere shell text says "Radius: from
  Photosphere to 1.5 Solar radii" and also "about 2,000 kilometers"
  (≈1.003 R_sun). Shell renders at constants_new.py CHROMOSPHERE_RADII
  = 1.1 R_sun (≈0.00512 AU). Three different extents: 2,000 km
  (physical), 1.1 (drawn), 1.5 (claimed).
- The drawn value is a declared stylization (there's a code comment).
  The text should say "drawn at 1.1" and note the physical extent.
**Gap:** Reconcile text, add Show-the-Envelope comment.
**Ref:** FABLE_shell_consistency_audit_report.md finding #31.
```

### L-181

```
#### [L-181] Single-source-of-truth constant layer for shell visualization
<!-- L:181 status:OPEN upd:2026-08-04 section:A flag: rice:5/4/80/3 -->
- Fable audit established the structural problem: up to six independent
  storage locations for one physical value (radius_fraction, hover_text,
  dead tooltip, module _info, CUSTOM_SHELLS tooltip, legacy inline
  builder dict). The reference pattern (Saturn/Uranus/Neptune/Sun) links
  text copies but not geometry to text — Saturn (fully migrated) carried
  the worst finding in the audit.
- Design required: define each value once as a named constant, derive
  radius_fraction and display text from it. The `<br>` canonical
  direction also belongs here: source text in `\n`, derive `<br>` at
  the Plotly boundary.
- 124 dead `tooltip` fields (83 sphere + 41 custom) are a
  delete-or-wire decision before migration.
- Natural companion to L-176 (illustrated dimensions).
**Gap:** Design the constant layer. Decide on dead tooltip fields.
Sequence migration per body.
**Ref:** FABLE_shell_consistency_audit_report.md §2 (Job 2),
migration status summary table.
```
