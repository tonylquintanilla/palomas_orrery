"""Skill + ledger patch -- safe-file-editing 1.4 -> 1.5 (Stamp What You
Change), L-220 opened, L-219's target version rebased to 1.6.

RUN COMMAND:  python patch_L220_1_stamp_what_you_change.py

Save this file into the REPO ROOT (the folder holding
LEDGER_CONSOLIDATED.md and skills/), open it in VS Code, and click Run.

Built on 50438c6505e40bb814166cfa2ead086d1986262d at
https://github.com/tonylquintanilla/palomas_orrery (branch main).

WHAT IT DOES -- two files, all-or-nothing across both.
  Edit 1 -- adds Stamp What You Change to safe-file-editing.
  Edit 2 -- bumps that skill 1.4 -> 1.5.
  Edit 3 -- rebases L-219's Gap from "would be 1.5" to "would be 1.6",
            since 1.5 is now spoken for.
  Edit 4 -- inserts L-220 at the end of section A.

THIS SCRIPT DEMONSTRATES ITS OWN RULE. Edit 2 is the currency stamp for
Edit 1: the version line, the history paragraph, the date and the model
attribution all move in the same transaction as the body. A patch that
added the section without Edit 2 would be the exact failure the section
describes.

PURE ADDITION CHECK
  Every line of skill 1.4 must still be present in 1.5, the version
  block excepted. A bump that removes anything aborts.

AFTER IT RUNS
  1. Run ledger_index.py the same way.
  2. Run skills_index.py the same way.
  3. (do) Reinstall safe-file-editing at Settings > Skills.
     The NEXT session confirms its loaded copy reads 1.5 before editing
     existing files. That obligation goes in the handoff.

WHAT IS PERMANENT
  The script is disposable; the skill section and the ledger blocks are
  not. Archive this file to documentation/ once it has run.

SUCCESS   one 'ok' line per edit, 'pure addition confirmed', then
          'patch applied'.
FAILURE   a single 'ERROR:' or 'ANCHOR FAIL' line; NEITHER file is
          written.
"""

import hashlib
import os
import sys

SKILL = os.path.join('skills', 'safe-file-editing', 'SKILL.md')
LEDGER = 'LEDGER_CONSOLIDATED.md'

FINGERPRINTS = {
    SKILL: 'd4987dd231a371ae5eb3b5f6a206d92c',
    LEDGER: 'a9b0b6af6c0b03a5affaccbbe8063da7',
}

SECTION_OLD = b"""## grep -c in && Chains [QUALITY]
"""

SECTION_NEW = b"""### Stamp What You Change [QUALITY]

A patch that edits a file also updates that file's own currency block,
in the SAME transaction as the body. Whichever of these the file
carries: the version line, the anchor SHA, the history or changelog
paragraph, the date, and -- where the change alters what the file DOES
-- the module description at the top.

The stamp names the model that made the change, e.g. "with Anthropic's
Claude Opus 5". Attribution is a partnership value here, and it is also
provenance: a reader can tell whether a human or a model last touched
the header, which matters most when the header is the thing being
trusted.

The patch PRINTS which stamps it updated, so the operator sees it
happened rather than trusting that it did.

**Why it belongs in the patch and nowhere else.** Nobody schedules a
separate pass to re-stamp headers, so a body-only edit leaves the file
describing a state that no longer exists, permanently. The patch is
already fingerprinting the file and already knows the anchor it was
built on. That is the only moment where the stamp is free and correct.
Same reasoning as Fix In Passing, Report It, one field over: the file is
open, the obligation is adjacent, and a separate sweep for it would
never be scheduled.

**The module description is the highest-stakes half.** A stale date
makes a file look older than it is, which is recoverable. A stale
DESCRIPTION misdirects a reader about what the file does -- and in this
project it propagates: `module_atlas.py` builds MODULE_ATLAS.md and
MODULE_INDEX.md from each module's own docstring, and the atlas says so
in its own header ("the source of truth is each module's own docstring
... do not hand-edit it"). So a description left stale after a
behaviour change is not one wrong line; it is a wrong line reproduced
into a generated document that presents itself as current.

(Origin: Tony's rule, 2026-08-20, from the observation that this project
"tends to update the body more than the anchors" -- master plan headers,
module histories and dates drift while their bodies stay current. The
alternative considered and rejected was a generated currency stamp
rebuilt by the maintenance run. It was rejected because it needs its own
generator to maintain, while a stamp written by the patch that caused
the staleness cannot drift: there is no second step to forget.)

## grep -c in && Chains [QUALITY]
"""

VERSION_OLD = b"""Skill version: 1.4 | Cut from palomas_orrery @ a872205 (v1.4), earlier @
1ba20c3 (v1.3), 3398970 (v1.2), bdaaa0c (v1.1) | August 16, 2026
Source: project_instructions_v3_29.md Part 3 + Part 5 technical lessons;
v1.1 adds the delivery-format convention from a same-day incident (a
transactional patch silently never run; see Field Notes). v1.3 adds
Line Endings Are Not Content, earned when a patch aborted twice on a
CRLF working copy whose bytes were identical to the repo's. v1.4 adds
Fix In Passing, Report It, after a patch blocked itself on two Unicode
arrows that predated it by months, and Naming and Archiving a Patch
Script, an unstated convention 96 scripts deep that Tony had been
following alone.
"""

VERSION_NEW = b"""Skill version: 1.5 | Cut from palomas_orrery @ 50438c6 (v1.5), earlier @
a872205 (v1.4), 1ba20c3 (v1.3), 3398970 (v1.2), bdaaa0c (v1.1)
| August 20, 2026, with Anthropic's Claude Opus 5
Source: project_instructions_v3_29.md Part 3 + Part 5 technical lessons;
v1.1 adds the delivery-format convention from a same-day incident (a
transactional patch silently never run; see Field Notes). v1.3 adds
Line Endings Are Not Content, earned when a patch aborted twice on a
CRLF working copy whose bytes were identical to the repo's. v1.4 adds
Fix In Passing, Report It, after a patch blocked itself on two Unicode
arrows that predated it by months, and Naming and Archiving a Patch
Script, an unstated convention 96 scripts deep that Tony had been
following alone. v1.5 adds Stamp What You Change (L-220), after Tony
observed that this project updates bodies more reliably than it updates
anchors, dates and module descriptions.
"""

L219_OLD = b"""which would be 1.5.
"""

L219_NEW = b"""which would be 1.6 -- 1.5 is taken by L-220.
"""

SECTION_A_OLD = b"""exposed it); HANDOFF_20260819_alfven_and_the_swap.md, error 4.

## PENDING ACTION (Tony-side)
"""

SECTION_A_NEW = b"""exposed it); HANDOFF_20260819_alfven_and_the_swap.md, error 4.

#### [L-220] A patch updates the body but not the anchor, date or description
<!-- L:220 status:DONE upd:2026-08-20 section:A flag: rice:3/3/85/1 -->
- **Tony's observation, 2026-08-20, and it is about the project rather
  than about any one file.** "We do not update these documents with
  every session, nor do we always update the module description,
  history, dates, etc. -- we tend to update the body more than the
  anchors." Confirmed across the three master plans:
  `MASTER_PLAN_CRITICAL_PATH_SUMMARY.md` carries both SHAs and a
  live-check note, `MASTER_PLAN_INTERACTIVE_GALLERY.md` carries no
  anchor at 2010 lines, and `MASTER_PLAN_WEB_PUBLICATION.md` carries an
  anchor six weeks stale. The ledger is the most current document
  because its index is machine-maintained, not because anyone is more
  disciplined about it.
- **Why a session-start anchor check was proposed and then dropped.**
  Claude proposed comparing every Context document's anchor against
  live HEAD. Tony's correction makes that unworkable: if anchors are
  updated only sometimes, a mismatch means EITHER the document is stale
  OR nobody re-stamped it, and nothing distinguishes them. Two
  conditions, one signal -- a check that fires constantly and means
  nothing, which is worse than no check.
- **Why a generated currency stamp was also rejected.** It needs its own
  generator to maintain. A stamp written by the patch that caused the
  staleness cannot drift, because there is no second step to forget.
  Tony's framing is the better one and it is the protocol's own "put the
  check where it runs," one layer over.
- **CLOSED 2026-08-20 in `safe-file-editing` 1.5, Stamp What You
  Change.** The patch updates the file's currency block -- version line,
  anchor, history, date, and the module description where behaviour
  changed -- in the same transaction as the body, names the model, and
  prints which stamps it updated. The module description is called out
  as the highest-stakes half because `module_atlas.py` regenerates
  MODULE_ATLAS.md and MODULE_INDEX.md from module docstrings, so a stale
  description propagates into a generated document that presents itself
  as current.
- **A limit Claude proposed and Tony declined.** Claude wanted "stamp
  only what the patch actually touches," on the grounds that stamping an
  untouched file is a false provenance claim. Tony: "I don't see when
  this would happen. Your patches are not incidental, always for a
  purpose." Recorded because the reasoning generalises -- the rule was
  written for an imagined failure, not an observed one, which is what
  Extend a Boundary Before Adding a Path exists to refuse. If it ever
  happens it earns a field note then.
**Note:** RICE is Claude's proposal, unratified.
**Ref:** `skills/safe-file-editing/SKILL.md` "Stamp What You Change" and
"Fix In Passing, Report It"; `module_atlas.py` header (L-163 Phase 3);
`skills/orrery-coding-conventions/SKILL.md` credit lines (the
attribution convention this generalises); L-219 (the other open
safe-file-editing gap, now targeting 1.6).

## PENDING ACTION (Tony-side)
"""

EDITS = [
    (SKILL, 'Stamp What You Change added', SECTION_OLD, SECTION_NEW),
    (SKILL, 'skill version 1.4 -> 1.5 (its own stamp)',
     VERSION_OLD, VERSION_NEW),
    (LEDGER, 'L-219 rebased to 1.6', L219_OLD, L219_NEW),
    (LEDGER, 'L-220 inserted', SECTION_A_OLD, SECTION_A_NEW),
]

STAMPS_UPDATED = [
    'skills/safe-file-editing/SKILL.md -- version 1.4 -> 1.5, history '
    'paragraph, date 2026-08-20, model attribution',
]


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    blobs = {}
    crlf = {}

    for name in (SKILL, LEDGER):
        path = os.path.join(here, name)
        if not os.path.exists(path):
            print('ERROR: %s not found under this script.' % name)
            print('       Save the script into the repo root.')
            return 1
        with open(path, 'rb') as handle:
            data = handle.read()
        fp = hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()
        if fp != FINGERPRINTS[name]:
            print('ERROR: BASE MOVED for %s' % name)
            print('       expected %s, found %s' % (FINGERPRINTS[name], fp))
            print('       Nothing written to either file.')
            return 1
        blobs[name] = data
        crlf[name] = data.count(b'\r\n') > 0
        print('base %-40s %s  %s'
              % (name, fp, 'CRLF' if crlf[name] else 'LF'))

    original_skill = blobs[SKILL]

    for name, label, old, new in EDITS:
        o, n = old, new
        if crlf[name]:
            o = o.replace(b'\n', b'\r\n')
            n = n.replace(b'\n', b'\r\n')
        count = blobs[name].count(o)
        if count != 1:
            print('ANCHOR FAIL: %s -- expected 1 match, found %d'
                  % (label, count))
            print('             Nothing written to either file.')
            return 1
        blobs[name] = blobs[name].replace(o, n)
        print('ok  %s' % label)

    before = original_skill.replace(b'\r\n', b'\n').split(b'\n')
    after = set(blobs[SKILL].replace(b'\r\n', b'\n').split(b'\n'))
    dropped_ok = (b'Skill version: 1.4', b'1ba20c3 (v1.3)',
                  b'following alone.')
    missing = [x for x in before
               if x.strip() and x not in after
               and not any(x.startswith(d) for d in dropped_ok)]
    if missing:
        print('ERROR: NOT A PURE ADDITION. %d line(s) from 1.4 are gone:'
              % len(missing))
        for x in missing[:10]:
            print('       %s' % x.decode('ascii', 'replace')[:70])
        print('       Nothing written to either file.')
        return 1
    print('pure addition confirmed (%d skill lines checked)' % len(before))

    if blobs[LEDGER].count(b'#### [L-220]') != 1:
        print('ANCHOR FAIL: L-220 header count is %d, expected 1'
              % blobs[LEDGER].count(b'#### [L-220]'))
        return 1

    for name in (SKILL, LEDGER):
        with open(os.path.join(here, name), 'wb') as handle:
            handle.write(blobs[name])
    print('patch applied (%d + %d bytes)'
          % (len(blobs[SKILL]), len(blobs[LEDGER])))
    print('')
    print('STAMPS UPDATED BY THIS PATCH (per Stamp What You Change):')
    for line in STAMPS_UPDATED:
        print('  %s' % line)
    print('  LEDGER_CONSOLIDATED.md -- no currency block of its own; its')
    print('    index is regenerated by ledger_index.py below.')
    print('')
    print('NEXT: 1. run ledger_index.py')
    print('      2. run skills_index.py')
    print('      3. reinstall safe-file-editing at Settings > Skills')
    return 0


if __name__ == '__main__':
    sys.exit(main())
