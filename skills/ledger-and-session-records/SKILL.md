---
name: ledger-and-session-records
description: Ledger and session-record conventions for the Paloma's Orrery project. Use when creating, updating, or closing items in LEDGER_CONSOLIDATED.md, running or modifying ledger_index.py, RICE-scoring items, writing or reading session handoffs or build manifests, recording protocol or skill version changes, regenerating MODULE_ATLAS.md via module_atlas.py, or tracing dependencies with dep_trace.py. Also use when writing or updating documentation/WHERE_WE_ARE.md, Tony's plain-language page of where the project is and where it is going, which every session updates at its end. Trigger words include L-handle references (L-001, L-078...), "ledger", "handoff", "manifest", "RICE", "module atlas", "dependency trace", "where we are". Do not use for projects other than Paloma's Orrery.
fires_when: Ledger edits, ledger_index.py, RICE, handoffs, manifests, atlas, dep_trace, WHERE_WE_ARE.md at every session's end
---

# Ledger and Session Records

Read this file in 3 parts: lines 1-224, 225-500, 501-677.

Skill version: 1.18 | 2026-10-08, with Anthropic's Claude Opus 5.5, at
palomas_orrery @ b0b3df82. v1.18 (L-418) records two conventions the
provenance-discipline split brought in, under A skill keeps three
version entries: a file longer than one read opens with a read plan
that skills_index.py writes, and a skill's extra files live in its
references folder, each named in its SKILL.md. The Anchor Requirement
names provenance-cross-check for a review prompt carried to another
model.
Earlier: 1.17 | 2026-10-07, with Anthropic's Claude Fable 5.1, at
palomas_orrery @ 8653ef1b. v1.17 (L-422) carries four of Tony's rulings
from one session. Under Where We Are -- Tony's page: the page's new
shape (each fact once; the box is the page; Settled; Signals), a
run-record zone at its end that no patch edits and that the close
reads from his timestamped copy, patches editing the page by section,
every ledger handle on the page carrying a short label, and the check
to build (date, and a cap of 130 lines above the marker). Under Ledger
Block Format: an item inside an ordered list needs no RICE score
(L-412). Under Where a File Goes: which repository a record goes to,
and that documentation/ stays flat.
Earlier: 1.16 | 2026-10-05, with Anthropic's Claude Opus 5.5, at
palomas_orrery @ d9f47a87. v1.16 (L-419) adds one rule under Where We
Are -- Tony's page: a patch checks a document Tony annotates (this
page, the handoffs, the ledger) only at the lines it edits, and a
rewrite of the page carries his notes into the handoff first. The
rule had lived only in one patch's code and was broken the same day.
Older entries are in documentation/SKILL_HISTORIES.md, moved there
on 2026-10-05 (L-418), 2026-10-07 (L-422) and 2026-10-08 (L-418).

Note: READING the ledger at session start is resident Part-1 behavior,
not this skill's job. This skill carries the maintenance mechanics.

## Contents

Generated from this file's headings. skills_index.py --check fails
if this list and the headings disagree (L-418).

- The Document Stack (the round trip)
  - Where We Are -- Tony's page [QUALITY]
- Ledger Block Format
  - A Closing Item Re-homes Its Loose Ends [QUALITY]
  - Cluster the Tail by Topic, Not by Age [QUALITY]
- Anchor Requirement (all outbound documents)
- Where a File Goes [QUALITY]
- Handoff Structure (the load-bearing lines)
- Protocol and Skills Change Log (v3.30 addition)
- Codebase Tooling
- Field Notes

## The Document Stack (the round trip)

protocol -> ledger -> handoff -> manifest -> code -> repo -> ledger.
- Protocol: the constitution; evolves slowly; amendments ratified by Tony.
- Ledger: the single authoritative backlog AND institutional memory;
  survives session boundaries. As of v3.30 it is also the change log for
  the protocol version history and the skills layer.
- Handoff: a session record -- decisions, deliveries, open scope. A
  handoff is a CLAIM, not a verification; the render and the repo are the
  facts. Design-session handoffs (zero code) are first-class outputs: the
  reasoning trail for WHY the design is what it is.
- Manifest: the executable build contract, written against HEAD at build
  time (never on an un-pushed base); opens with the anchor (built on
  <SHA> at <URL>) per the requirement below. If handoff and manifest
  disagree, that is a flag to raise, not a thing to silently resolve.

**The master plan is not a rung in that ordering** (Tony's ruling,
2026-08-20, L-221). It is the ROADMAP -- where we are and where we
are going, not what is directly in front. It is ONE document at two
zooms (v1.12, Tony's ruling of 2026-09-28, L-333 and L-362): an
EXECUTIVE SUMMARY at the top, and the body, which keeps the critical
path as Section 5a. The summary is REWRITTEN from the current state at
every restamp, never carried forward, so it cannot fall behind the
body the way the two separate companion files did: they restamped with
v19 and v20 and then stood still for a month while the plan reached
v33. Those files, `MASTER_PLAN_INTERACTIVE_GALLERY_SUMMARY.md` and
`MASTER_PLAN_CRITICAL_PATH_SUMMARY.md`, carry a retirement line and are
dated records. The plan restamps once per DESIGN BUILD; stepwise updating is the ledger's job.
That is Tony's ruling of 2026-09-06 (L-296), replacing "at key
junctures": a juncture is not countable, so the rule could not be
applied without a judgment call every time, and the call kept landing
on Tony. A design build is countable. Versions are REPLACED, not
archived -- only the PROTOCOL keeps a versioned copy per version -- and
git holds the superseded bytes either way, which is why the plan's own
rolling stamp keeps three entries and simply drops the fourth instead
of pushing it down into a history file. That cadence is not staleness
to be corrected by restamping more often.

It does not compete on the axis above, which is about STATUS: where
any two documents disagree about what is done, the ledger wins. The
plan carries a different authority, SEQUENCING. RICE ranks items in
isolation; bundling several items to complete a planned step
SUPERSEDES RICE order. The ledger already calls RICE
"prioritization for planning" -- this names what the planning is
and says it outranks the score.

**The same rule reaches past handoffs and manifests** (Tony's
ruling, 2026-08-20, L-221). Any session document -- a review
return, a design note, an analysis written this session -- can
assert that a question is open when the ledger has already settled
it. Being the newest file in the room makes a document's BYTES
current; it does not make it right about what was decided. Context
Priority ranks uploads above the repo for exactly the first reason
and not the second. So check a document's status claims against the
ledger before acting on them, and raise the disagreement rather
than resolving it silently. (Origin, 2026-08-20: a document's
closing section said a decision "belongs to Tony"; the ledger had
ruled it two sessions earlier and a build step depended on the
ruling.)

### Where We Are -- Tony's page [QUALITY]

`documentation/WHERE_WE_ARE.md` is the one document written for Tony
rather than for the work (v1.13, L-396). It is not a rung in the status
ordering and it is not another zoom of the master plan: the ledger still
wins on status and the plan on sequencing. It restates both in plain
words, for a reader who cannot hold the detail. Tony, 2026-09-30: "i
struggle to keep the big picture. it's the old dilemma of loosing the
forest for the trees." The plan's summary and critical path had been
tried for that job and had not really helped, by his account: they are
written for the work, and they move only at design builds.

- ONE file, edited IN PLACE, never versioned. Git holds the history.
  Old changes drop off the page; the ledger and git keep them.
- Updated at the END OF EVERY SESSION that changed the picture, inside
  that session's ledger patch, so it moves in the same transaction and
  costs Tony no extra run. A session with no patch that still changed
  the picture delivers a small one.
- A PATCH EDITS THE PAGE BY SECTION, AT EACH SECTION'S OWN ANCHOR
  (v1.17, L-422), never by rewriting the whole page. Two sessions
  closing the same day then each change their own lines and neither
  loses the other's. The failure this prevents: patch_L418_2, built on
  fbd223ee before the Horizons design session, rewrote the page whole
  and left it saying that design round was still ahead after it had
  happened. A whole-page rewrite is the exception, for a change of the
  page's SHAPE, and it copies every line of the page it replaces into
  the session's handoff first.
- THE RUN-RECORD ZONE (v1.17; Tony, 2026-10-07: "I use the where we are
  to record the run record and rename it with a time stamp."). The
  page ends with the marker line `--- Your run record below this line`,
  and everything under it is Tony's. He pastes the patch output and the
  test checklist there and answers each line in place ("-- yes", "--
  not clear", "-- let's discuss"), then saves the whole page as a
  timestamped copy, `documentation/WHERE_WE_ARE_<m-d-yy>_<hhmm>_run_record.md`,
  flat beside the live page (no subfolder: "I already mix handoffs,
  patches, design documents. Subfolders are more steps and also I scan
  the files to see what the recent changes were."). Three rules
  follow. No patch edits below the marker. The length cap counts only
  the lines above it. And a session's close READS HIS LATEST COPY
  before it writes anything: his verdicts there are the primary record
  of his rulings, so the ledger quotes them from the copy and names the
  copy, instead of re-pasting them into the handoff. His "-- not
  clear" and "-- let's discuss" lines are the open design items in his
  own words and go onto the page's design-talk list verbatim, with the
  date. Once read, the close empties the live zone; the copy is the
  record.
- TONY ANNOTATES THIS PAGE, THE HANDOFFS AND THE LEDGER, and a patch
  never refuses his notes (L-419; Tony, 2026-10-03, and 2026-10-05: "i
  am using our handoffs or the where we are as run records"). So a
  patch checks each of the three only at the lines it edits -- an
  anchor that must match there -- never by a fingerprint of the whole
  file. `documentation/patch_L413_4_session_close_20261005.py` is the
  worked example of carrying his notes; the failure it answers:
  patch_L413_3 fingerprinted the whole page and refused on two "--
  done" marks; Tony, "i though annotations would not be refused."
- A FIXED SHAPE that does not grow (v1.17 shape, L-422; Tony:
  "Confirmed"). EACH FACT APPEARS ONCE. In order: the header (the date,
  and the SHAs it was written at); the READ THIS FIRST box, which IS
  the page -- changed since you last read this, do next, needs you now;
  one line on the marks; THE ROAD, one numbered line per stage, the
  done stages folded into one line, marked [done], [NOW], [next],
  [later] or [goal]; SETTLED, one dated line per standing ruling from
  the last few sessions so a session does not re-raise it, each line
  leaving after a few weeks once it is habit; SIGNALS, three numbers
  READ FROM FILES when the page is written, never typed from memory --
  the last cache build and whether a rename needed a retry (gallery
  `data/cache_swap_log.jsonl`), the Tier-1 count on the files the push
  gate watches (`PROVENANCE_AUDIT.md`; until a tool prints the
  gate-path figure the line says so), and the page's own date against
  the ledger's newest stamp; WAITING ON YOU, split into at the next
  design talk, decisions one at a time, and not urgent in his order --
  the "now" half lives in the box; WHERE THE DETAILS ARE, last and
  short; then the marker and the run-record zone. The sections this
  replaced -- the goal, right now, the next three steps, six lines on
  the marks -- each repeated something the box or the road already
  said. About 110 lines above the marker; the check below holds it.
- ATTENTION MARKS, cleared and reset at every update so that they
  always mean "new since you last read this": **>> UPDATED THIS
  SESSION** beside a changed section's heading; "<< new this session"
  or "<< moved this session" beside a road stage; and *italics* on the
  must-reads -- the one next step, anything that needs Tony now, and
  the [NOW] stage. Tony: "attention is a human limitation."
- PLAIN WORDS IN SHORT BULLETS, one idea per bullet, no paragraphs.
  Tony, 2026-09-30: "the wall of text even a paragraph is an obstacle."
  A LEDGER HANDLE ON THIS PAGE ALWAYS CARRIES A SHORT LABEL IN
  PARENTHESES -- "L-421 (the typed facts)", never a bare L-421 --
  wherever it appears (Tony, 2026-10-07: "all ledger L-xxx items
  should have a brief parenthetical label"). Prefer the plain name in
  the body, and the handle where he will go and look the item up. The
  same holds in handoffs and in chat: a handle is the name of a thing,
  and only one of us can read it (the Register Rule). The Register
  Rule applies in full: this page is in the chat's register, not the
  reference register of this skill.
- At the end of a TURN that changes the picture, Claude's reply closes
  with two or three bullets under "Where this leaves us", in the page's
  own words. The page itself moves at session end.
- THE CHECK, recorded on L-396 and not yet built (v1.17 form): the
  orrery maintenance run fails when the page's "Last updated" date is
  older than the ledger's newest header stamp, OR when more than 130
  lines stand above the run-record marker. It targets the exact
  filename `WHERE_WE_ARE.md`, so a timestamped copy cannot stand in for
  the page; the doc indexer knows a copy by its `_run_record` ending.
  An unchecked store drifts, as the plan's two companions did for a
  month (L-333, L-362). Until the check is built, this rule is the only
  thing keeping the page current and short.

## Ledger Block Format

Write ONLY the detail block; then run ledger_index.py to regenerate all
index tables. NEVER hand-edit the index zone (between
<!-- INDEX:START --> and <!-- INDEX:END -->) and never hand-paste summary
rows.

```
#### [L-NNN] Title (track/category)
<!-- L:NNN status:OPEN upd:2026-07-01 section:A flag: rice:R/I/C/E -->
- Body: context, decisions, constraints. Bullets are fine here.
**Tony:** async comments from Tony to the next session -- address before
building.
**Note:** or **Claude:** -- Claude's own annotations (proposed RICE
scores, verification results, corrections, open questions for Tony).
**Gap:** what remains to close the item.
**Ref:** related files, handoffs, cross-linked L-handles.
```

- **Tony:** is reserved EXCLUSIVELY for Tony's own hand-written comments --
  never a label Claude applies to its own text, even when proposing
  something for Tony to react to (a RICE score, a verification result).
  Claude's own annotations use **Note:** or **Claude:** instead.
  Mislabeling a Claude-authored proposal as **Tony:** makes a draft read
  as if Tony already said something he didn't -- caught in this project's
  own ledger drafts (L-126/L-127, July 2026) before they were pasted in,
  not after.
- **Tony-action (do)** and **Tony-action (decide)** tag individual
  bullets -- inline, wherever they occur in the body or the Gap -- not a
  single top-level field like Gap:/Ref:, since an entry can carry several.
  **(do)** marks a mechanical, hands-on-keyboard action only Tony can
  perform: a file move via GitHub Desktop, a skill reinstall, running a
  script via VS Code's Run button, a push. No judgment required, just
  execution. **(decide)** marks a confirmation or judgment call only
  Tony's authority can give: approving an archive list, confirming a
  deletion, picking between two options -- an AI could often reason its
  way to a recommendation, but sole commit authority means it waits for
  Tony's explicit word before acting on it. Rollup rule: every
  Tony-action item, of either kind, gets swept into one consolidated
  list at the close of any ledger session or handoff -- never left
  scattered across the body where it was first raised. Applies whether
  the document is addressed to Tony, to another AI session, or both.
  (Surfaced when a design handoff's Tony-only items had no consistent
  tag and had to be hunted down by hand across a builder session's own
  report -- see the version-header note above.)
- Header regex: `#### [L-NNN] title` (an optional `| #tag` after the
  number is supported). The metadata comment's L number MUST match the
  header -- the indexer flags disagreement.
- status vocabulary: OPEN, BLOCKED, PENDING-GATE (these show Gap in the
  index), DONE and friends for closed. Sections: A (active), B/PENDING,
  C (closed archive -- items migrate there and STAY; the archive is
  institutional memory), D.* (categorized backlogs).
- RICE: rice:R/I/C/E with / separators (decimals allowed).
  Score = R x I x (C/100) / E. Scored items sort to the top of their
  section descending; unscored show --.
  AN ITEM INSIDE AN ORDERED LIST NEEDS NO RICE SCORE (v1.17; Tony's
  ruling of 2026-10-07, L-412). A list such as the Sun's slice (L-412)
  or Earth's list (L-413) IS the priority, under the master plan's
  sequencing authority (L-221), and a score beside it would only
  disagree with it. An item outside any list keeps RICE, and gets a
  coarse score when it is next opened rather than at creation. The
  index shows -- for the unscored; for list items that is expected.
- New items get the NEXT L-handle; NOTHING is ever renumbered. Reference
  work by L-handle, never by per-handoff item numbers (handoff numbering
  gets rebased across versions and items LEAK at the rebase -- the v23-v27
  chain lost real items that way; one authoritative running ledger is the
  cure).
- Capture on first mention: promote observations into the ledger
  immediately, even if no work happens yet. Floating items get lost.
- Verification honesty tags where useful: [verified @<sha>] vs
  [per chain] vs [render-gated] -- the ledger states which of its own
  claims are checked vs carried.

### A Closing Item Re-homes Its Loose Ends [QUALITY]

Before an item's status goes to DONE, read its body for work it
records as NOT done -- "not done, recorded", "add when X is next
open", a Gap saying another item carries something. Each one gets one
of two outcomes in the closing patch:

- a line in an OPEN item whose files that work will open (by files
  touched, as in the section below), naming the closing item; or
- struck in the closing item, with the reason.

The closing item's own record then says where each one went, by
handle.

The reason is where readers look. A closed item moves to section C,
and section C is institutional memory, not a backlog: no session
opens it to find the next job. A not-done line inside it is a floating
item that happens to have a handle -- Capture on First Mention
satisfied in form and defeated in effect.

Check a pointer as well as a line. A Gap saying "L-NNN carries it" is
a claim about another block; open that block and find the work in it.

(Origin, 2026-09-10, closing L-291 and L-303; Tony confirmed it as
method rather than a ruling. Three loose ends: Earth's rotation
period, recorded in L-291's body and pointed by its Gap and its
handoff at L-292, which never mentioned it; a planetocentric
`as_of_today` test inside L-168, closed the day before; and the
gallery editor's Copy carrying a card's pairing tag, inside L-303 --
which had already fired on the first Earth card, hiding it from the
desktop lobby, before anyone looked. L-311, L-237 and L-312 received
them.)

### Cluster the Tail by Topic, Not by Age [QUALITY]

RICE Effort is not a property of an item. It is a property of an item
GIVEN what else is open. Scoring each one alone is what produces a
tail: by August 2026 this ledger held 107 open items, 54 of them both
below RICE 3.0 and untouched for over 30 days, and a score-ordered
board cannot distinguish "correctly deprioritized" from "dropped."

The move is not a scheduled cleanup event. It is a STEP inside every
job: when work is scheduled, sweep the open ledger for items whose
FILES the job already opens, and clear them in the same patch. Sitting
inside a file the job has already fingerprinted lowers Effort, raises
Confidence, and lets one patch carry reach neither item had alone.

**Cluster by FILES TOUCHED, not by keyword.** A keyword sweep for the
worksheet-builder topic returned 36 items including a comet-tail
animation, a food-insecurity track and a ring-colour audit -- shared
vocabulary, unrelated work. The file list a job already holds is the
version that survives being run twice.

Two findings from the first run, and both are the reason it is worth
doing:
- An item 69 days old at RICE 1.0 was ALREADY DONE. The work had been
  finished and nobody closed the entry, so it sat in the tail counted
  as debt. A tail nobody looks at cannot say which of its items are
  dead.
- A ruled ASCII violation sat in a file the session had already
  fingerprinted, opened and edited. The safe-file-editing sweep
  conditions all held. The count was printed by the patch's own
  encoding report and read past, because the item that gave it meaning
  was seventy rows down a list sorted by score.

(Tony's proposal, 2026-08-19, replacing a by-age triage Claude had
recommended. His reasoning is the rule: coordination raises Reach,
Impact and Confidence at the same time as it lowers Effort.)

## Anchor Requirement (all outbound documents)

Any document that leaves the live session -- handoff, manifest,
as-built, review request, or a prompt/audit carried to another AI
(Mode 7 relay) -- opens with: built on <SHA> at <URL>, and after a
push, pushed at <new SHA>. Multi-repo work pins EACH repo's SHA+URL
separately (orrery and gallery move independently):
  - orrery: https://github.com/tonylquintanilla/palomas_orrery
  - gallery: https://github.com/tonylquintanilla/tonyquintanilla.github.io
This is the document-layer form of the protocol's SHA Round Trip
CRITICAL gate -- applies uniformly regardless of document type or
audience.

**A document leaving this Project needs a SECOND anchor line** when the
receiving partner has no resident protocol and no installed skills --
true for GPT, Gemini, and any Claude session outside this account and
Project (L-290). The code anchor says WHICH BYTES to read; this one
says WHAT RULES the work runs under. Without it a partner operates on
the code with none of the conventions governing how the work is done.

NAME THE SKILLS THE TASK FIRES, not a blanket list. Same judgment the
resident protocol already asks for under "Relevant skill unfired ->
Load it by name": a provenance review needs provenance-discipline, a
review prompt carried to another model needs provenance-cross-check
beside it, a patch needs safe-file-editing, and sending them all
teaches the partner to skim.

The wording depends on what the partner can actually do:

- **Claude or GPT (fetch-capable).** Name the files as fetch targets at
  the same pinned SHA: "also fetch PROJECT_INSTRUCTIONS.md and
  skills/<name>/SKILL.md at <SHA>." These partners pull the exact bytes
  the way they pull code -- L-191 records Fable running `git ls-remote`
  against a pinned SHA and parsing the source.
- **Gemini (snapshot-only, L-276).** Split by WHICH REPO WAS IMPORTED,
  not by whether it can fetch. `PROJECT_INSTRUCTIONS.md` and `skills/`
  live IN the orrery repo, so a Gemini that imported the orrery ALREADY
  HAS both -- unpinnable, fixed to whenever the import happened, but
  present. Name the import state and point at the paths: "operating
  from an orrery snapshot imported [date]; the protocol and skills are
  in that snapshot at `PROJECT_INSTRUCTIONS.md` and `skills/`."
  Gemini imports ONE repository, so a GALLERY import leaves it with no
  protocol and no skills at all -- they are in the other repo. THAT is
  the paste case: state the limitation and put the relevant excerpt in
  the document itself rather than pointing at a path.

**ASK FOR THE READ-BACK.** The outbound document asks the partner to
state which rule files it actually read. A return document that does
not name them is telling you it did not read them. This is the only
part of the mechanism that can FAIL VISIBLY; the anchor line itself
cannot, because a document that omits it looks exactly like one that
did not need it (A Check That Cannot Fail Is Not Passing).

Either way the requirement is the one above, one layer up: an
un-anchored document does not say what it describes, and for a partner
with no resident layer, "what it describes" includes the rules and not
only the code.

(Origin, 2026-09-06: a parallel Claude Sonnet session, outside this
account and Project, reached a correct conclusion and then proposed a
handle already taken and offered a ledger entry "ready to paste" --
both exactly the failures this rule prevents. It had the code and none
of the ledger skill's delivery rules. Tony ruled it in the same
session, his reason being that work now moves between Opus, Fable and
GPT under credit limits, so the relay discipline is load-bearing
precisely when the flexibility is wanted.)

## Where a File Goes [QUALITY]

Two directories, and the test is not how finished the file is.

  documentation/            read by a PERSON, occasionally
  documentation/worksheets/ read by a TOOL, on every run

A worksheet is the most finished thing in the project -- immutable
evidence, fixed at its date, never edited -- and it lives in
worksheets/ because worksheet_checker.py opens it every run. A handoff
is equally frozen and lives in documentation/ because no code opens
it. So "active versus archived" is the wrong cut; "input versus
record" is the right one.

Applied:
- worksheets, request files the builder emits, prompt templates,
  pinned key lists, site lists  -> documentation/worksheets/
- handoffs, as-builts, manifests, design reviews, spent patch scripts,
  archived protocol copies                      -> documentation/

WHICH REPOSITORY, AND NO SUBFOLDERS (v1.17, L-422). Tony's practice,
stated 2026-09-22: "my practice is to put all documentation in the
orrery documentation/ folder. i reserve the gallery documentation/
folder for the patch files." So every RECORD -- a handoff, a
manifest, a design note, a session record, a timestamped run-record
copy of Where We Are -- goes to the ORRERY's documentation/, whichever
repository the work touched; a spent GALLERY patch script goes to the
gallery's documentation/. The gallery's documentation/ also holds the
tool inputs its maintenance run reads (smoke suites, fixtures,
recorded payloads): those are inputs by the test above and stay where
the code reads them. And documentation/ stays FLAT. Tony, 2026-10-07,
declining a run_records/ folder: "I already mix handoffs, patches,
design documents. Subfolders are more steps and also I scan the files
to see what the recent changes were." A file's name carries its kind;
the folder does not.

Two consequences worth stating.

A tool input must not be filed by resemblance. The as-built describing
a batch of request files is a record and stays in documentation/, even
though it is about files that live in worksheets/.

A non-.md file is invisible to the checker's loader, which takes only
.md from that directory. That is why a .txt pin list can sit in
worksheets/ without becoming a phantom uncited worksheet -- checked,
not assumed, before the two files were moved there.

(Origin, August 14, 2026: the L-192 site list and key pins were first
written to documentation/ among the handoffs and the roughly one
hundred spent patch scripts. Tony moved them and named the reason. The
wording here is the corrected form of his rule -- his "live versus
finished" cut would have sent the worksheets themselves the other
way.)

## Handoff Structure (the load-bearing lines)

Every handoff opens with:
- Base SHA and URL per the Anchor Requirement above.
- Type declaration: BUILD / DESIGN SESSION (zero code) / DOCUMENTATION.
- Supersedes / companion lines (what this replaces; which manifest pairs
  with it). Superseded handoffs remain authoritative AS SESSION RECORDS
  by reference; their embedded ledgers do not.
Body: what was done (verified vs claimed), discrepancies surfaced,
open decisions for Tony, next-session scoping. Close with the credit
line ("Session/entry written [Month Year] with Anthropic's Claude
[model]").

## Protocol and Skills Change Log (v3.30 addition)

The protocol's version history lives in
`documentation/PROJECT_INSTRUCTIONS_HISTORY.md`, PART 1. The protocol
itself keeps the THREE most recent entries resident; a fourth pushes
the oldest down into that file, so an entry lives in exactly one place
and never both. (Until 2026-08-23 this paragraph said the history
lived in the ledger's appendix. v3.41 replaced that appendix with a
pointer on 2026-08-18 and this sentence did not follow -- the section
that owns the change-log convention carrying a stale claim about where
the log lives. The Correction Does Not Travel, safe-file-editing 1.8.)
Skill revisions are ledger entries too: each skill's SKILL.md carries a
version line + source SHA; a skill update gets an L-item (or a line in
the version-history appendix) recording skill name, new version, and the
SHA it was cut from. The resident protocol's Skill Manifest table states
the EXPECTED installed versions -- a mismatch STOPS the session under the
resident Stale Skill = Stop [CRITICAL] gate, which also tells Tony the two
actions needed (push to skills/, reinstall to the account profile).

**A skill keeps three version entries [QUALITY]** (L-418, Tony,
2026-10-05). The protocol's own rule, applied to the skills: a SKILL.md
keeps its three latest version entries under its version line, and the
patch that adds a fourth moves the oldest, word for word, to the end of
that skill's section in `documentation/SKILL_HISTORIES.md`. A skill
over Anthropic's 500-line guideline also opens with a `## Contents` list
of its headings, which `skills_index.py --check` holds to the headings
item by item; a patch that adds, removes or renames a heading updates
the list in the same edit. A file longer than one read -- 16,000
characters or 2,000 lines, the smaller of the two readers measured --
opens, just under its title, with a READ PLAN naming the line ranges
to read it in, one read each (v1.18, L-418). A patch puts the seed
line there, `Read this file in parts.`, and `skills_index.py` writes
the plan; `--check` fails on a long file with none, a part over one
read, or a line no part covers. A long skill still waiting for its
plan is named on the list `PLAN_NOT_YET` in `skills_index.py`, which
every run prints; it gets the plan at its next version, and comes off
the list in the same patch. A skill's extra files live in its
`references/` folder, each named in its SKILL.md with the moment to
open it; `--check` fails on one named and missing, or present and
never named. All of this for one reason: a plain read of a long file
shows only part of it -- its start and end in one reader, its start
alone in another -- so what opens a skill is the one part every
session is sure to see.

**Binding rule [QUALITY].** A skill version bump is not done until the
manifest agrees AND the protocol's history says what changed. FOUR
steps travel in ONE commit:

1. Bump the version line in `SKILL.md`.
2. Run `skills_index.py`.
3. Add a **protocol version-history entry** to
   `PROJECT_INSTRUCTIONS.md` naming the skill, the new version, and
   WHY -- and push the oldest resident entry down into
   `documentation/PROJECT_INSTRUCTIONS_HISTORY.md` if that makes a
   fourth.
4. Commit `SKILL.md`, `PROJECT_INSTRUCTIONS.md` and the archive
   together.

Do not leave any of it to a later checkpoint someone has to remember.

**ONE SESSION, ONE BUMP [QUALITY].** A session does not ship two
versions of one skill. Everything a session decides about a given skill
rides a SINGLE version number, in a single commit, under the four steps
above. Two amendments arriving the same evening do not become 1.10 and
1.11; they become one 1.10 carrying both. (Tony's ruling, 2026-09-06,
when L-290's relay-anchor amendment and L-296's plan-version rule both
wanted 1.10. Each bump costs a protocol history entry, a manifest
regeneration and a reinstall, so splitting them multiplies the
ceremony and the chances of step 3 not firing -- and it makes the
version history harder to read, since two entries then describe one
evening.)

**A WRONG SENTENCE IN A SKILL: BUMP NOW, OR CARRY IT [QUALITY].**
(v1.14, L-405.) A skill loads every session and is followed without
being noticed, so the test is what a session would DO if it followed the
wrong sentence as written.

- **It would do something wrong** -- edit the wrong file, skip or trust
  the wrong check, write a wrong number, tell Tony something false.
  Correct it in THIS session. If the session is not otherwise bumping
  that skill, this is a bump of its own: one wrong instruction is
  enough to earn one.
- **It would do nothing different** -- the sentence is a description
  that has gone out of date, a count or a list that has grown, a claim
  no step depends on. Carry it on a ledger item for the skill's next
  version, name it in the patch output (The Correction Does Not
  Travel), and correct it then. The ceremony of a bump -- a protocol
  entry, a manifest run, a reinstall -- is not spent on a sentence no
  one acts on.
- **If the session is already bumping that skill**, any wrong sentence
  in it rides that bump, whichever kind it is. One Session, One Bump.

When it is unclear which of the first two a sentence is, treat it as
the first. The worked case: interactive-exhibit 1.8 said every reader of
`data/objects_config.json` ignores its `"rooms"` section. A session
following it would at worst have looked in fewer places for a reader,
so on 2026-10-01 it was carried (L-404 to L-405), and corrected at 1.9.

**Step 3 is the one that stops firing** (Tony's observation,
2026-08-23). Steps 1, 2 and 4 are visible -- you are editing the file,
running the tool, making the commit. Step 3 is the only one with no
artifact prompting it, so it is the one that gets skipped, and the
manifest going current on its own DISGUISES the omission: the protocol
looks updated because half of it was. It is not a new rule --
`v3.35 (August 7, 2026): Updated skill safe-file-editing (v1.3).`
is a skill bump earning an entry on its own. It stopped firing, which
is harder to notice than a rule that never existed.

Detection for step 3 is designed and unbuilt (L-230): a
maintenance-suite checker that reports when a skill version changed
since the last run and the protocol version did not. It has to watch
the TRANSITION -- the naive form, asking whether each manifested
version appears somewhere in the written history, was measured on
2026-08-23 and reports 10 of 10 skills, which is a check nobody reads
twice.

This is the PREVENTION side. Detection is the resident protocol's
Stale Skill = Stop [CRITICAL] gate, which halts a session outright when a
loaded skill's version disagrees with the manifest row. Two layers because
prevention depends on remembering and detection does not: if the binding
rule is followed there is no window, and if it is missed the gate catches
it before any work is done on the wrong copy.

The reason is not tidiness. The protocol tells a session that finds a
skill-version mismatch to stop and reconcile, the same rule as a SHA
mismatch. A stale manifest therefore fires that alarm on every session
that loads the affected skill -- and an alarm that is always wrong is one
the reader learns to wave off, which is the state in which a REAL mismatch
stops registering. Bound to the commit, drift cannot exist at any pushed
SHA. (Earned: the manifest advertised 1.1/1.4 against an actual 1.2/1.6
for about three weeks, provenance-discipline having already gone stale a
version earlier -- Fable skills-layer review, Job 3 #8. `skills_index.py`
now prints what the manifest was advertising before it overwrites it, so
running the tool reports the drift instead of silently absorbing it.)

## Codebase Tooling

- module_atlas.py generates MODULE_ATLAS.md (roles, functions,
  dependency graph). Role classifications feed the provenance scanner's
  role-driven gate. A new module is picked up by adding a Role:/Domain:
  tag to its OWN docstring -- ROLE_MAP is a generated mirror since L-163
  Phase 3, rebuilt from those tags by regenerate_role_map() into a
  START/END marker zone (the pattern ledger_index.py uses for its INDEX).
  Hand-editing ROLE_MAP does nothing: the next module_atlas.py run
  overwrites it. Coverage-gap findings point at modules missing a tag.
- add_docstrings.py batch-inserts the module docstring standard.
- dep_trace.py builds the interactive dependency graph -- use it before
  multi-file changes to map touchpoints.
- ledger_index.py: regenerates the index zone in place; also supports
  migrating closed items to section C.
- skills_index.py: regenerates the Skill Manifest table from the
  skills/*/SKILL.md files and consistency-checks them. Same marker-zone
  pattern as the two above. It targets the LIVE protocol only
  (PROJECT_INSTRUCTIONS.md in the repo root); the versioned copies under
  documentation/ are archival snapshots the tool deliberately never
  rewrites, so do not expect a run to update them and do not hand-sync
  them either -- an archive that keeps changing is not an archive. Since
  August 2026 the run also PRINTS what the manifest was advertising before
  it overwrites it, so drift is reported rather than silently absorbed.
  See the binding rule under Protocol and Skills Change Log.

## Field Notes

- Enumerate the full /documentation set before reviewing a handoff chain
  (the enumerate-before-claiming-a-review gate applies to repo docs as
  much as uploads).
- Verify load-bearing chain claims against live code at HEAD, not
  handoff prose -- the v28 consolidation found "open" items already done
  and done-claims still open.
- A stale erratum can outlive its truth; when the code at HEAD
  contradicts a recorded status, the code wins and the record gets
  corrected.
- A skill can go stale on an installed account even while the repo copy
  is current -- diff the two directly rather than trusting either one's
  version line (L-163 build-prep, July 2026: an installed copy read 1.1
  while the repo carried 1.2; the delta was itself a rule governing the
  session's own deliverables).
