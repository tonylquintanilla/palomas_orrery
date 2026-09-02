# HANDOFF -- 2026-09-01: the maintenance session

**Built on** orrery `df80c35803ce916dafe6b84844d95181e43e5edd` at
https://github.com/tonylquintanilla/palomas_orrery (branch main),
gallery `54c8352f52b011f50295b2afbd9e187db19d73cc` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Both confirmed against the live remote at session end.

**Type:** BUILD. Ten patches ran and were pushed. Nothing is left
waiting on Tony's machine. Two ledger items opened, three closed.

---

## Confirm this first

Both repo HEADs against the anchors above.

Then, before work of the matching kind:

- `safe-file-editing` reads **1.10**, `ledger-and-session-records`
  **1.9**, `provenance-discipline` **2.10**, `gallery-cache-builder`
  **1.4**. All four loaded and matched the manifest during this session.
  The check is load-triggered, so it does not carry.
- **No skill was bumped this session.** The v3.50 and v3.51 obligations
  are discharged: `safe-file-editing` loaded at 1.10 and
  `orrery-coding-conventions` is not implicated in any of tonight's work.
  Nothing new is owed.

---

## What ran and was pushed

Ten patches, in the order they ran.

**`patch_L270_1_readme_rewrite.py`** (orrery) -- README.md rewritten
around two purposes. Prior version archived at
`documentation/README_archived_20260831.md`.

**`patch_L270_2_ledger_close_and_open.py`** (orrery) -- L-270 closed,
L-272 and L-273 opened.

**`patch_L272_1_gallery_readme.py`** (gallery) -- the gallery repo's
first README.

**`patch_L274_1_sibling_sweep.py`** (gallery) -- the sibling sweep ages
by the run id in the directory NAME, not by mtime. Plus
`documentation/check_cache_siblings.py`, a report-only runner row, and
eight test pins (149 checks -> 158).

**`patch_L274_2_ledger_sibling_sweep.py`** (orrery) -- L-274 opened.

**`patch_L274_3_readonly_rmtree.py`** (gallery) -- `_rmtree_force` at all
three deletion sites. This is the one that actually fixed it.

**`patch_L273_1_doc_index.py`** (orrery) -- `doc_index.py`, the README
marker zone, eight document tags, and a fifth generator row.

**`patch_L274_4_close_and_amend.py`** (orrery) -- L-274 amended and
closed, L-272 closed, L-273 amended.

**`patch_L273_2_dashboard_doc_index.py`** (orrery) -- Document Index in
the dashboard, and two stale counts removed.

**`patch_L275_1_gallery_dashboard_entries.py`** (orrery) -- two gallery
entries in the dashboard, L-275 opened.

Also delivered and run but not part of the repo:
`diag_L274_why_denied.py`, a read-only attribute diagnostic. It served
its purpose and can be deleted.

---

## Ledger state at session end

| Handle | State | What |
|---|---|---|
| L-270 | DONE | README.md rewritten |
| L-272 | DONE | gallery repo README |
| L-274 | DONE | the sibling sweep, both bugs |
| L-273 | OPEN | doc indexer -- built for 8 of 13 documents |
| L-275 | OPEN | dashboard cannot launch a Node tool |

---

## The decisions Tony made

**The README's original purpose is largely moot.** Describing the
project and how to access the Python is no longer the job, because the
galleries carry the work to everyone who is not the developer. Two
purposes replace it: what Paloma's Orrery is and where to find the
documents describing it, and how the codebase is kept correct. The file
is now organised as those two parts.

**The feature catalogue collapses to prose.** About fifty lines of
bullets became one paragraph ending in a pointer to MODULE_INDEX.md --
the middle option, against cutting it entirely.

**An indexer, not a checker.** Claude proposed a checker that fails when
the README's document table and the root document set disagree, and
recommended it. Tony proposed the third thing: an indexer writing into
the README in place, the way `skills_index.py` writes the manifest into
the protocol. It is better and it dissolves Claude's own objection --
the checker left the duplication in place and only made it loud, which
is the opposite of this project's fix-the-producer rule.

**Run the README patches now; build the indexer separately.** Against
holding the rewrite to ship one clean pass. The accepted cost was
editing README.md twice in two days.

**Take the two Python dashboard entries now, defer the Node three.** The
launcher change sits under every button in the dashboard and the file had
just been committed.

---

## What was found, and what each one teaches

**The sibling sweep was TWO independent bugs stacked, and the first
diagnosis said one.** The age test selected nothing, because mtime is
meaningless here -- a rename preserves it and OneDrive refreshes it.
Underneath that, invisible until the first was fixed, the deletion could
never have worked either: Windows refuses to DELETE a read-only directory
and happily RENAMES one, and every directory in the served tree carries
that attribute. The builder renames the live tree and deletes the
siblings. Same attribute, opposite outcome.

Fixing either alone would have changed nothing on screen. That is why
patch 1 appeared to make things worse -- 70 directories suddenly
reported unremovable -- when it had in fact given a six-week silence its
first voice.

**The mechanism was producing garbage it structurally could not
collect.** `.prev` could not be deleted, so the swap quarantined it; the
quarantine could not be deleted either. Fixing the delete did not just
clear 70 directories, it switched off the thing making them. No new
quarantine was minted on the confirming run.

**A diagnostic can return the right data with a conclusion that cannot
fail.** The attribute probe printed READONLY IS THE CAUSE while its own
instruction -- compare the control row against the stale rows -- showed
every row identical, live directory included. It tested for the flag
being PRESENT, not for what DIFFERED. Shipping a fix on that verdict
would have looked like a diagnosis and been a guess. What settled it was
reading the deletion sites against the rename sites.

**An estimate from a partial view is the enumerate-first failure in
miniature.** Claude said to expect about fifteen directories. It was 73,
including twenty-three `.staging_*` going back to July 11 that were never
mentioned -- estimated from a screenshot instead of asking for a full
listing.

**Two counts in the dashboard went stale within a day of being written**
-- "the four generated documents" (five now) and "the 149-check cache
builder suite" (158 now). Both were removed rather than corrected. A
count in a tool description is a hand-maintained copy of something the
tool reports accurately at run time.

**It is three document kinds, not two.** The kind the two-way split had
no room for is the one most likely to be mishandled: ZONED, hand-written
prose around a marker zone a tool rewrites. README.md,
PROJECT_INSTRUCTIONS.md and LEDGER_CONSOLIDATED.md are all zoned.

**Two gallery runner rows must never get a dashboard button.** `Served
reachability` and `Store drift` are in-process functions with no file to
launch. Recorded in L-275 as a ruling so a later session counting nine
against seven does not read it as a gap.

**Four checks written this session failed first on Claude's own errors**
-- a miscounted call site, a wrong expected age, a search string that
spanned a line wrap, and an escaping mistake. That is the only evidence
any of them could fail at all.

---

## Tony-action list

- **(do)** Delete `data/objects_config.json.bak` from the gallery repo by
  hand. L-271's widened ignore rule now hides it from git permanently,
  which is exactly the hazard that item was about.
- **(do)** Mode 5 on the Sun drawer, Stage A, on a phone. **This has not
  been reported and it gates Stage B.** Portrait is the check that
  matters: the Sun must not be covered by anything.
- **(do)** Replace the 22 placeholder `info_url` links (L-265). Still
  open from the prior session.
- **(do)** Say whether the `hovermode: false` fix cures the hover seize.
  That answer exists only on your machine, and it is still outstanding
  from the prior session.
- **(decide)** Whether `MASTER_PLAN_INTERACTIVE_GALLERY.md`'s two stale
  NEXT statements get their own pass. Both describe
  `gallery/feature_renderers.js` as unbuilt; it shipped 2026-08-29.
- **(decide)** L-268's order: the braid, or all sixteen with a harness.
- **(decide)** Which shape the dead-link check takes (L-266).

---

## What the next session should build

**Stage B of the Sun GUI, and not before Stage A has been seen on a
phone.**

B splits the drawer row -- the box draws, everything else moves the
camera -- and adds the focus label and cross-marker navigation. It is
also where `SUN_HALF_RANGE_AU` stops being a floor. That floor is
CORRECT today, because the frame only ever widens from a fixed arrival
view; it becomes wrong the moment the frame follows a chosen object.
Fifteen of the eighteen shells are smaller than 0.25 AU, so getting that
order wrong swallows them whole.

B rebuilds the rows Stage A creates. If Stage A needs anything changed
once Tony has seen it, B's anchors move.

Stage C, the i panel, is blocked until the 22 curated links exist.

**Not before Stage B**, but ready when wanted: L-273's generator half is
one line in each of `module_atlas.py`, `data_inventory.py`,
`provenance_scanner.py` and `worksheet_checker.py`, and the same tool
with a different scan root for the gallery README. L-275's launcher
change is small but sits under every dashboard button.

---

*Session written September 1, 2026 with Anthropic's Claude Opus 5. Built
on orrery `df80c358`, gallery `54c8352f`; both confirmed against the live
remote. Ten patches ran and were pushed; none are waiting.*
