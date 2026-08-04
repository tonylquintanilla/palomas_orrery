# Patch Specification — Batch 1 Cross-Check Fixes

**Built on `2ccf6839c4278f01db00fbe2101440ab267a90c2`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Verify HEAD matches before implementing.**

**Prepared:** August 3, 2026 by Claude Opus 4.6 (orchestration)
**Implements:** L-156 Phase 2 Batch 1 cross-check decisions

This spec is long. Use the file-level headers and edit IDs to navigate.

---

## Implementation notes

- Each edit has a unique ID (file prefix + number).
- Edits listed BOTTOM-UP per file for safe line-number ordering.
- Build as transactional patch scripts (one per file, binary-mode).
- Remove ALL `# Verified: April 2026 via Gemini fact-check` lines.
- Add `# Cross-checked:` annotations per provenance-discipline v1.5.
- Run py_compile + xvfb smoke test after each file's patch.
- Credit the model that found each correction.

---

# moon_visualization_shells.py

**MOON-1** (line 557): Hill sphere Source — replace with derived format, perihelion convention, note 60,000 km is conventional rounded value (range 58,147–64,901 km). Citation: derived from NSSDCA inputs. Credit: Claude (computation), GPT+Gemini (convergence).

**MOON-2** (line 208): Moonquake Source — replace "NASA Moon Fact Sheet; Apollo Seismic Experiment reports" with Nakamura et al. 1982, JGR 87:A117 and Nakamura 2005, JGR 110. Keep 700–1,200 km. Note concentration at 800–1,000 km. Credit: Claude (confirmed range from Nakamura abstract).

**MOON-3** (line 121): Outer core Source — keep dimensions (330 km, 150 km partial melt). DROP temperature 1300–1600 K from Source comment. Add note: unsourced after three independent searches. Weber 2011 is seismic, not thermal. In display text (line 129), replace temperature claim with "temperature is model-dependent and not well constrained." Credit: GPT+Gemini (both identified Weber as wrong citation type).

**MOON-4** (line 38): Inner core Source — keep dimension (240 km). DROP temperature 1600–1700 K. Same treatment as MOON-3. In display text (line 59), replace temperature sentence. Credit: GPT+Gemini.

---

# eris_visualization_shells.py

**ERIS-1** (lines 457–483): Hill sphere — fix 9.4 Mkm to ~14.3 Mkm in both display text copies (lines 466 and 482). Replace Source with derived format: system mass 1.66e22 kg from JPL SSD (= Eris-Dysnomia system mass by construction from Dysnomia orbit), perihelion 38.0 AU gives ~8.0 Mkm (shell uses this), semi-major axis 67.8 AU gives ~14.3 Mkm. Note barycenter binary convention. Remove "Verified" line. Credit: GPT (first to flag), Claude (confirmed computation).

**ERIS-2** (line 34): Core Source — replace Glein et al. 2024 with Nimmo & Brown 2023, Science Advances 9, eadi9201. Record four model inputs (heating 4.5e-12 W/kg, conductivity 3 W/m/K, surface 30 K, result 875 K). Note: modeled, ~500 K below rock melting, one model's output. Cite Nimmo & Brown for differentiation claim. In display text, replace ">85% rock" with "rock-dominated, differentiated interior." Remove "Verified" line. Credit: GPT (identified paper), Claude delta (corrected authorship, found differentiation claim).

**ERIS-3** (line 208): Crust — remove "Verified" line. Add Cross-checked annotation. No value changes.

**ERIS-4** (line ~385): Atmosphere — ADD new Source citation (Sicardy et al. 2011, Nature 478:493-496). Upper limit ~1 nbar, ~10,000x more tenuous than Pluto, temperature approximately −240°C (modeled range −217 to −243°C). This is the Tier 1 sourcing fix.

---

# mercury_visualization_shells.py

**MERC-1** (line 398): Hill sphere — remove "Verified" line. Replace Source with derived format, perihelion convention, body mass (no significant companion). No numeric Hill sphere in display text so annotation is qualitative.

**MERC-2** (lines 81–121): Sodium tail — MAJOR VALUE FIX. Replace 10,000 R_M with observed range ~120 to ~1,400 R_M. Citation: Baumgardner et al. 2008, GRL 35 (~1,400 R_M max); Schmidt et al. 2010, Icarus (>1,000 R_M, variable). Note Potter & Morgan 1985 is exosphere discovery, not tail extent. Fix display text in both copies (lines 87–88, 112–113): range and km values. Fix code: `max_tail_length = 1400 * MERCURY_RADIUS_AU`. Credit: GPT (flagged 10,000 as unsupported, Tier 2), Claude (confirmed from Baumgardner abstract, blind lookup).

**MERC-3** (line 44): Outer core — replace 1074 km with Hauck et al. 2013 core radius 2020 ± 30 km (for visualization). Source: Hauck et al. 2013, JGR Planets 118:1204. Display text: "Core radius approximately 2020 km." Remove "Verified" line. Credit: GPT+Gemini (both identified Hauck).

**MERC-4** (line 57): Crust — fix 35 km to 26 ± 11 km citing Sori 2018, EPSL 489:92. DROP diamond layer claim entirely (wrong author "Pei" = mis-parsed given name, wrong mechanism, wrong location). Remove "Verified" line. Display text: "About 26 km thick (Sori 2018)." Credit: Gemini (identified Sori gives 26 not 35, Tier 2), Claude (confirmed and identified Xu et al. 2024 as real paper, follow-up).

**MERC-5** (line 67): Exosphere — remove "Verified" line. Add Cross-checked annotation. No value changes.

**MERC-6** (lines 233, 524, 594): Magnetosphere — remove "Verified" from line 233. Add Cross-checked annotation confirming Winslow values. No value changes.

---

# venus_visualization_shells.py

**VEN-1** (line 649): Hill sphere — keep radius_fraction = 166. Replace Source with derived format: perihelion convention (107.48 Mkm gives ~1.004 Mkm / 166 R_V). Note semi-major axis gives 167.1 R_V. Credit: Claude (identified perihelion convention from project precedent, corrected own earlier recommendation).

**VEN-2** (line 560): Magnetotail Source — replace "ESA Venus Express; Pioneer Venus" with Edberg et al. 2024, JGR Space Physics 129, e2024JA032603 for the 45–60 R_V extent. Keep bow shock 1.3–1.7 R_V from Shan et al. 2015. Credit: GPT (identified Edberg 2024, follow-up).

**VEN-3** (line 417): Upper atmosphere Source — replace with Bertaux et al. 2007, Nature 450:646 for mesosphere 60–100 km only. Note thermosphere temperature and ionosphere peak are model/time-dependent; specific values removed. In display text: soften "300 K (27 degC)" to "vary significantly with altitude, local time, and solar conditions." Soften "120-140 km" ionosphere peak to "upper atmosphere." Credit: GPT (Bertaux identification).

**VEN-4** (lines 328–352): Atmosphere Tier 1 fixes — add Source above venus_atmosphere_info citing NSSDCA Venus Fact Sheet (92 bars, 464°C, 96.5%/3.5%). Fix "about 90 times" to "about 92 to 93 times." Fix troposphere to "approximately 60-65 kilometers (visualization uses 60 km)." De-duplicate description dict to reference venus_atmosphere_info with .replace("\\n", "<br>"), or if fragile, fix both copies and comment the duplication. Credit: Claude (NSSDCA identification, Tier 1), GPT (Sánchez-Lavega 2018 for tropopause range).

**VEN-5** (line 38/55): Core — add Cross-checked annotation. No value changes.

**VEN-6** (line 505/524/594): Magnetosphere parameters — add Cross-checked annotation confirming Zhang 2007 and Shan 2015 values.

---

# pluto_visualization_shells.py

**PLUT-1** (lines 565–596): Hill sphere — fix radius_fraction from 4685 to 5041. Replace Source with derived format: Pluto-Charon system mass (GM 869.3 + 106.1 from JPL SSD), perihelion 29.66 AU, ~5.99 Mkm. Document system-mass convention for barycenter binaries. Also fix inner Source comment. Credit: Claude (reverse-engineered convention, identified geometry mismatch), GPT (provided specific GM values).

**PLUT-2** (lines 474–516): Exobase — fix radius_fraction from 1.43 to 2.43. Fix Source: cite Young et al. 2018, Icarus 300:174 (supersedes Gladstone 2016). Exobase at ~1,710 km altitude / ~2,900 km from center / ~2.43 R_Pluto. Fix display text: keep "1700 km above the surface" (correct as altitude), fix "1.43 Pluto radii" references to "2.43 Pluto radii from center." Also fix inner Source comment. Credit: GPT (identified unit confusion, Tier 2), Claude (confirmed from Young et al., blind lookup).

**PLUT-3** (lines 33–70): Core — DROP "core temp ~1,000 K" from Source comments (both copies). Replace with note that Bierson supports hot-start formation, not a specific present temperature. In display text: remove the "Estimated Temperature: around 1000 K" paragraph. Change "around 40 K" surface temperature to "approximately 37-39 K (Gladstone et al. 2016: 37 ± 3 K; REX analysis: 38.9 ± 2.1 K)." Credit: Claude (verified Bierson abstract contains no temperature, blind lookup), GPT (consistent NOT FOUND).

**PLUT-4** (lines 205–238): Crust — replace ">98%" N2 with "predominantly nitrogen ice." Fix Source to cite Grundy et al. 2016 alongside Stern 2015. Note: no paper quantifies purity. Fix inner Source comment similarly. Credit: GPT (identified >98% as unsupported, Tier 2).

**PLUT-5** (lines 123/140): Mantle — add Cross-checked annotation. No value changes.

**PLUT-6** (lines 373/397): Haze/atmosphere — add Cross-checked annotation. No value changes.

---

## Edit count

| File | Value fixes | Citation fixes | Annotations | Total |
|------|:-----------:|:--------------:|:-----------:|:-----:|
| Moon | 2 (drop temps) | 4 | 4 | 10 |
| Eris | 2 | 3 | 4 | 9 |
| Mercury | 3 | 4 | 3 | 10 |
| Venus | 2 | 3 | 3 | 8 |
| Pluto | 4 | 3 | 3 | 10 |
| **Total** | **13** | **17** | **17** | **47** |

---

## Not in this patch

- Hill sphere class fix for Mars and gas giants (Batch 2+)
- Eris atmosphere wording ("upper limit" vs "detection" distinction in display text)
- Schmidt et al. 2010 bibliographic title reconciliation
- Venus VIRA-sourced values (thermosphere, ionosphere) if later sourced

---

*Patch specification prepared August 3, 2026 by Claude Opus 4.6.*
