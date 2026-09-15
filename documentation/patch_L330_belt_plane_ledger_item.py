"""Add ledger item L-330: the radiation belts are drawn in the wrong plane.

Target: LEDGER_CONSOLIDATED.md  (orrery repo root)
Built against orrery 695f1f04a98a925737df929430567957ad62ccaf.
2026-09-14, with Anthropic's Claude Opus 5.

The new block goes at the top of section A, immediately before L-001.
Only the detail block is written.  The index tables are NOT touched --
run ledger_index.py after this, which regenerates them.

The fingerprint deliberately excludes the INDEX zone, so this patch still
applies after a ledger_index.py run and does not care whether the zone
has been regenerated since.

AFTER RUNNING
-------------
  python ledger_index.py        (regenerates the index)

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

ANCHOR = b"""## A. ACTIVE SEPARATE TRACKS (not orrery-refactor backlog; cross-referenced)

#### [L-001] Food Insecurity (Earth System track)"""

BLOCK = b"""## A. ACTIVE SEPARATE TRACKS (not orrery-refactor backlog; cross-referenced)

#### [L-330] The radiation belts are drawn in the wrong plane (Earth exhibit track)
<!-- L:330 status:OPEN upd:2026-09-14 section:A flag: rice:3/3/70/2 -->
- **The finding.** The Van Allen belts are organised around Earth's
  MAGNETIC axis, not its rotation axis. The served data says so in its own
  words: the belts block's `_frame` note describes the edge rows as
  geocentric distances in the geomagnetic equatorial plane. The web
  renderer draws them anyway with no tilt at all. `feature_renderers.js`
  at gallery `0d8e6044` contains three references to tilt and all three
  belong to the ring systems of Saturn and Jupiter. So the drawn belts sit
  in the wrong plane by roughly nine degrees.
  [verified @0d8e6044 -- read from the file, NOT confirmed by eye]
- **The figure is also stale.** The desktop orrery types
  `magnetic_tilt_deg=11` at the call site in
  `earth_visualization_shells.py`, with no citation and no store row --
  `constants_new.py` has no dipole or geomagnetic constant of any kind.
  Eleven degrees is the textbook round number. The agencies that compute
  it from the field model give less: NOAA states 9.41 degrees from the
  WMM2020 coefficients and 9.21 degrees from WMM2025, and the British
  Geological Survey says about ten. The tilt drifts, so any stored row
  carries the model and the epoch it came from, the way a pole does.
- **Three questions before any code.**
  1. WHICH FIGURE AND WHICH EPOCH. A row computed from a named field model
     at a named year, or nothing.
  2. WHICH WAY. A tilt needs a direction as well as an angle, and the
     geomagnetic pole's longitude turns with the Earth once a day. The
     Earth exhibit is a frozen scene that states it shows no rotation, so
     there is no "now" to tilt toward. Either the scene declares an epoch
     for the magnetic longitude and says so in the hover, or the belts are
     drawn tilted by the angle in some declared reference direction and
     the hover says that the direction is a convention, not a time.
  3. WHETHER THE DESKTOP AGREES. The desktop orrery's legend already
     carries an item called "Earth: Dipole Cone", so something there
     already knows about the dipole axis. Whatever is decided has to hold
     in both places or the two pictures disagree.
- **Not to be folded into L-305.** The magnetopause and the bow shock must
  NOT be tilted: both papers fitted their surfaces in coordinates lined up
  with the solar wind, from crossings taken at every dipole tilt, so the
  tilt is already averaged into the published numbers and applying it
  afterwards would move the surface away from its own source. The belts
  are the opposite case. Same number, opposite answers, which is why they
  are separate items.
**Note:** RICE proposed by Claude, not scored by Tony. Reach 3 and Impact
3 because this is a visible figure on a public page rather than an
internal value; Confidence 70 because the code reading is solid and no
render has been checked by eye; Effort 2 because the drawing change is
small once the three questions above are ruled.
**Gap:** the three questions, then a store row, then the renderer, then
the same change in the desktop orrery.
**Ref:** raised 2026-09-14 while reviewing L-305 item 5. The belts'
`_frame` note is in `data/objects_config.json` under
`earth_magnetosphere`'s sibling `van_allen_belts`. Related: L-322, which
moves the maintenance checker off reading units from constant names --
the same class of problem, a machine reading a name instead of the
declaration beside the value.

#### [L-001] Food Insecurity (Earth System track)"""


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
        print("  (the INDEX zone and line endings are both excluded from"
              " this hash, so this is a real change to the body)")
        print("NOTHING was written.")
        return 1

    if b"L-330" in lf:
        print("FAILURE: L-330 is already in the ledger. NOTHING was written.")
        return 1

    is_crlf = data.count(b"\r\n") > 0
    anchor = ANCHOR.replace(b"\n", b"\r\n") if is_crlf else ANCHOR
    block = BLOCK.replace(b"\n", b"\r\n") if is_crlf else BLOCK

    count = data.count(anchor)
    if count != 1:
        print("FAILURE: expected 1 match for the insertion anchor, got %d."
              % count)
        print("NOTHING was written.")
        return 1

    data = data.replace(anchor, block)

    with open(TARGET, "wb") as handle:
        handle.write(data)

    print("OK: L-330 added to %s at the top of section A" % TARGET)
    print("    line endings preserved (%s)" % ("CRLF" if is_crlf else "LF"))
    print()
    print("Next: python ledger_index.py")
    print("      Expect ONE more block than the previous run reported,")
    print("      and no consistency problems.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
