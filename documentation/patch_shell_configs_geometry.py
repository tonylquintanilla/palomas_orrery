# -*- coding: ascii -*-
"""patch_shell_configs_geometry.py -- L-156 geometry corrections + <br> fix for shell_configs.py

Built on 06a16df768a010205b7078630ac31bf0cd17f846
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

HOW TO RUN
    Save this file into the SAME FOLDER as shell_configs.py, open it in
    VS Code, and click Run. No arguments, no flags, nothing to type.

    Success prints one "ok" line per edit then "patch applied".
    Failure prints one ANCHOR FAIL:/ERROR: line and writes NOTHING --
    the file on disk stays untouched, so it is always safe to re-run.

Transactional: every anchor must match exactly once before any byte is
written. Binary mode throughout; LF endings and ASCII preserved.

14 edits, applied bottom-up by line number.
"""

import os
import sys

TARGET = 'shell_configs.py'

# (edit_id, label, old_bytes, new_bytes) -- bottom-up by line number
EDITS = [
    ('SC-MARS-3', 'Mars dead custom tooltip bow shock 1.5 -> 1.64',
     b'                "2. Bow Shock: Forms where the solar wind first encounters Mars\' atmosphere/ionosphere (~1.5 Mars radii).\\n"',
     b'                "2. Bow Shock: Forms where the solar wind first encounters Mars\' atmosphere/ionosphere (~1.64 Mars radii).\\n"'),
    ('SC-MARS-2', 'Mars header bow shock 1.5 -> 1.64 (Vignes 2000)',
     b'    #         induced magnetosphere, bow shock 1.5 Rm, crustal magnetic fields',
     b'    #         induced magnetosphere, bow shock ~1.64 Rm (Vignes et al. 2000),'),
    ('SC-VEN-CRUST', 'Venus crust rf stays 1.0 -- flag stylization gap',
     b"        'crust': {\n            'name': 'Crust',\n            'radius_fraction': 1.0,\n            'color': 'rgb(255, 255, 224)',",
     b"        'crust': {\n            'name': 'Crust',\n            'radius_fraction': 1.0,\n            # STYLIZATION GAP (not resolved -- Mode 5 decision): the mantle below\n            # sits at rf 0.98, so the drawn crust is ~121 km thick while the text\n            # says 10-30 km. Closing the gap numerically would make the crust shell\n            # essentially invisible. Left stylized deliberately; see as-built.\n            'color': 'rgb(255, 255, 224)',"),
    ('SC-VEN-CORE', 'Venus core rf 0.5 -> 0.5288 (3,200 km)',
     b"        'core': {\n            'name': 'Core',\n            'radius_fraction': 0.5,\n            'color': 'rgb(255, 180, 140)',",
     b"        'core': {\n            'name': 'Core',\n            'radius_fraction': 0.5288,  # 3,200 km / 6,051.8 km (NASA Venus Fact Sheet)\n            'color': 'rgb(255, 180, 140)',"),
    ('SC-ERIS-MANTLE', 'Eris mantle rf 0.66 -> 0.686 (100 km ice shell)',
     b"            'radius_fraction': 0.66,",
     b"            'radius_fraction': 0.686,  # core 697.8 km + 100 km ice shell / 1,163 km"),
    ('SC-MOON-ART', "Moon outer_core live hover: stray '<br>:' -> '<br>'",
     b'                "330 kilometers. There might also be a small, partially molten layer of silicates around the outer core.<br>:"',
     b'                "330 kilometers. There might also be a small, partially molten layer of silicates around the outer core.<br>"'),
    ('SC-MOON-OC', 'Moon outer_core rf 0.2083 -> 0.1899 (330 km)',
     b"            'radius_fraction': 0.2083,",
     b"            'radius_fraction': 0.1899,  # 330 km / 1,737.4 km (Weber 2011 / Nakamura)"),
    ('SC-MOON-IC', 'Moon inner_core rf 0.1485 -> 0.1381 (240 km)',
     b"            'radius_fraction': 0.1485,",
     b"            'radius_fraction': 0.1381,  # 240 km / 1,737.4 km (Weber et al. 2011)"),
    ('SC-MOON-HDR', 'Moon body header -> Weber/Nakamura; drop Verified stamp',
     b'    # Source: Weber et al. (2011), Science, "Seismic Detection of the Lunar Core";\n    #         NASA Moon Fact Sheet; Apollo Seismic Experiment reports;\n    #         NASA Solar System Dynamics (Hill sphere radius); Draper (1847).\n    # Verified: April 2026 provenance audit; all 5 flagged claims confirmed.',
     b'    # Source: Weber et al. (2011), Science, "Seismic Detection of the Lunar Core"\n    #         -- inner core 240 km, outer core 330 km;\n    #         Nakamura et al. 1982, JGR 87:A117 and Nakamura 2005, JGR 110\n    #         -- deep moonquake source depths;\n    #         NASA Moon Fact Sheet; NASA Solar System Dynamics (Hill sphere); Draper (1847).\n    # Cross-checked: Weber 2011 / Nakamura via GPT 2026-08-03 (batch1_tier2_cross_check_gpt.md)\n    # Cross-checked: Weber 2011 / Nakamura via Gemini 2026-08-03 (batch1_tier2_cross_check_gemini.md)'),
    ('SC-MERC-CRUST', 'Mercury crust rf stays 1.0 -- flag layer-chain gap',
     b"        'crust': {\n            'name': 'Crust',\n            'radius_fraction': 1.0,\n            'color': 'rgb(128, 128, 128)',",
     b"        'crust': {\n            'name': 'Crust',\n            'radius_fraction': 1.0,\n            # LAYER CHAIN GAP (not resolved -- Mode 5 decision): 2,020 (core)\n            # + 331 (mantle) + 26 (crust) = 2,377 km against R = 2,439.7 km, a\n            # 62.7 km shortfall representing unmodelled structure. Crust stays at\n            # the surface (rf 1.0), so its drawn thickness is ~88.8 km, not 26 km.\n            # Note this GREW from ~48.8 km when the mantle moved to 0.9636.\n            'color': 'rgb(128, 128, 128)',"),
    ('SC-MERC-DIA-T', 'Mercury mantle tooltip -- drop diamond claim',
     b'                "Mantle: Surrounding the core is a rocky mantle. Recent research suggests this mantle might even contain a layer of \\n"\n                "diamonds, formed from ancient carbon-rich material under immense pressure. The mantle is significantly thinner than \\n"\n                "Earth\'s, estimated to be only about 331 kilometers thick."',
     b'                "diamonds, formed from ancient carbon-rich material under immense pressure. The mantle is significantly thinner than \\n"\n                "Earth\'s, estimated to be only about 331 kilometers thick."'),
    ('SC-MERC-MANTLE', 'Mercury mantle rf 0.98 -> 0.9636 + drop diamond claim (hover)',
     b'        \'mantle\': {\n            \'name\': \'Mantle\',\n            \'radius_fraction\': 0.98,\n            \'color\': \'rgb(230, 100, 20)\',\n            \'opacity\': 0.7,\n            \'n_points\': 25,\n            \'marker_size\': 3.4,\n            \'info_border\': \'white\',  # two-standards (May 29, 2026): burnt orange fill\n            \'hover_text\': (\n                "Mantle: Surrounding the core is a rocky mantle. Recent research suggests this mantle might even contain a layer of <br>"\n                "diamonds, formed from ancient carbon-rich material under immense pressure. The mantle is significantly thinner than <br>"\n                "Earth\'s, estimated to be only about 331 kilometers thick."',
     b'        \'mantle\': {\n            \'name\': \'Mantle\',\n            \'radius_fraction\': 0.9636,  # (2,020 + 331) km / 2,439.7 km\n            \'color\': \'rgb(230, 100, 20)\',\n            \'opacity\': 0.7,\n            \'n_points\': 25,\n            \'marker_size\': 3.4,\n            \'info_border\': \'white\',  # two-standards (May 29, 2026): burnt orange fill\n            \'hover_text\': (\n                "Mantle: Surrounding the core is a rocky mantle. The mantle is significantly thinner than <br>"\n                "Earth\'s, estimated to be only about 331 kilometers thick."'),
    ('SC-MERC-OC', 'Mercury outer_core rf 0.85 -> 0.828 (2,020 km)',
     b"        'outer_core': {\n            'name': 'Outer Core',\n            'radius_fraction': 0.85,\n            'color': 'rgb(255, 140, 0)',",
     b"        'outer_core': {\n            'name': 'Outer Core',\n            'radius_fraction': 0.828,  # 2,020 km / 2,439.7 km (Hauck et al. 2013)\n            'color': 'rgb(255, 140, 0)',"),
    ('SC-MERC-HDR', 'Mercury body header Margot -> Hauck; drop Verified stamp',
     b'    # Source: NASA MESSENGER Mission, Margot et al. (2012), Sori (2018)\n    # Verified: April 2026 via Gemini fact-check',
     b'    # Source: Hauck et al. 2013, JGR Planets 118:1204 -- core radius 2,020 +/- 30 km;\n    #         Sori 2018, EPSL 489:92 -- crustal thickness 26 +/- 11 km;\n    #         NASA MESSENGER Mission; Winslow et al. 2013 (magnetosphere geometry).\n    # Cross-checked: Hauck 2013 / Sori 2018 via GPT 2026-08-03 (batch1_tier2_cross_check_gpt.md)\n    # Cross-checked: Hauck 2013 / Sori 2018 via Gemini 2026-08-03 (batch1_tier2_cross_check_gemini.md)'),
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
