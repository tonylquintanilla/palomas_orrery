#!/usr/bin/env python3
"""
patch_L341_1_dashboard_search_and_groups_20260919.py -- ORRERY repo.

Run: save this file in the ORRERY repo ROOT (next to
PROJECT_INSTRUCTIONS.md), open it in VS Code and click Run.  Or:
python patch_L341_1_dashboard_search_and_groups_20260919.py

A patch is run from its repository's ROOT and filed in documentation/
AFTER it has run. This script refuses to run from documentation/.

Built on orrery 19dabe27de0c5fe0ca072c86a8c4ad7ad1bc537d
at https://github.com/tonylquintanilla/palomas_orrery
(gallery 2ead992b055054956816ddda3544e849e9789d9a
at https://github.com/tonylquintanilla/tonyquintanilla.github.io)

L-341. Tony asked for two things on 2026-09-19, after running a tool
from a terminal that the dashboard already carries a button for: a
search that says WHICH GROUP a match lives in, and the two oversized
groups split so that a visual scan works. He said he prefers a visual
check in general, and both changes serve that.

WHAT IT DOES (one file, 9 anchored edits):

  THE GROUPS GO FROM FIVE TO SEVEN. They were very unevenly filled:
  Solar System 2, Earth System 5, Stars 1, Gallery & Web 22, Developer
  Tools 37. Nearly everything was in the last two.

      Gallery & Web           ->  Gallery -- checks and data   (15)
                                  Gallery -- authoring          (8)
      Developer Tools         ->  Maintenance Run              (27)
                                  Tools and Caches             (11)

  "Gallery Cache Builder -- Manual Run" MOVES from Developer Tools to
  the gallery group. It was already the odd one out there: its base
  directory is GALLERY_REPO_DIR, it builds the gallery's serving cache,
  and it sat above the maintenance runner with nothing to do with it.

  NO ENTRY IS REORDERED AND NO DESCRIPTION IS TOUCHED. In particular
  the twenty checkers under the maintenance runner stay in one
  alphabetical run with their GENERATORS and CHECKERS sub-headings,
  because that arrangement is Tony's own ruling of 2026-09-12 and
  re-sorting them by kind would quietly overturn it. That is why
  Maintenance Run is still 27 -- it is a runner and its contents, drawn
  indented underneath it, not a flat list of 27 unrelated buttons.

  A SEARCH BOX above the groups. Type, and only the matching buttons
  remain -- each one still under its own group heading, so the search
  answers "where is it" as well as "what is it". A group with no match
  is not drawn, so the headings left on screen are themselves the
  answer. It searches descriptions as well as names, because the
  descriptions in this file are long and specific and are the part
  worth searching. A status line beside the box says how many of how
  many matched, and says plainly when nothing did.

HOW THE REDRAW IS SAFE. The groups now live in their own container
frame, so a search destroys and rebuilds only that. The header, the
resources section and the footer are packed into _main_frame before and
after it and are never touched.

SUCCESS looks like: one "ok" line per edit, then "patch applied".
FAILURE looks like: one ERROR: or ANCHOR FAIL: line, and NOTHING is
written. Undo is Discard Changes in GitHub Desktop.
"""

import hashlib
import os
import sys

DASH = "palomas_orrery_dashboard.py"
BASE = "3f5038423b5702ba34be4b45681ec511"


def fail(msg):
    print(msg)
    print("NOTHING was written. Undo is Discard Changes in GitHub Desktop.")
    sys.exit(1)


EDITS = []

EDITS.append(('GROUPS  Gallery & Web -> Gallery -- checks and data',
    b'    "Gallery & Web": [\n',
    b'    "Gallery -- checks and data": [\n'))
EDITS.append(('GROUPS  new group boundary before Exhibit Store Editor',
    b'        ("Exhibit Store Editor",\n',
    b'    ],\n    "Gallery -- authoring": [\n        ("Exhibit Store Editor",\n'))
EDITS.append(('GROUPS  lift Gallery Cache Builder out of Developer Tools',
    b'        ("Gallery Cache Builder -- Manual Run",\n         os.path.join("tools", "gallery_cache_builder.py"),\n         "Manual serving-cache build. Runs from the gallery repo ROOT: the "\n         "builder resolves its data/ paths from the working directory, so "\n         "launching it from tools/ cannot find data/objects_config.json. "\n         "With no flags it fetches from Horizons, validates, atomic-swaps "\n         "the new cache into data/solar-system, and STOPS -- it does not "\n         "commit or push. Commit it yourself in GitHub Desktop after the "\n         "run finishes. Do not commit while it is still running: mid-build "\n         "the working tree shows deletions only, which is the swap in "\n         "progress, not data loss. The console stays open at the repo root "\n         "if you want a flagged re-run (--dry-run --object <slug>, "\n         "--first-build).",\n         GALLERY_REPO_DIR,\n         True),\n        ("MAINTENANCE RUN -- everything indented below",',
    b'        ("MAINTENANCE RUN -- everything indented below",'))
EDITS.append(('GROUPS  Gallery Cache Builder lands in the gallery group',
    b'    "Gallery -- checks and data": [\n',
    b'    "Gallery -- checks and data": [\n        ("Gallery Cache Builder -- Manual Run",\n         os.path.join("tools", "gallery_cache_builder.py"),\n         "Manual serving-cache build. Runs from the gallery repo ROOT: the "\n         "builder resolves its data/ paths from the working directory, so "\n         "launching it from tools/ cannot find data/objects_config.json. "\n         "With no flags it fetches from Horizons, validates, atomic-swaps "\n         "the new cache into data/solar-system, and STOPS -- it does not "\n         "commit or push. Commit it yourself in GitHub Desktop after the "\n         "run finishes. Do not commit while it is still running: mid-build "\n         "the working tree shows deletions only, which is the swap in "\n         "progress, not data loss. The console stays open at the repo root "\n         "if you want a flagged re-run (--dry-run --object <slug>, "\n         "--first-build).",\n         GALLERY_REPO_DIR,\n         True),\n'))
EDITS.append(('GROUPS  Developer Tools -> Maintenance Run',
    b'    "Developer Tools": [\n',
    b'    "Maintenance Run": [\n'))
EDITS.append(('GROUPS  new group boundary before Add Module Docstrings',
    b'        ("Add Module Docstrings",\n',
    b'    ],\n    "Tools and Caches": [\n        ("Add Module Docstrings",\n'))
EDITS.append(('SYMBOLS  entries for the four new group names, plus REPO_AUDIT_GROUPS',
    b'    "Gallery & Web": "",\n}\n',
    b'    "Gallery -- checks and data": "",\n    "Gallery -- authoring": "",\n    "Maintenance Run": "",\n    "Tools and Caches": "",\n}\n\n# The groups whose buttons audit THIS repository. The heading carries a\n# "Running from:" reminder for these, because several copies of the repo\n# exist -- sandbox, clean repo, cloud snapshots -- and running against\n# the wrong one produces misleading results. Split out of the single\n# "Developer Tools" test when that group became two (L-341).\nREPO_AUDIT_GROUPS = ("Maintenance Run", "Tools and Caches")\n'))
EDITS.append(('RENDER  search row, container, filtering render',
    b'    def _build_launch_section(self):\n        """Four domain groups with launch buttons."""\n\n        for group_name, entries in LAUNCH_GROUPS.items():\n            # Section header\n            section_frame = ctk.CTkFrame(self._main_frame,\n                                         fg_color="transparent")\n            section_frame.pack(fill="x", padx=20, pady=(16, 4))\n\n            symbol = SECTION_SYMBOLS.get(group_name, "")\n            ctk.CTkLabel(\n                section_frame,\n                text=f"{symbol}  {group_name}",\n                font=FONT_SECTION, text_color=COLOR_TEXT,\n                anchor="w"\n            ).pack(side="left")\n\n            # Developer Tools: remind the user which codebase directory\n            # these tools should audit. Multiple copies of the repo exist\n            # (sandbox, clean repo, Google Drive snapshots) and running\n            # against the wrong one produces misleading results.\n            if group_name == "Developer Tools":\n                ctk.CTkLabel(\n                    section_frame,\n                    text=f"  Running from: {SCRIPT_DIR}",\n                    font=FONT_DESC, text_color=COLOR_TEXT_DIM,\n                    anchor="w"\n                ).pack(side="left", padx=(8, 0))\n\n            # Divider\n            div = ctk.CTkFrame(self._main_frame, fg_color=COLOR_DIVIDER,\n                               height=1)\n            div.pack(fill="x", padx=20, pady=(0, 8))\n\n            # Cards grid\n            cards_frame = ctk.CTkFrame(self._main_frame,\n                                       fg_color="transparent")\n            cards_frame.pack(fill="x", padx=20, pady=(0, 4))\n\n            for i, entry in enumerate(entries):\n                # A bare string is a HEADING inside the group, not a\n                # card. The maintenance runner prints GENERATORS then\n                # CHECKERS, and the indented list here is that same\n                # list, so it reads the same way. Alphabetical order\n                # within each half is Tony\'s, 2026-09-12: without the\n                # two labels a sorted run of twenty buttons gives no\n                # clue where one kind stops and the other starts.\n                if isinstance(entry, str):\n                    self._build_indent_heading(cards_frame, entry)\n                    continue\n                name, script, desc = entry[0], entry[1], entry[2]\n                base_dir = entry[3] if len(entry) > 3 else SCRIPT_DIR\n                interactive = entry[4] if len(entry) > 4 else False\n                args = entry[5] if len(entry) > 5 else None\n                indent = entry[6] if len(entry) > 6 else False\n                self._build_launch_card(cards_frame, name, script, desc,\n                                        base_dir, interactive, args, i,\n                                        indent)\n',
    b'    def _build_launch_section(self):\n        """The search row, then the launch groups under it.\n\n        The groups are drawn into their own container frame so that a\n        search can throw them away and draw them again without touching\n        the header, the resources section or the footer, which are\n        packed into _main_frame before and after this.\n        """\n        self._build_launch_search()\n\n        self._launch_container = ctk.CTkFrame(self._main_frame,\n                                              fg_color="transparent")\n        self._launch_container.pack(fill="x")\n\n        self._render_launch("")\n\n    def _build_launch_search(self):\n        """A filter box above the groups, and a line saying what it found.\n\n        WHY A FILTER AND NOT A FLAT RESULT LIST. A match is shown in its\n        own group, under that group\'s own heading, rather than in one\n        undifferentiated list. Finding the button is half the job; the\n        other half is learning WHERE it lives, so that the next time you\n        do not need the search at all. A flat list answers the first\n        question every time and never answers the second. (Tony\'s\n        choice, 2026-09-19, L-341.)\n\n        It searches the description as well as the name. The\n        descriptions in this file are long and specific, which makes\n        them the part worth searching: the tool that pulls the orrery\'s\n        export is called "Constants Export Pull", and somebody looking\n        for it is at least as likely to type "gallery numbers" or\n        "sha" as to type its name.\n        """\n        row = ctk.CTkFrame(self._main_frame, fg_color="transparent")\n        row.pack(fill="x", padx=20, pady=(16, 0))\n\n        ctk.CTkLabel(\n            row, text="Find a tool",\n            font=FONT_SECTION, text_color=COLOR_TEXT, anchor="w"\n        ).pack(side="left")\n\n        self._search_var = ctk.StringVar()\n        entry = ctk.CTkEntry(\n            row, textvariable=self._search_var, width=280,\n            placeholder_text="name or description, e.g. export"\n        )\n        entry.pack(side="left", padx=(12, 0))\n\n        clear = ctk.CTkButton(\n            row, text="Clear", width=64, font=FONT_DESC,\n            fg_color=COLOR_BUTTON_BG, hover_color=COLOR_BUTTON_HOVER,\n            command=lambda: self._search_var.set("")\n        )\n        clear.pack(side="left", padx=(8, 0))\n\n        self._search_status = ctk.CTkLabel(\n            row, text="", font=FONT_DESC, text_color=COLOR_TEXT_DIM,\n            anchor="w"\n        )\n        self._search_status.pack(side="left", padx=(12, 0))\n\n        self._search_var.trace_add(\n            "write", lambda *_: self._render_launch(self._search_var.get()))\n\n    def _launch_entry_total(self):\n        """How many launchable buttons exist. Bare strings are headings."""\n        return sum(1 for entries in LAUNCH_GROUPS.values()\n                   for entry in entries if not isinstance(entry, str))\n\n    def _entry_matches(self, entry, needle):\n        """Name or description contains `needle`, case-insensitively."""\n        return needle in entry[0].lower() or needle in entry[2].lower()\n\n    def _render_launch(self, query):\n        """Draw the groups, filtered by `query`.\n\n        An empty query draws everything, which is the ordinary view. A\n        non-empty one draws only the groups that still have a match, and\n        only the matching buttons inside them. A group with nothing left\n        is not drawn at all, so the headings that remain are themselves\n        the answer to "where does this live".\n        """\n        for child in self._launch_container.winfo_children():\n            child.destroy()\n\n        needle = (query or "").strip().lower()\n        shown = 0\n\n        for group_name, entries in LAUNCH_GROUPS.items():\n            if needle:\n                drawn = [e for e in entries\n                         if not isinstance(e, str)\n                         and self._entry_matches(e, needle)]\n            else:\n                drawn = list(entries)\n            if not drawn:\n                continue\n            shown += sum(1 for e in drawn if not isinstance(e, str))\n            self._build_group(group_name, drawn)\n\n        if not needle:\n            self._search_status.configure(\n                text="%d buttons in %d groups"\n                     % (self._launch_entry_total(), len(LAUNCH_GROUPS)))\n        elif shown:\n            self._search_status.configure(\n                text="%d of %d match \\u2014 shown under their own headings"\n                     % (shown, self._launch_entry_total()))\n        else:\n            self._search_status.configure(\n                text="nothing matches \\u2014 try fewer letters, or Clear")\n\n    def _build_group(self, group_name, entries):\n        """One group heading, its divider, and its cards."""\n        section_frame = ctk.CTkFrame(self._launch_container,\n                                     fg_color="transparent")\n        section_frame.pack(fill="x", padx=20, pady=(16, 4))\n\n        symbol = SECTION_SYMBOLS.get(group_name, "")\n        ctk.CTkLabel(\n            section_frame,\n            text=f"{symbol}  {group_name}",\n            font=FONT_SECTION, text_color=COLOR_TEXT,\n            anchor="w"\n        ).pack(side="left")\n\n        # The repo-auditing groups remind the user which codebase\n        # directory these tools examine. Multiple copies of the repo\n        # exist (sandbox, clean repo, cloud snapshots) and running\n        # against the wrong one produces misleading results.\n        if group_name in REPO_AUDIT_GROUPS:\n            ctk.CTkLabel(\n                section_frame,\n                text=f"  Running from: {SCRIPT_DIR}",\n                font=FONT_DESC, text_color=COLOR_TEXT_DIM,\n                anchor="w"\n            ).pack(side="left", padx=(8, 0))\n\n        div = ctk.CTkFrame(self._launch_container, fg_color=COLOR_DIVIDER,\n                           height=1)\n        div.pack(fill="x", padx=20, pady=(0, 8))\n\n        cards_frame = ctk.CTkFrame(self._launch_container,\n                                   fg_color="transparent")\n        cards_frame.pack(fill="x", padx=20, pady=(0, 4))\n\n        for i, entry in enumerate(entries):\n            # A bare string is a HEADING inside the group, not a\n            # card. The maintenance runner prints GENERATORS then\n            # CHECKERS, and the indented list here is that same\n            # list, so it reads the same way. Alphabetical order\n            # within each half is Tony\'s, 2026-09-12: without the\n            # two labels a sorted run of twenty buttons gives no\n            # clue where one kind stops and the other starts.\n            if isinstance(entry, str):\n                self._build_indent_heading(cards_frame, entry)\n                continue\n            name, script, desc = entry[0], entry[1], entry[2]\n            base_dir = entry[3] if len(entry) > 3 else SCRIPT_DIR\n            interactive = entry[4] if len(entry) > 4 else False\n            args = entry[5] if len(entry) > 5 else None\n            indent = entry[6] if len(entry) > 6 else False\n            self._build_launch_card(cards_frame, name, script, desc,\n                                    base_dir, interactive, args, i,\n                                    indent)\n'))
EDITS.append(('DOCSTRING  the change-log entry for L-341',
    b'documentation/run_hover_budget.py to wrap it.\n"""\n',
    b'documentation/run_hover_budget.py to wrap it.\nSeptember 19, 2026 with Anthropic\'s Claude Opus 5 (L-341): a Find a tool\nsearch box above the groups, and the two oversized groups split. Tony\nhad just run a tool from a terminal that this dashboard already carried\na button for, and asked for both. The search filters on NAME AND\nDESCRIPTION and draws each match under its own group heading rather\nthan in one flat list, so it answers "where does this live" as well as\n"where is it" -- his choice, because he prefers a visual check and\nbecause the second answer is the one that makes the search unnecessary\nnext time. Gallery & Web became Gallery -- checks and data and Gallery\n-- authoring; Developer Tools became Maintenance Run and Tools and\nCaches; Gallery Cache Builder -- Manual Run moved to the gallery group,\nwhere its GALLERY_REPO_DIR base always said it belonged. NO entry was\nreordered and no description was touched: in particular the twenty\ncheckers under the maintenance runner stay in one alphabetical run,\nbecause that arrangement is Tony\'s ruling of 2026-09-12 and re-sorting\nthem by kind would overturn it silently. The groups now draw into their\nown container frame so a search can rebuild them without disturbing the\nheader, the resources section or the footer.\n"""\n'))


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
             "\nIf the patch already ran, this is what a second run looks "
             "like: it refuses.")

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
    print("  1. Open the dashboard and LOOK at it. Seven groups, a Find a")
    print("     tool box at the top. Type 'export' and check that")
    print("     Constants Export Pull appears under Gallery -- checks and")
    print("     data. Clear it and check everything comes back.")
    print("  2. Run the orrery maintenance run.")
    print("  3. Move this script into documentation/.")
    print("  4. Commit EVERYTHING the run touched, including any")
    print("     regenerated file, and push. Report the new SHA.")
    print("")
    print("Undo at any point is Discard Changes in GitHub Desktop.")


if __name__ == "__main__":
    main()
