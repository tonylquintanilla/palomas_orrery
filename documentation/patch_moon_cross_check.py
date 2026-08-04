# -*- coding: ascii -*-
"""patch_moon_cross_check.py -- L-156 Phase 2 Batch 1 cross-check patch for moon_visualization_shells.py

Built on ee29e6c691cad2995992396e692fae1d0d5cadc0
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

HOW TO RUN
    Save this file into the SAME FOLDER as moon_visualization_shells.py, open it in
    VS Code, and click Run. No arguments, no flags, nothing to type.

    On success you get one "ok" line per edit, then:
        patch applied (N bytes)
    On failure you get a single ERROR: or ANCHOR FAIL: line and NOTHING
    is written -- the file on disk is untouched and it is always safe to
    re-check and run again.

Transactional: every anchor must match exactly once before any byte is
written. Binary mode throughout; LF endings and ASCII preserved.

7 edits, applied bottom-up by line number.
"""

import os
import sys

TARGET = 'moon_visualization_shells.py'

# (edit_id, label, old_bytes, new_bytes) -- bottom-up by line number
EDITS = [
    ('MOON-1', 'Hill sphere Source -> derived format',
     b'# Source: NASA Solar System Dynamics (SSD); Hill sphere radius ~60,000 km confirmed,\n#         34.53 lunar radii derived from Moon mean radius 1,737.4 km.',
     b'# Source: Derived from NASA NSSDCA Moon Fact Sheet inputs (Moon mass, Earth mass,\n#         Earth-Moon distance) via the standard Hill approximation,\n#         Claude Opus 5 2026-08-03.\n#         ~60,000 km is a conventional rounded value, not a measured constant.\n#         The Hill radius varies over the orbit from ~58,147 km (perigee) to\n#         ~64,901 km (apogee). The shell uses 34.53 lunar radii = ~59,992 km\n#         (Moon mean radius 1,737.4 km), which lies inside that range.\n# Cross-checked: derived Hill radius via Claude 2026-08-03 (worksheet_claude_batch1_tier2.md)\n# Note: SINGLE-LEG. Only the Claude tier-2 worksheet carries the 58,147-64,901 km\n#       range. GPT and Gemini converged on method and inputs but did not publish\n#       this range. A second independent leg is still owed for V2 scoring.'),
    ('MOON-2', 'Moonquake Source -> Nakamura 1982/2005',
     b'# Source: NASA Moon Fact Sheet; Apollo Seismic Experiment reports (deep moonquakes 700-1,200 km,\n#         tidal stress origin confirmed).',
     b'# Source: Nakamura et al. 1982, JGR 87:A117 -- deep moonquake source depths;\n#         Nakamura 2005, JGR 110 -- deep moonquake catalog reanalysis.\n#         Deep moonquakes 700-1,200 km depth, concentrated at 800-1,000 km;\n#         tidal stress origin.\n# Cross-checked: Nakamura et al. 1982 via Claude 2026-08-03 (worksheet_claude_batch1_followup.md)\n# Cross-checked: Nakamura 1982/2005 via GPT 2026-08-03 (batch1_tier2_followup_gpt.md)'),
    ('MOON-3a', 'Outer core display -- drop 1300-1600 K',
     b'            "* Estimated Temperature: This layer would be slightly cooler than the inner core, but still hot enough to be molten at <br>" \n            "  the lower pressures found here. Estimates typically fall around 1300 K to 1600 K. Let\'s use 1500 K as a representative <br>" \n            "  value for the outer core for your model.<br>" ',
     b'            "* Estimated Temperature: This layer is hot enough to be molten at the lower pressures found here, but the <br>" \n            "  temperature is model-dependent and not well constrained.<br>" '),
    ('MOON-3b', 'Outer core Source -- note removal',
     b'        # Source: NASA Moon Fact Sheet; Weber et al. (2011), Science, "Seismic Detection of the Lunar Core";\n        #         outer core ~330 km radius, partially molten silicate boundary layer ~150 km thick confirmed.',
     b'        # Source: NASA Moon Fact Sheet; Weber et al. (2011), Science, "Seismic Detection of the Lunar Core";\n        #         outer core ~330 km radius, partially molten silicate boundary layer ~150 km thick.\n        # Removed: former "1300 K to 1600 K" outer-core temperature from the display text.\n        #          Weber 2011 is a seismic study, not a thermal one; the temperature is\n        #          model-dependent and was not sourceable after three independent searches.\n        # Cross-checked: Weber et al. 2011 via GPT 2026-08-03 (batch1_tier2_cross_check_gpt.md)\n        # Cross-checked: Weber et al. 2011 via Gemini 2026-08-03 (batch1_tier2_cross_check_gemini.md)'),
    ('MOON-4a', 'Inner core display -- drop 1600-1700 K',
     b'            "* Inner Core: Believed to be a solid, iron-rich core, roughly 240 kilometers in radius:<br>" \n            "  * Estimates for the temperature of the Moon\\\'s inner core vary slightly depending on the studies and methods used, but <br>" \n            "    some more recent reanalyses of seismic data suggest temperatures around 1600-1700 K." ',
     b'            "* Inner Core: Believed to be a solid, iron-rich core, roughly 240 kilometers in radius:<br>" \n            "  * The temperature of the inner core is model-dependent and not well constrained; <br>" \n            "    seismic data constrain its size, not its temperature." '),
    ('MOON-4b', 'Inner core inner Source -- note removal',
     b'        # Source: Weber et al. (2011), Science, "Seismic Detection of the Lunar Core";\n        #         solid iron-rich inner core ~240 km radius, 1,600-1,700 K confirmed.',
     b'        # Source: Weber et al. (2011), Science, "Seismic Detection of the Lunar Core";\n        #         solid iron-rich inner core ~240 km radius (seismic constraint).\n        # Removed: former "1,600-1,700 K" -- see module-level note above.\n        # Cross-checked: Weber et al. 2011 via GPT 2026-08-03 (batch1_tier2_cross_check_gpt.md)\n        # Cross-checked: Weber et al. 2011 via Gemini 2026-08-03 (batch1_tier2_cross_check_gemini.md)'),
    ('MOON-4c', 'Inner core module Source -- note removal',
     b'# Source: Weber et al. (2011), Science, "Seismic Detection of the Lunar Core";\n#         inner core ~240 km radius, 1,600-1,700 K, refined from Apollo seismic data.',
     b'# Source: Weber et al. (2011), Science, "Seismic Detection of the Lunar Core";\n#         solid inner core ~240 km radius, from Apollo seismic array reanalysis.\n# Removed: former "1,600-1,700 K" inner-core temperature. Weber 2011 is a seismic\n#          detection study and reports no inner-core temperature; the value was not\n#          sourceable after three independent searches, so it is removed and the gap\n#          noted rather than re-cited.\n# Cross-checked: Weber et al. 2011 via GPT 2026-08-03 (batch1_tier2_cross_check_gpt.md)\n# Cross-checked: Weber et al. 2011 via Gemini 2026-08-03 (batch1_tier2_cross_check_gemini.md)'),
]


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, TARGET)

    if not os.path.exists(path):
        print("ERROR: %s not found next to this script." % TARGET)
        print("       Put this script in the same folder as %s." % TARGET)
        return 1

    with open(path, 'rb') as f:
        content = f.read()
    original_len = len(content)

    if b'\r\n' in content:
        print("ERROR: %s contains CRLF line endings; expected LF only." % TARGET)
        return 1

    # Pass 1 -- verify every anchor before writing anything.
    for edit_id, label, old, new in EDITS:
        n = content.count(old)
        if n != 1:
            print("ANCHOR FAIL: %s (%s) matched %d times, expected 1." % (edit_id, label, n))
            print("             Nothing was written. The file is unchanged.")
            print("             First line of the anchor it looked for:")
            print("             %r" % old.split(b'\n')[0][:100])
            return 1

    # Pass 2 -- apply.
    for edit_id, label, old, new in EDITS:
        content = content.replace(old, new, 1)
        print("ok  %-12s %s" % (edit_id, label))

    # Post-checks on the result, still before writing.
    try:
        content.decode('ascii')
    except UnicodeDecodeError as exc:
        print("ERROR: patched result contains non-ASCII bytes (%s). Nothing written." % exc)
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
