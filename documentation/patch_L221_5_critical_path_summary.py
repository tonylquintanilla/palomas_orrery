"""patch_L221_5_critical_path_summary.py

Built on 09736422e8b26d348f539cd8b49628e8a0c670ab at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Gallery at 02aefc0cefbf334889b7c6b3b05bf8fdfab74fa6.
Both confirmed by live git ls-remote.
Written August 23, 2026 with Anthropic's Claude Opus 5.

RUN IT LIKE THIS
    Save into documentation/ -- the same folder as the file it edits.
    Open in VS Code, click Run.
    Equivalent command: python patch_L221_5_critical_path_summary.py

Transactional, all-or-nothing, binary I/O. One target:
documentation/MASTER_PLAN_CRITICAL_PATH_SUMMARY.md. Nothing is written
unless every anchor matches exactly once.

WHY THIS PATCH EXISTS

This file is the readable companion to Section 5a, which reached v19
today. It answers "how far to the end," so the braid changes its
central claim, and its figures were read on August 20.

  THE BRAID
     1. Header restamped and the lead rewritten. The old lead
        announced what changed on August 20.
     2. "This is why the provenance work comes first" -- the exact
        sentence the braid overturns.
     4. Step three stops saying that drawing rings is "exactly what
        should not be" done. Drawing and LOCKING are separable, and
        conflating them is what kept the render unbuilt for six weeks.
     5. Step four needs step three plus a thirty-number slice, not
        "all three of the above."
    10. Steps two and three restated at the foot.

  RE-MEASURED AT HEAD
     3. and 6. The corpus: 107 -> 105 claims, and the four routing
        figures with it. Read from WORKSHEET_CHECK.md rather than
        carried. The document spells its numbers out, so these are
        spelled out too.

  TWO CLAIMS THAT WERE TRUE WHEN WRITTEN AND ARE NOT NOW
     7. L-214 is called "designed and unbuilt, and the next scheduled
        work." It went DONE on 2026-08-21, and the next work is now
        L-154.
     8. `STREAMER_BELT_RADII` no longer exists. L-224 renamed it
        HELMET_CUSP_RADII, moved it out of SHELL_CONFIGS, and changed
        its value from 6.0 to 4.0 on a real source. A summary naming a
        constant that is not in the code sends the next reader to grep
        for nothing.

  A CORRECTION TO A CORRECTION
     9. The streamer-belt paragraph exists because this file once
        carried a wrong claim and says so at length. It then states
        DeForest's Alfven surface as "17 R_sun or more." The published
        figure is 15 -- the arXiv abstract page disagrees with its own
        accepted manuscript, and the accepted manuscript wins. Fixed
        on 2026-08-22 in `constants_new.py` (L-209) and not here.
        Recorded rather than silently swapped, on this file's own
        stated principle: a wrong claim in a summary outlives the
        conversation it came from.

  SCAFFOLDING REMOVED
     1. The header carried a delivery instruction -- "Lands in
        documentation/ as MASTER_PLAN_CRITICAL_PATH_SUMMARY.md ... it
        belongs in the repo before either is pushed." It has been in
        the repo for days. An instruction that has been carried out
        reads, to a later session, as one still outstanding.

WHAT IS PERMANENT AND WHAT IS NOT
  The script is disposable; the revised document is not.

AFTER RUNNING
  1. Read the output; every line should say ok.
  2. Commit and push.
  3. Move this script to documentation/.
"""

import hashlib
import os
import sys

BASE_SHA = '09736422e8b26d348f539cd8b49628e8a0c670ab'
GALLERY_SHA = '02aefc0cefbf334889b7c6b3b05bf8fdfab74fa6'
MODEL = "Anthropic's Claude Opus 5"

HERE = os.path.dirname(os.path.abspath(__file__))
TARGET_NAME = 'MASTER_PLAN_CRITICAL_PATH_SUMMARY.md'
FINGERPRINT = '3a51a380ab592371f652907fe7888ae6'


# ==================================================================
# EDIT 1 -- the header: restamp, new lead, scaffolding removed
# ==================================================================

OLD_01 = (
    "**Updated August 20, 2026.** Orrery at\n"
    "`79729c98fd6bec8703fcc3bbc0806e6ee5226770`, gallery at\n"
    "`109162bbb8d291bce615d888557498a9342d4642`. Both confirmed by live\n"
    "check. First written August 16 at `227f5b2d`; the structure below is\n"
    "unchanged from that version -- the five steps have not moved, only\n"
    "our position along them.\n"
    "\n"
    "Two things changed on August 20. The reconciliation queue that had\n"
    "been open for two sessions is CLOSED: four rows decided, three\n"
    "values changed, one held. And a claim this document carried about\n"
    "`STREAMER_BELT_RADII` turned out to be wrong and is corrected below\n"
    "-- it had travelled here from a session reading rather than from a\n"
    "source.\n"
    "\n"
    "**Lands in `documentation/` as `MASTER_PLAN_CRITICAL_PATH_SUMMARY.md`.** Section 5a\n"
    "of the master plan and the readable snapshot both cite it by that exact\n"
    "name, so it belongs in the repo before either is pushed.\n"
    "\n"
)
NEW_01 = (
    "**Updated August 23, 2026.** Orrery at\n"
    "`09736422e8b26d348f539cd8b49628e8a0c670ab`, gallery at\n"
    "`02aefc0cefbf334889b7c6b3b05bf8fdfab74fa6`. Both confirmed against\n"
    "the live remote. First written August 16 at `227f5b2d`; the five\n"
    "steps below still have not moved.\n"
    "\n"
    "**What changed on August 23 is the order they are worked in.**\n"
    "Tony ruled on August 22 that provenance stops being a GATE and\n"
    "becomes a per-artifact slice. Step three -- teaching the assembler\n"
    "to draw -- goes first. Step one continues and stops blocking\n"
    "anything. Section 5a of the master plan carries the same change as\n"
    "of v19, and the argument behind it is in\n"
    "`documentation/DESIGN_NOTE_20260822_braid_and_citation_kind.md`.\n"
    "\n"
    "The short form: a precondition that does not terminate is not a\n"
    "plan. Step one had eight clean rows out of a hundred and five, and\n"
    "a full session on August 22 went to one solar shell that Artifact 2\n"
    "does not render. Priority becomes what the next artifact actually\n"
    "draws.\n"
    "\n"
    "Three claims in this file have also been corrected against the\n"
    "code rather than restated from it. They are marked where they\n"
    "appear.\n"
    "\n"
)


# ==================================================================
# EDIT 2 -- the sentence the braid overturns
# ==================================================================

OLD_02 = (
    "This is why the provenance work comes first. It is not a detour and it\n"
    "is not a parallel project. Its target is the orrery, so that importing\n"
    "from the orrery blind is a safe thing to do.\n"
)
NEW_02 = (
    "This is why the provenance work exists, and why it aims at the orrery\n"
    "rather than anywhere downstream. It is not a detour and it is not a\n"
    "parallel project.\n"
    "\n"
    "**Until August 23 this passage went one sentence further and said the\n"
    "provenance work therefore comes FIRST. That does not follow, and it is\n"
    "withdrawn.** What the asymmetry governs is what may be LOCKED, not what\n"
    "may be BUILT. A fingerprinted artifact freezes its numbers, so it must\n"
    "not be locked on unsourced ones. Drawing a ring on screen freezes\n"
    "nothing, and it can be un-drawn in an afternoon.\n"
    "\n"
    "The order also pays for itself. A ring radius nobody can see can only\n"
    "be checked as text against text. Once the assembler draws it, a wrong\n"
    "radius becomes something a person can look at -- which is this\n"
    "project's own definition of ground truth.\n"
)


# ==================================================================
# EDIT 3 -- step one: the corpus re-measured, the batch re-scoped
# ==================================================================

OLD_03 = (
    "**One. Make the orrery right.** One home for every feature constant,\n"
    "each carrying its source as data rather than as a comment somebody has\n"
    "to trust. Then the verification batches, of which the gas giants are\n"
    "the one Saturn and Jupiter need.\n"
    "\n"
    "The checker, the worksheet builder and the dispatch loop are the\n"
    "machinery of this step, not a step of their own. They exist because\n"
    "reconciling worksheets against the code by hand does not scale, and the\n"
    "scale is measured: 107 claims scored, eight of them clean.\n"
)
NEW_03 = (
    "**One. Make the orrery right.** One home for every feature constant,\n"
    "each carrying its source as data rather than as a comment somebody has\n"
    "to trust. Then the verification batches.\n"
    "\n"
    "**Since August 23 this step is scoped per artifact rather than run to\n"
    "completion.** What Artifact 2 needs is not the gas-giant batch -- that\n"
    "batch is Jupiter, Saturn, Uranus and Neptune, and the last two are not\n"
    "in Artifact 2. It is the slice Artifact 2 renders, and that slice is\n"
    "countable, which is the point of scoping it this way. Saturn's seven\n"
    "rings carry an inner and an outer radius each; Jupiter's four rings add\n"
    "a thickness; the belts carry three distances and one thickness. Thirty\n"
    "measured numbers. Two more are drawing parameters rather than\n"
    "measurements, and are declared as such.\n"
    "\n"
    "The checker, the worksheet builder and the dispatch loop are the\n"
    "machinery of this step, not a step of their own. They exist because\n"
    "reconciling worksheets against the code by hand does not scale, and the\n"
    "scale is measured: a hundred and five claims scored, eight of them\n"
    "clean.\n"
)


# ==================================================================
# EDIT 4 -- step three: drawing and locking are not the same act
# ==================================================================

OLD_04 = (
    "**Three. Teach the assembler to draw.** This one is independent of the\n"
    "first two and could be done tomorrow -- the data is already sitting in\n"
    "the served cache. Two lines in the resolver currently throw away every\n"
    "ring radius one step before anything could use them, and there is no\n"
    "browser code that draws a ring at all.\n"
    "\n"
    "Fixing it today would put Saturn's rings on screen immediately. They\n"
    "would just be rings drawn from unverified numbers, which is exactly what\n"
    "should not be locked into a reference artifact.\n"
)
NEW_04 = (
    "**Three. Teach the assembler to draw. This is the next work.** It is\n"
    "independent of the first two and could be done tomorrow -- the data is\n"
    "already sitting in the served cache. Two lines in the resolver currently\n"
    "throw away every ring radius one step before anything could use them,\n"
    "and there is no browser code that draws a ring at all. Re-checked at\n"
    "gallery `02aefc0` on August 23; both lines still read as described, and\n"
    "nothing in the gallery repo reads the served feature file at all.\n"
    "\n"
    "Fixing it puts Saturn's rings on screen immediately. They will be rings\n"
    "drawn from numbers that are not yet sourced, and **that is fine, because\n"
    "drawing is not locking.** Until August 23 this passage ended by calling\n"
    "it \"exactly what should not be locked into a reference artifact,\" which\n"
    "is true of locking and was being read as an argument against building.\n"
    "The two came apart on August 22 and this is the sentence that had\n"
    "welded them together.\n"
)


# ==================================================================
# EDIT 5 -- step four: what actually gates the lock
# ==================================================================

OLD_05 = (
    "**Four. Lock Artifact 2.** Jupiter and Saturn with rings and radiation\n"
    "belts, fingerprinted as the reference build. It needs all three of the\n"
    "above: sourced values, a faithful copy, and something that can actually\n"
    "render them.\n"
)
NEW_05 = (
    "**Four. Lock Artifact 2.** Jupiter and Saturn with rings, and Jupiter's\n"
    "radiation belts, fingerprinted as the reference build. Saturn has no\n"
    "radiation belts in the served cache or in the config behind it, which\n"
    "the old phrasing here obscured.\n"
    "\n"
    "It needs step three, and it needs step one's thirty-number slice. It\n"
    "does not need the rest of the audit, and it does not need step two --\n"
    "the transport protects a correct orrery from drifting away from its\n"
    "copy later, which is a different problem from locking a correct\n"
    "artifact now.\n"
)


# ==================================================================
# EDIT 6 -- the backlog figures, re-read rather than carried
# ==================================================================

OLD_06 = (
    "**Step one is in progress, the backlog is visible, and the loop has now\n"
    "run end to end.** Of 107\n"
    "verification claims, eight are clean, forty-eight need to go back to\n"
    "whoever filled them in, nineteen need a conversation, thirty-two are\n"
    "noted without a route, and twenty-two are not reachable by the scanner\n"
    "at all. That is not a discouraging result -- it is the first time the\n"
    "number has been knowable. Before the checker existed, the same claims\n"
    "were unexamined and looked fine.\n"
)
NEW_06 = (
    "**Step one is in progress, the backlog is visible, and the loop has now\n"
    "run end to end.** Of a hundred and five verification claims, eight are\n"
    "clean, forty-seven need to go back to whoever filled them in, nineteen\n"
    "need a conversation, thirty-one are noted without a route, and\n"
    "twenty-two are not reachable by the scanner at all. That is not a\n"
    "discouraging result -- it is the first time the number has been\n"
    "knowable. Before the checker existed, the same claims were unexamined\n"
    "and looked fine.\n"
    "\n"
    "(Those figures were read from `WORKSHEET_CHECK.md` on August 23. This\n"
    "file carried 107 / 48 / 32 from the August 20 reading, and the master\n"
    "plan carried 110 from August 19. All three were true when written; none\n"
    "was re-measured before being copied forward, which is how a figure\n"
    "drifts without anyone being wrong on the day.)\n"
)


# ==================================================================
# EDIT 7 -- L-214 was built two days after this sentence was written
# ==================================================================

OLD_07 = (
    "vocabulary. So one of the pilot's most useful results is a\n"
    "measurement of its own instrument. L-214 is designed and unbuilt,\n"
    "and it is the next scheduled work.\n"
)
NEW_07 = (
    "vocabulary. So one of the pilot's most useful results is a\n"
    "measurement of its own instrument. **L-214 was built on August 21**;\n"
    "this file called it \"designed and unbuilt, and the next scheduled\n"
    "work\" until August 23. The next work is now step three.\n"
)


# ==================================================================
# EDIT 8 -- a constant this file names no longer exists
# ==================================================================

OLD_08 = (
    "from centre (L-209). And `STREAMER_BELT_RADII` carried a citation that\n"
    "did not support the claim attached to it (L-210).\n"
)
NEW_08 = (
    "from centre (L-209). And `STREAMER_BELT_RADII` carried a citation that\n"
    "did not support the claim attached to it (L-210).\n"
    "\n"
    "**That constant no longer exists, as of August 22.** L-224 renamed it\n"
    "`HELMET_CUSP_RADII`, moved it out of the shell configuration into the\n"
    "Sun's custom shells, and changed its value from 6.0 to 4.0 on a real\n"
    "source -- Suess and Nerney (2004), on the extent of the closed-field\n"
    "helmet rather than of the streamer as a whole. The shell it draws is\n"
    "now a warped band with a stalk, not a sphere. The name is left in the\n"
    "sentences above because those describe what was found on August 20,\n"
    "under the name it had then; a reader grepping for it today will not\n"
    "find it.\n"
)


# ==================================================================
# EDIT 9 -- the correction paragraph needed correcting
# ==================================================================

OLD_09 = (
    "which is neither a floor nor a ceiling on streamer extent, and that\n"
    "paper's streamer-belt result is an Alfven surface at 17 R_sun or\n"
    "more -- a result that belongs to `ALFVEN_SURFACE_RADII`, not here.\n"
)
NEW_09 = (
    "which is neither a floor nor a ceiling on streamer extent, and that\n"
    "paper's streamer-belt result is an Alfven surface at 15 R_sun or\n"
    "more -- a result that belongs to `ALFVEN_SURFACE_RADII`, not here.\n"
    "\n"
    "**And that figure was wrong too, in the sentence written to fix the\n"
    "first error.** It read 17 R_sun until August 23. The published value\n"
    "is 15: the paper's arXiv abstract page disagrees with its own accepted\n"
    "manuscript, and the manuscript is what the figure comes from. Corrected\n"
    "in `constants_new.py` on August 22 under L-209, and only now here --\n"
    "which is the more interesting half. A correction written into the code\n"
    "does not travel to the prose that describes it unless somebody carries\n"
    "it, and nobody is assigned to.\n"
)


# ==================================================================
# EDIT 10 -- steps two and three at the foot
# ==================================================================

OLD_10 = (
    "**Step two is designed, not built.**\n"
    "\n"
    "**Step three has not been started.** It is the smallest piece of work\n"
    "standing between the project and a Saturn that renders.\n"
)
NEW_10 = (
    "**Step two is designed, not built**, and is no longer on the path to\n"
    "Artifact 2.\n"
    "\n"
    "**Step three has not been started, and it is now the next thing that\n"
    "happens.** It remains the smallest piece of work standing between the\n"
    "project and a Saturn that renders. What changed on August 23 is not\n"
    "its size but its position: it used to be the last of three\n"
    "prerequisites and it is now the first.\n"
)


# ==================================================================
# EDIT 11 -- the footer
# ==================================================================

OLD_11 = (
    "*Prepared August 16, 2026 with Anthropic's Claude Opus 5; figures\n"
    "updated August 18, dispatch result added August 19, reconciliation\n"
    "closed and the streamer-belt claim corrected August 20. Built on\n"
    "`79729c98fd6bec8703fcc3bbc0806e6ee5226770` at\n"
    "https://github.com/tonylquintanilla/palomas_orrery, gallery at\n"
    "`109162bbb8d291bce615d888557498a9342d4642`.*\n"
)
NEW_11 = (
    "*Prepared August 16, 2026 with Anthropic's Claude Opus 5; figures\n"
    "updated August 18, dispatch result added August 19, reconciliation\n"
    "closed and the streamer-belt claim corrected August 20. Revised\n"
    "August 23 for the braid ruled August 22: the ordering claim\n"
    "withdrawn, the corpus re-measured at 105, and three claims corrected\n"
    "against the code -- L-214's status, the retired\n"
    "`STREAMER_BELT_RADII`, and DeForest's 15 R_sun. Built on\n"
    "`09736422e8b26d348f539cd8b49628e8a0c670ab` at\n"
    "https://github.com/tonylquintanilla/palomas_orrery, gallery at\n"
    "`02aefc0cefbf334889b7c6b3b05bf8fdfab74fa6`. Both confirmed against\n"
    "the live remote.*\n"
)


EDITS = [
    ('01 header restamped, new lead, scaffolding removed', OLD_01, NEW_01),
    ('02 "provenance comes first" withdrawn', OLD_02, NEW_02),
    ('03 step one scoped per artifact; 107 -> 105', OLD_03, NEW_03),
    ('04 step three: drawing is not locking', OLD_04, NEW_04),
    ('05 step four: what actually gates the lock', OLD_05, NEW_05),
    ('06 backlog figures re-read at HEAD', OLD_06, NEW_06),
    ('07 L-214 was built on August 21', OLD_07, NEW_07),
    ('08 STREAMER_BELT_RADII no longer exists', OLD_08, NEW_08),
    ('09 DeForest 17 -> 15 R_sun', OLD_09, NEW_09),
    ('10 steps two and three restated', OLD_10, NEW_10),
    ('11 footer', OLD_11, NEW_11),
]


def fail(message):
    print('')
    print('ERROR: ' + message)
    print('Nothing was written. The file on disk is untouched.')
    sys.exit(1)


def main():
    target = os.path.join(HERE, TARGET_NAME)
    print('patch_L221_5_critical_path_summary.py')
    print('built on %s' % BASE_SHA)
    print('gallery  %s' % GALLERY_SHA)
    print('target   %s' % target)
    print('')

    if not os.path.exists(target):
        fail('%s not found beside this script.\n'
             '       Save this script into documentation/ -- the same\n'
             '       folder as the file it edits.\n'
             '       It looked in: %s' % (TARGET_NAME, HERE))

    with open(target, 'rb') as handle:
        raw = handle.read()

    normalized = raw.replace(b'\r\n', b'\n')
    got = hashlib.md5(normalized).hexdigest()
    if got != FINGERPRINT:
        fail('BASE MOVED. %s fingerprints %s; this patch was built against '
             '%s. Re-pull at HEAD, or ask for a rebuilt patch.'
             % (TARGET_NAME, got, FINGERPRINT))
    print('[base ok]      fingerprint %s (%d bytes)' % (got, len(raw)))

    is_crlf = b'\r\n' in raw
    print('[endings]      %s -- preserved on write'
          % ('CRLF' if is_crlf else 'LF'))

    text = normalized.decode('utf-8')

    # --- ASCII, both directions -------------------------------------
    pre_existing = sum(1 for ch in text if ord(ch) > 127)
    for label, old, new in EDITS:
        if sum(1 for ch in new if ord(ch) > 127) > \
                sum(1 for ch in old if ord(ch) > 127):
            fail('edit %s would INTRODUCE a non-ASCII character.' % label)
    with open(os.path.abspath(__file__), 'rb') as handle:
        own = handle.read()
    if any(byte > 127 for byte in own):
        fail('this script itself is not pure ASCII.')
    print('[ascii ok]     target holds %d non-ASCII char(s); no edit adds '
          'one; script is ASCII (%d bytes)' % (pre_existing, len(own)))

    # --- Every anchor matches exactly once ---------------------------
    working = text
    for label, old, new in EDITS:
        count = working.count(old)
        if count != 1:
            fail('ANCHOR FAIL on edit %s -- expected exactly 1 match, found '
                 '%d. First 70 chars: %r' % (label, count, old[:70]))
        working = working.replace(old, new, 1)
        print('[ok]           %s' % label)

    # --- No line vanishes that no edit claims to rewrite -------------
    allowed = set()
    for _label, old, new in EDITS:
        allowed.update(l for l in (set(old.split('\n')) - set(new.split('\n')))
                       if l)
    after = set(working.split('\n'))
    lost = [l for l in text.split('\n') if l and l not in after]
    unexpected = [l for l in lost if l not in allowed]
    if unexpected:
        fail('%d line(s) would be lost that no edit claims to rewrite. '
             'First: %r' % (len(unexpected), unexpected[0]))
    print('[addition ok]  %d line(s) rewritten, all accounted for'
          % len(lost))

    # --- A check that can fail: the stale figures must be GONE -------
    # Success carries evidence. Each string below is one this patch
    # exists to remove; if any survives, an edit landed somewhere it
    # should not have.
    must_be_gone = [
        'Updated August 20, 2026',
        '107 claims scored',
        'Of 107',
        'forty-eight need to go back',
        'thirty-two are',
        'L-214 is designed and unbuilt',
        '17 R_sun or',
        'This is why the provenance work comes first',
        'Lands in `documentation/`',
        '79729c98fd6bec8703fcc3bbc0806e6ee5226770',
    ]
    survivors = [s for s in must_be_gone if s in working]
    if survivors:
        fail('%d stale string(s) survived the patch: %r'
             % (len(survivors), survivors))
    print('[stale gone]   all %d targeted stale strings removed'
          % len(must_be_gone))

    out = working.encode('utf-8')
    if is_crlf:
        out = out.replace(b'\n', b'\r\n')
    with open(target, 'wb') as handle:
        handle.write(out)

    print('')
    print('patch applied (%d bytes -> %d bytes, %d edits)'
          % (len(raw), len(out), len(EDITS)))
    print('')
    print('CURRENCY STAMP UPDATED (Stamp What You Change, '
          'safe-file-editing 1.7):')
    print('  header  Updated August 20 -> August 23, 2026; both SHAs')
    print('  footer  revision line naming the braid and the three')
    print('          corrections, both SHAs')
    print('')
    print('NEXT:')
    print('  1. Commit and push.')
    print('  2. Move this script to documentation/.')


if __name__ == '__main__':
    main()
