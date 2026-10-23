r"""patch_L443_1_slice1_orrery_20261022.py -- L-443, slice 1 of the
orrery's objects on the website: the orrery half.

RUN COMMAND
    python patch_L443_1_slice1_orrery_20261022.py

Save it in the ORRERY repository's root folder
(C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\),
open it in VS Code and click Run. Then move it to documentation/.

WHAT IT CHANGES (built on orrery bfb6c474)
    celestial_objects.py  50 entries keyed, each with JPL's exact name;
                          their descriptions and links by the words list
                          Tony approved (WORDS_L443_slice1_20261022.md);
                          Schaumasse, Howell and Churyumov-Gerasimenko
                          re-pinned to JPL's newest records; Tempel 2's
                          wrong Deep Space 1 comment corrected
    export_objects.py     a keyed entry with a helio_id is served by it,
                          as a small body (served_identity)
    period_fetch.py       the same record for the period
    palomas_orrery.py     the elements pre-fetch, static and animated,
                          asks a body's helio_id around the Sun
    test_objects_export.py  a check, with a planted fault, that a
                          helio_id entry is served by it
    test_period_fetch.py  a planted fault's anchor follows the code

Permanent: every change above. The script itself is one-shot.

SUCCESS prints one "ok" line per file, then "patch applied".
FAILURE prints one FAILURE line, and NOTHING is written. Each code file
is checked against the content it was built on; undo is Discard Changes
in GitHub Desktop.

NEXT: patch_L443_3_close_20261022.py, then the orrery maintenance run
(HANDOFF_L443_slice1_build_20261022.md, section 2).

Role: devtool
Domain: dev_tools

Written October 22, 2026 with Anthropic's Claude Opus 5.5.
"""

import hashlib
import os
import sys

TITLE = 'L-443 slice 1, orrery'
FILES = [
    {"path": 'celestial_objects.py', "kind": "edit", "guard": 'md5', "md5": 'f5dd18d599cce00fc9d13fed8e526b4a', "edits": [
        (b'own entry, record 90000091, which until now only the website defined).\n"""\n',
         b'own entry, record 90000091, which until now only the website defined).\nModule updated: October 22, 2026 with Anthropic\'s Claude Opus 5.5 (L-443,\nslice 1 of the objects to the website: 50 entries keyed, each with JPL\'s\nname; their descriptions sourced or trimmed and their links one per body,\nby the words list Tony approved; Schaumasse, Howell and\nChuryumov-Gerasimenko re-pinned to JPL\'s newest records; a wrong Deep\nSpace 1 comment on Tempel 2 corrected).\n"""\n'),
        (b"    {'name': 'Eurybates', 'id': '1973 SO', 'var_name': 'eurybates_var', 'color_key': 'Eurybates', 'symbol': 'circle-open', 'object_type': 'orbital', \n",
         b"    {'name': 'Eurybates', 'key': 'eurybates', 'id': '1973 SO', 'horizons_name': '3548 Eurybates', 'var_name': 'eurybates_var', 'color_key': 'Eurybates', 'symbol': 'circle-open', 'object_type': 'orbital', \n"),
        (b"    'mission_info': 'Lucy flyby: Aug 12, 2027. D~64 km, C-type. Has satellite Queta (~1 km). First C-type Trojan to be visited.', \n    'mission_url': 'https://lucy.swri.edu/Eurybates.html'},\n",
         b"    'mission_info': 'Lucy flies past it on August 11, 2027. A C-type (carbon-rich) asteroid with a small moon, Queta.', \n    'mission_url': 'https://en.wikipedia.org/wiki/3548_Eurybates'},\n"),
        (b"    {'name': 'Patroclus', 'id': '920000617', 'var_name': 'patroclus_var', 'color_key': 'Patroclus', \n",
         b"    {'name': 'Patroclus', 'key': 'patroclus', 'id': '920000617', 'horizons_name': '617 Patroclus', 'var_name': 'patroclus_var', 'color_key': 'Patroclus', \n"),
        (b"     'mission_info': 'Primary body of binary Trojan. D=113 km. Binary period: 4.28 days. Lucy flyby: March 3, 2033.',\n     'mission_url': 'https://lucy.swri.edu/targets/Patroclus-Menoetius.html'},\n",
         b"     'mission_info': 'Two Jupiter Trojans of nearly the same size, Patroclus and Menoetius, orbiting each other. Lucy flies past them in March 2033.',\n     'mission_url': 'https://en.wikipedia.org/wiki/617_Patroclus'},\n"),
        (b"    {'name': 'Polymele', 'id': '1999 WB2', 'var_name': 'polymele_var', 'color_key': 'Polymele', 'symbol': 'circle-open', 'object_type': 'orbital', \n",
         b"    {'name': 'Polymele', 'key': 'polymele', 'id': '1999 WB2', 'horizons_name': '15094 Polymele', 'var_name': 'polymele_var', 'color_key': 'Polymele', 'symbol': 'circle-open', 'object_type': 'orbital', \n"),
        (b"    'mission_info': 'Lucy flyby: Sep 15, 2027. D~21 km, P-type. Has satellite Shaun (~5 km, discovered 2022 via occultation).', \n    'mission_url': 'https://lucy.swri.edu/Polymele.html'},\n",
         b"    'mission_info': 'Lucy flies past it in September 2027. A P-type (primitive) asteroid with a small moon, Shaun, found in 2022 when Polymele passed in front of a star.', \n    'mission_url': 'https://en.wikipedia.org/wiki/15094_Polymele'},\n"),
        (b"    {'name': 'Leucus', 'id': '1997 TS25', 'var_name': 'leucus_var', 'color_key': 'Leucus', 'symbol': 'circle-open', 'object_type': 'orbital', \n",
         b"    {'name': 'Leucus', 'key': 'leucus', 'id': '1997 TS25', 'horizons_name': '11351 Leucus', 'var_name': 'leucus_var', 'color_key': 'Leucus', 'symbol': 'circle-open', 'object_type': 'orbital', \n"),
        (b"    'mission_info': 'Lucy flyby: Apr 18, 2028. D~40 km, D-type. Extremely slow rotator (~446 hours). Dark, primitive surface.', \n    'mission_url': 'https://lucy.swri.edu/Leucus.html'},\n",
         b"    'mission_info': 'Lucy flies past it on April 18, 2028. A D-type asteroid with a dark, primitive surface, which rotates very slowly.', \n    'mission_url': 'https://en.wikipedia.org/wiki/11351_Leucus'},\n"),
        (b"    {'name': 'Orus', 'id': '1999 VQ10', 'var_name': 'orus_var', 'color_key': 'Orus', 'symbol': 'circle-open', 'object_type': 'orbital', \n",
         b"    {'name': 'Orus', 'key': 'orus', 'id': '1999 VQ10', 'horizons_name': '21900 Orus', 'var_name': 'orus_var', 'color_key': 'Orus', 'symbol': 'circle-open', 'object_type': 'orbital', \n"),
        (b"    'mission_info': 'Lucy flyby: Nov 11, 2028. D~51 km, D-type. Last L4 Trojan visit before heading to L5.', \n    'mission_url': 'https://lucy.swri.edu/Orus.html'},\n",
         b"    'mission_info': 'Lucy flies past it on November 11, 2028, its last stop among the Trojans that lead Jupiter. A D-type asteroid.', \n    'mission_url': 'https://en.wikipedia.org/wiki/21900_Orus'},\n"),
        (b"    {'name': 'Chariklo', 'id': '1997 CU26', 'var_name': 'chariklo_var', 'color_key': 'Chariklo', 'symbol': 'circle-open', 'object_type': 'orbital', \n",
         b"    {'name': 'Chariklo', 'key': 'chariklo', 'id': '1997 CU26', 'horizons_name': '10199 Chariklo', 'var_name': 'chariklo_var', 'color_key': 'Chariklo', 'symbol': 'circle-open', 'object_type': 'orbital', \n"),
        (b"    'mission_info': 'Horizons: 1997 CU26. Large Centaur. Retrograde (left-handed) orbit.', \n",
         b"    'mission_info': 'Horizons: 1997 CU26. Large Centaur.', \n"),
        (b"    {'name': 'Ceres', 'id': 'A801 AA', 'var_name': 'ceres_var', 'color_key': 'Ceres', 'symbol': 'circle', 'object_type': 'orbital', \n",
         b"    {'name': 'Ceres', 'key': 'ceres', 'id': 'A801 AA', 'horizons_name': '1 Ceres', 'var_name': 'ceres_var', 'color_key': 'Ceres', 'symbol': 'circle', 'object_type': 'orbital', \n"),
        (b'    \'mission_info\': \'Horizons: A801 AA. NASA: "Ceres was the first object discovered in the main asteroid belt. Dawn spacecraft orbited Ceres from 2015 to 2018."\', \n    \'mission_url\': \'https://science.nasa.gov/mission/dawn/science/ceres/\'},\n',
         b'    \'mission_info\': \'Horizons: A801 AA. NASA: "Ceres was the first object discovered in the main asteroid belt and is named for the Roman goddess of agriculture." NASA\\\'s Dawn spacecraft went into orbit around it in 2015.\', \n    \'mission_url\': \'https://science.nasa.gov/dwarf-planets/ceres/\'},\n'),
        (b"    {'name': 'Haumea', 'id': '920136108', 'var_name': 'haumea_var', \n",
         b"    {'name': 'Haumea', 'key': 'haumea', 'id': '920136108', 'horizons_name': '136108 Haumea', 'var_name': 'haumea_var', \n"),
        (b"    'mission_info': 'Horizons: 136108 Haumea. Egg-shaped dwarf planet with rings. Moon periods: Hi\\'iaka 49 days, Namaka 18 days. Rotation: 3.9 hours.', \n",
         b"    'mission_info': 'Horizons: 136108 Haumea. A dwarf planet with rings, spinning about once every 4 hours, fast enough to stretch it into an oval like a football.', \n"),
        (b"    {'name': 'Eris', 'id': '920136199', 'var_name': 'eris_var', 'color_key': 'Eris', 'symbol': 'circle', 'object_type': 'orbital', \n",
         b"    {'name': 'Eris', 'key': 'eris', 'id': '920136199', 'horizons_name': '136199 Eris', 'var_name': 'eris_var', 'color_key': 'Eris', 'symbol': 'circle', 'object_type': 'orbital', \n"),
        (b"    'mission_info': 'Horizons: 136199 Eris. Most massive dwarf planet (27% more than Pluto). Binary period with Dysnomia: 15.79 days.', \n",
         b"    'mission_info': 'Horizons: 136199 Eris. The most massive known dwarf planet, about the same size as Pluto.', \n"),
        (b"    {'name': 'Gonggong', 'id': '920225088', 'var_name': 'gonggong_var', 'color_key': 'Gonggong', 'symbol': 'circle', 'object_type': 'orbital', \n",
         b"    {'name': 'Gonggong', 'key': 'gonggong', 'id': '920225088', 'horizons_name': '225088 Gonggong', 'var_name': 'gonggong_var', 'color_key': 'Gonggong', 'symbol': 'circle', 'object_type': 'orbital', \n"),
        (b"    'mission_info': 'Horizons: 225088 Gonggong. Dwarf planet with highly inclined orbit. Binary period with Xiangliu: 25.22 days.', \n",
         b"    'mission_info': 'Horizons: 225088 Gonggong. Dwarf planet with a highly inclined orbit.', \n"),
        (b"\n    {'name': 'Makemake', 'id': '20136472', 'var_name': 'makemake_var', 'color_key': 'Makemake', 'symbol': 'circle', 'object_type': 'orbital', \n    'id_type': 'majorbody',\n",
         b"\n    {'name': 'Makemake', 'key': 'makemake', 'id': '20136472', 'horizons_name': '136472 Makemake', 'var_name': 'makemake_var', 'color_key': 'Makemake', 'symbol': 'circle', 'object_type': 'orbital', \n    'id_type': 'majorbody',\n"),
        (b"    {'name': 'Mani', 'id': '2002 MS4', 'var_name': 'ms4_var', 'color_key': 'MS4', 'symbol': 'circle', 'object_type': 'orbital', \n",
         b"    {'name': 'Mani', 'key': 'mani', 'id': '2002 MS4', 'horizons_name': '307261 Mani', 'var_name': 'ms4_var', 'color_key': 'MS4', 'symbol': 'circle', 'object_type': 'orbital', \n"),
        (b"    'mission_info': 'Horizons: 2002 MS4. One of the largest unnumbered Kuiper Belt Objects with no known moons.', \n    'mission_url': 'https://www.minorplanetcenter.net/db_search/show_object?object_id=2002+MS4'},\n",
         b"    'mission_info': 'Horizons: 2002 MS4. One of the largest Kuiper Belt objects with no known moons.', \n    'mission_url': 'https://en.wikipedia.org/wiki/307261_Mani'},\n"),
        (b"    {'name': 'Orcus', 'id': '920090482', 'var_name': 'orcus_var', 'color_key': 'Orcus', 'symbol': 'circle', 'object_type': 'orbital', \n",
         b"    {'name': 'Orcus', 'key': 'orcus', 'id': '920090482', 'horizons_name': '90482 Orcus', 'var_name': 'orcus_var', 'color_key': 'Orcus', 'symbol': 'circle', 'object_type': 'orbital', \n"),
        (b"    'mission_info': 'Horizons: 90482 Orcus. Dwarf planet with moon Vanth. Binary period: 9.54 days. Highest mass ratio (~16%) of any known binary.', \n",
         b"    'mission_info': 'Horizons: 90482 Orcus. A dwarf planet with a large moon, Vanth, about 16% of its mass: the highest share of any known planet or dwarf planet and its moon.', \n"),
        (b"    {'name': 'Quaoar', 'id': '920050000', 'var_name': 'quaoar_var', 'color_key': 'Quaoar', 'symbol': 'circle', 'object_type': 'orbital', \n",
         b"    {'name': 'Quaoar', 'key': 'quaoar', 'id': '920050000', 'horizons_name': '50000 Quaoar', 'var_name': 'quaoar_var', 'color_key': 'Quaoar', 'symbol': 'circle', 'object_type': 'orbital', \n"),
        (b"    'mission_info': 'Horizons: 50000 Quaoar. Kuiper Belt dwarf planet with ring system (discovered 2023). Binary period with Weywot: 12.44 days.', \n    'mission_url': 'https://solarsystem.nasa.gov/planets/dwarf-planets/quaoar/in-depth/'},\n",
         b"    'mission_info': 'Horizons: 50000 Quaoar. Kuiper Belt dwarf planet with a ring system, announced in 2023.', \n    'mission_url': 'https://en.wikipedia.org/wiki/50000_Quaoar'},\n"),
        (b"    {'name': 'Sedna', 'id': '2003 VB12', 'var_name': 'sedna_var', 'color_key': 'Sedna', 'symbol': 'circle', 'object_type': 'orbital', \n",
         b"    {'name': 'Sedna', 'key': 'sedna', 'id': '2003 VB12', 'horizons_name': '90377 Sedna', 'var_name': 'sedna_var', 'color_key': 'Sedna', 'symbol': 'circle', 'object_type': 'orbital', \n"),
        (b"    'mission_url': 'https://solarsystem.nasa.gov/planets/dwarf-planets/sedna/in-depth/'},\n",
         b"    'mission_url': 'https://en.wikipedia.org/wiki/Sedna_(dwarf_planet)'},\n"),
        (b"    {'name': 'Leleakuhonua', 'id': '2015 TG387', 'var_name': 'leleakuhonua_var', 'color_key': 'Leleakuhonua', 'symbol': 'circle', 'object_type': 'orbital', \n",
         b"    {'name': 'Leleakuhonua', 'key': 'leleakuhonua', 'id': '2015 TG387', 'horizons_name': '541132 Leleakuhonua', 'var_name': 'leleakuhonua_var', 'color_key': 'Leleakuhonua', 'symbol': 'circle', 'object_type': 'orbital', \n"),
        (b"    {'name': '2017 OF201', 'id': '2017 OF201', 'var_name': 'of201_var', 'color_key': '2017 OF201', 'symbol': 'circle', 'object_type': 'orbital', \n",
         b"    {'name': '2017 OF201', 'key': 'tno_2017_of201', 'id': '2017 OF201', 'horizons_name': '(2017 OF201)', 'var_name': 'of201_var', 'color_key': '2017 OF201', 'symbol': 'circle', 'object_type': 'orbital', \n"),
        (b"    'mission_info': 'Horizons: 2017 OF201. A extreme trans-Neptunian object with an extremely long orbit.', \n    'mission_url': 'https://en.wikipedia.org/wiki/2017_OF201#:~:text=2017%20OF201%20is%20an,have%20a%20directly%20estimated%20size.'},\n",
         b"    'mission_info': 'Horizons: 2017 OF201. An extreme trans-Neptunian object with an extremely long orbit.', \n    'mission_url': 'https://en.wikipedia.org/wiki/2017_OF201'},\n"),
        (b"    {'name': '2025 PN7', 'id': '2025 PN7', 'var_name': 'pn7_var', 'color_key': '2025 PN7', 'symbol': 'circle-open', 'object_type': 'orbital',\n",
         b"    {'name': '2025 PN7', 'key': 'asteroid_2025_pn7', 'id': '2025 PN7', 'horizons_name': '(2025 PN7)', 'var_name': 'pn7_var', 'color_key': '2025 PN7', 'symbol': 'circle-open', 'object_type': 'orbital',\n"),
        (b"    {'name': '2024 PT5', 'id': '2024 PT5', 'var_name': 'pt5_var', 'color_key': '2024 PT5', 'symbol': 'circle-open', 'object_type': 'orbital',\n",
         b"    {'name': '2024 PT5', 'key': 'asteroid_2024_pt5', 'id': '2024 PT5', 'horizons_name': '(2024 PT5)', 'var_name': 'pt5_var', 'color_key': '2024 PT5', 'symbol': 'circle-open', 'object_type': 'orbital',\n"),
        (b"    'mission_info': 'Horizons: 2024 PT5. Closest approach to Earth 8-9-2024.',\n    'mission_url': 'https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=2024%20PT5'},\n",
         b"    'mission_info': 'Horizons: 2024 PT5. Passed closest to Earth on August 8, 2024.',\n    'mission_url': 'https://science.nasa.gov/blogs/planetary-defense/2024/10/02/nasa-to-track-asteroid-2024-pt5-on-next-close-pass-january-2025/'},\n"),
        (b"    {'name': '2025 PY1', 'id': '2025 PY1', 'var_name': 'py1_var', 'color_key': '2025 PY1', 'symbol': 'circle-open', 'object_type': 'orbital',\n",
         b"    {'name': '2025 PY1', 'key': 'asteroid_2025_py1', 'id': '2025 PY1', 'horizons_name': '(2025 PY1)', 'var_name': 'py1_var', 'color_key': '2025 PY1', 'symbol': 'circle-open', 'object_type': 'orbital',\n"),
        (b"    'mission_url': 'https://www.jpl.nasa.gov/asteroid-watch/next-five-approaches/'},    \n",
         b"    'mission_url': 'https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=2025%20PY1'},    \n"),
        (b"    {'name': '2023 JF', 'id': '2023 JF', 'var_name': 'asteroid2023jf_var', 'color_key': '2023 JF', 'symbol': 'circle-open', 'object_type': 'orbital', \n",
         b"    {'name': '2023 JF', 'key': 'asteroid_2023_jf', 'id': '2023 JF', 'horizons_name': '(2023 JF)', 'var_name': 'asteroid2023jf_var', 'color_key': '2023 JF', 'symbol': 'circle-open', 'object_type': 'orbital', \n"),
        (b"    'mission_url': 'https://www.nasa.gov/solar-system/near-earth-object-observations-program/#:~:text=The%20NEO%20Observations%20Program%20sponsors,the%20sky%20to%20determine%20their'},\n",
         b"    'mission_url': 'https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=2023%20JF'},\n"),
        (b"    {'name': '2024 DW', 'id': '2024 DW', 'var_name': 'asteroid_dw_var', 'color_key': '2024 DW', 'symbol': 'circle-open', 'object_type': 'orbital',\n",
         b"    {'name': '2024 DW', 'key': 'asteroid_2024_dw', 'id': '2024 DW', 'horizons_name': '(2024 DW)', 'var_name': 'asteroid_dw_var', 'color_key': '2024 DW', 'symbol': 'circle-open', 'object_type': 'orbital',\n"),
        (b"    'mission_info': 'Horizons: 2024 DW. Closest approach to Earth 2-22-2024 approximately 5 UTC. Keplerian orbit perturbation from Jupiter.',\n",
         b"    'mission_info': 'Horizons: 2024 DW. Passed closest to Earth on February 22, 2024.',\n"),
        (b"    {'name': '2024 YR4', 'id': '2024 YR4', 'var_name': 'yr4_var', 'color_key': '2024 YR4', 'symbol': 'circle-open', 'object_type': 'orbital',\n",
         b"    {'name': '2024 YR4', 'key': 'asteroid_2024_yr4', 'id': '2024 YR4', 'horizons_name': '(2024 YR4)', 'var_name': 'yr4_var', 'color_key': '2024 YR4', 'symbol': 'circle-open', 'object_type': 'orbital',\n"),
        (b"    'mission_info': 'Closest approach to Earth 12-25-2024 4:46 UTC.',\n",
         b"    'mission_info': 'Passed close to Earth on December 25, 2024, two days before it was discovered.',\n"),
        (b"    {'name': 'Kamo oalewa', 'id': '2016 HO3', 'var_name': 'kamooalewa_var', 'color_key': 'Kamo oalewa', 'symbol': 'circle-open', 'object_type': 'orbital',\n",
         b"    {'name': 'Kamo oalewa', 'key': 'kamo_oalewa', 'id': '2016 HO3', 'horizons_name': '469219 Kamo`oalewa', 'var_name': 'kamooalewa_var', 'color_key': 'Kamo oalewa', 'symbol': 'circle-open', 'object_type': 'orbital',\n"),
        (b"    {'name': '16 Psyche', 'id': 'A852 FA', 'var_name': 'psyche16_var', 'color_key': '16 Psyche', 'symbol': 'circle-open', 'object_type': 'orbital',\n",
         b"    {'name': '16 Psyche', 'key': 'psyche', 'id': 'A852 FA', 'horizons_name': '16 Psyche', 'var_name': 'psyche16_var', 'color_key': '16 Psyche', 'symbol': 'circle-open', 'object_type': 'orbital',\n"),
        (b"    'mission_info': 'Horizons: A852 FA. A metal-rich asteroid located in the main asteroid belt. The NASA Psyche mission will reach the asteroid in August 2029', \n    'mission_url': 'https://news.arizona.edu/news/large-craters-offer-clues-origin-asteroid-16-psyche'},\n",
         b'    \'mission_info\': "Horizons: A852 FA. A metal-rich asteroid in the main asteroid belt. NASA\'s Psyche spacecraft begins its main mission there in August 2029.", \n    \'mission_url\': \'https://science.nasa.gov/solar-system/asteroids/16-psyche/\'},\n'),
        (b"    {'name': 'Bennu', 'id': '1999 RQ36', 'var_name': 'bennu_var', 'color_key': 'Bennu', 'symbol': 'circle-open', 'object_type': 'orbital', \n",
         b"    {'name': 'Bennu', 'key': 'bennu', 'id': '1999 RQ36', 'horizons_name': '101955 Bennu', 'var_name': 'bennu_var', 'color_key': 'Bennu', 'symbol': 'circle-open', 'object_type': 'orbital', \n"),
        (b"    {'name': 'Eros', 'id': 'A898 PA', 'var_name': 'eros_var', 'color_key': 'Eros', 'symbol': 'circle-open', 'object_type': 'orbital', \n",
         b"    {'name': 'Eros', 'key': 'eros', 'id': 'A898 PA', 'horizons_name': '433 Eros', 'var_name': 'eros_var', 'color_key': 'Eros', 'symbol': 'circle-open', 'object_type': 'orbital', \n"),
        (b"    {'name': 'Dinkinesh', 'id': '1999 VD57', 'var_name': 'dinkinesh_var', 'color_key': 'Dinkinesh', 'symbol': 'circle-open', 'object_type': 'orbital', \n",
         b"    {'name': 'Dinkinesh', 'key': 'dinkinesh', 'id': '1999 VD57', 'horizons_name': '152830 Dinkinesh', 'var_name': 'dinkinesh_var', 'color_key': 'Dinkinesh', 'symbol': 'circle-open', 'object_type': 'orbital', \n"),
        (b"    {'name': 'Itokawa', 'id': '1998 SF36', 'var_name': 'itokawa_var', 'color_key': 'Itokawa', 'symbol': 'circle-open', 'object_type': 'orbital', \n",
         b"    {'name': 'Itokawa', 'key': 'itokawa', 'id': '1998 SF36', 'horizons_name': '25143 Itokawa', 'var_name': 'itokawa_var', 'color_key': 'Itokawa', 'symbol': 'circle-open', 'object_type': 'orbital', \n"),
        (b"    'mission_url': 'https://en.wikipedia.org/wiki/25143_Itokawa'},\n",
         b"    'mission_url': 'https://science.nasa.gov/solar-system/asteroids/25143-itokawa/'},\n"),
        (b"    {'name': 'Lutetia', 'id': 'A852 VA', 'var_name': 'lutetia_var', 'color_key': 'Lutetia', 'symbol': 'circle-open', 'object_type': 'orbital', \n",
         b"    {'name': 'Lutetia', 'key': 'lutetia', 'id': 'A852 VA', 'horizons_name': '21 Lutetia', 'var_name': 'lutetia_var', 'color_key': 'Lutetia', 'symbol': 'circle-open', 'object_type': 'orbital', \n"),
        (b"    {'name': 'Ryugu', 'id': '1999 JU3', 'var_name': 'ryugu_var', 'color_key': 'Ryugu', 'symbol': 'circle-open', 'object_type': 'orbital', \n",
         b"    {'name': 'Ryugu', 'key': 'ryugu', 'id': '1999 JU3', 'horizons_name': '162173 Ryugu', 'var_name': 'ryugu_var', 'color_key': 'Ryugu', 'symbol': 'circle-open', 'object_type': 'orbital', \n"),
        (b"    {'name': 'Steins', 'id': '1969 VC', 'var_name': 'steins_var', 'color_key': 'Steins', 'symbol': 'circle-open', 'object_type': 'orbital', \n",
         b"    {'name': 'Steins', 'key': 'steins', 'id': '1969 VC', 'horizons_name': '2867 Steins', 'var_name': 'steins_var', 'color_key': 'Steins', 'symbol': 'circle-open', 'object_type': 'orbital', \n"),
        (b"     'mission_url': 'https://www.esa.int/Science_Exploration/Space_Science/Rosetta'},\n",
         b"     'mission_url': 'https://en.wikipedia.org/wiki/2867_%C5%A0teins'},\n"),
        (b"    {'name': 'Donaldjohanson', 'id': '1981 EQ5', 'var_name': 'donaldjohanson_var', 'color_key': 'Donaldjohanson', 'symbol': 'circle-open', 'object_type': 'orbital', \n",
         b"    {'name': 'Donaldjohanson', 'key': 'donaldjohanson', 'id': '1981 EQ5', 'horizons_name': '52246 Donaldjohanson', 'var_name': 'donaldjohanson_var', 'color_key': 'Donaldjohanson', 'symbol': 'circle-open', 'object_type': 'orbital', \n"),
        (b'     \'mission_info\': \'Lucy flyby: Apr 20, 2025. D~4 km, C-type. Named for paleoanthropologist who discovered "Lucy" fossil.\', \n',
         b'     \'mission_info\': \'Lucy flew past it on April 20, 2025. It is about 8 km long and 3.5 km wide, a C-type (carbon-rich) asteroid, named for the paleoanthropologist who discovered the "Lucy" fossil.\', \n'),
        (b"    {'name': 'Vesta', 'id': 'A807 FA', 'var_name': 'vesta_var', 'color_key': 'Vesta', 'symbol': 'circle-open', 'object_type': 'orbital', \n",
         b"    {'name': 'Vesta', 'key': 'vesta', 'id': 'A807 FA', 'horizons_name': '4 Vesta', 'var_name': 'vesta_var', 'color_key': 'Vesta', 'symbol': 'circle-open', 'object_type': 'orbital', \n"),
        (b"    'mission_url': 'https://dawn.jpl.nasa.gov/'},\n",
         b"    'mission_url': 'https://science.nasa.gov/solar-system/asteroids/4-vesta/'},\n"),
        (b"    {'name': 'Arrokoth', 'id': '2014 MU69', 'var_name': 'arrokoth_var', 'color_key': 'Arrokoth', 'symbol': 'circle-open', 'object_type': 'orbital', \n",
         b"    {'name': 'Arrokoth', 'key': 'arrokoth', 'id': '2014 MU69', 'horizons_name': '486958 Arrokoth', 'var_name': 'arrokoth_var', 'color_key': 'Arrokoth', 'symbol': 'circle-open', 'object_type': 'orbital', \n"),
        (b"    'mission_url': 'https://science.nasa.gov/resource/arrokoth-2014-mu69-in-3d/'},\n",
         b"    'mission_url': 'https://en.wikipedia.org/wiki/486958_Arrokoth'},\n"),
        (b"    {'name': 'Ixion', 'id': '2001 KX76', 'var_name': 'ixion_var', 'color_key': 'Ixion', 'symbol': 'circle-open', 'object_type': 'orbital', \n",
         b"    {'name': 'Ixion', 'key': 'ixion', 'id': '2001 KX76', 'horizons_name': '28978 Ixion', 'var_name': 'ixion_var', 'color_key': 'Ixion', 'symbol': 'circle-open', 'object_type': 'orbital', \n"),
        (b"    {'name': 'GV9', 'id': '2004 GV9', 'var_name': 'gv9_var', 'color_key': 'GV9', 'symbol': 'circle-open', 'object_type': 'orbital', \n",
         b"    {'name': 'GV9', 'key': 'goibniu', 'id': '2004 GV9', 'horizons_name': '90568 Goibniu', 'var_name': 'gv9_var', 'color_key': 'GV9', 'symbol': 'circle-open', 'object_type': 'orbital', \n"),
        (b"    'mission_url': 'https://en.wikipedia.org/wiki/(90568)_2004_GV9'},\n",
         b"    'mission_url': 'https://en.wikipedia.org/wiki/90568_Goibniu'},\n"),
        (b"    {'name': 'Varuna', 'id': '2000 WR106', 'var_name': 'varuna_var', 'color_key': 'Varuna', 'symbol': 'circle-open', 'object_type': 'orbital', \n",
         b"    {'name': 'Varuna', 'key': 'varuna', 'id': '2000 WR106', 'horizons_name': '20000 Varuna', 'var_name': 'varuna_var', 'color_key': 'Varuna', 'symbol': 'circle-open', 'object_type': 'orbital', \n"),
        (b"    {'name': 'Ammonite', 'id': '2023 KQ14', 'var_name': 'ammonite_var', 'color_key': 'Ammonite', 'symbol': 'circle-open', 'object_type': 'orbital', \n",
         b"    {'name': 'Ammonite', 'key': 'ammonite', 'id': '2023 KQ14', 'horizons_name': '(2023 KQ14)', 'var_name': 'ammonite_var', 'color_key': 'Ammonite', 'symbol': 'circle-open', 'object_type': 'orbital', \n"),
        (b"    {'name': 'Tempel 2', 'id': '90000214', 'var_name': 'comet_tempel2_var', 'color_key': 'Tempel 2', 'symbol': 'diamond',\n",
         b"    {'name': 'Tempel 2', 'key': 'tempel_2', 'id': '90000214', 'horizons_name': '10P/Tempel 2', 'var_name': 'comet_tempel2_var', 'color_key': 'Tempel 2', 'symbol': 'diamond',\n"),
        (b"    # Deep Space 1 flyby in 2001.\n    # ID: Record 90000214 (2013 epoch) - most recent solution. '10P' is ambiguous (22 records).\n    'mission_info': 'Horizons: 10P. Jupiter-family comet, 5.37-year period. Discovered 1873 by Wilhelm Tempel. Deep Space 1 flyby 2001.',\n",
         b"    # Corrected 2026-10-22 (L-443): no Deep Space 1 flyby. Deep Space 1 flew\n    # past 19P/Borrelly in 2001 (NASA's Borrelly page), not 10P.\n    # ID: Record 90000214, epoch-year 2017, the newest of JPL's 22 records for\n    # 10P, read 2026-10-22 (L-443). '10P' alone is ambiguous.\n    'mission_info': 'Horizons: 10P. A Jupiter-family comet, discovered in 1873 by Wilhelm Tempel.',\n"),
        (b"    {'name': 'Schaumasse', 'id': '90000355', 'var_name': 'comet_schaumasse_var', 'color_key': 'Schaumasse', 'symbol': 'diamond',\n",
         b"    {'name': 'Schaumasse', 'key': 'schaumasse', 'id': '90000356', 'horizons_name': '24P/Schaumasse', 'var_name': 'comet_schaumasse_var', 'color_key': 'Schaumasse', 'symbol': 'diamond',\n"),
        (b"    # ID: Record 90000355 (2021 epoch) - most recent solution. '24P' is ambiguous (12 records).\n    'mission_info': 'Horizons: 24P. Jupiter-family comet, 8.25-year period. Discovered 1911. Perihelion Jan 8, 2026 at 1.18 AU.',\n",
         b"    # ID: Record 90000356, epoch-year 2024, the newest of JPL's 12 records for\n    # 24P, read 2026-10-22 (L-443; 90000355, epoch-year 2015, until then).\n    # '24P' alone is ambiguous.\n    'mission_info': 'Horizons: 24P. A Jupiter-family comet, discovered in 1911.',\n"),
        (b"    {'name': 'Howell', 'id': '90000897', 'var_name': 'comet_howell_var', 'color_key': 'Howell', 'symbol': 'diamond',\n",
         b"    {'name': 'Howell', 'key': 'howell', 'id': '90000901', 'horizons_name': '88P/Howell', 'var_name': 'comet_howell_var', 'color_key': 'Howell', 'symbol': 'diamond',\n"),
        (b"    # ID: Record 90000897 (2019 epoch) - most recent solution. '88P' is ambiguous (9 records).\n    'mission_info': 'Horizons: 88P. Jupiter-family comet, 5.5-year period. Discovered 1981 by Ellen Howell. Perihelion Mar 18, 2026.',\n",
         b"    # ID: Record 90000901, epoch-year 2021, the newest of JPL's 9 records for\n    # 88P, read 2026-10-22 (L-443; 90000897, epoch-year 1997, until then).\n    # '88P' alone is ambiguous.\n    'mission_info': 'Horizons: 88P. A Jupiter-family comet, discovered in 1981 by Ellen Howell.',\n"),
        (b"    {'name': 'Churyumov', 'id': '90000699', 'var_name': 'comet_Churyumov_Gerasimenko_var', 'color_key': 'Churyumov', # 67P/Churyumov-Gerasimenko\n",
         b"    {'name': 'Churyumov', 'key': 'churyumov', 'id': '90000703', 'horizons_name': '67P/Churyumov-Gerasimenko', 'var_name': 'comet_Churyumov_Gerasimenko_var', 'color_key': 'Churyumov', # 67P/Churyumov-Gerasimenko\n"),
        (b"    # data arc: 2008-06-01 to 2023-04-26; Epoch: 2015-Oct-10; 67P; previously rec 90000704; record number needed to fetch Horizons data.\n    'mission_info': 'Horizons: 67P. 67P/Churyumov-Gerasimenko is the comet visited by the Rosetta spacecraft, August 2014 through September 2016.', \n",
         b"    # data arc: 2008-06-01 to 2023-04-26; Epoch: 2015-Oct-10; 67P; previously rec 90000704; record number needed to fetch Horizons data.\n    # ID: Record 90000703, epoch-year 2015 (the Rosetta visit), the newest of\n    # JPL's 9 records for 67P, read 2026-10-22 (L-443; 90000699, epoch-year\n    # 1995, with no covariance, until then).\n    'mission_info': 'Horizons: 67P. 67P/Churyumov-Gerasimenko is the comet visited by the Rosetta spacecraft, August 2014 through September 2016.', \n"),
        (b"    {'name': 'Hale-Bopp', 'id': 'C/1995 O1', 'var_name': 'comet_hale_bopp_var', 'color_key': 'Hale-Bopp', 'symbol': 'diamond', \n",
         b"    {'name': 'Hale-Bopp', 'key': 'hale_bopp', 'id': 'C/1995 O1', 'horizons_name': 'Hale-Bopp (C/1995 O1)', 'var_name': 'comet_hale_bopp_var', 'color_key': 'Hale-Bopp', 'symbol': 'diamond', \n"),
        (b"    {'name': 'Hyakutake', 'id': 'C/1996 B2', 'var_name': 'comet_hyakutake_var', 'color_key': 'Hyakutake', 'symbol': 'diamond', \n",
         b"    {'name': 'Hyakutake', 'key': 'hyakutake', 'id': 'C/1996 B2', 'horizons_name': 'Hyakutake (C/1996 B2)', 'var_name': 'comet_hyakutake_var', 'color_key': 'Hyakutake', 'symbol': 'diamond', \n"),
        (b"    'mission_info': 'Horizons: C/1996 B2. Retrograde. Passed very close to Earth in 1996. Retrograde (left-handed) orbit.', \n    'mission_url': 'https://science.nasa.gov/mission/ulysses/'},\n",
         b"    'mission_info': 'Horizons: C/1996 B2. Passed very close to Earth in 1996. It goes around the Sun in the opposite direction to the planets.', \n    'mission_url': 'https://nssdc.gsfc.nasa.gov/planetary/hyakutake.html'},\n"),
        (b"    {'name': 'Lemmon', 'id': 'C/2025 A6', 'var_name': 'comet_lemmon_var', 'color_key': 'Lemmon', 'symbol': 'diamond', \n",
         b"    {'name': 'Lemmon', 'key': 'lemmon', 'id': 'C/2025 A6', 'horizons_name': 'Lemmon (C/2025 A6)', 'var_name': 'comet_lemmon_var', 'color_key': 'Lemmon', 'symbol': 'diamond', \n"),
        (b"    'mission_info': 'Horizons: C/2025 A6. Retrograde. In Fall 2025, Comet Lemmon is brightening and moving into morning northern skies.', \n",
         b"    'mission_info': 'Horizons: C/2025 A6. In fall 2025 it brightened in the morning northern sky. It goes around the Sun in the opposite direction to the planets.', \n"),
        (b"    {'name': 'Ikeya-Seki', 'id': 'C/1965 S1-A', 'var_name': 'comet_ikeya_seki_var', 'color_key': 'Ikeya-Seki', 'symbol': 'diamond', \n",
         b"    {'name': 'Ikeya-Seki', 'key': 'ikeya_seki', 'id': 'C/1965 S1-A', 'horizons_name': 'Ikeya-Seki (C/1965 S1-A)', 'var_name': 'comet_ikeya_seki_var', 'color_key': 'Ikeya-Seki', 'symbol': 'diamond', \n"),
        (b"    'mission_info': 'Horizons: C/1965 S1-A. Retrograde. One of the brightest comets of the 20th century. Retrograde (left-handed) orbit.', \n    'mission_url': 'https://sites.google.com/view/tony-quintanilla/comets/ikeya-seki-1965'},\n",
         b"    'mission_info': 'Horizons: C/1965 S1-A. One of the brightest comets seen in the last thousand years. It goes around the Sun in the opposite direction to the planets.', \n    'mission_url': 'https://en.wikipedia.org/wiki/Comet_Ikeya%E2%80%93Seki'},\n"),
        (b"    {'name': 'NEOWISE', 'id': 'C/2020 F3', 'var_name': 'comet_neowise_var', 'color_key': 'NEOWISE', 'symbol': 'diamond', # C/2020 F3\n",
         b"    {'name': 'NEOWISE', 'key': 'neowise', 'id': 'C/2020 F3', 'horizons_name': 'NEOWISE (C/2020 F3)', 'var_name': 'comet_neowise_var', 'color_key': 'NEOWISE', 'symbol': 'diamond', # C/2020 F3\n"),
        (b"    'mission_info': 'Horizons: C/2020 F3. Retrograde. Brightest comet visible from the Northern Hemisphere in decades. Retrograde (left-handed) orbit.', \n    'mission_url': 'https://www.nasa.gov/missions/neowise/nasas-neowise-celebrates-10-years-plans-end-of-mission/'},\n",
         b"    'mission_info': 'Horizons: C/2020 F3. The brightest comet seen from the Northern Hemisphere since Hale-Bopp in 1997. It goes around the Sun in the opposite direction to the planets.', \n    'mission_url': 'https://www.nasa.gov/centers-and-facilities/jpl/comet-neowise-sizzles-as-it-slides-by-the-sun-providing-a-treat-for-observers/'},\n"),
        (b"    {'name': 'SWAN', 'id': 'C/2025 R2', 'var_name': 'comet_c2025r2_var', 'color_key': 'SWAN', 'symbol': 'diamond', \n",
         b"    {'name': 'SWAN', 'key': 'swan', 'id': 'C/2025 R2', 'horizons_name': 'SWAN (C/2025 R2)', 'var_name': 'comet_c2025r2_var', 'color_key': 'SWAN', 'symbol': 'diamond', \n"),
        (b"    'mission_info': 'Horizons: C/2025 R2 (SWAN). This is a non-periodic comet that was discovered on September 11, 2025.', \n",
         b"    'mission_info': 'Horizons: C/2025 R2 (SWAN). A long-period comet, discovered on September 11, 2025.', \n"),
        (b"    {'name': 'MAPS', 'id': 'C/2026 A1', 'var_name': 'comet_c2026a1_var', 'color_key': 'MAPS', 'symbol': 'diamond',    # C/2026 A1 in Horizons\n",
         b"    {'name': 'MAPS', 'key': 'maps', 'id': 'C/2026 A1', 'horizons_name': 'MAPS (C/2026 A1)', 'var_name': 'comet_c2026a1_var', 'color_key': 'MAPS', 'symbol': 'diamond',    # C/2026 A1 in Horizons\n"),
    ]},
    {"path": 'export_objects.py', "kind": "edit", "guard": 'md5', "md5": '347e4fc7b48a4e29343897c98c958699', "edits": [
        (b"                      horizons_id  the entry's 'id'\n",
         b"                      horizons_id  the entry's 'id', or its 'helio_id'\n                                   where it has one: the record the\n                                   orrery plots a body by when the Sun\n                                   is the centre, which the Sun-centred\n                                   rooms serve (L-443)\n"),
        (b"                      id_type      the entry's 'id_type', or null where\n",
         b"                      id_type      the entry's 'id_type' ('helio_id_type',\n                                   else 'smallbody', for a helio_id), or\n                                   null where\n"),
        (b'elements; a record with no target and no horizons_id is refused.)\n"""\n',
         b'elements; a record with no target and no horizons_id is refused.)\nModule updated: October 22, 2026 with Anthropic\'s Claude Opus 5.5 (L-443,\nslice 1: a keyed entry with a \'helio_id\' is served by it, as a small\nbody, through served_identity, so the Sun-centred rooms take the record\nthe orrery plots a body by around the Sun. No keyed entry had one\nbefore.)\n"""\n'),
        (b'          "horizons_name", "object_type")\n',
         b'          "horizons_name", "object_type", "helio_id", "helio_id_type")\n\n\ndef served_identity(f):\n    """(horizons_id, id_type) the website serves for an entry\'s fields:\n    its \'helio_id\' where it has one, as a small-body designation\n    (\'helio_id_type\', else \'smallbody\', the type plotting gives a\n    helio_id), else its \'id\' and \'id_type\'. The rooms are Sun-centred,\n    and a helio_id is the record the orrery itself plots a body by when\n    the Sun is the centre (L-443, Tony\'s ruling of 2026-10-22: a small\n    body is served by its helio_id). period_fetch.py asks the period of\n    the same record, so the period and the identity describe one body."""\n    helio = f.get("helio_id")\n    if helio is not None:\n        return str(helio), f.get("helio_id_type") or "smallbody"\n    hid = f.get("id")\n    return (None if hid is None else str(hid)), f.get("id_type")\n'),
        (b'                              "after the opening is removed" % key)\n        objects[key] = {\n',
         b'                              "after the opening is removed" % key)\n        served_id, served_type = served_identity(f)\n        objects[key] = {\n'),
        (b'            "horizons_id": None if f.get("id") is None else str(f["id"]),\n',
         b'            "horizons_id": served_id,\n'),
        (b'            "id_type": f.get("id_type"),\n',
         b'            "id_type": served_type,\n'),
    ]},
    {"path": 'period_fetch.py', "kind": "edit", "guard": 'md5', "md5": '6fa7b86ab78a329acedd35962f483a11', "edits": [
        (b'    None, as for the planets), no centre override. So a period fetched\n',
         b"    None, as for the planets), or its 'helio_id' as a small body where it\n    has one (L-443), no centre override. So a period fetched\n"),
        (b'now names is missing too, named with the reason, and the read-back\nrequires the new target.)\n"""\n\n',
         b'now names is missing too, named with the reason, and the read-back\nrequires the new target.)\nModule updated: October 22, 2026 with Anthropic\'s Claude Opus 5.5 (L-443:\nan entry with a helio_id is fetched by it, as a small body, as plotting\'s\npre-fetch now does around the Sun and as the export serves it.)\n"""\n\n'),
        (b'READ_FIELDS = ("name", "key", "id", "id_type", "object_type", "is_mission")\n',
         b'READ_FIELDS = ("name", "key", "id", "id_type", "object_type", "is_mission",\n               "helio_id", "helio_id_type")\n'),
        (b'        name = fields.get("name")\n        out.append({\n',
         b'        name = fields.get("name")\n        # palomas_orrery.py: obj_dict.get(\'id\', obj_name) and\n        # obj_dict.get(\'id_type\', \'smallbody\'); around the Sun, the\n        # helio_id where the entry has one, as a small body (L-443), the\n        # record the export serves (export_objects.served_identity)\n        horizons_id = str(fields.get("id", name))\n        id_type = fields.get("id_type", "smallbody")\n        if fields.get("helio_id") is not None:\n            horizons_id = str(fields["helio_id"])\n            id_type = fields.get("helio_id_type") or "smallbody"\n        out.append({\n'),
        (b'            # palomas_orrery.py: obj_dict.get(\'id\', obj_name) and\n            # obj_dict.get(\'id_type\', \'smallbody\')\n            "horizons_id": str(fields.get("id", name)),\n            "id_type": fields.get("id_type", "smallbody"),\n',
         b'            "horizons_id": horizons_id,\n            "id_type": id_type,\n'),
    ]},
    {"path": 'palomas_orrery.py', "kind": "edit", "guard": 'md5', "md5": 'e47dd41399992364f4b35ea6d427f494', "edits": [
        (b"Outer Oort Cloud, are gone, Tony's ruling of this day.)\n\n",
         b"Outer Oort Cloud, are gone, Tony's ruling of this day.)\nModule updated: October 22, 2026 with Anthropic's Claude Opus 5.5 (L-443:\nthe elements pre-fetch, static and animated, asks a body's elements of\nits helio_id when the Sun is the centre, as the position fetch already\ndid, so a body's orbit and marker come from one record, the one the\nwebsite serves.)\n\n"),
        (b"                    horizons_id = obj_dict.get('id', obj_name)\n                    id_type = obj_dict.get('id_type', 'smallbody')\n                    \n                    # Determine if this object needs barycentric elements\n",
         b"                    horizons_id = obj_dict.get('id', obj_name)\n                    id_type = obj_dict.get('id_type', 'smallbody')\n                    # FIXED 2026-10-22 (L-443): around the Sun, a body's\n                    # elements are asked of its helio_id, as this file's\n                    # position fetch already asks its position. Until now\n                    # the orbit came from the body's own centre and the\n                    # marker from its helio_id; the website serves the\n                    # helio_id record, so both instruments agree.\n                    if center_object_name == 'Sun' and 'helio_id' in obj_dict:\n                        horizons_id = obj_dict['helio_id']\n                        id_type = obj_dict.get('helio_id_type') or 'smallbody'\n                    \n                    # Determine if this object needs barycentric elements\n"),
        (b'                    horizons_id = obj_dict.get(\'id\', obj_name)\n                    id_type = obj_dict.get(\'id_type\', \'smallbody\')\n                    \n                    print(f"[ANIMATION PRE-FETCH] Using Horizons ID: {horizons_id} (type: {id_type})", flush=True)\n',
         b'                    horizons_id = obj_dict.get(\'id\', obj_name)\n                    id_type = obj_dict.get(\'id_type\', \'smallbody\')\n                    # FIXED 2026-10-22 (L-443): around the Sun, a body\'s\n                    # elements are asked of its helio_id, as this file\'s\n                    # position fetch already asks its position. Until now\n                    # the orbit came from the body\'s own centre and the\n                    # marker from its helio_id; the website serves the\n                    # helio_id record, so both instruments agree.\n                    if center_object_name == \'Sun\' and \'helio_id\' in obj_dict:\n                        horizons_id = obj_dict[\'helio_id\']\n                        id_type = obj_dict.get(\'helio_id_type\') or \'smallbody\'\n                    \n                    print(f"[ANIMATION PRE-FETCH] Using Horizons ID: {horizons_id} (type: {id_type})", flush=True)\n'),
    ]},
    {"path": 'test_objects_export.py', "kind": "edit", "guard": 'md5', "md5": '21d1b9d5dedc5ab4add41cf7621a129b', "edits": [
        (b'                            "for the wrong reason: %s" % exc)\n\n',
         b'                            "for the wrong reason: %s" % exc)\n\n    # L-443: an entry with a helio_id is served by it, as a small body.\n    helio = good.replace(" \'horizons_name\': \'Mars\',",\n                         " \'horizons_name\': \'Mars\', \'helio_id\': \'A123 BC\',")\n    served = ex.build_export(helio)["objects"]["mars"]\n    if (served["horizons_id"], served["id_type"]) != ("A123 BC", "smallbody"):\n        problems.append("an entry with a helio_id was not served by it, as a "\n                        "small body: %r" % ((served["horizons_id"],\n                                             served["id_type"]),))\n    if (export["objects"]["mars"]["horizons_id"] != "499"):\n        problems.append("an entry with no helio_id was not served by its id")\n\n'),
    ]},
    {"path": 'test_period_fetch.py', "kind": "edit", "guard": 'md5', "md5": '8ddd14b7a0ca3976f4ddd1760712a462', "edits": [
        (b'     \'"id_type": fields.get("id_type", "smallbody"),\',\n     \'"id_type": fields.get("id_type"),\', "args"),\n',
         b'     \'id_type = fields.get("id_type", "smallbody")\\n\',\n     \'id_type = fields.get("id_type")\\n\', "args"),\n'),
    ]},
]


def fail(msg):
    print("FAILURE: " + msg)
    print("NOTHING was written. Undo is Discard Changes in GitHub Desktop.")
    sys.exit(1)


def main():
    root = os.getcwd()
    plan = []
    for f in FILES:
        path = os.path.join(root, f["path"])
        if f["kind"] == "new":
            if os.path.exists(path):
                fail("%s already exists; this patch writes it new" % f["path"])
            plan.append((f, path, None, False))
            continue
        if not os.path.exists(path):
            fail("%s not found. Run this from the repository's root folder" % f["path"])
        raw = open(path, "rb").read()
        crlf = b"\r\n" in raw
        lf = raw.replace(b"\r\n", b"\n")
        if f["guard"] == "md5" and hashlib.md5(lf).hexdigest() != f["md5"]:
            fail("%s is not the file this patch was built against "
                 "(content fingerprint differs)" % f["path"])
        spots = []
        for k, (old, new) in enumerate(f["edits"]):
            n = lf.count(old)
            if n != 1:
                fail("ANCHOR FAIL in %s, edit %d: expected 1 match, found %d: %r"
                     % (f["path"], k + 1, n, old[:70]))
            spots.append((lf.index(old), old, new))
        spots.sort()
        out, last = b"", 0
        for i, old, new in spots:
            if i < last:
                fail("%s: two edits overlap" % f["path"])
            out += lf[last:i] + new
            last = i + len(old)
        out += lf[last:]
        plan.append((f, path, out, crlf))
    for f, path, out, crlf in plan:
        if f["kind"] == "new":
            os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
            open(path, "wb").write(f["content"])
            print("ok  %s (new, %d bytes)" % (f["path"], len(f["content"])))
        else:
            open(path, "wb").write(out)
            print("ok  %s (%d edits%s)" % (f["path"], len(f["edits"]),
                                        "; it was CRLF in the working copy, written LF" if crlf else ""))
    print("patch applied: %s (%d files)" % (TITLE, len(plan)))


if __name__ == "__main__":
    main()
