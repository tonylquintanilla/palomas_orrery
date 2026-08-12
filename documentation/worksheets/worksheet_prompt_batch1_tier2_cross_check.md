# Cross-Check Worksheet Prompt — Batch 1 Tier 2

**Built on `2ccf6839c4278f01db00fbe2101440ab267a90c2`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Verify fresh — this is stated, not assumed.**

---

## Your role

You are an independent cross-checker for Paloma's Orrery, a Python/Plotly
solar system visualization project. Tony Quintanilla is the integrator.

## The job

**Value verification AND citation verification.** Each claim below has a
`# Source:` citation. For each claim:

1. **Value verification:** Independently research the correct value from
   authoritative primary sources. Does the code's number match?
2. **Citation verification:** Go to the cited source. Does it actually
   contain this value at this precision? (The Mars cross-check showed
   these can diverge: a correct value with a wrong citation, or a wrong
   value with a correct citation.)

**Research against live authoritative sources. Use web search, reference
databases, and any primary source material you can access (including
textbooks and monographs). Do NOT answer from training memory — that is
the failure class this entire mechanism exists to prevent.**

**Routing:** Tony sends this same prompt to Claude, GPT, and Gemini
independently. All three research the same claims without seeing each
other's answers. Tony compares all three worksheets for convergence.

## Worksheet format

Fill in one row per claim:

| # | Claim | Code value | Cited source | Your value | Your source | Value correct? | Citation correct? | Notes |

"Value correct?" = does the code's number match authoritative sources?
YES / NO / APPROX

"Citation correct?" = does the cited source actually contain this value?
YES / NO / PARTIAL (value present but precision differs) /
DERIVED (formula-based, verify inputs) / UNSOURCED (citation names a
source that doesn't publish this specific value)

---

# File 1: moon_visualization_shells.py

## Source block 1 (line 38 / line 53): Inner Core

```python
# Source: Weber et al. (2011), Science, "Seismic Detection of the Lunar Core";
#         inner core ~240 km radius, 1,600-1,700 K, refined from Apollo seismic data.
```

Display text claims:
- "roughly 240 kilometers in radius"
- "temperatures around 1600-1700 K"

| # | Claim | Code value | Cited source |
|---|-------|-----------|-------------|
| M1 | Moon inner core radius | ~240 km | Weber et al. 2011, Science |
| M2 | Moon inner core temperature | 1600-1700 K | Weber et al. 2011, Science |

## Source block 2 (line 121 / line 228): Outer Core

```python
# Source: NASA Moon Fact Sheet; Weber et al. (2011), Science, "Seismic Detection of the Lunar Core";
#         outer core ~330 km radius, partially molten silicate boundary layer ~150 km thick confirmed.
```

Display text claims:
- "liquid, iron-rich outer core with a radius of about 330 kilometers"
- "partially molten layer of silicates around the outer core" (~150 km thick per citation)
- "Estimates typically fall around 1300 K to 1600 K"

| # | Claim | Code value | Cited source |
|---|-------|-----------|-------------|
| M3 | Moon outer core radius | ~330 km | NASA Moon Fact Sheet; Weber et al. 2011 |
| M4 | Partial melt / silicate boundary layer thickness | ~150 km | Weber et al. 2011 |
| M5 | Outer core temperature | 1300-1600 K | Weber et al. 2011 |

## Source block 3 (line 208): Mantle

```python
# Source: NASA Moon Fact Sheet; Apollo Seismic Experiment reports (deep moonquakes 700-1,200 km,
#         tidal stress origin confirmed).
```

Display text claims:
- "deep moonquakes originating in the mantle at depths of 700 to 1,200 km"

| # | Claim | Code value | Cited source |
|---|-------|-----------|-------------|
| M6 | Deep moonquake depth range | 700-1200 km | NASA Moon Fact Sheet; Apollo Seismic Experiment |

## Source block 4 (line 557): Hill Sphere

```python
# Source: NASA Solar System Dynamics (SSD); Hill sphere radius ~60,000 km confirmed,
#         34.53 lunar radii derived from Moon mean radius 1,737.4 km.
```

Display text claims:
- "approximately 60,000 kilometers"
- "approximately 34.53 lunar radii"

| # | Claim | Code value | Cited source |
|---|-------|-----------|-------------|
| M7 | Moon Hill sphere radius | ~60,000 km | NASA SSD |
| M8 | Moon Hill sphere in lunar radii | ~34.53 R_Moon | Derived: 60,000 / 1,737.4 |

---

# File 2: eris_visualization_shells.py

## Source block 1 (line 34): Core

```python
# Source: Sicardy et al. (2011), Nature (radius 1163 km, density 2.52 g/cm^3, albedo)
#         Glein et al. (2024) (875 K core temperature model, geochemical modeling)
#         JWST (2023/2024) (D/H ratio in methane ice, internal heating evidence)
# Verified: April 2026 via Gemini fact-check
```

Display text claims:
- "high bulk density (around 2.5 g/cm^3)"
- "making up a significant portion of its mass (possibly over 85%)"

| # | Claim | Code value | Cited source |
|---|-------|-----------|-------------|
| Er1 | Eris bulk density | ~2.5 g/cm^3 | Sicardy et al. 2011, Nature |
| Er2 | Rocky mass fraction | >85% | Sicardy et al. 2011 (implied from density) |

Note: The citation also claims radius 1163 km, density 2.52 g/cm^3,
and 875 K core temperature (Glein et al. 2024). These appear in the
`# Source:` comment but not in the display text. Verify the citation's
own claims are accurate even if the display text doesn't quote them.

| # | Claim | Code value | Cited source |
|---|-------|-----------|-------------|
| Er3 | Eris radius (citation only) | 1163 km | Sicardy et al. 2011 |
| Er4 | Eris density (citation only) | 2.52 g/cm^3 | Sicardy et al. 2011 |
| Er5 | Eris core temperature model | 875 K | Glein et al. 2024 |

## Source block 2 (line 208): Crust

```python
# Source: Sicardy et al. (2011), Nature (albedo 0.96)
#         Brown & Schaller (2007) (nitrogen/methane surface composition)
# Verified: April 2026 via Gemini fact-check
```

Display text claims:
- "reflecting about 96% of the sunlight that hits it"

| # | Claim | Code value | Cited source |
|---|-------|-----------|-------------|
| Er6 | Eris albedo | 0.96 (96%) | Sicardy et al. 2011, Nature |

## Source block 3 (line 457): Hill Sphere

```python
# Source: NASA Solar System Dynamics (mass, semi-major axis)
# Note: Shell geometry uses perihelion-based Hill sphere (~8.1 Mkm);
#       average orbital distance gives ~9.4 Mkm (~0.06 AU)
# Verified: April 2026 via Gemini fact-check
```

Display text claims:
- "average orbital distance (~67.8 AU)"
- "Hill sphere radius is approximately 9.4 million kilometers (~0.06 AU)"
- "perihelion distance (~38 AU), giving ~8.1 million km"
- "Dysnomia orbits at ~37,000 km"

| # | Claim | Code value | Cited source |
|---|-------|-----------|-------------|
| Er7 | Eris average orbital distance | ~67.8 AU | NASA SSD |
| Er8 | Hill sphere at average distance | ~9.4 Mkm (~0.06 AU) | Derived from NASA SSD (mass, a) |
| Er9 | Eris perihelion distance | ~38 AU | NASA SSD |
| Er10 | Hill sphere at perihelion | ~8.1 Mkm | Derived from NASA SSD |
| Er11 | Dysnomia orbital distance | ~37,000 km | NASA SSD |

---

# File 3: mercury_visualization_shells.py

## Source block 1 (line 44): Outer Core

```python
# Source: NASA MESSENGER Mission; Margot et al. (2012) (outer core 1074 km)
# Verified: April 2026 via Gemini fact-check
```

Display text claims:
- "About 1074 km thick"

| # | Claim | Code value | Cited source |
|---|-------|-----------|-------------|
| Me1 | Mercury outer core thickness | 1074 km | Margot et al. 2012 |

## Source block 2 (line 57): Crust

```python
# Source: NASA MESSENGER; Sori (2018) (crustal thickness ~35 km)
#         Pei et al. (2024) (diamond layer from graphite + meteorite impacts)
# Verified: April 2026 via Gemini fact-check
```

Display text claims:
- "About 35 km thick"
- "crust might be made of diamonds, formed by billions of years of meteorite impacts on a graphite-rich surface"

| # | Claim | Code value | Cited source |
|---|-------|-----------|-------------|
| Me2 | Mercury crustal thickness | ~35 km | Sori 2018 |
| Me3 | Diamond layer from meteorite impacts on graphite | qualitative | Pei et al. 2024 |

## Source block 3 (line 67): Exosphere

```python
# Source: NASA MESSENGER; NASA Mercury Fact Sheet
# Verified: April 2026 via Gemini fact-check
```

Display text claims:
- "composed mostly of oxygen, sodium, hydrogen, helium, and potassium"

| # | Claim | Code value | Cited source |
|---|-------|-----------|-------------|
| Me4 | Mercury exosphere composition | O, Na, H, He, K | NASA Mercury Fact Sheet |

## Source block 4 (line 81): Sodium Tail

```python
# Source: Potter & Morgan (1985); MESSENGER sodium tail observations
# Verified: April 2026 via Gemini fact-check
```

Display text claims:
- "extends incredibly far into space - up to 10,000 Mercury radii"
- "(approximately 24 million kilometers)"

| # | Claim | Code value | Cited source |
|---|-------|-----------|-------------|
| Me5 | Mercury sodium tail extent | up to 10,000 R_Mercury | Potter & Morgan 1985; MESSENGER |
| Me6 | Sodium tail in km | ~24 million km | Derived: 10,000 × 2,440 km |

## Source block 5 (line 233): Magnetosphere

```python
# Source: NASA MESSENGER Mission
# Verified: April 2026 via Gemini fact-check
```

Display text claims (from the magnetosphere_text block, lines 292+):
- "bow shock ... around 1.4 to 2.0 radii from the center"
- "magnetopause typically extends to about 1.1 to 1.5 radii"

Code parameters (line 260+):
- `sunward_distance: 1.45` — Source: Winslow et al. 2013
- `tail_base_radius: 2.7` — Source: Winslow 2013
- `bow_shock_standoff = 1.96` — Source: Winslow et al. 2013

| # | Claim | Code value | Cited source |
|---|-------|-----------|-------------|
| Me7 | Magnetopause subsolar standoff | 1.45 R_M | Winslow et al. 2013 |
| Me8 | Magnetotail radius at 3 R_M downstream | 2.7 R_M | Winslow 2013 |
| Me9 | Bow shock standoff distance | 1.96 R_M | Winslow et al. 2013 |

## Source block 6 (line 398): Hill Sphere

```python
# Source: NASA Solar System Dynamics
# Verified: April 2026 via Gemini fact-check
```

Display text: no specific numeric claims (just qualitative description).
But the Hill sphere radius_fraction in the code should be checked.

| # | Claim | Code value | Cited source |
|---|-------|-----------|-------------|
| Me10 | Mercury Hill sphere (qualitative — no number in display text) | verify code radius_fraction | NASA SSD |

---

# File 4: venus_visualization_shells.py

Note: Tier 1 items (atmosphere at lines 328/345) are handled in the
separate Tier 1 sourcing prompt. This covers only Tier 2 (cited claims).

## Source block 1 (line 38 / line 55): Core

```python
# Source: NASA Venus Fact Sheet; NASA Solar System Exploration;
#         iron-nickel core, radius ~3,200 km, lack of dynamo due to slow rotation or solid core confirmed.
```

Display text claims:
- "radius is estimated to be around 3,200 km"
- "very slow rotation (243 days)"

| # | Claim | Code value | Cited source |
|---|-------|-----------|-------------|
| V6 | Venus core radius | ~3,200 km | NASA Venus Fact Sheet |
| V7 | Venus rotation period | 243 days | NASA Venus Fact Sheet |

## Source block 2 (line 417): Upper Atmosphere

```python
# Source: ESA Venus Express Mission; NASA Pioneer Venus Project;
#         thermosphere ~300 K dayside, night-side cryosphere 90-120 km, ionosphere 120-140 km peak confirmed.
```

Display text claims:
- "Mesosphere (approximately 60 km to 90-100 km)"
- "Thermosphere (approximately 90-100 km to 200+ km)"
- "average temperatures around 300 K (27 degC)"
- "cryosphere around 90-120 km"
- "peak electron densities occurring around 120-140 km altitude"
- "Ionosphere (approximately 120 km to several hundred km)"

| # | Claim | Code value | Cited source |
|---|-------|-----------|-------------|
| V8 | Venus mesosphere range | ~60-100 km | ESA Venus Express; Pioneer Venus |
| V9 | Venus thermosphere range | ~100-200+ km | ESA Venus Express; Pioneer Venus |
| V10 | Venus thermosphere dayside temperature | ~300 K | ESA Venus Express |
| V11 | Night-side cryosphere altitude | 90-120 km | ESA Venus Express |
| V12 | Ionosphere peak electron density altitude | 120-140 km | ESA Venus Express |

## Source block 3 (line 505 / line 560): Magnetosphere

```python
# Source: ESA Venus Express: Magnetosphere; NASA Pioneer Venus Results;
#         induced magnetosphere (not intrinsic), formed by solar wind / ionosphere interaction confirmed.
```

And the magnetosphere_text block (line 560):
```python
# Source: ESA Venus Express: Magnetosphere; NASA Pioneer Venus Results;
#         induced magnetosphere, bow shock 1.3-1.7 Rv, comet-shaped tail confirmed.
```

Display text claims:
- "Bow shock (dayside): ~1.3 - 1.7 R_V from center"
- "Magnetopause (dayside): ~1.05 - 1.1 R_V"
- "Magnetotail (nightside): tens of R_V, reaching ~45 - 60 R_V"

Code parameters:
- `sunward_distance: 1.05` — Source: Zhang et al. 2007
- `bow_shock_standoff = 1.4` — Source: Shan et al. 2015 (range 1.36-1.46)

| # | Claim | Code value | Cited source |
|---|-------|-----------|-------------|
| V13 | Venus bow shock range | 1.3-1.7 R_V | ESA Venus Express |
| V14 | Venus induced magnetopause | 1.05-1.1 R_V | Zhang et al. 2007 |
| V15 | Venus magnetotail extent | 45-60 R_V | ESA Venus Express; Pioneer Venus |
| V16 | Bow shock standoff (code) | 1.4 R_V | Shan et al. 2015, range 1.36-1.46 |

## Source block 4 (line 649): Hill Sphere

```python
# Source: NASA Solar System Dynamics (SSD); NASA Venus Fact Sheet;
#         Hill sphere ~1.01 million km / ~167 Venus radii; no natural moons confirmed.
```

Display text claims:
- "approximately 1 million kilometers"

Code: `radius_fraction = 166` (with comment "166 Venus radii")

| # | Claim | Code value | Cited source |
|---|-------|-----------|-------------|
| V17 | Venus Hill sphere radius | ~1 Mkm / ~167 R_V | NASA SSD; NASA Venus Fact Sheet |
| V18 | Code uses 166 R_V vs citation says 167 | 166 vs 167 | Verify derivation |

---

# File 5: pluto_visualization_shells.py

## Source block 1 (line 33 / line 53): Core

```python
# Source: Stern et al. (2015, Science); Bierson et al. (2020, Nature Geoscience);
#         rocky core ~1,700 km diameter (~70% of total), radioactive heating (U, Th, K), core temp ~1,000 K confirmed.
```

Display text claims:
- "core's diameter is hypothesized to be about 1700 km"
- "approximately 70% of Pluto's total diameter"
- "Radioactive isotopes such as Uranium-238, Uranium-235, Thorium-232, and Potassium-40"

| # | Claim | Code value | Cited source |
|---|-------|-----------|-------------|
| P1 | Pluto core diameter | ~1700 km | Stern et al. 2015; Bierson et al. 2020 |
| P2 | Core diameter fraction | ~70% of total | Same |
| P3 | Core temperature | ~1000 K | Same (citation comment) |

## Source block 2 (line 123 / line 140): Mantle

```python
# Source: NASA New Horizons Mission Press Kit; Stern et al. (2015, Science); Bierson et al. (2020, Nature Geoscience);
#         water-ice mantle, subsurface ocean 100-180 km thick with ammonia antifreeze confirmed.
```

Display text claims:
- "ocean could be 100 to 180 km thick"
- "lithosphere ... potentially ranging from 45 to several hundred kilometers"

| # | Claim | Code value | Cited source |
|---|-------|-----------|-------------|
| P4 | Pluto subsurface ocean thickness | 100-180 km | Stern et al. 2015; Bierson et al. 2020 |
| P5 | Lithosphere thickness range | 45 to several hundred km | Same |

## Source block 3 (line 206): Crust

```python
# Source: NASA Pluto Fact Sheet; Stern et al. (2015, Science);
#         N2 ice surface (>98% in Sputnik Planitia), water-ice mountains 2-3 km, Sputnik Planitia age <10 Myr confirmed.
```

Display text claims:
- N2 ice surface (>98% in Sputnik Planitia per citation)
- Water-ice mountains 2-3 km (per citation)
- Sputnik Planitia age <10 Myr (per citation)

| # | Claim | Code value | Cited source |
|---|-------|-----------|-------------|
| P6 | Sputnik Planitia N2 ice fraction | >98% | Stern et al. 2015 |
| P7 | Water-ice mountain height | 2-3 km | Stern et al. 2015 |
| P8 | Sputnik Planitia surface age | <10 Myr | Stern et al. 2015 |

## Source block 4 (line 373 / line 397): Haze Layer / Atmosphere

```python
# Source: Stern et al. (2015, Science); Gladstone et al. (2016, Science);
#         20+ haze layers up to 200 km confirmed by New Horizons; temperature inversion confirmed.
```

Display text claims:
- "about 1/100,000th the surface pressure of Earth's"
- "layers of haze, extending up to 200 km above the surface"
- "20 distinct haze layers" (in description dict)

| # | Claim | Code value | Cited source |
|---|-------|-----------|-------------|
| P9 | Pluto surface pressure ratio to Earth | 1/100,000th | Stern et al. 2015; Gladstone et al. 2016 |
| P10 | Haze layer extent | up to 200 km | Same |
| P11 | Number of haze layers | 20+ | Same (New Horizons) |

## Source block 5 (line 473 / line 494): Upper Atmosphere

```python
# Source: Stern et al. (2015, Science); Gladstone et al. (2016, Science);
#         exobase ~1,700 km / ~1.43 Pluto radii confirmed; temperature inversion (40 K surface -> 110 K at 30 km) confirmed.
```

Display text claims:
- "approximately 1188 km" (Pluto radius, used as reference)
- exobase at ~1700 km / ~1.43 Pluto radii (per citation)
- temperature inversion: 40 K surface to 110 K at 30 km (per citation)

| # | Claim | Code value | Cited source |
|---|-------|-----------|-------------|
| P12 | Pluto exobase altitude | ~1700 km / ~1.43 R_Pluto | Gladstone et al. 2016 |
| P13 | Surface temperature | ~40 K | Gladstone et al. 2016 |
| P14 | Temperature at 30 km altitude | ~110 K | Gladstone et al. 2016 |

## Source block 6 (line 566 / line 587): Hill Sphere

```python
# Source: NASA Solar System Dynamics (SSD); NASA Pluto Fact Sheet;
#         Hill sphere ~5.99 million km (0.04 AU); all 5 moons (Charon, Styx, Nix, Kerberos, Hydra) confirmed within.
```

Display text claims:
- "approximately 5.99 million kilometers (0.04 AU)"
- "five known moons: Charon, Styx, Nix, Kerberos, and Hydra"

| # | Claim | Code value | Cited source |
|---|-------|-----------|-------------|
| P15 | Pluto Hill sphere radius | ~5.99 Mkm (0.04 AU) | NASA SSD |
| P16 | Pluto moon count | 5 | NASA SSD |

---

## What to produce

A completed worksheet with one row per claim across all five files,
answering both: is the value correct? and does the cited source contain
this value?

Flag anything where:
- The value is wrong (authoritative source says a different number)
- The citation is wrong (source doesn't contain this value)
- The citation is vague (e.g., "NASA MESSENGER Mission" without
  specifying which dataset or publication)
- A derived value's inputs or formula don't produce the stated result
- The value is a visualization choice, not a measured constant
  (so it should be labeled as such, not cited as fact)

---

*Worksheet prompt prepared August 3, 2026 by Claude Opus 4.6
(orchestration). Batch 1 Tier 2 — cited claims needing cross-checking.
Total: 56 individual claims across 5 files.*
