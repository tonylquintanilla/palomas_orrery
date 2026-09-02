"""
patch_L254_2_venus_mars_dead_builders.py -- L-254, the Venus and Mars slice.

Built on palomas_orrery df80c35803ce916dafe6b84844d95181e43e5edd at
https://github.com/tonylquintanilla/palomas_orrery (branch main).

WHAT IT DOES
  Annotation only. No function removed, no behaviour changed, nothing
  the render can see.

  venus_visualization_shells.py -- marks 6 dead create_venus_*_shell
      functions in their own docstrings, adds a dispatch note above the
      section naming create_venus_magnetosphere_shell as the live one,
      stamps the module docstring.
  mars_visualization_shells.py -- the same for 7 dead
      create_mars_*_shell functions, live one is
      create_mars_magnetosphere_shell.

  Follows the pattern patch_L254_1 established in
  earth_visualization_shells.py on 2026-08-26.

HOW TO RUN
  Open this file in VS Code from the palomas_orrery repo root (the same
  folder as venus_visualization_shells.py) and press Run. It takes no
  arguments and asks no questions.

GUARDS
  Both files are fingerprinted (MD5 over LF-normalised content) and
  every anchor is verified to match exactly once BEFORE anything is
  written. All-or-nothing: if any check fails, no file is touched.
  Post-conditions are read back from disk, and include a NEGATIVE check
  that the two live magnetosphere builders were not annotated.

  No .bak files are written (safe-file-editing 1.10). If you need to
  undo, use Discard Changes in GitHub Desktop.

Module created: September 1, 2026 with Anthropic's Claude Opus 5.
"""

import glob
import hashlib
import os
import re
import sys

# ---------------------------------------------------------------- config

EXPECTED = {
    'venus_visualization_shells.py': '45feeaacdb6e7f3355d5ca879b028443',
    'mars_visualization_shells.py':  'a78047026fd42a45420e2d8d75c44694',
}

MARKER = 'DEAD CODE (L-254, 2026-09-01)'
ANY_MARKER = re.compile(r'DEAD CODE \(L-254')

LIVE = {
    'venus_visualization_shells.py': 'create_venus_magnetosphere_shell',
    'mars_visualization_shells.py':  'create_mars_magnetosphere_shell',
}

SIG = '(center_position=(0, 0, 0)):'


def dead_block(fn_name, first_line, absorb=''):
    """Return (anchor, replacement) for a one-line docstring.

    The anchor includes the def line, so it is unique even where two
    functions in the same file share a docstring. `absorb` is extra text
    swallowed by the edit and NOT written back -- used to delete the
    orphaned string in create_mars_hill_sphere_shell.
    """
    head = 'def %s%s\n' % (fn_name, SIG)
    anchor = head + ('    """%s"""' % first_line) + absorb
    replacement = head + (
        '    """%s\n'
        '\n'
        '    %s. Not on the render path: imported at\n'
        '    planet_visualization.py and called nowhere. This body renders its\n'
        '    sphere shells through SHELL_CONFIGS -> build_sphere_shell(). Edit\n'
        '    that config, not this function -- a change here renders nothing.\n'
        '    Retained pending the codebase-wide sweep in L-254.\n'
        '    """' % (first_line, MARKER)
    )
    return anchor, replacement


# (function name, docstring first line, text absorbed and deleted)
VENUS_DEAD = [
    ('create_venus_core_shell', "Creates Venus's core shell.", ''),
    ('create_venus_mantle_shell', "Creates Venus's mantle shell.", ''),
    ('create_venus_crust_shell',
     "Creates Venus's crust shell using Mesh3d for better performance with improved hover.", ''),
    ('create_venus_atmosphere_shell', "Creates Venus's lower atmosphere shell.", ''),
    ('create_venus_upper_atmosphere_shell', "Creates Venus's upper atmosphere shell.", ''),
    ('create_venus_hill_sphere_shell', "Creates Venus's Hill sphere.", ''),
]

# Mars's Hill sphere builder carries a second, WRONG docstring-shaped
# string two lines below its real one -- a copy-paste orphan reading
# "Creates Mars's upper atmosphere shell." It is a no-op expression, but
# it is a stale label sitting in a file this patch is already
# fingerprinting, so it goes now rather than never. Reported at the end
# of the run. (safe-file-editing: a pre-existing violation found
# mid-patch gets fixed, not noted.)
MARS_DEAD = [
    ('create_mars_inner_core_shell', "Creates Mars's inner core shell.", ''),
    ('create_mars_outer_core_shell', "Creates Mars's outer core shell.", ''),
    ('create_mars_mantle_shell', "Creates Mars's mantle shell.", ''),
    ('create_mars_crust_shell',
     "Creates Mars's crust shell using Mesh3d for better performance with improved hover.", ''),
    ('create_mars_atmosphere_shell', "Creates Mars's lower atmosphere shell.", ''),
    ('create_mars_upper_atmosphere_shell', "Creates Mars's upper atmosphere shell.", ''),
    ('create_mars_hill_sphere_shell', "Creates Mars's Hill sphere.",
     '\n\n    """Creates Mars\'s upper atmosphere shell."""'),
]


def dispatch_note(body, live_fn):
    """The section note. Deliberately carries no count -- see the text."""
    return (
        '# DISPATCH NOTE (L-254, 2026-09-01). ONE builder in this file is live:\n'
        '# %s, reached through the CUSTOM_SHELLS\n'
        "# 'builder' string in shell_configs.py that planet_visualization.py\n"
        "# resolves by rsplit('.', 1) + getattr. EVERY OTHER create_%s_*_shell\n"
        '# function in this file is dead and says so in its own docstring. This\n'
        "# body's sphere shells render through SHELL_CONFIGS ->\n"
        '# build_sphere_shell(), so editing a dead function here changes nothing.\n'
        '#\n'
        '# No count is written here, on purpose. A count in a comment is a\n'
        '# hand-maintained copy of something the file already reports; add a\n'
        '# builder and the number rots with nothing to catch it. The live one is\n'
        '# named and the dead ones are marked one by one, so both survive the\n'
        '# file changing.\n'
        '#\n'
        '# ON THE PATTERN: L-254 measures create_*_shell. Live builders that do\n'
        '# NOT match that pattern exist in other modules --\n'
        '# create_jupiter_ring_system, create_sun_streamer_band and\n'
        '# create_mercury_sodium_tail among them. Read "dead" here as "dead, and\n'
        '# measured against create_*_shell".\n'
        '#\n'
        r'# The _info strings in this file are NOT dead. They are the canonical `\n`'
        '\n'
        '# form, read by the Tk checkbox tooltips through celestial_objects.\n'
        '# get_shell_tooltip_names() and globals(), and imported by\n'
        '# shell_configs.py, which derives `<br>` from them at the Plotly\n'
        '# boundary. Editing one changes what the user reads in two places.\n'
        % (live_fn, body)
    )


VENUS_STAMP = (
    "September 1, 2026 (L-254, Opus 5): the six dead create_venus_*_shell\n"
    "    functions are marked as dead in their own docstrings, and a dispatch\n"
    "    note above the section names the one that is live\n"
    "    (create_venus_magnetosphere_shell). Annotation only -- no function\n"
    "    removed and no behaviour changed.\n"
)

MARS_STAMP = (
    "September 1, 2026 (L-254, Opus 5): the seven dead create_mars_*_shell\n"
    "    functions are marked as dead in their own docstrings, and a dispatch\n"
    "    note above the section names the one that is live\n"
    "    (create_mars_magnetosphere_shell). An orphaned second docstring in\n"
    "    create_mars_hill_sphere_shell, wrongly reading 'Creates Mars's upper\n"
    "    atmosphere shell.', was removed in the same pass. Annotation only --\n"
    "    no function removed and no behaviour changed.\n"
)


def build_edits():
    """Return {filename: [(anchor, replacement), ...]}."""
    edits = {'venus_visualization_shells.py': [], 'mars_visualization_shells.py': []}

    v = edits['venus_visualization_shells.py']
    v.append((
        '    change beyond factory routing.\n"""',
        '    change beyond factory routing.\n' + VENUS_STAMP + '"""',
    ))
    v.append((
        '# Venus Shell Creation Functions\n',
        '# Venus Shell Creation Functions\n\n'
        + dispatch_note('venus', 'create_venus_magnetosphere_shell'),
    ))
    for fn_name, line, absorb in VENUS_DEAD:
        v.append(dead_block(fn_name, line, absorb))

    m = edits['mars_visualization_shells.py']
    m.append((
        '    (Mode 5). Magnetosphere and bow-shock markers keep factory red.\n"""',
        '    (Mode 5). Magnetosphere and bow-shock markers keep factory red.\n'
        + MARS_STAMP + '"""',
    ))
    m.append((
        '# Mars Shell Creation Functions\n',
        '# Mars Shell Creation Functions\n\n'
        + dispatch_note('mars', 'create_mars_magnetosphere_shell'),
    ))
    for fn_name, line, absorb in MARS_DEAD:
        m.append(dead_block(fn_name, line, absorb))

    return edits


# ------------------------------------------------------------------ run

def fail(msg):
    print('')
    print('FAILURE: %s' % msg)
    print('NOTHING was written. No file on disk has changed.')
    print('If a previous run did write, undo is Discard Changes in GitHub Desktop.')
    sys.exit(1)


def read_lf(path):
    raw = open(path, 'rb').read()
    was_crlf = b'\r\n' in raw
    return (raw.replace(b'\r\n', b'\n') if was_crlf else raw), was_crlf


def docstring_of(text, fn_name):
    """Return the docstring block following a def, or '' if not found."""
    m = re.search(r'^def %s\(.*?\n(.*?)(?=\n(?:def |# ))' % re.escape(fn_name),
                  text, re.S | re.M)
    return m.group(1) if m else ''


def live_builders():
    """The create_*_shell functions shell_configs.py actually dispatches.

    Read from the config at run time, not typed here.
    """
    if not os.path.exists('shell_configs.py'):
        return None
    text, _ = read_lf('shell_configs.py')
    text = text.decode('utf-8', 'replace')
    found = re.findall(r"'builder':\s*'[\w]*_visualization_shells\.(create_\w+_shell)'", text)
    return set(found)


def remaining_census():
    """Count dead-and-unannotated create_*_shell functions, from disk.

    Measured at run time rather than typed here, so this report cannot go
    stale the way a hand-written count does.
    """
    live = live_builders()
    if live is None:
        return None, None
    rows = []
    for path in sorted(glob.glob('*_visualization_shells.py')):
        text, _ = read_lf(path)
        text = text.decode('utf-8', 'replace')
        names = re.findall(r'^def (create_\w+_shell)\(', text, re.M)
        dead = [n for n in names if n not in live]
        marked = len(ANY_MARKER.findall(text))
        left = len(dead) - marked
        if left > 0:
            rows.append((path.split('_')[0], len(names), len(dead), marked, left))
    return rows, live


def main():
    print('patch_L254_2 -- Venus and Mars dead-builder annotation (L-254)')
    print('=' * 66)

    edits = build_edits()

    for fn, pairs in edits.items():
        for _, new in pairs:
            try:
                new.encode('ascii')
            except UnicodeEncodeError as exc:
                fail('non-ASCII in replacement text for %s: %s' % (fn, exc))

    staged = {}

    # --- Phase 1: verify EVERYTHING before writing anything --------------
    for fn, pairs in edits.items():
        if not os.path.exists(fn):
            fail('%s not found. Run this from the palomas_orrery repo root.' % fn)

        content, was_crlf = read_lf(fn)

        actual = hashlib.md5(content).hexdigest()
        if actual != EXPECTED[fn]:
            fail(
                'BASE MOVED for %s.\n'
                '  expected %s\n'
                '  found    %s\n'
                '  This patch was built against df80c358. Establish WHAT differs\n'
                '  before assuming an edit: a size delta of about one byte per\n'
                '  line is CRLF, not content.' % (fn, EXPECTED[fn], actual)
            )
        print('  %-34s fingerprint matches%s'
              % (fn, ' [CRLF working copy]' if was_crlf else ''))

        if MARKER.encode('ascii') in content:
            fail('%s already carries the L-254 marker. This patch has already run.' % fn)

        out = content
        for anchor, new in pairs:
            a = anchor.encode('ascii')
            n = out.count(a)
            if n != 1:
                fail('anchor matched %d times (expected 1) in %s:\n    %r'
                     % (n, fn, anchor[:70]))
            out = out.replace(a, new.encode('ascii'))

        staged[fn] = (out.replace(b'\n', b'\r\n') if was_crlf else out, was_crlf, len(pairs))

    print('  all anchors verified, %d edits staged'
          % sum(v[2] for v in staged.values()))

    # --- Phase 2: write ---------------------------------------------------
    for fn, (data, was_crlf, n_edits) in staged.items():
        with open(fn, 'wb') as f:
            f.write(data)
        print('  wrote %-34s %d edits' % (fn, n_edits))

    # --- Phase 3: post-conditions, read back from DISK --------------------
    print('')
    print('Post-conditions (read back from disk):')
    want_dead = {'venus_visualization_shells.py': 6, 'mars_visualization_shells.py': 7}
    ok = True
    for fn, want in want_dead.items():
        disk, _ = read_lf(fn)
        text = disk.decode('utf-8', 'replace')
        got = text.count(MARKER)
        note = text.count('DISPATCH NOTE (L-254, 2026-09-01)')
        live_fn = LIVE[fn]
        live_named = live_fn in text.split('# DISPATCH NOTE')[-1][:900]
        # NEGATIVE check: the live builder must NOT have been annotated.
        live_clean = MARKER not in docstring_of(text, live_fn)
        print('  %-34s dead marked %d/%d | dispatch note %d/1 | live named %s'
              ' | live builder unannotated %s'
              % (fn, got, want, note, live_named, live_clean))
        if got != want or note != 1 or not live_named or not live_clean:
            ok = False
    if not ok:
        print('')
        print('POST-CONDITION FAILED. Files were written but do not read back as')
        print('expected. Undo is Discard Changes in GitHub Desktop, then report this.')
        sys.exit(1)

    print('')
    print('DONE. 13 dead builders annotated, 2 dispatch notes placed.')
    print('')
    print('The two live builders were deliberately NOT touched, and the check')
    print('above confirms it rather than asserting it:')
    print('  create_venus_magnetosphere_shell   LIVE (shell_configs.py:2167)')
    print('  create_mars_magnetosphere_shell    LIVE (shell_configs.py:2204)')
    print('')
    print('Nothing rendered changes. A visual check is not required for this patch.')
    print('Next: commit and push, then record the SHA on L-254.')
    print('')

    mars_text = read_lf('mars_visualization_shells.py')[0].decode('utf-8', 'replace')
    print('Fixed in passing, and worth knowing about:')
    print('  create_mars_hill_sphere_shell carried a SECOND docstring-shaped')
    print("  string reading \"Creates Mars's upper atmosphere shell.\" -- a")
    print('  copy-paste orphan, wrong label, no effect. Removed.')
    print('  Occurrences of that string now in the file: %d (want 1, the real one).'
          % mars_text.count("Creates Mars's upper atmosphere shell."))
    print('')

    rows, live = remaining_census()
    if rows is None:
        print('Remaining census skipped: shell_configs.py not found beside this script.')
    else:
        total = sum(r[4] for r in rows)
        print('Still to annotate, counted from disk just now, %d across %d modules.'
              % (total, len(rows)))
        print('Live builders are read from shell_configs.py (%d of them) and excluded:'
              % len(live))
        for body, n_all, n_dead, marked, left in rows:
            print('    %-9s %2d create_*_shell, %2d dead, %2d marked, %2d left'
                  % (body, n_all, n_dead, marked, left))


if __name__ == '__main__':
    main()
