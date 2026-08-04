# Opus 5 Build Prompt: Geometry Corrections + `<br>` Fix

**Built on `55b07a6cf5ebfe2dce604d4e9fbff3c010e1b0eb`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).**

**Prepared:** August 4, 2026 by Claude Opus 4.6 (orchestration) · Tony Quintanilla, integrator
**Implements:** L-156 Batch 1 geometry follow-up + Mars retroactive fix
**Input:** `FABLE_shell_consistency_audit_report.md` (anchored at `679c2f4`)

---

## Who you are working for

Tony Quintanilla, PE — a retired civil and environmental engineer, artist,
and anthropologist. He builds Paloma's Orrery through conversational AI
collaboration ("vibe coding") and holds sole commit authority and final
judgment. The codebase's structure and discipline are the product of
iterative collaboration with Claude, not something Tony wrote unassisted.
Read code quality as evidence of the partnership, not of Tony's
independent programming skill.

Tony runs Python scripts by opening the file in VS Code and clicking the
Run button. He works with git exclusively through GitHub Desktop (commit
and push). Frame any instructions in those terms.

## Context

Batch 1 of L-156 (the provenance cross-check) corrected display text
and citations across five shell modules + `shell_configs.py` via
transactional patch scripts. A comprehensive Fable audit then discovered
that **the `radius_fraction` geometry constants were not updated to match
the corrected text values.** The shells render at the old sizes while the
hover text claims the new ones.

The same class of drift exists in Mars's dead code copies (Hill sphere
radius_fraction 320 vs the live 324.5, bow shock header 1.5 R_M vs the
live 1.64 R_M).

A separate finding: 95 of 126 module `_info` strings use `<br>` tags
instead of `\n`. Since the Tk GUI tooltip renders these literally, users
see markup text. This inverts the canonical format — the source text
should use `\n`, and `<br>` should be derived at the Plotly hover
boundary.

## Your two jobs

### Job 1: Geometry correction patches

Build transactional patch scripts (same pattern as Batch 1) to update
`radius_fraction` values in `shell_configs.py` to match the
cross-checked display text values.

**The governing principle:** the values that went through the three-model
competitive provenance cross-check are authoritative. The geometry must
match those values, not the other way around. Where a `radius_fraction`
encodes a different km value than the cross-checked text claims, the
`radius_fraction` moves.

**Body radii for rf computation** (from `constants_new.py` at HEAD):

| Body | Radius (km) | Source constant |
|------|------------|----------------|
| Mercury | 2,439.7 | MERCURY_RADIUS_KM |
| Moon | 1,737.4 | CENTER_BODY_RADII |
| Venus | 6,051.8 | CENTER_BODY_RADII |
| Eris | 1,163 | CENTER_BODY_RADII |
| Mars | 3,396.2 | CENTER_BODY_RADII |

#### Mercury geometry corrections

All edits in `shell_configs.py` unless noted.

| Shell | Current rf | Encodes (km) | Cross-checked value | Needed rf | Source |
|-------|-----------|-------------|-------------------|----------|--------|
| outer_core | 0.85 | 2,074 | 2,020 km (Hauck 2013) | 2020/2439.7 | Batch 1 worksheet |
| mantle | 0.98 | — | 331 km thick (above outer core) | (2020+331)/2439.7 | Batch 1 worksheet |
| crust | 1.0 | — | 26 km thick (Sori 2018) | see note | Batch 1 worksheet |

**Layer chain note.** 2,020 + 331 + 26 = 2,377 km vs R = 2,439.7 km.
The layers don't tile the body — a 63 km gap represents unmodeled
structure. The crust should remain at rf 1.0 (it's the surface layer).
This means the visual crust thickness will be (1.0 − mantle_rf) × R,
which is larger than 26 km. **Flag this in a comment but do not attempt
to resolve it** — that is a Mode 5 visual decision for Tony.

#### Moon geometry corrections

| Shell | Current rf | Encodes (km) | Cross-checked value | Needed rf | Source |
|-------|-----------|-------------|-------------------|----------|--------|
| inner_core | 0.1485 | 258 | 240 km (Weber 2011) | 240/1737.4 | Batch 1 worksheet |
| outer_core | 0.2083 | 362 | 330 km (Nakamura) | 330/1737.4 | Batch 1 worksheet |

#### Venus geometry corrections

| Shell | Current rf | Encodes (km) | Cross-checked value | Needed rf | Source |
|-------|-----------|-------------|-------------------|----------|--------|
| core | 0.5 | 3,026 | ~3,200 km (NASA Fact Sheet) | 3200/6051.8 | Batch 1 worksheet |
| crust | 1.0 | — | 10–30 km thick | see note | Batch 1 worksheet |

**Venus crust note.** Same issue as Mercury: a 10–30 km crust at rf 1.0
with the layer below it at rf 0.98 gives a visual thickness of 121 km.
Updating Venus mantle rf to close the 10–30 km gap would make the crust
shell essentially invisible. **Keep crust at rf 1.0, flag the stylization
gap in a comment.** Tony will decide via Mode 5.

#### Eris geometry corrections

| Shell | Current rf | Encodes (km) | Cross-checked value | Needed rf | Source |
|-------|-----------|-------------|-------------------|----------|--------|
| mantle | 0.66 (outer edge) | 70 km thick | ~100 km thick | compute | Batch 1 worksheet |

Note: the inner edge is at 0.60 (core). If mantle text says ~100 km
thick, the outer edge should be at (0.60 × 1163 + 100) / 1163.
Verify the text claim before computing.

#### Mars retroactive corrections

These are dead-code copies that carry pre-cross-check values. The live
config copies are already correct.

| Item | Location | Current | Correct | Notes |
|------|----------|---------|---------|-------|
| Hill sphere text | mars_visualization_shells.py (~line 844, 859) | "~320 Mars radii" | "~324.5 Mars radii" | Dead _info text; live config already says 324.5 |
| Hill sphere rf | mars_visualization_shells.py (~line 884) | `radius_fraction = 320` | `radius_fraction = 324.5` | Dead legacy builder dict |
| Bow shock header | shell_configs.py (~line 2188) | "bow shock 1.5 Rm" | "bow shock ~1.64 Rm (Vignes et al. 2000)" | Body-level header citation |
| Bow shock tooltip (dead) | shell_configs.py (CUSTOM_SHELLS Mars) | "~1.5 Mars radii" | "~1.64 Mars radii" | Dead custom tooltip |

#### Stale header corrections (Mercury + Moon body-level `# Source:`)

These are the Batch 1 as-built residual (b), confirmed by Fable:

| Body | Location | Issue | Fix |
|------|----------|-------|-----|
| Mercury | shell_configs.py lines 93–94 | Cites "Margot et al. (2012)" for core radius | Replace with "Hauck et al. (2013)" to match Batch 1 |
| Mercury | shell_configs.py line 94 | "Verified: April 2026 via Gemini" stamp | Replace with proper Cross-checked format referencing the Batch 1 worksheets |
| Moon | shell_configs.py lines 236–239 | Cites "Apollo Seismic Experiment reports" | Replace with "Weber et al. (2011)" to match Batch 1 |

#### What NOT to patch (flag only)

These are findings Fable surfaced that are **outside the cross-checked
scope**. Do not fix them — list them in the as-built for ledger tracking.

- Mercury mantle diamond claim (mercury:55, shell_configs:144/149) —
  pending Tony's decision from the Batch 1 as-built
- Mercury layer chain 63 km gap — structural, for future Mode 5
- Moon crust thickness three-way text disagreement (config 50/60,
  module 30–50/100+) — not cross-checked in Batch 1; Batch 2 candidate
- Moon `# dark red-orange at 1700K` colour comment (moon:56) — cosmetic
- Venus crust stylization (121 km rendered vs 10–30 km physical) — Mode 5
- Eris layer structure inversion suspicion (Fable finding #10) — Batch 2
- Earth shadow constants (EARTH_RADIUS_KM twice, mixing mean/equatorial) — separate L-item
- Solar gravitational influence 150k vs 126k AU — separate L-item
- Saturn Hill sphere three-way inconsistency — Batch 2
- Solar chromosphere three extents — separate L-item
- All 44 remaining "Verified: April 2026" stamps — Batch 2 sweep
- Jupiter/Saturn "not yet rendered" false claims in dead tooltips — Batch 2
- 124 dead `tooltip` fields across SHELL_CONFIGS/CUSTOM_SHELLS — migration design

### Job 2: `<br>` → `\n` conversion in module `_info` strings

Fable found that 95 of 126 module `_info` strings use `<br>` tags and
no `\n`. The Tk GUI tooltip (`CreateToolTip`) renders these literally —
users see `<br>` as text. The fix: replace `<br>` with `\n` in the
module `_info` strings.

**In-scope bodies (Mars + Batch 1 that need the fix):**

| Module | `_info` strings | Currently | Fix |
|--------|----------------|-----------|-----|
| moon_visualization_shells.py | ~6 | `<br>` | → `\n` |
| eris_visualization_shells.py | ~5 | `<br>` | → `\n` |
| pluto_visualization_shells.py | ~6 | `<br>` | → `\n` |
| mars_visualization_shells.py | ~7+ | `<br>` | → `\n` |

**Already clean (no action):** mercury_visualization_shells.py,
venus_visualization_shells.py — these already use `\n`.

**Out of scope (Batch 2+):** jupiter, saturn, uranus, neptune, planet9,
solar — same fix needed but not in this patch set.

**What to convert:**
- `<br>` → `\n` in all `_info` string definitions (the module-level
  strings consumed by `build_shell_checkboxes()` via `globals()`)
- `<br><br>` → `\n\n` (double line break)

**What NOT to convert:**
- Inline hover text inside custom geometry builder functions — these go
  to Plotly, where `<br>` is correct
- `shell_configs.py` `hover_text` fields — these go to Plotly, `<br>`
  is correct
- `shell_configs.py` `tooltip` fields — these are dead data; leave as-is

**For the four migrated bodies (Saturn, Uranus, Neptune, Sun) — out of
scope but important context:** their `shell_configs.py` entries import
the module `_info` and call `.replace('\n', '<br>')`. Currently that
`.replace()` is a no-op because the strings already have `<br>`. When
those bodies get the `<br>` → `\n` fix in Batch 2, the `.replace()` will
start working correctly. This is the intended future state — canonical
text in `\n`, derived `<br>` at the Plotly boundary.

## Build conventions

- **Transactional patch scripts** — same pattern as Batch 1. Each script
  is standalone, reads the target file in binary mode, verifies each
  anchor occurs exactly once, applies all edits bottom-up, writes only
  if all anchors match.
- **ASCII only, LF line endings** in all output
- **Bottom-up edit ordering** within each file
- **py_compile + xvfb run on a THROWAWAY copy** (agentic pre-test) —
  the deliverable is never edited by the pre-test
- **Anchors extracted programmatically** from the pristine file, not
  hand-transcribed
- Each script prints one `ok` line per edit, then a summary. Failure
  prints `ANCHOR FAIL:` and writes nothing.

## Run order

Any order — each script is independent. Tony saves each into the folder
containing its target file, opens it in VS Code, and clicks Run.

## Verification checklist (for the as-built)

- [ ] Every corrected rf value independently derived from
      `constants_new.py` body radius and the cross-checked km value
- [ ] Layer chain gaps flagged in comments, not silently adjusted
- [ ] `<br>` → `\n` applied only to `_info` strings, not to Plotly hover
      text or shell_configs.py hover_text
- [ ] Mars dead-copy values match live config values after patching
- [ ] Stale Mercury/Moon headers updated with Batch 1 cross-check sources
- [ ] py_compile clean on all targets after patching
- [ ] xvfb GUI run reaches `[DASHBOARD] Dashboard ready.`
- [ ] Live-dispatch smoke test: sample shells show corrected rf values
- [ ] Residual scan for every corrected rf value — zero old-value
      survivors in either copy (module + config)
- [ ] Neptune Hill sphere verified unchanged (collision guard, as in
      Batch 1)
- [ ] No "Fable not-to-patch" items accidentally included
- [ ] As-built lists all flagged items for ledger tracking

## Deliverables

1. Transactional patch scripts (one per target file)
2. As-built document anchored to the build SHA

---

*Prompt prepared August 4, 2026 by Claude Opus 4.6 (orchestration).*
