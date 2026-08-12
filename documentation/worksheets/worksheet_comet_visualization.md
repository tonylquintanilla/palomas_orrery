# Fact-Check Worksheet: comet_visualization_shells.py

## Instructions for Gemini

This file contains data for comet visualizations. Claims below need
verification. For each, confirm correctness and provide the
authoritative source.

Note: 3I/ATLAS and PANSTARRS entries already have extensive inline
data notes with JPL Horizons references. Those just need a formal
`# Source:` line — the data itself has been reviewed. Focus
verification effort on the other comets.

---

## Group A: Halley's Comet (line 72 area + line 1421)

| # | Claim | Value |
|---|-------|-------|
| A1 | Max dust tail length | 10 million km |
| A2 | Max ion tail length | 20 million km |
| A3 | Peak brightness | mag -0.5 |
| A4 | Perihelion distance | 0.586 AU |
| A5 | Nucleus dimensions | "15x8x8 km" (in info string) |
| A6 | Orbital period | "every 76 years" |
| A7 | Coma radius | "up to 100,000 km" |

Likely source: NASA/JPL Halley fact sheet, Giotto mission data.

---

## Group B: Hale-Bopp (line 78 area + line 1431)

| # | Claim | Value |
|---|-------|-------|
| B1 | Max dust tail length | 40 million km |
| B2 | Max ion tail length | 150 million km |
| B3 | Peak brightness | mag -1.0 |
| B4 | Perihelion distance | 0.914 AU |
| B5 | Nucleus diameter | "~60 km" (in info string) |
| B6 | Visible to naked eye | "for 18 months" |

Likely source: NASA Solar System Exploration.

---

## Group C: NEOWISE C/2020 F3 (line 88 area + line 1441)

| # | Claim | Value |
|---|-------|-------|
| C1 | Max dust tail length | 15 million km |
| C2 | Max ion tail length | 25 million km |
| C3 | Peak brightness | mag 1.0 |
| C4 | Perihelion distance | 0.295 AU |

Likely source: NASA/JPL, NEOWISE mission page.

---

## Group D: Comet West (line 98 area + line 1459)

| # | Claim | Value |
|---|-------|-------|
| D1 | Max dust tail length | 30 million km |
| D2 | Max ion tail length | 50 million km |
| D3 | Peak brightness | mag -3.0 |
| D4 | Perihelion distance | 0.197 AU |
| D5 | "Visible in daylight" | at mag -3.0? |
| D6 | "Nucleus fragmented during perihelion passage" | Confirm |

Likely source: Sekanina & Farrell 1978, NASA.

---

## Group E: Ikeya-Seki (line 108 area + line 1469)

| # | Claim | Value |
|---|-------|-------|
| E1 | Max dust tail length | 25 million km |
| E2 | Max ion tail length | 100 million km |
| E3 | Peak brightness | mag -10.0 |
| E4 | Perihelion distance | 0.008 AU |
| E5 | "450,000 km above Sun's surface" | derived from 0.008 AU? |
| E6 | "brighter than the full Moon" | at mag -10? |
| E7 | "Kreutz sungrazer family" | Confirm membership |
| E8 | "Nucleus fragmented from thermal stress" | Confirm |

Note: We already know Ikeya-Seki survived perihelion at 1.66 R_sun
inside the Roche limit (per MAPS session learnings). The 0.008 AU
claim should be checked — 0.008 AU = 1.197 million km from Sun
center = 1.72 R_sun. Does that match the known perihelion?

Likely source: Sekanina 1966/1967, NASA.

---

## Group F: Hyakutake (line 118 area + line 1450)

| # | Claim | Value |
|---|-------|-------|
| F1 | Max dust tail length | 20 million km |
| F2 | Max ion tail length | 580 million km |
| F3 | Peak brightness | mag 0.0 |
| F4 | Perihelion distance | 0.230 AU |
| F5 | Earth closest approach | "0.10 AU" |
| F6 | "LONGEST ION TAIL ever recorded" | Still true? |
| F7 | "record-breaking ion tail is still unmatched" | Still true? |

Note: The 580 million km ion tail claim is extraordinary.
Sun-Jupiter distance is ~780 million km, so "longer than
Sun-Jupiter distance" is wrong if the tail is 580 Mkm.
The info string says "longer than the Sun-Jupiter distance!"
— please confirm or correct.

Likely source: Ulysses spacecraft measurement (Geophys. Res. Lett.).

---

## Group G: MAPS C/2026 A1 (lines 225-530, 660)

The MAPS data was built collaboratively with detailed sourcing
during the April 2026 sessions. Claims to verify:

| # | Claim | Value |
|---|-------|-------|
| G1 | Nucleus diameter | ~400 m (JWST March 2026) |
| G2 | Disintegration time | April 4, 2026 ~08:15 UTC |
| G3 | Disintegration distance | 8.33 R_sun (~0.039 AU) |
| G4 | Perihelion distance | 0.005729 AU = 1.232 R_sun |
| G5 | Peak brightness | mag -0.6 (CCOR-1) |
| G6 | Perihelion velocity | 556 km/s |
| G7 | Ghost tail tracking duration | ~40 hours |
| G8 | Ghost tail dispersal | ~29 R_sun (~0.132 AU) by April 6 |
| G9 | Roche limit value used | 3.45 R_sun, 0.016 AU |
| G10 | Alfven Surface value | 18.8 R_sun, 0.087 AU |
| G11 | Streamer Belt value | 6.0 R_sun, 0.028 AU |
| G12 | Inner K-corona | 3.0 R_sun, 0.014 AU |
| G13 | "Great Comet of 363 AD" connection | Confirm |
| G14 | Corona temperature at 8.3 R_sun | "1-2 million K" |

Note: Shell values (G9-G12) should match constants_new.py. Those
are already verified through the constants provenance tests. The
MAPS-specific claims (G1-G8, G13-G14) need independent verification.

Likely sources: SOHO/LASCO observations, JWST press releases,
Sky & Telescope reports, JPL Horizons.

---

## Group H: Schaumasse, Howell, Tempel 2 (lines 256, 267, 278)

| # | Claim | Value |
|---|-------|-------|
| H1 | 24P/Schaumasse period | 8.25 years |
| H2 | Schaumasse discovery | 1911, Alexandre Schaumasse |
| H3 | Schaumasse nucleus | ~2.6 km |
| H4 | 88P/Howell period | 5.5 years |
| H5 | Howell discovery | 1981, Ellen Howell |
| H6 | 10P/Tempel 2 period | 5.37 years |
| H7 | Tempel 2 discovery | 1873, Wilhelm Tempel |
| H8 | Tempel 2 nucleus | ~16x9 km |

Likely source: JPL Small Body Database, NASA.

---

## Group I: Quad-jet structure (line 1259)

| # | Claim | Value |
|---|-------|-------|
| I1 | "120 deg spacing" of mini-jets | Confirm |
| I2 | "None point anti-sunward (anomalous for comets)" | Confirm |
| I3 | "Hubble Jan 2026: quad-jet structure confirmed" | Confirm date/source |

This is 3I/ATLAS-specific. The data notes at line 140 already
reference Hubble observations. Just needs the formal citation.

---

## Summary

Most claims will trace to:

1. NASA Solar System Exploration - individual comet pages
2. JPL Small Body Database (sbdb.jpl.nasa.gov) - orbital elements, periods
3. SOHO/LASCO reports - MAPS observations
4. Hubble press releases - 3I/ATLAS quad-jet
5. Sekanina papers - West and Ikeya-Seki fragmentation
6. Ulysses GRL paper - Hyakutake ion tail measurement
7. JWST press releases - MAPS nucleus size

For each claim: "A1: correct, source is [URL or citation]"
or "F6: WRONG, [correct info]."
