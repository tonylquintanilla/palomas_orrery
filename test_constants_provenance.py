"""
test_constants_provenance.py - Regression tests for verified numeric constants.

Checks the RELATIONS among constants in constants_new.py -- derivations,
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
ever audited, and at least one of those citations was false.

Run from the project directory:
    python test_constants_provenance.py

Exits 0 if all tests pass, non-zero on any failure.

Complement to provenance_scanner.py:
    Scanner:  where should I be worried? (open-ended discovery)
    Tests:    did this specific value drift? (binary pinning)

Motivation: close_approach_data.py carried a local copy of CENTER_BODY_RADII
with pre-April-16 volumetric values (Jupiter = 69911 instead of 71492). The
scanner would have flagged it as INCONSISTENT. These tests would have failed
on the first run after the Hybrid Radius Convention change, forcing the
discrepancy into attention immediately.

Design:
    - Plain assert functions, no pytest/unittest dependency
    - One test per value, docstring carries the citation
    - main() runs all tests and prints a pass/fail summary
    - Grouped into sections matching constants_new.py organization

The values tested here were verified by Anthropic's Claude Opus 4.6 against
IAU resolutions and NASA fact sheets in April 2026, cross-reviewed by Google
Gemini, and integrated by Tony. See constants_new.py docstring for the full
verification process.

Module created: April 17, 2026 with Anthropic's Claude Opus 4.7
Module updated: August 26, 2026 with Anthropic's Claude Opus 5
(L-249: Section 10, six relation tests for Earth's interior
boundaries. No pinned values -- derivations against their own
factors, orderings, and geometric brackets, so a corrected source
never makes them stale)
Module updated: October 4, 2026 with Anthropic's Claude Opus 5.5
(L-371: three relation tests for the Sun's distances -- each ranged
edge is drawn at an end of its range, the heliopause and the
gravitational reach are converted from their sources' units rather
than typed twice, and the unsourced range row stays gone. Still no
pinned values. A fourth the same day: the Roche limit is drawn at its
own full digits, outside the inner corona.)

Role: devtool
Domain: dev_tools
"""

import sys
import traceback

from constants_new import (
    # Fundamental constants (IAU/NIST exact definitions)
    KM_PER_AU,
    SUN_RADIUS_KM,
    EARTH_EQUATORIAL_RADIUS_KM,
    EARTH_POLAR_RADIUS_KM,
    JUPITER_EQUATORIAL_RADIUS_KM,
    JUPITER_POLAR_RADIUS_KM,
    SPEED_OF_LIGHT_KM_S,
    # Derived
    SOLAR_RADIUS_AU,
    LIGHT_MINUTES_PER_AU,
    # Solar structure
    CORE_AU,
    RADIATIVE_ZONE_AU,
    CHROMOSPHERE_PHYSICAL_RADII,
    INNER_CORONA_RADII,
    OUTER_CORONA_RADII,
    HELMET_CUSP_RADII,
    ROCHE_LIMIT_RADII,
    ALFVEN_SURFACE_RADII,
    # Heliosphere and Oort
    TERMINATION_SHOCK_AU,
    HELIOPAUSE_RADII,
    INNER_LIMIT_OORT_CLOUD_AU,
    INNER_OORT_CLOUD_AU,
    OUTER_OORT_CLOUD_AU,
    GRAVITATIONAL_INFLUENCE_AU,
    # L-371: the Sun's ranged edges, and the rows in their sources' units
    OORT_CLOUD_INNER_EDGE_LOW_AU,
    OORT_CLOUD_INNER_EDGE_HIGH_AU,
    OORT_CLOUD_OUTER_EDGE_LOW_AU,
    OORT_CLOUD_OUTER_EDGE_HIGH_AU,
    HELMET_CUSP_LOW_RADII,
    HELMET_CUSP_HIGH_RADII,
    ROCHE_LIMIT_DRAWN_RADII,
    HELIOPAUSE_AU,
    GRAVITATIONAL_INFLUENCE_PC,
    PARSEC_TO_AU,
    KM_PER_PARSEC,
    KM_PER_AU,
    SUN_RADIUS_KM,
    # Spacecraft reference
    PARKER_CLOSEST_RADII,
    # Earth interior boundaries (L-249)
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


# ============================================================
# Section 1: Fundamental constants (IAU/NIST exact definitions)
# ============================================================

# ============================================================
# Section 2: Derived constants (identity checks)
# ============================================================
# These must equal their derivation. If the primary constant changes,
# these should recompute automatically -- the test catches accidental
# hardcoding that would break that invariant.

def test_solar_radius_au_is_derived():
    """SOLAR_RADIUS_AU must equal SUN_RADIUS_KM / KM_PER_AU to full precision."""
    expected = SUN_RADIUS_KM / KM_PER_AU
    assert abs(SOLAR_RADIUS_AU - expected) < 1e-15, \
        f"SOLAR_RADIUS_AU = {SOLAR_RADIUS_AU}, expected {expected} (derivation broken)"


def test_light_minutes_per_au_is_derived():
    """LIGHT_MINUTES_PER_AU must equal KM_PER_AU / SPEED_OF_LIGHT_KM_S / 60 to full precision."""
    expected = KM_PER_AU / SPEED_OF_LIGHT_KM_S / 60.0
    assert abs(LIGHT_MINUTES_PER_AU - expected) < 1e-15, \
        f"LIGHT_MINUTES_PER_AU = {LIGHT_MINUTES_PER_AU}, expected {expected} (derivation broken)"


def test_solar_radius_au_value_sanity():
    """SOLAR_RADIUS_AU should be approximately 0.004650 (spot check on derivation)."""
    assert 0.00465 < SOLAR_RADIUS_AU < 0.00466, \
        f"SOLAR_RADIUS_AU = {SOLAR_RADIUS_AU} is outside expected ~0.00465 range"


def test_light_minutes_per_au_value_sanity():
    """LIGHT_MINUTES_PER_AU should be approximately 8.317 (spot check on derivation)."""
    assert 8.316 < LIGHT_MINUTES_PER_AU < 8.318, \
        f"LIGHT_MINUTES_PER_AU = {LIGHT_MINUTES_PER_AU} is outside expected ~8.317 range"


# ============================================================
# Section 3: Solar structure (AU and solar radii)
# ============================================================

def test_core_au_derived_from_solar_radius():
    """CORE_AU is a fraction of the solar radius, inside the
    conventional 0.2-0.25 R_sun core range (Carroll & Ostlie 2017,
    Ch. 11; Bahcall, Pinsonneault & Basu 2001, ApJ 555:990).

    Holds no copy of the measured fraction. Restated 2026-08-29
    (L-258) alongside its radiative-zone twin, which had the same
    shape and fired the moment its value moved. The store currently
    draws at the low end of the range; promoting it off 0.2 must not
    make this test stale.
    """
    ratio = CORE_AU / SOLAR_RADIUS_AU
    low, high = 0.20, 0.25
    eps = 1e-9  # float round-trip on (k * x) / x, not a physical margin
    assert low - eps <= ratio <= high + eps, \
        f"CORE_AU / SOLAR_RADIUS_AU = {ratio}, outside the " \
        f"{low}-{high} R_sun core range"


def test_radiative_zone_au_derived_from_solar_radius():
    """RADIATIVE_ZONE_AU is a fraction of the solar radius, inside the
    convection-zone base implied by Christensen-Dalsgaard, Gough &
    Thompson (1991), ApJ 378:413 -- depth 0.287 +/- 0.003 R_sun, so a
    base of 0.710 to 0.716 R_sun.

    Holds no copy of the measured fraction. Restated 2026-08-29
    (L-258): the pinned form asserted 0.7 and failed correctly when
    the store was corrected to 0.713. A re-sourcing that leaves the
    published band still fires; a rounding inside it does not.
    """
    ratio = RADIATIVE_ZONE_AU / SOLAR_RADIUS_AU
    low, high = 0.710, 0.716
    eps = 1e-9  # float round-trip on (k * x) / x, not a physical margin
    assert low - eps <= ratio <= high + eps, \
        f"RADIATIVE_ZONE_AU / SOLAR_RADIUS_AU = {ratio}, outside the " \
        f"{low}-{high} R_sun convection-zone base band"


def test_solar_shell_ordering():
    """Solar atmosphere shells must nest outward: chromosphere < corona < streamer < alfven."""
    assert CHROMOSPHERE_PHYSICAL_RADII < INNER_CORONA_RADII < ROCHE_LIMIT_RADII < HELMET_CUSP_RADII, \
        "Solar atmosphere shell ordering violated (chromo -> inner corona -> roche -> helmet cusp)"
    assert HELMET_CUSP_RADII < ALFVEN_SURFACE_RADII < OUTER_CORONA_RADII, \
        "Solar atmosphere shell ordering violated (helmet cusp -> alfven -> outer corona)"


# ============================================================
# Section 4: Heliosphere and Oort cloud (AU)
# ============================================================

def test_oort_cloud_ordering():
    """Oort cloud radii must nest outward: inner limit < inner < outer < gravitational influence."""
    assert INNER_LIMIT_OORT_CLOUD_AU < INNER_OORT_CLOUD_AU < OUTER_OORT_CLOUD_AU < GRAVITATIONAL_INFLUENCE_AU, \
        "Oort cloud shell ordering violated"


def test_sun_ranged_edges_drawn_at_an_end():
    """L-371: each ranged edge is drawn at the end its row states.

    The Oort cloud's inner edge at the near end of its range and its
    outer edge at the far end (Tony's ruling A, 2026-10-03), and the
    helmet cusp at the top of 2-4 solar radii.
    """
    assert OORT_CLOUD_INNER_EDGE_LOW_AU < OORT_CLOUD_INNER_EDGE_HIGH_AU
    assert INNER_LIMIT_OORT_CLOUD_AU == OORT_CLOUD_INNER_EDGE_LOW_AU, \
        "the inner edge is not drawn at the near end of its range"
    assert OORT_CLOUD_OUTER_EDGE_LOW_AU < OORT_CLOUD_OUTER_EDGE_HIGH_AU
    assert OUTER_OORT_CLOUD_AU == OORT_CLOUD_OUTER_EDGE_HIGH_AU, \
        "the outer edge is not drawn at the far end of its range"
    assert HELMET_CUSP_LOW_RADII < HELMET_CUSP_HIGH_RADII
    assert HELMET_CUSP_RADII == HELMET_CUSP_HIGH_RADII, \
        "the helmet cusp is not drawn at the top of its range"


def test_sun_distances_converted_not_typed():
    """L-371 / L-386: one distance, one row, in its source's unit.

    The heliopause is stored in AU and the gravitational reach in
    parsecs; the solar-radii and AU names are computed from them.
    """
    rel = 1e-12
    expect = HELIOPAUSE_AU * KM_PER_AU / SUN_RADIUS_KM
    assert abs(HELIOPAUSE_RADII - expect) <= rel * expect, \
        f"HELIOPAUSE_RADII {HELIOPAUSE_RADII} is not HELIOPAUSE_AU converted ({expect})"
    expect = PARSEC_TO_AU * KM_PER_AU
    assert abs(KM_PER_PARSEC - expect) <= rel * expect, \
        f"KM_PER_PARSEC {KM_PER_PARSEC} is not PARSEC_TO_AU in km ({expect})"
    expect = GRAVITATIONAL_INFLUENCE_PC * PARSEC_TO_AU
    assert abs(GRAVITATIONAL_INFLUENCE_AU - expect) <= rel * expect, \
        f"GRAVITATIONAL_INFLUENCE_AU {GRAVITATIONAL_INFLUENCE_AU} is not the parsec row in AU ({expect})"


def test_roche_limit_drawn_at_its_full_digits():
    """L-371, Tony's option B (2026-10-04): the drawn row equals the
    one-figure row at full digits, and stays outside the inner corona's
    drawn line, which is why it exists."""
    assert ROCHE_LIMIT_DRAWN_RADII == ROCHE_LIMIT_RADII, \
        "the Roche limit is not drawn at its own row's full digits"
    assert ROCHE_LIMIT_DRAWN_RADII > INNER_CORONA_RADII, \
        "the drawn Roche limit sits on or inside the inner corona"


def test_unsourced_gravitational_range_stays_gone():
    """L-371: the 100,000-200,000 AU range had no source and went with
    the midpoint drawn from it. A row of that name coming back would
    put an unsourced range back in front of a visitor."""
    import constants_new
    assert not hasattr(constants_new, "GRAVITATIONAL_INFLUENCE_RANGE_AU"), \
        "GRAVITATIONAL_INFLUENCE_RANGE_AU is back in constants_new.py"


# ============================================================
# Section 5: Spacecraft reference
# ============================================================

# ============================================================
# Section 6: CENTER_BODY_RADII dict -- the Hybrid Radius Convention
# ============================================================
# Hybrid convention (April 16, 2026):
#   - Major planets (Earth-Neptune) + Sun + Pluto: equatorial radius
#   - Small bodies (Bennu, Eris, Haumea, Makemake, Arrokoth, Planet 9): volumetric mean
#   - Mercury, Venus, Moon: volumetric retained (equatorial difference sub-0.1%)
#
# THIS SECTION CAUGHT THE close_approach_data.py STALENESS BUG.
# If any Jupiter/Saturn/Uranus/Neptune value drifts back to its volumetric
# counterpart, the test fails and forces attention.

def test_center_body_radii_sun():
    """IAU 2015 nominal solar radius = 695700 km (matches SUN_RADIUS_KM)."""
    assert CENTER_BODY_RADII['Sun'] == 695700, \
        f"CENTER_BODY_RADII['Sun'] drifted to {CENTER_BODY_RADII['Sun']}"


def test_center_body_radii_earth():
    """IERS Conventions (2010) equatorial radius. Hybrid convention:
    EQUATORIAL not volumetric (6371.0). The literal below is the whole
    check -- CENTER_BODY_RADII['Earth'] IS EARTH_EQUATORIAL_RADIUS_KM by
    reference, so comparing the two cannot fail and is not attempted."""
    assert CENTER_BODY_RADII['Earth'] == 6378.1366, \
        f"CENTER_BODY_RADII['Earth'] = {CENTER_BODY_RADII['Earth']}. " \
        f"If this is 6371.0, the pre-April-16 volumetric-mean convention returned."


def test_center_body_radii_jupiter():
    """IAU 2015 nominal equatorial. Hybrid convention: EQUATORIAL not volumetric (69911).

    THIS IS THE CANARY. close_approach_data.py carried a stale local copy with
    69911, producing ~1,580 km surface-distance errors on Jovian flybys. If
    this test ever fails, a volumetric-mean value has crept back in."""
    assert CENTER_BODY_RADII['Jupiter'] == 71492, \
        f"CENTER_BODY_RADII['Jupiter'] = {CENTER_BODY_RADII['Jupiter']}. " \
        f"If this is 69911, the pre-April-16 volumetric-mean convention returned."


def test_center_body_radii_completeness():
    """All expected bodies must be present. Protects against accidental deletion."""
    expected_bodies = {
        'Sun', 'Mercury', 'Venus', 'Earth', 'Moon', 'Mars',
        'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto',
        'Bennu', 'Eris', 'Haumea', 'Makemake', 'Arrokoth', 'Planet 9',
    }
    actual = set(CENTER_BODY_RADII.keys())
    missing = expected_bodies - actual
    assert not missing, f"CENTER_BODY_RADII missing expected bodies: {missing}"


# ============================================================
# Section 7: KNOWN_ORBITAL_PERIODS -- planets and key moons
# ============================================================
# Testing planets (IAU-anchored) and major moons with JPL-anchored values.
# Skipping approximations like "3.63 * 365.25" for asteroids -- too noisy
# and the values are computed expressions, not cited constants.

# ============================================================
# Section 8: Hyperbolic/parabolic objects must remain None
# ============================================================
# A careless edit that filled in a numeric period for a hyperbolic object
# would silently produce a nonsense "closed orbit" visualization. Pin None.

def test_hyperbolic_objects_are_none():
    """Hyperbolic and parabolic objects must have period = None (infinite)."""
    hyperbolic_objects = [
        'West',           # C/1975 V1-A (parabolic)
        'C/2025_K1',      # Hyperbolic
        'C/2025_K1-B',    # Hyperbolic fragment
        'C/2025_K1-D',    # Hyperbolic fragment
        'Borisov',        # Hyperbolic
        'McNaught',       # Hyperbolic
        'ATLAS',          # Hyperbolic (PER= 9.999999E99)
        'PANSTARRS',      # Hyperbolic
        '3I/ATLAS',       # Interstellar hyperbolic
        '1I/Oumuamua',    # Interstellar hyperbolic
        '2I/Borisov',     # Interstellar hyperbolic
        'Wierzchos',      # Near-parabolic, effectively open
    ]
    for name in hyperbolic_objects:
        assert name in KNOWN_ORBITAL_PERIODS, \
            f"Hyperbolic object '{name}' missing from KNOWN_ORBITAL_PERIODS"
        assert KNOWN_ORBITAL_PERIODS[name] is None, \
            f"Hyperbolic object '{name}' has non-None period " \
            f"{KNOWN_ORBITAL_PERIODS[name]} -- would render as closed orbit"


# ============================================================
# Section 9: Cross-module invariants
# ============================================================
# Checks that constants_new.py internal consistency holds across sections.
#
# Three tests were DELETED here on 2026-08-20 (L-210, Tony's ruling).
# They asserted that EARTH_EQUATORIAL_RADIUS_KM, JUPITER_EQUATORIAL_
# RADIUS_KM and SUN_RADIUS_KM each agreed with their CENTER_BODY_RADII
# entry. But that dict holds each constant BY REFERENCE, so every one
# was x == x: three test names promising a divergence check that could
# not fail. They were written for a shadow copy this file does not
# have. Two more of the same shape were deleted from Section 8, where
# the literal pins beside them are the checks that can actually fail.
# Do not restore them: if CENTER_BODY_RADII ever stops referencing the
# constants, the fix is to make it reference them again, not to add a
# test that watches the copy drift.

def test_earth_polar_less_than_equatorial():
    """Earth is oblate: polar radius must be less than equatorial."""
    assert EARTH_POLAR_RADIUS_KM < EARTH_EQUATORIAL_RADIUS_KM, \
        f"Earth polar ({EARTH_POLAR_RADIUS_KM}) >= equatorial ({EARTH_EQUATORIAL_RADIUS_KM})"


def test_jupiter_polar_less_than_equatorial():
    """Jupiter is oblate: polar radius must be less than equatorial."""
    assert JUPITER_POLAR_RADIUS_KM < JUPITER_EQUATORIAL_RADIUS_KM, \
        f"Jupiter polar ({JUPITER_POLAR_RADIUS_KM}) >= equatorial ({JUPITER_EQUATORIAL_RADIUS_KM})"


# ============================================================
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
    assert EARTH_POLAR_RADIUS_KM < EARTH_MEAN_RADIUS_KM < EARTH_EQUATORIAL_RADIUS_KM, \
        (f"Earth mean radius ({EARTH_MEAN_RADIUS_KM}) is not between polar "
         f"({EARTH_POLAR_RADIUS_KM}) and equatorial ({EARTH_EQUATORIAL_RADIUS_KM})")


def test_earth_lower_mantle_derived_from_660_depth():
    """The lower mantle boundary must remain a subtraction, not a literal.

    Fails if EARTH_LOWER_MANTLE_KM is hardcoded to 5711, or if either
    factor moves without it following. It cannot fail on a corrected
    660 depth, which is the point -- a new depth propagates.
    """
    expected = EARTH_MEAN_RADIUS_KM - EARTH_D660_DEPTH_KM
    assert abs(EARTH_LOWER_MANTLE_KM - expected) < 1e-9, \
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
        assert abs(fraction - expected) < 1e-15, \
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
        assert 0.0 < fraction < 1.0, \
            f"{name} ({fraction}) is not strictly between 0 and the surface"


def test_earth_interior_ordering():
    """The four shells must nest, innermost outward.

    Fails if two boundaries are transposed -- the copy-paste error that
    a block of four near-identical definitions invites, and one the
    render would show only as a colour in the wrong place.
    """
    assert (EARTH_INNER_CORE_RADII < EARTH_OUTER_CORE_RADII
            < EARTH_LOWER_MANTLE_RADII < EARTH_UPPER_MANTLE_RADII), \
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
            < EARTH_EQUATORIAL_RADIUS_KM), \
        ("Earth interior radii are not in increasing order: "
         f"{EARTH_INNER_CORE_KM}, {EARTH_OUTER_CORE_KM}, "
         f"{EARTH_LOWER_MANTLE_KM}, {EARTH_UPPER_MANTLE_KM} against a drawn "
         f"radius of {EARTH_EQUATORIAL_RADIUS_KM}")


# ============================================================
# Test runner
# ============================================================

def _collect_tests():
    """Find every module-level function whose name starts with 'test_'."""
    import inspect
    tests = []
    current_module = sys.modules[__name__]
    for name, obj in inspect.getmembers(current_module):
        if name.startswith('test_') and inspect.isfunction(obj):
            tests.append((name, obj))
    # Preserve definition order by sorting on source line number
    tests.sort(key=lambda pair: inspect.getsourcelines(pair[1])[1])
    return tests


def main():
    """Run all tests. Print summary. Exit non-zero on any failure."""
    tests = _collect_tests()

    passed = 0
    failed = 0
    failures = []

    print(f"Running {len(tests)} provenance tests against constants_new.py...")
    print("=" * 70)

    for name, fn in tests:
        try:
            fn()
            passed += 1
            print(f"  PASS  {name}")
        except AssertionError as e:
            failed += 1
            failures.append((name, str(e)))
            print(f"  FAIL  {name}")
        except Exception as e:
            failed += 1
            failures.append((name, f"Unexpected {type(e).__name__}: {e}"))
            print(f"  ERROR {name}")
            traceback.print_exc()

    print("=" * 70)
    print(f"Results: {passed} passed, {failed} failed, {len(tests)} total")

    if failures:
        print("\nFailure details:")
        for name, msg in failures:
            print(f"\n  {name}:")
            print(f"    {msg}")
        return 1

    # The runner quotes the LAST non-blank line as this tool's
    # verdict, so the count belongs here rather than only in the
    # Results line above. A verdict that cannot move cannot report a
    # suite that shrank.
    print(f"\n{passed} of {len(tests)} provenance tests passed against "
          f"constants_new.py. No constants have drifted.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
