"""
provenance_scanner.py - Fact provenance auditor for Paloma's Orrery.

Scans every .py file in the project for facts that need verification:
named constants, dictionary contents, and numeric claims in display
strings. Scores each finding by Vulnerability x Criticality and flags
cross-file duplicates and inconsistencies. Produces PROVENANCE_AUDIT.md.

Architecture: "unit of provenance"
    The unit is the smallest thing that has a coherent source citation.
    A dict with one `# Source:` comment is ONE unit, not N entries.
    A hover string with three numbers that co-refer is ONE unit, not
    three separate claims. Each unit is scored once; reports can break
    down to per-entry for dicts when displayed.

    This matters because citations in this codebase attach at the
    declaration level (above a dict, in its docstring, at the top of
    a section) rather than line-by-line. An earlier line-granular
    scanner flagged every dict entry as uncited even when the dict
    itself had a clear source block above it.

    Criticality is resolved per imported-name, not per module. If
    `KM_PER_AU` is imported by four files, it is C=5 (propagating).
    If `color_map` is defined in the same file but not imported
    anywhere, it is not C=5 just because its module is.

Companion tools:
    module_atlas.py               -- shared dependency graph
    test_constants_provenance.py  -- pins specific verified values
                                     in constants_new.py

Usage:
    python provenance_scanner.py                   # scan current directory
    python provenance_scanner.py /path/to/project  # scan specific directory
    python provenance_scanner.py --output audit.md # custom output filename

Known limitations and accepted residuals:
    1. Multi-line string false positives (info_dictionary.py):
       INFO strings can be 50-100 lines long. The scanner detects
       citations at the entry-key level (# Source: above the dict key)
       but individual continuation lines within the same string may
       fall outside the lookback window and be reported as uncited.
       Lookback was increased from 30 to 60 lines (April 2026) to
       reduce this, but entries longer than ~60 lines (Apollo 11 S-IVB,
       Halley, Artemis II) will still produce mid-string false positives.
       These are not real gaps -- the citation exists at the key level.
       Treat Tier-2 findings in info_dictionary.py as accepted residuals
       unless they correspond to a top-level entry key that genuinely
       lacks a # Source: comment.

    2. "Sourced but potentially stale" (V_STALE) findings:
       Entries verified correct by Gemini fact-check (April 2026) but
       containing date-sensitive language (e.g. "currently", "planned",
       "expected") are flagged V_STALE regardless. These reflect real
       staleness risk for mission status and close-approach data, not
       citation gaps. Review when adding new objects or updating missions,
       not as standalone audit tasks.

    3. Lagrange point entries (L1-L5, EM-L1 through EM-L5):
       Text is reproduced verbatim from JPL Horizons output and carries
       "From JPL Horizons" inline. Source comments added April 2026.
       Any residual flags on continuation lines are false positives.

    4. Numeric values in code lines flagged as display strings:
       The scanner occasionally flags numeric literals in Python code
       (variable assignments, np.radians() calls, coordinate arithmetic)
       as uncited display string claims. Known examples confirmed as
       false positives (April 2026 audit):
         - asteroid_belt_visualization_shells.py line 218 (showlegend=True)
         - earth_visualization_shells.py line 649 (trace construction)
         - neptune_visualization_shells.py lines 647, 679, 903
           (magnetic axis coordinates and offsets)
         - solar_visualization_shells.py lines 1237, 1497, 1621, 1672
           (rendering geometry)
       Root cause: the scanner uses AST string-node detection; numeric
       literals in adjacent code share the same line range. These will
       recur whenever shell files are regenerated. No action needed.

    5. Module docstrings and dict key strings flagged as display strings:
       Known false positives (April 2026 audit):
         - jupiter_visualization_shells.py line 1 (module docstring)
         - comet_visualization_shells.py line 1282 (function docstring)
         - sgr_a_star_data.py lines 657, 664 (dict key name strings,
           not display text)
         - star_notes.py line 1 (module docstring)
       The scanner's docstring detector catches most of these but misses
       dict key strings. No action needed.

    6. Dict values with inline 'source' keys not recognized as citations:
       spacecraft_encounters.py Tier-2 findings at lines 235 and 266
       carry 'source': 'NASA/JSC' as a dict value. The scanner requires
       a # Source: comment; inline dict keys are not recognized. These
       entries are cited -- the scanner notation is a false positive.
       Future fix: extend SOURCE_PATTERNS to recognize 'source': '...'
       dict value pattern.

    7. Accepted Tier-2 residuals (genuine gaps, low urgency):
       The following are real citation gaps but low-risk and deferred:
         - star_notes.py: Orion Belt stars (Bellatrix, Mintaka, Alnilam,
           Alnitak), Fomalhaut, Shaula stellar parameters. Queued for
           Gemini fact-check.
         - uranus_visualization_shells.py lines 534, 563: radiation belt
           extent "3 to 10 R" based on Voyager 2 data. Queued for
           Gemini fact-check.
         - solar_visualization_shells.py ~line 1694: Oort Cloud hover
           text population estimates. Queued for Gemini fact-check.
         - star_notes.py unique_notes dict (553 entries, score 15):
           stellar parameters drift as catalogs improve. Review when
           adding new stars, not as standalone audit task.
         - comet_visualization_shells.py COMET_NUCLEUS_SIZES dict and
           COMET_FEATURE_THRESHOLDS dict: rendering geometry, no user-
           visible impact if slightly off. Deferred.
         - constants_new.py Tier-2 items: all have source citations
           (score 10 = V_SOURCED x C_PROPAGATING). No action needed.

Module rewritten: April 17, 2026 with Anthropic's Claude Opus 4.7
    (replaces earlier line-granular scanner. The previous version
    produced ~2000 false-positive Tier-1 findings because block-level
    citations were invisible at its resolution.)
"""

import ast
import os
import re
import sys
from collections import defaultdict
from datetime import datetime

# Reuse the atlas dependency graph builder
from module_atlas import build_dependency_graph, classify_role


# ============================================================
# SCORING CONSTANTS
# ============================================================

# Vulnerability: how likely is this fact to be wrong?
V_FETCHED  = 1   # From authoritative pipeline at runtime
V_SOURCED  = 2   # Hardcoded but has citation
V_STALE    = 3   # Was sourced but may have changed
V_RECALLED = 4   # From LLM training data, no citation

# Criticality: what's the impact if it IS wrong?
C_COSMETIC    = 1   # Colors, label positions, descriptive text
C_INTERNAL    = 2   # Used in code but not displayed
C_LOADBEARING = 3   # Drives geometry, shell radii, orbit params
C_PUBLIC      = 4   # Visible in hover text, gallery, Instagram
C_PROPAGATING = 5   # Imported by other modules, affects calculations


def action_tier(score):
    """Return tier number (1=highest priority, 4=lowest)."""
    if score >= 16: return 1
    if score >= 10: return 2
    if score >= 5:  return 3
    return 4


# ============================================================
# CITATION PATTERNS
# ============================================================
# Applied to the text of a "context block" -- up to 30 lines
# preceding a unit, plus the unit's own lines. This is where
# `# Source: ...` block comments live.

SOURCE_PATTERNS = [
    re.compile(r'#\s*[Ss]ource\s*:', re.IGNORECASE),
    re.compile(r'#\s*(?:Ref|Reference)\s*:', re.IGNORECASE),
    re.compile(r'#\s*(?:IAU|JPL|NASA|ESA|NIST|Horizons|arXiv|doi|'
               r'SIMBAD|Gaia|Hipparcos|VizieR|NSSDCA|NOAA|BCO[- ]DMO|'
               r'ERA5|Copernicus)', re.IGNORECASE),
    re.compile(r'#\s*https?://', re.IGNORECASE),
    re.compile(r'#\s*(?:Verified|Confirmed)\s+', re.IGNORECASE),
    re.compile(r'#\s*(?:Based on|Per|Derived from|According to)\s+',
               re.IGNORECASE),
    # Markers that appear inside docstrings (no leading '#')
    re.compile(r'^\s*[Ss]ource\s*:\s', re.MULTILINE),
    re.compile(r'^\s*[Vv]erified\s*:\s', re.MULTILINE),
    re.compile(r'^\s*[Rr]ef(?:erence)?\s*:\s', re.MULTILINE),
    # URL-as-citation patterns (data dict entries like celestial_objects.py
    # where `mission_url` sits alongside `mission_info` narrative).
    # An https URL appearing anywhere in the context block, or a *_url
    # key in a dict, counts as a citation for adjacent claims.
    re.compile(r"['\"]?\w*url\w*['\"]?\s*[:=]\s*['\"]https?://",
               re.IGNORECASE),
    re.compile(r'https?://\S+\.\S+', re.IGNORECASE),
]

# Patterns that suggest a cited value may be stale (date-sensitive).
STALE_PATTERNS = [
    re.compile(r'(?:as of|current|currently|latest|updated)\s+\d{4}',
               re.IGNORECASE),
    re.compile(r'(?:Planned|Expected|Upcoming|scheduled)\b',
               re.IGNORECASE),
    re.compile(r'(?:Still active|Currently operating)', re.IGNORECASE),
]

# Looser patterns applied ONLY to docstring text. Docstrings are prose
# and mention provenance without the structured `# Source:` marker.
# If a module or function docstring uses any of these words in a
# citation-like context, we treat the associated claims as cited.
DOCSTRING_CITATION_PATTERNS = [
    re.compile(r'\b[Vv]erified\b', re.IGNORECASE),
    re.compile(r'\b[Cc]itation\b', re.IGNORECASE),
    re.compile(r'\b[Cc]ited\b', re.IGNORECASE),
    re.compile(r'\b(?:authoritative|nominal|canonical)\b', re.IGNORECASE),
    re.compile(r'\b(?:IAU|JPL|NASA|NIST|ESA|Horizons)\b'),
    re.compile(r'\b(?:arXiv|doi)\b', re.IGNORECASE),
    re.compile(r'\bper\s+(?:IAU|JPL|NASA|NIST|ESA|Gemini|review)\b',
               re.IGNORECASE),
    re.compile(r'\bSource of truth\b', re.IGNORECASE),
    re.compile(r'\b[Rr]eviewed\s+by\b'),
]


def has_citation(text, is_docstring=False):
    """Does the given text block contain a citation marker?

    If `is_docstring` is True, prose-style markers are also accepted
    (docstrings describe provenance in prose, not in `# Source:` form)."""
    for pat in SOURCE_PATTERNS:
        if pat.search(text):
            return True
    if is_docstring:
        for pat in DOCSTRING_CITATION_PATTERNS:
            if pat.search(text):
                return True
    return False


def has_stale_marker(text):
    """Does the given text contain a staleness indicator?"""
    for pat in STALE_PATTERNS:
        if pat.search(text):
            return True
    return False


# ============================================================
# NUMERIC CLAIM EXTRACTION (for display strings)
# ============================================================
# Captures numbers with optional comma separators and decimal parts.
# Comma handling: "31,000 km" is one token, not "31" + "000 km".

NUMERIC_CLAIM_RE = re.compile(
    r'(\d{1,3}(?:,\d{3})+(?:\.\d+)?|'     # 31,000 or 31,000.5
    r'\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)'    # 8.33 or 1.5e-3
    r'\s*'
    r'(R_sun|AU|km/s|km|m/s|degrees?|deg\b|arcsec|mas|pc|kpc|Mpc|'
    r'solar radii|Earth (?:masses|radii)|M_sun|M_earth|R_earth|'
    r'ly|light[- ]years?|parsec|'
    r'days?|years?|hours?|minutes?\b|min\b|sec\b|'
    r'K\b|kelvin|kg\b|g/cm3|g/cc|'
    r'km/h|mph)\b',
    re.IGNORECASE
)


def extract_numeric_claims(text):
    """Yield (num_str, unit, value_float) for each numeric claim in text.
    Trivial paired values (0/1/2/3 days/years/hours) are skipped."""
    for m in NUMERIC_CLAIM_RE.finditer(text):
        num_str = m.group(1)
        unit = m.group(2)
        try:
            value = float(num_str.replace(',', ''))
        except ValueError:
            continue
        if value in (0, 1, 2, 3) and unit.lower() in (
                'days', 'years', 'hours', 'minutes', 'min'):
            continue
        yield num_str, unit, value


# ============================================================
# IMPORT RESOLUTION (per-name, not per-module)
# ============================================================

def build_name_import_map(project_dir, local_modules):
    """For each local module, find which NAMES other modules import from it.

    Returns: dict mapping module_name -> {imported_name: set(consumer_modules)}

    Example: imported_names['constants_new']['KM_PER_AU'] =
        {'apsidal_markers', 'idealized_orbits', ...}

    This lets us score a specific symbol rather than the whole module.
    """
    imported_names = defaultdict(lambda: defaultdict(set))

    for fname in os.listdir(project_dir):
        if not fname.endswith('.py'):
            continue
        consumer = fname[:-3]
        filepath = os.path.join(project_dir, fname)
        try:
            with open(filepath, 'rb') as f:
                tree = ast.parse(f.read())
        except Exception:
            continue

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module:
                mod_root = node.module.split('.')[0]
                if mod_root not in local_modules:
                    continue
                for alias in node.names:
                    name = alias.name
                    if name == '*':
                        imported_names[mod_root]['*'].add(consumer)
                    else:
                        imported_names[mod_root][name].add(consumer)

    return imported_names


def name_is_imported(name, module_name, imported_names):
    """Return (count, consumers) for a name defined in module_name.
    Star imports conservatively contribute as if the name were imported."""
    mod_imports = imported_names.get(module_name, {})
    consumers = set(mod_imports.get(name, set()))
    consumers |= mod_imports.get('*', set())
    return len(consumers), consumers


# ============================================================
# PROVENANCE UNIT MODEL
# ============================================================

class ProvenanceUnit:
    """The smallest thing that has a coherent source citation.

    Three kinds:
      - 'constant':  a module-level UPPER_CASE or Title_Case assignment
      - 'dict':      a module-level dict literal assignment
      - 'string':    a single string literal containing numeric claims
    """

    __slots__ = [
        'kind', 'module', 'file', 'name', 'line_start', 'line_end',
        'context_text',        # text the unit sees for citation lookup
        'entries',             # for dicts: [(key_name, value, value_str, line)]
        'numeric_claims',      # for strings: [(num_str, unit, value)]
        'value',               # for constants: the numeric value
        'value_str',
        'vuln', 'vuln_reason',
        'crit', 'crit_reason',
        'score',
        'role', 'consumer_count', 'consumers',
        'is_docstring',        # for strings: True if this is a module/class/func docstring
    ]

    def __init__(self, **kwargs):
        for k in self.__slots__:
            setattr(self, k, kwargs.get(k, None))
        if self.entries is None:
            self.entries = []
        if self.numeric_claims is None:
            self.numeric_claims = []
        if self.consumers is None:
            self.consumers = set()

    def compute_score(self):
        if self.vuln and self.crit:
            self.score = self.vuln * self.crit
        else:
            self.score = 0

    @property
    def display_name(self):
        if self.kind == 'dict':
            return f"{self.name}[...]" if self.name else "<anonymous dict>"
        if self.kind == 'string':
            return f"display string @ line {self.line_start}"
        return self.name or "<anonymous>"

    @property
    def short_value(self):
        if self.kind == 'constant':
            return str(self.value_str) if self.value_str else str(self.value)
        if self.kind == 'dict':
            n = len(self.entries)
            return f"({n} entr{'y' if n == 1 else 'ies'})"
        if self.kind == 'string':
            n = len(self.numeric_claims)
            return f"({n} claim{'s' if n != 1 else ''})"
        return ''


# ============================================================
# CONTEXT BLOCK EXTRACTION
# ============================================================

def get_context_block(lines, unit_start_line, unit_end_line=None,
                      lookback=30, lookahead=15):
    """Return the block of text a unit can see for citation purposes.

    Looks both directions from the unit:
      - `lookback` lines BEFORE the unit (for section-header citations)
      - the unit's declaration itself
      - `lookahead` lines AFTER the unit (for trailing `# Source:` comments,
        which is this codebase's dominant convention)

    Both directions matter. constants_new.py places citations AFTER the
    declaration ("KM_PER_AU = 149597870.7\\n# Source: IAU 2012 ..."),
    but section headers and dict-level citations tend to be ABOVE.
    """
    if unit_end_line is None:
        unit_end_line = unit_start_line
    start = max(0, unit_start_line - 1 - lookback)
    end = min(len(lines), unit_end_line + lookahead)
    return ''.join(lines[start:end])


def get_unit_interior(lines, line_start, line_end):
    """Return the text inside the unit itself (per-entry comments)."""
    start = max(0, line_start - 1)
    end = min(len(lines), line_end)
    return ''.join(lines[start:end])


# ============================================================
# AST-BASED UNIT EXTRACTION
# ============================================================

CONSTANT_NAME_SKIP = {
    'Path', 'Optional', 'Dict', 'List', 'Tuple', 'Set', 'Union',
    'Any', 'Callable', 'Iterator', 'Sequence', 'Mapping',
    'TYPE_CHECKING',
}


def extract_numeric_value(node):
    """Evaluate an AST node to a numeric constant.
    Returns (value, display_str) or (None, None) if not numeric."""
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)) and not isinstance(
                node.value, bool):
            return node.value, str(node.value)
        return None, None
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        v, s = extract_numeric_value(node.operand)
        if v is not None:
            return -v, f"-{s}"
    if isinstance(node, ast.BinOp):
        try:
            v = eval(compile(ast.Expression(node), '<eval>', 'eval'))
            if isinstance(v, (int, float)):
                src = ast.unparse(node) if hasattr(ast, 'unparse') else str(v)
                return v, src
        except Exception:
            return None, None
    return None, None


def extract_units_from_file(filepath, module_name, role):
    """Walk the AST of one file and emit ProvenanceUnits.

    Emits:
      - 'constant' units for top-level numeric assignments
      - 'dict' units for top-level dict literal assignments
      - 'string' units for string literals containing numeric claims
        (only in files expected to carry public-facing narrative)
    """
    units = []

    try:
        with open(filepath, 'rb') as f:
            source_bytes = f.read()
        tree = ast.parse(source_bytes)
    except Exception:
        return units

    try:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            lines = f.readlines()
    except Exception:
        return units

    fname = os.path.basename(filepath)

    # ---- Top-level assignments: constants and dicts ----
    for node in ast.iter_child_nodes(tree):
        if not isinstance(node, ast.Assign):
            continue
        if len(node.targets) != 1:
            continue
        target = node.targets[0]
        if not isinstance(target, ast.Name):
            continue
        name = target.id

        if isinstance(node.value, ast.Dict):
            unit = _make_dict_unit(node, name, lines, module_name,
                                    fname, role)
            if unit is not None:
                units.append(unit)
            continue

        # Numeric constant? Only UPPER_CASE / Title_Case names.
        looks_like_constant = (name.isupper() or
                               (name[0].isupper() and '_' in name))
        if not looks_like_constant:
            continue
        if name in CONSTANT_NAME_SKIP:
            continue

        value, value_str = extract_numeric_value(node.value)
        if value is None:
            continue

        line_start = node.lineno
        line_end = getattr(node, 'end_lineno', line_start) or line_start
        context_text = get_context_block(lines, line_start, line_end,
                                         lookback=30, lookahead=15)

        units.append(ProvenanceUnit(
            kind='constant',
            module=module_name,
            file=fname,
            name=name,
            line_start=line_start,
            line_end=line_end,
            context_text=context_text,
            value=value,
            value_str=value_str,
            role=role,
        ))

    # ---- String literals with numeric claims ----
    narrative_files = {
        'constants_new', 'info_dictionary', 'celestial_objects',
        'spacecraft_encounters', 'close_approach_data',
        'exoplanet_systems', 'exoplanet_stellar_properties',
        'sgr_a_star_data', 'star_notes', 'solar_visualization_shells',
    }
    is_shell_file = module_name.endswith('_visualization_shells')
    if module_name in narrative_files or is_shell_file:
        units.extend(_extract_string_units(
            tree, lines, module_name, fname, role))

    return units


def _make_dict_unit(assign_node, name, lines, module_name, fname, role):
    """Build a ProvenanceUnit for a top-level dict assignment."""
    dict_node = assign_node.value
    if not isinstance(dict_node, ast.Dict):
        return None

    line_start = assign_node.lineno
    line_end = getattr(dict_node, 'end_lineno', line_start) or line_start
    # For dicts the interior is captured separately; use the declaration
    # line as both start/end for lookahead so we catch trailing
    # `# Source:` comments that follow the closing brace.
    context_text = get_context_block(lines, line_start, line_end,
                                     lookback=30, lookahead=10)
    interior_text = get_unit_interior(lines, line_start, line_end)

    entries = []
    for key, val in zip(dict_node.keys, dict_node.values):
        if key is None:  # ** unpacking
            continue
        if not (isinstance(key, ast.Constant) and isinstance(key.value, str)):
            continue
        key_name = key.value
        num_value, num_str = extract_numeric_value(val)
        if num_value is None:
            # Accept None / other AST-constant values (e.g. period=None for
            # hyperbolic comets). Skip non-constants (colors as RGB tuples,
            # nested dicts, etc).
            if isinstance(val, ast.Constant):
                num_value = val.value
                num_str = repr(val.value) if val.value is not None else 'None'
            else:
                continue
        entry_line = getattr(val, 'lineno', line_start)
        entries.append((key_name, num_value, num_str, entry_line))

    if not entries:
        return None

    return ProvenanceUnit(
        kind='dict',
        module=module_name,
        file=fname,
        name=name,
        line_start=line_start,
        line_end=line_end,
        context_text=context_text + '\n' + interior_text,
        entries=entries,
        role=role,
    )


def _extract_string_units(tree, lines, module_name, fname, role):
    """Find string literals containing numeric claims. One string = one unit.

    Module/class/function docstrings are treated specially: their own text
    is included in the citation-search scope, so a docstring that mentions
    "Verified", "Source:", "per NASA", etc. is treated as self-cited.
    """
    # Identify docstring string nodes by position (first stmt of module /
    # class / function whose value is a Constant str).
    docstring_lines = set()

    def _collect_docstrings(n):
        body = getattr(n, 'body', None)
        if body and body:
            first = body[0]
            if (isinstance(first, ast.Expr) and
                isinstance(first.value, ast.Constant) and
                isinstance(first.value.value, str)):
                docstring_lines.add(first.value.lineno)
        for child in ast.iter_child_nodes(n):
            if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef,
                                   ast.ClassDef, ast.Module)):
                _collect_docstrings(child)

    _collect_docstrings(tree)

    units = []
    seen_lines = set()

    for node in ast.walk(tree):
        if not isinstance(node, ast.Constant):
            continue
        if not isinstance(node.value, str):
            continue
        s = node.value
        if len(s) < 3:
            continue
        claims = list(extract_numeric_claims(s))
        if not claims:
            continue

        line_start = node.lineno
        if line_start in seen_lines:
            continue
        seen_lines.add(line_start)
        line_end = getattr(node, 'end_lineno', line_start) or line_start

        # If this string is a docstring, include its own text in the
        # citation-search scope (docstrings self-contextualize).
        #
        # Lookback=60: info_dictionary.py INFO strings can be 50-100 lines
        # long. With lookback=30, continuation lines deep in a long entry
        # fall outside the citation window even when `# Source:` sits just
        # above the entry key. 60 lines covers the longest INFO entries
        # without false-positives in shorter files.
        # Known residual: very long entries (Apollo 11 S-IVB, Halley,
        # Artemis II) may still generate mid-string false positives if the
        # entry itself exceeds 60 lines. These are accepted scanner
        # limitations -- the citation exists at the entry key level.
        base_context = get_context_block(lines, line_start, line_end,
                                         lookback=60, lookahead=10)
        if line_start in docstring_lines:
            context_text = base_context + '\n' + s
        else:
            context_text = base_context

        units.append(ProvenanceUnit(
            kind='string',
            module=module_name,
            file=fname,
            name=None,
            line_start=line_start,
            line_end=line_end,
            context_text=context_text,
            numeric_claims=claims,
            role=role,
            is_docstring=(line_start in docstring_lines),
        ))

    return units


# ============================================================
# SCORING
# ============================================================

def score_unit(unit, imported_names):
    """Assign vulnerability and criticality to a unit."""
    # ---- Vulnerability ----
    text = unit.context_text or ''
    is_doc = bool(unit.is_docstring)
    cited = has_citation(text, is_docstring=is_doc)
    stale = has_stale_marker(text)

    if cited and stale:
        unit.vuln = V_STALE
        unit.vuln_reason = "Sourced but potentially stale"
    elif cited:
        unit.vuln = V_SOURCED
        unit.vuln_reason = "Has source citation"
    elif stale:
        unit.vuln = V_STALE
        unit.vuln_reason = "No source, contains date-sensitive claims"
    else:
        unit.vuln = V_RECALLED
        unit.vuln_reason = "No source citation (recalled)"

    # ---- Criticality ----
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

    unit.compute_score()


def _role_based_criticality(unit):
    """Fallback criticality when per-name resolution doesn't apply."""
    if unit.kind == 'dict' and unit.name:
        lname = unit.name.lower()
        if lname in ('colors',) or 'label' in lname or 'color' in lname:
            return C_COSMETIC, f"Cosmetic dictionary ({unit.name})"

    role = unit.role or ''
    if unit.kind == 'dict' and role.startswith('rendering'):
        return C_LOADBEARING, f"Geometry dict in {role} module"

    if unit.kind == 'constant' and role in ('computation', 'data'):
        return C_LOADBEARING, f"Numeric constant in {role} module"

    return C_INTERNAL, "Internal use (not imported externally)"


# ============================================================
# DUPLICATE / INCONSISTENCY DETECTION
# ============================================================
# Hand-curated aliases avoid both false positives and false negatives.
# Same-spelled names across files are caught; deliberately different
# names (CENTER_BODY_RADII_KM shadow) are NOT caught here -- that
# requires shadow detection (planned separately).

CONCEPT_ALIASES = {
    # Map canonical concept name -> tuple of exact name matches.
    # Matching is done by checking if the constant NAME equals any alias
    # (substring matching is too loose -- SPEED_OF_LIGHT_KM_S would
    # collide with SPEED_OF_LIGHT even though they're in different units).
    'SOLAR_RADIUS_KM':   ('SOLAR_RADIUS_KM', 'SUN_RADIUS_KM'),
    'SOLAR_RADIUS_AU':   ('SOLAR_RADIUS_AU', 'SUN_RADIUS_AU'),
    'KM_PER_AU':         ('KM_PER_AU', 'AU_TO_KM', 'AU_IN_KM'),
    'EARTH_RADIUS_KM':   ('EARTH_RADIUS_KM', 'EARTH_EQUATORIAL_RADIUS_KM'),
    'SPEED_OF_LIGHT_M_S': ('SPEED_OF_LIGHT',),  # m/s variant
    'SPEED_OF_LIGHT_KM_S': ('SPEED_OF_LIGHT_KM_S', 'C_KM_S'),
    'OBLIQUITY':         ('OBLIQUITY', 'EARTH_OBLIQUITY'),
    'LIGHT_MINUTES_PER_AU': ('LIGHT_MINUTES_PER_AU',),
    'JUPITER_RADIUS_KM': ('JUPITER_RADIUS_KM', 'JUPITER_EQUATORIAL_RADIUS_KM'),
}


def canonical_concept(name):
    """Map a constant name to its canonical concept, or None.
    Uses EXACT name match (not substring) to avoid unit-mismatch
    false positives like SPEED_OF_LIGHT vs SPEED_OF_LIGHT_KM_S."""
    up = name.upper()
    for concept, aliases in CONCEPT_ALIASES.items():
        if up in aliases:
            return concept
    return None


def find_cross_file_issues(units):
    """Find same-concept constants across multiple files.
    Returns (consistent_dups, inconsistencies)."""
    by_concept = defaultdict(list)
    for u in units:
        if u.kind != 'constant' or u.name is None:
            continue
        concept = canonical_concept(u.name)
        if concept:
            by_concept[concept].append(u)

    consistent_dups = []
    inconsistencies = []

    for concept, group in by_concept.items():
        if len(group) < 2:
            continue
        files = set(u.file for u in group)
        if len(files) < 2:
            continue
        values = set()
        for u in group:
            try:
                values.add(round(float(u.value), 6))
            except (TypeError, ValueError):
                values.add(u.value)
        entry = {
            'concept': concept,
            'units': group,
            'files': files,
            'values': values,
        }
        if len(values) == 1:
            consistent_dups.append(entry)
        else:
            inconsistencies.append(entry)

    return consistent_dups, inconsistencies


# ============================================================
# MAIN SCAN
# ============================================================

def scan_project(project_dir, output_path='PROVENANCE_AUDIT.md'):
    """Scan all .py files and produce the provenance audit report."""
    print(f"Provenance Scanner -- scanning {project_dir}")
    print()

    deps, consumers, local_modules = build_dependency_graph(project_dir)
    imported_names = build_name_import_map(project_dir, local_modules)

    all_units = []
    files_scanned = 0

    for fname in sorted(os.listdir(project_dir)):
        if not fname.endswith('.py'):
            continue
        filepath = os.path.join(project_dir, fname)
        module_name = fname[:-3]
        role = classify_role(module_name)

        units = extract_units_from_file(filepath, module_name, role)
        for u in units:
            score_unit(u, imported_names)
        all_units.extend(units)
        files_scanned += 1

    consistent_dups, inconsistencies = find_cross_file_issues(all_units)

    generate_report(all_units, consistent_dups, inconsistencies,
                    files_scanned, project_dir, output_path)

    return all_units, consistent_dups, inconsistencies


# ============================================================
# REPORT GENERATION
# ============================================================

def generate_report(units, consistent_dups, inconsistencies,
                    files_scanned, project_dir, output_path):
    """Write PROVENANCE_AUDIT.md."""
    now = datetime.now().strftime('%B %d, %Y')

    scored = [u for u in units if u.score and u.score > 0]
    scored.sort(key=lambda u: (-u.score, u.file, u.line_start))

    tier_counts = defaultdict(int)
    for u in scored:
        tier_counts[action_tier(u.score)] += 1

    kind_counts = defaultdict(int)
    for u in scored:
        kind_counts[u.kind] += 1

    out = []

    # ---- Header ----
    out.append("# Paloma's Orrery -- Provenance Audit")
    out.append("")
    out.append(f"Generated: {now}")
    out.append(f"Files scanned: {files_scanned}")
    out.append(f"Total findings: {len(scored)}")
    out.append(f"Constants: {kind_counts.get('constant', 0)} | "
               f"Dicts: {kind_counts.get('dict', 0)} | "
               f"Display strings: {kind_counts.get('string', 0)}")
    out.append("")
    out.append("Unit of provenance: the smallest thing with a coherent "
               "source citation. A dict with one block-level `# Source:` "
               "comment is ONE unit; all its entries inherit that citation. "
               "A hover string with co-referring numbers is ONE unit.")
    out.append("")
    out.append("---")
    out.append("")

    # ---- Risk matrix ----
    out.append("## Risk Matrix: Vulnerability x Criticality")
    out.append("")
    out.append("**Vulnerability** (how likely to be wrong):")
    out.append("- 1 = Fetched (authoritative pipeline)")
    out.append("- 2 = Sourced (has citation)")
    out.append("- 3 = Stale (may have changed)")
    out.append("- 4 = Recalled (LLM training data, no citation)")
    out.append("")
    out.append("**Criticality** (impact if wrong):")
    out.append("- 1 = Cosmetic (colors, labels)")
    out.append("- 2 = Internal (used but not imported elsewhere)")
    out.append("- 3 = Load-bearing (drives geometry) or imported 1-2x")
    out.append("- 4 = Public-facing (hover text, gallery)")
    out.append("- 5 = Propagating (imported by 3+ modules)")
    out.append("")
    out.append("**Score = V x C** | Action thresholds:")
    out.append("- 16-20: FIX NOW")
    out.append("- 10-15: FIX NEXT SESSION")
    out.append("- 5-9: ADD SOURCE WHEN TOUCHED")
    out.append("- 1-4: NO ACTION NEEDED")
    out.append("")
    out.append("---")
    out.append("")

    # ---- Priority summary ----
    out.append("## Priority Summary")
    out.append("")
    out.append("| Tier | Score | Action | Count |")
    out.append("|------|-------|--------|------:|")
    tier_labels = {
        1: ("16-20", "FIX NOW"),
        2: ("10-15", "FIX NEXT SESSION"),
        3: ("5-9", "ADD SOURCE WHEN TOUCHED"),
        4: ("1-4", "NO ACTION NEEDED"),
    }
    for tier in [1, 2, 3, 4]:
        score_range, action = tier_labels[tier]
        count = tier_counts.get(tier, 0)
        out.append(f"| {tier} | {score_range} | {action} | {count} |")
    out.append("")
    out.append("---")
    out.append("")

    # ---- Inconsistencies (highest priority) ----
    if inconsistencies:
        out.append("## INCONSISTENCIES (Same concept, different values)")
        out.append("")
        out.append("Highest-risk findings: the same physical concept has ")
        out.append("different numeric values in different files.")
        out.append("")
        for entry in inconsistencies:
            out.append(f"### {entry['concept']}")
            out.append("")
            out.append(f"**Values found:** " +
                       ", ".join(str(v) for v in sorted(entry['values'])))
            out.append(f"**Files:** " + ", ".join(sorted(entry['files'])))
            out.append("")
            for u in sorted(entry['units'],
                            key=lambda x: (x.file, x.line_start)):
                out.append(f"- `{u.file}:{u.line_start}` -- "
                           f"`{u.name} = {u.value_str}`")
            out.append("")
            out.append("**Action:** Determine correct value with citation. "
                       "Consolidate to single source of truth in "
                       "constants_new.py. Replace duplicates with imports.")
            out.append("")
        out.append("---")
        out.append("")
    else:
        out.append("## INCONSISTENCIES")
        out.append("")
        out.append("None detected. No same-concept constants with differing ")
        out.append("values found across files.")
        out.append("")
        out.append("Note: this does NOT rule out silent shadowing (a local ")
        out.append("dict with different name but overlapping keys). That ")
        out.append("pattern is the April 16 bug family; shadow detection ")
        out.append("is planned for a future session.")
        out.append("")
        out.append("---")
        out.append("")

    # ---- Consistent duplicates ----
    if consistent_dups:
        out.append("## DUPLICATES (Same value, multiple files)")
        out.append("")
        out.append("Consistent values defined in multiple places rather ")
        out.append("than imported from one source. Consolidation candidates.")
        out.append("")
        for entry in consistent_dups:
            val = list(entry['values'])[0]
            files_str = ", ".join(sorted(entry['files']))
            out.append(f"- **{entry['concept']}** = {val} -- in {files_str}")
        out.append("")
        out.append("**Action:** Consolidate to constants_new.py and import.")
        out.append("")
        out.append("---")
        out.append("")

    # ---- Per-tier findings ----
    for tier in [1, 2, 3, 4]:
        tier_units = [u for u in scored if action_tier(u.score) == tier]
        if not tier_units:
            continue
        score_range, action = tier_labels[tier]
        out.append(f"## Tier {tier}: {action} (Score {score_range})")
        out.append("")

        by_file = defaultdict(list)
        for u in tier_units:
            by_file[u.file].append(u)

        for fname in sorted(by_file.keys()):
            out.append(f"### {fname}")
            out.append("")
            out.append("| Line | Kind | Name | Size/Value | V | C | "
                       "Score | Vulnerability | Criticality |")
            out.append("|-----:|------|------|------------|--:|--:|"
                       "------:|---------------|-------------|")
            for u in sorted(by_file[fname], key=lambda x: -x.score):
                name = u.display_name[:40]
                val = u.short_value[:20]
                out.append(
                    f"| {u.line_start} | {u.kind} | {name} | {val} | "
                    f"{u.vuln} | {u.crit} | **{u.score}** | "
                    f"{u.vuln_reason} | {u.crit_reason} |"
                )
            out.append("")
        out.append("---")
        out.append("")

    # ---- Footer ----
    out.append("## How to Use This Audit")
    out.append("")
    out.append("1. Start with INCONSISTENCIES -- these are confirmed problems.")
    out.append("2. Work through Tier 1 (FIX NOW) findings.")
    out.append("3. For each finding:")
    out.append("   a. Locate the correct value from an authoritative source.")
    out.append("   b. Update constants_new.py (or info_dictionary.py).")
    out.append("   c. Add a `# Source:` comment above the declaration.")
    out.append("   d. Replace local copies with imports.")
    out.append("   e. Verify downstream plots unchanged.")
    out.append("4. Re-run this scanner to confirm fixes.")
    out.append("")
    out.append("Companion tools:")
    out.append("- module_atlas.py              -- dependency graph")
    out.append("- test_constants_provenance.py -- pin constants_new.py values")
    out.append("- dep_trace.py                 -- per-module import tracing")
    out.append("")
    out.append("---")
    out.append("")
    out.append("*Generated by provenance_scanner.py -- "
               "Paloma's Orrery Developer Tools*")
    out.append("")

    content = "\n".join(out)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Audit written to {output_path}")
    print(f"  {len(scored)} findings across {files_scanned} files")
    print()
    print("Priority summary:")
    for tier in [1, 2, 3, 4]:
        score_range, action = tier_labels[tier]
        count = tier_counts.get(tier, 0)
        print(f"  Tier {tier} ({score_range}): {count:5d} findings -- {action}")

    if inconsistencies:
        print()
        print(f"  *** {len(inconsistencies)} INCONSISTENCIES detected ***")
    if consistent_dups:
        print(f"  {len(consistent_dups)} consistent duplicates "
              f"(consolidation candidates)")


# ============================================================
# CLI
# ============================================================

def main():
    project_dir = '.'
    output_path = 'PROVENANCE_AUDIT.md'

    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == '--output' and i + 1 < len(args):
            output_path = args[i + 1]
            i += 2
        elif not args[i].startswith('-'):
            project_dir = args[i]
            i += 1
        else:
            i += 1

    if not os.path.isdir(project_dir):
        print(f"ERROR: '{project_dir}' is not a directory")
        sys.exit(1)

    scan_project(project_dir, output_path)


if __name__ == '__main__':
    main()
