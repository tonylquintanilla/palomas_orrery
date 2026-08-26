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

RADIATIVE_ZONE_AU = 0.7 * SOLAR_RADIUS_AU
# Visualization boundary; rounds the helioseismic tachocline at ~0.713 R_sun
# Source: Christensen-Dalsgaard, Gough & Thompson (1991), ApJ 378:413
# Cross-checked: GPT 2026-08-02 -- helioseismology literature (constants_remaining_independent_verification_gpt.md)
# Cross-checked: Gemini 2026-08-02 -- Carroll & Ostlie (worksheet_gemini_constants_remaining.md)

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
# Source: Golub & Pasachoff, "The Solar Corona" (2010)
# Note: Visualization boundary for inner (K-)corona; physical extent 2-3 R_sun
# Cross-checked: Gemini 2026-08-02 -- Golub & Pasachoff (worksheet_gemini_constants_remaining.md)

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

