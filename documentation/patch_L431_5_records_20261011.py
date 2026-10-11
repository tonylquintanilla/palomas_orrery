"""patch_L431_5_records_20261011.py -- the records of L-431's build 1
(orbital periods from JPL: the period in the orrery's hovers).

Built on orrery 41e9a1d569098d35f327870ca30050cb83645924 at
https://github.com/tonylquintanilla/palomas_orrery ("Update
WHERE_WE_ARE_10-11-26_1311_run_record.md"). The gallery is not touched.
Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\;
gallery C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\.
Written October 11, 2026 with Anthropic's Claude Opus 5.5.

HOW TO RUN
    Run patch_L431_4_period_in_hovers_20261011.py first. Then this one,
    from the orrery repo's ROOT folder: open it in VS Code and press Run,
    or from a terminal in that folder:
        python patch_L431_5_records_20261011.py
    Success prints one "ok" line per edit, then "patch applied".

WHAT IT CHANGES
    LEDGER_CONSOLIDATED.md -- header stamp; L-431 (orbital periods):
        your run of the design close, build 1 built and tested, what it
        found, the Gap, the Ref.
    documentation/WHERE_WE_ARE.md -- by section, never below the
        run-record marker: the date, the box, road stage 6a, Signals,
        Where the details are; two marks cleared.
    documentation/HANDOFF_L431_period_build1_20261011.md -- created: the
        build record, with the hover's words for your approval.

SAFETY
    Each file is checked only at the lines this patch edits: every
    anchor must match exactly once, and no edit lands below the
    run-record marker. If any check fails, NOTHING is written. A file
    found with Windows line endings is matched after turning them into
    LF and written back LF, and the patch says so. Undo after a run is
    Discard Changes in GitHub Desktop (and delete the new handoff).
"""
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))

EDITS = [
    ('LEDGER_CONSOLIDATED.md', 'header stamp',
     "three builds' order; its design record), built on 324a574f.\nReview and RICE update Tony 6-21-2026\n",
     "three builds' order; its design record), built on 324a574f.\nModule updated: October 11, 2026 with Anthropic's Claude Opus 5.5\n(L-431 build 1: the period in the orrery's hovers, from JPL, by the\nlarger error; patch_L431_4; its record), built on 41e9a1d5.\nReview and RICE update Tony 6-21-2026\n"),
    ('LEDGER_CONSOLIDATED.md', 'L-431 build 1 and Gap',
     "**Gap:** three builds, in order (the record's section 3):\n1. The period in the orrery: keep PR, store it with centre, date and\n   error, the two-centre test at first fetch, the fallback order in the\n   hover, the parameters window and the fetch's record. Tony's look at\n   Encke, Sedna and Mercury.\n2. The drawn ellipse around the period's centre, and the markers from\n   the fetched period (Mode 5, Tony's look).\n3. The website: the export carries each period; every room's hover\n   prints it; the Horizons check compares it.\nAt build 1's close the two-centre test goes to\nhorizons-orbital-mechanics as method. The typed table's 132 unsourced\nentries stay one class, not chased.\n",
     '- **Tony\'s run of the design close, 2026-10-11** (his copy\n  `documentation/WHERE_WE_ARE_10-11-26_1311_run_record.md`):\n  patch_L431_3 run and pushed at 9802e04; ledger-and-session-records\n  1.20 "was done already". The build session loaded 1.20, matching the\n  manifest, so the obligation the design session carried is discharged.\n- **2026-10-11, build 1 built** (Claude Opus 5.5, at 41e9a1d5; record\n  `documentation/HANDOFF_L431_period_build1_20261011.md`), by\n  `patch_L431_4_period_in_hovers_20261011.py`:\n  - New `orbital_period.py`. One Horizons query per centre asks for PR\n    at the plot date and a Julian year later (a year earlier if\n    refused). The two-centre test runs at a body\'s first fetch and its\n    choice is saved; a refresh asks only the chosen centre, and runs the\n    test again if that centre moved more than the other did when\n    chosen (method 5, the build\'s choice). SBDB\'s sigma for small\n    bodies; a pinned record number is looked up by the name Horizons\n    gives it (2P/Encke -> 2P). Digits by the Report test on the larger\n    error, years and days apart. The fallback order for showing.\n  - The orbit cache keeps a `period` record beside each entry\'s\n    elements, written only by a fetch accepted in the "Update Orbital\n    Elements?" box; the direct fetches in `idealized_orbits.py` and\n    `spacecraft_encounters.py` cost what they did. A failed period\n    query keeps the last fetched record. The elements are unchanged.\n  - Readers: the hover (`format_detailed_hover_text`: the static plot,\n    the animation, the social export), the parameters window\'s Orbital\n    Period row, the precession note\'s orbit count, `fetch_position`\'s\n    period record. The elements fetch keeps PR as `P_days`, and the\n    record says whether it agrees with the period query.\n  - `D_PER_JULIAN_YEAR` (365.25 d, exact; IAU Style Manual, SI Units,\n    Table 5, read 2026-10-11) and the token `d_per_yr`. The export\n    carries both, as it carries `S_PER_HOUR`; the gallery\'s 27 offline\n    checks pass with that export in place (sandbox, at e3536c87).\n  - Confirmed before building, through the chat\'s web-fetch tool:\n    Horizons labels the period PR and prints 9.999E+99 for C/2025 N1\'s\n    open orbit; SBDB gives `per` with its sigma; astroquery 0.4.11 maps\n    PR to `P` in days (its source). The end-to-end live check is Tony\'s:\n    the patch asks JPL for Encke, Sedna, Mercury and 3I/ATLAS as it ends.\n  - Tested in the sandbox, which cannot reach JPL, with JPL faked from\n    the rulings record\'s section 5: the hovers print that table\'s three\n    lines exactly; Sedna around the barycentre, Mercury and Encke\n    around the Sun; 3I/ATLAS "none (open orbit)"; the Moon around\n    Earth with no test; a refresh asks only the chosen centre; a failed\n    query keeps the last record; Pluto from the Pluto-Charon\n    barycentre keeps its typed 6.387 days, marked. The window opens\n    headless; maintenance run 23 of 23, gate path 0, whole tree 292\n    (no change).\n- **Found in build 1, recorded and not chased (The Braid):**\n  - 39 moons\' `mission_info` in `celestial_objects.py` type a period\n    ("Saturn orbital period: 0.94 Earth days"); those hovers show it\n    under the fetched one. One class.\n  - SBDB\'s 2P solution is not record 90000091: its `per` sigma read\n    0.00011075 d on 2026-10-11, where this item recorded 0.00021413 d.\n    Both are far below Encke\'s year change, 0.29 d; the print holds.\n  - `VIEW_TO_OSCULATING_CENTRE` in `orbital_period.py` copies the\n    `osculating_center_body` block in `palomas_orrery.py` (checked equal\n    in the pre-test). Build 2 works on that path and gives it one home.\n  - On the typed period until build 2: the parameters window\'s\n    estimated apsis dates (it fills `params[\'period\']`),\n    `apsidal_markers.py`, `idealized_orbits.py`.\n  - `get_fallback_elements` reads the plain cache key, not the\n    centre-aware one. Build 2 works on that path.\n  - The bare 365.25s in other modules. One class.\n**Gap:** three builds, in order (the record\'s section 3):\n1. The period in the orrery: BUILT 2026-10-11. Waits for Tony\'s run\n   (its live check of four bodies) and his look at Encke, Sedna and\n   Mercury, where he approves the hover\'s words (the build record\'s\n   section 4).\n2. The drawn ellipse around the period\'s centre, and the markers from\n   the fetched period (Mode 5, Tony\'s look).\n3. The website: the export carries each period; every room\'s hover\n   prints it; the Horizons check compares it.\nOwed to horizons-orbital-mechanics once Tony\'s run shows build 1\nworking against JPL: the two-centre test, its choice saved at first\nfetch, SBDB\'s lookup of a pinned record by Horizons\' name. The typed\ntable\'s 132 unsourced entries stay one class, not chased.\n'),
    ('LEDGER_CONSOLIDATED.md', 'L-431 Ref',
     '**Ref:** `documentation/DESIGN_L431_orbital_periods_rulings_20261011.md`;\n`documentation/DESIGN_L431_orbital_periods_20261011.md`;\n',
     '**Ref:** `documentation/DESIGN_L431_orbital_periods_rulings_20261011.md`;\n`documentation/DESIGN_L431_orbital_periods_20261011.md`;\n`documentation/HANDOFF_L431_period_build1_20261011.md`; `orbital_period.py`;\n'),
    ('documentation/WHERE_WE_ARE.md', 'header date',
     'Last updated: October 11, 2026, at the orbital periods design talk.\n- Written at orrery 324a574 and gallery e3536c8.\n',
     'Last updated: October 11, 2026, at build 1 of orbital periods.\n- Written at orrery 41e9a1d and gallery e3536c8.\n'),
    ('documentation/WHERE_WE_ARE.md', 'the box',
     "> **Changed since you last read this:**\n> - Orbital periods are designed, every question settled: L-431\n>   (orbital periods). Each body's period comes from JPL, around the\n>   centre that moves less, with the digits its errors earn.\n> - Periods go on the website too, right after the orrery.\n> - Mercury checked: around the Sun its period moves 4 seconds a year.\n>\n> **Do next:** *build 1 of L-431 (orbital periods): the period in the\n> orrery's hovers, then your look at Encke, Sedna and Mercury.*\n>\n> **Needs you now:**\n> - *Orrery: patch_L431_3, maintenance run, push. If not done yet,\n>   upload ledger-and-session-records (1.20).*\n",
     "> **Changed since you last read this:**\n> - Orbital periods, build 1 is built: L-431 (orbital periods). The\n>   orrery's hovers show each body's period from JPL, the centre it\n>   was taken around, the date, and only the digits its errors earn.\n> - A period from the typed table now says it is typed.\n> - Nothing drawn moves yet. The orbits and markers are build 2.\n>\n> **Do next:** *your look at Encke, Sedna and Mercury, and your word\n> on the hover's wording (the build record, section 4).*\n>\n> **Needs you now:**\n> - *Orrery: patch_L431_4 (it asks JPL for four periods as it ends),\n>   patch_L431_5, maintenance run, your look, push.*\n"),
    ('documentation/WHERE_WE_ARE.md', 'road stage 6a',
     "  6a.  [next]  *Orbital periods from JPL: designed. Three builds: the\n               orrery's hovers, then the drawn orbits, then the\n               website.* << moved this session\n",
     "  6a.  [next]  *Orbital periods from JPL: build 1, the orrery's hovers,\n               is built and waits for your look. Then the drawn\n               orbits, then the website.* << moved this session\n"),
    ('documentation/WHERE_WE_ARE.md', 'Settled: mark cleared',
     '## Settled  **>> UPDATED THIS SESSION**\n',
     '## Settled\n'),
    ('documentation/WHERE_WE_ARE.md', 'Signals',
     '- Tier-1 on the gate path: 0, by name, in PROVENANCE_AUDIT.md at\n  f7c6f41 (your run of 2026-10-11). Whole tree: 292.\n',
     '- Tier-1 on the gate path: 0, by name, in PROVENANCE_AUDIT.md at\n  9802e04 (your run of 2026-10-11). Whole tree: 292.\n'),
    ('documentation/WHERE_WE_ARE.md', 'Waiting: mark cleared',
     '## Waiting on you  **>> UPDATED THIS SESSION**\n',
     '## Waiting on you\n'),
    ('documentation/WHERE_WE_ARE.md', 'Where the details are',
     '- Orbital periods: rulings\n  `documentation/DESIGN_L431_orbital_periods_rulings_20261011.md`;\n  first findings `documentation/DESIGN_L431_orbital_periods_20261011.md`\n- Your notes of Oct 10: `WHERE_WE_ARE_10-10-26_2019_run_record.md`\n',
     '- Orbital periods: rulings\n  `documentation/DESIGN_L431_orbital_periods_rulings_20261011.md`;\n  build 1 `documentation/HANDOFF_L431_period_build1_20261011.md`\n- Your notes of Oct 11: `WHERE_WE_ARE_10-11-26_1311_run_record.md`\n'),
]

HANDOFF_NAME = 'documentation/HANDOFF_L431_period_build1_20261011.md'
HANDOFF = '<!-- Doc-Kind: hand | Build record for L-431 (orbital periods from JPL), build 1 of 3: the period in the orrery\'s hovers. What was built, how it was tested, what Tony looks at, and what waits for builds 2 and 3. -->\n# L-431 (orbital periods from JPL): build 1, the period in the hovers\n\nBuilt on orrery 41e9a1d569098d35f327870ca30050cb83645924 at\nhttps://github.com/tonylquintanilla/palomas_orrery ("Update\nWHERE_WE_ARE_10-11-26_1311_run_record.md"); gallery\ne3536c8732d7b62faa5c09515e4b7f1d1c10af9c at\nhttps://github.com/tonylquintanilla/tonyquintanilla.github.io, read, not\ntouched.\nTony\'s local folders: orrery\n`C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\`;\ngallery `C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\`.\nWritten October 11, 2026 with Anthropic\'s Claude Opus 5.5.\n\n- Type: BUILD. Patches `patch_L431_4_period_in_hovers_20261011.py`\n  (the code) and `patch_L431_5_records_20261011.py` (the ledger, Where\n  We Are, this record), run in that order in the orrery folder.\n- Built from `documentation/DESIGN_L431_orbital_periods_rulings_20261011.md`,\n  sections 2 to 5, and L-431 in the ledger.\n- Skills loaded, each matching the manifest: ledger-and-session-records\n  1.20 (the obligation the design session carried is discharged),\n  horizons-orbital-mechanics 1.2, provenance-discipline 2.28,\n  orrery-coding-conventions 1.10, agentic-pre-test 1.3,\n  safe-file-editing 1.13. No skill version was cut.\n\n## 1. Read this first\n\n- The orrery\'s hovers now print each body\'s orbital period from JPL,\n  around the centre it is steadiest about, to the digits its errors\n  earn. A period from the typed table says it is typed.\n- Nothing drawn moves. The ellipses and the perihelion and aphelion\n  markers still use what they used (build 2).\n- Your part: run the two patches, read the live check the first one\n  prints, then look at Encke, Sedna and Mercury and approve the words\n  (section 4).\n\n## 2. What was built\n\n`orbital_period.py`, new:\n- One Horizons query per centre asks for the period at the plot date\n  and a Julian year later (a year earlier, if Horizons refuses the\n  later date).\n- At a body\'s first fetch, the two-centre test: around the Sun and\n  around the solar system\'s barycentre; the centre whose period moved\n  less in the year is kept, and the choice is saved. A later fetch\n  asks only the chosen centre: two queries in all, the elements and\n  the period, not four. If the chosen centre\'s period then moves more\n  than the other centre\'s did when the choice was made, the test runs\n  again. (The rulings record left this to the build; this is the\n  choice.)\n- Moons and the Pluto system keep the centre the orrery gives them,\n  with no test.\n- JPL\'s stated uncertainty of the orbit, from the Small-Body Database,\n  for small bodies only. A pinned record number such as Encke\'s\n  90000091 cannot be found there, so it is looked up by the name\n  Horizons gives the record: "2P/Encke" becomes "2P".\n- The digits: the larger of the year\'s change and that uncertainty,\n  years and days each placed by its own error, by the Report test of\n  provenance-discipline (The ceiling). Never fewer than one figure.\n- The fallback order for showing: the fetched period saved in the\n  orbit cache; the same record carried forward when a later fetch\n  could not get one; then the typed table, marked as typed.\n\nThe orbit cache, `data/osculating_cache.json`, keeps a `period` record\nbeside each entry\'s elements: the period in days, the centre, the plot\ndate it is for, the date it was fetched, the year\'s change, the SBDB\nuncertainty and what SBDB said, the larger error and which one it was,\nthe saved test, and whether the elements fetch\'s own period agreed. It\nis written only by a fetch you accept in the "Update Orbital\nElements?" box. The direct fetches in `idealized_orbits.py` and\n`spacecraft_encounters.py` do not ask for it and cost what they did.\n\nReaders, each reading through `orbital_period.py`:\n- The hover, `visualization_utils.format_detailed_hover_text`: the\n  static plot, the animation and the social export all build it there.\n- The orbital parameters window\'s Orbital Period row.\n- The precession note\'s orbit count, in `palomas_orrery.py`.\n- `fetch_position`\'s period record in `palomas_orrery.py`. Nothing reads\n  that record today; it follows the rule so a later reader is right.\n\nAlso: the elements fetch keeps Horizons\' period as `P_days`, and the\nperiod record says whether it agrees with the period query.\n`D_PER_JULIAN_YEAR` (365.25 days, exact, IAU Style Manual, "SI Units",\nTable 5, read 2026-10-11) and its unit token `d_per_yr`, so neither the\nyears nor the year\'s step divides by a bare number. The export carries\nthe row and the token, as it already carries `S_PER_HOUR`; the\ngallery\'s 27 offline checks pass with the new export in place.\n\n## 3. How it was checked\n\nBefore building, through the chat\'s web-fetch tool (2026-10-11):\n- Horizons labels the period PR, and prints 9.999E+99 for C/2025 N1\'s\n  open orbit.\n- SBDB gives the period as `per` with a sigma (Sedna "1900" days\n  without full precision; the design read 1864 with it).\n- astroquery 0.4.11 asks for AU and days and names PR "P", in days\n  (its own source, `jplhorizons/__init__.py`).\n\nThe sandbox cannot reach JPL. So the end-to-end live check is yours:\nthe first patch, after it writes, asks JPL for Encke, Sedna, Mercury\nand 3I/ATLAS and prints each record and its hover. It writes nothing.\n\nIn the sandbox, on a throwaway copy, with JPL faked from the rulings\nrecord\'s section 5:\n- The hovers print exactly section 5\'s three lines (below).\n- Sedna\'s centre is the barycentre; Mercury\'s and Encke\'s the Sun.\n- 3I/ATLAS prints "none (open orbit)".\n- The Moon, viewed from Earth, is measured around Earth with no test.\n- A refresh asks Horizons twice: the elements, then the chosen centre.\n- A failed period query keeps the last fetched record.\n- Pluto viewed from the Pluto-Charon barycentre keeps its typed 6.387\n  days, marked typed, and never borrows the Sun-centred period.\n- The orrery window opens headless; the maintenance run passes 23 of\n  23; the push gate holds at 0 Tier-1; the whole tree stays at 292.\n\n## 4. Your look: the words, old and new\n\nThe words beside each figure are yours to approve\n(orrery-coding-conventions, Hover Text Is Written for the Visitor). Old\nhover, every body: "Known Orbital Period: 0.2408 Earth years (87.97\ndays)".\n\nNew, as the sandbox printed them from section 5\'s numbers:\n\nEncke\n    Orbital period: 3.303 years (1206 days)\n    Around the Sun, from JPL Horizons, fetched 2026-10-11.\n    Rounded to how much the period changes in a year.\n\nSedna\n    Orbital period: 11,390 years (4,160,000 days)\n    Around the solar system\'s center of mass, from JPL Horizons, fetched 2026-10-11.\n    Rounded to JPL\'s stated uncertainty in the orbit.\n\nMercury\n    Orbital period: 0.2408455 years (87.9688 days)\n    Around the Sun, from JPL Horizons, fetched 2026-10-11.\n    Rounded to how much the period changes in a year;\n    JPL lists no orbit uncertainty for this body.\n\nA typed one (Venus, until it is fetched)\n    Orbital period: 0.615198 years (224.701 days)\n    Typed value, not fetched from JPL.\n\nAn open orbit\n    Orbital period: none (open orbit)\n    Around the Sun, from JPL Horizons, fetched 2026-10-11.\n\nThe numbers in your window will come from JPL\'s live answers, so they\nmay differ from section 5 in the last place.\n\nFour checks:\n1. Tick Encke, Sedna and Mercury, press Plot, answer Yes to each\n   "Update Orbital Elements?" box. The console prints a "[L-431\n   period]" line for each: the two centres\' year changes and the one\n   kept.\n2. Hover each. The lines read as above.\n3. Open the orbital parameters window and pick Encke: the Orbital\n   Period row reads "1206 days (3.303 yr), JPL, around the Sun".\n4. The ellipses and the perihelion and aphelion markers are where they\n   were.\n\n## 5. Found, recorded on L-431 and not chased\n\n- 39 moons\' descriptions in `celestial_objects.py` type a period, e.g.\n  "Saturn orbital period: 0.94 Earth days". Their hovers will show\n  that typed figure under the fetched one. One class.\n- SBDB\'s 2P solution is not Horizons\' record 90000091: its sigma read\n  0.00011075 days on 2026-10-11, where L-431 recorded 0.00021413. Both\n  are far below Encke\'s year change, 0.29 days, so the print does not\n  move.\n- `VIEW_TO_OSCULATING_CENTRE` in `orbital_period.py` copies the block in\n  `palomas_orrery.py` that sets `osculating_center_body`. The pre-test\n  checked they agree. Build 2 works on that path and gives it one home.\n- Still on the typed period until build 2: the parameters window\'s\n  estimated perihelion and aphelion dates, `apsidal_markers.py`,\n  `idealized_orbits.py`.\n- `get_fallback_elements` reads the plain cache key, not the\n  centre-aware one. Build 2 works on that path.\n- The bare 365.25s in other modules. One class.\n\n## 6. Owed\n\nTo horizons-orbital-mechanics, once your live run shows build 1\nworking: the two-centre test, its choice saved at first fetch, and\nSBDB\'s lookup of a pinned record by Horizons\' name (Method Belongs to\nthe Skill). Not cut this session: the build has not yet been seen\nworking against JPL.\n\n## 7. Tony-actions\n\n- (do) Save both patches in the orrery folder (already there if this\n  session was linked to your computer). Run\n  `patch_L431_4_period_in_hovers_20261011.py`; paste its output,\n  including the live check, into your run record.\n- (do) Run `patch_L431_5_records_20261011.py`, then\n  `orrery_maintenance_run.py`. Expect 23 of 23 and "0 TIER-1 -- the\n  push gate holds"; the whole tree should not move.\n- (do) The four checks in section 4.\n- (decide) The hover\'s words, section 4.\n- (do) Move both patches into `documentation/`; commit and push.\n\nSession record written October 2026 with Anthropic\'s Claude Opus 5.5.\n'


MARKER = '--- Your run record below this line'


def main():
    if not os.path.exists(os.path.join(ROOT, 'orbital_period.py')):
        print('ERROR: orbital_period.py is not here. Run '
              'patch_L431_4_period_in_hovers_20261011.py first. NOTHING was written.')
        sys.exit(1)
    hpath = os.path.join(ROOT, HANDOFF_NAME)
    if os.path.exists(hpath):
        print('ERROR: %s already exists; this patch has run. NOTHING was written.' % HANDOFF_NAME)
        sys.exit(1)
    texts, crlf = {}, set()
    for f, label, old, new in EDITS:
        path = os.path.join(ROOT, f)
        if f not in texts:
            if not os.path.exists(path):
                print('ERROR: %s not found in %s. NOTHING was written.' % (f, ROOT))
                sys.exit(1)
            raw = open(path, 'rb').read()
            if b'\r\n' in raw:
                crlf.add(f)
            texts[f] = raw.replace(b'\r\n', b'\n').decode('utf-8')
        t = texts[f]
        n = t.count(old)
        if n != 1:
            print('ANCHOR FAIL  %-34s %s (found %d times, expected 1). NOTHING was written.'
                  % (f, label, n))
            sys.exit(1)
        if MARKER in t and t.index(old) > t.index(MARKER):
            print('ANCHOR FAIL  %-34s %s lies below the run-record marker. NOTHING was written.'
                  % (f, label))
            sys.exit(1)
        texts[f] = t.replace(old, new)
        print('ok  %-34s %s' % (f, label))
    for f, text in texts.items():
        with open(os.path.join(ROOT, f), 'wb') as fh:
            fh.write(text.encode('utf-8'))
        if f in crlf:
            print('note: %s was CRLF in the working copy; written LF' % f)
    with open(hpath, 'wb') as fh:
        fh.write(HANDOFF.encode('utf-8'))
    print('ok  %-34s created' % HANDOFF_NAME)
    print()
    print('patch applied')
    print()
    print('NEXT:')
    print('  1. Run orrery_maintenance_run.py -- it rebuilds the ledger\'s index.')
    print('     Expect 23 of 23 and "0 TIER-1 -- the push gate holds".')
    print('  2. Your look: the four checks in the build record, section 4.')
    print('  3. Move both patch scripts into documentation/; commit and push.')


if __name__ == '__main__':
    main()
