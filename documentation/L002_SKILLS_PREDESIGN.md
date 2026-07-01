# L-002 Pre-Design: Protocol → Skills Refactor

Tony Quintanilla, PE | Claude Opus 4.6 | July 1, 2026
Status: PRE-DESIGN for Tony review → Fable 5 design session

---

## What this document is

A pre-design brief for L-002 (Protocol → Skills refactor). Tony and
Claude Opus 4.6 refine this in conversation; it then becomes the input
prompt for a Fable 5 design session. Fable produces the actual skill
files; Opus 4.6 implements and Tony reviews.

---

## The problem

The project instructions (v3.29, 807 lines) carry everything: philosophy,
operational modes, coding conventions, pipeline recipes, tool mechanics,
lessons, quotables. Every session loads all of it. Most of it is irrelevant
to any given task -- the provenance scanner mechanics don't help when
building a KMZ; the Gallery pipeline doesn't help when editing hover text.

The Anthropic skills system solves this: skills load on demand when their
trigger description matches the task. The protocol becomes leaner (the
constitution), and task-specific knowledge loads only when needed.

## The opportunity (Tony's broader vision)

The original L-002 scope was "extract Part 3 conventions into skills."
Tony's broader vision: skills as an extensible layer for the whole
project's accumulated knowledge -- not just coding conventions but
Earth System workflows, Gallery pipeline recipes, provenance procedures,
ledger management. Knowledge that currently lives in handoffs, memory,
and conversation history, re-established every session.

## Design principles

**The sorting principle (from the ledger block):** A skill only helps if
its trigger fires at the moment of need. The cut is NOT procedure-vs-
judgment -- it is "does the moment-of-need announce itself in the task?"

- Task-triggered guidance (writing hover text → AU convention) extracts
  cleanly.
- Checkpoint guidance that must fire UNPROMPTED (session start, every
  delivery) cannot be a skill -- nothing in the request triggers it --
  so it stays resident.

**The constitution stays.** Parts 1 (Operational), 2 (Principles), and
4 (Foundation) are the partnership's DNA. They stay resident. They inform
judgment on every turn, not just specific tasks.

**Skills are model-invariant.** The content doesn't change for different
models. What changes is the economics of carrying content resident vs.
on-demand. A 1M-context model could carry more resident, but skills
still help by keeping the protocol lean and the task-specific knowledge
organized.

---

## Architecture

### Layer 1: The Trimmed Protocol (always resident, ~350-400 lines)

What stays:

- **Preamble** -- why the protocol exists (unchanged)
- **Part 1: Operational** -- modes, triggers, context priority, quick
  decisions (unchanged; this IS the session-start orientation)
- **Part 2: Principles** -- core principles, criticality framework,
  anti-patterns, workflow patterns (lightly trimmed; iterative design
  planning stays)
- **Part 3: REDUCED** -- only the (C)-bucket CRITICAL gates that must
  fire unprompted:
  - SHA round trip
  - Uploads before project files
  - Enumerate uploads before claiming a review
  - Verify base against handoff
  - Verify execution, not appearance
  - Check all parallel pipelines
  - Fetched vs recalled
  - Show the envelope of the unknowable
  - Plus ONE-LINE POINTERS to each skill ("Before delivering agentic
    code, load the agentic-pre-test skill")
- **Part 4: Foundation** -- the philosophy (unchanged; this is the soul)
- **Part 5: REDUCED** -- quotables stay (they're the partnership's
  voice); roles stay; version history trimmed to latest 3-4 entries;
  lessons archive moves to a skill

What leaves: every task-triggered convention, procedure, and pipeline
recipe currently in Part 3. All technical reference that has a natural
task trigger.

**Target: ~350-400 lines.** Down from 807. Enough room saved to matter
in a 200K context window; not so aggressive that judgment-layer content
gets lost.

### Layer 2: Skills (load on demand, ~100-300 lines each)

Eight proposed skills, in two groups:

#### Group 1: Part 3 extractions (existing content, reorganized)

**Skill 1: orrery-coding-conventions**
Content:
- Marker symbol convention (table + rules)
- Single info marker pattern (code example + position rules)
- Hover text AU convention (conversion factor + examples)
- 3D axis control convention (dtick + range for both GUI and Studio)
- Credit line convention (template + placement rules)
- Module docstring standard (template + tooling reference)
- Barycenter rule (mass ratio gatekeeper)

Trigger description: "Conventions for writing or modifying visualization
code in the Paloma's Orrery project. Use whenever the task involves
markers, hover text, axis formatting, module headers, shell geometry,
or adding new visual elements to any orrery module. Also use when
creating new Python modules for the project."

Estimated size: ~150 lines

---

**Skill 2: safe-file-editing**
Content:
- Bottom-up editing (highest line numbers first)
- Unicode-safe editing (Python binary mode patterns)
- File encoding (LF line endings, ASCII only, grep check)
- Platform neutrality (SystemButtonFace, pathlib, encoding)
- grep -c in && chains (exits non-zero on zero count)

Trigger description: "Safe editing practices for Python files in
Paloma's Orrery. Use whenever editing existing .py files, especially
palomas_orrery.py or files with Unicode content. Also use for any
sed or grep operations on project files, or when checking line endings
and encoding."

Estimated size: ~100 lines

---

**Skill 3: agentic-pre-test**
Content:
- Full xvfb test protocol (setup + commands)
- THROWAWAY copy rule (sed round trip is NOT idempotent)
- Live-dispatch smoke test for data-content sweeps
- Whole-module exec pattern (tk mainloop suppressed)

Trigger description: "Pre-delivery testing protocol for Paloma's
Orrery agentic code. Use before delivering any complete file or
agentic code change. Also use when a sweep changes output DATA
(hover strings, legendgroup wiring, marker styling) rather than
control flow. CRITICAL: always load this skill before running
xvfb or py_compile tests on project code."

Resident pointer (stays in protocol Part 3):
"Before delivering agentic code, load the agentic-pre-test skill."

Estimated size: ~80 lines

---

**Skill 4: horizons-orbital-mechanics**
Content:
- Horizons center body rules (numeric IDs only, helio_id vs center_id)
- JPL binary IDs (20XXXXXX barycenter, 920XXXXXX primary, etc.)
- Reference frame diagnostic (inclination reveals coordinate system)
- Encounter resolution (cube scale, curvature scale)
- Osculating elements (must match viewing center)
- Horizons step format ({number}{unit})

Trigger description: "JPL Horizons API patterns and orbital mechanics
for Paloma's Orrery. Use whenever fetching data from Horizons, setting
up orbital queries, debugging reference frame issues, or working with
encounter/flyby scenarios. Also use when inclination values or coordinate
centers seem wrong."

Estimated size: ~120 lines

---

**Skill 5: provenance-discipline**
Content:
- Scanner mechanics (lookback window, unit types, fingerprinting)
- Exceptions file format and usage
- Tier system (1-4, score = V x C)
- Fetched-vs-recalled three outcomes (cite / remove-and-note / never cite-to-clear)
- Citation as provenance claim (must be TRUE)
- Show the envelope of the unknowable (companion rule)
- Clearing a finding: source-then-cite workflow

Trigger description: "Provenance scanning and citation discipline for
Paloma's Orrery. Use when running provenance_scanner.py, reviewing
PROVENANCE_AUDIT.md findings, adding # Source citations, clearing
flagged claims, or working with constants and hardcoded values. Also
use when the task involves factual claims, numeric constants, or data
attribution in any project file."

Estimated size: ~150 lines

Note: Fetched-vs-recalled and Show-the-envelope are ALSO in the
(C)-bucket resident gates. The skill carries the detailed procedures;
the protocol carries the one-line principle. No contradiction -- the
skill expands what the pointer compresses.

---

#### Group 2: New project workflow skills (Tony's broader vision)

**Skill 6: earth-system-pipeline**
Content:
- KMZ generation workflow (teaser HTML + KMZ, scenario_id, build stamps)
- 3+5 card pattern (compact header + tappable i-pin balloon)
- Data sources and APIs (ERA5/CDS, ERDDAP, IPC/HDX, Open-Meteo)
- Food insecurity discipline:
  - Transcribe-don't-sum (national totals are transcribed constants)
  - Full phase 1-5 breakdown mandatory (hidden Catastrophe problem)
  - >=20% rule stated on legend
  - IPC attribution voice (never upgrade IPC's framing)
- Scenario file architecture (controller glob, earth_system_common)
- ERA5T lag (~5 days from Copernicus CDS)

Trigger description: "Earth System visualization pipeline for Paloma's
Orrery. Use when building, modifying, or debugging KMZ layers, heat
wave scenarios, food insecurity maps, coral bleaching scenarios, or any
Earth System track work. Also use when working with ERA5 data, ERDDAP
queries, IPC food security data, or the earth_system_controller. Always
use for any task mentioning KMZ, Google Earth layers, or climate
scenarios in this project."

Estimated size: ~200 lines
Bundled reference (optional): data source URLs and API patterns

---

**Skill 7: gallery-pipeline**
Content:
- Studio → JSON converter → index.html flow
- _studio_config round-trip pattern
- Source vs export distinction
- WYSIWYG preview architecture (?preview= branch)
- _encyclopedia key in preserve list
- Non-destructive hover routing (_original_text stash)
- Two-repo coupling (orrery repo + gallery Pages repo)
- Gallery card / featured trace conventions

Trigger description: "Gallery Studio and web gallery pipeline for
Paloma's Orrery. Use when working with gallery_studio.py,
json_converter.py, index.html, or any gallery export/import workflow.
Also use when the task involves Studio configuration, gallery cards,
featured traces, the WYSIWYG preview, or the tonyquintanilla.github.io
repository."

Estimated size: ~180 lines

---

**Skill 8: ledger-and-tooling**
Content:
- Ledger block format (header, metadata, narrative, Gap, Ref)
- Metadata line syntax (L:NNN status: upd: section: flag: rice:)
- ledger_index.py usage (regenerate, --check, default path)
- RICE scoring system (R/I/C/E dimensions, score formula)
- Tony comment convention (**Tony:** blocks, **Note:** blocks)
- ID + status conventions (append-only handles, dispositions, evidence tags)
- Module Atlas tooling (module_atlas.py, MODULE_ATLAS.md)
- dep_trace.py usage

Trigger description: "Project management tooling for Paloma's Orrery.
Use when updating LEDGER_CONSOLIDATED.md, creating new ledger items,
running ledger_index.py, or working with the RICE scoring system. Also
use when running module_atlas.py, dep_trace.py, or when the task
involves dependency tracing, module classification, or project
documentation tooling."

Estimated size: ~150 lines

---

### Layer 3: Lessons Archive (bundled reference, loaded rarely)

The lessons archive (Technical, Process, Philosophical) is valuable
but rarely needed mid-task. Options:

- **Option A:** Bundle as a reference file inside the most relevant
  skill (e.g., technical lessons → safe-file-editing/references/)
- **Option B:** Standalone skill "project-lessons" that loads only
  when explicitly asked or when debugging a recurring pattern
- **Option C:** Keep in the trimmed protocol (costs ~100 lines of
  resident context)

Recommendation: **Option B** -- standalone, loads on explicit request
or when a failure pattern matches a known lesson.

---

## What this buys

| Metric | Before | After |
|--------|--------|-------|
| Resident protocol | ~807 lines | ~350-400 lines |
| Task-specific content | always loaded | loads on demand |
| Pipeline knowledge | in handoffs/memory | structured, versioned |
| Extensibility | edit 807-line file | add/edit individual skills |
| New workflow (e.g. stars) | re-explain every session | write a skill once |

---

## Open design questions for Tony

1. **Bundling granularity.** 8 skills feels right. Fewer = loading
   irrelevant content (AU convention when you're doing KMZ work).
   More = trigger confusion (which of 15 skills fires?). Agree?

2. **Lessons archive disposition.** Option A (bundle into skills),
   B (standalone skill), or C (keep resident)?

3. **Version history.** Currently ~50 lines in Part 5. Trim to last
   3-4 versions in the protocol, or move entirely to a reference file?

4. **Skill location.** Project-level (auto-syncs via repo connector)
   or user profile (persists across projects)? Project-level seems
   right since these are Paloma's Orrery specific.

5. **Quotables.** They're the partnership's voice, ~30 lines. Keep
   resident in the trimmed protocol, or move to a skill? I'd keep
   them -- they're short and they matter.

6. **Which workflows are stable enough to encode as skills?** Earth
   System and Gallery pipelines are mature. Encounter building is
   still evolving (L-046 open). Should we write a skill for it now
   or wait until L-046 lands?

7. **Sensitive content skills.** The food insecurity discipline
   (IPC voice, transcribe-don't-sum) is in the earth-system-pipeline
   skill. Should it be a separate skill with its own trigger, given
   the restraint-discipline principle? Or is bundling it with the
   pipeline sufficient?

---

## Proposed workflow

| Step | Who | What | Output |
|------|-----|------|--------|
| 1 | Opus 4.6 + Tony | Pre-design (this document) | This file |
| 2 | Opus 4.6 + Tony | Refine, resolve open questions | Updated pre-design |
| 3 | Opus 4.6 | Write Fable 5 prompt from refined design | Manifest/prompt |
| 4 | Tony → Fable 5 | Fable designs: writes all SKILL.md files + trimmed protocol | Skill drafts |
| 5 | Opus 4.6 + Tony | Implement: install skills, test triggers, adjust | Working skills |
| 6 | Tony → Fable 5 | Review: Fable audits final product for gaps/triggers | Review notes |
| 7 | Opus 4.6 + Tony | Implement review fixes | Final skills |

---

## What Fable 5 gets asked to do (step 4)

Fable receives:
- This pre-design (refined)
- The full protocol v3.29 (as input to extract from)
- The skill-creator SKILL.md (platform mechanics)
- Module Atlas (for trigger accuracy -- knows what modules exist)

Fable produces:
- 8 SKILL.md files with YAML frontmatter and body
- The trimmed protocol (everything that stays resident)
- A mapping table: "this protocol line → this skill, line N"
- Any gaps it finds (content that doesn't fit either layer)

This is the kind of long-horizon, thorough, self-checking work
where Fable's lead over other models grows.
