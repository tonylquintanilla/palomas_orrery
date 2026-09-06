# L-290 -- Relay anchors must name the protocol and skills: two drafts for Tony's ruling

**Built on** orrery `a57e86b82503380e92b4e78cd7d8995a71183f20` at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Carried into this file 2026-09-06 by Claude Fable 5.1 from a parallel
Claude Sonnet session Tony ran the same day. These are PROPOSALS. Nothing
below has been applied to PROJECT_INSTRUCTIONS.md or to any skill.

## What is being proposed, in one paragraph

Every outbound document already opens with the code repo's SHA and URL
(the Anchor Requirement). That tells a partner WHICH bytes to read. It
does not tell a partner with no resident access -- GPT, Gemini, or a
Claude session outside Tony's account and Project -- HOW this project
works, because that partner has no PROJECT_INSTRUCTIONS.md and no
installed skills. The proposal adds a second anchor line for such
partners: fetch-capable ones are told which rule files to fetch at the
same pinned SHA; Gemini, which can only import a snapshot (L-276), gets
the relevant excerpt pasted inline with the limitation stated.

## Two corrections to the Sonnet text before it is used

- It proposed the handle **L-288**. L-288 and L-289 were already taken;
  the ledger opens this as **L-290**.
- It offered the ledger entry "ready to paste". The ledger skill rules
  that out; the entry went in by fingerprinted patch
  (`patch_L289_5_ledger_mode5_rounds.py`). The drafts below are the
  parts Tony must rule on before they can be patched anywhere.

## Draft 1 -- resident protocol amendment (PROJECT_INSTRUCTIONS.md)

Extend the "Documents as handoffs" bullet under Mode 7 -> Key Principles.
The first paragraph is the current text; the second is the addition.

```
- Documents as handoffs: Copy/paste AI responses to share context --
  every outbound document (audit prompt, review request, relay
  manifest) opens with built on <SHA> at <URL>, same as a handoff.
  The repo moves, so an un-anchored document does not say which
  state it describes. A partner that can fetch needs the anchor to
  fetch the right bytes; a partner that cannot needs it to know what
  it is reading.
  A partner without resident access to this Project -- GPT, Gemini,
  or a Claude instance outside it -- also has no PROJECT_INSTRUCTIONS.md
  and no installed skills. The anchor for such a document names those
  as fetch targets too, not just the code repo, or the partner
  operates on the code with none of the conventions governing how the
  work is done. Wording differs by what the partner can actually do
  with a SHA (ledger-and-session-records carries the template).
```

## Draft 2 -- skill amendment (skills/ledger-and-session-records/SKILL.md, 1.9 -> 1.10)

Extend the Anchor Requirement section. The first paragraph is the
current text; everything from the bold sentence on is the addition.

```
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

**A document leaving this Project also needs a second anchor line**
when the receiving partner has no resident protocol or installed
skills -- true for GPT, Gemini, and any Claude session outside this
account/Project (L-290). What that line says depends on what the
partner can do with a SHA:

- Claude or GPT (fetch-capable): name the specific files as fetch
  targets at the same pinned SHA -- "also fetch
  PROJECT_INSTRUCTIONS.md and skills/<name>/SKILL.md at <SHA>."
  These partners can pull the exact bytes the way they pull code.
- Gemini (snapshot-only): no SHA pin is possible for the protocol or
  skills any more than it is for the code (L-276). State the
  limitation instead of promising a fetch: "operating from a
  repo snapshot imported at [date/time]; the protocol and skill
  conventions below are stated inline because Gemini cannot fetch
  them independently" -- then paste the relevant excerpt into the
  document itself rather than pointing at a path.

Either way the requirement is the same one line up: an un-anchored
document doesn't say what it describes, and for a partner with no
resident layer, "what it describes" includes the rules, not only the
code.
```

## If Tony accepts

One push, four steps, per the Protocol and Skills Change Log rule:
the protocol edit (v3.54), the skill edit with its version line at 1.10
and its SHA stamp, the reinstall to the account (Settings > Skills), and
`skills_index.py` to regenerate the manifest. Then the NEXT session
confirms its loaded copy of ledger-and-session-records reads 1.10 before
doing ledger work -- a mid-session reinstall cannot be verified from
inside the session that made it (Stale Skill = Stop).

## One observation Fable adds

The Sonnet session reached the right conclusion but wrote the ledger
entry as a paste and picked a handle from memory. Both are exactly the
failures L-290 is about: a partner outside the Project did not have the
ledger skill's delivery rules or the live ledger's handle count. The
proposal would have told it where to fetch both.
