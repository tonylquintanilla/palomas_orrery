# Opus Session Handoff -- Track 0 Scaffolding, Ready to Build

**Built on `6b8880d41d587eaa42d86fb79ee8be73780e5b0a`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Gallery pinned separately at `61a78c00668573dbff111ec9f10a96b1cd2fdc35`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Verify both HEADs before building; if either moved, trace the delta first.**

**Prepared:** August 7, 2026 by Claude Opus 5, Tony Quintanilla integrator.
**Session:** August 6-7, 2026. Design and record only -- zero source
modules changed.
**Closes:** the feature/constant transport design cycle (two Fable review
rounds).

---

## Read this before anything else

**Two patch scripts were delivered at the end of this session and may or
may not have been run.** Check state before assuming:

- Master plan at `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md` --
  **v17** means `patch_masterplan_v17.py` ran; **v16** means it did not.
- `LEDGER_CONSOLIDATED.md` -- **L-186 and L-187 present** means
  `patch_ledger_fable_review_v2.py` ran; absent means it did not.

If they ran, this handoff describes current state. If not, everything
below is proposal, and the two scripts carry it.

Both scripts are transactional: they verify an MD5 base fingerprint and
every anchor before writing anything, and print `NOTHING WAS WRITTEN` on
any failure. If the base moved they will refuse to run and need
rebuilding, not forcing.

---

## Who you are working for

Tony Quintanilla, PE -- a retired civil and environmental engineer,
artist, and anthropologist. He is not a professional programmer and not a
formally trained astronomer. He builds Paloma's Orrery through
conversational AI collaboration and holds sole commit authority and final
judgment. The codebase's structure and discipline are the product of that
collaboration; do not read code quality as evidence of his personal
programming fluency.

He runs Python by opening a file in VS Code and clicking Run, and works
through GitHub Desktop. Protocol v3.34 makes that a preference where
practical, not a prohibition. Deliver runnable transactional patch
scripts, not diffs or complete-file rewrites.

**Unpack jargon on first use.** This session failed that test repeatedly
-- "vendored pull", "ast", "restructure the store", the section-sign
character -- and Tony had to ask each time. Write "Section 7", not
"\xc2\xa77".

---

## The lesson this session actually taught

Three times, a design premise turned out to be false, and Tony found each
one by asking a plain question rather than by reading code. The pattern
was identical every time: **Claude read the codebase and treated that as
knowing the system.**

1. **"The exporter."** Both the round 1 handoff and Fable's round 1
   review wrote it as though pointing at something live.
   `export_orbit_cache.py` is a dormant Phase 1b seeding tool. Tony:
   "have we discussed the exporter before? i don't recall this." Then:
   "i don't recall an exporter. i am familiar with the nightly fetch.
   that's all."
2. **Derived constants as a complication.** After the exporter fell, this
   session proposed reading the store with `ast` without executing it,
   then found 7 of 45 assignments are derived and wrote that up as a
   defect. Tony: "one is primary and the other is derived. why do we need
   both in constants?" -- and the answer proved the store correct.
   `SOLAR_RADIUS_AU` has 11 consumer files.
3. **That the gallery could not execute the file.** Never tested. Tony:
   "it's just arithmetic in the python code. easy." `constants_new.py`
   imports only numpy and `datetime`; the builder already hard-depends on
   numpy through astroquery. Removing this premise produced the simplest
   design of the three.

The design got simpler each time a premise was removed. Treat that as
diagnostic: elaboration was compensating for an unexamined assumption,
not for real complexity.

---

## Phase 2 is now three tracks, in Tony's ruled order

| Track | What | Exit |
|---|---|---|
| **0** | Constant layer scaffolding (L-181) | One store, provenance as data, derivation, transport working end to end |
| **1** | Provenance batches (L-156) | Batch 2 gas giants verified, on the Track 0 scaffolding |
| **2** | Artifact 2 (Jupiter/Saturn) | Golden artifact locked on verified, sourced, derived values |

**Tony's reasoning, and it is the part to carry:** a golden artifact is
fingerprinted, so locking one on values that are not yet sourced and
derived means redoing the lock rather than editing a number. Scaffolding
first is the cheaper order, not the slower one.

This supersedes the August 5 "clear all batches before Artifact 2"
instruction. Batches still precede the artifact; Track 0 now precedes the
batches. "Track 0" rather than renumbering, because Section 6 already
cites "Phase 2 Track 1, Batch 1 / Batch 2" and existing handoffs use
those numbers.

---

## The transport design, settled in substance

**Fetch-and-import.** Endorsed by Fable round 2. NOT YET RATIFIED by
Tony -- that is decision 1 below.

The nightly builder resolves the orrery HEAD SHA, fetches
`constants_new.py` as text at that SHA, imports it, reads the feature
values and their sources, validates, and writes into staging under the
existing atomic-swap semantics. Python evaluates all derivation natively.

**Tony's workflow does not change.** He edits a constant, commits,
pushes. No exporter, no new file to run, no scheduled job committing into
the repo where he holds sole commit authority.

Why it does not violate the builder's "No orrery imports" rule:
`constants_new.py` is a leaf -- numpy and `datetime`, nothing else. No
Plotly, no shell modules. Update the docstring wording rather than leave
a rule that now reads broader than intended.

### Build requirements from Fable round 2

- **Drop the dead imports.** `numpy` and `timedelta` are imported by
  `constants_new.py` and never used (verified: zero `np.` occurrences).
  The store becomes stdlib-only, removing the version-skew surface
  between environments.
- **Pre-import gate, ~10 lines.** Parse the fetched file with `ast` and
  check exactly two structural properties: imports on an allowlist, and
  no duplicate dict keys. Then hand off to import. This is not a revival
  of ast-extraction -- it reads no values. It recovers the one capability
  fetch-and-import loses: after import Python has already silently kept
  the last duplicate, so the round 1 Phobos finding becomes invisible.
- **`FEATURE_REGISTRY`.** One dict in the store mapping body slug to that
  body's feature entries; the builder reads exactly that name. Every
  rename or regrouping inside the store stays internal. The only breaking
  change left is renaming the registry, which is one grep from impossible
  to miss.
- **Import hygiene.** `importlib.util.spec_from_file_location` from the
  staging path with a per-run module name. Never insert staging into
  `sys.path`.
- **Store docstring rule.** Data-only module, no top-level I/O --
  importing executes top-level code, so a future file write or network
  call would be inherited silently every night.
- **Run manifest** records both the orrery SHA and the content hash of
  the fetched file (`_write_run_manifest`, builder line 1476).

### Four validation layers, each catching a class the others miss

1. Source presence -- an ABORT, not a warning.
2. Unit-sanity RANGE checking. Shape and source-presence validation both
   PASS on a value whose units changed; only magnitude bounds catch a
   km-to-AU slip.
3. Cross-field ring invariant, **`inner <= outer`**.
4. Nightly value-diff against last night's committed copy, logging old,
   new, and both orrery SHAs. The only guard that sees CHANGE itself --
   the L-182 failure family.

**Correction to Fable, verified before recording.** Fable recommended
strict `inner < outer` and stated it catches nothing spurious today. It
would fire on 8 Neptune entries where inner and outer are deliberately
equal -- narrow ringlets modelled at a single radius (Le Verrier at
53,200 km; six Adams arcs at 62,932 km). Its directional claim holds:
`inner > outer` is genuinely zero across all 33 ring pairs. Use `<=`. A
check that fires spuriously on day one is one people learn to ignore.

---

## Tony-action items

### (decide) -- in order of need

1. **Ratify fetch-and-import.** Master plan Section 7 decision 12. Two
   reviewers recommend it; Tony has not ruled.
2. **Pilot slice inside Track 0.** Section 7 decision 16. Fable
   recommends migrating Jupiter (5 entries) through the full Track 0
   treatment and building the transport end-to-end against it, then
   scaling to the remaining 32 -- which needs zero transport rework. The
   argument: the transport cannot be tested against today's store at all,
   since no `source` fields exist for abort-on-missing-source to act on,
   so "transport after Track 0" really means "first end-to-end test after
   all 37 entries move." Jupiter also holds the resistant-prose cases.
   Cost: two passes over the migration tooling.
3. **Interpolation locus.** Section 7 decision 17. Templates plus values
   in the cache with the assembler interpolating at render time, or
   pre-interpolated strings with the builder doing it at build time.
   Fable recommends builder-side. It decides the cache schema, so it is
   decided before the schema is written.
4. **L-179 and L-180 values.** Section 7 decision 14. Solar gravitational
   influence (150,000 vs 126,000 AU) and the solar chromosphere's three
   inconsistent extents. Both are drift inside the store today, and they
   are Track 0's first step -- migrating before they are settled would
   transport a known-inconsistent value into three more
   authoritative-looking places.
5. **Annotation parser ruling.** L-186, Track 1. Three annotations name a
   worksheet `.md` file but append the checked value, e.g.
   `(batch1_tier2_followup_gpt.md: 14.27 Mkm)`. The parser tests that the
   parenthetical ENDS in `.md`, so a richer annotation is rejected for
   carrying more provenance. Strip the values, or extend the pattern?
   Claude's lean is extend; it sits adjacent to "do not loosen a checker
   to clear findings," so the ruling is Tony's.

### (do)

- Run the two patch scripts if not already run, then `ledger_index.py`.
- Nothing else outstanding. Task 2a landed at `5a56473`; the master plan
  v16 pass landed at `2445244`; L-184 and L-185 landed at `ee0da47`.

---

## Ledger state

At `6b8880d`: 180 blocks, 112 live items. After the pending patch: 182
blocks, 114 live items.

| Item | What | Track |
|---|---|---|
| **L-181** | Complete the constant layer -- the Track 0 build | 0 |
| **L-179** | Solar gravitational influence 150,000 vs 126,000 AU | 0, step 1 |
| **L-180** | Solar chromosphere, three inconsistent extents | 0, step 1 |
| **L-185** | Source discipline for assembler constants (~8 sites) + retirement note | independent |
| **L-176** | Illustrated dimensions in hover text | 0 |
| **L-186** | 12 cross-check annotation issues | 1, before Batch 2 |
| **L-177** | Mercury Hill sphere convention | 1 |
| **L-184** | Interactive build-path push gate (2a done, 2b reshaped) | 1 |
| **L-187** | info_dictionary numeric-overlap enumeration | deferred |
| L-154 | JS feature-rendering layer -- does not exist yet | 2 |

---

## Warnings earned this session

- **Reading code is not knowing the system.** Three false premises, three
  plain questions from Tony, three collapses. When a design keeps growing
  machinery, check whether it is compensating for an assumption nobody
  verified.
- **Verify a reviewer's claims before recording them.** Every Fable
  finding across both rounds was checked at the anchors. All held except
  the `inner < outer` operator, which would have shipped 8 false
  positives.
- **Anchors fail on characters, not just content.** The v17 patch failed
  its first run because a heading was typed as "Section 8" where the file
  has "\xc2\xa78". The harness caught it; nothing was written.
- **Dates.** This session recorded rulings as August 6 until Tony's
  question about review numbering surfaced that it was already August 7.
  The session spans both days. Check the clock rather than continuing
  yesterday's date.
- **A nightly build that succeeds proves nothing about feature data.**
  Confirmed live: the 2026-08-06 nightly refreshed vectors, elements and
  positions, and touched neither `objects_config.json` nor
  `feature_configs.json`. Every freshness signal was green.

---

*Handoff prepared August 7, 2026 with Anthropic's Claude Opus 5, built on
`6b8880d41d587eaa42d86fb79ee8be73780e5b0a` at
https://github.com/tonylquintanilla/palomas_orrery and
`61a78c00668573dbff111ec9f10a96b1cd2fdc35` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io*
