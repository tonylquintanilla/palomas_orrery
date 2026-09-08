"""
patch_L291_2_earth_shell_migration.py -- Earth shells read the store (L-291, step 2)

Built on orrery c51761a07ffcfa46a25ef49a175fb4e6d3b27a13
at https://github.com/tonylquintanilla/palomas_orrery (main).

WHAT THIS DOES
  patch_L291_1 gave constants_new.py names for the values Earth's shells
  draw. That made every matching literal in the shell modules a shadow
  constant (provenance-discipline, No Shadow Constants). This patch
  removes them: the builders and the tooltips now read the store, and the
  numbers in the hover text are formatted from the same names, so a
  value cannot change in one place and not the other.

  Tony's ruling, 2026-09-07: one store, one source of truth; the orrery
  side is not deferred.

  Two files, applied only if BOTH guards pass:

  earth_visualization_shells.py
    - import the new names
    - magnetosphere: sunward standoff, inner and outer belt distances
    - bow shock: standoff 15 -> EARTH_BOW_SHOCK_STANDOFF_RADII (12.5,
      Lugaz et al. 2016 midpoint). THIS CHANGES THE DRAWN SHAPE; Mode 5.
    - LEO: 6571 / 8371 km -> EARTH_LEO_INNER_KM / _OUTER_KM (6578 / 8378;
      the old figures were mean-radius sums)
    - geostationary: 42164.0 -> EARTH_GEOSTATIONARY_RADIUS_KM (derived,
      42164.17); hover ratio 6.62 -> 6.61 against the equatorial radius
    - Hill sphere: 235 -> EARTH_HILL_SPHERE_RADII (234.64)
    - the info strings and hover text quote the constants
    - docstring credit line

  shell_configs.py
    - import the new names
    - SHELL_CONFIGS['Earth']['hill_sphere'] radius_fraction and text
    - magnetosphere, leo and geostationary_belt tooltips

  NOT touched: the atmosphere shells at 1.05 and 1.25 radii. Those are
  drawing choices, not shadows of any store value (L-295 holds them).
  The Starlink density centre (6921 km) and the magnetotail dimensions
  are declared drawing parameters with no store constant; left as is.

HOW TO RUN
  Save to the repo root. Open in VS Code and press Run. It prints what
  it did and refuses to run twice. Then run the orrery, turn on Earth's
  magnetosphere, LEO, geostationary and Hill sphere shells, and look.

GUARDS
  Both files read in binary mode, LF-normalised, md5 checked against the
  values at c51761a0. Every edit must match its expected count or nothing
  is written. Inserted text is ASCII-only, LF line endings.

Written September 2026 with Anthropic's Claude Fable 5.1.
"""
import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

FILES = {
    "earth_visualization_shells.py": "e79a2394cf086dc03b9095755ab1a57d",
    "shell_configs.py": "a75af61ddfc5c1141eb0a2c23f917ab7",
}

# (old, new, expected_count) -- applied in order, all must match.
EDITS = {
    "earth_visualization_shells.py": [
        # E1: imports
        (
            "    EARTH_UPPER_MANTLE_KM, EARTH_UPPER_MANTLE_RADII,\n)\n",
            "    EARTH_UPPER_MANTLE_KM, EARTH_UPPER_MANTLE_RADII,\n"
            "    # L-291: the orbital and magnetospheric shells read the store too.\n"
            "    # Every number a hover quotes below is formatted from these names.\n"
            "    EARTH_EQUATORIAL_RADIUS_KM,\n"
            "    EARTH_MAGNETOPAUSE_STANDOFF_RADII, EARTH_BOW_SHOCK_STANDOFF_RADII,\n"
            "    EARTH_VAN_ALLEN_INNER_RADII, EARTH_VAN_ALLEN_OUTER_RADII,\n"
            "    EARTH_LEO_INNER_KM, EARTH_LEO_OUTER_KM,\n"
            "    EARTH_LEO_INNER_RADII, EARTH_LEO_OUTER_RADII,\n"
            "    EARTH_LEO_LOWER_ALTITUDE_KM, EARTH_LEO_UPPER_ALTITUDE_KM,\n"
            "    EARTH_GEOSTATIONARY_RADIUS_KM, EARTH_GEOSTATIONARY_RADII,\n"
            "    EARTH_HILL_SPHERE_KM, EARTH_HILL_SPHERE_RADII,\n"
            ")\n",
            1,
        ),
        # E10: docstring credit
        (
            "Module updated: May 2026 with Anthropic's Claude Opus 4.7\n",
            "Module updated: May 2026 with Anthropic's Claude Opus 4.7\n"
            "Module updated: September 2026 with Anthropic's Claude Fable 5.1 --\n"
            "    L-291: magnetosphere, bow shock, LEO, geostationary and Hill sphere\n"
            "    values read constants_new.py; no drawn literal remains.\n",
            1,
        ),
        # E2/E4: magnetosphere standoff in info string and hover (3 sites:
        # earth_magnetosphere_info, magnetosphere_text; shell_configs has its own)
        (
            "\"Earth's magnetosphere extends about 10 Earth radii on the Sun-facing side",
            "f\"Earth's magnetosphere extends about {EARTH_MAGNETOPAUSE_STANDOFF_RADII:g} Earth radii on the Sun-facing side",
            2,
        ),
        # E2/E6: bow shock standoff in info string and hover
        (
            "\"by Earth's magnetic field, typically located about 15 Earth radii upstream",
            "f\"by Earth's magnetic field, typically located about {EARTH_BOW_SHOCK_STANDOFF_RADII:g} Earth radii upstream",
            2,
        ),
        # E6: the old textbook caveat line, replaced by the sourced statement
        (
            "                \"Measured nominal standoff is ~11-14 R_E; the 15 R_E shown is the textbook value (Nature Comms 2016).<br>\"\n",
            "                \"Drawn at the midpoint of the 11-14 R_E measured under normal solar wind (Lugaz et al. 2016).<br>\"\n",
            1,
        ),
        # E3: params
        (
            "        'sunward_distance': 10,  # Compressed toward the sun\n",
            "        'sunward_distance': EARTH_MAGNETOPAUSE_STANDOFF_RADII,  # L-291: store, Shue et al. 1998\n",
            1,
        ),
        (
            "        'inner_belt_distance': 1.5,  # Distance in Earth radii\n"
            "        'outer_belt_distance': 4.5,  # Distance in Earth radii\n",
            "        'inner_belt_distance': EARTH_VAN_ALLEN_INNER_RADII,  # L-291: store, flux peak\n"
            "        'outer_belt_distance': EARTH_VAN_ALLEN_OUTER_RADII,  # L-291: store, flux peak\n",
            1,
        ),
        # E5: bow shock standoff
        (
            "    bow_shock_standoff = 15 * EARTH_RADIUS_AU  # Source: textbook ~15 R_E; measured nominal ~11-14 R_E (Nature Comms 2016)\n",
            "    # L-291: was a typed 15 R_E (textbook) with a comment conceding the\n"
            "    # measured 11-14. The store now holds the measured midpoint; see\n"
            "    # EARTH_BOW_SHOCK_STANDOFF_RADII in constants_new.py for the source.\n"
            "    bow_shock_standoff = EARTH_BOW_SHOCK_STANDOFF_RADII * EARTH_RADIUS_AU\n",
            1,
        ),
        # E7: LEO bands
        (
            "    LEO_LOW_KM  = 6571.0   # 200 km altitude\n"
            "    LEO_HIGH_KM = 8371.0   # 2000 km altitude\n",
            "    # L-291: were typed 6571 / 8371, which is the 6371 km MEAN radius plus\n"
            "    # the altitude -- a shadow of the wrong radius. The store derives\n"
            "    # both from the equatorial radius this shell is drawn against.\n"
            "    LEO_LOW_KM  = EARTH_LEO_INNER_KM    # 200 km altitude\n"
            "    LEO_HIGH_KM = EARTH_LEO_OUTER_KM    # 2000 km altitude\n",
            1,
        ),
        (
            "        \"Altitude range: 200 km to 2,000 km above surface<br>\"\n"
            "        \"Radius: 6,571 km to 8,371 km from Earth's center (1.03 to 1.31 Earth radii)<br><br>\"\n",
            "        f\"Altitude range: {EARTH_LEO_LOWER_ALTITUDE_KM:,.0f} km to {EARTH_LEO_UPPER_ALTITUDE_KM:,.0f} km above surface<br>\"\n"
            "        f\"Radius: {EARTH_LEO_INNER_KM:,.0f} km to {EARTH_LEO_OUTER_KM:,.0f} km from Earth's center \"\n"
            "        f\"({EARTH_LEO_INNER_RADII:.2f} to {EARTH_LEO_OUTER_RADII:.2f} Earth radii)<br><br>\"\n",
            1,
        ),
        # E8: geostationary
        (
            "    GEO_RADIUS_KM = 42164.0\n",
            "    GEO_RADIUS_KM = EARTH_GEOSTATIONARY_RADIUS_KM   # L-291: derived in the store from GM and rotation rate\n",
            1,
        ),
        (
            "        \"Altitude: 35,786 km / 0.000239 AU above surface<br>\"\n"
            "        \"Radius: 42,164 km / 0.000282 AU from Earth's center (6.62 Earth radii)<br><br>\"\n",
            "        f\"Altitude: {EARTH_GEOSTATIONARY_RADIUS_KM - EARTH_EQUATORIAL_RADIUS_KM:,.0f} km / \"\n"
            "        f\"{(EARTH_GEOSTATIONARY_RADIUS_KM - EARTH_EQUATORIAL_RADIUS_KM) / KM_PER_AU:.6f} AU above surface<br>\"\n"
            "        f\"Radius: {EARTH_GEOSTATIONARY_RADIUS_KM:,.0f} km / {EARTH_GEOSTATIONARY_RADIUS_KM / KM_PER_AU:.6f} AU \"\n"
            "        f\"from Earth's center ({EARTH_GEOSTATIONARY_RADII:.2f} Earth radii)<br><br>\"\n",
            1,
        ),
        # E9: Hill sphere (info string + hover: 2 sites)
        (
            "\"Earth's Hill Sphere (extends to ~235 Earth radii or about 1.5 million km",
            "f\"Earth's Hill Sphere (extends to about {EARTH_HILL_SPHERE_RADII:.0f} Earth radii or about {EARTH_HILL_SPHERE_KM / 1e6:.1f} million km",
            2,
        ),
        (
            "    radius_fraction = 235  # Earth's Hill sphere is about 235 Earth radii\n",
            "    radius_fraction = EARTH_HILL_SPHERE_RADII  # L-291: derived in the store from the two GMs\n",
            1,
        ),
    ],
    "shell_configs.py": [
        # S1: imports
        (
            "from constants_new import (\n"
            "    EARTH_INNER_CORE_RADII, EARTH_OUTER_CORE_RADII,\n"
            "    EARTH_LOWER_MANTLE_RADII, EARTH_UPPER_MANTLE_RADII,\n"
            ")\n",
            "from constants_new import (\n"
            "    EARTH_INNER_CORE_RADII, EARTH_OUTER_CORE_RADII,\n"
            "    EARTH_LOWER_MANTLE_RADII, EARTH_UPPER_MANTLE_RADII,\n"
            "    # L-291: the Earth tooltips below quote the store, not retyped numbers.\n"
            "    EARTH_EQUATORIAL_RADIUS_KM,\n"
            "    EARTH_MAGNETOPAUSE_STANDOFF_RADII, EARTH_BOW_SHOCK_STANDOFF_RADII,\n"
            "    EARTH_LEO_LOWER_ALTITUDE_KM, EARTH_LEO_UPPER_ALTITUDE_KM,\n"
            "    EARTH_LEO_INNER_RADII, EARTH_LEO_OUTER_RADII,\n"
            "    EARTH_GEOSTATIONARY_RADIUS_KM,\n"
            "    EARTH_HILL_SPHERE_KM, EARTH_HILL_SPHERE_RADII,\n"
            ")\n",
            1,
        ),
        # S2: Earth hill sphere (the only radius_fraction 235 in the file)
        (
            "            'radius_fraction': 235,\n",
            "            'radius_fraction': EARTH_HILL_SPHERE_RADII,  # L-291: store\n",
            1,
        ),
        (
            "\"Earth's Hill Sphere (extends to ~235 Earth radii or about 1.5 million km",
            "f\"Earth's Hill Sphere (extends to about {EARTH_HILL_SPHERE_RADII:.0f} Earth radii or about {EARTH_HILL_SPHERE_KM / 1e6:.1f} million km",
            2,
        ),
        # S3: magnetosphere tooltip
        (
            "\"Earth's magnetosphere extends about 10 Earth radii on the Sun-facing side",
            "f\"Earth's magnetosphere extends about {EARTH_MAGNETOPAUSE_STANDOFF_RADII:g} Earth radii on the Sun-facing side",
            1,
        ),
        (
            "\"by Earth's magnetic field, typically located about 15 Earth radii upstream",
            "f\"by Earth's magnetic field, typically located about {EARTH_BOW_SHOCK_STANDOFF_RADII:g} Earth radii upstream",
            1,
        ),
        # S4: LEO tooltip
        (
            "                \"Low Earth Orbit (LEO) is the region from roughly 200 km to 2,000 km altitude\\n\"\n"
            "                \"(1.03 to 1.31 Earth radii), where satellites orbit at all inclinations.\\n\\n\"\n",
            "                f\"Low Earth Orbit (LEO) is the region from roughly {EARTH_LEO_LOWER_ALTITUDE_KM:,.0f} km to {EARTH_LEO_UPPER_ALTITUDE_KM:,.0f} km altitude\\n\"\n"
            "                f\"({EARTH_LEO_INNER_RADII:.2f} to {EARTH_LEO_OUTER_RADII:.2f} Earth radii), where satellites orbit at all inclinations.\\n\\n\"\n",
            1,
        ),
        # S5: GEO tooltip
        (
            "                \"The geostationary belt (GEO) is a ring of orbital space at 42,164 km from Earth's center\\n\"\n"
            "                \"(35,786 km altitude), where satellites orbit at exactly Earth's rotation rate\\n\"\n",
            "                f\"The geostationary belt (GEO) is a ring of orbital space at {EARTH_GEOSTATIONARY_RADIUS_KM:,.0f} km from Earth's center\\n\"\n"
            "                f\"({EARTH_GEOSTATIONARY_RADIUS_KM - EARTH_EQUATORIAL_RADIUS_KM:,.0f} km altitude), where satellites orbit at exactly Earth's rotation rate\\n\"\n",
            1,
        ),
    ],
}


def main():
    texts = {}
    for name, md5 in FILES.items():
        p = ROOT / name
        lf = p.read_bytes().replace(b"\r\n", b"\n")
        got = hashlib.md5(lf).hexdigest()
        if got != md5:
            print("STOP: %s md5 (LF) is %s, expected %s (file at c51761a0)." % (name, got, md5))
            print("      Either this patch already ran or the file moved. Nothing written.")
            return 1
        texts[name] = lf.decode("utf-8")

    # Dry run: every edit must match its count before anything is written.
    for name, edits in EDITS.items():
        t = texts[name]
        for i, (old, new, n) in enumerate(edits, 1):
            c = t.count(old)
            if c != n:
                print("STOP: %s edit %d matched %d time(s), expected %d. Nothing written." % (name, i, c, n))
                print("      old text begins: %r" % old[:70])
                return 1
            try:
                new.encode("ascii")
            except UnicodeEncodeError as e:
                print("STOP: %s edit %d inserts non-ASCII: %s" % (name, i, e))
                return 1
            t = t.replace(old, new)
        texts[name] = t

    for name, t in texts.items():
        (ROOT / name).write_bytes(t.encode("utf-8"))
        print("Patched %-30s %2d edit(s), new md5 (LF) %s" %
              (name, len(EDITS[name]), hashlib.md5(t.encode("utf-8")).hexdigest()))
    print("Literals removed: magnetopause 10, bow shock 15, belts 1.5 / 4.5,")
    print("  LEO 6571 / 8371 km, GEO 42164 km, Hill 235 -- and the hover text")
    print("  for each now formats the store value.")
    print("Next: open the orrery, turn on Earth's magnetosphere, LEO, geostationary")
    print("  belt and Hill sphere, and look (the bow shock nose moves in to 12.5 R_E).")
    print("  Then provenance_scanner.py, commit, push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
