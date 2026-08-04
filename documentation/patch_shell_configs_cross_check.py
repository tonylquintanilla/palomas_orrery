# -*- coding: ascii -*-
"""patch_shell_configs_cross_check.py -- L-156 Phase 2 Batch 1 cross-check patch for shell_configs.py

Built on ee29e6c691cad2995992396e692fae1d0d5cadc0
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

HOW TO RUN
    Save this file into the SAME FOLDER as shell_configs.py, open it in
    VS Code, and click Run. No arguments, no flags, nothing to type.

    On success you get one "ok" line per edit, then:
        patch applied (N bytes)
    On failure you get a single ERROR: or ANCHOR FAIL: line and NOTHING
    is written -- the file on disk is untouched and it is always safe to
    re-check and run again.

Transactional: every anchor must match exactly once before any byte is
written. Binary mode throughout; LF endings and ASCII preserved.

24 edits, applied bottom-up by line number.
"""

import os
import sys

TARGET = 'shell_configs.py'

# (edit_id, label, old_bytes, new_bytes) -- bottom-up by line number
EDITS = [
    ('SC-MERC-2c', 'CUSTOM_SHELLS sodium tail tooltip 10000 -> range',
     b'                "TO VISUALIZE THE COMPLETE TAIL INCLUDE VENUS IN THE PLOT OR SET MANUAL SCALE TO 1.0 AU\\n\\n"\n                "Sodium Tail: Mercury has a remarkable sodium tail that extends incredibly far into space - up to 10,000 Mercury radii \\n"\n                "(approximately 24 million kilometers). This tail is created when sodium atoms from Mercury\'s exosphere \\n"',
     b'                "Sodium Tail: Mercury has a remarkable sodium tail. Observations place its extent in the range \\n"\n                "~120 to ~1,400 Mercury radii (approximately 0.3 to 3.4 million kilometers), varying strongly \\n"\n                "with orbital position and solar activity. This tail is created when sodium atoms from Mercury\'s exosphere \\n"'),
    ('SC-VEN-3b', 'Venus upper atm -- soften ionosphere peak',
     b'                "* Ionosphere (~120 km to several hundred km): peak electron density ~120 - 140 km; up to ~8% of the <br>"',
     b'                "* Ionosphere (~120 km to several hundred km): peak electron density in the upper atmosphere; up to ~8% of the <br>"'),
    ('SC-VEN-3a', 'Venus upper atm -- soften thermosphere 300 K',
     b'                "* Thermosphere (~90 - 200+ km): heated by solar EUV yet cold (~300 K dayside, colder at night, the <br>"',
     b'                "* Thermosphere (~90 - 200+ km): heated by solar EUV yet cold, varying with altitude, local time and solar <br>"'),
    ('SC-VEN-4b', 'Venus atmosphere tooltip 90 -> 92-93 times',
     b'                "Venus boasts an extremely dense atmosphere, about 90 times the pressure of Earth\'s atmosphere at the surface. It is \\n" ',
     b'                "Venus boasts an extremely dense atmosphere, about 92 to 93 times the pressure of Earth\'s atmosphere at the \\n" '),
    ('SC-VEN-4a', 'Venus atmosphere hover 90 -> 92-93x; troposphere 60-65 km',
     b'                "Venus boasts an extremely dense atmosphere, about 90 times the pressure of Earth\'s atmosphere at the surface. It is <br>" \n                "composed primarily of carbon dioxide (about 96.5%) and nitrogen (about 3.5%), with trace amounts of other gases, <br>" \n                "including sulfuric acid clouds that completely enshroud the planet. This thick, CO2-rich atmosphere creates a runaway <br>" \n                "greenhouse effect, making Venus the hottest planet in our solar system with surface temperatures around 464 degC. The <br>" \n                "upper atmosphere exhibits a phenomenon called \\"super-rotation,\\" where winds blow much faster than the planet\'s slow <br>" \n                "rotation.<br><br>"\n                "The \\"lower atmosphere\\" of Venus is generally considered to be the troposphere, which extends from the surface up to <br>" \n                "an altitude of approximately 60 kilometers. This region contains the dense, hot air and the main cloud layers."',
     b'                "Venus boasts an extremely dense atmosphere, about 92 to 93 times the pressure of Earth\'s atmosphere at the <br>" \n                "surface. It is composed primarily of carbon dioxide (about 96.5%) and nitrogen (about 3.5%), with trace <br>" \n                "amounts of other gases, including sulfuric acid clouds that completely enshroud the planet. This thick, <br>" \n                "CO2-rich atmosphere creates a runaway greenhouse effect, making Venus the hottest planet in our solar <br>" \n                "system with surface temperatures around 464 degC. The upper atmosphere exhibits a phenomenon called <br>" \n                "\\"super-rotation,\\" where winds blow much faster than the planet\'s slow rotation.<br><br>"\n                "The \\"lower atmosphere\\" of Venus is generally considered to be the troposphere, which extends from the <br>" \n                "surface up to approximately 60-65 kilometers (visualization uses 60 km). This region contains the dense, hot air and the main cloud layers."'),
    ('SC-ERIS-1b', 'Eris Hill tooltip 9.4 -> 14.3 Mkm',
     b'                "Hill Sphere: At Eris\'s average orbital distance (~67.8 AU), the Hill sphere radius is approximately \\n" \n                "9.4 million kilometers (~0.06 AU). The shell shown uses the perihelion distance (~38 AU), \\n" \n                "giving ~8.1 million km. Dysnomia orbits at ~37,000 km, well within either estimate."',
     b'                "Hill Sphere: At Eris\'s average orbital distance (~67.8 AU), the Hill sphere radius is approximately \\n" \n                "14.3 million kilometers (~0.095 AU). The shell shown uses the perihelion distance (~38 AU), \\n" \n                "giving ~8.0 million km. Dysnomia orbits at ~37,000 km, well within either estimate."'),
    ('SC-ERIS-1a', 'Eris Hill hover 9.4 -> 14.3 Mkm',
     b'                "force attracting satellites. At Eris\'s average orbital distance (~67.8 AU), the Hill sphere radius is approximately <br>" \n                "9.4 million kilometers (~0.06 AU). The shell shown here uses the perihelion distance (~38 AU), giving ~8.1 million km. <br>" ',
     b'                "force attracting satellites. At Eris\'s average orbital distance (~67.8 AU), the Hill sphere radius is approximately <br>" \n                "14.3 million kilometers (~0.095 AU). The shell shown here uses the perihelion distance (~38 AU), giving ~8.0 million km. <br>" '),
    ('SC-ERIS-2c', 'Eris core tooltip >85%',
     b'                "Core: Eris is believed to have a rocky core. Its high bulk density (around 2.5 g/cm^3) suggests that it is composed \\n" \n                "primarily of rock, making up a significant portion of its mass (possibly over 85%). This core likely contains radioactive \\n" ',
     b'                "Core: Eris is believed to have a rocky core. Its high bulk density (around 2.5 g/cm^3) suggests a \\n" \n                "rock-dominated, differentiated interior. This core likely contains radioactive \\n" '),
    ('SC-ERIS-2b', 'Eris core hover -- compositional models >85%',
     b'                "  * Compositional Models: Based on its density, scientists believe Eris is composed largely of rock (possibly over 85% of its <br>" \n                "    mass) with the remainder being primarily water ice. The ice forms the mantle surrounding the rocky core.<br>" ',
     b'                "  * Compositional Models: Based on its density, scientists believe Eris has a rock-dominated, <br>" \n                "    differentiated interior, the remainder primarily water ice forming the mantle around the core.<br>" '),
    ('SC-ERIS-2a', 'Eris core hover -- leading >85%',
     b'                "Core: Eris is believed to have a rocky core. Its high bulk density (around 2.5 g/cm^3) suggests that it is composed <br>" \n                "primarily of rock, making up a significant portion of its mass (possibly over 85%). This core likely contains radioactive <br>" ',
     b'                "Core: Eris is believed to have a rocky core. Its high bulk density (around 2.5 g/cm^3) suggests a <br>" \n                "rock-dominated, differentiated interior. This core likely contains radioactive <br>" '),
    ('SC-PLUT-1', 'Pluto Hill radius_fraction 4685 -> 5041',
     b"            'name': 'Hill Sphere',\n            'radius_fraction': 4685,\n            'color': 'rgb(0, 255, 0)',",
     b"            'name': 'Hill Sphere',\n            'radius_fraction': 5041,  # ~5.99 Mkm at perihelion (Pluto-Charon system mass)\n            'color': 'rgb(0, 255, 0)',"),
    ('SC-PLUT-2c', 'Pluto exobase summary 0.43 -> 1.43 / 2.43',
     b'                "considering the exobase, the atmosphere reaches about 0.43 Pluto radii above the surface, or 1.43 Pluto radii from the center. <br>" ',
     b'                "considering the exobase, the atmosphere reaches about 1.43 Pluto radii above the surface, or 2.43 Pluto radii from the center. <br>" '),
    ('SC-PLUT-2b', 'Pluto exobase fraction ~1.43 -> ~2.43',
     b'                "* In Pluto radii: To express this as a fraction of Pluto\'s radius: ~1.43.<br>" ',
     b'                "* In Pluto radii: 1700 km of altitude is ~1.43 Pluto radii, i.e. ~2.43 Pluto radii measured from the center.<br>" '),
    ('SC-PLUT-2a', 'Pluto atmosphere radius_fraction 1.43 -> 2.43',
     b"            'radius_fraction': 1.43,",
     b"            'radius_fraction': 2.43,  # exobase FROM CENTER (1,710 km altitude + 1,188.3 km radius)"),
    ('SC-PLUT-4', 'Pluto crust -- drop >98% purity',
     b'                "* Pluto\'s surface, or crust, is composed of various ices, primarily nitrogen ice (over 98%). It also contains smaller <br>" ',
     b'                "* Pluto\'s surface, or crust, is composed of various ices, predominantly nitrogen ice. It also contains smaller <br>" '),
    ('SC-PLUT-3', 'Pluto core -- drop 1000 K; surface 37-39 K',
     b'                "* Estimated Temperature: The estimated temperature of Pluto\'s core is around 1000 K. This estimate comes from models that <br>" \n                "  consider the heat generated by radioactive decay within a rocky core. These models also need to account for the heat transfer <br>" \n                "  through the icy mantle. Future research and more detailed data could refine this value. The exact temperature would depend on <br>" \n                "  the precise composition of the core and the efficiency of heat transfer through the mantle. In comparison, the surface <br>" \n                "  temperature of Pluto is extremely cold, around 40 K. The significant difference highlights the internal heating processes at <br>" \n                "  work within the dwarf planet. "',
     b'                "* Estimated Temperature: Bierson et al. (2020) support a hot-start formation history for Pluto, but no <br>" \n                "  published value fixes a present-day core temperature; models depend on the precise core composition <br>" \n                "  and on the efficiency of heat transfer through the icy mantle. In comparison, the surface temperature <br>" \n                "  of Pluto is extremely cold, approximately 37-39 K (Gladstone et al. 2016: 37 +/- 3 K; REX analysis: <br>" \n                "  38.9 +/- 2.1 K). The significant difference highlights the internal heating processes at work within <br>" \n                "  the dwarf planet. "'),
    ('SC-MOON-3', 'Moon outer core -- drop 1300-1600 K',
     b'                "* Estimated Temperature: This layer would be slightly cooler than the inner core, but still hot enough to be molten at <br>"\n                "  the lower pressures found here. Estimates typically fall around 1300 K to 1600 K. Let\'s use 1500 K as a representative <br>"\n                "  value for the outer core for your model.<br>"',
     b'                "* Estimated Temperature: This layer is hot enough to be molten at the lower pressures found here, but the <br>"\n                "  temperature is model-dependent and not well constrained.<br>"'),
    ('SC-MOON-4', 'Moon inner core -- drop 1600-1700 K',
     b'                "  * Estimates for the temperature of the Moon\'s inner core vary slightly depending on the studies and methods used, but <br>"\n                "    some more recent reanalyses of seismic data suggest temperatures around 1600-1700 K."',
     b'                "  * The temperature of the inner core is model-dependent and not well constrained; <br>"\n                "    seismic data constrain its size, not its temperature."'),
    ('SC-MERC-2b', 'Mercury exosphere summary 10,000 R_M',
     b'                "the sodium tail is a significant feature that extends incredibly far, up to 10,000 Mercury radii. The main body of the exosphere <br>"',
     b'                "the sodium tail is a significant feature that extends to ~120 - 1,400 Mercury radii. The main body of the exosphere <br>"'),
    ('SC-MERC-2a', 'Mercury exosphere sodium tail extent',
     b'                "  This tail has been detected extending to distances of over 24 million kilometers (approximately 10,000 Mercury radii) <br>"',
     b'                "  This tail has been detected extending to ~120 - 1,400 Mercury radii (roughly 0.3 - 3.4 million kilometers) <br>"'),
    ('SC-MERC-4b', 'Mercury crust tooltip -- 26 km, drop diamonds',
     b'                "Mercury has a solid silicate crust that is heavily cratered, resembling Earth\'s Moon. The crust is likely quite thin \\n"\n                "compared to Earth\'s. There\'s also a theory that a significant portion of Mercury\'s crust might be made of diamonds, \\n"\n                "formed by billions of years of meteorite impacts on a graphite-rich surface. About 35 km thick."',
     b'                "Mercury has a solid silicate crust that is heavily cratered, resembling Earth\'s Moon. The crust is likely quite thin \\n"\n                "compared to Earth\'s. About 26 km thick (Sori 2018)."'),
    ('SC-MERC-4a', 'Mercury crust hover -- 26 km, drop diamonds',
     b'                "Mercury has a solid silicate crust that is heavily cratered, resembling Earth\'s Moon. The crust is likely quite thin <br>"\n                "compared to Earth\'s. There\'s also a theory that a significant portion of Mercury\'s crust might be made of diamonds, <br>"\n                "formed by billions of years of meteorite impacts on a graphite-rich surface. About 35 km thick."',
     b'                "Mercury has a solid silicate crust that is heavily cratered, resembling Earth\'s Moon. The crust is likely quite thin <br>"\n                "compared to Earth\'s. About 26 km thick (Sori 2018)."'),
    ('SC-MERC-3b', 'Mercury outer core tooltip -- core radius 2020 km',
     b'                "Outer Core: Surrounding the solid inner core is a liquid metallic outer core. The movement of this molten iron \\n"\n                "is thought to be the source of Mercury\'s weak magnetic field. About 1074 km thick."',
     b'                "Outer Core: Surrounding the solid inner core is a liquid metallic outer core. The movement of this molten iron \\n"\n                "is thought to be the source of Mercury\'s weak magnetic field. Core radius approximately 2020 km."'),
    ('SC-MERC-3a', 'Mercury outer core hover -- core radius 2020 km',
     b'                "Outer Core: Surrounding the solid inner core is a liquid metallic outer core. The movement of this molten iron <br>"\n                "is thought to be the source of Mercury\'s weak magnetic field. About 1074 km thick."',
     b'                "Outer Core: Surrounding the solid inner core is a liquid metallic outer core. The movement of this molten iron <br>"\n                "is thought to be the source of Mercury\'s weak magnetic field. Core radius approximately 2020 km."'),
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
