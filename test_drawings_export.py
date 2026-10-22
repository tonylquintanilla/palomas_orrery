"""
test_drawings_export.py - each stored drawing in data/drawings/ is the
drawing its rows give today, git tracks it, and each check can fail.

For every entry in export_drawings.DRAWINGS it checks:

    the file      data/drawings/<name>.json exists and reads as JSON
    tracked       git does not ignore the file -- an ignored file never
                  reaches GitHub, and the website's pull of it would fail
                  with nothing here saying why (Tony's question of
                  2026-10-11 about ignored JSON files in data/)
    the dots      drawing it again from constants_new.py gives the same
                  file, byte for byte after line endings; so the file
                  follows the rows and the sampler, and nobody edited it
    the count     each list the file carries holds "dots" entries, and
                  dots is what the settings give: orbits times dots per
                  orbit (the Hills cloud), the two belts' dots (the belts)
    the tilt      the plane through the file's own dots is tilted as the
                  file records, and within the sampler's tolerance of
                  HILLS_CLOUD_TILT_DEG, the paper's "about 30" (for the
                  Hills cloud)
    the belts     every dot on a field line between its belt's edge rows,
                  none below the ground, and each belt thickest at its
                  peak at the equator, read from the file's own dots
                  (van_allen_belt_sampler.check_dots; for the belts)
    the exosphere every dot between its two rows, the dots in five shells
                  following the measured profile, and each dot's weight the
                  one its distance gives, read from the file's own dots
                  (earth_exosphere_sampler.check_dots; for the exosphere)
    the corona    every dot between the corona's base and the Alfven
                  surface, the dots in five shells following the electron
                  density, and each dot's weight the sunlight its distance
                  gives (sun_corona_sampler.check_dots)
    the dust      every dot between the dust-free zone and 5.2 AU, the
                  dots following the radial and the vertical profiles, and
                  each dot's weight the sunlight its distance gives
                  (zodiacal_dust_sampler.check_dots)
    the outer cloud  every dot between where the outer cloud begins and its
                  outer edge (outer_oort_sampler.check_dots); the count is
                  whatever the seed gives, held by the re-draw above
    the tide      every dot between the same two edges, the dots in four
                  distance shells following the band's rule, and in five
                  latitude shells following |sin b cos b| about the
                  galactic pole as its rows give it, worked out a second
                  way (galactic_tide_sampler.check_dots)

A check that passes is only worth something if it can fail, so faults
are planted first, each in memory, and each must be caught:

    planted                                  must be caught by
    one dot moved by 1,000 AU                the dots
    the eccentricity row set to 0.5          the dots
    git reporting the file as ignored        tracked
    a belt dot moved off its belt            the belts
    the outer belt's peak drawn at its edge  the belts
    an exosphere dot moved inside 3 radii    the exosphere
    the exosphere drawn with no fall-off     the exosphere
    an exosphere dot's weight changed        the exosphere
    a corona dot moved past the Alfven surface   the corona
    a corona dot moved to the Sun's surface  the corona
    the corona drawn with no fall-off        the corona
    a corona dot's weight changed            the corona
    a dust dot moved inside the dust-free zone   the dust
    the dust drawn with no flattening        the dust
    a dust dot's weight changed              the dust
    an outer cloud dot moved inside its row  the outer cloud
    a tide dot moved past the outer edge     the tide
    the tide drawn about the ecliptic's pole the tide

The last line starts "DRAWINGS EXPORT:", which the maintenance run
quotes. It names each drawing, its dots, its tilt and its sha256.

Run (VS Code Run button, or):
    python test_drawings_export.py

Needs git on the PATH, as Constants change does; without it the run
fails and says so rather than passing unchecked.

Role: dev_tools
Domain: orrery

Module created: October 11, 2026 with Anthropic's Claude Opus 5.5 (L-421,
the website half of the inner Oort cloud)
Module updated: October 17, 2026 with Anthropic's Claude Opus 5.5 (L-330:
the second drawing, Earth's radiation belts; the count reads each
drawing's own settings, the tilt is checked where a drawing records one,
and the belts' dots are checked against their rows, with two more faults
planted)
Module updated: October 17, 2026 with Anthropic's Claude Opus 5.5 (L-410:
the third drawing, Earth's hydrogen exosphere, checked against its rows,
with three more faults planted)
Module updated: October 19, 2026 with Anthropic's Claude Opus 5.5 (L-410
with L-131: the fourth and fifth drawings, the Sun's corona and the
zodiacal dust cloud, checked against their rows, with six more faults
planted)
Module updated: October 21, 2026 with Anthropic's Claude Opus 5.5 (L-460:
a corona dot moved to the Sun's surface is planted, and must be caught
now that the drawing starts at the corona's base)
Module updated: October 22, 2026 with Anthropic's Claude Opus 5.5 (L-434:
the sixth and seventh drawings, the outer Oort cloud and the galactic
tide, checked against their rows, with three more faults planted: an
outer cloud dot inside where its row says it begins, a tide dot past
the outer edge, and the tide drawn about the wrong pole)
"""
import hashlib
import json
import os
import subprocess
import sys

import export_drawings as ed
import hills_cloud_sampler as hcs
import van_allen_belt_sampler as vab
import earth_exosphere_sampler as ees
import sun_corona_sampler as scs
import zodiacal_dust_sampler as zds
import outer_oort_sampler as oos
import galactic_tide_sampler as gts

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))


def git_ignored(path):
    """True if git ignores path, False if not; raises if git cannot say."""
    result = subprocess.run(
        ["git", "check-ignore", "-q", "--no-index",
         os.path.relpath(path, PROJECT_DIR)],
        cwd=PROJECT_DIR, capture_output=True, text=True)
    if result.returncode == 0:
        return True
    if result.returncode == 1:
        return False
    raise RuntimeError("git check-ignore exited %d: %s"
                       % (result.returncode, result.stderr.strip()))


def check_one(name, text_on_disk, text_now, path, ignored=git_ignored):
    """Failures for one drawing, as sentences, and what was examined."""
    failures = []
    try:
        content = json.loads(text_on_disk)
    except ValueError as exc:
        return ["%s: the file does not read as JSON (%s)" % (name, exc)], {}
    try:
        if ignored(path):
            failures.append("%s: git ignores %s, so it never reaches GitHub "
                            "and the website cannot pull it -- change "
                            ".gitignore" % (name, os.path.relpath(path, PROJECT_DIR)))
    except (OSError, RuntimeError) as exc:
        failures.append("%s: could not ask git whether the file is ignored "
                        "(%s)" % (name, exc))
    if text_on_disk != text_now:
        now = json.loads(text_now)
        moved = [key for key in now if now.get(key) != content.get(key)]
        failures.append("%s: the file is not the drawing its rows give "
                        "today -- these fields differ: %s. Run "
                        "export_drawings.py" % (name, ", ".join(moved) or
                                                "(layout only)"))
    n = content.get("dots")
    settings = content.get("settings", {})
    axes = [axis for axis in ed.LISTS if axis in content]
    lengths = [len(content.get(axis, [])) for axis in axes]
    if "n_orbits" in settings:
        want = settings.get("n_orbits", 0) * settings.get("points_per_orbit", 0)
    elif "dots_inner" in settings:
        want = settings.get("dots_inner", 0) + settings.get("dots_outer", 0)
    elif "n_clumps" in settings:
        # L-434: how many dots the outer cloud keeps is what the seed gives, not
        # a setting; the re-draw above holds the count to the rows.
        want = n
    else:
        want = settings.get("dots", 0)
    if lengths != [n] * len(axes) or n != want or axes[:3] != ["x", "y", "z"]:
        failures.append("%s: %s dots recorded, %s hold %s, settings give "
                        "%d" % (name, n, "/".join(axes), lengths, want))
    elif name == "van_allen_belts":
        split = {}
        for index, key in enumerate(content.get("belts", [])):
            pick = [k for k, b in enumerate(content["belt"]) if b == index]
            split[key] = dict((axis, [content[axis][k] for k in pick])
                              for axis in ("x", "y", "z"))
        try:
            for line in vab.check_dots(split, vab.rows_from_store()):
                failures.append("%s: %s" % (name, line))
        except KeyError as exc:
            failures.append("%s: the file names no belt %s" % (name, exc))
    elif name == "earth_exosphere":
        for line in ees.check_dots(content, ees.rows_from_store()):
            failures.append("%s: %s" % (name, line))
    elif name == "sun_corona":
        for line in scs.check_dots(content, scs.rows_from_store()):
            failures.append("%s: %s" % (name, line))
    elif name == "zodiacal_dust":
        for line in zds.check_dots(content, zds.rows_from_store()):
            failures.append("%s: %s" % (name, line))
    elif name == "outer_oort_cloud":
        for line in oos.check_dots(content, oos.rows_from_store()):
            failures.append("%s: %s" % (name, line))
    elif name == "galactic_tide":
        for line in gts.check_dots(content, gts.rows_from_store()):
            failures.append("%s: %s" % (name, line))
    tilt = None
    if lengths == [n] * len(axes) and n and "plane_tilt_deg" in content:
        tilt = hcs.plane_tilt_deg(*(list(map(float, content[axis]))
                                    for axis in ("x", "y", "z")))
        if abs(round(tilt, 1) - content.get("plane_tilt_deg", -999)) > 0.05:
            failures.append("%s: the plane through the file's dots is tilted "
                            "%.1f deg, the file records %s"
                            % (name, tilt, content.get("plane_tilt_deg")))
        if name == "hills_cloud":
            paper = hcs.rows_from_store()["HILLS_CLOUD_TILT_DEG"]
            if abs(tilt - paper) > 10.0:
                failures.append("%s: the dots' plane is tilted %.1f deg, not "
                                "within 10 deg of the paper's %s"
                                % (name, tilt, paper))
    info = {"dots": n, "tilt": tilt,
            "sha256": hashlib.sha256(text_on_disk.encode("utf-8")).hexdigest()}
    return failures, info


def _planted(text_now, path):
    """Three faults, each with the check that must catch it."""
    out = []
    moved = json.loads(text_now)
    moved["x"][0] += 1000
    out.append(("one dot moved by 1,000 AU", ed.render(moved), text_now,
                git_ignored, "is not the drawing"))
    rows = hcs.rows_from_store()
    rows["HILLS_CLOUD_ECCENTRICITY"] = 0.5
    real = hcs.rows_from_store
    hcs.rows_from_store = lambda: dict(rows)
    try:
        other = ed.render(ed.DRAWINGS["hills_cloud"]())
    finally:
        hcs.rows_from_store = real
    out.append(("the eccentricity row set to 0.5", text_now, other,
                git_ignored, "is not the drawing"))
    out.append(("git reporting the file as ignored", text_now, text_now,
                lambda _p: True, "git ignores"))
    return out


def _planted_belts(text_now):
    """Two faults in the belts' file, each caught by the belts' check:
    the file is also re-drawn from its rows, so each planted text is
    compared with itself there and only the belts' check can catch it."""
    out = []
    moved = json.loads(text_now)
    moved["x"][0] += 3.0
    out.append(("a belt dot moved off its belt", ed.render(moved),
                "off the field lines"))
    edge = json.loads(text_now)
    rows = vab.rows_from_store()
    rows["EARTH_VAN_ALLEN_OUTER_RADII"] = (
        rows["EARTH_VAN_ALLEN_OUTER_BELT_INNER_EDGE"] + 0.05)
    other = vab.drawn_van_allen_belts(rows)
    outer = [k for k, b in enumerate(edge["belt"]) if b == 1]
    for axis in ("x", "y", "z"):
        for k, v in zip(outer, other["outer"][axis]):
            edge[axis][k] = round(v, 2)
    out.append(("the outer belt's peak drawn at its edge", ed.render(edge),
                "not thickest at the peak"))
    return out


def _planted_exosphere(text_now):
    """Three faults in the exosphere's file, each caught by the
    exosphere's check (each planted text is compared with itself, as the
    belts' are, so only that check can catch it)."""
    out = []
    moved = json.loads(text_now)
    moved["x"][0], moved["y"][0], moved["z"][0] = 1.0, 0.0, 0.0
    out.append(("an exosphere dot moved inside 3 radii", ed.render(moved),
                "lie outside"))
    flat = json.loads(text_now)
    rows = ees.rows_from_store()
    rows["EARTH_EXOSPHERE_H_FIT_EXPONENT"] = 0.0
    rows["EARTH_EXOSPHERE_H_OUTER_EXPONENT"] = 0.0
    other = ees.drawn_exosphere(rows)
    for axis in ("x", "y", "z"):
        flat[axis] = [round(v, 2) for v in other[axis]]
    out.append(("the exosphere drawn with no fall-off", ed.render(flat),
                "do not follow the profile"))
    heavy = json.loads(text_now)
    far = max(range(len(heavy["x"])), key=lambda k: heavy["x"][k] ** 2 +
              heavy["y"][k] ** 2 + heavy["z"][k] ** 2)
    heavy["w"][far] = 1.0
    out.append(("an exosphere dot's weight changed", ed.render(heavy),
                "carry a weight"))
    return out


def _planted_corona(text_now):
    """Three faults in the corona's file, each caught by the corona's
    check (each planted text is compared with itself, as the belts' are,
    so only that check can catch it)."""
    out = []
    moved = json.loads(text_now)
    moved["x"][0], moved["y"][0], moved["z"][0] = 40.0, 0.0, 0.0
    out.append(("a corona dot moved past the Alfven surface",
                ed.render(moved), "lie outside"))
    # L-460: the drawing began at the Sun's surface, under the
    # chromosphere; a dot back there must fail.
    low = json.loads(text_now)
    low["x"][0], low["y"][0], low["z"][0] = 1.0, 0.0, 0.0
    out.append(("a corona dot moved to the Sun's surface",
                ed.render(low), "lie outside"))
    flat = json.loads(text_now)
    inner, outer = scs.span(scs.rows_from_store())
    import numpy as np
    rng = np.random.default_rng(1)
    n = len(flat["x"])
    radii = rng.uniform(inner, outer, n)
    cos_t = rng.uniform(-1.0, 1.0, n)
    for k in range(n):
        s = (1.0 - cos_t[k] ** 2) ** 0.5
        flat["x"][k] = round(float(radii[k] * s), 3)
        flat["y"][k] = 0.0
        flat["z"][k] = round(float(radii[k] * cos_t[k]), 3)
    out.append(("the corona drawn with no fall-off", ed.render(flat),
                "do not follow the profile"))
    heavy = json.loads(text_now)
    far = max(range(len(heavy["x"])), key=lambda k: heavy["x"][k] ** 2 +
              heavy["y"][k] ** 2 + heavy["z"][k] ** 2)
    heavy["w"][far] = 1.0
    out.append(("a corona dot's weight changed", ed.render(heavy),
                "carry a weight"))
    return out


def _planted_dust(text_now):
    """Three faults in the dust cloud's file, each caught by its check."""
    out = []
    moved = json.loads(text_now)
    moved["x"][0], moved["y"][0], moved["z"][0] = 0.01, 0.0, 0.0
    out.append(("a dust dot moved inside the dust-free zone",
                ed.render(moved), "lie outside"))
    round_cloud = json.loads(text_now)
    rows = zds.rows_from_store()
    rows["ZODIACAL_DUST_BETA"] = 0.0
    other = zds.drawn_dust(rows)
    for axis in ("x", "y", "z"):
        round_cloud[axis] = [round(v, 4) for v in other[axis]]
    out.append(("the dust drawn with no flattening", ed.render(round_cloud),
                "vertical profile"))
    heavy = json.loads(text_now)
    far = max(range(len(heavy["x"])), key=lambda k: heavy["x"][k] ** 2 +
              heavy["y"][k] ** 2 + heavy["z"][k] ** 2)
    heavy["w"][far] = 1.0
    out.append(("a dust dot's weight changed", ed.render(heavy),
                "carry a weight"))
    return out


def _planted_outer_cloud(cloud_now, tide_now):
    """Three faults in the outer cloud's and the tide's files (L-434), each
    caught by its own check (each planted text is compared with itself,
    as the belts' are, so only that check can catch it)."""
    out = []
    near = oos.rows_from_store()["INNER_OORT_DISK_OUTER_AU"]
    inside = json.loads(cloud_now)
    inside["x"][0], inside["y"][0], inside["z"][0] = int(near) - 500, 0, 0
    out.append(("outer_oort_cloud", "an outer cloud dot moved inside its row",
                ed.render(inside), "where the outer cloud's row says it begins"))
    far = gts.rows_from_store()["OUTER_OORT_CLOUD_AU"]
    past = json.loads(tide_now)
    past["x"][0], past["y"][0], past["z"][0] = int(far) + 5000, 0, 0
    out.append(("galactic_tide", "a tide dot moved past the outer edge",
                ed.render(past), "edges:"))
    # The error L-406 replaced: the tide drawn about the ecliptic's pole
    # (RA 270 deg, Dec 90 deg less the obliquity) instead of the galaxy's.
    rows = gts.rows_from_store()
    rows["GALACTIC_NORTH_POLE_RA_J2000_DEG"] = 270.0
    rows["GALACTIC_NORTH_POLE_DEC_J2000_DEG"] = (
        90.0 - rows["EARTH_OBLIQUITY_J2000_DEG"])
    other = gts.drawn_tide(rows)
    tilted = json.loads(tide_now)
    for axis in ("x", "y", "z"):
        tilted[axis] = [int(round(float(v))) for v in other[axis]]
    out.append(("galactic_tide", "the tide drawn about the ecliptic's pole",
                ed.render(tilted), "tilt:"))
    return out


def main():
    print("=" * 70)
    print("  DRAWINGS EXPORT CHECK -- data/drawings/ against the rows")
    print("=" * 70)
    problems = []
    texts_now = {}
    for name, build in ed.DRAWINGS.items():
        texts_now[name] = ed.render(build())

    caught = 0
    planted = _planted(texts_now["hills_cloud"],
                       ed.path_of(PROJECT_DIR, "hills_cloud"))
    for label, on_disk, now, ignored, expect in planted:
        failures, _ = check_one("hills_cloud", on_disk, now,
                                ed.path_of(PROJECT_DIR, "hills_cloud"),
                                ignored)
        hit = any(expect in line for line in failures)
        print("  planted: %-36s %s" % (label, "caught" if hit else "MISSED"))
        if hit:
            caught += 1
        else:
            problems.append("planted fault not caught: " + label)
    belts_now = texts_now["van_allen_belts"]
    belt_planted = _planted_belts(belts_now)
    for label, text, expect in belt_planted:
        failures, _ = check_one("van_allen_belts", text, text,
                                ed.path_of(PROJECT_DIR, "van_allen_belts"),
                                lambda _p: False)
        hit = any(expect in line for line in failures)
        print("  planted: %-36s %s" % (label, "caught" if hit else "MISSED"))
        if hit:
            caught += 1
        else:
            problems.append("planted fault not caught: " + label)
    exo_planted = _planted_exosphere(texts_now["earth_exosphere"])
    for label, text, expect in exo_planted:
        failures, _ = check_one("earth_exosphere", text, text,
                                ed.path_of(PROJECT_DIR, "earth_exosphere"),
                                lambda _p: False)
        hit = any(expect in line for line in failures)
        print("  planted: %-36s %s" % (label, "caught" if hit else "MISSED"))
        if hit:
            caught += 1
        else:
            problems.append("planted fault not caught: " + label)
    sun_planted = ([("sun_corona", p) for p in
                    _planted_corona(texts_now["sun_corona"])] +
                   [("zodiacal_dust", p) for p in
                    _planted_dust(texts_now["zodiacal_dust"])])
    sun_planted += [(name, (label, text, expect)) for name, label, text,
                    expect in _planted_outer_cloud(texts_now["outer_oort_cloud"],
                                                   texts_now["galactic_tide"])]
    for name, (label, text, expect) in sun_planted:
        failures, _ = check_one(name, text, text,
                                ed.path_of(PROJECT_DIR, name),
                                lambda _p: False)
        hit = any(expect in line for line in failures)
        print("  planted: %-36s %s" % (label, "caught" if hit else "MISSED"))
        if hit:
            caught += 1
        else:
            problems.append("planted fault not caught: " + label)
    print("")

    named = []
    for name in ed.DRAWINGS:
        path = ed.path_of(PROJECT_DIR, name)
        if not os.path.exists(path):
            problems.append("%s: %s is missing -- run export_drawings.py"
                            % (name, os.path.relpath(path, PROJECT_DIR)))
            continue
        with open(path, "rb") as handle:
            on_disk = handle.read().replace(b"\r\n", b"\n").decode("utf-8")
        failures, info = check_one(name, on_disk, texts_now[name], path)
        problems.extend(failures)
        tilt = ("plane tilted %.1f deg" % info["tilt"]
                if info.get("tilt") is not None else "no plane recorded")
        print("  %-15s %s dots, %s, tracked by git: %s, "
              "sha256 %s" % (name, info.get("dots"), tilt,
                             "no" if any("git ignores" in f for f in failures)
                             else "yes", info.get("sha256", "")[:12]))
        if not failures:
            named.append("%s %s dots, %s, sha256 %s"
                         % (name, info["dots"], tilt, info["sha256"][:12]))
    print("")
    if problems:
        for line in problems:
            print("FAIL: " + line)
        print("DRAWINGS EXPORT: FAIL -- %d problem(s)" % len(problems))
        return 1
    print("DRAWINGS EXPORT: PASS -- %d of %d planted faults caught; %s"
          % (caught, len(planted) + len(belt_planted) + len(exo_planted)
             + len(sun_planted),
             "; ".join(named)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
