"""patch_L322_D_2_orrery_rows_and_poles_20260923.py -- L-322 Stage D, patch D2.

RUN COMMAND

    Save this file in the ROOT of the palomas_orrery repository, beside
    constants_new.py, open it in VS Code and click Run. It refuses to run
    from documentation/ or from anywhere else. After it has run, MOVE it
    into documentation/.

WHAT IT CHANGES, and what stays

    Five files. Every edit is anchored on text this patch expects to find,
    and the run is all-or-nothing: if one anchor is missing, or a file is
    not the version this was built against, NOTHING is written.

    constants_new.py      seven new rows and the pole dict. Earth's
                          sidereal rotation period, derived from the
                          rotation rate through an exact seconds-per-hour
                          row. Earth's two pole rows, the frame's own
                          axis, drawn only when the pole of the scene's
                          date cannot be fetched. The angle that defines
                          the drawing's frame, stored in arcseconds as
                          Horizons prints it, with its degree form
                          computed through an exact arcseconds-per-degree
                          row; its row says in words that it is not
                          Earth's tilt. The planet_poles dict, moved here
                          from idealized_orbits.py with its false
                          "cross-check exactly" sentence removed.
    constants_tokens.py   four unit tokens: arcsec, arcsec_per_deg,
                          hours, s_per_h.
    idealized_orbits.py   imports planet_poles instead of typing it; the
                          rotation into the ecliptic frame reads the
                          frame's angle row instead of a typed 23.439291
                          labelled "IAU 2006".
    solar_visualization_shells.py   one comment names the dict's new home.
    planet_visualization_utilities.py  Earth's axis hover prints the
                          sidereal period from the new row at seven
                          figures, "Sidereal rotation: 23.93447 h (one
                          turn against the stars)", where it typed
                          "23.93 h".

    NOT changed: Earth's axis still points where it did, and its tilt on
    the hover is still the typed 23.44 deg. The pole of the scene's date,
    fetched from Horizons, and the tilt derived from it are the next
    orrery patch. Nothing in the gallery repository is touched.

WHAT IS PERMANENT AND WHAT IS NOT

    This script is disposable and aborts on a second run. The rows, the
    tokens and the moved dict are permanent.

Built on orrery bba21459bb5dae46d94cb650fd6ba4ab05ee0286
at https://github.com/tonylquintanilla/palomas_orrery,
from documentation/BUILD_MANIFEST_L322_D_earth_pole_20260922.md rev 3.
(Gallery 2e0fa8f5de7ec1dc99597dc302e4e4c4eb745e72 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io is not
touched by this patch.)

Written September 23, 2026 with Anthropic's Claude Opus 5.5.
"""

import hashlib
import os
import sys

EDITS = [
    ('constants_new.py', 'f096b745c27ee00cd878684ebf4c90c1', '8cff4941131ffd9702d7dd86baa369ec', [
        ('retired "dimensionless" token for tokens that name the quantity)\n"""\n',
         'retired "dimensionless" token for tokens that name the quantity)\nModule updated: September 23, 2026 with Anthropic\'s Claude Opus 5.5\n(L-322 Stage D, patch D2: Earth\'s sidereal rotation period is derived\nfrom the rotation rate through an exact S_PER_HOUR row; Earth\'s pole\nrows are the frame\'s own axis, drawn only when the pole of the scene\'s\ndate cannot be fetched; the frame\'s defining obliquity is stored in\narcseconds, the form Horizons prints, and is never Earth\'s tilt; and the\nplanet_poles dict moves here from idealized_orbits.py, with its false\ncross-check sentence removed)\n"""\n'),
        ('# Derived: 42164.17 / 6378.1366 = 6.6107 -- report no more than five figures.\n',
         '# Derived: 42164.17 / 6378.1366 = 6.6107 -- report no more than five figures.\n\n# --- Earth\'s rotation axis and period (L-322 Stage D, 2026-09-23) ------------\n# Three kinds of number live here, and none of them is Earth\'s tilt.\n# The period is derived from the rotation rate above. The pole rows are the\n# frame\'s own axis, drawn only when the pole of the scene\'s date cannot be\n# fetched from Horizons. The obliquity rows are the angle that DEFINES the\n# drawing\'s frame from the ICRF; they turn Horizons\' sky directions into\n# that frame. Earth\'s actual tilt on a date is not stored anywhere: it is\n# the angle between the fetched pole of that date and the fetched orbit of\n# that date (Tony\'s ruling, 2026-09-23, build manifest rev 3 section 0).\n\nS_PER_HOUR = 3600.0\n# Unit: s_per_h\n# Status: declared 2026-09-23 -- an exact unit conversion, seconds in one\n# Status+: hour. Belongs to no body\'s slice.\n# Figures: exact -- a definition, not a measurement.\n# Read: Table 6, sec. 5.1.1, NIST Guide to the SI (SP 811), chapter 5,\n# Read+: 2026-09-23, Claude Opus 5.5\n# Source: NIST Special Publication 811, Guide for the Use of the SI, sec.\n# Source+: 5.1.1, Table 6 (units the CIPM accepts for use with the SI) --\n# Source+: the hour is 60 minutes, 3600 seconds, by definition.\n# Ref: https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-5-units-outside-si\n# Note: exists so the period below converts through a row and not a bare\n# Note+: 3600, because the unit check converts units by itself and a bare\n# Note+: divisor makes the stored value disagree with the arithmetic\n# Note+: (provenance-discipline 2.18, a unit conversion inside an\n# Note+: expression is an exact row). Neither checker judges this row; its\n# Note+: unit is asserted here, as DEG_PER_RAD\'s is.\n\nEARTH_SIDEREAL_ROTATION_PERIOD_H = 2.0 * math.pi / EARTH_ROTATION_RATE_RAD_S / S_PER_HOUR\n# Derived: one full turn, two pi radians, divided by the angular rate, in\n# Derived+: hours = 23.93447\n# Unit: hours\n# Status: derived 2026-09-23 -- inherits EARTH_ROTATION_RATE_RAD_S,\n# Status+: S_PER_HOUR\n# Figures: 7 -- set by EARTH_ROTATION_RATE_RAD_S (7.292115e-5, 7)\n# Note: the SIDEREAL period, one turn measured against the stars. The\n# Note+: 24-hour day a visitor knows is the turn measured against the Sun,\n# Note+: which is longer because Earth moves along its orbit while it\n# Note+: turns. The two pi stays a bare number on purpose: the rad_s token\n# Note+: already treats the radian as dimensionless, so giving two pi a\n# Note+: unit fails the unit check the other way.\n\nEARTH_POLE_RA_J2000_DEG = 0.0\n# Unit: deg\n# Status: declared 2026-09-23 -- a frame definition, the FALLBACK only\n# Figures: exact -- the ICRF\'s z-axis, by the frame\'s construction.\n# Declared: the right ascension of the axis drawn for Earth when the pole of\n# Declared+: the scene\'s date cannot be fetched from Horizons. At declination\n# Declared+: 90 every right ascension names the same direction, so this 0.0\n# Declared+: is a placeholder the transform ignores. The displays that draw\n# Declared+: this fallback say the axis shown is the frame\'s year-2000 axis\n# Declared+: because Horizons could not be reached.\n# Read: IERS Technical Note 36, chapter 2, section 2.1.1 "Equator", pp.\n# Read+: 21-22, 2026-09-23, Claude Opus 5.5; and the Horizons manual,\n# Read+: "Reference Frames", sections "International Celestial Reference\n# Read+: Frame (ICRF)" and "Ecliptic of Standard Epoch", 2026-09-23, Claude\n# Read+: Opus 5.5.\n# Source: IERS Conventions (2010), IERS Technical Note 36, sec. 2.1.1 -- the\n# Source+: ICRS principal plane is held close to the mean equator at\n# Source+: J2000.0, and the mean pole at J2000.0 sits 17.1 mas toward 12h and\n# Source+: 5.0 mas toward 18h from the ICRS pole (IERS 1996 nutation), or\n# Source+: 16.6 mas and 6.8 mas (MHB2000): about 0.02 arcseconds, some five\n# Source+: millionths of a degree. The Horizons manual: the ICRF was built to\n# Source+: align with FK5/J2000 and differs from it by at most 0.02\n# Source+: arcseconds.\n# Ref: https://iers-conventions.obspm.fr/content/tn36.pdf\n# Ref: https://ssd.jpl.nasa.gov/horizons/manual.html\n# Note: until 2026-09-23 this direction was typed in the planet_poles dict\n# Note+: in idealized_orbits.py and cited to the IAU working group report of\n# Note+: 2015 (Archinal et al. 2018), which says in its abstract, Table 1\n# Note+: footnote 2 and section 10 that it no longer gives Earth\'s pole.\n\nEARTH_POLE_DEC_J2000_DEG = 90.0\n# Unit: deg\n# Status: declared 2026-09-23 -- a frame definition, the FALLBACK only\n# Figures: exact -- the ICRF\'s z-axis, by the frame\'s construction.\n# Declared: the declination of the axis drawn for Earth when the pole of the\n# Declared+: scene\'s date cannot be fetched. The ICRF\'s z-axis is Earth\'s\n# Declared+: mean pole of the year 2000 to within the offset in the Source\n# Declared+: line of the row above, far below anything a drawing shows.\n# Read: as EARTH_POLE_RA_J2000_DEG, 2026-09-23, Claude Opus 5.5.\n# Source: as EARTH_POLE_RA_J2000_DEG.\n# Ref: https://iers-conventions.obspm.fr/content/tn36.pdf\n\nARCSEC_PER_DEG = 3600.0\n# Unit: arcsec_per_deg\n# Status: declared 2026-09-23 -- an exact unit conversion, arcseconds in\n# Status+: one degree. Belongs to no body\'s slice.\n# Figures: exact -- a definition, not a measurement.\n# Read: Table 6, sec. 5.1.1, NIST Guide to the SI (SP 811), chapter 5,\n# Read+: 2026-09-23, Claude Opus 5.5\n# Source: NIST Special Publication 811, sec. 5.1.1, Table 6 -- the second\n# Source+: of arc is one sixtieth of the minute of arc, which is one\n# Source+: sixtieth of the degree, so a degree is 3600 arcseconds by\n# Source+: definition.\n# Ref: https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-5-units-outside-si\n# Note: neither checker judges this row; its unit is asserted here.\n\nEARTH_OBLIQUITY_J2000_ARCSEC = 84381.448\n# Unit: arcsec\n# Status: declared 2026-09-23 -- a frame definition, not a measurement\n# Figures: exact -- a frame definition.\n# Declared: the angle Horizons rotates about the ICRF x-axis to build the\n# Declared+: frame it calls the ecliptic of J2000, which is the frame both\n# Declared+: drawings place everything in. It is the IAU 1976 value, and it\n# Declared+: is NOT Earth\'s tilt: IERS Technical Note 36, Table 1.1, gives\n# Declared+: Earth\'s obliquity at J2000.0 as 84381.406 arcseconds (IAU\n# Declared+: 2006), and the tilt on any other date moves further. This row\n# Declared+: is used to turn Horizons\' ICRF directions into the drawing\'s\n# Declared+: frame and is never printed as Earth\'s tilt (build manifest rev\n# Declared+: 3, section 0).\n# Read: the Horizons manual, "General Definitions", "Ecliptic", and\n# Read+: "Reference Frames", "Ecliptic of Standard Epoch (J2000 or B1950)",\n# Read+: 2026-09-23, Claude Opus 5.5.\n# Source: JPL Horizons manual -- Horizons turns the ICRF into its ecliptic\n# Source+: of J2000 with the fixed IAU 1976/1980 obliquity of 84381.448\n# Source+: arcseconds at the J2000.0 epoch, a rotation about the ICRF x-axis.\n# Ref: https://ssd.jpl.nasa.gov/horizons/manual.html\n\nEARTH_OBLIQUITY_J2000_DEG = EARTH_OBLIQUITY_J2000_ARCSEC / ARCSEC_PER_DEG\n# Derived: the frame\'s defining angle in degrees, 84381.448 / 3600\n# Derived+: = 23.439291111\n# Unit: deg\n# Status: derived 2026-09-23 -- inherits EARTH_OBLIQUITY_J2000_ARCSEC,\n# Status+: ARCSEC_PER_DEG\n# Figures: exact -- both inputs are exact.\n# Note: replaces the 23.439291 typed in idealized_orbits.py (the rotation\n# Note+: into the ecliptic frame) and in the gallery\'s feature_renderers.js,\n# Note+: both labelled "IAU 2006". The value was the frame\'s and the label\n# Note+: was wrong: the IAU 2006 value is 84381.406 arcseconds. Not printed\n# Note+: by any display, so it carries no print count.\n\n# The pole directions of the bodies the orrery draws with an axis, as ICRF\n# right ascension and declination in degrees. Moved here from\n# idealized_orbits.py on 2026-09-23 (L-322 ruling (a) of 2026-09-14), which\n# now imports it. Earth\'s entry reads the two fallback rows above; the\n# orrery draws Earth\'s pole of the scene\'s date from Horizons when it can.\n# Every other entry keeps the value it had and has no status line, which is\n# how this file says the provenance pass has not reached it. The checkers\n# read only top-level rows, so no checker sees these entries: the move\n# changes where they live, not whether anything checks them. Each is\n# checked when its own body is walked.\n# Source: IAU WGCCRE report, Archinal et al. (2018), Cel. Mech. Dyn. Astron.\n# Source+: 130:22, Table 1 (Sun and planets). Not for Earth, which the report\n# Source+: no longer gives, and not for the Moon, whose Table 2 row now reads\n# Source+: "See Sect. 3".\n# Note: compared with Table 1 at the year 2000 on 2026-09-22 (build manifest\n# Note+: section 2.5): Mercury, Uranus and Neptune disagree with the table and\n# Note+: are recorded on L-322 as one class, not fixed here. An earlier\n# Note+: comment said six entries cross-check exactly against the table; for\n# Note+: Uranus and Neptune that was false, and it is removed.\nplanet_poles = {\n    \'Sun\': {\'ra\': 286.13, \'dec\': 63.87},      # Source: IAU 2018 (Archinal et al.)\n    \'Mercury\': {\'ra\': 281.01, \'dec\': 61.45},  # Source: IAU 2018 (MESSENGER-updated)\n    \'Venus\': {\'ra\': 272.76, \'dec\': 67.16},    # Source: IAU 2018 (retrograde; pole is IAU-north)\n    \'Earth\': {\'ra\': EARTH_POLE_RA_J2000_DEG, \'dec\': EARTH_POLE_DEC_J2000_DEG},  # the frame\'s axis; fallback only\n    \'Moon\': {\'ra\': 269.99, \'dec\': 66.54},     # the cited Table 2 no longer has a row for the Moon ("See Sect. 3")\n    \'Mars\': {\'ra\': 317.68, \'dec\': 52.89},\n    \'Jupiter\': {\'ra\': 268.05, \'dec\': 64.49},\n    \'Saturn\': {\'ra\': 40.58, \'dec\': 83.54},\n    \'Uranus\': {\'ra\': 257.43, \'dec\': -15.10},\n    \'Neptune\': {\'ra\': 299.36, \'dec\': 43.46},\n    \'Pluto\': {\'ra\': 132.99, \'dec\': -6.16}\n}\n'),
    ]),
    ('constants_tokens.py', '7c57fd3343ef319c50bc4f2f3b556b21', '4c03c91854749b6437db1219f83d585c', [
        ('tokens carry Earth\'s dipole tilt rate and the coefficient rates it is\ncomputed from.)\n"""\n',
         'tokens carry Earth\'s dipole tilt rate and the coefficient rates it is\ncomputed from.)\nModule updated: September 23, 2026 with Anthropic\'s Claude Opus 5.5\n(L-322 Stage D: four tokens. arcsec and hours for the frame\'s obliquity\nand Earth\'s rotation period, and arcsec_per_deg and s_per_h for the two\nexact conversion rows those are converted through.)\n"""\n'),
        ('    "deg_per_year": {\n        "dimension": "deg / yr",\n        "defining_constant": None,\n        "meaning": "degrees of angle per year",\n    },\n}\n',
         '    "deg_per_year": {\n        "dimension": "deg / yr",\n        "defining_constant": None,\n        "meaning": "degrees of angle per year",\n    },\n    # L-322 Stage D (2026-09-23): two quantities and the two exact\n    # conversions they go through, so no expression divides by a bare\n    # 3600 (provenance-discipline 2.18).\n    "arcsec": {\n        "dimension": "arcsec",\n        "defining_constant": None,\n        "meaning": "arcseconds of angle",\n    },\n    "arcsec_per_deg": {\n        "dimension": "arcsec / deg",\n        "defining_constant": None,\n        "meaning": "arcseconds per degree, an exact unit conversion",\n    },\n    "hours": {\n        "dimension": "h",\n        "defining_constant": None,\n        "meaning": "hours",\n    },\n    "s_per_h": {\n        "dimension": "s / h",\n        "defining_constant": None,\n        "meaning": "seconds per hour, an exact unit conversion",\n    },\n}\n'),
    ]),
    ('idealized_orbits.py', '2708c9be400b69cd501eb6b4a11059de', '43ff9b435df77a51354d728065d70ec8', [
        ('(provenance audit; 45 hardcoded AU-in-km values replaced with KM_PER_AU\nimport from constants_new.py)\n\nRole: computation\n',
         "(provenance audit; 45 hardcoded AU-in-km values replaced with KM_PER_AU\nimport from constants_new.py)\nModule updated: September 23, 2026 with Anthropic's Claude Opus 5.5\n(L-322 Stage D: planet_poles moved to constants_new.py and imported\nhere; the rotation of a pole into the ecliptic frame reads\nEARTH_OBLIQUITY_J2000_DEG, the frame's defining angle, where it typed\n23.439291 labelled IAU 2006)\n\nRole: computation\n"),
        ('from constants_new import color_map, KNOWN_ORBITAL_PERIODS, KM_PER_AU\n',
         'from constants_new import color_map, KNOWN_ORBITAL_PERIODS, KM_PER_AU, EARTH_OBLIQUITY_J2000_DEG\n'),
        ("# Dictionary of planet pole directions (J2000)\n# IAU north-pole directions (ICRF equatorial, J2000). RA/Dec in degrees.\n# Source: IAU WGCCRE report, Archinal et al. 2018, Cel. Mech. Dyn. Astron. 130:22\n# Source+: (Table 1, planets/Sun; Table 2, Moon mean pole 269.9949/66.5392, E-terms dropped).\n# Source+: N15+ (June 2026): Sun/Mercury/Venus/Earth/Moon added so create_planet_transformation_matrix\n# Source+: yields a correct spin pole for every shell body (rotation-axis primitive). The six prior\n# Source+: entries are unchanged and cross-check exactly against the same IAU table.\nplanet_poles = {\n    'Sun': {'ra': 286.13, 'dec': 63.87},      # Source: IAU 2018 (Archinal et al.)\n    'Mercury': {'ra': 281.01, 'dec': 61.45},  # Source: IAU 2018 (MESSENGER-updated)\n    'Venus': {'ra': 272.76, 'dec': 67.16},    # Source: IAU 2018 (retrograde; pole is IAU-north)\n    'Earth': {'ra': 0.00, 'dec': 90.00},      # Source: IAU 2018 (J2000 celestial north)\n    'Moon': {'ra': 269.99, 'dec': 66.54},     # Source: IAU 2018 Table 2 mean pole (librates)\n    'Mars': {'ra': 317.68, 'dec': 52.89},\n    'Jupiter': {'ra': 268.05, 'dec': 64.49},\n    'Saturn': {'ra': 40.58, 'dec': 83.54},\n    'Uranus': {'ra': 257.43, 'dec': -15.10},\n    'Neptune': {'ra': 299.36, 'dec': 43.46},\n    'Pluto': {'ra': 132.99, 'dec': -6.16}\n}\n",
         "# Planet pole directions (ICRF right ascension and declination, degrees).\n# L-322 Stage D (2026-09-23): the dict moved to constants_new.py, which is\n# its citation home, and is imported here under the same name. Earth's\n# entry there is the frame's own axis, drawn only when the pole of the\n# scene's date cannot be fetched.\nfrom constants_new import planet_poles\n"),
        ('    _OBLIQUITY = np.radians(23.439291)  # IAU 2006 / J2000 mean obliquity of the ecliptic\n',
         '    # L-322 Stage D (2026-09-23): the angle Horizons builds its ecliptic of\n    # J2000 with, read from constants_new.py. It is the frame\'s angle, the\n    # IAU 1976 value, not Earth\'s tilt; the label "IAU 2006" that stood\n    # here named a standard whose value is 84381.406 arcseconds, not this.\n    _OBLIQUITY = np.radians(EARTH_OBLIQUITY_J2000_DEG)\n'),
    ]),
    ('solar_visualization_shells.py', 'ee4e6c0c763e4a32fdd1596a4ed29ec3', 'd2e5a75273f3c4d78f6a4d9be67a47e8', [
        ('    border to factory default red. Four sites size 6->8 visual bump.\n"""\n',
         '    border to factory default red. Four sites size 6->8 visual bump.\nSeptember 23, 2026 (Claude Opus 5.5, L-322 Stage D): one comment names\n    the pole dict\'s new home, constants_new.planet_poles. No code changed.\n"""\n'),
        ("    # Source: IAU 2018 solar pole, via idealized_orbits.planet_poles['Sun']\n",
         "    # Source: IAU 2018 solar pole, via constants_new.planet_poles['Sun']\n"),
    ]),
    ('planet_visualization_utilities.py', 'f9e44db71016137e8670f93b84dd8c5b', '6d9628f2211c3982a6288d7b5523d5b5', [
        ('_declared_count() does the formatting)\n\nRole: rendering\n',
         "_declared_count() does the formatting)\n\nModule updated: September 23, 2026 with Anthropic's Claude Opus 5.5 (L-322\nStage D: Earth's rotation period on the axis hover is the sidereal period\nrow in constants_new.py at its declared count, where it typed 23.93 h)\n\nRole: rendering\n"),
        ("    # L-322 Stage C2: the tilt's rate, printed beside it on the cone's hover.\n    EARTH_DIPOLE_TILT_RATE_DEG_PER_YEAR,\n",
         "    # L-322 Stage C2: the tilt's rate, printed beside it on the cone's hover.\n    EARTH_DIPOLE_TILT_RATE_DEG_PER_YEAR,\n    # L-322 Stage D: Earth's sidereal period, printed on the axis hover.\n    EARTH_SIDEREAL_ROTATION_PERIOD_H,\n"),
        ("    'Earth':   {'period_str': '23.93 h',\n",
         "    # L-322 Stage D: the period is the store's sidereal row at its declared\n    # count (seven figures), and says which turn it is. The tilt below is\n    # still typed; the pole-of-date patch replaces it with the tilt of the\n    # plot's date.\n    'Earth':   {'period_str': '%.*g h (one turn against the stars)' % (\n                    figures_of('EARTH_SIDEREAL_ROTATION_PERIOD_H'),\n                    EARTH_SIDEREAL_ROTATION_PERIOD_H),\n"),
    ]),
]


def content(raw):
    """LF-normalised bytes: line endings are not content."""
    return raw.replace(b"\r\n", b"\n")


def fingerprint(raw):
    return hashlib.md5(content(raw)).hexdigest()


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    if os.path.basename(here) == "documentation":
        print("ERROR: run this from the repository ROOT, not from "
              "documentation/. Move it up one level, run it, then move it "
              "back. NOTHING was written.")
        return 1
    if not os.path.exists(os.path.join(here, "constants_new.py")):
        print("ERROR: constants_new.py is not beside this script, so this "
              "is not the orrery root. NOTHING was written.")
        return 1

    planned = []
    problems = []
    notes = []
    for name, base_fp, want_fp, hunks in EDITS:
        path = os.path.join(here, name)
        if not os.path.exists(path):
            problems.append("%s: not found" % name)
            continue
        with open(path, "rb") as handle:
            raw = handle.read()
        is_crlf = b"\r\n" in raw
        body = content(raw)
        actual = hashlib.md5(body).hexdigest()
        if actual == want_fp:
            problems.append("%s: already carries this patch's result -- a "
                            "second run" % name)
            continue
        if actual != base_fp:
            problems.append("%s: BASE MOVED. Expected %s, found %s"
                            % (name, base_fp[:12], actual[:12]))
            continue
        if is_crlf:
            notes.append("%s: the working copy is CRLF; anchors matched "
                         "after normalising, and it is written back CRLF"
                         % name)
        text = body.decode("utf-8")
        before_non_ascii = sum(1 for ch in text if ord(ch) > 127)
        for index, (old, new) in enumerate(hunks, 1):
            found = text.count(old)
            if found != 1:
                problems.append("%s: ANCHOR FAIL, edit %d of %d matched %d "
                                "times" % (name, index, len(hunks), found))
                break
            if any(ord(ch) > 127 for ch in new):
                problems.append("%s: edit %d inserts a non-ASCII character"
                                % (name, index))
                break
            text = text.replace(old, new)
        else:
            after_non_ascii = sum(1 for ch in text if ord(ch) > 127)
            if before_non_ascii:
                notes.append("%s still holds %d non-ASCII byte(s) this patch "
                             "did not reach" % (name, before_non_ascii))
            if after_non_ascii > before_non_ascii:
                problems.append("%s: the result holds more non-ASCII bytes "
                                "than it started with" % name)
                continue
            out = text.encode("utf-8")
            if hashlib.md5(out).hexdigest() != want_fp:
                problems.append("%s: the result is not the file this patch "
                                "was built to produce" % name)
                continue
            planned.append((path, out.replace(b"\n", b"\r\n") if is_crlf
                            else out, name, len(hunks)))

    if problems:
        print("FAILURE -- NOTHING was written:")
        for line in problems:
            print("  " + line)
        print("")
        print("Undo is Discard Changes in GitHub Desktop.")
        return 1

    for path, data, name, count in planned:
        with open(path, "wb") as handle:
            handle.write(data)
        print("ok  %-36s %2d edit(s)" % (name, count))
    for line in notes:
        print("note: " + line)
    print("")
    print("patch applied (%d file(s), %d edit(s))"
          % (len(planned), sum(c for _p, _d, _n, c in planned)))
    print("")
    print("Stamps updated in the same transaction: the module docstring of "
          "every file above.")
    print("")
    print("DO THESE, IN THIS ORDER:")
    print("  1. Run the orrery maintenance run. It rewrites "
          "data/constants_export.json and the generated documents; a "
          "commit without them shows the run was skipped.")
    print("  2. See the run record for the checks this patch was tested "
          "against and what each should report.")
    print("  3. Commit and push. Do not start the next Stage D patch until "
          "the push is in; it is built on this commit.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
