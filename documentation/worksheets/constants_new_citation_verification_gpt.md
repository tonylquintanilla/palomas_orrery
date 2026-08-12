# Independent Cross-Check Worksheet — `constants_new.py` Citation Verification

**Pinned prompt commit:** `225071f6184c5fe150a8cdb258a03dbe10ae2718`  
**Cross-checker:** GPT-5.6 Thinking  
**Date:** August 2, 2026

## Scope and method

This worksheet answers the narrow provenance question posed in the prompt: **does the named citation contain or directly support the stated value at the stated precision?** It does not silently substitute a better source merely because the number itself is reasonable.

The public GitHub repository could not be fetched from the execution container because outbound DNS resolution was unavailable there. The commit and constants below therefore follow the supplied orchestration prompt. All scientific checks were made independently against live authoritative webpages, journal records, or papers; the pre-existing Gemini worksheet was not consulted.

Status meanings follow the prompt: **YES**, **NO**, **PARTIAL**, **DEAD LINK**, or **DERIVED**.

## Worksheet

| # | Constant | Value | Cited source | Citation correct? | Notes |
|---:|---|---:|---|---|---|
| 1 | `KM_PER_AU` | 149,597,870.7 km | IAU 2012 Resolution B2 | **YES** | Resolution B2 defines 1 au as exactly 149,597,870,700 m, which is exactly 149,597,870.7 km. |
| 2 | `SUN_RADIUS_KM` | 695,700.0 km | IAU 2015 Resolution B3 / Prša et al. 2016 | **YES** | The nominal solar radius is exactly \(6.957\times10^8\) m = 695,700 km. |
| 3 | `SPEED_OF_LIGHT_KM_S` | 299,792.458 km/s | NIST / SI definition | **YES** | NIST fixes \(c=299,792,458\) m/s exactly, equivalent to 299,792.458 km/s. |
| 4 | `EARTH_EQUATORIAL_RADIUS_KM` | 6,378.137 km | IAU 2015 Resolution B3; NASA fact sheet also cited | **PARTIAL** | IAU B3’s **nominal terrestrial equatorial radius** is 6,378.1 km, not 6,378.137 km. The more precise 6,378.137 km is an Earth reference-ellipsoid/fact-sheet value, so the number can be supported by the secondary “Also” citation but not by the named IAU nominal constant. |
| 5 | `EARTH_POLAR_RADIUS_KM` | 6,356.752 km | IAU 2015 Resolution B3 / Prša et al. 2016 | **NO** | IAU B3’s nominal terrestrial polar radius is 6,356.8 km. The code value is a more precise measured/reference-ellipsoid value, not the IAU nominal value cited. |
| 6 | `JUPITER_EQUATORIAL_RADIUS_KM` | 71,492 km | IAU 2015 Resolution B3 / Prša et al. 2016 | **YES** | This is the nominal jovian equatorial radius. |
| 7 | `JUPITER_POLAR_RADIUS_KM` | 66,854 km | IAU 2015 Resolution B3 / Prša et al. 2016 | **YES** | This is the nominal jovian polar radius. |
| 8 | `CORE_AU` | \(0.2R_\odot\) | “Standard solar model (Bahcall et al.)” | **PARTIAL** | Standard solar descriptions commonly place the nuclear-energy-producing core within roughly the inner 20–25% of the solar radius. The value is a defensible rounded visualization boundary, but “Bahcall et al.” is not a sufficiently specific citation to verify an exact 0.200 boundary. |
| 9 | `RADIATIVE_ZONE_AU` | \(0.7R_\odot\) | Standard solar model | **PARTIAL** | Helioseismic/standard models place the base of the convection zone near \(0.713R_\odot\). A 0.7 boundary is a rounded approximation, not the source value at the stated one-decimal precision if interpreted as exact. |
| 10 | `CHROMOSPHERE_RADII` | \(1.5R_\odot\) | Carroll & Ostlie (2017), Ch. 11 | **NO** | The chromosphere is only thousands of kilometres thick above the photosphere, so its ordinary outer radius is near \(1.00R_\odot\), not \(1.5R_\odot\). The cited textbook does not support 1.5 solar radii as the chromosphere’s physical radius. |
| 11 | `INNER_CORONA_RADII` | \(3R_\odot\) | Golub & Pasachoff (2010) | **PARTIAL** | The corona has no sharp universal “inner-corona outer boundary.” Three solar radii is plausible as a visualization cutoff, but the citation as given does not establish it as a uniquely defined constant. |
| 12 | `OUTER_CORONA_RADII` | \(50R_\odot\) | Mann et al. (2004), A&A 414:1127; “F-corona envelope” | **PARTIAL** | The F-corona is observed to very large elongations and can be discussed at tens of solar radii, but 50 \(R_\odot\) is a selected envelope/cutoff rather than a sharply defined boundary published as this constant. The provenance wording overstates precision. |
| 13 | `STREAMER_BELT_RADII` | \(6R_\odot\) | Golub & Pasachoff; DeForest et al. | **YES** | Outer-corona observations explicitly track structured streamer material beyond 6 solar radii. The value is supportable as the upper end of the cited 4–6 \(R_\odot\) visualization range. |
| 14 | `ROCHE_LIMIT_RADII` | \(3.45R_\odot\) | Fluid Roche formula; Murray & Dermott | **DERIVED** | Using \(d=2.44R_\odot(\rho_\odot/\rho_c)^{1/3}\), \(\rho_\odot\approx1.409\) g/cm³ and a representative comet density \(\rho_c\approx0.50\) g/cm³ gives \(d\approx3.45R_\odot\). The value is correct only with the density assumption stated; it is not a universal comet Roche limit. |
| 15 | `ALFVEN_SURFACE_RADII` | \(18.8R_\odot\) | Kasper et al. (2021), PRL 127:255101 | **YES** | The first Parker Solar Probe crossing is reported at about 18.8 solar radii in the paper’s event analysis. It is one crossing location, not a fixed spherical surface. |
| 16 | `TERMINATION_SHOCK_AU` | 94 AU | Stone et al. (2005); Voyager 1 | **YES** | NASA and the Voyager literature report Voyager 1 crossing the termination shock in December 2004 at about 94 AU. |
| 17 | `HELIOPAUSE_RADII` | 26,449 \(R_\odot\) | Voyager 1 heliopause at 121.6 AU; conversion from AU and nominal solar radius | **NO** | The stated inputs give \(121.6\times149,597,870.7/695,700=26,147.91R_\odot\), not 26,449. The code value corresponds to roughly 123.0 AU. |
| 18 | `INNER_LIMIT_OORT_CLOUD_AU` | 2,000 AU | Hills (1981); Oort (1950) | **PARTIAL** | Modern NASA summaries place the inner edge in a broad range, commonly 2,000–5,000 AU, while some descriptions allow about 1,000 AU. Thus 2,000 AU is a defensible lower estimate, not a uniquely established boundary. |
| 19 | `INNER_OORT_CLOUD_AU` | 20,000 AU | Hills (1981) | **PARTIAL** | “Inner/Hills cloud” boundaries are model-dependent, and the supplied citation is not specific enough to verify 20,000 AU as an exact outer edge. It is within ranges used in parts of the literature but should be labeled approximate/model-dependent. |
| 20 | `OUTER_OORT_CLOUD_AU` | 100,000 AU | Oort (1950); Weissman (1996) | **YES** | NASA’s current summary gives an estimated outer edge as far as about 100,000 AU. This is explicitly an estimate, not a measured boundary. |
| 21 | `GRAVITATIONAL_INFLUENCE_AU` | 126,000 AU | “Approximate Hill sphere radius of Sun in Milky Way” | **NO** | No specific source is cited, and a Galactic tidal/Hill radius depends on the adopted Galactic model and definition. The number may be a plausible order-of-magnitude estimate, but the citation does not point to a verifiable published value. |
| 22 | `PARKER_CLOSEST_RADII` | \(9.86R_\odot\) from Sun center | JHU/APL mission page; Dec. 24, 2024 perihelion | **PARTIAL** | Current NASA reporting gives about 3.8 million miles (about 6.1–6.2 million km) **above the solar surface**. Adding one nominal solar radius and converting gives roughly 9.8–9.9 \(R_\odot\) from center, so 9.86 is consistent with more precise trajectory data. However, the commonly displayed mission-page figure is surface altitude and does not itself directly state 9.86 center radii. Later perihelia through June 8, 2026 matched, rather than surpassed, this record distance. |
| 23 | `MERCURY_RADIUS_KM` | 2,439.7 km | NASA NSSDCA fact sheet, volumetric mean | **YES** | The NASA fact-sheet convention supports 2,439.7 km as Mercury’s mean radius. Current JPL physical parameters list 2,439.4 ± 0.1 km, so the citation should remain specifically tied to the NASA fact sheet rather than generalized to current JPL. |
| 24 | `VENUS_RADIUS_KM` | 6,051.8 km | NASA NSSDCA fact sheet, volumetric mean | **YES** | NASA/JPL tables give 6,051.8 km. |
| 25 | `MOON_RADIUS_KM` | 1,737.4 km | NASA NSSDCA / JPL satellite parameters | **YES** | JPL gives a mean radius of 1,737.4 ± 0.1 km. |
| 26 | `MARS_RADIUS_KM` | 3,396.2 km | IAU 2015 Resolution B3, described as nominal equatorial | **NO** | IAU 2015 B3 does not establish a nominal Martian radius. The numerical value is a conventional/NASA equatorial radius, but the stated IAU provenance is wrong. |
| 27 | `PHOBOS_RADIUS_KM` | 11.1 km | NASA/JPL SSD | **PARTIAL** | JPL’s current satellite table gives mean radius 11.08 ± 0.04 km. The code value is correctly rounded to one decimal, but does not appear at the same precision. |
| 28 | `SATURN_RADIUS_KM` | 60,268 km | IAU 2015 Resolution B3, described as nominal equatorial | **NO** | IAU B3 defines nominal solar, terrestrial, and jovian conversion constants, not a nominal Saturn radius. The number is a standard NASA equatorial radius, but the cited provenance is wrong. |
| 29 | `URANUS_RADIUS_KM` | 25,559 km | IAU 2015 Resolution B3, described as nominal equatorial | **NO** | The numerical value is the standard equatorial radius used by NASA fact sheets, but it is not an IAU 2015 B3 nominal constant. |
| 30 | `NEPTUNE_RADIUS_KM` | 24,764 km | IAU 2015 Resolution B3, described as nominal equatorial | **NO** | The numerical value is the standard equatorial radius used by NASA fact sheets, but it is not an IAU 2015 B3 nominal constant. |
| 31 | `PLUTO_RADIUS_KM` | 1,188.3 km | Nimmo et al. (2017), New Horizons | **YES** | New Horizons-derived work and JPL’s current physical-parameter table give 1,188.3 km. |
| 32 | `BENNU_RADIUS_KM` | 0.262 km | OSIRIS-REx, “volumetric mean” | **NO** | Published pre-encounter mean diameter was about 492 m, implying a mean radius near 0.246 km. A 0.262 km figure is not the volumetric-mean radius supported by the cited OSIRIS-REx characterization. |
| 33 | `ERIS_RADIUS_KM` | 1,163 km | Sicardy et al. (2011) occultation | **YES** | The paper reports \(1,163\pm6\) km. |
| 34 | `HAUMEA_RADIUS_KM` | 816 km | “Volumetric mean (1050×840×537 km)” | **NO** | Treating those three numbers as semiaxes gives a geometric-mean radius of about 779.5 km, not 816 km. Current JPL’s adopted mean radius is 715 km, reflecting a different shape solution. The stated dimensions do not derive the stated radius. |
| 35 | `MAKEMAKE_RADIUS_KM` | 715 km | Brown et al., volumetric mean | **PARTIAL** | Current JPL gives a mean radius of 714 ± 7 km, so 715 km is numerically consistent. “Brown et al.” is too incomplete to verify that the named paper itself publishes 715 km at this precision. |
| 36 | `ARROKOTH_RADIUS_KM` | 9.95 km | “Volumetric mean (~35×20×14 km bilobed)” | **NO** | A simple ellipsoid calculation from 35×20×14 km gives an equivalent radius about 10.70 km, not 9.95 km. More importantly, the modern merged shape model gives volume 3,185 km³ and volume-equivalent diameter 18.26 km, hence radius 9.13 km. |

## Calculations checked

### Heliopause conversion

\[
121.6\ {\rm AU}\times
\frac{149,597,870.7\ {\rm km/AU}}{695,700\ {\rm km}/R_\odot}
=26,147.91R_\odot
\]

Therefore `HELIOPAUSE_RADII = 26449` does not follow from the stated inputs.

### Solar Roche limit

For a fluid body:

\[
d=2.44R_\odot
\left(\frac{\rho_\odot}{\rho_{\rm comet}}\right)^{1/3}
\]

Using \(\rho_\odot=1.409\ {\rm g\,cm^{-3}}\) and
\(\rho_{\rm comet}=0.50\ {\rm g\,cm^{-3}}\):

\[
d=2.44(1.409/0.50)^{1/3}R_\odot\approx3.45R_\odot
\]

### Haumea dimensions supplied in the comment

\[
(1050\times840\times537)^{1/3}=779.5\ {\rm km}
\]

This does not yield 816 km.

### Arrokoth

The simple ellipsoid implied by full dimensions 35×20×14 km gives:

\[
r_{\rm eq}=\frac{(35\times20\times14)^{1/3}}{2}
=10.70\ {\rm km}
\]

The later merged shape model is preferable: volume-equivalent diameter 18.26 km, or radius 9.13 km.

## Recommended provenance corrections

The most consequential fixes are provenance fixes rather than necessarily code-value fixes. Earth’s 6,378.137/6,356.752 km values should cite an Earth ellipsoid or NASA fact-sheet source, not IAU nominal radii. Mars, Saturn, Uranus, and Neptune should cite NASA/NSSDCA or another explicit planetary physical-parameter table, because IAU 2015 Resolution B3 is not their source.

`HELIOPAUSE_RADII` should either be changed to approximately 26,148 for a stated 121.6 AU crossing, or its AU premise should be changed to approximately 123.0 AU. `BENNU_RADIUS_KM`, `HAUMEA_RADIUS_KM`, and `ARROKOTH_RADIUS_KM` require substantive re-evaluation because the cited derivations do not produce the code values.

`CHROMOSPHERE_RADII`, `INNER_CORONA_RADII`, `OUTER_CORONA_RADII`, and `STREAMER_BELT_RADII` would be cleaner if labeled explicitly as visualization cutoffs rather than physical constants with sharply defined boundaries.

## Principal sources consulted

IAU, 2012 Resolution B2, redefinition of the astronomical unit.

Prša et al. (2016), *Nominal Values for Selected Solar and Planetary Quantities*, AJ 152:41.

NIST, SI base-unit definitions and fixed speed of light.

NASA Science, Voyager mission overview and interstellar mission pages.

NASA Science, Oort Cloud facts.

Kasper et al. (2021), *Parker Solar Probe Enters the Magnetically Dominated Solar Corona*, PRL 127:255101.

NASA Science, Parker Solar Probe close-approach reports through June 8, 2026.

JPL Solar System Dynamics, Planetary Physical Parameters and Planetary Satellite Physical Parameters.

Sicardy et al. (2011), *A Pluto-like radius and a high albedo for the dwarf planet Eris from an occultation*, Nature 478.

Lauretta et al. (2015), OSIRIS-REx Bennu physical characterization.

Keane et al. (2022), Arrokoth merged shape model and bulk properties.
