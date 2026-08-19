# Pilot convergence report -- 23 rows, 3 legs, constants_new.py

**Built on `6fbce8c06fbd10f5ce9fc8190e8269a5f1894787` at
https://github.com/tonylquintanilla/palomas_orrery (branch main).**

Type: **MEASUREMENT.** Read against
`documentation/PILOT_EXPECTED_DISPOSITIONS_20260817.md`, which was
written before dispatch.

Legs of record, all dispatched at `eae95f5a` on 2026-08-18:

- `worksheet_gemini-3-1-pro_pilot_constants_new_20260818.jsonl`
  (Gemini 3.1 Pro, fresh chat)
- `worksheet_gpt-5-6-sol_pilot_constants_new_20260818.jsonl`
  (GPT 5.6 Sol, fresh chat)
- `worksheet_claude-opus-5_pilot_constants_new_20260818.jsonl`
  (Claude Opus 5, fresh chat, outside the project)

Renamed 2026-08-19 to the shape L-206 had already ruled --
`worksheet_<model>_<batch>_<YYYYMMDD>` with the model field carrying
the version. The names first used omitted the version and were
proposed without checking the ledger item that had settled it. The
rename was free because no annotation cited them yet; it would not
have been free an hour after the first `# Cross-checked:` leg.

Three further Gemini files, `_from0415`, `_from0602`, `_from0802`, are
NOT legs. They are continuation-thread runs kept as
context-sensitivity evidence; see Part 5.

Lands in `documentation/`.

---

## Part 1 -- The headline, scored

**Predicted: 13 clear, 10 return. Measured: 17 / 10 / 11.**

| Leg | Rows clearing both axes | Against a prediction of 13 |
|---|---|---|
| Gemini | 17 | 4 over |
| GPT | 10 | 3 under |
| Claude | 11 | 2 under |

Two of three legs landed within three rows of a prediction written
six days earlier by a reader who had no access to any of them. The
prediction was neither vacuous nor lucky: it named which rows would
return and why, and Part 2 scores those individually.

Gemini's 17 is the outlier, and the expectations file says how to read
it: a sweep of confirmations means the responder agreed with the code
rather than checked it. Gemini confirmed both trap-adjacent rows the
other two flagged, and confirmed Haumea and Bennu outright where the
other two refused or qualified. Its notes are also the shortest of the
three by a wide margin.

**Ten rows come back clean from all three legs.** Those are the
strongest results in the batch, because three models with different
training reached the same verdict independently:

`KM_PER_AU`, `SUN_RADIUS_KM`, `EARTH_POLAR_RADIUS_KM`,
`JUPITER_EQUATORIAL_RADIUS_KM`, `JUPITER_POLAR_RADIUS_KM`,
`SPEED_OF_LIGHT_KM_S`, `TERMINATION_SHOCK_AU`, `MARS_RADIUS_KM`,
`SATURN_RADIUS_KM`, `URANUS_RADIUS_KM`, `NEPTUNE_RADIUS_KM`.

That is eleven names for ten rows because `MOON_RADIUS_KM` clears on
Gemini only; it is in Part 3.

---

## Part 2 -- The three trap rows

The expectations file says to check these first, because their wrong
answer is diagnostic on its own.

**`SUN_RADIUS_KM` -- trap not sprung, all three legs.** The predicted
failure was citing the measured photospheric radius (~696,340 km) and
refuting the nominal 695,700. No leg did. Claude's note goes further
and states the distinction unprompted: B3 endnote 2 gives the
measurement as 695658 +/- 140 km and the resolution says explicitly
that nominal values should not be taken for true solar properties. The
`# Note:` in the block was read.

**`HELIOPAUSE_RADII` -- trap not sprung, and the canary is alive.**
The predicted failure was reading Gurnett's 121.6 AU, comparing it to
26148, and reporting a mismatch. No leg reported a mismatch. All three
returned DERIVED, and two reproduced the conversion arithmetic to the
digit. This row was on record as must-not-send-back: drift here would
have been a finding in the loop rather than in the constant. There is
none.

**`BENNU_RADIUS_KM` -- trap not sprung, and something better
happened.** The predicted failure was reporting 246 against a code
value of 0.246, tripping on units. No leg did; all three answered in
kilometres. But GPT and Claude both refused or qualified the value for
a reason the expectations file did not anticipate: the code carries
the pre-encounter radar figure, and OSIRIS-REx superseded it. Claude
puts the corrected value at 0.2450 km and adds a citation finding --
the comment attributes "mean radius 246 +/- 10 m, V = 0.062 km^3" to
OSIRIS-REx OLA, but those are the Nolan radar numbers restated, so the
row reads as though the mission independently produced the figure it
was confirming. That is the second-best outcome the expectations file
lists: the return contradicts the prediction and the return is right.

**Three traps, three not sprung.** The artifact conveyed what it was
supposed to convey. That is the pilot's primary result.

---

## Part 3 -- Convergent findings: rows all three legs flagged

Six rows drew a non-clearing verdict from every leg. Independent
agreement across three models is the strongest signal this method
produces.

| Row | Gemini | GPT | Claude |
|---|---|---|---|
| `EARTH_EQUATORIAL_RADIUS_KM` | no / no | confirmed / no | confirmed / partial |
| `CHROMOSPHERE_PHYSICAL_KM` | approx / confirmed | approx / unverified | approx / unverified |
| `INNER_CORONA_RADII` | unverified / unverified | no / unverified | approx / unverified |
| `STREAMER_BELT_RADII` | approx / confirmed | partial / partial | approx / no |
| `ROCHE_LIMIT_RADII` | derived / confirmed | approx / no | derived / unverified |
| `HELIOPAUSE_RADII` | derived / confirmed | derived / derived | derived / confirmed |

`HELIOPAUSE_RADII` appears here only because DERIVED does not clear.
It is a healthy row; see Part 2.

**`EARTH_EQUATORIAL_RADIUS_KM` is the cleanest confirmed prediction in
the batch.** The expectations file predicted PARTIAL on the citation
because B3 publishes 6378.1 and the third decimal comes from IERS,
named in a `# Note:` but not on the Source line. All three legs
flagged the citation, by three different routes. Claude states the fix
and observes that the row immediately below it -- the polar radius --
already does it correctly, citing IERS and noting separately what B3
rounds to. The repair is to make this row look like its neighbour.

**`STREAMER_BELT_RADII` is the most serious finding, and no prediction
anticipated it.** Claude reports the DeForest, Howard & McComas (2014)
citation is not merely imprecise but inverted: the paper's 6 R_sun is
an inner bound beyond which inbound wave motion was first detected,
and its streamer-belt result is a lower bound of 17 R_sun on the
Alfven surface. The code took a floor and used it as a ceiling, and
the paper's point is that the structure extends further out, not that
it stops there. GPT independently marked both axes PARTIAL. The value
6.0 may survive as a drawing choice; the citation attached to it does
not.

**`INNER_CORONA_RADII` is the artifact-bounds question arriving as a
row, exactly as predicted.** All three legs declined to confirm.
Beyond that they split on what kind of thing it is: GPT refuses the
value outright at 1.5 R_sun per the 2023 middle-corona consensus,
Claude calls it a defensible drawing convention that nests sensibly
with the 6 R_sun streamer shell while noting the reviews put the
transition nearer 1.5-2, and Gemini declines to answer at all. The
disagreement is not about a number. It is about whether a
visualization boundary is verdictable, which is Tony's ruling to make
and not a defect in any leg.

**`ROCHE_LIMIT_RADII` behaved as predicted and named its own problem.**
DERIVED from two legs. Claude adds what the derivation rests on: the
output is only as good as an assumed cometary density of 500 kg/m3,
which no source publishes for this constant, and the answer moves to
4.7 at 200 kg/m3 and 3.2 at 600. A scenario parameter wearing the
clothes of a constant.

---

## Part 4 -- Divergent findings: where the legs disagree

**`HAUMEA_RADIUS_KM` -- predicted as the row most likely to divide
readers, and it did.** Gemini confirmed 715 on both axes. GPT
confirmed the value and marked the citation partial. Claude refused
the value: 715 is exactly the volume-equivalent radius of the Lockwood
et al. 2014 model, reproduced to the digit, but that model was
overturned by the 2017 stellar occultation, the only direct size
measurement, which puts the mean radius near 798 km -- 11 percent
larger in radius, 39 percent in volume.

The expectations file called disagreement here a property of the body
rather than a defect in the worksheet. That holds, and one further
thing emerged that no prediction reached: **the dimensions in the
comment, 1050 x 840 x 537 km, match no published shape model.**
Lockwood gives 960 x 770 x 495 and Ortiz gives 1161 x 852 x 513. Yet
the comment's derived geometric mean of 779.5 km computes correctly
FROM those unsourced axes. Someone performed valid arithmetic on
numbers with no source. That failure leaves no arithmetic trace, so
neither the scanner nor a reader checking the maths would catch it,
and a sibling elsewhere in the corpus would be equally invisible.
Claude flags this as worth tracing rather than correcting.

**`ALFVEN_SURFACE_RADII` -- a finding no prediction reached, and it is
checkable against a sibling row.** The expectations file listed this
among the 13 expected to clear. Gemini and GPT confirmed the value;
Claude marked it APPROX and reports an origin mismatch: 18.8 R_sun is
an altitude above the photosphere, both in the Kasper et al. abstract
and the NASA release, while `PARKER_CLOSEST_RADII` at 9.86 is
heliocentric. Two constants in one file describing the same
spacecraft, differing by exactly one solar radius. If the Alfven
surface is drawn as a shell from Sun centre it is low by 1 R_sun and
should be 19.8. GPT independently marked the citation partial, noting
the paper does not itself print 18.8 -- that figure is from the press
release.

This is the single most consequential technical finding in the batch,
because it is a rendering error rather than a documentation one, and
it is confirmable from inside the file without consulting any source.

**`ARROKOTH_RADIUS_KM` -- the value has now been wrong in both
directions.** Gemini confirmed. GPT returned DERIVED at 9.13. Claude
returned APPROX and reports a newer New Horizons shape model giving
9.95 km, a 9 percent change moving opposite to the 2026-04-15
correction the comment records. Claude also traces the attribution:
the figure 3166 km^3 and the phrase about an equivalent 9.1 km sphere
appear verbatim in Amarante & Winter (2022) working from Spencer et
al. 2020, not in the cited Keane et al. 2022. A watch flag suits this
row better than another one-time fix.

**`PARKER_CLOSEST_RADII` -- prediction half right.** Predicted REFUTED
or UNSOURCED on the citation, testing whether a bare URL functions as
an authority. No leg refuted it. GPT marked it UNVERIFIED, reporting
the legacy JHUAPL page could not be retrieved. Claude marked it
PARTIAL, noting it did not fetch that page and that a bare mission
index with no section or retrieval date is thin for a page that
changes, while confirming 9.86 from two independent directions
including the WISPR instrument paper. So the URL did not function as
an authority -- but it failed by being unreachable rather than by
being wrong, which the prediction did not distinguish.

---

## Part 5 -- What the pilot measured about the loop itself

**The four join rows all arrived intact.** Chromosphere (1 joined
line), Moon (1), Haumea (2), Arrokoth (3). Arrokoth's 237-character
citation, the heaviest join in the corpus, came back complete enough
that Claude quoted the parenthetical about the April correction. Every
leg answered the joined content rather than its first line.

**Format discipline held completely.** Three legs, 69 rows, and across
all of them: zero unparseable lines, zero missing or modified row
hashes, zero duplicate keys, zero empty answer fields, zero tokens
outside the vocabulary. The JSON format needs no fallback, and the
`.md` fallback was never used. The hash mechanism did what it was
built for -- 69 of 69 verified, meaning key, claim and code value came
back untouched in every row of every leg.

**Continuation threads produce different answers than fresh ones.**
Three Gemini runs in threads that had produced earlier cross-check
rounds, given identical rows on the same day: one returned CONFIRMED
on all 46 verdict fields, one returned 44 confirmed and 2 derived, one
used four tokens and produced one refusal. The fresh Gemini run used
five distinct tokens on the value axis and produced the only
`unverified` of the four. Not proof of causation at n=4, but the
direction is consistent and it cost nothing to observe.

**Project context contaminates a fresh chat too.** The first Claude
attempt ran in a new chat INSIDE the Paloma's Orrery project and
declined to answer, on the grounds that the project's memory and
knowledge files told it three trap rows existed without telling it
which -- which would turn row-checking into trap-hunting, and would
make the leg unreproducible by anyone lacking that memory store. The
hygiene rule as written said "a fresh chat"; it now needs "and outside
any project." Found by a responder refusing a job, which is the
cheapest possible way to find it.

**Two dispatches were lost to a platform incident.** Anthropic's
status page carried an open investigation into degraded performance
across multiple models from 16:20 UTC on 2026-08-18. Two Claude
dispatches returned nothing, the second reusing the crashed thread.
Neither is a finding about the loop. Recorded because a report
claiming three clean dispatches, when there were five attempts across
two providers plus an in-project refusal, would misdescribe how this
behaves in practice.

**The UNKNOWN trigger fired, and the returns named its shape better
than the design did.** `DESIGN_20260818_unknown_verdict.md` pre-
registered two rows as the threshold. There are seven across the three
legs: Gemini 1, GPT 3, Claude 3. Every one carries a note describing a
lookup attempted and not completed. Claude's leg states the gap in the
vocabulary's own terms -- that `unverified` reads as *no answer given*
when what happened was *an answer attempted and not reached* -- and
then supplies what the design note did not: **all three of its cases
are print books.** Carroll & Ostlie, Golub & Pasachoff, Murray &
Dermott. GPT hit two of the same three. The missing verdict is not
scattered; it concentrates wherever the authority is a book no
responder can open.

That reframes the follow-on work. UNKNOWN is worth building, on the
four rulings already settled in the design note. But the finding
underneath it is about the corpus: three constants in this slice rest
on print authorities that no model-mediated check can ever reach, and
those rows need a human with library access, not a better token.

---

## Part 6 -- What this does not decide

Nothing here changes a constant. Every finding above is a claim by a
responder, and the next step is Tony's judgment per row, not a patch.

The rows carrying a recommendation strong enough to act on, in the
order I would take them:

1. `ALFVEN_SURFACE_RADII` -- origin mismatch, checkable inside the
   file, and a rendering error if the shell is drawn from Sun centre.
2. `STREAMER_BELT_RADII` -- inverted citation; the authority says the
   opposite of what the row uses it for.
3. `EARTH_EQUATORIAL_RADIUS_KM` -- Shape A citation swap, with the
   polar row below it as the template.
4. `HAUMEA_RADIUS_KM` -- the unsourced axes, traced rather than
   corrected.
5. `BENNU_RADIUS_KM` -- superseded value and a misattributed
   confirmation.

Items 1 and 2 are the ones I would not leave open.

---

*Prepared August 19, 2026 with Anthropic's Claude Opus 5. Legs
dispatched at `eae95f5a`; report built on `6fbce8c0`.*
