#!/usr/bin/env python3
"""
patch_L342_2_figure_counts_20260919.py -- ORRERY repo.

Run: save this file in the ORRERY repo ROOT (next to
PROJECT_INSTRUCTIONS.md), open it in VS Code and click Run.  Or:
python patch_L342_2_figure_counts_20260919.py

A patch is run from its repository's ROOT and filed in documentation/
AFTER it has run. This script refuses to run from documentation/.

Built on orrery 21065c5d95ecb22c79fa1f398644a30b73a9a5ed
at https://github.com/tonylquintanilla/palomas_orrery
(gallery 2ead992b055054956816ddda3544e849e9789d9a
at https://github.com/tonylquintanilla/tonyquintanilla.github.io)

L-342, Findings 2 and 3 of Claude Fable 5.1's review of L-322 Stage C1,
settled by Tony on 2026-09-19: implement the rules as the reference the
skill names states them. That reference is Wikipedia, Significant
figures (and ASTM E29), and it was read for this patch rather than
recalled.

WHAT THE PAGE ACTUALLY SAYS, because it is narrower than either side of
the argument had it. Its rule is:

    "Zeros to the right of the last non-zero digit (trailing zeros) in a
    number with the decimal point are significant IF THEY ARE WITHIN THE
    MEASUREMENT OR REPORTING RESOLUTION."

And separately, among the digits it lists as NOT significant:

    "Trailing zeros when they serve as placeholders. In the measurement
    1500 m, when the measurement resolution is 100 m, the trailing zeros
    are insignificant."

So significance turns on the SOURCE'S RESOLUTION, not on where a digit
happens to fall. The walk's rule -- a trailing zero in a padded decimal
place does not count -- had the right instinct and the wrong reason, and
was settled inside a figures line where it looked like fact. The
review's reading -- zeros after a decimal point always count -- is the
skill's compressed form and drops the resolution condition, which is
what makes 1500 m two figures.

WHAT IT DOES (one file, 6 anchored edits). Applied to the rows in
question, the resolution test gives the review's answers:

  EARTH_OUTER_CORE_KM      4 -> 5. PREM Table I reports every boundary
                           radius to 0.1 km, so 3480.0's zero is within
                           the reporting resolution and counts.
  EARTH_OUTER_CORE_RADII   4 -> 5, inherited.
  EARTH_MEAN_RADIUS_KM     4 -> 7. Same clause. AND THE OLD LINE'S
                           PREMISE WAS FALSE: it said the NASA sheet is
                           "padded to three decimals throughout", and the
                           same block prints 3485, 5513, 20.4 and 11.186.
                           It is not uniformly padded, so 6371.000 is a
                           deliberate seven figures. That correction is
                           the review's, and it is right.
  EARTH_HILL_SPHERE_KM     7 -> 3. Not a counting question. The Hill
                           radius is an approximation in its own right,
                           so seven figures claim a precision the formula
                           cannot deliver whatever its inputs carry. The
                           old line declared seven and then said in its
                           own next sentence to report three.
  EARTH_HILL_SPHERE_RADII  7 -> 3, inherited.

  The Hill sphere's own "# Derived:" line also read "= 1,496,559 km.
  Report 1.50e6 km." -- seven figures of arithmetic with an instruction
  to show three. It now reads 1,500,000 km, three figures. The figures
  checker caught that leftover on the first run of this patch, which is
  the checker doing its job on the builder.

NOTHING ELSE MOVES, and that was measured rather than assumed.
EARTH_MEAN_RADIUS_KM feeds only EARTH_LOWER_MANTLE_KM, whose count is
set by the 660 km depth at the tens place and stays 3; and
EARTH_OUTER_CORE_KM feeds only its own _RADII row.

TWO THINGS OWED TO provenance-discipline'S NEXT BUMP, and they are why
this patch does not touch the skill. Rule 2 should carry the resolution
condition, because without it the rule is wrong for 1500 m. And Rule 3
needs a sentence saying a row may declare FEWER figures than its inputs
support when the relation is itself approximate. Two of the skill's own
examples are stale either way: Rule 1's "the trailing zero in 3480 is
significant" and Rule 3's "6371.0 - 660 is good to units: 5711", which
C1 showed is 5710.

WHAT A VISITOR SEES CHANGES on two rows, and this is visitor-visible:
the outer core gains a digit, and the Hill sphere drops from
"234.6388 Earth radii" to "235". Run the gallery half afterwards.

SUCCESS looks like: one "ok" line per edit, then "patch applied".
FAILURE looks like: one ERROR: or ANCHOR FAIL: line, and NOTHING is
written. Undo is Discard Changes in GitHub Desktop.
"""

import hashlib
import os
import sys

STORE = "constants_new.py"
BASE = "da021fe9f712fde7a15f6b93c7ca3523"


def fail(msg):
    print(msg)
    print("NOTHING was written. Undo is Discard Changes in GitHub Desktop.")
    sys.exit(1)


EDITS = []

EDITS.append(('OUTER_CORE_KM  4 -> 5, on the reporting-resolution clause',
    b"# Figures: 4 -- PREM Table I prints 3480.0, but it pads every boundary\n# Figures+: radius to one decimal, so that trailing zero is the table's\n# Figures+: format rather than a claim to 100 m. A non-zero digit in that\n# Figures+: place does count, which is why 1221.5 and 6346.6 carry five.\n",
    b"# Figures: 5 -- PREM Table I prints 3480.0, and a trailing zero after the\n# Figures+: decimal point is significant when it is within the source's\n# Figures+: reporting resolution. That table reports every boundary radius\n# Figures+: to 0.1 km, so the zero is within it and counts. Corrected\n# Figures+: 2026-09-19 from 4: the old line said the zero was the table's\n# Figures+: padding and did not count, which is a rule this project never\n# Figures+: made. See Wikipedia, Significant figures, the trailing-zeros\n# Figures+: clause, which Tony named as the reference.\n"))
EDITS.append(('OUTER_CORE_RADII  4 -> 5, inherited',
    b'# Figures: 4 -- set by EARTH_OUTER_CORE_KM (3480, 4)\n',
    b'# Figures: 5 -- set by EARTH_OUTER_CORE_KM (3480.0, 5)\n'))
EDITS.append(('MEAN_RADIUS_KM  4 -> 7, and a false premise removed',
    b'# Figures: 4 -- the fact sheet prints 6371.000 in a table padded to three\n# Figures+: decimals throughout, so the trailing zeros are formatting and\n# Figures+: not precision. PREM quotes the same sphere as 6371 km.\n',
    b'# Figures: 7 -- the fact sheet prints 6371.000, and trailing zeros after\n# Figures+: the decimal point are significant when they are within the\n# Figures+: source\'s reporting resolution. Corrected 2026-09-19 from 4 on\n# Figures+: two counts. The rule was wrong: a trailing zero does not stop\n# Figures+: counting because of where it happens to fall. AND THE PREMISE\n# Figures+: WAS FALSE -- the old line said the sheet is "padded to three\n# Figures+: decimals throughout", and the same block prints core radius\n# Figures+: 3485, mean density 5513, topographic range 20.4 and escape\n# Figures+: velocity 11.186. It is not uniformly padded, so 6371.000 is a\n# Figures+: deliberate seven figures. PREM quotes the same sphere as\n# Figures+: 6371 km, to four, for its own purposes.\n'))
EDITS.append(('HILL_SPHERE_KM  7 -> 3, the relation is the limit',
    b"# Figures: 7 -- EARTH_GM_KM3_S2 carries nine and every other input is\n# Figures+: exact, but a = 1 AU is a substitution for Earth's semi-major\n# Figures+: axis and agrees with it only to seven figures (see the note\n# Figures+: below), so seven is the count. The formula's own idealisation\n# Figures+: is coarser than any of this; report 1.50e6 km.\n",
    b"# Figures: 3 -- THE RELATION ITSELF IS THE LIMIT, not the inputs. Rule 3\n# Figures+: counts measured inputs, and by that route this would be seven:\n# Figures+: EARTH_GM_KM3_S2 carries nine, every other input is exact, and\n# Figures+: a = 1 AU agrees with Earth's semi-major axis to seven. But the\n# Figures+: Hill radius is an approximation in its own right -- using\n# Figures+: Earth's perihelion distance instead of its mean distance moves\n# Figures+: it by more than one percent -- so seven figures claim a\n# Figures+: precision the formula cannot deliver whatever its inputs carry.\n# Figures+: Corrected 2026-09-19 from 7: the old line declared seven and\n# Figures+: then said in its own next sentence to report three, and the\n# Figures+: gallery formats from the declared count, so a visitor was shown\n# Figures+: 234.6388 Earth radii. Owed to provenance-discipline's next\n# Figures+: bump: a row may declare FEWER figures than its inputs support\n# Figures+: when the relation is itself approximate, with the reason in\n# Figures+: words on the row. (Fable's review of C1, Finding 3.)\n"))
EDITS.append(('HILL_SPHERE_RADII  7 -> 3, inherited',
    b'# Figures: 7 -- set by EARTH_HILL_SPHERE_KM\n',
    b'# Figures: 3 -- set by EARTH_HILL_SPHERE_KM\n'))
EDITS.append(('HILL_SPHERE_KM  the derived line rounds to the declared three',
    b'# Derived+: 0.0100039; x 149,597,870.7 km = 1,496,559 km. Report 1.50e6 km.\n',
    b'# Derived+: 0.0100039; x 149,597,870.7 km = 1,500,000 km, three figures.\n'))


def main():
    if os.path.basename(os.getcwd()) == "documentation":
        fail("ERROR: this script is running from documentation/. Move it "
             "to the repository ROOT and run it there.")
    if not os.path.exists(STORE):
        fail("ERROR: " + STORE + " is not here. Run this from the ORRERY "
             "repo root.")

    with open(STORE, "rb") as handle:
        raw = handle.read()
    got = hashlib.md5(raw.replace(b"\r\n", b"\n")).hexdigest()
    if got != BASE:
        fail("ERROR: " + STORE + " is not the file this patch was cut "
             "against.\n  expected " + BASE + "\n  found    " + got +
             "\nIf the patch already ran, this is what a second run looks "
             "like: it refuses.")

    is_crlf = raw.count(b"\r\n") > 0
    out = raw
    for label, old, new in EDITS:
        if is_crlf:
            old = old.replace(b"\n", b"\r\n")
            new = new.replace(b"\n", b"\r\n")
        n = out.count(old)
        if n != 1:
            fail("ANCHOR FAIL: expected exactly 1 match, found %d -- %s"
                 % (n, label))
        out = out.replace(old, new)

    try:
        out.decode("ascii")
    except UnicodeDecodeError as exc:
        fail("ERROR: the result is not ASCII (%s)." % exc)

    with open(STORE, "wb") as handle:
        handle.write(out)

    for label, _o, _n in EDITS:
        print("  ok  " + label)
    print("")
    print("      %-24s %7d -> %7d bytes" % (STORE, len(raw), len(out)))
    print("")
    print("patch applied (1 file, %d edits)" % len(EDITS))
    print("")
    print("NOW, in order:")
    print("  1. Run the orrery maintenance run. It REGENERATES THE")
    print("     EXPORT -- commit that file this time; the figure counts")
    print("     are what changed.")
    print("  2. Move this script into documentation/.")
    print("  3. Commit everything the run touched and push.")
    print("  4. Gallery: run patch_L342_1 first if it has not run, then")
    print("     pull the export, mirror, rebuild the cache with OneDrive")
    print("     PAUSED, and commit config and cache together.")
    print("")
    print("Undo at any point is Discard Changes in GitHub Desktop.")


if __name__ == "__main__":
    main()
