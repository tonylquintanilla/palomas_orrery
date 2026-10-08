<!-- Doc-Kind: hand | Next-session brief for L-418 (splitting provenance-discipline): the install trial's status, what changed since the design, and the build to do, 2026-10-08. -->
# Handoff: L-418 (splitting provenance-discipline), the build brief

Built on orrery cdb99833b657c2298c333b2200e634db9854fe31 at
https://github.com/tonylquintanilla/palomas_orrery. Gallery at
ab66aba70a5874b033742a8428070b5889484490 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, not read
and not touched by this split.

- Type: DOCUMENTATION (zero code). A brief for the session that builds
  the split.
- Companion to `documentation/PREDESIGN_L418_provenance_skill_split_20261006.md`
  (the design, ruled) and
  `documentation/HANDOFF_L418_skill_split_design_20261006.md` (the
  design session's record). Neither is superseded; where this brief
  disagrees with them, this brief is newer and says why.
- Written because Tony's run record of 2026-10-07
  (`documentation/WHERE_WE_ARE_10-7-26_0832_run_record.md`) says the
  L-418 session still owes the trial's result and a handoff sending the
  build to a fresh session, "cutting the ledger skill at 1.18 now, not
  1.17".
- Skills read by this brief: ledger-and-session-records 1.17 (loaded
  copy matches the repo byte for byte) and the protocol v3.85.

## Read this first

- *First: the install trial. As of 2026-10-08 it has not been checked.*
- *Then, if it passes: one patch builds the split. Three versions to
  cut: provenance-discipline 2.27, provenance-cross-check 1.0,
  ledger-and-session-records 1.18.*
- *One decision for Tony before building: whether the owed
  provenance-discipline rules ride the same 2.27 (section 4).*
- *Re-measure the read limit before writing the read plan (section 3).
  The 16,000-character figure in the design may not hold here.*

## 1. The install trial, where it stands

- **Not checked.** No session has reported it, and no record in the
  repo at cdb99833 holds a result.
- **Not visible to this session.** This session's mounted skill list
  (`/mnt/skills/user/manifest.json`, last updated 2026-10-08 19:35 UTC)
  has no install-probe. So Tony either has not uploaded it yet, or
  deleted it before a check. Ask him which, in one line.
- **The ZIP.** `install-probe.zip`, from the design session's chat.
  It holds `install-probe/SKILL.md` and
  `install-probe/references/probe.md`. probe.md's md5 is
  dc4f6011467ccc53f5b84f8a776b352b; its one line reads "Probe
  sentence: the extra file arrived with the skill. Token
  L418-probe-20261006-7c1d." Keep the ZIP out of the repo: inside
  `skills/`, skills_index.py would add it to the manifest.
- **The check, in the session after Tony uploads it** (a running
  session does not see a new install):
  - `find /mnt/skills -path '*install-probe*'`
  - PASS: `references/probe.md` is listed and reads the sentence above.
  - FAIL: SKILL.md arrived without the extra file. The split is not
    built; the design is reopened.
  - NOT INSTALLED: nothing found.
  - Then Tony deletes install-probe from Settings.
- **One new thing to record at the check.** Tony's eleven skills
  appear in the mounted manifest with source "plugin". Anthropic's
  appear as "anthropic" or "anthropic-example". Note the source the
  probe arrives with. If it is not "plugin", an uploaded ZIP and Tony's
  usual install may not be the same route, and the trial would not
  prove the eleven keep extra files. Say so plainly if that happens.

## 2. What changed since the design (orrery fbd223ee to cdb99833)

- **ledger-and-session-records went to 1.17** on 2026-10-07, in L-422
  (the ledger skill at 1.17 and Tony's page). So the split cuts it at
  1.18, not 1.17. Its size is now 37,626 characters, 662 lines.
- **The split's targets are unchanged.** provenance-discipline (2.26,
  137,837 characters, 2,590 lines), skills_index.py and
  provenance_scanner.py have no commits since fbd223ee. The design's
  section sizes still hold.
- **Where We Are has new rules** (ledger-and-session-records 1.17): the
  close edits the page by section, never whole; nothing below the
  run-record marker; every handle carries a short label; read Tony's
  latest timestamped copy before writing the ledger. patch_L418_2 (the
  design's close) rewrote the page whole and is the founding case.
- **The ledger's Gap line for L-418 (splitting provenance-discipline) is stale.** It still says "the split above,
  when a design talk reaches it". The design talk has happened. The
  build's ledger edit rewrites it to: the build, after the trial.
- **Signals on Tony's page** say no tool prints the Tier-1 count on the
  push gate's path alone, "owed on the provenance-discipline bump".
  That belongs to L-414 (the scanner's window and declared rows),
  section 4, not to the split.

## 3. Re-measure the read limit first

- The design's read plan assumed one read shows 16,000 characters,
  from the start and the end. That was measured on 2026-10-06 in that
  session's file viewer.
- This session's Read tool documents a different default: up to 2,000
  lines from the start. On that tool a plain read of
  provenance-discipline shows lines 1 to 2,000 and misses the last 590,
  the cross-check procedure and the field notes.
- So the limit belongs to the tool, not the file. Before writing the
  read plan:
  - read a throwaway test file built to cross both limits (more than
    2,000 short lines, and more than 16,000 characters in fewer lines);
  - record what came back;
  - set skills_index.py's part size from that measurement, and write
    the measured limit and the date into the check's own comment.
- If both limits apply on different tools, the parts stay under both:
  at most 16,000 characters and at most 2,000 lines each. With the
  split done, the remaining SKILL.md is about 61,000 characters, so the
  plan is about four parts either way.

## 4. The decision for Tony before the build

- **The question.** L-351 (what each skill is owed at its next
  version) lists four items for provenance-discipline's next version:
  - L-371 (the Sun room's served numbers): the range rule's example
    names a removed row, and a patch's predicted run output should
    state the scanner's CHANGE, not its total.
  - L-390 (the conversion marker): the skill does not yet name the
    marker or say the widening is built.
  - L-414 (the scanner's window and declared rows): a Source line 16
    lines below its row is missed, and declared rows count as uncited.
    This one needs a scanner change as well as a rule.
- One Session, One Bump says a session ships one version of a skill. So
  the split session either takes these into 2.27, or leaves them for
  2.28 in a later session.
- **Recommendation: take L-371 and L-390 into 2.27; leave L-414 to its
  own session.**
  - L-371 and L-390 are sentence fixes inside sections that stay in
    SKILL.md. They cost one reinstall instead of two.
  - L-414 changes provenance_scanner.py and the push gate's count. That
    is a build with its own tests, and it would bury the split's
    "moved text is unchanged" check under real rule changes.
  - The Fable sweep (`documentation/LEDGER_SWEEP_review_20261007.md`,
    section 3) asks for L-414 before the Sun's list reaches L-228 (the
    Alfven surface latitude ranges). Leaving it out of 2.27 keeps that
    order possible: the L-414 session cuts 2.28.
- **How the patch stays checkable with L-371 and L-390 in it:** it
  works in two phases. Phase 1 moves the sections and checks every
  moved section is byte-identical, ignoring line endings. Phase 2 makes
  the two sentence fixes and prints each changed line, before and
  after. A phase-2 edit inside a moved section is refused.
- If Tony says "as recommended", build that. If he says "split only",
  2.27 is the pure move and L-371 and L-390 wait with L-414 (the scanner's window).

## 5. The build, in order

From the design's build order, updated:

0. The trial passes (section 1) and the read limit is measured
   (section 3).
1. Load and read whole: safe-file-editing, ledger-and-session-records,
   provenance-discipline (by its parts), agentic-pre-test for the
   skills_index.py change. Check each loaded version against the
   manifest (Stale Skill = Stop).
2. One patch, `patch_L418_3_split_build_<date>.py`, from the orrery
   repo root:
   - provenance-discipline 2.27: the four moves in the design, the
     pointers, the version paragraph; older entries to
     `documentation/SKILL_HISTORIES.md` by the three-entry rule.
   - `skills/provenance-cross-check/SKILL.md` 1.0 and
     `references/worksheets.md`.
   - `skills/provenance-discipline/references/figures.md` and
     `references/field-notes.md`.
   - skills_index.py: the read plan written under each long skill's
     version line; `--check` fails on a part over the measured limit,
     a line left uncovered, a reference named and missing, or a file
     in `references/` that SKILL.md does not name. Show each failure
     firing on a throwaway copy before trusting a pass.
   - ledger-and-session-records 1.18: the Anchor Requirement names
     provenance-cross-check for review prompts.
   - The protocol: a version entry; the manifest's twelfth row comes
     from skills_index.py, not by hand.
   - LEDGER_CONSOLIDATED.md: the build recorded on L-418 (splitting
     provenance-discipline) and its Gap rewritten; what landed struck
     from L-351 (what each skill is owed); a header
     stamp.
   - Where We Are: by section, with labels, nothing below the marker.
   - The session's handoff.
3. Run it on throwaway copies first: as the repo stands, with notes
   added by Tony, with Windows line endings, and a second time over
   (must refuse and write nothing). Then the maintenance run on the
   copy: every gating checker passes, and Skill headers counts 12.
4. Tony runs it, runs orrery_maintenance_run.py, pushes, and uploads
   three ZIPs: provenance-discipline, provenance-cross-check,
   ledger-and-session-records. Each ZIP holds the skill's folder with
   the folder at the top.

## 6. The obligation that travels

- The session after the build confirms its loaded copies read
  provenance-discipline 2.27, provenance-cross-check 1.0 and
  ledger-and-session-records 1.18.
- It also lists both new skills' folders under `/mnt/skills` and
  confirms the reference files arrived.
- On its first figures task, it says whether it opened
  `references/figures.md` before writing a `# Figures:` line. That is
  the only check of whether the pointer fires.

## 7. Open decisions for Tony (rollup)

- **(do)** Upload install-probe.zip if not done; say so if it was
  deleted before a check.
- **(decide)** L-371 and L-390 ride 2.27; L-414 waits for its own
  session (recommended), or the split ships alone. (L-371: the Sun
  room's served numbers; L-390: the conversion marker; L-414: the
  scanner's window and declared rows.)

Brief written October 2026 with Anthropic's Claude Opus 5.5.
