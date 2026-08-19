# Cross-check request -- constants_new_pilot_claude

**Built on `eae95f5a119906968634d57a9fab8964e815466e` at https://github.com/tonylquintanilla/palomas_orrery.**

Extractor version: 2. Key format: `module.py::enclosing::label::cN`.

Selection: `constants_new` -- constants_new.py only -- the pilot slice (L-201). Its branch coverage is a property of the file, not of anyone's judgement about which rows are interesting.

23 of 100 rows in the corpus. The KEY identifies a row; the number in the first column is assigned by position in this file and means nothing outside it.

Do not edit the Key, Claim or Code value columns. They record what the code said at the SHA above, and the checker compares your answer against that state.

## What each column asks

- **Your value** -- the number the source states. If the sources disagree, give the range AND the rule you used to reduce it (for example "2.5-2.7, took the midpoint to two significant figures").
- **Source** -- the authority you consulted, specific enough to find again.
- **Value correct?** -- about the NUMBER only.
- **Citation correct?** -- about the code's cited source only, shown per row below. Answer it separately from the value: a right number under a wrong authority is a real finding and one token cannot say it.
- **Notes** -- anything a token cannot carry. The checker reads notes as prose for a human, never as a verdict.

Use one token per verdict cell. A cell holding a token plus a qualification is reported as unclassified rather than read, because guessing which half you meant is the interpretation this system is built to avoid.

## The accepted verdict words

Anything outside this list is read as unclassified and the row comes back.

- **ABSENT** -- `unverified` (answers whichever question the column asks)
- **CONFIRMED** -- `confirmed`, `correct`, `yes` (answers whichever question the column asks)
- **DERIVED** -- `derived` (answers whichever question the column asks)
- **INCOMPLETE** -- `approx`, `approximate`, `partial` (answers whichever question the column asks)
- **REFUTED** -- `no` (answers whichever question the column asks)
- **SOURCE_ABSENT** -- `unsourced` (answers the citation only)

## Rows in context (read-only)

**R1** -- `constants_new.py::KM_PER_AU`

- Site: `constants_new.py:54`
- Code value: `149597870.7`
- Claim: KM_PER_AU
- **Cited source (this is what "Citation correct?" answers):** IAU 2012 Resolution B2 -- exact definition
- Also cited, context only, NOT verdicted: Ref: https://syrte.obspm.fr/IAU_resolutions/Res_IAU2012_B2.pdf
- Also cited, context only, NOT verdicted: Also: https://nssdc.gsfc.nasa.gov/planetary/factsheet/fact_notes.html

**R2** -- `constants_new.py::SUN_RADIUS_KM`

- Site: `constants_new.py:62`
- Code value: `695700.0`
- Claim: SUN_RADIUS_KM
- **Cited source (this is what "Citation correct?" answers):** IAU 2015 Resolution B3 -- nominal solar radius
- Also cited, context only, NOT verdicted: Ref: Prsa et al. 2016, AJ 152:41 (arXiv:1605.09788)
- Also cited, context only, NOT verdicted: Also: https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html

**R3** -- `constants_new.py::EARTH_EQUATORIAL_RADIUS_KM`

- Site: `constants_new.py:72`
- Code value: `6378.137`
- Claim: EARTH_EQUATORIAL_RADIUS_KM
- **Cited source (this is what "Citation correct?" answers):** IAU 2015 Resolution B3 -- nominal terrestrial equatorial radius
- Also cited, context only, NOT verdicted: Ref: Prsa et al. 2016, AJ 152:41 (arXiv:1605.09788)
- Also cited, context only, NOT verdicted: Also: https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html

**R4** -- `constants_new.py::EARTH_POLAR_RADIUS_KM`

- Site: `constants_new.py:80`
- Code value: `6356.752`
- Claim: EARTH_POLAR_RADIUS_KM
- **Cited source (this is what "Citation correct?" answers):** IERS Conventions (Petit & Luzum 2010); IAU B3 rounds to 6356.8 km
- Also cited, context only, NOT verdicted: Ref: Prsa et al. 2016, AJ 152:41 (arXiv:1605.09788)

**R5** -- `constants_new.py::JUPITER_EQUATORIAL_RADIUS_KM`

- Site: `constants_new.py:86`
- Code value: `71492.0`
- Claim: JUPITER_EQUATORIAL_RADIUS_KM
- **Cited source (this is what "Citation correct?" answers):** IAU 2015 Resolution B3 -- nominal jovian equatorial radius
- Also cited, context only, NOT verdicted: Ref: Prsa et al. 2016, AJ 152:41 (arXiv:1605.09788)

**R6** -- `constants_new.py::JUPITER_POLAR_RADIUS_KM`

- Site: `constants_new.py:92`
- Code value: `66854.0`
- Claim: JUPITER_POLAR_RADIUS_KM
- **Cited source (this is what "Citation correct?" answers):** IAU 2015 Resolution B3 -- nominal jovian polar radius
- Also cited, context only, NOT verdicted: Ref: Prsa et al. 2016, AJ 152:41 (arXiv:1605.09788)

**R7** -- `constants_new.py::SPEED_OF_LIGHT_KM_S`

- Site: `constants_new.py:98`
- Code value: `299792.458`
- Claim: SPEED_OF_LIGHT_KM_S
- **Cited source (this is what "Citation correct?" answers):** NIST/SI exact definition
- Also cited, context only, NOT verdicted: Ref: https://physics.nist.gov/cgi-bin/cuu/Value?c

**R8** -- `constants_new.py::CHROMOSPHERE_PHYSICAL_KM`

- Site: `constants_new.py:175`
- Code value: `2000.0`
- Claim: CHROMOSPHERE_PHYSICAL_KM
- **Cited source (this is what "Citation correct?" answers):** Carroll & Ostlie, An Introduction to Modern Astrophysics, Ch. 11 -- chromosphere extends ~2000 km above the photosphere.

**R9** -- `constants_new.py::INNER_CORONA_RADII`

- Site: `constants_new.py:186`
- Code value: `3`
- Claim: INNER_CORONA_RADII
- **Cited source (this is what "Citation correct?" answers):** Golub & Pasachoff, "The Solar Corona" (2010)

**R10** -- `constants_new.py::STREAMER_BELT_RADII`

- Site: `constants_new.py:197`
- Code value: `6.0`
- Claim: STREAMER_BELT_RADII
- **Cited source (this is what "Citation correct?" answers):** Golub & Pasachoff (2010); DeForest, Howard & McComas (2014), ApJ 787:124
- Also cited, context only, NOT verdicted: See: Eclipse observations; helmet streamers extend 4-6 R_sun

**R11** -- `constants_new.py::ROCHE_LIMIT_RADII`

- Site: `constants_new.py:205`
- Code value: `3.45`
- Claim: ROCHE_LIMIT_RADII
- **Cited source (this is what "Citation correct?" answers):** Murray & Dermott, "Solar System Dynamics" (1999), Sec. 4.6
- Also cited, context only, NOT verdicted: Derived: Fluid Roche limit formula: d = 2.44 * R * (rho_sun/rho_comet)^(1/3)
- Also cited, context only, NOT verdicted: Calculation: 2.44 * 1.0 * (1408/500)^(1/3) = 3.45 R_sun Using rho_sun = 1408 kg/m3, rho_comet ~ 500 kg/m3

**R12** -- `constants_new.py::ALFVEN_SURFACE_RADII`

- Site: `constants_new.py:215`
- Code value: `18.8`
- Claim: ALFVEN_SURFACE_RADII
- **Cited source (this is what "Citation correct?" answers):** Kasper et al. (2021), Phys. Rev. Lett. 127:255101
- Also cited, context only, NOT verdicted: See: Parker Solar Probe first crossing, April 28, 2021
- Also cited, context only, NOT verdicted: Also: https://www.nasa.gov/feature/goddard/2021/nasa-enters-the-solar-atmosphere

**R13** -- `constants_new.py::TERMINATION_SHOCK_AU`

- Site: `constants_new.py:230`
- Code value: `94`
- Claim: TERMINATION_SHOCK_AU
- **Cited source (this is what "Citation correct?" answers):** Stone et al. (2005), Science 309:2017
- Also cited, context only, NOT verdicted: See: Voyager 1 crossed at 94 AU (Dec 2004)
- Also cited, context only, NOT verdicted: Also: Voyager 2 crossed at 84 AU (Aug 2007) -- asymmetric

**R14** -- `constants_new.py::HELIOPAUSE_RADII`

- Site: `constants_new.py:237`
- Code value: `26148`
- Claim: HELIOPAUSE_RADII
- **Cited source (this is what "Citation correct?" answers):** Gurnett et al. (2013), Science 341:1489
- Also cited, context only, NOT verdicted: See: Voyager 1 crossed heliopause at ~121.6 AU (Aug 2012)

**R15** -- `constants_new.py::PARKER_CLOSEST_RADII`

- Site: `constants_new.py:279`
- Code value: `9.86`
- Claim: PARKER_CLOSEST_RADII
- **Cited source (this is what "Citation correct?" answers):** https://parkersolarprobe.jhuapl.edu/The-Mission/index.php
- Also cited, context only, NOT verdicted: See: Parker Solar Probe perihelion 22, Dec 24, 2024

**R16** -- `constants_new.py::MOON_RADIUS_KM`

- Site: `constants_new.py:336`
- Code value: `1737.4`
- Claim: MOON_RADIUS_KM
- **Cited source (this is what "Citation correct?" answers):** NASA NSSDCA Fact Sheet (volumetric mean; oblateness ~0.0012) Also IAU/LRO reference radius (Archinal et al. 2011)

**R17** -- `constants_new.py::MARS_RADIUS_KM`

- Site: `constants_new.py:343`
- Code value: `3396.2`
- Claim: MARS_RADIUS_KM
- **Cited source (this is what "Citation correct?" answers):** Archinal et al. 2018, Celest. Mech. Dyn. Astr. 130:22 (equatorial; vol = 3389.5)

**R18** -- `constants_new.py::SATURN_RADIUS_KM`

- Site: `constants_new.py:351`
- Code value: `60268`
- Claim: SATURN_RADIUS_KM
- **Cited source (this is what "Citation correct?" answers):** Archinal et al. 2018, Celest. Mech. Dyn. Astr. 130:22 (equatorial; vol = 58232)

**R19** -- `constants_new.py::URANUS_RADIUS_KM`

- Site: `constants_new.py:356`
- Code value: `25559`
- Claim: URANUS_RADIUS_KM
- **Cited source (this is what "Citation correct?" answers):** Archinal et al. 2018, Celest. Mech. Dyn. Astr. 130:22 (equatorial; vol = 25362)

**R20** -- `constants_new.py::NEPTUNE_RADIUS_KM`

- Site: `constants_new.py:361`
- Code value: `24764`
- Claim: NEPTUNE_RADIUS_KM
- **Cited source (this is what "Citation correct?" answers):** Archinal et al. 2018, Celest. Mech. Dyn. Astr. 130:22 (equatorial; vol = 24622)

**R21** -- `constants_new.py::BENNU_RADIUS_KM`

- Site: `constants_new.py:369`
- Code value: `0.246`
- Claim: BENNU_RADIUS_KM
- **Cited source (this is what "Citation correct?" answers):** Nolan et al. 2013 (radar shape model), mean diameter 492 +/- 20 m Confirmed by OSIRIS-REx OLA: mean radius 246 +/- 10 m, V = 0.062 km^3

**R22** -- `constants_new.py::HAUMEA_RADIUS_KM`

- Site: `constants_new.py:379`
- Code value: `715`
- Claim: HAUMEA_RADIUS_KM
- **Cited source (this is what "Citation correct?" answers):** JPL SSD mean radius (Lockwood et al. 2014) Highly ellipsoidal: 1050x840x537 km -> geometric mean 779.5 km JPL SSD publishes 715; equatorial 870

**R23** -- `constants_new.py::ARROKOTH_RADIUS_KM`

- Site: `constants_new.py:390`
- Code value: `9.1`
- Claim: ARROKOTH_RADIUS_KM
- **Cited source (this is what "Citation correct?" answers):** Keane et al. 2022, JGR Planets (New Horizons shape model) Volume 3166 km^3 -> equivalent sphere radius 9.1 km Overall dims 35.95 x 19.90 x 9.75 km (bilobed contact binary) Corrected 2026-04-15 per Gemini review (was 0.0088 = 8.8 meters!)

## Response table

| # | Key | Claim | Code value | Your value | Source | Value correct? | Citation correct? | Notes |
|---|---|---|---|---|---|---|---|---|
| R1 | `constants_new.py::KM_PER_AU` | KM_PER_AU | 149597870.7 |  |  |  |  |  |
| R2 | `constants_new.py::SUN_RADIUS_KM` | SUN_RADIUS_KM | 695700.0 |  |  |  |  |  |
| R3 | `constants_new.py::EARTH_EQUATORIAL_RADIUS_KM` | EARTH_EQUATORIAL_RADIUS_KM | 6378.137 |  |  |  |  |  |
| R4 | `constants_new.py::EARTH_POLAR_RADIUS_KM` | EARTH_POLAR_RADIUS_KM | 6356.752 |  |  |  |  |  |
| R5 | `constants_new.py::JUPITER_EQUATORIAL_RADIUS_KM` | JUPITER_EQUATORIAL_RADIUS_KM | 71492.0 |  |  |  |  |  |
| R6 | `constants_new.py::JUPITER_POLAR_RADIUS_KM` | JUPITER_POLAR_RADIUS_KM | 66854.0 |  |  |  |  |  |
| R7 | `constants_new.py::SPEED_OF_LIGHT_KM_S` | SPEED_OF_LIGHT_KM_S | 299792.458 |  |  |  |  |  |
| R8 | `constants_new.py::CHROMOSPHERE_PHYSICAL_KM` | CHROMOSPHERE_PHYSICAL_KM | 2000.0 |  |  |  |  |  |
| R9 | `constants_new.py::INNER_CORONA_RADII` | INNER_CORONA_RADII | 3 |  |  |  |  |  |
| R10 | `constants_new.py::STREAMER_BELT_RADII` | STREAMER_BELT_RADII | 6.0 |  |  |  |  |  |
| R11 | `constants_new.py::ROCHE_LIMIT_RADII` | ROCHE_LIMIT_RADII | 3.45 |  |  |  |  |  |
| R12 | `constants_new.py::ALFVEN_SURFACE_RADII` | ALFVEN_SURFACE_RADII | 18.8 |  |  |  |  |  |
| R13 | `constants_new.py::TERMINATION_SHOCK_AU` | TERMINATION_SHOCK_AU | 94 |  |  |  |  |  |
| R14 | `constants_new.py::HELIOPAUSE_RADII` | HELIOPAUSE_RADII | 26148 |  |  |  |  |  |
| R15 | `constants_new.py::PARKER_CLOSEST_RADII` | PARKER_CLOSEST_RADII | 9.86 |  |  |  |  |  |
| R16 | `constants_new.py::MOON_RADIUS_KM` | MOON_RADIUS_KM | 1737.4 |  |  |  |  |  |
| R17 | `constants_new.py::MARS_RADIUS_KM` | MARS_RADIUS_KM | 3396.2 |  |  |  |  |  |
| R18 | `constants_new.py::SATURN_RADIUS_KM` | SATURN_RADIUS_KM | 60268 |  |  |  |  |  |
| R19 | `constants_new.py::URANUS_RADIUS_KM` | URANUS_RADIUS_KM | 25559 |  |  |  |  |  |
| R20 | `constants_new.py::NEPTUNE_RADIUS_KM` | NEPTUNE_RADIUS_KM | 24764 |  |  |  |  |  |
| R21 | `constants_new.py::BENNU_RADIUS_KM` | BENNU_RADIUS_KM | 0.246 |  |  |  |  |  |
| R22 | `constants_new.py::HAUMEA_RADIUS_KM` | HAUMEA_RADIUS_KM | 715 |  |  |  |  |  |
| R23 | `constants_new.py::ARROKOTH_RADIUS_KM` | ARROKOTH_RADIUS_KM | 9.1 |  |  |  |  |  |
