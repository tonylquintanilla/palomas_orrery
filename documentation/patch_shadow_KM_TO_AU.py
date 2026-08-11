"""
patch_shadow_KM_TO_AU.py

Removes the one shadow constant reported by provenance_scanner.py:
orbit_data_manager.py line 1850 defines a local

    KM_TO_AU = 1.0 / 149597870.7

which duplicates KM_PER_AU in constants_new.py (IAU 2012 Resolution B2,
exact). Per provenance-discipline, No Shadow Constants [CRITICAL]: delete
the local definition and import the real one -- do NOT add a "# Source:"
comment to the local copy.

TWO EDITS
  1. Add "from constants_new import KM_PER_AU" to the module import block.
  2. Line 1850: KM_TO_AU = 1.0 / 149597870.7  ->  KM_TO_AU = 1.0 / KM_PER_AU

The three use sites (lines 1861, 1862, 1873) are unchanged -- KM_TO_AU
keeps its name and its value. No import cycle: constants_new imports only
numpy and datetime.

HOW TO RUN
    Save this file into the SAME folder as orbit_data_manager.py
    (the palomas_orrery repo root), open it in VS Code, click Run.
    Equivalent command line: python patch_shadow_KM_TO_AU.py

WHAT SUCCESS LOOKS LIKE
    Two "ok" lines, then "patch applied". Nothing is written unless both
    anchors match exactly once.

WHAT FAILURE LOOKS LIKE
    One "ERROR:" line (base file is not what this was built against) or
    "ANCHOR FAIL" (an edit's text was not found). Nothing is written
    either way.

Built on 308053ceb2466e3d14d6df9208d3f69024ab488e at
https://github.com/tonylquintanilla/palomas_orrery

Patch written August 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

TARGET = "orbit_data_manager.py"
BASE_MD5 = "904659fdf05c287cbbf3881d28d9bf08"   # content, line endings normalized

EDITS = [
    # 1. import block -- appended after the existing third-party imports
    (b"from astroquery.jplhorizons import Horizons\n"
     b"from astropy.time import Time\n"
     b"import plotly.graph_objs as go\n",

     b"from astroquery.jplhorizons import Horizons\n"
     b"from astropy.time import Time\n"
     b"import plotly.graph_objs as go\n"
     b"\n"
     b"from constants_new import KM_PER_AU\n"),

    # 2. the shadow constant itself
    (b"        KM_TO_AU = 1.0 / 149597870.7\n",
     b"        KM_TO_AU = 1.0 / KM_PER_AU\n"),
]


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, TARGET)

    if not os.path.exists(path):
        print("ERROR: not found: %s" % TARGET)
        print("       Put this script in the same folder as %s." % TARGET)
        return 1

    with open(path, "rb") as f:
        data = f.read()

    fp = hashlib.md5(data.replace(b"\r\n", b"\n")).hexdigest()
    if fp != BASE_MD5:
        print("ERROR: base moved: %s" % TARGET)
        print("       expected %s" % BASE_MD5)
        print("       found    %s" % fp)
        print("       Nothing written.")
        return 1

    # Anchors are authored LF; translate to the file's own convention.
    is_crlf = data.count(b"\r\n") > 0

    for old, new in EDITS:
        o = old.replace(b"\n", b"\r\n") if is_crlf else old
        n = new.replace(b"\n", b"\r\n") if is_crlf else new
        count = data.count(o)
        if count != 1:
            print("ANCHOR FAIL: expected 1 match, got %d" % count)
            print("       %s" % o.split(b"\n")[0][:70].decode("ascii", "replace"))
            print("       Nothing written.")
            return 1
        data = data.replace(o, n)
        print("ok   %s" % o.split(b"\n")[0].strip()[:66].decode("ascii", "replace"))

    with open(path, "wb") as f:
        f.write(data)
    print("patch applied: %s (%d bytes)" % (TARGET, len(data)))
    print("")
    print("Re-run provenance_scanner.py: shadow constant count should go 1 -> 0.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
