# Shell Consolidation -- Phase D3.1 Handoff (v8, codebase audit + corrected diagnosis)

**Sessions:**
- May 22, 2026 -- Inventory + Mode 7 review (Opus 4.7 x2)
- May 23, 2026 (AM) -- Sweep implementation (Opus 4.6)
- May 23, 2026 (mid) -- Runtime verification + Earth fix attempt #1 (Opus 4.7)
- May 23, 2026 (PM) -- Dispatch-path scope discovery + structural fix (Opus 4.7)
- May 23, 2026 (PM2) -- Earth magnetosphere signature fix (Opus 4.7)
- May 23, 2026 (PM3) -- **Earth reconstructed from Tony's archive base; codebase audit (Opus 4.7)**
**Integrator:** Tony Quintanilla
**Status:** All 5 batches applied across 15 per-body files. Dispatch-path
structural fix applied to `orrery_rendering.py` and `shared_utilities.py`.
Earth reconstructed from Tony's archived working copy with D2 work
preserved and D3.1 sweep applied. Codebase audit confirms only Earth
regressed; all other 14 per-body files + 5 infrastructure files are in
expected state. **Tony's live working repo is clean and ready for Mode 5.**

**Next session entry point:** Tony runs the Mode 5 testing protocol v3
in a new session. If all pass, deploy to GitHub and write D3.1 closeout.

---

## What changed since v7

v7 diagnosed Earth's missing `sun_position` parameter as a "latent
Phase D2 bug" and added Item 62 to track restoring Earth's rotation
work. v8 corrects this: Earth's D2 work was never absent from D2
itself, only from the corrupted intermediate base that D3.1 ran
against on May 22. After Tony uploaded his archived working copy
(D2 intact), Earth was reconstructed cleanly by applying the D3.1
patcher to that base. A codebase audit confirmed Earth was the only
file to have regressed; the other 14 per-body files and 5
infrastructure files are in expected state. Item 62 is closed
(Earth rotation was always there). Tony's live working repo is
ready for Mode 5 in a new session.

See "Earth Regression Diagnosis and Reconstruction" and "Codebase
Audit" sections below for full detail.

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
| `d3_1_dispatch_smoke.py` | May 23 PM | Dispatch-path smoke test (sphere + custom) |
| `audit_d2_d3_1.py` | May 23 PM3 | **NEW.** Codebase audit vs D2 + D3.1 manifests |
| `apply_d3_1_earth_archive.py` | May 23 PM3 | **NEW.** Transactional patcher for Earth (from archive base) |
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

## Earth Regression Diagnosis and Reconstruction (corrected in v8)

### What v7 said (wrong)

v7 of this handoff diagnosed Earth's missing `sun_position` parameter
as "a latent Phase D2 bug" -- Earth as the one D2 outlier where the
sun_position contract was set in `CUSTOM_SHELLS` but the builder
signature was never updated. v7 added Item 62 (Earth magnetosphere
rotation toward Sun) as a deferred follow-up because the v7 fix only
added the parameter without restoring rotation work.

**This was wrong.** Tony's archived working copy of
`earth_visualization_shells.py`, uploaded after the v7 diagnosis,
contained the full D2 work: `rotate_to_sunward` import, signature
with `sun_position`, magnetosphere rotation with `magnetic_tilt_deg=11`,
bow shock rotation. D2's Snippet 3c had been correctly applied to
Earth on May 21. D2's testing protocol confirmed correct behavior
(bow shock facing Sun, magnetic tilt visible). Earth was not the D2
outlier.

### What actually happened

A codebase audit on May 23 PM3 against the D2 and D3.1 manifests
found that **Earth in `/mnt/project/` was missing both D2 work AND
D3.1 work, while every other file was in expected state.**

| File | D2 expected | D2 in `/mnt/project/` | D3.1 in `/mnt/project/` |
|------|:---:|:---:|:---:|
| mercury_visualization_shells.py | yes | PRESENT | PRESENT |
| venus_visualization_shells.py | yes | PRESENT | PRESENT |
| **earth_visualization_shells.py** | **yes** | **MISSING** | **MISSING** |
| mars_visualization_shells.py | yes | PRESENT | PRESENT |
| jupiter_visualization_shells.py | yes (tilt=10) | PRESENT | PRESENT |
| saturn_visualization_shells.py | yes | PRESENT | PRESENT |
| neptune_visualization_shells.py | yes | PRESENT | PRESENT |
| moon, uranus, pluto, eris, planet9, asteroid_belt, comet, solar | no D2 | n/a | PRESENT |
| shell_configs.py | 8 flags | PRESENT | n/a |
| shared_utilities.py | complete rewrite | PRESENT | n/a |
| planet_visualization.py | snippets 2a-2f | PRESENT | n/a |
| orrery_rendering.py | rotate_to_sunward signature | PRESENT | n/a |
| palomas_orrery.py | snippets 4a/4c-4g | PRESENT | n/a |

**Single-file regression, not endemic.** Mercury's audit shows D3.1
was correctly applied to a post-D2 base. Only Earth's base in the
May 22 D3.1 sweep session was pre-D2, producing an output that was
unchanged (because the patcher's anchors didn't match a pre-D2 file)
and silently overwriting Tony's then-current post-D2 working copy.
Tony unknowingly accepted that empty-effect output.

### Reconstruction

Tony uploaded his archived working copy (D2 intact, D3.1 missing).
A D3.1 patcher tuned to that base applied the 15 Batch 4 + Batch 5
edits transactionally with anchored byte-level replacements. Each
edit asserted exactly one occurrence before applying.

**Verification of reconstructed Earth:**

| Check | Result |
|-------|--------|
| `py_compile` | PASS |
| Module import | PASS |
| `rotate_to_sunward` import preserved | PASS |
| `magnetic_tilt_deg=11` preserved | PASS |
| `sun_position` in magnetosphere signature | PASS |
| 2 `rotate_to_sunward` calls with `sun_position=sun_position` | PASS |
| Dispatch-style call (the call pattern that crashed) | PASS, returns 8 traces |
| 13 D3.1 Rule 2 prepends present | PASS |
| Per-body smoke test | PASS (0 real failures) |
| Dispatch smoke test | PASS (0 failures) |
| Live working file matches reconstructed output (byte-identical) | PASS |

**Item 62 is therefore closed/removed.** Earth's magnetosphere
rotation already works -- it was never absent from D2, only from the
stale base D3.1 was applied against.

### Smoke test methodology improvement (kept from v7)

While the v7 Earth diagnosis was wrong, the smoke test improvement
prompted by the crash is real and remains valuable.
`d3_1_dispatch_smoke.py` now walks `CUSTOM_SHELLS` in addition to
`SHELL_CONFIGS`, lazy-imports each builder, and calls it the same
way `create_celestial_body_visualization` does (with or without
`sun_position` keyword per the `needs_sun_position` flag). 24 custom-
shell builders across 9 bodies are exercised. The same crash would
be caught by this smoke test before reaching Mode 5.

**Coverage after this session:**

| Smoke test | Pairs exercised | Result |
|------------|-----------------|--------|
| Per-body builder smoke (original) | 355 traces | 0 real failures |
| Dispatch sphere-shell walk | 83 (body, shell) pairs | 0 failures |
| Dispatch custom-shell walk (added PM2) | 24 builders | 0 failures |
| Sun direction indicator | 1 | PASS |

---

## Codebase Audit (new in v8)

Triggered by Tony's question: "we can't continue testing thinking
each file could be stale." A scripted audit (`audit_d2_d3_1.py`)
cross-checked every file the D2 and D3.1 manifests claim was touched
against the live state in `/mnt/project/`.

**Outcome: Earth was the only regressed file.**

The drift mechanism is now understood:
- The May 22 D3.1 sweep session worked from a `/mnt/project/`
  snapshot that contained a pre-D2 Earth (somehow lost or never
  uploaded post-D2). The other 6 D2 files in that snapshot were
  post-D2.
- The D3.1 patcher's anchors didn't match a pre-D2 Earth (different
  hover_text shape, different builder structure), so the patcher
  produced effectively-no-op output for Earth.
- Tony accepted the output without comparing against his post-D2
  working copy. The post-D2 Earth was silently overwritten.
- All other files received their D3.1 edits cleanly.

This is the v3.23 protocol's "Verify Base Against Handoff" [CRITICAL]
check in action -- the check that, when skipped, produces exactly
this failure mode. The protocol predicted this. We hit it anyway,
on one file out of 20.

**Live working repo state (verified May 23 PM3):**

| File | Status |
|------|--------|
| earth_visualization_shells.py | Reconstructed; D2 + D3.1 + Rule 2 prepends all present |
| mercury_visualization_shells.py | Correct (pre-existing); has Tony's recent prose edits |
| shared_utilities.py | Has dispatch-path Rule 2 fix applied today |
| orrery_rendering.py | Has dispatch-path Rule 2 fix applied today |
| Other 13 per-body files | Correct, unchanged today |
| Other infrastructure files | Correct, unchanged today |

**Tony's repo is ready for Mode 5 in a new session.**

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
| 4 | Dispatch-path smoke test passes (sphere + custom shells) | Done (May 23 PM2) |
| 5 | `orrery_rendering.py` + `shared_utilities.py` compile clean | Done |
| 6 | xvfb GUI launch | Done |
| 7 | Module docstring credits on all touched files | Done |
| 8 | **Codebase audit vs D2 + D3.1 manifests** | **Done (May 23 PM3)** |
| 9 | **Earth reconstructed from archive + D3.1 patcher** | **Done (May 23 PM3)** |
| 10 | Mode 5 visual verification (8-render protocol v3) | **Pending -- Tony, in new session** |
| 11 | Run provenance scanner on touched files | Pending |
| 12 | Update Module Atlas (`module_atlas.py`) | Pending |
| 13 | Deploy to GitHub | Pending (after Mode 5 pass) |
| 14 | Write D3.1 closeout summary | Pending |

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

### From Earth magnetosphere signature fix attempt (May 23 PM2)

**[QUALITY] -- The smoke test methodology improvement was real.**
Both smoke tests called every shell builder with no args -- which
works because all parameters have defaults. But the actual dispatch
in `create_celestial_body_visualization` calls custom-shell builders
with `builder(center_position, sun_position=sun_position)` -- a
keyword call that exposes the signature contract.

A smoke test that exercises only one call pattern can pass while
production crashes on another. The improved `d3_1_dispatch_smoke.py`
walks `CUSTOM_SHELLS` and honors `needs_sun_position` -- matching
the dispatch's keyword pattern. The methodology lesson stands even
though the underlying Earth diagnosis turned out wrong.

**[NOTE] -- The v7 "latent D2 bug" diagnosis was incorrect.** v7
treated Earth's missing `sun_position` parameter as a D2 contract
violation that survived testing. v8 (after Tony's archived working
copy revealed full D2 work) shows the actual diagnosis: Earth was
silently regressed between May 21 (D2 applied) and May 22 (D3.1
sweep ran against a stale pre-D2 base). Item 62, added in v7 to
track Earth's "missing rotation," is therefore closed -- Earth's
rotation work was never absent from D2, only from the corrupted
intermediate state.

### From codebase audit (May 23 PM3)

**[CRITICAL] -- The "Verify Base Against Handoff" check is
load-bearing.** The v3.23 protocol marks this check [CRITICAL] for
multi-session files: confirm the handoff's features exist in the
base file before building. If they don't, stop and flag. We did not
run this check on Earth on May 22. The result: D3.1 ran on a stale
pre-D2 Earth, produced a no-op output, and silently overwrote
Tony's post-D2 working copy. The protocol literally predicted this
failure mode. Skipping the check is what made it happen.

The check is cheap (one grep against the prior handoff). The
failure mode is expensive (today's whole session). Cost asymmetry
this stark means the check should be automatic, not optional. For
future multi-session files: a pre-flight script that takes the
prior handoff's "features that should exist" list and greps each
one against the candidate base. Refuse to proceed on miss.

**[QUALITY] -- A codebase audit answers questions that visual
testing cannot.** When Tony asked "we can't continue testing
thinking each file could be stale," the right response was a
scripted audit (`audit_d2_d3_1.py`) that cross-checks every file
the manifests claim was touched against the live state. The audit
ran in seconds and produced a 20-row table proving Earth was the
only regression. Without the audit, the question would have
required testing every body's every shell with every parameter
combination -- an infinite set. The audit reduced infinite
uncertainty to one specific finding.

**[PRACTICE] -- The drift mechanism is now understood.** The May 22
D3.1 sweep worked from a `/mnt/project/` snapshot that had a
pre-D2 Earth while the other 6 D2 files were post-D2. The patcher's
anchors didn't match pre-D2 Earth, producing an effective no-op.
Tony accepted it without comparison against his post-D2 working
copy. Net effect: post-D2 Earth silently replaced by pre-D2 Earth.
This is what "build on unverified base" looks like in practice --
not dramatic, not loud, just one file silently rolling back several
days while the other 19 files move forward.

**[PRACTICE] -- Tony's eyes won, and we learned why.** The initial
visible symptom (Mercury crust hover missing the header) was the
dispatch-path scope discovery. The next visible symptom (Earth
magnetosphere crash) was the regressed-Earth discovery. Both came
from Mode 5 visual testing catching what every automated check
missed. The lesson is not "visual testing is magic"; it is
"automated checks have scope-blindness baked in, and Mode 5
exercises the actual system without sharing that blindness."

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
  Earth mag sig fix: Anthropic's Claude Opus 4.7 (May 23, 2026 PM2)
  Earth reconstruction
   + codebase audit: Anthropic's Claude Opus 4.7 (May 23, 2026 PM3)
  Integrator:       Tony Quintanilla
  Models involved:  3 (Opus 4.6, Opus 4.7 x6 sessions)
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

*"One file silently rolling back several days while the other 19*
*files move forward -- that's what 'build on unverified base'*
*looks like in practice."*
*-- D3.1 codebase audit lesson, May 23, 2026 PM3*

*"The protocol literally predicted this failure mode. Skipping the*
*check is what made it happen."*
