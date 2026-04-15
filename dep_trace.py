"""
dep_trace.py - Targeted dependency path tracer for Paloma's Orrery
Usage:
    python dep_trace.py <module_name> [hops]

Examples:
    python dep_trace.py comet_visualization_shells
    python dep_trace.py spacecraft_encounters 2
    python dep_trace.py gallery_studio 1

Output:
    - Console: text summary (what imports what, who uses it)
    - dep_trace_<module>.html: interactive visual graph

Hub suppression: modules with many consumers (constants_new, shared_utilities,
palomas_orrery) are shown as boundary nodes -- not expanded through.
This keeps the graph focused on the neighborhood that matters.

Module updated: April 2026 with Anthropic's Claude Sonnet 4.6
"""

import ast
import os
import sys
import json
from pathlib import Path


# ── Configuration ─────────────────────────────────────────────────────────────

# Modules with many consumers - shown as boundary nodes, never expanded through
HUB_THRESHOLD = 8  # consumer count above which a module becomes a hub

# Visual categories derived from module_atlas.py ROLE_MAP (single source of truth)
# dep_trace uses fewer visual categories than the atlas roles for cleaner graphs
try:
    from module_atlas import ROLE_MAP, classify_role
    _ATLAS_AVAILABLE = True
except ImportError:
    _ATLAS_AVAILABLE = False
    ROLE_MAP = {}

# Map atlas roles -> dep_trace visual categories
_ROLE_TO_VISUAL = {
    'gui':              'gui',
    'rendering':        'builder',
    'rendering/shells': 'shells',
    'computation':      'builder',
    'data':             'data',
    'cache':            'cache',
    'pipeline':         'gallery',
    'scenario':         'scenario',
    'utility':          'utility',
    'devtool':          'utility',
    'legacy':           'legacy',
    'other':            'other',
}

CATEGORY_COLORS = {
    'gui':      '#4e9af1',   # blue
    'gallery':  '#e07b54',   # orange
    'cache':    '#a78bfa',   # purple
    'builder':  '#34d399',   # green
    'shells':   '#6ee7b7',   # light green
    'data':     '#fbbf24',   # amber
    'utility':  '#94a3b8',   # slate
    'scenario': '#f472b6',   # pink
    'legacy':   '#475569',   # dark slate
    'other':    '#cbd5e1',   # light slate
}


# ── Dependency extraction ──────────────────────────────────────────────────────

def get_imports(filepath):
    """Extract local module imports from a Python file using AST."""
    try:
        with open(filepath, 'rb') as f:
            tree = ast.parse(f.read())
    except Exception:
        return set()
    imports = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.add(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.add(node.module)
    return imports


def build_graph(project_dir='.'):
    """Build full bidirectional dependency graph for all local modules."""
    local_mods = {
        os.path.splitext(f)[0]
        for f in os.listdir(project_dir)
        if f.endswith('.py')
    }

    deps = {}       # mod -> set of mods it imports
    consumers = {}  # mod -> set of mods that import it

    for mod in local_mods:
        fpath = os.path.join(project_dir, mod + '.py')
        if os.path.exists(fpath):
            imported = get_imports(fpath) & local_mods
            deps[mod] = imported
            for imp in imported:
                consumers.setdefault(imp, set()).add(mod)

    return deps, consumers, local_mods


# ── Neighborhood extraction ────────────────────────────────────────────────────

def find_neighborhood(target, deps, consumers, hops=2):
    """
    Walk outward from target by `hops` steps in both directions.
    Hub modules are included as boundary nodes but not expanded through.
    Returns: (nodes, edges, hubs_encountered)
    """
    # Identify hubs
    hubs = {m for m, c in consumers.items() if len(c) >= HUB_THRESHOLD}

    neighborhood = {target}
    frontier = {target}

    for hop in range(hops):
        next_frontier = set()
        for m in frontier:
            if m in hubs and m != target:
                continue  # don't expand through hubs
            # upstream (things this module imports)
            for d in deps.get(m, set()):
                if d not in neighborhood:
                    neighborhood.add(d)
                    next_frontier.add(d)
            # downstream (things that import this module)
            for c in consumers.get(m, set()):
                if c not in neighborhood:
                    neighborhood.add(c)
                    next_frontier.add(c)
        frontier = next_frontier

    # Build edge list within neighborhood
    edges = []
    for m in neighborhood:
        for d in deps.get(m, set()):
            if d in neighborhood:
                edges.append((m, d))

    hubs_encountered = neighborhood & hubs - {target}
    return neighborhood, edges, hubs_encountered


def get_category(mod):
    """Get visual category for a module, using module_atlas ROLE_MAP as source."""
    if _ATLAS_AVAILABLE:
        role = classify_role(mod)
    elif mod in ROLE_MAP:
        role = ROLE_MAP[mod]
    elif mod.endswith('_visualization_shells') or mod.endswith('_shells'):
        role = 'rendering/shells'
    else:
        role = 'other'
    return _ROLE_TO_VISUAL.get(role, 'other')


def get_module_description(filepath):
    """Extract the first meaningful line of the module docstring."""
    try:
        with open(filepath, 'rb') as f:
            tree = ast.parse(f.read())
    except Exception:
        return ''
    doc = ast.get_docstring(tree)
    if not doc:
        return ''
    # Find the first meaningful line (skip filename-only lines)
    for line in doc.split('\n'):
        line = line.strip()
        if not line:
            continue
        # Skip lines that are just the filename
        base = os.path.basename(filepath).replace('.py', '')
        if line.replace('.py', '').replace(' ', '_') == base:
            continue
        # Skip underlines
        if all(c in '=-' for c in line):
            continue
        # Found a meaningful line -- strip "module.py - " prefix if present
        if ' - ' in line and line.split(' - ')[0].endswith('.py'):
            return line.split(' - ', 1)[1]
        return line
    return ''


# ── Text report ───────────────────────────────────────────────────────────────

def print_report(target, nodes, edges, hubs, deps, consumers):
    print(f"\n{'='*60}")
    print(f"  Dependency neighborhood: {target}")
    print(f"{'='*60}")

    print(f"\n  {target} IMPORTS ({len(deps.get(target, []))}):")
    for d in sorted(deps.get(target, [])):
        hub_tag = ' [HUB]' if d in hubs else ''
        print(f"    --> {d}{hub_tag}")

    print(f"\n  CONSUMED BY ({len(consumers.get(target, []))}):")
    for c in sorted(consumers.get(target, [])):
        hub_tag = ' [HUB]' if c in hubs else ''
        print(f"    <-- {c}{hub_tag}")

    non_hub_nodes = nodes - hubs - {target}
    print(f"\n  NEIGHBORHOOD ({len(non_hub_nodes)} modules, {len(edges)} edges):")
    for n in sorted(non_hub_nodes):
        cat = get_category(n)
        print(f"    {n}  [{cat}]")

    if hubs:
        print(f"\n  HUBS (shown as boundaries, not expanded):")
        for h in sorted(hubs):
            print(f"    {h}  ({len(consumers.get(h,[]))} consumers)")

    print()


# ── Mermaid output ────────────────────────────────────────────────────────────

def to_mermaid(target, nodes, edges, hubs):
    lines = ['graph LR']
    for m in sorted(nodes):
        cat = get_category(m)
        label = m.replace('_visualization_shells', '_shells')
        if m == target:
            lines.append(f'    {m}["{label}"]:::target')
        elif m in hubs:
            lines.append(f'    {m}["{label}"]:::hub')
        else:
            lines.append(f'    {m}["{label}"]:::{cat}')
    for src, dst in sorted(edges):
        lines.append(f'    {src} --> {dst}')
    lines.append('    classDef target fill:#ef4444,color:#fff,stroke:#b91c1c')
    lines.append('    classDef hub fill:#1e293b,color:#94a3b8,stroke:#475569')
    for cat, color in CATEGORY_COLORS.items():
        lines.append(f'    classDef {cat} fill:{color},color:#0f172a,stroke:none')
    return '\n'.join(lines)


# ── HTML interactive output ───────────────────────────────────────────────────

VIS_NETWORK_JS = 'vis-network.min.js'
VIS_NETWORK_URL = 'https://cdnjs.cloudflare.com/ajax/libs/vis-network/9.1.9/standalone/umd/vis-network.min.js'


def ensure_vis_network(project_dir):
    """Download vis-network.min.js once to project_dir if not present."""
    js_path = os.path.join(project_dir, VIS_NETWORK_JS)
    if os.path.exists(js_path):
        return  # Already cached
    try:
        import urllib.request
        print(f"  Downloading {VIS_NETWORK_JS} (one-time)...")
        urllib.request.urlretrieve(VIS_NETWORK_URL, js_path)
        print(f"  Saved to {js_path}")
    except Exception as e:
        print(f"  WARNING: Could not download {VIS_NETWORK_JS}: {e}")
        print(f"  HTML graph will require internet connection.")


def to_html(target, nodes, edges, hubs, deps, consumers, project_dir='.'):
    """Generate a self-contained interactive HTML graph using vis-network."""

    # Extract module descriptions
    descriptions = {}
    for m in nodes:
        fpath = os.path.join(project_dir, m + '.py')
        descriptions[m] = get_module_description(fpath)

    node_list = []
    for m in sorted(nodes):
        cat = get_category(m)
        color = CATEGORY_COLORS.get(cat, CATEGORY_COLORS['other'])
        label = m.replace('_visualization_shells', '\n_shells')
        is_target = m == target
        is_hub = m in hubs
        desc = descriptions.get(m, '')
        desc_html = f"<br><i>{desc}</i>" if desc else ''
        node_list.append({
            'id': m,
            'label': label,
            'color': {
                'background': '#ef4444' if is_target else ('#1e293b' if is_hub else color),
                'border': '#b91c1c' if is_target else ('#64748b' if is_hub else color),
                'highlight': {'background': '#fbbf24', 'border': '#d97706'}
            },
            'font': {
                'color': '#fff' if (is_target or is_hub) else '#0f172a',
                'size': 13 if is_target else 11
            },
            'size': 28 if is_target else (20 if is_hub else 16),
            'borderWidth': 3 if is_target else 1,
            'title': (
                f"<b>{m}</b>{desc_html}<br>"
                f"Category: {cat}<br>"
                f"Imports: {len(deps.get(m, []))}<br>"
                f"Consumed by: {len(consumers.get(m, []))}"
                + (' <br><i>[HUB - not expanded]</i>' if is_hub else '')
            ),
            'physics': not is_hub,
        })

    edge_list = []
    for src, dst in edges:
        edge_list.append({
            'from': src,
            'to': dst,
            'arrows': 'to',
            'color': {'color': '#475569', 'highlight': '#fbbf24'},
            'width': 1.5,
        })

    # Legend items
    legend = [(cat, color) for cat, color in CATEGORY_COLORS.items()
              if cat not in ('other',)]

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>dep_trace: {target}</title>
<script src="{VIS_NETWORK_JS}"></script>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ background: #0f172a; color: #e2e8f0; font-family: 'Courier New', monospace; height: 100vh; display: flex; flex-direction: column; overflow: hidden; }}
  header {{ padding: 12px 20px; background: #1e293b; border-bottom: 1px solid #334155; display: flex; align-items: center; gap: 16px; flex-shrink: 0; }}
  header h1 {{ font-size: 14px; color: #94a3b8; font-weight: normal; }}
  header .target {{ color: #ef4444; font-size: 16px; font-weight: bold; }}
  header .meta {{ font-size: 12px; color: #64748b; margin-left: auto; }}
  #graph {{ flex: 1; min-height: 0; overflow: hidden; }}
  #legend {{ position: fixed; bottom: 16px; left: 16px; background: #1e293b; border: 1px solid #334155; border-radius: 6px; padding: 10px 14px; font-size: 11px; }}
  #legend h3 {{ color: #64748b; margin-bottom: 6px; font-size: 10px; text-transform: uppercase; letter-spacing: 1px; }}
  .legend-item {{ display: flex; align-items: center; gap: 6px; margin: 3px 0; color: #94a3b8; }}
  .legend-dot {{ width: 10px; height: 10px; border-radius: 50%; flex-shrink: 0; }}
  #info {{ position: fixed; bottom: 16px; right: 16px; background: #1e293b; border: 1px solid #334155; border-radius: 6px; padding: 12px 16px; font-size: 12px; max-width: 360px; display: none; }}
  #info h3 {{ color: #fbbf24; margin-bottom: 6px; }}
  #info p {{ color: #94a3b8; line-height: 1.5; }}
  #hops-control {{ display: flex; align-items: center; gap: 8px; font-size: 12px; color: #64748b; }}
  #hops-control button {{ background: #334155; border: none; color: #94a3b8; padding: 3px 10px; border-radius: 4px; cursor: pointer; font-family: inherit; }}
  #hops-control button:hover {{ background: #475569; }}
</style>
</head>
<body>
<header>
  <h1>dep_trace /</h1>
  <span class="target">{target}</span>
  <span class="meta">{len(nodes)} modules &nbsp;·&nbsp; {len(edges)} edges &nbsp;·&nbsp; hub threshold: {HUB_THRESHOLD}+ consumers</span>
</header>
<div id="graph"></div>
<div id="legend">
  <h3>Categories</h3>
  {''.join(f'<div class="legend-item"><div class="legend-dot" style="background:{c}"></div>{cat}</div>' for cat, c in legend)}
  <div class="legend-item"><div class="legend-dot" style="background:#ef4444"></div>target</div>
  <div class="legend-item"><div class="legend-dot" style="background:#1e293b; border:1px solid #64748b"></div>hub (boundary)</div>
</div>
<div id="info"></div>
<script>
const nodes = new vis.DataSet({json.dumps(node_list, indent=2)});
const edges = new vis.DataSet({json.dumps(edge_list, indent=2)});

const moduleInfo = {json.dumps({
    m: {
        'desc': descriptions.get(m, ''),
        'imports': sorted(deps.get(m, set()) & nodes),
        'consumers': sorted(consumers.get(m, set()) & nodes),
    } for m in nodes
}, indent=2)};

const container = document.getElementById('graph');
const network = new vis.Network(container, {{ nodes, edges }}, {{
  layout: {{ improvedLayout: true }},
  physics: {{
    enabled: true,
    solver: 'barnesHut',
    barnesHut: {{ gravitationalConstant: -3000, springLength: 150, springConstant: 0.04, damping: 0.3 }},
    stabilization: {{ enabled: true, iterations: 300, fit: true }}
  }},
  interaction: {{ hover: true, tooltipDelay: 200, navigationButtons: false, keyboard: true }},
  nodes: {{ shape: 'box', margin: 6, borderWidthSelected: 2 }},
  edges: {{ smooth: {{ type: 'curvedCW', roundness: 0.1 }} }}
}});

network.once('stabilizationIterationsDone', function() {{
  network.setOptions({{ physics: {{ enabled: false }} }});
  network.fit();
}});

network.on('click', params => {{
  const info = document.getElementById('info');
  if (params.nodes.length > 0) {{
    const id = params.nodes[0];
    const mi = moduleInfo[id] || {{}};
    const desc = mi.desc ? '<p style="color:#e2e8f0;margin:4px 0 8px 0">' + mi.desc + '</p>' : '';
    const imports = (mi.imports || []).length > 0
      ? '<p><span style="color:#64748b">Imports:</span> ' + mi.imports.join(', ') + '</p>' : '';
    const cons = (mi.consumers || []).length > 0
      ? '<p><span style="color:#64748b">Consumed by:</span> ' + mi.consumers.join(', ') + '</p>' : '';
    info.innerHTML = '<h3>' + id + '</h3>' + desc + imports + cons;
    info.style.display = 'block';
  }} else {{
    info.style.display = 'none';
  }}
}});
</script>
</body>
</html>"""
    return html


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    target = sys.argv[1].replace('.py', '')
    hops = int(sys.argv[2]) if len(sys.argv) > 2 else 2

    project_dir = os.path.dirname(os.path.abspath(__file__))
    # If run from outside the project dir, try current dir
    if not os.path.exists(os.path.join(project_dir, target + '.py')):
        project_dir = '.'

    if not os.path.exists(os.path.join(project_dir, target + '.py')):
        print(f"ERROR: '{target}.py' not found in {project_dir}")
        sys.exit(1)

    print(f"Building dependency graph (hops={hops}, hub_threshold={HUB_THRESHOLD})...")
    deps, consumers, local_mods = build_graph(project_dir)

    if target not in local_mods:
        print(f"ERROR: '{target}' not found in module list")
        sys.exit(1)

    nodes, edges, hubs = find_neighborhood(target, deps, consumers, hops)
    print_report(target, nodes, edges, hubs, deps, consumers)

    # Write HTML
    ensure_vis_network(project_dir)
    html = to_html(target, nodes, edges, hubs, deps, consumers, project_dir)
    out_path = f"dep_trace_{target}.html"
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  Visual graph: {out_path}")

    # Write Mermaid snippet
    mermaid = to_mermaid(target, nodes, edges, hubs)
    mmd_path = f"dep_trace_{target}.mmd"
    with open(mmd_path, 'w', encoding='utf-8') as f:
        f.write(mermaid)
    print(f"  Mermaid snippet: {mmd_path}")
    print()


if __name__ == '__main__':
    main()
