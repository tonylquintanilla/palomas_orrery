#!/usr/bin/env python3
"""
patch_L411_2_voyager2_20261018.py -- a follow-up to the Sun's numbers
(L-411), on Tony's look of 2026-10-18: Voyager 2's termination-shock
crossing is read from Li, Wang and Richardson (2008), "about 83.6 AU",
the same paper and crossing as the wind speeds beside it; the
chromosphere's two citations, which ran together, are separated; the
chromosphere's typed name is recorded on the ledger.

Built on orrery f80a3ad0d5fe0814693b32d365f7c337d3034587 at
https://github.com/tonylquintanilla/palomas_orrery ("v3.103"). The
website has its own small patch, patch_L411_3_voyager2_words_20261018.py,
run after this one is pushed (gallery 0be187ec at
https://github.com/tonylquintanilla/tonyquintanilla.github.io).
Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\
gallery C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\
Written October 18, 2026 with Anthropic's Claude Opus 5.5.

RUN COMMAND

    python patch_L411_2_voyager2_20261018.py

    Saved in the ORRERY folder above. Open it in VS Code and click Run.
    It takes no arguments and asks no questions.

WHAT IT DOES, all or nothing. The two code files must match f80a3ad
exactly; the ledger is edited only at the lines it changes:

    constants_new.py               VOYAGER2_TERMINATION_SHOCK_AU 84 -> 83.6,
                                   from Li et al.; the chromosphere's
                                   Source gains its missing semicolon
    solar_visualization_shells.py  "and Voyager 2 at about 83.6 AU
                                   (Li et al. 2008)", in both hovers
    LEDGER_CONSOLIDATED.md         L-411 note; header stamp

WHAT IT PRINTS

    Success: one "ok" line per check and edit, then "patch applied".
    Failure: one ERROR or ANCHOR FAIL line and "NOTHING was written."

Undo is Discard Changes in GitHub Desktop.
"""

import hashlib
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SHA = 'f80a3ad0'
MARKERS = {}
FINGERPRINTS = {'constants_new.py': 'bb8e01e18a1e5d2177137e976086a38a', 'solar_visualization_shells.py': '306cffd0f5097789988a313a0696f6e2'}
RESULTS = {'constants_new.py': '5f29ae0a4c369a680342770151fd2782', 'solar_visualization_shells.py': '4eaede7f843c897ffee639005455b26f'}
NEXT = ['  1. Run orrery_maintenance_run.py (dashboard). Expect 31 of 31', '     gating checkers passed and the gate line 0 TIER-1. It rewrites', '     the ledger index and the constants export.', '  2. Move this script into documentation/; commit; push.', '  3. Then the website: patch_L411_3_voyager2_words_20261018.py.']
NEW_FILES = {}
EDITS = [
    ('constants_new.py', 'Voyager 2 crossing from Li et al. (2008)', 'VOYAGER2_TERMINATION_SHOCK_AU = 84\n# Unit: au\n# Status: measured V_SOURCED 2026-10-17 -- open page\n# Figures: 2 -- the source prints 84.\n# Read: NASA SVS 20132, 2026-10-17, Claude Opus 5.5.\n# Source: NASA Scientific Visualization Studio, "Voyager 2 Proves Solar\n# Source+: System is Squashed" (23 January 2008) -- Voyager 1 encountered\n# Source+: the termination shock at 94 AU and Voyager 2 encountered it at\n# Source+: only 84 AU. https://svs.gsfc.nasa.gov/20132\n# Also: Li, Wang and Richardson (2008), "Properties of the termination\n# Also+: shock observed by Voyager 2", GRL 35:L19107 -- about 83.6 AU, on\n# Also+: August 30, 2007.\n# Note: the hovers typed 84 with no row, and their comments credited it\n# Note+: to Stone et al. (2005), which is Voyager 1\'s crossing only (L-411).\n', 'VOYAGER2_TERMINATION_SHOCK_AU = 83.6\n# Unit: au\n# Status: measured V_SOURCED 2026-10-18 -- open page\n# Figures: 3 -- the source prints "about 83.6 AU".\n# Read: Li, Wang and Richardson (2008), the abstract and secs. 1 and 3,\n# Read+: 2026-10-18, Claude Opus 5.5.\n# Source: Li, H., Wang, C. and Richardson, J. D. (2008), "Properties of\n# Source+: the termination shock observed by Voyager 2", GRL 35:L19107 --\n# Source+: abstract: in August 2007, Voyager 2 reached the termination\n# Source+: shock and entered the heliosheath at a distance of about 83.6 AU.\n# Source+: https://www.spaceweather.ac.cn/~hli/papers/Li%20et%20al%202008%20GRL%20Properties%20of%20the%20termination%20shock%20observed%20by%20Voyager%202.pdf\n# Also: NASA Scientific Visualization Studio, "Voyager 2 Proves Solar\n# Also+: System is Squashed" (23 January 2008) -- 84 AU, whole AU.\n# Also+: https://svs.gsfc.nasa.gov/20132. Stone et al. (2008), "An\n# Also+: asymmetric solar wind termination shock", Nature 454:71, abstract\n# Also+: -- 83.7 au; the paper is not open. The shock moved, and Voyager 2\n# Also+: crossed it more than once.\n# Corrected: 2026-10-18 (L-411) -- was 84 from NASA SVS 20132, two\n# Corrected+: figures. Li et al. is the same paper and crossing as\n# Corrected+: VOYAGER2_TS_UPSTREAM_SPEED_KM_S and its downstream row\n# Corrected+: (Tony, 2026-10-18).\n# Note: the hovers typed 84 with no row, and their comments credited it\n# Note+: to Stone et al. (2005), which is Voyager 1\'s crossing only (L-411).\n', 1),
    ('constants_new.py', 'chromosphere: its two citations separated', '# Source+: https://solar.physics.montana.edu/YPOP/Spotlight/SunInfo/Chromosph.html\n# Source+: Hathaway, D. H., "NASA/Marshall Solar Physics", the chromosphere page -- the\n', '# Source+: https://solar.physics.montana.edu/YPOP/Spotlight/SunInfo/Chromosph.html;\n# Source+: Hathaway, D. H., "NASA/Marshall Solar Physics", the chromosphere page -- the\n', 1),
    ('constants_new.py', 'credit line', 'CORE_AU, RADIATIVE_ZONE_AU, SOLAR_RADIUS_AU and PARKER_CLOSEST_RADII\nare conversions of their rows.)\n"""\n', 'CORE_AU, RADIATIVE_ZONE_AU, SOLAR_RADIUS_AU and PARKER_CLOSEST_RADII\nare conversions of their rows.)\nModule updated: October 18, 2026 with Anthropic\'s Claude Opus 5.5\n(L-411 follow-up: Voyager 2\'s termination-shock crossing is read from\nLi, Wang and Richardson (2008), the paper its wind speeds come from, on\nTony\'s word; the chromosphere\'s two citations are separated.)\n"""\n', 1),
    ('solar_visualization_shells.py', 'Voyager 2 line, both hovers', 'and Voyager 2 at {row_text(\'VOYAGER2_TERMINATION_SHOCK_AU\')} AU (NASA).<br>"\n', 'and Voyager 2 at about {row_text(\'VOYAGER2_TERMINATION_SHOCK_AU\')} AU (Li et al. 2008).<br>"\n', 2),
    ('solar_visualization_shells.py', 'credit line', "Domain: orrery\n\nModule updated: October 17, 2026 with Anthropic's Claude Opus 5.5\n", "Domain: orrery\n\nModule updated: October 18, 2026 with Anthropic's Claude Opus 5.5\n(L-411 follow-up: the termination shock's Voyager 2 line cites Li et\nal. 2008, the paper its wind speeds come from. Tony's word.)\nModule updated: October 17, 2026 with Anthropic's Claude Opus 5.5\n", 1),
    ('LEDGER_CONSOLIDATED.md', 'header stamp', 'kelvin), built on 6f4fc9b0 and gallery da442bf2.\nReview and RICE update Tony 6-21-2026\n', "kelvin), built on 6f4fc9b0 and gallery da442bf2.\nModule updated: October 18, 2026 with Anthropic's Claude Opus 5.5\n(L-411 follow-up on Tony's look: Voyager 2's crossing from Li et al.;\nthe chromosphere's citations separated; its typed name recorded),\nbuilt on f80a3ad0 and gallery 0be187ec.\nReview and RICE update Tony 6-21-2026\n", 1),
    ('LEDGER_CONSOLIDATED.md', 'L-411 meta', '<!-- L:411 status:OPEN upd:2026-10-17 section:A flag: rice: -->', '<!-- L:411 status:OPEN upd:2026-10-18 section:A flag: rice: -->', 1),
    ('LEDGER_CONSOLIDATED.md', 'L-411 follow-up', "**Gap:** groups T, M and C and the three leftovers above, one shell\nat a time. Not part of the Sun's numbers half, which ends with L-455.\n", '- **2026-10-18, Tony\'s look at the two sampling lists.** "all read and\n  correct", with one question: why Voyager 1 at 94.01 AU and Voyager\n  2 at 84? Each printed its source\'s figures, and Voyager 2\'s source,\n  NASA SVS, gives whole AU. Li, Wang and Richardson (2008), already the\n  source of the wind speeds, give "about 83.6 AU" in their abstract\n  (Stone et al. 2008 give 83.7, but only the abstract is open). Tony:\n  "Yes." VOYAGER2_TERMINATION_SHOCK_AU is 83.6 from Li et al., and\n  both sites say "about 83.6 AU". Built the same morning with the\n  chromosphere\'s citations, which had run together with no break\n  (`patch_L411_2_voyager2_20261018.py`, website\n  `patch_L411_3_voyager2_words_20261018.py`).\n- **Recorded, not built:** the chromosphere\'s name types its depth,\n  "Chromosphere (2,000 km skin)", on both sites. The number agrees\n  with CHROMOSPHERE_PHYSICAL_KM, but it is typed. A name is a key: the\n  legend, the shell stamp and the display-figures fixture read it, so\n  it changes with the chromosphere\'s shell when that is next opened.\n**Gap:** groups T, M and C, the three leftovers above and the\nchromosphere\'s name, one shell at a time. Not part of the Sun\'s\nnumbers half, which ends with L-455.\n', 1),
]

class PatchError(Exception):
    pass


def read(rel):
    path = os.path.join(ROOT, rel)
    if not os.path.exists(path):
        raise PatchError("missing file: %s (is this the right folder?)" % rel)
    raw = open(path, "rb").read()
    return raw.replace(b"\r\n", b"\n").decode("utf-8"), (b"\r\n" in raw)


def fingerprint(text):
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def main():
    log, notes, texts, crlf = [], [], {}, {}
    try:
        for rel, content in NEW_FILES.items():
            if os.path.exists(os.path.join(ROOT, rel)):
                have, _c = read(rel)
                if have != content:
                    raise PatchError("%s already exists with other content; "
                                     "nothing was overwritten" % rel)
                notes.append("note: %s already present, identical" % rel)
            else:
                log.append("ok  new     %s" % rel)
        for rel in sorted(set(e[0] for e in EDITS)):
            texts[rel], crlf[rel] = read(rel)
        for rel, want in FINGERPRINTS.items():
            if fingerprint(texts[rel]) != want:
                raise PatchError("BASE MOVED: %s is not the file this patch "
                                 "was built against (%s)" % (rel, SHA))
            log.append("ok  base    %s matches %s" % (rel, SHA))
        for rel, label, old, new, count in EDITS:
            text = texts[rel]
            n = text.count(old)
            if n != count:
                raise PatchError("ANCHOR FAIL [%s %s]: %d matches, expected %d"
                                 % (rel, label, n, count))
            mark = MARKERS.get(rel)
            if mark and (text.count(mark) != 1
                         or text.rindex(old) + len(old) > text.index(mark)):
                raise PatchError("ANCHOR FAIL [%s %s]: not above the "
                                 "run-record marker" % (rel, label))
            texts[rel] = text.replace(old, new)
            log.append("ok  edit    %-44s %s" % (rel, label))
        for rel, want in RESULTS.items():
            if fingerprint(texts[rel]) != want:
                raise PatchError("%s did not come out as built" % rel)
        for page, mark in MARKERS.items():
            above = texts[page][:texts[page].index(mark)].count("\n")
            if above > 130:
                raise PatchError("%s would be %d lines above the run-record "
                                 "marker; the cap is 130" % (page, above))
            log.append("ok  check   %-44s %d lines above the marker (cap 130)"
                       % (page, above))
        for rel, text in list(texts.items()) + list(NEW_FILES.items()):
            bad = sum(1 for ch in text if ord(ch) > 127)
            if bad:
                raise PatchError("%s: %d non-ASCII character(s) after the "
                                 "edits" % (rel, bad))
    except PatchError as exc:
        print("ERROR: %s" % exc)
        print("NOTHING was written.")
        print("Undo is not needed. Discard Changes in GitHub Desktop restores "
              "any file you changed by hand.")
        sys.exit(1)

    for rel, content in NEW_FILES.items():
        path = os.path.join(ROOT, rel)
        os.makedirs(os.path.dirname(path) or ROOT, exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="") as handle:
            handle.write(content)
    for rel, text in texts.items():
        with open(os.path.join(ROOT, rel), "wb") as handle:
            handle.write(text.encode("utf-8"))
        if crlf[rel]:
            notes.append("note: %s was CRLF in the working copy; written LF"
                         % rel)
    for line in log:
        print(line)
    for line in notes:
        print(line)
    print("")
    print("patch applied (%d new files, %d edits in %d files)"
          % (len(NEW_FILES), len(EDITS), len(texts)))
    print("")
    print("NEXT:")
    for line in NEXT:
        print(line)
    print("Undo is Discard Changes in GitHub Desktop.")


if __name__ == "__main__":
    main()
