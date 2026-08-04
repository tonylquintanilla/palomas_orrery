# -*- coding: ascii -*-
"""patch_mercury_cross_check.py -- L-156 Phase 2 Batch 1 cross-check patch for mercury_visualization_shells.py

Built on ee29e6c691cad2995992396e692fae1d0d5cadc0
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

HOW TO RUN
    Save this file into the SAME FOLDER as mercury_visualization_shells.py, open it in
    VS Code, and click Run. No arguments, no flags, nothing to type.

    On success you get one "ok" line per edit, then:
        patch applied (N bytes)
    On failure you get a single ERROR: or ANCHOR FAIL: line and NOTHING
    is written -- the file on disk is untouched and it is always safe to
    re-check and run again.

Transactional: every anchor must match exactly once before any byte is
written. Binary mode throughout; LF endings and ASCII preserved.

8 edits, applied bottom-up by line number.
"""

import os
import sys

TARGET = 'mercury_visualization_shells.py'

# (edit_id, label, old_bytes, new_bytes) -- bottom-up by line number
EDITS = [
    ('MERC-1', 'Hill Source -> derived; drop Verified',
     b'# Source: NASA Solar System Dynamics\n# Verified: April 2026 via Gemini fact-check',
     b'# Source: Derived from NASA NSSDCA Mercury Fact Sheet inputs (Mercury GM,\n#         perihelion distance) via the standard Hill approximation,\n#         Claude Opus 5 2026-08-03. Perihelion convention.\n#         Mercury has no significant companion, so body mass is the correct\n#         input (no system-mass term).\n# Cross-checked: NSSDCA-derived Hill radius via Claude 2026-08-03 (worksheet_claude_batch1_tier2.md)\n# Cross-checked: NSSDCA-derived Hill radius via GPT 2026-08-03 (batch1_tier2_followup_gpt.md)'),
    ('MERC-6', 'Magnetosphere Source -- drop Verified, cite Winslow',
     b'# Source: NASA MESSENGER Mission\n# Verified: April 2026 via Gemini fact-check',
     b'# Source: NASA MESSENGER Mission; Winslow et al. 2013 -- magnetopause subsolar\n#         1.45 R_M and bow shock 1.96 R_M (the values used in the geometry below).\n# Cross-checked: Winslow et al. 2013 via Claude 2026-08-03 (worksheet_claude_batch1_tier2.md)\n# Cross-checked: Winslow et al. 2013 via GPT 2026-08-03 (batch1_tier2_cross_check_gpt.md)'),
    ('MERC-2c', 'Sodium tail GEOMETRY 10000 -> 1400 R_M',
     b'    # Sodium tail extends up to ~10,000 Mercury radii away from the Sun\n    max_tail_length = 10000 * MERCURY_RADIUS_AU',
     b'    # Sodium tail observed extent ~120 to ~1,400 Mercury radii; drawn at the upper end.\n    # Source: Baumgardner et al. 2008, GRL 35 (~1,400 R_M maximum observed extent)\n    max_tail_length = 1400 * MERCURY_RADIUS_AU'),
    ('MERC-2b', 'Sodium tail description text',
     b'            "Sodium Tail: Mercury has a remarkable sodium tail that extends incredibly far into space - up to 10,000 Mercury radii <br>"\n            "(approximately 24 million kilometers). This tail is created when sodium atoms from Mercury\'s exosphere <br>"',
     b'            "Sodium Tail: Mercury has a remarkable sodium tail. Observations place its extent in the range <br>"\n            "~120 to ~1,400 Mercury radii (approximately 0.3 to 3.4 million kilometers), varying strongly <br>"\n            "with orbital position and solar activity. This tail is created when sodium atoms from Mercury\'s exosphere <br>"'),
    ('MERC-2a', 'Sodium tail Source -> Baumgardner/Schmidt; info text',
     b'# Source: Potter & Morgan (1985); MESSENGER sodium tail observations\n# Verified: April 2026 via Gemini fact-check\nmercury_sodium_tail_info = (\n            "TO VISUALIZE CLOSE UP SET MANUAL SCALE TO AT LEAST 0.002 AU TO VISUALIZE.\\n"\n            "TO VISUALIZE THE COMPLETE TAIL INCLUDE VENUS IN THE PLOT OR SET MANUAL SCALE TO 1.0 AU\\n\\n" \n\n            "Sodium Tail: Mercury has a remarkable sodium tail that extends incredibly far into space - up to 10,000 Mercury radii \\n"\n            "(approximately 24 million kilometers). This tail is created when sodium atoms from Mercury\'s exosphere \\n"',
     b'# Source: Baumgardner et al. 2008, GRL 35 -- sodium tail observed to ~1,400 R_M;\n#         Schmidt et al. 2010, Icarus -- tail >1,000 R_M, highly variable.\n# Note: Potter & Morgan 1985 is the exosphere sodium DISCOVERY paper; it does not\n#       establish tail extent. The former "10,000 R_M" was unsupported by either\n#       source and has been replaced with the observed range.\n# Cross-checked: Baumgardner et al. 2008 via Claude 2026-08-03 (worksheet_claude_batch1_blind_lookup.md)\n# Cross-checked: Baumgardner et al. 2008 via GPT 2026-08-03 (batch1_blind_source_lookup_gpt.md)\nmercury_sodium_tail_info = (\n            "TO VISUALIZE CLOSE UP SET MANUAL SCALE TO AT LEAST 0.002 AU TO VISUALIZE.\\n"\n            "TO VISUALIZE THE COMPLETE TAIL INCLUDE VENUS IN THE PLOT OR SET MANUAL SCALE TO 1.0 AU\\n\\n" \n\n            "Sodium Tail: Mercury has a remarkable sodium tail. Observations place its extent in the range \\n"\n            "~120 to ~1,400 Mercury radii (approximately 0.3 to 3.4 million kilometers), varying strongly \\n"\n            "with orbital position and solar activity. This tail is created when sodium atoms from Mercury\'s exosphere \\n"'),
    ('MERC-5', 'Exosphere Source -- drop Verified, annotate',
     b'# Source: NASA MESSENGER; NASA Mercury Fact Sheet\n# Verified: April 2026 via Gemini fact-check',
     b'# Source: NASA MESSENGER; NASA Mercury Fact Sheet\n# Cross-checked: NASA Mercury Fact Sheet via Claude 2026-08-03 (worksheet_claude_batch1_tier2.md)\n# Cross-checked: NASA Mercury Fact Sheet via GPT 2026-08-03 (batch1_tier2_cross_check_gpt.md)'),
    ('MERC-4', 'Crust 35 -> 26 km (Sori 2018); drop diamond claim',
     b'# Source: NASA MESSENGER; Sori (2018) (crustal thickness ~35 km)\n#         Pei et al. (2024) (diamond layer from graphite + meteorite impacts)\n# Verified: April 2026 via Gemini fact-check\nmercury_crust_info = (\n            "SET MANUAL SCALE TO AT LEAST 0.002 AU TO VISUALIZE.\\n\\n"     \n            "Mercury has a solid silicate crust that is heavily cratered, resembling Earth\'s Moon. The crust is likely quite thin \\n" \n            "compared to Earth\'s. There\'s also a theory that a significant portion of Mercury\'s crust might be made of diamonds, \\n" \n            "formed by billions of years of meteorite impacts on a graphite-rich surface. About 35 km thick."',
     b'# Source: Sori 2018, EPSL 489:92 -- Mercury crustal thickness 26 +/- 11 km\n#         (MESSENGER gravity/topography, isostasy).\n# Removed: former "~35 km" (Sori 2018 gives 26, not 35) and the diamond-layer claim,\n#          which carried a mis-parsed author name, the wrong mechanism, and the wrong\n#          location. Removed rather than re-cited.\n# Cross-checked: Sori 2018 via Gemini 2026-08-03 (batch1_tier2_cross_check_gemini.md)\n# Cross-checked: Sori 2018 via GPT 2026-08-03 (batch1_tier2_cross_check_gpt.md)\nmercury_crust_info = (\n            "SET MANUAL SCALE TO AT LEAST 0.002 AU TO VISUALIZE.\\n\\n"     \n            "Mercury has a solid silicate crust that is heavily cratered, resembling Earth\'s Moon. The crust is likely quite thin \\n" \n            "compared to Earth\'s. About 26 km thick (Sori 2018)."'),
    ('MERC-3', 'Outer core 1074 -> Hauck 2013 core radius 2020 km',
     b'# Source: NASA MESSENGER Mission; Margot et al. (2012) (outer core 1074 km)\n# Verified: April 2026 via Gemini fact-check\nmercury_outer_core_info = (\n            "Outer Core: Surrounding the solid inner core is a liquid metallic outer core. The movement of this molten iron \\n" \n            "is thought to be the source of Mercury\'s weak magnetic field. About 1074 km thick."',
     b'# Source: Hauck et al. 2013, JGR Planets 118:1204 -- Mercury core radius\n#         2020 +/- 30 km (MESSENGER gravity and spin state). Used for visualization.\n# Cross-checked: Hauck et al. 2013 via GPT 2026-08-03 (batch1_blind_source_lookup_gpt.md)\n# Cross-checked: Hauck et al. 2013 via Gemini 2026-08-03 (batch1_tier2_cross_check_gemini.md)\nmercury_outer_core_info = (\n            "Outer Core: Surrounding the solid inner core is a liquid metallic outer core. The movement of this molten iron \\n" \n            "is thought to be the source of Mercury\'s weak magnetic field. Core radius approximately 2020 km."'),
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
