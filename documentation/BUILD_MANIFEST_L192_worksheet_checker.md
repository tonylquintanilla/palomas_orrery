# Build Manifest -- The Worksheet Checker (L-192)

**Built on `b22bcf8f39dab375f6b5cf1207826575fdda3415`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
HEAD verified live at session start and unchanged at the time of
writing. Gallery untouched at
`c2202dcc2c4ed210160ce6033b70346aef194b68` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.**

**Type: BUILD.** Two new modules, one patch script for an existing
module. No orrery rendering code touched. Nothing pushed -- Tony holds
commit authority and this has not run on his machine yet.

**Continues from** `documentation/HANDOFF_20260813_L192_rulings.md`
(anchored `6b99ace` / `b22bcf8`).

**Prepared:** August 13, 2026 by Claude Opus 5, Tony Quintanilla
integrator.

---

## The skill obligation from the previous handoff is DISCHARGED

`provenance-discipline` loaded at **2.2**. The manifest row reads 2.2
in the resident protocol AND in `PROJECT_INSTRUCTIONS.md` at HEAD --
checked against the repo as well as the resident copy, because the
resident copy was one version behind on August 12 and would have
produced a false STOP.

The other four skills this build loaded also match their manifest rows:
`agentic-pre-test` 1.2, `safe-file-editing` 1.3,
`ledger-and-session-records` 1.5, `orrery-coding-conventions` 1.3.

Nothing carries forward. No skill was bumped this session.

---

## Deliverables

| File | Status | Lines |
|---|---|---:|
| `worksheet_checker.py` | NEW, repo root | 1397 |
| `test_worksheet_checker.py` | NEW, repo root | 449 |
| `patch_L192_runner.py` | patch for `maintenance_run.py` | 143 |

**Install order.** Copy all three to the repo root. Open
`patch_L192_runner.py` in VS Code and click Run -- it edits
`maintenance_run.py` in place and prints the before and after
fingerprints. Then run `maintenance_run.py` normally. The patch script
is spent after one run and belongs in `documentation/` afterwards, the
same as `patch_L192_attachment.py`.

The patch is transactional: it fingerprints the file, checks both
anchors, and writes nothing if either is missing or duplicated. Run it
twice and the second run says the work is already done.

---

## What it does, in one paragraph

For every cross-check annotation attached to a value the scanner
scores, the checker opens the worksheet that annotation names, finds
the row about that value, and reads what the row actually recorded. Six
layers: the worksheet exists (L0), it belongs to the named checker
(LID), the row is located (L1), the code agrees with the row's evidence
(L2a), the code still equals what the checker read at the time (L2b),
and the verdict amounts to a completed check (L3).

It consumes the scanner's attachment rather than computing a second
one. It does not write, it does not gate the push, and it does not
grade a derivation.

---

## The first run, on a clean clone at `b22bcf8`

    WORKSHEET CHECK: 104 annotations, 3 clean, 39 send back,
                     22 to conversation, 30 not scanner-reachable

| Finding | Layer | Count |
|---|---|---:|
| VALUE_VERDICT_ABSENT | L3 | 46 |
| UNMATCHED | L1 | 25 |
| NO_NUMERIC_CLAIM | L1 | 18 |
| CITATION_DEFECT | L3 | 17 |
| INCOMPLETE_CHECK | L3 | 11 |
| DRIFTED | L2b | 8 |
| CLAIMS_UNADDRESSED | L1 | 4 |
| REFUTED | L3 | 4 |
| DERIVED | L3 | 3 |
| MISMATCH | L2a | 2 |
| UNPAIRED_UNITS | L2a | 2 |
| RANGE | L2a | 2 |
| UNREADABLE_VERDICT | L3 | 2 |
| WORKSHEET_UNREADABLE | L1 | 2 |
| CHECK_NOT_PERFORMED | L3 | 1 |

Findings go to `WORKSHEET_CHECK.md` at the repo root, beside
`PROVENANCE_AUDIT.md`. That placement is a choice, not a ruling, and it
is one line to change.

---

## THE PAYLOAD: four values moved after their check

This is the committed-history failure the tool was opened for, and it
is caught directly rather than inferred. `constants_change_report.py`
cannot see any of it: these edits were committed, so there is nothing
in the diff to notice.

| Constant | The checker read | The code says now |
|---|---:|---:|
| `HELIOPAUSE_RADII` | 26,449 | 26,148 |
| `BENNU_RADIUS_KM` | 0.262 | 0.246 |
| `HAUMEA_RADIUS_KM` | 816 | 715 |
| `ARROKOTH_RADIUS_KM` | 9.95 | 9.1 |

Each carries two annotations, which is why the count is eight.

Two of these are the false attributions already in the ledger, and the
mechanism is now visible: somebody corrected the value against a new
source and the annotation rode along unchanged. **The other two,
`HELIOPAUSE_RADII` and `HAUMEA_RADIUS_KM`, were not on any list.** They
are the same shape and nobody was looking for them.

`BENNU_RADIUS_KM` also comes back `CHECK_NOT_PERFORMED` at L3 -- row
G10 reads UNVERIFIED, "Not checked," while the annotation credits a
completed cross-check. Both known-true failures land, exactly as the
sequencing ruling intended: the first run catches them, and the catch
is what routes them.

---

## The corpus is 104 checkable annotations, not 134

The 134 figure counts annotation LINES. **30 of them are attached to
code the scanner does not score as a unit**, so they grant no credit
and this tool cannot check them:

- Four are the known orphans in `constants_new.py` (145-146, 316-317).
- The rest sit on code that never becomes a unit: `CORE_AU` and
  `RADIATIVE_ZONE_AU` (products of two names), `moon_inner_core_info`
  and its siblings (module-level strings the scanner does not reach),
  and dict keys in `shell_configs.py`.

That is **L-190** -- scanner reach -- not a defect here. The checker
prints the full list every run rather than letting it stay silent, and
the test suite fails if the count reaches zero, since zero could mean
either that the scanner started reaching them or that somebody stopped
collecting them.

---

## Three design corrections, all made by running it against real data

Each of these was a confident first pass that the corpus refuted. They
are recorded because the pattern matters more than the fixes.

**1. The constants worksheets have no value verdict at all.** Their
schema is `| # | Constant | Value | Cited source | Citation correct? |
Notes |`. The first version read that column as a value verdict and
reported twenty refuted values. That is precisely the conflation the
two-column schema exists to prevent: a right number under a wrong
authority is value-YES and citation-NO. Verdict tokens now carry a
SCOPE, and a citation verdict can never produce a value refutation.
This is the source of the 46 `VALUE_VERDICT_ABSENT` findings -- the
largest number in the report, and see the open decision below.

**2. Display strings do not match one row.** The worksheets record one
row per CLAIM, and a paragraph about Eris's crust states several.
Matching a string to a single row picks one claim and silently passes
the rest. The string path now checks every numeric claim and reports
the fraction addressed: **19 of 73** across the corpus.

**3. "Not checked" is not "the source does not publish it."** The
first version collapsed both into one class, which reported Bennu's
"Not checked" row as a citation defect -- blaming the source for work
that was never done. `UNVERIFIED` and `NOT CHECKED` now mean nobody
looked and route to SEND BACK; `NOT FOUND` and `UNSOURCED` mean
somebody looked and the source lacks it, and route to CONVERSATION.

A fourth, smaller: the orrery writes operating instructions into the
same string as the science -- a manual scale to set, a frame weight to
expect. Those are numbers no worksheet row could ever address, so
counting them inflates the denominator with claims that cannot be
answered even in principle. **27 are excluded and counted.**

---

## What it cannot see, printed every run

- The 30 annotation lines outside scanner reach, listed by file and
  line (L-190).
- 15 worksheet columns the header registry does not recognise, listed
  by file, line, and column name. All fifteen are auxiliary tables --
  basis comparisons, a tally, a two-source quantity table. None is a
  row table being missed, which is what makes the residue small enough
  to read.
- The eighteen inline literals duplicating cited constants. No
  worksheet names them, so they are outside these bounds by
  construction (do-item 4).
- Derivation arithmetic. A DERIVED row is routed, never graded.

---

## Verification

- `py_compile` clean on all three files.
- `test_worksheet_checker.py`: **46 of 46 checks pass.** Every layer is
  exercised twice, once with evidence that clears it and once with an
  injected violation that must not. The identity check reports zero
  mismatches across the whole corpus, and zero is what a broken
  identity check also reports, so the injected Gemini-over-a-Claude-
  worksheet case is what proves it works.
- The suite also pins the four DRIFTED constants and Bennu's L3
  finding against the live corpus, so a refactor that stops finding
  them goes red rather than changing a number quietly.
- Full `maintenance_run.py` executed with the patch applied. The two
  new rows read as intended.
- `provenance_scanner.py` run after the change: **Tier-1 +0, no file's
  Tier-1 count rose.** `worksheet_checker.py` adds three Tier-3
  findings, all tuning constants in a devtool.
- Everything above ran on THROWAWAY copies of the repo. The delivered
  files were never edited by a test.

Two pre-existing checker failures appear in the maintenance run --
`test_reset_completeness.py` and `test_orbit_cache.py` -- and both are
sandbox artifacts: no `astroquery` and no `tkinter` in the container.
Neither is caused by this change and neither should appear on Windows.

---

## Method note: a compile check passed on a file missing 204 lines

Worth recording because it happened during this build, roughly thirty
minutes after the same gate was written into the module's docstring.

An over-broad slice in an editing script deleted `Claim`,
`collect_claims`, `identity_token`, and `check_claim` -- 204 lines --
and `py_compile` reported success. What remained was syntactically
perfect and functionally hollow. The recovery point was the throwaway
sandbox copy, which is the only reason it cost minutes.

The fix was a guard that asserts the expected function set is still
present after every edit, run alongside `py_compile`. That is the
gate's own prescription: `py_compile` verifies that the file parses,
never that the file still contains what it is supposed to contain, and
a green result from it cannot distinguish the two.

---

## (decide) -- one new item, and it is the biggest number in the report

**Do the 46 citation-only annotations count as legs toward the
cross-checked rung?**

Every annotation on `constants_new.py` names a worksheet whose only
verdict column is `Citation correct?`. Those worksheets asked whether
the cited source publishes the value, and answered. That is a real
check and a completed one -- but it is not the same claim as "this
value is right," and the annotation asserts a cross-check without
saying which kind.

The checker deliberately does neither thing on its own: it reports the
class, names which column it read, and promotes nothing. **46 of 104
annotations sit here**, so the ruling moves the audit more than any
other single decision available.

The three existing (decide) items on Tier-3 constants now have three
more of exactly the same kind -- `MIN_PROSE_FRAGMENT`,
`INSTRUCTION_LOOKBACK`, `INSTRUCTION_LOOKAHEAD` in this module. Same
question, same low stakes; fold them into that one rather than opening
a handle.

---

## Next session

**Settle do-item 6 with the checker in hand.** The fork-4 ruling put
this checker in the runner with a denominator on its summary line; the
provenance scanner still discards its full output on every passing run,
including the L-189 delta that is already built. Two candidate fixes
were sketched last session and neither chosen. The checker's own output
shape is now a worked example to argue from.

**Then the backfill of the 27**, verdict-gated. The checker now names
which rows can carry it, and the report is the queue.

Not folded in and still open: the `(do)` on Pluto's reader-facing Hill
sphere text, and the five other `(decide)` items carried from the
previous handoff.

---

*Build manifest prepared August 2026 with Anthropic's Claude Opus 5.
Built on `b22bcf8f39dab375f6b5cf1207826575fdda3415` at
https://github.com/tonylquintanilla/palomas_orrery. Nothing pushed;
the anchor is the base, not a result.*
