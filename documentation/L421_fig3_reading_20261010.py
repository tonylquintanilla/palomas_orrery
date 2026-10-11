"""
L421_fig3_reading_20261010.py - how Fig. 3 of Nesvorny et al. (2025) was
read into the table HILLS_CLOUD_PLANES_READ in constants_new.py.

A RECORD, NOT A TOOL ON ANY BUILD PATH. It is kept so the reading can be
checked and repeated. Nothing imports it and the maintenance run does not
run it.

What it reads: Fig. 3 of Nesvorny, Dones, Vokrouhlicky, Levison, Beauge,
Faherty, Emmart and Parker, "A Spiral Structure in the Inner Oort Cloud",
arXiv:2502.11252v1 (ApJ 983:1, 2025), page 19 of the arXiv PDF: the
orbits of the model's inner Oort cloud bodies, one dot each, by galactic
nodal longitude (Omega_G, across) and galactic inclination (i_G, up).

How (Tony's ruling of 2026-10-10: "follow the paper. Draw following
figure 3 and describe following the text. And cite everything."):

1. The figure is a picture inside the PDF (a JPEG, 714 x 551 pixels),
   so it is read as it is stored, not re-drawn:
       pdfimages -f 19 -l 19 -j 2502.11252v1.pdf fig3
   which writes fig3-000.jpg.
2. The plot's frame is found as the long dark lines: Omega_G 0 to 360
   across, i_G 0 to 180 up. The calibration is CHECKED against three
   lines the figure draws itself, and the script stops if any is off by
   more than one degree: the red "ecliptic node" line at Omega_G = 186
   (the caption's value), the red "ecliptic plane" line at i_G = 60, and
   the black "polar orbits" line at i_G = 90.
3. Dark pixels are counted in cells 10 degrees of Omega_G by 5 degrees of
   i_G. Left out: the black polar-orbits line and a band of pixels either
   side of it, the frame's edges and tick marks, and the three black
   labels ("Retrograde", "Prograde", "polar orbits"). Each cell's
   coverage is its dark pixels over the pixels left in it.
4. Where dots overlap, coverage undercounts them. For dots of area a
   placed at random, the covered fraction f of an area A holding n dots
   is 1 - exp(-n a / A), so n = -(A / a) ln(1 - f). The dot area a is
   the median size of the figure's isolated dots.
5. Each cell's estimated dot count is rounded to a whole number; cells
   with none are left out.
6. WHAT THE FIGURE CANNOT SAY. In its densest part, Omega_G about 140 to
   175 and i_G about 80 to 90, the dots run together into solid black,
   and no reading can count them: those cells are SATURATED, held at the
   most the method gives (coverage taken as 99.9%), and named in the
   output. The true count there is unknown and probably higher, so the
   table, if anything, gives the core too little weight. Dots under the
   three black labels and under the figure's blue arrows, star and
   lettering are lost; those parts of the plot are sparse.

Printed at the end: the table as it is written into constants_new.py,
the total, the share inside the caption's ranges, and the calibration.

Run (in the sandbox; needs numpy, scipy and Pillow):
    python L421_fig3_reading_20261010.py fig3-000.jpg

Module updated: October 10, 2026 with Anthropic's Claude Opus 5.5 (L-421)
"""
import sys
import math

import numpy as np
from PIL import Image
from scipy import ndimage

NODE_BIN_DEG = 10
INCL_BIN_DEG = 5


def find_frame(dark):
    """Pixel edges of the plot frame: (x_left, x_right, y_bottom, y_top)."""
    h, w = dark.shape
    rows = dark.sum(axis=1)
    cols = dark.sum(axis=0)
    long_rows = [y for y in range(h) if rows[y] > 0.7 * w]
    long_cols = [x for x in range(w) if cols[x] > 0.6 * h]
    return min(long_cols), max(long_cols), max(long_rows), min(long_rows)


def main(png):
    rgb = np.asarray(Image.open(png).convert('RGB')).astype(int)
    # dark, and not the figure's red or blue lettering (JPEG darkens
    # their edges)
    dark = ((rgb.sum(axis=2) < 250)
            & (rgb[:, :, 0] - rgb[:, :, 1] < 60)
            & (rgb[:, :, 2] - rgb[:, :, 0] < 40))
    red = (rgb[:, :, 0] > 180) & (rgb[:, :, 1] < 80) & (rgb[:, :, 2] < 80)
    x0, x1, y0, y1 = find_frame(dark)

    def node_of(x):
        return (x - x0) / float(x1 - x0) * 360.0

    def incl_of(y):
        return (y0 - y) / float(y0 - y1) * 180.0

    def x_of(node):
        return x0 + node / 360.0 * (x1 - x0)

    def y_of(incl):
        return y0 - incl / 180.0 * (y0 - y1)

    px = (x1 - x0) / 360.0                       # pixels per degree, across
    py = (y0 - y1) / 180.0                       # pixels per degree, up
    m = int(round(4 * px))
    inner = (slice(y1 + m, y0 - m), slice(x0 + m, x1 - m))
    red_in = np.zeros_like(red)
    red_in[inner] = red[inner]
    x_red = int(np.argmax(red_in.sum(axis=0)))
    y_red = int(np.argmax(red_in.sum(axis=1)))
    dark_mid = np.zeros_like(dark)
    dark_mid[y1 + m:y0 - m, int(x_of(20)):int(x_of(200))] = \
        dark[y1 + m:y0 - m, int(x_of(20)):int(x_of(200))]
    y_polar = int(np.argmax(dark_mid.sum(axis=1)))
    checks = [('ecliptic node line, Omega_G', node_of(x_red), 186.0),
              ('ecliptic plane line, i_G', incl_of(y_red), 60.0),
              ('polar orbits line, i_G', incl_of(y_polar), 90.0)]
    for label, got, want in checks:
        print('calibration: %-28s read %7.2f, figure says %5.1f' % (label, got, want))
        if abs(got - want) > 1.0:
            raise SystemExit('STOP: the calibration is off by more than one degree.')

    usable = np.zeros_like(dark)
    mx = int(round(5 * px))                      # the frame and its ticks
    my = int(round(8 * py))
    usable[y1 + my:y0 - my, x0 + mx:x1 - mx] = True
    half = int(round(1.5 * py)) + 1              # the polar-orbits line
    usable[y_polar - half:y_polar + half + 1, :] = False
    for n_lo, n_hi, i_lo, i_hi in ((0, 125, 135, 180),    # "Retrograde"
                                   (0, 105, 0, 35),       # "Prograde"
                                   (255, 360, 80, 100)):  # "polar orbits"
        usable[int(y_of(i_hi)):int(y_of(i_lo)) + 1,
               int(x_of(n_lo)):int(x_of(n_hi)) + 1] = False
    ink = dark & usable

    labels, count = ndimage.label(ink)
    sizes = ndimage.sum(ink, labels, range(1, count + 1))
    single = sizes[(sizes >= 3) & (sizes <= 30)]
    dot_area = float(np.median(single))
    print('dot area: %.0f pixels, the median of %d isolated dots' % (dot_area, single.size))

    table = {}
    saturated = []
    for node in range(0, 360, NODE_BIN_DEG):
        xa, xb = int(round(x_of(node))), int(round(x_of(node + NODE_BIN_DEG)))
        for incl in range(0, 180, INCL_BIN_DEG):
            ya, yb = int(round(y_of(incl + INCL_BIN_DEG))), int(round(y_of(incl)))
            area = usable[ya:yb, xa:xb].sum()
            if area < 0.2 * (yb - ya) * (xb - xa):
                continue
            covered = ink[ya:yb, xa:xb].sum() / float(area)
            if covered <= 0:
                continue
            if covered > 0.999:
                saturated.append((node, incl))
            covered = min(covered, 0.999)
            # the cell's whole area, so pixels left out are filled at the
            # density of the pixels kept
            full = (yb - ya) * (xb - xa)
            n = -(full / dot_area) * math.log(1.0 - covered)
            if round(n) >= 1:
                table[(node, incl)] = int(round(n))

    total = sum(table.values())
    inside = sum(v for (n, i), v in table.items() if 120 <= n < 180 and 75 <= i < 90)
    print('cells: %d, estimated dots: %d' % (len(table), total))
    print('saturated cells (solid black, count unknown, held at the cap): %s'
          % ', '.join('%d,%d' % c for c in sorted(saturated)))
    print('inside the caption\'s ranges (Omega_G 120-180, i_G 75-90): %.0f%%'
          % (100.0 * inside / total))
    print('')
    # One entry per line: constants_change_report.py reads a dict entry
    # only on a line of its own.
    print('HILLS_CLOUD_PLANES_READ = {')
    for key in sorted(table):
        print("    '%d,%d': %d," % (key[0], key[1], table[key]))
    print('}')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    main(sys.argv[1])
