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

LEG_RE = re.compile(
    r'^\s*#\s*(%s):\s*(.*)$' % '|'.join((VERDICTED_LEG,) + CONTEXT_LEGS))

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
    """(verdicted, context) citation legs from a comment run.

    Returns the `# Source:` lines and, separately, every other leg.
    Both are lists: a run carrying two Source lines is a malformation
    (L-195) and this reports both rather than picking one.
    """
    verdicted = []
    context = []
    for line in (attached_text or '').splitlines():
        match = LEG_RE.match(line)
        if not match:
            continue
        label, body = match.group(1), match.group(2).strip()
        if label == VERDICTED_LEG:
            verdicted.append(body)
        else:
            context.append('%s: %s' % (label, body))
    return verdicted, context


class Request(object):
    """One pre-printed row: a key, a claim, and the code's value."""

    def __init__(self, key, claim, code_value, where, cited, context):
        self.key = key
        self.claim = claim
        self.code_value = code_value
        self.where = where
        self.cited = cited          # list of `# Source:` bodies
        self.context = context      # list of other legs, read-only
        self.row_id = ''


def requests_for_claim(claim, source_text):
    """Every row one annotation should produce.

    A constant is one row. A display string is one row per numeric
    claim it makes, numbered from 1 in the order the scanner finds
    them -- the same order the checker's ordinal means.
    """
    cited, context = legs_of(claim.unit.attached_text)
    where = '%s:%d' % (os.path.basename(claim.path), claim.unit.line_start)

    if claim.unit.kind == 'constant':
        key = wk.key_for_site(claim.path, source_text,
                              claim.unit.line_start, claim.label, None)
        return [Request(key, claim.label,
                        claim.unit.value_str, where, cited, context)]

    rows = []
    values, _dropped = wc.physical_claims(claim.unit)
    text = claim.unit.raw_value or ''
    for index, (_value, raw) in enumerate(values, start=1):
        key = wk.key_for_site(claim.path, source_text,
                              claim.unit.line_start, claim.label, index)
        rows.append(Request(key, excerpt(text), raw, where, cited, context))
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
    if skipped:
        print('%d file(s) not reached -- listed in the output.'
              % len(skipped))

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
