# A cross-check round where every leg failed differently

Built on orrery `f1bceefd05eeee0cac38fd519dd207314acb2383`
at https://github.com/tonylquintanilla/palomas_orrery
Gallery at `40b7d566aaa5f350919afe7ccd0f1d5bfaa2d032`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io

**Nothing was pushed this session.** Both HEADs read the same at open
and at close, confirmed by `ls-remote` at both ends. Tony was away from
his machine for most of the session, so every artifact below is
delivered and UNFILED.

Tony Quintanilla, PE | Claude Opus 5 | 2026-09-13
Type: REVIEW + DISCOVERY (zero code shipped). Protocol v3.57.
Handles: L-321, L-323, L-305, L-325, L-314, L-276.

## STEP 0 -- Gates for the next session

- Skills version-checked at load, all matching the manifest:
  `ledger-and-session-records` 1.11, `safe-file-editing` 1.11,
  `provenance-discipline` 2.11. **No skill was bumped. Nothing
  travels** -- but 2.12 is drafted and waiting (see OPEN).
- `git ls-remote` both repos. If either has moved, Tony filed this
  session's artifacts; read what landed before building.
- Five files were produced and none is in the repo. They are listed in
  the Tony-action rollup.

## WHAT HAPPENED

The session opened as a handoff verification and became a citation
round with four checker legs.

1. **Fable's review of the 2026-09-12 handoff was verified against the
   repo rather than taken on faith.** Its stale-anchor finding was
   right: the L-321 prompts were anchored at `62ee5149`, and
   `constants_new.py` is the one file of four that moved before
   `f1bceefd`. At the old anchor a checker resolving `[store value]`
   would have read the sixteen-digit magnetopause literal and the bow
   shock expression that L-325 retired. `patch_L321_reanchor_prompts_rev3.py`
   was built, pre-tested on a throwaway copy, and is unrun.
2. **The worksheets had already gone out** from a crossed message in the
   previous session, at the correct SHA with every number substituted.
   So the stale anchor reached nobody; the patch is a records fix.
3. **Four legs came back.** Fable 5.1 Medium, GPT 6 Medium, Gemini
   Flash 3.8, then later Gemini 3.1 Pro Extended Thinking and Fable 5.1
   High.
4. **GPT's URLs died in the clipboard.** Source names and access words
   survived, addresses did not, and GPT could not recover them. Three
   transcriptions were built with the gap marked inline and a banner
   saying no row may clear a citation until the addresses return.
5. **Gemini Flash 3.8 returned nothing usable** and said so plainly: it
   cannot fetch, so every Source cell reads WALLED. Gemini 3.1 Pro
   Extended Thinking, sent later, fetched three PDFs successfully.
   **The Flash returns are NOT filed in this repo** -- only the Pro
   ones are. That is deliberate and it is the one place this session
   leaves a claim without its artifact. The reason it is acceptable
   here and would not be for a citation: a CAPABILITY claim is
   re-testable in a single question, which is what the pre-flight rule
   in the 2.12 draft asks for, whereas a citation claim cannot be
   re-derived and has to be on disk. If the roster note is ever
   doubted, re-run the pre-flight rather than looking for the file.
6. **A source-recovery pass opened GPT's named sources by search**, on
   Tony's ruling, no additional cross check. Six real URLs recovered.
   Koskinen and Kilpua (2022) chapter 1, open access at Springer, was
   the decisive read.
7. **Gemini Pro's Intriligator finding was verified** before it went
   near a store row. It is real, correctly attributed, and does not
   mean what it looks like.

## WHAT THE ROUND DECIDED

**The belt extents are sourced, not unsourced.** Three open full-text
sources state them in geocentric Earth radii: Koskinen and Kilpua
(2022) sec. 1.1, Meredith et al. (2014), and Li, Tu et al. (2024). The
design record predicted UNSOURCED across the board and that prediction
was wrong. Item 7 is a citation job, not a removal job.

**Design record ruling B has lost its premise.** It holds that the
store carries L because the frame the sources state is L. Koskinen and
Kilpua state the extents in geocentric Earth radii and say so in the
chapter's own footnote 2; Meredith says "in the geomagnetic equatorial
plane", where the two coincide. The ruling may still be right. Its
stated reason is gone, and a session opening item 7 will read the
design record, not this handoff.

**Row 9's NO reverses.** The Fable Medium return called 60,000 km
physically impossible because 10.4 R_E sits outside the orrery's own
magnetopause. Koskinen and Kilpua put the outer belt's reach at 7 to 10
R_E. The belt's outer edge approaching the magnetopause is why
magnetopause shadowing is a standard loss mechanism.

**The magnetotail row holds 220 R_E.** Tony's ruling, 2026-09-13. Three
figures, three meanings: 220 (ISEE-3, coherent tail with neutral
sheet), 900-1050 (Ness 1967, connected field lines, intermittent over a
week, no coherent tail), 3100 (Intriligator et al. 1979, Geophys. Res.
Lett. 6:585, tail-ASSOCIATED phenomena, which later reviews read as
field lines disconnected from Earth). 220 is the only one where the
thing measured is the thing the hover names. Ness and Intriligator go
in the row's Source line as the more distant signatures.

**"Making complex life possible" does not survive.** Three legs
returned NO. Griessmeier et al. (2016), A&A 587 A159, open: at
Earth-like atmospheric pressure, weak or absent magnetospheric
shielding has a non-critical effect on biological dose rates. Gemini
Pro's lone YES rests on a NASA outreach page and the phrase "broadly
supported scientific consensus" -- recall wearing a citation.

**Two figures picked up a source in passing.** Koskinen and Kilpua
sec. 1.2 states the 11-degree dipole tilt, which the previous handoff
records as a measurement typed at a call site with no store row. The
same section puts the magnetopause nose near 10 R_E and the bow shock
about 3 R_E upstream of it -- independent textbook corroboration of
both standoffs.

## LESSONS WORTH CARRYING

Five are drafted as `provenance-discipline` field notes. They are not
repeated in full here; the draft carries the wording.

- **A negative verdict is the one verdict that cannot fail.** Every
  other token points at a document somebody can open. UNSOURCED points
  at nothing, so a checker that ran two queries and one that ran twenty
  return the identical cell. A DISCOVERY row has to show its search.
- **A source cell names what was opened, not what it cites.** Gemini
  named Usanova where the PDF was Meredith, and Ganushkina where it was
  Li and Tu. Right URL, right access word, right figure, wrong
  attribution -- invisible without a second fetch.
- **A link is an object, not text -- but the export is not the paste.**
  A hyperlink copied out of a chat arrives as a chip carrying no
  address, and the loss is silent. It is recoverable, from the file the
  checker itself exported, because a paste and an export fail
  differently. Ask for bare URLs in a code block AND keep the authored
  file; treat any transcription as derived from it.
- **A redundant artifact was the only copy of something.** Claude
  recommended deleting all six raw GPT copies as duplicates. Tony
  declined, on the argument that the checker's own files are the actual
  record. One of them held twenty addresses, including all four
  DISCOVERY-row sources. Redundancy looked like clutter right up to the
  moment it was the only copy.
- **Capability is a tier property, not a vendor property.** Gemini
  Flash 3.8 cannot fetch; Gemini 3.1 Pro Extended Thinking can. L-276's
  constraint is about the interface and the tier.
- **A checker inside the Project is not independent for a rerun.** Past
  chats are searchable, so once an instance has seen the answer a fresh
  session does not restore blindness. The Fable High tier test could
  not be run on worksheet 3 for this reason.
- **The round survived because its legs failed differently.** Fable had
  the discipline and missed the sources. GPT found them and lost the
  addresses. Gemini Flash had neither and said so. Gemini Pro found the
  one thing nobody else did and misnamed two of three others. No single
  leg would have got here, and that was luck rather than design.

## OPEN

1. **RULED, 2026-09-13: route the effort tier by job type.** DISCOVERY
   rows go to the highest tier available, CITATION rows stay at the
   working tier. Tony's ruling on the draft's note 5. Supporting
   evidence, not proof: Fable High on worksheet 1 opened Shue in full
   on Russell's UCLA site after Wiley blocked it, dropped row 3 to
   APPROX, and added ISEE-3 to row 7, where Medium had done none of
   those.
2. **Bump `provenance-discipline` to 2.12 -- the NEXT SESSION'S FIRST
   ACTION, ahead of item 7.** Nothing blocks it now, and the ordering
   is v3.55's: a bump taken before the build it serves is checked by
   the stale-skill gate against a matching manifest, instead of
   travelling as a promise. It was not taken in this session because
   the context was nearly spent, and a rushed edit to a 1712-line
   CRITICAL skill is how a bad rule ships. Note 3 of the draft was
   FALSE when written and was falsified four hours later in the same
   session; the draft-then-review gap is what caught it, which is the
   argument for the gap and against writing straight into the skill.
   Contents: the five method notes, the tier rule above, L-325's parked
   Gap, a Mode 7 reminder, and three field notes. Sequence is in the
   draft: patch SKILL.md, run `skills_index.py` (do not hand-edit the
   manifest zone), protocol entry v3.58, reinstall, ledger row.

   **The Mode 7 reminder splits four ways, on Tony's instruction of
   2026-09-13, and the split is the point -- two of these belong in the
   worksheet PROMPT, not in a habit Tony has to remember:**
   - *In the prompt:* pre-flight the checker -- ask it to open one
     open-access URL and quote a sentence before starting.
   - *In the prompt:* bare URLs inside a code block.
   - *Tony's own reminder:* do not reuse an instance that has already
     seen the round's answer, including inside the Project.
   - *Both:* record model AND tier -- in the prompt as a required
     response-header field, and in Tony's filing, where the filename
     convention already carries both.
3. **Design record revision 3** -- ruling B's premise, the four extents
   now sourced, row 9's reversal, and the magnetotail at 220. This is
   the one most at risk of being missed, because item 7 reads the
   design record rather than this handoff.
4. **L-305 item 7** -- now a citation job. Four belt scalars, the
   magnetotail row at 220, the outer peak's unit, the four typed
   extents becoming interpolations.
5. **Worksheet 1 row 7's loose end**, now closed: GPT cited a Fairfield
   1968 comparing Pioneer 7 against Explorer 28 and 33 at roughly 1,000
   R_E, and the Fairfield document opened under that title stops at 80.
   Fable High names Fairfield 1968, J. Geophys. Res. 73:6179, as not
   opened. Left unopened deliberately; 220 does not depend on it.
6. Unchanged from the previous handoff: **L-305 items 5, 6b, 8**,
   **L-322**, **L-318**, **L-316**, **L-319**, **L-313**, **L-314**,
   **L-315**.

### Deferred with a home

- **Three of GPT's sources remain without an address**, all from
  worksheets 1 and 2, which exported with no links at all: Urbar et al.
  (2019), Ingale et al., and Kumar and Pulkkinen (2025). The six named
  in the source-recovery finding for worksheet 3 -- Maiti and
  Ramachandran (2023), the University of Minnesota page, Y. X. Li et
  al. (2023), Selesnick et al. (2014), Li et al. (2015) and Shi et al.
  (2020) -- now carry URLs, recovered at `7bd5b1e8`. None of the three
  is load-bearing.
- **The two altitude pairs** (1,000-6,000 km and 13,000-60,000 km) rest
  on a magazine article, a news article and a university outreach page
  across three legs. No peer-reviewed source states either as written.
  They are item 7's to dispose of.

## TONY-ACTION ROLLUP

1. **(do)** File five artifacts. None is in either repo.
   - `patch_L321_reanchor_prompts_rev3.py` -- run it from
     `documentation/`, then leave it there.
   - `FINDING_L321_source_recovery_20260913.md` -> `documentation/`
   - `DRAFT_provenance_discipline_2_12_field_notes_20260913.md` ->
     `documentation/`
   - The three GPT worksheet transcriptions ->
     `documentation/worksheets/`, with the URL gap banner intact.
   - This handoff -> `documentation/`.
2. **(do)** File the Fable and Gemini returns under the naming
   convention: `worksheet_<model-slug>_L321_<subject>_20260913.md` in
   `documentation/worksheets/`. Slugs: `claude-fable-5-1-medium`,
   `claude-fable-5-1-high`, `gemini-3-1-pro-extended`,
   `gemini-flash-3-8`, `gpt-6-medium`.
3. **(decide)** Design ruling B -- keep L, or move the store to
   geocentric Earth radii now that three open sources state it that way.
4. **(decide)** Standoff precision. Fable High: the fit supports "about
   10", with 10.25 living in the store as the evaluated model value.
   The same question stands for 13.51.

Written September 2026 with Anthropic's Claude Opus 5.
