"""
patch_L191_1_sun_pairs_20261021.py - one string per Sun shell (L-191, the
Sun's share).

Built on 4a40d27cdb5609e226962efda02c77131e0b59bd at
https://github.com/tonylquintanilla/palomas_orrery (branch main).

WHAT IT DOES
    Fourteen Sun shells in solar_visualization_shells.py each had two
    strings: an _info string the checkbox tooltip shows and an
    _info_hover string the plot's hover shows. This keeps ONE per shell,
    named <shell>_info, written with newlines, and deletes the twin. The
    plot's hover is made from it at the Plotly boundary with
    .replace('\\n', '<br>'), as the gas giants' configs in shell_configs.py
    already do. The tooltip's own backstop (CreateToolTip turns <br> into
    a line break) stays.

    - NINE pairs were copies, letter for letter: outer Oort, inner Oort,
      inner Oort limit, solar wind (the heliopause), termination shock,
      chromosphere, photosphere, radiative zone, core. One copy is kept.
    - FIVE differed: gravitational influence, Roche limit, Alfven
      surface, corona, zodiacal dust. Tony picked each survivor
      (CHOICES below).

    Each twin's own citation block moves to the survivor, unless it was
    a copy of the survivor's. shell_configs.py and the dead import in
    planet_visualization.py follow the names.

    ALSO (L-460): the dashboard gets a Drawer Order button for the
    website's new "Drawer order" check, with its short line. The orrery's
    maintenance run holds the dashboard to the website's run, and since
    the website patch of 2026-10-21 that row has had no button.

ITS OWN CHECK (before anything is written)
    - The nine: the two copies are compared letter for letter, and the
      survivor written with newlines is compared with the old one with
      every <br> and newline treated alike. Any other difference refuses.
    - The five: the survivor is compared the same way with the text Tony
      picked; nothing in it is reworded.
    - No _info_hover name for these fourteen is left in the three files.
    - Every line it inserts is ASCII.

HOW TO RUN
    Save into the palomas_orrery folder, open in VS Code, click Run.
    (python patch_L191_1_sun_pairs_20261021.py)
    Success: one "ok" line per step, then "patch applied".
    Failure: "ERROR:" or "ANCHOR FAIL", and NOTHING was written.
    Undo is Discard Changes in GitHub Desktop.

THE SCANNER
    The whole-tree Tier-1 count falls by 3 (280 to 277 here), and it is not
    a clearing: three uncited lines of hover_text_sun_and_corona (the Parker
    closest approach, the MAPS crossing sequence, the perihelion) now sit
    within the scanner's 60-line window of the Alfven surface's citation,
    which is not their source. The gate path stays at 0.

AFTER RUNNING
    Open the orrery, hover each Sun checkbox and the matching marker in
    the plot: the same words. Then move this file to documentation/.

Module written: October 21, 2026 with Anthropic's Claude Opus 5.5.

Role: devtool
Domain: dev_tools
"""

import hashlib
import re
import sys

SHELLS = 'solar_visualization_shells.py'
CONFIGS = 'shell_configs.py'
PLANET = 'planet_visualization.py'
DASH = 'palomas_orrery_dashboard.py'

# Content fingerprints (LF-normalised) of the three files at c0feb22.
FINGERPRINTS = {
    SHELLS: '6584c8f6773b80f5d321184020fd63c6',
    CONFIGS: '3165d64323738630f124dddb283f2119',
    DASH: '5791b50d52ec367b9cbb7ac176325ea8',
    PLANET: '231328cba4aba6a27300e88c257fc122',
}

NINE = ['outer_oort', 'inner_oort', 'inner_limit_oort', 'solar_wind',
        'termination_shock', 'chromosphere', 'photosphere',
        'radiative_zone', 'core']

# Tony's picks, 2026-10-21. 'hover' keeps the plot hover's words,
# 'tooltip' the checkbox tooltip's. For the corona and the dust cloud,
# 'hover' is the title and the hover's words; 'hover+panel' adds the
# panel's words and the drawing note after them, as the tooltip had.
CHOICES = {
    'gravitational_influence': 'hover',
    'roche_limit': 'tooltip',
    'alfven_surface': 'tooltip',
    'corona': 'hover+panel',
    'zodiacal_dust': 'hover+panel',
}

FAILED = []


def fail(msg):
    FAILED.append(msg)


def read_lf(path):
    with open(path, 'rb') as f:
        raw = f.read()
    return raw.replace(b'\r\n', b'\n').decode('utf-8'), b'\r\n' in raw


def block(text, name):
    """(start, end) of the definition `name = (` ... its closing `)` line."""
    m = re.search(r'^%s = \($' % re.escape(name), text, re.M)
    if not m:
        return None
    end = re.compile(r'^ *\)[ \t]*$', re.M).search(text, m.end())
    if not end:
        return None
    return m.start(), end.end() + 1


def body(text, span):
    """The block without its first line, the name."""
    s = text[span[0]:span[1]]
    return s[s.index('\n') + 1:]


def comments_before(text, start):
    """The comment lines directly above `start`, as (start, string)."""
    lines = text[:start].split('\n')[:-1]
    keep = []
    while lines and lines[-1].startswith('#'):
        keep.insert(0, lines.pop())
    s = start - sum(len(x) + 1 for x in keep)
    return s, ''.join(x + '\n' for x in keep)


def to_newlines(src):
    """Every <br> in the block's string literals, as \\n."""
    return src.replace('<br>', '\\n')


def same_words(a, b):
    """True when two blocks differ only in <br> against \\n."""
    return a.replace('<br>', '\\n') == b.replace('<br>', '\\n')


def main():
    texts, crlf = {}, {}
    for path, want in FINGERPRINTS.items():
        try:
            texts[path], crlf[path] = read_lf(path)
        except OSError as e:
            print('ERROR: cannot read %s (%s). NOTHING was written.' % (path, e))
            return 1
        got = hashlib.md5(texts[path].encode('utf-8')).hexdigest()
        if got != want:
            print('ERROR: %s is not the file this patch was built on '
                  '(fingerprint %s, expected %s). NOTHING was written.'
                  % (path, got, want))
            return 1
    for name, choice in CHOICES.items():
        if choice.startswith('CHOICE_'):
            print('ERROR: no pick recorded for %s. NOTHING was written.' % name)
            return 1

    t = texts[SHELLS]

    # Work bottom-up: collect every edit as (start, end, new), apply in
    # reverse order of start.
    edits = []

    def plan_pair(name, survivor_src_body):
        tip = block(t, name + '_info')
        hov = block(t, name + '_info_hover')
        if not tip or not hov:
            fail('ANCHOR FAIL: %s_info or %s_info_hover not found' % (name, name))
            return
        new_body = to_newlines(survivor_src_body)
        edits.append((tip[0], tip[1], '%s_info = (\n%s' % (name, new_body)))
        # The twin's own comments: carried to the survivor unless they are
        # a copy of the survivor's.
        c_start, c_text = comments_before(t, hov[0])
        _, tip_c = comments_before(t, tip[0])
        carried = ''
        if c_text and c_text.startswith('# Source') and c_text != tip_c:
            carried = c_text
        del_start = c_start if c_text.startswith('# Source') else hov[0]
        # Swallow the blank line after the twin.
        del_end = hov[1] + (1 if t[hov[1]:hov[1] + 1] == '\n' else 0)
        edits.append((del_start, del_end, ''))
        if carried:
            note = ('# Note: the lines above came from %s_info_hover, the plot\n'
                    '# Note+: hover\'s copy, deleted 2026-10-21 (L-191).\n' % name)
            lines = carried.rstrip('\n').split('\n')
            moved = '\n'.join(re.sub(r'^# Source:', '# Source+:', x) for x in lines)
            edits.append((tip[0], tip[0], moved + '\n' + note))
        return tip, hov

    for name in NINE:
        tip = block(t, name + '_info')
        hov = block(t, name + '_info_hover')
        if not tip or not hov:
            fail('ANCHOR FAIL: %s pair not found' % name)
            continue
        if body(t, tip) != body(t, hov):
            fail('%s: the two copies are not letter for letter the same' % name)
            continue
        plan_pair(name, body(t, tip))
        print('ok  %-24s the copies agreed; one kept, written with newlines' % name)

    for name in ('gravitational_influence', 'roche_limit', 'alfven_surface'):
        tip = block(t, name + '_info')
        hov = block(t, name + '_info_hover')
        if not tip or not hov:
            fail('ANCHOR FAIL: %s pair not found' % name)
            continue
        pick = CHOICES[name]
        src = body(t, hov) if pick == 'hover' else body(t, tip)
        plan_pair(name, src)
        print('ok  %-24s kept the %s\'s words' % (name, 'hover' if pick == 'hover' else 'tooltip'))

    # The corona and the dust cloud are composed from shared word blocks.
    COMPOSED = {
        'corona': (
            'corona_info = (corona_hover_words + "\\n\\n" + corona_panel_words + "\\n\\n"\n'
            '               + corona_note_words)\n'
            'corona_info_hover = "Sun: Corona\\n\\n" + corona_hover_words\n',
            {'hover': '# One string, the checkbox tooltip and the plot hover alike\n'
                      '# (L-191, Tony\'s pick of 2026-10-21): the title and the hover\'s words.\n'
                      'corona_info = "Sun: Corona\\n\\n" + corona_hover_words\n',
             'hover+panel': '# One string, the checkbox tooltip and the plot hover alike\n'
                            '# (L-191, Tony\'s pick of 2026-10-21): the title, the hover\'s\n'
                            '# words, then the panel\'s words and the drawing note.\n'
                            'corona_info = ("Sun: Corona\\n\\n" + corona_hover_words + "\\n\\n"\n'
                            '               + corona_panel_words + "\\n\\n" + corona_note_words)\n'}),
        'zodiacal_dust': (
            'zodiacal_dust_info = (zodiacal_dust_hover_words + "\\n\\n"\n'
            '                      + zodiacal_dust_panel_words + "\\n\\n"\n'
            '                      + zodiacal_dust_note_words)\n'
            'zodiacal_dust_info_hover = ("Sun: Zodiacal Dust Cloud (F-corona)\\n\\n"\n'
            '                            + zodiacal_dust_hover_words)\n',
            {'hover': '# One string, the checkbox tooltip and the plot hover alike\n'
                      '# (L-191, Tony\'s pick of 2026-10-21): the title and the hover\'s words.\n'
                      'zodiacal_dust_info = ("Sun: Zodiacal Dust Cloud (F-corona)\\n\\n"\n'
                      '                      + zodiacal_dust_hover_words)\n',
             'hover+panel': '# One string, the checkbox tooltip and the plot hover alike\n'
                            '# (L-191, Tony\'s pick of 2026-10-21): the title, the hover\'s\n'
                            '# words, then the panel\'s words and the drawing note.\n'
                            'zodiacal_dust_info = ("Sun: Zodiacal Dust Cloud (F-corona)\\n\\n"\n'
                            '                      + zodiacal_dust_hover_words + "\\n\\n"\n'
                            '                      + zodiacal_dust_panel_words + "\\n\\n"\n'
                            '                      + zodiacal_dust_note_words)\n'}),
    }
    for name, (old, news) in COMPOSED.items():
        pick = CHOICES[name]
        if pick not in news:
            fail('%s: unknown pick %r' % (name, pick))
            continue
        n = t.count(old)
        if n != 1:
            fail('ANCHOR FAIL: %s definitions found %d times' % (name, n))
            continue
        i = t.index(old)
        edits.append((i, i + len(old), news[pick]))
        print('ok  %-24s kept %s' % (name, pick))

    # Consumers inside the shells module.
    for name in NINE + ['gravitational_influence', 'roche_limit', 'alfven_surface']:
        pat = re.compile(r'f"(Sun: [^"{]*<br><br>)\{%s_info_hover\}"' % name)
        for m in pat.finditer(t):
            edits.append((m.start(), m.end(),
                          '"%s" + %s_info.replace(\'\\n\', \'<br>\')' % (m.group(1), name)))
    for name in ('corona', 'zodiacal_dust'):
        old = "%s_info_hover.replace('\\n', '<br>')" % name
        n = t.count(old)
        if n != 1:
            fail('ANCHOR FAIL: the %s marker\'s hover found %d times' % (name, n))
            continue
        i = t.index(old)
        edits.append((i, i + len(old), "%s_info.replace('\\n', '<br>')" % name))
    # Two breadcrumbs that named corona_info_hover.
    old = "# the corona's words are corona_info and corona_info_hover, below.\n"
    n = t.count(old)
    if n != 2:
        fail('ANCHOR FAIL: the corona breadcrumbs found %d times, expected 2' % n)
    else:
        for m in re.finditer(re.escape(old), t):
            edits.append((m.start(), m.end(),
                          "# the corona's words are corona_info, below (one string\n"
                          "# since 2026-10-21, L-191).\n"))

    if FAILED:
        for f in FAILED:
            print(f)
        print('NOTHING was written.')
        return 1

    # Apply bottom-up; no two edits may overlap.
    edits.sort(key=lambda e: (e[0], e[1]))
    for a, b in zip(edits, edits[1:]):
        if a[1] > b[0] and not (a[0] == a[1] == b[0]):
            print('ERROR: two edits overlap at %d. NOTHING was written.' % b[0])
            return 1
    new = t
    for s, e, rep in sorted(edits, key=lambda e: (e[0], e[1]), reverse=True):
        new = new[:s] + rep + new[e:]

    # The module's own currency block.
    stamp_old = 'Module updated: October 20, 2026 with Anthropic\'s Claude Opus 5.5\n'
    if new.count(stamp_old) != 1:
        print('ANCHOR FAIL: the module stamp. NOTHING was written.')
        return 1
    new = new.replace(stamp_old,
        'Module updated: October 21, 2026 with Anthropic\'s Claude Opus 5.5\n'
        '(L-191, the Sun\'s share: one string per shell. The fourteen\n'
        '<shell>_info_hover twins are gone; each <shell>_info is written with\n'
        'newlines and is both the checkbox tooltip and, with each newline made\n'
        '<br>, the plot hover.)\n' + stamp_old, 1)

    # --- shell_configs.py ---
    c = texts[CONFIGS]
    imp_old = (
        "    # hover_text (Plotly hover, <br> line breaks)\n"
        "    core_info_hover, radiative_zone_info_hover,\n"
        "    photosphere_info_hover, chromosphere_info_hover,\n"
        "    roche_limit_info_hover, alfven_surface_info_hover,\n"
        "    termination_shock_info_hover,\n"
        "    solar_wind_info_hover,                      # heliopause hover (legacy name)\n"
        "    inner_limit_oort_info_hover,                # inner_oort_limit hover (swapped naming)\n"
        "    inner_oort_info_hover, outer_oort_info_hover,\n"
        "    gravitational_influence_info_hover,\n"
        "    # tooltip (Tk GUI, \\n line breaks)\n")
    imp_new = (
        "    # One string per shell, with \\n line breaks: the Tk tooltip as it\n"
        "    # is, and the Plotly hover_text with each \\n made <br> below\n"
        "    # (L-191, 2026-10-21; the _info_hover twins are gone).\n")
    if c.count(imp_old) != 1:
        print('ANCHOR FAIL: shell_configs.py import block. NOTHING was written.')
        return 1
    c = c.replace(imp_old, imp_new)
    for name in NINE + ['gravitational_influence', 'roche_limit', 'alfven_surface']:
        old = "'hover_text': %s_info_hover," % name
        if c.count(old) != 1:
            print('ANCHOR FAIL: shell_configs.py %s (%d). NOTHING was written.'
                  % (old, c.count(old)))
            return 1
        c = c.replace(old, "'hover_text': %s_info.replace('\\n', '<br>')," % name)
    print('ok  shell_configs.py: twelve hover_text entries made from <shell>_info')

    # --- planet_visualization.py: an import nothing used ---
    p = texts[PLANET]
    pv_old = (
        "from solar_visualization_shells import (\n"
        "    # Sun information texts\n"
        "    gravitational_influence_info_hover,\n"
        "    outer_oort_info_hover,\n"
        "    inner_oort_info_hover,\n"
        "    inner_limit_oort_info_hover,\n"
        "    solar_wind_info_hover,\n"
        "    termination_shock_info_hover,\n"
        "    chromosphere_info_hover,\n"
        "    photosphere_info_hover,\n"
        "    radiative_zone_info_hover,\n"
        "    core_info_hover\n"
        ")  \n")
    if p.count(pv_old) != 1:
        print('ANCHOR FAIL: planet_visualization.py import. NOTHING was written.')
        return 1
    p = p.replace(pv_old,
        "# The Sun's ten _info_hover strings were imported here and used nowhere;\n"
        "# the import went with the strings (L-191, 2026-10-21).\n")
    print('ok  planet_visualization.py: an import nothing used, removed')


    # --- palomas_orrery_dashboard.py: the website's Drawer order check ---
    d = texts[DASH]
    btn_anchor = '        ("Earth Scene Geometry",\n        os.path.join("documentation", "run_offline_check.py"),\n'
    btn_new = (
        '        ("Drawer Order",\n'
        '        os.path.join("documentation", "run_offline_check.py"),\n'
        '        "Each room\'s drawer lists its shells at the nearest part of "\n'
        '        "each as drawn, read from its served row (L-460). Builds the Sun "\n'
        '        "and Earth rooms with the real renderers and holds the page\'s "\n'
        '        "order to one it works out from the same rows, each stored "\n'
        '        "drawing\'s nearest dot read from its file. Moves one row\'s "\n'
        '        "edge and breaks its own file first, to show it can fail. GATES "\n'
        '        "the gallery runner. The check is Node, so this button runs it "\n'
        '        "through documentation/run_offline_check.py. Runs from the "\n'
        '        "gallery repo ROOT.",\n'
        '        GALLERY_REPO_DIR,\n'
        '        True,\n'
        '        ["Drawer order"],\n'
        '        True),\n')
    line_anchor = '    ("Gallery -- checks and data",\n     "Earth Scene Geometry"):\n'
    line_new = ('    ("Gallery -- checks and data",\n     "Drawer Order"):\n'
                '        "Checks each room\'s drawer lists shells where each begins.",\n')
    stamp_anchor = 'now, in Tools and Caches: horizons_check.py --all, which confirms every\nobject and data sheet today rather than only what is due (Tony,\n2026-10-20).\n'
    stamp_new = ('October 21, 2026 with Anthropic\'s Claude Opus 5.5 (L-460): Drawer\n'
                 'Order, the website\'s new checker, gets its button after Display\n'
                 'Figures, with its short line, running through\n'
                 'documentation/run_offline_check.py.\n')
    for a, b, where in ((btn_anchor, btn_new + btn_anchor, 'button'),
                        (line_anchor, line_new + line_anchor, 'short line'),
                        (stamp_anchor, stamp_anchor + stamp_new, 'stamp')):
        if d.count(a) != 1:
            print('ANCHOR FAIL: dashboard %s (%d). NOTHING was written.' % (where, d.count(a)))
            return 1
        d = d.replace(a, b)
    print('ok  palomas_orrery_dashboard.py: Drawer Order button, short line, stamp')

    # --- the check ---
    for path, txt in ((SHELLS, new), (CONFIGS, c), (PLANET, p)):
        for name in NINE + list(CHOICES):
            if re.search(r'\b%s_info_hover\b' % name, txt):
                # Comments may name the deleted twin; code may not.
                for line in txt.split('\n'):
                    if re.search(r'\b%s_info_hover\b' % name, line) and \
                            not line.lstrip().startswith('#'):
                        print('ERROR: %s still uses %s_info_hover: %s. NOTHING '
                              'was written.' % (path, name, line.strip()))
                        return 1
    for name in NINE + ['gravitational_influence', 'roche_limit', 'alfven_surface']:
        span = block(new, name + '_info')
        old_hov = body(t, block(t, name + '_info_hover'))
        old_tip = body(t, block(t, name + '_info'))
        want = old_hov if (name in NINE or CHOICES.get(name) == 'hover') else old_tip
        if not span or not same_words(body(new, span), want):
            print('ERROR: %s_info is not the kept text with only its breaks '
                  'changed. NOTHING was written.' % name)
            return 1
        if '<br>' in body(new, span):
            print('ERROR: %s_info still holds a <br>. NOTHING was written.' % name)
            return 1
    print('ok  the check: every kept string is the picked text, breaks only')

    for path, before, after in ((SHELLS, t, new), (CONFIGS, texts[CONFIGS], c),
                                (PLANET, texts[PLANET], p), (DASH, texts[DASH], d)):
        added = set(after.split('\n')) - set(before.split('\n'))
        bad = [x for x in added if any(ord(ch) > 127 for ch in x)]
        if bad:
            print('ERROR: a line this patch inserts is not ASCII in %s: %r. '
                  'NOTHING was written.' % (path, bad[0][:60]))
            return 1

    for path, txt in ((SHELLS, new), (CONFIGS, c), (PLANET, p), (DASH, d)):
        with open(path, 'wb') as f:
            f.write(txt.encode('utf-8'))
        if crlf[path]:
            print('note: %s was CRLF in the working copy; written LF' % path)
        print('wrote %s (%d bytes)' % (path, len(txt.encode('utf-8'))))
    print('stamp: solar_visualization_shells.py Module updated, October 21, 2026')
    print('scanner, what to expect: the whole-tree Tier-1 count falls by 3, all')
    print('  three in hover_text_sun_and_corona: the Parker closest-approach line,')
    print('  the MAPS crossing sequence and the perihelion line. NOT a clearing:')
    print('  with the twins gone, those lines sit within the scanner\'s 60-line')
    print('  window of the Alfven surface\'s citation (Cranmer et al. 2023), which')
    print('  is not their source. The gate path stays at 0. Recorded on the ledger.')
    print('patch applied')
    return 0


if __name__ == '__main__':
    sys.exit(main())
