# Two small fixes — manual edits

## 1. Em-dashes in comet_visualization_shells.py

Three em-dashes (UTF-8 \xe2\x80\x94) to replace with ` -- ` (space,
hyphen, hyphen, space). Use Ctrl+H in VS Code, paste the em-dash
character into the search field (—) and ` -- ` into the replace field.
Replace All should find exactly 3.

The three instances:

1. Display string: "headless ghost comet — dust and ion tails persist"
   -> "headless ghost comet -- dust and ion tails persist"

2. Comment: "# Roche status — disintegration was OUTSIDE"
   -> "# Roche status -- disintegration was OUTSIDE"

3. Display string: "<b>MAPS (C/2026 A1) — Nucleus Disintegrated</b>"
   -> "<b>MAPS (C/2026 A1) -- Nucleus Disintegrated</b>"

## 2. SHA stamp in provenance-discipline SKILL.md

Line 9 currently reads:
  Skill version: 1.3 | Cut from palomas_orrery @ <SHA after push> | July 31, 2026

Replace `<SHA after push>` with `4b6b5c12` (the SHA when v1.3 was first
pushed). The line becomes:
  Skill version: 1.3 | Cut from palomas_orrery @ 4b6b5c12 | July 31, 2026
