# Provenance Worksheet -- Final Round
## Paloma's Orrery | Tony + Claude | April 18, 2026

This covers:
- The one genuine Tier 1 uncited display string (Oort Cloud hover text)
- Tier 2 genuine gaps: star_notes stellar parameters, Uranus radiation belts

NOTE: 15 of the 16 Tier 1 scanner findings were false positives --
code lines (variable assignments, np.radians calls) and module
docstrings, not display strings. Only the Oort Cloud entry below
is a real uncited display string.

spacecraft_encounters.py Tier 2 lines 235/266 are also false positives:
they already carry `'source': 'NASA/JSC'` as a dict value -- the scanner
missed it because it's not a `# Source:` comment. No action needed there.

---

## GROUP A: Solar Shells -- Oort Cloud Hover Text
## (solar_visualization_shells.py, ~line 1694)

**Oort Cloud structure and population**
1. Hills Cloud (Inner Oort): 2,000-20,000 AU, disk-like/toroidal shape
2. Outer Oort Cloud: 20,000-100,000+ AU, roughly spherical but clumpy
3. Contains an estimated 1-100 trillion objects >1 km diameter
4. Jupiter-family comets indicate inner disk-like region
5. Sedna described as possible inner Oort Cloud member
6. 2012 VP113 described as evidence for inner Oort population

---

## GROUP B: star_notes.py -- Orion Belt Stars and Others
## (lines 756, 769, 782, 795, 808, 835, 897, 926, 973)

**Bellatrix (line 756)**
1. Third brightest star in Orion (after Rigel and Betelgeuse)
2. 27th brightest star in the entire night sky
3. Spectral type B2 III (blue giant)

**Mintaka (line 769)**
1. Multiple star system of six or more stars
2. Mintaka Aa1 and Aa2 are close binary stars; Ab is more distant

**Alnilam (line 782)**
1. Fourth brightest star in Orion
2. 29th brightest star in the night sky
3. Spectral type B0 Ia (blue supergiant)
4. Distance: ~2,000 light-years from Earth

**Alnitak (line 795-808)**
1. Easternmost star in Orion's Belt
2. Distance: ~817 light-years from Earth
3. Triple star system (Aa, Ab, B)
4. Alnitak Aa is a hot blue supergiant
5. Possible eclipsing binary (Aa and Ab)

**Fomalhaut (line 897)**
1. Brightest star in Piscis Austrinus (the Southern Fish)

**Zeta Puppis / Naos region (line 926)**
1. Described as likely ending life in supernova, leaving neutron star
   or black hole (claim about stellar evolution fate)

**Shaula / Lambda Scorpii (line 973)**
1. Spectral type B1.5 IV (blue subgiant)
2. Multiple star system of at least three stars
3. Known for rapid rotation causing flattened shape

---

## GROUP C: uranus_visualization_shells.py
## (lines 534, 563 -- same string repeated in two functions)

**Uranus radiation belts**
1. Radiation belts believed to extend roughly from 3 to 10 R (Uranus radii)
2. Some models suggest they might extend beyond this range
3. Most intense regions within 10 R
4. Belts are likely asymmetric due to complex magnetic field
5. Understanding primarily based on a single flyby from Voyager 2

---

## NOTES FOR GEMINI

- GROUP A: These are consensus Oort Cloud figures. The 1-100 trillion
  estimate and the Hills Cloud/Outer Oort boundaries are standard but
  worth a source citation.
- GROUP B: Star parameters (spectral types, distances, brightness ranks)
  drift as catalogs improve. Please cite the most current authoritative
  source (SIMBAD, Hipparcos, Gaia DR3, or standard star atlases).
- GROUP C: Uranus radiation belt knowledge is genuinely limited --
  Voyager 2 is the only spacecraft to have visited. Please confirm the
  3-10 R extent figure and note what source this comes from.
- For any claim that is simply uncertain or model-dependent, a verdict
  of UNCERTAIN with a note is fine -- we will document it as such.
