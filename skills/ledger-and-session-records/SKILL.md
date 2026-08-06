---
name: ledger-and-session-records
description: Ledger and session-record conventions for the Paloma's Orrery project. Use when creating, updating, or closing items in LEDGER_CONSOLIDATED.md, running or modifying ledger_index.py, RICE-scoring items, writing or reading session handoffs or build manifests, recording protocol or skill version changes, regenerating MODULE_ATLAS.md via module_atlas.py, or tracing dependencies with dep_trace.py. Trigger words include L-handle references (L-001, L-078...), "ledger", "handoff", "manifest", "RICE", "module atlas", "dependency trace". Do not use for projects other than Paloma's Orrery.
fires_when: Ledger edits, ledger_index.py, RICE, handoffs, manifests, atlas, dep_trace
---

# Ledger and Session Records

Skill version: 1.5 | Cut from palomas_orrery @ 3398970 | August 5, 2026
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
next module_atlas.py run overwrites.

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

The protocol's version history lives in the ledger (appendix section),
not in the protocol (which keeps the last few entries as a pointer).
Skill revisions are ledger entries too: each skill's SKILL.md carries a
version line + source SHA; a skill update gets an L-item (or a line in
the version-history appendix) recording skill name, new version, and the
SHA it was cut from. The resident protocol's Skill Manifest table states
the EXPECTED installed versions -- a mismatch STOPS the session under the
resident Stale Skill = Stop [CRITICAL] gate, which also tells Tony the two
actions needed (push to skills/, reinstall to the account profile).

**Binding rule [QUALITY].** A skill version bump is not done until the
manifest agrees. The three steps travel in ONE commit: bump the version
line in SKILL.md -> run `skills_index.py` -> commit SKILL.md and both
protocol copies together. Do not leave the regeneration to a later
checkpoint someone has to remember.

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
