<!-- Doc-Kind: hand | L-443 class check of 2026-10-26: every body in the Solar System room's drawer groups, and the fourteen open-path comets, against JPL's Small-Body Database orbit class, read live; the mismatches named. -->
# The drawer's groups against JPL's classes

Tony Quintanilla, PE | Claude Opus 5.5 | October 26, 2026

Built on orrery 5398439591f35979c4df1791e25477ac37119b01 at
https://github.com/tonylquintanilla/palomas_orrery (branch main) and
gallery 9223cd165422bf2616715e65ca59410b8245f9e5 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch main),
whose `data/objects_config.json` (the room's `drawer.rows`) gives the
groups and their bodies.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: CHECK (zero code). Asked for by your ruling of Oct 24, 23:27
(`COORD_L443_drawer_groups_ruling_20261024.md`): "let's follow the jpl
classification for our groupings. this would also apply to minor
planets."

## How it was read

- JPL's Small-Body Database API,
  `https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=<designation>`, one body
  per fetch, on 2026-10-26, by a helper Claude session of this one,
  through the web fetch tool (the sandbox's own route to JPL is
  blocked). Each row is JPL's `object.fullname` and
  `object.orbit_class` as returned.
- 67 bodies: 53 in the drawer's six groups today, and the fourteen
  open-path comets. No fetch failed. C/2025 K1 by its designation
  matched four objects (the comet and its pieces), so it was asked again
  by JPL's number for it, 1004075, which returned the comet alone.
- One caution about the route. For C/2025 N1 (3I/ATLAS) the plain
  address returned JPL's orbit of 2026-02-19, while the same query with
  `full-prec=1` returned the orbit of 2026-10-21: something between the
  fetch tool and JPL kept an old copy. The class is the same in both.
  Eleven of the newer bodies were re-read the second way and agreed.
  The other 42 rows of the groups come from the plain address only;
  their classes match the reads of Oct 22
  (`CHECK_L443_classes_pairs_20261022.md`) wherever both exist.

## What the check found

**No body sits in the wrong group.** Every body in Main asteroid belt,
Jupiter Trojans, Centaurs and Trans-Neptunian objects carries that
group's one class.

**Two groups gather more than one of JPL's classes:**

- **Comets**, four classes: Halley-type (HTC) Halley; Encke-type (ETc)
  Encke; Jupiter-family (JFc) Tempel 2, Schaumasse,
  Churyumov-Gerasimenko, Howell; Comet (COM) Ikeya-Seki, Hale-Bopp,
  Hyakutake, NEOWISE, Lemmon, SWAN, MAPS. Piece C of C/2025 K1 (COM)
  joins it.
- **Near-Earth asteroids**, three classes: Aten (ATE) Apophis; Amor
  (AMO) Eros; Apollo (APO) Bennu, Ryugu, Itokawa, Kamo`oalewa, 2025 PN7,
  2024 PT5, 2025 PY1, 2023 JF, 2024 DW, 2024 YR4. None is an Atira.

**The new groups hold:** Hyperbolic comets, ten, all HYP. Interstellar
objects: 2I/Borisov and 3I/ATLAS HYP, 'Oumuamua HYA ("Hyperbolic
Asteroid"), grouped by the IAU's "I" numbers as ruled.

**Found in passing, for the skill's next version:**
interactive-exhibit 1.25 lists the drawer's classes as "TNO, MBA, APO
and AMO, TJN, CEN, JFc and COM". JPL also gives HTC (Halley), ETc
(Encke) and ATE (Apophis). The sentence is a description that has gone
out of date; no step follows it, so it is carried to the next bump, not
bumped now.

## The decision that is yours

Whether a group that gathers several of JPL's classes stays one row,
or splits into a row per class. It now applies to two groups, not only
Near-Earth asteroids:

- Comets would become up to four rows (Halley-type 1, Encke-type 1,
  Jupiter-family 4, Comet 8).
- Near-Earth asteroids would become three (Aten 1, Amor 1, Apollo 10).

## Group A: the drawer's six groups (53)

| Group | Query | JPL's full name | Class | JPL's name for the class |
|---|---|---|---|---|
| Comets | 1P | 1P/Halley | HTC | Halley-type Comet* |
| Comets | 2P | 2P/Encke | ETc | Encke-type Comet |
| Comets | 10P | 10P/Tempel 2 | JFc | Jupiter-family Comet |
| Comets | 24P | 24P/Schaumasse | JFc | Jupiter-family Comet |
| Comets | C/1965 S1-A | C/1965 S1-A (Ikeya-Seki) | COM | Comet |
| Comets | 67P | 67P/Churyumov-Gerasimenko | JFc | Jupiter-family Comet |
| Comets | 88P | 88P/Howell | JFc | Jupiter-family Comet |
| Comets | C/1995 O1 | C/1995 O1 (Hale-Bopp) | COM | Comet |
| Comets | C/1996 B2 | C/1996 B2 (Hyakutake) | COM | Comet |
| Comets | C/2020 F3 | C/2020 F3 (NEOWISE) | COM | Comet |
| Comets | C/2025 A6 | C/2025 A6 (Lemmon) | COM | Comet |
| Comets | C/2025 R2 | C/2025 R2 (SWAN) | COM | Comet |
| Comets | C/2026 A1 | C/2026 A1 (MAPS) | COM | Comet |
| Near-Earth asteroids | 99942 | 99942 Apophis (2004 MN4) | ATE | Aten |
| Near-Earth asteroids | 433 | 433 Eros (A898 PA) | AMO | Amor |
| Near-Earth asteroids | 101955 | 101955 Bennu (1999 RQ36) | APO | Apollo |
| Near-Earth asteroids | 162173 | 162173 Ryugu (1999 JU3) | APO | Apollo |
| Near-Earth asteroids | 25143 | 25143 Itokawa (1998 SF36) | APO | Apollo |
| Near-Earth asteroids | 469219 | 469219 Kamo`oalewa (2016 HO3) | APO | Apollo |
| Near-Earth asteroids | 2025 PN7 | (2025 PN7) | APO | Apollo |
| Near-Earth asteroids | 2024 PT5 | (2024 PT5) | APO | Apollo |
| Near-Earth asteroids | 2025 PY1 | (2025 PY1) | APO | Apollo |
| Near-Earth asteroids | 2023 JF | (2023 JF) | APO | Apollo |
| Near-Earth asteroids | 2024 DW | (2024 DW) | APO | Apollo |
| Near-Earth asteroids | 2024 YR4 | (2024 YR4) | APO | Apollo |
| Main asteroid belt | 1 | 1 Ceres (A801 AA) | MBA | Main-belt Asteroid |
| Main asteroid belt | 4 | 4 Vesta (A807 FA) | MBA | Main-belt Asteroid |
| Main asteroid belt | 16 | 16 Psyche (A852 FA) | MBA | Main-belt Asteroid |
| Main asteroid belt | 21 | 21 Lutetia (A852 VA) | MBA | Main-belt Asteroid |
| Main asteroid belt | 2867 | 2867 Steins (1969 VC) | MBA | Main-belt Asteroid |
| Main asteroid belt | 52246 | 52246 Donaldjohanson (1981 EQ5) | MBA | Main-belt Asteroid |
| Main asteroid belt | 152830 | 152830 Dinkinesh (1999 VD57) | MBA | Main-belt Asteroid |
| Jupiter Trojans | 3548 | 3548 Eurybates (1973 SO) | TJN | Jupiter Trojan |
| Jupiter Trojans | 617 | 617 Patroclus (A906 UL) | TJN | Jupiter Trojan |
| Jupiter Trojans | 15094 | 15094 Polymele (1999 WB2) | TJN | Jupiter Trojan |
| Jupiter Trojans | 11351 | 11351 Leucus (1997 TS25) | TJN | Jupiter Trojan |
| Jupiter Trojans | 21900 | 21900 Orus (1999 VQ10) | TJN | Jupiter Trojan |
| Centaurs | 10199 | 10199 Chariklo (1997 CU26) | CEN | Centaur |
| Trans-Neptunian objects | 90482 | 90482 Orcus (2004 DW) | TNO | TransNeptunian Object |
| Trans-Neptunian objects | 136108 | 136108 Haumea (2003 EL61) | TNO | TransNeptunian Object |
| Trans-Neptunian objects | 136199 | 136199 Eris (2003 UB313) | TNO | TransNeptunian Object |
| Trans-Neptunian objects | 136472 | 136472 Makemake (2005 FY9) | TNO | TransNeptunian Object |
| Trans-Neptunian objects | 225088 | 225088 Gonggong (2007 OR10) | TNO | TransNeptunian Object |
| Trans-Neptunian objects | 50000 | 50000 Quaoar (2002 LM60) | TNO | TransNeptunian Object |
| Trans-Neptunian objects | 90377 | 90377 Sedna (2003 VB12) | TNO | TransNeptunian Object |
| Trans-Neptunian objects | 2002 MS4 | 307261 Mani (2002 MS4) | TNO | TransNeptunian Object |
| Trans-Neptunian objects | 28978 | 28978 Ixion (2001 KX76) | TNO | TransNeptunian Object |
| Trans-Neptunian objects | 20000 | 20000 Varuna (2000 WR106) | TNO | TransNeptunian Object |
| Trans-Neptunian objects | 2004 GV9 | 90568 Goibniu (2004 GV9) | TNO | TransNeptunian Object |
| Trans-Neptunian objects | 2015 TG387 | 541132 Leleakuhonua (2015 TG387) | TNO | TransNeptunian Object |
| Trans-Neptunian objects | 2017 OF201 | (2017 OF201) | TNO | TransNeptunian Object |
| Trans-Neptunian objects | 2023 KQ14 | (2023 KQ14) | TNO | TransNeptunian Object |
| Trans-Neptunian objects | 486958 | 486958 Arrokoth (2014 MU69) | TNO | TransNeptunian Object |

JPL's own asterisk on "Halley-type Comet*" is copied as returned.

## Group B: the fourteen open-path comets

Eccentricity (e) as JPL gives it at full precision (`full-prec=1`),
with its 1-sigma uncertainty. Above 1 is an open path.

| Query | JPL's full name | Class | JPL's name for the class | e | e, 1 sigma |
|---|---|---|---|---|---|
| C/2023 A3 | C/2023 A3 (Tsuchinshan-ATLAS) | HYP | Hyperbolic Comet | 1.000095368540586 | 2.2442E-7 |
| C/2024 G3 | C/2024 G3 (ATLAS) | HYP | Hyperbolic Comet | 1.000012291218472 | 3.9817E-7 |
| C/1975 V1-A | C/1975 V1-A (West) | HYP | Hyperbolic Comet | 1.000016087612074 | 5.6629E-6 |
| C/2006 P1 | C/2006 P1 (McNaught) | HYP | Hyperbolic Comet | 1.000018815882278 | 1.01E-6 |
| 1004075 | C/2025 K1 (ATLAS) | HYP | Hyperbolic Comet | 1.000257251473882 | 1.2714E-6 |
| C/2025 K1-B | C/2025 K1-B (ATLAS) | HYP | Hyperbolic Comet | 1.002033474126155 | 7.8776E-5 |
| C/2025 K1-C | C/2025 K1-C (ATLAS) | COM | Comet | .9999940934318799 | 3.1095E-5 |
| C/2025 K1-D | C/2025 K1-D (ATLAS) | HYP | Hyperbolic Comet | 1.002459703720921 | .00015466 |
| C/2025 R3 | C/2025 R3 (PANSTARRS) | HYP | Hyperbolic Comet | 1.000350131023512 | 6.2319E-7 |
| C/2025 V1 | C/2025 V1 (Borisov) | HYP | Hyperbolic Comet | 1.007732231432179 | .0014673 |
| A/2017 U1 | 'Oumuamua (A/2017 U1) | HYA | Hyperbolic Asteroid | 1.201133796102373 | 2.1064E-5 |
| C/2019 Q4 | C/2019 Q4 (Borisov) | HYP | Hyperbolic Comet | 3.356475782676596 | 1.9039E-5 |
| C/2025 N1 | C/2025 N1 (ATLAS) | HYP | Hyperbolic Comet | 6.123467394525528 | 4.3958E-5 |
| C/2024 E1 | C/2024 E1 (Wierzchos) | HYP | Hyperbolic Comet | 1.00005833991638 | 6.798E-7 |

Piece C's e falls short of 1 by about 0.000006, five times smaller
than its own uncertainty: JPL's numbers cannot yet tell a closed path
from an open one, as its words say.

## Tony-action rollup

- **(do)** Commit this file with your next orrery push.
- **(decide)** Whether Comets and Near-Earth asteroids each stay one
  row, or split by JPL's class.

Written October 26, 2026 with Anthropic's Claude Opus 5.5.
