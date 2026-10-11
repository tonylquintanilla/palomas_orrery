"""
test_hills_cloud_sampler.py - the Hills cloud's three checks, and proof
that each one can fail.

hills_cloud_sampler.check() judges the sample drawn from constants_new.py
on three things: the frame (Sgr A* within a degree of galactic longitude
and latitude 0), the reading of the paper's Fig. 3 (most of its dots inside the
caption's ranges), and the tilt (the plane through the dots within 10
degrees of the paper's "about 30"). A check that passes is only worth
something if it can fail, so this file first plants a fault for each one
and requires the right check to catch it, then runs the real rows:

    planted                           must be caught by
    the pole's RA and Dec swapped     frame
    the ecliptic node row set to 0    frame
    the reading moved 120 deg along   reading
    the tilt row set to 60 deg        tilt

The last line starts "HILLS CLOUD:", which the maintenance run quotes.

Run (VS Code Run button, or):
    python test_hills_cloud_sampler.py

Role: dev_tools
Domain: orrery

Module updated: October 10, 2026 with Anthropic's Claude Opus 5.5 (L-421)
"""
import sys

import hills_cloud_sampler as hcs


def _planted():
    rows = hcs.rows_from_store()

    swapped = dict(rows)
    swapped['GALACTIC_NORTH_POLE_RA_J2000_DEG'] = rows['GALACTIC_NORTH_POLE_DEC_J2000_DEG']
    swapped['GALACTIC_NORTH_POLE_DEC_J2000_DEG'] = rows['GALACTIC_NORTH_POLE_RA_J2000_DEG']

    no_node = dict(rows)
    no_node['ECLIPTIC_NODE_GALACTIC_LON_DEG'] = 0

    moved = dict(rows)
    moved['HILLS_CLOUD_PLANES_READ'] = {
        '%d,%s' % ((int(key.split(',')[0]) + 120) % 360, key.split(',')[1]): count
        for key, count in rows['HILLS_CLOUD_PLANES_READ'].items()}

    steep = dict(rows)
    steep['HILLS_CLOUD_TILT_DEG'] = 60

    return [('the pole\'s RA and Dec swapped', swapped, 'frame'),
            ('the ecliptic node row set to 0', no_node, 'frame'),
            ('the reading moved 120 deg along', moved, 'reading'),
            ('the tilt row set to 60 deg', steep, 'tilt')]


def main():
    problems = []
    for label, rows, expected in _planted():
        failures, _info = hcs.check(rows)
        caught = [f for f in failures if f.startswith(expected + ':')]
        if caught:
            print('planted: %-34s caught by %s' % (label, expected))
        else:
            problems.append('planted fault "%s" was NOT caught by the %s check '
                            '(failures: %s)' % (label, expected, failures or 'none'))
            print('planted: %-34s NOT CAUGHT' % label)

    failures, info = hcs.check()
    for line in failures:
        problems.append('real rows: ' + line)
    lon, lat = info['sgr_a_galactic_lon_lat_deg']
    print('real rows: plane tilt %.1f deg, Sgr A* at galactic %.2f, %.2f deg, '
          '%.0f%% of Fig. 3 inside its caption'
          % (info['plane_tilt_deg'], lon, lat, 100 * info['fig3_share_in_caption']))
    if problems:
        for line in problems:
            print('FAIL: ' + line)
        print('HILLS CLOUD: FAIL -- %d problem(s)' % len(problems))
        return 1
    print('HILLS CLOUD: PASS -- 4 of 4 planted faults caught; the real rows '
          'pass, the dots\' plane tilted %.1f deg' % info['plane_tilt_deg'])
    return 0


if __name__ == '__main__':
    sys.exit(main())
