"""patch_L196_8_builder_marker_join.py -- L-195 / L-192. Teach the
request builder to join continuation markers onto the leg they name.

RUN COMMAND
-----------
Save this file into the palomas_orrery repo root (the same folder as
worksheet_request_builder.py), open it in VS Code, and click Run.

    python patch_L196_8_builder_marker_join.py

Save test_worksheet_request_builder.py into the same folder first. This
patch adds a maintenance_run.py row that calls it, so without the file
present the next maintenance run reports a missing checker.

WHAT IT DOES
------------
Stage 1 relabeled 96 wrapped citation lines with a leg-specific marker:

    # Source: Nolan et al. 2013 (radar shape model),
    # Source+: mean diameter 492 +/- 20 m.

The builder has never heard of `Source+`, so it skips those lines
exactly as it skipped the padding they replaced, and the worksheet
still quotes half a citation. This patch is the builder half.

Four edits to worksheet_request_builder.py:

  1. LEG_RE accepts an optional `+` and returns it as its own group.
  2. legs_of joins a marked continuation onto the leg above it, and
     returns two new values -- a count of lines joined, and a list of
     malformed markers (a `# Ref+:` under a `# Source:` leg, or a
     marker with no leg above it at all). Malformed markers are
     reported, never joined onto the wrong authority.
  3. Request carries both, and the row context prints any malformation
     where the person filling in the worksheet will see it.
  4. main() prints the joined count on every run, including zero.

One edit to maintenance_run.py: a CHECKERS row for the new test file.

WHAT THIS PATCH IS NOT
----------------------
It does NOT make the builder fail on an UNMARKED continuation. That
ratchet needs stage 2 first -- 87 unmarked citation-leg continuation
runs remain in 19 files, and a loud failure turned on today would trip
on all of them. Order is Tony's ruling 3 of 2026-08-16: marker, then
join, then loud failure.

PERMANENT vs DISPOSABLE
-----------------------
This script is disposable and one-shot. What it installs is permanent:
the join behaviour in legs_of, the malformed-marker report, and the
maintenance row. test_worksheet_request_builder.py is a separate
permanent file, not written by this script.

SAFETY
------
All-or-nothing. Both files are fingerprinted (CRLF-normalized) before
anything is written, and every anchor must match exactly once. Any
mismatch aborts the whole run with nothing written. Each file's own
line endings are preserved.

Success: one 'ok' line per file, then 'patch applied (N bytes)'.
Failure: a single 'ERROR:' or 'ANCHOR FAIL' line; nothing is written.
"""

import hashlib
import os
import sys


OLD_LEG_RE = """LEG_RE = re.compile(
    r'^\\s*#\\s*(%s):\\s*(.*)$' % '|'.join((VERDICTED_LEG,) + CONTEXT_LEGS))
"""

NEW_LEG_RE = """# The optional `+` is the continuation marker stage 1 placed on wrapped
# citation lines (L-195). It is leg-specific on purpose: a `# Ref+:`
# sitting under a `# Source:` line is a mismatch that can be named,
# where a generic continuation marker would have nothing to compare
# against.
LEG_RE = re.compile(
    r'^\\s*#\\s*(%s)(\\+)?:\\s*(.*)$'
    % '|'.join((VERDICTED_LEG,) + CONTEXT_LEGS))
"""

OLD_LEGS_OF = '''def legs_of(attached_text):
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
'''

NEW_LEGS_OF = '''def legs_of(attached_text):
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

    An UNMARKED continuation is still dropped, silently, exactly as
    before. Making that loud is stage 2 work; see L-195.
    """
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
    return verdicted, context, problems, joined
'''

OLD_REQUEST = '''    def __init__(self, key, claim, code_value, where, cited, context):
        self.key = key
        self.claim = claim
        self.code_value = code_value
        self.where = where
        self.cited = cited          # list of `# Source:` bodies
        self.context = context      # list of other legs, read-only
        self.row_id = ''
'''

NEW_REQUEST = '''    def __init__(self, key, claim, code_value, where, cited, context,
                 problems=(), joined=0):
        self.key = key
        self.claim = claim
        self.code_value = code_value
        self.where = where
        self.cited = cited          # list of `# Source:` bodies
        self.context = context      # list of other legs, read-only
        self.problems = list(problems)  # markers that could not join
        self.joined = joined        # continuation lines joined on
        self.row_id = ''
'''

OLD_UNPACK = "    cited, context = legs_of(claim.unit.attached_text)\n"
NEW_UNPACK = ("    cited, context, problems, joined = legs_of("
              "claim.unit.attached_text)\n")

OLD_CONST_ROW = """        return [Request(key, claim.label,
                        claim.unit.value_str, where, cited, context)]
"""
NEW_CONST_ROW = """        return [Request(key, claim.label,
                        claim.unit.value_str, where, cited, context,
                        problems, joined)]
"""

OLD_STRING_ROW = ("        rows.append(Request(key, excerpt(text), raw, "
                  "where, cited, context))\n")
NEW_STRING_ROW = """        rows.append(Request(key, excerpt(text), raw, where,
                            cited, context, problems, joined))
"""

OLD_RENDER = """        for body in request.context:
            out.append('- Also cited, context only, NOT verdicted: %s'
                       % body)
        out.append('')
"""
NEW_RENDER = """        for body in request.context:
            out.append('- Also cited, context only, NOT verdicted: %s'
                       % body)
        for note in request.problems:
            out.append('- **Malformed continuation marker:** %s. The '
                       'text on that line is NOT part of the cited '
                       'source above, and was not joined to it.' % note)
        out.append('')
"""

OLD_MAIN = """    print('%d rows over %d distinct keys.'
          % (len(requests), len({r.key for r in requests})))
    if skipped:
        print('%d file(s) not reached -- listed in the output.'
              % len(skipped))
"""
NEW_MAIN = """    print('%d rows over %d distinct keys.'
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
"""

OLD_CHECKERS = ("    ('Worksheet key round trip', "
                "['test_worksheet_keys.py'], None),\n")
NEW_CHECKERS = ("    ('Worksheet key round trip', "
                "['test_worksheet_keys.py'], None),\n"
                "    ('Builder marker join', "
                "['test_worksheet_request_builder.py'], None),\n")

EDITS = {
    'worksheet_request_builder.py': {
        'fp': 'b8938e23495d929a2a1b9413007d8519',
        'edits': [
            (OLD_LEG_RE, NEW_LEG_RE),
            (OLD_LEGS_OF, NEW_LEGS_OF),
            (OLD_REQUEST, NEW_REQUEST),
            (OLD_UNPACK, NEW_UNPACK),
            (OLD_CONST_ROW, NEW_CONST_ROW),
            (OLD_STRING_ROW, NEW_STRING_ROW),
            (OLD_RENDER, NEW_RENDER),
            (OLD_MAIN, NEW_MAIN),
        ],
    },
    'maintenance_run.py': {
        'fp': '2200f53e6235f0fafd4ba602295a94fe',
        'edits': [
            (OLD_CHECKERS, NEW_CHECKERS),
        ],
    },
}

COMPANION = 'test_worksheet_request_builder.py'


def normalized(data):
    return data.replace(b'\r\n', b'\n')


def non_ascii_count(data):
    return sum(1 for byte in data if byte > 127)


def main():
    if not os.path.isfile('worksheet_request_builder.py'):
        print('ERROR: run this from the palomas_orrery repo root '
              '(the folder holding worksheet_request_builder.py).')
        return 1
    if not os.path.isfile(COMPANION):
        print('ERROR: %s is not in this folder. Save it here first -- '
              'this patch adds a maintenance row that calls it.'
              % COMPANION)
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
            # Scope the encoding gate to what this patch INTRODUCES.
            inserted = non_ascii_count(new.encode('utf-8'))
            if inserted:
                print('ERROR: %s -- an inserted block carries %d non-ASCII '
                      'byte(s). Nothing written.' % (name, inserted))
                return 1
            text = text.replace(old, new)

        out = text.encode('utf-8')
        pre_existing = non_ascii_count(out)
        if pre_existing:
            notes.append('note: %s still holds %d non-ASCII byte(s) this '
                         'patch did not reach' % (name, pre_existing))
        if crlf:
            out = out.replace(b'\n', b'\r\n')
        staged.append((name, out, len(spec['edits'])))
        total += len(out)

    for name, out, count in staged:
        with open(name, 'wb') as handle:
            handle.write(out)
        print('ok  %-34s %d edit(s)' % (name, count))

    for note in notes:
        print(note)
    print('patch applied (%d bytes)' % total)
    print('')
    print('Next: run test_worksheet_request_builder.py, then '
          'maintenance_run.py.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
