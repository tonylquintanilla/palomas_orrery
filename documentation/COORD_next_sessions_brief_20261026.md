<!-- Doc-Kind: hand | Brief from the coordinating session of Oct 26, 2026 (Claude Fable 5.1) to the next build session and the next talk: what is verified, the one red check, the queue in order, and the protocol item to open. Zero code. -->
# Brief for the next sessions: October 26, 2026, night

Tony Quintanilla, PE | Claude Fable 5.1 (coordinating session) | October 26, 2026, 21:00

Built on orrery 71b3992333e8aa7f5d94f44cf90cbd13943e27d4 at
https://github.com/tonylquintanilla/palomas_orrery (branch main) and
gallery b7e2edd4bea43d97c519ff514d5c8dc0dbf50f7e at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch main).
Both read live with git ls-remote at 20:56 on Oct 26, after Tony's
push of the night's records patch (patch_L494_4).

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: COORDINATION BRIEF (zero code). Supersedes nothing. Companion to
`HANDOFF_coordination_20261023_26.md`, whose section 5 queue this
replaces. The skills a build session fires from this brief:
ledger-and-session-records (records patch), safe-file-editing and
agentic-pre-test (the patch), interactive-exhibit and
provenance-discipline (the skill text).

## 1. Verified at HEAD, Oct 26, 20:56

- Orrery HEAD is 71b3992. The ledger carries L-495 (the night's
  changes), L-496 (groups in the search) and L-497 (left-aligned text).
  orrery-coding-conventions reads 1.12 in the repo, the manifest and
  Tony's account install (he reinstalled it; the repo copy and the
  manifest row agree with the version line in SKILL.md).
- Gallery HEAD is b7e2edd. Everything from the night is live and was
  checked on Tony's phone: slice 2 of L-443 (spacecraft and comets),
  the search box (L-493), the i button's note (L-494), the direction
  arrows, the AU note, the whole triad, the wrapped orbit lines, and a
  comet's farthest planet (L-495).
- The two Oct 26 coordination notes reached the repo at 140db0ae:
  `COORD_jpl_words_ruling_20261026.md` and
  `COORD_stale_scale_sentences_ruling_20261026.md`. Their items exist:
  L-492 for the stale sentences; the JPL-words rule rides L-443, carried
  for provenance-discipline's next version.
- The comet session did what the Oct 23-26 handoff asked of it: L-485
  (a nightly run) carries the five rulings, L-489 (compositions) and
  L-490 (the legacy list) are open.
- Tier-1 on the gate path: 0 by name, per the last orrery maintenance
  run in Tony's run record (the records patch pushed after it touched
  no code).

## 2. The one red check, and the fix

Tony's last orrery maintenance run of the night (in
`WHERE_WE_ARE_10-26-26_1451_run_record.md`, after patch_L494_4) read
"1 of 34 checkers FAILED -- Dashboard parity". The build session had
written "it should be all green" before Tony ran it and closed without
seeing the result. Every other checker passed.

The finding, in the checker's own words:

    NO BUTTON  gallery step "Direction arrows"
    (documentation/smoke_direction_arrows.js) has no button named so
    in "Gallery -- checks and data"

What happened: gallery patch b7e2edd added the Direction arrows check
as a gating step of the website's maintenance run
(`gallery_maintenance_run.py`, lines 505-506 at b7e2edd). The orrery's
dashboard, `palomas_orrery_dashboard.py`, has one button per gallery
step, and the Dashboard parity checker (L-440) compares the two by
name. No button was added, so the checker did its job.

The fix is small and belongs to the next orrery build session, first,
before the skill text:
- One button tuple in the "Gallery -- checks and data" group of
  `palomas_orrery_dashboard.py`, modelled on "Far Lines" (lines
  969-984 at 71b3992): name "Direction Arrows", runs through
  `documentation/run_offline_check.py` from the gallery repo root,
  step name `["Direction arrows"]`, with a description in the same
  voice as Far Lines (what the arrows are, five arrowhead lengths
  ahead, not drawn outside the view or when longer than the orbit at
  that scale; breaks its own file first to show it can fail; GATES
  the gallery runner).
- One short line in the short-lines table (model: the Far Lines entry
  near line 2090), twelve words or fewer, e.g. "Checks each orbit's
  direction arrow and that it stays inside the view."
- The test is the orrery maintenance run reading 34 of 34 green.

Record it under L-495 (the night's changes) in the same records patch:
the Direction arrows check got its dashboard button on <date>, and the
run that found it missing was the one after patch_L494_4.

## 2a. The first Claude Code session, and its form (Tony's rulings, Oct 26, 21:47)

Tony is trying the next build session in Claude Code (the desktop
app's Code tab, Local, this folder) instead of a Cowork session. His
rulings for it, in his words where he gave them:

- The deliverable is the edited files, not a patch file: "Code edits,
  tests and reports -- yes."
- "You review the change list in GitHub Desktop and commit -- yes."
  Commit and push stay Tony's. `.claude\settings.json` forbids Code
  from running push, commit, and the commands that discard work;
  `CLAUDE.md` says the same in words.
- "The diff works for Claude but not for me. A summary of the changes
  should be included in the Where We Are report, which should be
  maintained as our tactical document." So the page's "Changed since
  you last read this" box carries the plain-word summary of what
  changed and why, and the session's final report lists every file
  changed with its edit count, as a patch would print, for his run
  record.

Two files were added to the orrery root for this, placed on Oct 26
and to be included in Tony's next commit: `CLAUDE.md` (the door into
the protocol: it imports PROJECT_INSTRUCTIONS.md, names where the
skills live, and states the Code-session form above) and
`.claude\settings.json` (the git rules). CLAUDE.md points and does not
repeat; a sentence in it that disagrees with the protocol or a skill is
corrected, not followed.

Code does not read this claude.ai Project's instructions or the
account's installed skills, so the session reads the skills as files
at `skills/<name>/SKILL.md` and names which it read, the same read-back
rule used for GPT and Gemini (L-290). No fourth copy of the skills is
made.

## 3. The queue, in order

1. **Orrery build session, in Claude Code (section 2a), one commit:**
   a. the dashboard button above (section 2);
   b. interactive-exhibit 1.26 -> 1.27, everything carried on L-443
      under "Carried for interactive-exhibit 1.27" (the pointer
      sentence, a comet on a closed orbit and its farthest planet, the
      Find a body box, the AU note and the triad, the direction arrows,
      the headless-recipe candidate);
   c. provenance-discipline: the JPL-words rule into What a Visitor
      Reads, from `COORD_jpl_words_ruling_20261026.md` (keep the
      authority's word and explain it; never replace it).
   One Session, One Bump holds for each skill. Both bumps ride one
   protocol entry (v3.116) and one commit. The session reads the repo's
   copies of interactive-exhibit 1.26, horizons-orbital-mechanics 1.12,
   gallery-cache-builder 1.13 and orrery-coding-conventions 1.12 before
   work that fires them, and says so (the obligations carried from
   v3.114 and v3.115; in Code the repo copy is the loaded copy, so the
   read discharges them).
   The session ends with the orrery maintenance run read by itself, all
   green, and the records of section 2a.
2. **L-497 (left-aligned text):** a small gallery build. Plotly's own
   tap box centres its lines; the fix is in the text box's layout, not
   the words. Already ruled; no talk needed.
3. **L-492 (the stale scale sentences):** a short orrery session of its
   own, from `COORD_stale_scale_sentences_ruling_20261026.md`: the
   "SET MANUAL SCALE ..." and "n MB PER FRAME" sentences come out as a
   class (about 110 and 85 lines at 5398439, named there by file);
   keep the "plot with" halves; read save_utils.py line 145 first;
   the pre-test runs.
4. **A design talk (Fable or a talk-only session), four items, P1
   first:**
   - P1 on L-485: when a 30-day check disagrees with JPL at night, does
     that body keep its last confirmed values? This one gates the
     nightly-run build.
   - L-496: which words find a group in the search ("comet", "planet",
     "asteroid", Tony's examples), and what a group match shows.
   - Compositions (L-489): the noun, "view" or "scene"; and the first
     one to build (Voyager 1 with its planets in the Solar System room
     is the recommendation).
   - L-465: the orrery's own Sun axis hover, words to Tony first, and a
     source for "differential 24.5-35 d".
4a. **The master plan reviewed and restamped at slice 2's close**
   (Tony, Oct 26, 21:47: "we should add to this brief a review and
   update of the strategic master plan as we conclude slice 2").
   `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md` stands at v36,
   Oct 14, written before slice 1 and slice 2, before compositions
   (L-489), the nightly run on GitHub's computers (L-485) and the
   legacy list (L-490). A coordinating or talk-only session reads the
   plan at HEAD against the road on Where We Are and the ledger, and
   restamps it as v37 with its executive summary rewritten from the
   current state, never carried forward (ledger-and-session-records,
   The Document Stack). Its ledger lines go in the next records patch
   or Code session. Best taken in the same sitting as the design talk
   above, since compositions and the nightly run are the direction
   decisions the plan has to carry.
5. **L-485, the nightly run on GitHub's computers:** the build session,
   from `DESIGN_L485_nightly_run_rulings_20261025.md`, beginning with
   the verifications in its section 4 (the sixty-day pause above all),
   after P1 is decided.
6. **The protocol item (section 4 below):** a short talk-then-records
   session, after the skill work. Text in PROJECT_INSTRUCTIONS.md only;
   nothing else depends on it.
7. Unmoved: compositions discovery after the talk; L-490 (the legacy
   list), the people question first; the two papers in
   `READING_L456_tony_20261021.md`; the editor and the Solar System
   room's rows; choosing a date and animation.

## 4. The protocol item to open at the next records patch

Tony, Oct 26, 20:45: "We should update the relay method (mode 7?) in
the protocol regarding our new coordination approach and working in
Cowork." Then, 20:49, correcting the first draft of what the item
would say: talk-only sessions DO produce files, and the dividing line
is patches.

What the item records, for Tony to confirm or correct before the text
is written:

Mode 7 in the protocol describes a relay in which Tony carries
documents between models by hand. What the project actually runs now,
since Tony's Cowork request of Oct 10 (L-351, the local folders in
every header), is three
kinds of session told apart by what each is allowed to write:

- A COORDINATING session (Claude Fable 5.1, linked to Tony's
  computer): verifies before it recommends (git ls-remote on both
  repos, the run record read whole, the ledger and Where We Are at
  HEAD, a dry run of a patch in question); runs design talks, often
  from Tony's phone; and writes rulings, briefs and coordination notes
  straight into the orrery's documentation\ folder under their proper
  names, so nothing is a download. It writes no patch.
- A BUILD session (Claude Opus 5.5): works from the rulings and briefs
  in that folder; writes patches and a closing records patch; ends
  with a run order Tony answers in his run record.
- A TALK-ONLY session (Opus or Sonnet, not linked): writes design
  records and handoffs in Tony's words, which Tony saves to
  documentation\ by hand; runs no patch and touches no code. Tony's
  model of a talk-only close, pasted Oct 26, 20:49, quoted here as the
  example the protocol should carry:

    "All four talks are settled. Writing the design record and the
    handoff now. One check first: the bow shock comes from a different
    paper, so its faint surfaces should sit at the ends of its own
    fitted range, not Shue's.

    The two files are attached: `DESIGN_talks2_rulings_20261021.md`
    (the rulings in your words, what was read, the build notes) and
    `HANDOFF_talks2_20261021.md` (the ledger lines and Where We Are
    changes for whichever build session closes next). Save both in
    the orrery's `documentation/` folder; there is no patch to run.

    One thing differs slightly from the draft you approved: [the one
    difference, in three bullets]

    Where this leaves us: [three bullets]"

A fourth kind was added the same night: a CODE session (Claude Code in
the desktop app, opened on one repository folder). It is a build
session without a patch: it edits the files directly, runs the tests
itself and reads them, and ends with the records and a file-by-file
report for the run record; Tony reviews the change list in GitHub
Desktop and commits. Its door into the protocol is `CLAUDE.md` in the
repository root (section 2a). The patch rules in safe-file-editing and
the "a delivered patch is final" rule (L-471) keep their force for
Cowork build sessions and need a sentence each saying so.

Two lines in the protocol change with it. "Tony is the integrator"
stays true, but the carrying between sessions now happens through
files on his disk, read by the next session, rather than through
pasting; and "Documents as handoffs: Copy/paste AI responses" is out
of date for sessions inside this Project (it stays right for GPT and
Gemini, which the L-290 anchor rules already cover). The AI Roles
table gains the three session kinds by model.

The item opens with the next handle at the next records patch; no
handle is proposed here. The text goes into PROJECT_INSTRUCTIONS.md,
Part 1, Mode 7, at the talk in queue item 6, with Tony's ratification.

## 5. Tony-action rollup

- **(do)** Commit `CLAUDE.md`, `.claude\settings.json` and this brief
  with your next push, before the first Code session, so the session's
  base matches the remote.
- **(do)** Open the Claude desktop app, click Code, choose Local, Open
  folder, pick `palomas_orrery_for_github`. Its first message: "Read
  CLAUDE.md and start the session." It should answer with the base
  SHA, the skills it read with their versions, and one sentence on the
  job, then wait for your go-ahead.
- **(do)** After that session: review the change list in GitHub
  Desktop, commit and push; then reinstall interactive-exhibit 1.27 and
  provenance-discipline's new version (Settings > Skills) for the
  Cowork and chat sessions, which still load the account copies.
- **(decide)** Section 4's description of the three session kinds:
  confirm or correct before the protocol text is written.
- **(decide)** P1 on L-485, at the design talk (queue item 4).

Written October 26, 2026 with Anthropic's Claude Fable 5.1.
