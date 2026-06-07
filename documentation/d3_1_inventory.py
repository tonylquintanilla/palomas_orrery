"""
d3_1_inventory.py - Phase D3.1 hovertext/legendgroup inventory.

Walks every *_visualization_shells.py file with Python's AST, identifies
trace constructors (go.Scatter3d / go.Surface / go.Mesh3d) and known
helper calls (create_info_marker, build_sphere_shell), extracts the
showlegend / legendgroup / name / hover-lead-line state for each trace,
and groups by (file, builder, legendgroup) into legend entries.

Produces:
    /home/claude/inventory_per_trace.csv         - raw per-trace dump
    /home/claude/inventory_per_legend_entry.csv  - per-legend-entry summary
    /home/claude/D3_1_INVENTORY.md               - review document for Opus 4.7

Throwaway script. Lives in /home/claude only.

Module updated: May 2026 with Anthropic's Claude Opus 4.7
"""

import ast
import csv
import os
import re
from collections import defaultdict

SHELLS_DIR = "/home/claude/shells"
OUT_DIR = "/home/claude"

TRACE_CLASSES = {"Scatter3d", "Surface", "Mesh3d"}
HELPER_NAMES = {"create_info_marker", "build_sphere_shell"}

# Body name derived from filename. asteroid_belt and planet9 are
# multi-word, so we keep an explicit map for clarity.
FILE_TO_BODY = {
    "mercury_visualization_shells.py": "Mercury",
    "venus_visualization_shells.py": "Venus",
    "earth_visualization_shells.py": "Earth",
    "moon_visualization_shells.py": "Moon",
    "mars_visualization_shells.py": "Mars",
    "jupiter_visualization_shells.py": "Jupiter",
    "saturn_visualization_shells.py": "Saturn",
    "uranus_visualization_shells.py": "Uranus",
    "neptune_visualization_shells.py": "Neptune",
    "pluto_visualization_shells.py": "Pluto",
    "eris_visualization_shells.py": "Eris",
    "solar_visualization_shells.py": "Sun",
    "comet_visualization_shells.py": "Comet",
    "asteroid_belt_visualization_shells.py": "Asteroid Belt",
    "planet9_visualization_shells.py": "Planet 9",
}

# Functions defined in a shell file but never called anywhere in the
# codebase. Dead code -- their traces never reach the live dispatch.
# Verified by a project-wide grep with zero-reference filter.
ORPHAN_FUNCTIONS = {
    ("neptune_visualization_shells.py", "create_neptune_magnetic_poles"),
}

# -----------------------------------------------------------------------
# AST helpers
# -----------------------------------------------------------------------

def is_trace_call(node):
    """go.Scatter3d / go.Surface / go.Mesh3d"""
    if not isinstance(node, ast.Call):
        return None
    if isinstance(node.func, ast.Attribute):
        if (isinstance(node.func.value, ast.Name)
                and node.func.value.id == "go"
                and node.func.attr in TRACE_CLASSES):
            return node.func.attr
    return None


def is_helper_call(node):
    """create_info_marker(...) / build_sphere_shell(...)"""
    if not isinstance(node, ast.Call):
        return None
    if isinstance(node.func, ast.Name) and node.func.id in HELPER_NAMES:
        return node.func.id
    return None


def kw_dict(call):
    """Map of keyword arg name -> AST node for a Call."""
    return {kw.arg: kw.value for kw in call.keywords if kw.arg is not None}


def lit(node):
    """Best-effort literal: returns str of a Constant or a marker for non-literal."""
    if isinstance(node, ast.Constant):
        return repr(node.value) if isinstance(node.value, str) else str(node.value)
    return None


def resolve_var(name, assigns):
    """Look up a Name in the function's assignment table; return source AST node."""
    return assigns.get(name)


def render_expr(node, assigns, depth=0):
    """Turn an AST expression into a readable representation, resolving
    simple Name -> assignment one level deep. Returns one of:
      - "'literal string'"   for string constants
      - "f\"...{var}...\""   for f-strings
      - "<dynamic: ...>"     for anything we can't pin down

    The goal is human-readable for the inventory, not exact reconstruction.
    """
    if node is None:
        return ""

    # String literal
    if isinstance(node, ast.Constant):
        if isinstance(node.value, str):
            return repr(node.value)
        return repr(node.value)

    # f-string
    if isinstance(node, ast.JoinedStr):
        parts = []
        for v in node.values:
            if isinstance(v, ast.Constant) and isinstance(v.value, str):
                parts.append(v.value)
            elif isinstance(v, ast.FormattedValue):
                parts.append("{" + render_expr(v.value, assigns, depth + 1) + "}")
            else:
                parts.append("?")
        return 'f"' + "".join(parts) + '"'

    # Variable name -- try one level of resolution
    if isinstance(node, ast.Name):
        if depth < 2 and node.id in assigns:
            inner = render_expr(assigns[node.id], assigns, depth + 1)
            return "%s=%s" % (node.id, inner)
        return node.id

    # % formatting:  "%s: %s" % (body_name, config['name'])
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Mod):
        left = render_expr(node.left, assigns, depth + 1)
        right = render_expr(node.right, assigns, depth + 1)
        return "%s %% %s" % (left, right)

    # Subscript:  config['name']
    if isinstance(node, ast.Subscript):
        val = render_expr(node.value, assigns, depth + 1)
        if isinstance(node.slice, ast.Constant):
            return "%s[%r]" % (val, node.slice.value)
        return "%s[?]" % val

    # Tuple
    if isinstance(node, ast.Tuple):
        return "(" + ", ".join(render_expr(e, assigns, depth + 1) for e in node.elts) + ")"

    # Call
    if isinstance(node, ast.Call):
        if isinstance(node.func, ast.Name):
            return node.func.id + "(...)"
        if isinstance(node.func, ast.Attribute):
            return node.func.attr + "(...)"
        return "<call>"

    return "<expr>"


def first_hover_lead(text_repr):
    """Extract a 40-char lead from a string representation, stripping
    quotes and showing the first line."""
    if not text_repr:
        return ""
    s = text_repr.strip()
    # strip leading f" or " or '
    if s.startswith(("f'", 'f"')):
        s = s[2:]
    elif s.startswith(("'", '"')):
        s = s[1:]
    if s.endswith(("'", '"')):
        s = s[:-1]
    # take to first newline (literal \n or actual)
    s = s.split("\\n")[0].split("\n")[0]
    if len(s) > 40:
        s = s[:40] + "..."
    return s


# -----------------------------------------------------------------------
# Function-level analysis
# -----------------------------------------------------------------------

def collect_assigns(func_node):
    """Build a {var_name: last-assigned-AST-node} map within a function body."""
    assigns = {}
    for n in ast.walk(func_node):
        if isinstance(n, ast.Assign):
            for tgt in n.targets:
                if isinstance(tgt, ast.Name):
                    assigns[tgt.id] = n.value
    return assigns


def analyze_function(func_node, file_body, file_name):
    """Yield trace records for every trace constructor or helper call
    inside this function body."""
    assigns = collect_assigns(func_node)
    fname = func_node.name

    for node in ast.walk(func_node):
        trace_cls = is_trace_call(node)
        if trace_cls:
            kws = kw_dict(node)

            name_node = kws.get("name")
            lg_node = kws.get("legendgroup")
            sl_node = kws.get("showlegend")
            hi_node = kws.get("hoverinfo")
            ht_node = kws.get("hovertemplate")
            text_node = kws.get("text")

            # showlegend defaults to True for Scatter3d unless explicitly set
            if sl_node is None:
                showlegend = "True (default)"
            else:
                showlegend = render_expr(sl_node, assigns)

            hover_source = text_node if text_node is not None else ht_node
            hover_repr = render_expr(hover_source, assigns) if hover_source else ""

            yield {
                "file": file_name,
                "body": file_body,
                "builder": fname,
                "line": node.lineno,
                "trace_class": "go.%s" % trace_cls,
                "name": render_expr(name_node, assigns) if name_node else "<none>",
                "legendgroup": render_expr(lg_node, assigns) if lg_node else "<none>",
                "showlegend": showlegend,
                "hoverinfo": render_expr(hi_node, assigns) if hi_node else "<default>",
                "hover_lead": first_hover_lead(hover_repr),
                "via_helper": "",
            }
            continue

        helper = is_helper_call(node)
        if helper == "create_info_marker":
            # signature: (x, y, z, color, text, legendgroup, customdata=None)
            args = node.args
            text_arg = args[4] if len(args) > 4 else None
            lg_arg = args[5] if len(args) > 5 else None
            hover_repr = render_expr(text_arg, assigns) if text_arg else ""

            yield {
                "file": file_name,
                "body": file_body,
                "builder": fname,
                "line": node.lineno,
                "trace_class": "go.Scatter3d (helper)",
                "name": "''",  # helper sets name=''
                "legendgroup": render_expr(lg_arg, assigns) if lg_arg else "<none>",
                "showlegend": "False (helper)",
                "hoverinfo": "<default>",
                "hover_lead": first_hover_lead(hover_repr),
                "via_helper": "create_info_marker",
            }
            continue

        if helper == "build_sphere_shell":
            # signature: (config, body_name, center_position=...)
            # Emits two traces: geometry (showlegend=True) + info marker.
            # Both use legendgroup = "{body_name}: {config['name']}".
            args = node.args
            config_arg = args[0] if len(args) > 0 else None
            body_arg = args[1] if len(args) > 1 else None

            body_repr = render_expr(body_arg, assigns) if body_arg else "?"
            # Try to extract config['name'] reference symbolically.
            cfg_repr = render_expr(config_arg, assigns) if config_arg else "?"
            inferred_name = "%s + \": \" + %s['name']" % (body_repr, cfg_repr)

            # Geometry trace (legend leader)
            yield {
                "file": file_name,
                "body": file_body,
                "builder": fname,
                "line": node.lineno,
                "trace_class": "go.Scatter3d/Mesh3d (build_sphere_shell)",
                "name": inferred_name,
                "legendgroup": inferred_name,
                "showlegend": "True (build_sphere_shell)",
                "hoverinfo": "'skip'",
                "hover_lead": "<config['hover_text']>",
                "via_helper": "build_sphere_shell",
            }
            # Info marker trace (follower)
            yield {
                "file": file_name,
                "body": file_body,
                "builder": fname,
                "line": node.lineno,
                "trace_class": "go.Scatter3d (build_sphere_shell info)",
                "name": "''",
                "legendgroup": inferred_name,
                "showlegend": "False (build_sphere_shell)",
                "hoverinfo": "<default>",
                "hover_lead": "<config['hover_text']>",
                "via_helper": "build_sphere_shell",
            }
            continue


# -----------------------------------------------------------------------
# File-level driver
# -----------------------------------------------------------------------

def analyze_file(path):
    file_name = os.path.basename(path)
    body = FILE_TO_BODY.get(file_name, file_name.replace("_visualization_shells.py", "").title())
    with open(path, "r", encoding="utf-8") as f:
        src = f.read()
    tree = ast.parse(src, filename=path)
    traces = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            for rec in analyze_function(node, body, file_name):
                traces.append(rec)
    return traces


# -----------------------------------------------------------------------
# shell_configs cross-reference
# -----------------------------------------------------------------------

def load_needs_sun_position_map(configs_path):
    """Parse shell_configs.py to build {builder_function_name: True}.

    Looks for the literal pattern:
        'builder': 'module.function',
        ...
        'needs_sun_position': True,
    within the same dict. Implementation is regex-based since the file
    is large and we only need a key lookup, not a full parse.
    """
    if not os.path.exists(configs_path):
        return {}
    with open(configs_path, "r", encoding="utf-8") as f:
        src = f.read()
    # Split into shell-config blocks at each occurrence of `'builder':`
    # and look for `needs_sun_position` within the surrounding block.
    flag_map = {}
    # Find all 'builder': 'module.function', occurrences
    for m in re.finditer(r"'builder'\s*:\s*'([^']+)'", src):
        builder_full = m.group(1)  # e.g. mercury_visualization_shells.create_mercury_magnetosphere_shell
        func_name = builder_full.rsplit(".", 1)[-1]
        # Look 400 chars ahead for needs_sun_position
        window = src[m.end():m.end() + 400]
        if re.search(r"'needs_sun_position'\s*:\s*True", window):
            flag_map[func_name] = True
    return flag_map


# -----------------------------------------------------------------------

def aggregate_legend_entries(traces, needs_sun_map=None):
    """Group traces by (file, builder, legendgroup_normalized).

    Each group is one legend entry. The leader is the trace with
    showlegend=True (preferred) -- its name becomes the legend label.
    """
    if needs_sun_map is None:
        needs_sun_map = {}
    # Files where the "Body:" prefix convention doesn't naturally apply.
    # asteroid_belt entries are population names (Hilda Family, Jupiter
    # Trojans); comet entries prefix with the comet's own name (MAPS, etc.).
    CATEGORY_FILES = {
        "asteroid_belt_visualization_shells.py",
        "comet_visualization_shells.py",
    }

    groups = defaultdict(list)
    for t in traces:
        key = (t["file"], t["builder"], t["legendgroup"])
        groups[key].append(t)

    entries = []
    for (fname, builder, lg), members in groups.items():
        # Find leader: prefer first member where showlegend looks True
        leader = None
        for m in members:
            if "True" in m["showlegend"]:
                leader = m
                break
        if leader is None:
            leader = members[0]

        # All hover leads (deduped)
        hover_leads = []
        for m in members:
            if m["hover_lead"] and m["hover_lead"] not in hover_leads:
                hover_leads.append(m["hover_lead"])

        # Conformance checks
        body = leader["body"]
        legend_label = leader["name"]
        violations = []
        is_category_file = fname in CATEGORY_FILES

        # Rule 0: leader must have a legendgroup set.
        # If the leader's legendgroup is <none>, the trace can't toggle as
        # a unit with any paired info marker -- this is the crust-shell
        # pattern bug seen in Earth/Venus/Mars/etc.
        if "<none>" in lg and "True" in leader["showlegend"]:
            violations.append("leader trace missing legendgroup attribute")

        # Rule 1: legend label format "Body: Something" -- skipped for
        # category files (asteroid_belt, comet).
        if not is_category_file:
            label_clean = legend_label.replace("f\"", "").replace("f'", "").strip("\"'")
            if "<none>" in legend_label or "''" == legend_label.strip():
                violations.append("no legend name set on leader")
            elif legend_label.startswith(("'", '"')):
                # literal string -- must start with "Body:"
                if not label_clean.startswith(body + ":"):
                    violations.append("label does not start with '%s:'" % body)
            elif "{" in label_clean:
                # f-string -- body name must appear in the template literally
                # (we look in label_clean for the body word outside braces)
                template_parts = re.sub(r"\{[^}]*\}", "", label_clean)
                if body.lower() not in template_parts.lower():
                    violations.append("f-string label template may not include body name")

        # Rule 2: hovertext leads with legend label. Check ALL members,
        # not just the leader. The single-info-marker pattern has the
        # leader (geometry) with hoverinfo='skip' and the info marker
        # carrying the actual hover -- so only checking the leader
        # misses real violations like items 45 and 46 from Round 3.
        # Skip for category files (label prefix is not the file body name).
        if not is_category_file:
            for m in members:
                m_hi = m.get("hoverinfo", "") or ""
                m_hover = m.get("hover_lead", "") or ""
                if not m_hover:
                    continue
                if "skip" in m_hi or "none" in m_hi:
                    continue
                if "<config" in m_hover or "?" in m_hover:
                    continue
                if body.lower() not in m_hover.lower():
                    violations.append("hover lead does not echo body name")
                    break  # one violation per group

        # Rule 3: orphan (legendgroup with no showlegend=True trace)
        # Suppress for legendgroup=<none> singletons -- those are caught
        # by Rule 0 above. Otherwise flag.
        if not any("True" in m["showlegend"] for m in members):
            if "<none>" not in lg:
                violations.append("no showlegend=True leader in group")

        # Rule 4: multiple-leader (more than one showlegend=True in same group)
        leaders_count = sum(1 for m in members if "True" in m["showlegend"])
        if leaders_count > 1:
            violations.append("multiple showlegend=True traces in same group (%d)" % leaders_count)

        # Ambiguous: legend group has 3+ members and we can't tell why
        ambiguous = len(members) >= 3 and not violations

        # Orphan-function check: traces from functions never called in the
        # codebase are dead code. Flag the conformance separately so
        # reviewer knows to focus on live dispatch, not source-only state.
        is_orphan = (fname, builder) in ORPHAN_FUNCTIONS

        if is_orphan:
            conformance = "ORPHAN"
            if not violations:
                violations.append("function not called anywhere in codebase")
            else:
                violations.append("(also: function not called anywhere)")
        elif violations:
            conformance = "FAIL"
        elif ambiguous:
            conformance = "?"
        else:
            conformance = "OK"

        entries.append({
            "file": fname,
            "body": body,
            "builder": builder,
            "legend_label": legend_label,
            "legendgroup": lg,
            "trace_count": len(members),
            "hover_lead": (hover_leads[0] if hover_leads else ""),
            "conformance": conformance,
            "violations": "; ".join(violations) if violations else "",
            "line": leader["line"],
            "needs_sun_position": needs_sun_map.get(builder, False),
        })

    # Sort for stable output
    entries.sort(key=lambda e: (e["file"], e["line"]))
    return entries


# -----------------------------------------------------------------------
# CSV + markdown writers
# -----------------------------------------------------------------------

def write_per_trace_csv(traces, path):
    fields = ["file", "body", "builder", "line", "trace_class",
              "name", "legendgroup", "showlegend", "hoverinfo",
              "hover_lead", "via_helper"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for t in traces:
            w.writerow(t)


def write_per_entry_csv(entries, path):
    fields = ["file", "body", "builder", "legend_label", "legendgroup",
              "trace_count", "hover_lead", "conformance", "violations",
              "needs_sun_position", "line"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for e in entries:
            w.writerow(e)


def write_markdown(entries, traces, path):
    """Write the review document for Opus 4.7."""
    by_file = defaultdict(list)
    for e in entries:
        by_file[e["file"]].append(e)

    files_sorted = sorted(by_file.keys(), key=lambda f: FILE_TO_BODY.get(f, f))

    lines = []
    lines.append("# D3.1 Inventory: Hovertext and Legendgroup State Across Shell Files")
    lines.append("")
    lines.append("**Session:** May 22, 2026")
    lines.append("**Author:** Anthropic's Claude Opus 4.7")
    lines.append("**Reviewer (intended):** Anthropic's Claude Opus 4.7 (Mode 7 audit)")
    lines.append("**Integrator:** Tony Quintanilla")
    lines.append("")
    lines.append("Inventory phase of D3.1 (item 54). Captures the current state of "
                 "legend names, legendgroups, and hovertext-lead-lines across all 15 "
                 "`*_visualization_shells.py` files. Produced by static AST analysis "
                 "with single-level variable resolution.")
    lines.append("")
    lines.append("## Headline Finding")
    lines.append("")
    lines.append("The dominant non-conformance pattern is **Rule 2 (hovertext "
                 "leads with legend label)**, not Rule 1 or Rule 3. The info-marker "
                 "pattern is structurally correct -- one geometry trace with "
                 "`hoverinfo='skip'` plus one info marker carrying the hover -- "
                 "but the info marker's text is typically `layer_info['description']`, "
                 "`belt['description']`, or similar, which starts with the *description* "
                 "rather than the legend label. When the user hovers the cursor, they "
                 "see a paragraph about (say) atmospheric composition with no leading "
                 "indicator of which shell it belongs to.")
    lines.append("")
    lines.append("This explains Round 3 items 45 and 46 (Neptune radiation belts and "
                 "FAC hovertext \"not clearly labelled to connect them to the legend\") "
                 "as a codebase-wide pattern, not Neptune-specific. The sweep is "
                 "mechanical: prepend `\"{body}: {shell_name}\\n\\n\"` (or `<br><br>`) "
                 "to every info marker's text. The shell name is already available "
                 "in scope wherever the info marker is constructed.")
    lines.append("")
    lines.append("Secondary findings (much smaller counts):")
    lines.append("")
    lines.append("- **Legendgroup missing on crust/cloud surface traces** (15 entries). "
                 "Geometry trace omits `legendgroup`; paired info marker has its own. "
                 "They don't toggle together. Add `legendgroup=trace_name` on the surface.")
    lines.append("- **Solar shells use \"Sun's X\" or \"X\" instead of \"Sun: X\"** "
                 "(9 entries). Heliospheric region names. Judgment call: convert to "
                 "the convention or treat solar as a category file like comet/asteroid_belt?")
    lines.append("- **Neptune magnetosphere has two showlegend=True traces in one "
                 "group** (1 entry). Bow shock and envelope share legendgroup; both "
                 "claim the legend. Pick one leader; suppress the other.")
    lines.append("- **MAPS comet tails have seven showlegend=True traces in one "
                 "group** (1 entry, 7 traces). Same pattern as Neptune magnetosphere "
                 "but at higher count. Pick one leader.")
    lines.append("- **Orphan function** `create_neptune_magnetic_poles` (1 entry, dead "
                 "code from D2 Option C cleanup). Recommend removal.")
    lines.append("")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Section 1: Convention summary
    lines.append("## Section 1. Convention Summary (the rubric)")
    lines.append("")
    lines.append("Three rules that every legend entry must satisfy. The sweep "
                 "(D3.1 part 2) will bring non-conformant entries into compliance.")
    lines.append("")
    lines.append("**Rule 1 -- Legend label format.** The user-visible legend name "
                 "follows the form `\"Body: Shell Name\"` (e.g., `\"Earth: Magnetosphere\"`, "
                 "`\"Neptune: Adams Arc\"`). **Exemption:** `asteroid_belt_visualization_shells.py` "
                 "uses population names (`\"Hilda Family\"`, `\"Jupiter Trojans (Greeks - L4)\"`) "
                 "and `comet_visualization_shells.py` prefixes with the specific comet's "
                 "own name (`\"MAPS: Nucleus\"`, `\"C/2026 A1: Tail\"`). Rule 1 is not "
                 "applied to these two files. The label of a multi-body category file should "
                 "still be unambiguous within the legend.")
    lines.append("")
    lines.append("**Rule 2 -- Hovertext leads with the legend label.** The first "
                 "line of hover text matches the legend entry name. Applies to every "
                 "trace in the legendgroup, so the cursor always identifies the "
                 "entry regardless of which sub-trace it is over.")
    lines.append("")
    lines.append("**Rule 3 -- Legendgroup independence.** Each shell gets its own "
                 "legendgroup so it toggles independently. Within a group, exactly "
                 "one trace has `showlegend=True` (the leader, carrying the visible "
                 "name); all others have `showlegend=False`. Components of one "
                 "structure (e.g., the four surface patches of a magnetosphere "
                 "envelope) share a group. Functionally distinct features "
                 "(e.g., Adams arc vs Le Verrier arc) get separate groups.")
    lines.append("")
    lines.append("**Tony's tiebreaker for ambiguous cases:** \"Are they different "
                 "components of one structure, or are they functionally different "
                 "structures?\" If functionally different, split.")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Section 2: Conformance summary
    lines.append("## Section 2. Conformance Summary")
    lines.append("")
    lines.append("One row per file. `OK` = passes all rules. `FAIL` = at least "
                 "one rule violated. `?` = ambiguous (multiple traces in a group, "
                 "no rule violation detected, but reviewer should sanity-check). "
                 "`ORPHAN` = function exists in source but is never called -- "
                 "its traces never reach the live dispatch.")
    lines.append("")
    lines.append("| File | Body | Entries | OK | FAIL | ? | Orphan |")
    lines.append("|------|------|--------:|---:|-----:|--:|-------:|")
    total_e = total_ok = total_fail = total_amb = total_orph = 0
    for fname in files_sorted:
        es = by_file[fname]
        ok = sum(1 for e in es if e["conformance"] == "OK")
        fail = sum(1 for e in es if e["conformance"] == "FAIL")
        amb = sum(1 for e in es if e["conformance"] == "?")
        orph = sum(1 for e in es if e["conformance"] == "ORPHAN")
        body = FILE_TO_BODY.get(fname, "?")
        lines.append("| `%s` | %s | %d | %d | %d | %d | %d |" %
                     (fname, body, len(es), ok, fail, amb, orph))
        total_e += len(es); total_ok += ok; total_fail += fail
        total_amb += amb; total_orph += orph
    lines.append("| **TOTAL** | -- | **%d** | **%d** | **%d** | **%d** | **%d** |" %
                 (total_e, total_ok, total_fail, total_amb, total_orph))
    lines.append("")
    lines.append("---")
    lines.append("")

    # Section 3: Per-file detail
    lines.append("## Section 3. Per-File Detail")
    lines.append("")
    for fname in files_sorted:
        body = FILE_TO_BODY.get(fname, "?")
        es = by_file[fname]
        lines.append("### `%s` (%s)" % (fname, body))
        lines.append("")
        lines.append("| Line | Builder | Sun? | Legend Label | Group | # | Hover lead | Conf. | Notes |")
        lines.append("|-----:|---------|:----:|--------------|-------|--:|------------|:-----:|-------|")
        for e in es:
            label = (e["legend_label"] or "").replace("|", "\\|")
            grp = (e["legendgroup"] or "").replace("|", "\\|")
            # truncate long fields for table readability
            if len(label) > 50:
                label = label[:47] + "..."
            if len(grp) > 50:
                grp = grp[:47] + "..."
            hov = (e["hover_lead"] or "").replace("|", "\\|")
            if len(hov) > 40:
                hov = hov[:37] + "..."
            notes = (e["violations"] or "").replace("|", "\\|")
            sun_flag = "Y" if e.get("needs_sun_position") else ""
            lines.append("| %d | `%s` | %s | %s | %s | %d | %s | %s | %s |" %
                         (e["line"], e["builder"], sun_flag, label, grp,
                          e["trace_count"], hov, e["conformance"], notes))
        lines.append("")

    lines.append("---")
    lines.append("")

    # Section 4: Findings grouped by violation type
    lines.append("## Section 4. Findings -- Non-Conforming Entries by Violation Type")
    lines.append("")
    buckets = defaultdict(list)
    for e in entries:
        if not e["violations"]:
            continue
        for v in e["violations"].split(";"):
            v = v.strip()
            if v:
                buckets[v].append(e)

    if not buckets:
        lines.append("*No non-conforming entries detected by the script. "
                     "Review Section 5 for ambiguous cases.*")
        lines.append("")
    else:
        for vtype in sorted(buckets.keys()):
            lines.append("### %s" % vtype)
            lines.append("")
            lines.append("| File | Line | Builder | Legend Label |")
            lines.append("|------|-----:|---------|--------------|")
            for e in buckets[vtype]:
                label = (e["legend_label"] or "").replace("|", "\\|")
                if len(label) > 60:
                    label = label[:57] + "..."
                lines.append("| `%s` | %d | `%s` | %s |" %
                             (e["file"], e["line"], e["builder"], label))
            lines.append("")

    lines.append("---")
    lines.append("")

    # Section 5: Ambiguous cases
    lines.append("## Section 5. Ambiguous Cases Needing Judgment")
    lines.append("")
    lines.append("Legend entries with three or more traces and no rule violation. "
                 "Per the tiebreaker, the question is: are the traces in this "
                 "group **components of one structure** (keep grouped) or "
                 "**functionally different structures** (split into separate "
                 "legend entries)?")
    lines.append("")
    amb = [e for e in entries if e["conformance"] == "?"]
    if not amb:
        lines.append("*No ambiguous cases detected. Either every multi-trace group "
                     "violated a rule (caught in Section 4) or every group has "
                     "exactly 2 traces (geometry + info marker, the standard "
                     "pattern).*")
        lines.append("")
    else:
        lines.append("| File | Line | Builder | Legend Label | Traces | Group |")
        lines.append("|------|-----:|---------|--------------|-------:|-------|")
        for e in amb:
            label = (e["legend_label"] or "").replace("|", "\\|")
            grp = (e["legendgroup"] or "").replace("|", "\\|")
            if len(label) > 40:
                label = label[:37] + "..."
            if len(grp) > 40:
                grp = grp[:37] + "..."
            lines.append("| `%s` | %d | `%s` | %s | %d | %s |" %
                         (e["file"], e["line"], e["builder"], label,
                          e["trace_count"], grp))
        lines.append("")
        lines.append("For each row, decide: **KEEP** (one structure) or **SPLIT** "
                     "(distinct structures). SPLIT decisions feed the sweep manifest.")
        lines.append("")

    lines.append("---")
    lines.append("")

    # Section 6: Out-of-scope / known issues
    lines.append("## Section 6. Out-of-Scope / Known Issues")
    lines.append("")
    lines.append("Things the inventory cannot detect mechanically but are tracked "
                 "for downstream phases:")
    lines.append("")
    lines.append("- **Item 47a (Neptune arc superposition):** Adams, Le Verrier, "
                 "and Galle arc markers occupy the same coordinate. This is a "
                 "position bug, not a legendgroup bug. D3.2 handles it.")
    lines.append("- **Item 47b (Neptune ring marker superposition):** Lassell and "
                 "Arago ring markers superimposed. Same category as 47a.")
    lines.append("- **Items 43, 44 (hovertext truncation):** `\\n` newlines in "
                 "hover text strings render as backslash-n in Plotly; should be "
                 "`<br>`. Not visible in this inventory (we only capture the "
                 "first line). The sweep can normalize newlines wherever it "
                 "touches hover strings.")
    lines.append("- **Loop-generated traces collapsed to one row.** Several builders "
                 "(Earth radiation belts, Neptune radiation belts, Neptune FAC, "
                 "Mars crustal fields, ring systems) use a `for` loop to create N "
                 "traces, each with a dynamic name from `belt_names[i]`, `ring_info['name']`, "
                 "etc. The script sees one trace constructor inside the loop and "
                 "aggregates it as a single legend entry. At runtime, N legend "
                 "entries are produced. The sweep should still treat the loop body "
                 "as a single edit site -- whatever fix applies to one belt applies "
                 "to all -- but reviewers should know the runtime legend has more "
                 "entries than this table.")
    lines.append("- **Script false positives on Rule 2.** Some FAIL entries are "
                 "script-limitation false positives. When the hover text is a "
                 "multi-line string built via implicit string concatenation inside "
                 "a list literal (`text=[\"Foo bar...<br>\" \"continued...\"]`), the "
                 "script's `render_expr` returns `<expr>` and the body-name check "
                 "fails. The runtime hover text may in fact start with the body "
                 "name (e.g., line 604 Neptune magnetic center starts with \"Neptune's "
                 "magnetic field center is offset...\"). These are flagged with "
                 "`<expr>` in the hover-lead column and should be verified manually "
                 "during the sweep -- but the safest action regardless is to prepend "
                 "the legend label explicitly, which removes the ambiguity.")
    lines.append("- **Orphan functions (dead code).** A project-wide grep with "
                 "zero-reference filter identified one true orphan function: "
                 "`create_neptune_magnetic_poles` in `neptune_visualization_shells.py`. "
                 "This function still defines four `showlegend=True` traces "
                 "(magnetic center, axis line, north pole, south pole) -- the "
                 "old pre-D2 pattern that Option C replaced. The live dispatch "
                 "no longer reaches this function; the diamond marker is now "
                 "created inline inside `create_neptune_magnetosphere` at line "
                 "604. The orphan entries are tagged with conformance `ORPHAN` "
                 "in the per-file tables. Recommend: remove the orphan function "
                 "in the D3.1 sweep, since dead code in source confuses both "
                 "future readers and automated tooling like this inventory.")
    lines.append("- **Hover-echo check is best-effort.** The script flags entries "
                 "where the leader's hover lead does not contain the body name. "
                 "It correctly skips entries where hover is intentionally suppressed "
                 "(`hoverinfo='skip'` or `'none'`). For entries with f-string hover "
                 "templates the script cannot resolve to a literal, the check looks "
                 "at the rendered f-string template; if the template variable resolves "
                 "to something like `layer_info['description']`, the script cannot "
                 "tell whether the resulting string starts with the body name. "
                 "Manual review at the source is required for those rows; the per-trace "
                 "CSV preserves enough context to do that quickly.")
    lines.append("- **Crust shell pattern.** Several `*_crust_shell` builders "
                 "(Earth, Venus, Mars, Pluto, Eris, Jupiter, Saturn, Uranus, Neptune, "
                 "Moon) follow an older pattern where the `go.Mesh3d` surface has "
                 "`name` set but `legendgroup` omitted, and the paired info marker "
                 "uses a different legendgroup with `(Info)` appended. These show "
                 "up as two separate legend entries in this inventory rather than "
                 "one. The sweep should add a shared `legendgroup` to the surface "
                 "trace and remove the `(Info)` suffix from the info marker.")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Footer
    lines.append("## Appendix A. Raw Data Files")
    lines.append("")
    lines.append("- `inventory_per_trace.csv` -- one row per trace constructor call. "
                 "Raw working data for the sweep manifest.")
    lines.append("- `inventory_per_legend_entry.csv` -- one row per legend entry "
                 "(grouped by `legendgroup`). Same content as Section 3 tables.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("*Module updated: May 2026 with Anthropic's Claude Opus 4.7*")
    lines.append("*Paloma's Orrery | palomasorrery.com*")
    lines.append("")

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


# -----------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------

def main():
    needs_sun_map = load_needs_sun_position_map(
        os.path.join(SHELLS_DIR, "shell_configs.py"))
    print("Loaded needs_sun_position flag for %d builders from shell_configs.py"
          % len(needs_sun_map))

    all_traces = []
    files = sorted(f for f in os.listdir(SHELLS_DIR)
                   if f.endswith("_visualization_shells.py"))
    for f in files:
        path = os.path.join(SHELLS_DIR, f)
        try:
            traces = analyze_file(path)
            all_traces.extend(traces)
            print("  %s -> %d trace records" % (f, len(traces)))
        except SyntaxError as e:
            print("  SKIP %s: %s" % (f, e))

    entries = aggregate_legend_entries(all_traces, needs_sun_map=needs_sun_map)

    print("\nTotals: %d traces, %d legend entries" % (len(all_traces), len(entries)))

    write_per_trace_csv(all_traces, os.path.join(OUT_DIR, "inventory_per_trace.csv"))
    write_per_entry_csv(entries, os.path.join(OUT_DIR, "inventory_per_legend_entry.csv"))
    write_markdown(entries, all_traces, os.path.join(OUT_DIR, "D3_1_INVENTORY.md"))

    print("\nArtifacts written:")
    print("  /home/claude/inventory_per_trace.csv")
    print("  /home/claude/inventory_per_legend_entry.csv")
    print("  /home/claude/D3_1_INVENTORY.md")


if __name__ == "__main__":
    main()
