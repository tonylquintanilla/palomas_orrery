# Fact-Check Worksheet: mars_visualization_shells.py

## Instructions for Gemini

This file contains hover text for Mars's upper atmosphere,
magnetosphere, bow shock, and Hill sphere. Only 5 findings.

---

## Group A: Upper Atmosphere (lines 442, 463)

| # | Claim | Value |
|---|-------|-------|
| A1 | Exosphere starts "around 200 km/124 miles" | Confirm |
| A2 | "Without a global magnetosphere, the Martian atmosphere is directly exposed to the solar wind" | Confirm |
| A3 | Solar wind interaction "played a significant role" in atmospheric loss | Confirm |

Likely source: NASA MAVEN mission results.

---

## Group B: Magnetosphere (line 515)

| # | Claim | Value |
|---|-------|-------|
| B1 | Induced magnetosphere extends "only about 1-2 Mars radii on the Sun-facing side" | Confirm |
| B2 | Bow shock "around 1.5 Mars radii" | Confirm |
| B3 | Crustal magnetic fields "particularly in the southern hemisphere" | Confirm |
| B4 | Crustal fields are "remnants of Mars' ancient global magnetic field that existed billions of years ago" | Confirm |

Likely source: NASA MAVEN, Mars Global Surveyor.

---

## Group C: Bow Shock hover (line 624)

| # | Claim | Value |
|---|-------|-------|
| C1 | Mars bow shock "around 1.5 Mars radii" | Same as B2 |
| C2 | Comparison: "Earth's bow shock around 15 Earth radii" | Confirm |

---

## Group D: Hill Sphere (line 744)

| # | Claim | Value |
|---|-------|-------|
| D1 | "extends to ~324.5 Mars radii" | Confirm |
| D2 | "about 1.1 million km" | Confirm (324.5 * 3,389.5 km = ~1.1 Mkm) |
| D3 | "encompasses its two moons" | Confirm (Phobos at 9,376 km, Deimos at 23,463 km) |

Note: Mars radius = 3,389.5 km. 324.5 * 3,389.5 = 1.099 Mkm.
Check: Hill sphere = a * (M/3M_sun)^(1/3) where a = 1.524 AU.

Likely source: NASA Solar System Dynamics.

---

## Summary

Sources likely needed:

1. NASA MAVEN Mission (upper atmosphere, solar wind stripping)
2. Mars Global Surveyor (crustal magnetic fields)
3. NASA Mars Fact Sheet (atmospheric structure)
4. NASA Solar System Dynamics (Hill sphere)

For each: "A1: correct, source is [citation]"
or "D1: WRONG, correct value is [X]."
