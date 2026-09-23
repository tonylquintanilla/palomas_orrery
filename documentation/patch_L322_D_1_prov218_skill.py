"""
patch_L322_D_1_prov218_skill.py

Built on ac25d4f44a0607f734fdf98f21095e869abe790b
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Written 2026-09-23 with Anthropic's Claude Opus 5.5, Tony Quintanilla
integrator. Step 1 of L-322 Stage D: the skill update the build waits
for. The build itself is a later session.

WHAT THIS DOES

One skill update, provenance-discipline 2.17 -> 2.18, and the protocol
entry that records it (v3.67 -> v3.68). Three files:

  skills/provenance-discipline/SKILL.md
  PROJECT_INSTRUCTIONS.md
  documentation/PROJECT_INSTRUCTIONS_HISTORY.md

The skill gains four things, all settled with Tony on 2026-09-22 and
2026-09-23 in the Stage D manifest conversation:

  1. THREE KINDS OF DRAWING NUMBER (Tony's ruling). A physical value
     lives in constants_new.py; an eyeballed value does not promote; a
     rendering setting such as opacity or point count stays in the
     drawing code. This replaces the scope boundary in One Value, One
     Home, and fixes the sentence in A Drawing Approximation Does Not
     Promote that said opacity and point count stay "in the store".
  2. THE EXACT ROW, added to Rule 7, with a sixth form in Rule 1.
  3. THE CONVERSION ROW, added to Rule 3.
  4. THE MIDPOINT DEFAULT, added to When the Source Gives a Range.

The protocol gains its v3.68 history entry. v3.65, the oldest of the
three resident entries, moves down into the history file, so an entry
still lives in exactly one place.

HOW TO RUN

  Save this file in the ORRERY REPO ROOT (the folder that contains
  PROJECT_INSTRUCTIONS.md and the skills/ folder). Open it in VS Code
  and click Run.

  Or from a terminal in that folder:
      python patch_L322_D_1_prov218_skill.py

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

  1. This patch: the skill's version line and body, and the protocol
     history entry.
  2. Run skills_index.py (open it, click Run). It rewrites the manifest
     table in PROJECT_INSTRUCTIONS.md and prints the 2.17 -> 2.18 move.
  3. Commit the three files and the manifest change together, and push.
  4. Reinstall provenance-discipline to your account (Settings > Skills).

  This session cannot confirm the reinstall. The next session, the
  Stage D build, confirms its loaded copy reads 2.18 before touching
  constants_new.py.

  Then move this script into documentation/.

WHAT IS PERMANENT

  The script is disposable. The four rules it writes into the skill
  and the v3.68 entry are not.
"""

import hashlib
import os
import sys

SKILL = os.path.join('skills', 'provenance-discipline', 'SKILL.md')
PROTO = 'PROJECT_INSTRUCTIONS.md'
HIST = os.path.join('documentation', 'PROJECT_INSTRUCTIONS_HISTORY.md')

FINGERPRINTS = {
    SKILL: '55228c9984d4a1447262b19882f865c1',
    PROTO: 'c43772787f4e2eb124471294fb2b86a2',
    HIST: 'e467c0fe41b7a5ca78dac23b4c215002',
}


# ----------------------------------------------------------------------
# provenance-discipline 2.18
# ----------------------------------------------------------------------

SKILL_EDITS = []

# Stamp: version line, cut-from list, date, and the v2.18 paragraph.
SKILL_EDITS.append((
    'stamp: version line and v2.18 paragraph',
    b"""Skill version: 2.17 | Cut from palomas_orrery @ 1f6e55a9 (v2.17),
earlier @ a7014abb (v2.16),""",
    b"""Skill version: 2.18 | Cut from palomas_orrery @ ac25d4f4 (v2.18),
earlier @ 1f6e55a9 (v2.17), @ a7014abb (v2.16),""",
))

SKILL_EDITS.append((
    'stamp: date and v2.18 paragraph',
    b"""| September 22, 2026
v2.17 closes the gap a display decision opened.""",
    b"""| September 23, 2026
v2.18 settles where a drawing number lives and how an exact number
prints, before L-322 Stage D builds on both. THE SCOPE BOUNDARY in One
Value, One Home becomes THREE KINDS OF DRAWING NUMBER, Tony's ruling
of 2026-09-22: a physical value (a size, an edge, a cut angle) lives
in constants_new.py, sourced or declared; an eyeballed value does not
promote and is cleaned up as the braid reaches it; a rendering setting
(point count, opacity, colour, marker, font) stays in the drawing
code. The test is whether changing the number moves WHERE something
is drawn. This removes a contradiction: A Drawing Approximation Does
Not Promote said opacity and point count stay in the store, while One
Value, One Home kept them in the drawing code. RULE 7 GAINS THE EXACT
ROW: an exact quantity is stored in the form its definition prints,
every exact row a display prints states a print count as a field, and
the page prints by that count instead of by a width chosen at each
call site. RULE 1 gains the sixth form that carries it. RULE 3 GAINS
THE CONVERSION ROW: a unit conversion inside an expression is an
exact row with a compound-unit token, never a bare 3600, because the
unit check converts units by itself. WHEN THE SOURCE GIVES A RANGE
gains its default: the midpoint, unless the row states a reason for
an end. Worked cases: Earth's obliquity, which Horizons defines as
84381.448 arcseconds, and Earth's sidereal rotation period, whose
bare-divisor draft failed the unit check while the figures check
passed it. From Claude Fable 5.1's review of the Stage D manifest and
Claude Opus 5.5's answers to it, 2026-09-23; every form was run
through both checkers on a throwaway copy at ac25d4f4. Handle L-322.
v2.17 closes the gap a display decision opened.""",
))

# When the source gives a range: the midpoint default.
SKILL_EDITS.append((
    'range: midpoint default',
    b"""end. The rule is that **the pick is a declared choice and its reason
lives on the row.**
""",
    b"""end. The rule is that **the pick is a declared choice and its reason
lives on the row.**

**Where nothing in the source favours an end, the pick is the
midpoint** (v2.18). That is the construction the outer belt's peak and
the gravitational influence already use. An end is picked only for a
reason the row states, as the helmet cusp's top and the core's low end
do. So the question "which point in the range" is answered by this
section and does not go to Tony; a reason to leave the midpoint is
written on the row, where the next reader can check it. (Tony,
2026-09-23, on the magnetotail's flare, which Slavin et al. (1983)
place at 100 to 120 Earth radii: "I thought the midpoint
interpolation is in the skill." It was the practice and not the rule;
it is the rule now.)
""",
))

# A Drawing Approximation Does Not Promote: fix the contradiction.
SKILL_EDITS.append((
    'approximation: no longer lists rendering settings as stored',
    b"""**Two things this does not forbid**, and both matter or the rule
overreaches. A DECLARED drawing choice stays legal and stays in the
store -- opacity, point count, a pick from a sourced range with its
reason on the row. And a visibility stylization""",
    b"""**Two things this does not forbid**, and both matter or the rule
overreaches. A DECLARED pick that stands for a physical size -- a
pick from a sourced range with its reason on the row -- stays legal
and lives in constants_new.py. (Until v2.18 this sentence also listed
opacity and point count as staying "in the store"; they are rendering
settings, and One Value, One Home's Three Kinds of Drawing Number keeps
them in the drawing code.) And a visibility stylization""",
))

# One Value, One Home: the scope boundary becomes three kinds.
SKILL_EDITS.append((
    'one home: three kinds of drawing number',
    b"""**THE SCOPE BOUNDARY, and it must be stated in the same breath.**
MEASURED values migrate. DECLARED DRAWING PARAMETERS do not:
`n_points`, `marker_size`, `opacity`, `mesh_resolution`, an angular
marker step. Those stay where they are drawn. That is L-240's split, and
without it "only store" reads as hauling 25 and 3.4 into
`constants_new.py`, which buries the values that matter under the ones
that do not.
""",
    b"""**THE SCOPE BOUNDARY, and it must be stated in the same breath:
THREE KINDS OF DRAWING NUMBER** (v2.18, Tony's ruling of 2026-09-22).
Every number a drawing uses is one of three kinds, and each kind has
one home.

- **A PHYSICAL value** -- a size, an edge, a distance, a cut angle, a
  width -- lives in `constants_new.py`. A measured one is sourced. A
  decided one is declared, with its reason and the range it was picked
  from on the row (When the Source Gives a Range).
- **An EYEBALLED value** -- a physical value chosen because the render
  looked right, usually before the sourcing rules existed -- does not
  promote (A Drawing Approximation Does Not Promote). It is replaced by
  one of that section's three outcomes as the braid reaches it, and a
  published room is reached first.
- **A RENDERING SETTING** -- `n_points`, `n_rings`, `marker_size`,
  marker type, `opacity`, colour, font, `mesh_resolution`, an angular
  marker step -- makes no claim about the object. It stays in the
  drawing code where it is drawn. Tony: "these are defined in the code
  not in constants new."

**The test between the first kind and the third: does changing the
number move WHERE something is drawn, or only change HOW it looks?**
Earth's radiation-belt thickness of 0.5 Earth radii was the case that
needed the test. It looks like a drawing setting, but it moves where the
rings sit, so it is physical; with no recorded origin it is eyeballed,
and Stage D replaces it by the belts' served edges. A point count only
makes the same ring smoother.

Two notes on the third kind. A colour is a rendering setting, but a
hover sentence saying what colour the object IS is a claim and needs a
source like any other. And two rendering settings were still in
`constants_new.py` when this was written, `DEFAULT_MARKER_SIZE` and
`CENTER_MARKER_SIZE`; they are one ledger class and move to the drawing
code when their files are next touched.

This is L-240's split, sharpened. Without it "only store" reads as
hauling 25 and 3.4 into `constants_new.py`, which buries the values
that matter under the ones that do not.
""",
))

# Rule 1: a sixth form.
SKILL_EDITS.append((
    'rule 1: sixth form',
    b"""**Rule 1. `# Figures:` is a comment key beside the value.** Five forms:

```
# Figures: 5 -- set by EARTH_INNER_CORE_KM (1221.5, 5)
# Figures: 5 -- PREM reports to 0.1 km, so 3480.0's trailing zero counts
# Figures: exact -- IAU 2012 definition
""",
    b"""**Rule 1. `# Figures:` is a comment key beside the value.** Six forms:

```
# Figures: 5 -- set by EARTH_INNER_CORE_KM (1221.5, 5)
# Figures: 5 -- PREM reports to 0.1 km, so 3480.0's trailing zero counts
# Figures: exact -- IAU 2012 definition
# Figures: exact -- prints 8, the definition's own digits (84381.448)
""",
))

SKILL_EDITS.append((
    'rule 1: exact rows state a print count',
    b"""zero counts, because an integer literal cannot. A defined constant says
`exact`.""",
    b"""zero counts, because an integer literal cannot. A defined constant says
`exact`, and when a display prints it, also how many figures it prints
(`prints N`, Rule 7's exact row).""",
))

# Rule 3: the conversion row, after the DEG_PER_RAD paragraph.
SKILL_EDITS.append((
    'rule 3: the conversion row',
    b"""both checkers before this was written. `DEG_PER_RAD` has no store
inputs, so neither checker judges it and its unit is asserted; the
row says so in words, as a definition.
""",
    b"""both checkers before this was written. `DEG_PER_RAD` has no store
inputs, so neither checker judges it and its unit is asserted; the
row says so in words, as a definition.

**A unit conversion inside an expression is an exact row, never a bare
number** (v2.18). The unit check converts units by itself, so dividing
seconds by a bare 3600 leaves seconds. Earth's sidereal rotation period
was drafted as `2 * math.pi / EARTH_ROTATION_RATE_RAD_S / 3600.0` and
declared in hours; the unit check failed it as a MISMATCH, the
arithmetic giving 0.006648 hours against 23.93447 stored, while the
figures check passed the same row. The conversion is an exact row with
a compound-unit token -- `S_PER_HOUR` in `s_per_h`, `ARCSEC_PER_DEG` in
`arcsec_per_deg` -- and the expression divides by the row. A pure number
that belongs to the physics, like the two pi in a period, stays bare,
because the token it meets already treats the radian as dimensionless;
giving it a unit fails the check the other way ("declares s; the
arithmetic gives rad s"). Both forms were run through both checkers
before this was written. (Claude Fable 5.1's review of the Stage D
manifest, Finding 1, re-run by Claude Opus 5.5 at ac25d4f4. Other rows
that convert by a bare number, such as `LIGHT_MINUTES_PER_AU`, are one
ledger class.)
""",
))

# Rule 7: the exact row.
SKILL_EDITS.append((
    'rule 7: the exact row',
    b"""of that permission reached Tony as a readability call. Tony,
2026-09-21: "the basis should be in the skill not arbitrary.")
""",
    b"""of that permission reached Tony as a readability call. Tony,
2026-09-21: "the basis should be in the skill not arbitrary.")

**An exact row prints the digits its definition states** (v2.18). An
exact quantity has unlimited figures, so a served count of `exact`
cannot tell a page how many to print. Until v2.18 the gallery's
`fmtServed` printed every exact row with `toFixed` and a number of
places chosen at each of its call sites, which is the page choice this
rule forbids; nobody noticed while the exact rows were numbers like
2.0 and 120. Three parts:

- **Stored in the form its definition prints.** A quantity defined in
  arcseconds is a row in arcseconds, and its degree form is an
  expression over it and an exact conversion row (Rule 3). Horizons
  defines its ecliptic of J2000 by an obliquity of 84381.448
  arcseconds, so `EARTH_OBLIQUITY_J2000_ARCSEC` holds that and
  `EARTH_OBLIQUITY_J2000_DEG` divides it by `ARCSEC_PER_DEG`. The unit
  check then judges the degree row, instead of trusting a literal that
  has no inputs.
- **The print count is a field.** Every exact row a display prints
  states it on its `# Figures:` line as `exact -- prints N`, and a
  derived exact row inherits the print count of its defining input.
  It has to be a field because the literal cannot carry it. Python
  types whole numbers with a trailing `.0` by habit, and for a declared
  pick there is no source resolution to say whether that zero counts
  (Rule 2), so a count read from the literal would print a floor chosen
  as 200 km as "200.0 km". The checker refuses a print count larger
  than the significant digits the literal actually has. A zero prints
  as 0. An exact row no display prints carries no print count, and a
  page that reaches an exact row with none reports it rather than
  choosing a width.
- **The export carries it and the page prints by it.** The export
  serves the print count beside the value, and the page prints an
  exact row to that many significant figures. `toFixed` goes for exact
  rows. Earth's obliquity prints 23.439291 degrees, eight figures from
  84381.448.

(Claude Fable 5.1's review of the Stage D manifest, 2026-09-23,
Finding 2; the print-count field is Claude Opus 5.5's amendment to it
in the same round, because Fable's form counted from the literal.
Tony accepted both on 2026-09-23. The checker, the export and the page
implement this in the Stage D build.)
""",
))


# ----------------------------------------------------------------------
# PROJECT_INSTRUCTIONS.md v3.68
# ----------------------------------------------------------------------

V368 = b"""v3.68 (September 23, 2026): No rule changed in this document. ONE
skill bump, taken ahead of the build it serves, which is v3.55's
ordering.

provenance-discipline 2.17 -> 2.18 (L-322). WHERE A DRAWING NUMBER
LIVES, AND HOW AN EXACT NUMBER PRINTS.

THREE KINDS OF DRAWING NUMBER ARE TONY'S RULING. A physical value, such
as a size, an edge or a cut angle, lives in constants_new.py, sourced
or declared. A value chosen by eye does not promote, and is replaced as
the braid reaches it, published rooms first. A rendering setting, such
as opacity, point count, colour, marker or font, stays in the drawing
code. Tony, 2026-09-22: "these are defined in the code not in
constants new." The skill had contradicted itself on this for two
versions, one section keeping opacity and point count in the drawing
code and another listing them as stored. The test between the kinds is
whether changing the number moves where something is drawn. Earth's
belt thickness was the case that needed it: it looks like a setting,
it moves where the rings sit, and with no source it is replaced by the
belts' served edges.

THE EXACT ROW CAME FROM A QUESTION NOBODY COULD ANSWER. The Stage D
manifest asked how many figures Earth's obliquity should print. It is
exact, because Horizons defines its ecliptic frame by it, and Rule 7
said nothing about exact rows. Measured, the gallery printed every
exact row by a width chosen at each call site. Claude Fable 5.1's
answer: store a definition in the form it is printed, 84381.448
arcseconds, and print its own digits. Claude Opus 5.5 added the print
count as a field on the row, because a Python literal cannot tell a
meant trailing zero from a typing habit: counted from the literal, a
floor chosen as 200 km would print as 200.0.

THE CONVERSION ROW CAME FROM A CHECK THAT PASSED WHILE WRONG. Fable
ran the unit checker on the draft rotation-period row, written with a
bare divide-by-3600, and it failed: the checker converts units by
itself and found 0.0066 hours against 23.93 stored. The figures checker
passed the same row, so one checker alone looked green. A conversion is
now an exact row with its own unit.

THE MIDPOINT BECAME THE DEFAULT ON TONY'S READING. Asked where the
magnetotail's flare should end inside its sourced 100 to 120 Earth
radii, Tony said he thought the midpoint was already the skill's rule.
It was the practice in every case and not written anywhere. It is
written now: the midpoint, unless the row states a reason for an end.

THE OBLIGATION TRAVELS, as it always does. This session loaded 2.17,
and a reinstall cannot be verified from inside the session that makes
it. The next session confirms its loaded copy reads 2.18 before any
provenance or constants_new.py work, and that session is the Stage D
build, from documentation/BUILD_MANIFEST_L322_D_earth_pole_20260922.md
revision 2, with Fable's review filed beside it.

The header stamp and the SHA anchor move with this entry.

Version history: v3.65 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

"""

V365_START = b"v3.65 (September 20, 2026): No rule changed in this document. ONE\n"
V365_END_MARK = b"Version history: v3.62 moves down to\ndocumentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three\nresident.\n\n"

HIST_ANCHOR = b"""(Moved down from the resident protocol on 2026-09-22 when
v3.67 made a fourth entry.)
"""


def fingerprint(data):
    return hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()


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
    skill = load(SKILL)
    proto = load(PROTO)
    hist = load(HIST)

    skill = apply_edits(SKILL, skill, SKILL_EDITS)

    # Protocol: header stamp, anchor, the new entry, and v3.65 cut out.
    proto = apply_edits(PROTO, proto, [
        ('stamp: header version and date',
         b"Tony Quintanilla, PE | Claude | v3.67 | September 22, 2026",
         b"Tony Quintanilla, PE | Claude | v3.68 | September 23, 2026"),
        ('stamp: SHA anchor',
         b"Cut from 1f6e55a9 at https://github.com/tonylquintanilla/palomas_orrery",
         b"Cut from ac25d4f4 at https://github.com/tonylquintanilla/palomas_orrery"),
        ('history: v3.68 entry',
         b"v3.67 (September 22, 2026): No rule changed in this document. ONE\n",
         V368 + b"v3.67 (September 22, 2026): No rule changed in this document. ONE\n"),
    ])
    start, end_mark = convention(proto, V365_START, V365_END_MARK)
    if proto.count(start) != 1 or proto.count(end_mark) != 1:
        fail('ANCHOR FAIL: %s: v3.65 entry boundaries not found exactly once'
             % PROTO)
    i = proto.index(start)
    j = proto.index(end_mark) + len(end_mark)
    if j <= i:
        fail('ANCHOR FAIL: %s: v3.65 entry ends before it starts' % PROTO)
    v365 = proto[i:j]
    proto = proto[:i] + proto[j:]
    print('ok    %s: v3.65 entry cut (%d bytes)' % (PROTO, len(v365)))

    # History: v3.65 lands after v3.64, with its own moved-down note.
    note = (b"(Moved down from the resident protocol on 2026-09-23 when\n"
            b"v3.68 made a fourth entry.)\n")
    anchor, _ = convention(hist, HIST_ANCHOR, b"")
    if hist.count(anchor) != 1:
        fail('ANCHOR FAIL: %s: the v3.64 moved-down note not found exactly '
             'once' % HIST)
    if hist.count(b'\r\n') > 0:
        note = note.replace(b'\n', b'\r\n')
        sep = b'\r\n'
    else:
        sep = b'\n'
    hist = hist.replace(anchor, anchor + sep + v365.rstrip(b'\r\n') + sep
                        + sep + note)
    print('ok    %s: v3.65 entry added to PART 1' % HIST)

    for path, data in ((SKILL, skill), (PROTO, proto), (HIST, hist)):
        ascii_check(path, data)

    for path, data in ((SKILL, skill), (PROTO, proto), (HIST, hist)):
        with open(path, 'wb') as f:
            f.write(data)

    print('stamp %s: Skill version 2.18, cut from ac25d4f4, 2026-09-23'
          % SKILL)
    print('stamp %s: v3.68, cut from ac25d4f4, 2026-09-23' % PROTO)
    print('stamp %s: v3.65 moved down, dated 2026-09-23' % HIST)
    print('patch applied: %s, %s, %s' % (SKILL, PROTO, HIST))
    print('Next: run skills_index.py, then commit all of it together.')


if __name__ == '__main__':
    main()
