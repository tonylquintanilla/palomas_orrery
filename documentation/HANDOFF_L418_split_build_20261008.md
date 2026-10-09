<!-- Doc-Kind: hand | Session record: the provenance-discipline split built (L-418), the install trial and the read limit, 2026-10-08. -->
# Handoff: the provenance-discipline split, built (L-418)

Built on orrery b0b3df82 at
https://github.com/tonylquintanilla/palomas_orrery (branch main). The
gallery, ab66aba7 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, was read
for its swap log only and not changed.

- Type: BUILD. One patch, `patch_L418_3_split_build_20261008.py`.
- Companion to `documentation/HANDOFF_L418_split_build_brief_20261008.md`
  (the brief this session followed),
  `documentation/PREDESIGN_L418_provenance_skill_split_20261006.md` (the
  design) and `documentation/HANDOFF_L418_skill_split_design_20261006.md`.
- Skills read by this session, each loaded copy checked against the
  manifest and the repo byte for byte: provenance-discipline 2.26,
  ledger-and-session-records 1.17, safe-file-editing 1.13,
  agentic-pre-test 1.3.
- October 8, 2026, with Anthropic's Claude Opus 5.5. A parallel
  session (the ledger-session-records decisions session) ran the same
  evening; its note of 2026-10-08 carried two rulings here.

## Verified in this session

- **The install trial passed.** install-probe was installed:
  `references/probe.md` arrived beside SKILL.md, md5
  dc4f6011467ccc53f5b84f8a776b352b, holding the recorded sentence. Its
  manifest source was "plugin", the same as all eleven of Tony's
  skills, so the result speaks for them. Tony then deleted it.
- **The read limit.** This session's Read tool returned the first
  25,000 tokens of a file and announced the cut. On
  provenance-discipline 2.26 that was lines 1 to 1,106, 55,748
  characters. The design's viewer showed 16,000 characters from the
  start and the end. Read plans use the smaller: 16,000 characters and
  2,000 lines per part. The measurement and its date are written beside
  the limits in skills_index.py.
- **The patch, on throwaway copies of the repo:** the split moves
  fifteen sections and finds each whole in its new file; the 23 listed
  edits are each printed; a final check proves every section is its
  original plus exactly those edits. skills_index.py --check then ends
  "OK: 12 skills parsed". Each new check was shown failing first: a
  part over one read, lines in no part, an unfilled seed, a long file
  with no plan, a reference named and missing, a reference present and
  unnamed, a stray file in a skill folder, and a bad annotation example
  inside a reference file.
- **The L-252 paragraph checked against the code.** Three of its four
  definitions match `worksheet_checker.py`. UNCHECKED_MOVE is reached
  by two different cases, and Tony split the bullet into them.

## What changed

- provenance-discipline 2.27: the Review-Repair Protocol out to the new
  skill provenance-cross-check 1.0 (its three reference sections in
  `references/worksheets.md`); Rules 1 to 8 of the figure count to
  `references/figures.md`; the field notes to
  `references/field-notes.md`; the withdrawn derived-row rule and the
  v2.24 entry to `documentation/SKILL_HISTORIES.md`. A new heading,
  Cross-Checked Lines in the Store, keeps the two rules that fire on
  ordinary edits. Riding it: the range rule's examples (L-371), predict
  the scanner's change (L-371), the conversion marker (L-390), and the
  status-line and figures examples, which named rows since changed.
- provenance-cross-check 1.0: the protocol, with the L-252 paragraph
  beside the send-back rule.
- ledger-and-session-records 1.18: the read plan and reference files
  as conventions; the Anchor Requirement names provenance-cross-check
  for review prompts; its v1.15 entry to SKILL_HISTORIES.md.
- skills_index.py: writes and checks read plans, checks reference
  files, reads annotation examples in reference files, and lists
  provenance-cross-check after provenance-discipline in the manifest.
  PLAN_NOT_YET names gallery-cache-builder, interactive-exhibit,
  orrery-coding-conventions and safe-file-editing.
- PROJECT_INSTRUCTIONS.md v3.86; v3.83 to the history file.
- Ledger: L-418 records the build; L-390 closed; L-371 and L-351
  updated; L-424 opened (the checker's one word for two cases).

## Departures from the brief

- The brief said a phase-2 edit inside a moved section is refused.
  L-390's sentences and the L-252 paragraph both fall inside moved
  text, so the patch proves each section equals its original with
  exactly the listed edits instead.
- The brief named three versions to cut. Tony's ruling of 2026-10-06
  had said every skill over 16,000 characters gets a read plan; four
  more skills are that long, and each would have needed its own bump.
  Tony: plans at their next version ("confirmed as recommended").
- Where We Are's attention marks were left as found. A parallel session
  edits the same page tonight, and clearing its marks would hide its
  changes. The next close resets them.

## Next session

- Confirm the loaded copies read provenance-discipline 2.27,
  provenance-cross-check 1.0 and ledger-and-session-records 1.18.
- List both skill folders under the mounted skills and find the three
  reference files.
- On the first figures task, say whether `references/figures.md` was
  opened before a `# Figures:` line was written. Then L-418 closes.

## Tony-actions (rollup)

- **(do)** Run the patch, then orrery_maintenance_run.py; move the
  patch into documentation/; commit and push.
- **(do)** Install three skills from ZIPs: provenance-discipline,
  provenance-cross-check (new), ledger-and-session-records.
- **(do)** Replace the Project's instructions with PROJECT_INSTRUCTIONS.md.
- **(decide)** L-424 (the checker's one word for two cases): whether
  the checker itself prints two different words.

## Tony's notes carried from Where We Are

- None: this patch edits the page by section, and no line it edits
  carried a note.

## After the run, 2026-10-08 -- patch_L418_4 (the close)

Pushed at e5cc4bb21cdb69afe1393d394df704700f50f716 at
https://github.com/tonylquintanilla/palomas_orrery.

- Tony's run, from his run record
  (`documentation/WHERE_WE_ARE_10-8-26_1406_run_record.md`): all 13
  files written. The new check failed once, on two untracked
  `SKILL.md.bak` files in the orrery-coding-conventions and
  safe-file-editing folders on his machine. He deleted them, and the
  maintenance run passed 20 of 20, Skill headers 12. Pushed at
  ea2c0e16; skills installed; the Project's instructions replaced;
  pushed at e5cc4bb2.
- After the install, this session's mounted skills read
  provenance-discipline 2.27, provenance-cross-check 1.0 and
  ledger-and-session-records 1.18, with the three reference files.
  Tests A1 and A2 pass. The protocol says a mid-session install cannot
  be seen; this one was. Recorded on L-351.
- Delivered: `documentation/TESTING_PROTOCOL_provenance_skills_20261008.md`.
- Opened: L-425 (citation location checks), Tony to decide which to
  build.
- Two skill ZIPs were committed into skills/ (682c5395). Harmless to the
  check; recommended for deletion, because they go stale.
- Next session: tests A3 to A6. Then L-418 closes.

Tony-actions now: (do) run patch_L418_4, the maintenance run, push;
(decide) L-425; (decide) L-424; optional (do) delete the two ZIPs.

Session record written October 2026 with Anthropic's Claude Opus 5.5.
