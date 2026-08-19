"""
patch_L209_2_alfven_migration.py -- L-209: correct ALFVEN_SURFACE_RADII to the
heliocentric value, and make every display site READ the constant.

RUN THIS AFTER patch_L213_3_cache_line_and_close.py -- it is fingerprinted
against the ledger that patch produces.

WHAT THIS CHANGES
-----------------
constants_new.py
  - ALFVEN_SURFACE_RADII 18.8 -> 19.7. 18.8 is the ALTITUDE above the
    photosphere quoted by the NASA/JHUAPL release; the shell is drawn from
    Sun centre, so it rendered one solar radius small. Kasper et al. (2021)
    gives the crossing interval as 19.7 to 18.4 solar radii from the center
    of the Sun.
  - The explanation moves onto Source+ and See+ legs, which the worksheet
    request builder actually reads. It previously sat on a bare Note: line
    and an invented HELIOCENTRIC: label, and reached no responder (L-214).
  - The two 2026-08-02 Cross-checked legs are stripped: they certified 18.8.

solar_visualization_shells.py, comet_visualization_shells.py,
info_dictionary.py
  - 10 display sites now interpolate ALFVEN_SURFACE_RADII (and derive the AU
    and million-km figures from it) instead of holding typed copies.
    info_dictionary.py gains its first import.

solar_visualization_shells.py, spacecraft_encounters.py
  - 2 sites that cannot read a value -- a docstring and a # Source: comment
    -- have the figure dropped and point at the constant instead.

LEDGER_CONSOLIDATED.md
  - L-209 closed with the as-built record. L-214 opened for the builder gap.

RUN IT
------
Save this file into the repo root (the folder holding palomas_orrery.py),
open it in VS Code, and click Run. Or from a terminal in that folder:

    python patch_L209_2_alfven_migration.py

Success: one 'ok' line per edit, then 'patch applied' per file.
Failure: a single 'ERROR:' (base moved) or 'ANCHOR FAIL' line. Nothing is
written in either case.

AFTER IT RUNS: re-run ledger_index.py, run the orrery and check the Alfven
shell renders one solar radius larger, and archive this script to
documentation/.

PERMANENT vs DISPOSABLE: this script is disposable. The constant, the
comment block, the imports and the ledger entries are permanent.

Created August 2026 with Anthropic's Claude Opus 5.

Role: devtool
Domain: dev_tools
"""

import hashlib
import os
import sys


def fingerprint(data):
    """Hash CONTENT, not raw bytes: CRLF and LF copies are the same file."""
    return hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()


def to_file_eol(chunk, is_crlf):
    """Translate an LF-written anchor into the file's own line endings."""
    return chunk.replace(b'\n', b'\r\n') if is_crlf else chunk


def load(path, expected):
    if not os.path.exists(path):
        print("ERROR: %s not found. Run this script from the repo root "
              "(the folder holding palomas_orrery.py)." % path)
        sys.exit(1)
    with open(path, 'rb') as f:
        data = f.read()
    got = fingerprint(data)
    if got != expected:
        print("ERROR: BASE MOVED for %s" % path)
        print("  expected content fingerprint %s" % expected)
        print("  found                        %s" % got)
        print("  Nothing was written.")
        sys.exit(1)
    print("ok    base confirmed: %s" % path)
    return data


def apply_edits(path, data, edits):
    """edits: (label, old, new, expected_count). Bottom-up order."""
    is_crlf = data.count(b'\r\n') > 0
    for label, old, new, want in edits:
        old_f = to_file_eol(old, is_crlf)
        new_f = to_file_eol(new, is_crlf)
        n = data.count(old_f)
        if n != want:
            print("ANCHOR FAIL in %s: %s -- expected %d match(es), found %d. "
                  "Nothing written." % (path, label, want, n))
            sys.exit(1)
        data = data.replace(old_f, new_f)
        print("ok    %s: %s%s" % (path, label,
                                  " (x%d)" % want if want > 1 else ""))
    return data


def encoding_report(path, data, inserted):
    """Hard-fail on non-ASCII INSERTED; report pre-existing separately."""
    for chunk in inserted:
        bad = [b for b in chunk if b > 127]
        if bad:
            print("ERROR: this patch would insert %d non-ASCII byte(s) into "
                  "%s. Nothing written." % (len(bad), path))
            sys.exit(1)
    left = sum(1 for b in data if b > 127)
    if left:
        print("note: %s still holds %d non-ASCII byte(s) this patch did not "
              "reach" % (path, left))
    else:
        print("note: %s is ASCII-clean" % path)


def write_all(results):
    for path, blob, inserted in results:
        with open(path, 'wb') as f:
            f.write(blob)
        print("patch applied: %s (%d bytes)" % (path, len(blob)))
        encoding_report(path, blob, inserted)


CN = 'constants_new.py'
SV = 'solar_visualization_shells.py'
CV = 'comet_visualization_shells.py'
SE = 'spacecraft_encounters.py'
ID = 'info_dictionary.py'
LG = 'LEDGER_CONSOLIDATED.md'

EXPECTED = {'constants_new.py': '8ae925d590cda8e95b6e25311c2afb86', 'solar_visualization_shells.py': '8efc7748eed7b6acb726c8a5abc073f9', 'comet_visualization_shells.py': 'ac7e0d9fecf4fdc2d338291903696353', 'spacecraft_encounters.py': 'd1342757dbdf8f29df7ae270f8ef3e18', 'info_dictionary.py': '96e5682fca2abefd5c7ec3d427ff2c2f', 'LEDGER_CONSOLIDATED.md': 'f1cae88b7911dcf3a1eefbb13eda1df4'}

CN_EDITS = [('ALFVEN_SURFACE_RADII 18.8 -> 19.7, explanation onto legs the builder reads', b"ALFVEN_SURFACE_RADII = 18.8\n# Source: Kasper et al. (2021), Phys. Rev. Lett. 127:255101\n# See: Parker Solar Probe first crossing, April 28, 2021\n# Also: https://www.nasa.gov/feature/goddard/2021/nasa-enters-the-solar-atmosphere\n# Note: Varies 10-20 R_sun with solar activity; 18.8 is the measured crossing\n# HELIOCENTRIC: from Sun center. NASA/APL press releases word it as altitude\n#   above the surface, but Kasper's paper says 18.4-19.7 R_sun from center.\n# Cross-checked: Claude 2026-08-02 -- Kasper et al. (worksheet_claude_constants_new.md)\n# Cross-checked: GPT 2026-08-02 -- Kasper et al. (constants_new_citation_verification_gpt.md)\n", b"ALFVEN_SURFACE_RADII = 19.7\n# Source: Kasper et al. (2021), Phys. Rev. Lett. 127:255101 -- first crossing\n# Source+: 28 April 2021 09:33 UT; the sub-Alfvenic interval spans 19.7 to\n# Source+: 18.4 solar radii from the center of the Sun\n# See: HELIOCENTRIC, from Sun center, like every other shell radius in this\n# See+: file. The widely quoted 18.8 R_sun is the ALTITUDE above the\n# See+: photosphere, stated by the NASA/JHUAPL release of 14 December 2021;\n# See+: the paper's own abstract gives the same event as 13 million km above\n# See+: the photosphere. Adding one solar radius gives 19.8, which agrees\n# See+: with the paper's own 19.7 to rounding.\n# See+: PARKER_CLOSEST_RADII below carries the identical correction, made\n# See+: 2026-04-15: 8.86 was altitude, 9.86 is from Sun center.\n# See+: The surface is neither smooth nor fixed -- 10-20 R_sun varying with\n# See+: solar activity, and the 2021 crossing was into a boundary layer above\n# See+: a pseudostreamer rather than a global shell. 19.7 is the measured\n# See+: first crossing, drawn here as a nominal sphere.\n# Also: https://www.nasa.gov/feature/goddard/2021/nasa-enters-the-solar-atmosphere\n# Corrected: 2026-08-19 -- was 18.8, an altitude used as a heliocentric radius.\n#   The prose above was carried on a bare Note: line and an invented\n#   HELIOCENTRIC: label, neither of which the request builder reads, so it\n#   reached no responder. It now rides on See+ legs that do carry (L-214).\n#   The two Cross-checked legs dated 2026-08-02 certified 18.8 and were\n#   stripped with it: a check of the old value is not a check of the new one.\n# Resolved: worksheet_claude-opus-5_pilot_constants_new_20260818.jsonl constants_new.py::ALFVEN_SURFACE_RADII -- origin mismatch, value and Source replaced (L-209)\n", 1)]
SV_EDITS = [('docstring: drop the typed radius, name the constant', b'    Alfven surface: the true outer boundary of the solar corona (~18.8 solar radii,\n    ~0.087 AU). Beyond this surface, plasma can no longer communicate back to the Sun --\n', b'    Alfven surface: the true outer boundary of the solar corona, drawn at\n    ALFVEN_SURFACE_RADII from constants_new.py. Beyond this surface, plasma\n    can no longer communicate back to the Sun --\n', 1), ('MAPS sequence line: read radius and AU from the constant', b"    'Alfven Surface (April 3 ~18:00, 18.8 R_sun, 0.087 AU) -><br>'\n", b"    f'Alfven Surface (April 3 ~18:00, {ALFVEN_SURFACE_RADII} R_sun, {ALFVEN_SURFACE_RADII * SOLAR_RADIUS_AU:.3f} AU) -><br>'\n", 2), ('layer list line: read radius from the constant', b"    '* Alfven Surface: ~18.8 R_sun -- true corona/solar wind boundary<br>'\n", b"    f'* Alfven Surface: ~{ALFVEN_SURFACE_RADII} R_sun -- true corona/solar wind boundary<br>'\n", 2), ('alfven hover: read radius and km from the constant', b'    "* Measured directly: Parker Solar Probe, April 28, 2021 at 18.8 R_sun (13 million km)<br>"\n', b'    f"* Measured directly: Parker Solar Probe, April 28, 2021 at {ALFVEN_SURFACE_RADII} R_sun "\n    f"({ALFVEN_SURFACE_RADII * SUN_RADIUS_KM / 1e6:.1f} million km from Sun center)<br>"\n', 1), ('alfven tooltip: read radius and km from the constant', b'    "  On April 28, 2021, Parker Solar Probe crossed inward at 18.8 R_sun (13 million km),<br>"\n', b'    f"  On April 28, 2021, Parker Solar Probe crossed inward at {ALFVEN_SURFACE_RADII} R_sun "\n    f"({ALFVEN_SURFACE_RADII * SUN_RADIUS_KM / 1e6:.1f} million km from Sun center),<br>"\n', 1), ('Source comment: drop the typed radius, keep the authority', b'# Source: Cranmer et al. (2007); NASA Parker Solar Probe -- Alfven surface ~18.8 R_sun, solar corona boundary\n', b'# Source: Cranmer et al. (2007) -- solar corona boundary structure\n# Source+: the Alfven surface radius itself is ALFVEN_SURFACE_RADII in\n# Source+: constants_new.py, imported here rather than retyped (L-209)\n', 1), ('extended corona hierarchy: read radius from the constant', b'    "  Parker Solar Probe first crossing: 18.8 R_sun, April 28, 2021<br>"\n', b'    f"  Parker Solar Probe first crossing: {ALFVEN_SURFACE_RADII} R_sun, April 28, 2021<br>"\n', 1), ('outer corona note: read radius from the constant', b'    "  Parker Solar Probe measured this at 18.8 R_sun on April 28, 2021.<br>"\n', b'    f"  Parker Solar Probe measured this at {ALFVEN_SURFACE_RADII} R_sun on April 28, 2021.<br>"\n', 1)]
CV_EDITS = [('layer line: read Alfven and streamer radii from the constants', b'        f"Layer: between Alfven Surface (~18.8 R_sun, ~0.087 AU) and Streamer Belt (~6.0 R_sun, ~0.028 AU)<br>"\n', b'        f"Layer: between Alfven Surface (~{ALFVEN_SURFACE_RADII} R_sun, "\n        f"~{ALFVEN_SURFACE_RADII * SOLAR_RADIUS_AU:.3f} AU) and Streamer Belt "\n        f"(~{STREAMER_BELT_RADII} R_sun, ~{STREAMER_BELT_RADII * SOLAR_RADIUS_AU:.3f} AU)<br>"\n', 1), ('import the two shell radii instead of retyping them', b'from planet_visualization_utilities import (\n    KM_PER_AU, SUN_RADIUS_KM, SOLAR_RADIUS_AU)\n', b'from planet_visualization_utilities import (\n    KM_PER_AU, SUN_RADIUS_KM, SOLAR_RADIUS_AU,\n    ALFVEN_SURFACE_RADII, STREAMER_BELT_RADII)\n', 1)]
SE_EDITS = [('docstring: drop the typed Alfven radius', b'            8.33 R_sun confirmed between Alfven surface (~18.8 R_sun) and\n', b'            8.33 R_sun confirmed between the Alfven surface (see\n            ALFVEN_SURFACE_RADII in constants_new.py) and\n', 1)]
ID_EDITS = [('MAPS timeline: read radius and AU from the constant', b"        '* April 3 ~18:00 UTC: crossed the Alfven surface (~18.8 R_sun, ~0.087 AU) --\\n'\n", b"        f'* April 3 ~18:00 UTC: crossed the Alfven surface (~{ALFVEN_SURFACE_RADII} R_sun, ~{ALFVEN_SURFACE_RADII * SOLAR_RADIUS_AU:.3f} AU) --\\n'\n", 1), ('import the shell radius instead of retyping it', b'"""\n\n# Updated note_text for the GUI note_frame\n', b'"""\n\n# Shell radii are read from constants_new.py, never retyped here (L-209).\nfrom constants_new import ALFVEN_SURFACE_RADII, SOLAR_RADIUS_AU\n\n# Updated note_text for the GUI note_frame\n', 1)]
LG_EDITS = [('L-209 closed; L-214 opened for the builder gap', b"**Note:** RICE is Claude's proposal, unratified.\n**Gap:** unverified whether the shell renders from Sun centre. That\ncheck comes first and may close this as comment-only.\n**Ref:** `documentation/PILOT_CONVERGENCE_20260819.md` Part 4;\n`documentation/worksheets/`\n`worksheet_claude-opus-5_pilot_constants_new_20260818.jsonl` R12;\nL-206 (the filename convention these were renamed to obey);\nL-207 (the run that produced it).\n\n", b'- **Confirmed, and the render WAS wrong.** `shell_configs.py` builds the\n  Alfven shell as `ALFVEN_SURFACE_RADII * SOLAR_RADIUS_AU`, a sphere\n  centred on the Sun, so the constant is consumed heliocentrically and\n  the shell rendered one solar radius small.\n- **The correction was ALREADY IN THE FILE, on lines the check could not\n  see.** Two comment lines under the constant read "HELIOCENTRIC: from\n  Sun center ... Kasper\'s paper says 18.4-19.7 R_sun from center." A\n  previous session found the distinction, wrote the paper\'s own range\n  down, and left the value at 18.8 anyway. See L-214: those lines rode\n  on a bare `Note:` and an invented `HELIOCENTRIC:` label, neither of\n  which the request builder reads, so no responder ever saw them.\n- **Resolved at 19.7** (Tony, 2026-08-19), sourced to the PRL body text\n  rather than to the press release. Two independent routes agree: the\n  paper gives the sub-Alfvenic interval as 19.7 to 18.4 solar radii from\n  the center of the Sun, and converting the release\'s 18.8 R_sun of\n  altitude gives 19.8. Taking the paper drops the release as an\n  authority, which also answers GPT\'s separate PARTIAL: the paper does\n  not itself print 18.8.\n- **The two `# Cross-checked:` legs dated 2026-08-02 were stripped with\n  the value.** They certified 18.8. A check of the old value is not a\n  check of the new one -- the exact ride-along the skill warns about.\n  No new leg was written from the pilot: Claude returned APPROX and GPT\n  PARTIAL, neither of which earns one, and Gemini\'s CONFIRMED rests on\n  a note reading "Recollection of the Parker Solar Probe 8th encounter\n  results."\n- **As built** (`patch_L209_2_alfven_migration.py`). The value and the\n  whole explanation live in `constants_new.py`; every display site now\n  READS the constant rather than holding a copy. 12 typed instances\n  across four modules became imports: 8 interpolations in\n  `solar_visualization_shells.py`, 1 in `comet_visualization_shells.py`,\n  1 in `info_dictionary.py` (which gained its first import), and 2 sites\n  that cannot read a value -- a docstring and a `# Source:` comment --\n  had the figure dropped and now point at the constant. The derived\n  0.087 AU and 13 million km figures are computed from the constant, so\n  they moved with it.\n- **Found and NOT touched, deliberately.** The same display strings hold\n  other typed constants -- `ROCHE_LIMIT_RADII` as "3.45 R_sun", the\n  streamer belt as both "4-6" and "6.0". Migrating them is L-181 and\n  L-191, not this item.\n**Note:** RICE is Claude\'s proposal, unratified.\n**Gap:** none. Mode 5 outstanding: the Alfven shell should render one\nsolar radius larger, still nested inside the 50 R_sun outer corona.\n**Ref:** `documentation/PILOT_CONVERGENCE_20260819.md` Part 4;\n`documentation/worksheets/`\n`worksheet_claude-opus-5_pilot_constants_new_20260818.jsonl` R12;\nL-214 (the builder gap this exposed); L-181 and L-191 (the remaining\nshadow constants); L-207 (the run that produced it).\n\n#### [L-214] The request builder drops the comment lines that matter\n<!-- L:214 status:OPEN upd:2026-08-19 section:A flag: rice:3/3/85/2 -->\n- **Found by L-209, 2026-08-19.** The dispatched row for\n  `ALFVEN_SURFACE_RADII` carried two context lines. The three comment\n  lines that stated the answer -- a `# Note:` and two under an invented\n  `# HELIOCENTRIC:` label -- were dropped silently, and the worksheet\n  that resulted looked complete.\n- **The mechanism.** `worksheet_keys.py` defines `VERDICTED_LEG =\n  \'Source\'` and `CONTEXT_LEGS = (\'Ref\', \'Also\', \'See\', \'Derived\',\n  \'Calculation\')`. Anything else closes the run. An unrecognised LABEL\n  is not an unmarked continuation either, so the builder\'s refusal path\n  never fires: the text is not joined, not reported, and not refused.\n- **This is the Visibility Convention\'s own case.** A failure that\n  reaches no reader should REFUSE, not proceed. The builder refuses on\n  unmarked continuation text for exactly this reason and then walks past\n  a whole dropped label.\n- **It bears on the pilot result.** The traps did not spring, but at\n  least one row was checked against a redacted version of itself and\n  nothing in the returns could have said so. Three models spent a\n  dispatch rediscovering what the row already said, and the leg with the\n  least to work with confirmed the wrong value.\n- **Not yet decided:** whether the fix is to widen the recognised label\n  set, to refuse on any unrecognised label under a claim, or to report\n  dropped labels into the worksheet where a responder can name them. The\n  Visibility Convention argues for refusing, and the count of affected\n  rows across the corpus is unmeasured.\n**Note:** RICE is Claude\'s proposal, unratified.\n**Gap:** unmeasured -- how many rows in the 23-row pilot corpus, and how\nmany across `constants_new.py`, carry a label the builder does not read.\nThat count comes before the design.\n**Ref:** `worksheet_keys.py` `LEG_RE` / `legs_of` / `continues_a_leg`;\nL-209 (the row that exposed it); L-203 (the Visibility Convention);\nL-204; L-207.\n\n', 1)]


def main():
    out = []
    for path, edits in ((CN, CN_EDITS), (SV, SV_EDITS), (CV, CV_EDITS),
                        (SE, SE_EDITS), (ID, ID_EDITS), (LG, LG_EDITS)):
        data = load(path, EXPECTED[path])
        data = apply_edits(path, data, edits)
        out.append((path, data, [e[2] for e in edits]))

    # Residual check: no typed Alfven radius may survive in a DISPLAY module.
    # constants_new.py and the ledger are exempt on purpose -- both name 18.8
    # in prose, to record what the value used to be and why it was wrong.
    for path, blob, _ in out:
        if path in (CN, LG):
            continue
        if b'18.8 R_sun' in blob or b'18.8 solar radii' in blob:
            print("ANCHOR FAIL: a typed 18.8 Alfven radius survives in %s. "
                  "Nothing written." % path)
            sys.exit(1)

    write_all(out)
    print("")
    print("Next: re-run ledger_index.py, launch the orrery and confirm the "
          "Alfven shell renders one solar radius larger, then archive this "
          "script to documentation/.")


if __name__ == '__main__':
    main()
