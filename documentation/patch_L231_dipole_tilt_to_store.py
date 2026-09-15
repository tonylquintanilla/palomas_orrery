"""Give Earth's dipole tilt one home: the store.

Targets, in the orrery repo:
  constants_new.py
  planet_visualization_utilities.py
Built against orrery 695f1f04a98a925737df929430567957ad62ccaf.
Handle: L-231.  2026-09-15, with Anthropic's Claude Opus 5.

WHY
---
Tony, 2026-09-15: "if we quote it it should be in the store."

Earth's dipole tilt IS sourced -- Alken et al. 2021, IGRF-13, with an
epoch and a drift rate, cleared through L-009's provenance gate on
2026-06-22. What it is not is IN THE STORE. It lives as a literal inside
PLANET_DIPOLE in planet_visualization_utilities.py, which makes it a
sourced value with a home outside the citation home, against the standing
rule that one value has one home and the store is that home.

Nothing on the web page can quote a number that the store does not carry,
so the belt hover currently states the magnetic tilt without its figure.
This patch is what lets that sentence carry 9.6.

WHAT IT DOES
------------
1. Adds EARTH_DIPOLE_TILT_DEG = 9.6 to constants_new.py, with the source,
   the epoch, the drift rate, the rounding, and the spread across models
   written out.
2. Rewires PLANET_DIPOLE['Earth']['tilt_deg'] to READ that constant
   instead of repeating the literal, so there is one value in one place.
   The dict's own note and source lines stay where they are -- they say
   more than the row does and they are what the cone's hover reads.
3. Fixes a stale comment above PLANET_DIPOLE. It says only bodies with a
   sourced dipole tilt appear in the table and lists Earth at "~11 deg" as
   DEFERRED pending a sourced tilt. Earth has been in the table with a
   sourced 9.6 since June. That comment sits eleven lines above the row it
   contradicts, and it is one of the places the stale 11 keeps being read
   from.

WHAT IT DOES NOT DO
-------------------
Nothing is served and no hover changes. That is the next patch, on the
gallery side. Nothing about the belt PLANE changes here either.

The name ends in _DEG so the maintenance checker can read its unit from
the name, which is how that checker still works until L-322.

AFTER RUNNING
-------------
  python -c "import constants_new; print(constants_new.EARTH_DIPOLE_TILT_DEG)"
  python -c "import planet_visualization_utilities as p; \\
             print(p.PLANET_DIPOLE['Earth']['tilt_deg'])"
  Both must print 9.6.
  python provenance_scanner.py     (Tier-1 must not rise)

UNDO
----
Nothing is written unless both fingerprints match. To undo: in GitHub
Desktop, select the two files in Changes and Discard Changes.
"""

import hashlib
import os
import sys

CONSTANTS = "constants_new.py"
DIPOLE = "planet_visualization_utilities.py"

FINGERPRINTS = {
    CONSTANTS: "439ccc3c63a1b0bd5ee923126694f738",
    DIPOLE: "73c1bfd205a372810ab4c837b84f8a00",
}

ROW_ANCHOR = b"EARTH_SOLAR_WIND_PRESSURE_NPA = 2.0\n"

ROW_NEW = b'''EARTH_DIPOLE_TILT_DEG = 9.6
# Unit: deg
# Status: measured V_SOURCED 2026-06-22 -- promoted to the store 2026-09-15
# Source: Alken et al. (2021), "International Geomagnetic Reference Field:
# Source+: the thirteenth generation", Earth Planets Space 73:49,
# Source+: doi:10.1186/s40623-020-01288-x. The angle between the geomagnetic
# Source+: dipole axis and Earth's rotation axis, for epoch 2020-2025.
# Note: 9.6 is rounded to a tenth of a degree, which is the precision the
# Note+: dipole cone's projection can honour; the cone is what this value
# Note+: was sourced for (L-009, cleared 2026-06-22, cross-checked de novo
# Note+: by a second model in June 2026).
# Note+: The tilt DRIFTS, slowly decreasing by about 0.05 deg per decade,
# Note+: so this row carries its epoch and any quotation of it should too.
# Note+: Other authorities give slightly different figures for the same
# Note+: quantity -- NOAA states 9.41 deg from the WMM2020 coefficients and
# Note+: 9.21 from WMM2025, and the British Geological Survey says about
# Note+: ten. The spread is about which coefficients and which epoch define
# Note+: "the dipole", not about the belts, and at drawing precision it
# Note+: does not move anything. Quote this row's figure with its model and
# Note+: epoch, or say "about ten degrees" and quote nothing.
# Note: promoted here 2026-09-15 (L-231) because a value cannot be quoted
# Note+: on the web page unless the store carries it. It previously lived
# Note+: only as a literal in PLANET_DIPOLE, which made it a sourced value
# Note+: with a home outside the citation home. PLANET_DIPOLE now reads
# Note+: this row; the fuller note and source strings stay in that table
# Note+: because the cone's hover reads them.
# Note+: The 11 degrees still typed at earth_visualization_shells.py:865 is
# Note+: a DIFFERENT, uncited number and is ruled for removal (L-305).

EARTH_SOLAR_WIND_PRESSURE_NPA = 2.0
'''

IMPORT_ANCHOR = b"""from constants_new import (
    KM_PER_AU, SUN_RADIUS_KM, LIGHT_MINUTES_PER_AU, KNOWN_ORBITAL_PERIODS,
    CENTER_BODY_RADII,"""

IMPORT_NEW = b"""from constants_new import (
    KM_PER_AU, SUN_RADIUS_KM, LIGHT_MINUTES_PER_AU, KNOWN_ORBITAL_PERIODS,
    CENTER_BODY_RADII,
    # L-231 (2026-09-15): Earth's dipole tilt moved to the store so the web
    # page can quote it. One value, one home; this table reads it.
    EARTH_DIPOLE_TILT_DEG,"""

STALE_ANCHOR = b"""# Only bodies with a sourced dipole tilt appear. Others are omitted, the gap left
# visible rather than guessed (Earth ~11 deg, Jupiter ~10 deg, Saturn <1 deg,
# Mercury ~0 deg: deferred pending sourced tilt + sense, their own entries later)."""

STALE_NEW = b"""# Only bodies with a sourced dipole tilt appear. Others are omitted, the gap left
# visible rather than guessed.
# CORRECTED 2026-09-15 (L-231): this paragraph used to list Earth at ~11 deg,
# Jupiter ~10, Saturn <1 and Mercury ~0 as DEFERRED pending a sourced tilt.
# All four have been in the table with sourced tilts since 2026-06-22, eleven
# lines below. The paragraph sat there contradicting them, and it is one of
# the places the stale "Earth 11 degrees" keeps being read from. Earth's tilt
# is 9.6 deg and now lives in the store as EARTH_DIPOLE_TILT_DEG."""

TILT_ANCHOR = b"    'Earth':   {'tilt_deg': 9.6, 'azimuth_deg': 0.0, 'offset_fraction': 0.085,"

TILT_NEW = b"""    # L-231 (2026-09-15): the tilt is read from the store, not repeated
    # here. The note and source below say more than the store row does and
    # are what the cone's hover reads, so they stay.
    'Earth':   {'tilt_deg': EARTH_DIPOLE_TILT_DEG, 'azimuth_deg': 0.0,
                'offset_fraction': 0.085,"""


def content_md5(data):
    return hashlib.md5(data.replace(b"\r\n", b"\n")).hexdigest()


def main():
    files = {}
    for path, expected in FINGERPRINTS.items():
        if not os.path.isfile(path):
            print("FAILURE: %s not found. Run this from the orrery repo root."
                  % path)
            print("NOTHING was written.")
            return 1
        with open(path, "rb") as handle:
            files[path] = handle.read()
        actual = content_md5(files[path])
        if actual != expected:
            print("FAILURE: BASE MOVED for %s." % path)
            print("  expected content md5 %s" % expected)
            print("  found                %s" % actual)
            print("NOTHING was written.")
            return 1

    if b"EARTH_DIPOLE_TILT_DEG" in files[CONSTANTS]:
        print("FAILURE: EARTH_DIPOLE_TILT_DEG is already in the store."
              " NOTHING was written.")
        return 1

    crlf = {p: files[p].count(b"\r\n") > 0 for p in files}

    def fit(path, block):
        return block.replace(b"\n", b"\r\n") if crlf[path] else block

    plan = [
        (CONSTANTS, "the new store row", ROW_ANCHOR, ROW_NEW),
        (DIPOLE, "the import", IMPORT_ANCHOR, IMPORT_NEW),
        (DIPOLE, "the stale deferred-tilts paragraph", STALE_ANCHOR, STALE_NEW),
        (DIPOLE, "Earth's tilt literal", TILT_ANCHOR, TILT_NEW),
    ]

    for path, label, old, new in plan:
        count = files[path].count(fit(path, old))
        if count != 1:
            print("FAILURE: in %s, expected 1 match for %s, got %d."
                  % (path, label, count))
            print("NOTHING was written.")
            return 1

    for path, label, old, new in plan:
        files[path] = files[path].replace(fit(path, old), fit(path, new))

    for path in sorted(files):
        with open(path, "wb") as handle:
            handle.write(files[path])

    print("OK: two files written.")
    for path in sorted(files):
        print("    %-38s (%s)" % (path, "CRLF" if crlf[path] else "LF"))
    print()
    print("Next:")
    print('  python -c "import constants_new as c;'
          ' print(c.EARTH_DIPOLE_TILT_DEG)"')
    print('  python -c "import planet_visualization_utilities as p;'
          " print(p.PLANET_DIPOLE['Earth']['tilt_deg'])\"")
    print("  Both must print 9.6.")
    print("  python provenance_scanner.py   (Tier-1 must not rise)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
