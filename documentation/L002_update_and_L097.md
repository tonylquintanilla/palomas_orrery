# L-002 Update + L-097 New Item + Fable Prompt

Built on palomas_orrery @ b1a5616 (July 4, 2026).
Session with Claude Opus 4.6.

---

## 1. L-002 Amended Detail Block

Replace lines 435-469 of LEDGER_CONSOLIDATED.md with this block.
The design narrative is preserved as institutional memory; the Gap line
is replaced with a completion note. Migrate to section C on next
housekeeping pass.

```
#### [L-002] Protocol -> Skills refactor (process/tooling)
<!-- L:002 status:DONE upd:2026-07-04 section:A flag: rice:3/3/50/3 -->
- **Protocol -> Skills refactor (process/tooling, not orrery code).** Lift the
  task-triggered PROCEDURE/CONVENTION layer of Part 3 into Anthropic SKILL.md
  files (load on demand); keep the JUDGMENT layer (modes, criticality,
  anti-patterns, Foundation, double-helix) resident. Sketch-first /
  design-before-build -- the framing below is the leg-up from the v3.29 cleanup,
  NOT the design itself.
- **Sorting principle (the design lever):** a skill only helps if its trigger
  fires at the moment of need. So the cut is NOT QUALITY-vs-CRITICAL and NOT
  procedure-vs-judgment -- it is "does the moment-of-need announce itself in the
  task?" Task-coupled guidance (writing hover text -> AU convention) extracts
  cleanly; checkpoint guidance that must fire UNPROMPTED (session start, every
  delivery) can't be a skill -- nothing in the request triggers it -- so it stays
  resident by standing instruction.
- **Three buckets (v3.29 Part-3 inventory; illustrative, not the final set):**
  (A) EXTRACT -- task-triggered conventions/procedures: docstring standard,
      single-info-marker, marker-symbol, hover-AU, 3D-axis, Horizons centers,
      provenance-scanner mechanics, a safe-editing bundle (bottom-up + binary-mode
      + file-encoding), platform-neutrality, credit-line, barycenter.
  (B) RESIDENT POINTER + skill body -- CRITICAL but task-coupled: Agentic Pre-Test
      (a resident one-liner fires it; the commands + live-dispatch smoke test live
      in the skill).
  (C) STAY RESIDENT -- checkpoint CRITICAL gates, never extract: SHA round trip,
      uploads-before-project, enumerate-uploads, verify-base, verify-execution,
      check-parallel-pipelines, fetched-vs-recalled, show-the-envelope; + Parts 1/2/4.
- **COMPLETED July 4, 2026.** Designed with Claude Opus 4.6 (two pre-design
  sessions: L002_SKILLS_PREDESIGN.md, L002_SKILLS_PREDESIGN_v2.md). Built with
  Claude Fable 5 via collegial relay. Tony integrated and deployed.
  Eight skills at v1.0, all cut from palomas_orrery @ b29ad3f8 (gallery-pipeline
  also from tonyquintanilla.github.io @ 89c8bf30):
  orrery-coding-conventions, safe-file-editing, agentic-pre-test,
  horizons-orbital-mechanics, provenance-discipline, earth-system-pipeline,
  gallery-pipeline, ledger-and-session-records.
  Protocol v3.30 installed; version history moved to ledger appendix.
  Extraction audit: documentation/MAPPING_TABLE_L002.md (every v3.29 line mapped;
  deliberate duplication registry for future amendments).
  Reviewed by Opus 4.6 against HEAD @ 33f0b148 before deployment.
  Skills 6-8 are first-time capture (~2/3 of skill content): knowledge that
  previously lived only in handoffs and code.
- **Scanner carve-out (design question, decided):** skills contain numeric claims
  (AU conversion, reference distances) with prose attribution rather than
  # Source: comments. Carve-out: "skills cite by prose; masters live in cited .py
  code." The scanner covers the code; the skills describe conventions whose
  authoritative instances are under scanner coverage. No exceptions entries needed
  unless scanner scope widens to .md files.
- **Follow-on:** skills_index.py devtool (L-097) -- same pattern as
  ledger_index.py; kills manifest-table drift.
**Gap:** none -- move to section C.
**Ref:** documentation/MAPPING_TABLE_L002.md, documentation/LEDGER_version_history_block.md, documentation/README_DEPLOYMENT.md, documentation/README_DEPLOYMENT_v2.md, documentation/L002_SKILLS_PREDESIGN.md, documentation/L002_SKILLS_PREDESIGN_v2.md, skills/*.
```

---

## 2. New Ledger Entry: L-097

Paste after the last detail block in section A (currently after L-078).
Note: L-079 through L-096 are reserved for Section W (web publication
master plan); this item takes the next free handle.

```
#### [L-097] skills_index.py -- Skill Manifest auto-generation (process/tooling)
<!-- L:097 status:OPEN upd:2026-07-04 section:A flag: rice:2/2/80/1 -->
- **Devtool mirroring ledger_index.py:** walk skills/, read each SKILL.md
  frontmatter (name, description) and body version line, regenerate the Skill
  Manifest table in project_instructions_v3_30.md between markers. Kills
  manifest-table drift the same way ledger_index.py killed hand-pasted summary
  rows. Also runs a consistency check: every skill directory has a manifest row
  and vice versa; version in SKILL.md matches the manifest row.
- **Pattern:** ledger_index.py (402 lines, marker-based zone regeneration,
  --check mode for CI-style dry run). Read ledger_index.py as the recipe;
  mirror the architectural choices (parse -> validate -> regenerate -> report).
- **Scope:** one file (~150-200 lines), lives in repo root alongside
  ledger_index.py. Reads skills/*/SKILL.md, writes the zone in
  project_instructions_v3_30.md (or its successor). Add to
  ledger-and-session-records skill's tooling section on completion.
- **Collegial build candidate:** tight enough spec for Fable 5 (or Opus 4.8)
  via the standard relay. Prompt attached: documentation/FABLE_PROMPT_L097.md.
**Gap:** build session -- Fable prompt ready, spec is tight.
**Ref:** L-002 (parent), ledger_index.py (pattern), project_instructions_v3_30.md Part 3 Skill Manifest.
```

---

## 3. Fable Build Prompt

Save as documentation/FABLE_PROMPT_L097.md in the orrery repo.

```markdown
# L-097 Build Prompt: skills_index.py

Collegial relay prompt for Claude Fable 5 (or Opus 4.8).
Tony carries this prompt; Fable builds; Tony reviews and integrates.
Built on palomas_orrery @ b1a5616 | July 4, 2026 | Claude Opus 4.6.

## The Job

Build `skills_index.py` -- a devtool that auto-generates the Skill Manifest
table in the project instructions from the SKILL.md files in skills/.

This is the SAME PATTERN as `ledger_index.py` (402 lines, repo root). Read
that file first as the recipe. Mirror its architectural choices:
parse -> validate -> regenerate in-place -> report.

## What It Does

1. Walk `skills/*/SKILL.md`. For each file:
   - Parse YAML frontmatter: extract `name` and `description`.
   - Parse the body's version line (the `Skill version: X.X | Cut from ...`
     line that appears near the top of every skill). Extract version number.
   - Extract the "Fires when" text: this is the text in the `description`
     field of the frontmatter, condensed to a short phrase. BUT: the current
     manifest uses HAND-WRITTEN "Fires when" summaries that are shorter
     than the full description. So the tool should either:
     (a) Read a `fires_when:` field from the frontmatter if present, OR
     (b) Use the first sentence of the description, truncated to ~60 chars.
     Recommend option (a): add a `fires_when:` field to each SKILL.md
     frontmatter. This is the cleanest and gives Tony editorial control.

2. Regenerate the Skill Manifest table in `project_instructions_v3_30.md`
   (or whatever the current `project_instructions_v*.md` file is -- accept
   the filename as a CLI argument with a default). The zone is between
   markers that must be ADDED to the protocol file:
   ```
   <!-- MANIFEST:START (generated by skills_index.py -- do not edit this zone by hand) -->
   ... table ...
   <!-- MANIFEST:END -->
   ```
   The surrounding prose (the paragraph above the table and the paragraph
   below) stays untouched -- only the zone between the markers is rewritten.

3. Run consistency checks (same pattern as ledger_index.py's problems list):
   - Skill directory exists in skills/ but has no manifest row -> PROBLEM.
   - Manifest row exists but no matching skills/ directory -> PROBLEM.
   - Version in SKILL.md body differs from a prior run's recorded version
     (optional: version-change detection via a lightweight state, or just
     report what's found and let the human compare).
   - SKILL.md missing frontmatter or version line -> PROBLEM.

4. Support `--check` mode (dry run: report what would change, exit 1 on
   problems, don't write). Same as ledger_index.py.

## Table Format

The current manifest table (hand-written) looks like:

```
Skill                        Ver  Fires when
orrery-coding-conventions    1.0  Markers, hover text, axes, shells,
                                  legendgroups, docstrings, new visuals
safe-file-editing            1.0  Editing existing files, patch scripts,
                                  sed/regex edits, encoding checks (portable)
...
```

This is a plain-text aligned table (not markdown pipe-delimited). Match
this format: skill name left-aligned, version right after the name column,
"Fires when" text wraps with indentation. Sort alphabetically by skill name
(matching the current order, which happens to be alphabetical).

## Constraints

- Pure Python 3, no external dependencies. Same as ledger_index.py.
- ASCII only, LF line endings.
- Module docstring following the project standard (see
  orrery-coding-conventions skill, Module Docstring Standard).
- Credit line: "Module created: July 2026 with Anthropic's Claude [model]."
- File lives at repo root alongside ledger_index.py.
- ~150-200 lines target. This is a simple tool.
- Do NOT touch any content outside the MANIFEST:START / MANIFEST:END
  markers. If the markers don't exist, report a problem and exit without
  writing (same safety as ledger_index.py's INDEX:START/END).

## Deliverables

1. `skills_index.py` -- the complete file, ready to place at repo root.
2. A short note listing any SKILL.md frontmatter amendments needed (if
   option (a) above: the `fires_when:` field additions for each skill).
3. The MANIFEST:START / MANIFEST:END marker lines to insert into
   project_instructions_v3_30.md (Tony will place them).

## What NOT to Do

- Do not modify any SKILL.md file.
- Do not modify the protocol file outside the manifest zone.
- Do not add complexity beyond what ledger_index.py demonstrates.
- Do not add a GUI, a config file, or any dependency.
- Flag problems; don't fix them. The tool REPORTS; Tony DECIDES.

## Verification

After building, run:
```bash
python3 -m py_compile skills_index.py
python3 skills_index.py --check
python3 skills_index.py project_instructions_v3_30.md
```
Confirm: zero problems, manifest table matches the current hand-written
version (or improves on it), no content outside the markers is touched.
```

---

## 4. Note on L-046 -> Encounter Skill

Tony noted L-046 will become an important skill as L-079 (shared assembler
architecture) moves forward. This is a design decision for a future session:

- L-046's scope (encounter generator -> preset-authoring capability) is
  the right content for a skill once the pipeline stabilizes.
- It could be its own skill (`encounter-building` or
  `encounter-preset-authoring`) or expand `horizons-orbital-mechanics`.
- The horizons skill already explicitly says "do not treat this as the
  encounter build recipe" (lines 55-59) -- so the boundary is clean.
- Recommendation: own skill. The encounter pipeline crosses both repos
  (spacecraft_encounters.py in orrery, preset export in gallery) and has
  its own data contracts (cube scale, curvature scale, camera capture)
  that are distinct from the Horizons query mechanics. A separate skill
  keeps both focused.
- Natural trigger: when L-046 status moves past the design conversation
  and the encounter pipeline has a stable architecture worth documenting.
