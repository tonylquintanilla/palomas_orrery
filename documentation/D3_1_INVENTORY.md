# D3.1 Inventory: Hovertext and Legendgroup State Across Shell Files

**Session:** May 22, 2026
**Author:** Anthropic's Claude Opus 4.7
**Reviewer (intended):** Anthropic's Claude Opus 4.7 (Mode 7 audit)
**Integrator:** Tony Quintanilla

Inventory phase of D3.1 (item 54). Captures the current state of legend names, legendgroups, and hovertext-lead-lines across all 15 `*_visualization_shells.py` files. Produced by static AST analysis with single-level variable resolution.

## Headline Finding

The dominant non-conformance pattern is **Rule 2 (hovertext leads with legend label)**, not Rule 1 or Rule 3. The info-marker pattern is structurally correct -- one geometry trace with `hoverinfo='skip'` plus one info marker carrying the hover -- but the info marker's text is typically `layer_info['description']`, `belt['description']`, or similar, which starts with the *description* rather than the legend label. When the user hovers the cursor, they see a paragraph about (say) atmospheric composition with no leading indicator of which shell it belongs to.

This explains Round 3 items 45 and 46 (Neptune radiation belts and FAC hovertext "not clearly labelled to connect them to the legend") as a codebase-wide pattern, not Neptune-specific. The sweep is mechanical: prepend `"{body}: {shell_name}\n\n"` (or `<br><br>`) to every info marker's text. The shell name is already available in scope wherever the info marker is constructed.

Secondary findings (much smaller counts):

- **Legendgroup missing on crust/cloud surface traces** (15 entries). Geometry trace omits `legendgroup`; paired info marker has its own. They don't toggle together. Add `legendgroup=trace_name` on the surface.
- **Solar shells use "Sun's X" or "X" instead of "Sun: X"** (9 entries). Heliospheric region names. Judgment call: convert to the convention or treat solar as a category file like comet/asteroid_belt?
- **Neptune magnetosphere has two showlegend=True traces in one group** (1 entry). Bow shock and envelope share legendgroup; both claim the legend. Pick one leader; suppress the other.
- **MAPS comet tails have seven showlegend=True traces in one group** (1 entry, 7 traces). Same pattern as Neptune magnetosphere but at higher count. Pick one leader.
- **Orphan function** `create_neptune_magnetic_poles` (1 entry, dead code from D2 Option C cleanup). Recommend removal.


---

## Section 1. Convention Summary (the rubric)

Three rules that every legend entry must satisfy. The sweep (D3.1 part 2) will bring non-conformant entries into compliance.

**Rule 1 -- Legend label format.** The user-visible legend name follows the form `"Body: Shell Name"` (e.g., `"Earth: Magnetosphere"`, `"Neptune: Adams Arc"`). **Exemption:** `asteroid_belt_visualization_shells.py` uses population names (`"Hilda Family"`, `"Jupiter Trojans (Greeks - L4)"`) and `comet_visualization_shells.py` prefixes with the specific comet's own name (`"MAPS: Nucleus"`, `"C/2026 A1: Tail"`). Rule 1 is not applied to these two files. The label of a multi-body category file should still be unambiguous within the legend.

**Rule 2 -- Hovertext leads with the legend label.** The first line of hover text matches the legend entry name. Applies to every trace in the legendgroup, so the cursor always identifies the entry regardless of which sub-trace it is over.

**Rule 3 -- Legendgroup independence.** Each shell gets its own legendgroup so it toggles independently. Within a group, exactly one trace has `showlegend=True` (the leader, carrying the visible name); all others have `showlegend=False`. Components of one structure (e.g., the four surface patches of a magnetosphere envelope) share a group. Functionally distinct features (e.g., Adams arc vs Le Verrier arc) get separate groups.

**Tony's tiebreaker for ambiguous cases:** "Are they different components of one structure, or are they functionally different structures?" If functionally different, split.

---

## Section 2. Conformance Summary

One row per file. `OK` = passes all rules. `FAIL` = at least one rule violated. `?` = ambiguous (multiple traces in a group, no rule violation detected, but reviewer should sanity-check). `ORPHAN` = function exists in source but is never called -- its traces never reach the live dispatch.

| File | Body | Entries | OK | FAIL | ? | Orphan |
|------|------|--------:|---:|-----:|--:|-------:|
| `asteroid_belt_visualization_shells.py` | Asteroid Belt | 4 | 4 | 0 | 0 | 0 |
| `comet_visualization_shells.py` | Comet | 9 | 5 | 4 | 0 | 0 |
| `earth_visualization_shells.py` | Earth | 14 | 0 | 14 | 0 | 0 |
| `eris_visualization_shells.py` | Eris | 6 | 0 | 6 | 0 | 0 |
| `jupiter_visualization_shells.py` | Jupiter | 11 | 2 | 9 | 0 | 0 |
| `mars_visualization_shells.py` | Mars | 12 | 2 | 10 | 0 | 0 |
| `mercury_visualization_shells.py` | Mercury | 3 | 0 | 3 | 0 | 0 |
| `moon_visualization_shells.py` | Moon | 7 | 0 | 7 | 0 | 0 |
| `neptune_visualization_shells.py` | Neptune | 11 | 0 | 10 | 0 | 1 |
| `planet9_visualization_shells.py` | Planet 9 | 3 | 0 | 3 | 0 | 0 |
| `pluto_visualization_shells.py` | Pluto | 7 | 0 | 7 | 0 | 0 |
| `saturn_visualization_shells.py` | Saturn | 11 | 2 | 9 | 0 | 0 |
| `solar_visualization_shells.py` | Sun | 18 | 0 | 18 | 0 | 0 |
| `uranus_visualization_shells.py` | Uranus | 9 | 2 | 7 | 0 | 0 |
| `venus_visualization_shells.py` | Venus | 9 | 0 | 9 | 0 | 0 |
| **TOTAL** | -- | **134** | **17** | **116** | **0** | **1** |

---

## Section 3. Per-File Detail

### `asteroid_belt_visualization_shells.py` (Asteroid Belt)

| Line | Builder | Sun? | Legend Label | Group | # | Hover lead | Conf. | Notes |
|-----:|---------|:----:|--------------|-------|--:|------------|:-----:|-------|
| 204 | `create_main_asteroid_belt` |  | trace_name='Main Asteroid Belt' | trace_name='Main Asteroid Belt' | 2 | <expr> | OK |  |
| 300 | `create_hilda_group` |  | trace_name='Hilda Family' | trace_name='Hilda Family' | 2 | <expr> | OK |  |
| 400 | `create_jupiter_trojans_greeks` |  | trace_name='Jupiter Trojans (Greeks - L4)' | trace_name='Jupiter Trojans (Greeks - L4)' | 2 | <expr> | OK |  |
| 496 | `create_jupiter_trojans_trojans` |  | trace_name='Jupiter Trojans (Trojans - L5)' | trace_name='Jupiter Trojans (Trojans - L5)' | 2 | <expr> | OK |  |

### `comet_visualization_shells.py` (Comet)

| Line | Builder | Sun? | Legend Label | Group | # | Hover lead | Conf. | Notes |
|-----:|---------|:----:|--------------|-------|--:|------------|:-----:|-------|
| 457 | `create_comet_nucleus` |  | f"{comet_name}: Nucleus" | <none> | 1 | <expr> | FAIL | leader trace missing legendgroup attribute |
| 550 | `create_maps_disintegration_marker` |  | 'MAPS: Disintegration' | <none> | 1 | <expr> | FAIL | leader trace missing legendgroup attribute |
| 716 | `create_maps_ghost_tail_trace` |  | '' | 'maps_ghost_tail' | 2 | <expr> | FAIL | no showlegend=True leader in group |
| 800 | `create_comet_coma` |  | f"{comet_name}: Coma" | f"{comet_name}: Coma" | 2 | <expr> | OK |  |
| 993 | `create_comet_dust_tail` |  | f"{comet_name}: Dust Tail" | f"{comet_name}: Dust Tail" | 2 | <expr> | OK |  |
| 1146 | `create_comet_ion_tail` |  | f"{comet_name}: Ion Tail" | f"{comet_name}: Ion Tail" | 2 | <expr> | OK |  |
| 1308 | `create_comet_anti_tail` |  | f"{comet_name}: Anti-tail" | f"{comet_name}: Anti-tail" | 2 | <expr> | OK |  |
| 1362 | `create_comet_anti_tail` |  | f"{comet_name}: Mini-jet {<expr>}" | f"{comet_name}: Mini-jet {<expr>}" | 2 | <expr> | OK |  |
| 1760 | `add_comet_tails_to_figure` |  | 'MAPS: Nucleus (disintegrated April 4, 2026)' | <none> | 7 |  | FAIL | leader trace missing legendgroup attribute; multiple showlegend=True traces in same group (7) |

### `earth_visualization_shells.py` (Earth)

| Line | Builder | Sun? | Legend Label | Group | # | Hover lead | Conf. | Notes |
|-----:|---------|:----:|--------------|-------|--:|------------|:-----:|-------|
| 67 | `create_earth_inner_core_shell` |  | trace_name=f"Earth: {layer_info['name']}" | trace_name=f"Earth: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |
| 139 | `create_earth_outer_core_shell` |  | trace_name=f"Earth: {layer_info['name']}" | trace_name=f"Earth: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |
| 209 | `create_earth_lower_mantle_shell` |  | trace_name=f"Earth: {layer_info['name']}" | trace_name=f"Earth: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |
| 279 | `create_earth_upper_mantle_shell` |  | trace_name=f"Earth: {layer_info['name']}" | trace_name=f"Earth: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |
| 372 | `create_earth_crust_shell` |  | f"Earth: {layer_info['name']}" | <none> | 1 |   | FAIL | leader trace missing legendgroup attribute |
| 446 | `create_earth_crust_shell` |  | trace_name=f"Earth: {layer_info['name']} (Info)" | trace_name=f"Earth: {layer_info['name']} (Info)" | 1 | <expr> | FAIL | hover lead does not echo body name; no showlegend=True leader in group |
| 503 | `create_earth_atmosphere_shell` |  | trace_name=f"Earth: {layer_info['name']}" | trace_name=f"Earth: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |
| 575 | `create_earth_upper_atmosphere_shell` |  | trace_name=f"Earth: {layer_info['name']}" | trace_name=f"Earth: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |
| 678 | `create_earth_magnetosphere_shell` | Y | 'Earth: Magnetosphere' | 'Earth: Magnetosphere' | 2 | magnetosphere_text=<expr> | FAIL | hover lead does not echo body name |
| 748 | `create_earth_magnetosphere_shell` | Y | 'Earth: Bow Shock' | 'Earth: Bow Shock' | 2 | bow_shock_text=<expr> | FAIL | hover lead does not echo body name |
| 835 | `create_earth_magnetosphere_shell` | Y | belt_names=<expr>[?] | belt_names=<expr>[?] | 2 | belt_text=<expr> | FAIL | hover lead does not echo body name |
| 967 | `create_earth_leo_shell` |  | 'Earth: Low Earth Orbit (LEO)' | 'Earth: Low Earth Orbit (LEO)' | 2 | <expr> | FAIL | hover lead does not echo body name |
| 1078 | `create_earth_geostationary_belt_shell` |  | 'Earth: Geostationary Belt (GEO)' | 'Earth: Geostationary Belt (GEO)' | 2 | <expr> | FAIL | hover lead does not echo body name |
| 1146 | `create_earth_hill_sphere_shell` |  | 'Earth: Hill Sphere' | 'Earth: Hill Sphere' | 2 | <expr> | FAIL | hover lead does not echo body name |

### `eris_visualization_shells.py` (Eris)

| Line | Builder | Sun? | Legend Label | Group | # | Hover lead | Conf. | Notes |
|-----:|---------|:----:|--------------|-------|--:|------------|:-----:|-------|
| 91 | `create_eris_core_shell` |  | trace_name=f"Eris: {layer_info['name']}" | trace_name=f"Eris: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |
| 162 | `create_eris_mantle_shell` |  | trace_name=f"Eris: {layer_info['name']}" | trace_name=f"Eris: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |
| 261 | `create_eris_crust_shell` |  | f"Eris: {layer_info['name']}" | <none> | 1 |   | FAIL | leader trace missing legendgroup attribute |
| 335 | `create_eris_crust_shell` |  | trace_name=f"Eris: {layer_info['name']} (Info)" | trace_name=f"Eris: {layer_info['name']} (Info)" | 1 | <expr> | FAIL | hover lead does not echo body name; no showlegend=True leader in group |
| 410 | `create_eris_atmosphere_shell` |  | trace_name=f"Eris: {layer_info['name']}" | trace_name=f"Eris: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |
| 494 | `create_eris_hill_sphere_shell` |  | trace_name=f"Eris: {layer_info['name']}" | trace_name=f"Eris: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |

### `jupiter_visualization_shells.py` (Jupiter)

| Line | Builder | Sun? | Legend Label | Group | # | Hover lead | Conf. | Notes |
|-----:|---------|:----:|--------------|-------|--:|------------|:-----:|-------|
| 107 | `create_jupiter_core_shell` |  | trace_name=f"Jupiter: {layer_info['name']}" | trace_name=f"Jupiter: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |
| 177 | `create_jupiter_metallic_hydrogen_shell` |  | trace_name=f"Jupiter: {layer_info['name']}" | trace_name=f"Jupiter: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |
| 249 | `create_jupiter_molecular_hydrogen_shell` |  | trace_name=f"Jupiter: {layer_info['name']}" | trace_name=f"Jupiter: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |
| 346 | `create_jupiter_cloud_layer_shell` |  | f"Jupiter: {layer_info['name']}" | <none> | 1 |   | FAIL | leader trace missing legendgroup attribute |
| 420 | `create_jupiter_cloud_layer_shell` |  | trace_name=f"Jupiter: {layer_info['name']} (Info)" | trace_name=f"Jupiter: {layer_info['name']} (Info)" | 1 | <expr> | FAIL | hover lead does not echo body name; no showlegend=True leader in group |
| 479 | `create_jupiter_upper_atmosphere_shell` |  | trace_name=f"Jupiter: {layer_info['name']}" | trace_name=f"Jupiter: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |
| 556 | `create_jupiter_magnetosphere` | Y | 'Jupiter: Magnetosphere' | 'Jupiter: Magnetosphere' | 2 | mag_desc="Jupiter's magnetosphere ext... | OK |  |
| 633 | `create_jupiter_io_plasma_torus` |  | 'Jupiter: Io Plasma Torus' | 'Jupiter: Io Plasma Torus' | 2 | io_desc="Io plasma torus: A donut-sha... | FAIL | hover lead does not echo body name |
| 723 | `create_jupiter_radiation_belts` |  | belt_names=<expr>[?] | belt_names=<expr>[?] | 2 | belt_texts=<expr>[?] | OK |  |
| 789 | `create_jupiter_hill_sphere_shell` |  | trace_name=f"Jupiter: {layer_info['name']}" | trace_name=f"Jupiter: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |
| 954 | `create_jupiter_ring_system` |  | f"Jupiter: {ring_info['name']}" | f"Jupiter: {ring_info['name']}" | 2 | ring_info['description'] | FAIL | hover lead does not echo body name |

### `mars_visualization_shells.py` (Mars)

| Line | Builder | Sun? | Legend Label | Group | # | Hover lead | Conf. | Notes |
|-----:|---------|:----:|--------------|-------|--:|------------|:-----:|-------|
| 85 | `create_mars_inner_core_shell` |  | trace_name=f"Mars: {layer_info['name']}" | trace_name=f"Mars: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |
| 170 | `create_mars_outer_core_shell` |  | trace_name=f"Mars: {layer_info['name']}" | trace_name=f"Mars: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |
| 238 | `create_mars_mantle_shell` |  | trace_name=f"Mars: {layer_info['name']}" | trace_name=f"Mars: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |
| 331 | `create_mars_crust_shell` |  | f"Mars: {layer_info['name']}" | <none> | 1 |   | FAIL | leader trace missing legendgroup attribute |
| 405 | `create_mars_crust_shell` |  | trace_name=f"Mars: {layer_info['name']} (Info)" | trace_name=f"Mars: {layer_info['name']} (Info)" | 1 | <expr> | FAIL | hover lead does not echo body name; no showlegend=True leader in group |
| 464 | `create_mars_atmosphere_shell` |  | trace_name=f"Mars: {layer_info['name']}" | trace_name=f"Mars: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |
| 546 | `create_mars_upper_atmosphere_shell` |  | trace_name=f"Mars: {layer_info['name']}" | trace_name=f"Mars: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |
| 650 | `create_mars_magnetosphere_shell` | Y | 'Mars: Induced Magnetosphere' | 'Mars: Induced Magnetosphere' | 1 |  | OK |  |
| 718 | `create_mars_magnetosphere_shell` | Y | 'Mars: Bow Shock' | 'Mars: Bow Shock' | 2 | bow_shock_text=<expr>[0] | FAIL | hover lead does not echo body name |
| 806 | `create_mars_magnetosphere_shell` | Y | 'Mars: Crustal Magnetic Fields' | 'Mars: Crustal Magnetic Fields' | 2 | crustal_field_text=<expr>[0] | FAIL | hover lead does not echo body name; no showlegend=True leader in group |
| 894 | `create_mars_hill_sphere_shell` |  | f"Mars: {layer_info['name']}" | f"Mars: {layer_info['name']}" | 1 |  | OK |  |
| 910 | `create_mars_hill_sphere_shell` |  | '' | trace_name=f"Mars: {layer_info['name']}" | 1 | <expr> | FAIL | no legend name set on leader; hover lead does not echo body name; no showlegend=True leader in group |

### `mercury_visualization_shells.py` (Mercury)

| Line | Builder | Sun? | Legend Label | Group | # | Hover lead | Conf. | Notes |
|-----:|---------|:----:|--------------|-------|--:|------------|:-----:|-------|
| 181 | `create_mercury_sodium_tail` |  | trace_name=f"Mercury: {layer_info['name']}" | trace_name=f"Mercury: {layer_info['name']}" | 2 | layer_info=<expr>['description'] | FAIL | hover lead does not echo body name |
| 304 | `create_mercury_magnetosphere_shell` | Y | 'Mercury: Magnetosphere' | 'Mercury: Magnetosphere' | 2 | magnetosphere_text=<expr>[0] | FAIL | hover lead does not echo body name |
| 370 | `create_mercury_magnetosphere_shell` | Y | 'Mercury: Bow Shock' | 'Mercury: Bow Shock' | 2 | bow_shock_text=<expr>[0] | FAIL | hover lead does not echo body name |

### `moon_visualization_shells.py` (Moon)

| Line | Builder | Sun? | Legend Label | Group | # | Hover lead | Conf. | Notes |
|-----:|---------|:----:|--------------|-------|--:|------------|:-----:|-------|
| 64 | `create_moon_inner_core_shell` |  | trace_name=f"Moon: {layer_info['name']}" | trace_name=f"Moon: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |
| 137 | `create_moon_outer_core_shell` |  | trace_name=f"Moon: {layer_info['name']}" | trace_name=f"Moon: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |
| 226 | `create_moon_mantle_shell` |  | trace_name=f"Moon: {layer_info['name']}" | trace_name=f"Moon: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |
| 345 | `create_moon_crust_shell` |  | f"Moon: {layer_info['name']}" | <none> | 1 |   | FAIL | leader trace missing legendgroup attribute |
| 419 | `create_moon_crust_shell` |  | trace_name=f"Moon: {layer_info['name']} (Info)" | trace_name=f"Moon: {layer_info['name']} (Info)" | 1 | <expr> | FAIL | hover lead does not echo body name; no showlegend=True leader in group |
| 485 | `create_moon_exosphere_shell` |  | trace_name=f"Moon: {layer_info['name']}" | trace_name=f"Moon: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |
| 555 | `create_moon_hill_sphere_shell` |  | trace_name='Hill Sphere' | trace_name='Hill Sphere' | 2 | <expr> | FAIL | hover lead does not echo body name |

### `neptune_visualization_shells.py` (Neptune)

| Line | Builder | Sun? | Legend Label | Group | # | Hover lead | Conf. | Notes |
|-----:|---------|:----:|--------------|-------|--:|------------|:-----:|-------|
| 71 | `create_neptune_core_shell` |  | trace_name=f"Neptune: {layer_info['name']}" | trace_name=f"Neptune: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |
| 155 | `create_neptune_mantle_shell` |  | trace_name=f"Neptune: {layer_info['name']}" | trace_name=f"Neptune: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |
| 270 | `create_neptune_cloud_layer_shell` |  | f"Neptune: {layer_info['name']}" | <none> | 1 |   | FAIL | leader trace missing legendgroup attribute |
| 344 | `create_neptune_cloud_layer_shell` |  | trace_name=f"Neptune: {layer_info['name']} (Info)" | trace_name=f"Neptune: {layer_info['name']} (Info)" | 1 | <expr> | FAIL | hover lead does not echo body name; no showlegend=True leader in group |
| 419 | `create_neptune_upper_atmosphere_shell` |  | trace_name=f"Neptune: {layer_info['name']}" | trace_name=f"Neptune: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |
| 567 | `create_neptune_magnetosphere` | Y | 'Neptune: Magnetosphere' | 'Neptune: Magnetosphere' | 3 | magnetosphere_text="Neptune's Magneto... | FAIL | hover lead does not echo body name; multiple showlegend=True traces in same group (2) |
| 663 | `create_neptune_magnetic_poles` |  | 'Neptune: Magnetic Field Center' | <none> | 4 | <expr> | ORPHAN | leader trace missing legendgroup attribute; hover lead does not echo body name; multiple showlegend=True traces in same group (4); (also: function not called anywhere) |
| 950 | `create_neptune_radiation_belts` |  | f"Neptune: {belt['name']}" | f"Neptune: {belt['name']}" | 2 | belt['description'] | FAIL | hover lead does not echo body name |
| 1068 | `create_field_aligned_currents` |  | f"Neptune: {params['name']}" | f"Neptune: {params['name']}" | 2 | params['description'] | FAIL | hover lead does not echo body name |
| 1592 | `create_neptune_ring_system` |  | f"Neptune: {ring_info['name']}" | f"Neptune: {ring_info['name']}" | 2 | ring_info['description'] | FAIL | hover lead does not echo body name |
| 1662 | `create_neptune_hill_sphere_shell` |  | trace_name=f"Neptune: {layer_info['name']}" | trace_name=f"Neptune: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |

### `planet9_visualization_shells.py` (Planet 9)

| Line | Builder | Sun? | Legend Label | Group | # | Hover lead | Conf. | Notes |
|-----:|---------|:----:|--------------|-------|--:|------------|:-----:|-------|
| 111 | `create_planet9_surface_shell` |  | f"Planet 9: {layer_info['name']}" | <none> | 1 |   | FAIL | leader trace missing legendgroup attribute |
| 185 | `create_planet9_surface_shell` |  | trace_name=f"Planet 9: {layer_info['name']} (In... | trace_name=f"Planet 9: {layer_info['name']} (In... | 1 | <expr> | FAIL | hover lead does not echo body name; no showlegend=True leader in group |
| 270 | `create_planet9_hill_sphere_shell` |  | trace_name=f"Planet 9: {layer_info['name']}" | trace_name=f"Planet 9: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |

### `pluto_visualization_shells.py` (Pluto)

| Line | Builder | Sun? | Legend Label | Group | # | Hover lead | Conf. | Notes |
|-----:|---------|:----:|--------------|-------|--:|------------|:-----:|-------|
| 81 | `create_pluto_core_shell` |  | trace_name=f"Pluto: {layer_info['name']}" | trace_name=f"Pluto: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |
| 161 | `create_pluto_mantle_shell` |  | trace_name=f"Pluto: {layer_info['name']}" | trace_name=f"Pluto: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |
| 268 | `create_pluto_crust_shell` |  | f"Pluto: {layer_info['name']}" | <none> | 1 |   | FAIL | leader trace missing legendgroup attribute |
| 342 | `create_pluto_crust_shell` |  | trace_name=f"Pluto: {layer_info['name']} (Info)" | trace_name=f"Pluto: {layer_info['name']} (Info)" | 1 | <expr> | FAIL | hover lead does not echo body name; no showlegend=True leader in group |
| 427 | `create_pluto_haze_layer_shell` |  | trace_name=f"Pluto: {layer_info['name']}" | trace_name=f"Pluto: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |
| 520 | `create_pluto_atmosphere_shell` |  | trace_name=f"Pluto: {layer_info['name']}" | trace_name=f"Pluto: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |
| 605 | `create_pluto_hill_sphere_shell` |  | trace_name=f"Pluto: {layer_info['name']}" | trace_name=f"Pluto: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |

### `saturn_visualization_shells.py` (Saturn)

| Line | Builder | Sun? | Legend Label | Group | # | Hover lead | Conf. | Notes |
|-----:|---------|:----:|--------------|-------|--:|------------|:-----:|-------|
| 84 | `create_saturn_core_shell` |  | trace_name=f"Saturn: {layer_info['name']}" | trace_name=f"Saturn: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |
| 161 | `create_saturn_metallic_hydrogen_shell` |  | trace_name=f"Saturn: {layer_info['name']}" | trace_name=f"Saturn: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |
| 235 | `create_saturn_molecular_hydrogen_shell` |  | trace_name=f"Saturn: {layer_info['name']}" | trace_name=f"Saturn: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |
| 384 | `create_saturn_cloud_layer_shell` |  | f"Saturn: {layer_info['name']}" | <none> | 1 |   | FAIL | leader trace missing legendgroup attribute |
| 458 | `create_saturn_cloud_layer_shell` |  | trace_name=f"Saturn: {layer_info['name']} (Info)" | trace_name=f"Saturn: {layer_info['name']} (Info)" | 1 | <expr> | FAIL | hover lead does not echo body name; no showlegend=True leader in group |
| 562 | `create_saturn_upper_atmosphere_shell` |  | trace_name=f"Saturn: {layer_info['name']}" | trace_name=f"Saturn: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |
| 636 | `create_saturn_magnetosphere` | Y | 'Saturn: Magnetosphere' | 'Saturn: Magnetosphere' | 2 | mag_desc="Saturn has a large magnetos... | OK |  |
| 740 | `create_saturn_enceladus_plasma_torus` |  | 'Saturn: Enceladus Plasma Torus' | 'Saturn: Enceladus Plasma Torus' | 2 | enceladus_text=<expr>[0] | FAIL | hover lead does not echo body name |
| 859 | `create_saturn_radiation_belts` |  | belt_names=<expr>[?] | belt_names=<expr>[?] | 2 | belt_texts=<expr>[?] | OK |  |
| 934 | `create_saturn_hill_sphere_shell` |  | trace_name=f"Saturn: {layer_info['name']}" | trace_name=f"Saturn: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |
| 1152 | `create_saturn_ring_system` |  | f"Saturn: {ring_info['name']}" | f"Saturn: {ring_info['name']}" | 2 | ring_info['description'] | FAIL | hover lead does not echo body name |

### `solar_visualization_shells.py` (Sun)

| Line | Builder | Sun? | Legend Label | Group | # | Hover lead | Conf. | Notes |
|-----:|---------|:----:|--------------|-------|--:|------------|:-----:|-------|
| 927 | `create_sun_gravitational_shell` |  | "Sun's Gravitational Influence" | "Sun's Gravitational Influence" | 2 | <expr> | FAIL | label does not start with 'Sun:'; hover lead does not echo body name |
| 956 | `create_sun_outer_oort_shell` |  | 'Outer Oort Cloud' | 'Outer Oort Cloud' | 2 | <expr> | FAIL | label does not start with 'Sun:'; hover lead does not echo body name |
| 985 | `create_sun_inner_oort_shell` |  | 'Inner Oort Cloud' | 'Inner Oort Cloud' | 2 | <expr> | FAIL | label does not start with 'Sun:'; hover lead does not echo body name |
| 1014 | `create_sun_inner_oort_limit_shell` |  | 'Inner Limit of Oort Cloud' | 'Inner Limit of Oort Cloud' | 2 | <expr> | FAIL | label does not start with 'Sun:'; hover lead does not echo body name |
| 1043 | `create_sun_heliopause_shell` |  | 'Solar Wind Heliopause' | 'Solar Wind Heliopause' | 2 | <expr> | FAIL | label does not start with 'Sun:'; hover lead does not echo body name |
| 1072 | `create_sun_termination_shock_shell` |  | 'Solar Wind Termination Shock' | 'Solar Wind Termination Shock' | 2 | <expr> | FAIL | label does not start with 'Sun:'; hover lead does not echo body name |
| 1101 | `create_sun_outer_corona_shell` |  | 'Sun: Outer Corona' | 'Sun: Outer Corona' | 2 | <expr> | FAIL | hover lead does not echo body name |
| 1130 | `create_sun_inner_corona_shell` |  | 'Sun: Inner Corona' | 'Sun: Inner Corona' | 2 | <expr> | FAIL | hover lead does not echo body name |
| 1163 | `create_sun_streamer_belt_shell` |  | 'Sun: Streamer Belt (Visible Corona)' | 'Sun: Streamer Belt (Visible Corona)' | 2 | <expr> | FAIL | hover lead does not echo body name |
| 1201 | `create_sun_roche_limit_shell` |  | 'Sun: Roche Limit (Comets)' | 'Sun: Roche Limit (Comets)' | 2 | <expr> | FAIL | hover lead does not echo body name |
| 1236 | `create_sun_alfven_surface_shell` |  | 'Sun: Alfven Surface' | 'Sun: Alfven Surface' | 2 | <expr> | FAIL | hover lead does not echo body name |
| 1265 | `create_sun_chromosphere_shell` |  | 'Sun: Chromosphere' | 'Sun: Chromosphere' | 2 | <expr> | FAIL | hover lead does not echo body name |
| 1294 | `create_sun_photosphere_shell` |  | 'Sun: Photosphere' | 'Sun: Photosphere' | 2 | <expr> | FAIL | hover lead does not echo body name |
| 1323 | `create_sun_radiative_shell` |  | 'Sun: Radiative Zone' | 'Sun: Radiative Zone' | 2 | <expr> | FAIL | hover lead does not echo body name |
| 1352 | `create_sun_core_shell` |  | 'Sun: Core' | 'Sun: Core' | 2 | <expr> | FAIL | hover lead does not echo body name |
| 1426 | `create_sun_hills_cloud_torus` |  | 'Hills Cloud (Inner Oort - Toroidal)' | 'Hills Cloud (Inner Oort - Toroidal)' | 2 | <expr> | FAIL | label does not start with 'Sun:'; hover lead does not echo body name |
| 1507 | `create_sun_outer_oort_clumpy` |  | 'Outer Oort Cloud (Clumpy)' | 'Outer Oort Cloud (Clumpy)' | 2 | <expr> | FAIL | label does not start with 'Sun:'; hover lead does not echo body name |
| 1567 | `create_sun_galactic_tide` |  | 'Galactic Tide Region' | 'Galactic Tide Region' | 2 | <expr> | FAIL | label does not start with 'Sun:'; hover lead does not echo body name |

### `uranus_visualization_shells.py` (Uranus)

| Line | Builder | Sun? | Legend Label | Group | # | Hover lead | Conf. | Notes |
|-----:|---------|:----:|--------------|-------|--:|------------|:-----:|-------|
| 63 | `create_uranus_core_shell` |  | trace_name=f"Uranus: {layer_info['name']}" | trace_name=f"Uranus: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |
| 140 | `create_uranus_mantle_shell` |  | trace_name=f"Uranus: {layer_info['name']}" | trace_name=f"Uranus: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |
| 257 | `create_uranus_cloud_layer_shell` |  | f"Uranus: {layer_info['name']}" | <none> | 1 |   | FAIL | leader trace missing legendgroup attribute |
| 331 | `create_uranus_cloud_layer_shell` |  | trace_name=f"Uranus: {layer_info['name']} (Info)" | trace_name=f"Uranus: {layer_info['name']} (Info)" | 1 | <expr> | FAIL | hover lead does not echo body name; no showlegend=True leader in group |
| 404 | `create_uranus_upper_atmosphere_shell` |  | trace_name=f"Uranus: {layer_info['name']}" | trace_name=f"Uranus: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |
| 517 | `create_uranus_magnetosphere` | Y | trace_name='Uranus: Magnetosphere' | trace_name='Uranus: Magnetosphere' | 2 | description="Uranus's Magnetosphere: ... | OK |  |
| 671 | `create_uranus_radiation_belts` |  | belt_names=<expr>[?] | belt_names=<expr>[?] | 2 | belt_texts=<expr>[?] | OK |  |
| 1042 | `create_uranus_ring_system` |  | f"Uranus: {ring_info['name']}" | f"Uranus: {ring_info['name']}" | 2 | ring_info['description'] | FAIL | hover lead does not echo body name |
| 1119 | `create_uranus_hill_sphere_shell` |  | trace_name=f"Uranus: {layer_info['name']}" | trace_name=f"Uranus: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |

### `venus_visualization_shells.py` (Venus)

| Line | Builder | Sun? | Legend Label | Group | # | Hover lead | Conf. | Notes |
|-----:|---------|:----:|--------------|-------|--:|------------|:-----:|-------|
| 69 | `create_venus_core_shell` |  | trace_name=f"Venus: {layer_info['name']}" | trace_name=f"Venus: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |
| 135 | `create_venus_mantle_shell` |  | trace_name=f"Venus: {layer_info['name']}" | trace_name=f"Venus: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |
| 226 | `create_venus_crust_shell` |  | f"Venus: {layer_info['name']}" | <none> | 1 |   | FAIL | leader trace missing legendgroup attribute |
| 300 | `create_venus_crust_shell` |  | trace_name=f"Venus: {layer_info['name']} (Info)" | trace_name=f"Venus: {layer_info['name']} (Info)" | 1 | <expr> | FAIL | hover lead does not echo body name; no showlegend=True leader in group |
| 359 | `create_venus_atmosphere_shell` |  | trace_name=f"Venus: {layer_info['name']}" | trace_name=f"Venus: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |
| 467 | `create_venus_upper_atmosphere_shell` |  | trace_name=f"Venus: {layer_info['name']}" | trace_name=f"Venus: {layer_info['name']}" | 2 | <expr> | FAIL | hover lead does not echo body name |
| 632 | `create_venus_magnetosphere_shell` | Y | 'Venus: Magnetosphere' | 'Venus: Magnetosphere' | 2 | magnetosphere_text=<expr>[0] | FAIL | hover lead does not echo body name |
| 702 | `create_venus_magnetosphere_shell` | Y | 'Venus: Bow Shock' | 'Venus: Bow Shock' | 2 | bow_shock_text=<expr>[0] | FAIL | hover lead does not echo body name |
| 766 | `create_venus_hill_sphere_shell` |  | 'Venus: Hill Sphere' | 'Venus: Hill Sphere' | 2 | <expr> | FAIL | hover lead does not echo body name |

---

## Section 4. Findings -- Non-Conforming Entries by Violation Type

### (also: function not called anywhere)

| File | Line | Builder | Legend Label |
|------|-----:|---------|--------------|
| `neptune_visualization_shells.py` | 663 | `create_neptune_magnetic_poles` | 'Neptune: Magnetic Field Center' |

### hover lead does not echo body name

| File | Line | Builder | Legend Label |
|------|-----:|---------|--------------|
| `earth_visualization_shells.py` | 67 | `create_earth_inner_core_shell` | trace_name=f"Earth: {layer_info['name']}" |
| `earth_visualization_shells.py` | 139 | `create_earth_outer_core_shell` | trace_name=f"Earth: {layer_info['name']}" |
| `earth_visualization_shells.py` | 209 | `create_earth_lower_mantle_shell` | trace_name=f"Earth: {layer_info['name']}" |
| `earth_visualization_shells.py` | 279 | `create_earth_upper_mantle_shell` | trace_name=f"Earth: {layer_info['name']}" |
| `earth_visualization_shells.py` | 446 | `create_earth_crust_shell` | trace_name=f"Earth: {layer_info['name']} (Info)" |
| `earth_visualization_shells.py` | 503 | `create_earth_atmosphere_shell` | trace_name=f"Earth: {layer_info['name']}" |
| `earth_visualization_shells.py` | 575 | `create_earth_upper_atmosphere_shell` | trace_name=f"Earth: {layer_info['name']}" |
| `earth_visualization_shells.py` | 678 | `create_earth_magnetosphere_shell` | 'Earth: Magnetosphere' |
| `earth_visualization_shells.py` | 748 | `create_earth_magnetosphere_shell` | 'Earth: Bow Shock' |
| `earth_visualization_shells.py` | 835 | `create_earth_magnetosphere_shell` | belt_names=<expr>[?] |
| `earth_visualization_shells.py` | 967 | `create_earth_leo_shell` | 'Earth: Low Earth Orbit (LEO)' |
| `earth_visualization_shells.py` | 1078 | `create_earth_geostationary_belt_shell` | 'Earth: Geostationary Belt (GEO)' |
| `earth_visualization_shells.py` | 1146 | `create_earth_hill_sphere_shell` | 'Earth: Hill Sphere' |
| `eris_visualization_shells.py` | 91 | `create_eris_core_shell` | trace_name=f"Eris: {layer_info['name']}" |
| `eris_visualization_shells.py` | 162 | `create_eris_mantle_shell` | trace_name=f"Eris: {layer_info['name']}" |
| `eris_visualization_shells.py` | 335 | `create_eris_crust_shell` | trace_name=f"Eris: {layer_info['name']} (Info)" |
| `eris_visualization_shells.py` | 410 | `create_eris_atmosphere_shell` | trace_name=f"Eris: {layer_info['name']}" |
| `eris_visualization_shells.py` | 494 | `create_eris_hill_sphere_shell` | trace_name=f"Eris: {layer_info['name']}" |
| `jupiter_visualization_shells.py` | 107 | `create_jupiter_core_shell` | trace_name=f"Jupiter: {layer_info['name']}" |
| `jupiter_visualization_shells.py` | 177 | `create_jupiter_metallic_hydrogen_shell` | trace_name=f"Jupiter: {layer_info['name']}" |
| `jupiter_visualization_shells.py` | 249 | `create_jupiter_molecular_hydrogen_shell` | trace_name=f"Jupiter: {layer_info['name']}" |
| `jupiter_visualization_shells.py` | 420 | `create_jupiter_cloud_layer_shell` | trace_name=f"Jupiter: {layer_info['name']} (Info)" |
| `jupiter_visualization_shells.py` | 479 | `create_jupiter_upper_atmosphere_shell` | trace_name=f"Jupiter: {layer_info['name']}" |
| `jupiter_visualization_shells.py` | 633 | `create_jupiter_io_plasma_torus` | 'Jupiter: Io Plasma Torus' |
| `jupiter_visualization_shells.py` | 789 | `create_jupiter_hill_sphere_shell` | trace_name=f"Jupiter: {layer_info['name']}" |
| `jupiter_visualization_shells.py` | 954 | `create_jupiter_ring_system` | f"Jupiter: {ring_info['name']}" |
| `mars_visualization_shells.py` | 85 | `create_mars_inner_core_shell` | trace_name=f"Mars: {layer_info['name']}" |
| `mars_visualization_shells.py` | 170 | `create_mars_outer_core_shell` | trace_name=f"Mars: {layer_info['name']}" |
| `mars_visualization_shells.py` | 238 | `create_mars_mantle_shell` | trace_name=f"Mars: {layer_info['name']}" |
| `mars_visualization_shells.py` | 405 | `create_mars_crust_shell` | trace_name=f"Mars: {layer_info['name']} (Info)" |
| `mars_visualization_shells.py` | 464 | `create_mars_atmosphere_shell` | trace_name=f"Mars: {layer_info['name']}" |
| `mars_visualization_shells.py` | 546 | `create_mars_upper_atmosphere_shell` | trace_name=f"Mars: {layer_info['name']}" |
| `mars_visualization_shells.py` | 718 | `create_mars_magnetosphere_shell` | 'Mars: Bow Shock' |
| `mars_visualization_shells.py` | 806 | `create_mars_magnetosphere_shell` | 'Mars: Crustal Magnetic Fields' |
| `mars_visualization_shells.py` | 910 | `create_mars_hill_sphere_shell` | '' |
| `mercury_visualization_shells.py` | 181 | `create_mercury_sodium_tail` | trace_name=f"Mercury: {layer_info['name']}" |
| `mercury_visualization_shells.py` | 304 | `create_mercury_magnetosphere_shell` | 'Mercury: Magnetosphere' |
| `mercury_visualization_shells.py` | 370 | `create_mercury_magnetosphere_shell` | 'Mercury: Bow Shock' |
| `moon_visualization_shells.py` | 64 | `create_moon_inner_core_shell` | trace_name=f"Moon: {layer_info['name']}" |
| `moon_visualization_shells.py` | 137 | `create_moon_outer_core_shell` | trace_name=f"Moon: {layer_info['name']}" |
| `moon_visualization_shells.py` | 226 | `create_moon_mantle_shell` | trace_name=f"Moon: {layer_info['name']}" |
| `moon_visualization_shells.py` | 419 | `create_moon_crust_shell` | trace_name=f"Moon: {layer_info['name']} (Info)" |
| `moon_visualization_shells.py` | 485 | `create_moon_exosphere_shell` | trace_name=f"Moon: {layer_info['name']}" |
| `moon_visualization_shells.py` | 555 | `create_moon_hill_sphere_shell` | trace_name='Hill Sphere' |
| `neptune_visualization_shells.py` | 71 | `create_neptune_core_shell` | trace_name=f"Neptune: {layer_info['name']}" |
| `neptune_visualization_shells.py` | 155 | `create_neptune_mantle_shell` | trace_name=f"Neptune: {layer_info['name']}" |
| `neptune_visualization_shells.py` | 344 | `create_neptune_cloud_layer_shell` | trace_name=f"Neptune: {layer_info['name']} (Info)" |
| `neptune_visualization_shells.py` | 419 | `create_neptune_upper_atmosphere_shell` | trace_name=f"Neptune: {layer_info['name']}" |
| `neptune_visualization_shells.py` | 567 | `create_neptune_magnetosphere` | 'Neptune: Magnetosphere' |
| `neptune_visualization_shells.py` | 663 | `create_neptune_magnetic_poles` | 'Neptune: Magnetic Field Center' |
| `neptune_visualization_shells.py` | 950 | `create_neptune_radiation_belts` | f"Neptune: {belt['name']}" |
| `neptune_visualization_shells.py` | 1068 | `create_field_aligned_currents` | f"Neptune: {params['name']}" |
| `neptune_visualization_shells.py` | 1592 | `create_neptune_ring_system` | f"Neptune: {ring_info['name']}" |
| `neptune_visualization_shells.py` | 1662 | `create_neptune_hill_sphere_shell` | trace_name=f"Neptune: {layer_info['name']}" |
| `planet9_visualization_shells.py` | 185 | `create_planet9_surface_shell` | trace_name=f"Planet 9: {layer_info['name']} (Info)" |
| `planet9_visualization_shells.py` | 270 | `create_planet9_hill_sphere_shell` | trace_name=f"Planet 9: {layer_info['name']}" |
| `pluto_visualization_shells.py` | 81 | `create_pluto_core_shell` | trace_name=f"Pluto: {layer_info['name']}" |
| `pluto_visualization_shells.py` | 161 | `create_pluto_mantle_shell` | trace_name=f"Pluto: {layer_info['name']}" |
| `pluto_visualization_shells.py` | 342 | `create_pluto_crust_shell` | trace_name=f"Pluto: {layer_info['name']} (Info)" |
| `pluto_visualization_shells.py` | 427 | `create_pluto_haze_layer_shell` | trace_name=f"Pluto: {layer_info['name']}" |
| `pluto_visualization_shells.py` | 520 | `create_pluto_atmosphere_shell` | trace_name=f"Pluto: {layer_info['name']}" |
| `pluto_visualization_shells.py` | 605 | `create_pluto_hill_sphere_shell` | trace_name=f"Pluto: {layer_info['name']}" |
| `saturn_visualization_shells.py` | 84 | `create_saturn_core_shell` | trace_name=f"Saturn: {layer_info['name']}" |
| `saturn_visualization_shells.py` | 161 | `create_saturn_metallic_hydrogen_shell` | trace_name=f"Saturn: {layer_info['name']}" |
| `saturn_visualization_shells.py` | 235 | `create_saturn_molecular_hydrogen_shell` | trace_name=f"Saturn: {layer_info['name']}" |
| `saturn_visualization_shells.py` | 458 | `create_saturn_cloud_layer_shell` | trace_name=f"Saturn: {layer_info['name']} (Info)" |
| `saturn_visualization_shells.py` | 562 | `create_saturn_upper_atmosphere_shell` | trace_name=f"Saturn: {layer_info['name']}" |
| `saturn_visualization_shells.py` | 740 | `create_saturn_enceladus_plasma_torus` | 'Saturn: Enceladus Plasma Torus' |
| `saturn_visualization_shells.py` | 934 | `create_saturn_hill_sphere_shell` | trace_name=f"Saturn: {layer_info['name']}" |
| `saturn_visualization_shells.py` | 1152 | `create_saturn_ring_system` | f"Saturn: {ring_info['name']}" |
| `solar_visualization_shells.py` | 927 | `create_sun_gravitational_shell` | "Sun's Gravitational Influence" |
| `solar_visualization_shells.py` | 956 | `create_sun_outer_oort_shell` | 'Outer Oort Cloud' |
| `solar_visualization_shells.py` | 985 | `create_sun_inner_oort_shell` | 'Inner Oort Cloud' |
| `solar_visualization_shells.py` | 1014 | `create_sun_inner_oort_limit_shell` | 'Inner Limit of Oort Cloud' |
| `solar_visualization_shells.py` | 1043 | `create_sun_heliopause_shell` | 'Solar Wind Heliopause' |
| `solar_visualization_shells.py` | 1072 | `create_sun_termination_shock_shell` | 'Solar Wind Termination Shock' |
| `solar_visualization_shells.py` | 1101 | `create_sun_outer_corona_shell` | 'Sun: Outer Corona' |
| `solar_visualization_shells.py` | 1130 | `create_sun_inner_corona_shell` | 'Sun: Inner Corona' |
| `solar_visualization_shells.py` | 1163 | `create_sun_streamer_belt_shell` | 'Sun: Streamer Belt (Visible Corona)' |
| `solar_visualization_shells.py` | 1201 | `create_sun_roche_limit_shell` | 'Sun: Roche Limit (Comets)' |
| `solar_visualization_shells.py` | 1236 | `create_sun_alfven_surface_shell` | 'Sun: Alfven Surface' |
| `solar_visualization_shells.py` | 1265 | `create_sun_chromosphere_shell` | 'Sun: Chromosphere' |
| `solar_visualization_shells.py` | 1294 | `create_sun_photosphere_shell` | 'Sun: Photosphere' |
| `solar_visualization_shells.py` | 1323 | `create_sun_radiative_shell` | 'Sun: Radiative Zone' |
| `solar_visualization_shells.py` | 1352 | `create_sun_core_shell` | 'Sun: Core' |
| `solar_visualization_shells.py` | 1426 | `create_sun_hills_cloud_torus` | 'Hills Cloud (Inner Oort - Toroidal)' |
| `solar_visualization_shells.py` | 1507 | `create_sun_outer_oort_clumpy` | 'Outer Oort Cloud (Clumpy)' |
| `solar_visualization_shells.py` | 1567 | `create_sun_galactic_tide` | 'Galactic Tide Region' |
| `uranus_visualization_shells.py` | 63 | `create_uranus_core_shell` | trace_name=f"Uranus: {layer_info['name']}" |
| `uranus_visualization_shells.py` | 140 | `create_uranus_mantle_shell` | trace_name=f"Uranus: {layer_info['name']}" |
| `uranus_visualization_shells.py` | 331 | `create_uranus_cloud_layer_shell` | trace_name=f"Uranus: {layer_info['name']} (Info)" |
| `uranus_visualization_shells.py` | 404 | `create_uranus_upper_atmosphere_shell` | trace_name=f"Uranus: {layer_info['name']}" |
| `uranus_visualization_shells.py` | 1042 | `create_uranus_ring_system` | f"Uranus: {ring_info['name']}" |
| `uranus_visualization_shells.py` | 1119 | `create_uranus_hill_sphere_shell` | trace_name=f"Uranus: {layer_info['name']}" |
| `venus_visualization_shells.py` | 69 | `create_venus_core_shell` | trace_name=f"Venus: {layer_info['name']}" |
| `venus_visualization_shells.py` | 135 | `create_venus_mantle_shell` | trace_name=f"Venus: {layer_info['name']}" |
| `venus_visualization_shells.py` | 300 | `create_venus_crust_shell` | trace_name=f"Venus: {layer_info['name']} (Info)" |
| `venus_visualization_shells.py` | 359 | `create_venus_atmosphere_shell` | trace_name=f"Venus: {layer_info['name']}" |
| `venus_visualization_shells.py` | 467 | `create_venus_upper_atmosphere_shell` | trace_name=f"Venus: {layer_info['name']}" |
| `venus_visualization_shells.py` | 632 | `create_venus_magnetosphere_shell` | 'Venus: Magnetosphere' |
| `venus_visualization_shells.py` | 702 | `create_venus_magnetosphere_shell` | 'Venus: Bow Shock' |
| `venus_visualization_shells.py` | 766 | `create_venus_hill_sphere_shell` | 'Venus: Hill Sphere' |

### label does not start with 'Sun:'

| File | Line | Builder | Legend Label |
|------|-----:|---------|--------------|
| `solar_visualization_shells.py` | 927 | `create_sun_gravitational_shell` | "Sun's Gravitational Influence" |
| `solar_visualization_shells.py` | 956 | `create_sun_outer_oort_shell` | 'Outer Oort Cloud' |
| `solar_visualization_shells.py` | 985 | `create_sun_inner_oort_shell` | 'Inner Oort Cloud' |
| `solar_visualization_shells.py` | 1014 | `create_sun_inner_oort_limit_shell` | 'Inner Limit of Oort Cloud' |
| `solar_visualization_shells.py` | 1043 | `create_sun_heliopause_shell` | 'Solar Wind Heliopause' |
| `solar_visualization_shells.py` | 1072 | `create_sun_termination_shock_shell` | 'Solar Wind Termination Shock' |
| `solar_visualization_shells.py` | 1426 | `create_sun_hills_cloud_torus` | 'Hills Cloud (Inner Oort - Toroidal)' |
| `solar_visualization_shells.py` | 1507 | `create_sun_outer_oort_clumpy` | 'Outer Oort Cloud (Clumpy)' |
| `solar_visualization_shells.py` | 1567 | `create_sun_galactic_tide` | 'Galactic Tide Region' |

### leader trace missing legendgroup attribute

| File | Line | Builder | Legend Label |
|------|-----:|---------|--------------|
| `comet_visualization_shells.py` | 457 | `create_comet_nucleus` | f"{comet_name}: Nucleus" |
| `comet_visualization_shells.py` | 550 | `create_maps_disintegration_marker` | 'MAPS: Disintegration' |
| `comet_visualization_shells.py` | 1760 | `add_comet_tails_to_figure` | 'MAPS: Nucleus (disintegrated April 4, 2026)' |
| `earth_visualization_shells.py` | 372 | `create_earth_crust_shell` | f"Earth: {layer_info['name']}" |
| `eris_visualization_shells.py` | 261 | `create_eris_crust_shell` | f"Eris: {layer_info['name']}" |
| `jupiter_visualization_shells.py` | 346 | `create_jupiter_cloud_layer_shell` | f"Jupiter: {layer_info['name']}" |
| `mars_visualization_shells.py` | 331 | `create_mars_crust_shell` | f"Mars: {layer_info['name']}" |
| `moon_visualization_shells.py` | 345 | `create_moon_crust_shell` | f"Moon: {layer_info['name']}" |
| `neptune_visualization_shells.py` | 270 | `create_neptune_cloud_layer_shell` | f"Neptune: {layer_info['name']}" |
| `neptune_visualization_shells.py` | 663 | `create_neptune_magnetic_poles` | 'Neptune: Magnetic Field Center' |
| `planet9_visualization_shells.py` | 111 | `create_planet9_surface_shell` | f"Planet 9: {layer_info['name']}" |
| `pluto_visualization_shells.py` | 268 | `create_pluto_crust_shell` | f"Pluto: {layer_info['name']}" |
| `saturn_visualization_shells.py` | 384 | `create_saturn_cloud_layer_shell` | f"Saturn: {layer_info['name']}" |
| `uranus_visualization_shells.py` | 257 | `create_uranus_cloud_layer_shell` | f"Uranus: {layer_info['name']}" |
| `venus_visualization_shells.py` | 226 | `create_venus_crust_shell` | f"Venus: {layer_info['name']}" |

### multiple showlegend=True traces in same group (2)

| File | Line | Builder | Legend Label |
|------|-----:|---------|--------------|
| `neptune_visualization_shells.py` | 567 | `create_neptune_magnetosphere` | 'Neptune: Magnetosphere' |

### multiple showlegend=True traces in same group (4)

| File | Line | Builder | Legend Label |
|------|-----:|---------|--------------|
| `neptune_visualization_shells.py` | 663 | `create_neptune_magnetic_poles` | 'Neptune: Magnetic Field Center' |

### multiple showlegend=True traces in same group (7)

| File | Line | Builder | Legend Label |
|------|-----:|---------|--------------|
| `comet_visualization_shells.py` | 1760 | `add_comet_tails_to_figure` | 'MAPS: Nucleus (disintegrated April 4, 2026)' |

### no legend name set on leader

| File | Line | Builder | Legend Label |
|------|-----:|---------|--------------|
| `mars_visualization_shells.py` | 910 | `create_mars_hill_sphere_shell` | '' |

### no showlegend=True leader in group

| File | Line | Builder | Legend Label |
|------|-----:|---------|--------------|
| `comet_visualization_shells.py` | 716 | `create_maps_ghost_tail_trace` | '' |
| `earth_visualization_shells.py` | 446 | `create_earth_crust_shell` | trace_name=f"Earth: {layer_info['name']} (Info)" |
| `eris_visualization_shells.py` | 335 | `create_eris_crust_shell` | trace_name=f"Eris: {layer_info['name']} (Info)" |
| `jupiter_visualization_shells.py` | 420 | `create_jupiter_cloud_layer_shell` | trace_name=f"Jupiter: {layer_info['name']} (Info)" |
| `mars_visualization_shells.py` | 405 | `create_mars_crust_shell` | trace_name=f"Mars: {layer_info['name']} (Info)" |
| `mars_visualization_shells.py` | 806 | `create_mars_magnetosphere_shell` | 'Mars: Crustal Magnetic Fields' |
| `mars_visualization_shells.py` | 910 | `create_mars_hill_sphere_shell` | '' |
| `moon_visualization_shells.py` | 419 | `create_moon_crust_shell` | trace_name=f"Moon: {layer_info['name']} (Info)" |
| `neptune_visualization_shells.py` | 344 | `create_neptune_cloud_layer_shell` | trace_name=f"Neptune: {layer_info['name']} (Info)" |
| `planet9_visualization_shells.py` | 185 | `create_planet9_surface_shell` | trace_name=f"Planet 9: {layer_info['name']} (Info)" |
| `pluto_visualization_shells.py` | 342 | `create_pluto_crust_shell` | trace_name=f"Pluto: {layer_info['name']} (Info)" |
| `saturn_visualization_shells.py` | 458 | `create_saturn_cloud_layer_shell` | trace_name=f"Saturn: {layer_info['name']} (Info)" |
| `uranus_visualization_shells.py` | 331 | `create_uranus_cloud_layer_shell` | trace_name=f"Uranus: {layer_info['name']} (Info)" |
| `venus_visualization_shells.py` | 300 | `create_venus_crust_shell` | trace_name=f"Venus: {layer_info['name']} (Info)" |

---

## Section 5. Ambiguous Cases Needing Judgment

Legend entries with three or more traces and no rule violation. Per the tiebreaker, the question is: are the traces in this group **components of one structure** (keep grouped) or **functionally different structures** (split into separate legend entries)?

*No ambiguous cases detected. Either every multi-trace group violated a rule (caught in Section 4) or every group has exactly 2 traces (geometry + info marker, the standard pattern).*

---

## Section 6. Out-of-Scope / Known Issues

Things the inventory cannot detect mechanically but are tracked for downstream phases:

- **Item 47a (Neptune arc superposition):** Adams, Le Verrier, and Galle arc markers occupy the same coordinate. This is a position bug, not a legendgroup bug. D3.2 handles it.
- **Item 47b (Neptune ring marker superposition):** Lassell and Arago ring markers superimposed. Same category as 47a.
- **Items 43, 44 (hovertext truncation):** `\n` newlines in hover text strings render as backslash-n in Plotly; should be `<br>`. Not visible in this inventory (we only capture the first line). The sweep can normalize newlines wherever it touches hover strings.
- **Loop-generated traces collapsed to one row.** Several builders (Earth radiation belts, Neptune radiation belts, Neptune FAC, Mars crustal fields, ring systems) use a `for` loop to create N traces, each with a dynamic name from `belt_names[i]`, `ring_info['name']`, etc. The script sees one trace constructor inside the loop and aggregates it as a single legend entry. At runtime, N legend entries are produced. The sweep should still treat the loop body as a single edit site -- whatever fix applies to one belt applies to all -- but reviewers should know the runtime legend has more entries than this table.
- **Script false positives on Rule 2.** Some FAIL entries are script-limitation false positives. When the hover text is a multi-line string built via implicit string concatenation inside a list literal (`text=["Foo bar...<br>" "continued..."]`), the script's `render_expr` returns `<expr>` and the body-name check fails. The runtime hover text may in fact start with the body name (e.g., line 604 Neptune magnetic center starts with "Neptune's magnetic field center is offset..."). These are flagged with `<expr>` in the hover-lead column and should be verified manually during the sweep -- but the safest action regardless is to prepend the legend label explicitly, which removes the ambiguity.
- **Orphan functions (dead code).** A project-wide grep with zero-reference filter identified one true orphan function: `create_neptune_magnetic_poles` in `neptune_visualization_shells.py`. This function still defines four `showlegend=True` traces (magnetic center, axis line, north pole, south pole) -- the old pre-D2 pattern that Option C replaced. The live dispatch no longer reaches this function; the diamond marker is now created inline inside `create_neptune_magnetosphere` at line 604. The orphan entries are tagged with conformance `ORPHAN` in the per-file tables. Recommend: remove the orphan function in the D3.1 sweep, since dead code in source confuses both future readers and automated tooling like this inventory.
- **Hover-echo check is best-effort.** The script flags entries where the leader's hover lead does not contain the body name. It correctly skips entries where hover is intentionally suppressed (`hoverinfo='skip'` or `'none'`). For entries with f-string hover templates the script cannot resolve to a literal, the check looks at the rendered f-string template; if the template variable resolves to something like `layer_info['description']`, the script cannot tell whether the resulting string starts with the body name. Manual review at the source is required for those rows; the per-trace CSV preserves enough context to do that quickly.
- **Crust shell pattern.** Several `*_crust_shell` builders (Earth, Venus, Mars, Pluto, Eris, Jupiter, Saturn, Uranus, Neptune, Moon) follow an older pattern where the `go.Mesh3d` surface has `name` set but `legendgroup` omitted, and the paired info marker uses a different legendgroup with `(Info)` appended. These show up as two separate legend entries in this inventory rather than one. The sweep should add a shared `legendgroup` to the surface trace and remove the `(Info)` suffix from the info marker.

---

## Appendix A. Raw Data Files

- `inventory_per_trace.csv` -- one row per trace constructor call. Raw working data for the sweep manifest.
- `inventory_per_legend_entry.csv` -- one row per legend entry (grouped by `legendgroup`). Same content as Section 3 tables.

---

*Module updated: May 2026 with Anthropic's Claude Opus 4.7*
*Paloma's Orrery | palomasorrery.com*
