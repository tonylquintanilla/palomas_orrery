# -*- coding: ascii -*-
"""patch_eris_br_fix.py -- L-156 geometry corrections + <br> fix for eris_visualization_shells.py

Built on 06a16df768a010205b7078630ac31bf0cd17f846
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

HOW TO RUN
    Save this file into the SAME FOLDER as eris_visualization_shells.py, open it in
    VS Code, and click Run. No arguments, no flags, nothing to type.

    Success prints one "ok" line per edit then "patch applied".
    Failure prints one ANCHOR FAIL:/ERROR: line and writes NOTHING --
    the file on disk stays untouched, so it is always safe to re-run.

Transactional: every anchor must match exactly once before any byte is
written. Binary mode throughout; LF endings and ASCII preserved.

5 edits, applied bottom-up by line number.
"""

import os
import sys

TARGET = 'eris_visualization_shells.py'

# (edit_id, label, old_bytes, new_bytes) -- bottom-up by line number
EDITS = [
    ('BR-eris_hill_sphere_info', 'eris_hill_sphere_info: 5 <br> -> \\n',
     b'eris_hill_sphere_info = (\n            "SELECT MANUAL SCALE OF AT LEAST 0.1 AU TO VISUALIZE.<br>" \n            "1.3 MB PER FRAME FOR HTML.<br><br>"\n\n            "Hill Sphere: At Eris\'s average orbital distance (~67.8 AU), the Hill sphere radius is approximately <br>" \n            "14.3 million kilometers (~0.095 AU). The shell shown uses the perihelion distance (~38 AU), <br>" \n            "giving ~8.0 million km. Dysnomia orbits at ~37,000 km, well within either estimate."\n)\n',
     b'eris_hill_sphere_info = (\n            "SELECT MANUAL SCALE OF AT LEAST 0.1 AU TO VISUALIZE.\\n" \n            "1.3 MB PER FRAME FOR HTML.\\n\\n"\n\n            "Hill Sphere: At Eris\'s average orbital distance (~67.8 AU), the Hill sphere radius is approximately \\n" \n            "14.3 million kilometers (~0.095 AU). The shell shown uses the perihelion distance (~38 AU), \\n" \n            "giving ~8.0 million km. Dysnomia orbits at ~37,000 km, well within either estimate."\n)\n'),
    ('BR-eris_atmosphere_info', 'eris_atmosphere_info: 7 <br> -> \\n',
     b'eris_atmosphere_info = (\n            "2.7 MB PER FRAME FOR HTML.<br><br>"\n            "Atmosphere: Eris has a very tenuous atmosphere that is dynamic. When Eris is at its farthest point from the Sun <br>" \n            "(aphelion), the extremely cold temperatures cause its atmosphere, likely composed of nitrogen and methane, to freeze <br>" \n            "and fall as snow onto the surface. As Eris moves closer to the Sun in its highly elliptical orbit (perihelion), the <br>" \n            "surface warms up, and these ices sublimate, potentially creating a temporary atmosphere similar to Pluto\'s. However, <br>" \n            "observations have placed a very low upper limit on the current atmospheric pressure, suggesting it is currently very <br>" \n            "thin or mostly frozen."\n)\n',
     b'eris_atmosphere_info = (\n            "2.7 MB PER FRAME FOR HTML.\\n\\n"\n            "Atmosphere: Eris has a very tenuous atmosphere that is dynamic. When Eris is at its farthest point from the Sun \\n" \n            "(aphelion), the extremely cold temperatures cause its atmosphere, likely composed of nitrogen and methane, to freeze \\n" \n            "and fall as snow onto the surface. As Eris moves closer to the Sun in its highly elliptical orbit (perihelion), the \\n" \n            "surface warms up, and these ices sublimate, potentially creating a temporary atmosphere similar to Pluto\'s. However, \\n" \n            "observations have placed a very low upper limit on the current atmospheric pressure, suggesting it is currently very \\n" \n            "thin or mostly frozen."\n)\n'),
    ('BR-eris_crust_info', 'eris_crust_info: 4 <br> -> \\n',
     b'eris_crust_info = (\n            "USE MANUAL SCALED OF 0.005 AU TO VIEW CLOSELY."\n            "4.6 MB PER FRAME FOR HTML.<br><br>"\n            "Crust: The outermost layer is a crust of frozen gases, primarily nitrogen and methane ice. Eris has a very high albedo <br>" \n            "(reflectivity), reflecting about 96% of the sunlight that hits it. This bright surface is likely due to a frost layer <br>" \n            "formed from the condensation of its atmosphere when it is far from the Sun."\n)\n',
     b'eris_crust_info = (\n            "USE MANUAL SCALED OF 0.005 AU TO VIEW CLOSELY."\n            "4.6 MB PER FRAME FOR HTML.\\n\\n"\n            "Crust: The outermost layer is a crust of frozen gases, primarily nitrogen and methane ice. Eris has a very high albedo \\n" \n            "(reflectivity), reflecting about 96% of the sunlight that hits it. This bright surface is likely due to a frost layer \\n" \n            "formed from the condensation of its atmosphere when it is far from the Sun."\n)\n'),
    ('BR-eris_mantle_info', 'eris_mantle_info: 6 <br> -> \\n',
     b'eris_mantle_info = (\n            "2.1 MB PER FRAME FOR HTML.<br><br>"\n            "Mantle: Surrounding the rocky core is a substantial mantle made of water ice. Unlike Pluto\'s ice shell, Eris\'s ice <br>" \n            "mantle is thought to be convecting. This means that the warmer ice closer to the core rises, while the colder ice near <br>" \n            "the surface sinks, a process that helps dissipate the internal heat generated by the core. The thickness of this ice <br>" \n            "shell is estimated to be around 100 kilometers. There is currently no evidence to suggest the presence of a subsurface <br>" \n            "ocean within Eris."\n)\n',
     b'eris_mantle_info = (\n            "2.1 MB PER FRAME FOR HTML.\\n\\n"\n            "Mantle: Surrounding the rocky core is a substantial mantle made of water ice. Unlike Pluto\'s ice shell, Eris\'s ice \\n" \n            "mantle is thought to be convecting. This means that the warmer ice closer to the core rises, while the colder ice near \\n" \n            "the surface sinks, a process that helps dissipate the internal heat generated by the core. The thickness of this ice \\n" \n            "shell is estimated to be around 100 kilometers. There is currently no evidence to suggest the presence of a subsurface \\n" \n            "ocean within Eris."\n)\n'),
    ('BR-eris_core_info', 'eris_core_info: 6 <br> -> \\n',
     b'eris_core_info = (\n            "2.4 MB PER FRAME FOR HTML.<br><br>"\n            "Eris, a dwarf planet in the Kuiper Belt, has a structure that scientists have been piecing together through observations <br>" \n            "and theoretical modeling. Here\'s what we currently understand:<br>" \n            "Core: Eris is believed to have a rocky core. Its high bulk density (around 2.5 g/cm^3) suggests a <br>" \n            "rock-dominated, differentiated interior. This core likely contains radioactive <br>" \n            "elements, which produce internal heat."\n)\n',
     b'eris_core_info = (\n            "2.4 MB PER FRAME FOR HTML.\\n\\n"\n            "Eris, a dwarf planet in the Kuiper Belt, has a structure that scientists have been piecing together through observations \\n" \n            "and theoretical modeling. Here\'s what we currently understand:\\n" \n            "Core: Eris is believed to have a rocky core. Its high bulk density (around 2.5 g/cm^3) suggests a \\n" \n            "rock-dominated, differentiated interior. This core likely contains radioactive \\n" \n            "elements, which produce internal heat."\n)\n'),
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
