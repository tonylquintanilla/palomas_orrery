"""
patch_L291_3_earth_atmosphere_physical.py -- Earth's atmosphere shells draw the store (L-291 / L-295)

Built on orrery fe87147f3204b1997181fea83070036ae6cd250e
at https://github.com/tonylquintanilla/palomas_orrery (main).

WHAT THIS DOES
  SHELL_CONFIGS['Earth'] drew the lower atmosphere at 1.05 radii (about
  319 km up) and the upper atmosphere at 1.25 radii (about 1,595 km up),
  while their own hover text ended at the 50 km stratopause and "about
  1,000 km". Tony's ruling, 2026-09-07: remove the drawing choice and
  draw the physical boundary, as the Sun's chromosphere already does
  (CHROMOSPHERE_PHYSICAL_RADII). That closes L-295.

  Changes, all in shell_configs.py:
    - 'atmosphere'       radius_fraction 1.05 -> EARTH_STRATOPAUSE_RADII (1.0078)
    - 'upper_atmosphere' radius_fraction 1.25 -> EARTH_THERMOPAUSE_RADII (1.0941)
    - both declare info_polar_deg so their info markers clear the crust's:
      the interior-to-atmosphere stack is now upper mantle at the pole,
      crust at 10 deg, lower atmosphere at 20 deg, upper atmosphere at 30
      deg, each at its own radius (the build_sphere_shell mechanism the
      crust introduced under L-249).
    - the hover and tooltip quote the store altitudes and say where the
      exosphere is, since the shell no longer claims to include it
    - imports and a docstring credit line

  THIS CHANGES THE DRAWN SHAPE. Both shells now sit close to the crust:
  the lower one 0.8% above it, the upper one 9%. That is what the
  atmosphere is. Mode 5.

  NOT touched: the two DEAD atmosphere builders in
  earth_visualization_shells.py (L-254). They render nothing.

HOW TO RUN
  Save to the repo root. Open in VS Code and press Run. It prints what it
  did and refuses to run twice. Then open the orrery, turn on Earth's
  crust, lower atmosphere and upper atmosphere, and look -- and hover
  the three info markers to confirm they are separate.

GUARDS
  shell_configs.py read in binary mode, LF-normalised, md5 checked against
  the value at fe87147f. Every edit must match its expected count or
  nothing is written. Inserted text is ASCII-only, LF line endings.

Written September 2026 with Anthropic's Claude Fable 5.1.
"""
import hashlib
import sys
from pathlib import Path

TARGET = Path(__file__).resolve().parent / "shell_configs.py"
EXPECTED_MD5 = "0a306a54f1b4fd3fd18cf71deee93d17"

LOWER_HOVER = (
    "                f\"The lower atmosphere is drawn to the stratopause, {EARTH_STRATOPAUSE_ALTITUDE_KM:,.0f} km up<br>\"\n"
    "                \"(NOAA JetStream; NASA). It holds the troposphere (0-12 km) where weather occurs, and<br>\"\n"
    "                \"the stratosphere (12-50 km) which contains the ozone layer. These regions contain<br>\"\n"
    "                \"99% of atmospheric mass, primarily nitrogen and oxygen. Temperature varies from<br>\"\n"
    "                \"about 15 degC (59 degF) at sea level to -60 degC (-76 degF) at the tropopause (12 km).<br>\"\n"
    "                \"The stratopause (50 km) warms to near 0 degC (32 degF) due to ozone absorption.\"\n"
)
LOWER_TOOLTIP = LOWER_HOVER.replace("<br>", "\\n")

UPPER_HOVER = (
    "                f\"The upper atmosphere is drawn from the stratopause ({EARTH_STRATOPAUSE_ALTITUDE_KM:,.0f} km) to the<br>\"\n"
    "                f\"thermopause, about {EARTH_THERMOPAUSE_ALTITUDE_KM:,.0f} km up (NOAA JetStream; NASA). It includes<br>\"\n"
    "                \"the mesosphere where meteors burn up and the thermosphere where the aurora occurs and<br>\"\n"
    "                \"the International Space Station orbits. In the thermosphere, temperatures can reach<br>\"\n"
    "                \"2,000 degC (3,600 degF), though the gas is so thin that it would feel cold to human skin.<br>\"\n"
    "                \"Above the thermopause the exosphere thins into space with no boundary; its hydrogen<br>\"\n"
    "                f\"halo, the geocorona, is detected past {EARTH_GEOCORONA_RADII:.0f} Earth radii.\"\n"
)
UPPER_TOOLTIP = UPPER_HOVER.replace("<br>", "\\n")

EDITS = [
    # imports (the L-291 block patch 2 added)
    (
        "    EARTH_HILL_SPHERE_KM, EARTH_HILL_SPHERE_RADII,\n)\n",
        "    EARTH_HILL_SPHERE_KM, EARTH_HILL_SPHERE_RADII,\n"
        "    # L-295: the atmosphere shells draw their sourced boundaries.\n"
        "    EARTH_STRATOPAUSE_ALTITUDE_KM, EARTH_STRATOPAUSE_RADII,\n"
        "    EARTH_THERMOPAUSE_ALTITUDE_KM, EARTH_THERMOPAUSE_RADII,\n"
        "    EARTH_GEOCORONA_RADII,\n"
        ")\n",
        1,
    ),
    # docstring credit
    (
        "    moved to its sourced radius. Found by Mode 5, not by any checker.)\n\"\"\"\n",
        "    moved to its sourced radius. Found by Mode 5, not by any checker.)\n"
        "Module updated: September 7, 2026 with Anthropic's Claude Fable 5.1 (L-295:\n"
        "    Earth's two atmosphere shells stop drawing at 1.05 and 1.25 radii,\n"
        "    which were visibility choices their own hover contradicted, and draw\n"
        "    the stratopause and thermopause from constants_new.py, as the Sun's\n"
        "    chromosphere does. Their info markers step to 20 and 30 degrees so\n"
        "    the interior-to-atmosphere stack reads as four separate markers.\n"
        "    Tony's ruling, 2026-09-07.)\n\"\"\"\n",
        1,
    ),
    # lower atmosphere
    (
        "        'atmosphere': {\n"
        "            'name': 'Lower Atmosphere',\n"
        "            'radius_fraction': 1.05,\n",
        "        'atmosphere': {\n"
        "            'name': 'Lower Atmosphere',\n"
        "            'radius_fraction': EARTH_STRATOPAUSE_RADII,  # L-295: was 1.05, a drawing choice\n"
        "            'info_polar_deg': 20.0,  # clears the crust's marker at 10\n",
        1,
    ),
    (
        "            'hover_text': (\n"
        "                \"The lower atmosphere includes the troposphere (0-12 km) where weather occurs, and<br>\"\n"
        "                \"the stratosphere (12-50 km) which contains the ozone layer. These regions contain<br>\"\n"
        "                \"99% of atmospheric mass, primarily nitrogen and oxygen. Temperature varies from<br>\"\n"
        "                \"about 15 degC (59 degF) at sea level to -60 degC (-76 degF) at the tropopause (12 km).<br>\"\n"
        "                \"The stratopause (50 km) warms to near 0 degC (32 degF) due to ozone absorption.\"\n"
        "            ),\n"
        "            'tooltip': (\n"
        "                \"The lower atmosphere includes the troposphere (0-12 km) where weather occurs, and\\n\"\n"
        "                \"the stratosphere (12-50 km) which contains the ozone layer. These regions contain\\n\"\n"
        "                \"99% of atmospheric mass, primarily nitrogen and oxygen. Temperature varies from\\n\"\n"
        "                \"about 15 degC (59 degF) at sea level to -60 degC (-76 degF) at the tropopause (12 km).\\n\"\n"
        "                \"The stratopause (50 km) warms to near 0 degC (32 degF) due to ozone absorption.\"\n"
        "            ),\n",
        "            'hover_text': (\n" + LOWER_HOVER + "            ),\n"
        "            'tooltip': (\n" + LOWER_TOOLTIP + "            ),\n",
        1,
    ),
    # upper atmosphere
    (
        "        'upper_atmosphere': {\n"
        "            'name': 'Upper Atmosphere',\n"
        "            'radius_fraction': 1.25,\n",
        "        'upper_atmosphere': {\n"
        "            'name': 'Upper Atmosphere',\n"
        "            'radius_fraction': EARTH_THERMOPAUSE_RADII,  # L-295: was 1.25, a drawing choice\n"
        "            'info_polar_deg': 30.0,  # clears the lower atmosphere's marker at 20\n",
        1,
    ),
    (
        "            'hover_text': (\n"
        "                \"The upper atmosphere extends from 50 km to about 1,000 km altitude. It includes<br>\"\n"
        "                \"the mesosphere where meteors burn up, the thermosphere where the aurora occurs and<br>\"\n"
        "                \"the International Space Station orbits, and the exosphere which gradually transitions<br>\"\n"
        "                \"to space. In the thermosphere, temperatures can reach 2,000 degC (3,600 degF), though the<br>\"\n"
        "                \"gas is so thin that it would feel cold to human skin.\"\n"
        "            ),\n"
        "            'tooltip': (\n"
        "                \"The upper atmosphere extends from 50 km to about 1,000 km altitude. It includes\\n\"\n"
        "                \"the mesosphere where meteors burn up, the thermosphere where the aurora occurs and\\n\"\n"
        "                \"the International Space Station orbits, and the exosphere which gradually transitions\\n\"\n"
        "                \"to space. In the thermosphere, temperatures can reach 2,000 degC (3,600 degF), though the\\n\"\n"
        "                \"gas is so thin that it would feel cold to human skin.\"\n"
        "            ),\n",
        "            'hover_text': (\n" + UPPER_HOVER + "            ),\n"
        "            'tooltip': (\n" + UPPER_TOOLTIP + "            ),\n",
        1,
    ),
]


def main():
    lf = TARGET.read_bytes().replace(b"\r\n", b"\n")
    got = hashlib.md5(lf).hexdigest()
    if got != EXPECTED_MD5:
        print("STOP: shell_configs.py md5 (LF) is %s, expected %s (file at fe87147f)." % (got, EXPECTED_MD5))
        print("      Either this patch already ran or the file moved. Nothing written.")
        return 1
    text = lf.decode("utf-8")
    for i, (old, new, n) in enumerate(EDITS, 1):
        c = text.count(old)
        if c != n:
            print("STOP: edit %d matched %d time(s), expected %d. Nothing written." % (i, c, n))
            print("      old text begins: %r" % old[:70])
            return 1
        new.encode("ascii")
        text = text.replace(old, new)
    TARGET.write_bytes(text.encode("utf-8"))
    print("Patched shell_configs.py: %d edits, new md5 (LF) %s" %
          (len(EDITS), hashlib.md5(text.encode("utf-8")).hexdigest()))
    print("Earth lower atmosphere: 1.05 -> EARTH_STRATOPAUSE_RADII (1.0078), marker at 20 deg")
    print("Earth upper atmosphere: 1.25 -> EARTH_THERMOPAUSE_RADII (1.0941), marker at 30 deg")
    print("Next: orrery -> Earth crust + both atmospheres on, hover all three markers;")
    print("  then provenance_scanner.py, commit, push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
