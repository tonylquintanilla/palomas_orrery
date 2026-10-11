r"""patch_L431_3_design_close_20261011.py -- the close of L-431's design
talk (orbital periods from JPL): Tony's rulings onto L-431, the design
record, and Where We Are by section.

Built on orrery 324a574f4dd50f8acdea211b1d814f577343f927 at
https://github.com/tonylquintanilla/palomas_orrery ("v3.91 and run
record"); gallery e3536c8732d7b62faa5c09515e4b7f1d1c10af9c at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, read, not
touched. Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\;
gallery C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\.
Written October 11, 2026 with Anthropic's Claude Opus 5.5.

HOW TO RUN
    This file is saved in the orrery folder named above (the one that
    holds LEDGER_CONSOLIDATED.md). Open it in VS Code and press Run
    (python patch_L431_3_design_close_20261011.py). Success prints one
    "ok" line per edit, then "patch applied". The steps after it are
    printed at the end.

WHAT IT CHANGES
    LEDGER_CONSOLIDATED.md -- header stamp; L-431 gains the rulings of
        2026-10-11 and a new Gap: three builds, in order.
    documentation/WHERE_WE_ARE.md -- by section, never below the
        run-record marker: date line, the box, road stage 6a, Settled,
        Signals, Waiting on you, Where the details are.
    documentation/DESIGN_L431_orbital_periods_rulings_20261011.md --
        the design record, created. It was also saved there directly;
        an identical copy is accepted and left as it is.

    No code changes. This script is the delivery; move it to
    documentation/ once it has run.

SAFETY
    Each file is checked only at the lines this patch edits: every anchor
    must match exactly once. If any check fails, NOTHING is written. A
    file found with Windows line endings is matched after turning them
    into LF and written back LF, and the patch says so. A file this
    patch would create that is already there with the same content is
    accepted and named; with different content the patch refuses. Undo
    after a run is Discard Changes in GitHub Desktop.
"""
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
PAGE = 'documentation/WHERE_WE_ARE.md'
MARKER = b'--- Your run record below this line'

EDITS = [('LEDGER_CONSOLIDATED.md', 'L-431 rulings and Gap', "**Gap:** the design talk, then the build. Seven questions in the\ndesign record's section 7: the astroquery column; which centre; moons\nand the Pluto system; the drawn ellipse's same dependence on the\ncentre; queries per refresh; the typed table; the apsidal markers.\n**Ref:** `documentation/DESIGN_L431_orbital_periods_20261011.md`;\n", '- **Ruled at the design talk, 2026-10-11** (record\n  `documentation/DESIGN_L431_orbital_periods_rulings_20261011.md`):\n  - The period comes from the Horizons fetch (PR), for every body that\n    has one; the typed table only when nothing was fetched. Tony:\n    "Confirmed. I agree with this approach."\n  - Centre: ask for the Sun and the barycentre, at the plot date and a\n    year later; use the one whose period moves less, and name it in the\n    hover. Tony: "Confirmed as recommended".\n  - Digits: the larger of the year\'s movement and SBDB\'s sigma, years\n    and days each by its own error; a body with no SBDB entry prints by\n    the year\'s movement and says so. Tony: "Confirmed".\n  - Fallback order: a fresh fetch; then the last fetched period, saved\n    in the orbit cache (`data/osculating_cache.json`) with centre, date\n    and error; then the typed table, with a note such as "typed value,\n    not fetched from JPL". Not written back into `constants_new.py`.\n    Tony: "Confirmed".\n  - The website: "periods are basic data, for all bodies and should be\n    part of the hover text." Its step follows the orrery builds\n    directly, and the Daily Run\'s Horizons check compares the period.\n  - The drawn ellipse follows the period\'s centre, and the perihelion\n    and aphelion markers use the fetched period; one build, one look.\n    Tony: "Confirmed. This is the best solution."\n  - Mercury, read 2026-10-11: around the Sun its period moved 3.65 s in\n    a year (87.9688 days); around the barycentre it reads 90.8 then\n    90.0 days. The test picks the Sun.\n  - ledger-and-session-records 1.20, asked for at this session\'s\n    opening, was cut by the inner Oort cloud\'s website session at\n    1bbd9fe1; this session cut no second version.\n**Gap:** three builds, in order (the record\'s section 3):\n1. The period in the orrery: keep PR, store it with centre, date and\n   error, the two-centre test at first fetch, the fallback order in the\n   hover, the parameters window and the fetch\'s record. Tony\'s look at\n   Encke, Sedna and Mercury.\n2. The drawn ellipse around the period\'s centre, and the markers from\n   the fetched period (Mode 5, Tony\'s look).\n3. The website: the export carries each period; every room\'s hover\n   prints it; the Horizons check compares it.\nAt build 1\'s close the two-centre test goes to\nhorizons-orbital-mechanics as method. The typed table\'s 132 unsourced\nentries stay one class, not chased.\n**Ref:** `documentation/DESIGN_L431_orbital_periods_rulings_20261011.md`;\n`documentation/DESIGN_L431_orbital_periods_20261011.md`;\n'), ('LEDGER_CONSOLIDATED.md', 'header stamp', 'L-351, L-363, L-412 and L-416 updated), built on 1bbd9fe1.\nReview and RICE update Tony 6-21-2026\n', "L-351, L-363, L-412 and L-416 updated), built on 1bbd9fe1.\nModule updated: October 11, 2026 with Anthropic's Claude Opus 5.5\n(L-431's design talk: Tony's rulings on the period's source, centre,\ndigits, fallback, the website, the drawn orbit and the markers; the\nthree builds' order; its design record), built on 324a574f.\nReview and RICE update Tony 6-21-2026\n"), ('documentation/WHERE_WE_ARE.md', 'Where the details are', '- Orbital periods: design\n  `documentation/DESIGN_L431_orbital_periods_20261011.md`\n', '- Orbital periods: rulings\n  `documentation/DESIGN_L431_orbital_periods_rulings_20261011.md`;\n  first findings `documentation/DESIGN_L431_orbital_periods_20261011.md`\n'), ('documentation/WHERE_WE_ARE.md', 'Waiting on you', '- *Orbital periods first (L-431): which centre, the drawn ellipse,\n  the typed table, the apsidal markers.*\n', ''), ('documentation/WHERE_WE_ARE.md', 'Signals', '- Tier-1 on the gate path: 0, by name, in PROVENANCE_AUDIT.md at\n  1bbd9fe (your run of 2026-10-11). Whole tree: 292.\n', '- Tier-1 on the gate path: 0, by name, in PROVENANCE_AUDIT.md at\n  f7c6f41 (your run of 2026-10-11). Whole tree: 292.\n'), ('documentation/WHERE_WE_ARE.md', 'Settled', "- Orbital periods: JPL's own (PR), for every body that has one; the\n  hover shows it, not the typed table; digits by the errors. (Oct 10)\n", "- Orbital periods: JPL's own, every body, orrery and website; the\n  centre that moves less in a year, digits by the larger error, the\n  drawn orbit and markers alike; typed table last, marked. (Oct 11)\n"), ('documentation/WHERE_WE_ARE.md', 'road 6 and 6a', '  6.   [next]  The typed facts: the inner Oort cloud is drawn on the\n               website too. Left: the check. << moved this session\n  6a.  [next]  *Orbital periods from JPL for every body, printed by\n               their errors: design talk first.*\n', "  6.   [next]  The typed facts: the inner Oort cloud is drawn on the\n               website too. Left: the check.\n  6a.  [next]  *Orbital periods from JPL: designed. Three builds: the\n               orrery's hovers, then the drawn orbits, then the\n               website.* << moved this session\n"), ('documentation/WHERE_WE_ARE.md', 'the box', "> **Changed since you last read this:**\n> - The website draws the inner Oort cloud as the orrery does: the\n>   Hills cloud from the orrery's own dots. L-421 (the typed facts).\n> - The Galactic Plane row is in the Sun room: L-408 (the galactic\n>   plane), closed on your look.\n> - One check failed on Windows only; its fix waits for you.\n>\n> **Do next:** *the orbital periods design talk, then its build, as you\n> asked: `DESIGN_L431_orbital_periods_20261011.md`, section 7.*\n>\n> **Needs you now:**\n> - *Gallery: patch_L421_8, maintenance run, push. Orrery:\n>   patch_L421_9, maintenance run, push. Then upload\n>   ledger-and-session-records (1.20) and the instructions (v3.91).*\n", "> **Changed since you last read this:**\n> - Orbital periods are designed, every question settled: L-431\n>   (orbital periods). Each body's period comes from JPL, around the\n>   centre that moves less, with the digits its errors earn.\n> - Periods go on the website too, right after the orrery.\n> - Mercury checked: around the Sun its period moves 4 seconds a year.\n>\n> **Do next:** *build 1 of L-431 (orbital periods): the period in the\n> orrery's hovers, then your look at Encke, Sedna and Mercury.*\n>\n> **Needs you now:**\n> - *Orrery: patch_L431_3, maintenance run, push. If not done yet,\n>   upload ledger-and-session-records (1.20).*\n"), ('documentation/WHERE_WE_ARE.md', 'header date', "Last updated: October 11, 2026, at the inner Oort cloud's website close.\n- Written at orrery 1bbd9fe and gallery e5a3d13.\n", 'Last updated: October 11, 2026, at the orbital periods design talk.\n- Written at orrery 324a574 and gallery e3536c8.\n')]

NEW_FILES = {'documentation/DESIGN_L431_orbital_periods_rulings_20261011.md': '<!-- Doc-Kind: hand | Design record for L-431 (orbital periods from JPL): Tony\'s rulings at the design talk of 2026-10-11, the order of the three builds, the method the build follows, and Mercury\'s numbers. Zero code. Companion to DESIGN_L431_orbital_periods_20261011.md, which holds the first findings. -->\n# L-431 (orbital periods from JPL): the design talk\'s rulings\n\nBuilt on orrery 324a574f4dd50f8acdea211b1d814f577343f927 at\nhttps://github.com/tonylquintanilla/palomas_orrery ("v3.91 and run\nrecord") and gallery e3536c8732d7b62faa5c09515e4b7f1d1c10af9c at\nhttps://github.com/tonylquintanilla/tonyquintanilla.github.io, read,\nnot touched.\nTony\'s local folders: orrery\n`C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\`;\ngallery `C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\`.\nWritten October 11, 2026 with Anthropic\'s Claude Opus 5.5.\n\n- Type: DESIGN SESSION (zero code). The builds are later sessions\'.\n- Companion to `documentation/DESIGN_L431_orbital_periods_20261011.md`.\n  That record keeps JPL\'s numbers (its section 3) and every place the\n  orrery reads a period today (its section 6). Its proposals (sections\n  4 and 5) are now ruled, as below, and its section 7\'s questions are\n  all answered in section 4 here.\n- Skills read: ledger-and-session-records 1.19 was the copy this\n  session loaded. The repo moved to 1.20 during the session (the inner\n  Oort cloud\'s website session cut it at 1bbd9fe1, protocol v3.91).\n  The next session confirms its loaded copy reads 1.20 before ledger\n  or handoff work.\n- Skills the builds fire: horizons-orbital-mechanics (1.2),\n  provenance-discipline (2.28; "A Computed Position Prints What Its\n  Errors Earn"), orrery-coding-conventions (hover text),\n  agentic-pre-test, safe-file-editing; interactive-exhibit and\n  gallery-cache-builder for the website step.\n\n## 1. Read this first\n\n- *Every ruling Tony was asked for is made.* Seven, in section 2.\n- *Three builds, in order:* the period in the orrery; then the drawn\n  orbit and the perihelion and aphelion markers, with Tony\'s look;\n  then the website. Section 3.\n- *Nothing is left for Tony before the first build.* The words the\n  hover prints are his to approve at the first build\'s look.\n\n## 2. The rulings, in order, Tony\'s words\n\n1. **Where the period comes from.** The orrery takes each body\'s\n   period from its Horizons fetch, JPL\'s own PR ("sidereal orbit\n   period"), for every body that has one. The typed table\n   `KNOWN_ORBITAL_PERIODS` is used only when nothing has been fetched.\n   Tony: "Confirmed. I agree with this approach."\n2. **Which centre.** Horizons is asked for the period around the Sun\n   (500@10) and around the solar system\'s barycentre, its centre of\n   mass (500@0), each at the plot date and a year later. The centre\n   whose period moves less over the year is used, and the hover names\n   it. No distance threshold: nothing sources one. Tony: "Confirmed\n   as recommended".\n3. **How many digits.** The larger of two errors sets them: the\n   period\'s movement over the year around the chosen centre, and\n   JPL\'s stated uncertainty of the orbit fit (SBDB\'s sigma) where the\n   body has one. Years and days are each rounded by their own error,\n   by the Report test (provenance-discipline, The ceiling). A body\n   with no SBDB entry -- the planets, the Moon and the other moons --\n   prints by the year\'s movement alone, and the hover says so.\n   Tony: "Confirmed".\n4. **The typed table.** It stays as the last fallback. A hover that\n   reaches it says so, with a short note such as "typed value, not\n   fetched from JPL", and prints the value as typed. Its 132 entries\n   are not sourced or corrected now; they stay one ledger class on\n   L-431, not chased (The Braid). Tony: "Confirmed."\n5. **The fallback order.** Tony asked whether the fetched period\n   could be written back to the table as the next fallback. Answer:\n   the orbit cache, `data/osculating_cache.json`, already does that\n   job, without a program editing its own code in `constants_new.py`.\n   The order is: a fresh fetch; then the last fetched period, saved\n   in the cache with its centre, its date and its error; then the\n   typed table with its note. The hover gives the fetch date. Tony:\n   "Confirmed".\n6. **The website.** Tony: "periods are basic data, for all bodies and\n   should be part of the hover text." So the website step follows the\n   orrery build directly, not when some room first needs it: the\n   export carries each body\'s period with its centre, date and error,\n   every body\'s hover in the rooms shows it, and the website\'s daily\n   Horizons check compares the period with JPL too. Tony: "Confirmed".\n7. **The drawn orbit and the markers.** The drawn ellipse is taken\n   around the same centre as the period, so the hover and the drawing\n   describe one orbit. The perihelion and aphelion markers use the\n   fetched period, in the same fallback order. Both change what is\n   drawn, so they are one build with one look. Tony: "Confirmed." and\n   "Confirmed. This is the best solution."\n\n## 3. The three builds, in order\n\nAll under L-431. The orrery and gallery each pin their own SHA.\n\n1. **The period (orrery).** Keep PR from the elements fetch\n   (`orbit_data_manager.query_horizons_elements`), store it in the\n   orbit cache with the centre, the fetch date and the year\'s\n   movement (`osculating_cache_manager.fetch_osculating_elements`),\n   read SBDB\'s sigma where the body has one, and use the fallback\n   order everywhere the period is read for SHOWING: the hover\n   (`visualization_utils.format_detailed_hover_text`), the orbital\n   parameters window (`orbital_param_viz.py`), the fetch\'s position\n   record and the precession warning (`palomas_orrery.py`). The\n   drawn ellipse and the markers do not change in this build. Done\n   when Tony looks at Encke, Sedna and Mercury in the orrery window\n   and the hovers read as section 5 below.\n2. **The drawn orbit and the markers (orrery), Mode 5.** The ellipse\n   around the period\'s centre (`idealized_orbits.py`), following the\n   existing Pluto-Charon barycentre pattern, which already draws\n   Pluto and Charon from elements fetched around their barycentre;\n   and the markers\' dates from the fetched period (`apsidal_markers.py`,\n   the places named in the first record\'s section 6). Sedna\'s\n   ellipse shrinks from about 540 au around the Sun to about 506 au\n   around the barycentre (2026-10-10). Done on Tony\'s look at the\n   render.\n3. **The website (gallery, after the orrery builds).** The orrery\'s\n   export carries each body\'s period, centre, date and error; every\n   body\'s hover in the rooms prints it by the same digits rule; the\n   Daily Run\'s Horizons check compares the period with JPL. It waits\n   until no other session is building in the gallery.\n\n## 4. Method the builds follow (not Tony\'s; recorded so it is not re-asked)\n\nThe first record\'s section 7, answered:\n\n1. **The column.** astroquery\'s `elements()` documents the period as\n   "P", in days, from Horizons\' PR. The first build confirms it live\n   on Encke, Sedna, Mercury and one open-orbit comet, and prints what\n   it found. For an open orbit Horizons prints PR as 9.999E+99 (to be\n   confirmed live); the hover then says "none (open orbit)".\n2. **Which centre:** ruled, section 2.\n3. **Moons and the Pluto system.** They keep the centre the orrery\n   already gives them through `center_body` (their planet, or the\n   Pluto-Charon barycentre). No two-centre test. They print by the\n   year\'s movement, with the note.\n4. **The drawn orbit:** ruled, section 2, item 7.\n5. **Cost.** The two-centre test runs on a body\'s FIRST fetch, and\n   its choice is saved in the cache. A refresh then asks only for the\n   chosen centre, at the plot date and a year later: two queries, not\n   four. A refresh that sees the chosen centre move more than the\n   other did when it was chosen may re-run the test; the build decides\n   and says so.\n6. **The typed table:** ruled, section 2, items 4 and 5.\n7. **The markers:** ruled, section 2, item 7.\n\nOwed to horizons-orbital-mechanics at the first build\'s close, as\nmethod, once the build has shown it working: the two-centre test, and\nthat the choice is saved at first fetch (Method Belongs to the Skill).\n\n## 5. What the hovers will read (for the first build\'s look)\n\nFrom JPL\'s numbers at 2026-10-10, by the digits rule:\n\n| Body | Centre (chosen) | Larger error | Prints |\n|---|---|---|---|\n| Encke | Sun | year\'s movement, 0.29 d | 3.303 years (1206 days) |\n| Sedna | barycentre | SBDB sigma, 1864 d (5.1 yr) | 11,390 years (4,160,000 days) |\n| Mercury | Sun | year\'s movement, 3.7 s | 0.2408455 years (87.9688 days) |\n\nMercury, read 2026-10-11 from Horizons (EPHEM_TYPE=ELEMENTS, DE441,\n00:00 TDB, through the chat\'s web-fetch tool, which quoted the lines):\n\n| Centre | PR 2025-10-10 (s) | PR 2026-10-10 (s) | change in a year |\n|---|---|---|---|\n| Sun (500@10) | 7.600508693862242E+06 | 7.600505042307498E+06 | 3.65 s |\n| barycentre (500@0) | 7.845795957243782E+06 | 7.778018708926311E+06 | 0.78 days |\n\nAround the barycentre Mercury\'s period reads 90.8 and then 90.0 days,\nagainst 87.9688 around the Sun. Mercury is close enough to the Sun\nthat the Sun\'s own wobble around the barycentre, mostly from Jupiter,\nis a large share of its distance: Sedna\'s case reversed, and the\nreason a fixed distance rule could not serve both. Mercury\'s\nperihelion precession turns the orbit and moves the date of closest\napproach, not the period; JPL\'s integration includes relativity.\n\nThe words beside each figure -- the centre, "by the year\'s movement\nonly", "typed value, not fetched from JPL", the fetch date -- are\nproposed by the first build and approved by Tony at its look\n(provenance-discipline: words the display\'s owner approved).\n\n## 6. Skill versions this session\n\nTony asked at the opening for ledger-and-session-records 1.20, with\nthe rule recorded on L-351: every handoff, brief and design record\nnames his two local folders in its header beside the GitHub line. The\ninner Oort cloud\'s website session cut exactly that version during\nthis session, at 1bbd9fe1 (`patch_L421_9_close_20261011.py`,\nprotocol v3.91), and L-351 records it landed. One skill version only,\nso this session cut none. This record follows 1.20\'s header rule.\n\n## 7. Tony-actions\n\n- (do) Run `patch_L431_3_design_close_20261011.py` in the orrery\n  folder, then `orrery_maintenance_run.py`, then commit and push.\n- (do) If not done yet: upload ledger-and-session-records 1.20 to\n  Settings > Skills.\n\nSession record written October 2026 with Anthropic\'s Claude Opus 5.5.\n'}


def fail(msg):
    print('FAILURE: ' + msg)
    print('NOTHING was written. Undo is not needed.')
    sys.exit(1)


def full(path):
    return os.path.join(ROOT, *path.split('/'))


def non_ascii(data):
    return sum(1 for ch in data if ch > 127)


def main():
    if not os.path.exists(full('LEDGER_CONSOLIDATED.md')):
        fail("LEDGER_CONSOLIDATED.md is not in this folder. Save the patch in "
             "the orrery repo's root folder.")
    ledger = open(full('LEDGER_CONSOLIDATED.md'), 'rb').read()
    if b'DESIGN_L431_orbital_periods_rulings_20261011.md' in ledger:
        print('already applied: L-431 already names the rulings record. '
              'Nothing written.')
        return 0
    present = []
    for path, content in NEW_FILES.items():
        if os.path.exists(full(path)):
            have = open(full(path), 'rb').read().replace(b'\r\n', b'\n')
            if have == content.encode('ascii'):
                present.append(path)
            else:
                fail('%s already exists with different content. Compare it with '
                     'the one this patch carries before deleting either.' % path)

    texts, crlf = {}, []
    for path, _, _, _ in EDITS:
        if path not in texts:
            if not os.path.exists(full(path)):
                fail('%s not found.' % path)
            raw = open(full(path), 'rb').read()
            if b'\r\n' in raw:
                crlf.append(path)
            texts[path] = raw.replace(b'\r\n', b'\n')
    before = {path: non_ascii(data) for path, data in texts.items()}
    if texts[PAGE].count(MARKER) != 1:
        fail('WHERE_WE_ARE.md: the run-record marker was not found once.')
    below = texts[PAGE][texts[PAGE].index(MARKER):]

    for path, label, old, new in EDITS:
        try:
            o, n = old.encode('ascii'), new.encode('ascii')
        except UnicodeEncodeError:
            fail('%s -- %s: this patch would insert non-ASCII text.' % (path, label))
        count = texts[path].count(o)
        if count != 1:
            fail('ANCHOR FAIL %s -- %s: expected 1 match, found %d. Has that part '
                 'changed since 324a574?' % (path, label, count))
        texts[path] = texts[path].replace(o, n)
        print('ok  %-34s %s' % (path, label))
    if texts[PAGE][texts[PAGE].index(MARKER):] != below:
        fail('WHERE_WE_ARE.md: an edit reached below the run-record marker.')

    for path, data in texts.items():
        with open(full(path), 'wb') as handle:
            handle.write(data)
    for path, content in NEW_FILES.items():
        if path in present:
            print('ok  %s already there, identical; left as it is' % path)
            continue
        with open(full(path), 'wb') as handle:
            handle.write(content.encode('ascii'))
        print('ok  %s created' % path)
    for path in crlf:
        print('note: %s was CRLF in the working copy; written LF' % path)
    for path, count in before.items():
        if count:
            print('note: %s holds %d non-ASCII byte(s) this patch did not reach '
                  '(Tony\'s notes, if below the run-record marker)' % (path, count))
    above = texts[PAGE][:texts[PAGE].index(MARKER)].count(b'\n')
    print('note: WHERE_WE_ARE.md has %d lines above the run-record marker '
          '(the cap is 130)' % above)
    print('stamps updated: the ledger header; WHERE_WE_ARE.md date line')
    print('patch applied: %d edits in %d files, %d file(s) created or confirmed.'
          % (len(EDITS), len(texts), len(NEW_FILES)))
    print('')
    print('NEXT:')
    print('  1. Run orrery_maintenance_run.py. Expect every gating checker to '
          'pass and "GATE PATH: 0 TIER-1 -- the push gate holds". It rebuilds '
          'the ledger index.')
    print('  2. Move this script into documentation/; commit and push.')
    print('  3. If not done yet, upload ledger-and-session-records 1.20 to '
          'Settings > Skills.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
