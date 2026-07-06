"""
data_inventory.py - Inventory data stores and gallery for handoff and headroom.

Walks the orrery data dirs (gitignored local stores) and optionally the gallery
repo, groups files by extension (count/size/newest), peeks the schema of key
files, and computes GitHub Pages headroom against the 1 GB ceiling.

Emits DATA_INVENTORY.md to UPLOAD -- repo copies are stale/absent for the
orrery data; this is the current-state artifact. No large payloads leave the box.

Usage:
    python data_inventory.py                    # orrery data only (default)
    python data_inventory.py --gallery PATH     # include gallery repo inventory

Module updated: July 2026 with Anthropic's Claude Opus 4.6
"""

import os, json, pickle, sys, argparse
from collections import defaultdict
from datetime import datetime

# -- Config --
# Run from orrery root: C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github
ORRERY_DATA_DIRS = ["data", "star_data"]
GALLERY_DIR = os.path.join("..", "tonyquintanilla.github.io")
OUT = "DATA_INVENTORY.md"
PAGES_CEILING_MB = 1024   # GitHub Pages soft ceiling per repo (1 GB)


def human(n):
    """Format byte count as human-readable string."""
    for u in ("B", "KB", "MB", "GB"):
        if n < 1024:
            return f"{n:.1f} {u}"
        n /= 1024
    return f"{n:.1f} TB"


def inventory(dirs, skip_hidden=True):
    """Walk dirs and group files by extension. Returns dict of extension stats."""
    g = defaultdict(lambda: {"n": 0, "bytes": 0, "newest": 0, "big": ("", 0)})
    total_bytes = 0
    for d in dirs:
        if not os.path.isdir(d):
            continue
        for root, subdirs, files in os.walk(d):
            if skip_hidden:
                subdirs[:] = [s for s in subdirs
                              if not s.startswith('.') and s != 'node_modules']
            for f in files:
                if skip_hidden and f.startswith('.'):
                    continue
                p = os.path.join(root, f)
                try:
                    sz, mt = os.path.getsize(p), os.path.getmtime(p)
                except OSError:
                    continue
                ext = os.path.splitext(f)[1].lower() or "(none)"
                e = g[ext]
                e["n"] += 1
                e["bytes"] += sz
                e["newest"] = max(e["newest"], mt)
                if sz > e["big"][1]:
                    e["big"] = (f, sz)
                total_bytes += sz
    return g, total_bytes


def gallery_inventory(gallery_path):
    """Walk the gallery repo and return extension stats + total size.

    Unlike the orrery inventory which scans only data subdirs, this walks
    the entire repo (excluding .git) to compute the full Pages footprint.
    """
    g = defaultdict(lambda: {"n": 0, "bytes": 0, "newest": 0, "big": ("", 0)})
    total_bytes = 0
    file_count = 0
    for root, subdirs, files in os.walk(gallery_path):
        # Skip .git and node_modules
        subdirs[:] = [s for s in subdirs
                      if s not in ('.git', 'node_modules', '__pycache__')]
        for f in files:
            if f.startswith('.'):
                continue
            p = os.path.join(root, f)
            try:
                sz, mt = os.path.getsize(p), os.path.getmtime(p)
            except OSError:
                continue
            ext = os.path.splitext(f)[1].lower() or "(none)"
            e = g[ext]
            e["n"] += 1
            e["bytes"] += sz
            e["newest"] = max(e["newest"], mt)
            if sz > e["big"][1]:
                e["big"] = (f, sz)
            total_bytes += sz
            file_count += 1
    return g, total_bytes, file_count


def peek_orbit(path):
    """Peek at orbit_paths.json structure."""
    with open(path, "r") as f:
        data = json.load(f)
    fmts, pts = defaultdict(int), []
    for v in data.values():
        if isinstance(v, dict) and isinstance(v.get("data_points"), dict):
            fmts["data_points"] += 1
            pts.append(len(v["data_points"]))
        elif isinstance(v, dict) and "x" in v:
            fmts["xyz"] += 1
            pts.append(len(v.get("x", [])))
        else:
            fmts["other"] += 1
    sk = next(iter(data))
    return (f"- entries: {len(data)}, formats: {dict(fmts)}\n"
            f"- points/entry: min {min(pts)}, max {max(pts)}, total {sum(pts)}\n"
            f"- sample '{sk}':\n```\n{json.dumps(data[sk], indent=2)[:800]}\n```")


def peek_pickle(path):
    """Peek at pickle file structure."""
    with open(path, "rb") as f:
        obj = pickle.load(f)
    out = [f"- object type: {type(obj).__name__}"]
    if hasattr(obj, "shape") and hasattr(obj, "dtypes"):   # pandas DataFrame
        out.append(f"- shape: {obj.shape}")
        out.append(f"- dtypes: {dict(list(obj.dtypes.astype(str).items())[:20])}")
    elif isinstance(obj, dict):
        out.append(f"- dict keys (first 20): {list(obj.keys())[:20]}")
    return "\n".join(out)


def peek_gallery_metadata(gallery_path):
    """Peek at gallery_metadata.json: entry count, fields, categories."""
    meta_path = os.path.join(gallery_path, "gallery", "gallery_metadata.json")
    if not os.path.isfile(meta_path):
        return "(gallery_metadata.json not found)"
    with open(meta_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    vizs = data.get("visualizations", [])
    if not vizs:
        return f"- structure: {list(data.keys())}, no visualizations array"

    # Count entries and categories
    categories = defaultdict(int)
    modes = defaultdict(int)
    types = defaultdict(int)
    for v in vizs:
        categories[v.get("category", "(none)")] += 1
        modes[v.get("mode", "(none)")] += 1
        types[v.get("type", "curated")] += 1

    # Sample entry fields
    sample = vizs[0] if vizs else {}
    fields = list(sample.keys())

    lines = [
        f"- indexed entries: {len(vizs)}",
        f"- fields per entry: {fields}",
        f"- categories: {dict(categories)}",
        f"- modes: {dict(modes)}",
    ]
    if len(types) > 1 or "interactive" in types:
        lines.append(f"- types: {dict(types)}")
    return "\n".join(lines)


def write_ext_table(out, stats):
    """Write the extension breakdown table."""
    out.write("| ext | count | total | biggest | newest |\n")
    out.write("|---|---|---|---|---|\n")
    for ext, e in sorted(stats.items(), key=lambda kv: -kv[1]["bytes"]):
        nd = datetime.fromtimestamp(e["newest"]).strftime("%Y-%m-%d")
        out.write(f"| {ext} | {e['n']} | {human(e['bytes'])} | "
                  f"{e['big'][0]} ({human(e['big'][1])}) | {nd} |\n")


def main():
    parser = argparse.ArgumentParser(
        description="Inventory orrery data stores and the gallery repo.")
    parser.add_argument("--gallery", type=str, default=GALLERY_DIR,
                        help="Path to the gallery repo root "
                             "(default: %(default)s)")
    parser.add_argument("--no-gallery", action="store_true",
                        help="Skip gallery inventory")
    args = parser.parse_args()

    gallery_path = None if args.no_gallery else os.path.abspath(args.gallery)

    with open(OUT, "w", newline="\n") as out:
        # -- Orrery data (gitignored, local only) --
        out.write("# Data Inventory (local, gitignored -- CURRENT state)\n\n")
        out.write("Repo copies stale/absent; this reflects the live "
                  "local stores.\n\n")

        out.write("## Orrery Data -- By extension\n\n")
        orrery_stats, orrery_total = inventory(ORRERY_DATA_DIRS)
        write_ext_table(out, orrery_stats)

        # Peek key files
        for label, path, fn in [
            ("orbit_paths.json", "data/orbit_paths.json", peek_orbit),
            ("star_properties_magnitude.pkl",
             "star_data/star_properties_magnitude.pkl", peek_pickle)]:
            out.write(f"\n## {label}\n\n")
            try:
                out.write(fn(path) + "\n")
            except Exception as e:
                out.write(f"(peek failed: {e})\n")

        # -- Gallery repo --
        if gallery_path:
            if not os.path.isdir(gallery_path):
                out.write(f"\n## Gallery repo\n\n"
                          f"(path not found: {gallery_path})\n")
            else:
                out.write(f"\n---\n\n")
                out.write(f"## Gallery Repo -- {os.path.basename(gallery_path)}\n\n")
                out.write(f"Path: `{gallery_path}`\n\n")

                gal_stats, gal_total, gal_files = gallery_inventory(gallery_path)

                # Headroom
                gal_mb = gal_total / (1024 * 1024)
                headroom_mb = PAGES_CEILING_MB - gal_mb
                out.write(f"**Total size:** {human(gal_total)} "
                          f"({gal_files} files)\n\n")
                out.write(f"**GitHub Pages headroom:** {headroom_mb:.0f} MB "
                          f"remaining of {PAGES_CEILING_MB} MB ceiling "
                          f"({gal_mb / PAGES_CEILING_MB * 100:.1f}% used)\n\n")

                out.write("### By extension\n\n")
                write_ext_table(out, gal_stats)

                # Top 10 largest files
                out.write("\n### Largest files (top 10)\n\n")
                out.write("| file | size | path |\n")
                out.write("|---|---|---|\n")
                all_files = []
                for root, subdirs, files in os.walk(gallery_path):
                    subdirs[:] = [s for s in subdirs
                                  if s not in ('.git', 'node_modules',
                                               '__pycache__')]
                    for f in files:
                        if f.startswith('.'):
                            continue
                        p = os.path.join(root, f)
                        try:
                            sz = os.path.getsize(p)
                        except OSError:
                            continue
                        rel = os.path.relpath(p, gallery_path)
                        all_files.append((f, sz, rel))
                for f, sz, rel in sorted(all_files, key=lambda x: -x[1])[:10]:
                    out.write(f"| {f} | {human(sz)} | {rel} |\n")

                # Gallery metadata peek
                out.write(f"\n### gallery_metadata.json\n\n")
                try:
                    out.write(peek_gallery_metadata(gallery_path) + "\n")
                except Exception as e:
                    out.write(f"(peek failed: {e})\n")

        # -- Headroom summary (both repos) --
        if gallery_path and os.path.isdir(gallery_path):
            out.write(f"\n---\n\n## Headroom Summary\n\n")
            out.write(f"| repo | served size | ceiling | headroom | used |\n")
            out.write(f"|---|---|---|---|---|\n")
            out.write(f"| gallery | {human(gal_total)} | "
                      f"{PAGES_CEILING_MB} MB | "
                      f"{headroom_mb:.0f} MB | "
                      f"{gal_mb / PAGES_CEILING_MB * 100:.1f}% |\n")
            out.write(f"| orrery (gitignored data) | {human(orrery_total)} | "
                      f"n/a (not served) | -- | -- |\n")
            out.write(f"\nNote: orrery data is local/gitignored. If orbit cache "
                      f"files are pushed to either repo for web serving, "
                      f"re-run this inventory to update headroom.\n")

    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
