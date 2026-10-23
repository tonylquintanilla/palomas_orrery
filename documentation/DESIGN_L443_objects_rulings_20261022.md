<!-- Doc-Kind: hand | Design record for L-443, slice 1 of the orrery's objects on the website: Tony's rulings of 2026-10-22 in his words, the mock-up chosen, the measurement, the counts, the shared-centre pairs with their sources, and what the checks found. -->
# Design record: the orrery's objects come to the website, slice 1 (L-443, October 22, 2026)

Built on bfb6c474 at https://github.com/tonylquintanilla/palomas_orrery
and 0bb34344 at https://github.com/tonylquintanilla/tonyquintanilla.github.io
(branch main of each). Pushed at: (Tony's pushes, after the handoff's
run order).

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: DESIGN SESSION record, with the slice built in the same session.
Written October 22, 2026 by Anthropic's Claude Opus 5.5, from the brief
`HANDOFF_L443_objects_design_brief_rev2_20261022.md` (Claude Fable 5.1,
revision 2 of `HANDOFF_L438_objects_to_website_brief_20261013.md`).
Companion: `HANDOFF_L443_slice1_build_20261022.md`.

## 1. Tony's rulings, in his words

- **The drawer (question 1), at the mock-up** (the canvas "Solar System
  drawer options", two phone screens: A, groups are rooms, as the
  front-door design of 2026-09-29 wrote it; B, groups fold open): "B.
  this is the right view. the "room" would only apply if the object
  has additional features beyond the symbol such as future moon shells,
  or spacecraft encounters, or comet perihelion encounters, or asteroid
  near earth encounters, etc. another group not shown that could be
  added is the main asteroid belt." The main belt was in B, behind See
  more; recorded as a group row now, and a drawn belt cloud as later.
  This supersedes the 2026-09-29 line "Notables appear only in the
  group room, never under the group row in the solar system drawer".
- **The nightly cost (question 2)**, asked whether to fetch every body
  on every build: "yes".
- **The split (question 3)**, asked whether slice 1 is the 51 bodies
  the website can draw now, with the 13 comets on open paths going with
  the spacecraft: "Yes. Confirmed as recommended". (Wierzchos then
  moved with them, on JPL's own class; 50 bodies.)
- **The words list**: "Confirmed". Then, asked two of its four
  questions again: the three comet pins, "Re-pin to the newest
  (Recommended)"; Ikeya-Seki's link, "[No preference]", so the
  one-link rule decides it: Wikipedia.
- **The comets' anchor**, asked whether to draw every comet from its
  elements of today, Halley and Encke too: "Yes".

## 2. Measured

- **The dictionary at bfb6c474**: 183 entries -- orbital 67, satellite
  46, trajectory 38 (13 of them comets), exoplanet 11, lagrange_point
  10, barycenter 4, exo_host_star 2, exo_binary_star 2, fixed 1,
  hypothetical 1, exo_barycenter 1. The brief's 71, 47 and 6 were not
  what the file holds.
- **Slice 1, counted: 50 bodies**, by JPL's orbit class (SBDB):
  - comets, 11: Tempel 2, Schaumasse, Ikeya-Seki,
    Churyumov-Gerasimenko, Howell, Hale-Bopp, Hyakutake, NEOWISE,
    Lemmon, SWAN, MAPS (JFc 4, COM 7);
  - near-Earth asteroids, 11: Eros (AMO), Bennu, Ryugu, Itokawa,
    Kamo'oalewa, 2025 PN7, 2024 PT5, 2025 PY1, 2023 JF, 2024 DW,
    2024 YR4 (APO);
  - main belt, 7: Ceres, Vesta, 16 Psyche, Lutetia, Steins,
    Donaldjohanson, Dinkinesh (MBA);
  - Jupiter Trojans, 5: Eurybates, Patroclus and Menoetius, Polymele,
    Leucus, Orus (TJN);
  - centaurs, 1: Chariklo (CEN);
  - trans-Neptunian objects, 15: Orcus, Haumea, Eris, Makemake,
    Gonggong, Quaoar, Sedna, Mani, Ixion, Varuna, Goibniu (2004 GV9),
    Leleakuhonua, 2017 OF201, 2023 KQ14 (Ammonite), Arrokoth (TNO).
- **To the spacecraft slice, 14 comets on open or barely closed
  paths**: Tsuchinshan, ATLAS (C/2024 G3), West, McNaught, C/2025 K1
  and fragments B, C, D, PANSTARRS (C/2025 R3), Borisov (C/2025 V1),
  1I/Oumuamua, 2I/Borisov, 3I/ATLAS, and Wierzchos, which JPL classes
  hyperbolic (HYP). The website's orbit drawing
  (render_orbits.solve_kepler, sweep_conic) is elliptic only; the
  existing machinery for a path of positions is the spacecraft arc.
- **Left out, recorded on L-470**: 6AC4721, an entry whose id is
  "none" and whose link is MAPS's page -- MAPS under its temporary
  name; Planet 9 (no Horizons id); Patroclus and Menoetius as separate
  bodies, and the moons (slice 3).
- **The nightly cost**: the day's first build of 19 objects took 20 to
  34 seconds (run records of 2026-10-19 to 10-22), later builds the
  same day 2 to 4. About 1 to 2 seconds a body, so slice 1 adds one to
  two minutes. The first real build confirms it.
- **Descriptions with numbers**: 33 of the 50 carried a number that is
  a claim. Each was read against a page opened on 2026-10-22, or came
  out; the words list Tony approved is
  `WORDS_L443_slice1_20261022.md`.

## 3. The shared centres (the Barycenter Rule)

The centre two bodies orbit together is drawn, and the symbol's words
say so, only when it lies outside the bigger body. Distance from the
bigger body's centre = separation x m2/(m1+m2). All figures from open
pages opened on 2026-10-22; the quotes are in
`CHECK_L443_classes_pairs_20261022.md`.

| Pair | Mass ratio or share | Separation | Bigger body's radius | Centre | Verdict |
|---|---|---|---|---|---|
| Orcus-Vanth | 0.16 +/- 0.02 (Brown and Butler 2023, arXiv 2307.04848) | 9,030 km (Carry et al. 2011, arXiv 1108.5963) | 455 km (Brown and Butler 2018, arXiv 1801.07221) | about 1,246 km | OUTSIDE |
| Patroclus-Menoetius | Menoetius about 22% of the mass, assumed by the authors (Brozovic et al. 2024, AJ 167, 104, DOAJ abstract) | 692.5 km (same) | 59 km (Buie et al. 2015, via Grundy et al. 2019, arXiv 1903.03729) | about 152 km | OUTSIDE (any share over 8.5%) |
| Eris-Dysnomia | under 0.0085, one sigma (Brown and Butler 2023) | 37,460 km (Brown and Butler 2018) | 1,163 km | at most 316 km | INSIDE |
| Haumea with Hi'iaka, Namaka | Ragozzine and Brown 2009, arXiv 0903.4213 | -- | -- | about 224 km and 13 km | INSIDE |
| Makemake-MK2 | no measured mass found | 22,250 km | 715 km | needs a 3.2% share; at equal density MK2 holds about 0.18% | INSIDE, inferred from size |
| Gonggong-Xiangliu | under 0.0004 (dynamical limit) | -- | 615 km | 10 to 120 km | INSIDE |
| Quaoar-Weywot | Weywot's mass mostly an assumption | -- | 549 km | about 26 km | INSIDE |

So Orcus and Patroclus carry Pluto's kind of sentence on their drawer
rows; the other five are drawn as the body, with no sentence.

**Which record serves each.** A body with a 'helio_id' is served by it,
as a small body: rule 3 of the brief ("Agreed as settled"). JPL's Lookup
names every one of these records "integrated barycenter": the
small-body solution already follows the pair's shared centre. Orcus and
Patroclus are served by 2004 DW and A906 UL for that reason, and
because their system-barycentre numbers (20090482, 20000617) are found
in both of JPL's indexes, which the Horizons check reads as a wrong
id_type.

## 4. What the checks found (five readers, 2026-10-22)

Every page was opened live; the results files, word for word, are
saved beside this record:

- `CHECK_L443_tno_20261022.md` -- the dwarf planets and the rest
  beyond Neptune: 5 confirmed, 3 differed, 1 not found; 5 links failed
  the one-link rule.
- `CHECK_L443_asteroids_20261022.md` -- 28 of 35 numbers confirmed, 5
  differed, 2 not found; 12 links failed the rule, 3 with no page to
  replace them (2025 PY1, 2023 JF, 2024 DW: JPL's database page used).
- `CHECK_L443_comets_20261022.md` -- 14 confirmed, 3 differed; 3 links
  failed the rule. Deep Space 1 flew past 19P/Borrelly in 2001, not
  Tempel 2.
- `CHECK_L443_jpl_names_20261022.md` -- JPL's exact name for all 50;
  three pinned comets not on their newest record (Schaumasse, Howell,
  Churyumov-Gerasimenko).
- `CHECK_L443_classes_pairs_20261022.md` -- each body's JPL class, and
  the pairs above.

Two simple errors, fixed and reported: Chariklo was called retrograde
(JPL: inclination 23.4 degrees); Mani was called "unnumbered" (307261
Mani).

## 5. Where this leaves the brief's other questions

- **Question 4, comets and pins**: the periodic comets are pinned to
  their newest records (Tony's ruling); the long-period ones are found
  by designation, as MAPS is.
- **Question 5, the loose ends**: they stay with the slices that open
  them -- the moons' and the spacecraft's keys and checks with slices 3
  and 2; MAPS and 3I/ATLAS's live checks with their slices (MAPS is
  served now, so its check runs at the next orrery run).
- **Section 5's not-urgent decision** (whether the Lagrange points and
  the exoplanet entries are ever served): not asked, recorded on L-443.

Session record written October 2026 with Anthropic's Claude Opus 5.5.
