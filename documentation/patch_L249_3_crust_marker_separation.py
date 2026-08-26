r'''
patch_L249_3_crust_marker_separation.py -- L-249, patch 3.

Separates Earth's crust info marker from the upper mantle's, which
coincide after patch 2 moved the upper mantle to its sourced radius.

WHY. Every sphere shell puts one cross at its north pole, at r * 1.05.
That works while shells are separated by their radii. The upper mantle
now draws at 0.9950555 of the surface, so the two markers sit 0.49%
apart -- about 31 km at Earth scale, roughly two pixels on an
interior-only view. Plotly renders one cross where the user expects two.
The geometry is right, the legend is right, and the affordance silently
does not exist. Confirmed by Mode 5, 2026-08-26: Tony saw one cross.

WHAT CHANGES.

1. orrery_rendering.py -- build_sphere_shell() learns an optional
   `info_polar_deg` config key. Absent or zero, the marker sits at the
   pole exactly as before, so no existing shell in any body moves. Set,
   the marker steps that many degrees of polar angle along the +x
   meridian AT ITS OWN RADIUS. Angular separation, never radial: moving
   a marker off its shell's radius detaches it from the thing it labels.

2. shell_configs.py -- Earth's crust carries `'info_polar_deg': 10.0`.

WHY THE CRUST AND NOT THE MANTLE. The standing rule in
orrery-coding-conventions says the inner shell keeps the pole and outer
shells step. Tony's Mode 5 call the same day was to move the crust,
because it is the odd layer visually -- the only mesh3d surface in the
interior stack. Rule and eye agree, which is the comfortable case.

WHY 10 AND NOT 20. The recorded figure is 20 degrees, earned on the
solar skin stack where the family renders across a 0-3 R_sun view. Ten
degrees puts Earth's crust cross about 0.18 R from the upper mantle's,
roughly 1,150 km, which is 8-9% of the frame width on an interior-only
view. Tony's ruling, 2026-08-26: the convention becomes the OUTCOME
rather than the number -- step far enough to read as separate at the
scale the family actually renders at -- with 20 for the solar stack and
10 for Earth's interior as the two worked cases. That amendment belongs
in the skill and is NOT in this patch.

A DECLARED DRAWING PARAMETER, deliberately. Under L-240, info_polar_deg
is a drawing choice, not a measurement, so it lives in shell_configs.py
beside n_points and marker_size and does NOT go to constants_new.py.
The single-store rule confirmed 2026-08-26 governs measured values.

WHAT THIS PATCH DOES NOT VERIFY. That the markers now read as two on
screen. A patch can assert the key is present and the code path exists;
only the render can say whether it worked. Mode 5 after running it.

RUN COMMAND (save this file into the repo root -- the same folder as
orrery_rendering.py and shell_configs.py -- open it in VS Code and click
Run, or from a terminal in that folder):

    python patch_L249_3_crust_marker_separation.py

Success prints one `ok` line per edit then `patch applied`. Any failure
prints a single ERROR:/ANCHOR FAIL line and writes nothing to either
file. One-shot: a second run aborts on the fingerprint.

RUN ORDER: after patch_L249_2. Afterwards open the orrery, enable
Earth's Upper Mantle and Crust, and look at the north pole.

PERMANENT: the edits to both files.
DISPOSABLE: this script. Archive it to documentation/ once it has run.
'''

import hashlib
import os
import sys

RENDER = 'orrery_rendering.py'
CONFIGS = 'shell_configs.py'

# md5 of the LF-normalised bases, orrery e858c235d4cf324b17ef19b69ec984fba65689cb
BASE_FP = {
    RENDER: 'a12c096ec620f0ed447506611f9c95dc',
    CONFIGS: '02c8ab7dcefe185054d8e95fb60c2080',
}


def b(text):
    return text.encode('ascii')


IMPORT_OLD = b(r'''import numpy as np
import plotly.graph_objs as go''')

IMPORT_NEW = b(r'''import math
import numpy as np
import plotly.graph_objs as go''')

MARKER_OLD = b(r'''    r_info = radius_au * 1.05
    # Optional per-shell info-marker overrides. Dense-red shells set
    # 'info_fill' (e.g. 'white') so the cross reads against the red dot field;
    # the shell fill itself is unchanged. See handoff v14 / docstring above.
    # Absent keys -> factory defaults (shell-color fill, red border).
    info_trace = create_info_marker(
        center_x, center_y, center_z + r_info,''')

MARKER_NEW = b(r'''    r_info = radius_au * 1.05

    # Marker Separation for Near-Equal Radii (L-249, 2026-08-26).
    # Two shells within about 10% of each other put their crosses in the
    # same place at the pole, and Plotly draws one where the user expects
    # two -- geometry correct, legend correct, affordance silently absent.
    # A shell may declare 'info_polar_deg' to step that many degrees of
    # polar angle along the +x meridian, AT ITS OWN RADIUS. Angular, never
    # radial: a marker moved off its shell's radius stops labelling it.
    # Absent or zero reproduces the pole exactly, so no existing shell in
    # any body moves. How far to step is an outcome, not a fixed number --
    # far enough to read as separate at the scale the family renders at.
    # Worked cases: 20 degrees for the solar skin stack (0-3 R_sun view),
    # 10 for Earth's crust against the upper mantle (interior-only view).
    info_polar_deg = config.get('info_polar_deg', 0.0)
    if info_polar_deg:
        polar = math.radians(info_polar_deg)
        info_x = center_x + r_info * math.sin(polar)
        info_z = center_z + r_info * math.cos(polar)
    else:
        info_x = center_x
        info_z = center_z + r_info

    # Optional per-shell info-marker overrides. Dense-red shells set
    # 'info_fill' (e.g. 'white') so the cross reads against the red dot field;
    # the shell fill itself is unchanged. See handoff v14 / docstring above.
    # Absent keys -> factory defaults (shell-color fill, red border).
    info_trace = create_info_marker(
        info_x, center_y, info_z,''')

DOCSTRING_OLD = b(r'''        geometry_type     str    'scatter3d' (default, dot sphere) or
                                 'mesh3d' (triangulated solid surface)
        mesh_resolution   int    UV sphere resolution for mesh3d (default 24)''')

DOCSTRING_NEW = b(r'''        geometry_type     str    'scatter3d' (default, dot sphere) or
                                 'mesh3d' (triangulated solid surface)
        mesh_resolution   int    UV sphere resolution for mesh3d (default 24)
        info_polar_deg    float  polar-angle step for the info marker, in
                                 degrees along the +x meridian at the
                                 shell's own radius. Default 0 = north
                                 pole, unchanged. Set it only where two
                                 shells sit within ~10% of each other and
                                 their crosses would coincide.''')

CRUST_OLD = b(r"""            'color': 'rgb(70, 120, 160)',
            'opacity': 1.0,
            'geometry_type': 'mesh3d',
            'mesh_resolution': 24,""")

CRUST_NEW = b(r"""            'color': 'rgb(70, 120, 160)',
            'opacity': 1.0,
            'geometry_type': 'mesh3d',
            'mesh_resolution': 24,
            # L-249: the upper mantle draws at 0.9950555 of the surface, so
            # its cross and this one land 0.49% apart -- about 31 km, two
            # pixels, one visible marker. Stepping this one 10 degrees puts
            # them ~0.18 R apart. DECLARED drawing parameter (L-240): a
            # choice about the picture, not a measurement, so it stays here
            # and not in constants_new.py. Tony's Mode 5 call, 2026-08-26:
            # move the crust, because it is the odd layer visually.
            'info_polar_deg': 10.0,""")

RENDER_DOC_OLD = b(r"""    builders (magnetospheres, rings, tori) DO use their own inline markers.
\"\"\"""".replace('\\"', '"'))

RENDER_DOC_NEW = b(r"""    builders (magnetospheres, rings, tori) DO use their own inline markers.
August 26, 2026 (L-249, Opus 5): build_sphere_shell() gains the optional
    info_polar_deg key. A shell whose radius sits within ~10% of its
    neighbour can step its info marker angularly instead of hiding under
    it. Default 0 reproduces the previous north-pole placement exactly,
    so no existing shell on any body moves.
\"\"\"""".replace('\\"', '"'))

CONFIGS_DOC_OLD = b(r'''    its hover carries a toggle-off note the body module's string does
    not have.)
"""''')

CONFIGS_DOC_NEW = b(r'''    its hover carries a toggle-off note the body module's string does
    not have.)
Module updated: August 26, 2026 with Anthropic's Claude Opus 5 (L-249:
    Earth's crust declares info_polar_deg 10.0 so its info marker clears
    the upper mantle's, which it coincided with once the upper mantle
    moved to its sourced radius. Found by Mode 5, not by any checker.)
"""''')


def fingerprint(data):
    return hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()


def load(name):
    if not os.path.exists(name):
        print('ERROR: %s not found. Save this script into the repo root, '
              'beside %s and %s.' % (name, RENDER, CONFIGS))
        return (None, None)
    with open(name, 'rb') as handle:
        data = handle.read()
    fp = fingerprint(data)
    if fp != BASE_FP[name]:
        print('ERROR: BASE MOVED. %s fingerprints %s, expected %s.'
              % (name, fp, BASE_FP[name]))
        print('       Nothing written to either file. If this patch already '
              'ran, that is the expected result of a second run.')
        return (None, None)
    is_crlf = data.count(b'\r\n') > 0
    print('ok   base fingerprint %s (%s, %d bytes, %s)'
          % (fp, name, len(data), 'CRLF' if is_crlf else 'LF'))
    return (data, is_crlf)


def apply_edits(data, is_crlf, edits):
    for label, old, new in edits:
        if is_crlf:
            old = old.replace(b'\n', b'\r\n')
            new = new.replace(b'\n', b'\r\n')
        count = data.count(old)
        if count != 1:
            print('ANCHOR FAIL: %s -- expected 1 match, got %d: %r'
                  % (label, count, old[:70]))
            print('             Nothing written to either file.')
            return None
        data = data.replace(old, new, 1)
        print('ok   %s' % label)
    return data


def main():
    render, r_crlf = load(RENDER)
    if render is None:
        return 1
    configs, c_crlf = load(CONFIGS)
    if configs is None:
        return 1

    render = apply_edits(render, r_crlf, [
        ('rendering docstring stamp', RENDER_DOC_OLD, RENDER_DOC_NEW),
        ('math import', IMPORT_OLD, IMPORT_NEW),
        ('build_sphere_shell parameter docs', DOCSTRING_OLD, DOCSTRING_NEW),
        ('info marker polar placement', MARKER_OLD, MARKER_NEW),
    ])
    if render is None:
        return 1

    configs = apply_edits(configs, c_crlf, [
        ('configs docstring stamp', CONFIGS_DOC_OLD, CONFIGS_DOC_NEW),
        ('Earth crust info_polar_deg', CRUST_OLD, CRUST_NEW),
    ])
    if configs is None:
        return 1

    for raw in (MARKER_NEW, CRUST_NEW, DOCSTRING_NEW,
                RENDER_DOC_NEW, CONFIGS_DOC_NEW):
        try:
            raw.decode('ascii')
        except UnicodeDecodeError as exc:
            print('ERROR: non-ASCII byte in inserted text: %s' % exc)
            return 1
    print('ok   encoding gate -- inserted lines are ASCII')

    r_text = render.decode('ascii').replace('\r\n', '\n')
    c_text = configs.decode('ascii').replace('\r\n', '\n')

    # The old unconditional placement must be GONE, not merely joined by a
    # new branch. If it survives, both paths exist and the marker never
    # moves -- the failure that looks exactly like success.
    if 'center_x, center_y, center_z + r_info,' in r_text:
        print('ERROR: post-condition -- the unconditional pole placement '
              'survives; the new branch would never be reached.')
        return 1
    if 'info_x, center_y, info_z,' not in r_text:
        print('ERROR: post-condition -- create_info_marker is not being '
              'called with the computed position.')
        return 1
    print('ok   post-condition -- the marker call uses the computed position')

    # Count MODULE-LEVEL imports only. A bare count('import math') is 2,
    # because rotate_to_sunward() has carried a function-local `import
    # math` since before this patch. That local import is now redundant
    # and is deliberately left alone: it is not a violation of any ruled
    # convention, and tidying it would edit a function this patch has no
    # business in.
    if r_text.count('\nimport math\n') != 1:
        print('ERROR: post-condition -- module-level `import math` appears '
              '%d times.' % r_text.count('\nimport math\n'))
        return 1
    if r_text.index('\nimport math\n') > r_text.index('def build_sphere_shell'):
        print('ERROR: post-condition -- math is imported after its use.')
        return 1
    print('ok   post-condition -- math imported at module level, before use')

    # The crust key must be Earth's, and must be a usable angle.
    earth_start = c_text.index("    'Earth': {")
    earth_end = c_text.index("'atmosphere': {", earth_start)
    earth = c_text[earth_start:earth_end]
    if "'info_polar_deg': " not in earth:
        print('ERROR: post-condition -- info_polar_deg did not land inside '
              'the Earth block.')
        return 1
    raw_value = earth.split("'info_polar_deg': ")[1].split(',')[0]
    try:
        angle = float(raw_value)
    except ValueError:
        print('ERROR: post-condition -- info_polar_deg is not a number: %r'
              % raw_value)
        return 1
    if not 0.0 < angle < 90.0:
        print('ERROR: post-condition -- info_polar_deg is %r; a zero would '
              'silently keep both crosses at the pole and 90 or more would '
              'put the marker on the equator.' % angle)
        return 1
    print('ok   post-condition -- Earth carries info_polar_deg = %g, inside '
          'the usable range' % angle)

    if c_text.count("'info_polar_deg'") != 1:
        print('ERROR: post-condition -- info_polar_deg appears %d times; '
              'exactly one shell should declare it.'
              % c_text.count("'info_polar_deg'"))
        return 1
    print('ok   post-condition -- exactly one shell declares it')

    with open(RENDER, 'wb') as handle:
        handle.write(render)
    with open(CONFIGS, 'wb') as handle:
        handle.write(configs)
    print('patch applied (%s %d bytes, %s %d bytes)'
          % (RENDER, len(render), CONFIGS, len(configs)))
    print('')
    print('Next: open the orrery, enable Earth Upper Mantle and Crust, and')
    print('look at the north pole. Two crosses, the crust\'s offset toward')
    print('+x. No other shell on any body should have moved.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
