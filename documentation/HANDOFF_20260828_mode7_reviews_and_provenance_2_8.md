# HANDOFF 2026-08-28 -- the Mode 7 reviews, provenance-discipline 2.9, and what is now next

**Built on orrery `a263f73d473bd2cd9de8241372ee9d1885045d04` at
https://github.com/tonylquintanilla/palomas_orrery (branch main),
gallery `4127da3d49bac112d773888e93d657fbae293316` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch
main). Both confirmed against the live remote 2026-08-28.**

Session base was `7f4a2f9f`. Two patches landed and pushed; a third is
delivered and unrun.

---

## READ THIS FIRST -- two carried obligations

**1. Stale Skill = Stop cannot be cleared by the session that bumps a
skill.** `provenance-discipline` went 2.7 -> 2.8 -> **2.9** across this
session. The session that wrote them loaded 2.7 and stayed on 2.7,
because a reinstall lands in the account and is invisible to a running
conversation.

**The next session confirms its loaded copy reads 2.9 before doing any
provenance work.** If it reads 2.7 or 2.8, stop and reconcile -- do not
proceed and mention it afterwards.

**2. TWO patches are delivered and NOT run**, and either order works.

`patch_L256_3_gate_binds_at_export.py` -- provenance-discipline 2.9 and
protocol v3.46. Guarded against `a263f73d`.

`patch_L255_2_write_missing_ledger_block.py` -- the L-255 ledger block.
Also guarded against `a263f73d`. If `ledger_index.py` has been run and
committed since, its guard will refuse and it must be re-cut.

**3. One ledger edit is owed and was deliberately not patched.** L-256's
DETAIL block should gain a line recording the 2.9 correction. It was
left out because the ledger's fingerprint depends on whether
`patch_L255_2` and `ledger_index.py` have run, and guessing would make
the patch refuse for the wrong reason.

---

## What this session was

A review of two independent Mode 7 Part A responses (Claude Fable 5 and
GPT), then the rulings they produced, then the skill and protocol
changes those rulings required.

Part B was **retired unsent**. Both reviewers had independently
produced most of its proposal from Part A alone -- GPT derived all four
parts, Fable three -- so sending it would have returned our own
reasoning with our name on it, converting independent corroboration
into agreement-with-self. The two-dispatch rule had already done its
job. Recorded rather than quietly dropped, because the decision was
made by a Claude session about a Claude proposal and that is a real
interest to disclose.

---

## Tony's rulings, 2026-08-27 and 08-28

**The Access Standard.** "If we can't access from an open paper, an
abstract or a google scholar search with context then the citation
fails. No paywalls. I don't have access to a research library." Books
are held to the same test and are searchable through Scholar.

**The reader of an exhibit is Claude, not Tony.** "Honestly I don't
intend to go looking for quote text. Better would be links that I can
go fetch for you to read." The quotation stays required on a return as
a routing aid and a recall tripwire; the clearance is the source text
read in context.

**Measured is the goal, declared is the fallback**, promoted as soon as
possible. Where a source gives a RANGE, the range is stored as data and
the drawn value derived from it by a stated rule, with the reason for
the pick on the row -- not which end, but that the pick is declared.

**Status lives in `constants_new.py` and nowhere else.** "The status is
recorded in constants_new.py that's the only store again."

**Narrative documents are demoted, not deleted.** "The narrative can
stay we just don't use it as the primary reference just the backup."
The store answers provenance questions; the plan documents are backup.

**The gate binds at EXPORT, not at serving** (2026-08-28, correcting the
2.8 text written hours earlier). "I think provenance should be settled
before it leaves the orrery to the gallery cache. There is no provenance
checker in the gallery." Verified before the edit: `provenance_scanner.py`
exists only in the orrery repo; `gallery_cache_builder.py` lives in the
GALLERY repo and scores nothing. A gate at publication sits downstream of
the last checker in existence, across a repo boundary. The skill now
separates WHY (serving -- a visitor takes it as true) from WHERE IT FIRES
(export -- the last place a check can run), so it cannot drift back.

**Method belongs to the skill.** Three method questions were escalated
to Tony in one evening and all three were sent back -- the status-line
format, the mechanism for checking a citation, and which end of a range
to draw. The third came back as "Isn't #4 also a skill method?" after
Claude had conceded the principle two sentences earlier and escalated
anyway. Now a resident protocol rule.

---

## What landed and is pushed

| Item | State |
|---|---|
| `patch_L256_1_provenance_discipline_2_8.py` | RUN. 13 edits, 1094 -> 1536 lines |
| `patch_L256_2_protocol_v3_45_and_ledger.py` | RUN. 6 edits across 3 files |
| `ledger_index.py` | RUN. 251 blocks, no consistency problems |
| `skills_index.py` | RUN. Caught the 2.7 -> 2.8 transition and said so |
| `maintenance_run.py` | RUN. **11 of 11 gating checkers passed** |
| Skill reinstalled to account | DONE (unverifiable in-session -- see above) |
| `patch_L255_2_write_missing_ledger_block.py` | **DELIVERED, NOT RUN** |

**provenance-discipline 2.8** -- nine sections, four revisions. New:
The Gate Binds at SERVING, The Access Standard, The Status Line,
Measured Is the Goal / Declared Is the Fallback, The Exhibit
Requirement, A Cross-Check Retires With Its Value or Its Citation,
Observations Are Sourced Facts, Uncited Goes to the Ledger, Examples Go
Stale Like Values. Revised: the exhibit's reader; Gemini's book access
demoted to lead generation; the two-annotation criterion for
`V_CROSS_CHECKED` retired.

**Protocol v3.45** -- Method Belongs to the Skill added after The
Braid; v3.42 moved down to history so three entries stay resident.

**Ledger** -- L-256 (the bump and the status pass), L-257 (three
enforcement builds).

**Verified in the published bytes at `a263f73d`**, not from the
patches' own reports: skill 2.8, protocol v3.45, manifest row 2.8,
L-256 and L-257 present, v3.42 appearing once and only in history.

---

## Two numbers that did NOT move, and that is the finding

`maintenance_run.py` reports two checkers as report-only failures: 292
Tier-1 findings tree-wide, and the worksheet checker at 76 of 115
routed with 8 clean. **Both are identical to a baseline measured on an
unpatched copy before the patches ran.** Nothing this session touched
moved a number. The 292 is tree-wide; the gate is Tier-1 = 0 on the
active build path.

---

## The staging Tony set for the status pass

Three stages, and it is L-250 instantiated rather than a new structure
-- discovery enumerates and fixes nothing, remediation happens later in
slices.

1. **Beta: status only.** The Sun's nineteen values, plus one dict.
2. **Full: status only**, then an independent review pass.
3. **Implementation: confirm and fix along with the braid**, per body,
   at the ladder step that serves it.

**The beta needs a dict or it proves the format for 30 percent of the
store.** Measured at `7f4a2f9f`: 67 top-level assignments in
`constants_new.py` -- 46 literal scalars, 16 expressions, 3 dicts, 2
lists -- with the dicts holding 160 entries and the lists 14. About 236
statusable items, 160 of them inside dicts, and the Sun's nineteen are
all top-level scalars.

**Tony-action (decide):** which dict joins the beta.
`spectral_subclass_temps` (9 entries, flagged by Fable in August as an
uncited physical claim inside the store) or `CENTER_BODY_RADII` (18).

**Also open, from L-256 and L-257:** confirm or redirect both RICE
scores.

---

## The Sun's nineteen, already surveyed

`SUN_19_STATUS_WORKSHEET.md` (this session, read from the file at
`7f4a2f9f`) groups them by what needs doing. Headlines:

- **`RADIATIVE_ZONE_AU` holds 0.7 where its own comment says 0.713.**
  Under measured-is-the-goal it becomes 0.713. This is the chromosphere
  move, already made once on 2026-08-16.
- **`INNER_CORONA_RADII` is still cited to Golub & Pasachoff**, the
  work an independent nine-source read threw off `HELMET_CUSP_RADII` in
  August for giving no figure and no findable position.
- **`GRAVITATIONAL_INFLUENCE_RANGE_AU` names no work in its source
  line.** Nothing to fetch, so it cannot pass the access standard.
- **Four range-picks** -- core, inner corona, helmet cusp, inner Oort
  limit -- take the range-as-data treatment. Structural, so
  implementation, not the status pass.
- **Nine access checks queued.** Four probably clear in minutes; three
  are Science and PRL needing an arXiv or ADS route; two are textbooks
  and Tony's to search. `Suess & Nerney (2004)` was checked live this
  session and its abstract is open -- it clears at tier 2 with the
  qualifier intact.

**NASA ADS closes the pre-arXiv astronomy gap.** Oort 1950, Hills 1981
and Christensen-Dalsgaard 1991 all have free full text there. Worth
knowing before assuming a pre-1997 citation fails.

---

## Process failures this session, recorded not smoothed

**Three superseded states pulled forward from documents rather than the
store**, by the same session, inside three messages. The chromosphere
at 1.1 (from the SKILL's own worked example, retired in code eleven
days earlier). `HELMET_CUSP_RADII` described as a declared drawing
choice (true on 2026-08-20 under its old name `STREAMER_BELT_RADII`;
false after L-224 renamed, rehomed and re-sourced it two days later).
The DeForest 15-versus-17 question raised as unresolved when the row's
own review-note had already resolved it against ADS and Cranmer 2016.

Tony's diagnosis produced the status line: "we need to add the
provenance status of the data to constants_new.py so we don't keep
tripping over the same values again and again."

**The orrery push did not happen and the SHA round trip caught it.**
Remote HEAD read `32e13b63` while the reported SHA was `a263f73d`,
which the server rejected as an unknown ref. Gallery had pushed;
orrery had not. Two buttons in GitHub Desktop, gallery done last.
Detected in about ninety seconds, before anything was built on the
wrong base.

**A test-harness bug, not a patch bug, and it exercised a guard.** A
one-liner written to convert a file to CRLF truncated it instead --
`open(p,'wb')` evaluates before its argument. The patch's fingerprint
guard refused the empty file. That is the answer to "what would make
this check fail."

---

## What is NOT done

**The master plan is untouched.** Section 5a still carries the sentence
that a wrong ring radius "becomes something Tony's EYES can catch."
Fable's review contradicts it directly: Mode 5 catches frame errors and
factor-of-two errors, not seven percent -- the Alfven case was one
solar radius in fifteen and invisible at any zoom. That sentence is the
stated justification for the braid's ordering, so the correction is a
real edit and not a nit.

**The rendering ladder is still withheld.** The draft is at
`documentation/DRAFT_rendering_ladder_section.md`; the patch that would
write it into the master plan exists and has not been run. Four
amendments are owed from the reviews: a definition of *published*, a
per-step slice denominator stated before the step starts, a
whole-published-set revalidation sweep on every build (GPT's stated
condition of approval), and the transport hole. That last one is
now SHARPER than the reviews had it: `objects_config.json` is a hand copy
in the gallery repo, so under the export gate it is not a defence against
later drift -- it IS the gate's missing enforcement point. That raises
segment 2 above where both master plan documents place it.

**The golden-artifact mechanism is unrepaired.** Both reviewers
independently said replace the fourteen-field record with a frozen-input
fixture plus a small structural contract. Three findings stand: the
harness compares today's assembly to itself (`fp.compare(golden,
golden)`), three of fourteen fields change on every nightly build by
design, and the position tolerance is `0.001` RELATIVE -- about 150,000
km at Earth's distance, documented in `fingerprint.py` as Tony's to tune
and never tuned.

**L-257's three enforcement builds are unstarted.** The worksheet schema
does not yet require `quote` and `locator`; nothing parses `# Status:`;
the scanner still infers.

---

## Where the next session starts

**Housekeeping first, about half an evening.**

1. Confirm the loaded `provenance-discipline` reads **2.9**. If it reads
   2.7 or 2.8, stop and reconcile.
2. SHA round trip on both repos. Orrery `a263f73d`, gallery `4127da3d`
   at the close of this session.
3. Run the two unrun patches -- `patch_L256_3_gate_binds_at_export.py`
   and `patch_L255_2_write_missing_ledger_block.py` -- then
   `skills_index.py` and `ledger_index.py`, then `maintenance_run.py`.
4. Add the 2.9 line to L-256's ledger block.

**Then THE PRIORITY below. It goes ahead of everything else.**

---

## THE PRIORITY: the Sun, live in the interactive gallery

**Tony's ruling, 2026-08-28, at the close of the session.** He wants the
Sun visible on the public site. Not a dev page, not a local render --
the live page. "Even if it will need adjustments it should pass our
protocol." This goes AHEAD of the document work, the whole-store status
pass, and the golden artifact. None of those gates a Sun on screen.

**Three steps, roughly one evening each.**

**1. Close the Sun's nineteen values.** `SUN_19_STATUS_WORKSHEET.md`
(this session) lists them grouped by what each needs. Three need fixing:
`RADIATIVE_ZONE_AU` holds 0.7 where its own source says 0.713;
`INNER_CORONA_RADII` is cited to Golub & Pasachoff, a work already
removed from another row for giving no findable figure;
`GRAVITATIONAL_INFLUENCE_RANGE_AU` names no work at all in its source
line. Nine access checks queued, most clearable by Claude directly.
Write the status lines during the same pass -- one job, not two. Tony's
part: Mode 5 on the one value that moves.

**2. Add a Sun exhibit to `interactive.html`.** MEASURED at gallery
`4127da3d`, and this REVERSES an earlier framing: the live page ALREADY
carries the consent gate (29 references), Pyodide loading (28), the
`?exhibit=` parameter (8) and `100dvh` mobile handling. What it lacks is
any reference to the served cache. `gallery/solar_system_earth_test.html`
is the inverse -- it loads the assembler into Pyodide, fetches the
coverage index and `objects_config.json`, assembles and renders, and has
none of the page furniture.

So the move is to add an exhibit to the page that is already public,
which is what the `?exhibit=` scheme was designed for. It is NOT
"promote the dev page." **View-only, zero controls** -- the GUI harness
is ladder step 3 and stays a later conversation.

**Test the GitHub Pages path FIRST**, before anything else in step 2.
The dev page works over a local `python -m http.server`. Whether the
assembler package loads the same way when served from Pages is the one
real unknown, and it is better found early than late.

**3. Mode 5 on the render, then commit and push.** That is live.

**Attribution is not a blocker.** L-086 is still PROPOSED and untouched
since 2026-07-03, and its own gap says it gates any publicly reachable
release. But the master plan already ruled the narrower path: an exhibit
carrying inline "Data: JPL/NASA" credit passes, kept UNLINKED from the
landing page until L-086 lands. That is how `interactive.html` has been
public since July. The Sun fits inside it comfortably -- it is a
features-only cache entry with no Horizons fetch, so its shells are our
own drawing from cited literature rather than redistributed data.

**A consequence for the ladder draft, which is still unwritten.** Step 1
reads "Render the Sun as is, and look" -- a local render, explicitly not
a publication. Tony has now declined that intermediate step. When 5b is
written, step 1 becomes the live exhibit and the local-look framing goes.

**No ledger handle yet.** Captured here on first mention; mint one next
session rather than guessing a free number now.

---

## After the Sun -- two tracks, independent

**The documents.** Section 5a's Mode 5 sentence, the ladder landing as
5b with its three gaps closed, and segment 2 repositioned. Two evenings.

**The status-pass beta.** Blocked on Tony's ruling of which dict joins
it -- `spectral_subclass_temps` at nine entries, or `CENTER_BODY_RADII`
at eighteen. Note the Sun's nineteen close during the priority work
above, so the beta's remaining job is the dict and the format proof.

**Do NOT reconstruct any of this by reading the source conversation.**
It contains four superseded states of its own -- the chromosphere at
1.1, the helmet cusp as a declared choice, the DeForest question as
unresolved, and the gate binding at serving -- each stated before its
correction. A transcript is a chronology with no status line, which is
the failure this session's work exists to prevent. This document states
final positions; the store settles anything it does not cover.

*Prepared 2026-08-28 with Anthropic's Claude Opus 5.*
