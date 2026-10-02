#!/usr/bin/env python3
"""
patch_L395_mars_jupiter_links_20261001.py -- ORRERY repo.
Mars and Jupiter link to NASA's planet pages, not to NASA's search page.

Run: save this file in the ORRERY repo ROOT (next to palomas_orrery.py),
open it in VS Code and click Run. The same as: python
patch_L395_mars_jupiter_links_20261001.py

A patch is run from its repository's ROOT and filed in documentation/
AFTER it has run. This script refuses to run from documentation/.

Built on orrery 6b2ef097da67e67ab8f748b5481c222e5dd34acc
at https://github.com/tonylquintanilla/palomas_orrery
(gallery 5a38de15d69df48749ba230cdfacf0e9d9e2fb5e
at https://github.com/tonylquintanilla/tonyquintanilla.github.io;
not touched by this patch)

WHAT IT DOES.

  celestial_objects.py, OBJECT_DEFINITIONS, two mission_url lines:
      Mars     https://science.nasa.gov/?search=mars
            -> https://science.nasa.gov/mars/
      Jupiter  https://science.nasa.gov/?search=Jupiter
            -> https://science.nasa.gov/jupiter/
  Both pages were opened on 2026-10-01 and each names itself as its
  own canonical address. They are the addresses NASA Science's own
  menu gives for the two planets, the same pattern the other planets'
  entries already use (science.nasa.gov/saturn/ and so on). No other
  entry in OBJECT_DEFINITIONS points at a search page.

  The descriptions are unchanged. Each quotes a sentence that appears
  on the new page, so description and link now agree.

Tony's request, 2026-10-01 (L-395): "Please fix".

SUCCESS looks like: two "ok" lines, then "patch applied". FAILURE looks
like one ERROR: or ANCHOR FAIL: line, and NOTHING is written. Undo is
Discard Changes in GitHub Desktop.

Written October 1, 2026 with Anthropic's Claude Opus 5.5.
"""

import hashlib
import os

TARGET = "celestial_objects.py"
BASE_MD5 = "0cfcd7da45062cbb9c7ce0ce217303f3"   # LF-normalized, at 6b2ef097

EDITS = [
    ("    'mission_url': 'https://science.nasa.gov/?search=mars'},\n",
     "    'mission_url': 'https://science.nasa.gov/mars/'},\n",
     "Mars links to science.nasa.gov/mars/"),
    ("    'mission_url': 'https://science.nasa.gov/?search=Jupiter'},\n",
     "    'mission_url': 'https://science.nasa.gov/jupiter/'},\n",
     "Jupiter links to science.nasa.gov/jupiter/"),
]


def main():
    if os.path.basename(os.getcwd()) == "documentation":
        raise SystemExit("ERROR: run this from the ORRERY repo ROOT, next to "
                         "palomas_orrery.py -- not from documentation/. "
                         "NOTHING was written.")
    if not os.path.isfile("palomas_orrery.py"):
        raise SystemExit("ERROR: palomas_orrery.py is not here, so this is "
                         "not the orrery root. NOTHING was written.")
    if not os.path.isfile(TARGET):
        raise SystemExit("ERROR: %s is missing. NOTHING was written." % TARGET)

    with open(TARGET, "rb") as handle:
        raw = handle.read()
    got = hashlib.md5(raw.replace(b"\r\n", b"\n")).hexdigest()
    if got != BASE_MD5:
        raise SystemExit(
            "ERROR: %s is not the file this patch was built against.\n"
            "       expected %s, found %s.\n"
            "       (Line endings are excluded, so they are not the cause.)\n"
            "       If you already ran this patch, it has nothing left to do.\n"
            "       NOTHING was written." % (TARGET, BASE_MD5, got))

    nl = "\r\n" if raw.count(b"\r\n") > 0 else "\n"
    text = raw.decode("utf-8")
    done = []
    for old, new, label in EDITS:
        o = old.replace("\n", nl)
        n = new.replace("\n", nl)
        count = text.count(o)
        if count != 1:
            raise SystemExit("ANCHOR FAIL (%s): expected 1 match in %s, "
                             "found %d. NOTHING was written."
                             % (label, TARGET, count))
        text = text.replace(o, n)
        done.append(label)
    if "?search=" in text:
        raise SystemExit("ERROR: a search-page link would remain in %s. "
                         "NOTHING was written." % TARGET)

    with open(TARGET, "wb") as handle:
        handle.write(text.encode("utf-8"))
    for label in done:
        print("ok  %-24s %s" % (TARGET, label))

    print("")
    print("patch applied (2 edits in 1 file)")
    print("")
    print("NEXT:")
    print("  1. Move this script into documentation/.")
    print("  2. Commit and push. It can go with this session's closing")
    print("     patch, or on its own now.")


if __name__ == "__main__":
    main()
