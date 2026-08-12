"""
test_cross_checked.py - Regression tests for cross-check annotations.

Pins the L-156 Phase 2 (D4) mechanism in provenance_scanner.py: a claim
that already carries source evidence AND two annotation lines naming
distinct checkers scores V_CROSS_CHECKED (V2). Everything short of that
scores what it would have scored anyway.

Run from the project directory:
    python test_cross_checked.py

Exits 0 if all tests pass, non-zero on any failure.

Why these particular tests:
    Most of the load-bearing behavior here is NEGATIVE, and negatives
    fail silently. A parser that accepts too much does not produce an
    error -- it produces V2 findings that look verified in the audit
    while nobody checked anything. So the majority of these tests assert
    that something does NOT happen: an annotation without a reference
    earns nothing, one checker twice is not two checkers, a prose date
    is not an ISO date, and the phrase "cross-checked" in ordinary prose
    is not an annotation at all.

    That last one is not hypothetical. planet_visualization_utilities.py
    already contains the words "Giants cross-checked to Voyager 2" in a
    comment. The required colon is the only thing separating a live
    comment in the codebase from a false positive, so it gets its own
    test against the real file rather than a paraphrase of it.

Design (matches test_citation_inheritance.py):
    - Plain assert functions, no pytest/unittest dependency
    - Fixtures live INSIDE function bodies, never at module level. The
      scanner scans its own project directory, and a module-level string
      or dict carrying claim-shaped text would add findings to this
      file's own audit entry.
    - main() runs all tests and prints a pass/fail summary

Module created: August 2026 with Anthropic's Claude Opus 5.

Role: devtool
Domain: dev_tools
"""

import os
import sys
import tempfile
import traceback

from provenance_scanner import (
    CROSS_CHECK_ISSUES,
    ProvenanceUnit,
    V_CROSS_CHECKED,
    V_RECALLED,
    V_SOURCED,
    distinct_checker_identities,
    extract_units_from_file,
    has_citation,
    parse_cross_checks,
    score_unit,
)


# ============================================================
# HELPERS
# ============================================================

def _unit(context_text, raw_value=None, inherited_citation=None):
    """Build a synthetic display-string unit ready for score_unit().

    kind='string' keeps criticality on the public-facing branch, which
    needs no import map, so every scoring test can pass an empty one.
    """
    return ProvenanceUnit(
        kind='string',
        module='fixture_mod',
        file='fixture_mod.py',
        name=None,
        line_start=10,
        line_end=10,
        context_text=context_text,
        attached_text=context_text,
        attached_lines=(),
        raw_value=raw_value or 'fixture claim text',
        numeric_claims=[],
        role='data',
        is_docstring=False,
        inherited_citation=inherited_citation,
        scope_declined=False,
    )


def _scored(context_text, raw_value=None, inherited_citation=None):
    """Score a synthetic unit and hand it back."""
    unit = _unit(context_text, raw_value, inherited_citation)
    score_unit(unit, {})
    return unit


def _two_valid_annotations():
    """Two well-formed annotation lines naming different checkers."""
    return ("# Cross-checked: Gemini 2026-04-15 (worksheet_fixture.md)\n"
            "# Cross-checked: Claude 2026-08-01 (worksheet_fixture.md)")


def _identity(unit):
    """Stable finding identity: file, kind, name, content fingerprint."""
    return (unit.file, unit.kind, unit.name, unit.raw_value)


def _write_fixture(source):
    """Write a fixture module to a temp dir; return its path."""
    directory = tempfile.mkdtemp()
    path = os.path.join(directory, 'fixture_mod.py')
    with open(path, 'w') as handle:
        handle.write(source)
    return path


# ============================================================
# TESTS
# ============================================================

def test_full_v2_scoring():
    """Sourced plus two distinct valid annotations earns V2."""
    text = ("# Source: Fixture authority ALPHA\n"
            + _two_valid_annotations())
    unit = _scored(text)
    assert unit.vuln == V_CROSS_CHECKED, (
        f"expected V_CROSS_CHECKED, got V{unit.vuln}: {unit.vuln_reason}")
    assert 'Gemini' in unit.vuln_reason and 'Claude' in unit.vuln_reason, (
        f"reason should name both checkers, got: {unit.vuln_reason}")


def test_v2_with_inherited_citation():
    """An enclosing block's citation is source evidence for V2.

    The scanner already treats inherited citations as real sourcing when
    it assigns V3. Refusing them here would strand a legitimately
    cross-checked claim at V3 for a reason unrelated to the check.
    """
    text = _two_valid_annotations()
    unit = _scored(text, inherited_citation='# Source: enclosing block')
    assert not has_citation(text), (
        "fixture is broken: the annotation text must carry no citation "
        "of its own, or this tests nothing")
    assert unit.vuln == V_CROSS_CHECKED, (
        f"expected V_CROSS_CHECKED via inheritance, got V{unit.vuln}: "
        f"{unit.vuln_reason}")


def test_v2_requires_source_evidence():
    """Two valid annotations without any source stay at V4.

    A cross-check verifies a sourced claim; it is not a substitute for
    sourcing. Without this prerequisite an uncited claim carrying two
    annotations would jump V4 to V2 -- a stronger move than
    cite-to-clear, using the mechanism built to prevent it.
    """
    unit = _scored(_two_valid_annotations())
    assert unit.vuln == V_RECALLED, (
        f"expected V_RECALLED with no source, got V{unit.vuln}: "
        f"{unit.vuln_reason}")


def test_single_checker_is_incomplete():
    """One valid annotation on a sourced claim stays V3, and says so."""
    text = ("# Source: Fixture authority ALPHA\n"
            "# Cross-checked: Gemini 2026-04-15 (worksheet_fixture.md)")
    unit = _scored(text)
    assert unit.vuln == V_SOURCED, (
        f"expected V_SOURCED, got V{unit.vuln}")
    assert 'incomplete' in unit.vuln_reason.lower(), (
        f"reason should mark the incomplete state, got: {unit.vuln_reason}")


def test_same_identity_twice_is_not_two_checkers():
    """Two annotations naming one checker are one leg written twice."""
    text = ("# Source: Fixture authority ALPHA\n"
            "# Cross-checked: Gemini 2026-04-15 (worksheet_fixture.md)\n"
            "# Cross-checked: gemini 2026-06-02 (worksheet_other.md)")
    unit = _scored(text)
    assert unit.vuln == V_SOURCED, (
        f"expected V_SOURCED for a repeated identity, got V{unit.vuln}: "
        f"{unit.vuln_reason}")
    records, _issues = parse_cross_checks(text)
    assert len(records) == 2, "both lines should parse as valid records"
    assert len(distinct_checker_identities(records)) == 1, (
        "case and whitespace differences must not create a second checker")


def test_missing_reference_yields_no_record():
    """The anti-gaming rule: no parenthetical reference, no record.

    The claim keeps whatever its source status already gave it. The
    annotation is deliberately absent from SOURCE_PATTERNS, so it grants
    nothing on its own -- an unsourced claim carrying one stays at V4.
    """
    line = "# Cross-checked: Gemini 2026-04-15"
    records, issues = parse_cross_checks(line)
    assert records == [], f"expected no records, got {records}"
    assert issues and issues[0][1] == 'missing_reference', (
        f"expected missing_reference, got {issues}")
    unit = _scored(line)
    assert unit.vuln == V_RECALLED, (
        f"a bare annotation must not source anything, got V{unit.vuln}")


def test_trivial_reference_yields_no_record():
    """Empty and non-markdown references are both rejected."""
    empty = "# Cross-checked: Gemini 2026-04-15 ()"
    trivial = "# Cross-checked: Gemini 2026-04-15 (x)"
    for line, expected in ((empty, 'empty_reference'),
                           (trivial, 'non_markdown_reference')):
        records, issues = parse_cross_checks(line)
        assert records == [], f"expected no records for {line!r}"
        assert issues and issues[0][1] == expected, (
            f"expected {expected} for {line!r}, got {issues}")


def test_normal_citation_yields_no_records():
    """An ordinary citation is not an annotation."""
    records, issues = parse_cross_checks("# Source: NASA Planetary Fact Sheet")
    assert records == [] and issues == [], (
        f"a plain citation should parse as nothing, got {records} {issues}")


def test_voyager_line_is_not_an_annotation():
    """The live false positive in planet_visualization_utilities.py.

    Read from the real file rather than pasted here, so the test tracks
    the source instead of a copy that can silently drift away from it.
    If the comment is ever reworded this test still guards whatever
    replaced it, and if the file stops containing the phrase the test
    says so instead of passing vacuously.
    """
    target = 'planet_visualization_utilities.py'
    if not os.path.exists(target):
        raise AssertionError(f"{target} not found; run from the repo root")
    with open(target, 'rb') as handle:
        text = handle.read().decode('utf-8', 'replace')
    assert 'cross-checked' in text.lower(), (
        f"{target} no longer contains the phrase this test guards -- "
        "confirm the anchoring case still exists somewhere before "
        "deleting this test")
    records, issues = parse_cross_checks(text)
    assert records == [] and issues == [], (
        f"prose use of the phrase must not parse as an annotation: "
        f"{records} {issues}")


def test_case_insensitivity():
    """Lower and upper case annotation keywords both parse."""
    for line in ("  # cross-checked: gemini 2026-04-15 (worksheet.md)",
                 "# CROSS-CHECKED: GEMINI 2026-04-15 (WORKSHEET.MD)"):
        records, issues = parse_cross_checks(line)
        assert len(records) == 1, (
            f"expected one record for {line!r}, got {records} {issues}")


def test_iso_date_required():
    """Prose dates are rejected, ISO dates in three widths accepted.

    A prose date still contains a four-digit year, so a year test alone
    is not enough -- "Gemini April 2026" would split into the identity
    "Gemini April" and the date "2026". That is not a cosmetic mis-parse:
    two annotations from one checker in different months would then read
    as two distinct identities and earn V2 by themselves.
    """
    for line in ("# Cross-checked: Gemini (worksheet.md)",):
        records, issues = parse_cross_checks(line)
        assert records == [] and issues[0][1] == 'missing_year', (
            f"expected missing_year for {line!r}, got {records} {issues}")

    for line in ("# Cross-checked: Gemini April 2026 (worksheet.md)",
                 "# Cross-checked: Gemini 15 April 2026 (worksheet.md)"):
        records, issues = parse_cross_checks(line)
        assert records == [] and issues[0][1] == 'prose_date', (
            f"expected prose_date for {line!r}, got {records} {issues}")

    for line in ("# Cross-checked: Gemini 2026 (worksheet.md)",
                 "# Cross-checked: Gemini 2026-04 (worksheet.md)",
                 "# Cross-checked: Gemini 2026-04-15 (worksheet.md)"):
        records, _issues = parse_cross_checks(line)
        assert len(records) == 1 and records[0][0] == 'Gemini', (
            f"expected a clean ISO parse for {line!r}, got {records}")


def test_staleness_interaction():
    """A stale marker does not block V2; it is carried in the reason.

    Cross-checking establishes the value was right on the check date.
    Staleness says it may have moved since. Both are worth recording, so
    one does not overwrite the other.
    """
    text = ("# Source: Fixture authority ALPHA\n"
            "# Currently operating\n"
            + _two_valid_annotations())
    unit = _scored(text)
    assert unit.vuln == V_CROSS_CHECKED, (
        f"staleness must not block V2, got V{unit.vuln}")
    assert 'date-sensitive' in unit.vuln_reason, (
        f"reason should carry the staleness, got: {unit.vuln_reason}")


def test_population_conservation_by_identity():
    """Annotating a claim moves its score, never its identity.

    Total finding counts are the wrong instrument here -- they would
    also stay level if one finding vanished and another appeared. The
    identity key is what actually holds.
    """
    claim = "The fixture shell sits at some measured distance."
    plain = _scored("# Source: Fixture authority ALPHA", raw_value=claim)
    annotated = _scored(
        "# Source: Fixture authority ALPHA\n" + _two_valid_annotations(),
        raw_value=claim)
    assert _identity(plain) == _identity(annotated), (
        "the finding identity must not change when an annotation is added")
    assert plain.vuln == V_SOURCED and annotated.vuln == V_CROSS_CHECKED, (
        f"expected V3 then V2, got V{plain.vuln} then V{annotated.vuln}")
    assert annotated.score < plain.score, (
        "a cross-checked claim should score lower, not higher")


def test_lookback_window_bleed_is_closed():
    """An annotation reaches ONLY the claim whose statement it touches.

    Until L-192 this test asserted the opposite, and was right to.
    The flat context block carried an annotation to every claim inside
    it, so a separately sourced claim a few lines below an annotated
    one read that annotation too and received V2 without anyone having
    checked it. The mechanism was pinned here on purpose rather than
    left to inference.

    Credit now comes from the comment run touching a claim's own
    statement, so the near neighbour holds at V3. Both halves stay
    pinned -- near and far -- because a rule that only works at
    distance is the old behaviour wearing a new name.
    """
    def build(gap_lines):
        filler = "\n".join("# filler" for _ in range(gap_lines))
        return ('"""fixture."""\n\n'
                '# Source: Fixture authority ALPHA\n'
                + _two_valid_annotations() + '\n'
                'ANNOTATED = "Annotated shell sits at 71492 km."\n\n'
                + filler + '\n\n'
                '# Source: Fixture authority BETA\n'
                'NEIGHBOR = "Neighbour shell sits at 60268 km."\n')

    def neighbour_vuln(gap_lines):
        path = _write_fixture(build(gap_lines))
        units = extract_units_from_file(path, 'fixture_mod', 'data')
        for unit in units:
            score_unit(unit, {})
        assert len(units) == 2, (
            f"fixture should yield two units, got {len(units)}")
        return max(units, key=lambda u: u.line_start).vuln

    assert neighbour_vuln(5) == V_SOURCED, (
        "the near neighbour must NOT inherit an annotation written for "
        "another claim; if this fails, credit is flowing through the "
        "context window again (L-192)")
    assert neighbour_vuln(80) == V_SOURCED, (
        "a claim well beyond the window must not see the annotation")


def test_legacy_source_first_is_refused():
    """The retired source-first order earns nothing and says why.

    Both variants are covered. When the source carries its own year that
    year is taken as the check date and the checker falls outside the
    identity; when it does not, the whole prefix parses as the identity.
    Neither may quietly become a record.
    """
    for line in ("# Cross-checked: Hauck et al. 2013 via GPT 2026-08-03 "
                 "(worksheet.md)",
                 "# Cross-checked: IAU B2 via Claude 2026-08-02 "
                 "(worksheet.md)"):
        records, issues = parse_cross_checks(line)
        assert not records, (
            "source-first line must not parse as a record: %s" % line)
        assert issues and issues[0][1] == 'legacy_source_first', (
            "expected legacy_source_first, got %r for %s"
            % (issues, line))


def test_source_clause_after_date_is_accepted():
    """Checker-first parses, with and without the source clause.

    The ` -- <source>` clause is optional by design; the bare form has
    been the tested shape since the parser was written. Anything else
    between the date and the reference is refused.
    """
    with_source = ("# Cross-checked: GPT 2026-08-03 -- Hauck et al. 2013 "
                   "(worksheet.md)")
    records, issues = parse_cross_checks(with_source)
    assert len(records) == 1 and records[0][0] == 'GPT', (
        "checker-first with a source clause should parse to GPT, got %r"
        % (records,))
    assert not issues, "well-formed line raised issues: %r" % (issues,)

    bare = "# Cross-checked: Gemini 2026-04-15 (worksheet.md)"
    records, issues = parse_cross_checks(bare)
    assert len(records) == 1 and records[0][0] == 'Gemini', (
        "bare checker-first should parse to Gemini, got %r" % (records,))
    assert not issues, "bare line raised issues: %r" % (issues,)

    junk = "# Cross-checked: GPT 2026-08-03 Hauck et al. (worksheet.md)"
    records, issues = parse_cross_checks(junk)
    assert not records, "unseparated tail must not parse: %r" % (records,)
    assert issues and issues[0][1] == 'malformed_tail', (
        "expected malformed_tail, got %r" % (issues,))


def test_parse_issue_codes():
    """Every rejection reports which rule it broke.

    A malformed annotation that vanished silently would read, to anyone
    skimming the source, exactly like a completed cross-check. The issue
    list is what puts it in the audit instead.
    """
    del CROSS_CHECK_ISSUES[:]
    expected = {
        "# Cross-checked: Gemini (worksheet.md)": 'missing_year',
        "# Cross-checked: Gemini April 2026 (worksheet.md)": 'prose_date',
        "# Cross-checked: 2026-04-15 (worksheet.md)": 'missing_identity',
        "# Cross-checked: Gemini 2026-04-15": 'missing_reference',
        "# Cross-checked: Gemini 2026-04-15 ()": 'empty_reference',
        "# Cross-checked: Gemini 2026-04-15 (x)": 'non_markdown_reference',
    }
    for line, code in expected.items():
        _records, issues = parse_cross_checks(line)
        assert len(issues) == 1 and issues[0][1] == code, (
            f"expected {code} for {line!r}, got {issues}")

    del CROSS_CHECK_ISSUES[:]
    _scored("# Source: Fixture authority ALPHA\n"
            "# Cross-checked: Gemini 2026-04-15")
    codes = {entry[2] for entry in CROSS_CHECK_ISSUES}
    assert 'missing_reference' in codes, (
        f"score_unit should surface parse issues, got {CROSS_CHECK_ISSUES}")

    del CROSS_CHECK_ISSUES[:]
    _scored(_two_valid_annotations())
    codes = {entry[2] for entry in CROSS_CHECK_ISSUES}
    assert 'unsourced_annotation' in codes, (
        f"an annotation on an unsourced claim should be reported, got "
        f"{CROSS_CHECK_ISSUES}")

    del CROSS_CHECK_ISSUES[:]
    _scored("# Source: Fixture authority ALPHA\n"
            "# Cross-checked: Gemini 2026-04-15 (worksheet_fixture.md)\n"
            "# Cross-checked: Gemini 2026-06-02 (worksheet_other.md)")
    codes = {entry[2] for entry in CROSS_CHECK_ISSUES}
    assert 'duplicate_identity' in codes, (
        f"a repeated checker identity should be reported, got "
        f"{CROSS_CHECK_ISSUES}")
    del CROSS_CHECK_ISSUES[:]


TESTS = [
    test_full_v2_scoring,
    test_v2_with_inherited_citation,
    test_v2_requires_source_evidence,
    test_single_checker_is_incomplete,
    test_same_identity_twice_is_not_two_checkers,
    test_missing_reference_yields_no_record,
    test_trivial_reference_yields_no_record,
    test_normal_citation_yields_no_records,
    test_voyager_line_is_not_an_annotation,
    test_case_insensitivity,
    test_iso_date_required,
    test_staleness_interaction,
    test_population_conservation_by_identity,
    test_lookback_window_bleed_is_closed,
    test_parse_issue_codes,
    test_legacy_source_first_is_refused,
    test_source_clause_after_date_is_accepted,
]


def main():
    print("=" * 70)
    print("Cross-check annotation tests (L-156 Phase 2 Piece 1)")
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

    print("\nAll cross-check annotation tests passed.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
