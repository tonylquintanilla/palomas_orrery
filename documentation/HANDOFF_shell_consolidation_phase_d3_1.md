# Shell Consolidation -- Phase D3.1 Handoff (round trip)

**Session:** May 22, 2026 (D3.1 inventory)
**Executed by:** Anthropic's Claude Opus 4.7 (inventory script + analysis)
**Integrator:** Tony Quintanilla
**Status:** D3.1 inventory complete. Awaiting Mode 7 review by Opus 4.7.

**This is a round-trip handoff.** Carry the inventory to Opus 4.7 for
Mode 7 review. Bring the review back (with corrections, refinements,
or counter-proposals) and the next session writes the D3.1 sweep
manifest from the agreed-on findings.

**Next session entry point (post-review):** Write D3.1 sweep manifest --
Mode 1 targeted snippets, organized by file, integrating 4.7's feedback
and Tony's decisions documented below.

---

## What Was Produced This Session

Four artifacts. The first is the review document; the others are
working data and tooling.

| Artifact | Role | For |
|----------|------|-----|
| `D3_1_INVENTORY.md` | Review document (sections 1-6: rubric, conformance summary, per-file detail, findings, ambiguous, known issues) | Opus 4.7 Mode 7 review |
| `inventory_per_legend_entry.csv` | 134 rows, aggregated view | Working data |
| `inventory_per_trace.csv` | 249 rows, raw trace dump | Manifest authoring |
| `d3_1_inventory.py` | The script that produced the above | Re-run after sweep to verify FAIL count drops |

Inventory was produced by static AST analysis of all 15
`*_visualization_shells.py` files, with single-level variable resolution
and cross-reference against `shell_configs.py` for the `needs_sun_position`
flag. Hand-curated orphan-function list (one entry: see below).

---

## Headline Finding

**Rule 2 violations dominate.** 116 of 134 legend entries are flagged
for "hovertext does not lead with legend label." The pattern is
codebase-wide and structurally identical everywhere:

- Geometry trace correctly uses `hoverinfo='skip'` (no hover).
- Info marker correctly carries the hover via `text=[...]` + custom
  `hovertemplate`.
- BUT the info marker's text is typically `layer_info['description']`,
  `belt['description']`, `ring_info['description']`, etc. -- which
  starts with the *description content*, not the legend label.

The user hovers and sees a paragraph about (say) atmospheric composition
with no leading indicator of which shell it belongs to. This is exactly
items 45 and 46 from Round 3 testing (Neptune radiation belts and FAC),
generalized.

**Proposed mechanical fix:** prepend the legend label to every info
marker's hover text, e.g. `f"{trace_name}<br><br>{description}"` (or
`\n\n` depending on file convention). The trace name is already
available in scope wherever the info marker is constructed -- usually
as a local variable named `trace_name` or computed inline.

The remaining 38 non-Rule-2 violations break down into five smaller
buckets documented in the inventory; counts and per-file detail are in
the markdown.

---

## Tony's Decisions This Session

| Decision | Outcome |
|----------|---------|
| Solar shell naming convention (9 entries: "Outer Oort Cloud", "Sun's Gravitational Influence", etc.) | **Use "Sun: X" prefix consistently.** Sweep will convert all 9 solar shells to follow the convention. |
| `create_neptune_magnetic_poles` orphan function | **Deprecate, keep for reference.** Do NOT remove. Add a deprecation comment in the docstring noting that D2 Option C replaced this function with the inline diamond marker in `create_neptune_magnetosphere` (line 604), retained for historical reference. |
| Inventory granularity | Per-legend-entry for review; per-trace CSV kept for sweep authoring. |
| Files in scope | Full 15 `*_visualization_shells.py` files. |
| Inventory method | Hybrid: programmatic AST extraction + manual cross-checks. |
| Asteroid belt and comet files | Treated as category files. Rule 1 (Body: prefix) and Rule 2 (hover echoes body) suppressed; their labels use population names or comet-specific names instead. |

---

## What Opus 4.7 Should Review

The review document (`D3_1_INVENTORY.md`) has the full rubric and
per-file detail. Specific questions for Mode 7:

1. **Does the headline finding hold up?** Is "prepend legend label to
   info marker text" the right mechanical fix for the 116 Rule 2
   violations? Or are there subcategories within those 116 where a
   different fix is needed (e.g., short hover strings that already
   work fine, ring systems that need different treatment, anything
   that should be left alone)?

2. **Section 4 false positive rate.** Several FAIL entries are
   script-limitation false positives -- the script renders multi-line
   string concatenation as `<expr>` and the body-name check fails even
   though the rendered runtime string may start with the body name
   (e.g., Neptune magnetic center line 604 hover starts with "Neptune's
   magnetic field..."). Sample a handful of `<expr>` entries against
   the source to estimate the false positive rate. If it is high
   (say >25%), the sweep manifest should be more selective; if low,
   the "prepend regardless" rule is safer.

3. **Crust/cloud shell legendgroup fix.** 15 entries have geometry
   trace missing `legendgroup` and paired info marker with its own
   group plus `(Info)` suffix. Proposed fix: add `legendgroup=trace_name`
   on the geometry trace AND remove the `(Info)` suffix from the info
   marker's `legendgroup` (and probably also its `name`, since the
   info marker uses `showlegend=False` anyway). Confirm or counter-
   propose.

4. **Neptune magnetosphere double leader (D2 deployment artifact).**
   At line 567, `create_neptune_magnetosphere` ends up emitting two
   `showlegend=True` traces in the same legendgroup: the magnetosphere
   envelope and the new D2 diamond at line 604. The diamond should
   have `showlegend=False` (kept in the legendgroup, hidden from the
   legend itself). Confirm this is the correct read.

5. **MAPS comet tails 7-leader case.** `add_comet_tails_to_figure`
   at line 1760 has 7 traces all `showlegend=True` in one legendgroup.
   Big legend clutter. Likely needs one consolidated leader and six
   followers. Confirm and propose which trace should be the leader.

6. **Any missed pattern.** The script saw 249 trace constructors
   and aggregated to 134 legend entries. Loop-generated traces
   (radiation belts, ring systems) collapse to one row even though
   they emit N entries at runtime. Are there inventory rows where
   the loop hides a real bug that the manifest needs to know about?

---

## Updated D3 Staging

### D3.1 -- Hovertext/legendgroup sweep (item 54)

**Phase 1 (DONE this session):** Inventory across all 15 shell files.
Four artifacts produced. Three review questions surfaced. Tony's
decisions on solar convention and orphan function locked.

**Phase 2 (next session):** Write the sweep manifest from the
inventory + 4.7's review feedback. Mode 1 targeted snippets, organized
by file, with edits grouped by pattern (Rule 2 prepend; Rule 3
legendgroup add; solar convention rename; Neptune diamond showlegend
fix; MAPS tail leader pick).

**Phase 3:** Execute the sweep (Mode 1 by Tony or agentic Mode 2 by
Claude, depending on manifest character). Re-run `d3_1_inventory.py`
to verify FAIL count drops to near zero. Mode 5 visual verification
by Tony.

### D3.2 -- Neptune cluster

Items 44, 47a, 47b, 53. (Items 45 and 46 absorbed by D3.1's sweep --
they were specific instances of the codebase-wide Rule 2 pattern.)

**Open items remaining in D3.2:**
- Item 44: Neptune magnetosphere hovertext truncation (`\n` -> `<br>`)
- Item 47a: Adams/Le Verrier/Galle arc markers superimposed
- Item 47b: Lassell + Arago ring markers superimposed
- Item 53: Neptune magnetic center marker convention (`square-open` not `diamond`)

### D3.3 -- Quick targeted fixes

Items 48, 49, 50. Unchanged.
- Item 48: Mercury sodium tail sun_position wiring
- Item 49: Earth fly-to-Sun distance (~0.15 AU too small)
- Item 50: Sun direction indicator per-body legendgroup + label

### D3.4 -- Remaining items

Items 42, 43, D1 carryovers. Unchanged.
- Item 42: Mars induced magnetosphere info marker
- Item 43: Uranus magnetosphere hovertext truncation

### Deferred beyond D3

Item 24 (gas giant bow shocks) and item 51 (animation shell rendering
for non-center bodies). Unchanged.

---

## Updated Deferred Items Table (post-D3.1 inventory)

D2 closed items 4, 10, 11, 12. D3.1 inventory is **phase 1 of item 54**;
phase 2 (sweep) remains open pending review.

| Item | Stage | Description | Status |
|-----:|:-----:|-------------|--------|
| 4 | -- | sun_position wiring (static) | DONE (D2) |
| 10 | -- | Double sun direction indicator | DONE (D2) |
| 11 | -- | Earth/Jupiter magnetic_tilt_deg | DONE (D2) |
| 12 | -- | Neptune magnetic poles -> diamond marker | DONE (D2 Option C) |
| 24 | E+ | Gas giant bow shocks | Open -- beyond D3 |
| 25 | E+ | Mars magnetosphere info marker | Open (= item 42) |
| 42 | D3.4 | Mars induced magnetosphere hover/info marker | Open |
| 43 | D3.4 | Uranus magnetosphere hovertext truncation | Open |
| 44 | D3.2 | Neptune magnetosphere hovertext truncation | Open |
| 45 | D3.1 | Neptune radiation hovertext labelling | **Absorbed by D3.1 Rule 2 sweep** |
| 46 | D3.1 | Neptune FAC hovertext labelling | **Absorbed by D3.1 Rule 2 sweep** |
| 47a | D3.2 | Neptune arc markers superimposed | Open |
| 47b | D3.2 | Neptune Lassell + Arago superimposed | Open |
| 48 | D3.3 | Mercury sodium tail sun_position wiring | Open |
| 49 | D3.3 | Earth fly-to-Sun distance | Open |
| 50 | D3.3 | Sun direction indicator per-body legendgroup | Open |
| 51 | E+ | Animation: non-center body shells | Open -- beyond D3 |
| 53 | D3.2 | Neptune magnetic center marker convention | Open |
| 54 | D3.1 | Hovertext/legendgroup sweep | **Inventory DONE; sweep pending review** |
| 55 | D3.1 | Solar shell naming: "Sun: X" convention | **NEW -- locked, sweep pending** |
| 56 | D3.1 | Crust/cloud shell legendgroup fix (15 builders) | **NEW -- detected by inventory, sweep pending** |
| 57 | D3.1 | Neptune magnetosphere double-leader (D2 artifact) | **NEW -- detected by inventory, sweep pending** |
| 58 | D3.1 | MAPS comet tails 7-leader consolidation | **NEW -- detected by inventory, sweep pending** |
| 59 | D3.1 | Deprecate `create_neptune_magnetic_poles` orphan | **NEW -- locked, sweep pending** |

Items 55-59 are new items surfaced or formalized by the D3.1 inventory.
All are scoped to the D3.1 sweep phase 2. None require Mode 7 review
to proceed (Tony has locked them); they're listed for traceability.

---

## Procedural Lessons from D3.1 Inventory

Tagged with v3.23 criticality framework.

**[QUALITY] -- Static analysis catches what visual testing cannot.**
Round 3 testing surfaced items 45 and 46 (Neptune radiation and FAC
labelling) as Neptune-specific bugs. The D3.1 inventory revealed they
are instances of a codebase-wide pattern affecting 116 entries. Without
the inventory, the sweep would have been 116 file-specific fixes
instead of one mechanical pattern. The inventory's value is precisely
that it sees the whole codebase at once.

**[QUALITY] -- Iterative refinement of the inventory rubric.** The
initial script run produced 40 FAILs. After tightening Rule 2 to check
all traces (not just the leader), the count jumped to 116. This was
not the script "breaking" -- it was the script finally measuring the
right thing. Lesson: when a checking tool produces a comforting low
number, ask whether it's checking what you actually want to check.

**[PRACTICE] -- Orphan detection as a side effect.** While verifying
the D2 deployment of Item 12 (Neptune diamond), the inventory surfaced
`create_neptune_magnetic_poles` as still-defined-but-never-called dead
code. D2 had moved the diamond inline to `create_neptune_magnetosphere`
but left the old function in place. The inventory caught this only
because the script reported 4 `showlegend=True` traces inside a function
that should be retired. Without that signal, the dead code would have
persisted indefinitely.

**[PRACTICE] -- Reviewable artifacts beat agent-produced narratives.**
The markdown inventory is structured for Opus 4.7 to read top-to-bottom
and answer specific questions. Sections 4 (findings by violation type)
and 5 (ambiguous cases) are the action items; everything else is
context. This shape is deliberate -- 4.7 doesn't need to re-derive
what the inventory found, only to verify and refine.

---

## Architecture Notes

The D3.1 sweep manifest will likely have the following shape:

```
For each shell file:
    Find every info marker construction site
    Identify the trace_name variable in scope
    Prepend f"{trace_name}<br><br>" (or \n\n) to the text= argument
    
For each crust/cloud shell builder (15 files):
    Add legendgroup=trace_name to the surface trace
    Strip "(Info)" suffix from info marker's name and legendgroup
    
For solar_visualization_shells.py (9 builders):
    Rename "Outer Oort Cloud" -> "Sun: Outer Oort Cloud"
    Rename "Sun's Gravitational Influence" -> "Sun: Gravitational Influence"
    [etc, 9 renames]
    
For neptune_visualization_shells.py:
    Add showlegend=False on the line-604 diamond
    Add deprecation comment to create_neptune_magnetic_poles docstring
    
For comet_visualization_shells.py:
    Pick one leader for add_comet_tails_to_figure (line 1760)
    Set showlegend=False on the other 6 traces
```

Total edit sites estimated: ~150-200 across 15 files. Most are one-line
or two-line edits in a consistent pattern. Bottom-up editing per the
protocol.

---

## Credit

```
Module updated: May 2026 with Anthropic's Claude Opus 4.7 (D3.1 inventory)
```

Opus 4.7 produced the inventory script and the four artifacts. Tony
made the editorial calls on solar convention and orphan disposition.
The Mode 7 review by Opus 4.7 (separate session) will validate the
proposed mechanical fix shape and check sampling-based false positive
rate before the sweep manifest is written.

---

*Paloma's Orrery | palomasorrery.com*
*"Static analysis catches what visual testing cannot." -- D3.1 lesson, May 2026*
*"When a checking tool produces a comforting low number, ask whether it's*
*checking what you actually want to check." -- D3.1 lesson, May 2026*
