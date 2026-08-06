# -*- coding: ascii -*-
"""patch_shell_configs_mars_hill.py -- Mars Hill sphere 324.5 -> 319.2 R_Mars on the LIVE render path

Built on 339897000b63fa768ccb9b556dd432bac4f9d4eb
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

HOW TO RUN
    Save this file into the SAME FOLDER as shell_configs.py, open it in
    VS Code, and click Run. No arguments, nothing to type.

    Success prints one "ok" line per edit then "patch applied".
    Failure prints one ANCHOR FAIL:/ERROR: line and writes NOTHING --
    the file stays untouched, so re-running is always safe.

3 edits, applied bottom-up by line number.
"""

import os
import sys

TARGET = 'shell_configs.py'

EDITS = [
    ('SC-MARS-H3', 'Mars hill tooltip 324.5 -> 319.2',
     b'                "Mars\'s Hill Sphere (extends to ~324.5 Mars radii or about 1.1 million km), which defines the region of its \\n" ',
     b'                "Mars\'s Hill Sphere (extends to ~319.2 Mars radii or about 1.08 million km), which defines the region of its \\n" '),
    ('SC-MARS-H2', 'Mars hill hover 324.5 -> 319.2',
     b'                "Mars\'s Hill Sphere (extends to ~324.5 Mars radii or about 1.1 million km), which defines the region of its <br>" ',
     b'                "Mars\'s Hill Sphere (extends to ~319.2 Mars radii or about 1.08 million km), which defines the region of its <br>" '),
    ('SC-MARS-H1', 'Mars hill rf 324.5 -> 319.2 (the live render value)',
     b"        'hill_sphere': {\n            'name': 'Hill Sphere',\n            'radius_fraction': 324.5,\n            'color': 'rgb(0, 255, 0)',",
     b"        'hill_sphere': {\n            'name': 'Hill Sphere',\n            'radius_fraction': 319.2,  # 1,084,000 km / 3,396.2 km equatorial (Archinal 2018)\n            'color': 'rgb(0, 255, 0)',"),
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
