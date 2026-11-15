<!-- Doc-Kind: hand | Where the project is and where it is going, in plain words. One file, edited by section; Tony's run record sits below the marker at the end and no patch edits it. -->
# Where We Are

Last updated: November 15, 2026: the Code session (Opus) that brought Phobos and Deimos into the orrery, Mars's session 1 of 2 (L-514 (the Mars room)).
- Written at orrery 488cad20 (your commit "mars moons") and gallery d3e97b15; GitHub's orrery has one nightly commit since, e5b5eb58. Part 2, the ledger and this page are not yet pushed.

> **READ THIS FIRST**
>
> **Changed since you last read this:**
> - Phobos and Deimos are now served by the orrery: each has its key, JPL's own name, NASA's sentence you chose, and NASA's page as its link (L-514 (the Mars room)).
> - Their periods are JPL's, fetched around Mars: Phobos 0.31914 days, Deimos 1.2625 days. The typed periods and the unsourced "Retrogade" are gone.
> - Their accuracy is one row in the constants store, 10 km for both, from the 2025 paper's "a few kilometers". The website reads it from the constants export.
> - The orrery's own hover uses it too, on your word: seen from Mars, Phobos prints to tens of kilometres, "rounded to JPL's published accuracy for Phobos's orbit around Mars", where it said "JPL states no accuracy".
> - The orrery's checks passed, 36 of 36, and JPL confirmed both moons' names and periods today.
>
> **Do next:** *Mars, session 2 of 2, the website: a coordinating session writes its brief first, then a Code session in the website builds the moons into Mars's fold.*
>
> **Needs you now:**
> - *(do) Commit the orrery (Part 2, the ledger, this page), then Pull origin (GitHub's nightly commit), then Push origin. The two files that commit also changed already match yours exactly.*
> - *(do) Each morning, Fetch origin and Pull origin on both, orrery then website, before any work. If Pull origin shows up only once you have changes: Commit them first, then Pull origin, then Push origin. If Desktop stashes your changes anyway, restore them at once: Changes tab, Stashed Changes, Restore.*
> - *(do) Renew palomasorrery.com at Porkbun by 13 Feb 2027 (L-516).*

*Italic* lines are the must-reads. Marks reset at every update.

## The road  **>> UPDATED THIS SESSION**

Your order of Nov 5 (run record `WHERE_WE_ARE_11-4-26_2321_run_record.md`).
  1-14.[done]  Through Nov 6: the three rooms, the objects, the Sun's and
               Earth's slices, historical missions' slice 1, the paths by
               the plan (L-476, closed), path or orbit by e (L-510), A1
               and A2 of JPL's fallbacks (L-512), a green website night,
               the quick wins with L-423 (the website's checks), and the
               Moon's standards (L-513, closed).
 15.   [NOW]   *Mars (Phobos, Deimos) as the first new fold (L-514 (the
               Mars room)): the orrery's half done Nov 15, the website's
               next. Then Uranus and Neptune. Io, Titan, Charon and Pluto
               come to standard in their folds, keyed in the orrery
               first.* << moved this session
 16.   [later] Earth's fold: L-297 (the Lagrange points), the Earth-Moon
               barycentre, SOHO, Gaia, James Webb, Artemis II.
 17.   [later] Small-body systems' moons; then stars and exoplanets.
 18.   [goal]  The website does what the desktop orrery does, with a date
               to choose, within the range the data covers.
  l-c. [done]  L-517 (the lobby), L-518 (the shared link) and L-519
               (Featured's rethink): closed Nov 8 and 9 on your phone looks.
  g.   [done]  L-527 (a first visit's guide): closed Nov 12.
  s.   [done]  Sudan on Google Earth web, Nov 13, and its guided walk, Nov 14 (L-001 (food insecurity)).
 15a.  [later] The Earth Science room, after Mars and the moons (L-531 (the Earth Science room)).
  d.   [beside] Document caps (L-522 (document caps)): steps 1 and 2
               built Nov 10 and 11, the page of caps and the exhibit
               skill's split; steps 3 to 6 between builds.
  b.   [beside] Housekeeping: L-424, L-425, L-426 (the checkers' three);
               L-423 (the website's checks) item 3; L-357 (stale gallery
               artifacts); L-509 (obsolete code), after its talk.

## Settled

Standing rulings; a line leaves once it is habit, or a skill carries it.
- Earth System layers move to Google Earth on the web, not the desktop app; a layer's one home is its page, earth/<its id>.html (Nov 13; L-001 (food insecurity), L-530 (the other layers on the web)).
- Sentences we compose use American spelling; IPC's quoted words keep IPC's; a symbol taken from IPC is marked "after IPC" (Nov 13; L-001 (food insecurity)).
- The room is used upright: held sideways it shows one line asking for the phone upright; the drawer need not work sideways (Nov 12; L-527 (a first visit's guide)).
- One body's failed accuracy test: "Hold the bad data and report, then continue." A hold is not red; the night's commit title names the held body. A moon is held only when JPL gives no answer; more than five held is a failed build (Nov 11, the coordinator's changes). The room's title stays unchanged for a held body; its box says it (Nov 11, your "Yes, keep it"; L-525 (hold the bad data)).
- The Sun direction line stays out of Earth's fold: the day-night shading and the Sun at its true place show the direction (Nov 10; L-515 (one nested tree)).

## Deferred

Waiting behind other work; a line leaves when picked up.
- ESCAPADE, Blue and Gold: its own round after the Mars build; their Mars arrival becomes the first encounter at the guided-encounters talk (Nov 14; L-533 (ESCAPADE), L-529 (guided encounters)).
- Guided encounters, the guide's way of telling used for a flyby: a design talk after Mars (Nov 12; L-529 (guided encounters)).
- The hold's leftovers: Earth's own box in its fold does not say a body is held; a close pass is held on its older orbit (L-526 (a close pass held)), before 2029 (Nov 11; L-525 (hold the bad data)).
- The orrery's own Kepler solvers start the way the website's did; safe today, listed on L-524 (the Kepler solver's start), for an orrery session (Nov 11).
- Step 2b's three leftovers: Io, Titan, Pluto and Charon have no words or i-panel link until the orrery keys them; Find misses a shell of Earth's by its own name until Earth's fold is first opened; a view centred on Jupiter is not in the shared link (Nov 10; L-515 (one nested tree)).
- Three checks red in the drawer walk before Scenes was built, the page or the walk aged: a gallery session that next opens the drawer (Nov 9; L-521 (three red checks)).
- The saved pictures' words, which have no source: kept as made until the braid reaches them (Nov 8; L-520 (old pictures carry old words)).
- Charon's period is asked around Pluto's centre, not the barycentre;
  fix it before Pluto's room (L-150 (trusting a near-equal pair), Nov 6).
- When the road turned to the symbols (Nov 5): L-512 (fallbacks when
  JPL cannot answer) slices b and c; L-484 (the two agree), its brief
  and build; L-504 (the orrery's clock), the Earth System, stamps and
  tools; L-510 part 2, the path plan asked from before any launch.
- The other Earth System layers on the web, and South Sudan when IPC publishes (Nov 13; L-530 (the other layers on the web), L-070 (other countries)).
- L-511 (the export carries the words): behind the check (Nov 3).
- L-508 (a held body's alarm), L-485 (a nightly run): the website honours no orrery hold yet; the alarm's quiet half waits, its loud half built (L-525, Nov 11).
- L-462 (a shorter run); L-128 (the ice lines); L-500 (eyeballed numbers).
- L-483 (a comet room), after historical missions' slice 2.
- L-489 (compositions), with L-486 and L-488 under it: Artemis II in
  the Earth room first, with slice 2 (L-507 (historical missions));
  Apollo 11's S-IVB with them (Nov 5).
- A body crossing e = 1: its drawer row waits for JPL's class (L-510 (the typed fields), Nov 5).
- A craft riding a planet on 7-day points cuts corners between windows:
  a later item on L-507 (historical missions) (Nov 5).
- L-490 (the legacy list); L-499 (kinds of session); L-471 (a delivered
  patch is final), for safe-file-editing's next version.

## Signals  **>> UPDATED THIS SESSION**

Read from files when this page was written, not typed from memory.
- Last cache build: 20261114T181334Z, ok, no retry on the swap (gallery swap log at d3e97b15, read Nov 15).
- Tier-1 on the gate path: 0, the push gate holds (PROVENANCE_AUDIT.md, this session's run at orrery 488cad20, read Nov 15).
- This page's date and the ledger's newest stamp: both Nov 15. Agree.

## Waiting on you

Decisions, one at a time:
- None now.

At the next design talk:
- How obsolete code is treated, and when it goes (L-509 (obsolete
  code)); two cases now, the orrery's unused date function and its
  Pluto-centred view of the moons.
- Planet 9: how to show a body that may not exist.
- Whether the site counts visits, and tells visitors (Nov 13; for the Earth Science room's talk, L-531 (the Earth Science room)).

Not urgent, in your order:
1. Whether the editor also edits the Solar System room's rows, and
   adds a new body as a form (L-489 (compositions)).
2. The website's second run: keep, or stand down after a clean 08:17
   (L-485 (a nightly run)).
3. Earth's list (L-413 (Earth's list)): open as enhancements, or closed
   with its seven pieces moved to their own items.

## Where the details are  **>> UPDATED THIS SESSION**

- Every item: `LEDGER_CONSOLIDATED.md`.
- This session: L-514 (the Mars room), "Session 1 built"; its brief `COORD_L514_orrery_moons_brief_20261114.md`. The session before: rulings 5 and the accuracy, and L-533 (ESCAPADE).
- The caps: `DOCUMENT_CAPS.md`; L-522 (document caps); its brief
  `COORD_L522_step1_caps_brief_20261110.md` and the review beside it.
- The tree: L-515 (one nested tree), its briefs `COORD_L515_*`.
- The door: `documentation/python_work_door/`, and L-499 (kinds of session).

--- Your run record below this line. No patch edits it; the length cap
--- stops here; the close reads your timestamped copy and clears this.

**Tony**: Run record:

