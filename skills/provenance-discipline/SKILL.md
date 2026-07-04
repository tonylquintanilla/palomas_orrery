---
name: provenance-discipline
description: Provenance and citation discipline for the Paloma's Orrery project. Use whenever running or discussing provenance_scanner.py, reading PROVENANCE_AUDIT.md, clearing Tier-1 findings, adding or reviewing # Source: citations, editing provenance_exceptions.json, embedding constants or numeric/factual claims in orrery display strings or data modules, or preparing a GitHub push (Tier-1 = 0 is the push gate). Also use when composing on-layer or user-facing factual text for any orrery visualization. Do not use for projects other than Paloma's Orrery.
fires_when: Scanner runs, audits, citations, constants, pre-push (Tier-1 = 0)
---

# Provenance Discipline

Skill version: 1.0 | Cut from palomas_orrery @ b29ad3f8 | July 1, 2026
Source: project_instructions_v3_29.md Part 3 (Provenance Audit, Fetched vs
Recalled) + food insecurity build handoff + scanner source at HEAD.

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
  gate cannot classify -- resolve those by adding ROLE_MAP entries, not by
  editing the scanner.
- Loads data/provenance_exceptions.json for accepted residuals
  (suppression checks both context_text and raw_value). Run from a tree
  WITHOUT that file (e.g. a bare /mnt/project/ snapshot) and the count
  OVER-REPORTS. The confirming re-run is Tony-side, where the exceptions
  file lives.
- False positives get provenance_exceptions.json entries, not code
  workarounds.

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
