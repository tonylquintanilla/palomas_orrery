"""
patch_ledger_L194_text_only_assertions.py

Adds one new detail block, [L-194], to LEDGER_CONSOLIDATED.md, inserted
after L-193 and before the PENDING ACTION heading. Nothing else is
touched. The index zone is NOT edited by hand -- run ledger_index.py (or
maintenance_run.py, which includes it as a generator) afterwards to
regenerate the index tables.

Base fingerprint taken at repo HEAD 253bcdd, 2026-08-15.

Run:
    Save into the palomas_orrery repo root, open in VS Code, click Run.
    Or: python patch_ledger_L194_text_only_assertions.py

    Then run ledger_index.py the same way to rebuild the index.

Success: one "ok" line, then "patch applied".
Failure: a single ERROR or ANCHOR FAIL line; nothing is written.

Written August 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

LEDGER = 'LEDGER_CONSOLIDATED.md'
BASE_MD5 = 'ef488a89d27d0a58f0378f7fa572de9d'

ANCHOR = (
    b'`patch_L192_verdict_aware_L2b.py`.\n'
    b'\n'
    b'## PENDING ACTION (Tony-side)'
)

ENTRY = b"""`patch_L192_verdict_aware_L2b.py`.

#### [L-194] Text-only assertions -- claims the scanner cannot see
<!-- L:194 status:DEFERRED upd:2026-08-15 section:A flag: rice:4/3/60/5 -->
- **The class.** A qualitative sentence in display text carries no
  number, so the scanner emits no claim for it at all. Claim detection
  in display strings is `NUMERIC_CLAIM_RE` -- a number followed by a
  recognized unit -- and a string literal becomes a scannable unit only
  if it contains one. These sentences are not uncited. They are
  invisible, which is the failure class this project treats as equal to
  uncited.
- **The instance that surfaced it, 2026-08-15.** "Unlike Earth, Mars
  lacks a stratosphere," rendered from `shell_configs.py:1256` --
  `SHELL_CONFIGS` Mars `upper_atmosphere`, key `hover_text`, the key
  `orrery_rendering.py` actually reads. GPT found it unsupported. Raised
  as Break 2 of Fable's worksheet schema review, which cited
  `mars_visualization_shells.py:518`; that is the wrong file, and the
  word stratosphere appears nowhere in that module. The claim is real,
  the citation of it was not. [verified @253bcdd]
- **Population, measured @253bcdd.** Counting display prose strings over
  120 characters -- Claude's cut, not the scanner's -- as
  total / carrying a number+unit / carrying none:
  `shell_configs.py` 143 / 92 / 51; `saturn_visualization_shells.py`
  32 / 10 / 22; `mars_visualization_shells.py` 19 / 6 / 13;
  `jupiter_visualization_shells.py` 25 / 19 / 6;
  `earth_visualization_shells.py` 28 / 27 / 1. The third column is a
  FLOOR, not the total: a string that does contain a number can still
  carry unsourced qualitative sentences beside it.
- **The half that is worse than invisible.** Where a qualitative
  sentence shares a string literal with a numeric one, the scanner
  scores the string on the number, and a `# Source:` on that unit
  covers the whole literal. Mercury's inner core reads "a very large
  metallic core, unlike Earth's which is proportionally smaller" in the
  same string as "Core radius approximately 2020 km." Source the radius
  and the comparison inherits coverage nobody checked. This is
  proximity standing in for attachment one level BELOW the comment-run
  rule L-192 settled -- inside a single string literal rather than
  across a comment run.
- **Tony's governing ruling, 2026-08-15: if the checker cannot verify a
  claim, it should not be asked to do so.** This settles Break 2 of the
  schema review directly. Field 2 keeps a number as its object; it does
  NOT generalize to "the number, OR the claim text quoted verbatim."
  Asking a responder to verdict a claim the tool cannot check produces
  a verdict the tool must then interpret, which is the interpretation
  layer L-193 exists to shrink.
- **And it does not block.** Text-only assertions wait for a future
  refactor and gate nothing in the meantime -- not L-192's schema
  re-cut, not the request builder, not the dispatch errand. Many of
  these sentences came from Gemini and their sources are not readily
  available, so this is a sourcing errand of unknown size rather than a
  scanner patch, and its size is exactly why it must not sit in front
  of work that is ready to move.
- **Avenue Tony named, not yet designed:** a visible in-text marker for
  an unsourced assertion, in the spirit of Wikipedia's "citation
  needed." The attraction is that it makes the gap legible to a READER
  rather than only to a tool. Same move as L-192's orphan report and
  the protocol's Show the Envelope: state the absence, rather than let
  silence read as coverage.
**Note:** kept separate from L-190 deliberately. L-190 is about VALUES
that render from shapes the scanner does not reach -- bare literals
inside function bodies. This is about claims that have no value at all,
which no extension of shape coverage will ever find. Same rule of
Tony's underneath ("anything rendered should be reached by the
scanner"), different mechanism, different fix.
**Note:** RICE is Claude's proposal, unratified. Effort is scored high
because the corpus is large and the sourcing may not exist to be found.
**Gap:** a future refactor decides how an unverifiable rendered claim
is marked and how its absence of provenance is reported. Deferred by
ruling, not blocked by a dependency: nothing has to finish before this
can start, and nothing waits on it.
**Ref:** L-190 (scanner reach, the VALUE form of the same rule); L-191
(display-text duplication -- the same sentence can exist in three
copies with only one live); L-192 (the schema re-cut this waits on, and
its Break 2); L-193 (verdict honesty);
`documentation/FABLE_REVIEW_worksheet_schema.md`.

## PENDING ACTION (Tony-side)"""


L192_ANCHOR = (
    b'  header and already parses. The re-cut is "make the others look '
    b'like\n  the addendum."\n'
)

L192_ENTRY = (
    b'  header and already parses. The re-cut is "make the others look '
    b'like\n  the addendum."\n'
    b'- **Break 2 ruled, 2026-08-15: field 2\'s object stays a NUMBER.**\n'
    b'  Fable asked whether a claim with no number (a rendered qualitative\n'
    b'  sentence) could be verdicted by quoting it verbatim into the value\n'
    b'  cell. Tony: if the checker cannot verify a claim, it should not be\n'
    b'  asked to do so. The class is real and is recorded as L-194;\n'
    b'  it is deferred to a future refactor and blocks nothing here.\n'
    b'- **Break 5 ruled, 2026-08-15: field 3 verdicts the `# Source:` '
    b'line\n'
    b'  only.** `# Ref:` and `# Also:` are pre-printed on the dispatch row '
    b'as\n'
    b'  READ-ONLY context -- visible to the responder, never verdicted, '
    b'never\n'
    b'  read by the tool. One tri-state, and the 65-row count does not '
    b'move.\n'
    b'  Measured @253bcdd: 20 citation blocks in the repo carry more than '
    b'one\n'
    b'  leg, at least 9 of them in the dispatch corpus, all in\n'
    b'  `constants_new.py`. Shapes: Source+Ref (4), Source+Ref+Also (3),\n'
    b'  Source+Also (2). In the normal case the extra legs are a locator '
    b'and\n'
    b'  a corroboration for one authority, not separate claims --\n'
    b'  `SUN_RADIUS_KM` cites IAU 2015 B3, then the paper documenting it,\n'
    b'  then a NASA factsheet. The blocks where the authority is NOT in '
    b'the\n'
    b'  Source line are a malformation, not a schema case, and are '
    b'handled\n'
    b'  as L-195. A schema that bends to fit a bad annotation makes the '
    b'bad\n'
    b'  form permanent.\n'
)

L195_ANCHOR = (
    b'\n## PENDING ACTION (Tony-side)'
)

L195_ENTRY = b'''
#### [L-195] Citation legs -- put the authority in the Source line
<!-- L:195 status:OPEN upd:2026-08-15 section:A flag: rice:2/3/85/1 -->
- **The defect.** `# Source:`, `# Ref:` and `# Also:` do not carry
  consistent roles. In the normal case Source is the authority and the
  others are a locator and a corroboration -- `SUN_RADIUS_KM` cites IAU
  2015 Resolution B3, then Prsa et al. 2016 documenting it, then a NASA
  factsheet. In `ROCHE_LIMIT_RADII` the Source line holds a FORMULA and
  the authority (Murray & Dermott 1999, Sec. 4.6) sits in `# Ref:`.
  Same three labels, inverted roles.
- **Why it matters now.** L-192's Break 5 ruling makes field 3 verdict
  the Source line only. That rule is correct for the normal case and
  silently wrong wherever the authority is elsewhere: the row would
  read CITATION RIGHT while the actual authority went unchecked. The
  ruling is what makes this a defect rather than a style quibble.
- **Scope, measured @253bcdd.** 20 multi-leg citation blocks in the
  repo, 17 of them in `constants_new.py`. At least 9 sit in the
  dispatch corpus. Not every one is malformed -- most are the normal
  shape -- so the errand is to read 20 blocks and move the authority
  into Source where it is not already there. My scan breaks a block on
  an unlabeled continuation comment, so 20 is a floor.
- **Not a vocabulary change.** The labels stay. What is being fixed is
  which line the authority sits on, so that one rule reads the same
  thing in every block.
**Note:** RICE is Claude's proposal, unratified. Effort is low -- this
is a bounded read of 20 blocks in mostly one file.
**Gap:** enumerate the 20 blocks, identify the ones whose authority is
not in Source, move it, and re-run the checker. Do this before the
first dispatch that relies on the Break 5 rule.
**Ref:** L-192 (Break 5, the rule this makes true); L-186 (annotation
grammar); `documentation/FABLE_REVIEW_worksheet_schema.md` item 5.

## PENDING ACTION (Tony-side)'''


def fingerprint(data):
    return hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()


def main():
    if not os.path.exists(LEDGER):
        print('ERROR: not found: %s' % LEDGER)
        print('       run this from the palomas_orrery repo root.')
        return 1

    with open(LEDGER, 'rb') as handle:
        data = handle.read()

    got = fingerprint(data)
    if got != BASE_MD5:
        print('ERROR: base moved: %s' % LEDGER)
        print('       expected %s' % BASE_MD5)
        print('       found    %s' % got)
        print('       nothing written. Re-pull or re-anchor.')
        return 1

    if b'L:194' in data or b'L:195' in data:
        print('ERROR: L-194 or L-195 already present. Nothing written.')
        return 1

    old, new = ANCHOR, ENTRY
    if data.count(b'\r\n') > 0:
        old = old.replace(b'\n', b'\r\n')
        new = new.replace(b'\n', b'\r\n')

    count = data.count(old)
    if count != 1:
        print('ANCHOR FAIL (%d matches): L-193 Ref line / PENDING ACTION'
              % count)
        print('       nothing written.')
        return 1

    data = data.replace(old, new)
    print('  ok  L-194 inserted after L-193')

    old2, new2 = L192_ANCHOR, L192_ENTRY
    if data.count(b'\r\n') > 0:
        old2 = old2.replace(b'\n', b'\r\n')
        new2 = new2.replace(b'\n', b'\r\n')
    count2 = data.count(old2)
    if count2 != 1:
        print('ANCHOR FAIL (%d matches): L-192 schema bullet' % count2)
        print('       nothing written.')
        return 1
    data = data.replace(old2, new2)
    print('  ok  L-192 Break 2 + Break 5 rulings recorded')

    old3, new3 = L195_ANCHOR, L195_ENTRY
    if data.count(b'\r\n') > 0:
        old3 = old3.replace(b'\n', b'\r\n')
        new3 = new3.replace(b'\n', b'\r\n')
    count3 = data.count(old3)
    if count3 != 1:
        print('ANCHOR FAIL (%d matches): PENDING ACTION heading' % count3)
        print('       nothing written.')
        return 1
    data = data.replace(old3, new3)
    print('  ok  L-195 inserted after L-194')

    with open(LEDGER, 'wb') as handle:
        handle.write(data)
    print('patch applied: %s (%d bytes)' % (LEDGER, len(data)))
    print('NEXT: run ledger_index.py to regenerate the index tables.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
