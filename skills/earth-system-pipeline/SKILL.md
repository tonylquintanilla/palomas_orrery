---
name: earth-system-pipeline
description: "Earth System KMZ and climate visualization pipeline for the Paloma's Orrery project. Use for any task touching earth_system_generator.py, earth_system_common.py, food_insecurity_generator.py, the scenarios_* modules (heatwaves, coral bleaching, western heatwave, food insecurity), earth_system_controller.py, or their data sources (ERA5 / Copernicus CDS, Open-Meteo, ERDDAP / Coral Reef Watch, IPC Mapping Tool GeoJSON and Excel). Use when building or modifying KMZ layers for Google Earth on the web, a layer's page on the website (earth/[id].html) and its guided walk, Plotly teasers, intel/legend/encyclopedia cards, or scenario configs -- and for ANY Paloma's Orrery visualization or text where human cost is an element (heat deaths, food insecurity, displacement): the restraint discipline section applies even to prose about these layers. Do not use for projects other than Paloma's Orrery."
fires_when: KMZ layers, Google Earth web, a layer's page and its walk, ERA5/ERDDAP/IPC, scenarios, ANY human-cost visualization or text
---

# Earth System Pipeline

Skill version: 1.3 | 2026-11-14, with Anthropic's Claude Opus 5.5, at
palomas_orrery @ 5779e1f0. v1.3 (L-001) adds Google Earth on the Web
and A Layer's Page and Its Walk (Tony, 2026-11-14). Older entries, and
the Shared Conventions copied from their masters, are in
documentation/SKILL_HISTORIES.md (moved 2026-11-14).

## Architecture: Page, Blockbuster and Teaser

Every scenario produces up to three artifacts: the PAGE, its one home on
the website (A Layer's Page and Its Walk); the BLOCKBUSTER, a
single-document KMZ, data/<scenario_id>_blockbuster.kmz, its name stable;
and the TEASER, a 2D Plotly HTML for the old gallery
(generate_plotly_teaser). A web layer's KMZ is imported into Tony's
shared Google Earth project, whose link survives a re-import. A layer
still built for Google Earth Pro (L-530; Pro stops being offered on 25
June 2027) keeps the 3+5 card: a ScreenOverlay header plus a tappable
"i" pin whose CDATA balloon carries the briefing (create_info_placemark),
overlay names build-stamped as cache-bust insurance, and a gallery card
linking the KMZ by name. The population key is wrong for coral (gate on
`if populations:`).

## Engine vs Scenario Contract

earth_system_generator.py is the shared SCALAR engine (gridded fields):
run_scenario orchestrates fetch -> spikes KML -> heatmap KML -> impact KML
-> cards -> teaser -> package. Scenario modules provide a SCENARIOS list of
dicts plus a fetch function; _heat_scenarios() in earth_system_generator.py aggregates the scalar-engine
modules' SCENARIOS lists (food insecurity is deliberately NOT aggregated
there -- it has its own generator and its own controller entry point,
MissionControlApp in earth_system_controller.py, with the shared
ScenarioPicker from earth_system_common). Tony's rule: "The engine should
be centralized and the scenarios connect to it."

Vector/categorical layers (IPC food insecurity polygons) get a DEDICATED
generator that mirrors the family's single-doc-KMZ conventions
WITHOUT importing the scalar engine (which pulls in
plotly/scipy/matplotlib/tkinter at import). food_insecurity_generator.py is
the precedent. earth_system_common.py holds the engine-agnostic shared
pieces (balloon HTML builder, tappable "i" pin placemark, the injected-run
ScenarioPicker) -- put new shared pieces there, not in either engine.

The food_insecurity_* filename prefix is LOAD-BEARING: the Google Earth
controller globs on it.

## Google Earth on the Web

Tested 2026-11-13 and 14 (L-001). The generator's byte check enforces
the first three after every build and fails by name.
- Styles are shared, at Document level, referenced by id; one inside a
  Folder is LOST (every area plain yellow). simplekml nests them, so
  write the KML as text.
- No ScreenOverlay (unsupported): title, period and legend go in the "i"
  pin's pop-up, colours named in words, with the legend's own rule.
- Pop-ups: one <div> per line, <b> for labels; <br> and newlines are
  stripped, <table> becomes "TABLE SECTION". A packed icon shows.
- The phone APP shows top-level items as pages and an import arrives as
  one folder ("1/1"), so no switching there; a phone's BROWSER can. The
  words promise only where the map opens and that, in a web browser,
  the list on the left switches periods. Nothing about the app.
- The owner's switching is saved as the public view: a re-import ends
  with the view set back and the link opened signed out.
- earth.google.com refuses to be framed (X-Frame-Options SAMEORIGIN):
  the page links out.

## A Layer's Page and Its Walk

- One home: earth/<scenario_id>.html, written by the layer's generator
  from its KMZ's data and constants into data/earth/, copied to the
  website's earth/.
- Where a visitor needs a route, the walk lives on the page (Tony,
  2026-11-14): a short scroll of steps, a picture above a few
  sentences, upright phone first; Google Earth is the last step's button.
- Pictures are drawn at every build, earth/<scenario_id>_<step>.png,
  alt text on each; a close-up's frame and labels are read from the data.
- Each figure is built with its # Source at the source's page; a
  sentence stating a fact about the data is checked against it, or the
  build stops. No sideways scroll in 360 and 375 px frames; Tony reads
  every word before it goes live.

## Data Sources and Fetch Discipline

- ERA5 via Copernicus CDS API: ~/.cdsapirc in the USER HOME, never the
  repo (Windows: notepad %USERPROFILE%\.cdsapirc; watch for an appended
  .txt). License acceptance is one-time; a 403 carries its URL -- surface it.
- ERA5T (near-real-time) lags ~5 DAYS, not months -- "now" honestly means
  up to ~5 days back, so layers are dated/pinned, deliberately re-pulled,
  never live-auto-updating.
- Open-Meteo ERA5 archive serves the heatwave scenarios' fetch
  (fetch_era5_heatwave, persistent JSON cache in data/).
- ERDDAP (NOAA Coral Reef Watch) serves coral scenarios.
- IPC: the GeoJSON download holds the Current period's features whatever
  period is chosen; the Excel export holds every period, area by area.
  Figures from the Excel, outlines from the GeoJSON, joined by name; the
  run stops on a mismatch, naming the area.
- Three-tier fetch for developing scenarios, each tier for a different
  failure: CSV cache -> CDS API -> synthetic fallback (always works).
- Climatology (30 years x 24 h x grid) is the one-time cost, cached per day.
- Grid expansion requires CACHE INVALIDATION: delete the affected cached
  CSV / raw NC / climatology NC before re-run, or the three-tier fetch
  serves stale small-grid data. Earlier snapshots keep their own grids.
- "Modified Copernicus Climate Change Service information" attribution is
  a LICENSE REQUIREMENT when anomalies are computed from raw ERA5; the
  encyclopedia "i" card is the right home.

## Developing (Ongoing) Scenarios

Historical scenarios are static; developing ones accumulate:
date-parameterized SNAPSHOT_CONFIGS drive extent, grid and CSI per frozen
snapshot; RECORD_STATIONS' first_date gating adds stations as the event
progresses. Mark them provisional (the Western Heatwave convention); fetch
peak values at build time, never recall them; start the grid focused and
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
- HTML briefing text feeds the Plotly teaser (HTML) and the matplotlib
  intel card (plain text): strip tags AT THE ENGINE, <br> to double
  newlines first; never dual text per scenario. Mobile briefing: title +
  first paragraph, with a mobile_briefing override key.
- Briefing (the annotation: short, visual) and encyclopedia (the "i"
  card: deep, scrollable) are separate builders and keys. Organize by
  planetary boundaries, accumulating across snapshots. The encyclopedia
  owns the narrative: attribution science ("data preservation is climate
  action"), mechanism right (blocking is natural; magnitude is
  anthropogenic -- climate change raises the floor, not the pattern).

## SENSITIVE CONTENT: The Human-Cost Restraint Discipline

This section governs EVERY visualization or text where human cost is an
element -- food insecurity, heat events with deaths, conflict displacement.
The subject is human; the restraint IS the design. The stance:
synthesize nothing, transcribe everything, attribute to the source, defer
causation to the reader. The theme is respectful awareness (Tony,
2026-11-14): no adjectives of our own on suffering; people as people.

- TRANSCRIBE, DON'T SUM. National/headline totals are transcribed
  constants from the source's own text, NEVER computed from the file's
  parts. The worked near-miss: naively summing the IPC Sudan GeoJSON gave
  185k Phase-5 / 28M Phase-3+ / 51.7M total against IPC's published 135k
  / 19.5M / 47.5M, because IDP-settlement units overlap host localities.
  Polygons are for per-area color and per-area popups only.
- FULL PHASE 1-5 BREAKDOWN IN EVERY BALLOON. IPC's mapped phase is the
  highest severity affecting at least 20% of an area's population, so a
  sub-20% Catastrophe (Phase 5) population can hide under a Phase-4
  color. The popup carries the full phase1-5 split, phase5_population
  included, and the legend STATES the >=20% rule.
- SOURCE VOICE ONLY. Attribution voice is the analysis body's (IPC's),
  never upgraded with outside claims. Drivers ride as ONE national card
  transcribed in the source's words; if an area has no distinct driver
  text, omit rather than borrow. Never author causal linkages: carry a
  linkage ONLY if the source's own analysis names it (the Iran-war /
  Hormuz test case: IPC named the fuel-fertilizer price channel, so we
  transcribe IPC's framing and the informed reader draws the connection).
  "State the basis; do not hand the lay reader a connection we will not
  draw ourselves." Nor give the source a meaning in words it never uses
  (2026-11-14: "not a declaration"; IPC's worst-case words went in).
- TWO-TIER ON-LAYER TEXT. Fix the most sensitive sentences ON the layer
  so they cannot be ad-libbed -- but fixed is only safe if SOURCED. Split
  transcribed vs composed per the provenance-discipline skill; composed
  sentences are built in generator code with per-number # Source
  comments, scanner-visible. Narration reads FROM the framing text.
- The route through the map does ethical work, and honesty lives in the
  PATH (reveal the hidden Catastrophe population as a beat), not in a
  single frame. The route lives on the layer's page (above).
- FEWS NET is rejected as source-of-record for IPC layers (IPC-compatible
  but not IPC consensus). Per-country IPC releases are non-aligned in
  time -- regional mosaics import a date-reconciliation problem; single
  country first.

## Field Notes

- simplekml newpoint() makes pins (polystyle ignored); use newpolygon()
  for 3D extrusions.
- The contour colormap and the legend bands come from the same ramp.
- KML color order is aabbggrr; convert before comparing to web hex.
- clampToGround for station pins; pin labels show absolute temperature.
- Where a source file carries no colors (IPC GeoJSON), sample the ramp
  from the source's own published legend and flag it -- never embed
  recalled brand hex (fetched-vs-recalled).
- Verify the deployed file, not the working copy, on both sides of an
  engine/scenario contract.
- KMZ byte-inspection is a pre-render gate; Tony's Mode-5 look in Google
  Earth is the close gate.
