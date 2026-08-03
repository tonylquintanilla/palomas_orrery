# Blind Source Lookup — Batch 1 Final Resolution

**Built on `2ccf6839c4278f01db00fbe2101440ab267a90c2`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Verify fresh — this is stated, not assumed.**

---

## Context

You are an independent fact-checker for Paloma's Orrery, a Python/Plotly
solar system visualization project. Tony Quintanilla is the integrator.

This is a targeted follow-up. For each item below, you are given a
**specific source document** and asked to report **what it says** about
a specific topic. You are NOT told what value to expect. Report what the
source says in its own terms.

## Rules

- **Find the named source and report what it says.** Use web search,
  reference databases, and any primary source material you can access
  (including textbooks).
- **Do NOT work from training memory.** If you cannot access the source,
  say so. Do not reconstruct what it "probably says."
- **Quote or closely paraphrase the source's own language.** The goal is
  to know exactly what the paper states, not what the value "should be."
- **If the source does not address the topic, say "NOT ADDRESSED."**

**Routing:** Tony sends this same prompt to Claude, GPT, and Gemini
independently.

## Worksheet format

| # | Source to check | Topic | What the source says | Resolution |

---

## BL-1: Mercury sodium tail extent

Three papers to check. For each one, report what it says about the
spatial extent of Mercury's sodium tail (in Mercury radii, kilometers,
or any unit the paper uses).

| Paper | Full citation |
|-------|-------------|
| A | Potter, A.E. & Morgan, T.H. (1985), "Discovery of sodium in the atmosphere of Mercury", *Science* 229, 651–653 |
| B | Baumgardner, J., Wilson, J. & Mendillo, M. (2008), "Imaging the Sources and Full Extent of the Sodium Tail of the Planet Mercury", *GRL* 35, L03201 |
| C | Schmidt, C.A. et al. (2010), "Observations of Mercury's sodium tail", *Icarus* 207, 9–16 |

For each paper: what maximum extent does it report for the sodium tail?

## BL-2: Eris internal temperature

Search for the paper: "The Internal Structure of Eris Inferred from
Its Spin and Orbit Evolution", published in *Science Advances* (2023).
(GPT identified this as the likely source for Eris's modeled core
temperature, distinct from Glein et al.'s methane geochemistry paper.)

What present-day central temperature does this paper model for Eris?
What inputs does it use (heating rate, conductivity, surface
temperature)?

## BL-3: Mercury interior structure

Two papers to check:

| Paper | Full citation |
|-------|-------------|
| A | Margot, J.-L. et al. (2012), "Mercury's moment of inertia from spin and gravity data", *JGR Planets* |
| B | Hauck, S.A. et al. (2013), "The Curious Case of Mercury's Internal Structure", *JGR Planets* 118, 1204–1220 |

For each paper: what does it say about Mercury's internal dimensions?
Specifically, does it state values for: core radius, inner core radius,
outer core thickness, mantle thickness, or crustal thickness? Report
whatever dimensional values the paper gives.

## BL-4: Venus atmospheric structure

Two sources to check:

| Source | Full citation |
|-------|-------------|
| A | Bertaux, J.-L. et al. (2007), "A Warm Layer in Venus' Cryosphere and High-Altitude Measurements of HF, HCl, H2O and HDO", *Nature* 450, 646–649 |
| B | Seiff, A. et al. (1985), "Models of the structure of the atmosphere of Venus from the surface to 100 kilometers altitude", *Advances in Space Research* 5(11), 3–58 (the Venus International Reference Atmosphere — VIRA) |

For each source, what does it say about:
- The altitude boundaries of the mesosphere?
- The altitude boundaries of the thermosphere?
- Dayside thermosphere temperature?
- The nightside cryosphere and its altitude range?
- The ionosphere peak electron density altitude?

Report whatever the source gives for each of these. If it doesn't
address a particular item, say NOT ADDRESSED.

## BL-5: Lunar core temperatures

Search for: Williams, J.G. et al. (2006), likely published in *JGR
Planets* or a related journal, concerning the Moon's deep interior
thermal state. (Gemini identified this as the source for lunar core
temperature estimates of 1600–1700 K.)

Also check: Laneuville, M. et al. (2014), published in *EPSL* or
*JGR Planets*, on lunar thermal evolution.

For each paper: what does it say about the temperature of the Moon's
inner core? What does it say about the temperature of the outer core
or core-mantle boundary region?

## BL-6: Pluto internal temperature

Search for: Bierson, C.J., Nimmo, F. & Stern, S.A. (2020), "Evidence
for a Hot Start and Early Ocean Formation on Pluto", *Nature
Geoscience* 13, 468–472.

What does this paper say about Pluto's internal temperature — both at
the time of formation/accretion AND at the present day? Report both
if given.

## BL-7: Pluto surface temperature

Search for: Gladstone, G.R. et al. (2016), published in *Science* 351,
on Pluto's atmosphere as observed by New Horizons.

What surface temperature does this paper report for Pluto? In what
units? With what uncertainty?

## BL-8: Hill sphere convention for binary systems

This is a physics/orbital mechanics question, not a paper lookup.

When computing the Hill sphere radius for a binary system like
Pluto-Charon or Eris-Dysnomia orbiting the Sun:

- Should the mass used be the **primary body alone** (e.g., Pluto
  without Charon), or the **system barycenter mass** (Pluto + Charon
  combined)?
- Is there a standard convention in the planetary science literature?
- Does the choice matter for the physical meaning of the Hill sphere
  (i.e., the region where the system's gravity dominates over the
  Sun's)?

Search for how JPL SSD, Murray & Dermott "Solar System Dynamics", or
other standard references treat this. Report what they say.

---

## What to produce

A completed worksheet with one entry per item (BL-1 through BL-8),
reporting what each source says in its own terms. If you cannot access
a source, say so plainly.

---

*Blind-lookup prompt prepared August 3, 2026 by Claude Opus 4.6
(orchestration). Eight items requiring source verification without
prior value expectation.*
