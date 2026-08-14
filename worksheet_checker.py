"""worksheet_checker.py -- L-192. Does the worksheet say what the
annotation claims it says?

RUN COMMAND
-----------
Open this file in VS Code and click Run. It takes no arguments.

    python worksheet_checker.py

It is also the last CHECKERS row in maintenance_run.py, so a normal
maintenance run includes it.

WHAT IT DOES
------------
A cross-check annotation in the source asserts four things at once: a
named checker verified a specific value, against sources, on a date,
and wrote the check down in a named worksheet. The provenance scanner
parses that line's shape and knows which value it is attached to.
Nothing has ever opened the worksheet.

This tool opens it. For every annotation attached to a scored unit it
finds the row that is about that value and reads what the row actually
recorded. Six layers, each with a failure it can produce:

    L0   the named worksheet exists on disk
    LID  the worksheet belongs to the named checker
    L1   the row about this value is located
    L2a  the code's value agrees with the row's evidence value
    L2b  the code's value still equals what the checker read then
    L3   the row's verdict amounts to a completed check

WHY IT IS THE LAST CHECK STANDING
---------------------------------
constants_change_report.py asks git what moved since the last commit,
so a value corrupted and committed three weeks ago has nothing in the
diff to notice. The structural tests assert derivations and orderings,
never a measured value against outside evidence. A worksheet is a fixed
record: it said what it said, whatever happened to the code afterwards.
This is the only check here that reaches committed history.

TWO DISPOSITIONS, AND THIS TOOL NAMES WHICH ONE
-----------------------------------------------
Ruled 2026-08-13, and the distinction is the whole design:

  SEND BACK fires on INCOMPLETENESS. A row that shows no work, a
  PARTIAL or APPROX verdict, an annotation claiming a completed check
  over a row that records an incomplete one. The cause is known, and
  the answer is a better worksheet -- not a cleverer parser here.

  CONVERSATION fires on DISAGREEMENT. A complete row whose number
  disagrees with the code has already given everything needed to
  settle the question. Three outcomes are live -- convention mismatch,
  the code is wrong, the worksheet is wrong -- and NO TOOL ASSIGNS THE
  CAUSE. The Hill sphere is the worked case: checkers who computed at
  semimajor axis dropped the eccentricity factor and got a number that
  reads as a gross error and is not one.

WHAT IT DOES NOT DO
-------------------
It does not write. There is no propose mode and no argument that adds
one (ruled 2026-08-13). Proposed annotations are discussed in
conversation first. A tool that both judges evidence and writes
citations can satisfy itself, and the risk is not forgery -- it is a
matcher bug writing annotations against wrong rows and the same
matcher later confirming them.

It does not gate the push. Report-only. Exit 0 whenever the check RAN,
whatever it found; exit 1 only when the check could not run at all.
Expanding the Tier-1 push gate is a separate decision.

It does not grade a derivation. A DERIVED row is complete when it
names its inputs, shows the arithmetic, and the arithmetic closes --
and reading arbitrary prose arithmetic is not something this tool can
do honestly. It classifies the row and routes it to conversation.

WHAT IT CANNOT SEE, STATED SO NOBODY EXPECTS IT
-----------------------------------------------
Every run prints these rather than leaving them silent:

  - Annotation lines attached to code the scanner does not score as a
    unit. They grant no credit and this tool cannot check them. That
    is scanner reach (L-190), not a defect here.
  - The eighteen inline literals duplicating cited constants. No
    worksheet ever names them, so they are outside this tool's bounds
    by construction (handoff do-item 4).
  - Header sets the registry does not recognise. Reported with file
    and line, never skipped quietly.

Role: devtool
Domain: dev_tools

Module created: August 2026 with Anthropic's Claude Opus 5.
"""

import json
import os
import re
import sys

import provenance_scanner as ps

WORKSHEET_DIR = os.path.join('documentation', 'worksheets')
REPORT_PATH = 'WORKSHEET_CHECK.md'
STATE_PATH = os.path.join('data', 'worksheet_check_state.json')


# ============================================================
# HEADER ROLE REGISTRY
# ============================================================
#
# Eight column layouts existed before any prompt specified one, and
# thirty-one distinct header sets are on disk today. The registry maps
# a header CELL to a role. It is built from a measurement of the
# corpus, not from what a schema ought to look like.
#
# A header cell the registry does not know is recorded and printed. It
# is never dropped: silence about something unexamined is the failure
# this whole layer exists to prevent.

ROLE_NUM = 'num'
ROLE_ID = 'id'
ROLE_CODE = 'code_value'
ROLE_EVIDENCE = 'evidence_value'
ROLE_VALUE_VERDICT = 'value_verdict'
ROLE_CITATION_VERDICT = 'citation_verdict'
ROLE_SOURCE = 'source'
ROLE_NOTES = 'notes'
ROLE_STATUS = 'status'
# The followup worksheets resolve QUESTIONS rather than tabulate
# values, and their Resolution column carries verdicts for the value
# and for the citation depending on the token. It is its own role:
# folding it into either verdict column would assign a scope the cell
# does not state.
ROLE_RESOLUTION = 'resolution'

HEADER_ROLES = {
    '#': ROLE_NUM,

    'claim': ROLE_ID,
    'claim in code': ROLE_ID,
    'constant': ROLE_ID,
    'topic': ROLE_ID,
    'question': ROLE_ID,
    'source to check': ROLE_ID,

    # 'value' is the CODE's value in every row table that carries it;
    # the one auxiliary table using it has no identifier column, so it
    # never becomes a row table.
    'value': ROLE_CODE,
    'code value': ROLE_CODE,

    'your value': ROLE_EVIDENCE,
    'my value': ROLE_EVIDENCE,
    'what the source says': ROLE_EVIDENCE,
    'independently researched value / finding': ROLE_EVIDENCE,

    'value correct?': ROLE_VALUE_VERDICT,
    'match?': ROLE_VALUE_VERDICT,
    'citation correct?': ROLE_CITATION_VERDICT,

    'cited source': ROLE_SOURCE,
    'your source': ROLE_SOURCE,
    'my source': ROLE_SOURCE,
    'source': ROLE_SOURCE,
    'source (specific)': ROLE_SOURCE,
    'primary source': ROLE_SOURCE,
    'paper': ROLE_SOURCE,
    'full citation': ROLE_SOURCE,

    'notes': ROLE_NOTES,
    'resolution': ROLE_RESOLUTION,
    'headline': ROLE_NOTES,
    'note': ROLE_NOTES,
    'what it says': ROLE_NOTES,

    # Triage columns. A worksheet asking whether something NEEDS
    # verifying has not verified it, so these are deliberately not
    # verdicts.
    'needs verification?': ROLE_STATUS,
    'status': ROLE_STATUS,
    'reached the source?': ROLE_STATUS,
}

# A table is a ROW TABLE when it identifies its rows and records
# something about them. Anything else is an auxiliary table -- a
# citation list, a basis comparison, a tally -- and carries no rows
# this tool can check.
EVIDENCE_ROLES = (ROLE_CODE, ROLE_EVIDENCE, ROLE_VALUE_VERDICT,
                  ROLE_CITATION_VERDICT, ROLE_RESOLUTION)


# ============================================================
# VERDICT VOCABULARY
# ============================================================
#
# Exact match only, case-folded, after markdown emphasis is stripped.
# Verdicts are never fuzzy-matched: two counts of the same corpus
# disagreed by up to 62 on YES because two different grep rules were
# used on it, which is why the verdict COLUMN is read by role and the
# column that was read is reported.

V_CONFIRMED = 'CONFIRMED'      # a completed check
V_INCOMPLETE = 'INCOMPLETE'    # PARTIAL / APPROX -- goes back
V_REFUTED = 'REFUTED'          # the worksheet contradicts the code
V_ABSENT = 'ABSENT'            # nobody performed the check
V_SOURCE_ABSENT = 'SOURCE_ABSENT'  # checked; the source does not have it
V_DERIVED = 'DERIVED'          # answers the citation question
V_UNREADABLE = 'UNREADABLE'    # not in the vocabulary
V_EMPTY = 'EMPTY'              # no cell at all

# Each token maps to (class, scope). Scope names WHICH question the
# token answers -- the value, the citation, or either, in which case
# the column's own role decides. Without it, "wrong citation" sitting
# in a mixed Resolution column reads as a refuted value, which is the
# conflation the two-column schema exists to prevent.
SCOPE_VALUE = 'value'
SCOPE_CITATION = 'citation'
SCOPE_EITHER = 'either'

VERDICT_TOKENS = {
    'yes': (V_CONFIRMED, SCOPE_EITHER),
    'confirmed': (V_CONFIRMED, SCOPE_EITHER),
    'correct': (V_CONFIRMED, SCOPE_EITHER),

    'partial': (V_INCOMPLETE, SCOPE_EITHER),
    'approx': (V_INCOMPLETE, SCOPE_EITHER),
    'approximate': (V_INCOMPLETE, SCOPE_EITHER),

    'no': (V_REFUTED, SCOPE_EITHER),

    # UNVERIFIED means nobody looked. UNSOURCED means somebody looked
    # and the source does not publish it at all. Those are different
    # findings with different owners, and collapsing them reported the
    # Bennu row -- "Not checked" -- as a citation defect, which blames
    # the source for work that was never done.
    'unverified': (V_ABSENT, SCOPE_EITHER),
    'unsourced': (V_SOURCE_ABSENT, SCOPE_CITATION),

    'derived': (V_DERIVED, SCOPE_EITHER),
}

# WHAT WAS REMOVED, AND WHY IT IS NOT COMING BACK.
#
# An earlier registry read twenty tokens. It was built by measuring the
# corpus rather than by reading the vocabulary, on the reasoning that a
# word the prompts had commissioned should be honored rather than
# refused. That reasoning holds for exactly one word.
#
# Measured across the seventeen cited worksheets: of the three tokens
# earlier prompts named beyond the six, UNSOURCED appears ten times,
# DEAD LINK zero, OUTDATED zero. Everything else -- CONFIRMED (14),
# WRONG CITATION (10), NOT FOUND (7), WRONG VALUE (5), and a tail of
# one-offs like 'thermosphere' and 'see F5' -- was invented at the
# keyboard, and nearly every one sits in the Resolution column of the
# five followup files already going back for redo.
#
# So the translation table would have been maintained for files being
# re-commissioned anyway. WRONG VALUE and WRONG CITATION are the
# clearest case: they exist only because a worksheet had ONE verdict
# column, and the two-column schema states which one is wrong without
# needing a compound word for it.
#
# Anything outside the seven now reads UNREADABLE and goes back. That
# is the intended behaviour, not a gap. (Tony's ruling, 2026-08-13,
# after Fable argued for grandfathering and the measurement showed the
# grandfathered population was being re-commissioned regardless.)

# Verdicts that let an annotation stand as written. Everything else is
# a finding of some kind. PARTIAL and APPROX are deliberately absent:
# they return to the originator unconditionally, without first asking
# why the row is qualified (ruled 2026-08-13).
VERDICT_CLEARS = (V_CONFIRMED,)


# ============================================================
# MARKDOWN TABLE PARSING
# ============================================================

RULE_ROW_RE = re.compile(r'^\|[\s:\-\|]+\|$')

# Backticks and asterisks only. An underscore is NOT decoration here:
# it is half of every constant name in the corpus, and stripping it
# turned BENNU_RADIUS_KM into a string that matched nothing. Markdown
# underscore-emphasis is instead removed only where it wraps a token.
EMPHASIS_RE = re.compile(r'[*`]+')
WRAPPED_UNDERSCORE_RE = re.compile(r'(?<![A-Za-z0-9_])_+([^_]+?)_+(?![A-Za-z0-9_])')


def strip_cell(text):
    """Cell text with markdown emphasis and escapes removed."""
    text = (text or '').replace('\\#', '#').replace('\\|', '|')
    text = EMPHASIS_RE.sub('', text)
    text = WRAPPED_UNDERSCORE_RE.sub(r'\1', text)
    return ' '.join(text.split())


def split_row(line):
    """Cells of one markdown table row, outer pipes discarded."""
    body = line.strip()
    if body.startswith('|'):
        body = body[1:]
    if body.endswith('|'):
        body = body[:-1]
    return [cell.strip() for cell in body.split('|')]


class Table(object):
    """One markdown table: its header roles and its data rows."""

    def __init__(self, path, header_line, headers, rows):
        self.path = path
        self.header_line = header_line
        self.headers = headers
        self.rows = rows
        self.roles = [HEADER_ROLES.get(strip_cell(h).lower())
                      for h in headers]
        self.unregistered = [strip_cell(h) for h, role
                             in zip(headers, self.roles) if role is None]

    @property
    def is_row_table(self):
        return (ROLE_ID in self.roles
                and any(role in EVIDENCE_ROLES for role in self.roles))

    def column(self, role):
        """Index of the first column carrying `role`, or None."""
        for index, own in enumerate(self.roles):
            if own == role:
                return index
        return None

    def cell(self, row, role):
        index = self.column(role)
        if index is None or index >= len(row):
            return ''
        return strip_cell(row[index])


def parse_tables(path, text):
    """Every markdown table in one worksheet, in file order."""
    tables = []
    lines = text.splitlines()
    index = 0
    while index < len(lines) - 1:
        line = lines[index].strip()
        if line.startswith('|') and RULE_ROW_RE.match(lines[index + 1].strip()):
            headers = split_row(line)
            rows = []
            cursor = index + 2
            while cursor < len(lines) and lines[cursor].strip().startswith('|'):
                cells = split_row(lines[cursor])
                if not RULE_ROW_RE.match(lines[cursor].strip()):
                    rows.append((cursor + 1, cells))
                cursor += 1
            tables.append(Table(path, index + 1, headers, rows))
            index = cursor
        else:
            index += 1
    return tables


# ============================================================
# NUMERIC COMPARISON
# ============================================================
#
# Exact-or-rounded, never "within tolerance." Mercury is the
# cautionary case sitting in the corpus: 2439.7 in the code against
# 2439.4 +/- 0.1 from JPL in a worksheet cell. A significant-figures
# tolerance calls those a match at three figures and the finding
# vanishes.

NUMBER_RE = re.compile(
    r'[-+]?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?(?:\s*[eE]\s*[-+]?\d+)?')

RANGE_HINT_RE = re.compile(
    r'\d\s*(?:-|--|to|\u2013|\u2014)\s*\d')

# Multipliers that appear as words beside a number in these worksheets.
SCALE_WORDS = (
    ('million', 1e6), ('mkm', 1e6), ('billion', 1e9),
    ('thousand', 1e3), ('e6', 1e6), ('e3', 1e3),
)


def numbers_in(text):
    """Every number in a cell, as floats, in reading order."""
    out = []
    for match in NUMBER_RE.finditer(text or ''):
        raw = match.group(0).replace(',', '').replace(' ', '')
        try:
            out.append((match.group(0).strip(), float(raw)))
        except ValueError:
            continue
    return out


def scaled(value, text):
    """Apply a scale word appearing in the cell, if any."""
    low = (text or '').lower()
    for word, factor in SCALE_WORDS:
        if word in low:
            return value * factor
    return value


def displayed_precision(raw):
    """Decimal places shown in a number as written."""
    body = raw.split('e')[0].split('E')[0]
    if '.' not in body:
        return 0
    return len(body.split('.')[1])


def float_precision(value):
    """Decimal places a float carries as written."""
    text = repr(float(value))
    if 'e' in text or 'E' in text:
        return 12
    body = text.split('.')[1] if '.' in text else ''
    return len(body.rstrip('0'))


def compare(code_value, cell_text):
    """(verdict, detail) for one value against one worksheet cell.

    MATCH        equal, or equal once BOTH are rounded to the coarser
                 of the two displayed precisions
    RANGE        the cell states a range -- never a match, its own class
    CONVERSION   equal only after a scale word was applied
    MISMATCH     both are numbers and they disagree
    NO_NUMBER    the cell states no number at all

    Exact-or-rounded, never "within tolerance." Mercury is the
    cautionary case sitting in the corpus: 2439.7 in the code against
    2439.4 +/- 0.1 from JPL in a worksheet cell. Both are written to
    one decimal, so the coarser precision is one decimal, and they
    still disagree -- which is the finding, and a significant-figures
    tolerance would have dissolved it.

    Rounding to the COARSER of the two is what makes the rule
    symmetric. The code often carries a rounded display of a more
    precise measurement -- 243 against 243.0226 -- and reading that as
    a mismatch would report a rounding as a value error.
    """
    if code_value is None:
        return 'NO_CODE_VALUE', ''
    found = numbers_in(cell_text)
    if not found:
        return 'NO_NUMBER', (cell_text or '')[:60]
    if RANGE_HINT_RE.search(cell_text or ''):
        return 'RANGE', (cell_text or '')[:60]

    code_places = float_precision(code_value)
    for raw, value in found:
        if value == code_value:
            return 'MATCH', raw
        places = min(displayed_precision(raw), code_places)
        if round(code_value, places) == round(value, places):
            return 'MATCH', '%s (both at %d dp)' % (raw, places)

    for raw, value in found:
        lifted = scaled(value, cell_text)
        if lifted == code_value:
            return 'CONVERSION', '%s scaled' % raw
        places = min(displayed_precision(raw), code_places)
        if lifted and round(code_value, places) == round(lifted, places):
            return 'CONVERSION', '%s scaled' % raw

    return 'MISMATCH', ', '.join(raw for raw, _ in found[:3])



# ============================================================
# ROW MATCHING
# ============================================================
#
# Four rules, first hit wins, and a rule must produce a UNIQUE row. A
# tie announces rather than picking: mis-tuning rule 3 produces visible
# UNMATCHED noise, which is recoverable, while a silent wrong match is
# the failure that would let this tool confirm its own mistakes.

MIN_PROSE_FRAGMENT = 24

NUMERIC_MASK_RE = re.compile(r'[-+]?\d[\d,\.]*(?:\s*[eE][-+]?\d+)?')
WORD_RE = re.compile(r'[a-z]{4,}')


def masked(text):
    """Lowercased, whitespace-collapsed, with every number masked.

    The mask is what keeps prose matching non-circular: the row is
    found by the words around the numbers, never by the numbers this
    tool is about to check.
    """
    low = ' '.join((text or '').lower().split())
    return NUMERIC_MASK_RE.sub('#', low)


def longest_common_run(left, right):
    """Length of the longest shared substring. Small inputs only."""
    if not left or not right:
        return 0
    previous = [0] * (len(right) + 1)
    best = 0
    for i in range(1, len(left) + 1):
        current = [0] * (len(right) + 1)
        for j in range(1, len(right) + 1):
            if left[i - 1] == right[j - 1]:
                current[j] = previous[j - 1] + 1
                if current[j] > best:
                    best = current[j]
        previous = current
    return best


def name_hit(cell, name):
    """Does an identifier cell name this unit?"""
    if not name:
        return False
    return name.lower() in strip_cell(cell).lower()


def match_row(table, unit_name, unit_text, code_value):
    """(row, rule, note) for the row about this value, or (None, ...).

    Returns rule 'AMBIGUOUS' when a rule matched more than one row.
    """
    id_index = table.column(ROLE_ID)
    if id_index is None:
        return None, 'NO_ID_COLUMN', ''

    def unique(hits, rule):
        if len(hits) == 1:
            return hits[0], rule, ''
        if len(hits) > 1:
            return None, 'AMBIGUOUS', '%d rows under %s' % (len(hits), rule)
        return None, '', ''

    # Rule 1 and 2 -- the identifier cell names the unit.
    hits = [row for row in table.rows
            if id_index < len(row[1]) and name_hit(row[1][id_index], unit_name)]
    row, rule, note = unique(hits, 'NAME')
    if row or rule:
        return row, rule, note

    # Rule 3 -- masked prose containment against identifier plus notes.
    if unit_text:
        target = masked(unit_text)
        hits = []
        for row in table.rows:
            cells = row[1]
            prose = ' '.join([
                cells[id_index] if id_index < len(cells) else '',
                table.cell(row[1], ROLE_NOTES)])
            if longest_common_run(masked(prose), target) >= MIN_PROSE_FRAGMENT:
                hits.append(row)
        row, rule, note = unique(hits, 'PROSE')
        if row or rule:
            return row, rule, note

    # Rule 4 -- the CODE-value cell equals this value, and at least one
    # content word is shared. Never the evidence column: finding the row
    # by the thing being checked is the circularity to avoid.
    if code_value is not None and table.column(ROLE_CODE) is not None:
        words = set(WORD_RE.findall(masked(unit_text or unit_name or '')))
        hits = []
        for row in table.rows:
            verdict, _ = compare(code_value, table.cell(row[1], ROLE_CODE))
            if verdict not in ('MATCH', 'CONVERSION'):
                continue
            prose = ' '.join([
                row[1][id_index] if id_index < len(row[1]) else '',
                table.cell(row[1], ROLE_NOTES)])
            if not words or words & set(WORD_RE.findall(masked(prose))):
                hits.append(row)
        row, rule, note = unique(hits, 'CODE_VALUE')
        if row or rule:
            return row, rule, note

    return None, '', ''


def classify_verdict(cell, default_scope=SCOPE_EITHER):
    """(class, token, scope) for one verdict cell.

    Exact match on the LEADING token only. Verdicts are never
    fuzzy-matched: two counts of this same corpus disagreed by up to 62
    on YES because two grep rules were used on it, so the token is read
    where the header role says it lives and the column that was read is
    reported alongside it.
    """
    text = strip_cell(cell)
    if not text:
        return V_EMPTY, '', default_scope
    low = text.lower()
    # A cell may carry a token plus a caveat behind a dash, a
    # semicolon, or a parenthesis. The token is what is read; the
    # caveat is prose for the human reading the report.
    head = re.split(r'\s+--\s+|\s*;\s*|\s*\(', low)[0].strip().strip('.')
    # Longest token first, so a two-word token is never read as its
    # first word alone.
    for token in sorted(VERDICT_TOKENS, key=len, reverse=True):
        own, scope = VERDICT_TOKENS[token]
        if head == token or head.startswith(token + ' '):
            return own, text, (default_scope if scope == SCOPE_EITHER
                               else scope)
    return V_UNREADABLE, text, default_scope


def is_compound(cell):
    """Does this cell carry a recognized token PLUS other prose?

    Classifying by the leading token and discarding the rest is the
    tool deciding a qualification does not matter, which is
    interpretation by omission. A compound cell is flagged and its
    whole text rides the quoting path, so the qualification reaches a
    reader instead of being trimmed away.
    """
    text = strip_cell(cell)
    if not text:
        return False
    low = text.lower().strip().strip('.')
    for token in sorted(VERDICT_TOKENS, key=len, reverse=True):
        if low == token:
            return False
        if low.startswith(token):
            return True
    return False


# Quoting a worksheet is TRANSCRIPTION, not interpretation. The token
# decides; prose informs. That distinction only survives if the quote
# is visibly separated from the tool's own words -- a live finding once
# read "reads NO -- wrong authority -- wrong authority for a value that
# may still be right", half checker and half template, and no reader
# could tell which half was evidence.
QUOTE_LIMIT = 160


def quoted(text):
    """A worksheet cell, delimited, and cut only with a visible marker."""
    body = strip_cell(text)
    if not body:
        return '(blank)'
    if len(body) > QUOTE_LIMIT:
        body = body[:QUOTE_LIMIT].rstrip() + ' [...]'
    return '<<%s>>' % body


def dispose_verdict(claim, own, token, scope, where, extra=''):
    """Record the finding a classified verdict produces, if any.

    One place, because the constant path and the string path must not
    grow two answers to the same question. SCOPE decides whether a
    refusal lands on the value or on the citation: a right number under
    a wrong authority is value-YES and citation-NO, and calling that a
    refuted value misclassifies in both directions.
    """
    tag = quoted(token)
    if own in VERDICT_CLEARS:
        return True
    if own == V_INCOMPLETE:
        # PARTIAL and APPROX return to the originator unconditionally,
        # without first asking why the row is qualified.
        claim.fail('L3', 'INCOMPLETE_CHECK',
                   '%s reads %s%s' % (where, tag, extra), 'SEND BACK')
    elif own == V_ABSENT:
        claim.fail('L3', 'CHECK_NOT_PERFORMED',
                   '%s reads %s; the annotation claims a completed '
                   'check%s' % (where, tag, extra), 'SEND BACK')
    elif own == V_SOURCE_ABSENT:
        claim.fail('L3', 'CITATION_DEFECT',
                   '%s reads %s -- the cited source does not publish '
                   'it%s' % (where, tag, extra), 'CONVERSATION')
    elif own == V_REFUTED:
        if scope == SCOPE_CITATION:
            claim.fail('L3', 'CITATION_DEFECT',
                       '%s reads %s -- wrong authority for a value that '
                       'may still be right%s' % (where, tag, extra),
                       'CONVERSATION')
        else:
            claim.fail('L3', 'REFUTED',
                       '%s reads %s -- the worksheet contradicts the '
                       'code%s' % (where, tag, extra), 'CONVERSATION')
    elif own == V_DERIVED:
        # Complete when it names its inputs, shows the arithmetic, and
        # the arithmetic closes -- and then the value inherits the rung
        # of its weakest input (L-158). Reading prose arithmetic is not
        # something this tool can do honestly, so it routes and says so.
        claim.fail('L3', 'DERIVED',
                   '%s: derivation review, inherits its weakest input%s'
                   % (where, extra), 'CONVERSATION')
    elif own == V_EMPTY:
        claim.fail('L3', 'EMPTY_VERDICT',
                   '%s has a blank verdict%s' % (where, extra), 'SEND BACK')
    else:
        claim.fail('L3', 'UNREADABLE_VERDICT',
                   '%s reads %s -- not in the vocabulary%s'
                   % (where, tag, extra), 'SEND BACK')
    return False


def read_verdict(table, cells):
    """(class, token, scope, column) from whichever column carries it."""
    if table.column(ROLE_VALUE_VERDICT) is not None:
        own, token, scope = classify_verdict(
            table.cell(cells, ROLE_VALUE_VERDICT), SCOPE_VALUE)
        return own, token, scope, 'value'
    if table.column(ROLE_RESOLUTION) is not None:
        own, token, scope = classify_verdict(
            table.cell(cells, ROLE_RESOLUTION), SCOPE_VALUE)
        return own, token, scope, 'resolution'
    if table.column(ROLE_CITATION_VERDICT) is not None:
        own, token, scope = classify_verdict(
            table.cell(cells, ROLE_CITATION_VERDICT), SCOPE_CITATION)
        return own, token, scope, 'citation-only'
    return None, '', SCOPE_EITHER, 'none'

# ============================================================
# THE UNITS AND THEIR ANNOTATIONS
# ============================================================

ASSIGN_NAME_RE = re.compile(r"^\s*([A-Za-z_][A-Za-z_0-9]*)\s*[:=]")
DICT_KEY_RE = re.compile(r"^\s*['\"]([^'\"]+)['\"]\s*:")


def anchor_label(lines, anchors, line_start):
    """The variable name or dict key that introduces a unit.

    A display string carries no name of its own, but the attachment
    rule already knows which entry introduces it, so the label is
    available without any new parsing.
    """
    anchor = anchors.get(line_start, line_start)
    if anchor < 1 or anchor > len(lines):
        return ''
    line = lines[anchor - 1]
    match = DICT_KEY_RE.match(line) or ASSIGN_NAME_RE.match(line)
    return match.group(1) if match else ''



# The orrery writes operating instructions into the same string as the
# science: a manual scale to set before the shell is visible, the
# frame weight of the resulting HTML. They are surface instructions,
# not claims about a body, and they are the only numbers in these
# strings that no worksheet row could ever address.
DISPLAY_INSTRUCTION_RE = re.compile(
    r'(?i)manual scale|manual scaled|mb per frame|to visualize|'
    r'to view closely|frame for html')

# Tight and directional on purpose. The instruction phrase sits right
# against its own number -- "MANUAL SCALE OF 0.005 AU", "4.6 MB PER
# FRAME" -- so a wide window reaches across the paragraph break and
# swallows the science claim that follows it.
INSTRUCTION_LOOKBACK = 30
INSTRUCTION_LOOKAHEAD = 25


def physical_claims(unit):
    """(claims, instruction_count) for a display string.

    Positions come from the scanner's own claim regex, so the rule for
    what counts as a numeric claim has exactly one owner; only the
    offsets are recomputed here, because the scanner reports claims
    without them.
    """
    text = unit.raw_value or ''
    if not text:
        return [(value, raw) for raw, _u, value
                in (unit.numeric_claims or [])], 0
    kept = []
    dropped = 0
    for match in ps.NUMERIC_CLAIM_RE.finditer(text):
        raw = match.group(1)
        try:
            value = float(raw.replace(',', ''))
        except ValueError:
            continue
        window = text[max(0, match.start() - INSTRUCTION_LOOKBACK):
                      match.end() + INSTRUCTION_LOOKAHEAD]
        if DISPLAY_INSTRUCTION_RE.search(window):
            dropped += 1
            continue
        kept.append((value, raw))
    return kept, dropped


class Claim(object):
    """One annotation, with the value it is attached to."""

    def __init__(self, module, path, unit, checker, date, worksheet, label):
        self.module = module
        self.path = path
        self.unit = unit
        self.checker = checker
        self.date = date
        self.worksheet = worksheet
        self.label = label
        self.findings = []          # (layer, code, detail)
        self.route = ''             # SEND BACK / CONVERSATION / ''
        self.notes = ''             # the matched row's Notes, verbatim
        self.verdict_column = ''
        self.matched_line = None

    @property
    def where(self):
        return '%s:%d' % (os.path.basename(self.path), self.unit.line_start)

    @property
    def display(self):
        return self.label or self.unit.display_name

    @property
    def code_value(self):
        if self.unit.kind == 'constant':
            return self.unit.value
        return None

    @property
    def claim_values(self):
        """Numbers a display string asserts about the WORLD.

        The orrery's display text opens with instructions to the
        person driving it -- a manual scale to set, a frame size to
        expect. Those are numbers, and no worksheet will ever carry a
        row for them, so counting them would inflate the denominator
        with claims that cannot be addressed even in principle. They
        are excluded and counted separately.
        """
        return [value for value, _raw in physical_claims(self.unit)[0]]

    @property
    def instruction_count(self):
        return physical_claims(self.unit)[1]

    def fail(self, layer, code, detail, route):
        self.findings.append((layer, code, detail))
        if route and self.route != 'SEND BACK':
            self.route = route


def collect_claims(project_dir):
    """Every annotation attached to a scored unit, plus what is not.

    The scanner owns attachment. Two definitions of which annotations
    belong to a value would drift apart by construction, so this reads
    the scanner's answer rather than computing a second one.
    """
    claims = []
    unreached = []
    files = 0
    for fname in sorted(os.listdir(project_dir)):
        if not fname.endswith('.py'):
            continue
        path = os.path.join(project_dir, fname)
        module = fname[:-3]
        try:
            role = ps.classify_role(module, path)
            units = ps.extract_units_from_file(path, module, role)
            with open(path, encoding='utf-8', errors='replace') as handle:
                lines = handle.read().splitlines(True)
            tree = ps.ast.parse(''.join(lines))
            anchors = ps.entry_anchor_map(tree)
        except Exception as exc:                          # noqa: BLE001
            unreached.append((fname, 0, 'file could not be read: %s' % exc))
            continue
        files += 1

        seen = set()
        for unit in units:
            records, _issues = ps.parse_cross_checks(unit.attached_text or '')
            if not records:
                continue
            label = anchor_label(lines, anchors, unit.line_start)
            for line_no in (unit.attached_lines or ()):
                seen.add(line_no)
            for checker, date, worksheet in records:
                claims.append(Claim(module, path, unit, checker, date,
                                    worksheet, label))

        for index, line in enumerate(lines):
            if ps.CROSS_CHECK_LINE_RE.match(line) and (index + 1) not in seen:
                unreached.append((fname, index + 1, line.strip()))

    return claims, unreached, files


# ============================================================
# THE LAYERS
# ============================================================

CHECKER_TOKENS = {
    'claude': ('claude',),
    'gpt': ('gpt',),
    'gemini': ('gemini',),
    'fable': ('fable',),
    'opus': ('claude', 'opus'),
}


def identity_token(checker):
    """Filename tokens a named checker's worksheet should carry."""
    low = ' '.join((checker or '').split()).lower()
    for name, tokens in CHECKER_TOKENS.items():
        if name in low:
            return tokens
    return ()


def check_claim(claim, worksheets, unregistered):
    """Run every layer against one annotation. Mutates the claim."""

    # ---- L0: the worksheet exists ------------------------------------
    sheet = worksheets.get(claim.worksheet)
    if sheet is None:
        claim.fail('L0', 'MISSING_WORKSHEET',
                   'no such file in %s' % WORKSHEET_DIR, 'SEND BACK')
        return

    # ---- LID: the worksheet belongs to the named checker -------------
    #
    # Two annotations naming different checkers over ONE checker's
    # evidence would pass every other layer and fake the rung. The
    # top rung means two DISTINCT checkers, so identity is part of the
    # claim, not decoration.
    tokens = identity_token(claim.checker)
    if tokens and not any(t in claim.worksheet.lower() for t in tokens):
        claim.fail('LID', 'IDENTITY_MISMATCH',
                   '%s cites a worksheet naming no such checker'
                   % claim.checker, 'SEND BACK')

    tables = [t for t in sheet['tables'] if t.is_row_table]
    for table in sheet['tables']:
        for header in table.unregistered:
            unregistered.add((claim.worksheet, table.header_line, header))

    if not tables:
        claim.fail('L1', 'WORKSHEET_UNREADABLE',
                   'no table in it identifies its rows', 'SEND BACK')
        return

    # ---- L1: the row is located --------------------------------------
    #
    # A CONSTANT is one value and matches one row. A DISPLAY STRING is
    # not: the worksheets carry one row per CLAIM, and a paragraph about
    # Eris's crust states several. Matching a string to a single row
    # would pick one claim and silently pass the rest, so the string
    # path checks every claim it makes and reports the fraction the
    # worksheet addressed.
    if claim.unit.kind == 'string':
        check_string_claim(claim, tables)
        return

    best = None
    ambiguous = ''
    for table in tables:
        row, rule, note = match_row(table, claim.label, '', claim.code_value)
        if row is not None:
            best = (table, row, rule)
            break
        if rule == 'AMBIGUOUS':
            ambiguous = note
    if best is None:
        if ambiguous:
            claim.fail('L1', 'AMBIGUOUS_ROW', ambiguous, 'SEND BACK')
        else:
            claim.fail('L1', 'UNMATCHED',
                       'no row in %s is about %s'
                       % (claim.worksheet, claim.display), 'SEND BACK')
        return

    table, (line_no, cells), rule = best
    claim.matched_line = line_no
    claim.match_rule = rule
    # Keyed to the MATCHED row and nothing else. No row, no quote -- a
    # tool hunting for a nearby note when the match failed would have
    # crossed from transcription into interpretation.
    claim.notes = table.cell(cells, ROLE_NOTES)

    # ---- L2a: the value agrees with the evidence ---------------------
    evidence = table.cell(cells, ROLE_EVIDENCE)
    if claim.code_value is not None and evidence:
        verdict, detail = compare(claim.code_value, evidence)
        if verdict == 'MISMATCH':
            claim.fail('L2a', 'MISMATCH',
                       'code %s, worksheet %s' % (claim.unit.value_str, detail),
                       'CONVERSATION')
        elif verdict == 'RANGE':
            claim.fail('L2a', 'RANGE', 'evidence is a range: %s' % detail, '')
        elif verdict == 'CONVERSION':
            claim.fail('L2a', 'MATCHED_VIA_CONVERSION', detail, '')

    # ---- L2b: drift since the check ----------------------------------
    #
    # The code-value cell is what the checker read at the prompt's SHA.
    # Comparing it to the code NOW is the committed-history failure
    # caught directly rather than inferred. It exists only where the
    # schema carries the column, and the coverage count says so.
    recorded = table.cell(cells, ROLE_CODE)
    if claim.code_value is not None and recorded:
        verdict, detail = compare(claim.code_value, recorded)
        if verdict == 'MISMATCH':
            claim.fail('L2b', 'DRIFTED',
                       'code now %s, checker read %s'
                       % (claim.unit.value_str, detail), 'CONVERSATION')

    # ---- L3: the verdict is read -------------------------------------
    own, token, scope, column = read_verdict(table, cells)
    claim.verdict_column = column
    if own is None:
        claim.fail('L3', 'NO_VERDICT_COLUMN',
                   'the matched table records no verdict', 'SEND BACK')
        return
    if column == 'citation-only':
        # The constants worksheets carry ONLY a citation verdict. That
        # row records whether the cited source publishes the number --
        # a real check, and not the same claim as "the value is right."
        # Reported as its own class; nothing is promoted quietly, and
        # whether it earns a leg is a ruling, not a default.
        claim.fail('L3', 'VALUE_VERDICT_ABSENT',
                   'worksheet records a citation verdict only (%s)'
                   % (token or 'empty'), '')
    claim.verdict_class = own
    claim.verdict_token = token
    dispose_verdict(claim, own, token, scope,
                    'row %d' % (claim.matched_line or 0))


# ============================================================
# THE STRING PATH -- one row per CLAIM, not per string
# ============================================================
#
# The rung is per-unit; the evidence is per-claim. A display string can
# assert half a dozen numbers and the worksheets record one row for
# each, so the honest output for a string is a fraction: how many of
# the claims this string makes did the worksheet actually address.
#
# The denominator is bounded by what the string contains at this
# commit, so it cannot grow by imagination.

BODY_STOPWORDS = ('visualization', 'shells', 'configs', 'info', 'text')


def body_token(module):
    """The body a shells module is about -- 'eris' from eris_...shells."""
    for part in module.split('_'):
        if part and part not in BODY_STOPWORDS:
            return part
    return ''


def claim_rows(tables, value, string_text, token):
    """Rows recording one claim of this string, best table first.

    Matching runs against the CODE-VALUE column where the schema has
    one, and against the IDENTIFIER cell where it does not -- the
    followup worksheets state the number inside the question they are
    resolving ("Eris Hill radius at 67.8 AU"). Neither is the evidence
    column, which is the point: finding a row by the number about to be
    checked would make L2a confirm itself.

    The word filter is what stops a coincidental numeric equality in
    another body's row from being taken as this string's evidence. The
    body token comes from the module the annotation lives in.
    """
    words = set(WORD_RE.findall(masked(string_text)))
    if token:
        words.add(token)
    hits = []
    for table in tables:
        id_index = table.column(ROLE_ID)
        use_code = table.column(ROLE_CODE) is not None
        for line_no, cells in table.rows:
            id_cell = (cells[id_index] if id_index is not None
                       and id_index < len(cells) else '')
            if use_code:
                verdict, _detail = compare(value, table.cell(cells,
                                                             ROLE_CODE))
            else:
                verdict, _detail = compare(value, id_cell)
            if verdict not in ('MATCH', 'CONVERSION'):
                continue
            prose = ' '.join([id_cell, table.cell(cells, ROLE_NOTES)])
            row_words = set(WORD_RE.findall(masked(prose)))
            source_cell = (table.cell(cells, ROLE_CODE) if use_code
                           else id_cell)
            if token:
                if token in row_words:
                    hits.append((table, line_no, cells, source_cell))
            elif words & row_words:
                hits.append((table, line_no, cells, source_cell))
    return hits


def check_string_claim(claim, tables):
    """L1-L3 for a display string, per claim rather than per row."""
    values = claim.claim_values
    claim.claims_present = len(values)
    text = claim.unit.raw_value or ''
    token = body_token(claim.module)

    if not values:
        # Nothing numeric to check. The annotation still asserts a
        # check happened; it is simply not one this tool can read.
        claim.fail('L1', 'NO_NUMERIC_CLAIM',
                   'the string states no numeric claim to check', '')
        return

    addressed = 0
    for value in values:
        hits = claim_rows(tables, value, text, token)
        if not hits:
            continue
        addressed += 1
        table, line_no, cells, source_cell = hits[0]
        claim.matched_line = line_no
        claim.notes = table.cell(cells, ROLE_NOTES)

        evidence = table.cell(cells, ROLE_EVIDENCE)
        if evidence:
            verdict, detail = compare(value, evidence)
            if verdict == 'MISMATCH' and len(numbers_in(source_cell)) > 1:
                # The row states this value in more than one unit and
                # the evidence cell answers in only one of them. The
                # tool cannot pair them across cells, so it says that
                # rather than reporting a unit difference as a value
                # error. Loud is reserved for a real disagreement.
                claim.fail('L2a', 'UNPAIRED_UNITS',
                           'row %d states the value in more than one unit; '
                           'evidence reads %s' % (line_no, detail), '')
            elif verdict == 'MISMATCH':
                claim.fail('L2a', 'MISMATCH',
                           'code %g, worksheet %s (row %d)'
                           % (value, detail, line_no), 'CONVERSATION')
            elif verdict == 'RANGE':
                claim.fail('L2a', 'RANGE',
                           'evidence is a range: %s (row %d)'
                           % (detail, line_no), '')
            elif verdict == 'CONVERSION':
                claim.fail('L2a', 'MATCHED_VIA_CONVERSION',
                           '%s (row %d)' % (detail, line_no), '')

        own, tok, scope, column = read_verdict(table, cells)
        claim.verdict_column = column
        if own is None:
            claim.fail('L3', 'NO_VERDICT_COLUMN',
                       'row %d records no verdict' % line_no, 'SEND BACK')
            continue
        if column == 'citation-only':
            claim.fail('L3', 'VALUE_VERDICT_ABSENT',
                       'row %d records a citation verdict only' % line_no,
                       '')
        dispose_verdict(claim, own, tok, scope, 'row %d' % line_no,
                        ' for %g' % value)

    claim.claims_addressed = addressed
    if addressed == 0:
        claim.fail('L1', 'UNMATCHED',
                   'no row in %s records any of the %d numeric claims '
                   'this string makes'
                   % (claim.worksheet, len(values)), 'SEND BACK')
    elif addressed < len(values):
        claim.fail('L1', 'CLAIMS_UNADDRESSED',
                   '%d of %d numeric claims have no row'
                   % (len(values) - addressed, len(values)), '')



# ============================================================
# THE UNCITED SET
# ============================================================
#
# An uncited worksheet is PENDING WORK, not a defect: the provenance
# sweep is incomplete and those files cover code not yet annotated.
# One line steady-state with the date the set last changed; the full
# list prints only when the set differs from the recorded state.

def load_state(project_dir):
    path = os.path.join(project_dir, STATE_PATH)
    try:
        with open(path, encoding='utf-8') as handle:
            return json.load(handle)
    except (IOError, OSError, ValueError):
        return {}


def save_state(project_dir, state):
    path = os.path.join(project_dir, STATE_PATH)
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w', encoding='utf-8', newline='\n') as handle:
            json.dump(state, handle, indent=2, sort_keys=True)
            handle.write('\n')
    except (IOError, OSError):
        pass


def uncited_report(project_dir, worksheets, cited, today):
    """(headline, changed_lines, state) for the uncited set."""
    prompts = sorted(name for name in worksheets
                     if 'prompt' in name.lower())
    uncited = sorted(name for name in worksheets
                     if name not in cited and name not in prompts)
    state = load_state(project_dir)
    previous = state.get('uncited', None)
    since = state.get('uncited_changed', today)

    changed = []
    if previous is None:
        changed = ['first recorded run -- %d uncited worksheets'
                   % len(uncited)]
        since = today
    elif sorted(previous) != uncited:
        gained = [n for n in uncited if n not in previous]
        lost = [n for n in previous if n not in uncited]
        for name in gained:
            changed.append('now uncited: %s' % name)
        for name in lost:
            changed.append('now cited:   %s' % name)
        since = today

    state['uncited'] = uncited
    state['uncited_changed'] = since
    state['prompts'] = prompts
    headline = ('%d uncited worksheets pending wiring, %d prompt files '
                '-- unchanged since %s' % (len(uncited), len(prompts), since))
    return headline, changed, state, uncited


# ============================================================
# REPORT
# ============================================================

def write_report(project_dir, claims, unreached, unregistered,
                 headline, changed, uncited, files, worksheets):
    """The findings file. The console gets one line; this gets the rest."""
    out = []
    add = out.append

    routed = [c for c in claims if c.route]
    send_back = [c for c in claims if c.route == 'SEND BACK']
    conversation = [c for c in claims if c.route == 'CONVERSATION']
    clean = [c for c in claims if not c.findings]
    noted = [c for c in claims if c.findings and not c.route]

    add('# Worksheet Check (L-192)')
    add('')
    add('Generated by `worksheet_checker.py`. Report-only: this file '
        'does not gate a push.')
    add('')
    add('## Denominator')
    add('')
    add('| | Count |')
    add('|---|---:|')
    add('| Python files read | %d |' % files)
    add('| Worksheets on disk | %d |' % len(worksheets))
    add('| Annotations attached to a scored unit | %d |' % len(claims))
    add('| Clean -- every layer passed | %d |' % len(clean))
    add('| Routed to SEND BACK | %d |' % len(send_back))
    add('| Routed to CONVERSATION | %d |' % len(conversation))
    add('| Noted, no route | %d |' % len(noted))
    add('| Annotation lines the scanner does not score | %d |'
        % len(unreached))
    add('')

    add('## SEND BACK -- the cause is known')
    add('')
    add('Send-back fires on INCOMPLETENESS. The answer is a better '
        'worksheet: reopen the session that produced it and ask for a new '
        'file, rather than editing the original, which is the record of '
        'what was known on its date.')
    add('')
    if send_back:
        add('| Where | Value | Checker | Worksheet | Finding | '
            'What the checker wrote |')
        add('|---|---|---|---|---|---|')
        for claim in send_back:
            first = claim.findings[0]
            add('| `%s` | %s | %s | `%s` | **%s** -- %s | %s |'
                % (claim.where, claim.display, claim.checker,
                   claim.worksheet, first[1], first[2],
                   quoted(claim.notes)))
    else:
        add('None.')
    add('')

    add('## CONVERSATION -- the cause is open')
    add('')
    add('A complete row that disagrees is a FINDING, not a defective '
        'worksheet. No tool assigns the cause. Three outcomes are live: '
        'a convention mismatch, a wrong value in the code, or a wrong '
        'derivation in the worksheet.')
    add('')
    if conversation:
        add('| Where | Value | Worksheet | Row | Finding | '
            'What the checker wrote |')
        add('|---|---|---|---|---|---|')
        for claim in conversation:
            for layer, code, detail in claim.findings:
                add('| `%s` | %s | `%s` | %s | **%s** -- %s | %s |'
                    % (claim.where, claim.display, claim.worksheet,
                       claim.matched_line or '-', code, detail,
                       quoted(claim.notes)))
    else:
        add('None.')
    add('')

    add('## Noted, no route')
    add('')
    if noted:
        add('| Where | Value | Note |')
        add('|---|---|---|')
        for claim in noted:
            for layer, code, detail in claim.findings:
                add('| `%s` | %s | %s -- %s |'
                    % (claim.where, claim.display, code, detail))
    else:
        add('None.')
    add('')

    add('## What this tool cannot see')
    add('')
    add('Printed rather than left silent. Silence about something '
        'unexamined is the failure this layer exists to prevent.')
    add('')
    add('### Annotation lines attached to no scored unit (%d)'
        % len(unreached))
    add('')
    add('These grant no credit and cannot be checked here. Scanner reach '
        'is L-190, not a defect in this tool.')
    add('')
    if unreached:
        for fname, line_no, text in unreached:
            add('- `%s:%d` -- %s' % (fname, line_no, text[:96]))
    else:
        add('None.')
    add('')
    add('### Header sets the registry does not recognise (%d)'
        % len(unregistered))
    add('')
    if unregistered:
        for sheet, line_no, header in sorted(unregistered):
            add('- `%s` line %d -- column %r' % (sheet, line_no, header))
    else:
        add('None.')
    add('')
    add('### Outside the bounds by construction')
    add('')
    add('- The eighteen inline literals duplicating cited constants. No '
        'worksheet names them, so no annotation points at them.')
    add('- Derivation arithmetic. A DERIVED row is routed, never graded.')
    add('')

    add('## Uncited worksheets')
    add('')
    add(headline)
    add('')
    if changed:
        add('**The set changed:**')
        add('')
        for line in changed:
            add('- %s' % line)
        add('')
        for name in uncited:
            add('- `%s`' % name)
        add('')

    path = os.path.join(project_dir, REPORT_PATH)
    with open(path, 'w', encoding='utf-8', newline='\n') as handle:
        handle.write('\n'.join(out) + '\n')
    return path


# ============================================================
# MAIN
# ============================================================

def load_worksheets(project_dir):
    """Every worksheet on disk, parsed into tables."""
    directory = os.path.join(project_dir, WORKSHEET_DIR)
    sheets = {}
    for name in sorted(os.listdir(directory)):
        if not name.endswith('.md'):
            continue
        path = os.path.join(directory, name)
        with open(path, encoding='utf-8', errors='replace') as handle:
            text = handle.read()
        sheets[name] = {'path': path, 'tables': parse_tables(name, text)}
    return sheets


def run(project_dir, today):
    """Returns (summary_line, report_path, counts)."""
    worksheets = load_worksheets(project_dir)
    claims, unreached, files = collect_claims(project_dir)

    unregistered = set()
    for claim in claims:
        check_claim(claim, worksheets, unregistered)

    cited = set(claim.worksheet for claim in claims)
    headline, changed, state, uncited = uncited_report(
        project_dir, worksheets, cited, today)
    save_state(project_dir, state)

    report = write_report(project_dir, claims, unreached, unregistered,
                          headline, changed, uncited, files, worksheets)

    send_back = sum(1 for c in claims if c.route == 'SEND BACK')
    conversation = sum(1 for c in claims if c.route == 'CONVERSATION')
    clean = sum(1 for c in claims if not c.findings)
    counts = {
        'annotations': len(claims),
        'clean': clean,
        'send_back': send_back,
        'conversation': conversation,
        'unreached': len(unreached),
        'unregistered': len(unregistered),
    }

    # The summary line carries its denominator on purpose. A line that
    # always reads the same is wallpaper, and wallpaper is a check that
    # cannot fail.
    #
    # It is also SHORT on purpose. maintenance_run.py trims a checker's
    # verdict to 44 characters, and the first version of this line was
    # 101 -- so the runner row showed the denominator, which never
    # moves, and truncated away the two counts that do. The detail
    # belongs on its own line, which the standalone run prints and the
    # runner does not read.
    routed = send_back + conversation
    detail = ('Routing: %d send back, %d to conversation, %d noted, '
              '%d not scanner-reachable'
              % (send_back, conversation,
                 len(claims) - routed - clean, len(unreached)))
    summary = ('WORKSHEET CHECK: %d of %d routed, %d clean'
               % (routed, len(claims), clean))
    return summary, report, counts, headline, changed, detail


def main():
    project_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_dir)

    directory = os.path.join(project_dir, WORKSHEET_DIR)
    if not os.path.isdir(directory):
        print('Worksheet checker DID NOT RUN: %s is missing.' % WORKSHEET_DIR)
        return 1

    try:
        import datetime
        today = datetime.date.today().isoformat()
        summary, report, counts, headline, changed, detail = run(
            project_dir, today)
    except Exception as exc:                              # noqa: BLE001
        import traceback
        print('Worksheet checker DID NOT RUN: %s' % exc)
        traceback.print_exc()
        return 1

    print('=' * 70)
    print('WORKSHEET CHECKER -- does the worksheet say it? (L-192)')
    print('=' * 70)
    print('  %s' % headline)
    for line in changed:
        print('    %s' % line)
    if counts['unregistered']:
        print('  %d worksheet column(s) the registry does not recognise '
              '-- see the report' % counts['unregistered'])
    print()
    print('  ' + detail)
    print('  ' + summary)
    print('  Findings written to %s' % REPORT_PATH)
    print('=' * 70)
    return 0


if __name__ == '__main__':
    sys.exit(main())
