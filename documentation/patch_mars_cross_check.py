"""
Transactional patch: mars_visualization_shells.py cross-check fixes (L-156 Phase 2)

Run: python patch_mars_cross_check.py
From: the palomas_orrery repo root (same folder as mars_visualization_shells.py)

Applies all fixes identified by the Claude + GPT cross-check (August 2026):
  1. Bow shock display text: "around 1.5" -> "around 1.6" (3 locations)
  2. Hill sphere radii: 324.5 -> 320 (5 locations)
  3. Hill sphere perihelion: ~0.8 -> ~0.98 Mkm
  4. Hill sphere AU: 0.073 -> 0.007 (factor-of-10 error)
  5. Hill sphere Source: rewrite as derived-value citation
  6. Stratosphere: remove unsourceable claim (2 locations)
  7. Replace 4 old Verified lines with Cross-checked annotations

All-or-nothing: if any anchor is not found exactly once, nothing is written.

Built on 8d7c6074c020123917716b47853880f3a5b492b8
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
"""

import sys

TARGET = 'mars_visualization_shells.py'

# Each edit is (description, old_bytes, new_bytes).
# Order: bottom-up by line number so earlier anchors stay valid.
edits = [

    # --- Edit 1: Line 881 - Hill sphere radius_fraction constant ---
    (
        "Hill sphere radius_fraction 324.5 -> 320 (line 881)",
        b"radius_fraction = 324.5  # Mars's Hill sphere is about 324.5 Mars radii",
        b"radius_fraction = 320  # Mars's Hill sphere is about 320 Mars radii",
    ),

    # --- Edit 2: Line 864 - Hill sphere AU value (factor-of-10 error) ---
    (
        "Hill sphere AU 0.073 -> 0.007 (line 864)",
        b"1.1 million kilometers (about 0.073 astronomical units)",
        b"1.1 million kilometers (about 0.007 AU)",
    ),

    # --- Edit 3: Line 856 - Hill sphere description text (in layer_info, 16-space indent) ---
    (
        "Hill sphere ~324.5 -> ~320 in layer_info description (line 856)",
        b'                "Mars\'s Hill Sphere (extends to ~324.5 Mars radii',
        b'                "Mars\'s Hill Sphere (extends to ~320 Mars radii',
    ),

    # --- Edit 4: Line 851 - Hill sphere radius_fraction in dict ---
    (
        "Hill sphere radius_fraction dict 324.5 -> 320 (line 851)",
        b"'radius_fraction': 324.5,",
        b"'radius_fraction': 320,",
    ),

    # --- Edit 5: Lines 841 - Hill sphere info text (12-space indent) ---
    (
        "Hill sphere ~324.5 -> ~320 in mars_hill_sphere_info (line 841)",
        b'            "Mars\'s Hill Sphere (extends to ~324.5 Mars radii',
        b'            "Mars\'s Hill Sphere (extends to ~320 Mars radii',
    ),

    # --- Edit 6: Lines 835-838 - Hill sphere Source + Verified -> new format ---
    (
        "Hill sphere Source/Verified -> derived citation + Cross-checked (lines 835-838)",
        b"# Source: NASA Solar System Dynamics\n"
        b"#         Hill sphere varies with eccentricity (~0.8 Mkm perihelion to ~1.2 Mkm aphelion);\n"
        b"#         1.1 Mkm / 324.5 R_Mars is the semi-major axis average.\n"
        b"# Verified: April 2026 via Gemini fact-check",
        b"# Source: Derived from NASA NSSDCA Mars Fact Sheet (a, GM_Mars)\n"
        b"#         via standard Hill approximation, Claude Opus 5 2026-08-01\n"
        b"#         Hill sphere varies with eccentricity (~0.98 Mkm perihelion to ~1.19 Mkm aphelion);\n"
        b"#         ~1.08 Mkm / ~320 R_Mars is the semi-major axis average.\n"
        b"# Cross-checked: NASA NSSDCA Mars Fact Sheet via Claude 2026-08-01 (worksheet_claude_mars_visualization.md)\n"
        b"# Cross-checked: JPL SSD astrodynamic parameters via GPT 2026-08-01 (track1_gpt_independent_worksheet_mars_visualization.md)",
    ),

    # --- Edit 7: Line 713 - bow shock hover text 1.5 -> 1.6 ---
    (
        "Bow shock hover text 1.5 -> 1.6 (line 713)",
        b"It's much closer to Mars (around 1.5 Mars radii)<br>",
        b"It's much closer to Mars (around 1.6 Mars radii)<br>",
    ),

    # --- Edit 8: Lines 710-711 - bow shock Source + Verified -> Cross-checked ---
    (
        "Bow shock Source/Verified -> Cross-checked (lines 710-711)",
        b"# Source: NASA MAVEN; NASA Solar System Exploration\n"
        b"    # Verified: April 2026 via Gemini fact-check",
        b"# Source: Vignes et al. 2000, GRL 27 (bow shock 1.64 R_M);\n"
        b"    #         NASA Solar System Exploration (Earth comparison)\n"
        b"    # Cross-checked: Vignes et al. via Claude 2026-08-01 (worksheet_claude_mars_visualization.md)\n"
        b"    # Cross-checked: Vignes et al. via GPT 2026-08-01 (track1_gpt_independent_worksheet_mars_visualization.md)",
    ),

    # --- Edit 9: Line 655 - magnetosphere hover text 1.5 -> 1.6 ---
    (
        "Magnetosphere hover text 1.5 -> 1.6 (line 655)",
        b"but it's much closer to the planet (around 1.5 Mars radii).<br>\"",
        b"but it's much closer to the planet (around 1.6 Mars radii).<br>\"",
    ),

    # --- Edit 10: Line 606 - magnetosphere info text 1.5 -> 1.6 ---
    (
        "Magnetosphere info text 1.5 -> 1.6 (line 606)",
        b"but it's much closer to the planet (around 1.5 Mars radii).<br><br>\"",
        b"but it's much closer to the planet (around 1.6 Mars radii).<br><br>\"",
    ),

    # --- Edit 11: Lines 597-598 - magnetosphere Source + Verified -> Cross-checked ---
    (
        "Magnetosphere Source/Verified -> Cross-checked (lines 597-598)",
        b"# Source: NASA MAVEN Mission; Mars Global Surveyor (crustal magnetic fields)\n"
        b"# Verified: April 2026 via Gemini fact-check",
        b"# Source: NASA MAVEN Mission; Mars Global Surveyor (crustal magnetic fields);\n"
        b"#         Vignes et al. 2000, GRL 27 (MPB 1.29 R_M, bow shock 1.64 R_M)\n"
        b"# Cross-checked: Vignes et al. via Claude 2026-08-01 (worksheet_claude_mars_visualization.md)\n"
        b"# Cross-checked: Vignes et al. via GPT 2026-08-01 (track1_gpt_independent_worksheet_mars_visualization.md)",
    ),

    # --- Edit 12: Lines 545-548 - remove stratosphere (second occurrence, in layer_info) ---
    (
        "Remove stratosphere text from layer_info description (lines 545-548)",
        b"water on the surface. Unlike Earth, Mars lacks a stratosphere. On Earth, the stratosphere is characterized by a <br>\" \n"
        b"            \"temperature inversion due to the absorption of ultraviolet radiation by the ozone layer. Mars has a very thin <br>\" \n"
        b"            \"atmosphere and no significant ozone layer, so this distinct layer doesn't form.\"\n"
        b"        )",
        b"water on the surface.\"\n"
        b"        )",
    ),

    # --- Edit 13: Lines 524-527 - remove stratosphere (first occurrence, in mars_upper_atmosphere_info) ---
    (
        "Remove stratosphere text from mars_upper_atmosphere_info (lines 524-527)",
        b"water on the surface. Unlike Earth, Mars lacks a stratosphere. On Earth, the stratosphere is characterized by a <br>\" \n"
        b"            \"temperature inversion due to the absorption of ultraviolet radiation by the ozone layer. Mars has a very thin <br>\" \n"
        b"            \"atmosphere and no significant ozone layer, so this distinct layer doesn't form.\"\n"
        b")",
        b"water on the surface.\"\n"
        b")",
    ),

    # --- Edit 14: Lines 514-515 - upper atmosphere Source + Verified -> Cross-checked ---
    (
        "Upper atmosphere Source/Verified -> Cross-checked (lines 514-515)",
        b"# Source: NASA MAVEN Mission; NASA Mars Fact Sheet\n"
        b"# Verified: April 2026 via Gemini fact-check",
        b"# Source: NASA MAVEN Mission; NASA Mars Fact Sheet\n"
        b"# Cross-checked: MAVEN data via Claude 2026-08-01 (worksheet_claude_mars_visualization.md)\n"
        b"# Cross-checked: NASA MAVEN via GPT 2026-08-01 (track1_gpt_independent_worksheet_mars_visualization.md)",
    ),
]

# --- Execute transactionally ---
with open(TARGET, 'rb') as f:
    content = f.read()

original_size = len(content)

for desc, old, new in edits:
    n = content.count(old)
    if n != 1:
        print(f"ANCHOR FAIL: expected 1 match, got {n}: {desc}")
        print(f"  anchor (first 80 bytes): {old[:80]!r}")
        sys.exit(1)
    content = content.replace(old, new)
    print(f"ok: {desc}")

with open(TARGET, 'wb') as f:
    f.write(content)

print(f"\npatch applied ({original_size} -> {len(content)} bytes)")
