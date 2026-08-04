# -*- coding: ascii -*-
"""patch_eris_cross_check.py -- L-156 Phase 2 Batch 1 cross-check patch for eris_visualization_shells.py

Built on ee29e6c691cad2995992396e692fae1d0d5cadc0
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

HOW TO RUN
    Save this file into the SAME FOLDER as eris_visualization_shells.py, open it in
    VS Code, and click Run. No arguments, no flags, nothing to type.

    On success you get one "ok" line per edit, then:
        patch applied (N bytes)
    On failure you get a single ERROR: or ANCHOR FAIL: line and NOTHING
    is written -- the file on disk is untouched and it is always safe to
    re-check and run again.

Transactional: every anchor must match exactly once before any byte is
written. Binary mode throughout; LF endings and ASCII preserved.

9 edits, applied bottom-up by line number.
"""

import os
import sys

TARGET = 'eris_visualization_shells.py'

# (edit_id, label, old_bytes, new_bytes) -- bottom-up by line number
EDITS = [
    ('ERIS-1c', 'Hill description 9.4 -> 14.3 Mkm',
     b'            "force attracting satellites. At Eris\'s average orbital distance (~67.8 AU), the Hill sphere radius is approximately <br>" \n            "9.4 million kilometers (~0.06 AU). The shell shown here uses the perihelion distance (~38 AU), giving ~8.1 million km. <br>" \n            "Dysnomia orbits at ~37,000 km, well within either estimate.<br>" ',
     b'            "force attracting satellites. At Eris\'s average orbital distance (~67.8 AU), the Hill sphere radius is approximately <br>" \n            "14.3 million kilometers (~0.095 AU). The shell shown here uses the perihelion distance (~38 AU), giving ~8.0 million km. <br>" \n            "Dysnomia orbits at ~37,000 km, well within either estimate.<br>" '),
    ('ERIS-1b', 'Hill info text 9.4 -> 14.3 Mkm',
     b'            "Hill Sphere: At Eris\'s average orbital distance (~67.8 AU), the Hill sphere radius is approximately <br>" \n            "9.4 million kilometers (~0.06 AU). The shell shown uses the perihelion distance (~38 AU), <br>" \n            "giving ~8.1 million km. Dysnomia orbits at ~37,000 km, well within either estimate."',
     b'            "Hill Sphere: At Eris\'s average orbital distance (~67.8 AU), the Hill sphere radius is approximately <br>" \n            "14.3 million kilometers (~0.095 AU). The shell shown uses the perihelion distance (~38 AU), <br>" \n            "giving ~8.0 million km. Dysnomia orbits at ~37,000 km, well within either estimate."'),
    ('ERIS-1a', 'Hill Source -> derived; drop Verified',
     b'# Source: NASA Solar System Dynamics (mass, semi-major axis)\n# Note: Shell geometry uses perihelion-based Hill sphere (~8.1 Mkm);\n#       average orbital distance gives ~9.4 Mkm (~0.06 AU)\n# Verified: April 2026 via Gemini fact-check',
     b'# Source: Derived from JPL SSD Eris system mass 1.66e22 kg (Eris + Dysnomia by\n#         construction from Dysnomia\'s orbit) via the standard Hill approximation,\n#         Claude Opus 5 2026-08-03.\n#         Perihelion 38.0 AU gives ~8.0 Mkm (the shell uses this);\n#         semi-major axis 67.8 AU gives ~14.3 Mkm (~0.095 AU).\n#         Barycenter binary: system mass is the correct input, not Eris alone.\n# Corrected: the former "~9.4 Mkm" does not follow from these inputs.\n# Cross-checked: derived Hill radius via GPT 2026-08-03 (batch1_tier2_followup_gpt.md: 14.27 Mkm)\n# Cross-checked: derived Hill radius via Gemini 2026-08-03 (worksheet_gemini_batch1_followup.md: 14.26 Mkm)'),
    ('ERIS-4', 'Atmosphere -- ADD Sicardy 2011 Source (Tier 1)',
     b'eris_atmosphere_info = (',
     b"# Source: Sicardy et al. 2011, Nature 478:493-496 -- stellar occultation;\n#         upper limit ~1 nbar surface pressure, ~10,000x more tenuous than Pluto's.\n#         Surface temperature approximately -240 degC (modeled range -217 to -243 degC).\n# Cross-checked: Sicardy et al. 2011 via Claude 2026-08-03 (worksheet_claude_batch1_tier1_sourcing.md)\n# Cross-checked: Sicardy et al. 2011 via GPT 2026-08-03 (batch1_tier1_sourcing_gpt_independent.md)\neris_atmosphere_info = ("),
    ('ERIS-3', 'Crust Source -- drop Verified, annotate',
     b'# Source: Sicardy et al. (2011), Nature (albedo 0.96)\n#         Brown & Schaller (2007) (nitrogen/methane surface composition)\n# Verified: April 2026 via Gemini fact-check',
     b'# Source: Sicardy et al. (2011), Nature 478:493-496 (albedo 0.96)\n#         Brown & Schaller (2007) (nitrogen/methane surface composition)\n# Cross-checked: Sicardy et al. 2011 via Claude 2026-08-03 (worksheet_claude_batch1_tier2.md)\n# Cross-checked: Sicardy et al. 2011 via GPT 2026-08-03 (batch1_tier2_cross_check_gpt.md)'),
    ('ERIS-2d', 'Core description -- compositional models >85%',
     b'            "  * Compositional Models: Based on its density, scientists believe Eris is composed largely of rock (possibly over 85% of its <br>" \n            "    mass) with the remainder being primarily water ice. The ice forms the mantle surrounding the rocky core.<br>" ',
     b'            "  * Compositional Models: Based on its density, scientists believe Eris has a rock-dominated, <br>" \n            "    differentiated interior, the remainder primarily water ice forming the mantle around the core.<br>" '),
    ('ERIS-2c', 'Core description -- leading >85%',
     b'            "Core: Eris is believed to have a rocky core. Its high bulk density (around 2.5 g/cm^3) suggests that it is composed <br>" \n            "primarily of rock, making up a significant portion of its mass (possibly over 85%). This core likely contains radioactive <br>" \n            "elements, which produce internal heat.<br>" ',
     b'            "Core: Eris is believed to have a rocky core. Its high bulk density (around 2.5 g/cm^3) suggests a <br>" \n            "rock-dominated, differentiated interior. This core likely contains radioactive <br>" \n            "elements, which produce internal heat.<br>" '),
    ('ERIS-2b', 'Core info -- leading >85%',
     b'            "Core: Eris is believed to have a rocky core. Its high bulk density (around 2.5 g/cm^3) suggests that it is composed <br>" \n            "primarily of rock, making up a significant portion of its mass (possibly over 85%). This core likely contains radioactive <br>" \n            "elements, which produce internal heat."',
     b'            "Core: Eris is believed to have a rocky core. Its high bulk density (around 2.5 g/cm^3) suggests a <br>" \n            "rock-dominated, differentiated interior. This core likely contains radioactive <br>" \n            "elements, which produce internal heat."'),
    ('ERIS-2a', 'Core Source -> Nimmo & Brown 2023; drop Verified',
     b'# Source: Sicardy et al. (2011), Nature (radius 1163 km, density 2.52 g/cm^3, albedo)\n#         Glein et al. (2024) (875 K core temperature model, geochemical modeling)\n#         JWST (2023/2024) (D/H ratio in methane ice, internal heating evidence)\n# Verified: April 2026 via Gemini fact-check',
     b"# Source: Sicardy et al. (2011), Nature 478:493-496 (radius 1163 km, density 2.52 g/cm^3, albedo)\n#         Nimmo & Brown (2023), Science Advances 9, eadi9201 -- interior model inputs:\n#         radiogenic heating 4.5e-12 W/kg, thermal conductivity 3 W/m/K, surface 30 K,\n#         giving a modeled central temperature of 875 K. Modeled, not measured; one\n#         model's output, and ~500 K below rock melting.\n#         Nimmo & Brown (2023) also supports a differentiated, rock-dominated interior.\n#         JWST (2023/2024) (D/H ratio in methane ice, internal heating evidence)\n# Cross-checked: Nimmo & Brown 2023 via Claude 2026-08-03 (worksheet_claude_batch1_blind_lookup_DELTA.md)\n# Cross-checked: Nimmo & Brown 2023 via GPT 2026-08-03 (batch1_blind_source_lookup_gpt.md)"),
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
