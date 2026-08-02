# Cross-Check Worksheet -- `constants_new.py` Citation Verification

**Built on `225071f6184c5fe150a8cdb258a03dbe10ae2718`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
HEAD verified fresh at session start; it matches the stated anchor
exactly. All 35 values in the prompt were confirmed byte-for-byte
against the file at that SHA before any research began.**

**Checker:** Claude Opus 5
**Date:** 2026-08-02
**Job:** citation verification -- does the cited source contain this
value at this precision?

---

## Headline

**One citation is wrong for seven constants at once.** IAU 2015
Resolution B3 defines nominal radii for the Sun, the Earth, and Jupiter
only. It does not define nominal radii for Mars, Saturn, Uranus, or
Neptune, and the Earth values it does define carry fewer digits than the
code uses. The Group G section header and four inline comments cite B3
for values B3 does not publish.

The numbers themselves are almost all right. This is a provenance
problem, not an accuracy problem -- which is the harder kind to catch,
because nothing renders wrong.

**Two arithmetic errors** and **three small-body values that contradict
their own inline comments** are the accuracy findings.

---

## Coverage, stated honestly

I verified 24 of 35 constants against live sources this session. The
remaining 11 I could not verify by web search, and I have marked them
**UNVERIFIED** rather than guessing. An unverified row is not a passing
row. Most of the gap is Group D, where the citations are book chapters
(Carroll & Ostlie; Golub & Pasachoff) that web search cannot open.

---

## Group A: Fundamental Constants

| # | Constant | Value | Cited source | Citation correct? | Notes |
|---|----------|-------|--------------|-------------------|-------|
| A1 | `KM_PER_AU` | 149597870.7 | IAU 2012 Res. B2 | **YES** | B2 defines the au as 149,597,870,700 m exactly. The km value is that number, exact. |
| A2 | `SUN_RADIUS_KM` | 695700.0 | IAU 2015 Res. B3 | **YES** | B3 nominal solar radius = 6.957e8 m exactly. Confirmed via the IAU 2015 B3 resolution text and the Prsa et al. 2016 AJ paper. |
| A3 | `SPEED_OF_LIGHT_KM_S` | 299792.458 | NIST/SI exact | **YES** | c = 299,792,458 m/s is an exact SI definition. |

---

## Group B: Earth Reference -- right numbers, wrong authority

| # | Constant | Value | Cited source | Citation correct? | Notes |
|---|----------|-------|--------------|-------------------|-------|
| B1 | `EARTH_EQUATORIAL_RADIUS_KM` | 6378.137 | IAU 2015 B3 nominal | **PARTIAL** | B3 publishes 6.3781e6 m -- that is **6378.1 km, five significant figures**. The code carries three more digits than the cited resolution states. |
| B2 | `EARTH_POLAR_RADIUS_KM` | 6356.752 | IAU 2015 B3 nominal | **PARTIAL** | B3 publishes 6.3568e6 m = **6356.8 km**. Same over-precision. |

The values are not wrong. They are the IERS zero-tide radii, and the
Prsa et al. paper says so explicitly: B3's terrestrial radii were
*adopted from* the 2003 and 2010 IERS Conventions (McCarthy & Petit
2004; Petit & Luzum 2010) and rounded.

So the honest citation for 6378.137 and 6356.752 is IERS, with IAU B3
as the rounded standard derived from it. As written, the citation
asserts that B3 contains digits it does not.

For reference, JPL SSD publishes Earth equatorial radius as 6378.1366
+/- 0.0001 km (Archinal et al. 2018) -- a fourth decimal the code also
does not carry, and does not need to.

---

## Group C: Jupiter Reference -- clean

| # | Constant | Value | Cited source | Citation correct? | Notes |
|---|----------|-------|--------------|-------------------|-------|
| C1 | `JUPITER_EQUATORIAL_RADIUS_KM` | 71492.0 | IAU 2015 B3 nominal | **YES** | B3 nominal jovian equatorial radius = 7.1492e7 m exactly. Independently, JPL SSD gives 71492 +/- 4 km. |
| C2 | `JUPITER_POLAR_RADIUS_KM` | 66854.0 | IAU 2015 B3 nominal | **YES** | B3 nominal jovian polar radius = 6.6854e7 m exactly. |

These two are the cleanest citations in the file. B3 states them at
exactly the precision the code uses, because B3 defines them as exact.

---

## Group D: Solar Structure -- mostly unverifiable by this method

| # | Constant | Value | Cited source | Citation correct? | Notes |
|---|----------|-------|--------------|-------------------|-------|
| D1 | `CORE_AU` | 0.2 R_sun | Standard solar model (Bahcall et al.) | **UNVERIFIED** | 0.2-0.25 R_sun is the conventional core boundary, but I did not open a Bahcall paper to confirm the specific figure. |
| D2 | `RADIATIVE_ZONE_AU` | 0.7 R_sun | Standard solar model | **UNVERIFIED** | Same. Also note the citation names no author, year, or paper -- "Standard solar model" alone is not a locatable source. |
| D3 | `CHROMOSPHERE_RADII` | 1.5 | Carroll & Ostlie (2017), Ch. 11 | **UNVERIFIED** | Book chapter; not openable by web search. |
| D4 | `INNER_CORONA_RADII` | 3 | Golub & Pasachoff (2010) | **UNVERIFIED** | Book; not openable. No page or chapter given, which makes it unverifiable even with the book in hand. |
| D5 | `OUTER_CORONA_RADII` | 50 | "Various"; Mann et al. (2004), A&A 414:1127 | **UNVERIFIED** | "Various" is not a source. The Mann reference is specific and checkable by someone with journal access. |
| D6 | `STREAMER_BELT_RADII` | 6.0 | Golub & Pasachoff (2010); DeForest et al. (2018) | **UNVERIFIED** | The code's own comment says helmet streamers extend 4-6 R_sun, and 6.0 takes the top of that range with no stated reason. |
| D7 | `ROCHE_LIMIT_RADII` | 3.45 | Fluid Roche formula; Murray & Dermott (1999) Sec. 4.6 | **DERIVED -- verified** | See below. |
| D8 | `ALFVEN_SURFACE_RADII` | 18.8 | Kasper et al. (2021), PRL 127:255101 | **YES** | See below -- with an important correction to how the press coverage words it. |

### D7 -- the Roche derivation checks out, but its key input is unstated

Using the fluid formula d = 2.44 R (rho_Sun / rho_comet)^(1/3):

- Sun mean density from the IAU nominal solar radius and the nominal
  solar mass parameter = **1410 kg/m^3**
- The density that produces exactly 3.45 R_sun is **499 kg/m^3**

500 kg/m^3 is a reasonable cometary nucleus density -- 67P is around
533 -- so the derivation is sound and the constant is correct.

The problem is that the citation gives the formula and the textbook but
not the density assumption, and the density is the only free input.
Someone re-deriving this cannot reproduce 3.45 without guessing 500.

**Recommend:** add the assumed density to the comment. That converts an
unreproducible derivation into a reproducible one.

### D8 -- correct, and the code is right where NASA's press wording is loose

Kasper et al. 2021 (PRL 127:255101) is the right paper and 18.8 is the
right number. But the NASA and APL press releases say 18.8 solar radii
"above the solar surface," and that phrasing does not survive its own
arithmetic: 8.127 million miles converts to 18.8 R_sun measured **from
Sun center**, not from the surface.

The PRL paper is unambiguous -- during the crossing the spacecraft moved
"from 19.7 to 18.4 solar radii from the center of the Sun," which
brackets 18.8 heliocentrically.

The orrery draws its shells from Sun center, so the code is using the
value correctly. Worth a note in the comment so nobody later "fixes" it
to 19.8 on the strength of a press release.

---

## Group E: Heliosphere

| # | Constant | Value | Cited source | Citation correct? | Notes |
|---|----------|-------|--------------|-------------------|-------|
| E1 | `TERMINATION_SHOCK_AU` | 94 | Stone et al. (2005), Science 309:2017 | **YES** | Stone 2005 states Voyager 1 crossed on 16 December 2004 at 94.01 AU. Exact match, correct paper. |
| E2 | (comment) Voyager 2 at 84 AU, Aug 2007 | 84 | Stone et al. 2008 / Richardson 2008 | **YES** | Published as 83.7 AU (2007.66); "84" is the standard rounding used throughout the literature. |
| E3 | `HELIOPAUSE_RADII` | 26449 | Gurnett et al. (2013), Science 341:1489 -- via 121.6 AU | **NO -- arithmetic error** | See below. |
| E4 | `INNER_LIMIT_OORT_CLOUD_AU` | 2000 | Hills (1981); Oort (1950) | **UNVERIFIED** | Not checked against either paper this session. |
| E5 | `INNER_OORT_CLOUD_AU` | 20000 | Hills (1981) | **UNVERIFIED** | Same. |
| E6 | `OUTER_OORT_CLOUD_AU` | 100000 | Oort (1950); Weissman (1996) | **UNVERIFIED** | Same. |
| E7 | `GRAVITATIONAL_INFLUENCE_AU` | 126000 | "Approximate Hill sphere radius of Sun in Milky Way" | **NO SOURCE** | This names a concept, not a source. Nobody is cited, and no derivation is given. This is the weakest provenance in the file. |

### E3 -- the heliopause conversion is off by 301 R_sun

The code's own comment asks for exactly this check, so here it is:

- 121.6 AU x (149,597,870.7 / 695,700) = **26,148 R_sun**
- The code has **26,449**
- Working backwards, 26,449 R_sun = **123.0 AU**

The heliopause crossing distance is well established. Gurnett et al.
2013 and Stone et al. 2013 give 121.6 AU, and independent reviews quote
121.6-121.7 AU. The literature does not support 123.

Either the constant was computed from a 123 AU figure that isn't the
cited one, or a digit moved. The error is 1.15% -- invisible in a
rendered shell, which is exactly why it survived.

**Recommend:** 26148.

---

## Group F: Parker Solar Probe

| # | Constant | Value | Cited source | Citation correct? | Notes |
|---|----------|-------|--------------|-------------------|-------|
| F1 | `PARKER_CLOSEST_RADII` | 9.86 | PSP mission, perihelion 22, Dec 24 2024 | **YES** | Confirmed, and the April 2026 correction was right. |

The 8.86-vs-9.86 confusion has a clean explanation, and it is the same
center-vs-surface distinction as D8:

- 9.86 R_sun = 6.859e6 km **from Sun center**
- minus one solar radius = 6.164e6 km = **3.83 million miles above the
  surface** = 8.86 R_sun of altitude

Both numbers describe the same orbit. Riley et al. 2019 states the PSP
final perihelion as "a final heliocentric distance of 9.86 solar radii,"
citing the Fox et al. 2016 mission paper -- explicitly heliocentric, and
matching the code.

PSP completed perihelia 23 and 24 at the same distance as the December
2024 pass, so 9.86 remains the mission minimum. Nothing has superseded
it.

---

## Group G: Body Radii

**The section header is wrong.** It cites "IAU 2015 Resolution B3 (Prsa
et al. 2016) for Sun, Earth, Mars, Jupiter, Saturn, Uranus, Neptune
nominal values." Resolution B3 adopts five solar constants and six
planetary constants, and the six are: terrestrial equatorial radius,
terrestrial polar radius, jovian equatorial radius, jovian polar radius,
terrestrial mass parameter, jovian mass parameter.

There is no nominal Mars radius, no nominal Saturn radius, no nominal
Uranus radius, and no nominal Neptune radius in B3. The correct
authority for those four is the IAU/IAG Working Group on Cartographic
Coordinates and Rotational Elements -- Archinal et al. 2018, *Celest.
Mech. Dyn. Astr.* 130:22 -- which is what JPL SSD cites for every one of
them.

| # | Constant | Value | Cited source | Citation correct? | Notes |
|---|----------|-------|--------------|-------------------|-------|
| G1 | `MERCURY_RADIUS_KM` | 2439.7 | NASA Fact Sheet (volumetric mean) | **PARTIAL** | JPL SSD publishes mean radius **2439.4 +/- 0.1** and equatorial 2440.53. The NSSDCA fact sheet is the likely origin of 2439.7 but I did not open it this session. Two NASA-family sources cited in the same section disagree by 0.3 km. |
| G2 | `VENUS_RADIUS_KM` | 6051.8 | NASA Fact Sheet (volumetric mean) | **YES** | JPL SSD confirms 6051.8 +/- 1.0 for both equatorial and mean. |
| G3 | `MOON_RADIUS_KM` | 1737.4 | NASA Fact Sheet (volumetric mean) | **UNVERIFIED** | Not checked this session. |
| G4 | `MARS_RADIUS_KM` | 3396.2 | "IAU 2015 nominal equatorial" | **NO -- wrong authority** | Value correct: JPL SSD gives 3396.19 +/- 0.1 (Archinal et al. 2018). But B3 defines no Mars nominal radius. |
| G5 | `PHOBOS_RADIUS_KM` | 11.1 | NASA/JPL SSD | **DERIVED -- verified** | The NASA Mars Fact Sheet gives triaxial radii 13.4 x 11.2 x 9.2 km. Their geometric mean is **11.14 km**, so 11.1 is a correct volumetric mean. The comment should say it is derived. |
| G6 | `SATURN_RADIUS_KM` | 60268 | "IAU 2015 nominal equatorial" | **NO -- wrong authority** | Value correct: JPL SSD 60268 +/- 4 (Archinal 2018). B3 has no Saturn value. |
| G7 | `URANUS_RADIUS_KM` | 25559 | "IAU 2015 nominal equatorial" | **NO -- wrong authority** | Value correct: JPL SSD 25559 +/- 4. |
| G8 | `NEPTUNE_RADIUS_KM` | 24764 | "IAU 2015 nominal equatorial" | **NO -- wrong authority** | Value correct: JPL SSD 24764 +/- 15. |
| G9 | `PLUTO_RADIUS_KM` | 1188.3 | Nimmo et al. 2017 (Icarus) | **PARTIAL** | Value confirmed: JPL SSD gives 1188.3 +/- 1.6 for both equatorial and mean. I did not open Nimmo 2017 itself; JPL attributes its figure to Archinal et al. 2018. The citation is plausible and the number is right. |
| G10 | `BENNU_RADIUS_KM` | 0.262 | OSIRIS-REx (volumetric mean) | **UNVERIFIED** | Not checked. Flagging because published Bennu mean radii cluster near 0.245 km, so this one is worth confirming rather than assuming. |
| G11 | `ERIS_RADIUS_KM` | 1163 | Sicardy et al. 2011 occultation | **PARTIAL -- conflicts with the section's other cited source** | JPL SSD, named in the same header, publishes **1200 +/- 50** (Brown & Schaller 2007). 1163 is consistent with the 2011 occultation result and is the better measurement, but the file cites two sources that disagree. |
| G12 | `HAUMEA_RADIUS_KM` | 816 | Volumetric mean of 1050 x 840 x 537 km | **NO -- does not follow from its own inputs** | The geometric mean of 1050, 840, 537 is **779.5 km**, not 816. Separately, JPL SSD publishes mean radius **715** (Lockwood et al. 2014) and equatorial 870. 816 matches neither the stated derivation nor the cited database. |
| G13 | `MAKEMAKE_RADIUS_KM` | 715 | Brown et al. (volumetric mean) | **PARTIAL** | JPL SSD gives mean **714 +/- 7** and equatorial 717 +/- 7 (Brown 2013). 715 sits inside the error bar but is not the published mean. |
| G14 | `ARROKOTH_RADIUS_KM` | 9.95 | Volumetric mean of ~35 x 20 x 14 km | **NO -- does not follow from its own inputs** | An equivalent-volume sphere for those dimensions has radius **10.70 km**, not 9.95. Either the dimensions in the comment or the constant is wrong. |

---

## Summary by verdict

| Verdict | Count | Which |
|---------|------:|-------|
| YES | 9 | A1, A2, A3, C1, C2, D8, E1, E2, F1 |
| DERIVED -- verified | 2 | D7, G5 |
| PARTIAL | 6 | B1, B2, G1, G9, G11, G13 |
| NO -- wrong authority | 4 | G4, G6, G7, G8 |
| NO -- arithmetic | 3 | E3, G12, G14 |
| NO SOURCE | 1 | E7 |
| UNVERIFIED | 10 | D1-D6, E4, E5, E6, G3, G10 |

(11 rows are marked UNVERIFIED or NO SOURCE; D-group dominates.)

---

## Tony-action rollup

**(decide) -- accuracy, highest first**

1. `HELIOPAUSE_RADII`: 26449 -> **26148**. The cited 121.6 AU does not
   produce 26449; 26449 corresponds to 123.0 AU, which no source
   supports.
2. `HAUMEA_RADIUS_KM`: 816 matches neither its own stated axes (779.5)
   nor JPL SSD's published mean (715). Needs a decision on which
   convention the file wants, then a value that follows from it.
3. `ARROKOTH_RADIUS_KM`: 9.95 vs 10.70 from its own stated dimensions.
4. `MERCURY_RADIUS_KM`: reconcile NSSDCA 2439.7 against JPL SSD 2439.4,
   or say which one the file follows.
5. `ERIS_RADIUS_KM`: 1163 (Sicardy occultation) vs JPL SSD's 1200 +/-
   50. Keeping 1163 is defensible; citing both sources without saying
   which one won is not.

**(decide) -- provenance**

6. Rewrite the Group G section header: B3 covers Sun, Earth, Jupiter
   only. Mars, Saturn, Uranus, Neptune come from Archinal et al. 2018
   (IAU WGCCRE 2015 report), which is what JPL SSD cites.
7. Fix the four inline "IAU 2015 nominal equatorial" comments on Mars,
   Saturn, Uranus, Neptune.
8. Group B: cite IERS Conventions for the extra digits, with B3 as the
   rounded standard, or drop to B3's actual precision.
9. `GRAVITATIONAL_INFLUENCE_AU` has no source at all. Under the
   fetched-vs-recalled rule this is either sourced, derived with the
   derivation shown, or removed with the gap noted.
10. Add the assumed cometary density (500 kg/m^3) to the Roche limit
    comment so the derivation is reproducible.
11. Add a note to `ALFVEN_SURFACE_RADII` and `PARKER_CLOSEST_RADII` that
    both are heliocentric, since the NASA press releases for both
    describe the same distances as altitudes above the surface. This is
    the exact trap that produced the 8.86 error the first time.
12. Mark `PHOBOS_RADIUS_KM` as derived from the fact sheet's triaxial
    radii rather than read off a page.

**(do)**

13. Group D needs a checker with journal and book access, not web
    search. Six constants rest on citations I cannot open. If they
    cannot be verified by anyone, the honest move is a disclosure note
    on the shells they drive, not a silent citation.

---

## Note on what this exercise found

Every accuracy error here is under 2%, and every one of them sits behind
a correct-looking citation. That is the pattern the vulnerability ladder
was built for: a wrong number with a citation attached is harder to
catch than a wrong number without one, because the citation suppresses
the suspicion that would find it.

The Group G header is the clearest case. It names a real resolution, by
real authors, in a real journal -- for values that resolution does not
contain.

---

*Worksheet prepared August 2, 2026 by Claude Opus 5. Sources consulted
live: IAU 2015 Resolution B3 / Prsa et al. 2016 (AJ 152:41); JPL Solar
System Dynamics Planetary Physical Parameters (fetched directly); NASA
NSSDCA Mars Fact Sheet; Kasper et al. 2021 (PRL 127:255101) and the
JHUAPL/NASA release; Riley et al. 2019 (arXiv:1902.09673); Stone et al.
2005 (Science 309:2017); Gurnett et al. 2013 as quoted in ApJ and
Space Sci. Rev. reviews.*
