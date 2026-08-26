"""
patch_L249_1_earth_interior_constants.py -- L-249, patch 1 of 2.

Adds Earth's four interior boundary radii to constants_new.py as sourced
primaries, each with a derived shell fraction beside it. Nothing renders
differently after this patch: it only creates the single store that
patch_L249_2 will make shell_configs.py and earth_visualization_shells.py
read from.

New names (10):
    EARTH_MEAN_RADIUS_KM       primary  NASA Earth Fact Sheet
    EARTH_INNER_CORE_KM        primary  PREM (Dziewonski & Anderson 1981)
    EARTH_INNER_CORE_RADII     derived
    EARTH_OUTER_CORE_KM        primary  PREM
    EARTH_OUTER_CORE_RADII     derived
    EARTH_D660_DEPTH_KM        primary  seismological global average
    EARTH_LOWER_MANTLE_KM      derived  mean radius - 660
    EARTH_LOWER_MANTLE_RADII   derived
    EARTH_UPPER_MANTLE_KM      primary  PREM reference Moho
    EARTH_UPPER_MANTLE_RADII   derived

RUN COMMAND (save this file into the same folder as constants_new.py,
open it in VS Code, click Run -- or from a terminal in that folder):

    python patch_L249_1_earth_interior_constants.py

Success prints one `ok` line per edit then `patch applied (N bytes)`.
Any failure prints a single ERROR:/ANCHOR FAIL line and writes nothing.
One-shot: a second run aborts on the fingerprint and writes nothing.

PERMANENT: the constants added to constants_new.py.
DISPOSABLE: this script. Archive it to documentation/ once it has run.
"""

import hashlib
import os
import sys

TARGET = 'constants_new.py'

# md5 of the LF-normalised base, orrery 4fd02ddb41d4971d54b67e438ea8c72c4fc27b27
BASE_FP = 'fa6e3957f415664e83b3da3423f94fd5'

NEW_BLOCK = b'''

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
# Note: a GLOBAL AVERAGE, not a constant depth. The boundary varies by
# Note+: up to about +/-60 km with mantle temperature and is depressed to
# Note+: roughly 750 km beneath cold subducting slabs. That +/-60 km is
# Note+: an order of magnitude larger than any other uncertainty in this
# Note+: stack and it governs how the lower mantle shell may be reported:
# Note+: the sphere is drawn at one radius because a sphere is what the
# Note+: renderer draws, and the hover says the boundary varies.
# Review-note: single leg (Claude, 2026-08-26). A second independent
# Review-note+: cross-check is owed before this row counts as confirmed.

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
# Derived+: the numerator. Report no more than that.'''

DOC_ANCHOR = (b'Review-note, and an UNMATCHED cross-check on '
              b'SGR_A_DISTANCE_PC removed)\n')

DOC_STAMP = (b'Review-note, and an UNMATCHED cross-check on '
             b'SGR_A_DISTANCE_PC removed)\n'
             b'Module updated: August 26, 2026 with Anthropic\'s Claude Opus 5\n'
             b'(L-249: Earth\'s four interior boundary radii added as sourced\n'
             b'primaries with derived shell fractions. Tony\'s ruling of the same\n'
             b'day -- the original radius fractions were approximate values taken\n'
             b'by hand, not declared drawing choices, so every one of them derives\n'
             b'from the sourced radius and constants_new.py is the only store.\n'
             b'Derived quotients are held at full float precision and REPORTED\n'
             b'to the significant figures their least precise input supports)\n')

INSERT_ANCHOR = b'\n\nJUPITER_EQUATORIAL_RADIUS_KM = 71492.0\n'


def fingerprint(data):
    return hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()


def main():
    if not os.path.exists(TARGET):
        print('ERROR: %s not found. Save this script into the same folder '
              'as constants_new.py and run it there.' % TARGET)
        return 1

    with open(TARGET, 'rb') as f:
        data = f.read()

    fp = fingerprint(data)
    if fp != BASE_FP:
        print('ERROR: BASE MOVED. %s fingerprints %s, expected %s.'
              % (TARGET, fp, BASE_FP))
        print('       Nothing written. If this patch already ran, that is '
              'the expected result of a second run.')
        return 1
    print('ok   base fingerprint %s (%d bytes, %s)'
          % (fp, len(data), 'CRLF' if b'\r\n' in data else 'LF'))

    is_crlf = data.count(b'\r\n') > 0

    def conv(b):
        return b.replace(b'\n', b'\r\n') if is_crlf else b

    edits = [
        ('docstring stamp', conv(DOC_ANCHOR), conv(DOC_STAMP)),
        ('interior block', conv(INSERT_ANCHOR),
         conv(NEW_BLOCK) + conv(INSERT_ANCHOR)),
    ]

    for label, old, new in edits:
        n = data.count(old)
        if n != 1:
            print('ANCHOR FAIL: %s -- expected 1 match, got %d: %r'
                  % (label, n, old[:60]))
            print('             Nothing written.')
            return 1
        data = data.replace(old, new, 1)
        print('ok   %s' % label)

    # Encoding gate: every inserted line must be ASCII.
    for raw in (NEW_BLOCK, DOC_STAMP):
        try:
            raw.decode('ascii')
        except UnicodeDecodeError as exc:
            print('ERROR: non-ASCII byte in inserted text: %s' % exc)
            return 1
    print('ok   encoding gate -- inserted lines are ASCII')

    # Post-conditions. Each of these can fail: they read the patched bytes
    # back, not the literals the patch was built from.
    text = data.decode('ascii').replace('\r\n', '\n')
    for name in ('EARTH_MEAN_RADIUS_KM', 'EARTH_INNER_CORE_KM',
                 'EARTH_INNER_CORE_RADII', 'EARTH_OUTER_CORE_KM',
                 'EARTH_OUTER_CORE_RADII', 'EARTH_D660_DEPTH_KM',
                 'EARTH_LOWER_MANTLE_KM', 'EARTH_LOWER_MANTLE_RADII',
                 'EARTH_UPPER_MANTLE_KM', 'EARTH_UPPER_MANTLE_RADII'):
        if ('\n%s = ' % name) not in text:
            print('ERROR: post-condition -- %s not defined at column 0.' % name)
            return 1
    print('ok   post-condition -- 10 new names defined')

    if text.index('EARTH_INNER_CORE_RADII') < text.index('EARTH_EQUATORIAL_RADIUS_KM'):
        print('ERROR: post-condition -- derived fractions precede their divisor.')
        return 1
    print('ok   post-condition -- divisor defined before the derivations')

    with open(TARGET, 'wb') as f:
        f.write(data)
    print('patch applied (%d bytes)' % len(data))
    print('')
    print('Next: run  python -c "import constants_new"  to confirm the module')
    print('still imports, then patch_L249_2 wires the shells to these names.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
