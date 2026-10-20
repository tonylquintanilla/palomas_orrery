#!/usr/bin/env python3
"""
patch_L385_4_close_20261019.py -- closes L-385 (the opening views) on
Tony's look, and records the push in Where We Are and the handoff.

Built on orrery 59e1b656c56ac38660f7943cae066513e9ab7b77 at
https://github.com/tonylquintanilla/palomas_orrery ("v3.104"). The
website is not touched (gallery 4fc320fa at
https://github.com/tonylquintanilla/tonyquintanilla.github.io).
Tony's orrery folder:
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\
Written October 19, 2026 with Anthropic's Claude Opus 5.5.

RUN COMMAND

    python patch_L385_4_close_20261019.py

    Saved in the ORRERY folder above. Open it in VS Code and click Run.
    It takes no arguments and asks no questions.

WHAT IT DOES, all or nothing, checking only the lines it changes, so
your notes elsewhere are kept:

    LEDGER_CONSOLIDATED.md     L-385 DONE, with your looks and the push;
                               L-411 records the Gemini prompt;
                               the next ledger run moves it to the
                               closed section
    documentation/WHERE_WE_ARE.md   the box and the road: the opening
                               views done; next, the fades
    documentation/HANDOFF_L385_opening_views_20261019.md   "pushed at",
                               and the new Gemini prompt
    documentation/prompts/RELAY_L411_gemini_sun_numbers_20261019.md
                               new: the Sun's numbers, for Gemini 4

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
    'LEDGER_CONSOLIDATED.md': [
        ("  check marks it no longer found and it comes off HELD in the same\n  patch.\n**Gap:** groups T, M and C, the three leftovers above and the\nchromosphere's name, one shell at a time. Not part of the Sun's\n",
         '  check marks it no longer found and it comes off HELD in the same\n  patch.\n- **2026-10-19, an outside check asked for** (Tony: "are there any\n  already approved words that would benefit from a cross check or\n  words that we omitted from lack of sources where Gemini 4 could\n  help?"). The Sun\'s fourteen numbers of 2026-10-17 and 18 had one\n  reader only. A slice relay (provenance-cross-check 1.1):\n  `documentation/prompts/RELAY_L411_gemini_sun_numbers_20261019.md`,\n  eleven citation rows (those numbers) and five discovery rows (the\n  core\'s, the radiative zone\'s and the chromosphere\'s held temperatures\n  and density, Parker\'s 2021 crossing of the Alfven surface, the Hills\n  cloud model\'s year). The chromosphere\'s name already has a row and\n  needs printing from it, not a source. The orrery-only groups T, M and\n  C wait for their own slice.\n**Gap:** groups T, M and C, the three leftovers above and the\nchromosphere\'s name, one shell at a time. Not part of the Sun\'s\n'),
        ('\n#### [L-385] The orrery\'s Auto view of the Sun opens about 31 times wider since Stage D (orrery, Tony\'s eye)\n<!-- L:385 status:OPEN upd:2026-10-19 section:A flag: rice: -->\n**Tony:** (on Where We Are, 2026-09-30, how wide the Sun\'s opening view\nis in the orrery) "photosphere + 10%"\n',
         '\n#### [L-385] The orrery\'s Auto view of the Sun opens about 31 times wider since Stage D (orrery, Tony\'s eye)\n<!-- L:385 status:DONE upd:2026-10-19 section:C flag: rice: -->\n**Tony:** (on Where We Are, 2026-09-30, how wide the Sun\'s opening view\nis in the orrery) "photosphere + 10%"\n'),
        ("  - The rule is in orrery-coding-conventions 1.11, The Opening View\n    (protocol v3.104).\n**Gap (replaces the one above, 2026-10-19):** Tony's look at patch 2:\nthe Sun with only the photosphere and\nEarth plotted, still and animated; then the push. Close on that look.\n**Ref:** `documentation/HANDOFF_L322_D_orrery_pole_built_20260924.md` sec. 3; L-322;\n`documentation/HANDOFF_L385_opening_views_20261019.md`.\n",
         '  - The rule is in orrery-coding-conventions 1.11, The Opening View\n    (protocol v3.104).\n- **DONE 2026-10-19,** on Tony\'s runs and look, in his run record\n  (`documentation/WHERE_WE_ARE_10-18-26_1326_run_record.md`, session of\n  10-19): patch 2 applied (2 files); the Sun with the photosphere and\n  Earth plotted, still and animated, and Earth with its crust and the\n  Moon: "perfect"; patch 3 applied (14 files); the orrery run 31 of 31\n  gating, gate 0 Tier-1, whole tree 284 with the three patch scripts\n  still in the root (2 each, dev tools), 280 once moved; the two skills\n  reinstalled. Pushed at orrery e2a3465b99d552bb0d2bd3cf1ecbd987ddbe482c\n  ("L385 L456 L410"), then 59e1b656 ("v3.104", the protocol\'s archived\n  copy). The next session confirms its loaded copies read\n  orrery-coding-conventions 1.11 and provenance-cross-check 1.1.\n- **Loose end re-homed** (A Closing Item Re-homes Its Loose Ends): the\n  handoff\'s note that, when orbits widen the final view, the Sun\n  direction arrow keeps the length it was given inside the shells\' view\n  and can read short. It stays inside the view, and Tony\'s look at\n  that view read "perfect"; recorded here so a later look that finds\n  it short knows where it comes from. Nothing is open on it.\n**Gap:** none. Closed.\n**Ref:** `documentation/HANDOFF_L322_D_orrery_pole_built_20260924.md` sec. 3; L-322;\n`documentation/HANDOFF_L385_opening_views_20261019.md`.\n'),
    ],
    'documentation/WHERE_WE_ARE.md': [
        ('# Where We Are\n\nLast updated: October 19, 2026: the opening views built; the Sun\'s two fades designed.\n- Written at orrery 6e0cfac and gallery 4fc320f.\n\n> **READ THIS FIRST**\n>\n> **Changed since you last read this:**\n> - The opening views (L-385): the Sun and Earth now open on their\n>   farthest shell plus 20%; your look: "perfect".\n> - Patch 2 makes every view do it, still and animated, orbits included.\n> - The Sun\'s fades are designed (L-410, L-131 (the dust cloud)): the\n>   corona as one plasma fade, the dust as its own cloud of dots.\n>\n> **Do next:** *run patch 2, look at the Sun with Earth plotted, then\n> the records patch: the handoff\'s run order, section 1.*\n>\n> **Needs you now:**\n> - Your look at patch 2 closes L-385 (the opening views).\n> - The fades\' words, revision 2, when you have time: answer in place.\n\n*Italic* lines are the must-reads. Marks reset at every update.\n',
         '# Where We Are\n\nLast updated: October 19, 2026, evening: the opening views done and pushed; the Sun\'s two fades designed.\n- Written at orrery 59e1b65 and gallery 4fc320f.\n\n> **READ THIS FIRST**\n>\n> **Changed since you last read this:**\n> - The opening views (L-385) are done and pushed: every view opens on\n>   the farthest thing drawn plus 20%, still and animated; your looks:\n>   "perfect", twice.\n> - The Sun\'s fades are designed (L-410, L-131 (the dust cloud)): the\n>   corona as one plasma fade, the dust as its own cloud of dots.\n>\n> **Do next:** *the Sun\'s two fades (L-410, the corona; L-131, the\n> dust cloud), built from your answers on the words list.*\n>\n> **Needs you now:**\n> - The fades\' words, revision 2, before that build: answer in place in\n>   `WORDS_L410_sun_fades_20261019.md`, section 3 especially.\n\n*Italic* lines are the must-reads. Marks reset at every update.\n'),
        ("               orbital periods from JPL, orrery and website (Oct 14).\n  7.   [NOW]   *The Sun's slice (L-412): numbers done (Oct 18); the\n               opening views built (Oct 19); next, the two fades as\n               designed; the ice lines wait.* << moved this session\n  8-8c.[done]  The served objects checked against JPL, missing periods\n",
         "               orbital periods from JPL, orrery and website (Oct 14).\n  7.   [NOW]   *The Sun's slice (L-412): numbers done (Oct 18); the\n               opening views done (Oct 19); next, the two fades as\n               designed; the ice lines wait.* << moved this session\n  8-8c.[done]  The served objects checked against JPL, missing periods\n"),
        ("Read from files when this page was written, not typed from memory.\n- Last cache build: 20261019T132346Z, ok, every rename on the first try (gallery 4fc320f).\n- Tier-1 on the gate path: 0, by name (PROVENANCE_AUDIT.md, on the\n  patched copy of 6e0cfac). Whole tree: 280: orrery 116, Earth System\n  149, stars 13, utilities 2.\n- This page's date and the ledger's newest stamp: both Oct 19. Agree.\n\n",
         "Read from files when this page was written, not typed from memory.\n- Last cache build: 20261019T132346Z, ok, every rename on the first try (gallery 4fc320f).\n- Tier-1 on the gate path: 0, by name (the scanner at 59e1b65).\n  Whole tree: 280: orrery 116, Earth System 149, stars 13, utilities 2.\n- This page's date and the ledger's newest stamp: both Oct 19. Agree.\n\n"),
        ("\n- Every item: `LEDGER_CONSOLIDATED.md`.\n- *Next: `HANDOFF_L385_opening_views_20261019.md`, sec. 1 (your run order)*\n- The Sun's fades, designed: `SOURCES_L410_sun_corona_dust_20261019.md`;\n  their words for your review: `WORDS_L410_sun_fades_20261019.md`\n",
         "\n- Every item: `LEDGER_CONSOLIDATED.md`.\n- *Next: the fades; start from `HANDOFF_L385_opening_views_20261019.md`, sec. 6*\n- The Sun's fades, designed: `SOURCES_L410_sun_corona_dust_20261019.md`;\n  their words for your review: `WORDS_L410_sun_fades_20261019.md`\n"),
    ],
    'documentation/HANDOFF_L385_opening_views_20261019.md': [
        ('numbers") and gallery 4fc320fa6d2e0e10d9a50b8b69006cbff96a1364 at\nhttps://github.com/tonylquintanilla/tonyquintanilla.github.io ("daily\nrun 10-19-26"). Nothing pushed by this session; Tony pushes. The\nwebsite is not touched.\nTony\'s local folders: orrery\nC:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\\n',
         'numbers") and gallery 4fc320fa6d2e0e10d9a50b8b69006cbff96a1364 at\nhttps://github.com/tonylquintanilla/tonyquintanilla.github.io ("daily\nrun 10-19-26"). Pushed at orrery\ne2a3465b99d552bb0d2bd3cf1ecbd987ddbe482c ("L385 L456 L410") and\n59e1b656c56ac38660f7943cae066513e9ab7b77 ("v3.104"); every step in\nsection 1 done, Tony\'s looks "perfect" (his run record,\n`WHERE_WE_ARE_10-18-26_1326_run_record.md`, session of 10-19); L-385\nDONE. The website is not touched. Added at the close: a Gemini prompt\nfor the Sun\'s numbers,\n`prompts/RELAY_L411_gemini_sun_numbers_20261019.md` (L-411); carry it\nto Gemini 4 Argon at its highest thinking level, and save the worksheet\nin `documentation/worksheets/`.\nTony\'s local folders: orrery\nC:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\\n'),
    ],
}

NEW = {
    'documentation/prompts/RELAY_L411_gemini_sun_numbers_20261019.md': '<!-- Doc-Kind: hand | Relay prompt for Gemini 4: an outside check of the Sun\'s numbers rows (L-412) and a search for the sentences the website still holds without a source (L-411). Copy everything below the line into Gemini. -->\n# Relay prompt for Gemini 4 -- the Sun\'s numbers (L-411, L-412)\n\nWritten 2026-10-19 by Anthropic\'s Claude Opus 5.5 for Tony to carry to\nGemini 4. Copy everything below the line. Choose Gemini 4 Argon in the\nmodel menu and, under Thinking level, the highest setting offered: the\ndiscovery rows are only as good as how long the checker keeps looking.\nAsk it to name the model and setting your screen shows.\n\n---\n\nBuilt on palomas_orrery 59e1b656c56ac38660f7943cae066513e9ab7b77 at\nhttps://github.com/tonylquintanilla/palomas_orrery and\ntonyquintanilla.github.io 4fc320fa6d2e0e10d9a50b8b69006cbff96a1364 at\nhttps://github.com/tonylquintanilla/tonyquintanilla.github.io. The\ncitation rows below ARE in the orrery\'s constants_new.py at that\ncommit, and are served on the website\'s Sun room; every value you need\nis written out here anyway.\nVocabulary: v2 (2026-08-13)\n\n## Who you are working for\n\nTony Quintanilla, PE, a retired civil and environmental engineer, builds\nPaloma\'s Orrery, a 3D astronomy visualization (a desktop program and the\nwebsite palomasorrery.com), through conversation with AI partners. He is\nnot a professional programmer or astronomer. Every number a visitor\nreads must come from a source anyone can open. Please write plainly.\n\n## What this job is\n\nThe website\'s Sun room prints numbers about the Sun\'s layers. Fourteen\nof them were sourced on 2026-10-17 and 18, each read by one model\n(Claude) from the open source named below. No second reader has\nre-opened them: that is the citation half. Separately, five sentences\nthe room still shows carry a typed number with no source the project\nhas stored for it: that is the discovery half.\n\n## The rules this job follows\n\nIf you have imported the palomas_orrery repository, read these two\nfiles and name them at the top of your answer:\n\n- skills/provenance-discipline/SKILL.md -- sections The Access Standard\n  and What a Visitor Reads\n- skills/provenance-cross-check/references/worksheets.md -- section\n  Worksheet Types\n\nIf you have not imported it, say so; the rules you need are restated\nhere:\n\n1. **Open sources only.** A source counts only if its text can be read\n   without a paywall: open full text, a free abstract that states the\n   claim, an agency page or document, an arXiv preprint. A source\n   behind a paywall does not count, whatever its authority.\n2. **Name what you opened.** Give the title and authors as printed in\n   the document you actually opened, not a paper it cites.\n3. **Quote it.** Every row needs a short verbatim quote from the source\n   containing the figure or statement, and a locator (section,\n   equation, table, page, or the exact URL). A row without both is\n   recorded as UNVERIFIED whatever its verdict says. If you are\n   recalling rather than reading, say so and leave the row UNVERIFIED.\n   Silence is better than a guess.\n4. **Temperatures are stored in kelvin.** If a source gives degrees\n   Celsius, report the figure exactly as the source prints it; the\n   conversion is ours.\n5. **Prefer an agency or a peer-reviewed paper** (NASA, ESA, an open\n   journal article or arXiv preprint) over an educational or news page.\n   Say which kind each source is.\n\n## Before any row: a pre-flight\n\nOpen this page and quote one sentence from it, so we know your fetching\nworks:\n\n```\nhttps://arxiv.org/abs/2202.11533\n```\n\n## Your answer\'s header\n\nStart with one line naming your MODEL and your EFFORT TIER, then the\nlist of rule files you read (or "not imported").\n\n## The two kinds of row\n\n[CITATION] -- the row names a source. Open it and confirm it states the\nfigure or statement, at the figure\'s precision. Then, separately, check\nthe value against one other open source of your own choosing,\npreferably an agency or a paper.\n\n[DISCOVERY] -- the claim may have no source at all. Do not assume one\nexists, and do not reconcile it with any other row. Find whether an\nopen source states it. UNSOURCED is a valid and useful answer, but a\nnegative must show its search: list the queries you actually ran and\nthe places you looked, in a SEARCH LOG under the table. A negative with\nno search log is recorded as UNVERIFIED.\n\n## The table\n\nOne row per numbered item below, in this exact layout:\n\n| # | Job | Claim | Code value | Your value | Source unit | Source (URL opened, access word) | Value correct? | Citation correct? | Read by | Quote | Locator | Notes |\n\n- **Read by**: who opened the source -- your model name.\n- **Access word**: one of open full text, abstract, agency page, open\n  document, educational page, news page.\n- Each verdict cell holds EXACTLY ONE token, and the tokens belong to\n  their column:\n\n```\nValue correct?     YES  NO  APPROX  UNVERIFIED\nCitation correct?  YES  NO  PARTIAL  DERIVED  UNSOURCED  UNVERIFIED\n```\n\n  APPROX qualifies a value (right to a stated tolerance; say the\n  tolerance in Notes). PARTIAL qualifies a citation (the source supports\n  part of the claim). UNSOURCED means the named source does not publish\n  the figure at all; NO means it publishes a different one. For a\n  DISCOVERY row, "Citation correct?" answers whether the source you\n  found states the claim.\n\n- Put every URL as a bare address inside a code block, after the table,\n  numbered by row. Links pasted as chips lose their address.\n- Please deliver the whole answer as a downloadable Markdown file named\n  worksheet_gemini4_<effort tier>_L411_sun_numbers_20261019.md, as well\n  as in the chat.\n\n## The rows\n\n### Citation rows (a source is named)\n\nC1. The Sun\'s core, where energy is generated, reaches out to about 25\npercent of the distance from the centre to the surface (0.25 solar\nradii). Source named: D. H. Hathaway, NASA/Marshall Solar Physics, "The\nSolar Interior". https://solarscience.msfc.nasa.gov/interior.shtml\n\nC2. The radiative zone\'s outer edge (the base of the convection zone)\nis at 0.713 +/- 0.003 solar radii. Source named: Delahaye and\nPinsonneault, "The Solar Heavy Element Abundances: I. Constraints from\nStellar Interiors", arXiv:astro-ph/0511779, sec. 2.2, which quotes the\n1991 estimate (Christensen-Dalsgaard, Gough and Thompson, ApJ 378:413)\nbeside Basu and Antia\'s 0.7133 +/- 0.0005.\nhttps://arxiv.org/abs/astro-ph/0511779\n\nC3. The photosphere is a layer about 100 km thick. Source named:\nHathaway, NASA/Marshall, "The Photosphere".\nhttps://solarscience.msfc.nasa.gov/surface.shtml\n\nC4. At the visible surface the temperature has dropped to 5,700 K.\nSource named: Hathaway, NASA/Marshall, "The Solar Interior" (as C1).\n\nC5. The chromosphere is a layer of gas approximately 2,000 km thick.\nSource named: Yohkoh Public Outreach Project, Montana State University,\n"A \'Dancing\' Layer of the Sun".\nhttps://solar.physics.montana.edu/YPOP/Spotlight/SunInfo/Chromosph.html\nPlease also report what NASA\'s 2017 eclipse page gives (we read about\n5,000 km there): https://science.gsfc.nasa.gov/attic/eclipse2017.gsfc.nasa.gov/chromosphere.html\n\nC6. The Alfven surface spends most of its time between about 10 and 20\nsolar radii from the Sun\'s centre. Source named: Cranmer et al.\n(2023), "The Sun\'s Alfven Surface: Recent Insights and Prospects for\nthe Polarimeter to Unify the Corona and Heliosphere (PUNCH)", arXiv\n2310.05887, abstract. https://arxiv.org/abs/2310.05887\n\nC7. Voyager 1 crossed the termination shock on 16 December 2004 at\n94.01 AU. Source named: Stone et al. (2005), "Voyager 1 explores the\ntermination shock region and the heliosheath beyond", Science 309,\n2017, abstract at NASA ADS.\nhttps://ui.adsabs.harvard.edu/abs/2005Sci...309.2017S/abstract\n\nC8. Voyager 2 reached the termination shock in August 2007 at about\n83.6 AU. Source named: Li, Wang and Richardson (2008), "Properties of\nthe termination shock observed by Voyager 2", GRL 35:L19107, abstract.\nhttps://www.spaceweather.ac.cn/~hli/papers/Li%20et%20al%202008%20GRL%20Properties%20of%20the%20termination%20shock%20observed%20by%20Voyager%202.pdf\n\nC9. At Voyager 2\'s first crossing the solar wind\'s radial speed\naveraged 321.01 +/- 2.84 km/s upstream and 184.67 +/- 23.38 km/s\ndownstream. Source named: as C8, Table 1, shock 1.\n\nC10. The termination shock lies between 80 and 100 AU from the Sun.\nSource named: Treumann and Jaroschek, "The Heliospheric Termination\nShock", arXiv 0807.4170, secs. V.A and V.D.2.\nhttps://arxiv.org/abs/0807.4170\n\nC11. Parker Solar Probe\'s closest approach is 6.16 million km above the\nSun\'s surface (3.83 million miles), reached on 24 December 2024.\nSources named: Johns Hopkins APL, Parker Solar Probe, "The Mission",\nhttps://parkersolarprobe.jhuapl.edu/The-Mission/index.php ; and NASA\nScientific Visualization Studio 14741, https://svs.gsfc.nasa.gov/14741/\nPlease say whether each source gives the distance above the surface or\nfrom the Sun\'s centre.\n\n### Discovery rows (sentences the website shows with no stored source)\n\nFor each, find an open source, preferably an agency page or a\npeer-reviewed paper, that states the figure; quote it; and give the\nfigure in kelvin if the source does (if it gives degrees Celsius,\nreport it exactly as printed). Report every figure you find; do not\naverage them.\n\nD1. The core: "about 15 million kelvin at the very center, where the\ngas is about 150 times as dense as water". (Hathaway\'s interior page,\nC1, is known to say about 15,000,000 degrees C and about 150 g/cm3 at\nthe centre; find a second open source, ideally a standard solar model\npaper that tabulates the central temperature and density.)\n\nD2. The radiative zone: temperatures "fall from about 7 million kelvin\nnear the core to about 2 million at the top of the zone". (Hathaway\'s\ninterior page is known to say 7,000,000 to about 2,000,000 degrees C;\nfind a second open source, ideally a model or a helioseismology paper.)\n\nD3. The chromosphere: its temperature "rises with height, from about\n6,000 kelvin at the bottom to about 20,000 at the top". (Hathaway\'s\nchromosphere page, https://solarscience.msfc.nasa.gov/chromos.shtml ,\nis known to say 6000 degrees C to about 20,000 degrees C; note that\n6,000 degrees C is about 6,270 K, so please look for a source that\nstates the bottom temperature in kelvin, for example the temperature\nminimum at the top of the photosphere.)\n\nD4. "NASA\'s Parker Solar Probe crossed this boundary [the Alfven\nsurface] in April 2021, the first spacecraft to fly inside the corona."\nFind NASA\'s announcement or the paper reporting the crossing, with its\ndate and the distance at which it happened.\n\nD5. "A 2025 computer model finds instead a slightly warped disk tilted\nabout 30 degrees to the ecliptic, nearly at right angles to the plane\nof the Milky Way" (the Hills cloud, the inner Oort cloud). The project\ncites Nesvorny et al., arXiv 2502.11252. Confirm the year it was posted\nor published, and the tilt it states.\nhttps://arxiv.org/abs/2502.11252\n\n## What not to do\n\n- Do not propose wording for the website.\n- Do not combine rows, or reconcile one row\'s figure with another\'s.\n- Do not fill a cell from memory. If you could not open a source, the\n  cell is UNVERIFIED and Notes says what stopped you.\n',
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
    print('Next: the orrery maintenance run (it moves L-385 to the closed')
    print('section), move this script into documentation/, commit, push.')
    print('Undo is Discard Changes in GitHub Desktop.')


if __name__ == '__main__':
    main()
