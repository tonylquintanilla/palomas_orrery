#!/usr/bin/env python3
"""patch_L322_C2_0_skill_2_16_20260921.py -- ORRERY repo.

Stage C2-0 of L-322: the skill update that must come BEFORE the C2 build.
It writes into provenance-discipline how a stated uncertainty decides a
figure count, because the C2 build's figures checker implements exactly
that text and the build's figure lines follow it. A convention that is
not in the skill does not travel.

WHAT IT CHANGES, in one all-or-nothing pass:

  1. skills/provenance-discipline/SKILL.md, 2.15 -> 2.16.
     Rule 1 gains the field form of an uncertainty. Rule 3 gains "The
     ceiling": which uncertainty is propagated, show-or-cap for an
     approximate relation, when propagation sets the ceiling, how to
     propagate, how to report -- with what the reference page says kept
     apart from what this project adds. Rule 8 gains the ceiling check,
     specified here and built at C2. The version line and its paragraph
     move with it. The text is section 4.0 of
     documentation/BUILD_MANIFEST_L322_C2_magnetosphere_20260920.md,
     reviewed twice by Claude Fable 5.1.
  2. PROJECT_INSTRUCTIONS.md, v3.65 -> v3.66: the header stamp, the
     cut-from anchor, and a version-history entry saying what changed
     and why. The oldest of the four resident entries, v3.63, moves out.
  3. documentation/PROJECT_INSTRUCTIONS_HISTORY.md: v3.63 arrives at the
     end of PART 1, word for word, with a note saying when it moved.
  4. Then it runs skills_index.py, which rewrites the Skill Manifest
     table in PROJECT_INSTRUCTIONS.md from the new version line, and
     checks the table now reads 2.16.

Those four are the binding rule of ledger-and-session-records: a skill
bump is not done until the manifest agrees AND the protocol's history
says what changed, all in ONE commit.

WHAT IS PERMANENT: the new skill text, the protocol entry and the moved
history entry. This script is not; it is filed in documentation/ as the
record once it has run.

RUN IT LIKE THIS, from the ORRERY repo ROOT (the folder that holds
constants_new.py and PROJECT_INSTRUCTIONS.md):
    save this file in the repo root, open it in VS Code, click Run.
    (Terminal equivalent: python patch_L322_C2_0_skill_2_16_20260921.py)
It asks no questions. A patch run from documentation/ refuses and writes
nothing.

SUCCESS looks like: one "ok" line per edit, the stamps it updated, the
skills_index.py output, "Skill Manifest now reads provenance-discipline
2.16", then numbered steps.
FAILURE looks like: one "ERROR:" or "ANCHOR FAIL" line and "NOTHING was
written". Undo after a success is Discard Changes in GitHub Desktop.

Built on palomas_orrery a7014abb3394c009f88b9ed2bcce4964326d626a
at https://github.com/tonylquintanilla/palomas_orrery .
Written September 21, 2026 with Anthropic's Claude Opus 5.
"""
import hashlib
import os
import subprocess
import sys

SKILL = os.path.join("skills", "provenance-discipline", "SKILL.md")
PROTO = "PROJECT_INSTRUCTIONS.md"
HIST = os.path.join("documentation", "PROJECT_INSTRUCTIONS_HISTORY.md")
ZONE_START = b"<!-- SKILL-MANIFEST:START"
ZONE_END = b"<!-- SKILL-MANIFEST:END -->"

# Content fingerprints at a7014abb: md5 of the file with CRLF read as LF.
# The protocol's is taken OUTSIDE the Skill Manifest zone, because
# skills_index.py rewrites that zone and a guard must not fence it.
EXPECT = {
    SKILL: "d9439e3cb8a3210fe515256ce7acb078",
    PROTO: "8d3717aae66be3094321490aed842e28",
    HIST: "787d681b566b7dc31507c1b20765db30",
}


def fail(msg):
    print(msg)
    print("NOTHING was written.")
    sys.exit(1)


def fingerprint(path, lf):
    if path == PROTO:
        a = lf.index(ZONE_START)
        b = lf.index(ZONE_END) + len(ZONE_END)
        lf = lf[:a] + lf[b:]
    return hashlib.md5(lf).hexdigest()


def b(text):
    data = text.encode("ascii")  # refuses any non-ASCII inserted text
    return data


# ---------------------------------------------------------------- skill
SKILL_EDITS = [
    # version line and its date
    (b("Skill version: 2.15 | Cut from palomas_orrery @ 21065c5d (v2.15),\n"
       "earlier @ dfa779bd (v2.14), @ ebdc55cc (v2.13), @ bfc0505e (v2.12),\n"),
     b("Skill version: 2.16 | Cut from palomas_orrery @ a7014abb (v2.16),\n"
       "earlier @ 21065c5d (v2.15), @ dfa779bd (v2.14), @ ebdc55cc (v2.13),\n"
       "@ bfc0505e (v2.12),\n")),
    (b("| September 19, 2026\nv2.15 repairs the figure rules"),
     b("| September 21, 2026\n"
       "v2.16 writes down how a stated uncertainty decides a figure count,\n"
       "before L-322 Stage C2 builds the check for it. Rule 3 already said the\n"
       "uncertainty decides and counting is the fallback, and the procedure it\n"
       "was adopted from says to propagate; neither said how, and the checker\n"
       "counts only. On Tony's instruction of 2026-09-20, \"See the Skill on\n"
       "significant digits\", the magnetopause standoff was worked by the rule:\n"
       "Shue's five coefficient uncertainties propagate to +/- 0.13 Earth\n"
       "radii, which the reference page's single-number rule reports to\n"
       "tenths, 10.3 -- the stored 10.25 was a figure too many. RULE 3 GAINS\n"
       "THE CEILING, in five parts: which uncertainty is propagated (the\n"
       "inputs', not a model's scatter about its data); show or cap for an\n"
       "approximate relation; when propagation sets the ceiling and when\n"
       "counting does; how to propagate (central difference, root-sum-square,\n"
       "from full digits, independence stated with its bound, an implied\n"
       "half-unit for a primary that states none); and how to report, with\n"
       "the page's words kept apart from the log-scale measure this project\n"
       "adds. RULE 1 gains the field form of an uncertainty, so a checker\n"
       "reads a field and never prose. RULE 8 gains the ceiling check,\n"
       "specified here and built at C2. Claude Fable 5.1 reviewed the text\n"
       "twice before it was cut; its second look found that an earlier form\n"
       "of the ceiling rule would have failed fifteen finished C1 rows, and\n"
       "the rule now fails a row only for claiming more than its uncertainty\n"
       "supports. Handle L-322.\n"
       "v2.15 repairs the figure rules")),
    # Rule 1: two more forms and the field
    (b("**Rule 1. `# Figures:` is a comment key beside the value.** Three forms:\n"
       "\n"
       "```\n"
       "# Figures: 5 -- set by EARTH_INNER_CORE_KM (1221.5, 5)\n"
       "# Figures: 5 -- PREM reports to 0.1 km, so 3480.0's trailing zero counts\n"
       "# Figures: exact -- IAU 2012 definition\n"
       "```\n"
       "\n"
       "A derived row names the input that set its count. A measured row\n"
       "states what the source supports, and says in words whether a trailing\n"
       "zero counts, because an integer literal cannot. A defined constant says\n"
       "`exact`."),
     b("**Rule 1. `# Figures:` is a comment key beside the value.** Five forms:\n"
       "\n"
       "```\n"
       "# Figures: 5 -- set by EARTH_INNER_CORE_KM (1221.5, 5)\n"
       "# Figures: 5 -- PREM reports to 0.1 km, so 3480.0's trailing zero counts\n"
       "# Figures: exact -- IAU 2012 definition\n"
       "# Figures: 4 -- Table 1 prints 10.22, uncertainty 0.10\n"
       "# Figures: 3 -- uncertainty 0.13, root-sum-square of Shue's a1 to a5\n"
       "```\n"
       "\n"
       "A derived row names the input that set its count. A measured row\n"
       "states what the source supports, and says in words whether a trailing\n"
       "zero counts, because an integer literal cannot. A defined constant says\n"
       "`exact`. A measured row whose source STATES an uncertainty writes it\n"
       "as a FIELD: the word `uncertainty` followed directly by the number, in\n"
       "the row's own unit, on its `# Figures:` line. A checker reads that\n"
       "field and never the prose around it, so \"an uncertainty of 0.1 m\" in\n"
       "words is not read. A derived row writes the uncertainty form only when\n"
       "it declares more figures than counting alone allows, and then the\n"
       "number is the one recomputed from full digits (Rule 3, The ceiling).")),
    # Rule 3: pointer from the first paragraph
    (b("row. Where an input carries a stated uncertainty, the uncertainty\n"
       "decides instead and counting is the fallback.\n"),
     b("row. Where an input carries a stated uncertainty, the uncertainty\n"
       "decides instead and counting is the fallback; how is set out under The\n"
       "ceiling, below.\n")),
    # Rule 3: the ceiling, after the approximate-relation paragraph
    (b("its inputs carry. This is a floor on honesty, not a licence to round to\n"
       "taste: the row must say WHICH approximation caps it and by roughly how\n"
       "much. (L-342, Fable's review of C1, Finding 3.)\n"),
     b("its inputs carry. This is a floor on honesty, not a licence to round to\n"
       "taste: the row must say WHICH approximation caps it and by roughly how\n"
       "much. (L-342, Fable's review of C1, Finding 3.)\n"
       "\n"
       "**The ceiling: where an uncertainty is stated, propagate it** (v2.16).\n"
       "The procedure these rules were adopted from says it in one line:\n"
       "\"Where any input carries a stated uncertainty, propagate that instead\n"
       "and let it decide.\" Five parts make that usable. What the reference\n"
       "page says is kept apart from what this project adds, and the project's\n"
       "part is marked as its own.\n"
       "\n"
       "- **Which uncertainty.** Propagate the stated uncertainties of the\n"
       "  INPUTS: how well each was measured or fitted. A model's scatter about\n"
       "  the data it was fitted to is a different quantity. It describes the\n"
       "  real thing around the model, and it is shown beside the value, not\n"
       "  propagated into it.\n"
       "- **Show or cap.** Where the source publishes the size of a relation's\n"
       "  mismatch as a number the store can hold and the page can show, show\n"
       "  it beside the value: real magnetopause crossings scatter 1.23 Earth\n"
       "  radii about Shue's model, and the hover says so. Where it does not,\n"
       "  cap the count and say why on the row, as the Hill sphere's is in the\n"
       "  paragraph above. This decides which of the two answers applies.\n"
       "- **When propagation sets the ceiling.** A derived row's ceiling -- the\n"
       "  most figures it may declare -- is set by propagation whenever at\n"
       "  least one measured primary in its chain STATES an uncertainty, and by\n"
       "  counting otherwise. A row may always declare its ceiling or fewer. It\n"
       "  writes the uncertainty form of Rule 1 only when it declares MORE than\n"
       "  counting alone allows, so the reason for the extra figures is on the\n"
       "  row; a row that counts and stays within its ceiling keeps its\n"
       "  counting line. Implied uncertainties alone never set a ceiling:\n"
       "  Jelinek's bow shock standoff, whose chain states none, is 13.5 by\n"
       "  counting and would be 13.51 if they did.\n"
       "- **Propagate.** Trace the row to its primaries. Move each up and down\n"
       "  by its uncertainty and take the half-difference, a central\n"
       "  difference; a one-sided step gives a different answer wherever the\n"
       "  relation curves (Shue's standoff gives 0.129 up and 0.136 down).\n"
       "  Combine by root-sum-square, re-evaluating through the chain from full\n"
       "  digits: Rule 4 applies to an uncertainty exactly as to a value, and\n"
       "  an uncertainty converted from a rounded one is the same failure.\n"
       "  Root-sum-square assumes independent inputs; where the source gives no\n"
       "  correlations the row says so, and where the reported place would not\n"
       "  survive the plain sum of the effects, the row gives both numbers. A\n"
       "  primary that states no uncertainty contributes its implied one, half\n"
       "  a unit in its last significant place, as the page allows; that is a\n"
       "  full half-width rather than a standard deviation, so it errs large.\n"
       "  Declared conditions and exact numbers contribute nothing.\n"
       "- **Report. What the page says:** to report a single number, choose\n"
       "  the one whose implied range is close to the measured range, since\n"
       "  going coarser loses a lot of information; its examples are\n"
       "  3.78 +/- 0.07 kg and 3.78 +/- 0.09 kg, both best quoted as 3.8 kg.\n"
       "  Where the uncertainty is printed beside the value, it takes one or\n"
       "  two figures and the value ends in the same place. **What this project\n"
       "  adds, and why:** \"close\" is measured on a log scale, because implied\n"
       "  uncertainties step by factors of ten, and a tie goes to the coarser\n"
       "  place; a linear measure would keep the tenths place up to +/- 0.27\n"
       "  and overstate the precision five-fold. Each unit is reported by its\n"
       "  own uncertainty, so a value and its conversion can carry different\n"
       "  counts; the page warns of exactly this for unit conversions.\n"
       "\n"
       "The magnetopause standoff is the worked case. Shue's Table 1 states a\n"
       "standard deviation on every coefficient; propagated at the declared\n"
       "solar wind they give 10.2518729724 +/- 0.1326 Earth radii, reported\n"
       "10.3 -- the tenths place implies +/- 0.05 and the units place +/- 0.5,\n"
       "and the tenths is closer. The store had carried 10.25, a figure too\n"
       "many even by the largest single effect, +/- 0.09. In kilometres the\n"
       "same uncertainty is +/- 846 km, so 65,000 km at two figures; in AU,\n"
       "0.00044. The plain sum of the effects is 0.25 and the tenths place\n"
       "holds only to 0.158, which the row states. (Tony's instruction of\n"
       "2026-09-20, \"See the Skill on significant digits\"; worked in\n"
       "`documentation/BUILD_MANIFEST_L322_C2_magnetosphere_20260920.md`,\n"
       "section 2.1, and reviewed twice by Claude Fable 5.1. Handle L-322.)\n")),
    # Rule 8: the ceiling check
    (b("expression with no `# Derived:` line is itself a named gap. (At 2.12\n"
       "enumeration went by Status and saw 2 of 27.)\n"),
     b("expression with no `# Derived:` line is itself a named gap. (At 2.12\n"
       "enumeration went by Status and saw 2 of 27.)\n"
       "\n"
       "**The checker also enforces the ceiling of Rule 3.** It is specified\n"
       "here at 2.16 and built at L-322 Stage C2; until that build the checker\n"
       "counts only, and a row relying on the uncertainty route fails it. For\n"
       "every derived row it works out the ceiling -- by propagation where any\n"
       "measured primary in the chain states an uncertainty in the field\n"
       "form, by counting otherwise -- and FAILS a row only for declaring MORE\n"
       "than its ceiling; where the two ceilings differ it prints both. A row\n"
       "declaring more than counting allows must carry the uncertainty form,\n"
       "and its stated number must match the recomputed one to the digits\n"
       "stated, which is how a one-sided step or a rounded intermediate is\n"
       "caught. It reads uncertainties only from the field, never from prose,\n"
       "and names any primary whose figures line mentions an uncertainty in\n"
       "words without the field, so the blind spot announces.\n")),
]

# ------------------------------------------------------------- protocol
V366 = (
    "v3.66 (September 21, 2026): No rule changed in this document. ONE\n"
    "skill bump, taken ahead of the build it serves, which is v3.55's\n"
    "ordering.\n"
    "\n"
    "provenance-discipline 2.15 -> 2.16 (L-322). HOW A STATED UNCERTAINTY\n"
    "DECIDES A FIGURE COUNT IS WRITTEN DOWN.\n"
    "\n"
    "THE RULE WAS ALREADY THERE, AND IT WAS NOT APPLIED. Rule 3 said a\n"
    "stated uncertainty decides and counting is the fallback, and the\n"
    "procedure it was adopted from says to propagate. The C2 design session\n"
    "missed both and put a choice to Tony between counting digits and two\n"
    "uncertainty conventions. His answer was \"See the Skill on significant\n"
    "digits.\" It was method, which Method Belongs to the Skill had already\n"
    "said. What the skill lacked was HOW -- which uncertainty, how to\n"
    "propagate it, how to report it, and when it applies -- and the\n"
    "checker counts only, so the C2 build implements the new text.\n"
    "\n"
    "THE WORKED CASE. Shue's five coefficient uncertainties propagate to\n"
    "+/- 0.13 Earth radii at the declared solar wind, which the reference\n"
    "page's single-number rule reports to tenths: 10.3, where the store had\n"
    "carried 10.25. In kilometres the same uncertainty supports two\n"
    "figures, 65,000 km. Two more of Tony's corrections the same day shaped\n"
    "the design around it: compute with all the digits and round only at\n"
    "the end, which is Rule 4, and \"The single source of truth is\n"
    "constants_new.py\", which put the kilometre and AU figures in the store\n"
    "rather than in the page.\n"
    "\n"
    "WHAT IS OURS IS MARKED AS OURS. The page says to report so that the\n"
    "implied range is close to the measured one. That closeness is measured\n"
    "on a log scale is this project's choice, and it is written apart from\n"
    "the page's words with its reason -- 2.14 went wrong by restating a\n"
    "source with words changed and nobody able to see it.\n"
    "\n"
    "TWO REVIEWS BEFORE THE CUT. Claude Fable 5.1 reviewed the text in the\n"
    "C2 manifest twice. The first review found that the propagated figure\n"
    "is the fit's precision and not the magnetopause's -- real crossings\n"
    "scatter 1.23 Earth radii -- which became the show-or-cap sentence and,\n"
    "on Tony's ruling, a scatter line in each hover. The second found that\n"
    "an earlier form of the ceiling rule would have failed fifteen finished\n"
    "C1 rows; the rule now fails a row only for claiming more than its\n"
    "uncertainty supports, and measured over every derived Earth row, none\n"
    "does.\n"
    "\n"
    "THE OBLIGATION TRAVELS, as it always does. This session loaded 2.15,\n"
    "and a reinstall cannot be verified from inside the session that makes\n"
    "it. The next session confirms its loaded copy reads 2.16 before any\n"
    "provenance or store work, and that session is the C2 build, from\n"
    "documentation/BUILD_MANIFEST_L322_C2_magnetosphere_20260920.md.\n"
    "\n"
    "The header stamp and the SHA anchor move with this entry.\n"
    "\n"
    "Version history: v3.63 moves down to\n"
    "documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three\n"
    "resident.\n"
    "\n"
)
V363_START = b"v3.63 (September 19, 2026): No rule changed in this document. ONE\n"
PROTO_TAIL = b"Functional for Claude, readable for human, signal preserved."
PROTO_EDITS = [
    (b("Tony Quintanilla, PE | Claude | v3.65 | September 20, 2026\n"),
     b("Tony Quintanilla, PE | Claude | v3.66 | September 21, 2026\n")),
    (b("Cut from ba94e80e at https://github.com/tonylquintanilla/palomas_orrery\n"),
     b("Cut from a7014abb at https://github.com/tonylquintanilla/palomas_orrery\n")),
    (b("v3.65 (September 20, 2026): No rule changed in this document. ONE\n"),
     b(V366) + b("v3.65 (September 20, 2026): No rule changed in this document. ONE\n")),
]
HIST_ANCHOR = b("v3.65 made a fourth entry.)\n"
                "\n"
                "================================================================\n"
                "PART 2 -- LESSONS REMOVED FROM THE PROTOCOL AT v3.37\n")


def apply_edits(name, lf, edits):
    for old, new in edits:
        n = lf.count(old)
        if n != 1:
            fail("ANCHOR FAIL in %s: expected 1 match, found %d: %r"
                 % (name, n, old[:70]))
        lf = lf.replace(old, new)
        print("ok   %s: %s" % (name, old[:60].decode("ascii").splitlines()[0]))
    return lf


def main():
    if not (os.path.isfile("constants_new.py") and os.path.isfile(PROTO)
            and os.path.isdir("skills")):
        fail("ERROR: run this from the ORRERY repo ROOT (the folder holding "
             "constants_new.py and PROJECT_INSTRUCTIONS.md), not from "
             "documentation/ or anywhere else.")
    raw, lf, crlf = {}, {}, {}
    for path in (SKILL, PROTO, HIST):
        with open(path, "rb") as f:
            raw[path] = f.read()
        crlf[path] = b"\r\n" in raw[path]
        lf[path] = raw[path].replace(b"\r\n", b"\n")
    if b"Skill version: 2.16 |" in lf[SKILL]:
        fail("ERROR: SKILL.md already reads 2.16 -- this patch has been "
             "applied. Nothing to do.")
    for path in (SKILL, PROTO, HIST):
        got = fingerprint(path, lf[path])
        if got != EXPECT[path]:
            fail("ERROR: %s is not the file this patch was built on "
                 "(content md5 %s, expected %s). Pull or discard local "
                 "changes and check the orrery is at a7014abb."
                 % (path, got, EXPECT[path]))
    print("base ok: all three files match a7014abb by content")

    new = {}
    new[SKILL] = apply_edits(SKILL, lf[SKILL], SKILL_EDITS)

    p = lf[PROTO]
    if p.count(V363_START) != 1 or p.count(PROTO_TAIL) != 1:
        fail("ANCHOR FAIL in %s: v3.63 entry or closing line not found once"
             % PROTO)
    i = p.index(V363_START)
    j = p.index(PROTO_TAIL)
    if not i < j:
        fail("ANCHOR FAIL in %s: v3.63 entry is not the last resident entry"
             % PROTO)
    v363 = p[i:j]  # the whole entry, ending with its blank line
    if not v363.endswith(b"resident.\n\n"):
        fail("ANCHOR FAIL in %s: v3.63 entry does not end where expected"
             % PROTO)
    p = p[:i] + p[j:]
    print("ok   %s: v3.63 entry lifted out (%d bytes)" % (PROTO, len(v363)))
    new[PROTO] = apply_edits(PROTO, p, PROTO_EDITS)

    h = lf[HIST]
    if h.count(HIST_ANCHOR) != 1:
        fail("ANCHOR FAIL in %s: end of PART 1 not found once" % HIST)
    moved = (b"v3.65 made a fourth entry.)\n\n" + v363
             + b("(Moved down from the resident protocol on 2026-09-21 when\n"
                 "v3.66 made a fourth entry.)\n"
                 "\n"
                 "================================================================\n"
                 "PART 2 -- LESSONS REMOVED FROM THE PROTOCOL AT v3.37\n"))
    new[HIST] = h.replace(HIST_ANCHOR, moved)
    print("ok   %s: v3.63 entry placed at the end of PART 1" % HIST)

    # gates before anything is written
    for path, data in new.items():
        try:
            data.decode("ascii")
        except UnicodeDecodeError:
            fail("ERROR: %s would contain non-ASCII text" % path)
        if not data.endswith(b"\n"):
            fail("ERROR: %s would not end with a line break" % path)
    if new[PROTO].count(b"v3.63 (September 19, 2026)") != 0:
        fail("ERROR: v3.63 would still be resident")
    if new[HIST].count(b"v3.63 (September 19, 2026)") != 1:
        fail("ERROR: v3.63 would not be in the archive exactly once")

    for path, data in new.items():
        out = data.replace(b"\n", b"\r\n") if crlf[path] else data
        with open(path, "wb") as f:
            f.write(out)
    print("written: %s, %s, %s (line endings kept as found)" % (SKILL, PROTO, HIST))
    print("stamps updated: SKILL.md version line, cut-from list, date and "
          "v2.16 paragraph; protocol header v3.66, cut-from a7014abb, "
          "history entry v3.66; archive move-down note")

    print("\nrunning skills_index.py ...")
    r = subprocess.run([sys.executable, "skills_index.py"],
                       capture_output=True, text=True)
    print(r.stdout.rstrip())
    if r.stderr.strip():
        print(r.stderr.rstrip())
    with open(PROTO, "rb") as f:
        pz = f.read().replace(b"\r\n", b"\n")
    zone = pz[pz.index(ZONE_START):pz.index(ZONE_END)]
    row = [ln for ln in zone.split(b"\n") if ln.startswith(b"provenance-discipline")]
    if r.returncode != 0 or not row or b" 2.16 " not in row[0]:
        print("\nWARNING: the three files ARE written, but the Skill Manifest "
              "table did not come out reading 2.16. Do not commit. Run the "
              "orrery maintenance run and look at its Skill manifest line; if "
              "it still disagrees, Discard Changes in GitHub Desktop and tell "
              "Claude what skills_index.py printed.")
        sys.exit(1)
    print("Skill Manifest now reads provenance-discipline 2.16")

    print("""
patch applied.

DO, in this order:
  1. Run the orrery maintenance run (orrery_maintenance_run.py, Run
     button) and let it finish. It runs skills_index.py again, which
     should now say the manifest already matched.
  2. Move this patch file into documentation/.
  3. In GitHub Desktop, commit everything together -- SKILL.md,
     PROJECT_INSTRUCTIONS.md, the history file, the patch, and whatever
     the maintenance run rewrote -- then push, and tell Claude the SHA.
  4. Reinstall provenance-discipline to your account (Settings > Skills)
     from skills/provenance-discipline/SKILL.md, so it reads 2.16.
  5. Start a FRESH session for the C2 build. Its first act is to confirm
     it loaded provenance-discipline 2.16; this session cannot see the
     reinstall.
""")


if __name__ == "__main__":
    main()
