#!/usr/bin/env python3
"""
patch_L409_2_orrery_license_recognized_20261004.py -- ORRERY repo.
The orrery's license made recognizable to GitHub (L-409). Today GitHub
says "View license" rather than "MIT license", because LICENSE.md holds
a header line and two sections of attributions beside the MIT text.

Run: save this file in the ORRERY repo ROOT (next to palomas_orrery.py),
open it in VS Code and click Run. The same as: python patch_L409_2_orrery_license_recognized_20261004.py
It refuses to run from documentation/ or in the gallery repo. File it in
documentation/ after it has run.

Built on orrery a841ab6ee36fbbcef936408bc87774bc32a7598d
at https://github.com/tonylquintanilla/palomas_orrery
(gallery d4b408e60b1d9a45252174ca4a2c861ca17b49a5
at https://github.com/tonylquintanilla/tonyquintanilla.github.io).
It runs in either order with patch_L363_12 (this session's records).

FILES.
  LICENSE.md            the standard MIT text alone; Copyright 2024-2026
                        (it said 2024; the README said 2025-2026)
  NOTICE.md             NEW: the data attributions and third-party list,
                        moved word for word from LICENSE.md
  README.md             the License section's years and a pointer to
                        NOTICE.md; the structure line; the header stamp
  doc_index.py          describes LICENSE.md, which cannot carry the
                        tag any more, and names it in its report
  LEDGER_CONSOLIDATED.md   NEW item L-409, with your rulings

L-409 IS A NEW HANDLE. If the other session opens a new ledger item,
tell it L-409 is taken.

Not legal advice. Everything is written or nothing is. SUCCESS: one
"ok" line per change, then "patch applied". FAILURE: one ERROR: or
ANCHOR FAIL: line, and NOTHING is written. Undo is Discard Changes in
GitHub Desktop.

Written October 4, 2026 with Anthropic's Claude Opus 5.5.
"""

import os

PLAN = {'LEDGER_CONSOLIDATED.md': [['## A. ACTIVE SEPARATE TRACKS (not '
                             'orrery-refactor backlog; cross-referenced)\n'
                             '\n',
                             '## A. ACTIVE SEPARATE TRACKS (not '
                             'orrery-refactor backlog; cross-referenced)\n'
                             '\n'
                             "#### [L-409] The licenses: the orrery's "
                             "recognized by GitHub, the website's written "
                             '(orrery, gallery)\n'
                             '<!-- L:409 status:OPEN upd:2026-10-04 '
                             'section:A flag: rice: -->\n'
                             '- **Found 2026-10-04,** when Tony asked '
                             'whether the license was done\n'
                             "  properly. The orrery's `LICENSE.md` is in "
                             "the right place, but GitHub's\n"
                             '  sidebar said "View license", not "MIT '
                             'license": the file held the\n'
                             '  Doc-Kind tag and two sections of '
                             'attributions beside the MIT text. Its\n'
                             "  year, 2024, disagreed with the README's "
                             'License section, 2025-2026.\n'
                             "  The website's repository had no license "
                             'file; its README said\n'
                             '  "Licensed MIT, the same as the application '
                             'repository".\n'
                             "- **Tony's rulings, 2026-10-04:** the "
                             "website's code under the MIT\n"
                             '  License and its content -- words, pictures, '
                             'artwork, visualizations --\n'
                             '  under CC BY 4.0; a copyright line on the '
                             "lobby's About card; his email\n"
                             "  address as that card's last line. Years "
                             '2024-2026, the project having\n'
                             '  begun in September 2024.\n'
                             '- **Built:**\n'
                             '  - Orrery `patch_L409_2`: `LICENSE.md` the '
                             'standard text alone; its\n'
                             '    attributions moved word for word to '
                             "`NOTICE.md`; the README's\n"
                             '    License years and a pointer to '
                             '`NOTICE.md`; `doc_index.py`\n'
                             '    describes `LICENSE.md`, which cannot carry '
                             'the tag (UNTAGGABLE, one\n'
                             '    entry, named in its report).\n'
                             '  - Gallery `patch_L409_1`: `LICENSE` (MIT), '
                             '`LICENSE-CONTENT.md` (CC BY\n'
                             '    4.0: what counts as content, a suggested '
                             'credit, third-party data\n'
                             '    excluded), `NOTICE.md` (Plotly.js, MIT; '
                             'Pyodide, MPL-2.0 [verified\n'
                             '    2026-10-04 against pyodide.org]; data '
                             "stays under its providers'\n"
                             "    terms), the README's license line, and the "
                             "About card's two new\n"
                             '    lines.\n'
                             '- Claude said this is practical orientation, '
                             'not legal advice.\n'
                             "**Gap:** after both pushes, each repository's "
                             'GitHub page should say\n'
                             '"MIT license" in its sidebar -- the one check '
                             'that the recognition\n'
                             'worked. **Tony-action (do):** look at both.\n'
                             '**Ref:** L-085 (LICENSE to repo root); gallery '
                             '`index.html`, the About\n'
                             'overlay.\n'
                             '\n',
                             'L-409, new']],
 'README.md': [['this file was written against, not a promise the repository '
                'still sits\n'
                'there.\n',
                'this file was written against, not a promise the repository '
                'still sits\n'
                "there. Updated October 4, 2026 with Anthropic's Claude Opus "
                '5.5 (L-409):\n'
                "the License section's years, and its pointer to "
                '`NOTICE.md`.\n',
                'header stamp'],
               ['## License\n'
                '\n'
                'MIT License\n'
                '\n'
                'Copyright (c) 2025-2026 Tony Quintanilla\n',
                '## License\n'
                '\n'
                'The license file is `LICENSE.md`; data attributions and '
                'third-party\n'
                'components are in `NOTICE.md`.\n'
                '\n'
                'MIT License\n'
                '\n'
                'Copyright (c) 2024-2026 Tony Quintanilla\n',
                'License: years 2024-2026, and NOTICE.md'],
               ['|- README.md, LICENSE.md         # you are here\n',
                '|- README.md, LICENSE.md, NOTICE.md   # you are here\n',
                'structure: NOTICE.md']],
 'doc_index.py': [['UNTAGGED DOCUMENTS ARE REPORTED, NEVER DROPPED\n'
                   '----------------------------------------------',
                   'ONE DOCUMENT CANNOT CARRY THE TAG (L-409)\n'
                   '-----------------------------------------\n'
                   'LICENSE.md must hold the standard MIT text alone, or '
                   'GitHub does not\n'
                   'recognise the license: on 2026-10-04 its sidebar said '
                   '"View license",\n'
                   'while the file also held a tag and two sections of '
                   'attributions (now\n'
                   'NOTICE.md). Its row is described in UNTAGGABLE below, '
                   'and the report\n'
                   'names it as described there rather than by a tag. It is '
                   'the only entry;\n'
                   'a second one is a reason to look again, not a pattern to '
                   'extend.\n'
                   '\n'
                   'UNTAGGED DOCUMENTS ARE REPORTED, NEVER DROPPED\n'
                   '----------------------------------------------',
                   'docstring: the one exception'],
                  ["Module created: September 1, 2026 with Anthropic's "
                   'Claude Opus 5.\n',
                   "Module created: September 1, 2026 with Anthropic's "
                   'Claude Opus 5.\n'
                   "Module updated: October 4, 2026 with Anthropic's Claude "
                   'Opus 5.5 (L-409:\n'
                   'LICENSE.md described here, since it cannot carry the '
                   'tag).\n',
                   'stamp'],
                  ["SCAN_SUFFIXES = ('.md', '.txt')\n",
                   "SCAN_SUFFIXES = ('.md', '.txt')\n"
                   '\n'
                   '# L-409: documents whose content must stay exact, so '
                   'they cannot carry a\n'
                   '# tag. Described here instead; see the docstring.\n'
                   'UNTAGGABLE = {\n'
                   "    'LICENSE.md': ('hand', 'The MIT license, as the "
                   "standard text alone so '\n"
                   "                           'GitHub recognizes it. "
                   "Attributions are in '\n"
                   "                           'NOTICE.md.'),\n"
                   '}\n',
                   'UNTAGGABLE'],
                  ['        kind, purpose = read_tag(p)\n'
                   '        docs.append((p.name, kind, purpose))',
                   '        kind, purpose = read_tag(p)\n'
                   '        if kind is None and p.name in UNTAGGABLE:\n'
                   '            kind, purpose = UNTAGGABLE[p.name]\n'
                   '        docs.append((p.name, kind, purpose))',
                   'collect: use the exception'],
                  ['    problems = 0\n    if unknown:',
                   '    described = [n for n in UNTAGGABLE if (root / '
                   'n).is_file()]\n'
                   '    if described:\n'
                   "        print('  described in doc_index.py, not by a "
                   "tag: %s'\n"
                   "              % ', '.join(described))\n"
                   '\n'
                   '    problems = 0\n'
                   '    if unknown:',
                   'report names the exception']]}
NEW = {'NOTICE.md': '<!-- Doc-Kind: hand | Data attributions and third-party '
              'components, moved out of LICENSE.md so GitHub recognizes the '
              'license. -->\n'
              '# Notices\n'
              '\n'
              "The license for this repository's code is the MIT License, "
              'in\n'
              '`LICENSE.md`. These notices were part of that file until '
              'October 4,\n'
              '2026 (ledger L-409). They moved here because GitHub '
              'recognizes a license\n'
              'only when its file holds the standard text alone.\n'
              '\n'
              '## Data Source Attributions\n'
              '\n'
              'When using this software, please acknowledge the following '
              'data sources:\n'
              '\n'
              '- **NASA/JPL-Caltech**: JPL Horizons ephemeris data\n'
              '- **ESA**: Hipparcos catalog data  \n'
              '- **ESA/Gaia/DPAC**: Gaia Data Release 3\n'
              '- **CDS, Strasbourg, France**: SIMBAD astronomical database\n'
              '\n'
              '## Third-Party Components\n'
              '\n'
              'This software incorporates the following open-source '
              'libraries:\n'
              '- NumPy (BSD 3-Clause License)\n'
              '- Pandas (BSD 3-Clause License) \n'
              '- Plotly (MIT License)\n'
              '- Astropy (BSD 3-Clause License)\n'
              '- Astroquery (BSD 3-Clause License)\n'
              '- Matplotlib (PSF License)\n'
              '- SciPy (BSD 3-Clause License)\n'
              '\n'
              'Each component retains its original license terms.\n'}
REPLACE = {'LICENSE.md': ['<!-- Doc-Kind: hand | MIT license. -->\n'
                'MIT License\n'
                '\n'
                'Copyright (c) 2024 Tony Quintanilla\n'
                '\n'
                'Permission is hereby granted, free of charge, to any person '
                'obtaining a copy\n'
                'of this software and associated documentation files (the '
                '"Software"), to deal\n'
                'in the Software without restriction, including without '
                'limitation the rights\n'
                'to use, copy, modify, merge, publish, distribute, '
                'sublicense, and/or sell\n'
                'copies of the Software, and to permit persons to whom the '
                'Software is\n'
                'furnished to do so, subject to the following conditions:\n'
                '\n'
                'The above copyright notice and this permission notice shall '
                'be included in all\n'
                'copies or substantial portions of the Software.\n'
                '\n'
                'THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY '
                'KIND, EXPRESS OR\n'
                'IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF '
                'MERCHANTABILITY,\n'
                'FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO '
                'EVENT SHALL THE\n'
                'AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, '
                'DAMAGES OR OTHER\n'
                'LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR '
                'OTHERWISE, ARISING FROM,\n'
                'OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR '
                'OTHER DEALINGS IN THE\n'
                'SOFTWARE.\n'
                '\n'
                '## Data Source Attributions\n'
                '\n'
                'When using this software, please acknowledge the following '
                'data sources:\n'
                '\n'
                '- **NASA/JPL-Caltech**: JPL Horizons ephemeris data\n'
                '- **ESA**: Hipparcos catalog data  \n'
                '- **ESA/Gaia/DPAC**: Gaia Data Release 3\n'
                '- **CDS, Strasbourg, France**: SIMBAD astronomical '
                'database\n'
                '\n'
                '## Third-Party Components\n'
                '\n'
                'This software incorporates the following open-source '
                'libraries:\n'
                '- NumPy (BSD 3-Clause License)\n'
                '- Pandas (BSD 3-Clause License) \n'
                '- Plotly (MIT License)\n'
                '- Astropy (BSD 3-Clause License)\n'
                '- Astroquery (BSD 3-Clause License)\n'
                '- Matplotlib (PSF License)\n'
                '- SciPy (BSD 3-Clause License)\n'
                '\n'
                'Each component retains its original license terms.',
                'MIT License\n'
                '\n'
                'Copyright (c) 2024-2026 Tony Quintanilla\n'
                '\n'
                'Permission is hereby granted, free of charge, to any person '
                'obtaining a copy\n'
                'of this software and associated documentation files (the '
                '"Software"), to deal\n'
                'in the Software without restriction, including without '
                'limitation the rights\n'
                'to use, copy, modify, merge, publish, distribute, '
                'sublicense, and/or sell\n'
                'copies of the Software, and to permit persons to whom the '
                'Software is\n'
                'furnished to do so, subject to the following conditions:\n'
                '\n'
                'The above copyright notice and this permission notice shall '
                'be included in all\n'
                'copies or substantial portions of the Software.\n'
                '\n'
                'THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY '
                'KIND, EXPRESS OR\n'
                'IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF '
                'MERCHANTABILITY,\n'
                'FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO '
                'EVENT SHALL THE\n'
                'AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, '
                'DAMAGES OR OTHER\n'
                'LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR '
                'OTHERWISE, ARISING FROM,\n'
                'OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR '
                'OTHER DEALINGS IN THE\n'
                'SOFTWARE.\n']}
REPLACE_NOTE = {'LICENSE.md': 'the MIT text alone, 2024-2026'}
MUST_HAVE = ['palomas_orrery.py', 'LEDGER_CONSOLIDATED.md', 'doc_index.py']
MUST_NOT = ['interactive.html']
NEXT = ['  1. python orrery_maintenance_run.py (VS Code, Run). It files L-409 in',
 "     the ledger's index and adds NOTICE.md to the README's table, where",
 '     LICENSE.md now reads "The MIT license, as the standard text alone".',
 '  2. Move this script into documentation/; commit and push.',
 '  3. On GitHub, the orrery\'s page: its sidebar should now say "MIT',
 '     license" instead of "View license". GitHub can take a few',
 '     minutes to notice.']


def main():
    if os.path.basename(os.getcwd()) == "documentation":
        raise SystemExit("ERROR: run this from the ORRERY repo ROOT, not from "
                         "documentation/. NOTHING was written." )
    if not all(os.path.isfile(f) for f in MUST_HAVE) or any(os.path.isfile(f) for f in MUST_NOT):
        raise SystemExit("ERROR: this is not the ORRERY repo root. NOTHING was written.")
    for path in NEW:
        if os.path.exists(path):
            raise SystemExit("ERROR: %s already exists. If you already ran this "
                             "patch, it has nothing left to do. NOTHING was "
                             "written." % path)
    results = []
    for path, edits in sorted(PLAN.items()):
        with open(path, "rb") as handle:
            raw = handle.read()
        crlf = raw.count(b"\r\n") > 0
        text = raw.decode("utf-8").replace("\r\n", "\n")
        done = []
        for old, new, label in edits:
            count = text.count(old)
            if count != 1:
                raise SystemExit("ANCHOR FAIL (%s): expected 1 match in %s, "
                                 "found %d. NOTHING was written."
                                 % (label, path, count))
            if any(ord(ch) > 127 for ch in new):
                raise SystemExit("ERROR: new non-ASCII text in %s. NOTHING "
                                 "was written." % path)
            text = text.replace(old, new)
            done.append(label)
        results.append((path, text, done, crlf))
    for path, (want, content) in sorted(REPLACE.items()):
        with open(path, "rb") as handle:
            now = handle.read().decode("utf-8").replace("\r\n", "\n")
        if now != want:
            raise SystemExit("ERROR: %s is not the copy this patch was built "
                             "against. NOTHING was written." % path)
    for path, text, done, crlf in results:
        data = text.replace("\n", "\r\n") if crlf else text
        with open(path, "wb") as handle:
            handle.write(data.encode("utf-8"))
        for label in done:
            print("ok  %-30s %s%s" % (path, label, "  [CRLF]" if crlf else ""))
    for path, (want, content) in sorted(REPLACE.items()):
        with open(path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(content)
        print("ok  %-30s replaced: %s" % (path, REPLACE_NOTE[path]))
    for path, content in sorted(NEW.items()):
        with open(path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(content)
        print("ok  %-30s created" % path)
    print("")
    print("patch applied")
    print("")
    print("NEXT:")
    for line in NEXT:
        print(line)


if __name__ == "__main__":
    main()
