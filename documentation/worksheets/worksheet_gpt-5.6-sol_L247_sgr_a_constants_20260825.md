# Cross-check return -- L-247 Sagittarius A* and galactic-scale constants

**Return filename:** `worksheet_gpt-5.6-sol_L247_sgr_a_constants_20260825.md`

**Method note:** For measured quantities, `Value correct?` is judged against the best later primary measurement I could establish at the review date, not merely against whether an older paper once published the code literal. That distinction matters for rows 4 and 5. `Citation correct?` follows the request's separate rule: whether the source named in the code publishes the code value.

## Response table

| # | Constant | Code value | Code's source line | Your value | Your source | Value correct? | Citation correct? | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 | `GRAVITATIONAL_CONSTANT_SI` -- Newtonian constant of gravitation | 6.67430e-11 m^3 kg^-1 s^-2 | none | (6.67430 +/- 0.00015) x 10^-11 m^3 kg^-1 s^-2 | Mohr, Newell, Taylor & Tiesinga (2025), CODATA 2022 adjustment, *Rev. Mod. Phys.* 97, 025002, DOI 10.1103/RevModPhys.97.025002, Tables XXXII-XXXIII | YES | UNSOURCED | MEASURED/recommended, not exact. The code central value exactly matches CODATA 2022. CODATA publishes 6.67430(15) x 10^-11, relative standard uncertainty 2.2 x 10^-5. The digits in the literal do not exceed the published central-value precision, but omitting the uncertainty can make a measured constant look exact. |
| 2 | `SOLAR_MASS_KG` -- mass of the Sun | 1.989e30 kg | none | 1.988410(45) x 10^30 kg as a current nominal solar-mass conversion | IAU 2015 Resolution B3 / Prsa et al. (2016), *AJ* 152, 41, DOI 10.3847/0004-6256/152/2/41, gives exact nominal solar mass parameter (GM)^N_sun = 1.3271244 x 10^20 m^3 s^-2; combined here with CODATA 2022 G | APPROX | UNSOURCED | DERIVED, not independently measured in kg. Arithmetic: M^N_sun = (GM)^N_sun / G = 1.3271244e20 / 6.67430e-11 = 1.9884098707e30 kg. Propagating the CODATA G uncertainty gives about 4.47e25 kg, hence 1.988410(45)e30 kg. IAU explicitly treats the nominal GM value as an exact conversion constant, not the true solar property. `1.989e30` is a rough approximation, but at four significant figures the modern derived value rounds to `1.988e30`, not `1.989e30`. |
| 3 | `PARSEC_TO_AU` -- astronomical units per parsec | 206265.0 AU | none | 648000/pi = 206264.806247096... AU exactly | IAU 2015 Resolution B2 notes; the exact parsec definition is repeated in Prsa et al. (2016), *AJ* 152, 41, Appendix, DOI 10.3847/0004-6256/152/2/41 | APPROX | UNSOURCED | DEFINED. Arithmetic is the definition: 1 pc = (648000/pi) au. The code is the familiar nearest-AU rounding and has relative error about 9.39e-7. If the trailing `.0` is intended to imply 0.1-AU accuracy, it overstates the accuracy of this rounded literal; the exact relation itself has no measurement uncertainty. |
| 4 | `SGR_A_MASS_SOLAR` -- mass of Sagittarius A* | 4.154e6 solar masses | `# Source: GRAVITY Collaboration 2019` | (4.297 +/- 0.012_stat +/- ~0.040_sys) x 10^6 M_sun | GRAVITY Collaboration (2022), “Mass distribution in the Galactic Center based on interferometric astrometry of multiple stellar orbits,” *A&A* 657, L12, DOI 10.1051/0004-6361/202142465 | NO | YES | MEASURED. The code value is not invented: GRAVITY Collaboration (2019), *A&A* 625, L10, DOI 10.1051/0004-6361/201935656, Table 1, publishes 4.154 +/- 0.014 x 10^6 M_sun for its down-sampled-data fit. Thus the named authority does publish the number. But GRAVITY's later multi-star fit gives 4.297 x 10^6 M_sun, with stated statistical uncertainty 0.012 x 10^6 and systematic uncertainty about 0.040 x 10^6. The 2019 literal is therefore a valid historical fit, not the later GRAVITY best estimate. Its four significant digits were appropriate for the 2019 table; the issue is staleness, not fabricated precision. |
| 5 | `SGR_A_DISTANCE_LY` -- distance to Sagittarius A* | 26670.0 light-years | none | 26995.96 ly, from R0 = 8277 pc; approximately 26,996 +/- 29_stat +/- 98_sys ly | GRAVITY Collaboration (2022), *A&A* 657, L12, DOI 10.1051/0004-6361/202142465, gives R0 = 8277 +/- 9 pc with systematics about 30 pc; IAU definitions supply the unit conversion | NO | UNSOURCED | MEASURED distance with a DERIVED unit conversion. Using 1 pc = 648000/pi au, 1 au = 149597870700 m exactly, c = 299792458 m/s exactly, and one Julian year = 365.25 x 86400 s gives 1 pc = 3.261563777167... ly. Therefore 8277 pc = 26995.963... ly. The code's 26670 ly is very close to the older GRAVITY 2019 result: 8178 pc converts to 26673.07 ly, which rounds to 26670 ly at four significant figures. The `.0` is not supported as measurement precision; even the 2019 measurement corresponds to uncertainty of order 80 ly, and the later result has systematic uncertainty of about 98 ly after conversion. |

## Findings

The strongest finding is that rows 4 and 5 form a matched historical pair. GRAVITY Collaboration 2019 reported a distance of R0 = 8178 +/- 13_stat +/- 22_sys pc and, in Table 1, a down-sampled-data mass fit of 4.154 +/- 0.014 x 10^6 M_sun. Converting 8178 pc with the IAU definitions gives 26673.07 ly, so the code's `26670.0` is almost certainly a rounded conversion of that same 2019 result. The mass source line therefore points to a real publication and a real value; the distance appears to come from the same paper but lost its attribution.

GRAVITY's later 2022 multi-star analysis changed both quantities together, to R0 = 8277 +/- 9 pc and M_bh = 4.297 +/- 0.012 x 10^6 M_sun, with quoted systematics of about 30 pc and 40,000 M_sun respectively. Because mass and distance are correlated orbital-fit parameters, updating one without the other would be poor practice. If these constants are intended to represent the project's current adopted Galactic-center parameters, rows 4 and 5 should be reviewed as a pair. If instead they are deliberately frozen to the 2019 GRAVITY solution for reproducibility, both need an explicit provenance note saying so.

Row 2 is not best treated as a directly measured “mass of the Sun in kg.” The IAU deliberately standardized the nominal solar mass parameter, (GM)^N_sun, because G is much less precisely known than GM_sun. A kilogram conversion therefore inherits the uncertainty and revision history of G. The code value is usable as a coarse astronomy approximation, but the repair should say DERIVED and name both inputs rather than attach a source that supposedly publishes `1.989e30 kg` as an exact solar constant.

Row 3 is cleaner: the parsec-to-au relationship is a definition. The source-level value is not `206265.0`; it is exactly 648000/pi au. If the code needs a floating constant, a higher-precision evaluation such as 206264.806247096 is preferable. If the code only needs a rough scale, 206265 is fine, but its annotation should make the rounding explicit.

Row 1 needs no numerical repair. CODATA 2022 retains G = 6.67430(15) x 10^-11 m^3 kg^-1 s^-2. The repair is provenance plus uncertainty semantics, not a changed central value.

## Primary sources used

Mohr, P. J., Newell, D. B., Taylor, B. N., & Tiesinga, E. (2025), “CODATA recommended values of the fundamental physical constants: 2022,” *Reviews of Modern Physics* 97, 025002. DOI 10.1103/RevModPhys.97.025002.

Prsa, A., et al. (2016), “Nominal values for selected solar and planetary quantities: IAU 2015 Resolution B3,” *The Astronomical Journal* 152, 41. DOI 10.3847/0004-6256/152/2/41.

International Astronomical Union, 2012 Resolution B2, “On the re-definition of the astronomical unit of length,” defining 1 au = 149597870700 m exactly.

International Astronomical Union, 2015 Resolution B2, notes defining 1 pc = (648000/pi) au exactly.

GRAVITY Collaboration (2019), “A geometric distance measurement to the Galactic center black hole with 0.3% uncertainty,” *Astronomy & Astrophysics* 625, L10. DOI 10.1051/0004-6361/201935656.

GRAVITY Collaboration (2022), “Mass distribution in the Galactic Center based on interferometric astrometry of multiple stellar orbits,” *Astronomy & Astrophysics* 657, L12. DOI 10.1051/0004-6361/202142465.
