"""
patch_L265_267_stage_c_close.py -- close L-265, record Stage C on L-267,
and bring the master plan's status line up to date.

Built on orrery 019bf724672bb3d71e803eb80dc00a16d07abd78 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Gallery state described: 98cc99bd865feaea3c0e7ad7c3ad9b07db5e5ea8 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.

WHAT IT DOES

  LEDGER_CONSOLIDATED.md
    1. L-265 -> DONE. Its block MOVES from section A to the end of
       section C (closed items migrate there and stay), with a closing
       paragraph prepended: the 22 links are curated, served, and shown
       in the Sun exhibit's i panel. One (decide) it carried -- whether
       the eighteen `*_info` strings stay in the desktop GUI -- is named
       as carried, not closed.
    2. L-267 amended: Stage C shipped 2026-09-03 across three gallery
       patches, Mode 5 passed at gallery 98cc99bd; the "NOT started"
       paragraph is replaced. Two findings recorded: the i button had
       never been wired on the Sun path since Stage A (the wiring lived
       in initControls, which the Sun never calls), and the mockup's
       open hover-seize defect is answered -- no seize with the panel
       open. Option C for the height, Tony's hand edit to 40/60, and
       the phone pass carried as a Tony-action.

  documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md
    3. Status line v20 -> v21 with one sentence on the Sun GUI; Last
       updated moves to September 3, 2026.

  Builds nothing. The maintenance run regenerates the ledger index and
  MODULE_ATLAS.md afterwards -- expect both to change.

HOW TO RUN
  Save into the ORRERY repo root (the folder holding
  LEDGER_CONSOLIDATED.md), open in VS Code, press Run. Then
  orrery_maintenance_run.py, commit, push.

GUARDS
  Both files fingerprinted (MD5 over LF-normalised content). The L-265
  block is located by its header and must end exactly at the L-266
  header; its own bytes are fingerprinted too, so an edit to that block
  since 019bf724 aborts the run. Every anchor must match exactly once.
  The two files are written together or not at all. No .bak
  (safe-file-editing 1.10); undo is Discard Changes in GitHub Desktop.

Module created: September 3, 2026 with Anthropic's Claude Fable 5.1.
"""

import hashlib
import os
import sys

LEDGER = 'LEDGER_CONSOLIDATED.md'
PLAN = 'documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md'
FILES = {
    LEDGER: 'c95fd739bb5b61b5339213f787992d17',
    PLAN:   '0cf201e5d610b499bae1e0396f1dd3b4',
}
MARKER = 'STAGE C shipped 2026-09-03'

L265_HEAD = '#### [L-265] The i panel carries links, not curated prose\n'
L265_META_OLD = '<!-- L:265 status:OPEN upd:2026-09-03 section:A flag: rice:4/3/90/2 -->\n'
L265_META_NEW = '<!-- L:265 status:DONE upd:2026-09-03 section:C flag: rice:4/3/90/2 -->\n'
L266_HEAD = '#### [L-266] Nothing checks that a cited link still resolves\n'
SECTION_D = '## D. RECONCILED LEDGER -- OPEN\n'

L265_CLOSING = """**CLOSED 2026-09-03.** The 22 curated links ran into `objects_config.json`
via `patch_L265_info_url_curated.py` and were carried into the served
`feature_configs.json` by the cache builder (gallery `197fd963`; 20
`info_url` plus the two-entry `info_urls` array, zero placeholders,
verified against the served file at session start). The Sun exhibit's i
panel shows them from gallery `0edf4bf4` onward (L-267 Stage C): the
focused shell's name and one "Read more at NASA" or "Read more at
Wikipedia" link, read off the trace the renderer stamps it on. All
eighteen Sun groups carry exactly one link each, checked by feeding the
served config through the patched renderer. Mode 5 passed on the live
page 2026-09-03.

One item this row carried is NOT closed by this and is named so it does
not vanish with the row: **Tony-action (decide):** whether the eighteen
`*_info` strings stay in the orrery's own desktop GUI. They are Tier-2
there today and nothing here touches them.

"""

L267_META_OLD = '<!-- L:267 status:OPEN upd:2026-09-02 section:A flag: rice:4/3/85/3 -->\n**AMENDED 2026-09-02 -- Stage B shipped, after a hang.**\n'
L267_META_NEW = """<!-- L:267 status:OPEN upd:2026-09-03 section:A flag: rice:4/3/85/3 -->
**AMENDED 2026-09-03 -- Stage C shipped; the phone pass is what remains.**
"""

L267_STAGE_C_OLD = """STAGE C, the i panel, is NOT started and is blocked on L-265. All twenty
`info_url` values in the served `feature_configs.json` are the
placeholder `https://www.nasa.gov/`, so wiring the panel now would give
every shell the same dead link. Tony's stated preference 2026-09-02 is to
see the info icon working BEFORE the phone and tablet passes, which makes
L-265's curated links the thing standing between here and mobile.
"""

L267_STAGE_C_NEW = """STAGE C shipped 2026-09-03 across three gallery patches, once L-265's
links were in the served file. `patch_L267_4` (gallery `0edf4bf4`): the
i panel follows the focus the way the drawer handle does -- the focused
shell's swatch, name and one link out, over the exhibit description; no
radius, no citation, because the cross marker's hover already carries
those and the panel is not a second copy of it. The link reaches the
page on the trace: `renderShellSet` stamps it in Plotly's `meta`, and
`buildSunDrawer` reads it there, so there is one source for "which link
belongs to this group" rather than a second copy of the label formula.
`patch_L267_5` (`42a906f6`): the i button had NEVER been wired on the
Sun exhibit -- its listener lived inside `initControls()`, which the Sun
path does not call, so from Stage A to Tony's Mode 5 of 2026-09-03 the
button was decoration. Trial 1 found it. The wiring now lives in its own
function that both launch paths call. `patch_L267_6` (`6cfaf318`) and
Tony's hand edit (`98cc99bd`): the panel and the drawer SHARE the height
(Tony's option C) -- while the drawer is open the panel stops at its top
edge, measured, so no row, GO or All / none is covered; drawer 40%,
panel 60%, set by hand.

MODE 5 PASSED, Tony, 2026-09-03, on the live page, desktop: the panel
opens and closes; shows Core with its Wikipedia link, the link opens in a
new tab and the page still responds; switches to the Alfven surface and
its NASA link while open; keeps the name and link when the focused shell
is unticked. Panel open, markers hovered and the scene rotated: NO SEIZE.
That answers the study's open defect from 2026-08-30 -- the seize was
most likely the L-278 click re-entry, and the study's `hovermode: false`
workaround was deliberately NOT ported (Stage B found that exact relayout
throws inside Plotly and takes `viewInitial` with it).

Two lessons, both already in the protocol and both missed here. The
Stage C test proved the panel's CONTENTS were right and never asked
whether the panel could OPEN -- Verify Execution, Not Appearance, on the
page's own chrome. And "nothing focused" is a state the live page never
reaches, because arrival focuses the outermost shell drawn; the "Focus a
shell" text is correct and unreachable. Not a defect; noted so nobody
hunts for it.

**Tony-action (do):** the portrait pass on a phone -- Stages A, B and C
are all unverified on a small screen, and the 40/60 split was chosen on a
desktop. Carried from L-260.

"""

PLAN_STATUS_OLD = """**Status:** v20 -- Phase 2 (solar system assembler) BUILD UNDERWAY;
**the first feature-bearing exhibit is LIVE.** The Sun ships at
`palomasorrery.com/interactive.html?exhibit=sun`, unlinked from the
landing page, Mode 5 accepted 2026-08-29 (gallery `ac9a5c7b`).
"""
PLAN_STATUS_NEW = """**Status:** v21 -- Phase 2 (solar system assembler) BUILD UNDERWAY;
**the first feature-bearing exhibit is LIVE.** The Sun ships at
`palomasorrery.com/interactive.html?exhibit=sun`, unlinked from the
landing page, Mode 5 accepted 2026-08-29 (gallery `ac9a5c7b`). Its GUI
(L-267) is complete on desktop as of 2026-09-03 (gallery `98cc99bd`): a
drawer replaces the legend, cross markers and rows move the camera, and
the i panel follows the focus and carries each shell's curated link
(L-265, DONE). The phone pass is the one thing carried.
"""
PLAN_DATE_OLD = '**Last updated:** August 23, 2026\n'
PLAN_DATE_NEW = '**Last updated:** September 3, 2026\n'


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


def check_base(path):
    if not os.path.exists(path):
        fail('%s not found. Run this from the ORRERY repo root.' % path)
    content, was_crlf = read_lf(path)
    actual = hashlib.md5(content).hexdigest()
    if actual != FILES[path]:
        fail('BASE MOVED for %s.\n  expected %s\n  found    %s\n'
             '  Built against orrery 019bf724. A size delta of about one\n'
             '  byte per line is CRLF, not content.' % (path, FILES[path], actual))
    print('  %-48s fingerprint matches%s' % (path, ' [CRLF]' if was_crlf else ''))
    return content, was_crlf


def replace_once(content, old, new, label):
    for s in (old, new):
        try:
            s.encode('ascii')
        except UnicodeEncodeError as exc:
            fail('%s: non-ASCII in edit text: %s' % (label, exc))
    a = old.encode('ascii')
    n = content.count(a)
    if n != 1:
        fail('%s: anchor matched %d times (expected 1):\n  %r' % (label, n, old[:70]))
    print('  %-48s anchor verified' % label)
    return content.replace(a, new.encode('ascii'))


def main():
    print('patch_L265_267 -- close L-265, record Stage C, master plan v21')
    print('=' * 66)

    ledger, ledger_crlf = check_base(LEDGER)
    plan, plan_crlf = check_base(PLAN)
    if MARKER.encode('ascii') in ledger:
        fail('%s already carries "%s". This patch has run.' % (LEDGER, MARKER))

    # --- 1. move L-265 to section C -----------------------------------
    h = L265_HEAD.encode('ascii')
    if ledger.count(h) != 1:
        fail('L-265 header matched %d times' % ledger.count(h))
    start = ledger.index(h)
    nxt = ledger.find(b'\n' + L266_HEAD.encode('ascii'), start)
    if nxt < 0:
        fail('L-266 header not found after L-265; block end unknown')
    block = ledger[start:nxt + 1]           # includes trailing newline
    bmd5 = hashlib.md5(block).hexdigest()
    if bmd5 != BLOCK_265_EXPECTED:
        fail('L-265 block has changed since 019bf724 (md5 %s). Re-derive\n'
             '  this patch against the current block.' % bmd5)
    print('  %-48s block located, %d bytes, fingerprint matches'
          % ('L-265 block', len(block)))
    if not block.startswith(h + L265_META_OLD.encode('ascii')):
        fail('L-265 metadata line is not the expected OPEN line')
    new_block = (h + L265_META_NEW.encode('ascii') + L265_CLOSING.encode('ascii')
                 + block[len(h) + len(L265_META_OLD):])
    if not new_block.endswith(b'\n\n'):
        new_block = new_block.rstrip(b'\n') + b'\n\n'
    ledger = ledger[:start] + ledger[nxt + 1:]
    d = SECTION_D.encode('ascii')
    if ledger.count(d) != 1:
        fail('section D header matched %d times' % ledger.count(d))
    di = ledger.index(d)
    # L-276's last line sits directly above section D with no blank line.
    ledger = ledger[:di] + b'\n' + new_block + ledger[di:]
    print('  %-48s moved to the end of section C' % 'L-265')

    # --- 2. amend L-267 -------------------------------------------------
    ledger = replace_once(ledger, L267_META_OLD, L267_META_NEW, 'L-267 metadata + amended line')
    ledger = replace_once(ledger, L267_STAGE_C_OLD, L267_STAGE_C_NEW, 'L-267 Stage C paragraph')

    # --- 3. master plan -------------------------------------------------
    plan = replace_once(plan, PLAN_STATUS_OLD, PLAN_STATUS_NEW, 'master plan status line')
    plan = replace_once(plan, PLAN_DATE_OLD, PLAN_DATE_NEW, 'master plan Last updated')

    # --- write both -----------------------------------------------------
    for path, out, crlf in [(LEDGER, ledger, ledger_crlf), (PLAN, plan, plan_crlf)]:
        with open(path, 'wb') as f:
            f.write(out.replace(b'\n', b'\r\n') if crlf else out)
        print('  wrote %s' % path)

    # --- post-conditions ------------------------------------------------
    print('')
    print('Post-conditions (read back from disk):')
    L = read_lf(LEDGER)[0].decode('utf-8', 'replace')
    P = read_lf(PLAN)[0].decode('utf-8', 'replace')
    a_end = L.index('## C. RECONCILED LEDGER -- DONE')
    d_start = L.index(SECTION_D)
    ok = True
    for label, got, want in [
        ('L-265 header count',            L.count(L265_HEAD), 1),
        ('L-265 is DONE/section C',       L.count(L265_META_NEW), 1),
        ('L-265 sits after section C head', int(L.index(L265_HEAD) > a_end and L.index(L265_HEAD) < d_start), 1),
        ('L-265 gone from section A',     L[:a_end].count(L265_HEAD), 0),
        ('L-266 still present',           L.count(L266_HEAD), 1),
        ('L-267 amended line',            L.count('AMENDED 2026-09-03 -- Stage C shipped'), 1),
        ('L-267 old NOT-started gone',    L.count('STAGE C, the i panel, is NOT started'), 0),
        ('plan is v21',                   P.count('**Status:** v21'), 1),
        ('plan date moved',               P.count(PLAN_DATE_NEW), 1),
    ]:
        print('  %-34s %d (want %d) %s' % (label, got, want, 'ok' if got == want else 'FAIL'))
        if got != want:
            ok = False
    if not ok:
        print('')
        print('POST-CONDITION FAILED. Undo is Discard Changes in GitHub Desktop.')
        sys.exit(1)
    print('')
    print('DONE. Now orrery_maintenance_run.py (it regenerates the ledger index),')
    print('then commit and push.')


BLOCK_265_EXPECTED = '909b45365133cc7a6bce8dae1162c8e4'

if __name__ == '__main__':
    main()
