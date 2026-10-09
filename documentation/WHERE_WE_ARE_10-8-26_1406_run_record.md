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
  3. Commit and push. -- c921ef84bc3569b1d70e6a66ccee7b98e94c9958
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 

The new checks list gets the next free ledger number when the patch runs, and the patch prints it. That will be L-423, unless the split session adds an item first.

One small disagreement is noted in the handoff for later. The line above your run record says the close clears that section, but your brief said not to touch it. So the patch leaves it alone.

Where this leaves us

Every decision on your list is ruled. “Decisions, one at a time” on your page now says none are waiting.
The split session already has your 2.27 ruling and the checker paragraph.
Next is the typed facts, then the Horizons check build, then the Sun’s list.

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

**Session: OPEN: 10-8-26 1748: Opus: Install probe and split build**

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/patch_L418_3_split_build_20261008.py
patch_L418_3 -- built on orrery b0b3df82

ok  base: skills/provenance-discipline/SKILL.md, skills/ledger-and-session-records/SKILL.md, skills_index.py match orrery b0b3df82
ok  phase 1: 15 sections moved, each found whole in its new file: FIGCOUNT, REVIEW, LINK, THREE, ROLES, TWO, TYPES, NEG, ROUTE, QUOTE, FORMAT, EXHIBIT, BATCH, CREDIT, FIELD
ok  phase 1: 6 pieces stay in skills/provenance-discipline/SKILL.md: HEAD, REPORT, STORE, RETIRES, VERIFIED (and the text above the first)

PHASE 2 -- the listed edits, each shown before and after:

ok  skills/provenance-discipline/SKILL.md                read plan seed, and the 2.27 entry
      before | # Provenance Discipline
      before | 
      before | Skill version: 2.26 | 2026-10-05, with Anthropic's Claude Opus 5.5, at

      after  | # Provenance Discipline
      after  | 
      after  | Read this file in parts.
      after  | 
      after  | Skill version: 2.27 | 2026-10-08, with Anthropic's Claude Opus 5.5, at
      after  | palomas_orrery @ b0b3df82. v2.27 (L-418) splits the skill, and no rule is
      after  | reworded. The relay procedure, the Review-Repair Protocol, is now the
      after  | skill provenance-cross-check. Rules 1 to 8 of the figure count moved to
      after  | references/figures.md and the field notes to references/field-notes.md,
      after  | each opened when its pointer says; the withdrawn derived-row rule moved
      after  | to documentation/SKILL_HISTORIES.md. Every moved section is word for
      after  | word apart from the edits the build patch lists. The file opens with a
      after  | read plan, written by skills_index.py, because one read does not show
      after  | it whole: the design session's viewer showed 16,000 characters, from
      after  | the start and the end, and this session's reader showed lines 1 to
      after  | 1,106 and said it had stopped (2026-10-08). Riding this version: the
      after  | range rule's examples name rows that exist, and a patch predicts the
      after  | scanner's change rather than its total (both L-371); Rule 1 names the
      after  | conversion marker and Rule 8 records the widening as built (L-390); and
      after  | the examples in The Status Line and Report to the Figures You Have name
      after  | rows as they now stand.
      after  | Earlier: 2.26 | 2026-10-05, with Anthropic's Claude Opus 5.5, at

ok  skills/provenance-discipline/SKILL.md                v2.24 entry out to SKILL_HISTORIES.md (three-entry rule)
      before | v2.24 settles L-395 with one new section, A Simple Error a Check Finds
      before | Is Fixed and Reported. Tony's ruling, 2026-10-01: "simple errors such
      before | as the Apophis naming discrepancy should be fixed and reported." It
      before | says what counts as simple, that the fix rides the same patch and is
      before | named, what comes to Tony instead, how a number in a served description
      before | is sourced or removed, and how the rule sits beside The Braid.
      before | Older entries are in documentation/SKILL_HISTORIES.md, moved there
      before | on 2026-10-05 (L-418).

      after  | Older entries are in documentation/SKILL_HISTORIES.md, moved there
      after  | on 2026-10-05 and 2026-10-08 (L-418).

ok  skills/provenance-discipline/SKILL.md                contents list: the moved sections out, the new section in
      before | - Report to the Figures You Have [QUALITY]
      before |   - The Figure Count Is a Declared Field [QUALITY]
      before |   - The Store Carries the Verified Figure [CRITICAL]
      before |   - A Derived Row Stores the Figure Its Sources Support -- WITHDRAWN
      before | - Review-Repair Protocol for Cross-Checked Annotations
      before |   - A Link Is an Object, Not Text [QUALITY]
      before |   - Three Things the Prompt Must Require [QUALITY]
      before |   - Model Roles in the Competitive Pattern
      before |   - The Two-Dispatch Rule [CRITICAL]
      before |   - Worksheet Types
      before |   - A Negative Verdict Shows Its Search [CRITICAL]
      before |   - Route the Effort Tier by Job Type [QUALITY]
      before |   - Quoting a Worksheet Is Transcription, Not Interpretation [CRITICAL]
      before |   - Cross-Checked Annotation Format [CRITICAL]
      before |   - The Exhibit Requirement [CRITICAL]
      before |   - A Cross-Check Retires With Its Value or Its Citation [CRITICAL]
      before |   - Retired: `# Verified: April 2026 via Gemini fact-check`
      before |   - Batch Worksheet Workflow
      before |   - Model Credit in Annotations [PRACTICE]
      before | - Field Notes

      after  | - Report to the Figures You Have [QUALITY]
      after  |   - The Store Carries the Verified Figure [CRITICAL]
      after  | - Cross-Checked Lines in the Store
      after  |   - A Cross-Check Retires With Its Value or Its Citation [CRITICAL]
      after  |   - Retired: `# Verified: April 2026 via Gemini fact-check`
      after  | - Field Notes
      after  | 
      after  | Kept outside this file and opened when needed: `references/figures.md`
      after  | holds The Figure Count Is a Declared Field, Rules 1 to 8, and
      after  | `references/field-notes.md` the field notes. Sending a value to other
      after  | models for a check is the skill provenance-cross-check.

ok  skills/provenance-discipline/SKILL.md                range rule: a worked pair that exists (L-371)
      before | This is L-179's mechanism, generalised. `GRAVITATIONAL_INFLUENCE_AU` and
      before | `GRAVITATIONAL_INFLUENCE_RANGE_AU` are the existing pair: the range
      before | carries the citation and the access standard, the drawn number is a
      before | declared midpoint, and the hover shows the envelope.

      after  | This is L-179's mechanism, generalised. `HELMET_CUSP_LOW_RADII` and
      after  | `HELMET_CUSP_HIGH_RADII` are a worked pair: the two rows carry the
      after  | source, the access and the read, and the drawn `HELMET_CUSP_RADII` is
      after  | a declared construction over them, the top of the range. (Until v2.27
      after  | the example here was the gravitational influence, whose range rows
      after  | are gone: it is now the Sun's Hill radius, one calculated value.)

ok  skills/provenance-discipline/SKILL.md                range rule: who takes the midpoint (L-371)
      before | the gravitational influence takes the midpoint, the core takes the low

      after  | Earth's outer-belt peak takes the midpoint, the core takes the low

ok  skills/provenance-discipline/SKILL.md                range rule: the midpoint's users (L-371)
      before | midpoint** (v2.18). That is the construction the outer belt's peak and
      before | the gravitational influence already use. An end is picked only for a

      after  | midpoint** (v2.18). That is the construction the outer belt's peak
      after  | already uses. An end is picked only for a

ok  skills/provenance-discipline/SKILL.md                status line examples: rows as they now stand
      before | HELMET_CUSP_RADII = 4.0
      before | # Status: measured V_SOURCED 2026-08-28 -- abstract, open
      before | 
      before | CHROMOSPHERE_PHYSICAL_KM = 2000.0
      before | # Status: measured V_SOURCED -- access untested (textbook)
      before | 
      before | SOLAR_RADIUS_AU = SUN_RADIUS_KM / KM_PER_AU
      before | # Status: derived -- inherits SUN_RADIUS_KM, KM_PER_AU

      after  | HELMET_CUSP_HIGH_RADII = 4
      after  | # Status: measured V_SOURCED 2026-10-04 -- abstract, open
      after  | 
      after  | EARTH_MAGNETOPAUSE_SHUE_A1_RADII = 10.22
      after  | # Status: measured V_SOURCED 2026-09-11 -- open full text
      after  | 
      after  | EARTH_GEOSTATIONARY_RADIUS_KM = (EARTH_GM_KM3_S2 / EARTH_ROTATION_RATE_RAD_S ** 2) ** (1.0 / 3.0)
      after  | # Status: derived -- inherits EARTH_GM_KM3_S2, EARTH_ROTATION_RATE_RAD_S

ok  skills/provenance-discipline/SKILL.md                scanner mechanics: predict the change, not the total (L-371)
      before | - False positives get provenance_exceptions.json entries, not code
      before |   workarounds.

      after  | - False positives get provenance_exceptions.json entries, not code
      after  |   workarounds.
      after  | - **A patch predicts the scanner's CHANGE, not its total** (v2.27,
      after  |   L-371). Where a patch says what the run should print, it states how
      after  |   the Tier-1 count, and the findings it names, should move. The total
      after  |   differs between machines -- the sandbox and Tony's differed by one
      after  |   on 2026-10-04 -- and the patch script is itself scanned while it
      after  |   sits in the root folder, until it is moved to documentation/.

ok  skills/provenance-discipline/SKILL.md                report: where the figure-count rules now live
      before | the next reader does not re-derive it and a checker can read it; the
      before | section below says how the field is written and counted.

      after  | the next reader does not re-derive it and a checker can read it;
      after  | `references/figures.md` says how the field is written and counted.

ok  skills/provenance-discipline/SKILL.md                report: the example row is a derived row today
      before | EARTH_INNER_CORE_RADII = EARTH_INNER_CORE_KM / EARTH_EQUATORIAL_RADIUS_KM
      before | # Figures: 5 -- set by EARTH_INNER_CORE_KM (1221.5, 5)
      before | # Derived: 1221.5 / 6378.1366 = 0.19151

      after  | EARTH_GEOSTATIONARY_RADIUS_KM = (EARTH_GM_KM3_S2 / EARTH_ROTATION_RATE_RAD_S ** 2) ** (1.0 / 3.0)
      after  | # Figures: 7 -- set by EARTH_ROTATION_RATE_RAD_S (7.292115e-5, 7)
      after  | # Derived: (398600.4418 / 7.292115e-5^2)^(1/3) = 42164.17 km

ok  skills/provenance-discipline/references/figures.md   rule 1: the first form names a derived row today
      before | # Figures: 5 -- set by EARTH_INNER_CORE_KM (1221.5, 5)

      after  | # Figures: 7 -- set by EARTH_ROTATION_RATE_RAD_S (7.292115e-5, 7)

ok  skills/provenance-discipline/references/figures.md   rule 1: the conversion marker (L-390)
      before | lose the count.
      before | 
      before | **Rule 2.

      after  | lose the count.
      after  | 
      after  | **A conversion carries none of these lines** (v2.27, L-390). A name the
      after  | orrery keeps for a value in another unit (Rule 3) is marked with one
      after  | comment key instead, naming the row it converts:
      after  | 
      after  | ```
      after  | # Conversion: of <ROW> -- computed from that row, which carries the source and the count
      after  | ```
      after  | 
      after  | It carries no `# Figures:`, `# Status:`, `# Derived:`, `# Source:`,
      after  | `# Read:` or `# Cross-checked:` line, because its count and its source
      after  | are its row's. Its expression is that one row scaled only by rows that
      after  | define units. `constants_rows.conversion_problem()` checks it (Rule 8).
      after  | 
      after  | **Rule 2.

ok  skills/provenance-discipline/references/figures.md   rule 3: a conversion is marked (L-390)
      before | orrery's drawing code keeps for such a value is computed from the one
      before | row and states no precision of its own.

      after  | orrery's drawing code keeps for such a value is computed from the one
      after  | row, is marked `# Conversion: of <ROW>` (Rule 1), and states no
      after  | precision of its own.

ok  skills/provenance-discipline/references/figures.md   rule 8: the widening is built (L-390)
      before | The widening is built with the
      before | patch that retires the store's conversion rows (L-345, D20), because
      before | until then those rows declare counts the widened check would refuse.

      after  | The widening was built with
      after  | patch D20 (L-345), which retired the store's conversion rows. Since
      after  | then a marked conversion (Rule 1) is checked by
      after  | `constants_rows.conversion_problem()` and listed by name with its
      after  | source; a wrong one is CONVERSION WRONG, which fails, and a row shaped
      after  | like a conversion and not marked is UNMARKED CONVERSION, a named gap
      after  | that fails inside a closed slice (v2.27, L-390).

ok  skills/provenance-cross-check/SKILL.md               pointer: Worksheet Types is in the reference file
      before |    being checked, and specifies the job type (see Worksheet Types below).

      after  |    being checked, and specifies the job type (see Worksheet Types, in
      after  |    `references/worksheets.md`).

ok  skills/provenance-cross-check/SKILL.md               pointer: Model Roles is in the reference file
      before |    tier decides what the return is worth -- see the roster note under
      before |    Model Roles -- so a return that does not name it cannot be scored.

      after  |    tier decides what the return is worth -- see the roster note under
      after  |    Model Roles, in `references/worksheets.md` -- so a return that does
      after  |    not name it cannot be scored.

ok  skills/provenance-cross-check/SKILL.md               the checker's four outcomes beside the send-back rule (L-252)
      before | something it did not say at the time.
      before | 
      before | #### A Complete Row That Disagrees Is a Finding [CRITICAL]

      after  | something it did not say at the time.
      after  | 
      after  | **What the checker reports is a different list** (L-252, Tony,
      after  | 2026-10-08). `worksheet_checker.py` compares the code against a
      after  | worksheet and reports one of four outcomes. They are the checker's
      after  | words, not worksheet tokens, and never belong in a verdict cell.
      after  | 
      after  | - DRIFTED -- the worksheet confirmed a value and the code left it, or
      after  |   called it APPROX or PARTIAL and the code moved somewhere the
      after  |   worksheet never named. The only defect of the four; routed to
      after  |   conversation.
      after  | - CORRECTED -- the worksheet rejected the value and the code moved.
      after  |   Recorded, not routed.
      after  | - COMPLETED -- the worksheet called it APPROX or PARTIAL and supplied a
      after  |   value, and the code now reads exactly that value. Recorded, not
      after  |   routed.
      after  | - UNCHECKED_MOVE -- the code moved and the worksheet established
      after  |   nothing about the value. Routed, because nobody has established
      after  |   anything. Two different cases reach it, and the checker's line says
      after  |   which:
      after  |   - NO VALUE VERDICT -- the worksheet checked only the citation, or the
      after  |     value cell is blank, holds a word outside the vocabulary, or holds
      after  |     DERIVED, which answers the citation question and not this one.
      after  |   - UNVERIFIED -- a checker looked at the value and stopped before
      after  |     finishing. The line prints it as ABSENT, the checker's internal
      after  |     name for that token.
      after  | 
      after  | COMPLETED says only that the code took the value the worksheet
      after  | supplied. It is not a confirmation. The row is still APPROX or
      after  | PARTIAL, it earns no leg toward the cross-checked rung, and the
      after  | send-back rule above is unchanged.
      after  | 
      after  | #### A Complete Row That Disagrees Is a Finding [CRITICAL]

ok  skills/provenance-cross-check/references/worksheets.md pointer: The Read Field is in provenance-discipline
      before | (The Read Field,
      before | above).

      after  | (The Read Field,
      after  | in provenance-discipline).

ok  skills/provenance-cross-check/references/worksheets.md pointer: Route the Effort Tier is in SKILL.md
      before | They ask different questions, they fail differently, and per Route the
      before | Effort Tier by Job Type below they are not worth the same effort tier.

      after  | They ask different questions, they fail differently, and per Route the
      after  | Effort Tier by Job Type, in the skill's SKILL.md, they are not worth
      after  | the same effort tier.

ok  skills/ledger-and-session-records/SKILL.md           read plan seed, and the 1.18 entry
      before | # Ledger and Session Records
      before | 
      before | Skill version: 1.17 | 2026-10-07, with Anthropic's Claude Fable 5.1, at

      after  | # Ledger and Session Records
      after  | 
      after  | Read this file in parts.
      after  | 
      after  | Skill version: 1.18 | 2026-10-08, with Anthropic's Claude Opus 5.5, at
      after  | palomas_orrery @ b0b3df82. v1.18 (L-418) records two conventions the
      after  | provenance-discipline split brought in, under A skill keeps three
      after  | version entries: a file longer than one read opens with a read plan
      after  | that skills_index.py writes, and a skill's extra files live in its
      after  | references folder, each named in its SKILL.md. The Anchor Requirement
      after  | names provenance-cross-check for a review prompt carried to another
      after  | model.
      after  | Earlier: 1.17 | 2026-10-07, with Anthropic's Claude Fable 5.1, at

ok  skills/ledger-and-session-records/SKILL.md           v1.15 entry out to SKILL_HISTORIES.md (three-entry rule)
      before | Earlier: 1.15 | 2026-10-05, with Anthropic's Claude Opus 5.5, at
      before | palomas_orrery @ 72e3b558. v1.15 (L-418) adds one paragraph under the change log, A skill
      before | keeps three version entries, which writes down what this version does
      before | to all six long skills. A contents list now opens the skill, generated from its headings, and
      before | skills_index.py --check fails if the two disagree. Version history
      before | older than the two entries below moved to
      before | documentation/SKILL_HISTORIES.md. Both because a plain read of a
      before | long file shows its start and end and leaves out its middle, where
      before | the rules are (Tony, 2026-10-05).
      before | Older entries are in documentation/SKILL_HISTORIES.md, moved there
      before | on 2026-10-05 (L-418) and 2026-10-07 (L-422).

      after  | Older entries are in documentation/SKILL_HISTORIES.md, moved there
      after  | on 2026-10-05 (L-418), 2026-10-07 (L-422) and 2026-10-08 (L-418).

ok  skills/ledger-and-session-records/SKILL.md           anchor requirement: a review prompt needs provenance-cross-check
      before | Load it by name": a provenance review needs provenance-discipline, a
      before | patch needs safe-file-editing, and sending all ten teaches the partner
      before | to skim.

      after  | Load it by name": a provenance review needs provenance-discipline, a
      after  | review prompt carried to another model needs provenance-cross-check
      after  | beside it, a patch needs safe-file-editing, and sending them all
      after  | teaches the partner to skim.

ok  skills/ledger-and-session-records/SKILL.md           three version entries: the read plan and reference files
      before | the list in the same edit. Both for one reason: a plain read of a long
      before | file shows its start and end and leaves out its middle, so what opens
      before | a skill is the one part every session is sure to see.

      after  | the list in the same edit. A file longer than one read -- 16,000
      after  | characters or 2,000 lines, the smaller of the two readers measured --
      after  | opens, just under its title, with a READ PLAN naming the line ranges
      after  | to read it in, one read each (v1.18, L-418). A patch puts the seed
      after  | line there, `Read this file in parts.`, and `skills_index.py` writes
      after  | the plan; `--check` fails on a long file with none, a part over one
      after  | read, or a line no part covers. A long skill still waiting for its
      after  | plan is named on the list `PLAN_NOT_YET` in `skills_index.py`, which
      after  | every run prints; it gets the plan at its next version, and comes off
      after  | the list in the same patch. A skill's extra files live in its
      after  | `references/` folder, each named in its SKILL.md with the moment to
      after  | open it; `--check` fails on one named and missing, or present and
      after  | never named. All of this for one reason: a plain read of a long file
      after  | shows only part of it -- its start and end in one reader, its start
      after  | alone in another -- so what opens a skill is the one part every
      after  | session is sure to see.

ok  final check: every section is its original plus the listed edits and nothing else. Of 23 edits, 19 fell inside a section of provenance-discipline 2.26, 0 in text this patch adds, and 4 in ledger-and-session-records

ok  documentation/SKILL_HISTORIES.md                     provenance-discipline: v2.24 entry and the withdrawn rule
ok  documentation/SKILL_HISTORIES.md                     ledger-and-session-records: v1.15 entry
ok  skills_index.py                                      read plan and reference checks, edit 1 of 11
ok  skills_index.py                                      read plan and reference checks, edit 2 of 11
ok  skills_index.py                                      read plan and reference checks, edit 3 of 11
ok  skills_index.py                                      read plan and reference checks, edit 4 of 11
ok  skills_index.py                                      read plan and reference checks, edit 5 of 11
ok  skills_index.py                                      read plan and reference checks, edit 6 of 11
ok  skills_index.py                                      read plan and reference checks, edit 7 of 11
ok  skills_index.py                                      read plan and reference checks, edit 8 of 11
ok  skills_index.py                                      read plan and reference checks, edit 9 of 11
ok  skills_index.py                                      read plan and reference checks, edit 10 of 11
ok  skills_index.py                                      read plan and reference checks, edit 11 of 11
ok  PROJECT_INSTRUCTIONS.md                              header stamp v3.86
ok  PROJECT_INSTRUCTIONS.md                              SHA anchor
ok  PROJECT_INSTRUCTIONS.md                              v3.86 entry
ok  PROJECT_INSTRUCTIONS.md                              v3.83 out (34 lines)
ok  documentation/PROJECT_INSTRUCTIONS_HISTORY.md        v3.83 in, at the end of PART 1

ok  LEDGER_CONSOLIDATED.md                               L-418: the build recorded; Gap rewritten
ok  LEDGER_CONSOLIDATED.md                               L-418: metadata, date
ok  LEDGER_CONSOLIDATED.md                               L-424: opened, the checker's one word for two cases
ok  LEDGER_CONSOLIDATED.md                               L-390: landed; Gap none
ok  LEDGER_CONSOLIDATED.md                               L-390: metadata -> DONE, section C
ok  LEDGER_CONSOLIDATED.md                               L-371: the two skill sentences landed
ok  LEDGER_CONSOLIDATED.md                               L-371: metadata, date
ok  LEDGER_CONSOLIDATED.md                               L-351: provenance-discipline: what landed at 2.27
ok  LEDGER_CONSOLIDATED.md                               L-351: ledger-and-session-records: 1.18 landed
ok  LEDGER_CONSOLIDATED.md                               L-351: the four long skills owe a read plan
ok  LEDGER_CONSOLIDATED.md                               L-351: metadata, date
ok  LEDGER_CONSOLIDATED.md                               header stamp
ok  documentation/WHERE_WE_ARE.md                        header date
ok  documentation/WHERE_WE_ARE.md                        box: changed since you last read this (added above the other session's lines)
ok  documentation/WHERE_WE_ARE.md                        box: needs you now
ok  documentation/WHERE_WE_ARE.md                        settled: two rulings
ok  documentation/WHERE_WE_ARE.md                        signals: who owes the gate-path count
ok  documentation/WHERE_WE_ARE.md                        where the details are: the split
ok  documentation/HANDOFF_L418_split_build_20261008.md   the session's handoff (new)

patch applied: 13 files written:
  skills/provenance-discipline/SKILL.md
  skills/provenance-discipline/references/figures.md
  skills/provenance-discipline/references/field-notes.md
  skills/provenance-cross-check/SKILL.md
  skills/provenance-cross-check/references/worksheets.md
  skills/ledger-and-session-records/SKILL.md
  documentation/SKILL_HISTORIES.md
  skills_index.py
  PROJECT_INSTRUCTIONS.md
  documentation/PROJECT_INSTRUCTIONS_HISTORY.md
  LEDGER_CONSOLIDATED.md
  documentation/WHERE_WE_ARE.md
  documentation/HANDOFF_L418_split_build_20261008.md

skills_index.py -- writes the read plans and the manifest:

Read plan written: ledger-and-session-records/SKILL.md: Read this file in 3 parts: lines 1-224, 225-500, 501-677.
Read plan written: provenance-cross-check/SKILL.md: Read this file in 2 parts: lines 1-287, 288-566.
Read plan written: provenance-discipline/SKILL.md: Read this file in 5 parts: lines 1-303, 304-601, 602-904, 905-1201, 1202-1255.
Read plan written: provenance-discipline/references/figures.md: Read this file in 3 parts: lines 1-261, 262-514, 515-569.
Headers: 12 read as YAML by PyYAML.
CONSISTENCY PROBLEMS:
  - orrery-coding-conventions: SKILL.md.bak sits in the skill folder; only SKILL.md and references/ may
  - safe-file-editing: SKILL.md.bak sits in the skill folder; only SKILL.md and references/ may
Read plans checked (4): ledger-and-session-records/SKILL.md 3 parts, provenance-cross-check/SKILL.md 2 parts, provenance-discipline/SKILL.md 5 parts, provenance-discipline/references/figures.md 3 parts.
Long skills with no read plan yet, by PLAN_NOT_YET (4): gallery-cache-builder, interactive-exhibit, orrery-coding-conventions, safe-file-editing.
  WARNING: gallery-cache-builder: long and no read plan yet; on PLAN_NOT_YET, so it gets one at its next version
  WARNING: interactive-exhibit: SKILL.md body is 770 lines; Anthropic's guideline is under 500
  WARNING: interactive-exhibit: long and no read plan yet; on PLAN_NOT_YET, so it gets one at its next version
  WARNING: ledger-and-session-records: SKILL.md body is 672 lines; Anthropic's guideline is under 500
  WARNING: orrery-coding-conventions: SKILL.md body is 650 lines; Anthropic's guideline is under 500
  WARNING: orrery-coding-conventions: long and no read plan yet; on PLAN_NOT_YET, so it gets one at its next version
  WARNING: provenance-cross-check: SKILL.md body is 561 lines; Anthropic's guideline is under 500
  WARNING: provenance-discipline: SKILL.md body is 1250 lines; Anthropic's guideline is under 500
  WARNING: safe-file-editing: SKILL.md body is 714 lines; Anthropic's guideline is under 500
  WARNING: safe-file-editing: long and no read plan yet; on PLAN_NOT_YET, so it gets one at its next version
MANIFEST WAS STALE -- corrected below:
  - ledger-and-session-records: manifest said 1.17, SKILL.md says 1.18
  - provenance-discipline: manifest said 2.26, SKILL.md says 2.27
  - provenance-cross-check: missing from the manifest entirely
  Commit the protocol copies together with the SKILL.md
  change -- see the binding rule in ledger-and-session-records.
Skill Manifest regenerated (12 skills) in PROJECT_INSTRUCTIONS.md.

skills_index.py --check:

Headers: 12 read as YAML by PyYAML.
CONSISTENCY PROBLEMS:
  - orrery-coding-conventions: SKILL.md.bak sits in the skill folder; only SKILL.md and references/ may
  - safe-file-editing: SKILL.md.bak sits in the skill folder; only SKILL.md and references/ may
Read plans checked (4): ledger-and-session-records/SKILL.md 3 parts, provenance-cross-check/SKILL.md 2 parts, provenance-discipline/SKILL.md 5 parts, provenance-discipline/references/figures.md 3 parts.
Long skills with no read plan yet, by PLAN_NOT_YET (4): gallery-cache-builder, interactive-exhibit, orrery-coding-conventions, safe-file-editing.
  WARNING: gallery-cache-builder: long and no read plan yet; on PLAN_NOT_YET, so it gets one at its next version
  WARNING: interactive-exhibit: SKILL.md body is 770 lines; Anthropic's guideline is under 500
  WARNING: interactive-exhibit: long and no read plan yet; on PLAN_NOT_YET, so it gets one at its next version
  WARNING: ledger-and-session-records: SKILL.md body is 672 lines; Anthropic's guideline is under 500
  WARNING: orrery-coding-conventions: SKILL.md body is 650 lines; Anthropic's guideline is under 500
  WARNING: orrery-coding-conventions: long and no read plan yet; on PLAN_NOT_YET, so it gets one at its next version
  WARNING: provenance-cross-check: SKILL.md body is 561 lines; Anthropic's guideline is under 500
  WARNING: provenance-discipline: SKILL.md body is 1250 lines; Anthropic's guideline is under 500
  WARNING: safe-file-editing: SKILL.md body is 714 lines; Anthropic's guideline is under 500
  WARNING: safe-file-editing: long and no read plan yet; on PLAN_NOT_YET, so it gets one at its next version

skills_index.py reported a problem, above. The files are written; tell Claude what it printed.
Undo is Discard Changes in GitHub Desktop.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 

The patch worked. All 13 files were written, every edit printed "ok", the final check passed, and the read plans and the 12-skill manifest were written. Only one thing made the last check fail, and it's real.

**What it found.** There are two leftover backup files on your computer:

- `skills/orrery-coding-conventions/SKILL.md.bak`
- `skills/safe-file-editing/SKILL.md.bak`

They aren't on GitHub. Your repo is set to ignore `.bak` files, so they exist only in your folder. The new check flags them because a skill's folder is exactly what you zip and install. If you zipped either of those folders, the backup would go into Settings along with the skill. This is the new check catching a real problem on its first run.

**The fix.** Delete those two files in File Explorer. Nothing is lost, because git holds every version of those skills you've committed. If you'd like to be sure first, open one and compare it with the SKILL.md beside it. -- done

**Then carry on as the patch printed:**

1. Run orrery_maintenance_run.py. "Skill headers" should now say 12 skills with no problems.

======================================================================
MAINTENANCE RUN -- generators, then checkers (L-188)
======================================================================
  Provenance scan is current (last run 20261009T012542Z, 0 day(s) ago).

GENERATORS -- regenerate every time; a no-op when nothing moved
----------------------------------------------------------------------
  Ledger index                 1.7s  rewrote LEDGER_CONSOLIDATED.md
  Skill manifest               0.2s  unchanged (1 of 1 rewritten, content
                                     identical)
  Constants export             0.9s  unchanged (1 checked, not written)
  Objects export               0.1s  unchanged (1 checked, not written)
  Module atlas                 7.0s  rewrote MODULE_ATLAS.md, MODULE_INDEX.md
  Data inventory               4.7s  unchanged (1 of 1 rewritten, content
                                     identical)
  Exact rows report            1.7s  unchanged (1 checked, not written) -- 13 of
                                     34 exact rows printed at 42 lines (32
                                     orrery, 10 gallery); 8 drawn only, 11 not
                                     followed, 0 map entries broken
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
  Constants export check       1.9s  Export matches the store: sha256
                                     3b7000e368d1 on both sides; 105 rows
                                     re-read, 56 not exported, 27 tokens; 310
                                     conversions re-computed, 10 of 10 worked
                                     cases hold.
  Objects export check         0.1s  pass
  Skill headers                0.2s  12 skills parsed, no consistency problems.
  Exact rows by the count      2.2s  PASSING -- 13 printed exact rows each state
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
  Reset completeness          12.9s  PASS -- all 310 IntVars + 3 StringVars + 10
                                     entries reset to startup defaults; date set
                                     to now.
  Orbit cache                  2.4s  All 6 orbit cache tests passed: cache loads,
                                     old formats convert, corrupted entries are
                                     dropped.
  Earth pole of date           0.3s  all 14 checks passed (geometry, ERFA,
                                     fallback, cache, hover, transform).
  Worksheet checker            9.8s  74 of 110 routed, 8 clean
  Worksheet checker tests     17.3s  All 135 checks passed
  Worksheet key round trip     1.0s  RESULT: 52 sites minted 52 distinct keys,
                                     all resolved; 52 pinned keys still resolve;
                                     1 retired keys confirmed gone.
  Builder marker join         21.2s  All 76 checks passed
  Extractor pins               0.4s  RESULT: 29 string sites carry the pinned 73
                                     claims and 14 instruction drops, at LOOKBACK
                                     30 / LOOKAHEAD 25, extractor version 2.
  Provenance scanner          10.2s  296 TIER-1 FINDINGS IN THE SCANNED TREE

======================================================================
  20 of 20 gating checkers passed -- 99.5s total
  2 report-only, exit 0 whatever they find:
    Worksheet checker           74 of 110 routed, 8 clean
    Provenance scanner          296 TIER-1 FINDINGS IN THE SCANNED TREE
======================================================================

FILES WRITTEN THIS RUN
----------------------------------------------------------------------
  2122 file(s) examined, 6 written, 0 created, 0 removed, 6 rewritten identically
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

2. Move the patch into documentation/, then commit and push. -- ea2c0e16c2955a626816b03687a82d45c588e2c0
3. Zip and install the three skills: provenance-discipline, provenance-cross-check and ledger-and-session-records.
4. Replace the Project's instructions with PROJECT_INSTRUCTIONS.md.

**Two other things in the output, both fine:**

- The new ledger item is **L-424** (the checker's one word for two cases), not L-423. The decisions session's patch ran first and took L-423, so mine picked the next free number. The page and the handoff both say L-424.
- On Where We Are, my lines went in above the decisions session's lines in the "Changed since" box, so both sessions' news is there.