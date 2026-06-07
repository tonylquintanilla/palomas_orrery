# MANIFEST: Shell Consolidation Step 3 — Phase B (Moon + Planet 9)

**Project:** Paloma's Orrery | Plotting Consolidation Step 3
**Date:** May 14, 2026
**Source prompt:** `PROMPT_shell_consolidation_for_opus_v2.md`
**Phase A handoff:** `HANDOFF_shell_consolidation_phase_a.md` (May 13-14, 2026)
**Manifest by:** Anthropic's Claude Opus 4.7 (audit)
**For execution by:** Anthropic's Claude Opus 4.6 (implementation) + Tony (integrator)

---

## 1. Phase B Scope and Execution Model

### What Phase B delivers

Two more bodies wired through the unified dispatch established in Phase A.

After Phase B:

- **Moon** renders via `SHELL_CONFIGS['Moon']` (6 sphere shells, including mesh3d crust). No custom geometry.
- **Planet 9** renders via `SHELL_CONFIGS['Planet 9']` (2 sphere shells: mesh3d surface, dot Hill sphere). No custom geometry.
- `moon_visualization_shells.py` and `planet9_visualization_shells.py` become fully dead code paths (their functions are unreachable from the dispatch). Files are NOT modified — they'll be batch-archived in Phase D per the pre-decided policy.
- Moon and Planet 9 blocks in `create_planet_visualization()` are replaced with the one-line delegation pattern established for Mercury in Phase A.
- `shell_configs.py` grows by 8 new configs.

After Phase B, three bodies route through the unified dispatch: Mercury (Phase A), Moon, Planet 9. Eleven bodies (Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto, Eris, Sun, asteroids) still route through `create_planet_visualization()` / `create_sun_visualization()`. The codebase is fully functional at every step boundary.

### What Phase B explicitly does NOT do

- Does NOT modify `moon_visualization_shells.py` or `planet9_visualization_shells.py`. Per Phase B Decision 3 in the handoff, dead shell files are batch-archived in Phase D, not edited per-body. No indicator-call stripping, no dead-function removal, no docstring updates. Leave them alone.
- Does NOT touch Pluto or Eris. Those bodies have satellites (Charon + 4 small moons; Dysnomia) whose internal-structure shells need Horizons-sourced data not yet ready. Their migration is deferred to a later phase.
- Does NOT clean up the `_info` import chain. Moon and Planet 9 `*_info` strings continue to exist in their shell files and continue to be imported by `palomas_orrery.py` via `globals()`. Phase D handles that.
- Does NOT touch `celestial_objects.py` or GUI tooltip wiring. `build_shell_checkboxes('Moon', ...)` and `build_shell_checkboxes('Planet 9', ...)` continue to look up tooltips via `globals()` — those names continue to exist in the shell files.
- Does NOT retire `create_planet_visualization()`. Eleven bodies still need it. Phase D retires it.
- Does NOT touch `shared_utilities.py`. The `create_sun_direction_indicator` rename was reversed in Phase A — the function is back to its original name (the alias is the new `create_vernal_equinox_indicator` name) and the dispatch already calls the canonical name.

### Why this minimal blast radius matters

Phase A proved the pattern on one body with one custom-geometry case. Phase B proves the pattern at modest scale (2 bodies, 8 sphere shells, zero custom geometry) on the most heterogeneous data type: a real planet's body (Moon) plus a hypothetical body with very different scale conventions (Planet 9 — 24,000 km radius and a 48,000-Rp Hill sphere). If the config pattern handles these cleanly, Phases C and D become mechanical.

### Execution order (canonical)

Execute the sections below in this order. Each section is atomic. Run the syntax check at the end of each section before starting the next.

1. Pre-flight verification (Section 2)
2. Add Moon configs to `shell_configs.py` (Section 3)
3. Add Planet 9 configs to `shell_configs.py` (Section 4)
4. Modify `planet_visualization.py` — Moon delegation (Section 5)
5. Modify `planet_visualization.py` — Planet 9 delegation (Section 6)
6. Run verification plan (Section 7)

If any step fails its syntax check, STOP and resolve before proceeding.

---

## 2. Pre-flight Verification

### 2.1 Confirm Phase A is in place

Run:

```bash
python3 -c "
from orrery_rendering import build_sphere_shell, create_info_marker
from shell_configs import SHELL_CONFIGS, CUSTOM_SHELLS
assert 'Mercury' in SHELL_CONFIGS, 'Phase A SHELL_CONFIGS missing Mercury'
assert 'Mercury' in CUSTOM_SHELLS, 'Phase A CUSTOM_SHELLS missing Mercury'
assert len(SHELL_CONFIGS['Mercury']) == 6, 'Mercury sphere shell count mismatch'
assert len(CUSTOM_SHELLS['Mercury']) == 2, 'Mercury custom shell count mismatch'
print('Phase A baseline OK')
"
```

If anything fails, STOP — Phase B assumes Phase A is complete and consistent.

### 2.2 Confirm source files are post-Step-2

```bash
grep -c "hoverinfo='skip'" /path/to/moon_visualization_shells.py
# Expected: at least 5 (the 6 sphere shells; crust uses 'none' on mesh, so 5 is fine)

grep -c "hoverinfo='skip'" /path/to/planet9_visualization_shells.py
# Expected: at least 1 (Hill sphere; surface is mesh3d using 'none')

grep "Module updated:" /path/to/moon_visualization_shells.py | head -1
# Expected: contains "May 2026"

grep "Module updated:" /path/to/planet9_visualization_shells.py | head -1
# Expected: contains "May 2026"
```

If either file lacks the May 2026 credit or the `hoverinfo='skip'` markers, STOP — the file is not the post-Step-2 baseline.

### 2.3 Confirm CENTER_BODY_RADII entries exist

```bash
python3 -c "
from constants_new import CENTER_BODY_RADII, KM_PER_AU
print('Moon:', CENTER_BODY_RADII['Moon'], 'km =', CENTER_BODY_RADII['Moon']/KM_PER_AU, 'AU')
print('Planet 9:', CENTER_BODY_RADII['Planet 9'], 'km =', CENTER_BODY_RADII['Planet 9']/KM_PER_AU, 'AU')
"
# Expected:
# Moon: 1737.4 km = 1.16139... e-05 AU
# Planet 9: 24000 km = 1.60430... e-04 AU
```

Both must be present. `build_sphere_shell` resolves body radius via `CENTER_BODY_RADII[body_name] / KM_PER_AU`.

### 2.4 Confirm planet_visualization.py is post-Phase-A

```bash
grep -c "create_celestial_body_visualization" /path/to/planet_visualization.py
# Expected: at least 4 (function definition + Mercury delegation + docstring references)

grep -n "if planet_name == 'Mercury':" /path/to/planet_visualization.py
# Expected: should appear in create_planet_visualization() with the Phase A delegation pattern below it
```

If the file still has the pre-Phase-A if/elif chain for Mercury (multiple `create_mercury_*_shell` calls), STOP — Phase A was not applied to this file.

### 2.5 Backup files Phase B will touch

Before any edits:

```
shell_configs.py         -> shell_configs.py.phaseB_backup
planet_visualization.py  -> planet_visualization.py.phaseB_backup
```

Phase B touches exactly two files. Both are LF / ASCII (Phase A converted `planet_visualization.py` from CRLF).

### 2.6 Line ending inventory

| File | Expected | If different |
|------|----------|--------------|
| `shell_configs.py` | LF | Stop, investigate |
| `planet_visualization.py` | LF | Stop, investigate (Phase A converted) |
| `moon_visualization_shells.py` | LF | Not modified — informational only |
| `planet9_visualization_shells.py` | LF | Not modified — informational only |

Verify with `file <path>` on each. None should report "CRLF line terminators".

---

## 3. MODIFY — `shell_configs.py` — Add Moon configs

### 3.1 Where to insert

Locate the comment marker after Mercury's block:

```python
    # Other bodies added in Phases B, C, D
}
```

This is the closing of `SHELL_CONFIGS`. Insert the Moon block BEFORE this comment, so the Moon block sits between Mercury's `},` and the closing `}` of `SHELL_CONFIGS`. Match Mercury's indentation exactly (4 spaces for top-level body keys, 8 for shell keys).

### 3.2 Moon block contents

Copy the following block verbatim and insert it as described in Section 3.1. ASCII only, LF line endings. The hover_text values are the `description` field from each shell function's `layer_info` dict (with `<br>` tags). The tooltip values are the `moon_*_info` strings (with `\n` line breaks).

```python

    # ============================================================
    # Moon
    # ============================================================
    # Source: Weber et al. (2011), Science, "Seismic Detection of the Lunar Core";
    #         NASA Moon Fact Sheet; Apollo Seismic Experiment reports;
    #         NASA Solar System Dynamics (Hill sphere radius); Draper (1847).
    # Verified: April 2026 provenance audit; all 5 flagged claims confirmed.
    'Moon': {

        'inner_core': {
            'name': 'Inner Core',
            'radius_fraction': 0.1485,
            'color': 'rgb(255, 100, 0)',
            'opacity': 1.0,
            'n_points': 25,
            'marker_size': 4.0,
            'hover_text': (
                "The Moon has a small, partially molten core. Seismic data from Apollo missions and more recent studies of the Moon's wobble suggest:<br>"
                "* Inner Core: Believed to be a solid, iron-rich core, roughly 240 kilometers in radius:<br>"
                "  * Estimates for the temperature of the Moon's inner core vary slightly depending on the studies and methods used, but <br>"
                "    some more recent reanalyses of seismic data suggest temperatures around 1600-1700 K."
            ),
            'tooltip': (
                "The Moon has a small, partially molten core. Seismic data from Apollo missions and more recent studies of the Moon's wobble suggest:\n"
                "* Inner Core: Believed to be a solid, iron-rich core, roughly 240 kilometers in radius."
            ),
        },

        'outer_core': {
            'name': 'Outer Core',
            'radius_fraction': 0.2083,
            'color': 'rgb(255, 50, 0)',
            'opacity': 0.8,
            'n_points': 25,
            'marker_size': 3.7,
            'hover_text': (
                "Outer Core: Surrounding the inner core, this is thought to be a liquid, iron-rich outer core with a radius of about <br>"
                "330 kilometers. There might also be a small, partially molten layer of silicates around the outer core.<br>:"
                "* The Moon's outer core is generally understood to be hotter than its solid inner core, as it is in a molten or liquid <br>"
                "  state. <br>"
                "* Estimated Temperature: This layer would be slightly cooler than the inner core, but still hot enough to be molten at <br>"
                "  the lower pressures found here. Estimates typically fall around 1300 K to 1600 K. Let's use 1500 K as a representative <br>"
                "  value for the outer core for your model.<br>"
                "* Reasoning: As you move outwards, the temperature gradually decreases, but crucially, the pressure also decreases. At this <br>"
                "  depth and pressure, the temperature is above the melting point of the iron-rich material, allowing it to be liquid."
            ),
            'tooltip': (
                "Outer Core: Surrounding the inner core, this is thought to be a liquid, iron-rich outer core with a radius of about \n"
                "330 kilometers. There might also be a small, partially molten layer of silicates around the outer core."
            ),
        },

        # JUDGMENT CALL (flagged for Tony): the source function uses
        # radius_fraction=0.85 but the description text (and opacity=0.9655)
        # both indicate the outer mantle boundary is at 0.9655 of lunar radius
        # (1677.4 km / 1737.4 km). Preserved verbatim from source. If this is
        # a typo (opacity and radius_fraction swapped at some point), correct
        # to radius_fraction=0.9655 and opacity=1.0 before re-rendering.
        # See Section 8 / Decision Log for context.
        'mantle': {
            'name': 'Mantle',
            'radius_fraction': 0.85,
            'color': 'rgb(0, 50, 0)',
            'opacity': 0.9655,
            'n_points': 25,
            'marker_size': 3.4,
            'hover_text': (
                "Above the core lies the Moon's mantle, which makes up the bulk of its interior:<br>"
                "* Composition: Primarily composed of silicate rocks, similar to Earth's mantle, but with different proportions of <br>"
                "  elements. It's thought to be rich in olivine and pyroxene.<br>"
                "* State: The Moon's mantle is largely solid today. However, in its early history, it would have been at least partially <br>"
                "  molten, leading to volcanic activity that formed the vast maria (dark plains) on the lunar surface.<br>"
                "* Lunar Deep Moonquakes: Seismometers left by Apollo missions detected \"deep moonquakes\" originating in the mantle at <br>"
                "  depths of 700 to 1,200 km (435-745 miles). These are likely caused by tidal stresses from Earth.<br>"
                "* The Moon's mantle is a thick, largely solid layer, and its temperature varies significantly with depth, becoming <br>"
                "  cooler as you move outwards towards the crust.<br>"
                "  * Estimates for the temperature at the boundary between the mantle and the outer core range from 1573 K to 1743 K.<br>"
                "  * Estimates for the crust-mantle boundary are roughly 623 K to 823 K.<br>"
                "* The \"Draper point\" is around 798 K, which is the approximate temperature at which all solids start to glow a dim <br>"
                "  red. Therefore, the upper mantle, at these temperatures, would not visibly glow from black body radiation in normal <br>"
                "  conditions. Its primary emission would be in the infrared spectrum, invisible to the human eye. For the bulk of the <br>"
                "  mantle, it is primarily composed of silicate rocks like olivine and pyroxene. When seen in rock samples, these tend <br>"
                "  to be dark greenish to black (e.g., peridotite).<br>"
                "* Outer boundary of the mantle (base of the crust) as a fraction of Rm: 1677.4 km/1737.4 km~0.9655"
            ),
            'tooltip': (
                "Above the core lies the Moon's mantle, which makes up the bulk of its interior:\n"
                "* Composition: Primarily composed of silicate rocks, similar to Earth's mantle, but with different proportions of \n"
                "  elements. It's thought to be rich in olivine and pyroxene.\n"
                "* State: The Moon's mantle is largely solid today. However, in its early history, it would have been at least partially \n"
                "  molten, leading to volcanic activity that formed the vast maria (dark plains) on the lunar surface.\n"
                "* Lunar Deep Moonquakes: Seismometers left by Apollo missions detected \"deep moonquakes\" originating in the mantle at \n"
                "  depths of 700 to 1,200 km (435-745 miles). These are likely caused by tidal stresses from Earth."
            ),
        },

        # Crust uses mesh3d (solid surface) per Phase A pattern for crusts.
        # Source function used Mesh3d with flatshading + ambient=1.0 lighting;
        # build_sphere_shell mesh3d path produces equivalent output.
        'crust': {
            'name': 'Crust',
            'radius_fraction': 1.0,
            'color': 'rgb(190, 190, 180)',
            'opacity': 1.0,
            'geometry_type': 'mesh3d',
            'mesh_resolution': 24,
            'hover_text': (
                "The outermost layer of the Moon is its crust, which is significantly thicker on the far side than on the near side:<br>"
                "* Composition: Dominated by anorthositic rocks (rich in plagioclase feldspar), which are lighter in color and form the <br>"
                "  lunar highlands. The dark maria, on the other hand, are vast basaltic plains formed by ancient volcanic eruptions that <br>"
                "  filled large impact basins.<br>"
                "* Thickness: The lunar crust varies in thickness. On the near side (facing Earth), it's estimated to be around 30-50 <br>"
                "  kilometers thick. On the far side, it can be much thicker, possibly reaching up to 100 kilometers or more. This <br>"
                "  asymmetry is a major characteristic of the Moon. The most compelling explanations for the Moon's crustal thickness <br>"
                "  asymmetry point to a combination of factors related to its formation in Earth's intense thermal environment and a <br>"
                "  massive early impact that shaped its internal heat distribution and subsequent geological evolution.<br>"
                "* Surface Features: The crust is heavily cratered due to billions of years of impacts from asteroids and comets. Other <br>"
                "  features include rilles (channels, often associated with lava flows), domes, and wrinkle ridges.<br>"
                "* Given the mix of lighter highlands and darker maria, and the overall neutral tone, a medium, slightly warm grey.<br>"
                "* Unlike Earth, the Moon does not have a global, internally generated magnetic field today. However, rocks collected <br>"
                "  during the Apollo missions showed evidence of remnant magnetism, indicating that the Moon did possess a global <br>"
                "  magnetic field in its early history, likely generated by a liquid core dynamo similar to Earth's. Today, there are <br>"
                "  localized magnetic anomalies on the lunar surface, thought to be remnants of this ancient magnetic field or perhaps <br>"
                "  due to impact processes. These regions can sometimes interact with the solar wind, creating small <br>"
                "  \"mini-magnetospheres.\".<br>"
                "* Solar Wind Interaction: Without a global magnetic field, the Moon is directly exposed to the solar wind, a stream of <br>"
                "  charged particles from the Sun. This constant bombardment contributes to space weathering of the lunar surface.<br>"
                "* Water Ice: One of the most significant discoveries in recent lunar exploration is the confirmed presence of water ice, <br>"
                "  particularly in permanently shadowed regions within craters at the Moon's poles.<br>"
                "* Regolith: The entire lunar surface is covered by a layer of fine, powdery dust and broken rock fragments called regolith. <br>"
                "  It's formed by billions of years of micrometeoroid impacts and varies in thickness from a few meters in the maria to tens <br>"
                "  of meters in the highlands.<br>"
                "* Tidally Locked: The Moon is tidally locked with Earth, meaning the same side of the Moon (the \"near side\") always faces <br>"
                "  Earth."
            ),
            'tooltip': (
                "The outermost layer of the Moon is its crust, which is significantly thicker on the far side than on the near side:\n"
                "* Composition: Dominated by anorthositic rocks (rich in plagioclase feldspar), which are lighter in color and form the \n"
                "  lunar highlands. The dark maria, on the other hand, are vast basaltic plains formed by ancient volcanic eruptions that \n"
                "  filled large impact basins.\n"
                "* Thickness: The lunar crust varies in thickness. On the near side (facing Earth), it's estimated to be around 30-50 \n"
                "  kilometers thick. On the far side, it can be much thicker, possibly reaching up to 100 kilometers or more."
            ),
        },

        'exosphere': {
            'name': 'Exosphere',
            'radius_fraction': 1.06,
            'color': 'rgb(100, 150, 255)',
            'opacity': 0.3,
            'n_points': 20,
            'marker_size': 2.0,
            'hover_text': (
                "The Moon essentially has no atmosphere in the traditional sense. Instead, it has an exosphere. It's an incredibly <br>"
                "tenuous layer of gases, far less dense than a vacuum on Earth. It's so thin that gas molecules rarely collide with <br>"
                "each other.<br>"
                "* Sources: The exosphere is formed from gases released from the Moon's interior from radioactive decay, outgassing <br>"
                "  from the surface due to solar wind bombardment, and micrometeoroid impacts.<br>"
                "* Composition: Primarily composed of noble gases like argon and helium, along with trace amounts of sodium, potassium, <br>"
                "  hydrogen, and other elements.<br>"
                "* No Weather: Due to its extreme thinness, there's no atmospheric pressure, no wind, no weather, and no significant <br>"
                "  shielding from solar radiation or micrometeoroids.<br>"
                "* Practical or \"Dense\" Extent: For most practical purposes, where collisions between particles are still somewhat <br>"
                "  relevant or where density is higher, the exosphere is often considered to extend up to about 100 kilometers above <br>"
                "  the lunar surface. So, a more \"dense\" part of the exosphere extends from 1.0 Rm to roughly 1.06 Rm."
            ),
            'tooltip': (
                "The Moon essentially has no atmosphere in the traditional sense. Instead, it has an exosphere. It's an incredibly \n"
                "tenuous layer of gases, far less dense than a vacuum on Earth. It's so thin that gas molecules rarely collide with \n"
                "each other.\n"
                "* Composition: Primarily composed of noble gases like argon and helium, along with trace amounts of sodium, potassium, \n"
                "  hydrogen, and other elements.\n"
                "* No Weather: Due to its extreme thinness, there's no atmospheric pressure, no wind, no weather, and no significant \n"
                "  shielding from solar radiation or micrometeoroids."
            ),
        },

        'hill_sphere': {
            'name': 'Hill Sphere',
            'radius_fraction': 34.53,
            'color': 'rgb(0, 255, 0)',
            'opacity': 0.25,
            'n_points': 20,
            'marker_size': 1.0,
            'hover_text': (
                "The Moon's Hill sphere (also known as the Roche sphere in this context) is the region around it where its own gravity <br>"
                "is the dominant force attracting satellites, as opposed to the much stronger gravitational pull of the Earth. If an <br>"
                "object is outside the Moon's Hill sphere, it would typically end up orbiting Earth instead of the Moon.<br>"
                "* The estimated radius of the Moon's Hill sphere is approximately 60,000 kilometers, approximately 34.53 lunar radii."
            ),
            'tooltip': (
                "SET MANUAL SCALE TO AT LEAST 0.001 AU TO VISUALIZE.\n\n"
                "The Moon's Hill sphere (also known as the Roche sphere in this context) is the region around it where its own gravity \n"
                "is the dominant force attracting satellites, as opposed to the much stronger gravitational pull of the Earth. If an \n"
                "object is outside the Moon's Hill sphere, it would typically end up orbiting Earth instead of the Moon.\n"
                "* The estimated radius of the Moon's Hill sphere is approximately 60,000 kilometers, approximately 34.53 lunar radii."
            ),
        },

    },
```

### 3.3 Notes on this transcription

1. The Moon mantle entry intentionally preserves the source's apparent typo (`radius_fraction=0.85` vs `opacity=0.9655`). See the inline comment in the block. Tony's call whether to correct after visual verification.

2. Moon `inner_core` and `outer_core` source descriptions contain unicode-looking apostrophes (curly `'`) — these were generated by `\'` escapes in the original Python strings, which produce straight ASCII apostrophes. The values above use straight apostrophes (`'`). No Unicode introduced.

3. Moon exosphere `n_points=20` and Hill sphere `n_points=20` come from the source (not the build_sphere_shell default). Preserved explicitly.

4. The source `moon_outer_core` description has an artifact `<br>:` (extra colon) — preserved verbatim per "exact data extraction" rule. Cosmetic, doesn't affect rendering.

5. The Moon crust description includes content that doesn't appear in the source's `moon_crust_info` tooltip (the full bullet list on space weathering, water ice, regolith, tidal locking). The `tooltip` field in the config uses the abbreviated `*_info` string. The `hover_text` field uses the full `description`.

---

## 4. MODIFY — `shell_configs.py` — Add Planet 9 configs

### 4.1 Where to insert

Insert the Planet 9 block immediately after Moon's closing `},` and before the `# Other bodies added in Phases B, C, D` comment line.

### 4.2 Planet 9 block contents

```python

    # ============================================================
    # Planet 9 (hypothetical)
    # ============================================================
    # Source: Batygin & Brown (2016, 2021); Fortney et al. (2016);
    #         NASA Solar System Exploration.
    #         All values are model predictions for a 5-10 Earth-mass ice giant;
    #         Planet Nine has not been observationally confirmed.
    # Verified: April 2026 provenance audit; 2 corrections applied (Eris typo,
    #           2021 semi-major axis refinement note).
    'Planet 9': {

        # The internal name is 'Crust' even though the GUI label and var_suffix
        # are 'Surface' / 'surface'. The current trace renders as
        # "Planet 9: Crust" - preserved verbatim. This may have originated as a
        # copy-paste from Pluto/Eris crust configs (Planet 9 is hypothetical and
        # was modeled on inner-solar-system structure conventions). Cosmetic;
        # not a value bug.
        'surface': {
            'name': 'Crust',
            'radius_fraction': 1.0,
            'color': 'rgb(83, 68, 55)',
            'opacity': 1.0,
            'geometry_type': 'mesh3d',
            'mesh_resolution': 24,
            'hover_text': (
                "Planet 9 Surface<br>"
                "(Note: toggle off the cloud layer in the legend to better see the interior structure.)<br><br>"
                "The estimation of Planet Nine's radius being between 3 and 4 Earth radii, with a specific estimate of around 3.7 Earth <br>"
                "radii (or 23,500 - 24,000 km), appears in several scientific discussions. This size estimate is often linked to the <br>"
                "assumption that Planet Nine is likely an ice giant, similar in composition to Uranus and Neptune, but potentially a <br>"
                "smaller version.<br>"
                "* Mass and Density Relationship: For a given mass, the radius of a planet is strongly influenced by its density.<br>"
                "* Terrestrial Planets: Terrestrial planets (like Earth, Mars, Venus, Mercury) are primarily composed of rock and metal, <br>"
                "  making them quite dense. If Planet Nine were a terrestrial planet with 5-10 times the mass of Earth, its radius would <br>"
                "  likely be significantly smaller than 3-4 Earth radii due to its high density.<br>"
                "* Gas Giants: Gas giants (like Jupiter and Saturn) are composed mostly of hydrogen and helium, making them very large and <br>"
                "  not very dense. A planet with several Earth masses composed primarily of these light gases would have a much larger radius <br>"
                "  than 3-4 Earth radii.<br>"
                "* Ice Giants: Ice giants (like Uranus and Neptune) have a composition that includes heavier elements like oxygen, carbon, <br>"
                "  nitrogen, and sulfur, often in the form of water, methane, and ammonia ices, along with a significant amount of hydrogen and <br>"
                "  helium. This composition results in densities higher than gas giants but lower than terrestrial planets.<br>"
                "The 3-4 Earth radii estimate, particularly the 3.7 Earth radii figure, comes from models that assume Planet Nine has a mass <br>"
                "around 5-10 Earth masses and an internal composition similar to Uranus and Neptune. These models predict that such a planet <br>"
                "would have a larger radius than Earth due to its significant mass, but not as large as a pure gas giant with the same mass due <br>"
                "to the presence of heavier \"ice\" materials. Therefore, the estimated radius of 3-4 Earth radii strongly suggests that Planet <br>"
                "Nine, if it exists, is likely an ice giant or a sub-Neptune type of planet, rather than a rocky terrestrial planet or a large <br>"
                "gas giant. This is also consistent with theories about how a planet could have formed or been captured in the distant outer <br>"
                "solar system."
            ),
            'tooltip': (
                "USE MANUAL SCALED OF 0.005 AU TO VIEW CLOSELY."
                "4.6 MB PER FRAME FOR HTML.\n\n"
                "The estimation of Planet Nine's radius being between 3 and 4 Earth radii, with a specific estimate of around 3.7 Earth \n"
                "radii (or 23,500 - 24,000 km), appears in several scientific discussions. This size estimate is often linked to the \n"
                "assumption that Planet Nine is likely an ice giant, similar in composition to Uranus and Neptune, but potentially a \n"
                "smaller version."
            ),
        },

        # Hill sphere radius_fraction = 48000 (Planet 9 radii) corresponds to
        # ~7.6 AU using PLANET9_RADIUS_AU. NOTE: the source function had a
        # latent NameError bug (line 267: r_info = radius * 1.05 referenced
        # an undefined local 'radius' - the correct variable was 'layer_radius').
        # The bug would only trigger when the Hill sphere checkbox was toggled
        # on with a manual scale >= 8 AU. The migration silently fixes this
        # because build_sphere_shell computes r_info from the correctly-resolved
        # radius_au. No action needed - flagged for awareness.
        'hill_sphere': {
            'name': 'Hill Sphere',
            'radius_fraction': 48000,
            'color': 'rgb(0, 255, 0)',
            'opacity': 0.3,
            'n_points': 50,
            'marker_size': 2.0,
            'hover_text': (
                "SELECT MANUAL SCALE OF AT LEAST 8 AU TO VISUALIZE PLANET 9 CENTERED OR 800 AU HELIOCENTRIC.<br><br>"
                "Hill Sphere: Planet 9's Hill sphere, or Roche sphere, is the region around it where its gravitational influence dominates <br><br>"
                "over the Sun's. The radius of Planet 9's Hill sphere is very large, approximately 7.6 AU.<br>"
                "To arrive at the Hill sphere estimate of 7.6 AU, we made the following key assumptions about Planet Nine: <br>"
                "* Semi-major axis (a): We assumed a semi-major axis of 600 AU. This value is within the range of 500-700 AU suggested <br>"
                "  by some studies, including those considering the IRAS/AKARI observations. Note: 2021 refinements by Batygin & Brown <br>"
                "  favor a slightly closer orbit (~460 AU central estimate). The semi-major axis has a direct linear relationship with <br>"
                "  the Hill sphere radius. A larger semi-major axis leads to a larger Hill sphere.<br>"
                "* Eccentricity (e): We assumed an eccentricity of 0.30 (range 0.15-0.40 in newer models). This gives a perihelion <br>"
                "  around 280 AU and an aphelion around 1120 AU. The eccentricity affects the Hill sphere radius because the formula <br>"
                "  uses the distance to the Sun at the perihelion. A higher eccentricity would result in a smaller Hill sphere radius.<br>"
                "* Mass of Planet Nine (m): We assumed a mass of 6 times the mass of Earth. This is the current 'sweet spot' estimate <br>"
                "  from Batygin & Brown (2021), revised down from the original 10 Earth mass prediction. The mass has a cubic root <br>"
                "  relationship with the Hill sphere radius.<br>"
                "* Mass of the Sun (M): We used the standard value for the mass of the Sun. This is a well-established constant.<br>"
                "* In summary: the region where Planet 9's gravity is strong enough to hold onto its own moons despite the Sun's pull is <br>"
                "  what the Hill sphere represents. To estimate the radius of this safe zone, we take Planet Nine's average distance from <br>"
                "  the Sun, which we're assuming to be 600 AU (that's 600 times the distance between the Earth and the Sun). Because <br>"
                "  Planet Nine's orbit isn't a perfect circle but more of an oval shape (we call this eccentricity, and we're assuming <br>"
                "  it's 0.30), the closest it gets to the Sun is a bit less than this average. To account for this, we consider the distance <br>"
                "  at its closest approach, which is roughly its average distance multiplied by (one minus the eccentricity), <br>"
                "  so 600AUx(1-0.30)=600AUx0.70=420AU. This closest distance is important because the Sun's gravity is strongest there, <br>"
                "  making it harder for Planet Nine to hold onto moons. Now, we also need to consider how strong Planet Nine's gravity is <br>"
                "  compared to the Sun's. We're assuming Planet Nine has a mass of 6 times the mass of the Earth. The Sun, of course, is <br>"
                "  vastly more massive.<br>"
                "* The full equation for calculating the Hill sphere radius is: r_Hill = a x (m/(3 x M))^(1/3). Where: a is the semi-major <br>"
                "  axis of Planet Nine's orbit around the Sun; m is the mass of Planet Nine; M is the mass of the Sun."
            ),
            'tooltip': (
                "SELECT MANUAL SCALE OF AT LEAST 8 AU TO VISUALIZE PLANET 9 CENTERED OR 800 AU HELIOCENTRIC.\n"
                "1.3 MB PER FRAME FOR HTML.\n\n"
                "Hill Sphere: Planet 9's Hill sphere, or Roche sphere, is the region around it where its gravitational influence dominates \n"
                "over the Sun's. The radius of Planet 9's Hill sphere is very large, approximately 7.6 AU."
            ),
        },

    },
```

### 4.3 Notes on this transcription

1. `radius_fraction=48000` is correct: 48000 * PLANET9_RADIUS_AU = 48000 * (24000 km / 149597870.7 km/AU) ≈ 7.70 AU. Source tooltip claims "approximately 7.6 AU" — close enough.

2. `n_points=50` preserved from the source. The source function explicitly set `n_points=50` for the Planet 9 Hill sphere (which is unusual — Step 2 generally reduced large outer spheres to 20). Preserve verbatim; if Tony wants to reduce this for memory, that's a separate decision after Phase B verifies the migration is functionally correct.

3. `marker_size=2.0` preserved from the source despite the trace_name being Hill Sphere with green dots. (Step 2 generally used `marker_size=1.0` for Hill spheres — Mercury and Moon both use 1.0. Preserve the existing value for Planet 9.)

4. The Planet 9 surface tooltip has an oddity: `"USE MANUAL SCALED OF 0.005 AU TO VIEW CLOSELY."` lacks a newline before the next sentence (`"4.6 MB PER FRAME FOR HTML.\n\n"`). Preserved verbatim — looks like a missing `\n` in the source, but it's a cosmetic tk Label issue.

5. The hover_text for surface contains `"(Note: toggle off the cloud layer in the legend...)"` but Planet 9 has no cloud layer per SHELL_DEFINITIONS. Vestigial copy-paste text from a gas giant template. Preserved verbatim.

---

## 5. MODIFY — `planet_visualization.py` — Moon delegation

### 5.1 Strategy

Replace the Moon if-block in `create_planet_visualization()` with a one-line delegation to `create_celestial_body_visualization()`, matching the Phase A Mercury pattern.

### 5.2 Edit

Locate the Moon block in `create_planet_visualization()` (currently lines 713-725):

Find this exact text:

```python
    if planet_name == 'Moon':
        if shell_vars['moon_inner_core'].get() == 1:
            traces.extend(create_moon_inner_core_shell(center_position))
        if shell_vars['moon_outer_core'].get() == 1:
            traces.extend(create_moon_outer_core_shell(center_position))
        if shell_vars['moon_mantle'].get() == 1:
            traces.extend(create_moon_mantle_shell(center_position))
        if shell_vars['moon_crust'].get() == 1:
            traces.extend(create_moon_crust_shell(center_position))
        if shell_vars['moon_exosphere'].get() == 1:
            traces.extend(create_moon_exosphere_shell(center_position))
        if shell_vars['moon_hill_sphere'].get() == 1:
            traces.extend(create_moon_hill_sphere_shell(center_position))
```

Replace with:

```python
    if planet_name == 'Moon':
        # Step 3 Phase B: delegate to unified config-driven dispatch.
        # Same pattern as Mercury (Phase A). NOTE: center_object hardcoded
        # to body_name here because create_planet_visualization does not
        # receive the plot's center body. Corrected in Phase D when callers
        # use the unified function directly.
        return create_celestial_body_visualization(
            fig, planet_name, shell_vars,
            animate=animate, frames=frames,
            center_position=center_position,
            object_type='Moon',
            center_object='Moon',
        )
```

Note the early `return` — matches Mercury's pattern. Short-circuits the rest of the function for Moon.

### 5.3 Verification

```bash
python3 -m py_compile planet_visualization.py
# Expected: no output

grep -A 3 "if planet_name == 'Moon':" planet_visualization.py | head -10
# Expected: shows the new delegation block, not the old if/elif chain
```

---

## 6. MODIFY — `planet_visualization.py` — Planet 9 delegation

### 6.1 Strategy

Same as Section 5. Replace the Planet 9 if-block with a one-line delegation.

### 6.2 Edit

Locate the Planet 9 block in `create_planet_visualization()` (currently lines 851-855):

Find this exact text:

```python
    if planet_name == 'Planet 9':
        if shell_vars['planet9_surface'].get() == 1:
            traces.extend(create_planet9_surface_shell(center_position))
        if shell_vars['planet9_hill_sphere'].get() == 1:
            traces.extend(create_planet9_hill_sphere_shell(center_position))
```

Replace with:

```python
    if planet_name == 'Planet 9':
        # Step 3 Phase B: delegate to unified config-driven dispatch.
        # Same pattern as Mercury (Phase A) and Moon (Phase B above).
        return create_celestial_body_visualization(
            fig, planet_name, shell_vars,
            animate=animate, frames=frames,
            center_position=center_position,
            object_type='Planet 9',
            center_object='Planet 9',
        )
```

### 6.3 Edit order note

Edit Planet 9 (Section 6) BEFORE Moon (Section 5) if applying both edits in one pass with bottom-up discipline. Planet 9 is at a higher line number (~851) than Moon (~713). Bottom-up editing prevents line-number drift.

If sections are executed in document order (Moon first, then Planet 9), apply each as a self-contained `str_replace` using the exact-string anchors above — line numbers don't matter for `str_replace` since the search is by content. The bottom-up note is only relevant if working with raw line-number-addressed edits.

### 6.4 Verification

```bash
python3 -m py_compile planet_visualization.py

grep -A 3 "if planet_name == 'Planet 9':" planet_visualization.py | head -10
# Expected: shows the new delegation block

# Confirm no old-style if/elif chain remnants for Moon or Planet 9:
grep -c "create_moon_inner_core_shell" planet_visualization.py
# Expected: 1 (still imported at top of file, but not called from dispatch)

grep -c "create_planet9_surface_shell" planet_visualization.py
# Expected: 1 (still imported, not called from dispatch)
```

The shell function imports at the top of `planet_visualization.py` (lines ~90-300) are NOT removed in Phase B. Pure delete is part of Phase D cleanup. The functions are now unreachable from the dispatch path but the imports keep their names defined so dependent code (e.g., `palomas_orrery.py`'s `globals()` lookup for tooltips) continues working.

---

## 7. Verification Plan

### 7.1 Static checks

```bash
# Both modified files compile
python3 -m py_compile shell_configs.py planet_visualization.py

# Both are LF
for f in shell_configs.py planet_visualization.py; do
    file "$f" | grep -q CRLF && echo "FAIL: $f still CRLF" || echo "OK: $f"
done

# No new Unicode characters introduced
for f in shell_configs.py planet_visualization.py; do
    if grep -P '[^\x00-\x7F]' "$f" > /dev/null; then
        echo "FAIL: $f contains non-ASCII"
    else
        echo "OK: $f ASCII clean"
    fi
done
```

### 7.2 Import smoke test

```bash
python3 -c "
from orrery_rendering import build_sphere_shell, create_info_marker
from shell_configs import SHELL_CONFIGS, CUSTOM_SHELLS
from planet_visualization import create_celestial_body_visualization, create_planet_visualization

# Phase A baseline still intact
assert 'Mercury' in SHELL_CONFIGS and len(SHELL_CONFIGS['Mercury']) == 6
assert 'Mercury' in CUSTOM_SHELLS and len(CUSTOM_SHELLS['Mercury']) == 2

# Moon block - 6 sphere shells, no custom
moon = SHELL_CONFIGS['Moon']
assert set(moon.keys()) == {'inner_core', 'outer_core', 'mantle', 'crust', 'exosphere', 'hill_sphere'}, \
    'Moon sphere keys mismatch: %s' % sorted(moon.keys())
for shell_name, cfg in moon.items():
    assert 'radius_fraction' in cfg or 'radius_au' in cfg, '%s missing radius' % shell_name
    for k in ('name', 'color', 'opacity', 'hover_text', 'tooltip'):
        assert k in cfg, 'Moon/%s missing %s' % (shell_name, k)
    # mesh3d shells need mesh_resolution; scatter3d shells need marker_size
    if cfg.get('geometry_type') == 'mesh3d':
        assert 'mesh_resolution' in cfg, 'Moon/%s mesh3d missing mesh_resolution' % shell_name
    else:
        assert 'marker_size' in cfg, 'Moon/%s scatter3d missing marker_size' % shell_name

assert 'Moon' not in CUSTOM_SHELLS, 'Moon should have no CUSTOM_SHELLS entry'

# Planet 9 block - 2 sphere shells, no custom
p9 = SHELL_CONFIGS['Planet 9']
assert set(p9.keys()) == {'surface', 'hill_sphere'}, \
    'Planet 9 sphere keys mismatch: %s' % sorted(p9.keys())
for shell_name, cfg in p9.items():
    assert 'radius_fraction' in cfg or 'radius_au' in cfg
    for k in ('name', 'color', 'opacity', 'hover_text', 'tooltip'):
        assert k in cfg, 'Planet 9/%s missing %s' % (shell_name, k)

assert 'Planet 9' not in CUSTOM_SHELLS, 'Planet 9 should have no CUSTOM_SHELLS entry'

# Spot-check key values (will catch transcription errors)
assert SHELL_CONFIGS['Moon']['inner_core']['radius_fraction'] == 0.1485
assert SHELL_CONFIGS['Moon']['hill_sphere']['radius_fraction'] == 34.53
assert SHELL_CONFIGS['Moon']['crust']['geometry_type'] == 'mesh3d'
assert SHELL_CONFIGS['Moon']['mantle']['radius_fraction'] == 0.85  # see judgment call
assert SHELL_CONFIGS['Moon']['mantle']['opacity'] == 0.9655
assert SHELL_CONFIGS['Planet 9']['surface']['geometry_type'] == 'mesh3d'
assert SHELL_CONFIGS['Planet 9']['hill_sphere']['radius_fraction'] == 48000

print('All Phase B static checks PASS')
"
```

### 7.3 Builder smoke test (no GUI)

```bash
python3 -c "
from orrery_rendering import build_sphere_shell
from shell_configs import SHELL_CONFIGS

# Build every Moon shell - should not raise
for shell_name, cfg in SHELL_CONFIGS['Moon'].items():
    traces = build_sphere_shell(cfg, 'Moon', (0, 0, 0))
    assert len(traces) == 2, 'Moon/%s expected 2 traces, got %d' % (shell_name, len(traces))

# Build every Planet 9 shell - should not raise
for shell_name, cfg in SHELL_CONFIGS['Planet 9'].items():
    traces = build_sphere_shell(cfg, 'Planet 9', (0, 0, 0))
    assert len(traces) == 2, 'Planet 9/%s expected 2 traces, got %d' % (shell_name, len(traces))

print('Builder smoke test PASS')
"
```

### 7.4 Functional check — Moon renders via configs (Mode 5)

Run the orrery, select Moon as center body, enable all 6 Moon shells, generate a plot.

| Check | Pass criterion |
|-------|----------------|
| Inner core renders | Red-orange dot sphere at r ≈ 0.1485 of Moon radius |
| Outer core renders | Ember-red dot sphere at r ≈ 0.2083 |
| Mantle renders | Dark green dot sphere at r ≈ 0.85 (NOT 0.9655 - see judgment call) |
| Crust renders | Slightly warm grey SOLID surface (mesh3d) at r=1.0 |
| Exosphere renders | Lighter blue dot sphere at r ≈ 1.06 |
| Hill sphere renders | Sparse green dot sphere at r ≈ 34.53 (requires manual scale ≥ 0.001 AU) |
| Hover labels | One cross info marker per shell at north pole; new style (size=8, red outline) |
| Sun direction indicator | Appears ONCE, scaled to outermost active shell (Hill Sphere if active) |
| Visible regression | None vs Mercury (Phase A) rendering quality |

### 7.5 Functional check — Planet 9 renders via configs (Mode 5)

Run the orrery, select Planet 9 as center body, enable surface, generate a plot. (Hill sphere requires manual scale ≥ 8 AU and produces a 1.3 MB frame — verify separately if visually checked.)

| Check | Pass criterion |
|-------|----------------|
| Surface renders | Brownish solid surface (mesh3d) at r=1.0 (≈24,000 km diameter) |
| Surface trace name | "Planet 9: Crust" (preserved internal name) |
| Hover label | One cross info marker at north pole carrying full hover text |
| Sun direction indicator | Appears ONCE, scaled to surface radius |
| Hill sphere (if toggled, scale ≥ 8 AU) | Green sparse sphere at r ≈ 7.6 AU. Previously crashed with NameError — now works. |

### 7.6 Functional check — other bodies unchanged

Select Mercury (Phase A regression), Venus, Earth, Mars one at a time. All should render as before. The if/elif chain for the eleven non-migrated bodies is untouched.

For Mercury specifically, confirm:
- Sodium tail still renders (lazy import via CUSTOM_SHELLS)
- Magnetosphere still rotates to face Sun in off-center views
- One Sun direction indicator per render (Phase A's de-duplication still works)

### 7.7 Indicator de-duplication check

For Moon and Planet 9 (in their centered views), count the rendered Sun direction arrow segments. Expected: exactly ONE indicator regardless of how many shells are active.

Pre-Phase-B baseline: Planet 9 emitted one indicator per Hill sphere render (one `sun_traces` block at line 299). Moon emitted zero indicators (none of its sphere shell functions called `create_sun_direction_indicator` — Moon's functions never had the call).

Post-Phase-B: both bodies route through `create_celestial_body_visualization`, which emits one indicator per body at the outermost active shell radius. Net change for Moon: zero -> one (gain). Net change for Planet 9: one -> one (de-duplicated; no change in count, but now sized to outermost shell instead of inner surface).

Note that the indicator is suppressed entirely in body-centered views (`center_position == (0,0,0)`) per the Phase A restoration. The indicator appears only in heliocentric / fly-to views where the body is offset from origin.

### 7.8 GUI tooltip regression check

Hover the GUI checkboxes for Moon's 6 shells and Planet 9's 2 shells. Tooltips should still display correctly, sourced from `moon_*_info` / `planet9_*_info` strings via the `globals()` lookup in `build_shell_checkboxes`. The `*_info` strings are still defined in their shell files (Phase B does NOT remove them). Phase D will switch this to read from `SHELL_CONFIGS[body][shell]['tooltip']`.

### 7.9 File size baseline (informational)

Save a Moon-only static plot to HTML. Then save a Planet 9-only static plot. Compare to pre-Phase-B baselines if available.

Expected: similar or slightly smaller. The bulk of the size savings from Step 2's single-info-marker pattern is already in place; Phase B is architectural consolidation, not a size optimization. The big wins come from Phase C bodies with many shells (Earth, Jupiter, Saturn).

### 7.10 Mode 5 visual verification items for Tony

1. **Moon mantle radius judgment call.** With the migrated config (radius_fraction=0.85), the mantle dot sphere renders at 85% of Moon radius. The mantle/crust gap is significant (15% of Moon radius ≈ 260 km). The description text says the actual boundary is at 0.9655 (≈60 km gap). If the rendering looks "obviously wrong" (a large visible shell between mantle and crust), the typo theory is correct — change `radius_fraction` to 0.9655 and `opacity` to 1.0 in `shell_configs.py`, then re-test.

2. **Moon crust mesh3d**: Should render as a solid grey sphere (not dots), matching Mercury's crust from Phase A. If the surface looks broken (gaps, jagged tessellation), check that `mesh_resolution=24` is in the config and not being overridden.

3. **Moon Hill sphere trace name**: previously rendered as `'Hill Sphere'` (no body prefix). Now renders as `'Moon: Hill Sphere'`. Confirm in legend. Minor incidental cleanup.

4. **Planet 9 surface mesh3d**: Should render as a solid brownish sphere. The 4.6 MB / frame note in the source tooltip refers to the OLD pattern with 50 hover points per shell + 50 fibonacci_sphere copies. Post-Step-2 (and post-Phase-B), the size is much lower because there's one hover point.

5. **Planet 9 Hill sphere bug confirmation**: with manual scale set to 10 AU and Planet 9 centered, toggle the Hill sphere checkbox. Pre-Phase-B this crashed silently (or visibly). Post-Phase-B it renders a green sparse sphere at ~7.6 AU. If it still crashes, the migration didn't propagate — check that the Planet 9 block in `create_planet_visualization` is the new delegation, not the old if/elif chain.

---

## 8. Decision Log and Open Items

### Decisions made by this manifest

1. **Moon mantle radius_fraction preserved at 0.85** despite the description text indicating 0.9655. The provenance audit (April 2026) verified textual claims, not code-vs-data consistency. Tony's visual judgment in Section 7.10 determines whether to correct after Phase B is complete.

2. **Planet 9 surface internal name kept as 'Crust'**. Cosmetic mismatch with the GUI label "Surface" but matches the current rendering. Renaming would change the legend entry and is out of scope.

3. **Planet 9 Hill sphere bug treated as incidental fix**. The migration silently corrects the NameError. No source file edit (the file is dead post-Phase-B anyway).

4. **n_points and marker_size preserved verbatim** from source layer_info dicts. Step 2's tuning of these values is the canonical source. Planet 9 Hill sphere's `n_points=50` (rather than the more typical 20) is preserved — Tony can reduce in a future memory-optimization pass if desired.

5. **Shell files left untouched** per Phase B Decision 3. No indicator-call stripping in `planet9_visualization_shells.py` (which has one at line 299) — the call is unreachable post-migration because the function is not called from the unified dispatch. Whole-file archive in Phase D.

6. **No `_info` import pruning**. The `globals()` lookup path in `build_shell_checkboxes` continues to work because `moon_*_info` and `planet9_*_info` strings are still defined in their shell files. Phase D switches to `SHELL_CONFIGS[body][shell]['tooltip']`.

7. **`object_type` and `center_object` hardcoded** to body name in both delegations, matching the Mercury Phase A pattern. The proper threading of `center_object_name` from the plot caller is a Phase D change.

### Open items for future phases (NOT Phase B scope)

- **Moon mantle radius correction** (judgment call, awaiting visual): if Tony confirms 0.85 is wrong, the fix is a 2-character edit to `shell_configs.py` (`radius_fraction=0.85` -> `0.9655`, `opacity=0.9655` -> `1.0`). Trivial.
- **Planet 9 Hill sphere n_points reduction** (memory optimization): drop from 50 to 20 if 50 is unnecessary. Not blocking.
- **Planet 9 surface "(toggle off the cloud layer...)" note** (text accuracy): vestigial copy-paste, can be cleaned up later.
- **`*_info` string deletion** (Phase D): the `moon_*_info` and `planet9_*_info` strings in the shell files become fully dead once GUI tooltips read from SHELL_CONFIGS. Removed when the shell files are archived.

### Risks and mitigations

| Risk | Mitigation |
|------|-----------|
| Mantle visual regression (0.85 vs 0.9655) | Already flagged for Mode 5 verification (Section 7.10 item 1). Fix is trivial if needed. |
| Planet 9 Hill sphere crash recurrence | Section 7.5 verifies the migration fixes the NameError. If it crashes, migration didn't apply. |
| Body prefix collision with other bodies' keys | Tested by Phase A (Mercury) and confirmed by the body_prefix-strip logic. Each body iterates only its own shell_vars subset because the prefix filter discards non-matching keys. |
| Shell file imports breaking | Phase B does not modify the import section of `planet_visualization.py`. Shell function names remain defined; `globals()` lookups in GUI tooltip wiring continue to work. |
| Lazy import for Moon/Planet 9 custom geometry | N/A — neither body has CUSTOM_SHELLS entries. No lazy imports triggered. |

### Implementation discipline (per protocol)

- Python binary mode (`rb`/`wb`) for all file reads/writes
- Bottom-up editing when multiple edits to same file (Section 6.3 note)
- Exact-string matching with `str_replace`, never regex
- One section at a time; run syntax check before proceeding
- Credit line update: `Module updated: May 2026 with Anthropic's Claude Opus 4.7` on every modified file. For `shell_configs.py`, the existing credit line in the module docstring already shows Opus 4.7 from Phase A — no change needed unless preferred to bump date. For `planet_visualization.py`, the credit line was NOT updated in Phase A (still shows "April 16, 2026 with Anthropic's Claude Opus 4.6"). Phase B is a good opportunity to update it.
- ASCII only in all edits; verify with `grep -P '[^\x00-\x7F]'`
- If any source value can't be confirmed from the uploaded/project files, STOP and ask Tony

---

## 9. Workflow Provenance

This manifest:
- Audited by Anthropic's Claude Opus 4.7
- Following Phase A handoff (May 13-14, 2026) by Opus 4.6
- From prompt v2 by Tony Quintanilla + Anthropic's Claude Opus 4.6
- Following protocol v3.22 (collegial Mode 7)

To be executed by: Anthropic's Claude Opus 4.6 + Tony, in a separate session.

The Phase A manifest set the quality bar. Aim for the same level of precision here: every conversion site identified, every value extracted exactly, every judgment call flagged.

*Module updated: May 2026 with Anthropic's Claude Opus 4.7*
