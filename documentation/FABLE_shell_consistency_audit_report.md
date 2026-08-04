# Fable Shell Consistency Audit — Full Report

**Built on `679c2f4e9b6836204e4c03858361d881c6d49c4a`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).**

**Prepared:** August 4, 2026 by Claude Fable 5 (comprehensive audit leg) · Tony Quintanilla, integrator
**Responds to:** PROMPT_fable_shell_consistency_audit.md (anchored at `55b07a6`; the only commit
between that anchor and this HEAD is the prompt file itself, so all 16 audit targets are
byte-identical to the prompt's pre-work state — pre-work greps remain valid by construction).

**Method note.** All values below were obtained by importing the live modules at HEAD and
inspecting the runtime dicts (`SHELL_CONFIGS`, `CUSTOM_SHELLS`, module `_info` strings), with
body radii and `KM_PER_AU` taken from `constants_new.py` itself — fetched, not recalled.
Reference-pattern status was determined by Python object identity (a config field that *is*
the module string object is linked; equal-but-distinct is a duplicate). Live-vs-dead status
of each text path was determined by grepping for call sites, not imports.

---

## 0. Architecture correction (affects everything below)

The prompt's stated architecture is half-right and the audit corrected it:

**Live text paths (verified by reading the consumers):**

| Path | Source of text | Consumer |
|---|---|---|
| Plotly hover, sphere shells | `SHELL_CONFIGS[body][shell]['hover_text']` | `build_sphere_shell()` (orrery_rendering.py:101) |
| Plotly hover, custom shells | inline strings inside the builder functions | the builders themselves |
| GUI checkbox tooltip | module `_info` strings via `globals()` | `build_shell_checkboxes()` (celestial_objects.py:1457) → `CreateToolTip` (palomas_orrery.py:3534); Sun hand-wired (e.g. palomas_orrery.py:8986) |

**Dead text fields (no consumer anywhere in the codebase):**

- `SHELL_CONFIGS[...]['tooltip']` — 83 copies. `orrery_rendering.py` contains zero
  occurrences of "tooltip"; nothing else reads the key.
- `CUSTOM_SHELLS[...]['tooltip']` — 41 copies. Same: no reader.

So the codebase carries **124 dead text copies** that must still agree with their live twins
(a future migration would promote them), plus a **fourth copy class**: the legacy inline
sphere-shell builders in the `*_visualization_shells.py` modules (e.g.
`create_jupiter_core_shell`, jupiter:84) each carry their own `layer_info`/`description`
dicts with values. These builders are imported by planet_visualization.py but bypassed by
the dispatch (planet_visualization.py:405-427 routes any `shell_name in SHELL_CONFIGS`
straight to `build_sphere_shell`).

---

## 1. Job 1 — Findings tables (findings only; files with none are omitted)

### shell_configs.py

| # | Line(s) | Shell | Type | Description |
|---|---|---|---|---|
| 1 | 1712 (+ saturn module, see below) | Saturn/hill_sphere | CONSTANT_VS_TEXT | `radius_fraction: 1120` draws the shell at 67.5 M km. The imported text (saturn_hill_sphere_info) says "approximately 91 million kilometers (about 151 Saturn radii)". 91 M km = 1,510 R_S; 151 R_S = 9.1 M km. **Three mutually inconsistent values**; Saturn is migrated so this one text renders in both hover and GUI. |
| 2 | 118 | Mercury/outer_core | CONSTANT_VS_TEXT | rf 0.85 → 2,074 km; live hover (and the Batch-1 citation, mercury:44) say 2,020 km, which needs rf 0.828. **Batch 1 patched text + citation but not the geometry constant.** |
| 3 | 136 | Mercury/mantle | CONSTANT_VS_TEXT | Encoded thickness (0.85→0.98) = 317 km vs text "about 331 kilometers thick." Chain note: 2,020 + 331 + 26 = 2,377 km against R = 2,439.7 km — the layer chain doesn't close. |
| 4 | 156 | Mercury/crust | CONSTANT_VS_TEXT | Encoded thickness (0.98→1.0) = 49 km vs text "About 26 km thick (Sori 2018)." |
| 5 | 247 | Moon/inner_core | CONSTANT_VS_TEXT | rf 0.1485 → 258 km vs text (and Weber 2011 citation) "roughly 240 km" (needs 0.1381). Same patched-text/unpatched-constant pattern as #2. |
| 6 | 267 | Moon/outer_core | CONSTANT_VS_TEXT | rf 0.2083 → 362 km vs text "about 330 kilometers" (needs 0.1899). |
| 7 | 924 | Venus/core | CONSTANT_VS_TEXT | rf 0.5 → 3,026 km vs text (and NASA Fact Sheet citation) "around 3,200 km" (needs 0.529). |
| 8 | 965 | Venus/crust | CONSTANT_VS_TEXT | Encoded thickness (0.98→1.0) = 121 km vs text "10 to 30 kilometers." |
| 9 | 795 | Eris/mantle | CONSTANT_VS_TEXT | Encoded ice-shell thickness (0.60→0.66) = 70 km vs text "around 100 kilometers." |
| 10 | 795 area | Eris (structure) | SUSPICION | With mantle at 0.66 and crust at 1.0, the "crust" layer is 395 km thick against a 70-km "substantial mantle" — inverted vs the frost-crust narrative. For Batch 2. |
| 11 | 1425 | Earth/atmosphere | CONSTANT_VS_TEXT | rf 1.05 → shell edge at 319 km altitude; text describes the lower atmosphere as 0–50 km. Probably deliberate visibility stylization, but **undeclared in the text** (Show-the-Envelope gap). Contrast: Mars upper_atmosphere rf 1.06 → 204 km vs stated 200 km is to scale — the stylization convention is inconsistent across bodies. |
| 12 | 1448 | Earth/upper_atmosphere | CONSTANT_VS_TEXT | rf 1.25 → ~1,595 km altitude; text says "from 50 km to about 1,000 km." Same undeclared-stylization caveat. |
| 13 | 343, 362 | Moon/crust | TEXT_VS_TEXT | Config copies say crust "averaging about 50 km on the near side and about 60 km on the far side"; the config hover also carries "as thin as 20–30 km" / "exceeding 100 km" on the far-side highlands; module copy (moon:319, 341) says "near side 30–50 km ... far side up to 100 km or more." Three stories; the 60-km far-side average appears in exactly one copy and equals the encoded thickness (1.0 − 0.9655 = 60 km). |
| 14 | 226 | Mercury/hill_sphere | CROSS_COPY_DRIFT | Config (live) carries "extends to about 94 Mercury radii" (matches rf 94.4) and "SET MANUAL SCALE ... 0.005 AU"; module copy (mercury:422) says 0.003 AU and dropped the 94-radii value for a generic paragraph. |
| 15 | 1269, 1293 | Mars/hill_sphere | CROSS_COPY_DRIFT | Config (live): "~324.5 Mars radii" (matches rf 324.5). Module dead copies: "~320 Mars radii" at mars:844 and mars:859, plus a dead `radius_fraction = 320` constant at mars:884. |
| 16 | 2188 | Mars body header | SOURCE_VS_VALUE | Header cites "bow shock 1.5 Rm"; the code renders 1.64 R_M (mars:690, Vignes et al. 2000, with the Gemini Mode-7 note "1.5 was too low"). The correction propagated to the module but not to this header — same class as known residual (b). |
| 17 | 2371 | Jupiter/magnetosphere (custom tooltip, dead) | STALE_ANNOTATION | Claims the bow shock "(at ~80-100 R_J standoff) is not yet rendered" — jupiter:586 now renders it at 82 R_J. False claim in dead data; would mislead a migration. |
| 18 | 2474 | Saturn/magnetosphere (custom tooltip, dead) | STALE_ANNOTATION | Same: claims bow shock "(at ~22-27 R_S standoff) is not yet rendered" — saturn:669 renders it at 27 R_S. Also carries "(~0 deg tilt)" which the live module text dropped. |
| 19 | 2188 vicinity | Mars/magnetosphere (custom tooltip, dead) | CROSS_COPY_DRIFT | Custom tooltip says bow shock "~1.5 Mars radii"; live module text says "around 1.6"; code renders 1.64. |
| 20 | 93–94 | Mercury body header | STALE (residual b, confirmed) | Still cites Margot et al. (2012) after Batch 1 replaced the core value with Hauck et al. 2013. (Sori 2018 remains current for the crust.) Verified stamp on 94. |
| 21 | 236–239 | Moon body header | STALE (residual b, confirmed) | Still cites Apollo Seismic Experiment reports after Batch 1 re-sourced to Weber 2011 / Nakamura. |
| 22 | 144, 149 | Mercury/mantle | Residual (a), confirmed | Diamond-layer claim present in both config copies (and mercury:55) while mercury:61 records it as Removed. Pending Tony's decision. |
| 23 | 16 locations | (all bodies) | STALE_ANNOTATION | 16 "Verified: April 2026" stamps — matches the as-built count exactly. Informational; Batch 2 cleanup. |
| 24 | throughout | (all 83 sphere entries) | STRUCTURAL | Every `'tooltip'` field is dead data (see §0). |

### saturn_visualization_shells.py

| # | Line(s) | Shell | Type | Description |
|---|---|---|---|---|
| 25 | 930 | hill_sphere | SOURCE_VS_VALUE | `# Source: NASA SSD; Hill sphere ~91 million km / ~151 Saturn radii confirmed.` The citation "confirms" a mutually incompatible pair (91 M km = 1,510 R_S), and neither number matches rf 1120. The word "confirmed" over a self-contradictory pair is the cite-to-clear failure mode in the wild. |
| 26 | 936 | hill_sphere | TEXT_VS_TEXT | "approximately 91 million kilometers (about 151 Saturn radii)" — 10× internal contradiction in one sentence (likely a dropped digit: 1,510 → 151). This is the live text (imported by shell_configs). |
| 27 | 950, 954 | hill_sphere (dead legacy dict) | CROSS_COPY_DRIFT | The same contradictory pair repeated in the dead inline `description` dict and its `# Source`. Four total locations carry it. |
| 28 | — | hill_sphere | SUSPICION | For the Batch 2 cross-check: rf 1120 → 67.5 M km is the value closest to plausible; the 91 M km figure is the suspect. Not asserted — flagged. |

### solar_visualization_shells.py

| # | Line(s) | Shell | Type | Description |
|---|---|---|---|---|
| 29 | 50, 174 | gravitational | SOURCE_VS_VALUE | Both cite "`GRAVITATIONAL_INFLUENCE_AU=126000 in constants_new.py`" — the actual constant is **150000** (constants_new.py:233, which honestly notes a 100,000–200,000 AU literature range). The citations misquote the constant they name. |
| 30 | 61, 433 | gravitational | CONSTANT_VS_TEXT | Display text says influence "extends to about 2 light-years (~126,000 AU)" while the shell renders at 150,000 AU. Full chain: constant says 150 k; citation says the constant is 126 k; text says 126 k. Classic dual-pipeline drift — someone moved one copy. |
| 31 | 322, 759 | chromosphere | CONSTANT_VS_TEXT + TEXT_VS_TEXT | Text: "Radius: from Photosphere to 1.5 Solar radii or ~0.00465 - 0.0070 AU" — the shell renders at `CHROMOSPHERE_RADII = 1.1` (constants_new.py:152, ra ≈ 0.00512 AU). The same text also says the chromosphere extends "only about 2,000 kilometers" (≈1.003 R_sun). Three extents in one shell: 2,000 km (physical), 1.1 R_sun (drawn), 1.5 R_sun (claimed range). |
| 32 | module-wide | (all 15 shells) | STRUCTURAL | Nine of fifteen `_info`/`_info_hover` pairs are literally the same string object; the other six are distinct objects with identical `<br>` formatting. The hover/tooltip split in this module is vestigial. |

### earth_visualization_shells.py

| # | Line(s) | Shell | Type | Description |
|---|---|---|---|---|
| 33 | 907, 1019 | leo / geostationary_belt | SHADOW_CONSTANT | `EARTH_RADIUS_KM = 6371.0` defined **twice** locally. 6371 (mean radius) exists nowhere in constants_new.py (which has equatorial 6378.137 and polar 6356.752), so this is an uncited local value duplicated within one file. |
| 34 | 1018 | geostationary_belt | SHADOW_CONSTANT | `GEO_RADIUS_KM = 42164.0` local literal. |
| 35 | 908, 1020 | leo / geo | CONSTANT_VS_TEXT (derivation) | `AU_PER_KM = EARTH_RADIUS_AU / EARTH_RADIUS_KM` and `geo_radius_au = (GEO/6371) × EARTH_RADIUS_AU` mix an equatorial-based AU (EARTH_RADIUS_AU encodes 6378.137 — verified at runtime) with the mean-radius 6371 denominator: a built-in ~0.11% error and a roundabout construction. Should be `GEO_RADIUS_KM / KM_PER_AU`. |
| 36 | ~1031 | geostationary_belt | CONSTANT_VS_TEXT (comment) | Comment "Radial scatter: +/- 0.0002 AU (~30 km at GEO)" sits on code computing ±0.0002 × EARTH_RADIUS_AU ≈ **±1.3 km** in Earth-radius units — the comment is wrong on both the unit and the magnitude. |
| 37 | ~1048 | geostationary_belt | CONVENTION | GEO hover gives "Altitude: 35,786 km" / "Radius: 42,164 km" with **no AU equivalent** — the standing hover-text AU convention gap, confirmed at HEAD. |
| 38 | 13 locations | (module-wide) | STALE_ANNOTATION | 13 "Verified: April 2026" stamps — not previously enumerated in the prompt's pre-work. |

### jupiter_visualization_shells.py

| # | Line(s) | Shell | Type | Description |
|---|---|---|---|---|
| 39 | 586 | magnetosphere | SOURCE_VS_VALUE (minor) | `bs_standoff = 82 * R_J` with `# Source: Joy et al. 2002 (mean ~84 R_J, highly variable)` — code deviates from the cited mean; the comment acknowledges variability, so informational. |
| 40 | 84–150 etc. | core (and siblings) | STRUCTURAL | Dead legacy sphere builders carry their own value-bearing `layer_info` dicts (e.g. core "20,000K and up to 40,000K") — a fourth independent copy class. |
| 41 | 9 locations | (module-wide) | STALE_ANNOTATION | 9 "Verified: April 2026" stamps — not previously enumerated. |

### moon_visualization_shells.py

| # | Line(s) | Shell | Type | Description |
|---|---|---|---|---|
| 42 | 319, 341 | crust | CROSS_COPY_DRIFT | Module copy's crust-thickness values (30–50 near / up to 100+ far) diverge from the live config copies (50 near / 60 far) — the value side of finding #13. |
| 43 | outer_core info | outer_core | FORMAT | Stray "`:*`" opening a bullet — patch artifact. |
| 44 | 56 | outer core color | Residual (c), confirmed | `# dark red-orange at 1700K` comment survives after the temperature was removed from display text. |

### mercury_visualization_shells.py

| # | Line(s) | Shell | Type | Description |
|---|---|---|---|---|
| 45 | 422 | hill_sphere | CROSS_COPY_DRIFT | "0.003 AU" scale note vs config's "0.005 AU" (finding #14's module side). |
| 46 | crust/atmosphere infos | crust, atmosphere | CROSS_COPY_DRIFT (cosmetic) | Module copies carry an extra "SET MANUAL SCALE ... 0.002 AU" line the config lacks. |
| 47 | 55 | mantle | Residual (a), confirmed | Diamond claim present (with mercury:61 recording its removal elsewhere). |

### comet_visualization_shells.py

| # | Line(s) | Shell | Type | Description |
|---|---|---|---|---|
| 48 | 492–494 | (MAPS marker) | CLEARED | The known shadow-constant precedent is **fixed at HEAD**: locals removed in L-156 1f, replaced by module-scope imports, with an explanatory comment citing the No Shadow Constants gate. Confirm-and-close. |
| 49 | 6 locations | (module-wide) | STALE_ANNOTATION | 6 "Verified: April 2026" stamps — not previously enumerated. |

### Cross-file structural finding: `<br>` in the GUI tooltip path

**95 of 126 module `_info` strings contain `<br>` and zero `\n`** — every info string in the
moon, eris, pluto, mars, jupiter, saturn, uranus, neptune, planet9, and solar modules. These
are exactly the strings the Tk GUI passes raw to `CreateToolTip`, whose `tk.Label` renders
text literally — so the GUI checkbox tooltips for those ten bodies display literal `<br>`
markup. This contradicts shell_configs.py's own contract comment ("tooltip (Tk GUI, \n line
breaks)"). Clean modules: mercury (8/8), venus (7/7), earth (11/11), asteroid_belt (4/4).
The three Sun entries in CUSTOM_SHELLS (hills_cloud_torus, outer_oort_clumpy, galactic_tide)
inherit the same `<br>` strings. Render check pending Tony's eyes (Mode 5) — the code path
admits no other outcome, but the render is the close gate.

### Verified-consistent (stated so Batch 2 need not re-litigate)

Neptune hill (4685, exact), Uranus hill (7.02×10⁷ km vs rf 2770, 0.85%; text explicitly
notes mean radius 25,360 km while the denominator is equatorial 25,559 — acceptable),
Jupiter hill (740 → 52.9 M vs "53 million"), Mars hill config copy (324.5), all six Pluto
shells (core 1,700-km diameter / ~70%, exobase rf 2.43, hill 5041 — Batch 1 landed cleanly),
Eris hill (perihelion-based 8.0 M km with the 14.3 M average correctly explained), Moon
mantle (0.9655 with self-documenting arithmetic), Mercury inner core (0.41 → 1,000 km),
Earth inner/outer core and hill, Venus atmosphere and hill, Mars crust and upper atmosphere,
Planet 9 surface (24,000 km vs "~3.7 R_E" ≈ 23,600), Sun photosphere / radiative / inner
corona / streamer belt / Roche / Alfvén / termination shock / heliopause / all Oort shells,
Neptune and Uranus radiation-belt geometry (coded distances sit inside cited ranges),
Jupiter/Neptune/Uranus magnetopause and bow-shock standoffs vs their citations, Earth
magnetopause (10 R_E, text matches).

### Summary counts

**By file:** shell_configs.py 24 · saturn 4 · solar 4 · earth 6 · jupiter 3 · moon 3 ·
mercury 3 · comet 2 (1 cleared) · plus 1 cross-file structural. **Total: 50 finding rows**
(19 substantive value/citation conflicts, 12 cosmetic/format, 8 stale-annotation classes,
4 structural, 4 residual confirmations, 2 suspicions, 1 cleared).

**By type:** CONSTANT_VS_TEXT 14 · TEXT_VS_TEXT 3 · SOURCE_VS_VALUE 5 · CROSS_COPY_DRIFT 8 ·
SHADOW_CONSTANT 2 (+1 cleared) · STALE_ANNOTATION 44 stamps in 4 files + 2 false
"not yet rendered" claims · SUSPICION 2 · STRUCTURAL 4 · CONVENTION 1.

**The dominant substantive pattern:** Batch 1 moved display text and citations to the
corrected values (Hauck 2020 km, Sori 26 km, Weber 240/330 km, Venus 3,200 km) but the
`radius_fraction` geometry constants still encode the pre-patch numbers. The render draws
the old physics while the hover asserts the new — exactly the drift class this audit was
commissioned to find, one layer down from where Batch 1 looked.

---

## 2. Job 2 — Single-source-of-truth map

### Copy classes (the real structure, corrected from the prompt's two-location model)

For one physical value there are up to **six** storage forms:

1. `radius_fraction` / `radius_au` in SHELL_CONFIGS (live geometry)
2. `hover_text` in SHELL_CONFIGS (live Plotly hover)
3. `tooltip` in SHELL_CONFIGS (**dead**)
4. module `_info` string (live GUI tooltip)
5. `CUSTOM_SHELLS` tooltip (**dead**)
6. legacy inline builder dicts in the module (**dead** for sphere shells; live for custom geometry) — plus `# Source:` comments over 1, 2, 4, and 6 independently.

### Reference-pattern status (runtime identity test)

| Body | Sphere shells | Text pattern | Notes |
|---|---|---|---|
| Saturn | 6 | **REF** | config imports `*_info`; hover derived by `.replace('\n','<br>')` — a **no-op**, since the strings already contain `<br>` and no `\n` |
| Uranus | 5 | **REF** | same |
| Neptune | 5 | **REF** | same |
| **Sun** | 15 | **REF** | *extends the as-built list* — the Sun is already migrated; but 9 of 15 `_info`/`_info_hover` pairs are the same object (vestigial split) |
| Mercury | 6 | inline | duplicated; 2 shells drifted (crust/atm cosmetic, hill value) |
| Moon | 6 | inline | duplicated; crust drifted (values) |
| Planet 9 | 2 | inline | duplicated; agree |
| Pluto | 6 | inline | duplicated; agree (Batch 1 patched both copies) |
| Eris | 5 | inline | duplicated; agree |
| Venus | 6 | inline | duplicated; 1 cosmetic drift |
| Mars | 7 | inline | duplicated; hill + upper_atmosphere drifted |
| **Earth** | 8 | inline | *not migrated* (agrees byte-for-byte today — by luck, not linkage) |
| **Jupiter** | 6 | inline | *not migrated* (same) |

### Drifted-value map (every value found in >1 place that disagrees)

| Value | Copy 1 (live) | Copy 2 | Copy 3+ | Agree? | Ref? |
|---|---|---|---|---|---|
| Saturn Hill radius | shell_configs:1712 `rf 1120` (67.5 M km) | saturn:936 text "91 M km" | saturn:936 "151 R_S"; saturn:930/950 `# Source` "confirmed"; saturn:954 dead dict | **no — 3-way** | yes (text linked; constant not) |
| Mercury outer-core radius | shell_configs:118 `rf 0.85` (2,074) | config hover "2,020 km" | module info 2,020; mercury:44 citation 2,020±30 | **no** | no |
| Mercury crust thickness | rf pair 0.98→1.0 (49 km) | text "26 km (Sori)" | mercury:59 citation 26±11 | **no** | no |
| Mercury mantle thickness | rf pair 0.85→0.98 (317 km) | text "331 km" | — | **no** | no |
| Moon inner-core radius | shell_configs:247 `rf 0.1485` (258) | text "240 km" | moon:38 citation 240 | **no** | no |
| Moon outer-core radius | shell_configs:267 `rf 0.2083` (362) | text "330 km" | moon:130 citation 330 | **no** | no |
| Moon crust thickness | config text "50 near / 60 far" | config hover "20–30 … >100" | module "30–50 near / up to 100+ far"; encoded 60 km | **no — 3-way** | no |
| Venus core radius | shell_configs:924 `rf 0.5` (3,026) | text "3,200 km" | venus:38 citation 3,200 | **no** | no |
| Venus crust thickness | rf pair (121 km) | text "10–30 km" | — | **no** | no |
| Eris mantle thickness | rf pair 0.60→0.66 (70 km) | text "~100 km" | — | **no** | no |
| Earth lower-atm extent | shell_configs:1425 `rf 1.05` (319 km alt) | text "0–50 km" | — | **no** (stylization undeclared) | no |
| Earth upper-atm extent | shell_configs:1448 `rf 1.25` (1,595 km alt) | text "to ~1,000 km" | — | **no** (same) | no |
| Mars Hill radius | config `rf 324.5` + text 324.5 | mars:844/859 dead text "320" | mars:884 dead `radius_fraction = 320` | **no** (live copies agree; dead drifted) | no |
| Mars bow-shock standoff | mars:690 code 1.64 R_M + live texts "1.6" | shell_configs:2188 header "1.5 Rm" | dead custom tooltip "1.5" | **no** (dead+header stale) | n/a |
| Sun gravitational extent | constants_new:233 `150000` (renders) | solar:61/433 text "~126,000 AU" | solar:50/174 citations "=126000" | **no — constant vs both texts and its own citations** | yes |
| Sun chromosphere extent | constants_new:152 `1.1 R_sun` (renders) | text "to 1.5 Solar radii / 0.0070 AU" | same text "2,000 km" | **no — 3-way** | yes |
| Mercury hill scale note | config "0.005 AU" | mercury:422 "0.003 AU" | — | **no** | no |
| Earth mean radius | earth:907 `6371.0` | earth:1019 `6371.0` (second local def) | absent from constants_new | **agree with each other; uncited, wrong denominator vs EARTH_RADIUS_AU** | n/a |
| Jupiter/Saturn bow shock "not yet rendered" | code renders (jupiter:586, saturn:669) | dead custom tooltips claim otherwise (shell_configs:2371, 2474) | — | **no** | n/a |

Values in ≥2 places that **agree** (dual-pipeline but not drifted) are characterized by the
per-body counts below rather than enumerated row-by-row: for every inline body, *every* shell
text exists in ≥3 copies by construction (config hover + dead config tooltip + module info),
and the geometry-linked values (a km/AU figure in the text that the radius_fraction also
encodes) were machine-counted:

### Migration status summary

| Body | Text ref pattern? | Shells | Geometry-linked shells | km values in live hover | Drifted values |
|---|---|---|---|---|---|
| Mercury | no | 6 | 5 | 5 | 4 |
| Moon | no | 6 | 6 | 11 | 3 |
| Planet 9 | no | 2 | 1 | 1 | 0 |
| Pluto | no | 6 | 5 | 12 | 0 |
| Eris | no | 5 | 3 | 5 | 1 |
| Venus | no | 6 | 5 | 8 | 2 |
| Mars | no | 7 | 4 | 8 | 2 (dead copies) |
| Earth | no | 8 | 8 | 13 | 2 (+2 shadow constants) |
| Jupiter | no | 6 | 1 | 1 | 0 (+1 dead-claim) |
| Saturn | **yes** | 6 | 2 | 2 | **1 (the big one)** |
| Uranus | **yes** | 5 | 2 | 3 | 0 |
| Neptune | **yes** | 5 | 1 | 1 | 0 |
| Sun | **yes** | 15 | 5 | 6 | 2 |

### Migration-design implications (mapped, not designed — per the prompt's What-NOT-to-do)

1. The reference pattern links *text* copies only; it does **not** link geometry to text.
   Saturn — a fully migrated body — carries the worst finding in the audit. The constant
   layer has to link `radius_fraction` to the km value the text renders, or the same drift
   recurs.
2. 124 dead `tooltip` fields (83 sphere + 41 custom) are either delete-or-wire decisions
   before migration; migrating dead data entrenches it.
3. The canonical text should be stored once in `\n` form with `<br>` derived at the Plotly
   boundary — the current `.replace('\n','<br>')` no-ops prove the direction is currently
   inverted (the "canonical" strings are already `<br>`-formatted, and the GUI pays for it).
4. The legacy inline builder dicts (copy class 6) are the promotable-dead-code trap the
   prompt's architecture section warned about — Mars's dead `radius_fraction = 320`
   (mars:884) is a live example of what a naive promotion would resurrect.
5. Batch 2's three-model competitive cross-check should treat the `radius_fraction` values
   as first-class claims, not just the display text — that is where Batch 1's corrections
   failed to land.

---

## 3. Pre-work and residuals — status at HEAD

- Pre-work greps: valid by construction (only the prompt file changed since `55b07a6`).
- Residual (a) diamond claim: **present** — mercury:55, shell_configs:144/149.
- Residual (b) stale headers: **present** — Mercury 93–94, Moon 236–239; extended by the
  Mars header (shell_configs:2188, finding #16).
- Residual (c) 1700K color comment: **present** — moon:56.
- Residual (d) stale sodium-tail comment: **present** — palomas_orrery.py:7565.
- "Verified: April 2026" census at HEAD: shell_configs **16** (matches as-built),
  earth **13**, jupiter **9**, comet **6** = **44 total** (the last three counts are new
  information beyond the prompt's pre-work). All other audit files: 0.
- Comet shadow-constant precedent (492–493, 602): **cleared** in L-156 1f.

## 4. Honest gaps

- The row-per-value enumeration of *agreeing* dual-pipeline values is delivered as machine
  counts plus class map, not exhaustive rows (~200+ mechanically derivable agreements).
  Every **drifted** value is fully enumerated with file:line.
- The `<br>`-tooltip finding is code-path-proven but not render-verified; Mode 5 (Tony's
  eyes on a GUI tooltip for any Moon/Pluto/Sun shell) is the close gate.
- Comet, asteroid_belt, and planet9 display texts were audited for citations, stamps, and
  shadow constants but not line-by-line for internal numeric contradictions at the same
  depth as the planetary shell files; their citation blocks were read and are in the good
  (post-L-156) format.

*Report prepared August 4, 2026 by Claude Fable 5 · built on `679c2f4` — pushed-at SHA to be
appended by Tony after commit.*
