"""
test_row_run.py - Pins for L-414: a row's citation context is its own
comment run, declared rows are their own kind, and the gate-path figure
is computed and recorded by name.

Run from the project directory (VS Code: open this file, click Run):
    python test_row_run.py

Exits 0 if every test passes, 1 on any failure. The maintenance run
executes it as a gating checker ("Scanner row run (L-414)").

WHAT IT PINS
------------
Until L-414 the scanner read a constant's citation context through a
fixed window, 30 lines above and 15 below. In constants_new.py rows sit
packed, with no blank line between them, and the window failed both
ways:

  - a row's OWN Source line, pushed 16 lines down by a Figures block
    that grew, was missed (EARTH_MEAN_RADIUS_KM, measured 2026-10-04);
  - a NEIGHBOUR's Source and Ref, a few lines above, were credited to a
    row whose own Source had been removed (planted fault F1 on
    EARTH_THERMOPAUSE_ALTITUDE_KM, 2026-10-09).

And a row declaring "# Status: declared pending" with a written reason
was scored as an uncited measurement (the three solar-wind rows).

The tests below rebuild each of those shapes in a synthetic file, so
they survive edits to the rows that motivated them (the same design as
test_provenance_1d.py and test_citation_inheritance.py). Fifteen of
the sixteen FAIL against the pre-L-414 scanner -- checked when this
file was written, by running it beside the scanner at aa46bb10 -- and
a test that could not fail would not be pinning anything. The one that
passes there is test_other_files_keep_the_window, which pins what L-414
deliberately left alone, so it should pass on both.

Also pinned: rows outside constants_new.py keep the old window (L-414
did not touch them); the shadow detector's own-citation predicate
agrees with scoring; the gate path is read from the two exports and a
file it cannot read makes the figure UNKNOWN, not zero; and the run
history compares the gate path by NAME, so one finding cleared and
another gained is visible at an unchanged count.

Design: plain assert functions, no pytest; main() prints a summary.

Module created: October 9, 2026 with Anthropic's Claude Opus 5.5
(L-414, patch_L414_1_scanner_window_20261009.py).

Role: devtool
Domain: dev_tools
"""

import json
import os
import shutil
import sys
import tempfile
import traceback

import provenance_scanner as ps
import provenance_history as ph


# ============================================================
# HELPERS
# ============================================================

def _units(text, fname='constants_new.py'):
    """Extract and score the constant/dict units of one synthetic file."""
    tmp = tempfile.mkdtemp(prefix='rowrun_')
    try:
        path = os.path.join(tmp, fname)
        with open(path, 'w', encoding='ascii', newline='\n') as f:
            f.write(text)
        units = ps.extract_units_from_file(path, fname[:-3], 'data')
        out = {}
        for u in units:
            if u.kind in ('constant', 'dict'):
                ps.score_unit(u, {})
                out[u.name] = u
        return out
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def _tier(u):
    return ps.action_tier(u.score) if u.score else None


FIGURES_BLOCK = ''.join('# Figures+: line %d of a block that grew\n' % i
                        for i in range(15))


# ============================================================
# THE ROW'S OWN RUN
# ============================================================

def test_late_source_in_own_run_is_read():
    """A Source line 17 lines below the assignment, in the row's own
    run, is the row's citation (EARTH_MEAN_RADIUS_KM's shape)."""
    text = ('X_RADIUS_KM = 6371.0\n'
            '# Unit: km\n'
            '# Status: measured V_SOURCED 2026-09-19\n'
            + FIGURES_BLOCK +
            '# Source: a real reference\n'
            '\n'
            'Y_OTHER_KM = 1.0\n'
            '# Source: another reference\n')
    u = _units(text)['X_RADIUS_KM']
    assert ps.has_citation(u.context_text), \
        "own Source line 17 lines down was not read"
    assert _tier(u) != 1, "a cited row scored Tier-1: %s" % u.vuln_reason


def test_neighbour_above_is_not_credited():
    """Packed rows: B has no Source; A's Source sits in the run between
    them. That run is A's, and B is uncited (planted fault F1)."""
    text = ('A_ALTITUDE_KM = 50.0\n'
            '# Unit: km\n'
            '# Source: belongs to A\n'
            '# Ref: https://example.org/a\n'
            'B_ALTITUDE_KM = 600.0\n'
            '# Unit: km\n'
            '# Status: measured V_SOURCED 2026-09-19\n'
            '# Note: B lost its Source line\n')
    rows = _units(text)
    assert _tier(rows['A_ALTITUDE_KM']) != 1
    b = rows['B_ALTITUDE_KM']
    assert b.vuln == ps.V_RECALLED and _tier(b) == 1, \
        "B was credited with A's citation: %s" % b.vuln_reason


def test_neighbour_below_is_not_credited():
    """A row with no Source, a blank line, then the next row's header
    citation within 15 lines: the next row's, not this row's."""
    text = ('C_RADIUS_KM = 10.0\n'
            '# Unit: km\n'
            '\n'
            '# Source: belongs to D, a header above it\n'
            'D_RADIUS_KM = 20.0\n')
    rows = _units(text)
    assert _tier(rows['C_RADIUS_KM']) == 1, \
        "C was credited with D's header citation"
    assert _tier(rows['D_RADIUS_KM']) != 1, \
        "a header run fenced by a blank line is the row's own"


def test_dict_row_reads_only_its_own_run():
    """A dict row's only literal has no citation; the row above, across
    a blank line, has one. CENTER_BODY_RADII's shape."""
    text = ('E_RADIUS_KM = 9.1\n'
            '# Source: belongs to E\n'
            '\n'
            'F_RADII = {\n'
            "    'One': E_RADIUS_KM,\n"
            "    'Two': 24000       # Model estimate (no year)\n"
            '}\n')
    f = _units(text)['F_RADII']
    assert f.vuln == ps.V_RECALLED, \
        "a dict row took its neighbour's citation: %s" % f.vuln_reason


def test_other_files_keep_the_window():
    """L-414 is scoped to constants_new.py. The same packed shape in
    another module still reads the old window, so its findings do not
    move with this patch."""
    text = ('A_ALTITUDE_KM = 50.0\n'
            '# Source: belongs to A\n'
            'B_ALTITUDE_KM = 600.0\n')
    b = _units(text, fname='some_data_module.py')['B_ALTITUDE_KM']
    assert b.vuln == ps.V_SOURCED, \
        "a module outside ROW_CONVENTION_FILES changed its context rule"


def test_shadow_predicate_agrees_with_scoring():
    """constant_has_own_citation() and scoring use one rule: in a packed
    file the run between two rows belongs to the row above."""
    import re
    src_re = re.compile(r'#\s*[Ss]ource\s*:')
    lines = ('A = 1.0\n'
             '# Source: belongs to A\n'
             'B = 2.0\n'
             '# Unit: km\n').splitlines(keepends=True)
    assert ps.constant_has_own_citation(lines, 1, src_re)
    assert not ps.constant_has_own_citation(lines, 3, src_re), \
        "B inherited A's trailing citation"
    lines = ('# Source: header, then a blank\n'
             '\n'
             'C = 3.0\n').splitlines(keepends=True)
    assert not ps.constant_has_own_citation(lines, 3, src_re), \
        "a citation across a blank line was read as the row's own"


# ============================================================
# DECLARED ROWS
# ============================================================

def _declared_names():
    return [entry[2] for entry in ps.DECLARED_ROWS]


def test_declared_pending_with_reason_is_declared():
    """The solar-wind rows: declared pending, a handle, a Declared line."""
    del ps.DECLARED_ROWS[:]
    text = ('G_PRESSURE_NPA = 2.0\n'
            '# Unit: npa\n'
            '# Status: declared pending 2026-09-12 -- L-314\n'
            '# Declared: the pressure both fits are evaluated at.\n')
    g = _units(text)['G_PRESSURE_NPA']
    assert g.vuln == ps.V_DECLARED and not g.score, \
        "a declared row with its reason was scored: %s" % g.vuln_reason
    assert g.vuln_reason == 'Declared pending (L-314)', g.vuln_reason
    assert 'G_PRESSURE_NPA' in _declared_names()


def test_reason_on_the_status_line_counts():
    """M3_PER_KM3's shape: the reason is written after '--' on the
    Status line, the place the Status Line grammar gives a pointer."""
    del ps.DECLARED_ROWS[:]
    text = ('H_PER_KM3 = 1.0e9\n'
            '# Status: declared 2026-09-19 -- an exact unit conversion\n')
    h = _units(text)['H_PER_KM3']
    assert h.vuln == ps.V_DECLARED, h.vuln_reason
    assert any(e[2] == 'H_PER_KM3' and e[4] == 'Status line'
               for e in ps.DECLARED_ROWS)


def test_bare_handle_is_not_a_reason():
    """'-- L-314' with no Declared line points at backlog and gives no
    reason. The row is scored as any other and named as reasonless."""
    del ps.DECLARED_WITHOUT_REASON[:]
    text = ('J_SPEED_KM_S = 400.0\n'
            '# Status: declared pending 2026-09-12 -- L-314\n')
    j = _units(text)['J_SPEED_KM_S']
    assert j.vuln == ps.V_RECALLED and _tier(j) == 1, j.vuln_reason
    assert any(e[2] == 'J_SPEED_KM_S' for e in ps.DECLARED_WITHOUT_REASON)


def test_neighbours_declared_status_is_not_borrowed():
    """A declared row's Status line cannot declare the row below it."""
    text = ('K_ANGLE_DEG = 120.0\n'
            '# Status: declared 2026-09-14 -- a drawing limit\n'
            '# Declared: where the drawn surface stops.\n'
            'L_ANGLE_DEG = 105.0\n')
    l_row = _units(text)['L_ANGLE_DEG']
    assert l_row.vuln != ps.V_DECLARED, \
        "L borrowed K's declared status"


# ============================================================
# THE GATE PATH
# ============================================================

def _gate_tree(rows, objects, store_text, objects_text):
    tmp = tempfile.mkdtemp(prefix='gate_')
    os.makedirs(os.path.join(tmp, 'data'))
    if rows is not None:
        with open(os.path.join(tmp, 'data', 'constants_export.json'),
                  'w') as f:
            json.dump({'rows': {n: {} for n in rows}}, f)
    with open(os.path.join(tmp, 'data', 'objects_export.json'), 'w') as f:
        json.dump({'objects': {k: {} for k in objects}}, f)
    with open(os.path.join(tmp, 'constants_new.py'), 'w') as f:
        f.write(store_text)
    with open(os.path.join(tmp, 'celestial_objects.py'), 'w') as f:
        f.write(objects_text)
    return tmp


STORE = ('M_RADIUS_KM = 10.0\n'
         '# Source: cited\n'
         '\n'
         'N_RADIUS_KM = 20.0\n'
         '\n'
         'P_RADIUS_KM = M_RADIUS_KM * 2\n')
OBJECTS = ('OBJECT_DEFINITIONS = [\n'
           "    {'name': 'Sun', 'key': 'sun',\n"
           "     'mission_info': 'The Sun is 695,700 km in radius.'},\n"
           "    {'name': 'Not served', 'mission_info': 'Nothing.'},\n"
           ']\n')


def test_gate_path_names_its_tier1_rows():
    tmp = _gate_tree(['M_RADIUS_KM', 'N_RADIUS_KM', 'P_RADIUS_KM'], ['sun'],
                     STORE, OBJECTS)
    try:
        gp = ps.load_gate_path(tmp)
        assert not gp['problems'], gp['problems']
        assert set(gp['objects']) == {'sun'}
        units = []
        for fname in ('constants_new.py', 'celestial_objects.py'):
            for u in ps.extract_units_from_file(
                    os.path.join(tmp, fname), fname[:-3], 'data'):
                ps.score_unit(u, {})
                units.append(u)
        on = ps.gate_path_units(units, gp, tmp)
        names = ps.gate_path_names(on)
        assert 'constants_new.py::N_RADIUS_KM' in names, names
        assert 'constants_new.py::M_RADIUS_KM' not in names, names
        assert gp['computed'] == ['P_RADIUS_KM'], gp['computed']
        assert not gp['unscored'], gp['unscored']
        text = '\n'.join(ps.gate_path_lines(gp, on, 99))
        assert 'GATE PATH: %d TIER-1' % len(names) in text
        assert 'N_RADIUS_KM' in text, "the failing row was not named"
        assert 'Examined:' in text, "a figure without what it examined"
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def test_unreadable_export_makes_the_figure_unknown():
    """A missing export must never print as 'GATE PATH: 0'."""
    tmp = _gate_tree(None, ['sun'], STORE, OBJECTS)
    try:
        gp = ps.load_gate_path(tmp)
        assert gp['problems'], "a missing export raised no problem"
        text = '\n'.join(ps.gate_path_lines(gp, [], 0))
        assert 'GATE PATH: UNKNOWN' in text
        assert 'GATE PATH: 0' not in text
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def test_exported_row_the_scanner_skipped_is_announced():
    """A typed row in the export that produced no unit is a blind spot
    and makes the figure UNKNOWN (a lower-case name is never a unit)."""
    store = STORE + 'q_radius_km = 5.0\n'
    tmp = _gate_tree(['M_RADIUS_KM', 'q_radius_km'], ['sun'], store,
                     OBJECTS)
    try:
        gp = ps.load_gate_path(tmp)
        units = []
        for u in ps.extract_units_from_file(
                os.path.join(tmp, 'constants_new.py'), 'constants_new',
                'data'):
            ps.score_unit(u, {})
            units.append(u)
        ps.gate_path_units(units, gp, tmp)
        assert gp['unscored'] == ['q_radius_km'], gp['unscored']
        assert 'GATE PATH: UNKNOWN' in '\n'.join(
            ps.gate_path_lines(gp, [], 0))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


# ============================================================
# THE RUN HISTORY, BY NAME
# ============================================================

def _record(names):
    from datetime import datetime, timezone
    now = datetime.now(timezone.utc)
    return ph.make_run_record(now, now, '.', 1, len(names or []),
                              {1: len(names or [])}, {}, {},
                              gate_tier1=names)


def test_history_sees_a_swap_at_equal_count():
    """Cleared one, gained one: the count is unchanged and the names
    are not. The delta must say both."""
    prev = _record(['constants_new.py::A'])
    cur = _record(['constants_new.py::B'])
    d = ph.compare(prev, cur)
    assert d['tier_delta']['1'] == 0
    assert d['gate']['entered'] == ['constants_new.py::B']
    assert d['gate']['left'] == ['constants_new.py::A']
    text = '\n'.join(ph.gate_delta_lines(prev, cur, d['gate']))
    assert 'ENTERED' in text and 'constants_new.py  B' in text


def test_history_counts_a_repeated_name():
    """A second finding under a name already listed is one more entry,
    not folded into the first (a row assigned twice)."""
    prev = _record(['constants_new.py::A'])
    cur = _record(['constants_new.py::A', 'constants_new.py::A'])
    d = ph.compare(prev, cur)
    assert d['gate']['entered'] == ['constants_new.py::A'], d['gate']


def test_history_before_l414_is_not_read_as_zero():
    prev = _record(None)
    prev.pop('gate_tier1')
    cur = _record([])
    d = ph.compare(prev, cur)
    assert d['gate']['known'] is False
    text = '\n'.join(ph.gate_delta_lines(prev, cur, d['gate']))
    assert 'predates L-414' in text


# ============================================================
# RUNNER
# ============================================================

TESTS = [
    test_late_source_in_own_run_is_read,
    test_neighbour_above_is_not_credited,
    test_neighbour_below_is_not_credited,
    test_dict_row_reads_only_its_own_run,
    test_other_files_keep_the_window,
    test_shadow_predicate_agrees_with_scoring,
    test_declared_pending_with_reason_is_declared,
    test_reason_on_the_status_line_counts,
    test_bare_handle_is_not_a_reason,
    test_neighbours_declared_status_is_not_borrowed,
    test_gate_path_names_its_tier1_rows,
    test_unreadable_export_makes_the_figure_unknown,
    test_exported_row_the_scanner_skipped_is_announced,
    test_history_sees_a_swap_at_equal_count,
    test_history_counts_a_repeated_name,
    test_history_before_l414_is_not_read_as_zero,
]


def main():
    print('=' * 70)
    print('test_row_run.py -- L-414: the row run, declared rows, the gate path')
    print('=' * 70)
    passed, failed = 0, []
    for test in TESTS:
        try:
            test()
            passed += 1
            print('  PASS  %s' % test.__name__)
        except Exception:                                 # noqa: BLE001
            failed.append(test.__name__)
            print('  FAIL  %s' % test.__name__)
            traceback.print_exc(limit=1)
    print('=' * 70)
    print('Results: %d passed, %d failed, %d total'
          % (passed, len(failed), len(TESTS)))
    if failed:
        print('ROW RUN: FAILED -- %s' % ', '.join(failed))
        return 1
    print('ROW RUN: %d of %d pins hold -- each row reads its own comment '
          'run, declared rows are named, the gate path is read by name.'
          % (passed, len(TESTS)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
