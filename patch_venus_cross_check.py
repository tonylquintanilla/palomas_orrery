# -*- coding: ascii -*-
"""patch_venus_cross_check.py -- L-156 Phase 2 Batch 1 cross-check patch for venus_visualization_shells.py

Built on ee29e6c691cad2995992396e692fae1d0d5cadc0
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

HOW TO RUN
    Save this file into the SAME FOLDER as venus_visualization_shells.py, open it in
    VS Code, and click Run. No arguments, no flags, nothing to type.

    On success you get one "ok" line per edit, then:
        patch applied (N bytes)
    On failure you get a single ERROR: or ANCHOR FAIL: line and NOTHING
    is written -- the file on disk is untouched and it is always safe to
    re-check and run again.

Transactional: every anchor must match exactly once before any byte is
written. Binary mode throughout; LF endings and ASCII preserved.

10 edits, applied bottom-up by line number.
"""

import os
import sys

TARGET = 'venus_visualization_shells.py'

# (edit_id, label, old_bytes, new_bytes) -- bottom-up by line number
EDITS = [
    ('VEN-1', 'Hill Source -> derived format',
     b'# Source: NASA Solar System Dynamics (SSD); NASA Venus Fact Sheet;\n#         Hill sphere ~1.01 million km / ~167 Venus radii; no natural moons confirmed.',
     b'# Source: Derived from NASA NSSDCA Venus Fact Sheet inputs (Venus GM, perihelion\n#         distance 107.48 Mkm) via the standard Hill approximation,\n#         Claude Opus 5 2026-08-03.\n#         Perihelion gives ~1.004 Mkm = 166 Venus radii (the shell uses this);\n#         semi-major axis gives ~1.011 Mkm = 167.1 Venus radii.\n#         Venus has no natural moons, so body mass is the correct input.\n# Cross-checked: derived Hill radius via GPT 2026-08-03 (batch1_tier2_followup_gpt.md: 167.08 R_V at a)\n# Cross-checked: derived Hill radius via Claude 2026-08-03 (worksheet_claude_batch1_tier2.md)'),
    ('VEN-2', 'Magnetotail Source -> Edberg 2024',
     b'    # Source: ESA Venus Express: Magnetosphere; NASA Pioneer Venus Results;\n    #         induced magnetosphere, bow shock 1.3-1.7 Rv, comet-shaped tail confirmed.',
     b'    # Source: Edberg et al. 2024, JGR Space Physics 129, e2024JA032603 -- magnetotail\n    #         extends to ~45-60 R_V under active conditions;\n    #         Shan et al. 2015 -- induced bow shock 1.3-1.7 R_V.\n    # Cross-checked: Edberg et al. 2024 via GPT 2026-08-03 (batch1_tier2_cross_check_gpt.md)\n    # Cross-checked: Edberg et al. 2024 via Gemini 2026-08-03 (worksheet_gemini_batch1_followup.md)'),
    ('VEN-6', 'Magnetosphere Source -- annotate Zhang/Shan',
     b'# Source: ESA Venus Express: Magnetosphere; NASA Pioneer Venus Results;\n#         induced magnetosphere (not intrinsic), formed by solar wind / ionosphere interaction confirmed.',
     b'# Source: ESA Venus Express: Magnetosphere; NASA Pioneer Venus Results;\n#         Zhang et al. 2007 -- induced magnetopause ~1.05 R_V;\n#         Shan et al. 2015 -- induced bow shock 1.4 R_V (range 1.36-1.46).\n# Cross-checked: Zhang 2007 / Shan 2015 via Claude 2026-08-03 (worksheet_claude_batch1_tier2.md)\n# Cross-checked: Zhang 2007 / Shan 2015 via GPT 2026-08-03 (batch1_tier2_cross_check_gpt.md)'),
    ('VEN-3c', 'Upper atmosphere -- soften ionosphere peak',
     b'            "  radiation has ionized the atmospheric gases, creating a layer of charged particles (ions and electrons). Venus has a substantial ionosphere, with peak electron <br>" \n            "  densities occurring around 120-140 km altitude. The ionosphere plays a crucial role in interacting with the solar wind, as Venus lacks a strong global magnetic <br>" ',
     b'            "  radiation has ionized the atmospheric gases, creating a layer of charged particles (ions and electrons). Venus has a substantial ionosphere, with peak electron <br>" \n            "  densities occurring in the upper atmosphere. The ionosphere plays a crucial role in interacting with the solar wind, as Venus lacks a strong global magnetic <br>" '),
    ('VEN-3b', 'Upper atmosphere -- soften thermosphere 300 K',
     b'            "  extreme ultraviolet (EUV) radiation. This is the thermosphere. Unlike Earth\'s thermosphere, Venus\'s thermosphere is surprisingly cold, with average temperatures <br>" \n            "  around 300 K (27 degC), and even colder on the night side (the \\"cryosphere\\" around 90-120 km can reach extremely low temperatures). This is due to efficient <br>" ',
     b'            "  extreme ultraviolet (EUV) radiation. This is the thermosphere. Unlike Earth\'s thermosphere, Venus\'s thermosphere is surprisingly cold. Temperatures <br>" \n            "  vary significantly with altitude, local time, and solar conditions, and the night side (the \\"cryosphere\\") is colder still. This is due to efficient <br>" '),
    ('VEN-3a', 'Upper atmosphere Source -> Bertaux 2007 (mesosphere only)',
     b'        # Source: ESA Venus Express Mission; NASA Pioneer Venus Project;\n        #         thermosphere ~300 K dayside, night-side cryosphere 90-120 km, ionosphere 120-140 km peak confirmed.',
     b'        # Source: Bertaux et al. 2007, Nature 450:646 -- Venus mesosphere 60-100 km\n        #         (SPICAV/Venus Express stellar occultation). Mesosphere extent only.\n        # Removed: thermosphere temperature and ionosphere peak altitude as specific\n        #          values. Both are model- and time-dependent; softened in the display\n        #          text rather than cited. VIRA-sourced values may restore them later.\n        # Cross-checked: Bertaux et al. 2007 via Claude 2026-08-03 (worksheet_claude_batch1_blind_lookup.md)\n        # Cross-checked: Bertaux et al. 2007 via GPT 2026-08-03 (batch1_blind_source_lookup_gpt.md)'),
    ('VEN-4b', 'Atmosphere description -- 92-93x, troposphere 60-65 km',
     b'        \'description\': (\n            "Venus boasts an extremely dense atmosphere, about 90 times the pressure of Earth\'s atmosphere at the surface. It is <br>" \n            "composed primarily of carbon dioxide (about 96.5%) and nitrogen (about 3.5%), with trace amounts of other gases, <br>" \n            "including sulfuric acid clouds that completely enshroud the planet. This thick, CO2-rich atmosphere creates a runaway <br>" \n            "greenhouse effect, making Venus the hottest planet in our solar system with surface temperatures around 464 degC. The <br>" \n            "upper atmosphere exhibits a phenomenon called \\"super-rotation,\\" where winds blow much faster than the planet\'s slow <br>" \n            "rotation.<br><br>"\n            "The \\"lower atmosphere\\" of Venus is generally considered to be the troposphere, which extends from the surface up to \\n" \n            "an altitude of approximately 60 kilometers. This region contains the dense, hot air and the main cloud layers."',
     b'        \'description\': (\n            "Venus boasts an extremely dense atmosphere, about 92 to 93 times the pressure of Earth\'s atmosphere at the <br>" \n            "surface. It is composed primarily of carbon dioxide (about 96.5%) and nitrogen (about 3.5%), with trace <br>" \n            "amounts of other gases, including sulfuric acid clouds that completely enshroud the planet. This thick, <br>" \n            "CO2-rich atmosphere creates a runaway greenhouse effect, making Venus the hottest planet in our solar <br>" \n            "system with surface temperatures around 464 degC. The upper atmosphere exhibits a phenomenon called <br>" \n            "\\"super-rotation,\\" where winds blow much faster than the planet\'s slow rotation.<br><br>"\n            "The \\"lower atmosphere\\" of Venus is generally considered to be the troposphere, which extends from the <br>" \n            "surface up to approximately 60-65 kilometers (visualization uses 60 km). This region contains the dense, <br>" \n            "hot air and the main cloud layers."'),
    ('VEN-4a', 'Atmosphere info -- ADD NSSDCA Source; 92-93x',
     b'venus_atmosphere_info = (\n            "Venus boasts an extremely dense atmosphere, about 90 times the pressure of Earth\'s atmosphere at the surface. It is \\n" \n            "composed primarily of carbon dioxide (about 96.5%) and nitrogen (about 3.5%), with trace amounts of other gases, \\n" \n            "including sulfuric acid clouds that completely enshroud the planet. This thick, CO2-rich atmosphere creates a runaway \\n" \n            "greenhouse effect, making Venus the hottest planet in our solar system with surface temperatures around 464 degC. The \\n" \n            "upper atmosphere exhibits a phenomenon called \\"super-rotation,\\" where winds blow much faster than the planet\'s slow \\n" \n            "rotation."\n)',
     b'# Source: NASA NSSDCA Venus Fact Sheet -- surface pressure 92 bars, surface\n#         temperature 464 degC, CO2 96.5%, N2 3.5%.\n#         Sanchez-Lavega 2018 -- troposphere/tropopause top range 60-65 km.\n# Cross-checked: NSSDCA Venus Fact Sheet via Claude 2026-08-03 (worksheet_claude_batch1_tier1_sourcing.md)\n# Cross-checked: NSSDCA Venus Fact Sheet via GPT 2026-08-03 (batch1_tier1_sourcing_gpt_independent.md)\n# NOTE: duplicated text -- the description entry in create_venus_atmosphere_shell\n#       below carries a <br> copy of this block. Edit both copies together.\nvenus_atmosphere_info = (\n            "Venus boasts an extremely dense atmosphere, about 92 to 93 times the pressure of Earth\'s atmosphere at the \\n" \n            "surface. It is composed primarily of carbon dioxide (about 96.5%) and nitrogen (about 3.5%), with trace \\n" \n            "amounts of other gases, including sulfuric acid clouds that completely enshroud the planet. This thick, \\n" \n            "CO2-rich atmosphere creates a runaway greenhouse effect, making Venus the hottest planet in our solar \\n" \n            "system with surface temperatures around 464 degC. The upper atmosphere exhibits a phenomenon called \\n" \n            "\\"super-rotation,\\" where winds blow much faster than the planet\'s slow rotation."\n)'),
    ('VEN-5b', 'Core inner Source -- annotate',
     b'        # Source: NASA Venus Fact Sheet; NASA Solar System Exploration;\n        #         iron-nickel core, radius ~3,200 km, no dynamo (slow rotation or solid core) confirmed.',
     b'        # Source: NASA Venus Fact Sheet; NASA Solar System Exploration;\n        #         iron-nickel core, radius ~3,200 km, no dynamo (slow rotation or solid core).\n        # Cross-checked: NASA Venus Fact Sheet via Claude 2026-08-03 (worksheet_claude_batch1_tier2.md)\n        # Cross-checked: NASA Venus Fact Sheet via GPT 2026-08-03 (batch1_tier2_cross_check_gpt.md)'),
    ('VEN-5a', 'Core module Source -- annotate',
     b'# Source: NASA Venus Fact Sheet; NASA Solar System Exploration;\n#         iron-nickel core, radius ~3,200 km, lack of dynamo due to slow rotation or solid core confirmed.',
     b'# Source: NASA Venus Fact Sheet; NASA Solar System Exploration;\n#         iron-nickel core, radius ~3,200 km, lack of dynamo due to slow rotation or solid core.\n# Cross-checked: NASA Venus Fact Sheet via Claude 2026-08-03 (worksheet_claude_batch1_tier2.md)\n# Cross-checked: NASA Venus Fact Sheet via GPT 2026-08-03 (batch1_tier2_cross_check_gpt.md)'),
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
