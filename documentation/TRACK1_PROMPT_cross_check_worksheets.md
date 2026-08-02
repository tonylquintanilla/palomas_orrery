# Track 1 Orchestration Prompt — Cross-Check Worksheets (Claude's Leg)

**Built on `373c6d8be9e0b5d06b0d5b445219e0d6d152fa13`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Verify fresh — Tony may have pushed ledger/master plan updates since.**

---

## Your role

You are Claude Opus 4.6, orchestrating Track 1 of L-156 Phase 2. Your
job is to independently verify claims in Paloma's Orrery source files
against authoritative primary sources. This is the second leg of a
competitive cross-check — Gemini already verified these same claims in
April 2026. Tony will compare your results against Gemini's.

You are NOT building code. You are researching facts and citing sources.

Tony Quintanilla is the integrator. He compares both models' results,
judges convergence vs divergence, and decides what gets annotated.

---

## What Track 1 is

The provenance scanner audits every numeric claim in the codebase. Many
claims carry a `# Source:` citation but have never been independently
verified. The V_CROSS_CHECKED (V2) rung requires the competitive
pattern: the same claims go to two models independently, both research
against primary sources, Tony compares.

Gemini did its leg in April 2026. Fifteen worksheets on disk document
what Gemini checked. You do the other leg now — same claims, independent
research. You must NOT read Gemini's April answers before producing your
own. Research each claim fresh against authoritative sources (NASA fact
sheets, ESA, JPL, peer-reviewed papers, USGS, IAU).

After Tony compares:
- **Convergence** (both models found the same value from independent
  sources) → high confidence, annotate.
- **Divergence** (models disagree) → discuss. If unresolvable, that
  specific claim goes to GPT as a third cross-checker.

Once Tony confirms which claims converge, Opus 5 mechanically inserts
the `# Cross-checked:` annotations into the source files. You don't
write annotations — you verify facts.

---

## Process

For each file:

1. **Read the source file from the repo** to see the claims as they
   exist in the code today (the values Gemini checked have already been
   corrected where Gemini found errors in April).
2. **For each numeric/factual claim, independently research** the
   correct value from authoritative primary sources.
3. **Present your findings** as a worksheet: claim, your independently
   researched value, your source, and whether it matches the code.
4. **Do NOT read the Gemini worksheet first.** Tony will compare after
   you've produced your independent results.

Your worksheet format for each claim:

```
| # | Claim in code | Your value | Your source | Match? |
```

Where "Match?" is whether your independently researched value matches
what the code says.

---

## Starting order (smallest files first to calibrate)

| Priority | File | Findings | Worksheet(s) |
|----------|------|--------:|-------------|
| 1 | `mars_visualization_shells.py` | 4 | `worksheet_mars_visualization.md` |
| 2 | `eris_visualization_shells.py` | 5 | `worksheet_eris_visualization.md` |
| 3 | `asteroid_belt_visualization_shells.py` | 7 | `worksheet_asteroid_belt.md` + `provenance_worksheet_tier1_final.md` |
| 4 | `mercury_visualization_shells.py` | 7 | `worksheet_mercury_visualization.md` |
| 5 | `jupiter_visualization_shells.py` | 18 | `worksheet_jupiter_visualization.md` |
| 6 | `comet_visualization_shells.py` | 23 | `worksheet_comet_visualization.md` |
| 7 | `earth_visualization_shells.py` | 27 | `worksheet_earth_visualization.md` |
| 8 | `star_notes.py` | 32 | `provenance_worksheet_stars_final.md` + `provenance_worksheet_stars_followup.md` + `provenance_worksheet_final.md` |
| 9 | `uranus_visualization_shells.py` | 24 | `provenance_worksheet_final.md` (partial) |
| 10 | `solar_visualization_shells.py` | 25 | `provenance_worksheet_final.md` (partial) |
| 11 | `info_dictionary.py` | 124 | 4 info_dict worksheets (mostly accepted residuals) |

Start with Mars (4 claims). If the process works, continue down the
list. If Tony sees problems with the approach, adjust before scaling up.

---

## Important constraints

- **Research against live authoritative sources.** Use web search. Do
  NOT answer from training memory — that is the failure class this
  entire mechanism exists to prevent. A `# Cross-checked:` over
  recalled agreement is the same as `# Source:` over recalled data.

- **Only sourced claims can be cross-checked.** If a claim in the code
  has no `# Source:` citation (V_RECALLED), it needs sourcing first,
  not cross-checking. Skip it and note it.

- **Claim-level, not file-level.** Don't say "the file checks out."
  Each claim gets its own row in the worksheet.

- **Divergence is valuable, not failure.** If your researched value
  differs from the code, that's a finding worth investigating — not a
  reason to second-guess yourself and match the code.

---

## Documents to read from the repo

Pull and read from live HEAD before starting:

- The target source file (e.g. `mars_visualization_shells.py`) — to
  see the claims
- `documentation/PREDESIGN_phase2_cross_checked_annotation_R2.md` —
  full context on Phase 2 design
- `documentation/AS_BUILT_phase2_piece1.md` — what the scanner now
  recognizes
- `skills/provenance-discipline/SKILL.md` — v1.4, the competitive
  pattern definition
- `LEDGER_CONSOLIDATED.md` L-156 — Phase 2 build history

Do NOT read the Gemini worksheets (`documentation/worksheet_*.md`)
before producing your own results. Tony will compare afterward.

---

## What success looks like

A completed worksheet per file, with every sourced claim independently
verified against a primary source you found and cited. Tony then lays
it beside Gemini's April worksheet and checks for convergence.

---

*Track 1 prompt prepared August 1, 2026 by Claude Opus 4.6
(orchestration).*
