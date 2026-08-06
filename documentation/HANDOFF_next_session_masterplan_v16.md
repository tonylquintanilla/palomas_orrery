# Opus Session Handoff -- Master Plan v16, L-176, Batch Closure

**Built on `2becfbfdcdb5c110eac84ea6edc34abcc793de92`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Verify HEAD matches before building; if it does not, trace the delta first.**

**Prepared:** August 5, 2026 by Claude Opus 5 (orchestration), Tony Quintanilla integrator
**Closes:** the Fable skills-layer review cycle and the L-156 geometry follow-up

---

## Who you are working for

Tony Quintanilla, PE -- a retired civil and environmental engineer, artist,
and anthropologist. He is not a professional programmer and not a formally
trained astronomer. He builds Paloma's Orrery through conversational AI
collaboration and holds sole commit authority and final judgment. The
codebase's structure and discipline are the product of iterative
collaboration with Claude, not something Tony wrote unassisted -- read code
quality as evidence of the partnership.

He runs Python by opening a file in VS Code and clicking Run, and works
through GitHub Desktop. As of protocol v3.34 that is a **preference where
practical, not a prohibition** -- a terminal step is a fallback, not
forbidden. The standing obligation: don't hand over an operation outside his
known working set without explaining what it does and what could go wrong.

**Deliver runnable transactional patch scripts**, not diffs or complete-file
rewrites. The harness pattern that works: verify every anchor before writing
anything, normalize CRLF and report it, and on any failure print
`NOTHING WAS WRITTEN` explicitly. See `documentation/patch_ledger_closeout.py`
at HEAD for the current shape.

---

## Session start, in this order

1. **SHA round trip.** `git ls-remote` against both repos; pin each
   separately. Gallery is
   `https://github.com/tonylquintanilla/tonyquintanilla.github.io`.
2. **Read the ledger** -- open items, Tony comments, Gap notes.
3. **Master plan update FIRST.** This is Tony's explicit instruction for
   this session. `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md` is at
   **v15**, 1521 lines, last touched at `1e60c78`. It needs a v16 pass
   recording what the August 4-5 cycle actually closed (see below) before
   any new build work starts.
4. Propose approach, wait for go-ahead.

---

## What the August 4-5 cycle closed

Landed and verified at `2becfbf`:

- **Mars Hill sphere corrected to 319.2 R_Mars** across all seven copies,
  module and live config (L-182, DONE). The Aug-1 cross-check had derived
  ~1.084 Mkm but its patch targeted the shell module only; the live
  `shell_configs.py` never received it, and the Aug-4 consistency patch then
  harmonized the module *up* to the wrong value, erasing the correction
  entirely. Mode 5 confirmed the fix.
- **L-178 closed.** Both `EARTH_RADIUS_KM = 6371.0` shadow constants removed
  from `earth_visualization_shells.py`; conversion now goes straight through
  `KM_PER_AU`. GEO belt 42,212 -> 42,165 km; LEO band now renders on its own
  declared 200/2000 km bounds. Note the ledger title says "shadow constants"
  but the affected code is LEO/GEO band geometry -- no umbra involved.
- **Protocol v3.34.** Two amendments: the git-GUI preference ruling, and
  **Stale Skill = Stop [CRITICAL]** -- when a loaded skill's version
  disagrees with the manifest row, the session STOPS and asks Tony to push
  to `skills/` and reinstall in Settings. Do not proceed and mention it
  later; that is the failure the gate exists to prevent.
- **All 10 skills bumped and reconciled** across three stores (repo,
  manifest, account install). `skills_index.py` now prints what the manifest
  was advertising before overwriting it.
- **Ledger appendix** caught up: v3.32, v3.33, v3.34 entries added (it had
  stopped at v3.31).

---

## Task 1: Master plan v16

Record the above. Specific items the plan does not yet reflect:

- Line ~1468 states "Scanner state: Tier 1 207 -> 207 (provenance-neutral)."
  Still true at HEAD -- but see the tier analysis below, which reframes what
  that number means for Artifact 2.
- Line ~917's Phase 2 Track 1 status: Batch 1 COMPLETE, Batch 2 NEXT. Batch 2
  is now the stated gate before Artifact 2 (Tony's instruction: clear all
  batches first).
- L-182 as a new failure class in the plan's lessons: a correction that
  reaches one copy of a two-copy pair is worse than no correction, because
  the next consistency pass will harmonize *toward* the uncorrected copy.
- **The push gate changes in this phase** (Tony ratified August 5, 2026):
  "Tier-1 = 0" becomes "Tier-1 = 0 on the interactive build path." Name the
  path in the plan and record that it is computed, not listed (Task 2). The
  earth-science remainder gets its own L-item and its own schedule.

---

## Task 2: build the interactive-build-path gate

**This is a gate, not backlog. It is built before the batches it scopes.**
Tony's ruling, August 5, 2026, correcting an earlier proposal to open it as
an L-item for later: deferring the definition of a gate is the same error as
deferring the gate.

Two pieces, one cheap and one that needs a design decision.

### 2a. Domain breakdown in the console output (cheap, do first)

`provenance_scanner.py` already computes findings by domain --
`MODULE_DOMAIN_MAP` + `classify_domain()`, six domains, and the report
carries a full **Findings by Domain** table. The console run prints only
tier totals and a `207 TIER-1 FINDINGS -- PUSH GATE NOT MET` banner. Print
the domain split under each tier line:

```
Priority summary:
  Tier 1 (16-20):   207 findings -- FIX NOW
    earth_science     104
    orrery             92
    stars               9
    utilities           1
```

**Fix the coverage gap in the same pass.** The audit's own domain-coverage
note flags `orrery_rendering.py` and `shell_configs.py` as unmapped,
defaulting to `orrery`. Both are on the critical path -- the most important
file in the gate would otherwise land in the pile by accident. Add explicit
`MODULE_DOMAIN_MAP` entries. Also clear the two stale entries pointing at
files no longer in the root (`smoke_dipole_cone`, `smoke_rotation_axis`).

### 2b. The build-path axis (the gate itself)

Domain answers "what part of the project is this." The gate needs "does
this render in the thing being shipped." Those diverge inside `orrery`:
`shell_configs.py` (24 Tier-1, on the path) shares a bucket with
`comet_visualization_shells.py`, `planet9_*` and `sgr_a_*`, which are not.
So the domain split isolates the 104 earth-science findings as off-path --
half the problem -- and leaves the orrery 92 undifferentiated, which is
precisely the half the gate turns on.

**Derive it, do not declare it.** The project already carries two module
maps: `ROLE_MAP` (generated from docstring tags) and `MODULE_DOMAIN_MAP`
(hand-maintained). A third hand-maintained map is a third store that
drifts, and drift between duplicated stores is the failure this whole cycle
kept surfacing. `dep_trace.py` already walks the import graph for a named
module. Build-path membership is computable: define the orrery-side entry
points once, walk imports, tag everything reachable. It self-corrects when
imports change, and there is no list anyone has to remember to update.

**The one real design question, and it is Tony's (decide):** what are the
orrery-side entry points for the interactive build? The assembler lives in
the gallery repo, so the boundary is whatever orrery code feeds the served
cache and the exported artifacts -- candidates include
`tools/gallery_cache_builder.py` and `gallery_studio.py`, but confirm
against the actual Artifact 2 build rather than assuming. Defining two or
three entry points is far less upkeep than tagging 117 modules, and the
decision has to be made anyway to write the gate down at all.

**Output the gate can be checked against:**

```
  Tier 1 on interactive build path:   56   <-- THE GATE
  Tier 1 off path:                   151   (earth_science 104, stars 9, ...)
```

Open an L-item to track it, but the item records work being done now, not
work deferred.

---

## Task 3: L-176 -- illustrated dimensions in shell hover text

Tony wants this next, specifically so he can **verify text against plot
visually** rather than by manual computation.

Current spec (ledger L-176, OPEN, rice 4/3/70/3): add to each shell's hover
text a line of the form *"<shell> illustrated between _ and _ radii, a
thickness of _ km"*, **derived from `radius_fraction` at render time**, never
from a second typed literal.

**Scope boundary, recorded in L-176 this session -- do not oversell the
item.** Illustrated dimensions catch CONSTANT-VS-TEXT drift, which is the
Batch 1 class (Mercury's rf 0.85 drawing 2,074 km under text claiming
2,020 km). They do NOT catch a value that is internally consistent but
unsourced -- Mars's Hill sphere drew exactly the 324.5 R_Mars its text
claimed, and both were wrong. Drift is visible in the render;
wrong-but-consistent needs the provenance cross-check. Complementary
mechanisms, not substitutes.

**Design questions for Tony (decide):**

- Text format, and whether to show the physical value alongside the
  illustrated one for deliberately stylized shells (Mercury's crust draws
  ~88.8 km against a stated 26 km; Venus's draws ~121 km against 10-30 km).
  Both stylizations are flagged in code comments as Mode 5 decisions.
- Whether this ships before, with, or after the L-181 constant layer.
  L-176's own note says "build after L-181 or in parallel."

**Implementation note.** The natural home is `build_sphere_shell` in
`orrery_rendering.py`, which already receives the config dict and the body
radius -- one producer, every sphere shell inherits. Custom geometry
(`CUSTOM_SHELLS`) builds its own traces and would need separate handling.
Resist adding a second typed literal anywhere.

---

## Task 4: clear the batches before Artifact 2

Tony's instruction: **all batches cleared before Artifact 2 (Jupiter/Saturn)
proceeds.** Batch 2 targets the gas giants -- `jupiter_`, `saturn_`,
`uranus_`, `neptune_visualization_shells.py` plus their `shell_configs.py`
blocks.

Known Batch 2 inputs already sitting in the ledger and the Fable audit:

- **Saturn Hill sphere** is the audit's worst finding: `radius_fraction`
  1120 draws ~67.5 Mkm while the text claims 91 Mkm, and the citation is
  internally contradictory ("91 million kilometers (about 151 Saturn radii)"
  -- 91 Mkm is ~1,510 R_S, a 10x mismatch inside one sentence).
- **L-177: Mercury Hill sphere** rf 94.4 matches no convention (perihelion
  71.9, semi-major 90.5, aphelion 109.1) while its `# Source:` asserts the
  perihelion convention. Same shape as the Mars error just fixed. Tony must
  decide the convention.
- **42 remaining `# Verified: April 2026` stamps** -- shell_configs 14,
  earth 13, jupiter 9, comet 6. Retired format; replace with
  `# Cross-checked:` during the batch.
- **Jupiter/Saturn "not yet rendered" false claims** in dead tooltips.
- The Hill sphere convention table in `orrery-coding-conventions` v1.3 now
  reports per-body deviations rather than buckets. Read the deviation
  column: Saturn -1.73%, Uranus +1.01%, Eris +1.39% are near-misses whose
  labels are descriptive convenience only.

**Run the competitive cross-check pattern** (provenance-discipline v1.7,
Review-Repair Protocol): Claude preps the worksheet, Tony sends the same
prompt to GPT and Gemini independently, Claude compares. Do not let one
model review another's output.

**Include the cross-check worksheets in any audit prompt's Materials list.**
This session's Fable audit found the Mars contradiction correctly but
diagnosed its direction backwards, because the worksheets were not given to
it. That omission was the orchestrating Claude's, not Fable's.

---

## Task 5: the scanner tier evidence behind the gate

This is the measurement that produced Task 2. Kept here as the reasoning
trail; the decision is already made.

**Total: 877 findings. Tier 1 = 207, Tier 2 = 580, Tier 3 = 88, Tier 4 = 2.**

**Recommendation: do NOT clear all tiers. Clear a defined critical path.**

**Tier 2 (580) is already adjudicated.** The audit states it directly: all
Tier-2 findings are documented accepted residuals -- cited constants,
V_STALE staleness flags on verified strings, or known scanner limitations.
"No action required unless a new uncited entry appears." `info_dictionary.py`
alone holds 119 of them as multi-line-string false positives. Clearing these
is make-work and would mostly mean writing exceptions entries for things
already understood.

**Tier 3 + 4 (90) are low and lowest priority**, and 36 of the Tier-3 sit in
`dev_tools` -- audit and diagnostic scripts that never render anything.

**Tier 1 (207) is the real gate, but it is not where the plan assumes.**
Half of it is in a subsystem Artifact 2 never touches:

| Cluster | Tier 1 | On the Artifact 2 path? |
|---|---:|---|
| Paleoclimate + Earth scenarios | **104** | No |
| `shell_configs.py` | 24 | **Yes** |
| `idealized_orbits.py` | 26 | **Yes** |
| `planet_visualization_utilities.py` | 4 | **Yes** |
| `saturn_visualization_shells.py` | 1 | **Yes** |
| `orrery_rendering.py` | 1 | **Yes** |
| `jupiter_visualization_shells.py` | **0** | **Yes** |
| Stars domain | 9 | No |
| everything else | ~38 | mixed |

Two things follow, and both are worth saying to Tony plainly:

1. **The gas giant shells are already nearly clean** -- Jupiter 0 Tier-1,
   Saturn 1. Batch 2's job on those files is **value verification**, not
   Tier-1 clearance. Artifact 2 is not blocked by scanner debt in the shells
   themselves.
2. **The Artifact-2 critical path is ~56 Tier-1 findings**, dominated by
   `shell_configs.py` (24) and `idealized_orbits.py` (26). That is a
   tractable, well-defined target -- and `shell_configs.py`'s share will
   shrink as Batch 2 lands.

The 104 paleoclimate/Earth findings are real debt, but they belong to a
dormant subsystem (Fable's Job 1 Gap 2: no active ledger work, no owning
skill section). Deferring them does not endanger the interactive build.

**Tony ratified this on August 5, 2026.** The global "Tier-1 = 0" push gate
becomes **"Tier-1 = 0 on the interactive build path"** for this phase, the
path is named explicitly and computed (Task 2), and the earth-science
remainder gets its own L-item and schedule. A gate nobody can reach stops
functioning as a gate.

Tony's correction to the original proposal, and it is the load-bearing part:
the build-path axis is **not** backlog. It IS the gate, so it gets built
before the batches it scopes -- see Task 2. Deferring the definition of a
gate to an L-item is the same category error as deferring the gate.

---

## Ledger state at this anchor

178 blocks, 110 live items. Open and relevant:

| Item | What |
|---|---|
| **L-176** | Illustrated dimensions in hover text -- Task 2 above |
| **L-177** | Mercury Hill rf 94.4 matches no convention; `# Source:` claims perihelion. Tony decides. |
| **L-179** | Solar gravitational influence: constant 150,000 AU vs citations/display 126,000 AU |
| **L-180** | Solar chromosphere: three inconsistent extents in one shell |
| **L-181** | Single-source-of-truth constant layer -- the structural fix behind most of the above |
| **L-183** | Stars skill (~22-24 modules, largest coverage gap). Tony must decide where `sgr_a_*` and the shared `visualization_2d/3d/core/utils` modules belong. |
| L-124 | Systematic color-accuracy pass (low priority) |

Closed this cycle: L-178, L-182.

---

## Warnings earned this session -- read before building

- **A correction must reach every consumer in the same patch.** L-182's whole
  cause was a patch that fixed the module and missed the config. Enumerate
  consumers before delivering, and state which copy is authoritative *and
  why*, citing the worksheet -- never infer authority from which copy is
  live.
- **A single-match assertion proves uniqueness, not correctness.** A version
  bump anchored on the wrong line printed `ok` and silently replaced
  `resident protocol, Part 2.` Add content guards
  (`assert old.startswith(...)`) alongside the count check.
- **Verify tool behaviour before asserting it.** The orchestrating Claude
  told Tony `skills_index.py` updates both protocol copies. It updates only
  the live `PROJECT_INSTRUCTIONS.md`; versioned copies under `documentation/`
  are archival and the tool never targets them. That wrong claim was then
  written into an audit prompt as "do not report this as a defect."
- **Never edit an archived protocol snapshot.**
  `documentation/project_instructions_v3_*.md` record what each version
  said. Amend the live copy; snapshot separately.
- **Never write with a non-transactional one-liner.** `open(path, 'w')`
  truncates before the write succeeds -- an encoding error then leaves a
  zero-byte file. This happened to this very handoff during preparation.
  Build the content, verify it, then write; or write to a temp path and
  move. The transactional patch harness exists for exactly this reason,
  and it applies to Claude's own deliverables too.
- **The render is the gate.** Every geometry claim in this session was
  smoke-tested against `build_sphere_shell` on the live dispatch and then
  confirmed by Tony's eyes. Compile-clean proves nothing about what draws.

---

*Handoff prepared August 5, 2026 by Claude Opus 5, built on
`2becfbfdcdb5c110eac84ea6edc34abcc793de92` at
https://github.com/tonylquintanilla/palomas_orrery*
