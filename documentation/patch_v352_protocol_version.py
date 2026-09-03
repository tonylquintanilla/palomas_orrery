"""
patch_v352_protocol_version.py -- PROJECT_INSTRUCTIONS.md to v3.52.

Built on palomas_orrery e71f38aee761036db9a819c694dc8b76a0d73318 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Gallery at 4d33c80960595102041de870530ffa8da5bae519.

WHY

  The generated skill manifest inside PROJECT_INSTRUCTIONS.md changed
  tonight -- gallery-assembler 1.1 -> 1.2 -- so the document changed, and
  by the precedent v3.50 and v3.51 set (both "no rule changed, one skill
  bump") that is a version bump.

  It also repairs something older. The header line has read v3.49 since
  August 30 while the document's own Version History carries v3.50 and
  v3.51 entries. The history travelled and the header did not. Tony
  found it, 2026-09-02.

WHAT IT DOES

  PROJECT_INSTRUCTIONS.md
    - header v3.49 / August 30 -> v3.52 / September 2, 2026
    - SHA anchor ded99fbe -> e71f38ae
    - new v3.52 entry at the top of Version History
    - v3.49's entry REMOVED, per the mechanical rule: a fourth entry
      pushes the oldest down. Moved byte-exact, not retyped.

  documentation/PROJECT_INSTRUCTIONS_HISTORY.md
    - v3.49's entry appended to PART 1, after v3.48, with the note that
      says when and why it moved.

  documentation/project_instructions_v3_52.md
    - NEW. The archived copy, written from the patched document so the
      archive and the live file agree byte for byte.

NOT DONE, and recorded rather than fixed
  There are no archived copies for v3.50 or v3.51 -- documentation/ stops
  at v3_49. Their content is fully carried by their Version History
  entries, which are resident, and git holds the exact bytes. The v3.52
  entry says so. Reconstructing them from git is a separate decision and
  a separate patch.

HOW TO RUN
  Open in VS Code from the ORRERY repo root and press Run. Then run the
  maintenance runner (the manifest should come back unchanged), commit,
  push, and RE-UPLOAD PROJECT_INSTRUCTIONS.md to the UI -- the resident
  copy is a third store and this patch cannot reach it.

GUARDS
  Both edited files fingerprinted, every anchor verified once before any
  write, all-or-nothing. The archive is refused if it already exists. No
  .bak. Undo is Discard Changes in GitHub Desktop, plus deleting the new
  archive file.

Module created: September 2, 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

PROTO = 'PROJECT_INSTRUCTIONS.md'
HIST = os.path.join('documentation', 'PROJECT_INSTRUCTIONS_HISTORY.md')
ARCHIVE = os.path.join('documentation', 'project_instructions_v3_52.md')

EXPECTED = {
    PROTO: 'ef1fd66d9875db1cb729d51ad9082bcf',
    HIST:  '9bd4ebda91e18b0002a177f7d9d2a3fd',
}

HEADER_ANCHOR = 'Tony Quintanilla, PE | Claude | v3.49 | August 30, 2026\n'
HEADER_NEW = 'Tony Quintanilla, PE | Claude | v3.52 | September 2, 2026\n'

SHA_ANCHOR = 'Cut from ded99fbe at https://github.com/tonylquintanilla/palomas_orrery\n'
SHA_NEW = 'Cut from e71f38ae at https://github.com/tonylquintanilla/palomas_orrery\n'

# The v3.49 entry, to be lifted whole. Both markers verified unique.
V349_START = 'v3.49 (August 30, 2026): One rule added, in two pieces and two tiers.\n'
V349_END = ('Version history: v3.46 moved down to\n'
            'documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three\n'
            'resident.\n\n')

V351_START = 'v3.51 (August 31, 2026): No rule changed in this document. One skill\n'

V352 = """v3.52 (September 2, 2026): No rule changed in this document. One skill
bump, and a header that had stopped travelling.

gallery-assembler 1.1 -> 1.2 (L-279). Mode 5 as MEASUREMENT, not just
acceptance, plus a field note on mutating a plot from inside a Plotly
event handler.

The skill already owned this and was not used. Its `fires_when` line
said "Mode 5 acceptance" before tonight, and Claude version-checked the
skill during a four-hour hang investigation without ever opening it --
including at the moment of handing over a patch whose own output said
"this one needs Mode 5". The wording was the reason: acceptance reads as
judging something FINISHED, and nothing about a page that will not
respond sounds like acceptance. The trigger now names the diagnostic
case in the words Tony would use -- it hangs, it is unresponsive, it
worked yesterday.

The seven rules in that section are each attached to a failure that
earned them. Three came from stating conclusions about trials whose
CONDITIONS had been inferred rather than recorded, and Tony carried
every one of those corrections. That is the load this protocol exists to
spare him, and it is why the placement question was worth the time it
took. Tony's ruling: the home existed; use it.

THE HEADER HAD BEEN STALE SINCE v3.50. This line read v3.49 while the
document's own Version History carried v3.50 and v3.51 entries -- the
correction travelled into the history and stopped there, which is The
Correction Does Not Travel pointed at the version stamp itself. Fixed
here, along with the SHA anchor, which had also sat at `ded99fbe` across
three versions.

One gap recorded rather than closed: documentation/ has no archived copy
for v3.50 or v3.51. Their content is carried in full by their resident
Version History entries and git holds the exact bytes, so nothing is
lost; reconstructing the two files is a separate decision.

One obligation this bump cannot discharge from inside the session that
made it. A skill lives in three stores, and the account install is the
copy Claude actually loads; a reinstall is invisible to the running
conversation. So: gallery-assembler went to 1.2 at `e71f38ae`, the
session that bumped it had loaded 1.1, and the next session confirms its
loaded copy reads 1.2 before doing gallery work.

Version history: v3.49 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

"""

HIST_ANCHOR = """(Moved down from the resident protocol on 2026-08-31 when v3.51
made a fourth entry.)
"""

MOVED_NOTE = """
(Moved down from the resident protocol on 2026-09-02 when v3.52
made a fourth entry.)
"""


def fail(msg):
    print('')
    print('FAILURE: %s' % msg)
    print('NOTHING was written. No file on disk has changed.')
    print('If a previous run did write, undo is Discard Changes in GitHub')
    print('Desktop and delete documentation/project_instructions_v3_52.md.')
    sys.exit(1)


def read_lf(path):
    raw = open(path, 'rb').read()
    was_crlf = b'\r\n' in raw
    return (raw.replace(b'\r\n', b'\n') if was_crlf else raw), was_crlf


def once(hay, needle, where):
    n = hay.count(needle)
    if n != 1:
        fail('anchor matched %d times (expected 1) in %s:\n    %r'
             % (n, where, needle[:80]))


def main():
    print('patch_v352 -- PROJECT_INSTRUCTIONS.md to v3.52')
    print('=' * 56)

    for text in (HEADER_NEW, SHA_NEW, V352, MOVED_NOTE):
        try:
            text.encode('ascii')
        except UnicodeEncodeError as exc:
            fail('non-ASCII in replacement text: %s' % exc)

    for fn in (PROTO, HIST):
        if not os.path.exists(fn):
            fail('%s not found. Run this from the ORRERY repo root.' % fn)
    if os.path.exists(ARCHIVE):
        fail('%s already exists. This patch has run.' % ARCHIVE)

    proto, proto_crlf = read_lf(PROTO)
    hist, hist_crlf = read_lf(HIST)

    for fn, content, crlf in ((PROTO, proto, proto_crlf), (HIST, hist, hist_crlf)):
        actual = hashlib.md5(content).hexdigest()
        if actual != EXPECTED[fn]:
            fail('BASE MOVED for %s.\n  expected %s\n  found    %s\n'
                 '  Built against orrery e71f38ae. A size delta of about one\n'
                 '  byte per line is CRLF, not content.'
                 % (fn, EXPECTED[fn], actual))
        print('  %-46s fingerprint matches%s'
              % (fn, ' [CRLF]' if crlf else ''))

    if b'v3.52' in proto:
        fail('%s already mentions v3.52. This patch has run.' % PROTO)

    p = proto.decode('ascii', 'strict')

    # --- lift the v3.49 entry, byte-exact --------------------------------
    once(p, V349_START, PROTO)
    once(p, V349_END, PROTO)
    i = p.index(V349_START)
    j = p.index(V349_END, i) + len(V349_END)
    v349 = p[i:j]
    print('  v3.49 entry located, %d chars' % len(v349))

    # --- edits ------------------------------------------------------------
    once(p, HEADER_ANCHOR, PROTO)
    once(p, SHA_ANCHOR, PROTO)
    once(p, V351_START, PROTO)

    p = p.replace(HEADER_ANCHOR, HEADER_NEW)
    p = p.replace(SHA_ANCHOR, SHA_NEW)
    p = p.replace(V351_START, V352 + V351_START)
    p = p.replace(v349, '')
    print('  protocol: 4 edits applied')

    h = hist.decode('ascii', 'strict')
    once(h, HIST_ANCHOR, HIST)
    h = h.replace(HIST_ANCHOR, HIST_ANCHOR + '\n' + v349.rstrip('\n')
                  + '\n' + MOVED_NOTE)
    print('  history: v3.49 appended after v3.48')

    # --- write ------------------------------------------------------------
    out_p = p.encode('ascii')
    with open(PROTO, 'wb') as f:
        f.write(out_p.replace(b'\n', b'\r\n') if proto_crlf else out_p)
    print('  wrote %s' % PROTO)

    out_h = h.encode('ascii')
    with open(HIST, 'wb') as f:
        f.write(out_h.replace(b'\n', b'\r\n') if hist_crlf else out_h)
    print('  wrote %s' % HIST)

    # The archive is written FROM the patched file on disk, so the two
    # cannot disagree. Line endings copied verbatim.
    with open(PROTO, 'rb') as f:
        written = f.read()
    with open(ARCHIVE, 'wb') as f:
        f.write(written)
    print('  wrote %s' % ARCHIVE)

    # --- post-conditions, read back from disk ----------------------------
    print('')
    print('Post-conditions (read back from disk):')
    disk_p = read_lf(PROTO)[0].decode('utf-8', 'replace')
    disk_h = read_lf(HIST)[0].decode('utf-8', 'replace')
    disk_a = read_lf(ARCHIVE)[0].decode('utf-8', 'replace')

    ok = True
    for label, text, needle, want in [
        ('header reads v3.52',   disk_p, 'v3.52 | September 2, 2026', True),
        ('header v3.49 gone',    disk_p, 'v3.49 | August 30, 2026', False),
        ('anchor updated',       disk_p, 'Cut from e71f38ae at', True),
        ('v3.52 entry present',  disk_p, 'v3.52 (September 2, 2026):', True),
        ('v3.49 entry gone',     disk_p, V349_START.strip(), False),
        ('v3.51 still resident', disk_p, 'v3.51 (August 31, 2026):', True),
        ('v3.50 still resident', disk_p, 'v3.50 (August 31, 2026):', True),
        ('v3.49 in history',     disk_h, V349_START.strip(), True),
        ('move note in history', disk_h, 'when v3.52\nmade a fourth entry.', True),
        ('archive matches head', disk_a, 'v3.52 | September 2, 2026', True),
    ]:
        hit = needle in text
        print('  %-24s %s' % (label, hit == want))
        if hit != want:
            ok = False

    # Exactly three version entries may stay resident. This counts them
    # rather than trusting that one was removed.
    import re
    resident = len(re.findall(r'^v3\.\d+ \(', disk_p, re.M))
    print('  %-24s %d (want 3)' % ('resident entries', resident))
    if resident != 3:
        ok = False

    # The archive must be byte-identical to the live document, not merely
    # similar -- an archive that drifts is worse than none.
    same = (open(PROTO, 'rb').read() == open(ARCHIVE, 'rb').read())
    print('  %-24s %s' % ('archive byte-identical', same))
    if not same:
        ok = False

    if not ok:
        print('')
        print('POST-CONDITION FAILED. Undo is Discard Changes in GitHub')
        print('Desktop, and delete %s.' % ARCHIVE)
        sys.exit(1)

    print('')
    print('DONE. v3.52 in the repo, v3.49 moved down, archive written.')
    print('')
    print('Three stores, and this patch reached one:')
    print('  1. Repo -- done. Run the maintenance runner (the manifest')
    print('     should come back unchanged), then commit and push.')
    print('  2. UI -- RE-UPLOAD PROJECT_INSTRUCTIONS.md. The resident copy')
    print('     is what a session actually reads and this cannot touch it.')
    print('  3. gallery-assembler in Settings > Skills -- already done')
    print('     tonight, and the next session still has to confirm its')
    print('     loaded copy reads 1.2.')


if __name__ == '__main__':
    main()
