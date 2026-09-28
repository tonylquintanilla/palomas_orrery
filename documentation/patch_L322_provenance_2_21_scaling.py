"""
patch_L322_provenance_2_21_scaling.py -- provenance-discipline SKILL.md
2.20 -> 2.21

WHAT CHANGES, in one sentence: a sum that is good to a decimal place,
scaled by an exact number, keeps its place and not its figure count.

The case that earned it is the top of the chromosphere. The sum
695,700 + 2,000 km is good to thousands of kilometres (three figures,
698,000). Divided by the exact solar radius it was being counted at
three figures too, which prints 1.00 -- an implied error of 3,500 km on
a 2,000 km layer -- and, because the export rounds to the count, draws
the chromosphere on the photosphere. Kept by place it is good to
thousandths of a solar radius, 1.003, four figures. The reference page
the skill works from names exactly this case as its unit-conversion
exception (8 inches to "20. cm", not "20 cm"). Tony's ruling,
2026-09-28.

Eight anchored edits, all-or-nothing. Nothing is written unless every
anchor matches exactly once.

  1. version line 2.20 -> 2.21, SHA lineage rolled forward
  2. date line and the v2.21 changelog paragraph
  3. Rule 1: "Six forms" -> "Seven forms"
  4. Rule 1: the seventh form line, and the sentence naming what it
     carries
  5. Rule 3: the scaling paragraph and the chromosphere worked case
  6. The ceiling, implied-uncertainty bullet: the converted place is
     not an implied uncertainty
  7. The ceiling, Report bullet: cross-link to the scaling paragraph
  8. Rule 8: how the checker finds the place, and prints it

TARGET: skills/provenance-discipline/SKILL.md (path resolved relative
to this script, so save this file at the REPO ROOT, the folder that
contains skills/).

Built on 95b394f821891e4e704fc5d65bcc54ec556ed136 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
The target file at that SHA is byte-identical to the installed 2.20
(checked 2026-09-28).

RUN: save at the repo root, open in VS Code, click Run.
     Equivalent command line: python patch_L322_provenance_2_21_scaling.py

SUCCESS: one "ok" line per edit, then "patch applied (N bytes)".
FAILURE: a single "ERROR:" or "ANCHOR FAIL" line. Nothing is written
         either way, so it is always safe to re-check and retry.
         Undo, if ever needed, is Discard Changes in GitHub Desktop.

AFTER RUNNING -- THREE STORES, AND THIS MOVES ONE
  A skill lives in the repo, in your account install, and in the
  protocol's manifest table. This patch edits the repo copy only.
    1. Run skills_index.py. It rewrites the manifest table in
       PROJECT_INSTRUCTIONS.md and prints the 2.20 -> 2.21 move.
    2. Reinstall provenance-discipline to your account
       (Settings > Skills).
    3. Add the v3.71 entry to PROJECT_INSTRUCTIONS.md's version
       history (no rule changed; one skill bump), and move v3.68 down
       to PROJECT_INSTRUCTIONS_HISTORY.md to keep three resident.
  The reinstall cannot be verified from inside the session that makes
  it. The next session confirms its loaded copy reads 2.21 before any
  provenance or constants_new.py work.

NEXT, IN THE BUILD SESSION (not done by this script)
  Three rows in constants_new.py, run through both checkers on a
  throwaway copy before they land. The checker change in Rule 8 lands
  in the same build, since the row fails the counting check without it.

    SUN_RADIUS_KM = 695700.0
    # Figures: exact -- IAU 2015 nominal, a conversion constant

    CHROMOSPHERE_PHYSICAL_KM = 2000.0
    # Figures: 1 -- Carroll & Ostlie give "about 2,000 km"; the zeros
    # Figures+: are placeholders

    CHROMOSPHERE_PHYSICAL_RADII = (SUN_RADIUS_KM + CHROMOSPHERE_PHYSICAL_KM) / SUN_RADIUS_KM
    # Figures: 4 -- thousandths: thousands place of the sum, set by
    # Figures+: CHROMOSPHERE_PHYSICAL_KM (2000, 1), carried through the
    # Figures+: exact SUN_RADIUS_KM (Rule 3, scaling)
    # Derived: (695700 + 2000) / 695700 = 1.003

  Whether the second and third lines above may continue on a
  "# Figures+:" line is for the checker to say; if it reads only the
  first line, the field goes on one line. The sum form is the one the
  unit check accepted on 2026-09-27; under 2.21 the divide-first form
  counts the same, so either form the unit check accepts gives 1.003.
  If the hover prints a kilometre line, it needs its own row for the
  sum (three figures, 698,000 km); a print of 1.003 R_sun does not.
"""

import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TARGET = os.path.join(HERE, 'skills', 'provenance-discipline', 'SKILL.md')
BASE_MD5 = '1fec45d123eef52f185559b0a4afc3d8'   # SKILL.md at 95b394f8

EDITS = []

# 1. version line -------------------------------------------------------
EDITS.append((
    'version line 2.20 -> 2.21',
    b"Skill version: 2.20 | Cut from palomas_orrery @ 0e3d05fd (v2.20),\n"
    b"earlier @ de4eadc5 (v2.19), @ ac25d4f4 (v2.18),",
    b"Skill version: 2.21 | Cut from palomas_orrery @ 95b394f8 (v2.21),\n"
    b"earlier @ 0e3d05fd (v2.20), @ de4eadc5 (v2.19), @ ac25d4f4 (v2.18),",
))

# 2. date line + changelog ----------------------------------------------
EDITS.append((
    'date line and v2.21 changelog',
    b"| September 27, 2026\n"
    b"v2.20 writes down where a trailing \".0\" comes from, in Rule 2.",
    b"| September 28, 2026\n"
    b"v2.21 adds one paragraph to Rule 3: a value good to a decimal place,\n"
    b"scaled by an exact row, keeps its place and not its figure count. A\n"
    b"sum good to thousands of kilometres divided by the nominal solar\n"
    b"radius is good to thousandths of a solar radius; counted by fewest\n"
    b"figures it would keep three, and three figures of 1.003 is a factor\n"
    b"of seven coarser than three figures of 698,000, because the leading\n"
    b"digit went from 6 to 1. The reference page names the case as its\n"
    b"unit-conversion exception (8 inches converts to 20. cm, not 20 cm).\n"
    b"Rule 1 gains the seventh form that carries it; the ceiling's\n"
    b"implied-uncertainty bullet says a converted place is not that; the\n"
    b"Report bullet cross-links; Rule 8 says how the checker finds the\n"
    b"place and prints it. The worked case is the top of the chromosphere,\n"
    b"which prints 1.003 and not 1.00: at 1.00 the export, which rounds to\n"
    b"the count, would have drawn it on the photosphere and erased the\n"
    b"2,000 km hairline promoted on 2026-08-16. Before this the two forms\n"
    b"of the same expression counted differently, 1.00 sum-first and 1.003\n"
    b"divide-first, and the unit check forced the coarser. Tony's ruling,\n"
    b"2026-09-28, on Claude Fable 5.1's recommendation, checked against\n"
    b"the reference page the same day. Handle L-322.\n"
    b"v2.20 writes down where a trailing \".0\" comes from, in Rule 2.",
))

# 3. Rule 1: seventh form -----------------------------------------------
EDITS.append((
    'Rule 1: Six forms -> Seven forms',
    b"**Rule 1. `# Figures:` is a comment key beside the value.** Six forms:",
    b"**Rule 1. `# Figures:` is a comment key beside the value.** Seven forms:",
))
EDITS.append((
    'Rule 1: seventh form line',
    b"# Figures: 3 -- uncertainty 0.13, root-sum-square of Shue's a1 to a5\n"
    b"```\n\n"
    b"A derived row names the input that set its count.",
    b"# Figures: 3 -- uncertainty 0.13, root-sum-square of Shue's a1 to a5\n"
    b"# Figures: 4 -- thousandths: thousands place of the sum, set by CHROMOSPHERE_PHYSICAL_KM (2000, 1), carried through the exact SUN_RADIUS_KM\n"
    b"```\n\n"
    b"A derived row names the input that set its count. A place-governed\n"
    b"row scaled by an exact row names the place it keeps, the input that\n"
    b"set the place, and the exact row it was scaled by (Rule 3, scaling).",
))

# 4. Rule 3: scaling paragraph + chromosphere case ----------------------
EDITS.append((
    'Rule 3: scaling paragraph',
    b"decides instead and counting is the fallback; how is set out under The\n"
    b"ceiling, below.\n\n"
    b"**A row may declare FEWER figures than its inputs support when the\n",
    b"decides instead and counting is the fallback; how is set out under The\n"
    b"ceiling, below.\n\n"
    b"**A place-governed value scaled by an exact row keeps its place, not\n"
    b"its count** (v2.21). A sum or difference is good to a decimal place\n"
    b"(above). Multiplying or dividing it by an exact row -- a unit\n"
    b"conversion, a nominal radius -- moves that place with the value, and\n"
    b"the row keeps the place the scaling gives: a sum good to thousands of\n"
    b"kilometres, divided by 695,700 km per solar radius, is good to\n"
    b"thousandths of a solar radius, because 1,000 km is 0.0014 solar\n"
    b"radii. Counting the quotient by fewest figures instead keeps three on\n"
    b"either side of the division, and three figures of 698,000 is\n"
    b"+/- 500 km while three figures of 1.003 is +/- 3,500 km: the leading\n"
    b"digit went from 6 to 1 and the count lost a factor of seven. The\n"
    b"reference page names this case. Its arithmetic guidelines do not\n"
    b"ensure the result's implied uncertainty is close to the measured one,\n"
    b"it says the problem shows up in unit conversion, and its example is\n"
    b"8 inches (+/- 0.5 in) converted by the guideline to 20 cm (+/- 5 cm)\n"
    b"when the proper result is 20. cm (+/- 0.5 cm). The place kept is the\n"
    b"power of ten nearest, on a log scale, to the sum's place unit carried\n"
    b"through the scaling, a tie going to the coarser -- the same measure\n"
    b"the Report bullet under The ceiling uses: 1,000 km / 695,700 km is\n"
    b"0.0014, nearer 0.001 than 0.01, so thousandths. The row states the\n"
    b"place it keeps, the input that set the sum's place, and the exact row\n"
    b"it was scaled by (Rule 1, seventh form). The two forms of one\n"
    b"expression now count the same: 1 + 2000 / 695700 and\n"
    b"(695700 + 2000) / 695700 both keep thousandths, so whichever form the\n"
    b"unit check accepts, the count is 4. This is not an implied\n"
    b"uncertainty raising a count; it is the sum's own place, converted,\n"
    b"and it reaches nothing but a sum or difference scaled by exact rows.\n"
    b"A product or quotient of measured quantities keeps fewest figures as\n"
    b"before, and Jelinek's bow shock stays 13.5.\n\n"
    b"The top of the chromosphere is the worked case. `SUN_RADIUS_KM +\n"
    b"CHROMOSPHERE_PHYSICAL_KM` is good to thousands, set by the depth\n"
    b"Carroll & Ostlie give as about 2,000 km (one figure), so 698,000 km at\n"
    b"three figures; divided by the exact `SUN_RADIUS_KM` it keeps\n"
    b"thousandths, 1.003 at four figures -- one more figure than the\n"
    b"kilometre line, and the figure the drawing needs. The export rounds\n"
    b"to the count (Rule 6): at three figures the served value is 1.00,\n"
    b"which draws the chromosphere on the photosphere and erases the\n"
    b"2,000 km hairline promoted on 2026-08-16; at 1.003 it draws 2,087 km\n"
    b"above the photosphere, inside the source's \"about\". The hover still\n"
    b"says about 2,000 km deep, and the radius line no longer contradicts\n"
    b"it with an implied +/- 3,500 km. Before this paragraph the rule as\n"
    b"written gave 1.00 by the sum-first form and 1.003 by the divide-first\n"
    b"form, and the unit check forced the first. (Tony's ruling,\n"
    b"2026-09-28, confirming Claude Fable 5.1's recommendation, checked\n"
    b"against the reference page the same day. Handle L-322.)\n\n"
    b"**A row may declare FEWER figures than its inputs support when the\n",
))

# 5. The ceiling: implied-uncertainty bullet ----------------------------
EDITS.append((
    'ceiling: converted place is not an implied uncertainty',
    b"  Jelinek's bow shock standoff, whose chain states none, is 13.5 by\n"
    b"  counting and would be 13.51 if they did.\n",
    b"  Jelinek's bow shock standoff, whose chain states none, is 13.5 by\n"
    b"  counting and would be 13.51 if they did. A place carried through an\n"
    b"  exact scaling is not this: it is the sum's own place, converted\n"
    b"  (Rule 3, scaling).\n",
))

# 6. The ceiling: Report bullet cross-link ------------------------------
EDITS.append((
    'ceiling: Report bullet cross-link',
    b"  own uncertainty, so a value and its conversion can carry different\n"
    b"  counts; the page warns of exactly this for unit conversions.\n",
    b"  own uncertainty, so a value and its conversion can carry different\n"
    b"  counts; the page warns of exactly this for unit conversions, and on\n"
    b"  the counting route the same exception is Rule 3's scaling\n"
    b"  paragraph.\n",
))

# 7. Rule 8: the checker finds the place --------------------------------
EDITS.append((
    'Rule 8: checker applies the scaling paragraph',
    b"and names any primary whose figures line mentions an uncertainty in\n"
    b"words without the field, so the blind spot announces.\n\n"
    b"(Tony's rulings, 2026-09-16, adopting the procedure in\n",
    b"and names any primary whose figures line mentions an uncertainty in\n"
    b"words without the field, so the blind spot announces.\n\n"
    b"**The checker also applies Rule 3's scaling paragraph** (v2.21,\n"
    b"specified here and built with the chromosphere row). For a derived\n"
    b"row whose expression is a sum or difference of rows scaled only by\n"
    b"exact rows, the ceiling by counting is not the fewest figures among\n"
    b"the inputs but the place: the coarsest last place among the sum's\n"
    b"measured inputs, carried through the exact factors, snapped to the\n"
    b"nearest power of ten on the log scale with a tie to the coarser; the\n"
    b"count is the figures of the computed value down to that place. It\n"
    b"prints the place it found beside the count, so a wrong ceiling is\n"
    b"visible and not only a pass. Until it is built the chromosphere row\n"
    b"fails the counting check at four figures; the build that adds the\n"
    b"row adds the check.\n\n"
    b"(Tony's rulings, 2026-09-16, adopting the procedure in\n",
))


def main():
    if not os.path.isfile(TARGET):
        print('ERROR: target not found: %s' % TARGET)
        print('       Save this script at the repo root (the folder that '
              'contains skills/). NOTHING was written.')
        return 1
    with open(TARGET, 'rb') as f:
        content = f.read()
    md5 = hashlib.md5(content).hexdigest()
    if md5 != BASE_MD5:
        print('ERROR: SKILL.md fingerprint %s does not match the 2.20 base '
              '%s.' % (md5, BASE_MD5))
        print('       Either the file is not at 95b394f8 or the patch has '
              'already run. NOTHING was written.')
        return 1
    if b'\r\n' in content:
        print('ERROR: target has CRLF line endings; this patch expects LF. '
              'NOTHING was written.')
        return 1
    for label, old, new in EDITS:
        n = content.count(old)
        if n != 1:
            print('ANCHOR FAIL: %s -- expected 1 match, found %d. NOTHING '
                  'was written.' % (label, n))
            return 1
    for label, old, new in EDITS:
        content = content.replace(old, new)
        print('ok  %s' % label)
    try:
        content.decode('ascii')
    except UnicodeDecodeError as e:
        print('ERROR: result would contain non-ASCII at byte %d. NOTHING '
              'was written.' % e.start)
        return 1
    with open(TARGET, 'wb') as f:
        f.write(content)
    print('patch applied (%d bytes)' % len(content))
    print('next: python skills_index.py, then reinstall the skill '
          '(Settings > Skills), then the v3.71 entry.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
