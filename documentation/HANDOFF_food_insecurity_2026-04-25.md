# Handoff — Food Insecurity Module (Period 7)
**Session date:** April 25, 2026
**Partners:** Tony (integrator) + Claude Opus 4.7 (implementation) + Gemini (domain consultation)
**Status:** Editorial design contract substantially revised. Technical work partially built; major reorganization pending.

---

## TL;DR for next session

- The seven-panel V-Dem + FTS chart is being **replaced** by a three-band design.
- Tonight's session was 90% editorial reframing and 10% code. The technical pieces built (xlsx parser, HDX integration, empty-state rendering) all stay useful but serve a different argument now.
- **Do not start coding next session.** Start with two specific Mode 7 / data-source questions, listed below.

---

## What the chart is actually about (the design contract)

After substantial back-and-forth, the thesis settled here:

> "Food insecurity in fragile states arises through a sequence of failures. Households cannot acquire food at prices they can pay (entitlement failure). Domestic response capacity does not fill the gap. International humanitarian aid is requested to cover the residual; the aid that arrives often falls short of what was requested. The remaining unmet need produces measurable outcomes: acute malnutrition, mortality, displacement. The failures at each stage have plural causes — climate stress, conflict, governance collapse, currency instability, donor decisions, supply chain disruption — that vary across countries in ways defeating any single-cause explanation. The chart shows the sequence; it does not adjudicate the causes."

Read this aloud before designing anything. Every chart decision evaluates against: *does this serve the four-clause thesis?*

### The four clauses

1. **Entitlement failure**: households can't acquire food at affordable prices.
2. **Aid gap**: the international response that exists has a measurable shortfall vs. its own stated requirements.
3. **Residual harm**: malnutrition, mortality, displacement — what's left after both responses.
4. **Plural reasons**: the failures at each stage have contested causes that defeat monocausal accounts.

### The structural claim

The bands aren't independent variables. They're a chain. Each stage's gap is partially compensated by the next stage's response. The residual outcomes are what's left after all responses fail. **The chart's argument lives in the chain, not in any single band.**

---

## How tonight's editorial reframing happened (so you don't relitigate)

Tonight's session moved through these positions, in order:

1. **Started with**: the seven-panel chart wasn't rendering because of a parse failure (.xls/.xlsx confusion).
2. **Pivoted to**: hardcoded fallback data was masking real failures; removed it.
3. **Pivoted to**: the funding methodology question (HRP-only vs. all plans) was an editorial choice neither Tony nor Claude could defend.
4. **Pivoted to**: the chart was implicitly making a single-cause argument ("funding collapsed and that's the story") that Tony was uncomfortable defending.
5. **Pivoted to**: "you decide" agnosticism is itself a dodge — a pretense of neutrality that smuggles editorial choices through composition.
6. **Pivoted to**: the chart needs a defensible *negative* claim ("no monocausal account survives the data") rather than a defensible *positive* causal claim.
7. **Pivoted to**: "need" is ambiguous; what matters is *unmet need*.
8. **Pivoted to**: unmet need has *stages* — entitlement failure, aid gap, residual harm — and each stage has its own gap.
9. **Pivoted to**: "self-sufficiency" was the wrong frame for stage 1 — Sen's entitlement framework is the correct one.

Each pivot rejected an answer that wasn't quite right and kept asking what would be right. **Don't undo this.** The current frame is the cleanest the project has had.

### Lessons-archive candidates from tonight

- *"You decide" is not neutrality; it's an abdication that pretends to be a virtue. Honest neutrality looks like a clearly stated position with disclosed limits, not absence of position.*
- *Editorial clarity is achieved by examining the words that look like they don't need examining. "Need" looked obvious; "unmet need" was the real claim.*
- *When the project crosses into a domain with established theoretical frameworks, name the framework explicitly before designing. (Sen's entitlement framework was field-standard since the 1980s; Claude's "self-sufficiency" framing was 1970s thinking.)*
- *"Converted live from API" describes pipeline, not data currency. Always verify the snapshot date before relying on a third-party mirror as a current data source.*
- *Before recommending a labor-intensive workflow, search whether the source has a bulk export. The HDX file existed all along; the 52-files-of-clicking plan was almost adopted because nobody asked.*
- *Showing absence is part of honest data storytelling. Empty-state panels are truer than silent fallbacks.*

---

## The three-band design

### Band 1 — Market-level food access failure (Entitlement)

**Indicator**: Terms of Trade (ToT). Specifically:
- Labor-to-cereal ToT: kg of staple grain per day's casual unskilled wage
- Livestock-to-cereal ToT: kg of grain per local-quality goat/sheep (especially Somalia, Ethiopia pastoralist regions)

**Data sources** (per Gemini, need to verify URLs/access):
- WFP VAM (Vulnerability Analysis and Mapping)
- FSNAU (Food Security and Nutrition Analysis Unit) — particularly strong for Somalia, going back to the 1990s
- FEWS NET

**Time resolution**: Monthly. Will need 12-month rolling average or YoY % change to smooth seasonality (lean-season spikes are normal noise, not structural collapse).

**Methodology disclosure required**: Aid endogeneity. Humanitarian food assistance suppresses local prices, so the ToT signal *understates* the entitlement gap in countries with active aid programs. Plan: explicit annotation + show both labor-cereal (more aid-sensitive) and livestock-cereal (less aid-sensitive) so the divergence between them carries information about aid penetration.

**What this band claims**: "Households cannot acquire food at prices they can pay." Observational, well-defined, uncontroversial as a measurement.

### Band 2 — International aid gap

**Indicator**: OCHA HRP requirements vs. delivered funding, per country, per year.

**Data sources**:
- HDX `humanitarian-response-plans.csv` — 1999-present, snapshot dated 2026-01-30. Has requirements only, no funded amounts.
- HDX `HPC Tools API output.json` — 3.8 MB, marked "live." Need to verify whether it contains funded amounts (CSV doesn't).
- FTS `Trends_in_reported_funding_<Country>_*.xlsx` — 5 files (one per country), multi-year funded amounts. Already in `data/food_insecurity/`.
- FTS `Coordinated_plans_<Country>_<Year>_*.xlsx` — per-country per-year requirements + funded. Have 10 files (5 for 2025, 5 for 2026).

**Methodology**: HRP-only (country-specific plans, `locations == ISO_CODE` in HDX terms). Disclose: "Excludes regional plans (migrant response, refugee response, COVID GHRP). The chart tracks the gap *between OCHA's stated requirement and what was delivered*, by OCHA's own accounting. Readers who think OCHA's requirements are inflated still see a gap; readers who think they're conservative see a worse gap. The methodology is internal to the data, not imposed."

**What this band claims**: "The response system has a measurable, persistent shortfall." Observational, defensible without external standards.

### Band 3 — Residual outcomes (Unmet need that wasn't closed)

**Indicator** (TBD, leading candidates):
- GAM (Global Acute Malnutrition prevalence in children under 5) — most direct outcome measure of unmet food need; observational; WHO has thresholds; FEWS NET / UNICEF track it.
- Under-5 mortality rate (UNICEF / IGME) — broader outcome; harder to attribute to food specifically.
- IPC Phase 5 (Famine) population — captures system-collapse cases; rare but meaningful.

**Data sources**: UNICEF, FEWS NET, IPC partners.

**What this band claims**: "Children are measurably malnourished and dying because the system didn't reach them." Outcome data, observational, hard to dismiss as ideological.

---

## Technical work completed tonight (preserved, ready for use)

### `scenarios_food_insecurity.py` — substantial edits

**Built and tested**:
- New file glob pattern: `FTS_Coordinated_plans_<Country>_*.xls*` (replaces old `Trends_in_coordinated_plan_requirements_*`).
- `_read_fts_file()`: simplified to openpyxl primary + read_html defensive fallback. xlrd strategy removed entirely.
- `load_fts_data()`: hardcoded fallback dict removed. Missing or unparseable countries return `_missing` sentinel dicts. Reports specific missing-file reasons per country.
- `load_vdem_data()`: hardcoded fallback dict removed. Missing CSV or missing per-country rows return `_missing` sentinels.
- JS rendering updates:
  - `mkDS()` filters out `_missing` countries so V-Dem lines simply don't appear for missing countries.
  - `mkF()` checks `fts._missing` and renders an empty-state overlay (dashed border, "Data unavailable" message) instead of a broken chart.
  - V-Dem all-missing case (`V_ALL_MISSING`) renders both shared panels as empty-state.
- Module docstring updated with v3.20 credit line and change list.

**Status**: Code works correctly with the .xlsx download workflow when files match expected structure. Will need to be reorganized for three-band design, but the empty-state and parser logic carry over cleanly.

### `requirements.txt` — minor edits

- `xlrd` removed entirely (no longer needed; nothing in codebase imports it).
- `openpyxl>=3.1.0` kept.
- `lxml>=6.1.0` kept (defensive for read_html fallback).
- Header comment updated with the xlsx-over-xls download guidance: **"click 'xlsx' in the OCHA FTS dropdown, not 'xls'"** — the single most important piece of guidance to avoid re-walking this ground.
- Credit line updated.

### Other technical findings worth remembering

- **OCHA file naming changed in 2026**: `FTS_Trends_in_coordinated_plan_requirements_*` (old) → `FTS_Coordinated_plans_*` (new).
- **OCHA file format changed**: BIFF5 .xls → .xlsx (OOXML). Both formats may still be served; .xlsx is the cleaner choice.
- **Each `_<YEAR>_` file is a single-year snapshot.** To get historical multi-year requirements, either download per-year per-country files (52+ clicks) or use HDX bulk export (1 file, snapshot-dated).
- **HDX CSV is dated 2026-01-30, not live.** Description says "converted live from JSON API" but that describes the pipeline, not the snapshot. The JSON file on the same HDX page (3.8 MB) IS marked live but its contents need verification.
- **HDX CSV has only requirements, no funded amounts.** Funding side requires either FTS direct downloads or the HDX JSON file (TBD whether it has funded fields).

---

## Open Mode 7 questions for next session

These are the two questions that gate the next round of building. **Send to Gemini before coding.**

### Question 1 — Band 1 data sources, specifics

> "I'm building a Terms of Trade time-series visualization for Somalia, Yemen, South Sudan, Sudan, Ethiopia, 2008–present. I need:
>
> 1. Specific URLs / dataset names where I can download labor-to-cereal ToT and livestock-to-cereal ToT for these five countries.
> 2. File format(s) typically served (CSV, XLSX, API).
> 3. Update frequency.
> 4. Whether one consolidated source covers all five, or whether I need to pull from FSNAU for Somalia, WFP VAM for Yemen, etc.
> 5. Known gaps in the time series (e.g., South Sudan civil war 2014–2017, Yemen pre-2015) — where to expect missing data and how the field typically handles it.
>
> Goal: a manual-download workflow analogous to what we have for FTS funding files. The pipeline reads files from disk, no runtime API calls."

### Question 2 — Band 3 indicator selection

> "For residual outcomes (Band 3) showing measurable harm produced by unmet food need, three candidates:
>
> - Global Acute Malnutrition (GAM) prevalence in children under 5
> - Under-5 mortality rate
> - IPC Phase 5 (Famine) population
>
> For Somalia, Yemen, South Sudan, Sudan, Ethiopia, 2008–present:
>
> 1. Which has the cleanest time series and best per-country comparability?
> 2. Which is most directly attributable to food insecurity specifically (vs. broader humanitarian conditions)?
> 3. Where do the others fall short?
> 4. Are any of these subject to political contestation in the way IPC famine declarations sometimes are?
> 5. Same data-source specifics as Question 1: URLs, formats, update frequency, gaps."

---

## What NOT to do next session

- **Don't pick up coding without revisiting the design contract.** The three-band design is editorially sound but not yet built. Jumping into code before resolving the Mode 7 questions wastes the editorial work.
- **Don't relitigate the funding methodology question.** It's settled: HRP-only, OCHA's own accounting, methodological disclosure in chart annotation. Moving past this.
- **Don't try to put governance (V-Dem) back as a top-band signal.** It's still relevant, but it lives downstream of the chain as one of the "plural reasons," not as the headline. The seven-panel chart's V-Dem-at-top structure is being deprecated.
- **Don't restore the hardcoded fallback data.** The empty-state path is now the design. If a country's data is missing, the chart shows that, doesn't paper over it.
- **Don't accept "you decide" framings as a substitute for a position.** The chart's negative claim ("no monocausal account survives the data") is the position. Drift back toward neutrality is drift back toward dodge.

---

## Files in `/mnt/user-data/outputs/` from this session

- `scenarios_food_insecurity.py` — updated (xlsx parser, no fallback, empty-state rendering)
- `requirements.txt` — updated (xlrd removed, header guidance added)

Both files compile and run correctly. Visualization currently renders five "Data unavailable" panels for FTS because the underlying parser logic works but the data-shape mismatch hasn't been resolved (the new `Coordinated_plans_*.xlsx` files contain per-plan rows, not per-year rows). This is no longer a blocker because the entire FTS section is being reorganized into Band 2 of the three-band design — which will read from a different source (likely HDX JSON or a clean FTS direct-download with the right shape).

---

## Workflow / data files to deal with at session start

In `data/food_insecurity/`:

**Keep**:
- `vdem_food_insecurity.csv` — V-Dem source, used (eventually moves to "plural reasons" context, not Band 1)
- `chart.umd.js` — Chart.js library
- `humanitarian-response-plans.csv` — HDX requirements, snapshot 2026-01-30
- 5 × `FTS_Trends_in_reported_funding_<Country>_2026_*as_on_2026-04-24.xlsx` — multi-year funding
- 5 × `FTS_Coordinated_plans_<Country>_2025_*as_on_2026-04-25.xlsx` — 2025 plan year
- 5 × `FTS_Coordinated_plans_<Country>_2026_*as_on_2026-04-24.xlsx` — 2026 plan year

**Consider downloading next session**:
- HDX `HPC Tools API output.json` (3.8 MB, "live") — if it contains funded data, replaces need for per-year plan files
- Band 1 source files once Gemini answers Question 1
- Band 3 source files once Gemini answers Question 2

**Already deleted (no need to restore)**:
- Old .xls (BIFF5) FTS files
- Hardcoded fallback dictionaries (FTS and V-Dem) in code

---

## Project meta-notes

This was a long session — 30+ turns — that produced almost no net new code. What it produced was the editorial scaffolding for the next several sessions of code. By the protocol's own terms, "the conversation IS the discovery" — and tonight's discovery was that the project's central food-insecurity module needed substantial editorial reframing before any further technical work made sense. That reframing is now done. The next sessions can be heavily technical because the design contract is clear.

Mode 7 worked as the protocol describes: Tony as integrator, Gemini as domain check, Claude as implementation continuity. Gemini's Sen-framework correction was decisive and would have been hard to reach without an external partner with development-economics knowledge. Worth flagging that this was Mode 7 in *cooperative* form (helping refine a position) rather than competitive form (comparing reasoning across AIs).

The session also produced a clearer sense of what the food-insecurity module *is* in the broader project. Before tonight, it was "a chart about the Somalia funding crisis that grew." After tonight, it's "a structured analytical artifact about how unmet need unfolds in fragile states, designed to defeat monocausal accounts." That's a more durable purpose, and it informs how Period 7 fits alongside the climate, governance, and astronomical visualizations elsewhere in the orrery suite.

---

*Handoff written: April 25, 2026 with Anthropic's Claude Opus 4.7*
*Approved by Tony before session close: TBD*
