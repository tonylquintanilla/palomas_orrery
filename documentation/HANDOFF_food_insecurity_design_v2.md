# HANDOFF -- Food Insecurity Visualization, Design Re-Converged (v2)

Tony Quintanilla, PE | Claude | Earth System track | June 22, 2026
Base SHA: f1834dc (f1834dc487c24a07a08bceaee1142df86cc679ee), branch main.
Built on HEAD f1834dc PLUS the un-pushed L-001 revision and new L-064 from this
session (2026-06-22). Push handoff + ledger edits together. When build begins,
build base = HEAD at that time -- confirm the SHA round trip first.
Type: DESIGN SESSION (zero code). First-class output.
Supersedes: HANDOFF_food_insecurity_design_v1.md (de12f56) -- now reference only.
Companion: MANIFEST v2 (PENDING -- not yet written; see "On the manifest" below).

This handoff is the reasoning trail: WHY the design is what it is, what changed
since v1, and where the discipline bites. The manifest, when written, is the
executable contract. Read this first.

--------------------------------------------------------------------------------
## WHAT CHANGED SINCE v1, IN ONE BREATH

v1 was sound but it was written before the data was in hand and before the venue
was pinned. This session we fetched the real bytes, read IPC's own report, and
let the design re-converge -- and it converged by SIMPLIFYING every round:
East Africa -> Sudan -> Current period only; the popup got richer while the
scope got cleaner. That direction (each round simpler) is the signal the design
has stabilized and is ready to write down. Nothing here reopens v1's core stance
(synthesize nothing, transcribe everything, attribute to IPC, defer causation to
the reader). It sharpens the scope, upgrades the source, fixes one real error,
and adds two design decisions v1 could not have made without the data and the
venue.

--------------------------------------------------------------------------------
## WHY WE SLOWED DOWN (the operating reason)

The food layer is not visually complex. What is complex is the SUBJECT and the
duty to show it accurately to non-experts in a brief view (the gallery at
palomasorrery.com, then Reels on instagram palomas_orrery). The work left behind
earlier was not wrong; it moved fast on a hard subject and got lost in causal
detail (goats, sorghum, specific market towns) that Tony -- correctly -- does not
feel competent to adjudicate, and that no honest layer should author. The fix is
not more cleverness; it is restraint plus the right scope. This handoff exists so
the next session does not rebuild on a stale or over-reaching base.

--------------------------------------------------------------------------------
## THE DECISIONS, IN ORDER (the convergence path)

1. SCOPE -> Sudan, then Current period only. There is no single "East Africa
   release": IPC publishes per country on non-aligned schedules, so a regional
   map is a mosaic of mismatched date windows. Sudan is the first honest rung.
   Within Sudan, Phase 1 is the CURRENT period only (Feb-May 2026), which IPC
   analysed across the entire country (195 localities). The two projections
   (Jun-Sep 2026 lean; Oct 2026-Jan 2027 harvest) cover only 56 of 195 localities
   and carry IPC's explicit "caution comparing across periods" warning -- they
   are DEFERRED to a deliberate, caveated second layer. Current-only is both the
   honest data scope and the right length for a 60-90s Reel.

2. SOURCE -> IPC Mapping Tool no-key GeoJSON (supersedes the HDX-mirror plan).
   The IPC key request went unanswered for over a week, so v1's fallback was the
   HDX mirror. This session found a better path: IPC's own Mapping Tool offers
   public, no-key GeoJSON download. It is IPC-native geometry plus full per-area
   phase attributes in ONE file, so the key is no longer needed at all.
   Provenance UPGRADES from "IPC, retrieved via HDX" to plain "IPC, IPC Mapping
   Tool." HDX is demoted to a scriptable backup (stable resource IDs) and the
   route to the deferred historical arc (its area_long CSV spans 2019-2027).
   FEWS NET stays rejected as the source of record: by its own statement it is
   IPC-compatible but not IPC consensus and does not always match IPC's results,
   so naming it would make the Source line a claim about the wrong analysis body.

3. THE ERROR WE FIXED -> mapped phase vs population phase. Reading the GeoJSON's
   overall_phase_value (which tops out at 4) I concluded "zero Phase 5, no
   famine." That was wrong, and on this subject the difference is not academic.
   IPC's mapped phase is the highest severity affecting AT LEAST 20% of an area's
   population. A locality can hold a Phase-5 (Catastrophe) population below that
   20% line and still be MAPPED Phase 4. The report states ~135,000 people in
   Phase 5 (Catastrophe) for the current period (North Darfur, South Darfur,
   South Kordofan); the GeoJSON carries this in phase5_population across 23 areas,
   every one of them mapped P4. The map color HIDES the worst by construction.

4. THE STRUCTURAL FIX -> the popup carries the FULL phase breakdown. Because the
   color hides sub-20% Catastrophe populations, the per-area balloon must show the
   full phase1-5 population/percentage split, including phase5_population, not just
   the mapped phase. The legend must STATE the 20% rule so even the glance is
   honest about what the color does and does not mean. This is the design's
   structural answer to the error in (3): never let the Catastrophe population
   vanish behind a P4 color again.

5. TOTALS ARE TRANSCRIBED, NEVER SUMMED. Verifying the 135k, a naive sum of the
   GeoJSON gave 185k for Phase 5, 28M for Phase 3+, and 51.7M total -- versus
   IPC's published 135k, 19.5M, and 47.5M. The file over-counts when summed
   because IDP-settlement units overlap their host localities. So national
   headline figures get transcribed from IPC's text; the polygons are for
   per-area color and per-area popups only. Computing the headline from the file
   would have shown 28M in crisis -- a synthesized, wrong, indefensible number.
   This is v1's "transcribe, do not compute" stance, now with a concrete
   near-miss attached.

6. DRIVERS -> a single NATIONAL card in IPC's voice. The report's KEY DRIVERS are
   national and structured: conflict; displacement and immobility; high food
   prices; collapse of health and WASH systems; limited humanitarian access. The
   GeoJSON carries no per-area driver text, so we do NOT invent per-area prose --
   the drivers ride as one national card, transcribed and attributed. Per v1's
   rule, if an area has no distinct driver text, we omit rather than borrow.

7. THE IRAN-WAR TEST CASE RESOLVED -- in the design's favor. v1 set the boundary:
   we never author the Hormuz -> fuel/fertilizer linkage ourselves; we carry it
   ONLY if IPC's own analysis names it. IPC's report now names it: the Middle East
   conflict contributes to higher fuel, food, and fertilizer prices, with impacts
   likely to intensify. So we transcribe IPC's framing, attributed, and the reader
   who knows about Hormuz makes the connection themselves. The boundary held and
   the linkage surfaced through IPC's voice, not ours. This is the worked example
   from v1 coming true.

8. CORRECTED SECTION-10 FRAMING (replaces v1's stale Sept-2025 spot-check). v1
   verified against "El Fasher and Kadugli at Phase 5." That is retired -- but
   NOT because conditions improved. IPC says the data this round did not allow
   town-level disaggregation, so results are not directly comparable to the prior
   analysis, and concerns remain high. The honest current framing: no area mapped
   Phase 5; ~135k in Catastrophe; El Fasher/Kadugli not town-disaggregated this
   round (a data gap, not an improvement); 14 areas at risk of Famine in the
   Jun-Sep worst-case projection. Verification becomes "phases render where the
   CURRENT release puts them," with no hardcoded area-to-phase claim.

--------------------------------------------------------------------------------
## VENUE: ONE KMZ, SHOWN TWO WAYS (the artifact decision)

The gallery and Instagram are not two artifacts. Instagram Reels record the
explorer -- screen, hover, layer toggles, zoom -- so the interactive KMZ IS the
Instagram artifact, narrated. One thing to build, shown two ways. This dissolves
the glance-versus-fidelity tension: a Reel is not a glance, it is a guided 60-90s
walk where Tony controls the order of revelation. The honesty lives in the PATH
through the map, not in a single frame.

Consequence: the design is not just the KMZ, it is the ROUTE the Reel walks. For
Sudan the route does ethical work. A candidate arc, current-only:
  national figure -> the wall of P4 orange -> hover Kernoi/At Tina to reveal the
  Phase-5 population hiding under the 20% rule -> the national drivers card ->
  close.
The thing that bit us (the hidden Catastrophe) becomes the most honest beat in
the piece. A still could not do that; a path can. So the KMZ must be built with
the affordances the route needs to be revealable:
  - phase breakdown in the hover (decision 4),
  - the one not-analysed feature (Abyei PCA) visibly distinct,
  - the >=20% rule stated on the legend so narration can point at it,
  - the national drivers card reachable in one step.

The 60-90s ceiling is a design constraint, not a delivery detail: it caps how
many beats v1 can carry, and current-period-only fits one clean arc without the
projection's comparability caveat. Current-only is the right DATA scope and the
right LENGTH at once.

--------------------------------------------------------------------------------
## TWO-TIER ON-LAYER TEXT (the new safety decision)

For the most sensitive statements, fix the words ON the layer so they cannot be
ad-libbed at record time -- but fixed is only safe if it is also SOURCED. The old
El Fasher Phase-5 line was effectively hardcoded too, and it was wrong because it
was recalled, not sourced. So on-layer text splits by how its words get authority:

  TRANSCRIBED tier -- IPC's own words, lifted verbatim and attributed: the drivers
  card, the recommended citation, the period label, the analysis date. Safe by
  construction; IPC authored them, we carry them.

  COMPOSED tier -- sentences we write because no single IPC line says them. These
  are the dangerous ones and they get the strict treatment. Statement TYPES that
  live here (instances belong in the manifest):
    - mapped-vs-population reconciliations ("no area mapped Phase 5, but ~135k in
      Catastrophe");
    - any rule-plus-figure sentence (a methodology rule combined with a number);
    - famine-risk framing (the "N areas at risk of Famine in the projection" line,
      when projections land);
    - cross-period / coverage-comparison framing (the "coverage differs, do not
      compare" caveat, when projections land);
    - any on-layer statement of what the layer does NOT assert (causal restraint).

THE CONTRACT for the composed tier:
  - Hardcode each as a framing-layer text element (separate from the per-area
    balloons), so the words on screen are fixed.
  - BUILD the sentence in the generator code, with every numeric token carrying a
    `# Source:` comment within the scanner's lookback window -- NOT pasted as a
    finished string into a template, and NOT living only as text inside the .kmz
    where the scanner cannot see it. The reader sees the sentence on the layer;
    the scanner-visible source lives at the construction site in the generator.
  - It MUST trip provenance_scanner.py at Tier-1 and then clear by true sourcing:
    cite to where the number actually came from, or REMOVE and note the gap.
    Never cite-to-clear; a hardcoded sentence that cannot be sourced does not go
    on the layer.

The Reel narration then reads FROM the framing text, not alongside it -- the words
said equal the words on the layer equal the sourced words. That closes the ad-lib
gap completely.

This is the "show the envelope / say so in the hover" principle applied to the
highest-stakes claims: where a statement is composed rather than transcribed, mark
it as ours and source every number in it. The family-wide version of this -- making
the provenance scanner catch on-layer text across all Earth System visualizations,
not just food insecurity -- is logged as L-064.

--------------------------------------------------------------------------------
## THE DATA, AS FETCHED THIS SESSION (so the manifest writes against real bytes)

GeoJSON: IPC_SD_A_87143417_2026-06-22.geojson (IPC Mapping Tool, Sudan, current
analysis "SD February 2026"). 228 features: 189 area polygons (183 Polygon, 6
MultiPolygon) + 39 call-out points (the X / triangle / bag overlays). One period
only: 2026-02-01 to 2026-05-31. Per-area properties present and transcribe-ready:
  area_name; overall_phase_value + overall_phase_label (mapped phase);
  population / estimated_population; phase1..phase5 population AND percentage;
  phase3_plus_population + phase3_plus_percentage; confidence_level (evidence tier
  -- 1/2 seen, maps to Acceptable/Medium in IPC's legend); hfa_value (humanitarian
  food assistance level); risk_of_famine (bool; all false in the CURRENT export --
  it is a projection attribute); from_date / thru_date; analysis_name; country;
  export_timestamp.
Not-analysed in the current period collapses to ONE null-phase feature (Abyei PCA).
The file carries NO driver text, NO citation string, NO color ramp.

Report: IPC Sudan Special Report, Feb 2026-Jan 2027 (published 2026-06-03; data to
2026-04-10; National IPC Technical Working Group). Source of the national headline
figures (transcribe, do not sum), the KEY DRIVERS card, the period-window labels,
and the prose the corrected section-10 framing is drawn from.

HDX dataset "Sudan: Acute Food Insecurity Country Data" (data.humdata.org): carries
ipc_sdn.geojson + national/level1/area CSVs, spans 2019-2027. Scriptable backup +
historical-arc route only; not the v1 build source.

--------------------------------------------------------------------------------
## STILL TO SOURCE BEFORE BUILD (fetch, do not recall)

  1. The exact IPC recommended-citation string -- lift verbatim from the report.
  2. IPC's official phase hex ramp -- from IPC color/communication guidance; the
     GeoJSON carries no colors, so this is a fetched-vs-recalled item (do not embed
     recalled hex). Remember the KML aabbggrr byte order (alpha, blue, green, red).
  3. The exact projection-period windows + the 14 risk-of-Famine areas -- only when
     the projection layer is built (deferred); fetched from the projection export,
     not recalled.
  4. CONFIRM provenance_scanner.py traverses the food-insecurity generator's
     framing-layer display path at HEAD -- if it does not reach that path, making
     it reach it is a build task (this is the L-064 question, asked locally first).
  5. The live Earth System KMZ pipeline pattern at HEAD (generator module, KMZ
     assembly, output path, GUI registration) -- read it from the repo before
     writing integration; do not prescribe from this handoff or from memory.

--------------------------------------------------------------------------------
## DEFERRED LEDGER (named, not abandoned)

  - Projection layer (Jun-Sep 2026 + Oct 2026-Jan 2027): partial coverage (56/195),
    carries the famine-risk markers and IPC's comparability caveat. Deliberate
    second layer after current-only ships.
  - Regional mosaic (multi-country East Africa): after Sudan proves the pipeline;
    imports the per-country date-reconciliation problem.
  - Historical arc across releases: true time series via the HDX area_long CSV
    (2019-2027); uses the ERA5 TimeSpan machinery when built.
  - Call-out point overlays (risk-of-Famine triangles, HFA bags, limited-access,
    settlement icons): 39 point features are in the file; first-cut inclusion is a
    manifest scope call.

--------------------------------------------------------------------------------
## ON THE MANIFEST (Tony's step 3 -- advice)

Recommendation: write the manifest v2 NEXT SESSION, not now. Reason: the manifest
is the build contract, and writing the executable spec before the design has fully
settled is exactly the move that produced the work we are setting aside. The design
is now stable (it converged by simplifying), but the manifest should be written
against HEAD at build time, AFTER this handoff and the ledger edits are pushed, so
it is built on the real current base and not on un-pushed deltas. Writing it now,
on an un-pushed base, reintroduces the stale-base risk the round trip exists to
prevent.

What the manifest v2 must specify (the delta from manifest v1):
  - Current-period-only scope; projections explicitly out of v1, in the deferred
    layer.
  - Source = IPC Mapping Tool GeoJSON; field-by-field popup mapping from the real
    schema above; provenance line "IPC, IPC Mapping Tool."
  - Popup carries the full phase1-5 breakdown including phase5_population; legend
    states the >=20% mapped-phase rule.
  - National drivers card (transcribed, five drivers, IPC voice, includes IPC's
    Middle East fuel/fertilizer naming).
  - Totals transcribed from the report; an explicit NON-goal: do not sum the
    polygons for any headline figure.
  - The two-tier on-layer text design: the framing-layer text elements, the exact
    composed-tier sentences with their per-number source bindings, and the build
    mechanic that makes each numeric token scanner-visible within lookback.
  - The Reel route as a first-class section: the arc, and the affordances the KMZ
    must expose for it.
  - The confirm-at-HEAD ledger (items 1-5 above).

--------------------------------------------------------------------------------
## FOR THE BUILDER CLAUDE (when code begins)

  - This is the reasoning trail; the manifest v2 is the contract. If the two ever
    disagree, that disagreement is a flag to raise, not a thing to silently
    resolve.
  - The discipline that governs every field: synthesize nothing, transcribe
    everything, attribute to IPC, defer causation to the reader. The subject is
    human; the restraint is the design.
  - Confirm the SHA round trip and SHA-pin the build base before writing anything.
  - Read the live Earth System KMZ pattern from the repo at HEAD; do not invent the
    integration API from memory.
  - The render is the gate. If the map disagrees with the code reading, the render
    wins -- the lesson of this very session.

--------------------------------------------------------------------------------
Handoff drafted: June 2026 with Anthropic's Claude Opus 4.8
