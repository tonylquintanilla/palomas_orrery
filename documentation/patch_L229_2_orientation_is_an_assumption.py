"""patch_L229_2_orientation_is_an_assumption.py

Built on ca97e81d63dea33e848e8ed313f0992fd976609c at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Gallery at 8ec4f261013f09697d649efd25c8a746bffeff64.
Written August 23, 2026 with Anthropic's Claude Opus 5.

RUN IT LIKE THIS
    Save into the REPO ROOT. Open in VS Code, click Run.

Transactional, all-or-nothing, binary I/O, two targets.

WHY THIS PATCH EXISTS

`patch_L229_1` made a correct change for a reason it could not source.

The ROTATION is right and is not touched here. What is wrong is the
justification it wrote into a code comment and a ledger entry: that the
streamer belt follows the heliospheric current sheet, that the current
sheet tracks the solar magnetic equator, and that near solar minimum
the magnetic equator tracks the rotation equator. Tony asked whether
there was a reference for the belt's orientation. There is not. A
repo-wide search found none for the orientation, none for
`warp_amp_deg` = 15.0, none for the two-lobe warp, and none for the
hover's existing claim that the tilt sweeps toward the poles across the
11-year cycle.

Stating unsourced physics in a comment is the failure the resident rule
names: a citation is a claim about provenance and it must be TRUE, not
just present. Wrong-but-asserted is worse than uncited, because the
assertion suppresses the suspicion that would catch it.

WHAT IS SOURCED, AND IS ENOUGH ON ITS OWN

  The Sun's rotation pole -- `planet_poles['Sun']`, RA 286.13, dec
  63.87, IAU 2018 (Archinal et al.). Real, published, already cited.

  And a structural argument that needs no physics citation at all:
  `create_streamer_band_shape`'s own docstring says it returns points
  "in the body frame". The caller treated them as ecliptic. That is an
  internal contract violation, and the Sun's body frame is DEFINED by
  its rotation pole. So the band belongs in that frame because that is
  the frame it was built in -- not because anyone can cite that the
  belt tracks the magnetic equator.

  That argument fully supports the rotation. It just does not support
  the paragraph that was written around it.

WHAT THIS PATCH CHANGES

  1. The code comment drops the physics and keeps the two things that
     hold: the body-frame contract, and the sourced pole.

  2. The hover gains one short paragraph saying the orientation is a
     drawing choice anchored to a sourced pole, and naming the warp
     amplitude and lobe count as unsourced too. The module already ends
     with "Drawn as a visualization assumption where no measured
     boundary exists" -- this extends that habit to the plane the band
     sits in. Show the Envelope of the Unknowable: use the real geometry
     where it exists, and SAY SO where the choice is ours.

  3. L-229's "Why the solar equator is the right plane" bullet is
     replaced by an honest one, and the citation hunt is recorded as a
     Tony-side (do) item in the same shape as L-228.

  Every inserted hover line carries its own `<br>`, per
  orrery-coding-conventions 1.5. The self-check below enforces it.

  NOTE ON THE SCANNER. Adding hover lines moves line positions, which
  is exactly the coupling L-227 recorded: the provenance scanner judges
  citation by line distance. Re-run the maintenance suite after this
  and read the Tier-1 delta rather than assuming it held. Measured in
  the sandbox before delivery: this file stays at 6, tree stays at 292.

WHAT IS PERMANENT AND WHAT IS NOT
  The script is disposable. The honest framing is not.

AFTER RUNNING
  1. python ledger_index.py
  2. Maintenance suite. Expect 11 of 11 and the scanner unchanged at
     292; if it moved, say so.
  3. Commit and push.
  4. Move this script to documentation/.

  MODE 5 is NOT re-run for this. Nothing drawn changes -- only comments,
  hover prose and a ledger entry. The tilt Tony accepted stands.
"""

import hashlib
import os
import re
import sys

BASE_SHA = 'ca97e81d63dea33e848e8ed313f0992fd976609c'
MODEL = "Anthropic's Claude Opus 5"

HERE = os.path.dirname(os.path.abspath(__file__))
MODULE = 'solar_visualization_shells.py'
LEDGER = 'LEDGER_CONSOLIDATED.md'

FINGERPRINTS = {
    MODULE: 'f608c7fededd09542330d4d8595f5bcb',
    LEDGER: 'e2aa45fe33d45cddde353c897af9a15c',
}


# ==================================================================
# EDIT 1 -- the code comment stops asserting physics
# ==================================================================

OLD_1 = '''    # BODY FRAME -> ECLIPTIC. create_streamer_band_shape returns points in
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
'''
NEW_1 = '''    # BODY FRAME -> ECLIPTIC. create_streamer_band_shape's own docstring
    # says it returns points "in the body frame". Until 2026-08-23 the
    # caller scaled them and handed them to Plotly UNROTATED, i.e. treated
    # body-frame points as ecliptic ones. That is an internal contract
    # violation and it is the whole reason for this rotation -- no claim
    # about solar physics is needed to justify it, and none is made here.
    # The Sun's rotation axis trace, built from the very matrix used
    # below, was already correctly tilted, so two traces in one figure
    # disagreed about where the Sun's equator is. Found by Mode 5 (L-229).
    # Source: IAU 2018 solar pole, via idealized_orbits.planet_poles['Sun']
    #   (ra 286.13, dec 63.87) -- the SAME source build_rotation_axis_traces
    #   reads, so the band and the axis now derive from one matrix and
    #   cannot drift apart again.
    # ASSUMPTION: that the streamer belt is organized about the solar
    #   equator AT ALL is a drawing choice, not a sourced boundary. No
    #   citation for the belt's orientation exists in this project, nor
    #   for warp_amp_deg = 15.0, nor for the two-lobe warp. The pole is
    #   sourced; anchoring the band to it is ours. An earlier version of
    #   this comment argued the case from magnetic-equator physics that
    #   nobody had sourced -- withdrawn 2026-08-23, see L-229. The hover
    #   says the same thing to the reader.
'''


# ==================================================================
# EDIT 2 -- the hover tells the reader
# ==================================================================

OLD_2 = ('        "Drawn as a visualization assumption where no measured boundary<br>"\n'
         '        "exists (L-224)."\n')
NEW_2 = ('        "THE PLANE the band sits in is the SUN\'S equatorial plane, tilted<br>"\n'
         '        "about 7.25 degrees from the ecliptic by the IAU 2018 solar pole.<br>"\n'
         '        "The pole is measured. That the belt is organized about that plane<br>"\n'
         '        "at all is an ASSUMPTION -- as are the warp\'s 15-degree amplitude<br>"\n'
         '        "and its two lobes. No source for the belt\'s orientation is cited<br>"\n'
         '        "in this project. The ecliptic was worse, not the alternative.<br><br>"\n'
         '\n'
         '        "Drawn as a visualization assumption where no measured boundary<br>"\n'
         '        "exists (L-224)."\n')


# ==================================================================
# EDIT 3 -- L-229 stops asserting the physics
# ==================================================================

OLD_3 = (
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
)
NEW_3 = (
    "- **WITHDRAWN 2026-08-23, same day, and left visible.** This entry\n"
    "  originally carried a bullet titled \"Why the solar equator is the\n"
    "  right plane\", arguing from the heliospheric current sheet, the\n"
    "  solar magnetic equator, and the dipole's alignment with the spin\n"
    "  axis near solar minimum. **None of that is sourced anywhere in this\n"
    "  project.** Tony asked whether there was a reference for the belt's\n"
    "  orientation; a repo-wide search found none -- not for the\n"
    "  orientation, not for `warp_amp_deg` = 15.0, not for the two-lobe\n"
    "  warp, and not for the hover's existing claim that the tilt sweeps\n"
    "  toward the poles across the 11-year cycle. The physics may well be\n"
    "  right. It was stated as established, which is the failure the\n"
    "  resident rule names: wrong-but-asserted is worse than uncited,\n"
    "  because the assertion suppresses the suspicion that would catch it.\n"
    "  Recorded rather than deleted, because a claim withdrawn silently\n"
    "  leaves the next reader nothing to check against.\n"
    "- **What actually justifies the rotation, and needs no physics\n"
    "  citation.** `create_streamer_band_shape`'s own docstring says it\n"
    "  returns points \"in the body frame\"; the caller treated them as\n"
    "  ecliptic. That is an internal contract violation. The Sun's body\n"
    "  frame is DEFINED by its rotation pole, and that pole is sourced\n"
    "  (IAU 2018, RA 286.13, dec 63.87). So the band belongs in that frame\n"
    "  because it is the frame it was built in. Everything past that --\n"
    "  that the belt is organized about the solar equator at all -- is a\n"
    "  drawing choice, now declared as one in the code comment and in the\n"
    "  hover the reader sees.\n"
    "- **Tony-action (do): find a citation for the belt's orientation, or\n"
    "  leave it declared.** Same shape as L-228 and the same module. If a\n"
    "  source states that the streamer belt / heliospheric current sheet\n"
    "  is organized about the solar rotation or magnetic equator, cite it\n"
    "  and the ASSUMPTION note comes out. If none is found, the note\n"
    "  stays and that is an honest ending, not a failure. Unlike a range,\n"
    "  an orientation cannot be omitted -- the band has to be drawn\n"
    "  somewhere -- so this falls under Show the Envelope of the\n"
    "  Unknowable rather than under omit-if-unsourced.\n"
)


# ==================================================================
# EDIT 4 -- currency stamp
# ==================================================================

OLD_4 = (
    "Module updated: August 23, 2026 with Anthropic's Claude Opus 5 (L-229:\n"
    "streamer band rotated into the solar equatorial frame; the L-227\n"
    "citation-window follow-on), built on 851224c6.\n"
)
NEW_4 = (
    "Module updated: August 23, 2026 with Anthropic's Claude Opus 5 (L-229:\n"
    "streamer band rotated into the solar equatorial frame; the L-227\n"
    "citation-window follow-on), built on 851224c6.\n"
    "Module updated: August 23, 2026 with Anthropic's Claude Opus 5 (L-229\n"
    "part 2: the orientation is declared an ASSUMPTION; the unsourced\n"
    "magnetic-equator argument is withdrawn), built on ca97e81d.\n"
)


EDITS = [
    (MODULE, '1 code comment: contract + pole, no physics', OLD_1, NEW_1),
    (MODULE, '2 hover declares the plane an assumption', OLD_2, NEW_2),
    (LEDGER, '3 L-229: physics bullet withdrawn, visibly', OLD_3, NEW_3),
    (LEDGER, '4 ledger currency stamp', OLD_4, NEW_4),
]

TARGETS = [MODULE, LEDGER]


def fail(message):
    print('')
    print('ERROR: ' + message)
    print('Nothing was written. BOTH files on disk are untouched.')
    sys.exit(1)


def main():
    print('patch_L229_2_orientation_is_an_assumption.py')
    print('built on %s' % BASE_SHA)
    print('')

    paths, originals, endings = {}, {}, {}
    for name in TARGETS:
        path = os.path.join(HERE, name)
        if not os.path.exists(path):
            fail('%s not found beside this script. This one goes in the '
                 'REPO ROOT. It looked in: %s' % (name, HERE))
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

    # --- The hover convention this project wrote yesterday ------------
    # orrery-coding-conventions 1.5: every source line of a hover string
    # carries its own break, and no rendered line exceeds ~98 characters.
    inserted = [l for l in NEW_2.split('\n')
                if l.strip().startswith('"') or l.strip().startswith("'")]
    for idx, line in enumerate(inserted):
        body = re.findall(r'"((?:[^"\\]|\\.)*)"', line)
        if not body:
            continue
        text = body[0]
        is_last = (idx == len(inserted) - 1)
        # The final line of a hover string carries no break: nothing
        # follows it. Every other line must, or it joins the next one
        # into a single rendered run -- the L-227 defect.
        if '<br>' not in text and not is_last:
            fail('a hover line this patch inserts carries no <br>, which '
                 'is the exact defect L-227 fixed: %r' % text[:60])
        for seg in text.split('<br>'):
            if len(seg) > 98:
                fail('an inserted hover segment is %d characters; the file '
                     'norm is <= 98 (orrery-coding-conventions 1.5).'
                     % len(seg))
    print('[hover ok]      %d inserted hover lines, all break-terminated '
          '(bar the terminus), none over 98 chars' % len(inserted))

    working = {n: originals[n].replace(b'\r\n', b'\n').decode('utf-8')
               for n in TARGETS}

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

    # --- The unsourced physics must be GONE from both files ----------
    gone = ['tracks the solar\n    # MAGNETIC equator',
            'MAGNETIC equator. Near solar minimum the dipole lies close to the',
            'follows the heliospheric current sheet, which tracks the solar']
    for name in TARGETS:
        for phrase in gone:
            if phrase in working[name]:
                fail('unsourced physics survives in %s: %r'
                     % (name, phrase[:50]))
    if 'ASSUMPTION' not in working[MODULE]:
        fail('the ASSUMPTION note did not land in %s.' % MODULE)
    if 'WITHDRAWN 2026-08-23' not in working[LEDGER]:
        fail('the withdrawal record did not land in the ledger.')
    print('[honesty ok]    unsourced physics removed; ASSUMPTION note and '
          'withdrawal record both present')

    # --- The rotation itself must be UNTOUCHED -----------------------
    for token in ('create_planet_transformation_matrix', 'rot = M @ np.vstack',
                  'mx, my, mz = _to_ecliptic'):
        if token not in working[MODULE]:
            fail('this patch disturbed the rotation (%r missing). It is only '
                 'allowed to change comments and hover prose.' % token)
    print('[rotation ok]   the frame fix is untouched -- nothing drawn '
          'changes')

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
    print('  2. Maintenance suite. Expect 11 of 11 and the provenance')
    print('     scanner UNCHANGED at 292. Adding hover lines moves line')
    print('     positions, and the scanner judges citation by line')
    print('     distance (L-227), so read the delta rather than assume it.')
    print('  3. Commit and push.')
    print('  4. Move this script to documentation/.')
    print('')
    print('NO MODE 5 NEEDED. Nothing drawn changes -- comments, hover prose')
    print('  and one ledger entry. The 7.27-degree tilt already accepted')
    print('  stands exactly as it is.')
    print('')
    print('OPEN FOR TONY:')
    print('  - L-229 now carries a (do): find a citation for the belt\'s')
    print('    orientation, or leave it declared as a drawing choice. An')
    print('    orientation cannot be omitted the way an unsourced range')
    print('    can -- the band has to be drawn somewhere.')


if __name__ == '__main__':
    main()
