"""
test_dashboard_parity.py - every step the maintenance runs and the Daily
Run take has a dashboard button with the same name and the same script,
every button under a runner names one of its steps, every button's
script is on disk, and every card carries its short line; and proof that
this check can fail.

WHY THIS EXISTS

    When a row of a maintenance run goes red, you go to the dashboard to
    run that one check again, so its button has to carry the name the run
    printed (Tony's ruling of 2026-10-12, recorded in
    documentation/DESIGN_rulings_20261012.md). Every new check gets its
    button (Tony, 2026-10-10). Until now nothing held either rule: L-416
    matched the lists by hand three times, and L-324's note of 2026-09-12
    left this check as backlog. This is that check (L-440).

RUN COMMAND

    Open this file in VS Code and click Run. It takes no arguments.
        python test_dashboard_parity.py
    The orrery maintenance run runs it as the gating checker "Dashboard
    parity"; its last line starts "DASHBOARD PARITY:".

WHAT IT READS (both repositories; it edits neither)

    palomas_orrery_dashboard.py      LAUNCH_GROUPS and CARD_LINES. Loaded
                                     with its window libraries replaced by
                                     stand-ins, so no window opens and no
                                     display is needed.
    orrery_maintenance_run.py        GENERATORS and CHECKERS
    ../tonyquintanilla.github.io/gallery_maintenance_run.py
                                     GENERATORS and OFFLINE_CHECKERS
    ../tonyquintanilla.github.io/daily_run.py
                                     STEPS
    A runner it cannot find or read FAILS the run and is named. It is
    never skipped.

THE RULES IT HOLDS, by name, in both directions

    1. Every step has a button in its group -- the orrery's runs in
       "Maintenance Run", the website's in "Gallery -- checks and data",
       the Daily Run's in "Daily Run" -- with the same name. Names are
       compared ignoring case, a trailing "(L-...)" handle, and the
       difference between " -- " and ", ".
    2. That button runs the same script, with the same arguments, from
       the same repository. A Node step is run from the dashboard through
       documentation/run_offline_check.py with the step's own label, or
       through a wrapper named in WRAPPERS below.
    3. Every indented button in those three groups names a step.
    4. Every button's script is on disk (the dashboard's "Not Found").
    5. Every card has a line in CARD_LINES, of twelve words or fewer, and
       every line in CARD_LINES belongs to a card.
    The few steps a differently named button covers on purpose are in
    COVERED_BY, each with its reason; they are printed on every run so
    that they stay known.

    Not compared: the website's three LIVE checks (Served reachability,
    Export freshness, Store drift). They are functions inside the live
    run, not scripts, and the "Gallery Maintenance Run -- live" button
    runs them.

PROOF THAT IT CAN FAIL

    Before the real comparison it plants nine faults, one at a time, in
    copies of the real lists, and each must be caught by its own kind of
    finding: a step with no button, a renamed button, a button running
    the wrong script, a missing script, a card with no line, a line over
    twelve words, a line for no card, an indented button naming no step,
    and an unreadable runner.

Role: devtool
Domain: dev_tools

Module created: October 13, 2026 with Anthropic's Claude Opus 5.5 (L-440,
the dashboard's labels, descriptions and findability).
"""

import ast
import copy
import importlib.util
import os
import re
import sys
import types

HERE = os.path.dirname(os.path.abspath(__file__))
DASHBOARD = os.path.join(HERE, 'palomas_orrery_dashboard.py')
ORRERY_RUN = os.path.join(HERE, 'orrery_maintenance_run.py')
GALLERY = os.path.normpath(os.path.join(HERE, '..', 'tonyquintanilla.github.io'))

ORRERY_GROUP = 'Maintenance Run'
GALLERY_GROUP = 'Gallery -- checks and data'
DAILY_GROUP = 'Daily Run'
MAX_WORDS = 12

# Steps a differently named button covers on purpose: (repo, step) ->
# (button, reason). Printed on every run.
COVERED_BY = {
    ('gallery', 'Config mirror'): (
        'Config Mirror -- report only',
        'the same tool without --write: the run does the writing, the '
        'button only reports (2026-09-17)'),
    ('gallery', 'Objects mirror'): (
        'Objects Mirror Check',
        'the same tool without --write, which is also the checker step '
        '"Objects mirror check"'),
    ('gallery', 'Guest book'): (
        'Guest Book Checks',
        'both guest book checks behind one button (L-281)'),
    ('gallery', 'Guest book updater'): (
        'Guest Book Checks',
        'both guest book checks behind one button (L-281)'),
}

# A Node step the dashboard runs through a wrapper of its own.
WRAPPERS = {
    'Hover budget': 'documentation/run_hover_budget.py',
    'Solar System figures': 'documentation/run_solar_system_figures.py',
}
NODE_RUNNER = 'documentation/run_offline_check.py'

# Arguments a button leaves out because the script uses the same value by
# default: (repo, step) -> (argument, reason).
DEFAULT_ARGS = {
    ('orrery', 'Skill manifest'): (
        'PROJECT_INSTRUCTIONS.md',
        'skills_index.py defaults to PROJECT_INSTRUCTIONS.md'),
}


class Unreadable(Exception):
    """A file this check must read could not be read."""


def norm(name):
    """A name as compared: case, a trailing (L-...) and dashes ignored."""
    text = re.sub(r'\s*\([^)]*L-\d+[^)]*\)\s*$', '', name.strip())
    text = text.replace(' -- ', ' ').replace(', ', ' ')
    return ' '.join(text.casefold().split())


def _literal(path, name):
    """A module-level list, read by ast without running the file."""
    try:
        with open(path, encoding='utf-8') as f:
            tree = ast.parse(f.read())
    except (OSError, SyntaxError, UnicodeDecodeError) as exc:
        raise Unreadable('%s: %s' % (path, exc))
    for node in tree.body:
        if (isinstance(node, ast.Assign) and len(node.targets) == 1
                and getattr(node.targets[0], 'id', None) == name):
            return node.value
    raise Unreadable('%s: no %s list' % (path, name))


def _value(node):
    """ast.literal_eval, plus os.path.join over string literals."""
    if (isinstance(node, ast.Call)
            and ast.unparse(node.func) == 'os.path.join'):
        return '/'.join(_value(a) for a in node.args)
    if isinstance(node, (ast.List, ast.Tuple)):
        return [_value(e) for e in node.elts]
    return ast.literal_eval(node)


def read_runs(orrery_run=ORRERY_RUN, gallery=GALLERY):
    """Every step, as dicts: repo, kind, name, script, args."""
    steps = []
    for kind in ('GENERATORS', 'CHECKERS'):
        for row in _value(_literal(orrery_run, kind)):
            argv = row[1]
            steps.append(dict(repo='orrery', kind=kind, name=row[0],
                              script=argv[0], args=list(argv[1:]),
                              node=False))
    grun = os.path.join(gallery, 'gallery_maintenance_run.py')
    for row in _value(_literal(grun, 'GENERATORS')):
        argv, cwd = row[1], row[2]
        steps.append(dict(repo='gallery', kind='GENERATORS', name=row[0],
                          script=_join(cwd, argv[0]), args=list(argv[1:]),
                          node=False))
    for row in _value(_literal(grun, 'OFFLINE_CHECKERS')):
        runner, argv, cwd = row[1], row[2], row[3]
        steps.append(dict(repo='gallery', kind='CHECKERS', name=row[0],
                          script=_join(cwd, argv[0]), args=list(argv[1:]),
                          node=(runner == 'node')))
    daily = os.path.join(gallery, 'daily_run.py')
    for row in _value(_literal(daily, 'STEPS')):
        steps.append(dict(repo='gallery', kind='DAILY', name=row[0],
                          script=row[1], args=list(row[2]), node=False))
    return steps


def _join(cwd, script):
    if cwd in ('', '.'):
        return script
    return cwd.rstrip('/') + '/' + script


class _Stand(types.ModuleType):
    """A stand-in module: every attribute is a harmless class."""

    def __getattr__(self, name):
        if name.startswith('__'):
            raise AttributeError(name)
        return type(name, (object,), {'__init__': lambda s, *a, **k: None})


def read_dashboard(path=DASHBOARD):
    """(LAUNCH_GROUPS, CARD_LINES, SCRIPT_DIR, GALLERY_REPO_DIR)."""
    saved = {}
    for name in ('tkinter', 'customtkinter', 'PIL', 'PIL.Image',
                 'PIL.ImageTk'):
        saved[name] = sys.modules.get(name)
        sys.modules[name] = _Stand(name)
    try:
        spec = importlib.util.spec_from_file_location('_dash_parity', path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    except Exception as exc:
        raise Unreadable('%s: %s: %s' % (path, type(exc).__name__, exc))
    finally:
        for name, mod in saved.items():
            if mod is None:
                sys.modules.pop(name, None)
            else:
                sys.modules[name] = mod
    lines = getattr(module, 'CARD_LINES', None)
    if lines is None:
        raise Unreadable('%s: no CARD_LINES' % path)
    return (module.LAUNCH_GROUPS, lines, module.SCRIPT_DIR,
            module.GALLERY_REPO_DIR)


def buttons_of(groups, script_dir, gallery_dir):
    """Every card, as dicts: group, name, repo, script, args, indent."""
    out = []
    groot = os.path.abspath(gallery_dir)
    oroot = os.path.abspath(script_dir)
    for group, entries in groups.items():
        for e in entries:
            if isinstance(e, str):
                continue
            base = e[3] if len(e) > 3 else script_dir
            full = os.path.abspath(os.path.join(base, e[1]))
            if full.startswith(groot + os.sep):
                repo, rel = 'gallery', os.path.relpath(full, groot)
            else:
                repo, rel = 'orrery', os.path.relpath(full, oroot)
            out.append(dict(group=group, name=e[0], repo=repo,
                            script=rel.replace(os.sep, '/'),
                            args=list(e[5]) if len(e) > 5 and e[5] else [],
                            indent=bool(e[6]) if len(e) > 6 else False,
                            path=full))
    return out


def group_of(step):
    if step['kind'] == 'DAILY':
        return DAILY_GROUP
    return ORRERY_GROUP if step['repo'] == 'orrery' else GALLERY_GROUP


def compare(steps, buttons, card_lines):
    """All findings, as (kind, text). Empty means everything agrees."""
    found = []
    by_group = {}
    for b in buttons:
        by_group.setdefault(b['group'], []).append(b)
    claimed = set()
    for s in steps:
        group = group_of(s)
        pool = by_group.get(group, [])
        cover = COVERED_BY.get((s['repo'], s['name']))
        if cover and s['kind'] != 'DAILY':
            want = norm(cover[0])
        else:
            want = norm(s['name'])
        hits = [b for b in pool if norm(b['name']) == want]
        if not hits:
            found.append(('NO BUTTON', '%s step "%s" (%s) has no button '
                          'named so in "%s"' % (s['repo'], s['name'],
                                                s['script'], group)))
            continue
        b = hits[0]
        claimed.add((group, b['name']))
        problem = _command_problem(s, b, cover)
        if problem:
            found.append(('WRONG SCRIPT', '"%s" in "%s" %s'
                          % (b['name'], group, problem)))
    for group in (ORRERY_GROUP, GALLERY_GROUP, DAILY_GROUP):
        for b in by_group.get(group, []):
            if b['indent'] and (group, b['name']) not in claimed:
                found.append(('NAMES NO STEP', 'indented button "%s" in '
                              '"%s" names no step of its run'
                              % (b['name'], group)))
    for b in buttons:
        if not os.path.exists(b['path']):
            found.append(('NOT FOUND', '"%s" in "%s": %s is not on disk'
                          % (b['name'], b['group'], b['path'])))
    cards = set((b['group'], b['name']) for b in buttons)
    for key in sorted(cards):
        line = card_lines.get(key)
        if not line:
            found.append(('NO LINE', 'card "%s" in "%s" has no short line '
                          'in CARD_LINES' % (key[1], key[0])))
        elif len(line.split()) > MAX_WORDS:
            found.append(('LINE TOO LONG', 'card "%s" in "%s": %d words, '
                          'the limit is %d' % (key[1], key[0],
                                               len(line.split()), MAX_WORDS)))
    for key in sorted(set(card_lines) - cards):
        found.append(('LINE FOR NO CARD', 'CARD_LINES has a line for "%s" '
                      'in "%s", and no such card exists' % (key[1], key[0])))
    return found


def _command_problem(s, b, cover):
    """Why button b does not run step s, or None."""
    if b['repo'] != s['repo']:
        return 'runs a %s script; the step is in the %s' % (b['repo'],
                                                           s['repo'])
    if s['node']:
        if s['name'] in WRAPPERS:
            if b['script'] == WRAPPERS[s['name']]:
                return None
            return 'runs %s; the step is wrapped by %s' % (
                b['script'], WRAPPERS[s['name']])
        if cover:
            return None
        if b['script'] == NODE_RUNNER and b['args'] == [s['name']]:
            return None
        return 'runs %s %s; a Node step runs through %s "%s"' % (
            b['script'], ' '.join(b['args']), NODE_RUNNER, s['name'])
    if cover and s['kind'] != 'DAILY':
        if b['script'] == s['script']:
            return None
        if cover[0] == 'Guest Book Checks':
            return None
        return 'runs %s; the step runs %s' % (b['script'], s['script'])
    if b['script'] != s['script']:
        return 'runs %s; the step runs %s' % (b['script'], s['script'])
    want = list(s['args'])
    default = DEFAULT_ARGS.get((s['repo'], s['name']))
    if default and default[0] in want and default[0] not in b['args']:
        want.remove(default[0])
    if b['args'] != want:
        return 'passes %s; the step passes %s' % (b['args'] or 'nothing',
                                                   want or 'nothing')
    return None


def planted(steps, buttons, lines):
    """Nine faults, each required to produce its own kind of finding."""
    results = []

    def one(label, kind, s=steps, b=buttons, c=lines, runner=None):
        if runner is not None:
            try:
                runner()
                got = []
            except Unreadable as exc:
                got = [('UNREADABLE', str(exc))]
        else:
            got = compare(s, b, c)
        ok = any(k == kind for k, _t in got)
        results.append((label, kind, ok))

    def edit(name, field, value):
        bb = copy.deepcopy(buttons)
        for x in bb:
            if x['name'] == name and x['group'] == ORRERY_GROUP:
                x[field] = value
        return bb

    s1 = copy.deepcopy(steps) + [dict(repo='orrery', kind='CHECKERS',
                                      name='Planted step',
                                      script='planted_step.py', args=[],
                                      node=False)]
    one('a step with no button', 'NO BUTTON', s=s1)
    one('a renamed button', 'NO BUTTON',
        b=edit('Position Digits', 'name', 'Position Digit'))
    one('a button running the wrong script', 'WRONG SCRIPT',
        b=edit('Position Digits', 'script', 'test_orbit_markers.py'))
    one('a missing script', 'NOT FOUND',
        b=edit('Position Digits', 'path',
               os.path.join(HERE, 'no_such_script_planted.py')))
    c5 = dict(lines)
    c5.pop((ORRERY_GROUP, 'Position Digits'), None)
    one('a card with no line', 'NO LINE', c=c5)
    c6 = dict(lines)
    c6[(ORRERY_GROUP, 'Position Digits')] = ' '.join(['word'] * 13)
    one('a line over twelve words', 'LINE TOO LONG', c=c6)
    c7 = dict(lines)
    c7[(ORRERY_GROUP, 'Planted Card')] = 'A line for a card that is not there.'
    one('a line for no card', 'LINE FOR NO CARD', c=c7)
    b8 = copy.deepcopy(buttons) + [dict(group=ORRERY_GROUP,
                                        name='Planted Indented', repo='orrery',
                                        script='test_position_digits.py',
                                        args=[], indent=True,
                                        path=os.path.join(
                                            HERE, 'test_position_digits.py'))]
    c8 = dict(lines)
    c8[(ORRERY_GROUP, 'Planted Indented')] = 'A planted card.'
    one('an indented button naming no step', 'NAMES NO STEP', b=b8, c=c8)
    one('an unreadable runner', 'UNREADABLE',
        runner=lambda: read_runs(gallery=os.path.join(HERE,
                                                      'no_such_gallery')))
    return results


def main():
    print('DASHBOARD PARITY -- run steps against dashboard buttons (L-440)')
    print('  dashboard: %s' % DASHBOARD)
    print('  orrery run: %s' % ORRERY_RUN)
    print('  website repo: %s' % GALLERY)
    try:
        steps = read_runs()
        groups, lines, sdir, gdir = read_dashboard()
    except Unreadable as exc:
        print('')
        print('CANNOT READ: %s' % exc)
        print('DASHBOARD PARITY: FAIL -- a file it must read could not be '
              'read, so nothing was compared')
        return 1
    buttons = buttons_of(groups, sdir, gdir)

    print('')
    print('Planted faults, each must be caught by its own kind of finding:')
    caught = 0
    results = planted(steps, buttons, lines)
    for label, kind, ok in results:
        caught += ok
        print('  %-6s %-36s -> %s' % ('caught' if ok else 'MISSED', label,
                                      kind))

    found = compare(steps, buttons, lines)
    counts = {}
    for s in steps:
        key = 'Daily Run' if s['kind'] == 'DAILY' else s['repo']
        counts[key] = counts.get(key, 0) + 1
    print('')
    print('Compared %d orrery steps, %d website steps and %d Daily Run '
          'steps against %d buttons in %d groups; %d short lines read.'
          % (counts.get('orrery', 0), counts.get('gallery', 0),
             counts.get('Daily Run', 0), len(buttons), len(groups),
             len(lines)))
    print('Covered by a differently named button, on purpose (%d):'
          % len(COVERED_BY))
    for (repo, step), (button, why) in sorted(COVERED_BY.items()):
        print('  %s "%s" -> "%s": %s' % (repo, step, button, why))
    print('Not compared: the website\'s live checks, which are functions '
          'inside the live run (Served reachability, Export freshness, '
          'Store drift).')
    if found:
        print('')
        print('FINDINGS (%d):' % len(found))
        for kind, text in found:
            print('  %-16s %s' % (kind, text))
    print('')
    total = len(results)
    if found or caught != total:
        print('DASHBOARD PARITY: FAIL -- %d finding(s); %d of %d planted '
              'faults caught' % (len(found), caught, total))
        return 1
    print('DASHBOARD PARITY: PASS -- %d of %d planted faults caught; %d '
          'steps matched to their buttons by name and script; %d cards '
          'carry a short line' % (caught, total, len(steps),
                                  len(set((b['group'], b['name'])
                                          for b in buttons))))
    return 0


if __name__ == '__main__':
    sys.exit(main())
