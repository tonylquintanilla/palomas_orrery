"""
patch_L322_D_14_prov220_skill.py

Built on 0e3d05fd498f1ae8b49ec5dba58503f6bf448576
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Written 2026-09-27 with Anthropic's Claude Opus 5.5, Tony Quintanilla
integrator.

WHAT THIS DOES

One skill update, provenance-discipline 2.19 -> 2.20, and the protocol
entry that records it (v3.69 -> v3.70). Three files:

  skills/provenance-discipline/SKILL.md
  PROJECT_INSTRUCTIONS.md
  documentation/PROJECT_INSTRUCTIONS_HISTORY.md

Two changes to the skill, one version. Rule 2 gains one paragraph
saying where a trailing ".0" comes from. It is Python, by three routes: a decimal point is typed to
make a number a float, Python's division always returns a float, and a
float printed without a format always shows ".0". None of the three is
a statement about significant figures. So a row's figure count is never
read from its literal, its printed form or its exported form. Checked
by running Python 3 and Node on 2026-09-27.

Rule 7's exact row is brought into line with the code that builds it,
orrery patch D15, on Tony's approval of 2026-09-27: where the print
count is read (directly after "exact --"), what count a declared
construction takes (the digits of the value its rule gives, 4.5 prints
two), the checker's three refusals (more digits than the number has,
too few to write it in full, anything but 1 on a zero), and the check
that fails the maintenance run while a printed exact row is not printed
by its count. Run it with D15; the two agree line for line.

If you already ran the earlier copy of this patch, use Discard Changes
in GitHub Desktop on the three files first; this copy replaces it.

The protocol gains its v3.70 history entry. v3.67, the oldest of the
three resident entries, moves down into the history file, so an entry
still lives in exactly one place.

HOW TO RUN

  Save this file in the ORRERY REPO ROOT (the folder that contains
  PROJECT_INSTRUCTIONS.md and the skills/ folder). Open it in VS Code
  and click Run.

WHAT SUCCESS LOOKS LIKE

  One "ok" line per edit, then three "stamp" lines naming the header
  stamps it moved, then "patch applied" naming all three files.

WHAT FAILURE LOOKS LIKE

  A single line beginning "ERROR:" (a file is not the one this was
  built on) or "ANCHOR FAIL:" (an edit's text was not found exactly
  once). NOTHING is written if anything fails: all three files are
  checked before any is written. Undo after a success is Discard
  Changes in GitHub Desktop.

AFTERWARD -- FOUR STEPS, ONE COMMIT (ledger-and-session-records,
binding rule)

  1. This patch: the skill's version line and new paragraph, and the
     protocol history entry.
  2. Run the orrery maintenance run. Its "Skill manifest" step is
     skills_index.py; it rewrites the manifest table in
     PROJECT_INSTRUCTIONS.md from 2.19 to 2.20.
  3. Commit the three files and the manifest change together, and push.
  4. Reinstall provenance-discipline to your account (Settings > Skills).

  This session cannot confirm the reinstall. The next session confirms
  its loaded copy reads 2.20 before any provenance work.

  Then move this script into documentation/.

WHAT IS PERMANENT

  The script is disposable. The new paragraph and the v3.70 entry are
  not.
"""

import hashlib
import os
import sys

SKILL = os.path.join('skills', 'provenance-discipline', 'SKILL.md')
PROTO = 'PROJECT_INSTRUCTIONS.md'
HIST = os.path.join('documentation', 'PROJECT_INSTRUCTIONS_HISTORY.md')

FINGERPRINTS = {
    SKILL: 'bf8418e3fde8cb3fb4754fcb0261c58b',
    PROTO: '66fda6fcb0fed2462e0fca7415083cf6',
    HIST: '3da51999f2d5b58896367a5557974197',
}


# ----------------------------------------------------------------------
# provenance-discipline 2.20
# ----------------------------------------------------------------------

SKILL_EDITS = []

SKILL_EDITS.append((
    'stamp: version line',
    b"""Skill version: 2.19 | Cut from palomas_orrery @ de4eadc5 (v2.19),
earlier @ ac25d4f4 (v2.18),""",
    b"""Skill version: 2.20 | Cut from palomas_orrery @ 0e3d05fd (v2.20),
earlier @ de4eadc5 (v2.19), @ ac25d4f4 (v2.18),""",
))

SKILL_EDITS.append((
    'stamp: date and v2.20 paragraph',
    b"""| September 25, 2026
v2.19 replaces""",
    b"""| September 27, 2026
v2.20 writes down where a trailing ".0" comes from, in Rule 2. It is
Python, by three routes, and none of them is a statement about
significant figures: a decimal point is typed to make a number a
float, Python's division always returns a float, and a float printed
without a format always shows ".0". So a row's figure count is never
read from its literal, its printed form or its exported form, which is
why the count and an exact row's print count are both fields. Tony
asked for the claim to be checked and added on 2026-09-27, when the
Stage D print counts were settled from what each row says it was
chosen with. Checked by running Python 3 and Node. RULE 7'S EXACT ROW
is brought into line with the code that builds it, orrery patch D15:
the print count is read only directly after "exact --"; a declared
construction prints the digits of the value its rule gives, so the
outer belt's midpoint of 4 and 5 prints 4.5; the checker refuses a
count with more digits than the number has, one too small to write it
in full, and anything but 1 on a zero; and exact_rows_report.py
--check fails the maintenance run while any printed exact row is not
printed by its count. The last two are Claude Opus 5.5's additions in
building D15, approved by Tony the same day. Handle L-322.
v2.19 replaces""",
))

SKILL_EDITS.append((
    'Rule 2: where a trailing .0 comes from',
    b"""chosen cut angle) is exact for counting: it is a choice, not a
measurement, so all of its digits are known.
""",
    b"""chosen cut angle) is exact for counting: it is a choice, not a
measurement, so all of its digits are known.

**A trailing `.0` in this store is Python's, not a figure** (v2.20).
The digits of a choice are the digits it was chosen with, and a decimal
point Python needs is not one of them. A trailing `.0` reaches this
store and its displays by three routes, and none of them says anything
about significant figures:

- **Typing.** Python treats a number written with a decimal point as a
  float and one without as a whole number, so rows are typed `200.0`
  to make them floats. `200`, `200.0` and `200.00` are the same stored
  number; the float keeps no record of how it was typed. That is also
  why `13.50` is stored as `13.5` (Rule 1).
- **Arithmetic.** Division in Python always returns a float, even
  between whole numbers: `4 / 2` is `2.0`. A derived row can gain a
  `.0` from its expression without anyone typing one.
- **Printing.** A float printed with no format always shows at least
  one decimal place, so a whole-number float prints as `2.0`. That
  covers `str()`, a bare f-string `{x}`, and `json.dumps`, which
  writes `constants_export.json`. A format can remove it (`:g` prints
  `2`) and a page can put it back: the gallery printed the declared
  solar wind pressure as "2.0 nPa" by its own `toFixed(1)`, from a
  value JavaScript had read out of the export as plain 2.

So the literal, the printed value, the exported value and the page's
output cannot say which trailing zeros are meant. For a measured row
the source's reporting resolution says (above). For an exact row the
digits it was defined or chosen with say: the declared pressure is
2 nPa because Shue et al. (1998) use Dp = 2 nPa, and the `.0` in
`2.0` is Python's. That is why the count is a field on the
`# Figures:` line and an exact row's print count is a field too
(Rule 7), never read from the value. A choice that really was made to
a trailing zero says so on its `# Declared:` line, and its print count
states it. (Checked by running Python 3 and Node on 2026-09-27, at
Tony's request, when the Stage D print counts were settled. Handle
L-322.)
""",
))

SKILL_EDITS.append((
    'Rule 7 exact row: the parts',
    b"""2.0 and 120. Three parts:
""",
    b"""2.0 and 120. The parts:
""",
))

SKILL_EDITS.append((
    'Rule 7 exact row: the field, the count, the checker',
    b"""- **The print count is a field.** Every exact row a display prints
  states it on its `# Figures:` line as `exact -- prints N`, and a
  derived exact row inherits the print count of its defining input.
  It has to be a field because the literal cannot carry it. Python
  types whole numbers with a trailing `.0` by habit, and for a declared
  pick there is no source resolution to say whether that zero counts
  (Rule 2), so a count read from the literal would print a floor chosen
  as 200 km as \"200.0 km\". The checker refuses a print count larger
  than the significant digits the literal actually has. A zero prints
  as 0. An exact row no display prints carries no print count, and a
  page that reaches an exact row with none reports it rather than
  choosing a width.
""",
    b"""- **The print count is a field.** Every exact row a display prints
  states it on its `# Figures:` line directly after `exact --`, as
  `exact -- prints N`. That is the only place a checker reads it:
  measured rows' lines say \"the source prints 1.5\" in prose, and
  prose is never read. It has to be a field because the literal cannot
  carry it. A trailing `.0` is Python's, not a figure (Rule 2), and for
  a declared pick there is no source resolution to say whether a zero
  counts, so a count read from the literal would print a floor chosen
  as 200 km as \"200.0 km\". The count is the digits the definition or
  the choice was stated with: 3 for that floor, 1 for Shue's 2 nPa. An
  exact row defined from another exact row writes its defining input's
  count on its own line; nothing carries a count between rows. A
  DECLARED CONSTRUCTION (Rule 2) prints the digits of the value its
  rule gives, not the counts of the measured rows its rule is over,
  which are figure counts and not print counts: the midpoint of 4 and
  5 prints 4.5, two figures. Its line carries both fields:
  `exact -- prints 2, the digits of the value its rule gives (4.5);
  declared construction: midpoint of <row>, <row>`.
- **The checker refuses three counts** (v2.20). A count with more
  digits than the number has: for a typed number, the digits of the
  literal as written, trailing zeros included, so 200.0 allows up to
  four; for an expression, the digits of the value it computes. A
  count too small to write the number out in full, because an exact
  number printed rounded is a different number: 105 at two figures
  would print 100. And any count but 1 on a zero, which prints as 0.
  `constants_rows.print_count_problem()` makes all three, and the
  export stops on any of them. An exact row no display prints carries
  no print count. A display that reaches an exact row with none
  reports it rather than choosing a width: in the orrery,
  `constants_rows.exact_text()` raises where the display is built.
  `exact_rows_report.py --check` fails, naming each item, when a
  printed exact row states no count, when an orrery line prints one
  any way but `exact_text()`, or when the gallery does not serve the
  count beside it; the maintenance run runs it as \"Exact rows by the
  count\".
""",
))

SKILL_EDITS.append((
    'Rule 7 exact row: the example stays true after the build',
    b"""  \"Drawn to 120 degrees\", today by a width of 0 decimals chosen at the
  call site. Under this rule the row states `exact -- prints 3` and the
  page prints three figures; counted from the literal it would print
  \"120.0\".
""",
    b"""  \"Drawn to 120 degrees\", until Stage D by a width of 0 decimals chosen
  at the call site. Under this rule the row states `exact -- prints 3`
  and the page prints three figures; counted from the literal it would
  print \"120.0\".
""",
))

V370 = b"""v3.70 (September 27, 2026): No rule changed in this document. ONE
skill bump, provenance-discipline 2.19 -> 2.20 (L-322). WHERE A
TRAILING ".0" COMES FROM IS WRITTEN DOWN.

WHAT PROMPTED IT. The session that opened the Stage D print-count
build, manifest section 6, settled the print counts of the seven
printed exact rows from what each row's own comment says it was chosen
with: the declared solar wind pressure prints "2 nPa" because Shue's
paper uses 2 nPa, not "2.0". Tony confirmed that, and asked that the
claim behind it be checked and put in the skill: that the trailing
zero in a value like 2.0 comes from Python, not from significant
figures.

WHAT THE CHECK FOUND. Checked by running Python 3 and Node. The claim
holds, by three routes rather than one. Python needs a decimal point to
make a number a float, so rows are typed 200.0, and the stored float
keeps no record of how it was typed. Python's division always returns
a float, so 4 / 2 is 2.0. And a float printed without a format,
including by json.dumps into constants_export.json, always shows ".0".
The gallery's "2.0 nPa" turned out to be a fourth case: the page's own
toFixed(1), applied to a value JavaScript had read as plain 2.

WHAT THE SKILL NOW SAYS. Rule 2 gains one paragraph naming the three
routes and what follows from them: a row's figure count is never read
from its literal, its printed form or its exported form, which is why
the count and an exact row's print count are both fields. A choice
that really was made to a trailing zero says so on its # Declared:
line.

RULE 7'S EXACT ROW MATCHES THE CODE THAT BUILDS IT, orrery patch D15,
built the same session. The print count is read only directly after
"exact --". A declared construction prints the digits of the value its
rule gives, so the outer belt's midpoint of 4 and 5 prints 4.5. The
checker refuses a count with more digits than the number has, one too
small to write it in full, and anything but 1 on a zero. And
exact_rows_report.py --check fails the maintenance run while a printed
exact row is not printed by its count. The second refusal and the
declared construction's count were Claude's additions while building
D15; Tony approved both on 2026-09-27, on the condition that the code,
the provenance rules and the significant-figure rules all agree.

THE OBLIGATION TRAVELS, as it always does. This session loaded 2.19,
and a reinstall cannot be verified from inside the session that makes
it. The next session confirms its loaded copy reads 2.20 before any
provenance or constants_new.py work. That session is gallery patch 4,
the gallery half of section 6.

The header stamp and the SHA anchor move with this entry.

Version history: v3.67 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

"""

V367_START = b"v3.67 (September 22, 2026): No rule changed in this document. ONE\n"
V367_END_MARK = b"Version history: v3.64 moves down to\ndocumentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three\nresident.\n\n"

HIST_ANCHOR = b"""(Moved down from the resident protocol on 2026-09-25 when
v3.69 made a fourth entry.)
"""


def fingerprint(data):
    """md5 of the content, CRLF normalised, with the protocol's Skill
    Manifest zone left out: skills_index.py rewrites that zone, so a
    guard that fenced it could refuse for a reason that is not about
    content (safe-file-editing, A Guard Must Not Fence What a Generator
    Rewrites)."""
    lf = data.replace(b'\r\n', b'\n')
    start = b'<!-- SKILL-MANIFEST:START'
    end = b'<!-- SKILL-MANIFEST:END -->'
    if start in lf and end in lf:
        a = lf.index(start)
        b = lf.index(end) + len(end)
        lf = lf[:a] + lf[b:]
    return hashlib.md5(lf).hexdigest()


def fail(msg):
    print(msg)
    print('NOTHING was written. Undo is not needed.')
    sys.exit(1)


def load(path):
    if not os.path.exists(path):
        fail('ERROR: %s not found. Run this from the orrery repo root.' % path)
    with open(path, 'rb') as f:
        data = f.read()
    fp = fingerprint(data)
    if fp != FINGERPRINTS[path]:
        fail('ERROR: %s is not the file this patch was built on '
             '(fingerprint %s, expected %s). Pull or discard local '
             'changes first.' % (path, fp, FINGERPRINTS[path]))
    return data


def convention(data, old, new):
    if data.count(b'\r\n') > 0:
        return old.replace(b'\n', b'\r\n'), new.replace(b'\n', b'\r\n')
    return old, new


def apply_edits(path, data, edits):
    for label, old, new in edits:
        old, new = convention(data, old, new)
        n = data.count(old)
        if n != 1:
            fail('ANCHOR FAIL: %s: "%s" -- expected 1 match, got %d'
                 % (path, label, n))
        data = data.replace(old, new)
        print('ok    %s: %s' % (path, label))
    return data


def ascii_check(path, data):
    try:
        data.decode('ascii')
    except UnicodeDecodeError as exc:
        fail('ERROR: %s would not be ASCII after the patch (%s).'
             % (path, exc))


def main():
    if os.path.basename(os.getcwd()) == 'documentation':
        fail('ERROR: this is running from documentation/. Run it from the '
             'orrery repo root, then file it in documentation/.')

    skill = load(SKILL)
    proto = load(PROTO)
    hist = load(HIST)

    skill = apply_edits(SKILL, skill, SKILL_EDITS)

    # Protocol: header stamp, anchor, the new entry, and v3.67 cut out.
    proto = apply_edits(PROTO, proto, [
        ('stamp: header version and date',
         b"Tony Quintanilla, PE | Claude | v3.69 | September 25, 2026",
         b"Tony Quintanilla, PE | Claude | v3.70 | September 27, 2026"),
        ('stamp: SHA anchor',
         b"Cut from de4eadc5 at https://github.com/tonylquintanilla/palomas_orrery",
         b"Cut from 0e3d05fd at https://github.com/tonylquintanilla/palomas_orrery"),
        ('history: v3.70 entry',
         b"v3.69 (September 25, 2026): No rule changed in this document. ONE\n",
         V370 + b"v3.69 (September 25, 2026): No rule changed in this document. ONE\n"),
    ])
    start, end_mark = convention(proto, V367_START, V367_END_MARK)
    if proto.count(start) != 1 or proto.count(end_mark) != 1:
        fail('ANCHOR FAIL: %s: v3.67 entry boundaries not found exactly once'
             % PROTO)
    i = proto.index(start)
    j = proto.index(end_mark) + len(end_mark)
    if j <= i:
        fail('ANCHOR FAIL: %s: v3.67 entry ends before it starts' % PROTO)
    v367 = proto[i:j]
    proto = proto[:i] + proto[j:]
    print('ok    %s: v3.67 entry cut (%d bytes)' % (PROTO, len(v367)))

    # History: v3.67 lands after v3.66, with its own moved-down note.
    note = (b"(Moved down from the resident protocol on 2026-09-27 when\n"
            b"v3.70 made a fourth entry.)\n")
    anchor, _ = convention(hist, HIST_ANCHOR, b"")
    if hist.count(anchor) != 1:
        fail('ANCHOR FAIL: %s: the v3.66 moved-down note not found exactly '
             'once' % HIST)
    if hist.count(b'\r\n') > 0:
        note = note.replace(b'\n', b'\r\n')
        sep = b'\r\n'
    else:
        sep = b'\n'
    hist = hist.replace(anchor, anchor + sep + v367.rstrip(b'\r\n') + sep
                        + sep + note)
    print('ok    %s: v3.67 entry added to PART 1' % HIST)

    for path, data in ((SKILL, skill), (PROTO, proto), (HIST, hist)):
        ascii_check(path, data)

    for path, data in ((SKILL, skill), (PROTO, proto), (HIST, hist)):
        with open(path, 'wb') as f:
            f.write(data)

    print('stamp %s: Skill version 2.20, cut from 0e3d05fd, 2026-09-27'
          % SKILL)
    print('stamp %s: v3.70, cut from 0e3d05fd, 2026-09-27' % PROTO)
    print('stamp %s: v3.67 moved down, dated 2026-09-27' % HIST)
    print('patch applied: %s, %s, %s' % (SKILL, PROTO, HIST))
    print('Next: run the orrery maintenance run (its Skill manifest step is '
          'skills_index.py), then commit all of it together.')


if __name__ == '__main__':
    main()
