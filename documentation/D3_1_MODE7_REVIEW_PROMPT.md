# D3.1 Inventory Review -- Mode 7 Adversarial Audit

You are being asked to perform a Mode 7 adversarial review of a D3.1
inventory artifact for Paloma's Orrery -- Tony Quintanilla's solar
system / Earth system / climate visualization suite. This is the
collegial Mode 7 pattern: same-capability relay, Tony is the
integrator, your job is to push back productively. Treat this the
way you would treat a colleague's draft handed to you for review --
flag problems, propose better answers, and don't validate to be
polite.

The Paloma's Orrery v3.23 protocol applies. If Tony has not attached
it, ask for it before proceeding.

---

## Context (brief)

Paloma's Orrery is ~99 modules / ~86K lines. Phase D of the shell
consolidation work is cleaning up the magnetosphere/shell visualization
plumbing.

- **D2** (May 20-22, 2026) deployed `sun_position` threading through
  the static-rendering dispatch.
- **D3** is the cleanup sweep.
- **D3.1** is item 54: hovertext labels and legendgroup assignments
  across all 15 `*_visualization_shells.py` files.

D3.1 has two phases:

1. **Inventory** -- completed in a prior session, awaiting your
   review now.
2. **Sweep manifest** -- not yet started. Your review feeds this.

---

## What you are reviewing

**`D3_1_INVENTORY.md`** (attached). Six sections:

- Section 1: Convention rubric (the three rules)
- Section 2: Conformance summary (per-file)
- Section 3: Per-file detail tables
- Section 4: Findings grouped by violation type
- Section 5: Ambiguous cases
- Section 6: Known issues + script limitations

Supporting artifacts available if you want to drill into raw data
(attach on request):

- `inventory_per_legend_entry.csv` -- 134 rows aggregated
- `inventory_per_trace.csv` -- 249 rows raw
- `d3_1_inventory.py` -- the script that produced all three;
  preserved as a verification tool to re-run after the sweep

---

## The inventory's headline claim

**Rule 2 violations dominate.** 116 of 134 legend entries are flagged
for "hovertext does not lead with legend label." The proposed
mechanical fix is: prepend `f"{trace_name}<br><br>"` (or `\n\n`,
depending on the file's existing newline convention) to every info
marker's `text` argument across the codebase. The trace name is
already in scope wherever info markers are constructed.

This explains Round 3 items 45 and 46 (Neptune radiation belts and
FAC hovertext "not clearly labelled to connect to the legend") as
instances of a codebase-wide pattern, not Neptune-specific bugs.

---

## Tony's locked decisions -- do not propose reverting

These were settled before you got here. Not open for review:

1. **Solar shells will use `"Sun: X"` prefix consistently.** The 9
   entries currently labeled `"Outer Oort Cloud"`, `"Sun's
   Gravitational Influence"`, etc. will be renamed to follow the
   convention.
2. **`create_neptune_magnetic_poles` orphan function will be
   deprecated** (docstring note) but kept in source for historical
   reference. Not removed.
3. **asteroid_belt and comet files are category files.** Rule 1
   (Body: prefix) and Rule 2 (hover echoes body) are suppressed for
   these two files. Their labels use population names and
   comet-specific names instead.

If you disagree with any of these on technical grounds, note it in
"additional findings" but do not litigate it in your main review --
they are Tony's editorial calls.

---

## What is asked of you

Six specific questions, answered in order. Plus a free-form section
for anything else you flag.

### Q1. Does the headline finding hold up?

Is "prepend legend label to info marker text" the right mechanical
fix for all 116 Rule 2 violations? Or are there subcategories where
a different fix is needed?

Possible subcategories worth considering:
- Short, single-line hovers that already work fine without a prefix
- Multi-trace assemblies where the label is already implicit
- Anything that should be left alone for historical or aesthetic
  reasons

State your conclusion and your reasoning. If "prepend everywhere"
is wrong, propose the better shape.

### Q2. Sample false positive rate on Section 4

Several FAIL entries in Section 4 are script-limitation false
positives. When the hover text is built from list-of-strings
concatenation inside a list literal (e.g.,
`text=["Foo bar...<br>" "continued..."]`), the script's
`render_expr` returns `<expr>` and the body-name check fails -- even
though the runtime string may begin with the body name.

Spot-check 5-10 `<expr>` entries from Section 4 against the source
files. Estimate the false positive rate:

- **High (>25%):** the sweep should be more selective. Manual
  verification per row before applying the fix.
- **Low (<10%):** "prepend regardless" rule is safest. The fix
  is mechanical and idempotent -- prepending the label to a string
  that already starts with the label produces a slightly redundant
  but not incorrect result.
- **Middle:** propose a heuristic to triage automatically.

Show your work: which entries you sampled, what each turned out
to be, and your inferred rate.

### Q3. Crust/cloud shell legendgroup fix

15 entries (Section 4, "leader trace missing legendgroup attribute")
have geometry trace missing `legendgroup` and paired info marker
with its own legendgroup plus an `(Info)` suffix in both `name` and
`legendgroup`.

Proposed fix:
- Add `legendgroup=trace_name` on the geometry surface trace
- Strip `(Info)` suffix from the info marker's `legendgroup` (so
  it matches the surface)
- Strip `(Info)` suffix from the info marker's `name` (the info
  marker uses `showlegend=False` anyway, so the name is only used
  for accessibility/debugging; consistency with the surface is
  better)

Confirm, or counter-propose.

### Q4. Neptune magnetosphere double leader

D2 deployment left two `showlegend=True` traces in the same
legendgroup `'Neptune: Magnetosphere'`:

- Line 567: magnetosphere envelope (correct leader)
- Line 604: D2 diamond at the offset magnetic center (incorrectly
  exposed as a second leader)

Proposed fix: `showlegend=False` on the line-604 diamond. The
diamond stays in the legendgroup so it toggles with the envelope,
but it is not its own legend entry.

Confirm.

### Q5. MAPS comet tails 7-leader case

`add_comet_tails_to_figure` at line 1760 in
`comet_visualization_shells.py` has 7 traces all `showlegend=True`
in one legendgroup. Examine the source. Which trace should be the
leader, and what label should the consolidated legend entry use?

Note: comet is a category file, so the label does not need a
`"Comet:"` prefix. The current top-leader name
`'MAPS: Nucleus (disintegrated April 4, 2026)'` may or may not be
the right consolidated label.

### Q6. Did I miss anything?

The inventory script saw 249 trace constructors and aggregated to
134 legend entries. Loop-generated traces (radiation belts, ring
systems, multi-arc structures) collapse to one inventory row even
though they emit N legend entries at runtime.

Are there rows where the loop hides a real bug the inventory did
not surface? Are there entries in Section 3 you would re-classify
from OK to FAIL or vice versa? Anything else the rubric should
have caught but did not?

---

## Additional findings (free-form)

After Q1-Q6, list anything else that struck you while reading the
inventory. Possible categories:

- Patterns the inventory surfaced but did not name
- Architectural concerns about the shell-builder layer
- Risks in the proposed sweep (what could go wrong)
- Suggested ordering for the sweep manifest (which fixes go first,
  why)
- Recommendations for what to test after the sweep

You have explicit permission to disagree with the headline finding,
the rubric, or any methodological choice the previous session made.
Tony wants honest pushback. The v3.23 protocol explicitly flags
validation loops as an anti-pattern.

---

## Deliverable

A markdown document, similar shape to the inventory but shorter
(this is review, not re-derivation). One section per question Q1-Q6,
then "Additional findings." Each section: your answer, your
reasoning, your counter-proposal if any.

Tony will carry your review back to a new session, which will write
the D3.1 sweep manifest from the agreed-on findings.

---

*Mode 7 collegial pattern. Same model, different session, no*
*orchestration framework. "Here's the job, flag problems."*
