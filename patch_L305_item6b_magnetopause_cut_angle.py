"""Add EARTH_MAGNETOPAUSE_CUT_ANGLE_DEG to the store.

Target: constants_new.py  (orrery repo root)
Built against orrery 68102e1e (constants_new.py is byte-identical at
fc34bdc2, so either HEAD accepts this patch).
Handle: L-305 item 6b.  2026-09-14, with Anthropic's Claude Opus 5.

WHAT THIS ADDS
--------------
One row, saying where the drawn magnetopause stops: 120 degrees from the
nose.  Tony's ruling of 2026-09-14.

Shue's surface has no end.  The flaring exponent at the store's declared
conditions is 0.5896, and for any flaring at or above 0.5 the radius
grows without bound as the angle approaches 180 degrees.  So a drawing
has to choose a stopping point, and that choice is declared rather than
measured.

The reason for 120: Shue et al. (1998) figure 6 plots the model's own
uncertainty out to 120 degrees solar zenith angle, which is the furthest
the authors evaluate their own model.  The paper never states how far
round its crossings reached -- the read record of 2026-09-11 says so and
says that number would have to come from Shue et al. (1997), which is
not read.

The row is placed with the other magnetopause rows, between the last
Shue coefficient and the first Jelinek one, so the two boundaries stay
in separate blocks.

WHAT IT DOES NOT DO
-------------------
Nothing is served and nothing is drawn.  The gallery config rows and the
drawing code are the next two patches.

AFTER RUNNING
-------------
  python provenance_scanner.py      (Tier-1 must not rise)
  python -c "import constants_new"  (the file still imports)

UNDO
----
Nothing is written unless the fingerprint matches, so the file on disk is
the committed one at the moment this writes.  To undo: in GitHub Desktop,
right-click constants_new.py in Changes and Discard Changes.
"""

import hashlib
import os
import sys

TARGET = "constants_new.py"
BASE_FP = "e9b288b4017292d05b0da03467dcf718"

ANCHOR = b"""# Note+: Recorded so nobody re-derives the doubt.

EARTH_BOW_SHOCK_JELINEK_R0_RADII = 15.02"""

ROW = b"""# Note+: Recorded so nobody re-derives the doubt.

EARTH_MAGNETOPAUSE_CUT_ANGLE_DEG = 120.0
# Unit: deg
# Status: declared 2026-09-14 -- a drawing limit, not an edge
# Declared: where the drawn magnetopause stops, measured from the nose.
# Declared+: Shue's surface has no end. At the store's declared conditions
# Declared+: the flaring is 0.5896, and for any flaring at or above 0.5 the
# Declared+: radius grows without bound as theta approaches 180 degrees, so
# Declared+: a drawing must choose a stop.
# Declared+: Shue et al. (1998), doi:10.1029/98JA01103 -- fig. 6, p. 17,695,
# Declared+: plots the model's own uncertainty out to 120 degrees solar
# Declared+: zenith angle, the furthest the authors evaluate their own model.
# Declared+: Past that the drawing would show a surface the paper does not.
# Declared+: The paper states no angular range for the crossings it was
# Declared+: fitted to; that number exists only in Shue et al. (1997), which
# Declared+: is not read.
# Access: open full text, https://doi.org/10.1029/98JA01103 (2026-09-11).
# Record: documentation/L305_gap1_read_record_20260911.md
# Note: the same shape as EARTH_BOW_SHOCK_CUT_ANGLE_DEG and a different
# Note+: kind of reason. The bow shock stops where its crossings stopped,
# Note+: within 7 hours of local noon. The magnetopause stops where its
# Note+: authors stopped plotting. Both are drawing limits; neither is an
# Note+: edge of anything physical, and the hover has to say so.
# Note+: At the declared conditions the cut falls at r = 23.2 R_E,
# Note+: x = -11.6 R_E, R_yz = 20.1 R_E. For comparison the bow shock cut
# Note+: falls at x = -7.8 R_E, R_yz = 29.0 R_E, so the drawn shock is the
# Note+: wider and shorter of the two. That is not a physical statement
# Note+: about the two boundaries; it is two drawing limits set by two
# Note+: different papers for two different reasons.
# Note: Tony's ruling, 2026-09-14 (L-305 item 6b).

EARTH_BOW_SHOCK_JELINEK_R0_RADII = 15.02"""


def main():
    if not os.path.isfile(TARGET):
        print("FAILURE: %s not found. Run this from the orrery repo root."
              % TARGET)
        print("NOTHING was written.")
        return 1

    with open(TARGET, "rb") as handle:
        data = handle.read()

    lf = data.replace(b"\r\n", b"\n")
    actual = hashlib.md5(lf).hexdigest()
    if actual != BASE_FP:
        print("FAILURE: BASE MOVED.")
        print("  expected content md5 %s" % BASE_FP)
        print("  found                %s" % actual)
        print("  (line endings are normalized before hashing, so this is a"
              " real content difference)")
        print("NOTHING was written.")
        return 1

    if b"EARTH_MAGNETOPAUSE_CUT_ANGLE_DEG" in data:
        print("FAILURE: EARTH_MAGNETOPAUSE_CUT_ANGLE_DEG is already in the"
              " file. NOTHING was written.")
        return 1

    is_crlf = data.count(b"\r\n") > 0
    anchor = ANCHOR.replace(b"\n", b"\r\n") if is_crlf else ANCHOR
    row = ROW.replace(b"\n", b"\r\n") if is_crlf else ROW

    count = data.count(anchor)
    if count != 1:
        print("FAILURE: expected 1 match for the insertion anchor, got %d."
              % count)
        print("NOTHING was written.")
        return 1

    data = data.replace(anchor, row)

    with open(TARGET, "wb") as handle:
        handle.write(data)

    print("OK: EARTH_MAGNETOPAUSE_CUT_ANGLE_DEG = 120.0 added to %s"
          % TARGET)
    print("    line endings preserved (%s)" % ("CRLF" if is_crlf else "LF"))
    print()
    print("Next: python provenance_scanner.py   (Tier-1 must not rise)")
    print("      python -c \"import constants_new\"")
    return 0


if __name__ == "__main__":
    sys.exit(main())
