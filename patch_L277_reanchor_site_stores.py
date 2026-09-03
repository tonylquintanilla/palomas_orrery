"""patch_L277_reanchor_site_stores.py

Ledger handle L-277. Three things in one transaction:

1. The L-192 site store stops anchoring by LINE NUMBER and anchors by
   ENCLOSING NAME (the function or module-level constant a site sits
   in) plus label -- which is what its key already is.
2. The three live L-192 stores move from documentation/worksheets/ to
   the repo ROOT, each with a `# Doc-Kind: hand | ...` tag so
   doc_index.py lists them in README.md's key-documents table.
3. The four Python files that read them are updated, and L-277 and
   L-265 are amended in LEDGER_CONSOLIDATED.md.

Repo:   tonylquintanilla/palomas_orrery (the ORRERY repo)
Run it: save this file in the repo ROOT, open it in VS Code, click Run.
        Command line equivalent:
            python patch_L277_reanchor_site_stores.py
        Nothing to type, no flags.

Built on orrery faac433f138564d1426835b80ed56562a3ccb5c9 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).

FILES MOVED (three)
    documentation/worksheets/L192_annotated_sites.txt  -> L192_annotated_sites.txt  (REWRITTEN, see below)
    documentation/worksheets/L192_extractor_pins.txt   -> L192_extractor_pins.txt   (content unchanged; tag line added)
    documentation/worksheets/L192_key_pins.txt         -> L192_key_pins.txt         (content unchanged; tag line added)

FILES EDITED (five)
    worksheet_keys.py        parse_sites_doc reads module/enclosing/label and
                             REFUSES the old line format; new locate_site();
                             the two label regexes move here from the checker
                             so the site finder and the checker's labeler use
                             one pair (One Value One Home).
    worksheet_checker.py     ASSIGN_NAME_RE / DICT_KEY_RE now imported from
                             worksheet_keys; one path comment.
    test_worksheet_keys.py   new paths; the round trip now (a) composes the
                             key from the row, (b) finds the site by name,
                             (c) re-mints from that line and requires the same
                             key, and (d) compares the minted SET against the
                             pinned set by name. (d) is new and is the check
                             that could not fail before -- see the ledger.
    test_extractor_pins.py   new paths; measure() finds each string site by
                             name and the checker's own anchor map; repin_text
                             writes the Doc-Kind tag so a regeneration keeps it.
    LEDGER_CONSOLIDATED.md   L-277 amended (finding + what this patch did,
                             stays OPEN until the maintenance run is green);
                             L-265 amended (curation delivered).

WHY THE STORE WAS ALREADY WRONG, AND NOTHING SAID SO (found 2026-09-03)
All 23 constants_new.py rows pointed at lines that no longer held the
named constant, left over from the August constants migration. The
round trip stayed green because key_for_site falls back to the label
when no enclosing is found at a stale line, and for a constant the
label IS the key. Three rows (EARTH_POLAR_RADIUS_KM at old line 80,
SPEED_OF_LIGHT_KM_S at 98, BENNU_RADIUS_KM at 367) sat inside OTHER
constants' statements and minted wrong keys -- and the test never
compared minted keys to the pins, so it could not see that. The new
rows were derived from the pinned keys and verified: 52 rows mint
exactly the 52 live pins, none missing, none extra.

HOW IT IS SAFE
- Refuses to run unless all eight source files match the fingerprints
  this was built against (CRLF-normalized), and the three root targets
  do not already exist. If anything is off, NOTHING is written.
- Every text edit anchors on an exact string and asserts one match;
  all edits are planned before the first write.
- After writing it runs py_compile on the four Python files.
- No .bak is written. Undo is Discard Changes in GitHub Desktop (the
  moved files show there as deleted + added).
- Binary mode; each file keeps its own line endings.

AFTER IT RUNS
The maintenance run (orrery_maintenance_run.py) does the rest: it runs
both tests, regenerates the ledger index, and lets doc_index.py write
the three new rows into README.md. Expect README.md to change on that
run; that is the tracker picking the stores up.

Module updated: September 3, 2026 with Anthropic's Claude Fable 5.1.
"""

import hashlib
import os
import py_compile
import sys

WS = os.path.join("documentation", "worksheets")

FINGERPRINTS = {
    "worksheet_keys.py":                          "47316138fdab1f887cad812266409259",
    "worksheet_checker.py":                       "1ffbeec50f720c10efa11fc31bfd6691",
    "test_worksheet_keys.py":                     "101030e05425e6f5a6207f599ded3673",
    "test_extractor_pins.py":                     "980a95fe9db2507d53445fad4ee459e6",
    "LEDGER_CONSOLIDATED.md":                     "8c61f9f083a027608b122c942dd62a89",
    os.path.join(WS, "L192_annotated_sites.txt"): "3c0019993f1ceccb6e27e74caf4e85bf",
    os.path.join(WS, "L192_extractor_pins.txt"):  "836d6dc4e8efba3864bc43da15fb1d11",
    os.path.join(WS, "L192_key_pins.txt"):        "910824423c8a3631440722f46b3befb1",
}
NEW_ROOT = ["L192_annotated_sites.txt", "L192_extractor_pins.txt", "L192_key_pins.txt"]

PINS_TAG = ("# Doc-Kind: hand | Extractor pins for the L-192 corpus: what the "
            "instruction filter keeps and drops at each display-string site, "
            "frozen by Tony 2026-08-14. Read by test_extractor_pins.py on every "
            "maintenance run; regenerate only from that test's REPIN output.\n")
KEYS_TAG = ("# Doc-Kind: hand | Key pins for the L-192 corpus: every worksheet "
            "key minted at 305b269, asserted to still resolve by "
            "test_worksheet_keys.py on every maintenance run. A rename breaks "
            "this loudly; record the alias in worksheet_key_aliases.py, never "
            "regenerate to make it quiet.\n")

SITES_NEW = """\
# Doc-Kind: hand | The L-192 site store: every annotated provenance site the worksheet checker tracks, anchored by module, enclosing function or constant, and label. Read by test_worksheet_keys.py and test_extractor_pins.py on every maintenance run; edit a row when a site is added, renamed or retired.
# module<TAB>enclosing<TAB>label -- every annotated site the L-192 report names.
#
# Generated from WORKSHEET_CHECK.md at 305b269 as module/line/label.
# Reanchored to ENCLOSING NAMES 2026-09-03 (L-277): a comment or
# docstring inserted above a site cannot move it any more, and the key
# a row mints is the row itself -- module::enclosing::label, with the
# label dropped when it repeats the enclosing (a module-level constant
# or string is its own enclosing). A row whose second column is a
# number is the retired format and parse_sites_doc refuses it.
#
# RETIRED rows record why a site left the corpus and are skipped here;
# the pin that gives a retirement teeth lives in L192_key_pins.txt.
#   RETIRED<TAB>date<TAB>handle<TAB>module<TAB>enclosing<TAB>label
RETIRED\t2026-08-16\tL-196\tconstants_new.py\tCHROMOSPHERE_RADII\tCHROMOSPHERE_RADII
constants_new.py\tKM_PER_AU\tKM_PER_AU
constants_new.py\tSUN_RADIUS_KM\tSUN_RADIUS_KM
constants_new.py\tEARTH_EQUATORIAL_RADIUS_KM\tEARTH_EQUATORIAL_RADIUS_KM
constants_new.py\tEARTH_POLAR_RADIUS_KM\tEARTH_POLAR_RADIUS_KM
constants_new.py\tJUPITER_EQUATORIAL_RADIUS_KM\tJUPITER_EQUATORIAL_RADIUS_KM
constants_new.py\tJUPITER_POLAR_RADIUS_KM\tJUPITER_POLAR_RADIUS_KM
constants_new.py\tSPEED_OF_LIGHT_KM_S\tSPEED_OF_LIGHT_KM_S
constants_new.py\tCHROMOSPHERE_PHYSICAL_KM\tCHROMOSPHERE_PHYSICAL_KM
constants_new.py\tINNER_CORONA_RADII\tINNER_CORONA_RADII
constants_new.py\tSTREAMER_BELT_RADII\tSTREAMER_BELT_RADII
constants_new.py\tROCHE_LIMIT_RADII\tROCHE_LIMIT_RADII
constants_new.py\tALFVEN_SURFACE_RADII\tALFVEN_SURFACE_RADII
constants_new.py\tTERMINATION_SHOCK_AU\tTERMINATION_SHOCK_AU
constants_new.py\tHELIOPAUSE_RADII\tHELIOPAUSE_RADII
constants_new.py\tPARKER_CLOSEST_RADII\tPARKER_CLOSEST_RADII
constants_new.py\tMOON_RADIUS_KM\tMOON_RADIUS_KM
constants_new.py\tMARS_RADIUS_KM\tMARS_RADIUS_KM
constants_new.py\tSATURN_RADIUS_KM\tSATURN_RADIUS_KM
constants_new.py\tURANUS_RADIUS_KM\tURANUS_RADIUS_KM
constants_new.py\tNEPTUNE_RADIUS_KM\tNEPTUNE_RADIUS_KM
constants_new.py\tBENNU_RADIUS_KM\tBENNU_RADIUS_KM
constants_new.py\tHAUMEA_RADIUS_KM\tHAUMEA_RADIUS_KM
constants_new.py\tARROKOTH_RADIUS_KM\tARROKOTH_RADIUS_KM
eris_visualization_shells.py\teris_crust_info\teris_crust_info
eris_visualization_shells.py\teris_hill_sphere_info\teris_hill_sphere_info
mars_visualization_shells.py\tmars_upper_atmosphere_info\tmars_upper_atmosphere_info
mars_visualization_shells.py\tmars_magnetosphere_info\tmars_magnetosphere_info
mars_visualization_shells.py\tcreate_mars_magnetosphere_shell\tbow_shock_text
mars_visualization_shells.py\tmars_hill_sphere_info\tmars_hill_sphere_info
mercury_visualization_shells.py\tmercury_outer_core_info\tmercury_outer_core_info
mercury_visualization_shells.py\tmercury_crust_info\tmercury_crust_info
mercury_visualization_shells.py\tmercury_sodium_tail_info\tmercury_sodium_tail_info
mercury_visualization_shells.py\tmercury_magnetosphere_info\tmercury_magnetosphere_info
mercury_visualization_shells.py\tmercury_hill_sphere_info\tmercury_hill_sphere_info
moon_visualization_shells.py\tmoon_mantle_info\tmoon_mantle_info
moon_visualization_shells.py\tmoon_hill_sphere_info\tmoon_hill_sphere_info
pluto_visualization_shells.py\tpluto_core_info\tpluto_core_info
pluto_visualization_shells.py\tcreate_pluto_core_shell\tdescription
pluto_visualization_shells.py\tpluto_mantle_info\tpluto_mantle_info
pluto_visualization_shells.py\tcreate_pluto_mantle_shell\tdescription
pluto_visualization_shells.py\tpluto_crust_info\tpluto_crust_info
pluto_visualization_shells.py\tpluto_haze_layer_info\tpluto_haze_layer_info
pluto_visualization_shells.py\tcreate_pluto_haze_layer_shell\tdescription
pluto_visualization_shells.py\tcreate_pluto_atmosphere_shell\tdescription
pluto_visualization_shells.py\tpluto_hill_sphere_info\tpluto_hill_sphere_info
pluto_visualization_shells.py\tcreate_pluto_hill_sphere_shell\tdescription
venus_visualization_shells.py\tvenus_core_info\tvenus_core_info
venus_visualization_shells.py\tcreate_venus_core_shell\tdescription
venus_visualization_shells.py\tvenus_atmosphere_info\tvenus_atmosphere_info
venus_visualization_shells.py\tcreate_venus_upper_atmosphere_shell\tdescription
venus_visualization_shells.py\tvenus_magnetosphere_info\tvenus_magnetosphere_info
venus_visualization_shells.py\tvenus_hill_sphere_info\tvenus_hill_sphere_info
__ROWS__"""

# ---------------------------------------------------------------- edits
# Each entry: (file, [(old, new), ...]) -- exact text, LF line endings;
# converted to the file's own convention at apply time.

WK_REGEX_OLD = "Key = namedtuple('Key', 'module enclosing label ordinal')\n"
WK_REGEX_NEW = WK_REGEX_OLD + """
# The line that INTRODUCES a unit: a dict key or an assignment name.
# One home since L-277: worksheet_checker.anchor_label labels a unit
# with these, and locate_site below finds a site by the same two, so
# a site found by name is the site the checker would label.
ASSIGN_NAME_RE = re.compile(r"^\\s*([A-Za-z_][A-Za-z_0-9]*)\\s*[:=]")
DICT_KEY_RE = re.compile(r"^\\s*['\\"]([^'\\"]+)['\\"]\\s*:")
"""

WK_PARSE_OLD = '''def parse_sites_doc(path):
    """[(module, line, label)] from documentation/worksheets/L192_annotated_sites.txt.

    One parser, because the format has more than one consumer. Both
    test_worksheet_keys.py and test_extractor_pins.py read this file,
    and each carried its own copy of this loop until a RETIRED row was
    added for a deliberately retired key: the copy that had learned the
    tag passed, the copy that had not crashed on int('2026-08-16').
    Fixing the consumer that broke would have left the same landmine
    for the third consumer. (2026-08-16)

    A RETIRED row records why a site left the corpus and is skipped
    here. The inverted assertion that gives it teeth lives with the
    pins, in test_worksheet_keys.py -- this loader only has to not
    choke on it.
    """
    sites = []
    with open(path, encoding='utf-8') as handle:
        for raw in handle:
            raw = raw.rstrip('\\n')
            if not raw.strip() or raw.startswith('#'):
                continue
            if raw.startswith(RETIRED_TAG + '\\t'):
                continue
            parts = raw.split('\\t')
            if len(parts) >= 3:
                sites.append((parts[0], int(parts[1]), parts[2]))
    return sites
'''
WK_PARSE_NEW = '''def parse_sites_doc(path):
    """[(module, enclosing, label)] from L192_annotated_sites.txt at the repo root.

    One parser, because the format has more than one consumer. Both
    test_worksheet_keys.py and test_extractor_pins.py read this file,
    and each carried its own copy of this loop until a RETIRED row was
    added for a deliberately retired key: the copy that had learned the
    tag passed, the copy that had not crashed on int('2026-08-16').
    Fixing the consumer that broke would have left the same landmine
    for the third consumer. (2026-08-16)

    THE STORE ANCHORS BY NAME, NOT LINE (L-277, 2026-09-03). The
    second column is the enclosing function or module-level constant,
    the third the label -- the same two parts the key is made of. A
    line number went stale on every comment inserted above a site, and
    for constants it had ALREADY gone stale without the round trip
    noticing, because a stale line falls back to the label and the
    label is the key. A second column that is all digits is that old
    format, and it is refused rather than read: the caller must not
    be handed rows that look right and mean something else.

    A RETIRED row records why a site left the corpus and is skipped
    here. The inverted assertion that gives it teeth lives with the
    pins, in test_worksheet_keys.py -- this loader only has to not
    choke on it.
    """
    sites = []
    with open(path, encoding='utf-8') as handle:
        for number, raw in enumerate(handle, 1):
            raw = raw.rstrip('\\n')
            if not raw.strip() or raw.startswith('#'):
                continue
            if raw.startswith(RETIRED_TAG + '\\t'):
                continue
            parts = raw.split('\\t')
            if len(parts) < 3:
                continue
            if parts[1].isdigit():
                raise KeyError_(
                    '%s line %d anchors by line number (%r); since L-277 the '
                    'store anchors by enclosing name -- rewrite the row, do '
                    'not patch the number' % (path, number, raw))
            sites.append((parts[0], parts[1], parts[2]))
    return sites
'''

WK_LOCATE_ANCHOR = '''def key_for_site(module_path, source, line, label='', ordinal=None):
'''
WK_LOCATE_NEW = '''def locate_site(source, enclosing, label):
    """(line, reason): the line that introduces `label` inside `enclosing`.

    The inverse of key_for_site, and what lets the site store carry a
    name instead of a line (L-277). Returns the 1-based line of the
    dict key or assignment that introduces the label -- the same line
    worksheet_checker.anchor_label reads -- or (None, reason), where
    the reason names which of three things failed:

      SITE_UNREADABLE  the module does not parse
      SITE_LOST        no such enclosing, or no such label inside it
      SITE_AMBIGUOUS   the label is introduced more than once inside it

    A label equal to its enclosing is a module-level assignment (a
    constant or a module-level string) and resolves to that statement.
    None of the three is silent, on purpose: a site that cannot be
    found and reports nothing is the failure this module exists to
    make impossible.
    """
    try:
        tree = ast.parse(source)
    except SyntaxError as exc:
        return None, 'SITE_UNREADABLE: source does not parse (%s)' % exc
    lines = source.splitlines()

    if label == enclosing:
        for node in tree.body:
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == enclosing:
                        return node.lineno, ''

    span = None
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) \\
                and node.name == enclosing:
            span = (node.lineno, node.end_lineno)
            break
    if span is None:
        return None, 'SITE_LOST: no %s' % enclosing

    hits = []
    for number in range(span[0], span[1] + 1):
        text = lines[number - 1]
        match = DICT_KEY_RE.match(text) or ASSIGN_NAME_RE.match(text)
        if match and match.group(1) == label:
            hits.append(number)
    if len(hits) == 1:
        return hits[0], ''
    if not hits:
        return None, 'SITE_LOST: no %r inside %s' % (label, enclosing)
    return None, ('SITE_AMBIGUOUS: %r introduced %d times inside %s (lines %s)'
                  % (label, len(hits), enclosing,
                     ', '.join(str(h) for h in hits)))


''' + WK_LOCATE_ANCHOR

WK_STAMP_OLD = "Module updated: August 21, 2026 with Anthropic's Claude Opus 5 (L-214).\n"
WK_STAMP_NEW = WK_STAMP_OLD + ("Module updated: September 3, 2026 with Anthropic's Claude Fable 5.1 "
                               "(L-277: the site store anchors by enclosing name; parse_sites_doc "
                               "refuses the line format; locate_site added; the two label regexes "
                               "move here from worksheet_checker).\n")

WC_REGEX_OLD = '''ASSIGN_NAME_RE = re.compile(r"^\\s*([A-Za-z_][A-Za-z_0-9]*)\\s*[:=]")
DICT_KEY_RE = re.compile(r"^\\s*['\\"]([^'\\"]+)['\\"]\\s*:")
'''
WC_REGEX_NEW = '''# One home (L-277): the same two patterns locate a site by name in
# worksheet_keys.locate_site, so a site the store names is the site
# anchor_label below would label. Do not redefine them here.
ASSIGN_NAME_RE = wk.ASSIGN_NAME_RE
DICT_KEY_RE = wk.DICT_KEY_RE
'''
WC_PATH_OLD = "# documentation/worksheets/L192_extractor_pins.txt on every run.\n"
WC_PATH_NEW = "# L192_extractor_pins.txt (repo root since L-277) on every run.\n"
WC_STAMP_OLD = WK_STAMP_OLD
WC_STAMP_NEW = WK_STAMP_OLD + ("Module updated: September 3, 2026 with Anthropic's Claude Fable 5.1 "
                               "(L-277: label regexes now come from worksheet_keys).\n")

TK_PATH_OLD = '''# These are ACTIVE data, not archive. documentation/ holds session
# records that are finished when they are written; these two are read
# on every run and edited when the corpus changes, so they sit with
# the worksheets they describe. The checker's loader takes only .md
# from that directory, so a .txt here is invisible to it -- no phantom
# uncited worksheet, no unreadable-worksheet finding.
SITES_DOC = os.path.join('documentation', 'worksheets',
                         'L192_annotated_sites.txt')
PINS_DOC = os.path.join('documentation', 'worksheets',
                        'L192_key_pins.txt')
'''
TK_PATH_NEW = '''# These are ACTIVE data, not archive, and they live at the repo ROOT
# (L-277, Tony's ruling 2026-09-03): a live store under documentation/
# was lost among hundreds of archived files and invisible to
# doc_index.py, which scans only the root. Each carries a Doc-Kind tag
# so README.md's key-documents table lists it.
SITES_DOC = 'L192_annotated_sites.txt'
PINS_DOC = 'L192_key_pins.txt'
'''
TK_RT_OLD = '''def check_round_trip(sites, sources):
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
'''
TK_RT_NEW = '''def dealias(key, aliases):
    """The key in force today for a stored key; cycles return the key."""
    seen = []
    while key in aliases:
        if key in seen:
            return key
        seen.append(key)
        key = aliases[key]
    return key


def check_round_trip(sites, sources):
    """(minted, failures, collisions) for a list of (module, enclosing, label).

    Four things per row, each of which can fail on its own (L-277):
      1. the row composes to a key and that key RESOLVES;
      2. the site is still FINDABLE by name -- locate_site turns the
         enclosing and label back into a line, through any alias;
      3. re-minting from that line gives the SAME key, so the store and
         the checker agree on what encloses what;
      4. (in main) the minted SET equals the pinned set, by name.
    The old round trip did only (1), and a stale line that fell back to
    its label passed it. Three constants minted wrong keys for weeks.
    """
    minted = {}
    failures = []
    collisions = []
    for module, enclosing, label in sites:
        source = sources.get(module)
        if source is None:
            failures.append((module, enclosing, 'no source for %s' % module))
            continue
        key = wk.compose(module, enclosing, label)
        if key in minted and minted[key] != (module, enclosing, label):
            collisions.append((key, minted[key], (module, enclosing, label)))
        minted[key] = (module, enclosing, label)
        resolved, reason = wk.resolve(key, sources)
        if resolved is None:
            failures.append((module, enclosing, reason))
            continue
        live = wk.parse(dealias(key, wk.INSTALLED_ALIASES))
        live_source = sources.get(live.module)
        if live_source is None:
            failures.append((module, enclosing,
                             'alias points at unread module %s' % live.module))
            continue
        line, reason = wk.locate_site(live_source, live.enclosing, live.label)
        if line is None:
            failures.append((module, enclosing, reason))
            continue
        remint = wk.key_for_site(live.module, live_source, line, label=live.label)
        expect = wk.compose(live.module, live.enclosing, live.label)
        if remint != expect:
            failures.append((module, enclosing,
                             'MINT DRIFT: store says %s, line %d mints %s'
                             % (expect, line, remint)))
    return minted, failures, collisions
'''
TK_PRINT_OLD = '''    for module, line, reason in rt_failures:
        print('    %s:%d  %s' % (module, line, reason))
'''
TK_PRINT_NEW = '''    for module, enclosing, reason in rt_failures:
        print('    %s::%s  %s' % (module, enclosing, reason))
'''
TK_PINSET_OLD = '''        pin_failures = check_pins(pins, sources, aliases=None)
        pin_failures += check_retired_pins(retired, sources)
'''
TK_PINSET_NEW = '''        pin_failures = check_pins(pins, sources, aliases=None)
        pin_failures += check_retired_pins(retired, sources)
        # L-277: the corpus and the pins are the same set, BY NAME. A
        # count comparison could not fail (lose one, gain one, same
        # total); these two lists name what moved.
        for key in sorted(set(minted) - set(pins)):
            pin_failures.append((key, 'UNPINNED: minted by the site '
                                      'store, absent from the pins'))
        for key in sorted(set(pins) - set(minted)):
            pin_failures.append((key, 'UNMINTED: pinned, but no site '
                                      'store row composes it'))
'''
TK_DOC_OLD = '''Domain: dev_tools

The one-time measurement -- 53 distinct annotated sites, 53 distinct
'''
TK_DOC_NEW = '''Domain: dev_tools

Module updated: September 3, 2026 with Anthropic's Claude Fable 5.1
(L-277: the site store anchors by enclosing name and lives at the repo
root; the round trip re-mints from the located line and compares the
minted set to the pins by name).

The one-time measurement -- 53 distinct annotated sites, 53 distinct
'''

TE_PATH_OLD = '''# ACTIVE data, read on every run, so it sits with the worksheets rather
# than among the session records in documentation/. The checker's
# loader takes only .md from that directory, so a .txt here raises no
# phantom uncited worksheet -- the same reason the key pins live there.
SITES_DOC = os.path.join('documentation', 'worksheets',
                         'L192_annotated_sites.txt')
PINS_DOC = os.path.join('documentation', 'worksheets',
                        'L192_extractor_pins.txt')
'''
TE_PATH_NEW = '''# ACTIVE data, read on every run, and it lives at the repo ROOT
# (L-277, Tony's ruling 2026-09-03): a live store under documentation/
# was lost among hundreds of archived files and invisible to
# doc_index.py, which scans only the root. Each carries a Doc-Kind tag
# so README.md's key-documents table lists it.
SITES_DOC = 'L192_annotated_sites.txt'
PINS_DOC = 'L192_extractor_pins.txt'
'''
TE_MEASURE_OLD = '''def measure(sites):
    """({key: (kept_raws, dropped)}, unreadable_modules).

    Claim membership is computed by worksheet_checker.physical_claims,
    never re-implemented here. A second implementation would agree with
    itself and prove nothing.
    """
    modules = sorted({module for module, _line, _label in sites})
    sources = {}
    units = {}
    unreadable = []
    for name in modules:
        if not os.path.exists(name):
            unreadable.append(name)
            continue
        try:
            with open(name, encoding='utf-8') as handle:
                sources[name] = handle.read()
            for unit in ps.extract_units_from_file(name, name[:-3], 'orrery'):
                units[(name, unit.line_start)] = unit
        except (IOError, OSError, SyntaxError, ValueError) as exc:
            unreadable.append('%s (%s)' % (name, exc))

    measured = {}
    for module, line, label in sites:
        unit = units.get((module, line))
        if unit is None or not getattr(unit, 'raw_value', None):
            continue                   # a constant, not a display string
        kept, dropped = wc.physical_claims(unit)
        key = wk.key_for_site(module, sources[module], line, label=label)
        measured[key] = ([raw for _value, raw in kept], dropped)
    return measured, unreadable
'''
TE_MEASURE_NEW = '''def measure(sites):
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
'''
TE_CALL_OLD = '''    measured, unreadable = measure(sites)
    for name in unreadable:
        failures.append('UNREADABLE %s -- counted as a failure, not skipped'
                        % name)
'''
TE_CALL_NEW = '''    measured, unreadable, lost = measure(sites)
    for name in unreadable:
        failures.append('UNREADABLE %s -- counted as a failure, not skipped'
                        % name)
    for text in lost:
        failures.append('SITE NOT FOUND %s -- counted as a failure, not '
                        'skipped' % text)
'''
TE_REPIN_OLD = '''    lines = [
        '# Extractor pins -- what the instruction filter keeps and drops.',
'''
TE_REPIN_NEW = '''    lines = [
        '# Doc-Kind: hand | Extractor pins for the L-192 corpus: what the '
        'instruction filter keeps and drops at each display-string site, '
        'frozen by Tony 2026-08-14. Read by test_extractor_pins.py on every '
        'maintenance run; regenerate only from that test\\'s REPIN output.',
        '# Extractor pins -- what the instruction filter keeps and drops.',
'''
TE_DOC_OLD = '''Domain: dev_tools

Tony froze INSTRUCTION_LOOKBACK at 30 and INSTRUCTION_LOOKAHEAD at 25
'''
TE_DOC_NEW = '''Domain: dev_tools

Module updated: September 3, 2026 with Anthropic's Claude Fable 5.1
(L-277: the site store anchors by enclosing name and lives at the repo
root; measure() finds each string site by name through the checker's
own anchor map, and a site it cannot find fails the run).

Tony froze INSTRUCTION_LOOKBACK at 30 and INSTRUCTION_LOOKAHEAD at 25
'''

LG_277_OLD = '''<!-- L:277 status:OPEN upd:2026-09-02 section:A flag: rice:3/3/90/2 -->
'''
LG_277_NEW = '''<!-- L:277 status:OPEN upd:2026-09-03 section:A flag: rice:3/3/90/2 -->
- **Tony's ruling, 2026-09-03: (b), and move the stores.** "I agree
  with (b). What I am surprised by is that I was not aware of this
  important file lost among hundreds of archived files. This file
  should at least be located in the root not in documentation/ and it
  should be tracked by the document tracker." Widened on Claude's
  recommendation to all three live L-192 stores, since the sites and
  the two pin files work as one set.
- **Found while building it: the store was ALREADY stale and the
  round trip could not see it.** All 23 `constants_new.py` rows
  pointed at lines that no longer held the named constant, left over
  from the August constants migration. `key_for_site` falls back to
  the label when no enclosing is found at a stale line, and for a
  constant the label IS the key, so the test stayed green. Three rows
  sat inside OTHER constants' statements and minted wrong keys --
  `constants_new.py::KM_PER_AU::EARTH_POLAR_RADIUS_KM`,
  `::EARTH_EQUATORIAL_RADIUS_KM::SPEED_OF_LIGHT_KM_S`,
  `::OUTER_CORONA_RADII::BENNU_RADIUS_KM` -- and nothing reported it,
  because the round trip checked that minted keys RESOLVE and never
  compared them to the pinned set. A Check That Cannot Fail, in the
  test built to be the check.
- **`patch_L277_reanchor_site_stores.py` (2026-09-03):** the site
  store rows become `module TAB enclosing TAB label`;
  `parse_sites_doc` refuses a numeric second column; `locate_site()`
  turns a name back into a line (SITE_LOST / SITE_AMBIGUOUS, never
  silent); the round trip re-mints from that line and compares the
  minted set to the pins BY NAME; `measure()` in the extractor test
  finds each string site by name through the checker's own anchor
  map. The 52 new rows were derived from the pins and verified to
  mint exactly the 52 live pins. All three stores moved to the repo
  root with `Doc-Kind: hand` tags. Tested on a throwaway clone: both
  tests green, doc_index lists the three.
- **Tony-action (do):** run the patch, then the maintenance run.
  Expect README.md's key-documents table to gain three rows.
'''
LG_277_GAP_OLD = '''**Gap:** decision, then a patch. The 2026-09-02 breakage is already
repaired; this item is about the next eight.
**Ref:** worksheet_keys.py `key_for_site` / `enclosing_name` /
`parse_sites_doc`; documentation/worksheets/L192_annotated_sites.txt;
documentation/worksheets/L192_extractor_pins.txt; L-192; L-254.
'''
LG_277_GAP_NEW = '''**Gap:** the patch has run and the maintenance run is green with the
three stores in README.md's table. Close then. Decided and built
2026-09-03; the 2026-09-02 breakage was already repaired by hand.
**Ref:** worksheet_keys.py `key_for_site` / `enclosing_name` /
`locate_site` / `parse_sites_doc`; L192_annotated_sites.txt,
L192_extractor_pins.txt, L192_key_pins.txt (repo root since
2026-09-03); doc_index.py; L-192; L-254; L-273.
'''
LG_265_OLD = '''<!-- L:265 status:OPEN upd:2026-08-30 section:A flag: rice:4/3/90/2 -->
'''
LG_265_NEW = '''<!-- L:265 status:OPEN upd:2026-09-03 section:A flag: rice:4/3/90/2 -->
- **Curated 2026-09-02/03, patch delivered, not yet run.** Tony's
  rule: a NASA page where one is specific to the feature (not a hub
  page about the Sun or the atmosphere in general), else English
  Wikipedia; one exception by his word -- the corona shells take
  Wikipedia's Solar corona article because the only NASA corona page
  is Space Place, written for children. Result: 5 NASA (Alfven
  surface, Outer Oort Cloud x2, Lower Atmosphere, Upper Atmosphere,
  plus both radiation belts via the `info_urls` array), 15 Wikipedia.
  Every URL was returned live by a search or fetch on the day; none
  recalled. `patch_L265_info_url_curated.py` (gallery repo) edits
  `objects_config.json` only; the served `feature_configs.json` and
  `coverage_index.json` are builder outputs and follow on the next
  builder run. Claude first counted 20 and missed the two belts in
  `info_urls`; the patch now asserts zero placeholders remain anywhere
  in the file.
- **Tony-action (do):** run the patch, run the cache builder, commit
  and push both. Then Stage C (L-267) is unblocked.
'''

EDITS = [
    ("worksheet_keys.py", [
        (WK_REGEX_OLD, WK_REGEX_NEW),
        (WK_PARSE_OLD, WK_PARSE_NEW),
        (WK_LOCATE_ANCHOR, WK_LOCATE_NEW),
        (WK_STAMP_OLD, WK_STAMP_NEW),
    ]),
    ("worksheet_checker.py", [
        (WC_REGEX_OLD, WC_REGEX_NEW),
        (WC_PATH_OLD, WC_PATH_NEW),
        (WC_STAMP_OLD, WC_STAMP_NEW),
    ]),
    ("test_worksheet_keys.py", [
        (TK_PATH_OLD, TK_PATH_NEW),
        (TK_RT_OLD, TK_RT_NEW),
        (TK_PRINT_OLD, TK_PRINT_NEW),
        (TK_PINSET_OLD, TK_PINSET_NEW),
        (TK_DOC_OLD, TK_DOC_NEW),
    ]),
    ("test_extractor_pins.py", [
        (TE_PATH_OLD, TE_PATH_NEW),
        (TE_MEASURE_OLD, TE_MEASURE_NEW),
        (TE_CALL_OLD, TE_CALL_NEW),
        (TE_REPIN_OLD, TE_REPIN_NEW),
        (TE_DOC_OLD, TE_DOC_NEW),
    ]),
    ("LEDGER_CONSOLIDATED.md", [
        (LG_277_OLD, LG_277_NEW),
        (LG_277_GAP_OLD, LG_277_GAP_NEW),
        (LG_265_OLD, LG_265_NEW),
    ]),
]


def fail(msg):
    print("FAILURE: " + msg)
    print("NOTHING was written. Undo is Discard Changes in GitHub Desktop.")
    sys.exit(1)


def fingerprint(data):
    return hashlib.md5(data.replace(b"\r\n", b"\n")).hexdigest()


def main():
    # ---- gate: every source present and unchanged, every target absent
    raw = {}
    for path, expected in FINGERPRINTS.items():
        if not os.path.exists(path):
            fail("missing %s -- run from the orrery repo root" % path)
        with open(path, "rb") as f:
            raw[path] = f.read()
        fp = fingerprint(raw[path])
        if fp != expected:
            fail("base moved: %s is %s, expected %s" % (path, fp, expected))
        print("ok  fingerprint %s  %s" % (fp[:8], path))
    for name in NEW_ROOT:
        if os.path.exists(name):
            fail("%s already exists at the root; this patch would overwrite it" % name)

    # ---- plan every text edit before writing anything
    out = {}
    for path, edits in EDITS:
        data = raw[path]
        is_crlf = data.count(b"\r\n") > 0
        for old, new in edits:
            o = old.encode("utf-8")
            n = new.encode("utf-8")
            try:
                n.decode("ascii")
            except UnicodeDecodeError:
                fail("inserted text is not ASCII in %s" % path)
            if is_crlf:
                o = o.replace(b"\n", b"\r\n")
                n = n.replace(b"\n", b"\r\n")
            count = data.count(o)
            if count != 1:
                fail("ANCHOR FAIL in %s: expected 1 match, got %d for %r"
                     % (path, count, old[:70]))
            data = data.replace(o, n)
        out[path] = data
        print("ok  %d edit(s) planned  %s" % (len(edits), path))

    # ---- plan the three moves
    old_sites = raw[os.path.join(WS, "L192_annotated_sites.txt")]
    old_rows = [l for l in old_sites.decode("utf-8").replace("\r\n", "\n").split("\n")
                if l and not l.startswith("#") and not l.startswith("RETIRED\t")]
    n_old = len(old_rows)
    sites_text = SITES_NEW.replace("__ROWS__", "")
    n_new = len([l for l in sites_text.split("\n")
                 if l and not l.startswith("#") and not l.startswith("RETIRED\t")])
    if n_old != n_new:
        fail("row count: old store has %d rows, new has %d" % (n_old, n_new))
    old_labels = sorted((r.split("\t")[0], r.split("\t")[2]) for r in old_rows)
    new_labels = sorted((r.split("\t")[0], r.split("\t")[2]) for r in
                        [l for l in sites_text.split("\n")
                         if l and not l.startswith("#") and not l.startswith("RETIRED\t")])
    if old_labels != new_labels:
        fail("the new store does not carry the same (module, label) set")
    print("ok  site store: %d rows, same (module, label) set, now anchored by name" % n_new)
    sites_text.encode("ascii")

    moves = {
        "L192_annotated_sites.txt": (os.path.join(WS, "L192_annotated_sites.txt"),
                                     sites_text.encode("ascii")),
        "L192_extractor_pins.txt":  (os.path.join(WS, "L192_extractor_pins.txt"),
                                     PINS_TAG.encode("ascii") + raw[os.path.join(WS, "L192_extractor_pins.txt")]),
        "L192_key_pins.txt":        (os.path.join(WS, "L192_key_pins.txt"),
                                     KEYS_TAG.encode("ascii") + raw[os.path.join(WS, "L192_key_pins.txt")]),
    }
    for name, (src, content) in moves.items():
        if raw[src].count(b"\r\n") > 0:
            content = content.replace(b"\n", b"\r\n").replace(b"\r\r\n", b"\r\n")
            moves[name] = (src, content)

    # ---- write: edits, then new root files, then remove the old copies
    for path, data in out.items():
        with open(path, "wb") as f:
            f.write(data)
        print("wrote  %s" % path)
    for name, (src, content) in moves.items():
        with open(name, "wb") as f:
            f.write(content)
        os.remove(src)
        print("moved  %s -> %s" % (src, name))

    for path in ("worksheet_keys.py", "worksheet_checker.py",
                 "test_worksheet_keys.py", "test_extractor_pins.py"):
        try:
            py_compile.compile(path, doraise=True)
        except py_compile.PyCompileError as exc:
            print("COMPILE ERROR after write in %s: %s" % (path, exc))
            print("The edits are on disk. Undo is Discard Changes in GitHub Desktop.")
            sys.exit(1)
        print("ok  compiles  %s" % path)

    print("patch applied: 5 files edited, 3 stores moved to the root.")
    print("Stamps updated: worksheet_keys.py, worksheet_checker.py,")
    print("  test_worksheet_keys.py, test_extractor_pins.py (Module updated lines);")
    print("  L-277 and L-265 upd dates in LEDGER_CONSOLIDATED.md.")
    print("Next: run orrery_maintenance_run.py. Expect the two L-192 tests")
    print("  green and README.md's key-documents table to gain three rows.")


if __name__ == "__main__":
    main()
