# -*- coding: utf-8 -*-
"""patch_ledger_appendix.py -- add v3.32/v3.33/v3.34 to the ledger's
Protocol Version History appendix, which currently stops at v3.31.

Built on edf05f9a79094db2c2d557c68fa986b75df811e4
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

HOW TO RUN
    Save in the REPO ROOT, open in VS Code, click Run.

    The v3.32 text is copied verbatim from the protocol so the two
    stores say the same thing. Safe to run after patch_ledger.py --
    they touch different parts of the file.

AFTER RUNNING: run ledger_index.py (the appendix sits outside the
    INDEX zone, but re-running keeps the habit intact).
"""

import os
import sys

TARGET = 'LEDGER_CONSOLIDATED.md'

ENCODING_GATE = 'utf-8'

EDITS = [
    ('APX-1', 'append v3.32, v3.33, v3.34 to the version-history appendix',
     b'### Preserved verbatim: v3.29 Technical lessons (now field notes in skills)',
     b'v3.32 (July 19-20, 2026): Two additions. (1) The anchor requirement\ngeneralized from handoffs to any document leaving a session -- audit\nprompts, review requests, relay manifests, as-builts -- each opens with\n"built on <SHA> at <URL>"; an un-anchored document is unverifiable by a\nreceiving AI with no repo access of its own (Part 1 Key Principles, Part 3\nSHA Round Trip; line 326 corrected to match). (2) The Orrery and the\nAssembler added to Foundation, plus a matching quotable: the assembler\ninherits knowledge from the orrery, not machinery -- it exists to solve a\nproblem the orrery never has -- surfaced via M2 Layer 2 live-Horizons\ntesting (L-149, L-150, L-151). Corrected mid-push: ledger-and-session-\nrecords was already at 1.2 (July 19) when this version was drafted; the\nSkill Manifest table was still showing 1.0, and this entry\'s own first\ndraft nearly re-generalized already-generalized content before the\nmismatch was caught (L-152, retroactive entry). Skill Manifest bumped to\n1.2/1.1/1.1 (ledger-and-session-records / provenance-discipline /\ngallery-cache-builder) to match actual repo state, and a new row added\nfor gallery-assembler (L-151).\n\nv3.33 (July 30, 2026): The Register Rule added to Part 2. The protocol\'s compressed reference voice is distinguished from explanation voice \xe2\x80\x94 lead with the claim, one idea per sentence, no aphorisms in an explanation, gloss project terms on first use each session. Two yes-or-no checks before sending (does this paragraph do one job; does any sentence point at a label instead of saying the thing), with the test being "can Tony act on this without a follow-up question." Backstop: Tony says "opaque" at the point it fails, Claude rewrites that passage, and the miss is captured as a field note so it accumulates rather than repeating. Manifest table refreshed to 1.2/1.1/1.6.\n\nv3.34 (August 5, 2026): Two amendments, both from the Fable skills-layer review. (1) WHO TONY IS: the GitHub Desktop / Run-button preference is stated as a preference where practical, not a prohibition. The earlier "never the git command line" wording read as a ban and put the section in conflict with safe-file-editing\'s git apply delivery format (Fable Job 2 #16); Tony\'s ruling keeps the GUI as default and treats a terminal step as a fallback. The surviving obligation is unchanged: don\'t hand over an operation outside Tony\'s known working set without explaining what it does and what could go wrong. (2) Stale Skill = Stop [CRITICAL] added under the Skill Manifest. A skill lives in three stores \xe2\x80\x94 repo skills/, the account install Claude actually loads, and the generated manifest table. When a loaded skill\'s version disagrees with its manifest row, the session STOPS rather than proceeding and mentioning it later, and asks Tony to push to skills/ and reinstall in Settings. The prior wording asked only to "reconcile before trusting it," and the manifest still advertised 1.1/1.4 against an actual 1.2/1.6 for about three weeks with nothing surfacing it. Supporting change outside the protocol: skills_index.py now prints what the manifest was advertising before overwriting it, so running the tool reports drift instead of silently absorbing it; the prevention side is the binding rule in ledger-and-session-records v1.5.\n\n### Preserved verbatim: v3.29 Technical lessons (now field notes in skills)'),
]



def main():
    root = os.path.dirname(os.path.abspath(__file__))
    rels = []
    for e in EDITS:
        r = e[0] if len(e) == 5 else TARGET
        if r not in rels:
            rels.append(r)

    files, normalized = {}, []
    for rel in rels:
        path = os.path.join(root, rel.replace('/', os.sep))
        if not os.path.exists(path):
            print("ERROR: %s not found. Save this script in the repo root.")
            print("       NOTHING WAS WRITTEN.")
            return 1
        with open(path, 'rb') as f:
            data = f.read()
        if b'\r\n' in data:
            n = data.count(b'\r\n')
            data = data.replace(b'\r\n', b'\n')
            normalized.append((rel, n))
        files[rel] = data

    for rel, n in normalized:
        print("fix CRLF     %s: normalized %d line endings to LF" % (rel, n))

    # Pass 1 -- verify every anchor before writing anything.
    for e in EDITS:
        rel, eid, label, old, new = e if len(e) == 5 else (TARGET,) + e
        c = files[rel].count(old)
        if c != 1:
            print("ANCHOR FAIL: %s (%s) in %s matched %d, expected 1." % (eid, label, rel, c))
            print("             NOTHING WAS WRITTEN. Every file is unchanged.")
            print("             Fix the cause, then RE-RUN this script.")
            return 1

    # Pass 2 -- apply.
    for e in EDITS:
        rel, eid, label, old, new = e if len(e) == 5 else (TARGET,) + e
        files[rel] = files[rel].replace(old, new, 1)
        print("ok  %-10s %s" % (eid, label))

    for rel, data in files.items():
        try:
            data.decode(ENCODING_GATE)
        except UnicodeDecodeError as exc:
            print("ERROR: %s would not be valid %s (%s)." % (rel, ENCODING_GATE, exc))
            print("       NOTHING WAS WRITTEN. Every file is unchanged.")
            return 1

    for rel, data in files.items():
        with open(os.path.join(root, rel.replace('/', os.sep)), 'wb') as f:
            f.write(data)

    print("")
    print("patch applied to %d file(s)%s"
          % (len(files), " (+%d CRLF normalized)" % len(normalized) if normalized else ""))
    return 0


if __name__ == '__main__':
    sys.exit(main())
