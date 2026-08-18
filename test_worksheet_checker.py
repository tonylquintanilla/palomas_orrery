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
Module updated: August 18, 2026 with Anthropic's Claude Opus 5 (L-207).
"""

import json
import os
import sys
import tempfile

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
# RULE 0 -- THE KEY, AND ITS REFUSAL TO FALL THROUGH
# ============================================================
#
# The key rule is INERT against today's corpus: no worksheet carries a
# Key column yet, so match_row never reaches rule 0 and the live run
# proves nothing about it. These are synthetic on purpose. Each is
# shown to produce its outcome AND, where it matters, shown not to
# produce the outcome it would have had without the rule.

KEY_TABLE = """
| # | Key | Claim | Code value | Your value | Source | Value correct? | Citation correct? | Notes |
|---|---|---|---|---|---|---|---|---|
| R1 | `worksheet_keys.py::compose` | the compose helper | 1.0 | 1.0 | somewhere | YES | YES | fine |
| R2 | `worksheet_keys.py::parse` | the parse helper | 2.0 | 2.0 | somewhere | YES | YES | fine |
"""

DUPLICATE_KEY_TABLE = """
| # | Key | Claim | Code value | Notes |
|---|---|---|---|---|
| R1 | `worksheet_keys.py::compose` | first | 1.0 | a |
| R2 | `worksheet_keys.py::compose` | second | 1.0 | b |
"""

# A prose-matchable row whose key names a function that does not
# exist. Without rule 0 the PROSE rule would match it happily; that is
# precisely the lucky hit a rename must not hide behind.
STALE_KEY_TABLE = """
| # | Key | Claim | Code value | Notes |
|---|---|---|---|---|
| R1 | `worksheet_keys.py::function_renamed_away` | the compose helper writes a key from its parts | 1.0 | a |
"""


def test_key_rule():
    table = table_from(KEY_TABLE)
    check('a Key header is recognised as a role',
          table.column(wc.ROLE_KEY) is not None, table.unregistered)

    row, rule, _note = wc.match_row(table, '', '', 1.0,
                                    'worksheet_keys.py::compose')
    check('an exact key match wins as rule KEY', rule == 'KEY', rule)
    check('and it picks the row that carries the key',
          row is not None and 'compose' in ' '.join(row[1]), row)

    _row, rule, note = wc.match_row(table, '', '', 1.0,
                                    'worksheet_keys.py::resolve')
    check('a resolvable key no row carries is KEY_ABSENT',
          rule == 'KEY_ABSENT', '%s %s' % (rule, note))

    table = table_from(DUPLICATE_KEY_TABLE)
    _row, rule, note = wc.match_row(table, '', '', 1.0,
                                    'worksheet_keys.py::compose')
    check('two rows under one key announce rather than pick',
          rule == 'AMBIGUOUS', '%s %s' % (rule, note))

    # The load-bearing one. The worksheet records a key minted before a
    # rename, so it no longer resolves; the claim now mints a different
    # key that no row carries. The prose in that row WOULD satisfy the
    # PROSE rule, so a fall-through would report a clean match and the
    # rename would never surface.
    table = table_from(STALE_KEY_TABLE)
    _row, rule, note = wc.match_row(
        table, '', 'the compose helper writes a key from its parts', 1.0,
        'worksheet_keys.py::compose')
    check('a key the worksheet carries that no longer resolves is '
          'KEY_STALE', rule == 'KEY_STALE', '%s %s' % (rule, note))
    check('and it does NOT fall through to a prose match',
          rule != 'PROSE', rule)

    # Same table, no key supplied: the prose match must still succeed,
    # or the previous check proves nothing -- it would be passing
    # because nothing matches rather than because rule 0 stopped it.
    _row, rule, _note = wc.match_row(
        table, '', 'the compose helper writes a key from its parts', 1.0)
    check('the same row DOES match on prose when no key is given',
          rule == 'PROSE', rule)


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

    # L2b, the other two outcomes. DRIFTED above earns its name only
    # because that row's verdict is YES: the worksheet confirmed 137.5
    # and the code left it anyway. Change the verdict and the same
    # movement means something else entirely.
    claim = run_layers("""
| # | Constant | Code value | Your value | Value correct? |
|---|---|---|---|---|
| 1 | `TEST_RADIUS_KM` | 137.5 | 100.0 | **NO -- does not follow** |
""")
    check('a value the worksheet REFUTED reports CORRECTED, not DRIFTED',
          'CORRECTED' in codes(claim) and 'DRIFTED' not in codes(claim),
          codes(claim))
    check('a correction is recorded but not routed back',
          claim.route != 'SEND BACK', claim.route)

    claim = run_layers("""
| # | Constant | Code value | Your value | Value correct? |
|---|---|---|---|---|
| 1 | `TEST_RADIUS_KM` | 137.5 | 100.0 | **UNVERIFIED** |
""")
    check('a value nobody checked reports UNCHECKED_MOVE',
          'UNCHECKED_MOVE' in codes(claim), codes(claim))

    # The live corpus case. A worksheet whose only verdict column asks
    # about the CITATION has not answered the value question at all, so
    # neither DRIFTED nor CORRECTED is honest -- and a NO here routinely
    # means 'wrong authority, value correct' (rows G4, G6, G7, G8).
    claim = run_layers("""
| # | Constant | Value | Cited source | Citation correct? |
|---|---|---|---|---|
| 1 | `TEST_RADIUS_KM` | 137.5 | Somebody et al. | **NO -- wrong authority** |
""")
    check('a citation-only verdict cannot clear or condemn a moved value',
          'UNCHECKED_MOVE' in codes(claim), codes(claim))

    # L3 -- a qualification is evidence. The clearing branch is the one
    # place a verdict produces no finding at all, so it is the only
    # place a reservation can disappear. No live claim currently sits
    # on a qualified YES, which is exactly why these two run: the guard
    # would otherwise be unfalsifiable on this corpus.
    claim = run_layers("""
| # | Constant | Code value | Your value | Value correct? | Notes |
|---|---|---|---|---|---|
| 1 | `TEST_RADIUS_KM` | 100.0 | 100.0 | **YES -- to 2 dp only** | fine |
""")
    check('a YES carrying a reservation does not read as clean',
          'QUALIFIED_PASS' in codes(claim), codes(claim))

    claim = run_layers(VALUE_TABLE)
    check('a bare YES still clears with no findings at all',
          not codes(claim), codes(claim))

    # L3 -- the same NO means opposite things in the same column.
    # 'wrong authority' says the value is fine; 'arithmetic error' says
    # the source is fine. The tool may not pick one, and until this
    # change it printed the first reading over both.
    claim = run_layers("""
| # | Constant | Value | Cited source | Citation correct? | Notes |
|---|---|---|---|---|---|
| 1 | `TEST_RADIUS_KM` | 100.0 | Somebody et al. | **NO -- arithmetic error** | x |
""")
    check('a qualified refusal is not classified as a citation defect',
          'REFUSAL_UNCLASSIFIED' in codes(claim)
          and 'CITATION_DEFECT' not in codes(claim), codes(claim))

    claim = run_layers("""
| # | Constant | Value | Cited source | Citation correct? | Notes |
|---|---|---|---|---|---|
| 1 | `TEST_RADIUS_KM` | 100.0 | Somebody et al. | **NO** | x |
""")
    check('a bare NO in a citation column is still a citation defect',
          'CITATION_DEFECT' in codes(claim), codes(claim))

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

# All four moved after their worksheets ran, and all four sit in
# worksheets whose only verdict column asks about the CITATION. So the
# tool cannot say whether the movement was a correction or a defect,
# and says so. Before 2026-08-15 it called all eight rows DRIFTED,
# which asserted the strongest of the three readings on no evidence.
UNCHECKED_MOVE_CONSTANTS = ('HELIOPAUSE_RADII', 'BENNU_RADIUS_KM',
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
    moved = set()
    not_performed = set()
    for claim in claims:
        for _layer, code, _detail in claim.findings:
            if code == 'DRIFTED':
                drifted.add(claim.label)
            if code in ('UNCHECKED_MOVE', 'CORRECTED'):
                moved.add(claim.label)
            if code == 'CHECK_NOT_PERFORMED':
                not_performed.add(claim.label)

    for name in UNCHECKED_MOVE_CONSTANTS:
        check('L2b still sees the movement in %s' % name,
              name in moved, sorted(moved))

    # The point of the change is that the strong word is now reserved.
    # If DRIFTED reappears in this corpus, a worksheet grew a value
    # verdict and a real defect is being reported -- read it, do not
    # relax this.
    check('no live claim is called DRIFTED without a value verdict',
          not drifted, sorted(drifted))

    # Seven live refusals carry their own reason and are no longer
    # reported as wrong-authority. If this reaches zero, either the
    # worksheets were re-cut or the qualification stopped being read.
    unclassified = sum(1 for c in claims
                       for _l, code, _d in c.findings
                       if code == 'REFUSAL_UNCLASSIFIED')
    check('qualified refusals are reported as unclassified',
          unclassified > 0, unclassified)

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

def _pilot_row(**overrides):
    """One returned row object, valid unless an override breaks it."""
    row = {
        'record': 'row',
        'id': 'R1',
        'key': 'constants_new.py::KM_PER_AU',
        'claim': 'KM_PER_AU',
        'code_value': '149597870.7',
        'your_value': '149597870.7',
        'source': 'IAU 2012 Resolution B2',
        'value_correct': 'yes',
        'citation_correct': 'yes',
        'notes': '',
    }
    row['hash'] = wc.row_hash(row['key'], row['claim'], row['code_value'])
    row.update(overrides)
    return row


def _as_jsonl(rows):
    return '\n'.join(json.dumps(r, sort_keys=True) for r in rows) + '\n'


def test_json_reader():
    """A JSON return becomes the same Table a markdown one does."""
    header = {'record': 'header', 'batch': 'test', 'selection': 'all'}
    text = _as_jsonl([header, _pilot_row(), _pilot_row(id='R2')])
    tables, integrity, unreadable = wc.parse_json_worksheet('r.jsonl', text)

    check('json: one table comes back', len(tables) == 1, len(tables))
    if not tables:
        return
    table = tables[0]
    check('json: the header line is not a row', len(table.rows) == 2,
          len(table.rows))
    check('json: it is a row table the layers will use',
          table.is_row_table, repr(table.roles))
    check('json: no column is unregistered', table.unregistered == [],
          repr(table.unregistered))
    check('json: the code value lands in the code column',
          table.cell(table.rows[0][1], wc.ROLE_CODE) == '149597870.7',
          table.cell(table.rows[0][1], wc.ROLE_CODE))
    check('json: the citation verdict lands in its own column',
          table.cell(table.rows[0][1], wc.ROLE_CITATION_VERDICT) == 'yes',
          table.cell(table.rows[0][1], wc.ROLE_CITATION_VERDICT))
    check('json: nothing unreadable in a clean return', unreadable == [],
          repr(unreadable))
    check('json: every row is hash-checked', len(integrity) == 2,
          repr(integrity))


def test_json_row_hash():
    """The hash catches an edited do-not-edit field, and its absence."""
    good = _pilot_row()
    status, _detail = wc.check_row_hash(good)
    check('hash: a clean row passes', status == 'ok', status)

    rounded = _pilot_row(code_value='149597871')
    status, detail = wc.check_row_hash(rounded)
    check('hash: a rounded code value is caught', status == 'mismatch',
          status)
    check('hash: the detail names the cause',
          'do-not-edit' in detail, detail)

    reflowed = _pilot_row(key='constants_new.py :: KM_PER_AU')
    check('hash: a reflowed key is caught',
          wc.check_row_hash(reflowed)[0] == 'mismatch', '')

    stripped = _pilot_row()
    del stripped['hash']
    check('hash: a MISSING hash fails rather than passing',
          wc.check_row_hash(stripped)[0] == 'missing',
          wc.check_row_hash(stripped)[0])

    blank = _pilot_row(hash='')
    check('hash: a blank hash fails too',
          wc.check_row_hash(blank)[0] == 'missing', '')

    # The builder and the checker each carry this function; they must
    # agree byte for byte or every returned row reads as modified.
    check('hash: eight characters, as the request states',
          len(wc.row_hash('a', 'b', 'c')) == 8, wc.row_hash('a', 'b', 'c'))


def test_json_truncation_is_salvaged_and_announced():
    """A return cut off mid-generation keeps its complete rows."""
    header = {'record': 'header', 'batch': 'test'}
    text = _as_jsonl([header, _pilot_row(), _pilot_row(id='R2')])
    cut = text.strip().split('\n')
    cut[-1] = cut[-1][:40]
    tables, integrity, unreadable = wc.parse_json_worksheet(
        'cut.jsonl', '\n'.join(cut) + '\n')

    check('truncation: the complete rows survive',
          tables and len(tables[0].rows) == 1,
          len(tables[0].rows) if tables else 0)
    check('truncation: the broken line is REPORTED, not dropped',
          len(unreadable) == 1, repr(unreadable))


def test_json_array_return_is_accepted():
    """A responder who returns an array instead of lines is still read."""
    rows = [{'record': 'header'}, _pilot_row(), _pilot_row(id='R2')]
    tables, _integrity, unreadable = wc.parse_json_worksheet(
        'array.json', json.dumps(rows))
    check('array: rows are read', tables and len(tables[0].rows) == 2,
          len(tables[0].rows) if tables else 0)
    check('array: nothing reported unreadable', unreadable == [],
          repr(unreadable))


def test_markdown_has_no_integrity_map():
    """A markdown worksheet is NOT APPLICABLE, not passed."""
    text = ('| Key | Claim | Code value | Value correct? |\n'
            '|---|---|---|---|\n'
            '| `k` | KM_PER_AU | 149597870.7 | yes |\n')
    tables = wc.parse_tables('sheet.md', text)
    check('markdown: still parses', len(tables) == 1, len(tables))
    check('markdown: carries no integrity map',
          tables[0].integrity is None, repr(tables[0].integrity))

    # The layer must not invent a failure for a format that never had
    # hashes. Seventeen historical worksheets are markdown.
    class Fake(object):
        def __init__(self):
            self.findings = []
            self.route = ''
            self.current_ordinal = None
            self.routed_ordinals = []

        def fail(self, layer, code, detail, route):
            self.findings.append((layer, code, detail))
            if route:
                self.route = route

    claim = Fake()
    wc.check_row_integrity(claim, tables[0], 3)
    check('markdown: the integrity layer records nothing',
          claim.findings == [], repr(claim.findings))


def test_integrity_layer_fails_a_bad_row():
    """LH routes a modified or unhashed row back.

    The NOT APPLICABLE case above is only half the layer. A mutation
    that made check_row_integrity return early for EVERY status passed
    all 96 checks, because nothing here had ever asked it to fail.
    """
    class Fake(object):
        def __init__(self):
            self.findings = []
            self.route = ''
            self.current_ordinal = None
            self.routed_ordinals = []

        def fail(self, layer, code, detail, route):
            self.findings.append((layer, code, detail))
            if route:
                self.route = route

    header = {'record': 'header'}
    rows = [_pilot_row(id='R1'),
            _pilot_row(id='R2', code_value='999'),
            _pilot_row(id='R3')]
    del rows[2]['hash']
    tables, _integrity, _bad = wc.parse_json_worksheet(
        'r.jsonl', _as_jsonl([header] + rows))
    table = tables[0]
    lines = [line_no for line_no, _cells in table.rows]

    clean = Fake()
    wc.check_row_integrity(clean, table, lines[0])
    check('LH: a clean row records nothing', clean.findings == [],
          repr(clean.findings))

    modified = Fake()
    wc.check_row_integrity(modified, table, lines[1])
    check('LH: a modified row is caught',
          [f[1] for f in modified.findings] == ['ROW_MODIFIED'],
          repr(modified.findings))
    check('LH: a modified row goes back',
          modified.route == 'SEND BACK', modified.route)

    unhashed = Fake()
    wc.check_row_integrity(unhashed, table, lines[2])
    check('LH: an unhashed row is caught',
          [f[1] for f in unhashed.findings] == ['ROW_HASH_MISSING'],
          repr(unhashed.findings))
    check('LH: an unhashed row goes back',
          unhashed.route == 'SEND BACK', unhashed.route)

    absent = Fake()
    wc.check_row_integrity(absent, table, 9999)
    check('LH: a row missing from the map is caught, not assumed fine',
          absent.route == 'SEND BACK', repr(absent.findings))


def test_routing_file(project_dir):
    """The routing file is written, and says what it contains."""
    scratch = tempfile.mkdtemp(prefix='routing_test_')
    written, error = wc.write_routing_file(scratch, [])
    check('routing: an empty run still writes the file',
          error == '' and written == 0, '%r %r' % (written, error))

    # Deliberately NOT the repo's own copy. Checking the repo file
    # proved only that some earlier run had written one -- a mutation
    # replacing the write with `pass` passed this test.
    path = os.path.join(scratch, wc.ROUTED_PATH)
    check('routing: the file exists', os.path.isfile(path), path)
    if not os.path.isfile(path):
        return
    with open(path, encoding='utf-8') as handle:
        payload = json.load(handle)
    check('routing: it names its writer',
          payload.get('written_by') == 'worksheet_checker.py',
          repr(payload.get('written_by')))
    check('routing: the key list is a list',
          isinstance(payload.get('send_back'), list),
          repr(type(payload.get('send_back'))))
    check('routing: the count matches the list',
          payload.get('send_back_count') == len(payload.get('send_back', [])),
          repr(payload.get('send_back_count')))

    # With real keys, so the returned count and the file agree on a
    # number that is not zero. A mutation returning a hard 0 passed
    # while every count in sight was already 0.
    class FakeClaim(object):
        def __init__(self, key, route):
            self._key = key
            self.route = route
            self.routed_ordinals = []

        def key(self, ordinal=None):
            return self._key

    claims = [FakeClaim('a.py::ONE', 'SEND BACK'),
              FakeClaim('a.py::TWO', 'SEND BACK'),
              FakeClaim('a.py::THREE', 'CONVERSATION')]
    written, error = wc.write_routing_file(scratch, claims)
    check('routing: only SEND BACK rows are written',
          written == 2 and error == '', '%r %r' % (written, error))
    with open(path, encoding='utf-8') as handle:
        payload = json.load(handle)
    check('routing: the file holds the two routed keys',
          payload.get('send_back') == ['a.py::ONE', 'a.py::TWO'],
          repr(payload.get('send_back')))
    check('routing: the returned count matches what was written',
          written == len(payload.get('send_back', [])),
          '%r vs %r' % (written, payload.get('send_back')))


def _resolved_project(leg_line, rows, sheet='worksheet_pilot.jsonl',
                      sheet_text=None):
    """A throwaway project: one module carrying a leg, one worksheet.

    Written into a fresh temporary directory on purpose. Checking the
    repo's own tree proved only that some earlier run had left the
    right state behind -- the defect that let a mutation replacing the
    routing write with `pass` pass its test.

    `sheet_text` writes the worksheet verbatim, which is how the
    markdown cases get a table whose columns this test chooses.
    """
    scratch = tempfile.mkdtemp(prefix='resolved_test_')
    os.makedirs(os.path.join(scratch, wc.WORKSHEET_DIR))
    with open(os.path.join(scratch, 'fixture_module.py'), 'w',
              encoding='utf-8', newline='\n') as handle:
        handle.write('VALUE = 1.0\n')
        handle.write(leg_line + '\n')
    with open(os.path.join(scratch, wc.WORKSHEET_DIR, sheet), 'w',
              encoding='utf-8', newline='\n') as handle:
        if sheet_text is not None:
            handle.write(sheet_text)
        else:
            for row in rows:
                handle.write(json.dumps(row) + '\n')
    return scratch


def _linked(scratch):
    """(legs, codes) after the linkage layer has run."""
    legs = wc.collect_resolved(scratch)
    worksheets = wc.load_worksheets(scratch)
    for leg in legs:
        wc.check_resolved(leg, worksheets)
    return legs, [code for leg in legs for code, _detail in leg.findings]


KEY = 'fixture_module.py::VALUE::c1'
GOOD_LEG = ('# Resolved: worksheet_pilot.jsonl %s -- citation refuted, '
            'Source replaced (L-204)' % KEY)


def _row(key=KEY, citation='NO'):
    """One returned row. NO is the vocabulary's refuted token.

    Deliberately a real token rather than the word REFUTED: the
    vocabulary is exact-match by ruling, and a fixture using a word the
    checker does not accept would test the fixture rather than the
    layer.
    """
    return {'key': key, 'claim': 'the claim', 'code_value': '1.0',
            'citation_correct': citation}


def test_resolved_linkage():
    """L-200 -- the leg links, and every way it can fail does fail."""
    legs, codes = _linked(_resolved_project(GOOD_LEG, [_row()]))
    check('resolved: one leg is collected', len(legs) == 1, repr(legs))
    check('resolved: a good leg links clean', codes == [], repr(codes))
    if legs:
        check('resolved: it carries the handle it names',
              legs[0].handle == 'L-204', repr(legs[0].handle))
        check('resolved: it reports the verdict class it found',
              legs[0].verdict == wc.V_REFUTED, repr(legs[0].verdict))

    # A leg naming a worksheet that is not on disk.
    missing_sheet = GOOD_LEG.replace('worksheet_pilot.jsonl',
                                     'worksheet_absent.jsonl')
    _legs, codes = _linked(_resolved_project(missing_sheet, [_row()]))
    check('resolved: a missing worksheet fails',
          codes == ['RESOLVED_WORKSHEET_MISSING'], repr(codes))

    # A leg naming a row no worksheet carries. This is the failure the
    # layer exists for: an edit attributed to a verdict nobody can find.
    _legs, codes = _linked(
        _resolved_project(GOOD_LEG, [_row(key='other.py::THING::c1')]))
    check('resolved: a row that does not exist fails',
          codes == ['RESOLVED_ROW_MISSING'], repr(codes))

    # A leg citing a row that CLEARED. Nothing needed editing, so the
    # leg does not explain the edit it is attached to.
    _legs, codes = _linked(
        _resolved_project(GOOD_LEG, [_row(citation='CONFIRMED')]))
    check('resolved: a cleared row fails',
          codes == ['RESOLVED_VERDICT_CLEAR'], repr(codes))

    # A row whose verdict cell is empty is not a pass.
    _legs, codes = _linked(
        _resolved_project(GOOD_LEG, [_row(citation='')]))
    check('resolved: an unreadable verdict fails',
          codes == ['RESOLVED_VERDICT_UNREADABLE'], repr(codes))

    # A worksheet with no citation-verdict column at all. This one has
    # to be markdown: the JSON reader synthesizes every column in
    # JSON_FIELD_HEADERS whether or not the return carried it, so a
    # JSON worksheet always HAS the column and an absent verdict shows
    # up as an empty cell instead.
    no_column = ('| Key | Claim | Value correct? |\n'
                 '|---|---|---|\n'
                 '| `%s` | the claim | YES |\n' % KEY)
    md_leg = GOOD_LEG.replace('worksheet_pilot.jsonl', 'worksheet_pilot.md')
    _legs, codes = _linked(
        _resolved_project(md_leg, [], sheet='worksheet_pilot.md',
                          sheet_text=no_column))
    check('resolved: a worksheet with no verdict column fails',
          codes == ['RESOLVED_NO_VERDICT_COLUMN'], repr(codes))

    # A leg that does not complete the grammar never reaches linkage.
    _legs, codes = _linked(
        _resolved_project('# Resolved: worksheet_pilot.jsonl', [_row()]))
    check('resolved: a malformed leg fails at the grammar',
          codes == ['RESOLVED_MALFORMED'], repr(codes))

    # And a corpus with no legs collects none, rather than erroring.
    legs, codes = _linked(_resolved_project('VALUE2 = 2.0', [_row()]))
    check('resolved: a corpus with no legs collects none',
          legs == [] and codes == [], repr(legs))


def test_suffix_sets_agree():
    """The two stores of "what a worksheet file looks like" agree.

    The scanner decides which references the annotation grammar
    accepts; the checker decides which files it parses as JSON. Nothing
    connected them, so a fourth format added in one place would be
    accepted in a citation and never read, or read and never citable.
    """
    expected = ('.md',) + wc.JSON_SUFFIXES
    check('suffixes: the scanner and the checker agree',
          set(expected) == set(wc.ps.WORKSHEET_REFERENCE_SUFFIXES),
          '%r vs %r' % (expected, wc.ps.WORKSHEET_REFERENCE_SUFFIXES))
    check('suffixes: markdown is still accepted',
          '.md' in wc.ps.WORKSHEET_REFERENCE_SUFFIXES,
          repr(wc.ps.WORKSHEET_REFERENCE_SUFFIXES))




def test_citation_prompt(project_dir):
    """The prompt is written, groups by key, and is reproducible."""

    class PromptUnit(object):
        def __init__(self, attached_text=''):
            self.attached_text = attached_text
            self.line_start = 12

    class PromptClaim(object):
        """The fields the emitter reads, and nothing else."""

        def __init__(self, key, checker, worksheet, rows, route='',
                     attached='# Source: IAU 2015 Resolution B3'):
            self._key = key
            self.checker = checker
            self.worksheet = worksheet
            self.citation_rows = rows
            self.route = route
            self.unit = PromptUnit(attached)
            self.where = 'constants_new.py:12'

        def key(self, ordinal=None):
            return self._key

    def captured(source='IAU B3', verdict='partial', ordinal=None):
        return {'ordinal': ordinal, 'claim_text': 'EARTH_RADIUS_KM',
                'code_value': '6378.137', 'source': source,
                'citation_verdict': verdict, 'notes': 'over-precise'}

    scratch = tempfile.mkdtemp(prefix='citation_prompt_')

    # An empty run still writes the file. Checking the repo's own copy
    # would prove only that some earlier run wrote one -- the mistake
    # test_routing_file records having made.
    written, not_included, error = wc.write_citation_prompt(scratch, [])
    path = os.path.join(scratch, wc.CITATION_PROMPT_PATH)
    check('citation prompt: an empty run still writes the file',
          error == '' and written == 0 and os.path.isfile(path),
          '%r %r %s' % (written, error, path))
    if not os.path.isfile(path):
        return
    with open(path, encoding='utf-8') as handle:
        header = json.loads(handle.readline())
    check('citation prompt: the header names its writer and its item',
          header.get('written_by') == 'worksheet_checker.py'
          and header.get('ledger_item') == 'L-207',
          repr(header.get('written_by')))
    check('citation prompt: the header carries an anchor',
          bool(header.get('built_on_sha')),
          repr(header.get('built_on_sha')))
    check('citation prompt: the vocabulary comes from the registry',
          any(entry['means'] == wc.V_SOURCE_ABSENT
              for entry in header.get('verdict_tokens', [])),
          repr(header.get('verdict_tokens')))

    # Two checkers, one site: ONE row carrying TWO responses. A row
    # per annotation would put the same key and the same hash on two
    # lines, which is a hash identifying nothing.
    claims = [
        PromptClaim('constants_new.py::EARTH_RADIUS_KM', 'Claude',
                    'worksheet_claude_constants_new.md',
                    [captured(source='IAU B3', verdict='partial')]),
        PromptClaim('constants_new.py::EARTH_RADIUS_KM', 'GPT',
                    'constants_new_citation_verification_gpt.md',
                    [captured(source='IERS 2010', verdict='no')],
                    route='CONVERSATION'),
    ]
    written, not_included, error = wc.write_citation_prompt(
        scratch, claims)
    with open(path, encoding='utf-8') as handle:
        lines = [json.loads(line) for line in handle if line.strip()]
    rows = [line for line in lines if line.get('record') == 'row']
    check('citation prompt: two legs on one site make one row',
          written == 1 and len(rows) == 1,
          '%r %r' % (written, len(rows)))
    if not rows:
        return
    row = rows[0]
    check('citation prompt: both responders are carried',
          len(row.get('responses', [])) == 2,
          repr(row.get('responses')))
    check('citation prompt: the responses are ordered by checker',
          [entry['checker'] for entry in row['responses']]
          == ['Claude', 'GPT'],
          repr([entry['checker'] for entry in row['responses']]))
    check("citation prompt: the hash is over this row's own fields",
          row.get('hash') == wc.row_hash(row['key'], row['claim'],
                                         row['code_value']),
          repr(row.get('hash')))
    check("citation prompt: the code's own citation is carried",
          row.get('code_cited') == ['IAU 2015 Resolution B3'],
          repr(row.get('code_cited')))
    check('citation prompt: the answer fields are present and empty',
          row.get('review_verdict') == ''
          and row.get('review_source') == '',
          repr(row.get('review_verdict')))

    # Same input, same bytes. A prompt that changes when nothing
    # changed cannot be evidence of anything.
    with open(path, 'rb') as handle:
        first = handle.read()
    wc.write_citation_prompt(scratch, claims)
    with open(path, 'rb') as handle:
        second = handle.read()
    check('citation prompt: the same input gives the same bytes',
          first == second)

    # A matched row carrying neither a source nor a citation verdict
    # has nothing to review. It is excluded AND counted -- a silent
    # drop is the failure mode, not a tidy file.
    bare = [PromptClaim('constants_new.py::BARE_KM', 'Claude',
                        'worksheet_claude_constants_new.md',
                        [captured(source='', verdict='')])]
    written, not_included, error = wc.write_citation_prompt(
        scratch, bare)
    check('citation prompt: a row with nothing to review is excluded',
          written == 0
          and not_included['matched_rows_with_no_citation_material'] == 1,
          '%r %r' % (written, not_included))

    # An annotation that never matched a row is counted separately.
    unmatched = [PromptClaim('constants_new.py::NOMATCH_KM', 'Claude',
                             'worksheet_claude_constants_new.md', [])]
    written, not_included, error = wc.write_citation_prompt(
        scratch, unmatched)
    check('citation prompt: an unmatched annotation is counted',
          not_included['annotations_with_no_matched_row'] == 1,
          repr(not_included))

    # And the live corpus, because a synthetic pass proves the shape
    # and not the reach. Zero rows here would mean the emitter runs
    # and finds nothing, which reads exactly like a passing run.
    worksheets = wc.load_worksheets(project_dir)
    real, _unreached, _files = wc.collect_claims(project_dir)
    unregistered = set()
    for claim in real:
        wc.check_claim(claim, worksheets, unregistered)
    corpus_rows, _corpus_excluded = wc.citation_prompt_rows(real)
    check('citation prompt: the live corpus produces rows',
          len(corpus_rows) >= 40, repr(len(corpus_rows)))
    check('citation prompt: every corpus row carries a response',
          all(row['responses'] for row in corpus_rows))
    check('citation prompt: no key appears twice',
          len(set(row['key'] for row in corpus_rows)) == len(corpus_rows),
          repr(len(corpus_rows)))

def main():
    project_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_dir)

    print('=' * 70)
    print('WORKSHEET CHECKER TESTS -- can each layer fail? (L-192)')
    print('=' * 70)

    test_comparison()
    test_verdicts()
    test_registry()
    test_key_rule()
    test_layers()
    test_display_instructions()
    test_live_corpus(project_dir)
    test_json_reader()
    test_json_row_hash()
    test_json_truncation_is_salvaged_and_announced()
    test_json_array_return_is_accepted()
    test_markdown_has_no_integrity_map()
    test_integrity_layer_fails_a_bad_row()
    test_routing_file(project_dir)
    test_resolved_linkage()
    test_suffix_sets_agree()
    test_citation_prompt(project_dir)

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
