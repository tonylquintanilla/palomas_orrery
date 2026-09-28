"""
patch_L322_D_17_chromosphere_rows_20260928.py -- ORRERY repo.

Built on 95b394f821891e4e704fc5d65bcc54ec556ed136
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Written 2026-09-28 with Anthropic's Claude Opus 5.5, Tony Quintanilla
integrator. L-322 Stage D. Rules: provenance-discipline 2.21 (Rule 3,
scaling; Rule 7's exact row), from patch_L322_D_16_prov221_skill.py.
Run D16 first; the two touch different files.

RUN

  Save this file in the ORRERY REPO ROOT (the folder that contains
  constants_new.py -- NOT documentation/), open it in VS Code and click
  Run. File it in documentation/ AFTER it has run.

WHAT THIS DOES -- four files

  constants_new.py
      SUN_RADIUS_KM gets a unit and "exact -- prints 4": the IAU 2015
      nominal solar radius is a definition, 6.957 x 10^5 km.
      CHROMOSPHERE_PHYSICAL_KM gets a unit and one figure: Carroll &
      Ostlie give about 2,000 km, so the zeros are placeholders.
      CHROMOSPHERE_TOP_KM is new: the Sun's radius plus the depth,
      698,000 km at three figures, for the gallery's kilometre line.
      CHROMOSPHERE_PHYSICAL_RADII is rewritten as the sum over the
      radius, which the unit check accepts, and counts to four figures,
      1.003 solar radii, under 2.21's scaling rule.
  test_derived_figures.py
      Check 3 applies the scaling rule: a sum multiplied or divided by an
      exact number keeps its decimal place, not its figure count. The OK
      line prints the place it kept. Five new fixtures test it, including
      a single measured value scaled, which still keeps fewest figures.
      Every existing row's verdict is unchanged.
  solar_visualization_shells.py
      The orrery's chromosphere hover prints its radius by its count,
      "1.003 solar radii" (was 1.002875); the Sun's radius through
      exact_text(), "695,700 km" as before; and the skin as a share of
      the radius at the depth's one figure, "0.3%" (was 0.29%).
  exact_rows_report.py
      The gallery's three pointers to SUN_RADIUS_KM go in its DRAWN
      table: the Sun room reads the row only to turn solar radii into
      kilometres, and never prints it as itself.

SUCCESS: one "ok" line per edit, then "patch applied" naming four files.
FAILURE: one ERROR: or ANCHOR FAIL: line, and NOTHING is written. Undo
after a success is Discard Changes in GitHub Desktop.

AFTERWARD
  1. (do) Run the orrery maintenance run. The export now carries four
     more rows (89 exported). "Exact rows by the count" stays red, as
     it has been since D15, until gallery patch 4 is run: it names the
     Earth room's eleven prints, nothing else. Every other checker
     should pass.
  2. (do) Commit and push the orrery.
  3. (do) Do NOT run the gallery maintenance run until gallery patch 5
     is ready. Its mirror step would copy the new values into the
     gallery (the chromosphere at 1.003, the Sun's radius as exact)
     before the Sun room's hover code is ready for them.
"""

import hashlib
import os
import sys

FINGERPRINTS = {'constants_new.py': '31273da90859fbf5550b473cf50e5ed9', 'test_derived_figures.py': '277f37795bda1733cff99955abe7c10d', 'solar_visualization_shells.py': 'd2e5a75273f3c4d78f6a4d9be67a47e8', 'exact_rows_report.py': 'cbe30b6293d52d657636198900b4c9d4'}

EDITS = {
    'constants_new.py': [('SUN_RADIUS_KM: unit, status, exact, prints 4', b'SUN_RADIUS_KM = 695700.0\n# Source: IAU 2015 Resolution B3 -- nominal solar radius\n', b"SUN_RADIUS_KM = 695700.0\n# Unit: km\n# Status: measured V_CROSS_CHECKED 2026-08-02\n# Figures: exact -- prints 4, the definition's own digits (6.957 x 10^5\n# Figures+: km). IAU 2015 Resolution B3 defines the nominal solar radius\n# Figures+: as exactly 6.957 x 10^8 m, a conversion constant, so every\n# Figures+: digit is known; the .0 is Python's (Rule 2).\n# Source: IAU 2015 Resolution B3 -- nominal solar radius\n", 1), ('CHROMOSPHERE_PHYSICAL_KM: unit, status, 1 figure', b'CHROMOSPHERE_PHYSICAL_KM = 2000.0\n# Source: Carroll & Ostlie, An Introduction to Modern Astrophysics,\n', b'CHROMOSPHERE_PHYSICAL_KM = 2000.0\n# Unit: km\n# Status: measured V_CROSS_CHECKED 2026-08-02\n# Figures: 1 -- Carroll & Ostlie give about 2,000 km, so the zeros are\n# Figures+: placeholders and only the 2 counts (Rule 2); good to\n# Figures+: thousands of kilometres.\n# Source: Carroll & Ostlie, An Introduction to Modern Astrophysics,\n', 1), ('CHROMOSPHERE_TOP_KM and CHROMOSPHERE_PHYSICAL_RADII', b'CHROMOSPHERE_PHYSICAL_RADII = 1.0 + CHROMOSPHERE_PHYSICAL_KM / SUN_RADIUS_KM\n# Derived: 1 + 2000 / 695700 = 1.002875... solar radii\n', b"CHROMOSPHERE_TOP_KM = SUN_RADIUS_KM + CHROMOSPHERE_PHYSICAL_KM\n# Unit: km\n# Status: derived -- inherits SUN_RADIUS_KM, CHROMOSPHERE_PHYSICAL_KM\n# Figures: 3 -- set by CHROMOSPHERE_PHYSICAL_KM (2000, 1), good to\n# Figures+: thousands; SUN_RADIUS_KM is exact.\n# Derived: 695700 + 2000 = 698000 km from the Sun's centre\n# Note: the top of the chromosphere, for the hover's kilometre line.\n# Note+: L-322 Stage D, patch D17.\n\nCHROMOSPHERE_PHYSICAL_RADII = (SUN_RADIUS_KM + CHROMOSPHERE_PHYSICAL_KM) / SUN_RADIUS_KM\n# Unit: r_sun\n# Status: derived -- inherits SUN_RADIUS_KM, CHROMOSPHERE_PHYSICAL_KM\n# Figures: 4 -- thousandths: thousands place of the sum, set by\n# Figures+: CHROMOSPHERE_PHYSICAL_KM (2000, 1), carried through the exact\n# Figures+: SUN_RADIUS_KM (Rule 3, scaling, provenance-discipline 2.21)\n# Derived: (695700 + 2000) / 695700 = 1.003 solar radii\n# Note: written as the sum over the radius, not 1 + depth / radius: the\n# Note+: unit check refuses a bare 1 added to a ratio, and under 2.21 the\n# Note+: two forms count the same. It stays an expression over the\n# Note+: primaries, not CHROMOSPHERE_TOP_KM / SUN_RADIUS_KM, so the\n# Note+: checker follows it to them (Rule 4). L-322 Stage D, patch D17.\n", 1), ('stamp', b"observed reach. They replace five numbers chosen by eye in\nearth_visualization_shells.py)\nModule updated: September 27, 2026 with Anthropic's Claude Opus 5.5\n", b"observed reach. They replace five numbers chosen by eye in\nearth_visualization_shells.py)\nModule updated: September 28, 2026 with Anthropic's Claude Opus 5.5\n(L-322 Stage D, patch D17: the Sun's nominal radius, the chromosphere's\ndepth and radius gain units and figure counts, and the top of the\nchromosphere gets its own row, CHROMOSPHERE_TOP_KM, 698,000 km. The\nchromosphere's radius counts to 1.003 solar radii under\nprovenance-discipline 2.21's scaling rule.)\nModule updated: September 27, 2026 with Anthropic's Claude Opus 5.5\n", 1)],
    'test_derived_figures.py': [('Figures: the place-governed walk', b'    def ev(self, node):\n        """(value, figures or EXACT, decimal place or None)."""\n        if isinstance(node, ast.Constant) and isinstance(\n                node.value, (int, float)) and not isinstance(\n                node.value, bool):\n            return float(node.value), EXACT, None\n        if isinstance(node, ast.Name):\n            if node.id in self.by_name:\n                return self.leaf(node.id)\n            if node.id in self.NUMBERS:\n                return self.NUMBERS[node.id], EXACT, None\n            raise Stop("CANNOT JUDGE", "the name %s" % node.id)\n        if isinstance(node, ast.Attribute) and node.attr in self.NUMBERS:\n            return self.NUMBERS[node.attr], EXACT, None\n        if isinstance(node, ast.UnaryOp) and isinstance(\n                node.op, (ast.USub, ast.UAdd)):\n            value, figs, place = self.ev(node.operand)\n            return (-value if isinstance(node.op, ast.USub) else value,\n                    figs, place)\n        if isinstance(node, ast.BinOp):\n            left = self.ev(node.left)\n            right = self.ev(node.right)\n            op = node.op\n            if isinstance(op, (ast.Add, ast.Sub)):\n                value = (left[0] + right[0] if isinstance(op, ast.Add)\n                         else left[0] - right[0])\n                places = [p for p in (left[2], right[2]) if p is not None]\n                if not places:\n                    return value, EXACT, None\n                place = max(places)\n                if value == 0:\n                    raise Stop("CANNOT JUDGE", "a sum or difference in the "\n                               "expression is exactly zero")\n                return value, max(0, magnitude(value) - place + 1), place\n            if isinstance(op, ast.Mult):\n                value = left[0] * right[0]\n            elif isinstance(op, ast.Div):\n                value = left[0] / right[0]\n            elif isinstance(op, ast.Pow):\n                value = left[0] ** right[0]\n            else:\n                raise Stop("CANNOT JUDGE", "a %s operator"\n                           % type(op).__name__)\n            return self.limited(value, [left[1], right[1]])\n        if isinstance(node, ast.Call):\n            func = node.func\n            fname = (func.attr if isinstance(func, ast.Attribute) else\n                     func.id if isinstance(func, ast.Name) else None)\n            if fname not in self.FUNCS or node.keywords:\n                raise Stop("CANNOT JUDGE", "the call %s()" % fname)\n            parts = [self.ev(arg) for arg in node.args]\n            value = self.FUNCS[fname](*[p[0] for p in parts])\n            return self.limited(value, [p[1] for p in parts])\n        raise Stop("CANNOT JUDGE", "a %s node" % type(node).__name__)\n\n', b'    def ev(self, node):\n        """(value, figures or EXACT, decimal place or None)."""\n        return self._ev(node)[:3]\n\n    def _ev(self, node):\n        """(value, figures or EXACT, place or None, place-governed).\n\n        The fourth item is True for a sum or difference with a measured\n        part, and it stays True while the sum is scaled by exact parts:\n        such a value keeps its decimal place, carried through the\n        scaling, not its figure count (provenance-discipline 2.21,\n        Rule 3, scaling). A single measured value is not place-governed:\n        scaled by an exact row it keeps fewest figures, as 2.21 leaves it.\n        L-322 Stage D, patch D17.\n        """\n        if isinstance(node, ast.Constant) and isinstance(\n                node.value, (int, float)) and not isinstance(\n                node.value, bool):\n            return float(node.value), EXACT, None, False\n        if isinstance(node, ast.Name):\n            if node.id in self.by_name:\n                return self.leaf(node.id) + (False,)\n            if node.id in self.NUMBERS:\n                return self.NUMBERS[node.id], EXACT, None, False\n            raise Stop("CANNOT JUDGE", "the name %s" % node.id)\n        if isinstance(node, ast.Attribute) and node.attr in self.NUMBERS:\n            return self.NUMBERS[node.attr], EXACT, None, False\n        if isinstance(node, ast.UnaryOp) and isinstance(\n                node.op, (ast.USub, ast.UAdd)):\n            value, figs, place, governed = self._ev(node.operand)\n            return (-value if isinstance(node.op, ast.USub) else value,\n                    figs, place, governed)\n        if isinstance(node, ast.BinOp):\n            left = self._ev(node.left)\n            right = self._ev(node.right)\n            op = node.op\n            if isinstance(op, (ast.Add, ast.Sub)):\n                value = (left[0] + right[0] if isinstance(op, ast.Add)\n                         else left[0] - right[0])\n                places = [p for p in (left[2], right[2]) if p is not None]\n                if not places:\n                    return value, EXACT, None, False\n                place = max(places)\n                if value == 0:\n                    raise Stop("CANNOT JUDGE", "a sum or difference in the "\n                               "expression is exactly zero")\n                return (value, max(0, magnitude(value) - place + 1), place,\n                        True)\n            if isinstance(op, ast.Mult):\n                value = left[0] * right[0]\n            elif isinstance(op, ast.Div):\n                value = left[0] / right[0]\n            elif isinstance(op, ast.Pow):\n                value = left[0] ** right[0]\n            else:\n                raise Stop("CANNOT JUDGE", "a %s operator"\n                           % type(op).__name__)\n            scaled = self.scaled_by_exact(value, left, right, op)\n            if scaled is not None:\n                return scaled\n            return self.limited(value, [left[1], right[1]]) + (False,)\n        if isinstance(node, ast.Call):\n            func = node.func\n            fname = (func.attr if isinstance(func, ast.Attribute) else\n                     func.id if isinstance(func, ast.Name) else None)\n            if fname not in self.FUNCS or node.keywords:\n                raise Stop("CANNOT JUDGE", "the call %s()" % fname)\n            parts = [self._ev(arg) for arg in node.args]\n            value = self.FUNCS[fname](*[p[0] for p in parts])\n            return self.limited(value, [p[1] for p in parts]) + (False,)\n        raise Stop("CANNOT JUDGE", "a %s node" % type(node).__name__)\n\n    def scaled_by_exact(self, value, left, right, op):\n        """A place-governed part times, or divided by, an exact part.\n\n        provenance-discipline 2.21, Rule 3, scaling: the sum\'s place unit\n        is carried through the exact factor and snapped to the nearest\n        power of ten on a log scale, a tie going to the coarser place;\n        the count is the figures of the value down to that place. None\n        when the step is not that shape (then fewest figures applies).\n        Only a sum DIVIDED BY an exact part is a scaling; an exact part\n        divided by a sum is not. L-322 Stage D, patch D17.\n        """\n        if isinstance(op, ast.Mult):\n            pairs = ((left, right), (right, left))\n        elif isinstance(op, ast.Div):\n            pairs = ((left, right),)\n        else:\n            return None\n        for part, factor in pairs:\n            if (part[3] and part[1] is not EXACT and part[2] is not None\n                    and factor[1] is EXACT and factor[0] != 0\n                    and value != 0):\n                ratio = (abs(factor[0]) if isinstance(op, ast.Mult)\n                         else 1.0 / abs(factor[0]))\n                unit = 10.0 ** part[2] * ratio\n                place = int(math.floor(math.log10(unit) + 0.5))\n                self.places.append(place)\n                return (value, max(1, magnitude(value) - place + 1), place,\n                        True)\n        return None\n\n', 1), ('Figures: places found', b'        self.values = values\n        self.embedded = []\n', b'        self.values = values\n        self.embedded = []\n        # Places found by scaled_by_exact(), printed on the OK line so a\n        # wrong ceiling is seen and not only passed (2.21, Rule 8).\n        self.places = []\n', 1), ('check 3 records the place', b'            walker = Figures(by_name, values)\n            value, supported, _place = walker.ev(row.node)\n', b'            walker = Figures(by_name, values)\n            value, supported, _place = walker.ev(row.node)\n            if walker.places:\n                info["place"] = walker.places[-1]\n', 1), ('OK line prints the place', b'    if ceiling_u is None:\n        return "%s figures, within what its inputs support" % row.figures\n', b'    place = info.get("place")\n    scaled = ("" if place is None else\n              "; a sum scaled by an exact row, kept to place 10^%d "\n              "(Rule 3, scaling)" % place)\n    if ceiling_u is None:\n        return ("%s figures, within what its inputs support%s"\n                % (row.figures, scaled))\n', 1), ('docstring: check 3 names the scaling rule', b'         sums and differences are good to the coarsest decimal place\n         among their measured inputs;\n', b'         sums and differences are good to the coarsest decimal place\n         among their measured inputs;\n         a sum or difference multiplied or divided by an exact number\n         keeps its decimal place, carried through the scaling and\n         snapped to the nearest power of ten (provenance-discipline\n         2.21, Rule 3, scaling); the OK line prints the place it kept;\n', 1), ('docstring: stamp', b'(L-322 Stage D, patch D8: the uncertainty field\'s pattern is imported\nfrom constants_rows.py, its one home, rather than kept here.)\n"""\n', b'(L-322 Stage D, patch D8: the uncertainty field\'s pattern is imported\nfrom constants_rows.py, its one home, rather than kept here.)\nModule updated: September 28, 2026 with Anthropic\'s Claude Opus 5.5\n(L-322 Stage D, patch D17: check 3 applies provenance-discipline 2.21\'s\nscaling paragraph, and five fixtures test it, including the two forms\nof the chromosphere\'s arithmetic counting the same and a single measured\nvalue scaled by an exact number still keeping fewest figures.)\n"""\n', 1), ('fixtures: the scaling rows', b"# Figures: exact -- a declared construction\n# Derived: = 4.5\n'''\n", b"# Figures: exact -- a declared construction\n# Derived: = 4.5\nFIX_SUN_KM = 695700.0\n# Figures: exact -- a defined conversion constant\nFIX_SKIN_KM = 2000.0\n# Figures: 1 -- about 2000 km; the zeros are placeholders\nFIX_SCALED_SUM = (FIX_SUN_KM + FIX_SKIN_KM) / FIX_SUN_KM\n# Figures: 4 -- thousandths, set by FIX_SKIN_KM, through the exact FIX_SUN_KM\n# Derived: = 1.003\nFIX_SCALED_OVER = (FIX_SUN_KM + FIX_SKIN_KM) / FIX_SUN_KM\n# Figures: 5 -- set by FIX_SKIN_KM\n# Derived: = 1.0029\nFIX_SCALED_OTHER_FORM = 1.0 + FIX_SKIN_KM / FIX_SUN_KM\n# Figures: 4 -- set by FIX_SKIN_KM, thousandths\n# Derived: = 1.003\nFIX_SCALED_TIMES = 2.0 * (FIX_SUN_KM + FIX_SKIN_KM)\n# Figures: 4 -- set by FIX_SKIN_KM, the thousands place doubled\n# Derived: = 1.395e6\nFIX_SINGLE_SCALED = FIX_SKIN_KM * 2.54\n# Figures: 2 -- set by FIX_SKIN_KM\n# Derived: = 5100\n'''\n", 1), ('fixtures: expected verdicts', b'    "FIX_MID_NONAME": ["NAMES NO INPUT"],\n}\n', b'    "FIX_MID_NONAME": ["NAMES NO INPUT"],\n    # L-322 Stage D, patch D17: provenance-discipline 2.21, Rule 3,\n    # scaling. Both forms of the chromosphere\'s arithmetic keep the\n    # thousandths; one more figure is refused; a sum doubled keeps the\n    # doubled place; a single measured value scaled keeps fewest figures.\n    "FIX_SCALED_SUM": ["OK"],\n    "FIX_SCALED_OVER": ["OVER-DECLARED"],\n    "FIX_SCALED_OTHER_FORM": ["OK"],\n    "FIX_SCALED_TIMES": ["OK"],\n    "FIX_SINGLE_SCALED": ["OVER-DECLARED"],\n}\n', 1), ('fixtures: the OK line prints the place', b'                        ("FIX_LEO_OK", "propagation allows 10")):\n', b'                        ("FIX_LEO_OK", "propagation allows 10"),\n                        ("FIX_SCALED_SUM", "kept to place 10^-3")):\n', 1)],
    'solar_visualization_shells.py': [('import the figure helpers', b'                                            CHROMOSPHERE_PHYSICAL_KM, CHROMOSPHERE_PHYSICAL_RADII)\n', b'                                            CHROMOSPHERE_PHYSICAL_KM, CHROMOSPHERE_PHYSICAL_RADII)\n# L-322 Stage D, patch D17: print rows by the counts their rows state.\nfrom constants_rows import figures_of, exact_text, format_prints\n', 1), ('chromosphere line: radius by its count', b'    f"* Radius: drawn at true scale, {CHROMOSPHERE_PHYSICAL_RADII:.6f} solar radii<br>"\n', b'    f"* Radius: drawn at true scale, "\n    f"{format_prints(CHROMOSPHERE_PHYSICAL_RADII, figures_of(\'CHROMOSPHERE_PHYSICAL_RADII\'))} solar radii<br>"\n', 1), ('chromosphere line: solar radius by its print count', b'    f"{SUN_RADIUS_KM:,.0f} km in radius --<br>"\n    f"  roughly {100.0 * (CHROMOSPHERE_PHYSICAL_RADII - 1.0):.2f}% of the solar radius. At any scale that "\n', b'    f"{exact_text(\'SUN_RADIUS_KM\', grouping=True)} km in radius --<br>"\n    f"  roughly {format_prints(100.0 * CHROMOSPHERE_PHYSICAL_KM / SUN_RADIUS_KM, figures_of(\'CHROMOSPHERE_PHYSICAL_KM\'))}% of the solar radius. At any scale that "\n', 1), ('stamp', b"Module updated: August 2026 with Anthropic's Claude Opus 5 (L-224:\n", b"Module updated: September 28, 2026 with Anthropic's Claude Opus 5.5\n(L-322 Stage D, patch D17: the chromosphere hover prints its radius by\nits row's count, 1.003 solar radii (was 1.002875); the Sun's radius\nthrough exact_text(), 695,700 km as before; and the skin as a share of\nthe radius at the depth's one figure, 0.3% (was 0.29%).)\n\nModule updated: August 2026 with Anthropic's Claude Opus 5 (L-224:\n", 1)],
    'exact_rows_report.py': [('DRAWN: the Sun radius, used as a unit', b"    'orientation/pole/dec':\n        ('gallery/feature_renderers.js', 'basisFor', 'pole.dec'),\n}\n", b"    'orientation/pole/dec':\n        ('gallery/feature_renderers.js', 'basisFor', 'pole.dec'),\n    # L-322 Stage D, patch D17: the Sun's nominal radius, exact since D17,\n    # is read by the Sun room only as the kilometres a served radius in\n    # solar radii is converted with; the hover prints the product, never\n    # the row itself.\n    'sun_structures/sun_radius':\n        ('gallery/feature_renderers.js', 'renderShellSet',\n         'params.sun_radius'),\n    'solar_atmosphere/sun_radius':\n        ('gallery/feature_renderers.js', 'renderShellSet',\n         'params.sun_radius'),\n    'solar_wind/sun_radius':\n        ('gallery/feature_renderers.js', 'renderShellSet',\n         'params.sun_radius'),\n}\n", 1), ('docstring: DRAWN names the unit case', b"DRAWN, NOT PRINTED. Some gallery pointers to exact rows are read only to\nplace a drawing and never printed: the magnetotail's drawn radius and\n", b"DRAWN, NOT PRINTED. Some gallery pointers to exact rows are read only to\nplace a drawing, or only as a unit to convert with, and never printed as\nthemselves: the Sun's nominal radius, which turns a radius in solar\nradii into kilometres (patch D17); the magnetotail's drawn radius and\n", 1), ('docstring: stamp', b'while it is not. The orrery search also finds exact_text().)\n"""\n', b'while it is not. The orrery search also finds exact_text().)\nModule updated: September 28, 2026 with Anthropic\'s Claude Opus 5.5\n(L-322 Stage D, patch D17: the three gallery pointers to SUN_RADIUS_KM,\nan exact row since D17, are in DRAWN: the Sun room reads it only as the\nkilometres per solar radius.)\n"""\n', 1)],
}


def fingerprint(data):
    return hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()


def fail(msg):
    print(msg)
    print('NOTHING was written. Undo is not needed.')
    sys.exit(1)


def main():
    if os.path.basename(os.getcwd()) == 'documentation' or \
            os.path.basename(os.path.dirname(os.path.abspath(__file__))) == 'documentation':
        fail('ERROR: this is in or running from documentation/. Move it to '
             'the orrery repo root (the folder with constants_new.py), then '
             'click Run.')
    here = os.path.dirname(os.path.abspath(__file__))
    results = []
    for rel in FINGERPRINTS:
        path = os.path.join(here, rel)
        if not os.path.exists(path):
            fail('ERROR: %s not found beside this script. Save it in the '
                 'orrery repo root.' % rel)
        with open(path, 'rb') as f:
            data = f.read()
        fp = fingerprint(data)
        if fp != FINGERPRINTS[rel]:
            fail('ERROR: %s is not the file this patch was built on '
                 '(fingerprint %s, expected %s). Pull or discard local '
                 'changes first.' % (rel, fp, FINGERPRINTS[rel]))
        crlf = b'\r\n' in data
        for label, old, new, count in EDITS[rel]:
            if crlf:
                old = old.replace(b'\n', b'\r\n')
                new = new.replace(b'\n', b'\r\n')
            n = data.count(old)
            if n != count:
                fail('ANCHOR FAIL: %s: "%s" -- expected %d match(es), got %d'
                     % (rel, label, count, n))
            data = data.replace(old, new)
            print('ok    %s: %s' % (rel, label))
        try:
            data.decode('ascii')
        except UnicodeDecodeError as exc:
            fail('ERROR: %s would not be ASCII after the patch (%s).'
                 % (rel, exc))
        results.append((path, data))
    for path, data in results:
        with open(path, 'wb') as f:
            f.write(data)
    print('stamp: Module updated September 28, 2026 (patch D17) in all four')
    print('patch applied: %s' % ', '.join(FINGERPRINTS))
    print('Next: run the orrery maintenance run. "Exact rows by the count" '
          'stays red, naming only the Earth room\'s eleven prints, until '
          'gallery patch 4 is run. Do not run the gallery maintenance run '
          'until gallery patch 5 is ready.')


if __name__ == '__main__':
    main()
