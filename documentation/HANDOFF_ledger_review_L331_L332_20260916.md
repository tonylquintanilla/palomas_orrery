# The ledger review, two skill bumps, and the Sun's four hovers reach the panel

Built on orrery `d99d8db1d3bac407e1d3891b9c6b016d839898c7`
at https://github.com/tonylquintanilla/palomas_orrery
Gallery at `b375cfe1dd9901a133d7a811f6ccba0d48167975`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io

Both HEADs read back with `ls-remote` at session start and unchanged
through the session. Neither repository moved: nothing was pushed from
here. After Tony runs the three patches below and pushes, both move;
those SHAs are his to report.

Tony Quintanilla, PE | Claude Opus 5 | 2026-09-16
Type: DOCUMENTATION + BUILD. Two orrery patches (skills, protocol, four
generators, the ledger), one gallery patch (renderers, a smoke suite,
the page's info text).
Handles: L-332 (built and closed), L-331 (mechanical half built), L-273
(orrery half built), L-333 (opened), and five closures: L-226, L-232,
L-271, L-277, L-278.
Continues `HANDOFF_L316_L318_phone_chrome_20260916.md`. Does not
supersede it.

---

## STEP 0 -- before you do anything

1. `git status --porcelain` in both repositories. Expect nothing, unless
   Tony has run the patches and not yet committed.
2. `git ls-remote` both. Expect the SHAs Tony reports after pushing.
3. Version-check every skill at load. **The session that made a bump
   cannot verify its install.** This session loaded interactive-exhibit
   1.2, orrery-coding-conventions 1.8, ledger-and-session-records 1.11,
   safe-file-editing 1.11, agentic-pre-test 1.2, and matched the
   manifest at `d99d8db1`. After patch 1 the manifest says
   interactive-exhibit **1.3** and orrery-coding-conventions **1.9**. The
   next session confirms its loaded copies read 1.3 and 1.9 before
   exhibit or hover work. If they read 1.2 and 1.8, the reinstall did
   not land: stop, per Stale Skill = Stop.
4. The ledger's first `ledger_index.py` run after patch 2 prints twelve
   `[auto-fix]` lines and moves six blocks. That is the tool filing the
   closed items. The second run prints `OK: 328 L-blocks parsed`.

---

## WHAT HAPPENED

Tony asked for a review of the master plan and ledger for missing, stale
or misindexed items, with discretion to fix routine things and report.

**The plan is current; five ledger items were done and open.** The
master plan is at v32, stamped this morning. The ledger indexed clean
(327 blocks). But five items in section A had met their own Gap and
nobody had closed them, in one case for three weeks. Each was checked
against the repo at HEAD rather than against its record:

- L-226, safe-file-editing 1.8 -- the skill is at 1.11 and every session
  since has loaded it.
- L-277, the site store re-anchored -- its Gap named three conditions;
  all three hold, the two checkers run green here.
- L-278, the Plotly re-entry lesson -- in gallery-assembler, as its own
  body records.
- L-271, backup files -- rule in the skill, ignore rules widened in both
  repos, backups swept; its two Gaps are facts, not work.
- L-232, the gallery's served constants -- its second candidate shape is
  the runner's Store drift check, built as L-236 and widened twice. The
  residue (the `source` TEXT is unchecked) moved to L-266.

**Three ledger edits had no header stamp.** The patches of September 14,
15 and 16 edited LEDGER_CONSOLIDATED.md and did not add a "Module
updated" line. Added retroactively, marked as such (the September 12
precedent).

**The interactive-exhibit skill was five rounds stale** (L-332, the
previous handoff's first item). Bumped to 1.3. Tony's standing rule --
no compressed language in hover text -- also went into
orrery-coding-conventions as 1.9, because the orrery's hovers are where
it reaches next (L-321) and that session loads the conventions skill,
not the exhibit one. Protocol v3.60 names both; v3.57 moved to the
history file.

**L-273's indexer was half-built.** README.md's document table showed
five generated documents as **untagged** because their four generators
never emitted the `Doc-Kind` line. One line each; all five outputs now
open with the tag and `doc_index.py` reports "generated 5".

**L-331's mechanical half is built, render-gated.** The Sun's four
custom shapes send their citations to the i panel and end their hovers
with the pointer line. Found on the way: the Hills torus and Oort clump
`note` fields were read by nothing, so their caveats had been missing
from the hover AND the panel. The hover budget suite now builds the Sun
room; on the unpatched tree its pointer leg fails naming exactly those
four. Both rooms' info text stops saying a shell's source is in its
hover and Earth's stops saying the magnetosphere is not drawn.

---

## WHAT TONY RULED

Nothing new this session; it ran on standing rulings. Two of them did
the work:

- **"Routine fixes, do and report instead of report only"** (Tony,
  2026-09-16, opening this session). Five closures, three stamps, four
  generator lines and one stale pointer were done on that word.
- **"In general we should avoid compressed language in the hovertext"**
  (Tony, 2026-09-16, previous session). Written into two skills. The
  four new hover sentences in the gallery patch are its first
  application, and they go to Tony as the patch itself.

---

## VERIFIED VS CLAIMED

Verified inside the session:

- Every patch ran on a clean copy of the pushed tree and refused a
  second run. The two orrery patches ran in both orders.
- After patch 1 on the throwaway: `skills_index.py` reported the
  manifest stale on both rows and corrected it (11 skills, no
  problems); three protocol entries resident, v3.57 in the history
  file; all four generators compile and run, and each output's first
  line is the tag; `doc_index.py` shows no untagged row.
- After patch 2 on the throwaway: `ledger_index.py` files six blocks
  into section C on its first run and reports 328 blocks clean on its
  second.
- After the gallery patch on the throwaway: the renderers and the page's
  one inline script parse; `smoke_hover_budget.js` (96 hovers, ceiling
  still 17), `smoke_features.js`, `smoke_sun_shells.js` and
  `smoke_framing.js` all pass with the runner's own arguments; the
  budget suite's pointer leg FAILS on the unpatched renderers, naming
  the four Sun hovers. The four hovers and their `meta` were printed
  and read: each ends with the pointer line, each carries its caveat,
  the panel's Source line carries both citations joined by "; ".
- `test_worksheet_keys.py` and `test_extractor_pins.py` green at
  `d99d8db1` (L-277's closing condition).
- The three unstamped ledger commits and their base SHAs, from git.

Claimed and NOT verified:

- Every render. The sandbox has no WebGL and no phone. The four Sun
  hovers, the panel's Source and note lines, and both info texts are
  Tony's to see.
- The skill reinstall (architectural, see STEP 0).
- The `orrery_maintenance_run.py` end to end. The generators were run
  one at a time here; the runner itself was not.

---

## THE LESSON

**A closed Gap is not a closed item.** Five items had met the condition
their own Gap line stated -- one of them, L-277, said "Close then" in so
many words -- and stayed open, because the session that met the
condition was doing something else and no later session reads section
A looking for items that are already done. The ledger skill's Cluster
the Tail rule found the same shape in August (an item 69 days old,
already done). The move that found them here was cheap: print every
open item's Gap line and ask of each one whether the repo already
satisfies it. That is a session-start step, not a cleanup event.

The smaller one: **the four Sun hovers were missed because the check
that should have caught them never built the Sun**, and the fix here
was to make the suite read the served store rather than a fixture --
the store cannot go stale the way the Earth fixtures can. When adding a
room, add it to the suite before trusting the suite's green.

---

## STILL OPEN

1. **L-331** -- Mode 5 in the Sun room on the four hovers and the panel,
   and in both rooms on the info text. Then the plain-language pass over
   the remaining hovers ("served" x14, "sourced" x5, "drawing choice"
   x5, three capitalised labels), wording to Tony first. The Galactic
   Tide's served `source` string in `objects_config.json` still reads
   "DECLARED -- ..." and shows in the panel's Source line. The ceiling
   comes down with the tallest hover; it is 17.
2. **L-333** -- the two master-plan companions, stamped August 19 and
   29. Tony decides: restamp both, or retire the critical-path one.
3. **L-273** -- the gallery half (no `doc_index.py` there).
4. **Close L-316 and L-318?** Unchanged from the previous handoff.
5. **Carried, unchanged:** L-330, L-322, L-231's Jupiter builder, L-061.

---

## TONY-ACTION ROLLUP

1. **(do)** ORRERY: run `patch_L332_1_skills_protocol_generators_20260916.py`.
   Then `python skills_index.py` (or the maintenance run, which
   includes it and `doc_index.py`). Expect the manifest to report both
   rows stale and correct them.
2. **(do)** ORRERY: run `patch_L332_2_ledger_20260916.py`, then
   `python ledger_index.py LEDGER_CONSOLIDATED.md` TWICE (STEP 0, item
   4).
3. **(do)** ORRERY: commit both SKILL.md files, PROJECT_INSTRUCTIONS.md,
   the history file, the four generators, the ledger and the
   regenerated outputs together; push; report the SHA.
4. **(do)** Reinstall interactive-exhibit and orrery-coding-conventions
   at Settings > Skills.
5. **(decide)** GALLERY: read the VISITOR_WORDING block in
   `patch_L331_1_sun_hovers_to_panel.py` -- four sentences. Edit them or
   leave them; then **(do)** run it, run `gallery_maintenance_run.py`,
   commit, push, report the SHA.
6. **(do)** Mode 5, Sun room: name the Streamer Belt, Hills Cloud, Outer
   Oort Cloud and Galactic Tide. Each box should end with the pointer
   line and carry no citation; the i panel should show "Source:" under
   the link and the note beneath. Then read both rooms' info text.
7. **(do)** File this handoff to the orrery's `documentation/`. Archive
   the three spent patches to `documentation/` after they run, and
   `patch_L231_dashboard_hover_budget.py`, still in the orrery root
   from the previous handoff's rollup.
8. **(decide)** L-333: restamp both companions, or retire the
   critical-path one.
9. **(decide)** L-231 carries two `**Ref:**` blocks, a leftover from its
   merge. Harmless; fold them when the item is next open.

---

Session written September 2026 with Anthropic's Claude Opus 5.
