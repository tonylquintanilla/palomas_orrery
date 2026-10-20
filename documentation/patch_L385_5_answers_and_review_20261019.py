#!/usr/bin/env python3
"""
patch_L385_5_answers_and_review_20261019.py -- the last of the night's
records: Gemini 4's review of the Sun's numbers (L-411), and your
answers on the fades' words with the ruling that the corona and the
streamer belt are one feature (L-410).

Built on your orrery folder as patch_L385_4_close_20261019.py and the
maintenance run left it, on top of orrery
59e1b656c56ac38660f7943cae066513e9ab7b77 at
https://github.com/tonylquintanilla/palomas_orrery ("v3.104"). The
website is not touched.
Tony's orrery folder:
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\
Written October 19, 2026 with Anthropic's Claude Opus 5.5.

RUN COMMAND

    python patch_L385_5_answers_and_review_20261019.py

    Saved in the ORRERY folder above. Open it in VS Code and click Run.
    It takes no arguments and asks no questions.

WHAT IT DOES, all or nothing, checking only the lines it changes, so
your notes and marks are kept:

    LEDGER_CONSOLIDATED.md     L-411: Gemini 4's return and its new gap;
                               L-410: your answers and the one-feature
                               ruling
    documentation/WHERE_WE_ARE.md   the box: words answered, Gemini 4's
                               find; one old Settled line retired
    documentation/HANDOFF_L385_opening_views_20261019.md   the same
    documentation/WORDS_L410_sun_fades_20261019.md   revision 3, added
                               after your marks: the rulings and three
                               drafts to mark next session
    documentation/REVIEW_L411_gemini4_worksheet_20261019.md   new

WHAT IT PRINTS

    Success: one "ok" line per file, then "patch applied".
    Failure: one ANCHOR FAIL line and "NOTHING was written."

Undo is Discard Changes in GitHub Desktop.

Role: dev_tools
Domain: dev_tools
"""

import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))

ANCHOR = {
    'documentation/WHERE_WE_ARE.md': [
        ("> **Needs you now:**\n> - The fades' words, revision 2, before that build: answer in place in\n>   `WORDS_L410_sun_fades_20261019.md`, section 3 especially.\n\n",
         "> **Needs you now:**\n> - Fades' words answered; revision 3's three drafts (the corona and\n>   streamer belt now one feature) are marked at the build's start.\n> - Gemini 4 checked the Sun's numbers: they hold. One sentence is off:\n>   the chromosphere's base is near 4,400 kelvin, not 6,000. New words\n>   for it come to you as a list (L-411, the Sun's typed numbers).\n\n"),
        ("  its i panel. What a visitor reads: in provenance-discipline. (Oct 17)\n- Earth's talks wait; the Sun's numbers, then its drawings, then the objects. (Oct 17)\n- Temperatures in kelvin. The Sun's numbers end with L-455. (Oct 17)\n",
         "  its i panel. What a visitor reads: in provenance-discipline. (Oct 17)\n- Temperatures in kelvin. The Sun's numbers end with L-455. (Oct 17)\n"),
    ],
    'documentation/HANDOFF_L385_opening_views_20261019.md': [
        ("to Gemini 4 Argon at its highest thinking level, and save the worksheet\nin `documentation/worksheets/`.\nTony's local folders: orrery\n",
         "to Gemini 4 Argon at its highest thinking level, and save the worksheet\nin `documentation/worksheets/`. Done the same night: reviewed in\n`REVIEW_L411_gemini4_worksheet_20261019.md`. Its one real find, the\nchromosphere's base temperature in kelvin, needs new words from you.\nYour answers on the fades' words came back the same night; revision 3\nof the list\nrecords them, with the ruling that the corona and the streamer belt\nare one feature, and drafts for 1c, 1d and 1e to mark next session.\nTony's local folders: orrery\n"),
    ],
    'documentation/WORDS_L410_sun_fades_20261019.md': [
        ("<!-- Doc-Kind: hand | The words a visitor will read for the Sun's two fades (L-410 with L-131), revision 1, for Tony's review before the build. -->\n# Words: the Sun's corona and dust cloud, revision 2\n\n",
         "<!-- Doc-Kind: hand | The words a visitor will read for the Sun's two fades (L-410 with L-131), revision 1, for Tony's review before the build. -->\n# Words: the Sun's corona and dust cloud, revision 3\n\n"),
        ('\n## 4. The rows these words need (written at the build)\n',
         '\n## 5. Revision 3, from Tony\'s answers (2026-10-19, late)\n\nTony answered every item; his marks stay where he wrote them above. 2a,\nthe dust cloud\'s name, had no mark and is taken as "yes"; say if not.\n\n**Ruled.** The corona is ONE feature built from two drawings: the fade\nand the streamer belt, one name ("Corona"), one checkbox, one legend\nentry, one colour family, switched on and off together, with the hover\nexplaining that the belt is part of the corona. Tony: "yes, with the\nhover explaining." A single density model that varies with latitude\nwould merge them into one drawing; no open source for one has a stated\nrange, so that waits.\n\n**3c kept**, which answers the temperature question under "What goes":\nthe corona\'s one temperature is NASA\'s, up to about 2 million kelvin,\nfrom a row. The old "1 to 3 million", the wavelengths worked from it,\nand the dust-overtakes-electrons distance (sources range from 2.3 to 6\nsolar radii) stay out.\n\nDrafts for the next session, for Tony to mark there:\n\n**1c, one line added at the end of the hover.**\nThe streamer belt, drawn with it, is the part of the corona that the\nSun\'s magnetic field holds in loops over its magnetic equator.\n\n**1d, the sentence 3c adds at the end of the panel text.**\nThe corona is very hot, up to about {CORONA_TEMPERATURE_MAX_K} kelvin,\nfar hotter than the surface below it (NASA).\n\n**1e, reworded** (Tony\'s question: "how does the corona differ from\nthe streamer belt. this suggests they are connected." They are: the\nbelt is part of the corona).\nThe dots show the model\'s smooth average, drawn the same in every\ndirection. The real corona is shaped by the Sun\'s magnetic field. Over\nthe Sun\'s magnetic equator the field closes in loops that hold the gas\nin the helmets of the streamer belt, which reach about\n{HELMET_CUSP_LOW_RADII} to {HELMET_CUSP_HIGH_RADII} solar radii (Suess\nand Nerney, 2004) and are drawn with this one. The dots stop at the\nAlfven surface.\n\n**The streamer belt\'s own words** change too: today it is a separate\ncheckbox and entry. The build brings them as a list, with its seven\nnumbers set by eye (L-411), which come up when its shape is next\ntouched.\n\n## 4. The rows these words need (written at the build)\n'),
    ],
    'LEDGER_CONSOLIDATED.md': [
        ("    The words go to revision 2.\n**Gap (replaces the one above, 2026-10-19):** build the Sun's two fades\n",
         '    The words go to revision 2.\n  - **Tony\'s answers on the words, 2026-10-19 late** (in place in\n    `documentation/WORDS_L410_sun_fades_20261019.md`): every item yes but\n    two, discussed. On 1e, "how does the corona differ from the\n    streamer belt. this suggests they are connected": they are; the belt\n    is the part of the corona the magnetic field holds in loops. Then\n    Tony\'s question, "should we redraw the corona to include the\n    streamer belt as one feature rather than two", and on the\n    recommendation: "yes, with the hover explaining." So the corona is\n    ONE feature from two drawings (the fade and the streamer belt): one\n    name, one checkbox, one legend entry, switched together. Forward\n    scattering left out; the dust\'s origin kept; NASA\'s corona\n    temperature kept. Revision 3 holds the rulings and drafts for 1c,\n    1d and 1e, marked at the next session.\n**Gap (replaces the one above, 2026-10-19):** build the Sun\'s two fades\n'),
        ("  C wait for their own slice.\n**Gap:** groups T, M and C, the three leftovers above and the\nchromosphere's name, one shell at a time. Not part of the Sun's\nnumbers half, which ends with L-455.\n",
         '  C wait for their own slice.\n- **2026-10-19, Gemini 4\'s return** (high setting), reviewed in\n  `documentation/REVIEW_L411_gemini4_worksheet_20261019.md`. The\n  fourteen numbers held up; three rows it could not open stand on this\n  project\'s own reads. One real find, re-opened and confirmed: the\n  website\'s chromosphere sentence says "about 6,000 kelvin at the\n  bottom", but NASA\'s Sun Fact Sheet gives 4,400 K at the top of the\n  photosphere and about 30,000 K at the top of the chromosphere;\n  NASA/Marshall\'s 6,000 is degrees Celsius. New words to Tony. Sources\n  now opened for the held core and convection-zone temperatures\n  (Bahcall et al. 2001, Table 5 and sec. 3.3) and for Parker\'s first\n  crossing (Kasper et al. 2021: 28 April 2021, 19.7 to 18.4 solar radii\n  from the centre). Re-opening caught Gemini misquoting the Fact Sheet.\n**Gap:** the held sentences first, from Gemini 4\'s return (review\nabove): rows for the core\'s centre, the convection zone\'s base and\nParker\'s first crossing; new words for the chromosphere\'s temperature;\nthe chromosphere\'s name from its row. Then groups T, M and C, the three\nleftovers above, one shell at a time. Not part of the Sun\'s\nnumbers half, which ends with L-455.\n'),
    ],
}

NEW = {
    'documentation/REVIEW_L411_gemini4_worksheet_20261019.md': '<!-- Doc-Kind: hand | Review of Gemini 4\'s L-411 worksheet: the Sun\'s fourteen numbers re-checked, and the website\'s held Sun sentences searched; what it confirmed, found, held back and got wrong. -->\n# Review of Gemini 4\'s worksheet, L-411 (the Sun\'s numbers)\n\nBuilt on palomas_orrery 59e1b656c56ac38660f7943cae066513e9ab7b77 at\nhttps://github.com/tonylquintanilla/palomas_orrery and\ntonyquintanilla.github.io 4fc320fa6d2e0e10d9a50b8b69006cbff96a1364 at\nhttps://github.com/tonylquintanilla/tonyquintanilla.github.io.\nTony\'s local folders: orrery\nC:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\\ngallery\nC:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\\n\nWritten 2026-10-19 by Anthropic\'s Claude Opus 5.5. The worksheet is\n`documentation/worksheets/worksheet_gemini4_high_l411_sun_numbers_20261019.md`,\nnamed and saved by Tony. The prompt it answered is\n`documentation/prompts/RELAY_L411_gemini_sun_numbers_20261019.md`. The\nthird slice relay (provenance-cross-check 1.1).\n\n## In one sentence\n\nThe Sun\'s numbers held up; the one real find is that the website\'s\nchromosphere sentence gives its base as about 6,000 kelvin where the\nsources that speak in kelvin put it near 4,400.\n\n## Which model answered\n\nThe worksheet\'s header reads "Gemini (Task Mode / Gemini 4 Relay)",\neffort tier "High (Highest Thinking Setting)". Tony sent it as "response\nfrom Gemini 4" and named the file gemini4_high. Recorded as Gemini 4 at\nits highest thinking setting.\n\n## The citation rows: the fourteen numbers\n\nConfirmed with a quote and a locator: C1 (the core to 0.25 solar\nradii), C2 (0.713 +/- 0.003), C3 (100 km, from NASA/Marshall and the\nNSO), C4 (5,700 K), C6 (10 to 20 solar radii, heliocentric), C7 (94.01\nAU, through PubMed when ADS was blocked), C10 (80 to 100 AU, with the\narXiv HTML\'s section numbering noted), C11 (6.16 million km above the\nsurface; both named sources measure from the surface).\n\nHeld back, correctly, because a page would not open: C5 (the Montana\nState page), C8 and C9 (Li, Wang and Richardson\'s PDF). All three stand\non this project\'s own reads of 2026-10-17 and 18. For C8 it found 83.7\nAU in three other abstracts, which the row already records as Stone et\nal. (2008)\'s figure.\n\nTwo notes it raised, both definitions and not errors: other NASA pages\nput the photosphere at 400 to 500 km (measured to the temperature\nminimum, where ours measures the visible layer); and the chromosphere\'s\ndepth runs from 1,000 to 5,000 km across sources, the layer having no\nsharp top.\n\n## The discovery rows: the held sentences\n\nRe-opened here before anything is built on them:\n\n- **D3, the chromosphere: a real disagreement.** The website says the\n  temperature rises "from about 6,000 kelvin at the bottom to about\n  20,000 at the top". NASA/Marshall\'s page, re-opened, says "from\n  6000 degrees C to about 20,000 degrees C"; 6,000 degrees Celsius is\n  about 6,270 K. NASA\'s Sun Fact Sheet (D. R. Williams, last updated 9\n  May 2024), re-opened, gives "Temperature at top of photosphere:\n  4400 K" and "Temperature at top of chromosphere: ~30,000 K", with the\n  chromosphere "~2500 km" thick. So in kelvin the base is near 4,400\n  and the top tens of thousands. The sentence needs new words, which\n  are Tony\'s: they go on the next words list.\n- **Gemini misquoted the Fact Sheet.** It quoted "Temperature in\n  chromosphere: ~4300 - 8000 K" and a top of "~20,000 K", and an\n  effective-temperature line spelled "Surfaceura". The page, re-opened\n  twice, carries none of these: it says ~30,000 K at the top and has\n  no chromosphere range line. Its other quotes from that page match.\n  Recorded as an attribution error the re-open caught.\n- **D1, the core.** Bahcall, Pinsonneault and Basu (2001), arXiv\n  astro-ph/0010346, Table 5, re-opened: the standard model\'s centre at\n  15.696 (million K) and 152.7 g/cm3. The Fact Sheet, re-opened: 1.571\n  x 10^7 K and 162.2 g/cm3. Both support "about 15 million kelvin" and\n  "about 150 times as dense as water"; the Fact Sheet\'s density reads\n  nearer 160. A row for each can now be written.\n- **D2, the radiative zone.** Bahcall et al. (2001), same paper: the\n  temperature at the base of the convection zone today is 2.18 x 10^6\n  K, supporting "about 2 million at the top". The 7 million near the\n  core rests on NASA/Marshall and on Bahcall et al. (1995)\'s table\n  (7.9 million at 0.25 solar radii), the latter not re-opened.\n- **D4, Parker\'s crossing.** Kasper, Klein, Lichko and others,\n  "Parker Solar Probe Enters the Magnetically Dominated Solar Corona",\n  Phys. Rev. Lett. 127:255101 (2021), re-opened at the NSF\'s open copy\n  (par.nsf.gov/servlets/purl/10319180): at 09:33 UT on 28 April 2021,\n  13 million km above the photosphere, moving from 19.7 to 18.4 solar\n  radii from the Sun\'s centre (Table I: 19.8 to 18.4). This agrees with\n  ALFVEN_SURFACE_RADII, 19.7, and sources the sentence\'s "April 2021".\n  NASA\'s announcement says "18.8 solar radii ... above the solar\n  surface", which mixes centre and surface; the paper is the source.\n- **D5, the Hills cloud model.** Nesvorny et al., posted 16 February\n  2025, published ApJ 983:74; "inclined i ~ 30 degrees to the\n  ecliptic", nearly polar in the Galactic frame. Already the project\'s\n  cited source; the year can print from the citation.\n\n## How it did, against the rules\n\n- Header: model and setting given; rule files "not imported", said\n  plainly. Pre-flight quote given.\n- Quotes and locators on every row, one token per cell.\n- A long search log: 54 queries and the pages opened.\n- Held back on three pages it could not open, as UNVERIFIED.\n- One page misquoted (above), caught only by re-opening it. Its finds\n  on the other pages it quoted match where re-opened.\n\n## What it leaves for the next session\n\n- New words for the chromosphere\'s temperature sentence (D3), to Tony\n  as a list.\n- Rows for the core\'s centre (D1), the convection zone\'s base (D2) and\n  Parker\'s first crossing (D4), so those held sentences print from rows\n  and come off the website\'s held list.\n- The chromosphere\'s name prints its depth from its existing row.\n\nSession written October 2026 with Anthropic\'s Claude Opus 5.5.\n',
}


def main():
    out, crlf = {}, {}
    try:
        for rel, edits in ANCHOR.items():
            path = os.path.join(ROOT, rel)
            if not os.path.exists(path):
                raise RuntimeError('ERROR: %s not found. Save this script in the '
                                   'orrery folder.' % rel)
            with open(path, 'rb') as f:
                raw = f.read()
            crlf[rel] = b'\r\n' in raw
            text = raw.replace(b'\r\n', b'\n').decode('utf-8')
            for k, (old, new) in enumerate(reversed(edits), 1):
                n = text.count(old)
                if n != 1:
                    raise RuntimeError('ANCHOR FAIL: %s, edit %d from the bottom, '
                                       'found %d times: %r' % (rel, k, n, old[:70]))
                if any(ord(ch) > 127 for ch in new):
                    raise RuntimeError('ERROR: %s would gain non-ASCII text.' % rel)
                text = text.replace(old, new)
            out[rel] = text
        for rel, text in NEW.items():
            path = os.path.join(ROOT, rel)
            if os.path.exists(path):
                with open(path, 'rb') as f:
                    have = f.read().replace(b'\r\n', b'\n').decode('utf-8')
                if have != text:
                    raise RuntimeError('ERROR: %s already exists and differs.' % rel)
            crlf[rel] = False
            out[rel] = text
    except RuntimeError as e:
        print(e)
        print('NOTHING was written.')
        sys.exit(1)
    for rel, text in out.items():
        with open(os.path.join(ROOT, rel), 'w', encoding='utf-8', newline='') as f:
            f.write(text)
        print('ok  %s' % rel)
        if crlf[rel]:
            print('note: %s was CRLF in the working copy; written LF' % rel)
    print('patch applied (%d files).' % len(out))
    print('Next: the orrery maintenance run, then move both patch_L385_4 and')
    print('this script into documentation/, commit, push.')
    print('Undo is Discard Changes in GitHub Desktop.')


if __name__ == '__main__':
    main()
