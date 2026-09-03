"""Worksheet row keys -- one owner for the syntax and the resolution.

Role: devtool
Domain: dev_tools

A cross-check worksheet row has to name the thing it checked, and the
checker has to find that thing again later. Until now the finding was
done by four heuristics in sequence (constant name, prose containment,
code-value equality, and a fuzzy fallback), which works for constants
and fails for prose: 24 of the 25 UNMATCHED findings in the current
run are display-string claims that no row records.

This module mints the key and resolves it. Both tools import it --
worksheet_request_builder.py to put keys into requests, and
worksheet_checker.py to resolve keys coming back. That is deliberate.
If the builder computed the enclosing name one way and the checker
computed it another, a key could be born stale: minted correctly,
unresolvable forever, and nothing would say so. One function, two
importers, and a round-trip test that mints and resolves every
annotated site at the same commit.

WHAT A KEY LOOKS LIKE

    pluto_visualization_shells.py::create_pluto_core_shell::description::c1
    pluto_visualization_shells.py::pluto_core_info::c1
    constants_new.py::CHROMOSPHERE_PHYSICAL_KM

Module file, enclosing name, label, claim ordinal. The label is
dropped when it repeats the enclosing name (a module-level string is
introduced by its own assignment). The ordinal is dropped for
constants, which assert exactly one value.

TWO EXCLUSIONS, BOTH DELIBERATE

No line number. Edits shift them and a worksheet is a fixed record of
what was known on its date; a key that moves with the file would need
the worksheet edited to keep up, and editing a worksheet to match
today's code is the same failure as citing over recalled data.

No code value. A key holding the value would break under exactly the
drift the checker exists to detect -- the pointer would move with the
thing it is supposed to outlive.

WHY THE ENCLOSING NAME

pluto_visualization_shells.py carries five separate `description`
fields. Each sits inside its own create_*_shell() function, so the
function name separates them. Measured over the 53 distinct annotated
sites the current report names: 53 distinct keys, zero collisions.

The enclosing name is resolved by parsing the module, not by matching
text. A regex over line prefixes gets the same answer for this corpus
-- both a regex pass and an independent AST pass agreed at 53 of 53 --
but the parse is the one that stays right when a def is nested or a
decorator sits between the def and its body.

THE ORDINAL PROBLEM, AND WHAT ANSWERS IT

`::c2` means "the second numeric claim in this string". Insert a
number ahead of it and c2 silently re-points to a different claim.
Left alone that surfaces as DRIFTED -- the value at the new position
disagrees with the worksheet -- which is the wrong diagnosis and sends
the wrong errand.

So a key travels with two facts recorded at issue time: how many
claims the string carried, and the unit token sitting against the
claim the ordinal points at. Before any value is compared, both are
re-checked. Either mismatch is KEY_SHIFTED and no value comparison
runs for that row. The two ordinary edit shapes that re-point an
ordinal both disturb one of them: inserting or deleting a number
changes the count, and swapping one kind of quantity for another
changes the unit. Copy-editing that touches neither leaves the ordinal
meaning what it meant.

The residual, stated rather than hidden: a compensating swap -- delete
one quantity and insert a different one of the same unit elsewhere in
the same paragraph -- leaves count and unit intact and re-points the
ordinal silently. It surfaces as DRIFTED. The wrong label still sends
a useful errand, because the value at the new position genuinely has
no verified row.

ON THE EXTRACTOR VERSION

Which numbers count as claims is decided by the scanner's claim regex
and the checker's instruction filter, not by the prose. Extend the
instruction pattern by one phrase and a formerly-dropped number joins
the sequence, shifting every ordinal after it with no prose edit at
all. The version is therefore recorded alongside the count and the
unit -- but it does not gate resolution on its own. If the count and
the unit still match, the ordinal still points at the same claim, and
failing the row would fail a key that is fine. A version difference
annotates the row; a count or unit mismatch is what fires.

THE SECOND JOB: CITATION LEGS (L-207)

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

Module created: August 2026 with Anthropic's Claude Opus 5 (L-192).
Module updated: August 18, 2026 with Anthropic's Claude Opus 5 (L-207).
Module updated: August 21, 2026 with Anthropic's Claude Opus 5 (L-214).
Module updated: September 3, 2026 with Anthropic's Claude Fable 5.1 (L-277: the site store anchors by enclosing name; parse_sites_doc refuses the line format; locate_site added; the two label regexes move here from worksheet_checker).
"""

import ast
import os
import re
from collections import namedtuple

try:
    from worksheet_key_aliases import ALIASES as INSTALLED_ALIASES
except ImportError:                                        # noqa: BLE001
    # A missing alias store is not a quiet zero. Callers that pass
    # nothing get an empty map AND the reason, so a resolve failure
    # cannot be blamed on an alias that was never loaded.
    INSTALLED_ALIASES = {}
    ALIAS_STORE_MISSING = True
else:
    ALIAS_STORE_MISSING = False

KEY_SEP = '::'
ORDINAL_PREFIX = 'c'

# Bumped when the set of numbers treated as claims changes -- the
# scanner's claim regex or the checker's instruction filter. Recorded
# with every key; see ON THE EXTRACTOR VERSION above for why it is
# recorded and not enforced.
EXTRACTOR_VERSION = 2

Key = namedtuple('Key', 'module enclosing label ordinal')

# The line that INTRODUCES a unit: a dict key or an assignment name.
# One home since L-277: worksheet_checker.anchor_label labels a unit
# with these, and locate_site below finds a site by the same two, so
# a site found by name is the site the checker would label.
ASSIGN_NAME_RE = re.compile(r"^\s*([A-Za-z_][A-Za-z_0-9]*)\s*[:=]")
DICT_KEY_RE = re.compile(r"^\s*['\"]([^'\"]+)['\"]\s*:")

# What a shift check can say. NONE is the only one that permits a
# value comparison downstream.
SHIFT_OK = None
SHIFT_COUNT = 'KEY_SHIFTED: claim count %s at issue, %s now'
SHIFT_UNIT = 'KEY_SHIFTED: unit %r at issue, %r now'


class KeyError_(ValueError):
    """A key that cannot be parsed. Never raised for one that parses
    and then fails to resolve -- that is a finding, not an error."""


RETIRED_TAG = 'RETIRED'


# ============================================================
# CITATION LEGS (moved from worksheet_request_builder.py, L-207)
# ============================================================

# THE LABEL REGISTRY (L-214)
#
# Two axes, not one list. TRANSPORT says whether a label's text is
# shown to an outside responder or kept at home. GRAMMAR -- whether a
# body is validated, and against what -- is not here: it stays in
# provenance_scanner.py, with the scanner's line patterns derived from
# these names. Moving the names without the grammar is deliberate; a
# keys module that owned the semantics would be a second place for the
# meaning of a leg to drift.
#
# Before this registry existed, a label outside the set was not
# recognised as a LABEL at all, so deliberate withholding and silent
# dropping shared one code path and could not be told apart from
# inside it. That is L-209, and it is why the registry names the
# withheld labels explicitly rather than leaving them to fall through.

# The leg the citation verdict answers, and the legs that are shown
# but never verdicted. Break 5, 2026-08-15. `Note` joined them in
# L-214: it was already the corpus's most-used context label and was
# being dropped in silence on every dispatch.
VERDICTED_LEG = 'Source'
CONTEXT_LEGS = ('Ref', 'Also', 'See', 'Derived', 'Calculation', 'Note')

# Labels whose text is deliberately NOT shown to a responder. A second
# reader must not see what the last one concluded, or the leg stops
# being independent. `Review-note` is the free-form one -- withheld,
# with no body grammar -- and it exists because a record that is not a
# cross-check and not a resolution had nowhere to live.
RECORD_LEGS = ('Cross-checked', 'Resolved', 'Removed', 'Corrected',
               'Review-note')

TRAVELS = 'travels'
WITHHELD = 'withheld'

LABEL_TRANSPORT = {}
for _name in (VERDICTED_LEG,) + CONTEXT_LEGS:
    LABEL_TRANSPORT[_name] = TRAVELS
for _name in RECORD_LEGS:
    LABEL_TRANSPORT[_name] = WITHHELD
del _name

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

# Generic detection, ahead of classification. This matches the SHAPE of
# a labelled line and says nothing about whether the label is known.
# The invariant it buys: every syntactically labelled line attached to
# a claim finishes legs_of() in one named disposition. There is no
# disposition called `fell through the regex`.
ANY_LABEL_RE = re.compile(
    r'^\s*#\s*([A-Za-z][A-Za-z0-9_ /.-]{0,30})(\+)?:\s*(.*)$')

# Kept for the travelling set, and still what a caller asking `is this
# a citation leg` should use. It is no longer what legs_of() dispatches
# on -- that is ANY_LABEL_RE -- because building the detector from the
# vocabulary is the defect L-214 removed.
Legs = namedtuple(
    'Legs', 'cited context problems unmarked joined unknown')


def continues_a_leg(line):
    """True when this comment line is unlabelled continuation text."""
    if not COMMENT_RE.match(line) or line.strip() == '#':
        return False
    if PADDED_RE.match(line):
        return True
    return not OTHER_LABEL_RE.match(line)


def legs_of(attached_text):
    """Legs(cited, context, problems, unmarked, joined, unknown).

    Returns the `# Source:` lines and, separately, every other leg.
    Both are lists: a run carrying two Source lines is a malformation
    (L-195) and this reports both rather than picking one.

    A citation too long for one line continues on a marked line naming
    the leg it continues -- `# Source+:` under `# Source:`. Those are
    joined back onto their leg here, so the worksheet quotes the whole
    citation rather than its first line.

    `problems` holds continuation markers that could not be joined: one
    naming a different leg than the line above it, or one with no leg
    above it at all. Their label is reported and their text is NOT
    joined, because
    attaching it to the wrong authority is the failure this marker was
    made leg-specific to catch. `joined` counts the lines that did join,
    so a run that joins nothing says so rather than looking identical to
    a run with nothing to join.

    `unmarked` holds continuation text carrying no marker at all. That
    text is invisible everywhere -- not joined, and not printed into the
    worksheet the way a mismatched marker is -- so the builder refuses
    to write a request while any exists, rather than reporting it. Each
    entry is the offending line, stripped. Only a TRAVELLING leg can
    carry one: text under a withheld label is withheld with it, and
    nothing is being dropped from a request it was never entering.

    `unknown` holds the names of labels the registry does not carry.
    Their text is withheld -- never shipped to a responder on the
    strength of a label nobody has classified -- and the name is
    returned so the builder can print it. Report, not reject: a
    reported label is one this project can then read and decide about,
    where a rejected one stops the run and the decision never gets
    made. (Tony's ruling, 2026-08-19.)
    """
    verdicted = []
    context = []
    problems = []
    unmarked = []
    unknown = []
    joined = 0
    open_label = None
    open_leg = None
    open_travels = False
    for line in (attached_text or '').splitlines():
        # PADDING IS CHECKED FIRST, and the order is load-bearing.
        # `#   Highly ellipsoidal: 1050x840x537 km` is continuation
        # text, not a label called `Highly ellipsoidal`. Before L-214
        # the label test could not see it because the label had to be
        # in the vocabulary; now that ANY_LABEL_RE matches any
        # `# Word:` shape, the padding test is what keeps that line a
        # continuation.
        match = None if PADDED_RE.match(line) else ANY_LABEL_RE.match(line)
        if not match:
            # A line that continues a TRAVELLING leg but carries no
            # marker is the failure this refuses on. Under a withheld
            # leg the same line is withheld with it and is not a
            # defect -- nothing is being dropped from a request the
            # text was never going into. Anything else closes the run,
            # so a marker separated from its leg by unrelated prose
            # cannot join across the gap.
            if open_label is not None and continues_a_leg(line):
                if open_travels:
                    unmarked.append(line.strip())
                continue
            open_label = None
            open_leg = None
            open_travels = False
            continue
        label = match.group(1).strip()
        marker = match.group(2)
        body = match.group(3).strip()
        transport = LABEL_TRANSPORT.get(label)
        if transport is None:
            # The disposition L-214 exists to create. An unrecognised
            # label is WITHHELD, never silently dropped, and its name
            # is reported so a reader can decide what it should be.
            if label not in unknown:
                unknown.append(label)
            transport = WITHHELD
        if transport == WITHHELD:
            open_label = label
            open_leg = None
            open_travels = False
            continue
        if marker:
            if open_label is None:
                problems.append(
                    '`%s+:` continuation with no leg above it to join'
                    % label)
            elif not open_travels:
                problems.append(
                    '`%s+:` continuation under a withheld `%s:` leg'
                    % (label, open_label))
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
        open_travels = True
    return Legs(verdicted, context, problems, unmarked, joined, unknown)



def parse_sites_doc(path):
    """[(module, enclosing, label)] from L192_annotated_sites.txt at the repo root.

    One parser, because the format has more than one consumer. Both
    test_worksheet_keys.py and test_extractor_pins.py read this file,
    and each carried its own copy of this loop until a RETIRED row was
    added for a deliberately retired key: the copy that had learned the
    tag passed, the copy that had not crashed on int('2026-08-16').
    Fixing the consumer that broke would have left the same landmine
    for the third consumer. (2026-08-16)

    THE STORE ANCHORS BY NAME, NOT LINE (L-277, 2026-09-03). The
    second column is the enclosing function or module-level constant,
    the third the label -- the same two parts the key is made of. A
    line number went stale on every comment inserted above a site, and
    for constants it had ALREADY gone stale without the round trip
    noticing, because a stale line falls back to the label and the
    label is the key. A second column that is all digits is that old
    format, and it is refused rather than read: the caller must not
    be handed rows that look right and mean something else.

    A RETIRED row records why a site left the corpus and is skipped
    here. The inverted assertion that gives it teeth lives with the
    pins, in test_worksheet_keys.py -- this loader only has to not
    choke on it.
    """
    sites = []
    with open(path, encoding='utf-8') as handle:
        for number, raw in enumerate(handle, 1):
            raw = raw.rstrip('\n')
            if not raw.strip() or raw.startswith('#'):
                continue
            if raw.startswith(RETIRED_TAG + '\t'):
                continue
            parts = raw.split('\t')
            if len(parts) < 3:
                continue
            if parts[1].isdigit():
                raise KeyError_(
                    '%s line %d anchors by line number (%r); since L-277 the '
                    'store anchors by enclosing name -- rewrite the row, do '
                    'not patch the number' % (path, number, raw))
            sites.append((parts[0], parts[1], parts[2]))
    return sites


def compose(module, enclosing, label='', ordinal=None):
    """Build a key from its parts.

    `module` is a file name, not a path: a key names a module, and the
    absolute path differs between Tony's machine and any sandbox.
    """
    module = os.path.basename(module)
    parts = [module, enclosing]
    if label and label != enclosing:
        parts.append(label)
    if ordinal is not None:
        parts.append('%s%d' % (ORDINAL_PREFIX, ordinal))
    return KEY_SEP.join(parts)


def parse(key):
    """Split a key. Raises KeyError_ on anything malformed.

    Malformed is loud on purpose. A key that quietly parses to
    something plausible is a check that cannot fail.
    """
    if not key or not isinstance(key, str):
        raise KeyError_('empty key')
    parts = key.split(KEY_SEP)
    if len(parts) < 2:
        raise KeyError_('key needs at least module and enclosing: %r' % key)
    ordinal = None
    if parts[-1].startswith(ORDINAL_PREFIX) and parts[-1][1:].isdigit():
        ordinal = int(parts[-1][1:])
        parts = parts[:-1]
    if len(parts) > 3:
        raise KeyError_('too many segments: %r' % key)
    module = parts[0]
    enclosing = parts[1] if len(parts) > 1 else ''
    label = parts[2] if len(parts) > 2 else enclosing
    if not module.endswith('.py'):
        raise KeyError_('first segment is not a module file: %r' % key)
    return Key(module, enclosing, label, ordinal)


def enclosing_name(source, line):
    """The def or module-level assignment a line sits inside.

    A function wins over an assignment. A display string usually sits
    inside a local assignment too -- `trace = go.Scatter3d(...)` -- and
    those names are generic and short-lived, while the create_*_shell()
    function that holds them is the stable, human-meaningful handle.
    Only when no function contains the line does a module-level
    assignment answer, which is the module-level string case.

    Returns '' when neither contains the line. That is a real answer,
    not a failure, and the caller falls back to the label.
    """
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return ''

    def contains(node):
        start = getattr(node, 'lineno', None)
        end = getattr(node, 'end_lineno', None)
        return start is not None and end is not None and start <= line <= end

    best, best_span = '', None
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) \
                and contains(node):
            span = node.end_lineno - node.lineno
            if best_span is None or span < best_span:
                best, best_span = node.name, span
    if best:
        return best

    for node in tree.body:
        if isinstance(node, ast.Assign) and contains(node):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    return target.id
    return ''


def locate_site(source, enclosing, label):
    """(line, reason): the line that introduces `label` inside `enclosing`.

    The inverse of key_for_site, and what lets the site store carry a
    name instead of a line (L-277). Returns the 1-based line of the
    dict key or assignment that introduces the label -- the same line
    worksheet_checker.anchor_label reads -- or (None, reason), where
    the reason names which of three things failed:

      SITE_UNREADABLE  the module does not parse
      SITE_LOST        no such enclosing, or no such label inside it
      SITE_AMBIGUOUS   the label is introduced more than once inside it

    A label equal to its enclosing is a module-level assignment (a
    constant or a module-level string) and resolves to that statement.
    None of the three is silent, on purpose: a site that cannot be
    found and reports nothing is the failure this module exists to
    make impossible.
    """
    try:
        tree = ast.parse(source)
    except SyntaxError as exc:
        return None, 'SITE_UNREADABLE: source does not parse (%s)' % exc
    lines = source.splitlines()

    if label == enclosing:
        for node in tree.body:
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == enclosing:
                        return node.lineno, ''

    span = None
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) \
                and node.name == enclosing:
            span = (node.lineno, node.end_lineno)
            break
    if span is None:
        return None, 'SITE_LOST: no %s' % enclosing

    hits = []
    for number in range(span[0], span[1] + 1):
        text = lines[number - 1]
        match = DICT_KEY_RE.match(text) or ASSIGN_NAME_RE.match(text)
        if match and match.group(1) == label:
            hits.append(number)
    if len(hits) == 1:
        return hits[0], ''
    if not hits:
        return None, 'SITE_LOST: no %r inside %s' % (label, enclosing)
    return None, ('SITE_AMBIGUOUS: %r introduced %d times inside %s (lines %s)'
                  % (label, len(hits), enclosing,
                     ', '.join(str(h) for h in hits)))


def key_for_site(module_path, source, line, label='', ordinal=None):
    """Mint the key for one claim at one site.

    `label` comes from the checker's anchor_label -- the dict key or
    assignment that introduces the unit. It is passed in rather than
    recomputed here so that the label has exactly one owner, the same
    reason this module exists for the enclosing name.
    """
    enclosing = enclosing_name(source, line)
    if not enclosing:
        enclosing = label
    return compose(module_path, enclosing, label, ordinal)


def resolve(key, sources, aliases=None):
    """Find the site a key names.

    `sources` maps module file name -> source text. `aliases` maps a
    retired key to its replacement, recording a rename that happened;
    chains resolve transitively.

    Returns (line, reason). A `line` of None means unresolved, and
    `reason` says which layer gave up -- never a silent drop, because
    a key that resolves to nothing and reports nothing is the failure
    this module was built to make impossible.
    """
    # None means "use the map installed beside the checker"; pass an
    # empty dict to resolve with no aliases at all. The distinction
    # matters: a caller that forgets the argument should get the real
    # map, because a check in a store nobody reads cannot fail.
    if aliases is None:
        aliases = INSTALLED_ALIASES
    original = key
    hops = []
    while key in aliases:
        if key in hops:
            return None, 'ALIAS_CYCLE: %s' % ' -> '.join(hops + [key])
        hops.append(key)
        key = aliases[key]

    def failed(reason):
        """A broken alias is its own finding, never a stale key.

        The difference routes a different errand: KEY_STALE asks a
        human whether a rename happened, ALIAS_STALE says a human
        already answered that and answered it wrong.
        """
        if hops:
            return None, 'ALIAS_STALE: %s -> %s, %s' % (original, key, reason)
        return None, 'KEY_STALE: %s' % reason

    parsed = parse(key)
    source = sources.get(parsed.module)
    if source is None:
        return failed('no module %s' % parsed.module)

    try:
        tree = ast.parse(source)
    except SyntaxError as exc:
        return failed('%s does not parse (%s)' % (parsed.module, exc))

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if node.name == parsed.enclosing:
                return node.lineno, ''
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == parsed.enclosing:
                    return node.lineno, ''

    return failed('no %s in %s' % (parsed.enclosing, parsed.module))


def shift_check(recorded_count, recorded_unit, current_count, current_unit):
    """Has the ordinal stopped meaning what it meant?

    Runs BEFORE any value comparison. Returns None when the ordinal is
    still sound, or a KEY_SHIFTED reason string when it is not.
    """
    if recorded_count is not None and recorded_count != current_count:
        return SHIFT_COUNT % (recorded_count, current_count)
    if recorded_unit and (recorded_unit or '').lower() != (current_unit or '').lower():
        return SHIFT_UNIT % (recorded_unit, current_unit)
    return SHIFT_OK
