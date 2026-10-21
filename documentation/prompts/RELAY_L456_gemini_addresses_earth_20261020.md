<!-- Doc-Kind: hand | Relay prompt for Gemini 4: find the open web address of each work the Earth room's citations name (L-456). Copy everything below the line into Gemini. -->
# Relay prompt for Gemini 4 -- web addresses for the Earth room's citations (L-456)

Written 2026-10-20 by Anthropic's Claude Opus 5.5 for Tony to carry to
Gemini 4. Copy everything below the line. Any effort tier will do: every
row names its work, so each is bounded (open it, find the sentence,
stop). Claude re-opens every address that comes back before it goes on
a row. The Sun room's works are a first prompt, RELAY_L456_gemini_addresses_sun_20261020.md: two shorter answers lose less if the Gemini app drops one.

---

Built on palomas_orrery e8e714da99e0ec102fe179341cf767458d2e8545 at
https://github.com/tonylquintanilla/palomas_orrery and
tonyquintanilla.github.io ca5339fd3c22d61a1540e4314726e85003e48751 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io. Every
citation below is written out here as the website serves it today, so
you do not need the repositories.
Vocabulary: v2 (2026-08-13)

## Who you are working for

Tony Quintanilla, PE, a retired civil and environmental engineer, builds
Paloma's Orrery, a 3D astronomy visualization (a desktop program and the
website palomasorrery.com), through conversation with AI partners. He is
not a professional programmer or astronomer. Please write plainly.

## The job

The website's information panel lists the sources behind each drawn
feature. Visitors should be able to tap a source and open it. These
citations name their work but carry no web address. For each WORK
below, find the address of a copy anyone can read, open it, and show
us that it is the same work and that it says what we cite it for.

## The rules this job follows

If you have imported the palomas_orrery repository, read this file and
name it at the top of your answer:
skills/provenance-discipline/SKILL.md -- sections The Access Standard
and What a Visitor Reads. If you have not imported it, say so; the
rules you need are here:

1. **Open copies first.** Prefer, in this order: the publisher's own
   open-access page; an arXiv preprint of the same paper; the NASA ADS
   abstract page; an agency's own page or document. A paywalled page is
   still worth reporting as the DOI's address, but say it is paywalled
   and keep looking for an open copy.
2. **Name what you opened.** The title and authors exactly as printed
   on the page you opened. A different paper with a similar title is a
   different work: say so.
3. **Quote it.** A short verbatim quote from the page you opened that
   carries what we cite the work for, with a locator (section, table,
   equation, page, or abstract). A row without both is recorded as
   UNVERIFIED whatever it says. If you are recalling rather than
   reading, say so and leave the row UNVERIFIED. Silence is better than
   a guess.
4. **Never build an address from memory.** Every address you report is
   one you opened in this session.

## Before any row: a pre-flight

Open this page and quote one sentence from it, so we know your fetching
works:

```
https://arxiv.org/abs/2202.11533
```

## Your answer's header

Start with one line naming your MODEL and your EFFORT TIER, then the
rule file you read (or "not imported").

## The table

One row per numbered work, in this exact layout:

| # | Work as we cite it (short) | Address opened | Access word | Title and authors as printed | Quote | Locator | Same work? | Says what we cite? | Notes |

- **Access word**: one of open full text, abstract, agency page, open
  document, paywalled, book (no open copy).
- Each verdict cell holds EXACTLY ONE token:

```
Same work?           YES  NO  UNVERIFIED
Says what we cite?   YES  NO  PARTIAL  UNVERIFIED
```

- Where a work has a DOI, also give its doi.org address in Notes, even
  when the open copy is elsewhere.
- Put every address as a bare URL inside a code block after the table,
  numbered by row. Links pasted as chips lose their address.
- Please deliver the whole answer as a downloadable Markdown file named
  worksheet_gemini4_<effort tier>_L456_earth_20261020.md, as well as in
  the chat.

## The works

Each row gives the work as our citation names it, then, after "We cite
it for:", the sentence or figure our citation rests on.

E1. Alken, P. et al. (2021), "International Geomagnetic Reference Field: the thirteenth generation", Earth Planets Space 73:49, doi:10.1186/s40623-020-01288-x
We cite it for: Table 4: the 2020.0 north geomagnetic pole at 80.65 N, -72.68 E.

E2. IGRF-13 coefficient file igrf13coeffs.txt (IAGA Working Group V-MOD, served by NOAA NCEI)
We cite it for: g(1,0) at epoch 2020.0 is -29404.8 nT. Report the file's own address, opened.

E3. Baker, D. N. et al. (2018), "Space Weather Effects in the Earth's Radiation Belts", Space Sci. Rev. 214:17, doi:10.1007/s11214-017-0452-7
We cite it for: sec. 2: inner-zone proton fluxes peak near geocentric r ~ 1.5 R_E.

E4. Baliukin, I. I., Bertaux, J.-L., Quemerais, E., Izmodenov, V. V. & Schmidt, W. (2019), "SWAN/SOHO Lyman-alpha mapping: the hydrogen geocorona extends well beyond the Moon", J. Geophys. Res. Space Physics 124, 861-885, doi:10.1029/2018JA026136
We cite it for: the geocorona is detected to at least 100 Earth radii.

E5. Dziewonski, A. M. & Anderson, D. L. (1981), "Preliminary reference Earth model", Phys. Earth Planet. Inter. 25:297-356
We cite it for: the inner core boundary at r = 1221.5 km, the core-mantle boundary at r = 3480 km, and the base of the crust at r = 6346.6 km.

E6. Folkner, W. M., Williams, J. G., Boggs, D. H., Park, R. S. & Kuchynka, P. (2014), "The Planetary and Lunar Ephemerides DE430 and DE431", IPN Progress Report 42-196
We cite it for: abstract: the inner planets' orbits are known to subkilometer accuracy.

E7. IADC Space Debris Mitigation Guidelines, IADC-02-01 REVISION 2, March 2020
We cite it for: section 3.3.2 (1): the LEO Protected Region extends from the Earth's surface to an altitude of 2,000 km; section 3.3.1 takes the equatorial radius, 6,378 km, as the reference surface.

E8. IAU 2012 Resolution B2
We cite it for: the astronomical unit's exact definition.

E9. IERS Conventions (2010), Petit & Luzum (eds.), IERS Technical Note No. 36
We cite it for: Table 1.1: the Earth's equatorial radius and the geocentric gravitational constant GM_E = 3.986004418e14 m^3 s^-2; Table 1.2: the mean Earth angular velocity 7.292115e-5 rad s^-1; sec. 2.1.1: the mean pole at J2000.0 within about 0.02 arcseconds of the ICRS pole.

E10. Jelinek, K., Nemecek, Z. and Safrankova, J. (2012), "A new approach to magnetopause and bow shock modeling based on automated region identification", J. Geophys. Res. 117, A05208, doi:10.1029/2011JA017252
We cite it for: eq. 14, p. 5: R_BS = 15.02 p^(-1/6.55); sec. 4: lambda = 1.17 for the bow shock; fig. 7: a scatter of 0.69 R_E.

E11. Li, X., Xiang, Z., Mei, Y., O'Brien, D., Brennan, D., Zhao, H., Baker, D. N. and Temerin, M. A. (2025), "A New Electron and Proton Radiation Belt Identified by CIRBE/REPTile-2 Measurements After the Magnetic Super Storm of 10 May 2024", J. Geophys. Res. Space Physics 130, e2024JA033504, doi:10.1029/2024JA033504
We cite it for: sec. 1: the outer radiation belt is most intense around L = 4 and 5.

E12. Meredith et al. (2014), doi:10.1002/2014JA020064
We cite it for: introduction: the span of the inner and outer belts, the outer belt extending to 7 Earth radii.

E13. Li, Tu et al. (2024), doi:10.1029/2023JA032171
We cite it for: introduction: the outer belt extending to 7 Earth radii.

E14. NASA Planetary Fact Sheet, Earth
We cite it for: the volumetric mean radius.

E15. Ishii, T., Huang, R., Fei, H. et al. (2018), "Complete agreement of the post-spinel transition with the 660-km seismic discontinuity", Sci. Rep. 8:6358, doi:10.1038/s41598-018-24832-y
We cite it for: the global average depth of the discontinuity is 660 +/- 10 km.

E16. NOAA JetStream, "Layers of the Atmosphere"
We cite it for: the stratosphere to about 50 km; the thermosphere from about 85 km to about 600 km, the exosphere beyond.

E17. NASA, "Earth's Atmospheric Layers"
We cite it for: the stratosphere extends to 50 km; the thermosphere extends to 600 km.

E18. Shue, J.-H., Song, P., Russell, C. T. et al. (1998), "Magnetopause location under extreme solar wind conditions", J. Geophys. Res. 103(A8), 17691-17700, doi:10.1029/98JA01103
We cite it for: Table 1 "After Fit", p. 17,698: a1 = 10.22 +/- 0.10 R_E; p. 17,697: the model's standard deviation against the crossings, 1.23 R_E.

E19. Slavin, J. A., Smith, E. J., Sibeck, D. G., Baker, D. N., Zwickl, R. D. and Akasofu, S.-I. (1985), "An ISEE 3 study of average and substorm conditions in the distant magnetotail", J. Geophys. Res. 90(A11), 10875-10895, doi:10.1029/JA090iA11p10875
We cite it for: abstract: flaring ceases on average at |X| = 120 +/- 10 R_E; a magnetotail diameter of 60 +/- 5 R_E at |X| = 130 - 225 R_E.

E20. Slavin et al. (1983), Geophys. Res. Lett. 10(10):973, doi:10.1029/GL010i010p00973
We cite it for: the magnetotail observed to 220 R_E.

E21. Sibeck and Lin (2014), J. Geophys. Res. Space Physics 119, doi:10.1002/2013JA019471
We cite it for: the distant tail is often flattened along the part of the solar wind's magnetic field that lies across the Sun-Earth line.

E22. Maezawa, Hori, Mukai, Saito, Yamamoto, Kokubun and Nishida (1997), Adv. Space Res. 20(4-5):949, doi:10.1016/S0273-1177(97)00503-6
We cite it for: GEOTAIL found the distant tail about the same size in both directions under average conditions.

E23. JPL Horizons manual, its reference frames section
We cite it for: the ICRF was built to align with FK5/J2000 and differs from it by at most 0.02 arcseconds.


## What not to do

- Do not propose wording for the website.
- Do not combine rows.
- Do not fill a cell from memory. If you could not open a page, the
  cell is UNVERIFIED and Notes says what stopped you.
