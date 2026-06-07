# Protocol Update -- v3.24 Draft

**Session:** May 18, 2026
**Source:** Phase C4 implementation review + cross-model workflow discussion

---

## What this update adds

Two operational patterns from the Phase C collegial workflow (Part 1),
one verification convention extending fetched-vs-recalled (Part 3),
and three process lessons (Part 5). Plus a version history entry.

---

## Part 1: Insert after Mode 7 "Patterns" table

### Collegial Artifacts

Three document types emerge from the collegial Mode 7 pattern. Each
has a specific role in the workflow:

**Manifest** -- the operational contract between AI models that will
never share a context window. Written by the auditing model (reads
source, extracts exact values, spots patterns, makes architectural
recommendations). Consumed by the implementing model (executes the
plan, catches edge cases the auditor missed). The manifest must
specify enough that the implementer can execute without ambiguity,
but leave enough room that the implementer can flag problems the
auditor didn't see. Bugs caught during implementation that aren't
in the manifest (Saturn double-offset, Neptune info marker position)
prove the pattern works -- the manifest's precision makes the
unspecified gaps visible.

**Reply document** -- Tony + implementing model's written response
to the manifest author's design questions and recommendations,
produced BEFORE implementation begins. Names each decision, states
the rationale, and flags any overrides (e.g. "changed from 'leave'
to 'strip'"). The reply doc is the record that Tony's judgment --
not the manifest author's recommendation -- governs the work.

**Handoff document** -- the implementation record. Documents every
deviation from the manifest, every correction applied, every
verification result, and every new issue discovered. The handoff
is the review artifact: since the manifest author never sees the
implementation, the handoff closes the review gap by recording
everything a reviewer would check. Each handoff must be
self-contained enough to start a new session cold.

These three artifacts form a complete audit trail: manifest (plan)
-> reply (decisions) -> handoff (execution + verification). Tony
carries all three between models.

---

## Part 3: Insert after "Fetched vs Recalled Convention"

### Targeted Mode 7 Verification for Recalled Content [QUALITY]

When implementation produces human-readable text (tooltip strings,
hover descriptions, encyclopedia entries) that synthesizes domain
knowledge rather than extracting it from source code, the content
falls in the "recalled" category of the fetched-vs-recalled
convention. Automated tests cannot catch factual errors in prose.
Visual verification catches rendering issues but not physics claims.

For recalled content with factual claims (belt component counts,
ring dimensions, magnetic tilt values, source citations), queue a
targeted Mode 7 pass: send the text to Gemini for factual
verification against authoritative sources. Same pattern as the
provenance audit. This is cheaper than a full implementation review
and targets the exact error class that other verification layers
miss.

Rule of thumb: if a string was composed during implementation rather
than extracted from source, it needs domain verification before it
propagates into renders.

---

## Part 5: Add to Lessons Archive -- Process

- Manifest-as-contract: the manifest is not documentation layered on
  top of the work -- it IS the interface between the thinking
  partnership and the mechanical execution layer. Its precision makes
  unspecified gaps visible, which is why implementers catch bugs the
  auditor missed (Saturn double-offset, Neptune info marker position,
  Uranus missing legendgroup -- none in the manifest, all caught
  during implementation). Phase C proved this across 9 sessions.

- Audit trail as review: in the collegial pattern, the manifest author
  never sees the implementation. What closes the review gap is the
  handoff document -- it records every deviation, correction, and
  decision. A future session (with any model) can reconstruct the
  full story. The audit trail IS the review. This is an unusual
  pattern worth naming: traditional engineering has the designer
  review the execution; the collegial pattern has the documentation
  review the execution.

- Verification gap analysis: the three verification layers (automated
  tests, code-level auditing during implementation, visual
  verification) cover different error classes. The gap is factual
  claims in human-readable text (tooltips, descriptions) composed
  during implementation. These pass all automated tests and may
  survive visual review. Targeted Mode 7 verification (Gemini
  fact-check) closes this specific gap. Identified during Phase C4
  handoff review, May 2026.

---

## Version History Entry

v3.24 (May 18, 2026): Collegial artifacts named as operational
patterns (manifest, reply document, handoff) in Part 1 Mode 7.
Targeted Mode 7 verification for recalled content added to Part 3
near fetched-vs-recalled convention. Three process lessons added
to Part 5: manifest-as-contract, audit trail as review, verification
gap analysis. Emerged from Phase C4 handoff completeness review --
tracing 26 deferred items across 6 handoffs revealed both the
strength of the audit trail and the one gap it doesn't cover
(factual claims in composed text).

---

## On the "actionable vs narrative" question

The protocol currently has a clear gradient from skill (Part 1) to
narrative (Part 4), with Part 2 and Part 3 as hybrids. This is the
right structure. The question is where new material lands.

The test: **would a session fail if it didn't read this?**

- Yes -> Part 1 (operational) or Part 3 (technical reference)
- Would produce lower quality but not fail -> Part 2 (principle) or
  Part 3 with QUALITY marker
- No, but shapes judgment over time -> Part 4 (foundation) or Part 5
  (lessons archive)

The collegial artifacts go in Part 1 because a session doing collegial
Mode 7 would fail to produce the right documents without knowing the
pattern. The targeted verification convention goes in Part 3 because
skipping it produces a specific, identifiable quality gap. The lessons
go in Part 5 because they're retrospective understanding -- the
"why" behind the patterns named elsewhere.

Lessons graduate when a failure demonstrates they were load-bearing.
"Bottom-up editing" started as a lesson and moved to Part 3 when
line-shift bugs proved it critical. If the tooltip verification gap
ever produces a factual error that propagates into a published
render, the QUALITY marker on the convention would move to CRITICAL.

The Sonnet 4.6 intermediate update was right to push toward
actionable: the more of Part 1 and Part 3 that reads as "do this,
check that," the less interpretation a new session needs. But Parts
2 and 4 should stay narrative -- they calibrate judgment, and
judgment can't be reduced to checklists. The procedural criticality
framework you added in v3.23 names this tension directly: "Not all
rules carry equal weight. The experienced operator knows which
checks are load-bearing."
