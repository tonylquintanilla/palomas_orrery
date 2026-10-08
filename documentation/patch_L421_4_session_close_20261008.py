#!/usr/bin/env python3
"""
patch_L421_4_session_close_20261008.py -- ORRERY repo. Closes the typed
facts session's records.

Built on orrery 36176d5075fc8e896e2176c39bc053237a37ddbe at
https://github.com/tonylquintanilla/palomas_orrery (gallery
ab66aba70a5874b033742a8428070b5889484490 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io).

HOW TO RUN IT
    Save this file in the ORRERY repo's root folder (the one with
    palomas_orrery.py), open it in VS Code, click Run. Then follow the
    numbered steps it prints.

WHAT CHANGES (records only; no code)
    LEDGER_CONSOLIDATED.md
        a header stamp; L-421 (the typed facts) gains what was built, your
        verdicts quoted from WHERE_WE_ARE_10-7-26_0832_run_record.md, and a
        new Gap: the inner Oort cloud redrawn tilted, then the check. It
        stays open. L-351 (what each skill is owed) gains the served-hover
        method for interactive-exhibit's next version.
    documentation/WHERE_WE_ARE.md
        edited BY SECTION at each section's own lines: the header, the
        box, the road, Settled, the Signals mark, Waiting on you, Where
        the details are. Nothing below the run-record marker is touched.
    documentation/HANDOFF_L421_typed_facts_20261008.md
        new: this session's record.

Each edit is matched only at its own lines, so your notes anywhere else
never stop this patch. If another session has already changed one of
those lines, the patch refuses and writes nothing.

SUCCESS looks like: one "ok" line per edit, then "patch applied".
FAILURE looks like: one ERROR: or ANCHOR FAIL: line, and NOTHING is
written. Undo is Discard Changes in GitHub Desktop.

Written October 8, 2026 with Anthropic's Claude Opus 5.5.
"""

import os

ROOT_MARKERS = ("palomas_orrery.py", "LEDGER_CONSOLIDATED.md")
NEXT = ["1. Move this script into documentation/ first.",
        "2. Run orrery_maintenance_run.py.",
        "3. Commit and push."]

LEDGER = "LEDGER_CONSOLIDATED.md"
PAGE = "documentation/WHERE_WE_ARE.md"
HANDOFF = "documentation/HANDOFF_L421_typed_facts_20261008.md"

EDITS = {
  LEDGER: [
    ("header stamp",
     ("edited by section at the L-420 session's close), built on 1ba72f7f.\n"),
     ("edited by section at the L-420 session's close), built on 1ba72f7f.\n"
      "Module updated: October 8, 2026 with Anthropic's Claude Opus 5.5\n"
      "(L-421: three gallery patches served 15 of the 17 typed facts with\n"
      "their sources; L-351 gains the served-hover method), built on\n"
      "36176d50.\n")),
    ("L-421 date",
     "<!-- L:421 status:OPEN upd:2026-10-06 section:A flag: rice: -->\n",
     "<!-- L:421 status:OPEN upd:2026-10-08 section:A flag: rice: -->\n"),
    ("L-421 built, and what is left",
     ("**Gap:** the build, from the manifest, in a fresh session; then Tony's\n"
      "look on the phone; then the survey as a gating check.\n"),
     ("- **Sources, read 2026-10-06** (Round 1, recorded in\n"
      "  `documentation/L421_round1_sources_20261006.md`): five of the six\n"
      "  unsourced facts were sourced from what was read that day -- the\n"
      "  USNO Almanac glossary, USNO's Rise, Set and Twilight Definitions,\n"
      "  NASA Earth Observatory's Catalog of Earth Satellite Orbits, and\n"
      "  Williams (1994). The sense of rotation now cites Archinal et al.\n"
      "  (2019), the correction (Fig. 1, from the PDF Tony supplied), and the\n"
      "  glossary's diurnal and direct motion; the 2018 report was not\n"
      "  re-read, so it is no longer cited. The sixth, the inner Oort cloud\n"
      "  drawn flat in the ecliptic, is contradicted by Nesvorny et al.\n"
      "  (2025, ApJ 983), which finds a slightly warped disk tilted about 30\n"
      "  degrees to the ecliptic.\n"
      "- **Tony's ruling, 2026-10-06:** the inner Oort cloud is redrawn from\n"
      "  the 2025 paper as part of the Sun slice -- \"remember this is part\n"
      "  of the sun slice not deferred.\"\n"
      "- **Built, run and pushed, gallery** (no word a visitor reads\n"
      "  changed; each patch reproduced on a fresh clone, 24 of 24):\n"
      "  - `patch_L421_1_served_hover_words_20261006.py`, at 6fae15e0: the\n"
      "    geostationary ring, magnetopause, bow shock, magnetotail and both\n"
      "    belts print a served `hover` word, `{name}` filled from served\n"
      "    rows (E5 to E10). Tony on the phone: \"correct\".\n"
      "  - `patch_L421_2_served_guide_words_20261006.py`, at 4cfeca27: the\n"
      "    axis, Sun line, terminator and Moon arc print served words from\n"
      "    Earth's `orientation.words`, each with its source; the pole of\n"
      "    date's source prints from the cache builder's record; the Sun's\n"
      "    clumps and tide print served words (E1 to E4, E11 to E13, S2,\n"
      "    S3); the panel's words and footer move to the paragraph grey.\n"
      "    Tony: \"All type is correct.\"\n"
      "  - `patch_L421_3_guide_links_20261006.py`, at ab66aba7: the four\n"
      "    guides get Read more links (Wikipedia: Earth's rotation, Subsolar\n"
      "    point, Terminator (solar), Orbit of the Moon), and the panel now\n"
      "    fills an empty link or source from any trace in a group -- the\n"
      "    sources patch 2 served had not reached the panel until then.\n"
      "    Tony: each link \"correct\".\n"
      "  Verdicts quoted from\n"
      "  `documentation/WHERE_WE_ARE_10-7-26_0832_run_record.md` and chat.\n"
      "- **E10 as built:** \"2020\" and \"IGRF-13 model\" are served words in\n"
      "  the belts' `hovers_plane`, citing the tilt row's source, not fields\n"
      "  read from `constants_new.py`. L-322 (the IGRF epoch, a class) is\n"
      "  unchanged by this.\n"
      "- **S4 stays typed**, as the manifest ruled: the streamer belt's\n"
      "  caveat is a drawing choice.\n"
      "**Gap:** two parts of the Sun slice, then the check. (1) The inner\n"
      "Oort cloud redrawn as the 2025 paper's tilted disk, with the tilt's\n"
      "range as an envelope: its words come to Tony before they ship, and\n"
      "one question first -- the paper puts the disk at 1,000 to 10,000 au,\n"
      "where the served cloud runs 2,000 to 20,000 au from NASA and\n"
      "Portegies Zwart (2021), so trace what uses the outer edge before\n"
      "asking whether it moves. Then Tony's look. (2) The survey as a\n"
      "gating check in the gallery run, shown failing on a planted typed\n"
      "sentence first. Still unchecked: whether each served number's\n"
      "citation in `data/objects_config.json` agrees with its row's in\n"
      "`constants_new.py`. The L-363 `_declared` \"1.1 times\" fix did not\n"
      "ride these patches and is still owed there.\n")),
    ("L-351 interactive-exhibit, the served hover",
     ("  remains is the first half for arithmetic that is not a unit\n"
      "  conversion, such as an altitude from a radius.\n"),
     ("  remains is the first half for arithmetic that is not a unit\n"
      "  conversion, such as an altitude from a radius.\n"
      "- **interactive-exhibit, next bump -- how a hover's facts are served\n"
      "  (L-421, built 2026-10-06):** a shell's facts go in its `hover` word\n"
      "  (a belt's in the parallel lists `hovers_band`, `hovers_rings`,\n"
      "  `hovers_plane`); a new line starts a new hover line and `{name}`\n"
      "  is a value the renderer fills from a served row; `servedHover()`\n"
      "  prints it, and a missing word or a blank with no value warns and\n"
      "  prints nothing. The drawn guides keep theirs on the body's\n"
      "  `orientation.words`, each entry with its `source` and `info_url`.\n"
      "  A link or source carried only on an info marker reaches the panel.\n"
      "  Written here rather than bumped mid-session, to ride the skill's\n"
      "  next version.\n")),
  ],
  PAGE: [
    ("header",
     ("Last updated: October 8, 2026, end of the galactic plane session.\n"
      "- Written at orrery 1ba72f7f and gallery ab66aba0, before your run of\n"
      "  this closing patch.\n"),
     ("Last updated: October 8, 2026, end of the typed facts session.\n"
      "- Written at orrery 36176d50 and gallery ab66aba7, before your run of\n"
      "  this closing patch.\n")),
    ("box",
     ("> **Changed since you last read this:**\n"
      "> - The galactic plane work in the desktop orrery is finished, and you\n"
      ">   found it correct: the violet circle with its poles, Sagittarius A*,\n"
      ">   a hover cross on each coordinate circle, and a brighter galactic\n"
      ">   tide with its cone.\n"
      "> - The orrery's panels use one grey, gray90, on every system. You\n"
      ">   confirmed it, and L-027 (the panel colour) is closed.\n"
      "> - L-422 (the ledger skill at 1.17) is closed: the skill copy this\n"
      ">   session loads reads 1.17, and this page was edited under it.\n"
      ">\n"
      "> **Do next:** *the typed facts, in a fresh session, from the plan.*\n"),
     ("> **Changed since you last read this:**\n"
      "> - 15 of the 17 typed facts are served with their sources and live,\n"
      ">   in three website patches. You found every hover's words correct.\n"
      "> - Earth's four drawn guides have Read more links: the Sun\n"
      ">   Direction, the rotation axis, the day-night line and the Moon.\n"
      "> - Their sources reach the panel now; they had been served but not\n"
      ">   shown. The panel's words and footer are brighter.\n"
      "> - The inner Oort cloud is drawn flat, but a 2025 paper finds it\n"
      ">   tilted about 30 degrees. You ruled it is redrawn now, as part of\n"
      ">   the Sun's slice.\n"
      ">\n"
      "> **Do next:** *finish the typed facts: the inner Oort cloud redrawn\n"
      "> tilted, then the check that keeps facts out of the code.*\n")),
    ("road: heading mark",
     "## The road\n",
     "## The road  **>> UPDATED THIS SESSION**\n"),
    ("road: stages 5 and 6",
     ("  5.   [NOW]   *Earth's old items are finished, in your order.* The\n"
      "               website patch is live; the typed facts are the last part.\n"
      "  6.   [next]  The 17 facts typed in the Earth and Sun rooms' code move\n"
      "               into the served data, with their sources.\n"),
     ("  5.   [NOW]   *Earth's old items are finished, in your order.* The\n"
      "               website patch and Earth's typed facts are live.\n"
      "  6.   [next]  The typed facts: 15 of 17 served. Left: the inner Oort\n"
      "               cloud, redrawn tilted, and the check. << moved this session\n")),
    ("settled",
     ("- Code types only words about our picture; facts are served. (Oct 6)\n"),
     ("- Code types only words about our picture; facts are served. (Oct 6)\n"
      "- The inner Oort cloud is redrawn from the 2025 paper now, as part of\n"
      "  the Sun's slice, not deferred. (Oct 6)\n")),
    ("signals: mark cleared",
     "## Signals  **>> UPDATED THIS SESSION**\n",
     "## Signals\n"),
    ("waiting: design talk",
     ("  You: \"awaits the design talk.\" (Oct 7)\n"),
     ("  You: \"awaits the design talk.\" (Oct 7)\n"
      "- The inner Oort cloud's tilted disk: its words, and whether its outer\n"
      "  edge moves from 20,000 au to the paper's 10,000.\n")),
    ("details",
     ("- The typed facts plan: `documentation/MANIFEST_L421_typed_facts_20261006.md`\n"),
     ("- The typed facts: plan\n"
      "  `documentation/MANIFEST_L421_typed_facts_20261006.md`; record\n"
      "  `documentation/HANDOFF_L421_typed_facts_20261008.md`\n")),
  ],
}


HANDOFF_TEXT = '<!-- Doc-Kind: hand | Session record: L-421 (the typed facts), October 6 to 8, 2026 -- what was built, what Tony ruled, and what is left for the next session. -->\n# Handoff: L-421 (the typed facts), October 6 to 8, 2026\n\nBuilt on orrery 36176d5075fc8e896e2176c39bc053237a37ddbe at\nhttps://github.com/tonylquintanilla/palomas_orrery and gallery\nab66aba70a5874b033742a8428070b5889484490 at\nhttps://github.com/tonylquintanilla/tonyquintanilla.github.io.\nThe session started at orrery fbd223ee and gallery 8487b0f8, from\n`documentation/MANIFEST_L421_typed_facts_20261006.md`.\n\n- Type: BUILD, gallery. Three patches, run and pushed by Tony.\n- Skills: interactive-exhibit loaded at 1.12, matching the manifest,\n  which discharged the obligation carried from v3.84. The ledger skill\n  was read at 1.17 from the repo at HEAD for this close.\n\n## What was built\n\nAll three in the gallery repo. No word a visitor reads changed in any\nof them; each was applied to a fresh clone of the base it names,\nmatched the working copy byte for byte, refused a second run, and\npassed 24 of 24 gating checks.\n\n- **patch_L421_1** (pushed at 6fae15e0). The geostationary ring, the\n  magnetopause, the bow shock and the magnetotail each print a served\n  `hover` word from `data/objects_config.json`. Earth\'s belts print three\n  parallel lists, `hovers_band`, `hovers_rings`, `hovers_plane`. A\n  `{name}` blank is filled from a served row. `store_writer.py` and the\n  editor know the new fields. Items E5 to E10.\n- **patch_L421_2** (pushed at 4cfeca27). The rotation axis, the Sun\n  line, the terminator and the Moon\'s arc print served words from\n  Earth\'s `orientation.words`, each entry with its source. The pole of\n  date\'s source line prints from the cache builder\'s served record (it\n  matched the typed copy when that was deleted). The Sun\'s clumpy outer\n  cloud and galactic tide print served words. The panel\'s words, its\n  footer and the frame note\'s source line move from a 2.6:1 grey to the\n  6.3:1 paragraph grey. Items E1 to E4, E11 to E13, S2, S3.\n- **patch_L421_3** (pushed at ab66aba7). The four guides get Read more\n  links, each a Wikipedia article returned live by a search that day.\n  The cause of the missing link was in `interactive.html`: the panel took\n  a group\'s link and source only from its first and legend traces, and\n  the guides keep theirs on the info marker. It now fills an empty value\n  from any trace and never overwrites one. Measured headless in all\n  three rooms: only those eight Earth values changed.\n\n## Sources read\n\nRound 1 is recorded in `documentation/L421_round1_sources_20261006.md`.\nThe sense of rotation cites Archinal et al. (2019), the correction\n(Fig. 1), from the PDF Tony supplied, with the USNO glossary\'s diurnal\nand direct motion. The 2018 report was not re-read and is no longer\ncited.\n\n## Tony\'s rulings and verdicts\n\nQuoted from `documentation/WHERE_WE_ARE_10-7-26_0832_run_record.md`\n(his latest copy, 2,125 lines) and from chat.\n- Patch 1, the six hovers on the phone: "correct".\n- Patch 2: "All type is correct."\n- Patch 3, each of the four links: "correct".\n- The inner Oort cloud: "remember this is part of the sun slice not\n  deferred."\n- On the header: he meant the Sun Direction\'s missing link, not header\n  icons.\n\n## What is left, for the next session\n\n1. **The inner Oort cloud, redrawn.** Nesvorny et al. (2025, ApJ 983):\n   a slightly warped disk about 15,000 au across, tilted about 30\n   degrees to the ecliptic, its ends twisted toward the galactic poles,\n   the tilt a range that can be drawn as an envelope. First trace what\n   uses the cloud\'s outer edge: the paper puts the disk at 1,000 to\n   10,000 au, the served cloud runs 2,000 to 20,000. Then the one\n   question to Tony, the new words to Tony, the build, his look.\n2. **The check.** The survey that found the 17 becomes a gating check in\n   the gallery run, shown failing on a planted typed sentence first.\n3. Still unchecked: whether each served number\'s citation in\n   `data/objects_config.json` agrees with its row\'s in\n   `constants_new.py`.\n4. Owed elsewhere: the served-hover method is on L-351 (what each\n   skill is owed) for interactive-exhibit\'s next bump; L-363\'s\n   `_declared` "1.1 times" did not ride these patches.\n\n## Lesson\n\nA link that was served still did not show, because the panel read\nonly two of a group\'s traces. Every check passed; Tony\'s look found it.\nThe headless page harness then measured the fix across all three rooms.\n\nSession written October 2026 with Anthropic\'s Claude Opus 5.5.\n'


def read_lf(path):
    with open(path, "rb") as handle:
        raw = handle.read()
    return raw.decode("utf-8").replace("\r\n", "\n"), b"\r\n" in raw


def main():
    if os.path.basename(os.getcwd()) == "documentation":
        raise SystemExit("ERROR: run this from the repo ROOT, not from "
                         "documentation/. NOTHING was written.")
    for marker in ROOT_MARKERS:
        if not os.path.isfile(marker):
            raise SystemExit("ERROR: %s is not here, so this is not the "
                             "orrery root. NOTHING was written." % marker)
    if os.path.exists(HANDOFF):
        raise SystemExit("ERROR: %s already exists. Has this patch already "
                         "run? NOTHING was written." % HANDOFF)
    results = []
    marker = "--- Your run record below this line"
    for path in (LEDGER, PAGE):
        if not os.path.isfile(path):
            raise SystemExit("ERROR: %s is not here. NOTHING was written." % path)
        text, crlf = read_lf(path)
        zone_before = text[text.find(marker):] if path == PAGE else None
        done = []
        for label, old, new in EDITS[path]:
            found = text.count(old)
            if found != 1:
                raise SystemExit("ANCHOR FAIL (%s): expected 1 match in %s, "
                                 "found %d. Has this patch already run, or has "
                                 "another session changed those lines? NOTHING "
                                 "was written." % (label, path, found))
            text = text.replace(old, new)
            done.append(label)
        if path == PAGE:
            if marker not in text or text[text.find(marker):] != zone_before:
                raise SystemExit("ERROR: the run-record zone would change. "
                                 "NOTHING was written.")
            above = text[:text.find(marker)].count("\n")
            if above > 130:
                raise SystemExit("ERROR: the page would stand at %d lines above "
                                 "its marker (cap 130). NOTHING was written."
                                 % above)
        results.append((path, text, done, crlf))
    for path, text, done, crlf in results:
        with open(path, "wb") as handle:
            handle.write(text.encode("utf-8"))
        if crlf:
            print("note: %s was CRLF in the working copy; written LF" % path)
        for label in done:
            print("ok  %-52s %s" % (path, label))
    with open(HANDOFF, "wb") as handle:
        handle.write(HANDOFF_TEXT.encode("utf-8"))
    print("ok  %-52s %s" % (HANDOFF, "created"))
    print("")
    print("patch applied")
    print("")
    print("NEXT:")
    for line in NEXT:
        print("  " + line)


if __name__ == "__main__":
    main()
