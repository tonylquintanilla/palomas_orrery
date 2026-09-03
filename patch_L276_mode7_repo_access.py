"""patch_L276_mode7_repo_access.py

Ledger handle L-276. PROJECT_INSTRUCTIONS.md to v3.53.

WHAT CHANGES
  PROJECT_INSTRUCTIONS.md
    - Part 1, Mode 7, "Documents as handoffs": the clause that said the
      receiving AI "has zero independent repo access" is replaced. It was
      false -- Fable cloned the repo for the L-191 review, and Tony ruled
      2026-09-02 that every model queried here can reach GitHub. The
      anchor REQUIREMENT stands; only its stated reason changes.
    - Part 1, Mode 7, AI Roles: a note on HOW each partner reads the repo,
      so the next session does not rediscover it. Claude and GPT fetch
      live at a SHA. Gemini's web app imports one public repository as a
      snapshot; it cannot read a GitHub URL from a prompt, cannot fetch by
      SHA, and cannot see commit history (Google's own documentation for
      the feature, read 2026-09-03).
    - Header: v3.52 -> v3.53, date, cut-from SHA.
    - Version History: new v3.53 entry at the top; v3.50 REMOVED per the
      mechanical rule (a fourth entry pushes the oldest down). Moved
      byte-exact, not retyped.
  documentation/PROJECT_INSTRUCTIONS_HISTORY.md
    - v3.50's entry appended to PART 1 after v3.49, with the note that
      says when and why it moved.
  documentation/project_instructions_v3_53.md
    - NEW. The archived copy, written from the patched document so the
      archive and the live file agree byte for byte.
  LEDGER_CONSOLIDATED.md
    - L-276 closed (DONE).

RUN ORDER
  AFTER patch_L277_reanchor_site_stores.py. That patch edits the ledger;
  this one does too. The protocol and history files are fingerprinted
  against orrery faac433f (they are untouched by L-277). The ledger edit
  is anchor-guarded rather than fingerprinted, because the maintenance
  run regenerates the ledger's index zone and the fingerprint would
  depend on whether that run happened in between; each ledger anchor
  must match exactly once or nothing is written.

HOW TO RUN
  Save in the ORRERY repo root, open in VS Code, press Run. Command line
  equivalent: python patch_L276_mode7_repo_access.py
  Then the maintenance run (the skill manifest should come back
  unchanged), commit, push, and RE-UPLOAD PROJECT_INSTRUCTIONS.md to the
  UI -- the resident copy is a third store this patch cannot reach.

GUARDS
  All anchors must match exactly once. Both fingerprinted files must
  match. The archive must not already exist. All-or-nothing: nothing is
  written until every edit has been planned. Inserted text is ASCII;
  each file keeps its own line endings. No .bak: undo is Discard Changes
  in GitHub Desktop, plus deleting the new archive file.

Built on orrery faac433f138564d1426835b80ed56562a3ccb5c9 at
https://github.com/tonylquintanilla/palomas_orrery (branch main),
with patch_L277_reanchor_site_stores.py applied.

Module updated: September 3, 2026 with Anthropic's Claude Fable 5.1.
"""

import hashlib
import os
import sys

PROTO = 'PROJECT_INSTRUCTIONS.md'
HIST = os.path.join('documentation', 'PROJECT_INSTRUCTIONS_HISTORY.md')
LEDGER = 'LEDGER_CONSOLIDATED.md'
ARCHIVE = os.path.join('documentation', 'project_instructions_v3_53.md')

EXPECTED = {
    PROTO: 'be04753b864b61d42c71a96b8661957c',
    HIST:  'b1c06d5ce90dff0d33f220dfc0be278e',
}

HEADER_OLD = 'Tony Quintanilla, PE | Claude | v3.52 | September 2, 2026\n'
HEADER_NEW = 'Tony Quintanilla, PE | Claude | v3.53 | September 3, 2026\n'
SHA_OLD = 'Cut from e71f38ae at https://github.com/tonylquintanilla/palomas_orrery\n'
SHA_NEW = 'Cut from faac433f at https://github.com/tonylquintanilla/palomas_orrery\n'

CLAUSE_OLD = """- Documents as handoffs: Copy/paste AI responses to share context --
  every outbound document (audit prompt, review request, relay
  manifest) opens with built on <SHA> at <URL>, same as a handoff;
  the receiving AI has zero independent repo access, so an
  un-anchored document is unverifiable input.
"""
CLAUSE_NEW = """- Documents as handoffs: Copy/paste AI responses to share context --
  every outbound document (audit prompt, review request, relay
  manifest) opens with built on <SHA> at <URL>, same as a handoff.
  The repo moves, so an un-anchored document does not say which
  state it describes. A partner that can fetch needs the anchor to
  fetch the right bytes; a partner that cannot needs it to know what
  it is reading.
"""

ROLES_OLD = """Claude (other instance)  Same-capability relay: audit, manifest, bulk implementation

Patterns:
"""
ROLES_NEW = """Claude (other instance)  Same-capability relay: audit, manifest, bulk implementation

How each partner reads the repo (checked 2026-09-03, L-276): Claude and
GPT fetch GitHub live and can read a file at a pinned SHA. Gemini's web
app IMPORTS one public repository as a snapshot of HEAD at that moment;
it cannot read a GitHub URL given in a prompt, cannot fetch at a SHA,
and cannot see commit history, and the import is not available in the
mobile app. So for Gemini the anchor says which state its imported copy
corresponds to -- the second case in the clause below.

Patterns:
"""

V350_START = 'v3.50 (August 31, 2026): No rule changed in this document. One skill\n'
V350_END = ('Version history: v3.47 moves down to\n'
            'documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three\n'
            'resident.\n\n')

V352_START = 'v3.52 (September 2, 2026): No rule changed in this document. One skill\n'

V353 = """v3.53 (September 3, 2026): One clause corrected, one note added. No
skill changed.

MODE 7 SAID RELAY PARTNERS CANNOT READ THE REPO, AND THEY CAN (L-276).
The "Documents as handoffs" clause gave as its reason that "the
receiving AI has zero independent repo access." This project's own
records disproved it: the L-191 relay response records Fable running
`git ls-remote` against the pinned SHA and parsing the source, and
Tony ruled 2026-09-02 that every model queried here reaches GitHub.
The anchor requirement is unchanged. Its reason now covers both kinds
of partner: the repo moves, so an un-anchored document does not say
which state it describes; one that can fetch needs the anchor to fetch
the right bytes, one that cannot needs it to know what it is reading.

The failure that surfaced it is the lesson. A session read the L-191
relay response, which says plainly that Fable cloned the repo, and
then repeated the blanket sentence anyway -- a general claim in a
trusted document held over specific evidence already in hand. The
same shape as trusting a handoff over the render, one layer up.

THE GEMINI NOTE, on Tony's question 2026-09-03: how does Gemini see the
repo without an upload or Drive? Google's documentation for the Gemini
web app answers it: one public repository can be IMPORTED as a
snapshot, but a GitHub URL in a prompt is not read, nothing is fetched
at a SHA, commit history is not visible, and the feature is not on
mobile. Written under AI Roles so the next session does not rediscover
it. Gemini is the second case in the corrected clause.

Version history: v3.50 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

"""

HIST_ANCHOR = """(Moved down from the resident protocol on 2026-09-02 when v3.52
made a fourth entry.)
"""
MOVED_NOTE = """
(Moved down from the resident protocol on 2026-09-03 when v3.53
made a fourth entry.)
"""

LEDGER_META_OLD = '<!-- L:276 status:OPEN upd:2026-09-02 section:A flag: rice:3/3/95/1 -->\n'
LEDGER_META_NEW = '<!-- L:276 status:DONE upd:2026-09-03 section:A flag: rice:3/3/95/1 -->\n'
LEDGER_GAP_OLD = """- Tony-action (do): run the PROJECT_INSTRUCTIONS.md patch when it is
  built; it is a one-clause edit plus a version bump.
**Gap:** patch not yet built. Wording above is proposed, not approved.
**Ref:** PROJECT_INSTRUCTIONS.md Part 1 Mode 7;
documentation/RELAY_RESPONSE_L191_survey_fable_20260821.md; L-191.
"""
LEDGER_GAP_NEW = """- **Closed 2026-09-03 by `patch_L276_mode7_repo_access.py`**, protocol
  v3.53. Wording approved by Tony as proposed. On his question -- how
  does Gemini see the repo without an upload or Drive? -- Google's own
  documentation for the Gemini web app: one public repository can be
  imported as a snapshot; a GitHub URL in a prompt is not read; nothing
  is fetched at a SHA; commit history is not visible; not available on
  mobile. Written into Mode 7's AI Roles so it does not have to be
  rediscovered. Gemini is the second case in the corrected clause.
**Gap:** none. The UI copy of PROJECT_INSTRUCTIONS.md is the third
store; Tony re-uploads it after the push.
**Ref:** PROJECT_INSTRUCTIONS.md Part 1 Mode 7 (v3.53);
documentation/RELAY_RESPONSE_L191_survey_fable_20260821.md; L-191.
"""


def fail(msg):
    print('')
    print('FAILURE: %s' % msg)
    print('NOTHING was written. No file on disk has changed.')
    print('If a previous run did write, undo is Discard Changes in GitHub')
    print('Desktop and delete documentation/project_instructions_v3_53.md.')
    sys.exit(1)


def read_lf(path):
    raw = open(path, 'rb').read()
    was_crlf = b'\r\n' in raw
    return (raw.replace(b'\r\n', b'\n') if was_crlf else raw), was_crlf


def write_back(path, text, crlf):
    data = text.encode('ascii')
    if crlf:
        data = data.replace(b'\n', b'\r\n')
    with open(path, 'wb') as f:
        f.write(data)


def once(hay, needle, where):
    n = hay.count(needle)
    if n != 1:
        fail('anchor matched %d times (expected 1) in %s:\n    %r'
             % (n, where, needle[:80]))


def main():
    print('patch_L276 -- PROJECT_INSTRUCTIONS.md to v3.53')
    print('=' * 56)

    for text in (HEADER_NEW, SHA_NEW, CLAUSE_NEW, ROLES_NEW, V353,
                 MOVED_NOTE, LEDGER_META_NEW, LEDGER_GAP_NEW):
        try:
            text.encode('ascii')
        except UnicodeEncodeError as exc:
            fail('non-ASCII in replacement text: %s' % exc)

    for fn in (PROTO, HIST, LEDGER):
        if not os.path.exists(fn):
            fail('%s not found. Run this from the ORRERY repo root.' % fn)
    if os.path.exists(ARCHIVE):
        fail('%s already exists. This patch has run.' % ARCHIVE)

    proto, proto_crlf = read_lf(PROTO)
    hist, hist_crlf = read_lf(HIST)
    ledger, ledger_crlf = read_lf(LEDGER)

    for fn, content, crlf in ((PROTO, proto, proto_crlf), (HIST, hist, hist_crlf)):
        actual = hashlib.md5(content).hexdigest()
        if actual != EXPECTED[fn]:
            fail('BASE MOVED for %s.\n  expected %s\n  found    %s\n'
                 '  Built against orrery faac433f.' % (fn, EXPECTED[fn], actual))
        print('  %-46s fingerprint matches%s' % (fn, ' [CRLF]' if crlf else ''))
    if b'v3.53' in proto:
        fail('%s already mentions v3.53. This patch has run.' % PROTO)

    p = proto.decode('ascii', 'strict')
    h = hist.decode('ascii', 'strict')
    lg = ledger.decode('utf-8', 'strict')

    # --- lift the v3.50 entry, byte-exact ---------------------------------
    once(p, V350_START, PROTO)
    once(p, V350_END, PROTO)
    i = p.index(V350_START)
    j = p.index(V350_END, i) + len(V350_END)
    v350 = p[i:j]
    print('  v3.50 entry located, %d chars' % len(v350))

    # --- plan every edit before writing ------------------------------------
    for needle in (HEADER_OLD, SHA_OLD, CLAUSE_OLD, ROLES_OLD, V352_START):
        once(p, needle, PROTO)
    once(h, HIST_ANCHOR, HIST)
    once(lg, LEDGER_META_OLD, LEDGER)
    once(lg, LEDGER_GAP_OLD, LEDGER)
    if 'L-277' not in lg or 'patch_L277_reanchor_site_stores.py' not in lg:
        fail('the ledger does not carry the L-277 patch record; run '
             'patch_L277_reanchor_site_stores.py first.')

    p = p.replace(HEADER_OLD, HEADER_NEW)
    p = p.replace(SHA_OLD, SHA_NEW)
    p = p.replace(CLAUSE_OLD, CLAUSE_NEW)
    p = p.replace(ROLES_OLD, ROLES_NEW)
    p = p.replace(V352_START, V353 + V352_START)
    p = p.replace(v350, '')
    h = h.replace(HIST_ANCHOR, HIST_ANCHOR + '\n' + v350.rstrip('\n') + '\n' + MOVED_NOTE)
    lg = lg.replace(LEDGER_META_OLD, LEDGER_META_NEW)
    lg = lg.replace(LEDGER_GAP_OLD, LEDGER_GAP_NEW)

    # post-conditions
    if p.count('v3.50 (August 31, 2026)') != 0:
        fail('v3.50 entry still present in the protocol after removal')
    if h.count('v3.50 (August 31, 2026)') != 1:
        fail('v3.50 entry not landed exactly once in the history file')
    for needle in ('v3.53 (September 3, 2026)', 'v3.52 (September 2, 2026)',
                   'v3.51 (August 31, 2026)'):
        if p.count(needle) != 1:
            fail('resident Version History does not hold exactly one %s' % needle)
    # The phrase survives exactly once: quoted inside the v3.53 entry
    # that records its removal. Anywhere else means the clause survived.
    if p.count('zero independent repo access') != 1:
        fail('the old clause survived outside the v3.53 history entry')

    # --- write --------------------------------------------------------------
    write_back(PROTO, p, proto_crlf)
    write_back(HIST, h, hist_crlf)
    data = lg.encode('utf-8')
    if ledger_crlf:
        data = data.replace(b'\n', b'\r\n')
    with open(LEDGER, 'wb') as f:
        f.write(data)
    write_back(ARCHIVE, p, proto_crlf)

    print('  wrote %s (v3.53; header, anchor, clause, Gemini note, history)' % PROTO)
    print('  wrote %s (v3.50 appended to PART 1)' % HIST)
    print('  wrote %s (L-276 DONE)' % LEDGER)
    print('  wrote %s (archived copy)' % ARCHIVE)
    print('')
    print('patch applied. Next: maintenance run (manifest should be')
    print('unchanged), commit, push, then RE-UPLOAD PROJECT_INSTRUCTIONS.md')
    print('to the UI.')


if __name__ == '__main__':
    main()
