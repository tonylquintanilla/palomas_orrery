"""
provenance_scanner.py - Fact provenance auditor for Paloma's Orrery.

Scans every .py file in the project for hardcoded constants, dictionary
values, and numeric claims in strings. Scores each finding by
Vulnerability x Criticality to prioritize verification. Detects
duplicates and value inconsistencies across files.

Companion tool to module_atlas.py: uses the same dependency graph to
determine criticality (propagating constants score highest).

Key functions:
    scan_project() - main entry point, produces PROVENANCE_AUDIT.md
    scan_file_constants() - extract named constants and dict values
    scan_file_string_claims() - extract numeric claims from strings
    find_duplicates() - group same-value constants across files
    score_finding() - compute V x C risk score

Usage:
    python provenance_scanner.py                   # scan current directory
    python provenance_scanner.py /path/to/project  # scan specific directory
    python provenance_scanner.py --output audit.md # custom output filename

Module updated: April 2026 with Anthropic's Claude Opus 4.6
"""

import ast
import os
import re
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

# Reuse the atlas dependency graph builder
from module_atlas import build_dependency_graph, classify_role


# ============================================================
# VULNERABILITY SCORES
# ============================================================
# How likely is this fact to be wrong?

V_FETCHED  = 1   # From authoritative pipeline at runtime
V_SOURCED  = 2   # Hardcoded but has citation
V_STALE    = 3   # Was sourced but may have changed
V_RECALLED = 4   # From LLM training data, no citation

# ============================================================
# CRITICALITY SCORES
# ============================================================
# What's the impact if it IS wrong?

C_COSMETIC    = 1   # Colors, label positions, descriptive text
C_INTERNAL    = 2   # Used in code but not displayed
C_LOADBEARING = 3   # Drives geometry, shell radii, orbit params
C_PUBLIC      = 4   # Visible in hover text, gallery, Instagram
C_PROPAGATING = 5   # Imported by other modules, affects calculations

# ============================================================
# ACTION THRESHOLDS
# ============================================================

THRESHOLD_LABELS = {
    (16, 20): "FIX NOW -- Source, verify, consolidate",
    (10, 15): "FIX NEXT SESSION -- Add citation",
    (5, 9):   "ADD SOURCE WHEN TOUCHED",
    (1, 4):   "NO ACTION NEEDED",
}

def action_label(score):
    """Return action string for a given V x C score."""
    for (lo, hi), label in THRESHOLD_LABELS.items():
        if lo <= score <= hi:
            return label
    return "UNKNOWN"

def action_tier(score):
    """Return tier number (1=highest priority) for sorting."""
    if score >= 16: return 1
    if score >= 10: return 2
    if score >= 5:  return 3
    return 4


# ============================================================
# SOURCE DETECTION
# ============================================================

# Patterns that indicate a value has a source citation
SOURCE_PATTERNS = [
    re.compile(r'#\s*[Ss]ource:', re.IGNORECASE),
    re.compile(r'#\s*(?:IAU|JPL|NASA|ESA|NIST|Horizons|arXiv|doi)', re.IGNORECASE),
    re.compile(r'#\s*https?://', re.IGNORECASE),
    re.compile(r'#\s*(?:Verified|Confirmed)\s+(?:from|via|against)', re.IGNORECASE),
    re.compile(r'#\s*(?:Based on)\s+arXiv', re.IGNORECASE),
    re.compile(r'#\s*(?:From JPL|Per JPL|JPL uses)', re.IGNORECASE),
]

# Patterns that indicate staleness
STALE_PATTERNS = [
    re.compile(r'(?:as of|current|currently|latest|updated)\s+\d{4}', re.IGNORECASE),
    re.compile(r'(?:2024|2025|2026)\s*[-:]', re.IGNORECASE),
    re.compile(r'(?:Planned|Expected|Upcoming|scheduled)', re.IGNORECASE),
    re.compile(r'(?:Still active|Present\))', re.IGNORECASE),
]

# Patterns for numeric claims in strings (hover text, INFO dicts)
# Matches: number + unit pattern like "8.33 R_sun", "0.039 AU", "695700 km"
NUMERIC_CLAIM_RE = re.compile(
    r'(\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)\s*'
    r'(R_sun|AU|km|km/s|m/s|deg|degrees?|solar radii|'
    r'Earth (?:masses|radii)|M_sun|ly|light[- ]years?|'
    r'days?|years?|hours?|minutes?|arcsec|mas|pc|kpc|Mpc|'
    r'K|kg|g/cm3|g/cc|km/h|mph)\b',
    re.IGNORECASE
)


def has_source_citation(line_text, context_lines):
    """Check if a constant has a source citation on same or adjacent lines."""
    all_text = line_text + ' '.join(context_lines)
    for pat in SOURCE_PATTERNS:
        if pat.search(all_text):
            return True
    return False


def has_stale_markers(line_text, context_lines):
    """Check if a value has markers suggesting it may be stale."""
    all_text = line_text + ' '.join(context_lines)
    for pat in STALE_PATTERNS:
        if pat.search(all_text):
            return True
    return False


def assess_vulnerability(line_text, context_lines):
    """Determine vulnerability score for a finding."""
    if has_source_citation(line_text, context_lines):
        if has_stale_markers(line_text, context_lines):
            return V_STALE, "Sourced but potentially stale"
        return V_SOURCED, "Has source citation"
    if has_stale_markers(line_text, context_lines):
        return V_STALE, "No source, contains date-sensitive claims"
    return V_RECALLED, "No source citation (recalled)"


# ============================================================
# CRITICALITY ASSESSMENT
# ============================================================

def assess_criticality(module_name, finding_type, consumer_count, role):
    """Determine criticality score for a finding.
    
    Args:
        module_name: which module the finding is in
        finding_type: 'constant', 'dict_value', 'string_claim'
        consumer_count: how many modules import this module
        role: module role from atlas (data, rendering, etc.)
    """
    # Propagating: defined in a module imported by many others
    if consumer_count >= 3 and finding_type in ('constant', 'dict_value'):
        return C_PROPAGATING, f"Imported by {consumer_count} modules"
    
    # Public-facing: in hover text, INFO dicts, or rendering modules
    if finding_type == 'string_claim':
        return C_PUBLIC, "In display string (hover text / INFO)"
    
    # Shell/rendering modules with dict values = load-bearing geometry
    if role in ('rendering/shells', 'rendering') and finding_type == 'dict_value':
        return C_LOADBEARING, f"Geometry value in {role} module"
    
    # Data modules with constants = likely imported
    if role == 'data' and finding_type == 'constant':
        if consumer_count >= 1:
            return C_PROPAGATING, f"Data constant imported by {consumer_count} modules"
        return C_LOADBEARING, "Data constant (potential import target)"
    
    # Computation modules = load-bearing
    if role == 'computation':
        return C_LOADBEARING, f"Value in computation module"
    
    # Colors, labels, positions
    if module_name == 'constants_new' and finding_type == 'dict_value':
        # Could be color_map (cosmetic) or CENTER_BODY_RADII (propagating)
        return C_LOADBEARING, "Dictionary value in constants module"
    
    # Default
    return C_INTERNAL, "Internal use"


# ============================================================
# FILE SCANNING
# ============================================================

class Finding:
    """A single auditable fact found in the codebase."""
    __slots__ = [
        'file', 'line', 'name', 'value', 'value_str',
        'finding_type', 'context', 'vuln', 'vuln_reason',
        'crit', 'crit_reason', 'score', 'dict_name',
    ]
    
    def __init__(self, **kwargs):
        for k in self.__slots__:
            setattr(self, k, kwargs.get(k, ''))
        if self.vuln and self.crit:
            self.score = self.vuln * self.crit
        else:
            self.score = 0

    def __repr__(self):
        return f"Finding({self.file}:{self.line} {self.name}={self.value_str} score={self.score})"


def get_context_lines(lines, lineno, window=2):
    """Get surrounding lines for context (0-indexed lineno)."""
    start = max(0, lineno - window)
    end = min(len(lines), lineno + window + 1)
    return [lines[i] for i in range(start, end)]


def scan_file_constants(filepath, lines):
    """Extract named constants (module-level assignments to UPPER_CASE names).
    
    Finds patterns like:
        SOLAR_RADIUS_AU = 0.00465047
        KM_PER_AU = 149597870.7
    """
    findings = []
    
    try:
        with open(filepath, 'rb') as f:
            tree = ast.parse(f.read())
    except Exception:
        return findings
    
    for node in ast.iter_child_nodes(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    name = target.id
                    # Only UPPER_CASE or Title_Case constants
                    if not (name.isupper() or 
                            (name[0].isupper() and '_' in name)):
                        continue
                    # Skip class definitions, imports, etc.
                    if name in ('Path', 'Optional', 'Dict', 'List', 'Tuple'):
                        continue
                    
                    # Try to extract the value
                    value, value_str = extract_value(node.value, lines, node.lineno - 1)
                    if value is None:
                        continue
                    
                    # Skip non-numeric constants (strings, booleans, etc.)
                    if not isinstance(value, (int, float)):
                        continue
                    
                    context = get_context_lines(lines, node.lineno - 1)
                    line_text = lines[node.lineno - 1] if node.lineno - 1 < len(lines) else ''
                    
                    findings.append(Finding(
                        file=os.path.basename(filepath),
                        line=node.lineno,
                        name=name,
                        value=value,
                        value_str=value_str,
                        finding_type='constant',
                        context=context,
                    ))
    
    return findings


def extract_value(node, lines, lineno):
    """Try to extract a numeric value from an AST node."""
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value, str(node.value)
    elif isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        val, vs = extract_value(node.operand, lines, lineno)
        if val is not None:
            return -val, f"-{vs}"
    elif isinstance(node, ast.BinOp):
        # Try to evaluate simple expressions like 558.0 * 365.25
        try:
            line = lines[lineno] if lineno < len(lines) else ''
            # Find the expression in the line
            code = ast.get_source_segment(line.encode() if isinstance(line, str) else line, node)
            if code:
                val = eval(compile(ast.Expression(node), '<eval>', 'eval'))
                if isinstance(val, (int, float)):
                    return val, code.decode() if isinstance(code, bytes) else code
        except Exception:
            pass
    return None, None


def scan_file_dicts(filepath, lines):
    """Extract numeric values from dictionary literals.
    
    Finds patterns like:
        'Sun': 696340,
        'Mercury': 2440,
    """
    findings = []
    
    try:
        with open(filepath, 'rb') as f:
            source = f.read()
        tree = ast.parse(source)
    except Exception:
        return findings
    
    for node in ast.walk(tree):
        if isinstance(node, ast.Dict):
            # Find the parent assignment to get the dict name
            dict_name = _find_dict_name(tree, node)
            
            for key, val in zip(node.keys, node.values):
                if key is None:
                    continue
                # Get the key name
                if isinstance(key, ast.Constant) and isinstance(key.value, str):
                    key_name = key.value
                else:
                    continue
                
                # Get the value
                value, value_str = extract_value(val, lines, 
                    val.lineno - 1 if hasattr(val, 'lineno') else 0)
                if value is None:
                    continue
                if not isinstance(value, (int, float)):
                    continue
                
                lineno = val.lineno if hasattr(val, 'lineno') else 0
                context = get_context_lines(lines, lineno - 1) if lineno > 0 else []
                line_text = lines[lineno - 1] if 0 < lineno <= len(lines) else ''
                
                findings.append(Finding(
                    file=os.path.basename(filepath),
                    line=lineno,
                    name=f"{dict_name}['{key_name}']" if dict_name else f"'{key_name}'",
                    value=value,
                    value_str=value_str,
                    finding_type='dict_value',
                    context=context,
                    dict_name=dict_name or '',
                ))
    
    return findings


def _find_dict_name(tree, dict_node):
    """Find the variable name a dict is assigned to."""
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            if node.value is dict_node:
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        return target.id
    return None


def scan_file_string_claims(filepath, lines):
    """Extract numeric claims from string literals.
    
    Finds patterns like "8.33 R_sun", "0.039 AU", "18.8 R_sun" in
    hover text, INFO dicts, and docstrings.
    """
    findings = []
    
    # Scan all lines for string content with numeric claims
    in_string = False
    string_lines = []
    
    for i, line in enumerate(lines):
        # Look for numeric claims in any line that looks like string content
        # (inside quotes, triple quotes, or string continuation)
        matches = NUMERIC_CLAIM_RE.finditer(line)
        for m in matches:
            num_str = m.group(1)
            unit = m.group(2)
            try:
                value = float(num_str)
            except ValueError:
                continue
            
            # Skip very common/trivial values
            if value in (0, 1, 2, 3) and unit.lower() in ('days', 'years', 'hours'):
                continue
            
            context = get_context_lines(lines, i)
            
            # Try to identify what this claim is about from context
            claim_context = line.strip()[:120]
            
            findings.append(Finding(
                file=os.path.basename(filepath),
                line=i + 1,
                name=f"claim: {num_str} {unit}",
                value=value,
                value_str=f"{num_str} {unit}",
                finding_type='string_claim',
                context=context,
            ))
    
    return findings


# ============================================================
# DUPLICATE DETECTION
# ============================================================

def find_duplicates(all_findings):
    """Group findings by concept to detect duplicates and inconsistencies.
    
    Returns list of DuplicateGroup objects.
    """
    # Group by normalized name
    by_concept = defaultdict(list)
    
    for f in all_findings:
        if f.finding_type == 'string_claim':
            continue  # Don't duplicate-check string claims
        
        # Normalize the concept name
        concept = normalize_concept(f.name, f.value)
        if concept:
            by_concept[concept].append(f)
    
    # Also group by exact numeric value for cross-reference
    by_value = defaultdict(list)
    for f in all_findings:
        if f.finding_type == 'string_claim':
            continue
        if isinstance(f.value, (int, float)) and f.value != 0:
            # Round to avoid float precision issues
            key = round(f.value, 6)
            by_value[key].append(f)
    
    duplicates = []
    seen_concepts = set()
    
    for concept, findings in by_concept.items():
        if len(findings) > 1:
            files = set(f.file for f in findings)
            if len(files) > 1:  # Same concept in different files
                values = set(round(f.value, 6) for f in findings)
                duplicates.append({
                    'concept': concept,
                    'findings': findings,
                    'files': files,
                    'consistent': len(values) == 1,
                    'values': values,
                })
    
    return duplicates


def normalize_concept(name, value):
    """Normalize a constant name to a concept for duplicate detection.
    
    Only groups things that genuinely represent the SAME physical quantity.
    Dictionary entries like period_days for different planets are NOT 
    the same concept -- they're per-object properties.
    """
    name_upper = name.upper()
    
    # Known concept families -- physical constants that should be unique
    if 'SOLAR_RADIUS' in name_upper or 'SUN_RADIUS' in name_upper:
        return 'SOLAR_RADIUS'
    if 'KM_PER_AU' in name_upper or 'AU_TO_KM' in name_upper:
        return 'KM_PER_AU'
    if 'EARTH_RADIUS' in name_upper:
        return 'EARTH_RADIUS'
    if 'OBLIQUITY' in name_upper:
        return 'OBLIQUITY'
    
    # Dictionary entries: only flag if the dict key is a unique object name
    # AND the same object appears in multiple files with different values.
    # Keys like 'period_days', 'semi_major_axis_au' are per-object properties
    # that legitimately differ -- skip those.
    if '[' in name:
        # Extract dict_name['key'] -> only track if key is an object name
        # (like CENTER_BODY_RADII['Sun']) not a property name
        # (like exoplanet_data['period_days'])
        match = re.match(r"(\w+)\['(.+)'\]", name)
        if match:
            dict_name, key = match.groups()
            # Per-object property keys -- these SHOULD differ per planet
            per_object_keys = {
                'semi_major_axis_au', 'period_days', 'eccentricity',
                'inclination', 'mass_earth', 'radius_earth',
                'in_habitable_zone', 'mass_kg', 'mass_solar',
                'radius_solar', 'temp_k', 'luminosity_solar',
                'spectral_type', 'discovery_method', 'discovery_year',
                # Shell properties -- differ per planet by design
                'radius_fraction', 'opacity', 'color',
                'sunward_distance', 'equatorial_radius', 'polar_radius',
                'tail_length', 'tail_base_radius', 'tail_end_radius',
                'offset_x', 'offset_y', 'offset_z',
                'n_points', 'label', 'description',
            }
            if key in per_object_keys:
                return None  # Not a duplicate concept
            
            # Same object in same-named dict across files IS a duplicate
            return f"{dict_name}['{key}']"
        return None
    
    # Named constants (UPPER_CASE)
    if name.isupper() or (name[0].isupper() and '_' in name):
        return name
    
    return None


# ============================================================
# KNOWN SKIP LISTS
# ============================================================

# Dictionaries that are purely cosmetic (colors, label positions)
COSMETIC_DICTS = {
    'colors',           # in color_map()
    'stellar_class_labels',
}

# Dictionaries with values from authoritative sources
FETCHED_DICTS = {
    # (none currently -- but can be added as pipeline sources are identified)
}

def is_cosmetic_dict(dict_name):
    """Check if a dictionary is known to be cosmetic."""
    if not dict_name:
        return False
    return dict_name.lower() in COSMETIC_DICTS or dict_name == 'colors'


# ============================================================
# MAIN SCANNER
# ============================================================

def scan_project(project_dir, output_path='PROVENANCE_AUDIT.md'):
    """Scan all .py files and produce the provenance audit report."""
    
    print(f"Provenance Scanner -- scanning {project_dir}")
    print()
    
    # Build dependency graph (reuse from module_atlas)
    deps, consumers, local_modules = build_dependency_graph(project_dir)
    
    # Scan all files
    all_findings = []
    files_scanned = 0
    
    for fname in sorted(os.listdir(project_dir)):
        if not fname.endswith('.py'):
            continue
        
        filepath = os.path.join(project_dir, fname)
        module_name = fname[:-3]
        role = classify_role(module_name)
        consumer_count = len(consumers.get(module_name, set()))
        
        # Read file lines
        try:
            with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
                lines = f.readlines()
        except Exception:
            continue
        
        files_scanned += 1
        
        # Scan for constants
        constants = scan_file_constants(filepath, lines)
        
        # Scan for dictionary values
        dict_values = scan_file_dicts(filepath, lines)
        
        # Scan for string claims (only in files with INFO dicts or shell descriptions)
        string_claims = []
        # Only scan files likely to contain factual hover text / descriptions
        string_scan_files = {
            'constants_new', 'celestial_objects', 'spacecraft_encounters',
            'close_approach_data', 'exoplanet_systems', 'exoplanet_stellar_properties',
            'sgr_a_star_data', 'star_notes',
        }
        is_shell_file = module_name.endswith('_visualization_shells')
        if module_name in string_scan_files or is_shell_file:
            string_claims = scan_file_string_claims(filepath, lines)
        
        # Score all findings
        for f in constants + dict_values + string_claims:
            line_text = lines[f.line - 1] if 0 < f.line <= len(lines) else ''
            context = get_context_lines(lines, f.line - 1) if f.line > 0 else []
            
            # Vulnerability
            v, v_reason = assess_vulnerability(line_text, context)
            
            # Override for cosmetic dicts
            if f.finding_type == 'dict_value' and is_cosmetic_dict(f.dict_name):
                f.crit = C_COSMETIC
                f.crit_reason = "Cosmetic dictionary (colors/labels)"
            else:
                # Criticality from atlas
                c, c_reason = assess_criticality(
                    module_name, f.finding_type, consumer_count, role)
                f.crit = c
                f.crit_reason = c_reason
            
            f.vuln = v
            f.vuln_reason = v_reason
            f.score = f.vuln * f.crit
        
        all_findings.extend(constants + dict_values + string_claims)
    
    # Find duplicates
    duplicates = find_duplicates(all_findings)
    
    # Generate report
    generate_report(all_findings, duplicates, consumers, 
                    files_scanned, project_dir, output_path)
    
    return all_findings, duplicates


def generate_report(findings, duplicates, consumers, files_scanned,
                    project_dir, output_path):
    """Write PROVENANCE_AUDIT.md."""
    
    now = datetime.now().strftime('%B %d, %Y')
    
    # Sort findings by score descending
    scored = [f for f in findings if f.score > 0]
    scored.sort(key=lambda f: (-f.score, f.file, f.line))
    
    # Count by tier
    tier_counts = defaultdict(int)
    for f in scored:
        tier_counts[action_tier(f.score)] += 1
    
    # Count by type
    type_counts = defaultdict(int)
    for f in scored:
        type_counts[f.finding_type] += 1
    
    lines = []
    
    # Header
    lines.append("# Paloma's Orrery -- Provenance Audit")
    lines.append("")
    lines.append(f"Generated: {now}")
    lines.append(f"Files scanned: {files_scanned}")
    lines.append(f"Total findings: {len(scored)}")
    lines.append(f"Constants: {type_counts.get('constant', 0)} | "
                 f"Dict values: {type_counts.get('dict_value', 0)} | "
                 f"String claims: {type_counts.get('string_claim', 0)}")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # Risk matrix explanation
    lines.append("## Risk Matrix: Vulnerability x Criticality")
    lines.append("")
    lines.append("**Vulnerability** (how likely to be wrong):")
    lines.append("- 1 = Fetched (authoritative pipeline)")
    lines.append("- 2 = Sourced (has citation)")
    lines.append("- 3 = Stale (may have changed)")
    lines.append("- 4 = Recalled (LLM training data, no citation)")
    lines.append("")
    lines.append("**Criticality** (impact if wrong):")
    lines.append("- 1 = Cosmetic (colors, labels)")
    lines.append("- 2 = Internal (used but not displayed)")
    lines.append("- 3 = Load-bearing (drives geometry)")
    lines.append("- 4 = Public-facing (hover text, gallery)")
    lines.append("- 5 = Propagating (imported by other modules)")
    lines.append("")
    lines.append("**Score = V x C** | Action thresholds:")
    lines.append("- 16-20: FIX NOW")
    lines.append("- 10-15: FIX NEXT SESSION")
    lines.append("- 5-9: ADD SOURCE WHEN TOUCHED")
    lines.append("- 1-4: NO ACTION NEEDED")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # Summary by tier
    lines.append("## Priority Summary")
    lines.append("")
    lines.append("| Tier | Score | Action | Count |")
    lines.append("|------|-------|--------|------:|")
    tier_labels = {
        1: ("16-20", "FIX NOW"),
        2: ("10-15", "FIX NEXT SESSION"),
        3: ("5-9", "ADD SOURCE WHEN TOUCHED"),
        4: ("1-4", "NO ACTION NEEDED"),
    }
    for tier in [1, 2, 3, 4]:
        score_range, action = tier_labels[tier]
        count = tier_counts.get(tier, 0)
        lines.append(f"| {tier} | {score_range} | {action} | {count} |")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # Duplicates / Inconsistencies section (highest priority)
    if duplicates:
        inconsistent = [d for d in duplicates if not d['consistent']]
        consistent_dups = [d for d in duplicates if d['consistent']]
        
        if inconsistent:
            lines.append("## INCONSISTENCIES (Same concept, different values)")
            lines.append("")
            lines.append("These are the highest-risk findings: the same physical")
            lines.append("concept has different numeric values in different files.")
            lines.append("")
            
            for dup in inconsistent:
                lines.append(f"### {dup['concept']}")
                lines.append("")
                lines.append(f"**Values found:** {', '.join(str(v) for v in sorted(dup['values']))}")
                lines.append(f"**Files:** {', '.join(sorted(dup['files']))}")
                lines.append("")
                for f in sorted(dup['findings'], key=lambda x: (x.file, x.line)):
                    lines.append(f"- `{f.file}:{f.line}` -- `{f.name} = {f.value_str}`")
                lines.append("")
                lines.append("**Action:** Determine correct value with citation. "
                             "Consolidate to single source of truth in constants_new.py. "
                             "Replace duplicates with imports.")
                lines.append("")
            
            lines.append("---")
            lines.append("")
        
        if consistent_dups:
            lines.append("## DUPLICATES (Same value, multiple files)")
            lines.append("")
            lines.append("These constants have consistent values but are defined")
            lines.append("in multiple files instead of imported from one source.")
            lines.append("")
            
            for dup in consistent_dups:
                files_str = ', '.join(sorted(dup['files']))
                val = list(dup['values'])[0]
                lines.append(f"- **{dup['concept']}** = {val} -- in {files_str}")
            lines.append("")
            lines.append("**Action:** Consolidate to constants_new.py and import.")
            lines.append("")
            lines.append("---")
            lines.append("")
    
    # Findings by tier
    for tier in [1, 2, 3, 4]:
        tier_findings = [f for f in scored if action_tier(f.score) == tier]
        if not tier_findings:
            continue
        
        score_range, action = tier_labels[tier]
        lines.append(f"## Tier {tier}: {action} (Score {score_range})")
        lines.append("")
        
        # Group by file within tier
        by_file = defaultdict(list)
        for f in tier_findings:
            by_file[f.file].append(f)
        
        for fname in sorted(by_file.keys()):
            file_findings = by_file[fname]
            lines.append(f"### {fname}")
            lines.append("")
            lines.append(f"| Line | Name | Value | V | C | Score | Vulnerability | Criticality |")
            lines.append(f"|-----:|------|-------|--:|--:|------:|---------------|-------------|")
            
            for f in sorted(file_findings, key=lambda x: -x.score):
                name_short = f.name[:40]
                val_short = str(f.value_str)[:30]
                lines.append(
                    f"| {f.line} | {name_short} | {val_short} | "
                    f"{f.vuln} | {f.crit} | **{f.score}** | "
                    f"{f.vuln_reason} | {f.crit_reason} |"
                )
            lines.append("")
        
        lines.append("---")
        lines.append("")
    
    # Footer
    lines.append("## How to Use This Audit")
    lines.append("")
    lines.append("1. Start with INCONSISTENCIES -- these are confirmed problems")
    lines.append("2. Work through Tier 1 (FIX NOW) findings")
    lines.append("3. For each finding:")
    lines.append("   a. Find the correct value from an authoritative source")
    lines.append("   b. Update the value in constants_new.py")
    lines.append("   c. Add `# Source: [citation]` comment")
    lines.append("   d. Replace duplicates with imports")
    lines.append("   e. Verify downstream behavior unchanged")
    lines.append("4. Re-run this scanner to confirm fixes")
    lines.append("")
    lines.append("Companion tools:")
    lines.append("- module_atlas.py -- dependency graph for tracing propagation")
    lines.append("- dep_trace.py -- fine-grained import tracing")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("*Generated by provenance_scanner.py -- "
                 "Paloma's Orrery Developer Tools*")
    lines.append("")
    
    # Write
    content = '\n'.join(lines)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Audit written to {output_path}")
    print(f"  {len(scored)} findings across {files_scanned} files")
    print()
    
    # Print summary
    print("Priority summary:")
    for tier in [1, 2, 3, 4]:
        score_range, action = tier_labels[tier]
        count = tier_counts.get(tier, 0)
        print(f"  Tier {tier} ({score_range}): {count:4d} findings -- {action}")
    
    if any(not d['consistent'] for d in duplicates):
        n_incon = sum(1 for d in duplicates if not d['consistent'])
        print(f"\n  *** {n_incon} INCONSISTENCIES detected -- same concept, different values ***")
    
    n_dups = sum(1 for d in duplicates if d['consistent'])
    if n_dups:
        print(f"  {n_dups} consistent duplicates (consolidation candidates)")


# ============================================================
# MAIN
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
