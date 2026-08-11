"""
patch_masterplan_v18.py

Brings documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md current with the
August 8-10 session. Everything below was ruled by Tony; none of it is a
new proposal.

EIGHT EDITS

  1. Decision 12 -- fetch-and-import: RECOMMENDED -> RATIFIED, with the two
     conditions Tony attached (a data-only rule plus pre-import gate,
     because import executes top-level code; and builder fallback that must
     be OBSERVED at build time rather than inherited from a reviewer's
     claim).
  2. Decision 12 counts -- "7 of 45 top-level assignments are derived"
     measured at HEAD as 6 of 49. The 45-to-49 gap is exactly the four
     L-179/L-180 additions, so that half was stale rather than wrong. The
     constructor-call count is flagged as open rather than corrected: the
     plan says two, measurement finds one, and staleness explains a count
     going UP, not down. That one needs a look, not a patch.
  3. Decision 16 -- pilot slice: OPEN -> RULED. Jupiter first, structure
     before values.
  4. Decision 17 -- interpolation locus: OPEN -> RULED, builder side, with
     Tony's reason (so the orrery and assembler cannot diverge) and the
     accepted cost (the cache holds finished strings, so rephrasing needs
     a rebuild).
  5. New decision 18 -- the registry's three-zone shape. This was ruled on
     August 8 and has no home in the plan at all.
  6. Artifact 2 -- the migration-order ruling recorded next to the standing
     "Batch 2 gates Artifact 2" statement. Artifact 2 stops being blocked
     and becomes step 2. The older wording is left in place as history,
     matching how v17 handled the same kind of supersession.
  7. Layer 3 -- the two places the plan says the nightly Task Scheduler job
     is ENABLED. Retired August 10; disabled, not deleted.
  8. Closing status block -- skill versions and protocol version, which
     still read the August 5 state.

WHAT THIS DOES NOT DO

  The plan is not ASCII-only and is not meant to be -- it uses em dashes
  and section signs throughout. This patch leaves all existing characters
  alone and adds only ASCII, so the file's own conventions are preserved.

  Decision 13's retirement note for export_orbit_cache.py is untouched.
  The dashboard entry it mentions has since been removed, but confirming
  that is a separate check.

Target file: documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md
Built on c1ba36e4d8120cdca00f6fb67eb1340de8762782

HOW TO RUN
  Save this file in the ORRERY REPO ROOT (the folder containing
  documentation/), open it in VS Code, and click Run.

  Or from a terminal in that folder:  python patch_masterplan_v18.py

WHAT SUCCESS LOOKS LIKE
  One "ok" line per edit, then "patch applied" with the byte count.

WHAT FAILURE LOOKS LIKE
  A single line beginning "ERROR:" or "ANCHOR FAIL:". Nothing is written
  in either case. Every anchor is checked before anything is written.

AFTERWARD
  MASTER_PLAN_INTERACTIVE_GALLERY_SUMMARY.md was already updated on
  August 11 and needs nothing. Its header carries a note saying the
  summary is AHEAD of the plan on five rulings; once this patch lands
  that note is stale and can come out on the next pass.
"""

import hashlib
import os
import sys

TARGET = os.path.join('documentation', 'MASTER_PLAN_INTERACTIVE_GALLERY.md')
BASE_MD5 = 'f1e090f5849c3856868b178bc2a863b2'   # line-ending normalized

EDITS = []

# ------------------------------------------------------------------
# 1 + 2. Decision 12.
# ------------------------------------------------------------------

EDITS.append((
    'decision 12 header and conditions',
    """12. **How feature data crosses the repo boundary.** RECOMMENDED, not yet
    ratified: **fetch-and-import.** The nightly builder resolves the""",
    """12. **How feature data crosses the repo boundary.** **RATIFIED 2026-08-08
    (Tony).** **fetch-and-import.** The builder resolves the"""))

EDITS.append((
    'decision 12 ratification conditions',
    """    Trust argument, recorded because future sessions will re-ask it: the
    builder, the orrery GUI, and every patch script Tony runs already
    come from the same two repos under the same account, so importing one
    more file from it adds NO NEW TRUST ROOT. A raw fetch at a full
    40-character SHA is content-addressed, so there is no window in which
    what was checked and what was imported can differ.""",
    """    Trust argument, recorded because future sessions will re-ask it: the
    builder, the orrery GUI, and every patch script Tony runs already
    come from the same two repos under the same account, so importing one
    more file from it adds NO NEW TRUST ROOT. A raw fetch at a full
    40-character SHA is content-addressed, so there is no window in which
    what was checked and what was imported can differ.
    **Two conditions attach to the ratification (Tony, 2026-08-08).**
    (a) A data-only rule for `constants_new.py` plus a pre-import gate,
    because import executes top-level code. The gate is roughly ten lines
    and checks two structural properties before the file runs: that every
    import is on an allowlist, and that no dictionary has a duplicate key.
    The duplicate-key check is the one capability fetch-and-import
    otherwise loses, since after import Python has already silently kept
    the last duplicate. (b) The fallback when GitHub is unreachable must
    be OBSERVED at build time, not inherited from a reviewer's claim. It
    falls back to the last committed copy and never writes empty features.
    Feasibility confirmed at ratification: `constants_new.py` imports only
    numpy and datetime, nothing orrery-internal, so the fetch really is
    ONE file with no dependency tree. (The numpy import is dead -- present
    since April 5 2025 with zero uses across all 46 commits -- and comes
    out when the migration next touches the file.)"""))

EDITS.append((
    'decision 12 assignment counts',
    """    reading the file with Python's `ast` module without executing it
    (fights the store's design -- 7 of 45 top-level assignments are
    derived rather than literal, and two contain constructor calls
    `ast.literal_eval` cannot evaluate at all).""",
    """    reading the file with Python's `ast` module without executing it
    (fights the store's design -- 6 of 49 top-level assignments are
    derived rather than literal, and at least one contains a constructor
    call `ast.literal_eval` cannot evaluate at all).
    **Count correction, 2026-08-11.** Measured at HEAD: 49 assignments, 6
    derived. The plan read 7 of 45. The 45-to-49 gap is exactly the four
    L-179/L-180 additions, so that half was stale rather than wrong. The
    constructor-call count is a genuine open question rather than a
    correction: the plan says two, measurement finds one
    (`HORIZONS_MAX_DATE = datetime(...)`), with no calls nested inside any
    of the six derived expressions -- and staleness explains a count going
    UP, not down. Resolve by looking, not by patching. The argument
    against `ast` is unaffected either way; one non-evaluable constructor
    is as fatal to it as two."""))

# ------------------------------------------------------------------
# 3. Decision 16.
# ------------------------------------------------------------------

EDITS.append((
    'decision 16 ruled',
    """16. **Pilot slice inside Track 0.** OPEN, Tony decides. Fable round 2""",
    """16. **Pilot slice inside Track 0.** **RULED 2026-08-08 (Tony): Jupiter
    first, structure before values.** Prove the registry structure on
    Jupiter, where the served data is already complete and correct so the
    transport gets a real acceptance test. Then cross-check Artifact 2's
    remaining values, writing them into the proven structure. Then
    complete the migration and resolve what surfaces. The recommendation
    below is what Tony ruled on, and it stands as written except for one
    number: it says Jupiter has 5 entries, and the August 10 session
    counted 4 ring entries. Confirm before the pilot starts, since the
    pilot is scoped by it.
    Fable round 2"""))

# ------------------------------------------------------------------
# 4. Decision 17.
# ------------------------------------------------------------------

EDITS.append((
    'decision 17 ruled',
    """17. **Where description interpolation happens.** OPEN. The served cache
    can hold templates plus values, with the assembler interpolating at
    render time; or pre-interpolated final strings, with the builder
    interpolating at build time. Fable recommends builder-side: it keeps
    the assembler dumb, keeps the failure surface at build time where
    quarantine already exists, and means a template error is caught
    nightly rather than in a user's browser. Either answer works, but it
    decides the cache schema, so it is decided before the schema is
    written.""",
    """17. **Where description interpolation happens.** **RULED 2026-08-08
    (Tony): BUILDER SIDE.** The served cache holds pre-interpolated final
    strings. Tony's reason is not the one Fable argued: it is that the
    orrery and the assembler cannot diverge if only one of them ever
    composes the sentence. Accepted cost, stated at the time: the cache
    holds finished strings, so rephrasing anything requires a rebuild.
    Fable's supporting arguments also hold -- it keeps the assembler dumb,
    keeps the failure surface at build time where quarantine already
    exists, and means a template error is caught at build rather than in a
    user's browser. The alternative (cache holds templates plus values,
    assembler interpolates at render time) is retired.

18. **Shape of a registry entry.** **RULED 2026-08-08 (Tony): three
    zones.** Every entry separates:
    - **MEASURED** -- a published value, carrying value, unit, AND source.
      Not a bare number with the unit baked into the key name. Tony's
      reasoning: published values arrive in mixed units regardless, so a
      conversion step is needed for uniform display text no matter what
      is stored. Storage stays heterogeneous; conversion happens at the
      display step. This DELETED an earlier Claude recommendation for a
      per-feature unit convention.
    - **DECLARED** -- a developer style choice (color, opacity). No source
      is expected, and its absence is not a finding.
    - **DERIVED display text** -- NOT stored. Built by interpolation from
      the other two, at the builder, per decision 17.
    Two structural constraints follow. Everything measured must sit at
    MODULE SCOPE, readable without executing anything -- this is what
    makes L-181 the PRECONDITION for L-190 rather than more work for it,
    since a value inside a draw function cannot be walked by a static
    pass, which is exactly why the scanner cannot see `belt_distances`
    today. And there is ONE not-yet-sourced state, not two: the orrery is
    the source, so if the orrery does not offer a value there is nothing
    to render and no field to fill. A not-yet-sourced field means a value
    that IS rendered but has no recorded provenance. Distinguishable from
    absent; never an empty field.
    `CHROMOSPHERE_RADIUS_LINE` is the working precedent for the derived
    zone: two values stored in different units feeding one sentence that
    emits solar radii, AU, and km.
    One question stays open and is better answered against Jupiter's ring
    entries than in the abstract: should EVERY measured field be
    range-capable? The evidence that it might -- Jupiter's main ring
    `description` says the thickness is about 30 to 300 km while
    `thickness_km` says 30, so the prose is more accurate than the data
    beside it."""))

# ------------------------------------------------------------------
# 5. Artifact 2 ordering.
# ------------------------------------------------------------------

EDITS.append((
    'Artifact 2 migration order',
    """Batch 2 is the stated gate before Artifact 2 (Tony, 2026-08-05):
all provenance batches clear before the Jupiter/Saturn artifact
proceeds.""",
    """AMENDED AGAIN 2026-08-08 (Tony): Artifact 2 is no longer BLOCKED; it
becomes step 2. The migration proves the registry structure on Jupiter
first, because Jupiter's served data is complete and correct and so gives
the transport a real acceptance test. Artifact 2's remaining values are
then cross-checked INTO that proven structure, which is the same work the
Batch 2 gate was asking for, sequenced so it lands somewhere. The two
August wordings below are preserved as history, not withdrawn.
Batch 2 is the stated gate before Artifact 2 (Tony, 2026-08-05):
all provenance batches clear before the Jupiter/Saturn artifact
proceeds."""))

# ------------------------------------------------------------------
# 6. Layer 3, two sites.
# ------------------------------------------------------------------

EDITS.append((
    'Layer 3 status, section 1',
    """Independently: Layer 3 (nightly Task Scheduler) is ENABLED and its
core mechanism is proven -- unattended trigger, Horizons fetch, and data
assembly all confirmed working end to end -- but the final promotion step
has a known intermittent failure under the scheduler's execution context
(see S3a addendum, July 24). Watch a few more cycles before trusting it
fully hands-off.""",
    """Independently: Layer 3 (nightly Task Scheduler) is RETIRED as of
2026-08-10 (Tony). The task is DISABLED, not deleted, and the builder now
runs manually with Tony committing the result himself. His reasoning: the
build cannot run without his machine on anyway, so the schedule created an
appearance of automation the setup could not deliver -- three nights were
missed in the week before the ruling and the failure was silent. Running
it by hand also dissolves the surprise behind the August 10 gallery
incident, because a build in flight is no longer something he can walk
into unaware. First manual build ran clean end to end on 2026-08-11
(gallery `d5437f0`).
The layer's history is kept because it becomes live again the moment the
build runs unattended by ANY mechanism, including a GitHub Action: its
core mechanism was proven -- unattended trigger, Horizons fetch, and data
assembly all confirmed working end to end -- but the final promotion step
had a known intermittent failure under the scheduler's execution context
(see S3a addendum, July 24)."""))

EDITS.append((
    'Layer 3 status, closing block',
    """attempting Artifact 2 (Jupiter/Saturn) Mode 5. Layer 3 (nightly Task
Scheduler) enabled with known intermittent promotion-step glitch (S3a
addendum, July 24).""",
    """attempting Artifact 2 (Jupiter/Saturn) Mode 5. Layer 3 (nightly Task
Scheduler) RETIRED 2026-08-10 -- task disabled not deleted, builder run
manually, first manual build clean 2026-08-11. The known intermittent
promotion-step glitch (S3a addendum, July 24) is moot while manual and
returns with the schedule if it ever does."""))

# ------------------------------------------------------------------
# 7. Closing status block versions.
# ------------------------------------------------------------------

EDITS.append((
    'skill and protocol versions',
    """orrery-coding-conventions 1.3, provenance-discipline 1.7,
ledger-and-session-records 1.5, safe-file-editing 1.2,
agentic-pre-test 1.2, gallery-pipeline 1.2, gallery-assembler 1.1,
gallery-cache-builder 1.2, horizons-orbital-mechanics 1.1,
earth-system-pipeline 1.1. Protocol at v3.34.""",
    """orrery-coding-conventions 1.3, provenance-discipline 1.8,
ledger-and-session-records 1.5, safe-file-editing 1.3,
agentic-pre-test 1.2, gallery-pipeline 1.2, gallery-assembler 1.1,
gallery-cache-builder 1.3, horizons-orbital-mechanics 1.1,
earth-system-pipeline 1.1. Protocol at v3.37.
(Versions above current as of 2026-08-11: safe-file-editing 1.2 -> 1.3
Aug 7; provenance-discipline 1.7 -> 1.8 and gallery-cache-builder
1.2 -> 1.3 Aug 11; protocol v3.34 -> v3.37 Aug 8-11. All three stores
reconciled -- repo, manifest, account install.)"""))


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, TARGET)

    if not os.path.exists(path):
        print("ERROR: " + TARGET + " not found.")
        print("       Put this script in the orrery repo root (the folder")
        print("       that contains documentation/) and run again.")
        return 1

    with open(path, 'rb') as f:
        data = f.read()

    fp = hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()
    if fp != BASE_MD5:
        print("ERROR: base moved. The master plan is not the file this")
        print("       patch was built against. Expected " + BASE_MD5 + ",")
        print("       found " + fp + ". Nothing was written.")
        return 1

    text = data.decode('utf-8')
    crlf = '\r\n' in text
    if crlf:
        text = text.replace('\r\n', '\n')

    before_nonascii = sum(1 for ch in text if ord(ch) > 127)

    # Check every anchor before writing anything.
    for name, old, new in EDITS:
        n = text.count(old)
        if n != 1:
            print("ANCHOR FAIL: " + name)
            print("             expected 1 match, found " + str(n) + ".")
            print("             Nothing was written.")
            return 1

    for name, old, new in EDITS:
        text = text.replace(old, new)
        print("ok   " + name)

    after_nonascii = sum(1 for ch in text if ord(ch) > 127)
    if after_nonascii != before_nonascii:
        print("ANCHOR FAIL: non-ASCII count changed from "
              + str(before_nonascii) + " to " + str(after_nonascii) + ".")
        print("             This patch should not touch them. Nothing written.")
        return 1

    if crlf:
        text = text.replace('\n', '\r\n')

    with open(path, 'wb') as f:
        f.write(text.encode('utf-8'))

    print("")
    print("patch applied -- " + TARGET)
    print("now " + str(len(text.replace('\r\n', '\n').split('\n')))
          + " lines, " + str(before_nonascii)
          + " non-ASCII characters preserved unchanged.")
    print("")
    print("Decisions 12, 16, 17 now carry their rulings; 18 is new.")
    print("One item stays OPEN by design: the constructor-call count in 12.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
