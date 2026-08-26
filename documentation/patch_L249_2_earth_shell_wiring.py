r'''
patch_L249_2_earth_shell_wiring.py -- L-249, patch 2 of 2.

Makes constants_new.py the only store for Earth's four interior boundary
values, in the drawing AND in the prose, and moves Earth onto the
reference pattern that Saturn, Uranus, Neptune and the Sun already use.

TWO FILES, ALL OR NOTHING. Both are staged in memory and written only
after every edit and every post-condition passes.

WHAT CHANGES.

1. earth_visualization_shells.py -- the four `earth_*_info` strings stop
   typing their numbers and interpolate the constants instead. These are
   the CANONICAL form: `\n` line breaks, consumed by the Tk checkbox
   tooltip through celestial_objects.get_shell_tooltip_names() and
   globals(). `<br>` is derived at the Plotly boundary, never authored.

2. earth_visualization_shells.py -- the four `create_earth_*_shell`
   builders carry `radius_fraction` literals of their own. Those
   functions are imported at planet_visualization.py line 129 and CALLED
   NOWHERE; they are dead. The literals are wired to the constants
   anyway, because a number typed in dead code is still a second store
   and reads as authoritative to whoever finds it next. Whether the dead
   builders should exist at all is a separate question, not this patch's.

3. shell_configs.py -- the four Earth interior entries take their
   `radius_fraction` from the derived constants, and their `hover_text`
   and `tooltip` from the imported info strings via the reference
   pattern:

       'hover_text': earth_inner_core_info.replace('\n', '<br>'),
       'tooltip': earth_inner_core_info,

   This deletes Earth's inline prose duplication, which is Earth's slice
   of L-191, and it means the hover cannot wrap badly: every source line
   already ends in `\n`, so every rendered line gets its `<br>`.

WHAT THE SHELLS DO ON SCREEN. Three of the four move, and one moves a
lot. Against a drawn radius of 6,378.1366 km:

    inner core     1,211.8 -> 1,221.5 km      +9.7
    outer core     3,508.0 -> 3,480.0 km     -28.0
    lower mantle   5,421.4 -> 5,711.0 km    +289.6
    upper mantle   6,250.6 -> 6,346.6 km     +96.0

The crust is untouched: it draws at the surface by definition, and its
hover quotes no boundary that moved.

WHAT IS NOT IN THIS PATCH. The upper mantle and crust info markers land
0.49% apart once the upper mantle moves, which is inside the 10% trigger
in orrery-coding-conventions. The angular separation is patch 3.

RUN COMMAND (save this file into the repo root -- the same folder as
earth_visualization_shells.py and shell_configs.py -- open it in VS Code
and click Run, or from a terminal in that folder):

    python patch_L249_2_earth_shell_wiring.py

Success prints one `ok` line per edit then `patch applied`. Any failure
prints a single ERROR:/ANCHOR FAIL line and writes nothing to either file.
One-shot: a second run aborts on the fingerprint.

RUN ORDER: after patch_L249_1, patch_L249_1b and patch_L253_1.
Afterwards: python test_constants_provenance.py, then maintenance_run.py,
then open the orrery and look at Earth (Mode 5).

PERMANENT: the edits to both files.
DISPOSABLE: this script. Archive it to documentation/ once it has run.
'''

import hashlib
import os
import sys

SHELLS = 'earth_visualization_shells.py'
CONFIGS = 'shell_configs.py'

# md5 of the LF-normalised bases, orrery c0555c55a76595b7c856acee7a2bbeee5610cbf2
BASE_FP = {
    SHELLS: 'cdcf259c7417d753fc4c5a2e2bb04cde',
    CONFIGS: '2634d334672e13ca74039297db8d3e80',
}


def b(text):
    """Raw text -> ASCII bytes. Backslash-n in the source stays literal."""
    return text.encode('ascii')


# ------------------------------------------------------------------
# earth_visualization_shells.py
# ------------------------------------------------------------------

SHELLS_IMPORT_OLD = b(
    r"from constants_new import KM_PER_AU  # L-178: direct km<->AU conversion, no shadow constant")

SHELLS_IMPORT_NEW = b(r'''from constants_new import (
    KM_PER_AU,  # L-178: direct km<->AU conversion, no shadow constant
    # L-249: Earth's interior boundaries have exactly one home. The _KM
    # values below are quoted in the info strings; the _RADII draw the
    # dead builders further down. Neither is ever retyped as a literal.
    EARTH_MEAN_RADIUS_KM,
    EARTH_INNER_CORE_KM, EARTH_INNER_CORE_RADII,
    EARTH_OUTER_CORE_KM, EARTH_OUTER_CORE_RADII,
    EARTH_D660_DEPTH_KM, EARTH_LOWER_MANTLE_RADII,
    EARTH_UPPER_MANTLE_KM, EARTH_UPPER_MANTLE_RADII,
)''')

INNER_INFO_OLD = b(r'''            "complex dynamics in Earth's magnetic field. The inner core is approximately\n"
            "1,220 km (760 miles) in radius."''')

INNER_INFO_NEW = b(r'''            "complex dynamics in Earth's magnetic field. The inner core is\n"
            f"{EARTH_INNER_CORE_KM:,.1f} km in radius."''')

OUTER_INFO_OLD = b(
    r'''            "1,220 to 3,500 km from Earth's center and has temperatures ranging from\n"''')

OUTER_INFO_NEW = b(
    r'''            f"{EARTH_INNER_CORE_KM:,.1f} to {EARTH_OUTER_CORE_KM:,.0f} km from Earth's center and has temperatures ranging from\n"''')

LOWER_INFO_OLD = b(
    r'''            "This region extends from 660 to 2,900 km below Earth's surface and experiences\n"''')

LOWER_INFO_NEW = b(
    r'''            f"This region extends from {EARTH_D660_DEPTH_KM:,.0f} to "
            f"{EARTH_MEAN_RADIUS_KM - EARTH_OUTER_CORE_KM:,.0f} km below Earth's surface and experiences\n"''')

UPPER_INFO_OLD = b(r'''            "allowing tectonic plates to move. It extends from about 30 to 660 km below\n"
            "the surface, with temperatures from 500 degC to 2,200 degC (900 degF to 4,000 degF)."''')

UPPER_INFO_NEW = b(r'''            "allowing tectonic plates to move. It reaches from the base of the crust,\n"
            f"{EARTH_MEAN_RADIUS_KM - EARTH_UPPER_MANTLE_KM:,.1f} km below the surface in the reference model, down to\n"
            f"{EARTH_D660_DEPTH_KM:,.0f} km, with temperatures from 500 degC to 2,200 degC\n"
            "(900 degF to 4,000 degF)."''')

DEAD_BUILDERS = [
    ("inner core builder",
     r"        'radius_fraction': 0.19,  # Inner core: 0-19% of Earth's radius",
     r"        'radius_fraction': EARTH_INNER_CORE_RADII,  # L-249: derived, not typed"),
    ("outer core builder",
     r"        'radius_fraction': 0.55,  # Outer core: 19-55% of Earth's radius",
     r"        'radius_fraction': EARTH_OUTER_CORE_RADII,  # L-249: derived, not typed"),
    ("lower mantle builder",
     r"        'radius_fraction': 0.85,  # Lower mantle: 55-85% of Earth's radius",
     r"        'radius_fraction': EARTH_LOWER_MANTLE_RADII,  # L-249: derived, not typed"),
    ("upper mantle builder",
     r"        'radius_fraction': 0.98,  # Upper mantle: 85-98% of Earth's radius",
     r"        'radius_fraction': EARTH_UPPER_MANTLE_RADII,  # L-249: derived, not typed"),
]


# The dead builders each hold a THIRD copy of the prose, in <br> form, in
# their layer_info 'description'. The post-condition below found these:
# they were not in the first draft of this patch. Same reference pattern.
DEAD_DESCRIPTIONS = [
    ("inner core builder description", 'earth_inner_core_info', r"""'description': (
            "Earth's inner core is a solid sphere composed primarily of iron and nickel.<br>"
            "Despite incredible pressure, temperatures of 5,400 degC (9,800 degF) keep it nearly<br>"
            "at melting point. It rotates slightly faster than the rest of Earth, creating<br>"
            "complex dynamics in Earth's magnetic field. The inner core is approximately<br>"
            "1,220 km (760 miles) in radius."
        )"""),
    ("outer core builder description", 'earth_outer_core_info', r"""'description': (
            "The outer core is a liquid layer of iron, nickel, and lighter elements.<br>"
            "Convection currents in this highly conductive fluid generate Earth's<br>"
            "magnetic field through a process called the geodynamo. It extends from<br>"
            "1,220 to 3,500 km from Earth's center and has temperatures ranging from<br>"
            "4,500 degC (8,100 degF) to 5,400 degC (9,800 degF)."
        )"""),
    ("lower mantle builder description", 'earth_lower_mantle_info', r"""'description': (
            "The lower mantle is composed of solid silicate rocks rich in iron and magnesium.<br>"
            "Despite being solid, it flows very slowly through convection, driving plate tectonics.<br>"
            "This region extends from 660 to 2,900 km below Earth's surface and experiences<br>"
            "temperatures from 2,200 degC to 4,500 degC (4,000 degF to 8,100 degF) and extreme pressure."
        )"""),
    ("upper mantle builder description", 'earth_upper_mantle_info', r"""'description': (
            "The upper mantle includes the asthenosphere, a partially molten layer where<br>"
            "most magma originates. This region flows more readily than the lower mantle,<br>"
            "allowing tectonic plates to move. It extends from about 30 to 660 km below<br>"
            "the surface, with temperatures from 500 degC to 2,200 degC (900 degF to 4,000 degF)."
        )"""),
]

SHELLS_DOC_OLD = b(r'''    already factory-routed in this file (magnetosphere, bow shock,
    Van Allen loop, LEO, GEO) were untouched -- they already use the
    factory default (red border) and Tony's earlier Mode 5 testing
    marked them acceptable.
"""''')

SHELLS_DOC_NEW = b(r'''    already factory-routed in this file (magnetosphere, bow shock,
    Van Allen loop, LEO, GEO) were untouched -- they already use the
    factory default (red border) and Tony's earlier Mode 5 testing
    marked them acceptable.
August 26, 2026 (L-249, Opus 5): the four interior info strings stop
    typing their boundary figures and interpolate constants_new.py
    instead, and the four dead create_earth_*_shell builders take their
    radius_fraction from the same constants. Tony's ruling that day:
    constants_new.py is the only store for a numeric value, in prose as
    much as in code, and a literal in dead code is still a store.
"""''')

# ------------------------------------------------------------------
# shell_configs.py
# ------------------------------------------------------------------

CONFIGS_IMPORT_OLD = b(r'''# Phase D1: Import Sun radius constants for radius_au expressions.
from planet_visualization_utilities import (''')

CONFIGS_IMPORT_NEW = b(r'''# L-249: Earth joins the reference pattern. The four interior boundary
# fractions derive from constants_new.py, and the prose comes from the
# body module rather than being retyped here -- same shape Saturn,
# Uranus, Neptune and the Sun already use above.
from constants_new import (
    EARTH_INNER_CORE_RADII, EARTH_OUTER_CORE_RADII,
    EARTH_LOWER_MANTLE_RADII, EARTH_UPPER_MANTLE_RADII,
)
from earth_visualization_shells import (
    earth_inner_core_info, earth_outer_core_info,
    earth_lower_mantle_info, earth_upper_mantle_info,
)

# Phase D1: Import Sun radius constants for radius_au expressions.
from planet_visualization_utilities import (''')

CONFIG_SHELLS = [
    ("Earth inner_core fraction",
     r"""            'name': 'Inner Core',
            'radius_fraction': 0.19,""",
     r"""            'name': 'Inner Core',
            'radius_fraction': EARTH_INNER_CORE_RADII,"""),
    ("Earth outer_core fraction",
     r"""            'name': 'Outer Core',
            'radius_fraction': 0.55,""",
     r"""            'name': 'Outer Core',
            'radius_fraction': EARTH_OUTER_CORE_RADII,"""),
    ("Earth lower_mantle fraction",
     r"""            'name': 'Lower Mantle',
            'radius_fraction': 0.85,""",
     r"""            'name': 'Lower Mantle',
            'radius_fraction': EARTH_LOWER_MANTLE_RADII,"""),
    ("Earth upper_mantle fraction",
     r"""            'name': 'Upper Mantle',
            'radius_fraction': 0.98,""",
     r"""            'name': 'Upper Mantle',
            'radius_fraction': EARTH_UPPER_MANTLE_RADII,"""),
]

CONFIG_PROSE = [
    ("Earth inner_core prose", 'earth_inner_core_info', r'''            'hover_text': (
                "Earth's inner core is a solid sphere composed primarily of iron and nickel.<br>"
                "Despite incredible pressure, temperatures of 5,400 degC (9,800 degF) keep it nearly<br>"
                "at melting point. It rotates slightly faster than the rest of Earth, creating<br>"
                "complex dynamics in Earth's magnetic field. The inner core is approximately<br>"
                "1,220 km (760 miles) in radius."
            ),
            'tooltip': (
                "Earth's inner core is a solid sphere composed primarily of iron and nickel.\n"
                "Despite incredible pressure, temperatures of 5,400 degC (9,800 degF) keep it nearly\n"
                "at melting point. It rotates slightly faster than the rest of Earth, creating\n"
                "complex dynamics in Earth's magnetic field. The inner core is approximately\n"
                "1,220 km (760 miles) in radius."
            ),'''),
    ("Earth outer_core prose", 'earth_outer_core_info', r'''            'hover_text': (
                "The outer core is a liquid layer of iron, nickel, and lighter elements.<br>"
                "Convection currents in this highly conductive fluid generate Earth's<br>"
                "magnetic field through a process called the geodynamo. It extends from<br>"
                "1,220 to 3,500 km from Earth's center and has temperatures ranging from<br>"
                "4,500 degC (8,100 degF) to 5,400 degC (9,800 degF)."
            ),
            'tooltip': (
                "The outer core is a liquid layer of iron, nickel, and lighter elements.\n"
                "Convection currents in this highly conductive fluid generate Earth's\n"
                "magnetic field through a process called the geodynamo. It extends from\n"
                "1,220 to 3,500 km from Earth's center and has temperatures ranging from\n"
                "4,500 degC (8,100 degF) to 5,400 degC (9,800 degF)."
            ),'''),
    ("Earth lower_mantle prose", 'earth_lower_mantle_info', r'''            'hover_text': (
                "The lower mantle is composed of solid silicate rocks rich in iron and magnesium.<br>"
                "Despite being solid, it flows very slowly through convection, driving plate tectonics.<br>"
                "This region extends from 660 to 2,900 km below Earth's surface and experiences<br>"
                "temperatures from 2,200 degC to 4,500 degC (4,000 degF to 8,100 degF) and extreme pressure."
            ),
            'tooltip': (
                "The lower mantle is composed of solid silicate rocks rich in iron and magnesium.\n"
                "Despite being solid, it flows very slowly through convection, driving plate tectonics.\n"
                "This region extends from 660 to 2,900 km below Earth's surface and experiences\n"
                "temperatures from 2,200 degC to 4,500 degC (4,000 degF to 8,100 degF) and extreme pressure."
            ),'''),
    ("Earth upper_mantle prose", 'earth_upper_mantle_info', r'''            'hover_text': (
                "The upper mantle includes the asthenosphere, a partially molten layer where<br>"
                "most magma originates. This region flows more readily than the lower mantle,<br>"
                "allowing tectonic plates to move. It extends from about 30 to 660 km below<br>"
                "the surface, with temperatures from 500 degC to 2,200 degC (900 degF to 4,000 degF)."
            ),
            'tooltip': (
                "The upper mantle includes the asthenosphere, a partially molten layer where\n"
                "most magma originates. This region flows more readily than the lower mantle,\n"
                "allowing tectonic plates to move. It extends from about 30 to 660 km below\n"
                "the surface, with temperatures from 500 degC to 2,200 degC (900 degF to 4,000 degF)."
            ),'''),
]

CONFIGS_DOC_OLD = b(r'''Module updated: May 2026 with Anthropic's Claude Opus 4.6
"""''')

CONFIGS_DOC_NEW = b(r'''Module updated: May 2026 with Anthropic's Claude Opus 4.6
Module updated: August 26, 2026 with Anthropic's Claude Opus 5 (L-249:
    Earth's four interior entries join the Phase C4 reference pattern.
    radius_fraction derives from constants_new.py; hover_text and
    tooltip come from earth_visualization_shells.py rather than being
    retyped here. Earth's slice of L-191 closes with it. The crust is
    deliberately untouched -- it draws at the surface by definition and
    its hover carries a toggle-off note the body module's string does
    not have.)
"""''')


def fingerprint(data):
    return hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()


def load(name):
    if not os.path.exists(name):
        print('ERROR: %s not found. Save this script into the repo root, '
              'beside %s and %s.' % (name, SHELLS, CONFIGS))
        return (None, None)
    with open(name, 'rb') as handle:
        data = handle.read()
    fp = fingerprint(data)
    if fp != BASE_FP[name]:
        print('ERROR: BASE MOVED. %s fingerprints %s, expected %s.'
              % (name, fp, BASE_FP[name]))
        print('       Nothing written to either file. If this patch already '
              'ran, that is the expected result of a second run.')
        return (None, None)
    is_crlf = data.count(b'\r\n') > 0
    print('ok   base fingerprint %s (%s, %d bytes, %s)'
          % (fp, name, len(data), 'CRLF' if is_crlf else 'LF'))
    return (data, is_crlf)


def apply_edits(data, is_crlf, edits):
    for label, old, new in edits:
        if is_crlf:
            old = old.replace(b'\n', b'\r\n')
            new = new.replace(b'\n', b'\r\n')
        count = data.count(old)
        if count != 1:
            print('ANCHOR FAIL: %s -- expected 1 match, got %d: %r'
                  % (label, count, old[:70]))
            print('             Nothing written to either file.')
            return None
        data = data.replace(old, new, 1)
        print('ok   %s' % label)
    return data


def main():
    shells, s_crlf = load(SHELLS)
    if shells is None:
        return 1
    configs, c_crlf = load(CONFIGS)
    if configs is None:
        return 1

    shell_edits = [
        ('shells docstring stamp', SHELLS_DOC_OLD, SHELLS_DOC_NEW),
        ('shells constants import', SHELLS_IMPORT_OLD, SHELLS_IMPORT_NEW),
        ('inner core info', INNER_INFO_OLD, INNER_INFO_NEW),
        ('outer core info', OUTER_INFO_OLD, OUTER_INFO_NEW),
        ('lower mantle info', LOWER_INFO_OLD, LOWER_INFO_NEW),
        ('upper mantle info', UPPER_INFO_OLD, UPPER_INFO_NEW),
    ]
    shell_edits += [(label, b(old), b(new)) for label, old, new in DEAD_BUILDERS]
    for label, name, old in DEAD_DESCRIPTIONS:
        new = "'description': %s.replace('\\n', '<br>')" % name
        shell_edits.append((label, b(old), b(new)))
    shells = apply_edits(shells, s_crlf, shell_edits)
    if shells is None:
        return 1

    config_edits = [
        ('configs docstring stamp', CONFIGS_DOC_OLD, CONFIGS_DOC_NEW),
        ('configs imports', CONFIGS_IMPORT_OLD, CONFIGS_IMPORT_NEW),
    ]
    config_edits += [(label, b(old), b(new)) for label, old, new in CONFIG_SHELLS]
    for label, name, old in CONFIG_PROSE:
        new = ("            'hover_text': %s.replace('\\n', '<br>'),\n"
               "            'tooltip': %s," % (name, name))
        config_edits.append((label, b(old), b(new)))
    configs = apply_edits(configs, c_crlf, config_edits)
    if configs is None:
        return 1

    for raw in (SHELLS_IMPORT_NEW, CONFIGS_IMPORT_NEW,
                SHELLS_DOC_NEW, CONFIGS_DOC_NEW):
        try:
            raw.decode('ascii')
        except UnicodeDecodeError as exc:
            print('ERROR: non-ASCII byte in inserted text: %s' % exc)
            return 1
    print('ok   encoding gate -- inserted lines are ASCII')

    s_text = shells.decode('ascii').replace('\r\n', '\n')
    c_text = configs.decode('ascii').replace('\r\n', '\n')

    # No boundary figure may survive as a literal in either file's Earth
    # interior region. '660' is deliberately NOT checked: it is the name of
    # the discontinuity and appears in prose that is not a value.
    # The Earth block's end must be found FROM its start. A bare
    # c_text.index("'crust': {") returns Mercury's, which is earlier in the
    # file, and the slice comes out empty -- a region check that examines
    # nothing and reports pass. That is how the first draft of this patch
    # got a green light on a file it had not looked at.
    earth_start = c_text.index("    'Earth': {")
    earth_end = c_text.index("'crust': {", earth_start)
    if earth_end <= earth_start:
        print('ERROR: post-condition -- Earth block slice is empty; the '
              'region check would examine nothing.')
        return 1
    for name, text, region in (
            (SHELLS, s_text, s_text[:s_text.index('earth_crust_info')]),
            (CONFIGS, c_text, c_text[earth_start:earth_end])):
        for stale in ('1,220', '3,500', '2,900', '0.19,', '0.55,', '0.85,',
                      '0.98,'):
            if stale in region:
                print('ERROR: post-condition -- %r survives in %s.'
                      % (stale, name))
                return 1
    print('ok   post-condition -- no boundary literal survives in either file')

    # Every Earth interior entry must be on the reference pattern.
    earth = c_text[earth_start:earth_end]
    print('ok   post-condition -- Earth block located, %d chars examined'
          % len(earth))
    for name in ('earth_inner_core_info', 'earth_outer_core_info',
                 'earth_lower_mantle_info', 'earth_upper_mantle_info'):
        if ("'hover_text': %s.replace" % name) not in earth:
            print('ERROR: post-condition -- %s is not on the reference '
                  'pattern.' % name)
            return 1
        if ("'tooltip': %s," % name) not in earth:
            print('ERROR: post-condition -- %s has no tooltip entry.' % name)
            return 1
    print('ok   post-condition -- four Earth entries on the reference pattern')

    # The info strings must actually be f-strings now, or they interpolate
    # nothing and quietly print their own braces.
    for marker in ('f"{EARTH_INNER_CORE_KM:,.1f} km in radius."',
                   'f"{EARTH_INNER_CORE_KM:,.1f} to {EARTH_OUTER_CORE_KM:,.0f}',
                   'f"This region extends from {EARTH_D660_DEPTH_KM:,.0f} to "',
                   'f"{EARTH_MEAN_RADIUS_KM - EARTH_UPPER_MANTLE_KM:,.1f} km below'):
        if marker not in s_text:
            print('ERROR: post-condition -- interpolation missing: %s' % marker)
            return 1
    print('ok   post-condition -- all four info strings interpolate')

    with open(SHELLS, 'wb') as handle:
        handle.write(shells)
    with open(CONFIGS, 'wb') as handle:
        handle.write(configs)
    print('patch applied (%s %d bytes, %s %d bytes)'
          % (SHELLS, len(shells), CONFIGS, len(configs)))
    print('')
    print('Next: python test_constants_provenance.py, then maintenance_run.py,')
    print('then open the orrery and look at Earth. Three shells move; the')
    print('lower mantle moves 290 km outward and should be visible.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
