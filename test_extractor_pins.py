"""The instruction filter keeps and drops what it kept and dropped.

Domain: dev_tools

Module updated: September 3, 2026 with Anthropic's Claude Fable 5.1
(L-277: the site store anchors by enclosing name and lives at the repo
root; measure() finds each string site by name through the checker's
own anchor map, and a site it cannot find fails the run).

Tony froze INSTRUCTION_LOOKBACK at 30 and INSTRUCTION_LOOKAHEAD at 25
on 2026-08-14, after a grid measurement showed the drop set unchanged
across lookback 25 through 60 at every lookahead tested. Current sits
mid-plateau.

The freeze matters because the claim ordinal in every issued key --
the `::c2` -- counts claims AFTER this filter runs. Extend the
instruction pattern by one phrase and a formerly-dropped number joins
the sequence, shifting every ordinal after it with no prose edit at
all. A worksheet returned against the old ordinals then binds to the
wrong claim.

This is a check that CAN fail, which is the point. Retuning either
constant fails it. Editing either regex fails it. A prose edit that
adds or removes a number fails it, at the site that changed. A rename
that the alias store has not recorded fails it.

What it does NOT do is decide whether a change is wrong. It reports
that the extractor no longer means what the issued keys assume, and
prints the replacement pin file so re-pinning is a paste rather than a
regeneration.

Run: python test_extractor_pins.py

Module created: August 2026 with Anthropic's Claude Opus 5 (L-192).
"""

import os
import sys

import provenance_scanner as ps
import worksheet_checker as wc
import worksheet_keys as wk

# ACTIVE data, read on every run, and it lives at the repo ROOT
# (L-277, Tony's ruling 2026-09-03): a live store under documentation/
# was lost among hundreds of archived files and invisible to
# doc_index.py, which scans only the root. Each carries a Doc-Kind tag
# so README.md's key-documents table lists it.
SITES_DOC = 'L192_annotated_sites.txt'
PINS_DOC = 'L192_extractor_pins.txt'

SEP = '|'

# The header fields, in file order. Each is asserted literally against
# the live value; together they are the extractor's definition.
HEADER_FIELDS = ('EXTRACTOR_VERSION', 'INSTRUCTION_LOOKBACK',
                 'INSTRUCTION_LOOKAHEAD', 'NUMERIC_CLAIM_RE',
                 'DISPLAY_INSTRUCTION_RE')


def live_header():
    """The extractor's definition as it stands right now."""
    return {
        'EXTRACTOR_VERSION': str(wk.EXTRACTOR_VERSION),
        'INSTRUCTION_LOOKBACK': str(wc.INSTRUCTION_LOOKBACK),
        'INSTRUCTION_LOOKAHEAD': str(wc.INSTRUCTION_LOOKAHEAD),
        'NUMERIC_CLAIM_RE': ps.NUMERIC_CLAIM_RE.pattern.replace('\n', ''),
        'DISPLAY_INSTRUCTION_RE':
            wc.DISPLAY_INSTRUCTION_RE.pattern.replace('\n', ''),
    }


parse_sites = wk.parse_sites_doc


def parse_pins(path):
    """(header, {key: (kept_raws, dropped_count)}) from the pin file."""
    header = {}
    rows = {}
    with open(path, encoding='utf-8') as handle:
        for raw in handle:
            if raw.startswith('#') or not raw.strip():
                continue
            parts = raw.rstrip('\n').split('\t')
            if parts[0] in HEADER_FIELDS:
                header[parts[0]] = parts[1] if len(parts) > 1 else ''
                continue
            if len(parts) >= 3:
                kept = [v for v in parts[1].split(SEP) if v]
                rows[parts[0]] = (kept, int(parts[2]))
    return header, rows


def dealias(key, aliases, seen=None):
    """Follow a recorded rename to the key in force today.

    worksheet_keys.resolve owns the full semantics, including the
    ALIAS_STALE / KEY_STALE split. Only the hop is needed here: this
    test asks what a site CONTAINS, and the key test already asks
    whether the site is still findable.
    """
    seen = seen or []
    while key in aliases:
        if key in seen:
            return key
        seen.append(key)
        key = aliases[key]
    return key


def measure(sites):
    """({key: (kept_raws, dropped)}, unreadable_modules, lost_sites).

    Claim membership is computed by worksheet_checker.physical_claims,
    never re-implemented here. A second implementation would agree with
    itself and prove nothing.

    Since L-277 a site is found by NAME: locate_site turns the row's
    enclosing and label into the line that introduces the label, and
    the unit is the one the checker's own anchor map ties to that line.
    A site that cannot be found, or that matches more than one string
    unit, is returned in `lost_sites` and fails the run -- never
    skipped, because a skipped site looks exactly like a constant.
    """
    modules = sorted({module for module, _enclosing, _label in sites})
    sources = {}
    units = {}
    anchors = {}
    unreadable = []
    for name in modules:
        if not os.path.exists(name):
            unreadable.append(name)
            continue
        try:
            with open(name, encoding='utf-8') as handle:
                sources[name] = handle.read()
            units[name] = list(ps.extract_units_from_file(name, name[:-3], 'orrery'))
            anchors[name] = ps.entry_anchor_map(ps.ast.parse(sources[name]))
        except (IOError, OSError, SyntaxError, ValueError) as exc:
            unreadable.append('%s (%s)' % (name, exc))

    measured = {}
    lost = []
    aliases = wk.INSTALLED_ALIASES
    for module, enclosing, label in sites:
        if module not in sources:
            continue                   # already reported as unreadable
        stored = wk.compose(module, enclosing, label)
        live = wk.parse(dealias(stored, aliases))
        if live.module not in sources:
            lost.append('%s -- alias points at unread module %s'
                        % (stored, live.module))
            continue
        line, reason = wk.locate_site(sources[live.module], live.enclosing,
                                      live.label)
        if line is None:
            lost.append('%s -- %s' % (stored, reason))
            continue
        amap = anchors[live.module]
        hits = [u for u in units[live.module]
                if getattr(u, 'raw_value', None)
                and (u.line_start == line
                     or amap.get(u.line_start, u.line_start) == line)]
        if not hits:
            continue                   # a constant, not a display string
        if len(hits) > 1:
            lost.append('%s -- %d string units share line %d'
                        % (stored, len(hits), line))
            continue
        kept, dropped = wc.physical_claims(hits[0])
        key = wk.compose(live.module, live.enclosing, live.label)
        measured[key] = ([raw for _value, raw in kept], dropped)
    return measured, unreadable, lost


def repin_text(header, measured):
    """The pin file as it would be written now -- paste, do not retype."""
    lines = [
        '# Doc-Kind: hand | Extractor pins for the L-192 corpus: what the '
        'instruction filter keeps and drops at each display-string site, '
        'frozen by Tony 2026-08-14. Read by test_extractor_pins.py on every '
        'maintenance run; regenerate only from that test\'s REPIN output.',
        '# Extractor pins -- what the instruction filter keeps and drops.',
        '#',
        '# Frozen by Tony 2026-08-14. The claim ordinals in every issued',
        '# key are counted AFTER this filter runs, so a change here',
        '# re-points ordinals corpus-wide with no prose edit at all.',
        '# Read by test_extractor_pins.py on every maintenance run.',
        '#',
        '# Header lines are asserted literally. Row format:',
        '#   key <TAB> kept-claim raws, pipe separated <TAB> dropped count',
        '#',
    ]
    for field in HEADER_FIELDS:
        lines.append('%s\t%s' % (field, header[field]))
    lines.append('#')
    for key in sorted(measured):
        kept, dropped = measured[key]
        lines.append('%s\t%s\t%d' % (key, SEP.join(kept), dropped))
    return '\n'.join(lines) + '\n'


def main():
    project_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_dir)

    print('=' * 70)
    print('EXTRACTOR PINS')

    failures = []

    sites_path = os.path.join(project_dir, SITES_DOC)
    if not os.path.exists(sites_path):
        print('  DID NOT RUN: %s is missing.' % SITES_DOC)
        print('  Counted as a failure. A pin check with no corpus')
        print('  examines nothing and reports success.')
        print('=' * 70)
        return 1
    sites = parse_sites(sites_path)

    pins_path = os.path.join(project_dir, PINS_DOC)
    if not os.path.exists(pins_path):
        print('  DID NOT RUN: %s is missing.' % PINS_DOC)
        print('  Counted as a failure. Recomputing the filter and')
        print('  comparing it to itself agrees no matter what it says.')
        print('=' * 70)
        return 1

    pinned_header, pinned_rows = parse_pins(pins_path)
    header = live_header()

    # 1. The extractor's definition, asserted field by field.
    missing_fields = [f for f in HEADER_FIELDS if f not in pinned_header]
    for field in missing_fields:
        failures.append('HEADER ABSENT %s -- the pin file predates this '
                        'field and cannot vouch for it' % field)
    for field in HEADER_FIELDS:
        if field in pinned_header and pinned_header[field] != header[field]:
            failures.append(
                'FROZEN VALUE MOVED %s: pinned %r, live %r'
                % (field, pinned_header[field], header[field]))

    # 2. What each site currently carries.
    measured, unreadable, lost = measure(sites)
    for name in unreadable:
        failures.append('UNREADABLE %s -- counted as a failure, not skipped'
                        % name)
    for text in lost:
        failures.append('SITE NOT FOUND %s -- counted as a failure, not '
                        'skipped' % text)

    aliases = wk.INSTALLED_ALIASES
    resolved_pins = {}
    for key, value in pinned_rows.items():
        resolved_pins[dealias(key, aliases)] = (key, value)

    membership_moved = False
    for key in sorted(resolved_pins):
        original, (kept, dropped) = resolved_pins[key]
        via = '' if original == key else ' (via alias from %s)' % original
        if key not in measured:
            failures.append('PIN UNMATCHED %s%s -- no such site today; if a '
                            'rename happened, the alias store records it'
                            % (key, via))
            membership_moved = True
            continue
        now_kept, now_dropped = measured[key]
        if now_kept != kept:
            failures.append('CLAIMS MOVED %s: pinned %d %s, now %d %s'
                            % (key, len(kept), kept, len(now_kept), now_kept))
            membership_moved = True
        elif now_dropped != dropped:
            failures.append('DROPS MOVED %s: pinned %d, now %d'
                            % (key, dropped, now_dropped))
            membership_moved = True
    for key in sorted(measured):
        if key not in resolved_pins:
            failures.append('UNPINNED SITE %s -- in the corpus, absent from '
                            'the pins' % key)
            membership_moved = True

    kept_total = sum(len(k) for k, _d in measured.values())
    drop_total = sum(d for _k, d in measured.values())

    print('  Pin file:          %s' % PINS_DOC)
    print('  Definition fields: %d compared' % len(HEADER_FIELDS))
    print('  LOOKBACK/AHEAD:    %s / %s' % (header['INSTRUCTION_LOOKBACK'],
                                            header['INSTRUCTION_LOOKAHEAD']))
    print('  Extractor version: %s' % header['EXTRACTOR_VERSION'])
    print('  Aliases installed: %d' % len(aliases))
    print('  Corpus rows:       %d' % len(sites))
    print('  String sites:      %d measured, %d pinned'
          % (len(measured), len(pinned_rows)))
    print('  Claims:            %d kept, %d dropped as instructions'
          % (kept_total, drop_total))

    if failures:
        print('  RESULT: %d failure(s)' % len(failures))
        for note in failures:
            print('    %s' % note)
        if membership_moved:
            print()
            print('  If the change is intended, bump EXTRACTOR_VERSION in')
            print('  worksheet_keys.py, re-issue any dispatched ordinals,')
            print('  and replace %s with:' % PINS_DOC)
            print('  --- REPIN BEGINS ---')
            for line in repin_text(header, measured).splitlines():
                print('  %s' % line)
            print('  --- REPIN ENDS ---')
        print('=' * 70)
        return 1

    print('  RESULT: %d string sites carry the pinned %d claims and %d '
          'instruction drops, at LOOKBACK %s / LOOKAHEAD %s, extractor '
          'version %s.'
          % (len(measured), kept_total, drop_total,
             header['INSTRUCTION_LOOKBACK'], header['INSTRUCTION_LOOKAHEAD'],
             header['EXTRACTOR_VERSION']))
    print('=' * 70)
    return 0


if __name__ == '__main__':
    sys.exit(main())
