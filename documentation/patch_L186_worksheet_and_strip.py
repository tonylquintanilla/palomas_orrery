"""
patch_L186_worksheet_and_strip.py

L-186 cleanup, items 1-3 of the August 8 handoff.

  A. Repoint 8 filename-less annotations in constants_new.py at the newly
     filed Gemini worksheet:
         (Gemini worksheet) -> (worksheet_gemini_constants_remaining.md)
  B. Strip the appended checked-values from 3 annotations that already
     name a .md file, per Tony's ruling of 2026-08-08 (strip, not extend):
         (foo.md: 14.27 Mkm) -> (foo.md)

PREREQUISITE
    Save the Gemini worksheet as:
        documentation/worksheet_gemini_constants_remaining.md
    (delivered alongside this script, already correctly named)

HOW TO RUN
    Save this file into the SAME folder as constants_new.py
    (the palomas_orrery repo root), open it in VS Code, click Run.
    Equivalent command line: python patch_L186_worksheet_and_strip.py

WHAT SUCCESS LOOKS LIKE
    One "ok" line per edit (11 total), then one "patch applied" line
    per file. Nothing is written unless every edit in that file matches
    exactly once.

WHAT FAILURE LOOKS LIKE
    A single "ERROR:" line (base file is not what this was built against)
    or "ANCHOR FAIL" (a specific edit's text was not found). Nothing is
    written either way. Safe to re-check and retry.

Built on 0811ffcc1746d30971d731db7d1893176c2ae6a4 at
https://github.com/tonylquintanilla/palomas_orrery

Patch written August 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

NEW_REF = b"worksheet_gemini_constants_remaining.md"

# Base fingerprints, md5 of content with line endings normalized to LF.
# Line endings are not content: a CRLF working copy of an LF repo file
# is the same file and must not read as BASE MOVED.
BASES = {
    "constants_new.py":              "48cdb647a8fbe28f23164133c5a9545a",
    "eris_visualization_shells.py":  "e06dd30f2ee2910bdf29186180aeba2a",
    "venus_visualization_shells.py": "5b7c3768981746408434b2e94bb6286c",
}

# Anchors are two lines: the preceding line disambiguates, because five of
# the eight Gemini annotation lines are byte-identical to each other.
CONSTANTS_EDITS = [
    (b"# Also: https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html\n"
     b"# Cross-checked: Carroll & Ostlie via Gemini 2026-08-02 (Gemini worksheet)"),
    (b"# Also: Carroll & Ostlie (2017), Ch. 11 gives 0.2-0.25 R_sun\n"
     b"# Cross-checked: Carroll & Ostlie via Gemini 2026-08-02 (Gemini worksheet)"),
    (b"# Cross-checked: helioseismology literature via GPT 2026-08-02 (constants_remaining_independent_verification_gpt.md)\n"
     b"# Cross-checked: Carroll & Ostlie via Gemini 2026-08-02 (Gemini worksheet)"),
    (b"#   Carroll & Ostlie Ch. 11 confirms ~2000 km, not 1.5 R_sun)\n"
     b"# Cross-checked: Carroll & Ostlie via Gemini 2026-08-02 (Gemini worksheet)"),
    (b"#         Ch. 11 -- chromosphere extends ~2000 km above the photosphere.\n"
     b"# Cross-checked: Carroll & Ostlie via Gemini 2026-08-02 (Gemini worksheet)"),
    (b"# Note: Visualization boundary for inner (K-)corona; physical extent 2-3 R_sun\n"
     b"# Cross-checked: Golub & Pasachoff via Gemini 2026-08-02 (Gemini worksheet)"),
    (b"#   streamer-belt structure remains observable beyond 6 R_sun.\n"
     b"# Cross-checked: Golub & Pasachoff via Gemini 2026-08-02 (Gemini worksheet)"),
    (b"# Cross-checked: JPL SSD via GPT 2026-08-02 (constants_remaining_independent_verification_gpt.md)\n"
     b"# Cross-checked: NASA NSSDCA via Gemini 2026-08-02 (Gemini worksheet)"),
]

EDITS = {
    "constants_new.py": [
        (a, a.replace(b"(Gemini worksheet)", b"(" + NEW_REF + b")"))
        for a in CONSTANTS_EDITS
    ],
    "eris_visualization_shells.py": [
        (b"(batch1_tier2_followup_gpt.md: 14.27 Mkm)",
         b"(batch1_tier2_followup_gpt.md)"),
        (b"(worksheet_gemini_batch1_followup.md: 14.26 Mkm)",
         b"(worksheet_gemini_batch1_followup.md)"),
    ],
    "venus_visualization_shells.py": [
        (b"(batch1_tier2_followup_gpt.md: 167.08 R_V at a)",
         b"(batch1_tier2_followup_gpt.md)"),
    ],
}


def fingerprint(data):
    return hashlib.md5(data.replace(b"\r\n", b"\n")).hexdigest()


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    staged = {}

    # Pass 1: verify every base and every anchor. Write nothing yet.
    for name, edits in EDITS.items():
        path = os.path.join(here, name)
        if not os.path.exists(path):
            print("ERROR: not found: %s" % name)
            print("       Put this script in the same folder as constants_new.py.")
            return 1

        with open(path, "rb") as f:
            data = f.read()

        fp = fingerprint(data)
        if fp != BASES[name]:
            print("ERROR: base moved: %s" % name)
            print("       expected %s" % BASES[name])
            print("       found    %s" % fp)
            print("       Nothing written. Re-pull or re-cut this patch.")
            return 1

        # Anchors are authored LF. Translate to the file's own convention
        # rather than restyling the file.
        is_crlf = data.count(b"\r\n") > 0

        for old, new in edits:
            o = old.replace(b"\n", b"\r\n") if is_crlf else old
            n = new.replace(b"\n", b"\r\n") if is_crlf else new
            count = data.count(o)
            if count != 1:
                head = o.split(b"\n")[-1][:70].decode("ascii", "replace")
                print("ANCHOR FAIL in %s: expected 1 match, got %d" % (name, count))
                print("       %s" % head)
                print("       Nothing written.")
                return 1
            data = data.replace(o, n)
            print("ok   %s: %s" % (name, o.split(b"\n")[-1][:66].decode("ascii", "replace")))

        staged[path] = data

    # Pass 2: all anchors verified across all files. Now write.
    for path, data in staged.items():
        with open(path, "wb") as f:
            f.write(data)
        print("patch applied: %s (%d bytes)" % (os.path.basename(path), len(data)))

    print("")
    print("11 edits across 3 files.")
    print("Next: confirm documentation/%s is committed too."
          % NEW_REF.decode("ascii"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
