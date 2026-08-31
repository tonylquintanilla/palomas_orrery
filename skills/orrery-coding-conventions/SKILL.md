---
name: orrery-coding-conventions
description: Coding and visual conventions for the Paloma's Orrery solar system visualization project (palomas_orrery.py, *_visualization_shells.py, SHELL_CONFIGS, plot_objects/animate_objects, planet_visualization*, star_visualization_gui, and companion orrery modules). Use whenever working in the Paloma's Orrery codebase on Plotly traces, markers, hover text, legends, legendgroups, 3D axes, shells, module docstrings, or any new or modified visual element -- even if no convention is named in the request. Covers the marker symbol taxonomy, single info marker pattern, hover-text AU convention, 3D axis dtick/range control, credit lines, module docstring standard, barycenter rule, and the live shell dispatch path. Do not use for projects other than Paloma's Orrery.
fires_when: Markers, hover text, axes, shells, legendgroups, docstrings, new visuals
---

# Orrery Coding Conventions

Skill version: 1.7 | Cut from palomas_orrery @ 04bba3ca (v1.7),
earlier @ 3faa72a0 (v1.6),
earlier @ 15741822 (v1.5), 86f529a (v1.4), 3398970 (v1.3) | 2026-08-26
v1.6 (L-249) makes the angular step in Marker Separation for
Near-Equal Radii an OUTCOME rather than a fixed 20 degrees, with 20 and
10 recorded as the two worked cases. Earned when Earth's upper mantle
moved to its sourced radius and its cross vanished under the crust's.
Source: project_instructions_v3_29.md Part 3 + Part 5 technical lessons.
v1.4 adds Marker Separation for Near-Equal Radii to the Single Info
Marker Pattern, earned when the chromosphere moved to true scale and its
marker landed one pixel from the photosphere's; and Harvest the
Conventions You Find, which is how this skill grows.
v1.5 (L-227) adds Hover Line Width Is a Convention, Not an Accident,
found by Mode 5 when a tooltip ran off the viewport: a hover string had
been wrapped at 72 characters in the SOURCE with no `<br>` on the
lines, and rendered as one 378-character run. Canonical Text Format
already governed `\n` versus `<br>` and said nothing about width.
Criticality tiers ([CRITICAL]/[QUALITY]/[PRACTICE]) are defined in the
resident protocol, Part 2.

v1.2 adds the conventions earned in the L-156 Phase 2 Batch 1 cross-check
and the Fable shell-consistency audit (August 3-4, 2026): the
visualization-constant-vs-range convention, the Hill sphere documentation
standard (including the measured per-body state, which does NOT yet match
the intended convention), the canonical `\n` direction for module _info
strings, dual-pipeline detail added to the shell dispatch section, and
layer-chain gap handling. Two field notes added.

## Harvest the Conventions You Find [PRACTICE]

This skill holds the conventions somebody wrote down. The codebase holds
many more, and they live where they were invented -- a comment above one
function, a docstring paragraph, a pattern repeated across four modules
that nobody ever named. A convention that exists only in the file that
uses it is invisible to the next session, which will either reinvent it
differently or break it without knowing it was there.

**So when you touch a file and find a convention that is not in this
skill, say so.** Report it in the same message as the work. Do not
silently follow it -- following it without naming it is exactly how it
stays invisible for another six months.

Promote it here when all three hold:
- it applies beyond the file it was found in;
- it was a decision, not an accident of how that file happened to get
  written;
- a future session would get it wrong without it.

Report it even when they do not all hold. The judgment about promotion is
Tony's, not the finder's, and a convention named and declined costs one
line. One left unnamed costs a rediscovery.

What this looks like in practice: "while editing X I noticed every shell
module does Y -- that is not in the conventions skill. Worth adding?"
That is the whole obligation. It does not require stopping the work or
opening a ledger item.

(Tony's ruling, 2026-08-16: "there are many unrecorded conventions except
in local files." The same day, this skill's own v1.4 was delivered with
its version block deleted by an insert that was written as a replace --
see Field Notes.)

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

### Marker Separation for Near-Equal Radii [QUALITY]

The position choices above assume shells are separated by their radii.
Where two shells sit within about 10% of each other, r*1.05 puts both
markers in the same place and Plotly shows one where the user expects
two. The geometry is correct, the legend is correct, and the affordance
silently does not exist -- nothing errors and nothing renders wrong.

**Rule: the inner shell keeps the north pole. Each subsequent shell in
the stack steps in polar angle along the +x meridian, at its own
radius.** Separate angularly, never radially -- moving a marker off its
own shell's radius detaches it from the thing it labels.

**HOW FAR is an outcome, not a number: far enough to read as two markers
at the scale the family actually renders at.** The step needed depends
on frame width, and frame width depends on which shells the user has
enabled -- Earth's interior alone frames at about 1 R, but switch the
magnetosphere on and the same step collapses to nothing. Two worked
cases:

- **20 degrees, the solar skin stack.** Renders across a 0-3 R_sun view,
  so the markers land 0.365 R_sun apart, about 12% of the frame.
- **10 degrees, Earth's crust against the upper mantle.** Interior-only
  view, so 10 degrees puts them 0.183 R apart -- roughly 1,165 km, 8-9%
  of the frame, up from 33 km.

Declare it per shell with `'info_polar_deg'` in `SHELL_CONFIGS`;
`build_sphere_shell()` reads it and places the marker at
`r*1.05` stepped by that polar angle. Absent or zero reproduces the pole
exactly, so adding the key to one shell moves nothing else. It is a
DECLARED drawing parameter under L-240 and stays in `shell_configs.py`,
never in `constants_new.py`.

(Tony's ruling 2026-08-26, and his Mode 5 call on which shell moves:
the CRUST, because it is the odd layer visually -- the only mesh3d
surface in the interior stack. The standing rule would have moved it
too, being the outer of the pair. Rule and eye agreed.)

```python
info_polar_deg = 20.0                       # 0 for the innermost
r_info = r_shell * 1.05
info_x = r_info * math.sin(math.radians(info_polar_deg))
info_z = r_info * math.cos(math.radians(info_polar_deg))
# marker at (info_x, 0, info_z)
```

Worked case, the solar skin stack. The photosphere's marker sits at
1.050 solar radii. At the retired drawn radius of 1.1 the chromosphere's
sat at 1.155, comfortably clear. At true scale (1.002875) it lands at
1.053 -- 0.003 apart, about one pixel on a 0-3 R_sun view. Stepped 20
degrees it sits 0.365 solar radii away and reads as a separate marker at
every scale the shell family renders at.

**This is not the ring-marker fix.** Saturn's ring markers once collapsed
to a single X position and were separated in May 2026 by placing each on
its own already-rotated trace -- radial separation, which works because
ring radii differ by a lot. That approach cannot help at 0.29%, and
reaching for it here is the trap. Different mechanism, different trigger.

**The trigger is measurable, so measure it.** Two shells within 10% is
the test, not "looks close." A shell whose radius is a derived constant
can move without anyone editing the marker code.

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

## Barycenter Rule [QUALITY]

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
is smallest, giving the conservative bound. Re-measured 2026-08-05 with the
Mars Hill correction applied (L-182; pushed SHA recorded there), reporting
the deviation rather than a bucket -- a loose tolerance is what let Mars's
unsourceable 324.5 read as "semi-major" for a version:

| Body | coded rf | nearest convention | deviation |
|---|---|---|---|
| Venus | 166 | perihelion | +0.03% |
| Mars | 319.2 | semi-major | +0.00% |
| Neptune | 4685 | semi-major | -0.03% |
| Pluto | 5041 | perihelion | +0.15% |
| Jupiter | 740 | semi-major | -0.45% |
| Uranus | 2770 | semi-major | +1.01% |
| Eris | 6965 | perihelion | +1.39% |
| Saturn | 1120 | aphelion | -1.73% |
| **Mercury** | **94.4** | **none** | **+4.37% vs semi-major** |

Read the deviation column, not just the label. Anything past ~0.5% is a
near-miss, not a match: Saturn, Uranus and Eris sit far enough out that
their labels are descriptive convenience, and Mercury's rf 94.4 matches no
convention at all (perihelion 71.9, semi-major 90.5, aphelion 109.1) while
its `# Source:` comment asserts the perihelion convention -- an open
SOURCE_VS_VALUE conflict awaiting Batch 2.

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

## Hover Line Width Is a Convention, Not an Accident [QUALITY]

Companion to the section above, which governs WHICH break character to
use and says nothing about how often. This governs how often.

**Every source line of a hover string carries its own break.** In this
codebase the source wrap and the rendered wrap are ONE ACT, not two.
The existing strings are built that way -- `streamer_belt_info`,
`roche_limit_info`, `alfven_surface_info_hover` -- and their rendered
lines land between about 60 and 98 characters because their source
lines do.

**The failure mode is that correct-looking source produces broken
output.** Python's implicit string concatenation invites wrapping a
long literal across several source lines for readability. Do that
without a break on each line and the pieces concatenate into one run.
The diff looks tidy, the file looks tidy, and the tooltip runs off the
screen. Paragraph-level `<br><br>` does not save it: a paragraph is
still a single line.

```python
# WRONG -- renders as one 378-character line
"OPEN STALK -- above the pinch. A thin sheet along the current "
"sheet. It has NO outer edge: it thins into the slow solar wind, "

# RIGHT -- source wrap and rendered wrap are the same act
"OPEN STALK -- above the pinch. A thin sheet along the current<br>"
"sheet. It has NO outer edge: it thins into the slow solar wind,<br>"
```

Two details that follow from it. Put the break where the trailing
space was rather than after it -- the break IS the separator, so a
space before it renders as a stray one. And do not let a break fall
between a number and its unit: `at {cusp_rs:.1f} R_sun<br>` reads,
`at {cusp_rs:.1f}<br>R_sun` does not.

**Checking it is one line, and worth running after any hover edit:**

```python
max(len(s) for s in rendered_hover.split('<br>'))   # want <= ~98
```

Re-flowing an existing string is a BREAKS-ONLY edit. Prove it rather
than assert it: strip every `<br>`, collapse runs of whitespace, and
compare old against new. They must be byte-identical. A re-flow that
quietly reworded something is indistinguishable from one that did not,
unless the comparison runs.

(Origin, 2026-08-23, L-227. Tony hovered the streamer band during the
Mode 5 pass on L-224 and the tooltip ran off the viewport. The string
had been wrapped at 72 characters in the source with breaks only
between paragraphs; `streamer_belt_info`, forty lines up in the same
file, was correct. Nothing catches this but a person hovering it --
no checker reads rendered hover width, and the module compiles and
the trace builds either way. Tony's ruling, on adding it here: this
recurs from time to time rather than constantly, which is precisely
the kind of thing a person forgets and a written convention does not.)

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
- Position data reaches a viewer through FIVE parallel CONSUMERS, and a
  fix in one does not propagate. Map ALL of them first. Named here rather
  than counted, because a count does not say what it counted (L-269):
    static plot        plot_objects              palomas_orrery.py
    animation          animate_objects           palomas_orrery.py
    social export      export_social_view        palomas_orrery.py
    gallery curation   tools/gallery_studio.py   GALLERY repo
    JSON conversion    tools/json_converter.py   GALLERY repo
  TWO OF THE FIVE ARE IN THE OTHER REPOSITORY. Grep one repo and you find
  three. The old wording said "5 parallel pipelines in palomas_orrery.py",
  which put a cross-file count inside a single-file scope and hid them.
- FETCHING is a different question with a different answer. Six functions
  in palomas_orrery.py acquire position data -- resolve_shell_sun_position,
  update_orbit_paths, plot_actual_orbits, plot_objects, animate_objects,
  open_orbital_param_visualization -- across fetch_position,
  fetch_trajectory, fetch_orbit_path and orbit_data_manager, with
  plot_objects alone holding three near-identical branches. Three of the
  five consumers above fetch nothing; they render what was already
  fetched. Do not substitute one list for the other.
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
