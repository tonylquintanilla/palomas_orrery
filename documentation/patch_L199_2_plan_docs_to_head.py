"""patch_L199_2_plan_docs_to_head.py -- planning documents to HEAD.

RUN COMMAND
-----------
Save this file into the palomas_orrery repo root (the same folder as
LEDGER_CONSOLIDATED.md), open it in VS Code, and click Run.

    python patch_L199_2_plan_docs_to_head.py

Success prints one `ok` line per file and then `patch applied`. Failure
prints a single ERROR or ANCHOR FAIL line and writes NOTHING.

INDEPENDENT OF patch_L199_1_records_reconcile.py. That one edits the
protocol, the ledger and the lessons file; this one edits four
documents in documentation/. No file is touched by both, so they run in
either order. Prefer running the records patch FIRST, because two
sentences here state the protocol is at v3.41 and provenance-discipline
at 2.4, which that patch is what makes true.

WHAT IT DOES
------------
All four documents were written or last updated on 2026-08-16 and
anchored at 227f5b2d. Nine commits later, they have NOT drifted
equally, and the corrections are sized accordingly.

  CRITICAL_PATH_SUMMARY.md          four numbers and the anchor.
                                    Structurally sound; do not rewrite.
  TESTING_PROTOCOL.md               Layer 3 still tells a reader to
                                    enable a schedule retired on
                                    2026-08-10.
  MASTER_PLAN_INTERACTIVE_GALLERY_SUMMARY.md
                                    the real work. It is the "what is
                                    tracked right now" document, and
                                    right now moved.
  MASTER_PLAN_INTERACTIVE_GALLERY.md
                                    the you-are-here table and the
                                    anchor. The design itself has not
                                    changed.

THE NUMBER THAT NEEDS EXPLAINING, NOT JUST CORRECTING
-----------------------------------------------------
The summary reports Tier 1 = 206, measured twice and unchanged.
Measured at HEAD it is 289. The document's own argument says this
should not happen -- it explains the earlier stability by saying
nothing "added or removed a claim about the world."

Both are right. The POPULATION changed, not the world: L-198 taught the
scanner units it could not previously read, so claims that were always
there became visible and countable. The correction says so, because a
reader who remembers 206 and meets 289 will otherwise read it as
regression.

SUPERSEDED LINES ARE BRACKETED, NOT DELETED
-------------------------------------------
The summary already carries the right pattern: a bracketed note reading
"[Both since done ... Left as written because it is the record of what
was true then]". This patch uses it wherever a claim was TRUE when
written and has since been overtaken, and edits in place only where the
text was wrong rather than overtaken. A snapshot that silently
overwrites its own history stops being evidence of anything.

WHAT IS PERMANENT AND WHAT IS NOT
---------------------------------
This script is disposable and one-shot. Permanent: the corrections.

AFTER RUNNING
-------------
1. Read CRITICAL_PATH_SUMMARY.md end to end -- it is short, and it is
   the document most likely to be read by somebody outside the work.
2. Archive this script to documentation/.

Module created: August 18, 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys


ANCHOR_SHA = 'b65ac115fc0f820e8270c0807249813c67bde7bc'
GALLERY_SHA = 'ff18d3e6fa31f70a8f525df471e751d046cf14fa'

DOC = 'documentation'

FINGERPRINTS = {
    os.path.join(DOC, 'CRITICAL_PATH_SUMMARY.md'):
        '38f1f3251caad8d14f4c293e1b6c14d9',
    os.path.join(DOC, 'TESTING_PROTOCOL.md'):
        'fcd395c1ea27f2d2bdb2e9bd871fd815',
    os.path.join(DOC, 'MASTER_PLAN_INTERACTIVE_GALLERY_SUMMARY.md'):
        '102797977b4cb39c9023c0e563b4933c',
    os.path.join(DOC, 'MASTER_PLAN_INTERACTIVE_GALLERY.md'):
        '05ca20c29148b9ee8e9265ba395d5a6f',
}


# ============================================================
# 1. CRITICAL_PATH_SUMMARY.md
# ============================================================

CPS_EDITS = [
    ("""**August 16, 2026.** Orrery at `227f5b2d6763baa384c090a911c2c5ced64f4a4d`,
gallery at `3d10739b097e2b63395cf58742873cf378210e68`. Both confirmed by
live check.""",
     """**Updated August 18, 2026.** Orrery at
`b65ac115fc0f820e8270c0807249813c67bde7bc`, gallery at
`ff18d3e6fa31f70a8f525df471e751d046cf14fa`. Both confirmed by live
check. First written August 16 at `227f5b2d`; the structure below is
unchanged from that version and only the measured figures moved."""),

    ("""The checker, the worksheet builder and the dispatch loop are the
machinery of this step, not a step of their own. They exist because
reconciling worksheets against the code by hand does not scale, and the
scale is now measured: 102 claims scored, three of them clean.""",
     """The checker, the worksheet builder and the dispatch loop are the
machinery of this step, not a step of their own. They exist because
reconciling worksheets against the code by hand does not scale, and the
scale is measured: 110 claims scored, eight of them clean.

As of August 18 that machinery is FINISHED and unused. A request can be
built for a chosen slice of rows, carried out as JSON, returned,
checked, routed, and written back into the code as an annotation the
scanner accepts. The last inch closed on August 18: until then a
returned verdict could be checked and routed and then refused when
somebody tried to cite it, because the annotation grammar accepted only
a markdown reference. What has not happened is the first dispatch."""),

    ("""**Step one is in progress and the backlog is now visible.** Of 102
verification claims, three are clean, forty need to go back to whoever
filled them in, nineteen need a conversation, and forty are recorded
without a route. That is not a discouraging result -- it is the first
time the number has been knowable at all. Before the checker existed,
the same 102 claims were unexamined and looked fine.""",
     """**Step one is in progress and the backlog is now visible.** Of 110
verification claims, eight are clean, forty-eight need to go back to
whoever filled them in, twenty need a conversation, thirty-four are
noted without a route, and twenty-four are not reachable by the scanner
at all. That is not a discouraging result -- it is the first time the
number has been knowable. Before the checker existed, the same claims
were unexamined and looked fine.

The corpus grew from 102 and the clean count nearly tripled. Neither is
a change in the world: L-198 taught the scanner to read units it could
not previously see, so claims that were always there entered the corpus
and rows that had been mis-parsed resolved."""),

    ("""An independent review by two models in August found nine structural
problems in the dispatch machinery before a single questionnaire went
out. Both reviewers, working blind, said do not send it yet. One of the
nine has since been closed by a design decision that removed the
question rather than answering it.""",
     """An independent review by two models in August found nine structural
problems in the dispatch machinery before a single questionnaire went
out. Both reviewers, working blind, said do not send it yet. Eight are
now closed -- the first of them by a design decision that removed the
question rather than answering it. The ninth, a truncated ordinal
context window, is deliberately not exercised by the pilot, because
constants carry no ordinals and shipping a known-defective presentation
into the first dispatch would confound the thing being tested."""),

    ("""*Prepared August 16, 2026 with Anthropic's Claude Opus 5. Built on
`227f5b2d6763baa384c090a911c2c5ced64f4a4d` at
https://github.com/tonylquintanilla/palomas_orrery, gallery at
`3d10739b097e2b63395cf58742873cf378210e68`.*""",
     """*Prepared August 16, 2026 with Anthropic's Claude Opus 5; figures
updated August 18. Built on
`b65ac115fc0f820e8270c0807249813c67bde7bc` at
https://github.com/tonylquintanilla/palomas_orrery, gallery at
`ff18d3e6fa31f70a8f525df471e751d046cf14fa`.*"""),
]


# ============================================================
# 2. TESTING_PROTOCOL.md
# ============================================================

TP_EDITS = [
    ("""## Layer 3 -- Schedule

Only after Layers 1-2 pass on the tranche: enable the nightly Task Scheduler job
(working dir = repo root). Watch the first unattended runs; a nonzero exit
(A-2) now surfaces in Task Scheduler history. Backup discipline (L-106) stays in
force: the git history + off-site copy are the archive's rollback of last resort.""",
     """## Layer 3 -- Schedule (RETIRED 2026-08-10)

**Do not enable the schedule.** Tony retired it on 2026-08-10. The
Windows task is DISABLED, not deleted, so the corrected configuration
survives if this is ever revisited. The builder now runs MANUALLY and
Tony commits the result himself.

His reasoning: the build cannot run without his machine on anyway, so
the schedule created an appearance of automation the setup could not
deliver -- three nights were missed in one week and the failure was
silent. A manual run is honest about what it is. It also dissolves the
2026-08-10 gallery incident: somebody who starts the build himself
knows a build is in flight and cannot walk into the swap window
unaware.

What the retirement does NOT dissolve is the cadence question, which
changes shape rather than going away. "Did the nightly run?" becomes
"when did I last run it?", and something still has to say the served
data is eleven days old. That is L-189, and the retirement makes it
more load-bearing, not less, because a manual build has no expected
time at all.

Backup discipline (L-106) stays in force either way: the git history
plus the off-site copy are the archive's rollback of last resort.

This section previously carried the opposite instruction, gated on
Layers 1-2 passing. It was correct when written and was overtaken by
the ruling above. It is REPLACED rather than bracketed, and the old
wording is deliberately not quoted here: a testing protocol is read at
the moment of DOING the thing it describes, and a superseded
instruction left sitting in one -- even inside quotation marks -- is an
instruction somebody follows."""),
]


# ============================================================
# 3. MASTER_PLAN_INTERACTIVE_GALLERY_SUMMARY.md
# ============================================================

MPS_EDITS = [
    # -- header
    ("""Where we are 8/16/2026

Updated 2026-08-16 after the August 15-16 sessions. Built on
227f5b2d6763baa384c090a911c2c5ced64f4a4d at
https://github.com/tonylquintanilla/palomas_orrery (branch main);
gallery at 3d10739b097e2b63395cf58742873cf378210e68 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Both confirmed by live check on the date above.""",
     """Where we are 8/18/2026

Updated 2026-08-18 after the August 17-18 sessions. Built on
b65ac115fc0f820e8270c0807249813c67bde7bc at
https://github.com/tonylquintanilla/palomas_orrery (branch main);
gallery at ff18d3e6fa31f70a8f525df471e751d046cf14fa at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Both confirmed by live check on the date above.

Where a claim was TRUE when written and has since been overtaken, it is
left in place with a bracketed note rather than deleted. This document
is a record of what was tracked on a date, and one that silently
rewrites its own past stops being evidence of anything."""),

    # -- the short version
    ("""What the checker reports is the number that now organizes Track 1:
102 annotations scored, THREE clean. Forty route to SEND BACK,
nineteen to CONVERSATION, forty are noted with no route. That is not
a discouraging result. Before the checker existed the same 102 claims
were unexamined and looked fine.

The dispatch that clears them is repaired but not finished. Fable 5
and GPT 5.6 Sol reviewed it blind on August 16; both said do not send
it yet, and between them they found nine structural blockers where
two were known. One is closed, three are ruled and unbuilt, three are
open, two need no ruling.""",
     """What the checker reports is the number that organizes Track 1:
110 annotations scored, EIGHT clean. Forty-eight route to SEND BACK,
twenty to CONVERSATION, thirty-four are noted with no route, and
twenty-four are not scanner-reachable. That is not a discouraging
result. Before the checker existed the same claims were unexamined and
looked fine.

  [Read 2026-08-16 as: 102 scored, THREE clean, 40 SEND BACK, 19
  CONVERSATION, 40 noted. The corpus grew and the clean count nearly
  tripled between the 16th and the 18th, and neither is a change in
  the world -- L-198 taught the scanner units it could not read, so
  claims that were always there became visible and rows that had been
  mis-parsed resolved.]

The dispatch loop is FINISHED and unused. Fable 5 and GPT 5.6 Sol
reviewed it blind on August 16; both said do not send it yet, and
between them found nine structural blockers where two were known.
Eight are closed. The ninth -- the truncated ordinal context window --
is deliberately not exercised by the pilot, since constants carry no
ordinals.

The last inch closed on August 18. Until then a returned verdict could
be built, carried, filled, returned, checked and routed, and then
REFUSED when somebody wrote it back into the code, because the
annotation grammar accepted only a markdown reference (L-204). Found by
an integration test, not by reading the code."""),

    # -- the marker-join paragraph
    ("""The next session opens with the builder-side marker join. Ninety-six
continuation markers were placed in seven files on August 16 and the
builder does not yet know they exist, so the largest blocker -- 45 of
65 dispatch rows showing a truncated citation -- is still live.""",
     """  [2026-08-16 read: "The next session opens with the builder-side
  marker join. Ninety-six continuation markers were placed in seven
  files on August 16 and the builder does not yet know they exist, so
  the largest blocker -- 45 of 65 dispatch rows showing a truncated
  citation -- is still live." DONE, L-196. The builder joins 153
  continuations on every build and refuses to build at all when a
  citation continues onto an unmarked line.]

What opens the next session is the DISPATCH. The request is one file,
reader-agnostic, 23 rows over constants_new.py, with every row's
expected disposition written down before it goes out
(PILOT_EXPECTED_DISPOSITIONS_20260817.md: 13 clear, 10 return, three
trap rows). If all 23 come back clear, that is agreement rather than
success, and the prediction file is what makes the difference
visible."""),

    # -- the skill obligation
    ("""     CURRENTLY OUTSTANDING: safe-file-editing and
     orrery-coding-conventions both went 1.3 -> 1.4 on August 16. The
     session that bumped them loaded 1.3. The next session must
     confirm its loaded copies read 1.4 before any patch-script or
     marker work.""",
     """     CURRENTLY OUTSTANDING: provenance-discipline went 2.3 -> 2.4 on
     August 18. The session that bumped it loaded 2.3. The next
     session must confirm its loaded copy reads 2.4 before any
     provenance work.

     [The August 16 obligation -- safe-file-editing and
     orrery-coding-conventions at 1.3 -> 1.4 -- was discharged
     2026-08-17. All ten skills were compared loaded-against-repo on
     August 18 and only provenance-discipline differs.]"""),

    # -- scanner state
    ("""The tier breakdown below was measured at 1ba20c3 on August 7: 879
findings across 117 files, Tier 1 206, Tier 2 583, Tier 3 88, Tier 4 2.
Tier 1 was re-measured at 227f5b2 on August 16 and is UNCHANGED at 206
-- the chromosphere retirement and the continuation markers moved
nothing, which is correct, since neither added or removed a claim about
the world.

  Tier 1 by domain

    Earth System                105
    Orrery                       91
    Stars                         9
    Utilities                     1
    Dev Tools                     0
    Gallery                       0""",
     """Measured at b65ac115 on August 18: 1025 findings across 128 files,
Tier 1 289, Tier 2 620, Tier 3 114, Tier 4 2.

  [August 7 at 1ba20c3: 879 findings across 117 files, Tier 1 206,
  Tier 2 583, Tier 3 88, Tier 4 2. Re-measured at 227f5b2 on August 16
  and UNCHANGED at 206 -- the chromosphere retirement and the
  continuation markers moved nothing, which was correct, since neither
  added nor removed a claim about the world.]

Tier 1 went 206 -> 289 in two days, and the paragraph above says that
should not happen. Both are right, and the reconciliation is the point
worth keeping: the POPULATION changed, not the world. L-198 taught the
scanner claim vocabulary it did not have -- per-body radii, spelled-out
kilometres, units separated from their number by an intervening word --
so claims that had always been in the code became visible and
countable. A scanner that sees more is not a codebase that got worse.
Read 289 against 206 as coverage, not regression.

  Tier 1 by domain, at b65ac115

    Earth System                150
    Orrery                      125
    Stars                        12
    Utilities                     2
    Dev Tools                     0
    Gallery                       0"""),

    # -- artifact-2 per-file table
    ("""  shell_configs.py                      23
  idealized_orbits.py                   26
  planet_visualization_utilities.py      4
  saturn_visualization_shells.py         1
  uranus_visualization_shells.py         1
  orrery_rendering.py                    1
  jupiter_visualization_shells.py        0
  neptune_visualization_shells.py        0
                                        --
                                        56""",
     """  shell_configs.py                      35
  idealized_orbits.py                   29
  planet_visualization_utilities.py      4
  saturn_visualization_shells.py         1
  uranus_visualization_shells.py         1
  orrery_rendering.py                    1
  jupiter_visualization_shells.py        0
  neptune_visualization_shells.py        0
                                        --
                                        71

  [August 16: 23, 26, and a total of 56. The two that moved are the
  L-198 vocabulary effect again, not new debt.]"""),

    # -- ledger items by track, Track 1 block
    ("""  Track 1     L-186  Cross-check annotation issues  DONE
              L-192  Worksheet checker  BUILT and running as one of
                     the twelve maintenance checkers. Request builder
                     built. Key rule built. DISPATCH not finished --
                     see the nine blockers.""",
     """  Track 1     L-186  Cross-check annotation issues  DONE
              L-192  Worksheet checker  BUILT and running as one of
                     the maintenance checkers. Request builder built.
                     Key rule built. DISPATCH machinery now complete;
                     eight of nine blockers closed, the ninth
                     deliberately unexercised by the pilot.
              L-196  Citation continuations: mark, join, refuse  DONE
              L-197  Maintenance runner output: say what passed  DONE
              L-198  Claim vocabulary: the units the scanner could
                     not see  DONE -- and the reason Tier 1 moved
                     206 -> 289
              L-200  The Resolved leg -- record a verdict that
                     landed  DONE
              L-201  Request selection -- ask the builder for fewer
                     rows  DONE; also a dashboard card
              L-202  JSON worksheet format, markdown as fallback  DONE
              L-203  The visibility convention, now in the skill  DONE
              L-204  The worksheet reference may be JSON  DONE -- the
                     last inch of the loop
              L-205  The runner's verdict lines carry evidence  DONE"""),

    # -- already resolved: protocol and skill versions
    ("""Protocol at v3.40 (August 16) -- no change to its own rules; the entry
records two skill bumps and the two bad deliveries that preceded the
good ones. safe-file-editing 1.4 adds Fix In Passing, Report It and the
patch-script naming convention. orrery-coding-conventions 1.4 adds
Marker Separation for Near-Equal Radii and Harvest the Conventions You
Find. The v3.36 Register Rule amendment is applied, and
so is \"The Artifact Bounds the Audit\" (v3.37). v3.38 records the two
limits on Stale Skill = Stop. v3.39 adds \"A Check That Cannot Fail Is
Not Passing\" as a CRITICAL gate. provenance-discipline is at v2.3.""",
     """Protocol at v3.41 (August 18) -- a records restructure and a skill
bump, no rule changed. The version history left the protocol document
for documentation/PROJECT_INSTRUCTIONS_HISTORY.md, which is
LESSONS_ARCHIVE.md renamed and now carries both records; the ledger's
appendix became a pointer; three entries stay resident and a fourth
pushes the oldest down. The header gained an anchor and lost a
contradiction -- the repo copy read August 16 and the copy installed in
the Claude UI read August 17 under the same version.
provenance-discipline is at v2.4.

  [August 16 read: protocol at v3.40, provenance-discipline at v2.3.
  v3.40's own entry records two skill bumps and the two bad deliveries
  that preceded the good ones -- safe-file-editing 1.4 adding Fix In
  Passing, Report It and the patch-script naming convention, and
  orrery-coding-conventions 1.4 adding Marker Separation for
  Near-Equal Radii and Harvest the Conventions You Find. v3.36's
  Register Rule amendment, v3.37's \"The Artifact Bounds the Audit\",
  v3.38's two limits on Stale Skill = Stop and v3.39's \"A Check That
  Cannot Fail Is Not Passing\" all remain in force.]"""),

    # -- the four nightly-live sites
    ("""Phases 0, 1a and 1b are all closed. Layer 3, the nightly Task Scheduler
job, is RETIRED as of August 10 -- disabled, not deleted. Several
documents still describe it as live: MASTER_PLAN_INTERACTIVE_GALLERY.md
line 40, documentation/TESTING_PROTOCOL.md line 292, the
gallery-cache-builder skill line 70, and the deployment-model decision
block in the ledger near line 4555.""",
     """Phases 0, 1a and 1b are all closed. Layer 3, the nightly Task Scheduler
job, is RETIRED as of August 10 -- disabled, not deleted.

The four documents that described it as live were re-checked on August
18, and the list itself had gone stale.
MASTER_PLAN_INTERACTIVE_GALLERY.md line 40 was ALREADY corrected and
states the retirement with its reasoning. TESTING_PROTOCOL.md Layer 3
was still telling a reader to enable the schedule and is corrected in
the same patch as this note -- it mattered more than the others,
because a testing protocol is read at the moment of doing the thing it
describes. The gallery-cache-builder skill and the ledger's
deployment-model block still need a look; the line numbers recorded
here have moved and are not worth trusting.

That a to-do list about staleness went stale is the ordinary case, not
an irony. It is why the entries above carry what was measured and when
rather than a line number."""),

    # -- what is tracked right now
    ("""WHAT IS TRACKED RIGHT NOW -- 2026-08-16

  Ready to build, no ruling outstanding
    Builder marker join + loud failure  <- do this first; 96 markers
      are placed and currently do nothing
    Stage 2 continuation markers -- 117 runs, 23 files, fingerprints
      to be regenerated against 227f5b2
    Six Shape A citation swaps (L-195)
    Ordinal context window -- 26 rows share 8 excerpts today
    Print the seven verdict tokens in the request
    Resolver + models fix (L-154) -- independent of all provenance work

  Waiting on a ruling
    Lazy responder: canaries, or remove the self-certifying field
    Claim typing: real row types, or wait for a measured population
    Cross-worksheet disagreement, what UNKNOWN does, pluto 614/638,
      transition sequencing, whether batching becomes real

  Carried as an obligation
    Confirm safe-file-editing and orrery-coding-conventions load at
      1.4 before patch-script or marker work

  Not yet written
    Ledger entries for L-194, L-195, L-196 and the L-192 as-built""",
     """WHAT IS TRACKED RIGHT NOW -- 2026-08-18

  Unstarted and unblocked
    The pilot dispatch. 23 rows over constants_new.py, request built
      by selection 2, sent as JSON with markdown as the fallback,
      expected dispositions written before it goes out.

  Ready to build, no ruling outstanding
    Resolver + models fix (L-154) -- two lines and a type, then the
      renderers. Independent of every provenance question, and now the
      only item on this list. It is the smallest piece of work between
      the project and a Saturn that renders.
    Ordinal context window (blocker 7) -- 26 rows share 8 excerpts.
      Not exercised by the pilot on purpose.

  Waiting on a ruling
    Lazy responder: canaries, or remove the self-certifying field
    Claim typing: real row types, or wait for a measured population
    Cross-worksheet disagreement, what UNKNOWN does, pluto 614/638,
      transition sequencing, whether batching becomes real
    The Resolved leg's first token: shipped as the worksheet FILENAME,
      where the design wrote <batch>. Claude's reading, unruled.

  Carried as an obligation
    Confirm provenance-discipline loads at 2.4 before provenance work

  [2026-08-16 list, for the record: builder marker join (DONE, L-196),
  stage 2 continuation markers (DONE), six Shape A citation swaps
  (DONE as seven, L-195), print the seven verdict tokens (DONE), and
  ledger entries for L-194, L-195, L-196 and the L-192 as-built (all
  written).]"""),

    # -- footer
    ("""Entry written August 2026 with Anthropic's Claude Opus 5. Updated
August 16, 2026, built on 227f5b2d6763baa384c090a911c2c5ced64f4a4d.""",
     """Entry written August 2026 with Anthropic's Claude Opus 5. Updated
August 18, 2026, built on b65ac115fc0f820e8270c0807249813c67bde7bc;
gallery at ff18d3e6fa31f70a8f525df471e751d046cf14fa."""),
]


# ============================================================
# 4. MASTER_PLAN_INTERACTIVE_GALLERY.md
# ============================================================

MP_EDITS = [
    ("""### You are here -- 2026-08-16, orrery `227f5b2`, gallery `3d10739`""",
     """### You are here -- 2026-08-18, orrery `b65ac11`, gallery `ff18d3e`"""),

    ("""| Segment 1, orrery | IN PROGRESS. Track 0 has no open rulings. The reconciliation is measured: 102 annotations scored, **3 clean**, 40 SEND BACK, 19 CONVERSATION, 40 noted. Dispatch repaired but not finished -- 9 blockers found by the August 16 Fable/GPT review, 1 closed. |""",
     """| Segment 1, orrery | IN PROGRESS. Track 0 has no open rulings. The reconciliation is measured: 110 annotations scored, **8 clean**, 48 SEND BACK, 20 CONVERSATION, 34 noted, 24 not scanner-reachable. The corpus grew and the clean count tripled because L-198 taught the scanner units it could not read -- coverage, not regression. Dispatch machinery COMPLETE as of August 18; 8 of the 9 August-16 blockers closed, the 9th (ordinal context window) deliberately unexercised by the pilot. The first dispatch has not gone out. |"""),

    ("""| Segment 3, assembler draw | NOT STARTED. Two lines plus a type, then the renderers. |""",
     """| Segment 3, assembler draw | NOT STARTED. Two lines plus a type, then the renderers. Now the only item anywhere with no ruling outstanding and no dependency on the provenance work. |"""),
]


PLAN = [
    (os.path.join(DOC, 'CRITICAL_PATH_SUMMARY.md'), CPS_EDITS),
    (os.path.join(DOC, 'TESTING_PROTOCOL.md'), TP_EDITS),
    (os.path.join(DOC, 'MASTER_PLAN_INTERACTIVE_GALLERY_SUMMARY.md'),
     MPS_EDITS),
    (os.path.join(DOC, 'MASTER_PLAN_INTERACTIVE_GALLERY.md'), MP_EDITS),
]


def fingerprint(data):
    """Content fingerprint: line endings normalized before hashing."""
    return hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()


def non_ascii(data):
    return [b for b in data if b > 127]


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    os.chdir(here)

    for name, _edits in PLAN:
        if not os.path.isfile(name):
            print('ERROR: %s not found. Run this from the repo root.' % name)
            return 1
        with open(name, 'rb') as handle:
            data = handle.read()
        seen = fingerprint(data)
        want = FINGERPRINTS[name]
        if seen != want:
            print('ERROR: %s has moved. Expected %s, found %s.'
                  % (name, want, seen))
            print('       Nothing written. Built against %s.' % ANCHOR_SHA)
            return 1

    staged = {}
    notes = []
    for name, edits in PLAN:
        with open(name, 'rb') as handle:
            data = handle.read()
        is_crlf = data.count(b'\r\n') > 0
        content = data
        for old, new in edits:
            old_b = old.encode('utf-8')
            new_b = new.encode('utf-8')
            if non_ascii(new_b):
                print('ERROR: this patch would insert non-ASCII bytes into '
                      '%s. Nothing written.' % name)
                return 1
            if is_crlf:
                old_b = old_b.replace(b'\n', b'\r\n')
                new_b = new_b.replace(b'\n', b'\r\n')
            count = content.count(old_b)
            if count != 1:
                print('ANCHOR FAIL: %s -- expected 1 match, found %d for:'
                      % (name, count))
                print('   %s' % old.splitlines()[0][:70])
                print('Nothing written.')
                return 1
            content = content.replace(old_b, new_b)
        left = non_ascii(content)
        if left:
            notes.append('note: %s still holds %d non-ASCII byte(s) this '
                         'patch did not reach (pre-existing prose)'
                         % (name, len(left)))
        staged[name] = content

    for name, edits in PLAN:
        with open(name, 'wb') as handle:
            handle.write(staged[name])
        print('ok  %s (%d edits)' % (name, len(edits)))

    for note in notes:
        print(note)
    print('patch applied')
    print('')
    print('Next: read documentation/CRITICAL_PATH_SUMMARY.md end to end.')
    print('      It is short, and it is the one somebody outside the work')
    print('      is most likely to read.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
