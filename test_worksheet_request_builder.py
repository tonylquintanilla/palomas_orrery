"""test_worksheet_request_builder.py -- L-195 / L-192. Does the marker
join actually join, and can it fail?

RUN COMMAND
-----------
Open this file in VS Code and click Run. It takes no arguments.

    python test_worksheet_request_builder.py

It is also a CHECKERS row in maintenance_run.py, so a normal
maintenance run includes it.

WHY IT EXISTS
-------------
A citation too long for one line continues on a second line. Before
L-195 the builder matched labeled lines only, so that second line was
invisible and the worksheet quoted half a citation. Stage 1 relabeled
96 of those lines as leg-specific continuation markers (`# Source+:`
under `# Source:`), and this file tests the builder half that joins
them back on.

Every behaviour here is exercised twice -- once with input that should
join and once with input that must NOT join. A join that fires on
everything is indistinguishable from a join that fires correctly, and
both report zero problems. So the negative cases are the test.

The last check runs against the REAL corpus and pins two numbers: at
least one line is actually joined, and no annotation in the repo
carries a mismatched or orphaned marker. If a future edit places a
`# Ref+:` under a `# Source:` line, this goes red rather than the
worksheet quietly citing the wrong authority.

Role: devtool
Domain: dev_tools

Module created: August 2026 with Anthropic's Claude Opus 5.
"""

import json
import os
import sys

import worksheet_checker as wc
import worksheet_request_builder as b


PASSED = []
FAILED = []


def check(name, condition, detail=''):
    if condition:
        PASSED.append(name)
    else:
        FAILED.append((name, detail))


def run(*lines):
    """legs_of over a comment run written as separate lines."""
    return b.legs_of('\n'.join(lines))


def test_join():
    """A marked continuation joins onto the leg it names."""
    cited, _context, problems, _unmarked, joined = run(
        '# Source: Nolan et al. 2013 (radar shape model),',
        '# Source+: mean diameter 492 +/- 20 m.')
    check('join: two lines become one citation',
          cited == ['Nolan et al. 2013 (radar shape model), '
                    'mean diameter 492 +/- 20 m.'],
          repr(cited))
    check('join: reports one joined line', joined == 1, repr(joined))
    check('join: reports no problem', problems == [], repr(problems))

    cited, _context, _problems, _unmarked, joined = run(
        '# Source: one',
        '# Source+: two',
        '# Source+: three')
    check('join: a chain joins in order',
          cited == ['one two three'], repr(cited))
    check('join: chain counts both lines', joined == 2, repr(joined))

    _cited, context, _problems, _unmarked, joined = run(
        '# Ref: Archinal et al. 2011,',
        '# Ref+: IAU/LRO reference radius.')
    check('join: a context leg joins too',
          context == ['Ref: Archinal et al. 2011, '
                      'IAU/LRO reference radius.'], repr(context))
    check('join: context join is counted', joined == 1, repr(joined))


def test_unmarked_is_caught():
    """The pre-stage-1 shape. Padding does not join, and is REPORTED.

    Until L-195 this text was dropped in silence. It is now returned so
    the builder can refuse, which is the ratchet that keeps the next
    unmarked continuation from reaching a worksheet.
    """
    cited, _context, problems, unmarked, joined = run(
        '# Source: Nolan et al. 2013 (radar shape model),',
        '#         mean diameter 492 +/- 20 m.')
    check('unmarked: padding does not join',
          cited == ['Nolan et al. 2013 (radar shape model),'], repr(cited))
    check('unmarked: nothing counted as joined', joined == 0, repr(joined))
    check('unmarked: reported, not silent',
          unmarked == ['#         mean diameter 492 +/- 20 m.'],
          repr(unmarked))
    check('unmarked: not confused with a malformed marker',
          problems == [], repr(problems))

    # An unpadded comment line continuing a leg -- the other shape the
    # marking patches treated as continuation.
    _c, _x, _p, unmarked, _j = run(
        '# Derived: 63,241.077 AU per light-year',
        '# Previous hardcoded value was 8.3167')
    check('unmarked: an unpadded continuation is caught too',
          len(unmarked) == 1, repr(unmarked))


def test_what_is_not_a_continuation():
    """The negative half. Over-eager detection would refuse forever."""
    _c, _x, _p, unmarked, _j = run(
        '# Source: Nolan et al. 2013,',
        '# Note: an unrelated remark about the shape model')
    check('not-continuation: a new label closes the run',
          unmarked == [], repr(unmarked))

    _c, _x, _p, unmarked, _j = run(
        '# Source: Nolan et al. 2013,',
        '# Cross-checked: Claude 2026-08-03 -- Nolan (worksheet.md)')
    check('not-continuation: Cross-checked closes the run',
          unmarked == [], repr(unmarked))

    _c, _x, _p, unmarked, _j = run(
        '# Source: Nolan et al. 2013,',
        '#',
        '#         orphaned text after a blank comment')
    check('not-continuation: a bare # closes the run',
          unmarked == [], repr(unmarked))

    _c, _x, _p, unmarked, _j = run(
        '# Source: Nolan et al. 2013,',
        'BENNU_RADIUS_KM = 0.246')
    check('not-continuation: a code line closes the run',
          unmarked == [], repr(unmarked))

    # The case that broke the first detector: padded text whose own
    # words end in a colon. Padding wins, so this is continuation.
    _c, _x, _p, unmarked, _j = run(
        '# Source: JPL SSD mean radius (Lockwood et al. 2014)',
        '#         Highly ellipsoidal: 1050x840x537 km')
    check('not-continuation: padded text with a colon is still '
          'continuation', len(unmarked) == 1, repr(unmarked))


def test_label_mismatch():
    """A continuation naming a different leg is reported, never joined."""
    cited, context, problems, _unmarked, joined = run(
        '# Source: Nolan et al. 2013,',
        '# Ref+: mean diameter 492 +/- 20 m.')
    check('mismatch: reported', len(problems) == 1, repr(problems))
    check('mismatch: names both legs',
          problems and 'Ref' in problems[0] and 'Source' in problems[0],
          repr(problems))
    check('mismatch: text not joined onto the wrong leg',
          cited == ['Nolan et al. 2013,'], repr(cited))
    check('mismatch: text not smuggled into context',
          context == [], repr(context))
    check('mismatch: nothing counted as joined', joined == 0, repr(joined))


def test_orphan():
    """A continuation with no leg above it is reported, never joined."""
    cited, context, problems, _unmarked, joined = run(
        '# Source+: mean diameter 492 +/- 20 m.')
    check('orphan: reported', len(problems) == 1, repr(problems))
    check('orphan: nothing cited', cited == [], repr(cited))
    check('orphan: nothing in context', context == [], repr(context))
    check('orphan: nothing counted as joined', joined == 0, repr(joined))

    _cited, _context, problems, _unmarked, joined = run(
        '# Source: Nolan et al. 2013,',
        '# Note: unrelated prose about the shape model',
        '# Source+: mean diameter 492 +/- 20 m.')
    check('orphan: a non-leg line closes the run',
          len(problems) == 1, repr(problems))
    check('orphan: marker does not join across the gap',
          joined == 0, repr(joined))


def test_two_source_malformation():
    """Two Source legs is an existing malformation (L-195) and stays one.

    The join must not paper over it: both are still reported, and a
    continuation attaches to the leg immediately above it.
    """
    cited, _context, problems, _unmarked, joined = run(
        '# Source: first authority',
        '# Source: second authority',
        '# Source+: continued.')
    check('two-source: both legs still reported',
          len(cited) == 2, repr(cited))
    check('two-source: continuation joins the nearer leg',
          cited == ['first authority', 'second authority continued.'],
          repr(cited))
    check('two-source: join counted once', joined == 1, repr(joined))
    check('two-source: not treated as a marker problem',
          problems == [], repr(problems))


def test_empty_and_bare():
    """Degenerate input does not raise."""
    check('empty: no text', b.legs_of('') == ([], [], [], [], 0),
          repr(b.legs_of('')))
    check('empty: None', b.legs_of(None) == ([], [], [], [], 0),
          repr(b.legs_of(None)))
    cited, _context, problems, _unmarked, joined = run(
        '# Source: authority',
        '# Source+:')
    check('empty: a marker with no body joins nothing visible',
          cited == ['authority'], repr(cited))
    check('empty: still counted as a join', joined == 1, repr(joined))
    check('empty: not a problem', problems == [], repr(problems))


def test_live_corpus(project_dir):
    """The real annotated corpus, not synthetic input."""
    requests, _skipped = b.build(project_dir)
    joined = sum(request.joined for request in requests)
    flawed = [r for r in requests if r.problems]

    check('corpus: the join fires on real annotations', joined > 0,
          '%d lines joined' % joined)
    # Capped: a broken join reports a problem on nearly every row, and an
    # unreadable wall of text is how a red run gets skimmed past.
    shown = '; '.join('%s %s' % (r.where, r.problems[0]) for r in flawed[:5])
    if len(flawed) > 5:
        shown += ' ... and %d more row(s)' % (len(flawed) - 5)
    check('corpus: no mismatched or orphaned markers', not flawed,
          '%d row(s): %s' % (len(flawed), shown))

    stuck = [r for r in requests if r.unmarked]
    check('corpus: no unmarked continuation anywhere', not stuck,
          '; '.join('%s %s' % (r.where, r.unmarked[0])
                    for r in stuck[:5]))

    with_citation = [r for r in requests if r.cited]
    check('corpus: rows still carry citations',
          len(with_citation) == len(requests),
          '%d of %d rows cite nothing'
          % (len(requests) - len(with_citation), len(requests)))

    print('  corpus: %d rows, %d continuation line(s) joined'
          % (len(requests), joined))


def test_selection(project_dir):
    """A selection narrows the corpus and refuses to select nothing."""
    requests, _skipped = b.build(project_dir)

    every, error = b.apply_selection(b.SELECTIONS[0], requests, project_dir)
    check('selection: "all" returns the whole corpus',
          len(every) == len(requests) and error is None,
          '%d of %d, error %r' % (len(every), len(requests), error))

    pilot = [s for s in b.SELECTIONS if s.name == 'constants_new'][0]
    chosen, error = b.apply_selection(pilot, requests, project_dir)
    check('selection: the pilot slice is one file',
          chosen and error is None
          and set(r.where.split(':')[0] for r in chosen)
          == {'constants_new.py'},
          '%d rows from %s'
          % (len(chosen), sorted(set(r.where.split(':')[0]
                                     for r in chosen))))
    check('selection: the pilot slice is a strict subset',
          0 < len(chosen) < len(requests),
          '%d of %d' % (len(chosen), len(requests)))

    nothing = b.Selection('nothing', 'test', rule=lambda r: False)
    empty, error = b.apply_selection(nothing, requests, project_dir)
    check('selection: a rule matching nothing returns nothing',
          empty == [] and error is None, repr(error))

    # The refusal in main() turns that empty result into a stop. Pinned
    # here as a fact about the source, because an empty request is
    # indistinguishable from a finished one once it has left the room,
    # and the guard is four lines that a tidy-up could remove.
    source = open(os.path.join(project_dir,
                               'worksheet_request_builder.py'),
                  encoding='utf-8').read()
    check('selection: main refuses to write an empty request',
          'matched 0 of %d rows' in source
          or 'matched 0 of' in source,
          'the empty-selection guard is missing from main()')


def test_ratchet_is_not_bypassed_by_selection(project_dir):
    """The L-196 refusal reads the CORPUS, never the selection.

    This is the invariant, and it is not the order of statements in
    main(). Reordering so selection runs first changes nothing, because
    the refusal loop iterates every request the corpus produced. The
    mutation that DOES bypass it is a single word -- iterating the
    selected subset instead -- which lets a request go out over a
    corpus holding an unmarked continuation, as long as the offending
    file was not selected.

    Pinned against the source rather than by running main(), which
    prompts for input. A grep is a weak test in general; it is the
    right one here because the defect being pinned IS a one-word edit
    at a known line.
    """
    source = open(os.path.join(project_dir,
                               'worksheet_request_builder.py'),
                  encoding='utf-8').read()
    start = source.find('    blocked = {}')
    check('ratchet: the refusal block is still in main()', start != -1,
          'blocked = {} not found')
    if start == -1:
        return
    window = source[start:start + 400]
    check('ratchet: the refusal reads the whole corpus',
          'for request in requests:' in window,
          'the refusal iterates something other than `requests`: %r'
          % window[:120])
    check('ratchet: the refusal does not read the selection',
          'for request in selected:' not in window,
          'the refusal iterates the selected subset -- a selection can '
          'now exclude a site and excuse its unmarked continuation')


def test_row_hash():
    """The hash moves when a do-not-edit field moves, and not otherwise."""
    base = b.row_hash('constants_new.py::ROCHE_LIMIT_RADII',
                      'ROCHE_LIMIT_RADII', '3.45')
    check('hash: eight characters', len(base) == 8, base)
    check('hash: a rounded code value changes it',
          base != b.row_hash('constants_new.py::ROCHE_LIMIT_RADII',
                             'ROCHE_LIMIT_RADII', '3.450'), base)
    check('hash: a reflowed key changes it',
          base != b.row_hash('constants_new.py::ROCHE_LIMIT',
                             'ROCHE_LIMIT_RADII', '3.45'), base)
    check('hash: whitespace alone does not change it',
          base == b.row_hash(' constants_new.py::ROCHE_LIMIT_RADII ',
                             'ROCHE_LIMIT_RADII', '  3.45'), base)


def test_json_lines(project_dir):
    """Every line of the emitted request parses on its own."""
    requests, skipped = b.build(project_dir)
    pilot = [s for s in b.SELECTIONS if s.name == 'constants_new'][0]
    chosen, _error = b.apply_selection(pilot, requests, project_dir)
    for index, request in enumerate(chosen, start=1):
        request.row_id = 'R%d' % index
    payload = b.render_json(chosen, 'test_batch', 'deadbeef',
                            'https://example.invalid', skipped, pilot,
                            len(requests))

    lines = payload.strip().split('\n')
    parsed = []
    bad = ''
    for line in lines:
        try:
            parsed.append(json.loads(line))
        except ValueError as exc:
            bad = '%s: %s' % (exc, line[:60])
            break
    check('json: every line parses independently', not bad, bad)
    if bad:
        return

    check('json: one header plus one line per row',
          len(parsed) == len(chosen) + 1,
          '%d lines for %d rows' % (len(parsed), len(chosen)))
    check('json: the first record is the header',
          parsed[0].get('record') == 'header', repr(parsed[0])[:80])
    check('json: the header states the selection and the counts',
          parsed[0].get('selection') == 'constants_new'
          and parsed[0].get('rows_selected') == len(chosen)
          and parsed[0].get('corpus_size') == len(requests),
          repr(parsed[0].get('selection')))

    rows = parsed[1:]
    check('json: every row carries a hash',
          all(len(r.get('hash', '')) == 8 for r in rows),
          repr([r.get('id') for r in rows if len(r.get('hash', '')) != 8]))
    check('json: the hash matches the row it sits on',
          all(r.get('hash') == b.row_hash(r.get('key', ''),
                                          r.get('claim', ''),
                                          r.get('code_value', ''))
              for r in rows),
          'a row hash is missing or does not match its own fields')
    check('json: answer fields are present and empty',
          all(r.get(field) == '' for r in rows
              for field in ('your_value', 'source', 'value_correct',
                            'citation_correct', 'notes')),
          'an answer field is missing or pre-filled')

    # The vocabulary is read from the checker, so a token the checker
    # accepts and the request does not name would be a drift the pilot
    # would discover the hard way.
    named = set()
    for group in parsed[0].get('verdict_tokens', []):
        named.update(group.get('words', []))
    check('json: the request names every token the checker accepts',
          named == set(wc.VERDICT_TOKENS),
          'request %r vs checker %r'
          % (sorted(named), sorted(wc.VERDICT_TOKENS)))


def main():
    project_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_dir)

    print('=' * 70)
    print('BUILDER TESTS -- joins, selection, hash, JSON '
          '(L-195 / L-201 / L-202)')
    print('=' * 70)

    test_join()
    test_unmarked_is_caught()
    test_what_is_not_a_continuation()
    test_label_mismatch()
    test_orphan()
    test_two_source_malformation()
    test_empty_and_bare()
    test_live_corpus(project_dir)
    test_selection(project_dir)
    test_ratchet_is_not_bypassed_by_selection(project_dir)
    test_row_hash()
    test_json_lines(project_dir)

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
