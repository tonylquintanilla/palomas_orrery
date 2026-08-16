"""retire_chromosphere_stylization.py -- L-180 dormant, L-196.

RUN COMMAND
-----------
Save this file into the palomas_orrery repo root (the same folder as
constants_new.py), open it in VS Code, and click Run.

    python retire_chromosphere_stylization.py

RUN normalize_continuations_stage1.py FIRST. This patch is built
against the tree that script produces. If it has not run, this one
aborts on the constants_new.py fingerprint and writes nothing.

WHAT IT DOES
------------
Retires CHROMOSPHERE_RADII = 1.1, the drawn shell radius that sat about
36x thicker than the physical chromosphere for visibility at orrery
scale. The shell now draws at CHROMOSPHERE_PHYSICAL_RADII (1.002875
solar radii), which is true scale.

Tony's ruling, 2026-08-16: the user should see the real proportion. A
2,000 km skin reading as a hairline welded to the photosphere is not a
rendering defect, it is the fact, and it teaches the proportion better
than an enlarged ring does.

Fifteen edits across eight files:

  constants_new.py                    the retirement, and the note on
                                      CHROMOSPHERE_PHYSICAL_KM that
                                      described 1.1 as the drawn value
  solar_visualization_shells.py       true-scale draw, new hover text,
                                      new legend name, 20-degree info
                                      marker, three citation comments
  shell_configs.py                    radius_au and legend name
  planet_visualization_utilities.py   re-export dropped
  planet_visualization.py             unused import dropped
  palomas_orrery_helpers.py           unused import dropped
  palomas_orrery.py                   unused import dropped (one line,
                                      targeted -- no full-file rewrite)
  test_constants_provenance.py        ordering assertion retargeted

ONE INCIDENTAL FIX, DELIBERATE
------------------------------
palomas_orrery_helpers.py line 32 held two Unicode right arrows in its
module docstring (astropy -> erfa -> erfa.core), a standing violation of
the ASCII-only convention that predates this work. It is normalized to
'->' here rather than left for a separate sweep. Tony's ruling,
2026-08-16: where a patch is already fingerprinting a file and finds a
violation of an ALREADY-RULED convention, fix it in passing and report
it. A dedicated sweep for two characters is costly and would never be
scheduled, so 'note it and move on' means it never gets fixed.

THE MARKER, AND WHY IT MOVES
----------------------------
The single info marker convention puts a shell's marker at its radius
times 1.05, at the north pole. The photosphere's lands at 1.050 solar
radii. At the old drawn radius the chromosphere's landed at 1.155 --
clear of it. At true scale it lands at 1.053, about one pixel away, and
Plotly would show one marker where the user expects two.

So the chromosphere marker steps 20 degrees in polar angle along the +x
meridian while keeping its own radius. The photosphere keeps the pole.
This is a new convention (orrery-coding-conventions), not an existing
one: the ring-marker collision fixed in May 2026 was solved by radial
separation, which cannot work when two radii differ by 0.29%.

WHAT L-180 DOES NOW
-------------------
L-180 required any display text to declare the stylization. It stays ON
RECORD and DORMANT. It governs nothing while no solar shell is
stylized, and it is NOT categorically superseded -- a future
stylization anywhere would revive it (Tony's ruling, 2026-08-16).

WHAT THIS CHANGES DOWNSTREAM
----------------------------
CHROMOSPHERE_RADII carried two 2026-08-02 cross-check annotations and
no # Source: line, which made it the one row in the 65-row dispatch
where the request builder scripted the responder's answer. Retiring the
value removes the row. Expect the builder to emit 64 after this runs.

SAFETY
------
All-or-nothing. Every file is fingerprinted (CRLF-normalized) before
anything is written, and every replaced block must read exactly as
recorded. Any mismatch aborts the whole run with nothing written.
Edits apply bottom-up within each file; each file's own line endings
are preserved.

Success: one 'ok' line per file, then 'patch applied (N bytes)'.
Failure: a single 'ERROR:' or 'ANCHOR FAIL' line; nothing is written.
"""

import hashlib
import os
import sys

EDITS = {
    'constants_new.py': {
        'fp': '643246ac82b532202635ec56bba4bbc5',
        'edits': [
            (176, 178,
             [
              '# Note: the PHYSICAL extent. CHROMOSPHERE_RADII (1.1) is the DRAWN',
              '#       shell radius, ~36x thicker, chosen for visibility at orrery',
              '#       scale. Both figures are real; they answer different questions.',
             ],
             [
              '# Note: the PHYSICAL extent, and since 2026-08-16 the drawn one too.',
              '#       CHROMOSPHERE_PHYSICAL_RADII below converts it to solar radii and',
              '#       is what the shell draws at. The 1.1 stylization is retired.',
             ]),
            (160, 170,
             [
              '# Solar atmosphere (in solar radii)',
              'CHROMOSPHERE_RADII = 1.1',
              '# Visualization shell radius (physical chromosphere extends ~2000 km above',
              '# photosphere = ~1.003 R_sun; drawn at 1.1 for visibility at orrery scale)',
              '# DRAWN value, deliberately larger than physical -- see',
              '# CHROMOSPHERE_PHYSICAL_KM below, and say so in any display text',
              "# (Tony's ruling, 2026-08-07, L-180).",
              '# Corrected 2026-08-02: 1.5 -> 1.1 (1.5 overstated the physical extent;',
              '#   Carroll & Ostlie Ch. 11 confirms ~2000 km, not 1.5 R_sun)',
              '# Cross-checked: Gemini 2026-08-02 -- Carroll & Ostlie (worksheet_gemini_constants_remaining.md)',
              '# Cross-checked: GPT 2026-08-02 -- NASA chromosphere data (constants_remaining_independent_verification_gpt.md)',
             ],
             [
              '# Solar atmosphere (in solar radii)',
              '# RETIRED 2026-08-16 -- CHROMOSPHERE_RADII = 1.1, the DRAWN shell radius.',
              '# The chromosphere now draws at CHROMOSPHERE_PHYSICAL_RADII (below), at',
              "# true scale. Tony's ruling: the user should see the real proportion, and",
              '# a 2000 km skin reading as a hairline on the photosphere IS the lesson.',
              '# Discoverability moved to the legend name and the info marker (see',
              '# orrery-coding-conventions, 20-degree info marker separation).',
              '# L-180 (2026-08-07) required display text to declare the stylization. It',
              '# stays ON RECORD and DORMANT: it governs nothing while no solar shell is',
              '# stylized, and is NOT categorically superseded -- a future stylization',
              "# anywhere would revive it (Tony's ruling, 2026-08-16).",
              '# The 2026-08-02 cross-checks were checks on the drawn value and retire',
              '# with it; the physical value below carries its own.',
             ]),
        ],
    },
    'palomas_orrery.py': {
        'fp': '29c281f71e0ee31044a2b108df7a5e40',
        'edits': [
            (268, 268,
             [
              '    CHROMOSPHERE_RADII,',
             ],
             [
             ]),
        ],
    },
    'palomas_orrery_helpers.py': {
        'fp': 'fc3d445d15b589cf9414d3a0fedab90d',
        'edits': [
            (31, 31,
             [
              '# Import path has changed across versions (astropy \u2192 erfa \u2192 erfa.core).',
             ],
             [
              '# Import path has changed across versions (astropy -> erfa -> erfa.core).',
             ]),
            (184, 184,
             [
              '    CHROMOSPHERE_RADII,',
             ],
             [
             ]),
        ],
    },
    'planet_visualization.py': {
        'fp': '7b04a0d3e315cdbe61370eb3c75385d1',
        'edits': [
            (63, 63,
             [
              '    CHROMOSPHERE_RADII, INNER_CORONA_RADII, OUTER_CORONA_RADII,',
             ],
             [
              '    INNER_CORONA_RADII, OUTER_CORONA_RADII,',
             ]),
        ],
    },
    'planet_visualization_utilities.py': {
        'fp': '5bae2fbaa4f3bb9ec733577d8ac72adc',
        'edits': [
            (57, 57,
             [
              '    CHROMOSPHERE_RADII, INNER_CORONA_RADII, OUTER_CORONA_RADII,',
             ],
             [
              '    INNER_CORONA_RADII, OUTER_CORONA_RADII,',
             ]),
        ],
    },
    'shell_configs.py': {
        'fp': '791263d4bc02581bea73302c5366b097',
        'edits': [
            (1919, 1920,
             [
              "            'name': 'Chromosphere',",
              "            'radius_au': CHROMOSPHERE_RADII * SOLAR_RADIUS_AU,",
             ],
             [
              "            'name': 'Chromosphere (2,000 km skin)',",
              "            'radius_au': CHROMOSPHERE_PHYSICAL_RADII * SOLAR_RADIUS_AU,",
             ]),
            (74, 74,
             [
              '    CHROMOSPHERE_RADII, INNER_CORONA_RADII, OUTER_CORONA_RADII,',
             ],
             [
              '    CHROMOSPHERE_PHYSICAL_RADII, INNER_CORONA_RADII, OUTER_CORONA_RADII,',
             ]),
        ],
    },
    'solar_visualization_shells.py': {
        'fp': '0722456bdaddf0a4641c69c263b14d22',
        'edits': [
            (1288, 1309,
             [
              'def create_sun_chromosphere_shell():',
              '    """Creates the Sun\'s chromosphere shell."""',
              '    x, y, z = create_sphere_points(CHROMOSPHERE_RADII * SOLAR_RADIUS_AU, n_points=25)',
              '    r_info = CHROMOSPHERE_RADII * SOLAR_RADIUS_AU * 1.05',
              '',
              '    shell_trace = go.Scatter3d(',
              '        x=x, y=y, z=z,',
              "        mode='markers',",
              "        marker=dict(size=3.0, color='rgb(30, 144, 255)', opacity=0.5),",
              "        name='Sun: Chromosphere',",
              "        legendgroup='Sun: Chromosphere',",
              "        hoverinfo='skip',",
              '        showlegend=True',
              '    )',
              '    # Phase 1 re-pipe (May 28, 2026): factory-routed.',
              '    info_trace = create_info_marker(',
              '        0, 0, r_info,',
              "        'rgb(30, 144, 255)',",
              '        f"Sun: Chromosphere<br><br>{chromosphere_info_hover}",',
              "        'Sun: Chromosphere'",
              '    )',
              '    return [shell_trace, info_trace]',
             ],
             [
              'def create_sun_chromosphere_shell():',
              '    """Creates the Sun\'s chromosphere shell, at true physical scale.',
              '',
              '    The shell sits ~0.29% above the photosphere, so at any scale that',
              '    also renders the corona it reads as welded to the solar surface.',
              '    That is the correct proportion and it is the point (2026-08-16).',
              '    Because photosphere and chromosphere radii differ by less than 10%,',
              '    their info markers would collide at the north pole. Per',
              '    orrery-coding-conventions, the photosphere keeps the pole and this',
              '    marker steps 20 degrees in polar angle along the +x meridian.',
              '    """',
              '    r_shell = CHROMOSPHERE_PHYSICAL_RADII * SOLAR_RADIUS_AU',
              '    x, y, z = create_sphere_points(r_shell, n_points=25)',
              '    r_info = r_shell * 1.05',
              '    info_polar_deg = 20.0',
              '    info_x = r_info * math.sin(math.radians(info_polar_deg))',
              '    info_z = r_info * math.cos(math.radians(info_polar_deg))',
              '',
              '    shell_trace = go.Scatter3d(',
              '        x=x, y=y, z=z,',
              "        mode='markers',",
              "        marker=dict(size=3.0, color='rgb(30, 144, 255)', opacity=0.5),",
              "        name='Sun: Chromosphere (2,000 km skin)',",
              "        legendgroup='Sun: Chromosphere (2,000 km skin)',",
              "        hoverinfo='skip',",
              '        showlegend=True',
              '    )',
              '    # Phase 1 re-pipe (May 28, 2026): factory-routed.',
              '    info_trace = create_info_marker(',
              '        info_x, 0, info_z,',
              "        'rgb(30, 144, 255)',",
              '        f"Sun: Chromosphere (2,000 km skin)<br><br>{chromosphere_info_hover}",',
              "        'Sun: Chromosphere (2,000 km skin)'",
              '    )',
              '    return [shell_trace, info_trace]',
             ]),
            (475, 475,
             [
              '# OUTER_CORONA_RADII, INNER_CORONA_RADII, CHROMOSPHERE_RADII, GRAVITATIONAL_INFLUENCE_AU, Oort Cloud AU constants);',
             ],
             [
              '# OUTER_CORONA_RADII, INNER_CORONA_RADII, CHROMOSPHERE_PHYSICAL_RADII, GRAVITATIONAL_INFLUENCE_AU, Oort Cloud AU constants);',
             ]),
            (344, 350,
             [
              '# Source: constants_new.py CHROMOSPHERE_RADII=1.1 (DRAWN shell radius, a',
              '#         declared stylization for visibility) and CHROMOSPHERE_PHYSICAL_KM',
              '#         =2000 (physical extent, Carroll & Ostlie Ch. 11, ~1.003 R_sun);',
              '#         Golub & Pasachoff (2010) The Solar Corona.',
              '# Note: the previous citation asserted a chromosphere radius of 1.5 solar',
              '#       radii, which the store has not held since 2026-08-02',
              '#       (corrected L-180).',
             ],
             [
              '# Source: constants_new.py CHROMOSPHERE_PHYSICAL_KM = 2000 (physical extent,',
              '# Source+: Carroll & Ostlie Ch. 11, ~1.003 R_sun, and since 2026-08-16 the',
              '# Source+: drawn radius as well); Golub & Pasachoff (2010) The Solar Corona.',
              '# Note: two earlier drawn radii are retired. 1.5 solar radii has not been',
              '#       held since 2026-08-02; the 1.1 stylization was retired 2026-08-16',
              '#       when the shell moved to true scale.',
             ]),
            (77, 89,
             [
              '# Source: CHROMOSPHERE_RADII (drawn) and CHROMOSPHERE_PHYSICAL_KM /',
              '#         CHROMOSPHERE_PHYSICAL_RADII (physical) in constants_new.py;',
              '#         Carroll & Ostlie Ch. 11 for the ~2000 km physical extent.',
              '#         The drawn shell is a declared stylization for visibility at',
              '#         orrery scale and the text says so (L-180, 2026-08-07).',
              'CHROMOSPHERE_RADIUS_LINE = (',
              '    f"* Radius: drawn from the photosphere out to "',
              '    f"{CHROMOSPHERE_RADII} solar radii "',
              '    f"(~{SOLAR_RADIUS_AU:.5f} - {CHROMOSPHERE_RADII * SOLAR_RADIUS_AU:.5f} AU).<br>"',
              '    f"  A stylization for visibility: the physical chromosphere extends only "',
              '    f"~{CHROMOSPHERE_PHYSICAL_KM:,.0f} km<br>"',
              '    f"  above the photosphere (~{CHROMOSPHERE_PHYSICAL_RADII:.3f} solar radii).<br>"',
              ')',
             ],
             [
              '# Source: Carroll & Ostlie, An Introduction to Modern Astrophysics, Ch. 11',
              '# Source+: -- the ~2000 km physical extent above the photosphere, carried',
              '# Source+: by CHROMOSPHERE_PHYSICAL_KM / CHROMOSPHERE_PHYSICAL_RADII in',
              '# Source+: constants_new.py. The shell draws at TRUE SCALE as of',
              '# Source+: 2026-08-16; the 1.1 stylization is retired (L-180 dormant).',
              'CHROMOSPHERE_RADIUS_LINE = (',
              '    f"* Radius: drawn at true scale, {CHROMOSPHERE_PHYSICAL_RADII:.6f} solar radii<br>"',
              '    f"  (~{SOLAR_RADIUS_AU:.5f} - {CHROMOSPHERE_PHYSICAL_RADII * SOLAR_RADIUS_AU:.5f} AU).<br>"',
              '    f"  The chromosphere is a skin about {CHROMOSPHERE_PHYSICAL_KM:,.0f} km deep on a star "',
              '    f"{SUN_RADIUS_KM:,.0f} km in radius --<br>"',
              '    f"  roughly {100.0 * (CHROMOSPHERE_PHYSICAL_RADII - 1.0):.2f}% of the solar radius. At any scale that "',
              '    f"also shows the corona<br>"',
              '    f"  it is too thin to resolve, which is why this shell appears welded to the<br>"',
              '    f"  photosphere.<br>"',
              ')',
             ]),
            (38, 38,
             [
              'from planet_visualization_utilities import (create_sphere_points, SOLAR_RADIUS_AU, CORE_AU, RADIATIVE_ZONE_AU, CHROMOSPHERE_RADII,',
             ],
             [
              'from planet_visualization_utilities import (create_sphere_points, SOLAR_RADIUS_AU, CORE_AU, RADIATIVE_ZONE_AU, SUN_RADIUS_KM,',
             ]),
        ],
    },
    'test_constants_provenance.py': {
        'fp': '6f49a0f911be6478fdcc96cb54e760f6',
        'edits': [
            (148, 148,
             [
              '    assert CHROMOSPHERE_RADII < INNER_CORONA_RADII < ROCHE_LIMIT_RADII < STREAMER_BELT_RADII, \\',
             ],
             [
              '    assert CHROMOSPHERE_PHYSICAL_RADII < INNER_CORONA_RADII < ROCHE_LIMIT_RADII < STREAMER_BELT_RADII, \\',
             ]),
            (69, 69,
             [
              '    CHROMOSPHERE_RADII,',
             ],
             [
              '    CHROMOSPHERE_PHYSICAL_RADII,',
             ]),
        ],
    },
}


def normalized(data):
    return data.replace(b'\r\n', b'\n')


def main():
    if not os.path.isfile('constants_new.py'):
        print('ERROR: run this from the palomas_orrery repo root '
              '(the folder holding constants_new.py).')
        return 1

    staged = []
    fixed = []
    total = 0

    for name in sorted(EDITS):
        spec = EDITS[name]
        if not os.path.isfile(name):
            print('ERROR: %s not found.' % name)
            return 1

        with open(name, 'rb') as handle:
            raw = handle.read()

        fp = hashlib.md5(normalized(raw)).hexdigest()
        if fp != spec['fp']:
            print('ERROR: %s does not match the base this patch was built '
                  'against.' % name)
            print('       expected %s' % spec['fp'])
            print('       found    %s' % fp)
            if name == 'constants_new.py':
                print('       Most likely cause: '
                      'normalize_continuations_stage1.py has not been run '
                      'yet. Run it first, then re-run this.')
            print('       Nothing written.')
            return 1

        crlf = b'\r\n' in raw
        lines = normalized(raw).decode('utf-8').split('\n')

        # The gate is on what THIS patch introduces. A file that already
        # holds non-ASCII is reported rather than blocked -- blocking on
        # somebody else's bug stops a correct patch, and staying silent
        # about it is how the convention quietly stops being true.
        for _, _, _, new_lines in spec['edits']:
            for line in new_lines:
                try:
                    line.encode('ascii')
                except UnicodeEncodeError:
                    print('ERROR: this patch would insert non-ASCII into '
                          '%s. Nothing written.' % name)
                    print('       %r' % line)
                    return 1
        before = sum(1 for b in bytearray(raw) if b > 127)
        if before:
            fixed.append((name, before))

        for start, end, old, new in spec['edits']:
            if end >= len(lines):
                print('ANCHOR FAIL: %s lines %d-%d run past end of file.'
                      % (name, start + 1, end + 1))
                return 1
            if lines[start:end + 1] != old:
                print('ANCHOR FAIL: %s lines %d-%d do not read as recorded.'
                      % (name, start + 1, end + 1))
                for offset, want in enumerate(old):
                    got = lines[start + offset]
                    if got != want:
                        print('       first difference at line %d'
                              % (start + offset + 1))
                        print('       expected %r' % want)
                        print('       found    %r' % got)
                        break
                print('       Nothing written.')
                return 1
            lines[start:end + 1] = new

        out = '\n'.join(lines).encode('utf-8')
        if crlf:
            out = out.replace(b'\n', b'\r\n')
        staged.append((name, out, len(spec['edits'])))
        total += len(out)

    for name, out, count in staged:
        with open(name, 'wb') as handle:
            handle.write(out)
        print('ok  %-36s %d edit(s)' % (name, count))

    for name, before in fixed:
        with open(name, 'rb') as handle:
            after = sum(1 for b in bytearray(handle.read()) if b > 127)
        if after:
            print('note: %s still holds %d non-ASCII byte(s) this patch did '
                  'not reach' % (name, after))
        else:
            print('note: %s had %d non-ASCII byte(s); normalized to ASCII in '
                  'passing' % (name, before))
    print('patch applied (%d bytes, %d edits across %d files)'
          % (total, sum(c for _, _, c in staged), len(staged)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
