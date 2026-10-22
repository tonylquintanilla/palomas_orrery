"""
patch_L460_3_hills_inside_edges_20261021.py - the Hills cloud's dots stay
inside the cloud's sourced edges (L-460, Tony's check of the drawings).

Built on 4a40d27cdb5609e226962efda02c77131e0b59bd at
https://github.com/tonylquintanilla/palomas_orrery (branch main). It edits
two files the earlier two patches of the evening do not touch, so it can
run in any order with them.

WHAT IT DOES
    The Hills cloud is drawn as dots along orbits stretched by the
    declared eccentricity 0.8, evenly in time. Dots near an orbit's near
    end fell inside the cloud's inner edge of 2,000 AU, as close as
    257 AU, where no row puts the cloud: Nesvorny et al. (2025) place the
    inner cloud by distance from the Sun. Now the dots go only on the part
    of each orbit no nearer than the inner edge, still evenly in time
    there, and a fourth check, the edges, holds every dot between the
    inner edge and INNER_OORT_CLOUD_AU, with a planted fault (a dot at
    257 AU) that it must catch.
    - hills_cloud_sampler.py: the placement, the check, the docstring.
    - test_hills_cloud_sampler.py: the planted fault; five of five.

HOW TO RUN
    Save into the palomas_orrery folder, open in VS Code, click Run.
    (python patch_L460_3_hills_inside_edges_20261021.py)
    Success: one "ok" line per file, then "patch applied".
    Failure: "ERROR:" or "ANCHOR FAIL", and NOTHING was written.
    Undo is Discard Changes in GitHub Desktop.

AFTER RUNNING
    Move this file to documentation/. The orrery maintenance run's
    Drawings Export step rewrites data/drawings/hills_cloud.json: nearest
    dot 2,000 AU (was 257), 3,600 dots. Expect 31 of 31, "Hills cloud
    sampler" 5 of 5, the gate path at 0. Commit and push. Look at the
    Hills cloud in the orrery: the inside of the disk is now empty to
    2,000 AU.

Module written: October 21, 2026 with Anthropic's Claude Opus 5.5.

Role: devtool
Domain: dev_tools
"""
AFTER = ('Next: the orrery maintenance run (it re-exports the Hills cloud), '
         'then commit and push.')

import hashlib
import sys

FINGERPRINTS = {'hills_cloud_sampler.py': '25e59a23c6b8383500c5b5d52bb1dab5', 'test_hills_cloud_sampler.py': '769da31ee30e0c4e34d8af1832582e6b'}

EDITS = {'hills_cloud_sampler.py': [("- Every orbit has the eccentricity HILLS_CLOUD_ECCENTRICITY, a declared\n  pick. Dots go along each orbit evenly in TIME, so they gather at the\n  far ends, where a body spends most of its time, and that is where the\n  arms show. Dots near an orbit's near end can fall inside the cloud's\n  inner edge, as a real body on that orbit would.\n- The galactic angles are turned into the drawing's frame, the ecliptic\n  of J2000, by the matrix pole_frames.create_pole_transformation_matrix\n  builds about the north galactic pole (the rows the galactic tide is\n", "- Every orbit has the eccentricity HILLS_CLOUD_ECCENTRICITY, a declared\n  pick. Dots go along each orbit evenly in TIME, so they gather at the\n  far ends, where a body spends most of its time, and that is where the\n  arms show. They go only on the part of each orbit inside the cloud,\n  no nearer the Sun than its inner edge (INNER_LIMIT_OORT_CLOUD_AU): the\n  paper places the inner cloud by distance from the Sun (sec. 1, p. 2,\n  the row INNER_OORT_DISK_OUTER_AU), so no dot is drawn closer in.\n  FIXED 2026-10-21 (L-460): until then dots near an orbit's near end\n  fell inside the edge, to 257 AU, which no row allowed; a drawing ends\n  where a sourced row says it does (Tony, 2026-10-21).\n- The galactic angles are turned into the drawing's frame, the ecliptic\n  of J2000, by the matrix pole_frames.create_pole_transformation_matrix\n  builds about the north galactic pole (the rows the galactic tide is\n"), ('Module updated: October 11, 2026 with Anthropic\'s Claude Opus 5.5 (L-421,\nthe website half: drawn_hills_cloud() and its three settings, so the\norrery and the website draw the same seeded dots)\n"""\nimport math\n\n', 'Module updated: October 11, 2026 with Anthropic\'s Claude Opus 5.5 (L-421,\nthe website half: drawn_hills_cloud() and its three settings, so the\norrery and the website draw the same seeded dots)\nModule updated: October 21, 2026 with Anthropic\'s Claude Opus 5.5 (L-460:\ndots only on the part of each orbit inside the cloud\'s inner edge, still\nevenly in time there; a fourth check, the edges, that every dot lies\nbetween the inner edge and INNER_OORT_CLOUD_AU)\n"""\nimport math\n\n'), ("                        float(rows['INNER_OORT_CLOUD_AU']), rng)\n    a = aphelion / (1.0 + e)\n\n    mean_anomaly = rng.uniform(0, 2 * np.pi, (n_orbits, points_per_orbit))\n    big_e = _eccentric_anomaly(mean_anomaly, e)\n    in_x = a[:, None] * (np.cos(big_e) - e)\n    in_y = a[:, None] * math.sqrt(1.0 - e * e) * np.sin(big_e)\n", "                        float(rows['INNER_OORT_CLOUD_AU']), rng)\n    a = aphelion / (1.0 + e)\n\n    # L-460: evenly in time, but only on the part of the orbit no nearer\n    # the Sun than the cloud's inner edge. r = a (1 - e cos E) >= r_in\n    # where cos E <= (1 - r_in / a) / e; E0 is where that starts, and the\n    # mean anomaly M0 = E0 - e sin E0. A whole orbit outside the edge has\n    # E0 = 0, so nothing changes for it.\n    r_in = float(rows['INNER_LIMIT_OORT_CLOUD_AU'])\n    big_e0 = np.arccos(np.clip((1.0 - r_in / a) / e, -1.0, 1.0))\n    m0 = big_e0 - e * np.sin(big_e0)\n    share = rng.uniform(0, 1, (n_orbits, points_per_orbit))\n    mean_anomaly = m0[:, None] + share * (2 * np.pi - 2 * m0[:, None])\n    big_e = _eccentric_anomaly(mean_anomaly, e)\n    in_x = a[:, None] * (np.cos(big_e) - e)\n    in_y = a[:, None] * math.sqrt(1.0 - e * e) * np.sin(big_e)\n"), ('    }\n\n\ndef check(rows=None, seed=421, frame_tolerance_deg=1.0, tilt_tolerance_deg=10.0):\n    """The three checks, as a list of failure sentences (empty: all pass),\n    and the description they were judged on, from 4,000 orbits so the\n    tilt barely moves between runs. The two tolerances are the checks\'\n    own settings, not read from a source: a degree is well above how far\n', '    }\n\n\ndef edge_failures(sample, rows, slack_au=1.0):\n    """The edges check: every dot between the cloud\'s inner edge\n    (INNER_LIMIT_OORT_CLOUD_AU) and the far end of its band\n    (INNER_OORT_CLOUD_AU). slack_au allows for the stored file\'s rounding\n    of each coordinate to the whole AU (L-460)."""\n    r = np.sqrt(np.asarray(sample[\'x\']) ** 2 + np.asarray(sample[\'y\']) ** 2\n                + np.asarray(sample[\'z\']) ** 2)\n    lo = rows[\'INNER_LIMIT_OORT_CLOUD_AU\'] - slack_au\n    hi = rows[\'INNER_OORT_CLOUD_AU\'] + slack_au\n    out = []\n    inside = r < lo\n    beyond = r > hi\n    if inside.any():\n        out.append(\'edges: %d dot(s) inside the cloud\\\'s inner edge of %s AU, \'\n                   \'the nearest at %.0f AU\' % (int(inside.sum()),\n                   rows[\'INNER_LIMIT_OORT_CLOUD_AU\'], float(r.min())))\n    if beyond.any():\n        out.append(\'edges: %d dot(s) beyond %s AU, the farthest at %.0f AU\'\n                   % (int(beyond.sum()), rows[\'INNER_OORT_CLOUD_AU\'],\n                      float(r.max())))\n    return out\n\n\ndef check(rows=None, seed=421, frame_tolerance_deg=1.0, tilt_tolerance_deg=10.0):\n    """The four checks, as a list of failure sentences (empty: all pass),\n    and the description they were judged on, from 4,000 orbits so the\n    tilt barely moves between runs. The two tolerances are the checks\'\n    own settings, not read from a source: a degree is well above how far\n'), ('    catching a frame or a reading gone wrong."""\n    rows = rows_from_store() if rows is None else rows\n    failures = []\n    info = describe(sample_hills_cloud(4000, 6, rows, seed=seed), rows)\n    lon, lat = info[\'sgr_a_galactic_lon_lat_deg\']\n    if abs(lon) > frame_tolerance_deg or abs(lat) > frame_tolerance_deg:\n        failures.append(\'frame: Sgr A* falls at galactic longitude %.2f, \'\n', '    catching a frame or a reading gone wrong."""\n    rows = rows_from_store() if rows is None else rows\n    failures = []\n    sample = sample_hills_cloud(4000, 6, rows, seed=seed)\n    info = describe(sample, rows)\n    failures += edge_failures(sample, rows)\n    failures += edge_failures(drawn_hills_cloud(rows), rows)\n    lon, lat = info[\'sgr_a_galactic_lon_lat_deg\']\n    if abs(lon) > frame_tolerance_deg or abs(lat) > frame_tolerance_deg:\n        failures.append(\'frame: Sgr A* falls at galactic longitude %.2f, \'\n'), ("        for line in failures:\n            print('FAIL: ' + line)\n        return 1\n    print('PASS: frame, reading and tilt')\n    return 0\n\n\n", "        for line in failures:\n            print('FAIL: ' + line)\n        return 1\n    print('PASS: frame, reading, tilt and edges')\n    return 0\n\n\n")], 'test_hills_cloud_sampler.py': [('that each one can fail.\n\nhills_cloud_sampler.check() judges the sample drawn from constants_new.py\non three things: the frame (Sgr A* within a degree of galactic longitude\nand latitude 0), the reading of the paper\'s Fig. 3 (most of its dots inside the\ncaption\'s ranges), and the tilt (the plane through the dots within 10\ndegrees of the paper\'s "about 30"). A check that passes is only worth\nsomething if it can fail, so this file first plants a fault for each one\nand requires the right check to catch it, then runs the real rows:\n\n', 'that each one can fail.\n\nhills_cloud_sampler.check() judges the sample drawn from constants_new.py\non four things: the frame (Sgr A* within a degree of galactic longitude\nand latitude 0), the reading of the paper\'s Fig. 3 (most of its dots inside the\ncaption\'s ranges), and the tilt (the plane through the dots within 10\ndegrees of the paper\'s "about 30") and, since L-460, the edges (every\ndot between the cloud\'s inner edge and the far end of its band, in the\nlarge sample and in the drawing). A check that passes is only worth\nsomething if it can fail, so this file first plants a fault for each one\nand requires the right check to catch it, then runs the real rows:\n\n'), ('    the ecliptic node row set to 0    frame\n    the reading moved 120 deg along   reading\n    the tilt row set to 60 deg        tilt\n\nThe last line starts "HILLS CLOUD:", which the maintenance run quotes.\n\n', '    the ecliptic node row set to 0    frame\n    the reading moved 120 deg along   reading\n    the tilt row set to 60 deg        tilt\n    one drawn dot moved to 257 AU     edges\n\nThe last line starts "HILLS CLOUD:", which the maintenance run quotes.\n\n'), ('Domain: orrery\n\nModule updated: October 10, 2026 with Anthropic\'s Claude Opus 5.5 (L-421)\n"""\nimport sys\n\n', 'Domain: orrery\n\nModule updated: October 10, 2026 with Anthropic\'s Claude Opus 5.5 (L-421)\nModule updated: October 21, 2026 with Anthropic\'s Claude Opus 5.5 (L-460:\nthe edges check, and its planted fault)\n"""\nimport sys\n\n'), ("\ndef main():\n    problems = []\n    for label, rows, expected in _planted():\n        failures, _info = hcs.check(rows)\n        caught = [f for f in failures if f.startswith(expected + ':')]\n", '\ndef main():\n    problems = []\n    # L-460: a dot back where the drawing used to put one, 257 AU out.\n    rows = hcs.rows_from_store()\n    dots = hcs.drawn_hills_cloud(rows)\n    dots[\'x\'][0], dots[\'y\'][0], dots[\'z\'][0] = 257.0, 0.0, 0.0\n    caught = [f for f in hcs.edge_failures(dots, rows) if f.startswith(\'edges:\')]\n    if caught:\n        print(\'planted: %-34s caught by edges\' % \'one drawn dot moved to 257 AU\')\n    else:\n        problems.append(\'planted fault "one drawn dot moved to 257 AU" was NOT \'\n                        \'caught by the edges check\')\n        print(\'planted: %-34s NOT CAUGHT\' % \'one drawn dot moved to 257 AU\')\n    for label, rows, expected in _planted():\n        failures, _info = hcs.check(rows)\n        caught = [f for f in failures if f.startswith(expected + \':\')]\n'), ("            print('FAIL: ' + line)\n        print('HILLS CLOUD: FAIL -- %d problem(s)' % len(problems))\n        return 1\n    print('HILLS CLOUD: PASS -- 4 of 4 planted faults caught; the real rows '\n          'pass, the dots\\' plane tilted %.1f deg' % info['plane_tilt_deg'])\n    return 0\n\n", "            print('FAIL: ' + line)\n        print('HILLS CLOUD: FAIL -- %d problem(s)' % len(problems))\n        return 1\n    print('HILLS CLOUD: PASS -- 5 of 5 planted faults caught; the real rows '\n          'pass, the dots\\' plane tilted %.1f deg' % info['plane_tilt_deg'])\n    return 0\n\n")]}


def main():
    texts, crlf = {}, {}
    for path, want in FINGERPRINTS.items():
        try:
            with open(path, 'rb') as f:
                raw = f.read()
        except OSError as e:
            print('ERROR: cannot read %s (%s). Run from the folder this patch '
                  'names. NOTHING was written.' % (path, e))
            return 1
        crlf[path] = b'\r\n' in raw
        text = raw.replace(b'\r\n', b'\n').decode('utf-8')
        got = hashlib.md5(text.encode('utf-8')).hexdigest()
        if got != want:
            print('ERROR: %s is not the file this patch was built on '
                  '(fingerprint %s, expected %s). NOTHING was written.'
                  % (path, got, want))
            return 1
        texts[path] = text
    out = {}
    for path, pairs in EDITS.items():
        t = texts[path]
        for i, (old, new) in enumerate(reversed(pairs)):
            n = t.count(old)
            if n != 1:
                print('ANCHOR FAIL: %s edit %d matched %d times. NOTHING was '
                      'written.' % (path, len(pairs) - i, n))
                return 1
            t = t.replace(old, new)
        before = set(texts[path].split('\n'))
        bad = [x for x in t.split('\n') if x not in before and any(ord(c) > 127 for c in x)]
        if bad:
            print('ERROR: a line this patch inserts in %s is not ASCII. NOTHING '
                  'was written.' % path)
            return 1
        out[path] = t
        print('ok  %s: %d edit(s)' % (path, len(pairs)))
    for path, t in out.items():
        with open(path, 'wb') as f:
            f.write(t.encode('utf-8'))
        if crlf[path]:
            print('note: %s was CRLF in the working copy; written LF' % path)
    print(AFTER)
    print('patch applied')
    return 0


if __name__ == '__main__':
    sys.exit(main())
