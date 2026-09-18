#!/usr/bin/env python3
"""
patch_L334_2_ledger_stage_a_20260917.py -- ORRERY repo.

Run: save this file in the ORRERY repo ROOT (next to LEDGER_CONSOLIDATED.md),
open it in VS Code and click Run.  Or:  python patch_L334_2_ledger_stage_a_20260917.py

A patch is run from its repository's ROOT and filed in documentation/ AFTER
it has run. Filed first and run second, it stops with one line, writes
nothing, and the push goes out without it.

Built on orrery cf586daaf0dbc0b76b10df7aff34420793acb467
at https://github.com/tonylquintanilla/palomas_orrery
(LEDGER_CONSOLIDATED.md is byte-identical to cf414139, the SHA the build
contract was written against; the only commit between them added the
contract itself.)

WHAT IT DOES (one file, LEDGER_CONSOLIDATED.md, all-or-nothing):

  L-334  the design is SETTLED and piece 1 is BUILT. Questions 2 to 5
         ruled by Tony 2026-09-17; the arrival ruling in his words; piece
         1 shipped and Mode 5 passed. The old Gap is kept as history and a
         new Gap names stages B and C of the build contract. upd -> 09-17.
  L-322  a dated line recording that the gallery half is DEPLOYED, which
         the item did not yet say, and the deployment fault it caused.
         upd -> 09-17.
  L-216  the third occurrence of the failed folder swap, Tony's hand
         routine, and his answer on moving the repositories. The Gap's
         "One data point" is now false and is corrected. upd -> 09-17.
  L-336  NEW, opened and CLOSED here (section C): the served cache went
         out of step with the config and no check read the file the
         browser reads.
  L-337  NEW, OPEN (section A): a centre marker for bodies without shells.
  L-338  NEW, OPEN (section A): logic that needs no browser lives in its
         own file -- a PROPOSAL awaiting Tony's ruling, not a rule.
  L-339  NEW, OPEN (section A): the live check does not read every file
         the browser fetches.

THEN (Tony): python ledger_index.py LEDGER_CONSOLIDATED.md -- run it TWICE.
Expect "OK: 334 L-blocks parsed" both times (330 before this patch, 4 added).

FAILURE: a single ERROR: or ANCHOR FAIL line, and NOTHING is written.
Undo is Discard Changes in GitHub Desktop.

Written September 2026 with Anthropic's Claude Opus 5.
"""
import hashlib
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
TARGET = 'LEDGER_CONSOLIDATED.md'
FP_EXPECTED = '6bb5650fa55e5e7460530a254c1ddbf9'
ZONE = (b'<!-- INDEX:START', b'<!-- INDEX:END -->')

# ------------------------------------------------------------------
# L-334: the note that merges the two unapplied ledger texts
# ------------------------------------------------------------------
L334_NOTE = b"""- **Design SETTLED and piece 1 BUILT, 2026-09-17.** The contract is three
  files read together:
  `documentation/BUILD_MANIFEST_L334_store_editor_20260917.md` (the editor
  manifest, whose sections 3, 6 and 7 stand as written), amended by
  `documentation/HANDOFF_L334_arrival_and_cache_check_20260917.md`, and
  with its sections 2, 4, 5, 8, 9 and 10 REPLACED by
  `documentation/BUILD_MANIFEST_L334_editor_build_20260917.md`, the build
  contract this item now runs under.
- **Questions 2 to 5, RULED by Tony 2026-09-17.** (2) The file is EDITED
  IN PLACE by the scanner in the gallery's `tools/mirror_constants.py`,
  which the editor's writer shares; the proposal above, to accept a
  one-time reformat through `json.dump`, is SUPERSEDED, because the L-322
  mirror already edits the hand-formatted config in place and two writers
  with two layouts would fight. (3) The arrival settings ARE served now --
  piece 1 shipped the block. (4) The measure is a per-field line count
  shown beside the field as it is typed, plus a button that runs the
  offline checks and shows their verdicts. (5) Tkinter, started from VS
  Code's Run button, the same way Studio is.
- **Tony's arrival ruling, 2026-09-17, in his words:** a room opens on
  "the surface shell plus frame elements like sun direction, axes,
  terminator", and "exclude the moon with its box not selected." This
  SUPERSEDES two earlier rulings of his own -- the Sun's 0.25 AU arrival
  of 2026-08-29 and the L-291 eight-shell Earth arrival of 2026-09-06/08,
  where the terminator started off.
- **Piece 1 shipped** as gallery `7c95435` with `59ba809`. Each room's
  object in `data/objects_config.json` carries an `arrival` block naming
  the shells drawn when the room opens; `sunApplyArrival` in
  `interactive.html` applies it before the opening view is measured, so
  the view fits what is drawn. With no block the page behaves as before.
  Mode 5 on the phone, both rooms, Tony: "yes, perfect. beautiful."
  There is NO floor under the opening view, which settles the editor
  manifest's section 8 item 1. [render-confirmed Mode 5]
- **What the shipped block actually holds**, and it differs from the
  editor manifest's plan: `drawn` (a list of shell KEYS) and `moon` (true
  or false), plus an optional `min_half_range_au` that the page reads and
  neither room uses. The arrival block is read straight from
  `data/objects_config.json` by the page, so a change to it reaches a
  visitor on the push alone; the shells and their words come from the
  served cache and reach a visitor only after the cache builder has run.
  That split is the fact the editor's Save message has to tell the truth
  about (stage C). [verified @1b077401]
"""

L334_GAP_OLD = b"""**Gap:** L-322 first; then questions 2 to 5 in conversation; then the
build, in this order: the arrival block and its page reader (3), the
editor over prose and links (2, 5), the measure and the checks button
(4).
  **Tony-action (decide):** questions 2 to 5, at the start of the build
  session.
"""

L334_GAP_NEW = b"""**Gap (as it stood on 2026-09-16, now DISCHARGED -- kept as the record of
what the order was before the arrival scene shipped):** L-322 first; then
questions 2 to 5 in conversation; then the build, in this order: the
arrival block and its page reader (3), the editor over prose and links
(2, 5), the measure and the checks button (4).
  **Tony-action (decide) -- DONE 2026-09-17:** questions 2 to 5.
**Gap (current, 2026-09-17):** stages B and C of
`documentation/BUILD_MANIFEST_L334_editor_build_20260917.md`, in that
order, each pushed and confirmed before the next starts. STAGE B, the
arrival tidy-up, a visitor seeing no difference: `sunApplyArrival` moves
whole into a new `gallery/arrival.js`; `gallery/feature_renderers.js`
stamps each shell trace with its own `meta.shell_key`; the arrival
function matches on that key and the end-of-legend-group match is
removed; `documentation/smoke_arrival.js` requires the new file and gains
a fourth deliberate break (an unstamped shell trace); `SERVED_FILES`
gains three names (L-339). STAGE C, the editor itself: pieces 2 to 6 of
the editor manifest, its section 6 as the test list, with the writer
gaining a true-or-false operation for `moon` and refusing `_declared` and
`_comment` as well as `value`, `unit`, `figures` and `orrery_constant`;
one tick box per served shell by key and one for the Moon; a Save message
that says truthfully what reaches a visitor when; and piece 6's records,
which include the two skill bumps that make this session's lessons travel
-- interactive-exhibit 1.3 to 1.4 (the arrival block, the trace stamp, who
may write the config, and the rule that one check must read the file the
browser fetches) and gallery-cache-builder 1.4 to 1.5 (a config change is
not deployed until the cache is rebuilt, and the corrected occurrence
count for L-216), both carried by ONE protocol entry, v3.62.
"""

# ------------------------------------------------------------------
# L-322: the gallery half is deployed
# ------------------------------------------------------------------
L322_DEPLOYED = b"""**Note (2026-09-17, late) -- the gallery half is DEPLOYED, and the
deployment broke both rooms on the way.** The item did not yet say the
first part. Per the session record
(`documentation/HANDOFF_L334_arrival_and_cache_check_20260917.md`) the
gallery half went out at gallery `d2ca28b6` and the cache was rebuilt at
`9ff39cc4`. Confirmed at gallery `1b077401`: `tools/mirror_constants.py`,
`tools/test_mirror_constants.py` and `data/constants_export.json` are
present, and the runner carries Constants export pull, Config mirror,
Mirror suite, Config mirror check, Pointer join and Export freshness,
with Store drift narrowed rather than retired. [verified @1b077401]
THE FAULT, and it is L-336: the config was pushed ahead of the cache
builder. The unit spellings changed in the config and in the renderers,
the served cache still held the old ones, and the renderers refused every
shell that used them -- 9 drawer rows instead of 18 in the Sun's room, 8
in Earth's, while the maintenance run printed 11 of 11. The rule this
item now inherits: a config change is not deployed until the cache is
rebuilt, and the config and the cache are committed together.
"""

# ------------------------------------------------------------------
# L-216: third occurrence
# ------------------------------------------------------------------
L216_NOTE = b"""**Note (2026-09-17) -- THIRD OCCURRENCE, and the Gap's "One data point"
is now false.** The swap failed again at `staging -> live` with "Access is
denied", during the cache rebuild that the L-322 deployment fault made
necessary. It left the working copy with no served cache and GitHub
Desktop offering 67 changes, most of them deletions. Tony did not push.
Tony: "This is like the third time."
THE RECOVERY was the operational rule above, with ONE STEP ADDED, because
the same change list also held the arrival work: commit the NON-CACHE
files first, then discard the rest, then re-run. A blanket discard would
have thrown away committed-worthy work sitting beside the wreckage.
TONY'S CURRENT PRACTICE, and it is deliberate: the scheduled nightly run
is SUSPENDED and he builds by hand, pausing OneDrive syncing first and
watching GitHub Desktop's change list, stopping if the commit does not
form correctly. Pausing sync before the re-run worked.
MOVING THE REPOSITORIES OUT OF ONEDRIVE was raised as the lasting fix.
Tony, 2026-09-17: "not at this time." It is a change to his machine
outside his usual working set and needs its steps and risks written out
before he decides.
**Tony-action (do) -- SCHEDULED:** the skill sentence that calls this
"one data point" is corrected in gallery-cache-builder 1.5, together with
the hand routine above, as piece 6 of L-334's stage C.
"""

L216_GAP_OLD = b"""**Gap:** unmeasured -- whether the `staging -> live` rename is exposed
to the same lock as the cleanup, or was unlucky once. One data point.
"""

L216_GAP_NEW = b"""**Gap (corrected 2026-09-17):** the CAUSE, not the exposure. Three
occurrences settle what one did not: the `staging -> live` rename IS
exposed to the same lock as the cleanup, and it is not bad luck. What
remains is the fix -- retry the renames with backoff, or move the
repository off OneDrive (Tony: not at this time) -- and the visibility
gap above, which still comes first.
"""

# ------------------------------------------------------------------
# New blocks
# ------------------------------------------------------------------
L336_BLOCK = b"""#### [L-336] The served cache went out of step with the config, and no check read the file the browser reads (gallery)
<!-- L:336 status:DONE upd:2026-09-17 section:C flag: rice:4/4/95/2 -->
- **What happened, 2026-09-17.** The L-322 gallery half was pushed at
  gallery `d2ca28b6` before the cache builder had run. The exhibit rooms
  draw their shells from the served cache,
  `data/solar-system/coverage_index.json`, which the builder copies from
  `data/objects_config.json`. L-322 changed the unit spellings in the
  config and in the renderers (`R_sun` to `r_sun`). The cache still held
  the old spelling, so the renderers refused every shell that used it.
  Tony's phone showed the Sun's room with 9 drawer rows instead of 18 and
  Earth's with 8, on the live site. Claude reproduced the drawer row for
  row by building the rooms from the cache record in node.
- **Eleven checks passed while it was broken.** Every one of them built
  its scene from the config or from a recorded fixture. None read the
  cache, which is the file the browser fetches. A green run said nothing
  about the live site. This is the resident protocol's A Check That
  Cannot Fail Is Not Passing, in the third of its four shapes: the check
  was in a store nobody's browser opens.
- **What was built and is now gating.** `tools/check_cache_in_step.py`,
  wired into `gallery_maintenance_run.py` as "Cache in step". It compares
  the served cache against the config it was built from. Measured against
  two real commits: it PASSES at gallery `9ff39cc4` and FAILS at
  `d2ca28b6` -- the exact state that broke the rooms -- naming 36
  differences. At gallery `1b077401` the offline maintenance run is 12 of
  12 and the check compared 4 objects and 34 named shells in both cache
  files. [verified @1b077401]
- **THE LESSON, which is the durable half.** A CONFIG CHANGE IS NOT
  DEPLOYED UNTIL THE CACHE IS REBUILT, and the config and the cache are
  COMMITTED TOGETHER. This was true before 2026-09-17 and written down
  nowhere. It changes the routine for the L-322 mirror, for any config
  patch, and for the L-334 editor: change the config, run the cache
  builder, run the maintenance run, commit config and cache together,
  push. The general form: for anything a visitor sees, ask which file the
  browser actually fetches, and make one check read THAT file.
- **Two things this item does NOT close, both re-homed.** The lesson does
  not travel until it is in a skill: gallery-cache-builder 1.5 carries
  it, as piece 6 of L-334's stage C, and L-334's Gap names it. And the
  same blind spot exists one size smaller in the LIVE check, which does
  not read every file the browser fetches: that is L-339, which stage B
  closes.
- **Claude:** RICE 4/4/95/2 -> 7.6 proposed, unratified. Reach 4 because
  it gates every future config push in both rooms; Impact 4 because the
  failure it catches is a silently broken live site; Confidence 95
  because the check was measured against two real commits, one passing
  and one failing; Effort 2, built and shipped in one evening.
- **Ref:** L-322 (the deployment), L-334 (the editor that inherits the
  routine), L-339 (the live-check gap), L-235 (checks that cannot fail,
  gallery side), L-216 (the folder swap that made the rebuild an
  ordeal); gallery `tools/check_cache_in_step.py`,
  `gallery_maintenance_run.py`, `data/objects_config.json`,
  `data/solar-system/coverage_index.json`;
  `documentation/HANDOFF_L334_arrival_and_cache_check_20260917.md`,
  gallery `documentation/patch_L334_1c_cache_in_step_20260917.py`,
  `documentation/patch_L334_1d_dashboard_cache_in_step_20260917.py`.

"""

L337_BLOCK = b"""#### [L-337] A centre marker for bodies without shells in the exhibit rooms
<!-- L:337 status:OPEN upd:2026-09-17 section:A flag: rice:3/2/60/2 -->
- **Tony, 2026-09-17, at the phone check of both rooms:** the Sun's room
  has a "Sun" object at the centre, as the orrery does, and Earth's room
  has none; "that might be a useful object to add for future solar system
  scenes without shells."
- **Recorded, not built.** L-334's build contract puts it out of scope
  for that build (its section 7).
- **What a build would have to settle first.** What the marker IS -- the
  Sun's centre object may already be that thing, or may be a shell like
  any other, and nobody has looked. Where it comes from: drawn by the
  renderer from the served record, or a served feature in its own right.
  What it says on hover, under the exhibit's provenance contract, since a
  marker at the centre of a body is a natural place to put the body's own
  numbers and those numbers have to be served with their source.
- **Claude:** RICE 3/2/60/2 -> 1.8 proposed, unratified. Reach 3 because
  it is every future room rather than only Earth's; Impact 2 because a
  room without it is complete, not broken; Confidence 60 because nothing
  above is settled; Effort 2.
- **Ref:** L-334 (the contract that scoped it out), L-320 (info markers
  and the served marker angles), L-291 (the Earth room), interactive-exhibit
  skill (what an exhibit may render and where its numbers come from);
  gallery `gallery/feature_renderers.js` (`infoMarker`), `interactive.html`.

"""

L338_BLOCK = b"""#### [L-338] Logic that needs no browser lives in its own file -- a PROPOSAL, not yet a rule
<!-- L:338 status:OPEN upd:2026-09-17 section:A flag: rice:3/3/60/1 -->
- **Tony asked, 2026-09-17,** whether `interactive.html` should be
  modularized. The page is 3436 lines at gallery `1b077401` and holds
  logic that no browser is needed to run.
- **Claude's proposal, and it is a proposal.** No general reorganisation.
  Instead: logic that needs no browser MOVES OUT of the page into its own
  file WHEN A BUILD ALREADY TOUCHES IT, so a check can reach it. The
  reasoning is the same one behind A Check That Cannot Fail Is Not
  Passing -- `documentation/smoke_arrival.js` today tests the arrival
  function by CUTTING THE TEXT between two comment lines out of the page
  and running it in node, which is a check whose subject is a substring
  rather than a file, and it stops being true the moment the comment
  lines move.
- **This is recorded as awaiting a ruling, not as a rule in force.** It is
  written here so that a later session does not read a one-off move as a
  standing convention, or the reverse.
- **Its first instance is already scheduled either way.** Stage B of
  L-334's build contract moves `sunApplyArrival` into `gallery/arrival.js`
  and has `smoke_arrival.js` require the file instead of cutting text out
  of the page. Stage B goes ahead whether or not this becomes a rule.
  **Tony-action (decide):** whether it does. If adopted it belongs in the
  interactive-exhibit skill, where a page edit will load it.
- **Claude:** RICE 3/3/60/1 -> 5.4 proposed, unratified. Effort 1 because
  adopting it costs a sentence in a skill; the moves themselves are paid
  for by the builds that were already opening those files, which is the
  whole point of the proposal.
- **Ref:** L-334 (stage B, the first instance), L-339, L-235; gallery
  `interactive.html`, `gallery/feature_renderers.js`,
  `documentation/smoke_arrival.js`; resident protocol Part 3, A Check
  That Cannot Fail Is Not Passing; interactive-exhibit skill.

"""

L339_BLOCK = b"""#### [L-339] The live check does not read every file the browser fetches
<!-- L:339 status:OPEN upd:2026-09-17 section:A flag: rice:4/4/90/1 -->
- **Measured at gallery `1b077401`.** `gallery_maintenance_run.py --live`
  compares EIGHT served files against the working copy (`SERVED_FILES`,
  line 254): `interactive.html`, `gallery/feature_renderers.js`,
  `gallery/earth_geometry.js`, `gallery/assembler/resolver.py`,
  `gallery/assembler/__init__.py`,
  `data/solar-system/coverage_index.json`,
  `data/solar-system/feature_configs.json` and
  `data/solar-system/positions/voyager_1.json`. The list does NOT include
  `data/objects_config.json` or `gallery/nav_cluster.js`, and the page
  fetches both -- the script tag at `interactive.html` line 132 and the
  config read at line 2251. [verified @1b077401]
- **It is the same fault as L-336, one size smaller.** There, no check
  read the cache the browser draws from, and both rooms broke while
  eleven checks passed. Here, the check that exists precisely to compare
  what is SERVED with what is in the working copy skips two files the
  browser asks for. A file nobody compares can go stale on the live site
  with nothing saying so.
- **Stage B of L-334's build contract closes it**, adding
  `gallery/arrival.js` (new in that stage), `gallery/nav_cluster.js` and
  `data/objects_config.json` to `SERVED_FILES`.
- **Claude:** RICE 4/4/90/1 -> 14.4 proposed, unratified, and the score
  is descriptive rather than a scheduling claim -- stage B already
  carries it. Reach 4 and Impact 4 for the reason above: the arrival
  block is read from `data/objects_config.json` by the page itself, so a
  stale served copy changes what a visitor sees on opening. Effort 1
  because it is three names added to a list, though a first run may need
  a reconciliation if a served copy has already drifted.
- **Ref:** L-336 (the same fault, full size), L-235 (checks that cannot
  fail, gallery side), L-334 (stage B, which closes this), L-267 (the nav
  cluster); gallery `gallery_maintenance_run.py` (`SERVED_FILES`),
  `interactive.html`, `gallery/nav_cluster.js`,
  `data/objects_config.json`; resident protocol Part 3, A Check That
  Cannot Fail Is Not Passing.

"""

SECTION_A_ANCHOR = b"""## A. ACTIVE SEPARATE TRACKS (not orrery-refactor backlog; cross-referenced)

"""

SECTION_C_ANCHOR = b"""## C. RECONCILED LEDGER -- DONE (closed; for the record, do not re-do)

"""

EDITS = [
    # --- new OPEN blocks at the top of section A -------------------
    (SECTION_A_ANCHOR,
     SECTION_A_ANCHOR + L339_BLOCK + L338_BLOCK + L337_BLOCK),

    # --- L-334: upd, the note, and the new Gap ---------------------
    (b"<!-- L:334 status:OPEN upd:2026-09-16 section:A flag: rice:4/4/80/4 -->",
     b"<!-- L:334 status:OPEN upd:2026-09-17 section:A flag: rice:4/4/80/4 -->"),
    (L334_GAP_OLD, L334_NOTE + L334_GAP_NEW),

    # --- L-216: upd, the third-occurrence note, the corrected Gap --
    (b"<!-- L:216 status:OPEN upd:2026-08-19 section:A flag: rice:3/3/85/2 -->",
     b"<!-- L:216 status:OPEN upd:2026-09-17 section:A flag: rice:3/3/85/2 -->"),
    (L216_GAP_OLD, L216_NOTE + L216_GAP_NEW),

    # --- L-322: upd and the deployment line ------------------------
    (b"<!-- L:322 status:OPEN upd:2026-09-16 section:A flag: rice:4/5/70/6 -->",
     b"<!-- L:322 status:OPEN upd:2026-09-17 section:A flag: rice:4/5/70/6 -->"),
    (b"""**Ref:** L-305, L-306 (approximations are not promoted), L-314,
`constants_new.py`, `provenance_scanner.py`, `orrery_maintenance_run.py`,""",
     L322_DEPLOYED + b"""**Ref:** L-305, L-306 (approximations are not promoted), L-314,
`constants_new.py`, `provenance_scanner.py`, `orrery_maintenance_run.py`,"""),

    # --- the new DONE block at the top of section C ----------------
    (SECTION_C_ANCHOR, SECTION_C_ANCHOR + L336_BLOCK),
]


def lf(data):
    return data.replace(b'\r\n', b'\n')


def fingerprint(content):
    a = content.index(ZONE[0])
    b = content.index(ZONE[1]) + len(ZONE[1])
    return hashlib.md5(content[:a] + content[b:]).hexdigest()


def main():
    path = os.path.join(ROOT, TARGET)
    if not os.path.exists(path):
        print(f'ERROR: {TARGET} not found next to this script.')
        print('       Run this patch from the ORRERY repo ROOT, not from')
        print('       documentation/. NOTHING was written.')
        return 1
    raw = open(path, 'rb').read()
    was_crlf = b'\r\n' in raw
    content = lf(raw)
    actual = fingerprint(content)
    if actual != FP_EXPECTED:
        print(f'ERROR: {TARGET} is not the file this patch was built against')
        print(f'       expected {FP_EXPECTED}, found {actual}'
              f'{" [CRLF]" if was_crlf else ""}')
        print('       NOTHING was written. Undo is Discard Changes in GitHub Desktop.')
        return 1
    original = content
    for old, new in EDITS:
        n = content.count(old)
        if n != 1:
            print(f'ANCHOR FAIL: expected 1 match, found {n}: {old[:70]!r}')
            print('NOTHING was written. Undo is Discard Changes in GitHub Desktop.')
            return 1
        content = content.replace(old, new, 1)
    if any(c > 127 for c in content):
        print('ERROR: the patched ledger would hold non-ASCII bytes. NOTHING was written.')
        return 1
    if content == original:
        print('ERROR: unchanged after edits. NOTHING was written.')
        return 1
    out = content.replace(b'\n', b'\r\n') if was_crlf else content
    with open(path, 'wb') as f:
        f.write(out)
    print(f'ok  {TARGET}  ({len(out)} bytes'
          f'{", CRLF preserved" if was_crlf else ""})')
    print('edited: L-334 (design settled, piece 1 built, new Gap)')
    print('edited: L-322 (gallery half deployed, and the fault it caused)')
    print('edited: L-216 (third occurrence; "One data point" corrected)')
    print('added:  L-336 DONE, L-337 OPEN, L-338 OPEN, L-339 OPEN')
    print('')
    print('patch applied. NEXT: python ledger_index.py LEDGER_CONSOLIDATED.md')
    print('                     -- run it TWICE, expect "OK: 334" both times.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
