"""Amend L-231: the tilt sourcing is already done, and the cone is the precedent.

Target: LEDGER_CONSOLIDATED.md  (orrery repo root)
Built against orrery 695f1f04a98a925737df929430567957ad62ccaf.
Handle: L-231.  2026-09-14, with Anthropic's Claude Opus 5.

REPLACES the withdrawn patch_L330_belt_plane_ledger_item.py, which filed a
duplicate of this item.  If that patch was run, this one refuses -- the
fingerprint will not match -- which is the intended outcome.

THREE EDITS, all inside the L-231 block
---------------------------------------
1. The metadata line's upd date moves to 2026-09-14.
2. The sentence saying the tilt figures are not citable and that sourcing
   them is part of the build gets an inline SUPERSEDED marker.  It was
   true when written on 2026-08-24 and stopped being true on 2026-06-22,
   which is BEFORE it was written -- L-231 was carrying a gap that L-009
   had already closed.  A reader who stops at that sentence goes off to
   source something twice, which is the stale-erratum class.
3. Four dated bullets and a Gap and Ref line are added before the
   existing Note.

WHAT THE NEW BULLETS RECORD
---------------------------
- The sourcing exists: all six magnetosphere bodies carry a sourced
  dipole cone as of L-009, Earth at 9.6 degrees and Jupiter at 10.3.
- The cone is the precedent for the belts: no single orientation is right
  in general, so the drawing shows the swept envelope, and where the
  sweep is degenerate the element collapses to a line rather than
  pretending to a precision it has not got.
- Three documents name three different planes for the same rings.
- The orrery holds two different tilts for Earth, one sourced and one
  typed, and the typed one is the one already ruled for removal.

NOTHING IS BUILT BY THIS PATCH.  It is a record correction only.

AFTER RUNNING
-------------
  python ledger_index.py     (block count UNCHANGED -- no new item)

UNDO
----
Nothing is written unless the fingerprint matches.  To undo: in GitHub
Desktop, right-click LEDGER_CONSOLIDATED.md in Changes and Discard
Changes.
"""

import hashlib
import os
import sys

TARGET = "LEDGER_CONSOLIDATED.md"
BASE_FP = "61464b82711c3532259f1d2f973933d3"
ZONE_START = b"<!-- INDEX:START"
ZONE_END = b"<!-- INDEX:END -->"

EDITS = [
    (
        "the upd date",
        b"<!-- L:231 status:OPEN upd:2026-08-24 section:A flag: rice:2/2/90/2 -->",
        b"<!-- L:231 status:OPEN upd:2026-09-14 section:A flag: rice:2/2/90/2 -->",
    ),
    (
        "the superseded sourcing sentence",
        b"""Those figures are orientation for a future design round, NOT
  citable values; sourcing them is part of the build.""",
        b"""Those figures are orientation for a future design round, NOT
  citable values; sourcing them is part of the build.
  [SUPERSEDED 2026-09-14 -- the sourcing was already done; see below]""",
    ),
    (
        "the new bullets",
        b"**Note:** RICE 2/2/90/2 -> 1.8 is Claude's proposed score.",
        b"""- **The sourcing is already done, and was done BEFORE this item was
  last updated. Correction, 2026-09-14.** L-009 closed on 2026-06-22,
  verified in code at `26e58b2`: all six bodies with a magnetosphere
  carry a SOURCED dipole cone in CUSTOM_SHELLS -- Mercury, Earth,
  Jupiter, Saturn, Uranus, Neptune -- and the provenance gate that
  required every dipole tilt to be sourced rather than recalled was
  cleared in the same pass. Earth's cone is 9.6 degrees and Jupiter's is
  10.3. The offsets were sourced too and cross-checked by a second model
  in June. So the sentence above asking for a sourcing round is asking
  for work that was finished two months before it was written. The belt
  build does not need a sourcing round; it needs to use the tilt the
  cones already use.
- **The cone is the precedent, and it answers the hard question.**
  L-009's reason for drawing a cone rather than a tilt is that no single
  orientation is correct in general, so the drawing shows the swept
  envelope instead of choosing a moment. That is exactly the question
  the belts raise: the magnetic axis turns with the planet, so a belt
  plane tilted one particular way is a picture of one instant. L-009 also
  records what to do when the sweep is degenerate -- Mercury and Saturn
  have their dipole within a degree of the spin axis, so their cone
  renders as a line rather than as a cone claiming a precision it has
  not got. The belts face the same choice in the same two flavours:
  a band thick enough to hold the sweep, or the present flat ring with
  the hover saying the real plane is tilted and turns.
- **Three documents name three different planes for the same rings**
  [verified @695f1f04 orrery, @0d8e6044 gallery]. The served config
  describes the belt edge rows as geocentric distances in the GEOMAGNETIC
  EQUATORIAL plane. `gallery/feature_renderers.js` says in its own
  comment that the belts are drawn in the ECLIPTIC plane on purpose, to
  match what the orrery draws, and names scene equivalence as the reason.
  The orrery's belt comment claims the ROTATIONAL axis. Two of the three
  already know they disagree. Whatever is decided has to leave all three
  saying the same thing.
- **The orrery holds two different tilts for Earth.** The dipole cone
  uses the sourced 9.6 degrees. The magnetosphere shape is rotated by
  `magnetic_tilt_deg=11` typed at the `rotate_to_sunward` call in
  `earth_visualization_shells.py`, with no citation and no store row.
  9.6 agrees with what the agencies publish -- 9.41 degrees from the
  WMM2020 coefficients and 9.21 from WMM2025, per NOAA -- and 11 is the
  textbook round number. The typed 11 is already ruled for removal under
  L-305; this is a second reason for it, and a warning that the two
  numbers must not be reconciled by promoting the wrong one.
**Note:** RICE 2/2/90/2 -> 1.8 is Claude's proposed score.
**Gap:** not a sourcing round. Decide which of the three planes is right,
decide cone-style envelope or flat ring plus an honest hover, then build
it in the orrery and `feature_renderers.js` in the SAME pass -- the scene
equivalence this item already names.
**Ref:** L-009 (the cones, closed) for the precedent and the sourced
tilts; L-061 (open) for the rolling frame, because the belts sit in the
same coupling the cone does and one cannot be decided without the other;
L-305 for the typed 11 already ruled for removal. Raised 2026-09-14 while
reviewing L-305 item 5; a duplicate of this item was drafted as L-330 the
same evening and withdrawn unrun.""",
    ),
]


def fingerprint(lf):
    start = lf.index(ZONE_START)
    end = lf.index(ZONE_END) + len(ZONE_END)
    return hashlib.md5(lf[:start] + lf[end:]).hexdigest()


def main():
    if not os.path.isfile(TARGET):
        print("FAILURE: %s not found. Run this from the orrery repo root."
              % TARGET)
        print("NOTHING was written.")
        return 1

    with open(TARGET, "rb") as handle:
        data = handle.read()

    lf = data.replace(b"\r\n", b"\n")

    if ZONE_START not in lf or ZONE_END not in lf:
        print("FAILURE: the INDEX zone markers were not found.")
        print("NOTHING was written.")
        return 1

    actual = fingerprint(lf)
    if actual != BASE_FP:
        print("FAILURE: BASE MOVED.")
        print("  expected md5 %s" % BASE_FP)
        print("  found        %s" % actual)
        print("  If patch_L330_belt_plane_ledger_item.py was run, this is")
        print("  why -- that patch is withdrawn. Discard its change and")
        print("  run this one instead.")
        print("NOTHING was written.")
        return 1

    if b"SUPERSEDED 2026-09-14" in lf:
        print("FAILURE: this amendment is already in the file."
              " NOTHING was written.")
        return 1

    is_crlf = data.count(b"\r\n") > 0

    def fit(block):
        return block.replace(b"\n", b"\r\n") if is_crlf else block

    for label, old, new in EDITS:
        count = data.count(fit(old))
        if count != 1:
            print("FAILURE: expected 1 match for %s, got %d."
                  % (label, count))
            print("NOTHING was written.")
            return 1

    for label, old, new in EDITS:
        data = data.replace(fit(old), fit(new))

    with open(TARGET, "wb") as handle:
        handle.write(data)

    print("OK: L-231 amended in %s" % TARGET)
    print("    line endings preserved (%s)" % ("CRLF" if is_crlf else "LF"))
    print("    three edits: the upd date, the superseded sentence, and")
    print("    four new bullets with a Gap and a Ref.")
    print()
    print("Next: python ledger_index.py")
    print("      The block count must be UNCHANGED -- no new item.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
