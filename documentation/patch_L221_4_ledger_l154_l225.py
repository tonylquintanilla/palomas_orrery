"""patch_L221_4_ledger_l154_l225.py

Built on ce2ff5d15d4e2bb682d5603c3b945a6f0f5f8ff4 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Gallery at 02aefc0cefbf334889b7c6b3b05bf8fdfab74fa6.
Both confirmed by live git ls-remote.
Written August 23, 2026 with Anthropic's Claude Opus 5.

RUN IT LIKE THIS
    Save into the REPO ROOT -- the folder holding LEDGER_CONSOLIDATED.md
    and ledger_index.py, NOT documentation/. Open in VS Code, click Run.
    Equivalent command: python patch_L221_4_ledger_l154_l225.py
    (This one differs from patches 2 and 3, which lived in
    documentation/ because their targets did. The target here is at the
    root. The script resolves it beside itself and aborts clearly if it
    is in the wrong folder.)

Transactional, all-or-nothing, binary I/O. One target:
LEDGER_CONSOLIDATED.md. Nothing is written unless every anchor matches
exactly once.

WHY THIS PATCH EXISTS

The master plan reached v19 on 2026-08-23 and now asserts two things
the ledger contradicts. The plan carries SEQUENCING authority and the
ledger carries STATUS authority (L-221), so the plan may reorder the
work and may NOT quietly restate an item's status. This patch makes the
ledger say what was actually decided.

  EDIT 1 -- L-154 is no longer BLOCKED.
    status:BLOCKED -> status:OPEN, upd 2026-08-07 -> 2026-08-23.
    L-154 is the gallery feature-rendering layer: segment 3 of the
    critical path, and under the braid it is the FIRST work rather
    than work waiting on the provenance cluster.

  EDIT 2 -- the "Blocked on" bullet is superseded, not deleted.
    It reads "data/scoring settled before this gets built, not the
    other way around," which is exactly the sentence the braid
    reverses. The ledger's convention is that a reversal is RECORDED,
    so the bullet stays and gains a superseded-by line under it. A
    deleted blocker leaves the next reader unable to see that the
    question was ever decided differently.

  EDIT 3 -- L-225 gets a ledger entry.
    It had none. The highest handle was L-224, while the design note
    of 2026-08-22 cites L-225 four times and the session queue carries
    it as deferred-with-shape-settled. That is the floating-item
    failure the ledger exists to prevent: capture on first mention.
    Opened in section A as DEFERRED, carrying the shape already
    settled -- including that patch_L225_1_dispatch_request.py is
    WITHDRAWN, which is the kind of fact that otherwise resurfaces
    from a stale copy of a design note.

  EDIT 4 -- header currency stamp.

A PROPOSED RICE SCORE, NOT A SETTLED ONE
  L-225 is scored rice:2/3/80/2 -> 2.4, tagged **Note:** in the entry
  so it reads as Claude's proposal rather than as Tony's ruling (the
  skill is explicit that **Tony:** is never a label Claude applies to
  its own text). Reasoning: Reach 2 because it touches one shell
  family; Impact 3 because an unmigrated constant is invisible to the
  request builder and so cannot be dispatched at all; Confidence 80
  because the shape is settled but the dispatch outcome is not; Effort
  2 because the migration is mechanical and the dispatch is a known
  loop. Redirect it and re-run ledger_index.py; nothing else depends
  on the number.

WHAT IS PERMANENT AND WHAT IS NOT
  The script is disposable. The two status facts and the new L-225
  entry are permanent.

AFTER RUNNING
  1. python ledger_index.py        (regenerates the INDEX zone -- the
                                    index is GENERATED from the detail
                                    blocks and will disagree until this
                                    is run)
  2. Commit and push.
  3. Move this script to documentation/.
"""

import hashlib
import os
import sys

BASE_SHA = 'ce2ff5d15d4e2bb682d5603c3b945a6f0f5f8ff4'
GALLERY_SHA = '02aefc0cefbf334889b7c6b3b05bf8fdfab74fa6'
MODEL = "Anthropic's Claude Opus 5"

HERE = os.path.dirname(os.path.abspath(__file__))
LEDGER = 'LEDGER_CONSOLIDATED.md'
FINGERPRINT = '86886abebb2dfa10f96abe5125354909'


# ==================================================================
# EDIT 1 -- L-154 status line
# ==================================================================

OLD_1 = (
    "<!-- L:154 status:BLOCKED upd:2026-08-07 section:W.Active flag: "
    "rice:3/3/70/3 -->\n"
)
NEW_1 = (
    "<!-- L:154 status:OPEN upd:2026-08-23 section:W.Active flag: "
    "rice:3/3/70/3 -->\n"
)


# ==================================================================
# EDIT 2 -- the blocker is superseded, and stays visible
# ==================================================================

OLD_2 = (
    "- **Blocked on:** the L-155-162 provenance-scoring cluster below (data/\n"
    "  scoring settled before this gets built, not the other way around).\n"
)
NEW_2 = (
    "- **Blocked on:** the L-155-162 provenance-scoring cluster below (data/\n"
    "  scoring settled before this gets built, not the other way around).\n"
    "- **SUPERSEDED 2026-08-23 -- the bullet above is reversed, and left in\n"
    "  place because it was the standing rule for six weeks.** Tony's\n"
    "  ruling of 2026-08-22 (the braid): provenance stops being a GATE and\n"
    "  becomes a per-artifact slice, and this item is the FIRST work rather\n"
    "  than the last. Status moved BLOCKED -> OPEN the same day. Three\n"
    "  reasons, in the order they carry weight. (a) Nothing in the\n"
    "  provenance cluster changes a line of this item's code -- the\n"
    "  resolver discards parameters regardless of whether the values behind\n"
    "  them are sourced. (b) A ring drawn from an unsourced number freezes\n"
    "  nothing; only a FINGERPRINTED artifact does, so the sourcing\n"
    "  requirement belongs to L-080/Artifact 2 and not here. (c) Until this\n"
    "  is built, ring provenance is text checked against text -- once it\n"
    "  draws, a wrong radius becomes something Tony's eyes can catch, which\n"
    "  is this project's own ground truth. Verified again at gallery\n"
    "  `02aefc0` on 2026-08-23: `resolver.py` line 133 still reads\n"
    "  `tuple(rec.get(\"features\") or ())`, `models.py` line 91 still types\n"
    "  the field `Tuple[str, ...]` to match, and nothing in the gallery repo\n"
    "  reads `feature_configs.json` -- only the builder writes it. Fourth\n"
    "  independent verification, fourth different HEAD.\n"
    "  **Ref:** `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md` Section\n"
    "  5a, \"The order of execution\" (v19); "
    "`documentation/DESIGN_NOTE_20260822_braid_and_citation_kind.md`\n"
    "  Section 1; L-221 (sequencing authority).\n"
)


# ==================================================================
# EDIT 3 -- L-225 opened, immediately after L-224 in section A
# ==================================================================

OLD_3 = (
    "L-210 (the withdrawn range and the held 6.0 this replaces); L-209 (the\n"
    "Alfven surface it dissolves across); L-221 (the ruling that sequenced\n"
    "it); `orrery-coding-conventions` (single info marker, marker\n"
    "separation for near-equal radii, hover AU convention).\n"
    "\n"
    "## PENDING ACTION (Tony-side)\n"
)
NEW_3 = (
    "L-210 (the withdrawn range and the held 6.0 this replaces); L-209 (the\n"
    "Alfven surface it dissolves across); L-221 (the ruling that sequenced\n"
    "it); `orrery-coding-conventions` (single info marker, marker\n"
    "separation for near-equal radii, hover AU convention).\n"
    "\n"
    "#### [L-225] Migrate the comet shell constants into "
    "`constants_new.py`, then dispatch\n"
    "<!-- L:225 status:DEFERRED upd:2026-08-23 section:A flag: "
    "rice:2/3/80/2 -->\n"
    "- **Opened 2026-08-23, and late.** The design note of 2026-08-22 cites\n"
    "  L-225 four times and the session queue carried it as\n"
    "  deferred-with-shape-settled, but no ledger entry existed -- the\n"
    "  highest handle was L-224. Surfaced by the v19 full-document sweep.\n"
    "  Recorded here rather than quietly created, because \"capture on first\n"
    "  mention\" exists precisely so a handle cannot be in circulation while\n"
    "  the ledger has never heard of it.\n"
    "- **What.** `MAPS_DISINTEGRATION_RADII` and its siblings live in\n"
    "  `comet_visualization_shells.py`, which is outside the tree\n"
    "  `worksheet_request_builder` reaches. A constant the builder cannot\n"
    "  see cannot be put in a worksheet, so it cannot be dispatched, so it\n"
    "  can never be cleared -- it is invisible to the loop rather than\n"
    "  merely unscored. Migrate them into `constants_new.py`, where the\n"
    "  builder already reaches, and only then dispatch.\n"
    "- **This is the No Shadow Constants rule [CRITICAL] applied to a\n"
    "  specific file**, not a new decision. The migration is the work; the\n"
    "  dispatch is the follow-on.\n"
    "- **`patch_L225_1_dispatch_request.py` is WITHDRAWN. Do not run it.**\n"
    "  It dispatched against the constants in their current home and so\n"
    "  would have asked for verdicts on rows that cannot be written back.\n"
    "  Recorded here because a withdrawn script is exactly the kind of fact\n"
    "  that resurfaces from a stale copy of a design note.\n"
    "- **Part A must go out blind.** The dispatch carries a Claude proposal,\n"
    "  so it splits into two physical dispatches under the Two-Dispatch Rule\n"
    "  [CRITICAL] (`provenance-discipline` 2.6, section 2.6): Part A sent\n"
    "  alone, the answer collected, then Part B. Sending them together lets\n"
    "  the proposal contaminate the answer, which is a check that cannot\n"
    "  fail. The questions themselves are in the design note, Section 4.\n"
    "- **Note:** RICE 2/3/80/2 -> 2.4 is Claude's proposed score, not a\n"
    "  ruling. Reach 2 (one shell family), Impact 3 (an unmigrated constant\n"
    "  is invisible to the builder, not merely unscored), Confidence 80\n"
    "  (shape settled, dispatch outcome not), Effort 2 (mechanical migration\n"
    "  plus a known loop). **Tony-action (decide):** confirm or redirect,\n"
    "  then re-run `ledger_index.py`.\n"
    "- **Gap:** the migration is not written. Deferred deliberately -- the\n"
    "  braid puts L-154 and Artifact 2's thirty-number slice ahead of it,\n"
    "  and these constants are not in Artifact 2.\n"
    "- **Ref:** `comet_visualization_shells.py`; `constants_new.py`;\n"
    "  `worksheet_request_builder`;\n"
    "  `documentation/DESIGN_NOTE_20260822_braid_and_citation_kind.md`\n"
    "  Section 4; `provenance-discipline` 2.6; L-221 (sequencing authority);\n"
    "  L-224 (the session that surfaced it).\n"
    "\n"
    "## PENDING ACTION (Tony-side)\n"
)


# ==================================================================
# EDIT 4 -- header currency stamp
# ==================================================================

OLD_4 = (
    "Module updated: August 20, 2026 with Anthropic's Claude Opus 5 (L-222:\n"
    "docstring lines in the constants change report), built on 762aa5dd.\n"
)
NEW_4 = (
    "Module updated: August 20, 2026 with Anthropic's Claude Opus 5 (L-222:\n"
    "docstring lines in the constants change report), built on 762aa5dd.\n"
    "Module updated: August 23, 2026 with Anthropic's Claude Opus 5 (L-154\n"
    "BLOCKED -> OPEN under the braid; L-225 opened, having been in\n"
    "circulation with no entry), built on ce2ff5d1.\n"
)


EDITS = [
    ('1 L-154 status BLOCKED -> OPEN', OLD_1, NEW_1),
    ('2 L-154 blocker superseded, left visible', OLD_2, NEW_2),
    ('3 L-225 opened in section A', OLD_3, NEW_3),
    ('4 header currency stamp', OLD_4, NEW_4),
]


def fail(message):
    print('')
    print('ERROR: ' + message)
    print('Nothing was written. The file on disk is untouched.')
    sys.exit(1)


def main():
    target = os.path.join(HERE, LEDGER)
    print('patch_L221_4_ledger_l154_l225.py')
    print('built on %s' % BASE_SHA)
    print('gallery  %s' % GALLERY_SHA)
    print('target   %s' % target)
    print('')

    if not os.path.exists(target):
        fail('%s not found beside this script.\n'
             '       This one goes in the REPO ROOT, not documentation/ --\n'
             '       the folder that holds LEDGER_CONSOLIDATED.md and\n'
             '       ledger_index.py.\n'
             '       It looked in: %s' % (LEDGER, HERE))

    with open(target, 'rb') as handle:
        raw = handle.read()

    # --- Gate 1: is this the file we built against? ------------------
    normalized = raw.replace(b'\r\n', b'\n')
    got = hashlib.md5(normalized).hexdigest()
    if got != FINGERPRINT:
        fail('BASE MOVED. %s fingerprints %s; this patch was built against '
             '%s. Re-pull at HEAD, or ask for a rebuilt patch.'
             % (LEDGER, got, FINGERPRINT))
    print('[base ok]      fingerprint %s (%d bytes)' % (got, len(raw)))

    is_crlf = b'\r\n' in raw
    print('[endings]      %s -- preserved on write'
          % ('CRLF' if is_crlf else 'LF'))

    # --- Gate 2: the ledger is ASCII and stays that way --------------
    text = normalized.decode('utf-8')
    pre_existing = sum(1 for ch in text if ord(ch) > 127)
    if pre_existing:
        print('[note]         %s already holds %d non-ASCII character(s)'
              % (LEDGER, pre_existing))
    for label, old, new in EDITS:
        if sum(1 for ch in new if ord(ch) > 127) > \
                sum(1 for ch in old if ord(ch) > 127):
            fail('edit %s would INTRODUCE a non-ASCII character.' % label)
    with open(os.path.abspath(__file__), 'rb') as handle:
        own = handle.read()
    if any(byte > 127 for byte in own):
        fail('this script itself is not pure ASCII.')
    print('[ascii ok]     no edit introduces non-ASCII; script itself is '
          'ASCII (%d bytes)' % len(own))

    # --- Gate 3: the handle must not already exist -------------------
    # A check that CAN fail: if L-225 were somehow present, appending a
    # second entry would create a duplicate handle, which the ID
    # convention forbids and ledger_index.py would silently tolerate.
    if '<!-- L:225 ' in text:
        fail('L-225 already has an index comment in %s. This patch would '
             'create a duplicate handle. Re-read the ledger.' % LEDGER)
    print('[handle ok]    L-225 is absent, as expected -- no duplicate')

    # --- Gate 4: every anchor matches exactly once -------------------
    working = text
    for label, old, new in EDITS:
        count = working.count(old)
        if count != 1:
            fail('ANCHOR FAIL on edit %s -- expected exactly 1 match, found '
                 '%d. First 70 chars: %r' % (label, count, old[:70]))
        working = working.replace(old, new, 1)
        print('[ok]           %s' % label)

    # --- Gate 5: this patch only ADDS; nothing may be lost -----------
    # Every edit here is an insertion or a status-line swap, so the only
    # permitted losses are the two status-line variants.
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
    print('[addition ok]  %d line(s) rewritten, all accounted for; '
          '%d line(s) added' % (len(lost),
                                len(working.split('\n')) -
                                len(text.split('\n'))))

    # --- Write, all or nothing --------------------------------------
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
    print('  %s  -- new "Module updated" line, %s, built on %s'
          % (LEDGER, MODEL, BASE_SHA[:8]))
    print('')
    print('NEXT, in this order:')
    print('  1. python ledger_index.py')
    print('     The INDEX zone is GENERATED from the detail blocks and is')
    print('     now out of step -- it still shows L-154 as BLOCKED and has')
    print('     never heard of L-225. This is the step that fixes that.')
    print('  2. Commit and push.')
    print('  3. Move this script to documentation/.')
    print('')
    print('OPEN FOR TONY:')
    print('  - L-225 carries a PROPOSED RICE of 2/3/80/2 (score 2.4).')
    print('    Confirm or redirect, then re-run ledger_index.py.')


if __name__ == '__main__':
    main()
