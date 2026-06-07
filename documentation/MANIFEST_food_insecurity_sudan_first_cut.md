# MANIFEST -- Food Insecurity Layer, First Cut (Sudan)

Tony Quintanilla, PE | Claude | Earth System track | June 5, 2026
Base SHA: de12f56 (de12f5635a6f04c36b9e62509f24e517cce7ad07)
Status: DESIGN. This is the spec a build session executes against. No code yet.
Companion: HANDOFF_food_insecurity_design_v1.md (the reasoning trail; read it first).

--------------------------------------------------------------------------------
## 0. ONE-LINE PURPOSE

Render IPC acute food-insecurity classification for Sudan as a dated, sourced,
vector KMZ layer that joins the Earth System family of stressors (heat, ocean
acidification, ocean heat / El Nino) in one navigable frame. The layer documents
where the system is under strain; it asserts no causation of its own.

--------------------------------------------------------------------------------
## 1. SCOPE -- WHAT THIS FIRST CUT IS

- ONE country: Sudan. Not a regional mosaic.
- ONE IPC release: the current Sudan analysis (Current period plus its
  projection periods). Confirm exact windows at pull time; as of last search the
  current period was Feb-May 2026 with projections to Jan 2027.
- Approach B: real KML vector polygons per analysis area, each carrying a
  transcribed IPC popup. NOT a rasterized re-photograph of IPC's published map.
- Built as a FAMILY MEMBER, not a one-off: it must share legend placement,
  opacity / draping discipline, date-pinning, provenance popup, and a temporal
  axis with the existing temperature (ERA5) layers, so later co-visualization is
  a compositing job, not a rebuild.

--------------------------------------------------------------------------------
## 2. STANCE -- THE LINE THAT GOVERNS EVERY FIELD

The collection's stance is "food insecurity as a symptom of ecological-social
failure -- pay attention." The collection carries that thesis by JUXTAPOSITION
and CURATION (this layer sitting beside heat and ocean in one frame), never by a
causal arrow this layer draws.

Therefore:
- We synthesize NOTHING. Every popup field is a transcribed IPC value.
- Causal claims ("drivers") appear ONLY as IPC's own attributed, dated words.
  We never upgrade IPC's framing with a better-sourced claim from elsewhere,
  even when one exists. The reader makes cross-stressor connections themselves.
- "Where we are going" is IPC's own projection, attributed to IPC -- never our
  extrapolation.
- Provenance is a claim that must be TRUE: cite to where the data actually came
  from, or remove and note the gap. Never cite-to-clear.

This is the "access is not understanding" / real-people discipline. The subject
is human; the restraint is the point.

--------------------------------------------------------------------------------
## 3. DATA -- SOURCE AND FIELDS (all confirm-at-pull-time)

Primary source: IPC (ipcinfo.org) -- analysis shapefile / API for the current
Sudan release. Fallback: FEWS NET (often more current for the Horn).

Per analysis area, extract and TRANSCRIBE (do not compute, do not paraphrase):
- Geometry (polygon boundary of the analysis unit)
- IPC Phase classification (1-5) for each period
- "Not analysed / inadequate evidence" status where present (a real category;
  NOT Phase 1 -- see section 5)
- Evidence Level (IPC's per-area confidence tier, e.g. Medium)
- Assistance overlays where present:
  * households meeting a substantial share of caloric needs via assistance
  * area receiving significant humanitarian food assistance (accounted for in
    the phase classification)
- Population figures (per phase / Phase 3+ as IPC reports them)
- Key drivers -- IPC's verbatim driver text for the area/country (IPC voice)
- Analysis date, period label (Current / Projection 1 / Projection 2 with the
  literal date windows)
- IPC's recommended citation string and terms of use (transcribe literally)

CONFIRM AT PULL TIME, do not recall:
- Whether access is API or shapefile download, and the exact field names
- The analysis-area / admin-boundary geometry source
- The exact period windows of the current release
- Whether the current release names fuel/fertilizer (Iran-war-linked) costs in
  its drivers. If IPC names it, transcribe it. If IPC folds it into "economic
  decline," carry that. We do not add it ourselves.

--------------------------------------------------------------------------------
## 4. KMZ STRUCTURE

```
Document
  Styles:
    style_phase_1 ... style_phase_5      (polygon fill + line, per IPC ramp)
    style_not_analysed                   (distinct fill, see section 5)
    style_assistance_overlay (optional first cut -- scope TBD)
  Folder: "Current (<dates>)"            -> Placemarks, one per analysis area
  Folder: "Projection 1 (<dates>)"       -> Placemarks
  Folder: "Projection 2 (<dates>)"       -> Placemarks  (if present)
  ScreenOverlay: phase-ramp legend       (or inherit shared family legend)
```

Each Placemark:
- name: analysis area name
- styleUrl: by phase (or not-analysed)
- Polygon / outerBoundaryIs / LinearRing / coordinates
- description: CDATA HTML balloon carrying the transcribed fields (section 6)

TEMPORAL AXIS DECISION (first cut): use independent FOLDERS per period, not a
TimeSpan time-slider. Rationale: the projection periods are alternative forecast
windows, not a continuous time series; folders are honest about that
discreteness and let the reader toggle Current vs Projected cleanly. Reserve
TimeSpan for the deferred historical-arc extension (item 2), which IS a true
series across releases and should match the ERA5 time-slider convention.
CONFIRM: how the current temperature layers express their temporal axis, so the
family stays coherent.

--------------------------------------------------------------------------------
## 5. STYLING -- PHASE RAMP, NOT-ANALYSED, OPACITY

Phase ramp follows IPC's official 5-step scheme:
  Phase 1 Minimal    -- light green
  Phase 2 Stressed   -- yellow
  Phase 3 Crisis     -- orange
  Phase 4 Emergency  -- red
  Phase 5 Famine     -- dark red
CONFIRM exact hex from IPC's color guidance at pull time. Do NOT embed recalled
hex values as authoritative -- this is a fetched-vs-recalled item.

NOT-ANALYSED FILL is the one element with no temperature-pipeline analog and
must be designed in, not retrofit. IPC renders it distinct (grey / hatching). It
is NOT Phase 1 and must not read as "no problem." It frequently covers the
worst-off, hardest-to-reach areas (its presence can even depress the headline
Phase 3+ count). Render it as visually distinct and label it explicitly in the
balloon and legend.

KML COLOR GOTCHA: KML color order is aabbggrr (alpha, blue, green, red), the
reverse of standard RGB hex. The builder must convert IPC RGB -> KML order.

OPACITY / DRAPING: match the temperature layers so this layer composes legibly
underneath or beside a draped climate field. The not-analysed fill in
particular must still read correctly under an overlaid layer.

--------------------------------------------------------------------------------
## 6. POPUP / BALLOON TEMPLATE (all fields transcribed, none synthesized)

```
<area name>
IPC Phase: <n> (<label>)            e.g. 4 (Emergency)
Period: <Current | Projection k> (<date window>)
Population in Phase 3+: <as IPC reports>
Evidence level: <IPC tier>
Assistance: <overlay flags if present>
Key drivers (IPC): "<IPC verbatim driver text>"
Analysis date: <date>
Source: IPC -- <IPC recommended citation string>
Data retrieved: <date>
```

The "Key drivers (IPC)" line is the only place a causal statement appears, and
it is IPC's words in IPC's voice, quoted and attributed. If the area has no
distinct driver text, omit the line rather than borrow country-level prose
without basis.

--------------------------------------------------------------------------------
## 7. INTEGRATION

Mirror the existing Earth System KMZ pipeline. Likely touch points (CONFIRM
against repo at HEAD before building -- do not prescribe from recall):
- earth_system_generator.py (or current equivalent generator)
- scenarios_*.py pattern -- add a food-insecurity scenario module following the
  established naming (e.g. scenarios_food_insecurity.py) ONLY after confirming
  the actual dispatch / registration pattern in the repo
- KMZ assembly / output path conventions used by the temperature layers
- GUI registration so the layer appears in the Earth System selector

Read the live pattern first; do not invent the integration API from memory.

--------------------------------------------------------------------------------
## 8. NON-GOALS / DEFERRED (state, so they do not creep in)

- NO regional mosaic (multi-country). Sudan only. The mosaic imports a
  date-reconciliation problem because IPC releases are per-country with
  non-aligned windows; deferred deliberately.
- NO historical time-series across releases (deferred item 2; uses TimeSpan
  when built).
- NO live / auto-updating fetch. Layers are dated, pinned, deliberately
  re-pulled. Off the table by design (silent refresh is a provenance hazard).
- NO causal attribution authored by us. Drivers are IPC-voice only.
- NO rasterized GroundOverlay that re-photographs IPC's published cartography.

--------------------------------------------------------------------------------
## 9. CONFIRM-BEFORE-BUILDING LEDGER (fetch, do not recall)

1. IPC data access method + format (API vs shapefile) and exact field names
2. Analysis-area / admin-boundary geometry source
3. Official IPC phase hex colors
4. IPC recommended citation string + terms of use
5. Current Sudan release: exact Current + projection windows
6. Whether the current release names fuel/fertilizer in its drivers
7. Existing Earth System KMZ pipeline pattern in repo at HEAD (modules,
   dispatch, KMZ assembly, output path, GUI registration) -- mirror it
8. Temporal-axis convention of current temperature layers (folders vs TimeSpan)

--------------------------------------------------------------------------------
## 10. VERIFICATION (Mode-5 + smoke, before the layer is "done")

- KMZ opens in Google Earth with no error.
- Phases render in the correct geographic areas. Spot-check: greater Darfur /
  Kordofan high phase; El Fasher and Kadugli at Phase 5 in the relevant period.
- Not-analysed areas read visually distinct from Phase 1 and are labeled.
- Each balloon shows the transcribed fields. Spot-check that the drivers text
  matches the IPC source verbatim -- any synthesized sentence is a failure.
- Period folders toggle independently; Current vs Projected is clear.
- Opacity / draping is consistent with the temperature layers (overlay test).
- Generated source is ASCII, LF line endings.
- Citation present and matches IPC's recommended form (provenance is true,
  not merely present).

The render is the gate. If the map disagrees with the code reading, the render
wins.

--------------------------------------------------------------------------------
Module updated: June 2026 with Anthropic's Claude Opus 4.8
