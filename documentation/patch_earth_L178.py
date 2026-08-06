# -*- coding: ascii -*-
"""patch_earth_L178.py -- L-178: remove EARTH_RADIUS_KM shadow constants, fix +0.112% conversion error

Built on 339897000b63fa768ccb9b556dd432bac4f9d4eb
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

HOW TO RUN
    Save this file into the SAME FOLDER as earth_visualization_shells.py, open it in
    VS Code, and click Run. No arguments, nothing to type.

    Success prints one "ok" line per edit then "patch applied".
    Failure prints one ANCHOR FAIL:/ERROR: line and writes NOTHING --
    the file stays untouched, so re-running is always safe.

5 edits, applied bottom-up by line number.
"""

import os
import sys

TARGET = 'earth_visualization_shells.py'

EDITS = [
    ('L178-5', 'GEO hover: add AU alongside km (standing convention)',
     b'        "Altitude: 35,786 km above surface<br>"\n        "Radius: 42,164 km from Earth\'s center (6.62 Earth radii)<br><br>"',
     b'        "Altitude: 35,786 km / 0.000239 AU above surface<br>"\n        "Radius: 42,164 km / 0.000282 AU from Earth\'s center (6.62 Earth radii)<br><br>"'),
    ('L178-4', 'GEO radial-scatter comment: describe what the code does',
     b'    # Radial scatter: +/- 0.0002 AU (~30 km at GEO -- realistic station-keeping band)',
     b'    # Radial scatter: +/- 0.0002 EARTH RADII (~1.3 km), not AU. Real GEO\n    # station-keeping bands run to tens of km; widening this is a Mode 5\n    # call, so the value is unchanged and only the comment is corrected.'),
    ('L178-3', 'GEO: drop shadow constant, convert via KM_PER_AU',
     b'    EARTH_RADIUS_KM = 6371.0\n    geo_radius_au = (GEO_RADIUS_KM / EARTH_RADIUS_KM) * EARTH_RADIUS_AU',
     b'    # L-178: converted directly via KM_PER_AU. The former local\n    # EARTH_RADIUS_KM = 6371.0 (volumetric mean) was a shadow constant, and\n    # dividing into the equatorial-based EARTH_RADIUS_AU drew the belt\n    # ~47 km too high (+0.112%).\n    geo_radius_au = GEO_RADIUS_KM / KM_PER_AU'),
    ('L178-2', 'LEO: drop shadow constant, convert via KM_PER_AU',
     b'    EARTH_RADIUS_KM = 6371.0\n    AU_PER_KM = EARTH_RADIUS_AU / EARTH_RADIUS_KM',
     b'    # L-178: converted directly via KM_PER_AU. The former local\n    # EARTH_RADIUS_KM = 6371.0 (volumetric mean) was a shadow constant, and\n    # dividing it into the equatorial-based EARTH_RADIUS_AU (6,378.137 km)\n    # introduced a +0.112% error in every altitude band below.\n    AU_PER_KM = 1.0 / KM_PER_AU'),
    ('L178-1', 'import KM_PER_AU from constants_new',
     b'from planet_visualization_utilities import (EARTH_RADIUS_AU, create_sphere_points, create_magnetosphere_shape, create_bow_shock_shape)',
     b'from planet_visualization_utilities import (EARTH_RADIUS_AU, create_sphere_points, create_magnetosphere_shape, create_bow_shock_shape)\nfrom constants_new import KM_PER_AU  # L-178: direct km<->AU conversion, no shadow constant'),
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
