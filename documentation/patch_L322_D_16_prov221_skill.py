"""
patch_L322_D_16_prov221_skill.py -- ORRERY repo.

provenance-discipline 2.20 -> 2.21, and the protocol entry that
records it (v3.70 -> v3.71). Three files, one commit:

  skills/provenance-discipline/SKILL.md
  PROJECT_INSTRUCTIONS.md
  documentation/PROJECT_INSTRUCTIONS_HISTORY.md

Built on 95b394f821891e4e704fc5d65bcc54ec556ed136
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Written 2026-09-28 with Anthropic's Claude Opus 5.5, Tony Quintanilla
integrator. REPLACES patch_L322_provenance_2_21_scaling.py: it carries
Claude Fable 5.1's eight edits to the skill unchanged, except for one
added sentence (in the Rule 3 paragraph and its changelog) saying the
rule reaches sums and differences only, and a single measured value
scaled by an exact row stays under fewest figures for now. It also
writes the v3.71 protocol entry and moves v3.68 down to the history
file, which Fable's patch left to be done by hand.

WHAT THE SKILL CHANGE SAYS: a sum or difference scaled by an exact row
keeps its decimal place, carried through the scaling, not its figure
count. The Sun room's chromosphere prints 1.003 solar radii, not 1.00.

RUN: save in the ORRERY REPO ROOT, open in VS Code, click Run. It
refuses to run from documentation/.

SUCCESS: one "ok" line per edit, then "patch applied".
FAILURE: one ERROR: or ANCHOR FAIL: line, and NOTHING is written; all
three files are checked before any is written. Undo after a success is
Discard Changes in GitHub Desktop.

AFTERWARD
  1. (do) Run the orrery maintenance run. Its Skill manifest step,
     skills_index.py, moves the manifest table from 2.20 to 2.21.
  2. (do) Commit the three files and the manifest change together,
     and push.
  3. (do) Reinstall provenance-discipline (Settings > Skills).
  4. (do) Move this script into documentation/. Fable's
     patch_L322_provenance_2_21_scaling.py is not run; keep it beside
     this one as the record of the recommendation, or delete it.

  The rows and the checker the new rule needs are the next patch, D17.
"""

import hashlib
import os
import sys

SKILL = os.path.join('skills', 'provenance-discipline', 'SKILL.md')
PROTO = 'PROJECT_INSTRUCTIONS.md'
HIST = os.path.join('documentation', 'PROJECT_INSTRUCTIONS_HISTORY.md')

FINGERPRINTS = {
    SKILL: '1fec45d123eef52f185559b0a4afc3d8',
    PROTO: '089a0a6fc3e0f13ece4de8c048357c6e',
    HIST: 'a9509003d577f1d6029d91bf5ff0ddf5',
}

# Claude Fable 5.1's eight edits, with the one scope sentence added.
SKILL_EDITS = [('version line 2.20 -> 2.21', b'Skill version: 2.20 | Cut from palomas_orrery @ 0e3d05fd (v2.20),\nearlier @ de4eadc5 (v2.19), @ ac25d4f4 (v2.18),', b'Skill version: 2.21 | Cut from palomas_orrery @ 95b394f8 (v2.21),\nearlier @ 0e3d05fd (v2.20), @ de4eadc5 (v2.19), @ ac25d4f4 (v2.18),'), ('date line and v2.21 changelog', b'| September 27, 2026\nv2.20 writes down where a trailing ".0" comes from, in Rule 2.', b'| September 28, 2026\nv2.21 adds one paragraph to Rule 3: a value good to a decimal place,\nscaled by an exact row, keeps its place and not its figure count. A\nsum good to thousands of kilometres divided by the nominal solar\nradius is good to thousandths of a solar radius; counted by fewest\nfigures it would keep three, and three figures of 1.003 is a factor\nof seven coarser than three figures of 698,000, because the leading\ndigit went from 6 to 1. The reference page names the case as its\nunit-conversion exception (8 inches converts to 20. cm, not 20 cm).\nIt reaches sums and differences only; a single measured value scaled\nby an exact row stays under fewest figures for now.\nRule 1 gains the seventh form that carries it; the ceiling\'s\nimplied-uncertainty bullet says a converted place is not that; the\nReport bullet cross-links; Rule 8 says how the checker finds the\nplace and prints it. The worked case is the top of the chromosphere,\nwhich prints 1.003 and not 1.00: at 1.00 the export, which rounds to\nthe count, would have drawn it on the photosphere and erased the\n2,000 km hairline promoted on 2026-08-16. Before this the two forms\nof the same expression counted differently, 1.00 sum-first and 1.003\ndivide-first, and the unit check forced the coarser. Tony\'s ruling,\n2026-09-28, on Claude Fable 5.1\'s recommendation, checked against\nthe reference page the same day. Handle L-322.\nv2.20 writes down where a trailing ".0" comes from, in Rule 2.'), ('Rule 1: Six forms -> Seven forms', b'**Rule 1. `# Figures:` is a comment key beside the value.** Six forms:', b'**Rule 1. `# Figures:` is a comment key beside the value.** Seven forms:'), ('Rule 1: seventh form line', b"# Figures: 3 -- uncertainty 0.13, root-sum-square of Shue's a1 to a5\n```\n\nA derived row names the input that set its count.", b"# Figures: 3 -- uncertainty 0.13, root-sum-square of Shue's a1 to a5\n# Figures: 4 -- thousandths: thousands place of the sum, set by CHROMOSPHERE_PHYSICAL_KM (2000, 1), carried through the exact SUN_RADIUS_KM\n```\n\nA derived row names the input that set its count. A place-governed\nrow scaled by an exact row names the place it keeps, the input that\nset the place, and the exact row it was scaled by (Rule 3, scaling)."), ('Rule 3: scaling paragraph', b'decides instead and counting is the fallback; how is set out under The\nceiling, below.\n\n**A row may declare FEWER figures than its inputs support when the\n', b'decides instead and counting is the fallback; how is set out under The\nceiling, below.\n\n**A place-governed value scaled by an exact row keeps its place, not\nits count** (v2.21). A sum or difference is good to a decimal place\n(above). Multiplying or dividing it by an exact row -- a unit\nconversion, a nominal radius -- moves that place with the value, and\nthe row keeps the place the scaling gives: a sum good to thousands of\nkilometres, divided by 695,700 km per solar radius, is good to\nthousandths of a solar radius, because 1,000 km is 0.0014 solar\nradii. Counting the quotient by fewest figures instead keeps three on\neither side of the division, and three figures of 698,000 is\n+/- 500 km while three figures of 1.003 is +/- 3,500 km: the leading\ndigit went from 6 to 1 and the count lost a factor of seven. The\nreference page names this case. Its arithmetic guidelines do not\nensure the result\'s implied uncertainty is close to the measured one,\nit says the problem shows up in unit conversion, and its example is\n8 inches (+/- 0.5 in) converted by the guideline to 20 cm (+/- 5 cm)\nwhen the proper result is 20. cm (+/- 0.5 cm). The place kept is the\npower of ten nearest, on a log scale, to the sum\'s place unit carried\nthrough the scaling, a tie going to the coarser -- the same measure\nthe Report bullet under The ceiling uses: 1,000 km / 695,700 km is\n0.0014, nearer 0.001 than 0.01, so thousandths. The row states the\nplace it keeps, the input that set the sum\'s place, and the exact row\nit was scaled by (Rule 1, seventh form). The two forms of one\nexpression now count the same: 1 + 2000 / 695700 and\n(695700 + 2000) / 695700 both keep thousandths, so whichever form the\nunit check accepts, the count is 4. This is not an implied\nuncertainty raising a count; it is the sum\'s own place, converted,\nand it reaches nothing but a sum or difference scaled by exact rows.\nA product or quotient of measured quantities keeps fewest figures as\nbefore, and Jelinek\'s bow shock stays 13.5. Here a place-governed\nvalue means a sum or a difference. A single measured value scaled by\nan exact row, which is what the reference page\'s 8-inch example is,\nis deliberately left under the fewest-figures rule for now.\n\nThe top of the chromosphere is the worked case. `SUN_RADIUS_KM +\nCHROMOSPHERE_PHYSICAL_KM` is good to thousands, set by the depth\nCarroll & Ostlie give as about 2,000 km (one figure), so 698,000 km at\nthree figures; divided by the exact `SUN_RADIUS_KM` it keeps\nthousandths, 1.003 at four figures -- one more figure than the\nkilometre line, and the figure the drawing needs. The export rounds\nto the count (Rule 6): at three figures the served value is 1.00,\nwhich draws the chromosphere on the photosphere and erases the\n2,000 km hairline promoted on 2026-08-16; at 1.003 it draws 2,087 km\nabove the photosphere, inside the source\'s "about". The hover still\nsays about 2,000 km deep, and the radius line no longer contradicts\nit with an implied +/- 3,500 km. Before this paragraph the rule as\nwritten gave 1.00 by the sum-first form and 1.003 by the divide-first\nform, and the unit check forced the first. (Tony\'s ruling,\n2026-09-28, confirming Claude Fable 5.1\'s recommendation, checked\nagainst the reference page the same day. Handle L-322.)\n\n**A row may declare FEWER figures than its inputs support when the\n'), ('ceiling: converted place is not an implied uncertainty', b"  Jelinek's bow shock standoff, whose chain states none, is 13.5 by\n  counting and would be 13.51 if they did.\n", b"  Jelinek's bow shock standoff, whose chain states none, is 13.5 by\n  counting and would be 13.51 if they did. A place carried through an\n  exact scaling is not this: it is the sum's own place, converted\n  (Rule 3, scaling).\n"), ('ceiling: Report bullet cross-link', b'  own uncertainty, so a value and its conversion can carry different\n  counts; the page warns of exactly this for unit conversions.\n', b"  own uncertainty, so a value and its conversion can carry different\n  counts; the page warns of exactly this for unit conversions, and on\n  the counting route the same exception is Rule 3's scaling\n  paragraph.\n"), ('Rule 8: checker applies the scaling paragraph', b"and names any primary whose figures line mentions an uncertainty in\nwords without the field, so the blind spot announces.\n\n(Tony's rulings, 2026-09-16, adopting the procedure in\n", b"and names any primary whose figures line mentions an uncertainty in\nwords without the field, so the blind spot announces.\n\n**The checker also applies Rule 3's scaling paragraph** (v2.21,\nspecified here and built with the chromosphere row). For a derived\nrow whose expression is a sum or difference of rows scaled only by\nexact rows, the ceiling by counting is not the fewest figures among\nthe inputs but the place: the coarsest last place among the sum's\nmeasured inputs, carried through the exact factors, snapped to the\nnearest power of ten on the log scale with a tie to the coarser; the\ncount is the figures of the computed value down to that place. It\nprints the place it found beside the count, so a wrong ceiling is\nvisible and not only a pass. Until it is built the chromosphere row\nfails the counting check at four figures; the build that adds the\nrow adds the check.\n\n(Tony's rulings, 2026-09-16, adopting the procedure in\n")]

V371 = b"v3.71 (September 28, 2026): No rule changed in this document. ONE\nskill bump, provenance-discipline 2.20 -> 2.21 (L-322). A SUM SCALED\nBY AN EXACT NUMBER KEEPS ITS DECIMAL PLACE.\n\nWHAT PROMPTED IT. Settling the Sun room's chromosphere hover, which\nprinted its radius as 1.002874802357338 solar radii. The top of the\nchromosphere is the Sun's radius, 695,700 km, exact by the IAU's\ndefinition, plus a depth Carroll & Ostlie give as about 2,000 km, one\nfigure. The sum is good to thousands of kilometres, 698,000 km. Divided\nby the exact solar radius, the counting rule as written gave 1.00:\nthree figures, an implied error of about 3,500 km on a 2,000 km layer.\nWritten the other way, 1 + 2,000 / 695,700, the same rule gave 1.003,\nand the unit check forced the coarser form. And the export rounds each\nrow to its count, so at 1.00 the chromosphere would have been drawn on\nthe photosphere, erasing the 2,000 km hairline ruled on 2026-08-16.\n\nWHAT THE SKILL NOW SAYS. Rule 3 gains one paragraph: a sum or\ndifference, scaled by an exact row, keeps its decimal place carried\nthrough the scaling, not its figure count. 1,000 km is 0.0014 solar\nradii, nearest the thousandths, so the chromosphere prints 1.003. The\nreference page, Wikipedia's Significant figures, names this as the\nunit-conversion exception to its multiplication guideline: 8 inches\nbecomes 20. cm, not 20 cm. A single measured value scaled by an exact\nrow is deliberately left under the fewest-figures rule for now. Rule 1\ngains the form that carries it, the ceiling says a converted place is\nnot an implied uncertainty, and Rule 8 specifies the checker, which is\nbuilt with the chromosphere rows.\n\nWHO DECIDED. Claude Fable 5.1 recommended the rule; Tony ruled for it\non 2026-09-28. Claude Opus 5.5 checked the reference and the numbers\nthe same day and added the scope sentence, which Tony confirmed.\n\nTHE OBLIGATION TRAVELS. This bump was written in Fable's session and\nlands from this one, which had already shipped 2.20. The next session\nconfirms its loaded copy reads 2.21 before any provenance or\nconstants_new.py work.\n\nThe header stamp and the SHA anchor move with this entry.\n\nVersion history: v3.68 moves down to\ndocumentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three\nresident.\n\n"

V368_START = b"v3.68 (September 23, 2026): No rule changed in this document. ONE\n"
V368_END_MARK = (b"Version history: v3.65 moves down to\n"
                 b"documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three\n"
                 b"resident.\n\n")
HIST_ANCHOR = (b"(Moved down from the resident protocol on 2026-09-27 when\n"
               b"v3.70 made a fourth entry.)\n")


def fingerprint(data):
    """md5 of the content, CRLF normalised, with the protocol's Skill
    Manifest zone left out, since skills_index.py rewrites it."""
    lf = data.replace(b'\r\n', b'\n')
    start = b'<!-- SKILL-MANIFEST:START'
    end = b'<!-- SKILL-MANIFEST:END -->'
    if start in lf and end in lf:
        lf = lf[:lf.index(start)] + lf[lf.index(end) + len(end):]
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
    if b'\r\n' in data:
        fail('ERROR: %s has CRLF line endings; this patch expects LF.' % path)
    fp = fingerprint(data)
    if fp != FINGERPRINTS[path]:
        fail('ERROR: %s is not the file this patch was built on '
             '(fingerprint %s, expected %s). Pull or discard local changes '
             'first; if Fable\'s 2.21 patch was run, Discard Changes on it.'
             % (path, fp, FINGERPRINTS[path]))
    return data


def edit(path, data, label, old, new):
    n = data.count(old)
    if n != 1:
        fail('ANCHOR FAIL: %s: "%s" -- expected 1 match, got %d'
             % (path, label, n))
    print('ok    %s: %s' % (path, label))
    return data.replace(old, new)


def main():
    if os.path.basename(os.getcwd()) == 'documentation':
        fail('ERROR: this is running from documentation/. Run it from the '
             'orrery repo root, then file it in documentation/.')
    skill, proto, hist = load(SKILL), load(PROTO), load(HIST)
    for label, old, new in SKILL_EDITS:
        skill = edit(SKILL, skill, label, old, new)
    proto = edit(PROTO, proto, 'stamp: header version and date',
                 b'Tony Quintanilla, PE | Claude | v3.70 | September 27, 2026',
                 b'Tony Quintanilla, PE | Claude | v3.71 | September 28, 2026')
    proto = edit(PROTO, proto, 'stamp: SHA anchor',
                 b'Cut from 0e3d05fd at https://github.com/tonylquintanilla/palomas_orrery',
                 b'Cut from 95b394f8 at https://github.com/tonylquintanilla/palomas_orrery')
    proto = edit(PROTO, proto, 'history: v3.71 entry',
                 b'v3.70 (September 27, 2026): No rule changed in this document. ONE\n',
                 V371 + b'v3.70 (September 27, 2026): No rule changed in this document. ONE\n')
    if proto.count(V368_START) != 1 or proto.count(V368_END_MARK) != 1:
        fail('ANCHOR FAIL: %s: v3.68 entry boundaries not found exactly once'
             % PROTO)
    i = proto.index(V368_START)
    j = proto.index(V368_END_MARK) + len(V368_END_MARK)
    if j <= i:
        fail('ANCHOR FAIL: %s: v3.68 entry ends before it starts' % PROTO)
    v368 = proto[i:j]
    proto = proto[:i] + proto[j:]
    print('ok    %s: v3.68 entry cut (%d bytes)' % (PROTO, len(v368)))
    note = (b'(Moved down from the resident protocol on 2026-09-28 when\n'
            b'v3.71 made a fourth entry.)\n')
    hist = edit(HIST, hist, 'v3.68 entry added to PART 1', HIST_ANCHOR,
                HIST_ANCHOR + b'\n' + v368.rstrip(b'\n') + b'\n\n' + note)
    for path, data in ((SKILL, skill), (PROTO, proto), (HIST, hist)):
        try:
            data.decode('ascii')
        except UnicodeDecodeError as exc:
            fail('ERROR: %s would not be ASCII after the patch (%s).'
                 % (path, exc))
    for path, data in ((SKILL, skill), (PROTO, proto), (HIST, hist)):
        with open(path, 'wb') as f:
            f.write(data)
    print('stamp %s: Skill version 2.21, cut from 95b394f8' % SKILL)
    print('stamp %s: v3.71, cut from 95b394f8, 2026-09-28' % PROTO)
    print('patch applied: %s, %s, %s' % (SKILL, PROTO, HIST))
    print('Next: run the orrery maintenance run, then commit all of it '
          'together, and reinstall provenance-discipline.')


if __name__ == '__main__':
    main()
