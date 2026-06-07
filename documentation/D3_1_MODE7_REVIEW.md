# D3.1 Inventory Review -- Mode 7 Adversarial Audit

**Session:** May 22, 2026 (collegial Mode 7 review)
**Reviewer:** Anthropic's Claude Opus 4.7 (different session, same model)
**Integrator:** Tony Quintanilla
**Subject:** `D3_1_INVENTORY.md` produced by Opus 4.7 (prior session)

Review against the v3.23 protocol. Tony's locked decisions (solar
prefix, orphan deprecation, category-file treatment) are not relitigated
in the main body. Per the prompt, "Here's the job, flag problems."

---

## Pre-flight observation: an arithmetic gap in the framing

Before answering Q1, one thing the prior session and the round-trip
handoff both got slightly wrong, which the review document itself
makes recoverable.

The handoff and the prompt both say: *"116 of 134 legend entries are
flagged for 'hovertext does not lead with legend label.'"* The
inventory's own Section 2 says 116 FAIL out of 134 total. But the
"hovertext does not lead with legend label" violation (Rule 2) actually
fires on **102** entries, not 116. The 116 is the total FAIL count,
mixing Rule 2 with the 15 Rule 0 (missing-legendgroup), 14 Rule 3
(no-leader-in-group), 9 Rule 1 (Sun prefix), and the small handful of
Rule 4 (multi-leader) cases. Many entries violate two or three rules at
once -- so summing violation-buckets exceeds 116, and conflating "FAIL"
with "Rule 2 FAIL" understates the breadth of the secondary findings.

This isn't a content error -- Section 4 of the inventory shows the
correct per-rule counts. It's a framing error in the executive summary
that the sweep manifest should NOT inherit, because the post-sweep
verification re-run will look for the wrong target if it expects Rule 2
to be the only relevant pattern.

---

## Q1 -- Does the headline finding hold up?

**Yes, with one important refinement and one scope recommendation.**

The proposed fix -- prepend `f"{trace_name}<br><br>"` (or `\n\n`) to
every info marker's text -- is mechanically right and idempotent enough
for the sweep. I sampled three Rule-2 source sites (Earth magnetosphere
line 678, Neptune magnetosphere line 567, Earth crust shell line 446).
In all three cases:

1. The runtime hover text **does** contain the body name (e.g.,
   *"Earth's magnetosphere extends..."*).
2. The runtime hover text **does not** lead with the legend label
   (e.g., *"Earth: Magnetosphere\n\nEarth's magnetosphere extends..."*).
3. Prepending the legend label produces a clean, unambiguous hover
   header without making the prose redundant or wrong.

So the rubric's standard ("leads with the legend label") is genuinely
not met by the current state, even where the script's weaker proxy
("body name appears anywhere in first line") would say it is.

### The refinement: the script's check is a weak proxy for the rubric

This matters more than it looks. The inventory's Rule 2 implementation
is `body.lower() in m_hover.lower()`. Pass means "Earth" or "Neptune"
shows up somewhere in the first line. But the rubric (Section 1) says
*"the first line of hover text matches the legend entry name."* Those
are not the same standard. "Neptune's magnetosphere extends..." passes
the script and fails the rubric.

This has two implications:

- The script's false positive rate against itself is moderate (see
  Q2). The script's false positive rate against the rubric is very
  low. The prepend fix is correct under both readings, but the
  post-sweep verification deserves the stricter check (see Q6).
- The headline's claim ("Rule 2 violations dominate") would still
  hold even with the stricter check -- in fact it would be more
  comprehensive, because cases like Earth magnetosphere (which the
  script correctly flags, but partly for the wrong reason) would be
  unambiguously flagged.

### The scope recommendation: absorb the `\n` -> `<br>` normalization

Items 43 and 44 are currently scoped to D3.2 -- newline characters
inside hover strings rendering as literal `\n` in Plotly. The sweep
will touch every info marker in the codebase. Coming back later to
normalize newlines in the same strings is strictly more expensive than
doing both passes in the same edit. Suggest the D3.1 sweep manifest
absorb the newline normalization: wherever a hover-text edit lands,
replace any `\n` with `<br>` in the same string.

This expands D3.1's scope by maybe ~20% but eliminates D3.2's biggest
chunk. Tony's call.

---

## Q2 -- Sample false positive rate on Section 4

I sampled five `<expr>` entries from the per-file tables in Section 3,
chosen to span body types and structural patterns:

| Line | Source check | Runtime hover starts with | Script saw | Rubric verdict |
|------|--------------|---------------------------|------------|----------------|
| `earth_visualization_shells.py:678` | viewed | `"Earth's magnetosphere extends..."` | `magnetosphere_text=<expr>` (body name absent) | FAIL (no legend label) |
| `earth_visualization_shells.py:446` (crust info marker) | viewed | `layer_info['description']` (dictionary lookup, e.g. *"The Earth's crust is a thin..."*) | `<expr>` | FAIL (no legend label) |
| `neptune_visualization_shells.py:567` (envelope info marker) | viewed | `"Neptune's Magnetosphere: Unlike other planets..."` | `magnetosphere_text=<expr>` | FAIL (no legend label) |
| `neptune_visualization_shells.py:604` (D2 diamond) | viewed | `"Neptune's magnetic field center is offset..."` | `<expr>` | FAIL (no legend label) |
| `jupiter_visualization_shells.py:954` (ring system) | (inferred from inventory: `ring_info['description']`) | dictionary lookup, name-prefixed in source comment style | `ring_info['description']` (body name absent) | FAIL (no legend label) |

**Pattern observed.** In every sampled case, the script's `<expr>`
flag corresponds to a runtime string that **does** contain the body
name (it's somewhere in the description prose) but **does not** lead
with the legend label. So:

- Script false positive rate *against the script's own rule* (body
  name in hover): **high**, probably 60-80% of `<expr>` entries on
  spot-check. Most descriptions mention the body somewhere.
- Script false positive rate *against the rubric* (lead with legend
  label): **very low**, near zero. None of the sampled descriptions
  start with the legend label.

**Recommendation: prepend regardless.** The fix is mechanical and
idempotent-enough. Prepending `"Earth: Magnetosphere<br><br>"` to a
string that already mentions Earth somewhere is mildly redundant in
prose but operationally correct -- the user now sees the legend label
as a header. The conservative scenario the prompt asked about
("manual verification per row before applying the fix") is unnecessary;
the safe scenario ("prepend regardless") is preferred.

**One thing the script could not have caught but a careful sweep
should.** Two of the five sampled cases use a `layer_info['description']`
or `ring_info['description']` dictionary lookup. The dictionary content
lives in `shell_configs.py` (or wherever the config dict is sourced),
not at the trace construction site. The sweep manifest needs to
choose: prepend at the trace construction site (works, but every
trace duplicates the prefix logic) OR change the dict content
in `shell_configs.py` to include the prefix (single edit, but couples
hover-text formatting decisions to config data). I'd lean
construction-site -- it keeps formatting where the formatting lives --
but the manifest writer should make this call explicitly.

---

## Q3 -- Crust/cloud shell legendgroup fix

**Confirmed, with one specification refinement.**

I viewed `create_earth_crust_shell` (lines 372-459) to verify. The
proposed fix as stated is right:

1. Add `legendgroup=f"Earth: {layer_info['name']}"` to the surface
   `go.Mesh3d` at line 372 (currently missing).
2. Change the info marker's `legendgroup` at line 452 from
   `trace_name` (which equals `f"Earth: {layer_info['name']} (Info)"`)
   to `f"Earth: {layer_info['name']}"` -- matching the surface.
3. Change the info marker's `name` at line 451 from `trace_name` to
   the un-suffixed form, or simpler: redefine `trace_name` at line
   444 without the "(Info)" suffix so it can be used in both places.

The "(Info)" suffix exists because at the time the pattern was first
written, the info marker had its own legend entry. With the surface
trace getting `legendgroup` and the info marker being `showlegend=False`,
the "(Info)" suffix becomes redundant -- the info marker never appears
in the legend, only in mouseover tooltips, and there it's just
confusing.

### Refinement: an architectural alternative worth noting

Earth crust shell line 454 already does:
```python
customdata=[f"Earth: {layer_info['name']}"],
hovertemplate='%{text}<extra></extra>',
```

The customdata field is *already* carrying the legend label. A
slightly cleaner pattern would change the hovertemplate to:
```python
hovertemplate='%{customdata}<br><br>%{text}<extra></extra>',
```

This routes the prefix through Plotly's template engine instead of
string-concatenating into `text`. Earth magnetosphere line 675 follows
the same convention. It's a more elegant architecture and would let
the rubric standard ("lead with the legend label") be enforced
declaratively.

**But I'd defer this to a later cleanup.** D3.1 is a sweep, not a
refactor. The mechanical prepend is right for now. The customdata-
based approach is a v2 follow-up if the pattern proves useful.

---

## Q4 -- Neptune magnetosphere double leader

**Confirmed exactly as stated.**

I viewed lines 555-619 of `neptune_visualization_shells.py`. The trace
structure inside `create_neptune_magnetosphere` is:

- Line 567: magnetosphere envelope. `showlegend=True`,
  `legendgroup='Neptune: Magnetosphere'`, `hoverinfo='skip'`. Correct
  leader for the geometry.
- Line 590: `create_info_marker(...)` -- the standard info marker
  helper, presumably emits with `showlegend=False`. (Worth a quick
  glance at the helper to confirm, but the inventory's count of 3
  members suggests it does.)
- Line 604: D2 diamond at offset magnetic center. `showlegend=True`,
  `legendgroup='Neptune: Magnetosphere'`. **This is the bug.**

The fix is `showlegend=False` on the line-604 diamond. The diamond
stays in the legendgroup (toggles with the envelope) but doesn't claim
its own legend entry.

Side observation: the diamond's hover text at line 611 is a list
literal with implicit string concatenation -- exactly the AST pattern
that produces `<expr>` in the inventory. The runtime hover starts with
*"Neptune's magnetic field center is offset..."* which would pass the
script's body-name check but fail the rubric. So this trace gets
prepended in the Q1 sweep too. Two edits on the same line block,
one trip.

---

## Q5 -- MAPS comet tails 7-leader case

**Strong disagreement with the proposed framing.** The inventory's
read of this case is wrong -- not in the data, in the diagnosis.

I viewed `add_comet_tails_to_figure` at lines 1609-1825 of
`comet_visualization_shells.py`. The function is long; the
`showlegend=True` traces inside it are not redundant or
consolidatable. They are semantically distinct legend entries doing
real UI work:

| Line | Trace | Purpose |
|-----:|-------|---------|
| 1760 | `MAPS: Nucleus (disintegrated April 4, 2026)` | Post-disintegration in-memoriam placeholder. Tells the user the nucleus is gone. |
| 1796 | `f'{comet_name}: Coma (inactive, >{...} AU)'` | Far-from-Sun placeholder. Tells user coma is not visible at this distance. |
| 1805 | `f'{comet_name}: Dust Tail (inactive, >{...} AU)'` | Same -- dust tail inactive placeholder. |
| 1814 | `f'{comet_name}: Ion Tail (inactive, >{...} AU)'` | Same -- ion tail inactive placeholder. |

(There may be additional `showlegend=True` traces further down the
function -- I only viewed through line 1830 -- but the four above
are enough to make the structural point.)

These are NOT components of one structure. Each is a separate piece
of state communication: which features of this comet are inactive at
this rendering moment. Consolidating them into one leader would hide
that information from the user. The handoff's framing ("Big legend
clutter. Likely needs one consolidated leader and six followers") is
the wrong fix.

### Why the inventory misread this

The aggregator key is `(file, builder, legendgroup)`. All these
traces have `legendgroup` absent (which renders as `<none>` in the
inventory). So the aggregator groups them under
`(comet_visualization_shells.py, add_comet_tails_to_figure, <none>)`
-- one row -- and reports "7 showlegend=True traces in same group."
But at *runtime*, since `legendgroup` is absent on each trace, Plotly
treats each as its own implicit group. They're 7 (or however many)
separate legend entries already; the violation isn't "they share a
group, pick a leader," it's "they don't have explicit legendgroups
and so don't toggle correctly with paired info markers (none in this
case)."

### What the actual fix should be

Each of these placeholder traces should get its own explicit
legendgroup matching its name:

- Line 1760: `legendgroup='MAPS: Nucleus'` (or whatever consolidated
  name Tony prefers for the in-memoriam state)
- Line 1796: `legendgroup=f'{comet_name}: Coma'`
- Line 1805: `legendgroup=f'{comet_name}: Dust Tail'`
- Line 1814: `legendgroup=f'{comet_name}: Ion Tail'`

This way each placeholder is its own leader of its own group, and
when the comet *is* active and the real coma/dust/ion tail traces
render (from `create_comet_coma`, `create_comet_dust_tail`, etc., in
the other branch of the function), those active traces use matching
group names and the legend stays stable across distance regimes. The
"7 leaders in same group" violation disappears not because traces
are consolidated but because they were never really in the same group
at runtime.

I'd recommend the sweep manifest reclassify this case from "multi-
leader consolidation" to "missing legendgroup on placeholder traces."
It belongs in the same bucket as the 15 crust/cloud shell fixes
(Q3) -- "add explicit legendgroup matching the name."

**Editorial question for Tony before the sweep writes this:** what
about the active-state traces produced by lines 1739, 1750? Those
get renamed to `'MAPS: Dust Trail (Remains)'` and `'MAPS: Ion Trail
(Remains)'`. Do they share legendgroups with the inactive placeholders
(so users see one entry that switches state), or do they live in
their own groups (so users see active/inactive as distinct entries)?
This is a UX call, not a mechanical one. The current code makes them
distinct; the fix should be intentional either way.

---

## Q6 -- Did the inventory miss anything?

Several things, in order of importance:

### 6a. The "no ambiguous cases detected" claim is incorrect

Section 5 says: *"No ambiguous cases detected. Either every multi-
trace group violated a rule (caught in Section 4) or every group has
exactly 2 traces (geometry + info marker)."*

The MAPS case (Q5 above) is the most obvious counterexample: it WAS
flagged as a rule violation, but the rule it was flagged under
("multiple leaders in same group") was the wrong diagnosis. The
inventory's automated rules collapsed an ambiguous case into a
mis-diagnosed FAIL. This is a category of failure the rubric should
acknowledge: *"the script flagged something but the right fix is
not what the violation type suggests."* Mars Hill Sphere at lines
894/910 (one OK entry and one FAIL entry from the same builder) is
another suspicious pair -- not a clear ambiguity, but worth a manual
look during the sweep.

### 6b. Moon Hill Sphere label is not body-prefixed

`moon_visualization_shells.py:555` has `trace_name='Hill Sphere'`
(no "Moon:" prefix). The inventory does not flag this under Rule 1
"label does not start with 'Moon:'" -- which means the Rule 1
implementation has a hole. The script's Rule 1 check goes into
the literal-string branch only when `legend_label` starts with `'`
or `"`. But for `trace_name='Hill Sphere'`, the captured
`legend_label` is `trace_name='Hill Sphere'` (the variable-equals-
value form). That doesn't start with a quote, doesn't contain `{`,
so neither branch fires.

**Recommend the sweep manifest add Moon Hill Sphere to the rename
list:** `'Hill Sphere'` -> `'Moon: Hill Sphere'`. This is a small
finding but the kind of thing that would slip past a post-sweep
re-run of the same inventory script if not explicitly added.

### 6c. The "create_neptune_magnetic_poles" orphan has its own internal multi-leader

The inventory flags `create_neptune_magnetic_poles` (line 663) as
ORPHAN and notes "(also: function not called anywhere)." The flag
also includes "multiple showlegend=True traces in same group (4)" --
which is true but moot, since the function is dead code awaiting
deprecation per Tony's lock.

This is not a real bug, but the per-violation tally in the executive
summary is inflated by 1 because of it. The sweep manifest should
not include a fix for line 663 (the deprecation comment is the only
edit). Post-sweep verification will still see "multiple leaders" on
this function unless the script is taught to skip orphan-flagged
functions. Worth a script tweak when re-running.

### 6d. Loop-generated traces -- the inventory mostly handles this, but one note

The inventory correctly notes (Section 6) that loop-generated builders
like `create_neptune_radiation_belts` collapse to one row but emit N
entries at runtime. The fix is straightforward: prepend
`f"Neptune: {belt['name']}<br><br>"` to `belt['description']` inside
the loop body -- one edit, N runtime effects.

The note worth adding: the prepend string MUST use the loop's per-
iteration name variable, not a static label. The manifest writer
should explicitly identify the per-iteration name expression
(`belt['name']`, `ring_info['name']`, `params['name']`, etc.) for
each loop, since they're not all called the same thing across files.
Easy to get wrong if scripted blindly.

### 6e. Verification gap after the sweep

The current inventory script's Rule 2 check is `body.lower() in
m_hover.lower()`. After the sweep prepends legend labels, this check
will pass trivially -- but it won't actually verify that the prepend
was done correctly, only that the body name appears somewhere. The
post-sweep verification should use a stricter rule, something like:

```python
# Stricter: hover must start with the legend label
expected_prefix = legend_label.strip("'\"")
if not m_hover_resolved.startswith(expected_prefix):
    violations.append("hover does not start with legend label")
```

This requires the script to actually resolve `m_hover` more
aggressively (it currently can't see through `belt['description']`
lookups). The simpler verification might be a manual sample of 10-20
post-sweep hovers via the visual-verification path (Mode 5, Tony's
eyes). The script re-run is necessary but not sufficient.

---

## Additional findings

### Sweep ordering

Suggest the manifest order edits in batches that can each be
verified independently before moving on:

1. **Solar prefix renames** (9 edits, one file). Verifiable by
   re-running the inventory and confirming the "label does not
   start with 'Sun:'" count drops to 0.
2. **Multi-leader fixes** (Neptune line 604 `showlegend=False`,
   MAPS legendgroup additions per Q5). Verifiable: re-run inventory,
   confirm Rule 4 violations drop.
3. **Orphan deprecation** (one docstring edit on
   `create_neptune_magnetic_poles`). Verifiable: re-read the
   function, confirm the deprecation comment is present.
4. **Crust/cloud legendgroup fix** (15 builders, three edits each).
   Verifiable: re-run inventory, confirm "leader trace missing
   legendgroup attribute" drops to ~3 (the comet entries that need
   different treatment).
5. **Rule 2 prepend sweep** (the big one, ~100 edits). Verifiable
   by *strict* version of the script (per 6e) plus Mode 5 visual
   sampling.

Bottom-up by line number within each file (protocol convention).
But the batches should be sequential -- each one's verification
result informs the next.

### Risk: shell_configs.py vs. trace construction site

For the dictionary-lookup hovers (`layer_info['description']`,
`ring_info['description']`, etc.), the sweep can prepend at the
trace construction site (clean, but every trace duplicates the
prepend logic) or at the config dict source (single source of
truth, but couples hover formatting to config data). Construction-
site is the simpler manifest. Config-dict is the cleaner long-term
architecture. Recommend construction-site for D3.1; revisit if it
proves painful.

### Risk: hovertemplate vs. text-prepend

Per the customdata observation in Q3, some traces already use
`customdata=[legend_label]` alongside their text. The sweep could
exploit this by changing `hovertemplate='%{text}<extra></extra>'` to
`'%{customdata}<br><br>%{text}<extra></extra>'` wherever customdata
is set. This is more elegant but adds variability to the manifest
(some sites get text-prepend, others get hovertemplate change).
Recommend: uniform text-prepend for D3.1 to keep the manifest
mechanical; the customdata refactor is a v2 cleanup.

### Risk: file size

The Single Info Marker codebase-wide refactor (v3.22) saved 9-13 MB
per render. D3.1 prepends a ~20-30 character prefix to ~100 hover
strings. Net delta per render: maybe +3 KB. Inconsequential, but
worth noting that we're going slightly *up* in HTML size, not
down. Different optimization axis (UX vs. file size).

### Confidence checks for the manifest writer

When writing the sweep manifest, the manifest writer should:

- For each edit site in `d3_1_inventory.py`, verify the `trace_name`
  variable is actually defined in scope at the construction site.
  In the crust shell pattern, it's defined at line 444 (just before
  the info marker). In other patterns, the legend label is inline
  as a literal. The manifest should explicitly state which variable
  to use for each site.
- For loop-generated builders, explicitly identify the per-iteration
  name expression (per 6d above).
- Use Python binary mode (`rb`/`wb`) for all edits (protocol).
  Bottom-up line ordering within each file (protocol).
- Run xvfb pre-test after each batch (protocol).

---

## Summary

| Question | Verdict | Action |
|---------:|---------|--------|
| Q1 Headline | Yes, with refinement | Prepend everywhere; absorb `\n` -> `<br>` normalization; strengthen post-sweep check |
| Q2 FP rate | High vs. script, near-zero vs. rubric | Prepend regardless; no manual triage needed |
| Q3 Crust/cloud | Confirmed, refined | Drop "(Info)" from both name and legendgroup; redefine `trace_name` at definition site |
| Q4 Neptune double leader | Confirmed | `showlegend=False` on line 604 diamond |
| Q5 MAPS 7-leader | **Disagreement** | Not consolidation -- assign distinct legendgroups; UX question for Tony on active/inactive state |
| Q6 Missed items | Several | Moon Hill Sphere rename; Mars Hill Sphere pair; orphan tally inflation; verification strictness |

Overall: the inventory does its job. The headline finding is right
even if the framing arithmetic ("116 of 134") slightly conflates
total FAIL with Rule 2 FAIL. The big disagreement is Q5, where the
proposed mechanical fix ("pick one leader") is wrong for what the
traces actually are. The next session writing the sweep manifest
should treat the MAPS case the way it treats the crust/cloud
case -- not the way it treats the Neptune magnetosphere case.

---

*Module updated: May 2026 with Anthropic's Claude Opus 4.7
(Mode 7 collegial review)*

*"Three Claudes, one Tony, zero orchestration framework." -- May 2026*
*Paloma's Orrery | palomasorrery.com*
