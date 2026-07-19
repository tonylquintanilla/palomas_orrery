---
name: ledger-and-session-records
description: Ledger and session-record conventions for the Paloma's Orrery project. Use when creating, updating, or closing items in LEDGER_CONSOLIDATED.md, running or modifying ledger_index.py, RICE-scoring items, writing or reading session handoffs or build manifests, recording protocol or skill version changes, regenerating MODULE_ATLAS.md via module_atlas.py, or tracing dependencies with dep_trace.py. Trigger words include L-handle references (L-001, L-078...), "ledger", "handoff", "manifest", "RICE", "module atlas", "dependency trace". Do not use for projects other than Paloma's Orrery.
fires_when: Ledger edits, ledger_index.py, RICE, handoffs, manifests, atlas, dep_trace
---

# Ledger and Session Records

Skill version: 1.2 | Cut from palomas_orrery @ 079a0ec5c6a72f83fa7904e469cd359912746221 | July 19, 2026
Sources: LEDGER_CONSOLIDATED.md header, ledger_index.py at HEAD, handoff
v28 (consolidation) and v29 (cleanup), food insecurity handoffs.

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
the EXPECTED installed versions -- reconcile a mismatch before trusting a
skill, the same way a SHA mismatch is reconciled before a build.

## Codebase Tooling

- module_atlas.py generates MODULE_ATLAS.md (roles, functions,
  dependency graph). ROLE_MAP classifications feed the provenance
  scanner's role-driven gate -- new modules need ROLE_MAP entries
  (coverage-gap findings point at the missing ones).
- add_docstrings.py batch-inserts the module docstring standard.
- dep_trace.py builds the interactive dependency graph -- use it before
  multi-file changes to map touchpoints.
- ledger_index.py: regenerates the index zone in place; also supports
  migrating closed items to section C.

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
