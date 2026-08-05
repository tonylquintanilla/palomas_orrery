# -*- coding: ascii -*-
"""patch_mercury_geometry_text.py -- L-156 geometry corrections + <br> fix for mercury_visualization_shells.py

Built on 06a16df768a010205b7078630ac31bf0cd17f846
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

HOW TO RUN
    Save this file into the SAME FOLDER as mercury_visualization_shells.py, open it in
    VS Code, and click Run. No arguments, no flags, nothing to type.

    Success prints one "ok" line per edit then "patch applied".
    Failure prints one ANCHOR FAIL:/ERROR: line and writes NOTHING --
    the file on disk stays untouched, so it is always safe to re-run.

Transactional: every anchor must match exactly once before any byte is
written. Binary mode throughout; LF endings and ASCII preserved.

4 edits, applied bottom-up by line number.
"""

import os
import sys

TARGET = 'mercury_visualization_shells.py'

# (edit_id, label, old_bytes, new_bytes) -- bottom-up by line number
EDITS = [
    ('MERC-SCALE', 'Hill sphere scale note 0.003 -> 0.005 AU (matches config)',
     b'            "SET MANUAL SCALE TO AT LEAST 0.003 AU TO VISUALIZE.\\n\\n" ',
     b'            "SET MANUAL SCALE TO AT LEAST 0.005 AU TO VISUALIZE.\\n\\n" '),
    ('MERC-ATM-SCALE', 'Exosphere: drop SET MANUAL SCALE line (config lacks it)',
     b'mercury_atmosphere_info = (\n            "SET MANUAL SCALE TO AT LEAST 0.002 AU TO VISUALIZE.\\n\\n"     ',
     b'mercury_atmosphere_info = ('),
    ('MERC-CRUST-SCALE', 'Crust: drop SET MANUAL SCALE line (config lacks it)',
     b'mercury_crust_info = (\n            "SET MANUAL SCALE TO AT LEAST 0.002 AU TO VISUALIZE.\\n\\n"     ',
     b'mercury_crust_info = ('),
    ('MERC-DIAMOND', 'Mantle: drop diamond claim; add Removed note',
     b'mercury_mantle_info = (\n            "Mantle: Surrounding the core is a rocky mantle. Recent research suggests this mantle might even contain a layer of \\n" \n            "diamonds, formed from ancient carbon-rich material under immense pressure. The mantle is significantly thinner than \\n" \n            "Earth\'s, estimated to be only about 331 kilometers thick."',
     b'# Removed: the mantle diamond-layer claim ("might even contain a layer of\n#          diamonds, formed from ancient carbon-rich material under immense\n#          pressure"). Same unsourced assertion Batch 1 removed from the crust\n#          (see the Removed note below): mis-parsed author name, wrong mechanism,\n#          wrong location. Removed rather than re-cited.\nmercury_mantle_info = (\n            "Mantle: Surrounding the core is a rocky mantle. The mantle is significantly thinner than \\n" \n            "Earth\'s, estimated to be only about 331 kilometers thick."'),
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
        print("ERROR: %s contains CRLF line endings; expected LF only." % TARGET)
        return 1

    for edit_id, label, old, new in EDITS:
        n = content.count(old)
        if n != 1:
            print("ANCHOR FAIL: %s (%s) matched %d times, expected 1." % (edit_id, label, n))
            print("             Nothing was written. The file is unchanged.")
            print("             Anchor began: %r" % old.split(b'\n')[0][:90])
            return 1

    for edit_id, label, old, new in EDITS:
        content = content.replace(old, new, 1)
        print("ok  %-22s %s" % (edit_id, label))

    try:
        content.decode('ascii')
    except UnicodeDecodeError as exc:
        print("ERROR: patched result has non-ASCII bytes (%s). Nothing written." % exc)
        return 1
    if b'\r\n' in content:
        print("ERROR: patched result contains CRLF. Nothing written.")
        return 1

    with open(path, 'wb') as f:
        f.write(content)

    print("")
    print("patch applied (%d bytes, was %d)" % (len(content), original_len))
    return 0


if __name__ == '__main__':
    sys.exit(main())
