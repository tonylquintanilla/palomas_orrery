# DRAFT -- five sections for provenance-discipline 2.8

**Written 2026-08-27 with Anthropic's Claude Opus 5.** Orrery
`6ceb3f76c665a678d34a623aa47cb1cc0b427574`, gallery
`1a67b00d73813a1387ff1de7b77f8175c39c0f1e`, both read live. Measured,
not recalled.

**This is a draft to read, not a patch.** Nothing is written into
`skills/provenance-discipline/SKILL.md` yet. A skill bump also runs the
four-link chain (SKILL.md, `skills_index.py`, the manifest zone, a
protocol version entry) and cannot be verified from inside the session
that makes it, so it lands as a carried obligation for the next one.

---

## The Gate Binds at SERVING [CRITICAL]

Provenance binds where a claim reaches a reader, not where it is drawn.

Drawing a shell locally gates nothing. It costs an afternoon to undo and
nobody outside the room sees it. SERVING it to the interactive gallery
is different: a visitor takes what the site shows as true, and there is
no point downstream of the orrery where a wrong radius is caught -- not
the builder, not the resolver, not the browser. None of them knows what
a correct ring radius is.

So each rendering step closes its own provenance slice BEFORE it ships,
and the slice is bounded by what that step serves.

This EXTENDS the earlier line that the asymmetry "governs what an
artifact may LOCK, not what may be BUILT." That sentence was about
fingerprinted golden artifacts and is not withdrawn. Publication is the
sharper boundary.

The braid is intact: the audit stays bounded by the current artifact,
stays countable, and stays off the critical path as a gate. What moved
is where it binds.

**What the provenance leg requires, and what it does not.** It requires
Tier-1 = 0 on what is served -- cited, and TRUE. It does NOT require a
cross-check. A cited claim that has not been cross-checked scores 15,
which is Tier 2 REVIEW, and Tier 2 has never gated a push. Cross-checked
is a higher rung earned deliberately, not a condition of clearing
Tier 1.

(Tony's ruling, 2026-08-27. Worked case: the Sun's served features carry
111 numeric values -- 85 declared drawing parameters, 26 measured sites
holding 19 distinct values. Each measured field carries both a `source`
string and an `orrery_constant` pointer, and nine of nine served numbers
checked matched the store constant they name. That is a closed slice.)

---

## Observations Are Sourced Facts, and They Migrate [CRITICAL]

An observed event figure is a measured value with a source, and its home
is `constants_new.py` like any other.

A disintegration radius, a spacecraft's closest approach, a crossing
distance, a perihelion -- these read as narrative rather than as
constants, so they get typed into prose and stay there. They are
observations of the physical world with an authority behind them, and
One Value, One Home applies to them without exception.

The scope boundary is unchanged: MEASURED values migrate, DECLARED
drawing parameters stay where they are drawn.

The practical consequence is an ordering one. A citation cannot move
into the store ahead of the value it cites, because a citation with no
value beside it has nowhere to sit. So the migration is: value first,
then its source line, then the prose references the constant.

(Tony's ruling, 2026-08-27. Founding case: MAPS C/2026 A1's
disintegration at 8.33 R_sun is cited to SOHO/CCOR-1 observations at
`solar_visualization_shells.py` line 1226, and the figure itself lives
only in display strings.)

---

## Uncited Goes to the Ledger, Not the Bin [QUALITY]

When a claim outside the current slice has no citation, the disposition
is a DOCUMENTED LEDGER ROW for later sourcing -- not deletion.

Fetched-vs-Recalled's third branch (remove the claim and note the gap)
governs a claim that cannot be sourced against any authority. It does
not govern a claim nobody has sourced YET. Those are different states
and treating them alike destroys content that is merely waiting its
turn.

Per the braid: ONE ledger row per CLASS, never one per instance, so the
backlog grows by kinds rather than by counts.

**Before recording anything as uncited, check whether it is cited
ELSEWHERE in the same file.** The scanner reads a fixed lookback window,
so a real citation two hundred lines away reads as absent. A run of bare
string globals can sit far below the Source comments that cover them,
and the remedy there is to ATTACH the existing citation, not to drop the
sentence.

(Tony's ruling, 2026-08-27: "not eliminated -- documented for citation,
just not today." Worked case: `solar_visualization_shells.py` carries 26
Source blocks, 22 of which already name their store constant, while six
display-string findings 250 lines below them read as uncited. Tree-wide
the display-string class is 284 Tier-1 findings holding 553 claims,
which is why it is recorded by class and worked in slices.)

---

## A Cross-Check Retires With Its Value or Its Citation [CRITICAL]

A `# Cross-checked:` leg certifies one value against one citation on one
date. When either the value or the citation is replaced, the leg is
STRIPPED in the same patch, and the reason is recorded in the block.

Two ways this fires, and the store carries a worked case of each:

- **The value moved.** `ALFVEN_SURFACE_RADII` went 18.8 to 19.7 on
  2026-08-19 because 18.8 was an altitude used as a heliocentric radius.
  The two legs dated 2026-08-02 had certified 18.8 and were stripped
  with it: a check of the old value is not a check of the new one.
- **The citation went.** `HELMET_CUSP_RADII` held its value while its
  entire citation stack was removed on 2026-08-20 after an independent
  nine-source read. Its two legs went with the citations: a cross-check
  of a citation that no longer exists grants credit for nothing.

Leaving the leg standing is cite-to-clear wearing a checker's name. It
passes the scanner while certifying something that is no longer in the
file.

Record the removal in the block with its reasoning, because a removal
leaves no trace otherwise and the next reader should not have to
re-derive why a constant is uncited.

---

## The Exhibit Requirement [CRITICAL]

**A verdict without a quotation is UNVERIFIED, whatever the verdict
says.**

A leg that read the document can quote it. A leg that recalled restates
the citation it was given. That difference is a property of the RETURN,
not of the claim, so detecting it needs no domain knowledge and no
second opinion.

The worksheet schema gains two required fields:

- **quote** -- verbatim text from the named source containing the claim.
- **locator** -- where in the document: DOI, bibcode, section, table,
  page, or a resolvable URL.

State both IN THE PROMPT alongside the verdict vocabulary, and say that
a row without them will be recorded UNVERIFIED regardless of its verdict
token. A missing exhibit is not weighed, not averaged against another
leg, and not read as weak agreement. It is silence, and silence is the
correct output for a leg that did not read the source.

**What this changes about leg counts.**

- **Citation verification: ONE leg with an exhibit is sufficient.** The
  check moves from the model to Tony -- read the quote, see whether the
  claim is in it. That is a thirty-second check needing no astronomy,
  and it is falsifiable in a way a bare "confirmed" never is.
- **Value verification: TWO legs**, and only where a value must be FOUND
  rather than confirmed -- no source at all, or a citation check
  returned refuted and a replacement is needed.
- A leg returning no exhibit does not reduce the count. It contributes
  nothing.

**Measured, not assumed** (pilot returns at `6ceb3f76`, 138 rows):

| leg | rows | carried a quotation | carried a locator |
|---|---|---|---|
| Claude Opus 5 | 23 | 78% | 100% |
| GPT | 23 | 60% | 73% |
| Gemini | 92 | 1% | 28% |

The leg with no exhibits is the leg that confirmed `ALFVEN_SURFACE_RADII`
at 18.8 four times over, once describing it as a heliocentric distance
when it is an altitude. Its own notes field reads "Recollection of the
Parker Solar Probe 8th encounter results." Two legs concurring would
have kept the wrong number; the exhibit test separates them without
anyone knowing the answer in advance.

**Two limits, stated so they are not read past.** This is one dispatch.
It shows quote-presence separates a reading leg from a recalling leg; it
does NOT yet show quote-presence predicts correctness row by row inside
a single leg. And it puts a question against the Model Roles table's
claim that Gemini "can open the books" -- on this evidence Gemini
returned almost no exhibits, so that role needs re-testing rather than
assuming.

**Enforcement is a build, not prose.** This section states the rule. A
checker that refuses a row lacking `quote` or `locator` is a separate
item and needs its own handle, because a rule stated only in a skill is
a check that fires when somebody remembers it.

(Tony's ruling, 2026-08-27, on the failure he has actually seen: models
guessing and inventing. "Silence is better.")

---

## Field note -- a missing annotation is not missing verification

The absence of a `# Cross-checked:` line means no ANNOTATION. It does
not mean no work.

Verification lands in several places the annotation grammar does not
count: a `Resolved:` leg naming the returned verdict that caused an
edit, a `Record:` leg pointing at a source record in `documentation/`, a
`Review-note:` block carrying an independent read, and a convergence
report filed after a dispatch. A row can carry all four and still show
no cross-check.

Before reporting a value as unverified, read the block's other legs and
look for its source record. Say which claim is being made -- "carries no
cross-check annotation" and "has not been verified" are different
statements, and the first said carelessly is heard as the second.

(Origin, 2026-08-27: a session reported seven of the Sun's constants as
lacking cross-checks in a way that read as unverified. Two of the seven
were the most-worked rows in the file -- `ALFVEN_SURFACE_RADII` had a
three-model pilot dispatch behind it, recorded in
`PILOT_CONVERGENCE_20260819.md`, and `HELMET_CUSP_RADII` rested on a
paper Tony retrieved from NASA ADS himself, recorded in
`documentation/SOURCE_suess_nerney_2004_helmet_extent_20260821.md`. The
annotations were absent because the earlier legs had been correctly
stripped, which is the section above working, not a gap.)
