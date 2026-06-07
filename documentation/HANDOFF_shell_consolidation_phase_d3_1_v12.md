# Shell Consolidation -- Phase D3.1 Handoff (v12, Stage 2 closeout)

**Sessions (since v11):**
- May 26, 2026 PM (one session) -- Stage 2 item 2D plus in-session
  expansions surfaced through Mode 5 visual verification (Opus 4.7)

**Integrator:** Tony Quintanilla

**Status:** Stage 2 fully closed. All four batches (2A, 2B, 2C, 2D)
verified. Item 2D opened as three content edits and expanded through
visual testing into seven edits across one file, closing the
deferred Stage 4 "MAPS legend-toggle lag" item as a side effect and
surfacing two new procedural lessons.

**Next session entry point:** Open choice from Stage 3 cleanup
(asteroid belt dead calls, dormant sphere-shell builders, **new**
planetary shell info marker standard sweep) or Stage 4 bigger items
(Jupiter/Saturn bow shocks, `idealized_orbits.py` line 7331).
Recommended: Stage 3 sweep first -- leverage-preserving and the
planetary shell sweep is a natural follow-on to this session's
comet info marker standardization.

---

## What changed since v11

v11 closed with Stage 2 structurally complete except item 2D, which
was scoped as three content edits in `comet_visualization_shells.py`.
This session executed those three edits, then expanded through Mode 5
visual verification: Tony's eyes caught readability issues and bugs
that became four additional edits (one color, one architectural, one
positional, one convention-alignment). The architectural change closed
the Stage 4 "MAPS legend-toggle lag" item that v11 had deferred.

---

## Items closed this session

### 2D.4 -- MAPS disintegration marker symbol

`comet_visualization_shells.py`, lines 552-568. `symbol='diamond'`
-> `symbol='square-open'`, `size` 8 -> 10, `line=dict(color='white',
width=1)` removed. Convention compliance matching the 2C.5b precedent
from the prior session (Neptune Magnetic Field Center marker). The
disintegration is an event location / structural position, not a
celestial body, so the comet-diamond convention doesn't apply.

### 2D.5 -- MAPS ghost tail width

`comet_visualization_shells.py`, line 710. Segment `width` 3 -> 5
for contrast against the underlying perihelion osculating orbit
trace.

### 2D.6 -- MAPS post-disintegration hover text clarity

`comet_visualization_shells.py`, post-disintegration block (lines
1747-1767 before edit). The `tr.name` rename to "(Remains)" was
already in place from a prior session, but the info-trace hover
text header still read "MAPS: Dust Tail" / "MAPS: Ion Tail". Added
a text-replace into the existing rename loops so the header
reinforces the "(Remains)" framing. Scoped narrowly: header
alignment only, body description text unchanged (per scope
question 2 -- the active-tail physics text remains for this unique
case, flagged as a minor departure).

The `customdata` field was investigated as a parallel update site
and confirmed dead-letter: the gallery router at
`gallery_studio.py:1377` unconditionally overwrites trace customdata
with values parsed from `trace.text`, so source-side customdata is
not displayed. Card title comes from the first `<br>`-split segment
of `text` -- which item 2D.6 updates correctly.

### 2D.5b -- MAPS ghost tail color: green -> red (visual surfacing)

`comet_visualization_shells.py`, lines 705 and 725. Tony's eyes
caught that the green ghost tail (matching the disintegration marker
color) was too close to the underlying white osculating orbit trace
to read cleanly. Changed segment color and info marker color from
`rgb(80, 200, 120)` -> `rgb(255, 80, 80)`. Narratively coherent:
green marker = the moment of disintegration; red trail = the
catastrophic aftermath. Disintegration marker itself stays green --
the event vs. aftermath color shift is intentional.

### 2D.5c -- MAPS ghost tail single-trace architecture (closed Stage 4 item)

`comet_visualization_shells.py`, lines 698-718. Previously rendered
as 39 fading line segments (one per opacity step) because Plotly 3D
line color cannot vary along a single trace. Tony observed that the
fade was visually subtle anyway, and the 39-trace count caused
significant legend-toggle lag plus a secondary symptom: clicking the
ghost tail entry during the lag was interpreted by Plotly as a
double-click ("isolate") which hid all sibling traces.

Collapsed to a single `Scatter3d` line trace with constant opacity
0.85 plus the existing info marker = **40 traces -> 2 traces**.
Legend toggle is now instant. Fade visual is lost but was minor; the
solid red trail reads clearly against the dark background.

This closes v11's Stage 4 deferred item "MAPS legend-toggle lag --
Performance investigation, likely the 40-segment ghost tail." Both
the lag root cause and the click-during-lag isolate-misinterpretation
are resolved by the architectural change.

### 2D.B2 -- Dust / Ion tail info marker positions

`comet_visualization_shells.py`, lines 1011 (dust) and 1167 (ion).
The info markers were placed at `tail_points[0]` -- which is
deterministically the comet center, because the particle generator
sets `tail_distance = 0/N * length = 0` and `max_radius = 0` at
index 0. Both info markers were spatially coincident regardless of
randomness, making it impossible to hover them as distinct features.

Fix: offset to `num_particles // 8` (dust, ~12.5% along the curved
tail) and `num_particles // 12` (ion, ~8.3% along the straight
anti-solar tail). Different fractional positions plus the natural
3D divergence (dust curves, ion goes straight) gives clean spatial
separation. Test scenario at full-strength tails: ~459,000 km
between markers, well above pixel-coincidence threshold.

Affects ALL comets, not just MAPS -- the general comet rendering
functions, not the MAPS-specific path.

### 2D.B3 -- Comet info marker red-border standard (5 sites)

`comet_visualization_shells.py`, lines 820 (coma), 1015 (dust),
1171 (ion), 1328 (anti-tail), 1382 (mini-jet). Updated from the
older inline pattern `size=6, opacity=0.9, line=dict(color='white',
width=1)` to the newer central-factory standard `size=8,
opacity=1.0, line=dict(color='red', width=2)`. The red border
provides a unified "this is an info marker" visual signal,
contrasting with each feature's fill color (green, yellow, blue,
tan, purple respectively).

**Ghost tail info marker preserved as documented exception** at
line 720. Its fill color is itself red (matching the trail); red
border on red fill loses contrast. The white border serves the same
hover-affordance function via a different mechanism. Other crosses
get their "info marker" cue from the red outline; the ghost tail
gets it from the trail-color match.

---

## Stage 2 progress (final)

All four batches verified. Stage 2 is closed.

| # | Item | File | Status |
|---|------|------|--------|
| 1 | Hover font size in `create_info_marker` | `orrery_rendering.py` | Done (v11) |
| 2 | Mars Induced Magnetosphere missing info marker | `mars_visualization_shells.py` | Done (v11) |
| 3 | Neptune ring/arc markers superimposed | `neptune_visualization_shells.py` | Done (v11) |
| 4 | MAPS disintegration marker symbol | `comet_visualization_shells.py` | **Done (v12)** |
| 5 | MAPS ghost tail width | `comet_visualization_shells.py` | **Done (v12)** |
| 6 | MAPS post-disintegration hover text clarity | `comet_visualization_shells.py` | **Done (v12)** |
| -- | MAPS ghost tail color green -> red | `comet_visualization_shells.py` | **Done (v12)** (visual surfacing) |
| -- | MAPS ghost tail single-trace architecture | `comet_visualization_shells.py` | **Done (v12)** (closed Stage 4 lag item) |
| -- | Dust/Ion tail info marker offset | `comet_visualization_shells.py` | **Done (v12)** |
| -- | Comet info marker red-border standard (5 sites) | `comet_visualization_shells.py` | **Done (v12)** |

---

## Deferred items (new in v12)

### [NEW] Planetary shell info marker standard sweep

The newer `create_info_marker` standard from `orrery_rendering.py`
(`size=8, opacity=1.0, line=dict(color='red', width=2)`) is used by
magnetospheres and dispatch-managed custom shells. The older inline
pattern (`size=6, opacity=0.9, line=dict(color='white', width=1)`)
persists in planetary interior shell files. The comet info markers
were brought to the new standard this session (5 sites); the
planetary interior shells still lag.

Files needing review (incomplete list from May 26 grep):
- `earth_visualization_shells.py` -- 13 sites
- `mars_visualization_shells.py` -- 7 sites
- `mercury_visualization_shells.py` -- count TBD
- Probably Venus, Jupiter, Saturn, Uranus, Neptune sphere shells

Per-site pattern is identical -- three changes per marker:
- `size` 6 -> 8
- `opacity` 0.9 -> 1.0
- `line=dict(color='white', width=1)` -> `line=dict(color='red', width=2)`

Bulk find/replace per file should work cleanly. Apply the red-on-red
exception rule for any markers whose fill happens to be red --
keep white border in those cases.

Stage 3 candidate. Aesthetic uniformity rather than functional fix;
schedule when there's a natural session window.

Captured: May 26, 2026.

### [NEW] Studio editor comprehensive review

The gallery studio editor pipeline -- info card routing, `_studio`
config patterns, hover_mode interactions, featured trace labels,
fly-to behavior, portrait/mobile layout -- has accreted features
across many sessions without a holistic review. Worth its own
scoped session to audit the routing logic, document the design
patterns, and flag anything that's grown inconsistent.

Triggered by Scenario C of the 2D testing protocol -- the gallery
portrait card test was deferred to this future session rather than
run inline.

Captured: May 26, 2026.

---

## Deferred items (preserved from v11)

### Saturn / Uranus ring marker placement -- same pattern as 2C

Same bug as Neptune 2C: marker placed at `(outer_radius_au, 0, 0)`
then rotated only by axial tilt around X. Saturn and Uranus had
mitigations that hid the bug but not the cause.

Files: `saturn_visualization_shells.py` line 1171,
`uranus_visualization_shells.py` lines 1061-1062. Fix shape: same
as Neptune 2C. Single-line replacement per file.

### Center body marker edge case (no shells)

When a body is checked AND selected as center AND no shells are
rendered, two markers appear at origin (one full hover, one
truncated). Small audit of the no-shells block in
`palomas_orrery.py` lines 4558-4617. Stage 3 candidate.

### Planet 9 single sphere at n=50

One shell in `planet_9_visualization_shells.py` line 261 uses
`n_points=50` instead of the 20/25 convention. Speculative body,
minimal impact. Sweep when convenient.

### Shell Resolution GUI Control

GUI-exposed multiplier on existing per-shell n_points values. Two
knobs (sphere shells, rings) plus named exemptions for arcs and
sparse cloud. Could share a session with HTML export mode (same
file-size concern, different lever). Not a bug; feature stage.

### Asteroid belt 4 dead calls

`asteroid_belt_visualization_shells.py`. Delete lines 231, 327,
427, 523. Zero behavior change.

### Dormant sphere-shell builder calls (10 sites, 5 files)

Per v9 Residual Cleanup table. Cosmetic, safe to leave.

### Jupiter & Saturn bow shocks missing geometry

Stage 4. New paraboloid construction in giant-planet radii.
Co-toggle design decision needed.

### `idealized_orbits.py` line 7331

`name 'color' is not defined`. Localized fix, caught by surrounding
try/except. Behind Stage 2.

### Removed from deferred (closed this session)

- **MAPS legend-toggle lag** -- v11 Stage 4 item, closed by 2D.5c
  (single-trace architecture). Both the lag root cause and the
  click-during-lag isolate-misinterpretation are gone.

---

## Procedural lessons (new in v12)

### [QUALITY] -- Verify universal-propagation claims with grep

Two findings this session traced to the same pattern: a handoff or
mental model said "X applies everywhere" but in fact X only applied
to call sites that touched the relevant central factory.

First instance was already captured in v11 (Neptune/Uranus
magnetosphere overflow surviving item 2A's font-size fix, because
those magnetospheres set their hover text inline rather than
through the central `create_info_marker` factory).

Second instance is this session's discovery that the red-border info
marker standard exists in `create_info_marker` but doesn't propagate
to inline marker dicts throughout the codebase -- specifically, the
planetary interior shell files retain the older white-border inline
pattern.

The shared antipattern: a "central factory exists" claim does not
imply "every call site uses the central factory." When propagation
matters, grep the actual call sites; don't trust the handoff
narrative alone.

General rule: claims of universal coverage in handoff text are
hypotheses, not facts. Verify with `grep -rn "<pattern>" <files>`
when the propagation is load-bearing for the work being done.

Captured: May 26, 2026.

### [PRACTICE] -- Central factories need explicit migration intent

When a central factory is created, three viable paths exist:

1. **Migrate in scope.** The session that creates the factory also
   rewires all existing call sites. Most disciplined; highest
   churn cost.

2. **Defer with tracked backlog entry.** Factory lands; migration
   is captured as a tracked follow-up with a list of call sites
   and an estimated scope. Pragmatic; discipline is in the
   tracking.

3. **Declare new-code-only.** Factory docstring explicitly states
   "for new info markers; existing inline patterns are
   grandfathered until separately migrated." Lightweight;
   everyone knows the rule.

The danger zone is the unstated fourth option: factory exists, no
migration plan, no grandfathering declaration. Just an implicit
"use this from now on" that nobody enforces. The factory gets
quoted as a standard in handoffs but call sites bypass it freely.

The `create_info_marker` factory in `orrery_rendering.py` is
currently in the unstated-fourth-option zone. The Stage 3 sweep
(planetary shell info markers) is the deferred-with-backlog
treatment. Consider also adding a docstring declaration on
`create_info_marker` to prevent new code from adding to the debt
while the sweep waits.

Meta-question to ask BEFORE creating any factory: is this pattern
actually factory-worthy? Long pattern + stable structure + minimal
per-site variation = good factory candidate. Short pattern or
real per-site variation = leaving it inline is fine.

Captured: May 26, 2026.

---

## Lessons preserved from v11

All v11 lessons remain in force. See v11 for full text:
- [QUALITY] -- Symptom + presumed cause in one queue entry is fragile
- [QUALITY] -- Recurring ideas deserve a queue entry on first mention
- [PRACTICE] -- Floating items get lost; in-session capture closes them

And v10 lessons still in force:
- [CRITICAL] -- Verify handoff claims before relying on them
- [CRITICAL] -- Look for ALL early-returns above the gate you are opening
- [QUALITY] -- Indentation correctness is invisible until the test runs
- [QUALITY] -- Silent try/except blocks hide bugs in series
- [PRACTICE] -- Three-round fix is fine when each round teaches something new

---

## Edit counts (cumulative through v12)

| Batch | Scope | Edit sites | Files | Status |
|------:|-------|------------|------:|--------|
| 1 | Solar prefix renames | 27 | 1 | Done (v8) |
| 2 | Multi-leader + comet legendgroups | 10 | 2 | Done (v8) |
| 3 | Orphan deprecation + Moon Hill Sphere | 2 | 2 | Done (v8) |
| 4 | Crust/cloud legendgroup fix | 22 | 11 | Done (v8) |
| 5 | Rule 2 prepend + newline normalization | ~807 | 15 | Done (v8) |
| -- | Earth runtime-fix supplement (May 23 AM) | 15 | 1 | Done (v8) |
| -- | Dispatch-path structural fix (May 23 PM) | 2 | 2 | Done (v8) |
| -- | Module docstring credits | 15 | 15 | Done (v8) |
| -- | Sun Direction structural fix (May 25 AM) | 3 | 2 | Done (v9) |
| -- | Comet Sun Direction follow-through (May 25 PM) | 3 | 1 | Done (v10) |
| -- | Stage 2 structural sweep (May 26 AM) | ~17 | 10 | Done (v11) |
| -- | **Stage 2 item 2D + expansions (May 26 PM)** | **~14** | **1** | **Done (v12)** |

---

## Suggested close-out actions

1. Update the module-level docstring in
   `comet_visualization_shells.py` to append a credit line for
   this session's work. The file already has a multi-line credit
   block at line 21-25; add one more line referencing the v12
   work. Suggested wording:

   ```
   May 26, 2026: Stage 2 item 2D + expansions (Opus 4.7).
       MAPS disintegration marker, ghost tail simplification,
       dust/ion info marker offsets, comet info marker standard.
   ```

2. Regenerate `MODULE_ATLAS.md` to pick up the credit line change
   (cosmetic update only -- no function signatures changed).

3. Deploy to GitHub as the Stage 2 closeout commit. Suggested
   commit message: "Stage 2 closeout (D3.1 v12): MAPS marker
   convention, ghost tail single-trace, comet info marker
   standard."

4. Decide next session's entry point from the deferred items
   list. Recommended: Stage 3 sweep starting with the planetary
   shell info marker standardization (natural follow-on to this
   session's comet info marker work).

---

## Credit (updated through v12)

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
   + Sun Direction fix: Anthropic's Claude Opus 4.7 (May 25, 2026 AM)
  Mode 5 verification
   + comet follow-through: Anthropic's Claude Opus 4.7 (May 25, 2026 PM)
  Stage 2 structural sweep: Anthropic's Claude Opus 4.7 (May 26, 2026 AM)
  Stage 2 item 2D + expansions: Anthropic's Claude Opus 4.7 (May 26, 2026 PM)
  Integrator:       Tony Quintanilla
  Models involved:  3 (Opus 4.6, Opus 4.7 x10 sessions)
  Orchestration:    zero frameworks -- Tony carries context between sessions
```

---

*Paloma's Orrery | palomasorrery.com*

*"The conversation IS where the magic happens."*
*-- Standing convention*

*"Tony's eyes win."* -- still.

*"Factory exists" does not imply "every call site uses the factory.*
*Verify with grep, not with handoff narrative."*
*-- Stage 2 item 2D lesson, May 26, 2026 PM*

*"Three Claudes, one Tony, zero orchestration framework."*
*-- Standing convention*
