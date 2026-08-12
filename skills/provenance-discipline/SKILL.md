---
name: provenance-discipline
description: Provenance and citation discipline for the Paloma's Orrery project. Use whenever running or discussing provenance_scanner.py, reading PROVENANCE_AUDIT.md, clearing Tier-1 findings, adding or reviewing # Source: citations, editing provenance_exceptions.json, embedding constants or numeric/factual claims in orrery display strings or data modules, or preparing a GitHub push (the gate is Tier-1 = 0 on the active build path). Also use when composing on-layer or user-facing factual text for any orrery visualization. Do not use for projects other than Paloma's Orrery.
fires_when: Scanner runs, audits, citations, constants, pre-push (Tier-1 = 0 on the active build path)
---

# Provenance Discipline

Skill version: 1.9 | Cut from palomas_orrery @ cdcdb4b (v1.9), earlier
@ 8e4b5ca (v1.8), @ 3398970 (v1.7) | August 11, 2026
Source: project_instructions_v3_29.md Part 3 (Provenance Audit, Fetched vs
Recalled) + food insecurity build handoff + scanner source at HEAD. v1.1
adds the report domain-classification mechanics, the Review-Repair
Protocol (promoted from documentation/provenance_audit_handoff_v4.md),
and field notes from the F1 provenance-cleanup groundwork session (July
2026): the by-file/by-file-type report breakdown, a self-referential
scanning quirk, and a stale-audit-doc near-miss. v1.2 updates the
role-driven-inclusion bullet for L-163 Phase 3: a coverage gap is
resolved by tagging the module's own docstring, since ROLE_MAP is now a
regenerated mirror rather than a hand-maintained dict. MODULE_DOMAIN_MAP
and classify_domain() are unaffected and remain hand-maintained. v1.3
adds No Shadow Constants [CRITICAL]: local copies of constants_new.py
values must be deleted and replaced with proper imports -- a frozen copy
bypasses the citation chain and drifts silently, same failure class as
citing over recalled data. v1.4 rewrites Review-Repair Protocol step 2:
cross-checking is the competitive pattern (same worksheet, independent
models, Tony compares), not one model reviewing another's output.
v1.5 adds Model Roles (tested roles for Claude, GPT, Gemini, Fable in
the competitive pattern -- emerged from the Mars and constants_new.py
cross-check sessions, August 2026), two worksheet types (value
verification vs citation verification), the Cross-checked annotation
format, and the Batch Worksheet Workflow. v1.6 adds two rounds to that
workflow (blind source lookup and the Fable consistency audit), the
model-credit convention, the retirement of the `# Verified:` stamp
format, Geometry Constants as First-Class Claims, and three field notes
-- all earned in the L-156 Phase 2 Batch 1 cross-check and the Fable
shell-consistency audit, August 3-4, 2026. v1.8 adds Worksheet First,
Annotation Second (an annotation naming a worksheet that does not exist
is cite-to-clear in the annotation's own format) and the field note that
an evidence artifact is filed as received -- both earned August 10, 2026,
when a recovered worksheet proved an annotation true that the session had
already talked itself into calling fabricated.
v1.9 narrows The Goal State to the ACTIVE BUILD PATH gate Tony
ratified 2026-08-05 (L-184), keeping global Tier-1 = 0 as the
stated destination rather than the firing rule. The skill had
carried the retired global gate for a week; caught by Fable's
document-layer claim audit, finding F1, August 11, 2026.

The resident protocol carries the two governing principles as CRITICAL
gates: Fetched-vs-Recalled (a citation is a provenance claim that must be
TRUE; source-then-cite, never cite-to-clear) and Show the Envelope of the
Unknowable. This skill carries the working procedures and the scanner's
mechanics. If this skill and the resident gates ever seem to disagree, the
gates win -- flag it.

## The Goal State

**The push gate is Tier-1 = 0 ON THE ACTIVE BUILD PATH** -- the
files the project is currently building. As of August 2026 that is
the interactive gallery build path (Tony ratified 2026-08-05;
recorded in L-184). The scope MOVES with the work: when
Earth-science visualization work resumes, those files become the
gated path in turn.

**Global Tier-1 = 0 is the destination, not the current gate.** It
was suspended, not retired. At 206 Tier-1 findings a global gate
blocks every push forever, and a rule nobody can obey stops being
read as a rule at all. The global number is approached by clearing
paths as they go active -- which is why the gate is written
active-path rather than pinned to one named path.

Do not enforce the global form on a push outside the active path,
and do not read a bare "Tier-1 = 0" anywhere in this project as
the global form unless it says so. (Tony's ruling 2026-08-11, on
Fable audit finding F1: this skill and the protocol's manifest row
carried the global gate for a week after the ratification narrowed
it, while Tony pushed five times in one evening against it. A gate
that is routinely and correctly ignored is worse than a wrong
number -- it teaches the reader to ignore gates.)

A clean audit can rest on honest
removals: "Tier-1 = 0" does not imply "every claim sourced" -- it can mean
unsourceable claims were correctly stripped pending real sourcing. Record
which. The scanner must stay maintainable with accepted false positives,
not require regular manual intervention.

## Clearing a Flagged Claim (the only two moves)

1. Cite to where the data ACTUALLY came from, or
2. REMOVE the claim and NOTE the gap.

Never cite-to-clear. A # Source: over recalled data passes the check while
asserting a provenance that does not exist -- wrong-but-cited is worse than
uncited, because the citation suppresses the suspicion that would catch it.
A blank with a flag is honest; an unsourced assertion is not.

### Geometry Constants Are First-Class Claims

A `radius_fraction` in `shell_configs.py` is a provenance claim exactly as
much as a number in a display string. It asserts a physical size; it is
just written in units of body radii instead of km.

**When a cross-check corrects a display value, the constant moves in the
SAME patch.** Not deferred, not a follow-up. Batch 1 moved Mercury's outer
core text from 2,074 km to Hauck's 2,020 km and left `radius_fraction` at
0.85 -- so the shell kept drawing 2,074 km while the hover asserted 2,020.
Six shells across four bodies were in that state, and every offline test
passed the whole time.

**The scanner cannot catch this.** It flags numeric tokens in display
strings; `radius_fraction` is a dict constant with no unit attached, so it
is invisible to `NUMERIC_CLAIM_RE`. There is no scanner fix that would
help -- the constant is not wrong in isolation, it is wrong RELATIVE to a
string somewhere else in the file. That relation is what the Fable
consistency audit checks (workflow step 8), and it is the only thing that
does.

Record the derivation in the comment, so the next reader can re-run it:

```python
'radius_fraction': 0.828,  # 2,020 km / 2,439.7 km (Hauck et al. 2013)
```

## Review-Repair Protocol for Cross-Checked Annotations

**No model is its own verifier.** Clearing findings and earning
Cross-checked annotations is a multi-model competitive process, not
something any single AI does solo:

1. **Claude (orchestrating instance) preps a worksheet prompt.** Group
   claims by file, present each as a numbered claim with its current
   value and citation, and flag anything suspicious. The prompt is
   SHA-anchored (`built on <SHA> at <URL>`), includes the source code
   being checked, and specifies the job type (see Worksheet Types below).
   Claude does NOT propose corrected values -- only what needs checking.
2. **Tony sends the same prompt to Claude, GPT, and/or Gemini
   independently.** Same prompt, independent answers. Tony compares.
   Convergence builds confidence; divergence flags where to dig. This
   is NOT one model reviewing another's output -- all work from the
   original claims, not from each other.
3. **Claude (orchestrating instance) compares the worksheets** and
   produces a convergence/divergence report. Tony decides on
   divergences.
4. **Claude builds a transactional patch** with the confirmed fixes
   and Cross-checked annotations.

**Why the worksheet format matters for every checker.** The same
"fetched not recalled" rule that governs Claude's citations governs all
cross-checkers. A known failure mode is fabricating authority from
training memory when the output format allows ungrounded narrative. The
structured worksheet does not -- it forces primary source citations per
cell. Constrain the format, and the discipline follows.

### Model Roles in the Competitive Pattern

Tested and validated in the Mars and constants_new.py cross-check
sessions (August 2026). These are demonstrated strengths, not
assumptions.

| Model | Demonstrated strength | Use for |
|-------|----------------------|---------|
| Claude (Opus) | Derivations, citation-shape errors (catches when a source cannot contain the claim as written), honest about limitations (marks UNVERIFIED rather than bluffing) | Primary checker: papers, web sources, derivations, structural analysis |
| GPT | Papers with DOIs, explicit derivations with worked math, thorough web sourcing, catches date/year errors in citations | Primary checker: independent of Claude, complementary source selection |
| Gemini | Book citations (can access book content web search cannot reach), domain knowledge, structural/philosophical dialogue | Book-citation verification, domain review, tiebreaker when primaries diverge |
| Fable | Large-context comprehensive review, far-reaching audits across many files, pattern recognition at scale | Cross-codebase audits, manifest generation, bulk review when scope exceeds a bounded session |

**Default two-leg pattern:** Claude + GPT independently. Covers papers,
web sources, derivations, NASA/JPL data.

**Gemini escalation:** When either primary leg marks items UNVERIFIED
due to book citations, or when Claude and GPT diverge on domain-knowledge
questions. Also effective as a third independent leg when sent the same
prompt (tested: all three models received the same constants_new.py
remaining-items prompt; complementary coverage emerged naturally).

**Fable escalation:** When the scope of review exceeds what a bounded
session can hold -- auditing an entire manifest, reviewing cross-file
consistency, or pattern-matching across the full codebase. Not for
per-claim worksheet work (Opus handles that), but for the architectural
view that requires seeing everything at once.

**Key finding (August 2026):** Gemini can "open the books." It
demonstrated access to Carroll & Ostlie and Golub & Pasachoff content
that neither Claude nor GPT could reach via web search. This is a real,
tested capability -- not assumed from marketing. Use Gemini specifically
for book-citation verification and domain claims that rest on textbook
authority.

### Worksheet Types

Two types, same format, same competitive pattern, different job:

**Value verification:** "Is this number right?" The checker independently
researches each claim against primary sources, without seeing what the
other checker found. Catches wrong values behind correct-looking
citations. Used for shell modules (Mars was the first: bow shock 1.5
should have been 1.64, Hill sphere 324.5 should have been 320).

**Citation verification:** "Does the cited source actually contain this
value?" The checker goes to the stated source and confirms the value
appears there at the stated precision. Catches citations that point at
sources that don't contain the claimed value -- right number, wrong
provenance. Used for constants_new.py (IAU B3 cited for Mars/Saturn/
Uranus/Neptune radii it doesn't define; heliopause arithmetic used 123
AU where the source says 121.6).

Both types use the same worksheet table format:

| # | Claim/Constant | Value | Source | Verified? | Notes |

The distinction matters because the same file can need both: a shell
module's display text needs value verification while its `# Source:`
comments need citation verification.

### Cross-Checked Annotation Format

```python
# Source: Vignes et al. 2000, GRL 27, 49 -- subsolar bow shock 1.64 R_M
# Cross-checked: Vignes et al. via Claude 2026-08-01 (worksheet_claude_mars_visualization.md)
# Cross-checked: Vignes et al. via GPT 2026-08-01 (track1_gpt_independent_worksheet_mars_visualization.md)
```

**Source leads, model is subordinate, worksheet is the audit trail.**
The source names the authority. The model names who found it. The
parenthetical worksheet reference points to the evidence on disk. The
ISO date is the check date, not the publication date.

#### Worksheet First, Annotation Second [CRITICAL]

If no worksheet file exists on disk, the annotation does not get written.
Save the exchange as a `.md` in `documentation/` first, then write the
annotation against the real filename.

The parenthetical is a PATH, and a path that resolves to nothing asserts
an audit trail that cannot be walked. That is cite-to-clear wearing the
annotation format -- and it is worse than a bare `# Source:` line,
because the annotation's whole promise is that the evidence is on disk.

Two failure shapes, and they need different fixes:
- The check happened but was never filed. Recoverable: find the exchange,
  file it as received, repoint the annotation. Eight annotations in
  `constants_new.py` were in this state and were repaired on August 10
  once Tony recovered the worksheet.
- The check never happened. Not recoverable by filing anything. Strip the
  annotation, and re-run the claim through the workflow.

Do not write the annotation planning to file the worksheet afterwards.
The gap between the two is where the first shape comes from.
For derived values where the source is a computation, not a lookup:
```python
# Source: Derived from NASA NSSDCA Mars Fact Sheet (a, GM_Mars)
#         via standard Hill approximation, Claude Opus 5 2026-08-01
```

For visualization boundaries where the value is a display choice, not
a measured constant:
```python
# Visualization shell radius (physical chromosphere extends ~2000 km
# above photosphere = ~1.003 R_sun; drawn at 1.1 for visibility)
```

The scanner requires two `# Cross-checked:` lines with distinct
(identity, reference) pairs for V2 scoring. Same source from different
worksheets counts as two independent checks.

### Retired: `# Verified: April 2026 via Gemini fact-check`

This format is RETIRED. Do not add it; replace it on sight during a
cross-check batch. It records that a model looked, and nothing else --
no authority, no worksheet, no date that means anything, nothing a later
session can re-check. A `# Cross-checked:` line carries all four: the
authoritative source (not the model's name in the source position), the
model that ran the check, the worksheet on disk, and the ISO check date.

The stamp is worse than absent, because it stops the next reader from
looking. A `# Verified: April 2026` line sat over Eris's Hill sphere
while it read 9.4 Mkm against a correct ~14.3 Mkm -- a 34% error under a
verification stamp.

Census at `1e60c783`: 42 remaining -- shell_configs.py 14, earth 13,
jupiter 9, comet 6. Zero in the five Batch 1 modules and zero in Mars,
which were cleared as those batches landed. (Two came out of
shell_configs.py with the Mercury and Moon body headers in the geometry
follow-up, from 16.) The rest clear in Batch 2.

### Batch Worksheet Workflow

For scaling the competitive pattern across many modules:

1. **Claude prepares worksheet prompts** (one per file, SHA-anchored,
   with the file's claims extracted from the scanner findings).
2. **Tony sends each prompt to Claude + GPT independently.** Multiple
   file prompts can go in one session per model.
3. **Tony uploads both worksheets; Claude compares** and produces the
   convergence/divergence report per file.
4. **Tony decides on divergences.** Unresolved divergences go to Gemini
   or GPT as tiebreaker.
5. **Claude builds a transactional patch** (fixes + annotations) per
   file or per batch.
6. **Gemini gets targeted prompts** only for items both primaries
   marked UNVERIFIED (typically book citations).
7. **Blind source lookup**, when models converge suspiciously or diverge
   in a way that smells like anchoring. Every earlier round shows each
   model the value already in the code, which invites confirming it. So
   run a round with the expected value REMOVED: present the claim text
   only, and ask each model to source it cold. Batch 1 ran 8 items this
   way; 4 reached a primary source and 4 came back honestly unsourced --
   and it is what caught Mercury's sodium tail at 10,000 R_M (observed
   range is ~120 to ~1,400) and re-attributed Eris's 875 K core.
   A "NOT FOUND" from a blind round is a RESULT, not a failed round: it
   is how a claim earns removal rather than a softer citation.
8. **Fable consistency audit**, after the patches land. Full-codebase
   pass checking visualization CONSTANTS against display TEXT, and
   mapping every duplicated value for the single-source-of-truth
   migration (L-181). This catches what the per-claim worksheet
   structurally cannot: the worksheet asks "is this claim right?", never
   "does the geometry still agree with it?" Batch 1 corrected text and
   citations across five modules and left six `radius_fraction` values
   drawing the pre-patch physics. Prompt:
   `documentation/PROMPT_fable_shell_consistency_audit.md`; report:
   `documentation/FABLE_shell_consistency_audit_report.md`.

This keeps Gemini's book-access strength aimed where it matters rather
than diluted across routine web-checkable claims.

### Model Credit in Annotations [PRACTICE]

Name the model that produced each check in the `# Cross-checked:` line.
This is not vanity -- it is the record of WHICH LEG found the finding,
and it is the only way to see afterwards whether the legs were actually
independent.

```python
# Source: Hauck et al. 2013, JGR Planets 118:1204 -- core radius 2020 +/- 30 km
# Cross-checked: Hauck et al. 2013 via GPT 2026-08-03 (batch1_blind_source_lookup_gpt.md)
# Cross-checked: Hauck et al. 2013 via Gemini 2026-08-03 (batch1_tier2_cross_check_gemini.md)
```

**Two Claude passes are ONE leg, not two.** Same training data, same
priors, correlated errors. The same holds for two passes of any single
model. Two `# Cross-checked:` lines satisfy the scanner's V2 scoring
mechanically, but they only mean what they say if the identities differ.
Before writing the second line, check that the worksheet it names was
produced by a different model than the first.

And before citing any worksheet, confirm it exists on disk and contains
the finding. A parenthetical pointing at a plausible filename is the
citation-layer version of cite-to-clear.

Full multi-session history of this protocol (numbered Tier-1 items closed
via web_search + Gemini cross-check): `documentation/HANDOFF_provenance_
phase1_v17.md` and related handoffs. The originating rationale:
`documentation/provenance_audit_handoff_v4.md`.

## Scanner Mechanics (not obvious from the output)

- Flags by NUMERIC token (number + unit) via NUMERIC_CLAIM_RE. The unit
  vocabulary covers physical units (AU, km, deg, K, masses, radii, time
  units...) AND humanitarian units (people, persons, percent, %).
- A citation must sit WITHIN the LOOKBACK WINDOW of the flagged token and
  use the `# Source:` comment form. In-string "Source:" prose and distant
  comments do NOT count. A real citation outside the window, or in the
  wrong form, reads as uncited.
- File inclusion is role-driven (L-078): a module's display strings are
  extracted when its module_atlas.py ROLE_MAP role is in NARRATIVE_ROLES
  ({data, scenario, rendering, rendering/shells, computation}), OR its
  name is in the legacy narrative_files allow-list, OR it is a
  *_visualization_shells file. The allow-list is additive (a safety net)
  until ROLE_MAP is complete. A coverage-gap check reports modules the
  gate cannot classify -- resolve those by adding the Role:/Domain: tag to
  the module's own docstring, not by editing the scanner and not by
  hand-adding a ROLE_MAP entry (since L-163 Phase 3, ROLE_MAP is a
  generated mirror of those tags; the next module_atlas.py run overwrites
  anything hand-added).
- Loads data/provenance_exceptions.json for accepted residuals
  (suppression checks both context_text and raw_value). Run from a tree
  WITHOUT that file (e.g. a bare /mnt/project/ snapshot) and the count
  OVER-REPORTS. The confirming re-run is Tony-side, where the exceptions
  file lives.
- False positives get provenance_exceptions.json entries, not code
  workarounds.

## No Shadow Constants [CRITICAL]

Modules must not carry local copies of values that exist in constants_new.py. Import through the established shim (planet_visualization_utilities) or directly from constants_new.py. A local literal that numerically matches a tracked constant is a frozen copy -- it won't follow if the source value updates, and it bypasses the scanner's citation chain even when the number is correct today.

This is the code-side complement to the scanner's build_pinned_values() check: the scanner can flag a suspicious match, but the standing rule is that these should never be introduced in the first place. When found, delete the local definition and replace it with a proper import -- do not add a # Source: comment to the local copy, because that would cite-to-clear a structural problem rather than fix it.

Known precedent (FIXED in L-156 1f; kept as history): comet_visualization_shells.py lines 492-493 once hardcoded SUN_RADIUS_KM and KM_PER_AU despite KM_PER_AU already being imported, with line 602 deriving SUN_RADIUS_AU from the two local copies. Those lines now carry the fix comment recording the removal -- a reader sent to find shadow constants there will find the repair, not the defect. Same failure class as the close_approach_data.py stale-copy bug that originally motivated test_constants_provenance.py.

## Report Domain Classification (Findings by File / File Type)

Since July 2026, `PROVENANCE_AUDIT.md` breaks findings down two ways ahead
of the per-tier detail: **Findings by File** (every file with a finding,
tier counts, sorted worst-first) and **Findings by File Type** (the same
data rolled up by subject-matter domain).

Domain is a *report-only* grouping -- it answers "what part of the project
is this," not "what does this module do" (that's module_atlas.py's
ROLE_MAP, a different axis entirely; a module's functional role and its
domain are independent). Domain classification never affects which files
get scanned or how a finding scores.

Six domains: **orrery** (solar system bodies, orbital mechanics, core
app -- also the default catch-all), **earth_science**, **gallery**,
**stars** (stellar neighborhood, exoplanets, HR/planetarium), **utilities**
(genuinely cross-domain shared helpers), **dev_tools** (audit,
diagnostics, one-shot infra). The last two didn't exist before this round
-- they were split out, with the four-domain original (orrery, earth
science, gallery, stars) proving too coarse for files that don't belong to
any single subject-matter area.

Mechanics: `MODULE_DOMAIN_MAP` (a module-name-to-domain dict) plus
`classify_domain()` in provenance_scanner.py. Unmapped files default to
`orrery` and are tracked and surfaced in a "Domain coverage gap" note in
the report -- mirroring the existing ROLE_MAP coverage-gap pattern -- so a
new file with findings doesn't silently drift into the wrong bucket
forever. Extend `MODULE_DOMAIN_MAP` directly (not a heuristic) when a new
file needs a home; explicit mapping was chosen over name-pattern guessing
because domain assignment involves real judgment calls (several file
categorizations were confirmed with Tony directly rather than inferred).

**Gallery will usually read near-zero.** The gallery ASSEMBLER pipeline
(resolver.py, cache_reader.py, gallery_studio.py, json_converter.py,
render_orbits.py, etc.) lives in the separate tonyquintanilla.github.io
repo, entirely outside this scanner's reach. Only gallery-adjacent files
that live IN the palomas_orrery repo (currently just social_media_export.py)
can ever populate that domain here. Do not read a 0 there as "gallery has
no provenance debt" -- it means "gallery isn't scanned from here."

## Fetched vs Recalled -- the working procedure

Data from authoritative pipelines: trusted. Data from Claude's training
memory: verify or source -- and there is a THIRD branch: if a claim cannot
be sourced against an authority, REMOVE it and note the gap. Never embed
lookup tables from training memory. Tony's professional default: prefer
removing an unsourceable claim over citing it incorrectly.

Where a value is genuinely UNKNOWABLE (fixed by an input the model cannot
recover -- a rotation phase, an instantaneous azimuth): show the ENVELOPE
of possibilities as the honest object, and SAY SO in the hover where a
shape is approximate. Faking an unknowable value is the same failure
class as citing over recalled data. (Full treatment: resident protocol,
Show the Envelope.)

## Composed vs Transcribed On-Layer Text

For user-facing factual sentences (KMZ framing text, cards, briefings),
split by how the words get authority:
- TRANSCRIBED tier: the source's own words, lifted and attributed. Safe
  by construction.
- COMPOSED tier: sentences we write because no single source line says
  them. These get the strict treatment: BUILD the sentence in generator
  code with every numeric token carrying a `# Source:` comment within the
  scanner's lookback -- never pasted as a finished string into a template,
  and never living only inside an output artifact (a .kmz) where the
  scanner cannot see it. It must be scanner-visible at the construction
  site and clear by TRUE sourcing. A composed sentence that cannot be
  sourced does not ship.

## Field Notes

- **An evidence artifact is filed AS RECEIVED.** House style -- ASCII
  rules, naming conventions, header blocks -- applies to code and to
  documents we author. It does NOT apply to a document whose entire value
  is that someone else wrote it. A session took Tony's uploaded Gemini
  worksheet, converted its LaTeX to ASCII, stripped the markdown escaping,
  added a header block and a provenance note it wrote itself, and filed
  the result labelled as the Gemini worksheet. Tony caught it: "you have
  created a parallel unsourced worksheet not made by gemini." The corpus
  settled the question -- the existing GPT worksheet carries 115
  non-ASCII bytes and the earlier Gemini one 37, so there was no
  consistency to fix, only an assumed one. Reformatting an evidence file
  destroys the property that makes it evidence.
- **Unverified and true is still unverified -- do not over-confess.** Asked
  whether it had fabricated a `(Gemini worksheet)` annotation, a session
  gave an accurate account of its method (it had pattern-matched an
  adjacent annotation's shape without checking), then concluded from that
  the CONTENT was fabricated, called it cite-to-clear, and offered to
  strip the annotation. The recovered worksheet proved all three
  specifics it believed it had invented were true. Acting on the
  self-report would have deleted a real citation. Separate the two
  findings: the METHOD was wrong and is worth fixing; whether the CONTENT
  is wrong is a different question with its own evidence. An
  over-confession is as much a calibration failure as a denial, and it is
  more persuasive because it sounds like rigor.
- **Three wrong-paper citations survived into Batch 1 files**, each
  plausible enough to pass a reading. Mercury's crust cited "Pei" -- a
  mis-parsed GIVEN name read as a surname, so the author did not exist.
  Mercury's crust cited Sori 2018 for 35 km when Sori 2018 gives 26 --
  the cited paper REFUTED the value it was cited for. Eris's core cited
  Glein et al. for 875 K; Glein is a real author of a real paper on
  methane isotope geochemistry, but that paper does not contain 875 K,
  which comes from a different 2023 Science Advances paper. Three
  distinct ways to be wrong while looking right: a name that is not a
  name, a source that contradicts you, and a real author cited for
  someone else's number.
- A citation can be self-contradictory and still read as authoritative.
  Saturn's Hill sphere carries `# Source: ... ~91 million km / ~151
  Saturn radii confirmed` -- but 91 Mkm is ~1,510 R_S, so the two halves
  of the "confirmed" pair are a factor of ten apart, and neither matches
  the drawn value. The word "confirmed" over an internally inconsistent
  pair is cite-to-clear caught in the wild.
- **Verify the anchor SHA exists before trusting a document built on it.**
  An outbound prompt arrived anchored to a commit that was not in the
  repo -- it had been written but not pushed. The "does not exist"
  reading was correct at the moment of the check and resolved on push:
  the SHA round trip working exactly as designed, with the one failure
  mode honest and visible. Two repos in play makes this routine rather
  than exotic -- a HEAD that looks wrong may be the OTHER repo's HEAD.
  Check both before concluding anything.

- The scanner took ~10 sessions and multiple Gemini cross-checks to
  harden -- treat scanner changes as shared-CI changes with family-wide
  ripple (extending the unit vocabulary once exposed a pre-existing
  Tier-1 in star_notes.py that had been invisible).
- Fingerprint truncation was a prior scanner bug (fixed); if suppression
  behaves oddly, check fingerprints before assuming a data problem.
- Naive sums of source files can contradict the source's own published
  totals (overlapping units double-count). Transcribe headline figures;
  never compute them from parts unless the source says the parts sum.
  The full discipline for human-cost data is in earth-system-pipeline.
- Derive from known quantities; don't estimate manually.
- **The scanner scans itself, so editing provenance_scanner.py nudges its
  own self-scan numbers.** Adding a new module-level dict or descriptive
  string constant to the scanner (e.g. MODULE_DOMAIN_MAP, DOMAIN_LABELS)
  gets picked up as a claim-shaped unit in provenance_scanner.py's own
  audit entry, same as in any other file. This is correct behavior, not a
  bug -- but before assuming a total-findings delta after a scanner change
  means a real citation gap appeared somewhere in the project, check
  whether the scanner's own new code is the source of the delta first.
  (Observed July 2026: a report-formatting-only change to
  provenance_scanner.py shifted its total findings by +2, both new,
  correctly landing in the no-action tiers -- verified by diffing the
  before/after audit line by line, not by trusting the summary count.)
- **Multiple copies of PROVENANCE_AUDIT.md can exist and silently
  diverge -- verify which one you're reading.** The committed root-level
  file can go stale relative to a fresh scan (a small drift was observed
  directly: a committed doc claimed a different Tier-1 count than an
  immediate live re-run). Separately, an archived copy can sit elsewhere
  in the repo (e.g. under documentation/) dated months earlier. `cd`-ing
  into a subdirectory mid-session and not verifying `pwd` before reading
  "PROVENANCE_AUDIT.md" again is enough to silently read the wrong copy
  and draw a confidently wrong conclusion from it -- a real, self-caught
  near-miss this session. When precision matters (triage, before-citing
  a count), prefer a fresh live scan over any committed copy, and confirm
  the working directory before reading a same-named file a second time.

