"""
export_drawings.py -- write the orrery's stored drawings into
data/drawings/, one file per drawing, for the website to pull and draw.

RUN COMMAND
-----------
Open this file in VS Code and click Run. It takes no arguments.

    python export_drawings.py

orrery_maintenance_run.py runs it on every maintenance run, as a
GENERATOR, so a drawing cannot fall behind the rows it is drawn from.
test_drawings_export.py, among the checkers, then re-draws each one and
fails if the file does not hold the same dots.

WHY A DRAWING IS STORED (Tony's ruling of 2026-10-11, L-421, option A)
---------------------------------------------------------------------
Some shapes are scattered dots placed by random numbers, or by a model
the browser would have to rewrite: the Hills cloud is dots along orbits
following Nesvorny et al. (2025), Fig. 3. The orrery places them; the
website draws the dots it is given and places none itself. So there is
one way of placing them, the orrery's, and the website's cloud is the
orrery's cloud. A shape that is a few numbers and a formula (a sphere,
a ring) is not stored: the numbers are the drawing, and the website
computes it from the served rows. The other scattered-dot shells (the
streamer band, the outer cloud's clumps, the galactic tide) can join
this list later; that work is its own ledger item.

WHAT IT WRITES
--------------
data/drawings/<name>.json for each entry in DRAWINGS:

    schema        1
    drawing       the drawing's name, the same as the file's
    what          one sentence on what the dots are
    made_by       the function that places the dots
    frame         the frame the coordinates are in
    unit          "au"
    rounding      how each coordinate was rounded, and why that is safe
    settings      the drawing's settings: orbits, dots per orbit, seed
    rows          the constants_new.py rows the dots are placed from
    rows_sha256   sha256 of those rows' values (sorted JSON), so a
                  change to any of them shows as a change here
    dots          how many dots
    plane_tilt_deg  the tilt to the ecliptic of the plane through THESE
                  dots, as rounded, to 0.1 degree: the figure the
                  website's own check fits again from the served dots
    x, y, z       the dots, one list each, whole AU

DETERMINISTIC ON PURPOSE
------------------------
The same rows give the same file: the seed is fixed and nothing in the
file is a date or a commit. The file is written only when its content
would change, always with LF line endings, so an unchanged drawing
never shows in GitHub Desktop. As with data/constants_export.json, the
gallery records the orrery SHA it pulled the file at.

The coordinates are rounded to whole AU. The Hills cloud spans about
20,000 AU and its innermost dots sit near 200 AU, so half an AU moves
no dot a visitor can see, and the file is about half the size. The
plane's tilt is fitted after rounding.

Writes nothing, and exits 1, if a drawing cannot be made.

Role: devtool
Domain: dev_tools

Module created: October 11, 2026 with Anthropic's Claude Opus 5.5
(L-421, the website half of the inner Oort cloud: the first stored
drawing, the Hills cloud).
"""

import hashlib
import json
import os
import sys

DRAWINGS_DIR = os.path.join("data", "drawings")
SCHEMA = 1


def _hills_cloud():
    """The Hills cloud's file content, as a dict, from the store."""
    import hills_cloud_sampler as hcs
    rows = hcs.rows_from_store()
    dots = hcs.drawn_hills_cloud(rows)
    x = [int(round(v)) for v in dots['x']]
    y = [int(round(v)) for v in dots['y']]
    z = [int(round(v)) for v in dots['z']]
    tilt = hcs.plane_tilt_deg(*(list(map(float, axis)) for axis in (x, y, z)))
    return {
        "schema": SCHEMA,
        "drawing": "hills_cloud",
        "what": ("The Hills cloud, the inner Oort cloud, as dots along "
                 "orbits following Nesvorny et al. (2025), Fig. 3 "
                 "(arXiv:2502.11252): a disk tilted to the ecliptic, "
                 "with two arms."),
        "made_by": "hills_cloud_sampler.drawn_hills_cloud()",
        "frame": ("ecliptic and equinox of J2000, centred on the Sun, "
                  "the orrery's drawing frame"),
        "unit": "au",
        "rounding": ("each coordinate to the nearest whole AU: a drawing, "
                     "not a measurement, and half an AU is invisible at "
                     "this scale"),
        "settings": dots['settings'],
        "rows": list(hcs.ROW_NAMES),
        "rows_sha256": rows_sha256(rows),
        "dots": len(x),
        "plane_tilt_deg": round(tilt, 1),
        "x": x, "y": y, "z": z,
    }


# name -> function returning the file's content. A new stored drawing
# is one line here, and test_drawings_export.py checks every entry.
DRAWINGS = {
    "hills_cloud": _hills_cloud,
}


def rows_sha256(rows):
    """sha256 of the rows' values, as sorted JSON."""
    text = json.dumps(rows, sort_keys=True, ensure_ascii=True,
                      allow_nan=False)
    return hashlib.sha256(text.encode("ascii")).hexdigest()


def render(content):
    """The exact text written to disk: the header indented, one line per
    coordinate list, so a reader can open the file and see what it is."""
    head = {k: v for k, v in content.items() if k not in ("x", "y", "z")}
    text = json.dumps(head, indent=2, ensure_ascii=True, allow_nan=False)
    assert text.endswith("\n}")
    lines = [text[:-2]]
    for axis in ("x", "y", "z"):
        lines.append(',\n  "%s": %s' % (axis, json.dumps(
            content[axis], separators=(",", ":"))))
    return "".join(lines) + "\n}\n"


def path_of(project_dir, name):
    return os.path.join(project_dir, DRAWINGS_DIR, name + ".json")


def main():
    project_dir = os.path.dirname(os.path.abspath(__file__))
    print("=" * 70)
    print("  DRAWINGS EXPORT -- %s/" % DRAWINGS_DIR.replace(os.sep, "/"))
    print("=" * 70)
    made = {}
    for name, build in DRAWINGS.items():
        try:
            made[name] = render(build())
        except Exception as exc:          # report, write nothing
            print("FAIL: the drawing %r could not be made (%s: %s). "
                  "Nothing written." % (name, type(exc).__name__, exc))
            return 1
    written = 0
    for name, text in made.items():
        target = path_of(project_dir, name)
        old = None
        if os.path.exists(target):
            with open(target, "rb") as handle:
                old = handle.read().replace(b"\r\n", b"\n").decode("utf-8")
        content = json.loads(text)
        if old == text:
            action = "unchanged, not written"
        else:
            os.makedirs(os.path.dirname(target), exist_ok=True)
            with open(target, "w", encoding="utf-8", newline="") as handle:
                handle.write(text)
            action = "written" if old is not None else "created"
            written += 1
        print("  %-14s %s: %d dots, plane tilted %.1f deg, %d bytes, "
              "rows sha256 %s"
              % (name, action, content["dots"], content["plane_tilt_deg"],
                 len(text), content["rows_sha256"][:12]))
    print("")
    print("Drawings export: %d drawing(s) (%s), %d written."
          % (len(made), ", ".join(made), written))
    return 0


if __name__ == "__main__":
    sys.exit(main())
