# -*- coding: ascii -*-
"""patch_moon_br_fix.py -- L-156 geometry corrections + <br> fix for moon_visualization_shells.py

Built on 06a16df768a010205b7078630ac31bf0cd17f846
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

HOW TO RUN
    Save this file into the SAME FOLDER as moon_visualization_shells.py, open it in
    VS Code, and click Run. No arguments, no flags, nothing to type.

    Success prints one "ok" line per edit then "patch applied".
    Failure prints one ANCHOR FAIL:/ERROR: line and writes NOTHING --
    the file on disk stays untouched, so it is always safe to re-run.

Transactional: every anchor must match exactly once before any byte is
written. Binary mode throughout; LF endings and ASCII preserved.

6 edits, applied bottom-up by line number.
"""

import os
import sys

TARGET = 'moon_visualization_shells.py'

# (edit_id, label, old_bytes, new_bytes) -- bottom-up by line number
EDITS = [
    ('MOON-ARTIFACT', "dead description: stray '<br>:' -> '<br>'",
     b'            "330 kilometers. There might also be a small, partially molten layer of silicates around the outer core.<br>:" ',
     b'            "330 kilometers. There might also be a small, partially molten layer of silicates around the outer core.<br>" '),
    ('BR-moon_exosphere_info', 'moon_exosphere_info: 8 <br> -> \\n',
     b'moon_exosphere_info = (\n            "The Moon essentially has no atmosphere in the traditional sense. Instead, it has an exosphere. It\'s an incredibly <br>" \n            "tenuous layer of gases, far less dense than a vacuum on Earth. It\'s so thin that gas molecules rarely collide with <br>" \n            "each other.<br>" \n            "* Sources: The exosphere is formed from gases released from the Moon\\\'s interior from radioactive decay, outgassing <br>" \n            "  from the surface due to solar wind bombardment, and micrometeoroid impacts.<br>" \n            "* Composition: Primarily composed of noble gases like argon and helium, along with trace amounts of sodium, potassium, <br>" \n            "  hydrogen, and other elements.<br>" \n            "* No Weather: Due to its extreme thinness, there\'s no atmospheric pressure, no wind, no weather, and no significant <br>" \n            "  shielding from solar radiation or micrometeoroids."\n)\n',
     b'moon_exosphere_info = (\n            "The Moon essentially has no atmosphere in the traditional sense. Instead, it has an exosphere. It\'s an incredibly \\n" \n            "tenuous layer of gases, far less dense than a vacuum on Earth. It\'s so thin that gas molecules rarely collide with \\n" \n            "each other.\\n" \n            "* Sources: The exosphere is formed from gases released from the Moon\\\'s interior from radioactive decay, outgassing \\n" \n            "  from the surface due to solar wind bombardment, and micrometeoroid impacts.\\n" \n            "* Composition: Primarily composed of noble gases like argon and helium, along with trace amounts of sodium, potassium, \\n" \n            "  hydrogen, and other elements.\\n" \n            "* No Weather: Due to its extreme thinness, there\'s no atmospheric pressure, no wind, no weather, and no significant \\n" \n            "  shielding from solar radiation or micrometeoroids."\n)\n'),
    ('BR-moon_crust_info', 'moon_crust_info: 10 <br> -> \\n',
     b'moon_crust_info = (\n            "The outermost layer of the Moon is its crust, which is significantly thicker on the far side than on the near side:<br>" \n            "* Composition: Dominated by anorthositic rocks (rich in plagioclase feldspar), which are lighter in color and form the <br>" \n            "  lunar highlands. The dark maria, on the other hand, are vast basaltic plains formed by ancient volcanic eruptions that <br>" \n            "  filled large impact basins.<br>" \n            "* Thickness: The lunar crust varies in thickness. On the near side (facing Earth), it\'s estimated to be around 30-50 <br>" \n            "  kilometers thick. On the far side, it can be much thicker, possibly reaching up to 100 kilometers or more. This <br>" \n            "  asymmetry is a major characteristic of the Moon. The most compelling explanations for the Moon\'s crustal thickness <br>" \n            "  asymmetry point to a combination of factors related to its formation in Earth\\\'s intense thermal environment and a <br>" \n            "  massive early impact that shaped its internal heat distribution and subsequent geological evolution.<br>" \n            "* Surface Features: The crust is heavily cratered due to billions of years of impacts from asteroids and comets. Other <br>" \n            "  features include rilles (channels, often associated with lava flows), domes, and wrinkle ridges."\n)\n',
     b'moon_crust_info = (\n            "The outermost layer of the Moon is its crust, which is significantly thicker on the far side than on the near side:\\n" \n            "* Composition: Dominated by anorthositic rocks (rich in plagioclase feldspar), which are lighter in color and form the \\n" \n            "  lunar highlands. The dark maria, on the other hand, are vast basaltic plains formed by ancient volcanic eruptions that \\n" \n            "  filled large impact basins.\\n" \n            "* Thickness: The lunar crust varies in thickness. On the near side (facing Earth), it\'s estimated to be around 30-50 \\n" \n            "  kilometers thick. On the far side, it can be much thicker, possibly reaching up to 100 kilometers or more. This \\n" \n            "  asymmetry is a major characteristic of the Moon. The most compelling explanations for the Moon\'s crustal thickness \\n" \n            "  asymmetry point to a combination of factors related to its formation in Earth\\\'s intense thermal environment and a \\n" \n            "  massive early impact that shaped its internal heat distribution and subsequent geological evolution.\\n" \n            "* Surface Features: The crust is heavily cratered due to billions of years of impacts from asteroids and comets. Other \\n" \n            "  features include rilles (channels, often associated with lava flows), domes, and wrinkle ridges."\n)\n'),
    ('BR-moon_mantle_info', 'moon_mantle_info: 6 <br> -> \\n',
     b'moon_mantle_info = (\n            "Above the core lies the Moon\'s mantle, which makes up the bulk of its interior:<br>" \n            "* Composition: Primarily composed of silicate rocks, similar to Earth\'s mantle, but with different proportions of <br>" \n            "  elements. It\'s thought to be rich in olivine and pyroxene.<br>" \n            "* State: The Moon\'s mantle is largely solid today. However, in its early history, it would have been at least partially <br>" \n            "  molten, leading to volcanic activity that formed the vast maria (dark plains) on the lunar surface.<br>" \n            "* Lunar Deep Moonquakes: Seismometers left by Apollo missions detected \\"deep moonquakes\\" originating in the mantle at <br>" \n            "  depths of 700 to 1,200 km (435-745 miles). These are likely caused by tidal stresses from Earth."\n)\n',
     b'moon_mantle_info = (\n            "Above the core lies the Moon\'s mantle, which makes up the bulk of its interior:\\n" \n            "* Composition: Primarily composed of silicate rocks, similar to Earth\'s mantle, but with different proportions of \\n" \n            "  elements. It\'s thought to be rich in olivine and pyroxene.\\n" \n            "* State: The Moon\'s mantle is largely solid today. However, in its early history, it would have been at least partially \\n" \n            "  molten, leading to volcanic activity that formed the vast maria (dark plains) on the lunar surface.\\n" \n            "* Lunar Deep Moonquakes: Seismometers left by Apollo missions detected \\"deep moonquakes\\" originating in the mantle at \\n" \n            "  depths of 700 to 1,200 km (435-745 miles). These are likely caused by tidal stresses from Earth."\n)\n'),
    ('BR-moon_outer_core_info', 'moon_outer_core_info: 1 <br> -> \\n',
     b'moon_outer_core_info = (\n            "Outer Core: Surrounding the inner core, this is thought to be a liquid, iron-rich outer core with a radius of about <br>" \n            "330 kilometers. There might also be a small, partially molten layer of silicates around the outer core."\n)\n',
     b'moon_outer_core_info = (\n            "Outer Core: Surrounding the inner core, this is thought to be a liquid, iron-rich outer core with a radius of about \\n" \n            "330 kilometers. There might also be a small, partially molten layer of silicates around the outer core."\n)\n'),
    ('BR-moon_inner_core_info', 'moon_inner_core_info: 1 <br> -> \\n',
     b'moon_inner_core_info = (\n            "The Moon has a small, partially molten core. Seismic data from Apollo missions and more recent studies of the Moon\\\'s wobble suggest:<br>" \n            "* Inner Core: Believed to be a solid, iron-rich core, roughly 240 kilometers in radius."\n)\n',
     b'moon_inner_core_info = (\n            "The Moon has a small, partially molten core. Seismic data from Apollo missions and more recent studies of the Moon\\\'s wobble suggest:\\n" \n            "* Inner Core: Believed to be a solid, iron-rich core, roughly 240 kilometers in radius."\n)\n'),
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
