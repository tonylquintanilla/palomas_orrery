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
    the count     x, y and z each hold "dots" entries, and dots is the
                  settings' orbits times dots per orbit
    the tilt      the plane through the file's own dots is tilted as the
                  file records, and within the sampler's tolerance of
                  HILLS_CLOUD_TILT_DEG, the paper's "about 30" (for the
                  Hills cloud)

A check that passes is only worth something if it can fail, so three
faults are planted first, each in memory, and each must be caught:

    planted                                  must be caught by
    one dot moved by 1,000 AU                the dots
    the eccentricity row set to 0.5          the dots
    git reporting the file as ignored        tracked

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
"""
import hashlib
import json
import os
import subprocess
import sys

import export_drawings as ed
import hills_cloud_sampler as hcs

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
    lengths = [len(content.get(axis, [])) for axis in ("x", "y", "z")]
    want = settings.get("n_orbits", 0) * settings.get("points_per_orbit", 0)
    if lengths != [n, n, n] or n != want:
        failures.append("%s: %s dots recorded, x/y/z hold %s, settings give "
                        "%d" % (name, n, lengths, want))
    tilt = None
    if lengths == [n, n, n] and n:
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
        tilt = "%.1f deg" % info["tilt"] if info.get("tilt") is not None else "?"
        print("  %-14s %s dots, plane tilted %s, tracked by git: %s, "
              "sha256 %s" % (name, info.get("dots"), tilt,
                             "no" if any("git ignores" in f for f in failures)
                             else "yes", info.get("sha256", "")[:12]))
        if not failures:
            named.append("%s %s dots, tilt %s, sha256 %s"
                         % (name, info["dots"], tilt, info["sha256"][:12]))
    print("")
    if problems:
        for line in problems:
            print("FAIL: " + line)
        print("DRAWINGS EXPORT: FAIL -- %d problem(s)" % len(problems))
        return 1
    print("DRAWINGS EXPORT: PASS -- %d of %d planted faults caught; %s"
          % (caught, len(planted), "; ".join(named)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
