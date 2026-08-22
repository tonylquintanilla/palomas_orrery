"""
patch_L210_7_source_record_suess_nerney.py

Writes the primary-source record for Suess & Nerney (2004) into
documentation/, so the helmet-extent figure has evidence on disk before
any annotation cites it.

WHY THIS EXISTS
    Worksheet First, Annotation Second [CRITICAL]: if no record file
    exists on disk, the annotation does not get written. The helmet
    cusp at 4 R_sun is about to be drawn and cited, so the read that
    supports it is filed first.

    Delivered as a script rather than as text to paste, per
    safe-file-editing 1.7 (L-223). A paste that silently drops leaves
    the same evidence as one that lands; this either writes the file
    and says so, or raises.

WHERE IT LANDS, AND WHY NOT worksheets/
    documentation/SOURCE_suess_nerney_2004_helmet_extent_20260821.md

    The cut is input versus record. worksheet_checker.py opens every
    .md in documentation/worksheets/ on every run; nothing opens this.
    It is evidence a person reads, so it goes in documentation/ and is
    bound by no worksheet grammar. This establishes the SOURCE_ prefix,
    which the tree does not yet use.

ON THE ABSTRACT TEXT -- READ THIS BEFORE RUNNING
    The file records the bibliographic core, the retrieval provenance,
    what the paper was read to settle, and a PARAPHRASE of the two
    claims we take from it. It does NOT reproduce the abstract
    verbatim.

    Two reasons, and the second is the better one. The repo is public
    and the abstract is Elsevier's text. More usefully: a paraphrase
    plus the bibcode forces the question a copied block lets you skip
    -- what does this paper actually establish, and of what KIND. The
    verbatim abstract is one click away at the bibcode, permanently,
    which a copy in our repo is not.

    If you want the verbatim abstract in the file anyway, that is a
    reasonable scholarly source note and the file has a marked, empty
    section headed "Abstract as retrieved" for it. Paste it there after
    running this, or say so and the next patch will carry it.

HOW TO RUN
    Save into the repo ROOT (beside LEDGER_CONSOLIDATED.md), open in
    VS Code, click Run. Or:

        python patch_L210_7_source_record_suess_nerney.py

    It refuses if the file already exists -- it will not overwrite a
    record. Then commit, push, and archive this script to
    documentation/.

PERMANENT vs DISPOSABLE
    Disposable. The record is the permanent half.

Built on 6184b3b910e894784396dea26856f8a178c87bd0 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Written August 21, 2026 with Anthropic's Claude Opus 5.
"""

import os
import sys

ROOT_MARKER = "LEDGER_CONSOLIDATED.md"
OUT_DIR = "documentation"
OUT_NAME = "SOURCE_suess_nerney_2004_helmet_extent_20260821.md"

RECORD = """# Source record -- Suess & Nerney (2004), helmet extent

**Retrieved from NASA ADS on 2026-08-21 by Tony Quintanilla.** Record
written the same day with Anthropic's Claude Opus 5, against repo
`6184b3b9` at https://github.com/tonylquintanilla/palomas_orrery.

## The paper

- **Title:** Flow in streamer boundaries, and streamer stability
- **Authors:** Suess, S. T.; Nerney, S.
- **Publication:** Advances in Space Research, Volume 33, Issue 5,
  pages 668-675
- **Year:** 2004
- **DOI:** 10.1016/S0273-1177(03)00237-0
- **Bibcode:** 2004AdSpR..33..668S
- **Refereed:** yes
- **Keywords:** solar wind; solar corona; streamers

The bibcode is the handle to prefer in annotations. It resolves to the
ADS record, which is public. The DOI resolves to ScienceDirect, which
is paywalled.

## Why it was read

`STREAMER_BELT_RADII` in `constants_new.py` has carried 6.0 R_sun as a
declared visualization assumption since 2026-08-20 (L-210), after an
independent source read found its citation stack unsupported. The
shell is being redesigned from a sphere into a band with a pinch at
the helmet cusp, and the cusp radius needed a source rather than a
choice. This paper was already cited in the shell function's docstring
for a 2-4 R_sun helmet extent; this record is the read that confirms
the citation resolves and says what kind of claim it is.

## What we take from it

Two claims, paraphrased. The exact wording is in the abstract at the
bibcode above.

**1. Helmet extent.** Streamers as a whole reach out to many solar
radii, but the CLOSED-field portion -- the helmet -- goes no higher
than 2-4 solar radii. This is the figure the shell docstring already
cited and the basis for placing the band's cusp at 4, the top of the
stated range.

**2. What the visible streamer boundary is.** Because the closed
region stops so low, the brightness boundary that makes a streamer
visible in a coronagraph cannot be the edge between static plasma and
expanding wind. The paper describes it instead as a boundary between
different FLOW REGIMES, and states that it is reasonable to assume
this boundary separates fast coronal-hole wind from slow wind.

A third detail, not load-bearing but relevant to what the cusp means:
the modelled flow can leak out of the cusp in a way the paper likens
to the small mass releases SOHO/LASCO observes.

## Kind -- and this is the part that constrains the drawing

**Claim 1 is stated as established background, not measured here.**
The paper's own result is an essentially analytic MHD stagnation-flow
model of the streamer boundary. So `# Source:` is the correct leg and
the citation is sound, but the annotation should say the figure is
carried as context in a modelling paper. A later reader must not
mistake 2-4 for this paper's measurement.

**Claim 2 is explicitly an assumption.** The paper's own words mark it
as a reasonable thing to assume, not something it demonstrates. That
matters because the band's redesign would render this boundary as a
visible feature, and drawing a claim asserts it harder than writing it
does. It needs either an observational reference or an explicit
in-hover statement that the identification is an interpretation.
OPEN as of 2026-08-21.

## Related figures found while searching, NOT verified

Recorded so a later read does not start cold. Neither has been read at
source and neither may be cited on this basis.

- Endeve, Holzer & Leer 2004, ApJ 603 -- a two-fluid MHD model placing
  the helmet at about 3 R_sun along the equator.
- A 2005 review reports SOHO/UVCS placing the start of the
  heliospheric current sheet above the streamer core beyond about
  2.7 R_sun. Observational, and the closest thing to a measurement
  found so far.

Both sit below 4, which is consistent with 4 being the generous upper
edge of a range rather than a measured value.

## Abstract as retrieved

Deliberately left empty. See the note in
`patch_L210_7_source_record_suess_nerney.py` -- the verbatim abstract
is Elsevier's text and is one click away at bibcode
`2004AdSpR..33..668S`. Paste it here if a local copy is wanted.

## References from this record

- L-210 -- the streamer row, its withdrawn citations and its held value
- L-209 -- the Alfven surface, where the band dissolves
- `constants_new.py::STREAMER_BELT_RADII`
- `solar_visualization_shells.py::create_sun_streamer_belt_shell`
"""


def fail(msg):
    print("ERROR: " + msg)
    sys.exit(1)


def main():
    if not os.path.exists(ROOT_MARKER):
        fail("%s not found. Run this from the repo root (the folder "
             "holding LEDGER_CONSOLIDATED.md)." % ROOT_MARKER)
    if not os.path.isdir(OUT_DIR):
        fail("%s/ not found. Wrong folder, or the directory is missing."
             % OUT_DIR)

    path = os.path.join(OUT_DIR, OUT_NAME)

    # Refuse to overwrite. A record file is evidence; silently replacing
    # one is the failure this whole discipline exists to prevent.
    if os.path.exists(path):
        fail("%s already exists. Refusing to overwrite a source record. "
             "Nothing was written." % path)

    bad = [c for c in RECORD if ord(c) > 127]
    if bad:
        fail("record holds %d non-ASCII character(s). Refusing." % len(bad))

    # Binary mode with explicit LF, so a Windows run does not silently
    # produce CRLF where every other .md in documentation/ is LF.
    data = RECORD.encode("ascii")
    with open(path, "wb") as f:
        f.write(data)

    print("wrote %s (%d bytes)" % (path, len(data)))

    # ---- success carries evidence, read back from disk ---------------
    with open(path, "rb") as f:
        rb = f.read()

    checks = [
        ("file is byte-identical to what was intended", rb == data),
        ("line endings are LF, no CRLF introduced",
         rb.count(b"\r\n") == 0),
        ("ASCII throughout", all(b < 128 for b in rb)),
        ("bibcode present", b"2004AdSpR..33..668S" in rb),
        ("DOI present", b"10.1016/S0273-1177(03)00237-0" in rb),
        ("page range present", b"pages 668-675" in rb),
        ("retrieval provenance present",
         b"Retrieved from NASA ADS on 2026-08-21" in rb),
        ("kind is recorded for both claims",
         b"stated as established background" in rb
         and b"explicitly an assumption" in rb),
        ("the open question is marked OPEN",
         b"OPEN as of 2026-08-21." in rb),
        ("unverified related figures are marked NOT verified",
         b"NOT verified" in rb),
    ]

    print("")
    print("verification, %d checks, read back from disk:" % len(checks))
    failures = 0
    for desc, ok in checks:
        if not ok:
            failures += 1
        print("  %s  %s" % ("PASS" if ok else "FAIL", desc))

    if failures:
        print("")
        print("ERROR: %d check(s) failed after writing. Delete %s and "
              "report this." % (failures, path))
        sys.exit(1)

    print("")
    print("NEXT: commit, push, and archive this script to documentation/.")
    print("The record is now on disk, so an annotation may cite it.")


if __name__ == "__main__":
    main()
