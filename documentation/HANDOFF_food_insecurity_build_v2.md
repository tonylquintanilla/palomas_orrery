# Build Handoff -- Food Insecurity Layer (Sudan, current period)

**Pinned to:** `c8ee9056ebb281265edd38172f76fcc3f0a81697` (round-trip verified clean this session)
**Manifest executed:** `documentation/MANIFEST_food_insecurity_sudan_v2.md`
**Deliverable:** `food_insecurity_generator.py` (new module, 635 lines, ASCII/LF, py_compile clean)
**Scope built:** Sudan, CURRENT period only (Feb-May 2026). Projections, 14 famine-risk areas, and the 39 call-out points remain DEFERRED per manifest.
**Ledger:** closes the build half of L-001; opens a scanner item (see section 5; couples to L-064).

---

## 1. What was built

A dedicated **vector/categorical** generator (not a bend of the gridded-scalar `run_scenario`), reusing the family's single-doc-KMZ + ScreenOverlay-card conventions:

- Parses the IPC Mapping Tool GeoJSON: **189 analysis areas** (183 Polygon + 6 MultiPolygon); the 39 Point features are skipped this cut.
- Per-area choropleth by mapped IPC phase; MultiPolygons rendered as one placemark with shared style.
- **Full phase1-5 breakdown in every balloon** -- so a sub-20% Catastrophe population never hides behind a Phase-4 color.
- National totals are **transcribed constants**, never summed from polygons.
- Two ScreenOverlay cards (legend + national/intel) and a "Framing (read this first)" folder carrying composed/transcribed C1/C2/C3.
- Optional Plotly choropleth teaser for the gallery (guarded; KMZ never depends on it).

**Outputs (written to `data/`):** `food_insecurity_sdn_blockbuster.kmz`, `food_insecurity_sdn_teaser.html`, plus the two card PNGs.

**Architecture note (flag):** the module does **not** import `earth_system_generator`. That engine pulls in plotly/scipy/matplotlib/tkinter at import; this layer is categorical polygons, not a scalar field, so the single-doc-KMZ packaging is mirrored locally (`package_kmz`) to keep the food layer decoupled and import-robust. Retune if you'd rather share the packager.

---

## 2. Sourced values (transcribed, not recalled)

| Value | What | Source in the report |
|---|---|---|
| 47.5 million | total population analysed | Country-wide Analysis (Feb-May 2026) |
| ~19.5 million | IPC Phase 3+ (Crisis or worse), current | Country-wide Analysis ("41 percent") |
| >5 million | IPC Phase 4 (Emergency), current | Country-wide Analysis |
| ~135,000 | IPC Phase 5 (Catastrophe), current | Key Messages / Country-wide Analysis |
| ">=20% rule" | "mapped Phase represents highest severity affecting at least 20% of the population" | page-7 legend (IPC verbatim -> transcribed tier, not composed) |
| 5 KEY DRIVERS | Conflict / Displacement & immobility / High food prices / Collapse of health & WASH / Limited humanitarian access | "KEY DRIVERS" section (verbatim, ASCII-normalized) |
| Middle East line | conflict "contributing to higher fuel, food, and fertilizer prices... likely to intensify" | Key Messages (verbatim) |

**Phase ramp (provenance flag):** IPC carries no color in the GeoJSON. The hex values were **sampled from the report's own page-7 "Key for the Map" legend swatches** at 200 dpi (anti-alias +/-2): P1 `#D0E7C7`, P2 `#F8E303`, P3 `#E27826`, P4 `#C52127`, P5 `#621012`, not-analysed `#FFFFFF`, inadequate-evidence `#BBBCBE`. These are the colors IPC used in *this* report, not recalled brand hex. If you have IPC's published communication-guidance hex, swapping them in is a one-constant edit.

**Citation (flag):** the report has **no formal "recommended citation" line**. `CITATION` is assembled from the title-page facts (publisher, title, dates). Swap in IPC's preferred string if you have it.

**Per-area evidence/HFA (flag):** `confidence_level` (1/2) and `hfa_value` (1/2/3) are shown as **raw values** in each balloon (manifest §8 shows the value, not a decoded label). The report states overall evidence "Medium (**)" but gives no clean per-value 1/2/3 -> words legend, so no word mapping was invented.

---

## 3. Discrepancies surfaced (file wins per manifest's own rule)

1. **phase5_population > 0 appears in 10 areas, not 23** (manifest/handoff prose said 23). All 10 are mapped P4, so "all hidden Catastrophe sits under P4" holds; only the count differs. Built to the file (10). Largest: **Beliel** (mapped P4; 26,411 in Phase 5 @ 5%) -- used as the route example.
2. **Mapped phases present this export:** P2 (8), P3 (131), P4 (49), + one **not-analysed** (`Abyei PCA`, phase None / label 'P', pop 0). No P1, no mapped P5. Full P1-P5 ramp is still defined per §7; only 2/3/4 + not-analysed render.

---

## 4. Verification (render beats claims)

- ASCII/LF, `py_compile` clean.
- Live run: 189 areas parsed; KMZ + teaser written.
- KMZ byte-inspected: CDATA balloons unescaped (193 blocks, 0 escaped); phase fills match the data exactly (8x `cc03e3f8`, 131x `cc2678e2`, 49x `cc2721c5`, 1x `66ffffff`); **Beliel balloon shows Phase 5 Catastrophe 26,411 under mapped Phase 4**; Abyei = "Not analysed"; framing folder present; totals = transcribed constants.
- **Mode-5 (Google Earth visual render) is the authoritative gate -- still yours to run.** Tunable Mode-5 calls: `POLY_FILL_ALPHA` (currently `CC` ~80%; family overlays use ~40%) and the not-analysed white-`66` fill.

---

## 5. Provenance scanner finding (manifest §14 item 4 -- CONFIRMED) + proposed fix

**Confirmed:** the scanner's Tier-1 = 0 on this module is a **false clean**. Two compounding gaps, both proven empirically:

1. **Allow-list gap.** `_extract_string_units` only runs for a hardcoded `narrative_files` set (+ `*_visualization_shells`). A new module is excluded, so its framing/balloon display strings are never extracted or scored. (Proven: an uncited `12345 km` -- a *recognized* unit -- in a fresh file produced zero findings.)
2. **Vocabulary gap.** `NUMERIC_CLAIM_RE` recognizes only physical units (AU, km, degrees, masses, K, kg...). It has no `people | percent | % | million | thousand | billion`, so humanitarian figures aren't seen as claims even inside an allow-listed file.

**Proposed minimal two-part fix (NOT applied -- your go/defer):**

```python
# (1) provenance_scanner.py, narrative_files set: add
'food_insecurity_generator',

# (2) NUMERIC_CLAIM_RE unit alternation: append
r'km/h|mph|people|persons?|percent|%|million|thousand|billion)\b',
```

**Verified on a scratch copy of the scanner (repo copy untouched, hash unchanged):**
- This module's now-visible display strings (national figures, drivers, balloon rows) all score **"Has source citation," Tier-3 (score 8) -- no action**. The construction-site `# Source:` discipline holds; the module passes legitimately once the scanner can see it.
- An injected uncited food claim is reachable for scoring (the path now runs).

**Family-wide ripple (the L-064 coupling -- why this is your call, not a silent food-build edit):** extending the vocabulary newly exposes at least one pre-existing real finding outside this module -- **`star_notes.py` line 1257, Tier-1, "No source citation (recalled)"** -- previously invisible only because of the vocabulary gap. Part (2) is a shared-CI change with effects across the 113-file family; part (1) is local and safe. You may want to take **(1) now** and **defer (2)** to a dedicated L-064 pass, or take both and triage the ripple.

---

## 6. GUI registration (Mode-1 targeted snippet -- for you to place)

The module is standalone-runnable (`python food_insecurity_generator.py`). For the Earth System selector, it needs a dedicated entry (it isn't a scalar `SCENARIOS` member). Minimal wiring:

```python
import food_insecurity_generator  # near the other Earth System imports

# In the Earth System GUI, add a button / menu entry:
#   label: "Food Insecurity -- Sudan (IPC, Feb-May 2026)"
#   command: lambda: food_insecurity_generator.run(status_callback=self.set_status)
```

Provided as a snippet rather than a GUI-file rewrite; place it where the other Earth System launchers live and retune the label/callback to match your selector.

---

## 7. Open decisions for you

- [ ] Module name: `food_insecurity_generator.py` is a proposal (avoids the forbidden `scenarios_food_insecurity.py`). Rename freely.
- [ ] Scanner fix: take part (1) now / defer part (2) to L-064 / take both.
- [ ] Phase-ramp hex: keep report-sampled, or swap in IPC published hex.
- [ ] Citation string: keep title-page-assembled, or swap in IPC's preferred.
- [ ] `POLY_FILL_ALPHA` and not-analysed fill: Mode-5 retune.
- [ ] Mode-5 render in Google Earth = authoritative close gate.

*Build session: June 2026 with Anthropic's Claude Opus 4.8.*
