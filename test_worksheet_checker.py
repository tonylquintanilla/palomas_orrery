"""test_worksheet_checker.py -- L-192. Can each layer actually fail?

RUN COMMAND
-----------
Open this file in VS Code and click Run. It takes no arguments.

    python test_worksheet_checker.py

It is also a CHECKERS row in maintenance_run.py, so a normal
maintenance run includes it.

WHY IT EXISTS
-------------
A green result answers two questions at once and does not say which:
did this pass, or did it never run? The worksheet checker reports zero
identity mismatches across the whole corpus today, and zero is exactly
what a broken identity check also reports. So every layer here is
exercised twice -- once with evidence that should clear it and once
with an injected violation that must not clear it. A layer that cannot
be made to fail on demand is not being tested.

The second half pins the findings the checker produces against the
REAL corpus. Those are not synthetic: four constants whose values moved
after their check, and one annotation crediting a worksheet row that
records the check as not performed. If a refactor stops finding them,
this file goes red rather than the number quietly changing.

Role: devtool
Domain: dev_tools

Module created: August 2026 with Anthropic's Claude Opus 5.
"""

import os
import sys

import worksheet_checker as wc


PASSED = []
FAILED = []


def check(name, condition, detail=''):
    if condition:
        PASSED.append(name)
    else:
        FAILED.append((name, detail))


def table_from(text):
    """One markdown table written inline, parsed the production way."""
    tables = wc.parse_tables('synthetic.md', text)
    return tables[0] if tables else None


class FakeUnit(object):
    """The three fields the layers read off a scanner unit."""

    def __init__(self, kind='constant', value=None, value_str='',
                 raw_value='', line_start=1, claims=()):
        self.kind = kind
        self.value = value
        self.value_str = value_str
        self.raw_value = raw_value
        self.line_start = line_start
        self.numeric_claims = list(claims)
        self.display_name = 'unit'


def fake_claim(worksheet='worksheet_claude_thing.md', checker='Claude',
               label='TEST_RADIUS_KM', unit=None):
    return wc.Claim('mod', 'mod.py', unit or FakeUnit(), checker,
                    '2026-08-01', worksheet, label)


def codes(claim):
    return set(code for _layer, code, _detail in claim.findings)


# ============================================================
# COMPARISON -- exact or rounded, never a tolerance
# ============================================================

def test_comparison():
    # The Mercury case, and the reason a tolerance is refused. Both are
    # written to one decimal, so the coarser precision is one decimal,
    # and they still disagree.
    verdict, _ = wc.compare(2439.7, '2439.4 +/- 0.1 km')
    check('mercury precision disagreement is a MISMATCH',
          verdict == 'MISMATCH', verdict)

    # The symmetric case: the code carries a rounded display of a more
    # precise measurement. Reading that as a value error would report a
    # rounding as a finding.
    verdict, _ = wc.compare(243.0, '243.0226 days')
    check('a coarser code value matches a finer evidence value',
          verdict == 'MATCH', verdict)

    verdict, _ = wc.compare(700.0, '700-1200 km')
    check('a range is never a MATCH', verdict == 'RANGE', verdict)

    verdict, _ = wc.compare(0.246, '0.262 km')
    check('a moved value is a MISMATCH', verdict == 'MISMATCH', verdict)

    verdict, _ = wc.compare(5990000.0, '5.99 million km')
    check('a scale word is MATCHED_VIA_CONVERSION',
          verdict == 'CONVERSION', verdict)

    verdict, _ = wc.compare(1.0, 'no number here at all')
    check('a cell with no number announces NO_NUMBER',
          verdict == 'NO_NUMBER', verdict)


# ============================================================
# VERDICTS -- the token decides the class, the scope decides the target
# ============================================================

def test_verdicts():
    own, _tok, scope = wc.classify_verdict('**YES**')
    check('YES clears', own == wc.V_CONFIRMED, own)

    own, _tok, _s = wc.classify_verdict('**PARTIAL**')
    check('PARTIAL is INCOMPLETE, not a pass',
          own == wc.V_INCOMPLETE, own)

    own, _tok, _s = wc.classify_verdict('**APPROX**')
    check('APPROX is INCOMPLETE, not a pass',
          own == wc.V_INCOMPLETE, own)

    own, _tok, _s = wc.classify_verdict('**DERIVED -- verified**')
    check('DERIVED survives a compound token',
          own == wc.V_DERIVED, own)

    # The 2026-08-13 ruling: seven tokens, and a word outside them goes
    # back rather than being translated. WRONG CITATION and WRONG VALUE
    # were invented at the keyboard -- they exist only because a
    # worksheet had one verdict column, and the two-column schema says
    # which one is wrong without a compound word for it.
    own, _tok, _s = wc.classify_verdict('**WRONG CITATION**',
                                        wc.SCOPE_VALUE)
    check('an invented token is UNREADABLE, not translated',
          own == wc.V_UNREADABLE, own)

    own, _tok, _s = wc.classify_verdict('**NOT FOUND**', wc.SCOPE_CITATION)
    check('NOT FOUND is UNREADABLE -- no prompt ever asked for it',
          own == wc.V_UNREADABLE, own)

    # UNSOURCED is the one survivor beyond the six: the tier2 prompt
    # commissioned it by name and ten cells on disk use it.
    own, _tok, scope = wc.classify_verdict('**UNSOURCED**',
                                           wc.SCOPE_VALUE)
    check('UNSOURCED survives, scoped to the citation',
          own == wc.V_SOURCE_ABSENT and scope == wc.SCOPE_CITATION,
          '%s / %s' % (own, scope))

    # A qualification must not be trimmed away in silence.
    check('a token plus prose is flagged compound',
          wc.is_compound('**YES** -- fully confirmed at 3 dp'))
    check('a bare token is not compound',
          not wc.is_compound('**YES**'))

    # Quoting is transcription, and transcription that fuses with the
    # tool's own words is not transcription. A live finding once read
    # "reads NO -- wrong authority -- wrong authority for a value that
    # may still be right" with no way to tell evidence from template.
    quote = wc.quoted('NO -- wrong authority')
    check('a quoted cell is delimited from the tool text',
          quote.startswith('<<') and quote.endswith('>>'), quote)

    long_quote = wc.quoted('x' * (wc.QUOTE_LIMIT + 40))
    check('a long quote is cut with a visible marker',
          '[...]' in long_quote and len(long_quote) < wc.QUOTE_LIMIT + 40,
          len(long_quote))

    own, _tok, _s = wc.classify_verdict('mostly fine I think')
    check('an unvocabularied cell is UNREADABLE, not a pass',
          own == wc.V_UNREADABLE, own)

    own, _tok, _s = wc.classify_verdict('')
    check('a blank verdict cell is EMPTY, not a pass',
          own == wc.V_EMPTY, own)


# ============================================================
# THE HEADER REGISTRY
# ============================================================

VALUE_TABLE = """
| # | Constant | Code value | Your value | Value correct? | Notes |
|---|---|---|---|---|---|
| 1 | `TEST_RADIUS_KM` | 100.0 | 100.0 | **YES** | fine |
"""

CITATION_ONLY_TABLE = """
| # | Constant | Value | Cited source | Citation correct? | Notes |
|---|---|---|---|---|---|
| 1 | `TEST_RADIUS_KM` | 100.0 | IAU B3 | **YES** | fine |
"""

AUXILIARY_TABLE = """
| Basis | r_H |
|---|---|
| perihelion | 8.0 Mkm |
"""


def test_registry():
    table = table_from(VALUE_TABLE)
    check('a value table is a row table', table.is_row_table)
    check('an underscore in a constant name survives cell stripping',
          wc.strip_cell('`TEST_RADIUS_KM`') == 'TEST_RADIUS_KM',
          wc.strip_cell('`TEST_RADIUS_KM`'))

    table = table_from(AUXILIARY_TABLE)
    check('a basis comparison is not a row table',
          not table.is_row_table)
    check('its unknown headers are recorded rather than dropped',
          'Basis' in table.unregistered, table.unregistered)

    table = table_from(CITATION_ONLY_TABLE)
    _own, _tok, _scope, column = wc.read_verdict(table, table.rows[0][1])
    check('a citation-only table reports which column it read',
          column == 'citation-only', column)


# ============================================================
# THE LAYERS, EACH SHOWN TO FAIL
# ============================================================

def run_layers(sheet_text, worksheet='worksheet_claude_thing.md',
               checker='Claude', value=100.0, value_str='100.0'):
    sheets = {worksheet: {'path': worksheet,
                          'tables': wc.parse_tables(worksheet, sheet_text)}}
    claim = fake_claim(worksheet, checker,
                       unit=FakeUnit(value=value, value_str=value_str))
    wc.check_claim(claim, sheets, set())
    return claim


def test_layers():
    # L0 -- the named worksheet is not on disk.
    claim = fake_claim('worksheet_that_does_not_exist.md')
    wc.check_claim(claim, {}, set())
    check('L0 fails on a missing worksheet',
          'MISSING_WORKSHEET' in codes(claim), codes(claim))
    check('a missing worksheet routes to SEND BACK',
          claim.route == 'SEND BACK', claim.route)

    # LID -- the injected violation Fable named: an annotation crediting
    # one model over another model's evidence. Zero of these exist in
    # the corpus, which is exactly why the check needs proving.
    claim = run_layers(VALUE_TABLE, checker='Gemini')
    check('LID catches Gemini crediting a Claude worksheet',
          'IDENTITY_MISMATCH' in codes(claim), codes(claim))

    claim = run_layers(VALUE_TABLE, checker='Claude')
    check('LID clears when the worksheet names the checker',
          'IDENTITY_MISMATCH' not in codes(claim), codes(claim))

    # L1 -- no row is about this value.
    claim = run_layers("""
| # | Constant | Code value | Your value | Value correct? |
|---|---|---|---|---|
| 1 | `SOMETHING_ELSE_KM` | 5.0 | 5.0 | **YES** |
""")
    check('L1 fails when no row is about the value',
          'UNMATCHED' in codes(claim), codes(claim))

    # L1 -- a worksheet with no readable table at all.
    claim = run_layers(AUXILIARY_TABLE)
    check('L1 announces a worksheet it cannot read',
          'WORKSHEET_UNREADABLE' in codes(claim), codes(claim))

    # L2a -- the code and its own evidence disagree.
    claim = run_layers("""
| # | Constant | Code value | Your value | Value correct? |
|---|---|---|---|---|
| 1 | `TEST_RADIUS_KM` | 100.0 | 137.5 | **YES** |
""")
    check('L2a fails when the evidence disagrees',
          'MISMATCH' in codes(claim), codes(claim))
    check('a disagreement routes to CONVERSATION, not SEND BACK',
          claim.route == 'CONVERSATION', claim.route)

    # L2b -- the value moved after the check. This is the
    # committed-history failure nothing else here can reach.
    claim = run_layers("""
| # | Constant | Code value | Your value | Value correct? |
|---|---|---|---|---|
| 1 | `TEST_RADIUS_KM` | 137.5 | 100.0 | **YES** |
""")
    check('L2b fails when the code moved since the check',
          'DRIFTED' in codes(claim), codes(claim))

    # L3 -- the Oort shape: an annotation asserting a completed check
    # over a row that records the check as not performed.
    claim = run_layers("""
| # | Constant | Code value | Your value | Value correct? |
|---|---|---|---|---|
| 1 | `TEST_RADIUS_KM` | 100.0 | 100.0 | **UNVERIFIED** |
""")
    check('L3 fails on a row recording no check',
          'CHECK_NOT_PERFORMED' in codes(claim), codes(claim))
    check('a not-performed check routes to SEND BACK',
          claim.route == 'SEND BACK', claim.route)

    # L3 -- PARTIAL goes back unconditionally, without first asking
    # why the row is qualified.
    claim = run_layers("""
| # | Constant | Code value | Your value | Value correct? |
|---|---|---|---|---|
| 1 | `TEST_RADIUS_KM` | 100.0 | 100.0 | **PARTIAL** |
""")
    check('PARTIAL returns to the originator',
          'INCOMPLETE_CHECK' in codes(claim), codes(claim))
    check('PARTIAL routes to SEND BACK', claim.route == 'SEND BACK',
          claim.route)

    # L3 -- DERIVED is never cleared and never sent back. It hands the
    # question to its weakest input, which is a conversation.
    claim = run_layers("""
| # | Constant | Code value | Your value | Value correct? |
|---|---|---|---|---|
| 1 | `TEST_RADIUS_KM` | 100.0 | 100.0 | **DERIVED** |
""")
    check('DERIVED is routed, not cleared',
          'DERIVED' in codes(claim), codes(claim))
    check('DERIVED routes to CONVERSATION, not SEND BACK',
          claim.route == 'CONVERSATION', claim.route)

    # A clean row clears every layer. Without this the suite could pass
    # by failing everything.
    claim = run_layers(VALUE_TABLE)
    check('a complete agreeing row produces no finding',
          not claim.findings,
          [(c, d) for _l, c, d in claim.findings])


# ============================================================
# DISPLAY INSTRUCTIONS ARE NOT CLAIMS ABOUT THE WORLD
# ============================================================

def test_display_instructions():
    unit = FakeUnit(
        kind='string',
        raw_value=('USE MANUAL SCALED OF 0.005 AU TO VIEW CLOSELY.'
                   '4.6 MB PER FRAME FOR HTML.\n\n'
                   'The core radius is about 1700 km.'))
    values, dropped = wc.physical_claims(unit)
    numbers = [value for value, _raw in values]
    check('a manual-scale instruction is not counted as a claim',
          0.005 not in numbers, numbers)
    check('the science claim survives the filter', 1700.0 in numbers,
          numbers)
    check('excluded instructions are counted, not silently dropped',
          dropped >= 1, dropped)


# ============================================================
# THE LIVE CORPUS -- pin what the checker actually finds
# ============================================================

DRIFTED_CONSTANTS = ('HELIOPAUSE_RADII', 'BENNU_RADIUS_KM',
                     'HAUMEA_RADIUS_KM', 'ARROKOTH_RADIUS_KM')


def test_live_corpus(project_dir):
    sheets = wc.load_worksheets(project_dir)
    claims, unreached, files = wc.collect_claims(project_dir)
    unregistered = set()
    for claim in claims:
        wc.check_claim(claim, sheets, unregistered)

    check('the checker reads the whole python corpus', files > 50, files)
    check('annotations are found at all', len(claims) > 50, len(claims))

    drifted = set()
    not_performed = set()
    for claim in claims:
        for _layer, code, _detail in claim.findings:
            if code == 'DRIFTED':
                drifted.add(claim.label)
            if code == 'CHECK_NOT_PERFORMED':
                not_performed.add(claim.label)

    for name in DRIFTED_CONSTANTS:
        check('L2b still finds the drift in %s' % name,
              name in drifted, sorted(drifted))

    check('L3 still finds BENNU_RADIUS_KM crediting an unperformed check',
          'BENNU_RADIUS_KM' in not_performed, sorted(not_performed))

    # The blind spot has to stay visible. If this reaches zero because
    # somebody stopped collecting it rather than because the scanner
    # started reaching those lines, the count moving is the signal.
    check('annotation lines outside scanner reach are still reported',
          len(unreached) > 0, len(unreached))


# ============================================================
# MAIN
# ============================================================

def main():
    project_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_dir)

    print('=' * 70)
    print('WORKSHEET CHECKER TESTS -- can each layer fail? (L-192)')
    print('=' * 70)

    test_comparison()
    test_verdicts()
    test_registry()
    test_layers()
    test_display_instructions()
    test_live_corpus(project_dir)

    for name, detail in FAILED:
        print('  FAIL  %s' % name)
        if detail != '':
            print('        got: %s' % (detail,))

    total = len(PASSED) + len(FAILED)
    print('-' * 70)
    if FAILED:
        print('%d of %d checks FAILED' % (len(FAILED), total))
        return 1
    print('All %d checks passed' % total)
    return 0


if __name__ == '__main__':
    sys.exit(main())
