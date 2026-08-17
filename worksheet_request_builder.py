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

Open in VS Code and press Run. It asks for a batch name and writes one
file into documentation/worksheets/. No command-line flags.
"""

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


def render(requests, batch, sha, repo_url, skipped):
    """The request file, as markdown the checker can read back."""
    out = []
    out.append('# Cross-check request -- %s' % batch)
    out.append('')
    out.append('**Built on `%s` at %s.**' % (sha, repo_url))
    out.append('')
    out.append('Extractor version: %d. Key format: '
               '`module.py::enclosing::label::cN`.' % wk.EXTRACTOR_VERSION)
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


def main():
    project_dir = '.'
    if not os.path.isdir(os.path.join(project_dir, 'documentation')):
        print('Run this from the palomas_orrery repo root.')
        return 1

    requests, skipped = build(project_dir)
    for index, request in enumerate(requests, start=1):
        request.row_id = 'R%d' % index

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

    text = render(requests, batch, sha, repo_url, skipped)
    if not os.path.isdir(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    path = os.path.join(OUTPUT_DIR, 'REQUEST_%s.md' % batch)
    if os.path.exists(path):
        print('%s already exists. Nothing written.' % path)
        return 1
    with open(path, 'wb') as handle:
        handle.write(text.encode('ascii', 'replace'))
    print('Wrote %s (%d rows).' % (path, len(requests)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
