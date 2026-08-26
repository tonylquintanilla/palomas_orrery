"""
patch_L248_1_constants_gate_and_au_yr.py -- clear the gate, derive 4.74.

Run:  save into the repo root (the folder holding constants_new.py),
      open in VS Code, click Run.
      Or:  python patch_L248_1_constants_gate_and_au_yr.py

Built on cf865ffc12862eeaeee5c0d7b1a2627dc003d4bd
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

Step 1 of the path in HANDOFF_20260825_evening_singularity_thread.md.
Two files, two jobs.

(a) constants_change_report.py gains a THIRD case beside changed and
    added: DERIVED. A line of the form

        M_PER_AU = KM_PER_AU * 1000

    is reported with its parents and passes, because a derived value
    cannot move unless a parent moves and every parent is watched by
    this same tool. Before this it landed in the unparsed bucket and
    failed the run -- every time the unit-variant convention was
    followed. What still FAILS is the formula changing: the same name
    with a different expression on the two sides of the diff is a value
    edit and is judged documented-or-bare like any number.

(b) exoplanet_coordinates.py line 373 stops typing 4.74 and derives it
    from KM_PER_AU, following the significant-digits protocol already
    used by LIGHT_MINUTES_PER_AU in constants_new.py. The returned
    velocity rises by 0.0099%.

NOT IN THIS PATCH: 3.26156, which is L-248 -- 36 sites across 11
modules, and sweeping three of them because one file happened to be
open would leave 33 shadows.

WHAT IS PERMANENT
    The DERIVED case in constants_change_report.py, and the derivation
    in exoplanet_coordinates.py. The script itself is one-shot.

AFTER THIS RUN
    python constants_change_report.py     (should now exit 0)
    python maintenance_run.py

Success: one "ok" line per edit, then "patch applied".
Failure: a single "ERROR:" or "ANCHOR FAIL" line; nothing is written to
any file, including files whose edits had already been staged in memory.
"""

import hashlib
import os
import sys

# md5 of each file's content with CRLF normalized to LF -- line endings
# are not content (safe-file-editing 1.8).
BASES = {
    'constants_change_report.py': 'abb26bb3badf7eec7e990a506d943479',
    'exoplanet_coordinates.py': 'a2583d2350584a4b46845a37cde81c7d',
}


# ======================================================================
# constants_change_report.py
# ======================================================================

CC_DOC_DERIVED_OLD = b"""EXIT CODE
---------
"""

CC_DOC_DERIVED_NEW = b"""DERIVED LINES
-------------
A constant can be written as an expression over other constants:

    M_PER_AU = KM_PER_AU * 1000

That is not a number, so it used to fall into the unparsed bucket and
fail the run -- every time the unit-variant convention was followed. It
is a third case now, beside changed and added, reported with its
parents and passed:

    M_PER_AU                       DERIVED = KM_PER_AU * 1000
        parents: KM_PER_AU
        each is watched here, so this line owes no # Source: of its own

The pass rests entirely on the parents being watched, so the test is
strict. The expression must parse, must be built from nothing but
numbers, arithmetic and names assigned at module level in
constants_new.py, and must reference at least one such name. A function
call, an attribute, a string, an unknown name -- any of those and the
line is not a derivation this tool can vouch for, so it goes back to
announcing.

What still fails is the DERIVATION changing. The same name with a
different expression on the two sides of the diff is a value edit, and
it is judged documented-or-bare exactly like a number.

EXIT CODE
---------
"""

CC_DOC_EXIT_OLD = b"""0 only when everything was understood and every changed value also moved
its provenance. 1 when a value moved alone, when a change could not be
attributed, or when a changed line was not understood at all. The
maintenance runner surfaces that as a failed checker.
"""

CC_DOC_EXIT_NEW = b"""0 only when everything was understood and every changed value also moved
its provenance. 1 when a value moved alone, when a change could not be
attributed, or when a changed line was not understood at all. A derived
line is understood, so it does not fail the run; a derived line whose
formula moved is a changed value and is judged like one. The
maintenance runner surfaces a 1 as a failed checker.
"""

CC_STAMP_OLD = b"""Module created: August 2026 with Anthropic's Claude Opus 5.
\"\"\"
"""

CC_STAMP_NEW = b"""Module created: August 2026 with Anthropic's Claude Opus 5.
Module updated: August 25, 2026 with Anthropic's Claude Opus 5
    (L-249 step 1: NAME = EXPR over tracked constants is a third case,
    DERIVED, so following the unit-variant convention no longer fails
    this gate).
\"\"\"
"""

CC_HELPERS_OLD = b"""COMMENT_RE = re.compile(r'^\\s*#')


def docstring_lines(here, base):"""

CC_HELPERS_NEW = b"""COMMENT_RE = re.compile(r'^\\s*#')

# NAME = <anything that is not a comment>. Deliberately loose: the test
# that matters happens in parse_derived(), which parses the right-hand
# side and refuses everything it cannot account for.
DERIVED_RE = re.compile(
    r'^\\s*([A-Za-z_][A-Za-z0-9_]*)\\s*=\\s*([^#]+?)\\s*(?:#.*)?$')

# The only node types a derived expression may contain, besides Name and
# a numeric Constant. Anything else -- a call, an attribute, a
# subscript, a string -- means this tool cannot vouch for the line, and
# it goes back to announcing.
DERIVED_NODES = (
    ast.Expression, ast.BinOp, ast.UnaryOp, ast.Load,
    ast.Add, ast.Sub, ast.Mult, ast.Div, ast.FloorDiv,
    ast.Mod, ast.Pow, ast.USub, ast.UAdd,
)


def module_level_names(here, base):
    \"\"\"Every name assigned at module level in TARGET, at base and now.

    Returns (set_of_names, note). The note says what was actually read,
    so a caller can print it rather than infer it -- the same reason
    docstring_lines returns one.

    Both revisions are read, and the union is what counts. A derived
    line can arrive in the same diff that adds the parent it derives
    from, and a parent added in this very edit is still a parent this
    tool watches.
    \"\"\"
    names = set()
    notes = []

    def collect(source, label):
        try:
            tree = ast.parse(source)
        except Exception as exc:
            notes.append('%s unreadable (%s)' % (label, exc.__class__.__name__))
            return
        found = set()
        for node in tree.body:
            if isinstance(node, ast.Assign):
                targets = node.targets
            elif isinstance(node, ast.AnnAssign):
                targets = [node.target]
            else:
                continue
            for target in targets:
                if isinstance(target, ast.Name):
                    found.add(target.id)
        names.update(found)
        notes.append('%s %d name(s)' % (label, len(found)))

    ok, shown = git(['show', '%s:%s' % (base, TARGET)], here)
    if ok:
        collect(shown, 'base')
    else:
        notes.append('base UNAVAILABLE -- working copy only')

    try:
        with open(os.path.join(here, TARGET), 'rb') as handle:
            collect(handle.read().decode('utf-8', 'replace'), 'working')
    except OSError as exc:
        notes.append('working copy unreadable (%s)' % exc)

    return names, '; '.join(notes)


def parse_derived(line, tracked):
    \"\"\"(name, expression, parents) if the line derives a value, else None.

    Strict on purpose. The pass this grants rests on every parent being
    watched by this same tool, so one name that is not assigned at
    module level in TARGET is enough to disqualify the line. It then
    falls through to the unparsed bucket and announces, which is the
    correct outcome for a value edit written in a shape nobody has
    vouched for.
    \"\"\"
    match = DERIVED_RE.match(line)
    if not match:
        return None
    name, expr = match.group(1), match.group(2).strip()
    try:
        tree = ast.parse(expr, mode='eval')
    except SyntaxError:
        return None
    parents = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            parents.add(node.id)
        elif isinstance(node, ast.Constant):
            if isinstance(node.value, bool):
                return None
            if not isinstance(node.value, (int, float)):
                return None
        elif not isinstance(node, DERIVED_NODES):
            return None
    if not parents or not parents <= tracked:
        return None
    return name, expr, sorted(parents)


def docstring_lines(here, base):"""

CC_SIG_OLD = b"def read_changes(diff_text, docstrings=frozenset()):"
CC_SIG_NEW = (b"def read_changes(diff_text, docstrings=frozenset(),\n"
              b"                 tracked=frozenset()):")

CC_RCDOC_OLD = b"""    like no change at all.
    \"\"\"
    changed, added, removed, unparsed = [], [], [], []
    docstring_seen = []
"""

CC_RCDOC_NEW = b"""    like no change at all.

    DERIVED -- a line of the form NAME = <expression over tracked
    names> is a third case rather than an unparsed one. It is reported
    with its parents and passes. A CHANGED derivation is a different
    matter: the same name carrying a different expression on the two
    sides of the diff is a value edit, judged documented-or-bare
    exactly like a number.
    \"\"\"
    changed, added, removed, unparsed = [], [], [], []
    docstring_seen = []
    derived_changed, derived_added, derived_removed = [], [], []
"""

CC_HUNKINIT_OLD = b"""        old_vals, new_vals = {}, {}
        comment_moved = False"""

CC_HUNKINIT_NEW = b"""        old_vals, new_vals = {}, {}
        old_derived, new_derived = {}, {}
        comment_moved = False"""

CC_DOCTEST_OLD = b"""                if body.strip() in docstrings:
                    hunk_docstring.append(sign + body.rstrip())
                    continue
                if any(ch.isdigit() for ch in body) and body.strip():"""

CC_DOCTEST_NEW = b"""                if body.strip() in docstrings:
                    hunk_docstring.append(sign + body.rstrip())
                    continue
                found = parse_derived(body, tracked)
                if found is not None:
                    # Runs BEFORE the digit test, so a derivation with
                    # no digit in it (X = A * B) is caught too -- that
                    # shape used to pass by being silently ignored,
                    # which is the same failure as an unread value edit.
                    bucket = old_derived if sign == '-' else new_derived
                    bucket[found[0]] = (found[1], found[2])
                    continue
                if any(ch.isdigit() for ch in body) and body.strip():"""

CC_RETURN_OLD = b"""            elif after is not None:
                added.append((name, after, comment_moved))
            else:
                removed.append((name, before))

    return changed, added, removed, unparsed, docstring_seen
"""

CC_RETURN_NEW = b"""            elif after is not None:
                added.append((name, after, comment_moved))
            else:
                removed.append((name, before))

        for name in sorted(set(old_derived) | set(new_derived)):
            before, after = old_derived.get(name), new_derived.get(name)
            if before is not None and after is not None:
                if before[0] != after[0]:
                    derived_changed.append(
                        (name, before[0], after[0], after[1],
                         'documented' if comment_moved else 'bare'))
            elif after is not None:
                derived_added.append((name, after[0], after[1]))
            else:
                derived_removed.append((name, before[0]))

    return (changed, added, removed, unparsed, docstring_seen,
            (derived_changed, derived_added, derived_removed))
"""

CC_MAINUNPACK_OLD = b"""    docstrings, doc_note = docstring_lines(here, base)
    changed, added, removed, unparsed, doc_lines = read_changes(
        out, docstrings)

    if not (changed or added or removed or unparsed):"""

CC_MAINUNPACK_NEW = b"""    docstrings, doc_note = docstring_lines(here, base)
    tracked, tracked_note = module_level_names(here, base)
    changed, added, removed, unparsed, doc_lines, derived = read_changes(
        out, docstrings, tracked)
    derived_changed, derived_added, derived_removed = derived

    if not (changed or added or removed or unparsed or derived_changed
            or derived_added or derived_removed):"""

CC_REPORT_OLD = b"""    for name, before in removed:
        print('  %-30s REMOVED (was %s)' % (name, before))
        print()

    if unparsed:"""

CC_REPORT_NEW = b"""    for name, before in removed:
        print('  %-30s REMOVED (was %s)' % (name, before))
        print()

    derived_bare = []
    for name, before, after, parents, state in derived_changed:
        print('  %-30s %s -> %s' % (name, before, after))
        print('      DERIVATION CHANGED -- now from %s'
              % ', '.join(parents))
        if state == 'documented':
            print('      provenance also changed -- deliberate correction')
        else:
            print('      VALUE MOVED ALONE -- no provenance change in this'
                  ' block')
            derived_bare.append(name)
        print()

    for name, expr, parents in derived_added:
        print('  %-30s DERIVED = %s' % (name, expr))
        print('      parents: %s' % ', '.join(parents))
        print('      each is watched here, so this line owes no'
              ' # Source: of its own')
        print()

    for name, expr in derived_removed:
        print('  %-30s DERIVATION REMOVED (was %s)' % (name, expr))
        print()

    if unparsed:"""

CC_SUMMARY_OLD = b"""    print('  %d changed, %d added, %d removed'
          % (len(changed), len(added), len(removed)))"""

CC_SUMMARY_NEW = b"""    print('  %d changed, %d added, %d removed'
          % (len(changed), len(added), len(removed)))
    if derived_changed or derived_added or derived_removed:
        print('  parents read from %s' % tracked_note)
        print('  %d derived line(s): %d changed, %d added, %d removed'
              % (len(derived_changed) + len(derived_added)
                 + len(derived_removed), len(derived_changed),
                 len(derived_added), len(derived_removed)))"""

CC_EXIT_OLD = b"    return 1 if (bare or unclear or unparsed) else 0"
CC_EXIT_NEW = b"    return 1 if (bare or unclear or unparsed or derived_bare) else 0"


# ======================================================================
# exoplanet_coordinates.py
# ======================================================================

EX_STAMP_OLD = b"""Role: data
Domain: stars
\"\"\"
"""

EX_STAMP_NEW = b"""Role: data
Domain: stars

Module updated: August 25, 2026 with Anthropic's Claude Opus 5
    (L-249 step 1: the AU/year to km/s factor is derived from
    KM_PER_AU instead of typed as 4.74).
\"\"\"
"""

EX_IMPORT_OLD = b"from constants_new import PARSEC_TO_AU\n"
EX_IMPORT_NEW = b"from constants_new import PARSEC_TO_AU, KM_PER_AU\n"

EX_CALC_OLD = b"""    # Tangential velocity = distance x angular velocity
    # 1 AU/year = 4.74 km/s
    velocity_au_yr = distance_pc * PARSEC_TO_AU * pm_rad_yr
    velocity_km_s = velocity_au_yr * 4.74
"""

EX_CALC_NEW = b"""    # Tangential velocity = distance x angular velocity
    # 1 AU/year in km/s, derived rather than typed. Written inline
    # rather than as a named constant because it is used once here and
    # nowhere else; a module-level copy would be a shadow constant.
    # Derived: KM_PER_AU / (Julian year in seconds)
    #          149597870.7 / (365.25 x 86400) = 4.740470463...
    # Derived+: Previous hardcoded value was 4.74 (consistent to 3 sig
    #          figs). Deriving it raises the returned velocity by
    #          0.0099%.
    velocity_au_yr = distance_pc * PARSEC_TO_AU * pm_rad_yr
    velocity_km_s = velocity_au_yr * (KM_PER_AU / (365.25 * 86400.0))
"""


EDITS = {
    'constants_change_report.py': [
        (CC_HELPERS_OLD, CC_HELPERS_NEW,
         'DERIVED_RE, module_level_names(), parse_derived()'),
        (CC_SIG_OLD, CC_SIG_NEW, 'read_changes() takes the tracked names'),
        (CC_RCDOC_OLD, CC_RCDOC_NEW, 'read_changes() docstring + accumulators'),
        (CC_HUNKINIT_OLD, CC_HUNKINIT_NEW, 'per-hunk derived buckets'),
        (CC_DOCTEST_OLD, CC_DOCTEST_NEW, 'classify derived lines before the digit test'),
        (CC_RETURN_OLD, CC_RETURN_NEW, 'fold derived lines into the return'),
        (CC_MAINUNPACK_OLD, CC_MAINUNPACK_NEW, 'main() reads tracked names, unpacks derived'),
        (CC_REPORT_OLD, CC_REPORT_NEW, 'report derived changed / added / removed'),
        (CC_SUMMARY_OLD, CC_SUMMARY_NEW, 'summary counts derived lines and says what was read'),
        (CC_EXIT_OLD, CC_EXIT_NEW, 'a bare derivation change fails the run'),
        (CC_DOC_DERIVED_OLD, CC_DOC_DERIVED_NEW, 'docstring: DERIVED LINES section'),
        (CC_DOC_EXIT_OLD, CC_DOC_EXIT_NEW, 'docstring: EXIT CODE mentions derived'),
        (CC_STAMP_OLD, CC_STAMP_NEW, 'docstring: currency stamp'),
    ],
    'exoplanet_coordinates.py': [
        (EX_CALC_OLD, EX_CALC_NEW, 'derive the AU/year to km/s factor from KM_PER_AU'),
        (EX_IMPORT_OLD, EX_IMPORT_NEW, 'import KM_PER_AU'),
        (EX_STAMP_OLD, EX_STAMP_NEW, 'docstring: currency stamp'),
    ],
}


def fail(msg):
    print('ERROR: ' + msg)
    sys.exit(1)


def main():
    staged = {}

    for filename, edits in EDITS.items():
        if not os.path.exists(filename):
            fail('%s not found. Run this from the repo root.' % filename)

        with open(filename, 'rb') as handle:
            data = handle.read()

        is_crlf = data.count(b'\r\n') > 0
        norm = data.replace(b'\r\n', b'\n')
        fp = hashlib.md5(norm).hexdigest()
        if fp != BASES[filename]:
            print('ERROR: BASE MOVED -- %s' % filename)
            print('  expected content fingerprint %s' % BASES[filename])
            print('  found                        %s' % fp)
            print('  (line endings are normalized before hashing, so this')
            print('   is a content difference, not a CRLF/LF difference)')
            sys.exit(1)
        print('base ok  %-30s (%s)  %d bytes'
              % (filename, 'CRLF' if is_crlf else 'LF', len(data)))

        out = data
        for old, new, label in edits:
            o, n = old, new
            if is_crlf:
                o = o.replace(b'\n', b'\r\n')
                n = n.replace(b'\n', b'\r\n')
            bad = sorted({b for b in n if b > 127})
            if bad:
                fail('non-ASCII byte(s) in inserted text (%s): %r' % (label, bad))
            count = out.count(o)
            if count != 1:
                print('ANCHOR FAIL (%d matches, expected 1) in %s: %s'
                      % (count, filename, label))
                print('  nothing written to any file.')
                sys.exit(1)
            out = out.replace(o, n)
            print('ok  %-30s %s' % (filename, label))

        if is_crlf and out.count(b'\n') != out.count(b'\r\n'):
            fail('%s: mixed line endings introduced' % filename)
        pre_existing = sum(1 for b in data if b > 127)
        if pre_existing:
            print('note %-30s %d pre-existing non-ASCII byte(s), left alone'
                  % (filename, pre_existing))
        staged[filename] = (data, out, is_crlf)

    # Every edit in every file matched before anything is written.
    for filename, (data, out, is_crlf) in staged.items():
        with open(filename, 'wb') as handle:
            handle.write(out)
        print('patch applied  %-30s %+d bytes  (%s)'
              % (filename, len(out) - len(data), 'CRLF' if is_crlf else 'LF'))

    print('')
    print('NEXT, in order:')
    print('  1. python constants_change_report.py')
    print('     Expect exit 0. exoplanet_coordinates.py is not')
    print('     constants_new.py, so this run should report no changes')
    print('     at all -- the DERIVED case is exercised by the values')
    print('     L-249 adds, not by this patch.')
    print('  2. python maintenance_run.py')
    print('')
    print('NOT SWEPT, deliberately: 3.26156 at 36 sites across 11')
    print('modules. That is L-248 and it goes out as one job.')


if __name__ == '__main__':
    main()
