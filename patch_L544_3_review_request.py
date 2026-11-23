"""
patch_L544_3_review_request.py -- the review request for GPT and for
Gemini 4 Neon (L-522, document caps, step 3), written at the end of the
coordinating session of Nov 22 and 23, 2026.

Built on b0eedeab at https://github.com/tonylquintanilla/palomas_orrery
(branch main) with patch_L544_2_session_close.py on top. RUN THAT ONE
FIRST; this one refuses, writing nothing, until it has. Written by the
coordinating session (Claude Fable 5.2) under safe-file-editing 1.15
and ledger-and-session-records 1.23.

Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\
gallery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\

RUN COMMAND
    This file is in the orrery folder (palomas_orrery_for_github). Open
    it in VS Code and click Run:

        python patch_L544_3_review_request.py

    Success: four "ok" lines, "patch applied", "wrote" for the request,
    then two tools, each printing "ok".
    Failure: an "ERROR:" or "ANCHOR FAIL" line, and NOTHING is written.
    Undo after a success: Discard Changes in GitHub Desktop.
    Once it has run, move it to the documentation folder.

WHAT IT CHANGES (no code, no skill, no protocol)
    documentation/REVIEW_REQUEST_fundamental_documents_20261123.md:
        new. One request, the same words for both reviewers; how to
        carry it is at its top. This patch places it; it is not handed
        over any other way.
    LEDGER_CONSOLIDATED.md, L-522 (document caps): the request is
        written; Gemini 4 Neon is the second reviewer, in Tony's words.
    documentation/HANDOFF_document_upkeep_20261116.md: its line saying
        the request is not written gets a dated note that it is.
    documentation/WHERE_WE_ARE.md, above the marker: one "Needs you
        now" line, carrying the request first.

Permanent: the request and the records. This script is one-shot.

Written November 23, 2026 with Anthropic's Claude Fable 5.2.
"""

import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

EDITS = [('LEDGER_CONSOLIDATED.md',
  '<!-- L:522 status:OPEN upd:2026-11-22 section:A flag: rice: -->',
  '<!-- L:522 status:OPEN upd:2026-11-23 section:A flag: rice: -->'),
 ('LEDGER_CONSOLIDATED.md',
  '     request is written when step 3 is next. Claude recommended;\n'
  '     accepted in the same sentence.\n',
  '     request is written when step 3 is next. Claude recommended;\n'
  '     accepted in the same sentence.\n'
  '     WRITTEN 2026-11-23 by the coordinating session (Claude Fable\n'
  '     5.2): `documentation/REVIEW_REQUEST_fundamental_documents_20261123.md`,\n'
  '     one request in the same words for TWO reviewers. Tony, Nov 23,\n'
  '     09:25: "We had also discussed an independent review of documents\n'
  '     by GPT and now Gemini Neon may be up to it too."; asked whether\n'
  '     Gemini 4 Neon is the second reviewer, 09:30: "Yes". Google\n'
  '     released Gemini 4 Neon on 2026-11-18 (its announcement, read\n'
  '     2026-11-23 by web search). Not known: how it reads the\n'
  '     repository; the note of 2026-09-03 (L-276) predates it, so the\n'
  '     request has each reviewer say first how it read, and stop if it\n'
  '     could not. The request names five things not to open, this item\n'
  '     among them, to keep each review independent of the one of Nov 10.\n'
  '     Tony saves the replies as\n'
  '     `documentation/REVIEW_RETURN_gpt_20261123.md` and\n'
  "     `documentation/REVIEW_RETURN_gemini_neon_20261123.md`; step 3's\n"
  '     session compares them with the review of Nov 10 before the draft.\n'),
 ('documentation/HANDOFF_document_upkeep_20261116.md',
  '     compared. Not written. GPT has no protocol and no skills, so the\n'
  '     request names its fetch targets and asks which it read (L-290).\n',
  '     compared. Not written. GPT has no protocol and no skills, so the\n'
  '     request names its fetch targets and asks which it read (L-290).\n'
  '     (2026-11-23, the coordinating session, Claude Fable 5.2: WRITTEN,\n'
  '     `documentation/REVIEW_REQUEST_fundamental_documents_20261123.md`,\n'
  '     and carried to Gemini 4 Neon as well as GPT, Tony\'s "Yes". The\n'
  '     replies are `documentation/REVIEW_RETURN_gpt_20261123.md` and\n'
  '     `documentation/REVIEW_RETURN_gemini_neon_20261123.md`. L-522.)\n'),
 ('documentation/WHERE_WE_ARE.md',
  "> - *(do) Start the protocol's reduction in a new Fable session of its own, with",
  '> - *(do) First carry `documentation/REVIEW_REQUEST_fundamental_documents_20261123.md` to GPT '
  'and to Gemini 4 Neon, as its opening says, and save each reply under the name it gives. Then '
  "start the protocol's reduction in a new Fable session of its own, with")]

REQ_PATH = 'documentation/REVIEW_REQUEST_fundamental_documents_20261123.md'
REQ_TEXT = ("<!-- Doc-Kind: hand | A review request carried to GPT and to Gemini 4 Neon: the project's "
 'governing documents, read fresh, for gaps, effectiveness and efficiency (L-522, step 3). '
 'Communication; the same words for both reviewers. -->\n'
 '# Review request: the governing documents, read fresh\n'
 '\n'
 'Built on orrery `b0eedeabb6aa1c88243443b876e09bfc72ec3dd3`\n'
 'at https://github.com/tonylquintanilla/palomas_orrery (branch main)\n'
 'Gallery at `326863a62a18c6f9446967f967ba5719d21ca91e`\n'
 'at https://github.com/tonylquintanilla/tonyquintanilla.github.io\n'
 '\n'
 'Tony Quintanilla, PE | request drafted by Claude Fable 5.2 | 2026-11-23\n'
 'Handle: L-522 (document caps), step 3.\n'
 '\n'
 "Tony's local folders: orrery\n"
 'C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\\n'
 'gallery\n'
 'C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\\n'
 '\n'
 'For Tony, how to carry it:\n'
 '\n'
 '- The same words go to two reviewers: GPT, and Gemini 4 Neon. Neither\n'
 "  sees the other's reply, and neither sees any Claude review.\n"
 '- GPT: paste everything below the line into a new chat.\n'
 '- Gemini 4 Neon: on your computer, not the phone, import the orrery\n'
 '  repository first, as for earlier relays; then paste the same text\n'
 '  into a new chat. If the import is gone or works differently now,\n'
 '  tell the session before going on.\n'
 "- Save each reply, whole, in the orrery's documentation folder, as\n"
 '  `REVIEW_RETURN_gpt_20261123.md` and\n'
 '  `REVIEW_RETURN_gemini_neon_20261123.md`. The session that takes up\n'
 "  the protocol's reduction reads them from there.\n"
 '\n'
 '---\n'
 '\n'
 'You are asked for an independent review, as a colleague would give one:\n'
 'here is the job, flag problems, including problems with the job.\n'
 '\n'
 '## Who is asking, and who reads these documents\n'
 '\n'
 'Tony Quintanilla is a retired civil and environmental engineer, an\n'
 'artist and an anthropologist. He is not a programmer and not an\n'
 "astronomer. He builds Paloma's Orrery, a desktop solar-system program\n"
 'in Python and the website palomasorrery.com, through conversation with\n'
 "AI partners, and he alone commits and pushes. The code's quality is the\n"
 'product of that collaboration; it is not evidence of his programming\n'
 'skill. Write for an engineer, not for a developer.\n'
 '\n'
 'The documents under review have two readers. One is Tony, who often\n'
 'reads on a phone and has said he cannot follow compressed language. The\n'
 'other is an AI session, which starts with no memory and reads these\n'
 'documents to learn how the work is done here.\n'
 '\n'
 '## The question\n'
 '\n'
 'It is the question Tony gave a Claude session on November 10, 2026:\n'
 "review the project's governing documents for gaps, effectiveness and\n"
 'efficiency. What those three words mean in a given file is part of your\n'
 'judgment; say how you read them.\n'
 '\n'
 '## What to read\n'
 '\n'
 'In the orrery repository:\n'
 '\n'
 '- `PROJECT_INSTRUCTIONS.md`, whole. It is the protocol: how a session\n'
 '  is run.\n'
 "- `skills/<name>/SKILL.md`, twelve files. Read at least each one's\n"
 '  opening and its contents list. Read in full the ones you judge\n'
 '  matter most, and say which.\n'
 '- `documentation/WHERE_WE_ARE.md` and\n'
 '  `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md`.\n'
 '- `README.md`, `METHOD_MODEL_EFFORT.md`, `DOCUMENT_CAPS.md`,\n'
 '  `CLAUDE.md`.\n'
 '- `LEDGER_CONSOLIDATED.md` is 2.8 MB. Do not try to read it whole.\n'
 '  Read its opening and its generated index, and a few items of your\n'
 '  own choosing in full.\n'
 '- The tops of `PROVENANCE_AUDIT.md` and `MODULE_ATLAS.md`, and the\n'
 '  docstring of `constants_new.py`.\n'
 '\n'
 'In the website repository, if you can reach it: `README.md`,\n'
 '`CLAUDE.md`, and the opening of `INTERACTIVE_AS_BUILT.md`.\n'
 '\n'
 'The code is not under review.\n'
 '\n'
 '## What not to open\n'
 '\n'
 'An earlier review of this same question exists. To keep yours\n'
 'independent, do not open:\n'
 '\n'
 '- `documentation/REVIEW_fundamental_documents_20261110.md`\n'
 '- `documentation/DESIGN_document_caps_rulings_20261110.md`\n'
 '- `documentation/DESIGN_oversight_talk_20261110.md`\n'
 '- `documentation/HANDOFF_document_upkeep_20261116.md`\n'
 "- the ledger's item L-522\n"
 '\n'
 'If you open one, by accident or because a tool did, say so. A review\n'
 'that has seen the earlier one is still useful. It is a different thing\n'
 'from a fresh read, and we need to know which this is. You will meet\n'
 'rules in the documents that came out of that review; judge them as you\n'
 'would any other rule.\n'
 '\n'
 '## Say first how you read the repository\n'
 '\n'
 'Open your reply with one of these, whichever is true:\n'
 '\n'
 '- you fetched the files at the commit named at the top;\n'
 '- you worked from a copy imported on a date, and you give the date;\n'
 '- you could not read the repository.\n'
 '\n'
 'If you could not read it, stop there and say so. Do not review from\n'
 'memory, or from what a project like this usually contains.\n'
 '\n'
 'Then list what you read in full, what you read in part, and what you\n'
 'did not read. A reply that does not name its files is telling us it\n'
 'did not read them.\n'
 '\n'
 '## What to send back\n'
 '\n'
 'At most twelve findings, the most important first. For each:\n'
 '\n'
 '1. The finding, in one plain sentence.\n'
 '2. The evidence: a quotation of under 25 words, with its file and its\n'
 '   heading. No finding without one.\n'
 '3. Who pays for it, and how: Tony, a session, or the work itself.\n'
 '4. What you would change: the smallest change that would do.\n'
 '5. How sure you are, and what would change your mind.\n'
 '\n'
 'Then, separately:\n'
 '\n'
 '- Up to five things these documents do well and should not lose.\n'
 '- Anything in this request that is unclear, or that you think is the\n'
 '  wrong question.\n'
 '\n'
 'Findings and options only. Propose no rewrite of a whole document and\n'
 "make no edit; the rulings are Tony's.\n"
 '\n'
 'Plain language, short sentences, and a short gloss for any term a\n'
 'retired engineer might not know. Name things: "several skills" cannot\n'
 'be acted on, and four skills named can. About 1,500 words in all.\n')


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
                  "patch_L544_2_session_close.py has not run, run it first. "
                  "Otherwise tell the session. NOTHING was written." % (name, c, old[:70]))
            sys.exit(1)
        staged[name][0] = text.replace(o, n)
        print("ok   %s: %s" % (name, (old.strip().splitlines()
                                      or ['(end)'])[0][:52]))
    ppath = os.path.join(HERE, *REQ_PATH.split('/'))
    pbytes = REQ_TEXT.encode('ascii')
    write_req = True
    if os.path.exists(ppath):
        with open(ppath, 'rb') as f:
            have = f.read().replace(b'\r\n', b'\n')
        if have == pbytes:
            write_req = False
        else:
            print("ERROR: %s already exists and differs from the one this "
                  "patch places. Likely a copy saved by hand: delete it and "
                  "run again. NOTHING was written." % REQ_PATH)
            sys.exit(1)
    for name, (text, was_crlf) in staged.items():
        with open(os.path.join(HERE, *name.split('/')), 'wb') as f:
            f.write(text)
        if was_crlf:
            print("note: %s was CRLF in the working copy; written LF" % name)
    print("patch applied (%d edits, %d files)" % (len(EDITS), len(staged)))
    if write_req:
        with open(ppath, 'wb') as f:
            f.write(pbytes)
        print("wrote %s (%d bytes)" % (REQ_PATH, len(pbytes)))
    else:
        print("already there, identical: %s" % REQ_PATH)
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
    print("Do next: move this file into documentation; commit and push")
    print("the orrery. Then carry the request to GPT and to Gemini 4")
    print("Neon, as its opening says:")
    print(REQ_PATH)


if __name__ == '__main__':
    main()
