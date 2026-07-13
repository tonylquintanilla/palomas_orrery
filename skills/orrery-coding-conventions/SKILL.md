---
name: orrery-coding-conventions
description: Coding and visual conventions for the Paloma's Orrery solar system visualization project (palomas_orrery.py, *_visualization_shells.py, SHELL_CONFIGS, plot_objects/animate_objects, planet_visualization*, star_visualization_gui, and companion orrery modules). Use whenever working in the Paloma's Orrery codebase on Plotly traces, markers, hover text, legends, legendgroups, 3D axes, shells, module docstrings, or any new or modified visual element -- even if no convention is named in the request. Covers the marker symbol taxonomy, single info marker pattern, hover-text AU convention, 3D axis dtick/range control, credit lines, module docstring standard, barycenter rule, and the live shell dispatch path. Do not use for projects other than Paloma's Orrery.
fires_when: Markers, hover text, axes, shells, legendgroups, docstrings, new visuals
---

# Orrery Coding Conventions

Skill version: 1.1 | Cut from palomas_orrery @ e83fe9ce | 2026-07-12
Source: project_instructions_v3_29.md Part 3 + Part 5 technical lessons.
Criticality tiers ([CRITICAL]/[QUALITY]/[PRACTICE]) are defined in the
resident protocol, Part 2.

## Marker Symbol Convention [QUALITY]

| Symbol         | Plotly symbol | Used for                                   |
|----------------|---------------|--------------------------------------------|
| Filled circle  | circle        | Major bodies: planets, minor planets, moons |
| Open circle    | circle-open   | Minor bodies: asteroids                     |
| Filled diamond | diamond       | Comets                                      |
| Open diamond   | diamond-open  | Spacecraft                                  |
| Open square    | square-open   | Structural positions: Lagrange points       |
| Cross (+)      | cross         | Non-structural: coordinate ticks, info markers |

Circles are reserved for celestial objects. Cross is for hover information
only. When an existing marker already occupies a position, add hovertext via
customdata instead of adding a second marker.

## Single Info Marker Pattern [QUALITY]

For any visual trace covering area or length -- shells, particle clouds,
multi-segment lines -- separate geometry from interactivity:

- Geometry traces: hoverinfo='skip'. Purely visual.
- ONE info marker: a single cross symbol at a representative, visually
  uncluttered position, carrying the full hover text.

```python
go.Scatter3d(
    x=[0], y=[0], z=[r * 1.05],  # shell: north pole 5% above surface
    mode='markers',
    marker=dict(size=6, color=shell_color, symbol='cross',
                opacity=0.9, line=dict(color='white', width=1)),
    name='', showlegend=False,
    text=[info_hover_string],
    hovertemplate='%{text}<extra></extra>'
)
```

Position choices:
1. North pole at r*1.05 for sphere shells.
2. Named index along a line trace chosen for visual clarity (e.g. segment 10
   on an outbound arc).
3. Any fixed coordinate that is visually uncluttered.

Include the info marker in the geometry's legendgroup so it toggles with it.
Rationale: hover text on every point is N^2 storage and routing spam (the
May 2026 codebase-wide refactor converted 141 inline patterns across 18 files
and saved 9-13 MB per render).

## Hover Text AU Convention [QUALITY]

All distance hover text must include AU alongside km.
Conversion: km / 149597870.7.
Reference points: GEO ~0.000285 AU; Moon ~0.00257 AU; Apophis perigee
~0.000245 AU. AU enables cross-plot comparison. Apply to ALL new hover text
in orrery modules. (This convention is duplicated in the earth-system and
gallery skills for hover work that fires there; the master copy is here.)

## 3D Axis Control Convention [QUALITY]

Close-approach and flyby plots need dtick (tick spacing) and range (axis
extent) overridden -- default AU-scale axes make Earth-neighborhood geometry
(3 orders of magnitude smaller) invisible. Apply to all three scene axes
(x, y, z), in BOTH places:
- Orrery GUI at generation time (auto-range to data extent; auto dtick via
  _calculate_grid_dtick).
- Gallery Studio at refinement time (range min/max + dtick fields, active
  when Show Axes is on).

## Credit Line Convention [PRACTICE]

```python
# Module updated: April 2026 with Anthropic's Claude Sonnet 4.6
```
Place in the module docstring, in a section comment for new entries (e.g.
new spacecraft_encounters.py or celestial_objects.py entries), or in a
design-pattern block comment. Transparent attribution is a partnership
value. Add on any substantive edit.

## Module Docstring Standard [PRACTICE]

Every .py module gets a triple-quoted docstring at the very top:

```python
"""
module_name.py - One-line purpose statement.

2-3 sentences: what problem it solves, what data it works with, what
it produces. Written for Tony six months from now.

Key functions:
    function_name() - what it does (top 3-5 only)

Consumed by: primary consumers

Module updated: [date] with Anthropic's Claude [version]
"""
```
Optional, for modules with real operational risk (unattended
infrastructure, destructive file operations, cache managers) -- an
"Operational gotchas" block at the end of the docstring:

    Operational gotchas:
        KNOWN TRAP: <the one mistake an operator will plausibly make, and
        its consequence>
        NORMAL BUT SCARY: <the one alarming-looking state that is actually
        fine, so nobody "fixes" it>

One line each, only where earned; most modules never need it. (Motivated by
L-114: the config-swap trap and the .prev directory both needed exactly
this warning.)

Tooling: module_atlas.py generates MODULE_ATLAS.md; add_docstrings.py
batch-inserts docstrings. MODULE_ATLAS.md is the prompt artifact -- current
reference for codebase-aware sessions.

## Barycenter Rule

Barycenter visualization only when the barycenter lies outside the primary
body. Mass ratio is the gatekeeper.

## The Live Shell Dispatch (know before editing shells)

Sphere shells render via SHELL_CONFIGS -> build_sphere_shell ->
create_info_marker (the factory). The inline marker dicts in
*_visualization_shells.py are DEAD CODE for sphere shells -- editing them
changes nothing. Custom geometry (magnetospheres, rings, belts) routes via
CUSTOM_SHELLS and DOES use the live inline path. Grep for where a function
is CALLED, not imported, before editing any shell leaf. The resident
protocol's Verify Execution gate is the principle; this is the map.

## Visual Verification Details [QUALITY]

"Runs without errors" != correct. Verify: orbits in the right place, scales
reasonable, the kissing test passes, frames aligned. If it looks wrong,
check reference frames first (see the horizons-orbital-mechanics skill).
The render is the ground truth; Tony's eyes are the gate.

## Field Notes (technical lessons, earned in this codebase)

- Plotly Scatter3d ignores marker border WIDTH (plotly.js #4118) -- the
  contrast lever is FILL color, not border. The 3D symbol palette is only 8:
  circle, circle-open, cross, diamond, diamond-open, square, square-open, x.
- Plotly camera: axis ranges control zoom, not camera distance.
- Plotly 3D annotations go on scene.annotations; 2D on layout.annotations.
- Plotly customdata survives JSON extraction; the _studio flag survives --
  downstream consumers can detect curated plots.
- A swallowed exception in try/except hides render bugs; an undefined
  variable can drop a marker silently for weeks. Check the console for the
  caught-error print.
- Position data flows through 5 parallel pipelines in palomas_orrery.py --
  ALL must be patched. The same bugs appear independently in plot_objects /
  animate_objects and in the gallery pipeline. Map all consumers first.
- Structural fixes scale; data-side fixes don't. A violation in N consumers
  of one producer -> fix the producer (83 sphere-shell pairs brought into
  compliance by 2 edits to the factory). Central factories need explicit
  migration intent: migrate-in-scope, defer-with-tracked-backlog, or
  new-code-only -- never the unstated fourth option.
- Assign, don't hardcode, to stay in the house pattern: define
  color = 'white' once, reference it from both line and marker.
- Fixing an invisible thing surfaces its neighbors. Budget for "now I can
  see it's too close to its neighbors" after any "nothing renders" fix.
- Stacked bugs: fixing one can reveal a second that was invisible before.
- Roche limit is not absolute: tensile strength allows survival inside it.
- Celestial sphere in ecliptic frame: unit vectors rotated from equatorial
  via obliquity about the X axis.
