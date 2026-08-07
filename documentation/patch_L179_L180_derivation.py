"""
patch_L179_L180_derivation.py

Closes L-179 (solar gravitational influence: 126,000 vs 150,000 AU) and
L-180 (solar chromosphere: three inconsistent extents) by making every
displayed figure DERIVE from constants_new.py instead of being typed.

Built on 6623c696969e4c6a2245b51826f6cf04cce276f5 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).

HOW TO RUN
    Save this file into the palomas_orrery folder (the same folder that
    holds constants_new.py), open it in VS Code, and click Run.
    Equivalent command line: python patch_L179_L180_derivation.py

WHAT IT DOES
    constants_new.py
        + AU_PER_LIGHT_YEAR              (derived from existing primaries)
        + GRAVITATIONAL_INFLUENCE_RANGE_AU = (100000, 200000)
        + CHROMOSPHERE_PHYSICAL_KM = 2000.0
        + CHROMOSPHERE_PHYSICAL_RADII    (derived)
    planet_visualization_utilities.py
        re-exports the four new names
    solar_visualization_shells.py
        + two shared sentence fragments, built by interpolation
        four display sites now reference the fragments instead of typing
        numbers; three false # Source: citations corrected
    palomas_orrery.py
        scale-suggestion tooltip interpolates the constant it already imports
    test_constants_provenance.py
        stale assertion corrected; range assertion added

SAFETY
    Every file is fingerprinted (MD5) before any write, and every anchor
    must match EXACTLY ONCE. Any mismatch aborts the whole run with
    NOTHING WAS WRITTEN -- no file is touched unless all of them can be.
    Binary mode throughout, so line endings and encoding are preserved.

Module updated: August 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import pathlib
import sys

# ------------------------------------------------------------------
# Base fingerprints -- the exact bytes this patch was written against.
# ------------------------------------------------------------------
FINGERPRINTS = {
    'constants_new.py':                 'eb014dcbb96555e62bfdb77a9a85976c',
    'planet_visualization_utilities.py': 'ff05aa77132ee79256e71e858073edda',
    'solar_visualization_shells.py':     '3557a6dea9d80f31ace060ddc4d8d7cd',
    'palomas_orrery.py':                 '7a90ca01bd45e26d6b6e6f5033a7dfca',
    'test_constants_provenance.py':      '835b65972e67f4e1e24d3b39655e6910',
}

EDITS = {}

# ==================================================================
# 1. constants_new.py
# ==================================================================
EDITS['constants_new.py'] = [
    (
        "add AU_PER_LIGHT_YEAR (derived)",
        b"LIGHT_MINUTES_PER_AU = KM_PER_AU / SPEED_OF_LIGHT_KM_S / 60.0\n"
        b"# Derived: 149597870.7 / 299792.458 / 60 = 8.31675...\n"
        b"# Previous hardcoded value was 8.3167 (consistent to 5 sig figs)\n",

        b"LIGHT_MINUTES_PER_AU = KM_PER_AU / SPEED_OF_LIGHT_KM_S / 60.0\n"
        b"# Derived: 149597870.7 / 299792.458 / 60 = 8.31675...\n"
        b"# Previous hardcoded value was 8.3167 (consistent to 5 sig figs)\n"
        b"\n"
        b"AU_PER_LIGHT_YEAR = (SPEED_OF_LIGHT_KM_S * 365.25 * 86400.0) / KM_PER_AU\n"
        b"# Derived: 299792.458 km/s x Julian year (365.25 d x 86400 s) / KM_PER_AU\n"
        b"#          = 63,241.077 AU per light-year\n"
        b"# Source: IAU -- the light-year is defined as c x the Julian year.\n"
        b"# Ref: https://www.iau.org/public/themes/measuring/\n"
        b"# Note: reproduces the IAU published light-year (9.4607304726e12 km)\n"
        b"#       to ten significant figures. Added 2026-08-07 (L-179) so that\n"
        b"#       display text can derive light-year figures instead of typing\n"
        b"#       them beside an AU value that then drifts away from them.\n",
    ),
    (
        "add chromosphere physical extent as data",
        b"CHROMOSPHERE_RADII = 1.1\n"
        b"# Visualization shell radius (physical chromosphere extends ~2000 km above\n"
        b"# photosphere = ~1.003 R_sun; drawn at 1.1 for visibility at orrery scale)\n",

        b"CHROMOSPHERE_RADII = 1.1\n"
        b"# Visualization shell radius (physical chromosphere extends ~2000 km above\n"
        b"# photosphere = ~1.003 R_sun; drawn at 1.1 for visibility at orrery scale)\n"
        b"# DRAWN value, deliberately larger than physical -- see\n"
        b"# CHROMOSPHERE_PHYSICAL_KM below, and say so in any display text\n"
        b"# (Tony's ruling, 2026-08-07, L-180).\n",
    ),
    (
        "add CHROMOSPHERE_PHYSICAL_KM and its derived radii figure",
        b"# Cross-checked: NASA chromosphere data via GPT 2026-08-02 (constants_remaining_independent_verification_gpt.md)\n"
        b"\n"
        b"INNER_CORONA_RADII = 3\n",

        b"# Cross-checked: NASA chromosphere data via GPT 2026-08-02 (constants_remaining_independent_verification_gpt.md)\n"
        b"\n"
        b"CHROMOSPHERE_PHYSICAL_KM = 2000.0\n"
        b"# Source: Carroll & Ostlie, An Introduction to Modern Astrophysics,\n"
        b"#         Ch. 11 -- chromosphere extends ~2000 km above the photosphere.\n"
        b"# Cross-checked: Carroll & Ostlie via Gemini 2026-08-02 (Gemini worksheet)\n"
        b"# Note: the PHYSICAL extent. CHROMOSPHERE_RADII (1.1) is the DRAWN\n"
        b"#       shell radius, ~36x thicker, chosen for visibility at orrery\n"
        b"#       scale. Both figures are real; they answer different questions.\n"
        b"\n"
        b"CHROMOSPHERE_PHYSICAL_RADII = 1.0 + CHROMOSPHERE_PHYSICAL_KM / SUN_RADIUS_KM\n"
        b"# Derived: 1 + 2000 / 695700 = 1.002875... solar radii\n"
        b"\n"
        b"INNER_CORONA_RADII = 3\n",
    ),
    (
        "add GRAVITATIONAL_INFLUENCE_RANGE_AU beside the value",
        b"# Corrected 2026-08-02: 126000 -> 150000 (prior value unsourced;\n"
        b"#   150000 AU is a round midpoint of the published range)\n",

        b"# Corrected 2026-08-02: 126000 -> 150000 (prior value unsourced;\n"
        b"#   150000 AU is a round midpoint of the published range)\n"
        b"# Confirmed 2026-08-07 (Tony, L-179): 150000 stands, chosen as the\n"
        b"#   midpoint of the published range below. Display text must carry\n"
        b"#   the RANGE, not present the midpoint as a measurement.\n"
        b"\n"
        b"GRAVITATIONAL_INFLUENCE_RANGE_AU = (100000, 200000)\n"
        b"# Source: spread of published Sun-in-Galaxy Hill sphere estimates;\n"
        b"#         model-dependent, varying with assumed enclosed galactic mass\n"
        b"#         and the Sun's galactocentric distance.\n"
        b"# Note: 100,000-200,000 AU = 1.6-3.2 light-years. Stored as DATA rather\n"
        b"#       than prose so display strings can interpolate the envelope\n"
        b"#       instead of restating the midpoint alone (L-179, 2026-08-07).\n",
    ),
]

# ==================================================================
# 2. planet_visualization_utilities.py -- re-export the new names
# ==================================================================
EDITS['planet_visualization_utilities.py'] = [
    (
        "re-export AU_PER_LIGHT_YEAR from the store",
        b"    # Solar structure\n"
        b"    SOLAR_RADIUS_AU, CORE_AU, RADIATIVE_ZONE_AU,\n"
        b"    # Solar atmosphere (in solar radii)\n"
        b"    CHROMOSPHERE_RADII, INNER_CORONA_RADII, OUTER_CORONA_RADII,\n",

        b"    # Unit conversions\n"
        b"    AU_PER_LIGHT_YEAR,\n"
        b"    # Solar structure\n"
        b"    SOLAR_RADIUS_AU, CORE_AU, RADIATIVE_ZONE_AU,\n"
        b"    # Solar atmosphere (in solar radii)\n"
        b"    CHROMOSPHERE_RADII, INNER_CORONA_RADII, OUTER_CORONA_RADII,\n"
        b"    CHROMOSPHERE_PHYSICAL_KM, CHROMOSPHERE_PHYSICAL_RADII,\n",
    ),
    (
        "re-export GRAVITATIONAL_INFLUENCE_RANGE_AU",
        b"    GRAVITATIONAL_INFLUENCE_AU,\n"
        b")\n",

        b"    GRAVITATIONAL_INFLUENCE_AU, GRAVITATIONAL_INFLUENCE_RANGE_AU,\n"
        b")\n",
    ),
]

# ==================================================================
# 3. solar_visualization_shells.py
# ==================================================================
EDITS['solar_visualization_shells.py'] = [
    (
        "import the new names",
        b"                                            INNER_LIMIT_OORT_CLOUD_AU, INNER_OORT_CLOUD_AU, OUTER_OORT_CLOUD_AU, \n"
        b"                                            GRAVITATIONAL_INFLUENCE_AU)\n",

        b"                                            INNER_LIMIT_OORT_CLOUD_AU, INNER_OORT_CLOUD_AU, OUTER_OORT_CLOUD_AU, \n"
        b"                                            GRAVITATIONAL_INFLUENCE_AU, GRAVITATIONAL_INFLUENCE_RANGE_AU,\n"
        b"                                            AU_PER_LIGHT_YEAR,\n"
        b"                                            CHROMOSPHERE_PHYSICAL_KM, CHROMOSPHERE_PHYSICAL_RADII)\n",
    ),
    (
        "define the two shared fragments; fix the first false citation",
        b"# Source: GRAVITATIONAL_INFLUENCE_AU=126000 in constants_new.py; NASA Solar System Exploration\n"
        b"gravitational_influence_info = (\n",

        b"#####################################\n"
        b"# Shared derived sentences (L-179 / L-180, 2026-08-07)\n"
        b"#####################################\n"
        b"# Each figure below is interpolated from constants_new.py, never typed.\n"
        b"# One fragment, referenced by every string that states the fact, so the\n"
        b"# statement exists once and cannot drift from the constant or from its\n"
        b"# own duplicate. Editing the constant updates every display site.\n"
        b"\n"
        b"# Source: GRAVITATIONAL_INFLUENCE_AU and GRAVITATIONAL_INFLUENCE_RANGE_AU\n"
        b"#         in constants_new.py -- approximate Hill sphere of the Sun in the\n"
        b"#         Milky Way, model-dependent. Published estimates span\n"
        b"#         100,000-200,000 AU; the visualization draws the 150,000 AU\n"
        b"#         midpoint (Tony's ruling, 2026-08-07). Light-year figures derive\n"
        b"#         from AU_PER_LIGHT_YEAR. NASA Solar System Exploration.\n"
        b"GRAVITATIONAL_INFLUENCE_SENTENCE = (\n"
        b"    f\"The Sun's gravitational influence extends to roughly \"\n"
        b"    f\"{GRAVITATIONAL_INFLUENCE_AU / AU_PER_LIGHT_YEAR:.1f} light-years \"\n"
        b"    f\"(~{GRAVITATIONAL_INFLUENCE_AU:,.0f} AU). Published estimates range \"\n"
        b"    f\"{GRAVITATIONAL_INFLUENCE_RANGE_AU[0]:,.0f}-\"\n"
        b"    f\"{GRAVITATIONAL_INFLUENCE_RANGE_AU[1]:,.0f} AU \"\n"
        b"    f\"({GRAVITATIONAL_INFLUENCE_RANGE_AU[0] / AU_PER_LIGHT_YEAR:.1f}-\"\n"
        b"    f\"{GRAVITATIONAL_INFLUENCE_RANGE_AU[1] / AU_PER_LIGHT_YEAR:.1f} \"\n"
        b"    f\"light-years); this visualization draws the midpoint.\"\n"
        b")\n"
        b"\n"
        b"# Source: CHROMOSPHERE_RADII (drawn) and CHROMOSPHERE_PHYSICAL_KM /\n"
        b"#         CHROMOSPHERE_PHYSICAL_RADII (physical) in constants_new.py;\n"
        b"#         Carroll & Ostlie Ch. 11 for the ~2000 km physical extent.\n"
        b"#         The drawn shell is a declared stylization for visibility at\n"
        b"#         orrery scale and the text says so (L-180, 2026-08-07).\n"
        b"CHROMOSPHERE_RADIUS_LINE = (\n"
        b"    f\"* Radius: drawn from the photosphere out to \"\n"
        b"    f\"{CHROMOSPHERE_RADII} solar radii \"\n"
        b"    f\"(~{SOLAR_RADIUS_AU:.5f} - {CHROMOSPHERE_RADII * SOLAR_RADIUS_AU:.5f} AU). \"\n"
        b"    f\"This is a stylization for visibility: the physical chromosphere \"\n"
        b"    f\"extends only ~{CHROMOSPHERE_PHYSICAL_KM:,.0f} km above the \"\n"
        b"    f\"photosphere (~{CHROMOSPHERE_PHYSICAL_RADII:.3f} solar radii).<br>\"\n"
        b")\n"
        b"\n"
        b"# Source: GRAVITATIONAL_INFLUENCE_SENTENCE above (derived); NASA Solar\n"
        b"#         System Exploration for the heliopause and Oort Cloud framing.\n"
        b"gravitational_influence_info = (\n",
    ),
    (
        # BOTH copies -- the checkbox tooltip and the 3D marker hover carry
        # this identical pair of lines. They get the identical replacement,
        # so one edit with an expected count of 2 is clearer (and safer)
        # than two long anchors distinguished only by distant context.
        "both duplicate sites now reference the fragment",
        b"            \"Oort Cloud (2,000-20,000 AU), and the Outer Oort Cloud (20,000-100,000 AU). The Sun's gravitational influence<br>\" \n"
        b"            \"extends to about 2 light-years (~126,000 AU).<br><br>\" \n",

        b"            \"Oort Cloud (2,000-20,000 AU), and the Outer Oort Cloud (20,000-100,000 AU).<br><br>\" \n"
        b"            + GRAVITATIONAL_INFLUENCE_SENTENCE + \"<br><br>\"\n",
        2,
    ),
    (
        "drop the false constant claim from the galactic tide citation",
        b"# Source: Dones et al. (2004) Comets II -- galactic tidal sculpting of Oort Cloud; GRAVITATIONAL_INFLUENCE_AU=126000 in constants_new.py\n",

        b"# Source: Dones et al. (2004) Comets II -- galactic tidal sculpting of Oort Cloud.\n"
        b"# Note: this string states no gravitational-influence figure; the previous\n"
        b"#       citation asserted a gravitational-influence value of 126,000 AU\n"
        b"#       here, which was both wrong and irrelevant to the text below\n"
        b"#       (removed L-179).\n",
    ),
    (
        "chromosphere citation: 1.5 -> 1.1, drawn-vs-physical recorded",
        b"# Source: constants_new.py CHROMOSPHERE_RADII=1.5; Golub & Pasachoff (2010) The Solar Corona\n",

        b"# Source: constants_new.py CHROMOSPHERE_RADII=1.1 (DRAWN shell radius, a\n"
        b"#         declared stylization for visibility) and CHROMOSPHERE_PHYSICAL_KM\n"
        b"#         =2000 (physical extent, Carroll & Ostlie Ch. 11, ~1.003 R_sun);\n"
        b"#         Golub & Pasachoff (2010) The Solar Corona.\n"
        b"# Note: the previous citation asserted a chromosphere radius of 1.5 solar\n"
        b"#       radii, which the store has not held since 2026-08-02\n"
        b"#       (corrected L-180).\n",
    ),
    (
        "chromosphere radius line, tooltip copy",
        b"            \"* Radius: from Photosphere to 1.5 Solar radii or ~0.00465 - 0.0070 AU<br>\"\n"
        b"            \"* Temperature: ~6,000 to 20,000 K, for a average of 10,000 K<br>\"\n"
        b"            \"* Radiates at an average peak wavelength of ~290 nm, ultraviolet range, invisible.\"\n"
        b"        )\n"
        b"\n"
        b"# Source: NASA Solar System Exploration (solarsystem.nasa.gov/solar-system/sun); SUN_RADIUS_KM=695700 in constants_new.py\n",

        b"            + CHROMOSPHERE_RADIUS_LINE +\n"
        b"            \"* Temperature: ~6,000 to 20,000 K, for a average of 10,000 K<br>\"\n"
        b"            \"* Radiates at an average peak wavelength of ~290 nm, ultraviolet range, invisible.\"\n"
        b"        )\n"
        b"\n"
        b"# Source: NASA Solar System Exploration (solarsystem.nasa.gov/solar-system/sun); SUN_RADIUS_KM=695700 in constants_new.py\n",
    ),
    (
        "chromosphere radius line, hover copy",
        b"            \"* Radius: from Photosphere to 1.5 Solar radii or ~0.00465 - 0.0070 AU<br>\"\n"
        b"            \"* Temperature: ~6,000 to 20,000 K, for a average of 10,000 K<br>\"\n"
        b"            \"* Radiates at an average peak wavelength of ~290 nm, ultraviolet range, invisible.\"\n"
        b"        )\n"
        b"\n"
        b"photosphere_info_hover = (\n",

        b"            + CHROMOSPHERE_RADIUS_LINE +\n"
        b"            \"* Temperature: ~6,000 to 20,000 K, for a average of 10,000 K<br>\"\n"
        b"            \"* Radiates at an average peak wavelength of ~290 nm, ultraviolet range, invisible.\"\n"
        b"        )\n"
        b"\n"
        b"photosphere_info_hover = (\n",
    ),
]

# ==================================================================
# 4. palomas_orrery.py -- scale tooltip interpolates the constant
# ==================================================================
EDITS['palomas_orrery.py'] = [
    (
        "scale tooltip: derive the Hill sphere figure from the constant",
        b"\"* Inner Limit of Oort Cloud: 2,000 AU\\n* Outer Limit of Oort Cloud: 100,000 AU\\n"
        b"* Extent of Solar Gravitational Influence (Hill Sphere): 126,000 AU\\n* Proxima Centauri: 268,585 AU\")\n",

        b"\"* Inner Limit of Oort Cloud: 2,000 AU\\n* Outer Limit of Oort Cloud: 100,000 AU\\n\"\n"
        b"# Source: GRAVITATIONAL_INFLUENCE_AU in constants_new.py, imported above.\n"
        b"#         Interpolated rather than typed: this site carried a stale 126,000\n"
        b"#         literal with no link to the store until 2026-08-07 (L-179).\n"
        b"f\"* Extent of Solar Gravitational Influence (Hill Sphere): \"\n"
        b"f\"{GRAVITATIONAL_INFLUENCE_AU:,.0f} AU\\n* Proxima Centauri: 268,585 AU\")\n",
    ),
]

# ==================================================================
# 5. test_constants_provenance.py
# ==================================================================
EDITS['test_constants_provenance.py'] = [
    (
        "correct the stale assertion and add the range guard",
        b"def test_gravitational_influence_au():\n"
        b"    \"\"\"Approximate Hill sphere radius of Sun in Milky Way (~2 light-years).\"\"\"\n"
        b"    assert GRAVITATIONAL_INFLUENCE_AU == 126000, \\\n"
        b"        f\"GRAVITATIONAL_INFLUENCE_AU drifted to {GRAVITATIONAL_INFLUENCE_AU}\"\n",

        b"def test_gravitational_influence_au():\n"
        b"    \"\"\"Approximate Hill sphere radius of Sun in Milky Way (~2.4 light-years).\n"
        b"\n"
        b"    Two assertions, catching different things. The equality is a tripwire:\n"
        b"    it fires on ANY change, so a deliberate edit has to be acknowledged\n"
        b"    here. The range is a guard: it stays quiet for any value the published\n"
        b"    literature supports and fires only when a value leaves that envelope.\n"
        b"    A considered move to 152,000 trips the tripwire alone; a typo of\n"
        b"    15,000 trips both.\n"
        b"\n"
        b"    Corrected 2026-08-07 (L-179): this asserted 126000, which the store\n"
        b"    stopped holding on 2026-08-02. It was false for five days and nothing\n"
        b"    surfaced it, because this file is not on any run path. Per L-160 it\n"
        b"    retires once L-155's pinning engine absorbs these checks into\n"
        b"    provenance_scanner.py -- until then, treat these two assertions as the\n"
        b"    written spec for what the scanner should absorb.\n"
        b"    \"\"\"\n"
        b"    assert GRAVITATIONAL_INFLUENCE_AU == 150000, \\\n"
        b"        f\"GRAVITATIONAL_INFLUENCE_AU drifted to {GRAVITATIONAL_INFLUENCE_AU}\"\n"
        b"    low, high = GRAVITATIONAL_INFLUENCE_RANGE_AU\n"
        b"    assert low <= GRAVITATIONAL_INFLUENCE_AU <= high, \\\n"
        b"        (f\"GRAVITATIONAL_INFLUENCE_AU {GRAVITATIONAL_INFLUENCE_AU} is outside \"\n"
        b"         f\"the published range {low}-{high} AU\")\n",
    ),
    (
        "import the range constant used by the new assertion",
        b"    GRAVITATIONAL_INFLUENCE_AU,\n",

        b"    GRAVITATIONAL_INFLUENCE_AU,\n"
        b"    GRAVITATIONAL_INFLUENCE_RANGE_AU,\n",
    ),
]


# ==================================================================
# Harness -- verify everything, then write everything.
# ==================================================================
def main():
    here = pathlib.Path(__file__).parent
    staged = {}
    problems = []

    for name, fp_expected in FINGERPRINTS.items():
        path = here / name
        if not path.exists():
            problems.append(f"MISSING: {name} (run this from the palomas_orrery folder)")
            continue

        data = path.read_bytes()
        fp_actual = hashlib.md5(data).hexdigest()
        if fp_expected.startswith('__') or fp_actual != fp_expected:
            if not fp_expected.startswith('__'):
                problems.append(
                    f"BASE MOVED: {name}\n"
                    f"    expected MD5 {fp_expected}\n"
                    f"    actual   MD5 {fp_actual}\n"
                    f"    This patch was built against different bytes. Do not force it."
                )
                continue

        for edit in EDITS.get(name, []):
            label, old, new = edit[0], edit[1], edit[2]
            expected = edit[3] if len(edit) > 3 else 1
            count = data.count(old)
            if count != expected:
                problems.append(
                    f"ANCHOR {count} MATCHES (expected {expected}): {name} -- {label}\n"
                    f"    first 70 bytes: {old[:70]!r}"
                )
            else:
                data = data.replace(old, new, expected)

        staged[name] = data

    if problems:
        print("\n".join(problems))
        print("\nNOTHING WAS WRITTEN.")
        return 1

    total = 0
    for name, data in staged.items():
        (here / name).write_bytes(data)
        for edit in EDITS.get(name, []):
            label = edit[0]
            print(f"  ok  {name} -- {label}")
        total += len(data)

    print(f"\npatch applied ({total} bytes across {len(staged)} files)")
    print("\nNext: run the orrery, open the Sun's Gravitational Influence and")
    print("Chromosphere shells, and read the hover text. Tony's eyes are the gate.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
