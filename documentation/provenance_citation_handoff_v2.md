# Provenance Audit -- Citation Session Handoff v2

## Paloma's Orrery | Tony + Claude | April 18, 2026

---

## What This Session Did

Completed Stage 1 of the provenance audit: all shell files and
supporting modules. Worked through the provenance scanner's Tier 1
findings file by file, alphabetically. For each file:

1. Claude pulled the flagged lines and built a fact-check worksheet
2. Tony gave the worksheet to Gemini for verification
3. Gemini returned corrections and source citations
4. Claude made mechanical edits: inserted `# Source:` comments,
   fixed factual errors, updated module docstrings

---

## Files Completed -- Stage 1 (18 files, ~231 Tier 1 findings)

| File | Findings | Corrections | Key corrections |
|------|----------|-------------|-----------------|
| asteroid_belt_visualization_shells.py | 8 | 3 | Agamemnon/Patroclus camp swap, Hilda triangle, member count |
| comet_visualization_shells.py | 18 | 1 | Hyakutake ion tail comparison |
| earth_visualization_shells.py | 25 | 4 | Stratopause/tropopause swap, LEO count, debris count, "around a" typo |
| eris_visualization_shells.py | 4 | 2 | Hill sphere perihelion note, New Horizons attribution |
| jupiter_visualization_shells.py | 18 | 2 | Hill sphere 530->740 R_J, "around a" typo |
| mars_visualization_shells.py | 5 | 0 | Citations only |
| mercury_visualization_shells.py | 8 | 1 | Sodium tail 2.4->24 Mkm |
| moon_visualization_shells.py | 5 | 0 | Citations only |
| neptune_visualization_shells.py | 26 | 1 | Ring count 13->5 named rings |
| planet9_visualization_shells.py | 4 | 2 | Eris typo in formula, semi-major axis note |
| pluto_visualization_shells.py | 11 | 0 | Citations only |
| saturn_visualization_shells.py | 9 | 1 | "around a" typo |
| sgr_a_star_data.py | 4 | 0 | Citations only |
| solar_visualization_shells.py | 41 | 2 | Hills Cloud/Jupiter-family, Heliopause 123->122 AU |
| spacecraft_encounters.py | 4 | 0 | Citations only |
| star_notes.py | 7 | 4 | Regulus luminosity/mass, AD Leo rotation, Proxima period |
| uranus_visualization_shells.py | 23 | 2 | Eta Ring/Mab association, "around a" typo |
| venus_visualization_shells.py | 6 | 1 | Core radius 3000->3200 km |
| **Total** | **231** | **26** | |

### "Around a where" typo -- fixed in 5 files
Earth, Jupiter, Eris, Saturn, Uranus all had the same "around a where"
copy-paste error in their Hill sphere descriptions. All fixed to
"around a body where." Check remaining files if any Hill sphere
descriptions were not in the audit list.

---

## File Remaining -- Stage 2 (HIGH PRIORITY)

### info_dictionary.py (54 Tier 1 findings)

**What it is:** 2,141-line file containing:
- `note_text`: GUI welcome/about text (not audited -- editorial, not factual)
- `object_type_mapping`: SIMBAD type codes to readable descriptions
- `class_mapping`: Luminosity class Roman numerals to descriptions
- `INFO`: Large dictionary of object descriptions shown in GUI info
  panel and hover text -- this is where the 54 Tier 1 findings live

**Why it's high priority:** INFO strings appear in the GUI info panel
for every object the user clicks. Wrong facts here are seen by every
user on every interaction.

**File structure:**
- Lines 1-93: `note_text` (editorial, skip)
- Lines 96-~400: `object_type_mapping` and `class_mapping` (mostly labels, low risk)
- Lines ~400-2141: `INFO` dictionary -- this is where the 54 findings are

**Recommended approach for next session:**
The 54 findings span a large file. Rather than pulling every line
individually, group by object category for the Gemini worksheet:

1. **Stars** (Sun, nearby stars, variable stars, stellar types)
2. **Solar system bodies** (planets, dwarf planets, asteroids, comets)
3. **Deep sky / galactic** (nebulae, galaxies, clusters)
4. **Spacecraft** (if any INFO strings cover mission facts)

Each group can be one Gemini exchange. Expect 3-4 exchanges total.

**What Claude should do at session start:**
1. View lines ~400 to end to map the INFO dictionary structure
2. Identify which keys have the 54 flagged claims
3. Build grouped worksheets (stars / solar system / deep sky)
4. Run through the standard workflow: worksheet -> Gemini -> edits

---

## Files Remaining -- Stage 2/3 (LOW PRIORITY)

These were flagged by the scanner but are lower priority than
info_dictionary.py. Address after the info dictionary session.

| File | Findings | Notes |
|------|----------|-------|
| star_notes.py | Additional stars | 7 completed this session (Regulus, Vega, Aldebaran, etc.). Remaining flagged stars not yet counted -- likely 20-40 more entries throughout the 1,260-line file |
| sgr_a_star_data.py | 2 remaining | After SPEED_OF_LIGHT fix and 4 display strings audited this session, 2 low-priority findings remain |

---

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

---

## Key Patterns Established (carry forward)

- One `# Source:` block covers all claims in the info string below it
- Credit line format: "April 2026: provenance audit source citations
  added, Gemini fact-check applied. [specific corrections if any].
  Provenance audit identified by Anthropic's Claude Opus 4.7."
- Hill sphere "around a where" typo: fixed in Earth, Jupiter, Eris,
  Saturn, Uranus. Check any remaining Hill sphere descriptions.
- All files have CRLF line endings; str_replace handles them fine
- Bottom-up editing: highest line numbers first
- Syntax check (python3 -m py_compile) before every delivery

## What Claude Cannot Do

Add citations from training data. The worksheet -> Gemini -> Claude
pipeline exists because Claude inventing sources defeats the scanner's
purpose. Claude preps and inserts; Gemini (or Tony) verifies.

---

## Audit Statistics

- Total Stage 1 findings processed: 231
- Total corrections made: 26 (11% error rate)
- Most corrected file: star_notes.py (4 corrections -- stellar
  parameters drift as catalog reductions improve)
- Most common error type: "around a where" Hill sphere typo (5 files)
- Most significant science correction: Neptune ring count (13->5
  named rings), Hills Cloud / Jupiter-family comets (wrong origin),
  Regulus luminosity (140->288 L_sun)
- Files with zero corrections: mars, moon, pluto, sgr_a (4 files)
- Scanner re-run after info_dictionary complete should show Tier 1
  drop to near zero for all audited files
