<!-- Doc-Kind: hand | Brief for the Claude Code session that installs the reduced protocol Tony ratified on November 23, 2026 (L-522, step 3): the protocol, where its old lines go, the skills tool, three skills, the doors, the records. Communication; orders, with Tony's rulings in his words. -->
# Brief: install the reduced protocol (L-522, step 3)

Built on orrery `7087b3adda80fb91a9e0c413dc74a15092982537`
at https://github.com/tonylquintanilla/palomas_orrery (branch main)
and gallery `a811d350db2f3fd296ae5f71c10bc3afd3ce2063`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Record both bases yourself; nights commit on both, so either may have
moved, and that is not a missed push.

Tony Quintanilla, PE | written by the coordinating session, Claude
Fable 5.2 | 2026-11-23 | Handle: L-522 (document caps), step 3.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: BUILD, the direct form (Claude Code, Claude Opus 5.5, through the
python_work door, working in the orrery). Three parts, Tony's go-ahead
after each. Nothing here is a design question; where the brief and the
files disagree, stop and say so.

## What Tony ratified

- The text: `documentation/DRAFT_PROJECT_INSTRUCTIONS_reduced_20261123.md`,
  the fourth draft, 795 lines, 42,945 bytes, sha256
  `f36e51c745f95d702fca3eca338694556ed6011cf01e693b0ce440eb31f68c83`.
  Tony, Nov 23, 18:16: "ratified. thanks."
- CHECK THIS FIRST. The coordinating session placed that file from a
  linked session and could not read it back. Take its sha256 in the
  folder. If it differs, stop: the bytes on disk are not what he
  ratified.
- Five more files of that session sit in `documentation`, untracked,
  with their sizes in bytes. A clean `git status` apart from these
  seven is what to expect:
  `REVIEW_COMPARE_fundamental_documents_20261123.md` 15,104;
  `DESIGN_protocol_reduction_what_moves_20261123.md` 20,991;
  `DESIGN_protocol_reduction_items_for_tony_20261123.md` 24,036;
  `REVIEW_REQUEST_protocol_cold_read_20261123.md` 4,076;
  `REVIEW_RETURN_cold_read_20261123.md` 10,297; and this brief.
  A size that differs is reported, not repaired.
- Read before building: the draft, whole; the items file's two
  sections of Tony's answers; `DESIGN_protocol_reduction_rulings_20261110.md`.
  The rest is there if a question comes up.
- Skills this job fires: ledger-and-session-records and
  safe-file-editing in full; orrery-coding-conventions and
  agentic-pre-test in the parts Part 2 edits. You run under the present
  protocol, v3.145, until Tony installs the new one.

## Part 1: the protocol, and where its old lines go

1. THE OLD TEXT IS ALREADY KEPT WHOLE.
   `documentation/project_instructions_v3_145.md` equals the root
   `PROJECT_INSTRUCTIONS.md` byte for byte at 7087b3ad. Confirm it
   still does before anything is overwritten.
2. THE NEW PROTOCOL. `PROJECT_INSTRUCTIONS.md` becomes the draft, with
   these fills and nothing else changed:
   - line 1 is the protocol's own comment: `<!-- Doc-Kind: zoned | The
     protocol. How a session is run, which checks are load-bearing,
     and why. Carries the generated list of skill names. -->`
   - line 3's "DRAFT of the reduced protocol (vNEXT)" becomes `v4.0`,
     and `vNEXT` in Version History likewise. That number is the
     coordinator's suggestion; Tony changes it with a word.
   - `LANDING-DATE`, in six places, is the day you install it, written
     2026-11-xx like the dates beside it. Line 3's date too.
   - "Cut from 7087b3ad" names the commit you build on.
   Its archived copy, by the standing practice, is
   `documentation/project_instructions_v4_0.md`.
3. PROJECT_ORIGIN.md gains, at its end, one new heading, "The
   protocol's philosophy, as it stood until <date>", and under it
   these old line ranges, word for word, in this order: 1012-1017,
   1040-1048, 1053-1089, 1095-1108, 1132-1165, 1191-1196. Tony's own
   account above it is not touched. Its first-line description gains
   "and the protocol's philosophy as it stood until November 2026".
4. `documentation/PROJECT_INSTRUCTIONS_HISTORY.md`:
   - PART 1 gains the three resident entries, old lines 1269-1393, in
     its own order, and one new entry for v4.0: what was reduced, by
     whose rulings, and where each kind of line went.
   - A new PART 3, "The stories behind the rules, and the rules
     retired, moved 2026-11-xx", holds every other old line that is
     not kept, word for word, in the old order, each run under the
     heading it stood under: 1-8, 57-212, 233-251, 257-315, 331-341,
     346, 348-354, 356, 358-359, 361-367, 371-383, 388-397, 412-483,
     587-602, 614-652, 707-712, 744-808, 906-915, 940-950, 973-977,
     986-995, 1166-1178, 1207-1254 less 1252, 1258-1268.
   - Not copied: 484-586, the skill table, which a tool writes; and
     1007-1008, two blank lines.
   - The file's opening list of its parts gains PART 3. One sentence
     there says that PART 2's "STILL STATED IN: Part 4" pointers now
     lead to PROJECT_ORIGIN.md for the passages that moved.
5. THE ACCOUNT, by a throwaway script, printed in your report: every
   non-blank line of `project_instructions_v3_145.md` outside 484-586
   is found in the new protocol, in PART 1 or PART 3 of the history
   file, or in PROJECT_ORIGIN.md. Name any line found nowhere. The
   coordinating session's own count: 459 old lines kept in place, 106
   to PROJECT_ORIGIN.md, 827 to history with the table's 103 among
   them, 2 blank.
6. `skills_index.py`:
   - it writes the table of skills, versions and "fires when" to a
     generated file, `skills/SKILL_MANIFEST.md`, and no longer into
     the protocol;
   - it writes the twelve names, two to a line, between the protocol's
     new markers `SKILL-NAMES:START` and `SKILL-NAMES:END`;
   - `--check` fails when a folder under `skills/` is missing from the
     names, or a name has no folder; it no longer compares versions
     with the protocol. Show both able to fail on a throwaway copy.
   - Follow it outward. Known places that speak of the table in the
     protocol or of re-uploading it: `orrery_maintenance_run.py`
     (lines 348-349, 521-524, about 977-984, 1087),
     `palomas_orrery_dashboard.py` (lines 212, 1788-1790, 2223-2224,
     2716), `doc_index.py` (comments at 34, 42, 68). Search the tree
     for `SKILL-MANIFEST` and "Skill Manifest" for the rest. Dashboard
     parity must stay green.
7. `DOCUMENT_CAPS.md`: the protocol's row goes from 1394 to 800, by
   Tony's ruling 5 of Nov 10 ("Confirmed"). The sentence there that a
   shortened document's cap drops "to the new size" is true of the
   skills; for this row the number is his.
8. RUN AND READ: `skills_index.py`, `skills_index.py --check`,
   `doc_index.py --caps`, then `orrery_maintenance_run.py`. Report what
   each printed. Stop for Tony's go-ahead; he commits and pushes.

## Part 2: three skills and the doors

Each skill is at its cap. Before adding a line, move its oldest
version entry, word for word, to `documentation/SKILL_HISTORIES.md`
(the three-entry rule). One version each; each ledger note says why.
No protocol entry is written for a skill change any more.

1. `ledger-and-session-records` 1.23 to 1.24:
   - THE RUN-RECORD ZONE. Line 244, "Once read, the close empties the
     live zone; the copy is the record.", goes: both doors say nothing
     below the marker is touched, and Tony writes only in his copy
     (his ruling of Oct 28). On `documentation/WHERE_WE_ARE.md` the
     marker's second line ends "and clears this"; it ends "your
     timestamped copy." instead. `doc_index.py` matches the first
     marker line only (line 171); confirm nothing matches the second.
   - THE BINDING RULE. A skill bump no longer needs a protocol
     version-history entry. Its four steps become: the version line;
     `skills_index.py`; the ledger note; one commit. The paragraphs
     on "Step 3 is the one that stops firing" and on the manifest
     going stale move to SKILL_HISTORIES.md. The gate it names is now
     "The Installed Skill Equals the Repository's Copy".
   - ANCHOR REQUIREMENT. Add what Nov 23 found: Gemini 4 Neon in the
     Gemini app cannot fetch GitHub; the orrery, 2,549 files and 295
     MB, is past Google's import limit of 5,000 files and 100 MB, and
     a ZIP is limited to 10 files, so it is given a folder of copies
     with a list of what the folder holds. And: a request's commit
     lines go BELOW its "paste below this line" divider.
   - The Document Stack's line on the protocol, "read every session
     because it is resident", stands.
2. `orrery-coding-conventions` 1.13 to 1.14: its list of position
   consumers (lines 678-687) becomes six. The sixth: website rooms,
   `tools/gallery_cache_builder.py` -> `gallery/assembler/` ->
   `interactive.html`, GALLERY repo. THREE OF THE SIX are in the other
   repository. One sentence: the sixth asks JPL itself each night and
   draws from its own served cache, so a fix to the orrery does not
   reach it, nor the reverse. Read the three paths present in the
   gallery folder before writing them.
3. `agentic-pre-test` 1.3 to 1.4: line 29's example,
   `timeout 30 xvfb-run -a python3 _pretest_throwaway.py 2>&1 | head -50`,
   returns success after the program failed, because the pipe reports
   `head`'s result. Keep the whole output in a file, read the
   program's own exit status, then show the lines wanted. Say what a
   healthy window's exit looks like under `timeout` (124), and what a
   crash looks like. Show the old form passing a failing program and
   the new form catching it. Its two mentions of the old Modes are
   reworded: agentic work is the default.
4. THE DOORS. In `CLAUDE.md` here, in the website's `CLAUDE.md`, and in
   `documentation/python_work_door/python_work_CLAUDE.md` if it says
   the same: "Compare that version with the manifest's row" and the
   Stale Skill sentence go. A Code session reads the repository's
   copy, names each skill it read and its version line, and has
   nothing to compare. The orrery door's cap is 111; do not pass it.
   The website's door is the one edit this job makes in the other
   repository. No row of the website's run reads CLAUDE.md (L-522), so
   no gallery run is owed for it.
5. RUN AND READ, as in Part 1, with `skills_index.py --check` first.
   Stop for Tony's go-ahead.

Not in this job, each carried on L-522 by name in Part 3:
- Other skills that still name a retired part of the protocol, for
  each one's next version: provenance-discipline ("Skill Manifest",
  `/mnt/project`), safe-file-editing (the manifest), interactive-exhibit
  ("Stale Skill"), gallery-assembler ("Part 4").
- safe-file-editing's pointer at a SystemButtonFace workaround the
  pre-test skill records as removed.
- The website README's "five" position consumers, for step 6.

## Part 3: the records

By ledger-and-session-records. On L-522 (document caps), add the
design part below as written, then your own build record after it.

THE DESIGN PART, for the ledger, Tony's words exact:

- **Step 3, 2026-11-23, the coordinating session (Claude Fable 5.2),
  on orrery 7087b3ad and gallery a811d350.** Records:
  `REVIEW_COMPARE_fundamental_documents_20261123.md` (the three
  reviews side by side),
  `DESIGN_protocol_reduction_what_moves_20261123.md` (the list, and
  his rulings on it),
  `DESIGN_protocol_reduction_items_for_tony_20261123.md` (25 numbered
  passages and his answers), `REVIEW_RETURN_cold_read_20261123.md`.
- The three reviews do not contradict each other or the rulings of Nov
  10. Six of the ten findings of Nov 10 were found again by GPT or
  Gemini; the outside two added nine things, two of them faults in
  checks the protocol calls critical.
- Tony, 14:44, asked whether step 3 is still the job and offered two
  sittings: "Confirmed as recommended".
- Tony, 15:15, on the list of what moves: "please retain the double
  helix principle in the protocol. This is a foundational idea for
  working together"; "on the register rule: can we relax this given
  that 5.2 and 5.5 models already do this much better."; "Otherwise,
  no objections." The Weasley Principle moves; the ten process lessons
  stay; the conduct tables shrink (his choices A, B, C, Claude's
  recommendations).
- The conduct rules were tested against the ledger (ruling 4): found
  broken since August 24, going past what was asked (L-250), the wrong
  size of tool (L-506), plain speech (L-539, L-261); not found,
  guessing where a question was due.
- Tony, 15:52, five comments on the first draft: the seven Modes are
  retired but for Mode 5 and Mode 7 ("Mode 1 is now used only when I
  explicitly request it"); "My role as coordinator and carrier is
  largely replaced by Cowork and Code."; "I am not sure that AI roles
  are still needed or pertinent. Frontier models are broadly
  capable."; the triggers table, "an outdated effort to curtail
  verbosity and complexity"; two paragraphs of the Register Rule,
  "probably not needed".
- Tony, 15:59: "It seems largely procedural. Should some of this move
  to skills?" Two blocks became pointers: Check All Parallel Pipelines
  (to orrery-coding-conventions) and Mode 7 (to
  ledger-and-session-records). Claude's recommendation; approved with
  item 21.
- Tony, 16:44, by number: 3, 4, 6, 9, 12 "drop"; "mode 2 is largely
  the default mode"; on the uploads rule, "this may be obsolete given
  Claude reads directly from repo" (cut to one line, not dropped: the
  session began from an upload); "otherwise approved". 16:51: "14 was
  a typo I meant the opposite that Claude dropping files into my repo
  is routine as is Code." and "Yes on the cold read."
- The Register Rule's earlier relaxation, which Tony gave in a chat on
  2026-09-29, had never reached the ledger or the protocol.
- The cold read (a Claude Fable chat in incognito, outside the
  Project, Tony's carry): all eight cases matched answers written down
  beforehand, and it found eight faults both had read past, all fixed
  in the fourth draft.
- Tony, 18:16, on the fourth draft, 795 lines: "ratified. thanks."
- The session's two estimates were wrong and were said so: "750 to
  800", then 831 by parts; the first draft measured 896. His comments
  and the two pointers brought it under the cap, not tightening.
- At its start the session compared all twelve installed skills with
  the repository: equal, one by a line wrap in its header. That met
  v3.145's obligation for 1.20, 1.21, 1.5, 1.45 and 1.15.
- Placing files from the linked session: every write was reported
  written and none could be read back, the tool refusing to stage a
  file it called hardlinked. The Code session's sha256 is the
  read-back.
- CARRIED, with no home in the six steps, one line for each kind:
  the stamping rule (safe-file-editing, "Stamp What You Change") and
  `constants_new.py`'s 37 stamps; `PROVENANCE_AUDIT.md`'s "No file's
  Tier-1 count rose" (L-269 has it) and its 271 "FIX NOW" labels; ten
  modules with no Role tag (earth_pole_live_check.py,
  orrery_colors.py, path_drawing.py, test_drawings_export.py,
  test_earth_pole_of_date.py, test_extractor_pins.py,
  test_hills_cloud_sampler.py, test_path_drawing.py,
  test_worksheet_keys.py, worksheet_key_aliases.py); a search rule
  for Code sessions past the spent patches; the website's
  `INTERACTIVE_AS_BUILT.md`, uncapped, 2,150 lines on Nov 16 and 2,483
  on Nov 23; the 55 [CRITICAL] marks in the skills, for L-328.

ALSO IN THE CLOSE:
- L-522's Gap becomes steps 4 to 6. Its Tony-action on step 3's gate
  wordings is done.
- Items this step closes, each with its reason, after reading its
  body for loose ends: L-199 (protocol length); L-230 (a check for a
  skill bump with no protocol entry), no longer needed since a skill
  bump makes no entry; L-499 (kinds of session), whose Gap was the
  protocol's text. If a body holds work not done, leave it open and
  say what.
- L-548 (a missing id_type): its note says to map "all five"
  consumers; six.
- `documentation/WHERE_WE_ARE.md`, by section: what changed, in plain
  words; "Do next" moves on to L-538 (the orbiters' printed error);
  the handoff named in "Needs you now" and "Where the details are" is
  `HANDOFF_document_upkeep_20261123.md`, which the coordinating
  session's close never recorded there.
- `ledger_index.py`, and the maintenance run once more, read to its
  last line.

## Tony-actions, to roll up in your last report

- (do) After each part: look at the change list, commit, push. Part 2
  also touches the website's folder: one file, `CLAUDE.md`.
- (do) Paste the new `PROJECT_INSTRUCTIONS.md` into the Project's
  instructions on claude.ai. This is the last paste a skill change
  will ever ask for.
- (do) Reinstall three skills from the repository (Plugins, in the
  claude.ai sidebar): ledger-and-session-records,
  orrery-coding-conventions, agentic-pre-test.
- (decide) The version number, v4.0 unless he says otherwise.
- The next session that has a shell compares the installed skills
  with the repository's copies before it works. That comparison, not
  his word, clears the three.

## Out of scope

- No rule's wording changes from the ratified draft. A fault found in
  it is reported to Tony, not fixed.
- Steps 4 to 6 of L-522. The READMEs and the master plan.
- Any skill but the three named.

Written November 2026 with Anthropic's Claude Fable 5.2.
