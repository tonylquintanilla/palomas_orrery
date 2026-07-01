# L-002 Pre-Design: Protocol → Skills Refactor (v2)

Tony Quintanilla, PE | Claude Opus 4.6 | July 1, 2026
Status: REFINED — ready for Fable 5 design conversation

---

## To Fable 5

This document is not a specification. It is a pre-design brief from a
conversational design session between Tony and Claude Opus 4.6. You
are being consulted as a senior software engineer whose advice and
insights we are seeking. We want your feedback on this document before
proceeding to final design. Where you see a better approach, say so.
Where you see gaps, name them. Where you'd restructure, propose it.

Your specific strengths that matter here: you can hold the full protocol
(807 lines) plus significant codebase context in your 1M window
simultaneously, reason about the architecture as a whole, and propose
solutions that account for interactions across the system. The longer
and more complex the problem, the larger your lead — and this is a
genuinely complex architectural problem.

What we need from you:
1. Read the full protocol v3.29 (attached) and the skill-creator
   SKILL.md (attached) to understand both the source material and the
   platform mechanics
2. Review this pre-design and give feedback — what works, what doesn't,
   what we missed
3. Propose the final skill architecture, including any alternatives or
   novel ideas we haven't considered
4. Write the actual SKILL.md files with YAML frontmatter
5. Write the trimmed protocol (everything that stays resident)
6. Produce a mapping table so we can verify nothing was lost

This is a collegial conversation. Push back where the pre-design is
wrong. Suggest ideas we haven't thought of. You are not being asked
to follow instructions — you are being asked to think.

---

## Context

### The project

Paloma's Orrery (palomasorrery.com) is a Python/Plotly climate and
solar system visualization suite, ~115 modules, ~86K lines. Tony is
the sole developer, working conversationally with Claude (primarily
Opus 4.6 and Sonnet 4.6/5) and occasionally Gemini for domain
validation. The project protocol (v3.29, 807 lines) governs how Tony
and Claude collaborate — it covers operational modes, coding
conventions, pipeline recipes, philosophical framework, and lessons
learned over 9 months of partnership.

### The problem

The protocol carries everything in every session. Most of it is
irrelevant to any given task. The provenance scanner mechanics don't
help when building a KMZ; the Gallery pipeline doesn't help when
editing hover text. This wastes context window and dilutes the
signal-to-noise ratio.

### The opportunity

The Anthropic skills system loads knowledge on demand when a trigger
description matches the task. This lets us separate what must always
be present (the partnership's DNA — judgment, philosophy, modes,
critical safety gates) from what should load only when needed (coding
conventions, pipeline recipes, tool-specific procedures).

Tony's broader vision goes further: skills as an extensible layer for
the whole project's accumulated knowledge — not just coding conventions
extracted from Part 3, but Earth System workflows, Gallery pipeline
recipes, provenance procedures, ledger management. Knowledge that
currently lives in handoffs, memory, and conversation history, and
has to be re-established every session.

### Conversational context for Tony's workflow

Tony describes himself as a "vibe coder" — learning through building,
following curiosity. He is a retired professional engineer (PE), an
artist, and has an anthropology background. He values conversational
collaboration over agentic autonomy. His ranking of models by
conversational ease of use:

1. Opus 4.6 (most balanced in detail and ease of interpretation)
2. Sonnet 5 / Opus 4.8 (does not require interpreter but not always easy)
3. Opus 4.7 (mostly requires interpreter)
4. Fable 5 (requires interpreter for proper understanding)

This ranking is why the workflow uses Opus 4.6 as the primary
conversational partner and implementation model, and Fable 5 as a
specialist consultant accessed through the collegial relay pattern
(Tony carries context between models).

Skills should be written clearly and concisely — they will be consumed
by models across the capability spectrum (Sonnet 4.6 through Fable 5).
Dense jargon or complex cross-references make skills harder to use in
the conversational context that matters most.

---

## Design decisions (agreed with Tony)

### The sorting principle

A skill only helps if its trigger fires at the moment of need. The cut
is NOT procedure-vs-judgment — it is "does the moment-of-need announce
itself in the task?"

- Task-triggered guidance (writing hover text → AU convention) extracts
  cleanly — the task itself signals the need.
- Checkpoint guidance that must fire UNPROMPTED (session start, every
  delivery) cannot be a skill — nothing in the request triggers it —
  so it stays resident.

### What stays resident (the constitution)

- **Preamble** — why the protocol exists (unchanged)
- **Part 1: Operational** — modes, triggers, context priority, quick
  decisions (unchanged; this IS the session-start orientation)
- **Part 2: Principles** — core principles, criticality framework,
  anti-patterns, workflow patterns (lightly trimmed)
- **Part 3: REDUCED** — only the (C)-bucket CRITICAL gates that must
  fire unprompted (SHA round trip, uploads-before-project, enumerate
  uploads, verify base, verify execution, check parallel pipelines,
  fetched-vs-recalled, show the envelope) plus ONE-LINE POINTERS to
  skills where appropriate
- **Part 4: Foundation** — the philosophy (unchanged; this is the soul)
- **Part 5: REDUCED** — quotables stay; roles stay; lessons archive
  stays (it IS the philosophy in action)

### What moves out of Part 5

**Version history → LEDGER_CONSOLIDATED.md.** The version history
tells a story but costs ~50 lines. Move it to the ledger, where it
can also record new ideas for the protocol and skills. The last 2-3
entries stay in the protocol as a pointer.

### Skill location

**User profile** (Tony/settings/customize/skills/), not project-level.
These are installed to Tony's account. This means they persist across
the Claude interface and are not tied to the project connector sync.

### Lessons archive

**Stays resident in the protocol.** The lessons are about approach
and philosophy and working agreements. They belong with the
constitution, not in a skill.

### Quotables

**Stay resident.** They're the partnership's voice, ~30 lines.

### Sensitive content

Food insecurity discipline (IPC voice, transcribe-don't-sum) bundles
with the earth-system-pipeline skill, but with explicit special-case
language covering any visualization where human cost is an element.
Heat events, food insecurity, conflict displacement — all carry the
same restraint discipline. This is not a separate skill; it's a
prominent section within the pipeline skill.

---

## Proposed skill architecture (baseline — Fable, improve on this)

Eight skills proposed. This is a starting point, not a constraint.
Fable should consider alternatives: different bundling, additional
skills, skills we haven't thought of, or fewer skills if the triggers
work better that way.

### Group 1: Part 3 extractions

**Skill 1: orrery-coding-conventions**
- Marker symbol convention, single info marker pattern, hover AU
  convention, 3D axis control, credit line convention, module docstring
  standard, barycenter rule
- Trigger: tasks involving markers, hover text, axes, module headers,
  shell geometry, new visual elements

**Skill 2: safe-file-editing**
- Bottom-up editing, Unicode-safe editing (binary mode), file encoding
  (LF/ASCII), platform neutrality, grep -c in && chains
- Trigger: editing existing .py files, sed/grep operations, encoding

**Skill 3: agentic-pre-test** (Bucket B — has resident pointer)
- Full xvfb test protocol, throwaway copy rule, live-dispatch smoke
  test, whole-module exec pattern
- Trigger: before delivering agentic code or after data-content sweeps
- Resident pointer stays in protocol: "Before delivering agentic code,
  load the agentic-pre-test skill"

**Skill 4: horizons-orbital-mechanics**
- Horizons center body rules, JPL binary IDs, reference frame
  diagnostic, encounter resolution, osculating elements, step format
- Trigger: Horizons API queries, orbital mechanics, reference frames

**Skill 5: provenance-discipline**
- Scanner mechanics (lookback window, units, fingerprinting),
  exceptions file, tier system, fetched-vs-recalled procedures,
  citation-as-provenance-claim, clearing findings workflow
- Trigger: running provenance scanner, reviewing audit, adding
  citations, working with constants
- Note: fetched-vs-recalled and show-the-envelope are ALSO in the
  resident (C)-bucket gates. Skill carries detailed procedures;
  protocol carries the one-line principle. No contradiction.

### Group 2: New project workflow skills

**Skill 6: earth-system-pipeline**
- KMZ generation workflow, 3+5 card pattern, data sources/APIs,
  scenario file architecture, ERA5T lag
- **Sensitive content section:** Food insecurity discipline
  (transcribe-don't-sum, IPC voice, phase 1-5 breakdown, ≥20% rule).
  Extends to ALL visualizations where human cost is an element: heat
  events, food insecurity, conflict displacement. Restraint discipline:
  state the basis, do not hand the lay reader a connection we will not
  draw ourselves.
- Trigger: KMZ layers, heat scenarios, food insecurity, coral
  bleaching, Earth System track, ERA5, ERDDAP, IPC data

**Skill 7: gallery-pipeline**
- Studio → JSON converter → index.html flow, _studio_config round-trip,
  source vs export, WYSIWYG preview, _encyclopedia preservation,
  non-destructive hover routing, two-repo coupling
- Trigger: Gallery Studio, json_converter, web gallery, Studio
  configuration, gallery cards

**Skill 8: ledger-and-tooling**
- Ledger block format, metadata syntax, ledger_index.py, RICE scoring,
  Tony comment convention, ID + status conventions, module_atlas.py,
  dep_trace.py
- Trigger: updating ledger, creating items, running ledger_index.py,
  module atlas, dependency tracing

### Placeholder (not yet)

**Encounter building patterns** — the workflow is still evolving
(L-046 open). Create the skill after L-046 lands and the encounter
pipeline stabilizes.

---

## What Fable 5 receives for the design session

1. **This pre-design** (the brief)
2. **The full protocol v3.29** (807 lines — the source material)
3. **The skill-creator SKILL.md** (platform mechanics and constraints)
4. **MODULE_ATLAS.md** (for trigger accuracy — knows what modules exist
   and what they do)

## What Fable 5 produces

1. **Feedback on this pre-design** — before building anything
2. **The actual SKILL.md files** (8 or however many the final design
   calls for) with YAML frontmatter, trigger descriptions, and body
3. **The trimmed protocol** (everything that stays resident, ready to
   replace v3.29 as the project instructions)
4. **A mapping table** — "this protocol line → this skill, line N" so
   nothing gets lost in the extraction
5. **Any novel ideas** — skills we haven't thought of, structural
   improvements, workflow suggestions that leverage Fable's view of
   the whole system

---

## Proposed workflow

| Step | Who | What | Output |
|------|-----|------|--------|
| 1 | Opus 4.6 + Tony | Pre-design | This document (done) |
| 2 | Opus 4.6 + Tony | Refine, resolve questions | Updated pre-design (done) |
| 3 | Opus 4.6 | Write Fable 5 prompt from refined design | Manifest/prompt |
| 4 | Tony → Fable 5 | Fable reviews, gives feedback, then designs | Skill drafts + trimmed protocol |
| 5 | Opus 4.6 + Tony | Implement: install skills, test triggers | Working skills |
| 6 | Tony → Fable 5 | Review final product for gaps/triggers | Review notes |
| 7 | Opus 4.6 + Tony | Implement review fixes | Final skills |

**Timeline constraint:** Fable 5 available under Max subscription
until July 7. Steps 4 and 6 are the Fable touches and must happen
before that date.
