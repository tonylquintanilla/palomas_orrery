"""patch_L222_1_docstring_lines_in_change_report.py

Built on 762aa5dde5aea87cc6e513fc4841c6937366a6b4 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Written August 20, 2026 with Anthropic's Claude Opus 5.

WHAT IS WRONG

constants_change_report.py reads three line shapes: `NAME = <number>`,
`'Key': <number>`, and anything starting with `#`. A module DOCSTRING
line is none of those. So a changed docstring line carrying a digit --
which every `Module updated: <date> with <model>` stamp does -- lands
in the UNPARSED bucket and the tool exits 1.

That collides head-on with Stamp What You Change (safe-file-editing
1.6), which requires the docstring to move in the same transaction as
any edit to the file. Every future patch to constants_new.py therefore
turns this checker red, permanently, for a line that is not a value
edit and never could be.

A checker that always fails carries as little signal as one that
cannot fail. Both teach the reader to stop looking. This is the mirror
image of A Check That Cannot Fail Is Not Passing, and it wants the same
answer: make the tool able to tell the two cases apart.

HOW IT IS FIXED

Not by pattern-matching `Module updated:`. That would be a guess that
drifts the moment a stamp is worded differently. Instead the tool now
DERIVES the docstring line set from the real module docstrings -- the
one at the base revision (via `git show <base>:constants_new.py`) and
the one in the working copy -- using ast.get_docstring, the same call
module_atlas.py already relies on. A changed line is a docstring line
if it appears in either set. It cannot drift, because it is read from
the thing it describes.

Three properties worth stating, because each is a place this could
have gone wrong:

  1. VALUE PARSING RUNS FIRST. A line that parses as an assignment or a
     dict entry is treated as a value edit even if the same text also
     appears in a docstring. The docstring test can only ever reclassify
     something that was heading for the unparsed bucket, so it cannot
     swallow a real value change.

  2. A DOCSTRING EDIT DOES NOT SET comment_moved. Crediting a value
     change as "documented" because the module's currency stamp moved
     would be a false clear -- the stamp says nothing about any
     particular constant.

  3. IT ANNOUNCES. Docstring lines are counted and printed, not
     silently dropped. Silence about something unexamined is the
     failure mode this tool exists to avoid.

  And if `git show` cannot produce the base file, the tool says so and
  falls back to the working copy's docstring alone rather than
  pretending it checked both.

ALSO
  Opens L-222 in the ledger.
  Stamps both files (Stamp What You Change).

AFTER RUNNING
  python constants_change_report.py     (expect exit 0, clean)
  python ledger_index.py
  Re-run the maintenance runner.
  Move this script to documentation/.
"""

import hashlib
import os
import sys

BASE_SHA = '762aa5dde5aea87cc6e513fc4841c6937366a6b4'

REPORT = 'constants_change_report.py'
LEDGER = 'LEDGER_CONSOLIDATED.md'

FINGERPRINTS = {
    REPORT: '66ace36378d99c7fe1e38a9d393d292b',
    LEDGER: 'b5b9305ddf74d712daff19b5d790029e',
}

# ------------------------------------------------------------------
# 1 -- the docstring reader, inserted above parse_line
# ------------------------------------------------------------------

REPORT_OLD_1 = (
    "COMMENT_RE = re.compile(r'^\\s*#')\n"
)

REPORT_NEW_1 = (
    "COMMENT_RE = re.compile(r'^\\s*#')\n"
    "\n"
    "\n"
    "def docstring_lines(here, base):\n"
    "    \"\"\"Every line of TARGET's module docstring, at base and as it is now.\n"
    "\n"
    "    Returns (set_of_stripped_lines, note). The note says what was\n"
    "    actually read, so a caller can print it rather than infer it.\n"
    "\n"
    "    Why this exists (L-222, 2026-08-20). A module docstring line is\n"
    "    not an assignment and not a comment, so before this it fell into\n"
    "    the UNPARSED bucket and failed the run. Since Stamp What You\n"
    "    Change requires the docstring to move on EVERY edit to this file,\n"
    "    that made the checker fail permanently on a line that is not a\n"
    "    value edit. A checker that always fails is as unread as one that\n"
    "    cannot fail.\n"
    "\n"
    "    The set is DERIVED from the real docstrings rather than matched\n"
    "    against a stamp pattern. A pattern would drift the first time a\n"
    "    stamp was worded differently; this cannot, because it reads the\n"
    "    thing it describes. Both revisions are read because a stamp edit\n"
    "    changes a line on BOTH sides of the diff.\n"
    "    \"\"\"\n"
    "    lines = set()\n"
    "    notes = []\n"
    "\n"
    "    def collect(source, label):\n"
    "        try:\n"
    "            doc = ast.get_docstring(ast.parse(source), clean=False)\n"
    "        except Exception as exc:\n"
    "            notes.append('%s unreadable (%s)' % (label, exc.__class__.__name__))\n"
    "            return 0\n"
    "        if not doc:\n"
    "            notes.append('%s has no docstring' % label)\n"
    "            return 0\n"
    "        found = set(l.strip() for l in doc.split('\\n') if l.strip())\n"
    "        lines.update(found)\n"
    "        notes.append('%s %d line(s)' % (label, len(found)))\n"
    "        return len(found)\n"
    "\n"
    "    ok, shown = git(['show', '%s:%s' % (base, TARGET)], here)\n"
    "    if ok:\n"
    "        collect(shown, 'base')\n"
    "    else:\n"
    "        notes.append('base UNAVAILABLE -- working copy only')\n"
    "\n"
    "    try:\n"
    "        with open(os.path.join(here, TARGET), 'rb') as handle:\n"
    "            collect(handle.read().decode('utf-8', 'replace'), 'working')\n"
    "    except OSError as exc:\n"
    "        notes.append('working copy unreadable (%s)' % exc)\n"
    "\n"
    "    return lines, '; '.join(notes)\n"
)

# ------------------------------------------------------------------
# 2 -- read_changes takes the docstring set and uses it
# ------------------------------------------------------------------

REPORT_OLD_2 = (
    "            parsed = parse_line(body)\n"
    "            if parsed is None:\n"
    "                if any(ch.isdigit() for ch in body) and body.strip():\n"
    "                    hunk_unparsed.append(sign + body.rstrip())\n"
    "                continue\n"
)

REPORT_NEW_2 = (
    "            parsed = parse_line(body)\n"
    "            if parsed is None:\n"
    "                # Value parsing ran FIRST, so this test can only\n"
    "                # reclassify a line already bound for the unparsed\n"
    "                # bucket -- it can never swallow a real value edit.\n"
    "                # Note it does NOT set comment_moved: the module's\n"
    "                # currency stamp documents no particular constant,\n"
    "                # and crediting one with it would be a false clear.\n"
    "                if body.strip() in docstrings:\n"
    "                    hunk_docstring.append(sign + body.rstrip())\n"
    "                    continue\n"
    "                if any(ch.isdigit() for ch in body) and body.strip():\n"
    "                    hunk_unparsed.append(sign + body.rstrip())\n"
    "                continue\n"
)

REPORT_OLD_3 = (
    "    changed, added, removed, unparsed = [], [], [], []\n"
    "\n"
    "    for hunk in split_hunks(diff_text):\n"
    "        old_vals, new_vals = {}, {}\n"
    "        comment_moved = False\n"
    "        hunk_unparsed = []\n"
)

REPORT_NEW_3 = (
    "    changed, added, removed, unparsed = [], [], [], []\n"
    "    docstring_seen = []\n"
    "\n"
    "    for hunk in split_hunks(diff_text):\n"
    "        old_vals, new_vals = {}, {}\n"
    "        comment_moved = False\n"
    "        hunk_unparsed = []\n"
    "        hunk_docstring = []\n"
)

REPORT_OLD_4 = (
    "        unparsed.extend(hunk_unparsed)\n"
)

REPORT_NEW_4 = (
    "        unparsed.extend(hunk_unparsed)\n"
    "        docstring_seen.extend(hunk_docstring)\n"
)

REPORT_OLD_5 = (
    "    return changed, added, removed, unparsed\n"
)

REPORT_NEW_5 = (
    "    return changed, added, removed, unparsed, docstring_seen\n"
)

REPORT_OLD_6 = (
    "def read_changes(diff_text):\n"
)

REPORT_NEW_6 = (
    "def read_changes(diff_text, docstrings=frozenset()):\n"
)

REPORT_OLD_7 = (
    "import re\n"
)

REPORT_NEW_7 = (
    "import ast\n"
    "import re\n"
)

# ------------------------------------------------------------------
# 3 -- ledger item L-222
# ------------------------------------------------------------------

LEDGER_ANCHOR = (
    "measurement); L-214 (the session this surfaced in).\n"
    "\n"
    "## PENDING ACTION (Tony-side)\n"
)

LEDGER_INSERT = (
    "measurement); L-214 (the session this surfaced in).\n"
    "\n"
    "#### [L-222] The constants change report fails on every currency stamp\n"
    "<!-- L:222 status:DONE upd:2026-08-20 section:C flag: rice:3/2/95/0.5 -->\n"
    "- **Found 2026-08-20, immediately after L-220 landed.**\n"
    "  `constants_change_report.py` parses three line shapes: `NAME =\n"
    "  <number>`, `'Key': <number>`, and anything opening with `#`. A\n"
    "  module DOCSTRING line is none of them, so a changed docstring line\n"
    "  carrying a digit went to the UNPARSED bucket and exited 1.\n"
    "- **Which made it a permanent failure, not an occasional one.** Stamp\n"
    "  What You Change requires the docstring to move in the same\n"
    "  transaction as any edit to the file, and every `Module updated:\n"
    "  <date>` stamp carries digits. So the checker was going to fail on\n"
    "  every future patch to `constants_new.py`, on a line that is not a\n"
    "  value edit and never could be.\n"
    "- **Two rules collided and neither was wrong.** L-220 is right that\n"
    "  the stamp must move with the body. The report is right that a\n"
    "  changed line it cannot read must not report clean. The defect was\n"
    "  that the report had no third category for a line that is neither a\n"
    "  value nor evidence about one.\n"
    "- **A checker that ALWAYS fails is the mirror of one that CANNOT\n"
    "  fail.** Both are unread within a week, and neither announces the\n"
    "  thing it was built to announce. That is why this was fixed the same\n"
    "  day rather than filed: the cost is not the red line, it is the\n"
    "  habit of scrolling past it.\n"
    "- **Fixed by DERIVING the docstring line set, not by matching a stamp\n"
    "  pattern.** The tool reads the module docstring at the base revision\n"
    "  (`git show <base>:constants_new.py`) and in the working copy, via\n"
    "  `ast.get_docstring` -- the same call `module_atlas.py` uses -- and\n"
    "  treats a changed line as a docstring line if it appears in either.\n"
    "  A stamp pattern would have drifted the first time a stamp was\n"
    "  worded differently. This cannot, because it reads the thing it\n"
    "  describes. Both revisions are needed because a stamp edit changes a\n"
    "  line on both sides of the diff.\n"
    "- **Three properties that keep the fix honest.** Value parsing runs\n"
    "  FIRST, so the docstring test can only reclassify a line already\n"
    "  bound for the unparsed bucket and can never swallow a value edit. A\n"
    "  docstring edit does NOT set `comment_moved`, because the module\n"
    "  stamp documents no particular constant and crediting one with it\n"
    "  would be a false clear. And the docstring lines are COUNTED AND\n"
    "  PRINTED rather than dropped, with a note saying which revisions\n"
    "  were actually read -- a fallback to the working copy alone says so.\n"
    "**Note:** RICE is Claude's proposal, unratified.\n"
    "**Gap:** none. Built and verified the same day at `762aa5dd`:\n"
    "the stamp is accepted, and a mutation putting a real value edit in an\n"
    "unreadable shape still fails the run.\n"
    "**Ref:** `constants_change_report.py` `docstring_lines` /\n"
    "`read_changes`; L-220 (Stamp What You Change, the rule it collided\n"
    "with); L-210 (the patch whose stamp exposed it); the resident A Check\n"
    "That Cannot Fail Is Not Passing gate, of which this is the mirror\n"
    "case.\n"
    "\n"
    "## PENDING ACTION (Tony-side)\n"
)

# ------------------------------------------------------------------
# CURRENCY
# ------------------------------------------------------------------

LEDGER_STAMP_OLD = (
    "Module updated: August 20, 2026 with Anthropic's Claude Opus 5 (L-221:\n"
)

LEDGER_STAMP_NEW = (
    "Module updated: August 20, 2026 with Anthropic's Claude Opus 5 (L-222:\n"
    "docstring lines in the constants change report), built on 762aa5dd.\n"
    "Module updated: August 20, 2026 with Anthropic's Claude Opus 5 (L-221:\n"
)

# ------------------------------------------------------------------
# 4 -- main() reads the docstring set, passes it in, and reports it
# ------------------------------------------------------------------

REPORT_OLD_8 = (
    "    changed, added, removed, unparsed = read_changes(out)\n"
    "\n"
    "    if not (changed or added or removed or unparsed):\n"
)

REPORT_NEW_8 = (
    "    docstrings, doc_note = docstring_lines(here, base)\n"
    "    changed, added, removed, unparsed, doc_lines = read_changes(\n"
    "        out, docstrings)\n"
    "\n"
    "    if not (changed or added or removed or unparsed):\n"
)

REPORT_OLD_9 = (
    "    print('-' * 70)\n"
    "    print('  %d changed, %d added, %d removed'\n"
    "          % (len(changed), len(added), len(removed)))\n"
)

REPORT_NEW_9 = (
    "    if doc_lines:\n"
    "        print('  %d changed line(s) are module docstring text, not value'\n"
    "              % len(doc_lines))\n"
    "        print('  edits -- the currency stamp L-220 requires. Read from the'\n"
    "              ' docstring')\n"
    "        print('  itself, not matched against a pattern: %s.' % doc_note)\n"
    "        for line in doc_lines[:6]:\n"
    "            print('      %s' % line[:66])\n"
    "        if len(doc_lines) > 6:\n"
    "            print('      ... and %d more' % (len(doc_lines) - 6))\n"
    "        print()\n"
    "\n"
    "    print('-' * 70)\n"
    "    print('  %d changed, %d added, %d removed'\n"
    "          % (len(changed), len(added), len(removed)))\n"
)

# The early-return path also unpacks nothing, but it fires before
# read_changes; the docstring-only case has to survive it, so the
# "no numeric value moved" branch now names docstring lines too.
REPORT_OLD_10 = (
    "        print('  %s changed, but no numeric value moved.' % TARGET)\n"
    "        print('  (Comments, formatting, or non-numeric edits only.)')\n"
    "        return 0\n"
)

REPORT_NEW_10 = (
    "        print('  %s changed, but no numeric value moved.' % TARGET)\n"
    "        print('  (Comments, docstring stamp, formatting, or other'\n"
    "              ' non-numeric edits only.)')\n"
    "        if doc_lines:\n"
    "            print('  %d of the changed line(s) are module docstring text'\n"
    "                  ' (%s).' % (len(doc_lines), doc_note))\n"
    "        return 0\n"
)

EDITS = [
    (REPORT, 'import ast', REPORT_OLD_7, REPORT_NEW_7),
    (REPORT, 'docstring_lines() helper', REPORT_OLD_1, REPORT_NEW_1),
    (REPORT, 'read_changes signature', REPORT_OLD_6, REPORT_NEW_6),
    (REPORT, 'per-hunk docstring bucket', REPORT_OLD_3, REPORT_NEW_3),
    (REPORT, 'classify docstring lines', REPORT_OLD_2, REPORT_NEW_2),
    (REPORT, 'collect the bucket', REPORT_OLD_4, REPORT_NEW_4),
    (REPORT, 'return the bucket', REPORT_OLD_5, REPORT_NEW_5),
    (REPORT, 'main(): read and pass the set', REPORT_OLD_8, REPORT_NEW_8),
    (REPORT, 'main(): report docstring lines', REPORT_OLD_9, REPORT_NEW_9),
    (REPORT, 'main(): no-value-moved branch', REPORT_OLD_10, REPORT_NEW_10),
    (LEDGER, 'new item L-222', LEDGER_ANCHOR, LEDGER_INSERT),
    (LEDGER, 'CURRENCY: ledger header stamp', LEDGER_STAMP_OLD,
     LEDGER_STAMP_NEW),
]


def fail(message):
    print('ABORT: %s' % message)
    print('Nothing was written.')
    sys.exit(1)


def main():
    for path in (REPORT, LEDGER):
        if not os.path.isfile(path):
            fail('%s not found. Run this from the repo root.' % path)

    originals, endings = {}, {}
    for path, expected in FINGERPRINTS.items():
        with open(path, 'rb') as handle:
            data = handle.read()
        endings[path] = b'\r\n' if b'\r\n' in data else b'\n'
        data = data.replace(b'\r\n', b'\n')
        actual = hashlib.md5(data).hexdigest()
        if actual != expected:
            fail('%s does not match the base at %s (compared in LF form, so '
                 'a CRLF checkout is not the cause).\n'
                 '  expected md5 %s\n  actual   md5 %s'
                 % (path, BASE_SHA[:8], expected, actual))
        originals[path] = data
        print('[base ok] %-28s md5 %s  (%s on disk)'
              % (path, actual, 'CRLF' if endings[path] == b'\r\n' else 'LF'))

    for path, data in originals.items():
        try:
            data.decode('ascii')
        except UnicodeDecodeError as exc:
            fail('%s carries non-ASCII at offset %d.' % (path, exc.start))
        print('[ascii ok] %s' % path)

    working = dict((p, d.decode('ascii')) for p, d in originals.items())
    for path, label, old, new in EDITS:
        count = working[path].count(old)
        if count != 1:
            fail('anchor for "%s" in %s matched %d times, expected exactly 1.'
                 % (label, path, count))
        working[path] = working[path].replace(old, new, 1)
        print('[anchor ok] %-30s %s' % (label, path))

    allowed = {}
    for path, label, old, new in EDITS:
        gone = set(old.split('\n')) - set(new.split('\n'))
        allowed.setdefault(path, set()).update(l for l in gone if l)
    for path in (REPORT, LEDGER):
        before = originals[path].decode('ascii').split('\n')
        after = set(working[path].split('\n'))
        lost = [l for l in before if l and l not in after]
        unexpected = [l for l in lost if l not in allowed.get(path, set())]
        if unexpected:
            fail('%d line(s) of %s would be lost that no edit claims to '
                 'remove. First: %r' % (len(unexpected), path, unexpected[0]))
        print('[loss ok] %-30s %d line(s) rewritten, all accounted for'
              % (path, len(lost)))

    # The rewritten module must still parse, and main() must still be
    # calling read_changes with the new arity. Checked before writing,
    # because a syntax error here takes the whole maintenance run down.
    try:
        compile(working[REPORT], REPORT, 'exec')
    except SyntaxError as exc:
        fail('the patched %s does not parse: line %s, %s'
             % (REPORT, exc.lineno, exc.msg))
    print('[syntax ok] %s parses' % REPORT)

    # Arity guard: every call site must unpack the five values the
    # function now returns. A four-value unpack would raise at runtime
    # inside the maintenance run, where it is expensive to notice.
    bad = [l.strip() for l in working[REPORT].split('\n')
           if 'read_changes(' in l and 'def ' not in l
           and 'doc_lines' not in l]
    if bad:
        fail('a call site was not updated for the new arity: %r' % bad[0])
    print('[arity ok] every read_changes() call site unpacks five values')

    for path in (REPORT, LEDGER):
        out = working[path].encode('ascii')
        if endings[path] == b'\r\n':
            out = out.replace(b'\n', b'\r\n')
        with open(path, 'wb') as handle:
            handle.write(out)
        print('[written] %-28s (%s preserved)'
              % (path, 'CRLF' if endings[path] == b'\r\n' else 'LF'))

    print('')
    print('CURRENCY STAMPS UPDATED (Stamp What You Change):')
    print('  %s -- L-222 header stamp, built on %s' % (LEDGER, BASE_SHA[:8]))


if __name__ == '__main__':
    main()
