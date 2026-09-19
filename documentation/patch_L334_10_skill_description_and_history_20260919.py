#!/usr/bin/env python3
"""
patch_L334_10_skill_description_and_history_20260919.py -- ORRERY repo.

Run: save this file in the ORRERY repo ROOT (next to
LEDGER_CONSOLIDATED.md), open it in VS Code and click Run.
Or:  python patch_L334_10_skill_description_and_history_20260919.py

A patch is run from its repository's ROOT and filed in documentation/ AFTER
it has run. Filed first and run second, it stops with one line, writes
nothing, and the push goes out without it.

Built on orrery 071d1f04cb80cba67ae5d7a7c6deb8036612cf14
at https://github.com/tonylquintanilla/palomas_orrery
(gallery d9d7a48f90725f605b95dd39df5fccafe12c3dd3)

TWO REPAIRS TO patch_L334_9, both mine.

ONE. interactive-exhibit 1.4 would not install. Settings > Skills refused
it with "field 'description' in SKILL.md must be at most 1024
characters". Measured: the description is 1042 characters, 18 over. The
file's 35 kB is NOT the problem -- gallery-cache-builder installed fine
and every other skill's description is between 550 and 813. This patch
rewrites that one line to 991 characters, which keeps every subject the
old one named, adds the arrival block, the shell-key stamp and the store
editor, and leaves 33 characters of headroom.

TWO. v3.59 currently lives NOWHERE. patch_L334_9 removed it from
PROJECT_INSTRUCTIONS.md and printed it for Tony to paste by hand, which
is not how this is done -- a patch that deletes an entry from one file
writes it into the other in the same run, or the protocol's own rule
that an entry lives in exactly one place is broken in the direction of
zero. This patch appends it to documentation/PROJECT_INSTRUCTIONS_HISTORY.md,
PART 1, after v3.58 and before the PART 2 separator, with the
moved-down note every earlier entry there carries.

AND ONE LINE ON L-340, recording the 1024-character limit so the next
person to write a skill description knows it before the upload fails,
and proposing that skills_index.py check it -- that generator already
reads every SKILL.md, so it is the place where the check would actually
run rather than be remembered.

WHAT THIS PATCH DOES NOT CHANGE: the skill's version stays 1.4. The body
is untouched; only the frontmatter description line moves. The three
stores still agree once the install succeeds.

THEN (Tony), in this order:
  1. Settings > Skills -- upload skills/interactive-exhibit/SKILL.md
     again. It should save this time.
  2. python ledger_index.py LEDGER_CONSOLIDATED.md -- once is enough,
     nothing opens or closes. Expect "OK: 335" and 193 live items.
  3. python orrery_maintenance_run.py.
  4. Move this script into documentation/, commit and push.

FAILURE: a single ERROR: or ANCHOR FAIL line, and NOTHING is written.
Undo is Discard Changes in GitHub Desktop.

Written September 2026 with Anthropic's Claude Opus 5.
"""
import hashlib
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
ZONE = ('<!-- INDEX:START', '<!-- INDEX:END -->')

FINGERPRINTS = {
    'skills/interactive-exhibit/SKILL.md': '73c28c75ccf25353245a8c33873f7e3b',
    'documentation/PROJECT_INSTRUCTIONS_HISTORY.md':
        'de9c56a296fa00b98f9c8fc9182bc4a0',
    'LEDGER_CONSOLIDATED.md': '98d35e0ad95efecbd8a660f8e93f755d',
}

DESC_OLD = "How an interactive exhibit (a room in interactive.html such as ?exhibit=sun) is designed, built, verified and carded for the Paloma's Orrery gallery. Covers the exhibit switch and boot path, the assembler driver spec, the JS feature handoff, the shared chrome (drawer, nav cluster and frame zoom, i-panel, frame HUD, consent gate, back link), what is per-body, the served-data provenance contract (value / unit / source / orrery_constant pointer, checked by the live store-drift run), the Mode 5 sequence on the phone, and how the exhibit becomes a gallery card through Studio. Use when adding or changing an exhibit (Earth, Jupiter, the stars), when touching sun* chrome in interactive.html, or when deciding what an exhibit may render; when touching the arrival block, the shell-key stamp, or the store editor and its writer. Not for propagation math (gallery-assembler), the nightly data builder (gallery-cache-builder), or the Studio/converter chain for figure cards (gallery-pipeline). Do not use for projects other than Paloma's Orrery."

DESC_NEW = "How an interactive exhibit (a room in interactive.html such as ?exhibit=sun) is designed, built, verified and carded for the Paloma's Orrery gallery. Covers the exhibit switch and boot path, the assembler driver spec, the JS feature handoff, the shared chrome (drawer, nav cluster, frame zoom, i-panel, HUD, consent gate, back link), what is per-body, the served-data provenance contract, what a room opens on (the arrival block) and the shell-key stamp the renderers apply, who may write data/objects_config.json, the Mode 5 phone sequence, and carding an exhibit through Studio. Use when adding or changing an exhibit (Earth, Jupiter, the stars), touching sun* chrome in interactive.html, deciding what an exhibit may render, or editing the served words with store_writer or exhibit_store_editor. Not for propagation math (gallery-assembler), the nightly builder (gallery-cache-builder), or the Studio/converter chain (gallery-pipeline). Do not use for projects other than Paloma's Orrery."

HISTORY_ANCHOR = """(Moved down from the resident protocol on 2026-09-16 when v3.61
made a fourth entry.)

================================================================
PART 2 -- LESSONS REMOVED FROM THE PROTOCOL AT v3.37"""

V359 = """v3.59 (September 14, 2026): ONE RULE REWRITTEN, the Register Rule, on
Tony's instruction of the same evening. No skill bumped.

WHAT THE OLD WORDING GOT WRONG. It opened "plain speech is the default"
and then gave the compressed voice a home in this document and in the
skills. Read together, those two sentences describe a shared shorthand
that simply belongs in a different place. Tony's correction: it is not
shared. He cannot read it and Claude can, so it is a channel with one
party on it.

THE ASYMMETRY IS NOW THE RULE'S REASON rather than a footnote to it.
Claude holds the whole session at once and unpacks a compressed phrase
without effort. Tony is living through the session and cannot, and
noticing that a sentence is too dense already costs him the reading.
Compression is therefore free on one side and expensive on the other,
which is why every earlier version of this rule decayed: nothing in
writing a compressed sentence tells the writer it failed.

SUMMARIES ARE NAMED as where it fails, because that is where it failed
on 2026-09-14. A closing list of decisions names each one rather than
stating it, and a list of names is compressed prose wearing bullet
points. The evening produced four of those before Tony said so.

The three checks, the two supporting defaults and the backstop are
unchanged. What changed is the opening, which is the part that has to
carry the rule when a session is moving.

The header stamp and the SHA anchor move with this entry.

Version history: v3.56 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

(Moved down from the resident protocol on 2026-09-19 when v3.62
made a fourth entry.)
"""

HISTORY_NEW = """(Moved down from the resident protocol on 2026-09-16 when v3.61
made a fourth entry.)

""" + V359 + """
================================================================
PART 2 -- LESSONS REMOVED FROM THE PROTOCOL AT v3.37"""

LEDGER_OLD = """- **AND THE MODE 5 PASS ITSELF**, which is the point of this item."""

LEDGER_NEW = """- **A SKILL DESCRIPTION IS CAPPED AT 1024 CHARACTERS**, learned
  2026-09-19 by the upload refusing: "field 'description' in SKILL.md
  must be at most 1024 characters". interactive-exhibit 1.4 came out at
  1042 and would not install; the 35 kB body was never the problem, and
  gallery-cache-builder at 788 went in fine. Every other skill sits
  between 550 and 813, so this is the first time the ceiling has been
  met. Trimmed to 991 in
  `patch_L334_10_skill_description_and_history_20260919.py`.
  **Claude proposes, unratified:** `skills_index.py` should FAIL a run
  whose SKILL.md description exceeds 1024. It already reads every one of
  them to build the manifest, so it is the place where the check would
  actually run rather than be remembered -- and the failure it catches
  is a skill that cannot be installed, which is invisible until someone
  tries and is easy to abandon halfway.
- **AND THE MODE 5 PASS ITSELF**, which is the point of this item."""


def lf(text):
    return text.replace('\r\n', '\n')


def ledger_fingerprint(content):
    a = content.index(ZONE[0])
    b = content.index(ZONE[1]) + len(ZONE[1])
    return hashlib.md5((content[:a] + content[b:]).encode('utf-8')).hexdigest()


EDITS = {
    'skills/interactive-exhibit/SKILL.md': [(DESC_OLD, DESC_NEW)],
    'documentation/PROJECT_INSTRUCTIONS_HISTORY.md':
        [(HISTORY_ANCHOR, HISTORY_NEW)],
    'LEDGER_CONSOLIDATED.md': [(LEDGER_OLD, LEDGER_NEW)],
}


def main():
    if not os.path.exists(os.path.join(ROOT, 'LEDGER_CONSOLIDATED.md')):
        print('ERROR: LEDGER_CONSOLIDATED.md not found next to this script.')
        print('       Run this patch from the ORRERY repo ROOT, not from')
        print('       documentation/. NOTHING was written.')
        return 1

    loaded = {}
    for rel, want in FINGERPRINTS.items():
        path = os.path.join(ROOT, rel.replace('/', os.sep))
        if not os.path.exists(path):
            print('ERROR: %s not found. NOTHING was written.' % rel)
            return 1
        raw = open(path, 'rb').read()
        text = lf(raw.decode('utf-8'))
        got = (ledger_fingerprint(text) if rel.endswith('LEDGER_CONSOLIDATED.md')
               else hashlib.md5(text.encode('utf-8')).hexdigest())
        if got != want:
            print('ERROR: %s is not the file this patch was built against' % rel)
            print('       expected %s, found %s%s'
                  % (want, got, ' [CRLF]' if b'\r\n' in raw else ''))
            print('       NOTHING was written. Undo is Discard Changes in '
                  'GitHub Desktop.')
            return 1
        loaded[rel] = (text, b'\r\n' in raw)

    out = {}
    for rel, pairs in EDITS.items():
        text = loaded[rel][0]
        for old, new in pairs:
            n = text.count(old)
            if n != 1:
                print('ANCHOR FAIL in %s: expected 1 match, found %d: %r'
                      % (rel, n, old[:70]))
                print('NOTHING was written. Undo is Discard Changes in '
                      'GitHub Desktop.')
                return 1
            text = text.replace(old, new, 1)
        out[rel] = text

    # The whole point of this patch: the description must fit.
    import re
    check = re.search(r'^description: (.*)$',
                      out['skills/interactive-exhibit/SKILL.md'], re.M)
    if check is None or len(check.group(1)) > 1024:
        print('ERROR: the description would still be %s characters. NOTHING '
              'was written.' % (len(check.group(1)) if check else 'unreadable'))
        return 1

    for rel, text in out.items():
        bad = sum(1 for c in text if ord(c) > 127)
        if bad:
            print('ERROR: %s would hold %d non-ASCII character(s). NOTHING '
                  'was written.' % (rel, bad))
            return 1

    for rel, text in out.items():
        path = os.path.join(ROOT, rel.replace('/', os.sep))
        data = text.encode('ascii')
        if loaded[rel][1]:
            data = data.replace(b'\n', b'\r\n')
        open(path, 'wb').write(data)
        print('ok  %-46s (%d bytes%s)'
              % (rel, len(data), ', CRLF preserved' if loaded[rel][1] else ''))
    print('')
    print('interactive-exhibit description: %d characters, %d under the '
          'limit' % (len(check.group(1)), 1024 - len(check.group(1))))
    print('v3.59 is now in PROJECT_INSTRUCTIONS_HISTORY.md PART 1, after')
    print('v3.58 and before the PART 2 separator. It lives in exactly one')
    print('place again.')
    print('')
    print('NEXT, in this order:')
    print('  1. Settings > Skills -- upload skills/interactive-exhibit/'
          'SKILL.md again.')
    print('  2. python ledger_index.py LEDGER_CONSOLIDATED.md (once).')
    print('     Expect "OK: 335" and 193 live items.')
    print('  3. python orrery_maintenance_run.py')
    print('  4. Move this script into documentation/, commit and push.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
