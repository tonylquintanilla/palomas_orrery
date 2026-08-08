"""
patch_mode5_linebreaks.py

Mode 5 follow-up. Tony's render check found both derived sentences run
past the wrap width their neighbouring lines use. Adds line breaks.

Built on 9b4f2788ea0a95ac5c51489219020c5864898f6e at
https://github.com/tonylquintanilla/palomas_orrery (branch main).

HOW TO RUN
    Save into the palomas_orrery folder, open in VS Code, click Run.

WHAT IT DOES
    solar_visualization_shells.py
        GRAVITATIONAL_INFLUENCE_SENTENCE  one line -> two
        CHROMOSPHERE_RADIUS_LINE          one line -> three

    Rendered result in the Plotly hover:

      The Sun's gravitational influence extends to roughly 2.4 light-years
      (~150,000 AU).
      Published estimates range 100,000-200,000 AU (1.6-3.2 light-years);
      this visualization draws the midpoint.

      * Radius: drawn from the photosphere out to 1.1 solar radii
        (~0.00465 - 0.00512 AU).
        A stylization for visibility: the physical chromosphere extends
        only ~2,000 km above the photosphere (~1.003 solar radii).

NOTE ON THE TRADEOFF
    This adds two `<br>` tags, which the Tkinter checkbox tooltips render
    LITERALLY rather than as line breaks. That is the wrong direction, and
    it is accepted here only because those tooltips already carry 642 of
    them in this file alone. The real fix is L-181's canonical direction:
    author display text in `\\n` and convert to `<br>` at the Plotly
    boundary, so one source serves both surfaces. Tony's Mode 5 pass
    established the scope -- every solar shell GUI tooltip is affected,
    not just these two.

SAFETY
    Content-fingerprinted, anchors asserted to match exactly once, line
    endings preserved. Any mismatch aborts with NOTHING WAS WRITTEN.

Module updated: August 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import pathlib
import sys

TARGET = 'solar_visualization_shells.py'
CONTENT_FINGERPRINT = '0475f952a2667e4504591b9f04d886b4'

EDITS = [
    (
        "gravitational influence sentence: break after the AU figure",
        b"    f\"(~{GRAVITATIONAL_INFLUENCE_AU:,.0f} AU). Published estimates range \"\n",
        b"    f\"(~{GRAVITATIONAL_INFLUENCE_AU:,.0f} AU).<br>\"\n"
        b"    f\"Published estimates range \"\n",
    ),
    (
        "chromosphere radius line: break after the AU range and mid-clause",
        b"    f\"(~{SOLAR_RADIUS_AU:.5f} - {CHROMOSPHERE_RADII * SOLAR_RADIUS_AU:.5f} AU). \"\n"
        b"    f\"This is a stylization for visibility: the physical chromosphere \"\n"
        b"    f\"extends only ~{CHROMOSPHERE_PHYSICAL_KM:,.0f} km above the \"\n"
        b"    f\"photosphere (~{CHROMOSPHERE_PHYSICAL_RADII:.3f} solar radii).<br>\"\n",

        b"    f\"(~{SOLAR_RADIUS_AU:.5f} - {CHROMOSPHERE_RADII * SOLAR_RADIUS_AU:.5f} AU).<br>\"\n"
        b"    f\"  A stylization for visibility: the physical chromosphere extends only \"\n"
        b"    f\"~{CHROMOSPHERE_PHYSICAL_KM:,.0f} km<br>\"\n"
        b"    f\"  above the photosphere (~{CHROMOSPHERE_PHYSICAL_RADII:.3f} solar radii).<br>\"\n",
    ),
]


def main():
    here = pathlib.Path(__file__).parent
    path = here / TARGET
    if not path.exists():
        print(f"MISSING: {TARGET}\nRun from the palomas_orrery folder.")
        print("\nNOTHING WAS WRITTEN.")
        return 1

    data = path.read_bytes()
    fp = hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()
    if fp != CONTENT_FINGERPRINT:
        print(f"BASE MOVED: {TARGET}")
        print(f"    expected content MD5 {CONTENT_FINGERPRINT}")
        print(f"    actual   content MD5 {fp}")
        print("    (line endings normalized -- a real content difference.)")
        print("\nNOTHING WAS WRITTEN.")
        return 1

    is_crlf = data.count(b'\r\n') > 0
    if is_crlf:
        print(f"  ..  {TARGET}: CRLF file -- anchors translated, endings preserved")

    problems = []
    for label, old, new in EDITS:
        o, n = (old, new)
        if is_crlf:
            o = o.replace(b'\n', b'\r\n')
            n = n.replace(b'\n', b'\r\n')
        count = data.count(o)
        if count != 1:
            problems.append(f"ANCHOR {count} MATCHES (expected 1): {label}\n"
                            f"    first 70 bytes: {o[:70]!r}")
        else:
            data = data.replace(o, n, 1)

    if problems:
        print("\n".join(problems))
        print("\nNOTHING WAS WRITTEN.")
        return 1

    path.write_bytes(data)
    for label, _o, _n in EDITS:
        print(f"  ok  {TARGET} -- {label}")
    print("\npatch applied")
    print("\nNext: re-run the orrery and look at the two shells again, then")
    print("commit and push.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
