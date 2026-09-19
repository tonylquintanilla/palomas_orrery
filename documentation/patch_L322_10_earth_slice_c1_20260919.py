#!/usr/bin/env python3
"""
patch_L322_10_earth_slice_c1_20260919.py -- ORRERY repo.

Run: save this file in the ORRERY repo ROOT (next to
PROJECT_INSTRUCTIONS.md), open it in VS Code and click Run.  Or:
python patch_L322_10_earth_slice_c1_20260919.py

A patch is run from its repository's ROOT and filed in documentation/
AFTER it has run. Filed first and run second, it stops with one line,
writes nothing, and the push goes out without it. This script refuses to
run from documentation/.

Built on orrery 4801594104cdb229bc14fa9d77a9ba3ca1e686be
at https://github.com/tonylquintanilla/palomas_orrery
(gallery 82e786f17634f108a2e0df2ae7c693e5fcf62a60
at https://github.com/tonylquintanilla/tonyquintanilla.github.io)

STAGE C1 of documentation/BUILD_MANIFEST_L322_earth_slice_20260919.md:
the walk over the 29 Earth constants that carried no fields, plus
KM_PER_AU and GM_SUN_SI, which belong to no body's slice but feed
Earth's Hill sphere. Each row is visited ONCE and gets its unit, its
status, its figure count and, where it is in scope, its read line.

WHAT IT DOES (2 files, 34 anchored edits):

  constants_tokens.py
      four new tokens -- km3_s2, m3_s2, rad_s and m3_per_km3. rad_s
      carries the DIMENSION "1 / s", because the radian is dimensionless
      in SI. That is what makes the geostationary cube root come out in
      kilometres instead of kilometres per radian to the two-thirds, and
      it is what the checker's own built-in fixture already does.

  constants_new.py
      31 rows gain fields. Five comment lines that stated something
      false are corrected, and each correction says so on the row and
      leaves the old wording visible in the sentence that replaces it:

        EARTH_POLAR_RADIUS_KM      cited IERS as though TN36 tabulated a
                                   polar radius. It does not; the number
                                   follows from that table's equatorial
                                   radius and flattening factor, and the
                                   NASA fact sheet prints it directly.
        EARTH_GM_KM3_S2            said TCB-compatible. Table 1.1's own
                                   footnote says TCG-compatible.
        EARTH_ROTATION_RATE_RAD_S  said TN36 Table 1.1, which has no
                                   angular velocity in it. It is Table
                                   1.2, the GRS80 parameters.
        EARTH_LOWER_MANTLE_KM      said the 660 km depth was good to
                                   units and read off 5711 km. Its
                                   source gives 660 +/- 10 km, so it is
                                   good to TENS and the value is 5710.
        EARTH_THERMOPAUSE_RADII    declared 1.0078 and 1.0941, more
                                   figures than either altitude supports.

      One NEW row, M3_PER_KM3, an exact unit conversion. It exists
      because a bare 1.0e-9 inside the Hill sphere expression converted
      cubic metres to cubic kilometres where nothing could see that it
      carried a unit, and test_dimensions.py read the result as a
      MISMATCH of exactly 1000x. The rewritten expression is
      bit-identical, so no drawn value moves because of it.

ONE DRAWN NUMBER CHANGES, and Tony approved it before this was cut:
EARTH_LOWER_MANTLE_KM goes from 5711 to 5710 km. The gallery config
serves 5711.0 for the lower mantle shell and will be corrected on the
gallery side of C1, together with a false author list on the same entry.

THE READING is recorded in documentation/L322_earth_read_record_20260919.md.
Rows this session could not open are in its second section, "For Tony to
read". There is one of them.

SUCCESS looks like: one "ok" line per edit, then "patch applied".
FAILURE looks like: one ERROR: or ANCHOR FAIL: line, and NOTHING is
written to EITHER file. Undo is Discard Changes in GitHub Desktop.
"""

import hashlib
import os
import sys

STORE = "constants_new.py"
TOKENS = "constants_tokens.py"

# Content fingerprints, CRLF normalized.
BASE = {
    STORE:  "1e24b29ffc687e3553a6f373ab62d5d6",
    TOKENS: "db5f17b3afa345da36e2ddf85c6ae9bb",
}


def fail(msg):
    print(msg)
    print("NOTHING was written to either file. Undo is Discard Changes in "
          "GitHub Desktop.")
    sys.exit(1)


def fingerprint(raw):
    return hashlib.md5(raw.replace(b"\r\n", b"\n")).hexdigest()


# ---------------------------------------------------------------- edits
# (file, label, old_bytes, new_bytes). Every old must match EXACTLY ONCE.

EDITS = []

EDITS.append((TOKENS, 'TOKENS  four new tokens: km3_s2, m3_s2, rad_s, m3_per_km3',
    b'    "au": {\n        "dimension": "km",\n        "defining_constant": "KM_PER_AU",\n        "meaning": "astronomical units",\n    },\n',
    b'    "au": {\n        "dimension": "km",\n        "defining_constant": "KM_PER_AU",\n        "meaning": "astronomical units",\n    },\n    "km3_s2": {\n        "dimension": "km3 / s2",\n        "defining_constant": None,\n        "meaning": "cubic kilometres per second squared, a gravitational "\n                   "parameter",\n    },\n    "m3_s2": {\n        "dimension": "m3 / s2",\n        "defining_constant": None,\n        "meaning": "cubic metres per second squared, a gravitational "\n                   "parameter",\n    },\n    "rad_s": {\n        "dimension": "1 / s",\n        "defining_constant": None,\n        "meaning": "radians per second. The radian is dimensionless in "\n                   "SI, so the DIMENSION of an angular rate is a "\n                   "reciprocal second, which is what lets the "\n                   "geostationary cube root come out in kilometres",\n    },\n    "m3_per_km3": {\n        "dimension": "m3 / km3",\n        "defining_constant": None,\n        "meaning": "cubic metres per cubic kilometre, an exact unit "\n                   "conversion",\n    },\n'))
EDITS.append((STORE, 'KM_PER_AU  unit, status, figures, read',
    b'KM_PER_AU = 149597870.7\n',
    b'KM_PER_AU = 149597870.7\n# Unit: km\n# Status: measured V_CROSS_CHECKED 2026-09-19 -- belongs to no body\'s slice; it\n# Status+: is visited with Earth\'s because the Hill sphere needs it.\n# Figures: exact -- IAU 2012 Resolution B2 fixes 1 au at 149 597 870 700 m\n# Figures+: exactly, so every digit is known.\n# Read: Resolution B2, "on the re-definition of the astronomical unit of\n# Read+: length", IAU 2012 resolutions text, 2026-09-19, Claude Opus 5\n'))
EDITS.append((STORE, 'GM_SUN_SI  unit, status, figures, read',
    b'GM_SUN_SI = 1.3271244e20\n',
    b"GM_SUN_SI = 1.3271244e20\n# Unit: m3_s2\n# Status: measured V_CROSS_CHECKED 2026-09-19 -- belongs to no body's slice; it\n# Status+: is visited with Earth's because the Hill sphere needs it.\n# Figures: exact -- IAU 2015 Resolution B3 nominal values are exact by\n# Figures+: definition and are conversion factors, not measurements.\n# Read: Table 1, Prsa et al. 2016, AJ 152:41 (arXiv:1605.09788), 2026-09-19, Claude Opus 5\n"))
EDITS.append((STORE, 'EARTH_EQUATORIAL_RADIUS_KM  four fields',
    b'EARTH_EQUATORIAL_RADIUS_KM = 6378.1366\n',
    b'EARTH_EQUATORIAL_RADIUS_KM = 6378.1366\n# Unit: km\n# Status: measured V_CROSS_CHECKED 2026-09-19\n# Figures: 8 -- IERS gives 6378136.6 m with an uncertainty of 0.1 m, so\n# Figures+: the last significant digit is the tenth of a metre.\n# Read: Table 1.1 "IERS numerical standards", IERS Technical Note 36\n# Read+: p. 18, 2026-09-19, Claude Opus 5\n'))
EDITS.append((STORE, 'EARTH_POLAR_RADIUS_KM  source corrected, three fields',
    b'# Source: IERS Conventions (Petit & Luzum 2010); IAU B3 rounds to 6356.8 km\n',
    b"# Source: NASA Planetary Fact Sheet, Earth -- polar radius, 6356.752 km.\n# Source+: IERS Technical Note 36 does NOT tabulate a polar radius; it\n# Source+: follows from that table's equatorial radius and flattening\n# Source+: factor, 6378136.6 m x (1 - 1/298.25642) = 6356751.86 m, which\n# Source+: agrees with the fact sheet to the metre. Corrected 2026-09-19: the\n# Source+: old line named IERS as though it printed this number.\n# Unit: km\n# Status: measured V_CROSS_CHECKED 2026-09-19\n# Figures: 7 -- as printed on the fact sheet.\n"))
EDITS.append((STORE, 'EARTH_MEAN_RADIUS_KM  four fields',
    b'EARTH_MEAN_RADIUS_KM = 6371.0\n',
    b'EARTH_MEAN_RADIUS_KM = 6371.0\n# Unit: km\n# Status: measured V_SOURCED 2026-09-19\n# Figures: 4 -- the fact sheet prints 6371.000 in a table padded to three\n# Figures+: decimals throughout, so the trailing zeros are formatting and\n# Figures+: not precision. PREM quotes the same sphere as 6371 km.\n# Read: Earth Fact Sheet, bulk parameters, volumetric mean radius,\n# Read+: 2026-09-19, Claude Opus 5\n'))
EDITS.append((STORE, 'EARTH_INNER_CORE_KM  four fields',
    b'EARTH_INNER_CORE_KM = 1221.5\n',
    b'EARTH_INNER_CORE_KM = 1221.5\n# Unit: km\n# Status: measured V_SOURCED 2026-09-19\n# Figures: 5 -- PREM Table I gives the inner-core boundary as 1221.5 km.\n# Read: Table I, "Preliminary reference Earth model", Phys. Earth Planet.\n# Read+: Inter. 25:297-356, p. 308, 2026-09-19, Claude Opus 5\n'))
EDITS.append((STORE, 'EARTH_INNER_CORE_RADII  unit, figures',
    b'EARTH_INNER_CORE_RADII = EARTH_INNER_CORE_KM / EARTH_EQUATORIAL_RADIUS_KM\n',
    b'EARTH_INNER_CORE_RADII = EARTH_INNER_CORE_KM / EARTH_EQUATORIAL_RADIUS_KM\n# Unit: r_earth\n# Status: derived -- inherits EARTH_INNER_CORE_KM, EARTH_EQUATORIAL_RADIUS_KM\n# Figures: 5 -- set by EARTH_INNER_CORE_KM (1221.5, 5)\n'))
EDITS.append((STORE, 'EARTH_OUTER_CORE_KM  four fields',
    b'EARTH_OUTER_CORE_KM = 3480.0\n',
    b'EARTH_OUTER_CORE_KM = 3480.0\n# Unit: km\n# Status: measured V_SOURCED 2026-09-19\n# Figures: 4 -- PREM Table I prints 3480.0, but it pads every boundary\n# Figures+: radius to one decimal, so that trailing zero is the table\'s\n# Figures+: format rather than a claim to 100 m. A non-zero digit in that\n# Figures+: place does count, which is why 1221.5 and 6346.6 carry five.\n# Read: Table I, "Preliminary reference Earth model", Phys. Earth Planet.\n# Read+: Inter. 25:297-356, p. 308, 2026-09-19, Claude Opus 5\n'))
EDITS.append((STORE, 'EARTH_OUTER_CORE_RADII  unit, figures',
    b'EARTH_OUTER_CORE_RADII = EARTH_OUTER_CORE_KM / EARTH_EQUATORIAL_RADIUS_KM\n',
    b'EARTH_OUTER_CORE_RADII = EARTH_OUTER_CORE_KM / EARTH_EQUATORIAL_RADIUS_KM\n# Unit: r_earth\n# Status: derived -- inherits EARTH_OUTER_CORE_KM, EARTH_EQUATORIAL_RADIUS_KM\n# Figures: 4 -- set by EARTH_OUTER_CORE_KM (3480, 4)\n'))
EDITS.append((STORE, 'EARTH_D660_DEPTH_KM  four fields',
    b'EARTH_D660_DEPTH_KM = 660.0\n',
    b'EARTH_D660_DEPTH_KM = 660.0\n# Unit: km\n# Status: measured V_SOURCED 2026-09-19 -- L-253\n# Figures: 2 -- the global average depth is 660 +/- 10 km, so the last\n# Figures+: significant digit is the tens place. The trailing zero is not\n# Figures+: significant, which the source line above already said; the\n# Figures+: +/- 10 km behind it is now sourced (see the read line).\n# Read: Ishii et al. (2018), "Complete agreement of the post-spinel\n# Read+: transition with the 660-km seismic discontinuity", Sci. Rep.\n# Read+: 8:6358, results section -- "the global average depth of the\n# Read+: discontinuity is 660 +/- 10 km", 2026-09-19, Claude Opus 5\n'))
EDITS.append((STORE, 'EARTH_LOWER_MANTLE_KM  derived corrected 5711 -> 5710, unit, figures',
    b'# Derived: 6371.0 - 660 = 5711 km -- the OUTER boundary of the lower\n# Derived+: mantle shell, which is the 660 discontinuity. A SUBTRACTION is\n# Derived+: governed by decimal places, not significant figures: 6371.0 is\n# Derived+: good to tenths and 660 to units, so the difference is good to\n# Derived+: units. Physical uncertainty is far larger; see the note above.\n',
    b'# Derived: 6371.0 - 660 = 5710 km -- the OUTER boundary of the lower\n# Derived+: mantle shell, which is the 660 discontinuity. A SUBTRACTION is\n# Derived+: governed by decimal places, not significant figures. Corrected\n# Derived+: 2026-09-19: the old line said 660 was good to units and read off\n# Derived+: 5711. It is good to TENS -- its source gives 660 +/- 10 km --\n# Derived+: so the difference is good to tens and the value is 5710 km.\n# Unit: km\n# Status: derived -- inherits EARTH_MEAN_RADIUS_KM, EARTH_D660_DEPTH_KM\n# Figures: 3 -- 5710, the tens place, set by EARTH_D660_DEPTH_KM.\n'))
EDITS.append((STORE, 'EARTH_LOWER_MANTLE_RADII  derived corrected, unit, figures',
    b'# Derived: 5711 / 6378.1366 = 0.8954 -- 4 significant figures, set by\n# Derived+: the numerator. Report no more than that.\n',
    b'# Derived: 5710 / 6378.1366 = 0.895 -- 3 significant figures, set by\n# Derived+: the numerator. Report no more than that. Corrected 2026-09-19 with\n# Derived+: EARTH_LOWER_MANTLE_KM above.\n# Unit: r_earth\n# Status: derived -- inherits EARTH_LOWER_MANTLE_KM, EARTH_EQUATORIAL_RADIUS_KM\n# Figures: 3 -- set by EARTH_LOWER_MANTLE_KM\n'))
EDITS.append((STORE, 'EARTH_UPPER_MANTLE_KM  four fields',
    b'EARTH_UPPER_MANTLE_KM = 6346.6\n',
    b'EARTH_UPPER_MANTLE_KM = 6346.6\n# Unit: km\n# Status: measured V_SOURCED 2026-09-19\n# Figures: 5 -- PREM Table I gives the crust/LID boundary as 6346.6 km.\n# Read: Table I, "Preliminary reference Earth model", Phys. Earth Planet.\n# Read+: Inter. 25:297-356, p. 308, 2026-09-19, Claude Opus 5\n'))
EDITS.append((STORE, 'EARTH_UPPER_MANTLE_RADII  unit, figures',
    b'EARTH_UPPER_MANTLE_RADII = EARTH_UPPER_MANTLE_KM / EARTH_EQUATORIAL_RADIUS_KM\n',
    b'EARTH_UPPER_MANTLE_RADII = EARTH_UPPER_MANTLE_KM / EARTH_EQUATORIAL_RADIUS_KM\n# Unit: r_earth\n# Status: derived -- inherits EARTH_UPPER_MANTLE_KM, EARTH_EQUATORIAL_RADIUS_KM\n# Figures: 5 -- set by EARTH_UPPER_MANTLE_KM (6346.6, 5)\n'))
EDITS.append((STORE, 'EARTH_GM_KM3_S2  four fields',
    b'EARTH_GM_KM3_S2 = 398600.4418\n',
    b'EARTH_GM_KM3_S2 = 398600.4418\n# Unit: km3_s2\n# Status: measured V_SOURCED 2026-09-19\n# Figures: 9 -- the tabulated uncertainty, 8e5 m^3 s^-2 on 3.986004418e14,\n# Figures+: is about 2 parts in 1e9, so it falls in the ninth figure.\n# Read: Table 1.1 "IERS numerical standards", IERS Technical Note 36\n# Read+: p. 18, 2026-09-19, Claude Opus 5\n'))
EDITS.append((STORE, 'EARTH_GM_KM3_S2  note corrected TCB -> TCG',
    b'# Note: TCB-compatible value as tabulated; the TT-compatible value differs\n# Note+: in the ninth figure, below anything this file derives from it.\n',
    b'# Note: TCG-compatible value as tabulated; the TT-compatible value differs\n# Note+: in the ninth figure, below anything this file derives from it.\n# Note+: Corrected 2026-09-19 -- the old line said TCB. Table 1.1\'s own footnote\n# Note+: reads "The value for GM(Earth) is TCG-compatible."\n'))
EDITS.append((STORE, 'EARTH_ROTATION_RATE_RAD_S  source corrected Table 1.1 -> 1.2',
    b'# Source: IERS Conventions (2010), TN36 Table 1.1 -- nominal mean Earth\n# Source+: angular velocity, 7.292115e-5 rad s^-1.\n',
    b'# Source: IERS Conventions (2010), IERS Technical Note 36, Table 1.2\n# Source+: "Parameters of the Geodetic Reference System GRS80" -- nominal\n# Source+: mean Earth angular velocity, 7.292115e-5 rad s^-1. Corrected\n# Source+: 2026-09-19: the old line said Table 1.1, which has no angular\n# Source+: velocity in it. The value is unchanged; only the table is.\n'))
EDITS.append((STORE, 'EARTH_ROTATION_RATE_RAD_S  four fields',
    b'EARTH_ROTATION_RATE_RAD_S = 7.292115e-5\n',
    b'EARTH_ROTATION_RATE_RAD_S = 7.292115e-5\n# Unit: rad_s\n# Status: measured V_SOURCED 2026-09-19\n# Figures: 7 -- as printed.\n# Read: Table 1.2 "Parameters of the Geodetic Reference System GRS80",\n# Read+: IERS Technical Note 36 p. 19, 2026-09-19, Claude Opus 5\n'))
EDITS.append((STORE, 'EARTH_GEOSTATIONARY_RADIUS_KM  derived reworded, unit, figures',
    b'# Derived: (398600.4418 / 7.292115e-5^2)^(1/3) = 42164.17 km -- the\n# Derived+: circular orbit whose period is one sidereal rotation. Seven\n# Derived+: figures in both inputs; report 42,164 km.\n',
    b'# Derived: (398600.4418 / 7.292115e-5^2)^(1/3) = 42164.17 km -- the\n# Derived+: circular orbit whose period is one sidereal rotation. The\n# Derived+: rotation rate carries seven figures and the GM nine, so seven\n# Derived+: is the count; report 42,164 km.\n# Unit: km\n# Status: derived -- inherits EARTH_GM_KM3_S2, EARTH_ROTATION_RATE_RAD_S\n# Figures: 7 -- set by EARTH_ROTATION_RATE_RAD_S (7.292115e-5, 7). The\n# Figures+: cube root damps rather than magnifies, so no figure is dropped.\n'))
EDITS.append((STORE, 'EARTH_GEOSTATIONARY_RADII  unit, figures',
    b'EARTH_GEOSTATIONARY_RADII = EARTH_GEOSTATIONARY_RADIUS_KM / EARTH_EQUATORIAL_RADIUS_KM\n',
    b'EARTH_GEOSTATIONARY_RADII = EARTH_GEOSTATIONARY_RADIUS_KM / EARTH_EQUATORIAL_RADIUS_KM\n# Unit: r_earth\n# Status: derived -- inherits EARTH_GEOSTATIONARY_RADIUS_KM,\n# Status+: EARTH_EQUATORIAL_RADIUS_KM\n# Figures: 7 -- set by EARTH_GEOSTATIONARY_RADIUS_KM\n'))
EDITS.append((STORE, 'EARTH_LEO_UPPER_ALTITUDE_KM  three fields, read deferred to Tony',
    b'EARTH_LEO_UPPER_ALTITUDE_KM = 2000.0\n',
    b'EARTH_LEO_UPPER_ALTITUDE_KM = 2000.0\n# Unit: km\n# Status: measured V_SOURCED 2026-09-19\n# Figures: exact -- the IADC protected region is DEFINED at an altitude\n# Figures+: of 2,000 km. A definition, not a measurement.\n# Read: for Tony -- see documentation/L322_earth_read_record_20260919.md.\n# Read+: The primary IADC document could not be opened from this session;\n# Read+: the definition was confirmed only in reproductions of it.\n'))
EDITS.append((STORE, 'EARTH_LEO_LOWER_ALTITUDE_KM  unit, status, figures',
    b'EARTH_LEO_LOWER_ALTITUDE_KM = 200.0\n',
    b'EARTH_LEO_LOWER_ALTITUDE_KM = 200.0\n# Unit: km\n# Status: declared 2026-09-19 -- a drawing floor, not a measured boundary, so\n# Status+: there is no source to read against and none is expected.\n# Figures: exact -- a drawing choice, so all of its digits are known.\n'))
EDITS.append((STORE, 'EARTH_LEO_INNER_KM  derived line added, unit, figures',
    b'EARTH_LEO_INNER_KM = EARTH_EQUATORIAL_RADIUS_KM + EARTH_LEO_LOWER_ALTITUDE_KM\n',
    b'EARTH_LEO_INNER_KM = EARTH_EQUATORIAL_RADIUS_KM + EARTH_LEO_LOWER_ALTITUDE_KM\n# Derived: 6378.1366 + 200 = 6578.1366 km. A SUM is good to the coarsest\n# Derived+: decimal place among its MEASURED inputs; the 200 km floor is a\n# Derived+: declared choice and exact, so the equatorial radius sets it.\n# Unit: km\n# Status: derived -- inherits EARTH_EQUATORIAL_RADIUS_KM,\n# Status+: EARTH_LEO_LOWER_ALTITUDE_KM\n# Figures: 8 -- set by EARTH_EQUATORIAL_RADIUS_KM\n'))
EDITS.append((STORE, 'EARTH_LEO_OUTER_KM  unit, figures',
    b'EARTH_LEO_OUTER_KM = EARTH_EQUATORIAL_RADIUS_KM + EARTH_LEO_UPPER_ALTITUDE_KM\n',
    b'EARTH_LEO_OUTER_KM = EARTH_EQUATORIAL_RADIUS_KM + EARTH_LEO_UPPER_ALTITUDE_KM\n# Unit: km\n# Status: derived -- inherits EARTH_EQUATORIAL_RADIUS_KM,\n# Status+: EARTH_LEO_UPPER_ALTITUDE_KM\n# Figures: 8 -- set by EARTH_EQUATORIAL_RADIUS_KM; the 2,000 km IADC\n# Figures+: altitude is exact and does not limit the sum.\n'))
EDITS.append((STORE, 'EARTH_LEO_INNER_RADII  derived line added, unit, figures',
    b'EARTH_LEO_INNER_RADII = EARTH_LEO_INNER_KM / EARTH_EQUATORIAL_RADIUS_KM\n',
    b'EARTH_LEO_INNER_RADII = EARTH_LEO_INNER_KM / EARTH_EQUATORIAL_RADIUS_KM\n# Derived: 6578.1366 / 6378.1366 = 1.0313571\n# Unit: r_earth\n# Status: derived -- inherits EARTH_LEO_INNER_KM, EARTH_EQUATORIAL_RADIUS_KM\n# Figures: 8 -- set by EARTH_LEO_INNER_KM\n'))
EDITS.append((STORE, 'EARTH_LEO_OUTER_RADII  unit, figures',
    b'EARTH_LEO_OUTER_RADII = EARTH_LEO_OUTER_KM / EARTH_EQUATORIAL_RADIUS_KM\n',
    b'EARTH_LEO_OUTER_RADII = EARTH_LEO_OUTER_KM / EARTH_EQUATORIAL_RADIUS_KM\n# Unit: r_earth\n# Status: derived -- inherits EARTH_LEO_OUTER_KM, EARTH_EQUATORIAL_RADIUS_KM\n# Figures: 8 -- set by EARTH_LEO_OUTER_KM\n'))
EDITS.append((STORE, 'EARTH_STRATOPAUSE_ALTITUDE_KM  four fields',
    b'EARTH_STRATOPAUSE_ALTITUDE_KM = 50.0\n',
    b'EARTH_STRATOPAUSE_ALTITUDE_KM = 50.0\n# Unit: km\n# Status: measured V_SOURCED 2026-09-19\n# Figures: 2 -- NOAA gives the top of the stratosphere as "around 31 miles\n# Figures+: (50 km)"; 31 miles is 49.9 km, so two figures is what it says.\n# Read: "Layers of the Atmosphere", NOAA JetStream, stratosphere section,\n# Read+: 2026-09-19, Claude Opus 5\n'))
EDITS.append((STORE, 'EARTH_THERMOPAUSE_ALTITUDE_KM  four fields',
    b'EARTH_THERMOPAUSE_ALTITUDE_KM = 600.0\n',
    b'EARTH_THERMOPAUSE_ALTITUDE_KM = 600.0\n# Unit: km\n# Status: measured V_SOURCED 2026-09-19\n# Figures: 2 -- NOAA gives the thermopause at "about 375 miles (600 km)";\n# Figures+: 375 miles is 603.5 km, so the km figure carries two.\n# Read: "Layers of the Atmosphere", NOAA JetStream, thermosphere and\n# Read+: exosphere sections, 2026-09-19, Claude Opus 5\n'))
EDITS.append((STORE, 'EARTH_STRATOPAUSE_RADII  derived line added, unit, figures',
    b'EARTH_STRATOPAUSE_RADII = (EARTH_EQUATORIAL_RADIUS_KM + EARTH_STRATOPAUSE_ALTITUDE_KM) / EARTH_EQUATORIAL_RADIUS_KM\n',
    b'EARTH_STRATOPAUSE_RADII = (EARTH_EQUATORIAL_RADIUS_KM + EARTH_STRATOPAUSE_ALTITUDE_KM) / EARTH_EQUATORIAL_RADIUS_KM\n# Derived: (6378.1366 + 50) / 6378.1366 = 1.008. The 50 km altitude\n# Derived+: carries two figures, so its last significant digit is the ones\n# Derived+: place and the sum is good to units: 6428 km.\n# Unit: r_earth\n# Status: derived -- inherits EARTH_EQUATORIAL_RADIUS_KM,\n# Status+: EARTH_STRATOPAUSE_ALTITUDE_KM\n# Figures: 4 -- set by the sum, which EARTH_STRATOPAUSE_ALTITUDE_KM limits.\n'))
EDITS.append((STORE, 'EARTH_THERMOPAUSE_RADII  derived corrected, unit, figures',
    b'# Derived: 1.0078 and 1.0941.\n',
    b'# Derived: (6378.1366 + 600) / 6378.1366 = 1.09. The 600 km altitude\n# Derived+: carries two figures, so its last significant digit is the tens\n# Derived+: place and the sum is good to tens: 6980 km. Corrected 2026-09-19 --\n# Derived+: the old line read 1.0078 and 1.0941, which declared more\n# Derived+: figures than either altitude supports, and covered two rows.\n# Unit: r_earth\n# Status: derived -- inherits EARTH_EQUATORIAL_RADIUS_KM,\n# Status+: EARTH_THERMOPAUSE_ALTITUDE_KM\n# Figures: 3 -- set by the sum, which EARTH_THERMOPAUSE_ALTITUDE_KM limits.\n'))
EDITS.append((STORE, 'EARTH_GEOCORONA_RADII  four fields',
    b'EARTH_GEOCORONA_RADII = 100.0\n',
    b'EARTH_GEOCORONA_RADII = 100.0\n# Unit: r_earth\n# Status: measured V_SOURCED 2026-09-19\n# Figures: 1 -- Baliukin reports a detection FLOOR, "at least 100 Earth\n# Figures+: radii". The trailing zeros are not significant, and the note\n# Figures+: below says what the number is rather than implying an edge.\n# Read: abstract, Baliukin et al. (2019), J. Geophys. Res. Space Physics\n# Read+: 124:861-885 -- "found to extend at least up to 100 Earth Radii\n# Read+: ... encompassing the orbit of the Moon", 2026-09-19, Claude Opus 5\n'))
EDITS.append((STORE, 'EARTH_HILL_SPHERE_KM  named conversion M3_PER_KM3, unit, figures',
    b'EARTH_HILL_SPHERE_KM = KM_PER_AU * (EARTH_GM_KM3_S2 / (3.0 * GM_SUN_SI * 1.0e-9)) ** (1.0 / 3.0)\n',
    b"M3_PER_KM3 = 1.0e9\n# Unit: m3_per_km3\n# Status: declared 2026-09-19 -- an exact unit conversion, 1 km^3 = 1e9 m^3.\n# Status+: Belongs to no body's slice. It exists because a bare 1.0e-9\n# Status+: inside the Hill sphere expression converted cubic metres to\n# Status+: cubic kilometres where nothing could see that it carried a\n# Status+: unit, and test_dimensions.py read the result as a MISMATCH of\n# Status+: exactly 1000x. Naming the factor is the fix.\n# Figures: exact -- a definition, not a measurement.\n\nEARTH_HILL_SPHERE_KM = KM_PER_AU * (EARTH_GM_KM3_S2 * M3_PER_KM3 / (3.0 * GM_SUN_SI)) ** (1.0 / 3.0)\n# Unit: km\n# Status: derived -- inherits KM_PER_AU, EARTH_GM_KM3_S2, M3_PER_KM3, GM_SUN_SI\n# Figures: 7 -- EARTH_GM_KM3_S2 carries nine and every other input is\n# Figures+: exact, but a = 1 AU is a substitution for Earth's semi-major\n# Figures+: axis and agrees with it only to seven figures (see the note\n# Figures+: below), so seven is the count. The formula's own idealisation\n# Figures+: is coarser than any of this; report 1.50e6 km.\n"))
EDITS.append((STORE, 'EARTH_HILL_SPHERE_RADII  unit, figures',
    b'EARTH_HILL_SPHERE_RADII = EARTH_HILL_SPHERE_KM / EARTH_EQUATORIAL_RADIUS_KM\n',
    b'EARTH_HILL_SPHERE_RADII = EARTH_HILL_SPHERE_KM / EARTH_EQUATORIAL_RADIUS_KM\n# Unit: r_earth\n# Status: derived -- inherits EARTH_HILL_SPHERE_KM, EARTH_EQUATORIAL_RADIUS_KM\n# Figures: 7 -- set by EARTH_HILL_SPHERE_KM\n'))


def main():
    here = os.path.basename(os.getcwd())
    if here == "documentation":
        fail("ERROR: this script is running from documentation/. Move it "
             "to the repository ROOT and run it there.")
    for path in (STORE, TOKENS):
        if not os.path.exists(path):
            fail("ERROR: " + path + " is not here. Run this from the "
                 "ORRERY repo root.")

    raws = {}
    for path in (STORE, TOKENS):
        with open(path, "rb") as handle:
            raws[path] = handle.read()
        got = fingerprint(raws[path])
        if got != BASE[path]:
            fail("ERROR: " + path + " is not the file this patch was cut "
                 "against.\n  expected " + BASE[path] + "\n  found    "
                 + got + "\nIf the patch already ran, this is what a "
                 "second run looks like: it refuses.")

    out = dict(raws)
    for path, label, old, new in EDITS:
        is_crlf = raws[path].count(b"\r\n") > 0
        if is_crlf:
            old = old.replace(b"\n", b"\r\n")
            new = new.replace(b"\n", b"\r\n")
        n = out[path].count(old)
        if n != 1:
            fail("ANCHOR FAIL: expected exactly 1 match, found %d -- %s\n"
                 "  anchor began: %r" % (n, label, old[:70]))
        out[path] = out[path].replace(old, new)

    for path, data in out.items():
        try:
            data.decode("ascii")
        except UnicodeDecodeError as exc:
            fail("ERROR: the result for " + path + " is not ASCII (%s)."
                 % exc)

    for path, data in out.items():
        with open(path, "wb") as handle:
            handle.write(data)

    for path, label, _old, _new in EDITS:
        print("  ok  " + label)
    print("")
    for path in sorted(out):
        print("      %-24s %7d -> %7d bytes"
              % (path, len(raws[path]), len(out[path])))
    print("")
    print("patch applied (2 files, %d edits)" % len(EDITS))
    print("")
    print("NOW, in order:")
    print("  1. Run the orrery maintenance run. The three constants")
    print("     checkers should report Earth's rows JUDGED rather than")
    print("     NO UNIT, and nothing should fail.")
    print("  2. Move this script into documentation/.")
    print("  3. Commit and push. Report the new SHA.")
    print("  4. The gallery half of C1 follows: pull the export, run the")
    print("     mirror, rebuild the cache with OneDrive syncing PAUSED,")
    print("     run the gallery maintenance run, commit the config and")
    print("     the cache TOGETHER, push.")
    print("")
    print("Undo at any point is Discard Changes in GitHub Desktop.")


if __name__ == "__main__":
    main()
