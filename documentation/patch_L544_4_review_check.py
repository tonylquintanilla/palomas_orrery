"""
patch_L544_4_review_check.py -- the check of the two outside reviews
(GPT, Gemini 4 Neon; L-522, document caps, step 3), at the end of the
coordinating session of Nov 22 and 23, 2026.

Built on b0eedeab at https://github.com/tonylquintanilla/palomas_orrery
(branch main) with patch_L544_2_session_close.py and
patch_L544_3_review_request.py on top, which is how the orrery folder
stood on Tony's disk on Nov 23 at 14:00 (compared, identical). It
refuses, writing nothing, if either has not run. Written by the
coordinating session (Claude Fable 5.2) under safe-file-editing 1.15
and ledger-and-session-records 1.23.

Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\
gallery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\

RUN COMMAND
    This file is in the orrery folder (palomas_orrery_for_github). Open
    it in VS Code and click Run:

        python patch_L544_4_review_check.py

    Success: four "ok" lines, "patch applied", "wrote" for the check,
    then two tools, each printing "ok".
    Failure: an "ERROR:" or "ANCHOR FAIL" line, and NOTHING is written.
    Undo after a success: Discard Changes in GitHub Desktop.
    Once it has run, move it to the documentation folder.

WHAT IT CHANGES (no code, no skill, no protocol)
    documentation/REVIEW_CHECK_fundamental_documents_20261123.md: new.
        Which of the two reviews' findings hold against the files,
        where the two agree, and what touches a ruling. This patch
        places it; it is not handed over any other way.
    LEDGER_CONSOLIDATED.md: L-522 (document caps), both reviews back
        and checked, and where the replies are; L-548 (a missing
        id_type), the website's chain added to what its patch maps.
    documentation/HANDOFF_document_upkeep_20261116.md: where the
        replies are, and the check to read first.
    documentation/WHERE_WE_ARE.md, above the marker: one "Needs you
        now" line; the carry is done.

Permanent: the check and the records. This script is one-shot.

Written November 23, 2026 with Anthropic's Claude Fable 5.2.
"""

import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

EDITS = [('LEDGER_CONSOLIDATED.md',
  '     session compares them with the review of Nov 10 before the draft.\n',
  '     session compares them with the review of Nov 10 before the draft.\n'
  '     RETURNED 2026-11-23, both, and CHECKED by the coordinating\n'
  '     session: `documentation/REVIEW_CHECK_fundamental_documents_20261123.md`.\n'
  '     The replies are in `documentation/worksheets/`, where Tony put\n'
  '     them (13:59: "i put the responses in documentation/worksheets/"),\n'
  '     not in `documentation/` as written above; the worksheet checker\n'
  '     counts them among its uncited worksheets, 58 where it was 56, and\n'
  '     stays green. GPT fetched at the pinned commits: eight findings,\n'
  '     six of them facts, all six hold. Gemini 4 Neon could not fetch\n'
  '     GitHub ("Direct access to GitHub is blocked in this session."),\n'
  "     so L-276's note holds for it; it read a folder of 29 files the\n"
  '     session copied from the same commits, this item cut out of the\n'
  '     ledger copy: eleven findings, most hold, three of its counts\n'
  '     loose, one example not confirmed. The two agree on three things:\n'
  '     Session Start sends a session to the whole ledger and never names\n'
  "     Where We Are; the Pull sentence in Roles against the nights' own\n"
  '     commits; the READMEs and the plan still describing a hand copy.\n'
  '     The comparison with the review of Nov 10 is not done; it is step\n'
  '     3\'s. Tony had asked for the check file, 13:57: "yes".\n'),
 ('LEDGER_CONSOLIDATED.md',
  'and the check. All five consumers of position data are mapped first\n'
  "(the protocol's Check All Parallel Pipelines); `id_type` is on 68\n",
  'and the check. All five consumers of position data are mapped first\n'
  "(the protocol's Check All Parallel Pipelines), and the website's own\n"
  'chain with them, the builder, the assembler and the page: Gemini 4\n'
  "Neon's review of 2026-11-23, finding 3, says the gate's five leave it\n"
  'out, and the text bears that out\n'
  '(`documentation/REVIEW_CHECK_fundamental_documents_20261123.md`).\n'
  '`id_type` is on 68\n'),
 ('documentation/HANDOFF_document_upkeep_20261116.md',
  '     replies are `documentation/REVIEW_RETURN_gpt_20261123.md` and\n'
  '     `documentation/REVIEW_RETURN_gemini_neon_20261123.md`. L-522.)\n',
  '     replies are `documentation/REVIEW_RETURN_gpt_20261123.md` and\n'
  '     `documentation/REVIEW_RETURN_gemini_neon_20261123.md`. L-522.)\n'
  '     (Later the same day: both replies are back. Tony saved them in\n'
  '     `documentation/worksheets/`, under those two names, not in\n'
  '     `documentation/`. Which findings hold, and where the two agree:\n'
  '     `documentation/REVIEW_CHECK_fundamental_documents_20261123.md`.\n'
  '     Read it before the replies.)\n'),
 ('documentation/WHERE_WE_ARE.md',
  'First carry `documentation/REVIEW_REQUEST_fundamental_documents_20261123.md` to GPT and to '
  'Gemini 4 Neon, as its opening says, and save each reply under the name it gives. Then start the '
  "protocol's reduction",
  'Both outside reviews are back, in `documentation/worksheets/`, and checked: '
  "`documentation/REVIEW_CHECK_fundamental_documents_20261123.md`. Start the protocol's reduction")]

REC_PATH = 'documentation/REVIEW_CHECK_fundamental_documents_20261123.md'
REC_TEXT = ('<!-- Doc-Kind: hand | A check of the two outside reviews of the governing documents (GPT, Gemini '
 '4 Neon; L-522, step 3): which findings hold against the files, where the two agree, what touches '
 'a ruling. Communication; no rulings, nothing acted on. -->\n'
 '# Check of the two outside reviews, November 23, 2026\n'
 '\n'
 'Built on orrery `b0eedeabb6aa1c88243443b876e09bfc72ec3dd3`\n'
 'at https://github.com/tonylquintanilla/palomas_orrery (branch main)\n'
 'and gallery `326863a62a18c6f9446967f967ba5719d21ca91e`\n'
 'at https://github.com/tonylquintanilla/tonyquintanilla.github.io,\n'
 'the two commits the review request names. Every check below was made\n'
 'against those files.\n'
 '\n'
 'Tony Quintanilla, PE | written by the coordinating session, Claude\n'
 'Fable 5.2 | 2026-11-23 | Handle: L-522 (document caps), step 3.\n'
 '\n'
 "Tony's local folders: orrery\n"
 'C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\\n'
 'gallery\n'
 'C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\\n'
 '\n'
 'Type: DOCUMENTATION (zero code). For the session that takes up the\n'
 "protocol's reduction, so it does not repeat these checks. The request\n"
 'is `documentation/REVIEW_REQUEST_fundamental_documents_20261123.md`.\n'
 'The replies are where Tony saved them, in `documentation/worksheets/`:\n'
 '`REVIEW_RETURN_gpt_20261123.md` (10,202 bytes) and\n'
 '`REVIEW_RETURN_gemini_neon_20261123.md` (14,820 bytes). The worksheet\n'
 'checker now counts the two among its uncited worksheets, 58 where it\n'
 'was 56, and names them; it stays green.\n'
 '\n'
 'NOT DONE HERE: the comparison with the review of November 10. This\n'
 "session read only that review's opening. No finding was acted on.\n"
 '\n'
 '## How each reviewer read\n'
 '\n'
 '- GPT fetched both repositories at the pinned commits. It read two\n'
 '  skills in full (ledger-and-session-records, agentic-pre-test) and\n'
 '  the openings of the other ten. It says it opened none of the five\n'
 '  excluded things.\n'
 '- Gemini 4 Neon, in the Gemini app, could not fetch GitHub. Its first\n'
 '  reply: "Direct access to GitHub is blocked in this session." So the\n'
 "  protocol's note of 2026-09-03 (L-276) still holds for the new model.\n"
 '  It then read a folder of 29 files this session copied from the same\n'
 '  two commits: the protocol, the twelve skills, Where We Are, the\n'
 '  master plan and five more files whole; the tops of four; the ledger\n'
 '  in three parts, with item L-522 cut out (391 lines) and section C,\n'
 "  the closed items, left out for its size (1.3 MB). The folder's\n"
 '  MANIFEST.md said all of this. Gemini read six skills in full.\n'
 '- The whole repository cannot be imported into Gemini as it is: the\n'
 "  orrery is 2,549 files and 295 MB, and Google's stated limit for an\n"
 "  import or a code folder is 5,000 files and 100 MB. Google's stated\n"
 '  limit for a ZIP is 10 files, so the copies went as a folder.\n'
 '\n'
 "## GPT's eight findings\n"
 '\n'
 "1. The records skill has the close empty Tony's run-record zone; both\n"
 '   CLAUDE.md files say nothing below the marker is touched. HOLDS.\n'
 "   The skill's line 244; orrery CLAUDE.md line 77; website CLAUDE.md\n"
 "   line 92. The page's own marker line also says the close clears it.\n"
 "   This session's close left the zone alone.\n"
 "2. The pre-test's example command pipes into `head -50`, so it returns\n"
 '   success after the program failed. HOLDS. agentic-pre-test line 29.\n'
 '   Reproduced: a command exiting 7, piped to head, returns 0.\n'
 '3. A commit on GitHub that is not the expected one is diagnosed only\n'
 '   as "you didn\'t push"; the night commits too; Roles says Tony does\n'
 '   not use Pull while Where We Are tells him to each morning. HOLDS.\n'
 "   Both repositories' nights commit (github-actions[bot]): the\n"
 "   website's on Nov 22, the orrery's on Nov 23 at 19:15 UTC.\n"
 "4. The master plan's section 5a says the numbers' transfer is\n"
 '   "currently a HAND COPY" (line 1024) while its summary says that is\n'
 '   done (line 49); the website\'s README says "by hand" (lines 80, 107,\n'
 '   112). HOLDS.\n'
 '5. Session Start says to read the open items before proposing work;\n'
 '   the index reports 280 live items, 264 flagged. HOLDS.\n'
 "6. Where We Are's box makes Tony work out a schedule to find his next\n"
 "   action. A JUDGMENT, Tony's.\n"
 '7. The stale-skill gate says to reinstall to the account; a Code\n'
 "   session reads the repository's copy (both CLAUDE.md files). HOLDS.\n"
 "8. The protocol's two newest history entries narrate skill bumps in\n"
 '   which no protocol rule changed. A JUDGMENT, for the draft.\n'
 '\n'
 'On the request: GPT is right that its commit lines sit above the\n'
 '"paste below this line" divider, so a pasted copy would lack them.\n'
 'Both reviewers were given the whole file.\n'
 '\n'
 "## Gemini's eleven findings\n"
 '\n'
 '1. The protocol is 1,394 lines and 11,860 words; move Part 4, the\n'
 '   Quotables and the Lessons Archive out. SIZE EXACT; "roughly a\n'
 '   quarter" is OVERSTATED: those parts are lines 1009 to 1196, about\n'
 '   190 lines, 14 percent.\n'
 '2. Session Start never names Where We Are. HOLDS: the file is not\n'
 '   named anywhere before Part 2.\n'
 '3. The parallel-pipelines gate lists five consumers of position data\n'
 '   and omits the interactive gallery (the builder, the assembler, the\n'
 "   page). HOLDS as text; the website's README, line 192, repeats\n"
 '   "five". It bears on L-548 (a missing id_type), whose patch says to\n'
 '   map "all five" first.\n'
 '4. [CRITICAL] headings are in six skills though the protocol says\n'
 '   critical gates stay resident. HOLDS, and it is larger: 27, not 25\n'
 '   (provenance-discipline 12, provenance-cross-check 7,\n'
 '   interactive-exhibit 4, agentic-pre-test 2, gallery-cache-builder 1,\n'
 '   safe-file-editing 1).\n'
 '5. The Pull sentence and "run by hand". HOLDS; the same as GPT\'s 3 and\n'
 '   part of its 4.\n'
 '6. Both READMEs say the served config is kept by hand. HOLDS; the\n'
 "   orrery README's line 500.\n"
 '7. The ledger opens with 794 lines of update stamps. HOLDS: "Purpose\n'
 '   and use" is at line 795. Its "215 lines of stamps" for\n'
 '   `constants_new.py` was NOT CONFIRMED; the docstring is 254 lines.\n'
 '8. The Register Rule says the protocol is written compressed; Roles\n'
 '   says to unpack jargon "in this document\'s own prose". HOLDS.\n'
 '9. No headroom under the caps, and four governing files uncapped.\n'
 '   HOLDS: 15 of 19 rows at their cap, not 14 of 17;\n'
 '   METHOD_MODEL_EFFORT.md and INTERACTIVE_AS_BUILT.md are not in\n'
 '   DOCUMENT_CAPS.md.\n'
 '10. Eight of twelve skills pass 500 lines; three take 67 lines of the\n'
 '    resident manifest. HOLDS: provenance-discipline is 1,511 lines;\n'
 '    the three rows are 34, 18 and 16 lines, 68 in all.\n'
 '11. Three stale facts. TWO HOLD: safe-file-editing still points at a\n'
 '    SystemButtonFace workaround the pre-test skill now records as\n'
 '    removed; the master plan carries a "Status: v35" block (line 97)\n'
 '    under its v37 summary. The third, the exhibit skill\'s "wrong\n'
 '    default room", was NOT CONFIRMED and reads garbled: the sentence\n'
 '    it quotes names the Solar System room as the default.\n'
 '\n'
 'On the request: Gemini says 1,500 words pushes a reply toward\n'
 'compressed writing, and that a fresh reader cannot tell unfinished\n'
 'steps from faults. Both fair.\n'
 '\n'
 '## Where the two agree\n'
 '\n'
 "Neither saw the other's reply.\n"
 '\n'
 '- Session Start sends a session to the whole ledger, not to Where We\n'
 '  Are (GPT 5, Gemini 2).\n'
 "- The Pull sentence in Roles and the nights' own commits contradict\n"
 "  the protocol's account of Tony's routine (GPT 3, Gemini 5).\n"
 '- The READMEs and the master plan still describe a hand copy that is\n'
 '  automatic now (GPT 4, Gemini 6).\n'
 '- In part: the resident protocol carries weight it need not. GPT would\n'
 "  cut the history entries' narrative (its 8); Gemini would move Part 4\n"
 '  and the Quotables out (its 1).\n'
 '\n'
 '## What touches a ruling or a plan the reviewers could not see\n'
 '\n'
 "- Gemini 1: Tony's amendment of Nov 10, 16:37, binds the draft: the\n"
 '  passages on the conversation stay whole and in their own words, and\n'
 '  he sees the list of what moves before anything moves.\n'
 "- Gemini 7: removing the ledger's stamps is step 4 of L-522.\n"
 "- Gemini 9: each cap was set at the file's size that day, on purpose.\n"
 '\n'
 "## Two findings that do not wait on the reduction's shape\n"
 '\n'
 'GPT 2 is in a test the protocol calls critical, and GPT 1 could cost\n'
 "Tony notes. Both are skill changes, so they ride step 3's session.\n")


def main():
    staged = {}
    for name, old, new in EDITS:
        path = os.path.join(HERE, *name.split('/'))
        if not os.path.exists(path):
            print("ERROR: %s not found next to this script. Is it in the "
                  "orrery folder? NOTHING was written." % name)
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
                  "patch_L544_2 and patch_L544_3 have not both run, run "
                  "them first. Otherwise tell the session. NOTHING was "
                  "written." % (name, c, old[:70]))
            sys.exit(1)
        staged[name][0] = text.replace(o, n)
        print("ok   %s: %s" % (name, (old.strip().splitlines()
                                      or ['(end)'])[0][:52]))
    ppath = os.path.join(HERE, *REC_PATH.split('/'))
    pbytes = REC_TEXT.encode('ascii')
    write_rec = True
    if os.path.exists(ppath):
        with open(ppath, 'rb') as f:
            have = f.read().replace(b'\r\n', b'\n')
        if have == pbytes:
            write_rec = False
        else:
            print("ERROR: %s already exists and differs from the one this "
                  "patch places. Likely a copy saved by hand: delete it and "
                  "run again. NOTHING was written." % REC_PATH)
            sys.exit(1)
    for name, (text, was_crlf) in staged.items():
        with open(os.path.join(HERE, *name.split('/')), 'wb') as f:
            f.write(text)
        if was_crlf:
            print("note: %s was CRLF in the working copy; written LF" % name)
    print("patch applied (%d edits, %d files)" % (len(EDITS), len(staged)))
    if write_rec:
        with open(ppath, 'wb') as f:
            f.write(pbytes)
        print("wrote %s (%d bytes)" % (REC_PATH, len(pbytes)))
    else:
        print("already there, identical: %s" % REC_PATH)
    for tool in (["ledger_index.py"], ["doc_index.py", "--caps"]):
        r = subprocess.run([sys.executable] + tool, cwd=HERE,
                           capture_output=True, text=True)
        if r.returncode != 0:
            print((r.stdout or '')[-1800:] + (r.stderr or '')[-800:])
            print("ERROR: %s exited %d. The edits above are written; "
                  "Discard Changes in GitHub Desktop undoes them. Tell "
                  "the session what it printed." % (' '.join(tool),
                                                    r.returncode))
            sys.exit(1)
        print("ok   %s" % ' '.join(tool))
    print("")
    print("Do next: move this file into documentation, with patch_L544_2")
    print("and patch_L544_3 if they are still in the orrery folder. Then")
    print("commit and push the orrery: the close, the request, the two")
    print("replies and this check are all waiting for that push.")


if __name__ == '__main__':
    main()
