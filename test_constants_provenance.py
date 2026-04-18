"""
test_constants_provenance.py - Regression tests for verified numeric constants.

Pins every verified constant in constants_new.py against its cited value.
Fails if any value drifts. Forces deliberate updates with updated citation
comments rather than silent modification.

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
    CHROMOSPHERE_RADII,
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
    # Spacecraft reference
    PARKER_CLOSEST_RADII,
    # Dictionaries
    CENTER_BODY_RADII,
    KNOWN_ORBITAL_PERIODS,
)


# ============================================================
# Section 1: Fundamental constants (IAU/NIST exact definitions)
# ============================================================

def test_km_per_au():
    """IAU 2012 Resolution B2: 1 AU = 149,597,870,700 m exactly (149597870.7 km)."""
    assert KM_PER_AU == 149597870.7, f"KM_PER_AU drifted to {KM_PER_AU}"


def test_sun_radius_km():
    """IAU 2015 Resolution B3 nominal solar radius (Prsa et al. 2016, AJ 152:41)."""
    assert SUN_RADIUS_KM == 695700.0, f"SUN_RADIUS_KM drifted to {SUN_RADIUS_KM}"


def test_earth_equatorial_radius_km():
    """IAU 2015 Resolution B3 nominal terrestrial equatorial radius (WGS-84)."""
    assert EARTH_EQUATORIAL_RADIUS_KM == 6378.137, \
        f"EARTH_EQUATORIAL_RADIUS_KM drifted to {EARTH_EQUATORIAL_RADIUS_KM}"


def test_earth_polar_radius_km():
    """IAU 2015 Resolution B3 nominal terrestrial polar radius."""
    assert EARTH_POLAR_RADIUS_KM == 6356.752, \
        f"EARTH_POLAR_RADIUS_KM drifted to {EARTH_POLAR_RADIUS_KM}"


def test_jupiter_equatorial_radius_km():
    """IAU 2015 Resolution B3 nominal jovian equatorial radius."""
    assert JUPITER_EQUATORIAL_RADIUS_KM == 71492.0, \
        f"JUPITER_EQUATORIAL_RADIUS_KM drifted to {JUPITER_EQUATORIAL_RADIUS_KM}"


def test_jupiter_polar_radius_km():
    """IAU 2015 Resolution B3 nominal jovian polar radius."""
    assert JUPITER_POLAR_RADIUS_KM == 66854.0, \
        f"JUPITER_POLAR_RADIUS_KM drifted to {JUPITER_POLAR_RADIUS_KM}"


def test_speed_of_light_km_s():
    """NIST/SI exact definition: c = 299,792.458 km/s."""
    assert SPEED_OF_LIGHT_KM_S == 299792.458, \
        f"SPEED_OF_LIGHT_KM_S drifted to {SPEED_OF_LIGHT_KM_S}"


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


def test_chromosphere_radii():
    """Chromosphere extends to ~1.5 R_sun (Carroll & Ostlie 2017, Ch. 11)."""
    assert CHROMOSPHERE_RADII == 1.5, f"CHROMOSPHERE_RADII drifted to {CHROMOSPHERE_RADII}"


def test_inner_corona_radii():
    """Inner (K-)corona extends to 2-3 R_sun; we use 3 (Golub & Pasachoff 2010)."""
    assert INNER_CORONA_RADII == 3, f"INNER_CORONA_RADII drifted to {INNER_CORONA_RADII}"


def test_outer_corona_radii():
    """F-corona envelope extends to ~50 R_sun (Mann et al. 2004, A&A 414:1127)."""
    assert OUTER_CORONA_RADII == 50, f"OUTER_CORONA_RADII drifted to {OUTER_CORONA_RADII}"


def test_streamer_belt_radii():
    """Helmet streamers extend 4-6 R_sun; we use 6.0 (DeForest et al. 2018)."""
    assert STREAMER_BELT_RADII == 6.0, f"STREAMER_BELT_RADII drifted to {STREAMER_BELT_RADII}"


def test_roche_limit_radii():
    """Fluid Roche limit for comet densities: 2.44 * (1408/500)^(1/3) = 3.45 R_sun."""
    assert ROCHE_LIMIT_RADII == 3.45, f"ROCHE_LIMIT_RADII drifted to {ROCHE_LIMIT_RADII}"


def test_alfven_surface_radii():
    """Parker Solar Probe first crossing, April 28, 2021 (Kasper et al. 2021)."""
    assert ALFVEN_SURFACE_RADII == 18.8, f"ALFVEN_SURFACE_RADII drifted to {ALFVEN_SURFACE_RADII}"


def test_solar_shell_ordering():
    """Solar atmosphere shells must nest outward: chromosphere < corona < streamer < alfven."""
    assert CHROMOSPHERE_RADII < INNER_CORONA_RADII < ROCHE_LIMIT_RADII < STREAMER_BELT_RADII, \
        "Solar atmosphere shell ordering violated (chromo -> inner corona -> roche -> streamer)"
    assert STREAMER_BELT_RADII < ALFVEN_SURFACE_RADII < OUTER_CORONA_RADII, \
        "Solar atmosphere shell ordering violated (streamer -> alfven -> outer corona)"


# ============================================================
# Section 4: Heliosphere and Oort cloud (AU)
# ============================================================

def test_termination_shock_au():
    """Voyager 1 crossed termination shock at 94 AU, Dec 2004 (Stone et al. 2005)."""
    assert TERMINATION_SHOCK_AU == 94, f"TERMINATION_SHOCK_AU drifted to {TERMINATION_SHOCK_AU}"


def test_heliopause_radii():
    """~123 AU converted to solar radii: 123 * 149597870.7 / 695700 = 26449."""
    assert HELIOPAUSE_RADII == 26449, f"HELIOPAUSE_RADII drifted to {HELIOPAUSE_RADII}"


def test_heliopause_conversion_sanity():
    """Verify HELIOPAUSE_RADII conversion math: should round-trip to ~123 AU."""
    au_equivalent = HELIOPAUSE_RADII * SUN_RADIUS_KM / KM_PER_AU
    assert 122.9 < au_equivalent < 123.1, \
        f"HELIOPAUSE_RADII converts to {au_equivalent} AU, expected ~123 AU"


def test_inner_limit_oort_cloud_au():
    """Hills (1981); Oort (1950) -- inner edge estimate."""
    assert INNER_LIMIT_OORT_CLOUD_AU == 2000, \
        f"INNER_LIMIT_OORT_CLOUD_AU drifted to {INNER_LIMIT_OORT_CLOUD_AU}"


def test_inner_oort_cloud_au():
    """Hills (1981) -- outer edge of inner (Hills) cloud."""
    assert INNER_OORT_CLOUD_AU == 20000, f"INNER_OORT_CLOUD_AU drifted to {INNER_OORT_CLOUD_AU}"


def test_outer_oort_cloud_au():
    """Oort (1950); Weissman (1996) -- estimated outer boundary, ~0.5 parsec."""
    assert OUTER_OORT_CLOUD_AU == 100000, f"OUTER_OORT_CLOUD_AU drifted to {OUTER_OORT_CLOUD_AU}"


def test_gravitational_influence_au():
    """Approximate Hill sphere radius of Sun in Milky Way (~2 light-years)."""
    assert GRAVITATIONAL_INFLUENCE_AU == 126000, \
        f"GRAVITATIONAL_INFLUENCE_AU drifted to {GRAVITATIONAL_INFLUENCE_AU}"


def test_oort_cloud_ordering():
    """Oort cloud radii must nest outward: inner limit < inner < outer < gravitational influence."""
    assert INNER_LIMIT_OORT_CLOUD_AU < INNER_OORT_CLOUD_AU < OUTER_OORT_CLOUD_AU < GRAVITATIONAL_INFLUENCE_AU, \
        "Oort cloud shell ordering violated"


# ============================================================
# Section 5: Spacecraft reference
# ============================================================

def test_parker_closest_radii():
    """Parker Solar Probe perihelion 22, Dec 24, 2024.
    Corrected Apr 15, 2026 per Gemini review: 8.86 (surface altitude)
    -> 9.86 (from Sun center, consistent with other shell radii)."""
    assert PARKER_CLOSEST_RADII == 9.86, \
        f"PARKER_CLOSEST_RADII drifted to {PARKER_CLOSEST_RADII} " \
        f"(if this is 8.86, the 2026-04-15 Gemini correction was reverted)"


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


def test_center_body_radii_mercury():
    """NASA Fact Sheet volumetric mean (oblateness ~0.0009, equatorial diff sub-0.1%)."""
    assert CENTER_BODY_RADII['Mercury'] == 2439.7, \
        f"CENTER_BODY_RADII['Mercury'] drifted to {CENTER_BODY_RADII['Mercury']}"


def test_center_body_radii_venus():
    """NASA Fact Sheet volumetric mean (oblateness ~0)."""
    assert CENTER_BODY_RADII['Venus'] == 6051.8, \
        f"CENTER_BODY_RADII['Venus'] drifted to {CENTER_BODY_RADII['Venus']}"


def test_center_body_radii_earth():
    """IAU 2015 nominal equatorial (WGS-84). Hybrid convention: EQUATORIAL not volumetric (6371.0)."""
    assert CENTER_BODY_RADII['Earth'] == 6378.137, \
        f"CENTER_BODY_RADII['Earth'] = {CENTER_BODY_RADII['Earth']}. " \
        f"If this is 6371.0, the pre-April-16 volumetric-mean convention returned."
    # Cross-check with standalone constant
    assert CENTER_BODY_RADII['Earth'] == EARTH_EQUATORIAL_RADIUS_KM, \
        "CENTER_BODY_RADII['Earth'] and EARTH_EQUATORIAL_RADIUS_KM have diverged"


def test_center_body_radii_moon():
    """NASA Fact Sheet volumetric mean (oblateness ~0.0012)."""
    assert CENTER_BODY_RADII['Moon'] == 1737.4, \
        f"CENTER_BODY_RADII['Moon'] drifted to {CENTER_BODY_RADII['Moon']}"


def test_center_body_radii_mars():
    """IAU 2015 nominal equatorial. Hybrid convention: EQUATORIAL not volumetric (3389.5)."""
    assert CENTER_BODY_RADII['Mars'] == 3396.2, \
        f"CENTER_BODY_RADII['Mars'] = {CENTER_BODY_RADII['Mars']}. " \
        f"If this is 3389.5, the pre-April-16 volumetric-mean convention returned."


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


def test_center_body_radii_saturn():
    """IAU 2015 nominal equatorial. Hybrid convention: EQUATORIAL not volumetric (58232)."""
    assert CENTER_BODY_RADII['Saturn'] == 60268, \
        f"CENTER_BODY_RADII['Saturn'] = {CENTER_BODY_RADII['Saturn']}. " \
        f"If this is 58232, the pre-April-16 volumetric-mean convention returned."


def test_center_body_radii_uranus():
    """IAU 2015 nominal equatorial. Hybrid convention: EQUATORIAL not volumetric (25362)."""
    assert CENTER_BODY_RADII['Uranus'] == 25559, \
        f"CENTER_BODY_RADII['Uranus'] = {CENTER_BODY_RADII['Uranus']}. " \
        f"If this is 25362, the pre-April-16 volumetric-mean convention returned."


def test_center_body_radii_neptune():
    """IAU 2015 nominal equatorial. Hybrid convention: EQUATORIAL not volumetric (24622)."""
    assert CENTER_BODY_RADII['Neptune'] == 24764, \
        f"CENTER_BODY_RADII['Neptune'] = {CENTER_BODY_RADII['Neptune']}. " \
        f"If this is 24622, the pre-April-16 volumetric-mean convention returned."


def test_center_body_radii_pluto():
    """New Horizons occultation (Nimmo et al. 2017, Icarus)."""
    assert CENTER_BODY_RADII['Pluto'] == 1188.3, \
        f"CENTER_BODY_RADII['Pluto'] drifted to {CENTER_BODY_RADII['Pluto']}"


def test_center_body_radii_bennu():
    """Volumetric mean from OSIRIS-REx top-shape asteroid observations."""
    assert CENTER_BODY_RADII['Bennu'] == 0.262, \
        f"CENTER_BODY_RADII['Bennu'] drifted to {CENTER_BODY_RADII['Bennu']}"


def test_center_body_radii_eris():
    """Volumetric mean from 2011 occultation (Sicardy et al. 2011)."""
    assert CENTER_BODY_RADII['Eris'] == 1163, \
        f"CENTER_BODY_RADII['Eris'] drifted to {CENTER_BODY_RADII['Eris']}"


def test_center_body_radii_haumea():
    """Volumetric mean (highly ellipsoidal: 1050x840x537 km)."""
    assert CENTER_BODY_RADII['Haumea'] == 816, \
        f"CENTER_BODY_RADII['Haumea'] drifted to {CENTER_BODY_RADII['Haumea']}"


def test_center_body_radii_makemake():
    """Volumetric mean (Brown et al.)."""
    assert CENTER_BODY_RADII['Makemake'] == 715, \
        f"CENTER_BODY_RADII['Makemake'] drifted to {CENTER_BODY_RADII['Makemake']}"


def test_center_body_radii_arrokoth():
    """Volumetric mean (~35x20x14 km bilobed shape).
    Corrected 2026-04-15 per Gemini review: was 0.0088 (8.8 METERS!) -> 9.95 km."""
    assert CENTER_BODY_RADII['Arrokoth'] == 9.95, \
        f"CENTER_BODY_RADII['Arrokoth'] = {CENTER_BODY_RADII['Arrokoth']}. " \
        f"If this is 0.0088, the Gemini correction was reverted -- Arrokoth would be 8.8 METERS."


def test_center_body_radii_planet9():
    """Model estimate (Batygin & Brown; 5-10 M_Earth assumption)."""
    assert CENTER_BODY_RADII['Planet 9'] == 24000, \
        f"CENTER_BODY_RADII['Planet 9'] drifted to {CENTER_BODY_RADII['Planet 9']}"


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

def test_orbital_period_mercury():
    """Mercury orbital period: 87.969 days (JPL)."""
    assert KNOWN_ORBITAL_PERIODS['Mercury'] == 87.969, \
        f"Mercury orbital period drifted to {KNOWN_ORBITAL_PERIODS['Mercury']}"


def test_orbital_period_venus():
    """Venus orbital period: 224.701 days (JPL)."""
    assert KNOWN_ORBITAL_PERIODS['Venus'] == 224.701, \
        f"Venus orbital period drifted to {KNOWN_ORBITAL_PERIODS['Venus']}"


def test_orbital_period_earth():
    """Earth orbital period: 365.256 days (sidereal year, JPL)."""
    assert KNOWN_ORBITAL_PERIODS['Earth'] == 365.256, \
        f"Earth orbital period drifted to {KNOWN_ORBITAL_PERIODS['Earth']}"


def test_orbital_period_mars():
    """Mars orbital period: 686.980 days (JPL)."""
    assert KNOWN_ORBITAL_PERIODS['Mars'] == 686.980, \
        f"Mars orbital period drifted to {KNOWN_ORBITAL_PERIODS['Mars']}"


def test_orbital_period_jupiter():
    """Jupiter orbital period: 4332.589 days (JPL)."""
    assert KNOWN_ORBITAL_PERIODS['Jupiter'] == 4332.589, \
        f"Jupiter orbital period drifted to {KNOWN_ORBITAL_PERIODS['Jupiter']}"


def test_orbital_period_saturn():
    """Saturn orbital period: 10759.22 days (JPL)."""
    assert KNOWN_ORBITAL_PERIODS['Saturn'] == 10759.22, \
        f"Saturn orbital period drifted to {KNOWN_ORBITAL_PERIODS['Saturn']}"


def test_orbital_period_uranus():
    """Uranus orbital period: 30688.5 days (JPL)."""
    assert KNOWN_ORBITAL_PERIODS['Uranus'] == 30688.5, \
        f"Uranus orbital period drifted to {KNOWN_ORBITAL_PERIODS['Uranus']}"


def test_orbital_period_neptune():
    """Neptune orbital period: 60189.0 days (JPL)."""
    assert KNOWN_ORBITAL_PERIODS['Neptune'] == 60189.0, \
        f"Neptune orbital period drifted to {KNOWN_ORBITAL_PERIODS['Neptune']}"


def test_orbital_period_moon():
    """Moon sidereal orbital period: 27.321582 days."""
    assert KNOWN_ORBITAL_PERIODS['Moon'] == 27.321582, \
        f"Moon orbital period drifted to {KNOWN_ORBITAL_PERIODS['Moon']}"


def test_orbital_period_io():
    """Io orbital period: 1.769 days (42.456 hours, JPL)."""
    assert KNOWN_ORBITAL_PERIODS['Io'] == 1.769, \
        f"Io orbital period drifted to {KNOWN_ORBITAL_PERIODS['Io']}"


def test_orbital_period_europa():
    """Europa orbital period: 3.551 days (85.224 hours, JPL)."""
    assert KNOWN_ORBITAL_PERIODS['Europa'] == 3.551, \
        f"Europa orbital period drifted to {KNOWN_ORBITAL_PERIODS['Europa']}"


def test_orbital_period_ganymede():
    """Ganymede orbital period: 7.155 days (171.72 hours, JPL)."""
    assert KNOWN_ORBITAL_PERIODS['Ganymede'] == 7.155, \
        f"Ganymede orbital period drifted to {KNOWN_ORBITAL_PERIODS['Ganymede']}"


def test_orbital_period_callisto():
    """Callisto orbital period: 16.689 days (400.536 hours, JPL)."""
    assert KNOWN_ORBITAL_PERIODS['Callisto'] == 16.689, \
        f"Callisto orbital period drifted to {KNOWN_ORBITAL_PERIODS['Callisto']}"


def test_orbital_period_titan():
    """Titan orbital period: 15.945 days (382.68 hours, JPL)."""
    assert KNOWN_ORBITAL_PERIODS['Titan'] == 15.945, \
        f"Titan orbital period drifted to {KNOWN_ORBITAL_PERIODS['Titan']}"


def test_orbital_period_triton():
    """Triton orbital period: 5.877 days (141.05 hours, JPL). Note: retrograde orbit."""
    assert KNOWN_ORBITAL_PERIODS['Triton'] == 5.877, \
        f"Triton orbital period drifted to {KNOWN_ORBITAL_PERIODS['Triton']}"


def test_orbital_period_charon():
    """Charon orbital period: 6.387 days (153.29 hours, JPL). Pluto-Charon barycenter system."""
    assert KNOWN_ORBITAL_PERIODS['Charon'] == 6.387, \
        f"Charon orbital period drifted to {KNOWN_ORBITAL_PERIODS['Charon']}"


def test_orbital_period_phobos():
    """Phobos orbital period: 0.319 days (JPL)."""
    assert KNOWN_ORBITAL_PERIODS['Phobos'] == 0.319, \
        f"Phobos orbital period drifted to {KNOWN_ORBITAL_PERIODS['Phobos']}"


def test_orbital_period_deimos():
    """Deimos orbital period: 1.263 days (JPL)."""
    assert KNOWN_ORBITAL_PERIODS['Deimos'] == 1.263, \
        f"Deimos orbital period drifted to {KNOWN_ORBITAL_PERIODS['Deimos']}"


def test_orbital_period_halley():
    """Halley's comet period: 75.92414033 Julian years * 365.25 = 27731.29226 days.
    Epoch: JD 2439907.5 (1968-Feb-21)."""
    assert KNOWN_ORBITAL_PERIODS['Halley'] == 27731.29226, \
        f"Halley orbital period drifted to {KNOWN_ORBITAL_PERIODS['Halley']}"


def test_orbital_period_sedna():
    """Sedna orbital period: 11400 * 365.25 = 4163850.00 days (~11,400 years)."""
    assert KNOWN_ORBITAL_PERIODS['Sedna'] == 4163850.00, \
        f"Sedna orbital period drifted to {KNOWN_ORBITAL_PERIODS['Sedna']}"


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
