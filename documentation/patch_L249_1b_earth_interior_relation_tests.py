"""
patch_L249_1b_earth_interior_relation_tests.py -- L-249, patch 1b of 3.

Gives the maintenance runner something to say about the Earth interior
constants that patch_L249_1 added. Before this patch the "Constants
relations" row imports constants_new.py and verifies nothing about
Earth's interior: its import list is hand-maintained and its tests are
written one per constant. It reports pass having looked at nothing.

Adds six relation tests, and NO pinned values. This file's own rule --
"It holds no copy of any measured value, so a legitimate correction never
makes it stale" -- is why the 55 literal pins were retired on 2026-08-12.
Every assertion here is structural: a derivation against its own factors,
an ordering, a bracket that follows from geometry rather than from a
measurement.

    test_earth_mean_radius_between_polar_and_equatorial
    test_earth_lower_mantle_derived_from_660_depth
    test_earth_interior_fractions_are_derived
    test_earth_interior_fractions_are_below_the_surface
    test_earth_interior_ordering
    test_earth_interior_km_ordering_matches_fractions

What each one can actually fail on is named in its docstring, because a
test whose failure mode is unstated is the next thing nobody notices has
stopped working.

The runner discovers tests by name (`_collect_tests` walks module-level
`test_*` functions), so there is no registration list to update.

RUN COMMAND (save this file into the same folder as
test_constants_provenance.py, open it in VS Code, click Run -- or from a
terminal in that folder):

    python patch_L249_1b_earth_interior_relation_tests.py

Success prints one `ok` line per edit then `patch applied (N bytes)`.
Any failure prints a single ERROR:/ANCHOR FAIL line and writes nothing.
One-shot: a second run aborts on the fingerprint and writes nothing.

RUN ORDER: after patch_L249_1 (which defines the constants imported
here), before patch_L249_2 (the shell wiring).

PERMANENT: the tests added to test_constants_provenance.py.
DISPOSABLE: this script. Archive it to documentation/ once it has run.
"""

import hashlib
import os
import sys

TARGET = 'test_constants_provenance.py'

# md5 of the LF-normalised base, orrery daf8c09c1a8cc8a8ea800f7e0fd86459a3aa5775
BASE_FP = 'b74548cc88c10aed8b1579d66b061213'

IMPORT_ANCHOR = b'''    # Dictionaries
    CENTER_BODY_RADII,
    KNOWN_ORBITAL_PERIODS,
)
'''

IMPORT_NEW = b'''    # Earth interior boundaries (L-249)
    EARTH_MEAN_RADIUS_KM,
    EARTH_INNER_CORE_KM,
    EARTH_INNER_CORE_RADII,
    EARTH_OUTER_CORE_KM,
    EARTH_OUTER_CORE_RADII,
    EARTH_D660_DEPTH_KM,
    EARTH_LOWER_MANTLE_KM,
    EARTH_LOWER_MANTLE_RADII,
    EARTH_UPPER_MANTLE_KM,
    EARTH_UPPER_MANTLE_RADII,
    # Dictionaries
    CENTER_BODY_RADII,
    KNOWN_ORBITAL_PERIODS,
)
'''

TESTS_ANCHOR = b'''# ============================================================
# Test runner
# ============================================================
'''

TESTS_NEW = b'''# ============================================================
# Section 10: Earth interior boundaries (L-249)
# ============================================================
# Earth's four interior boundaries live in constants_new.py as radii in
# km with their own sources; the shell fractions derive from them. These
# tests hold NO measured value. They check the shape of that arrangement,
# which is what breaks when somebody types a fraction back in as a
# literal -- the failure the single-store rule exists to prevent, and the
# one nothing watched before this section existed.
#
# Read the frame note in constants_new.py before changing any of these:
# the boundaries are sourced against a MEAN Earth of 6371.0 km and drawn
# against the equatorial radius, on purpose.

def test_earth_mean_radius_between_polar_and_equatorial():
    """The volumetric mean radius must lie between the two axes.

    Fails if EARTH_MEAN_RADIUS_KM is ever replaced by an equatorial or
    polar value, which is the plausible mistake -- the three constants
    sit within 0.2% of each other and read alike.
    """
    assert EARTH_POLAR_RADIUS_KM < EARTH_MEAN_RADIUS_KM < EARTH_EQUATORIAL_RADIUS_KM, \\
        (f"Earth mean radius ({EARTH_MEAN_RADIUS_KM}) is not between polar "
         f"({EARTH_POLAR_RADIUS_KM}) and equatorial ({EARTH_EQUATORIAL_RADIUS_KM})")


def test_earth_lower_mantle_derived_from_660_depth():
    """The lower mantle boundary must remain a subtraction, not a literal.

    Fails if EARTH_LOWER_MANTLE_KM is hardcoded to 5711, or if either
    factor moves without it following. It cannot fail on a corrected
    660 depth, which is the point -- a new depth propagates.
    """
    expected = EARTH_MEAN_RADIUS_KM - EARTH_D660_DEPTH_KM
    assert abs(EARTH_LOWER_MANTLE_KM - expected) < 1e-9, \\
        (f"EARTH_LOWER_MANTLE_KM ({EARTH_LOWER_MANTLE_KM}) != "
         f"EARTH_MEAN_RADIUS_KM - EARTH_D660_DEPTH_KM ({expected})")


def test_earth_interior_fractions_are_derived():
    """Each shell fraction must equal its own radius over the drawn radius.

    Fails the moment any of the four is replaced by a rounded literal --
    0.19151 instead of the expression. That substitution is invisible to
    the eye, changes the drawn radius by centimetres, and silently
    creates a second store of a value that lives in one place.
    """
    pairs = [
        ('EARTH_INNER_CORE', EARTH_INNER_CORE_KM, EARTH_INNER_CORE_RADII),
        ('EARTH_OUTER_CORE', EARTH_OUTER_CORE_KM, EARTH_OUTER_CORE_RADII),
        ('EARTH_LOWER_MANTLE', EARTH_LOWER_MANTLE_KM, EARTH_LOWER_MANTLE_RADII),
        ('EARTH_UPPER_MANTLE', EARTH_UPPER_MANTLE_KM, EARTH_UPPER_MANTLE_RADII),
    ]
    for name, km, fraction in pairs:
        expected = km / EARTH_EQUATORIAL_RADIUS_KM
        assert abs(fraction - expected) < 1e-15, \\
            (f"{name}_RADII ({fraction!r}) is not {name}_KM / "
             f"EARTH_EQUATORIAL_RADIUS_KM ({expected!r}) -- a literal has "
             f"replaced the derivation")
    assert len(pairs) == 4, "expected 4 interior boundaries, got %d" % len(pairs)


def test_earth_interior_fractions_are_below_the_surface():
    """Every interior fraction must be strictly inside the crust.

    Fails on a fraction at or above 1.0, which would draw an interior
    shell outside the body. Geometry, not measurement: no interior
    boundary can reach the surface however the sources are revised.
    """
    for name, fraction in [
            ('EARTH_INNER_CORE_RADII', EARTH_INNER_CORE_RADII),
            ('EARTH_OUTER_CORE_RADII', EARTH_OUTER_CORE_RADII),
            ('EARTH_LOWER_MANTLE_RADII', EARTH_LOWER_MANTLE_RADII),
            ('EARTH_UPPER_MANTLE_RADII', EARTH_UPPER_MANTLE_RADII)]:
        assert 0.0 < fraction < 1.0, \\
            f"{name} ({fraction}) is not strictly between 0 and the surface"


def test_earth_interior_ordering():
    """The four shells must nest, innermost outward.

    Fails if two boundaries are transposed -- the copy-paste error that
    a block of four near-identical definitions invites, and one the
    render would show only as a colour in the wrong place.
    """
    assert (EARTH_INNER_CORE_RADII < EARTH_OUTER_CORE_RADII
            < EARTH_LOWER_MANTLE_RADII < EARTH_UPPER_MANTLE_RADII), \\
        ("Earth interior shells are not in increasing order: "
         f"inner core {EARTH_INNER_CORE_RADII}, outer core "
         f"{EARTH_OUTER_CORE_RADII}, lower mantle {EARTH_LOWER_MANTLE_RADII}, "
         f"upper mantle {EARTH_UPPER_MANTLE_RADII}")


def test_earth_interior_km_ordering_matches_fractions():
    """The km values must nest in the same order as the fractions.

    Redundant only while every fraction derives from its own km value.
    It stops being redundant the moment one of them does not, which is
    exactly when the other tests here need a second opinion.
    """
    assert (EARTH_INNER_CORE_KM < EARTH_OUTER_CORE_KM
            < EARTH_LOWER_MANTLE_KM < EARTH_UPPER_MANTLE_KM
            < EARTH_EQUATORIAL_RADIUS_KM), \\
        ("Earth interior radii are not in increasing order: "
         f"{EARTH_INNER_CORE_KM}, {EARTH_OUTER_CORE_KM}, "
         f"{EARTH_LOWER_MANTLE_KM}, {EARTH_UPPER_MANTLE_KM} against a drawn "
         f"radius of {EARTH_EQUATORIAL_RADIUS_KM}")


# ============================================================
# Test runner
# ============================================================
'''

DOC_ANCHOR = b'Module created: April 17, 2026 with Anthropic\'s Claude Opus 4.7\n'

DOC_STAMP = (b'Module created: April 17, 2026 with Anthropic\'s Claude Opus 4.7\n'
             b'Module updated: August 26, 2026 with Anthropic\'s Claude Opus 5\n'
             b'(L-249: Section 10, six relation tests for Earth\'s interior\n'
             b'boundaries. No pinned values -- derivations against their own\n'
             b'factors, orderings, and geometric brackets, so a corrected source\n'
             b'never makes them stale)\n')


def fingerprint(data):
    return hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()


def main():
    if not os.path.exists(TARGET):
        print('ERROR: %s not found. Save this script into the same folder '
              'as %s and run it there.' % (TARGET, TARGET))
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
        ('import list', conv(IMPORT_ANCHOR), conv(IMPORT_NEW)),
        ('Section 10 tests', conv(TESTS_ANCHOR), conv(TESTS_NEW)),
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

    for raw in (IMPORT_NEW, TESTS_NEW, DOC_STAMP):
        try:
            raw.decode('ascii')
        except UnicodeDecodeError as exc:
            print('ERROR: non-ASCII byte in inserted text: %s' % exc)
            return 1
    print('ok   encoding gate -- inserted lines are ASCII')

    # Post-conditions, read back off the patched bytes.
    text = data.decode('ascii').replace('\r\n', '\n')

    names = ['test_earth_mean_radius_between_polar_and_equatorial',
             'test_earth_lower_mantle_derived_from_660_depth',
             'test_earth_interior_fractions_are_derived',
             'test_earth_interior_fractions_are_below_the_surface',
             'test_earth_interior_ordering',
             'test_earth_interior_km_ordering_matches_fractions']
    for name in names:
        if ('\ndef %s(' % name) not in text:
            print('ERROR: post-condition -- %s not defined.' % name)
            return 1
    print('ok   post-condition -- %d test functions defined' % len(names))

    if text.count('# Test runner') != 1:
        print('ERROR: post-condition -- the Test runner header is not unique '
              '(%d occurrences); the anchor was duplicated rather than moved.'
              % text.count('# Test runner'))
        return 1
    print('ok   post-condition -- Test runner header still unique')

    if text.index('EARTH_INNER_CORE_RADII,') > text.index('def test_'):
        print('ERROR: post-condition -- the new imports land after the first '
              'test definition.')
        return 1
    print('ok   post-condition -- imports precede the tests')

    with open(TARGET, 'wb') as f:
        f.write(data)
    print('patch applied (%d bytes)' % len(data))
    print('')
    print('Next: python test_constants_provenance.py  -- expect the existing')
    print('count plus 6. Then maintenance_run.py, then patch_L249_2.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
