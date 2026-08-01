# Ledger note -- D8.5 closed, Option A retired (paste-ready)

Built on `adc9b20d2e6533c25544d565430336f835e87a48`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

One block, appended to **L-156**. It closes D8.5. Run `ledger_index.py`
afterward. Does not set `status:DONE` on L-156 itself -- Phase 1's
sourcing work remains.

---

## Block 1 -- append inside L-156

```
Note (2026-08-01, D8.5 CLOSED -- Option A retired): Prompt anchored adc9b20d,
matched live HEAD, no drift. Delivered patch_retire_option_a.py, uncommitted:
13 anchored edits across provenance_scanner.py and test_provenance_1d.py,
all-or-nothing across both, MD5 guard per file, idempotent refusal naming the
cause per file. Baseline this session reads 879 findings across 116 files, not
881/123 -- the patch scripts were moved out of the repo root at b813aa6, which
closes the self-scan floating item raised in the bleed-fix note.

MEASURED: Tier 1 171 -> 210 (+39), Tier 2 644 -> 605 (-39), Tier 3 62 and Tier 4
2 unchanged, total 879 conserved. 39 findings enter Tier 1, none leave -- the
same findings, scored correctly for the first time. Each removal isolated rather
than attributing one diff to two causes: Option A alone 171 -> 194 (+23), then
stale credit 194 -> 210 (+16).

PREDICTION MISS, recorded rather than smoothed over. I predicted +23 before
building. That was exactly right for Option A but missed the second mechanism's
interaction: I scored the stale-credited findings in isolation and read them as
staying in Tier 2, without accounting for those that are also C_PUBLIC display
strings, which land at 16 once vulnerability moves to V4. Direction right,
magnitude off by 70 percent. Also: the build prompt's "18 display strings Option
A credits" is low; the true figure is 26. That number predates 1d -- adding
Fahrenheit/Celsius recognition created new numeric claims in the climate modules,
some of which then matched pinned values and became newly eligible for Option A
credit. Of the 26, two are suppressed and one stays in Tier 2 (criticality not
public), leaving 23 that move.

KEPT, against the prompt's conditional instruction, after tracing every
reference. build_pinned_values() and its call site STAY: Option A was not its
only consumer. scan_shadow_constants() takes pinned_values and uses it to detect
DERIVED shadow constants -- expressions like 695700.0 / 149597870.7 built from
pinned literals. Removing it would have silently broken the shadow-constant
detector 1d added, and the breakage would not have appeared in any tier count.
test_pinned_values_still_feeds_the_shadow_detector now pins that dependency.
What did change: pinned_values feeds a diagnostic only and never reaches a
score, which is the advisory-not-exculpatory distinction the prompt's own
reasoning draws. Block-citation inheritance (1c) also kept and explicitly
guarded by test_block_inheritance_still_earns_v_sourced -- it is NOT the same
failure class, since an inheriting string carries a citation a person actually
wrote about the block it sits in. Real provenance one level up, not provenance
nobody wrote.

THE AUDIT FOUND A SECOND INSTANCE, and it is worse than Option A. Four lines
below it in the same function: "elif stale: unit.vuln = V_SOURCED;
unit.vuln_reason = 'No source, contains date-sensitive claims'". A unit with NO
citation at all scored V_SOURCED whenever its text matched a staleness pattern
(as of 2024 / Planned / Expected / Still active / Currently operating). Read the
reason against the score it assigns: the scanner states there is no source and
scores it as though there were, in the same breath. The logic also runs
backwards -- a staleness marker is evidence a claim will EXPIRE, so it makes a
claim more vulnerable over time, not less; if it moved the score at all it
should move it the other way. 15 findings were credited this way, in
shell_configs.py (4), scenarios_western_heatwave_march_2026.py (3),
solar_visualization_shells.py (3), info_dictionary.py (2), and one each in
comet_visualization_shells.py, eris_visualization_shells.py and
idealized_orbits.py. Removed in the same patch -- same defect, and leaving it
would have meant closing D8.5 with the failure class still live. Staleness is
still DETECTED and still carried in the reason string ("No source citation;
date-sensitive (recalled)"), so no signal is lost; it simply no longer
substitutes for a citation.

WHY BOTH EXISTED: both predate the D3 ladder. When they were written V_SOURCED
meant something looser than "a citation exists." After 1b landed the four-rung
ladder it means "cited, never independently cross-checked," and neither
mechanism can claim the first half of that. They were not wrong when written;
they were outlived by a definition change and never revisited. Worth carrying as
a general lesson: when a scoring DEFINITION changes, every mechanism that
assigns that score needs re-reading, not just the ones the change was aimed at.

REST OF THE AUDIT IS CLEAN. Traced every path that can set unit.vuln. Three
remain, all requiring a citation a person wrote: has_citation() on the unit's own
context; the docstring-prose patterns (a format allowance for docstrings, not a
substitute for sourcing); and 1c block inheritance. Suppression and accepted
residuals checked separately -- they filter which findings are REPORTED and never
touch a score, which is the correct separation. No other mechanism improves a
vulnerability score without a real citation present. Answering the prompt's
question directly: Option A was not the only instance of this failure class, but
after this patch there are none left.

Tests: test_provenance_1d.py 20 -> 27, the seven additions mostly negatives
(numeric match earns nothing, staleness earns nothing, staleness still detected
and still in the reason, real citations still credited, block inheritance still
credited, score_unit no longer accepts pinned_values as a signature-level guard,
build_pinned_values still feeds the shadow detector). test_citation_inheritance
20/20 and test_constants_provenance 73/73 unchanged; no existing test asserted
Option A behaviour, so none needed updating. py_compile, ASCII/LF gates,
idempotency all pass from a clean clone.

D8.5: CLOSED.

WHAT PHASE 1 HAS ACTUALLY DONE, for whoever reads the trend next. Tier 1 went
156 -> 132 across 1a-1c, then 132 -> 210 across 1d and this build. As a single
number that looks like regression. It is not two directions of the same thing:
1a-1c fixed cases where the scanner scored correctly-sourced claims as UNSOURCED
(false positives -- count comes down). 1d onward fixed the opposite, cases where
the scanner scored unsourced claims as SOURCED, whether by a blind spot (no
temperature recognition, +61), by numeric coincidence (Option A, +23), or by a
marker meaning the opposite of what it was credited for (staleness, +16). Those
are false negatives, and fixing them makes the count go up. The number got worse
because the instrument got honest.

Tony-action (decide): three separate increases now sit on Tier 1 and all are
real, previously-invisible findings. Whether they get one tracking item or
several is open -- the 1d/1e/1f as-built already proposed L-175 for the
temperature population; the Option A and staleness populations may belong with
it or separately.

Add to Ref: patch_retire_option_a.py; test_provenance_1d.py (now 27 tests);
documentation/AS_BUILT_retire_option_a.md.
```

---

## Rollup -- Tony-action

- **(do)** Run `patch_retire_option_a.py` (VS Code Run button). Expect 13
  `ok` lines across 2 files.
- **(do)** Run `test_provenance_1d.py` (27), `test_citation_inheritance.py`
  (20), `test_constants_provenance.py` (73).
- **(do)** Run `provenance_scanner.py .`. Expect Tier 1 **210**, Tier 2 605.
- **(do)** Paste Block 1 into L-156; mark D8.5 closed; run `ledger_index.py`.
- **(decide)** How the three Tier-1 increases get tracked (one item or
  several).
- **(do)** Push; record `pushed at <SHA>`.

Still carried over and not yet done, from earlier sessions: correct or
supersede `HANDOFF_phase1_1d_to_1f.md` (wrong on 1e at HEAD); stamp the
provenance-discipline v1.3 SHA placeholder; the three open decisions from
the 1d/1e/1f as-built (piece 3's Tier-1 increase, the Tier-1 "FIX NOW"
label, the em-dashes in `comet_visualization_shells.py`).

---

*Ledger note written August 2026 with Anthropic's Claude Opus 5.*
