# Fable Audit Prompt: Skills Layer Review

**Built on `339897000b63fa768ccb9b556dd432bac4f9d4eb`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Verify HEAD matches before starting; if it does not, trace the delta
before trusting any line number in this prompt.**

**Prepared:** August 5, 2026 by Claude Opus 5 (orchestration) | Tony Quintanilla, integrator

---

## Who you are working for

Tony Quintanilla, PE -- a retired civil and environmental engineer, artist,
and anthropologist. He is not a professional programmer and not a formally
trained astronomer. He builds Paloma's Orrery through conversational AI
collaboration ("vibe coding") and holds sole commit authority and final
judgment. The codebase's structure and discipline are the product of
iterative collaboration with Claude, not something Tony wrote unassisted.
Read code quality as evidence of the partnership, not of Tony's independent
programming skill.

What Tony owns and drives personally is the workflow: the protocol, master
planning, design handoffs, build oversight, the ledger, and the
inter-model relay that this prompt is part of. Mechanism-level novice
status (he uses GitHub Desktop, never the git command line, and runs
Python via the VS Code Run button) is not the same as passive. He directs
the process and makes every integration call.

**Practical consequence for your output:** unpack jargon on first use, and
frame any recommendation in terms of what it would change in a file, not
in terms of an abstraction he would have to translate.

## What the skills layer is

Since protocol v3.30 (July 2026) this project runs a **two-layer
instruction system**:

- **Layer 1, the resident protocol** (`documentation/project_instructions_*.md`,
  currently v3.33). Loaded every session. Carries judgment, the seven
  working modes, and the `[CRITICAL]` checkpoint gates that must fire
  unprompted.
- **Layer 2, the skills** (`skills/<name>/SKILL.md`). Ten files, loaded
  on demand when their subject matter comes up. Carries task-specific
  procedures and conventions, tiered `[QUALITY]` and `[PRACTICE]`.

Skills are versioned and SHA-stamped like code. `skills_index.py` scans
every `skills/*/SKILL.md` and regenerates the "Skill Manifest" table
inside the protocol between `SKILL-MANIFEST:START` / `END` markers -- the
SKILL.md files are the single source of truth; the table is a generated
mirror. The ledger (`LEDGER_CONSOLIDATED.md`) is the change log.

The manifest table doubles as an **under-trigger backstop**: if a skill is
relevant and has not fired, the protocol instructs Claude to load it by
name from that table.

## Your role

Fable: large-context comprehensive audit. You are being asked for the
architectural view of the whole skills layer at once -- the thing a
bounded per-skill session structurally cannot see.

This is a **review for improvements and gaps**, not a rewrite. Three jobs.

---

### Job 1: Coverage gaps -- what work has no owning skill?

The project is ~117 Python modules across several subject-matter domains.
Ten skills exist. Find the work that falls between them.

For each gap, state: what the work is, which modules it lives in, what a
session doing that work would currently have to reconstruct from scratch,
and whether it warrants a new skill, a section inside an existing skill,
or nothing at all ("no skill needed" is a legitimate finding -- the layer
should not grow for its own sake).

**One gap is already confirmed and seeded for you** (do not spend effort
rediscovering it; do assess its shape): the **stars / stellar
neighbourhood domain** has no owning skill. Eighteen modules --
`star_visualization_gui.py`, `star_properties.py`, `star_notes.py`,
`star_sphere_builder.py`, `stellar_parameters.py`, `stellar_data_patches.py`,
`hr_diagram_apparent_magnitude.py`, `hr_diagram_distance.py`,
`planetarium_apparent_magnitude.py`, `planetarium_distance.py`,
`messier_catalog.py`, `messier_object_data_handler.py`,
`exoplanet_coordinates.py`, `exoplanet_orbits.py`,
`exoplanet_stellar_properties.py`, `exoplanet_systems.py`,
`catalog_selection.py`, `sgr_a_star_data.py` -- are covered by no skill.
`orrery-coding-conventions` names `star_visualization_gui` in its
description but carries no star-specific convention. Meanwhile
`provenance-discipline` defines a `stars` domain for report
classification, so the project's own taxonomy already recognises the
area. Assess whether this warrants a skill and what it would contain.

Look for others. Candidate areas worth probing (not a closed list):
data caching and the various cache managers; the Tk GUI layer itself;
testing and diagnostics tooling; anything in the repo root that no skill
description mentions.

---

### Job 2: Per-skill quality audit

For each of the ten skills, read it against the codebase at HEAD and
report findings. What to look for:

1. **Stale or wrong assertions.** A skill that names a file, line, function,
   value, or behaviour that no longer matches HEAD. Skills are SHA-stamped
   at cut time and the code has moved since; several stamps are from July
   12. **Verify against the code, do not assume.**

2. **Aspirational statements written as descriptive ones.** A convention
   phrased as "the project does X" when the codebase only does X in some
   places. This is live and load-bearing: the
   just-installed `orrery-coding-conventions` v1.2 was drafted carrying
   "perihelion is the project convention for all bodies" for Hill spheres, which measurement
   showed is false at HEAD (3 bodies perihelion, 4 semi-major, 1 aphelion,
   1 matching nothing). It was rewritten as intent-plus-measured-state
   with an explicit "do not correct a body on the strength of this section
   alone." **Assess whether that pattern is right, and whether other
   conventions in other skills have the same unmarked aspirational
   problem.** A skill that overstates uniformity will cause a future
   session to "fix" correct code.

3. **Internal contradictions**, within a skill or against the resident
   protocol. The protocol wins; flag the skill.

4. **Tier misassignment.** `[CRITICAL]` / `[QUALITY]` / `[PRACTICE]` are
   defined in the protocol, Part 2. The critical tier must stay short --
   "if everything is critical, nothing is." Flag anything tiered too high
   or too low, with the failure that would justify the change.

5. **Register.** The protocol's Register Rule distinguishes reference
   voice (compressed, for a reader who already owns the idea) from
   explanation voice (one claim per sentence, gloss terms on first use).
   Skills are reference documents read by a model that resets every
   session and by Tony, who does not re-read. Flag passages that fail the
   test "can Tony act on this without a follow-up question."

6. **Length and balance.** The skills range from 89 lines
   (`horizons-orbital-mechanics`) to 469 (`provenance-discipline`); the two
   just-revised skills grew by 93% and 35% in one round. Flag skills that look under-built for their subject, and skills
   that have grown to the point where the important thing is hard to find.
   Note: length is not itself a defect -- say what is actually wrong.

7. **Field notes.** Most skills end with a field-notes section of earned
   lessons. Flag notes that have been superseded, that duplicate a note in
   another skill, or that state a lesson without the observation that
   earned it.

---

### Job 3: Cross-skill coherence and the two-layer boundary

The layer has to work as a system, not ten documents.

1. **Trigger reliability.** Each skill has a `description` and a
   `fires_when` field; both feed the decision to load it. Look for
   **overlap** (two skills that would both fire on the same request, with
   no statement of which governs) and **under-firing** (work that plainly
   needs a skill whose trigger language would not catch it). All ten
   currently have complete frontmatter -- the question is whether the
   wording actually discriminates.

2. **Duplication.** Where the same convention appears in more than one
   skill, is there a declared master? The hover-text AU convention does
   this correctly today: `orrery-coding-conventions` holds the master and
   says so, `gallery-pipeline` points back to it, `earth-system-pipeline`
   restates it. **That one is verified correct -- do not report it as a
   finding.** Look for duplication that does *not* follow that pattern.

3. **The cross-reference graph.** Skills point at each other. Verify each
   pointer is accurate and that the target still says what the pointer
   claims. The current graph (also seeded, do not re-derive):

   | Skill | Points to |
   |---|---|
   | agentic-pre-test | gallery-cache-builder, orrery-coding-conventions, safe-file-editing |
   | earth-system-pipeline | orrery-coding-conventions, provenance-discipline, safe-file-editing |
   | gallery-assembler | gallery-cache-builder, gallery-pipeline |
   | gallery-cache-builder | gallery-pipeline, horizons-orbital-mechanics |
   | gallery-pipeline | earth-system-pipeline, gallery-cache-builder, orrery-coding-conventions, safe-file-editing |
   | horizons-orbital-mechanics | orrery-coding-conventions |
   | orrery-coding-conventions | horizons-orbital-mechanics |
   | provenance-discipline | earth-system-pipeline |
   | safe-file-editing | agentic-pre-test |

   Note the asymmetries -- e.g. nothing points *to* `ledger-and-session-records`.
   Assess whether that is a real gap or correct.

4. **The layer boundary.** Is anything sitting in a skill that should be a
   resident `[CRITICAL]` gate, because a session that never loads that
   skill would miss it? And conversely, is anything in the resident
   protocol that has become task-specific enough to move down? The
   boundary is the design premise of v3.30; report on whether it still
   holds after a year of accretion.

5. **Versioning and manifest mechanics.** The manifest table is generated
   by `skills_index.py`, so drift means the tool was not re-run after a
   version bump. Assess whether the version-history-inside-the-skill
   convention (each skill opens with a paragraph narrating v1.1, v1.2,
   v1.3...) is still serving, or whether it has become preamble the reader
   scrolls past to reach the content.

---

## Version state at this anchor

Clean. Both revised skills are installed at `skills/<name>/SKILL.md` and
are the copies to review:

- `orrery-coding-conventions` **v1.2** (343 lines)
- `provenance-discipline` **v1.6** (469 lines)

The Skill Manifest table in the protocol was regenerated by
`skills_index.py` at this anchor and now matches the repo for all ten
skills -- verified. **Do not report manifest drift as a current finding.**

Two mechanics observations are seeded for Job 3 item 5. Neither is a live
defect right now; both are about what the layer depends on to stay
correct.

**(a) The manifest drifted for roughly three weeks before anyone ran the
tool.** `skills_index.py` regenerates the manifest from the SKILL.md
files, and it works -- but it runs only when someone remembers. Before it
was run at this anchor, the table advertised `orrery-coding-conventions`
1.1 against an actual 1.2, and `provenance-discipline` 1.4 against an
actual 1.6 -- the latter already two bumps behind, having gone stale at
1.5 well before this round.

Why that matters beyond tidiness: the protocol instructs a session that
finds a skill-version mismatch to reconcile before trusting the skill,
same rule as a SHA mismatch. A stale manifest therefore fires that alarm
on every session that loads the affected skill, and an alarm that is
always wrong is one the reader learns to wave off -- which is exactly the
state in which a *real* mismatch stops registering. The question for you
is whether regeneration belongs at a checkpoint (a push gate, a session-
close step, a ledger action) rather than depending on memory, and if so,
where it would sit without adding ceremony the project will not keep up.

**(b) Skills and the protocol each exist in more than one place.** All
copies are byte-identical at this anchor -- verified -- so nothing is
wrong today. But the two cases differ in an instructive way:

- **Tool-synced (fine):** the protocol lives at both
  `PROJECT_INSTRUCTIONS.md` and
  `documentation/project_instructions_v3_33.md`. `skills_index.py`
  rewrites the manifest zone in both, so they cannot silently diverge on
  the thing the tool owns. Do not report this as a defect.
- **Unmanaged (the actual question):**
  `documentation/orrery-coding-conventions_SKILL.md` and
  `documentation/provenance-discipline_SKILL.md` are staging copies of
  the installed skills, kept in sync by nothing at all. This is precisely
  the failure `provenance-discipline`'s own field notes warn about for
  `PROVENANCE_AUDIT.md` ("multiple copies can exist and silently diverge
  -- verify which one you're reading"), now latent in the skill carrying
  the warning.

Recommend a convention for where in-flight skill revisions live before
installation, and whether the staging copy should be deleted on install
or kept deliberately. The distinction above is the useful lens: a second
copy is safe when a tool owns it and dangerous when a habit does.

---

## Materials

**Primary (the audit targets), all at `skills/<name>/SKILL.md`:**

| Skill | Ver | Lines | Cut at |
|---|---|---:|---|
| agentic-pre-test | 1.1 | 96 | e83fe9ce, 2026-07-12 |
| earth-system-pipeline | 1.1 | 193 | e83fe9ce, 2026-07-12 |
| gallery-assembler | 1.0 | 118 | gallery a7abea59 / orrery e775050d, 2026-07-20 |
| gallery-cache-builder | 1.1 | 159 | github.io a08bdd10 / orrery af58f7f8, 2026-07-12 |
| gallery-pipeline | 1.1 | 160 | github.io 89c8bf30 |
| horizons-orbital-mechanics | 1.1 | 89 | e83fe9ce, 2026-07-12 |
| ledger-and-session-records | 1.4 | 175 | ca9c706e, 2026-07-26 |
| orrery-coding-conventions | **1.2** | 343 | 1e60c783, 2026-08-04 |
| provenance-discipline | **1.6** | 469 | 1e60c783, 2026-08-04 |
| safe-file-editing | 1.1 | 158 | b29ad3f8 |

**Context (read as needed, do not audit):**

- `documentation/project_instructions_v3_33.md` -- the resident protocol,
  Layer 1. Its Part 2 defines the criticality tiers and the Register Rule;
  Part 3 holds the manifest table and the CRITICAL gates.
- `skills_index.py` -- manifest generator and consistency checker.
- `LEDGER_CONSOLIDATED.md` -- change log; the Protocol Version History
  appendix carries the full lessons archive the skills were cut from.
- `documentation/PROMPT_fable_shell_consistency_audit.md` and
  `documentation/FABLE_shell_consistency_audit_report.md` -- your previous
  audit in this project, for format precedent.
- The codebase itself, for verifying that skill assertions match HEAD.

---

## Ground rules

- **Do not rewrite the skills.** Findings and recommendations only. Tony
  and the orchestrating Claude do the edits, as with the shell audit.
- **Do not add conventions of your own invention.** A skill records what
  this project learned, with the observation that earned it. Proposing a
  best practice the project has never used is out of scope -- if you think
  something is missing, say what evidence in the repo suggests it.
- **Verify against HEAD; do not cite from training memory.** If a skill
  asserts a file, line, function, or value, check it. Where you cannot
  verify, mark it UNVERIFIED rather than guessing -- that is a useful
  result, not a failure.
- **"No change needed" is a valid finding** and worth stating explicitly,
  so the next review does not re-litigate it.
- **Distinguish severity.** A wrong file path and an infelicitous sentence
  are not the same finding. Use the severity column.
- **Do not design the fix for anything structural.** Map it and hand it
  over, same as the shell audit's Job 2.

---

## Output format

### Job 1: Coverage gaps

| # | Gap | Modules affected | What a session must currently reconstruct | Recommendation | Severity |
|---|-----|------------------|-------------------------------------------|----------------|----------|

Recommendation is one of: **NEW SKILL** / **SECTION IN <skill>** /
**NO ACTION** (with reasoning).

### Job 2: Per-skill findings

One table per skill; omit skills with no findings, and list those in a
short "clean" list afterwards.

| # | Section / line | Type | Finding | Severity | Suggested direction |
|---|---------------|------|---------|----------|--------------------|

Types: **STALE** (no longer matches HEAD) | **ASPIRATIONAL** (stated as
descriptive, actually partial) | **CONTRADICTION** (internal or vs
protocol) | **TIER** (mis-tiered) | **REGISTER** (unclear/unactionable) |
**BALANCE** (under- or over-built) | **FIELD_NOTE** (superseded,
duplicated, or unearned) | **GOOD** (working well, worth preserving
explicitly under edit pressure).

Severity: **HIGH** (would cause a wrong action) | **MEDIUM** (would cause
confusion or wasted effort) | **LOW** (polish).

### Job 3: Cross-skill and boundary findings

| # | Finding | Skills involved | Type | Severity | Suggested direction |
|---|---------|-----------------|------|----------|--------------------|

Types: **TRIGGER_OVERLAP** | **TRIGGER_GAP** | **DUPLICATION** |
**BROKEN_REFERENCE** | **BOUNDARY** (belongs in the other layer) |
**MECHANICS** (versioning, manifest, install path).

### Closing summary

1. Counts by job, type, and severity.
2. **The three changes that would most improve the layer**, ranked, with
   reasoning. Be opinionated here -- this is the part Tony will act on
   first.
3. **What is working and should not be disturbed.** An audit that only
   reports defects invites edits that break what is already right.
4. **Honest gaps** -- what you could not verify, and why.

---

## Completed pre-work (do not repeat)

Run against HEAD `3398970`:

- Skill inventory with versions, line counts and SHA stamps -- the
  Materials table above.
- Frontmatter completeness: all ten skills carry `name`, `description`,
  and `fires_when`. No missing fields.
- Cross-reference graph -- the Job 3 table above.
- Hover-text AU convention duplication: verified **correct**
  (`orrery-coding-conventions:63` master, `gallery-pipeline:140` points
  back to it, `earth-system-pipeline:171` restates). Not a finding.
- Stars-domain coverage gap: 18 modules, zero skill coverage. Confirmed;
  seeded in Job 1.
- Manifest table: regenerated at this anchor and verified to match the repo
  for all ten skills. Not a current finding; the drift *window* is seeded in
  Version State (a). Older tables in `project_instructions_v3_31.md` and
  `v3_32.md` are archived snapshots -- drift there is expected and is not a
  finding.
- Duplicate copies: protocol (two paths, tool-synced) and staging skill
  copies under `documentation/` (unmanaged). All byte-identical at this
  anchor -- verified. See Version State (b).
- Skill install path: both revised skills are installed in `skills/` and in
  Tony's account profile as of this anchor.

---

*Prompt prepared August 5, 2026 by Claude Opus 5 (orchestration),
built on `339897000b63fa768ccb9b556dd432bac4f9d4eb` at
https://github.com/tonylquintanilla/palomas_orrery*
