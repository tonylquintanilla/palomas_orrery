# ENSO Standalone Chart -- Design Spec (Map Before Build)

Tony Quintanilla, PE | Claude (Opus 4.8) | June 18, 2026
Status: DESIGN / MAP -- v2. Open questions RESOLVED this session; build queued for
next session. No code this session. This is the handoff artifact for the build.
Drafted: June 2026 with Anthropic's Claude Opus 4.8.

---

## 0. Purpose

A standalone Earth-System gallery chart for ENSO that (a) shows the El Nino /
La Nina state honestly in a warming climate by leading with RONI, (b) shows the
developing 2026 event with a forecast drawn as a calibrated envelope, and (c)
teaches the ENSO <-> energy-imbalance relationship as a MECHANISM (schematic +
cited physics in the "i" card), NOT as a data overlay that could be misread as a
trend.

Audience is a gallery viewer, not a paper reader. The chart must not support a
naive misreading. That constraint drove every decision below.

External validation (June 2026): The Economist / The Climate Brink published a
RONI-led Nino-3.4 chart for this same event -- independently the same call as D2.
Their forecast is a single multi-model MEDIAN line spiking toward +2.5; that lone
line reads as near-certain and is exactly the choice we reject (see D6). Their
chart also leaves the forecast BASIS unstated under a RONI history -- the seam we
designed D2 around. Both are improved on below.

---

## 1. Agreed architecture (resolved forks)

- **D1 -- Standalone, single-unit.** New ENSO chart, y-axis deg C only. No W/m^2,
  no EEI/OHC line here. Energy-budget relationship told and cross-linked, not drawn.
- **D2 -- Native basis, both lines.** RONI is the lead series. ONI is a thin
  overlaid line so the divergence is visible AND so the forecast has its native
  basis to hang from. Nothing converted; nothing faked.
- **D3 -- Relationship as mechanism, no statistic.** ENSO <-> energy-imbalance link
  lives in the "i" card as a charge/discharge schematic (no time axis) with cited
  physics. No computed covariance / coefficient (outside the maintainer's
  interpretive control; a shared-axis overlay of two trending series invites the
  spurious co-trend read).
- **D4 -- Phases and strength computed, not recalled.** Shading derived from RONI
  crossing +/-0.5 deg C for 5 consecutive overlapping seasons. Strength descriptor
  from RONI magnitude, computed -- never a recalled Moderate/Strong/Super label.
- **D5 -- Sequencing.** Standalone chart FIRST (isolated new module, Mode-5
  verified). Energy-imbalance narrative correction + 2026 band is a SEPARATE,
  LATER, targeted Mode-1 pass (Section 5).
- **D6 -- Forecast as a CALIBRATED envelope.** Plume mean + skill-scaled Gaussian
  (official IRI product; width set by historical forecast skill, widest through the
  spring barrier). NOT a single median line. The upper edge is where the
  "strongest ever" possibility lives -- shown as possibility, not promise. Direct
  application of the project's "Show the Envelope of the Unknowable" principle.

---

## 2. Data sources

### 2.1 RONI (history) -- CONFIRMED this session
- URL: https://www.cpc.ncep.noaa.gov/data/indices/RONI.ascii.txt
- Plain ASCII: columns SEAS (3-month season), YR, ANOM. 1950 -> present, monthly.
  1991-2020 base. Same fetch shape as the GISS / NSIDC sources already in
  fetch_climate_data.py.
- Definition: Nino-3.4 SST anomaly minus tropical-mean (20N-20S) SST anomaly,
  variance-matched to ONI. Dampens recent El Ninos / amplifies La Ninas vs ONI by
  removing the background tropical warming trend.

### 2.2 ONI (history) -- CONFIRM EXACT FILE AT BUILD
- Likely https://www.cpc.ncep.noaa.gov/data/indices/oni.ascii.txt (NOT verified;
  do not hardcode until checked at HEAD). Want standard ONI, not a detrended
  variant. Thin overlaid line; anchors the plume.

### 2.3 Forecast plume (2026) -- EXISTS, FETCH FORMAT TBV AT BUILD
- Source: IRI / CCSR ENSO prediction plume. ~20 dynamical + statistical models,
  Nino-3.4 SST anomaly, nine overlapping 3-month seasons, monthly. Published as
  graph + table (SST_table.html style archive).
- Native basis is ONI / Nino-3.4 -- hangs off the ONI line, NOT RONI. No standard
  published RONI plume. STATE THE BASIS IN HOVER (the Economist chart's omission is
  the thing we fix).
- RESOLVED (D6): draw the plume MEAN + skill-scaled Gaussian envelope (the official
  calibrated product), NOT the raw min/max spread and NOT a lone median.
  Rationale: raw model spread is not a calibrated probability (correlated models,
  typically too narrow); the skill-scaled Gaussian is calibrated to real forecast
  skill and is what the headline El Nino/Neutral/La Nina probabilities derive from.
- FALLBACK: if IRI's skill-calibration parameters are not cleanly fetchable, draw a
  model-spread band (interquartile or min/max) captioned explicitly "model spread,
  not a calibrated probability." Honest either way.
- Main build risk: the plume scrape is fiddlier than the ascii files. First build
  task: confirm a stable parse or fall back to a manually-updated cached CSV (the
  three-tier cache -> fetch -> fallback pattern from the Western Heatwave module).

---

## 3. The chart (traces + layout)

Single 2D Plotly teaser, y-axis deg C, x-axis decimal year.

1. RONI history -- the lead series, drawn as a FILLED-TO-ZERO seesaw: red fill for
   El Nino (above zero), blue fill for La Nina (below zero). Recognizable and
   gallery-striking (the Economist/Climate Brink idiom). Filled bands use
   hoverinfo='skip'; info via a single info marker / annotations, not every vertex.
2. ONI history -- thin overlaid line beneath/over the seesaw, so the RONI-ONI
   divergence (the teaching point) stays visible.
3. Threshold reference lines at +0.5 / -0.5; zero line.
4. "Today" marker: vertical line at last observed value; everything right is forecast.
5. Forecast: calibrated Gaussian envelope band + mean, ONI basis, hung off the ONI
   line at "today". Styled clearly as forecast (translucent envelope, dashed mean);
   basis stated in hover; upper edge is the "record possible" region.
6. 2026 event shown NOW, PROVISIONAL, with preliminary/developing flagging (Western
   Heatwave convention) -- it is already front-page news (Economist, June 16 2026).

No elements beyond the above (Tony: let it land; each element earns its place).

Conventions (bake in at build): ASCII only, LF; no unicode (no deg sign, arrows,
em-dash). Hover states value + season/date, and "forecast (Nino-3.4 / ONI basis)"
on the plume. Cross (+) for info markers only. Module docstring + credit line.
Mobile + desktop variants from the start.

---

## 4. The "i" card -- mechanism, not overlay

- Visual: a PLOTLY-DRAWN charge/discharge schematic (no time axis, so it cannot be
  misread as a trend). Two states:
  - La Nina (charging): strong trades bury warm water subsurface in the west, cold
    tongue east, planet retains energy -- net TOA uptake.
  - El Nino (discharging): warm water surfaces east, ocean releases heat to the
    atmosphere (GMST "mini global warming") AND the warm surface radiates more to
    space (OLR), so net imbalance temporarily DIPS, a few months after the SST peak.
- Card text (cited physics, sourced -- not recalled numbers):
  - El Nino -> planet temporarily sheds energy; deepest net-imbalance minima
    coincide with mature El Ninos (1998, 2011, 2016, 2024). La Nina -> charging.
    Lag a few months.
  - Mechanism correction: the El Nino imbalance dip is led by OUTGOING LONGWAVE from
    the warm surface, with increased cloud reflection a secondary contributor -- NOT
    primarily "reflecting more sunlight."
  - RONI rationale: convection responds to RELATIVE (gradient) SST, so RONI is the
    better predictor of the atmospheric response; and ONI co-trends with OHC/EEI
    (both ride GHG warming), so RONI is the honest index to relate to the budget.
- Cross-link: card -> energy-imbalance chart; energy-imbalance chart -> this chart.
  EEI time series stays drawn ONCE on its own chart (no parallel pipeline).

---

## 5. Phase 2 (DEFERRED -- separate targeted pass, NOT this build)

Targeted Mode-1 edits to energy_imbalance.py, after the standalone chart ships:
- Narrative correction: OLR-not-reflection fix + RONI rationale (largely drafted).
- Add the 2026 band: RESOLVED -- provisional-with-flagging now (Western Heatwave
  convention), not waiting for a formal threshold crossing.
Captured here so it does not float. Do not conflate with the Section 3 build.
Consider splitting to its own L-handle (L-061) so it cannot leak when L-060 closes.

---

## 6. Build-session preamble (do first)

- SHA-pin: git ls-remote at HEAD, record base SHA. Build on fresh pull or upload,
  never /mnt/project.
- New module -- verify integration points against HEAD before editing shared files:
  fetch_climate_data.py (new RONI/ONI/plume fetch + cache + metadata),
  gallery_metadata.json (new entry, Climate Change subcategory, desktop + mobile),
  the gallery viewer / "i" card pipeline.
- Resolve the remaining build-time items: confirm ONI file URL (2.2); confirm plume
  parse and the skill-calibration params for the Gaussian, else the spread fallback
  (2.3); confirm phase computation matches the official threshold+persistence rule.
- Agentic pre-test before delivery (py_compile + xvfb where a GUI path is touched).
  Data correctness: smoke-test that traces CONSTRUCT with real fetched values and
  that computed phases match the published RONI episode list.
- Provenance: every numeric claim in card text cited; no recalled values. Run
  provenance_scanner on the new module; Tier-1 = 0 before push.

---

## 7. Open questions -- RESOLVED this session

1. Plume envelope style -> calibrated Gaussian (mean + skill-scaled spread); raw
   model-spread band only as a labeled fallback. (D6, 2.3)
2. "i" card schematic -> Plotly-drawn. (Section 4)
3. Phase 2 trigger for the 2026 band -> provisional-with-flagging now. (Section 5)
4. Anything to add to the chart -> no; let it land. (Section 3)

One genuine open item remains for the build session, not a design question:
confirm the ONI file URL and the IRI plume parse / skill-calibration params at HEAD
before hardcoding, with the cached-CSV and model-spread fallbacks ready.
