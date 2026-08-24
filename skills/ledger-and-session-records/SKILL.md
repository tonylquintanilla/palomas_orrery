---
name: ledger-and-session-records
description: Ledger and session-record conventions for the Paloma's Orrery project. Use when creating, updating, or closing items in LEDGER_CONSOLIDATED.md, running or modifying ledger_index.py, RICE-scoring items, writing or reading session handoffs or build manifests, recording protocol or skill version changes, regenerating MODULE_ATLAS.md via module_atlas.py, or tracing dependencies with dep_trace.py. Trigger words include L-handle references (L-001, L-078...), "ledger", "handoff", "manifest", "RICE", "module atlas", "dependency trace". Do not use for projects other than Paloma's Orrery.
fires_when: Ledger edits, ledger_index.py, RICE, handoffs, manifests, atlas, dep_trace
---

# Ledger and Session Records

Skill version: 1.9 | Cut from palomas_orrery @ 41c0b279 (v1.9), earlier
@ 3586970d (v1.8), @ 434a712b (v1.7), @ 305b269 (v1.6), @ 3398970
(v1.5) | August 23, 2026, with Anthropic's Claude Opus 5
Sources: LEDGER_CONSOLIDATED.md header, ledger_index.py at HEAD, handoff
v28 (consolidation) and v29 (cleanup), food insecurity handoffs. v1.3
adds the Tony-action (do)/(decide) tag convention and its rollup rule,
surfaced during the L-163 build-prep session (July 24, 2026) when a
handoff's Tony-only to-do items were found scattered across its body
with no consistent tag, discovered only because a builder session
(Opus 5) had to hunt for them by reading the whole document. v1.4
rewrites the Codebase Tooling ROLE_MAP bullet for L-163 Phase 3: a new
module is classified by tagging its own docstring, not by hand-adding a
ROLE_MAP entry, because ROLE_MAP became a regenerated mirror that the
next module_atlas.py run overwrites. v1.7 adds Cluster the Tail by
Topic, Not by Age -- Tony's ruling of August 19, 2026, replacing a
by-age triage, after a measurement found 54 of 107 open items both
below RICE 3.0 and untouched for a month (L-215). v1.8 adds the
master plan to The Document Stack as a SEQUENCING authority rather
than a rung in the status ordering, with Tony's ruling that
bundling items to complete a planned step supersedes RICE order,
and extends the status rule from handoff-vs-manifest to any session
document contradicting a settled ledger decision (both L-221,
August 20, 2026). v1.9 (L-230) does two things to the Protocol and
Skills Change Log. It adds the FOURTH step to the binding rule -- a
skill bump also earns a protocol version-history entry, which is
Tony's observation of August 23, 2026 that three links of a
four-link chain were firing. And it corrects that section's own
opening claim, which still said the protocol's version history lives
in the ledger appendix five days after v3.41 replaced that appendix
with a pointer.

Note: READING the ledger at session start is resident Part-1 behavior,
not this skill's job. This skill carries the maintenance mechanics.

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
are going, not what is directly in front -- traced at three levels
of zoom: the full plan, its summary, and the critical path. It
restamps at key junctures rather than at every change, because a
juncture is its unit; stepwise updating is the ledger's job. That
cadence is not staleness to be corrected by restamping more often.

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
