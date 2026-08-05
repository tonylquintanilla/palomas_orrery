---
name: orrery-coding-conventions
description: Coding and visual conventions for the Paloma's Orrery solar system visualization project (palomas_orrery.py, *_visualization_shells.py, SHELL_CONFIGS, plot_objects/animate_objects, planet_visualization*, star_visualization_gui, and companion orrery modules). Use whenever working in the Paloma's Orrery codebase on Plotly traces, markers, hover text, legends, legendgroups, 3D axes, shells, module docstrings, or any new or modified visual element -- even if no convention is named in the request. Covers the marker symbol taxonomy, single info marker pattern, hover-text AU convention, 3D axis dtick/range control, credit lines, module docstring standard, barycenter rule, and the live shell dispatch path. Do not use for projects other than Paloma's Orrery.
fires_when: Markers, hover text, axes, shells, legendgroups, docstrings, new visuals
---

# Orrery Coding Conventions

Skill version: 1.2 | Cut from palomas_orrery @ 1e60c783 | 2026-08-04
Source: project_instructions_v3_29.md Part 3 + Part 5 technical lessons.
Criticality tiers ([CRITICAL]/[QUALITY]/[PRACTICE]) are defined in the
resident protocol, Part 2.

v1.2 adds the conventions earned in the L-156 Phase 2 Batch 1 cross-check
and the Fable shell-consistency audit (August 3-4, 2026): the
visualization-constant-vs-range convention, the Hill sphere documentation
standard (including the measured per-body state, which does NOT yet match
the intended convention), the canonical `\n` direction for module _info
strings, dual-pipeline detail added to the shell dispatch section, and
layer-chain gap handling. Two field notes added.

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

Dual-pipeline detail, added after the Fable audit (August 2026):

- `shell_configs.py` has TWO sections. `SHELL_CONFIGS` holds sphere shells
  (rendered by `build_sphere_shell`); `CUSTOM_SHELLS` holds custom geometry
  (rendered by lazy-imported builder functions).
- The `tooltip` field in BOTH sections is **dead data** -- 124 entries
  (83 sphere + 41 custom) with no consumer anywhere in the codebase. It
  exists and does not render. Delete-or-wire is an L-181 decision; until
  then keep it in agreement with its live twin, because a migration would
  promote it.
- For sphere shells, `radius_fraction` in `SHELL_CONFIGS` controls the DRAWN
  geometry while `hover_text` describes the physical value. These are two
  independent copies of one fact. When they drift, the shell renders at the
  old size while the hover asserts the new one -- and nothing errors. Batch
  1 corrected text and citations without the constants; the geometry
  follow-up caught six shells drawing the pre-patch physics.
- A fourth copy class hides in the modules themselves: the legacy inline
  builder dicts (`layer_info` / `description`) carry their own values and are
  dead for sphere shells. Mars kept a dead `radius_fraction = 320` there
  while the live config said 324.5 -- what a naive promotion would
  resurrect.

## Visualization Constant vs Range Convention [QUALITY]

Many physical quantities have a RANGE in the literature, not a single value
(Venus troposphere top 60-65 km; Mercury crust 26 +/- 11 km). Three places
have to agree, and each says something different:

- **Code constant:** the best-sourced single value -- the one that came
  through the competitive cross-check.
- **Display text:** state the range, then identify the value the
  visualization uses.
- **`# Source:` comment:** cite the source for the chosen value AND record
  the range and why that value was chosen.

```python
# Source: Sanchez-Lavega 2018 -- troposphere/tropopause top range 60-65 km.
#         Visualization uses 60 km (lower bound, the better-sourced end).
```

The point is that a future cross-check WILL find a different number in a
different paper. When it does, the question is "was 60 chosen, or did it
drift?" -- and the answer has to be readable at the definition site, not
reconstructed from session history.

## Hill Sphere Documentation Standard [QUALITY]

Three separate things: the mass rule, the distance convention, and what to
write down.

**Mass rule.** For barycenter binaries -- Pluto-Charon, Eris-Dysnomia -- use
the SYSTEM mass (combined), because the Hill sphere belongs to the binary,
not the primary alone. For these bodies the JPL-published system mass is
derived from the companion's orbit, so it already IS the system mass; do not
also add the companion separately, and do not silently substitute the
primary's GM. For non-binaries, use the body's JPL-published GM.

**Distance convention -- intended, and NOT yet uniform in the code.** The
intent is perihelion: closest approach to the parent, where the Hill sphere
is smallest, giving the conservative bound. Measured against the coded
`radius_fraction` values at `1e60c783`, the codebase actually splits:

| What the coded rf matches | Bodies |
|---|---|
| perihelion | Venus, Pluto, Eris |
| semi-major axis | Mars, Jupiter, Uranus, Neptune |
| aphelion | Saturn (also the Fable audit's worst finding) |
| no convention within 3% | Mercury (rf 94.4; nearest is semi-major, off 4%) |

The perihelion convention holds for the bodies Batch 1 touched. It is an
aspiration for the rest, not a description of them. **Do not "correct" a
body to perihelion on the strength of this section alone** -- four bodies
would move, and the reconciliation has not been cross-checked. That work
belongs to a Batch 2 cross-check that treats `radius_fraction` as a
first-class claim (see provenance-discipline, Geometry Constants).

**What to write down.** State the extent in Mkm and in body radii in the
display text, and name the convention and its inputs in the `# Source:`
comment:

```python
# Source: Derived from JPL SSD GM values for the Pluto-Charon system
#         (GM_Pluto 869.3 + GM_Charon 106.1 km^3/s^2) at perihelion
#         29.66 AU, via the standard Hill approximation.
#         Result ~5.99 Mkm (0.04 AU) = 5041 Pluto radii.
#         Barycenter binary: system mass is the correct input.
```

Note what that example does NOT do: it does not write the primary's GM
alone and call it the system mass, and it does not use ASCII-unsafe
superscripts. Both are easy to typo into a citation that reads correct.

## Canonical Text Format: `\n`, Not `<br>` [QUALITY]

Module `_info` strings are consumed by the Tk GUI checkbox tooltip, via
`globals()` in `build_shell_checkboxes()` (celestial_objects.py) into
`CreateToolTip`. A `tk.Label` renders text literally, so `<br>` shows up
on screen as the characters `<br>`.

**The canonical form is `\n`.** `<br>` is DERIVED at the Plotly hover
boundary, which is exactly what the reference pattern already does:

```python
'hover_text': neptune_hill_sphere_info.replace('\n', '<br>'),
```

For bodies not yet on the reference pattern, `shell_configs.py` carries its
own inline copy using `<br>` for Plotly. The two copies differ in FORMAT by
design; they must never differ in CONTENT. L-181 removes the duplication.

Migration status at `1e60c783`, verified by runtime object identity:

- **Reference pattern (text linked):** Saturn, Uranus, Neptune, Sun
- **Inline duplicate (text independent):** Mercury, Venus, Moon, Mars,
  Earth, Eris, Pluto, Jupiter, Planet 9 -- plus Asteroid Belt and Comet

One trap: for a body still on `<br>`, the `.replace('\n', '<br>')` in a
reference-pattern config is a NO-OP. It looks like it is working. It starts
working only once the module strings carry `\n`.

## Layer Chain Gap Handling [PRACTICE]

A body's internal layers often do not sum to its radius. Mercury:
2,020 (core) + 331 (mantle) + 26 (crust) = 2,377 km against R = 2,439.7 km,
a 62.7 km shortfall. The gap is unmodelled structure, not an arithmetic
error to be absorbed.

- **Do not silently adjust** any value to close the gap. Each value has its
  own provenance; nudging one to make the sum work destroys that.
- **Flag it in a code comment** at the outermost affected shell.
- **Keep the surface layer at rf 1.0.** It is the surface, whether or not
  the layers beneath tile perfectly.
- **Visual thickness for readability is a Mode 5 decision** for Tony, not a
  patch target.

Watch for the second-order effect: correcting an inner layer changes the
DRAWN thickness of everything outside it. Moving Mercury's mantle from 0.98
to 0.9636 grew the drawn crust from ~48.8 km to ~88.8 km against a stated
26 km -- the correction made the outer layer more stylized, not less. Say so
when it happens; it is a legitimate outcome, but only if it is visible.

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
- The reference pattern links TEXT copies; it does not link geometry to
  text. Saturn is fully migrated and still carried the Fable audit's worst
  finding -- rf 1120 drawing 67.5 Mkm under text claiming 91 Mkm, itself
  internally contradictory ("91 million kilometers (about 151 Saturn
  radii)" is a 10x mismatch in one sentence). Migrating text does not
  protect constants. The single-source-of-truth constant layer (L-181) is
  the structural fix.
- "Defensible number, wrong citation" is the most common cross-check
  failure mode (GPT's framing, August 2026): the value survives a
  reasonableness test, so nobody looks again -- but the cited paper does
  not contain it. Reasonableness is not provenance.
- An anchor that looks unique often is not. Bare `'radius_fraction': 1.0,`
  and `0.98,` repeat across bodies, and Mercury's and Venus's mantle blocks
  are byte-identical through `marker_size`. Pluto's and Neptune's Hill
  spheres both held 4685 by coincidence. Anchor on the nearest UNIQUE text
  (usually the hover string), and let the single-match assertion be the
  thing that catches you.
