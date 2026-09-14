"""
patch_L305_item7_strings.py

L-305 item 7, part 2 of 3: the STRINGS. Points Earth's magnetosphere and
radiation-belt text at the store rows part 1 created, so no figure a
visitor reads is typed any more.

WHAT IT DOES (one file: earth_visualization_shells.py)
  1. Imports the five new rows from constants_new.py.
  2. Adds one helper, _km_above_surface(), right below the imports. It
     turns a geocentric distance in Earth radii into an altitude above the
     equatorial surface, rounded to two significant figures. Every
     kilometre figure in the text goes through it, so the rounding happens
     in the FORMAT and never as a number typed into a string.
  3. earth_magnetosphere_info (the Tk checkbox tooltip) loses both typed
     altitude pairs and gains derived ones, gains the observed magnetotail
     extent, and loses two claims the L-321 round did not support.
  4. magnetosphere_text (the Plotly hover) gains the tail sentence in the
     form the design record specifies -- the DRAWN length quoted from the
     drawing parameter, the OBSERVED extent from the store row, two homes
     in one sentence -- plus the seam between the two published fits,
     stated without a figure because the second fit's nose is not a row.
  5. belt_texts loses the two typed spans and gains the four edge rows,
     with a derived kilometre presentation labelled as a conversion. The
     outer belt's peak now reads as L with "at the equator" attached,
     because its unit moved to l_shell in part 1.
  6. Two retired "# Verified: April 2026 via Gemini fact-check" stamps go,
     on the two blocks this patch rewrites.

WHAT IT DOES NOT DO
  Eleven more of that retired stamp are elsewhere in this file (13 at
  HEAD, 11 after this patch) and are NOT touched. Forward-going on blocks touched; the rest is one ledger row by
  class, not a sweep (The Braid).
  The gallery's data/objects_config.json still holds its own copy of the
  span prose. That is part 3, in the other repository.

WHAT CHANGES ON SCREEN
  The information panel currently says the inner belt runs 1,000 to 6,000
  km and the outer 13,000 to 60,000 km. Derived from the store it reads
  roughly 640 to 6,400 km and roughly 13,000 to 38,000 km. The old pairs
  rest on a magazine article, a news article and a university outreach
  page; the new ones are arithmetic on sourced rows. The panel is being
  corrected, not merely reworded.
  Also gone: "making complex life possible", which three checker legs
  returned NO on against Griessmeier et al. (2016); and "solar radiation",
  which reads as sunlight and UV, from something that deflects particles.

HOW TO RUN IT (Tony)
  Save this file into the orrery repo root -- the same folder as
  earth_visualization_shells.py -- open it in VS Code, and click Run.
  Equivalent command: python patch_L305_item7_strings.py

  Success: seven "ok" lines, then "patch applied".
  Failure: one ERROR or ANCHOR FAIL line. NOTHING is written. Undo is
           Discard Changes in GitHub Desktop.

AFTER IT RUNS
  Run palomas_orrery.py, switch on Earth's magnetosphere and both
  radiation belts, and hover each one. That is the gate this patch cannot
  run for itself.

BASE
  Built on orrery 773e5c2d084f8e269abc5700d33928e530902b29 at
  https://github.com/tonylquintanilla/palomas_orrery
  Requires part 1 (patch_L305_item7_belt_rows.py) to have run: the
  imports this patch adds will not resolve without those rows.

Written September 14, 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

TARGET = "earth_visualization_shells.py"
BASE_FP = "e6d61be6a666289e1dd37f352f6261be"

# ---------------------------------------------------------------------------
# Edit 1 (lowest in the file): belt_texts and the comment block above it.
# ---------------------------------------------------------------------------

BELTS_OLD = b'''    # Source: NASA Van Allen Probes mission
    # Verified: April 2026 via Gemini fact-check
    belt_texts = [
        f"Inner Van Allen Belt: Region of trapped charged particles (mainly protons).<br>"
        f"Drawn at the flux peak, {EARTH_VAN_ALLEN_INNER_RADII:g} Earth radii from Earth's centre; the belt<br>"
        "spans roughly 1.1 to 2 Earth radii.<br>"
        "Source (peak): Baker et al. (2018), Space Sci. Rev. 214:17, doi:10.1007/s11214-017-0452-7.",
        f"Outer Van Allen Belt: Region of trapped charged particles (mainly electrons).<br>"
        f"Drawn at the flux peak, {EARTH_VAN_ALLEN_OUTER_RADII:g} Earth radii from Earth's centre; the belt<br>"
        "spans roughly 3 to 7 Earth radii and moves with geomagnetic activity.<br>"
        "Source (peak): J. Geophys. Res. Space Physics (2025), doi:10.1029/2024JA033504; Baker et al. (2018)."
    ]
'''

BELTS_NEW = b'''    # Source: every figure below interpolates a row in constants_new.py --
    # Source+: EARTH_VAN_ALLEN_INNER_RADII, EARTH_VAN_ALLEN_OUTER_RADII and
    # Source+: the four EARTH_VAN_ALLEN_*_EDGE rows, each carrying its own
    # Source+: citation and access route. The spans were typed here until
    # Source+: 2026-09-14, when L-305 item 7 gave them rows to read.
    # Source+: The kilometres are arithmetic on those rows, not a second
    # Source+: figure: see _km_above_surface() at the top of this module.
    belt_texts = [
        f"Inner Van Allen Belt: Region of trapped charged particles (mainly protons).<br>"
        f"Drawn at the flux peak, {EARTH_VAN_ALLEN_INNER_RADII:g} Earth radii from Earth's centre, about<br>"
        f"{_km_above_surface(EARTH_VAN_ALLEN_INNER_RADII, 2):,} km above the surface at the equator.<br>"
        f"The belt spans about {EARTH_VAN_ALLEN_INNER_BELT_INNER_EDGE:g} to {EARTH_VAN_ALLEN_INNER_BELT_OUTER_EDGE:g} Earth radii in the geomagnetic<br>"
        f"equatorial plane -- roughly {_km_above_surface(EARTH_VAN_ALLEN_INNER_BELT_INNER_EDGE, 2):,} to {_km_above_surface(EARTH_VAN_ALLEN_INNER_BELT_OUTER_EDGE, 1):,} km above the surface<br>"
        f"(every kilometre figure here converted from Earth radii).<br>"
        "Source (peak): Baker et al. (2018), Space Sci. Rev. 214:17, doi:10.1007/s11214-017-0452-7.<br>"
        "Source (extent): Meredith et al. (2014), J. Geophys. Res. Space Physics 119:5328.",
        f"Outer Van Allen Belt: Region of trapped charged particles (mainly electrons).<br>"
        f"Drawn at the flux peak, L = {EARTH_VAN_ALLEN_OUTER_RADII:g} -- about {_km_above_surface(EARTH_VAN_ALLEN_OUTER_RADII, 2):,} km above the<br>"
        "surface at the equator, where L equals geocentric distance in Earth radii.<br>"
        f"The belt spans about {EARTH_VAN_ALLEN_OUTER_BELT_INNER_EDGE:g} to {EARTH_VAN_ALLEN_OUTER_BELT_OUTER_EDGE:g} Earth radii and moves with geomagnetic<br>"
        f"activity -- roughly {_km_above_surface(EARTH_VAN_ALLEN_OUTER_BELT_INNER_EDGE, 1):,} to {_km_above_surface(EARTH_VAN_ALLEN_OUTER_BELT_OUTER_EDGE, 1):,} km above the surface<br>"
        f"(every kilometre figure here converted from Earth radii).<br>"
        "Source (peak): Li et al. (2025), doi:10.1029/2024JA033504 -- most intense across<br>"
        f"the L = 4 to 5 band; the drawn {EARTH_VAN_ALLEN_OUTER_RADII:g} is our midpoint of it.<br>"
        "Source (extent): Meredith et al. (2014); Li, Tu et al. (2024), doi:10.1029/2023JA032171."
    ]
'''

# ---------------------------------------------------------------------------
# Edit 7: bow_shock_text. Named in L-305 item 7 and skipped on the first
# pass, because the one change being hunted for -- the retired Lugaz
# midpoint sentence -- had already been removed by the item 4 patch.
# ---------------------------------------------------------------------------

BOWTEXT_OLD = b"""    bow_shock_text = ["Earth: Bow Shock<br><br>"
                "Bow Shock: The boundary where the supersonic solar wind is first slowed<br>"
                f"by Earth's magnetic field, typically located about {EARTH_BOW_SHOCK_STANDOFF_RADII:.4g} Earth radii upstream<br>"
                "from Earth on the Sun-facing side.<br>"
                "The Bow Shock points towards the Sun along the X-axis. The XY plane is the ecliptic.<br><br>"
                "Source (standoff): Jelinek et al. (2012), J. Geophys. Res. 117:A05208, doi:10.1029/2011JA017252."]
"""

BOWTEXT_NEW = b"""    bow_shock_text = ["Earth: Bow Shock<br><br>"
                "Bow Shock: the boundary where the supersonic solar wind first slows<br>"
                f"against Earth's magnetic field, about {EARTH_BOW_SHOCK_STANDOFF_RADII:.4g} Earth radii upstream on the<br>"
                f"Sun-facing side at a nominal solar wind pressure of {EARTH_SOLAR_WIND_PRESSURE_NPA:g} nPa.<br><br>"
                "That distance is a model evaluated at that pressure, not something anyone<br>"
                f"measured. Real crossings of the bow shock scatter about the fitted<br>"
                f"surface by {EARTH_BOW_SHOCK_JELINEK_SCATTER_RADII:g} Earth radii, and the shock itself moves in and out as<br>"
                "the pressure changes.<br><br>"
                "The bow shock points towards the Sun along the X-axis. The XY plane is<br>"
                "the ecliptic.<br><br>"
                "Source (standoff): Jelinek et al. (2012), J. Geophys. Res. 117:A05208, doi:10.1029/2011JA017252."]
"""


# ---------------------------------------------------------------------------
# Edit 2: magnetosphere_text.
# ---------------------------------------------------------------------------

MAGTEXT_OLD = b'''    magnetosphere_text = ["Earth: Magnetosphere<br><br>"
                 f"Earth's magnetosphere extends about {EARTH_MAGNETOPAUSE_STANDOFF_RADII:.4g} Earth radii on the Sun-facing side<br>"
                 "and stretches into a long magnetotail on the night side. It protects Earth<br>"
                 "from solar radiation and cosmic rays, making complex life possible.<br><br>"
                 "Source (standoff): Shue et al. (1998), J. Geophys. Res. 103:17691."]
'''

MAGTEXT_NEW = b'''    magnetosphere_text = ["Earth: Magnetosphere<br><br>"
                 f"Earth's magnetosphere reaches about {EARTH_MAGNETOPAUSE_STANDOFF_RADII:.4g} Earth radii on the Sun-facing<br>"
                 f"side at a nominal solar wind pressure of {EARTH_SOLAR_WIND_PRESSURE_NPA:g} nPa. It stretches into a<br>"
                 "long magnetotail on the night side, deflects the solar wind, and turns<br>"
                 "aside many of the energetic charged particles that reach Earth.<br><br>"
                 "That distance is a model evaluated at those conditions, not something<br>"
                 f"anyone measured. Real crossings of the magnetopause scatter about the<br>"
                 f"fitted surface by {EARTH_MAGNETOPAUSE_SHUE_SCATTER_RADII:g} Earth radii, and the boundary itself moves in<br>"
                 "and out as the solar wind pressure changes.<br><br>"
                 f"The tail is DRAWN to {tail_length_radii:g} Earth radii. It has been OBSERVED to at<br>"
                 f"least {EARTH_MAGNETOTAIL_OBSERVED_RADII:g} Earth radii, which is how far the spacecraft went rather<br>"
                 "than where the tail ends.<br><br>"
                 "The surface drawn through that nose is an approximation of the shape,<br>"
                 "not the model's own. A second fit, Jelinek et al. (2012), puts the nose<br>"
                 "about an Earth radius farther out, which is inside the scatter above.<br><br>"
                 "Source (standoff): Shue et al. (1998), J. Geophys. Res. 103:17691.<br>"
                 "Source (second fit): Jelinek et al. (2012), J. Geophys. Res. 117:A05208.<br>"
                 "Source (tail): Slavin et al. (1983), Geophys. Res. Lett. 10:973 -- ISEE-3."]
'''

# ---------------------------------------------------------------------------
# Edit 3: capture the drawn tail length before params are scaled to AU, so
# the hover above can quote the drawing parameter from where it is drawn.
# ---------------------------------------------------------------------------

SCALE_OLD = b"""    # Scale everything by Earth's radius in AU
    for key in params:
        params[key] *= EARTH_RADIUS_AU
"""

SCALE_NEW = b"""    # L-305 item 7: the DRAWN tail length, read before params are scaled to
    # AU so the hover can quote the drawing parameter from where it is drawn
    # rather than typing it. It stays a local read of the params dict -- a
    # drawing choice is not a store row (A Drawing Approximation Does Not
    # Promote), and hoisting it to module level would make it a claim-shaped
    # constant with no citation, which is a Tier-1 finding the scanner is
    # right to raise. The OBSERVED extent is the store row.
    tail_length_radii = params['tail_length']

    # Scale everything by Earth's radius in AU
    for key in params:
        params[key] *= EARTH_RADIUS_AU
"""

# ---------------------------------------------------------------------------
# Edit 4: earth_magnetosphere_info and its comment block.
# ---------------------------------------------------------------------------

INFO_OLD = b'''# Source: NASA Goddard Space Flight Center - Magnetosphere
# Source+: NASA Van Allen Probes (radiation belts)
# Verified: April 2026 via Gemini fact-check
earth_magnetosphere_info = (
            "SET MANUAL SCALE TO AT LEAST 0.01 AU TO VISUALIZE.\\n\\n" 

            f"Earth's magnetosphere extends about {EARTH_MAGNETOPAUSE_STANDOFF_RADII:.4g} Earth radii on the Sun-facing side\\n"
            "and stretches into a long magnetotail on the night side. It protects Earth\\n"
            "from solar radiation and cosmic rays, making complex life possible.\\n\\n"

            "Bow Shock: The boundary where the supersonic solar wind is first slowed\\n"
            f"by Earth's magnetic field, typically located about {EARTH_BOW_SHOCK_STANDOFF_RADII:.4g} Earth radii upstream\\n"
            "from Earth on the Sun-facing side.\\n\\n"

            "Inner Van Allen Belt: Region of trapped charged particles (mainly protons)\\n"
            "extending from about 1,000 km to 6,000 km above Earth's surface.\\n"
            "Outer Van Allen Belt: Region of trapped charged particles (mainly electrons)\\n"
            "extending from about 13,000 km to 60,000 km above Earth's surface."
)
'''

INFO_NEW = b'''# Source: every figure below interpolates a row in constants_new.py, and
# Source+: each row carries its own citation and access route:
# Source+: EARTH_MAGNETOPAUSE_STANDOFF_RADII (Shue et al. 1998),
# Source+: EARTH_BOW_SHOCK_STANDOFF_RADII (Jelinek et al. 2012),
# Source+: EARTH_MAGNETOTAIL_OBSERVED_RADII (Slavin et al. 1983), and the
# Source+: four EARTH_VAN_ALLEN_*_EDGE rows (Meredith et al. 2014; Li, Tu
# Source+: et al. 2024).
# Note: the two altitude pairs here were typed until 2026-09-14 and rested
# Note+: on a magazine article, a news article and a university outreach
# Note+: page. They are arithmetic on the belt rows now, which is why the
# Note+: outer figure changed. L-305 item 7.
earth_magnetosphere_info = (
            "SET MANUAL SCALE TO AT LEAST 0.01 AU TO VISUALIZE.\\n\\n" 

            f"Earth's magnetosphere extends about {EARTH_MAGNETOPAUSE_STANDOFF_RADII:.4g} Earth radii on the Sun-facing side\\n"
            "and stretches into a long magnetotail on the night side. It deflects the solar\\n"
            "wind and turns aside many of the energetic charged particles that reach Earth\\n"
            "from the Sun and from beyond the solar system.\\n\\n"

            f"Magnetotail: observed to at least {EARTH_MAGNETOTAIL_OBSERVED_RADII:g} Earth radii, which is how\\n"
            "far the spacecraft went rather than where the tail ends. The tail drawn\\n"
            "here is shorter, because it is a picture and not a measurement.\\n\\n"

            "Bow Shock: the boundary where the supersonic solar wind first slows\\n"
            f"against Earth's magnetic field, about {EARTH_BOW_SHOCK_STANDOFF_RADII:.4g} Earth radii upstream on the\\n"
            f"Sun-facing side at a nominal solar wind pressure of {EARTH_SOLAR_WIND_PRESSURE_NPA:g} nPa.\\n"
            f"Both standoffs above are models evaluated at that pressure rather than\\n"
            f"measurements: real crossings scatter about the fitted surfaces by\\n"
            f"{EARTH_MAGNETOPAUSE_SHUE_SCATTER_RADII:g} and {EARTH_BOW_SHOCK_JELINEK_SCATTER_RADII:g} Earth radii, and both boundaries move as the pressure\\n"
            "changes.\\n\\n"

            "Inner Van Allen Belt: Region of trapped charged particles (mainly protons),\\n"
            f"spanning about {EARTH_VAN_ALLEN_INNER_BELT_INNER_EDGE:g} to {EARTH_VAN_ALLEN_INNER_BELT_OUTER_EDGE:g} Earth radii in the geomagnetic equatorial plane --\\n"
            f"roughly {_km_above_surface(EARTH_VAN_ALLEN_INNER_BELT_INNER_EDGE, 2):,} to {_km_above_surface(EARTH_VAN_ALLEN_INNER_BELT_OUTER_EDGE, 1):,} km above the surface at the equator.\\n"
            "Outer Van Allen Belt: Region of trapped charged particles (mainly electrons),\\n"
            f"spanning about {EARTH_VAN_ALLEN_OUTER_BELT_INNER_EDGE:g} to {EARTH_VAN_ALLEN_OUTER_BELT_OUTER_EDGE:g} Earth radii and moving with geomagnetic\\n"
            f"activity -- roughly {_km_above_surface(EARTH_VAN_ALLEN_OUTER_BELT_INNER_EDGE, 1):,} to {_km_above_surface(EARTH_VAN_ALLEN_OUTER_BELT_OUTER_EDGE, 1):,} km above the surface at the\\n"
            "equator. Every kilometre figure here is converted from Earth radii."
)
'''

# ---------------------------------------------------------------------------
# Edit 5: the helper, inserted below the imports so the module-level string
# above can call it.
# ---------------------------------------------------------------------------

HELPER_ANCHOR = (
    b"from orrery_rendering import rotate_to_sunward, create_info_marker\n"
)

HELPER_NEW = b'''from orrery_rendering import rotate_to_sunward, create_info_marker


def _km_above_surface(radii, sig):
    """Altitude above Earth's equatorial surface, in km, from a geocentric
    distance in Earth radii, rounded to `sig` significant figures.

    L-305 item 7 (2026-09-14). Two things live here on purpose.

    The SUBTRAHEND is EARTH_EQUATORIAL_RADIUS_KM, not the mean radius, and
    that is not a taste. Everything in these shells is scaled by
    EARTH_RADIUS_AU, which is equatorial; L-178 retired a local mean-radius
    copy because mixing the two put a small systematic error into every
    altitude band. A hover that subtracted a different Earth from the one the
    shell is drawn against would put two Earths in one exhibit.

    The ROUNDING lives here rather than in the text, because a rounded figure
    typed into a string is exactly the failure this item removes, one digit
    smaller.

    `sig` is DECLARED, not derived. A Python float cannot say whether its
    source wrote "2" or "2.0", so nothing here can read the figure count off
    the input. Two is a choice, made for the callers this helper has: belt
    rows stated as schematic spans carrying one or two figures each, where a
    four-digit altitude would claim precision the input does not have. It
    over-reports the ends their sources state to a single figure, and that
    is the declared cost of one uniform rule over a per-number judgment.
    A caller whose row supports more figures must pass its own `sig`; this
    default must not be read as a claim about that row's source.
    """
    km = (radii - 1.0) * EARTH_EQUATORIAL_RADIUS_KM
    if km <= 0.0:
        return 0
    step = 10.0 ** (math.floor(math.log10(km)) - (sig - 1))
    return int(round(km / step) * step)
'''

# ---------------------------------------------------------------------------
# Edit 6 (highest in the file): the import list.
# ---------------------------------------------------------------------------

IMPORT_OLD = b'''    EARTH_VAN_ALLEN_INNER_RADII, EARTH_VAN_ALLEN_OUTER_RADII,
'''

IMPORT_NEW = b'''    EARTH_VAN_ALLEN_INNER_RADII, EARTH_VAN_ALLEN_OUTER_RADII,
    # L-305 item 7: the belt edges and the observed magnetotail extent.
    # The spans used to be typed into the strings below.
    EARTH_VAN_ALLEN_INNER_BELT_INNER_EDGE, EARTH_VAN_ALLEN_INNER_BELT_OUTER_EDGE,
    EARTH_VAN_ALLEN_OUTER_BELT_INNER_EDGE, EARTH_VAN_ALLEN_OUTER_BELT_OUTER_EDGE,
    EARTH_MAGNETOTAIL_OBSERVED_RADII,
    # L-305 item 7 part 4: the conditions a model standoff is evaluated at,
    # and how far real crossings sit from the surface it draws.
    EARTH_SOLAR_WIND_PRESSURE_NPA,
    EARTH_MAGNETOPAUSE_SHUE_SCATTER_RADII,
    EARTH_BOW_SHOCK_JELINEK_SCATTER_RADII,
'''


def fail(message):
    print("ERROR: " + message)
    sys.exit(1)


def apply_once(data, old, new, label):
    count = data.count(old)
    if count != 1:
        print("ANCHOR FAIL: %s matched %d times, expected 1" % (label, count))
        sys.exit(1)
    print("  ok  %s" % label)
    return data.replace(old, new)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    full = os.path.join(here, TARGET)

    if not os.path.exists(full):
        fail("%s not found beside this script. Put this file in the repo "
             "root, next to %s." % (TARGET, TARGET))

    store = os.path.join(here, "constants_new.py")
    if not os.path.exists(store):
        fail("constants_new.py not found beside this script.")
    with open(store, "rb") as handle:
        store_bytes = handle.read()
    if b"EARTH_MAGNETOTAIL_OBSERVED_RADII" not in store_bytes:
        fail("constants_new.py does not carry the rows this patch reads. "
             "Run patch_L305_item7_belt_rows.py first.")

    with open(full, "rb") as handle:
        data = handle.read()

    if b"\r\n" in data:
        fail("%s has CRLF line endings; this patch expects LF." % TARGET)

    fp = hashlib.md5(data).hexdigest()
    if fp != BASE_FP:
        print("ERROR: %s is not the file this patch was built against." % TARGET)
        print("  expected fingerprint %s" % BASE_FP)
        print("  found               %s" % fp)
        print("  Nothing was written.")
        sys.exit(1)

    if b"_km_above_surface" in data:
        fail("the helper is already present; this patch has run.")
    if b"EARTH_BOW_SHOCK_JELINEK_SCATTER_RADII" not in store_bytes:
        fail("constants_new.py does not carry the scatter rows this patch "
             "reads. Run patch_L305_item7_scatter_rows.py first.")

    # Bottom-up: lowest edit first.
    data = apply_once(data, BELTS_OLD, BELTS_NEW,
                      "belt_texts rewritten (edges interpolated, km derived)")
    data = apply_once(data, BOWTEXT_OLD, BOWTEXT_NEW,
                      "bow_shock_text rewritten (pressure, scatter)")
    data = apply_once(data, MAGTEXT_OLD, MAGTEXT_NEW,
                      "magnetosphere_text rewritten (tail, seam, scatter)")
    data = apply_once(data, SCALE_OLD, SCALE_NEW,
                      "drawn tail length captured before AU scaling")
    data = apply_once(data, INFO_OLD, INFO_NEW,
                      "earth_magnetosphere_info rewritten (altitudes derived)")
    data = apply_once(data, HELPER_ANCHOR, HELPER_NEW,
                      "_km_above_surface() helper added below the imports")
    data = apply_once(data, IMPORT_OLD, IMPORT_NEW,
                      "five new rows imported from constants_new")

    non_ascii = [b for b in bytearray(data) if b > 127]
    if non_ascii:
        fail("the patched text contains %d non-ASCII bytes; refusing to write."
             % len(non_ascii))

    with open(full, "wb") as handle:
        handle.write(data)

    print("patch applied to %s" % TARGET)
    print("  strings rewritten, and they are:")
    for name in ("earth_magnetosphere_info", "magnetosphere_text",
                 "belt_texts"):
        print("    %s" % name)
    print("  typed figures removed, and they are:")
    for name in ("inner belt 1.1 to 2 Earth radii",
                 "outer belt 3 to 7 Earth radii",
                 "inner belt 1,000 to 6,000 km",
                 "outer belt 13,000 to 60,000 km"):
        print("    %s" % name)
    print("  claims removed, and they are:")
    for name in ("making complex life possible",
                 "protects Earth from solar radiation"):
        print("    %s" % name)
    print("  next: run palomas_orrery.py and hover the three shells")


if __name__ == "__main__":
    main()
