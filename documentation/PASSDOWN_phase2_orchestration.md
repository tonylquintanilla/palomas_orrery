# Pass-Down Prompt — Phase 2 orchestration + model rotation review

**Built on `a8e3862d4dda314eaa5186074f1dc05581801afa`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Verify fresh — this is stated, not assumed.**

---

## Your role

You are Claude Opus 4.6, orchestrating Phase 2 of the L-156 provenance
scanner rebuild. Same role as the session that produced the Phase 1d-1f
predesign: verify the repo, read the ledger, confirm what's decided, map
out what Phase 2 requires, flag gaps, present options with tradeoffs.
You are not the designer or builder unless Tony says so.

Tony Quintanilla is the integrator. He mediates between sessions and
models, holds sole commit authority, and makes all judgment calls.

---

## Where this picks up

Phase 1 of the L-156 scanner rebuild is COMPLETE (1a through 1f plus
two follow-ons: the build_pinned_values() bleed fix and D8.5 Option A
retirement). The scanner is at a clean baseline: Tier 1 210, Tier 2 605,
Tier 3 62, Tier 4 2, total 879 across 116 files.

The Tier-1 count went UP across Phase 1, not down. This is correct —
the first half (1a-1c) fixed false positives (correctly-sourced claims
scored as unsourced, Tier 1 145 → 132), the second half (1d + D8.5)
fixed false negatives (unsourced claims scored as sourced, Tier 1
132 → 210). The number went up because the instrument got honest.

Phase 2 is **D4: the cross-checked annotation mechanism and backfill.**

---

## What Phase 2 is (from the design handoff + review, not recalled)

The design handoff (D4 section) and design review define two pieces:

**Piece 1: the scanner mechanism.** Teach the scanner to recognize a new
comment form:

```
# Source: NASA Planetary Fact Sheet
# Cross-checked: Gemini 2026-04-15 (worksheet_earth_visualization.md)
```

When found, bump vulnerability from V_SOURCED (V3) to V_CROSS_CHECKED
(V1). Same comment grammar, same lookback window as `# Source:` — one
new regex, no new positional rules.

**Anti-gaming rule (decided, design review confirmed):** the parenthetical
worksheet reference is REQUIRED. An annotation without a ref scores
SOURCED, not CROSS_CHECKED. The mechanism must not become a new way to
cite-to-clear — "I cross-checked it" without a traceable audit trail is
exactly the failure class Phase 1 just cleaned out.

**Piece 2: backfill.** Two tracks:

- **Track 1 (mechanical):** transcribe April 2026 Gemini worksheet
  confirmations into `# Cross-checked:` annotations on already-
  worksheeted files. The design handoff names Earth, Jupiter, Mercury,
  comets, star_notes, info_dictionary, and constants_new fundamentals.
  This is Role 3 of the Review-Repair Protocol — mechanical insertion
  of already-performed verification, worksheets as source of truth.
  Nothing gets annotated that a worksheet doesn't cover.

- **Track 2 (new worksheets):** draft and run new Gemini worksheets for
  uncovered files, starting with `celestial_objects.py` (50 findings,
  zero prior worksheet coverage). See the model rotation question below.

**Design review gap (still open):** confirm the backfill list against
the April worksheets' actual coverage before assuming which ~130 findings
are already clear.

---

## Two small items carried over from Phase 1

These are complete but not yet pushed or are cosmetic:

1. **`patch_retire_option_a.py`** still in the repo root. Move to
   `documentation/` — same as the other eight. It shows as a Tier-1
   self-scan finding until moved.

2. **Duplicate "Phase 1 measured arc"** in L-156 at line ~4303 (the old
   version that only goes through 1d/1e/1f). The expanded version at
   line ~4163 (through D8.5) supersedes it. Delete the old one. It
   starts with `**Phase 1 measured arc:** Tier 1: 145 →`.

Verify both at session start — Tony may have already handled them.

---

## Model rotation — decided

The current rotation:
- **Opus 4.6:** orchestration, conversation
- **Opus 5:** design and build
- **Sonnet 5:** as-built review, orchestration
- **Fable 5:** break-glass escalation (not standing rotation)
- **Gemini:** factual cross-checks
- **GPT:** selective design cross-checks

**Gemini stays in the cross-check role.** Gemini produced a candid
self-analysis acknowledging failure modes in its own work: fabricating
authority from memory, whiplash between confident speculation and
overcorrection, pattern-matching toward plausible-sounding explanations
when it lacks grounding. These failures happen when the output format
allows ungrounded narrative. The worksheet format does not — every cell
requires a primary source citation, and an empty citation field is a
visibly failed cell. The worksheet is the mechanical enforcement of
"fetched not recalled" applied to the cross-checker itself. Constrain
the format, and the discipline follows.

**What "cross-check" means in this rotation:** both models get the same
worksheet prompt independently. This is the Competitive pattern from
Mode 7 — same question, independent answers, compare. It is NOT one
model reviewing or grading another's existing output. The value comes
from convergence (both found the same answer from different sources —
high confidence) or divergence (they disagree — dig deeper). Tony
compares the results as integrator.

So for Phase 2 Track 2, each new worksheet goes to both the primary
model (Claude/Opus 5) and the cross-checker (Gemini) with the same
prompt. Tony compares. Divergences get investigated. The worksheet
format ensures both models cite primary sources rather than asserting
from memory.

**Kimi K3 note:** Moonshot AI released Kimi K3 in July 2026 (2.7T
parameters, open-weight, 1M-token context). Tony has not tested it yet.
Worth a bounded trial on one worksheet as a third cross-checker if Tony
wants to evaluate it — the competitive pattern scales to three models
with no structural change.

---

## Reference documents to read from the repo

Pull and read from live HEAD before proposing anything:

- `LEDGER_CONSOLIDATED.md` — L-156 (full Phase 1 history, Phase 2-4
  outline), L-157, L-161, L-155, L-160, L-175
- `documentation/DESIGN_HANDOFF_provenance_scoring_and_pinning.md` —
  D4 section (line 239)
- `documentation/DESIGN_REVIEW_provenance_scoring_and_pinning.md` —
  D4 confirmed, Track 1/Track 2 detail, sequencing revision
- `documentation/AS_BUILT_L156_phase1c.md`
- `documentation/AS_BUILT_L156_phase1d_e_f.md`
- `documentation/AS_BUILT_retire_option_a.md`
- `MASTER_PLAN_INTERACTIVE_GALLERY_SUMMARY.md` (Tony's current summary)
- `skills/provenance-discipline/SKILL.md` (v1.3)
- The `documentation/worksheet_*.md` set — these are the April 2026
  Gemini worksheets that Track 1 backfills from. Read them to understand
  what was actually verified and the worksheet format.

---

## What to do first

1. Verify HEAD. Record the SHA.
2. Read L-156 (the cleanup version, not the old build log) — especially
   "What remains open" and the decided constraints.
3. Read D4 in the design handoff and the design review's amendments.
4. Read the April worksheets to understand what Track 1 can backfill.
5. Map Phase 2's scope and propose a predesign — the model rotation
   is decided (see section above).

---

*Pass-down prompt drafted August 1, 2026 by Claude Opus 4.6.*
