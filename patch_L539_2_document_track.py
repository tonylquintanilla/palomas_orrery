"""
patch_L539_2_document_track.py -- the document review, L-522 (document
caps), joins the order of work. It runs AFTER patch_L539_1_close_record.py
and goes in the same commit.

Built on 97a8b733 at https://github.com/tonylquintanilla/palomas_orrery
(branch main) with patch_L539_1_close_record.py applied; gallery e6af10ea
at https://github.com/tonylquintanilla/tonyquintanilla.github.io.

Tony, 2026-11-22, 15:02: "One more thing. In a previous session we were
working on documents review. Can you integrate that into this plan?"
Asked "Do you confirm this order, with step 3 before L-538?", 15:07:
"Yes".

RUN COMMAND
    Run patch_L539_1_close_record.py first. Then open this file in VS
    Code, in the orrery folder (palomas_orrery_for_github), and click
    Run:

        python patch_L539_2_document_track.py

    Success: "ok" lines for the edits, "patch applied", then "ok" for
    ledger_index.py and the document-caps check.
    Failure: an "ERROR:" or "ANCHOR FAIL" line, and NOTHING is written.
    Undo after a success: Discard Changes in GitHub Desktop.
    Once it has run, move it to the documentation folder.

What it changes:
    LEDGER_CONSOLIDATED.md: L-522 (document caps), the order and Tony's
        words; L-538 (the orbiters' printed error), its order note.
    documentation/WHERE_WE_ARE.md: Do next, and the road's document
        line, each in place.
    documentation/PROMPT_coordinator_start_20261122_3.md, which the
        first patch made: the order of work.

No code, no skill and no data file is touched.

Written November 22, 2026 with Anthropic's Claude Fable 5.2.
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

EDITS = [('LEDGER_CONSOLIDATED.md',
  '**Gap:** steps 3 to 6 (step 1 built 2026-11-10, night; step 2 built',
  "**Note:** THE TRACK JOINS THE ROAD'S ORDER, Nov 22, 2026 (the\n"
  'coordinating session, Claude Fable 5.2). Tony, 15:02: "One more thing.\n'
  'In a previous session we were working on documents review. Can you\n'
  'integrate that into this plan?" The coordinating session proposed: the\n'
  "skills bump (v3.145); then L-544 (L4 and L5 tie); then this item's step\n"
  "3, the protocol's reduction, in its own Fable session, before L-538 (the\n"
  "orbiters' printed error) and the encounter's slice 2; then step 4, the\n"
  "ledger's closed items moved out, at the next gap between builds, and\n"
  'steps 5 and 6 the same way. Asked "Do you confirm this order, with step\n'
  '3 before L-538?", Tony, 15:07: "Yes". The reasons given him: after step\n'
  '3 a skill bump no longer needs the protocol pasted into the Project, and\n'
  'every build ahead owes a bump; the ledger is 2.8 MB and every session\n'
  'searches it; and the track had not moved since Nov 11 because a build\n'
  'always came first. Running step 3 beside L-538 with a second coordinator\n'
  'was advised against: it needs his rulings and a carry to GPT, and on Nov\n'
  '22 his carrying was the limit when two sessions ran at once.\n'
  "- SEEN Nov 22, for step 3's close: the handoff's line that every skill\n"
  '  sits at its cap, "so every change to one begins with moving something\n'
  '  out", held. The bump of that day stalled on finding room in\n'
  '  gallery-cache-builder (942 of 944) and horizons-orbital-mechanics (904\n'
  '  of 904), whose plain history earlier bumps had already moved. Each is\n'
  '  a candidate for the split the exhibit skill had at step 2; not\n'
  '  proposed to Tony yet.\n'
  '**Gap:** steps 3 to 6 (step 1 built 2026-11-10, night; step 2 built'),
 ('LEDGER_CONSOLIDATED.md',
  '<!-- L:522 status:OPEN upd:2026-11-16 section:A flag: rice: -->',
  '<!-- L:522 status:OPEN upd:2026-11-22 section:A flag: rice: -->'),
 ('LEDGER_CONSOLIDATED.md',
  '**Note:** ORDER, Nov 22, 2026: after the skills bump (v3.145) and after\n'
  "L-544 (L4 and L5 tie), by Tony's word of that day, recorded on L-544.",
  '**Note:** ORDER, Nov 22, 2026: after the skills bump (v3.145), after\n'
  "L-544 (L4 and L5 tie) and after the protocol's reduction, L-522\n"
  "(document caps) step 3, by Tony's two words of that day, recorded on\n"
  'L-544 and L-522.'),
 ('documentation/WHERE_WE_ARE.md',
  '> **Do next:** *The next coordinating session writes the one skills bump '
  '(v3.145) first, from '
  '`documentation/HANDOFF_coordinator_20261122_bump_notes.md`; then L-544 (L4 '
  "and L5 tie), ahead of L-538 (the orbiters' printed error) by your word of "
  "Nov 22; then the encounter's slice 2, its talk first (L-529 (guided "
  'encounters)).*',
  '> **Do next:** *The next coordinating session writes the one skills bump '
  '(v3.145) first, from '
  '`documentation/HANDOFF_coordinator_20261122_bump_notes.md`; then L-544 (L4 '
  "and L5 tie); then the protocol's reduction, step 3 of L-522 (document "
  "caps), in its own Fable session; then L-538 (the orbiters' printed error); "
  "then the encounter's slice 2, its talk first (L-529 (guided encounters)). "
  'Your "Yes" of Nov 22 to this order.*'),
 ('documentation/WHERE_WE_ARE.md',
  '  d.   [beside] Document caps (L-522 (document caps)): steps 1 and 2\n'
  '               built Nov 10 and 11; steps 3 to 6 between builds, the\n'
  "               protocol's reduction first, for a new Fable session.",
  '  d.   [beside] Document caps (L-522 (document caps)): steps 1 and 2\n'
  "               built Nov 10 and 11; step 3, the protocol's reduction, "
  'after L-544 and before L-538, in its own Fable session (your "Yes", Nov '
  "22); step 4, the ledger's closed items moved out,\n"
  '               at the next gap between builds; then steps 5 and 6.  << '
  'moved this session'),
 ('documentation/PROMPT_coordinator_start_20261122_3.md',
  "- Then L-538, then the encounter's slice 2, its talk first (L-529).\n",
  "- Then the protocol's reduction, step 3 of L-522 (document caps), in its\n"
  '  own Fable session, BEFORE L-538: Tony, Nov 22, 15:07, "Yes". He\n'
  '  starts it with documentation/HANDOFF_document_upkeep_20261116.md and\n'
  '  L-522; this session writes it no brief. It needs a review request\n'
  '  carried to GPT, then the draft, then his rulings on two gate wordings.\n'
  '  After it a skill bump no longer needs the protocol pasted into the\n'
  '  Project. Do not run it beside a build: one job at a time.\n'
  "- Then L-538, then the encounter's slice 2, its talk first (L-529).\n"
  "- Then step 4 of L-522, the ledger's closed items moved out by a tool,\n"
  '  at the next gap between builds; steps 5 and 6 the same way.\n')]


def main():
    for rel, text in []:
        path = os.path.join(HERE, *rel.split('/'))
        if os.path.exists(path):
            with open(path, 'rb') as f:
                have = f.read().replace(b'\r\n', b'\n')
            if have != text.encode('ascii'):
                print("ERROR: %s already exists and differs from this patch's "
                      "copy. Delete it and run again. NOTHING was written."
                      % rel)
                sys.exit(1)
    staged = {}
    for name, old, new in EDITS:
        path = os.path.join(HERE, *name.split('/'))
        if not os.path.exists(path):
            print("ERROR: %s not found. Run patch_L539_1_close_record.py "
                  "first, in the orrery folder (palomas_orrery_for_github). "
                  "NOTHING was written." % name)
            sys.exit(1)
        if name not in staged:
            with open(path, 'rb') as f:
                raw = f.read()
            staged[name] = [raw.replace(b'\r\n', b'\n'), b'\r\n' in raw]
        text = staged[name][0]
        o, n = old.encode('ascii'), new.encode('ascii')
        c = text.count(o)
        if c != 1:
            print("ANCHOR FAIL: %s, expected 1 match, found %d: %r\n"
                  "If this patch already ran, there is nothing to do. If "
                  "it has not, run patch_L539_1_close_record.py first; if that "
                  "one has run, tell the session. NOTHING was "
                  "written." % (name, c, old[:70]))
            sys.exit(1)
        staged[name][0] = text.replace(o, n)
        print("ok   %s: %s" % (name, old.strip().splitlines()[0][:60]))
    for rel, text in []:
        path = os.path.join(HERE, *rel.split('/'))
        if os.path.exists(path):
            print("ok   %s: already there, identical" % rel)
            continue
        with open(path, 'wb') as f:
            f.write(text.encode('ascii'))
        print("new  %s" % rel)
    for name, (text, was_crlf) in staged.items():
        with open(os.path.join(HERE, *name.split('/')), 'wb') as f:
            f.write(text)
        if was_crlf:
            print("note: %s was CRLF in the working copy; written LF" % name)
    print("patch applied (%d edits in %d files)"
          % (len(EDITS), len(staged)))
    for tool in (["ledger_index.py"], ["doc_index.py", "--caps"]):
        r = subprocess.run([sys.executable] + tool, cwd=HERE,
                           capture_output=True, text=True)
        if r.returncode != 0:
            print((r.stdout or '')[-1500:] + (r.stderr or '')[-800:])
            print("ERROR: %s exited %d. The edits above are written; "
                  "tell the session what it printed." % (' '.join(tool),
                                                        r.returncode))
            sys.exit(1)
        print("ok   %s" % ' '.join(tool))
    print("Next: move this patch to documentation, then commit and push "
          "the orrery. Suggested summary: L539 close record")


if __name__ == '__main__':
    main()
