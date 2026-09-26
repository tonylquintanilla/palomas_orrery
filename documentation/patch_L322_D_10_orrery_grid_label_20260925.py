"""patch_L322_D_10_orrery_grid_label_20260925.py -- L-322 Stage D, patch D10.

RUN COMMAND

    Save this file in the ROOT of the palomas_orrery repository, open it in
    VS Code and click Run (the same as typing: python
    patch_L322_D_10_orrery_grid_label_20260925.py). It refuses to run from
    documentation/. After it has run, MOVE it into documentation/.

    Success prints one "ok" line per file and "patch applied". Failure
    prints FAILURE and writes nothing; undo after a success is Discard
    Changes in GitHub Desktop.

WHAT IT CHANGES

    Every orrery plot page gets a small label naming the grid spacing, as
    the gallery's rooms have: for example "grid 0.0002 AU (29,920 km)".
    It reads the spacing Plotly actually drew, so it stays right under
    Auto scale, after a Fly To button, and during camera tracking. Pages
    not drawn in AU (star maps in light-years, 2D charts) get no label.

    save_utils.py      new _inject_grid_label(), called from _write_html
    documentation/RUN_RECORD_L322_D10_20260925.md   new

    Nothing in constants_new.py or in the gallery repository is touched.

    Permanent, once run: _inject_grid_label() and the label on every
    orrery page. This script itself is disposable.

Built on orrery d3135ce8ac062e53b48b4ca6543bcda596cd31ee
at https://github.com/tonylquintanilla/palomas_orrery.

Written September 25, 2026 with Anthropic's Claude Opus 5.5.
"""

import hashlib
import os
import sys

EDITS = [
    ('save_utils.py', 'fd758a8782ddf5e356d2fb040aaed5f6', 'cedb6502386059b18c56a1baacff72aa', [
        ('Module updated: May 2026 with Anthropic\'s Claude Opus 4.6\n"""\n',
         'Module updated: May 2026 with Anthropic\'s Claude Opus 4.6\nModule updated: September 25, 2026 with Anthropic\'s Claude Opus 5.5\n(L-322 Stage D, patch D10: every HTML page whose 3D scene is drawn in AU\nalso gets a small label naming the grid spacing, as the gallery\'s rooms\nhave, read from what Plotly drew so it stays right under Auto scale, Fly\nTo and camera tracking; see _inject_grid_label.)\n"""\n'),
        ('\n\ndef _write_html(fig, file_path, offline=False, auto_play=False):\n',
         '\n\ndef _grid_label_unit(fig):\n    """The unit of a figure\'s 3D scene when it is drawn in AU, else None.\n\n    The grid label is for the orrery\'s own scenes, whose axes are titled\n    "X (AU)" by visualization_utils.build_scene_axis. Other plots that\n    come through this writer -- star maps in light-years, 2D charts --\n    have no such title and get no label, rather than a label with the\n    wrong unit. (L-322 Stage D, patch D10.)\n    """\n    try:\n        title = fig.layout.scene.xaxis.title.text\n    except (AttributeError, ValueError):\n        return None\n    if title and \'(AU)\' in title:\n        return \'AU\'\n    return None\n\n\ndef _inject_grid_label(fig, html_str):\n    """Inject a small label naming the grid spacing of the 3D scene.\n\n    Shows, for example, "grid 0.0002 AU (29,920 km)", as the gallery\'s\n    rooms do. Tony, 2026-09-25: it "helps greatly in orientation\n    especially in close views."\n\n    The script reads the spacing Plotly ACTUALLY drew, from the page\'s\n    own layout after each redraw, not the one Python asked for. Three\n    cases need that: Auto scale, where Python sets no spacing and Plotly\n    picks its own; the Fly To buttons, which change the scale after the\n    plot is made; and camera tracking in animations, which changes it on\n    every frame. It only reads Plotly\'s layout and writes one small box,\n    so it cannot change the plot.\n\n    Below a thousandth of an AU the kilometre figure is shown too, from\n    KM_PER_AU in constants_new.py, exact, so the page never types its own\n    copy. The label is hidden when the grid is hidden. Where it sits on\n    the page is a rendering setting, for Tony\'s eye.\n\n    Returns the HTML unchanged when the figure has no 3D scene in AU.\n    (L-322 Stage D, patch D10, September 25, 2026, with Anthropic\'s\n    Claude Opus 5.5.)\n    """\n    unit = _grid_label_unit(fig)\n    if unit is None:\n        return html_str\n    from constants_new import KM_PER_AU\n    block = """\n<!-- ===== GRID LABEL ===== -->\n<div id="orrery-grid-label" style="position:fixed; left:21%; bottom:14px;\n  z-index:1000; padding:3px 9px; border-radius:4px;\n  background:rgba(0,0,0,0.65); border:1px solid #555; color:#ddd;\n  font:13px Arial, sans-serif; pointer-events:none; display:none"></div>\n<script>\n(function() {\n  var UNIT = __UNIT__;\n  var KM_PER_AU = __KM_PER_AU__;\n  var label = document.getElementById(\'orrery-grid-label\');\n  function spacing(ax) {\n    // Plotly writes the spacing it drew into the full layout, whether it\n    // was asked for (dtick) or chosen by Plotly (Auto scale).\n    if (!ax || ax.visible === false || ax.showgrid === false) return null;\n    var d = Number(ax.dtick);\n    return (d > 0 && isFinite(d)) ? d : null;\n  }\n  function text(d) {\n    // As many digits as the spacing has and no more: 0.0002, 0.25, 5.\n    return String(Number(d.toPrecision(12))) + \' \' + UNIT;\n  }\n  function update() {\n    var gd = document.querySelector(\'.plotly-graph-div\');\n    var sc = gd && gd._fullLayout && gd._fullLayout.scene;\n    if (!sc) { label.style.display = \'none\'; return; }\n    var dx = spacing(sc.xaxis), dy = spacing(sc.yaxis), dz = spacing(sc.zaxis);\n    if (dx === null && dy === null && dz === null) {\n      label.style.display = \'none\'; return;\n    }\n    var html;\n    if (dx !== null && dx === dy && dx === dz) {\n      html = \'grid <b>\' + text(dx) + \'</b>\';\n      if (dx < 1e-3) {\n        html += \' (\' + (dx * KM_PER_AU).toLocaleString(\'en-US\',\n                {maximumFractionDigits: 0}) + \' km)\';\n      }\n    } else {\n      // The three axes do not share one spacing (possible under Auto\n      // scale): name each rather than pretend.\n      var parts = [];\n      [[\'x\', dx], [\'y\', dy], [\'z\', dz]].forEach(function(p) {\n        if (p[1] !== null) parts.push(p[0] + \' \' + text(p[1]));\n      });\n      html = \'grid <b>\' + parts.join(\', \') + \'</b>\';\n    }\n    if (label.innerHTML !== html) label.innerHTML = html;\n    label.style.display = \'block\';\n  }\n  function later() {\n    // After a redraw Plotly has written the new spacing; read it on the\n    // next frame, and once more shortly after for slow redraws.\n    window.requestAnimationFrame(update);\n    setTimeout(update, 300);\n  }\n  function wire() {\n    var gd = document.querySelector(\'.plotly-graph-div\');\n    if (gd && typeof gd.on === \'function\' && gd._fullLayout) {\n      [\'plotly_afterplot\', \'plotly_relayout\', \'plotly_redraw\',\n       \'plotly_animated\', \'plotly_animatingframe\'].forEach(function(ev) {\n        gd.on(ev, later);\n      });\n      later();\n    } else {\n      setTimeout(wire, 100);\n    }\n  }\n  wire();\n})();\n</script>\n<!-- ===== END GRID LABEL ===== -->\n""".replace(\'__UNIT__\', json.dumps(unit)).replace(\n        \'__KM_PER_AU__\', repr(float(KM_PER_AU)))\n    return html_str.replace(\'</body>\', block + \'\\n</body>\')\n\n\ndef _write_html(fig, file_path, offline=False, auto_play=False):\n'),
        ('    # Inject camera-tracking relayout script if tracking data is present\n    html_str = _inject_camera_tracking(fig, html_str)\n    \n    # Write with binary mode to preserve encoding\n',
         '    # Inject camera-tracking relayout script if tracking data is present\n    html_str = _inject_camera_tracking(fig, html_str)\n\n    # Inject the grid-spacing label when the 3D scene is drawn in AU\n    # (L-322 Stage D, patch D10).\n    html_str = _inject_grid_label(fig, html_str)\n    \n    # Write with binary mode to preserve encoding\n'),
    ]),
]

NEW_FILES = [
    ('documentation/RUN_RECORD_L322_D10_20260925.md', 'f073e32f6e7d3a3e2b4513ee982e83b9',
     '# Run record -- L-322 Stage D, patch D10: a grid label on every orrery plot\n\n**Built on orrery `d3135ce8ac062e53b48b4ca6543bcda596cd31ee` at\nhttps://github.com/tonylquintanilla/palomas_orrery.** Gallery untouched,\nat `a21680abf2f6daefb2f639fde28100252eb16b03`.\n\nRules: protocol v3.68, orrery-coding-conventions 1.9, safe-file-editing\n1.11, agentic-pre-test 1.2, provenance-discipline 2.18.\n\nWritten for Tony and for any later session that touches the orrery\'s\nHTML pages.\n\n---\n\n## 1. Why\n\nTony, 2026-09-25, comparing the gallery\'s Earth room with the orrery\'s\nEarth plot: the gallery names its grid spacing ("0.0002 AU"), and that\n"helps greatly in orientation especially in close views." He asked for\nthe same in the orrery. He chose the label alone, not the gallery\'s\nturning triad of arrows ("confirmed as recommended"): the orrery\'s\n"Ecliptic Coordinates" box already says which axis is which, and the\ntriad would be a much larger job.\n\n## 2. What the patch changes\n\nOne file, `save_utils.py`, whose `_write_html` writes every orrery plot\nto its HTML page.\n\n- New `_inject_grid_label()`, called from `_write_html` after the two\n  page scripts it already adds (the encyclopedia and the camera\n  tracking). It adds a small box, "grid 0.0002 AU (29,920 km)", in the\n  lower left of the page.\n- The script reads the spacing Plotly actually drew, from the page\'s own\n  layout after every redraw. So it is right under Auto scale, where\n  Python sets no spacing and Plotly picks its own; after a Fly To button,\n  which changes the scale after the plot is made; and during camera\n  tracking in an animation, which changes it every frame. It only reads\n  the layout and writes the box; it cannot change the plot.\n- Below a thousandth of an AU the box also gives kilometres, from\n  `KM_PER_AU` in `constants_new.py`, as the gallery does.\n- If the three axes ever drew different spacings, it names each.\n- It appears only on a 3D scene whose axes are titled in AU, which is\n  every orrery scene. Star maps in light-years and 2D charts that use the\n  same writer get no label rather than a label in the wrong unit. It\n  hides when the grid is hidden.\n- Where it sits (21 percent from the left, 14 pixels from the bottom,\n  below the scene\'s left edge) is a rendering setting, for Tony\'s eye.\n\nNothing on the plot itself moves.\n\n## 3. How it was verified, in the sandbox\n\nFive test pages written through the real `_write_html`, opened in a\nheadless Chromium with WebGL:\n\n- A close manual scale, half-width 0.001 AU: "grid 0.0002 AU (29,920\n  km)". After a relayout like a Fly To button, to a 0.02 AU grid: "grid\n  0.02 AU". After a camera zoom: unchanged, as it should be, since\n  zooming the camera does not change the grid.\n- Auto scale, where Plotly chose the spacing: "grid 0.0005 AU (74,799\n  km)", matching the 0.0005 Plotly reported on all three axes.\n- A scene titled in light-years: no label.\n- A scene with the grid hidden: no label.\n- A 40 AU scale: "grid 10 AU".\n- An animation whose frames change the scale from a 0.2 to a 0.002 AU\n  grid: the label followed, ending at "grid 0.002 AU".\n- No script errors on any page.\n\nThe agentic pre-test: `save_utils.py` and `palomas_orrery.py` compile,\nand the orrery starts headless on a throwaway copy with no errors. The\nprovenance scanner, compared as counted lists of every finding: 1083\nbefore and after, none gained, none lost.\n\nWhat could not be tested here: a real orrery plot, which needs Horizons.\nYour plot is the test.\n\n## 4. Tony\'s run\n\n(Append the patch output, the maintenance run\'s result, and what the plot\nshowed.)\n\n---\n\nSession written September 2026 with Anthropic\'s Claude Opus 5.5.\n'),
]


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
        print("ok  %-48s %s" % (name, what))
    for line in notes:
        print("note: " + line)
    print("")
    print("patch applied (%d file(s))" % len(planned))
    print("")
    print("DO THESE, IN THIS ORDER:")
    print("  1. Plot Earth as the center with Earth's magnetosphere ticked "
          "and Manual scale set to 0.01 AU. A small box in the lower left "
          "should read the grid spacing, for example \"grid 0.002 AU\"; "
          "kilometres are added below 0.001 AU. Check it against the grid "
          "you see.")
    print("  2. Try a Fly To button, and an Auto scale plot. The box should "
          "change to the new spacing each time. Say if it sits badly on "
          "the page; where it sits is a setting.")
    print("  3. Run the orrery maintenance run.")
    print("  4. Commit and push, and move this script into documentation/.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
