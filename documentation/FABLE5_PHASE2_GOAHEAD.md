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

**3. Skills 6-8 sourcing: Derive from code with verify tags.**
The workflow handoffs are session artifacts, not in the repo. The
authoritative source is the code at HEAD. Read these modules and derive
the workflow patterns, tagging inferences `[DERIVED FROM CODE — VERIFY]`:

For earth-system-pipeline (skill 6):
- `earth_system_generator.py` (the engine)
- `earth_system_common.py` (shared helpers: briefing_to_balloon_html,
  create_info_placemark, ScenarioPicker)
- `food_insecurity_generator.py` (the food-insecurity engine)
- `scenarios_food_insecurity.py` (Sudan scenario, stub countries)
- `scenarios_heatwaves.py` (grid scenario registry)
- `scenarios_western_heatwave_march_2026.py` (dated-series pattern)
- `scenarios_coral_bleaching.py` (ocean pattern)

For gallery-pipeline (skill 7):
- `gallery_studio.py` (the Studio)
- `json_converter.py` (HTML → JSON)
- `index.html` in the gallery repo
  (https://github.com/tonylquintanilla/tonyquintanilla.github.io)

For ledger-and-session-records (skill 8, your renamed version):
- `ledger_index.py` (index generator + DONE migration)
- `LEDGER_CONSOLIDATED.md` (the ledger itself — read the header for
  conventions, format, and the document stack description)

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
