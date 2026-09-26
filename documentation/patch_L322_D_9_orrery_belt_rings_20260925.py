"""patch_L322_D_9_orrery_belt_rings_20260925.py -- L-322 Stage D, patch D9.

RUN COMMAND

    Save this file in the ROOT of the palomas_orrery repository, open it in
    VS Code and click Run (the same as typing: python
    patch_L322_D_9_orrery_belt_rings_20260925.py). It refuses to run from
    documentation/. After it has run, MOVE it into documentation/.

    Success prints one "ok" line per file and "patch applied". Failure
    prints FAILURE and writes nothing; undo after a success is Discard
    Changes in GitHub Desktop.

WHAT IT CHANGES

    Earth's radiation belts in the orrery, from Tony's notes on patch D8.
    The rings are evenly spaced from each belt's inner edge to its outer
    edge, on a step that also lands on the peak, so the brighter ring sits
    at the peak's true place and every gap is the same: 10 rings for the
    inner belt, 9 for the outer. The peak ring is fully opaque and drawn
    with larger points. Both belt hovers say the belt is one continuous
    region and the rings only mark its extent.

    earth_visualization_shells.py   the belts, their hovers, the new
                                    _even_belt_rings()
    measure_perframe_elements.py    its reduced variant follows the new
                                    ring code
    documentation/RUN_RECORD_L322_D9_20260925.md   new

    Nothing in constants_new.py or in the gallery repository is touched.

    Permanent, once run: _even_belt_rings() and the new drawing. This
    script itself is disposable.

Built on orrery 366fefad9f376a36c386fb9d8b6769f715486c7d
at https://github.com/tonylquintanilla/palomas_orrery.

Written September 25, 2026 with Anthropic's Claude Opus 5.5.
"""

import hashlib
import os
import sys

EDITS = [
    ('earth_visualization_shells.py', 'ae452655899e026a7f37b6bd27e1abcc', '3d02188a2a11526343359ad6966fa394', [
        ('    shared create_magnetosphere_shape; the other planets still do.\nModule updated: September 25, 2026 with Anthropic\'s Claude Opus 5.5\n"""\n',
         '    shared create_magnetosphere_shape; the other planets still do.\nSeptember 25, 2026 (L-322 Stage D, patch D9, Opus 5.5): the belts\' rings\n    are evenly spaced, on a step that lands on both edge rows and on the\n    peak row, so the brighter ring sits at the peak\'s true place and no\n    gap is uneven (Tony\'s Mode 5 note on D8: the uneven gaps read as a\n    physical feature). The peak ring is fully opaque and drawn with larger\n    points. The hover says the belt is one continuous region and the\n    rings only mark its extent.\nModule updated: September 25, 2026 with Anthropic\'s Claude Opus 5.5\n"""\n'),
        ('    if value != int(value):\n        raise ValueError("%s is not a whole number at %s figures"\n                         % (name, figures))\n    return "%d" % int(value)\n',
         '    if value != int(value):\n        raise ValueError("%s is not a whole number at %s figures"\n                         % (name, figures))\n    return "%d" % int(value)\n\n\ndef _even_belt_rings(inner, peak, outer):\n    """Ring radii for one radiation belt, and which ring is the peak.\n\n    The rings are evenly spaced from the inner edge to the outer edge, on\n    the largest step that also lands exactly on the peak: the greatest\n    common divisor of the two distances, edge to peak and peak to edge,\n    taken on the rows\' decimal values. At the rows as they stand, the\n    inner belt gets ten rings with the peak fifth from the inside, and the\n    outer belt nine with the peak fourth. Both peaks sit nearer the inner\n    edge than the middle, and the drawing shows that. (The rows\' values\n    are not repeated here: this comment would be a second home for them.)\n\n    L-322 Stage D, patch D9 (Tony, 2026-09-25, option 2 of two: "even\n    spacing with enough rings so that the peak ring can be identified at\n    the correct radius fraction"). D8 added the peak ring on top of five\n    evenly spaced rings, so it landed beside one of them and the gaps\n    stopped being equal, which read as a physical feature.\n\n    The ring positions are the rows\' own values; only the ring COUNT is a\n    rendering matter, and it follows from the rows. max_rings is a\n    rendering cap: a row typed with more decimals would make the step\n    tiny and the count huge, and this refuses rather than drawing\n    hundreds of rings.\n    """\n    from fractions import Fraction\n    max_rings = 25\n    a = Fraction(inner).limit_denominator(1000)\n    p = Fraction(peak).limit_denominator(1000)\n    b = Fraction(outer).limit_denominator(1000)\n    if not a < p < b:\n        raise ValueError("belt rows out of order: inner %g, peak %g, "\n                         "outer %g" % (inner, peak, outer))\n    low, high = p - a, b - p\n    step = Fraction(math.gcd(low.numerator * high.denominator,\n                             high.numerator * low.denominator),\n                    low.denominator * high.denominator)\n    count = int((b - a) / step) + 1\n    if count > max_rings:\n        raise ValueError("a belt from %g to %g with its peak at %g needs %d "\n                         "evenly spaced rings to put one on the peak; the "\n                         "cap is %d" % (inner, outer, peak, count, max_rings))\n    radii = [float(a + step * k) for k in range(count)]\n    return radii, int((p - a) / step)\n'),
        ('        f"Inner Van Allen Belt: Region of trapped charged particles (mainly protons).<br>"\n        "The rings run across the belt from edge to edge. The brighter ring is the<br>"\n        f"flux peak, {EARTH_VAN_ALLEN_INNER_RADII:g} Earth radii from Earth\'s centre, about<br>"\n',
         '        f"Inner Van Allen Belt: Region of trapped charged particles (mainly protons).<br>"\n        "The belt is one continuous region. The rings only mark its extent: they<br>"\n        "are evenly spaced from its inner edge to its outer edge, and the brighter<br>"\n        f"ring is the flux peak, {EARTH_VAN_ALLEN_INNER_RADII:g} Earth radii from Earth\'s centre, about<br>"\n'),
        ('        f"Outer Van Allen Belt: Region of trapped charged particles (mainly electrons).<br>"\n        "The rings run across the belt from edge to edge. The brighter ring is the<br>"\n        f"flux peak, L = {EARTH_VAN_ALLEN_OUTER_RADII:g} -- about {_km_above_surface(EARTH_VAN_ALLEN_OUTER_RADII, 2):,} km above the<br>"\n',
         '        f"Outer Van Allen Belt: Region of trapped charged particles (mainly electrons).<br>"\n        "The belt is one continuous region. The rings only mark its extent: they<br>"\n        "are evenly spaced from its inner edge to its outer edge, and the brighter<br>"\n        f"ring is the flux peak, L = {EARTH_VAN_ALLEN_OUTER_RADII:g} -- about {_km_above_surface(EARTH_VAN_ALLEN_OUTER_RADII, 2):,} km above the<br>"\n'),
        ('    belt_edge_alpha = 0.2   # the rings across the belt (the old opacity)\n    belt_peak_alpha = 0.6   # the ring at the peak\n',
         '    # L-322 Stage D, patch D9: the rings are evenly spaced on a step that\n    # lands on the edges and the peak (_even_belt_rings), and the peak ring\n    # is fully opaque with larger points. At D8 it was 0.6 against 0.2 at\n    # the same size, which Tony could barely see. Rendering settings.\n    belt_edge_alpha = 0.2   # the rings across the belt (the old opacity)\n    belt_peak_alpha = 1.0   # the ring at the peak\n    belt_edge_size = 1.5    # the old point size\n    belt_peak_size = 3.0\n'),
        ("        belt_point_colors = []\n        belt_rgb = belt_colors[i].replace('rgb(', '').replace(')', '')\n        \n        n_points = 80\n        n_rings = 5\n        \n        ring_radii = [belt_peak] + [\n            belt_inner + (belt_outer - belt_inner) * i_ring / (n_rings - 1)\n            for i_ring in range(n_rings)]\n        for i_ring, ring_radius in enumerate(ring_radii):\n            belt_radius = ring_radius * EARTH_RADIUS_AU\n            ring_alpha = belt_peak_alpha if i_ring == 0 else belt_edge_alpha\n            ring_color = 'rgba(%s, %g)' % (belt_rgb, ring_alpha)\n",
         "        belt_point_colors = []\n        belt_point_sizes = []\n        belt_rgb = belt_colors[i].replace('rgb(', '').replace(')', '')\n        \n        # 48 points a ring (80 at D8, with 6 rings): with 11 and 9 rings\n        # the two belts stay near D8's size per animation frame.\n        n_points = 48\n        \n        ring_radii, peak_ring = _even_belt_rings(belt_inner, belt_peak,\n                                                 belt_outer)\n        for i_ring, ring_radius in enumerate(ring_radii):\n            belt_radius = ring_radius * EARTH_RADIUS_AU\n            is_peak = i_ring == peak_ring\n            ring_color = 'rgba(%s, %g)' % (\n                belt_rgb, belt_peak_alpha if is_peak else belt_edge_alpha)\n            ring_size = belt_peak_size if is_peak else belt_edge_size\n"),
        ('                belt_point_colors.append(ring_color)\n',
         '                belt_point_colors.append(ring_color)\n                belt_point_sizes.append(ring_size)\n'),
        ('                marker=dict(\n                    size=1.5,\n                    # One colour per point, so the peak ring can be\n                    # brighter than the rest (L-322 Stage D, patch D8).\n                    color=belt_point_colors,\n                ),',
         '                marker=dict(\n                    # One colour and one size per point, so the peak ring\n                    # stands out from the rest (L-322 Stage D, D8 and D9).\n                    size=belt_point_sizes,\n                    color=belt_point_colors,\n                ),'),
        ("        traces.append(create_info_marker(\n            belt_x[0], belt_y[0], belt_z[0],\n            belt_colors[i], belt_text[0], belt_names[i],\n            border_color='white' if i == 0 else 'red'\n        ))",
         "        # L-322 Stage D, patch D9: the marker sits on the peak ring's first\n        # point; the rings are in order of radius now, not peak first.\n        marker_index = peak_ring * n_points\n        traces.append(create_info_marker(\n            belt_x[marker_index], belt_y[marker_index], belt_z[marker_index],\n            belt_colors[i], belt_text[0], belt_names[i],\n            border_color='white' if i == 0 else 'red'\n        ))"),
        ('    # promoted (A Drawing Approximation Does Not Promote). The rings run\n    # evenly from the inner edge row to the outer edge row, and one more\n    # ring sits at the peak row, drawn brighter; it comes first, so its\n    # first point carries the info marker. The ring count, the point count\n    # and the two brightnesses are rendering settings.\n',
         '    # promoted (A Drawing Approximation Does Not Promote). Since patch D9\n    # the rings are evenly spaced from the inner edge row to the outer edge\n    # row on a step that also lands on the peak row, and the peak ring is\n    # drawn brighter and larger (_even_belt_rings). The point count, the\n    # brightnesses and the sizes are rendering settings; the ring count\n    # follows from the rows.\n'),
    ]),
    ('measure_perframe_elements.py', '08b503c029845138c38200a1cdba3aea', '41922b496106dd792edadc95f6d797a8', [
        ('Module updated: June 2026 with Anthropic\'s Claude Fable 5\n"""\n',
         'Module updated: June 2026 with Anthropic\'s Claude Fable 5\nModule updated: September 25, 2026 with Anthropic\'s Claude Opus 5.5\n(L-322 Stage D, patch D9: Earth\'s belts now draw a ring count that\nfollows from their rows, so the reduced variant halves the points per\nring, 48 -> 24, and no longer patches a ring count; the row labels say so.)\n"""\n'),
        ('    density: belts 80x5 -> 40x3; the bow-shock call gains n_phi=15,',
         '    density: belts 48 -> 24 points a ring (their ring count follows from\n    the belt rows since L-322 Stage D, patch D9, and is not patched); the\n    bow-shock call gains n_phi=15,'),
        ("    assert src.count(b'n_points = 80') == 1, 'belt n_points literal moved'\n    assert src.count(b'n_rings = 5') == 1, 'belt n_rings literal moved'\n    patched = (src.replace(b'n_points = 80', b'n_points = 40')\n                  .replace(b'n_rings = 5', b'n_rings = 3')\n",
         "    assert src.count(b'n_points = 48') == 1, 'belt n_points literal moved'\n    patched = (src.replace(b'n_points = 48', b'n_points = 24')\n"),
        ("    row('Earth magnetosphere FULL (belts 80x5, shock 30x30)',",
         "    row('Earth magnetosphere FULL (belts 48/ring, shock 30x30)',"),
        ("    row('Earth magnetosphere REDUCED (belts 40x3, shock 15x15)',",
         "    row('Earth magnetosphere REDUCED (belts 24/ring, shock 15x15)',"),
    ]),
]

NEW_FILES = [
    ('documentation/RUN_RECORD_L322_D9_20260925.md', '7f52c8253d41448701a20591aec359a2',
     '# Run record -- L-322 Stage D, patch D9: the belts\' rings, evenly spaced\n\n**Built on orrery `366fefad9f376a36c386fb9d8b6769f715486c7d` at\nhttps://github.com/tonylquintanilla/palomas_orrery.** Gallery untouched,\nat `a21680abf2f6daefb2f639fde28100252eb16b03`.\n\nA follow-up to patch D8 (`RUN_RECORD_L322_D8_20260925.md`), from Tony\'s\nMode 5 notes on it. Rules as for D8.\n\nWritten for Tony and for the session that builds gallery patch 3.\n\n---\n\n## 1. Why\n\nTony\'s notes on D8, 2026-09-25: from the hover it was unclear whether\nthe rings are separate features or a way of drawing one region; the\nbrighter ring was barely brighter; and the gaps between rings were\nuneven, which suggests a physical feature rather than a drawing. The\nuneven gaps came from D8 itself: the peak ring was added on top of five\nevenly spaced rings, so it landed beside one of them.\n\nNeither belt peaks at its middle. The inner belt runs 1.1 to 2.0 Earth\nradii and peaks at 1.5; the outer runs 3 to 7 and peaks at 4.5. So an\nodd number of evenly spaced rings would put its centre ring at the\nmiddle, not at the peak. Two options were put to Tony; he chose the\nsecond (2026-09-25): "even spacing with enough rings so that the peak\nring can be identified at the correct radius fraction, plus text\nexplanation."\n\n## 2. What the patch changes\n\n- `earth_visualization_shells.py`\n  - New `_even_belt_rings()`: the rings are evenly spaced from the inner\n    edge row to the outer edge row, on the largest step that also lands\n    exactly on the peak row. The inner belt gets 10 rings, every 0.1\n    Earth radii, with the peak the fifth from the inside. The outer belt\n    gets 9, every 0.5, with the peak the fourth. The ring count follows\n    from the rows; if a row were ever typed so the step became tiny, the\n    function refuses above 25 rings rather than drawing hundreds.\n  - The peak ring is fully opaque (it was 0.6) and its points are twice\n    the size (3.0 against 1.5). The other rings are as before.\n  - 48 points a ring, where D8 had 80 with 6 rings, so the belts stay\n    about the same size per animation frame.\n  - The info marker sits on the peak ring.\n  - Both belt hovers say the belt is one continuous region and the rings\n    only mark its extent (section 4).\n- `measure_perframe_elements.py`: its reduced variant patched two\n  literals, `n_points = 80` and `n_rings = 5`. The ring count is no longer\n  a literal, so it now halves the points a ring, 48 to 24, and its row\n  labels say so.\n- A new file, this run record, in `documentation/`.\n\nWhat moves on screen: the belts\' rings, and the belts\' cross markers.\nNothing else.\n\n## 3. How it was verified, in the sandbox\n\n- The ring helper, on the rows: inner belt 1.1 to 2.0 in ten rings with\n  one gap size, 0.1, and the peak ring exactly at 1.5; outer belt 3 to 7\n  in nine rings, one gap size, 0.5, the peak exactly at 4.5.\n- It fails when it should: an inner edge typed as 1.13 needs 88 rings and\n  is refused; edges out of order are refused.\n- The drawn traces: the inner belt 480 points, the outer 432; two point\n  sizes and two brightnesses in each; each cross marker at the peak\'s\n  radius, 1.500 and 4.500 Earth radii.\n- The agentic pre-test: both files and `palomas_orrery.py` compile; the\n  orrery starts headless on a throwaway copy with no errors; the\n  live-dispatch test built Earth\'s shells through\n  `create_celestial_body_visualization` and found the new belt sentence\n  in the hovers.\n- The Earth pole of date checks, 14 of 14.\n- The per-frame size: 208.5 KB a frame, against D8\'s 209.6.\n- The longest rendered hover line is 90 characters.\n- The provenance scanner, compared as counted lists of every finding by\n  kind, claim and score: 1083 before and after, none lost, none gained.\n  A first draft typed the belt rows\' values into the new function\'s\n  docstring as an example; the scanner raised it as an uncited claim,\n  and the docstring now describes the rings in words.\n- **A finding about my own check.** For D8 I compared the scanner\'s\n  findings as a SET of names. A set cannot see a second finding that\n  looks like one already there, so that comparison could pass blind.\n  For D8 the scanner\'s own count agreed (295 before and after), so D8\'s\n  result stands. This record\'s comparison counts duplicates.\n\n## 4. The visitor-facing text, old and new\n\nInner belt, old:\n\n    The rings run across the belt from edge to edge. The brighter ring is the\n    flux peak, 1.5 Earth radii from Earth\'s centre, about\n\nInner belt, new:\n\n    The belt is one continuous region. The rings only mark its extent: they\n    are evenly spaced from its inner edge to its outer edge, and the brighter\n    ring is the flux peak, 1.5 Earth radii from Earth\'s centre, about\n\nThe outer belt\'s hover changes the same way, ending "ring is the flux\npeak, L = 4.5 -- about 22,000 km above the". The rest of both hovers is\nunchanged.\n\n## 5. For gallery patch 3\n\nDraw the belts the same way: evenly spaced rings from the served inner\nedge to the served outer edge, on the step that also lands on the served\npeak, with the peak ring brighter and larger, and the same hover\nsentence. The step can be computed in the page the same way, from the\nserved values.\n\n## 6. Tony\'s run\n\n(Append the patch output, the maintenance run\'s result, and what the plot\nshowed.)\n\n---\n\nSession written September 2026 with Anthropic\'s Claude Opus 5.5.\n'),
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
          "and Manual scale set to 0.01 AU. Each radiation belt should be "
          "rings with equal gaps, and one ring clearly brighter and "
          "thicker, nearer the inner edge than the middle.")
    print("  2. Hover each belt's cross, which now sits on its bright ring, "
          "and read the new sentence. Old and new are side by side in "
          "section 4 of documentation/RUN_RECORD_L322_D9_20260925.md.")
    print("  3. Run the orrery maintenance run.")
    print("  4. Commit and push, and move this script into documentation/.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
