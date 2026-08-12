# Independent Cross-Check Worksheet — Batch 1 Tier 1 Sourcing

**Prompt commit:** `2ccf6839c4278f01db00fbe2101440ab267a90c2`  
**Files:** `eris_visualization_shells.py`, `venus_visualization_shells.py`  
**Cross-checker:** GPT-5.6 Thinking  
**Date:** August 2, 2026

## Completed worksheet

| # | Claim in code | Code value | Your value | Your source | Match? | Notes |
|---|---|---:|---:|---|---|---|
| E1 | Upper limit on Eris surface atmospheric pressure | ~1 nanobar | No detected N₂, Ar, or CH₄ atmosphere above approximately 1 nbar surface pressure | Sicardy et al. (2011), “A Pluto-like radius and a high albedo for the dwarf planet Eris from an occultation,” *Nature* 478, 493–496, doi:10.1038/nature10550 | YES | This is an observational upper limit, not a measured present pressure. |
| E2 | Eris atmosphere compared with Pluto’s atmosphere | ~10,000 times thinner | The same paper describes the Eris limit as about 10,000 times more tenuous than Pluto’s then-present atmosphere | Sicardy et al. (2011), *Nature* 478, 493–496, doi:10.1038/nature10550 | YES | The comparison is stated directly in the paper. |
| E3 | Temperature at Eris aphelion | around −240 °C | NASA gives an orbital surface-temperature range of about −217 to −243 °C; the cold end corresponds to the distant/aphelion part of the orbit | NASA/GSFC StarChild, “The Dwarf Planet Eris”; supporting context: Sicardy et al. (2011) used an isothermal atmospheric model near 27.7 K | APPROX | “Around −240 °C” is a sound rounded description. Temperature depends on albedo, illumination, latitude, and whether one means local or global average. |
| V1 | Venus surface atmospheric pressure versus Earth | ~90 times Earth’s | NASA currently states 93 times Earth sea-level pressure; ESA states 92 times | NASA Science, “Venus: Facts,” updated June 23, 2026; ESA, “Venus’s surface” | APPROX | “About 90 times” is acceptable rounding. |
| V2 | Venus atmospheric CO₂ composition | ~96.5% | Standard lower-atmosphere composition is approximately 96.5% CO₂ by volume | ESA, “Venus: Zwillingsplanet der Erde”; Venus International Reference Atmosphere lineage, Seiff et al. (1985) | YES | Best qualified as the conventional lower-atmosphere composition. |
| V3 | Venus atmospheric N₂ composition | ~3.5% | Standard lower-atmosphere composition is approximately 3.5% N₂ by volume | ESA, “Venus: Zwillingsplanet der Erde”; Seiff et al. (1985), Venus International Reference Atmosphere | YES | Peplowski et al. later found about 5.0 ± 0.4 vol% N₂ at 60–100 km, so the 3.5% value should not be generalized to every altitude. |
| V4 | Venus surface temperature | ~464 °C | ESA gives an average surface temperature of 464 °C | ESA, “Venus’s surface” | YES | Direct match. |
| V5 | Venus troposphere height | ~60 km | The effective tropopause varies roughly 57–63 km with latitude; many references use a 0–60 km troposphere | Sánchez-Lavega et al. (2018), “Venus Atmospheric Thermal Structure and Radiative Balance,” *Space Science Reviews* 214:88, doi:10.1007/s11214-018-0525-2 | APPROX | Sixty kilometres is a defensible rounded boundary, not a fixed global altitude. |

## Findings

E1 and E2 converge directly on Sicardy et al. (2011). The code should preserve the difference between an upper limit and a detection. “Eris has an atmosphere of about 1 nanobar” would be wrong; “occultation observations constrain any global N₂, Ar, or CH₄ atmosphere to about 1 nanobar or less” is accurate.

E3 is a reasonable rounded statement. NASA’s cited temperature range reaches about −243 °C at the cold end, while the Sicardy occultation modeling used about 27.7 K, equivalent to roughly −245.5 °C.

For Venus, V1 is approximate rather than exact because authoritative sources give 92–93 Earth atmospheres. V2 and V3 are the standard conventional lower-atmosphere values. V4 is an exact match to ESA’s stated average surface temperature. V5 is a sound rounded description of a latitude-dependent tropopause near 57–63 km.

## Source-ready annotation recommendations

```python
# Eris atmosphere:
# Source: Sicardy et al. (2011), Nature 478, 493-496,
#         doi:10.1038/nature10550
# Finding: Stellar occultation constrains any global N2, Ar, or CH4
# atmosphere to ~1 nbar surface pressure, ~10,000 times below Pluto's
# atmosphere at that time.
# Temperature context: NASA/GSFC StarChild gives an orbital surface
# temperature range of about -217 to -243 C.
```

```python
# Venus atmosphere:
# Sources:
# NASA Science, "Venus: Facts" (surface pressure ~93 Earth atmospheres)
# ESA, "Venus's surface" (surface pressure ~92x Earth; mean temperature 464 C)
# Seiff et al. (1985), Venus International Reference Atmosphere
#   (conventional lower-atmosphere composition ~96.5% CO2, ~3.5% N2)
# Sanchez-Lavega et al. (2018), Space Sci. Rev. 214:88,
#   doi:10.1007/s11214-018-0525-2
#   (effective tropopause varies roughly 57-63 km)
```

## Bottom line

E1, E2, V2, V3, and V4 match authoritative sources. E3, V1, and V5 are valid rounded approximations.

No claim requires outright rejection, but the wording should clarify that Eris’s 1 nanobar figure is an upper limit, that Venus’s 96.5/3.5 mixture is the conventional lower-atmosphere composition, and that Venus’s 60 km tropopause is approximate and latitude-dependent.
