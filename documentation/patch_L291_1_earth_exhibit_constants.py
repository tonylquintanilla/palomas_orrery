"""
patch_L291_1_earth_exhibit_constants.py -- Earth exhibit constants (L-291, step 2)

Built on orrery d7151aafd8563901e3e1f478be0f4f280da56849
at https://github.com/tonylquintanilla/palomas_orrery (main).

WHAT THIS DOES
  Adds to constants_new.py the measured and derived values the Earth
  exhibit renders and the orrery's Earth shells currently carry as typed
  literals: geostationary radius (derived from GM and rotation rate),
  LEO edges, the stratopause and thermopause, the two Van Allen belt
  peaks, the magnetopause and bow shock standoffs, the geocorona extent,
  and the Hill sphere (derived from the two GMs). Every measured value
  carries its source inline; every derived value shows its arithmetic.

  Two insertions:
    1. After the EARTH_UPPER_MANTLE_RADII block -- the main Earth block.
    2. Before SOLAR_MASS_KG -- the Hill sphere pair, which needs
       GM_SUN_SI and so must sit below it (Python reads top-down).

  It changes NO existing line. It does not touch the shell modules;
  migrating their literals onto these names is a separate patch.

HOW TO RUN
  Save to the repo root (next to constants_new.py). Open in VS Code and
  press Run. It prints what it did and refuses to run twice.

GUARDS
  The file is read in binary mode, normalised to LF, and its md5 must
  equal the value below (constants_new.py at d7151aaf). On mismatch it
  stops without writing. Inserted text is ASCII-only, LF line endings.

Written September 2026 with Anthropic's Claude Fable 5.1.
"""
import hashlib
import sys
from pathlib import Path

TARGET = Path(__file__).resolve().parent / "constants_new.py"
EXPECTED_MD5 = "6bdd4eee5337ada6aebb596b4952e75e"

ANCHOR_1 = (
    "EARTH_UPPER_MANTLE_RADII = EARTH_UPPER_MANTLE_KM / EARTH_EQUATORIAL_RADIUS_KM\n"
    "# Derived: 6346.6 / 6378.1366 = 0.99506 -- 5 significant figures, set by\n"
    "# Derived+: the numerator. Report no more than that.\n"
)

BLOCK_1 = '''
# --- Earth exhibit block (L-291, 2026-09-07) -------------------------------
# The values below are what the Earth exhibit (interactive.html?exhibit=earth)
# renders and what the orrery's Earth shells draw. Until this block existed
# they were typed literals in earth_visualization_shells.py and
# shell_configs.py; the exhibit's served entry points at these names and the
# live store-drift run checks them by name. Migrating the shell modules onto
# these names is a follow-on patch, not this one.

EARTH_GM_KM3_S2 = 398600.4418
# Source: IERS Conventions (2010), IERS Technical Note 36, Table 1.1 --
# Source+: geocentric gravitational constant GM_E = 3.986004418e14 m^3 s^-2
# Source+: (uncertainty 8e5 m^3 s^-2). Converted to km^3 s^-2 here.
# Ref: https://iers-conventions.obspm.fr/content/tn36.pdf
# Note: TCB-compatible value as tabulated; the TT-compatible value differs
# Note+: in the ninth figure, below anything this file derives from it.

EARTH_ROTATION_RATE_RAD_S = 7.292115e-5
# Source: IERS Conventions (2010), TN36 Table 1.1 -- nominal mean Earth
# Source+: angular velocity, 7.292115e-5 rad s^-1.
# Ref: https://iers-conventions.obspm.fr/content/tn36.pdf

EARTH_GEOSTATIONARY_RADIUS_KM = (EARTH_GM_KM3_S2 / EARTH_ROTATION_RATE_RAD_S ** 2) ** (1.0 / 3.0)
# Derived: (398600.4418 / 7.292115e-5^2)^(1/3) = 42164.17 km -- the
# Derived+: circular orbit whose period is one sidereal rotation. Seven
# Derived+: figures in both inputs; report 42,164 km.
# Note: the orrery's geostationary shell types 42164.0 km and quotes
# Note+: 6.62 radii, a ratio taken against the 6371 km mean radius. Against
# Note+: the equatorial radius this file draws to, it is 6.611.
EARTH_GEOSTATIONARY_RADII = EARTH_GEOSTATIONARY_RADIUS_KM / EARTH_EQUATORIAL_RADIUS_KM
# Derived: 42164.17 / 6378.1366 = 6.6107 -- report no more than five figures.

EARTH_LEO_UPPER_ALTITUDE_KM = 2000.0
# Source: IADC Space Debris Mitigation Guidelines, IADC-02-01 Rev. 3
# Source+: (June 2021), section 3.3.2 -- the LEO Protected Region extends
# Source+: from the surface to an altitude of 2,000 km. Section 3.3.1 takes
# Source+: the equatorial radius as the reference surface, as this file does.
# Ref: https://orbitaldebris.jsc.nasa.gov/library/iadc-space-debris-guidelines-revision-2.pdf
EARTH_LEO_LOWER_ALTITUDE_KM = 200.0
# Declared: the floor the orrery's LEO shell draws from. The IADC region
# Declared+: starts at the surface; 200 km is a drawing choice marking where
# Declared+: orbits stop decaying within days. Not a measured boundary.
EARTH_LEO_INNER_KM = EARTH_EQUATORIAL_RADIUS_KM + EARTH_LEO_LOWER_ALTITUDE_KM
EARTH_LEO_OUTER_KM = EARTH_EQUATORIAL_RADIUS_KM + EARTH_LEO_UPPER_ALTITUDE_KM
# Derived: 6378.1366 + 200 = 6578.1 km; 6378.1366 + 2000 = 8378.1 km.
# Note: the orrery's LEO shell types 6571 and 8371 km, which is 6371 + the
# Note+: altitude -- the mean radius, not the equatorial one the shell is
# Note+: drawn against. Seven km, below the drawn resolution, but the
# Note+: hover text quotes those numbers. Follow-on with the migration.
EARTH_LEO_INNER_RADII = EARTH_LEO_INNER_KM / EARTH_EQUATORIAL_RADIUS_KM
EARTH_LEO_OUTER_RADII = EARTH_LEO_OUTER_KM / EARTH_EQUATORIAL_RADIUS_KM
# Derived: 1.0314 and 1.3136 -- report 1.03 and 1.31, as the hover does.

EARTH_STRATOPAUSE_ALTITUDE_KM = 50.0
# Source: NOAA JetStream, "Layers of the Atmosphere" -- stratosphere to
# Source+: about 50 km; and NASA, "Earth's Atmospheric Layers" -- the
# Source+: stratosphere extends to 50 km.
# Ref: https://www.noaa.gov/jetstream/atmosphere/layers-of-atmosphere
# Ref: https://www.nasa.gov/image-article/earths-atmospheric-layers-3/
EARTH_THERMOPAUSE_ALTITUDE_KM = 600.0
# Source: NOAA JetStream, same page -- thermosphere from about 85 km to
# Source+: about 600 km, the exosphere beyond; NASA, same page -- the
# Source+: thermosphere extends to 600 km.
# Note: a nominal figure. The thermopause moves with solar activity over
# Note+: roughly 500 to 1,000 km; the drawn shell is not that precise.
EARTH_STRATOPAUSE_RADII = (EARTH_EQUATORIAL_RADIUS_KM + EARTH_STRATOPAUSE_ALTITUDE_KM) / EARTH_EQUATORIAL_RADIUS_KM
EARTH_THERMOPAUSE_RADII = (EARTH_EQUATORIAL_RADIUS_KM + EARTH_THERMOPAUSE_ALTITUDE_KM) / EARTH_EQUATORIAL_RADIUS_KM
# Derived: 1.0078 and 1.0941.
# Note: SHELL_CONFIGS['Earth'] draws the lower atmosphere at 1.05 radii
# Note+: (about 319 km up) and the upper atmosphere at 1.25 radii (about
# Note+: 1,595 km up) while their own hover text ends at 50 km and about
# Note+: 1,000 km. Both drawn fractions are visibility choices wearing
# Note+: physical-looking numbers. Recorded under L-295; the exhibit's
# Note+: served entry declares the drawn fraction and points here for the
# Note+: physical one.

EARTH_VAN_ALLEN_INNER_RADII = 1.5
# Source: Baker, D. N. et al. (2018), "Space Weather Effects in the
# Source+: Earth's Radiation Belts", Space Sci. Rev. 214:17,
# Source+: doi:10.1007/s11214-017-0452-7 -- inner-zone proton fluxes peak
# Source+: near geocentric r ~ 1.5 R_E. Also "A New Electron and Proton
# Source+: Radiation Belt Identified by CIRBE/REPTile-2 Measurements After
# Source+: the Magnetic Super Storm of 10 May 2024", J. Geophys. Res. Space
# Source+: Physics (2025), doi:10.1029/2024JA033504 -- the inner belt is
# Source+: centred near L = 1.5.
# Note: a peak, not an edge. The inner belt spans roughly L = 1.1 to 2;
# Note+: the drawn torus marks where the flux is greatest.
EARTH_VAN_ALLEN_OUTER_RADII = 4.5
# Source: the CIRBE/REPTile-2 paper above, doi:10.1029/2024JA033504 -- the
# Source+: outer belt is most intense around L = 4 and 5; Kellerman et al.
# Source+: (2014) as cited in "Electron intensity measurements by the
# Source+: Cluster/RAPID/IES instrument in Earth's radiation belts and ring
# Source+: current" (2018, arXiv:1809.00902) -- maximum electron flux at
# Source+: L = 4-5. Midpoint of that band. Baker et al. (2018), above, put
# Source+: the outer zone at r ~ 3 to 6.5 R_E from SAMPEX.
# Note: a peak, not an edge. The outer belt spans roughly L = 3 to 7 and
# Note+: moves with geomagnetic activity; the drawn torus marks the peak.

EARTH_MAGNETOPAUSE_STANDOFF_RADII = 10.0
# Source: Shue, J.-H. et al. (1998), "Magnetopause location under extreme
# Source+: solar wind conditions", J. Geophys. Res. 103, 17691-17700,
# Source+: doi:10.1029/98JA01103 -- r0 = 10.22 + 1.29 tanh(0.184(Bz+8.14))
# Source+: x Dp^(-1/6.6), which is 10.2 R_E at Bz = 0 nT, Dp = 2 nPa.
# Source+: Lugaz et al. (2016), doi:10.1038/ncomms13001 -- typical subsolar
# Source+: magnetopause 9-11 R_E.
# Note: the nominal quiet-time standoff. Under storm compression it can
# Note+: fall inside geostationary orbit (6.6 R_E); the drawn shape is
# Note+: the quiet one.

EARTH_BOW_SHOCK_STANDOFF_RADII = 12.5
# Source: Lugaz, N. et al. (2016), "Earth's magnetosphere and outer
# Source+: radiation belt under sub-Alfvenic solar wind", Nat. Commun. 7,
# Source+: 13001, doi:10.1038/ncomms13001 -- under normal solar wind the
# Source+: bow shock forms at a subsolar distance of 11-14 R_E.
# Derived: midpoint of the sourced 11-14 R_E range.
# Note: the orrery's bow shock conic stands off at 15 R_E, a textbook
# Note+: figure its own code comment already flags against the measured
# Note+: 11-14. The store holds the measured value; the shell's 15 is a
# Note+: migration item. Model form: Farris & Russell (1994), J. Geophys.
# Note+: Res. 99, 17681, doi:10.1029/94JA01020.

EARTH_GEOCORONA_RADII = 100.0
# Source: Baliukin, I. I., Bertaux, J.-L., Quemerais, E., Izmodenov, V.
# Source+: V. & Schmidt, W. (2019), "SWAN/SOHO Lyman-alpha mapping: the
# Source+: hydrogen geocorona extends well beyond the Moon", J. Geophys.
# Source+: Res. Space Physics 124, 861-885, doi:10.1029/2018JA026136 --
# Source+: the geocorona is detected to at least 100 Earth radii.
# Note: a detection floor, not an edge -- the hydrogen thins without a
# Note+: boundary. The shell is drawn at the sourced floor and its hover
# Note+: says so. It encloses the Moon's orbit at about 60 radii.
# --- end Earth exhibit block --------------------------------------------------
'''

ANCHOR_2 = "\nSOLAR_MASS_KG = GM_SUN_SI / GRAVITATIONAL_CONSTANT_SI\n"

BLOCK_2 = '''
EARTH_HILL_SPHERE_KM = KM_PER_AU * (EARTH_GM_KM3_S2 / (3.0 * GM_SUN_SI * 1.0e-9)) ** (1.0 / 3.0)
# Derived: r_H = a (m / 3M)^(1/3) with a = 1 AU, m/M = GM_E / GM_Sun =
# Derived+: 398600.4418 / 1.3271244e11 = 3.00349e-6; (m/3M)^(1/3) =
# Derived+: 0.0100039; x 149,597,870.7 km = 1,496,559 km. Report 1.50e6 km.
# Derived+: Placed here, not in the Earth block above, because it needs
# Derived+: GM_SUN_SI and this file is read top-down (L-291).
# Note: a = 1 AU exactly. Earth's semi-major axis is 1.00000011 AU (NASA
# Note+: Earth Fact Sheet), agreement to seven figures, so the rounding is
# Note+: below everything else in the derivation.
# Ref: https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html
EARTH_HILL_SPHERE_RADII = EARTH_HILL_SPHERE_KM / EARTH_EQUATORIAL_RADIUS_KM
# Derived: 1,496,559 / 6378.1366 = 234.64 -- the "about 235 radii" the
# Derived+: orrery's Hill sphere shell types as radius_fraction = 235.
'''


def main():
    raw = TARGET.read_bytes()
    lf = raw.replace(b"\r\n", b"\n")
    got = hashlib.md5(lf).hexdigest()
    if got != EXPECTED_MD5:
        print("STOP: constants_new.py md5 (LF-normalised) is %s" % got)
        print("      expected %s (file at d7151aaf)." % EXPECTED_MD5)
        print("      Either this patch already ran or the file moved. Nothing written.")
        return 1

    text = lf.decode("utf-8")
    for a, label in ((ANCHOR_1, "anchor 1"), (ANCHOR_2, "anchor 2")):
        n = text.count(a)
        if n != 1:
            print("STOP: %s found %d times, need exactly 1. Nothing written." % (label, n))
            return 1

    for blk in (BLOCK_1, BLOCK_2):
        try:
            blk.encode("ascii")
        except UnicodeEncodeError as e:
            print("STOP: inserted text is not ASCII: %s" % e)
            return 1

    # Bottom-up: anchor 2 sits below anchor 1, so patch it first.
    text = text.replace(ANCHOR_2, BLOCK_2 + ANCHOR_2, 1)
    text = text.replace(ANCHOR_1, ANCHOR_1 + BLOCK_1, 1)

    TARGET.write_bytes(text.encode("utf-8"))
    names = [ln.split(" =")[0] for ln in (BLOCK_1 + BLOCK_2).splitlines()
             if ln[:1].isupper() and " = " in ln]
    print("Patched constants_new.py: %d lines added, %d constants:" %
          ((BLOCK_1 + BLOCK_2).count("\n"), len(names)))
    for n in names:
        print("  " + n)
    print("New md5 (LF): %s" % hashlib.md5(TARGET.read_bytes()).hexdigest())
    print("Next: run provenance_scanner.py, then commit and push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
