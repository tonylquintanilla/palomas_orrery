# Shell Consolidation -- Phase D3.1 Handoff (v6, platform-neutrality deferred item added)

**Sessions:**
- May 22, 2026 -- Inventory + Mode 7 review (Opus 4.7 x2)
- May 23, 2026 (AM) -- Sweep implementation (Opus 4.6)
- May 23, 2026 (mid) -- Runtime verification + Earth fix (Opus 4.7)
- May 23, 2026 (PM) -- **Dispatch-path scope discovery + structural fix (Opus 4.7)**
**Integrator:** Tony Quintanilla
**Status:** All 5 batches applied across 15 per-body files. Dispatch-path
structural fix applied to `orrery_rendering.py` and `shared_utilities.py`.
Both smoke tests pass. Mode 5 visual verification pending.

**Next session entry point:** Tony runs the Mode 5 testing protocol v3.
If all pass, deploy to GitHub and write D3.1 closeout. If any fail,
upload notes and fix in next session.

---

## What changed since v4

During Mode 5 visual testing of Render 1 (Mercury), Tony noticed
inconsistent Rule 2 header application -- some Mercury shells had the
header, others did not, with the crust hover specifically lacking any
label. Investigation revealed a **parallel rendering pipeline that the
original D3.1 inventory never saw.**

### The scope discovery

The 15 per-body `*_visualization_shells.py` files contain shell-builder
functions that the original inventory catalogued. But Paloma's Orrery
has been migrating to a **unified config-driven dispatch** as part of
Step 3 (Phases A through C4). At present:

```
SHELL_CONFIGS  (shell_configs.py)
    -> create_celestial_body_visualization  (planet_visualization.py)
       -> build_sphere_shell                (orrery_rendering.py)
          -> create_info_marker
```

**All 12 bodies route through this path:** Mercury, Venus, Earth,
Moon, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto, Eris, Planet 9.
For each body, standard interior shells (`inner_core`, `outer_core`,
`mantle`, `crust`, `atmosphere`, `hill_sphere`, and similar) are
rendered from `SHELL_CONFIGS` via `build_sphere_shell` -- not from
the per-body builder functions.

Custom geometries (magnetospheres, ring systems, radiation belts,
LEO/GEO for Earth) still go through per-body builders via the
`CUSTOM_SHELLS` dispatch -- those sweep edits remain on the live path.

### What the D3.1 inventory missed

`build_sphere_shell` constructed traces with `trace_name = "Body: Shell"`
as legendgroup but passed `config['hover_text']` to `create_info_marker`
with **no Rule 2 prepend**. So every body's standard interior shells
rendered with hover text starting at the description prose, with the
legend label absent as a structural header.

`shared_utilities.create_sun_direction_indicator` had the same gap:
`info_text` started with `"Sun Direction:"` in prose rather than as a
structural header.

The original `d3_1_inventory.py` script scanned only the 15 per-body
files. The unified dispatch never appeared in the inventory CSV. The
original `d3_1_runtime_smoke.py` exercised the per-body shell-builder
functions directly -- which work, but are no longer the active path
for standard interior shells. **We tested the trees while Plotly
renders from the forest.**

### The structural fix

Two single-block edits resolved the entire dispatch-path gap.

**`orrery_rendering.py`** -- in `build_sphere_shell`, the info marker
construction now prepends `trace_name` to `config['hover_text']`:

```python
info_trace = create_info_marker(
    center_x, center_y, center_z + r_info,
    config['color'],
    "%s<br><br>%s" % (trace_name, config['hover_text']),
    trace_name
)
```

**`shared_utilities.py`** -- in `create_sun_direction_indicator`,
`legend_name = 'Sun Direction'` moved above `info_text` construction,
and `info_text` now leads with `f"{legend_name}<br><br>"`.

**Coverage:** 83 sphere-shell pairs across 13 SHELL_CONFIGS entries
(includes Sun's 15 shells) + 1 sun direction indicator. All pass the
dispatch-path smoke test.

### Why this fix does not double-prepend with the per-body sweep

The per-body `*_visualization_shells.py` interior shell builders
(`create_earth_inner_core_shell`, `create_mercury_*` interior shells,
etc.) are still defined and importable, but no longer invoked by the
active dispatch. They are functionally dead code for standard interior
shells, kept for now to avoid breaking any callsite we have not yet
verified. The May 23 morning Earth fix to those interior-shell builders
is therefore a no-op on the live render -- it remains correct in the
file, just unreached.

The custom-geometry builders (magnetospheres, LEO/GEO, ring systems,
radiation belts) ARE still on the active path via CUSTOM_SHELLS. Their
prepends from the D3.1 sweep are live and correct. The dispatch-path
fix does not touch this code path.

---

## Edit Counts (updated)

| Batch | Scope | Edit sites | Files | Status |
|------:|-------|------------|------:|--------|
| 1 | Solar prefix renames | 27 (9 entries x 3) | 1 | Done |
| 2 | Multi-leader + comet legendgroups | 10 | 2 | Done |
| 3 | Orphan deprecation + Moon Hill Sphere | 2 | 2 | Done |
| 4 | Crust/cloud legendgroup fix | 22 (11 files x 2) | 11 | Done |
| 5 | Rule 2 prepend + `\n` normalization | ~107 prepends + ~700 `\n` -> `<br>` | 15 | Done |
| -- | Earth runtime-fix supplement (May 23 AM) | 15 | 1 | Done |
| -- | **Dispatch-path structural fix (May 23 PM)** | **2** | **2** | **Done** |
| -- | Module docstring credits | 15 | 15 | Done |

The dispatch-path fix's 2 edits cover 83 (body, shell) pairs + 1 sun
direction indicator -- the leverage ratio (83 + n indicator instances
to 2 edits) is why a structural fix beats data-side edits at scale.

---

## Artifacts Produced (updated)

| Artifact | Session | Role |
|----------|---------|------|
| `D3_1_INVENTORY.md` | May 22 | Rubric, per-file detail (now known to be scope-limited) |
| `D3_1_MODE7_REVIEW.md` | May 22 | Q1-Q6 answers |
| `D3_1_SWEEP_MANIFEST.md` | May 22 | Five-batch edit plan with snippets |
| `D3_1_TESTING_PROTOCOL.md v3` | May 23 PM | Mode 5 verification, dispatch-fix aware |
| `d3_1_runtime_smoke.py` | May 23 mid | Per-body builder smoke test |
| `d3_1_dispatch_smoke.py` | May 23 PM | **NEW.** Dispatch-path smoke test |
| `apply_d3_1_earth.py` | May 23 mid | Transactional patcher (Earth) |
| `inventory_per_legend_entry.csv` | May 22 | 134 rows (scope-limited) |
| `inventory_per_trace.csv` | May 22 | 249 rows (scope-limited) |
| `d3_1_inventory.py` | May 22 | Static-analysis script (scope-limited) |

The inventory artifacts are scope-limited to the 15 per-body files.
Treat them as historical -- a future inventory must also walk
SHELL_CONFIGS via build_sphere_shell.

---

## Mode 5 Note: Double-Header Survey

The dispatch-path fix introduces 14 cases where the legend label
header sits above a prose lead-in that also names the shell. These
are structurally correct but visually redundant. Tony should evaluate
each during Mode 5:

| Body | Shells with double header |
|------|---------------------------|
| Mercury | inner_core, outer_core, mantle, atmosphere, hill_sphere |
| Eris | mantle, atmosphere |
| Jupiter | metallic_hydrogen, molecular_hydrogen |
| Mars | mantle, upper_atmosphere |
| Moon | outer_core |
| Pluto | haze_layer, atmosphere |

If any look ugly, the fix is a content edit to the `hover_text` field
in `shell_configs.py` for that shell -- remove the redundant prefix
from the prose. This is content judgment, not structural.

Mercury's `crust` shell -- the original complaint -- now reads
correctly: `"Mercury: Crust<br><br>(Note: toggle off the crust layer...)"`.
The header is present; the prose does not redundantly repeat the
shell name.

---

## Platform Neutrality (deferred -- new in v6)

**Project goal:** code runs equally on Windows, macOS, and Linux.
Tony confirmed this as an explicit principle on May 23, 2026.

**Known exception:** `palomas_orrery.py` uses `SystemButtonFace` as a
Tk color name. This resolves correctly on Windows but does not resolve
on Linux or macOS. The agentic pre-test protocol works around it with
`sed s/SystemButtonFace/gray90/g` before xvfb and a restore-after --
that is a workaround, not a fix.

**Platform-neutral fix options** (pick one in a future session):
- (a) Use a hex literal that resolves the same on every platform,
      e.g. `'#F0F0F0'` for the standard Tk button face color.
- (b) Detect platform at startup and pick the right native color name
      (`SystemButtonFace` on Windows, native equivalent elsewhere).
- (c) Migrate to `ttk` styling, which reads the OS theme natively and
      removes most explicit color choices.

**Audit also deferred.** SystemButtonFace is the visible headliner.
A full codebase audit for other platform-specific patterns has not
been done. Candidates worth scanning for:
- Other Tk color names (`SystemWindow`, `SystemHighlight`, etc.)
- Hardcoded path separators (`\\` vs `/`); use `pathlib` or `os.path.join`
- Unicode characters in `print()` calls (break on Windows cp1252
  consoles -- protocol already enforces ASCII-only by convention)
- OS-specific syscalls or shell-outs
- File-encoding assumptions (open() default differs slightly across
  platforms; explicit `encoding='utf-8'` is safer)

**Confirmation that D3.1 introduced no new violations:** the
dispatch-path fix in `orrery_rendering.py` and `shared_utilities.py`
is pure Python string formatting -- no OS-specific calls, no
hardcoded paths, no shell-outs. The fix is platform-neutral by
construction.

**Tracking number:** Deferred item 61. Stage: open (not blocking
D3.1 closeout; pick up in a future targeted session or as part of a
broader cross-platform pass).

---

## Post-Sweep Checklist (updated)

| # | Task | Status |
|---|------|--------|
| 1 | All 15 per-body files `py_compile` clean | Done |
| 2 | All 15 per-body files runtime-construct without exceptions | Done |
| 3 | Per-body smoke test passes | Done (1 known false positive) |
| 4 | **Dispatch-path smoke test passes** | **Done (May 23 PM)** |
| 5 | `orrery_rendering.py` + `shared_utilities.py` compile clean | Done |
| 6 | xvfb GUI launch | Done |
| 7 | Module docstring credits on all touched files | Done |
| 8 | Mode 5 visual verification (8-render protocol v3) | Pending -- Tony |
| 9 | Run provenance scanner on touched files | Pending |
| 10 | Update Module Atlas (`module_atlas.py`) | Pending |
| 11 | Deploy to GitHub | Pending (after Mode 5 pass) |
| 12 | Write D3.1 closeout summary | Pending |

---

## Procedural Lessons (updated)

[Lessons from inventory, Mode 7 review, sweep implementation, and
runtime verification unchanged -- see v4.]

### From D3.1 dispatch-path discovery (May 23 PM)

**[CRITICAL] -- Inventory scope is itself an artifact subject to
review.** The D3.1 inventory scanned 15 `*_visualization_shells.py`
files and never asked "what else renders shells?" The unified
dispatch had been the active path for standard interior shells for
months (Step 3 Phases A-C4), but the inventory framework never
walked SHELL_CONFIGS. A scope decision made by the inventory tool
silently became a scope decision for the entire sweep.

The pattern matches the existing protocol lesson "position data
flows through 5 parallel pipelines in palomas_orrery.py -- ALL must
be patched." Generalization: any inventory of "what is the
codebase's state for property P" must enumerate the rendering paths
P traverses, not just the files where P is most commonly defined.

For future codebase-wide sweeps: the first artifact should be a
**pipeline map** -- which rendering paths exist, which files
participate at which stage. The inventory then walks every stage,
not just the files in stage one.

**[CRITICAL] -- A smoke test that exercises the wrong path passes
falsely.** `d3_1_runtime_smoke.py` exercised per-body shell-builder
functions and reported PASS. But the per-body interior shell
builders are no longer the active path. The smoke test was correct
about the code it tested; the code it tested was the wrong code to
test. Compile-clean is insufficient verification; runtime-smoke of
the wrong path is also insufficient. The only sufficient
verification is exercising the actual rendering dispatch.

The new `d3_1_dispatch_smoke.py` walks `SHELL_CONFIGS` and calls
`build_sphere_shell(config, body)` for every (body, shell) pair --
the live dispatch. This is what should have been written from the
start.

**[QUALITY] -- Structural fixes scale; data-side fixes do not.**
83 sphere-shell pairs across 13 bodies were brought into compliance
by 2 edits to `build_sphere_shell` and `create_sun_direction_indicator`.
The alternative (editing every `hover_text` field in `shell_configs.py`
to prepend the label) would have been ~83 edits and would have
duplicated label text in every config. A single point of formatting
in `build_sphere_shell` makes the convention testable and revisable
in one place.

The general rule: when a violation appears in N consumers of the
same producer, fix the producer. When the producer is shared infra,
the fix is cheap and the test surface shrinks.

**[PRACTICE] -- "If it ain't broke, don't fix it" applies to the
per-body interior shell builders.** The Earth interior shell
builders (`create_earth_inner_core_shell`, etc.) are no longer the
active path but they remain in their file with correct Rule 2
prepends. They are not broken; they are dormant. Stripping them
out is a separate cleanup pass that needs its own scoping. For now,
they stay -- the no-op cost is zero, the deletion risk is non-zero
(some caller might still reach them).

**[PRACTICE] -- Tony's eyes win. Again.** This finding emerged
because Tony noticed during Mode 5 visual testing of Render 1
(Mercury) that some shells had the header and others did not. The
inventory said the codebase was clean. The per-body smoke test
said the codebase was clean. Mode 5 visual testing said it was not.
"Trust your eyes. When Claude explains away what Tony's eyes see,
that is the moment to be most skeptical" -- the protocol said it,
the protocol was right.

---

## Credit (updated)

```
D3.1 sweep -- Shell Consolidation Phase D3.1
  Inventory:        Anthropic's Claude Opus 4.7 (May 22, 2026)
  Mode 7 review:    Anthropic's Claude Opus 4.7 (May 22, 2026, separate session)
  Review prompt:    Anthropic's Claude Opus 4.6
  Sweep manifest:   Anthropic's Claude Opus 4.7
  Implementation:   Anthropic's Claude Opus 4.6 (May 22-23, 2026)
  Runtime verify:   Anthropic's Claude Opus 4.7 (May 23, 2026 mid)
  Earth fix:        Anthropic's Claude Opus 4.7 (May 23, 2026 mid)
  Dispatch-path:    Anthropic's Claude Opus 4.7 (May 23, 2026 PM)
  Integrator:       Tony Quintanilla
  Models involved:  3 (Opus 4.6, Opus 4.7 x4 sessions)
  Orchestration:    zero frameworks -- Tony carries context between sessions
```

---

*Paloma's Orrery | palomasorrery.com*

*"We tested the trees while Plotly renders from the forest."*
*-- D3.1 dispatch-path lesson, May 23, 2026 PM*

*"When a violation appears in N consumers of the same producer,*
*fix the producer."*

*"Tony's eyes win. The inventory said clean, the smoke test said*
*clean, Mode 5 said no."*
