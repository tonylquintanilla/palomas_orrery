"""
test_enso_night_check.py - the El Nino night check (L-060) on NOAA's saved files, with no network: a newer discussion, RONI season or chances says EL NINO DUE and saves the copies; NOAA's files as the page shows them say CURRENT and write nothing; an outage is reported; the page is never touched.

WHY THIS EXISTS

    Tony's ruling of Nov 17, 2026 (08:48): the night run checks NOAA and
    flags; Tony rebuilds the El Nino page by hand. A flag that cannot fire
    is a check that cannot fail. So every case here runs the real
    night_check() of enso_page_generator.py against NOAA's own files with
    one thing planted, and the first case runs on a copy of the module with
    a fault planted in its comparison, which this suite must catch.

THE FILES

    data/earth/noaa_enso_reads/2026-11-16/: the RONI file, the
    probabilities page and the discussion of 12 November 2026, as NOAA
    served them on Nov 16 and the first build saved them byte for byte.
    The page's state is written here to match them, as a build would.

    Each case runs in a throwaway folder; NOAA's address is never asked.
    The runner's own night_gate(), night_allowed() and night_title_flags()
    judge the folder output and the commit title.

Run: python test_enso_night_check.py (or the maintenance run's row "El
Nino check suite"). Last line: EL NINO CHECK SUITE: PASS or FAIL.

Role: devtool
Domain: earth_science

Module updated: November 2026 with Anthropic's Claude Opus 5.5
"""
import datetime
import importlib.util
import json
import os
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
FIXTURE = os.path.join(HERE, "data", "earth", "noaa_enso_reads",
                       "2026-11-16")
TODAY = datetime.date(2026, 11, 17)

# What the page showed when the fixture was read (the build of Nov 16):
# the discussion of 12 November 2026, RONI to ASO 2026, chances issued
# November 2026. Read from the fixture's own lines below, not retyped,
# except as the planted values each case names.
STATE = {
    "built": "2026-11-16",
    "discussion_issued": "2026-11-12",
    "roni_newest": "ASO 2026",
    "probabilities_issued": "November 2026",
}


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def fixture():
    out = {}
    for key, fname in (("roni", "RONI.ascii.txt"),
                       ("probabilities", "enso_probabilities.html"),
                       ("discussion", "ensodisc.html")):
        with open(os.path.join(FIXTURE, fname), "rb") as fh:
            out[key] = fh.read()
    return out


def run_case(mod, files, outage=None):
    """night_check() in a fresh throwaway folder, NOAA served from
    `files`. Returns (rc, line, every file under the folder)."""
    tmp = tempfile.mkdtemp(prefix="enso_night_")
    cwd = os.getcwd()
    real_get = mod._get
    try:
        os.chdir(tmp)
        os.makedirs(os.path.join("data", "earth"))
        with open(mod.STATE_FILE, "w", encoding="ascii",
                  newline="\n") as fh:
            json.dump(STATE, fh)
        by_url = dict((url, key) for key, url, _f in mod.READ_FILES)

        def fake_get(url):
            if outage:
                raise mod.EnsoBuildStop(outage)
            return files[by_url[url]], {}
        mod._get = fake_get
        rc, line = mod.night_check(TODAY)
        rc2, line2 = mod.night_check(TODAY)
        found = []
        for root, _d, names in os.walk("."):
            for n in names:
                found.append(os.path.relpath(os.path.join(root, n), ".")
                             .replace(os.sep, "/"))
        with open(mod.STATE_FILE, encoding="ascii") as fh:
            state_after = json.load(fh)
        return rc, line, sorted(found), (rc2, line2), state_after
    finally:
        mod._get = real_get
        os.chdir(cwd)
        shutil.rmtree(tmp, ignore_errors=True)


def main():
    findings, checks = [], [0]

    def check(ok, name, detail):
        checks[0] += 1
        if not ok:
            findings.append("%s: %s" % (name, detail))

    gen_path = os.path.join(HERE, "enso_page_generator.py")
    mod = load(gen_path, "enso_under_test")
    real = fixture()
    copies = "data/earth/noaa_enso_reads/%s/" % TODAY.isoformat()
    state_file = "data/earth/el_nino_state.json"

    # The plant: a newer discussion, issued 10 December 2026.
    newer_disc = dict(real)
    newer_disc["discussion"] = real["discussion"].replace(
        b"12 November 2026", b"10 December 2026", 1)
    check(newer_disc["discussion"] != real["discussion"], "PLANT",
          "the discussion's date was not found to plant over")

    # 0. A planted fault in a copy of the module must be caught: the
    #    discussion's comparison turned off.
    tmpd = tempfile.mkdtemp(prefix="enso_fault_")
    try:
        with open(gen_path, "rb") as fh:
            src = fh.read()
        bad = src.replace(b'if disc["issued"] > shown:',
                          b'if disc["issued"] > shown and False:', 1)
        check(bad != src, "FAULT NOT PLANTED", "the comparison line moved")
        fpath = os.path.join(tmpd, "enso_fault.py")
        with open(fpath, "wb") as fh:
            fh.write(bad)
        faulty = load(fpath, "enso_fault")
        rc, line, _f, _second, _s = run_case(faulty, newer_disc)
        check(mod.NIGHT_FLAG not in line, "PLANTED FAULT NOT CAUGHT",
              "a module that ignores the discussion's date still said %r"
              % line)
    finally:
        shutil.rmtree(tmpd, ignore_errors=True)

    # 1. NOAA's files as the page shows them: CURRENT, nothing written.
    rc, line, found, second, state = run_case(mod, real)
    print("  today's real files:  %s" % line)
    check(rc == 0 and "CURRENT" in line and mod.NIGHT_FLAG not in line,
          "QUIET ON TODAY'S FILES", "said %r (exit %d)" % (line, rc))
    check(found == [state_file], "WROTE WHEN CURRENT",
          "files after the night: %s" % found)

    # 2. A newer discussion: EL NINO DUE, the three copies saved.
    rc, line, found, second, state = run_case(mod, newer_disc)
    print("  planted discussion:  %s" % line)
    check(rc == 0 and mod.NIGHT_FLAG in line, "DUE NOT FLAGGED",
          "a discussion of 10 December said %r (exit %d)" % (line, rc))
    want = sorted([state_file] + [copies + f for f in (
        "RONI.ascii.txt", "enso_probabilities.html", "ensodisc.html")])
    check(found == want, "COPIES NOT SAVED",
          "files after the night: %s, wanted %s" % (found, want))
    check(second[0] == 0 and mod.NIGHT_FLAG in second[1]
          and "already saved" in second[1], "SECOND NIGHT",
          "the same files a second night said %r" % (second[1],))
    check(state == STATE, "STATE CHANGED", "the night wrote %s" % state)
    check(not any(f.endswith((".html", ".png")) and "noaa_enso_reads"
                  not in f for f in found), "PAGE TOUCHED",
          "the night wrote %s" % found)
    with open(os.path.join(FIXTURE, "ensodisc.html"), "rb") as fh:
        check(fh.read() == real["discussion"], "FIXTURE CHANGED",
              "the saved discussion of Nov 16 changed")

    # 3. A newer RONI season.
    newer_roni = dict(real)
    newer_roni["roni"] = real["roni"].rstrip(b"\n") + b"\nSON  2026  2.10\n"
    rc, line, found, _s, _st = run_case(mod, newer_roni)
    check(rc == 0 and mod.NIGHT_FLAG in line and "RONI to SON 2026" in line,
          "RONI NOT FLAGGED", "a season SON 2026 said %r" % line)

    # 4. Chances issued in a later month.
    newer_p = dict(real)
    newer_p["probabilities"] = real["probabilities"].replace(
        b"Issued November 2026", b"Issued December 2026", 1)
    rc, line, found, _s, _st = run_case(mod, newer_p)
    check(rc == 0 and mod.NIGHT_FLAG in line
          and "chances issued December 2026" in line,
          "CHANCES NOT FLAGGED", "chances of December said %r" % line)

    # 5. NOAA unreachable: reported, nothing written.
    rc, line, found, _s, _st = run_case(mod, real, outage="timed out")
    check(rc == 1 and "UNREACHABLE" in line and found == [state_file],
          "OUTAGE", "an outage said %r (exit %d), files %s"
          % (line, rc, found))

    # 6. NOAA's sentence gone: reported, not a guess.
    gone = dict(real)
    gone["discussion"] = real["discussion"].replace(b"historic event",
                                                    b"large event")
    rc, line, found, _s, _st = run_case(mod, gone)
    check(rc == 1 and "UNREACHABLE" in line and "historic event" in line,
          "FORMAT CHANGE", "a changed discussion said %r" % line)

    # 7. The runner: the folder output, the gate and the title.
    runner = load(os.path.join(HERE, "orrery_maintenance_run.py"),
                  "runner_under_test")
    allowed = ["data/earth/noaa_enso_reads/", "data/nightly_run_record.json"]
    check(runner.night_allowed(copies + "ensodisc.html", allowed),
          "COPY REFUSED", "the night may not commit a dated copy")
    check(not runner.night_allowed("data/earth/el_nino.html", allowed),
          "PAGE ALLOWED", "the night may commit the page")
    check(not runner.night_allowed("data/earth/noaa_enso_reads_x.txt",
                                   allowed),
          "SIBLING ALLOWED", "a name beside the folder is allowed")
    rows = [r for r in runner.night_rows()[0] if r[0] == "El Nino check"]
    check(rows and rows[0][2] == ["data/earth/noaa_enso_reads/"],
          "ROW", "the night's El Nino row is %s" % rows)
    tmpr = tempfile.mkdtemp(prefix="enso_title_")
    try:
        os.makedirs(os.path.join(tmpr, "data"))
        for verdict, want_title in (
                ("EL NINO DUE -- NOAA has newer", "EL NINO DUE "),
                ("CURRENT -- the page shows NOAA's latest", "")):
            with open(os.path.join(tmpr, runner.NIGHT_RECORD), "w") as fh:
                json.dump({"rows": [{"row": "El Nino check",
                                     "verdict": verdict}]}, fh)
            got = runner.night_title_flags(tmpr)
            check(got == want_title, "TITLE",
                  "a verdict %r gave the title flag %r" % (verdict, got))
    finally:
        shutil.rmtree(tmpr, ignore_errors=True)

    if findings:
        for f in findings:
            print("  FINDING %s" % f)
        print("EL NINO CHECK SUITE: FAIL -- %d of %d checks failed"
              % (len(findings), checks[0]))
        return 1
    print("EL NINO CHECK SUITE: PASS -- %d checks: a planted fault caught; "
          "a newer discussion, RONI season and chances each flag EL NINO "
          "DUE and save the copies once; NOAA's files as the page shows "
          "them write nothing; an outage and a changed sentence are "
          "reported; the page is never touched; the folder output, the "
          "gate and the commit title hold." % checks[0])
    return 0


if __name__ == "__main__":
    sys.exit(main())
