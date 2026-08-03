# Cross-Check Worksheet -- Batch 1 Tier 2 (Claude's Leg, Partial)

**Built on `e902549ee9e34afb2842fcdcc926b43da06c562c`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).**

**Checker:** Claude Opus 5
**Date:** 2026-08-03
**Coverage:** 15 of 56 claims verified. The other 41 are **NOT ATTEMPTED**
and are listed as such. Read the coverage section before using this.

---

## Base reconciliation

The prompt anchors to `2ccf683`; live HEAD is `e902549`. All five shell
modules pulled fresh at HEAD. Line numbers and claim text in the prompt
match the files.

---

## Coverage, stated before the findings

56 claims, each needing an independent live source check, is more work
than one session can do honestly. I had a choice between 56 shallow rows
and a smaller number of rows I actually stand behind, and I took the
second.

**What I verified completely (15 claims):** every derived, computed, or
internally-checkable claim in the batch -- the five Hill spheres, the
sodium tail conversion, the Eris orbital geometry, and the Eris
radius/density pair. These are verifiable to the digit from fact-sheet
inputs plus arithmetic, with no judgment call about what a source
"supports."

**What I did not attempt (41 claims):** everything requiring a paper to
be opened -- Weber 2011, Margot 2012, Sori 2018, Pei 2024, Winslow 2013,
Zhang 2007, Shan 2015, Stern 2015, Bierson 2020, Gladstone 2016, Glein
2024, Potter & Morgan 1985. Those are listed at the end, unmarked.

**This is why the derived subset was worth taking first:** four of the
fifteen are wrong, and three of those four are wrong in a way no source
lookup would have caught. They are arithmetic that does not close.

**Recommended:** split the remaining 41 into two or three prompts by
source family (lunar seismology; Mercury magnetosphere; Pluto/New
Horizons) so each checker can actually open the papers.

---

## Findings, worst first

### F1 -- Eris Hill sphere at average distance: off by 34% [HIGH]

The display text, duplicated at lines 465-467 and 481-483, says that at
Eris's average orbital distance of ~67.8 AU the Hill sphere radius is
approximately 9.4 million km (~0.06 AU).

Computing it from the same inputs:

- Eris mass 1.66e22 kg (JPL SSD dwarf planet table)
- a = 67.8 AU
- r_H = a (m / 3 M_sun)^(1/3) = **14.27 Mkm = 0.0954 AU**

Not 9.4 Mkm. The error is 34%, and I could not find any convention --
different mass, different distance, (1-e) factor -- that produces 9.4.

The perihelion figure in the same sentence is fine: 38 AU gives **8.00
Mkm** against the code's ~8.1, and the rendered shell
(`radius_fraction = 6965` x 1163 km = 8.10 Mkm) matches the text it
claims to. So the shell you actually see is right. It is the alternative
figure quoted alongside it that is wrong.

### F2 -- Pluto's Hill sphere shell is 7% smaller than its own caption [HIGH]

Three different numbers are in play and no two agree:

| Source | Value |
|--------|------:|
| Display text and `# Source:` comment | 5.99 Mkm |
| Rendered shell (`radius_fraction = 4685` x 1188.3 km) | **5.567 Mkm** |
| Computed, semimajor axis + Pluto alone | 7.663 Mkm |
| Computed, perihelion + Pluto alone | 5.756 Mkm |
| Computed, perihelion + Pluto-Charon system mass | **5.981 Mkm** |

The good news: **5.99 Mkm is defensible and I can tell you exactly where
it comes from.** Perihelion distance with the Pluto-Charon *system* mass
gives 5.981 Mkm. That is a sensible convention for a shell whose whole
point is "all five moons sit inside this," since Charon is 12% of the
system mass and ignoring it understates the sphere that binds the
others.

The bad news: nothing says so, and the rendered geometry uses neither.
`radius_fraction = 4685` produces 5.567 Mkm -- 7% inside the caption.
I could not reverse-engineer 4685 from any combination of published
Pluto mass, radius, and orbital distance.

This is the Mars bow shock pattern again: the number in the caption and
the number in the geometry drifted apart, and only the caption is
legible to a reader.

**Recommended:** set `radius_fraction` to 5041 (= 5.99 Mkm / 1188.3 km)
and write the convention into the comment -- perihelion distance,
Pluto-Charon system mass -- so the next checker does not have to
reverse-engineer it as I just did.

### F3 -- Venus Hill sphere: the code contradicts its own citation [MEDIUM]

The citation says ~1.01 million km / ~167 Venus radii. My computation
agrees: **1,011,109 km = 167.1 R_V**, from NSSDCA Venus mass 4.8675e24
kg and semimajor axis 108.21e6 km.

The code uses `radius_fraction = 166`, which is 1,004,599 km -- 6,500 km
low and one radius short of what its own comment states.

**Recommended:** 167. This is the cleanest correction in the batch; the
citation was already right.

### F4 -- Moon Hill sphere: the number is conventional, the citation is not real [MEDIUM]

The arithmetic inside the claim is sound. 34.53 x 1737.4 km = 59,992 km,
so the stated derivation from the lunar mean radius closes exactly.

The base figure is 2.5% low against a straight computation:

| Basis | r_H |
|-------|----:|
| Semimajor axis 384,400 km | **61,524 km** = 35.41 R_Moon |
| Code | 60,000 km = 34.53 R_Moon |
| Perigee 363,300 km | 58,147 km |
| Apogee 405,500 km | 64,901 km |

60,000 km is the widely used round figure and sits inside the
perigee-apogee range, so I would call the value APPROX rather than
wrong. But it should say it is conventional.

The citation is the real problem, and it is **the same defect as the
Mars Hill sphere I flagged in the first worksheet**: "NASA Solar System
Dynamics (SSD)" does not publish Hill sphere radii. SSD publishes the
masses and orbital elements you compute one *from*. This is now the
third Hill sphere in the project citing SSD for a derived value it does
not carry.

**Recommended:** treat it as a class fix rather than three separate
ones. Every Hill sphere comment should name the inputs and the formula,
not a database that does not publish the output.

### F5 -- Mercury Hill sphere: the prompt's premise does not apply [LOW]

Item Me10 asks to verify the Mercury Hill sphere `radius_fraction`.
There isn't one. `mercury_visualization_shells.py` contains no
`radius_fraction` anywhere and no Hill sphere shell -- only
`mercury_hill_sphere_info` at line 400, which is qualitative text with
no numbers.

Nothing to check, and nothing wrong. If a numeric Hill sphere is ever
wanted there, the computation gives **220,603 km = 90.4 Mercury radii**
(mass 0.330e24 kg, a = 57.9e6 km).

---

## Verified worksheet (15 claims)

| # | Claim | Code value | Cited source | My value | Value correct? | Citation correct? |
|---|-------|-----------|--------------|----------|----------------|-------------------|
| M7 | Moon Hill sphere radius | ~60,000 km | NASA SSD | 61,524 km (semimajor); 58,147-64,901 km perigee-apogee | **APPROX** | **UNSOURCED** -- SSD does not publish Hill radii |
| M8 | Moon Hill in lunar radii | 34.53 | Derived: 60,000 / 1737.4 | 34.53 exactly (=59,992 km); 35.41 if based on 61,524 | **DERIVED -- verified** | Arithmetic closes; inherits M7's base |
| Er3 | Eris radius (citation only) | 1163 km | Sicardy et al. 2011 | 1163 +/- 6 km | **YES** | **YES** |
| Er4 | Eris density (citation only) | 2.52 g/cm^3 | Sicardy et al. 2011 | 2.52 +/- 0.05 g/cm^3 | **YES** | **YES** |
| Er1 | Eris bulk density (display) | ~2.5 g/cm^3 | Sicardy et al. 2011 | 2.52 | **YES** | **YES** |
| Er6 | Eris albedo | 0.96 | Sicardy et al. 2011 | ~0.96 visible geometric albedo | **YES** | **YES** |
| Er7 | Eris average orbital distance | ~67.8 AU | NASA SSD | 67.7 AU, from JPL SSD orbital period 557.56 y | **YES** | **YES** |
| Er9 | Eris perihelion distance | ~38 AU | NASA SSD | 37.97 AU = a(1-e) with e = 0.44 | **YES** | **YES** |
| Er8 | Hill sphere at average distance | ~9.4 Mkm (0.06 AU) | Derived from SSD | **14.27 Mkm (0.0954 AU)** | **NO** | Derivation does not close |
| Er10 | Hill sphere at perihelion | ~8.1 Mkm | Derived from SSD | 8.00 Mkm | **APPROX** | Shell geometry matches text |
| V17 | Venus Hill sphere | ~1 Mkm / ~167 R_V | NASA SSD; Venus Fact Sheet | 1,011,109 km = 167.1 R_V | **YES** | **UNSOURCED** for the Hill value; inputs are correct |
| V18 | Code 166 vs citation 167 | 166 | Verify derivation | **167** | **NO -- code is wrong** | Citation is right, code disagrees with it |
| P15 | Pluto Hill sphere | ~5.99 Mkm (0.04 AU) | NASA SSD | 5.981 Mkm (perihelion + Pluto-Charon system mass) | **YES -- but see F2** | **UNSOURCED**; convention undocumented |
| Me6 | Sodium tail in km | ~24 Mkm | Derived: 10,000 x 2440 km | 24.40 Mkm using the project's own 2439.7 km | **APPROX** | Derivation closes; rounds down |
| Me10 | Mercury Hill `radius_fraction` | -- | NASA SSD | No such value exists in the file | **N/A** | See F5 |

### One cross-check worth recording

Eris's radius and density are cited to Sicardy 2011 and its mass comes
from JPL SSD independently. Computing mass from Sicardy's radius and
density gives **1.660e22 kg**, against JPL's measured **1.66e22 kg**.

Two independent measurements closing to three digits is the strongest
result in this batch. Er1, Er3, and Er4 are as solid as anything in the
codebase.

---

## Not attempted (41 claims)

Listed so the gap is explicit rather than implied by absence. None of
these should be treated as passing.

**moon_visualization_shells.py:** M1 (inner core 240 km), M2 (inner core
1600-1700 K), M3 (outer core 330 km), M4 (partial melt 150 km), M5
(outer core 1300-1600 K), M6 (deep moonquakes 700-1200 km).
*Needs: Weber et al. 2011, Science.*

**eris_visualization_shells.py:** Er2 (rocky fraction >85%), Er5 (core
875 K), Er11 (Dysnomia at ~37,000 km).
*Needs: Glein et al. 2024; a source for Dysnomia's orbit. Note that Er2
is attributed to Sicardy 2011, which reports density, not composition --
a rocky mass fraction is an inference, and probably needs a different
citation or an explicit "inferred from density" label.*

**mercury_visualization_shells.py:** Me1 (outer core 1074 km), Me2
(crust ~35 km), Me3 (diamond layer), Me4 (exosphere composition), Me5
(sodium tail 10,000 R_M), Me7 (magnetopause 1.45 R_M), Me8 (tail base
2.7 R_M), Me9 (bow shock 1.96 R_M).
*Needs: Margot 2012, Sori 2018, Pei 2024, Winslow 2013, Potter & Morgan
1985.*

**venus_visualization_shells.py:** V6 (core ~3200 km), V7 (rotation 243
d), V8-V12 (atmospheric layer altitudes and temperatures), V13-V16
(magnetosphere geometry).
*Needs: Venus Express and Pioneer Venus results; Zhang 2007; Shan 2015.*

**pluto_visualization_shells.py:** P1-P3 (core), P4-P5 (mantle and
ocean), P6-P8 (surface), P9-P11 (haze), P12-P14 (upper atmosphere).
*Needs: Stern 2015, Bierson 2020, Gladstone 2016.*

---

## Two structural notes

**The Eris Hill sphere text is duplicated** at lines 465-467 and
481-483, exactly like the Venus atmosphere text in the Tier 1 batch. The
9.4 Mkm error is therefore in two places and both need the same fix.

**"Verified: April 2026 via Gemini fact-check" appears on several
blocks** whose numbers I have now found wrong -- the Eris Hill sphere
carries it. That annotation is doing the job a `# Cross-checked:` line
will do once Piece 2 lands, but without the structure: no worksheet
reference, no second checker, and no way to see what was actually
checked. The Eris block shows the cost. It reads as verified, and the
9.4 Mkm figure sitting inside it is off by a third.

Worth deciding whether those legacy "Verified:" lines get converted to
proper annotations, downgraded, or removed as this work proceeds.

---

## Tony-action rollup

- **(decide)** F1: correct Eris's 9.4 Mkm to **14.3 Mkm (0.095 AU)** in
  both copies, or drop the average-distance figure and keep only the
  perihelion one the shell actually uses.
- **(decide)** F2: set Pluto's `radius_fraction` to **5041** so the
  shell matches its caption, and document the perihelion +
  Pluto-Charon-system-mass convention.
- **(do)** F3: change Venus `radius_fraction` from 166 to **167**. The
  citation already says 167.
- **(decide)** F4: label the Moon's 60,000 km as a conventional round
  figure, and fix the SSD citation class-wide across Moon, Venus, Pluto,
  and Mars -- name the inputs and the formula, not a database that does
  not publish Hill radii.
- **(do)** Split the remaining 41 claims by source family so a checker
  can open the papers.
- **(decide)** What happens to the legacy "Verified: April 2026 via
  Gemini fact-check" lines.

---

*Worksheet prepared August 3, 2026 by Claude Opus 5, independently of
the GPT and Gemini legs. Computations use NASA NSSDCA fact-sheet masses
and orbital elements, JPL SSD dwarf-planet parameters, and a solar mass
derived from Kepler's third law applied to Mars's own orbit -- no
recalled constants.*
