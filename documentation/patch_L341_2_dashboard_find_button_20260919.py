#!/usr/bin/env python3
"""
patch_L341_2_dashboard_find_button_20260919.py -- ORRERY repo.

Run: save this file in the ORRERY repo ROOT (next to
PROJECT_INSTRUCTIONS.md), open it in VS Code and click Run.  Or:
python patch_L341_2_dashboard_find_button_20260919.py

A patch is run from its repository's ROOT and filed in documentation/
AFTER it has run. This script refuses to run from documentation/.

CUT AGAINST THE FILE AS patch_L341_1 LEFT IT, not against the repo. Run
patch_L341_1_dashboard_search_and_groups_20260919.py first. It does not
matter whether that one has been committed yet: this patch checks the
file on disk, and that file is the same either way.

Built on orrery 19dabe27de0c5fe0ca072c86a8c4ad7ad1bc537d plus
patch_L341_1
at https://github.com/tonylquintanilla/palomas_orrery
(gallery 2ead992b055054956816ddda3544e849e9789d9a
at https://github.com/tonylquintanilla/tonyquintanilla.github.io)

L-341, Tony's suggestion of 2026-09-19 on seeing the first version:
"add a Find button before the Clear button. that way the search
function does not update with every character typed only at the end."

WHAT IT DOES (one file, 6 anchored edits):

  A FIND BUTTON sits between the box and Clear, and the search runs
  when you press it. Enter in the box does the same thing. Clear
  empties the box and brings every group back in one action.

  TYPING NO LONGER REDRAWS ANYTHING. Two reasons, and the second is the
  one Tony was pointing at. Each redraw destroys and rebuilds all
  sixty-odd cards, which is real work to do once per letter. And the
  groups shuffle and disappear under the cursor while a word is still
  half typed, which is the opposite of a page you can scan.

  WHAT THAT LEAVES IS A SCREEN THAT CAN DISAGREE WITH THE BOX, so it
  says so. While the typed text and the drawn list differ, the status
  line reads "press Find, or Enter". That label is the ONLY thing a
  keystroke touches -- one short string, not the whole section -- so it
  costs nothing and it stops a typed-but-unsearched box sitting above a
  list that silently does not match it.

  A GROUP NAME NOW COUNTS AS A MATCH, and takes its whole group with
  it. This was found by testing rather than by reading: typing "stars"
  returned nothing at all. The Stars group exists, but its single
  button is called Star Visualization and no description contains the
  word. Somebody typing a category name means the category.

SUCCESS looks like: one "ok" line per edit, then "patch applied".
FAILURE looks like: one ERROR: or ANCHOR FAIL: line, and NOTHING is
written. Undo is Discard Changes in GitHub Desktop.
"""

import hashlib
import os
import sys

DASH = "palomas_orrery_dashboard.py"
BASE = "a1b5d6e999cf495f474b85f5c09f603d"


def fail(msg):
    print(msg)
    print("NOTHING was written. Undo is Discard Changes in GitHub Desktop.")
    sys.exit(1)


EDITS = []

EDITS.append(('SEARCH ROW  Find button, Enter key, Clear routed through a method',
    b'        entry.pack(side="left", padx=(12, 0))\n\n        clear = ctk.CTkButton(\n            row, text="Clear", width=64, font=FONT_DESC,\n            fg_color=COLOR_BUTTON_BG, hover_color=COLOR_BUTTON_HOVER,\n            command=lambda: self._search_var.set("")\n        )\n        clear.pack(side="left", padx=(8, 0))\n',
    b'        entry.pack(side="left", padx=(12, 0))\n        entry.bind("<Return>", lambda _event: self._run_search())\n\n        find = ctk.CTkButton(\n            row, text="Find", width=64, font=FONT_DESC,\n            fg_color=COLOR_BUTTON_BG, hover_color=COLOR_BUTTON_HOVER,\n            command=self._run_search\n        )\n        find.pack(side="left", padx=(8, 0))\n\n        clear = ctk.CTkButton(\n            row, text="Clear", width=64, font=FONT_DESC,\n            fg_color=COLOR_BUTTON_BG, hover_color=COLOR_BUTTON_HOVER,\n            command=self._clear_search\n        )\n        clear.pack(side="left", padx=(8, 0))\n'))
EDITS.append(('SEARCH ROW  keystrokes update the hint only; Find and Clear do the work',
    b'        self._search_var.trace_add(\n            "write", lambda *_: self._render_launch(self._search_var.get()))\n',
    b'        self._rendered_query = ""\n        self._search_var.trace_add("write", lambda *_: self._search_hint())\n\n    def _run_search(self):\n        """Filter the groups to what is in the box. Find, or Enter."""\n        self._render_launch(self._search_var.get())\n\n    def _clear_search(self):\n        """Empty the box and bring every group back."""\n        self._search_var.set("")\n        self._render_launch("")\n\n    def _search_hint(self):\n        """Typing changes the box; it does not redraw the list.\n\n        The list is redrawn on Find or on Enter, not on every keystroke\n        -- Tony\'s ruling of 2026-09-19. Two reasons, and the second is\n        the one that matters to him. A redraw destroys and rebuilds all\n        sixty-odd cards, which is real work to do once per letter. And\n        the groups shuffle and vanish under the cursor while a word is\n        still half typed, which is the opposite of a page you can scan.\n\n        What this leaves is a screen that can disagree with the box, so\n        this says so. It is the only thing a keystroke changes, and it\n        is one short label rather than the whole section.\n        """\n        if self._search_var.get().strip().lower() == self._rendered_query:\n            return\n        self._search_status.configure(text="press Find, or Enter")\n'))
EDITS.append(('RENDER  remember the query the screen is actually showing',
    b'        needle = (query or "").strip().lower()\n        shown = 0\n',
    b'        needle = (query or "").strip().lower()\n        self._rendered_query = needle\n        shown = 0\n'))
EDITS.append(('RENDER  a group NAME matches, and takes its whole group',
    b'            if needle:\n                drawn = [e for e in entries\n                         if not isinstance(e, str)\n                         and self._entry_matches(e, needle)]\n            else:\n                drawn = list(entries)\n',
    b'            if not needle:\n                drawn = list(entries)\n            elif needle in group_name.lower():\n                # The GROUP NAME counts as a match, and takes the whole\n                # group with it. Typing "stars" found nothing before\n                # this: the Stars group exists, but its one button is\n                # called Star Visualization and no description says\n                # "stars". Somebody typing a category name means the\n                # category. (Found by testing, 2026-09-19.)\n                drawn = list(entries)\n            else:\n                drawn = [e for e in entries\n                         if not isinstance(e, str)\n                         and self._entry_matches(e, needle)]\n'))
EDITS.append(('DOCSTRING  _build_launch_search says the search is on demand',
    b'    def _build_launch_search(self):\n        """A filter box above the groups, and a line saying what it found.\n',
    b'    def _build_launch_search(self):\n        """A search box above the groups, and a line saying what it found.\n\n        It searches ON DEMAND -- Find, or Enter -- and not while you\n        type. See _search_hint for why.\n'))
EDITS.append(('DOCSTRING  the change-log entry for the Find button',
    b'own container frame so a search can rebuild them without disturbing the\nheader, the resources section or the footer.\n"""\n',
    b'own container frame so a search can rebuild them without disturbing the\nheader, the resources section or the footer.\nSeptember 19, 2026 with Anthropic\'s Claude Opus 5 (L-341), same day, on\nTony\'s suggestion: a FIND button beside Clear, and the search now runs\non demand rather than on every keystroke. Enter in the box does the\nsame thing. Typing now changes one short label, which says "press Find,\nor Enter" whenever the box and the drawn list disagree -- without it a\ntyped-but-unsearched box would sit above a list that silently did not\nmatch it. Clear empties the box and brings every group back in one\naction.\n"""\n'))


def main():
    if os.path.basename(os.getcwd()) == "documentation":
        fail("ERROR: this script is running from documentation/. Move it "
             "to the repository ROOT and run it there.")
    if not os.path.exists(DASH):
        fail("ERROR: " + DASH + " is not here. Run this from the ORRERY "
             "repo root.")

    with open(DASH, "rb") as handle:
        raw = handle.read()
    got = hashlib.md5(raw.replace(b"\r\n", b"\n")).hexdigest()
    if got != BASE:
        fail("ERROR: " + DASH + " is not the file this patch was cut "
             "against.\n  expected " + BASE + "\n  found    " + got +
             "\nThis patch expects patch_L341_1 to have run already. If "
             "it has not, run it first. If this patch already ran, this "
             "is what a second run looks like: it refuses.")

    is_crlf = raw.count(b"\r\n") > 0
    out = raw
    for label, old, new in EDITS:
        if is_crlf:
            old = old.replace(b"\n", b"\r\n")
            new = new.replace(b"\n", b"\r\n")
        n = out.count(old)
        if n != 1:
            fail("ANCHOR FAIL: expected exactly 1 match, found %d -- %s\n"
                 "  anchor began: %r" % (n, label, old[:70]))
        out = out.replace(old, new)

    try:
        out.decode("ascii")
    except UnicodeDecodeError as exc:
        fail("ERROR: the result is not ASCII (%s)." % exc)

    with open(DASH, "wb") as handle:
        handle.write(out)

    for label, _o, _n in EDITS:
        print("  ok  " + label)
    print("")
    print("      %-34s %7d -> %7d bytes" % (DASH, len(raw), len(out)))
    print("")
    print("patch applied (1 file, %d edits)" % len(EDITS))
    print("")
    print("NOW, in order:")
    print("  1. Open the dashboard and LOOK at it. Type 'export' WITHOUT")
    print("     pressing anything: the list should not move, and the")
    print("     line beside the box should read 'press Find, or Enter'.")
    print("     Then press Find. Then Clear, type 'stars', press Enter.")
    print("  2. Run the orrery maintenance run.")
    print("  3. Move BOTH L-341 scripts into documentation/.")
    print("  4. Commit EVERYTHING the run touched and push. Report the")
    print("     new SHA.")
    print("")
    print("Undo at any point is Discard Changes in GitHub Desktop.")


if __name__ == "__main__":
    main()
