"""
patch_L258_significant_figures_at_rest.py

Two edits in the ORRERY repo, one transaction.

Built on orrery `071a0a651a4e03e7b4a3a163f09d93b33ffcf2e9` at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Confirmed against the live remote 2026-08-29.


WHY

Tony's ruling, 2026-08-29: "On 0.713 we established the rule that
significant figures where verified should be used," and "the significant
figure telling should be in the skill."

The second half is the load-bearing one.  The rule existed in Tony's head
and in one worked case; it had no home in any skill, so it reached him as
a question instead of being applied.  That is Method Belongs to the Skill
(resident protocol, Part 3).


EDIT 1 -- skills/provenance-discipline/SKILL.md, 2.9 -> 2.10

`Report to the Figures You Have` already governs how many figures a
REPORT states -- a hover, a tooltip, a comment restating a quotient.  It
says nothing about the stored value itself, and the gap is not academic:
`RADIATIVE_ZONE_AU` held 0.7 beside its own comment saying it rounds
0.713.  The store recorded that it was rounding, and rounded anyway, for
as long as anyone has looked.

New subsection: The Store Carries the Verified Figure.  Rounding belongs
at the reporting step, never at rest.

The section is deliberately narrow, because two neighbouring cases are
NOT this one and would be damaged by it.  A pick from a range is a
declared choice and stays one (Measured Is the Goal).  A visibility
stylization is a declared choice too, and promotes on its own terms --
the chromosphere's 1.1 went to 1.002875 because the physical value
became drawable, not because 1.1 had too few digits.


EDIT 2 -- constants_new.py, RADIATIVE_ZONE_AU 0.7 -> 0.713

Applying the rule, and repairing the citation in the same pass, because
reading the source turned up a second thing.

Christensen-Dalsgaard, Gough & Thompson (1991), ApJ 378:413 does not
state 0.713.  It states a convection-zone DEPTH of 0.287 +/- 0.003
solar radii; the base sits at 1 - 0.287.  Our comment reported the
subtraction as though it were the paper's own figure.  The line now says
what the paper says and shows the one-step derivation.

Access standard: the result is on the free NASA ADS abstract page
(1991ApJ...378..413C), so it clears without a paywall.  Independently
corroborated in open arXiv text, which gives the 1991 estimate as
0.713 +/- 0.003 and Basu & Antia (2004) as 0.7133 +/- 0.0005.

Figures: +/- 0.003 supports three decimal places, which is what 0.713
carries.  Not 0.7133 -- that is a different source's number and adopting
it would change which work the row cites.

Also corrected: the comment called the boundary "the helioseismic
tachocline."  The paper measures the base of the convection zone.  The
tachocline is the shear layer at approximately that depth, which is a
neighbouring claim rather than the cited one.

THE VALUE MOVES, so this is a Mode 5 item.  0.7 -> 0.713 R_sun is about
9,000 km -- 1.9 percent -- and the radiative zone is drawn inside the
photosphere at 1.0, so the gap between them narrows slightly.


WHAT MUST FOLLOW, IN THIS ORDER

1. Run this patch.
2. Run `skills_index.py` so the Skill Manifest advertises 2.10.
3. Reinstall provenance-discipline to the account (Settings > Skills).
   This CANNOT be verified from inside the session that did it -- the
   loaded copy is bound when the conversation starts.  It becomes a
   handoff obligation: the next session confirms its loaded copy reads
   2.10 before doing provenance work.
4. Commit and push the ORRERY.
5. Re-run the gallery cache builder, so the served feature config
   carries 0.713 instead of 0.7.
6. Mode 5 on the Sun exhibit, then commit and push the GALLERY.

Steps 5 and 6 are why this lands before the Sun push rather than after:
the served cache is a copy, and pushing the exhibit first would publish
the old number.


HOW TO RUN IT

Drop this file into the ORRERY repo root -- the folder holding
constants_new.py -- and press Run.

Prepared August 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

REPO_ROOT_FALLBACK = r"C:\Users\tonyq\Documents\GitHub\palomas_orrery"

CONSTANTS = "constants_new.py"
SKILL = os.path.join("skills", "provenance-discipline", "SKILL.md")

CONSTANTS_MD5 = "90711468b50e71b7015a3047da223dfc"
SKILL_MD5 = "1e48e5ebd85cdee2d581b78284de57c2"


def find_repo_root():
    here = os.path.dirname(os.path.abspath(__file__))
    for label, folder in (("beside this script", here),
                          ("working directory", os.getcwd()),
                          ("fallback path", REPO_ROOT_FALLBACK)):
        if os.path.isfile(os.path.join(folder, CONSTANTS)):
            print("found %s in the %s" % (CONSTANTS, label))
            return folder
    return None


# ---------------------------------------------------------------------
# EDIT 1 -- the skill
# ---------------------------------------------------------------------

SIGFIG_SECTION = '''(Tony's ruling, 2026-08-26, after exactly that appeared in a table.)

### The Store Carries the Verified Figure [CRITICAL]

**Where a source gives a verified figure more precise than the stored
value, the store carries the verified figure. Rounding happens at the
reporting step, never at rest.**

The section above governs how many figures a hover, tooltip or comment
STATES. This governs what the store HOLDS, and the answer is every
figure the source supports.

A rounded value at rest is a second, less precise store of a number that
already exists -- the same failure as a shadow constant, one digit at a
time. It also reads as a measurement to everything downstream: the
served cache copies it, the assembler draws it, and no layer below the
orrery knows it was rounded.

**The tell is a value whose own comment names a figure more precise than
the value beside it.**

```python
RADIATIVE_ZONE_AU = 0.7 * SOLAR_RADIUS_AU
# Visualization boundary; rounds the helioseismic tachocline at ~0.713
```

The store recorded that it was rounding, and rounded anyway. Held from
first writing until 2026-08-29, in a value drawn on a public page.

**How many figures is set by the source's uncertainty, not by taste.**
0.713 +/- 0.003 supports three decimal places. Adopting a later,
tighter figure from a different work is not a precision improvement --
it changes which work the row cites, and that is a re-sourcing with its
own access check.

**Two neighbouring cases are NOT this one**, and applying this rule to
them would be wrong:

- **A pick from a range** is a declared choice and stays one. The range
  carries the citation; the pick carries its reason. Adding digits to a
  midpoint does not make it measured.
- **A visibility stylization** promotes on its own terms, when the
  physical value becomes drawable -- not because it had too few digits.
  The chromosphere's 1.1 went to 1.002875 for that reason, on
  2026-08-16.

The question this rule answers is method, not judgement: it resolves the
same way next month, for a different constant, in a different file. It
does not go to Tony. (His ruling, 2026-08-29, sending exactly that
question back: "we established the rule that significant figures where
verified should be used.")
'''

SKILL_EDITS = [
    (
        "add The Store Carries the Verified Figure after the reporting rule",
        "(Tony's ruling, 2026-08-26, after exactly that appeared in a table.)",
        SIGFIG_SECTION.rstrip("\n"),
    ),
    (
        "bump the skill version line to 2.10",
        "Skill version: 2.9 | Cut from palomas_orrery @ a263f73d (v2.9),\n"
        "earlier @ 7f4a2f9f (v2.8), @ 3faa72a0 (v2.7), @ f603be3 (v2.6),\n"
        "@ 731066f (v2.5), @ 6b99ace (v2.2), @ 00219d9 (v2.1),\n"
        "@ eb77c83 (v2.0), @ cdcdb4b (v1.9) | August 28, 2026",

        "Skill version: 2.10 | Cut from palomas_orrery @ 071a0a65 (v2.10),\n"
        "earlier @ a263f73d (v2.9), @ 7f4a2f9f (v2.8), @ 3faa72a0 (v2.7),\n"
        "@ f603be3 (v2.6), @ 731066f (v2.5), @ 6b99ace (v2.2),\n"
        "@ 00219d9 (v2.1), @ eb77c83 (v2.0), @ cdcdb4b (v1.9)\n"
        "| August 29, 2026\n"
        "v2.10 adds The Store Carries the Verified Figure [CRITICAL] under\n"
        "Report to the Figures You Have, which governed REPORTING and left\n"
        "the stored value uncovered. Founding case: RADIATIVE_ZONE_AU held\n"
        "0.7 beside its own comment saying it rounded 0.713 -- the store\n"
        "recording that it was rounding, and rounding anyway, in a value\n"
        "drawn on a public page. The rule is narrowed in the same breath\n"
        "against the two cases it would damage: a pick from a range stays\n"
        "a declared choice, and a visibility stylization promotes when the\n"
        "physical value becomes drawable rather than for want of digits.\n"
        "Tony's ruling, 2026-08-29, and the reason it is a SKILL rule and\n"
        "not a decision: it resolves the same way next month, for a\n"
        "different constant, in a different file. Handle L-258.",
    ),
]


# ---------------------------------------------------------------------
# EDIT 2 -- the constant
# ---------------------------------------------------------------------

CONSTANTS_EDITS = [
    (
        "promote RADIATIVE_ZONE_AU to the verified figure and repair its source",
        "RADIATIVE_ZONE_AU = 0.7 * SOLAR_RADIUS_AU\n"
        "# Visualization boundary; rounds the helioseismic tachocline at ~0.713 R_sun\n"
        "# Source: Christensen-Dalsgaard, Gough & Thompson (1991), ApJ 378:413\n"
        "# Cross-checked: GPT 2026-08-02 -- helioseismology literature (constants_remaining_independent_verification_gpt.md)\n"
        "# Cross-checked: Gemini 2026-08-02 -- Carroll & Ostlie (worksheet_gemini_constants_remaining.md)\n",

        "RADIATIVE_ZONE_AU = 0.713 * SOLAR_RADIUS_AU\n"
        "# Source: Christensen-Dalsgaard, Gough & Thompson (1991), ApJ 378:413,\n"
        "#   \"The depth of the solar convection zone\" -- convection-zone DEPTH\n"
        "#   measured at 0.287 +/- 0.003 solar radii.\n"
        "# Derived: base of the convection zone = 1 - 0.287 = 0.713 R_sun. A\n"
        "# Derived+: subtraction, so decimal PLACES govern: three, matching the\n"
        "# Derived+: stated +/- 0.003.\n"
        "# Status: measured 2026-08-29 -- verified against the source\n"
        "# Access: free NASA ADS abstract, bibcode 1991ApJ...378..413C. Also\n"
        "#   corroborated in open arXiv text (astro-ph/0511779), which gives\n"
        "#   the 1991 estimate as 0.713 +/- 0.003 and Basu & Antia (2004) as\n"
        "#   0.7133 +/- 0.0005. The tighter figure is NOT adopted: it is a\n"
        "#   different work, and taking it is a re-sourcing, not a rounding.\n"
        "# Corrected: 2026-08-29 (L-258) -- held 0.7 beside a comment saying\n"
        "#   it rounded 0.713, which is the founding case for The Store\n"
        "#   Carries the Verified Figure (provenance-discipline 2.10). The\n"
        "#   comment also called this the helioseismic TACHOCLINE; the paper\n"
        "#   measures the base of the convection zone, and the tachocline is\n"
        "#   the shear layer at approximately that depth -- a neighbouring\n"
        "#   claim, not the cited one.\n"
        "# Cross-check retired: 2026-08-29 -- two legs dated 2026-08-02 were\n"
        "#   stripped, per A Cross-Check Retires With Its Value or Its\n"
        "#   Citation. Both triggers fired at once: the value moved 0.7 ->\n"
        "#   0.713, and the source line was repaired. The GPT leg certified\n"
        "#   0.7 against \"helioseismology literature\" and a check of the old\n"
        "#   value is not a check of the new one. The Gemini leg cited\n"
        "#   Carroll & Ostlie, which is not the work this row cites, so it\n"
        "#   certified a neighbouring claim. Recorded rather than deleted\n"
        "#   silently: a removal leaves no trace otherwise.\n",
    ),
    (
        "re-home INNER_CORONA_RADII to a source that passes the access standard",
        "INNER_CORONA_RADII = 3\n"
        "# Source: Golub & Pasachoff, \"The Solar Corona\" (2010)\n"
        "# Note: Visualization boundary for inner (K-)corona; physical extent 2-3 R_sun\n"
        "# Cross-checked: Gemini 2026-08-02 -- Golub & Pasachoff (worksheet_gemini_constants_remaining.md)\n",

        "INNER_CORONA_RADII = 3\n"
        "# Source: Lamy, Gilardy, Llebaria, Quemerais & Ernandez, \"Coronal\n"
        "#   Photopolarimetry with the LASCO-C3 Coronagraph over 24 Years\n"
        "#   [1996-2019]\", Solar Physics -- Sec. 1: the inner solar corona,\n"
        "#   \"defined here as extending to ~3 R_sun from the center of the\n"
        "#   solar disk\".\n"
        "# Status: declared 2026-08-29 -- a stated CONVENTION, not a\n"
        "#   measurement. The inner (K-)corona has no sharp edge; the\n"
        "#   boundary is where the F-corona overtakes the K-corona in\n"
        "#   brightness, which happens across roughly 2-3 R_sun. 3 is the\n"
        "#   top of that transition and the value the cited work adopts.\n"
        "# Access: open arXiv full text, arXiv:2009.04820. Companion Paper I\n"
        "#   (LASCO-C2) is Lamy et al. (2020), Solar Phys. 295:89.\n"
        "# Corrected: 2026-08-29 (L-258) -- previously cited Golub &\n"
        "#   Pasachoff, \"The Solar Corona\" (2010). That work fails the\n"
        "#   access standard on its own terms: the independent nine-source\n"
        "#   read of 2026-08-20 could locate it only as \"Chapter 1\", with no\n"
        "#   figure and no findable position. The VALUE is unchanged and was\n"
        "#   never in doubt; only the citation moved. (That read was about\n"
        "#   helmet-streamer extent, a different claim, so its finding does\n"
        "#   not transfer -- reachability does.)\n"
        "# Cross-check retired: 2026-08-29 -- the Gemini leg of 2026-08-02\n"
        "#   was stripped with the citation it checked. A cross-check of a\n"
        "#   citation that no longer exists grants credit for nothing.\n",
    ),
]


def check(path, expected_md5, edits, label):
    print("")
    print("--- %s" % label)
    print("path   :", path)
    if not os.path.isfile(path):
        print("REFUSED: no such file.")
        return None

    with open(path, "rb") as fh:
        raw = fh.read()

    actual = hashlib.md5(raw).hexdigest()
    print("md5    : %s (expected %s)" % (actual, expected_md5))
    if actual != expected_md5:
        print("REFUSED: not the file this patch was cut against.")
        return None

    if b"\r\n" in raw:
        print("REFUSED: CRLF line endings; this patch expects LF.")
        return None

    text = raw.decode("utf-8")
    for name, old, _new in edits:
        n = text.count(old)
        print("  anchor x%d  %s" % (n, name))
        if n != 1:
            print("REFUSED: anchor matched %d times, expected 1." % n)
            return None

    return raw, text


def main():
    print("patch_L258_significant_figures_at_rest.py")
    repo_root = find_repo_root()
    if repo_root is None:
        print("REFUSED: could not find %s. Move this script into the"
              % CONSTANTS)
        print("         ORRERY repo root and run it again.")
        return 1

    const_path = os.path.join(repo_root, CONSTANTS)
    skill_path = os.path.join(repo_root, SKILL)

    const = check(const_path, CONSTANTS_MD5, CONSTANTS_EDITS,
                  "EDIT 2  constants_new.py")
    if const is None:
        print("")
        print("NOTHING WAS WRITTEN.")
        return 1

    skill = check(skill_path, SKILL_MD5, SKILL_EDITS,
                  "EDIT 1  skills/provenance-discipline/SKILL.md")
    if skill is None:
        print("")
        print("NOTHING WAS WRITTEN. constants_new.py is untouched.")
        return 1

    outputs = []
    for (raw, text), edits, path in ((const, CONSTANTS_EDITS, const_path),
                                     (skill, SKILL_EDITS, skill_path)):
        for _name, old, new in edits:
            text = text.replace(old, new, 1)
        out = text.encode("utf-8")
        before = sum(1 for c in raw if c > 127)
        after = sum(1 for c in out if c > 127)
        if after != before:
            print("REFUSED: %s gained non-ASCII text (%d -> %d). Nothing written."
                  % (os.path.basename(path), before, after))
            return 1
        outputs.append((path, raw, out))

    print("")
    for path, raw, out in outputs:
        with open(path + ".bak", "wb") as fh:
            fh.write(raw)
        with open(path, "wb") as fh:
            fh.write(out)
        print("WROTE   %s  (%d -> %d bytes)" % (path, len(raw), len(out)))

    print("")
    print("RADIATIVE_ZONE_AU  0.7 -> 0.713 R_sun  (about 9,000 km, 1.9%)")
    print("provenance-discipline  2.9 -> 2.10")
    print("")
    print("Next, in order:")
    print("  1. python skills_index.py")
    print("  2. reinstall provenance-discipline (Settings > Skills)")
    print("  3. commit and push the ORRERY")
    print("  4. re-run the gallery cache builder")
    print("  5. Mode 5 on the Sun exhibit, then push the GALLERY")
    print("")
    print("Step 2 cannot be verified from inside this session. It becomes")
    print("a handoff obligation: the next session confirms 2.10 loaded.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
