# -*- coding: ascii -*-
"""patch_pluto_br_fix.py -- L-156 geometry corrections + <br> fix for pluto_visualization_shells.py

Built on 06a16df768a010205b7078630ac31bf0cd17f846
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

HOW TO RUN
    Save this file into the SAME FOLDER as pluto_visualization_shells.py, open it in
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

TARGET = 'pluto_visualization_shells.py'

# (edit_id, label, old_bytes, new_bytes) -- bottom-up by line number
EDITS = [
    ('BR-pluto_hill_sphere_info', 'pluto_hill_sphere_info: 7 <br> -> \\n',
     b'pluto_hill_sphere_info = (\n            "SELECT MANUAL SCALE OF AT LEAST 0.1 AU TO VISUALIZE.<br>" \n            "1.3 MB PER FRAME FOR HTML.<br><br>"\n\n            "Hill Sphere: Pluto\'s Hill sphere, or Roche sphere, is the region around it where its gravitational influence dominates <br>" \n            "over the Sun\'s. The radius of Pluto\'s Hill sphere is quite large, approximately 5.99 million kilometers (0.04 AU). This is <br>" \n            "significantly larger than Earth\'s Hill sphere in terms of volume. Any moon orbiting Pluto within this sphere is <br>" \n            "gravitationally bound to it. Pluto has five known moons: Charon, Styx, Nix, Kerberos, and Hydra, all of which reside within <br>" \n            "its Hill sphere."                     \n)\n',
     b'pluto_hill_sphere_info = (\n            "SELECT MANUAL SCALE OF AT LEAST 0.1 AU TO VISUALIZE.\\n" \n            "1.3 MB PER FRAME FOR HTML.\\n\\n"\n\n            "Hill Sphere: Pluto\'s Hill sphere, or Roche sphere, is the region around it where its gravitational influence dominates \\n" \n            "over the Sun\'s. The radius of Pluto\'s Hill sphere is quite large, approximately 5.99 million kilometers (0.04 AU). This is \\n" \n            "significantly larger than Earth\'s Hill sphere in terms of volume. Any moon orbiting Pluto within this sphere is \\n" \n            "gravitationally bound to it. Pluto has five known moons: Charon, Styx, Nix, Kerberos, and Hydra, all of which reside within \\n" \n            "its Hill sphere."                     \n)\n'),
    ('BR-pluto_atmosphere_info', 'pluto_atmosphere_info: 8 <br> -> \\n',
     b'pluto_atmosphere_info = (\n            "2.7 MB PER FRAME FOR HTML.<br><br>"\n            "Atmosphere: Pluto has a very thin atmosphere, about 1/100,000th the surface pressure of Earth\'s. It\'s primarily composed <br>" \n            "of nitrogen (N2), with smaller amounts of methane (CH4) and carbon monoxide (CO). This atmosphere is dynamic and changes <br>" \n            "with Pluto\'s orbit around the Sun. As Pluto moves farther away, the atmosphere freezes and falls to the surface as ice. <br>" \n            "When it\'s closer to the Sun, the surface ice sublimates, forming a gaseous atmosphere. The atmosphere contains layers of <br>" \n            "haze, extending up to 200 km above the surface, likely formed from the interaction of the atmospheric gases with high-energy <br>" \n            "radiation. Counterintuitively, Pluto\'s upper atmosphere is significantly warmer than its surface due to a temperature <br>" \n            "inversion, possibly caused by the presence of methane."\n)\n',
     b'pluto_atmosphere_info = (\n            "2.7 MB PER FRAME FOR HTML.\\n\\n"\n            "Atmosphere: Pluto has a very thin atmosphere, about 1/100,000th the surface pressure of Earth\'s. It\'s primarily composed \\n" \n            "of nitrogen (N2), with smaller amounts of methane (CH4) and carbon monoxide (CO). This atmosphere is dynamic and changes \\n" \n            "with Pluto\'s orbit around the Sun. As Pluto moves farther away, the atmosphere freezes and falls to the surface as ice. \\n" \n            "When it\'s closer to the Sun, the surface ice sublimates, forming a gaseous atmosphere. The atmosphere contains layers of \\n" \n            "haze, extending up to 200 km above the surface, likely formed from the interaction of the atmospheric gases with high-energy \\n" \n            "radiation. Counterintuitively, Pluto\'s upper atmosphere is significantly warmer than its surface due to a temperature \\n" \n            "inversion, possibly caused by the presence of methane."\n)\n'),
    ('BR-pluto_haze_layer_info', 'pluto_haze_layer_info: 8 <br> -> \\n',
     b'pluto_haze_layer_info = (\n            "2.7 MB PER FRAME FOR HTML.<br><br>"\n            "Atmosphere: Pluto has a very thin atmosphere, about 1/100,000th the surface pressure of Earth\'s. It\'s primarily composed <br>" \n            "of nitrogen (N2), with smaller amounts of methane (CH4) and carbon monoxide (CO). This atmosphere is dynamic and changes <br>" \n            "with Pluto\'s orbit around the Sun. As Pluto moves farther away, the atmosphere freezes and falls to the surface as ice. <br>" \n            "When it\'s closer to the Sun, the surface ice sublimates, forming a gaseous atmosphere. The atmosphere contains layers of <br>" \n            "haze, extending up to 200 km above the surface, likely formed from the interaction of the atmospheric gases with high-energy <br>" \n            "radiation. Counterintuitively, Pluto\'s upper atmosphere is significantly warmer than its surface due to a temperature <br>" \n            "inversion, possibly caused by the presence of methane."\n)\n',
     b'pluto_haze_layer_info = (\n            "2.7 MB PER FRAME FOR HTML.\\n\\n"\n            "Atmosphere: Pluto has a very thin atmosphere, about 1/100,000th the surface pressure of Earth\'s. It\'s primarily composed \\n" \n            "of nitrogen (N2), with smaller amounts of methane (CH4) and carbon monoxide (CO). This atmosphere is dynamic and changes \\n" \n            "with Pluto\'s orbit around the Sun. As Pluto moves farther away, the atmosphere freezes and falls to the surface as ice. \\n" \n            "When it\'s closer to the Sun, the surface ice sublimates, forming a gaseous atmosphere. The atmosphere contains layers of \\n" \n            "haze, extending up to 200 km above the surface, likely formed from the interaction of the atmospheric gases with high-energy \\n" \n            "radiation. Counterintuitively, Pluto\'s upper atmosphere is significantly warmer than its surface due to a temperature \\n" \n            "inversion, possibly caused by the presence of methane."\n)\n'),
    ('BR-pluto_crust_info', 'pluto_crust_info: 5 <br> -> \\n',
     b'pluto_crust_info = (\n            "USE MANUAL SCALED OF 0.005 AU TO VIEW CLOSELY."\n            "4.6 MB PER FRAME FOR HTML.<br><br>"\n            "Crust (Surface Layer): This is the outermost layer, composed of more volatile ices: primarily nitrogen ice, with smaller<br>" \n            "amounts of methane and carbon monoxide ice. The thickness of this layer likely varies but is estimated to be relatively <br>" \n            "thin in many regions, perhaps ranging from a few to tens of kilometers. In the deep Sputnik Planitia basin, the nitrogen <br>" \n            "ice layer is estimated to be several kilometers thick and overlies the water-ice lithosphere."\n)\n',
     b'pluto_crust_info = (\n            "USE MANUAL SCALED OF 0.005 AU TO VIEW CLOSELY."\n            "4.6 MB PER FRAME FOR HTML.\\n\\n"\n            "Crust (Surface Layer): This is the outermost layer, composed of more volatile ices: primarily nitrogen ice, with smaller\\n" \n            "amounts of methane and carbon monoxide ice. The thickness of this layer likely varies but is estimated to be relatively \\n" \n            "thin in many regions, perhaps ranging from a few to tens of kilometers. In the deep Sputnik Planitia basin, the nitrogen \\n" \n            "ice layer is estimated to be several kilometers thick and overlies the water-ice lithosphere."\n)\n'),
    ('BR-pluto_mantle_info', 'pluto_mantle_info: 4 <br> -> \\n',
     b'pluto_mantle_info = (\n            "2.1 MB PER FRAME FOR HTML.<br><br>"\n            "Mantle: Surrounding the rocky core is a mantle made of water ice. There\'s a compelling theory that a subsurface ocean <br>" \n            "of liquid water, possibly mixed with ammonia, exists at the boundary between the core and the ice mantle. This ocean <br>" \n            "could be 100 to 180 km thick. The presence of this ocean is supported by geological features observed on Pluto\'s surface."\n)\n',
     b'pluto_mantle_info = (\n            "2.1 MB PER FRAME FOR HTML.\\n\\n"\n            "Mantle: Surrounding the rocky core is a mantle made of water ice. There\'s a compelling theory that a subsurface ocean \\n" \n            "of liquid water, possibly mixed with ammonia, exists at the boundary between the core and the ice mantle. This ocean \\n" \n            "could be 100 to 180 km thick. The presence of this ocean is supported by geological features observed on Pluto\'s surface."\n)\n'),
    ('BR-pluto_core_info', 'pluto_core_info: 4 <br> -> \\n',
     b'pluto_core_info = (\n            "2.4 MB PER FRAME FOR HTML.<br><br>"\n            "Pluto core: Scientists believe Pluto has a dense, rocky core, likely composed of silicates and iron. The core\'s diameter <br>" \n            "is hypothesized to be about 1700 km, which is approximately 70% of Pluto\'s total diameter. Heat generated from the decay <br>" \n            "of radioactive elements within the core may still be present today."\n)\n',
     b'pluto_core_info = (\n            "2.4 MB PER FRAME FOR HTML.\\n\\n"\n            "Pluto core: Scientists believe Pluto has a dense, rocky core, likely composed of silicates and iron. The core\'s diameter \\n" \n            "is hypothesized to be about 1700 km, which is approximately 70% of Pluto\'s total diameter. Heat generated from the decay \\n" \n            "of radioactive elements within the core may still be present today."\n)\n'),
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
