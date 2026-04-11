# Paloma's Orrery -- Energy Imbalance Update Handoff v1

## Session Setup | April 3, 2026 | Claude Opus 4.6

-----

## Context

The March 2026 Western Heat Dome revealed a direct physical
connection between Earth's energy imbalance and extreme weather
events. The connection runs through a mechanism called **diabatic
ridge-building**, documented by Neal, Huang, and Nakamura (2022)
for the 2021 PNW heat dome and now observed again in March 2026.

The energy pathway:

1. **Ocean heat content** (energy imbalance accumulates in ocean)
   -> warmer Pacific SSTs (record-warm near-shore temperatures)
2. **Warmer SSTs** -> more atmospheric moisture -> more energetic
   storms (back-to-back Kona lows dumped 2+ trillion gallons on
   Hawaii, March 10-24)
3. **Latent heat release** from those storms -> diabatic ridge-
   building: as moist air ascends and condenses, it releases
   enormous quantities of latent heat, reorganizing the potential
   vorticity structure of the upper troposphere. Low-PV air
   spreads poleward, displacing the jet stream and amplifying a
   downstream ridge over western North America. Research on the
   2021 event showed ~78% of the temperature change along backward
   trajectories was diabatic (latent heating), only ~22% was
   adiabatic subsidence.
4. **Omega block** -> heat dome -> 17 state records -> snowpack
   destruction -> wildfire preconditioning -> water supply crisis

The energy doesn't disappear -- it transforms. Ocean heat ->
atmospheric moisture -> latent heat -> ridge amplification ->
surface temperature records. This is the energy imbalance made
visible.

**El Nino connection:** Signs increasingly point to a significant,
if not strong to very strong, El Nino for 2026-2027. Warmer ocean
-> more moisture -> more energetic storms -> stronger ridges ->
more extreme heat domes. The feedback loop tightens.

-----

## Existing Module

**`energy_imbalance.py`** (~950 lines):

- Modern era (2005-2025) temperature and energy imbalance
- Shows relationship between Earth's energy imbalance (cause) and
  temperature change (effect)
- Reveals climate inertia and committed warming
- Data sources: GISS temperature (monthly JSON), NOAA ocean heat
  content (Levitus, seasonal CSV)
- Plotly dual-axis visualization

-----

## What Needs Work

### 1. Connect the Energy Pathway Visually

The current module shows energy imbalance and temperature as
parallel time series. The March 2026 event provides an opportunity
to show the *mechanism* -- how stored ocean energy becomes an
extreme weather event through the diabatic ridge-building pathway.

Options to explore:
- A new scenario or panel showing the Hawaii -> atmospheric river
  -> ridge -> heat dome chain as a sequence
- Overlay ocean SST anomaly data for the Central Pacific during
  March 2026 on the existing energy imbalance timeline
- Connect the energy imbalance visualization to the Western
  Heatwave scenarios as linked narratives

### 2. Update Data Through 2026

- GISS temperature data: extend through early 2026
- Ocean heat content: update with latest Levitus data
- March 2026 will likely be a visible spike in the temperature
  record

### 3. El Nino Integration

- ENSO state transition: La Nina -> neutral -> developing El Nino
- Historical El Nino events overlaid on energy imbalance timeline
- Projected energy imbalance implications of a strong 2026-27
  El Nino

### 4. Diabatic Ridge-Building as Encyclopedia Content

The mechanism is well-documented and could be an encyclopedia
entry for the energy imbalance visualization, similar to the
omega block entry in the heatwave scenarios. Key references:

- Neal, Huang, and Nakamura (2022): local wave activity budget
  showing upstream diabatic heating builds blocking ridge
- Oertel et al. (2023): "Everything Hits at Once" -- ensemble
  sensitivity experiments showing anomalous western Pacific
  rainfall triggered cascade that built extreme ridge
- Swain (Weather West, March 2026): identified the same
  mechanism operating in the March 2026 event via the Hawaii
  Kona lows and atmospheric river

-----

## Key Sources

- **Diabatic mechanism:** cah2oresearch.com article "The Diabatic
  Engine Behind March 2026's Record-Shattering Western Heat Dome"
  (March 17, 2026) -- comprehensive review linking 2021 and 2026
  events through the same physical mechanism
- **Weather West:** Daniel Swain's analysis confirming "substantial
  contribution to the magnitude and persistence of the Southwestern
  heat dome by highly anomalous upstream diabatic heating in the
  Central Pacific, related to record-breaking rainfall and severe
  flooding in Hawaii"
- **Climate Adaptation Center:** "2026 Southwest U.S. Record Heat
  Wave" (April 2, 2026) -- back-to-back Kona lows dumped 2+
  trillion gallons on Hawaii; atmospheric river rode jet stream
  to Pacific NW; latent energy strengthened the ridge
- **NWS Honolulu:** March 10-24, 2026 severe weather summary --
  Maui summit recorded 54.92 inches; Molokai 41.58 inches;
  widespread flash flooding across all islands
- **Climate Central:** CSI 5 covered 3 million sq km (29% of
  continental US) on March 20 -- largest CSI 5 extent on record

-----

## Connection to Existing Scenarios

The energy imbalance update would link to the completed Western
Heatwave March 2026 scenario (9 snapshots, all ERA5). The two
modules tell complementary stories:

- **Heatwave scenario:** *what* happened (temperature anomalies,
  station records, spatial progression)
- **Energy imbalance:** *why* it happened (ocean heat storage,
  diabatic ridge-building, the physical mechanism connecting
  stored energy to extreme surface temperatures)

This is the "data preservation is climate action" philosophy at
its deepest: the data shows the event, the narrative explains the
mechanism, the energy imbalance connects it to the planetary-scale
forcing that made it possible.

-----

## Approach Suggestion

This is a design-first project (Mode 1 or iterative design
planning). The question isn't "how do we code it" but "what's
the right way to visualize the connection between energy imbalance
and a specific extreme event." Multiple rounds of conversation
before any code.

Potential Mode 7: Gemini for the atmospheric physics (diabatic
heating quantification, PV dynamics), Claude for implementation
and visualization architecture.

-----

*"Are the recent Hawaii Kona events and the El Nino related to
the heat waves? Should we update our earth system energy imbalance
visualizations?"* -- Tony, April 3, 2026

*Module updated: April 3, 2026 with Anthropic's Claude 4.6*
