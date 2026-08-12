# Cross-Check Worksheet Prompt — `constants_new.py` Citation Verification

**Built on `225071f6184c5fe150a8cdb258a03dbe10ae2718`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Verify fresh — this is stated, not assumed.**

---

## Your role

You are an independent cross-checker for Paloma's Orrery, a Python/Plotly
solar system visualization project. Tony Quintanilla is the integrator.

## The job

**Citation verification, not value discovery.** Each constant below has a
`# Source:` citation and sometimes a `# Ref:` URL. Your task is to verify
that the cited source actually contains the stated value at the stated
precision. This is not "what is the right number" — it is "does the
citation point where it claims to point."

For each constant:
1. Go to the cited source (or a current authoritative equivalent if the
   URL is dead).
2. Confirm the value appears there at the stated precision.
3. If the source says something different, report exactly what it says.
4. If the citation is a derivation (formula-based), verify the formula
   and inputs are correct.

**Research against live authoritative sources. Use web search. Do NOT
answer from training memory — that is the failure class this entire
mechanism exists to prevent.**

## Worksheet format

Fill in one row per constant:

| # | Constant | Value | Cited source | Citation correct? | Notes |
|---|----------|-------|-------------|-------------------|-------|

"Citation correct?" means: does the stated source contain this value?
YES / NO / PARTIAL (value is there but precision differs) /
DEAD LINK (URL gone, but value confirmed elsewhere) /
DERIVED (formula-based — inputs and formula verified)

---

## Group A: Fundamental Constants

```python
KM_PER_AU = 149597870.7
# Source: IAU 2012 Resolution B2 -- exact definition
# Ref: https://syrte.obspm.fr/IAU_resolutions/Res_IAU2012_B2.pdf
# Also: https://nssdc.gsfc.nasa.gov/planetary/factsheet/fact_notes.html

SUN_RADIUS_KM = 695700.0
# Source: IAU 2015 Resolution B3 -- nominal solar radius
# Ref: Prsa et al. 2016, AJ 152:41 (arXiv:1605.09788)
# Also: https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html

SPEED_OF_LIGHT_KM_S = 299792.458
# Source: NIST/SI exact definition
# Ref: https://physics.nist.gov/cgi-bin/cuu/Value?c
```

## Group B: Earth Reference

```python
EARTH_EQUATORIAL_RADIUS_KM = 6378.137
# Source: IAU 2015 Resolution B3 -- nominal terrestrial equatorial radius
# Ref: Prsa et al. 2016, AJ 152:41 (arXiv:1605.09788)
# Also: https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html

EARTH_POLAR_RADIUS_KM = 6356.752
# Source: IAU 2015 Resolution B3 -- nominal terrestrial polar radius
# Ref: Prsa et al. 2016, AJ 152:41 (arXiv:1605.09788)
```

## Group C: Jupiter Reference

```python
JUPITER_EQUATORIAL_RADIUS_KM = 71492.0
# Source: IAU 2015 Resolution B3 -- nominal jovian equatorial radius
# Ref: Prsa et al. 2016, AJ 152:41 (arXiv:1605.09788)

JUPITER_POLAR_RADIUS_KM = 66854.0
# Source: IAU 2015 Resolution B3 -- nominal jovian polar radius
# Ref: Prsa et al. 2016, AJ 152:41 (arXiv:1605.09788)
```

## Group D: Solar Structure

```python
CORE_AU = 0.2 * SOLAR_RADIUS_AU
# Source: Standard solar model (Bahcall et al.)

RADIATIVE_ZONE_AU = 0.7 * SOLAR_RADIUS_AU
# Source: Standard solar model

CHROMOSPHERE_RADII = 1.5
# Source: Carroll & Ostlie, "Introduction to Modern Astrophysics" (2017), Ch. 11

INNER_CORONA_RADII = 3
# Source: Golub & Pasachoff, "The Solar Corona" (2010)

OUTER_CORONA_RADII = 50
# Source: Various; F-corona envelope extends to ~50 R_sun
# Ref: Mann et al. (2004), A&A 414:1127

STREAMER_BELT_RADII = 6.0
# Source: Eclipse observations; helmet streamers extend 4-6 R_sun
# Ref: Golub & Pasachoff (2010); DeForest et al. (2018)

ROCHE_LIMIT_RADII = 3.45
# Source: Fluid Roche limit formula: d = 2.44 * R * (rho_sun/rho_comet)^(1/3)
# Ref: Murray & Dermott, "Solar System Dynamics" (1999), Sec. 4.6
# Note: Code uses 3.45 R_sun. Verify the formula produces this
#       with reasonable density assumptions.

ALFVEN_SURFACE_RADII = 18.8
# Source: Parker Solar Probe first crossing, April 28, 2021
# Ref: Kasper et al. (2021), Phys. Rev. Lett. 127:255101
# Also: https://www.nasa.gov/feature/goddard/2021/nasa-enters-the-solar-atmosphere
```

## Group E: Heliosphere

```python
TERMINATION_SHOCK_AU = 94
# Source: Voyager 1 crossed at 94 AU (Dec 2004)
# Ref: Stone et al. (2005), Science 309:2017
# Also: Voyager 2 crossed at 84 AU (Aug 2007) -- asymmetric

HELIOPAUSE_RADII = 26449
# Source: Voyager 1 crossed heliopause at ~121.6 AU (Aug 2012)
# Ref: Gurnett et al. (2013), Science 341:1489
# Note: HELIOPAUSE_RADII is in solar radii. Verify the conversion:
#       121.6 AU * (149,597,870.7 km / 695,700 km) = ? R_sun

INNER_LIMIT_OORT_CLOUD_AU = 2000
# Source: Hills (1981); Oort (1950) -- inner edge estimate

INNER_OORT_CLOUD_AU = 20000
# Source: Hills (1981) -- outer edge of inner (Hills) cloud

OUTER_OORT_CLOUD_AU = 100000
# Source: Oort (1950); Weissman (1996)

GRAVITATIONAL_INFLUENCE_AU = 126000
# Source: Approximate Hill sphere radius of Sun in Milky Way
```

## Group F: Parker Solar Probe

```python
PARKER_CLOSEST_RADII = 9.86
# Source: Parker Solar Probe perihelion 22, Dec 24, 2024
# Ref: https://parkersolarprobe.jhuapl.edu/The-Mission/index.php
# Note: This was corrected from 8.86 to 9.86 in April 2026 (Gemini
#       caught the error). 9.86 R_sun = from Sun center, not surface.
#       Verify against current mission data -- PSP has completed
#       additional perihelia since Dec 2024.
```

## Group G: Body Radii (14 named constants from L-162)

Convention: equatorial for major planets, volumetric mean for small/irregular
bodies. Section sources:
```
# IAU 2015 Resolution B3 (Prsa et al. 2016) for Sun, Earth, Mars,
#   Jupiter, Saturn, Uranus, Neptune nominal values.
# NASA NSSDCA Planetary Fact Sheets for Mercury, Venus, Moon.
# JPL Solar System Dynamics for dwarf planets / small bodies.
# Nimmo et al. 2017 (Icarus) for Pluto.
# Ref: https://nssdc.gsfc.nasa.gov/planetary/factsheet/
# Ref: https://ssd.jpl.nasa.gov/planets/phys_par.html
```

```python
MERCURY_RADIUS_KM = 2439.7    # NASA Fact Sheet (volumetric mean)
VENUS_RADIUS_KM = 6051.8      # NASA Fact Sheet (volumetric mean)
MOON_RADIUS_KM = 1737.4       # NASA Fact Sheet (volumetric mean)
MARS_RADIUS_KM = 3396.2       # IAU 2015 nominal equatorial (vol = 3389.5)
PHOBOS_RADIUS_KM = 11.1       # NASA/JPL SSD
SATURN_RADIUS_KM = 60268      # IAU 2015 nominal equatorial (vol = 58232)
URANUS_RADIUS_KM = 25559      # IAU 2015 nominal equatorial (vol = 25362)
NEPTUNE_RADIUS_KM = 24764     # IAU 2015 nominal equatorial (vol = 24622)
PLUTO_RADIUS_KM = 1188.3      # New Horizons (Nimmo et al. 2017)
BENNU_RADIUS_KM = 0.262       # OSIRIS-REx (volumetric mean)
ERIS_RADIUS_KM = 1163         # Sicardy et al. 2011 occultation
HAUMEA_RADIUS_KM = 816        # Volumetric mean (1050x840x537 km)
MAKEMAKE_RADIUS_KM = 715      # Brown et al. (volumetric mean)
ARROKOTH_RADIUS_KM = 9.95     # Volumetric mean (~35x20x14 km bilobed)
```

---

## Out of scope for this worksheet

- **Derived constants** (`SOLAR_RADIUS_AU`, `LIGHT_MINUTES_PER_AU`):
  computed from primaries above — no independent citation to verify.
- **`KNOWN_ORBITAL_PERIODS` dict**: ~80+ entries with inline comments
  sourced from JPL Horizons (live pipeline). Citation verification is
  a different job (Horizons query replay), not a web-search task.
- **`COLORS`, `MARKER_SYMBOLS` dicts**: visual parameters, not
  scientific claims.
- **`CENTER_BODY_RADII` dict**: contains the same values as the Group G
  named constants — verifying the named constants covers it.

---

## What to produce

A completed worksheet with one row per constant (Groups A-G), answering:
does the cited source contain this value at this precision?

Flag anything where:
- The cited source says a different number
- The cited source doesn't exist or the URL is dead
- The citation names a source that doesn't publish this specific value
  (same issue as Mars's Hill sphere citing "NASA SSD" for a derived value)
- A derivation's inputs or formula don't produce the stated result
- The value is correct but the citation is wrong (right number, wrong provenance)

---

*Worksheet prompt prepared August 2, 2026 by Claude Opus 4.6.*
