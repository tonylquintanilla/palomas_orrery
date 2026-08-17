"""patch_L196_15_loud_failure.py -- L-195 blocker 1, last piece. The
builder refuses to write a request when a citation wraps onto an
unmarked line.

RUN COMMAND
-----------
Save this file into the palomas_orrery repo root (the same folder as
worksheet_request_builder.py), open it in VS Code, and click Run.

    python patch_L196_15_loud_failure.py

WHAT IT DOES
------------
A citation too long for one line continues on a second line. Marked, it
joins. Unmarked, it was dropped in silence, and the worksheet asked a
person to verdict half a sentence. Stage 1 and stage 2 marked all 135
citation-leg continuations in the repo; this is the ratchet that keeps
the next one from arriving unmarked.

legs_of() now recognises an unmarked continuation and returns it. The
detection rule is the same one the two marking patches used, and it was
validated by reproducing stage 1's answer set exactly -- 48 runs, 96
lines, the same line numbers:

  - a comment line padded with two or more spaces after the '#' is a
    continuation, never a label. That is what keeps
    '#     Highly ellipsoidal: 1050x840x537 km' from being read as a
    label called 'Highly ellipsoidal';
  - otherwise a comment line that starts a new 'Word:' label closes
    the run;
  - otherwise a comment line is a continuation;
  - a bare '#' or any non-comment line closes the run.

build() collects them and main() refuses: it prints every site and
line and exits without writing, before asking for a batch name. All
of them are listed, not the first -- a refusal that names one problem
gets fixed one round trip at a time.

SCOPE: THE CLAIM CORPUS, NOT THE TREE
--------------------------------------
The check runs where the builder already reads -- annotated sites. A
file enters the corpus the moment someone adds a '# Cross-checked:'
line to it, and the refusal fires at the next build, which is still
before any worksheet is made from that file. So no truncated citation
reaches a worksheet either way, and scanning every .py file would buy
only earlier notice at the cost of a permanent exemption list, headed
by the MULTILINE_CITATION fixture in test_citation_inheritance.py that
stage 2 deliberately left unmarked. (Tony's ruling, 2026-08-17.)

WHAT STAYS NON-FATAL, AND WHY
------------------------------
A MISMATCHED marker -- '# Ref+:' sitting under a '# Source:' leg --
still reports rather than refuses. The distinction is whether the
failure is visible: a mismatch already prints a line into the
worksheet itself, where the person filling it in reads it, so the
dropped text is not silent. An unmarked continuation appears nowhere
at all. Silent gets the refusal; visible gets the annotation.

PERMANENT vs DISPOSABLE
-----------------------
This script is disposable and one-shot. What it installs is permanent:
the continuation rule in legs_of, the refusal in main, and the tests
that pin both.

SAFETY
------
All-or-nothing. Both files are fingerprinted (CRLF-normalized) and
every anchor must match exactly once before anything is written. Any
mismatch aborts with nothing written. Each file's own line endings are
preserved.

Success: one 'ok' line per file, then 'patch applied (N bytes)'.
Failure: a single 'ERROR:' or 'ANCHOR FAIL' line; nothing is written.
"""

import hashlib
import os
import sys


OLD_LEGRE_TAIL = """LEG_RE = re.compile(
    r'^\\s*#\\s*(%s)(\\+)?:\\s*(.*)$'
    % '|'.join((VERDICTED_LEG,) + CONTEXT_LEGS))
"""

NEW_LEGRE_TAIL = '''LEG_RE = re.compile(
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
'''

OLD_DOC = """    An UNMARKED continuation is still dropped, silently, exactly as
    before. Making that loud is stage 2 work; see L-195.
    \"\"\"
    verdicted = []
    context = []
    problems = []
    joined = 0
    open_label = None
    open_leg = None
    for line in (attached_text or '').splitlines():
        match = LEG_RE.match(line)
        if not match:
            # Any non-leg line closes the run a continuation could
            # attach to. Without this a marker separated from its leg by
            # unrelated prose would join across the gap.
            open_label = None
            open_leg = None
            continue
"""

NEW_DOC = """    `unmarked` holds continuation text carrying no marker at all. That
    text is invisible everywhere -- not joined, and not printed into the
    worksheet the way a mismatched marker is -- so the builder refuses
    to write a request while any exists, rather than reporting it. Each
    entry is the offending line, stripped.
    \"\"\"
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
"""

OLD_RETURN = "    return verdicted, context, problems, joined\n"
NEW_RETURN = "    return verdicted, context, problems, unmarked, joined\n"

OLD_SIG = """    def __init__(self, key, claim, code_value, where, cited, context,
                 problems=(), joined=0):"""
NEW_SIG = """    def __init__(self, key, claim, code_value, where, cited, context,
                 problems=(), unmarked=(), joined=0):"""

OLD_ATTRS = """        self.problems = list(problems)  # markers that could not join
        self.joined = joined        # continuation lines joined on
"""
NEW_ATTRS = """        self.problems = list(problems)  # markers that could not join
        self.unmarked = list(unmarked)  # continuation text with no marker
        self.joined = joined        # continuation lines joined on
"""

OLD_UNPACK = ("    cited, context, problems, joined = legs_of("
              "claim.unit.attached_text)\n")
NEW_UNPACK = ("    cited, context, problems, unmarked, joined = legs_of(\n"
              "        claim.unit.attached_text)\n")

OLD_CONST = """        return [Request(key, claim.label,
                        claim.unit.value_str, where, cited, context,
                        problems, joined)]
"""
NEW_CONST = """        return [Request(key, claim.label,
                        claim.unit.value_str, where, cited, context,
                        problems, unmarked, joined)]
"""

OLD_STRING = """        rows.append(Request(key, excerpt(text), raw, where,
                            cited, context, problems, joined))
"""
NEW_STRING = """        rows.append(Request(key, excerpt(text), raw, where,
                            cited, context, problems, unmarked, joined))
"""

OLD_MAIN = """    flawed = [r for r in requests if r.problems]
    if flawed:
        print('%d row(s) carry a malformed continuation marker -- '
              'listed in the output.' % len(flawed))
    if skipped:
        print('%d file(s) not reached -- listed in the output.'
              % len(skipped))
"""

NEW_MAIN = """    flawed = [r for r in requests if r.problems]
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
"""

OLD_TEST_DOC = '''def test_unmarked_does_not_join():
    """The pre-stage-1 shape. Padding is not a marker and must not join.

    This is the blocker the loud failure will later catch. Until stage 2
    marks the remaining 87 runs, the builder still drops these lines --
    pinned here so the limitation is a recorded fact rather than a
    surprise.
    """
    cited, _context, problems, joined = run(
        '# Source: Nolan et al. 2013 (radar shape model),',
        '#         mean diameter 492 +/- 20 m.')
    check('unmarked: padding does not join',
          cited == ['Nolan et al. 2013 (radar shape model),'], repr(cited))
    check('unmarked: nothing counted as joined', joined == 0, repr(joined))
    check('unmarked: silent, not reported as malformed',
          problems == [], repr(problems))
'''

NEW_TEST_DOC = '''def test_unmarked_is_caught():
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
'''

EDITS = {
    'worksheet_request_builder.py': {
        'fp': '69bee736cb638a0fe238f64417ea7e5a',
        'edits': [
            (OLD_LEGRE_TAIL, NEW_LEGRE_TAIL),
            (OLD_DOC, NEW_DOC),
            (OLD_RETURN, NEW_RETURN),
            (OLD_SIG, NEW_SIG),
            (OLD_ATTRS, NEW_ATTRS),
            (OLD_UNPACK, NEW_UNPACK),
            (OLD_CONST, NEW_CONST),
            (OLD_STRING, NEW_STRING),
            (OLD_MAIN, NEW_MAIN),
        ],
    },
    'test_worksheet_request_builder.py': {
        'fp': 'e07858afb8edf0c2c7e0c36ee80aa89f',
        'edits': [
            (OLD_TEST_DOC, NEW_TEST_DOC),
        ],
    },
}

# Every other unpack in the test file, rewritten for the 5-tuple.
TEST_TUPLE_EDITS = [
    ("    cited, _context, problems, joined = run(\n"
     "        '# Source: Nolan et al. 2013 (radar shape model),',\n"
     "        '# Source+: mean diameter 492 +/- 20 m.')\n",
     "    cited, _context, problems, _unmarked, joined = run(\n"
     "        '# Source: Nolan et al. 2013 (radar shape model),',\n"
     "        '# Source+: mean diameter 492 +/- 20 m.')\n"),
    ("    cited, _context, _problems, joined = run(\n"
     "        '# Source: one',\n",
     "    cited, _context, _problems, _unmarked, joined = run(\n"
     "        '# Source: one',\n"),
    ("    _cited, context, _problems, joined = run(\n"
     "        '# Ref: Archinal et al. 2011,',\n",
     "    _cited, context, _problems, _unmarked, joined = run(\n"
     "        '# Ref: Archinal et al. 2011,',\n"),
    ("    cited, context, problems, joined = run(\n"
     "        '# Source: Nolan et al. 2013,',\n"
     "        '# Ref+: mean diameter 492 +/- 20 m.')\n",
     "    cited, context, problems, _unmarked, joined = run(\n"
     "        '# Source: Nolan et al. 2013,',\n"
     "        '# Ref+: mean diameter 492 +/- 20 m.')\n"),
    ("    cited, context, problems, joined = run(\n"
     "        '# Source+: mean diameter 492 +/- 20 m.')\n",
     "    cited, context, problems, _unmarked, joined = run(\n"
     "        '# Source+: mean diameter 492 +/- 20 m.')\n"),
    ("    _cited, _context, problems, joined = run(\n"
     "        '# Source: Nolan et al. 2013,',\n"
     "        '# Note: unrelated prose about the shape model',\n"
     "        '# Source+: mean diameter 492 +/- 20 m.')\n",
     "    _cited, _context, problems, _unmarked, joined = run(\n"
     "        '# Source: Nolan et al. 2013,',\n"
     "        '# Note: unrelated prose about the shape model',\n"
     "        '# Source+: mean diameter 492 +/- 20 m.')\n"),
    ("    cited, _context, problems, joined = run(\n"
     "        '# Source: first authority',\n",
     "    cited, _context, problems, _unmarked, joined = run(\n"
     "        '# Source: first authority',\n"),
    ("    check('empty: no text', b.legs_of('') == ([], [], [], 0),\n"
     "          repr(b.legs_of('')))\n"
     "    check('empty: None', b.legs_of(None) == ([], [], [], 0),\n"
     "          repr(b.legs_of(None)))\n"
     "    cited, _context, problems, joined = run(\n",
     "    check('empty: no text', b.legs_of('') == ([], [], [], [], 0),\n"
     "          repr(b.legs_of('')))\n"
     "    check('empty: None', b.legs_of(None) == ([], [], [], [], 0),\n"
     "          repr(b.legs_of(None)))\n"
     "    cited, _context, problems, _unmarked, joined = run(\n"),
    ("    test_join()\n    test_unmarked_does_not_join()\n",
     "    test_join()\n    test_unmarked_is_caught()\n"
     "    test_what_is_not_a_continuation()\n"),
    ("    with_citation = [r for r in requests if r.cited]\n",
     "    stuck = [r for r in requests if r.unmarked]\n"
     "    check('corpus: no unmarked continuation anywhere', not stuck,\n"
     "          '; '.join('%s %s' % (r.where, r.unmarked[0])\n"
     "                    for r in stuck[:5]))\n\n"
     "    with_citation = [r for r in requests if r.cited]\n"),
]

EDITS['test_worksheet_request_builder.py']['edits'].extend(TEST_TUPLE_EDITS)


def normalized(data):
    return data.replace(b'\r\n', b'\n')


def non_ascii_count(text):
    return sum(1 for ch in text if ord(ch) > 127)


def main():
    if not os.path.isfile('worksheet_request_builder.py'):
        print('ERROR: run this from the palomas_orrery repo root '
              '(the folder holding worksheet_request_builder.py).')
        return 1

    staged = []
    total = 0
    notes = []

    for name in sorted(EDITS):
        spec = EDITS[name]
        if not os.path.isfile(name):
            print('ERROR: %s not found.' % name)
            return 1

        with open(name, 'rb') as handle:
            raw = handle.read()

        fp = hashlib.md5(normalized(raw)).hexdigest()
        if fp != spec['fp']:
            print('ERROR: %s does not match the base this patch was built '
                  'against.' % name)
            print('       expected %s' % spec['fp'])
            print('       found    %s' % fp)
            print('       Nothing written. If this patch has already run, '
                  'that is the expected abort -- it is one-shot.')
            return 1

        crlf = b'\r\n' in raw
        text = normalized(raw).decode('utf-8')

        for old, new in spec['edits']:
            count = text.count(old)
            if count != 1:
                print('ANCHOR FAIL: %s -- expected 1 match, found %d.'
                      % (name, count))
                print('       anchor starts: %r' % old[:70])
                print('       Nothing written.')
                return 1
            if non_ascii_count(new):
                print('ERROR: %s -- an inserted block carries non-ASCII. '
                      'Nothing written.' % name)
                return 1
            text = text.replace(old, new)

        out = text.encode('utf-8')
        pre_existing = non_ascii_count(text)
        if pre_existing:
            notes.append('note: %s still holds %d non-ASCII character(s) '
                         'this patch did not reach' % (name, pre_existing))
        if crlf:
            out = out.replace(b'\n', b'\r\n')
        staged.append((name, out, len(spec['edits'])))
        total += len(out)

    for name, out, count in staged:
        with open(name, 'wb') as handle:
            handle.write(out)
        print('ok  %-38s %d edit(s)' % (name, count))

    for note in notes:
        print(note)
    print('patch applied (%d bytes)' % total)
    print('')
    print('Next: run test_worksheet_request_builder.py, then '
          'maintenance_run.py.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
