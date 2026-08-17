# Handoff addendum -- 2026-08-16b -- the pipeline framing, and what patches 6 and 7 need

**Built on `227f5b2d6763baa384c090a911c2c5ced64f4a4d` at
https://github.com/tonylquintanilla/palomas_orrery (branch main);
gallery at `3d10739b097e2b63395cf58742873cf378210e68`.** Both confirmed
by live `git ls-remote`. Nothing pushed after `227f5b2` at the time of
writing.

Lands in `documentation/`.

**This is an ADDENDUM, not a replacement.**
`HANDOFF_20260816_review_and_chromosphere.md` is the record of the first
half and stays exactly as written -- including its anchor at `f4043bf`,
which was correct when it was written. Where the two disagree on a SHA,
this one is later.

---

## Read this first if you are the next session

The previous handoff was written before the second half of the session
and does not know about any of it. Three corrections to what it says:

1. **Its "regenerate stage 2 fingerprints against `f4043bf`" should read
   `227f5b2`.** Verify against live HEAD rather than either.
2. **Two patch scripts exist that it does not mention** --
   `patch_L196_6_master_plan_section_5a.py` and
   `patch_L196_7_summary_current.py`. If HEAD is still `227f5b2`, they
   have not been run.
3. **A document has to land before those patches are pushed.** See the
   next section. This is a blocker, not a nicety.

---

## BLOCKER: `CRITICAL_PATH_SUMMARY.md` must land first

Both patch 6 and patch 7 write text citing
`documentation/CRITICAL_PATH_SUMMARY.md` by name as a companion
document. That file was delivered to Tony as a download during the
session and has no patch landing it in the repo, because it is a NEW
file and needs none -- it just has to be saved.

If patches 6 and 7 are run and pushed without it, two documents in the
repo cite a file that does not exist. That is
cite-to-nonexistent-authority, and it is the THIRD instance in this one
session: the same shape as the `orrery-coding-conventions` v1.4 file
that was filed in `documentation/` while two pushed source comments
cited the 20-degree rule it contained.

Order, therefore:

1. Save `CRITICAL_PATH_SUMMARY.md` to `documentation/`.
2. Run `patch_L196_6_master_plan_section_5a.py` from the repo root.
3. Run `patch_L196_7_summary_current.py` from the repo root.
4. `maintenance_run.py`, commit, push.

Both patches are fingerprinted against `227f5b2` and abort with nothing
written if the base has moved.

**Root cause, recorded because it recurred three times in one day.** A
deliverable was named for the convenience of the download rather than
for its destination, and its destination was stated in conversation
instead of in the file. Both corrected: the file now opens with
`Lands in documentation/ as CRITICAL_PATH_SUMMARY.md`, and skill files
now ship inside a folder named for where they go.

---

## The conceptual output, which exists nowhere in the repo yet

This is the part most worth carrying, and it is not in any pushed file
until patch 6 runs.

**Tony's framing, 2026-08-16: the provenance refactor is not a leg
beside the assembler work. It precedes it, because its target is the
ORRERY.**

The assembler creates no data. It imports. So there is no point
downstream of the orrery where a wrong constant can be caught -- not in
the nightly builder, not in the resolver, not in the browser.

That splits the data into two kinds that behave completely differently,
and the distinction was verified against the builder's own source:

- **Ephemerides** are re-fetched from JPL Horizons every night.
  Provenance by construction; a bad value cannot survive a rebuild.
- **Feature constants** -- ring radii, belt distances, shell bounds --
  originate in the orrery's Python and reach the gallery **by hand
  copy** into `gallery/data/objects_config.json`. The builder's own
  docstring says so: *"No orrery imports; hard-won fetch specifics are
  COPIED WITH PROVENANCE from the orrery and kept in sync on change."*
  Horizons is never consulted for them. An error in the orrery becomes
  a permanent, silent error in the gallery.

Two consequences the plan did not previously state. Making the orrery
right is segment one. Making the COPY faithful is segment two, and it is
why Track 0 carries a cross-repo transport rather than just a registry
-- a correct orrery is not sufficient while `objects_config.json` is
maintained by hand.

---

## Measured this session, about Artifact 2

Verified at gallery HEAD `3d10739`, not relayed from the ledger.

**The served data is already complete.** `feature_configs.json` carries
Saturn's seven rings (D through E, inner and outer radii), Jupiter's
four rings with thickness, Jupiter's radiation belts (`belt_distances`,
`belt_thickness`, `n_rings`, `n_points`), and Earth's atmosphere shell
and Van Allen belts. Twelve objects in `coverage_index.json`. The
"roughly 23 values" figure from earlier sessions was about PROVENANCE,
not presence.

**The render gap is two lines and a type, then a real build.**
`resolver.py:133` reads `features = tuple(rec.get("features") or ())`,
which reduces a feature dict to its keys, with `models.py:91` typing the
field `Tuple[str, ...]` to match. A `params` field already flows through
`assemble.py`. Then L-154: **zero** references to `feature_configs.json`,
`ring_system`, `radiation_belts` or `van_allen` in any JS or HTML in the
gallery repo. The builder writes the file and nothing reads it.

**Artifact 1 proved the orbit path and exercised no features**, which is
how the feature path stayed broken while everything around it worked.

---

## What patches 6 and 7 change

**Patch 6 -- Section 5a rewritten as the critical path.** The old
section was an execution map that had drifted: it called Artifact 2
BLOCKED, which Section 6 of the same document amended on 2026-08-08; it
reported scanner Tier-1 at 210 and provenance-discipline at v1.4 against
a live 206 and 2.3; and its NEXT named work L-192 superseded. The new
section carries the end goal, the one-way pipeline, five segments, and a
"you are here" table. A guard asserted every changed line fell inside
the section bounds before the patch was cut.

**Patch 7 -- the readable snapshot brought current**, 514 to 624 lines.
Its motivating addition is a new section, **WHAT CLAUDE CHECKS BEFORE
ANYTHING ELSE**, written on Tony's instruction so he can track what the
session gate tracks. It lists all five checks, explains the two limits
on the skill gate, and states what Tony can do with the list.

One passage is deliberately left uncorrected: the old tail says the
checker "is designed and reviewed and NOT built." A bracketed note
records that both halves are since done and the original wording stays,
because correcting it would falsify the record.

---

## Still true from the first handoff

The obligation is unchanged and undischarged:

> `safe-file-editing` and `orrery-coding-conventions` both went 1.3 ->
> 1.4 on August 16. The session that bumped them loaded 1.3. **The next
> session confirms its loaded copies read 1.4 against the manifest
> before any patch-script or marker work.**

Verified present in the repo at `227f5b2`: both `skills/` copies read
1.4 and the manifest zone agrees.

The nine blockers, the open decisions, and the build queue are all in
the first handoff and unchanged. The build order there still holds, with
one clarification this session added: **the builder marker join goes
first**, because 96 continuation markers are placed in seven files and
the builder does not know they exist, so the largest blocker is still
live at HEAD.

---

## Order for the next session

1. Confirm both skills load at 1.4.
2. Save `CRITICAL_PATH_SUMMARY.md` to `documentation/`, then run
   patches 6 and 7, then push.
3. Builder marker join + loud failure.
4. Stage 2 markers, Shape A swaps, ordinal window, token list.
5. Ledger entries L-194 through L-196 and the L-192 as-built.

The resolver fix (L-154, two lines and a type) is independent of all of
the above and can be taken at any point. It is the smallest piece of
work standing between the project and a Saturn that renders -- but a
golden artifact locked on unsourced values means redoing the lock, so
rendering early is for looking, not for locking.

---

*Prepared August 16, 2026 with Anthropic's Claude Opus 5. Built on
`227f5b2d6763baa384c090a911c2c5ced64f4a4d` at
https://github.com/tonylquintanilla/palomas_orrery.*
