# Independent Citation Verification — `constants_new.py` Remaining Items

**Prompt commit:** `225071f6184c5fe150a8cdb258a03dbe10ae2718`  
**State reviewed:** Post-patch values and citations supplied in the prompt  
**Cross-checker:** GPT-5.6 Thinking  
**Date:** August 2, 2026

## Method and limitation

This review distinguishes between two different findings: **citation verified**, meaning the named source itself was accessible and directly supports the claim; and **value defensible**, meaning an authoritative source supports the number or approximation but the named citation could not be confirmed.

I could verify the papers and authoritative web references described below. I could not inspect the full searchable text of *The Solar Corona* (Golub & Pasachoff, 2010) or *An Introduction to Modern Astrophysics* (Carroll & Ostlie, 2017). I therefore do not claim that either book contains wording I could not directly see.

## Completed worksheet

| # | Constant | Value | Cited source | Citation correct? | Notes |
|---:|---|---:|---|---|---|
| 1 | `CORE_AU` | `0.2 * SOLAR_RADIUS_AU` | “Standard solar model (Bahcall et al.)” | **PARTIAL** | A solar core boundary is definition-dependent. NASA descriptions normally place the fusion core at about the inner **25%** of the solar radius, not specifically 0.20. Standard solar-model tables from Bahcall and collaborators provide radial luminosity-generation profiles, but they do not establish 0.20 R_sun as a unique structural boundary. The value 0.20 is defensible as the lower end of the common 0.20–0.25 convention, or as a visualization boundary, but “Bahcall et al.” is too vague and should not be presented as though a specific model reports an exact 0.200 boundary. |
| 2 | `RADIATIVE_ZONE_AU` | `0.7 * SOLAR_RADIUS_AU` | “Standard solar model” | **YES, AS ROUNDED** | Helioseismology locates the base of the convection zone at approximately 0.713 R_sun; NASA summaries describe the radiative zone as ending near 0.70–0.71 R_sun. Thus 0.7 is a conventional one-significant-digit visualization approximation. The citation should be made specific, preferably Christensen-Dalsgaard, Gough & Thompson (1991), with NASA/Marshall as an accessible explanatory source. |
| 3 | `INNER_CORONA_RADII` | `3` | Golub & Pasachoff, *The Solar Corona* (2010) | **UNVERIFIED / VALUE DEFENSIBLE** | I could not inspect the relevant book passage, so the book citation itself is not verified. The literature does not define a sharp universal inner/outer-corona transition at exactly 3 R_sun. However, “inner corona to 3 R_sun” is a defensible observational or instrument-domain cutoff: modern work explicitly describes and models the outer corona over roughly 1.5–3.1 R_sun. The code’s added label “visualization boundary” is appropriate and should be retained. |
| 4 | `STREAMER_BELT_RADII` | `6.0` | Golub & Pasachoff (2010); DeForest et al. (2018) | **PARTIAL / CITATION NEEDS CORRECTION** | Six solar radii is defensible as a visualization extent, but the identifiable DeForest source is **DeForest, Howard & McComas (2014)**, not 2018. That paper detected inbound motions beyond 6 R_sun and inferred an Alfvén-surface lower bound of about 17 R_sun in the streamer belt. It therefore proves that streamer-belt coronal structure persists beyond 6 R_sun, but it does not define helmet streamers as ending at 6 R_sun or establish a conventional 4–6 R_sun boundary. Five R_sun is not intrinsically more correct; 6 R_sun is reasonable as a selected display cutoff. |
| 5 | `MOON_RADIUS_KM` | `1737.4` km | NASA Fact Sheet, volumetric mean | **YES** | JPL Solar System Dynamics directly gives the Moon’s mean radius as **1737.4 ± 0.1 km** and defines “mean radius” as the radius of a sphere having equivalent volume. This independently confirms both the value and the volumetric-mean convention. The NASA NSSDCA attribution is consistent, but JPL SSD is the strongest directly verified citation. |
| 6 | Group D chromosphere/photospheric-radius note | `CHROMOSPHERE_RADII = 1.1` as a visualization shell | Carroll & Ostlie (2017), Ch. 11; NASA Sun material | **BOOK UNVERIFIED; 1.5 PHYSICALLY UNSUPPORTED** | I could not verify the text of Carroll & Ostlie Chapter 11. Authoritative NASA and NOAA descriptions place the ordinary chromosphere only about 2,000–2,100 km above the photosphere, corresponding to roughly 1.003 R_sun; dynamic spicules can reach about 10,000 km, still only about 1.014 R_sun. Nothing found supports interpreting the physical chromosphere as extending to 1.5 R_sun. The revised 1.1 R_sun value is therefore acceptable only as an explicitly exaggerated visualization shell, not as the physical chromospheric boundary. |

## Findings and recommended citation wording

### Solar core boundary

The standard solar model does not yield one invariant “core radius” unless “core” is operationally defined. It can mean the region of significant fusion, the radius containing a selected percentage of luminosity generation, the neutrino-production region, or a pedagogical structural layer. NASA’s solar-physics material says nuclear burning is almost completely shut off beyond approximately 25% of the solar radius. Accordingly, 0.20 R_sun is best described as the lower end of a common 0.20–0.25 convention, not as a uniquely demonstrated Bahcall-model boundary.

Bahcall, Pinsonneault & Basu (2001) and Bahcall, Serenelli & Basu (2005) are appropriate standard-model sources for radial physical and luminosity profiles. They are not clean citations for the standalone sentence “the core extends to 0.2 R_sun.” For code provenance, an accessible NASA structural description is more direct.

I could not verify whether Carroll & Ostlie chooses 0.20 or 0.25 in its solar-interior discussion.

### Radiative-zone boundary

The 0.7 value is a rounded version of the helioseismic boundary near 0.713 R_sun. Christensen-Dalsgaard, Gough & Thompson reported a convection-zone depth of 0.287 ± 0.003 R_sun, which places its base at 0.713 ± 0.003 R_sun. Later analyses obtained approximately 0.713 ± 0.001 R_sun.

A better code citation would be:

```python
RADIATIVE_ZONE_AU = 0.7 * SOLAR_RADIUS_AU
# Derived/rounded: base of solar convection zone is ~0.713 R_sun
# Source: Christensen-Dalsgaard, Gough & Thompson (1991), ApJ 378:413
# Also: NASA/Marshall Solar Physics, "The Solar Interior"
```

### Inner-corona boundary

I found no evidence of a sharp conventional transition at 3 R_sun. Coronal classifications vary with wavelength, observing technique, and scientific purpose. Three solar radii is nevertheless a sensible visualization boundary: observational papers explicitly refer to the 1.5–3.1 R_sun domain as the outer corona.

The code comment should therefore avoid saying the book defines the inner K-corona as ending at 3 R_sun unless the exact book page is supplied. A safer annotation is:

```python
INNER_CORONA_RADII = 3
# Visualization boundary, not a sharp physical transition.
# Outer-corona observations commonly treat the ~1.5-3 R_sun domain separately.
# Ref: Del Zanna et al. (2018), "Predicting the COSIE-C Signal
#      from the Outer Corona up to 3 Solar Radii"
```

### Streamer-belt extent

The DeForest citation appears to have the wrong year and to be characterized too narrowly. The relevant paper is DeForest, Howard & McComas (2014), *Inbound waves in the solar corona: a direct indicator of Alfvén surface location*. It reports inbound motion beyond 6 R_sun and a streamer-belt Alfvén-surface lower bound near 17 R_sun.

That supports the existence of structured streamer-belt corona beyond 6 R_sun; it does not say helmet streamers physically terminate at 4–6 R_sun. Eclipse observations likewise show white-light corona and streamer structure much farther out under suitable processing. Consequently, 6.0 is defensible as an upper display boundary, but not as a physical streamer endpoint.

Suggested wording:

```python
STREAMER_BELT_RADII = 6.0
# Visualization cutoff; streamer-belt structure remains observable beyond 6 R_sun.
# Ref: DeForest, Howard & McComas (2014), ApJ 787:124
```

### Moon radius

Confirmed. JPL lists the Moon’s mean radius as 1737.4 ± 0.1 km and explicitly defines this as the radius of a sphere with the same volume as the satellite. No correction is needed.

Suggested wording:

```python
MOON_RADIUS_KM = 1737.4
# Source: JPL SSD Planetary Satellite Physical Parameters
# Mean/volume-equivalent radius: 1737.4 +/- 0.1 km
```

### Chromosphere and the former 1.5 R_sun citation

NASA describes the chromosphere as approximately 400–2,100 km above the visible solar surface. NASA’s Imagine the Universe and NOAA give an approximately 2,000 km thickness. Even descriptions that include tall spicules reach about 10,000 km, far below 0.5 solar radius.

A 1.5 R_sun chromosphere would imply a height of roughly 348,000 km above the photosphere, which is incompatible with these definitions. It may have arisen from confusing chromospheric features or prominences with the chromosphere itself, or from assigning an intentionally oversized graphical shell. I found no source-based reason to attribute it to Carroll & Ostlie.

The revised 1.1 R_sun shell is still about 69,570 km above the photosphere, much larger than the physical chromosphere. It should be annotated unmistakably as a visual shell:

```python
CHROMOSPHERE_RADII = 1.1
# Visualization shell only; not the physical chromosphere thickness.
# The physical chromosphere extends roughly 2,000 km above the photosphere
# (~1.003 R_sun), with dynamic spicules reaching higher.
# Ref: NASA, "Layers of the Sun"; NASA Imagine the Universe, "The Chromosphere"
```

## Bottom line

The Moon radius is fully verified. The radiative-zone value is verified as a rounded approximation. The 0.2 core boundary is defensible only as a convention or selected visualization boundary, not as a uniquely identified Bahcall-model output.

The 3 R_sun inner-corona and 6 R_sun streamer values are reasonable visualization choices, but neither should be presented as a sharp physical boundary. The DeForest citation should be corrected from 2018 to 2014 and its evidentiary role described accurately.

The former 1.5 R_sun chromosphere attribution is unsupported. The revised 1.1 R_sun value must remain labeled as an intentionally enlarged visualization shell because the physical chromosphere is near 1.003 R_sun.
