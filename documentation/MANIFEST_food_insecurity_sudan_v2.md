# MANIFEST -- Food Insecurity Layer v2, Current Period (Sudan)

Tony Quintanilla, PE | Claude | Earth System track | June 24, 2026
Base SHA: 1178f1a (1178f1ac8e096e61adcfc7da612b81188c033e64), branch main.
  Verified by round trip against remote HEAD at manifest-writing time. Tony's
  local working copy is at eb6a384 (cleanup only, no code, un-pushed). When the
  build session begins, build base = HEAD at that time -- confirm the SHA round
  trip first; do not build on this header's SHA if HEAD has moved.
Status: DESIGN / CONTRACT. This is the spec a build session executes against.
  No code yet.
Supersedes: MANIFEST_food_insecurity_sudan_first_cut.md (de12f56) -- now
  reference only. The delta from the first cut is recorded inline.
Companion: HANDOFF_food_insecurity_design_v2.md (the reasoning trail -- WHY the
  design is what it is). Read it first. If this manifest and the handoff ever
  disagree, that disagreement is a flag to raise, not a thing to silently
  resolve.
Abandoned (do NOT build on): the April period-7 Chart.js thread
  (scenarios_food_insecurity.py -> data/period7_food_insecurity.html,
  food_insecurity_handoff_v2_5.md). That work led somewhere we are not using.
  It is named here only so its module name is not silently reused (see
  section 12, ISSUE A).

--------------------------------------------------------------------------------
## 0. ONE-LINE PURPOSE

Render IPC acute food-insecurity classification for Sudan, CURRENT PERIOD ONLY
(Feb-May 2026), as a dated, sourced, no-key vector KMZ layer that joins the
Earth System family of stressors (heat, ocean acidification, ocean heat /
El Nino) in one navigable frame. The layer documents where the system is under
strain; it asserts no causation of its own. It is built so a 60-90s Instagram
Reel can walk it as a guided path (section 11).

--------------------------------------------------------------------------------
## 1. STANCE -- THE LINE THAT GOVERNS EVERY FIELD

Synthesize nothing. Transcribe everything. Attribute to IPC. Defer causation to
the reader. The collection carries its thesis ("food insecurity as a symptom of
ecological-social failure -- pay attention") by JUXTAPOSITION and CURATION, never
by a causal arrow this layer draws.

Therefore:
- Every popup field is a transcribed IPC value.
- Causal claims ("drivers") appear ONLY as IPC's own attributed, dated words.
- "Where we are going" is IPC's own projection, attributed to IPC -- and in this
  cut it is DEFERRED entirely (section 2).
- Provenance is a claim that must be TRUE: cite to where the data actually came
  from, or remove and note the gap. Never cite-to-clear.

The subject is human; the restraint is the design. (Access is not understanding.)

--------------------------------------------------------------------------------
## 2. SCOPE -- WHAT THIS CUT IS, AND WHAT IT DEFERS

IN:
- ONE country: Sudan. Not a regional mosaic.
- ONE period: the CURRENT period (2026-02-01 to 2026-05-31), which IPC analysed
  across the entire country (195 localities, 189 area polygons in the file).
- Approach B: real IPC-native vector polygons per analysis area, each carrying a
  transcribed popup. NOT a rasterized re-photograph of IPC's published map.
- Built as a FAMILY MEMBER: shares legend placement, opacity / draping
  discipline, date-pinning, provenance popup, and temporal-axis convention with
  the existing temperature (ERA5) layers, so later co-visualization is a
  compositing job, not a rebuild.

DEFERRED (named, not abandoned -- see section 13):
- The two PROJECTION periods (Jun-Sep 2026 lean; Oct 2026-Jan 2027 harvest).
  They cover only 56 of 195 localities and carry IPC's explicit "caution
  comparing across periods" warning. They become a deliberate, caveated second
  layer. Current-only is both the honest data scope and the right length for a
  Reel.
- The 14 risk-of-Famine areas live in the projection data; risk_of_famine is
  all-false in the current export. Deferred with the projection layer.

DELTA FROM FIRST-CUT MANIFEST: the first cut planned Current PLUS projection
folders; v2 narrows to current-only and moves projections out entirely. The
design converged by simplifying.

--------------------------------------------------------------------------------
## 3. SOURCE -- THE REAL BYTES (fetched this design session)

PRIMARY (source of record): IPC Mapping Tool, public no-key GeoJSON download.
  File fetched: IPC_SD_A_87143417_2026-06-22.geojson (Sudan, current analysis
  "SD February 2026"). IPC-native geometry PLUS full per-area phase attributes
  in ONE file -- no API key needed.
  Provenance line on the layer: "IPC, IPC Mapping Tool."

REPORT (source of national headline figures, drivers, period labels, framing):
  IPC Sudan Special Report, Feb 2026-Jan 2027 (published 2026-06-03; data to
  2026-04-10; National IPC Technical Working Group). National headline figures
  are TRANSCRIBED from the report text, never summed from the polygons
  (section 6).

BACKUP / FUTURE ROUTE (not the build source): HDX dataset "Sudan: Acute Food
  Insecurity Country Data" (data.humdata.org) -- carries ipc_sdn.geojson +
  national/level1/area CSVs spanning 2019-2027. Use as scriptable backup (stable
  resource IDs) and as the route to the deferred historical arc only.

REJECTED as source of record: FEWS NET. By its own statement it is IPC-compatible
  but not IPC consensus and does not always match IPC's results; naming it would
  make the Source line a claim about the wrong analysis body.

--------------------------------------------------------------------------------
## 4. THE FILE SCHEMA -> POPUP FIELD MAPPING (transcribe, do not compute)

228 features total: 189 area polygons (183 Polygon + 6 MultiPolygon) + 39
call-out points (X / triangle / bag overlays -- deferred, section 13). One
period: from_date 2026-02-01, thru_date 2026-05-31.

Per-area properties present in the file, mapped to popup fields:
  area_name                                -> balloon title
  overall_phase_value / overall_phase_label-> MAPPED phase (drives polygon color)
  population / estimated_population         -> area population
  phase1..phase5 population AND percentage  -> FULL breakdown (section 5 -- this
                                              is the structural fix; show ALL of
                                              it, including phase5_population)
  phase3_plus_population / _percentage      -> per-area crisis+ figure
  confidence_level (1 / 2 seen)             -> evidence tier. CONFIRM the
                                              1->Acceptable / 2->Medium mapping
                                              against IPC's evidence-level legend
                                              at pull time (fetched-vs-recalled).
  hfa_value                                 -> humanitarian food assistance level
  risk_of_famine (bool)                     -> all FALSE in current export (a
                                              projection attribute); do not
                                              surface as a live field this cut.
  from_date / thru_date                     -> period window label
  analysis_name / country / export_timestamp-> provenance / "data retrieved"

The file carries NO driver text, NO citation string, NO color ramp. Those come
from the report (drivers, citation) and IPC color guidance (ramp), NOT from the
GeoJSON and NOT from recall.

Not-analysed in the current period collapses to ONE null-phase feature: Abyei
PCA. It is its own styled category (section 7), NOT Phase 1.

--------------------------------------------------------------------------------
## 5. THE ERROR THIS DESIGN FIXES, AND THE STRUCTURAL ANSWER

THE ERROR (do not reintroduce): IPC's MAPPED phase is the highest severity
affecting AT LEAST 20% of an area's population. A locality can hold a Phase-5
(Catastrophe) population BELOW that 20% line and still be MAPPED Phase 4. The
report states ~135,000 people in Phase 5 (Catastrophe) for the current period
(North Darfur, South Darfur, South Kordofan); the GeoJSON carries this in
phase5_population across 23 areas, every one of them mapped P4. The map color
HIDES the worst by construction.

THE STRUCTURAL FIX (two binding requirements):
  (a) The per-area balloon MUST show the full phase1-5 population/percentage
      split, INCLUDING phase5_population -- not just the mapped phase. The
      Catastrophe population must never vanish behind a P4 color again.
  (b) The legend MUST STATE the >=20% mapped-phase rule, so even the glance is
      honest about what the color does and does not mean.

--------------------------------------------------------------------------------
## 6. TOTALS ARE TRANSCRIBED, NEVER SUMMED (explicit non-goal)

A naive sum of the GeoJSON gives 185k Phase 5, 28M Phase 3+, 51.7M total --
versus IPC's published 135k, 19.5M, and 47.5M. The file over-counts when summed
because IDP-settlement units overlap their host localities.

BINDING: national headline figures are TRANSCRIBED from IPC's report text. The
polygons are for per-area color and per-area popups ONLY. Computing any headline
figure from the file is a NON-GOAL -- it would synthesize a wrong, indefensible
number (28M "in crisis"). This is the "transcribe, do not compute" stance with a
concrete near-miss attached.

--------------------------------------------------------------------------------
## 7. STYLING -- PHASE RAMP, NOT-ANALYSED, OPACITY

Phase ramp follows IPC's official 5-step scheme:
  Phase 1 Minimal     -- light green
  Phase 2 Stressed    -- yellow
  Phase 3 Crisis      -- orange
  Phase 4 Emergency   -- red
  Phase 5 Famine      -- dark red
CONFIRM exact hex from IPC color / communication guidance at pull time. Do NOT
embed recalled hex values as authoritative -- fetched-vs-recalled item.
KML COLOR GOTCHA: KML color order is aabbggrr (alpha, blue, green, red), the
reverse of standard RGB hex. The builder converts IPC RGB -> KML order.

NOT-ANALYSED FILL (Abyei PCA): the one element with no temperature-pipeline
analog; design it in, do not retrofit. IPC renders it distinct (grey / hatching).
It is NOT Phase 1 and must not read as "no problem." Render it visually distinct
and label it explicitly in the balloon and legend.

OPACITY / DRAPING: match the temperature layers so this layer composes legibly
underneath or beside a draped climate field. The not-analysed fill in particular
must still read correctly under an overlaid layer. CONFIRM the temperature
layers' opacity / draping values at HEAD before fixing these.

--------------------------------------------------------------------------------
## 8. POPUP / BALLOON TEMPLATE (all fields transcribed, none synthesized)

```
<area_name>
Mapped IPC Phase: <overall_phase_value> (<overall_phase_label>)
Period: Current (<from_date> to <thru_date>)
Population (area): <population / estimated_population>
Phase breakdown (people / %):
  Phase 1 Minimal:     <phase1_population>  (<phase1_percentage>%)
  Phase 2 Stressed:    <phase2_population>  (<phase2_percentage>%)
  Phase 3 Crisis:      <phase3_population>  (<phase3_percentage>%)
  Phase 4 Emergency:   <phase4_population>  (<phase4_percentage>%)
  Phase 5 Catastrophe: <phase5_population>  (<phase5_percentage>%)
Phase 3+: <phase3_plus_population> (<phase3_plus_percentage>%)
Evidence level: <confidence_level mapped to IPC tier>
Assistance (HFA): <hfa_value>
Analysis: <analysis_name>
Source: IPC, IPC Mapping Tool
Data retrieved: <export_timestamp / pull date>
```

The full Phase-1-5 breakdown is mandatory (section 5a). Where phase5_population
> 0 under a P4-mapped area, that line is the most important field in the popup --
it is the hidden Catastrophe made visible. No "Key drivers" line in the per-area
balloon: drivers are national only and ride as a single card (section 9), per
v1's rule that an area with no distinct driver text omits rather than borrows.

--------------------------------------------------------------------------------
## 9. NATIONAL DRIVERS CARD (single card, IPC voice, transcribed)

The GeoJSON carries no per-area driver text, so drivers ride as ONE national
card, transcribed verbatim and attributed to IPC. The report's KEY DRIVERS are
national and structured:
  - conflict
  - displacement and immobility
  - high food prices
  - collapse of health and WASH systems
  - limited humanitarian access

Includes IPC's own naming of the Middle East linkage: IPC's report states the
Middle East conflict contributes to higher fuel, food, and fertilizer prices,
with impacts likely to intensify. TRANSCRIBE IPC's framing, attributed; do NOT
author the Hormuz -> fuel/fertilizer linkage ourselves. The reader who knows
about Hormuz makes the connection. (The v1 Iran-war test case, resolved in the
design's favor: the boundary held and the linkage surfaced through IPC's voice.)

TRANSCRIBE the exact driver wording from the report at build; the bullets above
are the structure, not the final copy.

--------------------------------------------------------------------------------
## 10. TWO-TIER ON-LAYER TEXT (the safety contract)

For the most sensitive statements, fix the words ON the layer so they cannot be
ad-libbed at record time -- but fixed is only safe if it is also SOURCED.

TRANSCRIBED tier -- IPC's own words, lifted verbatim and attributed. Safe by
construction.
  Instances this cut: the national drivers card; the IPC recommended citation
  string; the period label; the analysis date.

COMPOSED tier -- sentences we write because no single IPC line says them. The
dangerous ones; strict treatment. Instances PRESENT in this current-only cut:
  C1. The mapped-vs-population reconciliation:
      "No area is mapped Phase 5, but about 135,000 people are in Phase 5
      (Catastrophe)." (numbers: 135,000 -> report; the Phase-5 area count and
      mapped-P4 fact -> file + report.)
  C2. The >=20% legend rule sentence (a rule-plus-figure statement):
      states that the mapped color is the phase affecting at least 20% of an
      area's population, so sub-20% Catastrophe can sit under a Phase-4 color.
  C3. The causal-restraint statement (what the layer does NOT assert): the layer
      documents where strain is recorded and attributes drivers to IPC; it draws
      no causal arrow of its own.
  Instances DEFERRED to the projection layer (do NOT place this cut): famine-risk
  framing ("N areas at risk of Famine in the projection"); cross-period /
  coverage-comparison caveat ("coverage differs, do not compare").

THE CONTRACT for every composed-tier instance:
  - Hardcode each as a framing-layer text element, SEPARATE from the per-area
    balloons, so the words on screen are fixed.
  - BUILD the sentence in the generator code, with every numeric token carrying a
    `# Source:` comment WITHIN the provenance scanner's lookback window -- NOT
    pasted as a finished string into a template, and NOT living only as text
    inside the .kmz where the scanner cannot see it. The reader sees the sentence
    on the layer; the scanner-visible source lives at the construction site.
  - It MUST trip provenance_scanner.py at Tier-1 and then clear by TRUE sourcing:
    cite to where the number actually came from, or REMOVE and note the gap.
    Never cite-to-clear. A hardcoded sentence that cannot be sourced does not go
    on the layer.

The Reel narration reads FROM the framing text, not alongside it -- words said =
words on layer = sourced words. That closes the ad-lib gap.

(Family-wide version -- making the scanner catch on-layer text across all Earth
System visualizations -- is L-064; asked locally first as item 4 in section 14.)

--------------------------------------------------------------------------------
## 11. VENUE AND REEL ROUTE (first-class section)

ONE KMZ, shown two ways. Instagram Reels record the explorer -- screen, hover,
layer toggles, zoom -- so the interactive KMZ IS the Instagram artifact,
narrated. The design is not just the KMZ; it is the ROUTE the Reel walks. A Reel
is a guided 60-90s walk where Tony controls the order of revelation; the honesty
lives in the PATH, not in a single frame.

CANDIDATE ARC (current-only):
  national figure (transcribed)
  -> the wall of P4 orange/red across Sudan
  -> hover an area whose phase5_population > 0 to reveal the Catastrophe hiding
     under the 20% rule
  -> the national drivers card
  -> close.
The thing that bit us (the hidden Catastrophe) becomes the most honest beat.

CONFIRM-AT-BUILD: the v1 handoff named Kernoi / At Tina as candidate hover areas.
Do NOT hardcode the route's example area from recall -- pick an area that
actually carries phase5_population > 0 in the fetched file (the report locates
Phase 5 in North Darfur, South Darfur, South Kordofan). Verify against the bytes.

AFFORDANCES THE KMZ MUST EXPOSE for the route to be revealable:
  - full phase breakdown in the hover (section 5a / 8),
  - the one not-analysed feature (Abyei PCA) visibly distinct (section 7),
  - the >=20% rule stated on the legend (section 5b),
  - the national drivers card reachable in one step (section 9).

The 60-90s ceiling is a design constraint, not a delivery detail: it caps the
beats and is why current-period-only (no comparability caveat) is the right
length and the right data scope at once.

--------------------------------------------------------------------------------
## 12. KMZ STRUCTURE

```
Document
  Styles:
    style_phase_1 ... style_phase_5     (polygon fill + line, per IPC ramp)
    style_not_analysed                  (distinct fill -- Abyei PCA, section 7)
  Folder: "Current (2026-02-01 to 2026-05-31)"
                                        -> Placemarks, one per analysis area
  Framing-layer text elements          (composed-tier C1/C2/C3, section 10)
  Legend                               (phase ramp + not-analysed + >=20% rule
                                        sentence; ScreenOverlay or inherit the
                                        shared family legend -- CONFIRM at HEAD)
```

Single period folder only (current-only -- no projection folders this cut). The
first cut planned multiple period folders; v2 has exactly one.

Each Placemark:
  - name: area_name
  - styleUrl: by overall_phase_value (or style_not_analysed for Abyei PCA)
  - Polygon / MultiPolygon geometry from the file (183 + 6)
  - description: CDATA HTML balloon carrying the transcribed fields (section 8)

--------------------------------------------------------------------------------
## 13. NON-GOALS / DEFERRED (state, so they do not creep in)

- NO projection periods this cut (Jun-Sep 2026 + Oct 2026-Jan 2027): partial
  coverage (56/195), carries the risk-of-Famine markers and IPC's comparability
  caveat. Deliberate second layer after current-only ships.
- NO regional mosaic (multi-country East Africa): after Sudan proves the
  pipeline; imports the per-country date-reconciliation problem.
- NO historical arc across releases: true time series via the HDX area_long CSV
  (2019-2027); uses the ERA5 TimeSpan machinery when built.
- NO call-out point overlays this cut (the 39 point features: risk-of-Famine
  triangles, HFA bags, limited-access, settlement icons). Rationale:
  risk_of_famine is all-false in the current export, so the famine triangles
  would not render anyway, and the remaining icons add clutter against the
  current-only arc. SCOPE CALL, subject to Tony's retuning -- if the HFA bags or
  limited-access icons earn their place in the route, promote them.
- NO live / auto-updating fetch. Layers are dated, pinned, deliberately
  re-pulled. Silent refresh is a provenance hazard.
- NO causal attribution authored by us. Drivers are IPC-voice only (section 9).
- NO rasterized GroundOverlay that re-photographs IPC's published cartography.
- NO headline figure computed from the polygons (section 6).

--------------------------------------------------------------------------------
## 14. CONFIRM-BEFORE-BUILDING LEDGER (fetch, do not recall)

  1. The exact IPC recommended-citation string -- lift verbatim from the report.
  2. IPC's official phase hex ramp -- from IPC color / communication guidance;
     the GeoJSON carries no colors (fetched-vs-recalled). Remember KML aabbggrr
     byte order.
  3. The confidence_level -> evidence-tier mapping (1->Acceptable, 2->Medium?) --
     confirm against IPC's evidence-level legend.
  4. CONFIRM provenance_scanner.py traverses the food-insecurity generator's
     framing-layer display path at HEAD. If it does not reach that path, making
     it reach it is a build task (the L-064 question, asked LOCALLY first).
  5. The live Earth System KMZ pipeline pattern at HEAD: generator module, KMZ
     assembly, output path, GUI registration, legend convention, opacity /
     draping values, temporal-axis convention (folders vs TimeSpan). Read it from
     the repo before writing integration; do not prescribe from this manifest or
     from memory.
  6. The route's hover-example area (section 11) -- pick one with
     phase5_population > 0 from the fetched file, not from recall.

  (Items 3 and 6 are added in v2; items 1, 2, 4, 5 carry from the handoff.)

--------------------------------------------------------------------------------
## 15. INTEGRATION (read the live pattern first)

Mirror the existing Earth System KMZ pipeline. Likely touch points (CONFIRM
against repo at HEAD per section 14 item 5 -- do not prescribe from recall):
  - the current Earth System KMZ generator module
  - KMZ assembly / output-path conventions used by the temperature layers
  - GUI registration so the layer appears in the Earth System selector
  - shared-family legend convention

MODULE NAME -- ISSUE A (decision needed, section "Issues" below): the name
scenarios_food_insecurity.py is already taken by the ABANDONED period-7 Chart.js
generator. The new KMZ generator must NOT silently reuse or overwrite it. Either
choose a distinct name that follows the live Earth System naming pattern
(confirm at HEAD), or make retiring the period-7 file an explicit, ledgered
action. Default for this manifest: distinct module name, to be fixed at build
against the live pattern; period-7 retirement handled separately if at all.

--------------------------------------------------------------------------------
## 16. VERIFICATION (Mode-5 + smoke, before the layer is "done")

- KMZ opens in Google Earth with no error.
- Phases render where the CURRENT release puts them. NO hardcoded area-to-phase
  claim (the corrected section-10 framing: this round did not allow town-level
  disaggregation, so no "El Fasher / Kadugli at Phase 5" assertion -- that is a
  data gap, not an improvement).
- Not-analysed (Abyei PCA) reads visually distinct from Phase 1 and is labeled.
- Each balloon shows the full transcribed phase1-5 breakdown. SPOT-CHECK that a
  P4-mapped area with phase5_population > 0 surfaces its Catastrophe line -- the
  hidden-worst made visible. A missing phase5 line there is a failure.
- National figures match the IPC report (135k / 19.5M / 47.5M), NOT a polygon
  sum. If any headline shows 28M / 51.7M, the sum leaked in -- failure.
- Composed-tier sentences (C1/C2/C3) trip provenance_scanner.py at Tier-1, then
  clear by true sourcing (cite-to-source or remove-and-note). Provenance is true,
  not merely present.
- Drivers card matches the report verbatim -- any synthesized sentence is a
  failure.
- Opacity / draping consistent with the temperature layers (overlay test).
- Generated source is ASCII, LF line endings.
- The render is the gate. If the map disagrees with the code reading, the render
  wins -- the lesson of the design session itself.

--------------------------------------------------------------------------------
Manifest drafted: June 2026 with Anthropic's Claude Opus 4.8
