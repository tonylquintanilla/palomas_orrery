# Decision page -- the extractor constants (decide item 4)

**Built on `66cf0cbcf298787542ae9b7bf335273d7ffa67d1` at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Verified live at session start.**

Lands in `documentation/`. It is a record read by a person, not a tool
input.

---

## The handle holds two questions, not one

Decide item 4 was opened as a scope question and the August 14 handoff
re-pointed it at a timing question. Both are real; only one blocks
dispatch.

**A. Which values may still move before keys are issued.** BLOCKING.
**B. Whether these six constants owe the audit a citation.** Not
blocking, cosmetic, and it should not ride along with A.

Everything below is A. B is left where it was.

---

## A. Only two of the six can move an ordinal

The key module names what decides claim membership: the scanner's
claim regex and the checker's instruction filter. Nothing else.

| Constant | File | Value | Moves an ordinal? |
|---|---|---|---|
| `INSTRUCTION_LOOKBACK` | `worksheet_checker.py` | 30 | **Yes** |
| `INSTRUCTION_LOOKAHEAD` | `worksheet_checker.py` | 25 | **Yes, in principle** |
| `MIN_PROSE_FRAGMENT` | `worksheet_checker.py` | 24 | No |
| `SCHEMA_VERSION` | `provenance_history.py` | 1 | No |
| `MAX_RUNS` | `provenance_history.py` | 6 | No |
| `EXPECTED_CADENCE_DAYS` | `provenance_history.py` | 1 | No |

`MIN_PROSE_FRAGMENT` has one call site, in `match_row` rule 3. It
decides which worksheet ROW a claim matches. It is not part of the key
and it cannot change how many claims a string carries. Mis-tuning it
produces UNMATCHED noise, which is visible and recoverable. It does
not need to be frozen before dispatch.

The three in `provenance_history.py` govern the run-history ring
buffer. They touch nothing in the key path.

**So the blocking set is two constants, not three.**

---

## The measurement

29 annotated display-string sites in the L-192 corpus, 41 claims kept
at current settings, 14 numbers dropped as display instructions.
Recomputed over a 10x10 grid. The cell is the count of sites whose
kept-claim sequence differs from the current one.

```
             LOOKAHEAD
              0   10   15   20   25   30   40   50   60   80
 LOOKBACK
    0        13   13    3    1    1    1    1    1    1    1
   15        13   13    3    1    1    1    1    1    1    1
   20        11   11    0    0    0    0    0    0    0    0
   25         0    0    0    0    0    0    0    0    0    0
   30         0    0    0    0    0    0    0    0    0    0
   40         0    0    0    0    0    0    0    0    0    0
   60         0    0    0    0    0    0    0    0    0    0
   80         1    1    1    1    1    1    1    1    1    1
```

Read three things off it.

**There is a plateau, and the current values sit inside it.**
LOOKBACK 25 through 60 gives an identical answer at every LOOKAHEAD
tested. Current is 30. Five to spare below, thirty above.

**Below 25 the filter starts missing instruction numbers**, which
promotes an operating instruction to a science claim.

**At 80 it swallows a real claim**, which is the exact failure the
comment above the constants predicts -- a wide window reaching across
the paragraph break.

---

## The finding inside the measurement

**`INSTRUCTION_LOOKAHEAD` is inert.** All 14 drops are found by the
back window. Thirteen are also found by the ahead window, redundantly.
**Zero are found by the ahead window alone.** Setting it to 0 changes
nothing in the corpus.

The reason is structural, not accidental. The orrery writes the phrase
in front of its number -- `SET MANUAL SCALE TO AT LEAST 0.005 TO
VISUALIZE`. The trailing-phrase case the constant was written for
(`4.6 MB PER FRAME`) never produces a claim to drop, because the
scanner's claim regex does not count that number in the first place.

This is a knob whose value cannot change the output. Same family as
the three checks that could not fail last session, one layer over: it
looks tuned and it is doing nothing. Not blocking, and it should not
be changed as part of this ruling -- deciding whether to delete it or
keep it as a documented guard is its own small decision.

---

## What a late retune would actually cost

The handoff says settling these after dispatch invalidates the errand
retroactively. True, with one correction worth having: the failure
would be LOUD.

`worksheet_keys.py` records the claim count and the unit token beside
every key, and checks both before any value comparison. A retune that
adds or removes a claim changes the count, which fires KEY_SHIFTED on
every affected row rather than passing a re-pointed ordinal through.

So the risk is a forced re-issue of the errand, announced -- not a
silent wrong answer. That is a smaller failure than the phrase
suggests, and it is still worth spending five minutes to avoid.

---

## Recommendation

**Freeze `INSTRUCTION_LOOKBACK = 30` and `INSTRUCTION_LOOKAHEAD = 25`
as they stand. No retune.** They sit mid-plateau; there is no better
value to move to, and moving inside the plateau changes nothing.

Two things travel with the freeze, both mine to build:

1. A pinned drop set -- the 14 dropped numbers, written down literally,
   resolved against current source on every run. Without it the
   plateau is a measurement taken once, and the constants become a
   check that cannot fail.
2. `EXTRACTOR_VERSION = 1` recorded with the pins, so the version, the
   constants and the drop set move together or not at all.

`MIN_PROSE_FRAGMENT` and the three history constants stay open under
question B and do not hold up dispatch.

---

*Prepared August 14, 2026 with Anthropic's Claude Opus 5. Built on
`66cf0cbcf298787542ae9b7bf335273d7ffa67d1` at
https://github.com/tonylquintanilla/palomas_orrery.*
