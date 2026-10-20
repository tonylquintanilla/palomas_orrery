<!-- Doc-Kind: hand | Session record of the Sun's two fades built (L-410, the corona, with L-131, the dust cloud), orrery and website; three patches, with Tony's run order. -->
# Handoff: the Sun's two fades built (L-410 with L-131)

Built on orrery 1b4733509558535e1d0db54471a05523a1f1952a at
https://github.com/tonylquintanilla/palomas_orrery and
gallery 4fc320fa6d2e0e10d9a50b8b69006cbff96a1364 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io. The
orrery's half was pushed at fcd191e91e56508223fe04fe61fb8f0a09252eee
("L410 sun fades and words"); the gallery moved by your Daily Run to
e8f6dd5e7ffce8e293ca7005e9ad1e3f692f2f24 ("daily run 10-20-26"). The
two patches of section 1 are built on those two SHAs.
Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: BUILD. Written October 20, 2026 by Anthropic's Claude Opus 5.5.
Follows `HANDOFF_L385_opening_views_20261019.md`, section 6.
Companions: `SOURCES_L410_sun_corona_dust_20261019.md`, the design and
its sources, with what was settled at the build in its last section;
the three words lists, each marked by you:
`WORDS_L410_sun_fades_20261019.md` (revision 3),
`WORDS_L410_build_list_20261019.md` and
`WORDS_L410_website_list_20261020.md`. Your verdicts are in your run
record, `WHERE_WE_ARE_10-18-26_1326_run_record.md`, the session of
10-19 to 20.

## 1. Your run order (every Tony-action of this session, in one list)

Each patch checks the files it edits and refuses rather than guess.

1. **(done)** Orrery folder: `patch_L410_5_sun_fades_orrery_20261020.py`;
   the maintenance run 31 of 31, "Drawings export check" 14 of 14, the
   gate 0 TIER-1; your looks: "the colors and shapes look great", and
   "looks great". Pushed fcd191e9.
2. **(do)** Orrery folder: run `patch_L410_6_sun_fades_close_20261020.py`,
   the records and three small code changes (section 2).
3. **(do)** Move patch 6 into `documentation/` first. Run in the
   folder's root, the maintenance run would list it in
   `module_atlas.py` as a module.
4. **(do)** Orrery maintenance run (dashboard). Expect 31 of 31 gating,
   the gate line 0 TIER-1 (whole tree 280), and "Skill headers" OK. It
   rewrites the ledger's index and the Skill Manifest, which then reads
   provenance-discipline 2.32. Then commit and push. The website patch
   needs this push: the Daily Run pulls the new Kasper citation from
   it.
5. **(do)** Reinstall provenance-discipline (2.32) in Settings > Skills.
6. **(do)** Gallery folder: run `patch_L410_7_sun_fades_website_20261020.py`.
7. **(do)** Move patch 7 into the gallery's `documentation/` first, for
   the same reason as step 3.
8. **(do)** The Daily Run. Expect 30 of 30 gating, "Drawings" 23 of 23
   planted faults caught, "Typed facts" and "Typed numbers" PASS, and
   the mirrors saying nothing to change. Then commit and push.
9. **(do)** The live check: `python gallery_maintenance_run.py --live`,
   as the Daily Run's last line says.
10. **(look)** Mode 5 on your phone: the Sun room, Corona ticked, then
   the Zodiacal Dust Cloud. The two corona spheres are gone; "Sun:
   Corona" is one row in the drawer and switches the streamer band too.
   Tap each i: the Source line lists its citations, each after a label.

## 2. What was built

**The orrery, patch 5** (pushed fcd191e9; L-410's ledger entry lists
it in full). The corona: 2,500 dots from the Sun's surface to the
Alfven surface, placed by the electron density of Mann et al. (2023)'s
solar wind model, each dot's brightness the sunlight it receives. The
streamer belt is drawn with it, under one checkbox and one legend
entry. The dust cloud: 3,000 dots by Kelsall et al. (1998)'s smooth
cloud, tilted to its own middle plane, thinning between 19 and 5 solar
radii, stopping at 5.2 AU. Eighteen rows; two stored drawings for the
website. The inner and outer corona spheres are gone.

**The website, patch 7** (gallery folder):
- `gallery/feature_renderers.js`: the fade shape draws dots in solar
  radii and AU as well as Earth radii, and draws the dust cloud as
  stored, not turned to the Sun's pole. The hover comes from the
  entry's served words, its numbers filled from served rows. The i
  panel prints each citation after a short label. The streamer band
  joins the corona's row in the drawer.
- `data/objects_config.json`: the corona and the dust cloud, in your
  approved words; the two corona spheres' entries gone; the Roche
  limit's note reworded; the Alfven surface's citation with Kasper et
  al.'s address, as the orrery now exports it.
- `tools/pull_drawings.py`, `tools/check_drawings.py`,
  `tools/store_writer.py`, `gallery_maintenance_run.py`: the two new
  drawings pulled, served and checked by their mechanism (between their
  edges, thinning out, the dust tilted about 2 degrees).
- Three smoke checks updated: the Sun's shells, typed numbers (a
  citation in words, "(Boe and others, 2021)", is a locator) and
  display figures (fixture re-recorded:
  `fixture_hovers_L410_on_e8f6dd5e.json`).

**The orrery, patch 6** (the close):
- `constants_new.py`: the Alfven surface's Source line names Kasper et
  al. (2021) by its title, with the paper's address.
- `solar_visualization_shells.py`: the corona's hover gives the Alfven
  surface's distance in km beside AU, from its row.
- `exact_rows_report.py`: the two corona spheres' entries removed.
- provenance-discipline 2.32 (section 5); protocol v3.105; the ledger;
  Where We Are; the sources record; your marked website list; this
  handoff.

## 3. Your rulings this session

All quoted from your run record and the three marked lists.
- Revision 3's drafts: "yes, 1d confirmed"; the streamer belt's and the
  Alfven surface's wording, "yes, clearer. approved". "Over the Sun's
  magnetic equator": "drop for now but keep a breadcrumb" (L-411).
- The build list: every item yes. On the corona's numbers: "keep the
  numbers ... not 2 million." On the dust line: "add the km
  parenthetically." The linear thinning near the Sun, and the cloud
  centred on the Sun: approved.
- The website list (`WORDS_L410_website_list_20261020.md`): the hover
  alone; km beside AU on both sites; the Source labels, "and we should
  note that the citation should have a live url link", with a live-link
  check every 30, 60 or 90 days (L-266); the dust cloud's Wikipedia
  link, and the corona's, "accepted" once its reason was given;
  comet-by-comet Roche limits, "not an urgent idea. it does not have to
  be carried in the sun slice" (L-457); ".; " in joined citations, "on
  a priority basis since the earth and sun slices are the template"
  (L-456).
- On the Kasper address: "we should add this to the skill"
  (provenance-discipline 2.32).

## 4. How it was checked

- Patch 5's own checks are in section 1, step 1: your runs.
- Patch 6 run on a clean copy at fcd191e9: the tested bytes; on
  Windows line endings too, with a note added to the ledger and to Where
  We Are, which it kept; a second run refuses. The orrery maintenance
  run on the patched copy: every checker passed but two this sandbox
  cannot satisfy, the Horizons confirmations (JPL is out of reach) and
  the dashboard parity (it reads the gallery folder beside the orrery's,
  which this copy did not have); gate path 0 Tier-1, whole tree 280, no
  file's count rose. Run with patch 6 still in the root, it listed the
  patch in `module_atlas.py`; moved first, it does not. Hence step 3.
  The exact-rows check passes against the gallery before and after
  patch 7. The website's atlas, too, lists a patch left in the root,
  hence step 7.
- Patch 7 run on a clean copy at e8f6dd5e, the same three ways. Then a
  stand-in for the Daily Run on that copy, with the orrery's export as
  patch 6 makes it: both mirrors find nothing to change; the website's
  maintenance run, offline, 30 of 30 gating. The display fixture changed
  in exactly the three hovers you marked: the corona's km, the dust
  cloud's km, the Roche limit's note.
- The website's renderer, drawn headless, showed the same dots as the
  orrery, one "Sun: Corona" legend row (patch 7 changed words only
  after that render).
- Not checked here: the live site and the phone. Steps 9 and 10.

## 5. Skill versions and what travels

This session's loaded copies read orrery-coding-conventions 1.11 and
provenance-cross-check 1.1 (discharging v3.104's obligation),
provenance-discipline 2.31, interactive-exhibit 1.17, agentic-pre-test
1.3, safe-file-editing 1.13 and ledger-and-session-records 1.21, as the
manifest expected. provenance-discipline goes to 2.32 in patch 6 (a
citation's address goes on its Source line); the next session confirms
its loaded copy reads 2.32 before provenance work.

## 6. What is left, and the next session

- L-410 and L-131 close on your steps 7 to 10.
- Next session, by your ruling from the coordination session: the
  Sun's fourteen hover and tooltip pairs reconciled (L-191). The Sun's
  tooltip strings were not touched in this one. Measured at fcd191e9,
  L-191 records: all fourteen twins are live; five pairs differ in
  content (gravitational influence, Roche limit, Alfven surface,
  corona, dust cloud; the last two by design), and nine are
  byte-identical copies; the Alfven surface's hover types no latitude
  range, but leaves out the 10 to 20 solar radii range its tooltip
  prints from L-228's rows.
- Then L-456: the panel's listed, linked sources, the Sun's and
  Earth's rooms first, and the 98 served citations with no web address.
- The rest of the Sun's slice (L-412): the streamer belt's and the
  clumps' numbers set by eye; L-241's Hills wording; the chromosphere's
  new words (L-411). Then L-443, the objects to the website, with the
  ice lines (L-128) after it.
- Carried, not chased: two places still name the inner K-corona, the
  MAPS paragraph and the comet hovers (L-411).
