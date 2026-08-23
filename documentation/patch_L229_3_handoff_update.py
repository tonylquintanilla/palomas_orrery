"""patch_L229_3_handoff_update.py

Built on bd93ef0530a3e1097933a1d52d964ee31ade41b6 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Gallery at 8ec4f261013f09697d649efd25c8a746bffeff64.
Written August 23, 2026 with Anthropic's Claude Opus 5.

RUN IT LIKE THIS
    Save into the REPO ROOT. Open in VS Code, click Run.
    It edits documentation/HANDOFF_20260823_braid_and_v19.md.

Transactional, all-or-nothing, binary I/O. One target.

WHY THIS PATCH EXISTS

The handoff was written and committed at `15741822`. The session then
ran on for four more ledger items, a second skill bump, and a
correction to one of its own patches. A handoff describing a state four
commits behind is the exact drift this project's anchors exist to stop,
and it is the FIRST thing the next session reads.

WHAT IT UPDATES

  1. The anchor block: pushed at `bd93ef05`, not `15741822`.
  2. A new section for the four items opened after the handoff was
     written -- L-226, L-227, L-228, L-229 -- and the Mode 5 pass.
  3. Skills: `orrery-coding-conventions` 1.4 -> 1.5 joins
     `safe-file-editing` 1.7 -> 1.8. TWO carried obligations now, not
     one.
  4. (do)/(decide): the Mode 5 items are discharged, four RICE scores
     await a ruling, and one Mode 5 check is OUTSTANDING -- see below.
  5. Next session: the SHA round trip and the skill confirmations.

THE ONE THING WORTH READING TWICE

  L-224's Mode 5 acceptance was given on the band AS IT WAS DRAWN
  THEN -- lying in the ecliptic plane. L-229 has since rotated it into
  the solar equatorial frame, and that render has NOT been looked at.
  The acceptance predates the change it would have to cover.

  This is not a defect and nothing is wrong on screen; it is a bookkeeping
  fact that would otherwise let a stale approval carry forward. One look
  settles it.

WHAT IS PERMANENT AND WHAT IS NOT
  The script is disposable. The corrected handoff is not.

AFTER RUNNING
  1. Commit and push. No index or maintenance run needed -- this touches
     one markdown file in documentation/ and no generated zone.
  2. Move this script to documentation/.
"""

import hashlib
import os
import sys

BASE_SHA = 'bd93ef0530a3e1097933a1d52d964ee31ade41b6'
GALLERY_SHA = '8ec4f261013f09697d649efd25c8a746bffeff64'

HERE = os.path.dirname(os.path.abspath(__file__))
TARGET = os.path.join('documentation', 'HANDOFF_20260823_braid_and_v19.md')
FINGERPRINT = '757fe6edc4134364b40d8081280fac67'


# ==================================================================
# EDIT 1 -- the anchor
# ==================================================================

OLD_1 = (
    "**Orrery: built on `38923c1cc64d492006135ec77779e1fb592582d5`, pushed at\n"
    "`15741822cb8f54ac26fc252aa8382cd90534570d`**\n"
)
NEW_1 = (
    "**Orrery: built on `38923c1cc64d492006135ec77779e1fb592582d5`, pushed at\n"
    "`bd93ef0530a3e1097933a1d52d964ee31ade41b6`**\n"
    "(this document was first written at `15741822`, four commits back; the\n"
    "session ran on and it was corrected here rather than left describing a\n"
    "state that no longer existed)\n"
)


# ==================================================================
# EDIT 2 -- the four items opened after the handoff was written
# ==================================================================

OLD_2 = (
    "## Skills\n"
    "\n"
    "`safe-file-editing` went **1.7 -> 1.8** this session (L-226). All three\n"
    "stores were reconciled and verified at `15741822`: the skill file\n"
    "declares 1.8, the generated manifest in `PROJECT_INSTRUCTIONS.md` reads\n"
    "1.8, and Tony reinstalled to the account.\n"
    "\n"
    "**CARRIED OBLIGATION.** A mid-session reinstall cannot be verified from\n"
    "inside the session that makes it. This session loaded 1.7, correctly at\n"
    "the time. **The next session confirms its loaded copy reads 1.8 before\n"
    "any file-editing work.**\n"
    "\n"
    "Also loaded and matched: `ledger-and-session-records` 1.8,\n"
    "`gallery-assembler` 1.1. No other bumps.\n"
    "\n"
    "Maintenance last ran clean at `15741822`: 11 of 11 gating checkers, 2\n"
    "report-only (worksheet checker 66 of 105 routed / 8 clean; provenance\n"
    "scanner 292 Tier-1 in the scanned tree).\n"
)
NEW_2 = (
    "## After the handoff was written: Mode 5, and four more items\n"
    "\n"
    "Everything below happened after this document was first committed. It\n"
    "started with Tony putting the render on screen.\n"
    "\n"
    "**MODE 5 PASSED on L-224 and L-209.** The streamer band read as a band\n"
    "with a dissolving stalk -- the saddle visible, the Sun in the trough,\n"
    "no smear, so `fade_exponent` was left alone. The Alfven shell rendered\n"
    "correctly nested inside the 50 R_sun outer corona. Both confirmed by\n"
    "Tony's eyes on 2026-08-23, which is the only gate that counts for\n"
    "either.\n"
    "\n"
    "**Then the render produced three defects that no checker could see.**\n"
    "That is the pattern of the evening and it is worth more than the list.\n"
    "\n"
    "**L-227 -- the hover ran off the screen.** `band_hover` rendered as\n"
    "EIGHT segments, longest 378 characters. It had been wrapped at ~72\n"
    "characters in the SOURCE with `<br>` only between paragraphs; in this\n"
    "file the source wrap and the rendered wrap are one act, and L-224\n"
    "copied the visual habit without the mechanism. Re-flowed to 29\n"
    "segments, longest 63, wording proven identical by stripping every\n"
    "break and comparing. Convention recorded as\n"
    "`orrery-coding-conventions` **1.5**, Hover Line Width Is a Convention,\n"
    "Not an Accident.\n"
    "\n"
    "**L-228 -- three Alfven ranges, none sourced.** `~15-20 R_sun`,\n"
    "`~10-20 solar radii`, and `polar 12-15 | streamer belt 17-19`, all\n"
    "hardcoded in hover strings in one module, under a bare `# Source:`\n"
    "naming Cranmer et al. (2007) with no position. The DRAWN radius is\n"
    "fine -- it interpolates `ALFVEN_SURFACE_RADII` and always has. Tony's\n"
    "rule applies: note a range where it has a citation, use the\n"
    "interpolated constant for the drawing, omit where the citation is\n"
    "insufficient. Open as a source read, with the disposition already\n"
    "decided.\n"
    "\n"
    "**L-229 -- the band was drawn in the wrong plane, and Tony's eye caught\n"
    "it.** He asked whether the belt should lie in the ecliptic rather than\n"
    "the solar equatorial plane. It should not, and the same figure carried\n"
    "the proof: `create_streamer_band_shape` returns points whose docstring\n"
    "says \"body frame\", the caller scaled them with no rotation, and\n"
    "meanwhile the Sun's rotation axis trace -- reading the IAU 2018 pole --\n"
    "was correctly tilted. The axis leaned; the band lay flat. Measured by\n"
    "fitting the point cloud's plane: 0.03 deg before, **7.27 deg after**,\n"
    "and 0.028 deg between the band's normal and the Sun's spin pole. Both\n"
    "traces now read ONE matrix, which matters more than the seven degrees.\n"
    "\n"
    "**And L-229 needed a second patch the same evening, for a mistake of\n"
    "Claude's that is worth keeping.** The first patch justified the\n"
    "rotation with physics -- the heliospheric current sheet, the magnetic\n"
    "equator, the dipole's alignment near solar minimum -- **none of which\n"
    "is sourced anywhere in this project.** Tony asked whether there was a\n"
    "reference for the belt's orientation. There is none: not for the\n"
    "orientation, not for `warp_amp_deg` = 15.0, not for the two-lobe warp,\n"
    "not for the hover's own claim about the 11-year cycle. The rotation is\n"
    "still right, on a ground that needs no physics citation at all: the\n"
    "generator declares body frame, the caller ignored it, and the Sun's\n"
    "body frame is defined by a sourced pole. The physics argument was\n"
    "withdrawn, visibly, and the orientation is now declared an ASSUMPTION\n"
    "in the code and in the hover the reader sees.\n"
    "\n"
    "**A sequencing error, and it is Claude's.** The first L-229 patch was\n"
    "delivered and only then was the sourcing problem raised. Tony ran it\n"
    "before reaching that paragraph, which is entirely reasonable behaviour\n"
    "on a patch that had just been handed over. The rule that failed is not\n"
    "a new one: raise the doubt BEFORE shipping the artifact, because a\n"
    "caveat arriving after a deliverable is a caveat competing with a Run\n"
    "button.\n"
    "\n"
    "---\n"
    "\n"
    "## Skills\n"
    "\n"
    "TWO bumps this session, and **TWO carried obligations**.\n"
    "\n"
    "`safe-file-editing` **1.7 -> 1.8** (L-226): the encoding gate rescoped\n"
    "to say PROSE explicitly, and a new section, The Correction Does Not\n"
    "Travel.\n"
    "\n"
    "`orrery-coding-conventions` **1.4 -> 1.5** (L-227): Hover Line Width Is\n"
    "a Convention, Not an Accident.\n"
    "\n"
    "All three stores reconciled and verified for both: skill files, the\n"
    "generated manifest in `PROJECT_INSTRUCTIONS.md`, and Tony's account\n"
    "install.\n"
    "\n"
    "**CARRIED OBLIGATION.** A mid-session reinstall cannot be verified from\n"
    "inside the session that makes it. This session loaded 1.7 and 1.4, both\n"
    "correct at the time. **The next session confirms its loaded copies read\n"
    "`safe-file-editing` 1.8 and `orrery-coding-conventions` 1.5 before any\n"
    "file-editing or orrery visual work.**\n"
    "\n"
    "Also loaded and matched: `ledger-and-session-records` 1.8,\n"
    "`gallery-assembler` 1.1, `agentic-pre-test` 1.2. No other bumps.\n"
    "\n"
    "Maintenance last ran clean at `bd93ef05`: 11 of 11 gating checkers, 2\n"
    "report-only (worksheet checker 66 of 105 routed / 8 clean; provenance\n"
    "scanner 292 Tier-1 in the scanned tree). The scanner is worth watching\n"
    "here: the L-227 re-flow pushed it to 294 by moving a computed figure\n"
    "out of the citation window, and L-229 brought it back to 292. Predicted\n"
    "in the sandbox each time and confirmed by the run.\n"
)


# ==================================================================
# EDIT 3 -- the do/decide list, rebuilt
# ==================================================================

OLD_3 = (
    "- **(do) Mode 5, carried from 2026-08-22. ONE Sun render closes both\n"
    "  outstanding items.** The streamer band (L-224) should read as a band\n"
    "  with a dissolving stalk, not a smear -- if it smears, raise\n"
    "  `fade_exponent` in `STREAMER_BAND_DEFAULTS`\n"
    "  (`planet_visualization_utilities.py`); that is a parameter, not a\n"
    "  rewrite. And the Alfven shell (L-209) should render one solar radius\n"
    "  larger than before, 18.8 -> 19.7, still nested inside the 50 R_sun\n"
    "  outer corona. L-209's remaining item is explicitly \"Tony's eyes on a\n"
    "  plot, not a build\" -- the code already reads 19.7.\n"
    "- **(decide)** Two proposed RICE scores, both Claude's, both tagged\n"
    "  `**Note:**` so neither reads as a ruling: **L-225** at 2/3/80/2\n"
    "  (score 2.4) and **L-226** at 3/3/90/1 (score 8.1). Confirm or\n"
    "  redirect, then re-run `ledger_index.py`.\n"
)
NEW_3 = (
    "- **(do) ONE Mode 5 check is OUTSTANDING, and it is subtle.** L-224's\n"
    "  acceptance was given on the band AS IT WAS DRAWN THEN -- lying in the\n"
    "  ecliptic. L-229 has since rotated it into the solar equatorial frame,\n"
    "  and THAT render has not been looked at. The approval predates the\n"
    "  change it would have to cover. Nothing is known to be wrong; a stale\n"
    "  approval carrying forward is the risk. One look: the band should lean\n"
    "  WITH the yellow rotation axis, about 7 degrees, rather than lying\n"
    "  flat on the ecliptic grid.\n"
    "- **(do) L-224 and L-209 are ready to close** once that look is done.\n"
    "  Their Mode 5 items passed on 2026-08-23: the band read as a band with\n"
    "  a dissolving stalk, and the Alfven shell nested correctly inside the\n"
    "  outer corona. Both still read OPEN in the ledger.\n"
    "- **(decide)** FOUR proposed RICE scores, all Claude's, all tagged\n"
    "  `**Note:**` so none reads as a ruling: **L-225** 2/3/80/2 (2.4),\n"
    "  **L-226** 3/3/90/1 (8.1), **L-227** 2/2/95/1 (3.8), **L-228**\n"
    "  2/3/60/2 (3.0), **L-229** 3/4/95/1 (11.4). Confirm or redirect, then\n"
    "  re-run `ledger_index.py`.\n"
    "- **(do) L-228 needs a source read** of Cranmer et al. (2007). Claude\n"
    "  cannot clear it by reasoning about it.\n"
    "- **(do) L-229 carries the same shape**: find a citation for the belt's\n"
    "  orientation, or leave it declared. Unlike a range, an orientation\n"
    "  cannot be omitted -- the band has to be drawn somewhere -- so this\n"
    "  falls under Show the Envelope of the Unknowable rather than under\n"
    "  omit-if-unsourced.\n"
)


# ==================================================================
# EDIT 4 -- next session
# ==================================================================

OLD_4 = (
    "**First, three cheap things:**\n"
    "1. Confirm the loaded `safe-file-editing` reads **1.8** (above).\n"
    "2. **L-154's ledger entry does not yet record that its first half\n"
    "   shipped.** It reads OPEN with no build note. One anchor, worth\n"
    "   fixing at session start while it is cheap.\n"
    "3. SHA round trip: orrery `15741822`, gallery `8ec4f261`.\n"
)
NEW_4 = (
    "**First, four cheap things:**\n"
    "1. Confirm the loaded `safe-file-editing` reads **1.8** AND\n"
    "   `orrery-coding-conventions` reads **1.5**. Two obligations, not one.\n"
    "2. **L-154's ledger entry does not yet record that its first half\n"
    "   shipped.** It reads OPEN with no build note. One anchor, worth\n"
    "   fixing at session start while it is cheap.\n"
    "3. SHA round trip: orrery `bd93ef05`, gallery `8ec4f261`.\n"
    "4. The outstanding Mode 5 look at the rotated band, if it has not\n"
    "   happened by then -- see the (do) list above.\n"
)


EDITS = [
    ('1 anchor: pushed at bd93ef05', OLD_1, NEW_1),
    ('2 new section + skills rebuilt (two obligations)', OLD_2, NEW_2),
    ('3 do/decide rebuilt: Mode 5 discharged, one outstanding', OLD_3, NEW_3),
    ('4 next session: four cheap things', OLD_4, NEW_4),
]


def fail(message):
    print('')
    print('ERROR: ' + message)
    print('Nothing was written. The file on disk is untouched.')
    sys.exit(1)


def main():
    path = os.path.join(HERE, TARGET)
    print('patch_L229_3_handoff_update.py')
    print('built on %s' % BASE_SHA)
    print('target   %s' % path)
    print('')

    if not os.path.exists(path):
        fail('%s not found. This script goes in the REPO ROOT and edits a '
             'file under documentation/. It looked in: %s' % (TARGET, HERE))

    with open(path, 'rb') as handle:
        raw = handle.read()

    normalized = raw.replace(b'\r\n', b'\n')
    got = hashlib.md5(normalized).hexdigest()
    if got != FINGERPRINT:
        fail('BASE MOVED. %s fingerprints %s; built against %s.'
             % (TARGET, got, FINGERPRINT))
    print('[base ok]      fingerprint %s (%d bytes)' % (got, len(raw)))

    is_crlf = b'\r\n' in raw
    print('[endings]      %s -- preserved on write'
          % ('CRLF' if is_crlf else 'LF'))

    for label, old, new in EDITS:
        if sum(1 for ch in new if ord(ch) > 127) > \
                sum(1 for ch in old if ord(ch) > 127):
            fail('edit %s would INTRODUCE a non-ASCII character.' % label)
    with open(os.path.abspath(__file__), 'rb') as handle:
        own = handle.read()
    if any(byte > 127 for byte in own):
        fail('this script itself is not pure ASCII.')
    print('[ascii ok]     no edit introduces non-ASCII; script is ASCII '
          '(%d bytes)' % len(own))

    working = normalized.decode('utf-8')
    for label, old, new in EDITS:
        count = working.count(old)
        if count != 1:
            fail('ANCHOR FAIL on edit %s -- expected 1 match, found %d. '
                 'First 70 chars: %r' % (label, count, old[:70]))
        working = working.replace(old, new, 1)
        print('[ok]           %s' % label)

    allowed = set()
    for _label, old, new in EDITS:
        allowed.update(l for l in (set(old.split('\n')) - set(new.split('\n')))
                       if l)
    after = set(working.split('\n'))
    lost = [l for l in working.split('\n') if False]
    lost = [l for l in normalized.decode('utf-8').split('\n')
            if l and l not in after]
    unexpected = [l for l in lost if l not in allowed]
    if unexpected:
        fail('%d line(s) would be lost that no edit claims to rewrite. '
             'First: %r' % (len(unexpected), unexpected[0]))
    print('[addition ok]  %d line(s) rewritten, all accounted for' % len(lost))

    # --- A check that can fail: the stale anchor must be GONE --------
    if '`15741822cb8f54ac26fc252aa8382cd90534570d`**' in working:
        fail('the stale pushed-at anchor survives.')
    for token in ('bd93ef0530a3e1097933a1d52d964ee31ade41b6',
                  'orrery-coding-conventions` reads **1.5**',
                  'OUTSTANDING, and it is subtle'):
        if token not in working:
            fail('expected content did not land: %r' % token[:50])
    print('[currency ok]  stale anchor gone; new anchor, second skill '
          'obligation and the outstanding Mode 5 all present')

    out = working.encode('ascii')
    if is_crlf:
        out = out.replace(b'\n', b'\r\n')
    with open(path, 'wb') as handle:
        handle.write(out)

    print('[written]      %s  %d -> %d bytes' % (TARGET, len(raw), len(out)))
    print('')
    print('patch applied -- %d edits' % len(EDITS))
    print('')
    print('NEXT:')
    print('  1. Commit and push. No index or maintenance run needed --')
    print('     one markdown file, no generated zone.')
    print('  2. Move this script to documentation/.')
    print('')
    print('THE ONE THING WORTH READING TWICE:')
    print('  L-224 was Mode 5 accepted on the band as it was drawn THEN,')
    print('  flat in the ecliptic. L-229 has since rotated it, and that')
    print('  render has not been seen. Nothing is known to be wrong; the')
    print('  risk is a stale approval carrying forward. One look settles')
    print('  it -- the band should lean WITH the yellow axis.')


if __name__ == '__main__':
    main()
