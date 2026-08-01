# D8.5 integration into L-156 — edit instructions

Five targeted edits in LEDGER_CONSOLIDATED.md. All within the existing
L-156 entry. Use Ctrl+H or manual editing in VS Code.

---

## Edit 1: Update the metadata tag (line 4150)

Find:
<!-- L:156 status:OPEN upd:2026-07-31 section:W.Active flag: rice:5/4/80/3 -->

Replace with:
<!-- L:156 status:OPEN upd:2026-08-01 section:W.Active flag: rice:5/4/80/3 -->

---

## Edit 2: Update the scanner state paragraph (line ~4160)

Find:
**Scanner state at HEAD (post-Phase-1, `b813aa6`):** Tier 1 171, Tier 2
644, Tier 3 62, Tier 4 2, total 879 across 116 files. Tier 1 is
132 baseline + 39 newly-visible temperature claims (tracked separately as
L-175).

Replace with:
**Scanner state at HEAD (post-D8.5, `42103d6`):** Tier 1 210, Tier 2
605, Tier 3 62, Tier 4 2, total 879 across 116 files. 879 conserved
across D8.5 — 39 findings moved Tier 2 to Tier 1 (23 from Option A
retirement, 16 from staleness-credit removal).

**Phase 1 measured arc (the instrument got honest):** Tier 1
145 → 156 (1a) → 156 (1b) → 133 (1c) → 132 (L-174) → 171 (1d/1e/1f)
→ 210 (D8.5). The first half (145 → 132) fixed false positives —
correctly-sourced claims scored as unsourced. The second half
(132 → 210) fixed false negatives — unsourced claims scored as sourced,
whether by a blind spot (temperature recognition, +61), numeric
coincidence (Option A, +23), or a marker meaning the opposite of what it
was credited for (staleness, +16). The number went up because the
instrument got honest.

---

## Edit 3: Add D8.5 closure to the build history section

After the paragraph ending "...re-divergence fails a test instead of
going unnoticed." (the build_pinned_values bleed fix paragraph), add:

**D8.5 — Option A retired (2026-08-01, Opus 5).** Two mechanisms removed
from `score_unit()`, both granting V_SOURCED without a real citation.
(a) Option A: credited display strings whose numeric claims matched
pinned constant values — coincidence, not sourcing. 26 findings affected
(not 18 — 1d's temperature units created new claims eligible for the
credit). 23 moved to Tier 1. (b) Staleness credit: granted V_SOURCED to
strings matching date-sensitive patterns ("as of 2024", "Planned",
"Still active") with no citation at all — the reason string said "no
source" and the score said "sourced." Logic also ran backwards: staleness
means a claim will expire, making it more vulnerable, not less.
15 findings, all now at V_RECALLED. `build_pinned_values()` kept — it
feeds `scan_shadow_constants()` for derived-shadow detection, now
diagnostic-only. Scoring path audit: three remaining paths that set
`unit.vuln`, all requiring a citation a person wrote. No other instance
of the credit-without-sourcing failure class remains.

**General lesson (D8.5):** when a scoring definition changes, every
mechanism assigning that score needs re-reading, not just the ones the
change targeted. Both Option A and staleness credit predated the D3
ladder and were not wrong when written — they were outlived by a
definition change and never revisited.

---

## Edit 4: Update "What remains open under L-156"

Find and DELETE the D8.5 paragraph:

**D8.5 (retire or keep Option A).** `build_pinned_values()` and Option A
scoring are still live. The bleed flaw is fixed but the mechanism itself
may not be worth keeping. Design question, not yet decided.

(The Phase 2, Phase 3, Phase 4 paragraphs stay as-is.)

---

## Edit 5: Add to the Ref block

At the end of the Ref list, before the blank line, add:

`documentation/patch_retire_option_a.py`;
`documentation/AS_BUILT_retire_option_a.md`.

---

After all five edits, run `ledger_index.py` and push.
