<!-- Doc-Kind: hand | Round 1 of the L-421 build: the sources for the typed facts that had none, 2026-10-06. -->
# L-421 Round 1: sources for the typed facts

Built on orrery fbd223eee7cb8823439c17d64fa23bb5e04110eb at
https://github.com/tonylquintanilla/palomas_orrery and gallery
8487b0f84ae8ba375e24ff20e9806a1214bcb3a0 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, from
documentation/MANIFEST_L421_typed_facts_20261006.md. October 6, 2026, with
Anthropic's Claude Opus 5.5. Research only: nothing is built or changed.

## Where each item stands

| # | What | Result |
|---|---|---|
| E1, E2 | Sense of Earth's spin, Archinal et al. (2018) | NOT RE-READ. The report is behind Springer's paywall and its free-read link refuses automated access, so sections 2 and 7 could not be read this session. A 2019 correction exists (Cel. Mech. Dyn. Astr. 131:61): it fixes the sign of the node's right ascension in Figs. 1 and 2, and its corrected Fig. 1 caption still reads "W increasing = prograde". The citation should name the correction. Needs Tony's PDF, or the reprint link pasted into chat. |
| E3 | Axis circles over thousands of years and nods | SOURCED: USNO glossary (precession, nutation, true equator of date) and Williams (1994) sec. 1 and 5 (precession about 50 arcsec a year, one circle in roughly 26,000 years). Words kept. |
| E5 | Geostationary keeps pace, one longitude | SOURCED: NASA Earth Observatory, Catalog of Earth Satellite Orbits, "High Earth Orbit". Words kept. |
| E11 | Sunrise defined with refraction and disc corrections | SOURCED: USNO Rise, Set and Twilight Definitions (16 + 34 = 50 arcmin), and the USNO glossary entry. Words kept. Once-a-day sweep from the served rotation period, as planned. |
| E12 | Moon's path drifts as the Sun and Earth's shape perturb it | SOURCED: Williams (1994) sec. 1-3; USNO glossary (osculating elements, perturbations). Words kept. |
| E13 | Subsolar point is where the Sun is overhead | SOURCED: USNO glossary, "sub-solar point". The manifest's question to Tony (does a definition count as the picture's own words?) is no longer needed. |
| S1 | Inner Oort cloud "drawn flattened toward the ecliptic, as the inner cloud is thought to be" | CONTRADICTED by a 2025 source. Nesvorny et al. (2025, ApJ 983) call the flat-in-the-ecliptic disk the older portrayal (Levison et al. 2001) and find a slightly warped disk tilted about 30 degrees to the ecliptic. The served note says the same older thing, unsourced. Portegies Zwart et al. (2021) gives the cloud's distance, not its shape. Tony's ruling needed. |

Not research items, checked at build time as the manifest says: E4 (compare the
served pole_source and orbit_source with the typed copy), E6-E10, S2, S3 (served
words already say it), S4 (a drawing choice, stays typed).

## Notes as taken


## S1 inner Oort cloud "drawn flattened toward the ecliptic, as the inner cloud is thought to be"
- Portegies Zwart et al. 2021 (A&A 652 A144), read sec 1-3.1 via ar5iv: gives the Hills cloud's
  distance (sec 2.2) but says NOTHING about its shape. Not a source for "flattened".
- Nesvorny, Dones, Vokrouhlicky, Levison, Beauge, Faherty, Emmart, Parker (2025),
  "A Spiral Structure in the Inner Oort Cloud", ApJ 983:1 (published 2025-04-08),
  arXiv:2502.11252v1, read in full (html) 2026-10-06:
  - Sec 1: the inner cloud "is therefore often portrayed as a relatively flat disk,
    roughly aligned with the ecliptic (Levison et al. 2001)".
  - Sec 1 and sec 5: their result -- a slightly warped disk ~15,000 au across,
    inclined ~30 deg to the ecliptic (nearly polar to the Galactic plane), seen
    from afar as a two-armed spiral; main axis aligned with the ecliptic, ends
    twisted away from it (sec 2).
- FINDING: the hover and the served note state the older picture as current.
  Tony's call (what the room shows), not method.

## E11 terminator: sunrise rule
- USNO Astronomical Applications Dept, "Rise, Set, and Twilight Definitions",
  https://aa.usno.navy.mil/faq/RST_defs, read in full 2026-10-06:
  sunrise/sunset conventionally = upper edge of the Sun's disk on the horizon,
  average atmosphere; for computation the Sun's centre is 50 arcmin below the
  horizontal plane = 16 arcmin average apparent radius + 34 arcmin average
  refraction at the horizon. SOURCED. Our sentence ("refraction and solar-disc
  corrections that define sunrise on the ground are not applied") matches it.
- "sweeps around once a day": manifest says derive from the served rotation
  period; USNO also states the Earth's rotation once a day causes rise and set.

## USNO glossary -- "Glossary", consistent with The Astronomical Almanac 2023,
## https://aa.usno.navy.mil/faq/asa_glossary, read in full 2026-10-06
- E13 subsolar point: "sub-solar point" = the point on a body's surface directly
  beneath the Sun on the line from the body's centre to the Sun's; for a round
  body the Sun is at the zenith there. SOURCED -> no need to ask Tony whether a
  definition counts as the picture's own words.
- E11 also: "sunrise, sunset" entry repeats 90 deg 50' = 34' horizontal
  refraction + 16' semidiameter. Second source for E11.
- E3 axis circles and nods: "precession" = smoothly changing orientation of a
  rotating body's equator; for Earth driven by Sun and Moon pulling on the
  equatorial bulge. "nutation" = oscillations of the rotation pole, in obliquity
  and longitude. "true equator and equinox" = of a date, affected by both.
  So "circles ... and nods slightly, so the pole and tilt belong to that date"
  is SOURCED. "over thousands of years" (the timescale) is NOT in the glossary.
- E12 Moon arc: "osculating elements" = the two-body orbit a body would follow if
  perturbations ceased; "perturbations" = deviations of the actual orbit from the
  reference orbit. Supports "the real path drifts from the two-body orbit".
  NOT sourced here: the named causes, "the Sun and Earth's shape".
- terminator: "the boundary between the illuminated and dark areas of a body".

## E5 geostationary ring "satellites here keep pace with Earth's turning and hang over one longitude"
- NASA Earth Observatory, Riebeek (2009, page updated 2025-11-14), "Catalog of
  Earth Satellite Orbits", sec "High Earth Orbit",
  https://science.nasa.gov/earth/earth-observatory/catalog-of-earth-satellite-orbits/
  read in full 2026-10-06: at 42,164 km from Earth's centre the orbit matches
  Earth's rotation, so the satellite seems to stay over a single longitude;
  circular and over the equator (zero eccentricity and inclination) it is
  geostationary, always over the same place. SOURCED, words kept.

## Williams, J. G. (1994), "Contributions to the Earth's obliquity rate,
## precession, and nutation", AJ 108(2):711, doi:10.1086/117108,
## https://articles.adsabs.harvard.edu/pdf/1994AJ....108..711W, read in full 2026-10-06
- E12 Moon arc: sec 1 -- the lunar orbit is inclined 5 deg to the ecliptic and
  strong solar torques drive the precession of its plane along the ecliptic
  with an 18.6 yr period; Earth's oblateness contributes a small torque trying
  to precess it along the equator. Sec 2 -- "the lunar orbit is strongly
  perturbed by the Sun". Sec 3 -- J2 (Earth's flattening) perturbations in
  lunar latitude and longitude. (Planets also perturb it, smaller; our sentence
  names two causes and does not claim they are all.) SOURCED, words kept.
- E3 timescale: sec 1 -- torques of Sun and Moon on the oblate Earth make the
  equator precess and nutate; precession is retrograde at ~50"/yr (sec 5:
  general precession 50.2877"/yr at J2000 adopted). 360 deg at that rate is
  ~25,800 yr -> "slowly circles over thousands of years" is SOURCED as a
  consequence of a stated rate. Sec 8: long-period terms exceed 10,000 yr.
  Note for build: if the hover ever prints the period, it needs a derived row
  with figures; the words as they stand print no number.
