<!-- Doc-Kind: hand | A review of the project's governing documents (protocol, skills, ledger, plan, READMEs, audit, atlas, constants store, the Code doors): where they have gaps, where they cost more than they return. Communication; findings and options, no rulings. -->
# Review: the fundamental documents, November 10, 2026

Built on orrery b3ce81f89f79a7c5aabf730ed5b6468d539cf570 at
https://github.com/tonylquintanilla/palomas_orrery
and gallery cea21af180b98a6694cb6bfb1083eca38e9b5c5d at
https://github.com/tonylquintanilla/tonyquintanilla.github.io
(both branch main, read 2026-11-10, 08:33 Chicago, as fresh clones).

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: DOCUMENTATION REVIEW (zero code, zero edits). A talk session
linked to Tony's computer. Nothing in either repository was changed.
This file is the only thing written. It holds findings and options.
It holds no rulings; those are Tony's.

## What was read, and how

The document set Tony named is about 4.4 MB. No reader can hold that,
so this review says exactly what was read and what was measured.

- Read in full: PROJECT_INSTRUCTIONS.md (v3.135), all four CLAUDE.md
  files in the two repositories, documentation/WHERE_WE_ARE.md,
  METHOD_MODEL_EFFORT.md.
- Read in part: the orrery README (outline, Part 1, half of Part 2);
  the website README (opening and its claims about the interactive
  gallery); the master plan (the whole executive summary and status
  block, the outline of the rest); the ledger (its preamble, its
  generated index, seven items in full); PROVENANCE_AUDIT.md (the top
  95 lines and the outline); MODULE_ATLAS.md (the top); constants_new.py
  (the docstring and the low-Earth-orbit rows); the skills (the header
  of all twelve, the outline of nine, three sections of
  ledger-and-session-records, two samples of interactive-exhibit).
- Measured by script, not read: every size, count and date below.
- Not read: the body of most ledger items, the body of most skills,
  the website's MODULE_ATLAS.md, the code.

Sizes: about 130 KB of file text read directly, the protocol aside.
The session's environment prints no token count.

## The claim in one paragraph

The documents are accurate where they were checked, and the checks
that guard the website's numbers hold. The problem is growth. Almost
every document here has a rule for how a line gets IN and no rule for
how a line LEAVES. So each one carries its own history inside it, each
grows every session, and every reader, Tony or a model, pays for the
history to reach the present state. Where We Are is the exception. It
has a length cap and a rule for when a line leaves, and it is the best
working document in the set. Most findings below are that one cause
seen in a different file.

## Findings

### 1. The working documents carry their own history, so they only grow

- The ledger is 2.5 MB and 38,649 lines. Its first 777 lines are 186
  "Module updated" stamps, before the file says what it is. About half
  its bytes are closed items.
- The protocol is 1,480 lines. It was 1,021 on August 17, when L-199
  (protocol length) measured it. Its version history is 153 lines and
  its skill table is 161 lines; together they are a quarter of it.
- The interactive-exhibit skill is 2,253 lines and 155 KB. Its first
  66 lines are version notes. Its body says "until v1.x" or the like
  84 times, quotes Tony with a date 26 times, and cites a ledger handle
  190 times.
- constants_new.py opens with a 245-line docstring holding 35 update
  stamps. 4,706 of its 6,303 lines are comments, and many rows carry
  their own correction history.
- The master plan carries a status block of about 110 lines that the
  plan itself says is no longer updated.

Git already keeps every one of these histories, and the ledger keeps
the reasons. The cure exists in three places already (the three-entry
rule, SKILL_HISTORIES.md, MASTER_PLAN_HISTORY.md). It is applied by
hand, one document at a time, by whichever session remembers.

Option: one rule for every working document. It states the present.
Its history lives in git and in one companion file, and a tool in the
maintenance run moves old lines there, not a session. For the ledger
that means closed items in a companion file with the same handles, and
the stamp block dropped, since each item already carries its own date.

### 2. A skill change costs a ceremony, and the ceremony has taken over the protocol's version number

Of the last 46 protocol versions (v3.90 to v3.135), 45 open with the
words "No rule changed in this document." There were 45 protocol
versions in October and 16 in the first nine days of November. Each
one is the same chain: the skill's version line, the skill table
rebuilt, a protocol history entry written, the oldest entry moved
down, Tony reinstalling the skill in Settings, and Tony pasting the
85 KB protocol into the Project's instructions.

The chain exists because the skill table lives inside the protocol,
and the stale-skill check compares version numbers.

This session tried a different check. The account's installed skills
arrive in a talk session as files. One command compared all twelve
with the repository at HEAD, byte for byte. All twelve match, their
reference folders included; one differs only by a line wrap in its
header. That check is stronger than comparing version numbers: it
would have caught the case of November 9, where two different texts
both said 1.37. It costs nothing to read. It needs no table in the
protocol.

Two options, the first smaller:
- A. Cut the table to name and version, twelve lines. The "fires
  when" column repeats each skill's own header, which is what makes a
  skill load. Stop writing a protocol version for a skill change; the
  skill's header and its ledger item already record it.
- B. Make the gate "the installed skill equals the repository's copy",
  and take the table out of the protocol. The protocol's version then
  moves only when a rule moves, and Tony pastes it only then.

The cost of B: a session with no shell (a phone talk) cannot run the
comparison. Such a session does not build.

A Code session reads its skills from the repository. For it the
present gate compares the repository with itself.

### 3. The interactive-exhibit skill has become the website's as-built description

A skill is meant to hold how the work is done (the protocol's Method
Belongs to the Skill). Most of this one describes what the page does:
which button sits where, which function does it, what it did before.
One section, the Solar System room's drawer, is 724 lines. The skill
went from version 1.2 on September 11 to 1.39 on November 9.

What the page does is already stated twice: by the code, and by the
checks that assert it (the gallery run's rows, the headless walk). A
third statement in the skill has to be read back from the code every
time it is written, and it is still a copy.

A website build session is told to read this skill in full. With the
protocol, the records skill, safe-file-editing, the brief and Where We
Are, that is roughly 350 KB, on the order of 90,000 tokens, before any
code is read.

Option: split it. A short skill of rules that changes rarely. A
separate as-built reference in documentation/, read by section, not
versioned as a skill, with no reinstall. A ruling such as "no See
more" belongs in the ledger and in a check that fails if the button
comes back. Most of the daily skill changes would then stop being
skill changes, which also removes most of finding 2.

### 4. The project's own upkeep items do not get done, and the Braid is the reason

Four items diagnosed this accurately months ago: L-199 (protocol
length, August 17), L-215 (ledger cleanup, August 19), L-230 (a check
for skill changes, August 23) and L-328 (a subtraction pass on the
skills, September 14). None was built. Since they were written:

- the protocol grew from 1,021 lines to 1,480;
- open ledger items grew from 107 to 242;
- [CRITICAL] tags in provenance-discipline grew from 20 to 24. The
  skills now carry 55 of them against 13 in the protocol, though the
  protocol says the critical gates stay resident and the tier must
  stay short.

The Braid says: if the current artifact does not reach it, it waits.
That is right for provenance. But no artifact ever reaches the
documents that manage the work, so by that rule their upkeep waits
forever. In plant terms this is preventive maintenance filed as
corrective work orders: it competes with production and never wins.

Option: give upkeep an interval, not a work order. One upkeep session
after each step of the road, or each fixed number of build sessions,
written on the road so it is seen.

### 5. The ledger no longer works as a list of work orders

- 242 of 258 live items carry the "!" flag, so the flag says nothing.
- 167 of them sit in one section, "A. Active Separate Tracks". Every
  row in the other open sections was last touched before September.
  The sections of June no longer match how the work is organised.
- 91 of the 167 have no RICE score. Scoring stopped for newer items.
- 118 open items have not been touched in two months or more.

One case shows the cost. L-012 is flagged critical. It was written on
June 21. The desktop orrery prints "fetched fresh data" over orbital
elements it read from its cache, and the line is hard-coded to
Mercury. That line is still in palomas_orrery.py today, at line 4872.
It is a false statement of where data came from, the class the
protocol treats as worst, and it has been open 142 days. It is on the
desktop orrery, which is not the current artifact, so waiting may be
right. The point is that nothing on the board tells "waiting by
decision" from "forgotten".

Where We Are already does this for about twenty items, in its Deferred
section. Option: one triage pass over the open items with three
outcomes only: on the road, deferred by decision with the reason, or
closed as not to be done.

### 6. The protocol's picture of where the truth lives is one generation old

The protocol's trust order and three of its critical gates guard an
upload workflow and a project-file snapshot (/mnt/project) that was
removed at v3.30. The Project holds no files now.

Meanwhile the work moved. Since October 26 builds run in Claude Code
on the working copy on Tony's computer, which can be ahead of GitHub;
the session of November 9 built on a commit not yet pushed. The
protocol has no resident line for that store. Its Session Start does
not mention Where We Are, which every Code session reads first. The
three kinds of session (L-499, ruled October 27) are in the ledger and
the master plan, not in the protocol. Its Modes table still describes
complete files and manifests.

So there are resident gates for a store that is gone, and none for
the store in use.

### 7. A stale second CLAUDE.md is loaded into Code sessions

documentation/CLAUDE.md in the orrery is a Claude Code handoff from
February 2026. It names protocol v3.9. It says "You operate in the
sandbox. You never touch the GitHub source directory", "Ask Tony what
directory am I working in", and to close by updating
web_gallery_handoff.md.

Claude Code loads a CLAUDE.md it finds in a subfolder when the session
reads a file in that folder. Every Code session reads
documentation/WHERE_WE_ARE.md as its first step. It happened here:
when this session read Where We Are, the February file arrived as
project instructions. It contradicts the root CLAUDE.md on where to
work and what records to write.

documentation/python_work_door/CLAUDE.md ("no work is done here") is
exposed the same way.

Option: rename both so neither is called CLAUDE.md where it sits. The
door's copy in the parent folder keeps its name.

### 8. The audit still prints the check the protocol names as unable to fail

The protocol's gate A Check That Cannot Fail gives, as its example of
a count that hides a change, PROVENANCE_AUDIT.md's line "No file's
Tier-1 count rose". The audit of November 9 still prints "Change since
the previous run: total +0, Tier-1 +0. No file's Tier-1 count rose."
L-269 (a report names its items) is open.

Three smaller things in the same file:
- 276 findings are labelled "FIX NOW". By the Braid they wait on
  purpose, and the count has not moved since at least October 27. A
  label nobody acts on teaches readers to ignore the label.
- A note dated April says all Tier-2 findings (707 now) are accepted.
  No run re-tests that sentence.
- "unclassified 2": path_drawing.py and test_path_drawing.py have no
  Domain tag. The atlas lists nine modules with no Role tag:
  earth_pole_live_check.py, path_drawing.py, test_drawings_export.py,
  test_earth_pole_of_date.py, test_extractor_pins.py,
  test_hills_cloud_sampler.py, test_path_drawing.py,
  test_worksheet_keys.py, worksheet_key_aliases.py.

### 9. The front doors are ten weeks old, and the plan missed a change of direction

- Both READMEs are dated August 31, with a licence edit on October 4.
  They describe the interactive gallery as the Sun exhibit. They do
  not mention the Solar System room as the front door (October 22),
  the exports from the orrery to the website, the daily run, the
  nightly run on GitHub, Claude Code sessions, or Where We Are. The
  orrery README says its second half is written for an AI collaborator
  starting cold.
- The master plan is v37 of October 27. Its direction is "the inner
  planets' rooms". It does not mention L-515 (one nested tree), whose
  rulings of November 7 to 9 replace rooms with one picture and one
  drawer. By the plan's own rule it is read and restamped when a
  decision changes direction.
- The website's CLAUDE.md did not receive the Token Economy edits the
  orrery's got on November 2. It still says to read each skill in
  full, and its final report has no token count.

### 10. Smaller observations

- documentation/ holds 1,772 files and 51 MB: 538 spent patches
  (16 MB), 267 handoffs, 56 run-record copies of Where We Are. Tony
  has ruled the folder stays flat, for his own scanning. The cost
  falls on a Code session's searches, which also match text in 538
  spent patches. A search rule for Code sessions could skip them
  without moving a file.
- The ledger's preamble says it "is not a session log" and "not a
  design document". Its largest item, L-515, is 1,068 lines and 72 KB.
  The largest items are both.

## What holds, in brief

- The gate on what leaves the orrery reads 0, and prints how many
  rows it examined and which it did not.
- The ledger's own check passes: 514 blocks, no inconsistency.
- All twelve installed skills equal the repository at b3ce81f8.
  interactive-exhibit reads 1.39 in the account's copy. That is the
  confirmation v3.135 asked the next session for. It was read from
  the session's skills folder and compared with the repository; it was
  not loaded through the skill loader.
- Where We Are, the seven kinds of document, and the SHA round trip
  are sound and are being followed.

## Small fixes: found, none made

Tony gave leave to make small fixes. None was made, for two reasons.
A build is running that writes records into both working copies, and
anything added now would be mixed into its change list. And this
session has no shell on Tony's computer, so it could not run the
maintenance run after an edit.

Candidates, each small, for after the build closes:
1. Rename the two CLAUDE.md files under documentation/ (finding 7).
2. Bring the website's CLAUDE.md level with the orrery's on Token
   Economy (finding 9).
3. Add Role and Domain tags to the nine modules listed in finding 8.
4. Move the master plan's frozen status block to
   MASTER_PLAN_HISTORY.md (finding 1).

## An order, offered as an option

1. The CLAUDE.md renames. Minutes.
2. Split interactive-exhibit into rules and an as-built reference.
   One session. The largest single saving.
3. Take the skill table out of the protocol's version cycle (2A or
   2B). With step 2 this ends nearly all of the daily ceremony.
4. The ledger: closed items and stamps to a companion file by tool;
   one triage of the open items.
5. The protocol: replace the gates for the retired store with the
   stores in use; add the kinds of session; move the version history
   out.
6. Restamp the master plan and both READMEs once step 2b of the one
   tree has landed.
7. Put an upkeep interval on the road, so the next review of this
   kind finds less.

Written November 10, 2026 with Anthropic's Claude Fable 5.2 (the model
this session is configured for), a talk session linked to Tony's
computer.
