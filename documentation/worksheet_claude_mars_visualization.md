# Cross-Check Worksheet (Claude's Leg) -- `mars_visualization_shells.py`

**Built on `8d7c6074c020123917716b47853880f3a5b492b8`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).**

**Checker:** Claude Opus 5
**Date:** 2026-08-01
**Track:** L-156 Phase 2, Track 1 -- second leg of the competitive pattern
**Gemini worksheets NOT read.** Every value below was researched fresh
against primary and peer-reviewed sources via web search.

---

## Base reconciliation

The Track 1 prompt anchors to `373c6d8`. Live HEAD at session start was
`8d7c607`, three commits ahead: `LEDGER_CONSOLIDATED.md`, the two master
plan documents, the Piece 1 as-built and ledger/master-plan update
documents, and the Track 1 prompt itself. No source file changed.
Piece 1 is confirmed present in `provenance_scanner.py` at HEAD.

---

## Scope note -- read before scaling

The scanner reports **4 findings** for this file. Each finding is one
numeric token, but the `# Source:` block above it covers a whole
paragraph containing several distinct factual claims. Verifying "the
finding" and verifying "the claim" are not the same job.

I verified **every factual claim inside each cited block**, which
produced 8 rows from 4 findings. I also verified the two inline-cited
code constants that set the rendered geometry, because one of them
contradicts the display text.

**Tony-action (decide):** confirm this granularity before Earth (27
findings) and `info_dictionary.py` (124). Row-per-claim rather than
row-per-finding roughly doubles the work but is the only level at which
an annotation is honest -- annotating a block means asserting the block
was checked.

---

## Worksheet

| # | Claim in code | My value | My source | Match? |
|---|---------------|----------|-----------|--------|
| M1 | Exosphere starts above the thermosphere "around 200 km/124 miles" | Exobase is variable: 140-200 km (MAVEN NGIMS), "near 170-200 km", ~220 km in some treatments. Not a sharp boundary. | Thiemann et al. 2018, JGR Planets (MAVEN EUVM occultations); MAVEN NGIMS exobase/homopause study, Icarus 2025; "The Aeronomy of Mars", LASP/MAVEN | **YES** (upper end of range) |
| M2 | Induced magnetosphere extends "only about 1-2 Mars radii on the Sun-facing side" | MPB subsolar standoff 1.29 +/- 0.04 R_M (Vignes 2000); 1.25 +/- 0.03 (Trotignon 2006); 1.33 +/- 0.15 (Edberg 2008) | Astronomy & Astrophysics 2021, MPB standoff study, summarizing all three | **YES** |
| M3 | Bow shock "around 1.5 Mars radii" (appears twice: `mars_magnetosphere_info` and `bow_shock_text`) | 1.64 +/- 0.08 R_M (Vignes 2000); 1.63 +/- 0.01 (Trotignon 2006); 1.58 +/- 0.18 (Edberg 2008); 1.63 from MHD simulation | ApJ 2020, "A 3D Parametric Martian Bow Shock Model", quoting all three empirical models | **NO -- diverges** |
| M4 | Earth's bow shock "around 15 Earth radii" | ~15 R_E typical (BIRA-IASB); 11-14 R_E under normal solar wind; 13 R_E (Jelinek 2012 empirical) to 18 R_E (Chapman & Cairns 2003 MHD); ~14 R_E / 90,000 km typical | Royal Belgian Institute for Space Aeronomy encyclopedia; Nature Communications 2016 (sub-Alfvenic solar wind); arXiv 1709.01407 | **YES** (at the upper end) |
| M5 | Hill sphere "extends to ~324.5 Mars radii" | **319.8 R_Mars** | Derived from NASA NSSDCA Mars Fact Sheet (see derivation below); independently corroborated by the Project Pluto planetary Hill-radius table at 319.8 R_Mars | **NO -- 1.5% high** |
| M6 | Hill sphere "about 1.1 million km" | 1,084,062 km (1.084 Mkm) | Same derivation; Project Pluto table gives 1,084,000 km | **YES** as a rounding ("about") |
| M7 | Source comment: Hill sphere varies "~0.8 Mkm perihelion to ~1.2 Mkm aphelion" | Perihelion **0.983 Mkm**, aphelion **1.185 Mkm** | Same derivation, using fact-sheet perihelion 206.650e6 km and aphelion 249.261e6 km | Aphelion **YES**; perihelion **NO -- diverges** |
| M8 | `sunward_distance = 1.29` R_M (MPB), cited to Vignes et al. 2000 | 1.29 +/- 0.04 R_M, Vignes et al. 2000 | A&A 2021 MPB standoff study, quoting Vignes 2000 directly | **YES** |
| M9 | `bow_shock_standoff = 1.64` R_M, cited to Vignes et al. 2000 | 1.64 +/- 0.08 R_M, Vignes et al. 2000 | ApJ 2020 Martian bow shock model, quoting Vignes 2000 directly | **YES** |

Nine rows because M5/M6/M7 split one finding's three separate numbers,
and M8/M9 are inline-cited constants outside the finding list.

---

## Divergences, in priority order

### D1. The bow shock display text says 1.5 R_M; the code says 1.64 [HIGH]

Two display strings tell the reader the Martian bow shock sits "around
1.5 Mars radii." The rendered geometry uses 1.64. The inline comment on
that constant says, in the code's own words, that 1.5 was too low and
was corrected against the Vignes pair.

So the April correction landed on the constant and never reached the two
strings describing it. The plot and its caption now disagree, and the
caption is the part a reader believes.

My independent research confirms the constant, not the text: every
empirical model I found puts the subsolar bow shock between 1.58 and
1.64 R_M. Nothing supports 1.5.

Locations: `mars_magnetosphere_info` (the "2. Bow Shock" sentence) and
`bow_shock_text` (the "much closer to Mars" sentence).

**This blocks annotation of both blocks.** A `# Cross-checked:` line
over text that contradicts its own module's constant would certify the
wrong number.

### D2. Hill sphere 324.5 R_Mars should be 319.8 [MEDIUM]

Deriving from the NASA fact sheet:

- a = 227.956e6 km, GM_Mars = 0.042828e6 km^3/s^2, R_Mars = 3389.5 km
- GM_Sun from Kepler III on Mars's own orbit (T = 686.980 d) =
  1.32739e11 km^3/s^2, so no external mass constant is needed
- r_H = a * (GM_Mars / 3 GM_Sun)^(1/3) = **1,084,062 km**
- = 1.084 Mkm = **319.8 R_Mars** = 0.00725 AU

324.5 x 3389.5 = 1,099,893 km. That is 1.1 Mkm exactly, which is the
tell: the radii figure looks derived from the *rounded* 1.1 Mkm rather
than from the underlying 1.084. The rounding is fine on its own; the
problem is a second value carrying a decimal place it has not earned.

The Project Pluto planetary table independently gives Mars 319.8
R_Mars / 1,084,000 km / 0.0073 AU, matching my derivation to all quoted
digits.

### D3. The perihelion Hill radius in the source comment [MEDIUM]

The citation block says the Hill sphere runs ~0.8 Mkm at perihelion to
~1.2 Mkm at aphelion. Aphelion checks out at 1.185 Mkm. Perihelion does
not: 206.650e6 km x the same factor gives **0.983 Mkm**, not 0.8. I
could not find a convention that produces 0.8.

This one matters more than it looks, because it sits in a `# Source:`
comment. It is a provenance claim, not display text.

### D4. Provenance question on the Hill sphere citation [MEDIUM]

The block cites "NASA Solar System Dynamics." I could not find a JPL SSD
page publishing a Mars Hill radius of 324.5 R_Mars or 1.1 Mkm. JPL SSD
publishes the orbital and physical elements a Hill radius is *computed
from*, which is a different thing.

If the number was computed from SSD inputs rather than read off an SSD
page, the honest citation names the inputs and the formula. As written,
the citation asserts a provenance I cannot confirm.

**Tony-action (decide):** whether D4 is a citation correction (rewrite
to name the derivation) or a sourcing gap.

---

## Convergent and ready to annotate, if Gemini agrees

- **M1** exosphere ~200 km -- with the caveat that the exobase moves
  40-45 km between aphelion and perihelion, so "around" is doing real
  work in that sentence.
- **M2** induced magnetosphere 1-2 R_M sunward.
- **M4** Earth bow shock ~15 R_E -- defensible, though several sources
  center lower (13-14). If Gemini also landed at 15, convergence is
  real; if Gemini landed at 13-14, this is worth a second look rather
  than a tie-break.
- **M6** Hill sphere "about 1.1 million km".
- **M8**, **M9** the two Vignes constants -- these are the cleanest
  results in the file. Both matched to the stated uncertainty.

---

## Sources used

- Vignes et al. 2000, *Geophys. Res. Lett.* 27, 49 -- MGS MAG/ER bow
  shock and MPB locations (accessed via ADS and the AGU listing)
- Wang et al. 2021, *Astronomy & Astrophysics* -- MPB subsolar standoff
  vs solar wind density and velocity; quotes Vignes/Trotignon/Edberg
- 2020, *ApJ* -- "A 3D Parametric Martian Bow Shock Model with the
  Effects of Mach Number, Dynamic Pressure, and the IMF"
- Thiemann et al. 2018, *JGR Planets* -- MAVEN EUVM solar occultations,
  thermosphere structure and exobase altitude
- MAVEN NGIMS exobase and homopause study, *Icarus* 2025
- "The Aeronomy of Mars", MAVEN/LASP
- Royal Belgian Institute for Space Aeronomy -- magnetosphere boundary
  encyclopedia entry (Earth bow shock standoff)
- *Nature Communications* 2016 -- Earth's magnetosphere under
  sub-Alfvenic solar wind
- NASA NSSDCA Mars Fact Sheet (Williams, NASA GSFC) -- bulk and orbital
  parameters
- Project Pluto planetary Hill-radius table -- corroboration only, not
  the primary basis for D2

---

## Tony-action rollup

- **(decide)** Confirm the row-per-claim granularity before scaling to
  Earth and `info_dictionary.py` (scope note above).
- **(decide)** D1: correct the two "1.5 Mars radii" display strings to
  match the 1.64 constant. Until then neither block can be annotated.
- **(decide)** D2: correct 324.5 R_Mars to 319.8, or drop the radii
  figure and keep only "about 1.1 million km".
- **(decide)** D3: correct the perihelion figure in the source comment
  from ~0.8 Mkm to ~0.98 Mkm.
- **(decide)** D4: whether the "NASA Solar System Dynamics" citation on
  the Hill sphere block is rewritten as a derivation or treated as a
  sourcing gap.
- **(do)** Lay this beside `documentation/worksheet_mars_visualization.md`
  (Gemini's April leg) and mark convergence per row.

---

*Worksheet prepared August 1, 2026 by Claude Opus 5, independently of
Gemini's April 2026 results.*
