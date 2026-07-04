# L-002 Deliverables -- Deployment Steps and Review (Tony-side)

All files built on palomas_orrery @ b29ad3f8 and tonyquintanilla.github.io
@ 89c8bf30 (both round-trip verified July 1, 2026). Nothing is pushed;
Claude has read-only access.

Reviewed by Claude Opus 4.6 on July 4, 2026 against repo HEAD @ 33f0b148.
SHA confirmed; all 8 skills, v3.30 protocol, and 3 documentation files
verified byte-identical between uploads and repo copies.


## Review Summary (Opus 4.6, July 4 2026)

VERDICT: Ready to deploy. The extraction is clean, the mapping is
auditable, and the two-layer architecture is sound.

What the protocol KEPT (correctly): all CRITICAL checkpoint gates, the
modes, the principles, the Foundation philosophy, the quotables, the
process and philosophical lessons. These fire unprompted -- they don't
belong behind a trigger.

What the protocol EXTRACTED (correctly): bottom-up editing, binary-mode
patching, pre-test mechanics, Horizons query patterns, scanner mechanics,
marker conventions, shell dispatch map, gallery pipeline chain. These load
at the moment of need.

The bridging mechanism (Skill Manifest table, lines 285-308) works:
specific enough "Fires when" column, plus the backstop trigger row
("Relevant skill unfired -> load it"). Context Priority tier 5 now names
the skills alongside the protocol -- correct elevation.

Skills 1-5 are clean extractions from v3.29 Part 3, verified at the
stated SHAs. Skills 6-8 (earth-system-pipeline, gallery-pipeline,
ledger-and-session-records) are the payoff -- first-time capture of
knowledge that previously lived only in handoffs and in your head. The
earth-system-pipeline alone captures the teaser/blockbuster architecture,
engine/scenario contract, 3+5 card pattern, developing-scenario pattern,
fetch discipline, and human-cost restraint discipline.

Specific verifications performed:
- provenance-discipline scanner mechanics updated to reflect L-078's
  role-driven gate (more current than v3.29's text, which predated it)
- horizons-orbital-mechanics explicitly scopes OUT the encounter build
  recipe (L-046 still evolving) -- responsible
- gallery-pipeline stamps TWO repo SHAs (both repos) -- correct
- safe-file-editing marked PORTABLE -- the one skill that applies
  beyond Paloma's Orrery
- All files ASCII, LF line endings, no encoding issues
- New process lesson (line 607): "Skills are stores too" -- self-
  referential in the right way

One cosmetic note: `file` command reports "exported SGML document" for
ledger-and-session-records/SKILL.md due to the <!-- --> HTML comment
syntax in the example block. Valid markdown, functions fine.

Accounting confirmed: 807 lines (v3.29) -> 644 lines resident (~21%
reduction) + 988 lines across 8 skills (~2/3 first-time capture).


## Fable's Suggestions -- Opus 4.6 Assessment

1. `skills_index.py` -- YES, build it. The pattern is proven
   (ledger_index.py solved the exact same drift class). The Skill
   Manifest table in v3.30 Part 3 is currently hand-maintained -- the
   same failure mode. A small devtool that walks skills/, reads
   frontmatter and body version line, regenerates the manifest table
   between markers. Natural L-item. Low cost, durable value.

2. Scanner scope for skills/ -- Documented carve-out recommended.
   "Skills cite by prose; the masters live in cited .py code." The
   skill values (AU conversion, reference distances) ARE cited in the
   code files they reference. Adding skills/ to scanner scope would
   create a wave of findings against prose that is, by design, one
   layer removed from the code. A one-line ledger note is the right
   landing.

3. Encounter-building skill placeholder -- Correct not to build.
   L-046 still evolving. The horizons skill says so explicitly.
   When the encounter pipeline stabilizes, natural skill addition.

4. README_DEPLOYMENT.md -- Clean seven-step checklist, correctly
   ordered. (This amended version preserves and extends it.)

5. Attribution -- Honest and accurate. Keep as written: "Designed
   with Claude Opus 4.6; built with Claude Fable 5 via collegial
   relay; Tony integrated."


## Deployment Steps

Review order and steps:

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


## Tony's To-Do Checklist

### Deploy v3.30 (steps 1-7 above)

- [ ] Read-through: skim each SKILL.md against your knowledge of the
      domain it covers. You wrote most of this knowledge into handoffs;
      Fable extracted it; this is your verification that nothing was
      lost or distorted.
- [ ] Rename MAPPING_TABLE.md to MAPPING_TABLE_L002.md in documentation/
      (currently at the plain name in the repo).
- [ ] Paste version history block into LEDGER_CONSOLIDATED.md (below the
      cut line in LEDGER_version_history_block.md).
- [ ] Run ledger_index.py -- confirm zero new problems.
- [ ] Write L-002 closing entry in the ledger (status -> DONE, note the
      SHAs, credit the relay).
- [ ] Run provenance_scanner.py -- confirm Tier-1 = 0.
- [ ] Install 8 skills to claude.ai account (Settings -> Skills).
- [ ] Replace v3.29 with v3.30 in project settings.
- [ ] Commit and push.
- [ ] Next session: confirm SHA round trip against new HEAD.

### Follow-up items (post-deploy, not blocking)

- [ ] Ledger note: scanner scope carve-out for skills/ ("skills cite
      by prose; masters live in cited .py code"). One line in L-002's
      detail block or a new L-item -- your call.
- [ ] New L-item: skills_index.py devtool (walks skills/, reads
      frontmatter, regenerates Skill Manifest table between markers
      in v3.30 Part 3). Same pattern as ledger_index.py.
- [ ] Decide: when encounter pipeline stabilizes (L-046), does it
      become its own skill or expand horizons-orbital-mechanics?
- [ ] Check Fable 5 subscription status before planning next Fable
      session (per on-the-horizon note).
