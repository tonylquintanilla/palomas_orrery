"""L-214 patch 1 of 2 -- the label registry, generic detection, corpus.

Built on e1c64dc955ba3323312d9b23ed53547985fe32cb at
https://github.com/tonylquintanilla/palomas_orrery (branch main).

WHAT THIS DOES

One all-or-nothing transaction over nine files. Nothing is written
until every edit on every file has been prepared and checked, so a
failure anywhere leaves the tree exactly as it was.

  worksheet_keys.py             the label registry; generic `# Label:`
                                detection ahead of classification;
                                `Note` admitted as travelling context;
                                `# Review-note:` added as a withheld
                                free-form record label; legs_of returns
                                a named 6-field result whose sixth
                                field is the unrecognised labels it
                                withheld; the legs_of docstring
                                one-word fix; the missing `Role:` tag
                                (Fix In Passing).
  worksheet_request_builder.py  reads the named result; prints the
                                unrecognised-label report on every run,
                                beside the existing refusal print.
  worksheet_checker.py          reads the named result at its one call
                                site.
  test_worksheet_request_builder.py
                                pins moved to the 6-field result, plus
                                four new pins covering the travelling,
                                withheld, unrecognised and ratchet
                                paths.
  constants_new.py              14 `# Note+:` continuation markers; the
                                invented `# HELIOCENTRIC:` fixed at
                                source; 7 dated `# Corrected` spellings
                                unified (date moves into the body).
  mercury_visualization_shells.py   2 continuation markers.
  venus_visualization_shells.py     1 continuation marker; `# NOTE:`
                                fixed at source.
  moon_visualization_shells.py  the single-leg comment rehomed from
                                `# Note:` to `# Review-note:`.
  mars_visualization_shells.py  1 dated `# Corrected` unified.

WHY THE CORPUS AND THE VOCABULARY MOVE TOGETHER

Admitting `Note` makes the builder see its wrapped lines. Wrapped
lines with no marker are what the L-195 ratchet refuses on. Mark them
first and the markers are dropped in silence, because the vocabulary
does not yet admit the label; admit first and the ratchet refuses on
lines the sweep has not reached. Neither order works alone, so it is
one transaction.

THE MARKING OBLIGATION IS 17 LINES AT 9 SITES

Measured at this SHA with the project's own collect_claims and
PADDED_RE. It is not the 28 the 2026-08-21 handoff carried: that count
included wrapped lines under WITHHELD labels, and the settled design
says a withheld label's continuations are withheld with it and never
flagged unmarked. (Tony's ruling, 2026-08-21.)

HOW TO RUN IT

Open this file in VS Code and press Run, from the repo root. It takes
no arguments and asks no questions. It prints every file it changed,
every stamp it updated, and a count of the edits per file. On any
failure it prints the reason and writes nothing at all.

Written August 21, 2026 with Anthropic's Claude Opus 5 (L-214).
"""

import hashlib
import os
import re
import sys

STAMP_OLD = ("Module updated: August 18, 2026 with Anthropic's "
             "Claude Opus 5 (L-207).")
STAMP_NEW = STAMP_OLD + ("\nModule updated: August 21, 2026 with "
                         "Anthropic's Claude Opus 5 (L-214).")


FINGERPRINTS = {
    'worksheet_keys.py': 'c48bdd0770f237c2158ebe75316c3547',
    'worksheet_request_builder.py': 'bbe6df4b84fbd89816af92e477f7c5dd',
    'worksheet_checker.py': 'a26c434d0563e1cf62da2c1bd4c5dc53',
    'test_worksheet_request_builder.py': 'a97eb2b819422b2692b9c7c086a62896',
    'constants_new.py': '2f19a32f98e0a7bc1fb4a60d78c58821',
    'mercury_visualization_shells.py': 'b1c67f31f2fa18c32cb6376f9f372ad2',
    'venus_visualization_shells.py': 'c0e3cb5c9123ecc309e992206bbcb4f0',
    'moon_visualization_shells.py': '56b85b3d50366ed6a6764e2d50945f78',
    'mars_visualization_shells.py': '8f3fde17c2f83efbde87b10d0fdacdcf',
}

CORPUS_EDITS = {
    'constants_new.py': [
        (467,
         '# Corrected 2026-08-02: 9.95 -> 9.1 per Keane shape model (prior dims were wrong)',
         '# Corrected: 2026-08-02 -- 9.95 -> 9.1 per Keane shape model (prior dims were wrong)'),
        (454,
         '# Corrected 2026-08-20: 715 -> 798 per the 2017 occultation',
         '# Corrected: 2026-08-20 -- 715 -> 798 per the 2017 occultation'),
        (453,
         '# Corrected 2026-08-02: 816 -> 715 per JPL SSD (prior value matched neither axes nor database)',
         '# Corrected: 2026-08-02 -- 816 -> 715 per JPL SSD (prior value matched neither axes nor database)'),
        (445,
         '#   the only direct measurement. 798 is chosen for that reason.',
         '# Note+: the only direct measurement. 798 is chosen for that reason.'),
        (444,
         '#   715 km directly and is what JPL SSD adopted; the 2017 occultation is',
         '# Note+: 715 km directly and is what JPL SSD adopted; the 2017 occultation is'),
        (443,
         '#   in radius. Lockwood et al. 2014, Earth Moon Planets 111:127 publishes',
         '# Note+: in radius. Lockwood et al. 2014, Earth Moon Planets 111:127 publishes'),
        (423,
         '# Corrected 2026-08-20: 0.246 -> 0.24503 (OSIRIS-REx supersedes radar)',
         '# Corrected: 2026-08-20 -- 0.246 -> 0.24503 (OSIRIS-REx supersedes radar)'),
        (422,
         '# Corrected 2026-08-02: 0.262 -> 0.246 (prior value matched no published source)',
         '# Corrected: 2026-08-02 -- 0.262 -> 0.246 (prior value matched no published source)'),
        (421,
         '#   independently derived, not a restatement of the radar result.',
         '# Note+: independently derived, not a restatement of the radar result.'),
        (420,
         '#   km), which this row previously carried. The mission figure is',
         '# Note+: km), which this row previously carried. The mission figure is'),
        (419,
         '#   2013, Icarus 226:629 (mean diameter 492 +/- 20 m, implying ~0.246',
         '# Note+: 2013, Icarus 226:629 (mean diameter 492 +/- 20 m, implying ~0.246'),
        (332,
         '#   the surface = 8.86 R_sun altitude. Same orbit, different reference.',
         '# Note+: the surface = 8.86 R_sun altitude. Same orbit, different reference.'),
        (331,
         '# HELIOCENTRIC: 9.86 from Sun center. NASA press reports ~3.83 Mkm above',
         '# Note: 9.86 from Sun center. NASA press reports ~3.83 Mkm above'),
        (310,
         '# Corrected 2026-08-02: 126000 -> 150000 (prior value unsourced;',
         '# Corrected: 2026-08-02 -- 126000 -> 150000 (prior value unsourced;'),
        (287,
         '# Corrected 2026-08-02: 26449 -> 26148 (prior comment used 123 AU;',
         '# Corrected: 2026-08-02 -- 26449 -> 26148 (prior comment used 123 AU;'),
        (244,
         '# inside it. Ikeya-Seki survived at 1.66 R_sun.',
         '# Note+: inside it. Ikeya-Seki survived at 1.66 R_sun.'),
        (186,
         '#       is what the shell draws at. The 1.1 stylization is retired.',
         '# Note+: is what the shell draws at. The 1.1 stylization is retired.'),
        (185,
         '#       CHROMOSPHERE_PHYSICAL_RADII below converts it to solar radii and',
         '# Note+: CHROMOSPHERE_PHYSICAL_RADII below converts it to solar radii and'),
        (80,
         '#   differ by 36.6 m.',
         '# Note+: differ by 36.6 m.'),
        (79,
         '#   exact nominal conversion constant, not a measurement, and the two',
         '# Note+: exact nominal conversion constant, not a measurement, and the two'),
        (71,
         '# (Haberreiter et al. 2008). Use nominal for all calculations.',
         '# Note+: (Haberreiter et al. 2008). Use nominal for all calculations.'),
        (70,
         '# measurement. The measured photospheric radius is ~696,340 km',
         '# Note+: measurement. The measured photospheric radius is ~696,340 km'),
    ],
    'mars_visualization_shells.py': [
        (841,
         '# Corrected 2026-08-05: the former ~324.5 R_Mars matched no published source',
         '# Corrected: 2026-08-05 -- the former ~324.5 R_Mars matched no published source'),
    ],
    'mercury_visualization_shells.py': [
        (93,
         '#       source and has been replaced with the observed range.',
         '# Note+: source and has been replaced with the observed range.'),
        (92,
         '#       establish tail extent. The former "10,000 R_M" was unsupported by either',
         '# Note+: establish tail extent. The former "10,000 R_M" was unsupported by either'),
    ],
    'moon_visualization_shells.py': [
        (582,
         '# Note: SINGLE-LEG. Only the Claude tier-2 worksheet carries the 58,147-64,901 km',
         '# Review-note: SINGLE-LEG. Only the Claude tier-2 worksheet carries the 58,147-64,901 km'),
    ],
    'venus_visualization_shells.py': [
        (337,
         '#       below carries a <br> copy of this block. Edit both copies together.',
         '# Note+: below carries a <br> copy of this block. Edit both copies together.'),
        (336,
         '# NOTE: duplicated text -- the description entry in create_venus_atmosphere_shell',
         '# Note: duplicated text -- the description entry in create_venus_atmosphere_shell'),
    ],
}

VOCAB_OLD = "# The leg the citation verdict answers, and the legs that are shown\n# but never verdicted. Break 5, 2026-08-15.\nVERDICTED_LEG = 'Source'\nCONTEXT_LEGS = ('Ref', 'Also', 'See', 'Derived', 'Calculation')"

VOCAB_NEW = "# THE LABEL REGISTRY (L-214)\n#\n# Two axes, not one list. TRANSPORT says whether a label's text is\n# shown to an outside responder or kept at home. GRAMMAR -- whether a\n# body is validated, and against what -- is not here: it stays in\n# provenance_scanner.py, with the scanner's line patterns derived from\n# these names. Moving the names without the grammar is deliberate; a\n# keys module that owned the semantics would be a second place for the\n# meaning of a leg to drift.\n#\n# Before this registry existed, a label outside the set was not\n# recognised as a LABEL at all, so deliberate withholding and silent\n# dropping shared one code path and could not be told apart from\n# inside it. That is L-209, and it is why the registry names the\n# withheld labels explicitly rather than leaving them to fall through.\n\n# The leg the citation verdict answers, and the legs that are shown\n# but never verdicted. Break 5, 2026-08-15. `Note` joined them in\n# L-214: it was already the corpus's most-used context label and was\n# being dropped in silence on every dispatch.\nVERDICTED_LEG = 'Source'\nCONTEXT_LEGS = ('Ref', 'Also', 'See', 'Derived', 'Calculation', 'Note')\n\n# Labels whose text is deliberately NOT shown to a responder. A second\n# reader must not see what the last one concluded, or the leg stops\n# being independent. `Review-note` is the free-form one -- withheld,\n# with no body grammar -- and it exists because a record that is not a\n# cross-check and not a resolution had nowhere to live.\nRECORD_LEGS = ('Cross-checked', 'Resolved', 'Removed', 'Corrected',\n               'Review-note')\n\nTRAVELS = 'travels'\nWITHHELD = 'withheld'\n\nLABEL_TRANSPORT = {}\nfor _name in (VERDICTED_LEG,) + CONTEXT_LEGS:\n    LABEL_TRANSPORT[_name] = TRAVELS\nfor _name in RECORD_LEGS:\n    LABEL_TRANSPORT[_name] = WITHHELD\ndel _name"

ANY_OLD = "OTHER_LABEL_RE = re.compile(r'^\\s*#\\s*([A-Za-z][A-Za-z0-9_ /.-]{0,30})\\+?:')"

ANY_NEW = "OTHER_LABEL_RE = re.compile(r'^\\s*#\\s*([A-Za-z][A-Za-z0-9_ /.-]{0,30})\\+?:')\n\n# Generic detection, ahead of classification. This matches the SHAPE of\n# a labelled line and says nothing about whether the label is known.\n# The invariant it buys: every syntactically labelled line attached to\n# a claim finishes legs_of() in one named disposition. There is no\n# disposition called `fell through the regex`.\nANY_LABEL_RE = re.compile(\n    r'^\\s*#\\s*([A-Za-z][A-Za-z0-9_ /.-]{0,30})(\\+)?:\\s*(.*)$')\n\n# Kept for the travelling set, and still what a caller asking `is this\n# a citation leg` should use. It is no longer what legs_of() dispatches\n# on -- that is ANY_LABEL_RE -- because building the detector from the\n# vocabulary is the defect L-214 removed.\nLegs = namedtuple(\n    'Legs', 'cited context problems unmarked joined unknown')"

DOC1_OLD = '    """(verdicted, context, problems, unmarked, joined) from a run.'

DOC1_NEW = '    """Legs(cited, context, problems, unmarked, joined, unknown).'

DOC2_OLD = '    above it at all. Their text is reported and NOT joined, because'

DOC2_NEW = '    above it at all. Their label is reported and their text is NOT\n    joined, because'

DOC3_OLD = '    to write a request while any exists, rather than reporting it. Each\n    entry is the offending line, stripped.\n    """'

DOC3_NEW = '    to write a request while any exists, rather than reporting it. Each\n    entry is the offending line, stripped. Only a TRAVELLING leg can\n    carry one: text under a withheld label is withheld with it, and\n    nothing is being dropped from a request it was never entering.\n\n    `unknown` holds the names of labels the registry does not carry.\n    Their text is withheld -- never shipped to a responder on the\n    strength of a label nobody has classified -- and the name is\n    returned so the builder can print it. Report, not reject: a\n    reported label is one this project can then read and decide about,\n    where a rejected one stops the run and the decision never gets\n    made. (Tony\'s ruling, 2026-08-19.)\n    """'

INIT_OLD = '    verdicted = []\n    context = []\n    problems = []\n    unmarked = []\n    joined = 0\n    open_label = None\n    open_leg = None'

INIT_NEW = '    verdicted = []\n    context = []\n    problems = []\n    unmarked = []\n    unknown = []\n    joined = 0\n    open_label = None\n    open_leg = None\n    open_travels = False'

LOOP_OLD = "    for line in (attached_text or '').splitlines():\n        match = LEG_RE.match(line)\n        if not match:\n            # A line that continues the leg above it but carries no\n            # marker is the failure this refuses on. Anything else\n            # closes the run, so a marker separated from its leg by\n            # unrelated prose cannot join across the gap.\n            if open_label is not None and continues_a_leg(line):\n                unmarked.append(line.strip())\n                continue\n            open_label = None\n            open_leg = None\n            continue\n        label = match.group(1)\n        marker = match.group(2)\n        body = match.group(3).strip()\n        if marker:\n            if open_label is None:\n                problems.append(\n                    '`%s+:` continuation with no leg above it to join'\n                    % label)\n            elif label != open_label:\n                problems.append(\n                    '`%s+:` continuation under a `%s:` leg'\n                    % (label, open_label))\n            else:\n                open_leg[-1] = (open_leg[-1] + ' ' + body).strip()\n                joined += 1\n            continue\n        if label == VERDICTED_LEG:\n            verdicted.append(body)\n            open_leg = verdicted\n        else:\n            context.append('%s: %s' % (label, body))\n            open_leg = context\n        open_label = label\n    return verdicted, context, problems, unmarked, joined"

LOOP_NEW = "    for line in (attached_text or '').splitlines():\n        # PADDING IS CHECKED FIRST, and the order is load-bearing.\n        # `#   Highly ellipsoidal: 1050x840x537 km` is continuation\n        # text, not a label called `Highly ellipsoidal`. Before L-214\n        # the label test could not see it because the label had to be\n        # in the vocabulary; now that ANY_LABEL_RE matches any\n        # `# Word:` shape, the padding test is what keeps that line a\n        # continuation.\n        match = None if PADDED_RE.match(line) else ANY_LABEL_RE.match(line)\n        if not match:\n            # A line that continues a TRAVELLING leg but carries no\n            # marker is the failure this refuses on. Under a withheld\n            # leg the same line is withheld with it and is not a\n            # defect -- nothing is being dropped from a request the\n            # text was never going into. Anything else closes the run,\n            # so a marker separated from its leg by unrelated prose\n            # cannot join across the gap.\n            if open_label is not None and continues_a_leg(line):\n                if open_travels:\n                    unmarked.append(line.strip())\n                continue\n            open_label = None\n            open_leg = None\n            open_travels = False\n            continue\n        label = match.group(1).strip()\n        marker = match.group(2)\n        body = match.group(3).strip()\n        transport = LABEL_TRANSPORT.get(label)\n        if transport is None:\n            # The disposition L-214 exists to create. An unrecognised\n            # label is WITHHELD, never silently dropped, and its name\n            # is reported so a reader can decide what it should be.\n            if label not in unknown:\n                unknown.append(label)\n            transport = WITHHELD\n        if transport == WITHHELD:\n            open_label = label\n            open_leg = None\n            open_travels = False\n            continue\n        if marker:\n            if open_label is None:\n                problems.append(\n                    '`%s+:` continuation with no leg above it to join'\n                    % label)\n            elif not open_travels:\n                problems.append(\n                    '`%s+:` continuation under a withheld `%s:` leg'\n                    % (label, open_label))\n            elif label != open_label:\n                problems.append(\n                    '`%s+:` continuation under a `%s:` leg'\n                    % (label, open_label))\n            else:\n                open_leg[-1] = (open_leg[-1] + ' ' + body).strip()\n                joined += 1\n            continue\n        if label == VERDICTED_LEG:\n            verdicted.append(body)\n            open_leg = verdicted\n        else:\n            context.append('%s: %s' % (label, body))\n            open_leg = context\n        open_label = label\n        open_travels = True\n    return Legs(verdicted, context, problems, unmarked, joined, unknown)"

ROLE_OLD = 'Worksheet row keys -- one owner for the syntax and the resolution.\n\nDomain: dev_tools'

ROLE_NEW = 'Worksheet row keys -- one owner for the syntax and the resolution.\n\nRole: devtool\nDomain: dev_tools'

BUILDER_CALL_OLD = '    cited, context, problems, unmarked, joined = legs_of(\n        claim.unit.attached_text)'

BUILDER_CALL_NEW = '    legs = legs_of(claim.unit.attached_text)\n    cited, context = legs.cited, legs.context\n    problems, unmarked, joined = legs.problems, legs.unmarked, legs.joined\n    unknown = legs.unknown'

BUILDER_ROW1_OLD = '        return [Request(key, claim.label,\n                        claim.unit.value_str, where, cited, context,\n                        problems, unmarked, joined)]'

BUILDER_ROW1_NEW = '        return [Request(key, claim.label,\n                        claim.unit.value_str, where, cited, context,\n                        problems, unmarked, joined, unknown)]'

BUILDER_ROW2_OLD = '        rows.append(Request(key, excerpt(text), raw, where,\n                            cited, context, problems, unmarked, joined))'

BUILDER_ROW2_NEW = '        rows.append(Request(key, excerpt(text), raw, where,\n                            cited, context, problems, unmarked, joined,\n                            unknown))'

BUILDER_INIT_OLD = '    def __init__(self, key, claim, code_value, where, cited, context,\n                 problems=(), unmarked=(), joined=0):'

BUILDER_INIT_NEW = '    def __init__(self, key, claim, code_value, where, cited, context,\n                 problems=(), unmarked=(), joined=0, unknown=()):'

BUILDER_FIELD_OLD = '        self.joined = joined        # continuation lines joined on'

BUILDER_FIELD_NEW = '        self.joined = joined        # continuation lines joined on\n        self.unknown = list(unknown)    # labels the registry does not carry'

BUILDER_REPORT_OLD = '    # The ratchet (L-195). An unmarked continuation is text that reaches'

BUILDER_REPORT_NEW = "    # The L-214 report. A label the registry does not carry is withheld\n    # from the request rather than dropped in silence, and its name is\n    # printed here so it can be read and decided about -- aliased,\n    # unified onto an existing label, or registered. Printed on every\n    # run including zero, because a report that only appears when it\n    # has something to say is indistinguishable from one that never\n    # ran. It prints BEFORE the ratchet so a refusing run still shows\n    # it.\n    unknown_at = {}\n    for request in requests:\n        for label in request.unknown:\n            unknown_at.setdefault(request.where, [])\n            if label not in unknown_at[request.where]:\n                unknown_at[request.where].append(label)\n    print('%d unrecognised label(s) at %d site(s), withheld from the '\n          'request.' % (sum(len(v) for v in unknown_at.values()),\n                        len(unknown_at)))\n    for where in sorted(unknown_at):\n        print('  %s' % where)\n        for label in unknown_at[where]:\n            print('      # %s:' % label)\n\n    # The ratchet (L-195). An unmarked continuation is text that reaches"

CHECKER_OLD = '        cited, context, _problems, _unmarked, _joined = wk.legs_of(\n            claim.unit.attached_text)'

CHECKER_NEW = '        _legs = wk.legs_of(claim.unit.attached_text)\n        cited, context = _legs.cited, _legs.context'

TEST_PINS_OLD = "    check('empty: no text', b.legs_of('') == ([], [], [], [], 0),\n          repr(b.legs_of('')))\n    check('empty: None', b.legs_of(None) == ([], [], [], [], 0),\n          repr(b.legs_of(None)))"

TEST_PINS_NEW = "    check('empty: no text', b.legs_of('') == ([], [], [], [], 0, []),\n          repr(b.legs_of('')))\n    check('empty: None', b.legs_of(None) == ([], [], [], [], 0, []),\n          repr(b.legs_of(None)))"

TEST_NEW_CASES = '\n\ndef test_note_travels():\n    """`Note` is context and travels (L-214)."""\n    _cited, context, _problems, unmarked, _joined, unknown = run(\n        \'# Note: a drawing choice, not a measurement,\',\n        \'# Note+: chosen to keep the shell visible.\')\n    check(\'note: travels as context\',\n          context == [\'Note: a drawing choice, not a measurement, \'\n                      \'chosen to keep the shell visible.\'], repr(context))\n    check(\'note: nothing unmarked\', unmarked == [], repr(unmarked))\n    check(\'note: nothing unknown\', unknown == [], repr(unknown))\n\n\ndef test_withheld_label_holds_its_continuation():\n    """A withheld leg keeps its wrapped text and raises no ratchet."""\n    cited, context, problems, unmarked, _joined, unknown = run(\n        \'# Review-note: SINGLE-LEG. A second leg is still owed\',\n        \'#     for V2 scoring.\')\n    check(\'withheld: not shown as context\', context == [], repr(context))\n    check(\'withheld: not shown as citation\', cited == [], repr(cited))\n    check(\'withheld: continuation is not unmarked\',\n          unmarked == [], repr(unmarked))\n    check(\'withheld: not a marker problem\', problems == [], repr(problems))\n    check(\'withheld: a known label is not unknown\',\n          unknown == [], repr(unknown))\n\n\ndef test_unknown_label_is_withheld_and_named():\n    """The disposition L-214 exists to create."""\n    cited, context, _problems, unmarked, _joined, unknown = run(\n        \'# HELIOCENTRIC: 9.86 from Sun center\',\n        \'#     which is what the shell draws at.\')\n    check(\'unknown: named once\', unknown == [\'HELIOCENTRIC\'], repr(unknown))\n    check(\'unknown: text does not travel as context\',\n          context == [], repr(context))\n    check(\'unknown: text does not travel as citation\',\n          cited == [], repr(cited))\n    check(\'unknown: continuation withheld, not unmarked\',\n          unmarked == [], repr(unmarked))\n\n\ndef test_unmarked_still_refuses_under_a_travelling_leg():\n    """The ratchet is unchanged where it applies."""\n    _cited, _context, _problems, unmarked, _joined, _unknown = run(\n        \'# Source: an authority\',\n        \'#     continued with no marker at all.\')\n    check(\'ratchet: still catches an unmarked continuation\',\n          unmarked == [\'#     continued with no marker at all.\'],\n          repr(unmarked))'


# ============================================================
# MACHINERY
# ============================================================

CHANGED = []


def die(reason):
    print('')
    print('STOPPED. %s' % reason)
    print('Nothing was written.')
    sys.exit(1)


def read(path):
    if not os.path.exists(path):
        die('%s not found. Run this from the repo root.' % path)
    with open(path, 'rb') as handle:
        raw = handle.read()
    if b'\r\n' in raw:
        die('%s has CRLF line endings; this patch expects LF.' % path)
    return raw.decode('utf-8')


def ascii_only(text, where):
    for char in text:
        if ord(char) > 127:
            die('non-ASCII character %r would be inserted into %s. '
                'Inserted text must be ASCII.' % (char, where))


def swap(text, old, new, where):
    """Replace exactly one occurrence, or stop."""
    found = text.count(old)
    if found != 1:
        die('anchor in %s matched %d times, expected exactly 1.' % (where, found))
    ascii_only(new, where)
    return text.replace(old, new, 1)


def stamp(text, path):
    if STAMP_OLD not in text:
        die('%s carries no L-207 currency line to stamp.' % path)
    return swap(text, STAMP_OLD, STAMP_NEW, '%s (stamp)' % path)


def apply_corpus(text, path):
    """Line-targeted edits, applied bottom-up so numbers cannot drift."""
    lines = text.split('\n')
    for number, old, new in CORPUS_EDITS[path]:
        actual = lines[number - 1]
        if actual != old:
            die('%s:%d does not read as expected.\n'
                '  expected: %s\n  found:    %s' % (path, number, old, actual))
        ascii_only(new, '%s:%d' % (path, number))
        lines[number - 1] = new
    return '\n'.join(lines)


# ============================================================
# THE TRANSACTION
# ============================================================

def main():
    if not os.path.isdir('documentation'):
        die('no documentation/ directory here. Run this from the '
            'palomas_orrery repo root.')

    # ---- 1. Read every file and check its fingerprint.
    source = {}
    for path, expected in sorted(FINGERPRINTS.items()):
        text = read(path)
        actual = hashlib.md5(text.encode('utf-8')).hexdigest()
        if actual != expected:
            die('%s does not match the file this patch was written '
                'against.\n  expected md5 %s\n  found        %s\n'
                'Re-pull the repo at e1c64dc9, or ask for a patch '
                'rebuilt on the current bytes.' % (path, expected, actual))
        source[path] = text
    print('%d file(s) fingerprint-matched at e1c64dc9.' % len(source))

    out = dict(source)

    # ---- 2. worksheet_keys.py -- the registry and the parser.
    path = 'worksheet_keys.py'
    text = out[path]
    text = swap(text, ROLE_OLD, ROLE_NEW, '%s (Role tag)' % path)
    text = swap(text, VOCAB_OLD, VOCAB_NEW, '%s (registry)' % path)
    text = swap(text, ANY_OLD, ANY_NEW, '%s (generic detector)' % path)
    text = swap(text, DOC1_OLD, DOC1_NEW, '%s (legs_of summary)' % path)
    text = swap(text, DOC2_OLD, DOC2_NEW, '%s (legs_of one-word fix)' % path)
    text = swap(text, DOC3_OLD, DOC3_NEW, '%s (legs_of new fields)' % path)
    text = swap(text, INIT_OLD, INIT_NEW, '%s (legs_of init)' % path)
    text = swap(text, LOOP_OLD, LOOP_NEW, '%s (legs_of loop)' % path)
    text = text.replace(
        "Module updated: August 18, 2026 with Anthropic's Claude Opus 5 (L-207).",
        "Module updated: August 18, 2026 with Anthropic's Claude Opus 5 (L-207).\n"
        "Module updated: August 21, 2026 with Anthropic's Claude Opus 5 (L-214).",
        1)
    out[path] = text
    CHANGED.append((path, 8))

    # ---- 3. worksheet_request_builder.py -- one reader, one report.
    path = 'worksheet_request_builder.py'
    text = out[path]
    text = swap(text, BUILDER_INIT_OLD, BUILDER_INIT_NEW, '%s (Request init)' % path)
    text = swap(text, BUILDER_FIELD_OLD, BUILDER_FIELD_NEW, '%s (Request field)' % path)
    text = swap(text, BUILDER_CALL_OLD, BUILDER_CALL_NEW, '%s (legs_of call)' % path)
    text = swap(text, BUILDER_ROW1_OLD, BUILDER_ROW1_NEW, '%s (constant row)' % path)
    text = swap(text, BUILDER_ROW2_OLD, BUILDER_ROW2_NEW, '%s (string rows)' % path)
    text = swap(text, BUILDER_REPORT_OLD, BUILDER_REPORT_NEW, '%s (report)' % path)
    text = stamp(text, path)
    out[path] = text
    CHANGED.append((path, 7))

    # ---- 4. worksheet_checker.py -- the one call site.
    path = 'worksheet_checker.py'
    text = out[path]
    text = swap(text, CHECKER_OLD, CHECKER_NEW, '%s (legs_of call)' % path)
    text = stamp(text, path)
    out[path] = text
    CHANGED.append((path, 2))

    # ---- 5. the test file -- moved pins, new pins, and their runner.
    #
    # The unpack rewrite is done by PATTERN, not by a list of literal
    # spellings. The first version of this patch listed six spellings,
    # counted nine matches, passed its own count check, and left six
    # sites unconverted -- a check that could not fail. The 15 below is
    # the whole population at e1c64dc9.
    path = 'test_worksheet_request_builder.py'
    text = out[path]
    unpack_re = re.compile(
        r'^(\s+)([_A-Za-z][_A-Za-z0-9]*(?:, [_A-Za-z][_A-Za-z0-9]*){4})'
        r' = (run|b\.legs_of)\(', re.M)
    matches = unpack_re.findall(text)
    if len(matches) != 15:
        die('expected 15 five-field unpacks in %s, found %d.'
            % (path, len(matches)))
    text = unpack_re.sub(
        lambda m: '%s%s, _unknown = %s(' % (m.group(1), m.group(2), m.group(3)),
        text)
    text = swap(text, TEST_PINS_OLD, TEST_PINS_NEW,
                '%s (empty-input pins)' % path)

    # The new cases go in above the runner, and the runner is told to
    # call them. A test function nothing calls is the same shape of
    # nothing as the count check above.
    ascii_only(TEST_NEW_CASES, path)
    text = swap(text, "\nif __name__ == '__main__':",
                TEST_NEW_CASES + "\n\n\nif __name__ == '__main__':",
                '%s (new cases)' % path)
    text = swap(text, '    test_empty_and_bare()',
                '    test_empty_and_bare()\n'
                '    test_note_travels()\n'
                '    test_withheld_label_holds_its_continuation()\n'
                '    test_unknown_label_is_withheld_and_named()\n'
                '    test_unmarked_still_refuses_under_a_travelling_leg()',
                '%s (runner)' % path)
    out[path] = text
    CHANGED.append((path, len(matches) + 7))

    # ---- 6. the corpus, bottom-up within each file.
    for path in sorted(CORPUS_EDITS):
        out[path] = apply_corpus(out[path], path)
        CHANGED.append((path, len(CORPUS_EDITS[path])))

    # ---- 7. Nothing has touched the disk yet. Write, all or nothing.
    for path in sorted(out):
        if out[path] == source[path]:
            die('%s came out identical to its input, which means an '
                'edit silently did nothing.' % path)
    for path in sorted(out):
        with open(path, 'wb') as handle:
            handle.write(out[path].encode('utf-8'))

    print('')
    for path, edits in sorted(CHANGED):
        print('  %-36s %2d edit(s)' % (path, edits))
    print('')
    print('Currency stamps updated: worksheet_keys.py, '
          'worksheet_request_builder.py, worksheet_checker.py.')
    print('')
    print('Corpus: 17 continuation markers, 2 odd labels fixed at '
          'source, 1 line rehomed to # Review-note:, 8 dated '
          '# Corrected spellings unified.')
    print('')
    print('NEXT: run test_worksheet_request_builder.py, then '
          'worksheet_request_builder.py and read the new '
          'unrecognised-label report. It should say 0.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
