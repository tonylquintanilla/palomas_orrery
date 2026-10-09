#!/usr/bin/env python3
"""
patch_L418_3_split_build_20261008.py -- splits provenance-discipline
(L-418, the long skills' contents, history and split).

HOW TO RUN: save this file in the orrery folder (the one holding
PROJECT_INSTRUCTIONS.md and LEDGER_CONSOLIDATED.md), open it in VS Code
and click Run. From a terminal the command is

    python patch_L418_3_split_build_20261008.py

It asks nothing. It reads every file first, checks each one is the
version it was built against, builds everything in memory, and writes
only if every check passed. Then it runs skills_index.py twice -- once to
write the read plans and the manifest, once with --check -- and prints
both.

WHAT IT DOES

1. provenance-discipline 2.26 -> 2.27. The relay procedure (the
   Review-Repair Protocol) moves out to a new skill,
   provenance-cross-check 1.0, with three of its reference sections in
   skills/provenance-cross-check/references/worksheets.md. Rules 1 to 8
   of the figure count move to references/figures.md and the field
   notes to references/field-notes.md, inside provenance-discipline's
   folder. The withdrawn derived-row rule and the v2.24 version entry
   move to documentation/SKILL_HISTORIES.md.
   PHASE 1 moves the text and checks every moved section arrived
   character for character (line endings aside). PHASE 2 makes the
   listed edits -- L-371 (the Sun room's served numbers), L-390 (the
   conversion marker), L-252 (the checker's fourth outcome), pointers
   to sections now in another file, and examples naming rows that have
   since changed -- and prints each one before and after. The final
   check proves each section now equals its original with exactly those
   edits applied, and nothing else.
2. ledger-and-session-records 1.17 -> 1.18: the read plan and reference
   files recorded as conventions; the Anchor Requirement names
   provenance-cross-check for review prompts; its v1.15 entry moves to
   SKILL_HISTORIES.md.
3. skills_index.py: the read plan, the reference-file check, and the
   annotation-example check reading reference files.
4. PROJECT_INSTRUCTIONS.md v3.86; v3.83 moves to
   documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1.
5. LEDGER_CONSOLIDATED.md, documentation/WHERE_WE_ARE.md (by section,
   nothing below the run-record marker) and the session's handoff.

SUCCESS: one "ok" line per edit, the phase checks, "patch applied", and
skills_index.py ending "OK: 12 skills parsed".
FAILURE: "ERROR:" or "ANCHOR FAIL:" and "NOTHING was written."
Running it a second time refuses and writes nothing.
Undo is Discard Changes in GitHub Desktop.

WHAT IS PERMANENT: the new skill folder and the two reference files,
the read plans, and skills_index.py's new checks. The script itself is
spent once it has run; move it to documentation/.

Built on orrery BASE_SHA at https://github.com/tonylquintanilla/palomas_orrery
(branch main). Written October 8, 2026 with Anthropic's Claude Opus 5.5.
"""
import hashlib
import os
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent
BASE_SHA = 'b0b3df82'
TODAY = '2026-10-08'

PD = 'skills/provenance-discipline/SKILL.md'
PD_FIG = 'skills/provenance-discipline/references/figures.md'
PD_FN = 'skills/provenance-discipline/references/field-notes.md'
XC = 'skills/provenance-cross-check/SKILL.md'
XC_WS = 'skills/provenance-cross-check/references/worksheets.md'
LSR = 'skills/ledger-and-session-records/SKILL.md'
SI = 'skills_index.py'
PI = 'PROJECT_INSTRUCTIONS.md'
PIH = 'documentation/PROJECT_INSTRUCTIONS_HISTORY.md'
SH = 'documentation/SKILL_HISTORIES.md'
LEDGER = 'LEDGER_CONSOLIDATED.md'
WWA = 'documentation/WHERE_WE_ARE.md'

# Content fingerprints (LF) of the files this patch replaces in whole or
# edits by line position. Tony does not annotate these, so a whole-file
# fingerprint is safe for them. The ledger, Where We Are and the two
# history files are checked only at the lines edited (L-419).
BASE_MD5 = {
    PD: '382fa81bb18d772d1a3b67eb784ec3c3',
    LSR: 'abc3d6f9a6a29adc77c46b838feed3bb',
    SI: 'db694a22fcda3b1eb469bf5843c94554',
}


class Refuse(Exception):
    pass


def read_lf(rel):
    path = ROOT / rel
    if not path.is_file():
        raise Refuse(f"ERROR: {rel} not found. Run this from the orrery "
                     f"folder.")
    raw = path.read_bytes()
    try:
        text = raw.decode('utf-8')
    except UnicodeDecodeError:
        raise Refuse(f"ERROR: {rel} is not UTF-8.")
    crlf = '\r\n' in text
    return text.replace('\r\n', '\n'), crlf


def md5(text):
    return hashlib.md5(text.encode('utf-8')).hexdigest()


LOG = []


def say(line):
    LOG.append(line)
    print(line)


def edit(text, old, new, rel, label, count=1, show=False):
    n = text.count(old)
    if n != count:
        raise Refuse(f"ANCHOR FAIL: {rel}: {label}: expected {count} "
                     f"match(es), found {n}.\n  anchor starts: "
                     f"{old[:90]!r}")
    say(f"ok  {rel:52s} {label}")
    if show:
        for tag, block in (('before', old), ('after ', new)):
            for line in block.strip('\n').split('\n'):
                print(f"      {tag} | {line}")
            print()
    return text.replace(old, new)


def ascii_check(rel, text):
    bad = [i for i, ch in enumerate(text) if ord(ch) > 127]
    if bad:
        line = text.count('\n', 0, bad[0]) + 1
        raise Refuse(f"ERROR: {rel} would hold {len(bad)} non-ASCII "
                     f"character(s), the first on line {line}.")


# ============================================================
# PROVENANCE-DISCIPLINE: WHERE EACH SECTION GOES
# ============================================================
# Every heading from Report to the Figures You Have to the end, in file
# order. A piece runs from its heading to the line before the next one
# here, so #### sub-sections travel inside their ### section. 'HEAD' is
# everything above the first, and stays.

PIECES = [
    ('REPORT',    '## Report to the Figures You Have [QUALITY]',                                  PD),
    ('FIGCOUNT',  '### The Figure Count Is a Declared Field [QUALITY]',                           PD_FIG),
    ('STORE',     '### The Store Carries the Verified Figure [CRITICAL]',                         PD),
    ('WITHDRAWN', '### A Derived Row Stores the Figure Its Sources Support -- WITHDRAWN',          SH),
    ('REVIEW',    '## Review-Repair Protocol for Cross-Checked Annotations',                       XC),
    ('LINK',      '### A Link Is an Object, Not Text [QUALITY]',                                  XC),
    ('THREE',     '### Three Things the Prompt Must Require [QUALITY]',                           XC),
    ('ROLES',     '### Model Roles in the Competitive Pattern',                                   XC_WS),
    ('TWO',       '### The Two-Dispatch Rule [CRITICAL]',                                         XC),
    ('TYPES',     '### Worksheet Types',                                                          XC_WS),
    ('NEG',       '### A Negative Verdict Shows Its Search [CRITICAL]',                           XC),
    ('ROUTE',     '### Route the Effort Tier by Job Type [QUALITY]',                              XC),
    ('QUOTE',     '### Quoting a Worksheet Is Transcription, Not Interpretation [CRITICAL]',      XC),
    ('FORMAT',    '### Cross-Checked Annotation Format [CRITICAL]',                               XC),
    ('EXHIBIT',   '### The Exhibit Requirement [CRITICAL]',                                       XC),
    ('RETIRES',   '### A Cross-Check Retires With Its Value or Its Citation [CRITICAL]',          PD),
    ('VERIFIED',  '### Retired: `# Verified: April 2026 via Gemini fact-check`',                  PD),
    ('BATCH',     '### Batch Worksheet Workflow',                                                 XC_WS),
    ('CREDIT',    '### Model Credit in Annotations [PRACTICE]',                                   XC),
    ('FIELD',     '## Field Notes',                                                               PD_FN),
]


def split_pd(text):
    """Cut provenance-discipline into HEAD and the pieces above. Each
    heading must be a line of its own exactly once, outside fenced code.
    Returns {key: text}; the pieces joined in order give back the file
    exactly, which is checked here."""
    lines = text.split('\n')
    fence, where = False, {}
    for i, line in enumerate(lines):
        if line.lstrip().startswith('```'):
            fence = not fence
            continue
        if fence:
            continue
        for key, head, _ in PIECES:
            if line == head:
                if key in where:
                    raise Refuse(f"ERROR: {PD}: heading {head!r} appears "
                                 f"twice.")
                where[key] = i
    for key, head, _ in PIECES:
        if key not in where:
            raise Refuse(f"ERROR: {PD}: heading {head!r} not found.")
    order = [k for k, _, _ in PIECES]
    starts = [where[k] for k in order]
    if starts != sorted(starts):
        raise Refuse(f"ERROR: {PD}: the headings are not in the order "
                     f"this patch was built against.")
    out = {'HEAD': '\n'.join(lines[:starts[0]]) + '\n'}
    for n, key in enumerate(order):
        end = starts[n + 1] if n + 1 < len(order) else len(lines)
        out[key] = '\n'.join(lines[starts[n]:end])
        if n + 1 < len(order):
            out[key] += '\n'
    if out['HEAD'] + ''.join(out[k] for k in order) != text:
        raise Refuse(f"ERROR: {PD}: the pieces do not join back into the "
                     f"file; nothing was moved.")
    return out


def body(piece):
    """A piece without its trailing blank lines, ending in one newline."""
    return piece.rstrip('\n') + '\n'


# ============================================================
# NEW TEXT: HEADERS, POINTERS AND THE NEW SKILL'S OPENING
# ============================================================

FIGURES_POINTER = """\
**Before writing or checking a `# Figures:` line, deriving a value, or
printing a number in a display, read `references/figures.md`.** It
holds The Figure Count Is a Declared Field: Rules 1 to 8, the declared
construction, The ceiling and its Report test, and the print count of
an exact row. Its checker, `test_derived_figures.py`, judges the
declarations on derived rows even in a session that never opened the
file. It does not judge measured rows or what a display prints; those
depend on this pointer being followed (L-418).
"""

XC_IN_PD = """\
## Cross-Checked Lines in the Store

The procedure for sending a value to other models for an independent
check -- the worksheet prompt, the verdicts that come back, and the
`# Cross-checked:` and `# Resolved:` lines that record them -- is the
skill provenance-cross-check. Load it when preparing a cross-check or a
relay prompt, or adjudicating a return. The two rules below stay here
because they fire on ordinary edits: whenever a value or a citation
that carries a cross-check is changed.
"""

FIELD_POINTER = """\
## Field Notes

The field notes are lessons, not rules, and they are in
`references/field-notes.md`. Read them when a scanner count or an audit
result surprises you, or before reporting a value as unverified.
"""

FIG_HEAD = """\
# The Figure Count (provenance-discipline reference)

Read this file in parts.

Opened from provenance-discipline's Report to the Figures You Have,
before writing or checking a `# Figures:` line, deriving a value, or
printing a number in a display. Moved here from provenance-discipline
2.26 on 2026-10-08 (L-418), word for word apart from the edits
provenance-discipline 2.27 lists. The core rule -- compute at full
precision, report to what the least precise input supports -- and The
Store Carries the Verified Figure stay in SKILL.md, and so do the rules
this one leans on: When the Source Gives a Range, The Status Line and
The Read Field.

"""

FN_HEAD = """\
# Field Notes (provenance-discipline reference)

Lessons, not rules. Opened from provenance-discipline when a scanner
count or an audit result surprises you, or before reporting a value as
unverified. Moved here from provenance-discipline 2.26 on 2026-10-08
(L-418), word for word.

"""

WS_HEAD = """\
# Worksheets and Model Roles (provenance-cross-check reference)

Opened from provenance-cross-check before writing a worksheet prompt
or choosing which models to send it to. Moved here from
provenance-discipline 2.26 on 2026-10-08 (L-418), word for word apart
from the two pointer edits provenance-cross-check 1.0 lists. The
annotation format, the exhibit requirement and the send-back rules are
in the skill's SKILL.md.

"""

XC_DESCRIPTION = (
    "How a value is sent to other models for an independent check in the "
    "Paloma's Orrery project, and how the answer is brought back: the "
    "worksheet prompt for GPT, Gemini or another Claude, the table schema "
    "and verdict vocabulary, the Two-Dispatch Rule, the exhibit "
    "requirement (a quotation and a locator), comparing returns, sending "
    "incomplete rows back, and writing the Cross-checked and Resolved "
    "lines that record a check. Use when preparing a cross-check or a "
    "relay prompt carried to another model, reading or adjudicating a "
    "worksheet return, or writing or reviewing a cross-check annotation. "
    "provenance-discipline holds the rules for storing and citing a value "
    "and fires with this one. Do not use for projects other than Paloma's "
    "Orrery.")

XC_HEAD = """\
---
name: provenance-cross-check
description: "%s"
fires_when: Cross-check worksheets and relay prompts, adjudicating returns, writing Cross-checked and Resolved lines
---

# Provenance Cross-Check

Read this file in parts.

Skill version: 1.0 | 2026-10-08, with Anthropic's Claude Opus 5.5, at
palomas_orrery @ %s. v1.0 (L-418) is provenance-discipline's
Review-Repair Protocol, moved here word for word when that skill was
split at 2.27, apart from the edits the build patch lists: four
pointers to sections now in another file, and one paragraph on the
checker's four outcomes (L-252). It loads only for relay work, so a
session that edits a citation without sending it anywhere no longer
loads it.

provenance-discipline holds the rules this procedure serves -- The
Access Standard, The Read Field, Fetched vs Recalled, A Cross-Check
Retires With Its Value or Its Citation -- and fires with it. Three
reference sections are in `references/worksheets.md`: Model Roles in
the Competitive Pattern, Worksheet Types (the table schema and the
verdict vocabulary), and the Batch Worksheet Workflow. Read it before
writing a worksheet prompt or choosing which models to send it to.

## Contents

Generated from this file's headings. skills_index.py --check fails
if this list and the headings disagree (L-418).

- Review-Repair Protocol for Cross-Checked Annotations
  - A Link Is an Object, Not Text [QUALITY]
  - Three Things the Prompt Must Require [QUALITY]
  - The Two-Dispatch Rule [CRITICAL]
  - A Negative Verdict Shows Its Search [CRITICAL]
  - Route the Effort Tier by Job Type [QUALITY]
  - Quoting a Worksheet Is Transcription, Not Interpretation [CRITICAL]
  - Cross-Checked Annotation Format [CRITICAL]
  - The Exhibit Requirement [CRITICAL]
  - Model Credit in Annotations [PRACTICE]

""" % (XC_DESCRIPTION, BASE_SHA)

SH_PD_INTRO_V224 = """\

The skill's v2.24 entry, moved here word for word on 2026-10-08 when
v2.27 made a fourth entry (L-418):
"""

SH_PD_INTRO_WITHDRAWN = """\

A section withdrawn on 2026-09-16, moved here word for word on
2026-10-08 when v2.27 split the skill (L-418). It stood under Report
to the Figures You Have, after The Store Carries the Verified Figure:

"""

SH_LSR_INTRO = """\

The skill's v1.15 entry, moved here word for word on 2026-10-08 when
v1.18 made a fourth entry (L-418):
"""


# ============================================================
# PHASE 2: THE LISTED EDITS
# ============================================================
# (file, label, old, new). Each old text must match exactly once in its
# file at the moment it is applied, and each is printed before and
# after. Nothing else in a moved section changes; the final check
# proves it.

V227 = """\
Skill version: 2.27 | 2026-10-08, with Anthropic's Claude Opus 5.5, at
palomas_orrery @ %s. v2.27 (L-418) splits the skill, and no rule is
reworded. The relay procedure, the Review-Repair Protocol, is now the
skill provenance-cross-check. Rules 1 to 8 of the figure count moved to
references/figures.md and the field notes to references/field-notes.md,
each opened when its pointer says; the withdrawn derived-row rule moved
to documentation/SKILL_HISTORIES.md. Every moved section is word for
word apart from the edits the build patch lists. The file opens with a
read plan, written by skills_index.py, because one read does not show
it whole: the design session's viewer showed 16,000 characters, from
the start and the end, and this session's reader showed lines 1 to
1,106 and said it had stopped (2026-10-08). Riding this version: the
range rule's examples name rows that exist, and a patch predicts the
scanner's change rather than its total (both L-371); Rule 1 names the
conversion marker and Rule 8 records the widening as built (L-390); and
the examples in The Status Line and Report to the Figures You Have name
rows as they now stand.
""" % BASE_SHA

V224 = """\
v2.24 settles L-395 with one new section, A Simple Error a Check Finds
Is Fixed and Reported. Tony's ruling, 2026-10-01: "simple errors such
as the Apophis naming discrepancy should be fixed and reported." It
says what counts as simple, that the fix rides the same patch and is
named, what comes to Tony instead, how a number in a served description
is sourced or removed, and how the rule sits beside The Braid.
"""

V118 = """\
Skill version: 1.18 | 2026-10-08, with Anthropic's Claude Opus 5.5, at
palomas_orrery @ %s. v1.18 (L-418) records two conventions the
provenance-discipline split brought in, under A skill keeps three
version entries: a file longer than one read opens with a read plan
that skills_index.py writes, and a skill's extra files live in its
references folder, each named in its SKILL.md. The Anchor Requirement
names provenance-cross-check for a review prompt carried to another
model.
""" % BASE_SHA

V115 = """\
Earlier: 1.15 | 2026-10-05, with Anthropic's Claude Opus 5.5, at
palomas_orrery @ 72e3b558. v1.15 (L-418) adds one paragraph under the change log, A skill
keeps three version entries, which writes down what this version does
to all six long skills. A contents list now opens the skill, generated from its headings, and
skills_index.py --check fails if the two disagree. Version history
older than the two entries below moved to
documentation/SKILL_HISTORIES.md. Both because a plain read of a
long file shows its start and end and leaves out its middle, where
the rules are (Tony, 2026-10-05).
"""

CONVERSION_PARA = """\
**A conversion carries none of these lines** (v2.27, L-390). A name the
orrery keeps for a value in another unit (Rule 3) is marked with one
comment key instead, naming the row it converts:

```
# Conversion: of <ROW> -- computed from that row, which carries the source and the count
```

It carries no `# Figures:`, `# Status:`, `# Derived:`, `# Source:`,
`# Read:` or `# Cross-checked:` line, because its count and its source
are its row's. Its expression is that one row scaled only by rows that
define units. `constants_rows.conversion_problem()` checks it (Rule 8).
"""

# The L-252 paragraph, word for word as Tony approved it in the
# parallel ledger session of 2026-10-08 and recorded on L-418. None
# until it arrives; the patch refuses to build without it.
P_L252 = """\
**What the checker reports is a different list** (L-252, Tony,
2026-10-08). `worksheet_checker.py` compares the code against a
worksheet and reports one of four outcomes. They are the checker's
words, not worksheet tokens, and never belong in a verdict cell.

- DRIFTED -- the worksheet confirmed a value and the code left it, or
  called it APPROX or PARTIAL and the code moved somewhere the
  worksheet never named. The only defect of the four; routed to
  conversation.
- CORRECTED -- the worksheet rejected the value and the code moved.
  Recorded, not routed.
- COMPLETED -- the worksheet called it APPROX or PARTIAL and supplied a
  value, and the code now reads exactly that value. Recorded, not
  routed.
- UNCHECKED_MOVE -- the code moved and the worksheet established
  nothing about the value. Routed, because nobody has established
  anything. Two different cases reach it, and the checker's line says
  which:
  - NO VALUE VERDICT -- the worksheet checked only the citation, or the
    value cell is blank, holds a word outside the vocabulary, or holds
    DERIVED, which answers the citation question and not this one.
  - UNVERIFIED -- a checker looked at the value and stopped before
    finishing. The line prints it as ABSENT, the checker's internal
    name for that token.

COMPLETED says only that the code took the value the worksheet
supplied. It is not a confirmation. The row is still APPROX or
PARTIAL, it earns no leg toward the cross-checked rung, and the
send-back rule above is unchanged.
"""

PHASE2 = [
    # ---------- provenance-discipline SKILL.md: the header ----------
    (PD, 'read plan seed, and the 2.27 entry',
     "# Provenance Discipline\n\n"
     "Skill version: 2.26 | 2026-10-05, with Anthropic's Claude Opus 5.5, at\n",
     "# Provenance Discipline\n\nRead this file in parts.\n\n" + V227 +
     "Earlier: 2.26 | 2026-10-05, with Anthropic's Claude Opus 5.5, at\n"),
    (PD, 'v2.24 entry out to SKILL_HISTORIES.md (three-entry rule)',
     V224 + "Older entries are in documentation/SKILL_HISTORIES.md, moved there\n"
     "on 2026-10-05 (L-418).\n",
     "Older entries are in documentation/SKILL_HISTORIES.md, moved there\n"
     "on 2026-10-05 and 2026-10-08 (L-418).\n"),
    (PD, 'contents list: the moved sections out, the new section in',
     "- Report to the Figures You Have [QUALITY]\n"
     "  - The Figure Count Is a Declared Field [QUALITY]\n"
     "  - The Store Carries the Verified Figure [CRITICAL]\n"
     "  - A Derived Row Stores the Figure Its Sources Support -- WITHDRAWN\n"
     "- Review-Repair Protocol for Cross-Checked Annotations\n"
     "  - A Link Is an Object, Not Text [QUALITY]\n"
     "  - Three Things the Prompt Must Require [QUALITY]\n"
     "  - Model Roles in the Competitive Pattern\n"
     "  - The Two-Dispatch Rule [CRITICAL]\n"
     "  - Worksheet Types\n"
     "  - A Negative Verdict Shows Its Search [CRITICAL]\n"
     "  - Route the Effort Tier by Job Type [QUALITY]\n"
     "  - Quoting a Worksheet Is Transcription, Not Interpretation [CRITICAL]\n"
     "  - Cross-Checked Annotation Format [CRITICAL]\n"
     "  - The Exhibit Requirement [CRITICAL]\n"
     "  - A Cross-Check Retires With Its Value or Its Citation [CRITICAL]\n"
     "  - Retired: `# Verified: April 2026 via Gemini fact-check`\n"
     "  - Batch Worksheet Workflow\n"
     "  - Model Credit in Annotations [PRACTICE]\n"
     "- Field Notes\n",
     "- Report to the Figures You Have [QUALITY]\n"
     "  - The Store Carries the Verified Figure [CRITICAL]\n"
     "- Cross-Checked Lines in the Store\n"
     "  - A Cross-Check Retires With Its Value or Its Citation [CRITICAL]\n"
     "  - Retired: `# Verified: April 2026 via Gemini fact-check`\n"
     "- Field Notes\n"
     "\n"
     "Kept outside this file and opened when needed: `references/figures.md`\n"
     "holds The Figure Count Is a Declared Field, Rules 1 to 8, and\n"
     "`references/field-notes.md` the field notes. Sending a value to other\n"
     "models for a check is the skill provenance-cross-check.\n"),
    # ---------- the range rule's examples (L-371) ----------
    (PD, "range rule: a worked pair that exists (L-371)",
     "This is L-179's mechanism, generalised. `GRAVITATIONAL_INFLUENCE_AU` and\n"
     "`GRAVITATIONAL_INFLUENCE_RANGE_AU` are the existing pair: the range\n"
     "carries the citation and the access standard, the drawn number is a\n"
     "declared midpoint, and the hover shows the envelope.\n",
     "This is L-179's mechanism, generalised. `HELMET_CUSP_LOW_RADII` and\n"
     "`HELMET_CUSP_HIGH_RADII` are a worked pair: the two rows carry the\n"
     "source, the access and the read, and the drawn `HELMET_CUSP_RADII` is\n"
     "a declared construction over them, the top of the range. (Until v2.27\n"
     "the example here was the gravitational influence, whose range rows\n"
     "are gone: it is now the Sun's Hill radius, one calculated value.)\n"),
    (PD, "range rule: who takes the midpoint (L-371)",
     "the gravitational influence takes the midpoint, the core takes the low\n",
     "Earth's outer-belt peak takes the midpoint, the core takes the low\n"),
    (PD, "range rule: the midpoint's users (L-371)",
     "midpoint** (v2.18). That is the construction the outer belt's peak and\n"
     "the gravitational influence already use. An end is picked only for a\n",
     "midpoint** (v2.18). That is the construction the outer belt's peak\n"
     "already uses. An end is picked only for a\n"),
    # ---------- The Status Line's examples ----------
    (PD, "status line examples: rows as they now stand",
     "HELMET_CUSP_RADII = 4.0\n"
     "# Status: measured V_SOURCED 2026-08-28 -- abstract, open\n"
     "\n"
     "CHROMOSPHERE_PHYSICAL_KM = 2000.0\n"
     "# Status: measured V_SOURCED -- access untested (textbook)\n"
     "\n"
     "SOLAR_RADIUS_AU = SUN_RADIUS_KM / KM_PER_AU\n"
     "# Status: derived -- inherits SUN_RADIUS_KM, KM_PER_AU\n",
     "HELMET_CUSP_HIGH_RADII = 4\n"
     "# Status: measured V_SOURCED 2026-10-04 -- abstract, open\n"
     "\n"
     "EARTH_MAGNETOPAUSE_SHUE_A1_RADII = 10.22\n"
     "# Status: measured V_SOURCED 2026-09-11 -- open full text\n"
     "\n"
     "EARTH_GEOSTATIONARY_RADIUS_KM = (EARTH_GM_KM3_S2 / EARTH_ROTATION_RATE_RAD_S ** 2) ** (1.0 / 3.0)\n"
     "# Status: derived -- inherits EARTH_GM_KM3_S2, EARTH_ROTATION_RATE_RAD_S\n"),
    # ---------- Scanner Mechanics (L-371) ----------
    (PD, "scanner mechanics: predict the change, not the total (L-371)",
     "- False positives get provenance_exceptions.json entries, not code\n"
     "  workarounds.\n",
     "- False positives get provenance_exceptions.json entries, not code\n"
     "  workarounds.\n"
     "- **A patch predicts the scanner's CHANGE, not its total** (v2.27,\n"
     "  L-371). Where a patch says what the run should print, it states how\n"
     "  the Tier-1 count, and the findings it names, should move. The total\n"
     "  differs between machines -- the sandbox and Tony's differed by one\n"
     "  on 2026-10-04 -- and the patch script is itself scanned while it\n"
     "  sits in the root folder, until it is moved to documentation/.\n"),
    # ---------- Report to the Figures You Have ----------
    (PD, "report: where the figure-count rules now live",
     "the next reader does not re-derive it and a checker can read it; the\n"
     "section below says how the field is written and counted.\n",
     "the next reader does not re-derive it and a checker can read it;\n"
     "`references/figures.md` says how the field is written and counted.\n"),
    (PD, "report: the example row is a derived row today",
     "EARTH_INNER_CORE_RADII = EARTH_INNER_CORE_KM / EARTH_EQUATORIAL_RADIUS_KM\n"
     "# Figures: 5 -- set by EARTH_INNER_CORE_KM (1221.5, 5)\n"
     "# Derived: 1221.5 / 6378.1366 = 0.19151\n",
     "EARTH_GEOSTATIONARY_RADIUS_KM = (EARTH_GM_KM3_S2 / EARTH_ROTATION_RATE_RAD_S ** 2) ** (1.0 / 3.0)\n"
     "# Figures: 7 -- set by EARTH_ROTATION_RATE_RAD_S (7.292115e-5, 7)\n"
     "# Derived: (398600.4418 / 7.292115e-5^2)^(1/3) = 42164.17 km\n"),
    # ---------- references/figures.md (L-390) ----------
    (PD_FIG, "rule 1: the first form names a derived row today",
     "# Figures: 5 -- set by EARTH_INNER_CORE_KM (1221.5, 5)\n",
     "# Figures: 7 -- set by EARTH_ROTATION_RATE_RAD_S (7.292115e-5, 7)\n"),
    (PD_FIG, "rule 1: the conversion marker (L-390)",
     "lose the count.\n\n**Rule 2.",
     "lose the count.\n\n" + CONVERSION_PARA + "\n**Rule 2."),
    (PD_FIG, "rule 3: a conversion is marked (L-390)",
     "orrery's drawing code keeps for such a value is computed from the one\n"
     "row and states no precision of its own.",
     "orrery's drawing code keeps for such a value is computed from the one\n"
     "row, is marked `# Conversion: of <ROW>` (Rule 1), and states no\n"
     "precision of its own."),
    (PD_FIG, "rule 8: the widening is built (L-390)",
     "The widening is built with the\n"
     "patch that retires the store's conversion rows (L-345, D20), because\n"
     "until then those rows declare counts the widened check would refuse.\n",
     "The widening was built with\n"
     "patch D20 (L-345), which retired the store's conversion rows. Since\n"
     "then a marked conversion (Rule 1) is checked by\n"
     "`constants_rows.conversion_problem()` and listed by name with its\n"
     "source; a wrong one is CONVERSION WRONG, which fails, and a row shaped\n"
     "like a conversion and not marked is UNMARKED CONVERSION, a named gap\n"
     "that fails inside a closed slice (v2.27, L-390).\n"),
    # ---------- provenance-cross-check SKILL.md ----------
    (XC, "pointer: Worksheet Types is in the reference file",
     "   being checked, and specifies the job type (see Worksheet Types below).\n",
     "   being checked, and specifies the job type (see Worksheet Types, in\n"
     "   `references/worksheets.md`).\n"),
    (XC, "pointer: Model Roles is in the reference file",
     "   tier decides what the return is worth -- see the roster note under\n"
     "   Model Roles -- so a return that does not name it cannot be scored.\n",
     "   tier decides what the return is worth -- see the roster note under\n"
     "   Model Roles, in `references/worksheets.md` -- so a return that does\n"
     "   not name it cannot be scored.\n"),
    (XC, "the checker's four outcomes beside the send-back rule (L-252)",
     "something it did not say at the time.\n\n"
     "#### A Complete Row That Disagrees Is a Finding [CRITICAL]\n",
     "something it did not say at the time.\n\n"
     "@@P_L252@@\n"
     "#### A Complete Row That Disagrees Is a Finding [CRITICAL]\n"),
    # ---------- references/worksheets.md ----------
    (XC_WS, "pointer: The Read Field is in provenance-discipline",
     "(The Read Field,\nabove).",
     "(The Read Field,\nin provenance-discipline)."),
    (XC_WS, "pointer: Route the Effort Tier is in SKILL.md",
     "They ask different questions, they fail differently, and per Route the\n"
     "Effort Tier by Job Type below they are not worth the same effort tier.\n",
     "They ask different questions, they fail differently, and per Route the\n"
     "Effort Tier by Job Type, in the skill's SKILL.md, they are not worth\n"
     "the same effort tier.\n"),
    # ---------- ledger-and-session-records SKILL.md ----------
    (LSR, 'read plan seed, and the 1.18 entry',
     "# Ledger and Session Records\n\n"
     "Skill version: 1.17 | 2026-10-07, with Anthropic's Claude Fable 5.1, at\n",
     "# Ledger and Session Records\n\nRead this file in parts.\n\n" + V118 +
     "Earlier: 1.17 | 2026-10-07, with Anthropic's Claude Fable 5.1, at\n"),
    (LSR, 'v1.15 entry out to SKILL_HISTORIES.md (three-entry rule)',
     V115 + "Older entries are in documentation/SKILL_HISTORIES.md, moved there\n"
     "on 2026-10-05 (L-418) and 2026-10-07 (L-422).\n",
     "Older entries are in documentation/SKILL_HISTORIES.md, moved there\n"
     "on 2026-10-05 (L-418), 2026-10-07 (L-422) and 2026-10-08 (L-418).\n"),
    (LSR, 'anchor requirement: a review prompt needs provenance-cross-check',
     "Load it by name\": a provenance review needs provenance-discipline, a\n"
     "patch needs safe-file-editing, and sending all ten teaches the partner\n"
     "to skim.\n",
     "Load it by name\": a provenance review needs provenance-discipline, a\n"
     "review prompt carried to another model needs provenance-cross-check\n"
     "beside it, a patch needs safe-file-editing, and sending them all\n"
     "teaches the partner to skim.\n"),
    (LSR, 'three version entries: the read plan and reference files',
     "the list in the same edit. Both for one reason: a plain read of a long\n"
     "file shows its start and end and leaves out its middle, so what opens\n"
     "a skill is the one part every session is sure to see.\n",
     "the list in the same edit. A file longer than one read -- 16,000\n"
     "characters or 2,000 lines, the smaller of the two readers measured --\n"
     "opens, just under its title, with a READ PLAN naming the line ranges\n"
     "to read it in, one read each (v1.18, L-418). A patch puts the seed\n"
     "line there, `Read this file in parts.`, and `skills_index.py` writes\n"
     "the plan; `--check` fails on a long file with none, a part over one\n"
     "read, or a line no part covers. A long skill still waiting for its\n"
     "plan is named on the list `PLAN_NOT_YET` in `skills_index.py`, which\n"
     "every run prints; it gets the plan at its next version, and comes off\n"
     "the list in the same patch. A skill's extra files live in its\n"
     "`references/` folder, each named in its SKILL.md with the moment to\n"
     "open it; `--check` fails on one named and missing, or present and\n"
     "never named. All of this for one reason: a plain read of a long file\n"
     "shows only part of it -- its start and end in one reader, its start\n"
     "alone in another -- so what opens a skill is the one part every\n"
     "session is sure to see.\n"),
]


# ============================================================
# THE PROTOCOL: v3.86, and v3.83 down to the history file
# ============================================================

V386 = """\
v3.86 (October 8, 2026): No rule changed in this document. THREE
skills, one version each (L-418): provenance-discipline 2.26 -> 2.27,
the new skill provenance-cross-check 1.0, and
ledger-and-session-records 1.17 -> 1.18. PROVENANCE-DISCIPLINE IS
SPLIT, AND A LONG FILE CARRIES ITS READ PLAN.

WHAT PROMPTED IT. provenance-discipline was 137,837 characters in 2,590
lines, and one read of a file does not show that much. The design
session's viewer showed 16,000 characters, from the start and the end;
this session's reader showed the first 1,106 lines and said it had
stopped. So the skill that guards facts and sources was the one least
likely to be read whole. Tony ruled the split on 2026-10-06 ("Read and
confirmed"), and a trial skill showed on 2026-10-08 that an installed
skill keeps the extra files in its folder.

WHAT CHANGED. The relay procedure, the Review-Repair Protocol, is the
new skill provenance-cross-check, with its worksheet sections in a
reference file. provenance-discipline keeps its rules, with the
figure-count rules and the field notes in two reference files, each
opened when its pointer says. Every moved section is word for word
apart from the edits the patch lists, and the patch proves it. Riding
2.27: L-371 (the Sun room's served numbers), L-390 (the conversion
marker) and L-252 (the checker's fourth outcome). skills_index.py
writes a read plan into every file longer than one read, and its
--check fails on a part too long, a line no part covers, or a reference
file named and missing or present and never named.
ledger-and-session-records 1.18 records those two conventions and names
provenance-cross-check for review prompts. Four other long skills get
their read plans at their next version, by Tony's ruling of the same
day, and skills_index.py names them on every run. The manifest has a
twelfth row.

THE OBLIGATION TRAVELS. A reinstall during a session is not visible to
that session. The next session confirms its loaded copies read
provenance-discipline 2.27, provenance-cross-check 1.0 and
ledger-and-session-records 1.18; lists both skill folders and finds
their reference files; and, on its first figures task, says whether it
opened the figures reference file before writing a figure count.

The header stamp and the SHA anchor move with this entry.

Version history: v3.83 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

"""

PI_V383_START = "v3.83 (October 6, 2026): No rule changed in this document. ONE\n"
PI_V383_END = ("Version history: v3.80 moves down to\n"
               "documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three\n"
               "resident.\n\n")
PIH_TAIL = ("\n(Moved down from the resident protocol on 2026-10-07 when\n"
            "v3.85 made a fourth entry.)\n\n"
            "================================================================\n"
            "PART 2 -- LESSONS REMOVED FROM THE PROTOCOL AT v3.37\n")


def build_protocol(pi, pih):
    """v3.86 in, v3.83 out of the protocol and onto the end of PART 1."""
    pi = edit(pi, "Tony Quintanilla, PE | Claude | v3.85 | October 7, 2026\n",
              "Tony Quintanilla, PE | Claude | v3.86 | October 8, 2026\n",
              PI, 'header stamp v3.86')
    pi = edit(pi, "Cut from 8653ef1b at https://github.com/tonylquintanilla/palomas_orrery\n",
              "Cut from %s at https://github.com/tonylquintanilla/palomas_orrery\n"
              % BASE_SHA, PI, 'SHA anchor')
    pi = edit(pi, "v3.85 (October 7, 2026): No rule changed in this document. ONE\n",
              V386 + "v3.85 (October 7, 2026): No rule changed in this document. ONE\n",
              PI, 'v3.86 entry')
    if pi.count(PI_V383_START) != 1:
        raise Refuse(f"ANCHOR FAIL: {PI}: the v3.83 entry was not found once.")
    a = pi.index(PI_V383_START)
    b = pi.find(PI_V383_END, a)
    if b < 0:
        raise Refuse(f"ANCHOR FAIL: {PI}: the end of the v3.83 entry was "
                     f"not found.")
    b += len(PI_V383_END)
    v383 = pi[a:b]
    pi = pi[:a] + pi[b:]
    say(f"ok  {PI:52s} v3.83 out ({v383.count(chr(10))} lines)")
    pih = edit(pih, PIH_TAIL,
               "\n(Moved down from the resident protocol on 2026-10-07 when\n"
               "v3.85 made a fourth entry.)\n\n" + v383.rstrip('\n') + "\n\n"
               "(Moved down from the resident protocol on 2026-10-08 when\n"
               "v3.86 made a fourth entry.)\n\n"
               "================================================================\n"
               "PART 2 -- LESSONS REMOVED FROM THE PROTOCOL AT v3.37\n",
               PIH, 'v3.83 in, at the end of PART 1')
    return pi, pih


# ============================================================
# skills_index.py: the read plan and the reference-file check
# ============================================================
# Applied in this order, bottom of the file first; each anchor
# matches exactly once at the moment it is applied.
SKILLS_INDEX_EDITS = [
    ('    else:\n        print(f"OK: {len(records)} skills parsed, no consistency problems.")\n    for w in warnings:\n        print(f"  WARNING: {w}")',
     '    else:\n        print(f"OK: {len(records)} skills parsed, no consistency problems.")\n    plans = [p for r in records for p in r.get(\'plans\', [])]\n    print(f"Read plans checked ({len(plans)}): "\n          f"{\', \'.join(plans) if plans else \'none\'}.")\n    if PLAN_NOT_YET:\n        print(f"Long skills with no read plan yet, by PLAN_NOT_YET "\n              f"({len(PLAN_NOT_YET)}): {\', \'.join(PLAN_NOT_YET)}.")\n    for w in warnings:\n        print(f"  WARNING: {w}")'),
    ('        sys.exit(2)\n\n    records, problems, warnings = [], [], []\n    for skill_dir in sorted(p for p in skills_dir.iterdir() if p.is_dir()):',
     '        sys.exit(2)\n\n    # L-418: in write mode, rewrite every read plan before the skills are\n    # read, so the check below reads what was written. Each change is\n    # named; a plan already right is left alone.\n    if not check_only:\n        for skill_dir in sorted(p for p in skills_dir.iterdir() if p.is_dir()):\n            paths = [skill_dir / \'SKILL.md\']\n            ref_dir = skill_dir / REFERENCES_DIRNAME\n            if ref_dir.is_dir():\n                paths.extend(sorted(ref_dir.glob(\'*.md\')))\n            for path in paths:\n                if path.is_file():\n                    written = write_read_plan(path)\n                    if written:\n                        rel = path.relative_to(skills_dir).as_posix()\n                        print(f"Read plan written: {rel}: {written}")\n\n    records, problems, warnings = [], [], []\n    for skill_dir in sorted(p for p in skills_dir.iterdir() if p.is_dir()):'),
    ('                    f"{stripped}")\n\n        # The Resolved leg (L-200) is checked the same way and for the\n        # same reason. A skill that teaches a leg the parser refuses is\n        # the L-186 defect in a second grammar.\n        for line in text.splitlines():\n            stripped = line.strip()\n            if not stripped.startswith(\'# Resolved:\') or \'<\' in stripped:\n                continue\n            records, issues = parse_resolved(stripped)\n            if len(records) != 1:\n                problems.append(\n                    f"{skill_dir.name}: Resolved example does not parse "\n                    f"({issues or \'no record\'}): {stripped}")\n    return problems\n',
     '                    f"{stripped}")\n\n            # The Resolved leg (L-200) is checked the same way and for the\n            # same reason. A skill that teaches a leg the parser refuses is\n            # the L-186 defect in a second grammar.\n            for line in text.splitlines():\n                stripped = line.strip()\n                if not stripped.startswith(\'# Resolved:\') or \'<\' in stripped:\n                    continue\n                records, issues = parse_resolved(stripped)\n                if len(records) != 1:\n                    problems.append(\n                        f"{label}: Resolved example does not parse "\n                        f"({issues or \'no record\'}): {stripped}")\n    return problems\n'),
    ('            if not stripped.startswith(\'# Cross-checked:\') or \'<\' in stripped:\n                continue\n            records, issues = parse_cross_checks(stripped)\n            if len(records) != 1:\n                problems.append(\n                    f"{skill_dir.name}: annotation example does not parse "\n                    f"({issues or \'no record\'}): {stripped}")\n                continue\n            identity = records[0][0]\n            runs = \'\'.join(c if c.isdigit() else \' \' for c in identity).split()\n            if any(len(run) >= 4 for run in runs):\n                problems.append(\n                    f"{skill_dir.name}: annotation example\'s checker carries "\n                    f"a year, so the date was parsed from the source: "\n                    f"{stripped}")\n\n            # The Resolved leg (L-200) is checked the same way and for the',
     '            if not stripped.startswith(\'# Cross-checked:\') or \'<\' in stripped:\n                continue\n            label = skill_dir.name\n            if path.name != \'SKILL.md\':\n                label += f"/{REFERENCES_DIRNAME}/{path.name}"\n            text = path.read_text(encoding=\'utf-8\', errors=\'replace\')\n            for line in text.splitlines():\n                stripped = line.strip()\n                if not stripped.startswith(\'# Cross-checked:\') or \'<\' in stripped:\n                    continue\n                records, issues = parse_cross_checks(stripped)\n                if len(records) != 1:\n                    problems.append(\n                        f"{label}: annotation example does not parse "\n                        f"({issues or \'no record\'}): {stripped}")\n                    continue\n                identity = records[0][0]\n                runs = \'\'.join(c if c.isdigit() else \' \' for c in identity).split()\n                if any(len(run) >= 4 for run in runs):\n                    problems.append(\n                        f"{label}: annotation example\'s checker carries "\n                        f"a year, so the date was parsed from the source: "\n                        f"{stripped}")\n\n            # The Resolved leg (L-200) is checked the same way and for the'),
    ("\n    for skill_dir in sorted(p for p in skills_dir.iterdir() if p.is_dir()):\n        path = skill_dir / 'SKILL.md'\n        if not path.is_file():\n            continue\n        text = path.read_text(encoding='utf-8', errors='replace')\n        for line in text.splitlines():\n            stripped = line.strip()\n            if not stripped.startswith('# Cross-checked:') or '<' in stripped:\n                continue\n            label = skill_dir.name",
     "\n    for skill_dir in sorted(p for p in skills_dir.iterdir() if p.is_dir()):\n        # L-418: reference files are read too. A rule that moved out of\n        # SKILL.md must not take its examples out of the check with it.\n        paths = [skill_dir / 'SKILL.md']\n        ref_dir = skill_dir / REFERENCES_DIRNAME\n        if ref_dir.is_dir():\n            paths.extend(sorted(ref_dir.glob('*.md')))\n        for path in paths:\n            if not path.is_file():\n                continue\n            label = skill_dir.name"),
    ("\n    return ({'name': name, 'version': version, 'fires_when': fires,\n             'header_how': header_how}, problems, warnings)\n\n",
     "\n    return ({'name': name, 'version': version, 'fires_when': fires,\n             'header_how': header_how, 'plans': plans}, problems, warnings)\n\n"),
    ('    check_contents(lines, body_start, skill_dir.name, body_lines, problems)\n\n    version = None\n    for line in lines[body_start:]:',
     '    check_contents(lines, body_start, skill_dir.name, body_lines, problems)\n\n    # L-418: reference files, and a read plan on every long file.\n    plans = []\n    on_list = skill_dir.name in PLAN_NOT_YET\n    probs, summary = read_plan_problems(file_lines(text),\n                                        f"{skill_dir.name}/SKILL.md",\n                                        required=not on_list)\n    problems.extend(probs)\n    if summary:\n        plans.append(summary)\n        if on_list:\n            problems.append(f"{skill_dir.name}: has a read plan and is still "\n                            f"on PLAN_NOT_YET; take it off the list")\n    elif on_list and is_long(file_lines(text)):\n        warnings.append(f"{skill_dir.name}: long and no read plan yet; on "\n                        f"PLAN_NOT_YET, so it gets one at its next version")\n    for ref in check_references(skill_dir, text, problems):\n        ref_lines = file_lines(ref.read_text(encoding=\'utf-8\'))\n        probs, summary = read_plan_problems(\n            ref_lines, f"{skill_dir.name}/{REFERENCES_DIRNAME}/{ref.name}",\n            required=True)\n        problems.extend(probs)\n        if summary:\n            plans.append(summary)\n\n    version = None\n    for line in lines[body_start:]:'),
    ('\n\ndef check_install_limits(name, desc, label, body_lines, problems, warnings):\n    """Anthropic\'s documented header limits (L-417), checked here so that a',
     '\n\ndef file_lines(text):\n    """A file\'s lines as a reader numbers them: a final newline does not\n    make an empty last line."""\n    lines = text.split(\'\\n\')\n    if text.endswith(\'\\n\'):\n        lines = lines[:-1]\n    return lines\n\n\ndef size_of(lines):\n    """Characters, each line counted with its newline."""\n    return sum(len(line) + 1 for line in lines)\n\n\ndef is_long(lines):\n    return (size_of(lines) > READ_PART_MAX_CHARS\n            or len(lines) > READ_PART_MAX_LINES)\n\n\ndef plan_line_index(lines):\n    """Index of the read plan line, or its seed, or None. Only the first\n    twenty lines are looked at: a plan is only any use at the top, inside\n    the part every read shows."""\n    for i, line in enumerate(lines[:20]):\n        if PLAN_ANY_RE.match(line):\n            return i\n    return None\n\n\ndef compute_parts(lines):\n    """Split a file into parts that each fit one read (L-418).\n\n    Each part is at most READ_PART_MAX_CHARS characters and\n    READ_PART_MAX_LINES lines. It ends just before a heading where one\n    falls inside it, else just before a blank line, else where the limit\n    falls; never inside fenced code unless no other place exists.\n    Returns [(first, last)], 1-based and inclusive.\n    """\n    headings, blanks, fence = set(), set(), False\n    for i, line in enumerate(lines):\n        if line.lstrip().startswith(\'```\'):\n            fence = not fence\n            continue\n        if fence:\n            continue\n        if re.match(r\'^#{1,4} \', line):\n            headings.add(i)\n        elif not line.strip():\n            blanks.add(i)\n    parts, start, n = [], 0, len(lines)\n    while start < n:\n        chars, end = 0, start\n        while (end < n and end - start < READ_PART_MAX_LINES\n               and chars + len(lines[end]) + 1 <= READ_PART_MAX_CHARS):\n            chars += len(lines[end]) + 1\n            end += 1\n        if end >= n:\n            parts.append((start + 1, n))\n            break\n        if end == start:          # one line longer than a read; the check names it\n            end = start + 1\n        # A heading is the best place to end a part, but not at the cost\n        # of a part less than half full: then a blank line is used.\n        half = start + (end - start) // 2\n        cut = max((c for c in headings if half < c <= end), default=None)\n        if cut is None:\n            cut = max((c for c in blanks if start < c <= end), default=None)\n        if cut is None:\n            cut = end\n        parts.append((start + 1, cut))\n        start = cut\n    return parts\n\n\ndef plan_text(parts):\n    spans = \', \'.join(\'%d-%d\' % p for p in parts)\n    word = \'part\' if len(parts) == 1 else \'parts\'\n    return f"Read this file in {len(parts)} {word}: lines {spans}."\n\n\ndef write_read_plan(path):\n    """Rewrite the read plan in a file that has one (or its seed). The\n    plan is one line, so writing it moves no other line; it is computed\n    again until it no longer changes, since its own length counts in the\n    first part. Returns the plan written, or None when nothing changed\n    or the file has no plan line."""\n    text = path.read_text(encoding=\'utf-8\')\n    lines = file_lines(text)\n    i = plan_line_index(lines)\n    if i is None:\n        return None\n    for _ in range(5):\n        new = plan_text(compute_parts(lines))\n        if lines[i] == new:\n            break\n        lines[i] = new\n    out = \'\\n\'.join(lines) + (\'\\n\' if text.endswith(\'\\n\') else \'\')\n    if out == text:\n        return None\n    with open(path, \'w\', encoding=\'utf-8\', newline=\'\') as f:\n        f.write(out)\n    return lines[i]\n\n\ndef read_plan_problems(lines, label, required):\n    """Check one file\'s read plan (L-418). Returns ([problems], summary).\n\n    A plan must name parts that start at line 1, follow on with no gap\n    and no overlap, end at the file\'s last line, and each fit one read.\n    A seed not yet filled fails. A long file with no plan fails when\n    `required`. summary is the text --check prints for a file that passes,\n    so a pass carries what was compared.\n    """\n    problems = []\n    i = plan_line_index(lines)\n    if i is None:\n        if is_long(lines) and required:\n            problems.append(\n                f"{label}: {size_of(lines):,} characters in {len(lines)} lines "\n                f"and no read plan; a file longer than one read "\n                f"({READ_PART_MAX_CHARS:,} characters or "\n                f"{READ_PART_MAX_LINES:,} lines) opens with one (L-418)")\n        return problems, None\n    line = lines[i]\n    if line == PLAN_SEED:\n        return [f"{label}: the read plan is still the seed; run "\n                f"skills_index.py to write it"], None\n    m = PLAN_RE.match(line)\n    if not m:\n        return [f"{label}: read plan line does not parse: {line!r}"], None\n    spans = []\n    for item in m.group(2).split(\',\'):\n        sm = re.fullmatch(r\'\\s*(\\d+)-(\\d+)\\s*\', item)\n        if not sm:\n            return [f"{label}: read plan part {item.strip()!r} is not "\n                    f"\'first-last\'"], None\n        spans.append((int(sm.group(1)), int(sm.group(2))))\n    if int(m.group(1)) != len(spans):\n        problems.append(f"{label}: read plan says {m.group(1)} parts and "\n                        f"lists {len(spans)}")\n    expected, n = 1, len(lines)\n    for k, (a, b) in enumerate(spans, 1):\n        if a > expected:\n            problems.append(f"{label}: lines {expected}-{a - 1} are in no "\n                            f"part of the read plan")\n        elif a < expected:\n            problems.append(f"{label}: read plan part {k} starts at line {a}, "\n                            f"inside the part before it")\n        if b < a:\n            problems.append(f"{label}: read plan part {k} ends before it "\n                            f"starts ({a}-{b})")\n        if b > n:\n            problems.append(f"{label}: read plan part {k} ends at line {b}; "\n                            f"the file has {n}")\n        chunk = lines[a - 1:min(b, n)]\n        if size_of(chunk) > READ_PART_MAX_CHARS or len(chunk) > READ_PART_MAX_LINES:\n            problems.append(f"{label}: read plan part {k} (lines {a}-{b}) is "\n                            f"{size_of(chunk):,} characters in {len(chunk)} "\n                            f"lines; one read is {READ_PART_MAX_CHARS:,} "\n                            f"characters and {READ_PART_MAX_LINES:,} lines")\n        expected = max(expected, b + 1)\n    if expected <= n:\n        problems.append(f"{label}: lines {expected}-{n} are in no part of "\n                        f"the read plan")\n    return problems, f"{label} {len(spans)} part{\'\' if len(spans) == 1 else \'s\'}"\n\n\ndef check_references(skill_dir, text, problems):\n    """Every reference file named and present, and nothing else in the\n    folder (L-418). Today a pointer to a missing file would pass silently,\n    because only SKILL.md was read. Returns the reference files present."""\n    label = skill_dir.name\n    named = set(REFERENCE_NAME_RE.findall(text))\n    present = []\n    for p in sorted(skill_dir.iterdir()):\n        if p.name == \'SKILL.md\':\n            continue\n        if p.is_dir() and p.name == REFERENCES_DIRNAME:\n            for q in sorted(p.iterdir()):\n                if q.is_file() and q.suffix == \'.md\':\n                    present.append(q)\n                else:\n                    problems.append(f"{label}: {REFERENCES_DIRNAME}/{q.name} "\n                                    f"is not a .md file")\n            continue\n        problems.append(f"{label}: {p.name} sits in the skill folder; only "\n                        f"SKILL.md and {REFERENCES_DIRNAME}/ may")\n    names = {q.name for q in present}\n    for n in sorted(named - names):\n        problems.append(f"{label}: SKILL.md names {REFERENCES_DIRNAME}/{n}, "\n                        f"which is not in the folder")\n    for n in sorted(names - named):\n        problems.append(f"{label}: {REFERENCES_DIRNAME}/{n} is in the folder "\n                        f"and SKILL.md never names it")\n    return present\n\n\ndef check_install_limits(name, desc, label, body_lines, problems, warnings):\n    """Anthropic\'s documented header limits (L-417), checked here so that a'),
    ("XML_TAG_RE = re.compile(r'<[A-Za-z/][^>]*>')  # neither field may hold an XML tag\nBODY_GUIDELINE_LINES = 500\n\n",
     "XML_TAG_RE = re.compile(r'<[A-Za-z/][^>]*>')  # neither field may hold an XML tag\nBODY_GUIDELINE_LINES = 500\n\n# One read of a file, measured (L-418). Two readers have been measured,\n# and a read plan's parts must fit the smaller of each:\n#   2026-10-06, the design session's file viewer: 16,000 characters,\n#     taken from the start and the end, the middle cut silently.\n#   2026-10-08, this build session's Read tool: the first 25,000 tokens\n#     and no more, with a notice saying so. On provenance-discipline\n#     2.26 that was lines 1 to 1,106, 55,748 characters. Its documented\n#     line limit is 2,000 lines.\n# So a part is at most 16,000 characters and at most 2,000 lines.\n# Characters are counted with each line's newline.\nREAD_PART_MAX_CHARS = 16000\nREAD_PART_MAX_LINES = 2000\nPLAN_SEED = 'Read this file in parts.'\nPLAN_RE = re.compile(r'^Read this file in (\\d+) parts?: lines (.+)\\.$')\nPLAN_ANY_RE = re.compile(r'^Read this file in ')\nREFERENCES_DIRNAME = 'references'\nREFERENCE_NAME_RE = re.compile(r'references/([A-Za-z0-9_.-]+\\.md)')\n\n# Long skills that have no read plan yet and get one at their next\n# version, so that adding the line costs no extra reinstall now. Each is\n# named in the --check output every run, so the list cannot be forgotten.\n# A skill not on this list fails --check when it is long and has no plan.\nPLAN_NOT_YET = [\n    # Tony, 2026-10-08: these get their plans at their next version.\n    # Each was under one read of the reader measured that day (about\n    # 55,000 characters), so none is cut today.\n    'gallery-cache-builder',\n    'interactive-exhibit',\n    'orrery-coding-conventions',\n    'safe-file-editing',\n]\n\n"),
    ("    'horizons-orbital-mechanics',\n    'provenance-discipline',\n    'earth-system-pipeline',\n    'gallery-pipeline',",
     "    'horizons-orbital-mechanics',\n    'provenance-discipline',\n    'provenance-cross-check',\n    'earth-system-pipeline',\n    'gallery-pipeline',"),
    ('by item, skipping fenced code. Six skills gained one the same day.)\n\nRole: devtool\nDomain: dev_tools',
     'by item, skipping fenced code. Six skills gained one the same day.)\n\nModule updated: October 8, 2026 with Anthropic\'s Claude Opus 5.5\n(L-418, the provenance-discipline split: two new checks and the read\nplan. A skill folder may now hold reference files in references/,\nopened only when the skill says to. Every file a SKILL.md names under\nreferences/ must exist, and every file in the folder must be named by\nit; nothing else may sit in a skill folder. A long file -- a SKILL.md or\na reference file over one read -- carries a READ PLAN as its first line\nafter the title, "Read this file in N parts: lines a-b, c-d, ...",\nwhich this tool writes: run it after putting the seed line "Read this\nfile in parts." where the plan goes. --check fails on a part over one\nread, on a line no part covers, on a seed not yet filled, and on a long\nfile with no plan unless its skill is on the named PLAN_NOT_YET list.\nIn write mode the tool rewrites every plan it finds before reading the\nskills, and names each one it changed. Annotation examples are now also\nread from reference files. A SKILL.md must not write another skill\'s\nreferences/ path, because the check would read it as its own.)\n\nRole: devtool\nDomain: dev_tools'),
]


# ============================================================
# RECORDS: the ledger, Where We Are, and the session's handoff
# ============================================================
# Tony annotates these, and a parallel session (the decisions session of
# 2026-10-08) edits the same two files. So every edit here is anchored on
# the lines this build owns, inside the item it belongs to, and a line
# somebody else changed first makes the patch stop before writing.

import re

HANDOFF = 'documentation/HANDOFF_L418_split_build_20261008.md'


def block_span(ledger, n):
    """Start and end of ledger item L-n: from its header to the next item
    header or section heading."""
    m = re.search(r'^#### \[L-%d\][^\n]*\n' % n, ledger, re.M)
    if not m:
        raise Refuse(f"ANCHOR FAIL: {LEDGER}: item L-{n} not found.")
    nxt = re.compile(r'^(#### \[L-|## )', re.M).search(ledger, m.end())
    return m.start(), (nxt.start() if nxt else len(ledger))


def block_edit(ledger, n, old, new, label):
    a, b = block_span(ledger, n)
    blk = ledger[a:b]
    if blk.count(old) != 1:
        raise Refuse(f"ANCHOR FAIL: {LEDGER}: L-{n}: {label}: expected 1 "
                     f"match inside the item, found {blk.count(old)}.\n"
                     f"  anchor starts: {old[:90]!r}")
    say(f"ok  {LEDGER:52s} L-{n}: {label}")
    return ledger[:a] + blk.replace(old, new) + ledger[b:]


def meta_edit(ledger, n, status=None, section=None):
    a, b = block_span(ledger, n)
    blk = ledger[a:b]
    pat = re.compile(r'<!-- L:%d status:(\S+) upd:(\S+) section:(\S+) ' % n)
    m = pat.search(blk)
    if not m:
        raise Refuse(f"ANCHOR FAIL: {LEDGER}: L-{n}: metadata line not found.")
    new = '<!-- L:%d status:%s upd:%s section:%s ' % (
        n, status or m.group(1), TODAY, section or m.group(3))
    blk = blk[:m.start()] + new + blk[m.end():]
    say(f"ok  {LEDGER:52s} L-{n}: metadata"
        + (f" -> {status}, section {section}" if status else ", date"))
    return ledger[:a] + blk + ledger[b:]


def next_handle(ledger):
    nums = [int(x) for x in re.findall(r'^#### \[L-(\d+)\]', ledger, re.M)]
    return max(nums) + 1


L418_BUILT = """\
- **2026-10-08, the install trial passed.** install-probe arrived with
  its `references/probe.md`, md5 dc4f6011467ccc53f5b84f8a776b352b, the
  recorded sentence, and the same "plugin" marking as Tony's eleven
  skills, so the result speaks for them. Tony then deleted it.
- **2026-10-08, the read limit measured.** This session's Read tool
  stops at 25,000 tokens and says so: lines 1 to 1,106 of 2.26, 55,748
  characters. The design's viewer showed 16,000 characters from the
  start and the end. A read plan's parts stay under both: 16,000
  characters and 2,000 lines.
- **2026-10-08, the split built** at orrery %(base)s:
  `patch_L418_3_split_build_20261008.py`. provenance-discipline 2.27,
  provenance-cross-check 1.0, ledger-and-session-records 1.18, protocol
  v3.86. Fifteen sections moved and each checked whole; 23 listed edits,
  each printed before and after; a final check that every section is
  its original plus exactly those edits. skills_index.py writes the
  read plans and checks them and the reference files; each new check
  was shown failing on a throwaway copy before it was trusted.
- **Tony's rulings of 2026-10-08, riding the build.** L-371 (the Sun
  room's served numbers) and L-390 (the conversion marker) ride 2.27
  ("As recommended? -- yes"). The L-252 paragraph, the checker's four
  outcomes, goes beside the send-back rule in provenance-cross-check
  ("Approved"), with its UNCHECKED_MOVE bullet split into its two cases
  ("approved as recommended"). The four other long skills --
  gallery-cache-builder, interactive-exhibit, orrery-coding-conventions,
  safe-file-editing -- get their read plans at their next version, and
  skills_index.py names them on PLAN_NOT_YET every run ("confirmed as
  recommended").
- **One departure from the brief, recorded.** The brief said a phase-2
  edit inside a moved section is refused. L-390's sentences and the
  L-252 paragraph both fall inside moved text, so instead the final
  check proves each section equals its original with exactly the listed
  edits applied.
"""

L418_GAP = """\
**Gap:** Tony runs the patch and orrery_maintenance_run.py, pushes,
installs three skills (provenance-discipline, provenance-cross-check,
ledger-and-session-records) and replaces the Project's instructions with
PROJECT_INSTRUCTIONS.md v3.86. The next session confirms its loaded
copies read 2.27, 1.0 and 1.18, finds both skills' reference files,
and on its first figures task says whether it opened the figures
reference file first; then this item closes.
"""

L390_LANDED = """\
- **Landed 2026-10-08** in provenance-discipline 2.27 (L-418),
  `patch_L418_3_split_build_20261008.py`. Rule 1 shows the
  `# Conversion:` form and says what a conversion carries and what it
  does not; Rule 3 says a conversion is marked; Rule 8 says the
  widening and the conversion check were built with D20 and names
  `UNMARKED CONVERSION` and `CONVERSION WRONG`. The three rules now live
  in the skill's `references/figures.md`. Nothing is left open.
**Gap:** none.
"""

L371_LANDED = """\
- **2026-10-08, the two skill sentences landed** in
  provenance-discipline 2.27 (L-418): the range rule's worked pair is
  the helmet cusp's two rows, and a patch predicts the scanner's change,
  not its total.
"""


def new_item(n):
    return """\
#### [L-%(n)d] The checker reports one word for two different cases (worksheet checker)
<!-- L:%(n)d status:OPEN upd:%(today)s section:A flag: rice: -->
- **Found 2026-10-08,** building L-418, while checking the L-252
  paragraph against `worksheet_checker.py` at %(base)s. UNCHECKED_MOVE
  is reported for two different cases: the worksheet has no value
  verdict (it checked only the citation, or the value cell is blank,
  holds a word outside the vocabulary, or holds DERIVED), and the value
  verdict is UNVERIFIED, which the checker reads as ABSENT. Tony: "they
  are not the same."
- **Settled in the skill:** provenance-cross-check 1.0 defines the two
  cases separately (Tony, 2026-10-08, "approved as recommended").
- **Not built:** whether the checker itself prints two different words.
  That is a change to `worksheet_checker.py` and its tests, for a
  session of its own.
  **Tony-action (decide):** whether the checker splits the word.
**Gap:** Tony's decision above; if yes, a session builds it with a test
for each case and updates the skill's bullet to match.
**Ref:** `worksheet_checker.py` (the L2b block); `test_worksheet_checker.py`;
L-252; L-418.

""" % {'n': n, 'today': TODAY, 'base': BASE_SHA}


def build_ledger(ledger):
    n_new = next_handle(ledger)
    # L-418: the build recorded; the Gap rewritten.
    a, b = block_span(ledger, 418)
    blk = ledger[a:b]
    g = blk.find('\n**Gap:**')
    r = blk.find('\n**Ref:**', g)
    if g < 0 or r < 0:
        raise Refuse(f"ANCHOR FAIL: {LEDGER}: L-418: Gap or Ref line not "
                     f"found.")
    blk = (blk[:g + 1] + (L418_BUILT % {'base': BASE_SHA}) + L418_GAP
           + blk[r + 1:])
    ledger = ledger[:a] + blk + ledger[b:]
    say(f"ok  {LEDGER:52s} L-418: the build recorded; Gap rewritten")
    ledger = meta_edit(ledger, 418)
    # The new item goes right after L-418.
    a, b = block_span(ledger, 418)
    ledger = ledger[:b] + new_item(n_new) + ledger[b:]
    say(f"ok  {LEDGER:52s} L-{n_new}: opened, the checker's one word for two cases")
    # L-390: landed, closed.
    a, b = block_span(ledger, 390)
    blk = ledger[a:b]
    g = blk.find('\n**Gap:**')
    r = blk.find('\n**Ref:**', g)
    if g < 0 or r < 0:
        raise Refuse(f"ANCHOR FAIL: {LEDGER}: L-390: Gap or Ref line not found.")
    blk = blk[:g + 1] + L390_LANDED + blk[r + 1:]
    ledger = ledger[:a] + blk + ledger[b:]
    say(f"ok  {LEDGER:52s} L-390: landed; Gap none")
    ledger = meta_edit(ledger, 390, status='DONE', section='C')
    # L-371: the two sentences landed.
    ledger = block_edit(ledger, 371,
                        "**Gap:** (1) PRINTS or DRAWN entries for the 11 not-followed pointers.",
                        L371_LANDED + "**Gap:** (1) PRINTS or DRAWN entries for the 11 not-followed pointers.",
                        'the two skill sentences landed')
    ledger = meta_edit(ledger, 371)
    # L-351: what landed struck, what is owed added.
    ledger = block_edit(
        ledger, 351,
        "  - provenance-discipline: the range rule's example names a removed\n"
        "    range row; a patch's \"what the run should say\" predicts the\n"
        "    scanner's CHANGE, not its total (both L-371); the conversion marker\n"
        "    and the widening (L-390); the scanner's window and declared rows\n"
        "    (L-414, if the fix is method there).\n",
        "  - provenance-discipline: the scanner's window and declared rows\n"
        "    (L-414, if the fix is method there). The range rule's example and\n"
        "    the scanner's change (both L-371) and the conversion marker (L-390)\n"
        "    landed at 2.27 on 2026-10-08 (L-418).\n",
        'provenance-discipline: what landed at 2.27')
    ledger = block_edit(
        ledger, 351,
        "    of that day. L-418's split cuts this skill at 1.18.\n",
        "    of that day. 1.18 (L-418, 2026-10-08) carried the read plan and\n"
        "    reference-file conventions; nothing is owed.\n",
        'ledger-and-session-records: 1.18 landed')
    ledger = block_edit(
        ledger, 351,
        "  - interactive-exhibit and the protocol: as above.\n",
        "  - gallery-cache-builder, interactive-exhibit,\n"
        "    orrery-coding-conventions, safe-file-editing: a read plan at the\n"
        "    next version, and the skill comes off PLAN_NOT_YET in\n"
        "    skills_index.py in the same patch (L-418; Tony, 2026-10-08).\n"
        "  - interactive-exhibit and the protocol: as above.\n",
        'the four long skills owe a read plan')
    ledger = meta_edit(ledger, 351)
    # The header stamp, above the RICE line every stamp sits above.
    ledger = edit(
        ledger, "Review and RICE update Tony 6-21-2026\n",
        "Module updated: October 8, 2026 with Anthropic's Claude Opus 5.5\n"
        "(L-418: the provenance-discipline split built -- 2.27,\n"
        "provenance-cross-check 1.0, ledger-and-session-records 1.18,\n"
        "protocol v3.86; L-390 closed; L-371 and L-351 updated; L-%d opened,\n"
        "the checker's one word for two cases), built on %s.\n"
        "Review and RICE update Tony 6-21-2026\n" % (n_new, BASE_SHA),
        LEDGER, 'header stamp')
    return ledger, n_new


# ---------- Where We Are: by section, nothing below the marker ----------

MARKER = '--- Your run record below this line.'


def build_wwa(wwa, n_new):
    if wwa.count(MARKER) != 1:
        raise Refuse(f"ANCHOR FAIL: {WWA}: the run-record marker was not "
                     f"found once.")
    cut = wwa.index(MARKER)
    top, tail = wwa[:cut], wwa[cut:]       # tail is Tony's and is not edited
    # Header: whoever closes last owns these two lines.
    m = re.search(r'^Last updated: [^\n]*\n- Written at [^\n]*\n(  [^\n]*\n)*',
                  top, re.M)
    if not m:
        raise Refuse(f"ANCHOR FAIL: {WWA}: the header lines were not found.")
    top = (top[:m.start()]
           + "Last updated: October 8, 2026, after the provenance split's build.\n"
             "- Written at orrery %s and gallery ab66aba7, before your run of\n"
             "  patch_L418_3.\n" % BASE_SHA + top[m.end():])
    say(f"ok  {WWA:52s} header date")
    # The box: what changed.
    head = "> **Changed since you last read this:**\n"
    if top.count(head) != 1:
        raise Refuse(f"ANCHOR FAIL: {WWA}: the box's 'Changed since' line "
                     f"was not found once.")
    mine = (
        "> - The provenance skill is split in two, so each part can be read\n"
        ">   whole. A new skill, provenance-cross-check, holds the procedure\n"
        ">   for checks by other models. Nothing in either was reworded.\n"
        "> - Three small fixes ride along: two from L-371 (the Sun room's\n"
        ">   served numbers), one from L-390 (the conversion marker), and\n"
        ">   your L-252 paragraph on the checker's four outcomes.\n"
        "> - Long skill files now open with a reading plan, and the check\n"
        ">   fails when one is missing or wrong. Four long skills get theirs\n"
        ">   at their next version.\n"
        "> - New item: L-%d (the checker's one word for two cases).\n" % n_new)
    old_list = (
        "> - 15 of the 17 typed facts are served with their sources and live,\n"
        ">   in three website patches. You found every hover's words correct.\n"
        "> - Earth's four drawn guides have Read more links: the Sun\n"
        ">   Direction, the rotation axis, the day-night line and the Moon.\n"
        "> - Their sources reach the panel now; they had been served but not\n"
        ">   shown. The panel's words and footer are brighter.\n"
        "> - The inner Oort cloud is drawn flat, but a 2025 paper finds it\n"
        ">   tilted about 30 degrees. You ruled it is redrawn now, as part of\n"
        ">   the Sun's slice.\n")
    if top.count(head + old_list) == 1:
        top = top.replace(head + old_list, head + mine)
        say(f"ok  {WWA:52s} box: changed since you last read this")
    else:
        top = top.replace(head, head + mine)
        say(f"ok  {WWA:52s} box: changed since you last read this "
            f"(added above the other session's lines)")
    # The box: what needs Tony now.
    need = "> **Needs you now:**\n"
    if top.count(need) != 1:
        raise Refuse(f"ANCHOR FAIL: {WWA}: 'Needs you now' was not found once.")
    mine_need = (
        "> - *Run patch_L418_3, then orrery_maintenance_run.py, and push.*\n"
        "> - *Install three skills: provenance-discipline,\n"
        ">   provenance-cross-check (new) and ledger-and-session-records.\n"
        ">   Then replace the Project's instructions with\n"
        ">   PROJECT_INSTRUCTIONS.md.*\n")
    old_need = "> - *Run this closing patch, then orrery_maintenance_run.py, and push.*\n"
    if top.count(need + old_need) == 1:
        top = top.replace(need + old_need, need + mine_need)
    else:
        top = top.replace(need, need + mine_need)
    say(f"ok  {WWA:52s} box: needs you now")
    # Settled: two standing rulings of today.
    st = "Standing rulings. A line leaves after a few weeks, once it is habit.\n"
    top = edit(top, st, st +
               "- Small fixes owed to a skill ride the version a session is already\n"
               "  making; a change to a checker gets its own session. (Oct 8)\n"
               "- A long skill gets its reading plan at its next version, not in a\n"
               "  bump of its own. (Oct 8)\n", WWA, 'settled: two rulings')
    # Signals: the owed tool belongs to L-414, not to this bump.
    top = edit(top,
               "  prints the number on the gate path alone; that is owed on the\n"
               "  provenance-discipline bump.\n",
               "  prints the number on the gate path alone; that is owed to L-414\n"
               "  (the scanner's window), not to the split.\n",
               WWA, 'signals: who owes the gate-path count')
    # Where the details are: the split's record.
    anchor = "- The reasoning behind the order:\n"
    top = edit(top, anchor,
               "- The provenance split: L-418 (splitting provenance-discipline),\n"
               "  built and waiting on your run; record\n"
               "  `documentation/HANDOFF_L418_split_build_20261008.md`\n" + anchor,
               WWA, 'where the details are: the split')
    return top + tail


HANDOFF_TEXT = """\
<!-- Doc-Kind: hand | Session record: the provenance-discipline split built (L-418), the install trial and the read limit, 2026-10-08. -->
# Handoff: the provenance-discipline split, built (L-418)

Built on orrery %(base)s at
https://github.com/tonylquintanilla/palomas_orrery (branch main). The
gallery, ab66aba7 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, was read
for its swap log only and not changed.

- Type: BUILD. One patch, `patch_L418_3_split_build_20261008.py`.
- Companion to `documentation/HANDOFF_L418_split_build_brief_20261008.md`
  (the brief this session followed),
  `documentation/PREDESIGN_L418_provenance_skill_split_20261006.md` (the
  design) and `documentation/HANDOFF_L418_skill_split_design_20261006.md`.
- Skills read by this session, each loaded copy checked against the
  manifest and the repo byte for byte: provenance-discipline 2.26,
  ledger-and-session-records 1.17, safe-file-editing 1.13,
  agentic-pre-test 1.3.
- October 8, 2026, with Anthropic's Claude Opus 5.5. A parallel
  session (the ledger-session-records decisions session) ran the same
  evening; its note of 2026-10-08 carried two rulings here.

## Verified in this session

- **The install trial passed.** install-probe was installed:
  `references/probe.md` arrived beside SKILL.md, md5
  dc4f6011467ccc53f5b84f8a776b352b, holding the recorded sentence. Its
  manifest source was "plugin", the same as all eleven of Tony's
  skills, so the result speaks for them. Tony then deleted it.
- **The read limit.** This session's Read tool returned the first
  25,000 tokens of a file and announced the cut. On
  provenance-discipline 2.26 that was lines 1 to 1,106, 55,748
  characters. The design's viewer showed 16,000 characters from the
  start and the end. Read plans use the smaller: 16,000 characters and
  2,000 lines per part. The measurement and its date are written beside
  the limits in skills_index.py.
- **The patch, on throwaway copies of the repo:** the split moves
  fifteen sections and finds each whole in its new file; the 23 listed
  edits are each printed; a final check proves every section is its
  original plus exactly those edits. skills_index.py --check then ends
  "OK: 12 skills parsed". Each new check was shown failing first: a
  part over one read, lines in no part, an unfilled seed, a long file
  with no plan, a reference named and missing, a reference present and
  unnamed, a stray file in a skill folder, and a bad annotation example
  inside a reference file.
- **The L-252 paragraph checked against the code.** Three of its four
  definitions match `worksheet_checker.py`. UNCHECKED_MOVE is reached
  by two different cases, and Tony split the bullet into them.

## What changed

- provenance-discipline 2.27: the Review-Repair Protocol out to the new
  skill provenance-cross-check 1.0 (its three reference sections in
  `references/worksheets.md`); Rules 1 to 8 of the figure count to
  `references/figures.md`; the field notes to
  `references/field-notes.md`; the withdrawn derived-row rule and the
  v2.24 entry to `documentation/SKILL_HISTORIES.md`. A new heading,
  Cross-Checked Lines in the Store, keeps the two rules that fire on
  ordinary edits. Riding it: the range rule's examples (L-371), predict
  the scanner's change (L-371), the conversion marker (L-390), and the
  status-line and figures examples, which named rows since changed.
- provenance-cross-check 1.0: the protocol, with the L-252 paragraph
  beside the send-back rule.
- ledger-and-session-records 1.18: the read plan and reference files
  as conventions; the Anchor Requirement names provenance-cross-check
  for review prompts; its v1.15 entry to SKILL_HISTORIES.md.
- skills_index.py: writes and checks read plans, checks reference
  files, reads annotation examples in reference files, and lists
  provenance-cross-check after provenance-discipline in the manifest.
  PLAN_NOT_YET names gallery-cache-builder, interactive-exhibit,
  orrery-coding-conventions and safe-file-editing.
- PROJECT_INSTRUCTIONS.md v3.86; v3.83 to the history file.
- Ledger: L-418 records the build; L-390 closed; L-371 and L-351
  updated; L-%(n)d opened (the checker's one word for two cases).

## Departures from the brief

- The brief said a phase-2 edit inside a moved section is refused.
  L-390's sentences and the L-252 paragraph both fall inside moved
  text, so the patch proves each section equals its original with
  exactly the listed edits instead.
- The brief named three versions to cut. Tony's ruling of 2026-10-06
  had said every skill over 16,000 characters gets a read plan; four
  more skills are that long, and each would have needed its own bump.
  Tony: plans at their next version ("confirmed as recommended").
- Where We Are's attention marks were left as found. A parallel session
  edits the same page tonight, and clearing its marks would hide its
  changes. The next close resets them.

## Next session

- Confirm the loaded copies read provenance-discipline 2.27,
  provenance-cross-check 1.0 and ledger-and-session-records 1.18.
- List both skill folders under the mounted skills and find the three
  reference files.
- On the first figures task, say whether `references/figures.md` was
  opened before a `# Figures:` line was written. Then L-418 closes.

## Tony-actions (rollup)

- **(do)** Run the patch, then orrery_maintenance_run.py; move the
  patch into documentation/; commit and push.
- **(do)** Install three skills from ZIPs: provenance-discipline,
  provenance-cross-check (new), ledger-and-session-records.
- **(do)** Replace the Project's instructions with PROJECT_INSTRUCTIONS.md.
- **(decide)** L-%(n)d (the checker's one word for two cases): whether
  the checker itself prints two different words.

## Tony's notes carried from Where We Are

- None: this patch edits the page by section, and no line it edits
  carried a note.

Session record written October 2026 with Anthropic's Claude Opus 5.5.
"""


def build_records(ledger, wwa):
    if (ROOT / HANDOFF).exists():
        raise Refuse(f"ERROR: {HANDOFF} already exists, so this patch has "
                     f"already run.")
    print()
    ledger, n_new = build_ledger(ledger)
    wwa = build_wwa(wwa, n_new)
    handoff = HANDOFF_TEXT % {'base': BASE_SHA, 'n': n_new}
    say(f"ok  {HANDOFF:52s} the session's handoff (new)")
    return ledger, wwa, {HANDOFF: handoff}


NEXT_STEPS = """\
NEXT:
  1. Run orrery_maintenance_run.py -- it rebuilds the ledger's index
     and moves L-390 into the closed section. Every gating checker
     should pass, and "Skill headers" should say 12 skills.
  2. Move this script into documentation/; commit and push.
  3. Make three ZIPs and install them in Settings, under Skills. In
     File Explorer, right-click each folder in skills/, then Send to,
     then Compressed (zipped) folder:
       skills/provenance-discipline       (replace the installed one)
       skills/provenance-cross-check      (new)
       skills/ledger-and-session-records  (replace the installed one)
  4. Replace the Project's instructions with PROJECT_INSTRUCTIONS.md
     (now v3.86).
"""


# ============================================================
# BUILD
# ============================================================

def build_split(pd_text):
    pieces = split_pd(pd_text)
    p = pieces
    files = {
        PD: (p['HEAD'] + p['REPORT'] + FIGURES_POINTER + "\n" + p['STORE']
             + XC_IN_PD + "\n" + p['RETIRES'] + p['VERIFIED'] + FIELD_POINTER),
        PD_FIG: FIG_HEAD + body(p['FIGCOUNT']),
        PD_FN: FN_HEAD + body(p['FIELD']),
        XC: (XC_HEAD + p['REVIEW'] + p['LINK'] + p['THREE'] + p['TWO']
             + p['NEG'] + p['ROUTE'] + p['QUOTE'] + p['FORMAT']
             + p['EXHIBIT'] + body(p['CREDIT'])),
        XC_WS: WS_HEAD + p['ROLES'] + p['TYPES'] + body(p['BATCH']),
    }
    dest = {'HEAD': PD}
    dest.update({k: d for k, _, d in PIECES})
    # PHASE 1: every piece arrived whole in its destination.
    moved = []
    for key, d in dest.items():
        if d == SH:
            continue                      # checked where SH is written
        if body(p[key]) not in files[d]:
            raise Refuse(f"ERROR: phase 1: {key} did not arrive whole in {d}.")
        if d != PD:
            moved.append(key)
    say(f"ok  phase 1: {len(moved)} sections moved, each found whole in its "
        f"new file: {', '.join(moved)}")
    say(f"ok  phase 1: 6 pieces stay in {PD}: HEAD, REPORT, STORE, RETIRES, "
        f"VERIFIED (and the text above the first)")
    return pieces, dest, files


def run_phase2(files, extra):
    """Apply PHASE2 to the in-memory files. `extra` holds texts not built
    by the split (the ledger skill). Returns the list of edits applied as
    (file, old, new) for the final check."""
    texts = dict(files)
    texts.update(extra)
    applied = []
    print("\nPHASE 2 -- the listed edits, each shown before and after:\n")
    for rel, label, old, new in PHASE2:
        new = new.replace('@@P_L252@@\n', P_L252.rstrip('\n') + '\n\n')
        texts[rel] = edit(texts[rel], old, new, rel, label, show=True)
        applied.append((rel, old, new))
    return texts, applied


def final_check(pieces, dest, texts, applied):
    """Each piece now equals its original with exactly the listed edits
    that fall inside it, and every listed edit fell inside one piece or
    inside text this patch added."""
    used = {i: 0 for i in range(len(applied))}
    for key, d in dest.items():
        if d == SH:
            continue
        want = body(pieces[key])
        for i, (rel, old, new) in enumerate(applied):
            if rel == d and old in want:
                want = want.replace(old, new)
                used[i] += 1
        if want not in texts[d]:
            raise Refuse(f"ERROR: final check: {key} in {d} is not its "
                         f"original with the listed edits.")
    for i, (rel, old, new) in enumerate(applied):
        if used[i] > 1:
            raise Refuse(f"ERROR: final check: edit {i + 1} fell in two "
                         f"sections.")
    inside = sum(1 for i in used if used[i])
    other = sum(1 for rel, _, _ in applied if rel not in
                {d for d in dest.values()})
    say(f"ok  final check: every section is its original plus the listed "
        f"edits and nothing else. Of {len(applied)} edits, {inside} fell "
        f"inside a section of provenance-discipline 2.26, "
        f"{len(applied) - inside - other} in text this patch adds, and "
        f"{other} in ledger-and-session-records")


def build_histories(sh, pieces, lsr_v115):
    sh = edit(sh, "\n## interactive-exhibit\n",
              SH_PD_INTRO_V224 + V224 + SH_PD_INTRO_WITHDRAWN
              + body(pieces['WITHDRAWN']) + "\n## interactive-exhibit\n",
              SH, 'provenance-discipline: v2.24 entry and the withdrawn rule')
    sh = edit(sh, "\n## gallery-cache-builder\n",
              SH_LSR_INTRO + lsr_v115 + "\n## gallery-cache-builder\n",
              SH, 'ledger-and-session-records: v1.15 entry')
    if body(pieces['WITHDRAWN']) not in sh:
        raise Refuse("ERROR: phase 1: WITHDRAWN did not arrive whole in "
                     "SKILL_HISTORIES.md.")
    return sh


def main():
    print(f"patch_L418_3 -- built on orrery {BASE_SHA}\n")
    try:
        if (ROOT / 'skills' / 'provenance-cross-check').exists():
            raise Refuse("ERROR: skills/provenance-cross-check already exists, "
                         "so this patch has already run.")
        if P_L252 is None:
            raise Refuse("ERROR: the L-252 paragraph is not filled in.")
        src = {}
        for rel in (PD, LSR, SI, PI, PIH, SH, LEDGER, WWA):
            src[rel], crlf = read_lf(rel)
            if crlf:
                say(f"note: {rel} was CRLF in the working copy; it is "
                    f"written LF")
        for rel, want in BASE_MD5.items():
            if md5(src[rel]) != want:
                raise Refuse(f"ERROR: {rel} is not the version this patch was "
                             f"built against (orrery {BASE_SHA}).")
        say(f"ok  base: {', '.join(BASE_MD5)} match orrery {BASE_SHA}")

        pieces, dest, files = build_split(src[PD])
        texts, applied = run_phase2(files, {LSR: src[LSR]})
        final_check(pieces, dest, texts, applied)

        print()
        sh = build_histories(src[SH], pieces, V115)
        si = src[SI]
        for i, (old, new) in enumerate(SKILLS_INDEX_EDITS, 1):
            si = edit(si, old, new, SI, f'read plan and reference checks, '
                      f'edit {i} of {len(SKILLS_INDEX_EDITS)}')
        pi, pih = build_protocol(src[PI], src[PIH])
        ledger, wwa, extra_files = build_records(src[LEDGER], src[WWA])

        out = {PD: texts[PD], PD_FIG: texts[PD_FIG], PD_FN: texts[PD_FN],
               XC: texts[XC], XC_WS: texts[XC_WS], LSR: texts[LSR],
               SH: sh, SI: si, PI: pi, PIH: pih, LEDGER: ledger, WWA: wwa}
        out.update(extra_files)
        for rel, text in out.items():
            ascii_check(rel, text)
    except Refuse as exc:
        print(f"\n{exc}\nNOTHING was written.")
        sys.exit(1)

    for rel, text in out.items():
        path = ROOT / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'w', encoding='utf-8', newline='') as f:
            f.write(text)
    print(f"\npatch applied: {len(out)} files written:")
    for rel in out:
        print(f"  {rel}")

    print("\nskills_index.py -- writes the read plans and the manifest:\n")
    r = subprocess.run([sys.executable, 'skills_index.py'], cwd=ROOT,
                       capture_output=True, text=True)
    print(r.stdout + r.stderr)
    print("skills_index.py --check:\n")
    r2 = subprocess.run([sys.executable, 'skills_index.py', '--check'],
                        cwd=ROOT, capture_output=True, text=True)
    print(r2.stdout + r2.stderr)
    if r.returncode or r2.returncode:
        print("skills_index.py reported a problem, above. The files are "
              "written; tell Claude what it printed.\nUndo is Discard "
              "Changes in GitHub Desktop.")
        sys.exit(1)
    print(NEXT_STEPS)


if __name__ == '__main__':
    main()
