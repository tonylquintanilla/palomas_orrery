<!-- Doc-Kind: hand | L-443 source check of 2026-10-22, a reader's results file saved word for word (non-ASCII letters written in ASCII). -->
# Orbit classes and shared centres -- source check

Checked 2026-10-22. Every page below was opened live with WebFetch in this run.
No repository file was edited.

## TASK 1: JPL orbit class (SBDB API)

Query form: https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=<designation> (spaces as %20).
Every one of the 51 queries returned a single object. None was ambiguous and none failed.
Values are object.fullname, object.orbit_class.code and object.orbit_class.name as returned.

| Queried | fullname | code | name |
|---|---|---|---|
| 1 | 1 Ceres (A801 AA) | MBA | Main-belt Asteroid |
| 136108 | 136108 Haumea (2003 EL61) | TNO | TransNeptunian Object |
| 136199 | 136199 Eris (2003 UB313) | TNO | TransNeptunian Object |
| 225088 | 225088 Gonggong (2007 OR10) | TNO | TransNeptunian Object |
| 136472 | 136472 Makemake (2005 FY9) | TNO | TransNeptunian Object |
| 90482 | 90482 Orcus (2004 DW) | TNO | TransNeptunian Object |
| 50000 | 50000 Quaoar (2002 LM60) | TNO | TransNeptunian Object |
| 90377 | 90377 Sedna (2003 VB12) | TNO | TransNeptunian Object |
| 2002 MS4 | 307261 Mani (2002 MS4) | TNO | TransNeptunian Object |
| 28978 | 28978 Ixion (2001 KX76) | TNO | TransNeptunian Object |
| 20000 | 20000 Varuna (2000 WR106) | TNO | TransNeptunian Object |
| 2004 GV9 | 90568 Goibniu (2004 GV9) | TNO | TransNeptunian Object |
| 2015 TG387 | 541132 Leleakuhonua (2015 TG387) | TNO | TransNeptunian Object |
| 2017 OF201 | (2017 OF201) | TNO | TransNeptunian Object |
| 2023 KQ14 | (2023 KQ14) | TNO | TransNeptunian Object |
| 486958 | 486958 Arrokoth (2014 MU69) | TNO | TransNeptunian Object |
| 10199 | 10199 Chariklo (1997 CU26) | CEN | Centaur |
| 4 | 4 Vesta (A807 FA) | MBA | Main-belt Asteroid |
| 16 | 16 Psyche (A852 FA) | MBA | Main-belt Asteroid |
| 21 | 21 Lutetia (A852 VA) | MBA | Main-belt Asteroid |
| 2867 | 2867 Steins (1969 VC) | MBA | Main-belt Asteroid |
| 52246 | 52246 Donaldjohanson (1981 EQ5) | MBA | Main-belt Asteroid |
| 152830 | 152830 Dinkinesh (1999 VD57) | MBA | Main-belt Asteroid |
| 433 | 433 Eros (A898 PA) | AMO | Amor |
| 101955 | 101955 Bennu (1999 RQ36) | APO | Apollo |
| 162173 | 162173 Ryugu (1999 JU3) | APO | Apollo |
| 25143 | 25143 Itokawa (1998 SF36) | APO | Apollo |
| 469219 | 469219 Kamo`oalewa (2016 HO3) | APO | Apollo |
| 2025 PN7 | (2025 PN7) | APO | Apollo |
| 2024 PT5 | (2024 PT5) | APO | Apollo |
| 2025 PY1 | (2025 PY1) | APO | Apollo |
| 2023 JF | (2023 JF) | APO | Apollo |
| 2024 DW | (2024 DW) | APO | Apollo |
| 2024 YR4 | (2024 YR4) | APO | Apollo |
| 3548 | 3548 Eurybates (1973 SO) | TJN | Jupiter Trojan |
| 617 | 617 Patroclus (A906 UL) | TJN | Jupiter Trojan |
| 15094 | 15094 Polymele (1999 WB2) | TJN | Jupiter Trojan |
| 11351 | 11351 Leucus (1997 TS25) | TJN | Jupiter Trojan |
| 21900 | 21900 Orus (1999 VQ10) | TJN | Jupiter Trojan |
| 10P | 10P/Tempel 2 | JFc | Jupiter-family Comet |
| 24P | 24P/Schaumasse | JFc | Jupiter-family Comet |
| 88P | 88P/Howell | JFc | Jupiter-family Comet |
| 67P | 67P/Churyumov-Gerasimenko | JFc | Jupiter-family Comet |
| C/1995 O1 | C/1995 O1 (Hale-Bopp) | COM | Comet |
| C/1996 B2 | C/1996 B2 (Hyakutake) | COM | Comet |
| C/1965 S1-A | C/1965 S1-A (Ikeya-Seki) | COM | Comet |
| C/2020 F3 | C/2020 F3 (NEOWISE) | COM | Comet |
| C/2025 A6 | C/2025 A6 (Lemmon) | COM | Comet |
| C/2025 R2 | C/2025 R2 (SWAN) | COM | Comet |
| C/2026 A1 | C/2026 A1 (MAPS) | COM | Comet |
| C/2024 E1 | C/2024 E1 (Wierzchos) | HYP | Hyperbolic Comet |

Counts by code (51 bodies): TNO 15 (Haumea, Eris, Gonggong, Makemake, Orcus,
Quaoar, Sedna, Mani, Ixion, Varuna, Goibniu/2004 GV9, Leleakuhonua, 2017 OF201,
2023 KQ14, Arrokoth); APO 10 (Bennu, Ryugu, Itokawa, Kamo`oalewa, 2025 PN7,
2024 PT5, 2025 PY1, 2023 JF, 2024 DW, 2024 YR4); MBA 7 (Ceres, Vesta, Psyche,
Lutetia, Steins, Donaldjohanson, Dinkinesh); COM 7 (Hale-Bopp, Hyakutake,
Ikeya-Seki, NEOWISE, Lemmon, SWAN, MAPS); TJN 5 (Eurybates, Patroclus,
Polymele, Leucus, Orus); JFc 4 (10P, 24P, 88P, 67P); CEN 1 (Chariklo);
AMO 1 (Eros); HYP 1 (C/2024 E1).

Notes worth knowing:
- 2004 GV9 now carries a number and name in SBDB: 90568 Goibniu.
- Mani's number is 307261 (SBDB fullname "307261 Mani (2002 MS4)").
- SBDB writes Kamo`oalewa with a backtick for the okina.
- Ceres is classed MBA, not as a dwarf planet; SBDB has no dwarf-planet class.
- A comet's class can change when JPL refits its orbit (COM vs HYP turns on
  whether the fitted eccentricity is below or above 1). These are today's values.

## TASK 2: shared centres (barycentre outside or inside the larger body)

Formula: d = a * m2/(m1+m2). With a mass ratio q = m2/m1, m2/(m1+m2) = q/(1+q).
OUTSIDE when d > R (larger body's radius). For each pair the threshold is also
given: the mass fraction needed for OUTSIDE is R/a.

### Orcus - Vanth: OUTSIDE

- Mass ratio: 0.16 +/- 0.02. Page: https://arxiv.org/abs/2307.04848, "Masses and
  densities of dwarf planet satellites measured with ALMA" (Brown & Butler 2023).
  Quote: "From the Vanth-Orcus barycentric motion, we find a Vanth-Orcus mass ratio
  of 0.16+/-0.02" "the highest of any known planet or dwarf planet."
- Separation: 9030 +/- 89 km. Page: https://arxiv.org/pdf/1108.5963, "Integral-field
  spectroscopy of (90482) Orcus-Vanth" (Carry et al. 2011). Table 5: "a | 9 030 | 89 |
  km | Semi-major axis".
- Orcus radius: 455 km (half of 910). Page: https://arxiv.org/pdf/1801.07221,
  "Medium-sized satellites of large Kuiper belt objects" (Brown & Butler 2018):
  "We find that Orcus has a diameter of 910^{+50}_{-40} km".
- Arithmetic: 0.16/1.16 = 0.1379; 9030 x 0.1379 = 1246 km. 1246 > 455.
  Across the ratio's range (0.14 to 0.18): 1109 to 1377 km. OUTSIDE at every value,
  about 2.7 Orcus radii from Orcus's centre. Cross-check inside the same 2023
  paper: it states Vanth orbits at "a/R_p ~ 20"; 20 x 0.138 = 2.8 radii.

### Patroclus - Menoetius: OUTSIDE

- Mass share: Menoetius about 22 percent of system mass, which the authors ASSUMED,
  not measured. Page: https://doaj.org/article/4a8ba688bb59407fb3bde26dbf0847d4,
  "Orbit of the Patroclus-Menoetius Binary System and Predictions for the 2024/2025
  Mutual Events Season" (Brozovic et al. 2024, AJ 167, 104). Quote: "we assumed that
  Menoetius contained ~22% of the system's mass." (The publisher's full text at
  doi.org/10.3847/1538-3881/ad1f6e refused the fetch: robots_disallowed.)
- Separation: same page: "The mean osculating semimajor axis is a = 692.5 +/- 4.0 km".
  Also https://arxiv.org/pdf/1903.03729, "The Upcoming Mutual Event Season for the
  Patroclus - Menoetius Trojan Binary" (Grundy et al. 2019), Table 2: "Semimajor axis
  (km) | 688.5 +/- 4.7".
- Patroclus radius: same 2019 paper, citing Buie et al. 2015: "Buie et al. (2015)
  estimated the b axis radii as 59 and 54 km, for Patroclus and Menoetius,
  respectively"; polar radius "A circle of radius 49 km, representing Patroclus".
- Arithmetic: 692.5 x 0.22 = 152 km. 152 > 59. OUTSIDE.
  The verdict does not depend on the assumed 22 percent: OUTSIDE needs only a share
  above 59/692.5 = 0.085, i.e. Menoetius above 8.5 percent of the system's mass,
  for two bodies whose radii (59 and 54 km) are nearly equal. NOTE: no measured
  individual masses were found in an open source.

### Eris - Dysnomia: INSIDE

- Mass ratio: upper limit only. Page: https://arxiv.org/abs/2307.04848, "Masses and
  densities of dwarf planet satellites measured with ALMA". Quote: "We find only an
  upper limit of the barycenter motion of Eris, which implies a one sigma upper
  limit" "to the Dysnomia-Eris mass ratio of 0.0085". (The body gives 0.0084 in
  Section 2.2; mass limit "1.4 x 10^20 kg" against a system mass "1.65x10^22 kg
  (Holler et al. 2021)".)
- Separation: 37460 +/- 80 km. Page: https://arxiv.org/pdf/1801.07221, "Medium-sized
  satellites of large Kuiper belt objects", Table 3: "semimajor axis | 37460 +/- 80 | km".
- Eris radius: 1163 km. Same 2018 page: "We assume the occultation-derived circular
  diameter of Eris of 2326+/-12 km (Sicardy 2011)". (The 2023 paper's text was read
  back to me as "diameter 1163 km (Sicardy 2011)"; 1163 is the radius. Either the
  paper or the reader slipped; the 2018 sentence is unambiguous.)
- Arithmetic: 0.0085/1.0085 = 0.00843; 37460 x 0.00843 = 316 km at most. 316 < 1163.
  INSIDE. OUTSIDE would need a ratio above 0.032 (1163/37460 = 0.031 as a share),
  nearly four times the one-sigma limit. The verdict holds on an upper limit.

### Haumea with Hi'iaka and Namaka: INSIDE (both)

- Mass ratios: Page: https://arxiv.org/pdf/0903.4213, "Orbits and Masses of the
  Satellites of the Dwarf Planet Haumea = 2003 EL61" (Ragozzine & Brown 2009).
  Quote: "The mass ratios of the satellite to Haumea are 0.00451 +/-0.00030 and
  0.00051 +/- 0.00036, respectively" (Hi'iaka, then Namaka). Namaka's mass is only
  marginally detected (1.2 sigma), and the authors say both may be overestimated.
- Separations: same page, Table 2: Hi'iaka "Semi-major axis | 49880 | +/- | 198 | km";
  Namaka "Semi-major axis | 25657 | +/- | 91 | km".
- Haumea size (elongated): Page: https://arxiv.org/abs/2006.03113, "The size, shape,
  density and ring of the dwarf planet Haumea from a stellar occultation" (Ortiz et
  al. 2017). Quotes: "The occultation by the main body provides an instantaneous
  elliptical limb with axes 1,704 +/- 4 km x 1,138 +/- 26 km." and "Haumea's largest axis
  is at least 2,322 +/- 60 km". So the largest semi-axis is at least 1161 km and the
  projected short semi-axis is 569 km. The true shortest semi-axis is NOT FOUND on
  the opened page (it is at most the projected 569 km).
- Arithmetic: Hi'iaka 0.00451/1.00451 = 0.00449; 49880 x 0.00449 = 224 km.
  Namaka 0.00051/1.00051 = 0.00051; 25657 x 0.00051 = 13 km.
  Both are far below 569 km, the smallest dimension found. INSIDE for each.
  Even the two offsets added together (237 km) stay inside. The missing true short
  axis does not threaten the verdict unless it were below 237 km, which the
  projected 1,138 km limb chord does not suggest.

### Makemake - MK2 (S/2015 (136472) 1): INSIDE (inferred; mass NOT FOUND)

- Mass ratio: NOT FOUND. No open source gives MK2's mass. Page:
  https://arxiv.org/html/2509.05880v3, "A preliminary orbit for the satellite of dwarf
  planet (136472) Makemake" (Bamberger 2025) gives only a combined mass, assuming
  "the entire mass of the system is concentrated in the primary".
- Separation: same page: "semi-major axis 22250 +/- 780 km". (Parker et al. 2016,
  https://arxiv.org/abs/1604.07461, allowed "semi-major axes in 21,100 km ? a ?
  300,000 km"; the fetch did not return a printed title; the search listing names it
  "Discovery of a Makemakean Moon".)
- Makemake radius: Bamberger page: "Assuming a radius of 715 +/- 15 km for Makemake"
  (citing M. Brown 2013).
- MK2 size: Parker et al. 2016: "S/2015 (136472) 1 would have a diameter of 175 km"
  (assuming a 4 percent albedo), and it "is 7.80+/-0.04 magnitudes fainter than
  Makemake".
- Threshold: OUTSIDE needs MK2 above 715/22250 = 3.2 percent of the system's mass.
  Inference, not a measurement: at equal density a 175 km moon against a 1430 km
  primary is (175/1430)^3 = 0.18 percent, giving a centre about 41 km from
  Makemake's centre. MK2 would need about 17 times Makemake's density to reach
  3.2 percent. The verdict INSIDE holds on size, not on a measured mass.

### Gonggong - Xiangliu: INSIDE (on a dynamical upper bound; mass NOT FOUND as a measurement)

- Mass ratio: not measured; bounded by dynamics. Page: https://arxiv.org/pdf/1903.05439,
  "The mass and density of the dwarf planet (225088) 2007 OR10" (Kiss et al. 2019).
  Quotes: "The only configurations that fulfill this requirement are those for which
  q <4x10-4 or RS = 18-50 km"; conclusion: "a small satellite (Rs < 50 km) with a
  relatively bright surface (pV > 0.2)"; and "An even smaller satellite, with a mass
  ratio of q <= 5x10-3". q is the satellite-to-primary mass ratio (Figure 3 caption:
  "satellite to primary mass ratio (q)"; one passage words it the other way round).
  The paper never uses the name Xiangliu.
- Separation: same page, Table 2: "a (km) 24021+/-202 24274+/-193" (prograde and
  retrograde solutions).
- Gonggong radius: 615 km. Abstract, https://arxiv.org/abs/1903.05439: "Assuming a
  spherical shape for the primary this approach provides a size of 1230+/-50 km".
- Arithmetic: q < 4e-4 gives 24021 x 0.0004 = 9.6 km. The looser q <= 5e-3 gives
  24021 x 0.005 = 120 km. Both far below 615. INSIDE. OUTSIDE would need a share above
  615/24021 = 0.026, five times the loosest bound in the paper.

### Quaoar - Weywot: INSIDE

- Masses: Page: https://arxiv.org/abs/2511.07351, "Beyond Point Masses. V. Weywot's
  Non-Keplerian Orbit" (abstract opened there; numbers from
  https://arxiv.org/pdf/2511.07351). Table 2, constrained fit: Quaoar
  "1212.27^{+5.39}_{-5.39}" and Weywot "2.4^{+1.2}_{-1.1}" (units 10^18 kg). Caution:
  Weywot's mass is essentially its prior ("with mean of 2.4 x 10^18 kg and standard
  deviation of 1.2 x 10^18 kg"), set from a 165 km diameter in an unpublished paper
  (Fernandez-Valenzuela, in prep.) and an assumed density; it is not an independent
  measurement.
- Separation: same paper, Table 2: "13329_{-19}^{+19}" km. (Older: Fraser et al.
  2013, https://arxiv.org/pdf/1211.1016, "The Mass, Orbit, and Tidal Evolution of the
  Quaoar-Weywot System", Table 2: "Semi-major Axis (10^4 km) | 1.31 +/- 0.02 | 1.35 +/-
  0.02 | 1.39 +/- 0.02 | 1.45+/-0.02".)
- Quaoar radius: same 2025 paper: "a volumetric radius of 548.8+/-1.1 km" (citing
  Margoti et al. 2024).
- Arithmetic: 2.4/(1212.27+2.4) = 0.00198; 13329 x 0.00198 = 26 km. 26 < 549. INSIDE.
  OUTSIDE needs a share above 549/13329 = 4.1 percent; even three times the prior
  mass (7.2e18 kg) gives 0.6 percent. Fraser 2013's "size ratios of <~5 %" points the
  same way.

## Verdict summary

Orcus-Vanth OUTSIDE; Patroclus-Menoetius OUTSIDE; Eris-Dysnomia INSIDE;
Haumea-Hi'iaka INSIDE; Haumea-Namaka INSIDE; Makemake-MK2 INSIDE (inferred from
size, mass not found); Gonggong-Xiangliu INSIDE (on the paper's dynamical bound);
Quaoar-Weywot INSIDE (Weywot mass prior-dominated).

Pages opened: 51 SBDB API queries (ssd-api.jpl.nasa.gov/sbdb.api, listed in the
Task 1 table); arxiv.org/abs/2307.04848; arxiv.org/pdf/2307.04848;
arxiv.org/abs/1801.07221; arxiv.org/pdf/1801.07221; arxiv.org/abs/1108.5963;
aanda.org/articles/aa/full_html/2011/10/aa17486-11 (no figures returned);
arxiv.org/pdf/1108.5963; doaj.org/article/4a8ba688bb59407fb3bde26dbf0847d4;
arxiv.org/pdf/1903.03729; doi.org/10.3847/1538-3881/ad1f6e (FAILED,
robots_disallowed); arxiv.org/abs/0903.4213; arxiv.org/pdf/0903.4213;
arxiv.org/abs/2006.03113; arxiv.org/html/2509.05880v3; arxiv.org/abs/1604.07461;
arxiv.org/abs/1903.05439; arxiv.org/pdf/1903.05439; arxiv.org/pdf/1211.1016;
arxiv.org/abs/2511.07351; arxiv.org/pdf/2511.07351.
