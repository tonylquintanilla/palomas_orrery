"""
patch_L334_1b_wire_arrival_check_20260917.py -- GALLERY repo. L-334,
piece 1, the two loose ends patch_L334_1 had to leave.

Built on gallery d2ca28b683affb6aee428b96c6bc4cb5364828ae
at https://github.com/tonylquintanilla/tonyquintanilla.github.io

RUN THIS SECOND. Run patch_L334_1_arrival_scene_20260917.py first, from
the gallery repo ROOT. This patch refuses if that one has not run,
because it wires in a check that patch creates.

RUN
---
Save this file in the GALLERY repo root and click Run in VS Code.

    python patch_L334_1b_wire_arrival_check_20260917.py

WHAT IT DOES -- all or nothing
------------------------------
    gallery_maintenance_run.py   one new gating checker, "Arrival", which
                                 runs documentation/smoke_arrival.js.
                                 The run goes from 10 gating checkers to
                                 11.
    gallery/earth_geometry.js    the comment above composeScene described
                                 the L-291 arrival of eight lit shells.
                                 It now says what is true: this function
                                 sets a default, and the page's served
                                 arrival block has the last word. No
                                 code in that file changes.

Why it is separate: on 2026-09-17 both files were fingerprinted by the
unpushed L-322 gallery patch, so patch_L334_1 could not touch them. That
patch is pushed now.

AFTER IT RUNS
-------------
    1. Move this script into documentation/.
    2. python gallery_maintenance_run.py
       Expect 11 of 11 gating checkers, with a row reading
       "Arrival ... both rooms open on the right things".
    3. Commit, push, then both rooms on the phone, portrait first.

UNDO: Discard Changes in GitHub Desktop.

Role: patch
Domain: gallery

Written September 17, 2026 with Anthropic's Claude Fable 5.1.
"""

import hashlib
import os
import sys

FINGERPRINTS = {
    "gallery_maintenance_run.py": "e3eee79f1b4dea54c41bedcf0ec67beb",
    "gallery/earth_geometry.js": "22c70838dab5eb46486456dabff84f09",
}

REQUIRES = os.path.join("documentation", "smoke_arrival.js")

EDITS = [
    ("gallery_maintenance_run.py", [
        (('      "gallery/earth_geometry.js", "interactive.html"],\n'
          '     ".", "===", False),\n'
          '\n'),
         ('      "gallery/earth_geometry.js", "interactive.html"],\n'
          '     ".", "===", False),\n'
          '\n'
          '    # L-334 piece 1 (2026-09-17): what each room opens on. It lifts\n'
          '    # sunApplyArrival out of interactive.html, applies it to both\n'
          '    # rooms with the served arrival blocks, and fails unless exactly\n'
          '    # the expected things are drawn -- the photosphere alone; the\n'
          '    # crust with the axis, the Sun direction and the terminator --\n'
          '    # and the Moon is not. It prints what it found drawn, and it\n'
          '    # checks that an object with no arrival block is left as it was.\n'
          '    ("Arrival", "node",\n'
          '     ["documentation/smoke_arrival.js"], ".", None, False),\n'
          '\n')),
    ]),
    ("gallery/earth_geometry.js", [
        (("   * Arrival policy (Tony's design round, L-291, 2026-09-06/08): eight\n"
          "   * shells lit -- the five interior, the two atmosphere, LEO -- plus the\n"
          "   * axis with the equator and the Sun direction. Everything else is a\n"
          "   * drawer row, unselected. The renderers already send anything larger\n"),
         ("   * ARRIVAL IS NOW DECIDED BY THE PAGE, NOT HERE (Tony's ruling,\n"
          "   * 2026-09-17, L-334): a room opens on the surface shell plus the frame\n"
          "   * elements, with the Moon unticked. The served \"arrival\" block in\n"
          "   * data/objects_config.json names the shells drawn, and\n"
          "   * sunApplyArrival in interactive.html applies it to the traces this\n"
          "   * function returns. So the crust alone is lit, and the terminator,\n"
          "   * which this function still hides, is switched back on by the page as\n"
          "   * a frame element. What follows is the DEFAULT this function sets,\n"
          "   * which is what a visitor gets only if no arrival block is served.\n"
          "   *\n"
          "   * The default (Tony's design round, L-291, 2026-09-06/08): eight\n"
          "   * shells lit -- the five interior, the two atmosphere, LEO -- plus the\n"
          "   * axis with the equator and the Sun direction. Everything else is a\n"
          "   * drawer row, unselected. The renderers already send anything larger\n")),
    ]),
]


def lf(data):
    return data.replace(b"\r\n", b"\n")


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    os.chdir(here)
    if not os.path.exists("gallery_maintenance_run.py"):
        raise SystemExit("ERROR: this script is not in the gallery repo "
                         "root. NOTHING was written.")
    if not os.path.exists(REQUIRES):
        raise SystemExit("ERROR: %s does not exist. Run "
                         "patch_L334_1_arrival_scene_20260917.py first, from "
                         "the gallery repo root. NOTHING was written."
                         % REQUIRES.replace(os.sep, "/"))

    planned = []
    for name, pairs in EDITS:
        with open(name, "rb") as handle:
            old = handle.read()
        if hashlib.md5(lf(old)).hexdigest() != FINGERPRINTS[name]:
            raise SystemExit("ERROR: %s is not the version this patch was "
                             "built on (d2ca28b6), or this patch has already "
                             "run. NOTHING was written." % name)
        was_crlf = b"\r\n" in old
        text = lf(old).decode("utf-8")
        for index, (before, after) in enumerate(pairs):
            if text.count(before) != 1:
                raise SystemExit("ANCHOR FAIL in %s, change %d of %d: found "
                                 "%d matches, expected 1. NOTHING was "
                                 "written." % (name, index + 1, len(pairs),
                                               text.count(before)))
            text = text.replace(before, after)
        data = text.encode("utf-8")
        if was_crlf:
            data = data.replace(b"\n", b"\r\n")
        planned.append((name, data, "%d change(s)" % len(pairs), was_crlf))

    for name, data, _what, _crlf in planned:
        try:
            lf(data).decode("ascii")
        except UnicodeDecodeError:
            raise SystemExit("ERROR: %s would contain non-ASCII text. "
                             "NOTHING was written." % name)

    for name, data, what, was_crlf in planned:
        with open(name, "wb") as handle:
            handle.write(data)
        print("ok  %-32s %s%s" % (name, what,
                                  " [CRLF kept]" if was_crlf else ""))
    print("")
    print("patch applied (%d files)" % len(planned))
    print("Next: move this script into documentation/, then run")
    print("python gallery_maintenance_run.py and expect 11 of 11.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
