"""
test_provenance_1d.py - Regression tests for the Phase 1d/1e changes.

Pins three recognition changes in provenance_scanner.py (ledger L-156,
sub-steps 1d and 1e):

  1. Shadow-constant detection (Gap item 5 / L-158). Local copies of
     values already defined and cited in constants_new.py.
  2. Author-year citation forms (Gap item 7). Genuinely cited values
     were scoring V4 RECALLED because has_citation() did not recognise
     a parenthetical reference.
  3. Fahrenheit/Celsius units (L-078(d)).

Plus the 1e tier-label change.

Run from the project directory:
    python test_provenance_1d.py

Exits 0 if all tests pass, non-zero on any failure.

Why these particular tests:
    Two of the three changes are regexes, and a regex that is too loose
    fails silently -- it clears findings by matching things it should
    not, and the tier totals move in the direction that looks like
    success. So roughly half the tests below are NEGATIVE: assertions
    that specific non-citations are still rejected, that a coincidental
    value match is not called a shadow constant, and that plain angular
    degrees are still angular degrees.

Design (matches test_constants_provenance.py and
test_citation_inheritance.py):
    - Plain assert functions, no pytest/unittest dependency
    - Synthetic fixtures where possible, so tests survive edits to the
      files that motivated them
    - main() runs all tests and prints a pass/fail summary

Module created: July 2026 with Anthropic's Claude Opus 5.

Role: devtool
Domain: dev_tools
"""

import ast
import os
import sys
import tempfile
import traceback

from provenance_scanner import (
    SHADOW_CONSTANTS,
    SHADOW_DERIVED_MIN_MAGNITUDE,
    build_cited_constant_names,
    build_pinned_values,
    constant_has_own_citation,
    extract_numeric_claims,
    has_citation,
    scan_shadow_constants,
)


# ============================================================
# HELPERS
# ============================================================

def _sandbox(files):
    """Write a dict of {filename: text} into a temp dir, return the path."""
    tmp = tempfile.mkdtemp(prefix='prov1d_')
    for name, text in files.items():
        with open(os.path.join(tmp, name), 'w', encoding='ascii') as f:
            f.write(text)
    return tmp


CONSTANTS_FIXTURE = '''\
# Source: IAU 2015 Resolution B3
SUN_RADIUS_KM = 695700.0

# Source: IAU 2012 Resolution B2
KM_PER_AU = 149597870.7

# No citation above this one, so it must not be treated as pinned.
UNCITED_VALUE = 4242.0

# Source: some real reference
SMALL_COUNT = 2.0
'''


def _run_scan(extra_files):
    """Build a sandbox with constants_new.py plus extras, run the scan."""
    files = {'constants_new.py': CONSTANTS_FIXTURE}
    files.update(extra_files)
    tmp = _sandbox(files)
    named = build_cited_constant_names(tmp)
    pinned = set()
    for value in named.values():
        for prec in (0, 1, 2, 3):
            pinned.add(round(value, prec))
    del SHADOW_CONSTANTS[:]
    scan_shadow_constants(tmp, named, pinned)
    return list(SHADOW_CONSTANTS)


# ============================================================
# TESTS -- shadow constants
# ============================================================

def test_direct_shadow_is_detected():
    """A local copy with the same NAME and VALUE is flagged."""
    hits = _run_scan({'user.py': 'def f():\n    SUN_RADIUS_KM = 695700.0\n'})
    names = [h[2] for h in hits]
    assert 'SUN_RADIUS_KM' in names, f"direct shadow missed; got {hits}"
    kinds = [h[3] for h in hits if h[2] == 'SUN_RADIUS_KM']
    assert 'direct' in kinds


def test_function_local_shadow_is_detected():
    """Detection reaches inside functions.

    This is the whole reason the detector exists as a separate scan
    rather than an amendment to Option A: all three known instances are
    function-local, and extract_units_from_file only reads top-level
    assignments, so they are invisible to the normal unit pipeline.
    """
    src = ('def outer():\n'
           '    def inner():\n'
           '        KM_PER_AU = 149597870.7\n'
           '        return KM_PER_AU\n'
           '    return inner\n')
    hits = _run_scan({'user.py': src})
    assert any(h[2] == 'KM_PER_AU' for h in hits), \
        f"nested function-local shadow missed; got {hits}"


def test_value_match_without_name_match_is_not_flagged():
    """A coincidental value under a different name is NOT a shadow.

    The load-bearing negative. Measured repo-wide when this was written:
    matching on value alone produced 77 candidates, almost all
    coincidental round numbers; matching on name AND value produced
    exactly the 2 real instances. If this test fails, the detector has
    become a noise generator and will be ignored, which is worse than
    not having it.
    """
    hits = _run_scan({'user.py': 'SOME_OTHER_NAME = 695700.0\n'})
    assert not hits, f"coincidental value match was flagged: {hits}"


def test_name_match_without_value_match_is_not_flagged():
    """Same name, different value -- not a frozen copy of anything."""
    hits = _run_scan({'user.py': 'SUN_RADIUS_KM = 12345.0\n'})
    assert not hits, f"name-only match was flagged: {hits}"


def test_uncited_constant_is_not_a_shadow_source():
    """Copies of UNCITED constants are not flagged.

    build_cited_constant_names only collects constants that carry a
    citation, mirroring build_pinned_values. Flagging a copy of an
    uncited value would assert a citation chain that does not exist at
    either end.
    """
    hits = _run_scan({'user.py': 'UNCITED_VALUE = 4242.0\n'})
    assert not hits, f"copy of an uncited constant was flagged: {hits}"


def test_constants_module_itself_is_excluded():
    """constants_new.py is the source of truth, not a shadow of itself."""
    hits = _run_scan({})
    assert not hits, f"constants_new.py flagged itself: {hits}"


def test_derived_shadow_is_detected():
    """A value recomputed from pinned literals is flagged."""
    src = 'def f():\n    SUN_RADIUS_AU = 695700.0 / 149597870.7\n'
    hits = _run_scan({'user.py': src})
    assert any(h[3] == 'derived' for h in hits), \
        f"derived shadow missed; got {hits}"


def test_trivial_derived_expression_is_not_flagged():
    """Small-integer arithmetic is not a frozen copy.

    Without the magnitude floor, an expression containing 2 twice
    matches, because 2.0 is itself a pinned constant. That produced a
    real false positive (SCHWARZSCHILD_RADIUS_METERS) during the build.
    """
    src = 'def f():\n    SOMETHING = 2.0 * 2.0\n'
    hits = _run_scan({'user.py': src})
    assert not hits, f"trivial small-integer expression flagged: {hits}"
    assert SHADOW_DERIVED_MIN_MAGNITUDE >= 100.0, \
        "magnitude floor lowered; trivial coincidences will return"


# ============================================================
# TESTS -- citation forms
# ============================================================

def test_author_year_citation_recognised():
    """Both live forms are recognised, with and without a year."""
    for text in ['# empirical limit (Vecellio et al.)',
                 '# thermodynamic limit (Sherwood & Huber)',
                 '# 31 degC = biological limit (Vecellio et al., 2022)',
                 '# 35 degC limit (Sherwood & Huber, 2010)',
                 '# rotation rate (Connerney 2022)',
                 '# semi-major axis (Brown & Butler 2023)',
                 '# lunar core (Weber et al. 2011)',
                 '# see (Smith and Jones 1999)']:
        assert has_citation(text), f"citation not recognised: {text!r}"


def test_date_parenthetical_is_not_a_citation():
    """(May 2026) is a date, not a reference.

    The load-bearing negative for this piece. A naive author-year
    pattern matched this on the first file in the repo during the
    build. A pattern that clears findings by reading dates as citations
    would be cite-to-clear implemented in a regex.
    """
    for text in ['# updated (May 2026)', '# added (April 2026)',
                 '# revised (Jan 2025)', '# checked (December 2024)']:
        assert not has_citation(text), \
            f"date parenthetical read as a citation: {text!r}"


def test_ordinary_parentheticals_are_not_citations():
    """Everyday parenthetical prose must not clear a finding."""
    for text in ['# Comet nucleus sizes (approximate, in km)',
                 '# radius (inner/outer, thickness)',
                 '# (see below)',
                 '# published (2022)',
                 '# full citation above ring_params (shim import)',
                 '# Roche limit (3.45 solar radii)']:
        assert not has_citation(text), \
            f"ordinary parenthetical read as a citation: {text!r}"


# ============================================================
# TESTS -- temperature units
# ============================================================

def test_temperature_units_recognised():
    """Fahrenheit and Celsius forms produce numeric claims."""
    for text, expect in [('31.0 degC', 31.0), ('100 degF', 100.0),
                         ('35 degrees C', 35.0), ('15 deg C', 15.0),
                         ('88 degrees F', 88.0),
                         ('5 degrees Celsius', 5.0)]:
        claims = list(extract_numeric_claims(text))
        assert claims, f"no claim extracted from {text!r}"
        assert claims[0][2] == expect, f"{text!r} -> {claims}"


def test_temperature_wins_over_angle():
    """'35 degrees C' is a temperature, not 35 angular degrees.

    Not a purely additive change: the generic degree alternative already
    matched this string, capturing the number and dropping the trailing
    C. The temperature alternatives must come FIRST in the alternation.
    """
    claims = list(extract_numeric_claims('35 degrees C'))
    assert claims and claims[0][1].strip().endswith('C'), \
        f"'35 degrees C' matched as {claims!r}, expected a temperature unit"


def test_plain_degrees_still_angular():
    """Angles are untouched -- no silent reclassification."""
    for text in ['45 degrees', '30 degrees north', '23.5 degrees tilt',
                 '12 deg']:
        claims = list(extract_numeric_claims(text))
        assert claims, f"angle claim lost: {text!r}"
        unit = claims[0][1].strip()
        assert unit in ('degrees', 'degree', 'deg'), \
            f"{text!r} reclassified to unit {unit!r}"


# ============================================================
# TESTS -- 1e tier labels
# ============================================================

def test_tier_labels_make_no_blanket_residual_claim():
    """No tier name asserts that its findings are already accepted.

    The old Tier-2 name was 'ALL ACCEPTED RESIDUALS', so the report
    template narrated every new finding in that band as already
    reviewed -- including the ones 1b had just moved there.
    """
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, 'provenance_scanner.py')
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        source = f.read()
    tree = ast.parse(source)

    banned = ('ALL ACCEPTED RESIDUALS', 'NO ACTION NEEDED',
              'no action required')
    for node in ast.walk(tree):
        if not isinstance(node, ast.Dict):
            continue
        for value in node.values:
            if not isinstance(value, ast.Tuple) or len(value.elts) != 2:
                continue
            label = value.elts[1]
            if not (isinstance(label, ast.Constant)
                    and isinstance(label.value, str)):
                continue
            for phrase in banned:
                assert phrase not in label.value, \
                    (f"tier label still asserts residual status: "
                     f"{label.value!r}")


# ============================================================
# TESTS -- the shared citation predicate
# ============================================================

import re as _re

_SRC_RE = _re.compile(r'#\s*[Ss]ource\s*:', _re.IGNORECASE)


def _lines(text):
    return text.splitlines(keepends=True)


def test_citation_below_assignment_counts():
    """constants_new.py's convention: citation on the following line."""
    src = _lines('X = 1.0\n# Source: a real reference\n')
    assert constant_has_own_citation(src, 1, _SRC_RE)


def test_citation_above_assignment_counts():
    """The rest of the codebase's convention: citation above."""
    src = _lines('# Source: a real reference\nX = 1.0\n')
    assert constant_has_own_citation(src, 2, _SRC_RE)


def test_blank_line_ends_the_run_below():
    """A blank line stops the search, so the NEXT constant's citation
    is not inherited.

    This is the bleed the predicate exists to prevent. With a distance
    window instead of contiguity, Y below would be scored as cited on
    the strength of Z's citation.
    """
    src = _lines('Y = 2.0\n'
                 '\n'
                 '# Source: this belongs to Z, not Y\n'
                 'Z = 3.0\n')
    assert not constant_has_own_citation(src, 1, _SRC_RE), \
        "Y inherited the citation belonging to Z"
    assert constant_has_own_citation(src, 4, _SRC_RE)


def test_preceding_code_ends_the_run_above():
    """Walking up stops at the previous assignment."""
    src = _lines('# Source: belongs to A\n'
                 'A = 1.0\n'
                 'B = 2.0\n')
    assert constant_has_own_citation(src, 2, _SRC_RE)
    assert not constant_has_own_citation(src, 3, _SRC_RE), \
        "B inherited the citation belonging to A"


def test_both_pinned_builders_agree():
    """The two callers must not diverge again.

    They answer the same question and now share one implementation. If
    this ever fails, one of them has grown its own rule back.
    """
    here = os.path.dirname(os.path.abspath(__file__))
    if not os.path.exists(os.path.join(here, 'constants_new.py')):
        print("    (skipped -- constants_new.py not found)")
        return

    pinned = build_pinned_values(here)
    named = build_cited_constant_names(here)
    from_names = set()
    for value in named.values():
        for prec in (0, 1, 2, 3):
            from_names.add(round(value, prec))

    assert pinned == from_names, (
        f"the two citation rules disagree: "
        f"{len(pinned - from_names)} only in build_pinned_values, "
        f"{len(from_names - pinned)} only in build_cited_constant_names")


# ============================================================
# RUNNER
# ============================================================

TESTS = [
    test_direct_shadow_is_detected,
    test_function_local_shadow_is_detected,
    test_value_match_without_name_match_is_not_flagged,
    test_name_match_without_value_match_is_not_flagged,
    test_uncited_constant_is_not_a_shadow_source,
    test_constants_module_itself_is_excluded,
    test_derived_shadow_is_detected,
    test_trivial_derived_expression_is_not_flagged,
    test_author_year_citation_recognised,
    test_date_parenthetical_is_not_a_citation,
    test_ordinary_parentheticals_are_not_citations,
    test_temperature_units_recognised,
    test_temperature_wins_over_angle,
    test_plain_degrees_still_angular,
    test_tier_labels_make_no_blanket_residual_claim,
    test_citation_below_assignment_counts,
    test_citation_above_assignment_counts,
    test_blank_line_ends_the_run_below,
    test_preceding_code_ends_the_run_above,
    test_both_pinned_builders_agree,
]


def main():
    print("=" * 70)
    print("Phase 1d/1e recognition tests (L-156) + citation predicate")
    print("=" * 70)

    passed = 0
    failures = []

    for test in TESTS:
        name = test.__name__
        try:
            test()
            passed += 1
            print(f"  PASS  {name}")
        except AssertionError as exc:
            failures.append((name, str(exc)))
            print(f"  FAIL  {name}")
        except Exception as exc:              # noqa: BLE001
            failures.append((name, f"Unexpected {type(exc).__name__}: {exc}"))
            print(f"  ERROR {name}")
            traceback.print_exc()

    print("=" * 70)
    print(f"Results: {passed} passed, {len(failures)} failed, "
          f"{len(TESTS)} total")

    if failures:
        print("\nFailure details:")
        for name, msg in failures:
            print(f"\n  {name}:")
            print(f"    {msg}")
        return 1

    print("\nAll Phase 1d/1e tests passed.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
