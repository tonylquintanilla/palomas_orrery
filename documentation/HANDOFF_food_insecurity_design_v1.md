# HANDOFF -- Food Insecurity Visualization, Design Re-Open (v1)

Tony Quintanilla, PE | Claude | Earth System track | June 5, 2026
Base SHA: de12f56 (de12f5635a6f04c36b9e62509f24e517cce7ad07)
Type: DESIGN SESSION (zero code). First-class output.
Companion: MANIFEST_food_insecurity_sudan_first_cut.md (the executable spec).

This handoff is the reasoning trail. The manifest says WHAT to build; this says
WHY, what was rejected, and where the discipline bites. Read this first.

--------------------------------------------------------------------------------
## SESSION PURPOSE

Re-open the food-insecurity visualization. Explicit instruction: do NOT continue
from prior work -- rethink the approach. Start basic: an IPC picture of East
Africa where insecurity is most acute now, rendered as KMZ heat-map-style layers
like the temperature maps, with no conclusions or attributions drawn by us at
this stage.

--------------------------------------------------------------------------------
## CONVERGENCE PATH (the decisions, in order)

1. "Grid" clarified -- Tony meant no special geometry, just a heatmap over the
   data's own spatial units.

2. Categorical, not continuous. The ERA5 temperature maps are a continuous
   scalar field where interpolation is meaningful. IPC is an ORDINAL category
   (Phase 1-5) per analysis area. A smoothed heatmap would invent gradients the
   data does not claim -- false precision, doubly wrong on a real-people subject.
   The honest render is a CATEGORICAL heatmap: hard-edged polygons, official IPC
   ramp. Hard borders are correct for IPC, not a flaw.

3. KMZ form: chose B (vector polygons), rejected A and C for the first cut.
   - A (rasterize polygons into a PNG GroundOverlay): fastest, reuses the
     temperature chassis, but it is just an image -- no clickable units, no
     metadata. Rejected: the metadata is where the value is.
   - C (hybrid raster fill + invisible clickable polygons): most work. Deferred.
   - B (real KML polygons with per-area popups): faithful, hard edges honest,
     metadata carried. Chosen.

4. Dynamism -- three senses separated:
   - (1) Within a single release: every IPC release carries a Current period
     plus one or two Projections. This is "where we are" + "where we are going,"
     already in the one downloaded file. CHOSEN as the first cut.
   - (2) Time series across releases (historical arc): real animation, would use
     the ERA5 TimeSpan / time-slider machinery. DEFERRED (bigger data assembly).
   - (3) Live auto-update: REJECTED by design -- silent refresh is a provenance
     hazard. "Stays current" means dated, labeled, deliberately re-pulled layers.

5. Country pick: SUDAN. Most acute (confirmed Phase 5 / Famine in El Fasher and
   Kadugli as of Sept 2025), most decision-relevant. Tradeoff accepted: Sudan
   carries significant "not analysed" areas, so the not-analysed rendering must
   be built on day one rather than proven on a cleaner country first. (South
   Sudan / Kenya were the cleaner-pipeline alternatives; Tony chose the most
   acute case.)

6. The fork the data revealed: there is NO single "East Africa release." IPC
   analyses are per-country, independent schedules, non-aligned period windows
   (Sudan Feb-May 2026; South Sudan ~Apr-Jul 2026; Kenya different again). A
   regional map is a mosaic of releases with a date-reconciliation problem.
   This drove convergence to one country first. Mosaic is deferred.

7. Why build at all (the "is this just a duplicate?" gate). Honest answer: as a
   STANDALONE Sudan food map it is close to a duplicate -- IPC already has an
   interactive tool with popups. The value is NOT standalone. It is the RUNG:
   the food layer that can sit in the SAME navigable frame, same legend family,
   same temporal axis, as the climate stressors. That same-frame co-visualization
   is the one thing IPC's house map structurally cannot do. So: build it, and
   build it to a FAMILY SPEC, not a one-off.

8. The frame Tony named: food insecurity as one tracked member of a family of
   stressors -- heat (new European heat wave), ocean acidification, ocean heat /
   El Nino. Not separate exhibits; instances of one statement -- the system under
   strain, pay attention. The thesis is carried by the COLLECTION; each layer
   stays honest about what it is. Convergence gift: IPC's Current/Projection
   structure already IS the "where we are / where we are going" half of the
   thesis, native to the data.

9. Attribution -- the struggle, resolved. Tony's real worry: getting lost in
   attributions he does not feel competent to create. Resolution: two senses of
   "attribution" were conflated.
   - CAUSAL ("why"): the hard one. IPC has ALREADY done it -- named drivers,
     Evidence Level tiers, a standing Famine Review Committee. We never author
     it; if it appears, it is IPC's attributed, dated words.
   - PROVENANCE ("where from"): the only one we do, and it is transcription, not
     creation -- a citation string copied faithfully.
   The source even MODELS the restraint: the FRC declined to classify the
   Feb-May 2026 window because conflict makes it too volatile to project. Our
   deferral of attribution MATCHES IPC's own stated humility.

10. Drivers in the popup: YES (Tony's call), carried as IPC's attributed voice.
    Reason: the drivers are the hooks a reader uses to connect this layer to the
    others. Either way they matter; including them serves the reader's own
    connection-making.

--------------------------------------------------------------------------------
## THE IRAN-WAR TEST CASE (why we do not author causation)

Tony noted, as a reader's side comment, that the 2026 Iran war has exacerbated
Sudan's crisis. Checked rather than affirmed (a causal claim from memory is the
same failure as a Source-comment over recalled data). It checks out, and the
mechanism is instructive: not Iran in Sudan's civil war, but the energy/
fertilizer channel -- Strait of Hormuz closure -> fuel and fertilizer price
shock -> Sudanese farmers cutting sorghum/millet/sesame planting. Sourced across
Reuters, CFR, Think Global Health, and the 2026 Global Report on Food Crises.

This is the live demonstration of the design boundary:
- It is a connection across sources our food layer does NOT contain.
- It emerged recently; a year ago it was not a factor. Baking it into a static
  popup would freeze a moving linkage and assert attribution we cannot
  adjudicate.
- So: our popup carries IPC's named drivers in IPC's dated voice. A reader who
  knows about Hormuz looks at "economic decline / staple prices" and makes the
  Iran connection THEMSELVES. That is the whole point of same-frame curation.
- Whether the words "Iran war" ever appear depends ONLY on whether IPC's own
  next Sudan analysis names fuel/fertilizer costs. If IPC writes it, transcribe
  it. If IPC folds it into "economic decline," carry that. Never upgrade IPC's
  framing with the better-sourced outside claim. That restraint is the discipline.

--------------------------------------------------------------------------------
## OPEN ITEMS / DEFERRED LEDGER

Deferred (named, not abandoned):
- Regional mosaic (multi-country East Africa) -- after Sudan proves the pipeline.
- Historical arc across releases -- true time series, TimeSpan machinery.
- Hybrid raster+vector (approach C) -- if the look ever needs the raster fill.
- Assistance-overlay rendering in the first cut -- scope TBD (fields designed in
  either way so it is not a retrofit).

Confirm-at-pull-time (see manifest section 9 for the full ledger): IPC data
access/format/fields, geometry source, exact phase hex, citation string, current
release windows, driver wording, existing KMZ pipeline pattern in repo, family
temporal-axis convention.

--------------------------------------------------------------------------------
## FOR THE BUILDER CLAUDE

- This was a pure design session. The manifest is the contract; this handoff is
  the intent behind it. If the two ever disagree, the disagreement is a flag to
  raise, not a thing to silently resolve.
- The discipline that governs every field: synthesize nothing, transcribe
  everything, attribute to IPC, defer causation to the reader. The subject is
  human; the restraint is the design, not an afterthought.
- Pull ground truth at HEAD and SHA-pin your base before building. de12f56 is
  the design base; the build base is whatever HEAD is at build time -- confirm
  the SHA round trip.
- Read the live Earth System KMZ pattern from the repo before writing the
  integration. Do not prescribe it from this handoff or from memory.

--------------------------------------------------------------------------------
Module updated: June 2026 with Anthropic's Claude Opus 4.8
