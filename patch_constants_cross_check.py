"""
Transactional patch: constants_new.py cross-check fixes (L-156 Phase 2)
CONSOLIDATED -- includes all accuracy, citation, and annotation fixes.

Run: python patch_constants_cross_check.py
From: the palomas_orrery repo root (same folder as constants_new.py)

Built on 225071f6184c5fe150a8cdb258a03dbe10ae2718
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

Checkers: Claude Opus 5, GPT-5.6 Thinking, Gemini (book citations)
"""

import sys

TARGET = 'constants_new.py'

edits = [

    # ============================================================
    # BOTTOM-UP from highest line numbers
    # ============================================================

    # --- Arrokoth (line 296) ---
    (
        "Arrokoth: 9.95 -> 9.1, Keane et al. 2022 shape model",
        b"ARROKOTH_RADIUS_KM = 9.95\n"
        b"# Source: Volumetric mean (~35x20x14 km bilobed shape)\n"
        b"# Corrected 2026-04-15 per Gemini review (was 0.0088 = 8.8 meters!)",
        b"ARROKOTH_RADIUS_KM = 9.1\n"
        b"# Source: Keane et al. 2022, JGR Planets (New Horizons shape model)\n"
        b"#         Volume 3166 km^3 -> equivalent sphere radius 9.1 km\n"
        b"#         Overall dims 35.95 x 19.90 x 9.75 km (bilobed contact binary)\n"
        b"# Corrected 2026-04-15 per Gemini review (was 0.0088 = 8.8 meters!)\n"
        b"# Corrected 2026-08-02: 9.95 -> 9.1 per Keane shape model (prior dims were wrong)\n"
        b"# Cross-checked: Keane et al. 2022 via Claude 2026-08-02 (worksheet_claude_constants_new.md)\n"
        b"# Cross-checked: Keane et al. 2022 via GPT 2026-08-02 (constants_new_citation_verification_gpt.md)",
    ),

    # --- Haumea (line 290) ---
    (
        "Haumea: 816 -> 715, JPL SSD published mean",
        b"HAUMEA_RADIUS_KM = 816\n"
        b"# Source: Volumetric mean (highly ellipsoidal: 1050x840x537 km)",
        b"HAUMEA_RADIUS_KM = 715\n"
        b"# Source: JPL SSD mean radius (Lockwood et al. 2014)\n"
        b"#         Highly ellipsoidal: 1050x840x537 km -> geometric mean 779.5 km\n"
        b"#         JPL SSD publishes 715; equatorial 870\n"
        b"# Corrected 2026-08-02: 816 -> 715 per JPL SSD (prior value matched neither axes nor database)\n"
        b"# Cross-checked: JPL SSD via Claude 2026-08-02 (worksheet_claude_constants_new.md)\n"
        b"# Cross-checked: JPL SSD via GPT 2026-08-02 (constants_new_citation_verification_gpt.md)",
    ),

    # --- Bennu (line 284) ---
    (
        "Bennu: 0.262 -> 0.246, Nolan et al. 2013",
        b"BENNU_RADIUS_KM = 0.262\n"
        b"# Source: Volumetric mean (top-shape asteroid, OSIRIS-REx)",
        b"BENNU_RADIUS_KM = 0.246\n"
        b"# Source: Nolan et al. 2013 (radar shape model), mean diameter 492 +/- 20 m\n"
        b"#         Confirmed by OSIRIS-REx OLA: mean radius 246 +/- 10 m, V = 0.062 km^3\n"
        b"# Corrected 2026-08-02: 0.262 -> 0.246 (prior value matched no published source)\n"
        b"# Cross-checked: Nolan et al. via Claude 2026-08-02 (worksheet_claude_constants_new.md)\n"
        b"# Cross-checked: OSIRIS-REx via GPT 2026-08-02 (constants_new_citation_verification_gpt.md)",
    ),

    # --- Neptune source (line 278) ---
    (
        "Neptune: IAU 2015 -> Archinal et al. 2018",
        b"NEPTUNE_RADIUS_KM = 24764\n"
        b"# Source: IAU 2015 nominal equatorial (volumetric = 24622)",
        b"NEPTUNE_RADIUS_KM = 24764\n"
        b"# Source: Archinal et al. 2018, Celest. Mech. Dyn. Astr. 130:22 (equatorial; vol = 24622)\n"
        b"# Cross-checked: JPL SSD via Claude 2026-08-02 (worksheet_claude_constants_new.md)\n"
        b"# Cross-checked: JPL SSD via GPT 2026-08-02 (constants_new_citation_verification_gpt.md)",
    ),

    # --- Uranus source (line 275) ---
    (
        "Uranus: IAU 2015 -> Archinal et al. 2018",
        b"URANUS_RADIUS_KM = 25559\n"
        b"# Source: IAU 2015 nominal equatorial (volumetric = 25362)",
        b"URANUS_RADIUS_KM = 25559\n"
        b"# Source: Archinal et al. 2018, Celest. Mech. Dyn. Astr. 130:22 (equatorial; vol = 25362)\n"
        b"# Cross-checked: JPL SSD via Claude 2026-08-02 (worksheet_claude_constants_new.md)\n"
        b"# Cross-checked: JPL SSD via GPT 2026-08-02 (constants_new_citation_verification_gpt.md)",
    ),

    # --- Saturn source (line 272) ---
    (
        "Saturn: IAU 2015 -> Archinal et al. 2018",
        b"SATURN_RADIUS_KM = 60268\n"
        b"# Source: IAU 2015 nominal equatorial (volumetric = 58232)",
        b"SATURN_RADIUS_KM = 60268\n"
        b"# Source: Archinal et al. 2018, Celest. Mech. Dyn. Astr. 130:22 (equatorial; vol = 58232)\n"
        b"# Cross-checked: JPL SSD via Claude 2026-08-02 (worksheet_claude_constants_new.md)\n"
        b"# Cross-checked: JPL SSD via GPT 2026-08-02 (constants_new_citation_verification_gpt.md)",
    ),

    # --- Mars source (line 266) ---
    (
        "Mars: IAU 2015 -> Archinal et al. 2018",
        b"MARS_RADIUS_KM = 3396.2\n"
        b"# Source: IAU 2015 nominal equatorial (volumetric = 3389.5)",
        b"MARS_RADIUS_KM = 3396.2\n"
        b"# Source: Archinal et al. 2018, Celest. Mech. Dyn. Astr. 130:22 (equatorial; vol = 3389.5)\n"
        b"# Cross-checked: JPL SSD via Claude 2026-08-02 (worksheet_claude_constants_new.md)\n"
        b"# Cross-checked: JPL SSD via GPT 2026-08-02 (constants_new_citation_verification_gpt.md)",
    ),

    # --- Moon Cross-checked (line 263) ---
    (
        "Moon: add Cross-checked (three-way verified)",
        b"MOON_RADIUS_KM = 1737.4\n"
        b"# Source: NASA Fact Sheet (volumetric mean; oblateness ~0.0012)",
        b"MOON_RADIUS_KM = 1737.4\n"
        b"# Source: NASA NSSDCA Fact Sheet (volumetric mean; oblateness ~0.0012)\n"
        b"#         Also IAU/LRO reference radius (Archinal et al. 2011)\n"
        b"# Cross-checked: NASA NSSDCA via Claude 2026-08-02 (worksheet_claude_constants_remaining.md)\n"
        b"# Cross-checked: JPL SSD via GPT 2026-08-02 (constants_remaining_independent_verification_gpt.md)\n"
        b"# Cross-checked: NASA NSSDCA via Gemini 2026-08-02 (Gemini worksheet)",
    ),

    # --- Group G header: B3 scope fix (line 237) ---
    (
        "Group G header: separate B3 from Archinal",
        b"#   IAU 2015 Resolution B3 (Prsa et al. 2016, AJ 152:41) for Sun,\n"
        b"#     Earth, Mars, Jupiter, Saturn, Uranus, Neptune nominal values.",
        b"#   IAU 2015 Resolution B3 (Prsa et al. 2016, AJ 152:41) for Sun,\n"
        b"#     Earth, Jupiter nominal values.\n"
        b"#   Archinal et al. 2018 (Celest. Mech. Dyn. Astr. 130:22) for Mars,\n"
        b"#     Saturn, Uranus, Neptune equatorial radii (IAU WGCCRE 2015 report).",
    ),

    # --- Group G Verified -> Cross-checked (line 244) ---
    (
        "Group G: Verified -> Cross-checked",
        b"# Verified: 2026-04-16 (equatorial convention adopted per downstream\n"
        b"#   usage analysis; prior volumetric values caused ~2.3% position error\n"
        b"#   for Jupiter-scaled shells like Io torus).",
        b"# Note: equatorial convention adopted 2026-04-16 per downstream usage\n"
        b"#   analysis; prior volumetric values caused ~2.3% position error for\n"
        b"#   Jupiter-scaled shells like Io torus.\n"
        b"# Cross-checked: IAU B3 / Archinal / JPL SSD via Claude 2026-08-02 (worksheet_claude_constants_new.md)\n"
        b"# Cross-checked: IAU B3 / Archinal / JPL SSD via GPT 2026-08-02 (constants_new_citation_verification_gpt.md)",
    ),

    # --- Parker: Verified -> Cross-checked + heliocentric (line 216) ---
    (
        "Parker: Verified -> Cross-checked, heliocentric note",
        b"# Verified: 2026-04-15\n"
        b"# Corrected: 2026-04-15 per Gemini review -- 8.86 was surface altitude,\n"
        b"#   9.86 is distance from Sun center (consistent with other shell radii).\n"
        b"#   Perihelion number corrected from 21 to 22.",
        b"# Corrected: 2026-04-15 per Gemini review -- 8.86 was surface altitude,\n"
        b"#   9.86 is distance from Sun center (consistent with other shell radii).\n"
        b"#   Perihelion number corrected from 21 to 22.\n"
        b"# HELIOCENTRIC: 9.86 from Sun center. NASA press reports ~3.83 Mkm above\n"
        b"#   the surface = 8.86 R_sun altitude. Same orbit, different reference.\n"
        b"# Cross-checked: JHUAPL/Riley et al. via Claude 2026-08-02 (worksheet_claude_constants_new.md)\n"
        b"# Cross-checked: NASA PSP mission data via GPT 2026-08-02 (constants_new_citation_verification_gpt.md)",
    ),

    # --- Gravitational influence: 126000 -> 150000 (line 207) ---
    (
        "Gravitational influence: 126000 -> 150000, add sourcing",
        b"GRAVITATIONAL_INFLUENCE_AU = 126000\n"
        b"# Source: Approximate Hill sphere radius of Sun in Milky Way\n"
        b"# Note: ~2 light-years; depends on local stellar density\n"
        b"# Verified: 2026-04-15",
        b"GRAVITATIONAL_INFLUENCE_AU = 150000\n"
        b"# Source: Approximate Hill sphere of Sun in Milky Way (model-dependent)\n"
        b"#         Estimates range 100,000-200,000 AU in the literature;\n"
        b"#         depends on assumed enclosed galactic mass and Sun's orbital distance.\n"
        b"#         ~2.4 light-years. Visualization boundary, not a measured value.\n"
        b"# Corrected 2026-08-02: 126000 -> 150000 (prior value unsourced;\n"
        b"#   150000 AU is a round midpoint of the published range)",
    ),

    # --- Heliopause: 26449 -> 26148 (line 186) ---
    (
        "Heliopause: 26449 -> 26148, fix arithmetic",
        b"HELIOPAUSE_RADII = 26449\n"
        b"# Note: This is in solar radii, not AU. ~123 AU = 123 * 149597870.7 / 695700 = 26449 R_sun\n"
        b"# Source: Voyager 1 crossed heliopause at ~121.6 AU (Aug 2012)\n"
        b"# Ref: Gurnett et al. (2013), Science 341:1489\n"
        b"# Verified: 2026-04-15\n"
        b"# Gemini confirmed: conversion math is correct (123 AU -> 26449 R_sun)\n"
        b"# TODO: Consider renaming to HELIOPAUSE_AU = 123 for clarity",
        b"HELIOPAUSE_RADII = 26148\n"
        b"# Note: This is in solar radii, not AU. 121.6 AU * 149597870.7 / 695700 = 26148 R_sun\n"
        b"# Source: Voyager 1 crossed heliopause at ~121.6 AU (Aug 2012)\n"
        b"# Ref: Gurnett et al. (2013), Science 341:1489\n"
        b"# Corrected 2026-08-02: 26449 -> 26148 (prior comment used 123 AU;\n"
        b"#   Gurnett source says 121.6 AU; both checkers independently found the error)\n"
        b"# Cross-checked: Gurnett et al. via Claude 2026-08-02 (worksheet_claude_constants_new.md)\n"
        b"# Cross-checked: Gurnett et al. via GPT 2026-08-02 (constants_new_citation_verification_gpt.md)",
    ),

    # --- Termination shock: Verified -> Cross-checked (line 184) ---
    (
        "Termination shock: Verified -> Cross-checked",
        b"# Also: Voyager 2 crossed at 84 AU (Aug 2007) -- asymmetric\n"
        b"# Verified: 2026-04-15",
        b"# Also: Voyager 2 crossed at 84 AU (Aug 2007) -- asymmetric\n"
        b"# Cross-checked: Stone et al. via Claude 2026-08-02 (worksheet_claude_constants_new.md)\n"
        b"# Cross-checked: Stone et al. via GPT 2026-08-02 (constants_new_citation_verification_gpt.md)",
    ),

    # --- Alfven: Verified -> Cross-checked + heliocentric (line 172) ---
    (
        "Alfven: Verified -> Cross-checked, heliocentric note",
        b"# Verified: 2026-04-15\n"
        b"# Note: Varies 10-20 R_sun with solar activity; 18.8 is the measured crossing",
        b"# Note: Varies 10-20 R_sun with solar activity; 18.8 is the measured crossing\n"
        b"# HELIOCENTRIC: from Sun center. NASA/APL press releases word it as altitude\n"
        b"#   above the surface, but Kasper's paper says 18.4-19.7 R_sun from center.\n"
        b"# Cross-checked: Kasper et al. via Claude 2026-08-02 (worksheet_claude_constants_new.md)\n"
        b"# Cross-checked: Kasper et al. via GPT 2026-08-02 (constants_new_citation_verification_gpt.md)",
    ),

    # --- Roche limit: Verified -> Cross-checked (line 164) ---
    (
        "Roche limit: Verified -> Cross-checked",
        b"# Ref: Murray & Dermott, \"Solar System Dynamics\" (1999), Sec. 4.6\n"
        b"# Verified: 2026-04-15",
        b"# Ref: Murray & Dermott, \"Solar System Dynamics\" (1999), Sec. 4.6\n"
        b"# Cross-checked: formula verified via Claude 2026-08-02 (worksheet_claude_constants_new.md)\n"
        b"# Cross-checked: formula verified via GPT 2026-08-02 (constants_new_citation_verification_gpt.md)",
    ),

    # --- Streamer belt: fix DeForest year + Verified -> vis note + Gemini (line 154-157) ---
    (
        "Streamer belt: DeForest 2018->2014, Verified -> vis note + Gemini confirmed",
        b"STREAMER_BELT_RADII = 6.0\n"
        b"# Source: Eclipse observations; helmet streamers extend 4-6 R_sun\n"
        b"# Ref: Golub & Pasachoff (2010); DeForest et al. (2018)\n"
        b"# Verified: 2026-04-15",
        b"STREAMER_BELT_RADII = 6.0\n"
        b"# Source: Eclipse observations; helmet streamers extend 4-6 R_sun\n"
        b"# Ref: Golub & Pasachoff (2010); DeForest, Howard & McComas (2014), ApJ 787:124\n"
        b"# Note: Visualization cutoff at upper end of 4-6 R_sun observed range;\n"
        b"#   streamer-belt structure remains observable beyond 6 R_sun.\n"
        b"# Cross-checked: Golub & Pasachoff via Gemini 2026-08-02 (Gemini worksheet)\n"
        b"# Cross-checked: DeForest et al. via GPT 2026-08-02 (constants_remaining_independent_verification_gpt.md)",
    ),

    # --- Outer corona: Verified -> vis note (line 151) ---
    (
        "Outer corona: Verified -> visualization note",
        b"# Ref: Mann et al. (2004), A&A 414:1127\n"
        b"# Verified: 2026-04-15",
        b"# Ref: Mann et al. (2004), A&A 414:1127\n"
        b"# Note: Visualization boundary for F-corona envelope; not a sharp physical edge",
    ),

    # --- Inner corona: Verified -> vis note + Gemini (line 146) ---
    (
        "Inner corona: Verified -> vis note + Gemini confirmed",
        b"# Note: Inner (K-)corona extends to 2-3 R_sun\n"
        b"# Verified: 2026-04-15",
        b"# Note: Visualization boundary for inner (K-)corona; physical extent 2-3 R_sun\n"
        b"# Cross-checked: Golub & Pasachoff via Gemini 2026-08-02 (Gemini worksheet)",
    ),

    # --- Chromosphere: 1.5 -> 1.1, relabel (line 138) ---
    (
        "Chromosphere: 1.5 -> 1.1, relabel as visualization shell",
        b"CHROMOSPHERE_RADII = 1.5\n"
        b"# Source: Carroll & Ostlie (2017), Ch. 11\n"
        b"# Note: Chromosphere extends from photosphere (~1.0) to ~1.5 R_sun\n"
        b"# Verified: 2026-04-15",
        b"CHROMOSPHERE_RADII = 1.1\n"
        b"# Visualization shell radius (physical chromosphere extends ~2000 km above\n"
        b"# photosphere = ~1.003 R_sun; drawn at 1.1 for visibility at orrery scale)\n"
        b"# Corrected 2026-08-02: 1.5 -> 1.1 (1.5 overstated the physical extent;\n"
        b"#   Carroll & Ostlie Ch. 11 confirms ~2000 km, not 1.5 R_sun)\n"
        b"# Cross-checked: Carroll & Ostlie via Gemini 2026-08-02 (Gemini worksheet)\n"
        b"# Cross-checked: NASA chromosphere data via GPT 2026-08-02 (constants_remaining_independent_verification_gpt.md)",
    ),

    # --- Radiative zone: fix citation (line 133-135) ---
    (
        "Radiative zone: cite Christensen-Dalsgaard, note rounding",
        b"RADIATIVE_ZONE_AU = 0.7 * SOLAR_RADIUS_AU\n"
        b"# Derived: radiative zone extends to ~0.7 solar radii\n"
        b"# Source: Standard solar model",
        b"RADIATIVE_ZONE_AU = 0.7 * SOLAR_RADIUS_AU\n"
        b"# Visualization boundary; rounds the helioseismic tachocline at ~0.713 R_sun\n"
        b"# Source: Christensen-Dalsgaard, Gough & Thompson (1991), ApJ 378:413\n"
        b"# Cross-checked: helioseismology literature via GPT 2026-08-02 (constants_remaining_independent_verification_gpt.md)\n"
        b"# Cross-checked: Carroll & Ostlie via Gemini 2026-08-02 (Gemini worksheet)",
    ),

    # --- Core boundary: relabel (line 129-131) ---
    (
        "Core: relabel as visualization boundary, cite Bahcall properly",
        b"CORE_AU = 0.2 * SOLAR_RADIUS_AU\n"
        b"# Derived: core extends to ~0.2 solar radii\n"
        b"# Source: Standard solar model (Bahcall et al.)",
        b"CORE_AU = 0.2 * SOLAR_RADIUS_AU\n"
        b"# Visualization boundary at low end of conventional 0.2-0.25 R_sun core range\n"
        b"# Source: Bahcall, Pinsonneault & Basu (2001), ApJ 555:990 (radial profiles)\n"
        b"# Also: Carroll & Ostlie (2017), Ch. 11 gives 0.2-0.25 R_sun\n"
        b"# Cross-checked: Carroll & Ostlie via Gemini 2026-08-02 (Gemini worksheet)\n"
        b"# Cross-checked: NASA solar structure via GPT 2026-08-02 (constants_remaining_independent_verification_gpt.md)",
    ),

    # --- Section header: Verified -> Cross-checked with Gemini (line 127) ---
    (
        "Solar structure header: Verified -> Cross-checked (Gemini book access)",
        b"# Source: Carroll & Ostlie, \"Introduction to Modern Astrophysics\" (2017)\n"
        b"# Also: https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html\n"
        b"# Verified: 2026-04-15",
        b"# Source: Carroll & Ostlie, \"Introduction to Modern Astrophysics\" (2017)\n"
        b"# Also: https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html\n"
        b"# Cross-checked: Carroll & Ostlie via Gemini 2026-08-02 (Gemini worksheet)\n"
        b"# Cross-checked: NASA Sun Fact Sheet via GPT 2026-08-02 (constants_new_citation_verification_gpt.md)",
    ),

    # --- Speed of light: Verified -> Cross-checked (line 94) ---
    (
        "Speed of light: Verified -> Cross-checked",
        b"# Ref: https://physics.nist.gov/cgi-bin/cuu/Value?c\n"
        b"# Verified: 2026-04-15",
        b"# Ref: https://physics.nist.gov/cgi-bin/cuu/Value?c\n"
        b"# Cross-checked: NIST/SI via Claude 2026-08-02 (worksheet_claude_constants_new.md)\n"
        b"# Cross-checked: NIST/SI via GPT 2026-08-02 (constants_new_citation_verification_gpt.md)",
    ),

    # --- Jupiter polar: Verified -> Cross-checked (line 89) ---
    (
        "Jupiter polar: Verified -> Cross-checked",
        b"# Source: IAU 2015 Resolution B3 -- nominal jovian polar radius\n"
        b"# Ref: Prsa et al. 2016, AJ 152:41 (arXiv:1605.09788)\n"
        b"# Verified: 2026-04-15",
        b"# Source: IAU 2015 Resolution B3 -- nominal jovian polar radius\n"
        b"# Ref: Prsa et al. 2016, AJ 152:41 (arXiv:1605.09788)\n"
        b"# Cross-checked: IAU B3 via Claude 2026-08-02 (worksheet_claude_constants_new.md)\n"
        b"# Cross-checked: IAU B3 via GPT 2026-08-02 (constants_new_citation_verification_gpt.md)",
    ),

    # --- Jupiter equatorial: Verified -> Cross-checked (line 84) ---
    (
        "Jupiter equatorial: Verified -> Cross-checked",
        b"# Source: IAU 2015 Resolution B3 -- nominal jovian equatorial radius\n"
        b"# Ref: Prsa et al. 2016, AJ 152:41 (arXiv:1605.09788)\n"
        b"# Verified: 2026-04-15",
        b"# Source: IAU 2015 Resolution B3 -- nominal jovian equatorial radius\n"
        b"# Ref: Prsa et al. 2016, AJ 152:41 (arXiv:1605.09788)\n"
        b"# Cross-checked: IAU B3 via Claude 2026-08-02 (worksheet_claude_constants_new.md)\n"
        b"# Cross-checked: IAU B3 via GPT 2026-08-02 (constants_new_citation_verification_gpt.md)",
    ),

    # --- Earth polar: Verified -> Cross-checked + IERS (line 79) ---
    (
        "Earth polar: Verified -> Cross-checked, note IERS",
        b"# Source: IAU 2015 Resolution B3 -- nominal terrestrial polar radius\n"
        b"# Ref: Prsa et al. 2016, AJ 152:41 (arXiv:1605.09788)\n"
        b"# Verified: 2026-04-15",
        b"# Source: IERS Conventions (Petit & Luzum 2010); IAU B3 rounds to 6356.8 km\n"
        b"# Ref: Prsa et al. 2016, AJ 152:41 (arXiv:1605.09788)\n"
        b"# Cross-checked: IAU B3 / IERS via Claude 2026-08-02 (worksheet_claude_constants_new.md)\n"
        b"# Cross-checked: IAU B3 / IERS via GPT 2026-08-02 (constants_new_citation_verification_gpt.md)",
    ),

    # --- Earth equatorial: Verified -> Cross-checked + IERS (line 74) ---
    (
        "Earth equatorial: Verified -> Cross-checked, note IERS",
        b"# Also: https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html\n"
        b"# Verified: 2026-04-15",
        b"# Also: https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html\n"
        b"# Note: B3 rounds to 6378.1 km; full precision from IERS Conventions\n"
        b"# Cross-checked: IAU B3 / IERS via Claude 2026-08-02 (worksheet_claude_constants_new.md)\n"
        b"# Cross-checked: IAU B3 / IERS via GPT 2026-08-02 (constants_new_citation_verification_gpt.md)",
    ),

    # --- Sun radius: Verified -> Cross-checked (line 65) ---
    (
        "Sun radius: Verified -> Cross-checked",
        b"# Source: IAU 2015 Resolution B3 -- nominal solar radius\n"
        b"# Ref: Prsa et al. 2016, AJ 152:41 (arXiv:1605.09788)\n"
        b"# Also: https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html\n"
        b"# Verified: 2026-04-15",
        b"# Source: IAU 2015 Resolution B3 -- nominal solar radius\n"
        b"# Ref: Prsa et al. 2016, AJ 152:41 (arXiv:1605.09788)\n"
        b"# Also: https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html\n"
        b"# Cross-checked: IAU B3 via Claude 2026-08-02 (worksheet_claude_constants_new.md)\n"
        b"# Cross-checked: IAU B3 via GPT 2026-08-02 (constants_new_citation_verification_gpt.md)",
    ),

    # --- KM_PER_AU: Verified -> Cross-checked (line 58) ---
    (
        "KM_PER_AU: Verified -> Cross-checked",
        b"# Also: https://nssdc.gsfc.nasa.gov/planetary/factsheet/fact_notes.html\n"
        b"# Verified: 2026-04-15",
        b"# Also: https://nssdc.gsfc.nasa.gov/planetary/factsheet/fact_notes.html\n"
        b"# Cross-checked: IAU B2 via Claude 2026-08-02 (worksheet_claude_constants_new.md)\n"
        b"# Cross-checked: IAU B2 via GPT 2026-08-02 (constants_new_citation_verification_gpt.md)",
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
