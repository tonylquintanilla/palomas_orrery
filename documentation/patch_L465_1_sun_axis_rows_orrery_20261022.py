"""
patch_L465_1_sun_axis_rows_orrery_20261022.py - the store rows the
website's new Sun rotation axis prints (L-465, Tony from his phone,
2026-10-22: "The sun's pole and rotational axis like the orrery?").

Built on b995472a40ba7766ea72ed4c18fe31124f1e17e5 at
https://github.com/tonylquintanilla/palomas_orrery (branch main) WITH
patch_L434_2_oort_edges_alfven_range_orrery_20261022.py applied. Run
that one first; this one refuses to run on files it did not expect.

WHAT IT DOES
    constants_new.py:
    - SUN_POLE_RA_J2000_DEG (286.13) and SUN_POLE_DEC_J2000_DEG (63.87),
      the Sun's pole as rows of their own, from NASA NAIF's pck00011,
      read this day. planet_poles['Sun'] now reads them; the numbers
      were typed there before.
    - SUN_ROTATION_RATE_DEG_PER_DAY (14.1844), the IAU's rate for the
      Sun, from the same file, with the IAU's rule for which way that
      turns (Archinal et al. 2019, Fig. 1), read this day.
    - DEG_PER_TURN (360), so the period divides a turn by a row.
    - Two worked-out rows the website prints:
      SUN_SIDEREAL_ROTATION_PERIOD_D, 25.3800 days, and
      SUN_EQUATOR_TILT_DEG, 7.25 degrees from the plane of Earth's orbit.
    constants_tokens.py: deg_per_day and days, the two new units.
    test_derived_figures.py and constants_change_report.py: both learn
    the inverse cosine (acos) and inverse sine, which the tilt is the
    first row to use. The unit check already knew them.
    palomas_orrery_dashboard.py: Label Words, the website check the
    waiting website patch L434_3 adds, gets its button; without it the
    Dashboard parity check fails once that patch runs. Two button texts
    say what their checks now do (Far Lines, Arrival).

HOW TO RUN
    Save into the palomas_orrery folder, open in VS Code, click Run.
    (python patch_L465_1_sun_axis_rows_orrery_20261022.py)
    Success: one "ok" line per file, then "patch applied".
    Failure: "ERROR:" or "ANCHOR FAIL", and NOTHING was written.
    Undo is Discard Changes in GitHub Desktop.

AFTER RUNNING
    Move this file to documentation/. Run the two website patches
    (L434_3, then L465_2) BEFORE the orrery maintenance run.
    In the maintenance run, expect ONE red row, Constants change, naming
    exactly two lines: the Sun's entry in planet_poles, old and new.
    That is right: its two numbers moved into the two rows above it,
    and the tool cannot follow numbers out of a dictionary. Anything
    else it names is a real finding. Everything else passes; the
    scanner's Tier-1 count does not move. Commit and PUSH.

Module written: October 22, 2026 with Anthropic's Claude Opus 5.5.

Role: devtool
Domain: dev_tools
"""

AFTER = 'Next: move this file to documentation/; run the website patches L434_3 and then L465_2; then the orrery maintenance run (expect Constants change red on the planet_poles Sun line only), commit and push.'
STAMPS = ['constants_new.py', 'constants_tokens.py', 'test_derived_figures.py', 'constants_change_report.py', 'palomas_orrery_dashboard.py']
FINGERPRINTS = {'constants_new.py': '901f6c2ecc11b3d9ef8a599ebc937385', 'constants_tokens.py': 'dd5ce7bc595c6ff29594bf9d2b44096d', 'test_derived_figures.py': '68269b9beb7fcc53e6475329a2deeaec', 'constants_change_report.py': '654f921a64e07a0cdafd9b5f6b0f485c', 'palomas_orrery_dashboard.py': '1617457472909df6d58d053995c1764a'}
EDITS = {'constants_new.py': [('\n(L-434: no value changed. GALACTIC_NORTH_POLE_RA_J2000_DEG\'s Declared\nnote names where the tide is now placed, galactic_tide_sampler.py.)\n"""\n\n', '\n(L-434: no value changed. GALACTIC_NORTH_POLE_RA_J2000_DEG\'s Declared\nnote names where the tide is now placed, galactic_tide_sampler.py.)\nModule updated: October 22, 2026 with Anthropic\'s Claude Opus 5.5\n(L-465, the Sun\'s rotation axis on the website: SUN_POLE_RA_J2000_DEG\nand SUN_POLE_DEC_J2000_DEG, the Sun\'s pole as rows of its own, which\nplanet_poles now reads; SUN_ROTATION_RATE_DEG_PER_DAY from NASA NAIF\'s\npck00011, read this day; DEG_PER_TURN; and two derived rows the website\nprints, SUN_SIDEREAL_ROTATION_PERIOD_D and SUN_EQUATOR_TILT_DEG.)\n"""\n\n'), ('\n# Note: drawn, never printed, so it carries no print count.\n\n# The pole directions of the bodies the orrery draws with an axis, as ICRF\n# right ascension and declination in degrees. Moved here from\n', '\n# Note: drawn, never printed, so it carries no print count.\n\n# The Sun\'s pole, as two rows of its own (L-465, 2026-10-22): the website\n# draws the Sun\'s rotation axis about it, and the Sun\'s equator\'s tilt,\n# SUN_EQUATOR_TILT_DEG, is worked out from it. Until this day the two\n# numbers were typed in planet_poles below, which now reads them.\n\nSUN_POLE_RA_J2000_DEG = 286.13\n# Unit: deg\n# Status: measured V_SOURCED 2026-10-22\n# Figures: 5 -- the kernel prints 286.13, to hundredths of a degree.\n# Read: the kernel\'s text at the address on the Source line, the line\n# Read+: "BODY10_POLE_RA = ( 286.13 0. 0. )" and the Sun section\'s note\n# Read+: "Values are unchanged in the 2015 IAU report.", 2026-10-22,\n# Read+: Claude Opus 5.5.\n# Source: NASA NAIF, planetary constants kernel pck00011.tpc,\n# Source+: https://naif.jpl.nasa.gov/pub/naif/generic_kernels/pck/pck00011.tpc\n# Source+: -- BODY10_POLE_RA = 286.13 degrees, the right ascension of the\n# Source+: Sun\'s north pole in the ICRF, with no change over time. The\n# Source+: kernel says the Sun\'s values are unchanged in the 2015 report of\n# Source+: the IAU Working Group on Cartographic Coordinates and Rotational\n# Source+: Elements (Archinal et al. 2018, Cel. Mech. Dyn. Astron. 130:22).\n# Ref: https://naif.jpl.nasa.gov/pub/naif/generic_kernels/pck/pck00011.tpc\n# Note: drawn, never printed, so the website prints no pole; the tilt it\n# Note+: prints is SUN_EQUATOR_TILT_DEG.\n\nSUN_POLE_DEC_J2000_DEG = 63.87\n# Unit: deg\n# Status: measured V_SOURCED 2026-10-22\n# Figures: 4 -- the kernel prints 63.87, to hundredths of a degree.\n# Read: as SUN_POLE_RA_J2000_DEG, the line "BODY10_POLE_DEC = ( 63.87 0.\n# Read+: 0. )", 2026-10-22, Claude Opus 5.5.\n# Source: NASA NAIF, planetary constants kernel pck00011.tpc,\n# Source+: https://naif.jpl.nasa.gov/pub/naif/generic_kernels/pck/pck00011.tpc\n# Source+: -- BODY10_POLE_DEC = 63.87 degrees, the declination of the Sun\'s\n# Source+: north pole in the ICRF, with no change over time; unchanged in\n# Source+: the IAU working group\'s 2015 report (Archinal et al. 2018).\n# Ref: https://naif.jpl.nasa.gov/pub/naif/generic_kernels/pck/pck00011.tpc\n\n# The pole directions of the bodies the orrery draws with an axis, as ICRF\n# right ascension and declination in degrees. Moved here from\n'), ("\n# Note+: Uranus and Neptune that was false, and it is removed.\nplanet_poles = {\n    'Sun': {'ra': 286.13, 'dec': 63.87},      # Source: IAU 2018 (Archinal et al.)\n    'Mercury': {'ra': 281.01, 'dec': 61.45},  # Source: IAU 2018 (MESSENGER-updated)\n    'Venus': {'ra': 272.76, 'dec': 67.16},    # Source: IAU 2018 (retrograde; pole is IAU-north)\n", "\n# Note+: Uranus and Neptune that was false, and it is removed.\nplanet_poles = {\n    'Sun': {'ra': SUN_POLE_RA_J2000_DEG, 'dec': SUN_POLE_DEC_J2000_DEG},  # the two rows above (L-465)\n    'Mercury': {'ra': 281.01, 'dec': 61.45},  # Source: IAU 2018 (MESSENGER-updated)\n    'Venus': {'ra': 272.76, 'dec': 67.16},    # Source: IAU 2018 (retrograde; pole is IAU-north)\n"), ('\n# Note+: unit check, so the tilt and its rate multiply by this row instead\n# Note+: (provenance-discipline 2.17, Rule 3).\n\nEARTH_IGRF13_G10_NT = -29404.8\n', '\n# Note+: unit check, so the tilt and its rate multiply by this row instead\n# Note+: (provenance-discipline 2.17, Rule 3).\n\n# --- The Sun\'s turning and the tilt of its equator (L-465, 2026-10-22) ----\n# The website\'s Sun room draws the Sun\'s rotation axis, as the orrery does,\n# and its hover prints the two numbers below. Both come from the IAU\'s\n# rotational elements for the Sun as NASA NAIF\'s kernel carries them: the\n# pole above (SUN_POLE_RA_J2000_DEG, SUN_POLE_DEC_J2000_DEG) and the rate\n# here. The orrery\'s own axis hover still types its Sun numbers in\n# planet_visualization_utilities.py, PLANET_ROTATION; that is L-465\'s Gap.\n\nDEG_PER_TURN = 360.0\n# Unit: deg\n# Status: declared 2026-10-22 -- an exact unit conversion, degrees in one\n# Status+: full turn. Belongs to no body\'s slice.\n# Figures: exact -- a definition, not a measurement.\n# Read: Table 6, sec. 5.1.1, NIST Guide to the SI (SP 811), chapter 5,\n# Read+: "Non-SI units accepted for use with the SI by the CIPM and this\n# Read+: Guide", the row "degree -- plane angle", 1 deg = (pi/180) rad,\n# Read+: at the address on the Source line, 2026-10-22, Claude Opus 5.5.\n# Source: NIST Special Publication 811, sec. 5.1.1, Table 6,\n# Source+: https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-5-units-outside-si\n# Source+: -- the degree is pi/180 radian, so a full turn, 2 pi radians,\n# Source+: is 360 degrees by definition.\n# Ref: https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-5-units-outside-si\n# Note: exists so the Sun\'s period below divides a turn by the rate\n# Note+: through a row and not a bare 360. Neither checker judges this row;\n# Note+: its unit is asserted here, as DEG_PER_RAD\'s is.\n\nSUN_ROTATION_RATE_DEG_PER_DAY = 14.1844\n# Unit: deg_per_day\n# Status: measured V_SOURCED 2026-10-22\n# Figures: 6 -- the kernel prints 14.18440. Its trailing zero is not\n# Figures+: counted: the kernel writes its rates to a fixed number of\n# Figures+: places, and nothing in it says the IAU\'s rate was measured to\n# Figures+: that place, so the row claims no more than the digits before it.\n# Read: the kernel\'s text at the address on the Source line, the line\n# Read+: "BODY10_PM = ( 84.176 14.18440 0. )", 2026-10-22, Claude Opus 5.5.\n# Read+: The sense: the correction to the IAU working group\'s 2015 report,\n# Read+: "Correction to: Report of the IAU Working Group on Cartographic\n# Read+: Coordinates and Rotational Elements: 2015", B. A. Archinal, C. H.\n# Read+: Acton, A. Conrad and others, its Fig. 1 caption at Springer\'s\n# Read+: page, the address on the Source line, 2026-10-22, Claude Opus 5.5.\n# Source: NASA NAIF, planetary constants kernel pck00011.tpc,\n# Source+: https://naif.jpl.nasa.gov/pub/naif/generic_kernels/pck/pck00011.tpc\n# Source+: -- BODY10_PM, the angle W of the Sun\'s prime meridian,\n# Source+: 84.176 + 14.18440 d degrees, d in days from J2000; the Sun\'s\n# Source+: values are unchanged in the IAU working group\'s 2015 report. The\n# Source+: sense of the turning: Archinal et al. (2019), Correction to:\n# Source+: Report of the IAU Working Group on Cartographic Coordinates and\n# Source+: Rotational Elements: 2015, Cel. Mech. Dyn. Astron. 131:61,\n# Source+: https://doi.org/10.1007/s10569-019-9925-1 -- Fig. 1 caption:\n# Source+: where W increases with time, the body\'s rotation is prograde.\n# Ref: https://naif.jpl.nasa.gov/pub/naif/generic_kernels/pck/pck00011.tpc\n# Ref: https://doi.org/10.1007/s10569-019-9925-1\n# Note: the IAU\'s rate for the Sun\'s map frame. The Sun is not solid and\n# Note+: does not turn at one rate; this is the rate the frame is defined\n# Note+: by. A sentence saying so waits for a source a visitor can open\n# Note+: (L-465).\n\nSUN_SIDEREAL_ROTATION_PERIOD_D = DEG_PER_TURN / SUN_ROTATION_RATE_DEG_PER_DAY\n# Derived: one full turn divided by the rate, 360 / 14.1844\n# Derived+: = 25.3800\n# Unit: days\n# Status: derived 2026-10-22 -- inherits DEG_PER_TURN,\n# Status+: SUN_ROTATION_RATE_DEG_PER_DAY\n# Figures: 6 -- set by SUN_ROTATION_RATE_DEG_PER_DAY (14.1844, 6)\n# Note: the SIDEREAL period, one turn measured against the stars. Printed\n# Note+: in the website\'s Sun room, on the rotation axis\'s hover.\n\nSUN_EQUATOR_TILT_DEG = math.acos(math.sin(SUN_POLE_DEC_J2000_DEG / DEG_PER_RAD) * math.cos(EARTH_OBLIQUITY_J2000_DEG / DEG_PER_RAD) - math.cos(SUN_POLE_DEC_J2000_DEG / DEG_PER_RAD) * math.sin(EARTH_OBLIQUITY_J2000_DEG / DEG_PER_RAD) * math.sin(SUN_POLE_RA_J2000_DEG / DEG_PER_RAD)) * DEG_PER_RAD\n# Derived: the angle between the Sun\'s pole and the pole of the drawing\'s\n# Derived+: ecliptic of J2000, which is the tilt of the Sun\'s equator from\n# Derived+: the plane of Earth\'s orbit. The ecliptic pole sits at right\n# Derived+: ascension 270 degrees and declination 90 degrees less the\n# Derived+: frame\'s obliquity, so the cosine of the angle is\n# Derived+: sin(dec) cos(eps) - cos(dec) sin(eps) sin(ra) = 7.25\n# Unit: deg\n# Status: derived 2026-10-22 -- inherits SUN_POLE_DEC_J2000_DEG,\n# Status+: EARTH_OBLIQUITY_J2000_DEG, SUN_POLE_RA_J2000_DEG, DEG_PER_RAD\n# Figures: 3 -- hundredths of a degree, the place of SUN_POLE_RA_J2000_DEG\n# Figures+: (286.13) and SUN_POLE_DEC_J2000_DEG (63.87). The tilt is an\n# Figures+: angle between two directions and moves degree for degree with\n# Figures+: the pole, so it keeps the pole\'s place; counting the pole\'s four\n# Figures+: figures would claim thousandths, a place finer than the pole is\n# Figures+: given to (provenance-discipline, Rule 3: a function that\n# Figures+: magnifies its input\'s uncertainty drops a figure, said here).\n# Note: printed in the website\'s Sun room, on the rotation axis\'s hover.\n\nEARTH_IGRF13_G10_NT = -29404.8\n')], 'constants_tokens.py': [('\n(L-410: j_per_k, kg, per_s, mean_molecular_weight and fan_shape_parameter,\nfor the corona\'s density model and the dust cloud\'s shape.)\n"""\n\n', '\n(L-410: j_per_k, kg, per_s, mean_molecular_weight and fan_shape_parameter,\nfor the corona\'s density model and the dust cloud\'s shape.)\nModule updated: October 22, 2026 with Anthropic\'s Claude Opus 5.5\n(L-465: deg_per_day and days, for the Sun\'s rotation rate and its\nsidereal period.)\n"""\n\n'), ('\n    # L-431 (2026-10-11): days per Julian year, the conversion an orbital\n    # period\'s years go through.\n    "d_per_yr": {\n        "dimension": "d / yr",\n', '\n    # L-431 (2026-10-11): days per Julian year, the conversion an orbital\n    # period\'s years go through.\n    # L-465 (2026-10-22): the Sun\'s rotation rate and its period.\n    "deg_per_day": {\n        "dimension": "deg / d",\n        "defining_constant": None,\n        "meaning": "degrees of angle per day",\n    },\n    "days": {\n        "dimension": "d",\n        "defining_constant": None,\n        "meaning": "days",\n    },\n    "d_per_yr": {\n        "dimension": "d / yr",\n')], 'test_derived_figures.py': [('\nfails inside a closed slice. Nine fixtures test both, and the check is\nshown failing on the real store before it is trusted.)\n"""\n\n', '\nfails inside a closed slice. Nine fixtures test both, and the check is\nshown failing on the real store before it is trusted.)\nModule updated: October 22, 2026 with Anthropic\'s Claude Opus 5.5\n(L-465: asin and acos join the functions a derived row may use, as\ntest_dimensions.py already allowed; SUN_EQUATOR_TILT_DEG is the first.)\n"""\n\n'), ('\n             "sqrt": math.sqrt, "sin": math.sin, "cos": math.cos,\n             "tan": math.tan, "atan": math.atan, "arctan": math.atan,\n             "radians": math.radians, "degrees": math.degrees,\n             "abs": abs, "fabs": abs, "cbrt": lambda x: math.copysign(\n', '\n             "sqrt": math.sqrt, "sin": math.sin, "cos": math.cos,\n             "tan": math.tan, "atan": math.atan, "arctan": math.atan,\n             # L-465 (2026-10-22): the inverse sine and cosine, which\n             # test_dimensions.py already knows; SUN_EQUATOR_TILT_DEG is\n             # the first row to use one.\n             "asin": math.asin, "arcsin": math.asin,\n             "acos": math.acos, "arccos": math.acos,\n             "radians": math.radians, "degrees": math.degrees,\n             "abs": abs, "fabs": abs, "cbrt": lambda x: math.copysign(\n')], 'constants_change_report.py': [('\n    in a derived line by name, so a row such as a circular orbit\'s\n    period, 2 pi sqrt(r^3 / GM), is understood instead of failing).\n"""\n\n', '\n    in a derived line by name, so a row such as a circular orbit\'s\n    period, 2 pi sqrt(r^3 / GM), is understood instead of failing).\nModule updated: October 22, 2026 with Anthropic\'s Claude Opus 5.5\n    (L-465: asin and acos join math\'s pure functions, so the Sun\'s\n    equator tilt, an angle worked out with acos, is understood).\n"""\n\n'), ("\n# math.pi, math.sqrt, math.atan and abs() in rows this tool announced as\n# not understood; the low-orbit periods were the next.\nMATH_PURE = ('pi', 'tau', 'e', 'sqrt', 'atan', 'atan2', 'sin', 'cos',\n             'tan', 'exp', 'log', 'log10', 'radians', 'degrees')\nBUILTIN_PURE = ('abs',)\n\n", "\n# math.pi, math.sqrt, math.atan and abs() in rows this tool announced as\n# not understood; the low-orbit periods were the next.\n# L-465 (2026-10-22): asin and acos too, as pure as the rest;\n# SUN_EQUATOR_TILT_DEG is the first row to use one.\nMATH_PURE = ('pi', 'tau', 'e', 'sqrt', 'atan', 'atan2', 'sin', 'cos',\n             'tan', 'asin', 'acos', 'exp', 'log', 'log10', 'radians',\n             'degrees')\nBUILTIN_PURE = ('abs',)\n\n")], 'palomas_orrery_dashboard.py': [('\nDrawer Order, with its short line, running through\ndocumentation/run_offline_check.py.\n"""\n\n', '\nDrawer Order, with its short line, running through\ndocumentation/run_offline_check.py.\nOctober 22, 2026 with Anthropic\'s Claude Opus 5.5 (L-468, L-465): Label\nWords, the website\'s new checker (gallery patch L434_3), gets its button\nafter Hover Budget, with its short line; the Far Lines text says what\nthat check holds since the same patch, and the Arrival text names the\nSun\'s rotation axis, a drawn guide that must carry no shell key.\n"""\n\n'), ('\n        "renderers, applies gallery/arrival.js with the real "\n        "data/objects_config.json, and compares what is drawn on "\n        "opening against its list; it also fails on any trace with no "\n        "shell key. It first makes itself fail on purpose four ways. "\n        "GATES the gallery runner. The check is Node, so this button "\n        "runs it through documentation/run_offline_check.py, which "\n', '\n        "renderers, applies gallery/arrival.js with the real "\n        "data/objects_config.json, and compares what is drawn on "\n        "opening against its list; it also fails on any shell trace with "\n        "no shell key, and on a drawn guide (the Sun\'s rotation axis) "\n        "that carries one. It first makes itself fail on purpose four ways. "\n        "GATES the gallery runner. The check is Node, so this button "\n        "runs it through documentation/run_offline_check.py, which "\n'), ('\n        "phone whenever the Sun room was zoomed in close. It works six "\n        "cases by hand, builds the Sun room from the served config and "\n        "names the lines it looks after, and checks every drawn point "\n        "lies inside the box. It breaks its own file three ways first, to "\n        "show it can fail. GATES the gallery runner. The check is Node, so "\n        "this button runs it through documentation/run_offline_check.py. "\n', '\n        "phone whenever the Sun room was zoomed in close. It works six "\n        "cases by hand, builds the Sun room from the served config and "\n        "names the lines it looks after, and checks every line that "\n        "reaches far past the view is cut to the box and every other line "\n        "is left as served. It breaks its own file three ways first, to "\n        "show it can fail. GATES the gallery runner. The check is Node, so "\n        "this button runs it through documentation/run_offline_check.py. "\n'), ('\n        True,\n        None,\n        True),\n        ("Page Framing",\n', '\n        True,\n        None,\n        True),\n        ("Label Words",\n        os.path.join("documentation", "run_offline_check.py"),\n        "Naming a shell in a room\'s drawer opens that shell\'s own words "\n        "(L-468). Builds the Sun and Earth rooms with the real renderers "\n        "and checks, for every shell row, that the marker the drawer "\n        "opens is the row\'s own: the corona\'s row had opened the streamer "\n        "belt\'s words, because the two are drawn as one feature. It "\n        "breaks its own pick first, to show it can fail. GATES the "\n        "gallery runner. The check is Node, so this button runs it "\n        "through documentation/run_offline_check.py. Runs from the "\n        "gallery repo ROOT.",\n        GALLERY_REPO_DIR,\n        True,\n        ["Label words"],\n        True),\n        ("Page Framing",\n'), ('\n     "Hover Budget"):\n        "Counts the lines in every room hover and names the ten longest.",\n    ("Gallery -- checks and data",\n     "Page Framing"):\n', '\n     "Hover Budget"):\n        "Counts the lines in every room hover and names the ten longest.",\n    ("Gallery -- checks and data",\n     "Label Words"):\n        "Checks naming a drawer row opens that shell\'s own words.",\n    ("Gallery -- checks and data",\n     "Page Framing"):\n')]}
NEW_FILES = {}

import hashlib
import os
import sys


def main():
    texts, crlf = {}, {}
    for path, want in FINGERPRINTS.items():
        try:
            with open(path, 'rb') as f:
                raw = f.read()
        except OSError as e:
            print('ERROR: cannot read %s (%s). Run from the folder this patch '
                  'names. NOTHING was written.' % (path, e))
            return 1
        crlf[path] = b'\r\n' in raw
        text = raw.replace(b'\r\n', b'\n').decode('utf-8')
        got = hashlib.md5(text.encode('utf-8')).hexdigest()
        if got != want:
            print('ERROR: %s is not the file this patch was built on '
                  '(fingerprint %s, expected %s). NOTHING was written.'
                  % (path, got, want))
            return 1
        texts[path] = text
    for path in NEW_FILES:
        if os.path.exists(path):
            print('ERROR: %s already exists; this patch creates it. NOTHING '
                  'was written.' % path)
            return 1
    out = {}
    for path, pairs in EDITS.items():
        t = texts[path]
        for i, (old, new) in enumerate(pairs):
            n = t.count(old)
            if n != 1:
                print('ANCHOR FAIL: %s edit %d matched %d times. NOTHING was '
                      'written.' % (path, i + 1, n))
                return 1
            t = t.replace(old, new)
        before = set(texts[path].split('\n'))
        bad = [x for x in t.split('\n')
               if x not in before and any(ord(c) > 127 for c in x)]
        if bad:
            print('ERROR: a line this patch inserts in %s is not ASCII. '
                  'NOTHING was written.' % path)
            return 1
        out[path] = t
    for path, t in NEW_FILES.items():
        if any(ord(c) > 127 for c in t):
            print('ERROR: %s is not ASCII. NOTHING was written.' % path)
            return 1
    for path, t in out.items():
        with open(path, 'wb') as f:
            f.write(t.encode('utf-8'))
        print('ok  %s: %d edit(s)' % (path, len(EDITS[path])))
        if crlf[path]:
            print('note: %s was CRLF in the working copy; written LF' % path)
    for path, t in NEW_FILES.items():
        folder = os.path.dirname(path)
        if folder:
            os.makedirs(folder, exist_ok=True)
        with open(path, 'wb') as f:
            f.write(t.encode('utf-8'))
        print('ok  %s: created' % path)
    for path in STAMPS:
        print('stamped (its own Module updated line): %s' % path)
    print(AFTER)
    print('patch applied')
    return 0


if __name__ == '__main__':
    sys.exit(main())
