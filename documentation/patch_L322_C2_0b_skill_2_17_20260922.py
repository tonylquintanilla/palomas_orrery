#!/usr/bin/env python3
"""patch_L322_C2_0b_skill_2_17_20260922.py -- ORRERY repo.

Stage C2-0b of L-322: the second skill update that must come BEFORE the
C2 build. It writes into provenance-discipline the rules settled on
2026-09-21 by five documents between Claude Fable 5.1 and Claude Opus 5
(one round also reviewed by GPT 6), each tested against the project's
own checkers before the next was written. It began with Tony's question
when a reviewer offered a display choice with no rule behind it: "when
it comes to a decision, what is the basis? the basis should be in the
skill not arbitrary."

WHAT IT CHANGES, in one all-or-nothing pass:

  1. skills/provenance-discipline/SKILL.md, 2.16 -> 2.17.
     Rule 7 is replaced whole: a display prints the declared count and
     never chooses fewer. Rule 2 gains the declared construction. Rule 3
     gains the derivative form for a rate and the DEG_PER_RAD form for
     an angle. Show or cap gains the snapshot of a moving quantity.
     Rule 6 gains the whole a source defines from parts it prints. When
     the source gives a range gains the typed-pick case. The version
     line and its paragraph move with it.
  2. PROJECT_INSTRUCTIONS.md, v3.66 -> v3.67: the header stamp, the
     cut-from anchor, and a version-history entry saying what changed
     and why. The oldest of the four resident entries, v3.64, moves out.
  3. documentation/PROJECT_INSTRUCTIONS_HISTORY.md: v3.64 arrives at the
     end of PART 1, word for word, with a note saying when it moved.
  4. documentation/BUILD_MANIFEST_L322_C2_magnetosphere_20260920.md
     gains section 17, the consolidated revision from the tilt rounds,
     so the build session reads one document.
  5. Then it runs skills_index.py, which rewrites the Skill Manifest
     table in PROJECT_INSTRUCTIONS.md from the new version line, and
     checks the table now reads 2.17.

Those are the binding rule of ledger-and-session-records: a skill bump
is not done until the manifest agrees AND the protocol's history says
what changed, all in ONE commit. The ledger row for this bump rides
the C2 ledger patch, one per pushed HEAD, as manifest section 9 says.

WHAT IS PERMANENT: the new skill text, the protocol entry, the moved
history entry and the manifest section. This script is not; it is
filed in documentation/ as the record once it has run.

RUN IT LIKE THIS, from the ORRERY repo ROOT (the folder that holds
constants_new.py and PROJECT_INSTRUCTIONS.md):
    save this file in the repo root, open it in VS Code, click Run.
    (Terminal equivalent: python patch_L322_C2_0b_skill_2_17_20260922.py)
It asks no questions. A patch run from documentation/ refuses and writes
nothing. A second run refuses.

SUCCESS looks like: "base ok", one "ok" line per edit, "written:", the
skills_index.py output, "Skill Manifest now reads provenance-discipline
2.17", then numbered steps.
FAILURE looks like: one "ERROR:" or "ANCHOR FAIL" line and "NOTHING was
written". Undo after a success is Discard Changes in GitHub Desktop.

Built on palomas_orrery 1f6e55a9e463d027709cc10a91dbd22785585185
at https://github.com/tonylquintanilla/palomas_orrery .
Written September 22, 2026 with Anthropic's Claude Fable 5.1.
"""
import hashlib
import os
import subprocess
import sys

SKILL = os.path.join("skills", "provenance-discipline", "SKILL.md")
PROTO = "PROJECT_INSTRUCTIONS.md"
HIST = os.path.join("documentation", "PROJECT_INSTRUCTIONS_HISTORY.md")
MANI = os.path.join("documentation",
                    "BUILD_MANIFEST_L322_C2_magnetosphere_20260920.md")
ZONE_START = b"<!-- SKILL-MANIFEST:START"
ZONE_END = b"<!-- SKILL-MANIFEST:END -->"

# Content fingerprints at 1f6e55a9: md5 of the file with CRLF read as LF.
# The protocol's is taken OUTSIDE the Skill Manifest zone, because
# skills_index.py rewrites that zone and a guard must not fence it.
EXPECT = {
    SKILL: "8d7195c98fd0ed811dfadeecfa34309d",
    PROTO: "b4ef803873ecd50b4a8309269e5a38ae",
    HIST: "7a9ac9d3c3119aa2de348b110464784d",
    MANI: "1c27de7f8f5493937420112efd4ac596",
}


def fail(msg):
    print(msg)
    print("NOTHING was written.")
    sys.exit(1)


def fingerprint(path, lf):
    if path == PROTO:
        a = lf.index(ZONE_START)
        b_ = lf.index(ZONE_END) + len(ZONE_END)
        lf = lf[:a] + lf[b_:]
    return hashlib.md5(lf).hexdigest()


def b(text):
    return text.encode("ascii")  # refuses any non-ASCII inserted text


# ---------------------------------------------------------------- skill
SKILL_EDITS = [
    # version line and its date
    (b("Skill version: 2.16 | Cut from palomas_orrery @ a7014abb (v2.16),\n"
       "earlier @ 21065c5d (v2.15), @ dfa779bd (v2.14), @ ebdc55cc (v2.13),\n"
       "@ bfc0505e (v2.12),\n"),
     b("Skill version: 2.17 | Cut from palomas_orrery @ 1f6e55a9 (v2.17),\n"
       "earlier @ a7014abb (v2.16), @ 21065c5d (v2.15), @ dfa779bd (v2.14),\n"
       "@ ebdc55cc (v2.13), @ bfc0505e (v2.12),\n")),
    (b("| September 21, 2026\nv2.16 writes down how a stated uncertainty"),
     b("| September 22, 2026\n"
       "v2.17 closes the gap a display decision opened. Asked whether Earth's\n"
       "dipole tilt should print 9.4 or 9.4105, a reviewer offered a\n"
       "readability call; Tony asked what the basis was -- \"the basis should\n"
       "be in the skill not arbitrary\" -- and there was none: Rule 7\n"
       "permitted a shorter display and gave no method. RULE 7 IS REPLACED\n"
       "WHOLE: a display prints the declared count and never chooses fewer;\n"
       "a number that reads as too many figures is a finding about the ROW,\n"
       "fixed under Rule 3, never by the page. RULE 2 GAINS THE DECLARED\n"
       "CONSTRUCTION: a drawing value that is a stated rule over measured\n"
       "rows is exact as a construction, the checker accepts exact on it\n"
       "only when its status begins declared, and the export serves it\n"
       "unrounded so every consumer draws the same value. RULE 3 GAINS two\n"
       "rules for a derived quantity: a rate is written as the derivative,\n"
       "never as a difference of two evaluations, because the difference\n"
       "form takes its count from the largest inputs rather than from the\n"
       "quantities the rate rests on; and an angle computed from a pure\n"
       "number multiplies by the exact row DEG_PER_RAD instead of calling\n"
       "degrees, because the unit check sees a bare number and refuses the\n"
       "call. SHOW OR CAP gains the snapshot of a moving quantity: where the\n"
       "source publishes the rate, the store holds its inputs and the page\n"
       "shows the epoch and the rate. RULE 6 says a whole the source defines\n"
       "from parts it prints is a derived row over rows for the parts, never\n"
       "a typed result with its working in a comment. WHEN THE SOURCE GIVES A\n"
       "RANGE says a pick typed as a literal with its range in prose does not\n"
       "meet it. The worked cases: Earth's dipole tilt, which IGRF-13 does\n"
       "not print and which the store held at 9.6, a figure in no epoch of\n"
       "the cited source; its rate; and the outer belt's peak, a midpoint of\n"
       "the L = 4 to 5 band typed as a literal with the band in prose. Five\n"
       "documents by Claude Fable 5.1 and Claude Opus 5 on 2026-09-21, each\n"
       "tested against the checkers before the next was written; GPT 6\n"
       "reviewed one round. Handle L-322.\n"
       "v2.16 writes down how a stated uncertainty")),
    # Rule 2: the declared construction
    (b("seven. A DECLARED drawing condition (a chosen solar wind pressure, a\n"
       "chosen cut angle) is exact for counting: it is a choice, not a\n"
       "measurement, so all of its digits are known.\n"),
     b("seven. A DECLARED drawing condition (a chosen solar wind pressure, a\n"
       "chosen cut angle) is exact for counting: it is a choice, not a\n"
       "measurement, so all of its digits are known.\n"
       "\n"
       "**A DECLARED CONSTRUCTION is exact in the same way** (v2.17). A drawing\n"
       "value that is a stated rule over measured rows -- the midpoint of a\n"
       "sourced band, the top of a sourced range -- is a choice, not a\n"
       "measurement, and its `# Figures:` line names the rule and the rows:\n"
       "`exact -- declared construction: midpoint of <row>, <row>`. The\n"
       "checker accepts `exact` only on a row whose `# Status:` begins\n"
       "`declared` (not `declared pending`), with every named row in the\n"
       "expression; a `measured` or `derived` row cannot declare exact over a\n"
       "measured input. The export serves an exact row unrounded, so every\n"
       "consumer draws the same value. The alternative was measured before\n"
       "this was written: counted to its rows' one figure, the outer belt's\n"
       "4.5 exported as 4.0 for the gallery while the orrery drew 4.5 from\n"
       "the float -- two consumers, two rings. The construction is not a\n"
       "measurement and the hover does not print it as one: it shows the\n"
       "range from the rows and states the rule (When the source gives a\n"
       "range). The checker lists every declared construction by name in its\n"
       "output, so each use is seen. Earth's outer-belt peak is the case\n"
       "(L-322 C2).\n")),
    # Rule 3: rates and angles, after the approximate-relation paragraph
    (b("its inputs carry. This is a floor on honesty, not a licence to round to\n"
       "taste: the row must say WHICH approximation caps it and by roughly how\n"
       "much. (L-342, Fable's review of C1, Finding 3.)\n"),
     b("its inputs carry. This is a floor on honesty, not a licence to round to\n"
       "taste: the row must say WHICH approximation caps it and by roughly how\n"
       "much. (L-342, Fable's review of C1, Finding 3.)\n"
       "\n"
       "**A rate or other derivative row is written as the derivative\n"
       "expression over the rows, never as a difference of two evaluations**\n"
       "(v2.17). The difference form is counted by decimal place from the two\n"
       "evaluated values, whose places come from the largest inputs, so the\n"
       "quantities the rate rests on set no count and the row claims a\n"
       "precision it borrowed. Earth's dipole tilt rate is the case: as a\n"
       "one-year difference of two tilts it would carry the main field's\n"
       "places; as the derivative over the six IGRF-13 rows it carries three\n"
       "figures, set by the sum inside it, -0.0493 degrees per year.\n"
       "Time-rate rows use time-rate tokens (`nt_per_year`, `deg_per_year`).\n"
       "\n"
       "**An angle computed from a pure number never applies `degrees` to the\n"
       "result.** An inverse trigonometric function of a ratio, or a rate\n"
       "derived from one, comes out of the arithmetic as a bare number or an\n"
       "inverse time. The unit check reduces a ratio whose units cancel to a\n"
       "plain float before the function, so `degrees` of the result is a bare\n"
       "number declared in `deg`, a MISMATCH; `degrees` of an inverse time it\n"
       "refuses outright, CANNOT EVALUATE, which fails inside a closed slice.\n"
       "The row multiplies by the exact row `DEG_PER_RAD` instead, whose unit\n"
       "is `deg` and which carries the radian, so the unit check follows the\n"
       "chain to degrees, or degrees per time, with no equivalency. Both the\n"
       "tilt and its rate are written this way, and both were run through\n"
       "both checkers before this was written. `DEG_PER_RAD` has no store\n"
       "inputs, so neither checker judges it and its unit is asserted; the\n"
       "row says so in words, as a definition.\n")),
    # Show or cap: the snapshot of a moving quantity
    (b("  cap the count and say why on the row, as the Hill sphere's is in the\n"
       "  paragraph above. This decides which of the two answers applies.\n"),
     b("  cap the count and say why on the row, as the Hill sphere's is in the\n"
       "  paragraph above. This decides which of the two answers applies. It\n"
       "  also decides a snapshot of a quantity that moves (v2.17): where the\n"
       "  source publishes the rate, the store holds the rate's inputs and the\n"
       "  page shows the epoch and the rate beside the value; where it does\n"
       "  not, the count is capped to the place the movement over the model's\n"
       "  validity span supports. Earth's dipole tilt is the case: IGRF-13\n"
       "  prints the secular variation, so the tilt prints at its full count\n"
       "  with its epoch and its rate.\n")),
    # Rule 6: a whole the source defines from parts it prints
    (b("export lands and the gallery stops parsing the store (L-322 ruling 6);\n"
       "they revert to expressions at their slice visit.\n"),
     b("export lands and the gallery stops parsing the store (L-322 ruling 6);\n"
       "they revert to expressions at their slice visit.\n"
       "\n"
       "**Where a source prints the parts and states the relation that makes\n"
       "the whole, the whole is a derived row over measured rows for the\n"
       "parts** (v2.17) -- never a typed result with its working in a comment,\n"
       "which a closed slice does not accept (Rule 8 names that shape).\n"
       "IGRF-13 prints the three degree-1 coefficients and says the pole is\n"
       "computed from them, so Earth's dipole tilt is an expression over\n"
       "three coefficient rows; the stored 9.6 it replaced was in no epoch of\n"
       "the cited source.\n")),
    # Rule 7: replaced whole
    (b("**Rule 7. The declared count governs reporting; a display may show\n"
       "fewer, never more.** A hover formats to the served count or to a shorter\n"
       "readable count; a shorter display is not a precision claim. A display\n"
       "with more figures than the row declares is the failure.\n"),
     b("**Rule 7. A display prints the declared count, never more, and never\n"
       "chooses fewer** (v2.17). A hover formats to the served count. A display\n"
       "with more figures than the row declares is the failure. A display that\n"
       "reads as too many figures is a finding about the ROW, not the page:\n"
       "the row's count comes down under Rule 3 -- by the ceiling where an\n"
       "uncertainty is stated, or by a cap with the reason on the row where\n"
       "the relation is approximate and its mismatch cannot be shown -- and\n"
       "the page then prints the shorter count because the row declares it.\n"
       "The page never shortens on its own, because a shortening the row does\n"
       "not record is a judgment nobody can find later, and the served count\n"
       "is what every checker reads. One format exception, named where it\n"
       "occurs: a display of fixed width truncates a longer served count and\n"
       "says so in its comment; the gallery's AU line at min(3, count) is\n"
       "that case. A display that FORMATS by a fixed number of places or\n"
       "figures rather than by the served count is not that exception; it is\n"
       "a site to be listed and assigned when the rule reaches it, as the\n"
       "orrery's Earth hovers were at L-322 C2: 47 sites, four kinds, one\n"
       "ledger class with no automated coverage, and the four that print more\n"
       "than the row declares pulled into the build. (Until v2.17 this rule\n"
       "let a display show fewer with no method for choosing, and every use\n"
       "of that permission reached Tony as a readability call. Tony,\n"
       "2026-09-21: \"the basis should be in the skill not arbitrary.\")\n")),
    # When the source gives a range: the typed pick
    (b("prose, where it cannot be interpolated and drifts from the number beside\n"
       "it.\n"
       "\n"
       "## A Drawing Approximation Does Not Promote [CRITICAL]\n"),
     b("prose, where it cannot be interpolated and drifts from the number beside\n"
       "it.\n"
       "\n"
       "A pick typed as a literal with its range in `# Declared:` prose does\n"
       "not meet this section, however well the prose cites (v2.17): the range\n"
       "is rows, the pick is an expression over them -- a declared\n"
       "construction, Rule 2 -- and the display shows the range from those\n"
       "rows. Earth's outer-belt peak, typed 4.5 with its L = 4 to 5 band in\n"
       "prose and the band typed again as literal text in the orrery's own\n"
       "hover, was the corrected case at L-322 C2.\n"
       "\n"
       "## A Drawing Approximation Does Not Promote [CRITICAL]\n")),
]

# ------------------------------------------------------------- protocol
V367 = b(
    "v3.67 (September 22, 2026): No rule changed in this document. ONE\n"
    "skill bump, the second taken ahead of the C2 build, which is v3.55's\n"
    "ordering applied twice to one build.\n"
    "\n"
    "provenance-discipline 2.16 -> 2.17 (L-322). A DISPLAY NEVER CHOOSES A\n"
    "COUNT, AND THREE STORAGE FORMS ARE WRITTEN DOWN.\n"
    "\n"
    "THE QUESTION THAT STARTED IT WAS TONY'S. Asked whether Earth's dipole\n"
    "tilt should print 9.4 or 9.4105, the reviewing session offered a\n"
    "readability call. Tony, 2026-09-21: \"when it comes to a decision,\n"
    "what is the basis? the basis should be in the skill not arbitrary.\"\n"
    "There was none. Rule 7 let a display show fewer figures and said\n"
    "nothing about when, so every use of it reached the integrator, which\n"
    "is the failure Method Belongs to the Skill names. Rule 7 is replaced\n"
    "whole: a display prints the declared count; a number that reads as\n"
    "too many figures is a finding about the row, fixed under Rule 3 where\n"
    "it is recorded, never by the page. That takes item 9 -- the\n"
    "geocorona, LEO's inner edge, the outer belt -- off Tony's decision\n"
    "list, because each resolves on its row.\n"
    "\n"
    "THE TILT WAS THE WORKED CASE, AND IT WAS WRONG IN THE STORE. IGRF-13\n"
    "prints no tilt; it prints the three degree-1 coefficients and says the\n"
    "pole is computed from them. The stored 9.6 is in no epoch of the\n"
    "cited source, and the row's drift rate was off by a factor of ten.\n"
    "Three forms are now in the skill. A whole the source defines from\n"
    "parts it prints is a derived row over rows for the parts, never a\n"
    "typed result with its working in a comment. A rate is the derivative\n"
    "expression, never a difference of two evaluations, because the\n"
    "difference form takes its count from the largest inputs and not from\n"
    "the quantities the rate rests on. An angle computed from a pure\n"
    "number multiplies by the exact row DEG_PER_RAD instead of calling\n"
    "degrees, because the unit check sees a bare number and refuses the\n"
    "call -- found only when Opus ran the unit checker on the tilt, which\n"
    "nobody had done, including the session that had said the checkers\n"
    "accepted everything the tilt needed.\n"
    "\n"
    "THE OUTER BELT TAUGHT THE DECLARED CONSTRUCTION. Its peak is typed\n"
    "4.5 with its L = 4 to 5 band in prose, which When the source gives a\n"
    "range already did not allow. Making it an expression over two\n"
    "one-figure band rows met three rules at once: Rule 2 says a declared\n"
    "pick is exact, the checker counts an expression from its measured\n"
    "inputs, and the export rounds to the count -- and measured, that\n"
    "exported 4.0 for the gallery while the orrery drew 4.5 from the\n"
    "float, two consumers drawing two rings. Rule 2 now names a declared\n"
    "construction: exact as a rule, accepted by the checker only on a row\n"
    "whose status begins declared, served unrounded so every consumer\n"
    "draws the same value, and shown to the visitor as the range and the\n"
    "rule rather than as a measurement.\n"
    "\n"
    "EACH ROUND WAS TESTED BEFORE THE NEXT. Five documents on 2026-09-21,\n"
    "by Claude Fable 5.1 and Claude Opus 5 with one round reviewed by GPT\n"
    "6, and each one's proposals were run through the figures walker, the\n"
    "unit checker and the export on a throwaway copy of the store before\n"
    "the next was written. Three of Fable's own proposals failed those\n"
    "runs and were corrected in the next revision: a row that was at once\n"
    "an expression over measured rows and exact, a rate counted at two\n"
    "figures where the sum inside it carries three, and a function the\n"
    "checkers do not know. The reach of the new Rule 7 was enumerated\n"
    "before it was adopted, as The Braid requires: the gallery's Earth\n"
    "room gains no failure, and the orrery's Earth hovers carry 47 format\n"
    "sites on 35 lines, named by line in the rev2 addendum, of which four\n"
    "come into C2 and the rest are one ledger class with no automated\n"
    "coverage, stated as such so a closed slice is not read as covering\n"
    "them.\n"
    "\n"
    "THE OBLIGATION TRAVELS, as it always does. The session that cut this\n"
    "bump had 2.15 mounted, the protocol in its context having refreshed\n"
    "to 2.16 mid-session, which is the note owed to Stale Skill = Stop\n"
    "since the C2 manifest; it worked from the repo copy at 1f6e55a9 and\n"
    "said so. The next session confirms its loaded copy reads 2.17 before\n"
    "any provenance or store work, and that session is the C2 build, from\n"
    "documentation/BUILD_MANIFEST_L322_C2_magnetosphere_20260920.md with\n"
    "its section 17.\n"
    "\n"
    "The header stamp and the SHA anchor move with this entry.\n"
    "\n"
    "Version history: v3.64 moves down to\n"
    "documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three\n"
    "resident.\n"
    "\n"
)
V364_START = b"v3.64 (September 19, 2026): No rule changed in this document. ONE\n"
PROTO_TAIL = b"Functional for Claude, readable for human, signal preserved."
PROTO_EDITS = [
    (b("Tony Quintanilla, PE | Claude | v3.66 | September 21, 2026\n"),
     b("Tony Quintanilla, PE | Claude | v3.67 | September 22, 2026\n")),
    (b("Cut from a7014abb at https://github.com/tonylquintanilla/palomas_orrery\n"),
     b("Cut from 1f6e55a9 at https://github.com/tonylquintanilla/palomas_orrery\n")),
    (b("v3.66 (September 21, 2026): No rule changed in this document. ONE\n"),
     V367 + b("v3.66 (September 21, 2026): No rule changed in this document. ONE\n")),
]
HIST_ANCHOR = b("v3.66 made a fourth entry.)\n"
                "\n"
                "================================================================\n"
                "PART 2 -- LESSONS REMOVED FROM THE PROTOCOL AT v3.37\n")

# ------------------------------------------------------------- manifest
MANI_ANCHOR = b("  closing stamp carries both dates.\n"
                "\n"
                "---\n"
                "\n"
                "Written September 20, 2026, and revised September 21, 2026, with\n"
                "Anthropic's Claude Opus 5.\n")
MANI_S17 = b(
    "  closing stamp carries both dates.\n"
    "\n"
    "## 17. The tilt rounds of 2026-09-21, consolidated for the build\n"
    "\n"
    "Written September 22, 2026 by Claude Fable 5.1 at the 2.17 cut. Five\n"
    "documents in `documentation/` carry the working: the reply\n"
    "(`REPLY_L322_C2_dipole_tilt_method_fable_20260921.md`), three\n"
    "addendum revisions (`ADDENDUM_L322_C2_dipole_tilt_display_rule_fable\n"
    "_20260921.md`, `_rev2_`, `_rev3_`), Opus's two reviews and its note\n"
    "(`NOTE_L322_C2_rev3_check_opus_20260921.md`), and GPT 6's review.\n"
    "Where this section and an earlier section disagree, this section\n"
    "governs. Rules named below are provenance-discipline 2.17.\n"
    "\n"
    "### 17.1 Rows added or changed, beyond section 4\n"
    "\n"
    "| Row | Form | Figures | Read |\n"
    "| --- | --- | --- | --- |\n"
    "| `DEG_PER_RAD` (new) | `180.0 / np.pi`, unit `deg` | exact -- a definition; no store inputs, so its unit is asserted, and the row says so | none |\n"
    "| `EARTH_IGRF13_G10_NT`, `_G11_NT`, `_H11_NT` (new) | measured, 2020.0 column: -29404.8, -1450.9, 4652.5 | 6, 5, 5 -- the file prints the 2020.0 column to 0.1 nT, its REPORTING resolution (definitive epochs print to 0.01); Lowes (2000), the error budget the paper names, not opened, recorded as a class | NOAA `igrf13coeffs.txt`, opened 2026-09-21 by Claude Opus 5 |\n"
    "| `EARTH_IGRF13_G10_SV_NT_PER_YEAR`, `_G11_SV_`, `_H11_SV_` (new) | measured, 2020-25 column: 5.7, 7.4, -25.9; token `nt_per_year` | 2, 2, 3 | same file, same read |\n"
    "| `EARTH_DIPOLE_TILT_DEG` | `np.arctan(np.sqrt(G11**2 + H11**2) / abs(G10)) * DEG_PER_RAD`, over the three main-field rows | 5 -- set by G11 and H11 (5); 9.4105 at epoch 2020.0 | none; derived. Source: Alken et al. (2021), full text, for the RELATION -- the poles are computed from the degree-1 coefficients |\n"
    "| `EARTH_DIPOLE_TILT_RATE_DEG_PER_YEAR` (new) | the derivative, section 17.2; token `deg_per_year` | 3 -- set by the sum `G11*G11' + H11*H11'`, good to thousands; -0.0493 | none; derived |\n"
    "| `EARTH_VAN_ALLEN_OUTER_BAND_LOW_L`, `_HIGH_L` (new) | measured, 4 and 5, unit `l_shell` | 1 each | builder opens Li et al. (2025) sec. 1 at the row's par.nsf.gov link; Li et al. (2015) and Kellerman (2014, via arXiv 1809.00902) as `# Source+:` |\n"
    "| `EARTH_VAN_ALLEN_OUTER_RADII` | `(LOW + HIGH) / 2`; status `declared` naming the rule | exact -- declared construction: midpoint of the two band rows | none; declared |\n"
    "\n"
    "The tilt row's note loses its sentences on rounding to a tenth, on\n"
    "\"0.05 deg per decade\" (the source gives 0.05 per YEAR), and on NOAA's\n"
    "WMM figures, which were never opened (A Breadcrumb Must Not Cite).\n"
    "Its words say epoch 2020.0 and IGRF-13 by name; IGRF-14 (June 2026)\n"
    "is recorded as a re-sourcing, not done. Tokens `nt_per_year`\n"
    "(nT/yr) and `deg_per_year` (deg/yr) join 4.1, each mapped to its\n"
    "astropy unit.\n"
    "\n"
    "### 17.2 The rate row, as it passed both checkers\n"
    "\n"
    "```python\n"
    "EARTH_DIPOLE_TILT_RATE_DEG_PER_YEAR = (\n"
    "    (abs(EARTH_IGRF13_G10_NT)\n"
    "     * (EARTH_IGRF13_G11_NT * EARTH_IGRF13_G11_SV_NT_PER_YEAR\n"
    "        + EARTH_IGRF13_H11_NT * EARTH_IGRF13_H11_SV_NT_PER_YEAR)\n"
    "     / np.sqrt(EARTH_IGRF13_G11_NT**2 + EARTH_IGRF13_H11_NT**2)\n"
    "     + np.sqrt(EARTH_IGRF13_G11_NT**2 + EARTH_IGRF13_H11_NT**2)\n"
    "     * EARTH_IGRF13_G10_SV_NT_PER_YEAR)\n"
    "    / (EARTH_IGRF13_G11_NT**2 + EARTH_IGRF13_H11_NT**2\n"
    "       + EARTH_IGRF13_G10_NT**2)\n"
    ") * DEG_PER_RAD\n"
    "```\n"
    "\n"
    "Opus ran this and the tilt on a throwaway store at `a318b3ec`: unit\n"
    "check OK (deg_per_year, -0.0492766; deg, 9.41053), figures check\n"
    "within what the inputs support (3; 5). `np.degrees` on either FAILS\n"
    "the unit check and is not used. The second term is `- H * d|g10|/dt`\n"
    "with `d|g10|/dt = -g10'` for negative g10, hence the plus sign.\n"
    "\n"
    "### 17.3 The checker, beyond 4.7\n"
    "\n"
    "- `test_derived_figures.py` accepts `exact` on a row whose `# Status:`\n"
    "  begins `declared` (not `declared pending`) when every row its\n"
    "  `# Figures:` line names is in the expression; it lists every such\n"
    "  declared construction by name in its output; and it is shown\n"
    "  failing on a `measured` row declaring exact over a measured input.\n"
    "\n"
    "### 17.4 Hovers, beyond section 6\n"
    "\n"
    "- Both belts, tilt line: the served tilt at its count, the epoch and\n"
    "  the served rate, all from the store: \"tilted 9.4105 degrees from\n"
    "  it (IGRF-13, epoch 2020.0), decreasing about 0.0493 degrees a\n"
    "  year\". Words Tony's. The renderer's typed \"(IGRF-13, epoch\n"
    "  2020-2025)\" goes; the epoch is served.\n"
    "- Outer belt: the line \"Drawn at 4.5 Earth radii ... = 28,701.615 km\n"
    "  (0.000192 AU)\" is replaced by the rule and the band from served\n"
    "  rows: \"Drawn at the midpoint of the L = 4 to 5 band in which the\n"
    "  sources place the outer belt's greatest intensity\". A declared\n"
    "  construction is not printed as a measurement, so it has no km line.\n"
    "  The existing \"where the measured particle flux peaks\" wording is\n"
    "  the class already in section 11; Tony's words.\n"
    "- Section 13, item 9 is removed: the geocorona and LEO's inner edge\n"
    "  print as their rows declare, and the outer belt resolves above.\n"
    "\n"
    "### 17.5 Orrery display sites that come into C2\n"
    "\n"
    "- `earth_visualization_shells.py`, the four `:.4g` sites on the two\n"
    "  standoffs (lines 791, 801, 882, 950 at `a318b3ec`): after C2 they\n"
    "  print the new expressions to four figures, more than the declared\n"
    "  three. They format by the export's declared count instead.\n"
    "- `earth_visualization_shells.py` line 1011, the typed \"L = 4 to 5\n"
    "  band\": printed from the two band rows.\n"
    "- `planet_visualization_utilities.py`, the `PLANET_DIPOLE['Earth']`\n"
    "  note and hover strings typing \"~9.6 deg\" and the drift, and the\n"
    "  comment near line 693; `earth_visualization_shells.py` comments\n"
    "  near lines 869 and 1046 naming 9.6.\n"
    "\n"
    "### 17.6 Reads already done, and the one that was Tony's\n"
    "\n"
    "The Opus session of 2026-09-21 read, and the C2 read record takes\n"
    "from `NOTE_L322_C2_rev3_check_opus_20260921.md` without repeating:\n"
    "Baker (2018) sec. 2; Meredith (2014) intro para. 1 (via the Wiley\n"
    "page, the NORA PDF refusing); Li, Tu et al. (2024) intro para. 1;\n"
    "Alken et al. (2021) full text; the NOAA file; and Alken Table 4's\n"
    "2020.0 row via a ResearchGate copy, north geomagnetic pole at 80.65\n"
    "N, -72.68 E, which the coefficients reproduce as 80.6512, -72.6797.\n"
    "That last read was the \"For Tony to read\" entry the reply proposed;\n"
    "it is done, and the section is expected empty again. NOT yet read:\n"
    "the magnetotail (NTRS 19830066648) and the outer-belt band sources,\n"
    "which the builder opens.\n"
    "\n"
    "### 17.7 Ledger classes added to section 11\n"
    "\n"
    "- The orrery's Earth display sites format by fixed width: 47 sites on\n"
    "  35 lines of `earth_visualization_shells.py`, four kinds, named by\n"
    "  line in the rev2 addendum. NO automated coverage: no checker reads\n"
    "  orrery display formatting, so a closed Earth slice does not cover\n"
    "  them. A helper that formats a row by the export's declared count is\n"
    "  the follow-on's mechanism, not designed here.\n"
    "- A count taken from a file's print resolution where a published\n"
    "  error budget exists and is unopened (IGRF-13 and Lowes 2000).\n"
    "- Declared picks with their range in prose on other bodies (the Sun's\n"
    "  helmet cusp, \"top of measured 2-4 range\").\n"
    "- Rate rows and angle rows on other bodies (Earth's pole at Stage D,\n"
    "  the Moon's node) follow the two Rule 3 forms.\n"
    "- The two static gallery card exports typing \"~9.6 deg\" twice each,\n"
    "  and `documentation/fixture_hovers_cdfa74c3.json` if nothing\n"
    "  references it.\n"
    "- IGRF-14 as a re-sourcing of the six coefficient rows.\n"
    "\n"
    "### 17.8 Section 12 and section 14, amended\n"
    "\n"
    "Section 12: not \"any new measured or declared constant\" -- a row that\n"
    "feeds a drawn value is in bound whatever its count (The Read Field's\n"
    "scope sentence). C2 adds eight measured rows and one exact definition\n"
    "under that principle. Section 14 gains: the figures checker's output\n"
    "names the outer-belt peak as a declared construction; both belt\n"
    "hovers print the tilt, epoch and rate from served rows; the four\n"
    "`:.4g` sites format by the declared count.\n"
    "\n"
    "---\n"
    "\n"
    "Written September 20, 2026, and revised September 21, 2026, with\n"
    "Anthropic's Claude Opus 5. Section 17 added September 22, 2026 with\n"
    "Anthropic's Claude Fable 5.1.\n"
)


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
    for path in (SKILL, PROTO, HIST, MANI):
        with open(path, "rb") as f:
            raw[path] = f.read()
        crlf[path] = b"\r\n" in raw[path]
        lf[path] = raw[path].replace(b"\r\n", b"\n")
    if b"Skill version: 2.17 |" in lf[SKILL]:
        fail("ERROR: SKILL.md already reads 2.17 -- this patch has been "
             "applied. Nothing to do.")
    for path in (SKILL, PROTO, HIST, MANI):
        got = fingerprint(path, lf[path])
        if got != EXPECT[path]:
            fail("ERROR: %s is not the file this patch was built on "
                 "(content md5 %s, expected %s). Pull or discard local "
                 "changes and check the orrery is at 1f6e55a9."
                 % (path, got, EXPECT[path]))
    print("base ok: all four files match 1f6e55a9 by content")

    new = {}
    new[SKILL] = apply_edits(SKILL, lf[SKILL], SKILL_EDITS)

    p = lf[PROTO]
    if p.count(V364_START) != 1 or p.count(PROTO_TAIL) != 1:
        fail("ANCHOR FAIL in %s: v3.64 entry or closing line not found once"
             % PROTO)
    i = p.index(V364_START)
    j = p.index(PROTO_TAIL)
    if not i < j:
        fail("ANCHOR FAIL in %s: v3.64 entry is not the last resident entry"
             % PROTO)
    v364 = p[i:j]  # the whole entry, ending with its blank line
    if not v364.endswith(b"resident.\n\n"):
        fail("ANCHOR FAIL in %s: v3.64 entry does not end where expected"
             % PROTO)
    p = p[:i] + p[j:]
    print("ok   %s: v3.64 entry lifted out (%d bytes)" % (PROTO, len(v364)))
    new[PROTO] = apply_edits(PROTO, p, PROTO_EDITS)

    h = lf[HIST]
    if h.count(HIST_ANCHOR) != 1:
        fail("ANCHOR FAIL in %s: end of PART 1 not found once" % HIST)
    moved = (b"v3.66 made a fourth entry.)\n\n" + v364
             + b("(Moved down from the resident protocol on 2026-09-22 when\n"
                 "v3.67 made a fourth entry.)\n"
                 "\n"
                 "================================================================\n"
                 "PART 2 -- LESSONS REMOVED FROM THE PROTOCOL AT v3.37\n"))
    new[HIST] = h.replace(HIST_ANCHOR, moved)
    print("ok   %s: v3.64 entry placed at the end of PART 1" % HIST)

    new[MANI] = apply_edits(MANI, lf[MANI], [(MANI_ANCHOR, MANI_S17)])

    # gates before anything is written
    for path, data in new.items():
        try:
            data.decode("ascii")
        except UnicodeDecodeError:
            fail("ERROR: %s would contain non-ASCII text" % path)
        if not data.endswith(b"\n"):
            fail("ERROR: %s would not end with a line break" % path)
    if new[PROTO].count(b"v3.64 (September 19, 2026)") != 0:
        fail("ERROR: v3.64 would still be resident")
    if new[HIST].count(b"v3.64 (September 19, 2026)") != 1:
        fail("ERROR: v3.64 would not be in the archive exactly once")
    if new[SKILL].count(b"(v2.17)") != 7:
        fail("ERROR: the skill would carry %d v2.17 marks, expected 7"
             % new[SKILL].count(b"(v2.17)"))

    for path, data in new.items():
        out = data.replace(b"\n", b"\r\n") if crlf[path] else data
        with open(path, "wb") as f:
            f.write(out)
    print("written: %s, %s, %s, %s (line endings kept as found)"
          % (SKILL, PROTO, HIST, MANI))
    print("stamps updated: SKILL.md version line, cut-from list, date and "
          "v2.17 paragraph; protocol header v3.67, cut-from 1f6e55a9, "
          "history entry v3.67; archive move-down note; manifest section 17")

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
    if r.returncode != 0 or not row or b" 2.17 " not in row[0]:
        print("\nWARNING: the four files ARE written, but the Skill Manifest "
              "table did not come out reading 2.17. Do not commit. Run the "
              "orrery maintenance run and look at its Skill manifest line; if "
              "it still disagrees, Discard Changes in GitHub Desktop and tell "
              "Claude what skills_index.py printed.")
        sys.exit(1)
    print("Skill Manifest now reads provenance-discipline 2.17")

    print("""
patch applied.

  1. Run the orrery maintenance run (python orrery_maintenance_run.py,
     or its Run button). Its Skill manifest line should read 2.17.
  2. Move this script to documentation/.
  3. In GitHub Desktop: commit SKILL.md, PROJECT_INSTRUCTIONS.md,
     PROJECT_INSTRUCTIONS_HISTORY.md, the manifest and this script
     TOGETHER, and push. Report the SHA.
  4. Settings > Skills: reinstall provenance-discipline. This session
     cannot see the reinstall; the NEXT session confirms it loaded 2.17
     as its first act, and that session is the C2 build.
""")


if __name__ == "__main__":
    main()
