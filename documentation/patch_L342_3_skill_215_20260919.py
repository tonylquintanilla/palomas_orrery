#!/usr/bin/env python3
"""
patch_L342_3_skill_215_20260919.py -- ORRERY repo.

Run: save this file in the ORRERY repo ROOT (next to
PROJECT_INSTRUCTIONS.md), open it in VS Code and click Run.  Or:
python patch_L342_3_skill_215_20260919.py

A patch is run from its repository's ROOT and filed in documentation/
AFTER it has run. This script refuses to run from documentation/.

Built on orrery 21065c5d95ecb22c79fa1f398644a30b73a9a5ed
at https://github.com/tonylquintanilla/palomas_orrery
(gallery 2ead992b055054956816ddda3544e849e9789d9a
at https://github.com/tonylquintanilla/tonyquintanilla.github.io)

RUN THIS BEFORE patch_L341_3_ledger_20260919.py, or tell Claude. Both
were cut against the same LEDGER_CONSOLIDATED.md and only one can go
first; whichever runs second will refuse on its fingerprint and needs
re-cutting. That refusal is the guard working, not damage.

ONE SKILL BUMP, provenance-discipline 2.14 -> 2.15, under the four
binding steps in ledger-and-session-records: the version line,
skills_index.py, a protocol version-history entry, and all of it in ONE
commit. L-342, confirmed by Tony on 2026-09-19.

WHAT IT DOES (four files, 12 anchored edits):

  skills/provenance-discipline/SKILL.md
      RULE 2 GAINS THE CONDITION IT HAD DROPPED. The cited page says a
      trailing zero after a decimal point is significant WHEN IT FALLS
      WITHIN THE SOURCE'S MEASUREMENT OR REPORTING RESOLUTION. v2.14
      said they count, full stop, which is wrong for the page's own
      example of 1500 m at 100 m resolution. The Earth walk, meeting
      PREM's 3480.0, invented the opposite rule and wrote it into one
      constant's comment. Both are replaced by what the page says.

      RULE 3 GAINS a sentence it never had: a row may declare FEWER
      figures than its inputs support when the RELATION is itself
      approximate, with the reason in words on the row. Earth's Hill
      sphere is the case.

      THE ASTM REFERENCE IS DEMOTED TO AN ASIDE. E29 costs $86, so a
      rule this project works from could not be opened by anybody in
      the loop -- which fails our own Access Standard -- and its scope
      is conformance with specification limits, which this store does
      not have. The reference is now the open page alone, so any rule
      below it can be checked by anybody. A new paragraph says that a
      stated condition is load-bearing and is not to be trimmed, which
      is the actual lesson: verbatim copying would not have prevented
      this, because what failed is that nobody could check the
      restatement against its source without opening the source.

      TWO STALE EXAMPLES corrected. Rule 1's "the trailing zero in 3480
      is significant" now shows the real row and its real count, and
      both copies of "6371.0 - 660 is good to units: 5711" now read
      tens and 5710, which is what C1 established from a sourced
      +/- 10 km.

  PROJECT_INSTRUCTIONS.md      stamp and anchor to v3.64 / 21065c5d;
                               the v3.64 entry added; v3.61 REMOVED,
                               because a fourth entry pushes the oldest
                               down and an entry lives in one place.
  documentation/PROJECT_INSTRUCTIONS_HISTORY.md
                               v3.61 lands at the end of PART 1.
  LEDGER_CONSOLIDATED.md       [L-342] opened in section A, recording
                               the live defect, why the check built is
                               not the check the review asked for, the
                               two figure corrections, the ASTM ruling,
                               and the disputed commit settled by the
                               commits themselves.

TWO GENERATED ZONES ARE EXCLUDED FROM THE FINGERPRINTS: the skill
manifest in PROJECT_INSTRUCTIONS.md and the INDEX zone in
LEDGER_CONSOLIDATED.md. This patch's own steps tell Tony to run both
tools, so guarding those zones would refuse for a reason that is not
about content.

SUCCESS looks like: one "ok" line per edit, then "patch applied".
FAILURE looks like: one ERROR: or ANCHOR FAIL: line, and NOTHING is
written to ANY of the four files.
Undo is Discard Changes in GitHub Desktop.
"""

import hashlib
import os
import sys

SKILL = "skills/provenance-discipline/SKILL.md"
PROTOCOL = "PROJECT_INSTRUCTIONS.md"
HISTORY = "documentation/PROJECT_INSTRUCTIONS_HISTORY.md"
LEDGER = "LEDGER_CONSOLIDATED.md"

BASE = {
    SKILL:    "119267d6f3af571b2a37d2a0628dd167",
    PROTOCOL: "2845f385024c7e7d22510f0268dce122",
    HISTORY:  "ccac98eb2c21a05e0afca1c931b89e6c",
    LEDGER:   "02c9f225e7c695433d0e16f5dcf1f9c4",
}

ZONES = {
    PROTOCOL: (b"<!-- SKILL-MANIFEST:START", b"<!-- SKILL-MANIFEST:END -->"),
    LEDGER:   (b"<!-- INDEX:START", b"<!-- INDEX:END -->"),
}


def fail(msg):
    print(msg)
    print("NOTHING was written to any file. Undo is Discard Changes in "
          "GitHub Desktop.")
    sys.exit(1)


def fingerprint(path, raw):
    lf = raw.replace(b"\r\n", b"\n")
    if path in ZONES:
        start, end = ZONES[path]
        try:
            a = lf.index(start)
            b = lf.index(end) + len(end)
        except ValueError:
            fail("ERROR: the generated-zone markers are missing from "
                 + path + ".")
        lf = lf[:a] + lf[b:]
    return hashlib.md5(lf).hexdigest()


EDITS = []

EDITS.append((SKILL, 'SKILL  version line 2.14 -> 2.15 with the v2.15 paragraph',
    b'Skill version: 2.14 | Cut from palomas_orrery @ dfa779bd (v2.14),\nearlier @ ebdc55cc (v2.13), @ bfc0505e (v2.12), @ 159c5a2c (v2.11),\nearlier @ 071a0a65 (v2.10), @ a263f73d (v2.9), @ 7f4a2f9f (v2.8),\n@ 3faa72a0 (v2.7), @ f603be3 (v2.6), @ 731066f (v2.5),\n@ 6b99ace (v2.2), @ 00219d9 (v2.1), @ eb77c83 (v2.0), @ cdcdb4b (v1.9)\n| September 19, 2026\n',
    b"Skill version: 2.15 | Cut from palomas_orrery @ 21065c5d (v2.15),\nearlier @ dfa779bd (v2.14), @ ebdc55cc (v2.13), @ bfc0505e (v2.12),\nearlier @ 159c5a2c (v2.11), @ 071a0a65 (v2.10), @ a263f73d (v2.9),\n@ 7f4a2f9f (v2.8), @ 3faa72a0 (v2.7), @ f603be3 (v2.6),\n@ 731066f (v2.5), @ 6b99ace (v2.2), @ 00219d9 (v2.1), @ eb77c83 (v2.0)\n| September 19, 2026\nv2.15 repairs the figure rules against the source they cite, after\nClaude Fable 5.1's review of L-322 Stage C1 found the walk deciding a\nrule inside one constant's comment. RULE 2 GAINS THE CONDITION IT HAD\nDROPPED: a trailing zero after a decimal point is significant when it\nfalls within the source's reporting resolution, which is what the cited\npage says and what makes 1500 m two figures rather than four. Without\nit the rule was simply wrong, and the walk's invented alternative --\nthat a padded zero never counts -- was wrong the other way. RULE 3\nGAINS a sentence it never had: a row may declare FEWER figures than its\ninputs support when the relation is itself approximate, with the reason\nin words on the row. Earth's Hill sphere is the case; it declared seven\nand told the reader to report three. THE ASTM REFERENCE IS DEMOTED TO\nAN ASIDE on Tony's ruling of 2026-09-19: E29 costs $86, so a rule this\nproject works from could not be opened by anybody in the loop, which\nfails our own Access Standard; and its scope is conformance with\nspecification limits, which the orrery does not have. Two stale\nexamples are corrected. Handle L-342.\n"))
EDITS.append((SKILL, 'SKILL  citation line: Wikipedia is the reference, ASTM an aside',
    b'These are the textbook rules (Wikipedia, Significant figures; ASTM\nE29), written down once so they resolve the same way for every row.\n',
    b"These are the textbook rules, written down once so they resolve the\nsame way for every row. The reference is **Wikipedia, Significant\nfigures**, which Tony named and which is open: every rule below can be\nchecked against it by anybody, which is the point. The same rules\nappear in ASTM E29, but that is an aside and NOT the reference we work\nfrom -- it costs $86, so a rule the project depends on could not be\nopened by any of us, which fails our own Access Standard; and its scope\nis conformance with specification limits, which this store has none of.\n(Tony's ruling, 2026-09-19, L-342.)\n\n**Where a rule below states a condition, the condition is load-bearing\nand is not to be trimmed.** v2.14's Rule 2 said trailing zeros after a\ndecimal point count, full stop. The page says they count WHEN THEY ARE\nWITHIN THE REPORTING RESOLUTION. Dropping four words made the rule\nwrong, and nobody could see it without opening the source -- which is\nthe argument for citing something openable rather than for copying a\nstandard verbatim.\n"))
EDITS.append((SKILL, 'SKILL  Rule 1 example corrected to the real row',
    b'# Figures: 4 -- source states 4; the trailing zero in 3480 is significant\n',
    b"# Figures: 5 -- PREM reports to 0.1 km, so 3480.0's trailing zero counts\n"))
EDITS.append((SKILL, 'SKILL  Rule 2 gains the reporting-resolution condition',
    b'**Rule 2. Counting a literal follows the standard rules.** Non-zero\ndigits count; zeros between them count; leading zeros never count;\nzeros after the decimal point at the end count; trailing zeros in an\ninteger count only if the source says so. An exact number has unlimited\nfigures.',
    b'**Rule 2. Counting a literal follows the standard rules.** Non-zero\ndigits count; zeros between them count; leading zeros never count;\ntrailing zeros in an integer count only if the source says so. An exact\nnumber has unlimited figures.\n\n**Trailing zeros after a decimal point count WHEN THEY FALL WITHIN THE\nSOURCE\'S MEASUREMENT OR REPORTING RESOLUTION**, and that condition is\nthe rule, not a refinement of it. 1500 m measured to a resolution of\n100 m has TWO figures, not four, and the page lists exactly that case\namong the digits which are not significant: trailing zeros serving as\nplaceholders. So the question to ask of a row is never "where does the\nlast digit fall" but "to what resolution does this source report". PREM\nTable I reports every boundary radius to 0.1 km, so `3480.0` carries\nfive. The NASA fact sheet prints `6371.000` in a block that also prints\n3485, 5513, 20.4 and 11.186, so it is not padding and the value carries\nseven.'))
EDITS.append((SKILL, 'SKILL  the 5711 example corrected, first place',
    b'`6371.0 - 660` is good to units, so 5711 and not 5711.0.\n',
    b'`6371.0 - 660` is good to TENS, because its 660 km input is good to\ntens, so 5710 and not 5711.\n'))
EDITS.append((SKILL, 'SKILL  the 5711 example corrected, second place',
    b'among the inputs (`6371.0 - 660` is good to units: 5711). Exact inputs',
    b'among the inputs (`6371.0 - 660` is good to tens: 5710, because its\n660 km input carries two figures). Exact inputs'))
EDITS.append((SKILL, 'SKILL  Rule 3 gains the approximate-relation sentence',
    b'decides instead and counting is the fallback.\n',
    b"decides instead and counting is the fallback.\n\n**A row may declare FEWER figures than its inputs support when the\nRELATION ITSELF is approximate, with the reason in words on the row.**\nCounting governs how precision flows through arithmetic; it says\nnothing about a formula that is an idealisation to begin with. Earth's\nHill sphere is the case: every input is exact or carries nine figures,\nso counting gives seven, but substituting Earth's perihelion distance\nfor its mean distance moves the answer by more than one percent. Seven\nfigures would claim a precision the relation cannot deliver whatever\nits inputs carry. This is a floor on honesty, not a licence to round to\ntaste: the row must say WHICH approximation caps it and by roughly how\nmuch. (L-342, Fable's review of C1, Finding 3.)\n"))
EDITS.append((PROTOCOL, 'PROTOCOL  header stamp and SHA anchor move to v3.64 / 21065c5d',
    b'Tony Quintanilla, PE | Claude | v3.63 | September 19, 2026\n\nCut from dfa779bd at https://github.com/tonylquintanilla/palomas_orrery\n',
    b'Tony Quintanilla, PE | Claude | v3.64 | September 19, 2026\n\nCut from 21065c5d at https://github.com/tonylquintanilla/palomas_orrery\n'))
EDITS.append((PROTOCOL, 'PROTOCOL  the v3.64 entry',
    b'v3.63 (September 19, 2026): No rule changed in this document. ONE\n',
    b"v3.64 (September 19, 2026): No rule changed in this document. ONE\nskill bump, taken after a review found a rule being decided in the\nwrong place.\n\nprovenance-discipline 2.14 -> 2.15 (L-342). THE FIGURE RULES ARE\nREPAIRED AGAINST THE SOURCE THEY CITE.\n\nWHAT WENT WRONG IS INSTRUCTIVE AND IS NOT A COUNTING ERROR. L-322's\nEarth walk met PREM's `3480.0` and had to decide whether that trailing\nzero counted. The skill's Rule 2 said it did, full stop. The walk\ndecided it did not, wrote a reason into that one constant's comment\nline -- that a zero in a padded decimal place is the table's formatting\n-- and moved on. Both were wrong, and the page the skill cites settles\nit: a trailing zero after a decimal point counts WHEN IT FALLS WITHIN\nTHE SOURCE'S REPORTING RESOLUTION. Rule 2 had dropped four words, which\nmade it wrong for the page's own example of 1500 m; the walk's\nreplacement was wrong the other way and, worse, was settled inside a\ncomment where it read as fact and would have been followed without\nbeing noticed. That is the second failure direction Method Belongs to\nthe Skill names, and this is what it looks like in practice.\n\nRULE 3 GAINS A SENTENCE IT NEVER HAD: a row may declare fewer figures\nthan its inputs support when the relation ITSELF is approximate, with\nthe reason in words on the row. Counting governs how precision flows\nthrough arithmetic and says nothing about a formula that is an\nidealisation to begin with. Earth's Hill sphere declared seven figures\nby counting and told the reader in its own next sentence to report\nthree, and the gallery, which formats from the declared count, showed a\nvisitor 234.6388 Earth radii.\n\nTHE ASTM REFERENCE IS DEMOTED TO AN ASIDE, on Tony's ruling. E29 costs\n$86, so a rule this project works from could not be opened by anybody\nin the loop -- the skill-layer form of a citation nobody read, and a\nfailure of our own Access Standard. Its scope is conformance with\nspecification limits, which this store does not have. The reference is\nnow the open page alone, so every rule can be checked against it by\nanybody. Asked whether to adopt the standard verbatim instead of\nrestating it, the answer is that verbatim would not have helped: what\nfailed was that nobody could check the restatement against its source\nwithout opening the source.\n\nTHE OBLIGATION TRAVELS, as it always does. This session loaded 2.14,\nand a reinstall cannot be verified from inside the session that makes\nit. The next session confirms its loaded copy reads 2.15 before any\nprovenance or store work.\n\nThe header stamp and the SHA anchor move with this entry.\n\nVersion history: v3.61 moves down to\ndocumentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three\nresident.\n\nv3.63 (September 19, 2026): No rule changed in this document. ONE\n"))
EDITS.append((PROTOCOL, 'PROTOCOL  v3.61 removed, a fourth entry pushes the oldest down',
    b'\nv3.61 (September 16, 2026): No rule changed in this document. ONE\nskill bump, taken ahead of the store work it serves.\n\nprovenance-discipline 2.12 -> 2.13 (L-335). L-322 (d), significant\nfigures, is ruled, and one ruling of four days earlier is withdrawn.\n\nTHE PROCEDURE IS THE TEXTBOOK ONE, written down once. Tony asked for\nstandard methods and named the reference. The skill now says: the\nfigure count is a declared field, "# Figures:", beside every value, the\nway the unit is; a literal is counted by the standard rules; a derived\nrow keeps the fewest figures of its measured inputs for a product or\nquotient and the coarsest decimal place for a sum or difference, with\nexact and declared numbers never limiting the result; the arithmetic\nruns from the primary inputs at full precision and rounds ONCE, half to\neven; and the export is where that rounding happens, carrying the count\nbeside the value so the gallery formats without guessing.\n\nTHE RULING WITHDRAWN IS L-325\'s, that a derived row stores a rounded\nliteral so a test can announce when an input moves. Tony withdrew it in\nthe same message that adopted the procedure, because a rounded literal\nat rest is a rounded intermediate for every row that chains from it.\nThe objection that earned the ruling, sixteen digits copied into a\ngallery config, is now answered at the export rather than at rest. The\nskill keeps a stub where the rule stood, so a reader who meets the two\nliteral rows knows why they look the way they do.\n\nWHAT MADE IT URGENT was measured, not recalled. The store holds 27\nderived rows and the checker could see 2 of them, because it found\nderived rows by a word on a Status line that 25 rows do not carry. It\nran green this session on the 2. The skill also disagreed with itself:\none section said a derived row stays an expression and the withdrawn\none said it stores a literal, and 21 rows followed the first while 2\nfollowed the second. Rule 8 has the checker enumerate by the\n"# Derived:" line and name every row it cannot judge.\n\nONE ADDITION BEYOND THE EIGHT RULES. The new section says the figure\nfield works "like # Unit:", and the skill had never defined "# Unit:";\nL-322 ruling 1 lived only in the ledger. The Status Line gains The Unit\nField. A convention that is not in the skill does not travel -- v3.57\'s\nlesson, a third time.\n\nTHE ORDERING IS v3.55\'s: the bump precedes the Earth-slice walk that\nwrites the field. The obligation travels: this session loaded 2.12, and\na reinstall cannot be verified from inside the session that makes it.\nThe next session confirms its loaded copy reads 2.13 before provenance\nor store work.\n\nThe header stamp and the SHA anchor move with this entry.\n\nVersion history: v3.58 moves down to\ndocumentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three\nresident.\n\n',
    b'\n'))
EDITS.append((HISTORY, 'HISTORY  v3.61 lands at the end of PART 1',
    b'(Moved down from the resident protocol on 2026-09-19 when v3.63\nmade a fourth entry.)\n\n================================================================\nPART 2 -- LESSONS REMOVED FROM THE PROTOCOL AT v3.37\n================================================================\n',
    b'(Moved down from the resident protocol on 2026-09-19 when v3.63\nmade a fourth entry.)\n\nv3.61 (September 16, 2026): No rule changed in this document. ONE\nskill bump, taken ahead of the store work it serves.\n\nprovenance-discipline 2.12 -> 2.13 (L-335). L-322 (d), significant\nfigures, is ruled, and one ruling of four days earlier is withdrawn.\n\nTHE PROCEDURE IS THE TEXTBOOK ONE, written down once. Tony asked for\nstandard methods and named the reference. The skill now says: the\nfigure count is a declared field, "# Figures:", beside every value, the\nway the unit is; a literal is counted by the standard rules; a derived\nrow keeps the fewest figures of its measured inputs for a product or\nquotient and the coarsest decimal place for a sum or difference, with\nexact and declared numbers never limiting the result; the arithmetic\nruns from the primary inputs at full precision and rounds ONCE, half to\neven; and the export is where that rounding happens, carrying the count\nbeside the value so the gallery formats without guessing.\n\nTHE RULING WITHDRAWN IS L-325\'s, that a derived row stores a rounded\nliteral so a test can announce when an input moves. Tony withdrew it in\nthe same message that adopted the procedure, because a rounded literal\nat rest is a rounded intermediate for every row that chains from it.\nThe objection that earned the ruling, sixteen digits copied into a\ngallery config, is now answered at the export rather than at rest. The\nskill keeps a stub where the rule stood, so a reader who meets the two\nliteral rows knows why they look the way they do.\n\nWHAT MADE IT URGENT was measured, not recalled. The store holds 27\nderived rows and the checker could see 2 of them, because it found\nderived rows by a word on a Status line that 25 rows do not carry. It\nran green this session on the 2. The skill also disagreed with itself:\none section said a derived row stays an expression and the withdrawn\none said it stores a literal, and 21 rows followed the first while 2\nfollowed the second. Rule 8 has the checker enumerate by the\n"# Derived:" line and name every row it cannot judge.\n\nONE ADDITION BEYOND THE EIGHT RULES. The new section says the figure\nfield works "like # Unit:", and the skill had never defined "# Unit:";\nL-322 ruling 1 lived only in the ledger. The Status Line gains The Unit\nField. A convention that is not in the skill does not travel -- v3.57\'s\nlesson, a third time.\n\nTHE ORDERING IS v3.55\'s: the bump precedes the Earth-slice walk that\nwrites the field. The obligation travels: this session loaded 2.12, and\na reinstall cannot be verified from inside the session that makes it.\nThe next session confirms its loaded copy reads 2.13 before provenance\nor store work.\n\nThe header stamp and the SHA anchor move with this entry.\n\nVersion history: v3.58 moves down to\ndocumentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three\nresident.\n\n(Moved down from the resident protocol on 2026-09-19 when v3.64\nmade a fourth entry.)\n\n================================================================\nPART 2 -- LESSONS REMOVED FROM THE PROTOCOL AT v3.37\n================================================================\n'))
EDITS.append((LEDGER, 'LEDGER  [L-342] opened in section A',
    b'#### [L-340]',
    b'#### [L-342] What C1 put on the live site, and the figure rules repaired\n<!-- L:342 status:OPEN upd:2026-09-19 section:A flag:! rice:4/4/95/2 -->\n- **Opened 2026-09-19** from Claude Fable 5.1\'s review of L-322 Stage\n  C1, reviewed at orrery `21065c5d` and gallery `2ead992b`. The review\n  confirmed the walk\'s constants and its reads independently, and found\n  one visitor-visible defect and three other things.\n- **A DEFECT THAT WAS LIVE.** Earth\'s geocorona hover read "Radius:\n  1e+2 Earth radii"; before C1 it read "100.0000 Earth radii".\n  `fmtServed` used `value.toPrecision(figures)`, and JavaScript switches\n  that to exponent notation whenever the integer part has more digits\n  than the figure count. C1 declared the first figure counts this store\n  has ever carried, so it is the first time a served value met the\n  condition. ALL FOURTEEN GALLERY CHECKS PASSED OVER IT, because none of\n  them reads the numbers inside a hover. Fixed by\n  `patch_L342_1_served_figures_formatter_20260919.py`.\n- **THE CHECK THE REVIEW ASKED FOR WAS NOT THE CHECK BUILT, and the\n  measurement is why.** A check that fails on any hover containing\n  exponent notation was written first and run: it fails on TWENTY hovers\n  that are correct -- the Oort cloud\'s "2.00e+3 AU", the Sun\'s\n  gravitational influence at "1.50e+5", Jupiter\'s main ring at\n  "2.01e-7", the Moon at "3.684e+05" -- all written deliberately by\n  other code at magnitudes where the notation is right. A check with\n  twenty standing exceptions is not a check. What was built runs every\n  served value carrying a figure count through the renderers\' own\n  formatter and fails if one returns an exponent. Demonstrated failing\n  by restoring the old formatter: it named the geocorona AND the lower\n  mantle, which does not reach a hover today because the interior shells\n  are served in kilometres.\n- **THE WALK DECIDED A RULE IN THE WRONG PLACE.** Meeting PREM\'s\n  `3480.0`, it wrote into that constant\'s own comment that a trailing\n  zero in a padded decimal place does not count. The skill said the\n  opposite. Both were wrong. The cited page says a trailing zero after a\n  decimal point is significant WHEN IT FALLS WITHIN THE SOURCE\'S\n  REPORTING RESOLUTION -- which is why 1500 m at 100 m resolution has\n  two figures. Rule 2 had dropped that condition; the walk\'s replacement\n  ignored it. Settled by Tony 2026-09-19: implement the rules as the\n  page states them. `EARTH_OUTER_CORE_KM` 4 -> 5,\n  `EARTH_MEAN_RADIUS_KM` 4 -> 7, both inherited by their `_RADII` rows.\n- **ONE PREMISE WAS ALSO FACTUALLY FALSE**, and the review caught it:\n  the mean radius row claimed the NASA fact sheet is "padded to three\n  decimals throughout", and the same block prints 3485, 5513, 20.4 and\n  11.186.\n- **THE HILL SPHERE DECLARED SEVEN FIGURES AND DISOWNED THEM** in its\n  own next sentence, and the gallery formats from the declared count, so\n  a visitor saw 234.6388 Earth radii. Corrected to three. The rule this\n  needed did not exist and is now in the skill: a row may declare fewer\n  figures than its inputs support when the RELATION is itself\n  approximate.\n- **RULING: ASTM E29 IS AN ASIDE, NOT THE REFERENCE.** Asked whether to\n  adopt the standard verbatim rather than restate it, Tony confirmed the\n  recommendation against. It costs $86, so a rule the project works from\n  could not be opened by anybody in the loop, which fails our own Access\n  Standard; and its scope is conformance with specification limits,\n  which this store does not have. Verbatim would not have prevented this\n  failure anyway: what failed is that nobody could check the\n  restatement against its source without opening the source.\n  provenance-discipline 2.14 -> 2.15 carries all of it.\n- **THE DISPUTED COMMIT, settled by the commits.** Orrery `4417217`\n  holds four files and none of the files a maintenance run always\n  rewrites; `4f54728` holds all of them. So Tony excluded nothing, as he\n  said twice, and the run had not been run. The builder\'s explanation --\n  that a file was left out of the commit -- was a guess and was wrong,\n  and the patch\'s own closing text, which said nothing would change, is\n  what made the run look optional. **Worth keeping:** a commit made\n  without the maintenance run is visible afterwards by the absence of\n  the files the run always rewrites.\n- **STILL OPEN.** The read check: the skill says a missing `# Read:` on\n  an in-scope row inside a closed slice FAILS, and no check does that\n  yet. It must be demonstrated failing before `CLOSED_SLICES` changes.\n  Also open: the geocorona hover gives its altitude as 631,436 km, six\n  figures beside a one-figure floor, which predates C1.\n- **Ref:** `gallery/feature_renderers.js`;\n  `documentation/smoke_hover_budget.js`; `constants_new.py`;\n  `skills/provenance-discipline/SKILL.md`.\n\n#### [L-340]'))


def main():
    if os.path.basename(os.getcwd()) == "documentation":
        fail("ERROR: this script is running from documentation/. Move it "
             "to the repository ROOT and run it there.")
    for path in BASE:
        if not os.path.exists(path):
            fail("ERROR: " + path + " is not here. Run this from the "
                 "ORRERY repo root.")

    raws = {}
    for path in BASE:
        with open(path, "rb") as handle:
            raws[path] = handle.read()
        got = fingerprint(path, raws[path])
        if got != BASE[path]:
            fail("ERROR: " + path + " is not the file this patch was cut "
                 "against.\n  expected " + BASE[path] + "\n  found    "
                 + got + "\nIf the patch already ran, this is what a "
                 "second run looks like: it refuses.")

    out = dict(raws)
    for path, label, old, new in EDITS:
        is_crlf = raws[path].count(b"\r\n") > 0
        if is_crlf:
            old = old.replace(b"\n", b"\r\n")
            new = new.replace(b"\n", b"\r\n")
        n = out[path].count(old)
        if n != 1:
            fail("ANCHOR FAIL: expected exactly 1 match, found %d -- %s"
                 % (n, label))
        out[path] = out[path].replace(old, new)

    for path, data in out.items():
        try:
            data.decode("ascii")
        except UnicodeDecodeError as exc:
            fail("ERROR: the result for " + path + " is not ASCII (%s)."
                 % exc)

    for path, data in out.items():
        with open(path, "wb") as handle:
            handle.write(data)

    for path, label, _o, _n in EDITS:
        print("  ok  " + label)
    print("")
    for path in sorted(out):
        print("      %-46s %7d -> %7d bytes"
              % (path, len(raws[path]), len(out[path])))
    print("")
    print("patch applied (4 files, %d edits)" % len(EDITS))
    print("")
    print("NOW, in order:")
    print("  1. Run skills_index.py. Expect it to report the manifest")
    print("     was advertising provenance-discipline 2.14 before it")
    print("     overwrites it with 2.15. That report is the tool working.")
    print("  2. Run ledger_index.py. Expect L-342 OPEN in section A.")
    print("     The block count is 336 if this patch ran before")
    print("     patch_L341_3, and 337 if that one ran first.")
    print("  3. Run the orrery maintenance run.")
    print("  4. Move this script into documentation/.")
    print("  5. Commit ALL of it together -- skill, protocol, history,")
    print("     ledger -- and push. The four travel in ONE commit.")
    print("  6. REINSTALL provenance-discipline 2.15 from Settings >")
    print("     Skills, and update the Project instructions to v3.64.")
    print("     This session cannot verify either.")
    print("")
    print("Undo at any point is Discard Changes in GitHub Desktop.")


if __name__ == "__main__":
    main()
