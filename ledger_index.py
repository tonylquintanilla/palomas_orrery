#!/usr/bin/env python3
"""
ledger_index.py - Generate the at-a-glance INDEX for the consolidated ledger.

The DETAIL blocks are the single source of truth. Each block is headed by:

    #### [L-016 | #6] Archive dead shell functions
    <!-- L:016 status:OPEN upd:- section:D.Structural flag: rice:2/1/80/1 -->
    <narrative, verbatim>
    **Gap:** ...
    **Ref:** ...

This tool scans every such block and rewrites the per-section index tables
between the INDEX:START / INDEX:END markers -- nothing else is touched, so it
is safe to re-run (module_atlas.py pattern).

What "properly indexed" means and what gets fixed automatically vs. flagged
for review is split by how safely it can be checked. Two facts matter --
the metadata `section:` tag, and the block's PHYSICAL position -- and
which one is treated as ground truth depends on which direction is being
checked:
  - If the tag ALREADY names a recognized closed bucket (a track's own
    bucket, e.g. `W.Done`), the TAG wins: a human tagged it that
    deliberately, so the tool trusts it for membership and only fixes
    physical position if it disagrees.
  - If the tag does NOT already name a closed bucket (still 'C', a live
    bucket, or anything else), PHYSICAL POSITION wins: a DONE block
    sitting inside a track's own physical span almost always means a
    forgotten retag, so the tool infers the correct tag from where it
    already sits and fixes the tag instead.
Either direction converges on the same end state: correct tag AND
physically inside that bucket's own destination heading.

STRUCTURAL CHECKS (always run; report only -- these need a human fix, a typo
or a genuine judgment call, not something this tool can decide):
  - malformed or missing metadata line below a #### header
  - header L-number disagrees with its own metadata line
  - duplicate L-number reused by more than one block
  - unrecognized `section:` tag (not in the known section list -- typos sort
    silently to the end of the index otherwise, with no error)
  - a NON-done block (OPEN/BLOCKED/PENDING-GATE/PROPOSED/DEFERRED/etc.)
    tagged 'C' or a track's closed bucket -- the dangerous direction: this
    makes live work invisible in the live-item count and easy to lose
    track of. This one stays a judgment call because a LIVE item has many
    legitimate destinations (A, D.*, E, G, H, W.Prep/Active/Deferred...)
    and physical position alone doesn't narrow it to one.

AUTO-FIX (runs every invocation that is not `--check`; no Gap phrase or
trigger text required -- see find_closed_bucket_issues, the single
function both check() and the fixer read from, so they can't drift apart):

For a DONE block, there is ALWAYS exactly one correct closed bucket, and
it's always mechanically knowable -- unlike a live item, DONE has no open
question about which bucket it belongs in, only whether the tag and the
physical position already agree on it. Each closed bucket has TWO nested
spans, found generically (never by mapping heading text to a code):
  - a coarse TRACK span (a '## ' heading, e.g. `## W. WEB PUBLICATION
    TRACK`) -- used only to INFER membership when the tag doesn't already
    claim a bucket (a forgotten retag).
  - an exact DESTINATION span (a '### ' heading inside that track, e.g.
    `### W.Done -- closed items, kept with the track`, or the general
    `## C. RECONCILED LEDGER...` for the default bucket) -- the actual
    physical home a block must end up inside, regardless of how its
    target bucket was determined.

  1. RETAG IN PLACE (only when the tag doesn't already name a recognized
     closed bucket). Membership is inferred from the coarse track span: a
     DONE block sitting anywhere inside it belongs to that track's
     bucket; a DONE block inside no track's span belongs to the general
     'C' archive -- there is no third option. If the current tag
     disagrees, it's corrected. No physical move in this step alone.
  2. PHYSICAL MOVE. Whatever the block's target bucket is (already
     correctly tagged, or just corrected in step 1), if it is NOT
     physically inside THAT bucket's own destination span, it gets
     relocated to the end of that span. A block can need both steps in
     the same run (tagged wrong AND stranded, like a forgotten retag that
     also never got filed); it can also need only step 2 (already tagged
     right, but physically stranded elsewhere, like an item correctly
     tagged a track's bucket but filed in the general archive by a
     chronological cleanup pass that didn't notice).

Every span above is found by find_span/find_top_level_span/
find_subsection_span, which only ever answer "does this block sit
anywhere under this ONE named heading" -- never "which specific
subsection". Mapping an arbitrary subsection's heading text back to its
canonical code (e.g. "### D.Feature -- Bucket A (near-term)" -> tag
D.Feature-A, or "## PENDING ACTION (Tony-side)" -> tag B) is NOT
attempted -- that reverse mapping isn't mechanical: several existing
headings don't literally contain their own tag, so a lookup table doing
it would need constant hand-maintenance and would misfire silently the
moment a heading is reworded. A span found by literal heading match costs
nothing to maintain: it just scans for the next matching line, whatever
it's named, so it can't go stale. That's exactly why DONE can be fully
automatic (a couple of literal-heading spans settle it) while LIVE cannot
(settling it would need that same fragile subsection mapping).

RICE scoring (adapted for Paloma's Orrery):
    Metadata field: rice:R/I/C/E (e.g., rice:3/2/80/1)
    Omit or use rice:- for unscored items.

    R (Reach/Value)   - Educational/visual value
                        3 = core experience, 2 = gallery quality,
                        1 = internal hygiene
    I (Impact)        - Magnitude of improvement
                        3 = new capability, 2 = meaningful,
                        1 = polish, 0.5 = marginal
    C (Confidence %)  - Scope clarity
                        100 = ready to build, 80 = mostly scoped,
                        50 = needs design, 25 = speculative
    E (Effort)        - Sessions to complete
                        0.5 = quick fix, 1 = one session,
                        2 = two sessions, 3 = three+

    Score = R x I x (C / 100) / E

    Items with scores are sorted descending within each section;
    unscored items follow, sorted by L-number.

Usage:
    python3 ledger_index.py LEDGER_CONSOLIDATED.md          # rewrite in place
    python3 ledger_index.py LEDGER_CONSOLIDATED.md --check   # report only, exit 1 on problems
    (no path given -> looks for LEDGER_CONSOLIDATED.md next to this script)

Exit codes: 0 = clean; 1 = consistency problems remain (the file is still
written when not run with --check -- problems are reported, not silently
dropped); 2 = no path given and no default file found next to the script.

Module updated: July 2026 with Anthropic's Claude Sonnet 5 (status/section
consistency checks across all statuses; every DONE-item closed-bucket
mismatch is fully auto-fixed via a two-level model -- a coarse track span
infers membership when the tag doesn't already claim a bucket, and each
bucket's own destination heading, e.g. `### W.Done`, is where the block
must physically end up either way, so a tag can also win over a stale
position when the tag already names a real bucket; only a live item's tag
and an unrecognized tag remain judgment calls). June 2026 with Anthropic's
Claude Opus 4.6 (RICE scoring).
"""
import re
import sys
import pathlib

HEAD_RE = re.compile(r'^####\s*\[L-(\d+)(?:\s*\|\s*#?([\w.\-/]+))?\]\s*(.+?)\s*$')
META_RE = re.compile(r'^<!--\s*L:(\d+)\s+status:(\S+)\s+upd:(\S+)\s+section:(\S+)(?:\s+flag:(\S*))?(?:\s+rice:(\S*))?\s*-->\s*$')
START = '<!-- INDEX:START (generated by ledger_index.py -- do not edit this zone by hand) -->'
END = '<!-- INDEX:END -->'

# Disposition -> needs-attention (gets the leading '!')
GAP_STATUS = {'OPEN', 'BLOCKED', 'PENDING-GATE'}

# Statuses that mean "closed" for status/section consistency purposes.
# 'DONE and friends' per the ledger's own convention -- add here if a new
# closed-equivalent status is ever introduced.
CLOSED_STATUSES = {'DONE'}
# (CLOSED_SECTIONS -- which tags count as a closed archive bucket -- is
# derived below from TRACK_DONE_BUCKETS, once that registry is defined.)

# Section display order (sections not listed sort to the end, alphabetically).
# Section C (closed/done) sorts last so the live backlog reads first.
SECTION_ORDER = ['A', 'B', 'D.Movement', 'D.Priority', 'D.Structural',
                 'D.Cosmetic', 'D.Feature-A', 'D.Feature-B', 'D.Feature-C',
                 'D.Parked', 'D.LooseEnd', 'E', 'G', 'H',
                 'O.Comets', 'O.Asteroids', 'O.Moons', 'O.Exoplanets',
                 'O.Spacecraft', 'O.Presets',
                 'W.Prep', 'W.Active', 'W.Deferred', 'C']

# Tag aliases: normalize legacy/variant section tags to the canonical letter.
SECTION_ALIASES = {'PENDING': 'B'}

# Descriptive titles mirroring the DETAIL '##'/'###' headers, so the index
# reads as a structural map rather than a column of bare letters.
SECTION_TITLES = {
    'A': 'A. Active Separate Tracks',
    'B': 'B. Pending Action (Tony-side)',
    'C': 'C. Reconciled -- Done (closed; for the record)',
    'D.Movement': 'D.Movement -- Movement track',
    'D.Priority': 'D.Priority -- Real bugs',
    'D.Structural': 'D.Structural -- Dead code / honest shells',
    'D.Cosmetic': 'D.Cosmetic -- Polish',
    'D.Feature-A': 'D.Feature-A -- Bucket A (near-term)',
    'D.Feature-B': 'D.Feature-B -- Bucket B (editorial)',
    'D.Feature-C': 'D.Feature-C -- Bucket C (architecture)',
    'D.Parked': 'D.Parked (Tony calls)',
    'D.LooseEnd': 'D.Loose end to reconcile',
    'E': 'E. AU-Convention Compliance',
    'G': 'G. Open Questions / Tony Calls',
    'H': 'H. Gallery / Studio Track',
    'O.Comets': 'O.Comets -- candidate comet objects',
    'O.Asteroids': 'O.Asteroids -- candidate asteroid objects',
    'O.Moons': 'O.Moons -- candidate moon objects',
    'O.Exoplanets': 'O.Exoplanets -- candidate exoplanet systems',
    'O.Spacecraft': 'O.Spacecraft -- candidate spacecraft objects',
    'O.Presets': 'O.Presets -- candidate gallery/studio presets',
    'O.Done': 'O.Done -- Object Candidates track, closed items',    
    'W.Prep': 'W.Prep -- Web Publication prep (before Phase 0)',
    'W.Active': 'W.Active -- Web Publication active phase',
    'W.Deferred': 'W.Deferred -- Web Publication deferred (captured)',
    'W.Done': 'W.Done -- Web Publication track, closed items',
}

# Every section tag this tool recognizes -- used to catch typos, which
# otherwise sort silently to the end of the index under their own literal
# (unrecognized) tag with no error at all.
KNOWN_SECTIONS = set(SECTION_TITLES) | set(SECTION_ALIASES) | {'C'}

# Sections always rendered in the index even when they have no items
# (so the standing structure is visible -- e.g. B. Pending Action).
ALWAYS_SHOW = {'B'}

# The literal, already-load-bearing header that opens section C physically
# in the DETAIL record (its close is found generically -- see
# find_top_level_span).
# The literal, already-load-bearing header that opens section C physically
# in the DETAIL record (its close is found generically -- see
# find_top_level_span).
SEC_C_HEADER = '## C. RECONCILED LEDGER'

# Tracks that own their OWN closed bucket, separate from the general C
# archive -- keyed by the section tag. Each entry carries two headers:
#   'track_header'  -- the track's own top-level ('## ') heading. Its span
#                      identifies COARSE membership: a DONE block sitting
#                      anywhere inside it, but not already tagged this
#                      track's bucket, is inferred to belong here (catches
#                      a forgotten retag).
#   'done_header'   -- the track's own physical closed-items subheading
#                      (e.g. '### W.Done -- ...'). Its span is the EXACT
#                      destination: a block already tagged this bucket, or
#                      one just inferred into it, must physically live
#                      here, and gets moved if it doesn't.
# Add an entry here if another track ever grows its own closed bucket.
TRACK_DONE_BUCKETS = {
    'W.Done': {
        'track_header': '## W. WEB PUBLICATION TRACK',
        'done_header': '### W.Done -- closed items, kept with the track',
    },
    'O.Done': {
        'track_header': '## O. OBJECT CANDIDATES TRACK',
        'done_header': '### O.Done -- closed items, kept with the track',
    },
}

# Section tags that count as CLOSED for status/section consistency
# purposes: the general archive plus every track's own closed bucket.
CLOSED_SECTIONS = {'C'} | set(TRACK_DONE_BUCKETS)


def parse_rice(rice_str):
    """Parse a rice:R/I/C/E string into (reach, impact, confidence, effort) or None.

    Returns a tuple of floats if all four components are present and valid,
    or None if the field is missing, '-', or malformed.
    Separator is '/' to allow decimal values (e.g., rice:3/2/80/0.5).
    """
    if not rice_str or rice_str == '-':
        return None
    parts = rice_str.split('/')
    if len(parts) != 4:
        return None
    try:
        r, i, c, e = float(parts[0]), float(parts[1]), float(parts[2]), float(parts[3])
        if e <= 0:
            return None  # division by zero guard
        return (r, i, c, e)
    except ValueError:
        return None


def compute_score(rice_tuple):
    """Compute RICE score: R x I x (C / 100) / E.  Returns float or None."""
    if rice_tuple is None:
        return None
    r, i, c, e = rice_tuple
    return r * i * (c / 100.0) / e


def fmt_score(score):
    """Format a RICE score for the index table."""
    if score is None:
        return '--'
    return f'{score:.1f}'


def parse_blocks(lines):
    """Return list of dicts (one per L-block) and a list of parse problems."""
    blocks, problems = [], []
    for i, line in enumerate(lines):
        m = HEAD_RE.match(line)
        if not m:
            continue
        lnum, alias, title = m.group(1), m.group(2), m.group(3).strip()
        meta = META_RE.match(lines[i + 1]) if i + 1 < len(lines) else None
        if not meta:
            problems.append(f"L-{lnum} ('{title}'): missing/malformed metadata line below the header")
            continue
        if meta.group(1) != lnum:
            problems.append(f"L-{lnum}: metadata L:{meta.group(1)} disagrees with header L-{lnum}")
        blocks.append({
            'L': lnum, 'alias': alias, 'title': title,
            'status': meta.group(2), 'upd': meta.group(3),
            'section': meta.group(4), 'flag': (meta.group(5) or '').strip(),
            'rice': parse_rice((meta.group(6) or '').strip()),
            'line': i,  # line index of the #### header
        })
    return blocks, problems


def find_span(lines, start_prefix, closing_re):
    """
    Find the physical span of a heading starting with start_prefix: from
    that line to the index of the first SUBSEQUENT line matching
    closing_re (exclusive), or end of file. Returns (start_idx, end_idx),
    or (None, None) if start_prefix isn't found.

    This is deliberately coarse: it answers "does this block sit anywhere
    under this ONE named heading", not "which specific sub-subsection".
    Mapping an individual subsection's heading text back to its canonical
    section code (e.g. "### D.Feature -- Bucket A (near-term)" -> tag
    D.Feature-A, or "## PENDING ACTION (Tony-side)" -> tag B) is NOT
    attempted -- several existing headings don't literally contain their
    own tag, so a lookup table doing that would need constant
    hand-maintenance and would misfire silently the moment a heading is
    reworded. A span found this way costs nothing to maintain: it just
    scans for the next line matching closing_re, whatever it's named.
    """
    start_idx = None
    for i, line in enumerate(lines):
        if line.startswith(start_prefix):
            start_idx = i
            break
    if start_idx is None:
        return None, None
    end_idx = len(lines)
    for i in range(start_idx + 1, len(lines)):
        if closing_re.match(lines[i]):
            end_idx = i
            break
    return start_idx, end_idx


# A '## ' heading's span closes only at the next '## ' heading (a nested
# '### ' subsection does not end it). A '### ' subsection's span closes at
# EITHER the next '### ' sibling or the enclosing '## ' heading -- whichever
# comes first.
TOP_LEVEL_CLOSE_RE = re.compile(r'^## ')
SUBSECTION_CLOSE_RE = re.compile(r'^#{2,3} ')


def find_top_level_span(lines, start_prefix):
    return find_span(lines, start_prefix, TOP_LEVEL_CLOSE_RE)


def find_subsection_span(lines, start_prefix):
    return find_span(lines, start_prefix, SUBSECTION_CLOSE_RE)


def find_c_bounds(lines):
    """Return (c_open_idx, d_idx) for the general C archive's physical span."""
    return find_top_level_span(lines, SEC_C_HEADER)


def find_bucket_destination_span(lines, target_tag):
    """
    Return the (start, end) span that is the ACTUAL destination for a
    block whose correct closed bucket is target_tag: the C archive's own
    span for 'C', or a track's own 'done_header' subsection span for a
    TRACK_DONE_BUCKETS entry. Returns (None, None) if target_tag isn't
    recognized or its heading isn't found (callers must handle that --
    no destination is assumed if a heading is missing or renamed).
    """
    if target_tag == 'C':
        return find_c_bounds(lines)
    cfg = TRACK_DONE_BUCKETS.get(target_tag)
    if cfg is None:
        return None, None
    return find_subsection_span(lines, cfg['done_header'])


def find_closed_bucket_issues(blocks, lines):
    """
    Single source of truth for every closed-bucket problem -- consumed by
    BOTH check() (report) and reconcile_closed_buckets() (fix), so the two
    can never quietly disagree about what needs doing.

    Returns a list of dicts: {'L', 'kind', 'detail', ['target_tag']}.

    For a DONE item there is ALWAYS exactly one correct closed bucket, and
    which one it is follows a clear priority:
      1. If the block is ALREADY tagged one of the recognized closed
         buckets (a TRACK_DONE_BUCKETS entry, e.g. 'W.Done'), that tag IS
         the membership signal and is TRUSTED -- a human tagged it that
         way deliberately, so the tool never second-guesses the tag
         itself. All that's checked is whether it physically lives in
         that bucket's own destination heading; if not, it gets MOVED
         there (the tag is right, the position was wrong).
      2. Otherwise (tagged 'C', a live bucket, or anything that isn't a
         recognized closed bucket), membership is INFERRED from physical
         position: a block sitting anywhere inside a track's own
         top-level span belongs to that track's bucket (catches a
         forgotten retag); everything else belongs to the general 'C'
         archive. If the current tag doesn't match, it gets RETAGGED
         (the position is right, the tag was wrong).
    Either path ends the same way: correct tag AND physically inside that
    bucket's own destination span. A block can need both fixes in one
    pass (retagged AND moved).

    kind values and what happens to each:
      'retag_closed' -- inferred membership (path 2) disagrees with the
          current tag. AUTO-FIXED: metadata retag in place (dict carries
          'target_tag').
      'move_to_bucket' -- whatever the (possibly just-retagged) target
          bucket is, the block is not physically inside that bucket's own
          destination span. AUTO-FIXED: physically moved there (dict
          carries 'target_tag' naming the destination).
      'live_in_closed' -- status is NOT DONE, but the tag is a closed
          bucket -- the dangerous direction (live work hidden from the
          live count). NOT auto-fixed: with many legitimate live buckets
          and no positional signal narrowing it to one, there's no
          mechanical answer for where it should go.
      'unknown_tag' -- section tag isn't recognized at all (probably a
          typo). NOT auto-fixed: the tool can't guess what was meant.
    """
    issues = []
    track_spans = {tag: find_top_level_span(lines, cfg['track_header'])
                   for tag, cfg in TRACK_DONE_BUCKETS.items()}

    def in_span(line_idx, span):
        s, e = span
        return s is not None and e is not None and s < line_idx < e

    for b in blocks:
        sec = SECTION_ALIASES.get(b['section'], b['section'])

        if sec not in KNOWN_SECTIONS:
            issues.append({'L': b['L'], 'kind': 'unknown_tag',
                            'detail': f"unrecognized section tag '{b['section']}' -- check for "
                                      f"a typo; it will silently sort to the end of the index otherwise"})
            continue  # nothing else to check sensibly against an unrecognized tag

        is_closed_status = b['status'] in CLOSED_STATUSES
        is_closed_section = sec in CLOSED_SECTIONS

        if not is_closed_status and is_closed_section:
            issues.append({'L': b['L'], 'kind': 'live_in_closed',
                            'detail': f"status {b['status']} (live) but section '{b['section']}' is "
                                      f"a closed bucket -- this hides live work from the live-item "
                                      f"count; likely lost from the active backlog"})
            continue

        if not is_closed_status:
            continue  # live item, correctly not in a closed bucket -- nothing to check

        # status is DONE from here on.
        if sec in TRACK_DONE_BUCKETS:
            # Already tagged a track's own bucket -- TRUST the tag for
            # membership; only physical placement gets checked below.
            target = sec
        else:
            # Not already tagged a recognized closed bucket -- infer
            # membership from physical position (catches a forgotten
            # retag, e.g. still tagged 'C' or a live bucket while sitting
            # inside a track's own physical area).
            owning_track = next((tag for tag, span in track_spans.items() if in_span(b['line'], span)), None)
            target = owning_track if owning_track is not None else 'C'
            if sec != target:
                where = (f"physically inside the span belonging to closed bucket '{target}'" if owning_track
                         else "not physically inside any track's own span, so the general archive")
                issues.append({'L': b['L'], 'kind': 'retag_closed', 'target_tag': target,
                                'detail': f"status DONE, tagged '{b['section']}', but {where} -- "
                                          f"correct tag is '{target}'"})

        dest_span = find_bucket_destination_span(lines, target)
        if not in_span(b['line'], dest_span):
            issues.append({'L': b['L'], 'kind': 'move_to_bucket', 'target_tag': target,
                            'detail': f"belongs in closed bucket '{target}' but is not physically "
                                      f"located in its destination heading"})

    return issues


ISSUE_TAGS = {
    'retag_closed': '[auto-fix]',
    'move_to_bucket': '[auto-fix]',
    'live_in_closed': '[needs review]',
    'unknown_tag': '',
}


def check(blocks, problems, lines=None):
    """
    Structural + status/section consistency checks. `lines` is optional
    (needed only for the physical-placement checks); omit it to skip
    those, e.g. when the file text isn't available.
    """
    seen = {}
    for b in blocks:
        seen.setdefault(b['L'], []).append(b['title'])
    for lnum, titles in sorted(seen.items()):
        if len(titles) > 1:
            problems.append(f"L-{lnum}: duplicate handle used by {len(titles)} blocks: {titles}")

    if lines is not None:
        for issue in find_closed_bucket_issues(blocks, lines):
            tag = ISSUE_TAGS[issue['kind']]
            prefix = f"{tag} " if tag else ""
            problems.append(f"{prefix}L-{issue['L']}: {issue['detail']}")

    return problems


def cell(s):
    """Make a string safe for a markdown table cell (escape the pipe)."""
    return s.replace('|', r'\|')


def fmt_disposition(b):
    s = b['status']
    return f"{s} [{b['flag']}]" if b['flag'] else s


def fmt_id(b):
    # ASCII, and pipe-free so it cannot break the table column count.
    return f"L-{b['L']} (#{b['alias']})" if b['alias'] else f"L-{b['L']}"


def build_index(blocks):
    # Group ALL blocks (including section C) by their canonical section,
    # normalizing tag aliases (e.g. PENDING -> B).
    by_section = {}
    for b in blocks:
        sec = SECTION_ALIASES.get(b['section'], b['section'])
        by_section.setdefault(sec, []).append(b)

    def sec_key(s):
        return (SECTION_ORDER.index(s) if s in SECTION_ORDER else len(SECTION_ORDER), s)

    # Summary counts are for the LIVE backlog (everything except every
    # recognized closed bucket -- section C and any TRACK_DONE_BUCKETS
    # entry, e.g. W.Done. A bare "!= 'C'" check here would silently count
    # W.Done items as live, which is what happened before this existed.
    open_blocks = [b for b in blocks
                   if SECTION_ALIASES.get(b['section'], b['section']) not in CLOSED_SECTIONS]
    closed_n = len(blocks) - len(open_blocks)

    out = [START, '', '## INDEX (generated -- status board; edit DETAIL blocks, then re-run ledger_index.py)', '']
    total = len(open_blocks)
    gaps = sum(1 for b in open_blocks if b['status'] in GAP_STATUS)
    scored = sum(1 for b in open_blocks if compute_score(b['rice']) is not None)
    out.append(f"*{total} live items; {gaps} need attention (`!`); {scored} RICE-scored; "
               f"{closed_n} closed (section C + {'/'.join(sorted(TRACK_DONE_BUCKETS))}). "
               "Find an `L-0NN` handle (Ctrl+F in VS Code) "
               "to jump to any item; search `| ! |` to list every gap. See \"Using and maintaining this "
               "ledger\" above for details.*")
    out.append('')

    # Display every section that has items, plus any always-show section.
    display_secs = set(by_section) | ALWAYS_SHOW
    for sec in sorted(display_secs, key=sec_key):
        out.append(f"### {SECTION_TITLES.get(sec, sec)}")
        rows = by_section.get(sec, [])
        if not rows:
            out.append('')
            out.append('*(none currently)*')
            out.append('')
            continue
        # Sort: scored items first (by score descending), then unscored (by L-number)
        def sort_key(b):
            s = compute_score(b['rice'])
            if s is not None:
                return (0, -s, int(b['L']))  # scored first, highest score first
            return (1, 0, int(b['L']))       # unscored after, by L-number
        rows = sorted(rows, key=sort_key)
        out.append('| Gap | L# | Item | Disposition | Score | Updated |')
        out.append('|:---:|----|------|-------------|:-----:|---------|')
        for b in rows:
            gap = '!' if b['status'] in GAP_STATUS else ''
            score = fmt_score(compute_score(b['rice']))
            out.append(f"| {gap} | {cell(fmt_id(b))} | {cell(b['title'])} | "
                       f"{cell(fmt_disposition(b))} | {score} | {b['upd']} |")
        out.append('')
    out.append(END)
    return '\n'.join(out)


def extract_block_text(lines, start_line):
    """
    Extract the full text of one L-block starting at start_line (the #### header).
    A block ends just before the next #### header at the same or higher level,
    or at a ## section header, or end of file.
    Returns the block text (with trailing newline stripped) and the
    exclusive end line index.
    """
    end = start_line + 1
    while end < len(lines):
        # Stop at any new #### L-block header or any ## section header
        if HEAD_RE.match(lines[end]):
            break
        if re.match(r'^#{1,3}\s', lines[end]):
            break
        end += 1
    # Trim trailing blank lines from the block body
    while end > start_line + 1 and lines[end - 1].strip() == '':
        end -= 1
    return '\n'.join(lines[start_line:end]), end


def reconcile_closed_buckets(text, blocks, lines):
    """
    Apply every AUTO-FIXABLE issue from find_closed_bucket_issues -- the
    same list check() reports from, so fixing and reporting can never
    quietly disagree:

      - 'retag_closed': rewrite the metadata section tag in place
        (no line removal -- line count is unchanged, so this always runs
        first and safely, before any physical moves).
      - 'move_to_bucket': physically relocate the block to the END of its
        target bucket's own destination span (the general C archive's
        span for 'C', or a track's 'done_header' subsection span for a
        TRACK_DONE_BUCKETS entry). Blocks are grouped by destination and
        each group is inserted together, in L-number order.

    'live_in_closed' and 'unknown_tag' are never touched here -- deciding
    the correct bucket for those is a judgment call, not a mechanical fact
    (see the module docstring).

    Returns (new_text, retag_count, move_count).
    """
    issues = find_closed_bucket_issues(blocks, lines)
    retags = {i['L']: i['target_tag'] for i in issues if i['kind'] == 'retag_closed'}
    movers = {i['L']: i['target_tag'] for i in issues if i['kind'] == 'move_to_bucket'}

    # --- Pass A: retag in place. Metadata-only; line count is unchanged,
    # so this is safe to do before any line-index work for Pass B. ---
    retag_count = 0
    for lnum, target_tag in retags.items():
        pattern = re.compile(r'(<!--\s*L:' + re.escape(lnum) + r'\s+status:\S+\s+upd:\S+\s+section:)\S+')
        new_text, n = pattern.subn(r'\g<1>' + target_tag, text, count=1)
        if n:
            text = new_text
            retag_count += 1

    if not movers:
        return text, retag_count, 0

    # --- Pass B: physically move blocks, entirely in line-list space. ---
    work_lines = text.split('\n')

    # Pre-validate every target's destination BEFORE removing anything.
    # A block is only ever taken out of its current position once we
    # already know a valid place to put it -- never remove-then-discover-
    # there's-nowhere-to-put-it, which would silently delete the block.
    valid_targets = set()
    for target_tag in set(movers.values()):
        _, dest_end = find_bucket_destination_span(work_lines, target_tag)
        if dest_end is None:
            skipped = sum(1 for t in movers.values() if t == target_tag)
            print(f"WARNING: could not find the destination heading for '{target_tag}'; "
                  f"{skipped} block(s) intended for it were left exactly where they are "
                  f"(any retag from Pass A above still applies -- only the move is skipped).")
        else:
            valid_targets.add(target_tag)

    movers = {L: t for L, t in movers.items() if t in valid_targets}
    if not movers:
        return '\n'.join(work_lines), retag_count, 0

    blocks2, _ = parse_blocks(work_lines)
    move_candidates = sorted([b for b in blocks2 if b['L'] in movers],
                              key=lambda x: int(x['L']), reverse=True)

    removed_by_target = {}  # target_tag -> [(lnum, block_text), ...]
    for b in move_candidates:
        current_line = None
        for i, line in enumerate(work_lines):
            m = HEAD_RE.match(line)
            if m and m.group(1) == b['L']:
                current_line = i
                break
        if current_line is None:
            continue

        block_text, end_line = extract_block_text(work_lines, current_line)
        target = movers[b['L']]
        removed_by_target.setdefault(target, []).append((int(b['L']), block_text))

        remove_end = end_line
        if remove_end < len(work_lines) and work_lines[remove_end].strip() == '':
            remove_end += 1
        del work_lines[current_line:remove_end]

    move_count = 0
    for target_tag, group in removed_by_target.items():
        group.sort(key=lambda x: x[0])
        # Destination span is re-found fresh against the CURRENT work_lines,
        # so an earlier group's insertion (a different target) is already
        # accounted for. Already pre-validated above, but re-checked here
        # too -- if it somehow vanished mid-move, append at end of file
        # rather than lose the block; it was already safely removed by
        # this point, so "somewhere, visibly" beats "gone silently".
        _, dest_end = find_bucket_destination_span(work_lines, target_tag)
        if dest_end is None:
            print(f"WARNING: destination heading for '{target_tag}' disappeared mid-move; "
                  f"{len(group)} block(s) appended at end of file instead of lost.")
            dest_end = len(work_lines)
        insertion_lines = []
        for _, block_text in group:
            insertion_lines.append('')
            insertion_lines.extend(block_text.split('\n'))
        work_lines[dest_end:dest_end] = insertion_lines
        move_count += len(group)

    text = '\n'.join(work_lines)
    return text, retag_count, move_count


def main():
    # Default: LEDGER_CONSOLIDATED.md in the same folder as this script.
    if len(sys.argv) < 2:
        default = pathlib.Path(__file__).parent / 'LEDGER_CONSOLIDATED.md'
        if default.exists():
            path = str(default)
            check_only = False
        else:
            print(__doc__)
            sys.exit(2)
    else:
        path = sys.argv[1]
        check_only = '--check' in sys.argv[2:]

    with open(path, encoding='utf-8') as f:
        text = f.read()
    lines = text.split('\n')

    blocks, problems = parse_blocks(lines)
    problems = check(blocks, problems, lines)

    if problems:
        print("CONSISTENCY PROBLEMS:")
        for p in problems:
            print(f"  - {p}")
    else:
        print(f"OK: {len(blocks)} L-blocks parsed, no consistency problems.")

    if check_only:
        sys.exit(1 if problems else 0)

    # Pass 1: reconcile closed-bucket issues (retag-in-place + physical move)
    text, retagged, moved = reconcile_closed_buckets(text, blocks, lines)
    if retagged or moved:
        parts = []
        if retagged:
            parts.append(f"retagged {retagged} block(s) to their correct closed bucket")
        if moved:
            parts.append(f"physically moved {moved} block(s) into their bucket's destination heading")
        msg = "; ".join(parts)
        print(msg[0].upper() + msg[1:] + ".")
        # Re-parse after reconciliation so the index reflects updated state
        lines = text.split('\n')
        blocks, _ = parse_blocks(lines)

    # Pass 2: regenerate the index
    index = build_index(blocks)
    if START in text and END in text:
        new = re.sub(re.escape(START) + r'.*?' + re.escape(END), index, text, flags=re.DOTALL)
    else:
        sep = text.find('\n---\n')
        cut = sep + len('\n---\n') if sep != -1 else len(text)
        new = text[:cut] + '\n' + index + '\n' + text[cut:]

    with open(path, 'w', encoding='utf-8') as f:
        f.write(new)

    # Final problem count reflects post-migration state (auto-fixed placement
    # problems should not still count against the exit code).
    final_problems = check(blocks, [], lines)
    if final_problems and not problems:
        # (shouldn't happen -- migration/reindex introduced a new problem)
        print("CONSISTENCY PROBLEMS (post-migration):")
        for p in final_problems:
            print(f"  - {p}")

    live_count = sum(1 for b in blocks
                     if SECTION_ALIASES.get(b['section'], b['section']) not in CLOSED_SECTIONS)
    print(f"Index regenerated ({live_count} live items) in {path}.")
    sys.exit(1 if final_problems else 0)


if __name__ == '__main__':
    main()
