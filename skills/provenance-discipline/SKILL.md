---
name: provenance-discipline
description: Provenance and citation discipline for the Paloma's Orrery project. Use whenever running or discussing provenance_scanner.py, reading PROVENANCE_AUDIT.md, clearing Tier-1 findings, adding or reviewing # Source: citations, editing provenance_exceptions.json, embedding constants or numeric/factual claims in orrery display strings or data modules, or preparing a GitHub push (Tier-1 = 0 is the push gate). Also use when composing on-layer or user-facing factual text for any orrery visualization. Do not use for projects other than Paloma's Orrery.
fires_when: Scanner runs, audits, citations, constants, pre-push (Tier-1 = 0)
---

# Provenance Discipline

Skill version: 1.5 | Cut from palomas_orrery @ 225071f6 | August 2, 2026
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
format, and the Batch Worksheet Workflow.

The resident protocol carries the two governing principles as CRITICAL
gates: Fetched-vs-Recalled (a citation is a provenance claim that must be
TRUE; source-then-cite, never cite-to-clear) and Show the Envelope of the
Unknowable. This skill carries the working procedures and the scanner's
mechanics. If this skill and the resident gates ever seem to disagree, the
gates win -- flag it.

## The Goal State

Tier-1 = 0 before any GitHub push. A clean audit can rest on honest
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

This keeps Gemini's book-access strength aimed where it matters rather
than diluted across routine web-checkable claims.

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

Modules must not carry local copies of values that exist in constants_new.py. Import through the established shim (planet_visualization_utilities) or directly from constants_new.py. A local literal that numerically matches a tracked constant is a frozen copy — it won't follow if the source value updates, and it bypasses the scanner's citation chain even when the number is correct today.

This is the code-side complement to the scanner's build_pinned_values() check: the scanner can flag a suspicious match, but the standing rule is that these should never be introduced in the first place. When found, delete the local definition and replace it with a proper import — do not add a # Source: comment to the local copy, because that would cite-to-clear a structural problem rather than fix it.

Known precedent: comet_visualization_shells.py lines 492-493 (SUN_RADIUS_KM, KM_PER_AU hardcoded despite KM_PER_AU already being imported) and line 602 (SUN_RADIUS_AU computed from the two hardcoded values). Same failure class as the close_approach_data.py stale-copy bug that originally motivated test_constants_provenance.py.

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

