# Provenance Audit -- Citation Session Handoff

## Paloma's Orrery | Tony + Claude | April 18, 2026

---

## What This Session Did

Worked through the provenance scanner's Tier 1 findings file by
file, alphabetically. For each shell file:

1. Claude pulled the flagged lines and built a fact-check worksheet
2. Tony gave the worksheet to Gemini for verification
3. Gemini returned corrections and source citations
4. Claude made mechanical edits: inserted `# Source:` comments,
   fixed factual errors, updated module docstrings

## Files Completed (7 shell files, ~86 Tier 1 findings)

| File | Findings | Corrections |
|------|----------|-------------|
| asteroid_belt_visualization_shells.py | 8 | Agamemnon/Patroclus camp swap, Hilda triangle mechanism, member count 4000->5000+ |
| comet_visualization_shells.py | 18 | Hyakutake ion tail comparison (580 Mkm < Sun-Jupiter 778 Mkm) |
| earth_visualization_shells.py | 25 | Stratopause/tropopause temperature label swap, LEO satellite count 8K->11K, debris 20K->35K, Hill sphere "around a" typo |
| eris_visualization_shells.py | 4 | Hill sphere perihelion vs semi-major axis noted, "New Horizons" attribution corrected (was Pluto not Eris) |
| jupiter_visualization_shells.py | 18 | Hill sphere inconsistency resolved (info said 530 R_J/0.25 AU, correct is 740 R_J/0.35 AU), "around a" typo |
| mars_visualization_shells.py | 5 | No corrections needed, citations only |
| mercury_visualization_shells.py | 8 | Sodium tail decimal error (2.4 Mkm -> 24 Mkm) |

Also completed (earlier in session):
- `sgr_a_star_data.py`: consolidated `SPEED_OF_LIGHT_KM_S` duplicate
  (import from constants_new instead of local definition)

## Files Remaining (alphabetical, Tier 1 counts from audit)

### Shell files (Stage 1 continued):
- moon_visualization_shells.py (5)
- neptune_visualization_shells.py (26)
- planet9_visualization_shells.py (4)
- pluto_visualization_shells.py (11)
- saturn_visualization_shells.py (9)
- solar_visualization_shells.py (41)
- uranus_visualization_shells.py (23)
- venus_visualization_shells.py (6)

### Other (Stages 2-3):
- info_dictionary.py (54) -- own session, prose fact-check
- star_notes.py -- low priority
- spacecraft_encounters.py -- low priority
- sgr_a_star_data.py -- low priority (2 remaining after SPEED_OF_LIGHT fix)

## Workflow (repeat for each file)

1. Claude pulls flagged lines from PROVENANCE_AUDIT.md, groups by
   likely source, builds a markdown worksheet with specific claims
2. Tony gives worksheet to Gemini: "verify each claim, provide source"
3. Tony pastes Gemini's response back to Claude
4. Claude makes mechanical edits bottom-up:
   - Insert `# Source:` comments above info strings
   - Fix any factual errors Gemini identified
   - Update module docstring per v3.20 standard with credits:
     `Anthropic's Claude Sonnet 4.6` (edits) and
     `Anthropic's Claude Opus 4.7` (audit identification)
5. Claude compiles, copies to outputs

## Key Patterns Established

- One `# Source:` block covers all claims in the info string below it
- Credit line format: "April 17, 2026: provenance audit source
  citations added, Gemini fact-check applied. [specific corrections].
  Provenance audit identified by Anthropic's Claude Opus 4.7"
- Hill sphere "around a where" typo exists in multiple files --
  fixed in Earth, Jupiter, Eris so far; check remaining planets
- All files have CRLF line endings; str_replace handles them fine
- Scanner re-run after all files complete should show Tier 1 drop

## What Claude Cannot Do

Add citations from training data. The worksheet -> Gemini -> Claude
pipeline exists because Claude inventing sources defeats the scanner's
purpose. Claude preps and inserts; Gemini (or Tony) verifies.
