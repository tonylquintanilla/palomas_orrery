r"""patch_L443_4_period_count_20261022.py -- L-443: a period's figure count
taken from the number as printed, and the close's records that patch 3's
later copies carried.

RUN COMMAND
    python patch_L443_4_period_count_20261022.py

Save it in the ORRERY repository's root folder
(C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\),
open it in VS Code and click Run. Then move it to documentation/.

Built on orrery d91dc1d0 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).

WHY
    The website's Solar System figures check failed on 2025 PN7. Its
    period, 363.9 days, prints "1.00" years -- three figures -- but
    orbital_period.figures_by_error counted the figures before rounding
    and the export served two, so the website printed "1.0". Counted
    now from the number as printed. Only PN7's count changes.

WHAT IT CHANGES
    orbital_period.py           figures_by_error counts the printed
                                number's figures (FIXED comment, stamp)
    test_objects_export.py      PN7's case: "1.00" years at 3 figures,
                                and a count taken before rounding is
                                noticed
    LEDGER_CONSOLIDATED.md      L-443: Tony's runs read, the fix, six
                                comets' centre warning recorded; L-470:
                                6AC4721 off the website, Gonggong's
                                method and Tony's notes; L-456: the
                                papers
    documentation/WHERE_WE_ARE.md  by section: header, box, Deferred,
                                Signals, Waiting on you, details. The
                                run-record zone is not touched
    documentation/HANDOFF_L443_slice1_build_20261022.md  section 9, new;
                                after your runs; sections 5 to 7
    documentation/READING_L456_tony_20261021.md  your three notes
    skills/horizons-orbital-mechanics/SKILL.md  1.8 -> 1.9: Which
                                Record Serves a Body
    documentation/SKILL_HISTORIES.md  its 1.6 entry, moved down
    PROJECT_INSTRUCTIONS.md     v3.109 names both skill bumps; the
                                manifest's 1.9; cut from d91dc1d0
    patch_L443_3_close_20261022.py (root)  REMOVED: the copy that never
                                ran (the one that ran is in
                                documentation/). Only that exact copy
                                is removed; another stops the patch.

The records are checked only at the lines this patch edits, so notes you
have added elsewhere in them do not stop it. The two code files are
checked whole.

SUCCESS prints one "ok" line per file, then "patch applied".
FAILURE prints one FAILURE line, and NOTHING is written; undo is
Discard Changes in GitHub Desktop.

NEXT: the orrery maintenance run, commit and push; then the website's
Daily Run (HANDOFF_L443_slice1_build_20261022.md, sec. 9).

Role: devtool
Domain: dev_tools
"""

import hashlib
import os
import sys

TITLE = 'L-443 period count and records'
FILES = [
    {"path": 'orbital_period.py', "kind": "edit", "guard": 'md5', "md5": '0cdff644f3818a263ef5e4ee84aa9c40', "edits": [
        (b'elements are never drawn as this body\'s orbit.)\n"""\n',
         b'elements are never drawn as this body\'s orbit.)\nModule updated: October 22, 2026 with Anthropic\'s Claude Opus 5.5 (L-443:\nfigures_by_error() counts the figures of the number as printed, so a\nperiod just under a power of ten, which gains a digit when it rounds,\nis served with the count its print shows.)\n"""\n'),
        (b'    the leading digit\'s place down to print_place. For the website\'s\n    copy of a period, which prints a served value at its served count\n    (L-431, build 3)."""\n',
         b'    the printed number\'s leading digit\'s place down to print_place. For\n    the website\'s copy of a period, which prints a served value at its\n    served count (L-431, build 3)."""\n'),
        (b'        return 1\n    top = int(math.floor(math.log10(abs(value))))\n    return top - print_place(value, err) + 1\n',
         b'        return 1\n    # FIXED 2026-10-22 (L-443): counted from the number as printed, not\n    # before rounding. A value just under a power of ten gains a digit\n    # when it rounds: 2025 PN7\'s 0.9963 years prints "1.00", three\n    # figures, which the count before rounding called two, so the website\n    # printed "1.0". The Solar System figures check caught it.\n    shown = float(format_by_error(value, err).replace(\',\', \'\'))\n    if shown == 0:\n        return 1\n    top = int(math.floor(math.log10(abs(shown))))\n    return top - print_place(value, err) + 1\n'),
    ]},
    {"path": 'test_objects_export.py', "kind": "edit", "guard": 'md5', "md5": '68bab296186aafeff9f1b742dfd8fe95', "edits": [
        (b'      (L-445)\n    - the self-test did not produce the refusals it must\n',
         b'      (L-445)\n    - a period that rounds up to a power of ten served with the count\n      it had before rounding (L-443)\n    - the self-test did not produce the refusals it must\n'),
        (b'each refused, shown failing on a planted fault first.)\n"""\n',
         b'each refused, shown failing on a planted fault first.)\nModule updated: October 22, 2026 with Anthropic\'s Claude Opus 5.5 (L-443:\na period that rounds up to a power of ten is served with its print\'s\ncount, 2025 PN7\'s "1.00" years at 3 figures.)\n"""\n'),
        (b'                        "refused")\n    redated = json.loads(json.dumps(with_period))\n',
         b'                        "refused")\n    # L-443: a period just under a power of ten gains a digit when it\n    # rounds, and its count must be the print\'s. 2025 PN7, 2026-10-22:\n    # 363.9 days, 1.5 days of error; its years print "1.00", 3 figures.\n    yrs = ex._printed(363.9 / 365.25, 1.5 / 365.25)\n    if yrs != {"value": 1.0, "figures": 3, "text": "1.00"}:\n        problems.append("a period that rounds up to a power of ten was "\n                        "served as %r, not 1.00 at 3 figures" % (yrs,))\n    if dict(yrs, figures=2) == {"value": 1.0, "figures": 3, "text": "1.00"}:\n        problems.append("a count taken before rounding was not noticed")\n    redated = json.loads(json.dumps(with_period))\n'),
        (b'          "no target and a changed confirmation date were each refused.")\n',
         b'          "no target and a changed confirmation date were each refused; "\n          "a period that rounds up to 1.00 years is served at 3 figures, "\n          "and a count taken before rounding is noticed.")\n'),
    ]},
    {"path": 'LEDGER_CONSOLIDATED.md', "kind": "edit", "guard": 'anchors', "md5": 'bc083c94f1284c6bf6b29f0364bac4f0', "edits": [
        (b"    checkbox from the orrery.\n  - **Gonggong**: on plotting's skip list (palomas_orrery.py's\n",
         b'    checkbox from the orrery.\n    Tony, 2026-10-22: "this was the prehorizons estimate so we can drop\n    it from the website." Nothing to build: the entry has no \'key\', so\n    the export never sends it. It stays in the orrery. His run record\n    the same evening (`documentation/WHERE_WE_ARE_10-22-26_2027_run_record.md`):\n    "6AC4721 is retired. Gonggong skipped but needs discussion."\n  - **Gonggong**: on plotting\'s skip list (palomas_orrery.py\'s\n'),
        (b"**Gap:** Tony's word on 6AC4721; a plot of Gonggong around the Sun.\n",
         b'- **Tony, 2026-10-22, on testing Gonggong:** "yes but only if it accords\n  with our method or requires a method revision. and we should document\n  our method developed in this session in the skill. and i can test in\n  the orrery too." The method is horizons-orbital-mechanics 1.9, Which\n  Record Serves a Body: Gonggong is on all six of palomas_orrery.py\'s\n  skip lists, every line from 2026-02-04 (commit c60572d), with no\n  record of what failed. The test asks 2007 OR10 around the Sun and\n  920225088 around each other centre Gonggong is plotted from; if each\n  answers, one patch takes the name off every list. A skip kept for\n  some centres only would be a method revision, written into the skill\n  first.\n**Gap (replaces the one below, 2026-10-22, evening):** the Gonggong test,\nby the skill\'s method, in a session and on Tony\'s orrery.\n**Gap (superseded above):** a plot of Gonggong around\nthe Sun.\n**Gap (superseded above):** Tony\'s word on 6AC4721; a plot of Gonggong\naround the Sun.\n'),
        (b"    (1997).\n  - No GPT prompt was needed (the brief's job 3): every work that\n",
         b"    (1997).\n  - Tony, 2026-10-22: the Hipparcos volume is in `papers/`; Delsemme's\n    ADS page timed out; Maezawa et al. is paywalled. The next Sun-room\n    or Earth-room session reads the Hipparcos section from his copy.\n  - No GPT prompt was needed (the brief's job 3): every work that\n"),
        (b"**Gap (replaces the one below, 2026-10-22, evening):** Tony's runs of\n",
         b'- **2026-10-22, late evening: Tony\'s runs, read** (his run record,\n  `documentation/WHERE_WE_ARE_10-22-26_2027_run_record.md`). Patches 1 and 3 ran\n  (patch 3\'s first copy); the orrery\'s maintenance run passed 31 of 31,\n  fetched 48 periods, confirmed 63 of 63 entries with JPL, and was\n  pushed at d91dc1d0. Patch 2 ran; the Daily Run built 69 objects, the\n  swap first try, the served window 88.0 days set by Mercury, the\n  shortest of 62 bodies\' spans; no trust measurement failed.\n  - **One gate failed, and it was the orrery\'s:** Solar System figures,\n    on 2025 PN7. Its period, 363.9 days, prints "1.00" years, three\n    figures, but `orbital_period.figures_by_error` counted the figures\n    before rounding and served two, so the website printed "1.0".\n    Counted from the number as printed now\n    (`patch_L443_4_period_count_20261022.py`), with a case in\n    test_objects_export.py; only PN7\'s count changes in the export.\n    The website\'s printer was right and is unchanged.\n  - **Recorded, not chased:** six comets (halley, ikeya_seki,\n    hale_bopp, hyakutake, neowise, lemmon) carry the builder\'s warning\n    "its period is around @0, but a comet is drawn from its elements\n    around the Sun": the hover\'s period and the drawn ellipse use\n    different centres. Halley carried it since L-431 build 3; the\n    others joined with slice 1. Against L-431\'s ruling 7 (one orbit\n    for hover and drawing); for the comets\' next design look.\n  - Patch 3\'s two later copies (the 6AC4721 ruling, the papers, the\n    horizons-orbital-mechanics 1.9 method) never ran: Tony had run the\n    first. Patch 4 carries them and removes the unrun copy at the root.\n**Gap (replaces the one below, 2026-10-22, late evening):** patch 4 and\nthe orrery maintenance run, pushed; the Daily Run again and the website\npushed; Tony\'s look; then slice 2, the spacecraft and the open-path\ncomets.\n**Gap (superseded above):** Tony\'s runs of\n'),
    ]},
    {"path": 'documentation/WHERE_WE_ARE.md', "kind": "edit", "guard": 'anchors', "md5": 'a9d5d4a1ecb606483ce8282f7f0e365e', "edits": [
        (b"Last updated: October 22, 2026, evening: slice 1 of the objects\ndesigned and built, 50 bodies in folding groups.\n- Written at orrery bfb6c47 and gallery 0bb3434, with the day's patches.\n",
         b'Last updated: October 22, 2026, late evening: slice 1 in the orrery;\none fix before the website goes.\n- Written at orrery d91dc1d and gallery 0bb3434, with patch 4.\n'),
        (b"> - Slice 1 of L-443 (the objects to the website) is designed and\n>   built: 50 bodies, in six groups that fold open in the drawer.\n> - Every comet is drawn from today's orbit, Halley and Encke too.\n> - A bare interactive.html link opens the Solar System room; the\n>   Explorer has its own address.\n",
         b"> - Slice 1 of L-443 (the objects to the website) is in the orrery,\n>   pushed: 50 bodies, in six groups that fold open in the drawer.\n> - The website's check caught one wrong figure count, 2025 PN7's\n>   period; the fix is the orrery's, in patch 4.\n> - The method for choosing JPL's records is in a skill now.\n"),
        (b"> **Do next:** *run slice 1's patches and runs in order (the handoff,\n> sec. 2), then your look on the phone.*\n",
         b"> **Do next:** *patch 4, the orrery run and push, then the Daily Run\n> and the website's push (the handoff, sec. 9).*\n"),
        (b"> - *(decide) The info panel's two rewritten sentences (the handoff,\n>   sec. 3), before the website patch.*\n> - *Reinstall interactive-exhibit 1.21.*\n> - Three papers into `papers/` (`READING_L456_tony_20261021.md`).\n",
         b'> - *(do) Patch 4 and the runs, in order (the handoff, sec. 9).*\n> - *Reinstall interactive-exhibit 1.21, horizons-orbital-mechanics 1.9.*\n> - Two papers left to try (`READING_L456_tony_20261021.md`).\n'),
        (b"- L-470 (entries the website cannot serve): 6AC4721, Gonggong's\n  period; and a drawn main-belt cloud (L-443). Behind slice 2.\n",
         b'- A drawn main-belt cloud (L-443 (the objects)), behind slice 2.\n'),
        (b"- Last cache build: 20261022T200533Z, ok, the swap's second try\n  (gallery 0bb3434).\n",
         b'- Last cache build: 20261023T021052Z, ok, first try (on gallery\n  0bb3434, not yet pushed).\n'),
        (b'At the next design talk:\n- The Daily Run checking the orrery it pulled is the one you pushed\n',
         b'At the next design talk:\n- "Gonggong skipped but needs discussion" (your run record, Oct 22;\n  L-470 (entries the website cannot serve)).\n- The Daily Run checking the orrery it pulled is the one you pushed\n'),
        (b'- *Next: `HANDOFF_L443_slice1_build_20261022.md`, sec. 2.*\n',
         b'- *Next: `HANDOFF_L443_slice1_build_20261022.md`, sec. 9.*\n'),
    ]},
    {"path": 'documentation/HANDOFF_L443_slice1_build_20261022.md', "kind": "edit", "guard": 'anchors', "md5": '1a653a254ad33f8f6259c2779583a00a', "edits": [
        (b"(branch main of each). Pushed at: (Tony's pushes, after section 2).\n",
         b"(branch main of each). Pushed at: orrery d91dc1d0 (section 2's steps\n1 to 3); the website, after section 9.\n"),
        (b"6. Reinstall interactive-exhibit 1.21 (Settings > Skills), from the\n   orrery's skills/ folder.\n",
         b"6. Reinstall interactive-exhibit 1.21 and horizons-orbital-mechanics\n   1.9 (Settings > Skills), from the orrery's skills/ folder.\n"),
        (b'\n- Deep Space 1 flew past comet Borrelly in 2001, not Tempel 2: the\n',
         b'\n- This session\'s way of choosing which JPL record serves a body is now\n  in horizons-orbital-mechanics 1.9, Which Record Serves a Body, on your\n  word ("we should document our method developed in this session in the\n  skill").\n\n- Deep Space 1 flew past comet Borrelly in 2001, not Tempel 2: the\n'),
        (b'- **The obligation.** The next session confirms its loaded copy reads\n  interactive-exhibit 1.21 before exhibit work.\n',
         b'- **The obligation.** The next session confirms its loaded copies read\n  interactive-exhibit 1.21 before exhibit work and\n  horizons-orbital-mechanics 1.9 before Horizons work.\n- **The Gonggong test** (L-470), by the method now in\n  horizons-orbital-mechanics 1.9, Which Record Serves a Body: ask each\n  record the orrery would ask, around each centre; take Gonggong off\n  every skip list only if each answers. You can test it in the orrery\n  too.\n'),
        (b"- **Carried, not chased:** L-470 (6AC4721, Gonggong's period); two\n",
         b"- **Carried, not chased:** L-470 (Gonggong's period); two\n"),
        (b'- (do) Section 2, steps 1 to 5, in order.\n- (do) Reinstall interactive-exhibit 1.21 (step 6).\n',
         b'- (do) Section 2, steps 1 to 5, in order. Done to step 5; then\n  section 9, steps 1 to 4.\n- (do) Reinstall interactive-exhibit 1.21 and horizons-orbital-mechanics\n  1.9 (step 6).\n'),
        (b'- (do) Three papers into `papers/` (`READING_L456_tony_20261021.md`),\n  carried from before.\n- (decide, not urgent) 6AC4721: retire or merge it with MAPS (L-470).\n',
         b'- (do) Two papers still to try, Delsemme (timed out) and Maezawa\n  (paywalled) (`READING_L456_tony_20261021.md`). The Hipparcos volume\n  is in `papers/`.\n- Decided 2026-10-22: 6AC4721, the pre-Horizons estimate for MAPS,\n  stays off the website (L-470). Nothing to build.\n'),
        (b"\nSession written October 2026 with Anthropic's Claude Opus 5.5.\n",
         b'\n## 9. After your runs (read 2026-10-22, 21:26)\n\nRead from your run record,\n`documentation/WHERE_WE_ARE_10-22-26_2027_run_record.md`.\n\nWhat your runs showed:\n- Patch 1 and patch 3 ran (the first of patch 3\'s copies). The orrery\'s\n  maintenance run passed 31 of 31, fetched 48 periods, confirmed 63 of\n  63 entries with JPL; you pushed it at d91dc1d0.\n- Patch 2 ran. The Daily Run built 69 objects; the swap worked first\n  try; the served window is 88.0 days, set by Mercury, the shortest of\n  62 bodies\' spans. No trust measurement failed, no null window.\n- Six comets carry a warning that is not new: their period is around\n  the solar system\'s centre of mass while their orbit is drawn around\n  the Sun (Halley has said so since October 14). Recorded on L-443\n  (the objects to the website), not a stop.\n- One check failed: Solar System figures, on 2025 PN7. Its period,\n  363.9 days, prints as "1.00" years, which is three figures. The\n  orrery counted the figures before rounding and served two, so the\n  website printed "1.0". The website was right; the orrery\'s count was\n  wrong. Patch 4 fixes the count; it changes only PN7\'s in the export.\n\nPatch 3\'s two later copies never ran (you had already run the first).\nPatch 4 carries what they added -- your word on 6AC4721, the papers,\nand the method in horizons-orbital-mechanics 1.9 -- and deletes the\nunrun copy left in the orrery\'s root folder.\n\nYour notes, read: "6AC4721 is retired" is on L-470 (entries the\nwebsite cannot serve); "Gonggong skipped but needs discussion" is on\nWhere We Are\'s design-talk list. Your run record below Where We Are\'s\nmarker is left as it is: tonight\'s website steps still go there, and\nthe next session\'s close reads it.\n\nYour run order now. Don\'t commit the website\'s changes until step 3.\n\nIn the ORRERY folder:\n1. `patch_L443_4_period_count_20261022.py`, then move it to\n   documentation/.\n2. The orrery maintenance run. Expect: Objects export rewritten; the\n   Objects export check passes; the rest as before. Commit and push.\n\nIn the WEBSITE folder:\n3. The Daily Run again. Its pull brings the new export, and the mirror\n   changes 2025 PN7\'s figure count from 2 to 3. Expect the Solar\n   System figures check to pass, PN7 printing "1.00 years (364 days)".\n   Then commit, push, and the live run.\n4. Reinstall interactive-exhibit 1.21 and horizons-orbital-mechanics\n   1.9; then your look on the phone (section 2, step 7).\n\nSession written October 2026 with Anthropic\'s Claude Opus 5.5.\n'),
    ]},
    {"path": 'documentation/READING_L456_tony_20261021.md', "kind": "edit", "guard": 'anchors', "md5": '0594b3e089aac64a718102b081f4d178', "edits": [
        (b'- Your note: -- could not open, timed out\n',
         b'- Your note: -- could not open, timed out (again 2026-10-22)\n'),
        (b'- Your note: -- downloaded 500+ pages to papers/\n',
         b'- Your note: DONE 2026-10-22: the volume is in papers/.\n'),
        (b'  under average conditions.\n- Your note: -- paywalled\n\n',
         b'  under average conditions.\n- Your note: -- paywalled (2026-10-22). If the page shows the\n  abstract, pasting it works, as it did for Slavin et al.\n\n'),
    ]},
    {"path": 'skills/horizons-orbital-mechanics/SKILL.md', "kind": "edit", "guard": 'anchors', "md5": '59fbadaf746cef0f949f9b81a25ddc75', "edits": [
        (b"description: JPL Horizons API and orbital mechanics reference for the Paloma's Orrery project (astroquery Horizons queries, orbit_data_manager, osculating_cache_manager, idealized_orbits, apsidal_markers, spacecraft_encounters, close_approach_data, position_accuracy, orbital_period, period_fetch). Use for any Paloma's Orrery task involving Horizons queries or ephemerides, coordinate center bodies, reference frames, osculating elements, orbit caches, a small body's position uncertainty (VEC_TABLE 2xr), orbital periods and the centre they are taken around, the drawn orbit and its markers' dates, encounter or flyby resolution, or whenever a rendered orbit looks wrong or an ephemeris API returns empty. Do not use for projects other than Paloma's Orrery.\nfires_when: Horizons queries, centers, frames, osculating elements, encounters, comet record pinning, 2xr uncertainties, periods, the drawn orbit's centre, the Horizons check (horizons_check.py, its period comparison and the data sheets' re-read), the period fetch before it (period_fetch.py)\n",
         b"description: JPL Horizons API and orbital mechanics reference for the Paloma's Orrery project (astroquery Horizons queries, orbit_data_manager, osculating_cache_manager, idealized_orbits, apsidal_markers, spacecraft_encounters, close_approach_data, position_accuracy, orbital_period, period_fetch). Use for any Paloma's Orrery task involving Horizons queries or ephemerides, coordinate center bodies, reference frames, osculating elements, orbit caches, a small body's position uncertainty (VEC_TABLE 2xr), orbital periods and the centre they are taken around, the drawn orbit and its markers' dates, which Horizons record serves a body (helio_id, a pinned comet record, a skip list), encounter or flyby resolution, or whenever a rendered orbit looks wrong or an ephemeris API returns empty. Do not use for projects other than Paloma's Orrery.\nfires_when: Horizons queries, centers, frames, osculating elements, encounters, comet record pinning, 2xr uncertainties, periods, the drawn orbit's centre, the Horizons check (horizons_check.py, its period comparison and the data sheets' re-read), the period fetch before it (period_fetch.py), which record serves a body (helio_id, re-pinning a comet, JPL's exact name, a body on a skip list)\n"),
        (b'Read this file in 2 parts: lines 1-233, 234-342.\n',
         b'Read this file in 2 parts: lines 1-216, 217-408.\n'),
        (b"Skill version: 1.8 | 2026-10-15, with Anthropic's Claude Opus 5.5, at\n",
         b'Skill version: 1.9 | 2026-10-22, with Anthropic\'s Claude Opus 5.5, at\npalomas_orrery @ bfb6c474. v1.9 (L-443, with L-470) adds Which Record\nServes a Body: around the Sun a body with a helio_id is asked by it, in\nevery reader; a TNO\'s small-body record is JPL\'s "integrated barycenter";\na pinned comet is re-pinned to its newest record on Tony\'s word; JPL\'s\nexact name is read for each entry before it is served; an orbit JPL\nclasses as open is not drawn as an ellipse; and a name on a skip list\nsays which record failed around which centre, and is tested before it\ncomes off (Tony, 2026-10-22: "some idiosyncrasies in Horizons are\naddressed with specific record numbers, which can change").\nEarlier: 1.8 | 2026-10-15, with Anthropic\'s Claude Opus 5.5, at\n'),
        (b"Earlier: 1.6 | 2026-10-14, with Anthropic's Claude Opus 5.5, at\npalomas_orrery @ 5cd63cce and gallery @ 4b2b660a. v1.6 (L-431 build 3,\nwith L-395's move) records where the Horizons check lives now and what\nit compares, under Where the Check Lives, and What It Compares: it runs\nin the orrery's maintenance run beside the objects export, asks JPL\nonly what is due, compares each fetched period with JPL's PR within the\nperiod's own error, and re-reads each spacecraft's data sheet on the\nsame 30-day cycle. It corrects the line under Small-Body Record Pinning\nthat put the check in the website's Daily Run. It is the first version long enough\nfor more than one read, so it opens with its read plan (L-418).\n",
         b''),
        (b'on 2026-10-12, 2026-10-13 and 2026-10-14 (L-431), and 2026-10-15\n(L-444, L-445).\n',
         b'on 2026-10-12, 2026-10-13 and 2026-10-14 (L-431), 2026-10-15\n(L-444, L-445) and 2026-10-22 (L-443).\n'),
        (b"- Derive the primary's position from the secondary via the mass ratio when\n  Horizons serves only one member.\n\n## Small-Body Record Pinning (periodic comets)\n",
         b'- Derive the primary\'s position from the secondary via the mass ratio when\n  Horizons serves only one member.\n\n## Which Record Serves a Body (L-443)\n\nLearned bringing 50 of the orrery\'s bodies to the website, 2026-10-22.\nDesign record: documentation/DESIGN_L443_objects_rulings_20261022.md;\nJPL\'s answers: documentation/CHECK_L443_jpl_names_20261022.md and\nCHECK_L443_classes_pairs_20261022.md. A record number is JPL\'s\nbookkeeping, not the body: it can be re-solved, replaced by a newer\none, or answer only for some centres. So the method is to know which\nrecord each question asks, and to ask the same one everywhere.\n\n- ONE RECORD PER BODY AND CENTRE, IN EVERY READER. Around the Sun, a\n  body with a `helio_id` is asked by its helio_id, as a small body\n  (`helio_id_type`, else \'smallbody\'), by every reader: the orrery\'s\n  position fetch, its elements pre-fetch at both sites (the static plot\n  and the animation), `export_objects.served_identity`, `period_fetch.py`\n  and the website\'s builder. Until 2026-10-22 the pre-fetch asked the\n  body\'s own `id`, so the orrery drew the orbit from one record and the\n  marker from another. Around any other centre the body\'s `id` serves.\n- A TNO\'S SMALL-BODY RECORD IS THE PAIR\'S CENTRE. JPL\'s Lookup names\n  every helio_id record served here (Eris, Haumea, Makemake, Gonggong,\n  Quaoar, Orcus, Patroclus) "integrated barycenter": the small-body\n  solution follows the shared centre of the body and its moons. So it\n  serves the system around the Sun. The system-barycentre numbers for\n  Orcus (20090482) and Patroclus (20000617) are found in BOTH of JPL\'s\n  indexes, which the Horizons check reads as a wrong id_type (Checking\n  an Entry Against JPL, below); the small-body records 2004 DW and\n  A906 UL are found in one. Whether the drawing says "shared centre" is\n  the barycenter rule\'s, in orrery-coding-conventions.\n- A PINNED COMET GOES STALE. Three periodic comets were pinned to a\n  record that was no longer their newest: Schaumasse, Howell and\n  Churyumov-Gerasimenko, re-pinned on Tony\'s word of 2026-10-22\n  ("Re-pin to the newest") to 90000356, 90000901 and 90000703. List a\n  comet\'s records with COMMAND=\'DES=<desig>;\' and take the newest\n  apparition\'s. The check reports a newer record; only Tony\'s word\n  re-pins (Small-Body Record Pinning, below).\n- JPL\'S EXACT NAME, READ BEFORE SERVING. Every served entry carries\n  `horizons_name`, JPL\'s own form of its name, read from the Lookup (or\n  the main service, for a pinned record) the day the entry is keyed,\n  never typed from memory. The check then holds it to JPL.\n- AN OPEN ORBIT IS NOT AN ELLIPSE. The website draws an orbit from its\n  elements with an elliptic solver (render_orbits.solve_kepler,\n  sweep_conic), so a comet JPL classes hyperbolic (SBDB class HYP, as\n  Wierzchos) or one fitted with e near 1 waits for a path drawing and is\n  not served as an orbit. Read SBDB\'s class; do not judge from the name.\n- A SKIP NAMES WHAT FAILED. Six lists in palomas_orrery.py keep a body\n  out of a Horizons question: SKIP_HORIZONS_PREFETCH in plot_objects and\n  in animate_objects, SKIP_HORIZONS_TRAJECTORY in the static plot\'s\n  trajectory worker, and the fallbacks ANALYTICAL_POSITION_FALLBACK\n  (plot_actual_orbits and the static worker) and\n  ANALYTICAL_ANIMATION_FALLBACK (animation_worker), which act only when\n  Horizons returned nothing. period_fetch.py copies the pre-fetch list\n  as SKIP_NAMES. A name goes on a list with a comment naming the record\n  that failed, the centre it failed around, and the date. Gonggong\n  (id 920225088, its body-centre record; helio_id 2007 OR10) is on all\n  six, every line from 2026-02-04 (commit c60572d), with no such\n  comment, so it has no fetched period (L-470). The lists\' own comment\n  speaks only for the moons.\n- TAKING A NAME OFF A SKIP LIST IS A TEST. Ask each record the orrery\n  would ask, around each centre the body is plotted from: around the\n  Sun, the helio_id; around any other centre, the id. If every one\n  answers, the name comes off every list that names it, in one patch,\n  and the period fetch then fetches its period. If one fails, the name\n  stays and gains its comment. A skip kept for some centres and not\n  others is not in this method yet; it is written here before it is\n  built.\n\n## Small-Body Record Pinning (periodic comets)\n'),
    ]},
    {"path": 'documentation/SKILL_HISTORIES.md', "kind": "edit", "guard": 'anchors', "md5": '5809fedc15a7051ecafb663d45fbee26', "edits": [
        (b'(Moved down 2026-10-15, when 1.8 made a fourth entry.)\n',
         b"(Moved down 2026-10-15, when 1.8 made a fourth entry.)\n\nEarlier: 1.6 | 2026-10-14, with Anthropic's Claude Opus 5.5, at\npalomas_orrery @ 5cd63cce and gallery @ 4b2b660a. v1.6 (L-431 build 3,\nwith L-395's move) records where the Horizons check lives now and what\nit compares, under Where the Check Lives, and What It Compares: it runs\nin the orrery's maintenance run beside the objects export, asks JPL\nonly what is due, compares each fetched period with JPL's PR within the\nperiod's own error, and re-reads each spacecraft's data sheet on the\nsame 30-day cycle. It corrects the line under Small-Body Record Pinning\nthat put the check in the website's Daily Run. It is the first version long enough\nfor more than one read, so it opens with its read plan (L-418).\n(Moved down 2026-10-22, when 1.9 made a fourth entry.)\n"),
    ]},
    {"path": 'PROJECT_INSTRUCTIONS.md', "kind": "edit", "guard": 'anchors', "md5": '8575fd2dfd813ca00f933a691f341c1a', "edits": [
        (b'Cut from bfb6c474 at https://github.com/tonylquintanilla/palomas_orrery\n',
         b'Cut from d91dc1d0 at https://github.com/tonylquintanilla/palomas_orrery\n'),
        (b'horizons-orbital-mechanics   1.8  Horizons queries, centers, frames, osculating\n',
         b'horizons-orbital-mechanics   1.9  Horizons queries, centers, frames, osculating\n'),
        (b'                                  before it (period_fetch.py)\n',
         b"                                  before it (period_fetch.py), which record\n                                  serves a body (helio_id, re-pinning a comet,\n                                  JPL's exact name, a body on a skip list)\n"),
        (b"v3.109 (October 22, 2026): No rule changed in this document. ONE\nskill bump, one version (L-443, slice 1 of the objects):\ninteractive-exhibit 1.20 -> 1.21. THE DRAWER'S GROUPS FOLD OPEN; EVERY\nCOMET IS DRAWN FROM TODAY; A BARE LINK OPENS THE SOLAR SYSTEM ROOM.\n",
         b"v3.109 (October 22, 2026): No rule changed in this document. TWO\nskill bumps, one version each (L-443, slice 1 of the objects, with\nL-470): interactive-exhibit 1.20 -> 1.21, horizons-orbital-mechanics\n1.8 -> 1.9. THE DRAWER'S GROUPS FOLD OPEN; EVERY COMET IS DRAWN FROM\nTODAY; A BARE LINK OPENS THE SOLAR SYSTEM ROOM; ONE RECORD SERVES A\nBODY, AND A SKIP SAYS WHAT FAILED.\n"),
        (b'"Yes." And stage 10, his ruling of 2026-10-01, built with the slice.\n\n',
         b'"Yes." And stage 10, his ruling of 2026-10-01, built with the slice.\nAsked why Gonggong has no period, and whether the next session should\ntest taking it off the skip list: "yes but only if it accords with our\nmethod or requires a method revision. and we should document our\nmethod developed in this session in the skill. ... some idiosyncrasies\nin Horizons are addressed with specific record numbers, which can\nchange"\n\n'),
        (b'documentation/SKILL_HISTORIES.md, by the three-entry rule.\n\n',
         b"documentation/SKILL_HISTORIES.md, by the three-entry rule.\nhorizons-orbital-mechanics gains Which Record Serves a Body: one record\nper body and centre in every reader, the helio_id around the Sun; a\nTNO's small-body record as the pair's centre; a pinned comet re-pinned\nto its newest record on Tony's word; JPL's exact name read before\nserving; an open orbit not served as an ellipse; a skip list's name\nsaying which record failed around which centre, and the test for\ntaking one off. Its v1.6 entry moved to documentation/SKILL_HISTORIES.md.\n\n"),
        (b'that session. The next session confirms its loaded copy reads\ninteractive-exhibit 1.21 before exhibit work. This session confirmed\n',
         b'that session. The next session confirms its loaded copies read\ninteractive-exhibit 1.21 before exhibit work and horizons-orbital-mechanics\n1.9 before Horizons work. This session confirmed\n'),
    ]},
    {"path": 'patch_L443_3_close_20261022.py', "kind": "delete", "md5": 'bad231ba9c52612d38a6ff8798d0abc7'},
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
        if f["kind"] == "delete":
            if not os.path.exists(path):
                plan.append((f, path, None, "gone"))
                continue
            raw = open(path, "rb").read().replace(b"\r\n", b"\n")
            if hashlib.md5(raw).hexdigest() != f["md5"]:
                fail("%s is not the copy this patch removes (content "
                     "fingerprint differs); nothing was removed" % f["path"])
            plan.append((f, path, None, False))
            continue
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
        if f["kind"] == "delete":
            if crlf == "gone":
                print("ok  %s (already gone)" % f["path"])
            else:
                os.remove(path)
                print("ok  %s (removed)" % f["path"])
            continue
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
