# Shell Consolidation -- Phase D3.1 Handoff (v9, Sun Direction follow-up)

**Sessions:**
- May 22, 2026 -- Inventory + Mode 7 review (Opus 4.7 x2)
- May 23, 2026 (AM) -- Sweep implementation (Opus 4.6)
- May 23, 2026 (mid) -- Runtime verification + Earth fix attempt #1 (Opus 4.7)
- May 23, 2026 (PM) -- Dispatch-path scope discovery + structural fix (Opus 4.7)
- May 23, 2026 (PM2) -- Earth magnetosphere signature fix (Opus 4.7)
- May 23, 2026 (PM3) -- Earth reconstructed from Tony's archive base; codebase audit (Opus 4.7)
- **May 25, 2026 -- Mode 5 review + Sun Direction indicator fixes (Opus 4.7)**

**Integrator:** Tony Quintanilla

**Status:** Mode 5 visual testing of the May 23 PM dispatch-path fix surfaced
two cross-cutting structural bugs in the Sun Direction indicator pipeline
that affected every body with custom shells (magnetosphere, rings, radiation
belts, LEO/GEO, plasma torus, FACs). Both bugs were fixed in this session
with three edits to two files: `planet_visualization.py` and
`shared_utilities.py`. All four functional test scenarios pass, plus
backward-compatibility for asteroid belt / comet callers. Mode 5 visual
verification queued for next session.

**Next session entry point:** Tony drops in the two updated files, runs the
focused Sun Direction test protocol (D3.1 Testing Protocol v4). If all
pass, deploy intermediate state to GitHub and proceed to the remaining
six items in this session's queue.

---

## What changed since v8

v8 closed with "Tony's repo is ready for Mode 5 in a new session." The
May 25 session ran that Mode 5. Tony's notes (em-dashed annotations on
the v3 protocol) flagged a recurring pattern: most observations of "Sun
Direction does not trigger" across Mercury, Venus, Earth (Earth-Moon
barycenter), Mars, Jupiter, Saturn, Uranus, and Neptune resolved to
**two structural bugs in the dispatch layer**, not 8+ independent bugs.

A revised A2 scope (consolidation) was executed after a dead-code
analysis showed that the originally planned "strip 25 legacy calls"
sub-task would have touched dormant per-body sphere-shell builders --
protocol-protected as "if it ain't broke, don't fix it" per v8. The
actual fix is purely in the dispatch and the shared helper; the legacy
calls in dormant code are left alone.

The session also produced clarifying lessons about heliocentric
populations (asteroid belt) and the Sun Direction indicator's purpose.

See "Sun Direction Bug Diagnosis and Fix" and "Residual Cleanup" sections
below for full detail.

---

## What changed since v4 (preserved from v8)

[Unchanged from v8 -- the dispatch-path scope discovery and Earth
reconstruction are still the foundation. See v8 for full detail. The
mechanical fix in this session built directly on the May 23 PM
"ONE sun direction indicator per body" architecture.]

---

## Sun Direction Bug Diagnosis and Fix (new in v9)

### The two bugs

**Bug 1 -- Sun Direction indicator suppressed when only custom shells
are selected.**

In `planet_visualization.py` (`create_celestial_body_visualization`),
`outermost_radius_au` only got updated inside the `SHELL_CONFIGS`
branch of the dispatch loop. The `CUSTOM_SHELLS` branch (magnetosphere,
rings, radiation belts, plasma torus, LEO/GEO, FACs, induced
magnetosphere) rendered the traces but never bumped the radius. So
when the user selected only those, `outermost_radius_au` stayed 0, and
the indicator's `if outermost_radius_au > 0:` guard suppressed it
entirely. Affected every body with custom shells.

The irony: magnetosphere shells are explicitly rotated to face the Sun
via `rotate_to_sunward()` (Phase D2 work). They are the shells that
most benefit from a sunward marker. They were the only ones not
getting one.

**Bug 2 -- Multi-body Sun Direction indicators all named "Sun Direction"
with shared legendgroup.**

In `shared_utilities.py`, `legend_name = 'Sun Direction'` was
hardcoded. The function received no body name. So when Earth + Moon
both rendered (barycenter view), both indicators got identical name
and legendgroup -- indistinguishable in the legend, toggled together.
Tony observed this in the Earth-Moon barycenter test.

### The fix (three edits, two files)

**`shared_utilities.py`** -- `create_sun_direction_indicator` signature
extended with `body_name=None` optional kwarg. When provided, the
indicator's legend label and legendgroup are prefixed with the body
name (e.g. `"Earth: Sun Direction"`). Default None preserves the
original `'Sun Direction'` label for callers that don't yet pass
body_name (asteroid belt populations, comet trails).

**`planet_visualization.py`** -- three additions in
`create_celestial_body_visualization`:

1. `custom_rendered = False` flag declared before the dispatch loop.
2. `custom_rendered = True` set when a `CUSTOM_SHELLS` builder runs.
3. Post-loop fallback before the existing `if outermost_radius_au > 0:`
   check:
   ```python
   if outermost_radius_au == 0 and custom_rendered and body_name in CENTER_BODY_RADII:
       body_r_au = CENTER_BODY_RADII[body_name] / KM_PER_AU
       outermost_radius_au = 100.0 * body_r_au
   ```
   The 100x multiplier matches the legacy per-shell call pattern
   (`100 * EARTH_RADIUS_AU` in the dormant
   `create_earth_magnetosphere_shell`).
4. `body_name=body_name` passed to the
   `create_sun_direction_indicator` call.

### Runtime verification

A functional test was run against the live dispatch with four
scenarios + a backward-compat check:

| # | Scenario | Expected | Got |
|---|---|---:|---:|
| 1 | Body-centered, sphere shells | 0 indicators (suppressed at origin) | 0 |
| 2 | Heliocentric, sphere shells | 1 indicator, `'Earth: Sun Direction'` | 1 |
| 3 | Heliocentric, **custom only** (Bug 1) | 1 indicator via fallback | 1 |
| 4 | Earth+Moon barycenter (Bug 2) | 2 distinct body-prefixed indicators | 2 |
| 5 | Backward-compat: no body_name | 1 indicator named `'Sun Direction'` | 1 |

All pass. Scenario 3's fallback produced
`shell_radius = 100 * EARTH_RADIUS_AU = ~0.00426 AU`, which the
indicator function then scaled to `~0.00490 AU` (1.15x) -- visible
relative to a magnetosphere render, scaled to the body. Mode 5 visual
verification queued for next session.

### Why this scope was smaller than the first plan

The first version of A2 included stripping ~25 legacy
`create_sun_direction_indicator` calls across 10 per-body files. A
function-by-function review found all 10 remaining calls (Mercury,
Uranus, Neptune already cleaned by Tony) lived inside dormant
sphere-shell builders (`upper_atmosphere`, `hill_sphere`). Those
builders are no longer on the dispatch path -- protocol-protected as
"if it ain't broke" per the v8 handoff. The calls inside them never
execute. Stripping them would be cosmetic cleanup of dormant code, not
a behavior fix.

The fix as actually applied is purely structural: the dispatch now
correctly produces the Sun Direction indicator in all cases. No
per-body file was touched.

---

## Residual Cleanup (deferred to a separate session)

These items were identified during the Sun Direction diagnosis but are
not behavior bugs. All are cosmetic / dead-code cleanup. Bundle them
into a single sweep when convenient.

### 1. Dormant sphere-shell builder calls (10 sites, 5 files)

Each is a 4-line block (`sun_traces = create_sun_direction_indicator(...)`
+ for loop) inside a `*_upper_atmosphere_shell` or `*_hill_sphere_shell`
function. The function itself is dormant -- the dispatch routes
`upper_atmosphere` and `hill_sphere` through `SHELL_CONFIGS` /
`build_sphere_shell` instead. Calls never fire.

| File | Line | Function |
|------|-----:|----------|
| venus_visualization_shells.py | 497 | create_venus_upper_atmosphere_shell |
| venus_visualization_shells.py | 798 | create_venus_hill_sphere_shell |
| earth_visualization_shells.py | 605 | create_earth_upper_atmosphere_shell |
| earth_visualization_shells.py | 1146 | create_earth_hill_sphere_shell |
| mars_visualization_shells.py | 576 | create_mars_upper_atmosphere_shell |
| mars_visualization_shells.py | 925 | create_mars_hill_sphere_shell |
| jupiter_visualization_shells.py | 509 | create_jupiter_upper_atmosphere_shell |
| jupiter_visualization_shells.py | 826 | create_jupiter_hill_sphere_shell |
| saturn_visualization_shells.py | 592 | create_saturn_upper_atmosphere_shell |
| saturn_visualization_shells.py | 965 | create_saturn_hill_sphere_shell |

Mercury, Uranus, Neptune already cleaned by Tony in prior session work.
Moon was never affected (all shells are sphere shells; no custom
geometry).

### 2. Asteroid belt's 4 dead calls (1 file, 4 sites)

| File | Line | Function |
|------|-----:|----------|
| asteroid_belt_visualization_shells.py | 231 | create_main_asteroid_belt |
| asteroid_belt_visualization_shells.py | 327 | create_hilda_group |
| asteroid_belt_visualization_shells.py | 427 | create_jupiter_trojans_greeks |
| asteroid_belt_visualization_shells.py | 523 | create_jupiter_trojans_trojans |

Tony's framing question -- "do these heliocentric populations even
need a Sun Direction indicator?" -- collapsed the cleanup. All 4 calls
use default `center_position=(0,0,0)`, and `palomas_orrery.py` invokes
them with no override (lines 4534-4543, 6184-6193). Inside the
indicator function, `dist = 0` triggers the suppression branch and
returns `[]`. The 4 calls do nothing every render.

This is the right behavior for heliocentric ring populations -- there
is no single sunward direction from a ring centered on the Sun. The
function's own suppression logic catches the meaningless case. The
cleanup is "delete the dead calls" -- no behavior change.

### 3. Comet calls (1 file, 2 sites)

| File | Line | Function context |
|------|-----:|----------|
| comet_visualization_shells.py | 1523 | (in active comet tail builder) |
| comet_visualization_shells.py | 1949 | (in active comet tail builder) |

These pass a real position (`center_position` for active comet,
`position_au` for general comet), so the indicator fires and produces
a useful sunward marker -- comet tails point away from the Sun, so
the indicator labels the reference direction. **Keep these calls.**

Optional enhancement: pass `body_name=comet_name` to get Bug 2
consistency (e.g. `"3I/ATLAS: Sun Direction"` instead of generic
`"Sun Direction"`). Small follow-up, not a strip.

---

## Mode 5 Note: Double-Header Survey (preserved from v8)

[Unchanged from v8 -- the dispatch-path fix's 14 double-header cases
are still pending content judgment. Per Tony's notes on the v3
testing protocol, this was marked "acceptable" for the cases reviewed
(Mercury, Earth). Final survey deferred until visual re-test confirms
all bodies render cleanly.]

---

## Edit Counts (updated through v9)

| Batch | Scope | Edit sites | Files | Status |
|------:|-------|------------|------:|--------|
| 1 | Solar prefix renames | 27 | 1 | Done |
| 2 | Multi-leader + comet legendgroups | 10 | 2 | Done |
| 3 | Orphan deprecation + Moon Hill Sphere | 2 | 2 | Done |
| 4 | Crust/cloud legendgroup fix | 22 | 11 | Done |
| 5 | Rule 2 prepend + newline normalization | ~807 | 15 | Done |
| -- | Earth runtime-fix supplement (May 23 AM) | 15 | 1 | Done |
| -- | Dispatch-path structural fix (May 23 PM) | 2 | 2 | Done |
| -- | Module docstring credits | 15 | 15 | Done |
| -- | **Sun Direction structural fix (May 25)** | **3** | **2** | **Done** |

The May 25 fix's 3 edits cover every body with custom shells (8+
bodies) plus the multi-body legend distinction issue. Same leverage
pattern as the dispatch-path fix: structural producer edit beats
data-side N-times-N edits.

---

## Artifacts Produced (updated through v9)

| Artifact | Session | Role |
|----------|---------|------|
| `D3_1_INVENTORY.md` | May 22 | Rubric, per-file detail (scope-limited) |
| `D3_1_MODE7_REVIEW.md` | May 22 | Q1-Q6 answers |
| `D3_1_SWEEP_MANIFEST.md` | May 22 | Five-batch edit plan with snippets |
| `D3_1_TESTING_PROTOCOL.md v3` | May 23 PM | Mode 5 verification, dispatch-fix aware |
| `D3_1_TESTING_PROTOCOL.md v4` | **May 25** | **Mode 5 verification, Sun Direction fix aware** |
| `d3_1_runtime_smoke.py` | May 23 mid | Per-body builder smoke test |
| `d3_1_dispatch_smoke.py` | May 23 PM | Dispatch-path smoke test (sphere + custom) |
| `audit_d2_d3_1.py` | May 23 PM3 | Codebase audit vs D2 + D3.1 manifests |
| `apply_d3_1_earth_archive.py` | May 23 PM3 | Transactional patcher for Earth |
| `apply_d3_1_earth.py` | May 23 mid | Transactional patcher (Earth) |
| `inventory_per_legend_entry.csv` | May 22 | 134 rows (scope-limited) |
| `inventory_per_trace.csv` | May 22 | 249 rows (scope-limited) |
| `d3_1_inventory.py` | May 22 | Static-analysis script (scope-limited) |

---

## Post-Sweep Checklist (updated through v9)

| # | Task | Status |
|---|------|--------|
| 1 | All 15 per-body files `py_compile` clean | Done |
| 2 | All 15 per-body files runtime-construct without exceptions | Done |
| 3 | Per-body smoke test passes | Done (1 known false positive) |
| 4 | Dispatch-path smoke test passes (sphere + custom shells) | Done (May 23 PM2) |
| 5 | `orrery_rendering.py` + `shared_utilities.py` compile clean | Done |
| 6 | xvfb GUI launch | Done |
| 7 | Module docstring credits on all touched files | Done |
| 8 | Codebase audit vs D2 + D3.1 manifests | Done (May 23 PM3) |
| 9 | Earth reconstructed from archive + D3.1 patcher | Done (May 23 PM3) |
| 10 | Mode 5 visual verification (8-render protocol v3) | **Done -- May 25 (with corrective findings)** |
| 11 | **Sun Direction structural fixes (Bug 1 + Bug 2)** | **Done -- May 25** |
| 12 | **Sun Direction functional test (4 scenarios + backward-compat)** | **Done -- May 25** |
| 13 | **Sun Direction Mode 5 visual verification (protocol v4)** | **Pending -- next session** |
| 14 | Run provenance scanner on touched files | Pending |
| 15 | Update Module Atlas (`module_atlas.py`) | Pending |
| 16 | Deploy to GitHub | Pending (after Mode 5 v4 pass) |
| 17 | Write D3.1 closeout summary | Pending |

---

## Next session queue (after Mode 5 v4 confirms Sun Direction fixes)

Six items, all from Tony's review of the v3 testing protocol. Order
preserves leverage and dependency reasoning -- structural fixes first,
content edits last.

1. **Hover font size in `create_info_marker`** (`orrery_rendering.py`)
   -- one structural edit to address the info-box overflow Tony
   reported for Mercury, Venus, Uranus, Neptune magnetospheres. Then
   re-test whether Tony's manual Mercury content edit can be reverted
   (keeping consistency with Earth's magnetosphere in
   `info_dictionary.py`).

2. **Mars Induced Magnetosphere missing info marker**
   (`mars_visualization_shells.py`). Pre-existing Step 2 omission
   flagged in C1 handoff. The `magnetosphere_text` is defined but
   never consumed by `create_info_marker`. Tony's eyes caught a known
   TODO.

3. **Neptune ring/arc markers superimposed**
   (`neptune_visualization_shells.py`). All markers placed at
   `[outer_radius_au, 0.0, 0.0]` and rotated by the same
   `neptune_tilt`. Adams ring + 5 arcs stack at one location. Use
   `ring_info['arc_center']` angle when present.

4. **MAPS disintegration marker symbol** `'diamond'` -> `'square-open'`
   (`comet_visualization_shells.py`). Convention: open square for
   structural positions (Lagrange points, event positions). Diamond
   reserved for active comets.

5. **MAPS ghost tail width** 3 -> 5
   (`comet_visualization_shells.py`). Ghost tail not visible against
   the orbital trace; increase line width for contrast.

6. **MAPS post-disintegration hover text clarity**
   (`comet_visualization_shells.py`). The trace `name` already says
   "Trail (Remains)", but the hover text body doesn't reinforce.
   Tony's note: plotted comet on 4/5/26 and it clearly shows comet
   structure except for nucleus; he assumed this is the remains, but
   the hovertext is not clear on this point.

### Deferred beyond next session

- **Jupiter & Saturn bow shocks missing geometry** (and Uranus, Neptune
  to a lesser extent). New paraboloid construction, needs sizing values
  in giant-planet radii. Design choice on co-toggle behavior. Separate
  scoped session.
- **MAPS legend-toggle lag**. Performance investigation; likely the
  40-segment ghost tail. Defer; understand before fixing.
- **Asteroid belt's 4 dead calls + 10 dormant sphere-shell calls**.
  Cosmetic cleanup pass per the Residual Cleanup section. Bundle into
  one sweep.
- **Comet calls Bug 2 enhancement**. Optional: pass `body_name=comet_name`
  to `create_sun_direction_indicator`.

---

## Platform Neutrality (preserved from v6)

[Unchanged from v8.]

---

## Procedural Lessons (updated through v9)

[Lessons from inventory through codebase audit unchanged -- see v8.]

### From Sun Direction structural fix (May 25, 2026)

**[CRITICAL] -- Mode 5 visual testing catches what automated checks
miss, again.** The dispatch-path smoke test (`d3_1_dispatch_smoke.py`)
exercises the dispatch with synthetic shell_vars where multiple shells
are typically active at once. The Sun Direction indicator fires from
the SHELL_CONFIGS path, the smoke test sees an indicator, and reports
PASS. But the user-mode behavior of "select only the magnetosphere
checkbox" was never tested in any automated smoke. Mode 5 caught it
across 8+ bodies. Pattern: smoke tests verify "the wiring is
connected," not "every interaction surface produces the right
behavior."

For future structural fixes that introduce conditional paths (the
`outermost_radius_au > 0` guard): write a smoke test variant that
exercises each conditional path separately. In this case, a smoke
that selected only custom shells (no sphere shells) would have caught
Bug 1 before Mode 5.

**[QUALITY] -- Re-examine your own consolidation work.** The first
version of this session's A2 plan included stripping ~25 legacy
`create_sun_direction_indicator` calls. The grep-based scope was
correct (the calls exist). The dispatch-path assessment was wrong --
the calls are all in dormant builders that don't execute. A
function-by-function review (which function houses each call, is
that function on the active dispatch?) caught the mistake before any
file was touched.

General rule: when a previous session's handoff says "X is dormant /
deprecated / dead code," a subsequent cleanup pass should verify that
claim before acting on its consequences. The v8 handoff was right
about the dormancy; the first A2 draft acted as if it could be
ignored. It can't -- the dormancy classification IS the relevant
information.

**[QUALITY] -- "It already does the right thing by accident."** The
asteroid belt's 4 `create_sun_direction_indicator` calls return `[]`
every render because `center_position` defaults to `(0,0,0)` and
`sun_position` defaults to `(0,0,0)`, triggering the function's own
`if dist < 1e-10: return []` suppression. The code looks like it does
something; it does not. The cleanup is "delete the dead calls" with
no behavior change. Recognizing this pattern -- code that is
wrong-looking but right-behaving -- saves a refactor.

**[PRACTICE] -- The framing question collapses the scope.** Tony's
question "do these heliocentric populations even need a Sun Direction
indicator?" reframed the entire asteroid belt sub-task. From
"consolidate 4 indicators or rename them" to "delete the 4 dead
calls; the answer was no all along." The Sun Direction indicator is
specifically about labeling the sunward direction from a body. For a
ring of objects centered on the Sun, there is no single sunward
direction -- the indicator is undefined. The framing question made
this obvious.

General rule: when scope feels disproportionate to the bug, ask
whether the framing is right before executing. The cleanup wasn't
small because the problem was complex; the cleanup was small because
the problem didn't exist.

**[PRACTICE] -- Pre-test functional testing on structural fixes.**
A 4-scenario test against the live dispatch (body-centered, helio
sphere, helio custom only, multi-body barycenter) plus a
backward-compat check (no body_name) caught no bugs but provided
confidence to deliver as snippets. Worth the ~10 minutes on edits
this small because the alternative is finding the issue in Mode 5
across multiple renders.

---

## Credit (updated through v9)

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
  Mode 5 review
   + Sun Direction fix: Anthropic's Claude Opus 4.7 (May 25, 2026)
  Integrator:       Tony Quintanilla
  Models involved:  3 (Opus 4.6, Opus 4.7 x7 sessions)
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

*"The framing question collapses the scope. Do these heliocentric*
*populations even need a Sun Direction indicator?"*
*-- Tony, May 25, 2026*

*"It already does the right thing by accident. Recognizing*
*wrong-looking-but-right-behaving code saves a refactor."*
*-- D3.1 Sun Direction lesson, May 25, 2026*
