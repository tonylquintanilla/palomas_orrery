"""Worksheet request builder -- ask the question the checker can read.

Role: devtool
Domain: dev_tools

Module created: August 2026 with Anthropic's Claude Opus 5.

WHAT THIS IS FOR

The checker (worksheet_checker.py) judges a worksheet that came back.
This module writes the worksheet that goes out. Keeping them apart is
deliberate: the checker is read-only over the corpus, and a builder
living inside it would put a writer behind that boundary.

The two modules share worksheet_keys.py, and that sharing is the point.
A key minted here and resolved there must be the same key. If the
builder computed the enclosing name one way and the checker computed it
another, a key could be born stale -- minted correctly, unresolvable
forever, with nothing to say so.

THE SCHEMA IT EMITS (Tony's rulings, 2026-08-15)

Four response fields per row:

  1. Code value at the time of the check -- PRE-FILLED by this module.
  2. Value verdict, plus the number, or a range with its reduction
     rule. The object is a NUMBER. Break 2 ruled that a claim with no
     number is out of scope here; see L-194.
  3. Citation verdict, asked SEPARATELY, and scoped to the `# Source:`
     line only. Break 5.
  4. Notes.

One pre-printed row per (key, ordinal). A constant asserts one value
and gets one row; a display string states several and gets one row per
claim, because matching a paragraph to a single row would pick one
claim and silently pass the rest.

WHY THE CITATION LEGS SIT ABOVE THE TABLE, NOT IN IT

Break 5 scopes the citation verdict to the `# Source:` line, with
`# Ref:` and `# Also:` visible but never verdicted. Both could have
been columns. They are not, for two reasons. The response table already
carries nine columns and a tenth makes it unreadable in the editors
these worksheets are actually filled in. And a leg sitting in a cell
invites a verdict token to be typed beside it, which is exactly the
compound answer the checker is forbidden to interpret. Above the table
they are prose, addressed to a reader, with no cell to fill.

WHAT THIS MODULE DOES NOT DO

It does not judge. No verdict token, no pass, no fail, no route. It
reads the corpus, mints keys, and prints questions. Every claim about
what an answer MEANS belongs to the checker.

RUNNING IT

Open in VS Code and press Run. No command-line flags; it asks three
questions in the console, in this order.

  1. WHICH ROWS. A numbered list of the named selections defined in
     this module. The prompt DEFAULTS TO 1 -- the whole corpus -- so
     pressing Enter here produces a request over every annotated row
     rather than the slice you meant. Type the number.
  2. BATCH NAME. Becomes the filename, and is recorded in the request
     header.
  3. ANCHOR SHA. The commit this request describes. A returned row is
     checked against it later, so it must be current HEAD at the
     moment of the run -- commit something afterwards and re-run.

It writes TWO files into documentation/worksheets/, both rendered from
the same Request list so there is no second source of truth:

    REQUEST_<batch>.jsonl   what goes out
    REQUEST_<batch>.md      the fallback, if a return will not parse

It refuses rather than overwriting if either name already exists, and
it refuses to write at all if a selection matches no rows -- an empty
worksheet is indistinguishable from a finished one once it is out of
the room.

It is also a launch card in palomas_orrery_dashboard.py, under
Developer Tools, which opens it in its own console window.
"""

import hashlib
import json
import os
import re
import sys

import worksheet_checker as wc
import worksheet_keys as wk

OUTPUT_DIR = os.path.join('documentation', 'worksheets')

# The leg the citation verdict answers, and the legs that are shown
# but never verdicted. Break 5, 2026-08-15.
VERDICTED_LEG = 'Source'
CONTEXT_LEGS = ('Ref', 'Also', 'See', 'Derived', 'Calculation')

# The optional `+` is the continuation marker stage 1 placed on wrapped
# citation lines (L-195). It is leg-specific on purpose: a `# Ref+:`
# sitting under a `# Source:` line is a mismatch that can be named,
# where a generic continuation marker would have nothing to compare
# against.
LEG_RE = re.compile(
    r'^\s*#\s*(%s)(\+)?:\s*(.*)$'
    % '|'.join((VERDICTED_LEG,) + CONTEXT_LEGS))

# Recognising an UNMARKED continuation, so the builder can refuse one.
# This is the rule the two marking patches used, and it was validated by
# reproducing stage 1's answer set exactly: 48 runs, 96 lines, the same
# line numbers.
#
# Padding is the discriminator, and it is checked FIRST. A line aligned
# under the leg above it is continuation text no matter what punctuation
# it contains, so '#         Highly ellipsoidal: 1050x840x537 km' is a
# continuation and not a label called 'Highly ellipsoidal'. The label
# test runs second and is deliberately loose about leading whitespace,
# so that the padding test is the thing deciding the case rather than an
# accident of how many spaces the label pattern happens to allow. Delete
# the padding test and that line reads as a label -- which is the bug
# the first version of this detector had.
COMMENT_RE = re.compile(r'^\s*#')
PADDED_RE = re.compile(r'^\s*#\s{2,}\S')
OTHER_LABEL_RE = re.compile(r'^\s*#\s*([A-Za-z][A-Za-z0-9_ /.-]{0,30})\+?:')


def continues_a_leg(line):
    """True when this comment line is unlabelled continuation text."""
    if not COMMENT_RE.match(line) or line.strip() == '#':
        return False
    if PADDED_RE.match(line):
        return True
    return not OTHER_LABEL_RE.match(line)

# Columns of the response table, in order. The header text is what the
# checker's HEADER_ROLES maps; changing a string here without changing
# it there produces a column the checker cannot read, which it reports
# as unrecognised rather than silently skipping.
COLUMNS = ('#', 'Key', 'Claim', 'Code value', 'Your value', 'Source',
           'Value correct?', 'Citation correct?', 'Notes')

CLAIM_EXCERPT = 90


def cell_safe(text):
    """Text that cannot break out of a markdown table cell."""
    flat = ' '.join((text or '').replace('|', '/').split())
    return flat.replace('<br>', ' ')


def excerpt(text, limit=CLAIM_EXCERPT):
    flat = cell_safe(text)
    if len(flat) <= limit:
        return flat
    return flat[:limit - 3].rstrip() + '...'


def legs_of(attached_text):
    """(verdicted, context, problems, joined) legs from a comment run.

    Returns the `# Source:` lines and, separately, every other leg.
    Both are lists: a run carrying two Source lines is a malformation
    (L-195) and this reports both rather than picking one.

    A citation too long for one line continues on a marked line naming
    the leg it continues -- `# Source+:` under `# Source:`. Those are
    joined back onto their leg here, so the worksheet quotes the whole
    citation rather than its first line.

    `problems` holds continuation markers that could not be joined: one
    naming a different leg than the line above it, or one with no leg
    above it at all. Their text is reported and NOT joined, because
    attaching it to the wrong authority is the failure this marker was
    made leg-specific to catch. `joined` counts the lines that did join,
    so a run that joins nothing says so rather than looking identical to
    a run with nothing to join.

    `unmarked` holds continuation text carrying no marker at all. That
    text is invisible everywhere -- not joined, and not printed into the
    worksheet the way a mismatched marker is -- so the builder refuses
    to write a request while any exists, rather than reporting it. Each
    entry is the offending line, stripped.
    """
    verdicted = []
    context = []
    problems = []
    unmarked = []
    joined = 0
    open_label = None
    open_leg = None
    for line in (attached_text or '').splitlines():
        match = LEG_RE.match(line)
        if not match:
            # A line that continues the leg above it but carries no
            # marker is the failure this refuses on. Anything else
            # closes the run, so a marker separated from its leg by
            # unrelated prose cannot join across the gap.
            if open_label is not None and continues_a_leg(line):
                unmarked.append(line.strip())
                continue
            open_label = None
            open_leg = None
            continue
        label = match.group(1)
        marker = match.group(2)
        body = match.group(3).strip()
        if marker:
            if open_label is None:
                problems.append(
                    '`%s+:` continuation with no leg above it to join'
                    % label)
            elif label != open_label:
                problems.append(
                    '`%s+:` continuation under a `%s:` leg'
                    % (label, open_label))
            else:
                open_leg[-1] = (open_leg[-1] + ' ' + body).strip()
                joined += 1
            continue
        if label == VERDICTED_LEG:
            verdicted.append(body)
            open_leg = verdicted
        else:
            context.append('%s: %s' % (label, body))
            open_leg = context
        open_label = label
    return verdicted, context, problems, unmarked, joined


class Request(object):
    """One pre-printed row: a key, a claim, and the code's value."""

    def __init__(self, key, claim, code_value, where, cited, context,
                 problems=(), unmarked=(), joined=0):
        self.key = key
        self.claim = claim
        self.code_value = code_value
        self.where = where
        self.cited = cited          # list of `# Source:` bodies
        self.context = context      # list of other legs, read-only
        self.problems = list(problems)  # markers that could not join
        self.unmarked = list(unmarked)  # continuation text with no marker
        self.joined = joined        # continuation lines joined on
        self.row_id = ''


def requests_for_claim(claim, source_text):
    """Every row one annotation should produce.

    A constant is one row. A display string is one row per numeric
    claim it makes, numbered from 1 in the order the scanner finds
    them -- the same order the checker's ordinal means.
    """
    cited, context, problems, unmarked, joined = legs_of(
        claim.unit.attached_text)
    where = '%s:%d' % (os.path.basename(claim.path), claim.unit.line_start)

    if claim.unit.kind == 'constant':
        key = wk.key_for_site(claim.path, source_text,
                              claim.unit.line_start, claim.label, None)
        return [Request(key, claim.label,
                        claim.unit.value_str, where, cited, context,
                        problems, unmarked, joined)]

    rows = []
    values, _dropped = wc.physical_claims(claim.unit)
    text = claim.unit.raw_value or ''
    for index, (_value, raw) in enumerate(values, start=1):
        key = wk.key_for_site(claim.path, source_text,
                              claim.unit.line_start, claim.label, index)
        rows.append(Request(key, excerpt(text), raw, where,
                            cited, context, problems, unmarked, joined))
    return rows


# ============================================================
# SELECTION -- ASKING THE BUILDER FOR FEWER ROWS (L-201)
# ============================================================
#
# A selection is CODE, not typing. Each entry below is a name, a
# one-line statement of what it is for, and a rule. A pilot chosen by
# hand is a one-off no matter how carefully it is chosen, because
# nothing records why those rows and nothing can produce them again.
# An entry here is reviewable in a diff, pinned to a SHA, and
# reproducible by anyone who runs the tool.
#
# Blank at the prompt means the whole corpus, so the behaviour before
# this existed is still the default.
#
# WHERE SELECTION HAPPENS: after the L-196 refusal, never before.
# Excluding a site must never excuse an unmarked continuation, and a
# ratchet with a bypass is not a ratchet.
#
# The ORDER in main() is not what enforces that, and saying so was
# wrong when first written here. What enforces it is the collection the
# refusal loop reads: it iterates the whole corpus, never the selected
# subset. Reordering main() so selection runs first changes nothing --
# measured, by doing it. The mutation that DOES bypass the ratchet is
# one line, `for request in selected`, and it writes a request over a
# corpus holding an unmarked continuation. test_worksheet_request_
# builder.py pins the invariant against exactly that edit.

# The checker writes this. A selection may read a key list ONLY when
# the checker wrote it -- never one a person typed. The test is whether
# the list can be regenerated: a checker-written list can, a remembered
# one cannot.
ROUTED_PATH = os.path.join('data', 'worksheet_routed.json')


class Selection(object):
    """One named way to choose rows.

    `rule` is a predicate over a Request, or None for the whole corpus.
    `keys_from` names a checker-written JSON file whose keys are the
    selection; it is read at run time, and a missing file is an ERROR
    rather than an empty result.
    """

    def __init__(self, name, why, rule=None, keys_from=None):
        self.name = name
        self.why = why
        self.rule = rule
        self.keys_from = keys_from


def _file_of(request):
    return request.where.split(':')[0]


def _is_constants_new(request):
    return _file_of(request) == 'constants_new.py'


SELECTIONS = (
    Selection('all', 'the whole annotated corpus'),
    Selection('constants_new',
              'constants_new.py only -- the pilot slice (L-201). Its '
              'branch coverage is a property of the file, not of '
              'anyone\'s judgement about which rows are interesting.',
              rule=_is_constants_new),
    Selection('sendbacks',
              'rows the checker last routed SEND BACK, read from %s'
              % ROUTED_PATH,
              keys_from=ROUTED_PATH),
)


def routed_keys(project_dir, path):
    """(keys, error) from a checker-written routing file.

    Returns a set of keys, or an error string. A missing or unreadable
    file is an error and stops the run: selecting from a list that is
    not there would otherwise produce an empty request that looks like
    a finished one.
    """
    full = os.path.join(project_dir, path)
    if not os.path.isfile(full):
        return None, ('%s does not exist. Run worksheet_checker.py '
                      'first -- it writes the routing file this '
                      'selection reads.' % path)
    try:
        with open(full, encoding='utf-8') as handle:
            data = json.load(handle)
    except (IOError, OSError, ValueError) as exc:
        return None, '%s could not be read: %s' % (path, exc)
    keys = data.get('send_back') if isinstance(data, dict) else None
    if not isinstance(keys, list):
        return None, ('%s carries no "send_back" list. It was written '
                      'by something other than the checker, or by an '
                      'older version of it.' % path)
    return set(str(key) for key in keys), None


def apply_selection(selection, requests, project_dir='.'):
    """(selected, error) for one named selection."""
    if selection.keys_from:
        keys, error = routed_keys(project_dir, selection.keys_from)
        if error:
            return None, error
        return [r for r in requests if r.key in keys], None
    if selection.rule is None:
        return list(requests), None
    return [r for r in requests if selection.rule(r)], None


# ============================================================
# ROW INTEGRITY HASH (L-202)
# ============================================================
#
# The case is ATTRIBUTION, not tamper-proofing.
#
# The request tells a responder not to edit the Key, Claim or Code
# value columns, and nothing verifies it. A responder who rounds a code
# value produces a row that looks fine, and the checker's L2b layer
# then compares the code NOW against the value the worksheet recorded,
# finds a mismatch, and reports that the CODE drifted -- sending
# somebody to investigate a constant that never moved. The defect is in
# the worksheet and the report names the code.
#
# Eight hex characters over the three fields, joined and
# whitespace-normalized, let the checker say the true thing instead:
# this row's immutable half was modified.
#
# A MISSING hash FAILS the row on the checker side. A hash that quietly
# passes when absent is a check that cannot fail.

HASH_CHARS = 8


def row_hash(key, claim, code_value):
    """Short digest over the fields a responder must not edit."""
    parts = []
    for field in (key, claim, code_value):
        parts.append(' '.join(str(field if field is not None else '').split()))
    blob = '\n'.join(parts).encode('utf-8')
    return hashlib.sha256(blob).hexdigest()[:HASH_CHARS]


def verdict_vocabulary():
    """The accepted verdict words, grouped, read from the checker.

    Read rather than retyped. A list written out here would be a second
    store of the same fact, free to drift from the registry the checker
    actually enforces -- and a request naming a word the checker
    rejects sends a responder to write UNREADABLE.
    """
    groups = {}
    for token in sorted(wc.VERDICT_TOKENS):
        own, scope = wc.VERDICT_TOKENS[token]
        groups.setdefault(own, {'words': [], 'scope': scope})
        groups[own]['words'].append(token)
    return [(own, groups[own]['words'], groups[own]['scope'])
            for own in sorted(groups)]


def build(project_dir='.'):
    """(requests, skipped) for the whole annotated corpus."""
    claims, _unreached, _files = wc.collect_claims(project_dir)

    sources = {}
    requests = []
    skipped = []
    seen = set()
    for claim in claims:
        name = os.path.basename(claim.path)
        if name not in sources:
            try:
                with open(claim.path, encoding='utf-8',
                          errors='replace') as handle:
                    sources[name] = handle.read()
            except OSError as exc:
                sources[name] = ''
                skipped.append((name, 'unreadable: %s' % exc))
        for request in requests_for_claim(claim, sources[name]):
            # One annotation can be recorded by two checkers, which is
            # two claims over one site. The site is asked about once.
            if request.key in seen:
                continue
            seen.add(request.key)
            requests.append(request)
    return requests, skipped


def render(requests, batch, sha, repo_url, skipped, selection,
           corpus_size):
    """The request file, as markdown the checker can read back."""
    out = []
    out.append('# Cross-check request -- %s' % batch)
    out.append('')
    out.append('**Built on `%s` at %s.**' % (sha, repo_url))
    out.append('')
    out.append('Extractor version: %d. Key format: '
               '`module.py::enclosing::label::cN`.' % wk.EXTRACTOR_VERSION)
    out.append('')
    out.append('Selection: `%s` -- %s' % (selection.name, selection.why))
    out.append('')
    out.append('%d of %d rows in the corpus. The KEY identifies a row; '
               'the number in the first column is assigned by position '
               'in this file and means nothing outside it.'
               % (len(requests), corpus_size))
    out.append('')
    out.append('Do not edit the Key, Claim or Code value columns. They '
               'record what the code said at the SHA above, and the '
               'checker compares your answer against that state.')
    out.append('')

    out.append('## What each column asks')
    out.append('')
    out.append('- **Your value** -- the number the source states. If the '
               'sources disagree, give the range AND the rule you used '
               'to reduce it (for example "2.5-2.7, took the midpoint '
               'to two significant figures").')
    out.append('- **Source** -- the authority you consulted, specific '
               'enough to find again.')
    out.append('- **Value correct?** -- about the NUMBER only.')
    out.append('- **Citation correct?** -- about the code\'s cited '
               'source only, shown per row below. Answer it separately '
               'from the value: a right number under a wrong authority '
               'is a real finding and one token cannot say it.')
    out.append('- **Notes** -- anything a token cannot carry. The '
               'checker reads notes as prose for a human, never as a '
               'verdict.')
    out.append('')
    out.append('Use one token per verdict cell. A cell holding a token '
               'plus a qualification is reported as unclassified rather '
               'than read, because guessing which half you meant is the '
               'interpretation this system is built to avoid.')
    out.append('')

    # Read from the checker's own registry rather than retyped here. A
    # list written out in this file would be free to drift from the one
    # the checker enforces, and a request naming a word the checker
    # rejects sends a responder to write UNREADABLE.
    out.append('## The accepted verdict words')
    out.append('')
    out.append('Anything outside this list is read as unclassified and '
               'the row comes back.')
    out.append('')
    for own, words, scope in verdict_vocabulary():
        answers = {'value': 'the value only',
                   'citation': 'the citation only'}.get(
                       scope, 'whichever question the column asks')
        out.append('- **%s** -- %s (answers %s)'
                   % (own, ', '.join('`%s`' % w for w in words), answers))
    out.append('')

    out.append('## Rows in context (read-only)')
    out.append('')
    for request in requests:
        out.append('**%s** -- `%s`' % (request.row_id, request.key))
        out.append('')
        out.append('- Site: `%s`' % request.where)
        out.append('- Code value: `%s`' % request.code_value)
        out.append('- Claim: %s' % request.claim)
        if request.cited:
            for body in request.cited:
                out.append('- **Cited source (this is what "Citation '
                           'correct?" answers):** %s' % body)
        else:
            out.append('- **Cited source:** none recorded. Answer '
                       '"Citation correct?" as NO and say so in Notes.')
        for body in request.context:
            out.append('- Also cited, context only, NOT verdicted: %s'
                       % body)
        for note in request.problems:
            out.append('- **Malformed continuation marker:** %s. The '
                       'text on that line is NOT part of the cited '
                       'source above, and was not joined to it.' % note)
        out.append('')

    out.append('## Response table')
    out.append('')
    out.append('| %s |' % ' | '.join(COLUMNS))
    out.append('|%s|' % '|'.join(['---'] * len(COLUMNS)))
    for request in requests:
        out.append('| %s | `%s` | %s | %s |  |  |  |  |  |'
                   % (request.row_id, request.key, request.claim,
                      request.code_value))
    out.append('')

    if skipped:
        out.append('## Not reached')
        out.append('')
        out.append('These files could not be read, so any claim in them '
                   'is absent from this request rather than cleared by '
                   'it.')
        out.append('')
        for name, reason in skipped:
            out.append('- `%s` -- %s' % (name, reason))
        out.append('')

    return '\n'.join(out)


def render_json(requests, batch, sha, repo_url, skipped, selection,
                corpus_size):
    """The request as JSON Lines -- one complete object per line.

    Line-delimited on purpose. A single JSON document fails whole-file:
    one trailing comma, one smart quote, one generation truncated at
    row 19 of 23, and nothing parses. With one object per line a
    truncated return is salvageable object by object, which is the only
    cheap hedge against the failure mode markdown does not have.
    (Tony's ruling 2026-08-17: send the JSON; if a return fails to
    parse, send the markdown. Markdown stays live permanently -- the
    seventeen historical worksheets are markdown.)

    Line 1 is the header. Every later line is one row. The `record`
    field says which.

    The answer fields are present and empty, so a responder fills them
    in place rather than inventing a shape.
    """
    lines = []
    header = {
        'record': 'header',
        'batch': batch,
        'built_on_sha': sha,
        'repo': repo_url,
        'extractor_version': wk.EXTRACTOR_VERSION,
        'key_format': 'module.py::enclosing::label::cN',
        'selection': selection.name,
        'selection_why': selection.why,
        'rows_selected': len(requests),
        'corpus_size': corpus_size,
        'row_hash': ('sha256 over key, claim and code value, first %d '
                     'hex characters. Do not edit those three fields; '
                     'the checker recomputes this and a row whose hash '
                     'is missing or wrong is returned rather than '
                     'read.' % HASH_CHARS),
        'identifies_rows': ('The KEY identifies a row. The id (R1, R2, '
                            '...) is assigned by position in this file '
                            'and means nothing outside it.'),
        'answer_fields': ['your_value', 'source', 'value_correct',
                          'citation_correct', 'notes'],
        'instructions': [
            'your_value -- the number the source states. If sources '
            'disagree, give the range AND the rule you used to reduce '
            'it (for example "2.5-2.7, took the midpoint to two '
            'significant figures").',
            'source -- the authority you consulted, specific enough to '
            'find again.',
            'value_correct -- about the NUMBER only.',
            'citation_correct -- about the code\'s cited source only, '
            'carried on each row as "cited". Answer it separately from '
            'the value: a right number under a wrong authority is a '
            'real finding and one token cannot say it.',
            'notes -- anything a token cannot carry. The checker reads '
            'notes as prose for a human, never as a verdict.',
            'One token per verdict field. A field holding a token plus '
            'a qualification is reported as unclassified rather than '
            'read, because guessing which half you meant is the '
            'interpretation this system is built to avoid.',
        ],
        'verdict_tokens': [
            {'means': own, 'words': words, 'answers': scope}
            for own, words, scope in verdict_vocabulary()
        ],
    }
    if skipped:
        header['not_reached'] = [
            {'file': name, 'reason': reason} for name, reason in skipped]
    lines.append(json.dumps(header, sort_keys=True))

    for request in requests:
        row = {
            'record': 'row',
            'id': request.row_id,
            'key': request.key,
            'claim': request.claim,
            'code_value': request.code_value,
            'hash': row_hash(request.key, request.claim,
                             request.code_value),
            'site': request.where,
            'cited': list(request.cited),
            'context_only': list(request.context),
            'your_value': '',
            'source': '',
            'value_correct': '',
            'citation_correct': '',
            'notes': '',
        }
        if not request.cited:
            row['cited_note'] = ('none recorded. Answer '
                                 'citation_correct as "no" and say so '
                                 'in notes.')
        if request.problems:
            row['malformed_continuation'] = list(request.problems)
        lines.append(json.dumps(row, sort_keys=True))

    return '\n'.join(lines) + '\n'

def choose_selection():
    """(selection, error) from the prompt.

    Numbered, because Tony runs this with VS Code's Run button and
    answers in the panel -- there are no command-line flags to pass.
    Blank means the whole corpus, so the behaviour before selection
    existed is still the default.
    """
    print('')
    print('Which rows?')
    for index, selection in enumerate(SELECTIONS, start=1):
        print('  %d. %s -- %s' % (index, selection.name, selection.why))
    answer = input('Selection [1]: ').strip()
    if not answer:
        return SELECTIONS[0], None
    try:
        number = int(answer)
    except ValueError:
        return None, ('"%s" is not one of the numbers above. Nothing '
                      'written.' % answer)
    if not 1 <= number <= len(SELECTIONS):
        return None, ('%d is outside 1-%d. Nothing written.'
                      % (number, len(SELECTIONS)))
    return SELECTIONS[number - 1], None


def main():
    project_dir = '.'
    if not os.path.isdir(os.path.join(project_dir, 'documentation')):
        print('Run this from the palomas_orrery repo root.')
        return 1

    requests, skipped = build(project_dir)

    print('%d rows over %d distinct keys.'
          % (len(requests), len({r.key for r in requests})))
    # Printed on every run, including zero. A join that fired on nothing
    # is otherwise indistinguishable from a corpus with nothing to join.
    print('%d continuation line(s) joined onto their leg.'
          % sum(r.joined for r in requests))
    flawed = [r for r in requests if r.problems]
    if flawed:
        print('%d row(s) carry a malformed continuation marker -- '
              'listed in the output.' % len(flawed))
    if skipped:
        print('%d file(s) not reached -- listed in the output.'
              % len(skipped))

    # The ratchet (L-195). An unmarked continuation is text that reaches
    # nobody: not joined onto its leg, not printed into the worksheet.
    # Refuse rather than issue a request that quotes half a citation.
    # Every one is listed, because a refusal naming one problem gets
    # fixed one round trip at a time.
    blocked = {}
    for request in requests:
        for line in request.unmarked:
            blocked.setdefault(request.where, [])
            if line not in blocked[request.where]:
                blocked[request.where].append(line)
    if blocked:
        count = sum(len(v) for v in blocked.values())
        print('')
        print('REFUSING TO WRITE. %d citation line(s) at %d site(s) '
              'continue a leg with no marker, so their text would be '
              'dropped from the request.' % (count, len(blocked)))
        for where in sorted(blocked):
            print('  %s' % where)
            for line in blocked[where]:
                print('      %s' % line)
        print('')
        print('Relabel each one with the leg it continues -- a line '
              'under `# Source:` becomes `# Source+:` -- then re-run.')
        return 1

    selection, error = choose_selection()
    if error:
        print(error)
        return 1

    selected, error = apply_selection(selection, requests, project_dir)
    if error:
        print('ERROR: %s' % error)
        print('Nothing written.')
        return 1

    # A selection matching nothing must refuse, not write an empty
    # request. An empty worksheet is indistinguishable from a finished
    # one once it is out of the room.
    if not selected:
        print('Selection "%s" matched 0 of %d rows. Nothing written.'
              % (selection.name, len(requests)))
        return 1

    print('Selection "%s": %d of %d rows.'
          % (selection.name, len(selected), len(requests)))

    # Numbered AFTER selection, because the id is positional within the
    # file being written. The key is what identifies a row anywhere
    # else, and the request says so.
    for index, request in enumerate(selected, start=1):
        request.row_id = 'R%d' % index

    batch = input('Batch name (e.g. batch3_gas_giants): ').strip()
    if not batch:
        print('No batch name. Nothing written.')
        return 1
    sha = input('Anchor SHA for this request: ').strip()
    if not sha:
        print('No anchor SHA. Nothing written -- a request without its '
              'anchor cannot be checked against the state it describes.')
        return 1
    repo_url = 'https://github.com/tonylquintanilla/palomas_orrery'

    # Both views, one producer. The JSON is what goes out; the markdown
    # is the fallback if a return will not parse, and it costs nothing
    # to write now rather than re-running later. Neither is derived
    # from the other -- both read the same Request list, so there is no
    # second source of truth to drift.
    text = render(selected, batch, sha, repo_url, skipped, selection,
                  len(requests))
    payload = render_json(selected, batch, sha, repo_url, skipped,
                          selection, len(requests))

    if not os.path.isdir(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    md_path = os.path.join(OUTPUT_DIR, 'REQUEST_%s.md' % batch)
    json_path = os.path.join(OUTPUT_DIR, 'REQUEST_%s.jsonl' % batch)
    for path in (md_path, json_path):
        if os.path.exists(path):
            print('%s already exists. Nothing written.' % path)
            return 1
    with open(md_path, 'wb') as handle:
        handle.write(text.encode('ascii', 'replace'))
    with open(json_path, 'wb') as handle:
        handle.write(payload.encode('ascii', 'replace'))

    print('Wrote %s (%d rows).' % (json_path, len(selected)))
    print('Wrote %s (%d rows) -- the fallback.' % (md_path, len(selected)))
    print('Send the .jsonl. If a return will not parse, send the .md '
          'and say so, so the pilot records which format was used.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
