<!-- Doc-Kind: hand | Handoff for a fresh session: design, then the first discovery run, of the check of the orrery's object list against JPL Horizons (L-395). -->
# Handoff: checking the object list against JPL Horizons (L-395)

Built on orrery 72e3b55805c29f1f08a583864bd815a47e7434c6 at
https://github.com/tonylquintanilla/palomas_orrery and gallery
624aa94557e16956b2fe022a467936ae2ccf3406 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io. Pushed
at: Tony's push of this session's closing patch, which carries this
file. The receiving session pulls both repos at HEAD and reads L-395
in LEDGER_CONSOLIDATED.md before anything else here.

Type: DESIGN, then DISCOVERY. Audience: a session inside this Project,
which has the protocol and the installed skills. Skills to load:
horizons-orbital-mechanics, provenance-discipline (2.26 if reinstalled),
ledger-and-session-records (1.15 if reinstalled). Written October 5,
2026, with Anthropic's Claude Opus 5.5.

## Why this, and why now

- Tony, 2026-10-05: it matters "because like our other accuracy
  disciplines this is about verification of information we are
  serving."
- The website serves eleven bodies whose identity facts are copies of
  the orrery's object list (`OBJECT_DEFINITIONS` in
  `celestial_objects.py`): the Sun, the eight planets, Pluto and
  Apophis. The copy is checked against the list (L-395's first build,
  2026-10-01). The list itself is checked against nothing.
- So the check is in scope under The Braid: it is bounded to what the
  website serves today, and it terminates.

## What is settled (Tony's rulings, on L-395)

- The orrery's object list is the one definition of each object; the
  website keeps copies written by `tools/mirror_objects.py` from
  `data/objects_export.json`, and a check fails on any difference.
- Horizons is the outside authority. The list can go stale -- legacy
  entries, the orrery's own evolution, errors -- so the check compares
  the list with Horizons, not only the website with the list (Tony,
  2026-09-29).
- Simple errors a check finds are fixed and reported; anything with a
  choice in it comes to Tony (provenance-discipline, A Simple Error a
  Check Finds Is Fixed and Reported).
- Discovery before remediation: the first run lists every disagreement
  and fixes nothing except simple errors, reported.

## What is open: the design round, in this order

1. What Horizons can confirm for an entry: that its id resolves to
   exactly one object; that object's name and designation; its kind.
   And what it cannot: the project's modelling choices, such as
   drawing Pluto about the Pluto-Charon barycentre.
2. Which fields are compared, and what counts as agreement. Apophis is
   the worked case: `2004 MN4` and `99942` name one Horizons record.
3. Where the check runs, and its cadence. It needs the network, so
   when it cannot reach Horizons it says so and never passes. It
   records the date each object was last confirmed, the way a
   constants row records who read its source, and re-confirms on a
   cadence rather than querying every object on every run.
4. Pinned records (Halley `90000030`, Encke `90000091`): flagged when
   JPL has a newer solution, for Tony to decide. Not among the eleven,
   so this may wait for stage 9; the design should say.
5. What the first run prints: every disagreement by name, the object
   and the field, with Horizons' answer beside the list's.

## One practical fact, found 2026-10-05

- This chat's sandbox cannot reach JPL: a Horizons API query was
  refused with `x-deny-reason: host_not_allowed`. So either the check
  runs on Tony's machine, like the cache builder, or Tony adds
  `ssd.jpl.nasa.gov` to the chat's allowed domains so a session can
  run the discovery pass itself. That is a (decide) for the design
  round, not before it.

## Not in scope

- The other 171 entries of the list (road stage 9), except as the
  design says the check will reach them later.
- Fields the list lacks (a moon's parent, a clean kind for comets):
  recorded on L-395, its own round.
- The numbers inside descriptions: L-403.

## Running beside the website session (Tony, 2026-10-05)

Tony asked that this design round and Earth's website patch run as two
sessions at once. The website session's handoff,
`documentation/HANDOFF_L413_earth_orrery_patch_20261005.md`, carries the
same three rules.

- DO NOT REWRITE WHERE WE ARE. The website session owns the page this
  round. Put this session's updates for the page in this session's
  handoff, under a heading saying so; the next rewrite picks them up.
- THE OPENING CHECKS ARE THE WEBSITE SESSION'S. This session reads the
  version of each skill it loads and compares it with the protocol's
  manifest, as always, but leaves closing L-369, L-418 and L-419 to the
  website session. In the ledger it edits only L-395, and any item it
  opens.
- PULL AGAIN BEFORE ANY PATCH. Both sessions start from orrery
  be67ca39. Before building a patch, re-read HEAD, build on whatever the
  website session has pushed, and name that commit. Ledger edits match
  only the lines they change (L-419), so the two sessions' ledger
  patches apply in either order.
- A design round is conversation first. Tony carries two threads; one
  question at a time.

## Tony-actions

(decide)
- At the design round: the five questions above, one at a time.
- Where the check runs: Tony's machine, or this chat with JPL allowed.

============================================================================
**Tony**: run record:

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/patch_L395_3_horizons_check_design_20261007.py
ok  LEDGER_CONSOLIDATED.md   header stamp
ok  LEDGER_CONSOLIDATED.md   L-395 date
ok  LEDGER_CONSOLIDATED.md   L-395 design round and Gap
ok  LEDGER_CONSOLIDATED.md   L-395 Ref
ok  documentation/DESIGN_L395_horizons_check_20261007.md created (336 lines)
ok  documentation/HORIZONS_ANSWERS_L395_20261007.md created (679 lines)

patch applied

NEXT:
  1. Run orrery_maintenance_run.py -- it rebuilds the ledger's index.

======================================================================
MAINTENANCE RUN -- generators, then checkers (L-188)
======================================================================
  Provenance scan is current (last run 20261007T191217Z, 0 day(s) ago).

GENERATORS -- regenerate every time; a no-op when nothing moved
----------------------------------------------------------------------
  Ledger index                 1.5s  rewrote LEDGER_CONSOLIDATED.md
  Skill manifest               0.2s  unchanged (1 of 1 rewritten, content
                                     identical)
  Constants export             0.7s  unchanged (1 checked, not written)
  Objects export               0.1s  unchanged (1 checked, not written)
  Module atlas                 6.5s  unchanged (2 of 2 rewritten, content
                                     identical)
  Data inventory               5.3s  unchanged (1 of 1 rewritten, content
                                     identical)
  Exact rows report            2.3s  unchanged (1 checked, not written) -- 13 of
                                     34 exact rows printed at 42 lines (32
                                     orrery, 10 gallery); 8 drawn only, 11 not
                                     followed, 0 map entries broken
  Document index               0.1s  unchanged (1 checked, not written)

CHECKERS -- verdict informs the push call
----------------------------------------------------------------------
  Constants change             0.3s  No changes to constants_new.py since HEAD.
  Constants relations          0.3s  25 of 25 provenance tests passed against
                                     constants_new.py. No constants have drifted.
  Derived figures              0.9s  No figure count exceeds its inputs: 36
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
  Dimensions                   1.7s  No unit contradicts its arithmetic: 54
                                     derived row(s) read -- 42 OK, 9 NO UNIT, 3
                                     NOT CHECKABLE.
  Cross-check annotations      0.2s  19 of 19 cross-check annotation tests
                                     passed.
  Citation inheritance         0.2s  20 of 20 citation-inheritance tests passed.
  Status lines                 0.1s  All 105 status lines in constants_new.py are
                                     well formed; 53 rows carry none.
  Row shape                    0.1s  All 161 row shapes in constants_new.py fit
                                     the assignment's own line.
  Scanner recognition 1d/1e    0.3s  27 of 27 recognition pins hold: real
                                     citations recognized, fake ones refused.
  Reset completeness          17.0s  PASS -- all 310 IntVars + 3 StringVars + 10
                                     entries reset to startup defaults; date set
                                     to now.
  Orbit cache                  2.2s  All 6 orbit cache tests passed: cache loads,
                                     old formats convert, corrupted entries are
                                     dropped.
  Earth pole of date           0.4s  all 14 checks passed (geometry, ERFA,
                                     fallback, cache, hover, transform).
  Worksheet checker           10.0s  74 of 110 routed, 8 clean
  Worksheet checker tests     15.3s  All 135 checks passed
  Worksheet key round trip     1.0s  RESULT: 52 sites minted 52 distinct keys,
                                     all resolved; 52 pinned keys still resolve;
                                     1 retired keys confirmed gone.
  Builder marker join         27.7s  All 76 checks passed
  Extractor pins               0.5s  RESULT: 29 string sites carry the pinned 73
                                     claims and 14 instruction drops, at LOOKBACK
                                     30 / LOOKAHEAD 25, extractor version 2.
  Provenance scanner          15.2s  296 TIER-1 FINDINGS IN THE SCANNED TREE

======================================================================
  20 of 20 gating checkers passed -- 113.3s total
  2 report-only, exit 0 whatever they find:
    Worksheet checker           74 of 110 routed, 8 clean
    Provenance scanner          296 TIER-1 FINDINGS IN THE SCANNED TREE
======================================================================

FILES WRITTEN THIS RUN
----------------------------------------------------------------------
  2093 file(s) examined, 4 written, 0 created, 0 removed, 8 rewritten identically
    written   LEDGER_CONSOLIDATED.md
    written   PROVENANCE_AUDIT.md
    written   data/provenance_history.json
    written   documentation/prompts/citation_review.jsonl
    rewritten with identical bytes, no action needed:
      DATA_INVENTORY.md
      MODULE_ATLAS.md
      MODULE_INDEX.md
      PROJECT_INSTRUCTIONS.md
      WORKSHEET_CHECK.md
      data/worksheet_check_state.json
      data/worksheet_routed.json
      test_output/test_orbit_paths.json
    20 file(s) over 2 MB compared by size and mtime only

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>

  2. Move this script into documentation/; commit and push. -- 
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 
