<!-- Doc-Kind: hand | Session record: the Fable 5.1 ledger sweep of October 4 to 7, 2026 -- the sweep's two reports, Tony's five rulings and their patches, the swap-log evidence, Where We Are redesigned, ledger-and-session-records 1.17, protocol v3.85. -->
# Handoff: the Fable ledger sweep, October 4 to 7, 2026

Built on orrery 8653ef1b593aaf3835ecbcf2186b9e3e28a28089 at
https://github.com/tonylquintanilla/palomas_orrery; the gallery read at
4cfeca27 at https://github.com/tonylquintanilla/tonyquintanilla.github.io
and not changed. Orrery pushed at: Tony's run record carries it. This
record is carried by `patch_L422_1_skill_1_17_and_tonys_page_20261007.py`.
Type: DOCUMENTATION (one skill version, one protocol entry, one page;
no code). Written October 7, 2026, with Anthropic's Claude Fable 5.1.

## What this session was

A review session beside the Opus sessions working Earth's list. Tony
asked for a sweep of LEDGER_CONSOLIDATED.md (closes, RICE, grouping,
errors) on October 4, an update of it on October 7, and then ruled on
five of the things it raised. The session wrote no code.

## Opening checks [verified @ orrery 8653ef1b]

- The installed copies of ledger-and-session-records (1.14) and
  safe-file-editing (1.11) in this conversation were bound before the
  pushes that took them to 1.16 and 1.13; the session read both skills
  from the repo at HEAD and said so. The October 6 and 7 sessions had
  already verified the account installs current, so no action fell to
  Tony from the mismatch.
- The ledger indexer's --check was clean at both anchors (cbde99dc on
  October 4; 8653ef1b on October 7).

## Done, verified

- `documentation/LEDGER_SWEEP_review_20261004.md` (in the repo; cited
  by L-413) and `documentation/LEDGER_SWEEP_review_20261007.md`: the
  sweep and its update. Nearly every proposal of the first landed by
  the second (17 closes, L-413 and L-421 opened, the header stamps,
  L-351 made the one place for what skills are owed). One correction
  in the second: it first said L-351 had not been made that place; it
  had, on October 4.
- The swap log read at gallery 4cfeca27: 29 lines, all ok; runs
  20261004T205153Z and 20261006T182032Z show staging_to_live taking two
  attempts, both Tony's hand builds with OneDrive paused. The L-216
  retry is PROVEN; the lock recurs even when paused; the retry absorbs
  it. The empty "solar-system (N)" folders are not a retry remnant.
- Tony's rulings of October 7, each in its own records-only patch,
  tested on copies of 8653ef1b alone and in both orders with the two
  Opus patches of the day:
  - `patch_L412_1_rice_ruling_20261007.py`: an item inside an ordered
    list needs no RICE score; items outside keep it (L-412 (a)).
  - `patch_L001_1_earth_system_track_20261007.py`: the Earth System
    track is central and behind the website build, the gallery's cards
    serving meanwhile; L-071 and L-077 (the 2026 heat domes) close,
    "the event is over"; the road gains stage 14.
  - `patch_L216_1_hand_run_stands_20261007.py`: the daily hand run with
    its four checks stands; Daily Run pauses OneDrive 24 hours; no
    schedule or move off OneDrive to be proposed again.
- This closing patch: ledger-and-session-records 1.17 (the Where We Are
  rules, RICE for lists, which repository a record goes to, flat);
  protocol v3.85; Where We Are in the new shape; L-422 opened.

## Tony's words that became rules (L-422)

- "I use the where we are to record the run record and rename it with
  a time stamp." -> the run-record zone, and the close reads his copy.
- "Confirmed, but no subfolder. I already mix handoffs, patches, design
  documents. Subfolders are more steps and also I scan the files to see
  what the recent changes were." -> documentation/ stays flat.
- "all ledger L-xxx items should have a brief parenthetical label."
- "Why don't you update the skill and add your own Where We Are
  updating with this Fable session." -> this patch, not the Horizons
  session's.

## Discrepancies surfaced, not resolved here

- `daily_run.py` (gallery) still says the OneDrive pause lasts 2 hours
  (lines 155 and 166); Tony pauses 24. One-line fix, owed on L-216.
- "Conflict copies" wording stands in four places (gallery .gitignore,
  check_cache_siblings.py, the orrery dashboard,
  L342_install_test_run_sequence.md) after the cause was ruled out.
- The scanner prints a whole-tree Tier-1 count (296) and no gate-path
  figure; the page's Signals say so. Owed on the provenance-discipline
  bump (L-414, L-351).
- patch_L418_2 was built on fbd223ee, before the Horizons design
  session, and rewrote the page whole; this patch's page takes the
  design round as done. The pattern is the founding case of the
  edit-by-section rule.

## Open decisions for Tony (rollup)

- **(decide)** Whether L-216 (the swap retry) closes. Recommended yes:
  the retry is proven and the hand run is ruled.
- **(decide)** L-412 question (b): the handful of RICE scores the sweep
  proposes (L-131 and L-128 at 3/3/70/2; L-228, L-241, L-292 confirmed;
  L-252 re-scored).
- **(decide)** Whether the gallery-checks list (L-235, L-237, L-262,
  L-367, L-378, L-357, L-379, L-360, L-380, L-388) becomes one ledger
  item before it is built. Road stage 9 has no handle today.
- **(decide)** L-027 (the panel colour) closes once patch_L027_2 has
  run; its last gap was discharged by the October 6 skills sweep.
- **(do)** Reinstall ledger-and-session-records (1.17); replace the
  Project's instructions with PROJECT_INSTRUCTIONS.md v3.85.
- **(do)** Move the day's six patch scripts into documentation/.

## The obligation that travels

The next session confirms its loaded copy of ledger-and-session-records
reads 1.17 before any ledger, handoff or session-record work. A
reinstall during a session is not visible to that session.

## Next-session scoping

In the order the sweep's report gives: (1) the typed facts (L-421)
in a fresh session from `MANIFEST_L421_typed_facts_20261006.md`; it
also confirms interactive-exhibit 1.12 and carries the `_declared`
"1.1 times" fix in the gallery's objects_config; (2) the
provenance-discipline bump carrying L-414 and L-351; (3) the Sun's
list from item 3 (L-385, L-228, L-411); (4) the Horizons check build
(L-395) from `DESIGN_L395_horizons_check_20261007.md`; (5) the
gallery-checks list as a ledger item, then its build.

## The page this patch replaced

Every line of `documentation/WHERE_WE_ARE.md` as it stood when this
patch ran, after the day's five patches and with any note Tony had
written on it. Kept here because the rewrite was whole (a change of
shape); from now on patches edit the page by section.

    <!-- Doc-Kind: hand | Where the project is and where it is going, in plain words. One file, rewritten in place; read it at the end of every session. -->
    # Where We Are
    
    Last updated: October 6, 2026, end of the skills sweep session.
    - Written at orrery fbd223ee. This session only designed: no code and
      no skill changed.
    
    > **READ THIS FIRST**
    >
    > **Changed this session:**
    > - All eleven skills were checked against the repo and the manifest.
    >   All match, including the three new versions you installed.
    > - The longest skill, provenance-discipline, is too long to be read
    >   whole: one read of a file shows 16,000 characters, and the skill
    >   has 137,837. The skill that guards facts and sources is the one
    >   least likely to be read in full.
    > - You confirmed a design to split it. The cross-checking procedure
    >   becomes its own skill, two long sections move into files inside
    >   the skill's folder, and a read plan at the top says which lines to
    >   read in turn. No rule is reworded.
    > - No skill is retired: every one has open work behind it.
    >
    > **Do next:**
    > - *Install the trial skill, then check it in a fresh session.*
    > - *The typed facts, in a fresh session, from the plan written on
    >   October 6.*
    >
    > **Needs you now:**
    > - *Run this closing patch, then the maintenance run, and push.*
    > - *Install install-probe.zip from Settings, and keep it out of the
    >   repo.*
    
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
    
    ## The road
    
      1. [done]   The Sun's room is live on the website.
      2. [done]   Earth's room is live, with every number traced to its source.
      3. [done]   The numbers come from one place: the orrery feeds the
                  website, and nothing is typed twice.
      4. [done]   The Solar System room becomes a second way in: all the
                  planets, a drawer to pick them, and a way into each
                  body's own room.
      5. [NOW]    *Earth's old items are finished, in the order you
                  confirmed.* The website patch is live; the typed facts
                  are the last part, with the design talks.
      6. [next]   The facts typed in the Earth and Sun rooms' code move into
                  the served data, with their sources.
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
     14. [later]  The Earth System layers -- heat, food insecurity, the
                  oceans -- come to the website from their generators and
                  sources, the way the orrery's numbers do. Until then the
                  gallery's Earth System cards carry them, as you ruled.
                  << new this session
     15. [goal]   The website does what the desktop orrery does, from data
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
    - The skills: all eleven match the repo and the manifest at fbd223ee.
      - provenance-discipline is 137,837 characters, and one read shows
        16,000, so most of its rules are not seen on a plain read.
      - The split you confirmed takes it to about 61,000 characters and
        moves the cross-checking procedure into a new skill,
        provenance-cross-check.
      - A read plan at the top of each long skill will say which lines to
        read in turn, so the rest is read whole.
      - First, a throwaway skill tests whether your account keeps the
        extra files in a skill's folder.
    
    ## The next three steps  **>> UPDATED THIS SESSION**
    
    1. *Your run of this closing patch, and the trial skill's install.*
    2. The typed facts move into the served data, in a fresh session, from
       `documentation/MANIFEST_L421_typed_facts_20261006.md`.
    3. The Horizons check's design round, in its own session, from
       `documentation/HANDOFF_L395_horizons_check_design_20261005.md`.
    
    The provenance-discipline split is built in its own fresh session
    once the trial passes, from
    `documentation/PREDESIGN_L418_provenance_skill_split_20261006.md`.
    It can go before or after the two above; the order is yours.
    
    ## Waiting on you  **>> UPDATED THIS SESSION**
    
    Now:
    - Run this closing patch, run orrery_maintenance_run.py, commit and
      push.
    - Install the trial skill, install-probe.zip, from Settings. Keep the
      ZIP out of the repo: inside skills/ it would join the manifest.
    - After the next session checks it, delete install-probe.
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
      - This session: L-418, the provenance-discipline split, designed and
        confirmed. It stays open until the split is built.
      - Earth's website session: L-413 (Earth's list), L-349 (the belt's
        words), L-379 (the saved scene), L-300 (the collapsed-features
        check), L-292 (the geocorona note), L-421 (the typed facts,
        opened). Closed: L-349, L-300, L-369 (Earth's tilt in words), L-415
        and L-419 (skill rules confirmed).
      - The galactic plane: L-420; the panel colour: L-027; their record:
        `documentation/HANDOFF_L420_galactic_plane_20261006.md`.
    - The plan for the typed facts:
      `documentation/MANIFEST_L421_typed_facts_20261006.md`
    - This session's record:
      `documentation/HANDOFF_L418_skill_split_design_20261006.md`
    - The split's design:
      `documentation/PREDESIGN_L418_provenance_skill_split_20261006.md`
    - Earth's website session's record:
      `documentation/HANDOFF_L413_earth_website_20261006.md`
    - The skills' old version history: `documentation/SKILL_HISTORIES.md`
    - The reasoning behind the order:
      `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md`
    - For the Horizons round:
      `documentation/HANDOFF_L395_horizons_check_design_20261005.md`
