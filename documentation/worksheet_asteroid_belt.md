# Fact-Check Worksheet: asteroid_belt_visualization_shells.py

## Instructions for Gemini

This file contains hover text and info strings for an astronomical
visualization. Each claim below needs verification against an
authoritative source. For each group, please confirm:

1. Is each number correct?
2. What is the authoritative source? (NASA fact sheet URL, IAU, 
   specific paper, etc.)
3. Flag anything that's wrong or imprecise.

---

## Group A: Main Asteroid Belt (lines 113-123, 198-200)

Claims in the info string and hover text:

| # | Claim | Needs verification? |
|---|-------|-------------------|
| A1 | Belt located "roughly 2.2 to 3.2 AU from the Sun" | Yes |
| A2 | Ceres diameter "940 km" | Yes |
| A3 | Total belt mass "about 4% of the Moon's mass" | Yes |
| A4 | "Peak density occurs around 2.7 AU" | Yes |
| A5 | Composition: "C-type (carbonaceous, 75%), S-type (silicaceous, 17%), or M-type (metallic)" | Yes - percentages especially |
| A6 | "Kirkwood gaps at distances where orbital resonances with Jupiter cause orbital instabilities" | Conceptual - likely correct but confirm |

Likely source: NASA Solar System Exploration - Asteroid Belt, or
JPL Small Bodies Database.

---

## Group B: Hilda Family (lines 235-242, 290-292)

| # | Claim | Needs verification? |
|---|-------|-------------------|
| B1 | "3:2 orbital resonance with Jupiter" | Yes |
| B2 | Located at "approximately 3.97 AU" | Yes |
| B3 | "triangular pattern...concentrations at the L3, L4, and L5 Lagrange points" | Yes - is L3 correct here, or is it the three libration points of the 3:2 resonance? |
| B4 | "Named after asteroid 153 Hilda, discovered in 1875" | Yes |
| B5 | "about 4,000 known members" | Yes - may have changed |
| B6 | "most are D-type (dark, reddish) asteroids" | Yes |

Note on B3: The Hilda triangle is NOT at Jupiter's Lagrange points.
The three vertices of the Hilda triangle are 120 degrees apart in a
pattern related to the 3:2 resonance geometry. The info string says
"L3, L4, and L5 Lagrange points relative to Jupiter" which may be
incorrect. Please clarify.

Likely source: Nesvorny et al. or JPL.

---

## Group C: Jupiter Trojans - L4 Greeks (lines 327-335, 383-385)

| # | Claim | Needs verification? |
|---|-------|-------------------|
| C1 | "L4 Lagrange point (leading Jupiter by 60 deg)" | Yes |
| C2 | Jupiter orbital distance "~5.2 AU" | Yes |
| C3 | "L4 Greeks slightly outnumber the L5 Trojans" | Yes |
| C4 | "624 Hektor (largest at ~250 km)" | Yes - is Hektor still considered largest? |
| C5 | "617 Patroclus (binary asteroid, NASA Lucy mission target)" | Yes |
| C6 | "588 Achilles" mentioned as notable | Yes - confirm it's notable/first discovered |
| C7 | "Most are D-type asteroids - dark, reddish bodies rich in organic compounds" | Yes |

Likely source: NASA Lucy mission page, MPC.

---

## Group D: Jupiter Trojans - L5 Trojans (lines 420-427, 475-477)

| # | Claim | Needs verification? |
|---|-------|-------------------|
| D1 | "L5 Lagrange point (trailing Jupiter by 60 deg)" | Yes |
| D2 | "884 Priamus, 1172 Aeneas, and 911 Agamemnon" as notable members | Yes - confirm these are real numbered asteroids at L5 |
| D3 | "L5 camp has about 40% fewer asteroids than L4" | Yes - this ratio is debated; confirm current understanding |
| D4 | "NASA's Lucy mission will visit both camps" | Yes |

Note on D2: 911 Agamemnon is traditionally listed as a Greek (L4),
not a Trojan (L5). If so, it's in the wrong camp in our text.
Please verify which camp each of these three belongs to.

Likely source: NASA Lucy mission page, MPC.

---

## Summary of Likely Sources

Most claims will trace back to 3-5 sources:

1. NASA Solar System Exploration - Asteroid Belt overview
2. NASA Lucy Mission - for Trojan-specific data
3. JPL Small Body Database - for specific asteroid numbers/sizes
4. IAU Minor Planet Center - for population counts
5. Possibly a textbook/review paper for the composition percentages

For each verified claim, just tell me: "A1: correct, source is [URL]"
or "B3: WRONG, the Hilda triangle is [correct explanation]."

I'll insert the citations into the code.
