# Shell Consolidation -- Phase D3.1 Handoff (v2, post-review)

**Session:** May 22, 2026 (D3.1 inventory + Mode 7 review + integration)
**Inventory by:** Anthropic's Claude Opus 4.7
**Mode 7 review by:** Anthropic's Claude Opus 4.7 (separate session)
**Integration review by:** Anthropic's Claude Opus 4.6
**Integrator:** Tony Quintanilla
**Status:** D3.1 inventory and review complete. Sweep manifest ready to write.

**Next session entry point:** Write D3.1 sweep manifest -- Mode 1
targeted snippets, organized by file, in five batches (see Manifest
Shape below). All decisions locked. Upload this handoff, the protocol,
`D3_1_INVENTORY.md`, `D3_1_MODE7_REVIEW.md`, and the 15
`*_visualization_shells.py` files.

---

## Summary

D3.1 Phase 1 (inventory) catalogued 134 legend entries across 15
shell files. Mode 7 review validated the headline finding with
corrections to the framing arithmetic and one significant
reclassification.

**Corrected headline (per Mode 7):** 116 total FAIL entries, of which
~102 are Rule 2 violations (hovertext does not lead with legend label).
The prior framing conflated total FAIL with Rule 2 FAIL. The remaining
~14 FAILs are Rule 0 (missing legendgroup), Rule 1 (missing body
prefix), Rule 3 (no leader in group), and Rule 4 (multi-leader).
Many entries violate multiple rules.

The mechanical fix -- prepend legend label to info marker text at
the construction site -- is confirmed correct by Mode 7 sampling
(5 source sites checked, all fail the rubric, all fixed by prepend).
False positive rate against the rubric is near zero. "Prepend
regardless" is the right sweep rule.

---

## Artifacts Produced

| Artifact | Session | Role |
|----------|---------|------|
| `D3_1_INVENTORY.md` | Opus 4.7 (inventory) | Rubric, per-file detail, findings |
| `D3_1_MODE7_REVIEW.md` | Opus 4.7 (review) | Q1-Q6 answers, additional findings |
| `D3_1_MODE7_REVIEW_PROMPT.md` | Opus 4.6 (pre-review) | Six questions for Mode 7 |
| `inventory_per_legend_entry.csv` | Opus 4.7 | 134 rows aggregated |
| `inventory_per_trace.csv` | Opus 4.7 | 249 rows raw |
| `d3_1_inventory.py` | Opus 4.7 | Verification script; re-run post-sweep |

---

## All Decisions (locked)

### From inventory session

| Decision | Outcome |
|----------|---------|
| Solar shell naming | Use `"Sun: X"` prefix consistently (9 renames) |
| `create_neptune_magnetic_poles` orphan | Deprecate in docstring, keep in source |
| Asteroid belt / comet files | Category files; Rule 1 body-prefix suppressed |

### From Mode 7 review + integration

| Decision | Outcome |
|----------|---------|
| Absorb `\n` -> `<br>` normalization into D3.1 | **Yes.** Items 43, 44 absorbed. Wherever the sweep touches a hover string, normalize newlines in the same edit. |
| MAPS active/inactive legendgroup sharing | **Separate.** Active traces (`'MAPS: Dust Trail (Remains)'`, etc.) and inactive placeholders are different structural elements. Each gets its own explicit legendgroup matching its name. No consolidation. |
| Moon Hill Sphere rename | **Yes.** `'Hill Sphere'` -> `'Moon: Hill Sphere'` at line 555. |
| Prepend location | **Construction site**, not config dict. Keeps formatting where formatting lives. |
| `customdata`-based hovertemplate approach | **Deferred.** More elegant but adds variability. Uniform text-prepend for D3.1. |
| Post-sweep verification | Re-run `d3_1_inventory.py` (necessary but not sufficient) + Mode 5 visual sampling by Tony. Script's Rule 2 check is a weak proxy; visual check is the real verification. |
| File docstrings | **Update module docstrings** on every file touched by the sweep to reflect the changes. |

---

## Mode 7 Review Findings (integrated)

### Q1: Headline confirmed

Prepend legend label to info marker text is correct for all Rule 2
violations. No subcategories requiring different treatment. Absorb
`\n` -> `<br>` normalization into the same pass (decided: yes).

### Q2: False positive rate -- near zero against rubric

5 `<expr>` entries sampled. All contain the body name in prose but
none lead with the legend label. "Prepend regardless" is safe. No
manual triage needed.

### Q3: Crust/cloud legendgroup fix -- confirmed with refinement

15 builders. Three edits each:
1. Add `legendgroup=trace_name` to the `go.Mesh3d` surface trace
2. Redefine `trace_name` at its definition site WITHOUT the `(Info)`
   suffix (so it's usable for both surface and info marker)
3. Info marker's `legendgroup` and `name` inherit the un-suffixed
   `trace_name` automatically

### Q4: Neptune double leader -- confirmed

`showlegend=False` on the line-604 diamond. Stays in legendgroup,
hidden from legend.

### Q5: MAPS 7-leader -- RECLASSIFIED (Mode 7 disagreement)

**Not consolidation. Missing legendgroups on placeholder traces.**
The inventory aggregator lumped them under `legendgroup=<none>`,
but at runtime Plotly treats each absent-legendgroup trace as its
own implicit group. They are semantically distinct (nucleus gone,
coma inactive, dust tail inactive, ion tail inactive). Fix: add
explicit `legendgroup` matching each trace's name. Same pattern as
the crust/cloud fix (Q3), not the Neptune multi-leader fix (Q4).

Active-state traces (Remains) stay in their own separate groups
(Tony's decision: different structural elements).

### Q6: Missed items

| Finding | Action |
|---------|--------|
| Moon Hill Sphere: `'Hill Sphere'` missing `"Moon:"` prefix | Add to sweep (item 60) |
| Mars Hill Sphere pair (lines 894/910): one OK, one FAIL from same builder | Manual check during sweep |
| Orphan function inflates violation tally by 1 | Skip in sweep (deprecation comment only); teach script to skip orphans on re-run |
| Loop-generated traces: prepend must use per-iteration name variable (`belt['name']`, `ring_info['name']`, etc.) | Manifest must identify the variable for each loop |
| Post-sweep verification script needs stricter Rule 2 check | Script improvement or rely on Mode 5 visual sampling |

---

## Manifest Shape (five batches, sequential)

Each batch independently verifiable before proceeding to the next.
Bottom-up line ordering within each file. Python binary mode for
all edits. Update module docstrings on every file touched.

### Batch 1: Solar prefix renames (9 edits, 1 file)

`solar_visualization_shells.py`: rename all 9 non-conformant labels
to `"Sun: X"` format. Both `name=` and `legendgroup=` on each trace.

**Verify:** re-run inventory, confirm Rule 1 "label does not start
with 'Sun:'" count drops to 0.

### Batch 2: Multi-leader and legendgroup fixes (small count, 2 files)

- `neptune_visualization_shells.py` line 604: `showlegend=False` on
  the D2 diamond
- `comet_visualization_shells.py`: add explicit `legendgroup` to each
  placeholder trace in `add_comet_tails_to_figure` (matching its name)
- `comet_visualization_shells.py`: add `legendgroup` to nucleus and
  disintegration marker (lines 457, 550)

**Verify:** re-run inventory, confirm multi-leader violations drop to
1 (the orphan function, which is expected).

### Batch 3: Orphan deprecation + Moon Hill Sphere rename (2 edits, 2 files)

- `neptune_visualization_shells.py`: add deprecation docstring to
  `create_neptune_magnetic_poles`
- `moon_visualization_shells.py` line 555: `'Hill Sphere'` ->
  `'Moon: Hill Sphere'`

**Verify:** read the edits.

### Batch 4: Crust/cloud legendgroup fix (15 builders, ~10 files)

For each of the 15 crust/cloud shell builders:
1. Redefine `trace_name` without `(Info)` suffix
2. Add `legendgroup=trace_name` to the `go.Mesh3d` surface trace
3. Info marker inherits the un-suffixed values

**Verify:** re-run inventory, confirm "leader trace missing
legendgroup" drops to ~3 (comet entries with different treatment).

### Batch 5: Rule 2 prepend sweep (~100 edit sites, all 15 files)

For every info marker construction site:
1. Identify the `trace_name` (or per-iteration name variable for
   loops: `belt['name']`, `ring_info['name']`, `params['name']`, etc.)
2. Prepend `f"{trace_name}<br><br>"` to the `text=` argument
3. In the same edit, normalize any `\n` to `<br>` in the hover string

This is the largest batch. Construction-site prepend, not config-dict.

**Verify:** re-run inventory (necessary but not sufficient) + Mode 5
visual sampling of hover text by Tony across representative bodies.

---

## Updated Deferred Items Table (post-D3.1 review)

| Item | Stage | Description | Status |
|-----:|:-----:|-------------|--------|
| 4 | -- | sun_position wiring (static) | DONE (D2) |
| 10 | -- | Double sun direction indicator | DONE (D2) |
| 11 | -- | Earth/Jupiter magnetic_tilt_deg | DONE (D2) |
| 12 | -- | Neptune magnetic poles -> diamond marker | DONE (D2 Option C) |
| 24 | E+ | Gas giant bow shocks | Open -- beyond D3 |
| 25 | E+ | Mars magnetosphere info marker | Open (= item 42) |
| 42 | D3.4 | Mars induced magnetosphere hover/info marker | Open |
| 43 | D3.1 | Uranus magnetosphere hovertext truncation | **Absorbed by D3.1 Batch 5 `\n` -> `<br>`** |
| 44 | D3.1 | Neptune magnetosphere hovertext truncation | **Absorbed by D3.1 Batch 5 `\n` -> `<br>`** |
| 45 | D3.1 | Neptune radiation hovertext labelling | **Absorbed by D3.1 Rule 2 sweep** |
| 46 | D3.1 | Neptune FAC hovertext labelling | **Absorbed by D3.1 Rule 2 sweep** |
| 47a | D3.2 | Neptune arc markers superimposed | Open |
| 47b | D3.2 | Neptune Lassell + Arago superimposed | Open |
| 48 | D3.3 | Mercury sodium tail sun_position wiring | Open |
| 49 | D3.3 | Earth fly-to-Sun distance | Open |
| 50 | D3.3 | Sun direction indicator per-body legendgroup | Open |
| 51 | E+ | Animation: non-center body shells | Open -- beyond D3 |
| 53 | D3.2 | Neptune magnetic center marker convention | Open |
| 54 | D3.1 | Hovertext/legendgroup sweep | **Review DONE; sweep manifest next** |
| 55 | D3.1 | Solar shell naming: "Sun: X" convention | Locked, Batch 1 |
| 56 | D3.1 | Crust/cloud shell legendgroup fix (15 builders) | Locked, Batch 4 |
| 57 | D3.1 | Neptune magnetosphere double-leader | Locked, Batch 2 |
| 58 | D3.1 | MAPS placeholder legendgroups (reclassified from consolidation) | Locked, Batch 2 |
| 59 | D3.1 | Deprecate `create_neptune_magnetic_poles` orphan | Locked, Batch 3 |
| 60 | D3.1 | Moon Hill Sphere: add "Moon:" prefix | NEW, Batch 3 |

Items absorbed into D3.1: 43, 44, 45, 46 (4 items).
Items added by D3.1: 55-60 (6 items, all scoped to the sweep).

### D3.2 -- Neptune cluster (reduced)

Items 47a, 47b, 53 only. Items 44, 45, 46 absorbed by D3.1.

### D3.3 -- Quick targeted fixes

Items 48, 49, 50. Unchanged.

### D3.4 -- Remaining items

Item 42 (Mars info marker) + D1 carryovers. Item 43 absorbed by D3.1.

### Deferred beyond D3

Items 24, 51. Unchanged.

---

## Procedural Lessons (updated)

### From D3.1 inventory session

**[QUALITY] -- Static analysis catches what visual testing cannot.**
Round 3 testing surfaced items 45 and 46 as Neptune-specific bugs.
The inventory revealed they are instances of a codebase-wide pattern
affecting ~102 entries. The inventory sees the whole codebase at once.

**[QUALITY] -- When a checking tool produces a comforting low number,
ask whether it's checking what you actually want to check.** Initial
script run: 40 FAILs. After tightening Rule 2: 116. The script was
finally measuring the right thing.

**[PRACTICE] -- Orphan detection as a side effect.** The inventory
surfaced `create_neptune_magnetic_poles` as dead code only because
it reported 4 `showlegend=True` traces inside an uncalled function.

**[PRACTICE] -- Reviewable artifacts beat agent-produced narratives.**
The inventory's structure (rubric -> summary -> detail -> findings ->
ambiguous -> known issues) is designed to be read top-to-bottom by
a reviewer answering specific questions.

### From D3.1 Mode 7 review

**[QUALITY] -- The aggregator key can misdiagnose.** The MAPS 7-leader
case was grouped under `legendgroup=<none>` by the script aggregator,
producing a "multiple leaders in same group" diagnosis. But at runtime,
absent legendgroups make each trace its own implicit group -- so the
real diagnosis is "missing explicit legendgroups," not "too many leaders
in one group." The fix is structurally different (add groups, not pick
a leader). Lesson: when an automated tool flags a violation, verify the
diagnosis, not just the detection.

**[QUALITY] -- The script's Rule 2 check is a weak proxy for the
rubric.** `body.lower() in m_hover.lower()` tests whether the body
name appears anywhere; the rubric requires the legend label as a
leading header. After the sweep prepends labels, the weak check passes
trivially but doesn't verify correctness. Post-sweep verification
needs Mode 5 visual sampling, not just a script re-run.

**[PRACTICE] -- Mode 7 self-review works.** Same model, different
session, six specific questions. The review caught a framing arithmetic
error, reclassified the MAPS case, found the Moon Hill Sphere gap, and
identified the Mars Hill Sphere pair for manual inspection. The
structure -- specific questions with "confirm or counter-propose" --
produced genuine pushback, not validation.

---

## Credit

```
Module updated: May 2026 with Anthropic's Claude Opus 4.7 (D3.1 inventory
                         and Mode 7 review)
                         and Anthropic's Claude Opus 4.6 (review prompt,
                         integration review, and v2 handoff)
```

---

*Paloma's Orrery | palomasorrery.com*
*"When an automated tool flags a violation, verify the diagnosis, not*
*just the detection." -- D3.1 Mode 7 lesson, May 2026*
