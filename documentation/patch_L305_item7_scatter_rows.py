"""
patch_L305_item7_scatter_rows.py

L-305 item 7, part 4: two store rows for the two model scatters, so a
hover can print the physical envelope beside a model value instead of
typing it.

WHY THIS EXISTS
  Both standoffs are model evaluations. 10.25 is Shue's equation 10 at
  the declared conditions and 13.51 is Jelinek's equation 14 at the
  declared pressure. Each carries the figures its own inputs support, and
  that is correct. What is missing from both hovers is how far the real
  boundary sits from the model, which is a different fact about a
  different quantity -- and without it a visitor reads a model evaluation
  as a measurement.
  Both papers state that figure. Neither is a row, so a hover printing
  one would be typing it, which is the same defect as the belt spans
  living in a Note.

WHAT IT DOES (one file: constants_new.py)
  1. EARTH_MAGNETOPAUSE_SHUE_SCATTER_RADII = 1.23 -- the standard
     deviation of Shue's improved model against the observed crossings it
     was fitted to, p. 17,697. Inserted above the magnetopause standoff.
  2. EARTH_BOW_SHOCK_JELINEK_SCATTER_RADII = 0.69 -- the scatter of
     crossings about Jelinek's bow shock model, fig. 7. Inserted above
     the bow shock standoff.

  Both are already stated inside other rows' comments, which is where the
  figures came from and why neither needed new sourcing. This patch moves
  them into rows of their own and leaves the comments where they are;
  those comments explain a neighbouring value's reasoning rather than
  serving the figure, so they are not a second store.

HOW TO RUN IT (Tony)
  Save into the orrery repo root, next to constants_new.py, open in
  VS Code, click Run.

  Success: two "ok" lines, then "patch applied".
  Failure: one ERROR or ANCHOR FAIL line. NOTHING is written.

AFTER IT RUNS
  Run test_status_lines.py. Expect 28 status lines, none malformed, up
  from 26.

BASE
  Built on orrery 773e5c2d084f8e269abc5700d33928e530902b29 at
  https://github.com/tonylquintanilla/palomas_orrery
  Run this BEFORE patch_L305_item7_strings.py, which imports both rows.

Written September 14, 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

TARGET = "constants_new.py"
BASE_FP = "0c736df31772d798dcf45f5b5400e8e9"

BOW_ANCHOR = b"EARTH_BOW_SHOCK_STANDOFF_RADII = 13.51\n"

BOW_NEW = b'''EARTH_BOW_SHOCK_JELINEK_SCATTER_RADII = 0.69
# Unit: r_earth
# Status: measured V_SOURCED 2026-09-14 -- open full text
# Source: Jelinek, Nemecek and Safrankova (2012), J. Geophys. Res. 117,
# Source+: A05208, doi:10.1029/2011JA017252 -- fig. 7: the scatter of
# Source+: observed crossings about the bow shock model is 0.69 R_E. The
# Source+: same figure gives 0.76 R_E for their magnetopause.
# Access: open full text, https://doi.org/10.1029/2011JA017252 (2026-09-10).
# Note: this is NOT an uncertainty on the model's own numbers -- the paper
# Note+: states none for its six fitted values. It is how far real crossings
# Note+: sit from the surface the model draws, which is a different quantity
# Note+: and the one a visitor needs in order not to read an evaluated model
# Note+: as a measurement. The standoff below therefore keeps the figures its
# Note+: inputs support and prints this beside it.
# Record: documentation/L305_gap1_read_record_20260911.md

EARTH_BOW_SHOCK_STANDOFF_RADII = 13.51
'''

MP_ANCHOR = b"EARTH_MAGNETOPAUSE_STANDOFF_RADII = 10.25\n"

MP_NEW = b'''EARTH_MAGNETOPAUSE_SHUE_SCATTER_RADII = 1.23
# Unit: r_earth
# Status: measured V_SOURCED 2026-09-14 -- open full text
# Source: Shue et al. (1998), doi:10.1029/98JA01103, p. 17,697 -- the
# Source+: improved model's standard deviation against the observed
# Source+: magnetopause crossings it was fitted to is 1.23 R_E.
# Access: open full text, https://doi.org/10.1029/98JA01103, read from the
# Access+: PDF 2026-09-11.
# Note: a spread of real crossings about the fitted surface, not an
# Note+: uncertainty on the standoff below, which is an evaluation of eq. 10
# Note+: at the declared conditions and carries its own inputs' figures.
# Note+: It is also the yardstick for the seam between the two published
# Note+: fits: Shue and Jelinek disagree about the magnetopause nose by
# Note+: about 1 R_E, which sits inside this one figure alone.
# Record: documentation/L305_gap1_read_record_20260911.md

EARTH_MAGNETOPAUSE_STANDOFF_RADII = 10.25
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
        fail("%s not found beside this script." % TARGET)

    with open(full, "rb") as handle:
        data = handle.read()

    if b"\r\n" in data:
        fail("%s has CRLF line endings; this patch expects LF." % TARGET)

    fp = hashlib.md5(data).hexdigest()
    if fp != BASE_FP:
        print("ERROR: %s is not the file this patch was built against." % TARGET)
        print("  expected fingerprint %s" % BASE_FP)
        print("  found               %s" % fp)
        print("  Nothing was written. If patch_L305_item7_belt_rows.py has "
              "not run yet, run it first.")
        sys.exit(1)

    if b"EARTH_BOW_SHOCK_JELINEK_SCATTER_RADII" in data:
        fail("the scatter rows are already present; this patch has run.")

    data = apply_once(data, BOW_ANCHOR, BOW_NEW,
                      "Jelinek bow shock scatter row added, 0.69 R_E")
    data = apply_once(data, MP_ANCHOR, MP_NEW,
                      "Shue magnetopause scatter row added, 1.23 R_E")

    non_ascii = [b for b in bytearray(data) if b > 127]
    if non_ascii:
        fail("the patched text contains %d non-ASCII bytes; refusing to write."
             % len(non_ascii))

    with open(full, "wb") as handle:
        handle.write(data)

    print("patch applied to %s" % TARGET)
    print("  rows added, and they are:")
    for name in ("EARTH_MAGNETOPAUSE_SHUE_SCATTER_RADII",
                 "EARTH_BOW_SHOCK_JELINEK_SCATTER_RADII"):
        print("    %s" % name)
    print("  next: run test_status_lines.py, then the strings patch")


if __name__ == "__main__":
    main()
