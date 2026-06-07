# info_dictionary.py -- Gemini Fact-Check Worksheet
## Paloma's Orrery | Tony + Claude | April 18, 2026

For each claim below, please verify accuracy and provide the best
authoritative source (NASA, ESA, peer-reviewed paper, JPL, etc.).
Format your response as:

> **[Object / Line]**
> Claim: [what the code says]
> Verdict: CORRECT / INCORRECT / UNCERTAIN
> Correction (if needed): [corrected value]
> Source: [journal, NASA page, or data source]

---

## GROUP 1: ASTEROID BELT -- Trojans & Lucy Mission Targets

**Polymele (line 710-712)**
1. Polymele II discovered in 2021 from Hubble Space Telescope images
2. Lucy flyby: Sep 15, 2027
3. D~40 km
4. D-type
5. Extremely slow rotator (~446 hours)

**Orus (line 714-715)**
1. Lucy flyby: Nov 11, 2028
2. D~51 km
3. D-type
4. Last L4 Trojan visit before heading to L5

**Leucus (line 717-718)**
1. Lucy flyby: Apr 18, 2028
2. D~34 km
3. D-type
4. Fourth Trojan to be visited

---

## GROUP 2: INNER PLANETS / GAS GIANTS (INFO strings)

**Jupiter (line 722)**
1. Famous for its Great Red Spot -- this is a label, not a factual claim; skip

**Saturn (line 739)**
1. Sixth planet from the Sun -- this is correct by definition; skip

---

## GROUP 3: KUIPER BELT OBJECTS

**Charon (line 842-844)**
1. Pluto's largest moon
2. Tidally locked with Pluto, forming a binary dwarf planet system
3. Period: 6.387 days
4. Distance: 19,596 km
5. Mass ratio to Pluto: 12% (highest was 12% until Orcus-Vanth at 16%)

**Styx (line 846-847)**
1. Smallest and innermost of Pluto's known moons
2. Orbits between Charon and Nix (i.e., is it really innermost, not between Charon and Nix?)

**Nix (line 849-850)**
1. Small, elongated moon of Pluto
2. Chaotic rotation

**Kerberos (line 852-853)**
1. Pluto's second-smallest moon
2. Thought to have a double-lobed shape

**Hydra (line 855-856)**
1. Outermost known moon of Pluto
2. Elongated
3. Highly reflective, icy surface

**Hi'iaka (line 864-865)**
1. Haumea's outer moon
2. Period: 49 days
3. Diameter ~310 km
4. Named for Hawaiian goddess

**Namaka (line 867-868)**
1. Haumea's inner moon
2. Period: 18 days
3. Diameter ~170 km
4. Orbit perturbed by Hi'iaka

**Makemake (line 870)**
1. Second-brightest KBO after Pluto
2. Has one known moon (MK2)

**MK2 (line 871-872)**
1. Makemake's moon (S/2015 (136472) 1)
2. Period: 18.0 days
3. Distance: ~22,250 km
4. Orbit edge-on to Earth
5. Very dark surface (~4% reflectivity)
6. Diameter ~175 km

**Dysnomia (line 887-888)**
1. Eris's moon
2. Period: 15.79 days
3. Diameter ~700 km
4. Both bodies tidally locked

---

## GROUP 4: TRANS-NEPTUNIAN / EXTREME OBJECTS

**Sedna (line 937-949)**
1. Mean distance: 526 AU (~79 billion km)
2. Perihelion: 76 AU
3. Aphelion: 936 AU
4. Orbital period: ~11,400 years
5. Current distance at time of writing: ~83.3 AU (this is time-dependent, flag if wrong for ~2025)

**Leleakuhonua (line 951-957)**
1. Discovered in 2015
2. Horizons: 2015 TG387
3. One of the largest known semi-major axes at ~1,090 AU
4. One of four confirmed members of the Sednoid class

**Chariklo (line 959-969)**
1. Largest known centaur
2. Orbits the Sun between Jupiter and Neptune
3. Average diameter ~250 km
4. Surface: water ice, silicate minerals, organic compounds
5. First minor (not Dwarf) planet discovered to have rings, found in 2013 during a stellar occultation
6. Inner ring named Oiapoque, ~7 km wide
7. Outer ring named Chui, ~3 km wide
8. Two rings separated by a 9-km gap
9. Rings orbit at ~400 km from Chariklo's center

**Orcus (line 972-992)**
1. Aphelion: 2019 (48 AU)
2. Perihelion: ~1895/~2142 (30 AU)
3. Orbital period: 247 years
4. Diameter: ~910 km
5. Discovered Feb 17, 2004 by Brown, Trujillo, and Rabinowitz

**Vanth (line 994-1010)**
1. Orcus's moon
2. Mass ratio: 16% of Orcus (higher than Charon's 12% of Pluto)
3. Separation: 9,000 km total
4. Vanth orbits barycenter at: ~7,770 km (86.3% of separation)
5. Orcus orbits barycenter at: ~1,230 km (13.7% of separation)
6. Period: 9.54 days
7. Eccentricity: ~0.007
8. Inclination: 90 deg to ecliptic
9. ALMA 2016 resolved the barycentric orbital motion
10. Discovered Nov 2005 by Brown in Hubble images. Announced Feb 2007
11. Diameter: ~443 km (occultation 2017)

**Orcus-Vanth Barycenter (line 1012-1027)**
Claims largely duplicate Vanth/Orcus entries above -- skip unless corrections were made there.

**Gonggong (line 1041-1046)**
1. Diameter ~1230 km
2. Highly inclined orbit (30.9 deg)
3. Named after the Chinese water god known for causing floods and chaos
4. Surface is extremely red due to tholins and water ice
5. Possible past cryovolcanism
6. Slow rotation period (~22 hours) likely caused by tidal forces from its moon Xiangliu
7. Currently near aphelion at ~52.7 AU (May 2033)
8. Orbital period: 550 years
9. Eccentricity: 0.50

**Xiangliu (line 1048-1053)**
1. Gonggong's only moon
2. Named after the nine-headed serpent minister in Chinese mythology
3. Discovered 2016 by Kiss et al. in Hubble images from 2010
4. Period: 25.22 days
5. Distance: ~24,000 km
6. Diameter: ~100 km (albedo-dependent)
7. Highly eccentric orbit (e~0.29)
8. Inclined 83 deg to ecliptic

**Planet 9 (line 1055-1069)**
1. Estimated to be 7-17 Earth masses (possibly Neptune-sized)
2. At 500-700 AU from the Sun
3. Last detected in the Eridanus constellation with two observations 23 years apart (1983 IRAS and 2006 AKARI)
4. If confirmed, orbit swinging between 280-1120 AU
(NOTE: This is based on a 2025 candidate study -- may be inherently provisional. Flag which claims are from the study vs. the general Planet 9 hypothesis.)

---

## GROUP 5: MISSIONS -- SPACECRAFT

**Voyager 1 (line 1072-1086)**
1. Distance: 165.2 AU (24.7 billion km; 15.4 billion mi) as of October 2024
2. Launched September 5, 1977 from Cape Canaveral, Florida
3. Reached Jupiter: March 5, 1979
4. Reached Saturn: November 12, 1980
5. Pale Blue Dot photograph taken February 14, 1990 from a distance of 6 billion km (3.7 billion miles)
6. Overtook Pioneer 10 to become most distant human-made object: February 17, 1998
7. Crossed heliopause: August 25, 2012
8. First spacecraft to enter interstellar space
9. Discovered active volcanoes on Jupiter's moon Io (NOTE: this was Voyager 1 -- correct?)
10. "Expected to continue operating until at least 2025" -- this is stale (written pre-2025), just flag as outdated

**Apollo 11 S-IVB (line 1185-1244)**
1. Splashdown: July 24, 16:50:35 (UTC?)
2. Splashdown in Pacific Ocean 2660 km east of Wake Island, 280 [km?] south of Johnston Atoll
3. 24 km from recovery ship USS Hornet
4. Armstrong's words: "That's one small step for man, one giant leap for mankind."
   (NOTE: Armstrong said "one small step for *a* man" -- the article is often disputed; what does the
   official NASA transcript say?)
5. About 21.5 hours on the lunar surface
6. Lunar orbit insertion: July 19, 17:21:50
7. Translunar injection: July 16, 16:22:13

**Pioneer 10 (line 1246-1253)**
1. First spacecraft to travel through the asteroid belt and make direct observations
2. First to be sent to the outer solar system and first to investigate Jupiter
3. Closest approach to Jupiter: December 4, 1973 (UTC), ~2.8 Jovian radii (~200,000 km)
4. Last fully successful acquisition of signal: March 3, 2002

**JUICE (line 1258-1276)**
1. Launched April 14, 2023 @ 12:14 UTC from French Guiana (ELA-3) on an Ariane 5
2. Planned to arrive at Jupiter: July 2031
3. Will enter orbit around Ganymede: December 2034
4. Nominal mission duration: three and a half years
5. Four gravity assist flybys of Venus and Earth before Jupiter
6. Pass through the asteroid Main-Belt twice
7. First Europa flyby: July 2032

**Arrokoth (line 1127-1155)**
1. Most distant object ever visited by a spacecraft
2. Closest approach by New Horizons: January 1, 2019, at 3537.7 km, at 5:34:31 UTC
3. Size: About 36 km (22 miles) long at its longest axis
4. Discovered 2014 by the New Horizons team using the Hubble Space Telescope
5. Very red, even redder than Pluto (due to tholins)
6. Orbital period of ~13 million years for Fragment C of C/2025 K1 (skip -- different object)
7. "Recent research suggests that Arrokoth may contain sugars like ribose and glucose" -- flag if this is speculation vs. confirmed

**Artemis II (line 1607-1676)**
1. Launched April 1, 2026 22:35:12 UTC from LC-39B, Kennedy Space Center
2. Crew: Reid Wiseman (Commander), Victor Glover (Pilot), Christina Koch (Mission Specialist), Jeremy Hansen (CSA, Mission Specialist)
3. SLS: 98m tall, 2.61 million kg, 39.1 MN thrust at liftoff
4. Orion pressurized volume: 19.6 m^3
5. Orion mass to Moon: ~27,000 kg; return landing mass: ~10,400 kg
6. Maximum distance from Earth: surpassing Apollo 13's record of 400,171 km
7. Entry interface: 122 km altitude, ~10.8 km/s
8. First crewed lunar flyby since Apollo 17 in December 1972 -- over 53 years

**Gaia (line 1500-1502)**
1. Mission ended 2025-3-28

**Juno (line 1157-1179)**
1. Juno launched: August 5, 2011
2. Earth flyby: October 9, 2013
3. Jupiter arrival: July 5, 2016
4. First Ganymede flyby: June 7, 2021
5. First Europa flyby: September 29, 2022
6. First Io flyby: December 30, 2023
7. Second Io flyby: February 3, 2024
8. End of recorded orbit: February 15, 2025
9. End of mission: September 2025 by Jupiter impact
10. First spacecraft to orbit Jupiter from pole to pole
11. First spacecraft to operate on solar power at such a great distance from the Sun
12. Jupiter's magnetic field is the strongest in the solar system, generated by a layer of metallic hydrogen

---

## GROUP 6: COMETS

**Ikeya-Seki (line 1679-1691)**
1. Formally designated C/1965 S1
2. One of the brightest comets of the 20th century
3. Member of the Kreutz sungrazers
4. Discovered September 18, 1965 by Kaoru Ikeya and Tsutomu Seki
5. Perihelion: October 21, 1965
6. Passed 450,000 km (280,000 mi) above the Sun's surface
7. Nucleus fragmented into at least three pieces
8. Orbital period estimated ~880 years

**West (line 1693-1718)**
1. Formally designated C/1975 V1-A
2. Discovered by Danish astronomer Richard M. West on August 10, 1975, at the European Southern Observatory in Chile
3. Perihelion: February 25, 1976
4. Reached apparent magnitude of -3 (comparable to Venus)
5. Core broke into at least four distinct pieces in early March 1976
6. Original orbit eccentricity: ~0.999996
7. Future orbit eccentricity: ~1.00001 (escape trajectory)

**Halley (line 1720-1768)**
1. Average orbital period: 76 Earth years
2. Period has been as short as 74.42 years (1835-1910) and as long as 79.25 years (451-530)
3. Eccentricity: 0.967
4. Orbit inclined 18 degrees to the ecliptic
5. Appeared in Bayeux Tapestry (1066)
6. 1910: first time captured on camera
7. Giotto mission provided first close-up images of the nucleus (1986)
8. Perihelion: February 9, 1986
9. Closest approach to Earth: April 11, 1986 at 0.42 AU or 62.4 million km
10. Aphelion: December 9, 2023
11. Next perihelion: July 28, 2061
12. Next aphelion: November 21, 2097
13. Eta Aquarids in May and Orionids in October (Halley's meteor showers)
14. Nucleus: ~15 km long, 8 km wide, 8 km thick
15. Reflects 4% of light (one of the darkest objects in the solar system)
16. Coma can extend up to 100,000 km
17. 2061 predicted magnitude: -0.3
18. 2134 closest approach: 0.09 AU (~13 million km), predicted magnitude: -2

**Tsuchinshan-ATLAS (line 1851-1857)**
1. Discovered independently by Purple Mountain Observatory in January 2023
   and ATLAS in South Africa in February 2023
2. From the Oort Cloud (tens of thousands of years to orbit)
3. Retrograde orbit
4. Perihelion: September 27, 2024, at 0.39 AU
5. Peak magnitude: ~-4.9 in early October 2024 -- brightest comet in over 25 years
6. Closest approach to Earth: October 12, 2024, at ~0.47 AU

**67P/Churyumov-Gerasimenko (line 1859-1892)**
1. Discovered in 1969 by Klim Churyumov and Svetlana Gerasimenko
2. Jupiter-family comet
3. Likely from the Kuiper Belt
4. Size: approximately 4.3 by 4.1 km
5. Orbital period: 6.44 years
6. Next perihelion calculated as ~February 2022 (from August 2015 + 6.44 years)
7. Rosetta: first mission to orbit a comet nucleus
8. First mission to deploy a lander (Philae) onto a comet's surface
9. Rosetta escorted 67P for over two years, August 2014 to September 2016
10. Rosetta found 67P water vapor has different isotopic composition than Earth's water
11. Launch: March 2, 2004
12. Arrival at 67P: August 6, 2014
13. Philae lander deployment: November 12, 2014
14. Mission end: September 30, 2016

**ATLAS (C/2024 G3) (line 1927-1944)**
1. Discovered April 5, 2024, by the ATLAS survey
2. "Sunskirter" -- orbit takes it close to the Sun, but not as close as a sungrazer
3. Perihelion: January 13, 2025, at ~0.09 AU (14 million km)
4. "More than three times closer to the Sun than Mercury gets" -- verify Mercury perihelion distance
5. Peak apparent magnitude: ~-3.8
6. "Nucleus likely disintegrated" -- but "survived a similar close approach before, with orbital period ~160,000 years"
   (flag: these two claims may be in tension -- did the nucleus actually disintegrate or partially survive?)

---

## GROUP 7: EXOPLANET SYSTEMS

**TOI-1338 Binary (line 2090-2116)**
1. Distance: 1,292 ly
2. Instability zone: 0.18-0.35 AU
3. Binary orbital period: 14.6 days
4. TOI-1338 A: G-type, 1.1 solar masses
5. TOI-1338 B: M-type Red Dwarf, 0.3 solar masses

**TOI-1338 b (line 2117-2126)**
1. Neptune-sized planet
2. ~6.9 times larger than Earth (diameter)
3. Mass ~11.3 Earth masses
4. Discovered 2020 via transit method (TESS)
5. Found by Wolf Cukier, a 17-year-old high school intern at NASA
6. Period: ~95.2 days
7. Orbit at 0.461 AU from barycenter

**TOI-1338 c (line 2127-2134)**
1. Jupiter-mass gas giant
2. Mass ~75.4 Earth masses
3. Discovered in 2023 using Radial Velocity method
4. First detection of a circumbinary planet using RV observations alone
5. Period: ~215.5 days
6. Orbit at 0.794 AU from barycenter

**Proxima Centauri (line 2136)**
1. Nearest star
2. M5.5V red dwarf at 4.24 ly

**Proxima b (line 2137)**
1. Habitable zone
2. Nearest exoplanet
3. 11.2 day period

**Proxima d (line 2138)**
1. Sub-Earth mass (0.26 M_Earth)
2. Lightest RV-detected planet
3. 5.1 day period

---

## NOTES FOR GEMINI

- Claims marked (skip) are definitional or editorial and don't need verification.
- For Artemis II: mission is very recent (April 2026). If you can verify the SLS specs
  and crew from NASA sources, that would be ideal.
- For Halley: historical dates (1066 Bayeux Tapestry, 1910 first photograph) are well-documented
  but worth a quick confirm.
- For TOI-1338: the Wolf Cukier intern story is widely reported -- confirm details.
- Priority order: GROUP 6 (Comets, public-facing), GROUP 3/4 (KBOs -- highest error rate
  from Stage 1), GROUP 5 (Missions), GROUP 7 (Exoplanets), GROUP 1 (Lucy targets).
