"""patch_L204_1_grammar_and_resolved_leg.py -- L-204, L-200, L-203.

RUN COMMAND
-----------
Save this file into the palomas_orrery repo root (the same folder as
provenance_scanner.py), open it in VS Code, and click Run.

    python patch_L204_1_grammar_and_resolved_leg.py

Success prints one `ok` line per edit and then `patch applied`.
Failure prints a single ERROR or ANCHOR FAIL line and writes NOTHING --
it is always safe to re-check and run again.

WHAT IT DOES
------------
Three ledger items in one patch, because all three touch the annotation
grammar and the tools that read it. Splitting them would mean two
patches fingerprinting the same file, and the second would abort by
construction.

L-204 -- the worksheet reference may be JSON.
    provenance_scanner.parse_cross_checks required the parenthetical
    reference to end in `.md`. That condition did two jobs: it required
    a FILENAME rather than free prose (the anti-gaming half of L-186,
    which does not move), and it pinned the only worksheet format that
    existed in August 2026. The JSON return format (L-202) landed
    2026-08-17, so a returned verdict could be checked and routed and
    then refused when it was written back into the code. The accepted
    set becomes ('.md', '.jsonl', '.json') and the issue code
    `non_markdown_reference` is renamed `unsupported_reference_format`,
    which is what the rule now says.

L-200 -- the Resolved leg and its linkage check.
    A record-only annotation leg naming the worksheet row whose verdict
    caused an edit, and the ledger handle that authorized it. The
    scanner gains the grammar; the checker gains the linkage layer, a
    report section, and a count printed on every run. Nothing in the
    request builder changes: the leg is deliberately absent from
    CONTEXT_LEGS, so a row dispatched a second time cannot see what the
    last one concluded.

L-203 -- the visibility convention gets a home.
    A failure that prints where the responder reads it gets an
    ANNOTATION; a failure that appears nowhere gets a REFUSAL.
    Visibility decides, not severity. It was recorded only in a
    decisions file, which nothing loads at the moment of need.

WHAT IS PERMANENT AND WHAT IS NOT
---------------------------------
This script is disposable and one-shot; its fingerprints describe a tree
that stops existing the moment it succeeds. Permanent:

    provenance_scanner.WORKSHEET_REFERENCE_SUFFIXES  (new constant)
    provenance_scanner.parse_resolved()              (new grammar)
    worksheet_checker.collect_resolved()             (new collector)
    worksheet_checker.check_resolved()               (new layer)
    the Resolved section in WORKSHEET_CHECK.md
    provenance-discipline SKILL.md at v2.4

AFTER RUNNING
-------------
1. python test_cross_checked.py
2. python test_worksheet_checker.py
3. python maintenance_run.py          (all 12 checkers green)
4. python skills_index.py             (regenerates the manifest table in
                                       PROJECT_INSTRUCTIONS.md; it will
                                       report the version moving 2.3 to
                                       2.4)
5. Reinstall provenance-discipline in Settings > Skills.
6. Archive this script to documentation/.

The reinstall CANNOT be verified from inside the session that makes it,
so the next session confirms its own loaded copy reads 2.4 before doing
provenance work.

Module created: August 17, 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys


# Normalized md5 (CRLF folded to LF) of each file this patch expects.
# Content, not raw bytes: a Windows working copy holding CRLF is
# content-identical to the LF copy in the repo, and a raw-byte guard
# would call that a moved base.
FINGERPRINTS = {
    'provenance_scanner.py': '2c1d170363cb8003f2a378f51c6c1b4e',
    'worksheet_checker.py': '55935042612be7511977274aeda5ed85',
    'test_cross_checked.py': '20e8cd6aefff7c7c06cff7cc88ef8380',
    'test_worksheet_checker.py': '4cdeba133260775f699395b56afb953f',
    'skills_index.py': '69dbde1cce475a9f83e08fe84f678144',
    os.path.join('skills', 'provenance-discipline',
                 'SKILL.md'): '2b2b43df9de572d752fb016400ce9553',
}


# ============================================================
# provenance_scanner.py
# ============================================================

SCANNER_SUFFIX_CONSTANT = '''CROSS_CHECK_TAIL_RE = re.compile(r'^\\s*--\\s+\\S')

# The worksheet reference formats the grammar accepts (L-204,
# 2026-08-17). The SHAPE check -- a parenthetical naming a file rather
# than free prose -- is the anti-gaming half of L-186 and does not
# move. This list is the other half, and it pinned the only worksheet
# format that existed when the rule was written. The JSON return format
# (L-202) landed 2026-08-17, at which point a returned verdict could be
# built, carried, filled, returned, checked and routed -- and then
# refused by this one condition when somebody tried to write it back
# into the code as an annotation.
#
# Widened rather than worked around. Rendering an accepted JSON return
# into markdown for citation would leave two stores of one return, free
# to drift, with the integrity hash in only one of them.
#
# worksheet_checker.JSON_SUFFIXES must stay a subset of this.
# test_worksheet_checker.py pins the two together, so a fourth format
# added in one place fails loudly instead of drifting in two.
WORKSHEET_REFERENCE_SUFFIXES = ('.md', '.jsonl', '.json')

# The Resolved leg (L-200, 2026-08-17). Record-only: it grants no
# source credit, is deliberately absent from SOURCE_PATTERNS, and is
# read by worksheet_checker for linkage. See parse_resolved below.
RESOLVED_LINE_RE = re.compile(
    r'(?mi)^[ \\t]*#[ \\t]*resolved[ \\t]*:(?P<body>[^\\n]*)$')

RESOLVED_BODY_RE = re.compile(
    r'^\\s*(?P<worksheet>\\S+)\\s+(?P<key>\\S+)\\s+--\\s+(?P<what>.+?)'
    r'\\s*\\((?P<handle>L-\\d+)\\)\\s*$')


def parse_resolved(text):
    """Parse Resolved annotation legs out of a block of source text.

    Returns (records, issues).

    records: list of (worksheet, key, what, handle) tuples.
    issues:  list of (raw_line, 'malformed_resolved') for a line that
        opens with the leg label and does not complete the grammar.

    Grammar (L-200, 2026-08-17). The leading hash is omitted here on
    purpose: the scanner scans itself, and a literal leg in this
    docstring would be extracted as one.

        Resolved: <worksheet> <key> -- <what changed> (L-nnn)

    It says which returned verdict caused an edit. Without it, an
    annotation edited in response to a worksheet is indistinguishable
    from an unexplained edit, and the only record of which is which
    lives in a handoff.

    The first token is the worksheet FILENAME -- the same thing the
    cross-check parenthetical names. The ledger block that designed
    this leg wrote <batch>; a batch name does not determine what the
    returned file is called, and "names a worksheet row that exists" is
    only mechanically checkable against a file on disk.

    The second token is the row KEY, never the row number. row_id is
    assigned by position at render time and renumbers whenever the
    corpus changes; module.py::enclosing::label::cN is stable.

    This function parses. It does not check that the worksheet or the
    row exists -- that is linkage, and it lives in worksheet_checker
    where the worksheets are already loaded.
    """
    records = []
    issues = []
    if not text or 'resolved' not in text.lower():
        return records, issues
    for match in RESOLVED_LINE_RE.finditer(text):
        raw = match.group(0).strip()
        body = RESOLVED_BODY_RE.match(match.group('body'))
        if body is None:
            issues.append((raw, 'malformed_resolved'))
            continue
        records.append((body.group('worksheet').strip('`'),
                        body.group('key').strip('`'),
                        body.group('what').strip(),
                        body.group('handle')))
    return records, issues


def parse_cross_checks(text):'''

SCANNER_EDITS = [
    # 1. the new constant, the Resolved grammar, and parse_resolved
    ("""CROSS_CHECK_TAIL_RE = re.compile(r'^\\s*--\\s+\\S')


def parse_cross_checks(text):""", SCANNER_SUFFIX_CONSTANT),

    # 2. the issue-code list in the docstring
    ("""        'empty_reference', 'non_markdown_reference',""",
     """        'empty_reference', 'unsupported_reference_format',"""),

    # 3. the grammar template in the docstring
    ("""        Cross-checked: <checker> <ISO date>[ -- <source>] (<ref>.md)""",
     """        Cross-checked: <checker> <ISO date>[ -- <source>] (<worksheet>)"""),

    # 4. the prose that states the rule
    ("""    A line qualifies only with an ISO date and, after that date, a
    parenthetical reference ending in `.md`. Anything less earns""",
     """    A line qualifies only with an ISO date and, after that date, a
    parenthetical reference naming a worksheet FILE -- one ending in
    `.md`, `.jsonl` or `.json` (L-204, 2026-08-17). Anything less earns"""),

    # 5. the condition itself
    ("""        if not reference.lower().endswith('.md'):
            issues.append((raw, 'non_markdown_reference'))""",
     """        if not reference.lower().endswith(WORKSHEET_REFERENCE_SUFFIXES):
            issues.append((raw, 'unsupported_reference_format'))"""),

    # 6. the report's own explanation of what earns V2
    ('''        out.append("A qualifying annotation needs an ISO date and, "
                   "after it, a parenthetical worksheet reference "
                   "ending in `.md`. Two of them, naming different "
                   "checkers, on a claim that already has a citation, "
                   "are what earns V2.")''',
     '''        out.append("A qualifying annotation needs an ISO date and, "
                   "after it, a parenthetical worksheet reference "
                   "ending in `.md`, `.jsonl` or `.json`. Two of them, "
                   "naming different checkers, on a claim that already "
                   "has a citation, are what earns V2.")'''),
]


# ============================================================
# worksheet_checker.py
# ============================================================

CHECKER_RESOLVED_SECTION = '''# ============================================================
# THE RESOLVED LEG (L-200)
# ============================================================
#
# The scanner owns the grammar; this owns the linkage. Two definitions
# of what a leg looks like would drift apart by construction.
#
# The check is LINKAGE, not meaning. Three existence facts: the leg
# parses, it names a worksheet row that exists, and that row's citation
# verdict was one requiring an edit. Whether the edit was the RIGHT one
# is a reader's judgement and stays with a reader -- the same division
# ruled 2026-08-17 for the pilot, where the mechanical checker stays at
# numbers and the citation comparison is done by a person.
#
# The failure this exists to catch is an edit attributed to a verdict
# nobody can find, which is an unexplained edit wearing a citation.


class Resolved(object):
    """One Resolved leg, and what the linkage check made of it."""

    def __init__(self, module, path, line_no, raw):
        self.module = module
        self.path = path
        self.line_no = line_no
        self.raw = raw
        self.worksheet = ''
        self.key = ''
        self.what = ''
        self.handle = ''
        self.verdict = ''
        self.findings = []

    @property
    def where(self):
        return '%s:%d' % (os.path.basename(self.path), self.line_no)

    def fail(self, code, detail):
        self.findings.append((code, detail))


def collect_resolved(project_dir):
    """Every Resolved leg in the corpus, parsed but not yet linked.

    Read straight off the file text rather than through scanner units.
    The leg is deliberately absent from the request builder's
    CONTEXT_LEGS -- a row dispatched a second time must not be shown
    what the last one concluded -- so it attaches to no unit, and a
    unit-driven walk would never see it.
    """
    legs = []
    for fname in sorted(os.listdir(project_dir)):
        if not fname.endswith('.py'):
            continue
        path = os.path.join(project_dir, fname)
        try:
            with open(path, encoding='utf-8', errors='replace') as handle:
                lines = handle.read().splitlines()
        except OSError:
            continue
        for index, line in enumerate(lines, start=1):
            if ps.RESOLVED_LINE_RE.match(line) is None:
                continue
            leg = Resolved(fname[:-3], path, index, line.strip())
            records, issues = ps.parse_resolved(line)
            if records:
                (leg.worksheet, leg.key, leg.what,
                 leg.handle) = records[0]
            else:
                detail = issues[0][1] if issues else 'malformed_resolved'
                leg.fail('RESOLVED_MALFORMED',
                         '%s -- expected: Resolved: <worksheet> <key> '
                         '-- <what changed> (L-nnn)' % detail)
            legs.append(leg)
    return legs


def check_resolved(leg, worksheets):
    """LR -- the leg names a real row whose verdict required an edit."""
    if leg.findings:
        return
    sheet = worksheets.get(leg.worksheet)
    if sheet is None:
        leg.fail('RESOLVED_WORKSHEET_MISSING',
                 'no such file in %s' % WORKSHEET_DIR)
        return

    row = None
    table = None
    for candidate in sheet['tables']:
        index = candidate.column(ROLE_KEY)
        if index is None:
            continue
        for entry in candidate.rows:
            cells = entry[1]
            if index >= len(cells):
                continue
            if strip_cell(cells[index]).strip('`') == leg.key:
                row, table = entry, candidate
                break
        if row is not None:
            break

    if row is None:
        leg.fail('RESOLVED_ROW_MISSING',
                 'no row in %s carries the key %s'
                 % (leg.worksheet, leg.key))
        return

    if table.column(ROLE_CITATION_VERDICT) is None:
        leg.fail('RESOLVED_NO_VERDICT_COLUMN',
                 '%s has no citation-verdict column, so what the row '
                 'concluded cannot be read' % leg.worksheet)
        return

    cell = table.cell(row[1], ROLE_CITATION_VERDICT)
    verdict, _token, _scope = classify_verdict(cell, SCOPE_CITATION)
    leg.verdict = verdict
    if verdict in (V_EMPTY, V_UNREADABLE):
        leg.fail('RESOLVED_VERDICT_UNREADABLE',
                 'row %d carries no readable citation verdict: %s'
                 % (row[0], quoted(cell)))
        return
    if verdict in VERDICT_CLEARS:
        leg.fail('RESOLVED_VERDICT_CLEAR',
                 'row %d reads %s -- a cleared row warrants no edit, so '
                 'this leg does not explain one' % (row[0], verdict))


# ============================================================
# THE UNCITED SET
# ============================================================'''

CHECKER_EDITS = [
    # 1. the new section, ahead of THE UNCITED SET
    ("""# ============================================================
# THE UNCITED SET
# ============================================================""",
     CHECKER_RESOLVED_SECTION),

    # 2. write_report takes the legs
    ("""def write_report(project_dir, claims, unreached, unregistered,
                 headline, changed, uncited, files, worksheets):""",
     """def write_report(project_dir, claims, unreached, unregistered,
                 headline, changed, uncited, files, worksheets,
                 resolved):"""),

    # 3. the denominator gains two rows
    ("""    add('| Annotation lines the scanner does not score | %d |'
        % len(unreached))
    add('')""",
     """    add('| Annotation lines the scanner does not score | %d |'
        % len(unreached))
    add('| Resolved legs examined | %d |' % len(resolved))
    add('| Resolved legs with a linkage problem | %d |'
        % sum(1 for leg in resolved if leg.findings))
    add('')"""),

    # 4. the report section itself
    ("""    add('## What this tool cannot see')""",
     """    add('## Resolved legs -- verdicts that landed in the code (L-200)')
    add('')
    add('Linkage only. That the leg names a real row whose citation '
        'verdict required an edit is checkable. Whether the edit was '
        'the RIGHT one is not, and stays with a reader.')
    add('')
    if resolved:
        add('| Where | Worksheet | Row key | Verdict | Handle | Finding |')
        add('|---|---|---|---|---|---|')
        for leg in resolved:
            finding = 'linked'
            if leg.findings:
                finding = '**%s** -- %s' % (leg.findings[0][0],
                                            leg.findings[0][1])
            add('| `%s` | `%s` | `%s` | %s | %s | %s |'
                % (leg.where, leg.worksheet or '-', leg.key or '-',
                   leg.verdict or '-', leg.handle or '-', finding))
    else:
        add('None in the corpus. Stated rather than left silent: the '
            'leg is new (L-200, 2026-08-17), and an empty section that '
            'prints nothing cannot be told from one that never ran.')
    add('')

    add('## What this tool cannot see')"""),

    # 5. run() collects and checks the legs
    ("""    worksheets = load_worksheets(project_dir)
    claims, unreached, files = collect_claims(project_dir)""",
     """    worksheets = load_worksheets(project_dir)
    claims, unreached, files = collect_claims(project_dir)

    resolved = collect_resolved(project_dir)
    for leg in resolved:
        check_resolved(leg, worksheets)"""),

    # 6. run() passes them to the report
    ("""    report = write_report(project_dir, claims, unreached, unregistered,
                          headline, changed, uncited, files, worksheets)""",
     """    report = write_report(project_dir, claims, unreached, unregistered,
                          headline, changed, uncited, files, worksheets,
                          resolved)"""),

    # 7. run() counts them
    ("""        'routed_keys_written': routed_written,
    }""",
     """        'routed_keys_written': routed_written,
        'resolved_legs': len(resolved),
        'resolved_problems': sum(1 for leg in resolved if leg.findings),
    }"""),

    # 8. the detail block reports them, every run, including zero
    ("""    if routing_error:
        detail += '\\n  %s' % routing_error""",
     """    # Printed every run, including zero, for the same reason the hash
    # line is: a section that says nothing when there is nothing cannot
    # be told from one that never ran.
    resolved_problems = sum(1 for leg in resolved if leg.findings)
    detail += ('\\n  %d Resolved leg(s) examined: %d linked, %d with a '
               'linkage problem'
               % (len(resolved), len(resolved) - resolved_problems,
                  resolved_problems))
    if routing_error:
        detail += '\\n  %s' % routing_error"""),
]


# ============================================================
# test_cross_checked.py
# ============================================================

TEST_CROSS_CHECKED_TEST = '''def test_json_worksheet_reference_is_accepted():
    """L-204 -- a JSON return can be cited, and prose still cannot.

    The `.md` condition did two jobs. It required the parenthetical to
    name a FILE rather than free prose, which is the anti-gaming half
    of L-186 and does not move. It also pinned the only worksheet
    format that existed in August 2026. The JSON return format (L-202)
    landed 2026-08-17, so a verdict could be returned, checked and
    routed as `.jsonl` and then refused when it was written back into
    the code -- which is where the loop stopped.
    """
    for suffix in WORKSHEET_REFERENCE_SUFFIXES:
        line = f"# Cross-checked: Gemini 2026-04-15 (worksheet_x{suffix})"
        records, issues = parse_cross_checks(line)
        assert len(records) == 1 and not issues, (
            f"expected {suffix} to be accepted, got {records} {issues}")
        assert records[0][2] == f"worksheet_x{suffix}", (
            f"the reference did not survive the parse: {records}")

    # The shape check survives. The widening is a list of FORMATS, not
    # a relaxation of the rule that a reference names a file.
    for bad in ("(the Gemini worksheet)", "(notes.txt)", "(worksheet)"):
        line = f"# Cross-checked: Gemini 2026-04-15 {bad}"
        records, issues = parse_cross_checks(line)
        assert records == [] and issues, (
            f"expected {bad} to be refused, got {records} {issues}")
        assert issues[0][1] == 'unsupported_reference_format', (
            f"expected unsupported_reference_format for {bad}: {issues}")

    assert WORKSHEET_REFERENCE_SUFFIXES == ('.md', '.jsonl', '.json'), (
        f"the accepted set moved: {WORKSHEET_REFERENCE_SUFFIXES}")


def test_resolved_leg_grammar():
    """L-200 -- the Resolved leg parses, and a partial one is refused.

    Record-only, so the thing to pin is that it grants nothing. A leg
    on an uncited claim must leave it at V_RECALLED exactly as if the
    line were not there, the same anti-gaming rule the cross-check
    annotation follows.
    """
    key = 'constants_new.py::ROCHE_LIMIT_RADII::c1'
    good = ("# Resolved: worksheet_pilot.jsonl %s -- citation refuted, "
            "Source replaced (L-204)" % key)
    records, issues = parse_resolved(good)
    assert len(records) == 1 and not issues, (
        f"expected one record, got {records} {issues}")
    worksheet, parsed_key, what, handle = records[0]
    assert worksheet == 'worksheet_pilot.jsonl', worksheet
    assert parsed_key == key, parsed_key
    assert what == 'citation refuted, Source replaced', what
    assert handle == 'L-204', handle

    for bad in ("# Resolved: worksheet_pilot.jsonl",
                "# Resolved: worksheet_pilot.jsonl %s -- no handle" % key,
                "# Resolved: -- citation refuted (L-204)"):
        records, issues = parse_resolved(bad)
        assert records == [] and issues, (
            f"expected a refusal for {bad!r}, got {records} {issues}")
        assert issues[0][1] == 'malformed_resolved', issues

    unit = _scored("# Source: Fixture authority ALPHA\\n" + good)
    assert unit.vuln != V_CROSS_CHECKED, (
        "a Resolved leg must not earn cross-check credit")
    unit = _scored(good)
    assert unit.vuln == V_RECALLED, (
        f"a Resolved leg must source nothing, got V{unit.vuln}")


'''

TEST_CROSS_CHECKED_EDITS = [
    # 1. import the new names
    ("""    V_SOURCED,
    distinct_checker_identities,""",
     """    V_SOURCED,
    WORKSHEET_REFERENCE_SUFFIXES,
    distinct_checker_identities,"""),

    # 2. parse_resolved joins the imported functions
    ("""    parse_cross_checks,
    score_unit,
)""",
     """    parse_cross_checks,
    parse_resolved,
    score_unit,
)"""),

    # 3. the trivial-reference test covers prose as well
    ('''    """Empty and non-markdown references are both rejected."""
    empty = "# Cross-checked: Gemini 2026-04-15 ()"
    trivial = "# Cross-checked: Gemini 2026-04-15 (x)"
    for line, expected in ((empty, 'empty_reference'),
                           (trivial, 'non_markdown_reference')):''',
     '''    """Empty and unsupported-format references are both rejected."""
    empty = "# Cross-checked: Gemini 2026-04-15 ()"
    trivial = "# Cross-checked: Gemini 2026-04-15 (x)"
    prose = "# Cross-checked: Gemini 2026-04-15 (the Gemini worksheet)"
    for line, expected in ((empty, 'empty_reference'),
                           (trivial, 'unsupported_reference_format'),
                           (prose, 'unsupported_reference_format')):'''),

    # 4. the issue-code map
    ('''        "# Cross-checked: Gemini 2026-04-15 (x)": 'non_markdown_reference',''',
     '''        "# Cross-checked: Gemini 2026-04-15 (x)":
            'unsupported_reference_format','''),

    # 5. the two new tests, ahead of the registry
    ("""TESTS = [""", TEST_CROSS_CHECKED_TEST + """TESTS = ["""),

    # 6. registered
    ("""    test_source_clause_after_date_is_accepted,
]""",
     """    test_source_clause_after_date_is_accepted,
    test_json_worksheet_reference_is_accepted,
    test_resolved_leg_grammar,
]"""),
]


# ============================================================
# test_worksheet_checker.py
# ============================================================

TEST_CHECKER_TESTS = '''def _resolved_project(leg_line, rows, sheet='worksheet_pilot.jsonl',
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
              encoding='utf-8', newline='\\n') as handle:
        handle.write('VALUE = 1.0\\n')
        handle.write(leg_line + '\\n')
    with open(os.path.join(scratch, wc.WORKSHEET_DIR, sheet), 'w',
              encoding='utf-8', newline='\\n') as handle:
        if sheet_text is not None:
            handle.write(sheet_text)
        else:
            for row in rows:
                handle.write(json.dumps(row) + '\\n')
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
    no_column = ('| Key | Claim | Value correct? |\\n'
                 '|---|---|---|\\n'
                 '| `%s` | the claim | YES |\\n' % KEY)
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


'''

TEST_CHECKER_EDITS = [
    ("""def main():
    project_dir = os.path.dirname(os.path.abspath(__file__))""",
     TEST_CHECKER_TESTS + """def main():
    project_dir = os.path.dirname(os.path.abspath(__file__))"""),

    ("""    test_routing_file(project_dir)

    for name, detail in FAILED:""",
     """    test_routing_file(project_dir)
    test_resolved_linkage()
    test_suffix_sets_agree()

    for name, detail in FAILED:"""),
]


# ============================================================
# skills_index.py
# ============================================================

SKILLS_INDEX_EDITS = [
    ("""    try:
        from provenance_scanner import parse_cross_checks
    except ImportError:""",
     """    try:
        from provenance_scanner import parse_cross_checks, parse_resolved
    except ImportError:"""),

    ("""            identity = records[0][0]
            runs = ''.join(c if c.isdigit() else ' ' for c in identity).split()
            if any(len(run) >= 4 for run in runs):
                problems.append(
                    f"{skill_dir.name}: annotation example's checker carries "
                    f"a year, so the date was parsed from the source: "
                    f"{stripped}")
    return problems""",
     """            identity = records[0][0]
            runs = ''.join(c if c.isdigit() else ' ' for c in identity).split()
            if any(len(run) >= 4 for run in runs):
                problems.append(
                    f"{skill_dir.name}: annotation example's checker carries "
                    f"a year, so the date was parsed from the source: "
                    f"{stripped}")

        # The Resolved leg (L-200) is checked the same way and for the
        # same reason. A skill that teaches a leg the parser refuses is
        # the L-186 defect in a second grammar.
        for line in text.splitlines():
            stripped = line.strip()
            if not stripped.startswith('# Resolved:') or '<' in stripped:
                continue
            records, issues = parse_resolved(stripped)
            if len(records) != 1:
                problems.append(
                    f"{skill_dir.name}: Resolved example does not parse "
                    f"({issues or 'no record'}): {stripped}")
    return problems"""),
]


# ============================================================
# skills/provenance-discipline/SKILL.md
# ============================================================

SKILL_VERSION_BLOCK = """Skill version: 2.4 | Cut from palomas_orrery @ 6b99ace (v2.2), earlier
@ 00219d9 (v2.1), @ eb77c83 (v2.0), @ cdcdb4b (v1.9) | August 17, 2026"""

SKILL_V24_NOTE = """
v2.4 (August 17, 2026) carries three changes, all earned the same day.
The annotation grammar now accepts a `.jsonl` or `.json` worksheet
reference as well as `.md` (L-204). The `.md` condition did two jobs:
it required the parenthetical to name a FILE rather than free prose,
which is the anti-gaming half of L-186 and does not move, and it
pinned the only worksheet format that existed in August 2026. The JSON
return format (L-202) landed 2026-08-17, and a returned verdict could
then be built, carried, filled, checked and routed -- and refused by
that one condition when somebody wrote it back into the code. Found by
an integration test, not by a reading. The Resolved Leg section is new
(L-200): a record-only leg saying which returned verdict caused an
edit. And The Visibility Convention is new (L-203), promoting a
one-off ruling about the request builder into the general rule it was
always an instance of.

## The Visibility Convention [CRITICAL]

**A failure that prints where the responder reads it gets an
ANNOTATION. A failure that appears nowhere gets a REFUSAL. Visibility
decides, not severity.**

The case that produced it: the request builder joins a citation
continued onto a marked line, and two things can go wrong. A
continuation marker whose label does not match the leg above it is
REPORTED -- the mismatch prints into the worksheet, where the person
filling the row will see it and can say so. A continuation line
carrying no marker at all REFUSES the whole build, because nothing
about it reaches any reader: the text is silently dropped and the
worksheet that results looks complete.

Severity would have ranked these the other way round. A label mismatch
is the louder defect on its face. What matters instead is whether the
system can be told about the failure by somebody who sees it, because
a defect with a reader has a correction path and a defect with no
reader does not.

The rule generalizes past the builder. Before choosing between
reporting a problem and refusing to proceed, ask where the report
lands and who reads it. If the honest answer is that it lands in a log
nobody opens, or in a file the next session will not load, then
reporting is silence wearing the costume of diligence, and the correct
behaviour is to refuse.

(Tony's ruling, 2026-08-17, settling an L-196 question as a convention
rather than a one-off, because the same distinction governs every
future case of the same shape.)
"""

SKILL_GRAMMAR = """### Cross-Checked Annotation Format [CRITICAL]

The checker comes FIRST. The grammar is fixed:

```
# Cross-checked: <checker> <ISO date>[ -- <source>] (<worksheet>)
```

The parenthetical names a worksheet FILE. Accepted formats are `.md`,
`.jsonl` and `.json` (L-204, 2026-08-17); anything that is not a
filename -- free prose, a bare word, a description of where the
evidence lives -- is refused as `unsupported_reference_format`. The
shape rule is the anti-gaming half of L-186 and does not move. The
format list widened when the JSON worksheet format landed (L-202),
because a return that can be checked and routed and then not cited is
a loop with no last inch."""

# The worked example is COMPOSED rather than written out, so that this
# script's own bytes never carry a leg at the start of a line. They
# would otherwise be collected as a real one for as long as the script
# sits in the repo root, and the first run after the patch would report
# a phantom finding. (Measured, not guessed: the first sandbox run
# reported exactly that -- 1 leg examined, 1 with a linkage problem.)
SKILL_RESOLVED_EXAMPLE = (
    '# ' + 'Resolved: worksheet_pilot.jsonl '
    'constants_new.py::ROCHE_LIMIT_RADII::c1 -- citation refuted, '
    'Source replaced (L-204)')

SKILL_RESOLVED_SECTION = '''#### The Resolved Leg [QUALITY]

A record-only leg naming the worksheet row whose verdict caused an
edit, and the ledger handle that authorized it (L-200, 2026-08-17):

```
%s
```''' % SKILL_RESOLVED_EXAMPLE + '''

Without it, an annotation edited in response to a verdict is
indistinguishable from an unexplained edit, and the only record of
which is which lives in a handoff.

**It cites the KEY, never the row number.** `row_id` is assigned by
position when a request is rendered and renumbers whenever the corpus
changes. `module.py::enclosing::label::cN` is stable. This is the same
failure the ledger already records for per-handoff item numbers.

**It is deliberately invisible to the request.** The leg is not in the
builder's `CONTEXT_LEGS`, so a row dispatched a second time cannot see
what the last one concluded. A context leg would anchor a second
reader the way a Claude-derived figure anchors Gemini.

**The checker checks LINKAGE, not meaning.** Three existence facts: the
leg parses, it names a worksheet row that exists, and that row's
citation verdict was one requiring an edit. A leg pointing at a row
that does not exist is refused -- an edit attributed to a verdict
nobody can find is an unexplained edit wearing a citation. Whether the
edit was the RIGHT one stays with a reader.

#### Worksheet First, Annotation Second [CRITICAL]'''

SKILL_EDITS = [
    ("""Skill version: 2.3 | Cut from palomas_orrery @ 6b99ace (v2.2), earlier
@ 00219d9 (v2.1), @ eb77c83 (v2.0), @ cdcdb4b (v1.9) | August 13, 2026""",
     SKILL_VERSION_BLOCK),

    ("""## The Goal State""", SKILL_V24_NOTE + """
## The Goal State"""),

    ("""### Cross-Checked Annotation Format [CRITICAL]

The checker comes FIRST. The grammar is fixed:

```
# Cross-checked: <checker> <ISO date>[ -- <source>] (<worksheet>.md)
```""", SKILL_GRAMMAR),

    ("""#### Worksheet First, Annotation Second [CRITICAL]""",
     SKILL_RESOLVED_SECTION),
]


# ============================================================
# HARNESS
# ============================================================

PLAN = [
    ('provenance_scanner.py', SCANNER_EDITS),
    ('worksheet_checker.py', CHECKER_EDITS),
    ('test_cross_checked.py', TEST_CROSS_CHECKED_EDITS),
    ('test_worksheet_checker.py', TEST_CHECKER_EDITS),
    ('skills_index.py', SKILLS_INDEX_EDITS),
    (os.path.join('skills', 'provenance-discipline', 'SKILL.md'),
     SKILL_EDITS),
]


def fingerprint(data):
    """Content fingerprint: line endings normalized before hashing.

    A Windows working copy holding CRLF is content-identical to the LF
    copy in the repo. A raw-byte hash calls that a moved base and sends
    everyone hunting an edit nobody made.
    """
    return hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()


def non_ascii(data):
    return [b for b in data if b > 127]


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    os.chdir(here)

    # ---- gate 1: every file present and the expected content --------
    for name, _edits in PLAN:
        if not os.path.isfile(name):
            print('ERROR: %s not found. Run this from the repo root.' % name)
            return 1
        with open(name, 'rb') as handle:
            data = handle.read()
        seen = fingerprint(data)
        want = FINGERPRINTS[name]
        if seen != want:
            print('ERROR: %s has moved. Expected %s, found %s.'
                  % (name, want, seen))
            print('       Nothing written. This patch was built against '
                  'df81b3358823139784dcd1e80052c6685dd86e22.')
            return 1

    # ---- gate 2: every anchor present exactly once ------------------
    staged = {}
    notes = []
    for name, edits in PLAN:
        with open(name, 'rb') as handle:
            data = handle.read()
        is_crlf = data.count(b'\r\n') > 0
        content = data
        for old, new in edits:
            old_b = old.encode('utf-8')
            new_b = new.encode('utf-8')
            if non_ascii(new_b):
                print('ERROR: this patch would insert non-ASCII bytes into '
                      '%s. Nothing written.' % name)
                return 1
            if is_crlf:
                old_b = old_b.replace(b'\n', b'\r\n')
                new_b = new_b.replace(b'\n', b'\r\n')
            count = content.count(old_b)
            if count != 1:
                print('ANCHOR FAIL: %s -- expected 1 match, found %d for:'
                      % (name, count))
                print('   %s' % old.splitlines()[0][:70])
                print('Nothing written.')
                return 1
            content = content.replace(old_b, new_b)
        # Fix in passing: pre-existing non-ASCII in a file this patch is
        # already fingerprinting. Reported either way, because a patch
        # that fixes some and not all must say which.
        left = non_ascii(content)
        if left:
            notes.append('note: %s still holds %d non-ASCII byte(s) this '
                         'patch did not reach' % (name, len(left)))
        staged[name] = content

    # ---- write, only now that every edit has been proven ------------
    written = 0
    for name, edits in PLAN:
        with open(name, 'wb') as handle:
            handle.write(staged[name])
        written += len(staged[name])
        print('ok  %s (%d edit%s)'
              % (name, len(edits), '' if len(edits) == 1 else 's'))

    for note in notes:
        print(note)
    print('patch applied (%d bytes across %d files)' % (written, len(PLAN)))
    print('')
    print('Next: python test_cross_checked.py')
    print('      python test_worksheet_checker.py')
    print('      python maintenance_run.py')
    print('      python skills_index.py      (manifest: 2.3 -> 2.4)')
    print('      then reinstall provenance-discipline in Settings > Skills')
    return 0


if __name__ == '__main__':
    sys.exit(main())
