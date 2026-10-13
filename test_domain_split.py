"""
test_domain_split.py - Checks for L-437: the provenance scanner's
whole-tree Tier-1 total prints with its domain split, and a module's
domain is read from its own docstring Domain: tag.

Run from the project directory (VS Code: open this file, click Run):
    python test_domain_split.py

Exits 0 if every check holds and every planted fault is caught, 1
otherwise. The maintenance run executes it as a gating checker,
"Domain Split", and its last line starts "DOMAIN SPLIT:".

WHAT IT CHECKS
--------------
Tony, 2026-10-12: "the provenance checker is still reporting 288 tier 1
items. Can we separate this into meaningful groups, like orrery, earth
science and stars in the checker report?" The split existed in the
audit's Findings by File Type table, and the total travelled without
it. And a module's domain had two homes: the scanner's hand list,
MODULE_DOMAIN_MAP, and the Domain: tag in each module's docstring,
which the atlas reads. They disagreed on 12 files at c5dff25.

Six checks, each on a small tree of synthetic modules written to a
temporary folder and scanned there, so they do not depend on the real
modules' findings, and nothing in the project folder is written:

  1. the tag is the domain: a file tagged stars is filed as stars, even
     under the name data_acquisition, which the old hand list filed as
     orrery; and the hand list is gone from the scanner.
  2. a file with no Domain: tag, and one with a tag outside the six,
     are counted as unclassified and named in the audit's coverage-gap
     note with the reason -- never defaulted into orrery.
  3. the whole-tree line on the console, the line in the audit's
     Priority Summary, the run history's tier1_by_domain and the Tier 1
     column of the audit's Findings by File Type table all give the
     same split, and it sums to the total.
  4. one finding moved between domains at an unchanged total changes
     the printed line, and the run history names the move (A Check That
     Cannot Fail Is Not Passing, its fourth move: the delta names what
     moved).
  5. the maintenance run's scanner row quotes the GATE PATH line first
     and the whole-tree line after it, and says so when either is
     missing.
  6. the run history keeps domain_counts as the all-tier count and
     tier1_by_domain as the Tier-1 count, two fields for two questions.

PLANTED FAULTS
--------------
Before the checks are trusted, six faults are planted, one at a time,
by swapping a function for a broken one inside this process (nothing
on disk changes), and each must make a named check fail:

  F1 the hand list back: every module filed as orrery.
  F2 an untagged file defaulted to orrery, not named.
  F3 the total printed without its split.
  F4 the run history written without tier1_by_domain.
  F5 the run history's comparison blind to domains.
  F6 the scanner row quoting the gate line only.

Then the real functions are restored and the checks must all pass.

Design: plain assert functions, no pytest; main() prints a summary.

Module created: October 13, 2026 with Anthropic's Claude Opus 5.5
(L-437, patch_L437_1_tier1_by_domain_20261013.py).

Role: devtool
Domain: dev_tools
"""

import contextlib
import io
import json
import os
import re
import shutil
import sys
import tempfile
import traceback

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import provenance_scanner as ps
import provenance_history as ph
import orrery_maintenance_run as omr


# ============================================================
# A SMALL TREE TO SCAN
# ============================================================
# Each module carries one display string with an uncited figure, which
# the scanner scores Tier-1. The docstring tag is the only thing that
# says which domain it belongs to.

def _module(domain_line, note):
    head = '"""A synthetic module for test_domain_split.py.\n\nRole: data\n'
    if domain_line:
        head += domain_line + '\n'
    return head + '"""\nNOTE = "%s"\n' % note


NOTES = {
    'o1': 'The probe passed 12,000 km above the surface at 9.5 km/s.',
    'o2': 'The moon orbits 384,400 km out, at 1.02 km/s.',
    's1': 'The star lies 4.2 light-years away, at 1.2 solar radii.',
    'e1': 'The heat wave reached 48 C on 5 days and displaced 2,000 people.',
}

BASE_TREE = {
    'orbit_one.py': _module('Domain: orrery', NOTES['o1']),
    'orbit_two.py': _module('Domain: orrery', NOTES['o2']),
    # The name the old hand list filed as orrery; the tag says stars.
    'data_acquisition.py': _module('Domain: stars', NOTES['s1']),
    'heat_wave.py': _module('Domain: earth_science', NOTES['e1']),
}


def _write_tree(files):
    tmp = tempfile.mkdtemp(prefix='domainsplit_')
    for name, text in files.items():
        with open(os.path.join(tmp, name), 'w', encoding='ascii',
                  newline='\n') as handle:
            handle.write(text)
    return tmp


def _scan(tmp):
    """Scan a tree; return (console text, audit text, history dict)."""
    audit = os.path.join(tmp, 'AUDIT.md')
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        ps.scan_project(tmp, audit)
    with open(audit, encoding='utf-8') as handle:
        audit_text = handle.read()
    with open(ph.history_path(tmp), encoding='utf-8') as handle:
        history = json.load(handle)
    return buf.getvalue(), audit_text, history


# ============================================================
# READING THE FOUR PLACES
# ============================================================

SHORT_TO_KEY = dict((short, key) for key, short in ps.DOMAIN_SHORT)
LABEL_TO_KEY = dict((label, key) for key, label in ps.DOMAIN_LABELS.items())


def _parse_split_text(text):
    """'5: orrery 2, stars 1' -> (5, {'orrery': 2, 'stars': 1})."""
    m = re.match(r'\s*(\d+)(?::\s*(.*))?$', text.strip().rstrip('.'))
    assert m, 'not a whole-tree split: %r' % text
    total = int(m.group(1))
    split = {}
    for part in (m.group(2) or '').split(','):
        part = part.strip()
        if not part:
            continue
        name, count = part.rsplit(' ', 1)
        assert name in SHORT_TO_KEY, 'unknown domain %r in %r' % (name, text)
        split[SHORT_TO_KEY[name]] = int(count)
    return total, split


def _console_split(console):
    lines = [l for l in console.splitlines() if 'Whole tree, Tier-1:' in l]
    assert len(lines) == 1, 'console whole-tree lines: %r' % lines
    return _parse_split_text(lines[0].split('Whole tree, Tier-1:', 1)[1])


def _audit_split(audit):
    m = re.search(r'\*\*Whole tree, Tier-1: (.*?)\.\*\*', audit)
    assert m, "the audit's Priority Summary has no whole-tree split"
    return _parse_split_text(m.group(1))


def _table_split(audit):
    """The Tier 1 column of Findings by File Type, nonzero domains."""
    section = audit.split('## Findings by File Type', 1)[1].split('\n---', 1)[0]
    split = {}
    for line in section.splitlines():
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) != 7 or not cells[2].isdigit():
            continue
        label = cells[0]
        key = LABEL_TO_KEY.get(label)
        if key is None and label.startswith('Unclassified'):
            key = ps.UNCLASSIFIED
        assert key, 'unknown table row %r' % label
        if int(cells[2]):
            split[key] = int(cells[2])
    return split


def _history_split(history):
    rec = history['runs'][-1]
    raw = rec.get('tier1_by_domain')
    assert raw is not None, 'the run record carries no tier1_by_domain'
    return int(rec['tier_counts']['1']), dict(
        (k, int(v)) for k, v in raw.items() if int(v))


# ============================================================
# THE CHECKS
# ============================================================

def check_tag_is_the_domain():
    """data_acquisition.py tagged stars is filed as stars."""
    assert not hasattr(ps, 'MODULE_DOMAIN_MAP'), \
        'the hand list MODULE_DOMAIN_MAP is still in the scanner'
    tmp = _write_tree(BASE_TREE)
    try:
        domain, problem = ps.classify_domain(
            'data_acquisition', os.path.join(tmp, 'data_acquisition.py'))
        assert (domain, problem) == ('stars', None), (domain, problem)
        _console, audit, _history = _scan(tmp)
        row = [l for l in audit.splitlines()
               if l.startswith('| `data_acquisition.py`')]
        assert row and '| stars |' in row[0], \
            'data_acquisition.py is not filed as stars: %r' % row
        assert _table_split(audit).get('stars') == 1, _table_split(audit)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def check_untagged_is_named_not_defaulted():
    """No tag and an unknown tag: unclassified, and named with why."""
    files = dict(BASE_TREE)
    files['mystery.py'] = _module(None, NOTES['o1'])
    files['odd_one.py'] = _module('Domain: astro', NOTES['o2'])
    tmp = _write_tree(files)
    try:
        _console, audit, _history = _scan(tmp)
        split = _table_split(audit)
        assert split.get(ps.UNCLASSIFIED) == 2, split
        assert split.get('orrery') == 2, \
            'an untagged file was counted as orrery: %r' % split
        gap = audit.split('**Domain coverage gap', 1)
        assert len(gap) == 2, 'no coverage-gap note in the audit'
        note = gap[1].split('\n---', 1)[0]
        assert '`mystery.py` -- no Domain: tag' in note, note
        assert '`odd_one.py` -- Domain: astro is not one of the six' in note, \
            note
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def check_four_places_agree():
    """Console, audit line, history field and table column agree."""
    tmp = _write_tree(BASE_TREE)
    try:
        console, audit, history = _scan(tmp)
        c_total, c_split = _console_split(console)
        a_total, a_split = _audit_split(audit)
        h_total, h_split = _history_split(history)
        t_split = _table_split(audit)
        assert c_total == a_total == h_total == 4, (c_total, a_total, h_total)
        assert sum(t_split.values()) == 4, t_split
        assert c_split == a_split == h_split == t_split, \
            'console %r, audit %r, history %r, table %r' % (
                c_split, a_split, h_split, t_split)
        assert t_split == {'orrery': 2, 'stars': 1, 'earth_science': 1}, \
            t_split
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def check_a_move_at_equal_total_shows():
    """One finding retagged from orrery to stars: same total, a
    different line, and the history names the move."""
    tmp = _write_tree(BASE_TREE)
    try:
        console1, _audit1, _history1 = _scan(tmp)
        with open(os.path.join(tmp, 'orbit_two.py'), 'w', encoding='ascii',
                  newline='\n') as handle:
            handle.write(_module('Domain: stars', NOTES['o2']))
        console2, _audit2, _history2 = _scan(tmp)
        t1, s1 = _console_split(console1)
        t2, s2 = _console_split(console2)
        assert t1 == t2 == 4, (t1, t2)
        assert s1 != s2, 'the line did not change when a finding moved'
        moved = [l for l in console2.splitlines() if 'MOVED by domain' in l]
        assert moved, 'the run history did not name the move'
        assert 'orrery 2 -> 1' in moved[0] and 'stars 1 -> 2' in moved[0], \
            moved[0]
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def check_maintenance_row_quotes_both():
    """The scanner row: the gate line first, the whole-tree line after."""
    rows = [r for r in omr.CHECKERS if r[1] == ['provenance_scanner.py']]
    assert len(rows) == 1, 'scanner rows: %r' % rows
    hint = rows[0][2]
    assert isinstance(hint, tuple) and hint[0] == 'GATE PATH:' \
        and 'Whole tree, Tier-1:' in hint, hint
    output = ('  GATE PATH: 0 TIER-1 -- the push gate holds\n'
              '  Whole tree, Tier-1: 4: orrery 2, stars 1, Earth System 1.\n')
    note = omr.verdict_from(output, hint)
    assert note.startswith('0 TIER-1 -- the push gate holds; '), note
    assert 'Whole tree, Tier-1: 4: orrery 2, stars 1, Earth System 1.' \
        in note, note
    missing = omr.verdict_from('  GATE PATH: 0 TIER-1\n', hint)
    assert 'no "Whole tree, Tier-1" line printed' in missing, missing
    rows = [r for r in omr.CHECKERS if r[1] == ['test_domain_split.py']]
    assert len(rows) == 1 and rows[0][0] == 'Domain Split' \
        and rows[0][2] == 'DOMAIN SPLIT:', rows


def check_history_keeps_two_fields():
    """domain_counts is all tiers; tier1_by_domain is Tier-1 only."""
    from datetime import datetime, timezone
    now = datetime.now(timezone.utc)
    rec = ph.make_run_record(now, now, '.', 3, 10, {1: 2, 3: 8},
                             {'orrery': 10}, {'a.py': 2},
                             tier1_by_domain={'orrery': 2})
    assert rec['domain_counts'] == {'orrery': 10}, rec['domain_counts']
    assert rec['tier1_by_domain'] == {'orrery': 2}, rec['tier1_by_domain']
    old = dict(rec)
    old.pop('tier1_by_domain')
    d = ph.compare(old, rec)
    assert d['domains']['known'] is False, d['domains']
    text = '\n'.join(ph.domain_delta_lines(old, rec, d['domains']))
    assert 'predates L-437' in text, text


CHECKS = [
    check_tag_is_the_domain,
    check_untagged_is_named_not_defaulted,
    check_four_places_agree,
    check_a_move_at_equal_total_shows,
    check_maintenance_row_quotes_both,
    check_history_keeps_two_fields,
]


# ============================================================
# THE PLANTED FAULTS
# ============================================================
# (name, target module, attribute, broken replacement builder, the
# check that must fail). Each replacement wraps or replaces the real
# function in memory only; the original is put back afterwards.

def _hand_list_back(real):
    def broken(module_name, filepath=None):
        return 'orrery', None
    return broken


def _untagged_defaults(real):
    def broken(module_name, filepath=None):
        domain, problem = real(module_name, filepath)
        if domain == ps.UNCLASSIFIED:
            return 'orrery', None
        return domain, problem
    return broken


def _total_only(real):
    def broken(total, split):
        return '%d' % total
    return broken


def _history_drops_split(real):
    def broken(*args, **kwargs):
        rec = real(*args, **kwargs)
        rec.pop('tier1_by_domain', None)
        return rec
    return broken


def _compare_blind(real):
    def broken(prev, cur):
        out = real(prev, cur)
        out['domains'] = {'known': True, 'moved': []}
        return out
    return broken


def _gate_line_only(real):
    def broken(output, hint):
        first = hint[0] if isinstance(hint, tuple) else hint
        return real(output, first)
    return broken


FAULTS = [
    ('F1 the hand list back', ps, 'classify_domain', _hand_list_back,
     check_tag_is_the_domain),
    ('F2 untagged defaulted to orrery', ps, 'classify_domain',
     _untagged_defaults, check_untagged_is_named_not_defaulted),
    ('F3 the total without its split', ps, 'whole_tree_split_text',
     _total_only, check_four_places_agree),
    ('F4 history without tier1_by_domain', ph, 'make_run_record',
     _history_drops_split, check_four_places_agree),
    ('F5 history blind to domains', ph, 'compare', _compare_blind,
     check_a_move_at_equal_total_shows),
    ('F6 the row quotes the gate only', omr, 'verdict_from',
     _gate_line_only, check_maintenance_row_quotes_both),
]


def run_fault(name, module, attr, builder, check):
    """True when the planted fault makes its check fail.

    Only counted as caught when the same check passes on the real
    functions (main() runs those first): a check that fails anyway
    would "catch" every fault and prove nothing.
    """
    real = getattr(module, attr)
    setattr(module, attr, builder(real))
    try:
        check()
    except AssertionError:
        return True
    finally:
        setattr(module, attr, real)
    return False


# ============================================================
# RUNNER
# ============================================================

def main():
    print('=' * 70)
    print('test_domain_split.py -- L-437: the whole-tree Tier-1 total and '
          'its domains')
    print('=' * 70)
    # The real functions first, so a fault is counted as caught only
    # by a check that passes without it.
    passed, failed = 0, []
    report = []
    for check in CHECKS:
        try:
            check()
            passed += 1
            report.append('  PASS  %s' % check.__name__)
        except Exception:                                 # noqa: BLE001
            failed.append(check.__name__)
            report.append('  FAIL  %s -- %s' % (
                check.__name__, traceback.format_exc(limit=1).strip()
                .splitlines()[-1]))
    print('Planted faults (each must make its check fail):')
    missed = []
    for name, module, attr, builder, check in FAULTS:
        if check.__name__ in failed:
            caught = False
            verdict = 'VOID  '
        else:
            try:
                caught = run_fault(name, module, attr, builder, check)
            except Exception:                             # noqa: BLE001
                caught = False
                traceback.print_exc(limit=1)
            verdict = 'CAUGHT' if caught else 'MISSED'
        print('  %s  %-38s by %s' % (verdict, name, check.__name__))
        if not caught:
            missed.append(name)
    print()
    print('Checks on the real functions:')
    for line in report:
        print(line)
    print('=' * 70)
    print('Results: %d of %d faults caught; %d of %d checks pass'
          % (len(FAULTS) - len(missed), len(FAULTS), passed, len(CHECKS)))
    if missed or failed:
        print('DOMAIN SPLIT: FAILED -- %s'
              % ', '.join(missed + failed))
        return 1
    print('DOMAIN SPLIT: PASS -- %d of %d planted faults caught; the '
          'split reads each module\'s Domain: tag and prints the same on '
          'the console, in the audit and in the run history.'
          % (len(FAULTS), len(FAULTS)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
