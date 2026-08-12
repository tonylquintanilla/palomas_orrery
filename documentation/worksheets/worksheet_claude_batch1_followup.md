# Follow-Up Worksheet -- Batch 1 Unresolved Items (Claude's Leg)

**Built on `e902549ee9e34afb2842fcdcc926b43da06c562c`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).**

**Checker:** Claude Opus 5
**Date:** 2026-08-03
**Resolved:** 6 of 18. The other 12 are marked NOT FOUND or NOT
ATTEMPTED and are listed explicitly.

---

## Read first: I was wrong about Venus, and it changes a recommendation

In the Tier 2 worksheet I told you to change Venus's
`radius_fraction` from 166 to 167. **Withdraw that.** The three-way
disagreement was not an arithmetic error by anyone. It was a convention
difference, and I picked the convention without checking which one the
project uses.

| Basis | r_H | In Venus radii |
|-------|----:|---------------:|
| Semimajor axis 108.21e6 km | 1,011,110 km | **167.08** |
| Perihelion 107.48e6 km | 1,004,289 km | **165.95** |
| Aphelion 108.94e6 km | 1,017,931 km | 168.20 |

My 167.1 was the semimajor-axis convention. Gemini's 1,004,000 km and
GPT's 165-166 are the **perihelion** convention -- and the code's 166
matches it to within a tenth of a radius.

The project already states a preference. The Eris Hill sphere comment
says outright that the shell geometry uses the perihelion-based Hill
sphere, and Pluto's 5.99 Mkm turns out to be perihelion-based too. Under
the project's own convention **166 is correct** and my recommendation
would have introduced an inconsistency.

The lesson generalizes past this one number: for a Hill sphere the
convention is not a rounding preference, it is a 1.3% swing on Venus and
a 20% swing on an eccentric body like Eris. Every Hill sphere comment
should name which distance it uses. That, and not the digits, is the
real fix across Mercury, Venus, Moon, Mars, Pluto, and Eris.

---

## Worksheet

| # | Question | What the source says | Source (specific) | Resolution |
|---|----------|---------------------|-------------------|------------|
| FU-M3 | Deep moonquake depth: 700-1200 or 700-1000 km? | Deep moonquakes occur in nests at depths of 700-1200 km. A narrower 800-1000 km band is where they *concentrate*, not the full range. | Nakamura et al. 1982, JGR 87:A117 (Apollo Lunar Seismic Experiment final summary); Nakamura 2005, JGR 110 | **CONFIRMED** (value); **WRONG CITATION** |
| FU-Me2 | Mercury crustal thickness: 35 or 26 km? | Sori 2018 finds a mean crustal thickness of **26 +/- 11 km**, described in the paper as 25% below the previously thinnest published figure. The 35 +/- 18 km value is Padovan et al. 2015. | Sori, M.M. 2018, "A thin, dense crust for Mercury", EPSL 489:92, DOI 10.1016/j.epsl.2018.02.033; Padovan et al. 2015, GRL 42:1029 | **WRONG VALUE and WRONG CITATION** |
| FU-Me3 | Mercury diamond layer -- is "Pei et al. 2024" right? | The paper is by Xu, Lin, Wu, Namur, Zhang and Charlier. Diamond crystallizes from the **cooling molten core** as the inner core solidifies, then floats to the core-mantle boundary, forming a layer up to ~18 km thick. | Xu, Y. et al. 2024, "A diamond-bearing core-mantle boundary on Mercury", Nature Communications 15:5061, DOI 10.1038/s41467-024-49305-x | **WRONG CITATION and WRONG MECHANISM** |
| FU-P1 | Pluto exobase: 1700 km altitude or from center? | The exobase is at a radius of ~2900 km, **or an altitude of ~1710 km**. Both numbers are given in the same sentence, so there is no ambiguity. | Young, L.A. et al. 2018, Icarus 300:174 (supersedes Gladstone et al. 2016 for the Alice occultation); corroborated by Strobel & Zhu 2017, Icarus | **WRONG VALUE** |
| FU-Er3 | Eris Hill sphere at 67.8 AU | Pure arithmetic; see derivation below. **14,265,497 km = 14.27 Mkm = 0.0954 AU** | Derived; inputs from JPL SSD and NSSDCA | **DERIVED** |
| FU-V3 | Venus Hill sphere from NSSDCA inputs | See the table above. The three-way split is a convention difference, not an error. | Derived; inputs from NSSDCA Venus Fact Sheet | **DERIVED** |

---

## FU-Me3 -- the most serious finding in this batch

Three things are wrong here, and only one of them is the author name.

**The author.** The third author of the paper is **Peiyan Wu**. "Pei" is
the first half of a given name, not a surname. "Pei et al. 2024" is
almost certainly a mis-parse of that. The paper is universally cited as
Xu et al. 2024.

This is the citation-fabrication pattern in its most deceptive form. The
year is right, the subject is right, and a plausible-looking surname was
lifted out of the middle of a real author's given name. It survives a
casual glance precisely because it is nearly right.

**The mechanism.** The code says the diamond layer formed "by billions
of years of meteorite impacts on a graphite-rich surface." The paper
says nothing of the kind. Diamond exsolves from the cooling molten
metallic core as the inner core crystallizes, and floats up to the
core-mantle boundary. Impacts play no role.

**The location.** The code puts this in the **crust** section. The paper
puts the layer at the **core-mantle boundary**, hundreds of kilometres
below the crust. A reader of the orrery would come away believing the
diamonds are near the surface, which is the opposite of what the paper
argues -- the authors specifically note the depth makes them
unreachable.

The primordial graphite flotation crust is a real and separate feature,
and MESSENGER's carbon detection is what motivated the study. So there
is a true statement in the neighbourhood. But the code has fused a
surface feature and a deep-interior one into a single claim that no
paper supports.

**Recommended:** rewrite the claim entirely, move it out of the crust
block, and cite Xu et al. 2024 properly. Or drop it -- the layer is
hypothesized, not observed, and a shell visualization has no obvious
place to put an 18 km layer at a boundary the model does not render.

---

## FU-Me2 -- the citation points at the paper that refutes it

Sori 2018 exists specifically to revise Mercury's crustal thickness
downward. Its finding is 26 +/- 11 km, and the number it revises is the
35 +/- 18 km from Padovan et al. 2015, which assumed Airy isostasy with
a single geoid-to-topography ratio.

So the code cites Sori for the value Sori's paper was written to
replace. Gemini's reading was right.

Worth knowing before you decide: the field has not fully settled on 26.
Later gravity work gives 23-50 km depending on the assumed minimum
spherical-harmonic degree and crustal density, and a 2023 flexural model
puts the crust-mantle interface between 19 and 42 km.

**Recommended:** either 26 +/- 11 km citing Sori 2018, or 35 +/- 18 km
citing Padovan et al. 2015. Both are honest. The current pairing is the
one combination that is not.

---

## FU-P1 -- a unit confusion, and GPT called it correctly

The source sentence gives both numbers together: the exobase sits at a
radius of ~2900 km, which is an altitude of ~1710 km. So:

| Reading | From center | Altitude | In Pluto radii |
|---------|------------:|---------:|---------------:|
| Code's reading (1700 km = radius) | 1,700 km | 512 km | 1.43 |
| **Correct** (1700 km = altitude) | **2,888 km** | 1,700 km | **2.43** |

The code's two figures, ~1700 km and ~1.43 R_Pluto, are internally
consistent -- but only under the wrong reading. That internal
consistency is what let the error survive: both numbers agree with each
other, so nothing looks off.

**Recommended:** exobase at ~1710 km altitude, ~2900 km from centre,
~2.44 Pluto radii. And change the citation: the Alice occultation
results were superseded by Young et al. 2018, which says so in its own
abstract.

**Related, not asked:** the same search turned up that Gladstone et al.
2016 reported Pluto's surface temperature as **37 +/- 3 K**, against the
code's ~40 K (claim P13). 40 sits at the top edge of the error bar. Not
wrong, but worth a look when P13 gets its turn.

---

## FU-M3 -- the code is right and a checker was wrong

700-1200 km is the standard published range, and it is not marginal. It
appears in Nakamura's own final summary of the Apollo experiment, in
Nakamura 2005, and in every review and reference work I checked.

The 800-1000 km figure is real but describes something different: the
depth interval where deep moonquake nests **concentrate**. Nakamura 1982
puts it precisely -- locations are bounded fairly sharply between about
800 and 1000 km, with clusters near both boundaries. That is a
sub-structure within the 700-1200 km range, not a replacement for it.

So GPT's 700-1000 km is a narrower band from a different framing, and
the code's number should stand.

The citation still needs fixing. "NASA Moon Fact Sheet; Apollo Seismic
Experiment reports" names no document. The real source is Nakamura et
al. 1982, JGR 87:A117, and Nakamura 2005, JGR 110.

---

## FU-Er3 and FU-V3 -- the arithmetic, with every input shown

Formula: r_H = a (m / 3 M_sun)^(1/3)

**Solar mass, derived rather than recalled.** Applying Kepler's third
law to Mars's own orbit, using NSSDCA Mars Fact Sheet values (a =
227.956e6 km, T = 686.980 d):

- GM_sun = 4 pi^2 a^3 / T^2 = **1.32739e11 km^3/s^2**
- M_sun = GM_sun / G, with G = 6.67430e-11 m^3/kg/s^2 = **1.98880e30 kg**

**Eris (FU-Er3):**

- m = 1.66e22 kg (JPL SSD dwarf planet parameters)
- a = 67.8 AU = 10,142,735,633 km
- (m / 3 M_sun)^(1/3) = 1.406474e-3
- **r_H = 14,265,497 km = 14.27 Mkm = 0.0954 AU = 12,266 Eris radii**

At perihelion, 38.0 AU: **7,995,411 km = 8.00 Mkm = 6,875 Eris radii**.
The code's shell (`radius_fraction` 6965 = 8.10 Mkm) matches this within
1.3%.

The code's 9.4 Mkm at 67.8 AU is not reproducible. I tried the
semimajor axis, perihelion, aphelion, and the (1-e) factor, with both
the JPL mass and a mass computed independently from Sicardy's radius and
density. None produces 9.4.

**Venus (FU-V3):**

- m = 4.8675e24 kg (NSSDCA Venus Fact Sheet)
- R_V = 6051.8 km (same sheet, volumetric mean)
- Results in the table at the top of this document.

---

## Not resolved (12 items)

Marked so the gap is explicit. None of these should be read as passing.

| # | Status | Note |
|---|--------|------|
| FU-M1 | NOT FOUND | Lunar inner core 1600-1700 K. Did not reach Williams et al. 2006 or Laneuville. |
| FU-M2 | NOT FOUND | Lunar outer core 1300-1600 K. Same. |
| FU-Me1 | NOT ATTEMPTED | Mercury outer core 1074 km. Hauck et al. 2013 is the right candidate to check; Margot 2012 is a moment-of-inertia paper, so Gemini's reading is likely correct. |
| FU-Me4 | NOT ATTEMPTED | Sodium tail 10,000 R_M. Potter & Morgan 1985 is the discovery paper for the sodium exosphere; the tail-length figure is almost certainly later. |
| FU-Er1 | NOT FOUND -- and likely unpublishable as stated | All three checkers agree Sicardy 2011 reports density, not composition. A rocky mass fraction is a two-end-member inference requiring assumed rock and ice densities, neither of which the code states. If it stays, it needs to be labeled as derived with those assumptions written down. |
| FU-Er2 | NOT ATTEMPTED | Glein et al. 2024, Eris core 875 K. |
| FU-V1 | NOT ATTEMPTED | Venus atmospheric layer boundaries. Five separate values, each needing its own publication. |
| FU-V2 | NOT ATTEMPTED | Venus magnetotail 45-60 R_V. |
| FU-P2 | NOT ATTEMPTED | Pluto core ~1000 K from Bierson et al. 2020. |
| FU-P3 | NOT ATTEMPTED | Sputnik Planitia N2 >98%. Grundy et al. 2016 is the right candidate. |
| FU-Dy1 | NOT ATTEMPTED | Dysnomia semi-major axis. |
| P13 | NEW, PARTIAL | Pluto surface 40 K vs Gladstone 2016's 37 +/- 3 K. Surfaced incidentally; see FU-P1. |

---

## Tony-action rollup

- **(do)** Revert my Tier 2 recommendation on Venus. `radius_fraction =
  166` is correct under the project's perihelion convention. Nothing to
  change.
- **(decide)** Adopt one Hill sphere convention project-wide and state
  it in every Hill sphere comment. The evidence says the project already
  uses perihelion; Mars's 324.5 R_Mars matches neither convention and is
  the outlier that needs fixing.
- **(decide)** FU-Me3: rewrite the Mercury diamond claim -- wrong
  author, wrong mechanism, wrong depth -- or remove it.
- **(decide)** FU-Me2: choose 26 +/- 11 km with Sori 2018, or 35 +/-
  18 km with Padovan et al. 2015.
- **(decide)** FU-P1: exobase to ~2.44 Pluto radii, citing Young et al.
  2018.
- **(do)** FU-M3: keep 700-1200 km, change the citation to Nakamura et
  al. 1982 and Nakamura 2005.
- **(decide)** FU-Er3: Eris's 9.4 Mkm is not reproducible from any
  convention. Correct to 14.27 Mkm or drop the average-distance figure.
- **(do)** Route the 12 unresolved items to a checker with journal
  access. FU-Me1, FU-Er2, FU-P2, and FU-P3 are all single-paper lookups.

---

*Prepared August 3, 2026 by Claude Opus 5, independently of the GPT and
Gemini legs. Arithmetic uses NASA NSSDCA fact-sheet and JPL SSD inputs
with a solar mass derived from Kepler's third law -- no recalled
constants.*
