"""patch_L221_2_critical_path_update.py

Built on 79729c98fd6bec8703fcc3bbc0806e6ee5226770 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Gallery at 109162bbb8d291bce615d888557498a9342d4642.
Written August 20, 2026 with Anthropic's Claude Opus 5.

WHY NOW, AND WHY THIS FILE

L-221 ruled that the master plan restamps at key JUNCTURES rather than
at every change. The reconciliation queue closing is a juncture: this
file's own text describes that queue as open and describes findings
that have since been decided.

Named for L-221 because that is the item that says when a master plan
is due. The content is L-210's outcome. That cross-handle mismatch is
L-219's open gap, recorded rather than worked around.

WHAT IT CHANGES -- five edits, no restructure

  1. The header re-anchors to 79729c98 / 109162bb, dated August 20, and
     says what moved rather than only that something did.

  2. THE STREAMER BELT CLAIM IS CORRECTED, and this is the one that
     matters. The file currently says the row "cites a paper inverted:
     the cited 6 R_sun is that paper's FLOOR." That was Claude's
     reading, carried into this document as fact. An independent source
     read on 2026-08-20 found otherwise: DeForest's 6 R_sun is the
     inbound-wave DETECTION THRESHOLD, not a floor on streamer extent,
     and the paper's streamer-belt result is an Alfven surface at >= 17
     R_sun. Neither cited work supports the 4-6 R_sun range the row
     carried. The value held as a declared drawing choice; the citation
     went. Leaving the old sentence would leave a wrong claim in the
     document a cold reader trusts most.

  3. The verification figures move from 110 claims to the current 107,
     with the routing counts that go with them.

  4. A new paragraph records the queue closing: four rows decided, what
     each decision was, and that three of them turned on material the
     request builder had been dropping.

  5. The footer restamps.

NOT CHANGED, on purpose. The five steps, the end goal, and the
one-fact-that-organizes-everything sections are untouched. The shape of
the work did not move today; only the position along it did.

AFTER RUNNING
  Re-run the maintenance runner.
  Move this script to documentation/.
"""

import hashlib
import os
import sys

BASE_SHA = '79729c98fd6bec8703fcc3bbc0806e6ee5226770'
GALLERY_SHA = '109162bbb8d291bce615d888557498a9342d4642'

TARGET = os.path.join('documentation',
                      'MASTER_PLAN_CRITICAL_PATH_SUMMARY.md')
FINGERPRINT_LF = '6397dcca741ebe699cbba2847005b5ae'

# ------------------------------------------------------------------
# 1 -- header anchor
# ------------------------------------------------------------------

HEAD_OLD = (
    "**Updated August 19, 2026.** Orrery at\n"
    "`9ffb9b403a7d62090b30a9acf9adbc6180a6baec`, gallery at\n"
    "`ff18d3e6fa31f70a8f525df471e751d046cf14fa`. Both confirmed by live\n"
    "check. First written August 16 at `227f5b2d`; the structure below is\n"
    "unchanged from that version. The figures moved, and one claim\n"
    "reversed: the first dispatch has now gone out and come back.\n"
)

HEAD_NEW = (
    "**Updated August 20, 2026.** Orrery at\n"
    "`79729c98fd6bec8703fcc3bbc0806e6ee5226770`, gallery at\n"
    "`109162bbb8d291bce615d888557498a9342d4642`. Both confirmed by live\n"
    "check. First written August 16 at `227f5b2d`; the structure below is\n"
    "unchanged from that version -- the five steps have not moved, only\n"
    "our position along them.\n"
    "\n"
    "Two things changed on August 20. The reconciliation queue that had\n"
    "been open for two sessions is CLOSED: four rows decided, three\n"
    "values changed, one held. And a claim this document carried about\n"
    "`STREAMER_BELT_RADII` turned out to be wrong and is corrected below\n"
    "-- it had travelled here from a session reading rather than from a\n"
    "source.\n"
)

# ------------------------------------------------------------------
# 2 -- the streamer belt correction
# ------------------------------------------------------------------

STREAMER_OLD = (
    "The pilot also found two things worth acting on that no reading had\n"
    "caught. `ALFVEN_SURFACE_RADII` measures from the photosphere while its\n"
    "sibling `PARKER_CLOSEST_RADII` measures from Sun centre -- two constants\n"
    "in one file, same spacecraft, one solar radius apart, which is a\n"
    "rendering defect rather than a documentation one if that shell draws\n"
    "from centre (L-209). And `STREAMER_BELT_RADII` cites a paper\n"
    "inverted: the cited 6 R_sun is that paper's FLOOR, and its actual\n"
    "result is a lower bound three times larger (L-210).\n"
)

STREAMER_NEW = (
    "The pilot also found two things worth acting on that no reading had\n"
    "caught. `ALFVEN_SURFACE_RADII` measures from the photosphere while its\n"
    "sibling `PARKER_CLOSEST_RADII` measures from Sun centre -- two constants\n"
    "in one file, same spacecraft, one solar radius apart, which is a\n"
    "rendering defect rather than a documentation one if that shell draws\n"
    "from centre (L-209). And `STREAMER_BELT_RADII` carried a citation that\n"
    "did not support the claim attached to it (L-210).\n"
    "\n"
    "**That second sentence used to say something sharper and it was\n"
    "wrong.** Until August 20 this file reported that the row cited its\n"
    "paper INVERTED -- that the cited 6 R_sun was the paper's floor being\n"
    "used as a ceiling. That was a session reading, written down here as\n"
    "though it were a finding. An independent source read on August 20\n"
    "found otherwise: DeForest, Howard & McComas (2014) uses 6 R_sun as\n"
    "the threshold at which inbound wave motion first became detectable,\n"
    "which is neither a floor nor a ceiling on streamer extent, and that\n"
    "paper's streamer-belt result is an Alfven surface at 17 R_sun or\n"
    "more -- a result that belongs to `ALFVEN_SURFACE_RADII`, not here.\n"
    "The companion citation did not carry the row either: Golub &\n"
    "Pasachoff bound coronal structure at roughly 5-10 R_sun and state no\n"
    "4-6 R_sun streamer range at all. So the 4-6 range in the code was\n"
    "sourced to nothing. The value held at 6.0 as a declared drawing\n"
    "choice, both citations were repaired, and the range was withdrawn\n"
    "with a note saying why.\n"
    "\n"
    "It is worth leaving that visible rather than quietly restating it.\n"
    "A wrong claim in a summary document outlives the conversation it\n"
    "came from, because the next reader has nothing else to check it\n"
    "against.\n"
)

# ------------------------------------------------------------------
# 3 -- the scale figure
# ------------------------------------------------------------------

SCALE_OLD = (
    "machinery of this step, not a step of their own. They exist because\n"
    "reconciling worksheets against the code by hand does not scale, and the\n"
    "scale is measured: 110 claims scored, eight of them clean.\n"
)

SCALE_NEW = (
    "machinery of this step, not a step of their own. They exist because\n"
    "reconciling worksheets against the code by hand does not scale, and the\n"
    "scale is measured: 107 claims scored, eight of them clean.\n"
)

# ------------------------------------------------------------------
# 4 -- the queue closing
# ------------------------------------------------------------------

STATUS_OLD = (
    "**Step one is in progress, the backlog is visible, and the loop has now\n"
    "run end to end.** Of 110\n"
    "verification claims, eight are clean, forty-eight need to go back to\n"
    "whoever filled them in, twenty need a conversation, thirty-four are\n"
    "noted without a route, and twenty-four are not reachable by the scanner\n"
    "at all. That is not a discouraging result -- it is the first time the\n"
    "number has been knowable. Before the checker existed, the same claims\n"
    "were unexamined and looked fine.\n"
)

STATUS_NEW = (
    "**Step one is in progress, the backlog is visible, and the loop has now\n"
    "run end to end.** Of 107\n"
    "verification claims, eight are clean, forty-eight need to go back to\n"
    "whoever filled them in, nineteen need a conversation, thirty-two are\n"
    "noted without a route, and twenty-two are not reachable by the scanner\n"
    "at all. That is not a discouraging result -- it is the first time the\n"
    "number has been knowable. Before the checker existed, the same claims\n"
    "were unexamined and looked fine.\n"
    "\n"
    "**And on August 20 the loop closed for the first time.** The four\n"
    "rows the pilot ranked as worth acting on had sat undecided for two\n"
    "sessions. All four are now decided, and the shape of the decisions is\n"
    "the useful part: `EARTH_EQUATORIAL_RADIUS_KM` moved to IERS\n"
    "precision because its source line credited a resolution that does\n"
    "not publish that many digits; `BENNU_RADIUS_KM` moved to the\n"
    "OSIRIS-REx figure, which supersedes the pre-encounter radar value the\n"
    "row carried; `HAUMEA_RADIUS_KM` moved to the 2017 occultation, the\n"
    "only direct measurement, with the competing solution named in the\n"
    "row; and `STREAMER_BELT_RADII` HELD, because the number was never\n"
    "the problem. Three of the four kept their value or changed it by\n"
    "less than a part in ten thousand. What changed was what the code\n"
    "claims about where its numbers came from.\n"
    "\n"
    "**Three of those four turned on material the request builder had\n"
    "been dropping** (L-214). The rows carried `# Note:` lines answering\n"
    "the exact question the responders spent a dispatch re-deriving, and\n"
    "the builder silently withheld them because the label was outside its\n"
    "vocabulary. So one of the pilot's most useful results is a\n"
    "measurement of its own instrument. L-214 is designed and unbuilt,\n"
    "and it is the next scheduled work.\n"
    "\n"
    "The values were confirmed against primary sources by an independent\n"
    "read rather than by asking a second model whether ours were right --\n"
    "a blind read can disagree, and a confirmation request mostly cannot.\n"
    "It disagreed twice.\n"
)

# ------------------------------------------------------------------
# 5 -- footer
# ------------------------------------------------------------------

FOOT_OLD = (
    "*Prepared August 16, 2026 with Anthropic's Claude Opus 5; figures\n"
    "updated August 18, dispatch result added August 19. Built on\n"
    "`9ffb9b403a7d62090b30a9acf9adbc6180a6baec` at\n"
    "https://github.com/tonylquintanilla/palomas_orrery, gallery at\n"
    "`ff18d3e6fa31f70a8f525df471e751d046cf14fa`.*\n"
)

FOOT_NEW = (
    "*Prepared August 16, 2026 with Anthropic's Claude Opus 5; figures\n"
    "updated August 18, dispatch result added August 19, reconciliation\n"
    "closed and the streamer-belt claim corrected August 20. Built on\n"
    "`79729c98fd6bec8703fcc3bbc0806e6ee5226770` at\n"
    "https://github.com/tonylquintanilla/palomas_orrery, gallery at\n"
    "`109162bbb8d291bce615d888557498a9342d4642`.*\n"
)

EDITS = [
    ('CURRENCY: header anchor and date', HEAD_OLD, HEAD_NEW),
    ('scale figure 110 -> 107', SCALE_OLD, SCALE_NEW),
    ('CORRECTION: the streamer belt claim', STREAMER_OLD, STREAMER_NEW),
    ('routing figures + the queue closing', STATUS_OLD, STATUS_NEW),
    ('CURRENCY: footer', FOOT_OLD, FOOT_NEW),
]


def fail(message):
    print('ABORT: %s' % message)
    print('Nothing was written.')
    sys.exit(1)


def main():
    if not os.path.isfile(TARGET):
        fail('%s not found. Run this from the repo root.' % TARGET)

    with open(TARGET, 'rb') as handle:
        raw = handle.read()
    ending = b'\r\n' if b'\r\n' in raw else b'\n'
    lf = raw.replace(b'\r\n', b'\n')

    actual = hashlib.md5(lf).hexdigest()
    if actual != FINGERPRINT_LF:
        fail('%s does not match the base at %s (compared in LF form).\n'
             '  expected md5 %s\n  actual   md5 %s'
             % (TARGET, BASE_SHA[:8], FINGERPRINT_LF, actual))
    print('[base ok] %s  md5 %s  (%s on disk)'
          % (TARGET, actual, 'CRLF' if ending == b'\r\n' else 'LF'))

    try:
        text = lf.decode('ascii')
    except UnicodeDecodeError as exc:
        fail('%s carries non-ASCII at offset %d.' % (TARGET, exc.start))
    print('[ascii ok] %s' % TARGET)

    for label, old, new in EDITS:
        count = text.count(old)
        if count != 1:
            fail('anchor for "%s" matched %d times, expected exactly 1.'
                 % (label, count))
        text = text.replace(old, new, 1)
        print('[anchor ok] %s' % label)

    # The stale anchors must be GONE. Both old SHAs appear twice each --
    # header and footer -- so a partial re-stamp is the failure to catch,
    # and it is exactly the drift L-220 exists for.
    for stale in ('9ffb9b40', 'ff18d3e6'):
        if stale in text:
            fail('a stale anchor survived: %r still appears. The header and '
                 'the footer both carry it and both must move.' % stale)
    for fresh in (BASE_SHA, GALLERY_SHA):
        if text.count(fresh) != 2:
            fail('%s appears %d time(s); expected 2 (header and footer).'
                 % (fresh[:8], text.count(fresh)))
    print('[anchors] both stale SHAs gone; both new SHAs present twice')

    if "that paper's FLOOR" in text:
        fail('the corrected claim is still present in its old form.')
    print('[correction] the inverted-citation claim is retired')

    out = text.encode('ascii')
    if ending == b'\r\n':
        out = out.replace(b'\n', b'\r\n')
    with open(TARGET, 'wb') as handle:
        handle.write(out)
    print('[written] %s (%s preserved)'
          % (TARGET, 'CRLF' if ending == b'\r\n' else 'LF'))

    print('')
    print('CURRENCY STAMPS UPDATED (Stamp What You Change):')
    print('  header  -- August 20, orrery %s, gallery %s'
          % (BASE_SHA[:8], GALLERY_SHA[:8]))
    print('  footer  -- same pair, plus what this revision changed')
    print('')
    print('ONE CORRECTION, not just an update: the streamer-belt')
    print('inverted-citation claim was wrong and is retired in place,')
    print('with the reason left visible rather than quietly restated.')
    print('')
    print('NEXT:')
    print('  1. Re-run the maintenance runner')
    print('  2. Move this script to documentation/')


if __name__ == '__main__':
    main()
