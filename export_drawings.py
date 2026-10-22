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
    unit          "au" (the Hills cloud, the dust cloud), "r_earth" (the
                  belts, the exosphere) or "r_sun" (the corona)
    rounding      how each coordinate was rounded, and why that is safe
    settings      the drawing's settings: orbits, dots per orbit, seed
    rows          the constants_new.py rows the dots are placed from
    rows_sha256   sha256 of those rows' values (sorted JSON), so a
                  change to any of them shows as a change here
    dots          how many dots
    plane_tilt_deg  (the Hills cloud only) the tilt to the ecliptic of the
                  plane through THESE dots, as rounded, to 0.1 degree:
                  the figure the website's own check fits again from the
                  served dots
    belts         (the belts only) the belts' names, in the order the
                  belt list numbers them
    x, y, z       the dots, one list each, whole AU (the Hills cloud) or
                  hundredths of an Earth radius (the belts)
    w, belt       each dot's weight, 0 to 1 (the belts: from the declared
                  fade; the exosphere: from the density at its distance;
                  the corona and the dust cloud: from the sunlight at its
                  distance),
                  and (the belts only) which belt it is in, 0 inner,
                  1 outer

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
Module updated: October 17, 2026 with Anthropic's Claude Opus 5.5 (L-330,
Tony's rulings of 2026-10-17: the second stored drawing, Earth's two
radiation belts, from van_allen_belt_sampler.py, in Earth radii in
Earth's body frame, with each dot's weight and belt; render() writes
whichever of the lists x, y, z, w and belt a drawing carries, so the
Hills cloud's file is unchanged byte for byte.)
Module updated: October 17, 2026 with Anthropic's Claude Opus 5.5 (L-410:
the third stored drawing, Earth's hydrogen exosphere, from
earth_exosphere_sampler.py, in Earth radii, with each dot's weight.)
Module updated: October 19, 2026 with Anthropic's Claude Opus 5.5 (L-410
with L-131: the fourth and fifth stored drawings, the Sun's corona from
sun_corona_sampler.py, in solar radii, and the zodiacal dust cloud from
zodiacal_dust_sampler.py, in AU in the ecliptic frame, each dot with its
weight, the sunlight reaching it.)
Module updated: October 21, 2026 with Anthropic's Claude Opus 5.5 (L-460:
the corona's drawing starts at the base of the corona, and its file says
so.)
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


def _van_allen_belts():
    """Earth's two radiation belts' file content, as a dict (L-330)."""
    import van_allen_belt_sampler as vab
    rows = vab.rows_from_store()
    dots = vab.drawn_van_allen_belts(rows)
    x, y, z, w, belt = [], [], [], [], []
    for index, key in enumerate(("inner", "outer")):
        part = dots[key]
        x += [round(v, 2) for v in part["x"]]
        y += [round(v, 2) for v in part["y"]]
        z += [round(v, 2) for v in part["z"]]
        w += [round(v, 2) for v in part["w"]]
        belt += [index] * len(part["x"])
    return {
        "schema": SCHEMA,
        "drawing": "van_allen_belts",
        "what": ("Earth's two radiation belts as dots scattered at random "
                 "along dipole field lines (r = L cos^2 latitude; Koskinen "
                 "and Kilpua 2022, sec. 1.2.1), between each belt's measured "
                 "edges and thickest at its measured peak. The fade is drawn "
                 "to show the shape, not measured."),
        "made_by": "van_allen_belt_sampler.drawn_van_allen_belts()",
        "frame": ("Earth's body frame, centred on Earth: z along the spin "
                  "axis, x and y in the equatorial plane. The instrument "
                  "turns it to Earth's pole."),
        "unit": "r_earth",
        "rounding": ("each coordinate to 0.01 Earth radii, about 64 km, and "
                     "each weight to 0.01: a drawing, not a measurement"),
        "belts": ["inner", "outer"],
        "settings": dots["settings"],
        "rows": list(vab.ROW_NAMES),
        "rows_sha256": rows_sha256(rows),
        "dots": len(x),
        "x": x, "y": y, "z": z, "w": w, "belt": belt,
    }


def _earth_exosphere():
    """Earth's hydrogen exosphere's file content, as a dict (L-410)."""
    import earth_exosphere_sampler as ees
    rows = ees.rows_from_store()
    dots = ees.drawn_exosphere(rows)
    return {
        "schema": SCHEMA,
        "drawing": "earth_exosphere",
        "what": ("Earth's hydrogen exosphere, the geocorona, as dots from 3 "
                 "to 100 Earth radii, thinning as Zoennchen et al. (2022) "
                 "measured on the day side to 15 Earth radii and by their "
                 "measured fall beyond. Drawn round; only the shape of the "
                 "thinning is drawn, not a density."),
        "made_by": "earth_exosphere_sampler.drawn_exosphere()",
        "frame": ("Earth's body frame, centred on Earth: z along the spin "
                  "axis. The drawing is round, so the frame changes nothing "
                  "a visitor sees."),
        "unit": "r_earth",
        "rounding": ("each coordinate to 0.01 Earth radii, about 64 km, and "
                     "each weight to 0.01: a drawing, not a measurement"),
        "settings": dots["settings"],
        "rows": list(ees.ROW_NAMES),
        "rows_sha256": rows_sha256(rows),
        "dots": len(dots["x"]),
        "x": [round(v, 2) for v in dots["x"]],
        "y": [round(v, 2) for v in dots["y"]],
        "z": [round(v, 2) for v in dots["z"]],
        "w": [round(v, 2) for v in dots["w"]],
    }


def _sun_corona():
    """The Sun's corona's file content, as a dict (L-410, 2026-10-19)."""
    import sun_corona_sampler as scs
    rows = scs.rows_from_store()
    dots = scs.drawn_corona(rows)
    return {
        "schema": SCHEMA,
        "drawing": "sun_corona",
        "what": ("The Sun's corona as dots from the base of the corona to "
                 "the Alfven surface. A dot's place follows the electron "
                 "density of Mann et al. (2023)'s solar wind model; its "
                 "weight, the sunlight reaching it, which falls with the "
                 "square of distance. Drawn round, the model's long-term "
                 "average; only the shape of the thinning is drawn."),
        "made_by": "sun_corona_sampler.drawn_corona()",
        "frame": ("centred on the Sun. The drawing is round, so no frame "
                  "turn changes what a visitor sees."),
        "unit": "r_sun",
        "rounding": ("each coordinate to 0.001 solar radii, about 700 km, "
                     "and each weight to 0.01: a drawing, not a "
                     "measurement"),
        "settings": dots["settings"],
        "rows": list(scs.ROW_NAMES),
        "rows_sha256": rows_sha256(rows),
        "dots": len(dots["x"]),
        "x": [round(v, 3) for v in dots["x"]],
        "y": [round(v, 3) for v in dots["y"]],
        "z": [round(v, 3) for v in dots["z"]],
        "w": [round(v, 2) for v in dots["w"]],
    }


def _zodiacal_dust():
    """The zodiacal dust cloud's file content, as a dict (L-131,
    2026-10-19)."""
    import zodiacal_dust_sampler as zds
    rows = zds.rows_from_store()
    dots = zds.drawn_dust(rows)
    return {
        "schema": SCHEMA,
        "drawing": "zodiacal_dust",
        "what": ("The zodiacal dust cloud as dots from the edge of the "
                 "dust-free zone to 5.2 AU. A dot's place follows the "
                 "smooth cloud of Kelsall et al. (1998)'s COBE model, "
                 "flattened toward a middle plane tilted to the ecliptic, "
                 "thinning near the Sun between the edges Lamy et al. "
                 "(2022) give; its weight, the sunlight reaching it, which "
                 "falls with the square of distance."),
        "made_by": "zodiacal_dust_sampler.drawn_dust()",
        "frame": ("ecliptic and equinox of J2000, centred on the Sun, the "
                  "orrery's drawing frame"),
        "unit": "au",
        "rounding": ("each coordinate to 0.0001 AU, about 15,000 km, and "
                     "each weight to 0.01: a drawing, not a measurement"),
        "settings": dots["settings"],
        "rows": list(zds.ROW_NAMES),
        "rows_sha256": rows_sha256(rows),
        "dots": len(dots["x"]),
        "x": [round(v, 4) for v in dots["x"]],
        "y": [round(v, 4) for v in dots["y"]],
        "z": [round(v, 4) for v in dots["z"]],
        "w": [round(v, 2) for v in dots["w"]],
    }


# name -> function returning the file's content. A new stored drawing
# is one line here, and test_drawings_export.py checks every entry.
DRAWINGS = {
    "hills_cloud": _hills_cloud,
    "van_allen_belts": _van_allen_belts,
    "earth_exosphere": _earth_exosphere,
    "sun_corona": _sun_corona,
    "zodiacal_dust": _zodiacal_dust,
}

# The lists a drawing may carry, one line each in the file, in this
# order: the coordinates, then (the belts) each dot's weight and belt.
LISTS = ("x", "y", "z", "w", "belt")


def rows_sha256(rows):
    """sha256 of the rows' values, as sorted JSON."""
    text = json.dumps(rows, sort_keys=True, ensure_ascii=True,
                      allow_nan=False)
    return hashlib.sha256(text.encode("ascii")).hexdigest()


def render(content):
    """The exact text written to disk: the header indented, one line per
    coordinate list, so a reader can open the file and see what it is."""
    head = {k: v for k, v in content.items() if k not in LISTS}
    text = json.dumps(head, indent=2, ensure_ascii=True, allow_nan=False)
    assert text.endswith("\n}")
    lines = [text[:-2]]
    for axis in LISTS:
        if axis not in content:
            continue
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
        tilt = content.get("plane_tilt_deg")
        print("  %-15s %s: %d dots, %s%d bytes, rows sha256 %s"
              % (name, action, content["dots"],
                 "" if tilt is None else "plane tilted %.1f deg, " % tilt,
                 len(text), content["rows_sha256"][:12]))
    print("")
    print("Drawings export: %d drawing(s) (%s), %d written."
          % (len(made), ", ".join(made), written))
    return 0


if __name__ == "__main__":
    sys.exit(main())
