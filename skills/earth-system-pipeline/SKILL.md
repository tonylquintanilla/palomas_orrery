---
name: earth-system-pipeline
description: Earth System KMZ and climate visualization pipeline for the Paloma's Orrery project. Use for any task touching earth_system_generator.py, earth_system_common.py, food_insecurity_generator.py, the scenarios_* modules (heatwaves, coral bleaching, western heatwave, food insecurity), earth_system_controller.py, or their data sources (ERA5 / Copernicus CDS, Open-Meteo, ERDDAP / Coral Reef Watch, IPC Mapping Tool GeoJSON). Use when building or modifying KMZ layers, Google Earth scenarios, Plotly teasers, intel/legend/encyclopedia cards, or scenario configs -- and for ANY Paloma's Orrery visualization or text where human cost is an element (heat deaths, food insecurity, displacement): the restraint discipline section applies even to prose about these layers. Do not use for projects other than Paloma's Orrery.
---

# Earth System Pipeline

Skill version: 1.0 | Cut from palomas_orrery @ b29ad3f8 | July 1, 2026
Sources: earth_system_generator.py, earth_system_common.py,
food_insecurity_generator.py, scenarios_* at HEAD; western heatwave handoff
v9; food insecurity design + build handoffs v2.

## Architecture: Teaser and Blockbuster

Every scenario produces two artifacts:
- The TEASER: a fast-loading 2D Plotly HTML for the web gallery
  (generate_plotly_teaser), which then rides the gallery pipeline.
- The BLOCKBUSTER: a single-document KMZ for Google Earth Pro
  (KML layers + card PNGs zipped by package_and_cleanup).

KMZ filenames are STABLE per scenario_id -- gallery cards link to them by
name, so a regenerated KMZ replaces the file without touching the gallery
JSON. A KMZ-only update (replace file in gallery/assets/, push) is a valid
fast path that skips the full pipeline. Build-stamped overlay naming
(intel_<ID>_<YYYY-MM-DD-HH-MM>.png) is cache-bust insurance inside the KMZ.

## Engine vs Scenario Contract

earth_system_generator.py is the shared SCALAR engine (gridded fields):
run_scenario orchestrates fetch -> spikes KML -> heatmap KML -> impact KML
-> cards -> teaser -> package. Scenario modules provide a SCENARIOS list of
dicts plus a fetch function; the GUI (MissionSelector) extends
all_scenarios from each module's SCENARIOS. Tony's rule: "The engine should
be centralized and the scenarios connect to it."

Vector/categorical layers (IPC food insecurity polygons) get a DEDICATED
generator that mirrors the family's single-doc-KMZ + ScreenOverlay-card
conventions WITHOUT importing the scalar engine (which pulls in
plotly/scipy/matplotlib/tkinter at import). food_insecurity_generator.py is
the precedent. earth_system_common.py holds the engine-agnostic shared
pieces (balloon HTML builder, tappable "i" pin placemark, the injected-run
ScenarioPicker) -- put new shared pieces there, not in either engine.

The food_insecurity_* filename prefix is LOAD-BEARING: the Google Earth
controller globs on it.

## The 3+5 Card Pattern (KMZ info cards)

Compact always-on header (ScreenOverlay: title + date + hint) plus a
tappable "i" Placemark at the grid centroid whose balloon carries the full
briefing. simplekml entity-escapes description fields by default -- wrap
balloon content in <![CDATA[...]]> to emit unescaped HTML
(create_info_placemark in earth_system_common does this). The population
exposure key is inappropriate for coral scenarios (gate on
`if populations:`).

## Data Sources and Fetch Discipline

- ERA5 via Copernicus CDS API (~/.cdsapirc in the USER HOME, never the
  repo; Windows: notepad %USERPROFILE%\.cdsapirc, and watch for a silently
  appended .txt). CDS license acceptance is a one-time manual step; a 403
  includes the acceptance URL -- surface it in error messages.
- ERA5T (near-real-time) lags ~5 DAYS, not months -- "now" honestly means
  up to ~5 days back, so layers are dated/pinned, deliberately re-pulled,
  never live-auto-updating.
- Open-Meteo ERA5 archive serves the heatwave scenarios' fetch
  (fetch_era5_heatwave, persistent JSON cache in data/).
- ERDDAP (NOAA Coral Reef Watch) serves coral scenarios.
- Three-tier fetch for developing scenarios: CSV cache (instant) -> CDS
  API (automatic) -> synthetic fallback (always works). Each tier catches
  a different failure mode.
- Climatology is the expensive one-time cost (30 years x 24 h x grid),
  cached per day-of-month; the event-day download is small.
- Grid expansion requires CACHE INVALIDATION: delete the affected cached
  CSV / raw NC / climatology NC before re-run, or the three-tier fetch
  serves stale small-grid data. Earlier snapshots keep their own grids --
  each snapshot's config drives its extent independently.
- "Modified Copernicus Climate Change Service information" attribution is
  a LICENSE REQUIREMENT when anomalies are computed from raw ERA5; the
  encyclopedia "i" card is the right home.

## Developing (Ongoing) Scenarios

Historical scenarios are static; developing ones accumulate. The pattern:
date-parameterized SNAPSHOT_CONFIGS drive anomaly extent, grid, and CSI
per snapshot; RECORD_STATIONS carry first_date gating so stations
accumulate as the event progresses; each snapshot is a frozen moment but
the SCENARIOS list grows. Mark developing content provisional/preliminary
(the Western Heatwave convention). Fetch peak values at build time; never
recall breaking-news numbers. Let the data drive the grid: start focused,
expand as the event reveals itself.

## Layer Semantics

- Anomaly vs absolute: contour shows anomaly (the event's spatial
  pattern); station pins show absolute temperature (what people
  experienced). Both are needed; they answer different questions.
- Anomaly vs records are complementary: the field says "abnormally hot
  everywhere"; the pins say "these places exceeded anything measured."
- Overlapping pins tell the story -- a station breaking its own record
  three times in a week IS the narrative. spike_stride is grid-density
  dependent; confirmed-observation scenarios use station pins instead.
- HTML briefing text feeds TWO consumers: the Plotly teaser renders HTML;
  the matplotlib intel card needs plain text. Strip tags AT THE ENGINE
  (preserving <br> as double newlines first) so every scenario is
  protected; never maintain dual text per scenario. Mobile briefing is
  auto-generated (title + first paragraph) with a mobile_briefing
  override key.
- Briefing vs encyclopedia are separate builders and separate keys: the
  briefing serves the annotation (short, visual); the encyclopedia serves
  the "i" card (deep, scrollable). Organize Earth System context by
  planetary boundaries; boundaries accumulate across snapshots. The
  encyclopedia is where the project owns the narrative -- lean into
  attribution science ("data preservation is climate action"), and get
  the mechanism right (e.g. blocking is natural; magnitude is
  anthropogenic -- climate change raises the floor, it does not create
  the pattern).

## SENSITIVE CONTENT: The Human-Cost Restraint Discipline

This section governs EVERY visualization or text where human cost is an
element -- food insecurity, heat events with deaths, conflict displacement.
The subject is human; the restraint IS the design. The stance:
synthesize nothing, transcribe everything, attribute to the source, defer
causation to the reader.

- TRANSCRIBE, DON'T SUM. National/headline totals are transcribed
  constants from the source's own text, NEVER computed from the file's
  parts. The worked near-miss: naively summing the IPC Sudan GeoJSON gave
  185k Phase-5 / 28M Phase-3+ / 51.7M total against IPC's published 135k
  / 19.5M / 47.5M, because IDP-settlement units overlap host localities.
  Polygons are for per-area color and per-area popups only.
- FULL PHASE 1-5 BREAKDOWN IN EVERY BALLOON. IPC's mapped phase is the
  highest severity affecting at least 20% of an area's population, so a
  sub-20% Catastrophe (Phase 5) population can hide under a Phase-4
  color. The popup must carry the full phase1-5 population/percentage
  split including phase5_population, and the legend must STATE the >=20%
  rule so even the glance is honest about what the color hides.
- SOURCE VOICE ONLY. Attribution voice is the analysis body's (IPC's),
  never upgraded with outside claims. Drivers ride as ONE national card
  transcribed in the source's words; if an area has no distinct driver
  text, omit rather than borrow. Never author causal linkages: carry a
  linkage ONLY if the source's own analysis names it (the Iran-war /
  Hormuz test case: IPC named the fuel-fertilizer price channel, so we
  transcribe IPC's framing and the informed reader draws the connection).
  "State the basis; do not hand the lay reader a connection we will not
  draw ourselves."
- TWO-TIER ON-LAYER TEXT. Fix the most sensitive sentences ON the layer
  so they cannot be ad-libbed -- but fixed is only safe if SOURCED. Split
  transcribed vs composed per the provenance-discipline skill; composed
  sentences are built in generator code with per-number # Source
  comments, scanner-visible. Narration reads FROM the framing text.
- The route through the map does ethical work: an Instagram Reel is a
  guided 60-90s walk, and honesty lives in the PATH (e.g. reveal the
  hidden Catastrophe population as a beat), not in a single frame. Design
  the KMZ with the affordances the route needs.
- FEWS NET is rejected as source-of-record for IPC layers (IPC-compatible
  but not IPC consensus). Per-country IPC releases are non-aligned in
  time -- regional mosaics import a date-reconciliation problem; single
  country first.

## Shared Conventions (duplicated here deliberately; masters elsewhere)

- Credit line on substantive edits: "Module updated: [Month Year] with
  Anthropic's Claude [model]" (master: orrery-coding-conventions).
- ASCII-only / LF for all Python deliverables (master: safe-file-editing).
- Distance hover text includes AU alongside km where distances appear
  (master: orrery-coding-conventions).
- Provenance: Tier-1 = 0 before push; composed text sourced at the
  construction site (master: provenance-discipline).

## Field Notes

- simplekml newpoint() creates pins, not extruded polygons -- polystyle on
  a point is ignored; use newpolygon() for 3D extrusions.
- Two color systems must agree: the contour colormap (matplotlib) and the
  legend bands must be generated from the same ramp (continuous colorbar
  legend matches the contour exactly).
- KML color order is aabbggrr (alpha, blue, green, red) -- convert before
  comparing to web hex.
- clampToGround for station pins; pin labels show absolute temperature.
- Where a source file carries no colors (IPC GeoJSON), sample the ramp
  from the source's own published legend and flag it -- never embed
  recalled brand hex (fetched-vs-recalled).
- Verify the deployed file, not the working copy -- check both sides of
  an engine/scenario contract.
- KMZ byte-inspection is a valid pre-render gate (CDATA unescaped, style
  counts match data); Mode-5 Google Earth render remains the
  authoritative close gate, and it is Tony's.
