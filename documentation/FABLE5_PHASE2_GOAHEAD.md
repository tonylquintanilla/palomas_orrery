# Phase 2 Go-Ahead

Your Phase 1 feedback was excellent. Here are my decisions on your four
questions, followed by the green light for Phase 2.

## Answers

**1. Author-in-repo / install-as-deployment: Yes.**
You're right — account-level skills without version control violate our
own epistemology. Author in `skills/` in the repo, install to my account
as a deployment step. The ledger becomes the skill change log. Deliver
the `skills/` directory structure.

**2. Lessons archive split: Yes.**
Technical lessons distribute into matching skills as "field notes."
Process and Philosophical stay resident. The full archive (all three
lists) is preserved in the ledger as institutional memory. Your point
stands: JPL binary ID encoding and `JSON.stringify(undefined)` guards
are not philosophy — they're task-triggered reference.

**3. Skills 6-8 sourcing: Code at HEAD PLUS handoffs from documentation/.**
The workflow handoffs ARE in the repo's `documentation/` directory —
you can fetch them directly. Use code as the mechanical ground truth
and handoffs for workflow narrative, design rationale, and lessons.
Tag any inference not grounded in either source `[VERIFY]`.

For earth-system-pipeline (skill 6):
- Code: `earth_system_generator.py`, `earth_system_common.py`,
  `food_insecurity_generator.py`, `scenarios_food_insecurity.py`,
  `scenarios_heatwaves.py`, `scenarios_western_heatwave_march_2026.py`,
  `scenarios_coral_bleaching.py`
- Handoffs (in `documentation/`):
  `HANDOFF_food_insecurity_design_v2.md` (18KB — design rationale)
  `western_heatwave_handoff_v9.md` (40KB — latest workflow)
  `HANDOFF_food_insecurity_build_v2.md` (8KB — build lessons)

For gallery-pipeline (skill 7):
- Code: `gallery_studio.py`, `json_converter.py`
- Gallery repo: https://github.com/tonylquintanilla/tonyquintanilla.github.io
  (index.html is the viewer)
- Handoff: `documentation/web_gallery_handoff.md` (253KB — 30+ sessions,
  the master gallery document. This is large; read at least the latest
  sessions and the architecture sections)

For ledger-and-session-records (skill 8, your renamed version):
- Code: `ledger_index.py`
- Source: `LEDGER_CONSOLIDATED.md` (read the header for conventions,
  format, and the document stack description)
- Handoffs: `documentation/handoff_v29_ledger_cleanup.md`,
  `documentation/HANDOFF_v28_consolidated_ledger.md`

**4. Horizons portability: No. Anchor to the project.**
No non-orrery astro work in this account. Horizons gets the same
project-anchored trigger as the other orrery-specific skills.

## Accepted feedback (all nine points)

I accept all nine points from your Phase 1. To confirm:

1. **Author-in-repo / install-as-deployment** — accepted (answered above)
2. **Portability taxonomy** — accepted. safe-file-editing is the only
   portable skill. All others project-anchored with two-factor triggers
   (strict project match, pushy task match using atlas vocabulary)
3. **Lessons archive split** — accepted (answered above)
4. **Skills 2 and 3 separate, pre-test gets three firing paths** —
   accepted. (a) somewhat-announced trigger, (b) Bucket-B resident
   pointer, (c) skill manifest
5. **Skill manifest table in trimmed protocol** — accepted. Structural
   table in Part 3: skill name, purpose, expected version, when it
   should have fired. Replaces scattered one-line pointers
6. **Cross-pipeline small duplication** — accepted. One-to-three-line
   conventions duplicated into each pipeline skill, tracked in the
   mapping table. The three-line human-cost restraint core duplicated
   into gallery-pipeline with pointer to full treatment
7. **Skill 8 renamed ledger-and-session-records** — accepted. Includes
   handoff structure alongside ledger mechanics. "Read the ledger at
   session start" stays in resident Part 1
8. **Phase 2 sourcing from code** — accepted (answered above)
9. **Calibrate success** — accepted. ~30% resident cut, but the real
   payoff is extensibility and bringing workflow knowledge (skills 6-8)
   into the system for the first time

## Phase 2 deliverables

Please produce:

1. **The `skills/` directory structure** — one folder per skill, each
   containing SKILL.md with YAML frontmatter. If any skill warrants
   bundled reference files, include those in a `references/` subfolder
2. **The trimmed protocol** — `project_instructions_v3_30.md`, ready to
   replace v3.29 as the project instructions. Include the skill manifest
   table in Part 3. Move version history to the ledger (keep last 2-3
   entries as a pointer in the protocol)
3. **A mapping table** — "this v3.29 section/line → this skill, line N"
   so we can verify nothing was lost
4. **A version-history block** for the ledger — the full version history
   (v1.0 through v3.29) formatted as a ledger section, plus a v3.30
   entry documenting this refactor
5. **Any novel ideas** you want to flag — skills we haven't considered,
   structural improvements, workflow observations from reading the code

Take your time with this. Thoroughness matters more than speed. If the
output needs to span multiple messages, that's fine — just indicate
"continued in next message" and keep going.
