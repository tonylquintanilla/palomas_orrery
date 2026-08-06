# -*- coding: utf-8 -*-
"""patch_ledger.py -- add L-182 (Mars Hill) and L-183 (stars skill); L-178 -> PENDING-GATE

Built on 339897000b63fa768ccb9b556dd432bac4f9d4eb
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

HOW TO RUN
    Save this file in the REPO ROOT (the folder with LEDGER_CONSOLIDATED.md), open it in VS Code, and click Run.

    All anchors are verified before anything is written; on failure
    nothing is touched.

AFTER RUNNING: run ledger_index.py to regenerate the index tables.
    Never hand-edit the INDEX zone.
"""

import os
import sys

EDITS = [
    ('LEDGER_CONSOLIDATED.md', 'LED-2', 'insert L-182 and L-183 blocks',
     b'## PENDING ACTION (Tony-side)',
     b'#### [L-182] Mars Hill sphere \xe2\x80\x94 cross-check correction lost across the config pipeline\n<!-- L:182 status:PENDING-GATE upd:2026-08-05 section:A flag: rice:3/4/100/1 -->\n- The Aug-1 Mars cross-check found `324.5 R_Mars` unsourceable and derived\n  ~1.084 Mkm (worksheet D2: "no page publishing a Mars Hill radius of 324.5\n  R_Mars"). `patch_mars_cross_check.py` corrected 5 sites but targeted\n  `mars_visualization_shells.py` ONLY \xe2\x80\x94 the correction never reached\n  `shell_configs.py`, so the live render kept 324.5 the whole time.\n- The Aug-4 Fable shell audit saw module=320 vs config=324.5 and read the\n  config as authoritative; the geometry prompt encoded that ("live config\n  already says 324.5"); the Aug-4 geometry patch then harmonized the module\n  UP to 324.5, erasing the last copies of the corrected value. Net effect:\n  the correction was removed from the codebase entirely, and the render was\n  never right at any commit.\n- At the pre-fix HEAD the module carried a two-leg `# Cross-checked:`\n  citation asserting ~320 R_Mars three lines above display text asserting\n  324.5 \xe2\x80\x94 a SOURCE_VS_VALUE contradiction created by the harmonization.\n- Resolved value: **319.2 R_Mars** = 1,084,000 km / 3,396.2 km equatorial\n  (Archinal et al. 2018, the project\'s `CENTER_BODY_RADII[\'Mars\']`). The\n  worksheet\'s 319.8 is the same 1.084 Mkm over the volumetric mean radius\n  3,389.5 km; this project uses equatorial where oblateness matters.\n- Class: a Check All Parallel Pipelines failure (resident CRITICAL gate),\n  not a value error. Both patches touched one side of a two-copy pair \xe2\x80\x94 the\n  first fixed the module and missed the config, the second aligned the\n  module to the config that had never been fixed.\n**Note:** Surfaced by the Fable skills-layer review, which flagged the\nprovenance-discipline worksheet example ("Hill sphere 324.5 should have\nbeen 320") as contradicting orrery-coding-conventions. Fable rated it HIGH\nand diagnosed it as a pending perihelion-vs-semi-major convention question;\nthe worksheet showed the opposite \xe2\x80\x94 a settled correction silently reverted.\nThe audit found the right contradiction from the skills alone and could not\nresolve its direction, because the cross-check worksheets were not in the\naudit prompt\'s Materials list. Include them next time.\n**Note:** Prevention candidates for Tony to weigh \xe2\x80\x94 (a) a cross-check patch\nmust enumerate every consumer of a corrected value before delivery, the way\nthe geometry follow-up now does; (b) a harmonize step must state WHICH copy\nis authoritative and cite the worksheet that makes it so, rather than\ninferring authority from which copy happens to be live.\n- Tony-action (do): run `patch_mars_hill_correction.py` and\n  `patch_shell_configs_mars_hill.py`, then push and record the SHA here.\n**Gap:** Patches built and smoke-tested (render moves 1,102,067 km ->\n1,084,067 km). Awaiting Tony\'s run and push; close on SHA record.\n**Ref:** worksheet_claude_mars_visualization.md D2;\ndocumentation/patch_mars_cross_check.py (module-only target);\npatch_mars_dead_copies.py (the reverting patch);\nFABLE_skills_layer_review_report.md Job 2 #8 / Job 3 #1; L-181.\n\n#### [L-183] Stars / stellar neighbourhood skill (coverage gap)\n<!-- L:183 status:OPEN upd:2026-08-05 section:A flag: rice:4/3/70/4 -->\n- Fable skills-layer review, Job 1 #1: the largest uncovered domain in the\n  project. ~22-24 modules with no owning skill \xe2\x80\x94 the acquisition ->\n  processing -> visualization chain for the stellar neighbourhood.\n- Scope as assessed: Gaia/Hipparcos catalog fetch and VOTable caching\n  (`data_acquisition*`, `data_processing`, `vot_cache_manager`), SIMBAD\n  query discipline (`simbad_manager`), the paired dual-mode pattern\n  (`hr_diagram_apparent_magnitude`/`_distance`,\n  `planetarium_apparent_magnitude`/`_distance` \xe2\x80\x94 one physics, two selection\n  modes), stellar parameter estimation and its hand-patch layer\n  (`stellar_parameters`, `stellar_data_patches`), Messier handling\n  (`messier_catalog`, `messier_object_data_handler`), exoplanet modules,\n  `star_notes`, `star_properties`, `star_sphere_builder`,\n  `star_visualization_gui`, `catalog_selection`, `sgr_a_star_data`.\n- The project already recognises the domain twice: provenance-discipline\n  defines a `stars` report domain, and a scanner-hardening episode exposed\n  a Tier-1 in `star_notes.py`. The existence of a hand-patch module\n  (`stellar_data_patches`) is itself an earned lesson with no written home.\n**Note:** Two scope decisions ride with the cut, and the new skill\'s\nfrontmatter is where they get settled: where `sgr_a_*` belongs (6 modules,\ncurrently classified `orrery`), and where the shared\n`visualization_2d/3d/core/utils` modules belong. The prompt\'s seed list and\nthe scanner\'s MODULE_DOMAIN_MAP disagree at exactly those edges.\n**Note:** Trigger cleanup travels with it \xe2\x80\x94 orrery-coding-conventions\'\ndescription names `star_visualization_gui` but the skill holds no\nstar-specific content, so a star-GUI session loads 343 lines and finds\nnothing for it while believing it fired the right skill (Fable Job 3 #4).\nMove the filename into the new skill\'s description when it lands.\n**Note:** Also noted by Fable: 19 root modules are unmapped in\nMODULE_DOMAIN_MAP and default to `orrery`, and 2 map entries point at files\nno longer in the root (`smoke_dipole_cone`, `smoke_rotation_axis`) \xe2\x80\x94 a\nsmall scanner-side cleanup that pairs naturally with this work.\n- Tony-action (decide): approve the scope boundary before the cut.\n**Gap:** Own design session. Not a bolt-on; the domain has its own\nacquisition and caching discipline.\n**Ref:** FABLE_skills_layer_review_report.md Job 1 #1, Job 3 #4.\n\n## PENDING ACTION (Tony-side)'),
    ('LEDGER_CONSOLIDATED.md', 'LED-1', 'L-178 -> PENDING-GATE + resolution note',
     b'<!-- L:178 status:OPEN upd:2026-08-04 section:A flag: rice:3/3/40/2 -->\n- Fable findings #33-36. `earth_visualization_shells.py` defines\n  `EARTH_RADIUS_KM = 6371.0` twice (lines 907, 1019). This is the mean\n  radius; constants_new.py has equatorial 6378.137 and polar 6356.752\n  but no mean radius. The derivation of AU_PER_KM mixes the\n  equatorial-based EARTH_RADIUS_AU with the mean 6371 denominator \xe2\x80\x94\n  a built-in ~0.11% error.\n- Also: GEO scatter comment claims "\xc2\xb10.0002 AU (~30 km at GEO)" but the\n  code computes \xc2\xb10.0002 \xc3\x97 EARTH_RADIUS_AU \xe2\x89\x88 \xc2\xb11.3 km. And GEO hover\n  text is missing the AU equivalent (standing convention gap).\n- No Shadow Constants gate (provenance-discipline v1.3) applies to the\n  local EARTH_RADIUS_KM.\n**Gap:** Add mean radius to constants_new.py or switch to equatorial.\nFix the GEO scatter comment. Add AU to GEO hover.',
     b'<!-- L:178 status:PENDING-GATE upd:2026-08-05 section:A flag: rice:3/3/40/2 -->\n- Fable findings #33-36. `earth_visualization_shells.py` defines\n  `EARTH_RADIUS_KM = 6371.0` twice (lines 907, 1019). This is the mean\n  radius; constants_new.py has equatorial 6378.137 and polar 6356.752\n  but no mean radius. The derivation of AU_PER_KM mixes the\n  equatorial-based EARTH_RADIUS_AU with the mean 6371 denominator \xe2\x80\x94\n  a built-in ~0.11% error.\n- Also: GEO scatter comment claims "\xc2\xb10.0002 AU (~30 km at GEO)" but the\n  code computes \xc2\xb10.0002 \xc3\x97 EARTH_RADIUS_AU \xe2\x89\x88 \xc2\xb11.3 km. And GEO hover\n  text is missing the AU equivalent (standing convention gap).\n- No Shadow Constants gate (provenance-discipline v1.3) applies to the\n  local EARTH_RADIUS_KM.\n**Note (2026-08-05):** Resolved without answering mean-vs-equatorial \xe2\x80\x94 the\nquestion is deleted rather than decided. Both local shadow constants are\nremoved and the conversion goes directly through `KM_PER_AU`\n(`AU_PER_KM = 1.0 / KM_PER_AU`), correct regardless of which Earth radius\nanything else uses. Note the ledger title says "shadow constants" but the\naffected code is LEO/GEO band geometry; no umbra/penumbra geometry is\ninvolved, so no physics decision was needed. Verified: GEO belt\n42,212 -> 42,165 km (target 42,164); LEO band 6578/8380 -> 6571/8371 km,\nnow matching its own declared LEO_LOW_KM / LEO_HIGH_KM constants, which it\ndid not before.\n**Note:** GEO radial scatter left unchanged at \xc2\xb10.0002 Earth radii\n(~1.3 km) \xe2\x80\x94 the comment claimed ~30 km and real station-keeping bands run\nto tens of km, so the comment was corrected to describe the code and the\nwidening flagged in-code as a Mode 5 call for Tony.\n- Tony-action (do): run `patch_earth_L178.py`, push, then close.\n**Gap:** Patch built and smoke-tested; awaiting Tony\'s run and push.\n**Ref:** FABLE_shell_consistency_audit_report.md findings #33-37;\npatch_earth_L178.py; L-182 (same session).'),
]


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    files = {}
    for rel, eid, label, old, new in EDITS:
        path = os.path.join(root, rel.replace('/', os.sep))
        if rel not in files:
            if not os.path.exists(path):
                print("ERROR: %s not found. Check where you saved this script." % rel)
                return 1
            with open(path, 'rb') as f:
                files[rel] = f.read()
            if b'\r\n' in files[rel]:
                print("ERROR: %s has CRLF line endings." % rel)
                return 1

    for rel, eid, label, old, new in EDITS:
        n = files[rel].count(old)
        if n != 1:
            print("ANCHOR FAIL: %s (%s) in %s matched %d, expected 1." % (eid, label, rel, n))
            print("             Nothing written.")
            return 1

    for rel, eid, label, old, new in EDITS:
        files[rel] = files[rel].replace(old, new, 1)
        print("ok  %-8s %s" % (eid, label))

    for rel, data in files.items():
        try:
            data.decode('utf-8')
        except UnicodeDecodeError as exc:
            print("ERROR: %s would not be valid UTF-8 (%s). Nothing written." % (rel, exc))
            return 1

    for rel, data in files.items():
        with open(os.path.join(root, rel.replace('/', os.sep)), 'wb') as f:
            f.write(data)
    print("")
    print("patch applied to %d file(s)" % len(files))
    return 0


if __name__ == '__main__':
    sys.exit(main())
