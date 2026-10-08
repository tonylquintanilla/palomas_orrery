#!/usr/bin/env python3
"""
patch_L418_2_split_design_close_20261006.py -- ORRERY repo. Closes the
skills sweep session of 2026-10-06: the ledger, Where We Are, the
split's design and this session's record. No code and no skill changes.

Built on orrery fbd223eee7cb8823439c17d64fa23bb5e04110eb at
https://github.com/tonylquintanilla/palomas_orrery. The gallery is not
touched.

HOW TO RUN IT
    Save this file in the ORRERY repo ROOT (next to palomas_orrery.py),
    open it in VS Code and click Run (the command is
    python patch_L418_2_split_design_close_20261006.py). Then follow the
    NEXT steps it prints.

YOUR NOTES ARE NEVER REFUSED (L-419)
    Neither the ledger nor Where We Are is checked by a fingerprint of
    the whole file. Each is matched only at the lines this patch edits.
    If you wrote a note on, or between, the lines being replaced, the
    patch carries it word for word into this session's handoff, prints
    it, and goes on.
    It refuses only if Where We Are is not the October 6 Earth website
    version it updates (for example, if another session closed first),
    or if an edited line cannot be found at all.

WHAT CHANGES
    LEDGER_CONSOLIDATED.md   L-418 records the design and your ruling;
        a header stamp.
    documentation/WHERE_WE_ARE.md   the Read-this-first box, Right now,
        the next steps, Waiting on you and Where the details are; the
        old marks cleared from The road.
    documentation/PREDESIGN_L418_provenance_skill_split_20261006.md
        written with your ruling. If you already saved the first copy,
        it is replaced by the ruled one; if you edited it, yours is kept.
    documentation/HANDOFF_L418_skill_split_design_20261006.md   new: this
        session's record and the install trial's instructions.

    Permanent: the two documents and the ledger entry. The script itself
    is spent once it has run.

SUCCESS looks like: one "ok" line per edit, any carried notes, then
"patch applied". FAILURE looks like: one ERROR: or ANCHOR FAIL: line,
and NOTHING is written. Undo is Discard Changes in GitHub Desktop.

Written October 6, 2026 with Anthropic's Claude Opus 5.5.
"""

import difflib
import os
import sys

ROOT_MARKERS = ("palomas_orrery.py", "LEDGER_CONSOLIDATED.md")
LEDGER = "LEDGER_CONSOLIDATED.md"
WWA = "documentation/WHERE_WE_ARE.md"
DESIGN = "documentation/PREDESIGN_L418_provenance_skill_split_20261006.md"
HANDOFF = "documentation/HANDOFF_L418_skill_split_design_20261006.md"
WWA_MARKER = "Last updated: October 6, 2026, end of the Earth website session."

DESIGN_ORIG = '<!-- Doc-Kind: hand | Design for splitting provenance-discipline: what moves where, and the size after each move (L-418), 2026-10-06. -->\n# Design: splitting provenance-discipline (L-418)\n\nBuilt on orrery fbd223eee7cb8823439c17d64fa23bb5e04110eb at\nhttps://github.com/tonylquintanilla/palomas_orrery. DESIGN SESSION:\nno code written, no file changed. October 6, 2026, with Anthropic\'s\nClaude Opus 5.5.\n\nSupersedes nothing. It answers the item L-418 left open: moving\nprovenance-discipline\'s two long procedures into files loaded only\nwhen needed.\n\n## Read this first\n\n- *Needs you now: a ruling on the five points at the end, under\n  "Rulings asked for".*\n- *Do next, once ruled: the install trial (step 0 of the build order),\n  before any skill is changed.*\n- provenance-discipline is 137,837 characters. One read of a file\n  shows 16,000 of them, from the start and the end.\n- After the moves below, what loads when the skill fires drops from\n  roughly 34,000 tokens to roughly 15,000.\n- No rule is reworded. Every section moves word for word, as L-418 did.\n- The rules that remain still do not fit in one read. A read plan at\n  the top of the file, written by skills_index.py, makes reading them\n  whole reliable.\n\n## Why this matters for accuracy\n\n- The skill is 2,591 lines, five times Anthropic\'s 500-line guideline.\n- The file viewer cuts any file over 16,000 characters from the\n  middle. A plain read of this skill sees about one-ninth of it.\n- The middle is where most of the rules are. So the skill that guards\n  facts and sources is the one least likely to be read whole.\n- The start of a file is always seen. That is why the read plan goes\n  there.\n\n## What moves where\n\n### 1. A new skill: provenance-cross-check\n\n- **What it is.** The Review-Repair Protocol: preparing worksheets and\n  prompts that send values to GPT, Gemini or another Claude for an\n  independent check, and writing the `# Cross-checked:` lines that come\n  back.\n- **Why a separate skill.** It is a different job with a different\n  trigger. It happens only when a relay is being prepared or its return\n  adjudicated. Today it loads into every session that touches a\n  citation.\n- **Its SKILL.md, 23,918 characters,** holds these ten sections:\n  - Review-Repair Protocol for Cross-Checked Annotations (the opening)\n  - A Link Is an Object, Not Text [QUALITY]\n  - Three Things the Prompt Must Require [QUALITY]\n  - The Two-Dispatch Rule [CRITICAL]\n  - A Negative Verdict Shows Its Search [CRITICAL]\n  - Route the Effort Tier by Job Type [QUALITY]\n  - Quoting a Worksheet Is Transcription, Not Interpretation [CRITICAL]\n  - Cross-Checked Annotation Format [CRITICAL]\n  - The Exhibit Requirement [CRITICAL]\n  - Model Credit in Annotations [PRACTICE]\n- **Its reference file, `references/worksheets.md`, 12,067\n  characters,** holds three reference sections, opened when writing a\n  worksheet prompt or choosing which models to send it to:\n  - Model Roles in the Competitive Pattern\n  - Worksheet Types\n  - Batch Worksheet Workflow\n- **Two sections from the relay part stay in provenance-discipline,**\n  because they fire on ordinary edits, not only during a relay:\n  - A Cross-Check Retires With Its Value or Its Citation [CRITICAL].\n    It applies whenever a value or citation carrying a\n    `# Cross-checked:` line is changed.\n  - Retired: `# Verified: April 2026 via Gemini fact-check`. It says\n    to replace that stamp on sight.\n\n### 2. `references/figures.md` inside provenance-discipline\n\n- **What moves:** The Figure Count Is a Declared Field, Rules 1 to 8,\n  32,951 characters.\n- **What stays in SKILL.md:**\n  - Report to the Figures You Have [QUALITY], the core rule: compute at\n    full precision, report to what the least precise input supports,\n    and a subtraction is governed by decimal places.\n  - The Store Carries the Verified Figure [CRITICAL].\n- **The pointer that stays:** "Before writing or checking a\n  `# Figures:` line, deriving a value, or printing a number in a\n  display, read `references/figures.md`."\n- **The backstop is partial, stated plainly.** Rule 8\'s checker,\n  test_derived_figures.py, judges the declarations on DERIVED rows even\n  if a session never opened the file. It does not judge measured rows\n  or what a display prints. Those depend on the pointer firing.\n\n### 3. `references/field-notes.md` inside provenance-discipline\n\n- **What moves:** Field Notes, 7,062 characters. These are lessons,\n  not rules.\n\n### 4. To documentation/SKILL_HISTORIES.md\n\n- **What moves:** A Derived Row Stores the Figure Its Sources Support\n  -- WITHDRAWN, 674 characters. A withdrawn rule is history.\n\n## Sizes after the moves\n\n- **provenance-discipline SKILL.md:** 137,837 characters becomes about\n  61,200, plus a few hundred for the pointers. Roughly 15,000 tokens,\n  read in four parts.\n- **provenance-cross-check SKILL.md:** about 25,400 characters with its\n  header, read in two parts. It loads only for relay work.\n- **The three reference files** cost nothing until opened.\n\n## Reading the rules whole: a read plan at the top\n\n- skills_index.py writes one line under each long skill\'s version\n  line, for example: "Read this file in 4 parts: lines 1-310,\n  311-640, 641-980, 981-1240."\n- Each part ends at a heading and stays under 16,000 characters.\n- The line sits at the top of the file, inside the part every read\n  shows, so the instruction is always seen.\n- `skills_index.py --check` fails if a part is over 16,000 characters,\n  or if the parts leave any line uncovered.\n- It applies to every skill over 16,000 characters, so the other five\n  long skills get it without anything moving.\n\n## New checks, each shown failing before it is trusted\n\n- **References exist.** Every file a SKILL.md names under\n  `references/` is in the folder, and every file in the folder is named\n  by its SKILL.md. Today skills_index.py reads only SKILL.md, so a\n  pointer to a missing file would pass silently.\n- **Moved text is unchanged.** The patch compares every moved section,\n  before and after, ignoring line endings, as L-418 did.\n- **The read plan,** as above.\n\n## Installing a skill with extra files\n\n- Settings takes a ZIP of the skill\'s folder, with the folder itself at\n  the top of the ZIP. In File Explorer: right-click the folder, then\n  Send to, then Compressed (zipped) folder.\n- **Not yet known:** whether your account keeps the extra files. This\n  session shows Anthropic\'s own skills arriving with theirs. Your\n  eleven arrive with one file each, because each folder holds only\n  SKILL.md.\n- **The trial settles it first (step 0).** A throwaway skill,\n  `install-probe`, holds SKILL.md and `references/probe.md` with one\n  known sentence. You install it; the next fresh session lists the\n  folder and reads the sentence; then you delete the skill.\n- If the extra file does not arrive, the build stops. The moves would\n  otherwise leave rules where no session can reach them.\n\n## Edits elsewhere\n\n- **ledger-and-session-records,** under Anchor Requirement: "a\n  provenance review needs provenance-discipline" also names\n  provenance-cross-check for review prompts.\n- **The protocol:** a version entry and the manifest\'s twelfth row,\n  written by skills_index.py. No rule changes.\n- **No edit needed** where other files cite moved sections by name\n  (interactive-exhibit citing Rule 3; test_derived_figures.py\'s\n  docstring). The sections keep their names; only their file changes.\n\n## Considered and not recommended\n\n- **Splitting the scanner and push gate into a skill of their own.**\n  Eight sections, 14,208 characters, would fit one read: The\n  Visibility Convention, The Gate Binds at EXPORT, Uncited Goes to the\n  Ledger, A Simple Error a Check Finds Is Fixed and Reported, The Goal\n  State, Clearing a Flagged Claim, Scanner Mechanics, and Report Domain\n  Classification.\n- **Against it:** clearing a scanner finding means writing a citation,\n  which needs the rules for storing a value. The two would fire\n  together most of the time. That means two loads, a second install,\n  and a chance that one of them does not fire, for little saving.\n- **Rewording rules to shorten them.** The paragraphs that are plainly\n  origin stories come to only 4,663 characters. Real savings would mean\n  rewriting rule text, which L-418 deliberately did not do. It would\n  need its own review, by another model, section by section.\n\n## Not in this design\n\n- **The other five long skills** get the same treatment once this one\n  has proved out. Their sizes: interactive-exhibit 50,371;\n  safe-file-editing 35,546; orrery-coding-conventions 32,894;\n  ledger-and-session-records 32,871; gallery-cache-builder 25,169.\n- **The protocol,** 69,507 characters, read on every turn of every\n  session. A separate design.\n\n## Build order\n\n0. The install trial, as above.\n1. One patch: the moves, the new skill, the two new checks and the read\n   plan in skills_index.py, the ledger-and-session-records pointer, the\n   L-418 ledger update, WHERE_WE_ARE.md, and the protocol entry.\n   Versions: provenance-discipline 2.27, provenance-cross-check 1.0,\n   ledger-and-session-records 1.17.\n2. You run it, push, and install two ZIPs and one updated skill.\n3. The next session confirms the loaded versions, that both folders\n   hold their files, and, on its first figures task, that it opened\n   `references/figures.md`.\n\n## Rulings asked for\n\n1. A new skill, provenance-cross-check, with the scope above.\n2. The three moves into reference files and the one into\n   SKILL_HISTORIES.md.\n3. The read plan at the top of every long skill, and its check.\n4. Not splitting off the scanner and push gate.\n5. The install trial before the build.\n\nDesign written October 2026 with Anthropic\'s Claude Opus 5.5.\n'
DESIGN_RULED = '<!-- Doc-Kind: hand | Design for splitting provenance-discipline: what moves where, and the size after each move (L-418), 2026-10-06. -->\n# Design: splitting provenance-discipline (L-418)\n\nBuilt on orrery fbd223eee7cb8823439c17d64fa23bb5e04110eb at\nhttps://github.com/tonylquintanilla/palomas_orrery. DESIGN SESSION:\nno code written, no file changed. October 6, 2026, with Anthropic\'s\nClaude Opus 5.5.\n\nSupersedes nothing. It answers the item L-418 left open: moving\nprovenance-discipline\'s two long procedures into files loaded only\nwhen needed.\n\n## Read this first\n\n- *Ruled 2026-10-06: all five points confirmed (see "Ruled" at the\n  end).*\n- *Do next, once ruled: the install trial (step 0 of the build order),\n  before any skill is changed.*\n- provenance-discipline is 137,837 characters. One read of a file\n  shows 16,000 of them, from the start and the end.\n- After the moves below, what loads when the skill fires drops from\n  roughly 34,000 tokens to roughly 15,000.\n- No rule is reworded. Every section moves word for word, as L-418 did.\n- The rules that remain still do not fit in one read. A read plan at\n  the top of the file, written by skills_index.py, makes reading them\n  whole reliable.\n\n## Why this matters for accuracy\n\n- The skill is 2,591 lines, five times Anthropic\'s 500-line guideline.\n- The file viewer cuts any file over 16,000 characters from the\n  middle. A plain read of this skill sees about one-ninth of it.\n- The middle is where most of the rules are. So the skill that guards\n  facts and sources is the one least likely to be read whole.\n- The start of a file is always seen. That is why the read plan goes\n  there.\n\n## What moves where\n\n### 1. A new skill: provenance-cross-check\n\n- **What it is.** The Review-Repair Protocol: preparing worksheets and\n  prompts that send values to GPT, Gemini or another Claude for an\n  independent check, and writing the `# Cross-checked:` lines that come\n  back.\n- **Why a separate skill.** It is a different job with a different\n  trigger. It happens only when a relay is being prepared or its return\n  adjudicated. Today it loads into every session that touches a\n  citation.\n- **Its SKILL.md, 23,918 characters,** holds these ten sections:\n  - Review-Repair Protocol for Cross-Checked Annotations (the opening)\n  - A Link Is an Object, Not Text [QUALITY]\n  - Three Things the Prompt Must Require [QUALITY]\n  - The Two-Dispatch Rule [CRITICAL]\n  - A Negative Verdict Shows Its Search [CRITICAL]\n  - Route the Effort Tier by Job Type [QUALITY]\n  - Quoting a Worksheet Is Transcription, Not Interpretation [CRITICAL]\n  - Cross-Checked Annotation Format [CRITICAL]\n  - The Exhibit Requirement [CRITICAL]\n  - Model Credit in Annotations [PRACTICE]\n- **Its reference file, `references/worksheets.md`, 12,067\n  characters,** holds three reference sections, opened when writing a\n  worksheet prompt or choosing which models to send it to:\n  - Model Roles in the Competitive Pattern\n  - Worksheet Types\n  - Batch Worksheet Workflow\n- **Two sections from the relay part stay in provenance-discipline,**\n  because they fire on ordinary edits, not only during a relay:\n  - A Cross-Check Retires With Its Value or Its Citation [CRITICAL].\n    It applies whenever a value or citation carrying a\n    `# Cross-checked:` line is changed.\n  - Retired: `# Verified: April 2026 via Gemini fact-check`. It says\n    to replace that stamp on sight.\n\n### 2. `references/figures.md` inside provenance-discipline\n\n- **What moves:** The Figure Count Is a Declared Field, Rules 1 to 8,\n  32,951 characters.\n- **What stays in SKILL.md:**\n  - Report to the Figures You Have [QUALITY], the core rule: compute at\n    full precision, report to what the least precise input supports,\n    and a subtraction is governed by decimal places.\n  - The Store Carries the Verified Figure [CRITICAL].\n- **The pointer that stays:** "Before writing or checking a\n  `# Figures:` line, deriving a value, or printing a number in a\n  display, read `references/figures.md`."\n- **The backstop is partial, stated plainly.** Rule 8\'s checker,\n  test_derived_figures.py, judges the declarations on DERIVED rows even\n  if a session never opened the file. It does not judge measured rows\n  or what a display prints. Those depend on the pointer firing.\n\n### 3. `references/field-notes.md` inside provenance-discipline\n\n- **What moves:** Field Notes, 7,062 characters. These are lessons,\n  not rules.\n\n### 4. To documentation/SKILL_HISTORIES.md\n\n- **What moves:** A Derived Row Stores the Figure Its Sources Support\n  -- WITHDRAWN, 674 characters. A withdrawn rule is history.\n\n## Sizes after the moves\n\n- **provenance-discipline SKILL.md:** 137,837 characters becomes about\n  61,200, plus a few hundred for the pointers. Roughly 15,000 tokens,\n  read in four parts.\n- **provenance-cross-check SKILL.md:** about 25,400 characters with its\n  header, read in two parts. It loads only for relay work.\n- **The three reference files** cost nothing until opened.\n\n## Reading the rules whole: a read plan at the top\n\n- skills_index.py writes one line under each long skill\'s version\n  line, for example: "Read this file in 4 parts: lines 1-310,\n  311-640, 641-980, 981-1240."\n- Each part ends at a heading and stays under 16,000 characters.\n- The line sits at the top of the file, inside the part every read\n  shows, so the instruction is always seen.\n- `skills_index.py --check` fails if a part is over 16,000 characters,\n  or if the parts leave any line uncovered.\n- It applies to every skill over 16,000 characters, so the other five\n  long skills get it without anything moving.\n\n## New checks, each shown failing before it is trusted\n\n- **References exist.** Every file a SKILL.md names under\n  `references/` is in the folder, and every file in the folder is named\n  by its SKILL.md. Today skills_index.py reads only SKILL.md, so a\n  pointer to a missing file would pass silently.\n- **Moved text is unchanged.** The patch compares every moved section,\n  before and after, ignoring line endings, as L-418 did.\n- **The read plan,** as above.\n\n## Installing a skill with extra files\n\n- Settings takes a ZIP of the skill\'s folder, with the folder itself at\n  the top of the ZIP. In File Explorer: right-click the folder, then\n  Send to, then Compressed (zipped) folder.\n- **Not yet known:** whether your account keeps the extra files. This\n  session shows Anthropic\'s own skills arriving with theirs. Your\n  eleven arrive with one file each, because each folder holds only\n  SKILL.md.\n- **The trial settles it first (step 0).** A throwaway skill,\n  `install-probe`, holds SKILL.md and `references/probe.md` with one\n  known sentence. You install it; the next fresh session lists the\n  folder and reads the sentence; then you delete the skill.\n- If the extra file does not arrive, the build stops. The moves would\n  otherwise leave rules where no session can reach them.\n\n## Edits elsewhere\n\n- **ledger-and-session-records,** under Anchor Requirement: "a\n  provenance review needs provenance-discipline" also names\n  provenance-cross-check for review prompts.\n- **The protocol:** a version entry and the manifest\'s twelfth row,\n  written by skills_index.py. No rule changes.\n- **No edit needed** where other files cite moved sections by name\n  (interactive-exhibit citing Rule 3; test_derived_figures.py\'s\n  docstring). The sections keep their names; only their file changes.\n\n## Considered and not recommended\n\n- **Splitting the scanner and push gate into a skill of their own.**\n  Eight sections, 14,208 characters, would fit one read: The\n  Visibility Convention, The Gate Binds at EXPORT, Uncited Goes to the\n  Ledger, A Simple Error a Check Finds Is Fixed and Reported, The Goal\n  State, Clearing a Flagged Claim, Scanner Mechanics, and Report Domain\n  Classification.\n- **Against it:** clearing a scanner finding means writing a citation,\n  which needs the rules for storing a value. The two would fire\n  together most of the time. That means two loads, a second install,\n  and a chance that one of them does not fire, for little saving.\n- **Rewording rules to shorten them.** The paragraphs that are plainly\n  origin stories come to only 4,663 characters. Real savings would mean\n  rewriting rule text, which L-418 deliberately did not do. It would\n  need its own review, by another model, section by section.\n\n## Not in this design\n\n- **The other five long skills** get the same treatment once this one\n  has proved out. Their sizes: interactive-exhibit 50,371;\n  safe-file-editing 35,546; orrery-coding-conventions 32,894;\n  ledger-and-session-records 32,871; gallery-cache-builder 25,169.\n- **The protocol,** 69,507 characters, read on every turn of every\n  session. A separate design.\n\n## Build order\n\n0. The install trial, as above.\n1. One patch: the moves, the new skill, the two new checks and the read\n   plan in skills_index.py, the ledger-and-session-records pointer, the\n   L-418 ledger update, WHERE_WE_ARE.md, and the protocol entry.\n   Versions: provenance-discipline 2.27, provenance-cross-check 1.0,\n   ledger-and-session-records 1.17.\n2. You run it, push, and install two ZIPs and one updated skill.\n3. The next session confirms the loaded versions, that both folders\n   hold their files, and, on its first figures task, that it opened\n   `references/figures.md`.\n\n## Rulings asked for\n\n1. A new skill, provenance-cross-check, with the scope above.\n2. The three moves into reference files and the one into\n   SKILL_HISTORIES.md.\n3. The read plan at the top of every long skill, and its check.\n4. Not splitting off the scanner and push gate.\n5. The install trial before the build.\n\n## Ruled\n\n- Tony, 2026-10-06: "Read and confirmed." All five points as\n  recommended.\n- Next: the install trial, then the build in a fresh session.\n\nDesign written October 2026 with Anthropic\'s Claude Opus 5.5.\n'
HANDOFF_TEXT = '<!-- Doc-Kind: hand | Session record: the skills sweep, the provenance-discipline split designed and ruled, and the install trial (L-418), 2026-10-06. -->\n# Handoff: the skills sweep and the provenance-discipline split (L-418)\n\nBuilt on orrery fbd223eee7cb8823439c17d64fa23bb5e04110eb at\nhttps://github.com/tonylquintanilla/palomas_orrery. The gallery was not\nread. DESIGN SESSION (zero code): no code and no skill changed.\nCompanion: `documentation/PREDESIGN_L418_provenance_skill_split_20261006.md`.\nOctober 6, 2026, with Anthropic\'s Claude Opus 5.5.\n\n## What Tony asked\n\n- Sweep the skills and the protocol so they fit the needs and abilities\n  of Claude Opus 5.5. Remove a skill if it is no longer needed, or add\n  improvements.\n- The aim: better accuracy and precision of facts and sources, and less\n  computational overhead where possible.\n\n## What was verified, not claimed\n\n- All eleven installed skills match `skills/<n>/SKILL.md` at fbd223ee\n  byte for byte, and their versions match the manifest.\n- That discharges the checks carried forward: interactive-exhibit 1.12\n  (v3.84), agentic-pre-test 1.3 (v3.83) and ledger-and-session-records\n  1.16 (v3.82).\n- Sizes, in characters: provenance-discipline 137,837;\n  interactive-exhibit 50,371; safe-file-editing 35,546;\n  orrery-coding-conventions 32,894; ledger-and-session-records 32,871;\n  gallery-cache-builder 25,169; gallery-assembler 14,451;\n  earth-system-pipeline 11,730; gallery-pipeline 8,537;\n  agentic-pre-test 6,518; horizons-orbital-mechanics 4,520. The\n  protocol is 69,507.\n- The file viewer shows at most 16,000 characters of a file per read,\n  taken from the start and the end.\n- Anthropic\'s pages, read this session: a custom skill is uploaded as a\n  ZIP of its folder; extra files in the folder enter the context only\n  when they are read, and SKILL.md should say when to read them.\n- In this session\'s sandbox, Anthropic\'s own skills arrive with their\n  extra files (the Word skill has 61; skill-creator has `references/`\n  and `scripts/`). Tony\'s eleven arrive under `/mnt/skills/plugins/`,\n  one file each.\n- Every skill area has open ledger items, so no skill is retired. The\n  quietest, earth-system-pipeline, has 9, among them L-001 and L-078,\n  and carries the human-cost restraint rule; gallery-pipeline has 13.\n\n## Found, not acted on\n\n- Anthropic\'s support page on creating custom skills gives the\n  description a 200-character maximum. The developer overview and\n  best-practices pages give 1,024, which L-417\'s check uses. Our\n  descriptions are longer than 200 and reach the session in full, so the\n  200 figure appears out of date. No change proposed.\n- Tony\'s skills are mounted under `/mnt/skills/plugins/`, not\n  `/mnt/skills/user/`, where uploaded skills usually appear. The trial\n  shows where an uploaded skill lands.\n- The protocol, 69,507 characters, is read on every turn of every\n  session. Its own design is not started.\n\n## Pushback, recorded\n\n- No rule is removed on the grounds that a newer model needs it less. A\n  model\'s say-so about its own reliability is not a check; it is the\n  same failure as a `# Source:` line over remembered data.\n\n## Rulings\n\n- Tony, "Confirmed as recommended": write the split as a design for his\n  ruling, with no code.\n- Tony, "Read and confirmed": all five points of the design.\n\n## The install trial\n\n- `install-probe.zip` holds `install-probe/SKILL.md` and\n  `install-probe/references/probe.md`. Tony keeps the ZIP out of the\n  repo: inside `skills/`, skills_index.py would add it to the manifest.\n- probe.md holds one line: "Probe sentence: the extra file arrived with\n  the skill. Token L418-probe-20261006-7c1d." Its md5, LF endings, is\n  dc4f6011467ccc53f5b84f8a776b352b.\n- The next session runs `find /mnt/skills -path \'*install-probe*\'` and\n  reports one of three results, in plain words:\n  - PASS: `references/probe.md` is listed and reads the sentence above.\n  - FAIL: SKILL.md arrived without the extra file.\n  - NOT INSTALLED: nothing found.\n- Then Tony deletes install-probe from Settings.\n- On FAIL, the split is not built and the design is reopened.\n\n## Next session\n\n- The trial check, then the split, built from the design\'s build order.\n- Versions to cut: provenance-discipline 2.27, provenance-cross-check\n  1.0, ledger-and-session-records 1.17. The protocol gets a version entry\n  and a twelfth manifest row.\n\n## Tony\'s notes carried from Where We Are\n\n{CARRIED}\n\nSession record written October 2026 with Anthropic\'s Claude Opus 5.5.\n'

NEXT = [
    "1. Move this script into documentation/.",
    "2. Run orrery_maintenance_run.py. This patch touches only the ledger",
    "   and three documents, so it should report as it did before.",
    "3. Commit and push.",
    "4. Install the trial skill: in Settings, under Skills, Upload skill,",
    "   and choose install-probe.zip. Keep the ZIP OUT of the repo folder;",
    "   inside skills/ it would be added to the manifest.",
    "5. Open a fresh chat in this Project and say: check the install probe.",
    "6. After that check, delete install-probe from Settings.",
]


def die(msg):
    print(msg)
    print("Nothing was written.")
    sys.exit(1)


def read_lf(path):
    with open(path, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    if "\r\n" in text:
        print(f"  note: {path} had Windows line endings; written back as LF.")
        text = text.replace("\r\n", "\n")
    return text


def matches(line, want):
    """A line matches if it is the expected text, or the expected text
    followed by a note of Tony's after a space."""
    return line == want or line.startswith(want + " ")


def replace_region(lines, expected, new, label, notes):
    """Replace the region that starts with expected[0] and ends with
    expected[-1]. Lines in the region that differ from what was expected
    are Tony's notes: carried, never refused."""
    starts = [i for i, l in enumerate(lines) if matches(l, expected[0])]
    if len(starts) != 1:
        die(f"ANCHOR FAIL: {label}: found {len(starts)} lines starting "
            f"{expected[0]!r}; expected exactly one.")
    s = starts[0]
    e = None
    if len(expected) == 1:
        e = s
    else:
        for j in range(s + 1, min(len(lines), s + len(expected) + 40)):
            if matches(lines[j], expected[-1]):
                e = j
                break
    if e is None:
        die(f"ANCHOR FAIL: {label}: no line starting {expected[-1]!r} "
            f"after {expected[0]!r}.")
    actual = lines[s:e + 1]
    sm = difflib.SequenceMatcher(a=expected, b=actual, autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag in ("replace", "insert"):
            for line in actual[j1:j2]:
                notes.append((label, line))
    lines[s:e + 1] = new
    print(f"  ok  {label}")


def insert_after(lines, anchor, new, label, notes, within=None):
    lo, hi = within if within else (0, len(lines))
    hits = [i for i in range(lo, hi) if matches(lines[i], anchor)]
    if len(hits) != 1:
        die(f"ANCHOR FAIL: {label}: found {len(hits)} lines starting "
            f"{anchor!r}; expected exactly one.")
    i = hits[0]
    if lines[i] != anchor:
        notes.append((label, lines[i]))
    lines[i + 1:i + 1] = new
    print(f"  ok  {label}")


def main():
    for m in ROOT_MARKERS:
        if not os.path.exists(m):
            die("ERROR: run this from the ORRERY repo root (next to "
                "palomas_orrery.py), not from documentation/.")

    notes = []
    writes = {}

    # ---------------- ledger ----------------
    led = read_lf(LEDGER).split("\n")
    head = [i for i, l in enumerate(led) if l.startswith("<!-- L:418 ")]
    if len(head) != 1:
        die(f"ANCHOR FAIL: ledger: found {len(head)} L-418 status lines.")
    h = head[0]
    end = next((j for j in range(h + 1, len(led)) if led[j].startswith("#### [L-")),
               len(led))
    insert_after(led,
        "  byte for byte. The item stays open only for the split.",
        [
        "- **2026-10-06, the split designed and ruled.** A design session at",
        "  orrery fbd223ee measured the skill: 137,837 characters, of which a",
        "  single read shows 16,000. The design is",
        "  `documentation/PREDESIGN_L418_provenance_skill_split_20261006.md`;",
        "  the record is `documentation/HANDOFF_L418_skill_split_design_20261006.md`.",
        "- **Tony's ruling, 2026-10-06 (\"Read and confirmed\"), all five",
        "  points:** a new skill, provenance-cross-check, holds the",
        "  Review-Repair Protocol, except A Cross-Check Retires With Its Value",
        "  or Its Citation and the retired `# Verified:` stamp, which stay",
        "  because they fire on ordinary edits; Rules 1 to 8 of the figure",
        "  count go to `references/figures.md` and the field notes to",
        "  `references/field-notes.md`; the withdrawn derived-row rule goes to",
        "  `documentation/SKILL_HISTORIES.md`; skills_index.py writes a read",
        "  plan at the top of every skill over 16,000 characters, and its",
        "  check fails on a part over 16,000 or a line left uncovered, and on",
        "  a reference file that is named and missing or present and unnamed;",
        "  the scanner and push gate are NOT split off; the install trial",
        "  comes first. No rule is reworded.",
        "- **The trial:** `install-probe.zip`, a throwaway skill with one extra",
        "  file. The next session checks it; Tony then deletes it.",
        "- **Still open:** the build, in a fresh session after the trial",
        "  passes. Versions to cut: provenance-discipline 2.27,",
        "  provenance-cross-check 1.0, ledger-and-session-records 1.17.",
        ], "ledger: L-418", notes, within=(h, end))
    insert_after(led,
        "Tony's runs; Tony's look at L-420 recorded), built on e7073fce.",
        [
        "Module updated: October 6, 2026 with Anthropic's Claude Opus 5.5",
        "(L-418: the provenance-discipline split designed and ruled; the",
        "install trial set), built on fbd223ee.",
        ], "ledger: header stamp", notes)
    writes[LEDGER] = "\n".join(led)

    # ---------------- Where We Are ----------------
    w = read_lf(WWA).split("\n")
    if not any(matches(l, WWA_MARKER) for l in w):
        die("ERROR: documentation/WHERE_WE_ARE.md is not the October 6 Earth "
            "website version this patch updates. Another session may have "
            "closed first. Ask this session to rebuild the patch.")

    replace_region(w, [
        "Last updated: October 6, 2026, end of the Earth website session.",
        "- Written at orrery e7073fce and gallery 38f1e7b0, after your runs of",
        "  the website patch and of the galactic-plane and panel-colour patches.",
    ], [
        "Last updated: October 6, 2026, end of the skills sweep session.",
        "- Written at orrery fbd223ee. This session only designed: no code and",
        "  no skill changed.",
    ], "Where We Are: header", notes)

    replace_region(w, [
        "> **READ THIS FIRST**",
        ">",
        "> **Changed this session:**",
        "> - Earth's website patch is live, and your look on the phone found it",
        ">   correct. The inner belt says \"trapped protons\", in your words, and",
        ">   Jupiter's belts no longer claim a measured distance.",
        "> - The saved Earth scene the checks use is re-recorded from the real",
        ">   data, with a tool that can remake it. That showed two hovers on the",
        ">   live site were already too tall for the phone; with your approved",
        ">   changes all three tall ones fit.",
        "> - A search of both rooms found 17 facts typed in the code instead of",
        ">   served with their sources. You ruled they are fixed now, as part of",
        ">   finishing the Earth and Sun rooms. The plan is written down for a",
        ">   fresh session.",
        "> - A written rule now says code may type only words about our picture;",
        ">   facts, papers and sources are served.",
        "> - In the orrery, from a session of its own: the Celestial Grid draws",
        ">   the galactic plane, a violet circle, with its poles, and the Star",
        ">   Background marks Sagittarius A*, the galaxy's centre.",
        "> - The desktop orrery opens on Linux and macOS again: its panels use",
        ">   one grey, gray90, that every system knows.",
        ">",
        "> **Do next:**",
        "> - *The typed facts, in a fresh session, from the plan written today.*",
        ">",
        "> **Needs you now:**",
        "> - *Run this closing patch in the orrery repo, reinstall",
        ">   interactive-exhibit, and replace the Project's instructions with",
        ">   v3.84.*",
    ], [
        "> **READ THIS FIRST**",
        ">",
        "> **Changed this session:**",
        "> - All eleven skills were checked against the repo and the manifest.",
        ">   All match, including the three new versions you installed.",
        "> - The longest skill, provenance-discipline, is too long to be read",
        ">   whole: one read of a file shows 16,000 characters, and the skill",
        ">   has 137,837. The skill that guards facts and sources is the one",
        ">   least likely to be read in full.",
        "> - You confirmed a design to split it. The cross-checking procedure",
        ">   becomes its own skill, two long sections move into files inside",
        ">   the skill's folder, and a read plan at the top says which lines to",
        ">   read in turn. No rule is reworded.",
        "> - No skill is retired: every one has open work behind it.",
        ">",
        "> **Do next:**",
        "> - *Install the trial skill, then check it in a fresh session.*",
        "> - *The typed facts, in a fresh session, from the plan written on",
        ">   October 6.*",
        ">",
        "> **Needs you now:**",
        "> - *Run this closing patch, then the maintenance run, and push.*",
        "> - *Install install-probe.zip from Settings, and keep it out of the",
        ">   repo.*",
    ], "Where We Are: Read this first", notes)

    replace_region(w, ["## The road  **>> UPDATED THIS SESSION**"],
                   ["## The road"], "Where We Are: road mark cleared", notes)
    replace_region(w, [
        "              confirmed.* << this session: the website patch is live;",
        "              the typed facts are the last part, with the design talks.",
    ], [
        "              confirmed.* The website patch is live; the typed facts",
        "              are the last part, with the design talks.",
    ], "Where We Are: road stage 5 mark cleared", notes)
    replace_region(w, [
        "              the served data, with their sources. << new this session",
    ], [
        "              the served data, with their sources.",
    ], "Where We Are: road stage 6 mark cleared", notes)

    replace_region(w, [
        "- The skill copies this session loaded all matched the repo, and the",
        "  ones you reinstalled read their new versions.",
    ], [
        "- The skills: all eleven match the repo and the manifest at fbd223ee.",
        "  - provenance-discipline is 137,837 characters, and one read shows",
        "    16,000, so most of its rules are not seen on a plain read.",
        "  - The split you confirmed takes it to about 61,000 characters and",
        "    moves the cross-checking procedure into a new skill,",
        "    provenance-cross-check.",
        "  - A read plan at the top of each long skill will say which lines to",
        "    read in turn, so the rest is read whole.",
        "  - First, a throwaway skill tests whether your account keeps the",
        "    extra files in a skill's folder.",
    ], "Where We Are: Right now", notes)

    replace_region(w, [
        "1. *Your run of this closing patch, and the reinstall.*",
    ], [
        "1. *Your run of this closing patch, and the trial skill's install.*",
    ], "Where We Are: next steps, item 1", notes)
    insert_after(w,
        "   `documentation/HANDOFF_L395_horizons_check_design_20261005.md`.",
        [
        "",
        "The provenance-discipline split is built in its own fresh session",
        "once the trial passes, from",
        "`documentation/PREDESIGN_L418_provenance_skill_split_20261006.md`.",
        "It can go before or after the two above; the order is yours.",
        ], "Where We Are: next steps, the split", notes)

    replace_region(w, [
        "Now:",
        "- Run this closing patch, run orrery_maintenance_run.py, commit and",
        "  push.",
        "- Reinstall interactive-exhibit (1.12) and replace the Project's",
        "  instructions with PROJECT_INSTRUCTIONS.md, now v3.84.",
    ], [
        "Now:",
        "- Run this closing patch, run orrery_maintenance_run.py, commit and",
        "  push.",
        "- Install the trial skill, install-probe.zip, from Settings. Keep the",
        "  ZIP out of the repo: inside skills/ it would join the manifest.",
        "- After the next session checks it, delete install-probe.",
    ], "Where We Are: Waiting on you", notes)

    replace_region(w, [
        "  - This session: L-413 (Earth's list), L-349 (the belt's words),",
        "    L-379 (the saved scene), L-300 (the collapsed-features check), L-292",
        "    (the geocorona note), L-421 (the typed facts, opened). Closed: L-349",
        "    (the belt's words), L-300 (the collapsed-features check), L-369",
        "    (Earth's tilt in words), L-415 and L-419 (skill rules confirmed).",
        "  - L-418 stays open only for splitting provenance-discipline's two",
        "    long procedures into their own files.",
    ], [
        "  - This session: L-418, the provenance-discipline split, designed and",
        "    confirmed. It stays open until the split is built.",
        "  - Earth's website session: L-413 (Earth's list), L-349 (the belt's",
        "    words), L-379 (the saved scene), L-300 (the collapsed-features",
        "    check), L-292 (the geocorona note), L-421 (the typed facts,",
        "    opened). Closed: L-349, L-300, L-369 (Earth's tilt in words), L-415",
        "    and L-419 (skill rules confirmed).",
    ], "Where We Are: details, handles", notes)
    replace_region(w, [
        "- This session's record:",
        "  `documentation/HANDOFF_L413_earth_website_20261006.md`",
    ], [
        "- This session's record:",
        "  `documentation/HANDOFF_L418_skill_split_design_20261006.md`",
        "- The split's design:",
        "  `documentation/PREDESIGN_L418_provenance_skill_split_20261006.md`",
        "- Earth's website session's record:",
        "  `documentation/HANDOFF_L413_earth_website_20261006.md`",
    ], "Where We Are: details, records", notes)
    writes[WWA] = "\n".join(w)

    # ---------------- the design ----------------
    if os.path.exists(DESIGN):
        cur = read_lf(DESIGN)
        if cur == DESIGN_RULED:
            print(f"  ok  {DESIGN}: already the ruled copy")
        elif cur == DESIGN_ORIG:
            writes[DESIGN] = DESIGN_RULED
            print(f"  ok  {DESIGN}: your first copy replaced by the ruled one")
        else:
            print(f"  ok  {DESIGN}: you edited it, so your copy is kept")
    else:
        writes[DESIGN] = DESIGN_RULED
        print(f"  ok  {DESIGN}: written")

    # ---------------- the handoff ----------------
    if notes:
        carried = "\n".join(f"- {lab}: \"{line}\"" for lab, line in notes)
    else:
        carried = "- None: the lines this patch edited carried no notes."
    ho = HANDOFF_TEXT.replace("{CARRIED}", carried)
    if os.path.exists(HANDOFF):
        if read_lf(HANDOFF) != ho:
            die(f"ERROR: {HANDOFF} already exists and differs.")
        print(f"  ok  {HANDOFF}: already present")
    else:
        writes[HANDOFF] = ho
        print(f"  ok  {HANDOFF}: written")

    for text in writes.values():
        bad = [c for c in set(text) if ord(c) > 127]
        if bad and text is not writes.get(LEDGER) and text is not writes.get(WWA):
            die(f"ERROR: non-ASCII characters in a new document: {bad}")

    total = 0
    for path, text in writes.items():
        data = text.encode("utf-8")
        with open(path, "wb") as f:
            f.write(data)
        total += len(data)

    print(f"Notes of yours carried into the handoff: {len(notes)}")
    for lab, line in notes:
        print(f"  {lab}: {line}")
    print("Stamps updated: the ledger's header stamp; Where We Are's"
          " 'Last updated' lines.")
    print(f"patch applied ({total} bytes in {len(writes)} files)")
    print("NEXT")
    for s in NEXT:
        print(s)


if __name__ == "__main__":
    main()
