"""
Transactional patch: document color/RGB exclusion from provenance-scanner
claims, project-wide, per Tony's call (July 16, 2026). Run this once from
the repo root (same directory as provenance_scanner.py). Verified against
a disposable clone: py_compile clean, ASCII-only, and re-running the
scanner afterward reproduces identical tier counts (673 findings,
102/155/396/20) -- documentation only, no scoring change.
"""

fn = 'provenance_scanner.py'
with open(fn, 'rb') as f:
    c = f.read()

edits = [
    # A: extend the numbered known-limitations list in the module docstring
    (b"""         - Agamemnon in L5 list: WRONG. 911 Agamemnon is at L4 (Greek
           camp). Moved to L4 entry.

Module rewritten: April 17, 2026 with Anthropic's Claude Opus 4.7""",
     b"""         - Agamemnon in L5 list: WRONG. 911 Agamemnon is at L4 (Greek
           camp). Moved to L4 entry.

    11. Color/RGB values are exempt from citable claims -- by design,
        not a gap (Tony's call, July 16, 2026; see LEDGER_CONSOLIDATED.md
        L-124/L-125):
        _make_dict_unit already skips non-constant dict values (colors as
        RGB tuples, nested dicts) when building a dict unit's scored
        `entries` -- a color never becomes its own claim needing its own
        citation. What was previously ambiguous is the OTHER direction:
        the "unit of provenance" convention above says a block `# Source:`
        comment covers the whole dict as one unit, which reads as if it
        also certifies that dict's `color` field(s). It does not. Color
        selection across this codebase is a developer/AI aesthetic
        judgment call -- sometimes loosely informed by real imagery or
        composition data, sometimes chosen purely for visual contrast or
        distinction, sometimes arbitrary -- and is never itself a claim
        this scanner verifies, regardless of what citation sits nearby.
        generate_report() prints this as a standing disclosure so it is
        visible in every generated audit, not just in this docstring.

Module rewritten: April 17, 2026 with Anthropic's Claude Opus 4.7"""),

    # B: credit line for this session's change
    (b"""    total-findings delta always means a real citation gap appeared
    elsewhere -- check whether the delta is this file scanning its own
    diff first.
\"\"\"""",
     b"""    total-findings delta always means a real citation gap appeared
    elsewhere -- check whether the delta is this file scanning its own
    diff first.

Updated with Claude Sonnet 5, July 16, 2026: documented the color/RGB
    exemption from citable claims (item 11 above) and added the matching
    disclosure paragraph to generate_report()'s header, per Tony's
    direct call that color citations across the codebase have been
    uneven and some effectively overclaimed -- this documents the
    scanner's existing skip behavior rather than changing any scoring.
\"\"\""""),

    # C: standing disclosure paragraph printed at the top of every generated report
    (b"""    out.append("Unit of provenance: the smallest thing with a coherent "
               "source citation. A dict with one block-level `# Source:` "
               "comment is ONE unit; all its entries inherit that citation. "
               "A hover string with co-referring numbers is ONE unit.")
    out.append("")
    out.append("---")""",
     b"""    out.append("Unit of provenance: the smallest thing with a coherent "
               "source citation. A dict with one block-level `# Source:` "
               "comment is ONE unit; all its entries inherit that citation. "
               "A hover string with co-referring numbers is ONE unit.")
    out.append("")
    out.append("**Color values are excluded from this audit.** RGB/color "
               "fields are never scored as claims (see _make_dict_unit), "
               "and a dict's block `# Source:` citation should never be "
               "read as covering that dict's `color` field(s), even when "
               "it covers everything else in the same unit. This does not "
               "mean color choices have no basis at all -- some are loosely "
               "informed by real imagery or composition data -- but color "
               "selection across this codebase is inconsistent in method: "
               "sometimes evidence-informed, sometimes chosen purely for "
               "visual contrast or distinction, sometimes arbitrary. Treat "
               "every color value as a developer/AI judgment call, not a "
               "measured or verified quantity, regardless of what citation "
               "sits nearby. (Tony's call, July 16, 2026; a low-priority "
               "wishlist item for a real, systematic color-accuracy pass is "
               "tracked at LEDGER_CONSOLIDATED.md L-124.)")
    out.append("")
    out.append("---")"""),
]

for old, new in edits:
    n = c.count(old)
    assert n == 1, f"expected 1 match, got {n}: {old[:60]!r}"
    c = c.replace(old, new)

with open(fn, 'wb') as f:
    f.write(c)

print("provenance_scanner.py patched OK -- 3 edits applied.")