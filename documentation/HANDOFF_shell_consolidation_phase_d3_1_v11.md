# Shell Consolidation -- Phase D3.1 Handoff (v11, Stage 2 structural sweep)

**Sessions (since v10):**
- May 26, 2026 (one session) -- Stage 2 items 2A through 2C plus
  structural extras and prior-session debt cleanup (Opus 4.7)

**Integrator:** Tony Quintanilla

**Status:** Stage 2's structural sweep is complete. Items 2A, 2B, 2C
verified clean against the live orrery. Three additional structural
items surfaced during the sweep and were closed in-session:
the Mercury sodium tail anti-sunward direction bug (a floating debt
from Phase D Sun Direction work that hadn't been queued), the center
body checkbox shadowing mechanism (a UX bug that was also silently
hiding the body's full hover marker), and the magnetosphere hovertext
overflow on Neptune and Uranus (a missing-`<br>` bug whose symptom was
queued under item 2A but whose root cause was not). Stage 2 item 2D
(three edits in `comet_visualization_shells.py`) is the remaining
work and is scoped for a separate session.

**Next session entry point:** Stage 2 item 2D (MAPS marker symbol +
ghost tail width + post-disintegration hover text clarity).

---

## What changed since v10

v10 closed with D3.1 functionally complete and a six-item queue
deferred to follow-on sessions. This session executed the structural
half of that queue (items 1, 2, 3) and addressed three additional
items that surfaced during the work.

The session also produced two procedural lessons worth carrying
forward, and corrected a misconception about a prior standardization
decision (n_points is 20/25 split by shell type, not uniform 20).

---

## Items closed this session

### 2A -- Hover font size in `create_info_marker`

`orrery_rendering.py`, single edit. Added
`hoverlabel=dict(font=dict(size=11))` to the returned `Scatter3d`.
The change propagates through every info marker in the codebase
because the function is the central factory.

Result: partial fix. The font drop from default 13pt to 11pt is a
~15% reduction in horizontal extent. Helped on most magnetospheres.
Did NOT fully resolve the overflow on Neptune and Uranus -- see 2C.5a
for the root cause that was hiding behind the font symptom.

### 2A.5 -- Mercury sodium tail anti-sunward direction

`mercury_visualization_shells.py` + `shell_configs.py`, two edits.

Same family as the May 25 Sun Direction structural fix. The sodium
tail builder was computing "direction from origin to Mercury" and
treating that as anti-sunward, which is correct only when the Sun is
at the origin (heliocentric view). Broke in barycenter views and
body-centered views with Mercury as center, where the inline fallback
landed at an arbitrary `+x`.

Fix: added `sun_position` parameter, computed direction as
`(center - sun_position)` normalized, added `'needs_sun_position': True`
to the shell_configs dispatch entry so the dispatch loop threads the
actual Sun position through.

This bug was not in any queue. It was floating outside the deferred
list, surfaced when Tony asked "is this deferred?". Closed in-session
to get it off the books. Added to the procedural lessons archive
below as evidence that floating items get lost.

### 2A.7 -- Center body checkbox shadowing removed

`palomas_orrery.py`, four edits (bottom-up).

The UX symptom: when a body was checked AND selected as the center,
the checkbox silently went to 0 and the last-selected body's
checkbox replaced it. The user's intent was discarded with no
warning.

The deeper symptom (discovered during diagnosis): the shadow was
suppressing the body's full hover marker entirely. The position-fetch
loop at line 4263 skips bodies with var=0, so the shadowed center
never landed in the `positions` dict, and `add_celestial_object`
never ran for it. When shells were rendered, the only marker at the
center was the truncated "(center body)" entry from the no-shells
block at lines 4558-4617 -- or nothing at all if shells WERE
rendered, since both gates closed.

Original justification for the shadow was preventing a perceived
duplicate legend entry. But the things being deduplicated convey
different information: the rendered shells show structure, the body
marker carries mass/type/classification info that the shells don't
replicate. Removing the marker has a real information cost, not just
a redundancy elimination.

Fix: removed the shadow mechanism from `on_center_change` and three
orphan `_was_checked` cleanup blocks from the preset wrappers
(`_apply_mission_preset`, comet perihelion preset, comet
disintegration preset). The preset data structures in
`spacecraft_encounters.py` -- which are authored externally via the
gallery editor in a separate repo -- were not touched. Only the
local Tkinter-state wrapper logic in `palomas_orrery.py`.

Known edge case left in place: body checked + body-as-center + no
shells selected produces two markers at origin (one full hover, one
truncated). Same behavior the Sun-checked-as-center case has always
exhibited. Queue for follow-up if it bothers anyone -- it's a small
audit of the no-shells block to skip bodies already in
`selected_objects`. Listed in Stage 3.

### 2B -- Mars Induced Magnetosphere missing info marker

`mars_visualization_shells.py`, single edit. The C1 sweep left a
`TODO` at line 666-670 because `magnetosphere_text` was built and
`magnetosphere_customdata` was set but no `create_info_marker` call
followed. C1 chose not to add it as a "mechanical refactor" to avoid
editorial decisions. The decision was now editorial-trivial (match
Mercury's pattern: `traces.append(create_info_marker(x[0], y[0],
z[0], color, "Mars: Induced Magnetosphere<br><br>...", legendgroup))`)
and the TODO is closed.

### 2C -- Neptune ring/arc markers superimposed

`neptune_visualization_shells.py`, single edit at lines 1620-1625.

Diagnosis: six markers (Adams Ring + five Adams arcs) were collapsing
to a single 3D point. Three coupled root causes:

1. Marker placement used `rotate_points([outer_radius_au], [0.0],
   [0.0], neptune_tilt, 'x')`. Rotation around the X axis of a point
   with y=z=0 is a no-op, so the tilt had no effect on the marker.
2. All five Adams arcs share `outer_radius_km = 62932` -- they're
   arcs of the same ring. Combined with #1, all six collapsed to the
   same body-frame coordinate.
3. The marker bypassed both ring rotations (32 deg around X plus 34
   deg around Z applied at lines 1588-1593), so even rings with
   distinct radii had markers floating off the rendered ring plane.

Fix: anchor the marker at `x_final[0], y_final[0], z_final[0]` --
the first point of the fully-transformed ring/arc geometry. This is
the same pattern Mercury/Mars/Venus magnetospheres use. Complete
rings start at `(inner_radius, 0, 0)` -- distinct per ring because
inner radii differ. Arcs start at `(inner_radius * cos(arc_start),
inner_radius * sin(arc_start), 0)` -- distinct per arc because
`arc_start` differs (-2 deg, 5.75 deg, 11.9 deg, 20 deg, 35.5 deg).
All markers ride with the ring's two-rotation transform, so they
sit in the rendered ring's plane.

Same buggy pattern exists in Saturn (`saturn_visualization_shells.py`
line 1171) and Uranus (`uranus_visualization_shells.py` lines
1061-1062) but with mitigations: Saturn ring radii are all distinct
so markers separate along the +X axis even with the no-op rotation;
Uranus applies a second Y rotation that partially compensates. Both
flagged in Deferred Items below.

### 2C.5a -- Magnetosphere hovertext overflow on Neptune and Uranus

`neptune_visualization_shells.py` + `uranus_visualization_shells.py`,
two edits.

Diagnosis: the Phase C4 work added info marker descriptions to
Neptune's and Uranus's magnetospheres as multi-fragment Python
literal concatenations with NO `<br>` between fragments. Result: one
continuous ~310-322 character string per planet, no line breaks
until the `<br><br>` near the end. Plotly's hoverlabel has no
default max width, so the text extended off the chart.

Fix: appended `<br>` to each fragment's trailing space, matching the
convention used in Mars/Mercury info dictionaries.

This bug was queued as Stage 2 item 1 in v10 but framed as a
font-size issue ("Fixes info-box overflow on Mercury/Venus/Uranus/
Neptune magnetospheres"). The 13->11 font drop in 2A partially
addressed the symptom and could have been treated as Closed. The
root cause -- missing `<br>` tags -- was NOT separately captured
and only surfaced because Tony observed the residual overflow after
2A and pushed deeper. Added to procedural lessons below.

### 2C.5b -- Neptune Magnetic Field Center marker symbol

`neptune_visualization_shells.py`, single edit at lines 609-610.

The magnetic field center is a structural position (like a Lagrange
point), not a celestial body. Was rendering with `symbol='diamond'`
plus an `orange` outline -- convention-violating; diamonds are
reserved for comets. Replaced with `symbol='square-open'` matching
the Lagrange point convention in `celestial_objects.py` and the
apsidal markers in `apsidal_markers.py`. Dropped the `line=dict(...)`
since `square-open` uses `color` for its outline. Bumped size 8->10
because open markers read smaller than filled at the same nominal
size.

Comment block at lines 597-602 updated to reflect the symbol change
and cite the marker convention.

---

## Stage 2 progress

Order from v10 preserved leverage: structural fixes (1, 2, 3) before
content edits (4, 5, 6). Items 4-6 are all in the same file -- handle
together.

| # | Item | File | Status |
|---|------|------|--------|
| 1 | Hover font size in `create_info_marker` | `orrery_rendering.py` | **Done** (partial -- root cause for Neptune/Uranus was 2C.5a) |
| 2 | Mars Induced Magnetosphere missing info marker | `mars_visualization_shells.py` | **Done** |
| 3 | Neptune ring/arc markers superimposed | `neptune_visualization_shells.py` | **Done** |
| -- | Mercury sodium tail anti-sunward direction | `mercury_visualization_shells.py` + `shell_configs.py` | **Done** (was floating, not in queue) |
| -- | Center body checkbox shadowing | `palomas_orrery.py` | **Done** (4 edits) |
| -- | Neptune/Uranus magnetosphere `<br>` overflow | `neptune_visualization_shells.py` + `uranus_visualization_shells.py` | **Done** (root cause of item 1's residual symptom) |
| -- | Neptune Magnetic Field Center symbol | `neptune_visualization_shells.py` | **Done** (convention compliance) |
| 4 | MAPS disintegration marker symbol | `comet_visualization_shells.py` | **Pending** -- next session |
| 5 | MAPS ghost tail width | `comet_visualization_shells.py` | **Pending** -- next session |
| 6 | MAPS post-disintegration hover text clarity | `comet_visualization_shells.py` | **Pending** -- next session |

Edit counts this session: 10 files touched, ~17 edit sites.

---

## Deferred items (existing and new)

### Saturn / Uranus ring marker placement -- same pattern as 2C

Same bug as Neptune 2C: marker placed at `(outer_radius_au, 0, 0)`
then rotated only by axial tilt around X. Rotation is a no-op for
X-axis points, so markers don't ride with the rotated ring plane.

Mitigations that kept these from being flagged:
- Saturn -- ring outer radii are all distinct, so markers separate
  along the +X axis even without proper rotation.
- Uranus -- two rotations applied (X then Y), partially compensating.

Files: `saturn_visualization_shells.py` line 1171,
`uranus_visualization_shells.py` lines 1061-1062.

Fix shape: same as Neptune 2C -- anchor marker at `x_final[0],
y_final[0], z_final[0]` of the rendered ring geometry. Single-line
replacement per file.

Captured: May 26, 2026.

### Center body marker edge case (no shells)

When a body is checked AND selected as center AND no shells are
rendered, two markers appear at origin: one full hover from
`add_celestial_object`, one truncated from the no-shells block at
lines 4558-4617 of `palomas_orrery.py`.

Same behavior the Sun-as-center case has always exhibited. Fixable
with a small audit of the no-shells block to skip when the body is
already in `selected_objects`. Stage 3 candidate.

Captured: May 26, 2026.

### Planet 9 single sphere at n=50

One shell in `planet_9_visualization_shells.py` line 261 uses
`n_points=50` instead of the 20/25 convention. Speculative body,
rarely rendered, minimal impact. Sweep when convenient.

Captured: May 26, 2026.

### Shell Resolution GUI Control

Goal: expose shell sphere resolution as a user-tunable GUI parameter,
likely via a multiplier on existing per-shell n_points values.

**Current state of n_points across the codebase (verified May 26, 2026):**

| Geometry type | Standard | Sparse variant |
|---|---|---|
| Sphere shell (outer: atmospheres, magnetospheres, Hill spheres) | n=20 | -- |
| Sphere shell (inner/solid: cores, mantles, crusts) | n=25 | -- |
| Ring (solid) | n=100 | -- |
| Ring (dusty/gossamer) | n=80 | -- |
| Arc | 10 pts/deg | -- |
| Sparse cloud (solar galactic tide) | n=2000 | -- |

These are intentional, not drift. The 20/25 split was decided
April 14, 2026 in the plotting consolidation handoff. The 100/80
split for rings is consistent across all four ringed planets.

**History:**

- Apr 10, 2025 -- First raised in Jupiter animation file-size
  investigation (333.6 MB problem). Proposed `n_points` 100->60.
- Apr 14, 2026 -- Decision: 20/25 split by shell type. Documented
  in `plotting_consolidation_handoff.md` decision log. Defaults
  landed in code as part of shell consolidation work.
- May 26, 2026 -- Re-raised as a GUI-exposed multiplier idea (not
  new absolute defaults). The multiplier would preserve the
  existing proportional design.

**Adjacent dormant handoff:** `HANDOFF_HTML_EXPORT_MODE.md` (Jan 2026)
-- CDN vs Portable HTML mode. Same file-size concern, different lever.
Could bundle as one GUI panel.

**Design preference (NOT a single multiplier):**

Three quantization regimes exist (spheres, rings, specialty). One
global knob would misapply: a 1.5x multiplier on the cloud (2000 ->
3000) tanks performance with no visible improvement; 0.7x on dusty
rings (80 -> 56) might start showing polygonal artifacts.

Likely shape: 1-2 knobs with named exemptions.
- Knob 1: sphere shell detail multiplier (20/25 baseline)
- Knob 2 (optional): ring detail multiplier (100/80 baseline)
- Exempt: arc resolution (geometric -- pts/deg makes sense),
  sparse cloud (already at upper bound for its purpose)

Not a bug fix. Not a Stage 3 cleanup item. Belongs in its own
feature stage when ready -- could share a session with HTML export
mode (same file-size concern, different lever).

Captured: May 26, 2026.

### Dormant items preserved from v10

- Asteroid belt 4 dead calls (`asteroid_belt_visualization_shells.py`)
  -- Stage 3 cleanup. Delete lines 231, 327, 427, 523. Zero behavior
  change.
- Dormant sphere-shell builder calls (10 sites, 5 files) -- per v9
  Residual Cleanup table. Cosmetic, safe to leave.
- Jupiter & Saturn bow shocks missing geometry -- Stage 4. New
  paraboloid construction in giant-planet radii. Co-toggle design
  decision needed.
- MAPS legend-toggle lag -- Stage 4. Performance investigation,
  likely the 40-segment ghost tail.
- `idealized_orbits.py` line 7331 -- `name 'color' is not defined`.
  Localized fix, caught by surrounding try/except. Behind Stage 2.

---

## Procedural lessons (new in v11)

### [QUALITY] -- Symptom + presumed cause in one queue entry is fragile

When a queue item names both what was observed and what's thought to
be wrong, the fix may resolve the cause without resolving the
observation. The Neptune/Uranus magnetosphere overflow was queued as
v10 Stage 2 item 1 with the framing "Hover font size in
`create_info_marker` -- Fixes info-box overflow on Mercury/Venus/
Uranus/Neptune magnetospheres." The 13->11 font drop helped most
magnetospheres but did not fully resolve Neptune and Uranus. The
real root cause was missing `<br>` tags in two Phase C4 info marker
descriptions, which the queue's diagnosis did not separately
identify.

The partial improvement from the font drop gave plausible cover to
consider the item Closed. Only Tony's post-2A observation that the
overflow persisted led to the deeper diagnosis.

General rule: mark the cause in a queue entry as *hypothesis*, not
as the bug. Verify after the fix that the symptom is actually gone,
not just diminished. If overflow was observed on N planets, hover
over N planets after the fix and confirm. Don't trust "fixed it on
one of them, the rest should work the same."

Captured: May 26, 2026.

### [QUALITY] -- Recurring ideas deserve a queue entry on first mention

The "shell resolution GUI control" idea was discussed in April 2025
(Jupiter animation file-size investigation, ~333 MB) and partially
implemented in April 2026 (the 20/25 split landed in code via the
plotting consolidation work) but the GUI control itself was never
elevated to a deferred-items handoff entry. When Tony re-raised it
in this session as if new, the conversation_search tool found the
April 2025 origin -- but only because the right query was asked.

The cost of capturing a recurring idea on first mention is two lines
of markdown in a handoff. The cost of not capturing it is repeating
the same diagnosis cold, sometimes years later, with no guarantee
that the prior context surfaces.

General rule: if an idea surfaces twice across separated sessions,
that's evidence the conversation alone isn't enough to retain it.
Promote to a handoff deferred-items entry even if no immediate work
is planned. The same rule applies in reverse: if an idea is in a
handoff but keeps coming up "as new," that's evidence the handoff
isn't being read at session start.

Captured: May 26, 2026.

### [PRACTICE] -- Floating items get lost; in-session capture closes them

The Mercury sodium tail anti-sunward bug was a real bug, well
understood, with a fix shape identical to the May 25 Sun Direction
work. But it was not in any queue. Tony asked "is this deferred?"
which surfaced it -- if he hadn't, it would have continued floating.

General rule: when a real bug is observed mid-session, decide
immediately whether to fix it now or queue it explicitly. Treating
it as "we'll get to it" without a queue entry is a quiet way to
lose it. The protocol's "open-ended ideas converge through
conversation" principle is about design exploration, not bug
triage -- bugs need explicit slots.

Captured: May 26, 2026.

---

## Lessons preserved from v10

All v10 lessons remain in force. See v10 for full text:
- [CRITICAL] -- Verify handoff claims before relying on them
- [CRITICAL] -- Look for ALL early-returns above the gate you are opening
- [QUALITY] -- Indentation correctness is invisible until the test runs
- [QUALITY] -- Silent try/except blocks hide bugs in series
- [PRACTICE] -- Three-round fix is fine when each round teaches something new

---

## Misconception corrected this session

The n_points "standardization" was decided April 14, 2026 as a
**20/25 split by shell type**, not uniform n=20. This was documented
in the plotting consolidation handoff decision log but not surfaced
in conversation history easily; the May 26 session began with the
mistaken recollection of uniform n=20, and a codebase grep revealed
the actual 20/25 split was working as designed.

Future-me reading this: the 20 for outer / 25 for inner solid /
100 for solid rings / 80 for dusty rings convention is intentional
and consistent. Don't propose "fixing the mix."

---

## Edit counts (cumulative through v11)

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
| -- | **Stage 2 structural sweep (May 26)** | **~17** | **10** | **Done (v11)** |

---

## Credit (updated through v11)

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
  Stage 2 structural sweep: Anthropic's Claude Opus 4.7 (May 26, 2026)
  Integrator:       Tony Quintanilla
  Models involved:  3 (Opus 4.6, Opus 4.7 x9 sessions)
  Orchestration:    zero frameworks -- Tony carries context between sessions
```

---

*Paloma's Orrery | palomasorrery.com*

*"The framing of a bug determines whether the fix lands or just*
*pacifies the symptom."*
*-- Stage 2 lesson, May 26, 2026 -- on the Neptune magnetosphere*
*overflow that survived its first fix*

*"Floating items get lost. The protocol's 'just ask' is for design,*
*not bug triage. Bugs need slots."*
*-- Stage 2 lesson, May 26, 2026 -- on the Mercury sodium tail*

*"Three Claudes, one Tony, zero orchestration framework."*
*-- Standing convention*

*"The conversation IS where the magic happens."*
*-- Standing convention*
