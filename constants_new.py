"""
constants_new.py - Verified numeric constants for Paloma's Orrery.

Single source of truth for all physical constants, orbital periods,
body radii, and color mappings. Every propagating constant has a
source citation and verification date. Derived values are computed
from primary constants -- never hardcoded independently.

Import from this module. Do not redefine these values locally.
See provenance_scanner.py for audit, module_atlas.py for consumers.

Verification process (April 2026):
    1. Claude sourced constants from IAU resolutions and NASA fact sheets
    2. Google Gemini reviewed all values against authoritative sources
    3. Gemini caught two errors Claude introduced during verification:
       - Arrokoth radius: 0.0088 km (8.8 m!) -> 9.95 km (actual mean)
       - Parker closest approach: 8.86 R_sun (surface altitude)
         -> 9.86 R_sun (from Sun center, consistent with shell radii);
         perihelion number corrected from 21 to 22
    4. Tony integrated corrections and made final decisions

Revised 2026-04-16 by Anthropic's Claude Opus 4.6 and Google Gemini:
    - CENTER_BODY_RADII convention changed from volumetric mean to
      hybrid (equatorial for major planets, volumetric for small
      bodies). Rationale: shell modules scale by R_body as a unit
      of measure (e.g. 5.9 R_J for Io torus), and planetary-science
      literature cites these fractions against equatorial radii.
      Volumetric mean introduced silent ~2.3% position errors.
    - Parker Solar Probe closest approach: 8.86 -> 9.86 R_sun was
      correctly applied; this revision does not affect Parker.    

Lesson: Verification by the same AI that generated the value is not
verification. Cross-AI review (Mode 7) is load-bearing for facts.

Role: data
Domain: orrery

Module updated: April 2026 with Anthropic's Claude Opus 4.6
Reviewed: April 2026 by Google Gemini (Mode 7 cross-verification)

Module updated: August 20, 2026 with Anthropic's Claude Opus 5 (L-210 reconciliation; see the Resolved legs on the affected rows)
Module updated: August 21, 2026 with Anthropic's Claude Opus 5 (L-209: DeForest 2014 rehomed to ALFVEN_SURFACE_RADII, and its figure corrected from 17 to the published 15 R_sun)
Module updated: July 2026 with Anthropic's Claude Sonnet 5 (L-162: 14
remaining CENTER_BODY_RADII bodies promoted to named constants; value
and citation carried forward unchanged from each dict entry)
Module updated: August 25, 2026 with Anthropic's Claude Opus 5 (L-247:
the five migrated Sgr A* and galactic-scale constants sourced against
three independent returns. GM_SUN_SI and SGR_A_DISTANCE_PC added as
sourced primaries; SOLAR_MASS_KG and SGR_A_DISTANCE_LY derived from
them; PARSEC_TO_AU given its exact definitional value; SGR_A_MASS_SOLAR
advanced from the 2019 to the 2022 GRAVITY determination under the
epoch policy recorded in the section header)
Module updated: August 25, 2026 with Anthropic's Claude Opus 5 (L-247:
annotation repair only, no value moves -- continuation lines marked,
four Resolved legs added, an invented Superseded label retired into
Review-note, and an UNMATCHED cross-check on SGR_A_DISTANCE_PC removed)
Module updated: August 26, 2026 with Anthropic's Claude Opus 5
(L-253: two figures removed from EARTH_D660_DEPTH_KM's Note that
the Ishii 2019 reference beside them does not support. The Note
keeps the qualitative statement; the figures and their candidate
papers move to the ledger, which is outside the audit)
Module updated: August 26, 2026 with Anthropic's Claude Opus 5
(L-249: Earth's four interior boundary radii added as sourced
primaries with derived shell fractions. Tony's ruling of the same
day -- the original radius fractions were approximate values taken
by hand, not declared drawing choices, so every one of them derives
from the sourced radius and constants_new.py is the only store.
Derived quotients are held at full float precision and REPORTED
to the significant figures their least precise input supports)
Module updated: September 12, 2026 with Anthropic's Claude Opus 5
(L-305 Gap item 4: Earth's magnetosphere rebuilt on two published
models. Fifteen rows added -- three declared solar wind conditions,
Shue et al. (1998)'s eight magnetopause coefficients, Jelinek et al.
(2012)'s three bow shock parameters and the bow shock cut angle. The
two standoffs are superseded and are now derived from those rows
rather than typed. A Lugaz-midpoint derivation and a Farris & Russell
"Model form" miscitation are removed. Every row written here carries a
"# Unit:" line, the fifteenth comment key, per L-322 ruling 1)
Module updated: September 12, 2026 with Anthropic's Claude Opus 5
(L-325: the two derived rows now STORE the figure they already said
to report -- 10.25 and 13.51 -- rather than the arithmetic result.
test_derived_figures.py recomputes each from the inputs its Status
line names and fails when the rounding stops holding)
"""

import numpy as np
from datetime import datetime, timedelta


# ============================================================
# FUNDAMENTAL CONSTANTS (IAU-defined, exact)
# ============================================================

KM_PER_AU = 149597870.7
# Source: IAU 2012 Resolution B2 -- exact definition
# Ref: https://syrte.obspm.fr/IAU_resolutions/Res_IAU2012_B2.pdf
# Also: https://nssdc.gsfc.nasa.gov/planetary/factsheet/fact_notes.html
# Cross-checked: Claude 2026-08-02 -- IAU B2 (worksheet_claude_constants_new.md)
# Cross-checked: GPT 2026-08-02 -- IAU B2 (constants_new_citation_verification_gpt.md)
# Note: 1 AU = 149,597,870,700 m exactly. We use km (divide by 1000).

SUN_RADIUS_KM = 695700.0
# Source: IAU 2015 Resolution B3 -- nominal solar radius
# Ref: Prsa et al. 2016, AJ 152:41 (arXiv:1605.09788)
# Also: https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html
# Cross-checked: Claude 2026-08-02 -- IAU B3 (worksheet_claude_constants_new.md)
# Cross-checked: GPT 2026-08-02 -- IAU B3 (constants_new_citation_verification_gpt.md)
# Note: This is the IAU nominal value (conversion constant), not a
# Note+: measurement. The measured photospheric radius is ~696,340 km
# Note+: (Haberreiter et al. 2008). Use nominal for all calculations.

EARTH_EQUATORIAL_RADIUS_KM = 6378.1366
# Source: IERS Conventions (2010), Petit & Luzum (eds.), IERS Technical
# Source+: Note No. 36, Table 1.1; IAU B3 rounds to 6378.1 km
# Ref: Prsa et al. 2016, AJ 152:41 (arXiv:1605.09788)
# Also: https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html
# Note: IERS publishes 6378136.6 +/- 0.1 m. IAU B3's 6.3781e6 m is an
# Note+: exact nominal conversion constant, not a measurement, and the two
# Note+: differ by 36.6 m.
# Resolved: worksheet_claude-opus-5_pilot_constants_new_20260818.jsonl constants_new.py::EARTH_EQUATORIAL_RADIUS_KM -- Source moved from IAU B3 to IERS and the value taken to IERS precision (L-210)
# Cross-checked: Claude 2026-08-02 -- IAU B3 / IERS (worksheet_claude_constants_new.md)
# Cross-checked: GPT 2026-08-02 -- IAU B3 / IERS (constants_new_citation_verification_gpt.md)

EARTH_POLAR_RADIUS_KM = 6356.752
# Source: IERS Conventions (Petit & Luzum 2010); IAU B3 rounds to 6356.8 km
# Ref: Prsa et al. 2016, AJ 152:41 (arXiv:1605.09788)
# Cross-checked: Claude 2026-08-02 -- IAU B3 / IERS (worksheet_claude_constants_new.md)
# Cross-checked: GPT 2026-08-02 -- IAU B3 / IERS (constants_new_citation_verification_gpt.md)

# ============================================================
# EARTH INTERIOR BOUNDARIES (L-249)
# ============================================================
# Each boundary is stored ONCE, here, as a radius from Earth's centre in
# km with its own source. The shell fraction beside it is derived. No
# consumer -- shell_configs.py, earth_visualization_shells.py, hover text
# or tooltip -- may carry a numeric copy of either.
#
# FRAME NOTE, and it is load-bearing. PREM's radii and the seismological
# depth scale are both referenced to a MEAN Earth of 6371.0 km. The
# orrery draws Earth's shells against EARTH_EQUATORIAL_RADIUS_KM
# (6378.1366), because that is what CENTER_BODY_RADII['Earth'] hands to
# build_sphere_shell(). Dividing a sourced radius by the equatorial
# radius therefore draws each boundary at its correct ABSOLUTE radius,
# and its depth below the DRAWN surface comes out about 7 km greater
# than the textbook depth. That 7 km is the equatorial-versus-mean
# difference, not an error in either number. Radius is what PREM
# measures; depth is derived from it. Radius wins.
#
# PRECISION. The derivations below are held at FULL float precision in
# code -- rounding a derived constant would introduce error and would
# also make the rounded copy a second store of a value that lives here.
# What significant figures govern is REPORTING: every quotient stated in
# a comment, a hover string or a tooltip carries no more figures than its
# least precise input, and the figure count is named beside it so the
# next reader does not have to re-derive it.

EARTH_MEAN_RADIUS_KM = 6371.0
# Source: NASA Planetary Fact Sheet, Earth -- volumetric mean radius
# Ref: https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html
# Note: the reference sphere that PREM and the seismological depth scale
# Note+: are quoted against. NOT the radius the orrery draws to -- see
# Note+: the frame note above.

EARTH_INNER_CORE_KM = 1221.5
# Source: Dziewonski, A. M. & Anderson, D. L. (1981), "Preliminary
# Source+: reference Earth model", Phys. Earth Planet. Inter. 25:297-356
# Source+: -- inner core boundary (ICB) at r = 1221.5 km (5 sig figs).
# Note: the shell previously carried radius_fraction 0.19, an
# Note+: approximate value taken by hand when the shells were first
# Note+: drawn (Tony's account, 2026-08-26). It drew 1211.8 km.
EARTH_INNER_CORE_RADII = EARTH_INNER_CORE_KM / EARTH_EQUATORIAL_RADIUS_KM
# Derived: 1221.5 / 6378.1366 = 0.19151 -- 5 significant figures, set
# Derived+: by the numerator. Report no more than that.

EARTH_OUTER_CORE_KM = 3480.0
# Source: Dziewonski & Anderson (1981), PREM, Phys. Earth Planet. Inter.
# Source+: 25:297-356 -- core-mantle boundary (CMB) at r = 3480 km
# Source+: (4 sig figs).
# Note: the NASA Earth Fact Sheet lists a core radius of 3485 km. PREM is
# Note+: preferred because the other three boundaries in this nested
# Note+: stack are PREM's, and mixing reference models across one stack
# Note+: is the class of inconsistency this migration exists to remove.
# Note+: The 5 km difference is below the drawn resolution either way.
EARTH_OUTER_CORE_RADII = EARTH_OUTER_CORE_KM / EARTH_EQUATORIAL_RADIUS_KM
# Derived: 3480 / 6378.1366 = 0.5456 -- 4 significant figures, set by
# Derived+: the numerator. Report no more than that.

EARTH_D660_DEPTH_KM = 660.0
# Source: the 660-km seismic discontinuity, ringwoodite dissociating to
# Source+: bridgmanite plus ferropericlase; global average depth 660 km
# Source+: (2 sig figs -- the trailing zero is not significant).
# Ref: Ishii, T., Huang, R., Myhill, R. et al. (2019), "Sharp 660-km
# Ref+: discontinuity controlled by extremely narrow binary post-spinel
# Ref+: transition", Nature Geoscience 12:869-872.
# Note: a GLOBAL AVERAGE, not a constant depth. The boundary is not
# Note+: uniform: it lies deeper where the mantle is colder and shallower
# Note+: where it is warmer. The shell is drawn at one radius because a
# Note+: sphere is what the renderer draws, and no figure for that
# Note+: variation is stated anywhere in this codebase, because none has
# Note+: been sourced.
# Review-note: single leg (Claude, 2026-08-26). A second independent
# Review-note+: cross-check is owed before this row counts as confirmed.
# Review-note+: Two figures for the variation, and the papers that may
# Review-note+: support them, are held in L-253 -- unsourced, unused, and
# Review-note+: deliberately not restated here or the breadcrumb would
# Review-note+: itself read as a citation for this value.

EARTH_LOWER_MANTLE_KM = EARTH_MEAN_RADIUS_KM - EARTH_D660_DEPTH_KM
# Derived: 6371.0 - 660 = 5711 km -- the OUTER boundary of the lower
# Derived+: mantle shell, which is the 660 discontinuity. A SUBTRACTION is
# Derived+: governed by decimal places, not significant figures: 6371.0 is
# Derived+: good to tenths and 660 to units, so the difference is good to
# Derived+: units. Physical uncertainty is far larger; see the note above.
EARTH_LOWER_MANTLE_RADII = EARTH_LOWER_MANTLE_KM / EARTH_EQUATORIAL_RADIUS_KM
# Derived: 5711 / 6378.1366 = 0.8954 -- 4 significant figures, set by
# Derived+: the numerator. Report no more than that.

EARTH_UPPER_MANTLE_KM = 6346.6
# Source: Dziewonski & Anderson (1981), PREM, Phys. Earth Planet. Inter.
# Source+: 25:297-356 -- base of the crust (Mohorovicic discontinuity) in
# Source+: the reference model, r = 6346.6 km (5 sig figs), i.e. 24.4 km
# Source+: below the mean radius.
# Note: the Moho is not a sphere. It lies about 5-10 km below ocean
# Note+: basins, 30-50 km below continents, and as deep as 70 km below
# Note+: young mountain belts. 6346.6 km is the reference global average
# Note+: and the shell's hover text says so rather than implying a
# Note+: precision the boundary does not have.
EARTH_UPPER_MANTLE_RADII = EARTH_UPPER_MANTLE_KM / EARTH_EQUATORIAL_RADIUS_KM
# Derived: 6346.6 / 6378.1366 = 0.99506 -- 5 significant figures, set by
# Derived+: the numerator. Report no more than that.

# --- Earth exhibit block (L-291, 2026-09-07) -------------------------------
# The values below are what the Earth exhibit (interactive.html?exhibit=earth)
# renders and what the orrery's Earth shells draw. Until this block existed
# they were typed literals in earth_visualization_shells.py and
# shell_configs.py; the exhibit's served entry points at these names and the
# live store-drift run checks them by name. Migrating the shell modules onto
# these names is a follow-on patch, not this one.

EARTH_GM_KM3_S2 = 398600.4418
# Source: IERS Conventions (2010), IERS Technical Note 36, Table 1.1 --
# Source+: geocentric gravitational constant GM_E = 3.986004418e14 m^3 s^-2
# Source+: (uncertainty 8e5 m^3 s^-2). Converted to km^3 s^-2 here.
# Ref: https://iers-conventions.obspm.fr/content/tn36.pdf
# Note: TCB-compatible value as tabulated; the TT-compatible value differs
# Note+: in the ninth figure, below anything this file derives from it.

EARTH_ROTATION_RATE_RAD_S = 7.292115e-5
# Source: IERS Conventions (2010), TN36 Table 1.1 -- nominal mean Earth
# Source+: angular velocity, 7.292115e-5 rad s^-1.
# Ref: https://iers-conventions.obspm.fr/content/tn36.pdf

EARTH_GEOSTATIONARY_RADIUS_KM = (EARTH_GM_KM3_S2 / EARTH_ROTATION_RATE_RAD_S ** 2) ** (1.0 / 3.0)
# Derived: (398600.4418 / 7.292115e-5^2)^(1/3) = 42164.17 km -- the
# Derived+: circular orbit whose period is one sidereal rotation. Seven
# Derived+: figures in both inputs; report 42,164 km.
# Note: the orrery's geostationary shell types 42164.0 km and quotes
# Note+: 6.62 radii, a ratio taken against the 6371 km mean radius. Against
# Note+: the equatorial radius this file draws to, it is 6.611.
EARTH_GEOSTATIONARY_RADII = EARTH_GEOSTATIONARY_RADIUS_KM / EARTH_EQUATORIAL_RADIUS_KM
# Derived: 42164.17 / 6378.1366 = 6.6107 -- report no more than five figures.

EARTH_LEO_UPPER_ALTITUDE_KM = 2000.0
# Source: IADC Space Debris Mitigation Guidelines, IADC-02-01 Rev. 3
# Source+: (June 2021), section 3.3.2 -- the LEO Protected Region extends
# Source+: from the surface to an altitude of 2,000 km. Section 3.3.1 takes
# Source+: the equatorial radius as the reference surface, as this file does.
# Ref: https://orbitaldebris.jsc.nasa.gov/library/iadc-space-debris-guidelines-revision-2.pdf
EARTH_LEO_LOWER_ALTITUDE_KM = 200.0
# Declared: the floor the orrery's LEO shell draws from. The IADC region
# Declared+: starts at the surface; 200 km is a drawing choice marking where
# Declared+: orbits stop decaying within days. Not a measured boundary.
EARTH_LEO_INNER_KM = EARTH_EQUATORIAL_RADIUS_KM + EARTH_LEO_LOWER_ALTITUDE_KM
EARTH_LEO_OUTER_KM = EARTH_EQUATORIAL_RADIUS_KM + EARTH_LEO_UPPER_ALTITUDE_KM
# Derived: 6378.1366 + 200 = 6578.1 km; 6378.1366 + 2000 = 8378.1 km.
# Note: the orrery's LEO shell types 6571 and 8371 km, which is 6371 + the
# Note+: altitude -- the mean radius, not the equatorial one the shell is
# Note+: drawn against. Seven km, below the drawn resolution, but the
# Note+: hover text quotes those numbers. Follow-on with the migration.
EARTH_LEO_INNER_RADII = EARTH_LEO_INNER_KM / EARTH_EQUATORIAL_RADIUS_KM
EARTH_LEO_OUTER_RADII = EARTH_LEO_OUTER_KM / EARTH_EQUATORIAL_RADIUS_KM
# Derived: 1.0314 and 1.3136 -- report 1.03 and 1.31, as the hover does.

EARTH_STRATOPAUSE_ALTITUDE_KM = 50.0
# Source: NOAA JetStream, "Layers of the Atmosphere" -- stratosphere to
# Source+: about 50 km; and NASA, "Earth's Atmospheric Layers" -- the
# Source+: stratosphere extends to 50 km.
# Ref: https://www.noaa.gov/jetstream/atmosphere/layers-of-atmosphere
# Ref: https://www.nasa.gov/image-article/earths-atmospheric-layers-3/
EARTH_THERMOPAUSE_ALTITUDE_KM = 600.0
# Source: NOAA JetStream, same page -- thermosphere from about 85 km to
# Source+: about 600 km, the exosphere beyond; NASA, same page -- the
# Source+: thermosphere extends to 600 km.
# Note: a nominal figure. The thermopause moves with solar activity over
# Note+: roughly 500 to 1,000 km; the drawn shell is not that precise.
EARTH_STRATOPAUSE_RADII = (EARTH_EQUATORIAL_RADIUS_KM + EARTH_STRATOPAUSE_ALTITUDE_KM) / EARTH_EQUATORIAL_RADIUS_KM
EARTH_THERMOPAUSE_RADII = (EARTH_EQUATORIAL_RADIUS_KM + EARTH_THERMOPAUSE_ALTITUDE_KM) / EARTH_EQUATORIAL_RADIUS_KM
# Derived: 1.0078 and 1.0941.
# Note: SHELL_CONFIGS['Earth'] draws the lower atmosphere at 1.05 radii
# Note+: (about 319 km up) and the upper atmosphere at 1.25 radii (about
# Note+: 1,595 km up) while their own hover text ends at 50 km and about
# Note+: 1,000 km. Both drawn fractions are visibility choices wearing
# Note+: physical-looking numbers. Recorded under L-295; the exhibit's
# Note+: served entry declares the drawn fraction and points here for the
# Note+: physical one.

EARTH_VAN_ALLEN_INNER_RADII = 1.5
# Unit: r_earth
# Status: measured V_SOURCED 2026-09-14 -- open full text
# Source: Baker, D. N. et al. (2018), "Space Weather Effects in the
# Source+: Earth's Radiation Belts", Space Sci. Rev. 214:17,
# Source+: doi:10.1007/s11214-017-0452-7 -- sec. 2: inner-zone proton fluxes
# Source+: peak near geocentric r ~ 1.5 R_E. Geocentric, equatorial, which
# Source+: is the frame this row is in.
# Access: open full text,
# Access+: https://link.springer.com/article/10.1007/s11214-017-0452-7
# Access+: (2026-09-13).
# Note: a peak, not an edge; the edges are their own rows since 2026-09-14.
# Note+: The drawn torus marks where the flux is greatest.
# Note+: The same number is read a second time in a different frame, kept
# Note+: here as a second reading and not as agreement: Li et al. (2025),
# Note+: doi:10.1029/2024JA033504, centres the inner belt near L = 1.5, and
# Note+: Selesnick et al. (2014), doi:10.1002/2014JA020188 sec. 5, puts the
# Note+: peak near L = 1.5 for 46 and 66 MeV protons against 1.6 for 26 MeV.
# Note+: L and geocentric radii coincide at the magnetic equator, so the
# Note+: agreement here is arithmetic rather than evidence about the frame.
# Record: documentation/worksheets/L321_worksheet_3_van_allen_gemini31pro_20260913.md
EARTH_VAN_ALLEN_OUTER_RADII = 4.5
# Unit: l_shell
# Status: declared 2026-09-14 -- a pick from a range, L-305 item 7
# Declared: the midpoint of an L band, not a measured peak, and the pick is
# Declared+: ours. Li et al. (2025), "A New Electron and Proton Radiation
# Declared+: Belt Identified by CIRBE/REPTile-2 Measurements After the
# Declared+: Magnetic Super Storm of 10 May 2024", J. Geophys. Res. Space
# Declared+: Physics, doi:10.1029/2024JA033504, sec. 1 -- the outer belt is
# Declared+: most intense around L = 4 and 5. Li et al. (2015),
# Declared+: doi:10.1002/2014JA020777, sec. 1 -- greatest intensity between
# Declared+: 4 and 5 equatorial R_E for electrons above 500 keV.
# Declared+: Kellerman et al. (2014), as reported in "Electron intensity
# Declared+: measurements by the Cluster/RAPID/IES instrument in Earth's
# Declared+: radiation belts and ring current" (2018, arXiv:1809.00902) --
# Declared+: maximum electron flux at L = 4-5. The arXiv paper is the
# Declared+: document opened; Kellerman is the layer below it.
# Access: open full text, https://par.nsf.gov/servlets/purl/10575739
# Access+: (2026-09-13), the same paper Wiley serves.
# Note: a peak, not an edge; the edges are their own rows since 2026-09-14.
# Note+: The unit is L, the McIlwain parameter, because the value is the
# Note+: midpoint of an L band. L equals geocentric distance in Earth radii
# Note+: only where a field line crosses the magnetic equator, so any string
# Note+: printing this row says "at the equator".
# Note+: Baker et al. (2018) was REMOVED from this row's citation on
# Note+: 2026-09-14. His figure 30 uses L* = 4.5 as a selected analysis
# Note+: location and his figure 12 concerns variable peak positions, so
# Note+: neither identifies a universal peak. His span figure is on
# Note+: EARTH_VAN_ALLEN_OUTER_BELT_OUTER_EDGE, which is what it measures.
# Record: documentation/worksheets/L321_worksheet_3_van_allen_gemini31pro_20260913.md

# --- Van Allen belt edges, L-305 item 7 (2026-09-14) ------------------------
# The spans used to live in each peak row's "# Note:" line, as prose, while
# the hovers, the information panel and the gallery config each typed their
# own copy. A Note became a store. These rows hold the figures instead, so a
# string can interpolate one and a checker can compare them.
#
# FRAME: geocentric, in the geomagnetic equatorial plane. That is the frame
# the cited papers state, and Tony ruled on 2026-09-14 that the store holds
# it. The literature is mixed -- Y. X. Li et al. (2023) states the outer
# span in L shells and Baker et al. (2018) states it both ways -- so "the
# frame the source states" only answers once the row names WHICH source its
# figure follows. Each row does, and the frame travels with it.
#
# Design record:
# documentation/DESIGN_a_figure_in_prose_needs_a_home_rev3_20260914.md

EARTH_VAN_ALLEN_INNER_BELT_INNER_EDGE = 1.1
# Unit: r_earth
# Status: measured V_SOURCED 2026-09-14 -- open full text
# Source: Meredith, N. P., Horne, R. B., Kersten, T., Fraser, B. J. and
# Source+: Grew, R. S. (2014), "Global morphology and spectral properties of
# Source+: EMIC waves derived from CRRES observations", J. Geophys. Res.
# Source+: Space Physics 119, 5328-5342, doi:10.1002/2014JA020064 --
# Source+: introduction, first paragraph: the inner belt extends from about
# Source+: 1.1 to 2 Earth radii in the geomagnetic equatorial plane.
# Access: open full text,
# Access+: https://nora.nerc.ac.uk/id/eprint/507469/1/jgra51120.pdf
# Access+: (2026-09-13).
# Note: Meredith states this as background and passes it on from Baker et
# Note+: al. (2007), which is the layer below rather than the source.
# Note+: Koskinen and Kilpua (2022) sec. 1.1 corroborate 1.1 to 2 R_E, and
# Note+: are NOT this row's source, because they state it for the inner
# Note+: ELECTRON belt; the same section puts the energetic protons over
# Note+: about 1.1 to 3 R_E, so they cannot carry a hover calling this belt
# Note+: mainly protons. The figure matched and the scope did not.
# Record: documentation/worksheets/L321_worksheet_3_van_allen_gemini31pro_20260913.md

EARTH_VAN_ALLEN_INNER_BELT_OUTER_EDGE = 2.0
# Unit: r_earth
# Status: measured V_SOURCED 2026-09-14 -- open full text
# Source: Meredith et al. (2014), doi:10.1002/2014JA020064 -- introduction,
# Source+: first paragraph, the outer end of the same stated span.
# Access: open full text,
# Access+: https://nora.nerc.ac.uk/id/eprint/507469/1/jgra51120.pdf
# Access+: (2026-09-13).
# Note: two rows rather than a tuple, because provenance is per number and
# Note+: the two edges do not move together. The layer below is Baker et al.
# Note+: (2007), as above.
# Record: documentation/worksheets/L321_worksheet_3_van_allen_gemini31pro_20260913.md

EARTH_VAN_ALLEN_OUTER_BELT_INNER_EDGE = 3.0
# Unit: r_earth
# Status: measured V_SOURCED 2026-09-14 -- open full text
# Source: Meredith et al. (2014), doi:10.1002/2014JA020064 -- introduction,
# Source+: first paragraph: the outer belt extends from 3 to 7 R_E. Li, Tu,
# Source+: Selesnick and Huang (2024), "Modeling the contribution of
# Source+: precipitation loss to a radiation belt electron dropout observed
# Source+: by Van Allen Probes", J. Geophys. Res. Space Physics 129,
# Source+: e2023JA032171, doi:10.1029/2023JA032171 -- introduction, first
# Source+: paragraph, the same span independently.
# Access: open full text,
# Access+: https://nora.nerc.ac.uk/id/eprint/507469/1/jgra51120.pdf and
# Access+: https://par.nsf.gov/servlets/purl/10578577 (2026-09-13).
# Note: the layer below is Paulikas and Blake (1979) with Baker et al.
# Note+: (1986) for Meredith, and Ganushkina et al. (2011) with Van Allen et
# Note+: al. (1958) for Li. Both papers state the span as background.
# Note+: Baker et al. (2018) sec. 2 gives the same inner edge, r ~ 3 R_E
# Note+: from SAMPEX, and reports it reaching L ~ 2.5 under strong driving.
# Record: documentation/worksheets/L321_worksheet_3_van_allen_gemini31pro_20260913.md

EARTH_VAN_ALLEN_OUTER_BELT_OUTER_EDGE = 7.0
# Unit: r_earth
# Status: measured V_SOURCED 2026-09-14 -- open full text
# Source: Meredith et al. (2014), doi:10.1002/2014JA020064, and Li, Tu et
# Source+: al. (2024), doi:10.1029/2023JA032171 -- both state the outer belt
# Source+: extending to 7 Earth radii, in their introductions.
# Access: open full text,
# Access+: https://nora.nerc.ac.uk/id/eprint/507469/1/jgra51120.pdf and
# Access+: https://par.nsf.gov/servlets/purl/10578577 (2026-09-13).
# Note: the measuring review disagrees on the outside and the disagreement
# Note+: is recorded rather than resolved by silence. Baker et al. (2018),
# Note+: doi:10.1007/s11214-017-0452-7, sec. 2 and 3.4, puts the outer zone
# Note+: at r ~ 3 to >= 6.5 R_E from SAMPEX and, in L, at about 3.0 to 6.5.
# Note+: Koskinen and Kilpua (2022) sec. 1.1 put the outer reach at 7 to 10
# Note+: R_E, which is why 10.4 R_E is not the physical impossibility one
# Note+: checker called it: the belt's outer edge approaches the
# Note+: magnetopause, and magnetopause shadowing is a standard loss
# Note+: mechanism.
# Record: documentation/worksheets/L321_worksheet_3_van_allen_gemini31pro_20260913.md
# Record: documentation/worksheets/Fable51_medium_citation_worksheet_3_van_allen_belts_RETURN.md

# --- magnetosphere: two published models, L-305 (2026-09-12) ----------------
# The magnetopause is Shue et al. (1998), the bow shock is Jelinek et al.
# (2012). They are separate fits in separate frames -- Shue in aberrated GSM,
# Jelinek in aberrated GSE -- and both are rotationally symmetric about the
# aberrated Sun-Earth line, so the two frames share the X axis and nothing
# drawn depends on the difference. Do not "fix" a frame mismatch here; there
# is none to fix. The two models disagree about the magnetopause nose by
# about 1 R_E (Shue 10.25, Jelinek 11.24), which is inside Shue's own fit
# scatter of 1.23 R_E, and the hovers say so rather than letting the pair
# read as one measurement.
#
# The declared conditions come first because the standoffs are evaluated at
# them. L-314 replaces all three with a measured feed.

EARTH_SOLAR_WIND_PRESSURE_NPA = 2.0
# Unit: npa
# Status: declared pending 2026-09-12 -- L-314
# Declared: the solar wind dynamic pressure both fits are evaluated at.
# Declared+: Shue et al. (1998) p. 17,695 uses Dp = 2 nPa as an average
# Declared+: value, which is the paper's own reason for this pick. It sits
# Declared+: inside Shue's fitted range (0.5 to 8.5 nPa, p. 17,693) and
# Declared+: inside Jelinek's recommended range (0.6 to 11 nPa, conclusion
# Declared+: para. 30).
# Note: Shue's Dp includes the helium contribution by the factor
# Note+: (1 + 0.04 N_alpha), where N_alpha is the He++ concentration as a
# Note+: PERCENTAGE, 4 percent being used when it is missing -- so a factor
# Note+: of 1.16, not 1.0016 (fig. 1 caption, p. 17,692). A feed reporting
# Note+: proton density alone inherits that assumption. See L-314.

EARTH_SOLAR_WIND_BZ_NT = 0.0
# Unit: nt
# Status: declared pending 2026-09-12 -- L-314
# Declared: a neutral midpoint chosen here, NOT a figure from the paper.
# Declared+: Shue's own averages are +/- 4 nT, northward and southward taken
# Declared+: separately (p. 17,695). Zero is the unloaded case the drawn
# Declared+: shape shows, and it sits inside the fitted range
# Declared+: -18 nT < Bz < 15 nT (p. 17,693).

EARTH_SOLAR_WIND_SPEED_KM_S = 400.0
# Unit: km_s
# Status: declared pending 2026-09-12 -- L-314
# Declared: a nominal speed whose reason is NOT YET WRITTEN, and that is the
# Declared+: honest state of this row. The 410 km/s on Shue p. 17,694 is the
# Declared+: speed during one January 1997 event and does not source a
# Declared+: nominal figure.
# Note: neither standoff depends on this. It sets the aberration angle,
# Note+: atan(v_orbit / v_sw), about 4.3 degrees at this value.

EARTH_MAGNETOPAUSE_SHUE_A1_RADII = 10.22
# Unit: r_earth
# Status: measured V_SOURCED 2026-09-11 -- open full text
# Source: Shue, J.-H., Song, P., Russell, C. T., Steinberg, J. T., Chao,
# Source+: J. K., Zastenker, G., Vaisberg, O. L., Kokubun, S., Singer, H. J.,
# Source+: Detman, T. R. and Kawano, H. (1998), "Magnetopause location under
# Source+: extreme solar wind conditions", J. Geophys. Res. 103(A8),
# Source+: 17691-17700, doi:10.1029/98JA01103 -- Table 1 "After Fit" row a1,
# Source+: p. 17,698: 10.22 +/- 0.10 R_E. The leading term of eq. 10.
# Access: open full text, https://doi.org/10.1029/98JA01103, read from the
# Access+: PDF 2026-09-11. Sandbox fetches of the DOI page are refused by bot
# Access+: detection, which is not a paywall; the download was Tony's.
# Record: documentation/L305_gap1_read_record_20260911.md
# Note: eq. 10, p. 17,697, is the standoff --
# Note+: r0 = {a1 + a2 tanh[a3 (Bz + a4)]} Dp^(-1/a5), with Bz in nT, Dp in
# Note+: nPa and r0 in Earth radii. The +/- figures on rows a1 to a8 are
# Note+: standard deviations from 200 Monte Carlo refits (p. 17,698).

EARTH_MAGNETOPAUSE_SHUE_A2_RADII = 1.29
# Unit: r_earth
# Status: measured V_SOURCED 2026-09-11 -- open full text
# Source: Shue et al. (1998), doi:10.1029/98JA01103 -- Table 1 "After Fit"
# Source+: row a2, p. 17,698: 1.29 +/- 0.06 R_E. The amplitude of eq. 10's
# Source+: Bz term.
# Access: open full text, https://doi.org/10.1029/98JA01103 (2026-09-11).

EARTH_MAGNETOPAUSE_SHUE_A3_PER_NT = 0.184
# Unit: per_nt
# Status: measured V_SOURCED 2026-09-11 -- open full text
# Source: Shue et al. (1998), doi:10.1029/98JA01103 -- Table 1 "After Fit"
# Source+: row a3, p. 17,698: 0.184 +/- 0.007 per nT. The scale inside
# Source+: eq. 10's hyperbolic tangent.
# Access: open full text, https://doi.org/10.1029/98JA01103 (2026-09-11).

EARTH_MAGNETOPAUSE_SHUE_A4_NT = 8.14
# Unit: nt
# Status: measured V_SOURCED 2026-09-11 -- open full text
# Source: Shue et al. (1998), doi:10.1029/98JA01103 -- Table 1 "After Fit"
# Source+: row a4, p. 17,698: 8.14 +/- 0.39 nT. The Bz offset inside
# Source+: eq. 10's hyperbolic tangent.
# Access: open full text, https://doi.org/10.1029/98JA01103 (2026-09-11).

EARTH_MAGNETOPAUSE_SHUE_A5 = 6.6
# Unit: dimensionless
# Status: measured V_SOURCED 2026-09-11 -- open full text
# Source: Shue et al. (1998), doi:10.1029/98JA01103 -- Table 1 "After Fit"
# Source+: row a5, p. 17,698: 6.6 +/- 0.5. The pressure exponent, r0 varying
# Source+: as Dp^(-1/a5).
# Access: open full text, https://doi.org/10.1029/98JA01103 (2026-09-11).
# Note: the name carries no unit suffix because the value has no unit. The
# Note+: "# Unit:" line above is the declaration; nothing is renamed to suit
# Note+: a reader of names (L-322).

EARTH_MAGNETOPAUSE_SHUE_A6 = 0.58
# Unit: dimensionless
# Status: measured V_SOURCED 2026-09-11 -- open full text
# Source: Shue et al. (1998), doi:10.1029/98JA01103 -- Table 1 "After Fit"
# Source+: row a6, p. 17,698: 0.58 +/- 0.01. The leading term of eq. 11.
# Access: open full text, https://doi.org/10.1029/98JA01103 (2026-09-11).
# Note: eq. 11, p. 17,697, is the flaring --
# Note+: alpha = (a6 + a7 Bz) [1 + a8 ln(Dp)], and the surface is then
# Note+: r = r0 [2 / (1 + cos theta)]^alpha, theta measured from the
# Note+: aberrated Sun-Earth line.

EARTH_MAGNETOPAUSE_SHUE_A7_PER_NT = -0.007
# Unit: per_nt
# Status: measured V_SOURCED 2026-09-11 -- open full text
# Source: Shue et al. (1998), doi:10.1029/98JA01103 -- Table 1 "After Fit"
# Source+: row a7, p. 17,698: -0.007 +/- 0.0005 per nT. Eq. 11 prints it as
# Source+: the subtraction (0.58 - 0.007 Bz); the table carries the sign, so
# Source+: the stored coefficient is negative and adds.
# Access: open full text, https://doi.org/10.1029/98JA01103 (2026-09-11).

EARTH_MAGNETOPAUSE_SHUE_A8 = 0.024
# Unit: dimensionless
# Status: measured V_SOURCED 2026-09-11 -- open full text
# Source: Shue et al. (1998), doi:10.1029/98JA01103 -- Table 1 "After Fit"
# Source+: row a8, p. 17,698: 0.024 +/- 0.0004. The pressure term of eq. 11.
# Access: open full text, https://doi.org/10.1029/98JA01103 (2026-09-11).
# Note: the Kumar and Pulkkinen EGUsphere preprint (2024-1113) prints this
# Note+: as 0.24. That is a typo in the preprint; the primary says 0.024.
# Note+: Recorded so nobody re-derives the doubt.

EARTH_MAGNETOPAUSE_CUT_ANGLE_DEG = 120.0
# Unit: deg
# Status: declared 2026-09-14 -- a drawing limit, not an edge
# Declared: where the drawn magnetopause stops, measured from the nose.
# Declared+: Shue's surface has no end. At the store's declared conditions
# Declared+: the flaring is 0.5896, and for any flaring at or above 0.5 the
# Declared+: radius grows without bound as theta approaches 180 degrees, so
# Declared+: a drawing must choose a stop.
# Declared+: Shue et al. (1998), doi:10.1029/98JA01103 -- fig. 6, p. 17,695,
# Declared+: plots the model's own uncertainty out to 120 degrees solar
# Declared+: zenith angle, the furthest the authors evaluate their own model.
# Declared+: Past that the drawing would show a surface the paper does not.
# Declared+: The paper states no angular range for the crossings it was
# Declared+: fitted to; that number exists only in Shue et al. (1997), which
# Declared+: is not read.
# Access: open full text, https://doi.org/10.1029/98JA01103 (2026-09-11).
# Record: documentation/L305_gap1_read_record_20260911.md
# Note: the same shape as EARTH_BOW_SHOCK_CUT_ANGLE_DEG and a different
# Note+: kind of reason. The bow shock stops where its crossings stopped,
# Note+: within 7 hours of local noon. The magnetopause stops where its
# Note+: authors stopped plotting. Both are drawing limits; neither is an
# Note+: edge of anything physical, and the hover has to say so.
# Note+: At the declared conditions the cut falls at r = 23.2 R_E,
# Note+: x = -11.6 R_E, R_yz = 20.1 R_E. For comparison the bow shock cut
# Note+: falls at x = -7.8 R_E, R_yz = 29.0 R_E, so the drawn shock is the
# Note+: wider and shorter of the two. That is not a physical statement
# Note+: about the two boundaries; it is two drawing limits set by two
# Note+: different papers for two different reasons.
# Note: Tony's ruling, 2026-09-14 (L-305 item 6b).

EARTH_BOW_SHOCK_JELINEK_R0_RADII = 15.02
# Unit: r_earth
# Status: measured V_SOURCED 2026-09-10 -- open full text
# Source: Jelinek, K., Nemecek, Z. and Safrankova, J. (2012), "A new
# Source+: approach to magnetopause and bow shock modeling based on automated
# Source+: region identification", J. Geophys. Res. 117, A05208,
# Source+: doi:10.1029/2011JA017252 -- eq. 14, p. 5: R_BS = 15.02 p^(-1/6.55),
# Source+: so 15.02 R_E is the bow shock stand-off at p = 1 nPa. Fitted from
# Source+: Themis crossings, in aberrated GSE.
# Access: open full text, https://doi.org/10.1029/2011JA017252, read from the
# Access+: PDF 2026-09-10.
# Record: documentation/L305_gap1_read_record_20260911.md
# Note: the paper states no uncertainty on its six fitted numbers. It gives
# Note+: the scatter of crossings about the model instead -- fig. 7, 0.69 R_E
# Note+: for the bow shock and 0.76 R_E for the magnetopause.
# Note+: Do NOT pick up eqs. 17-18 (12.90 and 14.94). Those are a validation
# Note+: refit against observed crossings (sec. 5.2), not the model, and the
# Note+: two pairs are close enough to be mistaken for one another.

EARTH_BOW_SHOCK_JELINEK_EPS = 6.55
# Unit: dimensionless
# Status: measured V_SOURCED 2026-09-10 -- open full text
# Source: Jelinek et al. (2012), doi:10.1029/2011JA017252 -- eq. 14, p. 5:
# Source+: the pressure exponent of R_BS = 15.02 p^(-1/6.55).
# Access: open full text, https://doi.org/10.1029/2011JA017252 (2026-09-10).

EARTH_BOW_SHOCK_JELINEK_LAMBDA = 1.17
# Unit: dimensionless
# Status: measured V_SOURCED 2026-09-10 -- open full text
# Source: Jelinek et al. (2012), doi:10.1029/2011JA017252 -- sec. 4, in the
# Source+: text after eq. 11: lambda = 1.17 for the bow shock (1.54 for the
# Source+: magnetopause, which this file does not store because the
# Source+: magnetopause is Shue's).
# Access: open full text, https://doi.org/10.1029/2011JA017252 (2026-09-10).
# Note: the per-boundary scaling of the parabolic surface, eqs. 15-16:
# Note+: x = R0 p^(-1/eps) - tau^2 / 2 and
# Note+: R_yz = sqrt(2 R0 p^(-1/eps)) tau / lambda.

EARTH_BOW_SHOCK_CUT_ANGLE_DEG = 105.0
# Unit: deg
# Status: measured V_SOURCED 2026-09-11 -- open full text
# Source: Jelinek et al. (2012), doi:10.1029/2011JA017252 -- sec. 2 para. 9,
# Source+: p. 2: the regions are identified on the whole dayside and toward
# Source+: the flanks within +/- 7 hours of local time about local noon.
# Source+: That envelope is the extent over which the fit is supported.
# Derived: 7 h x 15 deg/h = 105 deg from the nose. The paper gives the
# Derived+: hours; the degrees are this file's conversion, exact by
# Derived+: definition (360 deg / 24 h). Same shape as EARTH_GM_KM3_S2,
# Derived+: which converts IERS's m^3 s^-2 and stays one measured row.
# Access: open full text, https://doi.org/10.1029/2011JA017252 (2026-09-11).
# Note: the drawn bow shock stops here. Beyond it the paraboloid is
# Note+: unsupported -- it reaches 67 R_E at x = -100 R_E -- and the real
# Note+: shock follows a Mach cone the paper does not model. At the declared
# Note+: pressure the cut falls at x = -7.8 R_E, R_yz = 29.0 R_E.

EARTH_MAGNETOPAUSE_SHUE_SCATTER_RADII = 1.23
# Unit: r_earth
# Status: measured V_SOURCED 2026-09-14 -- open full text
# Source: Shue et al. (1998), doi:10.1029/98JA01103, p. 17,697 -- the
# Source+: improved model's standard deviation against the observed
# Source+: magnetopause crossings it was fitted to is 1.23 R_E.
# Access: open full text, https://doi.org/10.1029/98JA01103, read from the
# Access+: PDF 2026-09-11.
# Note: a spread of real crossings about the fitted surface, not an
# Note+: uncertainty on the standoff below, which is an evaluation of eq. 10
# Note+: at the declared conditions and carries its own inputs' figures.
# Note+: It is also the yardstick for the seam between the two published
# Note+: fits: Shue and Jelinek disagree about the magnetopause nose by
# Note+: about 1 R_E, which sits inside this one figure alone.
# Record: documentation/L305_gap1_read_record_20260911.md

EARTH_MAGNETOPAUSE_STANDOFF_RADII = 10.25
# Unit: r_earth
# Status: derived 2026-09-12 -- inherits EARTH_MAGNETOPAUSE_SHUE_A1_RADII
# Status+: through EARTH_MAGNETOPAUSE_SHUE_A5, EARTH_SOLAR_WIND_PRESSURE_NPA
# Status+: and EARTH_SOLAR_WIND_BZ_NT
# Derived: Shue eq. 10 at the declared conditions --
# Derived+: (a1 + a2 tanh[a3 (Bz + a4)]) Dp^(-1/a5)
# Derived+: = (10.22 + 1.29 tanh(0.184 x 8.14)) x 2^(-1/6.6)
# Derived+: = 10.251872972379905.
# Derived+: REPORT 10.25. Table 1 gives a1 to +/- 0.10 R_E and a5 to
# Derived+: +/- 0.5, and either one alone moves r0 by about +/- 0.09, so the
# Derived+: fourth figure is the last one the coefficients support.
# Note: the STORED value is that reported figure, not the arithmetic
# Note+: result. Tony's ruling, 2026-09-12 (L-325): a store carries the
# Note+: figures its sources support. Sixteen digits on a value uncertain
# Note+: in the first decimal is calculator output, not precision. The
# Note+: arithmetic stays recorded above, so the row is still auditable.
# Note+: This row was ALREADY a literal and so already followed nothing:
# Note+: the Status line above names EARTH_SOLAR_WIND_PRESSURE_NPA, which
# Note+: is declared pending (L-314), and had it moved this value would
# Note+: have gone quietly stale with no test anywhere to catch it.
# Note+: test_derived_figures.py now recomputes this row from the inputs
# Note+: the Status line names and fails when the rounding stops holding.
# Note+: That check is what replaces an expression's automatic
# Note+: recomputation, and it announces rather than moving a published
# Note+: number quietly. An earlier Note here said L-322 would turn this
# Note+: row back into an expression once the gallery's parser is retired.
# Note+: That plan is superseded: the stored form is the reported figure
# Note+: whatever the parser can read.
# Note+: Superseded a typed 10.0 on 2026-09-12 (L-305). The old row's own
# Note+: Source already read 10.2 R_E at these conditions while the value
# Note+: read 10.0 -- a drift inside one row, cleared here.
# Note+: Quiet-time. Under storm compression the magnetopause can fall
# Note+: inside geostationary orbit (6.6 R_E); the drawn shape is the quiet
# Note+: one. Lugaz et al. (2016), doi:10.1038/ncomms13001, gives 9-11 R_E
# Note+: as the typical subsolar distance, which contains this.

EARTH_BOW_SHOCK_JELINEK_SCATTER_RADII = 0.69
# Unit: r_earth
# Status: measured V_SOURCED 2026-09-14 -- open full text
# Source: Jelinek, Nemecek and Safrankova (2012), J. Geophys. Res. 117,
# Source+: A05208, doi:10.1029/2011JA017252 -- fig. 7: the scatter of
# Source+: observed crossings about the bow shock model is 0.69 R_E. The
# Source+: same figure gives 0.76 R_E for their magnetopause.
# Access: open full text, https://doi.org/10.1029/2011JA017252 (2026-09-10).
# Note: this is NOT an uncertainty on the model's own numbers -- the paper
# Note+: states none for its six fitted values. It is how far real crossings
# Note+: sit from the surface the model draws, which is a different quantity
# Note+: and the one a visitor needs in order not to read an evaluated model
# Note+: as a measurement. The standoff below therefore keeps the figures its
# Note+: inputs support and prints this beside it.
# Record: documentation/L305_gap1_read_record_20260911.md

EARTH_BOW_SHOCK_STANDOFF_RADII = 13.51
# Unit: r_earth
# Status: derived 2026-09-12 -- inherits EARTH_BOW_SHOCK_JELINEK_R0_RADII,
# Status+: EARTH_BOW_SHOCK_JELINEK_EPS and EARTH_SOLAR_WIND_PRESSURE_NPA
# Derived: Jelinek eq. 14 at the declared pressure -- 15.02 x 2^(-1/6.55)
# Derived+: = 13.511736110493397. REPORT 13.51: the paper states no
# Derived+: uncertainty on R0 or eps, so what bounds this is the crossing
# Derived+: scatter, 0.69 R_E (fig. 7).
# Note: the STORED value is that reported figure, not the arithmetic
# Note+: result. It was the expression
# Note+: EARTH_BOW_SHOCK_JELINEK_R0_RADII *
# Note+: EARTH_SOLAR_WIND_PRESSURE_NPA ** (-1 / EARTH_BOW_SHOCK_JELINEK_EPS)
# Note+: until 2026-09-12. Tony's ruling (L-325): a store carries the
# Note+: figures its sources support, and four of them against a crossing
# Note+: scatter of 0.69 R_E is already generous. Storing the expression
# Note+: bought an automatic recomputation when an input moved, which is
# Note+: a published number changing with nobody looking;
# Note+: test_derived_figures.py recomputes this row from its inputs and
# Note+: FAILS instead, which is the same protection said out loud.
# Note+: superseded a typed 12.5 on 2026-09-12 (L-305). Two claims went with
# Note+: it. The value was the midpoint of Lugaz et al. (2016)'s 11-14 R_E,
# Note+: which is not a model; and the shape was cited to Farris & Russell
# Note+: (1994), doi:10.1029/94JA01020, which is a semiempirical relation for
# Note+: the STANDOFF at a given Mach number and takes obstacle shape as an
# Note+: INPUT -- so citing it for a shape was a miscitation. Lugaz's
# Note+: 11-14 R_E survives as a corroborating range and this value sits
# Note+: inside it.
# Note+: The stale Note saying the shell draws 15 R_E is gone too:
# Note+: earth_visualization_shells.py has read this constant since L-291.

EARTH_MAGNETOTAIL_OBSERVED_RADII = 220.0
# Unit: r_earth
# Status: measured V_SOURCED 2026-09-14 -- abstract, open
# Source: Slavin, J. A., Tsurutani, B. T., Smith, E. J., Jones, D. E. and
# Source+: Sibeck, D. G. (1983), "Average configuration of the distant (less
# Source+: than 220-earth-radii) magnetotail - Initial ISEE-3 magnetic field
# Source+: results", Geophys. Res. Lett. 10(10), 973-976,
# Source+: doi:10.1029/GL010i010p00973 -- the abstract states that the
# Source+: magnetotail retains much of its near-Earth structure out to
# Source+: X = -220 Earth radii, that flaring ceases at 100-120 R_E, and
# Source+: that the tail diameter settles near 60 R_E.
# Access: abstract, open, https://ntrs.nasa.gov/citations/19830066648
# Access+: (NTRS document 19830066648, read 2026-09-14). The Wiley pages are
# Access+: walled. The NTRS abstract prints "-100 to -1200 earth radii" where
# Access+: -120 is meant.
# Note: read as OBSERVED TO AT LEAST, the same form as EARTH_GEOCORONA_RADII
# Note+: below. 220 R_E is ISEE-3's reach on its first two tail passes, not
# Note+: an edge: the tail kept its near-Earth structure out to the
# Note+: spacecraft's apogee, so the figure is bounded by the orbit.
# Note+: Two further signatures are recorded here so a later session does not
# Note+: read this row as ignorance of them. Both are more distant and less
# Note+: like a tail, which is why neither is the value.
# Note+: Ness, N. F., Scearce, C. S. and Cantarano, S. C. (1967), "Probable
# Note+: observations of the geomagnetic tail at 10^3 Earth radii by Pioneer
# Note+: 7", J. Geophys. Res. 72(15), 3769-3776,
# Note+: doi:10.1029/JZ072i015p03769 -- Pioneer 7 was in the expected tail
# Note+: region at 900 to 1,050 R_E from 26 September to 3 October 1966, with
# Note+: tail-like fields appearing intermittently and no coherent,
# Note+: well-ordered tail observed. The title says "probable". Open as GSFC
# Note+: preprint X-612-67-183,
# Note+: https://ntrs.nasa.gov/citations/19670023428
# Note+: Intriligator, D. S. et al. (1979), Geophys. Res. Lett. 6, 585 --
# Note+: tail-ASSOCIATED phenomena near 3,100 R_E, read by later work as
# Note+: signatures disconnected from Earth rather than a tail. Abstract
# Note+: open, https://ntrs.nasa.gov/citations/19790061874
# Note+: The DRAWN tail length is 100 R_E, a drawing parameter at
# Note+: earth_visualization_shells.py line 765, and it is NOT promoted here
# Note+: (A Drawing Approximation Does Not Promote). It sits inside the
# Note+: coherent range this row records.
# Record: documentation/worksheets/L321_worksheet_1_magnetopause_fable_high_recheck_20260913.md

EARTH_GEOCORONA_RADII = 100.0
# Source: Baliukin, I. I., Bertaux, J.-L., Quemerais, E., Izmodenov, V.
# Source+: V. & Schmidt, W. (2019), "SWAN/SOHO Lyman-alpha mapping: the
# Source+: hydrogen geocorona extends well beyond the Moon", J. Geophys.
# Source+: Res. Space Physics 124, 861-885, doi:10.1029/2018JA026136 --
# Source+: the geocorona is detected to at least 100 Earth radii.
# Note: a detection floor, not an edge -- the hydrogen thins without a
# Note+: boundary. The shell is drawn at the sourced floor and its hover
# Note+: says so. It encloses the Moon's orbit at about 60 radii.
# --- end Earth exhibit block --------------------------------------------------

JUPITER_EQUATORIAL_RADIUS_KM = 71492.0
# Source: IAU 2015 Resolution B3 -- nominal jovian equatorial radius
# Ref: Prsa et al. 2016, AJ 152:41 (arXiv:1605.09788)
# Cross-checked: Claude 2026-08-02 -- IAU B3 (worksheet_claude_constants_new.md)
# Cross-checked: GPT 2026-08-02 -- IAU B3 (constants_new_citation_verification_gpt.md)

JUPITER_POLAR_RADIUS_KM = 66854.0
# Source: IAU 2015 Resolution B3 -- nominal jovian polar radius
# Ref: Prsa et al. 2016, AJ 152:41 (arXiv:1605.09788)
# Cross-checked: Claude 2026-08-02 -- IAU B3 (worksheet_claude_constants_new.md)
# Cross-checked: GPT 2026-08-02 -- IAU B3 (constants_new_citation_verification_gpt.md)

SPEED_OF_LIGHT_KM_S = 299792.458
# Source: NIST/SI exact definition
# Ref: https://physics.nist.gov/cgi-bin/cuu/Value?c
# Cross-checked: Claude 2026-08-02 -- NIST/SI (worksheet_claude_constants_new.md)
# Cross-checked: GPT 2026-08-02 -- NIST/SI (constants_new_citation_verification_gpt.md)


# ============================================================
# DERIVED CONSTANTS (computed from primaries above)
# ============================================================
# Do not hardcode these values. They are computed to ensure
# consistency with the IAU primary definitions.

SOLAR_RADIUS_AU = SUN_RADIUS_KM / KM_PER_AU
# Derived: 695700 / 149597870.7 = 0.004650467...
# Derived+: Previous hardcoded value was 0.00465047 (consistent to 6 sig figs)

LIGHT_MINUTES_PER_AU = KM_PER_AU / SPEED_OF_LIGHT_KM_S / 60.0
# Derived: 149597870.7 / 299792.458 / 60 = 8.31675...
# Derived+: Previous hardcoded value was 8.3167 (consistent to 5 sig figs)

AU_PER_LIGHT_YEAR = (SPEED_OF_LIGHT_KM_S * 365.25 * 86400.0) / KM_PER_AU
# Derived: 299792.458 km/s x Julian year (365.25 d x 86400 s) / KM_PER_AU
# Derived+: = 63,241.077 AU per light-year
# Source: IAU -- the light-year is defined as c x the Julian year.
# Ref: https://www.iau.org/public/themes/measuring/
# Note: reproduces the IAU published light-year (9.4607304726e12 km)
#       to ten significant figures. Added 2026-08-07 (L-179) so that
#       display text can derive light-year figures instead of typing
#       them beside an AU value that then drifts away from them.


# ============================================================
# GUI CONSTANTS (application settings, not physical)
# ============================================================

DEFAULT_MARKER_SIZE = 7
HORIZONS_MAX_DATE = datetime(2199, 12, 29, 0, 0, 0)
CENTER_MARKER_SIZE = 10  # For central objects like the Sun


# ============================================================
# SOLAR STRUCTURE (in AU unless noted)
# ============================================================
# Interior boundaries are approximate; based on standard solar models.
# Source: Carroll & Ostlie, "Introduction to Modern Astrophysics" (2017)
# Also: https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html
# Cross-checked: Gemini 2026-08-02 -- Carroll & Ostlie (worksheet_gemini_constants_remaining.md)
# Cross-checked: GPT 2026-08-02 -- NASA Sun Fact Sheet (constants_new_citation_verification_gpt.md)

CORE_AU = 0.2 * SOLAR_RADIUS_AU
# Visualization boundary at low end of conventional 0.2-0.25 R_sun core range
# Source: Bahcall, Pinsonneault & Basu (2001), ApJ 555:990 (radial profiles)
# Also: Carroll & Ostlie (2017), Ch. 11 gives 0.2-0.25 R_sun
# Cross-checked: Gemini 2026-08-02 -- Carroll & Ostlie (worksheet_gemini_constants_remaining.md)
# Cross-checked: GPT 2026-08-02 -- NASA solar structure (constants_remaining_independent_verification_gpt.md)

RADIATIVE_ZONE_AU = 0.713 * SOLAR_RADIUS_AU
# Source: Christensen-Dalsgaard, Gough & Thompson (1991), ApJ 378:413,
#   "The depth of the solar convection zone" -- convection-zone DEPTH
#   measured at 0.287 +/- 0.003 solar radii.
# Derived: base of the convection zone = 1 - 0.287 = 0.713 R_sun. A
# Derived+: subtraction, so decimal PLACES govern: three, matching the
# Derived+: stated +/- 0.003.
# Status: measured V_SOURCED 2026-08-29 -- verified against the source
# Access: free NASA ADS abstract, bibcode 1991ApJ...378..413C. Also
#   corroborated in open arXiv text (astro-ph/0511779), which gives
#   the 1991 estimate as 0.713 +/- 0.003 and Basu & Antia (2004) as
#   0.7133 +/- 0.0005. The tighter figure is NOT adopted: it is a
#   different work, and taking it is a re-sourcing, not a rounding.
# Corrected: 2026-08-29 (L-258) -- held 0.7 beside a comment saying
#   it rounded 0.713, which is the founding case for The Store
#   Carries the Verified Figure (provenance-discipline 2.10). The
#   comment also called this the helioseismic TACHOCLINE; the paper
#   measures the base of the convection zone, and the tachocline is
#   the shear layer at approximately that depth -- a neighbouring
#   claim, not the cited one.
# Cross-check retired: 2026-08-29 -- two legs dated 2026-08-02 were
#   stripped, per A Cross-Check Retires With Its Value or Its
#   Citation. Both triggers fired at once: the value moved 0.7 ->
#   0.713, and the source line was repaired. The GPT leg certified
#   0.7 against "helioseismology literature" and a check of the old
#   value is not a check of the new one. The Gemini leg cited
#   Carroll & Ostlie, which is not the work this row cites, so it
#   certified a neighbouring claim. Recorded rather than deleted
#   silently: a removal leaves no trace otherwise.

# Solar atmosphere (in solar radii)
# RETIRED 2026-08-16 -- CHROMOSPHERE_RADII = 1.1, the DRAWN shell radius.
# The chromosphere now draws at CHROMOSPHERE_PHYSICAL_RADII (below), at
# true scale. Tony's ruling: the user should see the real proportion, and
# a 2000 km skin reading as a hairline on the photosphere IS the lesson.
# Discoverability moved to the legend name and the info marker (see
# orrery-coding-conventions, 20-degree info marker separation).
# L-180 (2026-08-07) required display text to declare the stylization. It
# stays ON RECORD and DORMANT: it governs nothing while no solar shell is
# stylized, and is NOT categorically superseded -- a future stylization
# anywhere would revive it (Tony's ruling, 2026-08-16).
# The 2026-08-02 cross-checks were checks on the drawn value and retire
# with it; the physical value below carries its own.

CHROMOSPHERE_PHYSICAL_KM = 2000.0
# Source: Carroll & Ostlie, An Introduction to Modern Astrophysics,
# Source+: Ch. 11 -- chromosphere extends ~2000 km above the photosphere.
# Cross-checked: Gemini 2026-08-02 -- Carroll & Ostlie (worksheet_gemini_constants_remaining.md)
# Note: the PHYSICAL extent, and since 2026-08-16 the drawn one too.
# Note+: CHROMOSPHERE_PHYSICAL_RADII below converts it to solar radii and
# Note+: is what the shell draws at. The 1.1 stylization is retired.

CHROMOSPHERE_PHYSICAL_RADII = 1.0 + CHROMOSPHERE_PHYSICAL_KM / SUN_RADIUS_KM
# Derived: 1 + 2000 / 695700 = 1.002875... solar radii

INNER_CORONA_RADII = 3
# Source: Lamy, Gilardy, Llebaria, Quemerais & Ernandez, "Coronal
#   Photopolarimetry with the LASCO-C3 Coronagraph over 24 Years
#   [1996-2019]", Solar Physics -- Sec. 1: the inner solar corona,
#   "defined here as extending to ~3 R_sun from the center of the
#   solar disk".
# Status: declared 2026-08-29 -- a stated CONVENTION, not a
#   measurement. The inner (K-)corona has no sharp edge; the
#   boundary is where the F-corona overtakes the K-corona in
#   brightness, which happens across roughly 2-3 R_sun. 3 is the
#   top of that transition and the value the cited work adopts.
# Access: open arXiv full text, arXiv:2009.04820. Companion Paper I
#   (LASCO-C2) is Lamy et al. (2020), Solar Phys. 295:89.
# Corrected: 2026-08-29 (L-258) -- previously cited Golub &
#   Pasachoff, "The Solar Corona" (2010). That work fails the
#   access standard on its own terms: the independent nine-source
#   read of 2026-08-20 could locate it only as "Chapter 1", with no
#   figure and no findable position. The VALUE is unchanged and was
#   never in doubt; only the citation moved. (That read was about
#   helmet-streamer extent, a different claim, so its finding does
#   not transfer -- reachability does.)
# Cross-check retired: 2026-08-29 -- the Gemini leg of 2026-08-02
#   was stripped with the citation it checked. A cross-check of a
#   citation that no longer exists grants credit for nothing.

OUTER_CORONA_RADII = 50
# Source: Mann et al. (2004), A&A 414:1127
# See: Various; F-corona envelope extends to ~50 R_sun
# Note: Visualization boundary for F-corona envelope; not a sharp physical edge

# New shells (added April 2026); renamed and resourced 2026-08-22 (L-224)
HELMET_CUSP_RADII = 4.0
# Source: Suess & Nerney (2004), Adv. Space Res. 33:668-675, bibcode
#   2004AdSpR..33..668S -- "the closed field regions, or helmets, reach
#   no higher than 2-4 solar radii". 4.0 is the TOP of that stated
#   range, chosen so the drawn cusp does not understate the helmet.
# Note: this is the CUSP -- where the closed loops open -- not an outer
#   edge of the streamer belt. The belt has no outer edge: above the
#   cusp an open stalk continues into the slow solar wind. The renderer
#   draws the transition and dissolves the stalk rather than stopping
#   it (L-224, solar_visualization_shells.create_sun_streamer_band).
# Note: the source STATES 2-4 as established background; the paper's own
#   result is an analytic stagnation-flow model. Correctly cited, but do
#   not read 2-4 as this paper's measurement. Modelled, so the rendered
#   pinch is drawn soft rather than sharp.
# Corrected: 2026-08-22 -- was STREAMER_BELT_RADII = 6.0, an unsourced
#   visualization assumption sitting above the helmet and inside the
#   stalk, representing neither (L-210). The rename is the substance:
#   a constant named for the belt while holding the helmet cusp is the
#   name-meaning drift that produced the citation failure it replaces.
# Record: documentation/SOURCE_suess_nerney_2004_helmet_extent_20260821.md
# Review-note: this row's entire citation stack was removed on
#   2026-08-20 after an independent nine-source read, when it was
#   STREAMER_BELT_RADII = 6.0. Kept because the removals still stand
#   and the reasoning is why this row is now cited to a different work
#   for a different quantity. Recorded here
#   because a removal leaves no trace otherwise, and the next reader
#   should not have to re-derive why an uncited constant is uncited.
#   (a) "helmet streamers extend 4-6 R_sun" appeared in neither
#   cited work. (b) DeForest, Howard & McComas (2014), ApJ 787:124
#   was removed: its 6 R_sun is the inbound-wave DETECTION
#   THRESHOLD, not a streamer extent, and its streamer-belt result
#   is an Alfven surface at >= 15 R_sun -- a result that belongs to
#   ALFVEN_SURFACE_RADII (L-209), where it was rehomed 2026-08-21.
#   That figure read ">= 17" here until 2026-08-21; 17 is the arXiv
#   abstract-metadata value and the published paper says 15. (c) Golub &
#   Pasachoff, "The Solar Corona" (2010) was removed last: asked
#   for helmet-streamer extent it returned a cavity height near 1
#   R_sun and a loose 5-10 R_sun corona bound, located only as
#   "Chapter 1" -- the one return in nine that gave no figure, no
#   uncertainty and no findable position. (d) The two Cross-checked
#   legs went with them: Gemini 2026-08-02 against Golub &
#   Pasachoff, GPT 2026-08-02 against DeForest. A cross-check of a
#   citation that no longer exists grants credit for nothing.
#   The read was decisive about what to REMOVE and silent about what
#   to KEEP. Those need different evidence: a removal needs only the
#   absence of support, a citation needs its presence.
# Resolved: worksheet_claude-opus-5_pilot_constants_new_20260818.jsonl constants_new.py::HELMET_CUSP_RADII (as STREAMER_BELT_RADII) -- value held, unsupported citation removed, 4-6 R_sun range withdrawn (L-210); renamed and resourced 2026-08-22 (L-224)

ROCHE_LIMIT_RADII = 3.45
# Source: Murray & Dermott, "Solar System Dynamics" (1999), Sec. 4.6
# Derived: Fluid Roche limit formula: d = 2.44 * R * (rho_sun/rho_comet)^(1/3)
# Calculation: 2.44 * 1.0 * (1408/500)^(1/3) = 3.45 R_sun
# Calculation+: Using rho_sun = 1408 kg/m3, rho_comet ~ 500 kg/m3
# Cross-checked: Claude 2026-08-02 -- formula verified (worksheet_claude_constants_new.md)
# Cross-checked: GPT 2026-08-02 -- formula verified (constants_new_citation_verification_gpt.md)
# Note: Roche limit is NOT absolute; tensile strength allows survival
# Note+: inside it. Ikeya-Seki survived at 1.66 R_sun.

ALFVEN_SURFACE_RADII = 19.7
# Source: Kasper et al. (2021), Phys. Rev. Lett. 127:255101 -- first crossing
# Source+: 28 April 2021 09:33 UT; the sub-Alfvenic interval spans 19.7 to
# Source+: 18.4 solar radii from the center of the Sun
# See: HELIOCENTRIC, from Sun center, like every other shell radius in this
# See+: file. The widely quoted 18.8 R_sun is the ALTITUDE above the
# See+: photosphere, stated by the NASA/JHUAPL release of 14 December 2021;
# See+: the paper's own abstract gives the same event as 13 million km above
# See+: the photosphere. Adding one solar radius gives 19.8, which agrees
# See+: with the paper's own 19.7 to rounding.
# See+: PARKER_CLOSEST_RADII below carries the identical correction, made
# See+: 2026-04-15: 8.86 was altitude, 9.86 is from Sun center.
# See+: The surface is neither smooth nor fixed -- 10-20 R_sun varying with
# See+: solar activity, and the 2021 crossing was into a boundary layer above
# See+: a pseudostreamer rather than a global shell. 19.7 is the measured
# See+: first crossing, drawn here as a nominal sphere.
# Also: https://www.nasa.gov/feature/goddard/2021/nasa-enters-the-solar-atmosphere
# Also+: DeForest, Howard & McComas (2014), ApJ 787:124 -- the first remote
# Also+: measurement of the Alfven surface, a LOWER BOUND of 15 R_sun in the
# Also+: streamer belt and 12 R_sun over the polar coronal holes, from inbound
# Also+: wave motion in STEREO-A/COR2. It does NOT source the value above: it
# Also+: is a 2014 bound superseded by Kasper's 2021 in-situ crossing, and it
# Also+: is consistent with it (19.7 is above 15). Both of its bounds are
# Also+: INSTRUMENTAL rather than physical -- the paper states the streamer
# Also+: figure is set by the coronagraph's field of view and the polar figure
# Also+: by the noise floor, so the true surface lies somewhere above each.
# Also+: Rehomed here 2026-08-21 from HELMET_CUSP_RADII (then named
# Also+: STREAMER_BELT_RADII), where it had been
# Also+: cited for a claim it does not make (L-210).
# Review-note: this row previously would have received "17 R_sun in the
#   streamer belt, 12.5 over the poles". The published paper says 15 and 12,
#   in its abstract, its Section 5 and its Section 6. The 12.5/17 pair is the
#   arXiv ABSTRACT METADATA at arxiv.org/abs/1404.3235, which does not match
#   the accepted manuscript at arxiv.org/pdf/1404.3235; NASA ADS and Cranmer
#   et al. 2016 (ApJ 828:66) both carry 12 and 15. Two earlier reads reported
#   17 because both quoted that same listing page -- agreement between two
#   reads of one wrong page is not verification. Do not "restore" 17.
# Corrected: 2026-08-19 -- was 18.8, an altitude used as a heliocentric radius.
#   The prose above was carried on a bare Note: line and an invented
#   HELIOCENTRIC: label, neither of which the request builder reads, so it
#   reached no responder. It now rides on See+ legs that do carry (L-214).
#   The two Cross-checked legs dated 2026-08-02 certified 18.8 and were
#   stripped with it: a check of the old value is not a check of the new one.
# Resolved: worksheet_claude-opus-5_pilot_constants_new_20260818.jsonl constants_new.py::ALFVEN_SURFACE_RADII -- origin mismatch, value and Source replaced (L-209)


# ============================================================
# HELIOSPHERE BOUNDARIES (in AU)
# ============================================================

TERMINATION_SHOCK_AU = 94
# Source: Stone et al. (2005), Science 309:2017
# See: Voyager 1 crossed at 94 AU (Dec 2004)
# Also: Voyager 2 crossed at 84 AU (Aug 2007) -- asymmetric
# Cross-checked: Claude 2026-08-02 -- Stone et al. (worksheet_claude_constants_new.md)
# Cross-checked: GPT 2026-08-02 -- Stone et al. (constants_new_citation_verification_gpt.md)

HELIOPAUSE_RADII = 26148
# Note: This is in solar radii, not AU. 121.6 AU * 149597870.7 / 695700 = 26148 R_sun
# Source: Gurnett et al. (2013), Science 341:1489
# See: Voyager 1 crossed heliopause at ~121.6 AU (Aug 2012)
# Corrected: 2026-08-02 -- 26449 -> 26148 (prior comment used 123 AU;
#   Gurnett source says 121.6 AU; both checkers independently found the error)
# Cross-checked: Claude 2026-08-02 -- Gurnett et al. (worksheet_claude_constants_new.md)
# Cross-checked: GPT 2026-08-02 -- Gurnett et al. (constants_new_citation_verification_gpt.md)

# Oort Cloud and gravitational influence (in AU)
INNER_LIMIT_OORT_CLOUD_AU = 2000
# Source: Hills (1981); Oort (1950) -- inner edge estimate
# Note: Highly uncertain; ranges 2000-5000 AU in literature

INNER_OORT_CLOUD_AU = 20000
# Source: Hills (1981) -- outer edge of inner (Hills) cloud
# Note: Boundary between inner and outer Oort cloud is uncertain

OUTER_OORT_CLOUD_AU = 100000
# Source: Oort (1950); Weissman (1996)
# Note: Estimated outer boundary, ~0.5 parsec

GRAVITATIONAL_INFLUENCE_AU = 150000
# Source: Approximate Hill sphere of Sun in Milky Way (model-dependent)
# Source+: Estimates range 100,000-200,000 AU in the literature;
# Source+: depends on assumed enclosed galactic mass and Sun's orbital distance.
# Source+: ~2.4 light-years. Visualization boundary, not a measured value.
# Corrected: 2026-08-02 -- 126000 -> 150000 (prior value unsourced;
#   150000 AU is a round midpoint of the published range)
# Confirmed 2026-08-07 (Tony, L-179): 150000 stands, chosen as the
#   midpoint of the published range below. Display text must carry
#   the RANGE, not present the midpoint as a measurement.

GRAVITATIONAL_INFLUENCE_RANGE_AU = (100000, 200000)
# Source: spread of published Sun-in-Galaxy Hill sphere estimates;
# Source+: model-dependent, varying with assumed enclosed galactic mass
# Source+: and the Sun's galactocentric distance.
# Note: 100,000-200,000 AU = 1.6-3.2 light-years. Stored as DATA rather
#       than prose so display strings can interpolate the envelope
#       instead of restating the midpoint alone (L-179, 2026-08-07).

# Spacecraft reference
PARKER_CLOSEST_RADII = 9.86
# Source: https://parkersolarprobe.jhuapl.edu/The-Mission/index.php
# See: Parker Solar Probe perihelion 22, Dec 24, 2024
# Corrected: 2026-04-15 per Gemini review -- 8.86 was surface altitude,
#   9.86 is distance from Sun center (consistent with other shell radii).
#   Perihelion number corrected from 21 to 22.
# Note: 9.86 from Sun center. NASA press reports ~3.83 Mkm above
# Note+: the surface = 8.86 R_sun altitude. Same orbit, different reference.
# Cross-checked: Claude 2026-08-02 -- JHUAPL/Riley et al. (worksheet_claude_constants_new.md)
# Cross-checked: GPT 2026-08-02 -- NASA PSP mission data (constants_new_citation_verification_gpt.md)
# 9.86 R_sun = 6.86 million km = 0.0459 AU


# ============================================================
# CENTER BODY RADII (km)
# ============================================================
# Hybrid convention:
#   - Major planets (Earth through Neptune) + Sun + Pluto: equatorial
#     radius. Matches IAU 2015 nominal values and planetary-science
#     literature convention for "N radii" measurements (e.g. Io torus
#     at 5.9 R_J assumes equatorial = 71,492 km).
#   - Small bodies (Bennu, Eris, Haumea, Makemake, Arrokoth, Planet 9):
#     volumetric mean radius. "Equatorial" is not well-defined for
#     irregular or highly ellipsoidal bodies.
#   - Mercury, Venus, Moon: difference is sub-0.1%; volumetric retained.
#
# Sources:
#   IAU 2015 Resolution B3 (Prsa et al. 2016, AJ 152:41) for Sun,
#     Earth, Jupiter nominal values.
#   Archinal et al. 2018 (Celest. Mech. Dyn. Astr. 130:22) for Mars,
#     Saturn, Uranus, Neptune equatorial radii (IAU WGCCRE 2015 report).
#   NASA NSSDCA Planetary Fact Sheets for Mercury, Venus, Moon.
#   JPL Solar System Dynamics for dwarf planets / small bodies.
#   Nimmo et al. 2017 (Icarus) for Pluto.
# Ref: https://nssdc.gsfc.nasa.gov/planetary/factsheet/
# Ref: https://ssd.jpl.nasa.gov/planets/phys_par.html
# Note: equatorial convention adopted 2026-04-16 per downstream usage
#   analysis; prior volumetric values caused ~2.3% position error for
#   Jupiter-scaled shells like Io torus.
# Cross-checked: Claude 2026-08-02 -- IAU B3 / Archinal / JPL SSD (worksheet_claude_constants_new.md)
# Cross-checked: GPT 2026-08-02 -- IAU B3 / Archinal / JPL SSD (constants_new_citation_verification_gpt.md)

# ------------------------------------------------------------
# Named constants (L-162, 2026-07-29): the 14 remaining bodies,
# promoted from CENTER_BODY_RADII dict entries to their own named
# constant, same pattern as SUN_RADIUS_KM / EARTH_EQUATORIAL_RADIUS_KM /
# JUPITER_EQUATORIAL_RADIUS_KM above. Value and citation carried forward
# unchanged from the dict entry each replaces -- no new sourcing done
# in this pass. Planet 9 excluded (model estimate; L-159).
# ------------------------------------------------------------

MERCURY_RADIUS_KM = 2439.7
# Source: NASA Fact Sheet (volumetric mean; oblateness ~0.0009)

VENUS_RADIUS_KM = 6051.8
# Source: NASA Fact Sheet (volumetric mean; oblateness ~0)

MOON_RADIUS_KM = 1737.4
# Source: NASA NSSDCA Fact Sheet (volumetric mean; oblateness ~0.0012)
# Source+: Also IAU/LRO reference radius (Archinal et al. 2011)
# Cross-checked: Claude 2026-08-02 -- NASA NSSDCA (worksheet_claude_constants_remaining.md)
# Cross-checked: GPT 2026-08-02 -- JPL SSD (constants_remaining_independent_verification_gpt.md)
# Cross-checked: Gemini 2026-08-02 -- NASA NSSDCA (worksheet_gemini_constants_remaining.md)

MARS_RADIUS_KM = 3396.2
# Source: Archinal et al. 2018, Celest. Mech. Dyn. Astr. 130:22 (equatorial; vol = 3389.5)
# Cross-checked: Claude 2026-08-02 -- JPL SSD (worksheet_claude_constants_new.md)
# Cross-checked: GPT 2026-08-02 -- JPL SSD (constants_new_citation_verification_gpt.md)

PHOBOS_RADIUS_KM = 11.1
# Source: NASA/JPL Solar System Dynamics group

SATURN_RADIUS_KM = 60268
# Source: Archinal et al. 2018, Celest. Mech. Dyn. Astr. 130:22 (equatorial; vol = 58232)
# Cross-checked: Claude 2026-08-02 -- JPL SSD (worksheet_claude_constants_new.md)
# Cross-checked: GPT 2026-08-02 -- JPL SSD (constants_new_citation_verification_gpt.md)

URANUS_RADIUS_KM = 25559
# Source: Archinal et al. 2018, Celest. Mech. Dyn. Astr. 130:22 (equatorial; vol = 25362)
# Cross-checked: Claude 2026-08-02 -- JPL SSD (worksheet_claude_constants_new.md)
# Cross-checked: GPT 2026-08-02 -- JPL SSD (constants_new_citation_verification_gpt.md)

NEPTUNE_RADIUS_KM = 24764
# Source: Archinal et al. 2018, Celest. Mech. Dyn. Astr. 130:22 (equatorial; vol = 24622)
# Cross-checked: Claude 2026-08-02 -- JPL SSD (worksheet_claude_constants_new.md)
# Cross-checked: GPT 2026-08-02 -- JPL SSD (constants_new_citation_verification_gpt.md)

PLUTO_RADIUS_KM = 1188.3
# Source: New Horizons occultation (Nimmo et al. 2017)

BENNU_RADIUS_KM = 0.24503
# Source: Barnouin et al. 2019, Nature Geoscience 12:247, Table 1 --
# Source+: mean radius 245.03 +/- 0.08 m from OSIRIS-REx OLA and imaging
# Note: supersedes the pre-encounter radar shape model of Nolan et al.
# Note+: 2013, Icarus 226:629 (mean diameter 492 +/- 20 m, implying ~0.246
# Note+: km), which this row previously carried. The mission figure is
# Note+: independently derived, not a restatement of the radar result.
# Corrected: 2026-08-02 -- 0.262 -> 0.246 (prior value matched no published source)
# Corrected: 2026-08-20 -- 0.246 -> 0.24503 (OSIRIS-REx supersedes radar)
# Cross-checked: Claude 2026-08-02 -- Nolan et al. (worksheet_claude_constants_new.md)
# Review-note: a `Cross-checked: GPT 2026-08-02 -- OSIRIS-REx` leg was
#   removed here 2026-08-20. GPT REFUSED this row in that worksheet;
#   the row was then corrected in response. A verdict that causes an
#   edit is Resolved, not Cross-checked -- but Resolved did not exist
#   until L-200 (2026-08-17), so there was no correct leg to write at
#   the time. Recorded rather than treated as bad faith.
# Resolved: worksheet_claude-opus-5_pilot_constants_new_20260818.jsonl constants_new.py::BENNU_RADIUS_KM -- value superseded by OSIRIS-REx, misattributed OLA confirmation removed (L-210)

ERIS_RADIUS_KM = 1163
# Source: Volumetric mean (Sicardy et al. 2011 occultation)

HAUMEA_RADIUS_KM = 798
# Source: Ortiz et al. 2017, Nature 550:219 (stellar occultation) --
# Source+: semi-axes 1161 +/- 30, 852 +/- 4, 513 +/- 16 km
# Derived: volume-equivalent radius (1161 * 852 * 513)^(1/3) = 797.6 km,
# Derived+: rounded to 798. Ortiz publishes the semi-axes and no mean
# Derived+: radius, so this value is COMPUTED here rather than quoted.
# Note: VISUALIZATION VALUE, and the two shape solutions differ by ~11%
# Note+: in radius. Lockwood et al. 2014, Earth Moon Planets 111:127 publishes
# Note+: 715 km directly and is what JPL SSD adopted; the 2017 occultation is
# Note+: the only direct measurement. 798 is chosen for that reason.
# Review-note: an unsourced "1050x840x537 km -> geometric mean 779.5 km"
#   line was removed 2026-08-20. Those axes match NO published shape
#   model -- Lockwood gives 960x770x495, Ortiz 1161x852x513 -- yet the
#   779.5 computes correctly FROM them, so valid arithmetic on numbers
#   with no source left no trace a reader or scanner could catch.
#   Beware also the widespread secondary-source error of reading Ortiz's
#   semi-axes as full axes, which halves Haumea to ~399 km.
# Corrected: 2026-08-02 -- 816 -> 715 per JPL SSD (prior value matched neither axes nor database)
# Corrected: 2026-08-20 -- 715 -> 798 per the 2017 occultation
# Resolved: worksheet_claude-opus-5_pilot_constants_new_20260818.jsonl constants_new.py::HAUMEA_RADIUS_KM -- moved to the 2017 occultation solution, unsourced axes removed (L-210)
# Cross-checked: Claude 2026-08-02 -- JPL SSD (worksheet_claude_constants_new.md)
# Cross-checked: GPT 2026-08-02 -- JPL SSD (constants_new_citation_verification_gpt.md)

MAKEMAKE_RADIUS_KM = 715
# Source: Volumetric mean (Brown et al.)

ARROKOTH_RADIUS_KM = 9.1
# Source: Keane et al. 2022, JGR Planets (New Horizons shape model)
# Source+: Volume 3166 km^3 -> equivalent sphere radius 9.1 km
# Source+: Overall dims 35.95 x 19.90 x 9.75 km (bilobed contact binary)
# Source+: Corrected 2026-04-15 per Gemini review (was 0.0088 = 8.8 meters!)
# Corrected: 2026-08-02 -- 9.95 -> 9.1 per Keane shape model (prior dims were wrong)
# Cross-checked: Claude 2026-08-02 -- Keane et al. 2022 (worksheet_claude_constants_new.md)
# Cross-checked: GPT 2026-08-02 -- Keane et al. 2022 (constants_new_citation_verification_gpt.md)

CENTER_BODY_RADII = {       # km (equatorial for major bodies, volumetric for small)
    # L-162 (2026-07-29): all 17 named bodies now reference their own
    # named constant below instead of a raw literal -- Sun/Earth/Jupiter
    # were already named; Mercury through Arrokoth are newly promoted in
    # this pass. Planet 9 stays a raw literal -- model estimate, excluded
    # from promotion and from pinning per L-159.
    'Sun':      SUN_RADIUS_KM,
    'Mercury':  MERCURY_RADIUS_KM,
    'Venus':    VENUS_RADIUS_KM,
    'Earth':    EARTH_EQUATORIAL_RADIUS_KM,
    'Moon':     MOON_RADIUS_KM,
    'Mars':     MARS_RADIUS_KM,
    'Phobos':   PHOBOS_RADIUS_KM,
    'Jupiter':  JUPITER_EQUATORIAL_RADIUS_KM,
    'Saturn':   SATURN_RADIUS_KM,
    'Uranus':   URANUS_RADIUS_KM,
    'Neptune':  NEPTUNE_RADIUS_KM,
    'Pluto':    PLUTO_RADIUS_KM,
    'Bennu':    BENNU_RADIUS_KM,
    'Eris':     ERIS_RADIUS_KM,
    'Haumea':   HAUMEA_RADIUS_KM,
    'Makemake': MAKEMAKE_RADIUS_KM,
    'Arrokoth': ARROKOTH_RADIUS_KM,
    'Planet 9': 24000       # Model estimate (Batygin & Brown; 5-10 M_Earth assumption)
}

KNOWN_ORBITAL_PERIODS = {
    # Planets (converted from years to days)
    'Mercury':  87.969,      
    'Venus':    224.701,       
    'Earth':    365.256,       
    'Mars':     686.980,
    'Phobos':   0.319,        # JPL Horizons        
    'Jupiter':  4332.589,    
    'Saturn':   10759.22,   
    'Uranus':   30688.5,    
    'Neptune':  60189.0,   
    
    # Earth satellite
    'Moon': 27.321582,
    
    # Mars satellites
    'Phobos': 0.319,       # Verified from JPL
    'Deimos': 1.263,       # Verified from JPL
    
    # Jupiter satellites
    'Io': 1.769,           # 42.456 hours
    'Europa': 3.551,       # 85.224 hours
    'Ganymede': 7.155,     # 171.72 hours
    'Callisto': 16.689,    # 400.536 hours
    'Metis': 0.295,        # 7.08 hours
    'Adrastea': 0.298,     # 7.15 hours
    'Amalthea': 0.498,     # 11.95 hours
    'Thebe': 0.675,        # 16.20 hours
    
    # Saturn satellites
    'Mimas': 0.942,        # 22.61 hours
    'Enceladus': 1.370,    # 32.88 hours
    'Tethys': 1.888,       # 45.31 hours
    'Dione': 2.737,        # 65.69 hours
    'Rhea': 4.518,         # 108.43 hours
    'Titan': 15.945,       # 382.68 hours
    'Hyperion': 21.277,    # 510.65 hours
    'Iapetus': 79.331,     # 1903.94 hours
    'Phoebe': 550.56,      # 1.51 years
    'Pan': 0.575,          # 13.80 hours
    'Daphnis': 0.594,      # 14.26 hours
    'Atlas': 0.602,        # 14.45 hours
    'Prometheus': 0.616,   # 14.78 hours
    'Pandora': 0.631,      # 15.14 hours
    'Epimetheus': 0.694,   # 16.66 hours
    'Janus': 0.695,        # 16.68 hours
    
    # Uranus satellites
    'Miranda': 1.413,      # 33.91 hours
    'Ariel': 2.520,        # 60.48 hours
    'Umbriel': 4.144,      # 99.46 hours
    'Titania': 8.706,      # 208.94 hours
    'Oberon': 13.463,      # 323.11 hours
    'Puck': 0.762,         # 18.29 hours
    'Portia': 0.513,       # 12.31 hours
    'Mab': 0.923,          # 22.15 hours
    
    # Neptune satellites  
    'Triton': 5.877,       # 141.05 hours 
    'Despina': 0.335,      # 8.04 hours
    'Galatea': 0.429,      # 10.30 hours
    'Proteus': 1.122,      # 26.93 hours
    'Larissa': 0.555,      # 13.32 hours
    'Naiad': 0.294,        # 7.06 hours
    
    # Pluto satellites
    'Charon': 6.387,       # 153.29 hours
    'Styx': 20.162,        # 483.89 hours
    'Nix': 24.856,         # 596.54 hours
    'Kerberos': 32.168,    # 772.03 hours
    'Hydra': 38.202,       # 916.85 hours
        
    # Eris satellite
    'Dysnomia': 15.786,    # 378.86 hours
    
    # Gonggong satellite
    'Xiangliu': 25.22,      # Based on arXiv:2305.17175 (May 2023)

    # Orcus satellite
    'Vanth': 9.54,         # Based on arXiv:1509.01719 (Sept 2015)

    # Quaoar satellite
    'Weywot': 12.44,       # Based on arXiv:astro-ph/0405636 (May 2004)

    # Haumea satellites
    "Hi'iaka": 49.12,      # ~49 days
    'Namaka': 18.28,       # ~18 days (non-Keplerian due to Hi'iaka)
    
    # Makemake satellite
    'MK2': 18.0,           # Based on arXiv:2509.05880 (Sept 2025)
    
    # Dwarf planets and KBOs (converted from years to days)
    'Pluto': 90560.0,    
    'Ceres': 1680.15,      # 4.6 * 365.25
    'Eris': 203809.50,     # 558.0 * 365.25
    'Haumea': 103731.00,   # 284.0 * 365.25
    'Makemake': 111766.50, # 306.0 * 365.25
    'Quaoar': 105192.00,   # 288.0 * 365.25
    'Orcus': 90314.9912925,     # 247.26897 * 365.25; 247.26897
    'Ixion': 91239.49018,       # PER= 249.80011 jy
    'Mani': 99305.28767,        # PER= 271.88306 jy
    'GV9': 100352.0613,         # PER= 274.74897 jy
    'Varuna': 102799.14,
    'Arrokoth': 108224.98,
    'Gonggong': 201010.45,
    '2017 OF201': 10048413.07,

    # Sednoid Trans-Neptunian Objects
    'Ammonite': 1444383.67 ,     # PER 3954.53339 Julian years 
    'Sedna': 4163850.00,   # 11400.0 * 365.25
    'Leleakuhonua': 12643548.84594,  # Orbital period in days;  34616.15016 julian years x 365.25

    # Centaurs -- unstable objects between Jupiter and Neptune
    'Chariklo': 22996.00,         # PER= 62.95962 jy = 22996.00121 days 

    # Asteroids
    'Apophis': 323.60,          # 0.89 * 365.25
    'Bennu': 436.65,            # 1.20 * 365.25
    'Ryugu': 473.98,            # 1.30 * 365.25
    'Phaethon': 523.42,         # 1.43 * 365.25
    'Itokawa': 556.38,          # 1.52 * 365.25
    'Eros': 642.63,             # 1.76 * 365.25
    'Lutetia': 1321.00,         # 3.62 * 365.25
    'Vesta': 1325.75,           # 3.63 * 365.25
    'Steins': 1327.41,          # 3.64 * 365.25
    'Dinkinesh': 1387.50,       # 3.80 * 365.25
    'Donaldjohanson': 1446.04,  # 3.96 * 365.25
    'Juno': 1591.93,            # 4.358 * 365.25
    'Pallas': 1685.37,          # 4.614 * 365.25
    '16 Psyche': 1826.18,       # 4.99982 * 365.25  
    'Hygiea': 2041.88,          # 5.592 * 365.25
 
    # Trojan asteroids (Jupiter's L4 and L5)
    'Orus': 4274.32,       # 11.71 * 365.25
    'Polymele': 4319.33,   # 11.83 * 365.25
    'Eurybates': 4333.71,  # 11.87 * 365.25
    'Patroclus': 4336.36,  # 11.88 * 365.25
    'Menoetius': 4336.36,  # 11.88 * 365.25
    'Leucus': 4352.24,     # 11.92 * 365.25
    
    # Near-Earth asteroids
    '2024 YR4': 922.84,         # 2.53 * 365.25
    '2025 PN7': 367.5547275,    # 1.00631 * 365.25   
    '2024 PT5': 368.75,         # 1.01 * 365.25
    '2025 PY1': 409.072695,     # days from PER in julian years
    '2023 JF': 493.37,          # 1.35 * 365.25
    '2025 KV': 695.85,          # 1.91 * 365.25
    
    # Comets (converted from years to days where applicable)
    'Halley': 27731.29226,          # 75.92414033 * 365.25 = 27731.29226; EPOCH=  2439907.5 ! 1968-Feb-21.0000000
    'Hyakutake': 35773534.62,       # PER= 97942.599927659 jy
    'Hale-Bopp': 863279.5035,       # PER= 2363.5304681429 jy = 863279.5035
    'Ikeya-Seki': 319800.00,        # 876.0 * 365.25 (estimate)
    'ISON': 230970.00,              # 632.3 * 365.25 (pre-disruption)
    'SWAN': 8237831.493,            # PER= 22553.953438133 jy
    '6AC4721': 311232,              # Approximate period for sungrazer comet C/2026 A1. This is equivalent to roughly 852.1 years.
    'MAPS': 418226.4926,            # Approximate period for sungrazer comet C/2026 A1. This is equivalent to roughly 1145.041732 years.    
    'Lemmon': 492252.5179,          # PER= 1347.7139437075 jy    
    'Schaumasse': 3014.1,           # 8.252 years * 365.25 = 3014.1 days
    'Howell': 2009.4,              # ~5.5 years * 365.25 = 2009.375 days
    'Tempel 2': 1961.8,            # 5.37 years * 365.25 = 1961.4 days
  
    # For hyperbolic/parabolic objects, period is undefined
    'West': None,           # West (C/1975 V1-A);  Parabolic comet - effectively infinite period  
    'C/2025_K1': None,      # Hyperbolic comet - effectively infinite period
    'C/2025_K1-B': None,    # Hyperbolic fragment - escaping solar system
    'C/2025_K1-C': None,    # Technically ~13M year period, effectively infinite
    'C/2025_K1-D': None,    # Hyperbolic fragment - escaping solar system    
    'Borisov': None,        # Hyperbolic comet - effectively infinite period    
    'McNaught': None,       # Hyperbolic comet - effectively infinite period 
    'ATLAS': None,          # Hyperbolic comet -- infinite period   PER= 9.999999E99
    'PANSTARRS': None,      # PER= 9.999999E99 jy (hyperbolic)
    '3I/ATLAS': None,       # Interstellar hyperbolic object - effectively infinite period
    '1I/Oumuamua': None,    # Interstellar hyperbolic object - effectively infinite period  
    '2I/Borisov': None,     # Interstellar hyperbolic object - effectively infinite period
    'Wierzchos': None,      # Near-parabolic, outbound ~200,000 years; effectively open trajectory     
    
    # Hypothetical
    'Planet 9': 3652500.00, # ~10000 * 365.25 (estimated)
}

# Mapping of SIMBAD object types to full descriptions



# Function to map celestial objects to colors
def color_map(planet):
    colors = {
        'Sun': 'rgb(102, 187, 106)',      # chlorophyll green
    #    'Sun': 'rgb(255, 249, 240)',  # Slightly warm white to represent 6000K at the Sun's surface. The inner corona is 2M K.
        'Mercury': 'rgb(128, 128, 128)',   # Description: Dark Gray reflecting Mercury's rocky and heavily cratered surface.
        'Venus': 'rgb(255, 255, 224)',
        'Earth': 'rgb(0, 102, 204)',
        'Moon': 'rgb(211, 211, 211)',
        'Mars': 'rgb(188, 39, 50)',
        'Phobos': 'rgb(139, 0, 0)',
        'Deimos': 'rgb(105, 105, 105)',
        'Ceres': 'rgb(105, 105, 105)',

        'Jupiter': 'rgb(255, 165, 0)',
        'Io': 'rgb(255, 140, 0)',
        'Europa': 'rgb(173, 216, 230)',
        'Ganymede': 'rgb(150, 75, 0)',
        'Callisto': 'rgb(169, 169, 169)',
        'Metis': 'rgb(180, 120, 100)',    # Reddish-brown
        'Adrastea': 'rgb(190, 150, 130)',  # Light reddish-brown
        'Amalthea': 'rgb(200, 60, 50)',    # Red
        'Thebe': 'rgb(170, 110, 90)',       # Dark reddish-brown

        'Saturn': 'rgb(210, 180, 140)',
        'Titan': 'rgb(255, 215, 0)',
        'Enceladus': 'rgb(192, 192, 192)',
        'Rhea': 'rgb(211, 211, 211)',
        'Dione': 'rgb(255, 182, 193)',
        'Tethys': 'rgb(173, 216, 230)',
        'Mimas': 'rgb(105, 105, 105)',
        'Pan': 'rgb(180, 180, 180)',            # (Light Gray)
        'Daphnis': 'rgb(190, 190, 190)',        # (Slightly lighter gray)
        'Prometheus': 'rgb(170, 170, 170)',     # (Medium Gray)
        'Pandora': 'rgb(185, 185, 185)',        # (Light-Medium Gray)
        'Hyperion': 'rgb(160, 100, 80)',        # (Dark reddish-brown)
        'Iapetus': 'rgb(220, 220, 220)',        # Trailing Hemisphere: (220, 220, 220) (Light Gray/Whitish); 
                                                # Leading Hemisphere (Cassini Regio): (50, 50, 50) (Very dark gray/almost black) 
        'Phoebe': 'cyan',

        'Uranus': 'rgb(173, 216, 230)',
        'Titania': 'rgb(221, 160, 221)',         
        'Oberon': 'rgb(128, 0, 128)',
        'Umbriel': 'rgb(148, 0, 211)',    
        'Ariel': 'rgb(144, 238, 144)',
        'Miranda': 'rgb(0, 128, 0)',
        'Portia': 'rgb(150, 150, 150)',
        'Mab': 'rgb(100, 100, 120)',

        'Neptune': 'rgb(0, 0, 255)',
        'Triton': 'rgb(0, 255, 255)',
        'Despina': 'rgb(175, 175, 175)',
        'Galatea': 'rgb(175, 175, 175)',

        'Pluto': 'rgb(205, 92, 92)',
        'Charon': 'rgb(169, 169, 169)',
        'Styx': 'rgb(180, 180, 180)',
        'Nix': 'rgb(200, 200, 200)',  
        'Kerberos': 'rgb(170, 170, 170)',      
        'Hydra': 'rgb(190, 190, 190)', 

        'Planet 9': 'grey',  # grey
       
        'Voyager 1': 'white',
        'Voyager 2': 'magenta',
        'Cassini': 'green',
        'New Horizons': 'cyan',
        'Arrokoth': 'red',
        'Juno': 'cyan',
        'Galileo': 'white',
        'Apollo 11 S-IVB': 'cyan', 
        'Artemis II': 'magenta',       
        'Pioneer 10': 'red',
        'Pioneer 11': 'green',
        'Clipper': 'red',
        'Psyche': 'green',
        'JUICE': 'blue', 
        'OSIRIS': 'cyan',
        'Parker': 'white',
        'JWST': 'magenta',
        'Rosetta': 'white',
        'BepiColombo': 'red',
        'SolO': 'red',
        'SOHO': 'green',
        'Akatsuki': 'cyan',
        'MarsRover': 'white',

        'EM-L1': 'cyan',        
        'EM-L2': 'white',
        'EM-L3': 'green',
        'EM-L4': 'magenta',
        'EM-L5': 'red',
        'L1': 'cyan',        
        'L2': 'white',
        'L3': 'green',
        'L4': 'magenta',
        'L5': 'red',

        'Kamo oalewa': 'cyan',
        '2025 PN7': 'magenta',        
        '2024 PT5': 'red',
        '2025 PY1': 'white',
        '2023 JF': 'white',
        '2024 DW': 'magenta',        
        '2024 YR4': 'green',

        '16 Psyche': 'magenta',
        'Apophis': 'red',
        'Vesta': 'cyan',
        'Bennu': 'white',
        'Lutetia': 'green',
        'Steins': 'red',  

        '1I/Oumuamua': 'magenta',
        '3I/ATLAS': 'red',
        'Ikeya-Seki': 'green',
        'West': 'red',
        'Halley': 'cyan',
        'Hyakutake': 'white',
        'Hale-Bopp': 'magenta',
        'McNaught': 'green',
        'NEOWISE': 'red',
        'C/2025_K1': 'cyan',
        'C/2025_K1-B': 'rgb(0, 200, 220)',          # Teal - darker cyan variant
        'C/2025_K1-C': 'magenta',           # magenta - the bound fragment (special!)
        'C/2025_K1-D': 'rgb(100, 180, 255)',          # Sky blue - cooler variant        
        'Borisov': 'green',        
        'Tsuchinshan': 'cyan',
        'ATLAS': 'white',
        'Churyumov': 'magenta',
        '2I/Borisov': 'red',
        'SWAN': 'magenta',
        'PANSTARRS': 'green',
        '6AC4721': 'cyan',
        'MAPS': 'cyan',
        'Lemmon': 'green',  
        'Wierzchos': 'cyan',
        'Schaumasse': 'magenta',
        'Howell': 'white',
        'Tempel 2': 'red',             

        'SOHO': 'white',
        'JamesWebb': 'magenta',
        'Ryugu': 'magenta',
        'Eros': 'green',
        'Dinkinesh': 'white',
        'Donaldjohanson': 'red',
        'Eurybates': 'green',
        'Patroclus': 'white',
        'Menoetius': 'red',
        'Leucus': 'magenta',
        'Polymele': 'cyan',
        'Orus': 'pink',
        'Itokawa': 'red',
        'MarsRover': 'white',
        'DART': 'magenta',
        'Lucy': 'green',
        'Gaia': 'red',
        'Hayabusa2': 'cyan',  
        'Quaoar': 'rgb(244, 164, 96)',
        'Dysnomia': 'white',
        'Xiangliu': 'rgb(210, 105, 30)',
        'Vanth': 'rgb(169, 169, 169)',
        'Weywot': 'rgb(205, 133, 63)',
        "Hi'iaka": 'rgb(200, 180, 220)',    # Light purple (Haumea family)
        'Namaka': 'rgb(180, 160, 200)',     # Slightly darker purple
        'MK2': 'rgb(80, 80, 80)',           # Very dark (low albedo)        
        'Chariklo': 'rgb(100, 50, 50)',
        'Orcus': 'rgb(0, 100, 0)',
        'Varuna': 'rgb(218, 165, 32)',
        'Ixion': 'rgb(218, 165, 32)',
        'GV9': 'rgb(128, 0, 128)',
        'Mani': 'rgb(255, 0, 0)',  
        'Gonggong': 'red',    
        'Haumea': 'rgb(128, 0, 128)',
        'Makemake': 'rgb(255, 192, 203)',
        'Eris': 'rgb(240, 240, 240)',
        'Ammonite': 'rgb(255, 0, 0)', 
        'Sedna': 'rgb(135, 206, 235)',
        'Leleakuhonua': 'cyan',
        '2017 OF201': 'rgb(150, 90, 60)',                       
    }
    return colors.get(planet, 'goldenrod')

# Define positions for stellar class labels with different x positions and fonts
stellar_class_labels = [
        {
            'text': 'Supergiants', 
            'x': 0.2, 
            'y': 5.5,
            'font': dict(color='lightblue', size=14, family='Arial')
        },
        {
            'text': 'Supergiants', 
            'x': 0.66, 
            'y': 5.5,
            'font': dict(color='red', size=14, family='Arial')
        },
        {
            'text': 'Bright Giants', 
            'x': 0.22, 
            'y': 3.7,
            'font': dict(color='lightblue', size=14, family='Arial')
        },
        {
            'text': 'Bright Giants', 
            'x': 0.857, 
            'y': 3.7,
            'font': dict(color='red', size=14, family='Arial')
        },
        {
            'text': 'Carbon Stars', 
            'x': 0.96, 
            'y': 3.0,
            'font': dict(color='red', size=14, family='Arial')
        },
        {
            'text': 'Giants', 
            'x': 0.25, 
            'y': 2.25,
            'font': dict(color='lightblue', size=14, family='Arial')
        },
        {
            'text': 'Giants', 
            'x': 0.83, 
            'y': 2.25,
            'font': dict(color='red', size=14, family='Arial')
        },
        {
            'text': 'Subgiants', 
            'x': 0.2, 
            'y': 1.0,
            'font': dict(color='lightblue', size=14, family='Arial')
        },
        {
            'text': 'Subgiants', 
            'x': 0.75, 
            'y': 1.0,
            'font': dict(color='red', size=14, family='Arial')
        },
        {
            'text': 'Main Sequence', 
            'x': 0.4, 
            'y': 0.2, 
            'rotation': 15,
            'font': dict(color='white', size=20, family='Arial', weight='bold')  # Making this one bold as an example
        },
                {
            'text': 'Dwarfs', 
            'x': 0.77, 
            'y': -1,
            'font': dict(color='red', size=14, family='Arial')
        },
        {
            'text': 'White Dwarfs', 
            'x': 0.4, 
            'y': -4.5,
            'font': dict(color='white', size=14, family='Arial')
        }
    ]

spectral_subclass_temps = {
    'O': {0: 50000, 9: 30000},    # O0 to O9
    'B': {0: 30000, 9: 10000},    # B0 to B9
    'A': {0: 10000, 9: 7500},     # A0 to A9
    'F': {0: 7500, 9: 6000},      # F0 to F9
    'G': {0: 6000, 9: 5200},      # G0 to G9
    'K': {0: 5200, 9: 3700},      # K0 to K9
    'M': {0: 3700, 9: 2400},      # M0 to M9
    'L': {0: 2400, 9: 1300},      # L0 to L9
    'T': {0: 1300, 9: 600},       # T0 to T9 (optional)
}

# ============================================================
# SAGITTARIUS A* AND GALACTIC-SCALE CONSTANTS
# Migrated 2026-08-25 from sgr_a_star_data.py under L-247, then sourced
# and repaired the same day against three independent returns
# (documentation/CONVERGENCE_L247_sgr_a_constants.md).
#
# Epoch policy, Tony's ruling 2026-08-25: the most recent publication
# that reports a value AS A RESULT is authoritative, and the value it
# replaces is recorded rather than overwritten. A later paper that
# merely carries the quantity as a fit parameter or quotes it in
# passing does not supersede the paper that measured it.
# ============================================================

GRAVITATIONAL_CONSTANT_SI = 6.67430e-11
# Note: units m^3 kg^-1 s^-2. Measured, not exact: the relative standard
# Note+: uncertainty is 2.2e-05, so a bare literal reads as more
# Note+: precise than the quantity is.
# Source: CODATA 2022 -- Mohr, Newell, Taylor & Tiesinga (2025),
# Source+: Rev. Mod. Phys. 97, 025002,
# Source+: doi:10.1103/RevModPhys.97.025002. Published as
# Source+: 6.67430(15)e-11.
# Cross-checked: Claude 2026-08-25 -- CODATA 2022 (worksheet_claude-opus-5_L247_sgr_a_constants_20260825.md)
# Cross-checked: GPT 2026-08-25 -- CODATA 2022 (worksheet_gpt-5.6-sol_L247_sgr_a_constants_20260825.md)
# Cross-checked: Gemini 2026-08-25 -- CODATA 2018/2022 (worksheet_gemini-2.5-pro_L247_sgr_a_constants_20260825.md)
# Note: the three legs agree on the value digit for digit and differ
# Note+: only on which adjustment to name. The 2022 adjustment took in
# Note+: no new competitive datum for G, so 2018 and 2022 publish the
# Note+: same central value; 2022 is named here as the current
# Note+: authority.

SPEED_OF_LIGHT_M_S = SPEED_OF_LIGHT_KM_S * 1000
# Derived: the store already holds this quantity in km/s. Carrying a
#          second literal would put two spellings of one exact value in
#          one file, which is the failure L-247 exists to close.

GM_SUN_SI = 1.3271244e20
# Note: the nominal solar mass parameter, units m^3 s^-2. EXACT by
# Note+: definition -- it is a conversion constant, not a measurement
# Note+: of the Sun.
# Source: IAU 2015 Resolution B3, published as Prsa et al. (2016),
# Source+: AJ 152, 41, doi:10.3847/0004-6256/152/2/41.
# Cross-checked: Claude 2026-08-25 -- IAU 2015 B3 (worksheet_claude-opus-5_L247_sgr_a_constants_20260825.md)
# Cross-checked: GPT 2026-08-25 -- IAU 2015 B3 (worksheet_gpt-5.6-sol_L247_sgr_a_constants_20260825.md)
# Cross-checked: Gemini 2026-08-25 -- IAU 2015 B3 (worksheet_gemini-2.5-pro_L247_sgr_a_constants_20260825.md)

EARTH_HILL_SPHERE_KM = KM_PER_AU * (EARTH_GM_KM3_S2 / (3.0 * GM_SUN_SI * 1.0e-9)) ** (1.0 / 3.0)
# Derived: r_H = a (m / 3M)^(1/3) with a = 1 AU, m/M = GM_E / GM_Sun =
# Derived+: 398600.4418 / 1.3271244e11 = 3.00349e-6; (m/3M)^(1/3) =
# Derived+: 0.0100039; x 149,597,870.7 km = 1,496,559 km. Report 1.50e6 km.
# Derived+: Placed here, not in the Earth block above, because it needs
# Derived+: GM_SUN_SI and this file is read top-down (L-291).
# Note: a = 1 AU exactly. Earth's semi-major axis is 1.00000011 AU (NASA
# Note+: Earth Fact Sheet), agreement to seven figures, so the rounding is
# Note+: below everything else in the derivation.
# Ref: https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html
EARTH_HILL_SPHERE_RADII = EARTH_HILL_SPHERE_KM / EARTH_EQUATORIAL_RADIUS_KM
# Derived: 1,496,559 / 6378.1366 = 234.64 -- the "about 235 radii" the
# Derived+: orrery's Hill sphere shell types as radius_fraction = 235.

SOLAR_MASS_KG = GM_SUN_SI / GRAVITATIONAL_CONSTANT_SI
# Derived: 1.3271244e20 / 6.67430e-11 = 1.9884098707e30 kg.
# Derived+: Previous hardcoded value was 1.989e30, which is 0.0297%
# Derived+: high. It was not a typo. Dividing the same exact GM by the
# Derived+: CODATA 1986 G, 6.67259e-11, gives 1.98892e30 -- 1.989e30 to
# Derived+: four figures. The number moved because G moved, not because
# Derived+: the Sun did.
# Resolved: worksheet_gpt-5.6-sol_L247_sgr_a_constants_20260825.md constants_new.py::SOLAR_MASS_KG -- literal replaced by a derivation from the IAU-exact GM, value 1.989e30 to 1.9884098707e30 (L-247)
# Note: written as a derivation rather than as a corrected literal
# Note+: (Tony's ruling, 2026-08-25). The product G x M is known far
# Note+: better than either factor, and this file holds both. Carried
# Note+: as two literals, their product was 1.32751827e20 against a
# Note+: defined 1.3271244e20 -- 0.030% off a quantity the IAU declares
# Note+: exact, implicitly, where nothing watched it. Derived, the
# Note+: product is exact by construction and cannot drift when CODATA
# Note+: next moves G.
# Note: the kilogram value still inherits G's 2.2e-05 uncertainty. What
# Note+: the derivation fixes is the PRODUCT, not the precision of the
# Note+: mass.

M_PER_AU = KM_PER_AU * 1000
# Derived: 1 AU in metres, from the IAU 2012 definition above.
# Note: replaces AU_TO_METERS in sgr_a_star_data.py, renamed to match
#       this file's KM_PER_AU direction rather than the AU_TO_ one.

PARSEC_TO_AU = 206264.806247096
# Note: DEFINED, not measured. One parsec is the distance at which one
# Note+: astronomical unit subtends one arcsecond, so the value is
# Note+: exactly 648000/pi au and no source publishes it as a
# Note+: measurement.
# Derived: 648000 / pi = 206264.80624709636...
# Derived+: Previous hardcoded value was 206265.0 (consistent to 6 sig
# Derived+: figs; relative error 9.39e-07). The trailing .0 asserted a
# Derived+: tenth-of-an-au precision the number did not have -- the
# Derived+: true fourth decimal is 8, not 0.
# Source: IAU 2015 Resolution B2; the exact relation is restated in
# Source+: Prsa et al. (2016), AJ 152, 41,
# Source+: doi:10.3847/0004-6256/152/2/41.
# Cross-checked: Claude 2026-08-25 -- IAU 2015 B2 (worksheet_claude-opus-5_L247_sgr_a_constants_20260825.md)
# Cross-checked: GPT 2026-08-25 -- IAU 2015 B2 (worksheet_gpt-5.6-sol_L247_sgr_a_constants_20260825.md)
# Cross-checked: Gemini 2026-08-25 -- IAU 2015 B2 (worksheet_gemini-2.5-pro_L247_sgr_a_constants_20260825.md)
# Resolved: worksheet_gpt-5.6-sol_L247_sgr_a_constants_20260825.md constants_new.py::PARSEC_TO_AU -- rounded 206265.0 replaced by the exact IAU definition 648000/pi (L-247)
# Note: written as a literal rather than as 648000.0/math.pi, following
# Note+: SPEED_OF_LIGHT_KM_S, which is equally exact by definition and
# Note+: equally written out. A math.pi expression would also be
# Note+: unreadable to constants_change_report.py's DERIVED case, which
# Note+: accepts only names tracked in this file.
# Note: this value carries the whole star pipeline once L-248 lands.
# Note+: PARSEC_TO_AU / AU_PER_LIGHT_YEAR is 3.2615637772 with the
# Note+: exact parsec and was 3.2615668 with the rounded one; the
# Note+: literal 3.26156 that L-248 sweeps is closer to the first.

SGR_A_MASS_SOLAR = 4.297e6
# Source: GRAVITY Collaboration (2022), "Mass distribution in the
# Source+: Galactic Center based on interferometric astrometry of
# Source+: multiple stellar orbits", A&A 657, L12,
# Source+: doi:10.1051/0004-6361/202142465. Published as
# Source+: 4.297 +/- 0.012 (stat) +/- 0.040 (sys) e6 solar masses.
# Cross-checked: GPT 2026-08-25 -- GRAVITY Collaboration 2022 (worksheet_gpt-5.6-sol_L247_sgr_a_constants_20260825.md)
# Resolved: worksheet_gpt-5.6-sol_L247_sgr_a_constants_20260825.md constants_new.py::SGR_A_MASS_SOLAR -- advanced from the 2019 to the 2022 GRAVITY determination, 4.154e6 to 4.297e6, under the epoch policy above (L-247)
# Review-note: the value this replaces was 4.154e6, GRAVITY
#              Collaboration (2019), A&A 625, L10,
#              doi:10.1051/0004-6361/201935656, Table 1. It was held
#              here until 2026-08-25 under a source line reading only
#              "GRAVITY Collaboration 2019", which named no paper, DOI
#              or table. Recorded rather than deleted, per the epoch
#              policy above.
# Review-note: ONE cross-check leg, not two. Of the three returns, only
#              GPT reached the 2022 value; the Claude return noted that
#              a successor exists without giving its numbers, and the
#              Gemini return gave the 2022 distance in prose but not the
#              mass. A second independent leg is owed on this row.
# Note: this value and SGR_A_DISTANCE_PC below came out of the same
# Note+: orbit fit of the same stars and are strongly correlated. If
# Note+: either is ever updated, the other moves in the SAME edit and
# Note+: from the SAME paper. A newer distance beside an older mass is
# Note+: a pair no publication supports, and no single-value check
# Note+: would catch it, because each number would remain individually
# Note+: citable.

SGR_A_DISTANCE_PC = 8277.0
# Note: parsecs is what the primary publications actually report. This
# Note+: file stores the published quantity and derives the display
# Note+: one, the same shape as GM_SUN_SI above.
# Source: GRAVITY Collaboration (2022), A&A 657, L12,
# Source+: doi:10.1051/0004-6361/202142465. Published as
# Source+: R_0 = 8277 +/- 9 (stat) pc, with a stated systematic near
# Source+: 30 pc.
# Review-note: NO cross-check leg, and the absence is the honest state.
#              A cross-check line naming the GPT worksheet stood here
#              from 2026-08-25 until later the same day, when the
#              checker reported UNMATCHED: no row in that worksheet is
#              about SGR_A_DISTANCE_PC. The worksheet's row 5 is about
#              SGR_A_DISTANCE_LY and the value it examined was 26670.0.
#              This name did not exist when the request went out. The
#              line was removed rather than reworded, because an
#              annotation asserting a check that was not performed on
#              this name is the failure this apparatus exists to catch.
# Review-note: what the returns DO support: the GPT row 5 reached
#              R_0 = 8277 pc from GRAVITY 2022, and the Gemini Findings
#              prose states the same figure while attributing it to
#              "GRAVITY 2021". Neither is a verdicted row about this
#              constant. A dispatch is owed on this name.
# Note: paired with SGR_A_MASS_SOLAR -- see the note on that row.

SGR_A_DISTANCE_LY = SGR_A_DISTANCE_PC * PARSEC_TO_AU / AU_PER_LIGHT_YEAR
# Derived: 8277 pc x 3.2615637772 ly/pc = 26995.963 light-years.
# Derived+: Previous hardcoded value was 26670.0, which is the 2019
# Derived+: R_0 of 8178 pc converted (26673.07) and rounded to four
# Derived+: significant figures. Inverted, 26670.0 ly is 8177.06 pc,
# Derived+: which matches no column of the 2019 Table 1.
# Resolved: worksheet_gpt-5.6-sol_L247_sgr_a_constants_20260825.md constants_new.py::SGR_A_DISTANCE_LY -- 26670.0 literal retired; the value now derives from a sourced SGR_A_DISTANCE_PC at the 2022 R_0 (L-247)
# Note: the trailing .0 on the old literal asserted 0.1 ly against a
# Note+: real uncertainty near 100 ly, overstated by three orders of
# Note+: magnitude. Deriving removes the claim rather than restating
# Note+: it.

