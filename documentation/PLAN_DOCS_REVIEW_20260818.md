# Plan-document review -- what is stale at HEAD

**Built on `b65ac115fc0f820e8270c0807249813c67bde7bc` at
https://github.com/tonylquintanilla/palomas_orrery (branch main); gallery
at `ff18d3e6fa31f70a8f525df471e751d046cf14fa`.** Both confirmed by live
`git ls-remote`.

Type: **REVIEW.** Nothing here is built. Every number below was measured
at HEAD, not recalled.

Lands in `documentation/`.

---

## The three documents and how far each has drifted

All three were written on August 16 and anchored at `227f5b2d`. Nine
commits and two working days have passed. They have NOT drifted equally,
and the difference matters for how much work each needs.

| Document | Lines | What it claims to answer | State |
|---|---|---|---|
| `CRITICAL_PATH_SUMMARY.md` | 155 | how far to the end | **Structurally sound.** Four numbers stale, no reasoning wrong. |
| `MASTER_PLAN_INTERACTIVE_GALLERY_SUMMARY.md` | 623 | what is tracked right now | **Substantially stale.** It is the "right now" document and right now has moved. |
| `MASTER_PLAN_INTERACTIVE_GALLERY.md` | 2009 | the shape of the work | **Largely current.** It describes design, and the design has not changed. |

That split is the finding. The reference document ages slowly by
construction; the snapshot ages fastest because its whole job is to be
current. A snapshot that is two days stale is not a small version of a
correct document -- it is actively misleading about what is left to do.

---

## 1. CRITICAL_PATH_SUMMARY.md -- four numbers

Everything structural still holds: the end goal, the one-way pipeline,
the five segments, and the reasoning about why provenance comes first.
Do not rewrite it. Correct these.

**The anchor.** Header and footer both name `227f5b2d` and gallery
`3d10739b`. Now `b65ac115` and `ff18d3e6`.

**The routing figures, quoted twice.** "102 claims scored, three of them
clean" and "Of 102 verification claims, three are clean, forty need to
go back ... nineteen need a conversation, and forty are recorded without
a route."

Measured at HEAD: **110 rows, 8 clean, 68 routed** -- 48 SEND BACK, 20
CONVERSATION, 34 noted, 24 not scanner-reachable.

The clean count nearly tripled and the corpus grew by eight. Both are
real and both are explained by L-198: the scanner learned to read units
it previously could not see, so claims that were invisible entered the
corpus, and rows that were mis-parsed resolved.

**"One of the nine has since been closed by a design decision."** Of the
nine blockers, one remains -- blocker 7, the ordinal context window --
and it is deliberately not exercised by the pilot, since constants carry
no ordinals.

**"Step one is in progress."** Still true, but the sentence under it --
"the checker, the worksheet builder and the dispatch loop are the
machinery of this step" -- now describes finished machinery. The loop
runs end to end as of today. What is unstarted is the dispatch itself.

---

## 2. MASTER_PLAN_INTERACTIVE_GALLERY_SUMMARY.md -- the real work

### 2a. Things stated as pending that are done

- **"The next session opens with the builder-side marker join ... 45 of
  65 dispatch rows showing a truncated citation -- is still live."**
  Done. L-196 closed; 153 continuations join on every build.
- **Six Shape A citation swaps (L-195), "ruled, NOT built."** Built --
  seven, taking `OUTER_CORONA_RADII` in passing. L-195 is DONE.
- **"Print the seven verdict tokens in the request."** Done, read from
  `worksheet_checker.VERDICT_TOKENS` rather than retyped.
- **"Ledger entries for L-194, L-195, L-196 and the L-192 as-built --
  not yet written."** Written.
- **The skill obligation** naming `safe-file-editing` and
  `orrery-coding-conventions` at 1.3 -> 1.4. Discharged. The obligation
  that replaces it is `provenance-discipline` 2.3 -> 2.4.
- **"provenance-discipline is at v2.3."** 2.4.
- **"Protocol at v3.40 (August 16)."** v3.41 once `patch_L199_1` runs.

### 2b. The scanner section is the most wrong, and interestingly so

It reports 880 findings and **Tier 1 = 206**, measured August 7 and
re-measured unchanged on August 16.

Measured at HEAD: **1025 findings, Tier 1 = 289.**

That is +83 Tier-1 findings in two days, and the document's own logic
says this should not happen -- it argues Tier 1 held steady because
"neither added or removed a claim about the world." Both statements are
correct. The population changed, not the world: L-198 taught the scanner
units it could not previously see, so claims that were always there
became visible and countable.

This is worth writing INTO the document rather than just correcting the
number, because a reader who remembers 206 and sees 289 will otherwise
read it as regression.

The domain table is stale in both directions:

| Domain | Doc says | Measured at HEAD |
|---|---:|---:|
| Earth System | 105 | 150 |
| Orrery | 91 | 125 |
| Stars | 9 | 12 |
| Utilities | 1 | 2 |
| Dev Tools | 0 | 0 |
| Gallery | 0 | 0 |

The Artifact-2 per-file table has moved too -- `shell_configs.py` 23 ->
**35**, `idealized_orbits.py` 26 -> **29**, others unchanged; the total
goes 56 -> **71**. The paragraph under it still holds: the gas giant
shells remain nearly clean at two findings across four files, and the
critical path is still tractable across eight named files.

### 2c. The tracked list needs rebuilding

"WHAT IS TRACKED RIGHT NOW -- 2026-08-16" is the section with the
shortest half-life and it is now mostly false. What it should say:

**Ready to build, no ruling outstanding**
- Resolver + models fix (L-154). Unchanged, and now the only item on
  this list -- worth noting, because it has been sitting behind
  provenance work for weeks and is independent of all of it.
- Blocker 7, the ordinal context window.

**Waiting on a ruling** (unchanged from August 16)
- The lazy responder; claim typing; cross-worksheet disagreement; what
  UNKNOWN does; pluto 614/638; transition sequencing; whether batching
  becomes real.
- New: the `<batch>`-as-filename reading in the Resolved leg.

**Unstarted, unblocked**
- The pilot dispatch itself. 23 rows, expected dispositions written.

**Carried as an obligation**
- Confirm `provenance-discipline` loads at 2.4 before provenance work.

### 2d. Ledger items by track

The track list stops at L-196. Missing entirely: L-197 through L-205,
which is nine handles including everything the dispatch loop needed.
L-192's line still reads "DISPATCH not finished -- see the nine
blockers"; eight of nine are closed.

### 2e. One item to leave alone

The bracketed note under the August 12-13 section -- "[Both since done
... Left as written because it is the record of what was true then]" --
is the right pattern and should be used for 2a rather than deleting
those lines. A snapshot that silently overwrites its own history stops
being evidence of anything.

---

## 3. MASTER_PLAN_INTERACTIVE_GALLERY.md -- one correction, and it is not what the summary predicted

The summary lists four documents that still describe the nightly Task
Scheduler job as live, and names this file's line 40 as one of them.

**Measured: that is already fixed.** Line 40 states the retirement,
dated, with Tony's reasoning. The correction landed and the summary's
to-do list was never updated -- so the summary is now stale about
another document's staleness.

Of the four sites the summary names:

| Site | State at HEAD |
|---|---|
| `MASTER_PLAN_INTERACTIVE_GALLERY.md:40` | **fixed** |
| `documentation/TESTING_PROTOCOL.md:292` | **still live** -- Layer 3 still says "enable the nightly Task Scheduler job" |
| `skills/gallery-cache-builder/SKILL.md:70` | line has moved; needs a look rather than a line number |
| ledger near 4555 | needs a look |

The TESTING_PROTOCOL one matters more than the others, because a testing
protocol is read at the moment of doing the thing it describes. It tells
a reader to enable a schedule that was deliberately retired.

Otherwise the plan is current. Section 5a carries the pipeline framing
and has not been overtaken. Its anchor line needs the same SHA update as
the other two.

---

## Recommended order

1. **`CRITICAL_PATH_SUMMARY.md`** -- four numbers and the anchor. Fastest
   and it is the document most likely to be read by someone outside the
   work.
2. **`TESTING_PROTOCOL.md` Layer 3** -- one paragraph, and it is the only
   correction here that could cause a wrong action rather than a wrong
   impression.
3. **The summary** -- the real rewrite. Sections 2a through 2d.
4. **The plan** -- anchor only, unless Section 5a should record that the
   dispatch machinery is now complete.

---

*Prepared August 18, 2026 with Anthropic's Claude Opus 5. Built on
`b65ac115fc0f820e8270c0807249813c67bde7bc`.*
