"""patch_L276_2_gemini_recheck_20261013.py -- one Note on L-276: Gemini
re-checked on 2026-10-13 and found with no repository access by any
route, so for Gemini a Mode 7 document carries the text itself.

Built on orrery 28e1b7d at
https://github.com/tonylquintanilla/palomas_orrery ("maintenance", after
L-437's close), on top of patch_L436_1_idea_20261013.py, which must have
run first (this patch anchors on the header stamp that one adds and
refuses if it is absent). The gallery is not touched.
Tony's local folder: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\.
Written October 13, 2026 with Anthropic's Claude Fable 5.1, at the close
of the coordination session of October 12 and 13.

HOW TO RUN
    From the orrery repo's ROOT folder: open this file in VS Code and
    press Run. Success prints one "ok" line per edit, then "patch
    applied". It touches ONE file and contacts nothing.

WHAT IT CHANGES
    LEDGER_CONSOLIDATED.md: a Note appended to L-276 (closed, stays
        closed); its upd date moves to 2026-10-13; one stamp line in
        the header. The index zone is left alone; the maintenance run
        rebuilds it.

WHAT THE NOTE RECORDS
    The two tests Tony ran on 2026-10-13 against Gemini ("Argon") in
    the Gemini web app, and their result: it could not read either
    repository by any route. Root page URLs returned an empty page
    shell; raw.githubusercontent.com and api.github.com addresses,
    given whole, were refused before any content arrived; no import
    and no GitHub integration were offered. It answered "cannot fetch"
    on every line and invented nothing. So the L-276 close's account
    of the Gemini import (checked 2026-09-03) does not describe this
    surface, and for Gemini a Mode 7 document carries the text it is
    to read, with the anchor saying which commit the text came from.
    No rule changes: that is the second case of the clause L-276
    wrote. Whether the import still exists in another Gemini app is
    not known.

SAFETY
    Every anchor is matched exactly once; if any fails, NOTHING is
    written. A file found with Windows line endings is matched after
    turning them into LF and written back LF, and the patch says so.
    Refuses on a second run (the Note's first words are already
    there). Undo is Discard Changes in GitHub Desktop.
"""
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
LEDGER = 'LEDGER_CONSOLIDATED.md'
SENTINEL = '**Note (2026-10-13): Gemini re-checked'

NOTE = '''**Note (2026-10-13): Gemini re-checked, and this surface has no repository
access by any route.** Tony ran two tests against Gemini ("Argon") in the
Gemini web app, written in the coordination session of 2026-10-12 and 13
so that a model answering from memory could not pass: the HEAD SHA and
subject of both repositories, a line of a file at HEAD, and the
provenance-discipline version line at HEAD (2.29) and at 400a9615 (2.28).
First with the repository root URLs: every item "cannot fetch"; the root
pages opened but returned an empty page shell, and it reported that it
can open only a URL pasted whole and cannot build one. Second with every
URL given whole (raw.githubusercontent.com at main and at the pinned
SHA, api.github.com for the commits): every item "cannot fetch"; all
five addresses were refused before any content arrived
(URL_FETCH_STATUS_MISC_ERROR). No import of a repository and no GitHub
integration were offered in that session. It invented nothing and
offered to work from pasted text. So the Gemini import described at
this item's close (checked 2026-09-03) is not what this surface does;
whether it still exists in another Gemini app is not known. For Gemini,
a Mode 7 document carries the text it is to read, and the anchor says
which commit that text came from -- the second case of the clause
above, unchanged. Attachments DO work, including a whole repository as
a zip (Tony, 2026-10-13: "it can accept attachments even large repos"),
so the working form for Gemini is: attach the files or the zip, and the
anchor says which commit they were taken from. GitHub serves a zip of
any commit at github.com/<user>/<repo>/archive/<SHA>.zip, which makes
the anchor exact. No rule changes; Mode 7's AI Roles line on how Gemini
reads the repo is stale for this surface and is corrected at the
protocol's next restamp, not in a patch of its own.
'''

EDITS = [
    ('header stamp (requires patch_L436_1 to have run)',
     "built on 28e1b7d.\nReview and RICE update Tony 6-21-2026\n",
     "built on 28e1b7d.\nModule updated: October 13, 2026 with Anthropic's Claude Fable 5.1\n(L-276 Note: Gemini re-checked, no repository access on this surface),\nbuilt on 28e1b7d.\nReview and RICE update Tony 6-21-2026\n"),
    ('L-276 upd date',
     "<!-- L:276 status:DONE upd:2026-09-03 section:C flag: rice:3/3/95/1 -->",
     "<!-- L:276 status:DONE upd:2026-10-13 section:C flag: rice:3/3/95/1 -->"),
    ('L-276 Note before its Gap line',
     "**Gap:** none. The UI copy of PROJECT_INSTRUCTIONS.md is the third\nstore; Tony re-uploads it after the push.\n**Ref:** PROJECT_INSTRUCTIONS.md Part 1 Mode 7 (v3.53);",
     NOTE + "**Gap:** none. The UI copy of PROJECT_INSTRUCTIONS.md is the third\nstore; Tony re-uploads it after the push.\n**Ref:** PROJECT_INSTRUCTIONS.md Part 1 Mode 7 (v3.53);"),
]


def main():
    path = os.path.join(ROOT, LEDGER)
    if not os.path.exists(path):
        print('ERROR: %s not found in %s. NOTHING was written.' % (LEDGER, ROOT))
        return 1
    raw = open(path, 'rb').read()
    crlf = b'\r\n' in raw
    t = raw.replace(b'\r\n', b'\n').decode('utf-8')
    if SENTINEL in t:
        print('ERROR: the Note is already in the ledger; this patch has run. NOTHING was written.')
        return 1
    if EDITS[0][1] not in t:
        print('ANCHOR FAIL  the header stamp from patch_L436_1_idea_20261013.py is not present.')
        print('             Run that patch first, then this one. NOTHING was written.')
        return 1
    done = []
    for label, old, new in EDITS:
        n = t.count(old)
        if n != 1:
            print('ANCHOR FAIL  %s (found %d times, expected 1). NOTHING was written.' % (label, n))
            return 1
        if any(ord(c) > 127 for c in new):
            print('ERROR: edit %r would add non-ASCII. NOTHING was written.' % label)
            return 1
        t = t.replace(old, new)
        done.append(label)
    with open(path, 'w', encoding='utf-8', newline='') as h:
        h.write(t)
    for label in done:
        print('ok  %-28s %s' % (LEDGER, label))
    if crlf:
        print('note: %s was CRLF in the working copy; written LF' % LEDGER)
    print()
    print('patch applied (%d edits in 1 file)' % len(done))
    print('Stamps updated: the ledger header.')
    print()
    print('NEXT:')
    print('  1. Paste this output into your run record.')
    print('  2. Run orrery_maintenance_run.py (the Ledger index rebuilds).')
    print('  3. Move this script into documentation/; commit with the note; push.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
