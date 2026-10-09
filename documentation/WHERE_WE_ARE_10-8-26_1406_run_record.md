<!-- Doc-Kind: hand | Where the project is and where it is going, in plain words. One file, edited by section; Tony's run record sits below the marker at the end and no patch edits it. -->
# Where We Are -- **Tony**: notes and run record --

Last updated: October 8, 2026, after the Horizons design's close.
- Written at orrery 3b36b3bf and gallery ab66aba7, before your run of
  patch_L395_4.

> **READ THIS FIRST**
>
> **Changed since you last read this:**
> - 15 of the 17 typed facts are served with their sources and live,
>   in three website patches. You found every hover's words correct.
> - Earth's four drawn guides have Read more links: the Sun
>   Direction, the rotation axis, the day-night line and the Moon.
> - Their sources reach the panel now; they had been served but not
>   shown. The panel's words and footer are brighter.
> - The inner Oort cloud is drawn flat, but a 2025 paper finds it
>   tilted about 30 degrees. You ruled it is redrawn now, as part of
>   the Sun's slice.
>
> **Do next:** *finish the typed facts: the inner Oort cloud redrawn
> tilted, then the check that keeps facts out of the code.*
>
> **Needs you now:**
> - *Run this closing patch, then orrery_maintenance_run.py, and push.* -- everthing has run and pushed. 

*Italic* lines are the must-reads. Marks reset at every update.

## The road  **>> UPDATED THIS SESSION**

  1-4. [done]  The Sun, Earth and Solar System rooms are live; the orrery
               feeds the website and nothing is typed twice.
  5.   [NOW]   *Earth's old items are finished, in your order.* The
               website patch and Earth's typed facts are live.
  6.   [next]  The typed facts: 15 of 17 served. Left: the inner Oort
               cloud, redrawn tilted, and the check. << moved this session
  7.   [next]  The Sun's numbers get the checking Earth's got.
  8.   [next]  The served objects are checked against JPL Horizons.
               Designed and recorded; build next, with Encke added
               to the orrery's list. << new this session
  9.   [next]  The website's checks get a short list of their own.
 10.   [next]  A bare interactive.html link opens the Solar System room;
               the Explorer gets its own address.
 11.   [later] The rest of the orrery's objects come to the website.
 12.   [later] Encounters: comets and spacecraft at the dates that matter.
 13.   [later] The planets get their details, Jupiter and Saturn first.
 14.   [later] The Earth System layers; the gallery's cards meanwhile.
 15.   [goal]  The website does what the desktop orrery does, with a date
               to choose, within the range the data covers.

## Settled  **>> UPDATED THIS SESSION**

Standing rulings. A line leaves after a few weeks, once it is habit.
- The galactic tide keeps its cone, to show its pull as physics. (Oct 7)
- No colour or other name that only one system knows. The panels'
  grey is one name, gray90. (Oct 6)
- The daily hand run stays a hand run. (Oct 7)
- OneDrive: pause 24 hours before a build; the retry absorbs the lock
  either way. Empty "solar-system (N)" folders are harmless; delete by
  hand. (Oct 7)
- Items in an ordered list carry no RICE score. (Oct 7)
- Every ledger handle on this page carries a short label. (Oct 7)
- Code types only words about our picture; facts are served. (Oct 6)
- The inner Oort cloud is redrawn from the 2025 paper now, as part of
  the Sun's slice, not deferred. (Oct 6)

## Signals

Read from files when this page was written, not typed from memory.
- Last cache build: 20261008T013323Z, ok, one attempt. Last retry: the
  Oct 6 18:20 hand build, two attempts, ok.
- Tier-1 findings, whole tree: 296, unchanged since Oct 6. No tool yet
  prints the number on the gate path alone; that is owed on the
  provenance-discipline bump.
- This page's date and the ledger's newest stamp: both Oct 8. Agree.

## Waiting on you  **>> UPDATED THIS SESSION**

At the next design talk:
- The fuzzy outer corona, with the dust cloud; the exosphere the same way.
- Moving the highlighted row to the top of the list.
- GO's arrow, only if the text box stays centred.
- Earth's design talks, the belts' shape first.
- Whether the phone's Sun room gets the galactic plane, its poles,
  Sgr A* and the tide's cone: L-408 (the galactic plane on the phone).
  You: "awaits the design talk." (Oct 7)
- The inner Oort cloud's tilted disk: its words, and whether its outer
  edge moves from 20,000 au to the paper's 10,000.

Decisions, one at a time:
- At the Horizons check's build, L-395 (the Horizons check): whether
  Halley is checked too, and Encke's description and link.
- Whether L-216 (the swap retry) closes. Recommended: yes.
- The handful of RICE scores the sweep proposes.
- Whether the gallery-checks list becomes a ledger item before building.

Not urgent, in your order:
1. Whether the editor also edits the Solar System room's rows.
2. Choosing a date, and animation.
3. The scattered disk, with the Kuiper belt. Not the fuzzy-boundary idea.

## Where the details are  **>> UPDATED THIS SESSION**

- Every item: `LEDGER_CONSOLIDATED.md`. The Fable sweep: L-422 (the ledger
  skill at 1.17 and this page), L-001 (the Earth System track), L-071
  and L-077 (the 2026 heat domes, closed), L-216 (the swap retry and
  the hand run), L-412 (the RICE ruling), L-395 (the Horizons check,
  designed). Open for build: L-421 (the typed facts), L-418 (splitting
  provenance-discipline).
- The Fable sweep's record:
  `documentation/HANDOFF_L422_fable_sweep_close_20261007.md`
- The galactic plane and the panel colour, both closed: L-420 (the
  galactic plane), L-027 (the panel colour);
  `documentation/HANDOFF_L420_galactic_plane_20261006.md`
- The sweep's report: `documentation/LEDGER_SWEEP_review_20261007.md`
- The typed facts: plan
  `documentation/MANIFEST_L421_typed_facts_20261006.md`; record
  `documentation/HANDOFF_L421_typed_facts_20261008.md`
- The Horizons check design:
  `documentation/DESIGN_L395_horizons_check_20261007.md`
- The reasoning behind the order:
  `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md`

--- Your run record below this line. No patch edits it; the length cap
--- stops here; the close reads your timestamped copy and clears this.

**Tony**: Run record:

+++++++++++++++++++++++++++++++++++++++++++++++++++++++

**Session: OPEN: 10-8-26 1451: Fable: Opus design and build coordination**

I'll read the project's preferences and principles files, then pull the repo at HEAD to ground the review before suggesting anything.

Ground truth first, then the suggestion.

**What I checked**
- The orrery repo is at `b0b3df82`, pushed at 14:49 today. That commit holds Opus's split brief (`HANDOFF_L418_split_build_brief_20261008.md`) and your 14:06 run record. The gallery is at `ab66aba7`, unchanged. So everything in your run record is pushed; nothing is waiting on you from the last two sessions.
- At HEAD, the protocol reads v3.85 and the ledger skill reads 1.17. I have not loaded my account copy of the ledger skill, because this session writes no ledger or page edits. If that changes I will check it first.
- The install probe is not in this session's skill list either. That agrees with Opus's finding: it has not been uploaded yet, or was deleted before a check.

**Where things stand, in one line each**
- L-421 (the typed facts): 15 of 17 served. Left: the inner Oort cloud redrawn tilted, then the gating check, then the citation-agreement check.
- L-418 (splitting provenance-discipline): fully briefed, blocked only on the install trial.
- L-395 (the Horizons check): designed; build is next on the road.
- L-414 (the scanner's window): owed before the Sun's list reaches L-228 (the Alfven ranges).
- Four decisions sit with no session attached: L-216 (the swap retry) closing, the RICE scores, the gallery-checks list as a ledger item, and L-371/L-390 riding the split.

**Suggested order of sessions**

1. **You, now, no session:** upload `install-probe.zip` from Settings > Skills. Keep the ZIP outside the repo.

2. **Opus session A: the probe check and the split build, in one session.** Open a fresh chat, say "check the install probe." If it passes, the same session measures the read limit and builds the split from the brief, rather than handing off to yet another fresh session. The brief is complete and nothing has changed under it, so a second handoff would be overhead. It will ask one decision: whether L-371 (the Sun room's served numbers) and L-390 (the conversion marker) ride version 2.27. Opus recommended yes, with L-414 (the scanner's window) kept for its own session; I agree. After the run: maintenance run, push, upload the three ZIPs, delete install-probe.
   - Why this before the Oort cloud: the Oort cloud build is citation-heavy, and the part of provenance-discipline it most needs (the cross-check procedure) is the part a plain read currently never reaches. The split fixes that. The protocol's own rule is skill bumps before builds.

3. **Opus session B: finish L-421 (the typed facts).** The inner Oort cloud redrawn from Nesvorny et al. 2025 as a tilted disk, its words brought to you before they ship, and the outer-edge question (20,000 au served vs the paper's 10,000) traced before it is asked. Then the survey as a gating check, shown failing on a planted sentence first. Two small owed fixes should ride this session because it touches the same files: the gallery's `_declared` "1.1 times" fix, and the citation-agreement check between `objects_config.json` and `constants_new.py`. Have the paper ready to upload from `papers/`. This session confirms its loaded skills read 2.27, 1.0 and 1.18.

4. **Opus session C: build L-395 (the Horizons check)** as a Daily Run step, with Encke added. Carry the one-line `daily_run.py` fix (it still says the OneDrive pause is 2 hours; you pause 24) under L-216 (the swap retry), since the session is in that file anyway. Decisions it will ask: whether Halley is checked, and Encke's description and link.

5. **After that:** the Sun's list from item 3, L-385 (the Sun's opening view); then L-414 (the scanner's window) as its own session cutting provenance-discipline 2.28, before L-228.

The three loose decisions (L-216 close, the RICE scores, the gallery-checks ledger item) can be ruled whenever you like and recorded by whichever session closes next; none of them blocks the order above. The design talks (the fuzzy corona, the belts' shape, L-408 the galactic plane on the phone) stay parked until you want a design session.

One session at a time is my recommendation, since each closes by editing the ledger and your page.

**My one question:** does this order stand, or do you want the Oort cloud (session B) ahead of the split (session A)?

**Tony**: decision session instead

I'll pull the exact wording of each open decision from the ledger and the sweep report, so the handoff carries the options as they stand rather than from memory.

I have what I need. Writing the handoff now.

The brief is `HANDOFF_decisions_session_brief_20261008.md`, anchored on orrery `b0b3df82` and gallery `ab66aba7`.

**What it sets up**
- A phone session: Opus presents one decision per message, you rule, and nothing in it asks you to run, upload or push. The patch and the handoff come out as files for when you are at your machine.
- Six decisions, smallest first: L-216 (the swap retry) closing; the RICE scores; the gallery-checks list as a ledger item; Halley and Encke's words for L-395 (the Horizons check); what rides the split's version 2.27 for L-418; and the order of the next three sessions.
- One thing I found while writing it: most of the proposed RICE scores are moot under your own October 7 ruling, because those items sit inside ordered lists. The real question left there is L-252 (an INCOMPLETE verdict is not a confirmation), which still carries the second-highest score in the ledger with an empty Gap. The brief says so, and asks Opus to strike the dead scores so the index matches the rule.

To open the session, attach the file to a fresh Opus chat in this Project and paste:

> Decisions session, from the attached brief. No build, no design. Read back the version of ledger-and-session-records you loaded, then present decision 1.

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

**Session: DONE: 10-8-26 1314: Opus: Horizons check design handoff documentation**

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/patch_L395_4_run_confirmed_and_page_20261008.py
ok  LEDGER_CONSOLIDATED.md         header stamp
ok  LEDGER_CONSOLIDATED.md         L-395 date
ok  LEDGER_CONSOLIDATED.md         L-395 Tony's run
ok  WHERE_WE_ARE.md                header date
ok  WHERE_WE_ARE.md                road stage 8
ok  WHERE_WE_ARE.md                decisions: the Horizons build

patch applied

NEXT:
  1. Run orrery_maintenance_run.py -- it rebuilds the ledger's index.

======================================================================
MAINTENANCE RUN -- generators, then checkers (L-188)
======================================================================
  Provenance scan is current (last run 20261008T190120Z, 0 day(s) ago).

GENERATORS -- regenerate every time; a no-op when nothing moved
----------------------------------------------------------------------
  Ledger index                 1.3s  rewrote LEDGER_CONSOLIDATED.md
  Skill manifest               0.1s  unchanged (1 of 1 rewritten, content
                                     identical)
  Constants export             0.7s  unchanged (1 checked, not written)
  Objects export               0.1s  unchanged (1 checked, not written)
  Module atlas                 9.5s  rewrote MODULE_ATLAS.md, MODULE_INDEX.md
  Data inventory               5.5s  unchanged (1 of 1 rewritten, content
                                     identical)
  Exact rows report            2.1s  unchanged (1 checked, not written) -- 13 of
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
  Skill headers                0.2s  11 skills parsed, no consistency problems.
  Exact rows by the count      2.1s  PASSING -- 13 printed exact rows each state
                                     a count; 32 orrery lines print through
                                     exact_text() or row_text(); 10 gallery lines
                                     are served the count
  Dimensions                   1.5s  No unit contradicts its arithmetic: 54
                                     derived row(s) read -- 42 OK, 9 NO UNIT, 3
                                     NOT CHECKABLE.
  Cross-check annotations      0.1s  19 of 19 cross-check annotation tests
                                     passed.
  Citation inheritance         0.2s  20 of 20 citation-inheritance tests passed.
  Status lines                 0.1s  All 105 status lines in constants_new.py are
                                     well formed; 53 rows carry none.
  Row shape                    0.1s  All 161 row shapes in constants_new.py fit
                                     the assignment's own line.
  Scanner recognition 1d/1e    0.3s  27 of 27 recognition pins hold: real
                                     citations recognized, fake ones refused.
  Reset completeness          18.3s  PASS -- all 310 IntVars + 3 StringVars + 10
                                     entries reset to startup defaults; date set
                                     to now.
  Orbit cache                  2.5s  All 6 orbit cache tests passed: cache loads,
                                     old formats convert, corrupted entries are
                                     dropped.
  Earth pole of date           0.4s  all 14 checks passed (geometry, ERFA,
                                     fallback, cache, hover, transform).
  Worksheet checker           12.2s  74 of 110 routed, 8 clean
  Worksheet checker tests     20.9s  All 135 checks passed
  Worksheet key round trip     1.4s  RESULT: 52 sites minted 52 distinct keys,
                                     all resolved; 52 pinned keys still resolve;
                                     1 retired keys confirmed gone.
  Builder marker join         31.0s  All 76 checks passed
  Extractor pins               0.6s  RESULT: 29 string sites carry the pinned 73
                                     claims and 14 instruction drops, at LOOKBACK
                                     30 / LOOKAHEAD 25, extractor version 2.
  Provenance scanner          14.9s  296 TIER-1 FINDINGS IN THE SCANNED TREE

======================================================================
  20 of 20 gating checkers passed -- 129.7s total
  2 report-only, exit 0 whatever they find:
    Worksheet checker           74 of 110 routed, 8 clean
    Provenance scanner          296 TIER-1 FINDINGS IN THE SCANNED TREE
======================================================================

FILES WRITTEN THIS RUN
----------------------------------------------------------------------
  2112 file(s) examined, 7 written, 0 created, 0 removed, 5 rewritten identically
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

  2. Move this script into documentation/; commit and push. -- cdb99833b657c2298c333b2200e634db9854fe31
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 

Where this leaves us

The served objects are checked against JPL Horizons: designed and recorded; build next, with Encke added to the orrery’s list.
At that build, you decide whether Halley is checked too, and Encke’s description and link.

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

**Session: DONE: 10-8-26 1442: Opus: Updating skills for Claude Opus 5.5 compatibility**

The handoff is written: `HANDOFF_L418_split_build_brief_20261008.md`, for the orrery's `documentation/` folder. It's built on your push at `cdb99833`. I read the ledger skill at 1.17, and this session's loaded copy matches the repo.

**What the new session will find**
- **The trial skill has not been checked yet.** This session's list of installed skills has no install-probe. So either it was never uploaded, or it was deleted before a check. I've re-sent the ZIP in case you need it.
- **The ledger skill is now cut at 1.18, not 1.17.** The Fable sweep took it to 1.17, as your run record noted.
- **Nothing else the split touches has changed** since the design. The design's sizes still hold.
- **A measurement to redo first.** The design assumed one read of a file shows 16,000 characters. This session's file reader is documented as showing 2,000 lines instead. The new session measures its own reader before writing the read plan, so the plan fits the tool actually in use.
- **One thing to watch at the trial.** Your eleven skills arrive marked as installed through a plugin. If the trial skill arrives marked differently, uploading a ZIP may not be the same route as your usual install. The brief says to report that plainly.

**One decision for you, which the new session will ask before building**
- Three sentence fixes are owed to provenance-discipline. The question is whether they ride the split's version.
- I recommend:
  - the two small ones go in with the split: L-371 (the Sun room's served numbers) and L-390 (the conversion marker);
  - L-414 (the scanner's window and declared rows) gets its own session, because it changes the scanner itself.
- You can answer "as recommended" or "split only" when the new session asks.

Is the trial skill uploaded, or should that be your first step?

**Where this leaves us:** the split is designed, ruled and briefed. Next, a fresh session checks the trial skill and then builds the split in one patch.

==============================================================

Good. Uploading it before anything else is right, because the build depends on the result.

**The steps**
1. Save `install-probe.zip` somewhere outside the repo folder, such as Downloads.
2. In Settings, under Skills, choose Upload skill and pick the ZIP.
3. Open a **fresh** chat in this Project and say: "check the install probe." A chat that was already open won't see the new skill.
4. That session reports one of three results:
   - **PASS:** the extra file arrived.
   - **FAIL:** only the main file arrived. The split is not built, and we redesign.
   - **NOT INSTALLED:** nothing was found.

   It also reports how the skill is marked compared with your eleven, which tells us whether the trial speaks for them.
5. After that check, delete install-probe from Settings.

If it passes, the split build goes to another fresh session, started from the brief in `documentation/`.

**Where this leaves us:** you upload the trial skill next, then a fresh chat checks it. The split build waits on that result.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

**Session: OPEN: 10-8-26 1657: Opus: Ledger-session-records decisions**

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/patch_L412_2_decisions_20261008.py
ok  LEDGER                   header stamp
ok  LEDGER                   L-216 closed
ok  LEDGER                   L-216 decide line marked decided
ok  LEDGER                   L-216 Gap closed
ok  LEDGER                   L-216 no-pause trial note
ok  LEDGER                   L-252 closed
ok  LEDGER                   L-252 Gap closed, paragraph re-homed
ok  LEDGER                   L-423 opened before L-412
ok  LEDGER                   L-412 date
ok  LEDGER                   L-412 question (b) answered
ok  LEDGER                   L-131 RICE struck
ok  LEDGER                   L-131 struck-score note
ok  LEDGER                   L-128 RICE struck
ok  LEDGER                   L-128 struck-score note
ok  LEDGER                   L-228 RICE struck
ok  LEDGER                   L-228 struck-score note
ok  LEDGER                   L-241 RICE struck
ok  LEDGER                   L-241 struck-score note
ok  LEDGER                   L-292 RICE struck
ok  LEDGER                   L-292 struck-score note
ok  LEDGER                   L-235 RICE struck
ok  LEDGER                   L-235 struck-score note
ok  LEDGER                   L-237 RICE struck
ok  LEDGER                   L-237 struck-score note
ok  LEDGER                   L-262 RICE struck
ok  LEDGER                   L-262 struck-score note
ok  LEDGER                   L-262 fixes found already in
ok  LEDGER                   L-367 date
ok  LEDGER                   L-367 list membership
ok  LEDGER                   L-378 date
ok  LEDGER                   L-378 list membership
ok  LEDGER                   L-360 date
ok  LEDGER                   L-360 list membership
ok  LEDGER                   L-380 date
ok  LEDGER                   L-380 list membership
ok  LEDGER                   L-388 date
ok  LEDGER                   L-388 list membership
ok  LEDGER                   L-235 date
ok  LEDGER                   L-235 list membership
ok  LEDGER                   L-237 date
ok  LEDGER                   L-237 list membership
ok  LEDGER                   L-357 date
ok  LEDGER                   L-357 delete ruling
ok  LEDGER                   L-351 date
ok  LEDGER                   L-351 gallery-cache-builder owed items
ok  LEDGER                   L-395 date
ok  LEDGER                   L-395 decide line marked decided
ok  LEDGER                   L-395 rulings recorded before the Gap
ok  LEDGER                   L-418 date
ok  LEDGER                   L-418 2.27 ruling and the approved paragraph
ok  LEDGER                   L-414 date
ok  LEDGER                   L-414 own session, 2.28
ok  WHERE_WE_ARE             header date
ok  WHERE_WE_ARE             box: old changed line 1  (removed)
ok  WHERE_WE_ARE             box: old changed line 2  (removed)
ok  WHERE_WE_ARE             box: old changed line 3  (removed)
ok  WHERE_WE_ARE             box: old changed line 4  (removed)
ok  WHERE_WE_ARE             box: changed since
ok  WHERE_WE_ARE             box: do next (the confirmed order)
ok  WHERE_WE_ARE             box: old needs-you line  (removed)
ok  WHERE_WE_ARE             box: needs you now
ok  WHERE_WE_ARE             road: stage 6 mark cleared
ok  WHERE_WE_ARE             road: stage 8
ok  WHERE_WE_ARE             road: stage 9
ok  WHERE_WE_ARE             settled: OneDrive, and no numbers in object words
ok  WHERE_WE_ARE             waiting: decisions cleared
ok  WHERE_WE_ARE             details: this session

New item: L-423 (the website's checks).
Stamps updated: LEDGER_CONSOLIDATED.md header stamp; WHERE_WE_ARE.md "Last updated" lines.
Where We Are: 126 lines above the run-record marker (cap 130); nothing below it touched.

patch applied

NEXT:
  1. Run orrery_maintenance_run.py -- it rebuilds the ledger's index
     and moves L-216 and L-252 into the closed section.

======================================================================
MAINTENANCE RUN -- generators, then checkers (L-188)
======================================================================
  Provenance scan is current (last run 20261008T192100Z, 1 day(s) ago).

GENERATORS -- regenerate every time; a no-op when nothing moved
----------------------------------------------------------------------
  Ledger index                 1.5s  rewrote LEDGER_CONSOLIDATED.md
  Skill manifest               0.2s  unchanged (1 of 1 rewritten, content
                                     identical)
  Constants export             1.4s  unchanged (1 checked, not written)
  Objects export               0.1s  unchanged (1 checked, not written)
  Module atlas                 7.5s  rewrote MODULE_ATLAS.md, MODULE_INDEX.md
  Data inventory               5.0s  unchanged (1 of 1 rewritten, content
                                     identical)
  Exact rows report            2.2s  unchanged (1 checked, not written) -- 13 of
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
  Reset completeness          18.8s  PASS -- all 310 IntVars + 3 StringVars + 10
                                     entries reset to startup defaults; date set
                                     to now.
  Orbit cache                  1.9s  All 6 orbit cache tests passed: cache loads,
                                     old formats convert, corrupted entries are
                                     dropped.
  Earth pole of date           0.3s  all 14 checks passed (geometry, ERFA,
                                     fallback, cache, hover, transform).
  Worksheet checker            9.9s  74 of 110 routed, 8 clean
  Worksheet checker tests     15.4s  All 135 checks passed
  Worksheet key round trip     0.9s  RESULT: 52 sites minted 52 distinct keys,
                                     all resolved; 52 pinned keys still resolve;
                                     1 retired keys confirmed gone.
  Builder marker join         20.5s  All 76 checks passed
  Extractor pins               0.4s  RESULT: 29 string sites carry the pinned 73
                                     claims and 14 instruction drops, at LOOKBACK
                                     30 / LOOKAHEAD 25, extractor version 2.
  Provenance scanner           8.5s  296 TIER-1 FINDINGS IN THE SCANNED TREE

======================================================================
  20 of 20 gating checkers passed -- 101.6s total
  2 report-only, exit 0 whatever they find:
    Worksheet checker           74 of 110 routed, 8 clean
    Provenance scanner          296 TIER-1 FINDINGS IN THE SCANNED TREE
======================================================================

FILES WRITTEN THIS RUN
----------------------------------------------------------------------
  2118 file(s) examined, 6 written, 0 created, 0 removed, 6 rewritten identically
    written   LEDGER_CONSOLIDATED.md
    written   MODULE_ATLAS.md
    written   MODULE_INDEX.md
    written   PROVENANCE_AUDIT.md
    written   data/provenance_history.json
    written   documentation/prompts/citation_review.jsonl
    rewritten with identical bytes, no action needed:
      DATA_INVENTORY.md
      PROJECT_INSTRUCTIONS.md
      WORKSHEET_CHECK.md
      data/worksheet_check_state.json
      data/worksheet_routed.json
      test_output/test_orbit_paths.json
    20 file(s) over 2 MB compared by size and mtime only

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>

  2. Move this script into documentation/, with these two files from
     the decisions session: HANDOFF_decisions_20261008.md and
     NOTE_for_split_session_L252_paragraph_20261008.md, and the
     brief HANDOFF_decisions_brief_20261008.md if it is not there.
  3. Commit and push.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++