"""
patch_L291_4_earth_hover_sources.py -- every live Earth hover names its source (L-291)

Built on orrery 5170bec1c81a6a025c5499610e328e0f788e6a43
at https://github.com/tonylquintanilla/palomas_orrery (main).

WHAT THIS DOES
  Tony's ruling, 2026-09-07: a hover that quotes a measured number names
  its source in the hover, where the viewer can see it, not only in the
  code comment the scanner reads. The rule is pending as
  orrery-coding-conventions 1.8; this patch applies it to Earth.

  Each Source line is SCOPED to what it sources. The interior hovers
  quote temperatures PREM does not give, so the line says "Source
  (radius)", and the temperatures stay as they were -- uncited prose,
  not a claim dressed as a measurement.

  Two lines are REPLACED rather than annotated. The belt hovers quoted
  altitude ranges (1,000-6,000 km; 13,000-60,000 km) that match no
  source consulted -- ESA's Cluster page gives 6,000-12,000 km for the
  inner belt, the review literature gives L-shell spans, and none of
  them gives those two ranges. Under the project's rule an unsourceable
  claim is removed and the gap noted, so both now state the sourced
  peak distance and span in Earth radii, from the same papers the store
  cites. The shell_configs tooltip carries the same two lines and gets
  the same replacement.

  Also: the LEO hover typed "42,164 km" for GEO; it now formats the
  store constant (a shadow patch 2 missed because the string is about
  GEO inside the LEO builder).

  Files: earth_visualization_shells.py (interior info strings,
  magnetosphere, bow shock, belts, LEO) and shell_configs.py (crust,
  Hill sphere, magnetosphere tooltip). The geostationary hover already
  carried a Source line and is unchanged. The dead builders (L-254) are
  not touched.

HOW TO RUN
  Save to the repo root. Open in VS Code and press Run. Then open the
  orrery and read any Earth hover: its last line names the source.
  Then provenance_scanner.py, commit, push.

GUARDS
  Both files read in binary mode, LF-normalised, md5 checked against the
  values at 5170bec1. Every edit must match its expected count or nothing
  is written. Inserted text is ASCII-only, LF line endings.

Written September 2026 with Anthropic's Claude Fable 5.1.
"""
import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

FILES = {
    "earth_visualization_shells.py": "a511ab3b617ce1aa761b2cb6712a01b0",
    "shell_configs.py": "95412c5f53780d9f6e279e246bc5fcd8",
}

PREM = "Dziewonski & Anderson (1981), PREM, Phys. Earth Planet. Inter. 25:297"
D660 = "Ishii et al. (2019), Nature Geoscience 12:869"

INNER_BELT_OLD = (
    "        \"Inner Van Allen Belt: Region of trapped charged particles (mainly protons)<br>\"\n"
    "        \"extending from about 1,000 km to 6,000 km above Earth's surface.\",\n"
    "        \"Outer Van Allen Belt: Region of trapped charged particles (mainly electrons)<br>\"\n"
    "        \"extending from about 13,000 km to 60,000 km above Earth's surface.\"\n"
)
INNER_BELT_NEW = (
    "        f\"Inner Van Allen Belt: Region of trapped charged particles (mainly protons).<br>\"\n"
    "        f\"Drawn at the flux peak, {EARTH_VAN_ALLEN_INNER_RADII:g} Earth radii from Earth's centre; the belt<br>\"\n"
    "        \"spans roughly 1.1 to 2 Earth radii.<br>\"\n"
    "        \"Source (peak): Baker et al. (2018), Space Sci. Rev. 214:17, doi:10.1007/s11214-017-0452-7.\",\n"
    "        f\"Outer Van Allen Belt: Region of trapped charged particles (mainly electrons).<br>\"\n"
    "        f\"Drawn at the flux peak, {EARTH_VAN_ALLEN_OUTER_RADII:g} Earth radii from Earth's centre; the belt<br>\"\n"
    "        \"spans roughly 3 to 7 Earth radii and moves with geomagnetic activity.<br>\"\n"
    "        \"Source (peak): J. Geophys. Res. Space Physics (2025), doi:10.1029/2024JA033504; Baker et al. (2018).\"\n"
)

EDITS = {
    "earth_visualization_shells.py": [
        # interior info strings -- scoped source line before the closing paren
        (
            "            f\"{EARTH_INNER_CORE_KM:,.1f} km in radius.\"\n)\n",
            "            f\"{EARTH_INNER_CORE_KM:,.1f} km in radius.\\n\\n\"\n"
            "            \"Source (radius): " + PREM + ".\"\n)\n",
            1,
        ),
        (
            "            \"4,500 degC (8,100 degF) to 5,400 degC (9,800 degF).\"\n)\n",
            "            \"4,500 degC (8,100 degF) to 5,400 degC (9,800 degF).\\n\\n\"\n"
            "            \"Source (radius): " + PREM + ".\"\n)\n",
            1,
        ),
        (
            "            \"temperatures from 2,200 degC to 4,500 degC (4,000 degF to 8,100 degF) and extreme pressure.\"\n)\n",
            "            \"temperatures from 2,200 degC to 4,500 degC (4,000 degF to 8,100 degF) and extreme pressure.\\n\\n\"\n"
            "            \"Source (boundaries): " + PREM + "; " + D660 + ".\"\n)\n",
            1,
        ),
        (
            "            \"(900 degF to 4,000 degF).\"\n)\n",
            "            \"(900 degF to 4,000 degF).\\n\\n\"\n"
            "            \"Source (boundaries): " + D660 + "; " + PREM + ".\"\n)\n",
            1,
        ),
        # magnetosphere hover
        (
            "                 \"from solar radiation and cosmic rays, making complex life possible.\"]\n",
            "                 \"from solar radiation and cosmic rays, making complex life possible.<br><br>\"\n"
            "                 \"Source (standoff): Shue et al. (1998), J. Geophys. Res. 103:17691; \"\n"
            "                 \"Lugaz et al. (2016), Nat. Commun. 7:13001.\"]\n",
            1,
        ),
        # bow shock hover
        (
            "                \"The Bow Shock points towards the Sun along the X-axis. The XY plane is the ecliptic.\"]\n",
            "                \"The Bow Shock points towards the Sun along the X-axis. The XY plane is the ecliptic.<br><br>\"\n"
            "                \"Source (standoff): Lugaz et al. (2016), Nat. Commun. 7:13001, doi:10.1038/ncomms13001.\"]\n",
            1,
        ),
        # belt texts (replacement, see docstring)
        (INNER_BELT_OLD, INNER_BELT_NEW, 1),
        # LEO hover: GEO shadow literal, then source line
        (
            "        \"Compare with the Geostationary Belt (GEO) at 42,164 km -- 5x farther out,<br>\"\n"
            "        \"invisible to the naked eye, but controlling global communications.\"\n",
            "        f\"Compare with the Geostationary Belt (GEO) at {EARTH_GEOSTATIONARY_RADIUS_KM:,.0f} km -- 5x farther out,<br>\"\n"
            "        \"invisible to the naked eye, but controlling global communications.<br><br>\"\n"
            "        \"Source (upper edge): IADC Space Debris Mitigation Guidelines, IADC-02-01 Rev. 3 (2021), \"\n"
            "        \"sec. 3.3.2. The 200 km floor is a drawing choice, not a measured boundary.\"\n",
            1,
        ),
    ],
    "shell_configs.py": [
        # crust hover + tooltip
        (
            "                \"made primarily of granite. The crust contains all known life and the accessible portion<br>\"\n"
            "                \"of Earth's geological resources. Surface temperatures range from -80 degC to 60 degC (-112 degF to 140 degF).\"\n"
            "            ),\n",
            "                \"made primarily of granite. The crust contains all known life and the accessible portion<br>\"\n"
            "                \"of Earth's geological resources. Surface temperatures range from -80 degC to 60 degC (-112 degF to 140 degF).<br><br>\"\n"
            "                \"Source (radius): IERS Conventions (2010), TN36 Table 1.1, equatorial radius; \"\n"
            "                \"crust thicknesses: USGS, Interior of the Earth.\"\n"
            "            ),\n",
            1,
        ),
        (
            "                \"made primarily of granite. The crust contains all known life and the accessible portion\\n\"\n"
            "                \"of Earth's geological resources. Surface temperatures range from -80 degC to 60 degC (-112 degF to 140 degF).\"\n"
            "            ),\n",
            "                \"made primarily of granite. The crust contains all known life and the accessible portion\\n\"\n"
            "                \"of Earth's geological resources. Surface temperatures range from -80 degC to 60 degC (-112 degF to 140 degF).\\n\\n\"\n"
            "                \"Source (radius): IERS Conventions (2010), TN36 Table 1.1, equatorial radius; \"\n"
            "                \"crust thicknesses: USGS, Interior of the Earth.\"\n"
            "            ),\n",
            1,
        ),
        # Hill sphere hover -- Earth block anchored on its own first line;
        # the formula paragraph itself is shared by five bodies.
        (
            'f"Earth\'s Hill Sphere (extends to about {EARTH_HILL_SPHERE_RADII:.0f} Earth radii or about {EARTH_HILL_SPHERE_KM / 1e6:.1f} million km)<br><br>"\n                "The Hill sphere is the region around a body where its own gravity is the dominant force in attracting satellites. For <br>" \n                "a planet orbiting a star, it\'s the region where the planet\'s gravity is stronger than the star\'s tidal forces.<br><br>" \n                "The Hill Sphere radius can be described in words as follows: it is equal to the planet\'s average distance from the <br>" \n                "Sun (its orbital semi-major axis) multiplied by the cube root of the ratio between the planet\'s mass and three times <br>" \n                "the Sun\'s mass. In other words, you take how far the planet orbits out from the Sun, then scale that distance by the <br>" \n                "cube root of (planet mass / [3 x solar mass]) to find the boundary within which the planet\'s gravity dominates over the Sun\'s."',
            'f"Earth\'s Hill Sphere (extends to about {EARTH_HILL_SPHERE_RADII:.0f} Earth radii or about {EARTH_HILL_SPHERE_KM / 1e6:.1f} million km)<br><br>"\n                "The Hill sphere is the region around a body where its own gravity is the dominant force in attracting satellites. For <br>" \n                "a planet orbiting a star, it\'s the region where the planet\'s gravity is stronger than the star\'s tidal forces.<br><br>" \n                "The Hill Sphere radius can be described in words as follows: it is equal to the planet\'s average distance from the <br>" \n                "Sun (its orbital semi-major axis) multiplied by the cube root of the ratio between the planet\'s mass and three times <br>" \n                "the Sun\'s mass. In other words, you take how far the planet orbits out from the Sun, then scale that distance by the <br>" \n                "cube root of (planet mass / [3 x solar mass]) to find the boundary within which the planet\'s gravity dominates over the Sun\'s."\n                "<br><br>Source (radius): derived from GM_Earth (IERS Conventions 2010) and GM_Sun (IAU 2015 B3) at a = 1 AU."',
            1,
        ),
        # magnetosphere tooltip: same two belt lines, tooltip form
        (
            "                \"Inner Van Allen Belt: Region of trapped charged particles (mainly protons)\\n\"\n"
            "                \"extending from about 1,000 km to 6,000 km above Earth's surface.\\n\"\n"
            "                \"Outer Van Allen Belt: Region of trapped charged particles (mainly electrons)\\n\"\n"
            "                \"extending from about 13,000 km to 60,000 km above Earth's surface.\\n\\n\"\n",
            "                f\"Inner Van Allen Belt: trapped protons, drawn at the flux peak {EARTH_VAN_ALLEN_INNER_RADII:g} Earth radii out\\n\"\n"
            "                \"(Baker et al. 2018). Outer Van Allen Belt: trapped electrons, drawn at the flux peak\\n\"\n"
            "                f\"{EARTH_VAN_ALLEN_OUTER_RADII:g} Earth radii out (doi:10.1029/2024JA033504).\\n\"\n"
            "                \"Standoffs: Shue et al. (1998); Lugaz et al. (2016).\\n\\n\"\n",
            1,
        ),
    ],
}

# The tooltip edit needs two belt constants shell_configs does not yet import.
IMPORT_OLD = "    EARTH_MAGNETOPAUSE_STANDOFF_RADII, EARTH_BOW_SHOCK_STANDOFF_RADII,\n    EARTH_LEO_LOWER_ALTITUDE_KM,"
IMPORT_NEW = ("    EARTH_MAGNETOPAUSE_STANDOFF_RADII, EARTH_BOW_SHOCK_STANDOFF_RADII,\n"
              "    EARTH_VAN_ALLEN_INNER_RADII, EARTH_VAN_ALLEN_OUTER_RADII,\n"
              "    EARTH_LEO_LOWER_ALTITUDE_KM,")
EDITS["shell_configs.py"].insert(0, (IMPORT_OLD, IMPORT_NEW, 1))


def main():
    texts = {}
    for name, md5 in FILES.items():
        lf = (ROOT / name).read_bytes().replace(b"\r\n", b"\n")
        got = hashlib.md5(lf).hexdigest()
        if got != md5:
            print("STOP: %s md5 (LF) is %s, expected %s (file at 5170bec1)." % (name, got, md5))
            print("      Either this patch already ran or the file moved. Nothing written.")
            return 1
        texts[name] = lf.decode("utf-8")
    for name, edits in EDITS.items():
        t = texts[name]
        for i, (old, new, n) in enumerate(edits, 1):
            c = t.count(old)
            if c != n:
                print("STOP: %s edit %d matched %d time(s), expected %d. Nothing written." % (name, i, c, n))
                print("      old text begins: %r" % old[:70])
                return 1
            new.encode("ascii")
            t = t.replace(old, new)
        texts[name] = t
    for name, t in texts.items():
        (ROOT / name).write_bytes(t.encode("utf-8"))
        print("Patched %-30s %2d edit(s), new md5 (LF) %s" %
              (name, len(EDITS[name]), hashlib.md5(t.encode("utf-8")).hexdigest()))
    print("Source lines added: inner core, outer core, lower mantle, upper mantle,")
    print("  crust, lower/upper atmosphere (already), magnetosphere, bow shock,")
    print("  inner belt, outer belt, LEO, geostationary (already), Hill sphere.")
    print("Replaced: the two belt altitude ranges (unsourceable) with sourced peaks.")
    print("Next: read any Earth hover in the orrery; provenance_scanner.py; commit; push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
