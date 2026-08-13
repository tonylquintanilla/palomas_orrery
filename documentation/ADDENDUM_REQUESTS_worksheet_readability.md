# Two Addendum Requests -- for the session that produced them

Both worksheets came from the same conversation:

> **"DONE: Phase 2 design and build Piece 1"**
> (opened as "OPEN: Phase 2 design and build Piece 1", August 2-4, 2026)

Paste the relevant prompt below into that conversation. Each asks for a
NEW file; neither edits the original, which stays as the historical
record.

**Why both are being asked for.** A worksheet checker is being built
that opens the file each annotation names and confirms it states the
value and records a verdict. It reads markdown tables by column role. A
document it cannot parse gets reported as unreadable on every run
forever, and a verdict of PARTIAL over an unfinished lookup is not a
completed check. The fix is a finished answer in a readable shape, not a
cleverer parser.

---

## PROMPT 1 -- for `worksheet_claude_batch1_blind_lookup_DELTA.md`

Copy from here:

---

I need an addendum to `worksheet_claude_batch1_blind_lookup_DELTA.md`,
which you wrote on August 3, 2026 as a delta rather than a worksheet
because a completed Claude blind-lookup worksheet already existed.

Re-verify the repo HEAD first
(https://github.com/tonylquintanilla/palomas_orrery, branch main) and
open with the anchor line.

**The problem:** that file is prose. Its findings are real -- the Nimmo
& Brown 2023 authorship correction, the fourth model input (4.5e-12
W/kg), the Eris differentiation citation, the lunar core dimensional
constraints -- but a tool cannot read them. One annotation in
`eris_visualization_shells.py` line 41 cites this file as a Claude leg,
and the checker being built will flag it as unreadable on every run.

**What I need:** a new file,
`worksheet_claude_batch1_blind_lookup_DELTA_addendum.md`, restating your
findings as a markdown table with exactly these columns:

    | # | Claim in code | Code value | Your value | Source | Value correct? | Notes |

One row per BL item you addressed (BL-1 through BL-8). The `#` cell
carries the BL number. The `Value correct?` cell carries EXACTLY ONE of
these tokens and nothing else:

    YES  NO  PARTIAL  APPROX  DERIVED  UNVERIFIED

Put the reasoning in Notes, not in the verdict cell. Where you marked
something NOT ATTEMPTED or NOT FOUND, the verdict is UNVERIFIED and the
Notes say what blocked you.

**Keep the independence disclaimer, and put it above the table, not
inside it.** Your original file states that you were not blind -- you
had read all three follow-up worksheets before starting -- and that two
Claude passes are one leg reported twice. That is the most valuable
thing in the document and it must survive the reformatting verbatim.
Whether the Eris annotation still counts as a completed Claude leg is
Tony's ruling, and he needs your statement of the limitation to make it.

Do not revisit the research. This is a format job.

---

End of prompt 1.

---

## PROMPT 2 -- for `worksheet_claude_constants_new.md`

Copy from here:

---

I need you to finish the citation verification you began on August 2,
2026 in `worksheet_claude_constants_new.md`, and return the result as an
addendum.

Re-verify the repo HEAD first
(https://github.com/tonylquintanilla/palomas_orrery, branch main) and
open with the anchor line. `constants_new.py` has changed since your
anchor `225071f`; check each value against the file as it stands now,
not as your worksheet records it.

**The problem:** 17 of your 37 rows are unresolved -- 11 UNVERIFIED and
6 PARTIAL. You marked them honestly, and the coverage note in your own
headline says so. But a downstream tool now reads these verdicts, and an
unresolved row cannot support the annotation that cites this worksheet.

The 11 UNVERIFIED are mostly Group D, where the citations are book
chapters (Carroll & Ostlie; Golub & Pasachoff) that web search could not
open, plus the Oort cloud limits. The 6 PARTIAL are
`EARTH_EQUATORIAL_RADIUS_KM`, `EARTH_POLAR_RADIUS_KM`,
`MERCURY_RADIUS_KM`, `PLUTO_RADIUS_KM`, `ERIS_RADIUS_KM`, and
`MAKEMAKE_RADIUS_KM`.

**The Mercury row is the one to start with**, because it is the case
that prompted this request. You wrote PARTIAL with the note that JPL SSD
publishes 2439.4 +/- 0.1 while the code carries 2439.7 from the NASA
fact sheet, that two NASA-family sources disagree by 0.3 km, and that
you did not open the one the code cites. Open it. Resolve which value
the cited source actually publishes, and give a verdict.

**What I need:** a new file,
`worksheet_claude_constants_new_addendum.md`, covering only the 17
unresolved rows, as a markdown table with exactly these columns:

    | # | Constant | Code value | Your value | Source | Value correct? | Citation correct? | Notes |

Keep your original row numbers (A1, B1, G1 ...) in the `#` cell so the
rows can be matched back. Each verdict cell carries EXACTLY ONE of:

    YES  NO  PARTIAL  APPROX  DERIVED  UNVERIFIED

Two separate verdicts per row, and do not conflate them. `Value
correct?` asks whether the number is right. `Citation correct?` asks
whether the named source publishes it. A right number under a wrong
authority is value-YES and citation-NO, and that distinction is the
whole point of the column.

**Where you still cannot resolve something, say UNVERIFIED and say what
blocked you in the Notes.** An honest UNVERIFIED is a usable answer. A
PARTIAL that means "I ran out of session" is not, and should be
UNVERIFIED instead. Reserve PARTIAL for a claim that is genuinely
half-right -- for example, a source that publishes the value at lower
precision than the code carries.

Do not edit the original worksheet. It is the record of what was known
on August 2.

---

End of prompt 2.

---

## Note for Tony, not part of either prompt

Several of the 11 UNVERIFIED rows are blocked on book chapters that web
search cannot open. Claude is likely to return UNVERIFIED again on those
for the same reason. Gemini has previously reached textbook and
monograph content the other models could not, so those specific rows may
be a Gemini job rather than a Claude one -- worth deciding after
Prompt 2 comes back and you can see which rows actually moved.

---

*Prepared August 12, 2026 with Anthropic's Claude Opus 5, against the
repo at `00219d9852c65d653ae49855d3138050dd8f76dd`.*
