# Food Insecurity Visualization — Handoff v2.5
## Sessions: April 19-24, 2026 | Tony + Claude Opus 4.6 + Gemini 3.1 Pro

---

## 1. CURRENT STATE

### Period 7 chart: RENDERING FROM PYTHON PIPELINE
- Script: `scenarios_food_insecurity.py` (orrery root directory)
- Output: `data/period7_food_insecurity.html` (standalone, self-contained)
- Seven Chart.js panels, five countries, pixel-aligned axes
- Chart.js 4.4.1 embedded inline (no CDN dependency)
- V-Dem data loaded from CSV with 2015-2025 year filter
- FTS data: fallback to verified hardcoded values (Excel parsing deferred)

### What changed this session (April 24, 2026)

**Content layer — COMPLETE:**
- Eight event hovertexts rewritten with IPCC confidence tags,
  V-Dem governance numbers with directional cues, FTS funding
  numbers, primary/contributing stressor attribution, and
  bracketed endnote reference numbers [1]-[12]
- Bridge text finalized (Tony's editorial voice, locked)
- Six endnotes sections: V-Dem interpretation, confidence
  methodology, measurement basis (72M caveat), counter-examples
  and limitations, references (12 numbered + 3 dataset citations),
  acronyms (13 terms expanded)
- Citation worksheet: 48 claims verified by Gemini Session 5
- Measurement basis differentiated per country in Event 8
  (IPC 3+ for Somalia/Sudan/S.Sudan; HNO for Yemen; PIN for Ethiopia)

**Architecture — MIGRATED TO PYTHON:**
- `scenarios_food_insecurity.py` reads local data files, generates
  self-contained HTML with embedded Chart.js
- V-Dem CSV loader with year filter (2015-2025) and NaN handling
- FTS Excel loader with HTML-as-XLS fallback (OCHA format)
- Chart.js library embedded inline from `data/food_insecurity/chart.umd.js`
- Event hovertexts, bridge text, and endnotes defined as Python
  data structures (editable, versionable, reviewable)
- JS template uses raw string with placeholder substitution
  (eliminates f-string double-brace escaping problems)
- Unicode apostrophe/quote escaping for JS string safety

**Bugs fixed:**
- V-Dem CSV dumping full 1789-2025 dataset with NaN values
- Missing DOCTYPE/HTML wrapper (CSS variables undefined standalone)
- Chart.js CDN blocked from file:// protocol
- Unicode curly apostrophes breaking JS single-quoted strings
- Extra closing braces in mkF Chart constructor (f-string artifact)

### Implementation architecture

Python script generates standalone HTML. This is a DIFFERENT
pipeline from typical orrery scenarios (which use earth_system_generator.py).

**Data flow:**
```
data/food_insecurity/vdem_food_insecurity.csv  -->  load_vdem_data()
data/food_insecurity/FTS_*.xls                 -->  load_fts_data()
data/food_insecurity/chart.umd.js              -->  embedded inline
EVENTS list (Python)                           -->  _js_events()
BRIDGE_TEXT, ENDNOTES (Python)                 -->  f-string HTML
                                               -->  data/period7_food_insecurity.html
```

**Fallback pattern:** Both data loaders have verified hardcoded
fallback values. If source files aren't found or can't be parsed,
the script falls back to the same numbers that were manually
extracted from OCHA exports on April 19-21, 2026. The output is
identical either way — the pipeline verification is for auditability.

---

## 2. CONFIDENCE FRAMEWORK — IMPLEMENTED

### IPCC-aligned confidence tags in all eight event hovertexts

Each event opens with italicized confidence level:
- *Very high confidence* — Events 5, 8 (funding data)
- *High confidence* — Events 1, 2, 3, 4, 7
- *Medium confidence* — Event 8 (systemic attribution)
- *Low-medium confidence* — Event 6 (FEWS NET impact)

### Confidence methodology statement (in endnotes)

Transparent about assessment process: single analyst (Tony
Quintanilla, PE) with AI-assisted data integration (Claude Opus 4.6)
and domain validation (Gemini 3.1 Pro). Not peer-reviewed, not
expert panel consensus. Causal note: high confidence in data does
not mean causal interpretation is proven.

### Attribution framework

Each event hovertext uses:
- **Primary stressor:** the dominant factor
- **Contributing:** secondary factors
- Narrative explanation of "why this outcome and not another"

This replaces the pie-chart approach (rejected as false precision)
with defensible narrative attribution.

---

## 3. BRIDGE TEXT — LOCKED

Tony's editorial, finalized April 24, 2026. Two paragraphs:
1. Purpose, process, methodology transparency
2. Conclusions: 72M figure with measurement caveat, Ethiopia
   non-event caveat, Somalia natural experiment, thesis statement

Signed: "— Tony Quintanilla, April 2026"

Key line: "That fact is policy, not ecology."

---

## 4. CITATION WORKSHEET — VALIDATED

### Gemini Session 5 results (April 24, 2026)

48 claims across 8 events validated. Key outcomes:
- All IPC/FTS/V-Dem figures confirmed against primary sources
- 12 numbered references identified with specific document titles
- "Siege" → "deliberate blockade" (terminology correction)
- "Natural experiment" confirmed as our analytical framing (not sourced)
- Measurement basis clarified: 72.8M aggregates IPC 3+ with HNO/PIN
- Counter-examples identified (both directions): Kenya/South Africa
  (low funding, no crisis) and Yemen/S.Sudan (high funding, crisis
  anyway — access was the bottleneck)
- FEWS NET: WFP VAM and FAO GIEWS identified as alternatives that
  continued during shutdown but lacked FEWS NET's integrated forecasting
- Sudan: deliberate starvation formally documented by UN FFM and HRW,
  naming both RSF and SAF

### Gemini temporal caveat
Gemini's training data doesn't cover 2025-2026 events. It validated
historical events (2015-2024) against real-world primary sources.
2025-2026 data verified against OCHA FTS official exports in Tony's
possession. Noted in confidence methodology.

---

## 5. FILES

### Current deliverables:
- `scenarios_food_insecurity.py` — Python generator script (orrery root)
- `data/food_insecurity/chart.umd.js` — Chart.js 4.4.1 UMD build (205KB)
- `data/food_insecurity/vdem_food_insecurity.csv` — V-Dem extracted data
- `data/food_insecurity/FTS_*.xls` — OCHA FTS exports (10 files)
- `data/period7_food_insecurity.html` — generated output (~238KB)

### Supporting documentation:
- `food_insecurity_citation_worksheet.md` — 48-claim verification table
- `food_insecurity_hovertexts_final.md` — verified hovertext drafts
- `food_insecurity_endnotes_final.md` — endnotes content
- Handoff versions: v1 through v2.5 (this file)

### Previous deliverable (superseded):
- `period7_seven_panel_complete.html` — original Chart.js prototype
  (generated in Claude's artifact viewer, sessions April 19-21)
- `period7_seven_panel_v2.html` — intermediate version with hovertexts
  (generated in Claude's artifact viewer, April 24, before Python migration)

---

## 6. NEXT SESSION PRIORITIES

1. **FTS Excel parsing — BLOCKING.** The whole point of the Python
   pipeline is to read local data files, not embedded fallback data.
   Currently the script falls back to hardcoded values because OCHA
   FTS exports are HTML tables saved with .xls extension, which
   neither xlrd nor pd.read_html can parse. The fallback is false
   security — the script appears to work while silently not reading
   the source files. Once parsing is fixed, REMOVE the fallback data
   entirely so the script fails loudly if it can't read the files.
   Fix options:
   a) Tony opens each .xls in Excel, Save As .xlsx (gives clean files)
   b) Tony screenshots the column structure so Claude can write a
      custom parser for the specific OCHA HTML format
   c) Investigate the actual file format (may need different parser)
   This must be resolved before the pipeline can be called verified.

2. **Cross-marker hover interaction** — replace hover-anywhere-in-event
   with discrete cross (+) markers per orrery convention. Improves
   readability, consistency with orrery interaction patterns, and
   touch device compatibility. Color-coded tooltip backgrounds (option 1)
   can combine with this.

3. **Gallery deployment** — the HTML file can go directly into the web
   gallery as a standalone interactive (Chart.js inline).
   Separate treatment from JSON converter pipeline since this isn't Plotly.

4. **Earth system GUI integration** — add launch button to
   earth_system_visualization_gui.py that opens the generated HTML.

5. **Gemini final pressure-test** — on the complete rendered artifact
   (not just the text). "What would a critical reviewer say about
   this visualization?"

### Deferred:
- Plotly translation (Ring 2 — only if Plotly features needed)
- Historical periods (1-6) — working backward through history
- Ecological signal top band (ERA5 or ENSO data)
- Yemen, Sudan, Ethiopia FTS panels expansion
- Kenya as non-event reference country
- War deaths integration
- Somalia KMZ/Google Earth deep dive

---

## 7. TECHNICAL NOTES

### Requirements additions:
```
xlrd>=2.0.1           # Excel .xls parsing (OCHA FTS legacy format)
lxml>=4.9.0           # HTML parsing for FTS exports saved as .xls
```

### Running the script:
```
cd orrery/
python scenarios_food_insecurity.py
# Opens data/period7_food_insecurity.html in browser
```

### Key architectural decisions:
- Chart.js embedded inline (not CDN) for offline rendering
- JS template as raw Python string with placeholder substitution
  (NOT f-string — f-string double-brace escaping is unmaintainable
  for complex JS with nested objects and template literals)
- V-Dem CSV filtered to 2015-2025 at load time (full dataset has
  data from 1789 with NaN values that break Chart.js)
- Unicode characters in event hovertexts escaped for JS strings
  (\u2019 right quote, \u2018 left quote, \u2014 em dash)

---

## 8. KEY QUOTES

"Nature creates scarcity. Policy creates famine."

"Why us and not the NYT?" — Tony, April 19

"The plan itself disintegrated." — On Ethiopia 2025

"Two different stories, same ending." — Somalia vs South Sudan

"My biggest concern is explanatory accuracy. I don't want to
distort the picture. How do we make it balanced?" — Tony, April 21

"Stressors are complex. Response is complex. What is clear is the
adequacy of the humanitarian response plan funding." — Tony

"Buildings don't care who the architect is." — Tony, on why
accountability and corruption matter more than political system

"The variable that changed was money." — Somalia 2022 natural experiment

"That fact is policy, not ecology." — Bridge text thesis

"Non-events shouldn't be idealized." — Bridge text caveat

72.8 million people. All below 25% funded or plan-collapsed.

---

*Handoff prepared: April 24, 2026 | Claude Opus 4.6*
*Gemini contributions: Sessions 1-5*
*Next: cross-marker interaction, gallery deployment, pressure-test*
*"6.5 million people are falling through a hole in our collective imagination."*
