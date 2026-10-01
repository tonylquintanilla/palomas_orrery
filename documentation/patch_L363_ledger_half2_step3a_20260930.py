#!/usr/bin/env python3
"""
patch_L363_ledger_half2_step3a_20260930.py -- ORRERY repo. Closes the
session of 2026-09-30 and 10-01.

Run: save this file in the ORRERY repo ROOT (next to palomas_orrery.py),
open it in VS Code and click Run. The same as: python
patch_L363_ledger_half2_step3a_20260930.py

A patch is run from its repository's ROOT and filed in documentation/
AFTER it has run. This script refuses to run from documentation/.

Built on orrery 10012821cf6289095912c0a5f2a0ae86d26ce1e1
at https://github.com/tonylquintanilla/palomas_orrery
(gallery 432435a84aaeaaa7226bb1bbdb431390547f0d18
at https://github.com/tonylquintanilla/tonyquintanilla.github.io)

WHAT IT DOES.

  LEDGER_CONSOLIDATED.md
      - header stamp;
      - L-397 added, done: "Cache in step" compares every object;
      - L-398 added: distance figures take JPL's own accuracy (next);
      - L-399 added: small bodies' own uncertainty, with the asteroid
        design (Apophis's line until then);
      - L-400 added: the stray "data/solar-system (1)" folder;
      - L-392 marked done: the drawer list is served;
      - L-363, L-395 updated; your notes recorded on L-385 and L-389.
  documentation/WHERE_WE_ARE.md
      rewritten for this session. Your annotated copy, or the copy in
      the repo, may be there; either is replaced. Any other content
      makes the patch refuse.
  documentation/HANDOFF_L363_half2_step3a_20260930.md
      this session's record (new).

No skill changes. Everything is written or nothing is.

AFTER IT RUNS:
  1. python orrery_maintenance_run.py -- it rebuilds the ledger index.
     This patch does not touch the index zone or fingerprint it.
  2. Move this script into documentation/.
  3. Commit together with your fix to celestial_objects.py (the three
     duplicated fields), and push.

SUCCESS looks like: one "ok" line per edit and per file, then "patch
applied". FAILURE looks like: one ERROR: or ANCHOR FAIL: line, and
NOTHING is written. Undo is Discard Changes in GitHub Desktop.

Written October 1, 2026 with Anthropic's Claude Opus 5.5.
"""

import hashlib
import os
import sys

LEDGER = "LEDGER_CONSOLIDATED.md"
LEDGER_FP = "e8f32d8e2e1701a5ebc48f68594c163a"
INDEX = ("<!-- INDEX:START", "<!-- INDEX:END -->")
PAGE = "documentation/WHERE_WE_ARE.md"
PAGE_FPS = ("2145e59039596144706ae97e115ab0e1",   # the repo's copy at 10012821
            "f395c08b86fce264765a255b1d5feb22")   # Tony's annotated copy
HANDOFF = "documentation/HANDOFF_L363_half2_step3a_20260930.md"

EDITS = [('header stamp', 'Review and RICE update Tony 6-21-2026\n', "Module updated: October 1, 2026 with Anthropic's Claude Opus 5.5\n(L-363 Half 2 steps 1 to 3a; L-397 done; L-398, L-399, L-400\nopened; L-392 done; notes on L-385, L-389, L-395), built on 10012821.\nReview and RICE update Tony 6-21-2026\n"), ('L-397 to L-400 added', "#### [L-396] Tony's page: WHERE_WE_ARE.md", '#### [L-400] A stray folder "data/solar-system (1)" in Tony\'s gallery copy (gallery, housekeeping)\n<!-- L:400 status:OPEN upd:2026-09-30 section:A flag: rice: -->\n- Reported by the gallery maintenance run\'s Cache siblings check on\n  2026-09-30: one directory in data/ the builder did not make. The name\n  has the shape of a OneDrive conflict copy (the L-216 class). Git\n  ignores it and the check is report-only.\n- Tony-action (do): look inside, then delete it.\n**Gap:** the deletion.\n**Ref:** documentation/check_cache_siblings.py (gallery); L-216.\n\n#### [L-399] Small bodies: fetch each one\'s own position uncertainty from Horizons (gallery, builder)\n<!-- L:399 status:OPEN upd:2026-10-01 section:A flag: rice: -->\n- JPL\'s planetary report (L-398) gives accuracies for the planets and\n  Pluto only. An asteroid\'s accuracy is kept per body. Until it is\n  fetched, Apophis\'s text box carries one line: "JPL\'s own uncertainty\n  for this position is not yet included." (Tony, 2026-10-01: keep the\n  distance; "We have been computing it all along from Horizons\n  ephemeris." He noted that near-Earth tracking knows these\n  trajectories with high precision; the fetched figure is expected to\n  confirm that.)\n- Candidate: the nightly builder asks Horizons for each small body\'s\n  range uncertainty (likely the 3-sigma range quantity of an\n  ephemeris query; unverified) and serves it; the page then uses it as\n  the source accuracy and the line goes away.\n**Gap:** with the near-Earth asteroid design.\n**Ref:** L-398; L-363; tools/gallery_cache_builder.py (gallery).\n\n#### [L-398] Distance figures: the source\'s own accuracy, not only our drift from Horizons (gallery, provenance)\n<!-- L:398 status:OPEN upd:2026-10-01 section:A flag: rice: -->\n- **Ruled 2026-09-30.** Distances in the Solar System room are written\n  out (no exponents) and printed to "the actual sig figs". Built at step\n  3a (gallery 432435a8): the figures come from the builder\'s measured\n  drift (error_rate_deg_per_day times the days since the elements\'\n  date, as a distance at the body\'s distance), placed by the Report\n  test, never finer than whole kilometres. Tony confirmed it as the\n  rule for every computed position, to go into provenance-discipline.\n- **Gap found 2026-10-01** by Tony\'s question, "does Horizons serve the\n  distance to pluto with 9 significant digits?" The drift measures how\n  closely the page reproduces Horizons, not how well JPL knows where\n  the body is. Pluto printed ten figures.\n- **Source read 2026-10-01.** Folkner et al. 2014, IPN Progress Report\n  42-196 (DE430), abstract: the inner planets to subkilometre accuracy;\n  Jupiter and Saturn to tens of kilometres; Uranus, Neptune and Pluto\n  limited to several thousand kilometres. Park et al. 2021, AJ 161:105\n  (DE440, the ephemeris Horizons uses): Jupiter, Saturn and Pluto\n  improved, no new kilometre figures; Uranus and Neptune statistically\n  consistent with DE430. So the 2014 groups are a conservative upper\n  bound. Both read from JPL\'s own sites (ipnpr.jpl.nasa.gov,\n  ssd.jpl.nasa.gov).\n- **Ruled 2026-10-01.** Use whichever is larger, our drift or the\n  source\'s accuracy; the three groups are the source accuracy. Apophis\n  keeps its distance with one line (L-399).\n- **Build.** Orrery: three rows in constants_new.py citing the 2014\n  report, each stating the accuracy the source names in words as a\n  place -- a new case for provenance-discipline, which also gains the\n  computed-position rule. Gallery: each served object points at its\n  group\'s row through orrery_constant and the mirror; the page uses the\n  larger of the two; Apophis\'s line; interactive-exhibit records the\n  rooms section and the served row words (label, about, source_note).\n**Gap:** the build above, and both skill bumps.\n**Ref:** interactive.html solarSystemDistanceLine (gallery); L-363; L-399; L-345.\n\n#### [L-397] "Cache in step" compared only bodies with shells; it now compares every object (gallery, checks)\n<!-- L:397 status:DONE upd:2026-09-30 section:A flag: rice: -->\n- **Found 2026-09-30** adding five planets and Pluto (L-363):\n  tools/check_cache_in_step.py compared the served cache with\n  data/objects_config.json only for objects serving shells -- the Sun,\n  Earth, Jupiter and Saturn. A body added to the config with no shells\n  could have been pushed without a cache rebuild, and no check would\n  have said so. Tony: "let\'s do this on a priority basis."\n- **Built** by patch_L397_cache_in_step_all_objects_20260930.py (gallery\n  1530bb6d -> f6d1ca95). Every object in the config must be in both\n  cache files, and nothing may be in either that the config does not\n  list. Seven identity fields must match coverage_index.json: name,\n  Horizons id, category, availability, parent, centre, frame. Each run\n  first shows the comparison can fail, on in-memory copies (an unbuilt\n  object, a changed name). Shown failing against the cache before the\n  step 2 build (0f513fd5), naming the six new bodies in each file.\n  [verified @f6d1ca95: Tony\'s maintenance run, 19 of 19 gating checks]\n- **Does not check:** orbit numbers (the config holds none), build\n  recency (the trust window and the Daily Run cover it), the rooms\n  section (the page reads it from the config directly).\n**Note:** gallery-cache-builder\'s description of the check widens at its next bump.\n**Ref:** tools/check_cache_in_step.py (gallery); L-363; L-322.\n\n#### [L-396] Tony\'s page: WHERE_WE_ARE.md'), ('L-395 note', '<!-- L:395 status:OPEN upd:2026-09-29 section:A flag: rice: -->\n', '<!-- L:395 status:OPEN upd:2026-10-01 section:A flag: rice: -->\n- **2026-10-01, first use and a check.** Tony: each body\'s description\n  and link in the rooms come from the dictionary, as a standard written\n  into the skill; Pluto\'s row in the Solar System room uses NASA\'s\n  Pluto page ("this is what visitors expect"). Three entries had a\n  field written twice -- Earth, Moon, Patroclus-Menoetius Barycenter --\n  the first silently discarded by Python and invisible to the\n  provenance scanner (Earth\'s discarded line gave the Moon\'s 27.32-day\n  period). Tony fixed them by hand the same day. The export gets a\n  check that refuses an entry with a duplicated field.\n'), ('L-392 done', '<!-- L:392 status:OPEN upd:2026-09-29 section:A flag: rice: -->\n', '<!-- L:392 status:DONE upd:2026-09-30 section:A flag: rice: -->\n- **Done 2026-09-30.** The list is served: a top-level "rooms" section\n  of data/objects_config.json holds the Solar System room\'s drawer rows,\n  in order, with See more marked per row, and its opening view (Tony:\n  "confirmed as recommended"). Every reader of the file reads only\n  "objects", checked before it was proposed. Built by\n  patch_L363_7_half2_config_20260930.py; read by the page from\n  patch_L363_8_room_step3a_20260930.py (gallery 432435a8).\n'), ('L-389 Tony note', '<!-- L:389 status:OPEN upd:2026-09-28 section:A flag: rice: -->\n', '<!-- L:389 status:OPEN upd:2026-09-30 section:A flag: rice: -->\n**Tony:** (on Where We Are, 2026-09-30) "this depends on the source. Re\nis based on the equatorial radius. The crust is ~0.99... Re"\n'), ('L-385 Tony note', '<!-- L:385 status:OPEN upd:2026-09-28 section:A flag: rice: -->\n', '<!-- L:385 status:OPEN upd:2026-09-30 section:A flag: rice: -->\n**Tony:** (on Where We Are, 2026-09-30, how wide the Sun\'s opening view\nis in the orrery) "photosphere + 10%"\n'), ('L-363 session bullet', '<!-- L:363 status:OPEN upd:2026-09-29 section:A flag: rice: -->\n', '<!-- L:363 status:OPEN upd:2026-10-01 section:A flag: rice: -->\n- **Session 2026-09-30 to 10-01 (Half 2, steps 1 to 3a).** Design talk\n  closed: ticking a planet opens its row; Apophis keeps one See more\n  row; the tick order lives only in the open tab, nothing stored\n  between visits. The room\'s settings are served in a new "rooms"\n  section of data/objects_config.json (L-392). Step 2\n  (patch_L363_7_half2_config_20260930.py, gallery 1530bb6d): Mercury,\n  Venus, Mars, Uranus, Neptune and the Pluto-Charon barycentre\n  (Horizons 9 about the Sun -- the room\'s Pluto, by the barycentre rule)\n  served; the whole cache is now trusted +/- 88 days, Mercury\'s period.\n  Step 3a (patch_L363_8_room_step3a_20260930.py, gallery 432435a8): the\n  room draws its rows from the rooms section, opens on the Sun and\n  Earth with Earth\'s row highlighted, and prints Tony\'s approved words\n  -- Pluto named Pluto with his barycenter sentence, the source line\n  with "Horizons id:" and "Julian date" written out, the two panel\n  paragraphs, the Explorer sentence dropped (the Explorer stays, not as\n  a featured card). Orbit crosses name the orbit only. Distances are\n  written out with earned figures (L-398). Colours from the orrery\'s\n  color_map. Standing rule (Tony): real names are fine in a card once\n  explained, never as shorthand.\n- **Remaining, in Tony\'s order:** L-398 (figures), L-395 (descriptions\n  and NASA links; Pluto\'s row uses NASA\'s Pluto page), then step 3b\n  (See more / See fewer, opened rows with "Enter the Sun room" or "No\n  room or cards yet", tap a body to highlight its row, the Sun\'s row\n  not tickable, Home walking back through the tick order), then Tony\'s\n  phone check.\n')]

PAGE_TEXT = '<!-- Doc-Kind: hand | Where the project is and where it is going, in plain words. One file, rewritten in place; read it at the end of every session. -->\n# Where We Are\n\nLast updated: October 1, 2026\n- Written at orrery 10012821 plus this session\'s closing patch, and\n  gallery 432435a8.\n\n> **READ THIS FIRST**\n>\n> **Changed this session:**\n> - All eight planets and Pluto are now in the Solar System room on\n>   the website.\n> - The room opens on the Sun and Earth. You tick the others in the\n>   drawer.\n> - Every word a visitor sees in the room is one you approved.\n> - Each body\'s distance is written out in full, with only the figures\n>   its accuracy earns.\n> - The check comparing the website\'s data with its settings now\n>   covers every body, not just the four with layers.\n>\n> **Do next:**\n> - *Claude adds JPL\'s own accuracy to the distance figures, so Pluto,\n>   Uranus and Neptune stop showing more figures than JPL knows.*\n>\n> **Needs you now:**\n> - *Run this session\'s closing patch in the orrery folder, then commit\n>   and push. Include your fix to the dictionary\'s duplicated lines.*\n\nHow to read the marks:\n- *Italic* lines are the must-reads.\n- **>> UPDATED THIS SESSION** beside a heading means that section\n  changed in the latest session.\n- Sections without it are as they were.\n- The marks are cleared and reset at every session\'s update, so they\n  always mean "new since you last read this."\n\n## The goal\n\n- Paloma\'s Orrery on the web.\n- Anyone can open interactive rooms of the solar system in a browser,\n  with nothing to install.\n- Built from the same code and the same checked numbers as the desktop\n  orrery.\n\n## The road\n\n  1. [done]   The Sun\'s room is live on the website.\n  2. [done]   Earth\'s room is live, with every number traced to its source.\n  3. [done]   The numbers come from one place: the orrery feeds the\n              website, and nothing is typed twice.\n  4. [NOW]    *The Solar System room becomes the front door: all the\n              planets, a drawer to pick them, and a way into each\n              body\'s own room.*\n  5. [next]   The Sun\'s numbers get the same checking Earth\'s got.\n  6. [next]   The front door becomes the page the website opens on.\n  7. [later]  The rest of the orrery\'s objects come to the website --\n              dwarf planets, asteroids, moons -- from the orrery\'s own\n              object list, checked against JPL Horizons.\n  8. [later]  Encounters: comets and spacecraft shown at the dates\n              that matter.\n  9. [later]  The planets get their details -- layers, rings, magnetic\n              fields -- Jupiter and Saturn first.\n 10. [goal]   The orrery\'s own Python runs in the browser.\n\n## Right now  **>> UPDATED THIS SESSION**\n\n- The Solar System room shows the Sun, all eight planets, Pluto and\n  the asteroid Apophis, where they are when you open it.\n- It opens on the Sun and Earth, with Earth\'s row highlighted.\n- The drawer lists every body in order outward from the Sun.\n- Each text box gives the body\'s distance in AU and in km, written out.\n- Still to fix: Pluto, Uranus and Neptune show more figures than JPL\n  actually knows.\n- The drawer\'s new behaviours have not been built yet.\n\n## The next three steps  **>> UPDATED THIS SESSION**\n\n1. *The distance figures get JPL\'s own accuracy.*\n   - Claude writes two patches: three accuracy rows for the orrery,\n     taken from JPL\'s own report, and the website change that uses\n     them.\n   - You run both.\n2. Each body gets its NASA description and link, taken from the\n   orrery\'s own object list.\n   - Pluto\'s row links to NASA\'s Pluto page.\n3. The drawer\'s new behaviours are built.\n   - "See more", "Enter the Sun room", tapping a body to find its row,\n     and Home remembering what you ticked.\n   - You check them on your phone and desktop.\n\n## Waiting on you  **>> UPDATED THIS SESSION**\n\nNow:\n- *Run the closing patch in the orrery folder, commit and push.\n  Include your fix to the dictionary\'s duplicated lines.*\n\nAt the next design talk:\n- Nothing is waiting.\n\nNot urgent:\n- A folder named "solar-system (1)" sits in the website\'s data folder.\n  - It looks like a OneDrive copy, and git ignores it.\n  - Have a look inside, then delete it.\n- Each orbit\'s small cross now just says "Mercury\'s orbit" and so on.\n  Change the words if you would like others.\n- Earth\'s atmosphere: your note says it depends on the source. Claude\n  brings it back when that item is worked.\n\n## Where the details are\n\n- Every item, done and open: `LEDGER_CONSOLIDATED.md`\n  - This session: L-363, L-392, L-395, L-397, L-398, L-399, L-400.\n- The reasoning behind the order:\n  `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md`\n- The latest session record:\n  `documentation/HANDOFF_L363_half2_step3a_20260930.md`\n'

HANDOFF_TEXT = '<!-- Doc-Kind: hand | Session record for the Solar System room, Half 2 steps 1 to 3a (L-363), 2026-09-30 and 10-01. -->\n# HANDOFF -- L-363 Half 2: design closed, five planets and Pluto served, room step 3a live\n\nBuilt on orrery 10012821cf6289095912c0a5f2a0ae86d26ce1e1 at\nhttps://github.com/tonylquintanilla/palomas_orrery, and gallery\n0f513fd5d8ad2ce1e3ba5f19ea2f44388484690e at\nhttps://github.com/tonylquintanilla/tonyquintanilla.github.io.\nGallery pushed at 1530bb6d (step 2), f6d1ca95 (L-397), 432435a8 (step 3a).\nOrrery: this record lands with the closing patch\npatch_L363_ledger_half2_step3a_20260930.py.\n\nType: BUILD.\nSupersedes: nothing. Companion to\nHANDOFF_L363_three_strands_integrated_20260929.md (whose section 4 this\nsession carried out, and to whose local copy Tony appended the run\nrecords of this session\'s patches).\n\nSession written October 2026 with Anthropic\'s Claude Opus 5.5.\n\n## 1. Skills at session start\n\nAll loaded copies matched the manifest: ledger-and-session-records\n1.13 (the obligation from v3.74 is discharged), interactive-exhibit 1.6,\nprovenance-discipline 2.22, gallery-cache-builder 1.6, safe-file-editing\n1.11, agentic-pre-test 1.2, orrery-coding-conventions 1.9,\nhorizons-orbital-mechanics 1.1. No skill was bumped this session; the\nbumps this session\'s rulings need travel with L-398\'s build (section 6).\n\n## 2. Rulings, in Tony\'s words where he gave them\n\n- Ticking a planet in the drawer also opens its row: yes.\n- Apophis keeps one row, under See more, until the near-Earth asteroids\n  get their own design: yes.\n- The room\'s settings are served, in a new top-level "rooms" section of\n  data/objects_config.json: "confirmed as recommended". Every reader of\n  the file (builder, assembler, both writers, the checks) reads only\n  "objects"; checked before recommending.\n- Home\'s tick order lives only in the open tab: "No stored information\n  between sessions locally."\n- Pluto in the Sun-centred room is the Pluto-Charon barycentre (Horizons\n  9 @sun), by the barycentre rule; named "Pluto": "confirmed". Hover\n  sentence, Tony\'s wording: "The symbol marks the gravitational center\n  (barycenter) that Pluto and its moon Charon orbit together. It lies\n  outside Pluto itself."\n- Words: "See more" / "See fewer"; "Enter the Sun room" / "Enter the\n  Earth room"; "No room or cards yet"; distances written out, not in\n  exponent form; the x, y, z line dropped; the panel\'s Explorer sentence\n  dropped ("the explorer will remain but not as a featured card").\n- Source line: "Horizons id: 199", not "target"; "measured from the\n  Sun\'s centre"; the date written out with the Julian date in brackets.\n  Standing rule: "spell out JD, Julian date, the first time it is named\n  in a card. i think that it is okay to use actual names as long as\n  they are explained not just short hand."\n- Figures: "use the actual sig figs"; then, confirmed, each distance\n  prints the figures its measured error earns at the minute drawn, as a\n  rule for every computed position (provenance skill). Then, on Tony\'s\n  question about Pluto, the source\'s own accuracy enters: use whichever\n  is larger (L-398, confirmed 2026-10-01), JPL\'s three groups as the\n  source accuracy, Apophis keeps its distance with one line saying JPL\'s\n  own uncertainty is not yet included (Tony: "We have been computing it\n  all along from Horizons ephemeris").\n- Descriptions and links: from the orrery\'s object dictionary, standard\n  and in the skill; Pluto\'s row uses NASA\'s Pluto page (L-395).\n- Work order, confirmed: the figures fix, then the dictionary export,\n  then step 3b.\n- L-397 "on a priority basis".\n- From Tony\'s notes on Where We Are: the Sun\'s opening view in the orrery\n  is "photosphere + 10%" (L-385); Earth\'s atmosphere "depends on the\n  source. Re is based on the equatorial radius. The crust is ~0.99...\n  Re" (L-389).\n\n## 3. What was built, verified\n\n| Patch | Repo | Pushed | Verified |\n|---|---|---|---|\n| patch_L363_7_half2_config_20260930.py | gallery | 1530bb6d | Tony\'s run: offline suite, six dry runs, first build, the six objects in the cache with their own windows covering today; read back live (all six @sun, ecliptic inclinations). Whole cache now trusted +/- 88 days (Mercury). |\n| patch_L397_cache_in_step_all_objects_20260930.py | gallery | f6d1ca95 | Tony\'s run: 19 of 19 gating checks. In the sandbox: fails against the pre-build cache naming the six new bodies; self-test catches a broken comparison. |\n| patch_L363_8_room_step3a_20260930.py | gallery | 432435a8 | Tony\'s run: all checks pass. Room\'s driver run in CPython on the real cache, compose run in Node: no warnings. NOT run in a browser by Claude; Tony viewed it live. |\n\n## 4. Found this session\n\n- The cache-in-step blind spot (L-397, fixed).\n- The orbit cross\'s text box gave the distance of an arbitrary point on\n  the orbit in exponent form; the word list had missed it. It now says\n  "Mercury\'s orbit" (Tony may reword).\n- Distance figures overclaim for the outer bodies (L-398, next).\n- Three entries in OBJECT_DEFINITIONS had a field written twice (Earth,\n  Moon, Patroclus-Menoetius Barycenter), the first silently discarded by\n  Python and invisible to the provenance scanner. Tony fixed them by\n  hand on 2026-10-01; not yet pushed when this was written. The export\n  (L-395) gets a duplicate-field check.\n- A stray folder data/solar-system (1) in Tony\'s gallery copy (L-400).\n\n## 5. Discrepancies\n\n- None between handoff and base: step 0 of the previous handoff had\n  landed (L-363 updated, L-391 to L-396 present, plan v35).\n\n## 6. Next session\n\n1. Confirm the orrery HEAD carries this closing patch and Tony\'s\n   dictionary fix (no entry in celestial_objects.py with a duplicated\n   field).\n2. L-398, the figures fix:\n   - orrery: three rows in constants_new.py, citing Folkner et al. 2014\n     (IPN Progress Report 42-196, abstract), stating each group\'s\n     accuracy as the place the source names; provenance-discipline gains\n     the computed-position rule and the "accuracy stated in words" case;\n     exported.\n   - gallery: each served object points at its group\'s row\n     (orrery_constant, mirrored); the page uses the larger of drift and\n     source accuracy; Apophis\'s line; interactive-exhibit records the\n     rooms section and served row words (label, about, source_note).\n3. L-395, the dictionary export (descriptions, NASA links, the\n   duplicate check).\n4. L-363 step 3b, the drawer, then Tony\'s phone check.\n\n## 7. Tony-actions, rolled up\n\n- (do) Run patch_L363_ledger_half2_step3a_20260930.py from the orrery\n  root; then orrery_maintenance_run.py; commit together with the\n  dictionary fix; push.\n- (do) Look inside data/solar-system (1) in the gallery copy, then\n  delete it (L-400).\n- (decide, optional) Reword the orbit crosses if wanted.\n'


def norm(raw):
    return raw.replace(b"\r\n", b"\n").decode("utf-8")


def ledger_fp(text):
    start, end = INDEX
    if start in text and end in text:
        a = text.index(start)
        b = text.index(end) + len(end)
        text = text[:a] + text[b:]
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def write(path, text, crlf):
    data = text.replace("\n", "\r\n") if crlf else text
    with open(path, "wb") as f:
        f.write(data.encode("utf-8"))


def main():
    if os.path.basename(os.getcwd()) == "documentation":
        raise SystemExit("ERROR: run this from the ORRERY repo ROOT, next to "
                         "palomas_orrery.py -- not from documentation/. "
                         "NOTHING was written.")
    if not os.path.isfile("palomas_orrery.py"):
        raise SystemExit("ERROR: palomas_orrery.py is not here, so this is "
                         "not the orrery root. NOTHING was written.")

    with open(LEDGER, "rb") as f:
        raw = f.read()
    crlf = b"\r\n" in raw
    text = norm(raw)
    fp = ledger_fp(text)
    if fp != LEDGER_FP:
        raise SystemExit("ERROR: %s is not the file this patch was built "
                         "against (fingerprint %s, expected %s). It has "
                         "changed since 10012821, or this patch has already "
                         "run. NOTHING was written." % (LEDGER, fp, LEDGER_FP))
    for label, old, new in EDITS:
        n = text.count(old)
        if n != 1:
            raise SystemExit("ANCHOR FAIL: %s -- %s: expected 1 match, found "
                             "%d. NOTHING was written." % (LEDGER, label, n))
        text = text.replace(old, new)

    page_crlf = False
    if os.path.exists(PAGE):
        with open(PAGE, "rb") as f:
            praw = f.read()
        page_crlf = b"\r\n" in praw
        pfp = hashlib.md5(norm(praw).encode("utf-8")).hexdigest()
        if pfp not in PAGE_FPS:
            raise SystemExit("ERROR: %s holds content this patch does not "
                             "know (fingerprint %s). NOTHING was written."
                             % (PAGE, pfp))
    if os.path.exists(HANDOFF):
        raise SystemExit("ERROR: %s already exists, so this patch has "
                         "probably run. NOTHING was written." % HANDOFF)

    write(LEDGER, text, crlf)
    for label, _old, _new in EDITS:
        print("ok  %s  %s" % (LEDGER, label))
    write(PAGE, PAGE_TEXT, page_crlf)
    print("ok  %s  rewritten" % PAGE)
    write(HANDOFF, HANDOFF_TEXT, False)
    print("ok  %s  new" % HANDOFF)
    print("")
    print("Stamps updated: the ledger's header line; Where We Are's date.")
    print("patch applied")
    print("")
    print("NEXT:")
    print("  1. python orrery_maintenance_run.py  (rebuilds the ledger index)")
    print("  2. Move this script into documentation/.")
    print("  3. Commit with your celestial_objects.py fix, and push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
