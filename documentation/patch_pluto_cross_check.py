# -*- coding: ascii -*-
"""patch_pluto_cross_check.py -- L-156 Phase 2 Batch 1 cross-check patch for pluto_visualization_shells.py

Built on ee29e6c691cad2995992396e692fae1d0d5cadc0
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

HOW TO RUN
    Save this file into the SAME FOLDER as pluto_visualization_shells.py, open it in
    VS Code, and click Run. No arguments, no flags, nothing to type.

    On success you get one "ok" line per edit, then:
        patch applied (N bytes)
    On failure you get a single ERROR: or ANCHOR FAIL: line and NOTHING
    is written -- the file on disk is untouched and it is always safe to
    re-check and run again.

Transactional: every anchor must match exactly once before any byte is
written. Binary mode throughout; LF endings and ASCII preserved.

18 edits, applied bottom-up by line number.
"""

import os
import sys

TARGET = 'pluto_visualization_shells.py'

# (edit_id, label, old_bytes, new_bytes) -- bottom-up by line number
EDITS = [
    ('PLUT-1c', 'Hill inner Source -- derived',
     b'        # Source: NASA Solar System Dynamics (SSD); NASA Pluto Fact Sheet;\n        #         Hill sphere ~5.99 million km (0.04 AU) confirmed; all 5 moons within confirmed.',
     b'        # Source: Derived from JPL SSD Pluto-Charon system GM (869.3 + 106.1 km^3/s^2)\n        #         at perihelion 29.66 AU: ~5.99 Mkm (0.04 AU) = 5041 Pluto radii.\n        #         All 5 moons (Charon, Styx, Nix, Kerberos, Hydra) lie within.\n        # Cross-checked: Pluto/Charon GM via GPT 2026-08-03 (batch1_blind_source_lookup_gpt.md)\n        # Cross-checked: derived Hill radius via Claude 2026-08-03 (worksheet_claude_batch1_tier2.md)'),
    ('PLUT-1b', 'Hill radius_fraction 4685 -> 5041',
     b"        'radius_fraction': 4685, ",
     b"        'radius_fraction': 5041,  # ~5.99 Mkm at perihelion (Pluto-Charon system mass)"),
    ('PLUT-1a', 'Hill module Source -- derived; note geometry fix',
     b'# Source: NASA Solar System Dynamics (SSD); NASA Pluto Fact Sheet;\n#         Hill sphere ~5.99 million km (0.04 AU); all 5 moons (Charon, Styx, Nix, Kerberos, Hydra) confirmed within.',
     b'# Source: Derived from JPL SSD GM values for the Pluto-Charon system\n#         (GM_Pluto 869.3 + GM_Charon 106.1 km^3/s^2) at perihelion 29.66 AU,\n#         via the standard Hill approximation, Claude Opus 5 2026-08-03.\n#         Result ~5.99 Mkm (0.04 AU) = 5041 Pluto radii.\n#         Barycenter binary: system mass is the correct input, not Pluto alone.\n# Corrected: the former radius_fraction 4685 drew a ~5.57 Mkm shell while the text\n#            claimed 5.99 Mkm -- geometry and text now agree.\n# Cross-checked: Pluto/Charon GM values via GPT 2026-08-03 (batch1_blind_source_lookup_gpt.md)\n# Cross-checked: derived Hill radius via Claude 2026-08-03 (worksheet_claude_batch1_tier2.md)'),
    ('PLUT-2e', 'Exobase summary 0.43 -> 1.43 altitude / 2.43 from center',
     b'            "considering the exobase, the atmosphere reaches about 0.43 Pluto radii above the surface, or 1.43 Pluto radii from the center. <br>" ',
     b'            "considering the exobase, the atmosphere reaches about 1.43 Pluto radii above the surface, or 2.43 Pluto radii from the center. <br>" '),
    ('PLUT-2d', 'Exobase fraction 1.43 -> 2.43 from center',
     b'            "* Significant Atmosphere: The atmosphere, composed primarily of nitrogen with traces of methane and carbon monoxide, has <br>" \n            "  been detected extending up to 1700 km above the surface (the exobase).<br>" \n            "* In Pluto radii: To express this as a fraction of Pluto\'s radius: ~1.43.<br>" ',
     b'            "* Significant Atmosphere: The atmosphere, composed primarily of nitrogen with traces of methane and carbon monoxide, has <br>" \n            "  been detected extending up to 1700 km above the surface (the exobase).<br>" \n            "* In Pluto radii: 1700 km of altitude is ~1.43 Pluto radii, i.e. ~2.43 Pluto radii measured from the center.<br>" '),
    ('PLUT-2c', 'Atmosphere inner Source -> Young 2018',
     b'        # Source: Stern et al. (2015, Science); Gladstone et al. (2016, Science);\n        #         exobase ~1,700 km / ~1.43 Pluto radii confirmed; temperature inversion (40 K surface -> 110 K at 30 km) confirmed.',
     b'        # Source: Young et al. 2018, Icarus 300:174 -- exobase ~1,710 km altitude\n        #         (~2,900 km from center, ~2.43 R_Pluto). Supersedes Gladstone 2016.\n        #         Stern et al. (2015, Science) -- temperature inversion.\n        # Corrected: former "~1.43 Pluto radii" treated the 1,700 km ALTITUDE as a\n        #            center distance. From center the exobase is ~2.43 R_Pluto.\n        # Cross-checked: Young et al. 2018 via Claude 2026-08-03 (worksheet_claude_batch1_followup.md)\n        # Cross-checked: Young et al. 2018 via GPT 2026-08-03 (batch1_tier2_followup_gpt.md)'),
    ('PLUT-2b', 'Atmosphere radius_fraction 1.43 -> 2.43',
     b"        'radius_fraction': 1.43,  ",
     b"        'radius_fraction': 2.43,  # exobase FROM CENTER (1,710 km altitude + 1,188.3 km radius)"),
    ('PLUT-2a', 'Atmosphere module Source -> Young 2018',
     b"# Source: Stern et al. (2015, Science); Gladstone et al. (2016, Science);\n#         surface pressure ~10 microbars (1/100,000th Earth's); exobase ~1,700 km; 20+ haze layers confirmed.",
     b'# Source: Young et al. 2018, Icarus 300:174 -- Pluto exobase at ~1,710 km altitude\n#         (~2,900 km from center, ~2.43 Pluto radii). Supersedes Gladstone et al. 2016\n#         for exobase altitude.\n#         Stern et al. (2015, Science) -- surface pressure ~10 microbars (1/100,000th Earth\'s);\n#         20+ haze layers.\n# Corrected: the former "~1.43 Pluto radii" treated the 1,700 km ALTITUDE as if it\n#            were a center distance. From center the exobase is ~2.43 R_Pluto.\n# Cross-checked: Young et al. 2018 via Claude 2026-08-03 (worksheet_claude_batch1_followup.md)\n# Cross-checked: Young et al. 2018 via GPT 2026-08-03 (batch1_tier2_followup_gpt.md)'),
    ('PLUT-6b', 'Haze inner Source -- annotate',
     b'        # Source: Stern et al. (2015, Science); Gladstone et al. (2016, Science);\n        #         20 distinct haze layers up to 200 km, tholin formation mechanism, blue backlit color all confirmed.',
     b'        # Source: Stern et al. (2015, Science); Gladstone et al. (2016, Science);\n        #         20 distinct haze layers up to 200 km, tholin formation, blue backlit color.\n        # Cross-checked: Gladstone et al. 2016 via Claude 2026-08-03 (worksheet_claude_batch1_tier2.md)\n        # Cross-checked: Gladstone et al. 2016 via GPT 2026-08-03 (batch1_tier2_cross_check_gpt.md)'),
    ('PLUT-6a', 'Haze module Source -- annotate',
     b'# Source: Stern et al. (2015, Science); Gladstone et al. (2016, Science);\n#         20+ haze layers up to 200 km confirmed by New Horizons; temperature inversion confirmed.',
     b'# Source: Stern et al. (2015, Science); Gladstone et al. (2016, Science);\n#         20+ haze layers up to 200 km observed by New Horizons; temperature inversion.\n# Cross-checked: Gladstone et al. 2016 via Claude 2026-08-03 (worksheet_claude_batch1_tier2.md)\n# Cross-checked: Gladstone et al. 2016 via GPT 2026-08-03 (batch1_tier2_cross_check_gpt.md)'),
    ('PLUT-4c', 'Crust display -- drop >98% purity',
     b'            "* Pluto\'s surface, or crust, is composed of various ices, primarily nitrogen ice (over 98%). It also contains smaller <br>" ',
     b'            "* Pluto\'s surface, or crust, is composed of various ices, predominantly nitrogen ice. It also contains smaller <br>" '),
    ('PLUT-4b', 'Crust inner Source -- Grundy 2016; drop >98%',
     b'        # Source: NASA Pluto Fact Sheet; Stern et al. (2015, Science);\n        #         N2 ice >98%, water-ice mountains (2-3 km, Rocky Mountain scale), Sputnik Planitia convection confirmed.',
     b'        # Source: NASA Pluto Fact Sheet; Stern et al. (2015, Science);\n        #         Grundy et al. (2016, Science) -- surface composition mapping.\n        #         N2-dominated ice surface, water-ice mountains (2-3 km), Sputnik Planitia convection.\n        # Removed: former ">98%" N2 purity -- no published paper quantifies it.\n        # Cross-checked: Grundy et al. 2016 via GPT 2026-08-03 (batch1_tier2_followup_gpt.md)\n        # Cross-checked: Grundy et al. 2016 via Gemini 2026-08-03 (worksheet_gemini_batch1_followup.md)'),
    ('PLUT-4a', 'Crust module Source -- Grundy 2016; drop >98%',
     b'# Source: NASA Pluto Fact Sheet; Stern et al. (2015, Science);\n#         N2 ice surface (>98% in Sputnik Planitia), water-ice mountains 2-3 km, Sputnik Planitia age <10 Myr confirmed.',
     b'# Source: NASA Pluto Fact Sheet; Stern et al. (2015, Science);\n#         Grundy et al. (2016, Science) -- surface composition mapping;\n#         N2-dominated ice surface (Sputnik Planitia), water-ice mountains 2-3 km,\n#         Sputnik Planitia age <10 Myr.\n# Removed: former ">98%" N2 purity. No published paper quantifies N2 ice purity;\n#          replaced with a qualitative statement rather than re-cited.\n# Cross-checked: Grundy et al. 2016 via GPT 2026-08-03 (batch1_tier2_followup_gpt.md)\n# Cross-checked: Grundy et al. 2016 via Gemini 2026-08-03 (worksheet_gemini_batch1_followup.md)'),
    ('PLUT-5b', 'Mantle inner Source -- annotate',
     b'        # Source: NASA New Horizons Mission Press Kit; Stern et al. (2015); Bierson et al. (2020);\n        #         ocean 100-180 km thick; lithosphere at least 300 km thick in some models to support high mountains.',
     b'        # Source: NASA New Horizons Mission Press Kit; Stern et al. (2015); Bierson et al. (2020);\n        #         ocean 100-180 km thick; lithosphere at least 300 km thick in some models to support high mountains.\n        # Cross-checked: Bierson et al. 2020 via Claude 2026-08-03 (worksheet_claude_batch1_tier2.md)\n        # Cross-checked: Bierson et al. 2020 via GPT 2026-08-03 (batch1_tier2_cross_check_gpt.md)'),
    ('PLUT-5a', 'Mantle module Source -- annotate',
     b'# Source: NASA New Horizons Mission Press Kit; Stern et al. (2015, Science); Bierson et al. (2020, Nature Geoscience);\n#         water-ice mantle, subsurface ocean 100-180 km thick with ammonia antifreeze confirmed.',
     b'# Source: NASA New Horizons Mission Press Kit; Stern et al. (2015, Science); Bierson et al. (2020, Nature Geoscience);\n#         water-ice mantle, subsurface ocean 100-180 km thick with ammonia antifreeze.\n# Cross-checked: Bierson et al. 2020 via Claude 2026-08-03 (worksheet_claude_batch1_tier2.md)\n# Cross-checked: Bierson et al. 2020 via GPT 2026-08-03 (batch1_tier2_cross_check_gpt.md)'),
    ('PLUT-3c', 'Core display -- drop 1000 K; fix surface 37-39 K',
     b'            "  maintaining this liquid layer.<br>" \n            "* Estimated Temperature: The estimated temperature of Pluto\'s core is around 1000 K. This estimate comes from models that <br>" \n            "  consider the heat generated by radioactive decay within a rocky core. These models also need to account for the heat transfer <br>" \n            "  through the icy mantle. Future research and more detailed data could refine this value. The exact temperature would depend on <br>" \n            "  the precise composition of the core and the efficiency of heat transfer through the mantle. In comparison, the surface <br>" \n            "  temperature of Pluto is extremely cold, around 40 K. The significant difference highlights the internal heating processes at <br>" \n            "  work within the dwarf planet. "',
     b'            "  maintaining this liquid layer.<br>" \n            "* Estimated Temperature: Bierson et al. (2020) support a hot-start formation history for Pluto, but no <br>" \n            "  published value fixes a present-day core temperature; models depend on the precise core composition <br>" \n            "  and on the efficiency of heat transfer through the icy mantle. In comparison, the surface temperature <br>" \n            "  of Pluto is extremely cold, approximately 37-39 K (Gladstone et al. 2016: 37 +/- 3 K; REX analysis: <br>" \n            "  38.9 +/- 2.1 K). The significant difference highlights the internal heating processes at work within <br>" \n            "  the dwarf planet. "'),
    ('PLUT-3b', 'Core inner Source -- drop ~1,000 K',
     b'        # Source: Stern et al. (2015, Science); Bierson et al. (2020, Nature Geoscience);\n        #         core ~1,700 km / 70% diameter, radioactive isotopes (U-238, U-235, Th-232, K-40), ~1,000 K, ocean evidence all confirmed.',
     b'        # Source: Stern et al. (2015, Science); Bierson et al. (2020, Nature Geoscience);\n        #         core ~1,700 km / 70% diameter, radioactive isotopes (U-238, U-235, Th-232, K-40), ocean evidence.\n        # Removed: former "~1,000 K" core temperature -- see module-level note above.\n        # Cross-checked: Bierson et al. 2020 via Claude 2026-08-03 (worksheet_claude_batch1_tier2.md)\n        # Cross-checked: Bierson et al. 2020 via GPT 2026-08-03 (batch1_tier2_cross_check_gpt.md)'),
    ('PLUT-3a', 'Core module Source -- drop core temp ~1,000 K',
     b'# Source: Stern et al. (2015, Science); Bierson et al. (2020, Nature Geoscience);\n#         rocky core ~1,700 km diameter (~70% of total), radioactive heating (U, Th, K), core temp ~1,000 K confirmed.',
     b'# Source: Stern et al. (2015, Science); Bierson et al. (2020, Nature Geoscience);\n#         rocky core ~1,700 km diameter (~70% of total), radioactive heating (U, Th, K).\n# Removed: former "core temp ~1,000 K". Bierson et al. 2020 supports a hot-start\n#          formation history but states no specific present-day core temperature;\n#          verified absent from the abstract. Removed rather than re-cited.\n# Cross-checked: Bierson et al. 2020 via Claude 2026-08-03 (worksheet_claude_batch1_tier2.md)\n# Cross-checked: Bierson et al. 2020 via GPT 2026-08-03 (batch1_tier2_cross_check_gpt.md)'),
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
