"""patch_L209_1_pilot_findings.py -- three items from the pilot run.

RUN COMMAND
-----------
Save this file into the palomas_orrery repo root, open it in VS Code,
and click Run. It takes no arguments.

    python patch_L209_1_pilot_findings.py

Then run, and it is NOT optional:

    python ledger_index.py

That is what rebuilds the index table so the three new items appear in
it with their RICE scores. Skipping it leaves the table silently three
items short.

Success: one `ok` line, then `patch applied`.
Failure: a single `ERROR:` or `ANCHOR FAIL:` line, and nothing is
written.

WHAT IT DOES
------------
Adds three OPEN items to section A, from the 2026-08-18 pilot run.
Tony's ruling, 2026-08-19: three items, split by KIND of problem
rather than by row.

  L-209  ALFVEN_SURFACE_RADII origin mismatch. Alone, because it is a
         possible RENDERING error and everything else in the batch is
         documentation. RICE 3/3/85/1.
  L-210  Four citation findings from the pilot, together, because they
         are the same shape of work in the same file. RICE 3/3/80/2.
  L-211  Build UNKNOWN. The trigger in
         DESIGN_20260818_unknown_verdict.md pre-registered two rows;
         seven arrived. RICE 3/3/85/2.

Full evidence for all three: documentation/PILOT_CONVERGENCE_20260819.md.

WHAT IS PERMANENT AND WHAT IS NOT
---------------------------------
This script is disposable; the three ledger blocks are not.

Written August 2026 with Anthropic's Claude Opus 5. Built on
9ffb9b403a7d62090b30a9acf9adbc6180a6baec at
https://github.com/tonylquintanilla/palomas_orrery
"""

import hashlib
import os
import sys


BASE = {
    'LEDGER_CONSOLIDATED.md': '2fcfd9dd587c3dfd99138588a03266f5',
    'documentation/PILOT_CONVERGENCE_20260819.md':
        '8448dd198a805e709283a324b22aee92',
}

# The report was written and pushed before the worksheets were renamed
# to the shape L-206 had already ruled. It names all three legs, so its
# file list is now three citations to files that do not exist. Fixed in
# the same transaction as the ledger blocks that cite them, because a
# rename landing without its references is the failure the rename was
# meant to prevent.
REPORT = 'documentation/PILOT_CONVERGENCE_20260819.md'
REPORT_OLD = (
    "- `worksheet_gemini_constants_new_20260818.jsonl` (Gemini 3.1 "
    "Pro, fresh chat)\n"
    "- `worksheet_gpt_constants_new_20260818.jsonl` (GPT, fresh chat)\n"
    "- `worksheet_claude_constants_new_20260818.jsonl` (Claude, fresh "
    "chat, outside the project)\n")
REPORT_NEW = (
    "- `worksheet_gemini-3-1-pro_pilot_constants_new_20260818.jsonl`\n"
    "  (Gemini 3.1 Pro, fresh chat)\n"
    "- `worksheet_gpt-5-6-sol_pilot_constants_new_20260818.jsonl`\n"
    "  (GPT 5.6 Sol, fresh chat)\n"
    "- `worksheet_claude-opus-5_pilot_constants_new_20260818.jsonl`\n"
    "  (Claude Opus 5, fresh chat, outside the project)\n"
    "\n"
    "Renamed 2026-08-19 to the shape L-206 had already ruled --\n"
    "`worksheet_<model>_<batch>_<YYYYMMDD>` with the model field "
    "carrying\nthe version. The names first used omitted the version "
    "and were\nproposed without checking the ledger item that had "
    "settled it. The\nrename was free because no annotation cited "
    "them yet; it would not\nhave been free an hour after the first "
    "`# Cross-checked:` leg.\n")

# Inserted before the end of section A. Anchored on the tail of L-206,
# which is the last block in that section.
ANCHOR = ("**Ref:** L-200 (the leg that cites the filename); L-186; "
          "L-192.\n\n## PENDING ACTION (Tony-side)\n")

BLOCKS = """**Ref:** L-200 (the leg that cites the filename); L-186; L-192.

#### [L-209] ALFVEN_SURFACE_RADII -- origin mismatch, photosphere vs Sun centre
<!-- L:209 status:OPEN upd:2026-08-19 section:A flag: rice:3/3/85/1 -->
- **The finding, pilot run 2026-08-18.** `ALFVEN_SURFACE_RADII = 18.8`
  is an ALTITUDE above the photosphere, not a heliocentric radius.
  Both the Kasper et al. 2021 abstract (13 million km above the
  photosphere) and the NASA/APL release (8.127 million miles above the
  solar surface) measure from the surface.
- **Checkable inside the file, against a sibling.**
  `PARKER_CLOSEST_RADII = 9.86` IS heliocentric: the mission's 3.8
  million miles above the surface is 8.86 R_sun of altitude and 9.86
  from centre. So two constants in one file, describing the same
  spacecraft, use different origins and differ by exactly 1 R_sun.
- **Why this is alone rather than with the other pilot findings.** If
  the Alfven surface is drawn as a shell from Sun centre alongside
  HELIOPAUSE_RADII and PARKER_CLOSEST_RADII, the render is low by one
  solar radius and the value should be 19.8. That makes it a rendering
  defect, not a documentation defect, and it fails Mode 5 in a way no
  citation error does.
- **Confirm the dispatch before editing the leaf.** Whether the shell
  is drawn from centre is the question that decides whether this is a
  render bug or only a comment bug. Grep for consumers of the constant
  first.
- **Two further cautions from the same return, if it IS drawn as a
  sphere.** The crossing was into a low-Mach-number boundary layer
  above a pseudostreamer, not a global surface; later PSP work puts
  the Alfven surface at 10-20 R_sun, non-spherical, and expanding with
  rising solar activity.
- **Citation half.** GPT independently marked the citation PARTIAL:
  Kasper et al. 2021 does not itself print 18.8 R_sun. That figure is
  from the press release, so the row cites the paper for a number only
  the release states.
**Note:** RICE is Claude's proposal, unratified.
**Gap:** unverified whether the shell renders from Sun centre. That
check comes first and may close this as comment-only.
**Ref:** `documentation/PILOT_CONVERGENCE_20260819.md` Part 4;
`documentation/worksheets/`
`worksheet_claude-opus-5_pilot_constants_new_20260818.jsonl` R12;
L-206 (the filename convention these were renamed to obey);
L-207 (the run that produced it).

#### [L-210] Pilot citation findings -- four rows in constants_new.py
<!-- L:210 status:OPEN upd:2026-08-19 section:A flag: rice:3/3/80/2 -->
- **Grouped on purpose.** Four findings, same file, same shape of
  work: the value is defensible and the authority attached to it is
  not. One pass, one patch. The rendering defect from the same run is
  L-209 and is deliberately NOT here.
- **`STREAMER_BELT_RADII` -- inverted citation. Take this one first.**
  DeForest, Howard & McComas 2014 does not support "4-6 R_sun" for
  streamers. The paper's 6 R_sun is an INNER bound beyond which
  inbound wave motion was first detected; its streamer-belt result is
  a LOWER bound of 17 R_sun on the Alfven surface, 12.5 over the polar
  holes. A bounding figure was taken from the wrong end of the result,
  and the paper's point is that the structure extends further out, not
  that it stops there. The value 6.0 may survive as a drawing choice
  for the top of the closed helmet structure; the citation does not.
  Note it is the same paper cited on the Alfven row, where it belongs.
- **`EARTH_EQUATORIAL_RADIUS_KM` -- Shape A swap, with its own
  template one row below.** IAU 2015 B3 states 6378.1; the third
  decimal comes from IERS/WGS84, named in a `# Note:` but not on the
  Source line. All three legs flagged it, which is the prediction in
  `PILOT_EXPECTED_DISPOSITIONS_20260817.md` confirmed exactly. The fix
  is to make this row look like `EARTH_POLAR_RADIUS_KM` directly
  below, which already cites IERS and notes separately what B3 rounds
  to.
- **`BENNU_RADIUS_KM` -- superseded value AND a misattributed
  confirmation.** 0.246 is the pre-encounter Nolan radar figure;
  OSIRIS-REx gives 490.06 +/- 0.16 m mean diameter, so 0.245. Beyond
  the digit: the comment attributes "mean radius 246 +/- 10 m, V =
  0.062 km^3" to OSIRIS-REx OLA, and those are the radar numbers
  restated. OLA and SPC give 0.0615 and 0.061354 km^3 to about 0.1
  percent. The row reads as though the mission independently produced
  the figure it was confirming.
- **`HAUMEA_RADIUS_KM` -- trace, do not simply correct.** 715 km is
  the volume-equivalent radius of the Lockwood et al. 2014 model,
  reproduced to the digit, but that model was overturned by the 2017
  stellar occultation -- the only direct size measurement -- which
  puts the mean radius near 798 km. Separately, the axes in the
  comment (1050 x 840 x 537 km) match NO published shape model:
  Lockwood gives 960 x 770 x 495, Ortiz gives 1161 x 852 x 513. Yet
  the comment's geometric mean of 779.5 computes correctly FROM those
  axes. Somebody did valid arithmetic on unsourced numbers, which
  leaves no arithmetic trace and would be equally invisible elsewhere
  in the corpus. Find where the axes came from before editing.
- **`ARROKOTH_RADIUS_KM` -- watch flag, not another one-time fix.**
  A newer New Horizons shape model gives ~9.95 km against 9.1, a 9
  percent change moving OPPOSITE to the 2026-04-15 correction the
  comment already records. This row has now been wrong in both
  directions. Attribution also drifts: the figure 3166 km^3 and the
  phrase about a 9.1 km equivalent sphere appear verbatim in Amarante
  & Winter 2022 working from Spencer et al. 2020, not in the cited
  Keane et al. 2022.
**Note:** RICE is Claude's proposal, unratified.
**Gap:** every item above is a RESPONDER's claim, not a verdict. Each
needs Tony's judgment per row before any patch is written.
**Ref:** `documentation/PILOT_CONVERGENCE_20260819.md` Parts 3-4;
L-195 (Shape A swaps); L-209 (the rendering half of the same run).

#### [L-211] UNKNOWN -- the verdict for "checked, could not determine"
<!-- L:211 status:OPEN upd:2026-08-19 section:A flag: rice:3/3/85/2 -->
- **The trigger fired, and it was pre-registered.**
  `documentation/DESIGN_20260818_unknown_verdict.md` set the threshold
  at two returned rows where a responder reached for `unverified`
  beside a note describing a search actually attempted and failed.
  Seven arrived on the first run: Gemini 1, GPT 3, Claude 3. Build it.
- **The design is settled; only the build is open.** Four rulings from
  the design note, not to be re-litigated: it routes CONVERSATION and
  never SEND BACK, since sending it back asks the same responder to
  repeat a search that already failed; it REQUIRES a non-empty note,
  and an UNKNOWN with an empty note routes SEND BACK as incomplete,
  which is a presence check rather than prose-reading and inverts the
  incentive so UNKNOWN costs more than a real answer; it earns no
  rung; and two or more INDEPENDENT UNKNOWNs on one key stop being
  about the responders and become a removal candidate under the
  Fetched-vs-Recalled third branch.
- **What the run added that the design did not have.** Claude's leg
  states the gap in the vocabulary's own terms -- `unverified` reads
  as NO ANSWER GIVEN when what happened was AN ANSWER ATTEMPTED AND
  NOT REACHED -- and then supplies the pattern: all three of its cases
  are PRINT BOOKS. Carroll & Ostlie, Golub & Pasachoff, Murray &
  Dermott. GPT hit two of the same three. The missing verdict is not
  scattered; it concentrates wherever the authority is a book no
  responder can open.
- **Which reframes the follow-on, and this is the larger finding.**
  Three constants in this slice rest on print authorities that no
  model-mediated check can ever reach. Those rows need a human with
  library access, not a better token. UNKNOWN makes the condition
  VISIBLE and countable; it does not resolve it.
- **Counting UNKNOWNs per key is cheap** because L-207 already groups
  responder legs under one key in `citation_prompt_rows`. Extending
  that count is the "extend a boundary before adding a path" shape.
**Note:** RICE is Claude's proposal, unratified.
**Gap:** unbuilt. The vocabulary lives in `VERDICT_TOKENS`, so the
request builder and the citation prompt both pick it up for free once
the token exists.
**Ref:** `documentation/DESIGN_20260818_unknown_verdict.md`;
`documentation/PILOT_CONVERGENCE_20260819.md` Part 5; L-207.

## PENDING ACTION (Tony-side)
"""


def fingerprint(data):
    return hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()


def fail(message):
    print('ERROR: %s' % message)
    print('Nothing was written.')
    return 1


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    os.chdir(here)

    name = 'LEDGER_CONSOLIDATED.md'
    if not os.path.isfile(name):
        return fail('%s not found. Save this script in the repo root '
                    'and run it there.' % name)
    with open(name, 'rb') as handle:
        data = handle.read()
    found = fingerprint(data)
    if found != BASE[name]:
        return fail('%s has moved since this patch was built (expected '
                    '%s, found %s).' % (name, BASE[name], found))

    # Handles must be free. A reused handle is worse than a missing
    # one: two blocks answer to the same name and the index picks one.
    text = data.decode('utf-8')
    for handle_no in (209, 210, 211):
        if 'L:%d ' % handle_no in text or '[L-%d]' % handle_no in text:
            return fail('L-%d is already in use.' % handle_no)

    try:
        BLOCKS.encode('ascii')
    except UnicodeEncodeError as exc:
        return fail('this patch would insert non-ASCII text: %s' % exc)

    if not os.path.isfile(REPORT):
        return fail('%s not found.' % REPORT)
    with open(REPORT, 'rb') as handle:
        report = handle.read()
    if fingerprint(report) != BASE[REPORT]:
        return fail('%s has moved since this patch was built.' % REPORT)

    crlf = data.count(b'\r\n') > 0
    old = ANCHOR.encode('ascii')
    new = BLOCKS.encode('ascii')
    if crlf:
        old = old.replace(b'\n', b'\r\n')
        new = new.replace(b'\n', b'\r\n')
    count = data.count(old)
    if count != 1:
        print('ANCHOR FAIL: expected 1 match, found %d' % count)
        print('Nothing was written.')
        return 1
    data = data.replace(old, new)

    rcrlf = report.count(b'\r\n') > 0
    rold = REPORT_OLD.encode('ascii')
    rnew = REPORT_NEW.encode('ascii')
    if rcrlf:
        rold = rold.replace(b'\n', b'\r\n')
        rnew = rnew.replace(b'\n', b'\r\n')
    if report.count(rold) != 1:
        print('ANCHOR FAIL: %s -- expected 1 match for the leg list, '
              'found %d' % (REPORT, report.count(rold)))
        print('Nothing was written.')
        return 1
    report = report.replace(rold, rnew)

    with open(name, 'wb') as handle:
        handle.write(data)
    print('  ok  %s (%d bytes, 3 blocks added)' % (name, len(data)))
    with open(REPORT, 'wb') as handle:
        handle.write(report)
    print('  ok  %s (%d bytes, leg list renamed)' % (REPORT, len(report)))
    print('patch applied')
    print('')
    print('NOW RUN, and it is not optional:')
    print('  python ledger_index.py')
    return 0


if __name__ == '__main__':
    sys.exit(main())
