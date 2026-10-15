<!-- Doc-Kind: hand | Closing report for L-442: the master plan's restamp to v36 (strategy only), its dated history and lineage moved to MASTER_PLAN_HISTORY.md, and ledger-and-session-records 1.21 carrying Tony's seven kinds of document. Built and pre-tested; waiting on Tony's run. -->
# Handoff: the master plan restamp (v36) and the seven kinds of document (L-442)

Built on orrery 9248845ca8516dcee3498f07c554e6a24426c23c at
https://github.com/tonylquintanilla/palomas_orrery ("v3.96"); gallery
read at 86ef2df6313f956f5c9e49611e6a2bdd0e95da29 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io and not
touched. Pushed at 2b0e54cc525f616e477f639e4234a284be94d14d
(Tony's push of 2026-10-14; his run record is
`documentation/WHERE_WE_ARE_10-14-26_2250_run_record.md`).
Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`;
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.
Written October 14, 2026 with Anthropic's Claude Opus 5.5, in a
coordination session.

- Type: DOCUMENTATION build. One patch, orrery only, no code changed.
- Built from: `documentation/HANDOFF_master_plan_restamp_brief_20261013.md`.
- Patch: `patch_L442_1_master_plan_restamp_20261014.py`, saved in the
  orrery folder. Built and pre-tested here; not yet run by Tony.

## 1. What the patch does

- **The plan, v35 to v36.** A new front page says what the plan is
  (strategy) and is not (the order, which is the road; the status,
  which is the ledger's), lists the seven kinds of document, and says
  where the work stands by the five segments. Section 5a keeps the
  shape and gains The direction, the paragraph for L-433 (the road
  after the Sun and Earth rooms). Every line that named 5a as the
  order's home now points at the road. The plan goes from 3,362 lines
  to 1,729.
- **The plan's history moves out**, word for word, to a new record,
  `documentation/MASTER_PLAN_HISTORY.md`. Part 1 is the critical
  path's dated record (the "You are here" table of Aug 23 and the
  subsections Aug 25 to Sep 29). Part 2 is the lineage, formerly
  Section 10, which stops at v19 (Aug 23).
- **The skill ledger-and-session-records, 1.20 to 1.21.** The Document
  Stack becomes your seven kinds, each with when it is read. Sequencing
  moves from the plan to the road. Its 1.18 entry moves to
  `documentation/SKILL_HISTORIES.md`.
- **The protocol, v3.96 to v3.97.** One entry, no rule changed; v3.94
  moves to `documentation/PROJECT_INSTRUCTIONS_HISTORY.md`.
- **The ledger.** L-442 records the ruling and closes. L-433 closes:
  you confirmed its order on Oct 12. Its unfinished notes go, word for
  word, to a new item, L-443 (the objects to the website). L-221 gets a
  Note: sequencing moved, status stays. L-431's line saying the
  website's live check was missing from your record is corrected.
- **Where We Are**, by section, above the run-record marker only.

## 2. Where this departs from the brief, and why

- **Protocol v3.97, not v3.96.** Build 3 used v3.96 the same day, so
  v3.94 is the entry that moves down.
- **Section 10 moved too, and the file has a different name.** Your
  ruling of Oct 14, after you asked for a recommendation: "Changing
  ruling to: Yes move it." One file holds both histories, so it is
  `MASTER_PLAN_HISTORY.md`, not `MASTER_PLAN_CRITICAL_PATH_CHRONICLE.md`.
- **The "You are here" table moved with the dated subsections** rather
  than being deleted. It is dated Aug 23 too, and moving it loses
  nothing.
- **L-443 opened now, not at the objects session's close.** L-433
  could not close while its notes had no open home. The brief's own
  handle, L-438, had been retired.
- **The Doc-Kind table adds no value.** The brief assumed the Doc-Kind
  line is where a file's class is written. It is not: its three values
  (hand, zoned, generated) say how a file is written. The skill maps
  them onto the seven kinds in a table. The plan had no Doc-Kind line
  and gets one; no file is retagged.
- **Where We Are:** stage 11 (the objects) is marked [next], because
  the page's own Do next already named its design session. The
  OneDrive line left Settled to keep the page within its 130 lines.

## 3. Sections 6 and 7 against the ledger (one pass, The Braid)

Five disagreements, each corrected in one line and marked "at v36":
- Section 6 said L-154 (the feature renderers) still read BLOCKED. It
  closed DONE on Aug 24.
- Section 6 said retiring MODULE_DOMAIN_MAP was deferred. L-437 retired
  it on Oct 13.
- Section 7, decision 12, retired a JSON export. L-322 then built one,
  `data/constants_export.json`, on Sep 16, and it is the route today.
- Section 7, decision 13, said there is no generation step. There is
  one since Sep 16, for the same reason.
- Section 7, decision 18, left open whether every measured field should
  hold a range. The provenance skill answers it as method: store the
  range as rows.

Checked and in agreement, or still open in the ledger: L-080, L-068
with L-066, L-016 and L-014, L-087, L-162, L-170 to L-173, L-176 to
L-182, L-190.

Recorded on L-442, not chased: Section 6's Attribution page ("not
started", required before any public interactive page) has no ledger
item. The plan's long status block under the summary was last written
at v35; it now says so.

## 4. The pre-test

- On a throwaway copy of the orrery at 9248845: the patch ran clean (47
  edits in 8 files); run a second time, it refused.
- `skills_index.py`: the manifest moved ledger-and-session-records 1.20
  to 1.21; `--check` passed; the skill's read plan is now 4 parts.
- `ledger_index.py`: moved L-433 into the closed section; 241 live
  items; L-438 and L-439 stay retired.
- The orrery maintenance run, on a clean copy and on the patched copy
  side by side: the same 28 of 32 passed on both. The same four failed
  on both, for reasons in this sandbox, not in the patch: Reset
  completeness, Earth pole of date, Position digits, Orbit markers.
  Tier-1 on the gate path: 0 on both. The whole tree: 280 on both, and
  no file rose.
- Planted faults, each caught by the patch's own post-checks: a dated
  subsection left in 5a; a line saying the order lives in 5a; the skill
  still giving the plan SEQUENCING; the history file one byte short;
  the lineage left in the plan as well; a non-ASCII character; the
  patch run before L-431 (orbital periods) closed.

## 5. What travels to the next session

- The next session confirms its loaded copy of
  ledger-and-session-records reads 1.21 before ledger work.
- This session confirmed its loaded copies read horizons-orbital-mechanics
  1.6, gallery-cache-builder 1.9 and interactive-exhibit 1.15, which
  discharges v3.96's obligation.
- Next on the road: the design session for L-443 (the objects to the
  website), from `documentation/HANDOFF_L438_objects_to_website_brief_20261013.md`.
  The brief calls the item L-438; it is L-443.

## 6. Tony's actions, all of them

- (decide) The new front page of the plan: does it tell you what the
  plan is for, in about one screen? A change goes in before you run.
- (do) Run `patch_L442_1_master_plan_restamp_20261014.py` from the
  orrery folder (VS Code, Run).
- (do) Run `orrery_maintenance_run.py`. Expect the manifest to move
  ledger-and-session-records 1.20 to 1.21, and the ledger index to move
  L-433 and L-442 to the closed section.
- (do) Reinstall ledger-and-session-records from `skills/` in
  Settings > Skills.
- (do) Save `PROJECT_INSTRUCTIONS.md` as
  `documentation/project_instructions_v3_97.md`, and copy it into the
  Project's instructions.
- (do) Move the patch into `documentation/`; commit and push.

Session written October 2026 with Anthropic's Claude Opus 5.5.
