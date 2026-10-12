"""patch_L401_2_design_close_20261011.py -- the close of the session of
2026-10-11: L-401 (the orrery's distance digits) promoted to next and
designed with three outside reviews, the typed sky-position table
settled with it; L-431 build 1 (orbital periods) recorded as working
against JPL.

Built on orrery 28a4636717920e86965f2e1777f3bf92386d1bb6 at
https://github.com/tonylquintanilla/palomas_orrery ("L431_4 _5 period in
hovers"). The gallery is not touched.
Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\;
gallery C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\.
Written October 11, 2026 with Anthropic's Claude Opus 5.5.

It replaces patch_L401_1_on_the_room_lists_20261011.py, which was never
run: delete that one. This patch refuses to run if it finds L-401's
earlier list wording already in the ledger.

HOW TO RUN
    From the orrery repo's ROOT folder: open it in VS Code and press Run,
    or from a terminal in that folder:
        python patch_L401_2_design_close_20261011.py
    Success prints one "ok" line per edit, then "patch applied".

WHAT IT CHANGES
    LEDGER_CONSOLIDATED.md -- header stamp; L-401 promoted and designed,
        with the typed sky-position table settled in it; L-431 build 1
        confirmed; L-399 (its route found); L-412 and L-413 (L-401
        first).
    documentation/WHERE_WE_ARE.md -- by section, never below the
        run-record marker: the date, the box, road stages 5 and 6a,
        Settled, Signals, Waiting on you, Where the details are.
    documentation/DESIGN_L401_distance_digits_rulings_20261011.md --
        created: the design record and session record.

SAFETY
    Each file is checked only at the lines this patch edits: every
    anchor must match exactly once, and no edit lands below the
    run-record marker. If any check fails, NOTHING is written. A file
    found with Windows line endings is matched after turning them into
    LF and written back LF, and the patch says so. Undo after a run is
    Discard Changes in GitHub Desktop (and delete the new record).
"""
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))

EDITS = [
    ('LEDGER_CONSOLIDATED.md', 'header stamp',
     'larger error; patch_L431_4; its record), built on 41e9a1d5.\nReview and RICE update Tony 6-21-2026\n',
     "larger error; patch_L431_4; its record), built on 41e9a1d5.\nModule updated: October 11, 2026 with Anthropic's Claude Opus 5.5\n(L-401 promoted to next and designed with three outside reviews, the\ntyped sky-position table settled with it; L-431 build 1 confirmed\nagainst JPL; L-399, L-412 and L-413 updated), built on 28a4636.\nReview and RICE update Tony 6-21-2026\n"),
    ('LEDGER_CONSOLIDATED.md', 'L-431 build 1 confirmed',
     "**Gap:** three builds, in order (the record's section 3):\n1. The period in the orrery: BUILT 2026-10-11. Waits for Tony's run\n   (its live check of four bodies) and his look at Encke, Sedna and\n   Mercury, where he approves the hover's words (the build record's\n   section 4).\n",
     '- **2026-10-11, build 1 confirmed working** (record:\n  `documentation/DESIGN_L401_distance_digits_rulings_20261011.md`,\n  section 7). Pushed at 28a4636. The patch\'s live check (Tony\'s copy\n  `documentation/WHERE_WE_ARE_10-11-26_1812_run_record.md`): Encke\'s\n  and Mercury\'s elements fetch and period query "agree"; 3I/ATLAS\n  "none (open orbit)". His plot saved records for Mercury (Sun, year\n  change 31 s), Sedna (barycentre, SBDB sigma 1,864 d) and Encke (Sun,\n  year change 0.15 d). Tony: "the orbital periods look reasonable".\n  His first screenshots showed the old hover only because the orrery\n  window was open before the patch ran.\n- **Found by Fable\'s review (L-401), 2026-10-11:** the hover\'s "JPL\n  lists no orbit uncertainty for this body" is false of JPL for a\n  planet; JPL states the planets\' accuracy in the 2014 report. Its\n  wording waits for Tony\'s word, with the rest of the hover\'s words.\n**Gap:** three builds, in order (the record\'s section 3):\n1. The period in the orrery: BUILT and working against JPL\n   (2026-10-11). Open: Tony\'s word on the hover\'s wording, with the\n   corrected sentence for a planet (L-401\'s design record, section 5).\n'),
    ('LEDGER_CONSOLIDATED.md', 'L-431 owed to the skill',
     "Owed to horizons-orbital-mechanics once Tony's run shows build 1\nworking against JPL:",
     "Owed to horizons-orbital-mechanics, now that build 1 works against JPL,\nin one version with L-401's method:"),
    ('LEDGER_CONSOLIDATED.md', 'L-401 date',
     '<!-- L:401 status:OPEN upd:2026-10-01 section:A flag: rice: -->',
     '<!-- L:401 status:OPEN upd:2026-10-11 section:A flag: rice: -->'),
    ('LEDGER_CONSOLIDATED.md', 'L-401 designed',
     "**Gap:** discovery first -- list every orrery site that prints a computed\ndistance, by function -- then fix in slices when the work reaches the\norrery's hovers.\n**Ref:** visualization_utils.py; formatting_utils.py; constants_new.py\n(DE430 rows); provenance-discipline 2.23; L-398.\n",
     '- **2026-10-11, promoted to next and designed** (record\n  `documentation/DESIGN_L401_distance_digits_rulings_20261011.md`).\n  Tony, after his look at L-431\'s hover: "the orbital periods look\n  reasonable, but not the distances"; then "It should be included as\n  part of the braid and theme work for the sun and earth rooms"; then\n  "actually, let\'s promote L401 to next. accuracy and precision are\n  fundamental. let\'s do it here. we have room." It goes first on\n  L-413 and L-412.\n- **Discovery done:** 376 fixed-width sites in 110 functions across 34\n  files, sorted by kind in the record\'s section 3. The first slice is\n  the body hover, `format_detailed_hover_text` and its two formatters.\n- **Three outside reviews** (Tony: "This is highly technical and my\n  instinct only partially helpful"): Claude Fable 5.1 and GPT-6 read\n  the rules at 28a4636 and opened their sources; Gemini 2.5 Pro\n  opened nothing, so its numbers are not used. Requests, returns and\n  the comparison: `documentation/REVIEW_L401_distance_digits_*`.\n- **Settled** by their agreement or an earlier ruling: the planets\n  keep the 2014 rows; the Moon gets a 1 metre row from the same\n  report; small bodies take JPL\'s own 3-sigma; a number with no\n  stated error prints to whole kilometres with a plain sentence, never\n  ten figures, and "no error" is its own state in the code; another\n  centre takes the larger error (Tony, 2026-10-01); every unit carries\n  the same error, placed by its own Report test.\n- **Fable\'s finding, re-run by Claude:** Horizons\' vector query with\n  `VEC_TABLE=\'2xr\'` returns a small body\'s 1-sigma position and\n  velocity uncertainties with the position (Sedna, 2026-10-12, from\n  the Sun: R_s 85,939.995 km; three times, 257,820 km, against\n  quantity 39\'s 257,817.569 km). No extra query; astroquery cannot\n  ask for it, so a direct call.\n- **Ruled 2026-10-11:** the speed ("Reading 1"): a small body\'s speed\n  by JPL\'s velocity uncertainties combined; any other body\'s to its\n  distance\'s relative precision, said in the box, with no separate\n  floor.\n- **The sky-position line, settled with this item** (Tony: "let\'s\n  follow Fable\'s recommendation", then "i think we should settle this\n  now too"). The hover prints a planet\'s RA and Dec "+/-0.005 arcsec,\n  JPL DE440/441 ephemeris" from `MAJOR_BODY_UNCERTAINTIES` in\n  `celestial_coordinates.py`, a typed table with no source line; the\n  DE440 paper gives no angular accuracy for a planet (read by GPT,\n  Fable and Claude). `get_precision_note` also prints ", typical"\n  fallbacks. Both come out; where Horizons gives no figure the line\n  says plainly that JPL gives none; the small bodies\' fetched 3-sigma\n  figures stay; the line says "as seen from Earth", since\n  `fetch_radec_for_hover` asks from Earth\'s centre (Fable). Kept for\n  later: Fable\'s sourced figure for a planet, worked out from its\n  position row and its distance from Earth.\n**Gap:** three questions at the next talk (the record\'s section 5):\nthe box\'s shape (one light-time line, the surface line only where the\ncentre has a surface, plain numbers); L-431\'s planet sentence; the\nspeed of a body whose distance has no stated error. Then the first\nbuild, the body hover, with the sky-position table\'s removal.\n**Ref:** `documentation/DESIGN_L401_distance_digits_rulings_20261011.md`;\n`documentation/REVIEW_L401_distance_digits_comparison_20261011.md`;\nvisualization_utils.py; formatting_utils.py; constants_new.py (DE430\nrows); palomas_orrery.py (`fetch_position`); provenance-discipline\n2.28; L-398; L-399; L-431; `celestial_coordinates.py`.\n'),
    ('LEDGER_CONSOLIDATED.md', 'L-399 route found',
     '**Gap:** with the near-Earth asteroid design.\n',
     "- **2026-10-11, the route found** under L-401: Horizons' vector query\n  with `VEC_TABLE='2xr'` returns a small body's position and velocity\n  uncertainties with the position (Fable, re-run by Claude). The\n  orrery builds it first (L-401); the website's builder can ask the\n  same way.\n**Gap:** with the near-Earth asteroid design; the route is L-401's.\n"),
    ('LEDGER_CONSOLIDATED.md', 'L-413 date',
     '<!-- L:413 status:OPEN upd:2026-10-06 section:A flag: rice: -->',
     '<!-- L:413 status:OPEN upd:2026-10-11 section:A flag: rice: -->'),
    ('LEDGER_CONSOLIDATED.md', 'L-413 L-401 first',
     '**Gap:** L-421 from its manifest; then the design talks in the order\nabove.\n',
     '- **Added 2026-10-11, first:** L-401, the orrery\'s distance digits.\n  Tony: "actually, let\'s promote L401 to next. accuracy and precision\n  are fundamental."\n**Gap:** L-401 first; then L-421\'s check; then the design talks in the\norder above.\n'),
    ('LEDGER_CONSOLIDATED.md', 'L-412 L-401 first',
     '**Gap:** after L-413, work down the list from item 3.\n',
     "- **Added 2026-10-11:** L-401 (the orrery's distance digits) goes\n  first, ahead of both lists, on Tony's word; worked once for both\n  rooms.\n**Gap:** after L-413, work down the list from item 3.\n"),
    ('documentation/WHERE_WE_ARE.md', 'header date',
     'Last updated: October 11, 2026, at build 1 of orbital periods.\n- Written at orrery 41e9a1d and gallery e3536c8.\n',
     'Last updated: October 11, 2026, at the L-401 design talk.\n- Written at orrery 28a4636 and gallery e3536c8.\n'),
    ('documentation/WHERE_WE_ARE.md', 'the box',
     "> - Orbital periods, build 1 is built: L-431 (orbital periods). The\n>   orrery's hovers show each body's period from JPL, the centre it\n>   was taken around, the date, and only the digits its errors earn.\n> - A period from the typed table now says it is typed.\n> - Nothing drawn moves yet. The orbits and markers are build 2.\n>\n> **Do next:** *your look at Encke, Sedna and Mercury, and your word\n> on the hover's wording (the build record, section 4).*\n>\n> **Needs you now:**\n> - *Orrery: patch_L431_4 (it asks JPL for four periods as it ends),\n>   patch_L431_5, maintenance run, your look, push.*\n",
     "> - Orbital periods, build 1 works against JPL: L-431 (orbital periods).\n> - L-401 (the distance digits) is next, by your word; three reviewers\n>   answered, most of it is settled. Speeds follow their distance's\n>   precision; the typed sky-position table comes out with it.\n>\n> **Do next:** *L-401's three last questions, then its first build:\n> the body hover.*\n>\n> **Needs you now:**\n> - *Orrery: delete patch_L401_1 (never run); run patch_L401_2,\n>   the maintenance run, push.*\n"),
    ('documentation/WHERE_WE_ARE.md', 'road stage 5',
     "  5.   [NOW]   *Earth's old items are finished, in your order.* The\n               website patch and Earth's typed facts are live.\n",
     "  5.   [NOW]   *L-401 (the distance digits) first, then Earth's\n               remaining items, in your order.* << moved this session\n"),
    ('documentation/WHERE_WE_ARE.md', 'road stage 6a',
     "  6a.  [next]  *Orbital periods from JPL: build 1, the orrery's hovers,\n               is built and waits for your look. Then the drawn\n               orbits, then the website.* << moved this session\n",
     '  6a.  [next]  Orbital periods from JPL: build 1 works; your word on\n               its words is open. Then the drawn orbits, then the\n               website.\n'),
    ('documentation/WHERE_WE_ARE.md', 'Settled',
     '## Settled\n\nStanding rulings. A line leaves after a few weeks, once it is habit.\n',
     "## Settled  **>> UPDATED THIS SESSION**\n\nStanding rulings. A line leaves after a few weeks, once it is habit.\n- Digits by the error JPL states; whole km and a plain sentence where it\n  states none; speeds to their distance's precision. (Oct 11)\n"),
    ('documentation/WHERE_WE_ARE.md', 'Signals',
     '  9802e04 (your run of 2026-10-11). Whole tree: 292.\n',
     '  28a4636 (your run of 2026-10-11). Whole tree: 292.\n'),
    ('documentation/WHERE_WE_ARE.md', 'Waiting mark',
     '## Waiting on you\n\nAt the next design talk:\n',
     "## Waiting on you  **>> UPDATED THIS SESSION**\n\nAt the next design talk:\n- L-401's three last questions (its record, section 5).\n"),
    ('documentation/WHERE_WE_ARE.md', 'Details',
     '- Your notes of Oct 11: `WHERE_WE_ARE_10-11-26_1311_run_record.md`\n',
     '- The distance digits: `DESIGN_L401_distance_digits_rulings_20261011.md`;\n  the reviews `REVIEW_L401_distance_digits_comparison_20261011.md`\n- Your notes of Oct 11: `WHERE_WE_ARE_10-11-26_1812_run_record.md`\n'),
    ('documentation/WHERE_WE_ARE.md', 'Details: Horizons check out',
     '- The Horizons check: design\n  `documentation/DESIGN_L395_horizons_check_20261007.md`; record\n  `documentation/HANDOFF_L395_horizons_check_build_20261010.md`\n',
     ''),
]

REC_NAME = 'documentation/DESIGN_L401_distance_digits_rulings_20261011.md'
REC = '<!-- Doc-Kind: hand | Design record for L-401 (the orrery\'s distance digits, printed by the errors JPL states): Tony\'s rulings of 2026-10-11, the discovery list, the three outside reviews and what they settled, the decisions still open, and the method the build follows. Zero code. Also the session record of build 1 of L-431 (orbital periods) working against JPL. -->\n# L-401 (the orrery\'s distance digits): the design talk\'s rulings\n\nBuilt on orrery 28a4636717920e86965f2e1777f3bf92386d1bb6 at\nhttps://github.com/tonylquintanilla/palomas_orrery ("L431_4 _5 period in\nhovers"); gallery e3536c8732d7b62faa5c09515e4b7f1d1c10af9c at\nhttps://github.com/tonylquintanilla/tonyquintanilla.github.io, read, not\ntouched.\nTony\'s local folders: orrery\n`C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\`;\ngallery `C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\`.\nWritten October 11, 2026 with Anthropic\'s Claude Opus 5.5.\n\n- Type: DESIGN SESSION (zero code), the second half of the session\n  that built L-431\'s first build.\n- Companions: the three review requests and returns, and their\n  comparison, in `documentation/` under `REVIEW_L401_distance_digits_*`.\n- Skills read this session, each matching the manifest:\n  ledger-and-session-records 1.20, horizons-orbital-mechanics 1.2,\n  provenance-discipline 2.28, provenance-cross-check 1.0,\n  orrery-coding-conventions 1.10, agentic-pre-test 1.3,\n  safe-file-editing 1.13. No skill version was cut.\n\n## 1. Read this first\n\n- *L-401 is next, by Tony\'s word.* It goes ahead of everything else on\n  the Sun\'s and Earth\'s lists.\n- *Most of the design is settled.* Three outside reviewers answered the\n  same nine questions; where they agreed, or an earlier ruling of\n  Tony\'s decides, it is settled (section 4).\n- *Two rulings tonight:* a speed with no stated accuracy is printed to\n  its distance\'s precision; the typed sky-position table comes out,\n  settled now as part of this item.\n- *Still open:* three small decisions (section 5), then the first\n  build, the body hover.\n\n## 2. Tony\'s words, in order\n\n1. On seeing L-431\'s hover beside the distances: "the orbital periods\n   look reasonable, but not the distances."\n2. "It should be included as part of the braid and theme work for the\n   sun and earth rooms."\n3. "actually, let\'s promote L401 to next. accuracy and precision are\n   fundamental. let\'s do it here. we have room."\n4. "let\'s talk this through instead of a questionnaire. this is not\n   simple."\n5. "Please prepare and request to Fable and GPT and Gemini for their\n   opinions. This is highly technical and my instinct only partially\n   helpful."\n6. On the speed: "Meters per second suggests precision limited by\n   distance", then, offered two readings, "Reading 1": the speed\'s\n   precision follows from the distance\'s, with no separate floor.\n7. On the sky-position table: "let\'s follow Fable\'s recommendation."\n   Then, having misread the question: "i think we should settle this\n   now too" -- with this item, not as one of its own.\n\n## 3. Discovery: where the orrery prints a computed number\n\nA search of every module for a fixed-width number printed beside a\nunit, and for the two shared formatters, found 376 sites in 110\nfunctions across 34 files. By kind:\n\n- The body hover, the first slice: `visualization_utils.format_detailed_hover_text`\n  and its two formatters in `formatting_utils.py`, ten decimal places\n  of an AU and ten significant figures of a kilometre. One function\n  builds it for the static plot, the animation and the social export.\n- Its sky-position line: `celestial_coordinates.py`,\n  `MAJOR_BODY_UNCERTAINTIES` and `get_precision_note` (settled with\n  this item, section 5).\n- Markers on the plot: `apsidal_markers.py` (perihelion, aphelion,\n  Kepler position, closest approach, encounters) and the\n  closest-plotted-point hovers. Their dates ride L-431\'s build 2.\n- Orbit hovers: `idealized_orbits.py`, 16 functions.\n- Encounters and close approaches: `spacecraft_encounters.py`,\n  `close_approach_data.py`.\n- The fly-to buttons and the parameters window.\n- Not this item: shells (store rows, already under the Figures rule),\n  the stars (`sgr_a_*`, `exoplanet_*`), console prints.\n\n## 4. Settled, by the reviews\' agreement or an earlier ruling\n\nPresented to Tony as settled on 2026-10-11; he went on to the open\nquestions. The evidence for each is in the comparison file.\n\n1. **Planets and Pluto** keep the three 2014 rows (Folkner et al.,\n   DE430). The 2021 DE440 paper gives fit residuals, not position\n   accuracy, and says Uranus and Neptune are "statistically consistent\n   with DE430" (read by GPT, Fable and Claude).\n2. **The Moon** gains a row from the same 2014 report: "The present-day\n   lunar orbit is known to submeter accuracy", stored as its place, 1\n   metre (Fable; the build reads it before writing the row).\n3. **Small bodies** take JPL\'s own 3-sigma uncertainty. Fable found,\n   and Claude re-ran, that Horizons\' vector query with\n   `VEC_TABLE=\'2xr\'` returns the 1-sigma position and velocity\n   uncertainties with the position itself. Sedna from the Sun,\n   2026-10-12: R_s 85,939.995 km; three times that is 257,820 km,\n   against quantity 39\'s 257,817.569 km.\n4. **No stated error** (the planets\' moons in a planet-centred plot,\n   spacecraft, Lagrange points, barycentres, the Sun as a body): print\n   to whole kilometres, the website\'s floor, with a plain sentence that\n   JPL states no accuracy for it. Never ten figures; never a dropped\n   line. "No error" is its own state in the code, never a tiny invented\n   one. A moon in a Sun-centred plot uses its planet\'s row as a floor\n   (Fable).\n5. **The level is 3-sigma**, and the box says in words which kind of\n   figure it is: a published accuracy for the planets, a computed one\n   for the date for a small body.\n6. **Another centre:** the larger of the two bodies\' errors (Tony\'s\n   ruling of 2026-10-01, "use whichever is larger").\n7. **Units:** AU, kilometres and light time carry the same error, each\n   placed by its own Report test.\n\n## 5. Ruled tonight, and still open\n\nRuled:\n- **The speed** (Tony, "Reading 1"): a small body\'s speed uses JPL\'s\n  velocity uncertainties, combined into one bound (Fable). Any other\n  body\'s speed is printed to the same relative precision as its\n  distance, and the box says so. No separate metres-per-second floor.\n  This can ADD digits: Mercury\'s speed earns about 41.92415 km/s.\n- **The sky-position table** (Tony, "follow Fable\'s recommendation",\n  then "settle this now too"): the typed values come out, with the\n  ", typical" fallbacks; the line says JPL gives no uncertainty where it\n  gives none, and says "as seen from Earth". Part of this item, in its\n  first build, since that build opens the same hover. Kept for later:\n  Fable\'s sourced figure for a planet, from its position row and its\n  distance from Earth.\n\nOpen, one at a time at the next talk:\n1. The box\'s shape: one light-time line (light-minutes under an hour,\n   light-hours above); the surface line only where the centre has a\n   surface; plain numbers, no scientific notation. All three reviewers\n   proposed these.\n2. L-431 build 1\'s sentence "JPL lists no orbit uncertainty for this\n   body", which Fable shows is false of JPL for a planet; with Tony\'s\n   word on the period hover\'s wording as a whole.\n3. The speed of a body whose distance has no stated error (moons\n   seen from their planet, spacecraft): Reading 1 gives it nothing to\n   follow. The floor with a sentence, as for its distance, is the\n   obvious candidate.\n\n## 6. Method the build follows (not Tony\'s; recorded so it is not re-asked)\n\n- Small bodies\' positions are fetched with `VEC_TABLE=\'2xr\'`, by a\n  direct call to the Horizons API: astroquery 0.4.11 cannot ask for it\n  (its request sets no VEC_TABLE). Columns are read by name (R_s, VR_s,\n  VT_s, VN_s), never by position. No extra query.\n- The sigma level is written into every field name (`range_3sigma_km`).\n- An error is keyed by body, centre and date.\n- Gemini\'s suggestion to fold quantity 39 into the existing sky-position\n  query would give the range from Earth, not from the plot\'s centre:\n  not used.\n- Owed to horizons-orbital-mechanics at L-401\'s build, in one version\n  with what L-431 owes it: the vector-table uncertainties and the\n  astroquery limit; the two-centre test and its saved choice; SBDB\'s\n  lookup of a pinned record by Horizons\' name.\n\n## 7. L-431 build 1, confirmed working\n\n- Tony ran `patch_L431_4` and `_5` on 2026-10-11 and pushed them at\n  28a4636. The patch\'s live check (his copy\n  `documentation/WHERE_WE_ARE_10-11-26_1812_run_record.md`) asked JPL\n  for four bodies: Encke\'s and Mercury\'s elements fetch and period\n  query "agree"; 3I/ATLAS "none (open orbit)".\n- His plot at 19:41 UTC saved period records for Mercury (around the\n  Sun, its year change 31 seconds), Sedna (around the barycentre,\n  JPL\'s uncertainty 1,864 days) and Encke (around the Sun, year change\n  0.15 days). Tony: "the orbital periods look reasonable".\n- His first screenshots showed the old hover because the orrery window\n  was open before the patch ran; reopening it fixed that.\n\n## 8. Tony-actions\n\n- (do) Delete `patch_L401_1_on_the_room_lists_20261011.py` from the\n  orrery folder. It was never run, and it put L-401 after L-421.\n- (do) Run `patch_L401_2_design_close_20261011.py`, then\n  `orrery_maintenance_run.py`; move the patch into `documentation/`;\n  commit and push. The review files are already in `documentation/`.\n- (decide, at the next talk) Section 5\'s three open questions.\n\nSession record written October 2026 with Anthropic\'s Claude Opus 5.5.\n'


MARKER = '--- Your run record below this line'


def main():
    rpath = os.path.join(ROOT, REC_NAME)
    if os.path.exists(rpath):
        print('ERROR: %s already exists; this patch has run. NOTHING was written.' % REC_NAME)
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
            if f == 'LEDGER_CONSOLIDATED.md' and 'On the room lists, 2026-10-11' in texts[f]:
                print('ERROR: patch_L401_1 has already run on this ledger. Discard its '
                      'changes in GitHub Desktop first. NOTHING was written.')
                sys.exit(1)
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
    with open(rpath, 'wb') as fh:
        fh.write(REC.encode('utf-8'))
    print('ok  %-34s created' % REC_NAME)
    print()
    print('patch applied')
    print()
    print('NEXT:')
    print('  1. Delete patch_L401_1_on_the_room_lists_20261011.py (never run).')
    print('  2. Run orrery_maintenance_run.py -- it rebuilds the ledger\'s index.')
    print('  3. Move this script into documentation/; commit and push.')


if __name__ == '__main__':
    main()
