# -*- coding: ascii -*-
"""patch_mars_hill_correction.py -- Mars Hill sphere 324.5 -> 319.2 R_Mars (cross-check correction restored)

Built on 339897000b63fa768ccb9b556dd432bac4f9d4eb
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

HOW TO RUN
    Save this file into the SAME FOLDER as mars_visualization_shells.py, open it in
    VS Code, and click Run. No arguments, nothing to type.

    Success prints one "ok" line per edit then "patch applied".
    Failure prints one ANCHOR FAIL:/ERROR: line and writes NOTHING --
    the file stays untouched, so re-running is always safe.

4 edits, applied bottom-up by line number.
"""

import os
import sys

TARGET = 'mars_visualization_shells.py'

EDITS = [
    ('MARS-H4', 'dead legacy builder rf 324.5 -> 319.2',
     b"    radius_fraction = 324.5  # Mars's Hill sphere is about 324.5 Mars radii",
     b'    radius_fraction = 319.2  # 1,084,000 km / 3,396.2 km equatorial (Archinal 2018)'),
    ('MARS-H3', 'dead description text 324.5 -> 319.2',
     b'                "Mars\'s Hill Sphere (extends to ~324.5 Mars radii or about 1.1 million km), which defines the region of its <br>" ',
     b'                "Mars\'s Hill Sphere (extends to ~319.2 Mars radii or about 1.08 million km), which defines the region of its <br>" '),
    ('MARS-H2', 'dead legacy dict rf 324.5 -> 319.2',
     b"        'radius_fraction': 324.5,  ",
     b"        'radius_fraction': 319.2,  "),
    ('MARS-H1', 'info text + Source: 324.5 -> 319.2, record denominator',
     b'#         ~1.08 Mkm / ~320 R_Mars is the semi-major axis average.\n# Cross-checked: NASA NSSDCA Mars Fact Sheet via Claude 2026-08-01 (worksheet_claude_mars_visualization.md)\n# Cross-checked: JPL SSD astrodynamic parameters via GPT 2026-08-01 (track1_gpt_independent_worksheet_mars_visualization.md)\nmars_hill_sphere_info = (\n            "SET MANUAL SCALE TO AT LEAST 0.01 AU TO VISUALIZE.\\n\\n" \n            "Mars\'s Hill Sphere (extends to ~324.5 Mars radii or about 1.1 million km), which defines the region of its \\n" ',
     b'#         ~1.084 Mkm / ~319.2 R_Mars is the semi-major axis average, using the\n#         project equatorial radius 3,396.2 km (Archinal et al. 2018).\n# Corrected 2026-08-05: the former ~324.5 R_Mars matched no published source\n#         (1.5% high). The Aug-1 cross-check derived ~1.084 Mkm; that correction\n#         reached this module but never reached shell_configs.py, and was then\n#         reverted here by the Aug-4 consistency patch. Both copies now agree.\n#         Note 319.8 appears in the worksheet: same 1.084 Mkm over the volumetric\n#         mean radius 3,389.5 km. This project uses equatorial, so 319.2 is correct.\n# Cross-checked: NASA NSSDCA Mars Fact Sheet via Claude 2026-08-01 (worksheet_claude_mars_visualization.md)\n# Cross-checked: JPL SSD astrodynamic parameters via GPT 2026-08-01 (track1_gpt_independent_worksheet_mars_visualization.md)\nmars_hill_sphere_info = (\n            "SET MANUAL SCALE TO AT LEAST 0.01 AU TO VISUALIZE.\\n\\n" \n            "Mars\'s Hill Sphere (extends to ~319.2 Mars radii or about 1.08 million km), which defines the region of its \\n" '),
]


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, TARGET)
    if not os.path.exists(path):
        print("ERROR: %s not found next to this script." % TARGET)
        return 1
    with open(path, 'rb') as f:
        content = f.read()
    original_len = len(content)
    if b'\r\n' in content:
        print("ERROR: %s has CRLF line endings; expected LF only." % TARGET)
        return 1

    for edit_id, label, old, new in EDITS:
        n = content.count(old)
        if n != 1:
            print("ANCHOR FAIL: %s (%s) matched %d times, expected 1." % (edit_id, label, n))
            print("             Nothing written. The file is unchanged.")
            print("             Anchor began: %r" % old.split(b'\n')[0][:90])
            return 1

    for edit_id, label, old, new in EDITS:
        content = content.replace(old, new, 1)
        print("ok  %-14s %s" % (edit_id, label))

    try:
        content.decode('ascii')
    except UnicodeDecodeError as exc:
        print("ERROR: non-ASCII bytes in result (%s). Nothing written." % exc)
        return 1
    if b'\r\n' in content:
        print("ERROR: CRLF in result. Nothing written.")
        return 1

    with open(path, 'wb') as f:
        f.write(content)
    print("")
    print("patch applied (%d bytes, was %d)" % (len(content), original_len))
    return 0


if __name__ == '__main__':
    sys.exit(main())
