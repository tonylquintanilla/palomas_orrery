# Fact-Check Worksheet: jupiter_visualization_shells.py

## Instructions for Gemini

This file contains hover text and info strings for Jupiter's interior
layers, atmosphere, rings, Hill sphere, and magnetosphere. Please
verify each claim and provide the authoritative source.

---

## Group A: Jupiter Core (lines 62-82)

| # | Claim | Needs verification? |
|---|-------|-------------------|
| A1 | Core is "a dense mixture of rock, metal, and hydrogen compounds" | Yes |
| A2 | Core "may be up to 10 times the mass of Earth" | Yes |
| A3 | Core "might be partially dissolved or 'fuzzy'" | Yes - this is from Juno results |
| A4 | Core temperature "about 20,000K and up to 40,000K" | Yes |

Likely source: NASA Juno mission results, Wahl et al. (2017).

---

## Group B: Metallic Hydrogen Layer (lines 117-135)

| # | Claim | Needs verification? |
|---|-------|-------------------|
| B1 | "hydrogen transitions to a metallic state" under extreme pressure | Yes |
| B2 | "responsible for generating Jupiter's powerful magnetic field" | Yes |
| B3 | "Temperatures in this region may reach 10,000K" | Yes |

Likely source: NASA Jupiter fact sheet, Juno mission.

---

## Group C: Molecular Hydrogen Layer (lines 171-192)

| # | Claim | Needs verification? |
|---|-------|-------------------|
| C1 | "transition from metallic to molecular hydrogen is gradual" | Yes |
| C2 | "makes up the bulk of Jupiter's mass" | Yes |
| C3 | Temperature "ranges from about 5,000K (outer) to 10,000K (inner)" | Yes |

Likely source: NASA Jupiter fact sheet.

---

## Group D: Cloud Layer (lines 227-252)

| # | Claim | Needs verification? |
|---|-------|-------------------|
| D1 | Clouds "primarily composed of ammonia, ammonium hydrosulfide, and water" | Yes |
| D2 | Temperature "120 K in the highest ammonia ice clouds" | Yes |
| D3 | Temperature "about 200 K in the lower ammonium hydrosulfide clouds" | Yes |

Likely source: NASA Jupiter fact sheet, Galileo probe data.

---

## Group E: Upper Atmosphere (lines 388-411)

| # | Claim | Needs verification? |
|---|-------|-------------------|
| E1 | "contains hydrocarbon haze produced by solar ultraviolet radiation" | Yes |
| E2 | Temperature "200K in the stratosphere to 1000K in the thermosphere" | Yes |

Likely source: NASA Jupiter fact sheet.

---

## Group F: Radiation Belts (line 594)

| # | Claim | Needs verification? |
|---|-------|-------------------|
| F1 | No specific numeric claims in this string | Conceptual only |

Low priority — just says "trapped high-energy particles."

---

## Group G: Hill Sphere (lines 688-710)

| # | Claim | Needs verification? |
|---|-------|-------------------|
| G1 | "extends to ~530 Jupiter radii or about 0.25 AU" (info string) | Yes |
| G2 | "extends to ~740 Jupiter radii" (description hover text) | Yes |
| G3 | radius_fraction = 740 (code value) | Yes |

**INCONSISTENCY FLAG:** The info string says ~530 R_J / 0.25 AU,
but the hover description and the code both use 740 R_J. These
can't both be right. Please determine the correct Hill sphere
radius for Jupiter.

Note: Jupiter's equatorial radius = 71,492 km (per constants_new.py
Hybrid Radius Convention). Hill sphere radius formula:
R_H = a * (M_planet / 3*M_star)^(1/3)
where a = 5.2 AU (Jupiter semi-major axis).

Likely source: NASA Solar System Dynamics.

---

## Group H: Jupiter Ring System (lines 798-846)

| # | Claim | Needs verification? |
|---|-------|-------------------|
| H1 | Main Ring: 122,500 km to 129,000 km from center | Yes |
| H2 | Main Ring thickness: 30-300 km | Yes |
| H3 | Main Ring: "dust ejected from...Metis and Adrastea" | Yes |
| H4 | Halo Ring: extends to 100,000 km from center | Yes |
| H5 | Halo Ring: "12,500 km vertically" | Yes |
| H6 | Halo Ring: "fine dust...pushed by electromagnetic forces" | Yes |
| H7 | Amalthea Gossamer Ring: to 182,000 km (Amalthea's orbit) | Yes |
| H8 | Thebe Gossamer Ring: to 226,000 km (beyond Thebe's orbit) | Yes |
| H9 | Thebe Gossamer Ring: "vertical extension of about 8,600 km" | Yes |

Likely source: Galileo spacecraft data, NASA Jupiter Ring Fact Sheet.

---

## Group I: Magnetosphere (line 904)

| # | Claim | Needs verification? |
|---|-------|-------------------|
| I1 | "extends up to 100 Jupiter radii on the sunward side" | Yes |
| I2 | "magnetotail stretching beyond Saturn's orbit" | Yes |
| I3 | "radiation belts that would be lethal to humans" | Yes |
| I4 | Io plasma torus from "volcanic activity" | Yes |

Likely source: NASA Jupiter Magnetosphere page, Juno data.

---

## Summary

Most claims should trace to:

1. NASA Solar System Exploration - Jupiter
   (https://science.nasa.gov/jupiter/)
2. NASA Juno Mission results (core structure, magnetosphere)
3. NASA Jupiter Ring Fact Sheet / Galileo data
4. NASA Planetary Fact Sheet
   (https://nssdc.gsfc.nasa.gov/planetary/factsheet/jupiterfact.html)

**Priority flag:** The Hill sphere inconsistency (G1 vs G2) needs
resolution — one of the two values is wrong in the code.

For each claim: "A1: correct, source is [URL or citation]"
or "G1: WRONG, correct value is [X]."
