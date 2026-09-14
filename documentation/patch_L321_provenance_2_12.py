"""
patch_L321_provenance_2_12.py

Bumps skills/provenance-discipline/SKILL.md from 2.11 to 2.12.

HOW TO RUN
    Save into the orrery repo ROOT (beside LEDGER_CONSOLIDATED.md),
    open in VS Code, click Run.
    Equivalent: python patch_L321_provenance_2_12.py
    Archive it to documentation/ once it has run.

WHY
    The L-321 cross-check round produced five method rules, and L-325
    parked a sixth for this bump. They are drafted, reviewed and ruled
    in documentation/DRAFT_provenance_discipline_2_12_field_notes_20260913.md.
    The handoff makes this bump the session's first action, ahead of
    L-305 item 7, so the gate checks a matching manifest instead of a
    promise travelling in a handoff.

WHAT IT CHANGES -- one file, seven edits, all-or-nothing
    skills/provenance-discipline/SKILL.md
      1. version line 2.11 -> 2.12, SHA list, date, v2.12 paragraph
      2. The Access Standard gains A Source Names What Was Opened,
         Not What It Cites [CRITICAL]
      3. Review-Repair step 1 gains A Link Is an Object, Not Text
         [QUALITY] and the three things the prompt must require
      4. the Gemini roster cell gains its tier qualifier
      5. Model Roles gains the two roster corrections
      6. Worksheet Types gains the row-job vocabulary and schema,
         A Negative Verdict Shows Its Search [CRITICAL], and
         Route the Effort Tier by Job Type [QUALITY]
      7. The Store Carries the Verified Figure gains A Derived Row
         Stores the Figure Its Sources Support [CRITICAL]

BEYOND THE DRAFT -- read this before running
    Edit 6 adds the [CITATION] / [DISCOVERY] row-job vocabulary and
    the ten-column schema, neither of which is in the skill today.
    The draft's notes 1 and 5 both use "DISCOVERY row" as though the
    skill defined it. It does not -- the term was defined in the L-321
    prompt and never travelled. The definitions here are transcribed
    from L321_slice1_prompts_rev3_20260912.md and the schema from the
    table the three worksheets actually ran, not composed.

    NOT touched: the "eight different column layouts" sentence. The
    count is history and this schema does not change it.

PERMANENT HALF
    The SKILL.md edits. The script is one-shot; the fingerprint it
    guards on describes a tree that stops existing the moment it runs.

AFTER IT RUNS
    1. python skills_index.py   (regenerates the manifest zone in
       PROJECT_INSTRUCTIONS.md -- do NOT hand-edit that zone)
    2. protocol version entry v3.58 + ledger row: separate patch
    3. reinstall to the account profile, Settings > Skills
    A reinstall cannot be verified from inside the session that makes
    it, so the NEXT session confirms its loaded copy reads 2.12 before
    provenance work.

UNDO
    Discard Changes in GitHub Desktop.

Built on orrery bfc0505e070e70254892109e04b0cefbccbdd6bb at
https://github.com/tonylquintanilla/palomas_orrery

Written September 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

TARGET = os.path.join("skills", "provenance-discipline", "SKILL.md")
FINGERPRINT = "5c163d28b1536038b39e3f7a3b558d93"

# ---------------------------------------------------------------- edits
# Bottom-up: highest position in the file first.

EDITS = []

# 7. after The Store Carries the Verified Figure
EDITS.append((
b"""## No Shadow Constants [CRITICAL]
""",
b"""### A Derived Row Stores the Figure Its Sources Support [CRITICAL]

A derived constant stores the figure its inputs actually support, not
the arithmetic result. Sixteen digits on a value uncertain in the first
decimal is calculator output, not precision. The arithmetic stays
recorded on the row, so it remains auditable, and a check recomputes
the row from the inputs its Status line names and FAILS when the
rounding stops holding.

An expression recomputes silently when an input moves, which is a
published number changing with nobody looking. A literal plus a test
announces instead.

**Scope: this governs rows whose inputs are DECLARED CONSTANTS.** L-314
may serve solar wind speed and pressure from the cache, and a stored
literal guarded by a test that fails every time the wind changes is a
test nobody reads. Re-examine when L-314 is designed.

(Tony's ruling, 2026-09-12, stopping two standoff values from being
copied into the gallery config at full stored precision: "the store
should only carry significant digits not what the calculator
generates." Both rows already declared what to report and stored
something else. Handle L-325; the scope paragraph is his own ledger
note under L-314.)

## No Shadow Constants [CRITICAL]
"""))

# 6c. Worksheet Types -- notes 1 and 5 at the end of the section
EDITS.append((
b"""### Quoting a Worksheet Is Transcription, Not Interpretation [CRITICAL]
""",
b"""### A Negative Verdict Shows Its Search [CRITICAL]

UNSOURCED is the one verdict that cannot fail. Every other token points
at a document somebody can open and check. A negative points at
nothing, so a checker that ran two queries and a checker that ran
twenty return the identical cell, and the worksheet cannot tell them
apart.

So a DISCOVERY row carries a SEARCH LOG: the queries actually run, the
terms tried, and where it looked. A negative is then inspectable -- you
read the query list and see the hole.

Say it in the prompt as a requirement of the row, not a courtesy: "no
source states this" is a claim about the search, and a search nobody
can see is a claim nobody can check.

(L-321, 2026-09-13. A Medium-tier return marked three belt-extent rows
UNSOURCED. Three open full-text sources state those figures --
Koskinen and Kilpua 2022, Meredith et al. 2014, Li, Tu et al. 2024 --
and two later checkers found them. The verdict was honest and wrong,
and nothing in the worksheet could have caught it. This is A Check That
Cannot Fail Is Not Passing, at the worksheet layer.)

### Route the Effort Tier by Job Type [QUALITY]

A DISCOVERY row asks a checker to establish a NEGATIVE across the
literature. That is bounded by how long it keeps looking, which is what
the effort tier buys. A CITATION row is bounded by construction -- open
the named paper, find the sentence, stop -- and is cheap at any tier.

So route DISCOVERY rows to the highest tier available and leave
CITATION rows at the working tier.

(Tony's ruling, 2026-09-13. Recorded as a ruling rather than as a
measured result, because the experiment that would have proved it is
no longer runnable: every instance in the Project has seen the answer.
Supporting evidence only -- a High-tier leg on worksheet 1 opened Shue
in full on Russell's UCLA site after Wiley blocked it, dropped one row
to APPROX and added ISEE-3 to another, where the Medium leg had done
none of those.)

### Quoting a Worksheet Is Transcription, Not Interpretation [CRITICAL]
"""))

# 6a/6b. Worksheet Types -- schema and row jobs
EDITS.append((
b"""Both types use the same worksheet table format:

| # | Claim/Constant | Code value | Your value | Source | Value correct? | Citation correct? | Notes |
""",
b"""Both types use the same worksheet table format:

| # | Job | Claim | Code value | Your value | Source unit | Source (URL opened, access word) | Value correct? | Citation correct? | Notes |

**Every row says which job it is.** The two types above describe what a
whole worksheet is FOR; a real worksheet usually needs both, and the
marker is per row:

    [CITATION] -- the string names a source for this claim. Go to that
    source and confirm it states the claim, at the stated precision.
    Then, separately, check the value against an accessible primary
    source of your own choosing.

    [DISCOVERY] -- the string states a figure that may have no source
    at all. Do not assume one exists, and do not reconcile it with any
    other figure in the worksheet. Find whether an accessible source
    states it, say which, and if none does, say that. UNSOURCED is a
    valid and useful answer.

Do not treat a DISCOVERY row as a CITATION row with a missing citation.
They ask different questions, they fail differently, and per Route the
Effort Tier by Job Type below they are not worth the same effort tier.

`Source unit` is not decoration. The same belt edge reads 1.1 to 2 in
Earth radii and 1,000 to 6,000 in kilometres, and a row that omits the
unit cannot be compared against the code value at all.
"""))

# 5. Model Roles -- the two roster corrections
EDITS.append((
b"""### The Two-Dispatch Rule [CRITICAL]
""",
b"""**Gemini: the tier decides whether it can check citations at all.**
Flash 3.8 cannot fetch; it declared so and returned a table with every
Source cell WALLED. Pro 3.1 with Extended Thinking fetches -- it opened
three PDFs in full. So the constraint recorded at L-276 is about the
interface and the tier, not about Gemini, and a Flash tier is not a
citation checker at any prompt quality.

**A checker inside the Project is not independent for a rerun.** Once
an instance has transcribed or reviewed a return, it has seen the
answer, and past chats are searchable, so a fresh session in the same
Project does not restore independence. A rerun meant to test search
depth has to go outside the Project or not happen.

### The Two-Dispatch Rule [CRITICAL]
"""))

# 4. Gemini roster cell
EDITS.append((
b"""| Gemini | Domain knowledge, structural/philosophical dialogue.""",
b"""| Gemini | Domain knowledge, structural/philosophical dialogue. Fetching is TIER-DEPENDENT -- see the roster note below."""))

# 3. Review-Repair step 1 -- the link rule and the prompt requirements
EDITS.append((
b"""**Why the worksheet format matters for every checker.**""",
b"""### A Link Is an Object, Not Text [QUALITY]

Ask for bare URLs inside a code block. A hyperlink pasted out of a chat
interface arrives as a chip carrying no address, and the loss is
silent: source names and access words survive, addresses do not. A
checker asked afterwards to reprint them has nothing left to reprint.

But the paste is not the only artifact. KEEP THE FILE THE CHECKER
EXPORTED. An export preserves addresses a paste destroys, so the
authored file is the record and any transcription is derived from it;
where the two disagree, the authored file wins.

(L-321, 2026-09-13. Three returns lost every URL in transfer and the
checker could not recover them. Twenty addresses came back anyway, out
of its own exported markdown, after the recommendation to delete the
authored copies as redundant was declined. One of those addresses
matched, character for character, a URL an independent search pass had
reached without seeing it.)

### Three Things the Prompt Must Require [QUALITY]

These are prompt text, not habits anyone has to remember.

1. **Bare URLs inside a code block**, for the reason above.
2. **A pre-flight.** Before any row, the checker opens one known
   open-access URL and quotes a sentence from it. A checker that cannot
   fetch is then visible in one exchange instead of in a finished table
   of WALLED cells.
3. **A response header naming the MODEL and the EFFORT TIER.** The
   tier decides what the return is worth -- see the roster note under
   Model Roles -- so a return that does not name it cannot be scored.
   Tony's filing convention carries both in the filename.

**Why the worksheet format matters for every checker.**"""))

# 2. The Access Standard -- what was opened
EDITS.append((
b"""**When a source fails access, re-home the citation to an accessible""",
b"""**A source names what was OPENED, not what it cites.** The Source cell
records the document the checker opened. Not the paper that document
cites for the claim, and not what the checker believes the document to
be.

The failure is invisible without a second fetch: right URL, right
access word, right figure, wrong attribution. A row can be entirely
correct about the literature and still send the next session to a paper
nobody read.

So the row quotes the TITLE AND AUTHOR LIST AS PRINTED in the document
opened. One field, mechanical, and it fails visibly when a checker is
reconstructing from memory instead of reading a title page. Where the
figure is background the document passes on from earlier work, that
earlier work is recorded as the next layer down, not as the source.

(L-321, 2026-09-13. A checker returned two correct extents and named
Usanova 2014 and Ganushkina 2011. The PDFs at those URLs are Meredith
et al. 2014 and Li, Tu et al. 2024, each citing the named paper in its
introduction. Two of three load-bearing rows; the third had opened a
paper that cites the one it was asked to check.)

**When a source fails access, re-home the citation to an accessible"""))

# 1b. date
EDITS.append((
b"""| September 8, 2026
""",
b"""| September 14, 2026
"""))

# 1a. version line + SHA list + v2.12 paragraph
EDITS.append((
b"""Skill version: 2.11 | Cut from palomas_orrery @ 159c5a2c (v2.11),
earlier @ 071a0a65 (v2.10),
""",
b"""Skill version: 2.12 | Cut from palomas_orrery @ bfc0505e (v2.12),
earlier @ 159c5a2c (v2.11), @ 071a0a65 (v2.10),
"""))

EDITS.append((
b"""v2.11 adds A Drawing Approximation Does Not Promote [CRITICAL],""",
b"""v2.12 adds five rules from the L-321 cross-check round and one
carried from L-325's Gap. Worksheet Types gains the row-job
vocabulary the round actually ran -- [CITATION] and [DISCOVERY] --
with the schema that carries it, and two rules that depend on it: A
Negative Verdict Shows Its Search [CRITICAL], because UNSOURCED is
the one token pointing at no document anybody can open, and Route
the Effort Tier by Job Type [QUALITY], Tony's ruling of 2026-09-13.
The Access Standard gains a source names what was OPENED, after a
checker returned the right URLs under the wrong author names. Step 1
of the Review-Repair Protocol gains A Link Is an Object, Not Text
[QUALITY] and the three things the prompt must require. The roster
records that Gemini's fetching is tier-dependent, so L-276's
constraint is about the interface and the tier rather than the
vendor, and that a checker inside the Project is not independent for
a rerun. A Derived Row Stores the Figure Its Sources Support
[CRITICAL] joins The Store Carries the Verified Figure, closing the
Gap L-325 parked for this bump. Handles L-321, L-325, L-314.
v2.11 adds A Drawing Approximation Does Not Promote [CRITICAL],"""))


# ---------------------------------------------------------------- run
def fail(msg):
    print("ERROR: " + msg)
    sys.exit(1)


def main():
    if not os.path.exists(TARGET):
        fail("%s not found. Run this from the orrery repo ROOT, the folder\n"
             "       that holds LEDGER_CONSOLIDATED.md and skills/." % TARGET)

    with open(TARGET, "rb") as f:
        raw = f.read()

    # Line Endings Are Not Content: fingerprint the LF-normalised bytes.
    lf = raw.replace(b"\r\n", b"\n")
    actual = hashlib.md5(lf).hexdigest()
    if FINGERPRINT != "PLACEHOLDER" and actual != FINGERPRINT:
        fail("%s does not match the tree this patch was built against.\n"
             "       expected md5 %s\n"
             "       found    md5 %s\n"
             "       Pull the repo at bfc0505e, or the patch has already run."
             % (TARGET, FINGERPRINT, actual))

    # Check every anchor BEFORE writing anything.
    work = lf
    for i, (old, new) in enumerate(EDITS, 1):
        n = work.count(old)
        if n != 1:
            fail("ANCHOR FAIL edit %d: found %d matches, expected 1.\n"
                 "       %r" % (i, n, old[:70]))
        work = work.replace(old, new, 1)

    # Encoding gate on the result: ASCII only, LF only.
    if b"\r" in work:
        fail("result carries CR bytes; expected LF only.")
    bad = sorted(set(c for c in work if c > 127))
    if bad:
        fail("result carries non-ASCII bytes: %r" % bad[:8])

    with open(TARGET, "wb") as f:
        f.write(work)

    print("ok  9 edits applied to %s" % TARGET)
    print("ok  version line reads 2.12")
    print("patch applied")
    print("")
    print("Next: python skills_index.py   (regenerates the manifest zone;")
    print("      do NOT hand-edit it), then the v3.58 protocol entry and")
    print("      ledger row, then reinstall in Settings > Skills.")


if __name__ == "__main__":
    main()
