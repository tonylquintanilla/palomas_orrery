"""
test_hills_cloud_sampler.py - the Hills cloud's three checks, and proof
that each one can fail.

hills_cloud_sampler.check() judges the sample drawn from constants_new.py
on four things: the frame (Sgr A* within a degree of galactic longitude
and latitude 0), the reading of the paper's Fig. 3 (most of its dots inside the
caption's ranges), and the tilt (the plane through the dots within 10
degrees of the paper's "about 30") and, since L-460, the edges (every
dot between the cloud's inner edge and the far end of its band, in the
large sample and in the drawing) and, since L-434, the fill-in (the dots
rising across the inner edge's range). A check that passes is only worth
something if it can fail, so this file first plants a fault for each one
and requires the right check to catch it, then runs the real rows:

    planted                           must be caught by
    the pole's RA and Dec swapped     frame
    the ecliptic node row set to 0    frame
    the reading moved 120 deg along   reading
    the tilt row set to 60 deg        tilt
    one drawn dot moved to 257 AU     edges
    the disk drawn full from 2,000 AU fill-in

The last line starts "HILLS CLOUD:", which the maintenance run quotes.

Run (VS Code Run button, or):
    python test_hills_cloud_sampler.py

Role: dev_tools
Domain: orrery

Module updated: October 10, 2026 with Anthropic's Claude Opus 5.5 (L-421)
Module updated: October 21, 2026 with Anthropic's Claude Opus 5.5 (L-460:
the edges check, and its planted fault)
Module updated: October 22, 2026 with Anthropic's Claude Opus 5.5 (L-434:
the fill-in check, and its planted fault: the disk drawn full from the
inner edge's low end, as it was until this day)
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

    # L-434: the range collapsed onto its low end, which draws the disk
    # full from there, as it was drawn until 2026-10-22.
    full = dict(rows)
    full['OORT_CLOUD_INNER_EDGE_HIGH_AU'] = rows['INNER_LIMIT_OORT_CLOUD_AU'] + 1e-6

    return [('the pole\'s RA and Dec swapped', swapped, 'frame'),
            ('the ecliptic node row set to 0', no_node, 'frame'),
            ('the reading moved 120 deg along', moved, 'reading'),
            ('the tilt row set to 60 deg', steep, 'tilt'),
            ('the disk drawn full from 2,000 AU', full, 'fill-in')]


def main():
    problems = []
    # L-460: a dot back where the drawing used to put one, 257 AU out.
    rows = hcs.rows_from_store()
    dots = hcs.drawn_hills_cloud(rows)
    dots['x'][0], dots['y'][0], dots['z'][0] = 257.0, 0.0, 0.0
    caught = [f for f in hcs.edge_failures(dots, rows) if f.startswith('edges:')]
    if caught:
        print('planted: %-34s caught by edges' % 'one drawn dot moved to 257 AU')
    else:
        problems.append('planted fault "one drawn dot moved to 257 AU" was NOT '
                        'caught by the edges check')
        print('planted: %-34s NOT CAUGHT' % 'one drawn dot moved to 257 AU')
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
    print('HILLS CLOUD: PASS -- 6 of 6 planted faults caught; the real rows '
          'pass, the dots\' plane tilted %.1f deg' % info['plane_tilt_deg'])
    return 0


if __name__ == '__main__':
    sys.exit(main())
