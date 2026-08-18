"""patch_L207_1_citation_prompt.py -- L-207. The citation prompt.

RUN COMMAND
-----------
Save this file into the palomas_orrery repo root (the folder holding
worksheet_checker.py), open it in VS Code, and click Run. It takes no
arguments.

    python patch_L207_1_citation_prompt.py

Success: one `ok` line per file, then `patch applied`.
Failure: a single `ERROR:` or `ANCHOR FAIL:` line, and NOTHING is
written -- every edit is applied in memory and the files are rewritten
only after all of them have matched. A failed run is always safe to
re-run once its cause is fixed.

ONE-SHOT BY CONSTRUCTION. It guards on a content fingerprint of each
file as it stood at 731066f4, so a second run aborts and writes
nothing. Archive it to documentation/ once it has run.

WHAT IT DOES
------------
Two changes.

1. THE LEG PARSER MOVES (Tony's ruling, 2026-08-18: move it and get
   one parser). `legs_of` and its regexes move from
   worksheet_request_builder.py into worksheet_keys.py, the module the
   builder and the checker both already import. The builder keeps the
   old names as ALIASES, so worksheet_request_builder.legs_of IS the
   function in worksheet_keys rather than a copy of it. The move was
   forced by direction: the checker cannot import the builder, because
   the builder imports the checker.

2. THE CITATION PROMPT IS EMITTED (L-207). worksheet_checker.py gains
   an emitter that writes documentation/prompts/citation_review.jsonl
   on every run -- one row per key, carrying what the code cites, what
   each responder cited, what each responder concluded, and empty
   answer fields for a reviewer to fill.

WHAT IS PERMANENT AND WHAT IS NOT
---------------------------------
This script is disposable. What it installs is not:

  - worksheet_keys.legs_of and the leg regexes, now the single store
    of the leg grammar.
  - worksheet_checker.write_citation_prompt and the row builder under
    it, plus the documentation/prompts/ artifact.
  - New checks in both test suites, including the one-parser identity
    pin that goes red if the parser is ever forked again.

Written August 2026 with Anthropic's Claude Opus 5. Built on
731066f4be14fde0837fa33864505c371a4f5a33 at
https://github.com/tonylquintanilla/palomas_orrery
"""

import hashlib
import os
import sys


# Content fingerprints at 731066f4, taken after normalising line
# endings. A Windows working copy holding CRLF is content-identical to
# the repo's LF and must not be called BASE MOVED for it.
BASE = {
    'worksheet_keys.py':
        'a564355ca899ba20d7a21a298c5c93c1',
    'worksheet_request_builder.py':
        '7296cf0261532f1df693f7fee04b56c9',
    'worksheet_checker.py':
        'd143591c72ecba52e35910113a4a26d8',
    'test_worksheet_checker.py':
        'fd07292a7b0377e631b09eb89cf56017',
    'test_worksheet_request_builder.py':
        '80a663fdbf321bb831722ae4d56f04aa',
}

CREDIT = ("Module created: August 2026 with Anthropic's Claude Opus 5.\n")
CREDIT_NEW = (CREDIT + "Module updated: August 18, 2026 with Anthropic's "
              "Claude Opus 5 (L-207).\n")


# ============================================================
# 1. THE LEG PARSER, AS IT WILL LIVE IN worksheet_keys.py
# ============================================================

KEYS_DOC = '''THE SECOND JOB: CITATION LEGS (L-207)

A comment run above a value carries its citation on a `# Source:` leg
and its context on `# Ref:`, `# See:`, `# Derived:` and the rest, with
a wrapped line continuing on a leg-specific `+` marker. Parsing that
run lived in worksheet_request_builder.py for as long as the builder
was its only reader.

The citation prompt made worksheet_checker.py a second reader of the
same comment run, and the checker cannot import the builder -- the
builder imports the checker. So the parser moved here, to the module
both already share, rather than being copied into a second store free
to drift from the first. The builder keeps the old names as aliases:
worksheet_request_builder.legs_of IS this function, and
test_worksheet_request_builder.py pins that identity so a later fork
goes red rather than quietly giving two answers to one question.
(Tony's ruling, 2026-08-18: move it and get one parser.)

'''

KEYS_LEGS = '''

# ============================================================
# CITATION LEGS (moved from worksheet_request_builder.py, L-207)
# ============================================================

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
    r'^\\s*#\\s*(%s)(\\+)?:\\s*(.*)$'
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
COMMENT_RE = re.compile(r'^\\s*#')
PADDED_RE = re.compile(r'^\\s*#\\s{2,}\\S')
OTHER_LABEL_RE = re.compile(r'^\\s*#\\s*([A-Za-z][A-Za-z0-9_ /.-]{0,30})\\+?:')


def continues_a_leg(line):
    """True when this comment line is unlabelled continuation text."""
    if not COMMENT_RE.match(line) or line.strip() == '#':
        return False
    if PADDED_RE.match(line):
        return True
    return not OTHER_LABEL_RE.match(line)


def legs_of(attached_text):
    """(verdicted, context, problems, unmarked, joined) from a run.

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

'''


BUILDER_ALIASES = '''# THE LEG GRAMMAR LIVES IN worksheet_keys.py (L-207, 2026-08-18).
#
# It moved there when the citation prompt made worksheet_checker.py a
# second reader of the same comment run. The checker cannot import
# this module -- this module imports the checker -- so a shared parser
# had to live in the module both already import.
#
# These are ALIASES, not copies. `legs_of` here IS
# `worksheet_keys.legs_of`, and test_worksheet_request_builder.py pins
# that identity: an edit that restores a local copy goes red instead
# of quietly giving two answers to one question.
VERDICTED_LEG = wk.VERDICTED_LEG
CONTEXT_LEGS = wk.CONTEXT_LEGS
LEG_RE = wk.LEG_RE
COMMENT_RE = wk.COMMENT_RE
PADDED_RE = wk.PADDED_RE
OTHER_LABEL_RE = wk.OTHER_LABEL_RE
continues_a_leg = wk.continues_a_leg
legs_of = wk.legs_of
'''


# ============================================================
# 2. THE EMITTER, AS IT WILL LIVE IN worksheet_checker.py
# ============================================================

CHECKER_EMITTER = '''
# ============================================================
# THE CITATION PROMPT (L-207)
# ============================================================
#
# The numerical half of a return routes. The citation half -- the
# source a responder actually consulted, and their verdict on the
# source the CODE cites -- is parsed into the Table and stops there.
# That is not a defect in the split: whether a source SUPPORTS a claim
# is a language judgement, and the ruling of 2026-08-17 put it with a
# reader on purpose, leaving the mechanical checker at numbers. What
# was never built is the leg carrying the material to that reader.
#
# This is that leg. It is an EMITTER over the Table the run already
# built: no second parse, no new verdict class, no routing change. The
# precedent is the JSON adapter, which converted JSON into the same
# Table rather than standing up a second checker.
#
# A PROMPT RATHER THAN A WORKLIST, on purpose (Tony, 2026-08-18). A
# worklist is data; a request inherits the discipline the request
# builder already has -- keyed rows, a hash over the do-not-edit
# fields, a SHA anchor, generated rather than typed. Same HEAD plus
# the same returns must give the same bytes, which is what makes a
# citation review evidence rather than an opinion: re-runnable against
# another model, comparable across sessions, reproducible by anyone
# holding the repo.
#
# ONE ROW PER KEY, NOT PER ANNOTATION. Two checkers who both examined
# one site produce two legs and one row. The key names the row and the
# hash is taken over the key, so two rows sharing both would make the
# hash stop identifying anything. Grouping also puts the two sources
# side by side, where a disagreement between responders is visible
# without inventing a mechanism to look for one.
#
# THE RESPONDER'S VERDICT IS SHOWN (ruled 2026-08-18). It makes the
# review a comparison rather than a re-derivation, and disagreement
# between their verdict and the reviewer's is the lazy-responder
# canary, measured per row on real rows. The cost is anchoring, and it
# was traded away deliberately; the mitigations are weaker than
# structural blindness would be, so they are named rather than
# assumed: their verdict sits in its own field, after the evidence,
# and the prompt states that the review is independent and that
# disagreement is a FINDING rather than an error to reconcile.
#
# WHAT IT DOES NOT DO. It does not route, score, or promote. A
# returned citation review does not become a `# Cross-checked:` leg by
# itself: what lands in the code is an edit, and what records it is a
# `# Resolved:` leg, which this tool already checks for linkage.

CITATION_PROMPT_PATH = os.path.join('documentation', 'prompts',
                                    'citation_review.jsonl')
CITATION_PROMPT_REPO = 'https://github.com/tonylquintanilla/palomas_orrery'


def capture_citation_row(claim, table, cells, ordinal, claim_text,
                         code_value):
    """Keep the citation half of a row the match already found.

    Called at the point of the match, where the table and the row are
    both in hand. A later pass that went looking for the row again
    would be a second matcher, and two matchers disagreeing about
    which row belongs to a value is the failure this file exists to
    prevent.
    """
    claim.citation_rows.append({
        'ordinal': ordinal,
        'claim_text': ' '.join((claim_text or '').split()),
        'code_value': '' if code_value is None else str(code_value),
        'source': table.cell(cells, ROLE_SOURCE),
        'citation_verdict': table.cell(cells, ROLE_CITATION_VERDICT),
        'notes': table.cell(cells, ROLE_NOTES),
    })


def citation_vocabulary():
    """The verdict words that answer a CITATION question.

    Read from the registry rather than retyped. A prompt naming a word
    the vocabulary does not carry would send a reviewer to write
    something this project's own tools read as UNREADABLE.
    """
    groups = {}
    for token in sorted(VERDICT_TOKENS):
        own, scope = VERDICT_TOKENS[token]
        if scope not in (SCOPE_CITATION, SCOPE_EITHER):
            continue
        groups.setdefault(own, [])
        groups[own].append(token)
    return [{'means': own, 'words': groups[own]} for own in sorted(groups)]


def anchor_sha(project_dir):
    """HEAD as this run reads it, or a stated absence.

    An unknown anchor is written out rather than omitted. A prompt
    carrying no anchor line looks exactly like one whose anchor was
    unreadable, and the rule here is that a document leaving the
    session says what it was built on.
    """
    try:
        import provenance_history as ph
        sha = ph.head_sha(project_dir)
    except Exception:                                     # noqa: BLE001
        sha = None
    return sha or 'unknown -- not a git checkout, or HEAD unreadable'


def citation_prompt_rows(claims):
    """(rows, not_included) -- one row per key, legs grouped under it.

    `not_included` counts what was left out, by reason, and every
    count is reported whether or not it is zero. A row dropped in
    silence is the blind spot this file has a rule about.
    """
    rows = {}
    not_included = {
        'annotations_with_no_matched_row': 0,
        'matched_rows_with_no_citation_material': 0,
        'matched_rows_with_no_key': 0,
    }
    for claim in claims:
        if not claim.citation_rows:
            not_included['annotations_with_no_matched_row'] += 1
            continue
        cited, context, _problems, _unmarked, _joined = wk.legs_of(
            claim.unit.attached_text)
        for captured in claim.citation_rows:
            if not captured['source'] and not captured['citation_verdict']:
                not_included[
                    'matched_rows_with_no_citation_material'] += 1
                continue
            key = claim.key(captured['ordinal'])
            if not key:
                not_included['matched_rows_with_no_key'] += 1
                continue
            row = rows.get(key)
            if row is None:
                row = {
                    'record': 'row',
                    'key': key,
                    'claim': captured['claim_text'],
                    'code_value': captured['code_value'],
                    'site': claim.where,
                    # What the CODE cites, read from the code NOW --
                    # the authority a reviewer would edit, not the one
                    # a months-old worksheet happened to be shown.
                    'code_cited': list(cited),
                    # Not decoration. The context legs are what
                    # separate a citation that is WRONG from one that
                    # is merely MISPLACED.
                    'context_legs': list(context),
                    'responses': [],
                    'review_verdict': '',
                    'review_source': '',
                    'review_notes': '',
                }
                row['hash'] = row_hash(key, row['claim'],
                                       row['code_value'])
                rows[key] = row
            row['responses'].append({
                'checker': claim.checker,
                'worksheet': claim.worksheet,
                'numerical_route': claim.route or 'not routed',
                'their_source': captured['source'],
                'their_citation_verdict': captured['citation_verdict'],
                'their_notes': captured['notes'],
            })

    ordered = []
    for key in sorted(rows):
        row = rows[key]
        row['responses'].sort(
            key=lambda entry: (entry['checker'], entry['worksheet']))
        ordered.append(row)
    return ordered, not_included


def citation_prompt_payload(project_dir, claims):
    """(text, row count, not_included) -- the prompt as it is written.

    Deterministic by construction: rows sorted by key, responses
    sorted inside a row, keys sorted inside every object, and no
    timestamp anywhere. Same HEAD and same returns, same bytes -- so
    git reporting no change is itself the statement that the review is
    reproducible.
    """
    rows, not_included = citation_prompt_rows(claims)
    header = {
        'record': 'header',
        'artifact': 'citation_review_prompt',
        'written_by': 'worksheet_checker.py',
        'ledger_item': 'L-207',
        'built_on_sha': anchor_sha(project_dir),
        'repo': CITATION_PROMPT_REPO,
        'extractor_version': wk.EXTRACTOR_VERSION,
        'key_format': 'module.py::enclosing::label::cN',
        'rows': len(rows),
        'responder_legs': sum(len(row['responses']) for row in rows),
        'not_included': not_included,
        'question': ('For each row: does the source the CODE cites '
                     'support the claim the code makes? Whether the '
                     'NUMBER is right is checked elsewhere and is not '
                     'what this asks.'),
        'row_hash': ('sha256 over key, claim and code value, first %d '
                     'hex characters. Those three fields are not yours '
                     'to edit; a row whose hash does not match them is '
                     'returned rather than read.' % HASH_CHARS),
        'answer_fields': ['review_verdict', 'review_source',
                          'review_notes'],
        'instructions': [
            'review_verdict -- about the CODE\\'s cited source only, '
            'carried on each row as code_cited. Does that authority '
            'publish or support this claim? One token, from the list '
            'below.',
            'review_source -- what you consulted to answer that, '
            'specific enough to find again.',
            'review_notes -- anything a token cannot carry. Say in '
            'particular whether a citation that looks wrong is WRONG '
            'or merely MISPLACED: the context legs are shown for '
            'exactly that reason, and a value whose last digits come '
            'from a second authority named in a context leg is a '
            'citation to swap, not a number to change.',
            'The responses field carries what an earlier responder '
            'cited and what they concluded. Your review is '
            'INDEPENDENT: read the claim and the cited source first, '
            'and record disagreement with them as a FINDING rather '
            'than reconciling it away. Agreement nobody checked is '
            'the thing this is measuring.',
            'One token per verdict field. A field holding a token plus '
            'a qualification is reported as unclassified rather than '
            'read, because guessing which half you meant is the '
            'interpretation this system exists to avoid.',
        ],
        'verdict_tokens': citation_vocabulary(),
    }
    lines = [json.dumps(header, sort_keys=True)]
    for row in rows:
        lines.append(json.dumps(row, sort_keys=True))
    return '\\n'.join(lines) + '\\n', len(rows), not_included


def write_citation_prompt(project_dir, claims):
    """(rows_written, not_included, error). Written every run."""
    payload, count, not_included = citation_prompt_payload(
        project_dir, claims)
    path = os.path.join(project_dir, CITATION_PROMPT_PATH)
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'wb') as handle:
            handle.write(payload.encode('ascii', 'replace'))
    except (IOError, OSError) as exc:
        return 0, not_included, ('could not write %s: %s'
                                 % (CITATION_PROMPT_PATH, exc))
    return count, not_included, ''

'''


# ============================================================
# 3. THE TESTS
# ============================================================

CHECKER_TESTS = '''

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
'''


BUILDER_TESTS = '''

def test_one_parser():
    """The builder's leg names ARE the shared ones, not copies.

    The parser moved to worksheet_keys.py on 2026-08-18 so the checker
    could read the same comment run without importing this module.
    Aliases make the move invisible to every caller, which is the
    point -- and also the risk: a later edit could restore a local
    copy here and nothing else would notice. This is what notices.
    """
    check('one parser: legs_of is worksheet_keys.legs_of',
          b.legs_of is wk.legs_of,
          '%r vs %r' % (b.legs_of, wk.legs_of))
    check('one parser: the regexes and labels are shared too',
          b.LEG_RE is wk.LEG_RE and b.VERDICTED_LEG is wk.VERDICTED_LEG,
          '%r vs %r' % (b.LEG_RE, wk.LEG_RE))
'''


# ============================================================
# THE EDITS
# ============================================================
#
# (filename, [(anchor, replacement), ...]). Every anchor must match
# EXACTLY ONCE. Anchors were read from the file bytes at 731066f4, not
# recalled: a recalled anchor is how a patch aborted last session.

CHECKER_DOC_OLD = (
    "It does not write. There is no propose mode and no argument that "
    "adds\none (ruled 2026-08-13). Proposed annotations are discussed "
    "in\nconversation first. A tool that both judges evidence and "
    "writes\ncitations can satisfy itself, and the risk is not forgery "
    "-- it is a\nmatcher bug writing annotations against wrong rows and "
    "the same\nmatcher later confirming them.\n")

CHECKER_DOC_NEW = (
    "It does not write INTO THE CORPUS. There is no propose mode and "
    "no\nargument that adds one (ruled 2026-08-13). Proposed "
    "annotations are\ndiscussed in conversation first. A tool that both "
    "judges evidence and\nwrites citations can satisfy itself, and the "
    "risk is not forgery -- it\nis a matcher bug writing annotations "
    "against wrong rows and the same\nmatcher later confirming them.\n"
    "\nIt DOES write reports, and there are three: this file,\n"
    "data/worksheet_routed.json, and the citation prompt at\n"
    "documentation/prompts/citation_review.jsonl (L-207). A report is "
    "not\na corpus edit, and none of them proposes an annotation.\n")

EDITS = [
    ('worksheet_keys.py', [
        ("Module created: August 2026 with Anthropic's Claude Opus 5 "
         "(L-192).\n",
         KEYS_DOC
         + "Module created: August 2026 with Anthropic's Claude Opus 5 "
           "(L-192).\nModule updated: August 18, 2026 with Anthropic's "
           "Claude Opus 5 (L-207).\n"),
        ("import ast\nimport os\nfrom collections import namedtuple\n",
         "import ast\nimport os\nimport re\nfrom collections import "
         "namedtuple\n"),
        ("RETIRED_TAG = 'RETIRED'\n",
         "RETIRED_TAG = 'RETIRED'\n" + KEYS_LEGS),
    ]),

    ('worksheet_request_builder.py', [
        (CREDIT, CREDIT_NEW),
        # re is unused here once the regexes move. Removed in passing
        # rather than left as a dead import.
        ("import hashlib\nimport json\nimport os\nimport re\nimport sys\n",
         "import hashlib\nimport json\nimport os\nimport sys\n"),
    ]),

    ('worksheet_checker.py', [
        (CREDIT, CREDIT_NEW),
        (CHECKER_DOC_OLD, CHECKER_DOC_NEW),
        # Where the captured citation halves live.
        ("        self.routed_ordinals = []\n"
         "        self.current_ordinal = None\n",
         "        self.routed_ordinals = []\n"
         "        self.current_ordinal = None\n"
         "        # The citation half of every row this claim matched,\n"
         "        # kept for the citation prompt (L-207). Filled at the\n"
         "        # point of the match; empty means no row was found.\n"
         "        self.citation_rows = []\n"),
        # Capture on the constant path.
        ("    # Keyed to the MATCHED row and nothing else. No row, no "
         "quote -- a\n    # tool hunting for a nearby note when the "
         "match failed would have\n    # crossed from transcription "
         "into interpretation.\n"
         "    claim.notes = table.cell(cells, ROLE_NOTES)\n",
         "    # Keyed to the MATCHED row and nothing else. No row, no "
         "quote -- a\n    # tool hunting for a nearby note when the "
         "match failed would have\n    # crossed from transcription "
         "into interpretation.\n"
         "    claim.notes = table.cell(cells, ROLE_NOTES)\n"
         "    capture_citation_row(claim, table, cells, None,\n"
         "                         claim.label, claim.unit.value_str)\n"),
        # The raw spelling of each string claim, for the prompt.
        ("    values = claim.claim_values\n"
         "    claim.claims_present = len(values)\n",
         "    values = claim.claim_values\n"
         "    # The raw spelling of each claim, kept for the citation\n"
         "    # prompt so it states the value the way the code writes\n"
         "    # it, as a request row does.\n"
         "    raws = [raw for _value, raw in "
         "physical_claims(claim.unit)[0]]\n"
         "    claim.claims_present = len(values)\n"),
        # Capture on the string path.
        ("        claim.matched_line = line_no\n"
         "        claim.notes = table.cell(cells, ROLE_NOTES)\n"
         "        check_row_integrity(claim, table, line_no)\n",
         "        claim.matched_line = line_no\n"
         "        claim.notes = table.cell(cells, ROLE_NOTES)\n"
         "        capture_citation_row(\n"
         "            claim, table, cells, ordinal, text,\n"
         "            raws[ordinal - 1] if ordinal <= len(raws) else '')\n"
         "        check_row_integrity(claim, table, line_no)\n"),
        # The emitter, ahead of run().
        ("def run(project_dir, today):\n"
         '    """Returns (summary_line, report_path, counts)."""\n',
         CHECKER_EMITTER
         + "\ndef run(project_dir, today):\n"
           '    """Returns (summary_line, report_path, counts)."""\n'),
        # Called in the run, after the routing file.
        ("    routed_written, routing_error = write_routing_file"
         "(project_dir, claims)\n",
         "    routed_written, routing_error = write_routing_file"
         "(project_dir, claims)\n"
         "    prompt_rows, prompt_excluded, prompt_error = "
         "write_citation_prompt(\n        project_dir, claims)\n"),
        # Counted.
        ("        'resolved_problems': sum(1 for leg in resolved if "
         "leg.findings),\n    }\n",
         "        'resolved_problems': sum(1 for leg in resolved if "
         "leg.findings),\n"
         "        'citation_prompt_rows': prompt_rows,\n"
         "    }\n"),
        # Printed every run, including zero, like its neighbours.
        ("    if routing_error:\n"
         "        detail += '\\n  %s' % routing_error\n",
         "    # Printed every run, including zero, and the excluded\n"
         "    # counts ride with it: a prompt that quietly dropped half\n"
         "    # the corpus reads exactly like one with nothing to drop.\n"
         "    if prompt_error:\n"
         "        detail += '\\n  %s' % prompt_error\n"
         "    else:\n"
         "        detail += ('\\n  %d citation row(s) written to %s'\n"
         "                   % (prompt_rows, CITATION_PROMPT_PATH))\n"
         "    detail += ('\\n    not included: %d annotation(s) matched "
         "no row, '\n               '%d row(s) carried no citation "
         "material'\n               % (prompt_excluded"
         "['annotations_with_no_matched_row'],\n                  "
         "prompt_excluded"
         "['matched_rows_with_no_citation_material']))\n"
         "    if routing_error:\n"
         "        detail += '\\n  %s' % routing_error\n"),
    ]),

    ('test_worksheet_checker.py', [
        (CREDIT, CREDIT_NEW),
        ("def main():\n", CHECKER_TESTS + "\ndef main():\n"),
        ("    test_suffix_sets_agree()\n",
         "    test_suffix_sets_agree()\n"
         "    test_citation_prompt(project_dir)\n"),
    ]),

    ('test_worksheet_request_builder.py', [
        (CREDIT, CREDIT_NEW),
        ("import worksheet_checker as wc\n"
         "import worksheet_request_builder as b\n",
         "import worksheet_checker as wc\n"
         "import worksheet_keys as wk\n"
         "import worksheet_request_builder as b\n"),
        ("def main():\n", BUILDER_TESTS + "\ndef main():\n"),
        ("    test_json_lines(project_dir)\n",
         "    test_json_lines(project_dir)\n"
         "    test_one_parser()\n"),
    ]),
]


# The two regions of worksheet_request_builder.py that MOVE. Cutting
# by marker and verifying the cut against a digest is exact without
# transcribing 130 lines of anchor: the digest is of the region as it
# stood at 731066f4, so a region that has changed aborts the run
# rather than being replaced blind.
BUILDER_REGIONS = [
    ("# The leg the citation verdict answers",
     "    return not OTHER_LABEL_RE.match(line)\n",
     'b82a37cb6fe8056b529d632c330e81bf',
     BUILDER_ALIASES),
    ("def legs_of(attached_text):",
     "    return verdicted, context, problems, unmarked, joined\n\n\n",
     None,
     ''),
]


def fingerprint(data):
    return hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()


def fail(message):
    print('ERROR: %s' % message)
    print('Nothing was written.')
    return 1


def cut_regions(text):
    """Replace the moved regions, or return (None, why)."""
    for start_marker, end_marker, digest, replacement in BUILDER_REGIONS:
        start = text.find(start_marker)
        if start < 0:
            return None, 'marker not found: %r' % start_marker[:50]
        end = text.find(end_marker, start)
        if end < 0:
            return None, 'end marker not found: %r' % end_marker[:50]
        end += len(end_marker)
        region = text[start:end]
        if digest is not None:
            found = hashlib.md5(region.encode('ascii')).hexdigest()
            if found != digest:
                return None, ('the moved region has changed (expected '
                              '%s, found %s)' % (digest, found))
        text = text[:start] + replacement + text[end:]
    return text, ''


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    os.chdir(here)

    # ---- guard: every file is the one this was built against --------
    for name, expected in sorted(BASE.items()):
        if not os.path.isfile(name):
            return fail('%s not found. Save this script in the repo '
                        'root and run it there.' % name)
        with open(name, 'rb') as handle:
            data = handle.read()
        found = fingerprint(data)
        if found != expected:
            return fail('%s has moved since this patch was built '
                        '(expected %s, found %s). Re-cut the patch '
                        'rather than forcing it.'
                        % (name, expected, found))

    # ---- apply in memory, all or nothing ----------------------------
    staged = {}
    for name, edits in EDITS:
        with open(name, 'rb') as handle:
            data = handle.read()
        crlf = data.count(b'\r\n') > 0
        for anchor, replacement in edits:
            old = anchor.encode('ascii')
            new = replacement.encode('ascii')
            if crlf:
                old = old.replace(b'\n', b'\r\n')
                new = new.replace(b'\n', b'\r\n')
            count = data.count(old)
            if count != 1:
                print('ANCHOR FAIL: %s -- expected 1 match, found %d '
                      'for %r' % (name, count, anchor[:70]))
                print('Nothing was written.')
                return 1
            data = data.replace(old, new)
        staged[name] = (data, crlf)

    # ---- the two regions that move out of the builder ---------------
    data, crlf = staged['worksheet_request_builder.py']
    text = data.decode('ascii')
    if crlf:
        text = text.replace('\r\n', '\n')
    text, why = cut_regions(text)
    if text is None:
        return fail('worksheet_request_builder.py: %s' % why)
    if crlf:
        text = text.replace('\n', '\r\n')
    staged['worksheet_request_builder.py'] = (text.encode('ascii'), crlf)

    # ---- gates ------------------------------------------------------
    for name, (data, _crlf) in sorted(staged.items()):
        try:
            data.decode('ascii')
        except UnicodeDecodeError as exc:
            return fail('%s would hold non-ASCII bytes: %s' % (name, exc))
    moved = staged['worksheet_keys.py'][0].decode('ascii')
    if 'def legs_of(' not in moved:
        return fail('the parser did not land in worksheet_keys.py.')
    left = staged['worksheet_request_builder.py'][0].decode('ascii')
    if 'def legs_of(' in left or 'def continues_a_leg(' in left:
        return fail('a copy of the parser is still in the builder.')

    # ---- write ------------------------------------------------------
    for name, (data, _crlf) in sorted(staged.items()):
        with open(name, 'wb') as handle:
            handle.write(data)
        print('  ok  %s (%d bytes)' % (name, len(data)))

    print('patch applied')
    print('')
    print('Then run, in this order:')
    print('  python test_worksheet_keys.py')
    print('  python test_worksheet_request_builder.py')
    print('  python test_worksheet_checker.py')
    print('  python worksheet_checker.py')
    return 0


if __name__ == '__main__':
    sys.exit(main())
