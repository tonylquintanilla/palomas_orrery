"""
data_inventory.py - Inventory the large, gitignored data stores for handoff.

Walks the orrery data dirs, groups files by extension (count/size/newest), and
peeks the schema of the two files that feed a web path (orbit_paths.json and one
star_properties pickle). Emits DATA_INVENTORY.md to UPLOAD -- repo copies are
stale/absent; this is the current-state artifact. No large payloads leave the box.

Module updated: July 2026 with Anthropic's Claude Opus 4.8
"""

import os, json, pickle
from collections import defaultdict
from datetime import datetime

DIRS = ["data", "star_data"]            # set to your actual paths under orrery/
OUT  = "DATA_INVENTORY.md"

def human(n):
    for u in ("B", "KB", "MB", "GB"):
        if n < 1024: return f"{n:.1f} {u}"
        n /= 1024
    return f"{n:.1f} TB"

def inventory(dirs):
    g = defaultdict(lambda: {"n": 0, "bytes": 0, "newest": 0, "big": ("", 0)})
    for d in dirs:
        for root, _, files in os.walk(d):
            for f in files:
                p = os.path.join(root, f)
                try: sz, mt = os.path.getsize(p), os.path.getmtime(p)
                except OSError: continue
                ext = os.path.splitext(f)[1].lower() or "(none)"
                e = g[ext]; e["n"] += 1; e["bytes"] += sz
                e["newest"] = max(e["newest"], mt)
                if sz > e["big"][1]: e["big"] = (f, sz)
    return g

def peek_orbit(path):
    with open(path, "r") as f: data = json.load(f)
    fmts, pts = defaultdict(int), []
    for v in data.values():
        if isinstance(v, dict) and isinstance(v.get("data_points"), dict):
            fmts["data_points"] += 1; pts.append(len(v["data_points"]))
        elif isinstance(v, dict) and "x" in v:
            fmts["xyz"] += 1; pts.append(len(v.get("x", [])))
        else: fmts["other"] += 1
    sk = next(iter(data))
    return (f"- entries: {len(data)}, formats: {dict(fmts)}\n"
            f"- points/entry: min {min(pts)}, max {max(pts)}, total {sum(pts)}\n"
            f"- sample '{sk}':\n```\n{json.dumps(data[sk], indent=2)[:800]}\n```")

def peek_pickle(path):
    with open(path, "rb") as f: obj = pickle.load(f)
    out = [f"- object type: {type(obj).__name__}"]
    if hasattr(obj, "shape") and hasattr(obj, "dtypes"):   # pandas DataFrame
        out.append(f"- shape: {obj.shape}")
        out.append(f"- dtypes: {dict(list(obj.dtypes.astype(str).items())[:20])}")
    elif isinstance(obj, dict):
        out.append(f"- dict keys (first 20): {list(obj.keys())[:20]}")
    return "\n".join(out)

def main():
    with open(OUT, "w", newline="\n") as out:
        out.write("# Data Inventory (local, gitignored -- CURRENT state)\n\n")
        out.write("Repo copies stale/absent; this reflects the live local stores.\n\n")
        out.write("## By extension\n\n| ext | count | total | biggest | newest |\n")
        out.write("|---|---|---|---|---|\n")
        for ext, e in sorted(inventory(DIRS).items(), key=lambda kv: -kv[1]["bytes"]):
            nd = datetime.fromtimestamp(e["newest"]).strftime("%Y-%m-%d")
            out.write(f"| {ext} | {e['n']} | {human(e['bytes'])} | "
                      f"{e['big'][0]} ({human(e['big'][1])}) | {nd} |\n")
        for label, path, fn in [
            ("orbit_paths.json", "data/orbit_paths.json", peek_orbit),
            ("star_properties_magnitude.pkl",
             "star_data/star_properties_magnitude.pkl", peek_pickle)]:
            out.write(f"\n## {label}\n\n")
            try: out.write(fn(path) + "\n")
            except Exception as e: out.write(f"(peek failed: {e})\n")
    print(f"Wrote {OUT}")

if __name__ == "__main__":
    main()