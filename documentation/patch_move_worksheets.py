"""Move the cross-check evidence chain into documentation/worksheets/.

RUN COMMAND
-----------
Save this file into the palomas_orrery repo ROOT, open it in VS Code, and
click Run.

    python patch_move_worksheets.py

WHAT IT DOES
------------
Creates documentation/worksheets/ and moves 34 files into it: the
worksheets returned by each checker, and the prompts that were sent to
produce them. Then updates the two LIVE documents that spell out a
worksheet path.

WHY
---
Tony's ruling, 2026-08-12. These stopped being archive the moment a tool
started reading them. The worksheet named in a `# Cross-checked:`
annotation is the evidence behind that constant, and the planned
worksheet checker opens it and confirms it states the value. A file a
checker reads is a live source, and `documentation/` -- roughly 700 files
of session records, handoffs, and spent patch scripts -- does not say
that about anything in it.

`data/` was considered and set aside: it means what the application
produces and consumes, and worksheets are evidence from a human-and-AI
review process rather than application data.

ONE RULE, NOT A JUDGEMENT PER FILE
----------------------------------
Everything in the evidence chain moves -- prompts sent, worksheets
returned, cited or not. Moving only the cited ones would mean a worksheet
had to be relocated the day an annotation started pointing at it.

Nine of the worksheets are cited by no annotation today. They are NOT
orphans: the provenance sweep is incomplete, and those cover files not
yet annotated (Tony, 2026-08-12). The worksheet checker must treat an
uncited worksheet as pending work rather than a defect.

THE ANNOTATIONS DO NOT MOVE
---------------------------
All 134 `# Cross-checked:` lines name a bare filename, never a path, so
the machine-read link is untouched by this. Nothing in any source module
changes.

WHAT IS DELIBERATELY LEFT ALONE
-------------------------------
Seven references spell out `documentation/<worksheet>.md` inside handoffs
and spent patch scripts. Those are historical claims about the state a
session was built on, and rewriting one makes it assert a path that did
not exist when it was written -- the same reasoning that keeps a
handoff's `built on <SHA>` anchor fixed. They become dead pointers, which
is the honest cost of the move.

The two updated here are different: the ledger and the master plan
summary describe CURRENT state, so their pointers are claims about now.

SAFETY
------
- Verifies all 34 sources exist and that both text anchors match exactly
  once BEFORE moving or writing anything.
- Refuses if documentation/worksheets/ already contains any of them, so a
  second run reports rather than half-repeats.
- Text edits use binary-mode I/O with LF-normalized fingerprints, so a
  CRLF working copy does not read as a moved base.

WHAT SUCCESS LOOKS LIKE
-----------------------
34 `moved` lines, two `ok` lines for the text edits, then a summary. Any
`ERROR:` or `ANCHOR FAIL` means nothing was moved and nothing written.

AFTER RUNNING
-------------
GitHub Desktop will show these as deletions plus additions rather than
renames until you commit; that is normal for a bulk move. Run
maintenance_run.py, then commit.
"""

import hashlib
import os
import sys

DOCS = 'documentation'
DEST = os.path.join('documentation', 'worksheets')

WORKSHEETS = [
    'TRACK1_PROMPT_cross_check_worksheets.md',
    'batch1_blind_source_lookup_gemini.md',
    'batch1_blind_source_lookup_gpt.md',
    'batch1_tier1_sourcing_gpt_independent.md',
    'batch1_tier2_cross_check_gemini.md',
    'batch1_tier2_cross_check_gpt.md',
    'batch1_tier2_followup_gpt.md',
    'constants_new_citation_verification_gpt.md',
    'constants_remaining_independent_verification_gpt.md',
    'track1_gpt_independent_worksheet_mars_visualization.md',
    'worksheet_asteroid_belt.md',
    'worksheet_batch1_tier1_sourcing_gemini.md',
    'worksheet_claude_batch1_blind_lookup.md',
    'worksheet_claude_batch1_blind_lookup_DELTA.md',
    'worksheet_claude_batch1_followup.md',
    'worksheet_claude_batch1_tier1_sourcing.md',
    'worksheet_claude_batch1_tier2.md',
    'worksheet_claude_constants_new.md',
    'worksheet_claude_constants_remaining.md',
    'worksheet_claude_mars_visualization.md',
    'worksheet_comet_visualization.md',
    'worksheet_earth_visualization.md',
    'worksheet_eris_visualization.md',
    'worksheet_gemini_batch1_followup.md',
    'worksheet_gemini_constants_remaining.md',
    'worksheet_jupiter_visualization.md',
    'worksheet_mars_visualization.md',
    'worksheet_mercury_visualization.md',
    'worksheet_prompt_batch1_blind_lookup.md',
    'worksheet_prompt_batch1_followup.md',
    'worksheet_prompt_batch1_tier1_sourcing.md',
    'worksheet_prompt_batch1_tier2_cross_check.md',
    'worksheet_prompt_constants_new.md',
    'worksheet_prompt_constants_remaining.md',
]

LEDGER = 'LEDGER_CONSOLIDATED.md'
SUMMARY = os.path.join('documentation',
                       'MASTER_PLAN_INTERACTIVE_GALLERY_SUMMARY.md')

BASE_MD5 = {
    LEDGER: '786b92a7e1f03569c0a38db2d238ce6a',
    SUMMARY: '74c3ee24744a1fe3c43f00a8767956bc',
}

EDITS = [
    (LEDGER, 'ledger: worksheet path',
     b'documentation/worksheet_earth_visualization.md',
     b'documentation/worksheets/worksheet_earth_visualization.md'),
    (SUMMARY, 'master plan summary: worksheet path',
     b'documentation/worksheet_gemini_constants_remaining.md',
     b'documentation/worksheets/worksheet_gemini_constants_remaining.md'),
]


def fingerprint(data):
    """MD5 over LF-normalized content -- line endings are not content."""
    return hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    docs = os.path.join(here, DOCS)
    dest = os.path.join(here, DEST)

    if not os.path.isdir(docs):
        print('ERROR: %s/ not found. Run this from the repo root.' % DOCS)
        sys.exit(1)

    # ---- check every source before touching anything -----------------
    missing = [n for n in WORKSHEETS
               if not os.path.isfile(os.path.join(docs, n))]
    if missing:
        print('ERROR: %d worksheet(s) not found in %s/:'
              % (len(missing), DOCS))
        for name in missing:
            print('       %s' % name)
        print('Nothing moved.')
        sys.exit(1)

    collisions = [n for n in WORKSHEETS
                  if os.path.exists(os.path.join(dest, n))]
    if collisions:
        print('ERROR: %d file(s) already exist in %s/:'
              % (len(collisions), DEST))
        for name in collisions[:5]:
            print('       %s' % name)
        print('This patch has probably already run. Nothing moved.')
        sys.exit(1)

    # ---- check both text anchors before writing ----------------------
    blobs, crlf = {}, {}
    for name in BASE_MD5:
        path = os.path.join(here, name)
        if not os.path.exists(path):
            print('ERROR: %s not found.' % name)
            sys.exit(1)
        with open(path, 'rb') as handle:
            data = handle.read()
        got = fingerprint(data)
        if got != BASE_MD5[name]:
            print('ERROR: base moved for %s' % name)
            print('       expected %s' % BASE_MD5[name])
            print('       got      %s' % got)
            print('Nothing moved, nothing written.')
            sys.exit(1)
        blobs[name] = data
        crlf[name] = data.count(b'\r\n') > 0
        if crlf[name]:
            print('note: %s uses CRLF; anchors translated to match.' % name)

    for name, label, old, new in EDITS:
        anchor = old.replace(b'\n', b'\r\n') if crlf[name] else old
        if blobs[name].count(anchor) != 1:
            print('ANCHOR FAIL (%s): expected 1 match, found %d.'
                  % (label, blobs[name].count(anchor)))
            print('Nothing moved, nothing written.')
            sys.exit(1)

    # ---- move --------------------------------------------------------
    if not os.path.isdir(dest):
        os.makedirs(dest)
        print('created %s/' % DEST)

    for name in WORKSHEETS:
        os.rename(os.path.join(docs, name), os.path.join(dest, name))
        print('  moved  %s' % name)

    # ---- write -------------------------------------------------------
    for name, label, old, new in EDITS:
        if crlf[name]:
            old = old.replace(b'\n', b'\r\n')
            new = new.replace(b'\n', b'\r\n')
        blobs[name] = blobs[name].replace(old, new)
        print('  ok     %s' % label)

    for name, data in blobs.items():
        with open(os.path.join(here, name), 'wb') as handle:
            handle.write(data)

    print()
    print('%d files moved into %s/' % (len(WORKSHEETS), DEST))
    print('2 live path references updated.')
    print('7 references in handoffs and spent patch scripts left alone --')
    print('  those are historical claims and their pointers do not move.')
    print()
    print('NEXT: run maintenance_run.py, then commit.')


if __name__ == '__main__':
    main()
