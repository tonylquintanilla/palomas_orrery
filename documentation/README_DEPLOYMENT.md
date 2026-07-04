# L-002 Deliverables -- Deployment Steps (Tony-side)

All files built on palomas_orrery @ b29ad3f8 and tonyquintanilla.github.io
@ 89c8bf30 (both round-trip verified July 1, 2026). Nothing is pushed;
Claude has read-only access. Review order and steps:

1. REVIEW. Read the 8 SKILL.md files and project_instructions_v3_30.md
   against MAPPING_TABLE.md. The mapping table is the extraction audit:
   every v3.29 line has a destination; the duplication registry lists the
   copies that must move together in future amendments.

2. REPO (author-in-repo). Copy skills/ into the orrery repo root as
   skills/, MAPPING_TABLE.md into documentation/ (suggested name
   MAPPING_TABLE_L002.md -- the ledger entry references that name), and
   project_instructions_v3_30.md into its usual home.

3. LEDGER. Paste the body of LEDGER_version_history_block.md (below its
   cut line) at the end of LEDGER_CONSOLIDATED.md; run ledger_index.py and
   confirm zero new problems. Update L-002's status/detail block per your
   convention (the appendix is the version history; L-002 still needs its
   own closing entry).

4. PROVENANCE. Run provenance_scanner.py before push, per the standing
   gate. Note: the skills contain numeric claims (AU conversions, reference
   values) with prose attributions rather than # Source: comments; if the
   scanner's coverage ever extends to skills/ or .md files, they will need
   exceptions entries or a documented carve-out. Flagged as a design
   question in the session notes -- your call.

5. INSTALL (deployment step). Add each skill to your account
   (Settings -> Capabilities/Skills, per current claude.ai UI) by pasting
   or uploading each SKILL.md. Installed version must match the repo
   version -- the Skill Manifest in v3.30 Part 3 is the drift check.

6. PROJECT INSTRUCTIONS. Replace v3.29 with v3.30 in the project settings.

7. PUSH. Normal loop: local repo -> commit -> push; confirm the round trip
   next session against the new HEAD.
