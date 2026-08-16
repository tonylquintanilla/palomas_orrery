"""Round trip: every annotated site mints a key that resolves back.

Domain: dev_tools

The one-time measurement -- 53 distinct annotated sites, 53 distinct
keys, zero collisions -- was run twice by hand, once with a regex and
once with an AST, by two models. That is a fact about one afternoon.
This makes it a fact the tools assert on every run.

It is a check that CAN fail, which is the point. A rename breaks it. A
split implementation between the builder and the checker breaks it. A
change to the enclosing-name rule breaks it. All three break it
loudly, at the commit that introduced them, rather than months later
when a returned worksheet will not bind.

Run: python test_worksheet_keys.py
"""

import os
import sys

import worksheet_keys as wk

# These are ACTIVE data, not archive. documentation/ holds session
# records that are finished when they are written; these two are read
# on every run and edited when the corpus changes, so they sit with
# the worksheets they describe. The checker's loader takes only .md
# from that directory, so a .txt here is invisible to it -- no phantom
# uncited worksheet, no unreadable-worksheet finding.
SITES_DOC = os.path.join('documentation', 'worksheets',
                         'L192_annotated_sites.txt')
PINS_DOC = os.path.join('documentation', 'worksheets',
                        'L192_key_pins.txt')


def load_sources(project_dir, modules):
    sources = {}
    for name in modules:
        path = os.path.join(project_dir, name)
        if os.path.exists(path):
            with open(path, encoding='utf-8') as handle:
                sources[name] = handle.read()
    return sources


def check_round_trip(sites, sources):
    """(minted, failures, collisions) for a list of (module, line, label)."""
    minted = {}
    failures = []
    collisions = []
    for module, line, label in sites:
        source = sources.get(module)
        if source is None:
            failures.append((module, line, 'no source for %s' % module))
            continue
        key = wk.key_for_site(module, source, line, label=label)
        if key in minted and minted[key] != (module, line):
            collisions.append((key, minted[key], (module, line)))
        minted[key] = (module, line)
        resolved, reason = wk.resolve(key, sources)
        if resolved is None:
            failures.append((module, line, reason))
    return minted, failures, collisions


def check_pins(pins, sources, aliases=None):
    """Resolve keys recorded EARLIER against the code as it is now.

    This is the half the round trip cannot do. Minting a key from
    today's source and resolving it against today's source agrees with
    itself no matter what the source says -- rename a function and the
    freshly minted key simply carries the new name. Only a key written
    down before the rename can notice one.

    Measured: renaming create_pluto_core_shell in a throwaway copy left
    the round trip reporting 53 of 53 resolved. The pins caught it.
    """
    failures = []
    for key in pins:
        resolved, reason = wk.resolve(key, sources, aliases)
        if resolved is None:
            failures.append((key, reason))
    return failures


RETIRED_TAG = wk.RETIRED_TAG


def parse_pins(path):
    """(live, retired) pins. A retired pin INVERTS the assertion.

    A key can leave the corpus two ways and they are not the same
    event. A RENAME is an accident and must fail loudly. A RETIREMENT
    is a decision and must be recorded -- deleting the line loses why
    the key vanished, and an inert '# RETIRED' comment records it
    while checking nothing, which is a check that cannot fail.

    So a retired pin asserts the opposite of a live one: this key must
    NOT resolve. If it resolves again, either the constant came back
    or the retirement record is wrong, and both deserve a red run.

    Format, tab-separated:  RETIRED  <date>  <handle>  <key>
    """
    live = []
    retired = []
    with open(path, encoding='utf-8') as handle:
        for raw in handle:
            raw = raw.strip()
            if not raw or raw.startswith('#'):
                continue
            if raw.startswith(RETIRED_TAG + '\t'):
                parts = raw.split('\t')
                if len(parts) < 4:
                    retired.append(('<malformed>', raw, ''))
                    continue
                retired.append((parts[3], parts[1], parts[2]))
                continue
            live.append(raw)
    return live, retired


def check_retired_pins(retired, sources):
    """A retired key that still resolves is a failure."""
    failures = []
    for key, when, handle in retired:
        if key == '<malformed>':
            failures.append((when, 'malformed RETIRED line -- want '
                                   'RETIRED<tab>date<tab>handle<tab>key'))
            continue
        resolved, _ = wk.resolve(key, sources)
        if resolved is not None:
            failures.append((key, 'recorded RETIRED %s (%s) but it resolves '
                                  'again at line %s' % (when, handle,
                                                        resolved)))
    return failures


parse_sites = wk.parse_sites_doc


def unit_tests():
    """The behaviours the round trip cannot show."""
    failures = []

    def expect(name, got, want):
        if got != want:
            failures.append('%s: got %r, want %r' % (name, got, want))

    expect('compose with ordinal',
           wk.compose('a_shells.py', 'create_x_shell', 'description', 1),
           'a_shells.py::create_x_shell::description::c1')
    expect('compose drops repeated label',
           wk.compose('a_shells.py', 'x_info', 'x_info', 1),
           'a_shells.py::x_info::c1')
    expect('compose constant',
           wk.compose('constants_new.py', 'FOO_KM'),
           'constants_new.py::FOO_KM')

    parsed = wk.parse('a_shells.py::create_x_shell::description::c2')
    expect('parse ordinal', parsed.ordinal, 2)
    expect('parse enclosing', parsed.enclosing, 'create_x_shell')
    expect('parse label defaults to enclosing',
           wk.parse('a_shells.py::x_info::c1').label, 'x_info')

    for bad in ['', 'no_separator', 'notamodule::x', 'a.py::b::c::d::c1']:
        try:
            wk.parse(bad)
            failures.append('parse accepted malformed key %r' % bad)
        except wk.KeyError_:
            pass

    # A key that names nothing must say so, not fall through.
    resolved, reason = wk.resolve('gone.py::create_x_shell::c1', {})
    if resolved is not None or 'KEY_STALE' not in reason:
        failures.append('missing module did not report KEY_STALE: %r' % reason)

    src = 'def create_x_shell():\n    d = {"description": "1,700 km"}\n'
    resolved, reason = wk.resolve('m.py::create_y_shell::c1', {'m.py': src})
    if resolved is not None or 'KEY_STALE' not in reason:
        failures.append('missing enclosing did not report KEY_STALE')

    # Aliases: a rename resolves through a hop.
    aliases = {'m.py::create_y_shell::c1': 'm.py::create_x_shell::c1'}
    resolved, reason = wk.resolve('m.py::create_y_shell::c1',
                                  {'m.py': src}, aliases)
    if resolved is None:
        failures.append('alias did not resolve: %r' % reason)

    # Two hops: a site renamed twice needs only the new hop appended.
    chain = {'m.py::a::c1': 'm.py::b::c1',
             'm.py::b::c1': 'm.py::create_x_shell::c1'}
    resolved, reason = wk.resolve('m.py::a::c1', {'m.py': src}, chain)
    if resolved is None:
        failures.append('alias chain did not resolve: %r' % reason)

    # A cycle is its own finding.
    cycle = {'a.py::x': 'a.py::y', 'a.py::y': 'a.py::x'}
    resolved, reason = wk.resolve('a.py::x', {'a.py': src}, cycle)
    if 'ALIAS_CYCLE' not in reason:
        failures.append('alias cycle not reported: %r' % reason)

    # A broken alias is ALIAS_STALE, never KEY_STALE. The two route
    # different errands: one asks whether a rename happened, the other
    # says someone already answered that and answered it wrong.
    broken = {'m.py::create_y_shell::c1': 'm.py::create_gone_shell::c1'}
    resolved, reason = wk.resolve('m.py::create_y_shell::c1',
                                  {'m.py': src}, broken)
    if resolved is not None or 'ALIAS_STALE' not in reason:
        failures.append('broken alias did not report ALIAS_STALE: %r' % reason)
    if 'KEY_STALE' in reason:
        failures.append('broken alias reported KEY_STALE, masking the cause')

    # An unaliased miss stays KEY_STALE.
    resolved, reason = wk.resolve('m.py::create_gone_shell::c1',
                                  {'m.py': src}, {})
    if 'KEY_STALE' not in reason:
        failures.append('unaliased miss did not report KEY_STALE: %r' % reason)

    # The installed map is the default, and its absence is announced.
    if wk.ALIAS_STORE_MISSING:
        failures.append('worksheet_key_aliases.py did not import')

    # Shift detection runs before any value comparison.
    expect('count change fires', wk.shift_check(3, 'km', 4, 'km') is None, False)
    expect('unit change fires', wk.shift_check(3, 'km', 3, 'K') is None, False)
    expect('unchanged passes', wk.shift_check(3, 'km', 3, 'km'), None)
    expect('unit case insensitive', wk.shift_check(3, 'KM', 3, 'km'), None)
    expect('no recorded count is not a pass by default',
           wk.shift_check(None, 'km', 9, 'K') is None, False)

    return failures


def main():
    project_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_dir)

    print('=' * 70)
    print('WORKSHEET KEY ROUND TRIP (L-192)')
    print('=' * 70)

    failures = unit_tests()
    print('  Unit checks: %d failure(s)' % len(failures))
    for line in failures:
        print('    %s' % line)

    sites_path = os.path.join(project_dir, SITES_DOC)
    if not os.path.exists(sites_path):
        print('  ROUND TRIP DID NOT RUN: %s is missing.' % SITES_DOC)
        print('  A missing site list is a failure, not a pass -- the whole')
        print('  point of this test is the corpus.')
        return 1

    sites = parse_sites(sites_path)
    modules = sorted(set(site[0] for site in sites))
    sources = load_sources(project_dir, modules)

    missing = [m for m in modules if m not in sources]
    minted, rt_failures, collisions = check_round_trip(sites, sources)

    print('  Sites read:        %d' % len(sites))
    print('  Modules read:      %d of %d' % (len(sources), len(modules)))
    print('  Distinct keys:     %d' % len(minted))
    print('  Unresolved:        %d' % len(rt_failures))
    print('  Key collisions:    %d' % len(collisions))
    for module, line, reason in rt_failures:
        print('    %s:%d  %s' % (module, line, reason))
    for key, first, second in collisions:
        print('    COLLISION %s  %s and %s' % (key, first, second))
    for name in missing:
        print('    UNREADABLE %s -- counted as a failure, not skipped' % name)

    pins_path = os.path.join(project_dir, PINS_DOC)
    if not os.path.exists(pins_path):
        print('  PINS DID NOT RUN: %s is missing.' % PINS_DOC)
        print('  Counted as a failure. A round trip with no pinned keys')
        print('  agrees with itself and cannot detect a rename.')
        pin_failures = [('<no pin file>', PINS_DOC)]
        pins = []
        retired = []
    else:
        pins, retired = parse_pins(pins_path)
        # aliases=None on purpose: the pins resolve through the map
        # installed beside the checker, which is the only way a
        # repaired rename shows up as repaired.
        pin_failures = check_pins(pins, sources, aliases=None)
        pin_failures += check_retired_pins(retired, sources)
        print('  Aliases installed: %d' % len(wk.INSTALLED_ALIASES))
        print('  Pinned keys:       %d live, %d retired'
              % (len(pins), len(retired)))
        print('  Pins unresolved:   %d' % len(pin_failures))
        for key, reason in pin_failures:
            print('    %s  %s' % (key, reason))

    total = (len(failures) + len(rt_failures) + len(collisions)
             + len(missing) + len(pin_failures))
    if total:
        print('  RESULT: %d failure(s)' % total)
        print('=' * 70)
        return 1

    print('  RESULT: %d sites minted %d distinct keys, all resolved; '
          '%d pinned keys still resolve; %d retired keys confirmed gone.'
          % (len(sites), len(minted), len(pins), len(retired)))
    print('=' * 70)
    return 0


if __name__ == '__main__':
    sys.exit(main())
