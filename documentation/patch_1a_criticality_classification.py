"""Phase 1a -- D1/D2 criticality classification (ledger L-156).

Built on 459fecd1e5c1bf7b391cd4e794075aacdbfea120
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

Target: provenance_scanner.py  (md5 of expected base: e8357354c55491a676b8c29bd3eea8c8)

Replaces volume-based criticality (how many modules import a name) with
type-based criticality (what kind of claim the value makes). Consumer count
is still resolved and still reported; it no longer sets the score.

Transactional: every anchor must match exactly once or nothing is written.
Edits are applied bottom-up. Binary mode throughout -- no encoding rewrite.

Run from the repo root:  python patch_1a_criticality_classification.py
"""

import hashlib
import os
import sys

PATH = 'provenance_scanner.py'
EXPECTED_MD5 = 'e8357354c55491a676b8c29bd3eea8c8'


def main():
    if not os.path.exists(PATH):
        print('ERROR: run this from the repo root (%s not found)' % PATH)
        return 1

    with open(PATH, 'rb') as f:
        src = f.read()

    actual = hashlib.md5(src).hexdigest()
    if actual != EXPECTED_MD5:
        print('ERROR: base file is not the expected revision.')
        print('  expected md5: %s' % EXPECTED_MD5)
        print('  actual   md5: %s' % actual)
        print('  Re-pull at HEAD and re-check before patching.')
        return 1

    edits = build_edits()

    for label, old, new in edits:
        n = src.count(old)
        if n != 1:
            print('ANCHOR FAIL [%s]: %d matches, expected 1. Nothing written.'
                  % (label, n))
            return 1

    for label, old, new in edits:
        src = src.replace(old, new, 1)
        print('  ok  %s' % label)

    with open(PATH, 'wb') as f:
        f.write(src)

    print('patch applied (%d bytes)' % len(src))
    print('next: python -m py_compile provenance_scanner.py')
    print('      python provenance_scanner.py . --output PROVENANCE_AUDIT.md')
    return 0


def build_edits():
    """Return [(label, old_bytes, new_bytes)] in bottom-up file order."""
    edits = []

    # ---- Edit 3 (highest line): score_unit criticality block ----
    edits.append((
        'score_unit criticality block',
        b"""    # ---- Criticality ----
    if unit.kind == 'string':
        unit.crit = C_PUBLIC
        unit.crit_reason = "Public-facing display string (hover/INFO)"
    elif unit.kind in ('constant', 'dict') and unit.name:
        count, consumers = name_is_imported(
            unit.name, unit.module, imported_names)
        unit.consumer_count = count
        unit.consumers = consumers
        if count >= 3:
            unit.crit = C_PROPAGATING
            unit.crit_reason = f"Imported by {count} modules"
        elif count >= 1:
            unit.crit = C_LOADBEARING
            unit.crit_reason = f"Imported by {count} module(s)"
        else:
            unit.crit, unit.crit_reason = _role_based_criticality(unit)
    else:
        unit.crit, unit.crit_reason = _role_based_criticality(unit)
""",
        b"""    # ---- Criticality ----
    # D1: criticality is now by claim TYPE, not by import volume. Consumer
    # count is still resolved and still reported (blast radius is useful
    # information) but it no longer sets the score.
    if unit.kind == 'string':
        unit.crit = C_PUBLIC
        unit.crit_reason = "Public-facing display string (hover/INFO)"
    elif unit.kind in ('constant', 'dict') and unit.name:
        count, consumers = name_is_imported(
            unit.name, unit.module, imported_names)
        unit.consumer_count = count
        unit.consumers = consumers
        unit.crit, unit.crit_reason = classify_criticality(unit)
    else:
        unit.crit, unit.crit_reason = _role_based_criticality(unit)
"""))

    # ---- Edit 2: insert the classifier ahead of score_unit ----
    edits.append((
        'insert classify_criticality',
        b"def score_unit(unit, imported_names, pinned_values=None):\n",
        b'''def classify_criticality(unit):
    """Classify a constant/dict unit into a D1 criticality category.

    Returns (crit, crit_reason). Match order is significant:

        role veto -> cosmetic -> absolute-override -> relational
                  -> measured -> internal(name) -> same four on entry KEYS
                  -> measured(role) -> undetermined

    Name before keys is deliberate: a dict's entry keys are usually its
    DOMAIN (body names, module names), not the quantity it stores.
    Classifying CENTER_BODY_RADII from its keys would read "Mercury",
    not "radii".
    """
    numeric_entries = any(
        isinstance(v, (int, float)) and not isinstance(v, bool)
        for _, v, _, _ in (unit.entries or []))

    role = unit.role or ''
    # Role VETO. A devtool/gui/cache module does not hold claims about the
    # world, so a generic physical stem must not promote its parameters.
    # Measured during the 1a build: without this, HUB_THRESHOLD ('threshold'),
    # MAX_DATA_AGE_DAYS ('_days') and PERFRAME_INDICATOR_RADIUS_FACTOR
    # ('radius') all scored MEASURED and put uncited tool config into Tier 1.
    if role in CRIT_INTERNAL_ROLES:
        return C_INTERNAL, f"Internal (role '{role}')"

    cat = _crit_by_vocabulary(unit.name or '', unit.kind, numeric_entries)
    src = 'name'
    if cat is None:
        for key, _, _, _ in (unit.entries or []):
            cat = _crit_by_vocabulary(key, unit.kind, numeric_entries)
            if cat is not None:
                src = 'key'
                break
    if cat is None:
        if role in CRIT_PHYSICAL_ROLES:
            return C_MEASURED, f"MEASURED (inferred from role '{role}')"
        return C_UNDETERMINED, "UNDETERMINED -- could not be classified"

    if cat == 'cosmetic':
        return C_COSMETIC, f"Cosmetic ({src} vocabulary)"
    if cat == 'relational':
        return C_RELATIONAL, f"RELATIONAL -- defined against a tracked base ({src})"
    if cat == 'measured':
        return C_MEASURED, f"MEASURED -- independently catalogued fact ({src})"
    return C_INTERNAL, f"Internal use ({src} vocabulary)"


def _crit_by_vocabulary(name, kind, numeric_entries):
    """Match one name against the criticality vocabulary. None = no match."""
    if _vocab_hit(name, CRIT_COSMETIC_STEMS):
        # D2 cosmetic gate: the name heuristic alone is not enough. A dict
        # named "colors" that holds numbers stops being waved through.
        if not (kind == 'dict' and numeric_entries):
            return 'cosmetic'
    if name in CRIT_ABSOLUTE_OVERRIDE:
        return 'measured'
    if _vocab_hit(name, CRIT_RELATIONAL_STEMS):
        return 'relational'
    if _vocab_hit(name, CRIT_MEASURED_STEMS):
        return 'measured'
    if _vocab_hit(name, CRIT_INTERNAL_STEMS):
        return 'internal'
    return None


def _vocab_hit(name, stems):
    """Token-aware stem match.

    Tokens, not substrings: PAGES_CEILING_MB must not match the stem 'age',
    and TEMPLATE must not match 'temp'. A stem written with a leading
    underscore matches the FINAL token only, so '_km' reads as a unit suffix
    rather than an anywhere-match.
    """
    tokens = [t for t in (name or '').lower().replace('-', '_').split('_') if t]
    if not tokens:
        return False
    for stem in stems:
        if stem.startswith('_'):
            if tokens[-1] == stem[1:]:
                return True
        else:
            for tok in tokens:
                if tok == stem or (tok.startswith(stem)
                                   and len(tok) - len(stem) <= 2):
                    return True
    return False


def score_unit(unit, imported_names, pinned_values=None):
'''))

    # ---- Edit 1 (lowest line): constants + vocabulary ----
    edits.append((
        'criticality constants + vocabulary',
        b"C_PROPAGATING = 5   # Imported by other modules, affects calculations\n",
        b'''C_PROPAGATING = 5   # Imported by other modules, affects calculations

# D1 (ledger L-156) replaced volume-based criticality with type-based
# criticality. The two categories that now decide a constant's or dict's
# score:
C_RELATIONAL  = 4   # Defined as a fraction/multiple of a tracked base
C_MEASURED    = 5   # Independently catalogued fact (radii, periods, masses)
# Ambiguity is not resolved by guessing in either direction. It scores at
# the MEASURED weight (fail-safe up, per D2) AND raises its own report
# banner (per the design review's amendment), so it can neither be buried
# by a low score nor lost in a normal finding row.
C_UNDETERMINED = 5

# ============================================================
# CRITICALITY CLASSIFICATION VOCABULARY (D2, ledger L-156)
# ============================================================
# D2 settled that classification rides the codebase's own naming
# conventions rather than a hand-curated list of named constants. This is
# that rule. It is widened from D2's four unit suffixes to the noun stems
# the codebase actually uses -- KNOWN_ORBITAL_PERIODS and
# COMET_NUCLEUS_SIZES carry their physical meaning in the noun, not in a
# _km/_au suffix, and under D2 as written both defaulted to unclassified
# (62 of 112 constant/dict units did).
#
# L-163's docstring role tags did not exist when D2 was written. They are
# used here as a second, structural input: as a veto on the physical
# categories for devtool/gui/cache modules, and as a fallback for what the
# vocabulary leaves unresolved in data/computation modules.
#
# Additions to these tuples are ledger-tracked under L-156.

CRIT_COSMETIC_STEMS = (
    'color', 'colour', 'label', 'opacity', 'font', 'rgb', 'symbol',
    'tooltip', 'marker',
)
CRIT_RELATIONAL_STEMS = (
    'fraction', 'multiplier', 'scale', 'ratio', 'factor', 'radii',
)
CRIT_MEASURED_STEMS = (
    '_km', '_au', '_kg', '_days', '_deg', '_sec', '_yr',
    'period', 'radius', 'size', 'mass', 'distance', 'belt', 'magnitude',
    'luminosity', 'velocity', 'density', 'albedo', 'diameter',
    'uncertainty', 'inclination', 'eccentricity', 'tilt', 'obliquity',
    'gravity', 'pressure', 'flux', 'wavelength', 'temp', 'temperature',
    'threshold',
)
CRIT_INTERNAL_STEMS = (
    'map', 'mapping', 'name', 'names', 'slug', 'config', 'dir', 'path',
    'url', 'version', 'schema', 'key', 'order', 'alias', 'width',
    'height', 'frames', 'points', 'resolution', 'decimals', 'interval',
    'title', 'tag', 'desc', 'col', 'wrap', 'trunc', 'kb', 'mb', 'count',
    'index', 'limit', 'skip', 'default', 'docstring', 'docstrings',
    'patch', 'ceiling', 'age',
)
CRIT_INTERNAL_ROLES = ('devtool', 'gui', 'cache')
CRIT_PHYSICAL_ROLES = ('data', 'computation')

# Names whose suffix reads relational but whose values are absolute.
# CENTER_BODY_RADII stores kilometres, not multiples of a base radius, so
# the '_radii' stem would misfile the project's central radius dict.
# NOTE: this becomes moot once L-162 (Phase A) rewires the dict to
# reference named *_RADIUS_KM constants -- the values become Name nodes,
# the dict yields no numeric entries, and the named constants are scored
# directly instead. Re-check after Phase A lands.
CRIT_ABSOLUTE_OVERRIDE = ('CENTER_BODY_RADII',)
'''))

    return edits


if __name__ == '__main__':
    sys.exit(main())
