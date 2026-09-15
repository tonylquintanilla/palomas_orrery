"""Record the belt plane ruling, Fable's findings, and open an item for the shape.

Target: LEDGER_CONSOLIDATED.md  (orrery repo root)
Built against orrery 695f1f04a98a925737df929430567957ad62ccaf.
Handles: L-231 (amended), L-305 (gap extended), L-330 (new).
2026-09-15, with Anthropic's Claude Opus 5.

REPLACES the withdrawn patch_L231_belt_plane_amendment.py, which was built
before Fable's review of 2026-09-15. If that one was run, this refuses.
It also replaces the earlier withdrawn patch_L330_belt_plane_ledger_item.py,
which filed a duplicate of L-231; the handle L-330 was never used and is
taken here for something else.

FOUR EDITS
----------
1. L-231's upd date moves to 2026-09-15.
2. The sentence saying the tilt figures still need sourcing gets an inline
   SUPERSEDED marker. The sourcing was finished on 2026-06-22, which is
   two months BEFORE that sentence was last touched.
3. L-231 gains Fable's findings, my verification of them, and Tony's
   ruling. It stops being a question and becomes a build.
4. L-305's gap line about the typed 11 degrees gains the reason it should
   not wait, and a corrected line number.
5. L-330 opens for the belt's SHAPE, which is a separate decision from its
   plane and is deliberately not bundled with it.

WHAT WAS RULED, 2026-09-15
--------------------------
Draw the belts about the spin axis, in Earth's equatorial plane, in both
instruments in one pass. Remove the saddle warp. Put the 9.6 degrees in
the hover rather than the geometry. Shape is a separate pass.

VERIFICATION
------------
Every one of Fable's five record findings was checked against the files by
Claude before this was written, at orrery 695f1f04 and gallery 0d8e6044.
All five hold. The line numbers and code quoted below were read, not
recalled.

AFTER RUNNING
-------------
  python ledger_index.py     (expect ONE more block than the last run)

UNDO
----
Nothing is written unless the fingerprint matches. To undo: in GitHub
Desktop, right-click LEDGER_CONSOLIDATED.md in Changes and Discard Changes.
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
        "L-231's upd date",
        b"<!-- L:231 status:OPEN upd:2026-08-24 section:A flag: rice:2/2/90/2 -->",
        b"<!-- L:231 status:OPEN upd:2026-09-15 section:A flag: rice:2/2/90/2 -->",
    ),
    (
        "the superseded sourcing sentence in L-231",
        b"""Those figures are orientation for a future design round, NOT
  citable values; sourcing them is part of the build.""",
        b"""Those figures are orientation for a future design round, NOT
  citable values; sourcing them is part of the build.
  [SUPERSEDED 2026-09-15 -- the sourcing was already done; see below]""",
    ),
    (
        "the L-305 gap line about the typed tilt",
        b"""  in the `rotate_to_sunward` call at `earth_visualization_shells.py:785`
  [verified @5fea1795] -- so its removal stays in the Gap.""",
        b"""  in the `rotate_to_sunward` call at `earth_visualization_shells.py:785`
  [verified @5fea1795] -- so its removal stays in the Gap.
- **That removal should not wait, and here is why (2026-09-15).** The call
  is now at `earth_visualization_shells.py:865` and still carries
  `magnetic_tilt_deg=11` [verified @695f1f04]. The BOW SHOCK call sixty
  lines below passes no tilt at all [verified @695f1f04]. So the desktop
  currently draws a magnetopause leaning eleven degrees inside an upright
  bow shock: one drawing, two answers, and the lean is the one with no
  citation behind it. Found by Fable, 2026-09-15, checking a brief that
  wrongly told it this was already built. The web renderer built the same
  evening applies no tilt, so the two instruments will disagree until the
  desktop call is changed.""",
    ),
    (
        "L-231's new findings, ruling and gap",
        b"**Note:** RICE 2/2/90/2 -> 1.8 is Claude's proposed score.",
        b"""- **The sourcing is already done, and was done BEFORE this item was last
  updated. Correction, 2026-09-15.** L-009 closed on 2026-06-22, verified
  in code at `26e58b2`: all six bodies with a magnetosphere carry a SOURCED
  dipole cone, and the provenance gate requiring every dipole tilt to be
  sourced rather than recalled was cleared in the same pass. Earth's is 9.6
  degrees, Jupiter's 10.3. So the sentence above asking for a sourcing
  round asks for work finished two months before it was written. Read 9.6
  from `PLANET_DIPOLE`, not the "about 11 deg" in the body text above,
  which is where the stale number keeps being picked up.
- **What is drawn is not a plane at all.** Both belt builders place their
  points at `z = 0.2 * r * sin(2 * angle)` -- gallery `beltPoints` in
  `feature_renderers.js`, orrery `earth_visualization_shells.py:1031`
  [verified @0d8e6044 and @695f1f04]. That is a saddle: the ring rises and
  falls TWICE per circuit, by a fifth of its radius. For the outer belt at
  4.5 R_E that is 0.9 R_E up and 0.9 down. A ring genuinely tilted 9.6
  degrees would rise and fall ONCE, by 0.17 R_E. So the current drawing has
  more vertical swing than the real tilt would give, at twice the
  frequency, meaning nothing. The orrery comment beside it says the wobble
  makes the belt "thinner near poles"; the code changes no cross-section,
  it moves the whole ring. THE WARP MUST COME OUT IN THE SAME PASS: a real
  tilt added on top of it sums into a shape nobody can describe. Found by
  Fable, 2026-09-15; confirmed in both files by Claude.
- **Four statements, not three, and the fourth is the one the visitor
  reads.** The served `_frame` note says geomagnetic equatorial. The
  comment at the head of `renderBelts` says ecliptic, on purpose. The
  orrery's belt comment says rotational axis. And forty lines inside
  `renderBelts`, the L-305 item 7 comment says "These rings are drawn in
  that plane" -- meaning the MAGNETIC equatorial plane -- while the hover
  the visitor sees says the outer belt is drawn where that shell crosses
  the magnetic equator. [verified @0d8e6044]
- **That fourth statement is load-bearing and it is false.** It is the
  whole justification for accepting `l_shell` as a drawable unit: L equals
  a geocentric radius in exactly one plane, so an L value may be drawn at
  that radius IF the ring is in that plane. The ring is in the ecliptic.
  This is not a design question -- it is a false sentence in visitor-facing
  text, shipped 2026-09-14, and it needs correcting under EVERY option
  including leaving the plane alone. Under the ruling below the honest
  wording is that the RADIUS is where the shell crosses the magnetic
  equator, and the RING is drawn in the daily-average plane.
- **The served edges are drawn by neither instrument.** Four edge rows
  landed 2026-09-14: inner belt 1.1 to 2.0 R_E, outer 3.0 to 7.0. Neither
  renderer reads them. Both draw a ring at the peak with a typed half-width
  (`belt_thickness: 0.5`). The inner belt is served 0.9 R_E wide and drawn
  0.5; the outer is served 4 R_E wide and drawn 0.5. The gallery hover then
  prints "Band thickness: 0.5 radii" a few lines above a served note giving
  the true span -- a drawing choice printed as if it were the belt's width,
  which is A Drawing Approximation Does Not Promote running backwards. Fix
  the hover in this pass whatever else is decided; fix the shape under
  L-330.
- **The cone precedent transfers as a choice of AXIS, not as a swept
  shape.** Fable's analysis, checked and agreed: a ring tilted 9.6 degrees
  and spun about the spin axis sweeps a band of half-height r sin(9.6 deg)
  -- 0.25 R_E at the inner belt, 0.75 at the outer. But a belt is bounded
  by field lines, and a dipole line crossing the equator at L reaches
  latitude arccos(1/sqrt(L)): 55 degrees at L = 3, 68 at L = 7. The daily
  sweep is swallowed by the belt's own shape at every radius. Drawing the
  sweep would read as thickness and teach a belt three times fatter than it
  is. A cone works because a line has no thickness and the sweep gives it
  one; a belt already has thickness. THE TIME-VARYING TILT IS A SENTENCE,
  NOT A SHAPE.
- **Why not the magnetic equator itself.** A tilted plane needs a direction
  as well as an angle, and the direction turns once a day. The Earth
  exhibit is frozen and says on its own face that it shows no rotation, so
  it has no hour to give. Any direction chosen is one instant and a reader
  cannot tell that from the shape. If the exhibit ever declares an epoch,
  the magnetic pole's longitude at that hour is a lookup from the same
  model that gives the 9.6, and the tilted plane becomes honest -- better
  than the ruling below. Until then it is not writable: the hover would
  have two blanks that no store row can fill.
- **TONY'S RULING, 2026-09-15.** Draw the belts about the SPIN AXIS, in
  Earth's equatorial plane, using the pole basis both instruments already
  have. Remove the saddle warp. Put the 9.6 degrees in the hover, not in
  the geometry. Correct the two code comments and the false fourth
  statement. Do BOTH INSTRUMENTS IN ONE PASS. The deciding argument is the
  geostationary ring: the exhibit already draws it in the spin-equatorial
  plane (the scene checker asserts GEO and the equator share one plane),
  geostationary orbit is at 6.6 R_E, and the outer belt is served as
  spanning 3 to 7 -- so today the picture puts that ring 23 degrees away
  from a belt it lies inside. The obliquity is the big error and the
  magnetic tilt is the small one; this ruling fixes the big one, and unlike
  a hover it is visible without anyone reading. The spin equator is also
  the daily average of the magnetic equator, so the choice stays correct
  across the whole orbit rather than picturing one instant.
- **Scene equivalence is not a reason for a plane.** The renderer's comment
  gives it as the reason for the ecliptic. It is a reason for the two
  instruments to MATCH; it says nothing about which plane they should match
  in. The real reason is build order -- the orrery builds in ecliptic XY
  unless something calls `orient_to_planet_pole`, and the belt builders
  never did, while Saturn's did. Correct that comment rather than
  preserving it.
**Note:** RICE 2/2/90/2 -> 1.8 is Claude's proposed score.
**Gap:** not a sourcing round and no longer a question. BUILD: spin-axis
basis in both instruments, warp removed, hover reworded (the false L
sentence, the typed width named as a drawing choice beside the sourced
span, the 9.6 degrees as a sentence), both code comments corrected. One
pass, then Mode 5.
**Ref:** L-009 (closed) for the sourced tilts and the cone precedent;
L-061 (open) for the rolling frame; L-305 for the typed 11 in the desktop
magnetopause; L-330 (open) for the belt's SHAPE, deliberately separated
from this. Review by Claude Fable 5.1, 2026-09-15, at orrery `695f1f04`
and gallery `0d8e6044`; five record findings, all five confirmed in the
files by Claude before this was written. An earlier duplicate of this item
was drafted as L-330 on 2026-09-14 and withdrawn unrun.""",
    ),
    (
        "the new L-330 block",
        b"""## A. ACTIVE SEPARATE TRACKS (not orrery-refactor backlog; cross-referenced)

#### [L-001] Food Insecurity (Earth System track)""",
        b"""## A. ACTIVE SEPARATE TRACKS (not orrery-refactor backlog; cross-referenced)

#### [L-330] Belt shape: rings at the peaks, not the served region (Earth exhibit)
<!-- L:330 status:OPEN upd:2026-09-15 section:A flag: rice:3/3/60/3 -->
- **Separate from L-231 on purpose.** L-231 is which PLANE the belts sit
  in and is ruled. This is what SHAPE they are. They were separated so that
  the plane fix, which is nearly free and corrects something visible, is
  not held hostage to a shape change that has to be judged by eye.
  Build the plane first, look at it, then decide this.
- **The gap.** Four edge rows are served and neither instrument reads them:
  inner belt 1.1 to 2.0 R_E, outer 3.0 to 7.0 [verified @0d8e6044]. Both
  draw a ring at the sourced peak with a typed half-width of 0.5 R_E. The
  outer belt is served 4 R_E wide and drawn 0.5.
- **The proposal, from Fable 2026-09-15.** Draw each belt as the region
  between two dipole shells built from its served edges, using the dipole
  L-shell relation r = L cos^2(latitude). It needs NO NEW NUMBER: the
  edges are served, the relation is textbook, and the only declared
  drawing choices are that the region is bounded by dipole field lines and
  cut at the crust. The slot between about 2 and 3 R_E then appears by
  itself rather than being drawn. The sourced peak rings can stay as
  brighter lines inside the region so the peaks remain visible.
- **Why it might be worth it.** It is why trapped particles reach high
  latitudes and why the South Atlantic Anomaly exists, neither of which a
  flat ring can show. For a layperson's learning tool that is the teaching
  content of the whole feature.
- **Why it might not.** The inner belt's inner edge at 1.1 R_E sits inside
  the Low Earth Orbit shell and its field line reaches the surface at about
  17 degrees latitude. Physically right, possibly unreadable against the
  crust and LEO shells. Fable's own fallback: draw the inner belt as a
  plain torus from its edges and keep the shells for the outer belt, whose
  horns are the teaching point. MODE 5 DECIDES, and it cannot be decided
  from code.
- **A wrinkle neither the proposal nor the review resolves.** Dipole shells
  are MAGNETIC geometry. Drawing them about the SPIN axis, as L-231 rules,
  is a hybrid: the daily-average argument still holds but the hover has to
  carry it, and it is a longer sentence than the one a ring needs.
- **Smaller, and independent of all of the above.** The hover prints the
  typed 0.5 R_E as "Band thickness" a few lines above a served note giving
  the true span. That is fixed in L-231's pass, not here, because it is
  wrong whatever shape is drawn.
**Note:** RICE 3/3/60/3 -> 1.8 is Claude's proposed score. Confidence 60
because the physics is settled and the readability is not.
**Gap:** build L-231 first. Then a design round on this, then a decision,
then both instruments in one pass.
**Ref:** L-231 (the plane, ruled) is the prerequisite. L-181 for the belt
and torus numbers being function-local literals. Raised 2026-09-15 from
Fable's review of the plane question.

#### [L-001] Food Insecurity (Earth System track)""",
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
        print("  If either withdrawn patch was run --")
        print("    patch_L330_belt_plane_ledger_item.py, or")
        print("    patch_L231_belt_plane_amendment.py --")
        print("  discard its change and run this one instead. Both are")
        print("  superseded by this patch.")
        print("NOTHING was written.")
        return 1

    if b"L:330" in lf or b"SUPERSEDED 2026-09-1" in lf:
        print("FAILURE: part of this is already in the file."
              " NOTHING was written.")
        return 1

    is_crlf = data.count(b"\r\n") > 0

    def fit(block):
        return block.replace(b"\n", b"\r\n") if is_crlf else block

    for label, old, new in EDITS:
        count = data.count(fit(old))
        if count != 1:
            print("FAILURE: expected 1 match for %s, got %d." % (label, count))
            print("NOTHING was written.")
            return 1

    for label, old, new in EDITS:
        data = data.replace(fit(old), fit(new))

    with open(TARGET, "wb") as handle:
        handle.write(data)

    print("OK: ledger updated.")
    print("    L-231 amended: ruling recorded, five findings, gap rewritten")
    print("    L-305 gap extended: why the typed tilt should not wait")
    print("    L-330 opened: the belt's shape, separate from its plane")
    print("    line endings preserved (%s)" % ("CRLF" if is_crlf else "LF"))
    print()
    print("Next: python ledger_index.py")
    print("      Expect ONE more block than the previous run reported.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
