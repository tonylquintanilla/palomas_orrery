"""L-223 patch 2 of 2 -- the ledger records the paste instance.

Built on d424c459ef31dbac23b493e43b0b6ad35bf0d495 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).

WHAT THIS DOES

Inserts one new ledger block, L-223, immediately before L-222 in
LEDGER_CONSOLIDATED.md. It records what Tony observed in VS Code on
2026-08-21 -- the perishable half. The durable rule went into
safe-file-editing 1.7 in patch 1 of 2.

The block opens DONE. There is no work owed: the finding is recorded
and its rule is already promoted. What it carries instead is a Note
saying the mechanism was never verified, so a later reader does not
mistake a plausible account for a diagnosis.

WHY IT ANCHORS ON L-222

LEDGER_CONSOLIDATED.md is 579 KB and its exact line wrapping on disk
cannot be verified from outside the machine. So this anchors on the
L-222 header, which is short and unique, and inserts before it. It
does not depend on the surrounding prose.

ledger_index.py will place the block in its correct bucket itself and
regenerate the index. Do not hand-edit the index zone.

HOW TO RUN IT

Save it to the repo root, open it in VS Code, press Run. It takes no
arguments. It writes nothing on any failure. Then run ledger_index.py
twice: the first run may report a placement fix, the second should
report no consistency problems.

Written August 21, 2026 with Anthropic's Claude Opus 5 (L-223).
"""

import os
import sys

PATH = 'LEDGER_CONSOLIDATED.md'
ANCHOR = '#### [L-222]'

BLOCK = """#### [L-223] A paste into the ledger is an unverified transfer
<!-- L:223 status:DONE upd:2026-08-21 section:C flag: -->
- **Observed 2026-08-21, editing LEDGER_CONSOLIDATED.md in VS Code.**
  Tony selected a block and pasted over it. Nothing appeared. He
  repeated the paste several times, still with no visible effect, and
  raised it. He then cut, pasted again, and WAITED -- and the text
  arrived roughly a minute later, complete and correct. He also
  noticed that the spinner ended when he refocused the cursor.
- **What was actually observed, kept separate from what it might
  mean.** Four things: a paste that showed no effect for about a
  minute; a completed, correct paste at the end of that; no
  duplicates from the repeated attempts; and a spinner that resolved
  on refocus. Tony checked for the duplicates specifically, because
  Claude had raised multiple pending pastes as a risk. They were not
  there. Recorded as a checked negative rather than left standing as
  speculation.
- **The mechanism was never verified and this entry does not claim
  one.** Claude's account -- that modern VS Code negotiates several
  clipboard formats with the source application before inserting, and
  that serving a rich flavour from a browser can block -- fits the
  refocus detail and the browser-to-editor path, and is offered as
  plausibility only. Nobody instrumented the editor. A future session
  reading this should treat it as an unexplained observation with a
  candidate attached, not as a diagnosis. If it recurs, one setting
  worth trying is `editor.pasteAs.enabled` set to false, which turns
  off the alternative-paste offers and keeps plain paste.
- **THE FINDING IS NOT THE DELAY. It is that nothing reports the
  outcome.** A paste that dropped and a paste that landed produce the
  same evidence, which is none: no participant in the chain -- source
  application, OS clipboard, editor paste handling, buffer, save --
  owns saying whether the transfer completed. Tony caught this one
  only because he happened to be comparing the paste against the
  copy. That is this project's own confirming question, "what tells
  us it is working," asked of a text editor. Same shape as A Check
  That Cannot Fail Is Not Passing, one layer out from the code.
- **The retry instinct is the hazard the delay creates.** Repeating a
  paste that seems not to have happened is the natural response, and
  it is how one pending transfer becomes two. It did not happen here.
  It is written down because the next person to meet this cold will
  reach for the same response.
- **PROMOTED to `safe-file-editing` 1.7, same day** (Tony's ruling).
  The durable rule is that an edit to a version-controlled file is
  delivered as a patch script INCLUDING prose, markdown and ledger
  files -- because a hand-paste is an unverified transfer, not
  because any editor is buggy. The skill had never said patch
  discipline was for `.py` files only, but every example in it was
  code, and this project had been hand-editing a 579 KB markdown
  ledger on that silence. The rule as written outlives whatever this
  particular stall turns out to be.
- **The human fallback, in Tony's own terms, for when a hand edit is
  unavoidable:** watch until the text actually appears before
  clicking or typing anything else, and do not retry on silence. It
  is what caught this. It is also a person looking, standing in for a
  check the tooling does not perform, which is why it is the fallback
  and the patch is the default.
**Note:** RICE not scored. The item was closed on arrival -- the
observation is recorded and its rule promoted in the same session, so
there is no work to prioritise.
**Ref:** `skills/safe-file-editing/SKILL.md` (A Paste Is An Unverified
Transfer, v1.7); `documentation/patch_L223_1_safe_file_editing_paste_
rule.py`; `documentation/patch_L223_2_ledger_paste_instance.py`;
L-214 (the block being pasted when this surfaced); the resident A
Check That Cannot Fail Is Not Passing gate.

"""


def die(reason):
    print('')
    print('STOPPED. %s' % reason)
    print('Nothing was written.')
    sys.exit(1)


def main():
    if not os.path.isdir('documentation'):
        die('no documentation/ directory here. Run this from the '
            'palomas_orrery repo root.')
    if not os.path.exists(PATH):
        die('%s not found.' % PATH)

    with open(PATH, 'rb') as handle:
        raw = handle.read()
    crlf = raw.count(b'\r\n')
    text = raw.decode('utf-8')
    if crlf:
        text = text.replace('\r\n', '\n')

    if '#### [L-223]' in text:
        die('the ledger already carries an L-223 block. Nothing to do, '
            'or the handle was taken by other work -- read it before '
            'reusing the number.')

    found = text.count(ANCHOR)
    if found != 1:
        die('%s matched %d times, expected exactly 1.' % (ANCHOR, found))

    for char in BLOCK:
        if ord(char) > 127:
            die('non-ASCII character %r in the new block.' % char)

    at = text.index(ANCHOR)
    out = text[:at] + BLOCK + text[at:]

    if out == text:
        die('the file came out identical to its input.')

    if crlf:
        out = out.replace('\n', '\r\n')
    with open(PATH, 'wb') as handle:
        handle.write(out.encode('utf-8'))

    print('%s: L-223 inserted before L-222 (%d characters).'
          % (PATH, len(BLOCK)))
    print('')
    print('NEXT: run ledger_index.py twice. The first run may report a '
          'placement fix and perform it; the second should report no '
          'consistency problems.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
