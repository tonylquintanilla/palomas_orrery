"""patch_L322_D_5_orrery_earth_cone_hover_20260923.py -- L-322 Stage D, patch D5.

RUN COMMAND

    Save this file in the ROOT of the palomas_orrery repository, open it in
    VS Code and click Run. It refuses to run from documentation/. After it
    has run, MOVE it into documentation/.

    This replaces patch_L322_D_5_orrery_cone_hover_wrap_20260923.py, which
    was never run. Delete that one.

WHAT IT CHANGES, and what stays

    One file, planet_visualization_utilities.py: the magnetic dipole cone
    and its hover. Tony, 2026-09-23: the Earth slice is the time to clean
    up this hover.

    Earth's cone hover:
      - The tilt prints once, "Dipole tilt: 9.4105 deg from the spin axis",
        from EARTH_DIPOLE_TILT_DEG at its declared count. It printed
        "~9.4" on the first line and "9.4105" further down, the first a
        display choosing its own count (provenance-discipline Rule 7). The
        note below it now gives only the epoch and the yearly rate.
      - The typed centre offset is removed: 0.085 Earth radii, 540 km and
        22 N 140 E had no row and no source read. The cone's apex, which
        was moved 0.085 Earth radii (about 540 km) north along the spin
        axis, goes back to Earth's centre. The drawing had also put the
        whole offset along the axis, while the note said it points mostly
        sideways. The hover now says the offset exists and is not drawn
        because its size and direction are not yet sourced.
    Every cone hover (all six bodies):
      - "Drawn axis is ONE arbitrary instant; the cone is the honest sweep"
        becomes "The line shows the magnetic axis at one moment; the cone
        shows every direction it points during one turn".
      - Lines longer than 70 characters wrap at a space.

    What moves on screen: Earth's dipole cone, by 0.085 Earth radii, to
    start at Earth's centre. Nothing else moves. The other bodies' typed
    tilts and offsets are untouched; each is its own slice.

    Nothing in the gallery repository is touched.

Built on orrery 50343e03f9f98240acbccdf117117dd2ca072851
at https://github.com/tonylquintanilla/palomas_orrery.

Written September 23, 2026 with Anthropic's Claude Opus 5.5.
"""

import hashlib
import os
import sys

EDITS = [
    ('planet_visualization_utilities.py', 'bfb3c487ec26ef7a8e937b6aab156488', 'ec6d2a5304b9a90ce20ba0ae1ba9bbdb', [
        ("Stage D, patch D3: Earth's axis hover prints the tilt of the plot's date,\nfrom earth_pole_of_date.py, where it typed a fixed tilt)\n",
         "Stage D, patch D3: Earth's axis hover prints the tilt of the plot's date,\nfrom earth_pole_of_date.py, where it typed a fixed tilt)\n\nModule updated: September 23, 2026 with Anthropic's Claude Opus 5.5 (L-322\nStage D, patch D5, Earth's dipole cone hover, on Tony's instruction that\nthe Earth slice is the time to clean it: the tilt prints once, from the\nrow, at its declared count, where it printed a rounded copy beside it;\nthe line about the drawn instant is in plain words; the typed centre\noffset is removed, the cone's apex goes back to Earth's centre, and the\nhover says the offset is not drawn and why. And every cone hover wraps\nlong lines.)\n"),
        ('import math\nimport numpy as np\n',
         'import math\nimport textwrap\nimport numpy as np\n'),
        ('    sign said in words. Used only on the two small numbers in the Earth\n    dipole note below.\n',
         "    sign said in words. Used on Earth's dipole tilt line and on the rate\n    in the Earth dipole note below.\n"),
        ("_EARTH_DIPOLE_NOTE = 'Tilt %s deg at epoch 2020.0 (IGRF-13); %s about %s deg a year' % (\n    _declared_count('EARTH_DIPOLE_TILT_DEG', EARTH_DIPOLE_TILT_DEG),\n    'decreasing' if EARTH_DIPOLE_TILT_RATE_DEG_PER_YEAR < 0 else 'increasing',\n",
         "# L-322 Stage D, patch D5: the tilt itself is printed once, on the first\n# line of the hover (_EARTH_DIPOLE_TILT_LINE); this note carries its epoch\n# and its rate, and no longer repeats it.\n_EARTH_DIPOLE_TILT_LINE = 'Dipole tilt: %s deg from the spin axis' % (\n    _declared_count('EARTH_DIPOLE_TILT_DEG', EARTH_DIPOLE_TILT_DEG))\n_EARTH_DIPOLE_NOTE = ('The tilt is for epoch 2020.0 (IGRF-13) and is %s by '\n                      'about %s deg a year') % (\n    'decreasing' if EARTH_DIPOLE_TILT_RATE_DEG_PER_YEAR < 0 else 'increasing',\n"),
        ("    'Earth':   {'tilt_deg': EARTH_DIPOLE_TILT_DEG, 'azimuth_deg': 0.0,\n                'offset_fraction': 0.085,\n                'offset_note': 'Center offset: ~0.085 R_E northward, axial '\n                               'approximation (~540 km); the true center is also '\n                               'displaced laterally toward ~22 N, 140 E '\n                               '(secular variation, unmodeled here)',\n",
         "    # L-322 Stage D, patch D5 (2026-09-23): the offset_fraction of 0.085 and\n    # the note's 540 km and 22 N 140 E were typed, with no row and no read\n    # (A Drawing Approximation Does Not Promote). The drawing was also wrong\n    # in shape: it moved the apex along the spin axis by the whole offset,\n    # while the note itself said the offset points mostly sideways. The\n    # sideways part turns with Earth once a day, and the orrery does not\n    # draw Earth turning. So the apex is at the centre, and the hover says\n    # the offset exists and why it is not drawn. The paper to source it\n    # from, Koochak and Fraser-Smith (2017), Earth and Space Science 4,\n    # 626, doi:10.1002/2017EA000280, could not be opened from this session;\n    # the gap is recorded on L-322.\n    'Earth':   {'tilt_deg': EARTH_DIPOLE_TILT_DEG, 'azimuth_deg': 0.0,\n                'tilt_line': _EARTH_DIPOLE_TILT_LINE,\n                'offset_note': 'The magnetic centre is not exactly at '\n                               'Earth\\'s centre. That offset is not drawn, '\n                               'because its size and direction are not yet '\n                               'sourced here.',\n"),
        ("    else:\n        lines.append('Dipole tilt: ~%.1f deg from the spin axis' % dip['tilt_deg'])\n        lines.append('Swept about the spin axis once per rotation (sense: %s)'\n                     % rot.get('sense'))\n        lines.append('Drawn axis is ONE arbitrary instant; the cone is the honest sweep')\n",
         '    else:\n        # L-322 Stage D, patch D5: a body whose tilt is a row prints it\n        # from the row (\'tilt_line\'); the others keep the old line until\n        # their own slice reaches them.\n        lines.append(dip.get(\'tilt_line\',\n                             \'Dipole tilt: ~%.1f deg from the spin axis\'\n                             % dip[\'tilt_deg\']))\n        lines.append(\'Swept about the spin axis once per rotation (sense: %s)\'\n                     % rot.get(\'sense\'))\n        # Plain words for what was "Drawn axis is ONE arbitrary instant;\n        # the cone is the honest sweep" (Tony\'s hover-text rule).\n        lines.append(\'The line shows the magnetic axis at one moment; the \'\n                     \'cone shows every direction it points during one turn\')\n'),
        ("    lines.append('Source: %s' % dip['source'])\n    hover = '<br>'.join(lines)\n",
         "    lines.append('Source: %s' % dip['source'])\n    # L-322 Stage D, patch D5: a hover does not wrap by itself, so a long\n    # line runs across the screen. Earth's centre-offset line was 167\n    # characters; Mercury's, Jupiter's and Saturn's notes ran past 150.\n    # Each line is broken at spaces to at most 70 characters (a rendering\n    # setting). Words and numbers are unchanged by the wrap.\n    hover = '<br>'.join('<br>'.join(textwrap.wrap(line, 70)) or line\n                        for line in lines)\n"),
    ]),
]

NEW_FILES = []


def content(raw):
    """LF-normalised bytes: line endings are not content."""
    return raw.replace(b"\r\n", b"\n")


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    if os.path.basename(here) == "documentation":
        print("ERROR: run this from the repository ROOT, not from "
              "documentation/. Move it up one level, run it, then move it "
              "back. NOTHING was written.")
        return 1
    store = os.path.join(here, "constants_new.py")
    if not os.path.exists(store):
        print("ERROR: constants_new.py is not beside this script, so this "
              "is not the orrery root. NOTHING was written.")
        return 1
    with open(store, "rb") as handle:
        pass
    if not os.path.exists(os.path.join(here, "earth_pole_of_date.py")):
        print("ERROR: patch D3 has not been applied (earth_pole_of_date.py "
              "is missing). NOTHING was written.")
        return 1

    planned = []
    problems = []
    notes = []
    already = 0
    for name, base_fp, want_fp, hunks in EDITS:
        path = os.path.join(here, name)
        if not os.path.exists(path):
            problems.append("%s: not found" % name)
            continue
        with open(path, "rb") as handle:
            raw = handle.read()
        is_crlf = b"\r\n" in raw
        body = content(raw)
        actual = hashlib.md5(body).hexdigest()
        if actual == want_fp:
            problems.append("%s: already carries this patch's result -- a "
                            "second run" % name)
            already += 1
            continue
        if actual != base_fp:
            problems.append("%s: BASE MOVED. Expected %s, found %s"
                            % (name, base_fp[:12], actual[:12]))
            continue
        if is_crlf:
            notes.append("%s: the working copy is CRLF; written back CRLF"
                         % name)
        text = body.decode("utf-8")
        for index, (old, new) in enumerate(hunks, 1):
            found = text.count(old)
            if found != 1:
                problems.append("%s: ANCHOR FAIL, edit %d of %d matched %d "
                                "times" % (name, index, len(hunks), found))
                break
            if any(ord(ch) > 127 for ch in new):
                problems.append("%s: edit %d inserts a non-ASCII character"
                                % (name, index))
                break
            text = text.replace(old, new)
        else:
            out = text.encode("utf-8")
            if hashlib.md5(out).hexdigest() != want_fp:
                problems.append("%s: the result is not the file this patch "
                                "was built to produce" % name)
                continue
            planned.append((path, out.replace(b"\n", b"\r\n") if is_crlf
                            else out, name, "%d edit(s)" % len(hunks)))
    for name, want_fp, text in NEW_FILES:
        path = os.path.join(here, name)
        data = text.encode("utf-8")
        if hashlib.md5(data).hexdigest() != want_fp:
            problems.append("%s: the text in this patch is damaged" % name)
            continue
        if os.path.exists(path):
            with open(path, "rb") as handle:
                if hashlib.md5(content(handle.read())).hexdigest() == want_fp:
                    problems.append("%s: already exists with this patch's "
                                    "content -- a second run" % name)
                else:
                    problems.append("%s: already exists with OTHER content; "
                                    "this patch will not overwrite it" % name)
            continue
        planned.append((path, data, name, "new file"))

    if problems:
        print("FAILURE -- NOTHING was written:")
        for line in problems:
            print("  " + line)
        print("")
        print("Undo is Discard Changes in GitHub Desktop.")
        return 1

    for path, data, name, what in planned:
        with open(path, "wb") as handle:
            handle.write(data)
        print("ok  %-36s %s" % (name, what))
    for line in notes:
        print("note: " + line)
    print("")
    print("patch applied (%d file(s))" % len(planned))
    print("")
    print("DO THESE, IN THIS ORDER:")
    print("  1. Plot Earth as the center, Auto scale, crust, axis and dipole "
          "cone shown. The cone should now start at Earth's centre. Hover "
          "its tip: the tilt appears once, and no line runs far past the "
          "others.")
    print("  2. Run the orrery maintenance run.")
    print("  3. Commit and push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
