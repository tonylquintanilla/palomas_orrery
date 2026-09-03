"""
patch_L278_session_ledger_20260902.py -- the 2026-09-02 session record.

Built on palomas_orrery 91735ac4b4cf7353a80a954e80c2c96151df7aeb at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Gallery at 6fd6baaf236ef1fff10b36a03d3c9fe66dcd7b9e.

WHAT IT DOES

  LEDGER_CONSOLIDATED.md only. Two amendments and two new items.

  L-254 amended -- the Venus and Mars slice is done, and the "SIX are
      live" count is corrected to say which axis it was measured on.
      Six of 82 `create_*_shell`; 25 builders are live in those modules
      once the ones that do not match that pattern are counted.
  L-267 amended -- Stage A and Stage B both shipped. The click hang and
      its fix are recorded. Stage C is blocked on L-265.
  L-278 opened -- a relayout called from inside a Plotly event handler
      re-enters the update machinery before the dispatch returns. The
      portable finding, and the gallery-pipeline field note it needs.
  L-279 opened -- a test protocol that leaves the test CONDITIONS
      uncontrolled produces confident wrong readings. Three this
      session.

  The INDEX regenerates on the next maintenance run; this patch does not
  touch it.

HOW TO RUN
  Open in VS Code from the ORRERY repo root and press Run. Then run the
  maintenance runner, which rebuilds the ledger index.

GUARDS
  Fingerprinted, every anchor verified once before any write,
  all-or-nothing, no .bak. Undo is Discard Changes in GitHub Desktop.

Module created: September 2, 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

TARGET = 'LEDGER_CONSOLIDATED.md'
EXPECTED = '75025053cc43bda3ec1a8b5903596e36'

L254_ANCHOR = """#### [L-254] 76 dead sphere-shell builders, unmarked, across 12 modules
<!-- L:254 status:OPEN upd:2026-08-26 section:A flag: rice:3/3/95/3 -->
"""

L254_NEW = """#### [L-254] 76 dead sphere-shell builders, unmarked, across 12 modules
<!-- L:254 status:OPEN upd:2026-09-02 section:A flag: rice:3/3/95/3 -->
**AMENDED 2026-09-02 -- the axis, and the Venus and Mars slice.**

THE COUNT NEEDED ITS AXIS. "SIX are live" is true of
`create_*_shell` and of nothing else. Nineteen further builders in the
same modules are on the live dispatch and simply do not carry the
`_shell` suffix, so 25 builders are live in total: jupiter's
`io_plasma_torus`, `magnetosphere`, `radiation_belts` and `ring_system`;
saturn's `enceladus_plasma_torus`, `magnetosphere`, `radiation_belts` and
`ring_system`; solar's `galactic_tide`, `hills_cloud_torus`,
`outer_oort_clumpy` and `streamer_band`; uranus's and neptune's
`magnetosphere`, `radiation_belts` and `ring_system` each; and mercury's
`sodium_tail`. Verified against shell_configs.py at 5639a952.

The 76 dead are still dead -- nothing about the census was wrong. What
was wrong was a conclusion drawn from it in session: that the modules
other than venus and mars were "all dead". Only four are: pluto, eris,
moon and planet9. The other eight have live builders sitting beside dead
ones. This is A Report Names Its Items in its sharpest form again -- a
count does not carry the axis it was counted on -- and the axis is now
written into the dispatch notes in the code rather than left in a
document.

DONE THIS SLICE, at `5639a952` via `patch_L254_2`: venus 6 and mars 7
annotated, with a dispatch note in each naming the live magnetosphere
builder and stating the census pattern. Deliberately no count in those
notes; a count in a comment is a hand-maintained copy of something the
file already reports.

FIXED IN PASSING: `create_mars_hill_sphere_shell` carried a second
docstring-shaped string reading "Creates Mars's upper atmosphere shell."
-- a copy-paste orphan with the wrong label and no effect. Removed.

REMAINING 55, counted from disk at 5639a952: solar 14, jupiter 6,
saturn 6, moon 6, pluto 6, eris 5, neptune 5, uranus 5, planet9 2.
Solar's fourteen are the only ones the current artifact reaches. The rest
wait for the ladder, per The Braid.

FORWARD COST, and it is L-277: four of those nine modules also hold
L-192 sites, so four more slices will break the worksheet key round trip
and the extractor pins the same way this one did.

"""

L267_ANCHOR = """#### [L-267] The Sun exhibit GUI shape: drawer, focus label, marker navigation
<!-- L:267 status:OPEN upd:2026-08-30 section:A flag: rice:4/3/85/3 -->
"""

L267_NEW = """#### [L-267] The Sun exhibit GUI shape: drawer, focus label, marker navigation
<!-- L:267 status:OPEN upd:2026-09-02 section:A flag: rice:4/3/85/3 -->
**AMENDED 2026-09-02 -- Stage B shipped, after a hang.**

STAGE A shipped 2026-08-31 at gallery `2ed12564`: the drawer replaced the
legend and the portrait defect was fixed.

STAGE B shipped 2026-09-02 at gallery `e0edd16c` via `patch_L267_2`, a
port of `sun_gui_mockup.html`, which Tony accepted at Mode 5 over two
rounds on 2026-08-30. Ten edits: the row split with a red GO, the focused
row style, the focus label replacing the count on the drawer handle,
cross-marker navigation keyed on `curveNumber`, and the framing floor
removed for focus framing while the arrival floor stays. One job per
control -- the box draws, everything else moves the camera.

THEN IT HUNG. Clicking a cross marker froze the page with
`RangeError: Maximum call stack size exceeded` from inside
plotly-2.35.2. Eight reads to attribute; the finding is portable and is
recorded separately as L-278. Fixed at gallery `6fd6baaf` via
`patch_L267_3`, two lines: the click handler defers `sunFocusOn` by one
tick so Plotly finishes dispatching before the relayout starts.

MODE 5 PASSED, Tony, 2026-09-02, on the live page: markers click freely
and fast including the outer corona and the Alfven surface with nothing
freezing; the focus label and camera follow the marker clicked; the
drawer checkboxes draw and hide without moving the camera.

STAGE C, the i panel, is NOT started and is blocked on L-265. All twenty
`info_url` values in the served `feature_configs.json` are the
placeholder `https://www.nasa.gov/`, so wiring the panel now would give
every shell the same dead link. Tony's stated preference 2026-09-02 is to
see the info icon working BEFORE the phone and tablet passes, which makes
L-265's curated links the thing standing between here and mobile.

"""

L278 = """#### [L-278] A relayout from inside a Plotly event handler re-enters the update machinery
<!-- L:278 status:OPEN upd:2026-09-02 section:A flag: rice:3/3/90/1 -->
- **The failure.** Clicking a cross marker in the Sun exhibit froze the
  page: no rotation, no hover, the modebar reset dead, recoverable only
  by reload. One error, `RangeError: Maximum call stack size exceeded`,
  thrown from inside plotly-2.35.2.
- **The code was correct. The CONTEXT was the bug.** The same
  `Plotly.relayout` completed cleanly three separate ways -- called from
  the console with a tooltip up, with the tooltip dismissed, and on a
  five-second timer while the pointer rested on a marker. In every one
  the axes took their new tick spacing and the page kept working. It was
  fatal only when reached from inside `plotly_click`, because Plotly had
  not finished dispatching the click when `layoutReplot` was sent back
  into it.
- **The tell was the stack DEPTH, and it was missed twice.** The recorded
  stack is about twenty-five frames. A stack overflow on a SHALLOW stack
  is not runaway recursion -- it is a large array applied as function
  arguments, which is what a half-finished replot re-entering itself
  produces. Two hypotheses were pursued and discarded before that was
  read correctly.
- **The fix is one tick.** `setTimeout(fn, 0)` around the focus call lets
  the dispatch return first. Confirmed live from the console, by
  replacing the handler in the running page, BEFORE any patch was
  written.
- **Scope: anything that mutates a plot from a Plotly event.**
  `plotly_click`, `plotly_hover`, `plotly_selected`, `plotly_relayout`.
  The gallery has one such handler today; the orrery's Plotly code and
  any future exhibit can grow more.
**Note:** two hypotheses died on the way and both are worth keeping.
Hover hit-testing was blamed first, on the strength of a real 2026-08-30
finding and the fact that its `Plotly.Fx.unhover` fix never travelled
from the mockup to `interactive.html` -- but dismissing the tooltip was
tested directly and changed nothing. Trace size was blamed second, on the
65,000-argument limit -- but the largest trace in the scene is 4,332
points and the one that hung is 400. Neither was a bad guess; both were
testable, and testing is what killed them.
- Tony-action (do): bump `gallery-pipeline` with this as a field note,
  since it fires on exactly the code that would hit it again.
**Gap:** skill patch not written. The finding lives only here and in
`patch_L267_3`'s comment until it does.
**Ref:** gallery `6fd6baaf` `interactive.html` the `plotly_click`
handler; `patch_L267_3_defer_click_focus.py`;
`TEST_PROTOCOL_sun_hang_20260902.md`; L-267; L-262.

"""

L279 = """#### [L-279] A test protocol that leaves the CONDITIONS uncontrolled produces confident wrong readings
<!-- L:279 status:OPEN upd:2026-09-02 section:A flag: rice:3/2/80/1 -->
- **What happened.** The Sun hang protocol specified what to DO in each
  trial and not what STATE to do it in. Three readings were wrong as a
  result, each stated confidently to Tony before he corrected it.
- **The three.** (1) Trials 1 and 2 were read as exonerating hover and
  scene weight; both had been run on a light scene, one shell at a time,
  and Trial 2 never tapped a marker at all -- it exercised the checkbox
  path. (2) Trial R was then read as running with the full default set;
  it used the same reduced set as Trial 1, so the drawn set was never the
  variable. (3) Read 6 was reported by Tony as "both hang" and read that
  way, when his own notes said the timed relayouts completed -- the
  secondary ticks appeared -- and the hang came on a click both times.
- **The pattern.** Each wrong reading came from inferring the test
  conditions rather than recording them. The trials themselves were
  sound; what was missing was a stated starting state and a stated
  gesture.
- **What would have prevented all three.** Every trial names the drawn
  set, the gesture, and the pointer's location, and the report form asks
  for those back rather than only for the outcome.
**Note:** the deeper version is this project's own rule pointed at its
own diagnostics. A trial that cannot fail is one thing; a trial that CAN
fail but whose conditions are unrecorded is worse, because it produces a
result that looks like evidence. Tony carried the correction three times
in one session, which is exactly the load the protocol exists to spare
him.
- Tony-action (decide): where this lands. It is method, so
  Method Belongs to the Skill points at a skill -- but no current skill
  owns diagnostic protocols, and the two readers it protects are the same
  two A Report Names Its Items was written for, which argues for the
  resident protocol instead.
**Gap:** decision, then a patch. Nothing is written anywhere yet.
**Ref:** `TEST_PROTOCOL_sun_hang_20260902.md`, which carries all three
corrections in view; L-278; PROJECT_INSTRUCTIONS.md Part 3 A Check That
Cannot Fail Is Not Passing.

"""

L277_ANCHOR = """#### [L-277] The L-192 site store anchors by line number, so any insertion breaks two checkers
"""


def fail(msg):
    print('')
    print('FAILURE: %s' % msg)
    print('NOTHING was written. No file on disk has changed.')
    print('If a previous run did write, undo is Discard Changes in GitHub Desktop.')
    sys.exit(1)


def read_lf(path):
    raw = open(path, 'rb').read()
    was_crlf = b'\r\n' in raw
    return (raw.replace(b'\r\n', b'\n') if was_crlf else raw), was_crlf


EDITS = [
    (L254_ANCHOR, L254_NEW),
    (L267_ANCHOR, L267_NEW),
    (L277_ANCHOR, L278 + L279 + L277_ANCHOR),
]


def main():
    print('patch_L278 -- the 2026-09-02 session ledger')
    print('=' * 58)

    for _, new in EDITS:
        try:
            new.encode('ascii')
        except UnicodeEncodeError as exc:
            fail('non-ASCII in replacement text: %s' % exc)

    if not os.path.exists(TARGET):
        fail('%s not found. Run this from the ORRERY repo root.' % TARGET)

    content, was_crlf = read_lf(TARGET)
    actual = hashlib.md5(content).hexdigest()
    if actual != EXPECTED:
        fail('BASE MOVED for %s.\n  expected %s\n  found    %s\n'
             '  Built against orrery 91735ac4. A size delta of about one\n'
             '  byte per line is CRLF, not content.' % (TARGET, EXPECTED, actual))
    print('  %-24s fingerprint matches%s' % (TARGET, ' [CRLF]' if was_crlf else ''))

    if b'L:278' in content:
        fail('%s already carries L-278. This patch has run.' % TARGET)

    out = content
    for anchor, new in EDITS:
        a = anchor.encode('ascii')
        n = out.count(a)
        if n != 1:
            fail('anchor matched %d times (expected 1):\n    %r'
                 % (n, anchor.strip()[:80]))
        out = out.replace(a, new.encode('ascii'))
    print('  all %d anchors verified' % len(EDITS))

    with open(TARGET, 'wb') as f:
        f.write(out.replace(b'\n', b'\r\n') if was_crlf else out)
    print('  wrote %s' % TARGET)

    # --- Post-conditions, read back from disk -------------------------
    disk = read_lf(TARGET)[0].decode('utf-8', 'replace')
    print('')
    print('Post-conditions (read back from disk):')

    ok = True
    checks = [
        ('L-278 header',      '#### [L-278] A relayout from inside'),
        ('L-278 metadata',    '<!-- L:278 status:OPEN upd:2026-09-02'),
        ('L-279 header',      '#### [L-279] A test protocol that leaves'),
        ('L-279 metadata',    '<!-- L:279 status:OPEN upd:2026-09-02'),
        ('L-254 amended',     'AMENDED 2026-09-02 -- the axis, and the Venus'),
        ('L-254 date bumped', '<!-- L:254 status:OPEN upd:2026-09-02'),
        ('L-267 amended',     'AMENDED 2026-09-02 -- Stage B shipped'),
        ('L-267 date bumped', '<!-- L:267 status:OPEN upd:2026-09-02'),
        ('L-277 still there', '#### [L-277] The L-192 site store'),
    ]
    for label, needle in checks:
        hit = needle in disk
        print('  %-20s %s' % (label, hit))
        if not hit:
            ok = False

    # Every header must be a FOUR-hash line. An off-by-one here produced a
    # three-hash header once before, and the indexer silently skipped the
    # block while reporting a clean pass. (L-269 session, 2026-08-30.)
    for handle in ('L-278', 'L-279'):
        bad = ('### [%s]' % handle) in disk and ('#### [%s]' % handle) not in disk
        print('  %-20s %s' % ('%s four-hash' % handle, not bad))
        if bad:
            ok = False

    # The old L-254 and L-267 metadata dates must be GONE, not merely
    # accompanied by the new ones.
    for label, needle in [('old L-254 date gone', '<!-- L:254 status:OPEN upd:2026-08-26'),
                          ('old L-267 date gone', '<!-- L:267 status:OPEN upd:2026-08-30')]:
        gone = needle not in disk
        print('  %-20s %s' % (label, gone))
        if not gone:
            ok = False

    if not ok:
        print('')
        print('POST-CONDITION FAILED. Undo is Discard Changes in GitHub Desktop.')
        sys.exit(1)

    print('')
    print('DONE. L-254 and L-267 amended, L-278 and L-279 opened.')
    print('')
    print('Next: run the maintenance runner. ledger_index.py rebuilds the')
    print('INDEX; expect 274 blocks and two more live items than last run.')
    print('Then commit and push, and the handoff can carry the new SHA.')


if __name__ == '__main__':
    main()
