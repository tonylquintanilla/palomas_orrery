"""
patch_L322_D_11_prov219_skill.py

Built on de4eadc58e3de746183515dff422aaab3943fe6a
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Written 2026-09-25 with Anthropic's Claude Opus 5.5, Tony Quintanilla
integrator.

WHAT THIS DOES

One skill update, provenance-discipline 2.18 -> 2.19, and the protocol
entry that records it (v3.68 -> v3.69). Three files:

  skills/provenance-discipline/SKILL.md
  PROJECT_INSTRUCTIONS.md
  documentation/PROJECT_INSTRUCTIONS_HISTORY.md

The skill's Rule 7 gave Earth's obliquity as its example of an exact
row a display prints. Since the Stage D manifest's revision 3 no
display prints the obliquity; the axis hovers print the tilt of date.
The example becomes the gallery's magnetopause hover, which prints the
exact row EARTH_MAGNETOPAUSE_CUT_ANGLE_DEG, and the obliquity stays as
the case of an exact row no display prints. No rule changes.

The protocol gains its v3.69 history entry. v3.66, the oldest of the
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

  1. This patch: the skill's version line and example, and the
     protocol history entry.
  2. Run the orrery maintenance run. Its "Skill manifest" step is
     skills_index.py; it rewrites the manifest table in
     PROJECT_INSTRUCTIONS.md from 2.18 to 2.19.
  3. Commit the three files and the manifest change together, and push.
  4. Reinstall provenance-discipline to your account (Settings > Skills).

  This session cannot confirm the reinstall. The next session, gallery
  patch 3, confirms its loaded copy reads 2.19 before any provenance
  work.

  Then move this script into documentation/.

WHAT IS PERMANENT

  The script is disposable. The new example and the v3.69 entry are
  not.
"""

import hashlib
import os
import sys

SKILL = os.path.join('skills', 'provenance-discipline', 'SKILL.md')
PROTO = 'PROJECT_INSTRUCTIONS.md'
HIST = os.path.join('documentation', 'PROJECT_INSTRUCTIONS_HISTORY.md')

FINGERPRINTS = {
    SKILL: '8e4e607faf23498b8a96fe35195c63be',
    PROTO: '4756fb86793a05fbab003d519ced24b7',
    HIST: '4552eab95e49f2a8e2fc7dc66903fdbe',
}


# ----------------------------------------------------------------------
# provenance-discipline 2.19
# ----------------------------------------------------------------------

SKILL_EDITS = []

SKILL_EDITS.append((
    'stamp: version line',
    b"""Skill version: 2.18 | Cut from palomas_orrery @ ac25d4f4 (v2.18),
earlier @ 1f6e55a9 (v2.17),""",
    b"""Skill version: 2.19 | Cut from palomas_orrery @ de4eadc5 (v2.19),
earlier @ ac25d4f4 (v2.18), @ 1f6e55a9 (v2.17),""",
))

SKILL_EDITS.append((
    'stamp: date and v2.19 paragraph',
    b"""| September 23, 2026
v2.18 settles""",
    b"""| September 25, 2026
v2.19 replaces one worked example that had gone stale. Rule 7's exact
row said Earth's obliquity "prints 23.439291 degrees". Since the Stage
D manifest's revision 3 (2026-09-23) no display prints the obliquity:
the axis hovers print the tilt of date, worked out from the pole
Horizons serves, and the obliquity row is used only as the angle that
defines the ecliptic frame. The rule itself stands; the example now is
the gallery's magnetopause hover, which prints the exact row
EARTH_MAGNETOPAUSE_CUT_ANGLE_DEG today with a width chosen at the call
site. Found carried in two handoffs; checked against the skill, the
manifest and the code on 2026-09-25, where every consumer of the
obliquity was also confirmed to use the right value for the right job.
Handle L-322.
v2.18 settles""",
))

SKILL_EDITS.append((
    'Rule 7 exact row: the worked example',
    b"""  exact row to that many significant figures. `toFixed` goes for exact
  rows. Earth's obliquity prints 23.439291 degrees, eight figures from
  84381.448.
""",
    b"""  exact row to that many significant figures. `toFixed` goes for exact
  rows. The gallery's magnetopause hover is the case: it prints
  `EARTH_MAGNETOPAUSE_CUT_ANGLE_DEG`, a declared limit typed 120.0, as
  "Drawn to 120 degrees", today by a width of 0 decimals chosen at the
  call site. Under this rule the row states `exact -- prints 3` and the
  page prints three figures; counted from the literal it would print
  "120.0".
- **Earth's obliquity carries no print count.** It is the row this
  rule was first written on, and it was the example until v2.19. Since
  the Stage D manifest's revision 3 no display prints it: the axis
  hovers print the tilt of date, worked out from Horizons' pole, and
  `EARTH_OBLIQUITY_J2000_DEG` is used only as the angle that defines
  the ecliptic frame. An exact row no display prints carries no print
  count, as the second part above says.
""",
))

V369 = b"""v3.69 (September 25, 2026): No rule changed in this document. ONE
skill bump, taken ahead of the build that will next read the rule it
touches.

provenance-discipline 2.18 -> 2.19 (L-322). A WORKED EXAMPLE THAT HAD
GONE STALE IS REPLACED.

WHAT WAS WRONG. Rule 7's exact row gave Earth's obliquity as its
example: it "prints 23.439291 degrees". That was written on the
morning of 2026-09-23. Later that day the Stage D manifest's revision 3
changed the axis hover to print the tilt of date, worked out from the
pole Horizons serves, and D6 and D7 built it. Since then no display
prints the obliquity; its row is only the angle that defines the
ecliptic frame. The example described a hover that no longer exists.

HOW IT WAS FOUND. Two handoffs carried it as a ledger class, the
second without re-checking it. Tony asked what "stale" meant, and then
two questions: were the consumers of the obliquity using a correct
number, and should the skill change now so it is not forgotten. The
consumers were checked in the orrery, in the export and in the
gallery's served cache: all carry 23.439291111 degrees, and all use it
to turn equatorial directions into Horizons' ecliptic frame, never as
Earth's tilt and never printed. Nothing on screen was wrong.

THE NEW EXAMPLE is the gallery's magnetopause hover, which prints the
exact row EARTH_MAGNETOPAUSE_CUT_ANGLE_DEG today with a width chosen at
its call site, the thing the rule forbids. The obliquity stays in the
text as the case of an exact row no display prints, which carries no
print count.

WHY NOW. Tony: update it now so it is not forgotten. The next two
Stage D sessions both reach this rule: gallery patch 3 edits the Earth
room's hovers, where the cut angle is printed, and manifest section 6
builds the print-count field itself. A stale example in a skill that
loads every session is followed without being noticed.

THE OBLIGATION TRAVELS, as it always does. This session loaded 2.18,
and a reinstall cannot be verified from inside the session that makes
it. The next session confirms its loaded copy reads 2.19 before any
provenance or constants_new.py work, and that session is gallery patch
3, from documentation/HANDOFF_L322_D_orrery_magnetosphere_built_20260925.md.

The header stamp and the SHA anchor move with this entry.

Version history: v3.66 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

"""

V366_START = b"v3.66 (September 21, 2026): No rule changed in this document. ONE\n"
V366_END_MARK = b"Version history: v3.63 moves down to\ndocumentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three\nresident.\n\n"

HIST_ANCHOR = b"""(Moved down from the resident protocol on 2026-09-23 when
v3.68 made a fourth entry.)
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

    # Protocol: header stamp, anchor, the new entry, and v3.66 cut out.
    proto = apply_edits(PROTO, proto, [
        ('stamp: header version and date',
         b"Tony Quintanilla, PE | Claude | v3.68 | September 23, 2026",
         b"Tony Quintanilla, PE | Claude | v3.69 | September 25, 2026"),
        ('stamp: SHA anchor',
         b"Cut from ac25d4f4 at https://github.com/tonylquintanilla/palomas_orrery",
         b"Cut from de4eadc5 at https://github.com/tonylquintanilla/palomas_orrery"),
        ('history: v3.69 entry',
         b"v3.68 (September 23, 2026): No rule changed in this document. ONE\n",
         V369 + b"v3.68 (September 23, 2026): No rule changed in this document. ONE\n"),
    ])
    start, end_mark = convention(proto, V366_START, V366_END_MARK)
    if proto.count(start) != 1 or proto.count(end_mark) != 1:
        fail('ANCHOR FAIL: %s: v3.66 entry boundaries not found exactly once'
             % PROTO)
    i = proto.index(start)
    j = proto.index(end_mark) + len(end_mark)
    if j <= i:
        fail('ANCHOR FAIL: %s: v3.66 entry ends before it starts' % PROTO)
    v366 = proto[i:j]
    proto = proto[:i] + proto[j:]
    print('ok    %s: v3.66 entry cut (%d bytes)' % (PROTO, len(v366)))

    # History: v3.66 lands after v3.65, with its own moved-down note.
    note = (b"(Moved down from the resident protocol on 2026-09-25 when\n"
            b"v3.69 made a fourth entry.)\n")
    anchor, _ = convention(hist, HIST_ANCHOR, b"")
    if hist.count(anchor) != 1:
        fail('ANCHOR FAIL: %s: the v3.65 moved-down note not found exactly '
             'once' % HIST)
    if hist.count(b'\r\n') > 0:
        note = note.replace(b'\n', b'\r\n')
        sep = b'\r\n'
    else:
        sep = b'\n'
    hist = hist.replace(anchor, anchor + sep + v366.rstrip(b'\r\n') + sep
                        + sep + note)
    print('ok    %s: v3.66 entry added to PART 1' % HIST)

    for path, data in ((SKILL, skill), (PROTO, proto), (HIST, hist)):
        ascii_check(path, data)

    for path, data in ((SKILL, skill), (PROTO, proto), (HIST, hist)):
        with open(path, 'wb') as f:
            f.write(data)

    print('stamp %s: Skill version 2.19, cut from de4eadc5, 2026-09-25'
          % SKILL)
    print('stamp %s: v3.69, cut from de4eadc5, 2026-09-25' % PROTO)
    print('stamp %s: v3.66 moved down, dated 2026-09-25' % HIST)
    print('patch applied: %s, %s, %s' % (SKILL, PROTO, HIST))
    print('Next: run the orrery maintenance run (its Skill manifest step is '
          'skills_index.py), then commit all of it together.')


if __name__ == '__main__':
    main()
