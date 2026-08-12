"""Retire the pinned literals in test_constants_provenance.py.

RUN COMMAND
-----------
Save this file into the palomas_orrery repo ROOT, open it in VS Code, and
click Run.

    python patch_retire_constant_pins.py

Requires constants_change_report.py to be in the repo root already, since
this removes the check it replaces. The patch refuses otherwise.

WHAT IT DOES
------------
Removes 55 test functions from test_constants_provenance.py -- every test
whose assertion compares a constant to a hand-typed number. The file
discovers its tests with _collect_tests() rather than listing them, so
removing the function is the whole edit. Rewrites the module docstring to say what the
file is now. Adds constants_change_report.py to maintenance_run.py as a
checker.

18 tests remain, and they are a different kind: derivations
(SOLAR_RADIUS_AU must equal SUN_RADIUS_KM / KM_PER_AU), orderings (the
solar shells ascend, Earth's polar radius is under its equatorial),
cross-consistency (CENTER_BODY_RADII agrees with the named constants),
and completeness. None of them holds a copy of a measured value, so none
of them goes stale when a value is legitimately corrected.

WHY
---
Tony's ruling, 2026-08-12: "I don't think we should do is create a second
dictionary. Can we create a diff that would alert us to drift or
intentional revision?"

Those 55 pins WERE a second dictionary. Each held its own copy of a number
that also lives in constants_new.py, so every legitimate correction
required a synchronized hand-edit in two files with nothing enforcing it.
On 2026-08-02 a cross-check batch corrected six constants and updated zero
pins. The tests then failed correctly for ten days, describing sourced
values as "drifted," while the file that was actually stale was the test.

Worse, the pins carried citations of their own, unaudited: the scanner
extracts claims only from narrative-role files and this one is
Role: devtool, so nothing has ever checked them. test_chromosphere_radii
attributed "~1.5 R_sun" to Carroll & Ostlie Ch. 11 -- the same chapter the
August check read as ~2000 km, about 1.003 R_sun. A false citation in an
unaudited file is the failure this project treats as worse than no
citation at all.

WHAT REPLACES THEM
------------------
constants_change_report.py, which stores no numbers. It asks git what
changed in constants_new.py since the last commit and reads both the old
and new value out of the diff. A correction moves the number and its
comment block together; corruption moves the number alone, and the report
says which happened. It also covers constants that do not exist yet: a
value added next month is reported the first time it moves, with nobody
writing a test.

Still to come, and NOT part of this patch: the worksheet checker, which
opens the .md a `# Cross-checked:` annotation names and confirms it states
the value. That is the check that reaches committed history, which the
diff reader cannot see.

SAFETY
------
- Transactional. Base fingerprints verified first; every removal counted;
  the result is re-parsed and the surviving test count asserted BEFORE
  anything is written. Any mismatch writes nothing to either file.
- Functions are removed bottom-up so earlier line numbers stay valid.
- Binary-mode I/O; each file's own line endings preserved.

WHAT SUCCESS LOOKS LIKE
-----------------------
`removed 55 pinned tests`, `18 tests remain`, two `ok` lines for
maintenance_run.py, then `patch applied`.

AFTER RUNNING
-------------
    python test_constants_provenance.py   -- expect 18 passed, 0 failed
    python maintenance_run.py             -- expect all checkers green
Then commit.
"""

import ast
import hashlib
import os
import sys

TESTS_FILE = 'test_constants_provenance.py'
RUNNER = 'maintenance_run.py'
REQUIRED = 'constants_change_report.py'

BASE_MD5 = {
    TESTS_FILE: '324cb86fdfb4579f1585ab2793e6111a',
    RUNNER: 'eb9b9b728184f7827a886991f462dcb2',
}

EXPECTED_REMOVED = 55
EXPECTED_REMAINING = 18

# Every test whose assertion compares a constant to a hand-typed number.
RETIRE = [
    'test_km_per_au',
    'test_sun_radius_km',
    'test_earth_equatorial_radius_km',
    'test_earth_polar_radius_km',
    'test_jupiter_equatorial_radius_km',
    'test_jupiter_polar_radius_km',
    'test_speed_of_light_km_s',
    'test_chromosphere_radii',
    'test_inner_corona_radii',
    'test_outer_corona_radii',
    'test_streamer_belt_radii',
    'test_roche_limit_radii',
    'test_alfven_surface_radii',
    'test_termination_shock_au',
    'test_heliopause_radii',
    'test_heliopause_conversion_sanity',
    'test_inner_limit_oort_cloud_au',
    'test_inner_oort_cloud_au',
    'test_outer_oort_cloud_au',
    'test_gravitational_influence_au',
    'test_parker_closest_radii',
    'test_center_body_radii_mercury',
    'test_center_body_radii_venus',
    'test_center_body_radii_moon',
    'test_center_body_radii_mars',
    'test_center_body_radii_saturn',
    'test_center_body_radii_uranus',
    'test_center_body_radii_neptune',
    'test_center_body_radii_pluto',
    'test_center_body_radii_bennu',
    'test_center_body_radii_eris',
    'test_center_body_radii_haumea',
    'test_center_body_radii_makemake',
    'test_center_body_radii_arrokoth',
    'test_center_body_radii_planet9',
    'test_orbital_period_mercury',
    'test_orbital_period_venus',
    'test_orbital_period_earth',
    'test_orbital_period_mars',
    'test_orbital_period_jupiter',
    'test_orbital_period_saturn',
    'test_orbital_period_uranus',
    'test_orbital_period_neptune',
    'test_orbital_period_moon',
    'test_orbital_period_io',
    'test_orbital_period_europa',
    'test_orbital_period_ganymede',
    'test_orbital_period_callisto',
    'test_orbital_period_titan',
    'test_orbital_period_triton',
    'test_orbital_period_charon',
    'test_orbital_period_phobos',
    'test_orbital_period_deimos',
    'test_orbital_period_halley',
    'test_orbital_period_sedna',
]

# Kept, and why: none of these holds a copy of a measured value.
#   derivations  -- solar_radius_au_is_derived, light_minutes_per_au_is_derived,
#                   core_au_derived_from_solar_radius,
#                   radiative_zone_au_derived_from_solar_radius
#   sanity bands -- solar_radius_au_value_sanity,
#                   light_minutes_per_au_value_sanity
#                   (these bound a DERIVED quantity, catching a broken
#                   derivation rather than pinning a measurement)
#   orderings    -- solar_shell_ordering, oort_cloud_ordering,
#                   earth_polar_less_than_equatorial,
#                   jupiter_polar_less_than_equatorial
#   consistency  -- center_body_radii_sun / _earth / _jupiter,
#                   earth_equatorial_matches_center_body,
#                   jupiter_equatorial_matches_center_body,
#                   sun_radius_matches_center_body
#   structure    -- center_body_radii_completeness,
#                   hyperbolic_objects_are_none

OLD_DOCSTRING_HEAD = b'''Pins every verified constant in constants_new.py against its cited value.
Fails if any value drifts. Forces deliberate updates with updated citation
comments rather than silent modification.'''

NEW_DOCSTRING_HEAD = b'''Checks the RELATIONS among constants in constants_new.py -- derivations,
orderings, cross-consistency, completeness. It holds no copy of any
measured value, so a legitimate correction never makes it stale.

Drift in the values themselves is NOT checked here. That is
constants_change_report.py, which reads the git diff rather than storing
its own copy of the numbers.

Retired 2026-08-12 (Tony's ruling): 55 tests that pinned a constant to a
hand-typed literal. They were a second dictionary -- every correction
needed a synchronized edit in two files, enforced by nothing. An August 2
cross-check batch corrected six values and updated no pins; the tests
then failed correctly for ten days while describing sourced values as
"drifted." The pins also carried their own citations, which nothing has
ever audited, and at least one of those citations was false.'''

RUNNER_OLD = b'''CHECKERS = [
    ('Constants provenance', ['test_constants_provenance.py'], None),'''
RUNNER_NEW = b'''CHECKERS = [
    ('Constants change', ['constants_change_report.py'], None),
    ('Constants relations', ['test_constants_provenance.py'], None),'''

RUNNER_DOC_OLD = b'''CHECKERS report a problem and inform the push call. They run last so
their verdict is the last thing on screen.'''
RUNNER_DOC_NEW = b'''CHECKERS report a problem and inform the push call. They run last so
their verdict is the last thing on screen.

Constants change runs first among them: it reads the git diff for
constants_new.py and reports any value that moved without its provenance
moving too. It replaced 55 hand-pinned literals on 2026-08-12 and stores
no numbers of its own.'''


def fingerprint(data):
    """MD5 over LF-normalized content -- line endings are not content."""
    return hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()


def main():
    here = os.path.dirname(os.path.abspath(__file__))

    if not os.path.exists(os.path.join(here, REQUIRED)):
        print('ERROR: %s is not in this folder.' % REQUIRED)
        print('       It is what replaces the pins being removed here.')
        sys.exit(1)

    blobs, crlf = {}, {}
    for name in BASE_MD5:
        path = os.path.join(here, name)
        if not os.path.exists(path):
            print('ERROR: %s not found. Run this from the repo root.' % name)
            sys.exit(1)
        with open(path, 'rb') as handle:
            data = handle.read()
        got = fingerprint(data)
        if got != BASE_MD5[name]:
            print('ERROR: base moved for %s' % name)
            print('       expected %s' % BASE_MD5[name])
            print('       got      %s' % got)
            print('Nothing written to any file.')
            sys.exit(1)
        blobs[name] = data
        crlf[name] = data.count(b'\r\n') > 0
        if crlf[name]:
            print('note: %s uses CRLF; preserved.' % name)

    # ---- test file: remove functions bottom-up ------------------------
    text = blobs[TESTS_FILE].decode('utf-8')
    newline = '\r\n' if crlf[TESTS_FILE] else '\n'
    lines = text.split(newline)

    tree = ast.parse(text.replace('\r\n', '\n'))
    spans = {}
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            spans[node.name] = (node.lineno, node.end_lineno)

    missing = [n for n in RETIRE if n not in spans]
    if missing:
        print('ERROR: %d named test(s) not found: %s'
              % (len(missing), ', '.join(missing[:5])))
        print('Nothing written to any file.')
        sys.exit(1)

    for name in sorted(RETIRE, key=lambda n: spans[n][0], reverse=True):
        start, end = spans[name]
        stop = end
        while stop < len(lines) and lines[stop].strip() == '':
            stop += 1
        del lines[start - 1:stop]

    # No registry to prune: this file discovers its tests with
    # _collect_tests() rather than listing them, unlike
    # test_cross_checked.py. Removing the function is the whole edit.
    result = newline.join(lines)

    old_doc = OLD_DOCSTRING_HEAD.decode()
    if crlf[TESTS_FILE]:
        old_doc = old_doc.replace('\n', '\r\n')
    if result.count(old_doc) != 1:
        print('ANCHOR FAIL (test docstring): expected 1 match, found %d.'
              % result.count(old_doc))
        print('Nothing written to any file.')
        sys.exit(1)
    new_doc = NEW_DOCSTRING_HEAD.decode()
    if crlf[TESTS_FILE]:
        new_doc = new_doc.replace('\n', '\r\n')
    result = result.replace(old_doc, new_doc)

    # ---- verify the result before writing -----------------------------
    try:
        checked = ast.parse(result.replace('\r\n', '\n'))
    except SyntaxError as exc:
        print('ERROR: result does not parse: %s' % exc)
        print('Nothing written to any file.')
        sys.exit(1)

    remaining = [n.name for n in checked.body
                 if isinstance(n, ast.FunctionDef)
                 and n.name.startswith('test_')]
    if len(remaining) != EXPECTED_REMAINING:
        print('ERROR: expected %d tests to remain, found %d.'
              % (EXPECTED_REMAINING, len(remaining)))
        print('Nothing written to any file.')
        sys.exit(1)

    print('  removed %d pinned tests' % len(RETIRE))
    print('  %d tests remain' % len(remaining))
    blobs[TESTS_FILE] = result.encode('utf-8')

    # ---- runner -------------------------------------------------------
    for label, old, new in (('runner: add the change reporter',
                             RUNNER_OLD, RUNNER_NEW),
                            ('runner: docstring',
                             RUNNER_DOC_OLD, RUNNER_DOC_NEW)):
        if crlf[RUNNER]:
            old = old.replace(b'\n', b'\r\n')
            new = new.replace(b'\n', b'\r\n')
        if blobs[RUNNER].count(old) != 1:
            print('ANCHOR FAIL (%s): expected 1 match, found %d.'
                  % (label, blobs[RUNNER].count(old)))
            print('Nothing written to any file.')
            sys.exit(1)
        blobs[RUNNER] = blobs[RUNNER].replace(old, new)
        print('  ok  %s' % label)

    for name, data in blobs.items():
        with open(os.path.join(here, name), 'wb') as handle:
            handle.write(data)

    print()
    print('patch applied')
    for name, data in sorted(blobs.items()):
        print('  %-38s %d bytes' % (name, len(data)))
    print()
    print('NEXT:')
    print('  1. python test_constants_provenance.py   -- expect 18 / 0')
    print('  2. python maintenance_run.py             -- expect all green')
    print('  3. commit')


if __name__ == '__main__':
    main()
