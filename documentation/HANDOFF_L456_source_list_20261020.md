<!-- Doc-Kind: hand | Session record of L-456's first build: the i panel's sources as a linked list in every room, Earth's four inner shells in Earth radii, the Gemini prompts for the missing addresses, and the rulings on a monthly run and a "report a problem" link; two patches, with Tony's run order. -->
# Handoff: the i panel's sources as a linked list (L-456)

Built on orrery e8e714da99e0ec102fe179341cf767458d2e8545 at
https://github.com/tonylquintanilla/palomas_orrery ("L410 sun fades
close and cleanup") and gallery ca5339fd3c22d61a1540e4314726e85003e48751
at https://github.com/tonylquintanilla/tonyquintanilla.github.io ("L 410
fixture hovers"). Both patches of section 1 are built on those two SHAs;
neither is run yet.
Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: BUILD, with rulings. Written October 20, 2026 by Anthropic's
Claude Opus 5.5, the same session as
`HANDOFF_L410_sun_fades_build_20261020.md`, which it follows. Your
verdicts are in your run record, `WHERE_WE_ARE_10-18-26_1326_run_record.md`,
the session of 10-20.

## 1. Your run order (every Tony-action of this session, in one list)

Each patch checks the files it edits and refuses rather than guess. The
website patch goes FIRST: the orrery patch gives the dashboard a button
for the website's new check, and the dashboard's own check fails while
the website lacks it.

1. **(do)** Gallery folder: run `patch_L456_1_source_list_website_20261020.py`.
2. **(do)** Move it into the gallery's `documentation/`, and
   `patch_L410_7_sun_fades_website_20261020.py` with it, which is still
   in the gallery's top folder (pushed there at ca5339fd). Both before
   the Daily Run, which would otherwise list them in `module_atlas.py`
   as modules.
3. **(do)** The Daily Run. Expect 31 of 31 gating, "Source list" PASS,
   "Display figures" PASS. Its Config mirror writes the Alfven
   surface's new citation, with its address, from the orrery. Then
   commit and push.
4. **(do)** The live check: `python gallery_maintenance_run.py --live`.
5. **(look)** Mode 5 on your phone: the Sun room, Corona, tap the i: a
   bulleted list of sources, each address a link; tap one. Then the
   Earth room, the Inner Core's hover: "Radius: 0.19151 Earth radii",
   then "= 1,221.5 km (0.000008165 AU)".
6. **(do)** Orrery folder: run `patch_L456_2_session_close_20261020.py`,
   then move it into `documentation/`.
7. **(do)** The orrery maintenance run. Expect 31 of 31 gating, the gate
   line 0 TIER-1 (whole tree 280), "Skill headers" OK and "Dashboard
   parity" PASS. It rewrites the ledger's index and the Skill Manifest
   (interactive-exhibit 1.18). Commit; push.
8. **(do)** Reinstall interactive-exhibit (1.18) in Settings > Skills.
9. **(do)** Carry the two Gemini prompts, in the orrery's
   `documentation/prompts/`, to Gemini 4: `RELAY_L456_gemini_addresses_sun_20261020.md`
   and `RELAY_L456_gemini_addresses_earth_20261020.md`. A desktop
   browser may hold up better than the phone app. Save each answer in
   `documentation/worksheets/` under the name the prompt asks for.

## 2. What was built

**The website, patch_L456_1** (gallery folder):
- `gallery/source_list.js` (new): turns a feature's citations into one
  list, and finds where each web address in a citation ends.
- `interactive.html`: loads it. The i panel prints "Source:" or
  "Sources:" and a bulleted list: each citation after its label in
  bold, the website's note after a dash, every address a link that
  opens in a new tab, long addresses wrapping on the phone. Every room.
- `gallery/feature_renderers.js`: where citations are gathered (the
  corona, the dust cloud, a shell whose words name a second number, the
  exosphere's fade) they also ride as a list, `source_items`. Earth's
  inner core, outer core, lower mantle and upper mantle give their
  radius in Earth radii first, from the row's served "in".
- `gallery/earth_geometry.js`: the axis's, the Sun direction's, the
  terminator's and the Moon arc's citations as a list too.
- `documentation/smoke_source_list.js` (new, gating "Source list"):
  names, for every feature in the Sun room and Earth's recorded scene,
  how many citations it lists and how many carry a link.
- `documentation/smoke_display_figures.js`: grades the four new
  Earth-radii lines by its own arithmetic and pins your approved
  figures. The hover fixture did not change.
- `gallery_maintenance_run.py`: runs the new check; the live check
  fetches `gallery/source_list.js`.

The joined citation line that every other check reads is unchanged.

**The orrery, patch_L456_2** (the close):
- `palomas_orrery_dashboard.py`: a Source List button for the website's
  new check; and "Horizons Check -- everything, now" in Tools and
  Caches, `horizons_check.py --all`, which confirms every object and
  data sheet today rather than only what is due.
- interactive-exhibit 1.18 (section 5); protocol v3.106; the ledger;
  Where We Are; this handoff; the two Gemini prompts, already in your
  folder.

How many citations carry a link, measured at ca5339fd: the Sun room 22
of 43, the Earth room 9 of 29. The addresses close that gap.

## 3. Your rulings this session

- From the phone: "need hyperlinks" and "need some kind of itemization
  for readability". Then: "can we do L456 in this session so we are
  ready for the sun's 14 pairs?" So L-456 goes before L-191's fourteen
  pairs.
- The addresses: "ask Gemini to do the search and Claude checks they
  are correct."
- The link check: every 30 days, automatically, "Yes"; and by hand any
  time. "Can you add the 30-day Checkers to the dashboard?" -- the
  Horizons button now; the link check's with its build.
- One monthly run, started by the Daily Run, with the link check as its
  first job: "Yes, as recommended." (L-459)
- A "report a problem" link: reports land "in the daily maintenance
  report"; through the guest book's form, pre-filled, no second sheet;
  for any problem a visitor sees, "perhaps an expert would see a
  problem we have not caught." "Confirmed." (L-458)

## 4. How it was checked

- The website patch, on clean copies at ca5339fd with Unix and with
  Windows line endings: the tested bytes both times; a second run
  refuses.
- The website's maintenance run on a stand-in copy: 31 of 31 gating
  (the three pulls, and the two mirrors that wait on them, fail only
  because the sandbox cannot reach GitHub's API; they are not gating). "Source list" breaks its own file two ways first and goes red
  both times. "Hover budget", "Typed facts", "Typed numbers" and
  "Display figures" pass.
- The corona's i panel drawn headless at phone width with the page's
  own panel code and styles (`panel_preview_corona.png`, sent in chat).
  The phone has not seen it: step 5.
- The orrery close: the dashboard compiles; "Dashboard parity" passes
  against the patched gallery, 10 of 10 planted faults caught.

## 5. Skill versions and what travels

This session's loaded copies read interactive-exhibit 1.17 and
provenance-cross-check 1.1, as the manifest expected, beside the
earlier half's (`HANDOFF_L410_sun_fades_build_20261020.md`, section 5).
interactive-exhibit goes to 1.18 in patch_L456_2; the next session
confirms its loaded copy reads 1.18 before exhibit work, and
provenance-discipline 2.32 before provenance work.

## 6. What is left, and the next session

- The addresses: when Gemini's two answers are saved, re-open every
  address before it goes on its row's Source line in the orrery
  (provenance-discipline 2.32), the Sun's first, then Earth's; a review
  of each return. Then the website's Daily Run carries them.
- Then L-191: the Sun's fourteen hover and tooltip pairs reconciled
  (its entry records what was measured).
- Still on L-456: the Celsius words for Earth's surface and air, as a
  list for you; the export serving a derived row's inherited citations
  as a list, so they itemize too.
- L-459 with L-266: the monthly run and its link check, after the
  addresses are in. L-458: the "report a problem" link, when its words
  list is ready.
