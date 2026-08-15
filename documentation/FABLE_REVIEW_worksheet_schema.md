# Review reply: worksheet schema (Task 1) and remaining interpretation (Task 2)

**Built on `bdb56d8a5b0503c9afa3ff0511add2854064586e` at
https://github.com/tonylquintanilla/palomas_orrery (branch main).**
Remote HEAD at review time is `f8b4356abe53c423e9730b2c70086f3fa5f1fcd7`;
the delta was diffed (see Method) and does not change any finding below.

Prepared August 15, 2026 by Claude (Fable role). Tony Quintanilla holds
every decision here.

---

## Method (stated before findings, as requested)

I executed; I did not reason from the request text alone. Steps, in order:

1. `git ls-remote` confirmed remote HEAD is `f8b4356` (matches Tony's
   statement). Cloned and checked out the pinned commit `bdb56d8`.
2. Diffed `bdb56d8..f8b4356`: the delta touches the QUALIFIED_PASS
   message wording in `worksheet_checker.py` (3 lines), regenerated
   report/ledger/atlas files, this review prompt itself, and the L-193
   patch scripts. Nothing structural. The review stands at `bdb56d8`.
3. Read `worksheet_checker.py` at the pinned commit -- specifically
   `compare()`, `match_row()`, `classify_verdict()`, `is_compound()`,
   `physical_claims()`, `dispose_verdict()` -- plus `worksheet_keys.py`,
   `documentation/worksheets/L192_key_pins.txt`, `WORKSHEET_CHECK.md`,
   and the claim sites named below in `constants_new.py`,
   `eris_visualization_shells.py`, and GPT's Mars worksheet.
4. This is a different method from the line-window approach the request
   flags: I traced concrete corpus rows through the checker's source.

What I did not check: I did not re-derive the request's measured tables
(104 annotations, 61 routed, 16 classes) row by row. Spot checks only:
QUALIFIED_PASS count is 3 (matches defect #7), 35 `.md` worksheets on
disk (matches the report), and the refusal examples quoted in the
request appear verbatim in `WORKSHEET_CHECK.md`. I also confirmed
`worksheet_request_builder.py` does not exist at `bdb56d8` -- the row
format is not yet fixed, so these findings land before dispatch.

---

## Task 1 -- three rows the four fields cannot express as written

No fifth response field is required. But three concrete rows break the
schema unless three request-side rules are added. Each row is in the
corpus at the pinned commit.

### Break 1 -- `constants_new.py:162`, CHROMOSPHERE_RADII = 1.1

This is a drawn value: deliberately ~36x the physical extent, by Tony's
ruling (L-180), with the physical value carried separately as
CHROMOSPHERE_PHYSICAL_KM = 2000. Field 2 has no unambiguous cell for it:

- **WRONG** (against Carroll & Ostlie's ~1.003 R_sun) routes a settled
  ruling to send-back on every future run, forever.
- **RIGHT** silently redefines RIGHT to mean "matches the ruling" for
  this row while meaning "matches the source" everywhere else -- the
  same one-token-two-questions defect as NO, reborn one level up.

This is not hypothetical: Gemini's row 12 already wrote `No` for this
constant, and the checker emitted CITATION_DEFECT ("wrong authority for
a value that may still be right") for a value that was never claiming
to be physical. Same class: INNER_CORONA_RADII, OUTER_CORONA_RADII,
STREAMER_BELT_RADII.

**Rule needed (request side):** the builder partitions keys by what the
verdict is AGAINST before dispatch. For drawn/convention values, the
dispatched question is different and comparison-safe: (a) does the
stated physical anchor check out (2000 km -- a normal four-field row),
and (b) is the drawn value labeled as drawn in the display text (a
containment check). Never dispatch a value verdict whose reference is a
ruling.

### Break 2 -- `mars_visualization_shells.py:518`, "Mars lacks a stratosphere"

Rendered to users, checked by GPT, found unsupported ("terminology-
dependent... not established by the cited NASA pages"). Field 2 is
"RIGHT / WRONG / UNKNOWN, **plus the number**" -- this claim has no
number. As written, the verdict on it can live only in Notes, where
nothing routes it. Per The Artifact Bounds the Audit, the bound is what
the orrery renders, and this sentence renders.

**Rule needed, one of two -- Tony's ruling:** either (a) qualitative
rendered claims are explicitly out of the worksheet system's scope
(then an unsupported rendered sentence has no home, and that gap should
be stated, not silent), or (b) field 2's object generalizes to "the
number, OR the claim text quoted verbatim." Option (b) stays
comparison-safe: the checker verifies the quote still appears
byte-for-byte in the code string (containment is comparison, not
interpretation) and reads the tri-state beside it.

### Break 3 -- cardinality: `constants_new.py:203` and `eris_visualization_shells.py:477`

ROCHE_LIMIT_RADII = 3.45 has three provenance legs: the formula (Murray
& Dermott -- sourceable), rho_sun = 1408 (sourceable; GPT's worksheet
used 1409), rho_comet ~ 500 ("representative" -- unsourceable by
nature). One Citation tri-state cannot say "formula RIGHT, rho_sun
RIGHT, rho_comet UNKNOWN."

`eris_hill_sphere_info` is one pinned key over a string making four
scored numeric claims; GPT's row 24 addressed one of them, and the
checker already witnesses the gap as CLAIMS_UNADDRESSED (3 of 4). One
Value cell cannot carry a split verdict.

**Rule needed (request side):** one pre-printed row per (key, ordinal),
with field 1 -- code value at time of check -- filled in by the builder,
so the responder only fills verdicts and notes. Field 1 per row is
load-bearing beyond drift detection: if the string is later edited and
ordinals shift, the pre-printed code value stops matching and the
misbinding is loud instead of silent. (The key grammar in
`worksheet_keys.py::compose()` already accepts an ordinal; the pins at
`bdb56d8` are unit-level, so this is a dispatch decision, not new
machinery.)

---

## Task 2 -- where interpretation survives the schema

Assume the four fields land with the three rules above. Seven places
the checker would still decide what a human meant, with the deletion or
containment for each:

**1. Row-to-claim binding.** `match_row()` rules 3 and 4 (masked-prose
longest-common-run, code-value-plus-shared-word) are interpretation and
produced the UNMATCHED class (25 findings). With pre-printed keyed
rows, binding becomes exact string equality on the echoed key and
`match_row()` deletes. A row without an exact key gets one loud class,
never a fuzzy bind.

**2. Verdict cell reading.** `classify_verdict()` splits at
dash/semicolon/paren and reads the head token -- and the words split off
are exactly the disambiguating ones. The repair path interprets too: at
`bdb56d8` the QUALIFIED_PASS message characterized `<<YES -- fully
confirmed>>` (MOON_RADIUS_KM, row 72) as "confirmed with a reservation"
-- the tool describing prose it did not understand, wrongly. Under the
schema: the cell must equal one of three tokens exactly; anything else
is one class (MALFORMED_VERDICT), quoted whole, routed, never
characterized. The 17% token-plus-prose rate says responders WILL write
qualified verdicts; the schema survives only if malformed cells fail
loudly rather than get split.

**3. Numeric reading of field 2.** Three interpretive subsystems:
scale-word lifting (`scaled()`: "million"), range detection
(RANGE_HINT_RE), and the coarser-of-two-precisions rounding rule in
`compare()`. The rounding rule and the over-precision finding are
mutually exclusive: for EARTH_EQUATORIAL_RADIUS_KM, code 6378.137
against worksheet 6378.1 MATCHes under coarser-rounding -- silently
absorbing the very "code carries digits the cited source does not
state" finding both worksheets raised (visible today only because those
rows were citation-only). Decide once, as policy: either the request
instructs "write the number at the source's stated precision, in the
code's units" and the checker compares exactly with excess digits
flagged as their own computed class, or coarser-rounding stays and
over-precision is declared out of the checker's scope. Units likewise:
the request pre-prints the code value with units, the responder answers
in those units, and `scaled()` deletes.

**4. Evaluating the reduction rule.** Field 2 for ranges carries the
rule as prose ("volumetric mean of 1050 x 840 x 537 km"). If the
checker ever parses or evaluates that prose, interpretation returns --
and Haumea shows two live candidate rules (stated volumetric mean gives
779.5; JPL adopted gives 715). Rule: the worksheet states the rule AND
the resulting single number; the checker compares only the number; the
rule text is for humans and the conversation.

**5. The citation verdict's object.** Annotations carry `# Source:`
plus `# Ref:` plus `# Also:` (SUN_RADIUS_KM carries three legs). One
tri-state cannot split them. Rule: field 3 verdicts the `# Source:`
line only; Ref/Also are out of scope or get their own pre-printed rows.
Otherwise "Citation: WRONG" is ambiguous across legs -- the NO-ambiguity
again, one field over.

**6. Cross-worksheet disagreement.** Two responders, same (key,
ordinal), opposite tri-states. Comparing the verdicts for equality is
safe; choosing between them is not. Report both, route to conversation,
decide nothing. Worth writing down now because "one aggregated verdict
per claim" is the natural next feature request, and it is an
interpretation engine.

**7. UNKNOWN routing.** UNKNOWN is a state, not a route. Whether it
blocks, passes, or parks is a one-time policy ruling, set explicitly by
Tony -- otherwise the checker's default quietly becomes a policy nobody
made.

---

## One-line summary

The four fields hold, provided the interpretation is moved out of the
RESPONSE and into the REQUEST: pre-printed per-(key, ordinal) rows with
field 1 filled, the verdict's reference stated per row, a verbatim-quote
object for qualitative rendered claims, and a strict fail-loud grammar
on every cell the checker reads.

*Built on `bdb56d8a5b0503c9afa3ff0511add2854064586e` at
https://github.com/tonylquintanilla/palomas_orrery; reviewed while HEAD
stood at `f8b4356abe53c423e9730b2c70086f3fa5f1fcd7`.*
