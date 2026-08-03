# Follow-Up Worksheet Prompt — Batch 1 Tier 2 Unresolved Items

**Built on `2ccf6839c4278f01db00fbe2101440ab267a90c2`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Verify fresh — this is stated, not assumed.**

---

## Context

Three independent cross-checkers (Claude, GPT, Gemini) completed
worksheets for 56 claims across 5 shell modules. Many claims converged
cleanly. The items below did NOT converge, or converged on "the value
is plausible but the citation doesn't contain it."

## Your job

For each item below, **find the actual source document and quote or
closely paraphrase what it says.** The question is not "is this value
plausible" — it is "which specific document, page, table, or equation
states this value?"

**Rules:**
- Use web search, reference databases, and any primary source material
  you can access (including textbooks and monographs).
- If you find the source document, state exactly what it says about the
  specific value in question.
- If you CANNOT find a source that states the specific value, say so
  plainly. "I could not find a source that publishes this specific
  value" is the correct answer when that is the case.
- Do NOT fill in a value from training memory. That is the failure
  mode this entire process exists to prevent.
- If the value is derived (computed from other values), state the
  inputs, the formula, and the result explicitly.

**Routing:** Tony sends this same prompt to Claude, GPT, and Gemini
independently.

## Worksheet format

| # | Question | What the source says | Source (specific) | Resolution |

"Resolution" = one of:
- CONFIRMED (source found, value matches)
- WRONG VALUE (source found, says something different — state what)
- WRONG CITATION (value is correct but comes from a different source)
- DERIVED (not published; computed from stated inputs via stated formula)
- NOT FOUND (could not find any source publishing this specific value)

---

## Moon — core temperatures and moonquake depth

### FU-M1: Moon inner core temperature 1600–1700 K

The code cites Weber et al. 2011, Science. All three checkers agree
Weber 2011 is a seismic-structure paper that detects the core but does
not model its temperature. The value 1600–1700 K is plausible but
needs a different citation.

**Question:** Which specific paper publishes a lunar inner core
temperature of 1600–1700 K? Candidates suggested by checkers include
Williams et al. 2006 and Laneuville et al. Find the paper and quote
what it says about inner core temperature.

### FU-M2: Moon outer core temperature 1300–1600 K

Same issue as FU-M1. Weber 2011 does not publish temperatures.

**Question:** Which specific paper publishes a lunar outer core
temperature range of 1300–1600 K?

### FU-M3: Deep moonquake depth range — 700–1200 km or 700–1000 km?

The code says 700–1200 km. GPT found NASA MSFC Seismology explicitly
gives 700–1000 km and says the 1200 km upper end is less standard.

**Question:** What does the Apollo seismic experiment literature
actually say about the depth range of deep moonquakes? Find a specific
source (not "NASA Moon Fact Sheet" generically) and quote the range it
gives. Is 1200 km supported or is 1000 km the correct upper bound?

---

## Mercury — outer core, crust, diamond layer, sodium tail

### FU-Me1: Mercury outer core thickness 1074 km

The code cites Margot et al. 2012. GPT says 1074 km as a shell
thickness is not cleanly supported by that paper. Gemini says Margot
provides moment-of-inertia constraints and the thickness is derived in
later models (e.g., Hauck et al. 2013).

**Question:** Does Margot et al. 2012 state an outer core thickness
of 1074 km? If not, which paper does? Check Hauck et al. 2013,
"The curious case of Mercury's internal structure" (JGR Planets) and
any MESSENGER-era interior models. Quote what the source says.

### FU-Me2: Mercury crustal thickness — 35 km or 26 km?

The code says ~35 km citing Sori 2018. Gemini says Sori 2018
specifically revised the thickness DOWN to 26 km and that 35 km comes
from older papers like Padovan et al. 2015.

**Question:** What does Sori 2018 actually say about Mercury's crustal
thickness? Find the paper and quote the specific value. Also check
whether Padovan et al. 2015 or another source gives 35 km.

### FU-Me3: Mercury diamond layer — is "Pei et al. 2024" the right citation?

The code cites Pei et al. (2024) for a diamond layer formed by
meteorite impacts on a graphite-rich surface. Gemini says web search
shows Pei 2024 papers in other fields, and the Mercury diamond theory
is generally attributed to other authors (Bekaert et al. or LPSC
abstracts).

**Question:** Find the actual paper that proposes diamond formation on
Mercury from meteorite impacts on graphite. Is the author "Pei" or
someone else? Quote the source.

### FU-Me4: Mercury sodium tail — 10,000 R_Mercury from Potter & Morgan 1985?

The code cites Potter & Morgan 1985 and MESSENGER. GPT says the 1985
discovery paper predates observations that measured the tail at this
scale.

**Question:** Does Potter & Morgan 1985 state that Mercury's sodium
tail extends to 10,000 Mercury radii? If not, which paper establishes
this figure? The value likely comes from later MESSENGER-era
observations — find the specific paper.

---

## Eris — rocky mass fraction and core temperature

### FU-Er1: Eris rocky mass fraction >85%

The code says "possibly over 85%" and cites Sicardy et al. 2011.
All three checkers agree Sicardy reports density (2.52 g/cm³) but
does not state a rocky mass fraction. The >85% figure is an inference
from the density, not a published value.

**Question:** Does any published paper state that Eris's rocky mass
fraction is >85%? Or is this purely a derived inference from the bulk
density? If derived, state the calculation. If published, cite the
paper.

### FU-Er2: Eris core temperature 875 K — what does Glein et al. 2024 say?

The code cites Glein et al. 2024 (described as "geochemical modeling").
GPT says PARTIAL — model-specific, not a measured value.

**Question:** Find Glein et al. 2024 and confirm whether it models
an Eris core temperature of 875 K. Is this in Science Advances as
Gemini suggests? Quote what the paper says about Eris's internal
temperature.

### FU-Er3: Eris Hill sphere — confirm the arithmetic

Claude and GPT independently computed ~14.2–14.3 Mkm at average
distance (67.8 AU), not 9.4 Mkm. Gemini accepted 9.4 Mkm.

**Question:** Using Eris mass from JPL SSD and semi-major axis 67.8 AU,
compute the Hill sphere radius via r_H = a × (m / 3M_sun)^(1/3).
Show the inputs, the calculation, and the result. This is purely
arithmetic — there is no source to look up.

---

## Venus — atmospheric layer citations and Hill sphere computation

### FU-V1: Venus mesosphere, thermosphere, cryosphere — specific sources

The code cites "ESA Venus Express Mission; NASA Pioneer Venus Project"
for atmospheric layer boundaries: mesosphere ~60–100 km, thermosphere
~100–200+ km, dayside ~300 K, night-side cryosphere 90–120 km,
ionosphere peak 120–140 km.

GPT marked all of these "PARTIAL" because the mission-level citation
is too vague. Gemini accepted them.

**Question:** For each of these values, find the specific publication
(not "ESA Venus Express" generically) that states the boundary
altitude or temperature. Candidates: Limaye et al. (2018, Space Sci
Rev), Sánchez-Lavega et al. (2017), VIRA (Seiff et al. 1985),
Bougher et al. (various). Quote what each source says for:
- Mesosphere upper boundary (60 km, 65 km, or what?)
- Thermosphere dayside temperature (~300 K or what?)
- Cryosphere altitude (90–120 km or what?)
- Ionosphere peak electron density altitude (120 km, 140 km, or what?)

### FU-V2: Venus magnetotail 45–60 R_V — which source?

The code cites "ESA Venus Express; NASA Pioneer Venus." GPT says this
is now supported by newer flyby data (Edberg et al. 2024/2025), not
the older missions as cited.

**Question:** Find the specific paper that establishes Venus's
magnetotail extent at 45–60 R_V. Is it from Venus Express, Pioneer
Venus Orbiter, Solar Orbiter flybys, or something else?

### FU-V3: Venus Hill sphere — compute from NSSDCA inputs

Claude computes 1,011,109 km (167.1 R_V). Gemini computes 1,004,000
km (165.9 R_V). GPT gets 165–166 R_V.

**Question:** Using the NASA NSSDCA Venus Fact Sheet values for Venus
mass and semi-major axis, and the Sun's mass, compute the Hill sphere
radius. Show all inputs with their exact values and sources, the
formula, and the result. This is arithmetic — there is no source to
look up for the Hill radius itself.

---

## Pluto — exobase, core temperature, N₂ purity

### FU-P1: Pluto exobase — 1700 km altitude or 1700 km from center?

The code says the exobase is at "~1,700 km" and "~1.43 Pluto radii."
GPT flags a unit confusion: 1700 km altitude above the surface =
2888 km from center = 2.43 R_Pluto. But 1.43 R_Pluto from center =
1700 km from center = only 512 km altitude.

**Question:** What does Gladstone et al. 2016 (Science) actually say
about Pluto's exobase altitude? Find the paper and quote the specific
value — is it 1700 km above the surface, 1700 km from center, 1.43 R,
or something else?

### FU-P2: Pluto core temperature ~1000 K

The code cites Stern et al. 2015 and Bierson et al. 2020. GPT says
the cited papers do not establish a measured 1000 K.

**Question:** Does Bierson et al. 2020 (Nature Geoscience) model or
state a Pluto core temperature of ~1000 K? Find the paper and quote
what it says about internal temperature.

### FU-P3: Sputnik Planitia N₂ ice >98%

The code says N₂ ice fraction >98% citing Stern et al. 2015. GPT says
the paper says N₂-dominated but doesn't quantify >98%.

**Question:** Does Stern et al. 2015 state that Sputnik Planitia is
>98% nitrogen ice? If not, does any New Horizons paper give a
specific quantitative purity? (Grundy et al. 2016 on surface
composition is a candidate.) Quote what the source says.

---

## Dysnomia orbit — confirm source

### FU-Dy1: Dysnomia orbital distance ~37,000 km

GPT says YES from JPL satellite elements. Gemini says APPROX from
Brown & Schaller 2007. The value appears correct but the specific
source matters.

**Question:** What does JPL SSD list for Dysnomia's semi-major axis?
And does Brown & Schaller 2007 give this value, or is it from a later
paper (e.g., Brown & Butler 2018)?

---

## What to produce

A completed worksheet with one row per item (FU-M1 through FU-Dy1),
answering: what does the actual source document say?

Do not fill in plausible values. If you cannot find the source
document, the correct answer is "NOT FOUND."

---

*Follow-up prompt prepared August 3, 2026 by Claude Opus 4.6
(orchestration). 18 unresolved items from Batch 1 Tier 2 three-way
comparison.*
