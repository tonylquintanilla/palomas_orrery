<!-- Doc-Kind: hand | Session record for L-440: the dashboard's cards, the website checks' six headings, the run names on the buttons, the orrery's console window, and the Dashboard parity check. -->
# L-440: the dashboard's labels, short lines and headings

Built on orrery db63721d258004b855c1259371d8adf15bf7647c at
https://github.com/tonylquintanilla/palomas_orrery ("L437 close"). The
gallery was read at 924977a353b6c3e7d50e360e840fe176685f97c9 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io and is not
touched. Pushed at: Tony's commit after running the patch; the next
session reads it with `git ls-remote`.
Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`;
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.
Written October 13, 2026 with Anthropic's Claude Opus 5.5.

- Type: BUILD (design and build in one session).
- Brief: `documentation/HANDOFF_dashboard_labels_brief_20261012.md`, with
  `documentation/AUDIT_dashboard_labels_20261012.md`. Coordination:
  `documentation/HANDOFF_scaffolding_sessions_coordination_20261013.md`.
- Patch: `patch_L440_1_dashboard_labels_20261013.py` (one, the orrery).
- Skills loaded and matched against the manifest: safe-file-editing 1.13,
  agentic-pre-test 1.3, ledger-and-session-records 1.20,
  orrery-coding-conventions 1.10. No skill or protocol version changes.

## 1. What Tony asked, and what he ruled

His request of 2026-10-12: labels you can recognize from the script,
pithy descriptions, and a way to find a tool besides the search.

His rulings in this session, 2026-10-13, in his words:

- Where the paragraph goes: option B, "+ more" opens it inside the card.
  "B. Confirmed." He saw both options rendered at desktop width and at a
  9:16 width first ("Can you show me the cards in 9:16 view like a
  phone?"), and noted "this is only a desktop App!"
- The website checks group: six headings, in his order. "i would order
  them: 4, 5, 3, 1, 2. the logic is manual use first tools, then
  generated reports, then checks in pipeline order: jpl checks, then
  served data, then gallery renders." And: "i would also make these
  groups collapsible but keeping the indentation method." The split of
  JPL's check from the served cache: "confirmed as recommended."
- The "when" index: "record for later."
- The console window, from his note read with the brief, then narrowed:
  "the way it works now is okay ... what i wanted was for the orrery to
  also open a console window instead of just the dashboard status." Only
  Paloma's Orrery moved; every other button runs as it did.
- Already ruled before the session: "Test" comes off the checker labels
  (ruling 5, `DESIGN_rulings_20261012.md`), and a button is named what
  the run prints (the same record).

## 2. What the patch does

- **Every card**: its name; the repository and script it runs, in small
  type (the same text the Launch button's tooltip shows); one short line
  of at most twelve words from CARD_LINES; "+ more" opens the full
  paragraph in place and "- less" closes it. Text wraps to the window's
  width, and the Launch button is packed first. Before, the paragraph
  wrapped at a fixed 600 pixels, which in a narrow window pushed every
  Launch button off the card (seen in the 9:16 render).
- **Headings fold.** A heading inside a group is a button: "-" open, "+"
  folded. Every heading starts open at launch, so what a runner runs
  stays visible (Tony's ruling of 2026-08-12). Folding is not remembered.
  A search keeps the heading above each match.
- **The website checks group** has six headings, cards alphabetical
  under each: TOOLS YOU RUN BY HAND (Daily Run Steps, Guest Book Checks,
  Store Editor Suite, Store Writer Suite); THE MODULE ATLAS (Module
  Atlas); JPL'S CHECK OF THE OBJECTS (Horizons Check Suite, Horizons
  Confirmations); THE SERVED CACHE (Artifact 1 Assembler, Cache Builder
  Suite, Cache In Step, Cache Siblings); FROM THE ORRERY (Config Mirror --
  report only, Config Mirror Check, Constants Export Pull, Drawings,
  Drawings Pull, Mirror Suite, Objects Export Pull, Objects Mirror Check,
  Objects Mirror Suite, Pointer Join, Pole of Date); THE ROOMS (Arrival,
  Collapsed Features, Display Figures, Earth Scene Geometry, Feature
  Renderers, Hover Budget, Page Framing, Solar System Drawer, Solar
  System Figures, Sun Shells). The two runners stay at top and bottom.
- **Buttons renamed to the run's names** (29): in the orrery group, Ledger
  Index, Skill Manifest, Module Atlas, Constants Change, Constants
  Relations, Derived Figures, Constants Export Check, Objects Export
  Check, Skill Headers, Exact Rows by the Count, Dimensions, Cross-Check
  Annotations, Citation Inheritance, Status Lines, Row Shape, Scanner
  Recognition 1d/1e, Scanner Row Run, Reset Completeness, Orbit Cache,
  Earth Pole of Date, Hills Cloud Sampler, Drawings Export Check,
  Position Digits, Worksheet Checker Tests; in the website group, Cache
  Builder Suite, Drawings, Artifact 1 Assembler, Module Atlas; in the
  Daily Run, Cache Builder. The orrery's generators and checkers are
  re-sorted alphabetically under the new names (the 2026-09-12 rule).
  Five descriptions that named an old label now name the new one.
- **The run rows keep their names.** The brief allowed renaming poorly
  named rows in both places. With the script now printed on each card,
  the modes of one script read apart on their own ("exact_rows_report.py
  --check"), so no row was renamed and the website repository is not
  touched. Standalone tools outside the runs keep their labels too.
- **Paloma's Orrery** opens its own console window, kept open after the
  program closes, as the maintenance run's button does. On macOS and
  Linux no new window opens; the output goes to the terminal the
  dashboard was started from.
- **Dashboard parity**, new: `test_dashboard_parity.py`, the run's
  "Dashboard parity" row and the "Dashboard Parity" button. It reads both
  runners, the Daily Run and the dashboard, edits nothing, and fails on:
  a step with no button of its name; a button running a different script
  or arguments; an indented button naming no step; a script not on disk;
  a card with no short line, one over twelve words, or a line for no
  card; a file it cannot read. Four steps are covered by a differently
  named button on purpose and printed on every run: Config mirror and
  Objects mirror (their buttons run the report-only form; the run does
  the writing) and the two guest book checks (one button, L-281). Not
  compared: the website's three live checks, which are functions inside
  the live run.
- The maintenance run's GATING AND REPORT-ONLY paragraph is left as it
  is: since L-269 it names no count, and the run counts its rows itself.

## 3. The short lines, and how they were checked

Each of the 107 lines was written from its script's own module
docstring, read at db63721d by a script that printed every button's
description beside the first lines of its script's docstring, not from
the dashboard's paragraph alone. Where the docstring and the paragraph
differed in emphasis the docstring won (Add Module Docstrings: its
default mode is the Role/Domain tag sweep). Dashboard parity holds the
twelve-word limit; on its first run it caught two of these lines at
thirteen words, which were shortened before delivery.

## 4. Verified, and how

- The patch on a throwaway copy of both repositories at db63721d / 924977a3:
  every edit "ok"; a second run refuses and writes nothing.
- Every one of the 106 existing entries survives with the same fields;
  only its label (the 29 renames), five description words, and the
  orrery's console flag change; one entry is added. Proved by loading the
  old and new LAUNCH_GROUPS side by side.
- `test_dashboard_parity.py` on the patched copy: 9 of 9 planted faults
  caught, each by its own kind of finding; 77 steps (39 orrery, 34
  website, 4 Daily Run) matched by name and script; 107 cards with a line.
- The dashboard under xvfb, on the copy: 107 Launch buttons, 0 Not
  Found; 107 "+ more"; eight headings, all open at launch; folding and
  reopening work; "+ more" opens and "- less" closes; a search for
  "parity" finds 1 under CHECKERS and one for "jpl" 11 under their own
  headings; Clear brings all 107 back; at 560 pixels wide all 107 Launch
  buttons stay inside the window.
- py_compile on the dashboard, the runner and the new checker; all files
  ASCII and LF.
- Not run here: the whole orrery maintenance run (the sandbox lacks the
  orrery's scientific libraries). Your run is the check of the other 26
  rows.

## 5. Other sessions' work this session met

- The handle. This work was first delivered as patch_L438_1 on
  082dbb15, under L-438, then the next free number in the ledger. A
  brief pushed the same day, `HANDOFF_L438_objects_to_website_brief_20261013.md`,
  claims L-438, and the master plan restamp brief names L-439, so this
  work is L-440. patch_L438_1 never ran; Tony deletes it from
  documentation/. This patch replaces it, rebuilt on db63721d.
- L-269's replacement (patch_L269_5, run before this one) added the
  Maintenance Report button and row; its card gets its short line
  here, and the run's GATING AND REPORT-ONLY paragraph, which no
  longer names a number, is left as it is.
- L-437 ran before this patch and added Domain Split; its button gets its
  short line here, and its row is in the parity count.
- How a later patch adds a button now: the entry in LAUNCH_GROUPS, its
  line in CARD_LINES, keyed by the same group and label, and, under a
  runner, the run's own name. In the website group, under a heading.

## 6. Your look

- Open `palomas_orrery_dashboard.py` with Run.
- Each card: the name, the script in small grey type under it, one short
  line, and "+ more" beside the name. Click "+ more" on any card: the
  paragraph opens under the line and the link reads "- less".
- Scroll to Gallery -- checks and data: six headings, each starting with
  "-". Click one: its cards fold away and it starts with "+".
- Maintenance Run: GENERATORS and CHECKERS fold the same way; the
  checkers read without "Test" and run in alphabetical order.
- Type "jpl" in Find a tool and press Enter: the matches show under
  their headings.
- Make the window narrow: the Launch buttons stay on the cards.
- Launch Paloma's Orrery: a console window opens beside it and carries
  its printed output.
- Your verdicts, in your run record, one per line: the card; "+ more";
  the six headings and their order; folding; the console window.

## 7. Tony-actions

- (do) Delete `documentation/patch_L438_1_dashboard_labels_20261013.py`
  (never run; replaced by this patch).
- (do) Save `patch_L440_1_dashboard_labels_20261013.py` in the orrery
  folder and Run it; paste the output into your run record.
- (do) Run `orrery_maintenance_run.py`: every gating checker passes,
  Dashboard parity among them with 9 of 9 planted faults caught.
- (do) The look, section 6.
- (decide) The look.
- (do) Move the patch into `documentation/`; commit and push.
- (decide, recorded for later) The "when" index, generated from tags.

Session record written October 2026 with Anthropic's Claude Opus 5.5.
