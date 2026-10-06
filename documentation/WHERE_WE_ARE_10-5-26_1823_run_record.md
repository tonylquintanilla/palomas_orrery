<!-- Doc-Kind: hand | Where the project is and where it is going, in plain words. One file, rewritten in place; read it at the end of every session. -->
# Where We Are

Last updated: October 5, 2026, end of the session held mostly from
your phone. -- **Tony**: notes 10-5 and 10-6-2026 -- 
- Written at orrery d9f47a87 and gallery ed48d078, after your runs.

> **READ THIS FIRST**
>
> **Changed this session:**
> - Earth's orrery patch is in: the geocorona has its own shell,
>   Earth's tilt is said in words where "23.4" was typed, and the inner
>   belt's words say "near the measured proton flux peak", as you ruled.
> - The atmosphere and low Earth orbit heights stay measured from the
>   equatorial radius, as you clarified. Notes on those rows now say why.
> - Every step of both maintenance runs gets a dashboard button: eleven
>   new ones.
> - The skill check now enforces Anthropic's written limits on a
>   skill's name and description.
> - Six long skills now open with a list of their contents, kept true by
>   that check, and their old history moved to its own file.
>   provenance-discipline's rules now come before its long procedures.
> - The check of the object list against JPL Horizons has its own
>   handoff, for a fresh session.
> - Your notes in this page, the handoffs and the ledger are protected
>   by a written rule now: a patch checks only the lines it edits.
>
> **Do next:**
> - *The website patch for Earth, or the Horizons design round, in the
>   order you choose.*
>
> **Needs you now:**
> - *Look at the "Ecliptic Coordinates (J2000)" box at the plot's left:
>   its teal-circle line. The rest of your look was correct.*
> - *Run the skill patch, reinstall ledger-and-session-records, and
>   replace the Project's instructions with v3.82.*

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
              confirmed.* << this session: the orrery patch is built;
              the website patch and the design talks remain.
  6. [next]   The Sun's numbers get the same checking Earth's got: the
              Sun's list, from its opening view.
  7. [next]   The served objects are checked against JPL Horizons, the
              way the numbers are checked against their sources.
              << new this session: moved up from "not urgent", because
              it verifies what the website already serves.
  8. [next]   The website's checks get a short list of their own, so a
              new room or a moved front door can't break unnoticed.
  9. [next]   A bare interactive.html link opens the Solar System room,
              and the Explorer gets its own address. The lobby's wide
              Solar System card, its first half, is done.
 10. [later]  The rest of the orrery's objects come to the website --
              dwarf planets, asteroids, moons -- through the same
              connection that now carries the room's eleven bodies,
              checked against JPL Horizons.
 11. [later]  Encounters: comets and spacecraft shown at the dates
              that matter.
 12. [later]  The planets get their details -- layers, rings, magnetic
              fields -- Jupiter and Saturn first.
 13. [goal]   The website does what the desktop orrery does, from data
              fetched from JPL each night, with a date to choose and
              time to play within the range the data covers.

## Right now  **>> UPDATED THIS SESSION**

- Earth's orrery patch is in, and your look found it correct.
  - A new checkbox, "-- Exosphere (Geocorona)", draws a faint shell at
    100 Earth radii, in the website's colour, with the words you
    approved.
  - The two coordinate hovers, the Celestial Sphere tooltip and the
    coordinate guide say "Earth's axial tilt" instead of typing 23.4.
    Earth's rotation-axis hover already gives the angle for the date.
  - The Upper Atmosphere tooltip said the layer reaches 1,000 km; it
    now shows the hover's words, which say 600 km, the height drawn.
- The website still says the inner belt sits "where the measured
  particle flux peaks", and it says the same of Jupiter's belts, whose
  distances have no source. The website patch fixes both.
- The skills: each long one opens with its contents, and the check
  fails if a list stops matching its headings. Five skills are still
  longer than Anthropic's 500-line guideline; splitting
  provenance-discipline's two long procedures into separate files is
  recorded, not scheduled.
- This chat cannot reach JPL. The Horizons check will run on your
  machine, unless you allow JPL in this chat's network settings.
- My closing patch refused to rewrite this page because of your
  "-- done" marks. That broke your rule that you can annotate the
  documents; the new closing patch keeps your notes instead.
- The ledger holds 242 open items: L-418 and L-419 opened; L-389, L-416
  and L-417 closed.

## The next three steps  **>> UPDATED THIS SESSION**

1. *Your look at the coordinate box's teal-circle line.*
2. Earth's website patch, then your look on the phone.
   - The inner belt's words, and no "measured" claim for Jupiter's.
   - The geocorona note corrected.
   - The saved Earth test scene re-recorded from today's data.
   - The collapsed-features check added to the website's maintenance
     run, with its own button.
3. The Horizons check: a design round first, in a fresh session, from
   `documentation/HANDOFF_L395_horizons_check_design_20261005.md`.

## Waiting on you  **>> UPDATED THIS SESSION**

Now:
- The coordinate box's teal-circle line, in the orrery.
- Run patch_L419_1, reinstall ledger-and-session-records, and replace
  the Project's instructions with PROJECT_INSTRUCTIONS.md, now v3.82.

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
  - This session: L-413 (Earth's list, the orrery patch), L-418 (the
    skills' contents and histories), L-419 (your notes in documents),
    L-395 (the Horizons check moved up). Closed: L-389, L-416 (dashboard
    buttons), L-417 (the skill limits).
- Your run record for this session:
  `documentation/WHERE_WE_ARE_10-5-26_1627_run_record.md`
  - The Sun's list: L-412.
- The skills' old version history: `documentation/SKILL_HISTORIES.md`
- The reasoning behind the order:
  `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md`
- The latest session records:
  `documentation/HANDOFF_L413_earth_orrery_patch_20261005.md`, and for
  the next round, `documentation/HANDOFF_L395_horizons_check_design_20261005.md`

====================================================================================

I've put the rules into the handoffs, so each new session reads them on its own and you don't have to carry them between sessions.

**What the patch adds**
- **The website session's handoff:** a section "Running beside the Horizons session" with the three rules.
  - It owns Where We Are this round.
  - It does the opening checks. Those include closing L-369, with your "beautiful" on the coordinate box as the evidence.
  - It pulls the repo again before its final patch.
- **The Horizons session's handoff:** the matching section.
  - It leaves Where We Are alone and puts its updates in its own handoff.
  - It edits only L-395 in the ledger, plus any item it opens.
  - It pulls the repo again before any patch.
- **One correction:** the website handoff expected the ledger skill at 1.15. It now says 1.16, since the later patch bumped it.

**How it's guarded**
- It matches each handoff only at the lines it changes, as today's rule says, so your notes elsewhere won't stop it.
- On a copy of your push it ran cleanly, a second run refused, and the scanner stayed at 296.

**Your steps**
1. Run `patch_L413_5` in the orrery root.

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/patch_L413_5_parallel_sessions_20261005.py
ok  documentation/HANDOFF_L395_horizons_check_design_20261005.md the parallel run
ok  documentation/HANDOFF_L413_earth_orrery_patch_20261005.md    next session: the versions and the parallel run

patch applied

NEXT:
  1. Move this script into documentation/.
  2. Commit and push. No maintenance run is needed: only two
     handoffs changed.
  3. Start the two sessions, each from its handoff.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 

2. Move it into `documentation/`, then commit and push. No maintenance run is needed. -- 0493fad007456fe68a7690a2400af2c2d185a410
3. Start each session with one line, for example: "Start from `documentation/HANDOFF_L413_earth_orrery_patch_20261005.md`" and "Start from `documentation/HANDOFF_L395_horizons_check_design_20261005.md`."

Where this leaves us:
- After this push, Earth's website patch and the Horizons design round can start side by side, each from its own handoff.

=============================================================================================================================

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/patch_L420_1_galactic_plane_item_20261005.py
ok  LEDGER_CONSOLIDATED.md                                       header stamp
ok  LEDGER_CONSOLIDATED.md                                       L-420 opened
ok  documentation/HANDOFF_L413_earth_orrery_patch_20261005.md    L-420 for Where We Are

patch applied

NEXT:
  1. Move this script into documentation/. -- done
  2. Run orrery_maintenance_run.py: its Ledger index step adds
     L-420 to the index.

OK: 415 L-blocks parsed, no consistency problems.
Index regenerated (243 live items) in C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\LEDGER_CONSOLIDATED.md.

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>

  3. Commit and push. Run it before the website session's patch if
     you can; either order works. -- 51436054330aefd6be2a7efd93ebd58f06c4a2d2
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 

=====================================================================================

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/patch_L420_2_galactic_plane_and_centre_20261006.py
ok  constants_new.py         docstring stamp (L-420)
ok  constants_new.py         Sgr A* position rows
ok  palomas_orrery.py        docstring stamp (L-420)
ok  palomas_orrery.py        static plot box: violet circle line
ok  palomas_orrery.py        animation box: violet circle line
ok  palomas_orrery.py        Celestial Sphere tooltip
ok  palomas_orrery.py        Star Background tooltip
ok  palomas_orrery.py        Celestial Grid tooltip
ok  palomas_orrery.py        Labels tooltip
ok  star_sphere_builder.py   docstring stamp (L-420)
ok  star_sphere_builder.py   import the galactic rows
ok  star_sphere_builder.py   build_galactic_grid()
ok  star_sphere_builder.py   Sgr A* marker in the Star Background
ok  star_sphere_builder.py   galactic plane circle
ok  star_sphere_builder.py   NGP and SGP markers
ok  star_sphere_builder.py   celestial pole hover shows the full name (in passing)
ok  star_sphere_builder.py   ecliptic pole hover shows the full name (in passing)

stamps updated: the docstrings of constants_new.py, star_sphere_builder.py and palomas_orrery.py
patch applied (17 edits in 3 files)

NEXT:
  1. Run patch_L420_3_session_close_20261006.py the same way.
  2. Run orrery_maintenance_run.py. Constants export rewrites
     data/constants_export.json: 105 rows exported, up from 101.

======================================================================
MAINTENANCE RUN -- generators, then checkers (L-188)
======================================================================
  Provenance scan is current (last run 20261005T230218Z, 1 day(s) ago).

GENERATORS -- regenerate every time; a no-op when nothing moved
----------------------------------------------------------------------
  Ledger index                 2.1s  rewrote LEDGER_CONSOLIDATED.md
  Skill manifest               0.4s  rewrote PROJECT_INSTRUCTIONS.md
  Constants export             2.2s  rewrote data/constants_export.json
  Objects export               0.1s  unchanged (1 checked, not written)
  Module atlas                10.0s  rewrote MODULE_ATLAS.md, MODULE_INDEX.md
  Data inventory               5.7s  rewrote DATA_INVENTORY.md
  Exact rows report            1.9s  rewrote EXACT_ROWS_PRINTED.md -- 13 of 34
                                     exact rows printed at 42 lines (32 orrery,
                                     10 gallery); 8 drawn only, 11 not followed,
                                     0 map entries broken
  Document index               0.1s  unchanged (1 checked, not written)

CHECKERS -- verdict informs the push call
----------------------------------------------------------------------
  Constants change             0.4s  2 derived line(s): 0 changed, 2 added, 0
                                     removed
  Constants relations          0.3s  25 of 25 provenance tests passed against
                                     constants_new.py. No constants have drifted.
  Derived figures              0.9s  No figure count exceeds its inputs: 36
                                     derived row(s) read, 26 judged OK -- 26 OK,
                                     10 NOT YET MIGRATED, 1 NO DERIVED LINE, 1
                                     UNMARKED CONVERSION; 18 conversion(s)
                                     checked.
  Constants export check       1.3s  Export matches the store: sha256
                                     3b7000e368d1 on both sides; 105 rows
                                     re-read, 56 not exported, 27 tokens; 310
                                     conversions re-computed, 10 of 10 worked
                                     cases hold.
  Objects export check         0.1s  pass
  Skill headers                0.2s  11 skills parsed, no consistency problems.
  Exact rows by the count      1.6s  PASSING -- 13 printed exact rows each state
                                     a count; 32 orrery lines print through
                                     exact_text() or row_text(); 10 gallery lines
                                     are served the count
  Dimensions                   1.7s  No unit contradicts its arithmetic: 54
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
  Reset completeness          26.6s  PASS -- all 310 IntVars + 3 StringVars + 10
                                     entries reset to startup defaults; date set
                                     to now.
  Orbit cache                  2.1s  All 6 orbit cache tests passed: cache loads,
                                     old formats convert, corrupted entries are
                                     dropped.
  Earth pole of date           0.3s  all 14 checks passed (geometry, ERFA,
                                     fallback, cache, hover, transform).
  Worksheet checker            9.6s  74 of 110 routed, 8 clean
  Worksheet checker tests     17.3s  All 135 checks passed
  Worksheet key round trip     1.1s  RESULT: 52 sites minted 52 distinct keys,
                                     all resolved; 52 pinned keys still resolve;
                                     1 retired keys confirmed gone.
  Builder marker join         26.9s  All 76 checks passed
  Extractor pins               0.5s  RESULT: 29 string sites carry the pinned 73
                                     claims and 14 instruction drops, at LOOKBACK
                                     30 / LOOKAHEAD 25, extractor version 2.
  Provenance scanner          11.6s  298 TIER-1 FINDINGS IN THE SCANNED TREE

======================================================================
  20 of 20 gating checkers passed -- 125.8s total
  2 report-only, exit 0 whatever they find:
    Worksheet checker           74 of 110 routed, 8 clean
    Provenance scanner          298 TIER-1 FINDINGS IN THE SCANNED TREE
======================================================================

FILES WRITTEN THIS RUN
----------------------------------------------------------------------
  2079 file(s) examined, 11 written, 0 created, 0 removed, 3 rewritten identically
    written   DATA_INVENTORY.md
    written   EXACT_ROWS_PRINTED.md
    written   LEDGER_CONSOLIDATED.md
    written   MODULE_ATLAS.md
    written   MODULE_INDEX.md
    written   PROJECT_INSTRUCTIONS.md
    written   PROVENANCE_AUDIT.md
    written   WORKSHEET_CHECK.md
    written   data/constants_export.json
    written   data/provenance_history.json
    written   documentation/prompts/citation_review.jsonl
    rewritten with identical bytes, no action needed:
      data/worksheet_check_state.json
      data/worksheet_routed.json
      test_output/test_orbit_paths.json
    20 file(s) over 2 MB compared by size and mtime only

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>

  3. Move both patch scripts into documentation/, commit and push. -- e7073fce5cc214836d2175d3f7643ff0855c7064
  4. Your look: plot with Star Background, Celestial Grid and Labels on. -- looks great. some issues:
  a) galactic tide is very faint and the X is not discernible
  b) can we move the coordinate circle descriptions to hovertext markers on the circles
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 

=================================================================================

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/patch_L420_3_session_close_20261006.py
ok  LEDGER_CONSOLIDATED.md                                     header stamp
ok  LEDGER_CONSOLIDATED.md                                     L-420 date
ok  LEDGER_CONSOLIDATED.md                                     L-420 built, Gap and Ref
ok  documentation/HANDOFF_L413_earth_orrery_patch_20261005.md  L-420 built: where its page lines are
ok  documentation/HANDOFF_L420_galactic_plane_20261006.md      created

stamps updated: the ledger's header stamp; the new handoff opens with its anchor
patch applied

NEXT:
  1. Run orrery_maintenance_run.py. Its Ledger index step updates
     L-420's row; its Constants export step writes the four new rows.
  2. Move both L420 patch scripts into documentation/, commit and push.
  3. Your look: plot with Star Background, Celestial Grid and Labels on.
     The violet colour, the marker sizes, where the labels sit. -- looks good
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 

===================================================================================

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/patch_L027_1_panel_colour_20261006.py
ok  LEDGER_CONSOLIDATED.md                           header stamp
ok  LEDGER_CONSOLIDATED.md                           L-027 date
ok  LEDGER_CONSOLIDATED.md                           L-027 corrected and built
ok  PROJECT_INSTRUCTIONS.md                          header stamp
ok  PROJECT_INSTRUCTIONS.md                          SHA anchor
ok  PROJECT_INSTRUCTIONS.md                          v3.83 entry
ok  PROJECT_INSTRUCTIONS.md                          v3.80 moves down
ok  documentation/HANDOFF_L420_galactic_plane_20261006.md L-027 section
ok  documentation/HANDOFF_L420_galactic_plane_20261006.md L-027 Where We Are lines
ok  documentation/HANDOFF_L420_galactic_plane_20261006.md L-027 Tony-actions
ok  documentation/HANDOFF_L420_galactic_plane_20261006.md L-027 next session
ok  documentation/PROJECT_INSTRUCTIONS_HISTORY.md    receives v3.80
ok  palomas_orrery.py                                docstring stamp
ok  palomas_orrery.py                                PANEL_BG defined after the root window
ok  palomas_orrery.py                                the 23 SystemButtonFace sites use PANEL_BG
ok  skills/agentic-pre-test/SKILL.md                 description: the throwaway rule, unnamed
ok  skills/agentic-pre-test/SKILL.md                 v1.3 entry
ok  skills/agentic-pre-test/SKILL.md                 Standard Test without the swap
ok  skills/agentic-pre-test/SKILL.md                 the throwaway section, with its true founding case

patch applied

NEXT:
  1. Run orrery_maintenance_run.py. Every checker should pass,
     Reset completeness included; Skill manifest rewrites the
     agentic-pre-test row in PROJECT_INSTRUCTIONS.md to 1.3.
  2. Open the orrery and look at the panels: a shade darker grey.
  3. Move this script into documentation/, commit and push. -- e7073fce5cc214836d2175d3f7643ff0855c7064
  4. Reinstall agentic-pre-test in Settings > Skills, and replace
     the Project's instructions with PROJECT_INSTRUCTIONS.md (v3.83). -- done
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 

=================================================================================

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/patch_L413_6_earth_website_20261006.py
ok  documentation/payload_earth_scene.json           re-recorded whole
ok  data/objects_config.json                         L-349: what each belt's measured peak is a peak of
ok  data/objects_config.json                         geocorona note: the orrery has its shell now (L-292)
ok  documentation/smoke_display_figures.js           header: why the fixture moved
ok  documentation/smoke_display_figures.js           fixture: the L-349 recording
ok  documentation/smoke_display_figures.js           acceptance: Earth's inner belt in Tony's words
ok  documentation/smoke_display_figures.js           acceptance: the old wording must not come back
ok  documentation/smoke_display_figures.js           acceptance: the belts' tilt sentence, approved 2026-10-06
ok  documentation/smoke_display_figures.js           acceptance: the outer belt's old tilt wording must not come back
ok  documentation/smoke_display_figures.js           acceptance: the inner belt's old tilt wording must not come back
ok  documentation/smoke_earth_geometry.js            header: where the recording comes from
ok  documentation/smoke_earth_geometry.js            header: credit line
ok  documentation/smoke_earth_geometry.js            the pole of date is the recording's
ok  documentation/smoke_earth_geometry.js            the magnetotail and period are the recording's
ok  documentation/smoke_earth_geometry.js            the scene's date is the recording's
ok  documentation/smoke_earth_geometry.js            the Moon's arc dates: any day, with the hour
ok  documentation/smoke_earth_geometry.js            the belts' tilt: the served number, as printed
ok  documentation/smoke_earth_geometry.js            the stale note about the old recording
ok  documentation/smoke_hover_budget.js              the Earth room is measured from the recording as recorded
ok  gallery/earth_geometry.js                        credit line
ok  gallery/earth_geometry.js                        the tilt sentence in three lines
ok  gallery/earth_geometry.js                        no empty line before the curved arrows
ok  gallery/earth_geometry.js                        the period ends without a break: the tail brings its own
ok  gallery/feature_renderers.js                     credit line
ok  gallery/feature_renderers.js                     read the belts' flux_peak_of list
ok  gallery/feature_renderers.js                     the single-distance line claims a measurement only with a source
ok  gallery/feature_renderers.js                     unbandedLead, defined beside the band's words
ok  gallery/feature_renderers.js                     the belts' tilt sentence, approved 2026-10-06
ok  gallery_maintenance_run.py                       credit line
ok  gallery_maintenance_run.py                       L-300: the sweep joins the checkers, after Cache in step
ok  tools/store_writer.py                            docstring: the new list
ok  tools/store_writer.py                            credit line
ok  tools/store_writer.py                            BELT_WORD_LISTS gains flux_peak_of
ok  documentation/fixture_hovers_L349_on_ed48d078.json new file
ok  tools/record_earth_scene.py                      new file

patch applied

NEXT:
  1. Run the cache builder: the dashboard button 'Gallery Cache Builder
     -- Manual Run', or tools/gallery_cache_builder.py from this folder.
     Read its [SWAP] line.

[RECOVER] removed retained data\solar-system.prev (cleared read-only on 5 entries)
[sweep] no sibling directories present
[POLE] earth: pole of 2026-10-06 served (RA 0.70064, Dec 89.85005 deg); tilt 23.43808 deg
[SWAP] staging_to_live refused on attempt 1 of 6 ([WinError 5] Access is denied: 'data\\.staging_solar-system_20261006T182032Z' -> 'data\\solar-system'); waiting 2s
[SWAP] staging_to_live succeeded on attempt 2 of 6
[SWAP] the new cache is in place after a refused rename: staging_to_live took 2 tries. The builder absorbed it. Recorded in data/cache_swap_log.jsonl
[warn] sun: features-only entry; no Horizons fetch
[done] run 20261006T182032Z (nightly): 19 objects

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
  PASS Module atlas              0.9s  no change to MODULE_ATLAS.md,
                                    MODULE_INDEX.md
  PASS Constants export pull     1.0s  no change to
                                    data/constants_export.json,
                                    data/constants_export.sha
  PASS Config mirror             0.1s  no change to
                                    data/objects_config.json
  PASS Objects export pull       0.6s  no change to
                                    data/objects_export.json,
                                    data/objects_export.sha
  PASS Objects mirror            0.1s  no change to
                                    data/objects_config.json

CHECKERS -- the verdict informs the push call
  PASS Cache builder suite      12.3s  PASS (229 checks, 0 failures)
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
  PASS Store writer suite        5.7s  All 289 store-writer checks
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
  PASS Store editor suite        0.1s  All 272 store-editor checks
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
                                    link(s) against orrery e7073fce, 4
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
  PASS Feature renderers         0.1s  === ALL CHECKS PASSED ===
  PASS Page framing              0.1s  === ALL CHECKS PASSED ===
  PASS Sun shells                0.1s  ALL CHECKS PASSED
  PASS Earth scene geometry      0.1s  === ALL CHECKS PASSED ===
  PASS Hover budget              0.1s  === ALL CHECKS PASSED ===
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
  last swap 2026-10-06T18:20:35.041866+00:00: succeeded after a refused rename -- staging_to_live took 2 attempts -- a refusal this build absorbed
======================================================================

  After you push: python gallery_maintenance_run.py --live

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  2. In GitHub Desktop, look at the change list. A good build
     shows changed and added files and NO pile of deletions.
  3. Commit and push. -- 38f1e7b058ac359d5b7806fc3d2fe7da77d48e64
  4. After the push, check what the live site serves:
         python gallery_maintenance_run.py --live

TONY-ACTION ROLLUP for this run:
  (do)     steps 1 to 4 above, in that order.
----------------------------------------------------------------------

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  2. Run gallery_maintenance_run.py. Expect 24 of 24 -- one more than
     before: Collapsed features. A red Cache in step means step 1 has
     not run.
  3. Move this script into documentation/. Commit the config and the
     cache together, and push. -- 38f1e7b058ac359d5b7806fc3d2fe7da77d48e64
  4. On your phone, open Earth's room and read three hovers: the inner
     belt (the trapped protons), the outer belt, and the rotation axis. -- correct
     Then Jupiter's inner belt: it should make no 'measured' claim. -- Jupiter inner belt not in the room yet. correct in the orrery.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> 

==================================================================================

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/patch_L413_7_session_close_20261006.py
ok  LEDGER_CONSOLIDATED.md                                     header stamp
ok  LEDGER_CONSOLIDATED.md                                     L-421 opened
ok  LEDGER_CONSOLIDATED.md                                     L-419 closed
ok  LEDGER_CONSOLIDATED.md                                     L-419 confirmed
ok  LEDGER_CONSOLIDATED.md                                     L-415 closed
ok  LEDGER_CONSOLIDATED.md                                     L-415 confirmed
ok  LEDGER_CONSOLIDATED.md                                     L-418 versions confirmed
ok  LEDGER_CONSOLIDATED.md                                     L-418 date
ok  LEDGER_CONSOLIDATED.md                                     L-369 closed
ok  LEDGER_CONSOLIDATED.md                                     L-369 Tony's look
ok  LEDGER_CONSOLIDATED.md                                     L-420 Tony's look
ok  LEDGER_CONSOLIDATED.md                                     L-349 website built
ok  LEDGER_CONSOLIDATED.md                                     L-349 date
ok  LEDGER_CONSOLIDATED.md                                     L-379 built
ok  LEDGER_CONSOLIDATED.md                                     L-379 date
ok  LEDGER_CONSOLIDATED.md                                     L-300 built
ok  LEDGER_CONSOLIDATED.md                                     L-300 date
ok  LEDGER_CONSOLIDATED.md                                     L-292 the website's note
ok  LEDGER_CONSOLIDATED.md                                     L-413 progress
ok  LEDGER_CONSOLIDATED.md                                     L-413 date
ok  PROJECT_INSTRUCTIONS.md                                    header stamp
ok  PROJECT_INSTRUCTIONS.md                                    anchor
ok  PROJECT_INSTRUCTIONS.md                                    v3.84, and v3.81 moved down
ok  PROJECT_INSTRUCTIONS.md                                    v3.81 leaves
ok  documentation/PROJECT_INSTRUCTIONS_HISTORY.md              v3.81 arrives
ok  documentation/SKILL_HISTORIES.md                           interactive-exhibit 1.9 moved here
ok  palomas_orrery_dashboard.py                                change log
ok  palomas_orrery_dashboard.py                                offline runner names the sweep
ok  palomas_orrery_dashboard.py                                Collapsed Features button
ok  skills/interactive-exhibit/SKILL.md                        version 1.12, and 1.9 moved down
ok  skills/interactive-exhibit/SKILL.md                        the rule
ok  documentation/WHERE_WE_ARE.md                              rewritten whole
ok  documentation/HANDOFF_L413_earth_website_20261006.md       created
ok  documentation/MANIFEST_L421_typed_facts_20261006.md        created

carried 0 line(s) of yours from Where We Are into the handoff

patch applied

NEXT:
  1. Move this script into documentation/. -- done
  2. Run orrery_maintenance_run.py. Its Ledger index step adds L-421
     and moves the five closed items; its Skill manifest step writes
     interactive-exhibit 1.12 into PROJECT_INSTRUCTIONS.md.

======================================================================
MAINTENANCE RUN -- generators, then checkers (L-188)
======================================================================
  Provenance scan is current (last run 20261006T163329Z, 0 day(s) ago).

GENERATORS -- regenerate every time; a no-op when nothing moved
----------------------------------------------------------------------
  Ledger index                 1.2s  rewrote LEDGER_CONSOLIDATED.md
  Skill manifest               0.1s  rewrote PROJECT_INSTRUCTIONS.md
  Constants export             0.6s  unchanged (1 checked, not written)
  Objects export               0.1s  unchanged (1 checked, not written)
  Module atlas                 5.6s  rewrote MODULE_ATLAS.md, MODULE_INDEX.md
  Data inventory               4.0s  rewrote DATA_INVENTORY.md
  Exact rows report            1.4s  rewrote EXACT_ROWS_PRINTED.md -- 13 of 34
                                     exact rows printed at 41 lines (32 orrery, 9
                                     gallery); 8 drawn only, 11 not followed, 0
                                     map entries broken
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
  Constants export check       1.2s  Export matches the store: sha256
                                     3b7000e368d1 on both sides; 105 rows
                                     re-read, 56 not exported, 27 tokens; 310
                                     conversions re-computed, 10 of 10 worked
                                     cases hold.
  Objects export check         0.1s  pass
  Skill headers                0.1s  11 skills parsed, no consistency problems.
  Exact rows by the count      1.3s  PASSING -- 13 printed exact rows each state
                                     a count; 32 orrery lines print through
                                     exact_text() or row_text(); 9 gallery lines
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
  Reset completeness          12.2s  PASS -- all 310 IntVars + 3 StringVars + 10
                                     entries reset to startup defaults; date set
                                     to now.
  Orbit cache                  1.6s  All 6 orbit cache tests passed: cache loads,
                                     old formats convert, corrupted entries are
                                     dropped.
  Earth pole of date           0.3s  all 14 checks passed (geometry, ERFA,
                                     fallback, cache, hover, transform).
  Worksheet checker            7.5s  74 of 110 routed, 8 clean
  Worksheet checker tests     13.4s  All 135 checks passed
  Worksheet key round trip     0.8s  RESULT: 52 sites minted 52 distinct keys,
                                     all resolved; 52 pinned keys still resolve;
                                     1 retired keys confirmed gone.
  Builder marker join         17.7s  All 76 checks passed
  Extractor pins               0.4s  RESULT: 29 string sites carry the pinned 73
                                     claims and 14 instruction drops, at LOOKBACK
                                     30 / LOOKAHEAD 25, extractor version 2.
  Provenance scanner           8.5s  296 TIER-1 FINDINGS IN THE SCANNED TREE

======================================================================
  20 of 20 gating checkers passed -- 80.9s total
  2 report-only, exit 0 whatever they find:
    Worksheet checker           74 of 110 routed, 8 clean
    Provenance scanner          296 TIER-1 FINDINGS IN THE SCANNED TREE
======================================================================

FILES WRITTEN THIS RUN
----------------------------------------------------------------------
  2084 file(s) examined, 10 written, 0 created, 0 removed, 3 rewritten identically
    written   DATA_INVENTORY.md
    written   EXACT_ROWS_PRINTED.md
    written   LEDGER_CONSOLIDATED.md
    written   MODULE_ATLAS.md
    written   MODULE_INDEX.md
    written   PROJECT_INSTRUCTIONS.md
    written   PROVENANCE_AUDIT.md
    written   WORKSHEET_CHECK.md
    written   data/provenance_history.json
    written   documentation/prompts/citation_review.jsonl
    rewritten with identical bytes, no action needed:
      data/worksheet_check_state.json
      data/worksheet_routed.json
      test_output/test_orbit_paths.json
    20 file(s) over 2 MB compared by size and mtime only

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>

  3. Commit and push. -- d5c6179381a5dd6b8ab54dc2dcc10fc9914016e0
  4. Reinstall interactive-exhibit in Settings > Skills (1.12), and
     replace the Project's instructions with PROJECT_INSTRUCTIONS.md,
     now v3.84. -- done
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 
