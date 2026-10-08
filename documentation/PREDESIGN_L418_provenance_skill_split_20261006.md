<!-- Doc-Kind: hand | Design for splitting provenance-discipline: what moves where, and the size after each move (L-418), 2026-10-06. -->
# Design: splitting provenance-discipline (L-418)

Built on orrery fbd223eee7cb8823439c17d64fa23bb5e04110eb at
https://github.com/tonylquintanilla/palomas_orrery. DESIGN SESSION:
no code written, no file changed. October 6, 2026, with Anthropic's
Claude Opus 5.5.

Supersedes nothing. It answers the item L-418 left open: moving
provenance-discipline's two long procedures into files loaded only
when needed.

## Read this first

- *Ruled 2026-10-06: all five points confirmed (see "Ruled" at the
  end).*
- *Do next, once ruled: the install trial (step 0 of the build order),
  before any skill is changed.*
- provenance-discipline is 137,837 characters. One read of a file
  shows 16,000 of them, from the start and the end.
- After the moves below, what loads when the skill fires drops from
  roughly 34,000 tokens to roughly 15,000.
- No rule is reworded. Every section moves word for word, as L-418 did.
- The rules that remain still do not fit in one read. A read plan at
  the top of the file, written by skills_index.py, makes reading them
  whole reliable.

## Why this matters for accuracy

- The skill is 2,591 lines, five times Anthropic's 500-line guideline.
- The file viewer cuts any file over 16,000 characters from the
  middle. A plain read of this skill sees about one-ninth of it.
- The middle is where most of the rules are. So the skill that guards
  facts and sources is the one least likely to be read whole.
- The start of a file is always seen. That is why the read plan goes
  there.

## What moves where

### 1. A new skill: provenance-cross-check

- **What it is.** The Review-Repair Protocol: preparing worksheets and
  prompts that send values to GPT, Gemini or another Claude for an
  independent check, and writing the `# Cross-checked:` lines that come
  back.
- **Why a separate skill.** It is a different job with a different
  trigger. It happens only when a relay is being prepared or its return
  adjudicated. Today it loads into every session that touches a
  citation.
- **Its SKILL.md, 23,918 characters,** holds these ten sections:
  - Review-Repair Protocol for Cross-Checked Annotations (the opening)
  - A Link Is an Object, Not Text [QUALITY]
  - Three Things the Prompt Must Require [QUALITY]
  - The Two-Dispatch Rule [CRITICAL]
  - A Negative Verdict Shows Its Search [CRITICAL]
  - Route the Effort Tier by Job Type [QUALITY]
  - Quoting a Worksheet Is Transcription, Not Interpretation [CRITICAL]
  - Cross-Checked Annotation Format [CRITICAL]
  - The Exhibit Requirement [CRITICAL]
  - Model Credit in Annotations [PRACTICE]
- **Its reference file, `references/worksheets.md`, 12,067
  characters,** holds three reference sections, opened when writing a
  worksheet prompt or choosing which models to send it to:
  - Model Roles in the Competitive Pattern
  - Worksheet Types
  - Batch Worksheet Workflow
- **Two sections from the relay part stay in provenance-discipline,**
  because they fire on ordinary edits, not only during a relay:
  - A Cross-Check Retires With Its Value or Its Citation [CRITICAL].
    It applies whenever a value or citation carrying a
    `# Cross-checked:` line is changed.
  - Retired: `# Verified: April 2026 via Gemini fact-check`. It says
    to replace that stamp on sight.

### 2. `references/figures.md` inside provenance-discipline

- **What moves:** The Figure Count Is a Declared Field, Rules 1 to 8,
  32,951 characters.
- **What stays in SKILL.md:**
  - Report to the Figures You Have [QUALITY], the core rule: compute at
    full precision, report to what the least precise input supports,
    and a subtraction is governed by decimal places.
  - The Store Carries the Verified Figure [CRITICAL].
- **The pointer that stays:** "Before writing or checking a
  `# Figures:` line, deriving a value, or printing a number in a
  display, read `references/figures.md`."
- **The backstop is partial, stated plainly.** Rule 8's checker,
  test_derived_figures.py, judges the declarations on DERIVED rows even
  if a session never opened the file. It does not judge measured rows
  or what a display prints. Those depend on the pointer firing.

### 3. `references/field-notes.md` inside provenance-discipline

- **What moves:** Field Notes, 7,062 characters. These are lessons,
  not rules.

### 4. To documentation/SKILL_HISTORIES.md

- **What moves:** A Derived Row Stores the Figure Its Sources Support
  -- WITHDRAWN, 674 characters. A withdrawn rule is history.

## Sizes after the moves

- **provenance-discipline SKILL.md:** 137,837 characters becomes about
  61,200, plus a few hundred for the pointers. Roughly 15,000 tokens,
  read in four parts.
- **provenance-cross-check SKILL.md:** about 25,400 characters with its
  header, read in two parts. It loads only for relay work.
- **The three reference files** cost nothing until opened.

## Reading the rules whole: a read plan at the top

- skills_index.py writes one line under each long skill's version
  line, for example: "Read this file in 4 parts: lines 1-310,
  311-640, 641-980, 981-1240."
- Each part ends at a heading and stays under 16,000 characters.
- The line sits at the top of the file, inside the part every read
  shows, so the instruction is always seen.
- `skills_index.py --check` fails if a part is over 16,000 characters,
  or if the parts leave any line uncovered.
- It applies to every skill over 16,000 characters, so the other five
  long skills get it without anything moving.

## New checks, each shown failing before it is trusted

- **References exist.** Every file a SKILL.md names under
  `references/` is in the folder, and every file in the folder is named
  by its SKILL.md. Today skills_index.py reads only SKILL.md, so a
  pointer to a missing file would pass silently.
- **Moved text is unchanged.** The patch compares every moved section,
  before and after, ignoring line endings, as L-418 did.
- **The read plan,** as above.

## Installing a skill with extra files

- Settings takes a ZIP of the skill's folder, with the folder itself at
  the top of the ZIP. In File Explorer: right-click the folder, then
  Send to, then Compressed (zipped) folder.
- **Not yet known:** whether your account keeps the extra files. This
  session shows Anthropic's own skills arriving with theirs. Your
  eleven arrive with one file each, because each folder holds only
  SKILL.md.
- **The trial settles it first (step 0).** A throwaway skill,
  `install-probe`, holds SKILL.md and `references/probe.md` with one
  known sentence. You install it; the next fresh session lists the
  folder and reads the sentence; then you delete the skill.
- If the extra file does not arrive, the build stops. The moves would
  otherwise leave rules where no session can reach them.

## Edits elsewhere

- **ledger-and-session-records,** under Anchor Requirement: "a
  provenance review needs provenance-discipline" also names
  provenance-cross-check for review prompts.
- **The protocol:** a version entry and the manifest's twelfth row,
  written by skills_index.py. No rule changes.
- **No edit needed** where other files cite moved sections by name
  (interactive-exhibit citing Rule 3; test_derived_figures.py's
  docstring). The sections keep their names; only their file changes.

## Considered and not recommended

- **Splitting the scanner and push gate into a skill of their own.**
  Eight sections, 14,208 characters, would fit one read: The
  Visibility Convention, The Gate Binds at EXPORT, Uncited Goes to the
  Ledger, A Simple Error a Check Finds Is Fixed and Reported, The Goal
  State, Clearing a Flagged Claim, Scanner Mechanics, and Report Domain
  Classification.
- **Against it:** clearing a scanner finding means writing a citation,
  which needs the rules for storing a value. The two would fire
  together most of the time. That means two loads, a second install,
  and a chance that one of them does not fire, for little saving.
- **Rewording rules to shorten them.** The paragraphs that are plainly
  origin stories come to only 4,663 characters. Real savings would mean
  rewriting rule text, which L-418 deliberately did not do. It would
  need its own review, by another model, section by section.

## Not in this design

- **The other five long skills** get the same treatment once this one
  has proved out. Their sizes: interactive-exhibit 50,371;
  safe-file-editing 35,546; orrery-coding-conventions 32,894;
  ledger-and-session-records 32,871; gallery-cache-builder 25,169.
- **The protocol,** 69,507 characters, read on every turn of every
  session. A separate design.

## Build order

0. The install trial, as above.
1. One patch: the moves, the new skill, the two new checks and the read
   plan in skills_index.py, the ledger-and-session-records pointer, the
   L-418 ledger update, WHERE_WE_ARE.md, and the protocol entry.
   Versions: provenance-discipline 2.27, provenance-cross-check 1.0,
   ledger-and-session-records 1.17.
2. You run it, push, and install two ZIPs and one updated skill.
3. The next session confirms the loaded versions, that both folders
   hold their files, and, on its first figures task, that it opened
   `references/figures.md`.

## Rulings asked for

1. A new skill, provenance-cross-check, with the scope above.
2. The three moves into reference files and the one into
   SKILL_HISTORIES.md.
3. The read plan at the top of every long skill, and its check.
4. Not splitting off the scanner and push gate.
5. The install trial before the build.

## Ruled

- Tony, 2026-10-06: "Read and confirmed." All five points as
  recommended.
- Next: the install trial, then the build in a fresh session.

Design written October 2026 with Anthropic's Claude Opus 5.5.
