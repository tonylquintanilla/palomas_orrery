"""patch_L196_13_continuations_stage2.py -- L-195 / L-192. Mark the
remaining citation-leg continuation comments so nothing pre-existing
can trip the loud failure.

RUN COMMAND
-----------
Save this file into the palomas_orrery repo root (the same folder as
shell_configs.py), open it in VS Code, and click Run.

    python patch_L196_13_continuations_stage2.py

WHAT IT DOES
------------
Stage 1 relabeled the 96 wrapped citation lines in the seven files the
request builder reads today. This is stage 2: the same relabeling for
every other file in the repo.

    # Source: Smith et al. (1989, Science);
    #         NASA Planetary Ring Node.

becomes

    # Source: Smith et al. (1989, Science);
    # Source+: NASA Planetary Ring Node.

Text is unchanged. Only the line's leading comment padding becomes a
label naming the leg it continues. Nothing rendered changes.

SCOPE, AND WHY IT IS NOT THE NUMBER THE HANDOFF RECORDS
--------------------------------------------------------
152 lines across 86 runs in 18 files. The handoff of 2026-08-16 records
stage 2 as 235 lines / 117 runs / 23 files.

That figure does not reproduce. The detector used here was validated
against the pre-stage-1 tree and returns stage 1's answer set exactly --
48 runs, 96 lines, the same line numbers, all seven files. Counting
tails under non-citation labels as well (`# Note:`, `# Cross-checked:`)
gives 111 runs / 217 lines / 27 files, which is not the recorded figure
either. The likeliest reading is that 235/117/23 predates Tony's ruling
5 of 2026-08-16, which scoped the work to citation legs only.

So the repo total is 135 citation-leg continuations, not 165: 96 marked
by stage 1, 6 by the chromosphere retirement, 152 here, and one run
deliberately left alone.

THE ONE RUN LEFT ALONE
----------------------
test_citation_inheritance.py:122-123, inside the MULTILINE_CITATION
fixture. That fixture exists to prove the scanner captures a whole
multi-line citation run, and the test asserts on text from its first
and third lines specifically to catch truncation at the top and in the
middle. Marking it would convert the repo's only test of the UNMARKED
padded shape into a test of the marked shape, silently removing that
coverage. It is a fixture, so it will never gain the cross-check
annotations that would put it in the dispatch corpus.

This matters for the loud failure that comes next: scope it to the
claim corpus rather than to every .py file, or that fixture needs an
explicit exemption. Left as Tony's call.

FIXED IN PASSING
----------------
apsidal_markers.py holds four em-dash characters in comments and a
docstring, predating this work. The repo convention is ASCII-only in
code, the file is already fingerprinted here, and replacing an em-dash
with '--' in a comment needs no judgment, so they are fixed in the same
patch and reported.

info_dictionary.py holds ten non-ASCII characters and they are NOT
touched. All ten sit inside string literals that reach the reader:
superscripts in 'g/cm^3' and 'm/s^2', em-dashes in prose, and the
Polish surname Wierzchos with its accented s. Rewriting those changes
what a person reads and, in one case, misspells a name. That is a
content decision, not mechanical compliance, so it goes to Tony rather
than into a sweep.

SAFETY
------
All-or-nothing. Every file is fingerprinted (CRLF-normalized) before
anything is written, and every target line must match its recorded text
exactly. Any mismatch aborts the whole run with nothing written. Edits
apply bottom-up within each file, so no line number drifts. Each file's
own line endings are preserved. The encoding gate hard-fails on
non-ASCII in an inserted line and reports, without failing, any
pre-existing non-ASCII the patch did not reach.

PERMANENT vs DISPOSABLE
-----------------------
This script is disposable and one-shot. What it installs is permanent:
the markers themselves, which the builder's join reads.

Success: one 'ok' line per file, then 'patch applied (N bytes)'.
Failure: a single 'ERROR:' or 'ANCHOR FAIL' line; nothing is written.
"""

import hashlib
import os
import re
import sys


EDITS = {
    'add_docstrings.py': {
        'fp': '0d56d4dc0421e117bb80dde20c399a80',
        'edits': [
            (825,
             "    # as-built for Tony's review.",
             "    # Source+: as-built for Tony's review."),
            (824,
             '    # explicit; NEW = classified this session, listed in the Phase 2',
             '    # Source+: explicit; NEW = classified this session, listed in the Phase 2'),
            (823,
             '    # MODULE_DOMAIN_MAP; HEUR = the _shells suffix heuristic, now made',
             '    # Source+: MODULE_DOMAIN_MAP; HEUR = the _shells suffix heuristic, now made'),
        ],
    },
    'apsidal_markers.py': {
        'fp': 'e7a2147e3f8e64d52e8487cb79ae551d',
        'edits': [
            (1954,
             '                # Horizons velocities are in AU/day \u2014 convert to km/s',
             '                # Horizons velocities are in AU/day -- convert to km/s'),
            (1881,
             "                'rel_x':          relative position x (AU) \u2014 spacecraft minus target,",
             "                'rel_x':          relative position x (AU) -- spacecraft minus target,"),
            (1865,
             '    Dates must be aligned \u2014 same length, same time steps. If not aligned, the function',
             '    Dates must be aligned -- same length, same time steps. If not aligned, the function'),
            (1854,
             '# a physical constant -- see compute_pairwise_encounter() for usage context.',
             '# Source+: a physical constant -- see compute_pairwise_encounter() for usage context.'),
            (1853,
             '# generously at 0.5 AU to capture all close approaches. Engineering choice, not',
             '# Source+: generously at 0.5 AU to capture all close approaches. Engineering choice, not'),
            (1849,
             '# TWO objects that are both plotted \u2014 e.g. New Horizons relative to Pluto',
             '# TWO objects that are both plotted -- e.g. New Horizons relative to Pluto'),
        ],
    },
    'comet_visualization_shells.py': {
        'fp': '7c687594708c104b690fb633a5b2914b',
        'edits': [
            (1532,
             '#         JPL Small-Body Database (orbital elements)',
             '# Source+: JPL Small-Body Database (orbital elements)'),
            (1531,
             '#         Sekanina (1966) (Ikeya-Seki)',
             '# Source+: Sekanina (1966) (Ikeya-Seki)'),
            (1530,
             '#         Sekanina & Farrell (1978) (West fragmentation)',
             '# Source+: Sekanina & Farrell (1978) (West fragmentation)'),
            (1529,
             '#         Jones et al., Nature (2000) / Ulysses spacecraft (Hyakutake ion tail)',
             '# Source+: Jones et al., Nature (2000) / Ulysses spacecraft (Hyakutake ion tail)'),
            (1528,
             '#         ESA Giotto Mission Archive (Halley)',
             '# Source+: ESA Giotto Mission Archive (Halley)'),
            (1353,
             '            #         Loeb & Scarmato 2026 (RNAAS); Jan 22 alignment obs. Man-To Hui (SHAO).',
             '            # Source+: Loeb & Scarmato 2026 (RNAAS); Jan 22 alignment obs. Man-To Hui (SHAO).'),
            (1352,
             '            #         3 mini-jets at 120 deg) via Larson-Sekanina gradient filter --',
             '            # Source+: 3 mini-jets at 120 deg) via Larson-Sekanina gradient filter --'),
            (1351,
             '            #         Jan 7/14/22 2026; four-jet structure (1 sunward anti-tail +',
             '            # Source+: Jan 7/14/22 2026; four-jet structure (1 sunward anti-tail +'),
            (703,
             '    #         Shell values from constants_new.py (verified via test_constants_provenance)',
             '    # Source+: Shell values from constants_new.py (verified via test_constants_provenance)'),
            (521,
             '    #         Shell values from constants_new.py',
             '    # Source+: Shell values from constants_new.py'),
            (520,
             '    #         JWST Early Release Observations (nucleus ~400 m, March 2026)',
             '    # Source+: JWST Early Release Observations (nucleus ~400 m, March 2026)'),
            (249,
             '    #         JPL Horizons (perihelion distance)',
             '    # Source+: JPL Horizons (perihelion distance)'),
            (248,
             '    #         Sky & Telescope March 14, 2026 (coma color)',
             '    # Source+: Sky & Telescope March 14, 2026 (coma color)'),
            (86,
             '#         NASA NEOWISE Mission / IPAC (C/2020 F3)',
             '# Source+: NASA NEOWISE Mission / IPAC (C/2020 F3)'),
            (85,
             '#         NASA JPL Small-Body Database (orbital elements)',
             '# Source+: NASA JPL Small-Body Database (orbital elements)'),
            (84,
             '#         Sekanina (1966) (Ikeya-Seki, Kreutz sungrazer family)',
             '# Source+: Sekanina (1966) (Ikeya-Seki, Kreutz sungrazer family)'),
            (83,
             '#         Sekanina & Farrell (1978) (West fragmentation into 4 pieces)',
             '# Source+: Sekanina & Farrell (1978) (West fragmentation into 4 pieces)'),
            (82,
             '#         Jones et al., Nature (2000) / Ulysses spacecraft (Hyakutake ion tail: 3.8 AU)',
             '# Source+: Jones et al., Nature (2000) / Ulysses spacecraft (Hyakutake ion tail: 3.8 AU)'),
        ],
    },
    'earth_visualization_shells.py': {
        'fp': '18c1169f7baa56f7d251d2b5710d43a0',
        'edits': [
            (944,
             '    #         SpaceX Starlink status; NASA (ISS, Hubble altitudes)',
             '    # Source+: SpaceX Starlink status; NASA (ISS, Hubble altitudes)'),
            (868,
             '#         Satellite/debris counts as of early 2026',
             '# Source+: Satellite/debris counts as of early 2026'),
            (635,
             '#         NASA Van Allen Probes (radiation belts)',
             '# Source+: NASA Van Allen Probes (radiation belts)'),
        ],
    },
    'food_insecurity_generator.py': {
        'fp': 'c92cd561d88de600555879dd5a60bd38',
        'edits': [
            (187,
             '#   Food Insecurity Analysis February 2026-January 2027"; published 3 June 2026).',
             '# Source+: Food Insecurity Analysis February 2026-January 2027"; published 3 June 2026).'),
            (171,
             '#   to intensify in the near and medium term."',
             '# Source+: to intensify in the near and medium term."'),
            (170,
             '#   fertilizer prices. The impacts of the Middle East crisis on Sudan are likely',
             '# Source+: fertilizer prices. The impacts of the Middle East crisis on Sudan are likely'),
            (169,
             '#   ongoing conflict in the Middle East "contributing to higher fuel, food, and',
             '# Source+: ongoing conflict in the Middle East "contributing to higher fuel, food, and'),
            (140,
             '#   (page 6). Wording lifted verbatim; smart quotes/dashes normalized to ASCII.',
             '# Source+: (page 6). Wording lifted verbatim; smart quotes/dashes normalized to ASCII.'),
            (129,
             '#   Phase represents highest severity affecting at least 20% of the population".',
             '# Source+: Phase represents highest severity affecting at least 20% of the population".'),
            (121,
             '#   "nearly 135,000 people are classified in IPC Phase 5 (Catastrophe)".',
             '# Source+: "nearly 135,000 people are classified in IPC Phase 5 (Catastrophe)".'),
            (120,
             '#   current period, including over 5 million people in IPC Phase 4 (Emergency)";',
             '# Source+: current period, including over 5 million people in IPC Phase 4 (Emergency)";'),
            (119,
             '#   "nearly 19.5 million people are classified in IPC Phase 3 or above for the',
             '# Source+: "nearly 19.5 million people are classified in IPC Phase 3 or above for the'),
            (118,
             '#   (Feb-May 2026): "covering the total population of Sudan (47.5 million)";',
             '# Source+: (Feb-May 2026): "covering the total population of Sudan (47.5 million)";'),
            (81,
             '#   inadequate evidence" (grey) are distinct legend categories, not a phase.',
             '# Source+: inadequate evidence" (grey) are distinct legend categories, not a phase.'),
            (72,
             '#   legend swatches, sampled at 200 dpi (anti-alias +/-2; see build handoff).',
             '# Source+: legend swatches, sampled at 200 dpi (anti-alias +/-2; see build handoff).'),
            (71,
             '#   page 7 "Key for the Map / IPC Acute Food Insecurity Phase Classification"',
             '# Source+: page 7 "Key for the Map / IPC Acute Food Insecurity Phase Classification"'),
        ],
    },
    'idealized_orbits.py': {
        'fp': '22f758e85b0bb5026f4c0b907e3aa077',
        'edits': [
            (4666,
             '    # = 384,400 km x (0.01230 / 1.01230) ~ 4,672 km ~ 0.0000312 AU',
             '    # Calculation+: = 384,400 km x (0.01230 / 1.01230) ~ 4,672 km ~ 0.0000312 AU'),
            (2790,
             '    # = 9,000 km x (0.16 / 1.16) ~ 1,241 km ~ 0.0000083 AU',
             '    # Calculation+: = 9,000 km x (0.16 / 1.16) ~ 1,241 km ~ 0.0000083 AU'),
            (2492,
             '    # = 19,596 km x (0.122 / 1.122) ~ 2,131 km ~ 0.0000142 AU',
             '    # Calculation+: = 19,596 km x (0.122 / 1.122) ~ 2,131 km ~ 0.0000142 AU'),
            (55,
             '# entries are unchanged and cross-check exactly against the same IAU table.',
             '# Source+: entries are unchanged and cross-check exactly against the same IAU table.'),
            (54,
             '# yields a correct spin pole for every shell body (rotation-axis primitive). The six prior',
             '# Source+: yields a correct spin pole for every shell body (rotation-axis primitive). The six prior'),
            (53,
             '# N15+ (June 2026): Sun/Mercury/Venus/Earth/Moon added so create_planet_transformation_matrix',
             '# Source+: N15+ (June 2026): Sun/Mercury/Venus/Earth/Moon added so create_planet_transformation_matrix'),
            (52,
             '#         (Table 1, planets/Sun; Table 2, Moon mean pole 269.9949/66.5392, E-terms dropped).',
             '# Source+: (Table 1, planets/Sun; Table 2, Moon mean pole 269.9949/66.5392, E-terms dropped).'),
        ],
    },
    'info_dictionary.py': {
        'fp': '751963a0833e294332a24f0c305e368a',
        'edits': [
            (242,
             '# (Full version including sub-types: 0, Ia+, Ia, Iab, Ib, sd, D)',
             '# Source+: (Full version including sub-types: 0, Ia+, Ia, Iab, Ib, sd, D)'),
            (241,
             '# Mapping of Roman numerals to luminosity class descriptions',
             '# Source+: Mapping of Roman numerals to luminosity class descriptions'),
            (106,
             '# Mapping of SIMBAD object types to full descriptions',
             '# Source+: Mapping of SIMBAD object types to full descriptions'),
        ],
    },
    'neptune_visualization_shells.py': {
        'fp': '269fc048fea6e1af7ad4fa52c1981d06',
        'edits': [
            (1348,
             '            #         confirmed Voyager 2 1989; Galatea resonance confinement confirmed.',
             '            # Source+: confirmed Voyager 2 1989; Galatea resonance confinement confirmed.'),
            (1169,
             '#         "13 known rings" is a high estimate; updated to 5 primary named rings per current consensus.',
             '# Source+: "13 known rings" is a high estimate; updated to 5 primary named rings per current consensus.'),
            (1168,
             '#         Neptune has 5 named rings (Galle, Le Verrier, Lassell, Arago, Adams) plus diffuse sheets.',
             '# Source+: Neptune has 5 named rings (Galle, Le Verrier, Lassell, Arago, Adams) plus diffuse sheets.'),
            (910,
             '            #         Neptune dipole 47 deg tilt, 0.55 R_N offset from center.',
             '            # Source+: Neptune dipole 47 deg tilt, 0.55 R_N offset from center.'),
            (834,
             '    # Belt names and descriptions based on current understanding',
             '    # Source+: Belt names and descriptions based on current understanding'),
            (833,
             '    #         Belt locations (1.2-2.5 R_N inner, 3.5 R_N electron, 6.0 R_N plasma sheet, 4.2 R_N cusps) confirmed.',
             '    # Source+: Belt locations (1.2-2.5 R_N inner, 3.5 R_N electron, 6.0 R_N plasma sheet, 4.2 R_N cusps) confirmed.'),
            (832,
             '    #         Voyager 2 is the only spacecraft to visit Neptune; all belt parameters derive from 1989 flyby data.',
             '    # Source+: Voyager 2 is the only spacecraft to visit Neptune; all belt parameters derive from 1989 flyby data.'),
            (595,
             '    # from center. Confirmed NASA "30 Years Ago: Voyager 2 Explores Neptune" (2024).    ',
             '    # Source+: from center. Confirmed NASA "30 Years Ago: Voyager 2 Explores Neptune" (2024).'),
            (594,
             '    # offset tilted dipole inclined 47 deg to rotation axis, displaced 0.55 R_N',
             '    # Source+: offset tilted dipole inclined 47 deg to rotation axis, displaced 0.55 R_N'),
            (460,
             '#         47 deg tilt and 0.55 R_N offset discovered by Voyager 2, 1989.',
             '# Source+: 47 deg tilt and 0.55 R_N offset discovered by Voyager 2, 1989.'),
            (219,
             '        #         record confirmed; cloud cover decrease linked to solar cycle (2024 Keck/Lick/Hubble study).',
             '        # Source+: record confirmed; cloud cover decrease linked to solar cycle (2024 Keck/Lick/Hubble study).'),
            (195,
             '#         Wind speed 2,100 km/h is solar system record; H2/He/CH4 composition confirmed.',
             '# Source+: Wind speed 2,100 km/h is solar system record; H2/He/CH4 composition confirmed.'),
            (130,
             '        #         mantle 80-85% R_N, 2,000-5,000 K, superionic water and diamond rain confirmed.',
             '        # Source+: mantle 80-85% R_N, 2,000-5,000 K, superionic water and diamond rain confirmed.'),
            (111,
             '#         superionic water and diamond rain confirmed by high-pressure experiments; 10-15 Earth masses confirmed.',
             '# Source+: superionic water and diamond rain confirmed by high-pressure experiments; 10-15 Earth masses confirmed.'),
            (55,
             '        #         core mass ~1.2 Earth masses, pressure ~700-800 GPa, temperature ~5,100 degC confirmed.',
             '        # Source+: core mass ~1.2 Earth masses, pressure ~700-800 GPa, temperature ~5,100 degC confirmed.'),
            (38,
             '#         core ~1.2 Earth masses, ~700-800 GPa, ~5,100 degC; iron/nickel/silicate composition confirmed.',
             '# Source+: core ~1.2 Earth masses, ~700-800 GPa, ~5,100 degC; iron/nickel/silicate composition confirmed.'),
        ],
    },
    'orbital_elements.py': {
        'fp': '9cd216a0f29b15f510741ac550ac7ab4',
        'edits': [
            (23,
             '        #   Here are the updated values with J2000.0 mean elements. ',
             '        # Source+: Here are the updated values with J2000.0 mean elements.'),
            (22,
             '        #   JPL Approximate Positions: https://ssd.jpl.nasa.gov/planets/approx_pos.html',
             '        # Source+: JPL Approximate Positions: https://ssd.jpl.nasa.gov/planets/approx_pos.html'),
        ],
    },
    'palomas_orrery.py': {
        'fp': 'b536c56fde8424f3bc636bdd3ff37c1f',
        'edits': [
            (10297,
             '#         literal with no link to the store until 2026-08-07 (L-179).',
             '# Source+: literal with no link to the store until 2026-08-07 (L-179).'),
            (10296,
             '#         Interpolated rather than typed: this site carried a stale 126,000',
             '# Source+: Interpolated rather than typed: this site carried a stale 126,000'),
        ],
    },
    'planet9_visualization_shells.py': {
        'fp': '4388cb1754e77b38cc79d922040d05d3',
        'edits': [
            (233,
             '        #         Planet Nine is hypothetical -- all values are model predictions.',
             '        # Source+: Planet Nine is hypothetical -- all values are model predictions.'),
            (232,
             '        #         Using perihelion distance in Hill sphere formula is more physically accurate for satellite stability.',
             '        # Source+: Using perihelion distance in Hill sphere formula is more physically accurate for satellite stability.'),
            (231,
             '        #         a=600 AU baseline (2021 refinement: ~460 AU central estimate), e=0.30, m=6 Earth masses.',
             '        # Source+: a=600 AU baseline (2021 refinement: ~460 AU central estimate), e=0.30, m=6 Earth masses.'),
            (213,
             '#         Planet Nine is hypothetical -- all values are model predictions, not confirmed observations.',
             '# Source+: Planet Nine is hypothetical -- all values are model predictions, not confirmed observations.'),
            (212,
             '#         Note: 2021 refinement favors a=460 +/- 100 AU as central estimate; 600 AU remains valid for visualization.',
             '# Source+: Note: 2021 refinement favors a=460 +/- 100 AU as central estimate; 600 AU remains valid for visualization.'),
            (211,
             '#         Hill sphere ~7.6 AU derived from a=600 AU, e=0.30, m=6 Earth masses.',
             '# Source+: Hill sphere ~7.6 AU derived from a=600 AU, e=0.30, m=6 Earth masses.'),
            (56,
             '        #         Planet Nine is hypothetical -- all values are model predictions.',
             '        # Source+: Planet Nine is hypothetical -- all values are model predictions.'),
            (55,
             '        #         3.7 Earth radii for 5-10 Earth mass ice giant; composition modeled on Uranus/Neptune.',
             '        # Source+: 3.7 Earth radii for 5-10 Earth mass ice giant; composition modeled on Uranus/Neptune.'),
            (36,
             '#         Planet Nine is hypothetical -- all values are model predictions, not confirmed observations.',
             '# Source+: Planet Nine is hypothetical -- all values are model predictions, not confirmed observations.'),
            (35,
             '#         radius 3-4 Earth radii (~3.7 R_E) from thermal evolution models for 5-10 Earth mass ice giant.',
             '# Source+: radius 3-4 Earth radii (~3.7 R_E) from thermal evolution models for 5-10 Earth mass ice giant.'),
        ],
    },
    'saturn_visualization_shells.py': {
        'fp': '636d9194c757ec1ec2a4aa06892245f9',
        'edits': [
            (1229,
             '#         magnetic axis tilt <0.1 deg (unique among planets), Enceladus as dominant plasma source confirmed.',
             '# Source+: magnetic axis tilt <0.1 deg (unique among planets), Enceladus as dominant plasma source confirmed.'),
            (950,
             '        #         Hill sphere ~91 million km / ~151 Saturn radii at semi-major axis confirmed.',
             '        # Source+: Hill sphere ~91 million km / ~151 Saturn radii at semi-major axis confirmed.'),
            (930,
             '#         Hill sphere ~91 million km / ~151 Saturn radii confirmed.',
             '# Source+: Hill sphere ~91 million km / ~151 Saturn radii confirmed.'),
            (769,
             '    #         geyser rate hundreds kg/s, plasma loading ~100 kg/s, E ring fed by Enceladus ice confirmed.',
             '    # Source+: geyser rate hundreds kg/s, plasma loading ~100 kg/s, E ring fed by Enceladus ice confirmed.'),
            (501,
             '        #         thermosphere ~300 degC / 570 K at poles from auroral heating confirmed.',
             '        # Source+: thermosphere ~300 degC / 570 K at poles from auroral heating confirmed.'),
            (297,
             '        #         composition, wind speed, hexagonal jet stream, cloud deck order all confirmed.',
             '        # Source+: composition, wind speed, hexagonal jet stream, cloud deck order all confirmed.'),
            (276,
             '#         ~75% H2, ~25% He, winds 1,800 km/h, north pole hexagon, cloud deck order all confirmed.',
             '# Source+: ~75% H2, ~25% He, winds 1,800 km/h, north pole hexagon, cloud deck order all confirmed.'),
            (140,
             '        #         transition at 0.4-0.5 R, weaker field than Jupiter, ~6,000 K at transition confirmed.',
             '        # Source+: transition at 0.4-0.5 R, weaker field than Jupiter, ~6,000 K at transition confirmed.'),
            (54,
             '        #         fuzzy core (ring seismology) to ~60% R; ~17 Earth masses rock/ice in ~55 Earth mass total region confirmed.',
             '        # Source+: fuzzy core (ring seismology) to ~60% R; ~17 Earth masses rock/ice in ~55 Earth mass total region confirmed.'),
            (37,
             '#         fuzzy core to ~60% R, ~17 Earth masses rock/ice (~55 total with H/He), ~11,700-12,000 K confirmed.',
             '# Source+: fuzzy core to ~60% R, ~17 Earth masses rock/ice (~55 total with H/He), ~11,700-12,000 K confirmed.'),
        ],
    },
    'scenarios_heatwaves.py': {
        'fp': 'fb192c8501ec6444b5e2d040e9b1b9c1',
        'edits': [
            (705,
             '        #   fresh source check at build time -- do not backfill from recall.',
             '        # Source+: fresh source check at build time -- do not backfill from recall.'),
            (704,
             '        #   figures below are deliberately [TO-FETCH] pending a real fetch and a',
             '        # Source+: figures below are deliberately [TO-FETCH] pending a real fetch and a'),
            (703,
             "        #   event's June 27-Jul 1 peak as of this scaffold; all peak/station",
             "        # Source+: event's June 27-Jul 1 peak as of this scaffold; all peak/station"),
            (702,
             '        #   retrieved 2026-06-30). No observed wet-bulb field exists yet for the',
             '        # Source+: retrieved 2026-06-30). No observed wet-bulb field exists yet for the'),
            (701,
             '        #   available by 12 UTC (Copernicus C3S / ECMWF CDS documentation,',
             '        # Source+: available by 12 UTC (Copernicus C3S / ECMWF CDS documentation,'),
        ],
    },
    'shell_configs.py': {
        'fp': '2d0c516ab353fe2da75917fe1e8920db',
        'edits': [
            (2648,
             '    #         Smith et al. (1989, Science); NASA Planetary Ring Node.',
             '    # Source+: Smith et al. (1989, Science); NASA Planetary Ring Node.'),
            (2558,
             '    #         Elliot et al. (1977) Nature; de Pater et al. (2006).',
             '    # Source+: Elliot et al. (1977) Nature; de Pater et al. (2006).'),
            (2442,
             '    #         NASA Voyager 2 Saturn Encounter; Mankovich & Fuller (2021).',
             '    # Source+: NASA Voyager 2 Saturn Encounter; Mankovich & Fuller (2021).'),
            (2441,
             '    #         NASA Saturn Magnetosphere Overview; Cassini Mission: Enceladus;',
             '    # Source+: NASA Saturn Magnetosphere Overview; Cassini Mission: Enceladus;'),
            (2341,
             '    #         NASA Jupiter Magnetosphere Overview.',
             '    # Source+: NASA Jupiter Magnetosphere Overview.'),
            (2340,
             '    #         Galileo plasma instrument data (Io torus);',
             '    # Source+: Galileo plasma instrument data (Io torus);'),
            (2241,
             '    #         Inner radiation belt ~1.5 R_E (protons), outer ~4.5 R_E (electrons).',
             '    # Source+: Inner radiation belt ~1.5 R_E (protons), outer ~4.5 R_E (electrons).'),
            (2240,
             '    #         sunward, magnetotail ~100 R_E. Bow shock standoff ~15 R_E.',
             '    # Source+: sunward, magnetotail ~100 R_E. Bow shock standoff ~15 R_E.'),
            (2239,
             "    #         NASA Heliophysics. Earth's magnetosphere extends ~10 R_E",
             "    # Source+: NASA Heliophysics. Earth's magnetosphere extends ~10 R_E"),
            (2238,
             '    #         NASA Van Allen Probes (radiation belts, 2012-2019);',
             '    # Source+: NASA Van Allen Probes (radiation belts, 2012-2019);'),
            (2202,
             '    #         (Acuna et al. 1999 -- MGS MAG/ER discovery).',
             '    # Source+: (Acuna et al. 1999 -- MGS MAG/ER discovery).'),
            (2201,
             '    #         induced magnetosphere, bow shock ~1.64 Rm (Vignes et al. 2000),',
             '    # Source+: induced magnetosphere, bow shock ~1.64 Rm (Vignes et al. 2000),'),
            (2165,
             '    #         induced magnetosphere, bow shock 1.3-1.7 Rv, comet-shaped tail.',
             '    # Source+: induced magnetosphere, bow shock 1.3-1.7 Rv, comet-shaped tail.'),
            (1872,
             '    #         NASA Heliophysics; IAU 2015 nominal solar radius.',
             '    # Source+: NASA Heliophysics; IAU 2015 nominal solar radius.'),
            (1806,
             '    #         Ness et al. (1989) Science (magnetometer).',
             '    # Source+: Ness et al. (1989) Science (magnetometer).'),
            (1739,
             '    #         Ness et al. (1986) Science (magnetometer).',
             '    # Source+: Ness et al. (1986) Science (magnetometer).'),
            (1662,
             '    #         NASA Saturn Magnetosphere Overview; Mankovich & Fuller (2021).',
             '    # Source+: NASA Saturn Magnetosphere Overview; Mankovich & Fuller (2021).'),
            (1511,
             '    #         (fuzzy core to ~60% R_J).',
             '    # Source+: (fuzzy core to ~60% R_J).'),
            (1510,
             '    #         NASA Solar System Exploration; NASA Juno gravity science',
             '    # Source+: NASA Solar System Exploration; NASA Juno gravity science'),
            (1318,
             '    #         NASA Van Allen Probes, NASA Solar System Dynamics.',
             '    # Source+: NASA Van Allen Probes, NASA Solar System Dynamics.'),
            (1317,
             '    #         NOAA / NCEI (atmosphere boundaries), NASA Goddard,',
             '    # Source+: NOAA / NCEI (atmosphere boundaries), NASA Goddard,'),
            (439,
             '    #         Planet Nine has not been observationally confirmed.',
             '    # Source+: Planet Nine has not been observationally confirmed.'),
            (438,
             '    #         All values are model predictions for a 5-10 Earth-mass ice giant;',
             '    # Source+: All values are model predictions for a 5-10 Earth-mass ice giant;'),
            (437,
             '    #         NASA Solar System Exploration.',
             '    # Source+: NASA Solar System Exploration.'),
            (246,
             '    #         NASA Moon Fact Sheet; NASA Solar System Dynamics (Hill sphere); Draper (1847).',
             '    # Source+: NASA Moon Fact Sheet; NASA Solar System Dynamics (Hill sphere); Draper (1847).'),
            (245,
             '    #         -- deep moonquake source depths;',
             '    # Source+: -- deep moonquake source depths;'),
            (244,
             '    #         Nakamura et al. 1982, JGR 87:A117 and Nakamura 2005, JGR 110',
             '    # Source+: Nakamura et al. 1982, JGR 87:A117 and Nakamura 2005, JGR 110'),
            (243,
             '    #         -- inner core 240 km, outer core 330 km;',
             '    # Source+: -- inner core 240 km, outer core 330 km;'),
            (95,
             '    #         NASA MESSENGER Mission; Winslow et al. 2013 (magnetosphere geometry).',
             '    # Source+: NASA MESSENGER Mission; Winslow et al. 2013 (magnetosphere geometry).'),
            (94,
             '    #         Sori 2018, EPSL 489:92 -- crustal thickness 26 +/- 11 km;',
             '    # Source+: Sori 2018, EPSL 489:92 -- crustal thickness 26 +/- 11 km;'),
        ],
    },
    'solar_visualization_shells.py': {
        'fp': 'e74ab93dc4b265572549b8dba2d8c0d0',
        'edits': [
            (1224,
             '# MAPS disintegration at 8.33 R_sun from SOHO/CCOR-1 observations April 2026',
             '# Source+: MAPS disintegration at 8.33 R_sun from SOHO/CCOR-1 observations April 2026'),
            (851,
             '# CORE_AU=0.2*SOLAR_RADIUS_AU, RADIATIVE_ZONE_AU=0.7*SOLAR_RADIUS_AU in constants_new.py',
             '# Source+: CORE_AU=0.2*SOLAR_RADIUS_AU, RADIATIVE_ZONE_AU=0.7*SOLAR_RADIUS_AU in constants_new.py'),
            (789,
             '# Bahcall et al. standard solar model; SUN_RADIUS_KM=695700 in constants_new.py',
             '# Source+: Bahcall et al. standard solar model; SUN_RADIUS_KM=695700 in constants_new.py'),
            (580,
             '# TERMINATION_SHOCK_AU=94, STREAMER_BELT_RADII=6 in constants_new.py',
             '# Source+: TERMINATION_SHOCK_AU=94, STREAMER_BELT_RADII=6 in constants_new.py'),
            (478,
             '# Dones et al. (2004) Comets II; Golub & Pasachoff (2010) The Solar Corona; NASA solar interior model',
             '# Source+: Dones et al. (2004) Comets II; Golub & Pasachoff (2010) The Solar Corona; NASA solar interior model'),
            (477,
             '# OUTER_CORONA_RADII, INNER_CORONA_RADII, CHROMOSPHERE_PHYSICAL_RADII, GRAVITATIONAL_INFLUENCE_AU, Oort Cloud AU constants);',
             '# Source+: OUTER_CORONA_RADII, INNER_CORONA_RADII, CHROMOSPHERE_PHYSICAL_RADII, GRAVITATIONAL_INFLUENCE_AU, Oort Cloud AU constants);'),
            (95,
             '#         System Exploration for the heliopause and Oort Cloud framing.',
             '# Source+: System Exploration for the heliopause and Oort Cloud framing.'),
            (65,
             '#         from AU_PER_LIGHT_YEAR. NASA Solar System Exploration.',
             '# Source+: from AU_PER_LIGHT_YEAR. NASA Solar System Exploration.'),
            (64,
             "#         midpoint (Tony's ruling, 2026-08-07). Light-year figures derive",
             "# Source+: midpoint (Tony's ruling, 2026-08-07). Light-year figures derive"),
            (63,
             '#         100,000-200,000 AU; the visualization draws the 150,000 AU',
             '# Source+: 100,000-200,000 AU; the visualization draws the 150,000 AU'),
            (62,
             '#         Milky Way, model-dependent. Published estimates span',
             '# Source+: Milky Way, model-dependent. Published estimates span'),
            (61,
             '#         in constants_new.py -- approximate Hill sphere of the Sun in the',
             '# Source+: in constants_new.py -- approximate Hill sphere of the Sun in the'),
        ],
    },
    'spacecraft_encounters.py': {
        'fp': '040477e94b69b742ff781a0a6c44d577',
        'edits': [
            (145,
             '            #         12,472 km altitude, 13.78 km/s, 28,800 km Charon distance, Sputnik Planitia all confirmed.',
             '            # Source+: 12,472 km altitude, 13.78 km/s, 28,800 km Charon distance, Sputnik Planitia all confirmed.'),
            (116,
             '            #         slowed to ~19 km/s at Jupiter, +4 km/s assist, 3 years saved confirmed.',
             '            # Source+: slowed to ~19 km/s at Jupiter, +4 km/s assist, 3 years saved confirmed.'),
            (115,
             '            #         launch 16.26 km/s (fastest ever at launch), heliocentric ~43-45 km/s,',
             '            # Source+: launch 16.26 km/s (fastest ever at launch), heliocentric ~43-45 km/s,'),
        ],
    },
    'star_notes.py': {
        'fp': 'f32cdbc4598c4176317a50b16ca0c7d6',
        'edits': [
            (927,
             '        # runaway from Vela OB2 association at >60 km/s, rotation ~220 km/s',
             '        # Source+: runaway from Vela OB2 association at >60 km/s, rotation ~220 km/s'),
            (896,
             '        # Fomalhaut c status contested; distance ~25 ly, 18th brightest, spectral type A3V',
             '        # Source+: Fomalhaut c status contested; distance ~25 ly, 18th brightest, spectral type A3V'),
            (805,
             '        # illuminates Flame Nebula NGC 2024 and Horsehead Nebula region',
             '        # Source+: illuminates Flame Nebula NGC 2024 and Horsehead Nebula region'),
            (790,
             '        # NGC 1990 reflection nebula',
             '        # Source+: NGC 1990 reflection nebula'),
            (775,
             '        # O9.5 II, distance ~1200 ly (Hipparcos/Gaia). Gemini fact-check Apr 2026: corrected from 900 ly.',
             '        # Source+: O9.5 II, distance ~1200 ly (Hipparcos/Gaia). Gemini fact-check Apr 2026: corrected from 900 ly.'),
        ],
    },
    'uranus_visualization_shells.py': {
        'fp': '6369dd817786c37c81d37867b2293cf9',
        'edits': [
            (802,
             '# de Pater et al. (2006) Science -- ring properties, widths, colors; Showalter & Lissauer (2006)',
             '# Source+: de Pater et al. (2006) Science -- ring properties, widths, colors; Showalter & Lissauer (2006)'),
            (624,
             '    # asymmetry from ~60-deg magnetic tilt, Voyager 2 (1986) sole in-situ measurement',
             '    # Source+: asymmetry from ~60-deg magnetic tilt, Voyager 2 (1986) sole in-situ measurement'),
            (533,
             '    # sheet). Sidereal rotation ~17.24 h (17h 14m).',
             '    # Source+: sheet). Sidereal rotation ~17.24 h (17h 14m).'),
            (532,
             '    # Dipole offset 0.3 R_U (~1/3 radius). Axial tilt 97.77 deg (NASA Uranus fact',
             '    # Source+: Dipole offset 0.3 R_U (~1/3 radius). Axial tilt 97.77 deg (NASA Uranus fact'),
            (531,
             "    # spurious digits. Not a 'refined value' question -- a significant-figures one.",
             "    # Source+: spurious digits. Not a 'refined value' question -- a significant-figures one."),
            (530,
             '    # so 60, ~59, and the often-cited 58.6 are the same measurement and 58.6 is',
             '    # Source+: so 60, ~59, and the often-cited 58.6 are the same measurement and 58.6 is'),
            (529,
             "    # a single flyby's tilt determination does not justify sub-degree precision,",
             "    # Source+: a single flyby's tilt determination does not justify sub-degree precision,"),
            (528,
             '    # Dipole-vs-rotation tilt reported as 60 deg. Display uses 60 (one sig fig):',
             '    # Source+: Dipole-vs-rotation tilt reported as 60 deg. Display uses 60 (one sig fig):'),
        ],
    },
}


MARKER_RE = re.compile(
    r'^\s*#\s*(Source|Ref|Also|See|Derived|Calculation)\+:')


def normalized(data):
    return data.replace(b'\r\n', b'\n')


def non_ascii_count(text):
    return sum(1 for ch in text if ord(ch) > 127)


def main():
    if not os.path.isfile('shell_configs.py'):
        print('ERROR: run this from the palomas_orrery repo root '
              '(the folder holding shell_configs.py).')
        return 1

    staged = []
    total = 0
    notes = []

    for name in sorted(EDITS):
        spec = EDITS[name]
        if not os.path.isfile(name):
            print('ERROR: %s not found.' % name)
            return 1

        with open(name, 'rb') as handle:
            raw = handle.read()

        fp = hashlib.md5(normalized(raw)).hexdigest()
        if fp != spec['fp']:
            print('ERROR: %s does not match the base this patch was built '
                  'against.' % name)
            print('       expected %s' % spec['fp'])
            print('       found    %s' % fp)
            print('       Nothing written. If this patch has already run, '
                  'that is the expected abort -- it is one-shot.')
            return 1

        crlf = b'\r\n' in raw
        lines = normalized(raw).decode('utf-8').split('\n')

        for number, old, new in spec['edits']:
            index = number - 1
            if index < 0 or index >= len(lines):
                print('ANCHOR FAIL: %s line %d is past end of file.'
                      % (name, number))
                return 1
            if lines[index] != old:
                print('ANCHOR FAIL: %s line %d does not read as recorded.'
                      % (name, number))
                print('       expected %r' % old)
                print('       found    %r' % lines[index])
                print('       Nothing written.')
                return 1
            if non_ascii_count(new):
                print('ERROR: %s line %d would insert non-ASCII. Nothing '
                      'written.' % (name, number))
                return 1
            lines[index] = new

        text = '\n'.join(lines)
        pre_existing = non_ascii_count(text)
        if pre_existing:
            notes.append('note: %s still holds %d non-ASCII character(s) '
                         'this patch did not reach' % (name, pre_existing))
        out = text.encode('utf-8')
        if crlf:
            out = out.replace(b'\n', b'\r\n')
        markers = sum(1 for _n, _o, new in spec['edits']
                      if MARKER_RE.match(new))
        staged.append((name, out, markers, len(spec['edits']) - markers))
        total += len(out)

    marked = 0
    swept = 0
    for name, out, markers, fixes in staged:
        with open(name, 'wb') as handle:
            handle.write(out)
        if fixes:
            print('ok  %-38s %3d marked, %d non-ASCII fixed in passing'
                  % (name, markers, fixes))
        else:
            print('ok  %-38s %3d lines marked' % (name, markers))
        marked += markers
        swept += fixes

    for note in notes:
        print(note)
    print('patch applied (%d bytes, %d continuation lines marked in %d '
          'files, %d pre-existing non-ASCII character(s) fixed in passing)'
          % (total, marked, len(staged), swept))
    print('')
    print('One run is deliberately unmarked: test_citation_inheritance.py '
          'lines 122-123. See the module docstring.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
