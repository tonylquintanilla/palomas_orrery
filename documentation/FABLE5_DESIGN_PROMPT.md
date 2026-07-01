# Design Consultation: Protocol → Skills Refactor for Paloma's Orrery

## Who I am

I'm Tony Quintanilla, PE — a retired engineer, artist, and sole developer of
Paloma's Orrery (palomasorrery.com), a Python/Plotly climate and solar system
visualization suite (~115 modules, ~86K lines). I've been building this project
conversationally with Claude (primarily Opus 4.6 and Sonnet 4.6/5) for nine
months. I also work with Gemini for domain validation. I describe myself as a
"vibe coder" — learning through building, following curiosity.

## What I'm asking you to do

I'm consulting you as a senior software engineer on an architectural refactoring
problem. My primary Claude partner (Opus 4.6) and I have produced a pre-design
for extracting task-specific knowledge from our 807-line project protocol into
Anthropic SKILL.md files. I want your expert review, feedback, and then — once
we've discussed — your design and implementation.

This is a collegial conversation. Push back where the pre-design is wrong.
Suggest ideas we haven't thought of. Propose novel solutions. You are not
following instructions — you are thinking with me.

## How this relay works

I work conversationally with Opus 4.6 as my primary partner. You are being
consulted through a collegial relay — I carry context between models. Opus 4.6
wrote this prompt and will implement your design. Your role is the deep
architectural thinking and production of the skill files. I'm the integrator.

My model ease-of-use ranking (conversational, not intelligence):
1. Opus 4.6 (most balanced — my daily partner)
2. Sonnet 5 / Opus 4.8 (clear but not always easy)
3. Opus 4.7 (mostly requires interpretation)
4. Fable 5 (requires interpretation — but worth it for depth)

This ranking is why you're being consulted, not used as the daily driver. Your
depth of reasoning justifies the interpretation cost for architectural work
like this. Don't constrain your style on my account — it's my job and Opus
4.6's job to interpret your output.

## Source files to read

The project repo is public: https://github.com/tonylquintanilla/palomas_orrery
Current HEAD SHA: please verify with `git ls-remote` or the repo page.

**Please fetch and read these files before responding:**

1. **project_instructions_v3_29.md** — the full 807-line protocol. This is
   the source material you'll be extracting from.
   `https://raw.githubusercontent.com/tonylquintanilla/palomas_orrery/main/project_instructions_v3_29.md`

2. **MODULE_ATLAS.md** — complete module inventory with role classifications,
   function listings, and dependency graph. Essential for writing accurate
   trigger descriptions.
   `https://raw.githubusercontent.com/tonylquintanilla/palomas_orrery/main/MODULE_ATLAS.md`

3. **LEDGER_CONSOLIDATED.md** — the project backlog. L-002 is this item.
   Read at least the L-002 detail block for context on what's been discussed.
   `https://raw.githubusercontent.com/tonylquintanilla/palomas_orrery/main/LEDGER_CONSOLIDATED.md`

## Skill platform mechanics

Skills use YAML frontmatter with `name` and `description` fields. The
`description` is the trigger — it's what causes the skill to load when a task
matches. Skills should be under 500 lines. They can bundle reference files in
subdirectories (references/, scripts/, assets/) for progressive disclosure.

The description should be somewhat "pushy" — err on over-triggering rather
than under-triggering, because the platform tends to under-trigger skills.
But these skills will be installed at account level (not project level), so
triggers must be specific enough not to fire on unrelated conversations.

YAML frontmatter format:
```yaml
---
name: skill-name
description: When to trigger. Be specific but inclusive. Include both what the skill does AND contexts for when to use it.
---
```

## The pre-design brief

What follows is the pre-design produced by Opus 4.6 and me. Read it as a
starting point, not a constraint.

---

### The problem

The project protocol (v3.29, 807 lines) carries everything: philosophy,
operational modes, coding conventions, pipeline recipes, tool mechanics,
lessons, quotables. Every session loads all of it. Most of it is irrelevant
to any given task.

### The opportunity

Skills load on demand when their trigger matches the task. The protocol
becomes leaner (the constitution), and task-specific knowledge loads only
when needed. But the vision goes further: skills as an extensible layer for
the whole project's accumulated knowledge — not just coding conventions but
Earth System workflows, Gallery pipeline recipes, provenance procedures,
ledger management. Knowledge that currently lives in handoffs and memory,
re-established every session.

### The sorting principle

A skill only helps if its trigger fires at the moment of need. The cut is
NOT procedure-vs-judgment — it is "does the moment-of-need announce itself
in the task?"

- Task-triggered guidance (writing hover text → AU convention) extracts
  cleanly — the task itself signals the need.
- Checkpoint guidance that must fire UNPROMPTED (session start, every
  delivery) cannot be a skill — nothing in the request triggers it — so
  it stays resident.

### What stays resident (the constitution)

- **Preamble** — why the protocol exists (unchanged)
- **Part 1: Operational** — modes, triggers, context priority, quick
  decisions (unchanged; this IS the session-start orientation)
- **Part 2: Principles** — core principles, criticality framework,
  anti-patterns, workflow patterns (lightly trimmed)
- **Part 3: REDUCED** — only the (C)-bucket CRITICAL gates that must fire
  unprompted: SHA round trip, uploads-before-project, enumerate uploads,
  verify base, verify execution, check parallel pipelines, fetched-vs-
  recalled, show the envelope. Plus ONE-LINE POINTERS to skills.
- **Part 4: Foundation** — the philosophy (unchanged; this is the soul)
- **Part 5: REDUCED** — quotables stay; roles stay; lessons archive stays
  (it IS the philosophy in action)

### What moves out of Part 5

**Version history → LEDGER_CONSOLIDATED.md.** The version history tells a
story but costs ~50 lines of resident context. Move it to the ledger. Keep
the last 2-3 entries in the protocol as a pointer.

### Agreed design decisions

- **Lessons archive: stays resident.** It's about approach and philosophy.
- **Quotables: stay resident.** They're the partnership's voice.
- **Skill location: user profile** (account settings/customize/skills/),
  not project-level. Persists across the interface. Trigger descriptions
  must be project-specific enough not to fire on unrelated conversations.
- **Sensitive content: bundled, not separate.** Food insecurity discipline
  (IPC voice, transcribe-don't-sum) bundles with the earth-system-pipeline
  skill, with explicit language covering ANY visualization where human cost
  is an element — heat events, food insecurity, conflict displacement.
- **Encounter building: placeholder, wait.** Workflow still evolving
  (L-046 open). Write the skill after it stabilizes.
- **Bundling: 8 skills as a baseline, not a constraint.** You have full
  latitude to propose different groupings, additional skills, or fewer
  skills if the triggers work better that way.

### Proposed skills (baseline — improve on this)

#### Group 1: Part 3 extractions

**1. orrery-coding-conventions** — marker symbols, single info marker
pattern, hover AU, 3D axis control, credit lines, module docstrings,
barycenter rule. Trigger: markers, hover text, axes, module headers, shells.

**2. safe-file-editing** — bottom-up editing, binary mode, LF/ASCII
encoding, platform neutrality, grep -c gotcha. Trigger: editing .py files,
sed/grep operations, encoding checks.

**3. agentic-pre-test** (has resident pointer) — xvfb protocol, throwaway
copy rule, live-dispatch smoke test, whole-module exec. Trigger: before
delivering agentic code, after data-content sweeps.

**4. horizons-orbital-mechanics** — center body rules, JPL binary IDs,
reference frames, encounter resolution, osculating elements. Trigger:
Horizons API, orbital queries, reference frame issues.

**5. provenance-discipline** — scanner mechanics, exceptions file, tier
system, fetched-vs-recalled procedures, citation-as-provenance-claim.
Trigger: running scanner, reviewing audit, adding citations, working with
constants. (Note: fetched-vs-recalled is ALSO a resident (C)-gate. Skill
carries the procedures; protocol carries the principle.)

#### Group 2: New project workflow skills

**6. earth-system-pipeline** — KMZ workflow, 3+5 card pattern, data
sources, scenario architecture, ERA5T lag. INCLUDES sensitive content
section: food insecurity discipline + any visualization where human cost
is an element. Trigger: KMZ, heat scenarios, food insecurity, coral
bleaching, ERA5, ERDDAP, IPC data.

**7. gallery-pipeline** — Studio → JSON → index.html, _studio_config
round-trip, source vs export, WYSIWYG preview, _encyclopedia preservation,
two-repo coupling. Trigger: Gallery Studio, json_converter, web gallery,
gallery cards.

**8. ledger-and-tooling** — block format, metadata syntax, ledger_index.py,
RICE scoring, module_atlas.py, dep_trace.py. Trigger: updating ledger,
creating items, module atlas, dependency tracing.

---

## What I need from you

**Phase 1 — Feedback (do this first, before building anything):**
- What works in this pre-design? What doesn't?
- What have we missed? What would you restructure?
- Are the trigger descriptions well-targeted? Would any collide or
  leave gaps?
- Are there skills we haven't thought of that the codebase needs?
- Any novel architectural ideas that leverage your view of the whole
  system?

**Phase 2 — Design and build (after I've responded to your feedback):**
- The actual SKILL.md files with YAML frontmatter and body
- The trimmed protocol (everything that stays resident, ready to become
  project_instructions_v3_30.md)
- A mapping table: "this protocol section/line → this skill" so we can
  verify nothing was lost in the extraction
- Any additional recommendations

Please start with Phase 1. I'll respond to your feedback before we
proceed to Phase 2. This is a conversation, not a one-shot delivery.
