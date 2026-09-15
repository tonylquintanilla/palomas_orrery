"""Belts into Earth's equatorial plane, saddle out, and the uncited tilt removed.

Target: earth_visualization_shells.py  (orrery repo root)
Built against orrery 695f1f04a98a925737df929430567957ad62ccaf.
Handles: L-231 (the plane), L-305 (the typed tilt).
2026-09-15, with Anthropic's Claude Opus 5.

THIS IS THE OTHER HALF OF ONE PASS. The gallery half is
patch_L231_belt_plane_gallery.py. Push them together -- scene equivalence
is the standing rule and L-231 names it.

FOUR CHANGES, ALL IN create_earth_magnetosphere_shell
-----------------------------------------------------
1. THE PLANE. The belts were built in the ecliptic XY plane and never
   rotated, while the comment beside them claimed they were around Earth's
   rotational axis. They now pass through orient_to_planet_pole(..., 'Earth')
   before the centre offset, exactly as Saturn's belt builder already does
   at saturn_visualization_shells.py:898. That is the call this module
   never made, which L-231 records as the real reason the ecliptic was
   used -- build order, not a choice.

2. THE SADDLE IS GONE. Every belt point carried z = 0.2 * belt_radius *
   sin(2 * angle): the ring rose and fell a fifth of its radius TWICE per
   circuit. That is more vertical swing than Earth's real 9.6-degree
   magnetic tilt would give, at twice the frequency, and it means nothing.
   The comment beside it said the wobble made the belt "thinner near
   poles"; the code changed no cross-section, it moved the whole ring. Any
   real vertical extent is L-330's question.

3. THE UNCITED 11 DEGREES IS REMOVED. The magnetopause call passed
   magnetic_tilt_deg=11, uncited, while the bow shock call sixty lines
   below passes nothing -- so the desktop drew a leaning magnetopause
   inside an upright bow shock. Already ruled for removal under L-305;
   removed here because it is the same function and the same question
   about which axis things are drawn around. rotate_to_sunward defaults
   this argument to 0, so dropping it is the whole change.

   Earth's real dipole tilt is 9.6 degrees, sourced to IGRF-13, and it is
   shown by the DIPOLE CONE, which is a different element in a different
   frame. It is not applied to a magnetosphere whose two models are both
   fitted symmetric about the Sun line.

4. Both misleading comments are rewritten rather than deleted, so the
   history stays readable.

WHAT DOES NOT CHANGE
--------------------
The belts are still rings at the sourced peaks with a typed width. The
region between the served edges is L-330. The info marker still sits at
the first point of the ring.

I COULD NOT RUN THIS. No tkinter and no live Horizons connection in the
sandbox where it was written. It compiles and the edit is a rotation call
of the same form Saturn already uses, but the render is yours to judge.

AFTER RUNNING
-------------
  python -m py_compile earth_visualization_shells.py
  python provenance_scanner.py          (Tier-1 must not rise)
  Then render Earth with the belts on. Expect: both belts in the same
  plane as the equator and the geostationary ring rather than 23 degrees
  off it, flat rather than saddle-shaped, and the magnetopause upright
  inside the bow shock rather than leaning.

UNDO
----
Nothing is written unless the fingerprint matches. To undo: in GitHub
Desktop, right-click earth_visualization_shells.py in Changes and Discard
Changes.
"""

import hashlib
import os
import sys

TARGET = "earth_visualization_shells.py"
BASE_FP = "f9568635cfe863fab1117e9851091a04"

EDITS = [
    (
        "the pole helper import",
        b"from orrery_rendering import rotate_to_sunward, create_info_marker",
        b"""from orrery_rendering import rotate_to_sunward, create_info_marker
# L-231 (2026-09-15): the belts are drawn in Earth's equatorial plane now,
# using the same call Saturn's belt builder has always used.
from idealized_orbits import orient_to_planet_pole""",
    ),
    (
        "the uncited magnetic tilt on the magnetopause call",
        b"        sun_position=sun_position, magnetic_tilt_deg=11,",
        b"""        # L-305 (2026-09-15): magnetic_tilt_deg=11 removed. It was uncited,
        # it disagreed with the sourced 9.6 in PLANET_DIPOLE, and the bow
        # shock call below passes no tilt at all -- so this leaned the
        # magnetopause inside an upright bow shock. Both boundary models
        # are fitted symmetric about the Sun line from crossings taken at
        # every dipole tilt, so the tilt is already averaged into their
        # coefficients. The dipole cone is where Earth's tilt is shown.
        sun_position=sun_position,""",
    ),
    (
        "the belt ring construction",
        b"""                # Create a belt around Earth's rotational axis
                x = belt_radius * np.cos(angle)
                y = belt_radius * np.sin(angle)
                
                # Add some z variation based on angle to create the shape of a belt
                # rather than a perfect torus (thinner near poles)
                z_scale = 0.2 * belt_radius  # Controls how flat the belts are
                z = z_scale * np.sin(2 * angle)
                """,
        b"""                # A flat ring in the body frame. It becomes a ring around
                # Earth's rotational axis a few lines below, where
                # orient_to_planet_pole rotates it -- which is what the
                # old comment here claimed and the code never did.
                x = belt_radius * np.cos(angle)
                y = belt_radius * np.sin(angle)
                
                # L-231 (Tony's ruling, 2026-09-15): the saddle is gone.
                # This was z = 0.2 * belt_radius * sin(2 * angle), lifting
                # the ring a fifth of its radius TWICE per circuit -- more
                # vertical swing than the real 9.6-degree magnetic tilt
                # would give, at twice the frequency, meaning nothing. The
                # comment here said it made the belt "thinner near poles";
                # it changed no cross-section, it moved the whole ring.
                # Any real vertical extent is L-330's question.
                z = 0.0
                """,
    ),
    (
        "the centre offset, where the rotation belongs",
        b"""        # Apply center position offset
        belt_x = np.array(belt_x) + center_x
        belt_y = np.array(belt_y) + center_y
        belt_z = np.array(belt_z) + center_z""",
        b"""        # L-231 (Tony's ruling, 2026-09-15): into Earth's EQUATORIAL
        # plane, before the centre offset. The deciding argument is the
        # geostationary ring, which is drawn in that plane at 6.6 R_E,
        # inside an outer belt whose sources span 3 to 7 -- the ecliptic
        # put those two 23.4 degrees apart in one picture. The magnetic
        # equator would be better still, but it needs a DIRECTION as well
        # as an angle and that direction turns once a day; the spin
        # equator is its daily average. Same call Saturn's belts use.
        belt_x, belt_y, belt_z = orient_to_planet_pole(
            np.array(belt_x), np.array(belt_y), np.array(belt_z), 'Earth')

        # Apply center position offset
        belt_x = np.array(belt_x) + center_x
        belt_y = np.array(belt_y) + center_y
        belt_z = np.array(belt_z) + center_z""",
    ),
]


def main():
    if not os.path.isfile(TARGET):
        print("FAILURE: %s not found. Run this from the orrery repo root."
              % TARGET)
        print("NOTHING was written.")
        return 1

    with open(TARGET, "rb") as handle:
        data = handle.read()

    actual = hashlib.md5(data.replace(b"\r\n", b"\n")).hexdigest()
    if actual != BASE_FP:
        print("FAILURE: BASE MOVED.")
        print("  expected content md5 %s" % BASE_FP)
        print("  found                %s" % actual)
        print("NOTHING was written.")
        return 1

    if b"orient_to_planet_pole" in data:
        print("FAILURE: this patch is already applied. NOTHING was written.")
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

    print("OK: %s written (%s)." % (TARGET, "CRLF" if is_crlf else "LF"))
    print("    belts rotated into Earth's equatorial plane")
    print("    saddle warp removed")
    print("    uncited magnetic_tilt_deg=11 removed from the magnetopause")
    print()
    print("Next:")
    print("  python -m py_compile earth_visualization_shells.py")
    print("  python provenance_scanner.py")
    print("  Then render Earth and look: belts coplanar with the equator")
    print("  and the GEO ring, flat, and the magnetopause upright inside")
    print("  the bow shock.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
