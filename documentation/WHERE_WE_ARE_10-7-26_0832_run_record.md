<!-- Doc-Kind: hand | Where the project is and where it is going, in plain words. One file, rewritten in place; read it at the end of every session. -->
# Where We Are

Last updated: October 6, 2026, end of the Earth website session.
- Written at orrery e7073fce and gallery 38f1e7b0, after your runs of
  the website patch and of the galactic-plane and panel-colour patches.

> **READ THIS FIRST**
>
> **Changed this session:**
> - Earth's website patch is live, and your look on the phone found it
>   correct. The inner belt says "trapped protons", in your words, and
>   Jupiter's belts no longer claim a measured distance.
> - The saved Earth scene the checks use is re-recorded from the real
>   data, with a tool that can remake it. That showed two hovers on the
>   live site were already too tall for the phone; with your approved
>   changes all three tall ones fit.
> - A search of both rooms found 17 facts typed in the code instead of
>   served with their sources. You ruled they are fixed now, as part of
>   finishing the Earth and Sun rooms. The plan is written down for a
>   fresh session.
> - A written rule now says code may type only words about our picture;
>   facts, papers and sources are served.
> - In the orrery, from a session of its own: the Celestial Grid draws
>   the galactic plane, a violet circle, with its poles, and the Star
>   Background marks Sagittarius A*, the galaxy's centre.
> - The desktop orrery opens on Linux and macOS again: its panels use
>   one grey, gray90, that every system knows.
>
> **Do next:**
> - *The typed facts, in a fresh session, from the plan written today.*
>
> **Needs you now:**
> - *Run this closing patch in the orrery repo, reinstall
>   interactive-exhibit, and replace the Project's instructions with
>   v3.84.*

How to read the marks:
- *Italic* lines are the must-reads.
- **>> UPDATED THIS SESSION** beside a heading means that section
  changed in the latest session.
- "<< new this session" beside a road stage marks a change to the road.
- Sections without a mark are as they were.
- The marks are cleared and reset at every session's update, so they
  always mean "new since you last read this."

## The goal

- Paloma's Orrery on the web.
- The website does what the desktop orrery does, in the browser, from
  data fetched from JPL each night, so a visitor never waits on JPL.
- Anyone can open it, with nothing to install.
- Built from the same code and the same checked numbers as the desktop
  orrery.
- The one real limit: the browser can show only the dates the saved
  data covers.
- Saved data covering one orbit of each body is enough, as you decided.
- Within that range, a visitor will be able to choose a date, and
  perhaps play time forward.

## The road  **>> UPDATED THIS SESSION**

  1. [done]   The Sun's room is live on the website.
  2. [done]   Earth's room is live, with every number traced to its source.
  3. [done]   The numbers come from one place: the orrery feeds the
              website, and nothing is typed twice.
  4. [done]   The Solar System room becomes a second way in: all the
              planets, a drawer to pick them, and a way into each
              body's own room.
  5. [NOW]    *Earth's old items are finished, in the order you
              confirmed.* << this session: the website patch is live;
              the typed facts are the last part, with the design talks.
  6. [next]   The facts typed in the Earth and Sun rooms' code move into
              the served data, with their sources. << new this session
  7. [next]   The Sun's numbers get the same checking Earth's got: the
              Sun's list, from its opening view.
  8. [next]   The served objects are checked against JPL Horizons, the
              way the numbers are checked against their sources.
  9. [next]   The website's checks get a short list of their own, so a
              new room or a moved front door can't break unnoticed.
 10. [next]   A bare interactive.html link opens the Solar System room,
              and the Explorer gets its own address. The lobby's wide
              Solar System card, its first half, is done.
 11. [later]  The rest of the orrery's objects come to the website --
              dwarf planets, asteroids, moons -- through the same
              connection that now carries the room's eleven bodies,
              checked against JPL Horizons.
 12. [later]  Encounters: comets and spacecraft shown at the dates
              that matter.
 13. [later]  The planets get their details -- layers, rings, magnetic
              fields -- Jupiter and Saturn first.
 14. [goal]   The website does what the desktop orrery does, from data
              fetched from JPL each night, with a date to choose and
              time to play within the range the data covers.

## Right now  **>> UPDATED THIS SESSION**

- Earth's website patch is live: 24 of 24 checks after the cache build,
  and your look on the phone found it correct.
  - The inner belt reads in your approved words, and the word
    "protons" comes from the served data, not the code.
  - Jupiter's three belts say only where they are drawn.
  - The geocorona note no longer says the orrery lacks its shell.
  - The collapsed-features check now runs in the website's maintenance
    run, so it counts 24, with its own dashboard button.
- The saved Earth scene was five weeks old. A new tool remakes it the
  way the page makes it, and the checks now see the live site as it is.
  - Seen that way, the rotation axis hover was 21 lines and the outer
    belt's 18, on the live site, over the phone's 17-line limit.
  - Your approved changes bring all three tall hovers to 17: the axis's
    layout, and one shorter sentence on both belts.
- The 17 typed facts: 13 in Earth's room, 4 in the Sun's. Most are
  already backed by a served source and only need moving; six need a
  source found and read, or removal with the gap noted.
- Jupiter's inner belt isn't in a website room yet, so its new words
  wait for a Jupiter room; the orrery's are correct, as you saw.
- The galactic plane in the orrery is in, and you found it good. Your
  two requests are recorded with it: the galactic tide is very faint
  and its X can't be made out, and the coordinate circles' descriptions
  could move to hover markers on the circles.
- The panels' grey: a shade darker than before, the grey of January to
  June. A look on Windows, and a run on a Mac when convenient.
- The skill copies this session loaded all matched the repo, and the
  ones you reinstalled read their new versions.

## The next three steps  **>> UPDATED THIS SESSION**

1. *Your run of this closing patch, and the reinstall.*
2. The typed facts move into the served data, in a fresh session, from
   `documentation/MANIFEST_L421_typed_facts_20261006.md`.
3. The Horizons check's design round, in its own session, from
   `documentation/HANDOFF_L395_horizons_check_design_20261005.md`.

## Waiting on you  **>> UPDATED THIS SESSION**

Now:
- Run this closing patch, run orrery_maintenance_run.py, commit and
  push.
- Reinstall interactive-exhibit (1.12) and replace the Project's
  instructions with PROJECT_INSTRUCTIONS.md, now v3.84.
- A look at the orrery's panels on Windows; a Mac run when convenient.

At the Horizons design round:
- What Horizons can confirm, what counts as agreement, where the check
  runs and how often, and what to do with pinned comet records.
- Whether this chat should be allowed to reach JPL.

At the next design talk:
- The fuzzy outer corona, designed together with the dust cloud. The
  exosphere is now a candidate for the same treatment.
- Moving the highlighted row to the top of the list.
- GO's arrow, only if the text box stays in the centre, as you ruled.
  If it can't, no arrow.
- Earth's design talks, the belts' shape first.

Decisions from the Fable sweep, one at a time when you're ready:
- Whether items inside an ordered list need RICE scores at all.
- A handful of scores it proposes.

Not urgent, in your order:
1. Whether the editor should also edit the words on the Solar System
   room's rows.
2. Choosing a date, and animation.
3. The scattered disk, with the Kuiper belt in the Solar System room.
   It is not the fuzzy boundary idea: the disk is a population of icy
   bodies, the fuzzy boundary is a way of drawing an edge. When the
   disk is designed, its edges would likely be drawn that way.

## Where the details are  **>> UPDATED THIS SESSION**

- Every item, done and open: `LEDGER_CONSOLIDATED.md`
  - This session: L-413 (Earth's list), L-349 (the belt's words),
    L-379 (the saved scene), L-300 (the collapsed-features check), L-292
    (the geocorona note), L-421 (the typed facts, opened). Closed: L-349
    (the belt's words), L-300 (the collapsed-features check), L-369
    (Earth's tilt in words), L-415 and L-419 (skill rules confirmed).
  - L-418 stays open only for splitting provenance-discipline's two
    long procedures into their own files.
  - The galactic plane: L-420; the panel colour: L-027; their record:
    `documentation/HANDOFF_L420_galactic_plane_20261006.md`.
- The plan for the typed facts:
  `documentation/MANIFEST_L421_typed_facts_20261006.md`
- This session's record:
  `documentation/HANDOFF_L413_earth_website_20261006.md`
- The skills' old version history: `documentation/SKILL_HISTORIES.md`
- The reasoning behind the order:
  `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md`
- For the Horizons round:
  `documentation/HANDOFF_L395_horizons_check_design_20261005.md`

  =====================================================================

  **Tony**: Run record:

  PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/patch_L421_1_served_hover_words_20261006.py
ok  documentation/payload_earth.json                 re-recorded whole
ok  documentation/payload_earth_scene.json           re-recorded whole
ok  data/objects_config.json                         L-421: "hover": "A ring in the equatorial plane, not a sphere: sate
ok  data/objects_config.json                         L-421: "source": "Derived: (GM_E / omega^2)^(1/3) from IERS Convent
ok  data/objects_config.json                         L-421: "hover": "Shue et al. (1998), for the solar wind assumed her
ok  data/objects_config.json                         L-421: "hover": "Jelinek et al. (2012), at dynamic pressure {pressu
ok  data/objects_config.json                         L-421: "hover": "The straight widening up to that point is our choi
ok  data/objects_config.json                         L-421: "source": "Alken et al. (2021), International Geomagnetic Re
ok  data/objects_config.json                         L-421: ],
ok  documentation/smoke_display_figures.js           L-421: //
ok  documentation/smoke_display_figures.js           L-421: const FIXTURE_AT = "8487b0f8";
ok  documentation/smoke_display_figures.js           L-421: "fixture_hovers_L421_on_8487b0f8.json");
ok  gallery/feature_renderers.js                     L-421: * Module updated: October 6, 2026 with Anthropic's Claude Op
ok  gallery/feature_renderers.js                     L-421: }
ok  gallery/feature_renderers.js                     L-421: // L-421: the band sentence is the belt's served hovers_band
ok  gallery/feature_renderers.js                     L-421: ? (bandWords === null ? "" :
ok  gallery/feature_renderers.js                     L-421: // L-379 (2026-10-06): Tony's approved words. L-421: they ar
ok  gallery/feature_renderers.js                     L-421: // L-421: the belt's served hovers_rings.
ok  gallery/feature_renderers.js                     L-421: // L-421: the ring's served hover words.
ok  gallery/feature_renderers.js                     L-421: // L-421: the paper, its conditions and its limits are the
ok  gallery/feature_renderers.js                     L-421: // L-421: the tail's served hover words.
ok  gallery/feature_renderers.js                     L-421: // L-421: the bow shock's served hover words. (The three-lin
ok  tools/exhibit_store_editor.py                    L-421: Updated October 6, 2026 with Anthropic's Claude Opus 5.5 (L-
ok  tools/exhibit_store_editor.py                    L-421: # `hover` (L-421): the facts a hover states, served rather t
ok  tools/exhibit_store_editor.py                    L-421: LONG_FIELDS = ("description", "about", "note", "source", "ho
ok  tools/exhibit_store_editor.py                    L-421: "numbers. Its hover sentences (hovers_band, "
ok  tools/store_writer.py                            L-421: Updated October 6, 2026 with Anthropic's Claude Opus 5.5 (L-
ok  tools/store_writer.py                            L-421: # `hover` (L-421, 2026-10-06): the facts a hover states, ser
ok  tools/store_writer.py                            L-421: # hovers_band, hovers_rings and hovers_plane (L-421) are the
ok  tools/store_writer.py                            L-421: "flux_peak_of", "hovers_band", "hovers_rings",
ok  documentation/fixture_hovers_L421_on_8487b0f8.json new file

patch applied

NEXT:
  1. Run the cache builder: the dashboard button 'Gallery Cache Builder
     -- Manual Run', or tools/gallery_cache_builder.py from this folder.
     Read its [SWAP] line. 

[RECOVER] removed retained data\solar-system.prev (cleared read-only on 6 entries)
[sweep] no sibling directories present
[POLE] earth: pole of 2026-10-07 served (RA 0.70498, Dec 89.85004 deg); tilt 23.43809 deg
[SWAP] the new cache is in place; every rename worked on the first try. Recorded in data/cache_swap_log.jsonl
[warn] sun: features-only entry; no Horizons fetch
[done] run 20261007T133935Z (nightly): 19 objects

----------------------------------------------------------------------
WHAT TO DO NEXT, before you commit anything:

  1. Run the gallery maintenance run, from this same folder:
         python gallery_maintenance_run.py
     Every gating checker should pass. Its LAST line reads the
     swap log back and should agree with the [SWAP] line above.

======================================================================
  gallery maintenance run -- OFFLINE (before a commit)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

GENERATORS -- rewritten every time; a no-op when nothing moved
  PASS Module atlas              1.4s  rewrote MODULE_ATLAS.md,
                                    MODULE_INDEX.md
  PASS Constants export pull     0.7s  no change to
                                    data/constants_export.json,
                                    data/constants_export.sha
  PASS Config mirror             0.1s  no change to
                                    data/objects_config.json
  PASS Objects export pull       0.5s  no change to
                                    data/objects_export.json,
                                    data/objects_export.sha
  PASS Objects mirror            0.1s  no change to
                                    data/objects_config.json

CHECKERS -- the verdict informs the push call
  PASS Cache builder suite      18.4s  PASS (229 checks, 0 failures)
  PASS Pole of date              0.3s  POLE OF DATE: all 11 checks passed
                                    (frame angle, orrery, ERFA, block
                                    checker, and each shown able to
                                    fail).
  PASS Mirror suite              0.1s  All 64 mirror checks passed:
                                    served, spelling, relabel refused
                                    and accepted, conflict refused,
                                    definition as exactly 1, fallback
                                    and absent named, no-slot refused,
                                    five shapes, formatting kept,
                                    idempotent, report writes nothing,
                                    uncertainty written as served,
                                    Earth's pole served, print count
                                    written as served, "in" written as
                                    served and a slot served in
                                    another unit from it.
  PASS Store writer suite       13.7s  All 322 store-writer checks
                                    passed: an allow list that lets
                                    through only a shell's words, a
                                    belt's words and the arrival
                                    settings, the rooms section's
                                    included; a no-edit round trip;
                                    one line per change; empty words
                                    handled; a refused batch writing
                                    nothing; awkward text; and the
                                    shell list matching the cache
                                    check's rule.
  PASS Store editor suite        0.3s  All 305 store-editor checks
                                    passed: every box the form offers
                                    is one the writer allows; the word
                                    list and the tick list differ by
                                    the belts, on purpose; nothing
                                    typed saves nothing; the save
                                    message does not promise a visitor
                                    sees what they cannot yet; and a
                                    red Cache in step is explained
                                    rather than just shown.
  PASS Objects mirror suite      0.2s  MIRROR OBJECTS SUITE: pass
  PASS Objects mirror check      0.1s  OBJECTS MIRROR: pass
  PASS Config mirror check       0.1s  Every served link holds the
                                    export's value, unit and figure
                                    count; 101 link(s) compared, store
                                    3b7000e368d1.
  PASS Pointer join              0.1s  Every link is accounted for: 108
                                    link(s) against orrery fbd223ee, 4
                                    fallback named; read check: 43 of
                                    43 measured rows reached carry a
                                    read.
  PASS Cache in step             0.1s  The served cache holds the
                                    config's 19 object(s) and their
                                    features exactly: 4 object(s) with
                                    35 named shell(s), in both cache
                                    files.
  PASS Collapsed features        0.1s  33 stored as themselves, 16
                                    collapsed, 0 unclassified.
  PASS Feature renderers         1.4s  === ALL CHECKS PASSED ===
  PASS Page framing              0.2s  === ALL CHECKS PASSED ===
  PASS Sun shells                0.3s  ALL CHECKS PASSED
  PASS Earth scene geometry      0.2s  === ALL CHECKS PASSED ===
  PASS Hover budget              0.2s  === ALL CHECKS PASSED ===
  PASS Arrival                   0.3s  Arrival: both rooms open on the
                                    right things; every shell trace
                                    carries its key; the fallback with
                                    no arrival block is unchanged.
  PASS Display figures           0.3s  === PASS: 57 hover(s) and 307
                                    number(s) examined; 13 graded, 7
                                    graded by line, 44 held to the
                                    fixture ===
  PASS Solar System figures      0.1s  === PASS: 6 worked cases, 11
                                    drawer rows matched to their
                                    accuracy rows, 10 served
                                    distances; Uranus, Neptune and
                                    Pluto print to JPL's ten-thousands
                                    place ===
  PASS Solar System drawer       0.1s  === PASS: the Sun is never ticked,
                                    See more hides only what is not
                                    ticked, the handle names the last
                                    body ticked, All / none leaves the
                                    Sun, rooms are offered only where
                                    they exist, and the page asks this
                                    file ===
  PASS Guest book                0.1s  === GUEST BOOK: all 8 checks
                                    passed
  PASS Guest book updater        0.4s  === GUEST BOOK UPDATER: all 43
                                    checks passed (6 scripted runs,
                                    self-test first)
  PASS Daily run steps           0.1s  === DAILY RUN: all 3 step scripts
                                    found
  PASS Artifact 1 assembler      0.3s  === ALL CHECKS PASSED -- 5
                                    verdicts and T3's feature set
                                    match the 2026-08-31 pin ===
  PASS Cache siblings            0.1s  RESULT: 1 directory in data/ the
                                    builder did not make: solar-system
                                    (1). Check whether they belong
                                    there; the newer .gitignore rules
                                    keep the known conflict-copy
                                    shapes out of git but do not
                                    remove anything.

======================================================================
  24 of 24 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Cache siblings         RESULT: 1 directory in data/ the builder
  last swap 2026-10-07T13:39:37.748519+00:00: succeeded first time
======================================================================

  After you push: python gallery_maintenance_run.py --live

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  2. In GitHub Desktop, look at the change list. A good build
     shows changed and added files and NO pile of deletions.
  3. Commit and push. -- 6fae15e09b1f094b5619521a78cfae82e33c8804
  4. After the push, check what the live site serves:
         python gallery_maintenance_run.py --live

======================================================================
  gallery maintenance run -- LIVE (after a push)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

LIVE -- what the deployed site actually serves

  fetching 15 files from https://palomasorrery.com/
    SERVED   interactive.html                               matches the working copy
    SERVED   gallery/feature_renderers.js                   matches the working copy
    SERVED   gallery/earth_geometry.js                      matches the working copy
    SERVED   gallery/assembler/resolver.py                  matches the working copy
    SERVED   gallery/assembler/__init__.py                  matches the working copy
    SERVED   data/solar-system/coverage_index.json          matches (the working copy is CRLF)
    SERVED   data/solar-system/feature_configs.json         matches (the working copy is CRLF)
    SERVED   data/solar-system/positions/voyager_1.json     matches the working copy
    SERVED   gallery/arrival.js                             matches the working copy
    SERVED   gallery/nav_cluster.js                         matches the working copy
    SERVED   gallery/solar_system_figures.js                matches the working copy
    SERVED   gallery/solar_system_drawer.js                 matches the working copy
    SERVED   data/objects_config.json                       matches the working copy
    SERVED   gallery/guestbook.js                           matches the working copy
    SERVED   data/guestbook.json                            matches the working copy

  PASS Served reachability       2.5s  all 15 files served and
                                    byte-identical to the working copy

  orrery export pinned at fbd223ee

  PASS Export freshness          0.2s  the served export is the orrery's
                                    at fbd223ee, byte for byte

  orrery HEAD fbd223ee
  examining 7 of 108 links; the other 101 are served from the export
    NOT IN STORE  planet_poles['Sun']              not a top-level constant in the store
                  /objects/0/features/orientation
    NOT IN STORE  planet_poles['Jupiter']          not a top-level constant in the store
                  /objects/2/features/orientation/pole
    NOT IN STORE  planet_poles['Saturn']           not a top-level constant in the store
                  /objects/3/features/orientation/pole
  7 pointers: 4 match, 0 DRIFT, 0 UNIT MISMATCH, 3 could not be examined.

  PASS Store drift               1.1s  7 pointers against orrery fbd223ee
                                    -- 4 match, 0 DRIFT, 0 UNIT
                                    MISMATCH, 3 could not be examined.

======================================================================
  2 of 2 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Store drift            7 pointers against orrery fbd223ee -- 4
  last swap 2026-10-07T13:39:37.748519+00:00: succeeded first time
======================================================================

  Offline pass: python gallery_maintenance_run.py

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>


TONY-ACTION ROLLUP for this run:
  (do)     steps 1 to 4 above, in that order.
----------------------------------------------------------------------

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  2. Run gallery_maintenance_run.py. Expect 24 of 24. A red Cache in
     step means step 1 has not run.
  3. Move this script into documentation/. Commit the config and the
     cache together, and push.
  4. On your phone, open Earth's room and read six hovers: the
     geostationary ring, the magnetopause, the bow shock, the
     magnetotail and both belts. Every word should be as it was; in
     the magnetopause and bow shock two lines may break in a different
     place. -- correct.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> 

Yes, it's enough when paired with a source I've already read. We don't need the 2018 report.

**What the correction gives us**
- Its Figure 1 caption gives the definition.
- If a body's spin angle increases with time, its rotation is prograde; Mercury and Jupiter are its examples.
- It does not say which way Earth turns. That was the part I wanted from the 2018 report's section 7.

**What fills the gap**
- The Naval Observatory's almanac glossary, which I read in full in Round 1, has three entries that settle it:
  - *Diurnal motion:* the sky's daily motion from east to west is caused by Earth's rotation. So Earth turns west to east.
  - *Earth Rotation Angle:* Earth's spin angle; its rate of change is Earth's angular velocity, so it increases with time. By the correction's definition, that is prograde.
  - *Direct motion:* counter-clockwise seen from the north pole is the same sense as west to east.
- Together these support every word of the hover: "prograde, west to east, counter-clockwise seen from above the north pole."

**What I'll do with it**
- The axis's panel source will cite the 2019 correction and the glossary.
- It will no longer cite the 2018 report's sections 2 and 7, because neither of us has read them this session.
- This goes into the second patch, with the axis.

The second patch is still waiting on the first. When you've run it, the pushed SHA is all I need.

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/patch_L421_2_served_guide_words_20261006.py
ok  documentation/payload_earth_scene.json           re-recorded whole
ok  data/objects_config.json                         L-421: "hover": "Drawn in clumps to show the cloud is not smooth; w
ok  data/objects_config.json                         L-421: "hover": "Drawn tilted to the galaxy's plane; how thick it i
ok  data/objects_config.json                         L-421: "note": "Same shape as the Sun's orientation block; read by 
ok  documentation/smoke_display_figures.js           L-421: //
ok  documentation/smoke_display_figures.js           L-421: const FIXTURE_AT = "b43cc515";
ok  documentation/smoke_display_figures.js           L-421: "fixture_hovers_L421_2_on_b43cc515.json");
ok  documentation/smoke_earth_geometry.js            L-421: // L-421: the terminator's words are served and wrap by the 
ok  documentation/smoke_earth_geometry.js            L-421: /FROZEN/.test(termPlain) && /no lighting is modelled/.test(t
ok  documentation/smoke_earth_geometry.js            L-421: /prograde, west to east/.test(axisG.find(t => t.mode === "ma
ok  documentation/smoke_earth_geometry.js            L-421: // L-421 (2026-10-06): the citation is SERVED on Earth's ori
ok  gallery/earth_geometry.js                        L-421: * Updated October 6, 2026 with Anthropic's Claude Opus 5.5 (
ok  gallery/earth_geometry.js                        L-421: }
ok  gallery/earth_geometry.js                        L-421: *   words           the served orientation block's `words` (
ok  gallery/earth_geometry.js                        L-421: // L-421 (2026-10-06): what a guide's hover says about natur
ok  gallery/earth_geometry.js                        L-421: guideWords("tilt") + "<br>";
ok  gallery/earth_geometry.js                        L-421: // The period sentence follows on the served sentence's last
ok  gallery/earth_geometry.js                        L-421: source: guideSource("sense") +
ok  gallery/earth_geometry.js                        L-421: guideWords("subsolar") + "<br>" +
ok  gallery/earth_geometry.js                        L-421: ", propagated to the epoch by the assembler's Kepler solver 
ok  gallery/earth_geometry.js                        L-421: guideWords("terminator",
ok  gallery/earth_geometry.js                        L-421: ? "(" + opts.planetRadius.source + ")" : "as served") + "." 
ok  gallery/earth_geometry.js                        L-421: guideWords("moon_arc") + "<br><br>" +
ok  gallery/earth_geometry.js                        L-421: source: "JPL Horizons osculating elements for the Moon about
ok  gallery/earth_geometry.js                        L-421: /* L-421: the pole of date's provenance, from the served rec
ok  gallery/earth_geometry.js                        L-421: // L-421 (2026-10-06): the query is printed from the record 
ok  gallery/earth_geometry.js                        L-421: words: orient.words || null,
ok  gallery/feature_renderers.js                     L-421: *   and hovers_plane -- and printed by servedHover(). No wor
ok  gallery/feature_renderers.js                     L-421: // L-421 (2026-10-06): the clumpy outer cloud's caveat and t
ok  gallery/feature_renderers.js                     L-421: (shape === "torus" ? HILLS_CAVEAT
ok  gallery/feature_renderers.js                     L-421: servedHover(cfg.hover, {}, where, warn);
ok  gallery/feature_renderers.js                     L-421: // L-421: so earth_geometry.js prints the guides' served wor
ok  interactive.html                                 L-421: .sun-frame-note .src { color: var(--text-secondary); font-si
ok  interactive.html                                 L-421: color: var(--text-secondary);
ok  interactive.html                                 L-421: /* L-421 (Tony, 2026-10-06, from the phone): the panel's wor
ok  documentation/fixture_hovers_L421_2_on_b43cc515.json new file

patch applied

NEXT:
  1. Run the cache builder: the dashboard button 'Gallery Cache Builder
     -- Manual Run', or tools/gallery_cache_builder.py from this folder.
     Read its [SWAP] line.

[RECOVER] removed retained data\solar-system.prev (cleared read-only on 6 entries)
[sweep] no sibling directories present
[POLE] earth: pole of 2026-10-07 served (RA 0.70498, Dec 89.85004 deg); tilt 23.43809 deg
[SWAP] the new cache is in place; every rename worked on the first try. Recorded in data/cache_swap_log.jsonl
[warn] sun: features-only entry; no Horizons fetch
[done] run 20261007T143110Z (nightly): 19 objects

----------------------------------------------------------------------
WHAT TO DO NEXT, before you commit anything:

  1. Run the gallery maintenance run, from this same folder:
         python gallery_maintenance_run.py
     Every gating checker should pass. Its LAST line reads the
     swap log back and should agree with the [SWAP] line above.
  2. In GitHub Desktop, look at the change list. A good build
     shows changed and added files and NO pile of deletions.
  3. Commit and push.
  4. After the push, check what the live site serves:
         python gallery_maintenance_run.py --live

TONY-ACTION ROLLUP for this run:
  (do)     steps 1 to 4 above, in that order.
----------------------------------------------------------------------

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  2. Run gallery_maintenance_run.py. Expect 24 of 24. A red Cache in
     step means step 1 has not run.

======================================================================
  gallery maintenance run -- OFFLINE (before a commit)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

GENERATORS -- rewritten every time; a no-op when nothing moved
  PASS Module atlas              1.5s  rewrote MODULE_ATLAS.md,
                                    MODULE_INDEX.md
  PASS Constants export pull     0.9s  rewrote data/constants_export.sha
  PASS Config mirror             0.1s  no change to
                                    data/objects_config.json
  PASS Objects export pull       0.6s  rewrote data/objects_export.sha
  PASS Objects mirror            0.1s  no change to
                                    data/objects_config.json

CHECKERS -- the verdict informs the push call
  PASS Cache builder suite      13.6s  PASS (229 checks, 0 failures)
  PASS Pole of date              0.2s  POLE OF DATE: all 11 checks passed
                                    (frame angle, orrery, ERFA, block
                                    checker, and each shown able to
                                    fail).
  PASS Mirror suite              0.1s  All 64 mirror checks passed:
                                    served, spelling, relabel refused
                                    and accepted, conflict refused,
                                    definition as exactly 1, fallback
                                    and absent named, no-slot refused,
                                    five shapes, formatting kept,
                                    idempotent, report writes nothing,
                                    uncertainty written as served,
                                    Earth's pole served, print count
                                    written as served, "in" written as
                                    served and a slot served in
                                    another unit from it.
  PASS Store writer suite        8.0s  All 322 store-writer checks
                                    passed: an allow list that lets
                                    through only a shell's words, a
                                    belt's words and the arrival
                                    settings, the rooms section's
                                    included; a no-edit round trip;
                                    one line per change; empty words
                                    handled; a refused batch writing
                                    nothing; awkward text; and the
                                    shell list matching the cache
                                    check's rule.
  PASS Store editor suite        0.1s  All 305 store-editor checks
                                    passed: every box the form offers
                                    is one the writer allows; the word
                                    list and the tick list differ by
                                    the belts, on purpose; nothing
                                    typed saves nothing; the save
                                    message does not promise a visitor
                                    sees what they cannot yet; and a
                                    red Cache in step is explained
                                    rather than just shown.
  PASS Objects mirror suite      0.1s  MIRROR OBJECTS SUITE: pass
  PASS Objects mirror check      0.1s  OBJECTS MIRROR: pass
  PASS Config mirror check       0.1s  Every served link holds the
                                    export's value, unit and figure
                                    count; 101 link(s) compared, store
                                    3b7000e368d1.
  PASS Pointer join              0.1s  Every link is accounted for: 108
                                    link(s) against orrery 12693a53, 4
                                    fallback named; read check: 43 of
                                    43 measured rows reached carry a
                                    read.
  PASS Cache in step             0.1s  The served cache holds the
                                    config's 19 object(s) and their
                                    features exactly: 4 object(s) with
                                    35 named shell(s), in both cache
                                    files.
  PASS Collapsed features        0.1s  33 stored as themselves, 16
                                    collapsed, 0 unclassified.
  PASS Feature renderers         0.8s  === ALL CHECKS PASSED ===
  PASS Page framing              0.1s  === ALL CHECKS PASSED ===
  PASS Sun shells                0.2s  ALL CHECKS PASSED
  PASS Earth scene geometry      0.1s  === ALL CHECKS PASSED ===
  PASS Hover budget              0.2s  === ALL CHECKS PASSED ===
  PASS Arrival                   0.2s  Arrival: both rooms open on the
                                    right things; every shell trace
                                    carries its key; the fallback with
                                    no arrival block is unchanged.
  PASS Display figures           0.2s  === PASS: 57 hover(s) and 307
                                    number(s) examined; 13 graded, 7
                                    graded by line, 44 held to the
                                    fixture ===
  PASS Solar System figures      0.1s  === PASS: 6 worked cases, 11
                                    drawer rows matched to their
                                    accuracy rows, 10 served
                                    distances; Uranus, Neptune and
                                    Pluto print to JPL's ten-thousands
                                    place ===
  PASS Solar System drawer       0.1s  === PASS: the Sun is never ticked,
                                    See more hides only what is not
                                    ticked, the handle names the last
                                    body ticked, All / none leaves the
                                    Sun, rooms are offered only where
                                    they exist, and the page asks this
                                    file ===
  PASS Guest book                0.1s  === GUEST BOOK: all 8 checks
                                    passed
  PASS Guest book updater        0.2s  === GUEST BOOK UPDATER: all 43
                                    checks passed (6 scripted runs,
                                    self-test first)
  PASS Daily run steps           0.1s  === DAILY RUN: all 3 step scripts
                                    found
  PASS Artifact 1 assembler      0.2s  === ALL CHECKS PASSED -- 5
                                    verdicts and T3's feature set
                                    match the 2026-08-31 pin ===
  PASS Cache siblings            0.1s  RESULT: 2 directories in data/ the
                                    builder did not make: solar-system
                                    (1), solar-system (2). Check
                                    whether they belong there; the
                                    newer .gitignore rules keep the
                                    known conflict-copy shapes out of
                                    git but do not remove anything.

======================================================================
  24 of 24 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Cache siblings         RESULT: 2 directories in data/ the
  last swap 2026-10-07T14:31:12.817167+00:00: succeeded first time
======================================================================

  After you push: python gallery_maintenance_run.py --live

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  3. Move this script into documentation/. Commit the config and the
     cache together, and push. -- 4cfeca27d2a84171a0b278e20b1f79cf606a1f0b
  4. On your phone, in Earth's room, read the rotation axis, the Sun
     line, the terminator and the Moon's arc; in the Sun's room, the
     clumpy outer cloud and the galactic tide. Every word should be as
     it was. Then open a panel: the words and the footer line should
     be easier to read.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> 

===============================================================================

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/patch_L420_4_circle_hovers_and_tide_20261006.py
ok  LEDGER_CONSOLIDATED.md                           header stamp
ok  LEDGER_CONSOLIDATED.md                           L-420 after the look
ok  LEDGER_CONSOLIDATED.md                           L-408 date
ok  LEDGER_CONSOLIDATED.md                           L-408: the orrery has the plane
ok  LEDGER_CONSOLIDATED.md                           L-027: run and pushed
ok  documentation/HANDOFF_L420_galactic_plane_20261006.md after the look: section
ok  documentation/HANDOFF_L420_galactic_plane_20261006.md after the look: Where We Are lines
ok  documentation/HANDOFF_L420_galactic_plane_20261006.md after the look: Tony-actions
ok  documentation/HANDOFF_L420_galactic_plane_20261006.md after the look: next session
ok  palomas_orrery.py                                docstring stamp (L-420, the box)
ok  palomas_orrery.py                                static plot box: circle lines move to hovers
ok  palomas_orrery.py                                animation box: circle lines move to hovers
ok  solar_visualization_shells.py                    docstring stamp (L-420, the tide)
ok  solar_visualization_shells.py                    tide: 5,000 points by default
ok  solar_visualization_shells.py                    tide docstring: the cone
ok  solar_visualization_shells.py                    tide docstring: the point count
ok  solar_visualization_shells.py                    tide hover: the cone line
ok  solar_visualization_shells.py                    tide points: brighter
ok  solar_visualization_shells.py                    tide: the cone
ok  solar_visualization_shells.py                    tide returns the cone
ok  star_sphere_builder.py                           docstring stamp (L-420, the circle hovers)
ok  star_sphere_builder.py                           the circles' cross places and words
ok  star_sphere_builder.py                           build_galactic_grid docstring: the info point
ok  star_sphere_builder.py                           build_galactic_grid returns the info point
ok  star_sphere_builder.py                           one hover cross per circle

patch applied

NEXT:
  1. Run orrery_maintenance_run.py; the gating checkers pass.

======================================================================
MAINTENANCE RUN -- generators, then checkers (L-188)
======================================================================
  Provenance scan is current (last run 20261006T190614Z, 1 day(s) ago).

GENERATORS -- regenerate every time; a no-op when nothing moved
----------------------------------------------------------------------
  Ledger index                 1.7s  rewrote LEDGER_CONSOLIDATED.md
  Skill manifest               0.2s  unchanged (1 of 1 rewritten, content
                                     identical)
  Constants export             1.0s  unchanged (1 checked, not written)
  Objects export               0.1s  unchanged (1 checked, not written)
  Module atlas                 7.0s  rewrote MODULE_ATLAS.md, MODULE_INDEX.md
  Data inventory               5.4s  rewrote DATA_INVENTORY.md
  Exact rows report            2.0s  rewrote EXACT_ROWS_PRINTED.md -- 13 of 34
                                     exact rows printed at 42 lines (32 orrery,
                                     10 gallery); 8 drawn only, 11 not followed,
                                     0 map entries broken
  Document index               0.1s  unchanged (1 checked, not written)

CHECKERS -- verdict informs the push call
----------------------------------------------------------------------
  Constants change             0.2s  No changes to constants_new.py since HEAD.
  Constants relations          0.3s  25 of 25 provenance tests passed against
                                     constants_new.py. No constants have drifted.
  Derived figures              0.8s  No figure count exceeds its inputs: 36
                                     derived row(s) read, 26 judged OK -- 26 OK,
                                     10 NOT YET MIGRATED, 1 NO DERIVED LINE, 1
                                     UNMARKED CONVERSION; 18 conversion(s)
                                     checked.
  Constants export check       1.5s  Export matches the store: sha256
                                     3b7000e368d1 on both sides; 105 rows
                                     re-read, 56 not exported, 27 tokens; 310
                                     conversions re-computed, 10 of 10 worked
                                     cases hold.
  Objects export check         0.1s  pass
  Skill headers                0.2s  11 skills parsed, no consistency problems.
  Exact rows by the count      1.7s  PASSING -- 13 printed exact rows each state
                                     a count; 32 orrery lines print through
                                     exact_text() or row_text(); 10 gallery lines
                                     are served the count
  Dimensions                   1.3s  No unit contradicts its arithmetic: 54
                                     derived row(s) read -- 42 OK, 9 NO UNIT, 3
                                     NOT CHECKABLE.
  Cross-check annotations      0.1s  19 of 19 cross-check annotation tests
                                     passed.
  Citation inheritance         0.1s  20 of 20 citation-inheritance tests passed.
  Status lines                 0.1s  All 105 status lines in constants_new.py are
                                     well formed; 53 rows carry none.
  Row shape                    0.1s  All 161 row shapes in constants_new.py fit
                                     the assignment's own line.
  Scanner recognition 1d/1e    0.3s  27 of 27 recognition pins hold: real
                                     citations recognized, fake ones refused.
  Reset completeness          24.2s  PASS -- all 310 IntVars + 3 StringVars + 10
                                     entries reset to startup defaults; date set
                                     to now.
  Orbit cache                  2.4s  All 6 orbit cache tests passed: cache loads,
                                     old formats convert, corrupted entries are
                                     dropped.
  Earth pole of date           0.3s  all 14 checks passed (geometry, ERFA,
                                     fallback, cache, hover, transform).
  Worksheet checker            9.5s  74 of 110 routed, 8 clean
  Worksheet checker tests     16.3s  All 135 checks passed
  Worksheet key round trip     1.1s  RESULT: 52 sites minted 52 distinct keys,
                                     all resolved; 52 pinned keys still resolve;
                                     1 retired keys confirmed gone.
  Builder marker join         25.1s  All 76 checks passed
  Extractor pins               0.4s  RESULT: 29 string sites carry the pinned 73
                                     claims and 14 instruction drops, at LOOKBACK
                                     30 / LOOKAHEAD 25, extractor version 2.
  Provenance scanner          11.8s  297 TIER-1 FINDINGS IN THE SCANNED TREE

======================================================================
  20 of 20 gating checkers passed -- 115.6s total
  2 report-only, exit 0 whatever they find:
    Worksheet checker           74 of 110 routed, 8 clean
    Provenance scanner          297 TIER-1 FINDINGS IN THE SCANNED TREE
======================================================================

FILES WRITTEN THIS RUN
----------------------------------------------------------------------
  2089 file(s) examined, 10 written, 0 created, 0 removed, 4 rewritten identically
    written   DATA_INVENTORY.md
    written   EXACT_ROWS_PRINTED.md
    written   LEDGER_CONSOLIDATED.md
    written   MODULE_ATLAS.md
    written   MODULE_INDEX.md
    written   PROVENANCE_AUDIT.md
    written   WORKSHEET_CHECK.md
    written   data/provenance_history.json
    written   documentation/WHERE_WE_ARE_10-7-26_0832_run_record.md
    written   documentation/prompts/citation_review.jsonl
    rewritten with identical bytes, no action needed:
      PROJECT_INSTRUCTIONS.md
      data/worksheet_check_state.json
      data/worksheet_routed.json
      test_output/test_orbit_paths.json
    20 file(s) over 2 MB compared by size and mtime only

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>

  2. Move this script into documentation/, commit and push. -- 12693a53f9cb57c6beacada13f307985842b1780
  3. Your look: plot the Sun with Galactic Tide, Celestial Grid and
     Star Background on. Turn until the violet circle is edge-on and
     look at the tide and its cone; hover the circles' three crosses. -- correct
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/patch_L420_5_close_20261007.py
ok  LEDGER_CONSOLIDATED.md                                   header stamp
ok  LEDGER_CONSOLIDATED.md                                   L-420 closed and moved to section C
ok  documentation/HANDOFF_L420_galactic_plane_20261006.md    closing section
ok  documentation/HANDOFF_L420_galactic_plane_20261006.md    Where We Are lines
ok  documentation/HANDOFF_L420_galactic_plane_20261006.md    Next session

patch applied

NEXT:
  1. Move this script into documentation/ FIRST, so the maintenance
     run does not count it (it did in your last two runs).
  2. Run orrery_maintenance_run.py; the ledger index moves L-420 to
     the closed table.

======================================================================
MAINTENANCE RUN -- generators, then checkers (L-188)
======================================================================
  Provenance scan is current (last run 20261007T134806Z, 0 day(s) ago).

GENERATORS -- regenerate every time; a no-op when nothing moved
----------------------------------------------------------------------
  Ledger index                 1.3s  rewrote LEDGER_CONSOLIDATED.md
  Skill manifest               0.2s  unchanged (1 of 1 rewritten, content
                                     identical)
  Constants export             0.9s  unchanged (1 checked, not written)
  Objects export               0.1s  unchanged (1 checked, not written)
  Module atlas                 6.9s  rewrote MODULE_ATLAS.md, MODULE_INDEX.md
  Data inventory               5.2s  rewrote DATA_INVENTORY.md
  Exact rows report            1.9s  rewrote EXACT_ROWS_PRINTED.md -- 13 of 34
                                     exact rows printed at 42 lines (32 orrery,
                                     10 gallery); 8 drawn only, 11 not followed,
                                     0 map entries broken
  Document index               0.1s  unchanged (1 checked, not written)

CHECKERS -- verdict informs the push call
----------------------------------------------------------------------
  Constants change             0.2s  No changes to constants_new.py since HEAD.
  Constants relations          0.2s  25 of 25 provenance tests passed against
                                     constants_new.py. No constants have drifted.
  Derived figures              0.9s  No figure count exceeds its inputs: 36
                                     derived row(s) read, 26 judged OK -- 26 OK,
                                     10 NOT YET MIGRATED, 1 NO DERIVED LINE, 1
                                     UNMARKED CONVERSION; 18 conversion(s)
                                     checked.
  Constants export check       1.2s  Export matches the store: sha256
                                     3b7000e368d1 on both sides; 105 rows
                                     re-read, 56 not exported, 27 tokens; 310
                                     conversions re-computed, 10 of 10 worked
                                     cases hold.
  Objects export check         0.1s  pass
  Skill headers                0.2s  11 skills parsed, no consistency problems.
  Exact rows by the count      1.3s  PASSING -- 13 printed exact rows each state
                                     a count; 32 orrery lines print through
                                     exact_text() or row_text(); 10 gallery lines
                                     are served the count
  Dimensions                   1.4s  No unit contradicts its arithmetic: 54
                                     derived row(s) read -- 42 OK, 9 NO UNIT, 3
                                     NOT CHECKABLE.
  Cross-check annotations      0.1s  19 of 19 cross-check annotation tests
                                     passed.
  Citation inheritance         0.1s  20 of 20 citation-inheritance tests passed.
  Status lines                 0.1s  All 105 status lines in constants_new.py are
                                     well formed; 53 rows carry none.
  Row shape                    0.1s  All 161 row shapes in constants_new.py fit
                                     the assignment's own line.
  Scanner recognition 1d/1e    0.2s  27 of 27 recognition pins hold: real
                                     citations recognized, fake ones refused.
  Reset completeness          20.9s  PASS -- all 310 IntVars + 3 StringVars + 10
                                     entries reset to startup defaults; date set
                                     to now.
  Orbit cache                  2.1s  All 6 orbit cache tests passed: cache loads,
                                     old formats convert, corrupted entries are
                                     dropped.
  Earth pole of date           0.3s  all 14 checks passed (geometry, ERFA,
                                     fallback, cache, hover, transform).
  Worksheet checker            8.3s  74 of 110 routed, 8 clean
  Worksheet checker tests     17.6s  All 135 checks passed
  Worksheet key round trip     1.4s  RESULT: 52 sites minted 52 distinct keys,
                                     all resolved; 52 pinned keys still resolve;
                                     1 retired keys confirmed gone.
  Builder marker join         26.8s  All 76 checks passed
  Extractor pins               0.5s  RESULT: 29 string sites carry the pinned 73
                                     claims and 14 instruction drops, at LOOKBACK
                                     30 / LOOKAHEAD 25, extractor version 2.
  Provenance scanner          11.8s  296 TIER-1 FINDINGS IN THE SCANNED TREE

======================================================================
  20 of 20 gating checkers passed -- 112.5s total
  2 report-only, exit 0 whatever they find:
    Worksheet checker           74 of 110 routed, 8 clean
    Provenance scanner          296 TIER-1 FINDINGS IN THE SCANNED TREE
======================================================================

FILES WRITTEN THIS RUN
----------------------------------------------------------------------
  2090 file(s) examined, 9 written, 0 created, 0 removed, 5 rewritten identically
    written   DATA_INVENTORY.md
    written   EXACT_ROWS_PRINTED.md
    written   LEDGER_CONSOLIDATED.md
    written   MODULE_ATLAS.md
    written   MODULE_INDEX.md
    written   PROVENANCE_AUDIT.md
    written   WORKSHEET_CHECK.md
    written   data/provenance_history.json
    written   documentation/prompts/citation_review.jsonl
    rewritten with identical bytes, no action needed:
      PROJECT_INSTRUCTIONS.md
      data/worksheet_check_state.json
      data/worksheet_routed.json
      test_output/test_orbit_paths.json
      window_config.json
    20 file(s) over 2 MB compared by size and mtime only

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>

  3. Commit and push. -- 8c457b7d291c3359b8e8368797dd47a3fe580f00
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 

Your push is confirmed at 8c457b7, and with the script moved first, the scanner read 296. L-420 is closed.

Here are the two items still waiting on you.

**1. A look at the orrery's panels on Windows (L-027).**
This is the colour fix from yesterday. The orrery's control window, the Tkinter panels with the checkboxes and buttons, not the plot in the browser, now uses a light grey called `gray90` everywhere. It is the grey you chose in January and used until June, a shade darker than the Windows grey the panels have shown since June. All I need is your word that the panels look right. -- confirmed.

A test on a Mac, whenever you have one handy, would confirm the last system, but it isn't required to close the item.

**2. The phone's design decision (L-408).**
The desktop orrery now draws four things the phone's Sun room does not: the galactic plane, its poles, Sgr A*, and the tide's cone with its brighter points. The phone's Sun room already draws the tide itself. The question is whether the phone should get these too. It's a design question rather than a quick look, so it belongs in a design talk; nothing is blocked while it waits.

================================================================

Here is the order. Every one of these runs from the orrery root with the Run button.

1. **patch_L027_2** (Opus, the panel colour confirmed). Records only.

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/patch_L027_2_panels_confirmed_20261007.py
ok  LEDGER_CONSOLIDATED.md                                   header stamp
ok  LEDGER_CONSOLIDATED.md                                   L-027 date
ok  LEDGER_CONSOLIDATED.md                                   L-027 panels confirmed
ok  LEDGER_CONSOLIDATED.md                                   L-408 awaits the design talk
ok  documentation/HANDOFF_L420_galactic_plane_20261006.md    Where We Are: panels done
ok  documentation/HANDOFF_L420_galactic_plane_20261006.md    Next session: L-027

patch applied

NEXT:
  1. Move this script into documentation/ first.
  2. Run orrery_maintenance_run.py.

======================================================================
MAINTENANCE RUN -- generators, then checkers (L-188)
======================================================================
  Provenance scan is current (last run 20261007T192404Z, 1 day(s) ago).

GENERATORS -- regenerate every time; a no-op when nothing moved
----------------------------------------------------------------------
  Ledger index                 1.9s  rewrote LEDGER_CONSOLIDATED.md
  Skill manifest               0.2s  unchanged (1 of 1 rewritten, content
                                     identical)
  Constants export             1.8s  unchanged (1 checked, not written)
  Objects export               0.1s  unchanged (1 checked, not written)
  Module atlas                 9.8s  rewrote MODULE_ATLAS.md, MODULE_INDEX.md
  Data inventory               6.2s  rewrote DATA_INVENTORY.md
  Exact rows report            3.0s  unchanged (1 checked, not written) -- 13 of
                                     34 exact rows printed at 42 lines (32
                                     orrery, 10 gallery); 8 drawn only, 11 not
                                     followed, 0 map entries broken
  Document index               0.1s  unchanged (1 checked, not written)

CHECKERS -- verdict informs the push call
----------------------------------------------------------------------
  Constants change             0.3s  No changes to constants_new.py since HEAD.
  Constants relations          0.3s  25 of 25 provenance tests passed against
                                     constants_new.py. No constants have drifted.
  Derived figures              1.0s  No figure count exceeds its inputs: 36
                                     derived row(s) read, 26 judged OK -- 26 OK,
                                     10 NOT YET MIGRATED, 1 NO DERIVED LINE, 1
                                     UNMARKED CONVERSION; 18 conversion(s)
                                     checked.
  Constants export check       1.8s  Export matches the store: sha256
                                     3b7000e368d1 on both sides; 105 rows
                                     re-read, 56 not exported, 27 tokens; 310
                                     conversions re-computed, 10 of 10 worked
                                     cases hold.
  Objects export check         0.1s  pass
  Skill headers                0.3s  11 skills parsed, no consistency problems.
  Exact rows by the count      1.9s  PASSING -- 13 printed exact rows each state
                                     a count; 32 orrery lines print through
                                     exact_text() or row_text(); 10 gallery lines
                                     are served the count
  Dimensions                   1.6s  No unit contradicts its arithmetic: 54
                                     derived row(s) read -- 42 OK, 9 NO UNIT, 3
                                     NOT CHECKABLE.
  Cross-check annotations      0.2s  19 of 19 cross-check annotation tests
                                     passed.
  Citation inheritance         0.2s  20 of 20 citation-inheritance tests passed.
  Status lines                 0.2s  All 105 status lines in constants_new.py are
                                     well formed; 53 rows carry none.
  Row shape                    0.1s  All 161 row shapes in constants_new.py fit
                                     the assignment's own line.
  Scanner recognition 1d/1e    0.4s  27 of 27 recognition pins hold: real
                                     citations recognized, fake ones refused.
  Reset completeness          28.7s  PASS -- all 310 IntVars + 3 StringVars + 10
                                     entries reset to startup defaults; date set
                                     to now.
  Orbit cache                  2.6s  All 6 orbit cache tests passed: cache loads,
                                     old formats convert, corrupted entries are
                                     dropped.
  Earth pole of date           0.6s  all 14 checks passed (geometry, ERFA,
                                     fallback, cache, hover, transform).
  Worksheet checker           13.5s  74 of 110 routed, 8 clean
  Worksheet checker tests     22.4s  All 135 checks passed
  Worksheet key round trip     1.4s  RESULT: 52 sites minted 52 distinct keys,
                                     all resolved; 52 pinned keys still resolve;
                                     1 retired keys confirmed gone.
  Builder marker join         27.3s  All 76 checks passed
  Extractor pins               0.4s  RESULT: 29 string sites carry the pinned 73
                                     claims and 14 instruction drops, at LOOKBACK
                                     30 / LOOKAHEAD 25, extractor version 2.
  Provenance scanner          11.3s  296 TIER-1 FINDINGS IN THE SCANNED TREE

======================================================================
  20 of 20 gating checkers passed -- 139.7s total
  2 report-only, exit 0 whatever they find:
    Worksheet checker           74 of 110 routed, 8 clean
    Provenance scanner          296 TIER-1 FINDINGS IN THE SCANNED TREE
======================================================================

FILES WRITTEN THIS RUN
----------------------------------------------------------------------
  2105 file(s) examined, 8 written, 0 created, 0 removed, 5 rewritten identically
    written   DATA_INVENTORY.md
    written   LEDGER_CONSOLIDATED.md
    written   MODULE_ATLAS.md
    written   MODULE_INDEX.md
    written   PROVENANCE_AUDIT.md
    written   WORKSHEET_CHECK.md
    written   data/provenance_history.json
    written   documentation/prompts/citation_review.jsonl
    rewritten with identical bytes, no action needed:
      PROJECT_INSTRUCTIONS.md
      data/worksheet_check_state.json
      data/worksheet_routed.json
      test_output/test_orbit_paths.json
      window_config.json
    20 file(s) over 2 MB compared by size and mtime only

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>

  3. Commit and push. -- 3f4c01e287ce3fd265d60bce0a3ec00321900785
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 

2. **patch_L418_2** (Opus, the split design closed). It rewrites the page whole, so it goes before anything else that touches the page.

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/patch_L418_2_split_design_close_20261006.py
  ok  ledger: L-418
  ok  ledger: header stamp
  ok  Where We Are: header
  ok  Where We Are: Read this first
  ok  Where We Are: road mark cleared
  ok  Where We Are: road stage 5 mark cleared
  ok  Where We Are: road stage 6 mark cleared
  ok  Where We Are: Right now
  ok  Where We Are: next steps, item 1
  ok  Where We Are: next steps, the split
  ok  Where We Are: Waiting on you
  ok  Where We Are: details, handles
  ok  Where We Are: details, records
  ok  documentation/PREDESIGN_L418_provenance_skill_split_20261006.md: already the ruled copy
  ok  documentation/HANDOFF_L418_skill_split_design_20261006.md: written
Notes of yours carried into the handoff: 0
Stamps updated: the ledger's header stamp; Where We Are's 'Last updated' lines.
patch applied (1509431 bytes in 3 files)
NEXT
1. Move this script into documentation/.
2. Run orrery_maintenance_run.py. This patch touches only the ledger
   and three documents, so it should report as it did before.

OK: 416 L-blocks parsed, no consistency problems.
Index regenerated (238 live items) in C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\LEDGER_CONSOLIDATED.md.

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>

======================================================================
MAINTENANCE RUN -- generators, then checkers (L-188)
======================================================================
  Provenance scan is current (last run 20261008T004636Z, 0 day(s) ago).

GENERATORS -- regenerate every time; a no-op when nothing moved
----------------------------------------------------------------------
  Ledger index                 1.3s  unchanged (1 of 1 rewritten, content
                                     identical)
  Skill manifest               0.2s  unchanged (1 of 1 rewritten, content
                                     identical)
  Constants export             0.8s  unchanged (1 checked, not written)
  Objects export               0.1s  unchanged (1 checked, not written)
  Module atlas                 6.5s  rewrote MODULE_ATLAS.md, MODULE_INDEX.md
  Data inventory               5.0s  unchanged (1 of 1 rewritten, content
                                     identical)
  Exact rows report            1.6s  unchanged (1 checked, not written) -- 13 of
                                     34 exact rows printed at 42 lines (32
                                     orrery, 10 gallery); 8 drawn only, 11 not
                                     followed, 0 map entries broken
  Document index               0.1s  unchanged (1 checked, not written)

CHECKERS -- verdict informs the push call
----------------------------------------------------------------------
  Constants change             0.2s  No changes to constants_new.py since HEAD.
  Constants relations          0.3s  25 of 25 provenance tests passed against
                                     constants_new.py. No constants have drifted.
  Derived figures              0.9s  No figure count exceeds its inputs: 36
                                     derived row(s) read, 26 judged OK -- 26 OK,
                                     10 NOT YET MIGRATED, 1 NO DERIVED LINE, 1
                                     UNMARKED CONVERSION; 18 conversion(s)
                                     checked.
  Constants export check       1.4s  Export matches the store: sha256
                                     3b7000e368d1 on both sides; 105 rows
                                     re-read, 56 not exported, 27 tokens; 310
                                     conversions re-computed, 10 of 10 worked
                                     cases hold.
  Objects export check         0.1s  pass
  Skill headers                0.2s  11 skills parsed, no consistency problems.
  Exact rows by the count      1.4s  PASSING -- 13 printed exact rows each state
                                     a count; 32 orrery lines print through
                                     exact_text() or row_text(); 10 gallery lines
                                     are served the count
  Dimensions                   1.0s  No unit contradicts its arithmetic: 54
                                     derived row(s) read -- 42 OK, 9 NO UNIT, 3
                                     NOT CHECKABLE.
  Cross-check annotations      0.1s  19 of 19 cross-check annotation tests
                                     passed.
  Citation inheritance         0.1s  20 of 20 citation-inheritance tests passed.
  Status lines                 0.1s  All 105 status lines in constants_new.py are
                                     well formed; 53 rows carry none.
  Row shape                    0.1s  All 161 row shapes in constants_new.py fit
                                     the assignment's own line.
  Scanner recognition 1d/1e    0.2s  27 of 27 recognition pins hold: real
                                     citations recognized, fake ones refused.
  Reset completeness          13.0s  PASS -- all 310 IntVars + 3 StringVars + 10
                                     entries reset to startup defaults; date set
                                     to now.
  Orbit cache                  1.8s  All 6 orbit cache tests passed: cache loads,
                                     old formats convert, corrupted entries are
                                     dropped.
  Earth pole of date           0.3s  all 14 checks passed (geometry, ERFA,
                                     fallback, cache, hover, transform).
  Worksheet checker            9.5s  74 of 110 routed, 8 clean
  Worksheet checker tests     16.0s  All 135 checks passed
  Worksheet key round trip     0.9s  RESULT: 52 sites minted 52 distinct keys,
                                     all resolved; 52 pinned keys still resolve;
                                     1 retired keys confirmed gone.
  Builder marker join         18.7s  All 76 checks passed
  Extractor pins               0.4s  RESULT: 29 string sites carry the pinned 73
                                     claims and 14 instruction drops, at LOOKBACK
                                     30 / LOOKAHEAD 25, extractor version 2.
  Provenance scanner           9.1s  296 TIER-1 FINDINGS IN THE SCANNED TREE

======================================================================
  20 of 20 gating checkers passed -- 91.4s total
  2 report-only, exit 0 whatever they find:
    Worksheet checker           74 of 110 routed, 8 clean
    Provenance scanner          296 TIER-1 FINDINGS IN THE SCANNED TREE
======================================================================

FILES WRITTEN THIS RUN
----------------------------------------------------------------------
  2106 file(s) examined, 6 written, 0 created, 0 removed, 6 rewritten identically
    written   MODULE_ATLAS.md
    written   MODULE_INDEX.md
    written   PROVENANCE_AUDIT.md
    written   WORKSHEET_CHECK.md
    written   data/provenance_history.json
    written   documentation/prompts/citation_review.jsonl
    rewritten with identical bytes, no action needed:
      DATA_INVENTORY.md
      LEDGER_CONSOLIDATED.md
      PROJECT_INSTRUCTIONS.md
      data/worksheet_check_state.json
      data/worksheet_routed.json
      test_output/test_orbit_paths.json
    20 file(s) over 2 MB compared by size and mtime only

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>

3. Commit and push. -- d43a0191b5a737e5a569c0f83cce468cacc7c892 and a1b4d4fbffbc73057c952a117e23697a8a22c3b4
4. Install the trial skill: in Settings, under Skills, Upload skill,
   and choose install-probe.zip. Keep the ZIP OUT of the repo folder;
   inside skills/ it would be added to the manifest.
5. Open a fresh chat in this Project and say: check the install probe.
6. After that check, delete install-probe from Settings.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 

1. **patch_L001_1** (mine, the Earth System track). Adds road stage 14 at an anchor the step-2 page still has; tested in that order.

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/patch_L001_1_earth_system_track_20261007.py
ok  LEDGER_CONSOLIDATED.md             header stamp
ok  LEDGER_CONSOLIDATED.md             L-001 date
ok  LEDGER_CONSOLIDATED.md             L-001 ruling
ok  LEDGER_CONSOLIDATED.md             L-060 date
ok  LEDGER_CONSOLIDATED.md             L-060 pointer
ok  LEDGER_CONSOLIDATED.md             L-070 date
ok  LEDGER_CONSOLIDATED.md             L-070 pointer
ok  LEDGER_CONSOLIDATED.md             L-071 closed
ok  LEDGER_CONSOLIDATED.md             L-071 close record
ok  LEDGER_CONSOLIDATED.md             L-077 closed
ok  LEDGER_CONSOLIDATED.md             L-077 close record
ok  documentation/WHERE_WE_ARE.md      road: stage 14, the Earth System layers

patch applied

NEXT:
  1. Move this script into documentation/.
  2. Run orrery_maintenance_run.py (its Ledger index step moves L-071
     and L-077 into the closed section; that is expected).

======================================================================
MAINTENANCE RUN -- generators, then checkers (L-188)
======================================================================
  Provenance scan is current (last run 20261008T005417Z, 0 day(s) ago).

GENERATORS -- regenerate every time; a no-op when nothing moved
----------------------------------------------------------------------
  Ledger index                 1.3s  rewrote LEDGER_CONSOLIDATED.md
  Skill manifest               0.1s  unchanged (1 of 1 rewritten, content
                                     identical)
  Constants export             0.7s  unchanged (1 checked, not written)
  Objects export               0.1s  unchanged (1 checked, not written)
  Module atlas                 6.4s  rewrote MODULE_ATLAS.md, MODULE_INDEX.md
  Data inventory               4.0s  unchanged (1 of 1 rewritten, content
                                     identical)
  Exact rows report            1.6s  unchanged (1 checked, not written) -- 13 of
                                     34 exact rows printed at 42 lines (32
                                     orrery, 10 gallery); 8 drawn only, 11 not
                                     followed, 0 map entries broken
  Document index               0.1s  unchanged (1 checked, not written)

CHECKERS -- verdict informs the push call
----------------------------------------------------------------------
  Constants change             0.2s  No changes to constants_new.py since HEAD.
  Constants relations          0.2s  25 of 25 provenance tests passed against
                                     constants_new.py. No constants have drifted.
  Derived figures              0.7s  No figure count exceeds its inputs: 36
                                     derived row(s) read, 26 judged OK -- 26 OK,
                                     10 NOT YET MIGRATED, 1 NO DERIVED LINE, 1
                                     UNMARKED CONVERSION; 18 conversion(s)
                                     checked.
  Constants export check       1.1s  Export matches the store: sha256
                                     3b7000e368d1 on both sides; 105 rows
                                     re-read, 56 not exported, 27 tokens; 310
                                     conversions re-computed, 10 of 10 worked
                                     cases hold.
  Objects export check         0.1s  pass
  Skill headers                0.1s  11 skills parsed, no consistency problems.
  Exact rows by the count      1.5s  PASSING -- 13 printed exact rows each state
                                     a count; 32 orrery lines print through
                                     exact_text() or row_text(); 10 gallery lines
                                     are served the count
  Dimensions                   1.0s  No unit contradicts its arithmetic: 54
                                     derived row(s) read -- 42 OK, 9 NO UNIT, 3
                                     NOT CHECKABLE.
  Cross-check annotations      0.1s  19 of 19 cross-check annotation tests
                                     passed.
  Citation inheritance         0.1s  20 of 20 citation-inheritance tests passed.
  Status lines                 0.1s  All 105 status lines in constants_new.py are
                                     well formed; 53 rows carry none.
  Row shape                    0.1s  All 161 row shapes in constants_new.py fit
                                     the assignment's own line.
  Scanner recognition 1d/1e    0.2s  27 of 27 recognition pins hold: real
                                     citations recognized, fake ones refused.
  Reset completeness          12.3s  PASS -- all 310 IntVars + 3 StringVars + 10
                                     entries reset to startup defaults; date set
                                     to now.
  Orbit cache                  1.5s  All 6 orbit cache tests passed: cache loads,
                                     old formats convert, corrupted entries are
                                     dropped.
  Earth pole of date           0.3s  all 14 checks passed (geometry, ERFA,
                                     fallback, cache, hover, transform).
  Worksheet checker            8.6s  74 of 110 routed, 8 clean
  Worksheet checker tests     15.8s  All 135 checks passed
  Worksheet key round trip     0.9s  RESULT: 52 sites minted 52 distinct keys,
                                     all resolved; 52 pinned keys still resolve;
                                     1 retired keys confirmed gone.
  Builder marker join         18.4s  All 76 checks passed
  Extractor pins               0.4s  RESULT: 29 string sites carry the pinned 73
                                     claims and 14 instruction drops, at LOOKBACK
                                     30 / LOOKAHEAD 25, extractor version 2.
  Provenance scanner           8.9s  296 TIER-1 FINDINGS IN THE SCANNED TREE

======================================================================
  20 of 20 gating checkers passed -- 87.1s total
  2 report-only, exit 0 whatever they find:
    Worksheet checker           74 of 110 routed, 8 clean
    Provenance scanner          296 TIER-1 FINDINGS IN THE SCANNED TREE
======================================================================

FILES WRITTEN THIS RUN
----------------------------------------------------------------------
  2106 file(s) examined, 7 written, 0 created, 0 removed, 5 rewritten identically
    written   LEDGER_CONSOLIDATED.md
    written   MODULE_ATLAS.md
    written   MODULE_INDEX.md
    written   PROVENANCE_AUDIT.md
    written   WORKSHEET_CHECK.md
    written   data/provenance_history.json
    written   documentation/prompts/citation_review.jsonl
    rewritten with identical bytes, no action needed:
      DATA_INVENTORY.md
      PROJECT_INSTRUCTIONS.md
      data/worksheet_check_state.json
      data/worksheet_routed.json
      test_output/test_orbit_paths.json
    20 file(s) over 2 MB compared by size and mtime only

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>

  3. Commit and push. -- 
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 

2. **patch_L412_1** (mine, the RICE ruling). Records only.
3. **patch_L216_1** (mine, the hand run). Records only.
4. **patch_L422_1** (mine, the skill at 1.17 and the page). It checks that 1 through 5 have run and refuses otherwise.
5. **orrery_maintenance_run.py**, once. The manifest table goes to 1.17; the index step moves L-071 and L-077 to the closed section.
6. **Commit and push.** Then the two account steps: reinstall ledger-and-session-records, replace the Project's instructions with v3.85.
7. **Paste the note into the four sessions.** Only now, because it tells them to read the skill and the page from HEAD.
8.  **Anything the fourth session closes with** is built after step 9, by section, against the new page.

Steps 1 to 5 can be in any order among themselves; I tested the pairs. The two that must hold are 2 before 3, so the road edit lands on the rewritten page, and 6 last.
