"""patch_L229_1_streamer_band_frame.py

Built on 851224c6a52e6a9f56140ce421050a8bb59b96b4 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Gallery at 8ec4f261013f09697d649efd25c8a746bffeff64.
Both confirmed by live git ls-remote.
Written August 23, 2026 with Anthropic's Claude Opus 5.

RUN IT LIKE THIS
    Save into the REPO ROOT -- the folder holding
    solar_visualization_shells.py and LEDGER_CONSOLIDATED.md.
    Open in VS Code, click Run.

Transactional, all-or-nothing, binary I/O, two targets.

WHAT IT FIXES -- found by Mode 5, 2026-08-23

Tony looked at the render and asked whether the streamer belt should lie
in the ecliptic plane rather than the solar equatorial plane. It should
not, and the same figure already contained the proof.

  1. THE BAND WAS DRAWN IN THE WRONG PLANE.
     `create_streamer_band_shape` returns points whose own docstring says
     "Positions in SOLAR RADII in the body frame." The caller scaled them
     and handed them to Plotly with no rotation, so the band's plane of
     symmetry landed on the ECLIPTIC.

     Meanwhile `build_rotation_axis_traces` -- the yellow axis in the
     same figure -- takes its spin pole from
     `create_planet_transformation_matrix('Sun')`, which reads
     `planet_poles['Sun'] = {'ra': 286.13, 'dec': 63.87}` (IAU 2018). It
     is correctly tilted. Two traces in one plot disagreed about where
     the Sun's equator is, and the axis leaned while the band lay flat.

     MEASURED, before and after, by fitting the point cloud's plane:
       before   normal (-0.0003, -0.0004, 1.0000), tilt 0.03 deg
       after    normal ( 0.1227, -0.0314, 0.9920), tilt 7.27 deg
       angle between the band's normal and the Sun's spin pole: 0.028 deg
     The expected inclination of the solar equator to the ecliptic is
     7.25 deg. The band and the axis now derive from ONE matrix, so they
     cannot disagree again.

     The physics: the streamer belt follows the heliospheric current
     sheet, which tracks the solar MAGNETIC equator. Near solar minimum
     the dipole lies close to the spin axis, so the magnetic equator
     tracks the ROTATION equator. This module already commits to that
     regime -- `warp_amp_deg: 15.0` is described as the neutral line's
     tilt off the equator, and the hover says the warp is drawn in one
     configuration near solar minimum. So the band is "equator plus
     warp", and it was warping around the wrong equator. The magnetic
     equator is not exactly the rotation equator even at minimum; the
     ecliptic has no claim on it at all.

  2. THE INFO MARKER IS ROTATED WITH IT.
     The marker is placed in the same body-frame spherical coordinates.
     Rotating the band and not the marker would leave the marker
     floating off the band edge -- geometry right, affordance wrong.
     Verified unchanged: marker to nearest band point is 2.038e-03 AU
     before and after.

  3. A CITATION THE RE-FLOW PUSHED OUT OF REACH (L-227 follow-on).
     The provenance scanner decides whether a claim is cited by how many
     LINES away the nearest `# Source:` comment is. Re-flowing the hover
     yesterday moved one line past that window, and the tree count went
     292 -> 294. The number was never uncited: it is COMPUTED from
     ALFVEN_SURFACE_RADII, which carries its own source.

     MEASURED on a live scanner run, not reasoned about:
       solar_visualization_shells.py Tier-1  7 -> 6
     The first attempt used `# Derived:` and did NOT clear it -- that
     token belongs to the worksheet leg vocabulary, not to the scanner's
     SOURCE_PATTERNS. `# Source:` is what the scanner accepts. Recorded
     because the two vocabularies overlap enough to mislead.

WHAT IT DOES NOT DO
  It does not touch `warp_amp_deg`, the warp lobes, or any drawn value.
  Only the frame changes.

WHAT IS PERMANENT AND WHAT IS NOT
  The script is disposable. The rotation and the citation are not.

AFTER RUNNING
  1. python ledger_index.py
  2. Maintenance suite. Expect 11 of 11, and the provenance scanner to
     drop by one in this file.
  3. Commit and push.
  4. Move this script to documentation/.

  MODE 5, and it is the gate: relaunch and look at the Sun. The band
  should now lean with the yellow rotation axis instead of lying flat
  against the ecliptic grid. In the +X view the tilt is about 7 degrees
  -- visible, not dramatic. If the band and the axis still disagree,
  say so and do not push.
"""

import hashlib
import os
import sys

BASE_SHA = '851224c6a52e6a9f56140ce421050a8bb59b96b4'
GALLERY_SHA = '8ec4f261013f09697d649efd25c8a746bffeff64'
MODEL = "Anthropic's Claude Opus 5"

HERE = os.path.dirname(os.path.abspath(__file__))
MODULE = 'solar_visualization_shells.py'
LEDGER = 'LEDGER_CONSOLIDATED.md'

FINGERPRINTS = {
    MODULE: '2d6d52ea3573aa9f505bf90bc7d6a35e',
    LEDGER: '1a518fd0d5c8f7440050e6f85175f85b',
}


# ==================================================================
# EDIT 1 -- body frame to ecliptic
# ==================================================================

OLD_1 = '''    xs, ys, zs, alphas, sizes = create_streamer_band_shape(params)

    scale = SOLAR_RADIUS_AU
    x_au = [v * scale for v in xs]
    y_au = [v * scale for v in ys]
    z_au = [v * scale for v in zs]
'''

NEW_1 = '''    xs, ys, zs, alphas, sizes = create_streamer_band_shape(params)

    # BODY FRAME -> ECLIPTIC. create_streamer_band_shape returns points in
    # the SUN'S frame, so the band's plane of symmetry is the solar
    # equator -- inclined about 7.25 deg to the ecliptic. Until 2026-08-23
    # these points were scaled and handed to Plotly UNROTATED, which laid
    # the band flat in the ecliptic while the Sun's rotation axis trace,
    # built from the very matrix used here, was correctly tilted. Two
    # traces in one figure disagreeing about where the Sun's equator is.
    # Found by Mode 5, not by any check (L-229).
    # Source: IAU 2018 solar pole, via idealized_orbits.planet_poles['Sun']
    #   (ra 286.13, dec 63.87) -- the SAME source build_rotation_axis_traces
    #   reads, so the band and the axis now derive from one matrix and
    #   cannot drift apart again.
    # The import is lazy for the same reason it is lazy in
    #   build_rotation_axis_traces: idealized_orbits is heavy.
    from idealized_orbits import create_planet_transformation_matrix

    M = np.asarray(create_planet_transformation_matrix('Sun'), dtype=float)

    def _to_ecliptic(bx, by, bz):
        """Rotate one body-frame point into ecliptic coordinates."""
        v = M @ np.array([bx, by, bz], dtype=float)
        return float(v[0]), float(v[1]), float(v[2])

    rot = M @ np.vstack([np.asarray(xs, dtype=float),
                         np.asarray(ys, dtype=float),
                         np.asarray(zs, dtype=float)])

    scale = SOLAR_RADIUS_AU
    x_au = (rot[0] * scale).tolist()
    y_au = (rot[1] * scale).tolist()
    z_au = (rot[2] * scale).tolist()
'''


# ==================================================================
# EDIT 2 -- the info marker rides with the band
# ==================================================================

OLD_2 = '''    r_i = cusp_rs * SOLAR_RADIUS_AU * 1.02
    info_trace = create_info_marker(
        r_i * math.cos(lat_i) * math.cos(lon_i),
        r_i * math.cos(lat_i) * math.sin(lon_i),
        r_i * math.sin(lat_i),
'''

NEW_2 = '''    r_i = cusp_rs * SOLAR_RADIUS_AU * 1.02
    # The marker is placed in the SAME body frame as the band and rotated
    # with it. Rotating one and not the other would leave the marker
    # floating off the band edge: the geometry would be right and the
    # affordance would be wrong, which is the harder kind of bug to see.
    mx, my, mz = _to_ecliptic(r_i * math.cos(lat_i) * math.cos(lon_i),
                              r_i * math.cos(lat_i) * math.sin(lon_i),
                              r_i * math.sin(lat_i))
    info_trace = create_info_marker(
        mx, my, mz,
'''


# ==================================================================
# EDIT 3 -- put the computed figures back inside a citation window
# ==================================================================

OLD_3 = ('        f"past the Alfven surface at {fade_rs:.1f} R_sun<br>"\n'
         '        f"({fade_km:,.0f} km, {fade_au:.6f} AU), where the corona becomes<br>"\n')
NEW_3 = ('        f"past the Alfven surface at {fade_rs:.1f} R_sun<br>"\n'
         '        # Source: constants_new.py ALFVEN_SURFACE_RADII -- the km and AU\n'
         '        #   figures on the next line are COMPUTED from it, not typed, so\n'
         '        #   this line restates a cited constant rather than making an\n'
         '        #   independent claim. See the Source+ leg on that constant\n'
         '        #   (L-209). The comment sits HERE, mid-string, because the\n'
         '        #   scanner judges citation by line distance and the L-227\n'
         '        #   re-flow moved this line out of the window (L-229).\n'
         '        f"({fade_km:,.0f} km, {fade_au:.6f} AU), where the corona becomes<br>"\n')


# ==================================================================
# EDIT 4 -- L-229
# ==================================================================

OLD_4 = (
    "\n"
    "## PENDING ACTION (Tony-side)\n"
)
NEW_4 = (
    "\n"
    "#### [L-229] Streamer band drawn in the ecliptic plane, not the solar "
    "equator\n"
    "<!-- L:229 status:OPEN upd:2026-08-23 section:A flag: rice:3/4/95/1 -->\n"
    "- **Found by Mode 5 on 2026-08-23.** Tony looked at the render and\n"
    "  asked whether the belt should lie in the ecliptic rather than the\n"
    "  solar equatorial plane. It should not, and the same figure already\n"
    "  carried the proof.\n"
    "- **The defect.** `create_streamer_band_shape` returns points whose own\n"
    "  docstring says \"Positions in SOLAR RADII in the body frame.\" The\n"
    "  caller scaled them and handed them to Plotly with NO rotation, so\n"
    "  the band's plane of symmetry landed on the ecliptic. Meanwhile\n"
    "  `build_rotation_axis_traces` takes the Sun's spin pole from\n"
    "  `create_planet_transformation_matrix('Sun')` and is correctly\n"
    "  tilted. The axis leaned; the band lay flat.\n"
    "- **Measured, by fitting the point cloud's plane:** before, normal\n"
    "  (-0.0003, -0.0004, 1.0000), tilt 0.03 deg from the ecliptic; after,\n"
    "  normal (0.1227, -0.0314, 0.9920), tilt 7.27 deg. Angle between the\n"
    "  band normal and the Sun's spin pole after the fix: 0.028 deg. The\n"
    "  solar equator is inclined 7.25 deg to the ecliptic.\n"
    "- **Both traces now read ONE matrix**, so they cannot disagree again.\n"
    "  That is the structural half of the fix and it matters more than the\n"
    "  seven degrees.\n"
    "- **Why the solar equator is the right plane.** The streamer belt\n"
    "  follows the heliospheric current sheet, which tracks the solar\n"
    "  MAGNETIC equator. Near solar minimum the dipole lies close to the\n"
    "  spin axis, so the magnetic equator tracks the rotation equator, and\n"
    "  this module already commits to that regime: `warp_amp_deg` is the\n"
    "  neutral line's tilt OFF THE EQUATOR and the hover says the warp is\n"
    "  one configuration near solar minimum. The band is \"equator plus\n"
    "  warp\" and it was warping around the wrong equator. Honest caveat:\n"
    "  the magnetic equator is not exactly the rotation equator even at\n"
    "  minimum. The ecliptic has no claim on it at all.\n"
    "- **The info marker rotates with the band.** Rotating one and not the\n"
    "  other would leave the marker off the band edge -- geometry right,\n"
    "  affordance wrong. Verified unchanged at 2.038e-03 AU to the nearest\n"
    "  band point, before and after.\n"
    "- **Nothing automated could have caught this.** The module compiles,\n"
    "  the trace builds, the geometry is internally consistent, and no\n"
    "  checker compares two traces' frames. Fourth instance this month of\n"
    "  the render being the only gate: L-227 (hover width), L-224 (band\n"
    "  shape), L-209 (shell radius), and now the frame.\n"
    "- **Also fixed here (L-227 follow-on):** the L-227 re-flow moved a\n"
    "  computed figure out of the scanner's citation window, taking the\n"
    "  tree count 292 -> 294. A `# Source:` comment now sits mid-string\n"
    "  above that line. Measured on a live scanner run: this file's Tier-1\n"
    "  count 7 -> 6. The first attempt used `# Derived:` and did NOT clear\n"
    "  it -- that token is worksheet-leg vocabulary, not scanner\n"
    "  `SOURCE_PATTERNS`. The two overlap enough to mislead.\n"
    "- **Note:** RICE 3/4/95/1 -> 11.4 is Claude's proposed score. Impact 4\n"
    "  because a wrong frame is a wrong physical claim on screen, not a\n"
    "  cosmetic one. **Tony-action (decide):** confirm or redirect, then\n"
    "  re-run `ledger_index.py`.\n"
    "- **Tony-action (do): Mode 5.** Relaunch and look at the Sun. The band\n"
    "  should lean with the yellow rotation axis instead of lying flat on\n"
    "  the ecliptic grid -- about 7 degrees, visible but not dramatic.\n"
    "- **Ref:** `solar_visualization_shells.py::create_sun_streamer_band`;\n"
    "  `planet_visualization_utilities.py::create_streamer_band_shape` and\n"
    "  `build_rotation_axis_traces`;\n"
    "  `idealized_orbits.py::create_planet_transformation_matrix` and\n"
    "  `planet_poles['Sun']` (IAU 2018); L-224 (the band build); L-227 (the\n"
    "  re-flow); L-209 (the Alfven constant this cites).\n"
    "\n"
    "## PENDING ACTION (Tony-side)\n"
)


# ==================================================================
# EDIT 5 -- L-227 gains the coupling it taught us
# ==================================================================

OLD_5 = (
    "  Third demonstration this month that the render is the gate.\n"
)
NEW_5 = (
    "  Third demonstration this month that the render is the gate.\n"
    "- **A RE-FLOW IS NOT COSMETIC IN THIS PROJECT** (learned 2026-08-23,\n"
    "  after this item shipped). The provenance scanner decides whether a\n"
    "  claim is cited by how many LINES away the nearest `# Source:`\n"
    "  comment is. Breaking one long line into six moved a computed figure\n"
    "  past that window, and the tree count went 292 -> 294 on a change\n"
    "  that altered no wording at all. Fixed under L-229. The general\n"
    "  form: when line positions move, provenance state can move with\n"
    "  them, so re-run the scanner after any re-flow and read the delta.\n"
)


# ==================================================================
# EDIT 6 -- ledger currency stamp
# ==================================================================

OLD_6 = (
    "Module updated: August 23, 2026 with Anthropic's Claude Opus 5 (L-227\n"
    "hover wrap + orrery-coding-conventions 1.5; L-228 Alfven ranges),\n"
    "built on 15741822.\n"
)
NEW_6 = (
    "Module updated: August 23, 2026 with Anthropic's Claude Opus 5 (L-227\n"
    "hover wrap + orrery-coding-conventions 1.5; L-228 Alfven ranges),\n"
    "built on 15741822.\n"
    "Module updated: August 23, 2026 with Anthropic's Claude Opus 5 (L-229:\n"
    "streamer band rotated into the solar equatorial frame; the L-227\n"
    "citation-window follow-on), built on 851224c6.\n"
)


EDITS = [
    (MODULE, '1 band: body frame -> ecliptic', OLD_1, NEW_1),
    (MODULE, '2 info marker rides with the band', OLD_2, NEW_2),
    (MODULE, '3 citation back inside the scanner window', OLD_3, NEW_3),
    (LEDGER, '4 L-229 opened', OLD_4, NEW_4),
    (LEDGER, '5 L-227 gains the re-flow coupling', OLD_5, NEW_5),
    (LEDGER, '6 ledger currency stamp', OLD_6, NEW_6),
]

TARGETS = [MODULE, LEDGER]


def fail(message):
    print('')
    print('ERROR: ' + message)
    print('Nothing was written. BOTH files on disk are untouched.')
    sys.exit(1)


def main():
    print('patch_L229_1_streamer_band_frame.py')
    print('built on %s' % BASE_SHA)
    print('')

    paths, originals, endings = {}, {}, {}
    for name in TARGETS:
        path = os.path.join(HERE, name)
        if not os.path.exists(path):
            fail('%s not found beside this script.\n'
                 '       This one goes in the REPO ROOT.\n'
                 '       It looked in: %s' % (name, HERE))
        paths[name] = path
        with open(path, 'rb') as handle:
            originals[name] = handle.read()

    for name in TARGETS:
        normalized = originals[name].replace(b'\r\n', b'\n')
        got = hashlib.md5(normalized).hexdigest()
        if got != FINGERPRINTS[name]:
            fail('BASE MOVED. %s fingerprints %s; this patch was built '
                 'against %s. Re-pull at HEAD, or ask for a rebuilt patch.'
                 % (name, got, FINGERPRINTS[name]))
        endings[name] = b'\r\n' if b'\r\n' in originals[name] else b'\n'
        print('[base ok]       %-32s %s (%s)'
              % (name, got, 'CRLF' if endings[name] == b'\r\n' else 'LF'))

    for _name, label, old, new in EDITS:
        if sum(1 for ch in new if ord(ch) > 127) > \
                sum(1 for ch in old if ord(ch) > 127):
            fail('edit %s would INTRODUCE a non-ASCII character.' % label)
    with open(os.path.abspath(__file__), 'rb') as handle:
        own = handle.read()
    if any(byte > 127 for byte in own):
        fail('this script itself is not pure ASCII.')
    print('[ascii ok]      no edit introduces non-ASCII; script is ASCII '
          '(%d bytes)' % len(own))

    working = {n: originals[n].replace(b'\r\n', b'\n').decode('utf-8')
               for n in TARGETS}

    if '<!-- L:229 ' in working[LEDGER]:
        fail('L-229 already has an index comment; this would duplicate it.')
    print('[handle ok]     L-229 is absent, as expected')

    for name, label, old, new in EDITS:
        count = working[name].count(old)
        if count != 1:
            fail('ANCHOR FAIL on edit %s -- expected exactly 1 match, found '
                 '%d. First 70 chars: %r' % (label, count, old[:70]))
        working[name] = working[name].replace(old, new, 1)
        print('[ok]            %s' % label)

    for name in TARGETS:
        allowed = set()
        for n, _label, old, new in EDITS:
            if n != name:
                continue
            allowed.update(l for l in
                           (set(old.split('\n')) - set(new.split('\n'))) if l)
        after = set(working[name].split('\n'))
        before = originals[name].replace(b'\r\n', b'\n').decode('utf-8')
        lost = [l for l in before.split('\n') if l and l not in after]
        unexpected = [l for l in lost if l not in allowed]
        if unexpected:
            fail('%d line(s) of %s would be lost that no edit claims to '
                 'rewrite. First: %r'
                 % (len(unexpected), name, unexpected[0]))
        print('[addition ok]   %-32s %d line(s) rewritten'
              % (name, len(lost)))

    # --- Evidence the intended change is the change made -------------
    m = working[MODULE]
    if 'create_planet_transformation_matrix' not in m:
        fail('the transformation matrix import did not land.')
    if 'x_au = [v * scale for v in xs]' in m:
        fail('the unrotated scaling survives -- the band would still be '
             'drawn in the ecliptic plane.')
    if 'mx, my, mz' not in m:
        fail('the info marker was not rotated with the band.')
    if m.count('# Source: constants_new.py ALFVEN_SURFACE_RADII') != 1:
        fail('the citation comment did not land exactly once.')
    print('[intent ok]     rotation wired, flat scaling gone, marker '
          'rotated, citation placed')

    import ast
    try:
        ast.parse(working[MODULE], filename=MODULE)
    except SyntaxError as exc:
        fail('the patched %s would not parse: %s' % (MODULE, exc))
    print('[syntax ok]     %s parses' % MODULE)

    for name in TARGETS:
        out = working[name].encode('ascii')
        if endings[name] == b'\r\n':
            out = out.replace(b'\n', b'\r\n')
        with open(paths[name], 'wb') as handle:
            handle.write(out)
        print('[written]       %-32s %d -> %d bytes'
              % (name, len(originals[name]), len(out)))

    print('')
    print('patch applied -- %d edits across %d files'
          % (len(EDITS), len(TARGETS)))
    print('')
    print('NEXT:')
    print('  1. python ledger_index.py')
    print('  2. Maintenance suite. Expect 11 of 11, and the provenance')
    print('     scanner one lower than last run.')
    print('  3. Commit and push.')
    print('  4. Move this script to documentation/.')
    print('')
    print('MODE 5 -- and it is the gate here, not a formality:')
    print('  Relaunch and look at the Sun. The band should LEAN WITH the')
    print('  yellow rotation axis instead of lying flat on the ecliptic')
    print('  grid. About 7 degrees: visible, not dramatic. If the band and')
    print('  the axis still disagree, say so and do not push.')
    print('')
    print('OPEN FOR TONY:')
    print('  - L-229 proposed RICE 3/4/95/1 (11.4). Impact 4 because a')
    print('    wrong frame is a wrong physical claim on screen. Confirm or')
    print('    redirect, then re-run ledger_index.py.')


if __name__ == '__main__':
    main()
