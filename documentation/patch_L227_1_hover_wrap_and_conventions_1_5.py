"""patch_L227_1_hover_wrap_and_conventions_1_5.py

Built on 15741822cb8f54ac26fc252aa8382cd90534570d at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Gallery at 8ec4f261013f09697d649efd25c8a746bffeff64.
Both confirmed by live git ls-remote.
Written August 23, 2026 with Anthropic's Claude Opus 5.

RUN IT LIKE THIS
    Save into the REPO ROOT -- the folder holding
    solar_visualization_shells.py, LEDGER_CONSOLIDATED.md, skills/ and
    ledger_index.py. Open in VS Code, click Run.
    Equivalent command: python patch_L227_1_hover_wrap_and_conventions_1_5.py

Transactional, all-or-nothing, binary I/O, three targets. Nothing is
written to ANY file unless every anchor in ALL THREE matches once.

  solar_visualization_shells.py               band_hover re-flowed
  skills/orrery-coding-conventions/SKILL.md   1.4 -> 1.5
  LEDGER_CONSOLIDATED.md                      L-227 and L-228 opened

WHAT IT FIXES -- found by Mode 5 on 2026-08-23

Tony hovered the streamer band and the tooltip ran off the screen.

`band_hover` (built live in `create_sun_streamer_band_shell`) carried
`<br><br>` between PARAGRAPHS and no break at all inside them. Measured
as rendered: EIGHT segments, the longest **378 characters**, six of them
over 98. `streamer_belt_info`, forty lines up in the same file, tops out
at 98 because every one of its source lines ends with `<br>`.

The cause is worth naming because it will recur. `band_hover` was
written as implicitly-concatenated string literals wrapped at ~72 chars
FOR SOURCE READABILITY. In the older strings the source wrap and the
rendered wrap are the same act, because each line carries its own
`<br>`. L-224 copied the visual habit and not the mechanism, so the
source looked correctly wrapped and the output was one 378-character
line. Nothing catches this except a human hovering it.

  After: 29 segments, longest 63 characters, none over 98.

**NO WORDING CHANGES.** Verified mechanically before this patch was
written: strip every `<br>` from the old and new text, collapse runs of
whitespace, compare. Byte-identical. The self-check below re-runs that
comparison at patch time so it cannot rot -- if a word moved, the patch
refuses.

WHAT IT ADDS TO THE SKILL -- orrery-coding-conventions 1.4 -> 1.5

  "Hover Line Width Is a Convention, Not an Accident."
  Sits next to Canonical Text Format, which governs `\\n` vs `<br>` and
  says nothing about WIDTH. Tony's ruling, 2026-08-23: this recurs from
  time to time rather than constantly, which is exactly the kind of
  thing a person forgets and a written convention does not.

WHAT IT OPENS IN THE LEDGER

  L-227 -- this defect and the convention it produced.
  L-228 -- the Alfven latitude ranges, Tony-side (do).

     Three different Alfven ranges are hardcoded across hover strings in
     this one module: `~15-20 R_sun` in the outer corona hover,
     `~10-20 solar radii` in alfven_surface_info, and `Polar coronal
     holes: ~12-15 | Streamer belt: ~17-19` in both Alfven strings. The
     drawn radius is fine -- it interpolates ALFVEN_SURFACE_RADII and
     always has. These are PROSE ranges with a bare `# Source:` line.

     Tony's rule, restated 2026-08-23: a range may be NOTED where it has
     a citation; the VISUALIZATION uses the interpolated constant; where
     the citation is insufficient the values are OMITTED. So this is a
     citation hunt with a decided disposition, not an open question.
     Flagged partly because `~17-19` sits close to the 17 R_sun that was
     corrected at source the day before, and DeForest's own figures are
     12 polar and 15 streamer-belt as INSTRUMENTAL FLOORS.

WHAT IS PERMANENT AND WHAT IS NOT
  The script is disposable. The re-flowed hover, skill v1.5, and the two
  ledger items are not.

AFTER RUNNING, IN THIS ORDER
  1. python ledger_index.py
  2. python skills_index.py
     The manifest still advertises orrery-coding-conventions 1.4 until
     this runs, and Stale Skill = Stop compares against the manifest.
  3. Settings > Skills: reinstall orrery-coding-conventions (now 1.5).
  4. Run the maintenance suite; expect 11 of 11.
  5. Commit and push.
  6. Move this script to documentation/.

  MODE 5: hover the streamer band once more. The text should now wrap
  inside the viewport. That is the only gate that catches this class of
  defect, and it is Tony's.

CARRIED OBLIGATION FOR THE HANDOFF
  orrery-coding-conventions goes to 1.5. A mid-session reinstall cannot
  be verified from inside the session that makes it, so the NEXT session
  confirms its loaded copy reads 1.5 before orrery visual work. This
  session loaded 1.4, correct at the time. safe-file-editing 1.8 carries
  the same obligation from earlier today.
"""

import hashlib
import os
import re
import sys

BASE_SHA = '15741822cb8f54ac26fc252aa8382cd90534570d'
GALLERY_SHA = '8ec4f261013f09697d649efd25c8a746bffeff64'
MODEL = "Anthropic's Claude Opus 5"

HERE = os.path.dirname(os.path.abspath(__file__))

MODULE = 'solar_visualization_shells.py'
SKILL = os.path.join('skills', 'orrery-coding-conventions', 'SKILL.md')
LEDGER = 'LEDGER_CONSOLIDATED.md'

FINGERPRINTS = {
    MODULE: 'bd76b46fc0a6b0fa03995688e87365ac',
    SKILL: 'd4d8b32836e5119d59e3eab7da836cdd',
    LEDGER: '1dc7a5d5ae5d162ca721f7e562f47c1b',
}


# ==================================================================
# EDIT 1 -- re-flow band_hover. Breaks only; no word changes.
# ==================================================================

OLD_1 = '''    band_hover = (
        "One object with two regimes, not a shell with a radius.<br><br>"

        "CLOSED HELMET -- the dense, wide base. Magnetic arcades stand "
        "over the neutral line, closed at both ends. They reach no "
        f"higher than 2-4 R_sun, and the band pinches at {cusp_rs:.1f} "
        f"R_sun ({cusp_km:,.0f} km, {cusp_au:.6f} AU) where they open.<br>"
        "Source: Suess & Nerney (2004), Adv. Space Res. 33:668-675 -- "
        "stated there as established background, not measured by it, so "
        "the pinch is drawn soft rather than sharp.<br><br>"

        "OPEN STALK -- above the pinch. A thin sheet along the current "
        "sheet. It has NO outer edge: it thins into the slow solar wind, "
        "so this drawing dissolves instead of stopping. Nothing is drawn "
        f"past the Alfven surface at {fade_rs:.1f} R_sun ({fade_km:,.0f} "
        f"km, {fade_au:.6f} AU), where the corona becomes wind. Beyond "
        "that the sheet continues as the heliospheric current sheet, out "
        "to the heliopause.<br><br>"

        "THE VISIBLE EDGE. That a sharp brightness boundary exists is a "
        "coronagraph observation. What it DIVIDES is an interpretation: "
        "Suess & Nerney take it as reasonable to assume it separates "
        "fast coronal-hole wind from slow wind. Slow-wind origin is not "
        "settled, so the edge is drawn and its meaning is attributed.<br><br>"

        "DeForest, Howard & McComas (2014), ApJ 787:124 followed inbound "
        f"wave motion out to 15 R_sun ({fov_km:,.0f} km, {fov_au:.6f} "
        "AU). That is the coronagraph's field of view, not an extent -- "
        "a floor, not an edge.<br><br>"

        "THE WARP is drawn in ONE configuration, near solar minimum. The "
        "neutral line's tilt sweeps toward the poles across the 11-year "
        "cycle; this is the shape, not a measurement of today's.<br><br>"

        "Drawn as a visualization assumption where no measured boundary "
        "exists (L-224)."
    )
'''

NEW_1 = '''    # Every line carries its own <br>: in this file the SOURCE wrap and
    # the RENDERED wrap are one act, and a line without a break renders
    # as part of a run that can reach hundreds of characters (L-227).
    band_hover = (
        "One object with two regimes, not a shell with a radius.<br><br>"

        "CLOSED HELMET -- the dense, wide base. Magnetic arcades stand<br>"
        "over the neutral line, closed at both ends. They reach no<br>"
        f"higher than 2-4 R_sun, and the band pinches at {cusp_rs:.1f} R_sun<br>"
        f"({cusp_km:,.0f} km, {cusp_au:.6f} AU) where they open.<br>"
        "Source: Suess & Nerney (2004), Adv. Space Res. 33:668-675 --<br>"
        "stated there as established background, not measured by it, so<br>"
        "the pinch is drawn soft rather than sharp.<br><br>"

        "OPEN STALK -- above the pinch. A thin sheet along the current<br>"
        "sheet. It has NO outer edge: it thins into the slow solar wind,<br>"
        "so this drawing dissolves instead of stopping. Nothing is drawn<br>"
        f"past the Alfven surface at {fade_rs:.1f} R_sun<br>"
        f"({fade_km:,.0f} km, {fade_au:.6f} AU), where the corona becomes<br>"
        "wind. Beyond that the sheet continues as the heliospheric<br>"
        "current sheet, out to the heliopause.<br><br>"

        "THE VISIBLE EDGE. That a sharp brightness boundary exists is a<br>"
        "coronagraph observation. What it DIVIDES is an interpretation:<br>"
        "Suess & Nerney take it as reasonable to assume it separates<br>"
        "fast coronal-hole wind from slow wind. Slow-wind origin is not<br>"
        "settled, so the edge is drawn and its meaning is attributed.<br><br>"

        "DeForest, Howard & McComas (2014), ApJ 787:124 followed inbound<br>"
        f"wave motion out to 15 R_sun ({fov_km:,.0f} km, {fov_au:.6f} AU).<br>"
        "That is the coronagraph's field of view, not an extent --<br>"
        "a floor, not an edge.<br><br>"

        "THE WARP is drawn in ONE configuration, near solar minimum. The<br>"
        "neutral line's tilt sweeps toward the poles across the 11-year<br>"
        "cycle; this is the shape, not a measurement of today's.<br><br>"

        "Drawn as a visualization assumption where no measured boundary<br>"
        "exists (L-224)."
    )
'''


# ==================================================================
# EDIT 2 -- skill version line
# ==================================================================

OLD_2 = (
    "Skill version: 1.4 | Cut from palomas_orrery @ 86f529a (v1.4), earlier @\n"
    "3398970 (v1.3) | 2026-08-16\n"
)
NEW_2 = (
    "Skill version: 1.5 | Cut from palomas_orrery @ 15741822 (v1.5),\n"
    "earlier @ 86f529a (v1.4), 3398970 (v1.3) | 2026-08-23\n"
)


# ==================================================================
# EDIT 3 -- skill adds-paragraph
# ==================================================================

OLD_3 = (
    "v1.4 adds Marker Separation for Near-Equal Radii to the Single Info\n"
    "Marker Pattern, earned when the chromosphere moved to true scale and its\n"
    "marker landed one pixel from the photosphere's; and Harvest the\n"
    "Conventions You Find, which is how this skill grows.\n"
)
NEW_3 = (
    "v1.4 adds Marker Separation for Near-Equal Radii to the Single Info\n"
    "Marker Pattern, earned when the chromosphere moved to true scale and its\n"
    "marker landed one pixel from the photosphere's; and Harvest the\n"
    "Conventions You Find, which is how this skill grows.\n"
    "v1.5 (L-227) adds Hover Line Width Is a Convention, Not an Accident,\n"
    "found by Mode 5 when a tooltip ran off the viewport: a hover string had\n"
    "been wrapped at 72 characters in the SOURCE with no `<br>` on the\n"
    "lines, and rendered as one 378-character run. Canonical Text Format\n"
    "already governed `\\n` versus `<br>` and said nothing about width.\n"
)


# ==================================================================
# EDIT 4 -- the new skill section
# ==================================================================

OLD_4 = (
    "One trap: for a body still on `<br>`, the `.replace('\\n', '<br>')` in a\n"
    "reference-pattern config is a NO-OP. It looks like it is working. It starts\n"
    "working only once the module strings carry `\\n`.\n"
    "\n"
    "## Layer Chain Gap Handling [PRACTICE]\n"
)
NEW_4 = (
    "One trap: for a body still on `<br>`, the `.replace('\\n', '<br>')` in a\n"
    "reference-pattern config is a NO-OP. It looks like it is working. It starts\n"
    "working only once the module strings carry `\\n`.\n"
    "\n"
    "## Hover Line Width Is a Convention, Not an Accident [QUALITY]\n"
    "\n"
    "Companion to the section above, which governs WHICH break character to\n"
    "use and says nothing about how often. This governs how often.\n"
    "\n"
    "**Every source line of a hover string carries its own break.** In this\n"
    "codebase the source wrap and the rendered wrap are ONE ACT, not two.\n"
    "The existing strings are built that way -- `streamer_belt_info`,\n"
    "`roche_limit_info`, `alfven_surface_info_hover` -- and their rendered\n"
    "lines land between about 60 and 98 characters because their source\n"
    "lines do.\n"
    "\n"
    "**The failure mode is that correct-looking source produces broken\n"
    "output.** Python's implicit string concatenation invites wrapping a\n"
    "long literal across several source lines for readability. Do that\n"
    "without a break on each line and the pieces concatenate into one run.\n"
    "The diff looks tidy, the file looks tidy, and the tooltip runs off the\n"
    "screen. Paragraph-level `<br><br>` does not save it: a paragraph is\n"
    "still a single line.\n"
    "\n"
    "```python\n"
    "# WRONG -- renders as one 378-character line\n"
    "\"OPEN STALK -- above the pinch. A thin sheet along the current \"\n"
    "\"sheet. It has NO outer edge: it thins into the slow solar wind, \"\n"
    "\n"
    "# RIGHT -- source wrap and rendered wrap are the same act\n"
    "\"OPEN STALK -- above the pinch. A thin sheet along the current<br>\"\n"
    "\"sheet. It has NO outer edge: it thins into the slow solar wind,<br>\"\n"
    "```\n"
    "\n"
    "Two details that follow from it. Put the break where the trailing\n"
    "space was rather than after it -- the break IS the separator, so a\n"
    "space before it renders as a stray one. And do not let a break fall\n"
    "between a number and its unit: `at {cusp_rs:.1f} R_sun<br>` reads,\n"
    "`at {cusp_rs:.1f}<br>R_sun` does not.\n"
    "\n"
    "**Checking it is one line, and worth running after any hover edit:**\n"
    "\n"
    "```python\n"
    "max(len(s) for s in rendered_hover.split('<br>'))   # want <= ~98\n"
    "```\n"
    "\n"
    "Re-flowing an existing string is a BREAKS-ONLY edit. Prove it rather\n"
    "than assert it: strip every `<br>`, collapse runs of whitespace, and\n"
    "compare old against new. They must be byte-identical. A re-flow that\n"
    "quietly reworded something is indistinguishable from one that did not,\n"
    "unless the comparison runs.\n"
    "\n"
    "(Origin, 2026-08-23, L-227. Tony hovered the streamer band during the\n"
    "Mode 5 pass on L-224 and the tooltip ran off the viewport. The string\n"
    "had been wrapped at 72 characters in the source with breaks only\n"
    "between paragraphs; `streamer_belt_info`, forty lines up in the same\n"
    "file, was correct. Nothing catches this but a person hovering it --\n"
    "no checker reads rendered hover width, and the module compiles and\n"
    "the trace builds either way. Tony's ruling, on adding it here: this\n"
    "recurs from time to time rather than constantly, which is precisely\n"
    "the kind of thing a person forgets and a written convention does not.)\n"
    "\n"
    "## Layer Chain Gap Handling [PRACTICE]\n"
)


# ==================================================================
# EDIT 5 -- L-227 and L-228
# ==================================================================

OLD_5 = (
    "\n"
    "## PENDING ACTION (Tony-side)\n"
)
NEW_5 = (
    "\n"
    "#### [L-227] Streamer band hover rendered as one 378-character line\n"
    "<!-- L:227 status:OPEN upd:2026-08-23 section:A flag: rice:2/2/95/1 -->\n"
    "- **Found by Mode 5 on 2026-08-23**, hovering the streamer band during\n"
    "  the L-224 acceptance pass. The tooltip ran off the viewport.\n"
    "- **Measured as rendered:** `band_hover` had EIGHT segments, longest\n"
    "  378 characters, six over 98. `streamer_belt_info`, forty lines up in\n"
    "  the same file, tops out at 98. After the fix: 29 segments, longest\n"
    "  63, none over 98.\n"
    "- **Cause.** The string was written as implicitly-concatenated literals\n"
    "  wrapped at ~72 characters FOR SOURCE READABILITY, with `<br><br>`\n"
    "  only between paragraphs. In this file the source wrap and the\n"
    "  rendered wrap are one act, because each older line carries its own\n"
    "  `<br>`. L-224 copied the visual habit without the mechanism, so the\n"
    "  source looked correctly wrapped and the output was one long run.\n"
    "- **Nothing but a person catches this.** No checker reads rendered\n"
    "  hover width; the module compiles and the trace builds either way.\n"
    "  Third demonstration this month that the render is the gate.\n"
    "- **Breaks only, no wording changed** -- proven mechanically, not\n"
    "  asserted: strip every `<br>`, collapse whitespace, compare old to\n"
    "  new, byte-identical. The patch re-ran that comparison as a self-check\n"
    "  so it could refuse if a word had moved.\n"
    "- **Convention recorded:** `orrery-coding-conventions` 1.5, Hover Line\n"
    "  Width Is a Convention, Not an Accident. Tony's ruling: this recurs\n"
    "  from time to time rather than constantly, which is the kind of thing\n"
    "  a person forgets and a written convention does not.\n"
    "- **Note:** RICE 2/2/95/1 -> 3.8 is Claude's proposed score.\n"
    "  **Tony-action (decide):** confirm or redirect, then re-run\n"
    "  `ledger_index.py`.\n"
    "- **Tony-action (do):** run `skills_index.py`, reinstall\n"
    "  orrery-coding-conventions at Settings > Skills, and hover the band\n"
    "  once more to confirm it wraps.\n"
    "- **Ref:** `solar_visualization_shells.py::create_sun_streamer_band_"
    "shell`;\n"
    "  `skills/orrery-coding-conventions/SKILL.md` v1.5; L-224 (the build\n"
    "  that introduced it); L-191 (the `<br>`-in-tooltip sweep, separate).\n"
    "\n"
    "#### [L-228] Alfven surface latitude ranges: source them or omit them\n"
    "<!-- L:228 status:OPEN upd:2026-08-23 section:A flag:Tony "
    "rice:2/3/60/2 -->\n"
    "- **Surfaced 2026-08-23** while reading the hover strings for L-227.\n"
    "- **THE DRAWN VALUE IS NOT AT ISSUE.** `ALFVEN_SURFACE_RADII` is\n"
    "  interpolated into every hover that quotes it, including the derived\n"
    "  million-km figure, and carries a `# Source+:` leg saying so (L-209).\n"
    "  When it moved 18.8 -> 19.7 the hovers followed by construction. No\n"
    "  shadow constant. This item is about PROSE ranges only.\n"
    "- **Three different ranges are hardcoded across hover strings in one\n"
    "  module**, all for the same quantity: `~15-20 R_sun` in\n"
    "  `outer_corona_info_hover`; `~10-20 solar radii` in\n"
    "  `alfven_surface_info`; and `Polar coronal holes: ~12-15 R_sun |\n"
    "  Streamer belt: ~17-19 R_sun` in BOTH Alfven strings. The `# Source:`\n"
    "  above them reads Cranmer et al. (2007), with no position given.\n"
    "- **Why it is worth a look rather than a shrug.** `~17-19` sits close\n"
    "  to the 17 R_sun corrected at source on 2026-08-22, and DeForest,\n"
    "  Howard & McComas (2014) give 12 polar and 15 streamer-belt as\n"
    "  INSTRUMENTAL FLOORS -- a noise floor and a coronagraph field of view,\n"
    "  not a shape. A range that looks like a measured latitude variation\n"
    "  and is actually two instrument limits is the exact confusion the\n"
    "  citation-KIND rule was drafted for (design note 2026-08-22,\n"
    "  Section 2).\n"
    "- **Disposition is already decided; only the citation is open.**\n"
    "  Tony's rule, restated 2026-08-23: a range may be NOTED where it has\n"
    "  a citation, the VISUALIZATION uses the interpolated constant, and\n"
    "  where the citation is insufficient the values are OMITTED. So:\n"
    "  read Cranmer et al. (2007) for a locatable position stating the\n"
    "  latitude variation. If it carries it, cite it properly and keep the\n"
    "  range as prose. If it does not, remove all three ranges and note the\n"
    "  gap. Do not reconcile them against each other -- three unsourced\n"
    "  numbers agreeing is not evidence.\n"
    "- **Tony-action (do):** the source read. Claude cannot clear this by\n"
    "  reasoning about it, and guessing here is the failure this week was\n"
    "  spent on.\n"
    "- **Note:** RICE 2/3/60/2 -> 3.0 is Claude's proposed score.\n"
    "  Confidence is 60 because whether Cranmer carries the claim is\n"
    "  unknown until somebody reads it. **Tony-action (decide):** confirm\n"
    "  or redirect.\n"
    "- **Ref:** `solar_visualization_shells.py` (`outer_corona_info_hover`,\n"
    "  `alfven_surface_info`, `alfven_surface_info_hover`);\n"
    "  `constants_new.py::ALFVEN_SURFACE_RADII`; L-209 (the DeForest\n"
    "  correction and the interpolation leg); L-210;\n"
    "  `documentation/DESIGN_NOTE_20260822_braid_and_citation_kind.md`\n"
    "  Section 2 (value, source, KIND).\n"
    "\n"
    "## PENDING ACTION (Tony-side)\n"
)


# ==================================================================
# EDIT 6 -- ledger currency stamp
# ==================================================================

OLD_6 = (
    "Module updated: August 23, 2026 with Anthropic's Claude Opus 5 (L-226:\n"
    "safe-file-editing 1.7 -> 1.8), built on 6d12ecac.\n"
)
NEW_6 = (
    "Module updated: August 23, 2026 with Anthropic's Claude Opus 5 (L-226:\n"
    "safe-file-editing 1.7 -> 1.8), built on 6d12ecac.\n"
    "Module updated: August 23, 2026 with Anthropic's Claude Opus 5 (L-227\n"
    "hover wrap + orrery-coding-conventions 1.5; L-228 Alfven ranges),\n"
    "built on 15741822.\n"
)


EDITS = [
    (MODULE, '1 band_hover re-flowed (breaks only)', OLD_1, NEW_1),
    (SKILL, '2 skill version 1.4 -> 1.5', OLD_2, NEW_2),
    (SKILL, '3 skill adds-paragraph', OLD_3, NEW_3),
    (SKILL, '4 new section: Hover Line Width', OLD_4, NEW_4),
    (LEDGER, '5 L-227 and L-228 opened', OLD_5, NEW_5),
    (LEDGER, '6 ledger currency stamp', OLD_6, NEW_6),
]

TARGETS = [MODULE, SKILL, LEDGER]

SUBS = {'{cusp_rs:.1f}': '4.0', '{cusp_km:,.0f}': '2,782,800',
        '{cusp_au:.6f}': '0.018602', '{fade_rs:.1f}': '19.7',
        '{fade_km:,.0f}': '13,705,290', '{fade_au:.6f}': '0.091614',
        '{fov_km:,.0f}': '10,435,500', '{fov_au:.6f}': '0.069757'}


def fail(message):
    print('')
    print('ERROR: ' + message)
    print('Nothing was written. ALL files on disk are untouched.')
    sys.exit(1)


def render(block):
    """Concatenate the literals of a python string-concat block."""
    text = ''.join(re.findall(r'(?:f?)"((?:[^"\\]|\\.)*)"', block))
    for key, value in SUBS.items():
        text = text.replace(key, value)
    return text


def words_only(text):
    return re.sub(r'\s+', ' ', text.replace('<br>', ' ')).strip()


def main():
    print('patch_L227_1_hover_wrap_and_conventions_1_5.py')
    print('built on %s' % BASE_SHA)
    print('gallery  %s' % GALLERY_SHA)
    print('')

    paths, originals, endings = {}, {}, {}
    for name in TARGETS:
        path = os.path.join(HERE, name)
        if not os.path.exists(path):
            fail('%s not found relative to this script.\n'
                 '       This one goes in the REPO ROOT -- the folder with\n'
                 '       solar_visualization_shells.py, LEDGER_CONSOLIDATED.md\n'
                 '       and skills/.\n'
                 '       It looked in: %s' % (name, HERE))
        paths[name] = path
        with open(path, 'rb') as handle:
            originals[name] = handle.read()

    for name in TARGETS:
        normalized = originals[name].replace(b'\r\n', b'\n')
        got = hashlib.md5(normalized).hexdigest()
        if got != FINGERPRINTS[name]:
            fail('BASE MOVED. %s fingerprints %s; this patch was built '
                 'against %s. Re-pull at HEAD, or ask for a rebuilt patch.'
                 % (name, got, FINGERPRINTS[name]))
        endings[name] = b'\r\n' if b'\r\n' in originals[name] else b'\n'
        print('[base ok]       %-42s %s (%s)'
              % (name, got, 'CRLF' if endings[name] == b'\r\n' else 'LF'))

    # --- ASCII, both directions --------------------------------------
    for _name, label, old, new in EDITS:
        if sum(1 for ch in new if ord(ch) > 127) > \
                sum(1 for ch in old if ord(ch) > 127):
            fail('edit %s would INTRODUCE a non-ASCII character.' % label)
    with open(os.path.abspath(__file__), 'rb') as handle:
        own = handle.read()
    if any(byte > 127 for byte in own):
        fail('this script itself is not pure ASCII.')
    print('[ascii ok]      no edit introduces non-ASCII; script is ASCII '
          '(%d bytes)' % len(own))

    # --- THE SELF-CHECK THAT CAN FAIL --------------------------------
    # A re-flow that quietly reworded something is indistinguishable
    # from one that did not, unless this comparison runs. It runs.
    before_text, after_text = render(OLD_1), render(NEW_1)
    if words_only(before_text) != words_only(after_text):
        fail('THE RE-FLOW CHANGED WORDING. Strip the breaks and collapse '
             'whitespace and the two texts differ. This patch is only '
             'allowed to move line breaks.')
    before_segs = [s for s in before_text.split('<br>') if s]
    after_segs = [s for s in after_text.split('<br>') if s]
    before_max = max(len(s) for s in before_segs)
    after_max = max(len(s) for s in after_segs)
    if after_max > 98:
        fail('re-flowed hover still has a %d-character line; the file norm '
             'is <= 98.' % after_max)
    if before_max <= 98:
        fail('the ORIGINAL hover is already within 98 characters (%d). '
             'Either the file moved or this patch is aimed at the wrong '
             'string -- refusing to "fix" something that is not broken.'
             % before_max)
    print('[wording ok]    breaks only -- identical after stripping <br> '
          'and collapsing space')
    print('[width ok]      %d segments/longest %d  ->  %d segments/longest %d'
          % (len(before_segs), before_max, len(after_segs), after_max))

    working = {n: originals[n].replace(b'\r\n', b'\n').decode('utf-8')
               for n in TARGETS}

    for handle_id in ('227', '228'):
        if '<!-- L:%s ' % handle_id in working[LEDGER]:
            fail('L-%s already has an index comment. This patch would '
                 'create a duplicate handle.' % handle_id)
    print('[handle ok]     L-227 and L-228 are absent, as expected')

    for name, label, old, new in EDITS:
        count = working[name].count(old)
        if count != 1:
            fail('ANCHOR FAIL on edit %s -- expected exactly 1 match, found '
                 '%d. First 70 chars: %r' % (label, count, old[:70]))
        working[name] = working[name].replace(old, new, 1)
        print('[ok]            %s' % label)

    for name in TARGETS:
        allowed = set()
        for n, _label, old, new in EDITS:
            if n != name:
                continue
            allowed.update(l for l in
                           (set(old.split('\n')) - set(new.split('\n'))) if l)
        after = set(working[name].split('\n'))
        before = originals[name].replace(b'\r\n', b'\n').decode('utf-8')
        lost = [l for l in before.split('\n') if l and l not in after]
        unexpected = [l for l in lost if l not in allowed]
        if unexpected:
            fail('%d line(s) of %s would be lost that no edit claims to '
                 'rewrite. First: %r'
                 % (len(unexpected), name, unexpected[0]))
        print('[addition ok]   %-42s %d line(s) rewritten'
              % (name, len(lost)))

    if 'Skill version: 1.5' not in working[SKILL]:
        fail('the skill version did not land as 1.5.')
    if 'Skill version: 1.4' in working[SKILL]:
        fail('a 1.4 version line survives in the skill.')
    print('[version ok]    SKILL.md declares 1.5, no 1.4 line survives')

    import ast
    try:
        ast.parse(working[MODULE], filename=MODULE)
    except SyntaxError as exc:
        fail('the patched %s would not parse: %s' % (MODULE, exc))
    print('[syntax ok]     %s parses' % MODULE)

    for name in TARGETS:
        out = working[name].encode('ascii')
        if endings[name] == b'\r\n':
            out = out.replace(b'\n', b'\r\n')
        with open(paths[name], 'wb') as handle:
            handle.write(out)
        print('[written]       %-42s %d -> %d bytes'
              % (name, len(originals[name]), len(out)))

    print('')
    print('patch applied -- %d edits across %d files'
          % (len(EDITS), len(TARGETS)))
    print('')
    print('NEXT, IN THIS ORDER:')
    print('  1. python ledger_index.py')
    print('  2. python skills_index.py     (manifest still says 1.4)')
    print('  3. Settings > Skills: reinstall orrery-coding-conventions (1.5)')
    print('  4. Maintenance suite; expect 11 of 11.')
    print('  5. Commit and push.')
    print('  6. Move this script to documentation/.')
    print('')
    print('MODE 5 -- the only gate that catches this class of defect:')
    print('  hover the streamer band again. The text should wrap inside')
    print('  the viewport now. Nothing automated reads rendered hover')
    print('  width, which is why it survived the L-224 build.')
    print('')
    print('CARRIED OBLIGATION for the handoff:')
    print('  orrery-coding-conventions goes to 1.5 at this SHA; this')
    print('  session loaded 1.4. The next session confirms its loaded copy')
    print('  reads 1.5 before orrery visual work. safe-file-editing 1.8')
    print('  carries the same obligation from earlier today.')
    print('')
    print('OPEN FOR TONY:')
    print("  - L-227 proposed RICE 2/2/95/1 (3.8); L-228 proposed 2/3/60/2")
    print("    (3.0). Both are Claude's. Confirm or redirect, re-run the index.")
    print('  - L-228 needs a source read of Cranmer et al. (2007). Claude')
    print('    cannot clear it by reasoning about it.')


if __name__ == '__main__':
    main()
