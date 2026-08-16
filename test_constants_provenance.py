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
    STREAMER_BELT_RADII,
    ROCHE_LIMIT_RADII,
    ALFVEN_SURFACE_RADII,
    # Heliosphere and Oort
    TERMINATION_SHOCK_AU,
    HELIOPAUSE_RADII,
    INNER_LIMIT_OORT_CLOUD_AU,
    INNER_OORT_CLOUD_AU,
    OUTER_OORT_CLOUD_AU,
    GRAVITATIONAL_INFLUENCE_AU,
    GRAVITATIONAL_INFLUENCE_RANGE_AU,
    # Spacecraft reference
    PARKER_CLOSEST_RADII,
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
    """CORE_AU must equal 0.2 * SOLAR_RADIUS_AU (standard solar model)."""
    expected = 0.2 * SOLAR_RADIUS_AU
    assert abs(CORE_AU - expected) < 1e-15, \
        f"CORE_AU = {CORE_AU}, expected {expected} (derivation broken)"


def test_radiative_zone_au_derived_from_solar_radius():
    """RADIATIVE_ZONE_AU must equal 0.7 * SOLAR_RADIUS_AU (standard solar model)."""
    expected = 0.7 * SOLAR_RADIUS_AU
    assert abs(RADIATIVE_ZONE_AU - expected) < 1e-15, \
        f"RADIATIVE_ZONE_AU = {RADIATIVE_ZONE_AU}, expected {expected} (derivation broken)"


def test_solar_shell_ordering():
    """Solar atmosphere shells must nest outward: chromosphere < corona < streamer < alfven."""
    assert CHROMOSPHERE_PHYSICAL_RADII < INNER_CORONA_RADII < ROCHE_LIMIT_RADII < STREAMER_BELT_RADII, \
        "Solar atmosphere shell ordering violated (chromo -> inner corona -> roche -> streamer)"
    assert STREAMER_BELT_RADII < ALFVEN_SURFACE_RADII < OUTER_CORONA_RADII, \
        "Solar atmosphere shell ordering violated (streamer -> alfven -> outer corona)"


# ============================================================
# Section 4: Heliosphere and Oort cloud (AU)
# ============================================================

def test_oort_cloud_ordering():
    """Oort cloud radii must nest outward: inner limit < inner < outer < gravitational influence."""
    assert INNER_LIMIT_OORT_CLOUD_AU < INNER_OORT_CLOUD_AU < OUTER_OORT_CLOUD_AU < GRAVITATIONAL_INFLUENCE_AU, \
        "Oort cloud shell ordering violated"


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
    # Cross-check with standalone SUN_RADIUS_KM
    assert CENTER_BODY_RADII['Sun'] == SUN_RADIUS_KM, \
        "CENTER_BODY_RADII['Sun'] and SUN_RADIUS_KM have diverged"


def test_center_body_radii_earth():
    """IAU 2015 nominal equatorial (WGS-84). Hybrid convention: EQUATORIAL not volumetric (6371.0)."""
    assert CENTER_BODY_RADII['Earth'] == 6378.137, \
        f"CENTER_BODY_RADII['Earth'] = {CENTER_BODY_RADII['Earth']}. " \
        f"If this is 6371.0, the pre-April-16 volumetric-mean convention returned."
    # Cross-check with standalone constant
    assert CENTER_BODY_RADII['Earth'] == EARTH_EQUATORIAL_RADIUS_KM, \
        "CENTER_BODY_RADII['Earth'] and EARTH_EQUATORIAL_RADIUS_KM have diverged"


def test_center_body_radii_jupiter():
    """IAU 2015 nominal equatorial. Hybrid convention: EQUATORIAL not volumetric (69911).

    THIS IS THE CANARY. close_approach_data.py carried a stale local copy with
    69911, producing ~1,580 km surface-distance errors on Jovian flybys. If
    this test ever fails, a volumetric-mean value has crept back in."""
    assert CENTER_BODY_RADII['Jupiter'] == 71492, \
        f"CENTER_BODY_RADII['Jupiter'] = {CENTER_BODY_RADII['Jupiter']}. " \
        f"If this is 69911, the pre-April-16 volumetric-mean convention returned."
    # Cross-check with standalone constant
    assert CENTER_BODY_RADII['Jupiter'] == JUPITER_EQUATORIAL_RADIUS_KM, \
        "CENTER_BODY_RADII['Jupiter'] and JUPITER_EQUATORIAL_RADIUS_KM have diverged"


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

def test_earth_equatorial_matches_center_body():
    """EARTH_EQUATORIAL_RADIUS_KM and CENTER_BODY_RADII['Earth'] must agree."""
    assert EARTH_EQUATORIAL_RADIUS_KM == CENTER_BODY_RADII['Earth'], \
        "EARTH_EQUATORIAL_RADIUS_KM != CENTER_BODY_RADII['Earth'] -- internal inconsistency"


def test_jupiter_equatorial_matches_center_body():
    """JUPITER_EQUATORIAL_RADIUS_KM and CENTER_BODY_RADII['Jupiter'] must agree."""
    assert JUPITER_EQUATORIAL_RADIUS_KM == CENTER_BODY_RADII['Jupiter'], \
        "JUPITER_EQUATORIAL_RADIUS_KM != CENTER_BODY_RADII['Jupiter'] -- internal inconsistency"


def test_sun_radius_matches_center_body():
    """SUN_RADIUS_KM and CENTER_BODY_RADII['Sun'] must agree."""
    assert SUN_RADIUS_KM == CENTER_BODY_RADII['Sun'], \
        "SUN_RADIUS_KM != CENTER_BODY_RADII['Sun'] -- internal inconsistency"


def test_earth_polar_less_than_equatorial():
    """Earth is oblate: polar radius must be less than equatorial."""
    assert EARTH_POLAR_RADIUS_KM < EARTH_EQUATORIAL_RADIUS_KM, \
        f"Earth polar ({EARTH_POLAR_RADIUS_KM}) >= equatorial ({EARTH_EQUATORIAL_RADIUS_KM})"


def test_jupiter_polar_less_than_equatorial():
    """Jupiter is oblate: polar radius must be less than equatorial."""
    assert JUPITER_POLAR_RADIUS_KM < JUPITER_EQUATORIAL_RADIUS_KM, \
        f"Jupiter polar ({JUPITER_POLAR_RADIUS_KM}) >= equatorial ({JUPITER_EQUATORIAL_RADIUS_KM})"


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

    print("\nAll provenance tests passed. No constants have drifted.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
