#!/usr/bin/env python3
"""
patch_L334_4_ledger_stage_b_20260918.py -- ORRERY repo.

Run: save this file in the ORRERY repo ROOT (next to LEDGER_CONSOLIDATED.md),
open it in VS Code and click Run.  Or:  python patch_L334_4_ledger_stage_b_20260918.py

A patch is run from its repository's ROOT and filed in documentation/ AFTER
it has run. Filed first and run second, it stops with one line, writes
nothing, and the push goes out without it.

Built on orrery 386347328a2d8a48ad2a156218a91d8622117c05
at https://github.com/tonylquintanilla/palomas_orrery
(gallery 2f971040d14f9a9ee8c3d7c49c9d2aa182a1e0f4)

WHAT IT DOES (one file, LEDGER_CONSOLIDATED.md, all-or-nothing):

  L-339  CLOSED. The live run now reads eleven served files instead of
         eight and found every one byte-identical. status -> DONE,
         section -> C. ledger_index.py moves the block there on its next
         run; this patch does not move it by hand.
  L-338  RULED by Tony on 2026-09-18, so the title stops calling it a
         proposal. His reason is recorded as his, and it is not the one
         the proposal argued from. A Gap remains: the rule does not
         travel until it is in the interactive-exhibit skill.
  L-334  Stage B is BUILT, PUSHED and seen on Tony's phone. The Gap
         narrows to stage C. Two places the build contract disagreed
         with the code are recorded, because the second one decides what
         the editor's arrival panel can offer.
  L-309  One line: the first piece of chrome to leave interactive.html
         took a name without the sun prefix, so the rename has one fewer
         identifier to reach and a precedent to follow.

THEN (Tony): python ledger_index.py LEDGER_CONSOLIDATED.md -- run it TWICE.

THE TWO RUNS PRINT DIFFERENT THINGS, and the first one looks worse than
it is. Expect, on the FIRST run:

    CONSISTENCY PROBLEMS:
      - [auto-fix] L-339: belongs in closed bucket 'C' but is not
        physically located in its destination heading
    Physically moved 1 block(s) into their bucket's destination heading.
    Index regenerated (194 live items) in LEDGER_CONSOLIDATED.md.

That is the indexer doing its job, not a failure: this patch marks L-339
closed and leaves the block where it sits, and the indexer is the thing
that moves a closed block into section C. It exits 0.

The SECOND run is the one to read as the verdict:

    OK: 334 L-blocks parsed, no consistency problems.
    Index regenerated (194 live items) in LEDGER_CONSOLIDATED.md.

194 live items rather than 195, because L-339 closed.

FAILURE: a single ERROR: or ANCHOR FAIL line, and NOTHING is written.
Undo is Discard Changes in GitHub Desktop.

Written September 2026 with Anthropic's Claude Opus 5.
"""
import hashlib
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
TARGET = 'LEDGER_CONSOLIDATED.md'
FP_EXPECTED = '86d9649bdb9d20a92de3a897389eab01'
ZONE = (b'<!-- INDEX:START', b'<!-- INDEX:END -->')

# ------------------------------------------------------------------
# L-339 -- closed by measurement
# ------------------------------------------------------------------
L339_CLOSE = b"""- **CLOSED 2026-09-18, and closed by measurement rather than by
  inspection.** Stage B of L-334 added the three names to
  `SERVED_FILES`. The live maintenance run at gallery `2f971040` fetched
  ELEVEN files from palomasorrery.com instead of eight and reported
  every one of them byte-identical to the working copy -- the three new
  ones among them: `gallery/arrival.js`, `gallery/nav_cluster.js` and
  `data/objects_config.json`. The check that compares what is served
  with what is committed now reads every file the page asks for.
  [verified @2f971040]
- **What it does NOT cover, said so the green is not read as wider than
  it is.** The list is files the page fetches BY NAME. The served cache
  under `data/solar-system/` is covered by two entries and by Cache in
  step, not file by file; a position file for an object nobody has drawn
  yet is not compared. That is a bound, not a gap: L-336's lesson is
  about the file the browser reads, and every one of those is now on the
  list.
**Gap:** none -- move to section C.
"""

# ------------------------------------------------------------------
# L-338 -- ruled
# ------------------------------------------------------------------
L338_RULING = b"""- **RULED, Tony, 2026-09-18:** yes. His words, and his reason: "the idea
  is to limit the increasing size of the interactive.html file, so yes."
- **His reason is not the one the proposal argued from, and the
  difference matters.** The proposal above argued from TESTABILITY -- a
  function inside the page can only be tested by cutting text out of the
  page. Tony's reason is SIZE. They point the same way for the arrival
  function and they part company at the edges: size also covers bulk
  that is not logic at all, a long block of styling for one, which
  testability says nothing about. The rule is written with his reason
  first and the second reason after it, and the wording goes to him when
  the skill is bumped, because that is where the scope question has to
  be answered rather than left to whoever reads it next.
- **First instance, done.** L-334 stage B moved the arrival function into
  `gallery/arrival.js` at gallery `2f971040`. 118 lines left
  `interactive.html`, `documentation/smoke_arrival.js` now requires the
  file instead of cutting text out of the page, and Tony's phone found
  both rooms unchanged.
**Gap:** the rule does not travel until it is in a skill a page edit
loads. It goes into interactive-exhibit 1.4 as piece 6 of L-334's stage
C, with the wording above for Tony to read. A convention that is not in
the skill does not travel (L-317, L-326, L-335, now here).
"""

# ------------------------------------------------------------------
# L-334 -- stage B built; the Gap narrows to stage C
# ------------------------------------------------------------------
L334_STAGE_B = b"""- **STAGE B BUILT, PUSHED and SEEN, 2026-09-18.** Delivered as
  `patch_L334_3_arrival_module_20260918.py`, pushed at gallery
  `2f971040`. What exists now: `gallery/arrival.js`, holding the arrival
  function whole and attached as `GalleryArrival.applyArrival`;
  `stampShell()` in `gallery/feature_renderers.js`, putting
  `meta.shell_key` on every trace that belongs to a served shell at nine
  sites; `stampLink()` giving each trace its own `meta` object and
  carrying an existing key across, so the two stamps cannot overwrite
  each other in either order; the end-of-legend-group-name match GONE,
  leaving one way of matching instead of two; `SERVED_FILES` at eleven
  names (L-339); and a rewritten `documentation/smoke_arrival.js` that
  requires the new file and checks that every trace the feature
  renderers build carries a key.
- **A visitor sees no difference, and that was measured, not judged.**
  Every trace in both rooms was compared before and after for its legend
  group and its arrival visibility: 86 traces, all identical. The
  offline run was 12 of 12 with Cache in step passing, which confirms
  the cache did not need to change -- the key is stamped in the browser
  and never stored. The four deliberate breaks each failed the check and
  named the cause, the fourth of them -- a shell trace with its stamp
  removed -- being the one the old name match could not have seen. Mode
  5 on the phone, both rooms, Tony: "correct". [render-confirmed Mode 5]
- **TWO PLACES THE BUILD CONTRACT DISAGREED WITH THE CODE.** Recorded
  because the second decides what stage C's arrival panel can offer.
  (1) The contract says `renderShellSet` already receives the shell's key
  as `featureKey`. It does not: `featureKey` is the GROUP -- `earth_interior`,
  `solar_atmosphere` -- and the shell key is the loop variable inside it.
  The stamping follows the file.
  (2) Earth's two radiation belts have NO key of their own in the served
  config. Their names and colours come from parallel lists, so there is
  nothing per-belt to stamp, and both carry the feature key
  `van_allen_belts`. An arrival block naming it draws both belts
  together. Stage C's panel therefore cannot offer one tick box per
  drawer row for the belts; it offers one box for the pair, unless Tony
  wants the served shape changed first.
  **Tony-action (decide), stage C:** one box for both belts, or a served
  change that gives each belt a key.
"""

L334_GAP_OLD_HEAD = b"""**Gap (current, 2026-09-17):** stages B and C of
"""

L334_GAP_NEW_HEAD = b"""**Gap (current, 2026-09-18):** STAGE C, the editor itself. Stage B is
done and its description is kept below as the record of what it was
contracted to do. Stage C is pieces 2 to 6 of the editor manifest with
its section 6 as the test list: the writer, which gains a true-or-false
operation for the arrival block's `moon` and refuses `_declared` and
`_comment` as well as `value`, `unit`, `figures` and `orrery_constant`;
the window, with one tick box per served shell by key and one for the
Moon; a Save message that tells the truth about what reaches a visitor
when, since words go through the cache builder and arrival ticks do not;
a Run-the-checks button that explains a red Cache in step rather than
just showing it; the suite; and piece 6's records, including the two
skill bumps under one protocol entry, v3.62. The editor does NOT start
the cache builder.
**Gap (as contracted on 2026-09-17; stage B is DONE):** stages B and C of
"""

# ------------------------------------------------------------------
# L-309 -- the rename gains a precedent
# ------------------------------------------------------------------
L309_NOTE = b"""- **2026-09-18, L-334 stage B: the first piece to leave the page took a
  name without the prefix.** The arrival function moved into
  `gallery/arrival.js` and is reached as `GalleryArrival.applyArrival`,
  not `sunApplyArrival`. It cost nothing, because a new file and one
  caller are not a hundred identifiers in a working room. So this item
  is one identifier smaller, and it has a precedent to follow: a piece
  that MOVES gets the new name in the move. `GalleryFeatures` and
  `GalleryArrival` are the shape for the rest.
"""

EDITS = [
    # --- L-339: closed ---------------------------------------------
    (b"<!-- L:339 status:OPEN upd:2026-09-17 section:A flag: rice:4/4/90/1 -->",
     b"<!-- L:339 status:DONE upd:2026-09-18 section:C flag: rice:4/4/90/1 -->"),
    (b"""- **Ref:** L-336 (the same fault, full size), L-235 (checks that cannot
  fail, gallery side), L-334 (stage B, which closes this), L-267 (the nav
  cluster);""",
     L339_CLOSE + b"""**Ref:** L-336 (the same fault, full size), L-235 (checks that cannot
fail, gallery side), L-334 (stage B, which closed this), L-267 (the nav
cluster);"""),

    # --- L-338: ruled ----------------------------------------------
    (b"#### [L-338] Logic that needs no browser lives in its own file -- a PROPOSAL, not yet a rule",
     b"#### [L-338] Logic that needs no browser lives in its own file (Tony's rule, 2026-09-18)"),
    (b"<!-- L:338 status:OPEN upd:2026-09-17 section:A flag: rice:3/3/60/1 -->",
     b"<!-- L:338 status:OPEN upd:2026-09-18 section:A flag: rice:3/3/80/1 -->"),
    (b"""- **Ref:** L-334 (stage B, the first instance), L-339, L-235; gallery
  `interactive.html`, `gallery/feature_renderers.js`,
  `documentation/smoke_arrival.js`;""",
     L338_RULING + b"""**Ref:** L-334 (stage B, the first instance), L-339, L-235; gallery
`interactive.html`, `gallery/feature_renderers.js`, `gallery/arrival.js`,
`documentation/smoke_arrival.js`;"""),

    # --- L-334: stage B done, Gap narrows --------------------------
    (b"<!-- L:334 status:OPEN upd:2026-09-17 section:A flag: rice:4/4/80/4 -->",
     b"<!-- L:334 status:OPEN upd:2026-09-18 section:A flag: rice:4/4/85/3 -->"),
    (L334_GAP_OLD_HEAD, L334_STAGE_B + L334_GAP_NEW_HEAD),

    # --- L-309: the rename gains a precedent -----------------------
    (b"""**Gap:** none until a third room or a free session; a rename, not a
redesign.""",
     L309_NOTE + b"""**Gap:** none until a third room or a free session; a rename, not a
redesign."""),
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
    print('edited: L-339 CLOSED (the live check now reads every file the '
          'browser fetches)')
    print('edited: L-338 RULED by Tony, with his reason recorded as his')
    print('edited: L-334 stage B built and seen; the Gap is stage C alone')
    print('edited: L-309 the rename gains one fewer identifier and a precedent')
    print('')
    print('patch applied. NEXT: python ledger_index.py LEDGER_CONSOLIDATED.md')
    print('                     -- run it TWICE.')
    print('')
    print('The FIRST run prints CONSISTENCY PROBLEMS and names L-339 as an')
    print('[auto-fix]. That is the indexer moving the closed block into')
    print('section C, which is its job -- not a failure. It exits 0.')
    print('The SECOND run is the verdict: expect "OK: 334 L-blocks parsed"')
    print('and 194 live items.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
