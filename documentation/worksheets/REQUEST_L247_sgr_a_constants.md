# Cross-check request -- L-247 Sagittarius A* and galactic-scale constants

**Built on `cf865ffc12862eeaeee5c0d7b1a2627dc003d4bd` at
https://github.com/tonylquintanilla/palomas_orrery (branch main).**

Vocabulary: v2 (2026-08-13)

Worksheet type: VALUE VERIFICATION, with first-time sourcing. Four of
the five rows carry no citation at all, so the job is to establish one
rather than to confirm one.

Expected return filename, per the L-206 convention:

    worksheet_<model>-<version>_L247_sgr_a_constants_<YYYYMMDD>.md

Underscores separate fields, hyphens live inside a field, the date is
last. Add a trailing letter to the date if a day repeats.

---

## What these values are

Five constants in `constants_new.py`, migrated there on 2026-08-25 from
`sgr_a_star_data.py`. The migration moved them without changing them.
Only one arrived carrying any attribution, and that one names no paper,
DOI or table.

Two related constants in the same block are NOT in this request because
they are derived from values that are already cited: `SPEED_OF_LIGHT_M_S`
and `M_PER_AU`.

## The question, for every row

1. Is the number right? Give your own value and the primary source that
   publishes it, with enough detail to find the exact statement -- paper,
   year, DOI, table or page, or the specific data page for an agency
   source.
2. At what precision does the source publish it, and does the code's
   precision overstate that?
3. **If the quantity is DEFINED or DERIVED rather than measured, say so
   and show the arithmetic.** Some of these may not have a source to
   cite because no source publishes them as numbers -- they follow from
   a definition. That is a legitimate answer and it changes the repair,
   so do not force a citation onto a value that has none to give. A
   derivation is complete when it names its inputs, shows the work, and
   the arithmetic closes.
4. If you cannot establish a value or a source, write UNVERIFIED and say
   in Notes what stopped you. An honest UNVERIFIED is a usable answer.

## Two things deliberately withheld

Each of these constants carries a `# Review-note:` comment written by an
earlier session. Those notes are not reproduced here, because two of them
characterize where the value probably comes from and this request is for
an independent look. Ask if you want them after you have answered.

No Claude proposal travels with this request. Nothing below states what
anyone expects the answer to be.

## Response table

Fill `Your value`, `Your source`, `Value correct?`, `Citation correct?`
and `Notes`. Do not edit `Constant` or `Code value`: they record what the
code said at the SHA above.

Verdict tokens -- exactly one per cell, nothing else, reasoning in Notes:

    Value correct?     YES  NO  APPROX  UNVERIFIED
    Citation correct?  YES  NO  PARTIAL  DERIVED  UNSOURCED  UNVERIFIED

`Value correct?` asks whether the number is right. `Citation correct?`
asks whether the source NAMED IN THE CODE publishes it. They are separate
questions and a right number under a wrong authority is value-YES and
citation-NO.

Rows 1, 2, 3 and 5 name no source in the code, so there is nothing there
for the citation verdict to be right about: write `UNSOURCED`, and put
what you found in `Your source`. Row 4 is the only row where the citation
question is live.

| # | Constant | Code value | Code's source line | Your value | Your source | Value correct? | Citation correct? | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 | `GRAVITATIONAL_CONSTANT_SI` -- Newtonian constant of gravitation | 6.67430e-11 m^3 kg^-1 s^-2 | none | | | | | |
| 2 | `SOLAR_MASS_KG` -- mass of the Sun | 1.989e30 kg | none | | | | | |
| 3 | `PARSEC_TO_AU` -- astronomical units per parsec | 206265.0 AU | none | | | | | |
| 4 | `SGR_A_MASS_SOLAR` -- mass of Sagittarius A* | 4.154e6 solar masses | `# Source: GRAVITY Collaboration 2019` | | | | | |
| 5 | `SGR_A_DISTANCE_LY` -- distance to Sagittarius A* | 26670.0 light-years | none | | | | | |

Row 4's source line is quoted verbatim and is the whole of it. It names
no paper, DOI or table, so part of that row is identifying which
publication is meant, if any single one is.

## Findings section

Below the table, in prose: anything that does not fit a verdict cell. A
value that is right for a reason different from the one the code implies,
a source that publishes a range where the code carries a point, a unit or
epoch mismatch, a definition that changed between editions.

## What happens to this

Two models answer this independently, without seeing each other's return.
A human compares them. Disagreement between the two returns is a FINDING,
not an error to reconcile before sending back.

Nothing here becomes a `# Cross-checked:` annotation automatically. A
returned verdict is evidence; what lands in the code is a separate edit,
made in conversation, that cites this worksheet by filename.

---

*Request written August 25, 2026 with Anthropic's Claude Opus 5, against
`cf865ffc12862eeaeee5c0d7b1a2627dc003d4bd`. Ledger: L-247.*
