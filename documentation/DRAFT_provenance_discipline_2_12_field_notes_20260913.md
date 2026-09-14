# provenance-discipline 2.11 -> 2.12 -- draft field notes for review

Built on orrery `f1bceefd05eeee0cac38fd519dd207314acb2383`
at https://github.com/tonylquintanilla/palomas_orrery

Tony Quintanilla, PE | Claude Opus 5 | 2026-09-13
Type: DRAFT for review (zero code). Handles: L-321, L-325, L-314.

## Why this is a draft and not a patch

You are away from the machine, and these are rules that will load at
the start of every worksheet session and be followed without being
noticed. That is the failure direction Method Belongs to the Skill
warns about: a judgment absorbed into a skill becomes a rule nobody
ruled. So the wording gets your eyes before it gets installed.

The bump also needs three things done together in one push -- the
SKILL.md edit, a protocol version entry, and a ledger row -- and
`skills_index.py` has to regenerate the manifest zone rather than
anyone hand-editing it. All of that needs you at the machine.

Six notes below. Five are method. One is marked as yours.

---

## 1. A Negative Verdict Shows Its Search [CRITICAL]

Proposed home: alongside Worksheet Types.

> UNSOURCED is the one verdict that cannot fail. Every other token
> points at a document somebody can open and check. A negative points
> at nothing, so a checker that ran two queries and a checker that ran
> twenty return the identical cell, and the worksheet cannot tell them
> apart.
>
> So a DISCOVERY row carries a SEARCH LOG: the queries actually run,
> the terms tried, and where it looked. A negative is then inspectable
> -- you read the query list and see the hole.
>
> Say it in the prompt as a requirement of the row, not a courtesy:
> "no source states this" is a claim about the search, and a search
> nobody can see is a claim nobody can check.
>
> (L-321, 2026-09-13. A Medium-tier return marked three belt-extent
> rows UNSOURCED. Three open full-text sources state those figures --
> Koskinen and Kilpua 2022, Meredith et al. 2014, Li and Tu et al.
> 2024 -- and two later checkers found them. The verdict was honest and
> wrong, and nothing in the worksheet could have caught it. This is A
> Check That Cannot Fail Is Not Passing, at the worksheet layer.)

## 2. A Source Names What Was Opened, Not What It Cites [CRITICAL]

Proposed home: The Access Standard, after the snippet-qualifier rule.

> The Source cell records the document the checker OPENED. Not the
> paper that document cites for the claim, and not what the checker
> believes the document to be.
>
> The failure is invisible without a second fetch: right URL, right
> access word, right figure, wrong attribution. A row can be entirely
> correct about the literature and still send the next session to a
> paper nobody read.
>
> So the row quotes the TITLE AND AUTHOR LIST AS PRINTED in the
> document opened. One field, mechanical, and it fails visibly when a
> checker is reconstructing from memory instead of reading a title
> page. Where the figure is background the document passes on from
> earlier work, that earlier work is recorded as the next layer down,
> not as the source.
>
> (L-321, 2026-09-13. A checker returned two correct extents and named
> Usanova 2014 and Ganushkina 2011. The PDFs at those URLs are Meredith
> et al. 2014 and Li, Tu et al. 2024, each citing the named paper in
> its introduction. Two of three load-bearing rows; the third had
> opened a paper that cites the one it was asked to check.)

## 3. A Link Is an Object, Not Text [QUALITY]

Proposed home: with the worksheet prompt mechanics in step 1.

> Ask for bare URLs inside a code block. A hyperlink pasted out of a
> chat interface arrives as a chip carrying no address, and the loss is
> silent: source names and access words survive, addresses do not. A
> checker asked afterwards to reprint them has nothing left to reprint.
>
> But the paste is not the only artifact. KEEP THE FILE THE CHECKER
> EXPORTED. An export preserves addresses a paste destroys, so the
> authored file is the record and any transcription is derived from it;
> where the two disagree, the authored file wins. Downloading it is an
> operator action and belongs in the Mode 7 reminder, not only in the
> prompt.
>
> (L-321, 2026-09-13. Three returns lost every URL in transfer and the
> checker could not recover them. Twenty addresses came back anyway,
> out of its own exported markdown, after the recommendation to delete
> the authored copies as redundant was declined. One of those addresses
> matched, character for character, a URL an independent search pass
> had reached without seeing it.)

## 4. Model roster -- two corrections

Proposed home: the Model Roles in the Competitive Pattern table.

> **Gemini: the tier decides whether it can check citations at all.**
> Flash 3.8 cannot fetch; it declared so and returned a table with every
> Source cell WALLED. Pro 3.1 with Extended Thinking fetches -- it
> opened three PDFs in full. So the constraint recorded at L-276 is
> about the interface and the tier, not about Gemini, and a Flash tier
> is not a citation checker at any prompt quality.
>
> **A checker inside the Project is not independent for a rerun.** Once
> an instance has transcribed or reviewed a return, it has seen the
> answer, and past chats are searchable, so a fresh session in the same
> Project does not restore independence. A rerun meant to test search
> depth has to go outside the Project or not happen.

## 5. Route the Effort Tier by Job Type -- YOUR CALL

Proposed home: Worksheet Types.

This one is marked as yours because it spends your model access, and
because the experiment that would have proved it is no longer runnable
-- every Fable instance in this Project has now seen the answer.

The reasoning without the experiment:

> A DISCOVERY row asks a checker to establish a NEGATIVE across the
> literature. That is bounded by how long it keeps looking, which is
> what the effort tier buys. A CITATION row is bounded by construction
> -- open the named paper, find the sentence, stop -- and is cheap at
> any tier.
>
> So route DISCOVERY rows to the highest tier available and leave
> CITATION rows at the working tier.

Rule it, or leave it out and decide per round.

## 6. A Derived Row Stores the Figure Its Sources Support [CRITICAL]

This is L-325's Gap, which the 2026-09-12 handoff parked for this
bump. It is not from the worksheet round.

> A derived constant stores the figure its inputs actually support, not
> the arithmetic result. Sixteen digits on a value uncertain in the
> first decimal is calculator output, not precision. The arithmetic
> stays recorded on the row, so it remains auditable, and a check
> recomputes the row from the inputs its Status line names and FAILS
> when the rounding stops holding.
>
> An expression recomputes silently when an input moves, which is a
> published number changing with nobody looking. A literal plus a test
> announces instead.
>
> Scope: this governs rows whose inputs are DECLARED CONSTANTS. L-314
> may serve solar wind speed and pressure from the cache, and a stored
> literal guarded by a test that fails every time the wind changes is a
> test nobody reads. Re-examine when L-314 is designed.

The scope paragraph is carried straight from your own ledger note of
2026-09-12 under L-314. Say if you want it worded as a harder boundary
or dropped until L-314 lands.

---

## What running this looks like, when you are back

1. Patch `skills/provenance-discipline/SKILL.md` -- the five approved
   notes, version line to 2.12.
2. Run `skills_index.py` to regenerate the manifest zone in
   `PROJECT_INSTRUCTIONS.md`. Do not hand-edit that zone.
3. Protocol version entry v3.58, recording the bump and the
   obligation: this session loaded 2.11, and a reinstall cannot be
   verified from inside the session that makes it, so the NEXT session
   confirms its loaded copy reads 2.12 before provenance work.
4. Reinstall to the account profile, Settings > Skills.
5. Ledger row for the bump, and close L-325's Gap.

Written September 2026 with Anthropic's Claude Opus 5.
