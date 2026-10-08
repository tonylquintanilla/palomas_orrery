<!-- Doc-Kind: hand | Session record: the skills sweep, the provenance-discipline split designed and ruled, and the install trial (L-418), 2026-10-06. -->
# Handoff: the skills sweep and the provenance-discipline split (L-418)

Built on orrery fbd223eee7cb8823439c17d64fa23bb5e04110eb at
https://github.com/tonylquintanilla/palomas_orrery. The gallery was not
read. DESIGN SESSION (zero code): no code and no skill changed.
Companion: `documentation/PREDESIGN_L418_provenance_skill_split_20261006.md`.
October 6, 2026, with Anthropic's Claude Opus 5.5.

## What Tony asked

- Sweep the skills and the protocol so they fit the needs and abilities
  of Claude Opus 5.5. Remove a skill if it is no longer needed, or add
  improvements.
- The aim: better accuracy and precision of facts and sources, and less
  computational overhead where possible.

## What was verified, not claimed

- All eleven installed skills match `skills/<n>/SKILL.md` at fbd223ee
  byte for byte, and their versions match the manifest.
- That discharges the checks carried forward: interactive-exhibit 1.12
  (v3.84), agentic-pre-test 1.3 (v3.83) and ledger-and-session-records
  1.16 (v3.82).
- Sizes, in characters: provenance-discipline 137,837;
  interactive-exhibit 50,371; safe-file-editing 35,546;
  orrery-coding-conventions 32,894; ledger-and-session-records 32,871;
  gallery-cache-builder 25,169; gallery-assembler 14,451;
  earth-system-pipeline 11,730; gallery-pipeline 8,537;
  agentic-pre-test 6,518; horizons-orbital-mechanics 4,520. The
  protocol is 69,507.
- The file viewer shows at most 16,000 characters of a file per read,
  taken from the start and the end.
- Anthropic's pages, read this session: a custom skill is uploaded as a
  ZIP of its folder; extra files in the folder enter the context only
  when they are read, and SKILL.md should say when to read them.
- In this session's sandbox, Anthropic's own skills arrive with their
  extra files (the Word skill has 61; skill-creator has `references/`
  and `scripts/`). Tony's eleven arrive under `/mnt/skills/plugins/`,
  one file each.
- Every skill area has open ledger items, so no skill is retired. The
  quietest, earth-system-pipeline, has 9, among them L-001 and L-078,
  and carries the human-cost restraint rule; gallery-pipeline has 13.

## Found, not acted on

- Anthropic's support page on creating custom skills gives the
  description a 200-character maximum. The developer overview and
  best-practices pages give 1,024, which L-417's check uses. Our
  descriptions are longer than 200 and reach the session in full, so the
  200 figure appears out of date. No change proposed.
- Tony's skills are mounted under `/mnt/skills/plugins/`, not
  `/mnt/skills/user/`, where uploaded skills usually appear. The trial
  shows where an uploaded skill lands.
- The protocol, 69,507 characters, is read on every turn of every
  session. Its own design is not started.

## Pushback, recorded

- No rule is removed on the grounds that a newer model needs it less. A
  model's say-so about its own reliability is not a check; it is the
  same failure as a `# Source:` line over remembered data.

## Rulings

- Tony, "Confirmed as recommended": write the split as a design for his
  ruling, with no code.
- Tony, "Read and confirmed": all five points of the design.

## The install trial

- `install-probe.zip` holds `install-probe/SKILL.md` and
  `install-probe/references/probe.md`. Tony keeps the ZIP out of the
  repo: inside `skills/`, skills_index.py would add it to the manifest.
- probe.md holds one line: "Probe sentence: the extra file arrived with
  the skill. Token L418-probe-20261006-7c1d." Its md5, LF endings, is
  dc4f6011467ccc53f5b84f8a776b352b.
- The next session runs `find /mnt/skills -path '*install-probe*'` and
  reports one of three results, in plain words:
  - PASS: `references/probe.md` is listed and reads the sentence above.
  - FAIL: SKILL.md arrived without the extra file.
  - NOT INSTALLED: nothing found.
- Then Tony deletes install-probe from Settings.
- On FAIL, the split is not built and the design is reopened.

## Next session

- The trial check, then the split, built from the design's build order.
- Versions to cut: provenance-discipline 2.27, provenance-cross-check
  1.0, ledger-and-session-records 1.17. The protocol gets a version entry
  and a twelfth manifest row.

## Tony's notes carried from Where We Are

- None: the lines this patch edited carried no notes.

Session record written October 2026 with Anthropic's Claude Opus 5.5.
