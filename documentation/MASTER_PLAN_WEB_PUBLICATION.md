# MASTER PLAN: Web Publication of Paloma's Orrery

**Status:** Draft v5 — ready for review round.
**Base:** main @ `d6c8c42`, gallery @ `89c8bf30`
**Date begun:** July 3, 2026
**Participants:** Tony Quintanilla, Claude Opus 4.6, Claude Opus 4.8, Claude Fable 5

---

## §1 — Architectural Constraints (settled)

These are not options. They are facts that constrain every downstream decision,
drawn from the Opus 4.8 convergence handoff with fetched sources (July 2, 2026).

**The site never fetches Horizons.** JPL terms require one request at a time and
prohibit website embedding (NASA CORS policy). This applies to every publication
path — server, browser, all of them. The cache is the entire served surface.

**Three-tier cache, all offline-populated (orrery domain):**

- Tier 1 — Scheduled standard catalog. Sequential batch job refreshes a fixed
  set of object/center pairs, rolling the date window forward. Size-stable.
- Tier 2 — Curated specials, define-once. Encounters, perihelia, close
  approaches. Write-once/read-forever. Fetched by Tony via the desktop app.
- Tier 3 — User requests, manually curated. Tony produces and caches offline;
  the user is notified when ready. Whether fulfilled requests persist in the
  shared cache is a dial Tony sets (see §7).

There is no server-side fetch infrastructure to build.

**The GUI declares the envelope.** A cache miss is something the UI will not let
you request — not a runtime error, not a silent wrong plot. Coverage is a
visible, honest boundary. This is "Show the Envelope of the Unknowable" applied
at product scale. The envelope extends to content type: at launch, static scenes
are freely available; animations are offered as curated preset exports
(encounters, comets, close approaches, satellites, planets). Live animation
assembly is a dial to open later.

**Two hosting substrates, not one:**

- **Cache:** static files on GitHub Pages (or R2 when size/bandwidth requires).
  Gallery is ~479 MB against Pages' 1 GB ceiling — headroom is shared between
  gallery growth and the cache. A separate Pages project site (each gets its
  own 1 GB) is an option.
- **App:** depends on the server-vs-serverless decision (see §7). A server
  (Dash on HF Spaces/Render) runs a Python process. A serverless path (Pyodide)
  runs Python in the browser with no server at all.

**Assemblers read cache through the coverage-index abstraction from day one** —
never by opening data files directly — so cache restructuring cannot break
the assemblers. The coverage index is a **solar system concept** where the
envelope is complex (object/center/date-range matrix). Other domains declare
their bounds simply: stars state distance and magnitude limits, orbital
parameters are always available, Earth system lists available scenarios.

---

## §2 — The Fork Decision (settled)

The web GUI is a fork, not a replacement. The desktop tkinter app continues as
the power-user channel with full capability (live Horizons, animation export,
KML/KMZ). Both GUIs are thin harvesters feeding shared assemblers (§3).

**Shared computation layer — verified at HEAD (`d6c8c42`):**

Six modules are import-clean (zero tkinter references): `idealized_orbits.py`,
`planet_visualization.py`, `visualization_utils.py`, `orbit_data_manager.py`,
`constants_new.py`, `shell_configs.py`.

**Two named seams:**

1. `celestial_objects.py` — data half (`OBJECT_DEFINITIONS`) is import-clean.
   Selection/instance half is tk-shaped: `build_objects_list()` injects tk vars,
   `build_shell_checkboxes()` takes GUI-construction parameters. The web fork
   imports the data; it supplies its own selection-state injection.

2. `palomas_orrery_helpers.py` — imports tkinter directly and carries computation
   the assembler will want: `calculate_planet9_position_on_orbit`, `rotate_points2`,
   `calculate_axis_range`. Fix: split computation from GUI helpers. Natural
   companion to L-026 (CRLF → LF).

---

## §3 — The Shared Assembler Architecture (settled)

**One shared assembler per domain, both GUIs as thin harvesters.**

**The pattern — three stages:**

1. **Harvest.** The GUI reads its inputs and produces a scene spec — a plain
   data document describing what to build. This is the only GUI-specific code.
2. **Assemble.** A shared assembler takes the spec plus cached data (through the
   coverage-index abstraction) and builds the output. No tkinter, no network
   calls, no knowledge of which GUI produced the spec.
3. **Display.** The GUI takes the output and presents it.

**The assembler is new code.** The original desktop code is the recipe reference.
The assembler is written fresh against the scene-spec vocabulary, calling the
shared computation engines. The original code is archived for reference or
reconstruction.

**Per-domain migration tails, not a single Phase 7.** The desktop migrates onto
each assembler right after that assembler validates — shrinking each drift
window to weeks instead of months. Any orchestration change to the desktop
during the build gets a ledger tag ("assembler-must-inherit"), making drift
enumerable rather than discovered. This dissolves the parallel-pipeline risk the
plan works hard to escape.

**The parallel-pipeline discipline is satisfied at every layer:** computation
engines shared, orchestration shared (one assembler per domain), only the
input-reading glue is per-GUI.

---

## §4 — Four Visualization Domains

### §4a — Solar System (the main build)

**Current GUI:** `palomas_orrery.py` (11,110 lines at HEAD). `plot_objects` and
`animate_objects` are the orchestration functions.

**Computation engines:** `idealized_orbits.py`, `planet_visualization.py`,
`visualization_utils.py`, `orbit_data_manager.py`, `shell_configs.py`,
`celestial_objects.py`, `constants_new.py`, plus shell visualization modules,
`spacecraft_encounters.py`, `close_approach_data.py`, `exoplanet_orbits.py`,
`star_sphere_builder.py`, `apsidal_markers.py`.

**Output:** Plotly 3D interactive figures.

**Web assembler:** Scene spec (objects, center, dates, display options, content
type static/animation) → assembler → Plotly figure. Animation/static
consolidation is inherent — the assembler handles both via a content-type tag.

**Cache model:** Three-tier (§1). Coverage index drives the envelope.

### §4b — Stars

**Current GUI:** `star_visualization_gui.py`. Launches HR diagram and
planetarium scripts as subprocesses; results return via `plot_data_exchange.py`.

**Pipeline scripts:** `hr_diagram_distance.py`, `hr_diagram_apparent_magnitude.py`,
`planetarium_distance.py`, `planetarium_apparent_magnitude.py`. Already follow
a spec-like pattern: receive parameters, load data, process, build figure.

**Computation engines:** `data_processing.py`, `stellar_parameters.py`,
`visualization_2d.py`, `visualization_3d.py`, `visualization_core.py`,
`star_properties.py`, `simbad_manager.py`, `incremental_cache_manager.py`,
`catalog_selection.py`.

**Data:** Gaia and Hipparcos catalogs with deduplication boundaries, enriched
via SIMBAD (which rate-limits large calls). **Fully cached** in PKL files
locally. Coverage: 101 light-years distance, apparent magnitude 9. This cache
represents careful, rate-limited construction — it cannot be casually
regenerated. The PKL files are gitignored (exceed GitHub size limits) and
distributed via Releases for the desktop. For the web version: cache weight
needs local measurement (`du -sh star_data/`), wire format is an open
sub-decision (pickle is Python-version-coupled — fine for a server, brittle
for Pyodide — a convert-to-Parquet-or-JSON step at cache-build time is the
standard escape), and hosting location must be decided against the headroom
budget.

**Output:** Plotly 2D figures (HR diagrams) and Plotly 3D figures (stellar
neighborhoods, planetarium views).

**Rich options, not just presets.** Magnitude limits, distance limits,
visualization type, star search, spectral class filtering, notable star
annotations. The web version preserves this interactivity.

### §4c — Orbital Parameters (educational showcase)

**Current GUI:** `orbital_param_viz.py`. Object selector, display option
checkboxes, interactive eccentricity slider demo.

**Computation engines:** `idealized_orbits.py`, `constants_new.py`,
`apsidal_markers.py`. Pure geometry — no data fetching.

**Output:** Plotly 3D figures (orbital transformation) and matplotlib 2D
(eccentricity demo).

**Web-native showcase.** Lightest domain. Educational, interactive,
computationally lightweight. The eccentricity slider teaches the Keplerian
language the rest of the orrery speaks. Serves as the two-sided pilot (Phase 0).

### §4d — Earth System

**Current GUI:** `earth_system_visualization_gui.py`. Hub/launcher.

**Generators:** `earth_system_generator.py` (scalar heat engine),
`food_insecurity_generator.py` (categorical/vector). Shared helpers in
`earth_system_common.py`.

**Scenario modules:** `scenarios_heatwaves.py`, `scenarios_food_insecurity.py`,
`scenarios_coral_bleaching.py`, `scenarios_western_heatwave_march_2026.py`,
and the paleoclimate family.

**Output:** Mixed — **KMZ files for Google Earth** and **Plotly figures** (ENSO
charts, paleoclimate timelines, teasers). The KMZ rendering question (downloads
with teasers, Plotly choropleth, or map library) is resolved in Phase 5.

**Cache model:** Hybrid — mostly manually archived, but a CDS updater fetches
ERA5/ERA5T climate data automatically (desktop-side). ERA5 data is archived
once the reanalysis is complete. IPC GeoJSON is static per analysis period.
All served data is static.

**Stance carries forward:** "Synthesize nothing, transcribe everything, attribute
to IPC." "Data Preservation is Climate Action."

### §4e — Cross-Domain Integration

- **Celestial sphere** (`star_sphere_builder.py`): Adds star traces to orrery
  figures. Called by the solar system assembler.
- **Exoplanet orbits** (`exoplanet_orbits.py`): Bridges solar system and star
  domains. Phase 4 (hybrid).
- **Sgr A* Grand Tour** (`sgr_a_grand_tour.py`): Self-contained visualization.
  Phase 4 (hybrid).

---

## §5 — Phased Approach

**Characterization harness (L-080) is an ongoing gate.** Tony's render remains
the close authority (Mode 5).

**Delta-log discipline throughout:** any orchestration change to the desktop
during the build gets a ledger tag ("assembler-must-inherit").

### Phase 0 — Two-Sided Pilot

Build the orbital parameter eccentricity visualization twice: **Dash on HF
Spaces** and **Pyodide on a static page**. Same visualization, two delivery
mechanisms. Tests hosting assumptions, cold-start vs first-load download, phone
experience, ops feel — and turns the server-vs-serverless decision (§7 #1)
from a debate into a measured comparison. The cheapest place to buy real data on
the largest open decision.

Note: if either pilot is publicly reachable, keep unlisted until the attribution
page lands.

Gate: lessons-learned document + server-vs-serverless decision before proceeding.

### Phase 1 — Shared Spec Skeleton + Solar System Vocabulary

Design the **shared spec skeleton** — what every spec has across all domains:
domain tag, content type, display options. Then design the **solar system
vocabulary**: objects, center, dates, display options, content type
(static/animation). Other domain vocabularies are designed just-in-time at the
head of their own phases, informed by lessons learned.

Also in Phase 1:
- Gate check: confirm no shared-layer seams beyond the two named in §2.
- Design the **coverage index interface** for the solar system domain.
- Define **scene equivalence criteria** — the concrete definition of what
  "equivalent output" means. Largely Mode 5 (Tony's visual judgment), plus a
  convention checklist (single-info-marker, AU in hover, marker symbols). This
  definition shapes what L-080's golden artifacts capture.

Gate: vocabulary document, index interface spec, and equivalence criteria
reviewed and stable before any build.

### Phase 2 — Solar System Assembler + Desktop Migration

The main build. Scene spec in, Plotly figure out. Written with `plot_objects` and
`animate_objects` as the recipe reference. Animation/static consolidation is
inherent. `orbit_paths.json` (accessed through the index abstraction) serves as
fixture data during development.

**Desktop migration tail:** once the assembler validates, the tkinter solar
system GUI migrates onto it. Original orchestration code archived.

Gate: scene equivalence (Phase 1 criteria) + Mode 5.

### Phase 3 — Star Vocabulary + Assembler + Cache + Desktop Migration

Design the star vocabulary (just-in-time, informed by Phase 2 lessons). Build
the star assembler using existing pipeline scripts as the recipe reference.
Resolve the star cache wire format and hosting location.

**Desktop migration tail:** star GUI migrates onto the assembler.

Gate: scene equivalence + Mode 5.

### Phase 4 — Hybrid: Exoplanets + Sgr A* + Desktop Migration

Exoplanet orbits bridge domains. Sgr A* Grand Tour is self-contained. Both
handled as scene types within the solar system assembler or as standalone
extensions.

**Desktop migration tail:** relevant desktop paths migrate.

Gate: scene equivalence + Mode 5.

### Phase 5 — Earth System Vocabulary + Assembler + Desktop Migration

Design the Earth system vocabulary. Build the assembler for Plotly outputs
(paleoclimate, ENSO, teasers). Resolve the KMZ rendering question (downloads,
Plotly choropleth, or map library). Generators are already well-factored.

**Desktop migration tail:** Earth system GUI migrates onto the assembler.

Gate: scene equivalence + Mode 5.

### Phase 6 — Web UI

Framework chosen based on Phase 0 lessons. Dash is the front-runner. One web
application presenting all domains. Implements the envelope-declaring GUI.
Curated animation presets available: comet perihelia, encounter flybys, close
approaches, satellite orbits, planetary tours.

Gate: end-to-end on hosting platform. Mode 5.

---

## §6 — Prep Work (before Phase 0)

**L-080 — Smoke-test harness.** Spec for scene equivalence (§5 Phase 1 criteria).

**LICENSE to repo root.** Move from `documentation/LICENSE.md`. Harmonize
copyright year (file: 2024; README: 2025-2026).

**Attribution page.** Data sources: JPL Horizons, JPL SBDB/CAD, Copernicus CDS /
ERA5 / ERA5T, NOAA Coral Reef Watch, IPC and FEWS NET, HDX, OCHA FTS, SIMBAD
(CDS), Gaia (ESA), Hipparcos, NSIDC, Mauna Loa CO₂ (NOAA GML/Scripps), HOT
program. Provider citation strings need fetching. Copernicus and IPC terms most
likely to constrain hosting.

**L-068 residuals** (L-066, L-016, L-014) — Desktop cleanup. Not web blockers.

**`palomas_orrery_helpers.py` split** — Separate computation from tkinter GUI
helpers. Companion to L-026.

---

## §7 — Open Decisions

1. **Server vs serverless.** Dash (Python process, HF Spaces/Render) vs Pyodide
   (Python in browser, static hosting only). §1's "site never fetches Horizons"
   removed the CORS blocker on Pyodide — the app reads static cached JSON,
   same-origin, no live fetch. Dash is Plotly-native, less new code; Pyodide has
   zero ops burden, zero cost, infinite scale. Phase 0 two-sided pilot resolves
   this. Note: if Pyodide wins, the web app is a static site that naturally
   merges with the existing gallery viewer — Fable's Option E (one front end,
   interchangeable back ends) arrives nearly for free. If Dash wins, the gallery
   stays a sibling.
2. **Scene-spec vocabulary design.** The architecture is S3 (offline
   resolver/assembler split) — settled. What remains is the vocabulary itself.
   Solar system in Phase 1; other domains just-in-time.
3. **Multi-file cache structure (solar system):** per-object vs per-pair vs
   per-(pair+window); coverage index format. Resolved in Phase 2/3.
4. **Tier-1 standard catalog:** which pairs, what window, what intervals.
5. **Tier-3 persistence:** on or off. A dial.
6. **Pages headroom strategy:** separate Pages project site, scene-weight
   reduction, gallery culling (L-074), or early R2 graduation.
7. **Earth system KMZ rendering on the web:** downloads with teasers, Plotly
   choropleth, or map library.
8. **Star cache wire format:** PKL (Python-version-coupled) vs Parquet/JSON.
   Tied to decision #1 (Pyodide needs non-pickle format).

---

## §8 — Vision Opportunities & Open Questions

*Captured in `LEDGER_CONSOLIDATED.md` per house rule ("floating items get lost;
capture on first mention"). Several already carry L-numbers. Summary:*

Preset authoring (L-046). Option E unified front end. Embeddable scenes for
educators. Educational guided explorations. Community cache as commons. Earth
system as web narrative (L-071). PWA / offline for classrooms. Gallery
generators as spec-producers. What the web orrery *feels* like (suite-design
conversation before Phase 6).

---

## §9 — What This Plan Does NOT Cover

Desktop development continues on its own track. The web fork is additive.
The Instagram pipeline is independent. The existing ledger is unaffected.

---

## §10 — Lineage

This plan draws from eight design sessions:

- **Fable 5 survey** (July 2, 2026): Four-front survey. L-079 as keystone.
  Five publication options. Six code proposals (L-079–L-084).
- **Fable 5 L-079 deep dive** (July 2, 2026): Five S-options, four M-options,
  three phasing strategies, repricing map.
- **Opus 4.8 convergence handoff** (July 2, 2026): Fetched JPL/GitHub terms.
  Converged site-never-fetches, three-tier cache, envelope-declaring GUI.
- **Opus 4.8 review of v2** (July 3, 2026): Verified shared-layer boundary.
  Caught `celestial_objects.py` seam.
- **Fable 5 review of v2** (July 3, 2026): Found `palomas_orrery_helpers.py`
  seam. Named assembly-duplication tension. Redefined gate as scene equivalence.
- **Opus 4.6 + Tony convergence** (July 3, 2026): Resolved option (b) — shared
  assembler. Fork decision. Four domains identified.
- **Opus 4.8 review of v3.1** (July 3, 2026): Named server-vs-serverless
  decision. Two-substrate model. Cache-through-index from day one.
- **Fable 5 review of v4** (July 3, 2026): Star PKL cache provenance. Module
  corrections. Phase 7 drift window → per-domain migration tails. Vocabulary
  waterfall → just-in-time. Two-sided pilot. Animation envelope. Scene
  equivalence criteria. Coverage index as solar system concept.

**Decisions made (cumulative):**
- Site never fetches Horizons (§1)
- Three-tier cache, all offline (§1)
- GUI declares the envelope, including content type (§1)
- Two hosting substrates: cache on Pages/R2, app TBD (§1)
- Assemblers read cache through index abstraction from day one (§1)
- Coverage index is solar system concept; other domains declare bounds simply (§1)
- Web GUI is a fork, not a replacement (§2)
- One shared assembler per domain, both GUIs as thin harvesters (§3)
- Assembler is new code; original code archived (§3)
- Per-domain migration tails + delta-log discipline (§3)
- Architecture is S3 / M3 from Fable's options (settled by §1/§3)
- Four visualization domains recognized (§4)
- Star data is fully cached, 101 ly / mag 9, Gaia + Hipparcos (§4b)
- Phase 0 is two-sided pilot: Dash + Pyodide (§5)
- Phase 1 designs shared skeleton + solar system vocabulary only (§5)
- Scene equivalence criteria defined in Phase 1 (§5)
- Other domain vocabularies designed just-in-time (§5)
- Animation presets as curated tier-2 exports (§1/§5)
- Phasing: Pilot → Solar System → Stars → Hybrid → Earth System (§5)

---

Base: main @ `d6c8c42` / gallery @ `89c8bf30`. Nothing built, nothing pushed.
Round discipline: this document should get SHORTER next round — options struck
as decisions land, not added.
