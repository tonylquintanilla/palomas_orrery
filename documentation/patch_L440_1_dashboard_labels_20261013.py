"""patch_L440_1_dashboard_labels_20261013.py -- L-440: the dashboard's
cards say what each tool is, the website checks sit under six headings
that fold, and a new check holds the run steps and the buttons together.

Built on orrery db63721d258004b855c1259371d8adf15bf7647c at
https://github.com/tonylquintanilla/palomas_orrery ("L437 close").
The gallery is read (by the new checker) and not touched.
Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\;
gallery C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\.
Written October 13, 2026 with Anthropic's Claude Opus 5.5.
Record: documentation/HANDOFF_L440_dashboard_labels_20261013.md (written
by this patch). Brief: documentation/HANDOFF_dashboard_labels_brief_20261012.md.

HOW TO RUN
    Save it in the orrery repo's ROOT folder, open it in VS Code and
    press Run, or from a terminal in that folder:
        python patch_L440_1_dashboard_labels_20261013.py
    Success prints one "ok" line per edit, then "patch applied". It asks
    nothing and fetches nothing. A second run finds its new files already
    there and writes nothing.

WHAT IT CHANGES
    palomas_orrery_dashboard.py: every card shows its script and a short
      line, the paragraph under "+ more"; text wraps to the window;
      headings fold; the website checks get six headings; buttons under
      a runner take the run's names; CARD_LINES; Paloma's Orrery opens
      its own console window; the docstring says what changed and why.
    orrery_maintenance_run.py: CHECKERS gains Dashboard parity; the
      GATING AND REPORT-ONLY count is restated from the table.
    test_dashboard_parity.py (new): the check, nine faults planted.
    LEDGER_CONSOLIDATED.md: the L-440 block, one stamp line, a note on
      L-324. documentation/WHERE_WE_ARE.md: by section, never below the
      run-record marker, within its 130-line cap. The handoff (new).
    The script is disposable. What it installs is permanent: the card
    and CARD_LINES, the folding headings, the website group's headings,
    the run names on the buttons, and the new check with its row.

SAFETY
    Other sessions build beside this one. The dashboard's groups are
    rebuilt from their own structure, so a button another session added
    to the orrery's group is kept and sorted into place; one added to the
    website group stops the patch, since only its session can say which
    heading it belongs under. Every other edit is anchored on lines this
    patch alone changes, matched exactly once; your notes in the page and
    the ledger cannot make it refuse. If any check fails, NOTHING is
    written. A file with Windows line endings is matched as LF and written
    back LF, and the patch says so. Undo after a run is Discard Changes in
    GitHub Desktop, and delete the two new files.

Role: patch
Domain: dev_tools
"""
import ast
import hashlib
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
DASHBOARD = 'palomas_orrery_dashboard.py'
RUNNER = 'orrery_maintenance_run.py'
LEDGER = 'LEDGER_CONSOLIDATED.md'
PARITY_FILE = 'test_dashboard_parity.py'
HANDOFF_FILE = 'documentation/HANDOFF_L440_dashboard_labels_20261013.md'
BASE_SHORT = 'db63721d'
GALLERY_SHORT = '924977a3'
REGION_MD5 = 'b821e87a18cfde96be64e0c4751f3d1a'

NEW_REGION = '    def _entry_matches(self, group_name, entry, needle):\n        """Name, short line or description contains `needle`, any case.\n\n        The short line is searched as well as the paragraph (L-440): it\n        is the text a card shows, so a word read on a card finds it.\n        """\n        return (needle in entry[0].lower()\n                or needle in card_line(group_name, entry[0]).lower()\n                or needle in entry[2].lower())\n\n    def _render_launch(self, query):\n        """Draw the groups, filtered by `query`.\n\n        An empty query draws everything, which is the ordinary view. A\n        non-empty one draws only the groups that still have a match, and\n        only the matching buttons inside them. A group with nothing left\n        is not drawn at all, so the headings that remain are themselves\n        the answer to "where does this live". A heading inside a group\n        is kept when a card under it matches, so a match is also shown\n        under its own heading (L-440).\n        """\n        for child in self._launch_container.winfo_children():\n            child.destroy()\n\n        needle = (query or "").strip().lower()\n        self._rendered_query = needle\n        shown = 0\n\n        for group_name, entries in LAUNCH_GROUPS.items():\n            if not needle:\n                drawn = list(entries)\n            elif needle in group_name.lower():\n                # The GROUP NAME counts as a match, and takes the whole\n                # group with it. Typing "stars" found nothing before\n                # this: the Stars group exists, but its one button is\n                # called Star Visualization and no description says\n                # "stars". Somebody typing a category name means the\n                # category. (Found by testing, 2026-09-19.)\n                drawn = list(entries)\n            else:\n                drawn = filter_entries(\n                    entries,\n                    lambda e, g=group_name: self._entry_matches(g, e, needle))\n            if not drawn:\n                continue\n            shown += sum(1 for e in drawn if not isinstance(e, str))\n            self._build_group(group_name, drawn)\n\n        if not needle:\n            self._search_status.configure(\n                text="%d buttons in %d groups"\n                     % (self._launch_entry_total(), len(LAUNCH_GROUPS)))\n        elif shown:\n            self._search_status.configure(\n                text="%d of %d match \\u2014 shown under their own headings"\n                     % (shown, self._launch_entry_total()))\n        else:\n            self._search_status.configure(\n                text="nothing matches \\u2014 try fewer letters, or Clear")\n\n    def _build_group(self, group_name, entries):\n        """One group heading, its divider, and its cards."""\n        section_frame = ctk.CTkFrame(self._launch_container,\n                                     fg_color="transparent")\n        section_frame.pack(fill="x", padx=20, pady=(16, 4))\n\n        symbol = SECTION_SYMBOLS.get(group_name, "")\n        ctk.CTkLabel(\n            section_frame,\n            text=f"{symbol}  {group_name}",\n            font=FONT_SECTION, text_color=COLOR_TEXT,\n            anchor="w"\n        ).pack(side="left")\n\n        # The repo-auditing groups remind the user which codebase\n        # directory these tools examine. Multiple copies of the repo\n        # exist (sandbox, clean repo, cloud snapshots) and running\n        # against the wrong one produces misleading results.\n        if group_name in REPO_AUDIT_GROUPS:\n            ctk.CTkLabel(\n                section_frame,\n                text=f"  Running from: {SCRIPT_DIR}",\n                font=FONT_DESC, text_color=COLOR_TEXT_DIM,\n                anchor="w"\n            ).pack(side="left", padx=(8, 0))\n\n        div = ctk.CTkFrame(self._launch_container, fg_color=COLOR_DIVIDER,\n                           height=1)\n        div.pack(fill="x", padx=20, pady=(0, 8))\n\n        cards_frame = ctk.CTkFrame(self._launch_container,\n                                   fg_color="transparent")\n        cards_frame.pack(fill="x", padx=20, pady=(0, 4))\n\n        # The frame holding the cards under the current heading, or None\n        # outside any heading. A heading\'s cards run to the next heading\n        # or to the first card that is not indented (the live runner at\n        # the foot of the website group), whichever comes first.\n        section = None\n        for i, entry in enumerate(entries):\n            # A bare string is a HEADING inside the group, not a\n            # card. The maintenance runner prints GENERATORS then\n            # CHECKERS, and the indented list here is that same\n            # list, so it reads the same way. Alphabetical order\n            # within each half is Tony\'s, 2026-09-12: without the\n            # two labels a sorted run of twenty buttons gives no\n            # clue where one kind stops and the other starts.\n            if isinstance(entry, str):\n                section = self._build_indent_heading(cards_frame, entry)\n                continue\n            name, script, desc = entry[0], entry[1], entry[2]\n            base_dir = entry[3] if len(entry) > 3 else SCRIPT_DIR\n            interactive = entry[4] if len(entry) > 4 else False\n            args = entry[5] if len(entry) > 5 else None\n            indent = entry[6] if len(entry) > 6 else False\n            if not indent:\n                section = None\n            parent = section if section is not None else cards_frame\n            self._build_launch_card(parent, group_name, name, script, desc,\n                                    base_dir, interactive, args, i,\n                                    indent)\n\n    def _build_indent_heading(self, parent, text):\n        """A heading inside a group, which folds the cards under it.\n\n        Drawn for a bare string in a LAUNCH_GROUPS list. Not a card: it\n        names which part of the group the buttons below it belong to,\n        and clicking it hides or shows them (Tony, 2026-10-13, L-440).\n        "-" in front means open, "+" means folded. Every heading starts\n        OPEN when the dashboard launches, so what a runner runs stays\n        visible, which is Tony\'s ruling of 2026-08-12; folding is for\n        the moment, and is not remembered. Returns the frame the cards\n        under it are drawn into.\n        """\n        state = {"open": True}\n        heading = ctk.CTkButton(\n            parent, text="-  " + text, anchor="w",\n            font=FONT_DESC, text_color=COLOR_TEXT_DIM,\n            fg_color="transparent", hover_color=COLOR_SURFACE_HOVER,\n            height=24, corner_radius=6\n        )\n        heading.pack(anchor="w", padx=(22, 0), pady=(10, 2))\n        section = ctk.CTkFrame(parent, fg_color="transparent")\n        section.pack(fill="x")\n\n        def toggle():\n            if state["open"]:\n                section.pack_forget()\n                heading.configure(text="+  " + text)\n            else:\n                section.pack(fill="x", after=heading)\n                heading.configure(text="-  " + text)\n            state["open"] = not state["open"]\n\n        heading.configure(command=toggle)\n        return section\n\n    def _build_launch_card(self, parent, group_name, name, script, desc,\n                           base_dir, interactive, args, index,\n                           indent=False):\n        """Individual launch card: name, script, short line, paragraph.\n\n        `indent` marks a tool that the maintenance runner already covers.\n        Indenting rather than removing was Tony\'s ruling of 2026-08-12:\n        the individual entries stay launchable, and staying visible is how\n        the automation\'s contents remain known instead of disappearing\n        behind one button. The runner sits directly above its indented\n        group.\n\n        The card (L-440, Tony\'s choice of option B, 2026-10-13): the name;\n        the repository and script it runs, in small type, so the mapping\n        is visible without hovering; the short line from CARD_LINES; and\n        the paragraph, opened in place by "+ more". A card with no short\n        line yet shows its paragraph, as every card did before, so\n        nothing is hidden, and Dashboard Parity names the card. Text\n        wraps to the column\'s width, and the Launch button is packed\n        first, so a narrow window never pushes the button off the card.\n        """\n        card = ctk.CTkFrame(parent, fg_color=COLOR_SURFACE,\n                            corner_radius=10)\n        card.pack(fill="x", pady=4, ipady=4,\n                  padx=(28, 0) if indent else 0)\n\n        inner = ctk.CTkFrame(card, fg_color="transparent")\n        inner.pack(fill="x", padx=16, pady=6)\n\n        # Right side first: the launch button keeps its place whatever\n        # the window\'s width.\n        script_path = os.path.join(base_dir, script)\n        exists = os.path.exists(script_path)\n\n        btn = ctk.CTkButton(\n            inner,\n            text="Launch" if exists else "Not Found",\n            font=FONT_DESC,\n            width=100,\n            height=32,\n            fg_color=COLOR_BUTTON_BG if exists else COLOR_DIVIDER,\n            hover_color=COLOR_BUTTON_HOVER if exists else COLOR_DIVIDER,\n            text_color=COLOR_TEXT if exists else COLOR_TEXT_DIM,\n            corner_radius=8,\n            command=lambda s=script, b=base_dir, ia=interactive, a=args: self._launch(s, b, ia, a),\n            state="normal" if exists else "disabled"\n        )\n        btn.pack(side="right", padx=(12, 0))\n\n        # Name the repo and file this button runs. A missing script shows\n        # the full path instead, so "Not Found" says where it looked.\n        if exists:\n            target = launch_target_label(script, base_dir, args)\n        else:\n            target = "Not found: %s" % script_path\n        Tooltip(btn, target)\n\n        # Left side: name, script, short line, paragraph.\n        text_frame = ctk.CTkFrame(inner, fg_color="transparent")\n        text_frame.pack(side="left", fill="x", expand=True)\n\n        title_row = ctk.CTkFrame(text_frame, fg_color="transparent")\n        title_row.pack(anchor="w", fill="x")\n        ctk.CTkLabel(\n            title_row, text=name,\n            font=FONT_BUTTON, text_color=COLOR_TEXT, anchor="w"\n        ).pack(side="left")\n\n        ctk.CTkLabel(\n            text_frame, text=target,\n            font=FONT_SCRIPT, text_color=COLOR_TEXT_DIM, anchor="w",\n            justify="left"\n        ).pack(anchor="w")\n\n        wrapped = []\n        short = card_line(group_name, name)\n        para = ctk.CTkLabel(\n            text_frame, text=desc,\n            font=FONT_DESC, text_color=COLOR_TEXT_DIM, anchor="w",\n            wraplength=600, justify="left"\n        )\n        wrapped.append(para)\n        if short:\n            line = ctk.CTkLabel(\n                text_frame, text=short,\n                font=FONT_DESC, text_color=COLOR_TEXT, anchor="w",\n                wraplength=600, justify="left"\n            )\n            line.pack(anchor="w")\n            wrapped.insert(0, line)\n            state = {"open": False}\n            more = ctk.CTkButton(\n                title_row, text="+ more", width=60, height=22,\n                font=FONT_DESC, fg_color="transparent",\n                hover_color=COLOR_BUTTON_HOVER, text_color=COLOR_LINK\n            )\n\n            def toggle(p=para, s=state, m=more):\n                if s["open"]:\n                    p.pack_forget()\n                    m.configure(text="+ more")\n                else:\n                    p.pack(anchor="w", pady=(4, 0))\n                    m.configure(text="- less")\n                s["open"] = not s["open"]\n\n            more.configure(command=toggle)\n            more.pack(side="left", padx=(10, 0))\n        else:\n            para.pack(anchor="w")\n\n        last = {"width": None}\n\n        def rewrap(event, labels=wrapped, last=last):\n            # CTk scales a wraplength by the display\'s scaling, while the\n            # event gives real pixels, so divide the scaling back out.\n            if event.width == last["width"]:\n                return\n            last["width"] = event.width\n            for lab in labels:\n                try:\n                    scale = lab._get_widget_scaling()\n                except Exception:\n                    scale = 1.0\n                lab.configure(wraplength=max(200, int((event.width - 8)\n                                                      / scale)))\n\n        text_frame.bind("<Configure>", rewrap, add="+")\n\n'

PARITY_SOURCE = '"""\ntest_dashboard_parity.py - every step the maintenance runs and the Daily\nRun take has a dashboard button with the same name and the same script,\nevery button under a runner names one of its steps, every button\'s\nscript is on disk, and every card carries its short line; and proof that\nthis check can fail.\n\nWHY THIS EXISTS\n\n    When a row of a maintenance run goes red, you go to the dashboard to\n    run that one check again, so its button has to carry the name the run\n    printed (Tony\'s ruling of 2026-10-12, recorded in\n    documentation/DESIGN_rulings_20261012.md). Every new check gets its\n    button (Tony, 2026-10-10). Until now nothing held either rule: L-416\n    matched the lists by hand three times, and L-324\'s note of 2026-09-12\n    left this check as backlog. This is that check (L-440).\n\nRUN COMMAND\n\n    Open this file in VS Code and click Run. It takes no arguments.\n        python test_dashboard_parity.py\n    The orrery maintenance run runs it as the gating checker "Dashboard\n    parity"; its last line starts "DASHBOARD PARITY:".\n\nWHAT IT READS (both repositories; it edits neither)\n\n    palomas_orrery_dashboard.py      LAUNCH_GROUPS and CARD_LINES. Loaded\n                                     with its window libraries replaced by\n                                     stand-ins, so no window opens and no\n                                     display is needed.\n    orrery_maintenance_run.py        GENERATORS and CHECKERS\n    ../tonyquintanilla.github.io/gallery_maintenance_run.py\n                                     GENERATORS and OFFLINE_CHECKERS\n    ../tonyquintanilla.github.io/daily_run.py\n                                     STEPS\n    A runner it cannot find or read FAILS the run and is named. It is\n    never skipped.\n\nTHE RULES IT HOLDS, by name, in both directions\n\n    1. Every step has a button in its group -- the orrery\'s runs in\n       "Maintenance Run", the website\'s in "Gallery -- checks and data",\n       the Daily Run\'s in "Daily Run" -- with the same name. Names are\n       compared ignoring case, a trailing "(L-...)" handle, and the\n       difference between " -- " and ", ".\n    2. That button runs the same script, with the same arguments, from\n       the same repository. A Node step is run from the dashboard through\n       documentation/run_offline_check.py with the step\'s own label, or\n       through a wrapper named in WRAPPERS below.\n    3. Every indented button in those three groups names a step.\n    4. Every button\'s script is on disk (the dashboard\'s "Not Found").\n    5. Every card has a line in CARD_LINES, of twelve words or fewer, and\n       every line in CARD_LINES belongs to a card.\n    The few steps a differently named button covers on purpose are in\n    COVERED_BY, each with its reason; they are printed on every run so\n    that they stay known.\n\n    Not compared: the website\'s three LIVE checks (Served reachability,\n    Export freshness, Store drift). They are functions inside the live\n    run, not scripts, and the "Gallery Maintenance Run -- live" button\n    runs them.\n\nPROOF THAT IT CAN FAIL\n\n    Before the real comparison it plants nine faults, one at a time, in\n    copies of the real lists, and each must be caught by its own kind of\n    finding: a step with no button, a renamed button, a button running\n    the wrong script, a missing script, a card with no line, a line over\n    twelve words, a line for no card, an indented button naming no step,\n    and an unreadable runner.\n\nRole: devtool\nDomain: dev_tools\n\nModule created: October 13, 2026 with Anthropic\'s Claude Opus 5.5 (L-440,\nthe dashboard\'s labels, descriptions and findability).\n"""\n\nimport ast\nimport copy\nimport importlib.util\nimport os\nimport re\nimport sys\nimport types\n\nHERE = os.path.dirname(os.path.abspath(__file__))\nDASHBOARD = os.path.join(HERE, \'palomas_orrery_dashboard.py\')\nORRERY_RUN = os.path.join(HERE, \'orrery_maintenance_run.py\')\nGALLERY = os.path.normpath(os.path.join(HERE, \'..\', \'tonyquintanilla.github.io\'))\n\nORRERY_GROUP = \'Maintenance Run\'\nGALLERY_GROUP = \'Gallery -- checks and data\'\nDAILY_GROUP = \'Daily Run\'\nMAX_WORDS = 12\n\n# Steps a differently named button covers on purpose: (repo, step) ->\n# (button, reason). Printed on every run.\nCOVERED_BY = {\n    (\'gallery\', \'Config mirror\'): (\n        \'Config Mirror -- report only\',\n        \'the same tool without --write: the run does the writing, the \'\n        \'button only reports (2026-09-17)\'),\n    (\'gallery\', \'Objects mirror\'): (\n        \'Objects Mirror Check\',\n        \'the same tool without --write, which is also the checker step \'\n        \'"Objects mirror check"\'),\n    (\'gallery\', \'Guest book\'): (\n        \'Guest Book Checks\',\n        \'both guest book checks behind one button (L-281)\'),\n    (\'gallery\', \'Guest book updater\'): (\n        \'Guest Book Checks\',\n        \'both guest book checks behind one button (L-281)\'),\n}\n\n# A Node step the dashboard runs through a wrapper of its own.\nWRAPPERS = {\n    \'Hover budget\': \'documentation/run_hover_budget.py\',\n    \'Solar System figures\': \'documentation/run_solar_system_figures.py\',\n}\nNODE_RUNNER = \'documentation/run_offline_check.py\'\n\n# Arguments a button leaves out because the script uses the same value by\n# default: (repo, step) -> (argument, reason).\nDEFAULT_ARGS = {\n    (\'orrery\', \'Skill manifest\'): (\n        \'PROJECT_INSTRUCTIONS.md\',\n        \'skills_index.py defaults to PROJECT_INSTRUCTIONS.md\'),\n}\n\n\nclass Unreadable(Exception):\n    """A file this check must read could not be read."""\n\n\ndef norm(name):\n    """A name as compared: case, a trailing (L-...) and dashes ignored."""\n    text = re.sub(r\'\\s*\\([^)]*L-\\d+[^)]*\\)\\s*$\', \'\', name.strip())\n    text = text.replace(\' -- \', \' \').replace(\', \', \' \')\n    return \' \'.join(text.casefold().split())\n\n\ndef _literal(path, name):\n    """A module-level list, read by ast without running the file."""\n    try:\n        with open(path, encoding=\'utf-8\') as f:\n            tree = ast.parse(f.read())\n    except (OSError, SyntaxError, UnicodeDecodeError) as exc:\n        raise Unreadable(\'%s: %s\' % (path, exc))\n    for node in tree.body:\n        if (isinstance(node, ast.Assign) and len(node.targets) == 1\n                and getattr(node.targets[0], \'id\', None) == name):\n            return node.value\n    raise Unreadable(\'%s: no %s list\' % (path, name))\n\n\ndef _value(node):\n    """ast.literal_eval, plus os.path.join over string literals."""\n    if (isinstance(node, ast.Call)\n            and ast.unparse(node.func) == \'os.path.join\'):\n        return \'/\'.join(_value(a) for a in node.args)\n    if isinstance(node, (ast.List, ast.Tuple)):\n        return [_value(e) for e in node.elts]\n    return ast.literal_eval(node)\n\n\ndef read_runs(orrery_run=ORRERY_RUN, gallery=GALLERY):\n    """Every step, as dicts: repo, kind, name, script, args."""\n    steps = []\n    for kind in (\'GENERATORS\', \'CHECKERS\'):\n        for row in _value(_literal(orrery_run, kind)):\n            argv = row[1]\n            steps.append(dict(repo=\'orrery\', kind=kind, name=row[0],\n                              script=argv[0], args=list(argv[1:]),\n                              node=False))\n    grun = os.path.join(gallery, \'gallery_maintenance_run.py\')\n    for row in _value(_literal(grun, \'GENERATORS\')):\n        argv, cwd = row[1], row[2]\n        steps.append(dict(repo=\'gallery\', kind=\'GENERATORS\', name=row[0],\n                          script=_join(cwd, argv[0]), args=list(argv[1:]),\n                          node=False))\n    for row in _value(_literal(grun, \'OFFLINE_CHECKERS\')):\n        runner, argv, cwd = row[1], row[2], row[3]\n        steps.append(dict(repo=\'gallery\', kind=\'CHECKERS\', name=row[0],\n                          script=_join(cwd, argv[0]), args=list(argv[1:]),\n                          node=(runner == \'node\')))\n    daily = os.path.join(gallery, \'daily_run.py\')\n    for row in _value(_literal(daily, \'STEPS\')):\n        steps.append(dict(repo=\'gallery\', kind=\'DAILY\', name=row[0],\n                          script=row[1], args=list(row[2]), node=False))\n    return steps\n\n\ndef _join(cwd, script):\n    if cwd in (\'\', \'.\'):\n        return script\n    return cwd.rstrip(\'/\') + \'/\' + script\n\n\nclass _Stand(types.ModuleType):\n    """A stand-in module: every attribute is a harmless class."""\n\n    def __getattr__(self, name):\n        if name.startswith(\'__\'):\n            raise AttributeError(name)\n        return type(name, (object,), {\'__init__\': lambda s, *a, **k: None})\n\n\ndef read_dashboard(path=DASHBOARD):\n    """(LAUNCH_GROUPS, CARD_LINES, SCRIPT_DIR, GALLERY_REPO_DIR)."""\n    saved = {}\n    for name in (\'tkinter\', \'customtkinter\', \'PIL\', \'PIL.Image\',\n                 \'PIL.ImageTk\'):\n        saved[name] = sys.modules.get(name)\n        sys.modules[name] = _Stand(name)\n    try:\n        spec = importlib.util.spec_from_file_location(\'_dash_parity\', path)\n        module = importlib.util.module_from_spec(spec)\n        spec.loader.exec_module(module)\n    except Exception as exc:\n        raise Unreadable(\'%s: %s: %s\' % (path, type(exc).__name__, exc))\n    finally:\n        for name, mod in saved.items():\n            if mod is None:\n                sys.modules.pop(name, None)\n            else:\n                sys.modules[name] = mod\n    lines = getattr(module, \'CARD_LINES\', None)\n    if lines is None:\n        raise Unreadable(\'%s: no CARD_LINES\' % path)\n    return (module.LAUNCH_GROUPS, lines, module.SCRIPT_DIR,\n            module.GALLERY_REPO_DIR)\n\n\ndef buttons_of(groups, script_dir, gallery_dir):\n    """Every card, as dicts: group, name, repo, script, args, indent."""\n    out = []\n    groot = os.path.abspath(gallery_dir)\n    oroot = os.path.abspath(script_dir)\n    for group, entries in groups.items():\n        for e in entries:\n            if isinstance(e, str):\n                continue\n            base = e[3] if len(e) > 3 else script_dir\n            full = os.path.abspath(os.path.join(base, e[1]))\n            if full.startswith(groot + os.sep):\n                repo, rel = \'gallery\', os.path.relpath(full, groot)\n            else:\n                repo, rel = \'orrery\', os.path.relpath(full, oroot)\n            out.append(dict(group=group, name=e[0], repo=repo,\n                            script=rel.replace(os.sep, \'/\'),\n                            args=list(e[5]) if len(e) > 5 and e[5] else [],\n                            indent=bool(e[6]) if len(e) > 6 else False,\n                            path=full))\n    return out\n\n\ndef group_of(step):\n    if step[\'kind\'] == \'DAILY\':\n        return DAILY_GROUP\n    return ORRERY_GROUP if step[\'repo\'] == \'orrery\' else GALLERY_GROUP\n\n\ndef compare(steps, buttons, card_lines):\n    """All findings, as (kind, text). Empty means everything agrees."""\n    found = []\n    by_group = {}\n    for b in buttons:\n        by_group.setdefault(b[\'group\'], []).append(b)\n    claimed = set()\n    for s in steps:\n        group = group_of(s)\n        pool = by_group.get(group, [])\n        cover = COVERED_BY.get((s[\'repo\'], s[\'name\']))\n        if cover and s[\'kind\'] != \'DAILY\':\n            want = norm(cover[0])\n        else:\n            want = norm(s[\'name\'])\n        hits = [b for b in pool if norm(b[\'name\']) == want]\n        if not hits:\n            found.append((\'NO BUTTON\', \'%s step "%s" (%s) has no button \'\n                          \'named so in "%s"\' % (s[\'repo\'], s[\'name\'],\n                                                s[\'script\'], group)))\n            continue\n        b = hits[0]\n        claimed.add((group, b[\'name\']))\n        problem = _command_problem(s, b, cover)\n        if problem:\n            found.append((\'WRONG SCRIPT\', \'"%s" in "%s" %s\'\n                          % (b[\'name\'], group, problem)))\n    for group in (ORRERY_GROUP, GALLERY_GROUP, DAILY_GROUP):\n        for b in by_group.get(group, []):\n            if b[\'indent\'] and (group, b[\'name\']) not in claimed:\n                found.append((\'NAMES NO STEP\', \'indented button "%s" in \'\n                              \'"%s" names no step of its run\'\n                              % (b[\'name\'], group)))\n    for b in buttons:\n        if not os.path.exists(b[\'path\']):\n            found.append((\'NOT FOUND\', \'"%s" in "%s": %s is not on disk\'\n                          % (b[\'name\'], b[\'group\'], b[\'path\'])))\n    cards = set((b[\'group\'], b[\'name\']) for b in buttons)\n    for key in sorted(cards):\n        line = card_lines.get(key)\n        if not line:\n            found.append((\'NO LINE\', \'card "%s" in "%s" has no short line \'\n                          \'in CARD_LINES\' % (key[1], key[0])))\n        elif len(line.split()) > MAX_WORDS:\n            found.append((\'LINE TOO LONG\', \'card "%s" in "%s": %d words, \'\n                          \'the limit is %d\' % (key[1], key[0],\n                                               len(line.split()), MAX_WORDS)))\n    for key in sorted(set(card_lines) - cards):\n        found.append((\'LINE FOR NO CARD\', \'CARD_LINES has a line for "%s" \'\n                      \'in "%s", and no such card exists\' % (key[1], key[0])))\n    return found\n\n\ndef _command_problem(s, b, cover):\n    """Why button b does not run step s, or None."""\n    if b[\'repo\'] != s[\'repo\']:\n        return \'runs a %s script; the step is in the %s\' % (b[\'repo\'],\n                                                           s[\'repo\'])\n    if s[\'node\']:\n        if s[\'name\'] in WRAPPERS:\n            if b[\'script\'] == WRAPPERS[s[\'name\']]:\n                return None\n            return \'runs %s; the step is wrapped by %s\' % (\n                b[\'script\'], WRAPPERS[s[\'name\']])\n        if cover:\n            return None\n        if b[\'script\'] == NODE_RUNNER and b[\'args\'] == [s[\'name\']]:\n            return None\n        return \'runs %s %s; a Node step runs through %s "%s"\' % (\n            b[\'script\'], \' \'.join(b[\'args\']), NODE_RUNNER, s[\'name\'])\n    if cover and s[\'kind\'] != \'DAILY\':\n        if b[\'script\'] == s[\'script\']:\n            return None\n        if cover[0] == \'Guest Book Checks\':\n            return None\n        return \'runs %s; the step runs %s\' % (b[\'script\'], s[\'script\'])\n    if b[\'script\'] != s[\'script\']:\n        return \'runs %s; the step runs %s\' % (b[\'script\'], s[\'script\'])\n    want = list(s[\'args\'])\n    default = DEFAULT_ARGS.get((s[\'repo\'], s[\'name\']))\n    if default and default[0] in want and default[0] not in b[\'args\']:\n        want.remove(default[0])\n    if b[\'args\'] != want:\n        return \'passes %s; the step passes %s\' % (b[\'args\'] or \'nothing\',\n                                                   want or \'nothing\')\n    return None\n\n\ndef planted(steps, buttons, lines):\n    """Nine faults, each required to produce its own kind of finding."""\n    results = []\n\n    def one(label, kind, s=steps, b=buttons, c=lines, runner=None):\n        if runner is not None:\n            try:\n                runner()\n                got = []\n            except Unreadable as exc:\n                got = [(\'UNREADABLE\', str(exc))]\n        else:\n            got = compare(s, b, c)\n        ok = any(k == kind for k, _t in got)\n        results.append((label, kind, ok))\n\n    def edit(name, field, value):\n        bb = copy.deepcopy(buttons)\n        for x in bb:\n            if x[\'name\'] == name and x[\'group\'] == ORRERY_GROUP:\n                x[field] = value\n        return bb\n\n    s1 = copy.deepcopy(steps) + [dict(repo=\'orrery\', kind=\'CHECKERS\',\n                                      name=\'Planted step\',\n                                      script=\'planted_step.py\', args=[],\n                                      node=False)]\n    one(\'a step with no button\', \'NO BUTTON\', s=s1)\n    one(\'a renamed button\', \'NO BUTTON\',\n        b=edit(\'Position Digits\', \'name\', \'Position Digit\'))\n    one(\'a button running the wrong script\', \'WRONG SCRIPT\',\n        b=edit(\'Position Digits\', \'script\', \'test_orbit_markers.py\'))\n    one(\'a missing script\', \'NOT FOUND\',\n        b=edit(\'Position Digits\', \'path\',\n               os.path.join(HERE, \'no_such_script_planted.py\')))\n    c5 = dict(lines)\n    c5.pop((ORRERY_GROUP, \'Position Digits\'), None)\n    one(\'a card with no line\', \'NO LINE\', c=c5)\n    c6 = dict(lines)\n    c6[(ORRERY_GROUP, \'Position Digits\')] = \' \'.join([\'word\'] * 13)\n    one(\'a line over twelve words\', \'LINE TOO LONG\', c=c6)\n    c7 = dict(lines)\n    c7[(ORRERY_GROUP, \'Planted Card\')] = \'A line for a card that is not there.\'\n    one(\'a line for no card\', \'LINE FOR NO CARD\', c=c7)\n    b8 = copy.deepcopy(buttons) + [dict(group=ORRERY_GROUP,\n                                        name=\'Planted Indented\', repo=\'orrery\',\n                                        script=\'test_position_digits.py\',\n                                        args=[], indent=True,\n                                        path=os.path.join(\n                                            HERE, \'test_position_digits.py\'))]\n    c8 = dict(lines)\n    c8[(ORRERY_GROUP, \'Planted Indented\')] = \'A planted card.\'\n    one(\'an indented button naming no step\', \'NAMES NO STEP\', b=b8, c=c8)\n    one(\'an unreadable runner\', \'UNREADABLE\',\n        runner=lambda: read_runs(gallery=os.path.join(HERE,\n                                                      \'no_such_gallery\')))\n    return results\n\n\ndef main():\n    print(\'DASHBOARD PARITY -- run steps against dashboard buttons (L-440)\')\n    print(\'  dashboard: %s\' % DASHBOARD)\n    print(\'  orrery run: %s\' % ORRERY_RUN)\n    print(\'  website repo: %s\' % GALLERY)\n    try:\n        steps = read_runs()\n        groups, lines, sdir, gdir = read_dashboard()\n    except Unreadable as exc:\n        print(\'\')\n        print(\'CANNOT READ: %s\' % exc)\n        print(\'DASHBOARD PARITY: FAIL -- a file it must read could not be \'\n              \'read, so nothing was compared\')\n        return 1\n    buttons = buttons_of(groups, sdir, gdir)\n\n    print(\'\')\n    print(\'Planted faults, each must be caught by its own kind of finding:\')\n    caught = 0\n    results = planted(steps, buttons, lines)\n    for label, kind, ok in results:\n        caught += ok\n        print(\'  %-6s %-36s -> %s\' % (\'caught\' if ok else \'MISSED\', label,\n                                      kind))\n\n    found = compare(steps, buttons, lines)\n    counts = {}\n    for s in steps:\n        key = \'Daily Run\' if s[\'kind\'] == \'DAILY\' else s[\'repo\']\n        counts[key] = counts.get(key, 0) + 1\n    print(\'\')\n    print(\'Compared %d orrery steps, %d website steps and %d Daily Run \'\n          \'steps against %d buttons in %d groups; %d short lines read.\'\n          % (counts.get(\'orrery\', 0), counts.get(\'gallery\', 0),\n             counts.get(\'Daily Run\', 0), len(buttons), len(groups),\n             len(lines)))\n    print(\'Covered by a differently named button, on purpose (%d):\'\n          % len(COVERED_BY))\n    for (repo, step), (button, why) in sorted(COVERED_BY.items()):\n        print(\'  %s "%s" -> "%s": %s\' % (repo, step, button, why))\n    print(\'Not compared: the website\\\'s live checks, which are functions \'\n          \'inside the live run (Served reachability, Export freshness, \'\n          \'Store drift).\')\n    if found:\n        print(\'\')\n        print(\'FINDINGS (%d):\' % len(found))\n        for kind, text in found:\n            print(\'  %-16s %s\' % (kind, text))\n    print(\'\')\n    total = len(results)\n    if found or caught != total:\n        print(\'DASHBOARD PARITY: FAIL -- %d finding(s); %d of %d planted \'\n              \'faults caught\' % (len(found), caught, total))\n        return 1\n    print(\'DASHBOARD PARITY: PASS -- %d of %d planted faults caught; %d \'\n          \'steps matched to their buttons by name and script; %d cards \'\n          \'carry a short line\' % (caught, total, len(steps),\n                                  len(set((b[\'group\'], b[\'name\'])\n                                          for b in buttons))))\n    return 0\n\n\nif __name__ == \'__main__\':\n    sys.exit(main())\n'

L440_BLOCK = '#### [L-440] The dashboard\'s labels, short lines and headings, and the parity check (dashboard, both repos)\n<!-- L:440 status:OPEN upd:2026-10-13 section:A flag: rice: -->\n- **Tony\'s request, 2026-10-12**, after confirming every run step has a\n  button: "Could you check for labeling that is easily recognizable\n  based on the script name and functionality? And pithy descriptions?\n  And easy way to find besides search?" Brief:\n  `documentation/HANDOFF_dashboard_labels_brief_20261012.md`, with its\n  audit `documentation/AUDIT_dashboard_labels_20261012.md`.\n- **Tony\'s rulings in the build session, 2026-10-13** (his words in this\n  session\'s chat; the handoff quotes each):\n  - "Test" comes off the checker labels (ruling 5 of 2026-10-12, before\n    the session).\n  - Where the paragraph goes: option B, "+ more" opens it inside the\n    card ("B. Confirmed."), after seeing both at desktop and 9:16 width.\n  - The website checks group gets six headings, in his order: tools you\n    run by hand, the module atlas, JPL\'s check, the served cache, from\n    the orrery, the rooms. His logic: "manual use first tools, then\n    generated reports, then checks in pipeline order: jpl checks, then\n    served data, then gallery renders." Headings fold, keeping the\n    indentation ("i would also make these groups collapsible but keeping\n    the indentation method"); all start open.\n  - The "when" index: "record for later." If built, it is generated from\n    a tag on each entry, never hand-written.\n  - Only Paloma\'s Orrery changes how it launches: its own console\n    window, as the maintenance run has ("what i wanted was for the\n    orrery to also open a console window instead of just the dashboard\n    status"). Every other button stays as it was.\n- **Built:** `patch_L440_1_dashboard_labels_20261013.py`, on orrery\n  db63721d. Each card shows its name, its repository and script in small\n  type, and one line of at most twelve words from CARD_LINES; the\n  paragraph opens under "+ more". Text wraps to the window\'s width, so\n  the Launch button stays on the card in a narrow window. Buttons under a\n  runner take the name the run prints; the orrery\'s generators and\n  checkers re-sorted alphabetically under the new names. New checker\n  `test_dashboard_parity.py`, the run\'s "Dashboard parity" row and the\n  "Dashboard Parity" button: every step of both runs and the Daily Run\n  against the buttons, by name and script, both directions; every\n  script on disk; every card\'s short line; nine planted faults, each\n  caught by its own kind of finding. %(gating)d gating checkers.\n- **Not renamed, recorded:** the run rows themselves keep their names\n  (the printed script line now tells the modes of one script apart),\n  and the standalone tools outside the runs keep theirs.\n**Gap:** Tony\'s look at the dashboard (the handoff, section 6). Later\nslice, recorded: the "when" index, from per-entry tags.\n**Ref:** `documentation/HANDOFF_L440_dashboard_labels_20261013.md`;\n`palomas_orrery_dashboard.py`; `test_dashboard_parity.py`;\nL-324 (its parity row, now built); L-416; L-341; L-281.\n\n'

HANDOFF_TEXT = '<!-- Doc-Kind: hand | Session record for L-440: the dashboard\'s cards, the website checks\' six headings, the run names on the buttons, the orrery\'s console window, and the Dashboard parity check. -->\n# L-440: the dashboard\'s labels, short lines and headings\n\nBuilt on orrery db63721d258004b855c1259371d8adf15bf7647c at\nhttps://github.com/tonylquintanilla/palomas_orrery ("L437 close"). The\ngallery was read at 924977a353b6c3e7d50e360e840fe176685f97c9 at\nhttps://github.com/tonylquintanilla/tonyquintanilla.github.io and is not\ntouched. Pushed at: Tony\'s commit after running the patch; the next\nsession reads it with `git ls-remote`.\nTony\'s local folders: orrery\n`C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\`;\ngallery `C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\`.\nWritten October 13, 2026 with Anthropic\'s Claude Opus 5.5.\n\n- Type: BUILD (design and build in one session).\n- Brief: `documentation/HANDOFF_dashboard_labels_brief_20261012.md`, with\n  `documentation/AUDIT_dashboard_labels_20261012.md`. Coordination:\n  `documentation/HANDOFF_scaffolding_sessions_coordination_20261013.md`.\n- Patch: `patch_L440_1_dashboard_labels_20261013.py` (one, the orrery).\n- Skills loaded and matched against the manifest: safe-file-editing 1.13,\n  agentic-pre-test 1.3, ledger-and-session-records 1.20,\n  orrery-coding-conventions 1.10. No skill or protocol version changes.\n\n## 1. What Tony asked, and what he ruled\n\nHis request of 2026-10-12: labels you can recognize from the script,\npithy descriptions, and a way to find a tool besides the search.\n\nHis rulings in this session, 2026-10-13, in his words:\n\n- Where the paragraph goes: option B, "+ more" opens it inside the card.\n  "B. Confirmed." He saw both options rendered at desktop width and at a\n  9:16 width first ("Can you show me the cards in 9:16 view like a\n  phone?"), and noted "this is only a desktop App!"\n- The website checks group: six headings, in his order. "i would order\n  them: 4, 5, 3, 1, 2. the logic is manual use first tools, then\n  generated reports, then checks in pipeline order: jpl checks, then\n  served data, then gallery renders." And: "i would also make these\n  groups collapsible but keeping the indentation method." The split of\n  JPL\'s check from the served cache: "confirmed as recommended."\n- The "when" index: "record for later."\n- The console window, from his note read with the brief, then narrowed:\n  "the way it works now is okay ... what i wanted was for the orrery to\n  also open a console window instead of just the dashboard status." Only\n  Paloma\'s Orrery moved; every other button runs as it did.\n- Already ruled before the session: "Test" comes off the checker labels\n  (ruling 5, `DESIGN_rulings_20261012.md`), and a button is named what\n  the run prints (the same record).\n\n## 2. What the patch does\n\n- **Every card**: its name; the repository and script it runs, in small\n  type (the same text the Launch button\'s tooltip shows); one short line\n  of at most twelve words from CARD_LINES; "+ more" opens the full\n  paragraph in place and "- less" closes it. Text wraps to the window\'s\n  width, and the Launch button is packed first. Before, the paragraph\n  wrapped at a fixed 600 pixels, which in a narrow window pushed every\n  Launch button off the card (seen in the 9:16 render).\n- **Headings fold.** A heading inside a group is a button: "-" open, "+"\n  folded. Every heading starts open at launch, so what a runner runs\n  stays visible (Tony\'s ruling of 2026-08-12). Folding is not remembered.\n  A search keeps the heading above each match.\n- **The website checks group** has six headings, cards alphabetical\n  under each: TOOLS YOU RUN BY HAND (Daily Run Steps, Guest Book Checks,\n  Store Editor Suite, Store Writer Suite); THE MODULE ATLAS (Module\n  Atlas); JPL\'S CHECK OF THE OBJECTS (Horizons Check Suite, Horizons\n  Confirmations); THE SERVED CACHE (Artifact 1 Assembler, Cache Builder\n  Suite, Cache In Step, Cache Siblings); FROM THE ORRERY (Config Mirror --\n  report only, Config Mirror Check, Constants Export Pull, Drawings,\n  Drawings Pull, Mirror Suite, Objects Export Pull, Objects Mirror Check,\n  Objects Mirror Suite, Pointer Join, Pole of Date); THE ROOMS (Arrival,\n  Collapsed Features, Display Figures, Earth Scene Geometry, Feature\n  Renderers, Hover Budget, Page Framing, Solar System Drawer, Solar\n  System Figures, Sun Shells). The two runners stay at top and bottom.\n- **Buttons renamed to the run\'s names** (29): in the orrery group, Ledger\n  Index, Skill Manifest, Module Atlas, Constants Change, Constants\n  Relations, Derived Figures, Constants Export Check, Objects Export\n  Check, Skill Headers, Exact Rows by the Count, Dimensions, Cross-Check\n  Annotations, Citation Inheritance, Status Lines, Row Shape, Scanner\n  Recognition 1d/1e, Scanner Row Run, Reset Completeness, Orbit Cache,\n  Earth Pole of Date, Hills Cloud Sampler, Drawings Export Check,\n  Position Digits, Worksheet Checker Tests; in the website group, Cache\n  Builder Suite, Drawings, Artifact 1 Assembler, Module Atlas; in the\n  Daily Run, Cache Builder. The orrery\'s generators and checkers are\n  re-sorted alphabetically under the new names (the 2026-09-12 rule).\n  Five descriptions that named an old label now name the new one.\n- **The run rows keep their names.** The brief allowed renaming poorly\n  named rows in both places. With the script now printed on each card,\n  the modes of one script read apart on their own ("exact_rows_report.py\n  --check"), so no row was renamed and the website repository is not\n  touched. Standalone tools outside the runs keep their labels too.\n- **Paloma\'s Orrery** opens its own console window, kept open after the\n  program closes, as the maintenance run\'s button does. On macOS and\n  Linux no new window opens; the output goes to the terminal the\n  dashboard was started from.\n- **Dashboard parity**, new: `test_dashboard_parity.py`, the run\'s\n  "Dashboard parity" row and the "Dashboard Parity" button. It reads both\n  runners, the Daily Run and the dashboard, edits nothing, and fails on:\n  a step with no button of its name; a button running a different script\n  or arguments; an indented button naming no step; a script not on disk;\n  a card with no short line, one over twelve words, or a line for no\n  card; a file it cannot read. Four steps are covered by a differently\n  named button on purpose and printed on every run: Config mirror and\n  Objects mirror (their buttons run the report-only form; the run does\n  the writing) and the two guest book checks (one button, L-281). Not\n  compared: the website\'s three live checks, which are functions inside\n  the live run.\n- The maintenance run\'s GATING AND REPORT-ONLY paragraph is left as it\n  is: since L-269 it names no count, and the run counts its rows itself.\n\n## 3. The short lines, and how they were checked\n\nEach of the 107 lines was written from its script\'s own module\ndocstring, read at db63721d by a script that printed every button\'s\ndescription beside the first lines of its script\'s docstring, not from\nthe dashboard\'s paragraph alone. Where the docstring and the paragraph\ndiffered in emphasis the docstring won (Add Module Docstrings: its\ndefault mode is the Role/Domain tag sweep). Dashboard parity holds the\ntwelve-word limit; on its first run it caught two of these lines at\nthirteen words, which were shortened before delivery.\n\n## 4. Verified, and how\n\n- The patch on a throwaway copy of both repositories at db63721d / 924977a3:\n  every edit "ok"; a second run refuses and writes nothing.\n- Every one of the 106 existing entries survives with the same fields;\n  only its label (the 29 renames), five description words, and the\n  orrery\'s console flag change; one entry is added. Proved by loading the\n  old and new LAUNCH_GROUPS side by side.\n- `test_dashboard_parity.py` on the patched copy: 9 of 9 planted faults\n  caught, each by its own kind of finding; 77 steps (39 orrery, 34\n  website, 4 Daily Run) matched by name and script; 107 cards with a line.\n- The dashboard under xvfb, on the copy: 107 Launch buttons, 0 Not\n  Found; 107 "+ more"; eight headings, all open at launch; folding and\n  reopening work; "+ more" opens and "- less" closes; a search for\n  "parity" finds 1 under CHECKERS and one for "jpl" 11 under their own\n  headings; Clear brings all 107 back; at 560 pixels wide all 107 Launch\n  buttons stay inside the window.\n- py_compile on the dashboard, the runner and the new checker; all files\n  ASCII and LF.\n- Not run here: the whole orrery maintenance run (the sandbox lacks the\n  orrery\'s scientific libraries). Your run is the check of the other 26\n  rows.\n\n## 5. Other sessions\' work this session met\n\n- The handle. This work was first delivered as patch_L438_1 on\n  082dbb15, under L-438, then the next free number in the ledger. A\n  brief pushed the same day, `HANDOFF_L438_objects_to_website_brief_20261013.md`,\n  claims L-438, and the master plan restamp brief names L-439, so this\n  work is L-440. patch_L438_1 never ran; Tony deletes it from\n  documentation/. This patch replaces it, rebuilt on db63721d.\n- L-269\'s replacement (patch_L269_5, run before this one) added the\n  Maintenance Report button and row; its card gets its short line\n  here, and the run\'s GATING AND REPORT-ONLY paragraph, which no\n  longer names a number, is left as it is.\n- L-437 ran before this patch and added Domain Split; its button gets its\n  short line here, and its row is in the parity count.\n- How a later patch adds a button now: the entry in LAUNCH_GROUPS, its\n  line in CARD_LINES, keyed by the same group and label, and, under a\n  runner, the run\'s own name. In the website group, under a heading.\n\n## 6. Your look\n\n- Open `palomas_orrery_dashboard.py` with Run.\n- Each card: the name, the script in small grey type under it, one short\n  line, and "+ more" beside the name. Click "+ more" on any card: the\n  paragraph opens under the line and the link reads "- less".\n- Scroll to Gallery -- checks and data: six headings, each starting with\n  "-". Click one: its cards fold away and it starts with "+".\n- Maintenance Run: GENERATORS and CHECKERS fold the same way; the\n  checkers read without "Test" and run in alphabetical order.\n- Type "jpl" in Find a tool and press Enter: the matches show under\n  their headings.\n- Make the window narrow: the Launch buttons stay on the cards.\n- Launch Paloma\'s Orrery: a console window opens beside it and carries\n  its printed output.\n- Your verdicts, in your run record, one per line: the card; "+ more";\n  the six headings and their order; folding; the console window.\n\n## 7. Tony-actions\n\n- (do) Delete `documentation/patch_L438_1_dashboard_labels_20261013.py`\n  (never run; replaced by this patch).\n- (do) Save `patch_L440_1_dashboard_labels_20261013.py` in the orrery\n  folder and Run it; paste the output into your run record.\n- (do) Run `orrery_maintenance_run.py`: every gating checker passes,\n  Dashboard parity among them with 9 of 9 planted faults caught.\n- (do) The look, section 6.\n- (decide) The look.\n- (do) Move the patch into `documentation/`; commit and push.\n- (decide, recorded for later) The "when" index, generated from tags.\n\nSession record written October 2026 with Anthropic\'s Claude Opus 5.5.\n'

# ---------------------------------------------------------------------------
# DATA: the renames, the website group's headings, and the short lines.
# ---------------------------------------------------------------------------

# Old label -> new label, per group. A button under a runner takes the name
# that run prints (Tony's ruling of 2026-10-12, DESIGN_rulings_20261012.md,
# ruling 5 for "Test"). Every old label here must be found exactly once in
# its group, or the patch refuses.
RENAMES = {
    "Daily Run": {
        "Gallery Cache Builder -- Manual Run": "Cache Builder",
    },
    "Gallery -- checks and data": {
        "Gallery Builder Offline Tests": "Cache Builder Suite",
        "Drawings Check": "Drawings",
        "Artifact 1 Assembler Pin": "Artifact 1 Assembler",
        "Gallery Module Atlas": "Module Atlas",
    },
    "Maintenance Run": {
        "Update Ledger Index": "Ledger Index",
        "Update Skill Manifest": "Skill Manifest",
        "Regenerate Module Atlas": "Module Atlas",
        "Constants Change Report": "Constants Change",
        "Test Constants Provenance": "Constants Relations",
        "Test Derived Figures": "Derived Figures",
        "Test Constants Export": "Constants Export Check",
        "Test Objects Export": "Objects Export Check",
        "Test Skill Headers": "Skill Headers",
        "Test Exact Rows By The Count": "Exact Rows by the Count",
        "Test Dimensions": "Dimensions",
        "Test Cross-Check Annotations": "Cross-Check Annotations",
        "Test Citation Inheritance": "Citation Inheritance",
        "Test Status Lines": "Status Lines",
        "Test Row Shape": "Row Shape",
        "Test Scanner Recognition": "Scanner Recognition 1d/1e",
        "Test Scanner Row Run": "Scanner Row Run",
        "Test Reset Completeness": "Reset Completeness",
        "Test Orbit Cache": "Orbit Cache",
        "Test Earth Pole of Date": "Earth Pole of Date",
        "Test Hills Cloud Sampler": "Hills Cloud Sampler",
        "Test Drawings Export": "Drawings Export Check",
        "Test Position Digits": "Position Digits",
        "Test Worksheet Checker": "Worksheet Checker Tests",
    },
}

# Text inside a description that names a renamed button: (group, NEW label
# of the card whose description it is, old text, new text). Each must match
# exactly once in that card's source. The Correction Does Not Travel.
DESC_FIXES = [
    ("Daily Run", "Daily Run -- everything indented below",
     '"the website\'s objects that are due (L-395). Then the Gallery "\n'
     '         "Cache Builder, with',
     '"the website\'s objects that are due (L-395). Then the Cache "\n'
     '         "Builder, with'),
    ("Maintenance Run", "Exact Rows Report",
     "Test Exact Rows By The Count is the same check",
     "Exact Rows by the Count is the same check"),
    ("Maintenance Run", "Row Shape",
     "Same script as Test Status Lines, run",
     "Same script as Status Lines, run"),
    ("Maintenance Run", "Status Lines",
     "Test Row Shape ",
     "Row Shape "),
    ("Maintenance Run", "Skill Headers",
     '(L-407). The Update "\n         "Skill Manifest button',
     '(L-407). The Skill "\n         "Manifest button'),
]

# The website checks group, in Tony's order of 2026-10-13 (L-440): manual
# tools first, then the generated report, then the checks in pipeline
# order -- JPL, served data, the rooms. Cards alphabetical under each.
GALLERY_GROUP = "Gallery -- checks and data"
GALLERY_TOP = "Gallery Maintenance Run -- offline"
GALLERY_BOTTOM = "Gallery Maintenance Run -- live, AFTER a push"
GALLERY_SECTIONS = [
    ("TOOLS YOU RUN BY HAND -- each tests a tool you use yourself",
     ["Daily Run Steps", "Guest Book Checks", "Store Editor Suite",
      "Store Writer Suite"]),
    ("THE MODULE ATLAS -- the website's map of its own modules",
     ["Module Atlas"]),
    ("JPL'S CHECK OF THE OBJECTS",
     ["Horizons Check Suite", "Horizons Confirmations"]),
    ("THE SERVED CACHE -- what the website serves, and its builder",
     ["Artifact 1 Assembler", "Cache Builder Suite", "Cache In Step",
      "Cache Siblings"]),
    ("FROM THE ORRERY -- its numbers, drawings and pole",
     ["Config Mirror -- report only", "Config Mirror Check",
      "Constants Export Pull", "Drawings", "Drawings Pull", "Mirror Suite",
      "Objects Export Pull", "Objects Mirror Check", "Objects Mirror Suite",
      "Pointer Join", "Pole of Date"]),
    ("THE ROOMS -- as the page draws them",
     ["Arrival", "Collapsed Features", "Display Figures",
      "Earth Scene Geometry", "Feature Renderers", "Hover Budget",
      "Page Framing", "Solar System Drawer", "Solar System Figures",
      "Sun Shells"]),
]

# The orrery's own button that now opens its own console (Tony, 2026-10-13).
CONSOLE_GROUP = "Solar System"
CONSOLE_LABEL = "Paloma's Orrery"

# The new button for the new checker, placed in CHECKERS alphabetically.
PARITY_ENTRY = '''        ("Dashboard Parity",
         "test_dashboard_parity.py",
         "Check that every row of the orrery's maintenance run, the website's "
         "offline maintenance run and the Daily Run has a button here with "
         "the same name and the same script, that every indented button "
         "names a row, that every button's script is on disk, and that every "
         "card carries its short line of twelve words or fewer. It reads "
         "both repositories and edits neither. Nine faults are planted "
         "first, each caught by name. Ends on \\"DASHBOARD PARITY: PASS\\" "
         "(L-440).",
         SCRIPT_DIR,
         True,
         None,
         True)'''

# One line per card, at most twelve words, written from each script's own
# docstring at db63721d (L-440). Keyed (group, label). The order here is
# the order they are written into the file, group by group.
CARD_LINES = [
    ("Solar System", "Paloma's Orrery",
     "The 3D solar system: planets, comets, asteroids and spacecraft, by date."),
    ("Solar System", "Orbital Construction",
     "Shows step by step how six orbital elements build an orbit."),
    ("Earth System", "Earth System Viewer",
     "A hub window of climate data plots and planetary boundaries."),
    ("Earth System", "Google Earth Controller",
     "Pick and open the climate KMZ layers in Google Earth Pro."),
    ("Earth System", "Earth System Generator",
     "Builds the climate layers: a Plotly preview and a Google Earth KMZ."),
    ("Earth System", "Food Insecurity Generator",
     "Builds Sudan's IPC food-insecurity layer for Google Earth from IPC data."),
    ("Earth System", "Food Insecurity Controller",
     "The Google Earth controller, opened with the food-insecurity layers loaded."),
    ("Stars", "Star Visualization",
     "HR diagrams, 3D stellar neighborhoods and planetarium views of nearby stars."),
    ("Daily Run", "Daily Run -- everything indented below",
     "The website's daily routine: guest book, JPL check, cache build, checks."),
    ("Daily Run", "Guest Book Updater",
     "Approve, decline or defer each new guest book message; write entries."),
    ("Daily Run", "Horizons Check",
     "Asks JPL whether each object the website serves is still that object."),
    ("Daily Run", "Cache Builder",
     "Fetches from JPL, checks, and swaps in the website's new served cache."),
    ("Daily Run", "Gallery Maintenance Run -- offline",
     "Every website check that needs no network; run before you commit."),
    ("Gallery -- checks and data", "Gallery Maintenance Run -- offline",
     "Every website generator and check that needs no network, in one run."),
    ("Gallery -- checks and data", "Daily Run Steps",
     "Fails if any script the Daily Run calls is missing."),
    ("Gallery -- checks and data", "Guest Book Checks",
     "Both guest book checks: the page's drawing of it and its updater."),
    ("Gallery -- checks and data", "Store Editor Suite",
     "Checks the room-words editor's logic without opening its window."),
    ("Gallery -- checks and data", "Store Writer Suite",
     "Checks the words writer changes only the line asked, refuses the rest."),
    ("Gallery -- checks and data", "Module Atlas",
     "Regenerates the website repo's own module atlas and index."),
    ("Gallery -- checks and data", "Horizons Check Suite",
     "The Horizons check on JPL's recorded answers, planted mistakes caught."),
    ("Gallery -- checks and data", "Horizons Confirmations",
     "Fails on any served object JPL has not confirmed within 30 days."),
    ("Gallery -- checks and data", "Artifact 1 Assembler",
     "Compares the Artifact 1 assembler test's verdicts with their recorded pin."),
    ("Gallery -- checks and data", "Cache Builder Suite",
     "The cache builder's offline tests, JPL mocked: build, swap, roll back."),
    ("Gallery -- checks and data", "Cache In Step",
     "Checks the served cache holds what data/objects_config.json says."),
    ("Gallery -- checks and data", "Cache Siblings",
     "Reports leftover staging and quarantine folders beside the served cache."),
    ("Gallery -- checks and data", "Config Mirror -- report only",
     "Lists what the mirror would write into the config; writes nothing."),
    ("Gallery -- checks and data", "Config Mirror Check",
     "Checks every served number in the config matches the orrery's export."),
    ("Gallery -- checks and data", "Constants Export Pull",
     "Copies the orrery's constants export into the website, noting its commit."),
    ("Gallery -- checks and data", "Drawings",
     "Checks each stored drawing is pulled, served, and tilted as recorded."),
    ("Gallery -- checks and data", "Drawings Pull",
     "Copies the orrery's stored drawings, the Hills cloud's dots, into the website."),
    ("Gallery -- checks and data", "Mirror Suite",
     "Checks the constants mirror's writes and refusals on made-up files."),
    ("Gallery -- checks and data", "Objects Export Pull",
     "Copies the orrery's objects export (names, JPL ids, links) into the website."),
    ("Gallery -- checks and data", "Objects Mirror Check",
     "Lists every object field in the config that differs from the export."),
    ("Gallery -- checks and data", "Objects Mirror Suite",
     "Checks the objects mirror's writes and refusals on made-up files."),
    ("Gallery -- checks and data", "Pointer Join",
     "Sorts the config's links into the orrery's store: served, waiting, outside."),
    ("Gallery -- checks and data", "Pole of Date",
     "Checks the website's copy of Earth's tilt geometry against the orrery's."),
    ("Gallery -- checks and data", "Arrival",
     "Checks the Sun and Earth rooms open on the right things."),
    ("Gallery -- checks and data", "Collapsed Features",
     "Sorts every served feature group; fails on one it cannot classify."),
    ("Gallery -- checks and data", "Display Figures",
     "Checks every number in an Earth hover shows only the figures earned."),
    ("Gallery -- checks and data", "Earth Scene Geometry",
     "Checks the Earth room's tilt, rings, terminator and Moon on recorded data."),
    ("Gallery -- checks and data", "Feature Renderers",
     "Checks the code that draws every shell, ring, belt and magnetosphere."),
    ("Gallery -- checks and data", "Hover Budget",
     "Counts the lines in every room hover and names the ten longest."),
    ("Gallery -- checks and data", "Page Framing",
     "Checks the page's framing helpers give the right axis ranges."),
    ("Gallery -- checks and data", "Solar System Drawer",
     "Checks the Solar System room's drawer does what your design says."),
    ("Gallery -- checks and data", "Solar System Figures",
     "Checks the Solar System room prints distances only to earned digits."),
    ("Gallery -- checks and data", "Sun Shells",
     "Checks the Sun room's shells are built and shaped as configured."),
    ("Gallery -- checks and data", "Gallery Maintenance Run -- live, AFTER a push",
     "After a push: checks what palomasorrery.com actually serves."),
    ("Gallery -- authoring", "Exhibit Store Editor",
     "A window to edit the words visitors read in each room."),
    ("Gallery -- authoring", "Gallery Cleanup",
     "Finds gallery files no card uses, and deletes them after you confirm."),
    ("Gallery -- authoring", "Gallery Editor",
     "Arrange the gallery's rooms and cards, and edit their details."),
    ("Gallery -- authoring", "Gallery JSON Fixer",
     "Updates older gallery JSON files so the current viewer reads them."),
    ("Gallery -- authoring", "Gallery Studio",
     "Curate an orrery Plotly plot and export it for the gallery."),
    ("Gallery -- authoring", "Inspect Staging",
     "A plain-language report on a dry-run cache build; changes nothing."),
    ("Gallery -- authoring", "JSON Converter",
     "Converts saved orrery HTML plots into lightweight gallery JSON files."),
    ("Gallery -- authoring", "Serve Gallery Locally",
     "Serves the website at localhost:8000 and opens the assembler dev page."),
    ("Maintenance Run", "MAINTENANCE RUN -- everything indented below",
     "Every orrery generator, then every check, with one summary at the end."),
    ("Maintenance Run", "Constants Export",
     "Writes the constants export the website reads, from constants_new.py."),
    ("Maintenance Run", "Data Inventory",
     "Lists the large local data stores in DATA_INVENTORY.md."),
    ("Maintenance Run", "Document Index",
     "Regenerates README.md's table of key documents from their own tags."),
    ("Maintenance Run", "Drawings Export",
     "Writes the Hills cloud's dots to data/drawings/ for the website."),
    ("Maintenance Run", "Exact Rows Report",
     "Lists every place an exact row of constants_new.py is printed."),
    ("Maintenance Run", "Ledger Index",
     "Regenerates the ledger's index from its detail blocks."),
    ("Maintenance Run", "Module Atlas",
     "Regenerates MODULE_ATLAS.md and MODULE_INDEX.md from each module's docstring."),
    ("Maintenance Run", "Objects Export",
     "Writes the objects export the website reads, from celestial_objects.py."),
    ("Maintenance Run", "Skill Manifest",
     "Regenerates the protocol's skill table from skills/*/SKILL.md."),
    ("Maintenance Run", "Builder Marker Join",
     "Checks the worksheet request builder joins a continued citation line."),
    ("Maintenance Run", "Citation Inheritance",
     "Checks the scanner's rule that a block's citation covers its strings."),
    ("Maintenance Run", "Constants Change",
     "Reports what moved in constants_new.py, and whether its source moved too."),
    ("Maintenance Run", "Constants Export Check",
     "Checks the constants export matches constants_new.py, row by row."),
    ("Maintenance Run", "Constants Relations",
     "Checks how constants relate: derivations, orderings, completeness."),
    ("Maintenance Run", "Cross-Check Annotations",
     "Checks the grammar and scoring of cross-check annotations."),
    ("Maintenance Run", "Dashboard Parity",
     "Checks run steps against buttons by name, and every card's short line."),
    ("Maintenance Run", "Derived Figures",
     "Checks a derived constant claims no more figures than its inputs."),
    ("Maintenance Run", "Dimensions",
     "Checks each derived constant's unit follows from its arithmetic."),
    ("Maintenance Run", "Domain Split",
     "Checks the scanner's Tier-1 total prints with its split by domain."),
    ("Maintenance Run", "Drawings Export Check",
     "Checks each stored drawing is exactly what its rows give today."),
    ("Maintenance Run", "Earth Pole of Date",
     "Checks Earth's tilt of date offline, against ERFA, with its fallback."),
    ("Maintenance Run", "Exact Rows by the Count",
     "Fails where a printed exact row gives no print count."),
    ("Maintenance Run", "Extractor Pins",
     "Checks the citation filter still keeps and drops the same numbers."),
    ("Maintenance Run", "Hills Cloud Sampler",
     "Checks the Hills cloud's frame, Fig. 3 reading and tilt, faults planted."),
    ("Maintenance Run", "Maintenance Report",
     "Checks the run's summary names each file whose Tier-1 count rose."),
    ("Maintenance Run", "Objects Export Check",
     "Checks the objects export matches celestial_objects.py, entry by entry."),
    ("Maintenance Run", "Orbit Cache",
     "Tests orbit cache loading, saving, conversion and repair."),
    ("Maintenance Run", "Orbit Markers",
     "Checks each orbit's centre, its marker dates, and its hover digits."),
    ("Maintenance Run", "Position Digits",
     "Checks the body hover prints only the digits JPL's errors earn."),
    ("Maintenance Run", "Provenance Scanner",
     "Scans for numbers that need a source; writes PROVENANCE_AUDIT.md."),
    ("Maintenance Run", "Reset Completeness",
     "Checks the orrery's Reset button returns every control to its default."),
    ("Maintenance Run", "Row Shape",
     "Checks each constants_new.py value fits on its assignment's own line."),
    ("Maintenance Run", "Scanner Recognition 1d/1e",
     "Checks the scanner accepts a real citation and refuses a fake one."),
    ("Maintenance Run", "Scanner Row Run",
     "Checks the scanner reads each row's citation from its own comments."),
    ("Maintenance Run", "Skill Headers",
     "Checks every skill header reads the way the Settings uploader reads it."),
    ("Maintenance Run", "Status Lines",
     "Checks the Status line grammar on every constants_new.py row."),
    ("Maintenance Run", "Worksheet Checker",
     "Reports whether each worksheet records what its cross-check annotation claims."),
    ("Maintenance Run", "Worksheet Checker Tests",
     "Checks each layer of the worksheet checker can actually fail."),
    ("Maintenance Run", "Worksheet Key Round Trip",
     "Checks every annotated site's key resolves back to that site."),
    ("Tools and Caches", "Add Module Docstrings",
     "Adds the Role and Domain tags to module docstrings; touches no code."),
    ("Tools and Caches", "Animation HTML Tool",
     "Measures a saved animation's traces, frames and payload size."),
    ("Tools and Caches", "Climate Cache Manager",
     "Updates the climate data caches safely, with validation and rollback."),
    ("Tools and Caches", "Create Ephemeris Database",
     "Rebuilds satellite_ephemerides.json from idealized_orbits.py and Horizons files."),
    ("Tools and Caches", "Dependency Trace",
     "Shows which modules a module uses, and which use it."),
    ("Tools and Caches", "Earth Pole Live Check",
     "Asks Horizons for Earth's pole on five dates and checks the tilt."),
    ("Tools and Caches", "Export Orbit Cache",
     "Writes web-servable orbit files from the local orbit caches."),
    ("Tools and Caches", "Osculating Cache Manager",
     "Loads and reports on the osculating orbital elements cache."),
    ("Tools and Caches", "SIMBAD Query Manager",
     "Tests SIMBAD queries on a few stars, with rate limits and retries."),
    ("Tools and Caches", "Verify Orbit Cache",
     "Backs up, validates and repairs orbit_paths.json."),
    ("Tools and Caches", "VOT Cache Manager",
     "Checks the VizieR VOT cache files are intact."),
    ("Tools and Caches", "Worksheet Request Builder",
     "Writes the cross-check request sent out to another model."),
]


# ---------------------------------------------------------------------------
# THE DASHBOARD TRANSFORM
# ---------------------------------------------------------------------------

class PatchError(Exception):
    """A check failed. Nothing is written."""


def _q(text):
    """A Python double-quoted literal for an ASCII label."""
    return '"%s"' % text.replace('\\', '\\\\').replace('"', '\\"')


def _offsets(text):
    """Character offset of the start of each line (1-based line numbers)."""
    starts = [0, 0]
    for i, ch in enumerate(text):
        if ch == '\n':
            starts.append(i + 1)
    return starts


def _span(node, starts):
    return (starts[node.lineno] + node.col_offset,
            starts[node.end_lineno] + node.end_col_offset)


def _launch_groups(text):
    """(dict node, [(group, list node)]) for LAUNCH_GROUPS, read by ast."""
    tree = ast.parse(text)
    for node in tree.body:
        if (isinstance(node, ast.Assign) and len(node.targets) == 1
                and getattr(node.targets[0], 'id', None) == 'LAUNCH_GROUPS'):
            groups = []
            for key, value in zip(node.value.keys, node.value.values):
                if not (isinstance(key, ast.Constant)
                        and isinstance(value, ast.List)):
                    raise PatchError('LAUNCH_GROUPS has a group this patch '
                                     'cannot read')
                groups.append((key.value, value))
            return node, groups
    raise PatchError('LAUNCH_GROUPS not found in %s' % DASHBOARD)


def _label(elt):
    if isinstance(elt, ast.Constant) and isinstance(elt.value, str):
        return None
    if (isinstance(elt, ast.Tuple) and elt.elts
            and isinstance(elt.elts[0], ast.Constant)
            and isinstance(elt.elts[0].value, str)):
        return elt.elts[0].value
    raise PatchError('an entry in LAUNCH_GROUPS is neither a heading nor '
                     'a tuple whose first item is its label')


def _indented(elt):
    return (isinstance(elt, ast.Tuple) and len(elt.elts) > 6
            and isinstance(elt.elts[6], ast.Constant)
            and elt.elts[6].value is True)


def _element_text(text, starts, group, elt, report):
    """An entry's source, with this patch's rename and fixes applied."""
    a, b = _span(elt, starts)
    seg = text[a:b]
    old = _label(elt)
    if old is None:
        return seg, None
    new = RENAMES.get(group, {}).get(old, old)
    if new != old:
        la, lb = _span(elt.elts[0], starts)
        seg = seg[:la - a] + _q(new) + seg[lb - a:]
        report.append('renamed  %-28s %s -> %s' % (group[:28], old, new))
    for g, label, before, after in DESC_FIXES:
        if g == group and label == new:
            n = seg.count(before)
            if n != 1:
                raise PatchError('the description of "%s" (%s) should name a '
                                 'renamed button once; found %d' % (new, g, n))
            seg = seg.replace(before, after)
            report.append('wording  %-28s %s: names the new label'
                          % (group[:28], new))
    if group == CONSOLE_GROUP and new == CONSOLE_LABEL:
        if len(elt.elts) != 3:
            raise PatchError('"%s" was expected to have three fields; it has '
                             '%d' % (CONSOLE_LABEL, len(elt.elts)))
        seg = seg[:-1] + ',\n         SCRIPT_DIR,\n         True)'
        report.append('console  %-28s %s: opens its own console window'
                      % (group[:28], new))
    return seg, new


def _sorted_half(items):
    return sorted(items, key=lambda pair: pair[1].casefold())


def transform_launch_groups(text, report):
    """Rename, re-sort and re-head LAUNCH_GROUPS, by its own structure.

    Works on the source of each entry as it stands, so an entry another
    session added is kept: in the orrery's group it is sorted into its
    half; in the website group it stops the patch, because its heading
    is a judgment this patch cannot make.
    """
    starts = _offsets(text)
    _node, groups = _launch_groups(text)
    seen = dict((g, set()) for g in RENAMES)
    edits = []
    for group, lst in groups:
        if group in ('Maintenance Run', GALLERY_GROUP):
            continue
        for elt in lst.elts:
            label = _label(elt)
            if label is None:
                continue
            if label in RENAMES.get(group, {}):
                seen[group].add(label)
            new_seg, _new = _element_text(text, starts, group, elt, report)
            a, b = _span(elt, starts)
            if new_seg != text[a:b]:
                edits.append((a, b, new_seg))

    for group, lst in groups:
        if group == 'Maintenance Run':
            body = _rebuild_orrery(text, starts, group, lst, report, seen)
        elif group == GALLERY_GROUP:
            body = _rebuild_gallery(text, starts, group, lst, report, seen)
        else:
            continue
        a, b = _span(lst, starts)
        edits.append((a, b, '[\n' + body + '    ]'))

    for group, olds in RENAMES.items():
        missing = sorted(set(olds) - seen.get(group, set()))
        if missing:
            raise PatchError('in group "%s", these buttons were not found '
                             'under the names this patch renames: %s'
                             % (group, ', '.join(missing)))
    for a, b, new in sorted(edits, reverse=True):
        text = text[:a] + new + text[b:]
    return text


def _rebuild_orrery(text, starts, group, lst, report, seen):
    """Runner, GENERATORS heading, generators, CHECKERS heading, checkers."""
    elts = lst.elts
    heads = [i for i, e in enumerate(elts) if _label(e) is None]
    if len(heads) != 2 or heads[0] != 1:
        raise PatchError('the Maintenance Run group should be: runner, '
                         'GENERATORS heading, generators, CHECKERS heading, '
                         'checkers; it is not')
    runner = _element_text(text, starts, group, elts[0], report)[0]
    gen_head = text[slice(*_span(elts[heads[0]], starts))]
    chk_head = text[slice(*_span(elts[heads[1]], starts))]
    gens, chks = [], []
    known = set(RENAMES[group]) | set(RENAMES[group].values())
    for i, elt in enumerate(elts):
        if i == 0 or i in heads:
            continue
        old = _label(elt)
        if old in RENAMES[group]:
            seen[group].add(old)
        seg, new = _element_text(text, starts, group, elt, report)
        if old not in known and new not in KNOWN_UNRENAMED:
            report.append('kept     %-28s %s (another session\'s button, '
                          'sorted into place)' % (group[:28], new))
        (gens if i < heads[1] else chks).append((seg, new))
    if not any(new == 'Dashboard Parity' for _s, new in chks):
        chks.append((PARITY_ENTRY, 'Dashboard Parity'))
        report.append('added    %-28s Dashboard Parity' % group[:28])
    out = '        ' + runner + ',\n'
    out += '        ' + gen_head + ',\n'
    for seg, _new in _sorted_half(gens):
        out += '        ' + seg + ',\n'
    out += '        ' + chk_head + ',\n'
    for seg, _new in _sorted_half(chks):
        out += '        ' + seg + ',\n'
    report.append('sorted   %-28s generators and checkers, alphabetically '
                  'under their new names' % group[:28])
    return out


def _rebuild_gallery(text, starts, group, lst, report, seen):
    """Top runner, Tony's six headings with their cards, bottom runner."""
    by_label = {}
    for elt in lst.elts:
        old = _label(elt)
        if old is None:
            raise PatchError('the website group already has a heading; this '
                             'patch expects none')
        if old in RENAMES[group]:
            seen[group].add(old)
        seg, new = _element_text(text, starts, group, elt, report)
        if new in by_label:
            raise PatchError('two buttons named "%s" in the website group'
                             % new)
        by_label[new] = (seg, _indented(elt))
    placed = [GALLERY_TOP, GALLERY_BOTTOM]
    for _head, labels in GALLERY_SECTIONS:
        placed.extend(labels)
    extra = sorted(set(by_label) - set(placed))
    if extra:
        raise PatchError('the website group holds buttons this patch has no '
                         'heading for: %s. Its session must say where they '
                         'go.' % ', '.join(extra))
    absent = [label for label in placed if label not in by_label]
    if absent:
        raise PatchError('the website group lacks buttons this patch places: '
                         '%s' % ', '.join(absent))
    out = '        ' + by_label[GALLERY_TOP][0] + ',\n'
    for head, labels in GALLERY_SECTIONS:
        out += '        ' + _q(head) + ',\n'
        for label in sorted(labels, key=str.casefold):
            seg, indented = by_label[label]
            if not indented:
                raise PatchError('"%s" is not indented, so it cannot sit '
                                 'under a heading' % label)
            out += '        ' + seg + ',\n'
    out += '        ' + by_label[GALLERY_BOTTOM][0] + ',\n'
    report.append('headed   %-28s six headings, cards alphabetical under each'
                  % group[:28])
    return out


# Labels in the orrery group this patch knows and does not rename.
KNOWN_UNRENAMED = set([
    'Constants Export', 'Data Inventory', 'Exact Rows Report',
    'Document Index', 'Drawings Export', 'Objects Export', 'Builder Marker Join',
    'Extractor Pins', 'Provenance Scanner', 'Orbit Markers',
    'Worksheet Checker', 'Worksheet Key Round Trip', 'Domain Split',
    'Dashboard Parity', 'Maintenance Report',
])


def card_lines_source():
    """The CARD_LINES block and its two helpers, as source text."""
    out = [
        '',
        '',
        '# ============================================================',
        '# CARD LINES (L-440)',
        '# ============================================================',
        '# One short line per card, at most twelve words, saying what the',
        '# tool does. The card shows it; the paragraph above opens under',
        '# "+ more" (Tony\'s choice, 2026-10-13). Keyed (group, label), so a',
        '# button added to LAUNCH_GROUPS needs its line added here too.',
        '# Dashboard Parity (test_dashboard_parity.py) fails on a card with',
        '# no line, a line over twelve words, and a line for no card. Each',
        '# line was written from the script\'s own docstring, not from the',
        '# paragraph alone.',
        '',
        'CARD_LINES = {',
    ]
    for group, label, line in CARD_LINES:
        out.append('    (%s,' % _q(group))
        out.append('     %s):' % _q(label))
        out.append('        %s,' % _q(line))
    out.append('}')
    out.append('')
    out.append('')
    out.append('def card_line(group_name, label):')
    out.append('    """The short line for a card, or "" when it has none yet."""')
    out.append('    return CARD_LINES.get((group_name, label), "")')
    out.append('')
    out.append('')
    out.append('def entry_indented(entry):')
    out.append('    """True for a card the runner above it already runs."""')
    out.append('    return (not isinstance(entry, str) and len(entry) > 6')
    out.append('            and bool(entry[6]))')
    out.append('')
    out.append('')
    out.append('def filter_entries(entries, keep):')
    out.append('    """The entries for which keep() is true, with their headings.')
    out.append('')
    out.append('    A heading is kept when a kept card falls under it: its cards')
    out.append('    run to the next heading or to the first card that is not')
    out.append('    indented. So a search shows a match under its own heading,')
    out.append('    and a heading with no match is not drawn (L-440).')
    out.append('    """')
    out.append('    out = []')
    out.append('    pending = None')
    out.append('    for entry in entries:')
    out.append('        if isinstance(entry, str):')
    out.append('            pending = entry')
    out.append('            continue')
    out.append('        if not entry_indented(entry):')
    out.append('            pending = None')
    out.append('        if keep(entry):')
    out.append('            if pending is not None:')
    out.append('                out.append(pending)')
    out.append('                pending = None')
    out.append('            out.append(entry)')
    out.append('    return out')
    return '\n'.join(out) + '\n'


# ---------------------------------------------------------------------------
# THE OTHER EDITS, THE RECORDS, AND THE WRITER
# ---------------------------------------------------------------------------

FONT_OLD = 'FONT_FOOTER = ("Segoe UI", 10)\n'
FONT_NEW = ('FONT_FOOTER = ("Segoe UI", 10)\n'
            'FONT_SCRIPT = ("Consolas", 10)     # the script a card runs (L-440)\n')

TARGETS_OLD = (
    '# Each entry: (display_name, script_filename, description,\n'
    '#              [base_dir], [interactive])\n'
    '# base_dir:    optional, defaults to SCRIPT_DIR\n'
    '# interactive: optional, True = opens in its own console window\n'
    '#              (for scripts that need terminal input)\n')
TARGETS_NEW = (
    '# Each entry: (display_name, script_filename, description,\n'
    '#              [base_dir], [interactive], [args], [indent])\n'
    '# base_dir:    optional, defaults to SCRIPT_DIR\n'
    '# interactive: optional, True = opens in its own console window\n'
    '#              (for scripts that need terminal input, and for the\n'
    '#              orrery, whose printed output shows there; L-440)\n'
    '# args:        optional list of arguments passed to the script\n'
    '# indent:      optional, True = a step the runner above it runs\n'
    '# A bare string is a heading inside its group; it folds the cards\n'
    '# under it. Each card\'s short line is in CARD_LINES, below, keyed by\n'
    '# (group, display_name): add one with every new button. A button\n'
    '# under a runner is named what that run prints (Tony, 2026-10-12).\n'
    '# Dashboard Parity holds both rules on every maintenance run (L-440).\n')

CARDS_ANCHOR = ('\n}\n\n'
                '# ============================================================\n'
                '# LAUNCH TARGET LABELS AND HOVER TEXT\n')

REGION_START = '    def _entry_matches(self, entry, needle):\n'
REGION_END = ('    def _launch(self, script, base_dir=None, interactive=False, '
              'args=None):\n')

DASH_DOC_ANCHOR = '\n"""\n\nimport os\nimport sys\n'
DASH_STAMP = '''
October 13, 2026 with Anthropic's Claude Opus 5.5 (L-440, the dashboard's
labels, descriptions and findability; Tony's request of 2026-10-12). Each
card shows its name, the repository and script it runs in small type, and
one short line of at most twelve words saying what the tool does; the
paragraph opens in place under "+ more" (Tony's choice of 2026-10-13,
option B). The lines are in CARD_LINES, keyed by group and label, each
written from its script's own docstring. Text wraps to the window's width
and the Launch button is packed first, so a narrow window no longer pushes
the button off the card, as the fixed 600-pixel wrap did. A heading inside
a group now folds the cards under it; every heading starts open, so what a
runner runs stays visible (Tony's ruling of 2026-08-12), and a search keeps
a heading that holds a match. The website checks group gains six headings
in Tony's order of 2026-10-13: tools you run by hand, the module atlas,
JPL's check, the served cache, from the orrery, the rooms -- the manual
tools first, then the generated report, then the checks in the order the
data flows. A button under a runner now carries the name that run prints
(Tony's ruling, 2026-10-12, DESIGN_rulings_20261012.md; ruling 5 took
"Test" off), and the orrery's generators and checkers are re-sorted
alphabetically under the new names. Dashboard Parity
(test_dashboard_parity.py), a checker of the orrery's maintenance run,
holds all of it. Paloma's Orrery now opens in its own console window, as
the maintenance run does, so its printed output shows (Tony, 2026-10-13);
on macOS and Linux no new window opens and the output goes to the terminal
the dashboard was started from. Every other button runs as before.
Standing rules, carried here so the next builder reads them in the file:
the Maintenance Run group is GENERATORS then CHECKERS, each alphabetical
(2026-09-12, L-324); the search filters name, short line and paragraph and
draws each match under its own headings (2026-09-19, L-341); every check
keeps its own button, the two guest book checks excepted (L-281); a
runner's card sits directly above its indented group; and nothing written
in a description is cut, only moved behind "+ more".'''

RUN_ROW_ANCHOR = ('    # A fourth field marks a tool REPORT-ONLY: it exits 0 '
                  'whatever it\n')
RUN_ROW = (
    "    # L-440: every step of both maintenance runs and of the Daily Run\n"
    "    # has a dashboard button with the same name and script, and every\n"
    "    # card its short line; nine faults planted first, each caught.\n"
    "    ('Dashboard parity', ['test_dashboard_parity.py'],\n"
    "     'DASHBOARD PARITY:'),\n")
RUN_DOC_ANCHOR = '"""\n\nimport hashlib\n'

NUMBER_WORDS = dict(enumerate(
    ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
     'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
     'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']))
for _tens, _word in ((20, 'twenty'), (30, 'thirty'), (40, 'forty')):
    NUMBER_WORDS[_tens] = _word
    for _unit in range(1, 10):
        NUMBER_WORDS[_tens + _unit] = _word + '-' + NUMBER_WORDS[_unit]
WORD_NUMBERS = dict((w, n) for n, w in NUMBER_WORDS.items())

LEDGER_STAMP_ANCHOR = 'Review and RICE update Tony 6-21-2026\n'
LEDGER_STAMP = (
    "Module updated: October 13, 2026 with Anthropic's Claude Opus 5.5\n"
    "(L-440 opened and built: the dashboard's cards, headings and names,\n"
    "and the Dashboard parity check; L-324's parity row is built), built on\n"
    "%s.\n" % BASE_SHORT)
LEDGER_SECTION_A = ('## A. ACTIVE SEPARATE TRACKS (not orrery-refactor '
                    'backlog; cross-referenced)\n\n')
L324_ANCHOR = ('that they keep agreeing; that parity check is one row of '
               'backlog by\nclass, not built here. [verified @a391262e]\n')
L324_NOTE = (
    "**Note (2026-10-13) -- the parity check is built, by L-440.**\n"
    "`test_dashboard_parity.py`, the maintenance run's \"Dashboard parity\"\n"
    "row, compares every step of both runs and the Daily Run with the\n"
    "dashboard's buttons, by name and script, in both directions.\n")

PAGE = 'documentation/WHERE_WE_ARE.md'
PAGE_MARKER = '--- Your run record below this line'
PAGE_EDITS = [
    ('the box: changed since you last read this',
     "> - Orbital periods, build 2 (the drawn orbits and markers): accepted\n"
     ">   at your look and closed; all four fixes from your plot are in.\n"
     "> - The maintenance run's summary names any file whose count of\n"
     ">   problems to fix now (Tier-1) rose since the last run.\n",
     "> - The dashboard: one short line per card, \"+ more\" opens the rest;\n"
     ">   the website checks under your six headings, which fold; the orrery\n"
     ">   opens its own console. A new check, Dashboard Parity.\n"),
    ('the box: needs you now',
     "> - *Run patch_L269_5 and the maintenance run; delete the old\n"
     ">   patch_L269_1; move the new one and patch_L431_9 into documentation/;\n"
     ">   push.*\n",
     "> - *Run patch_L440_1, then the maintenance run (Dashboard parity\n"
     ">   among the passes); open the dashboard and look; then push.*\n"),
    ('the road: stage 5b',
     "  5b.  [NOW]   The scaffolding checks (L-424, L-425, L-426, the\n"
     "               dashboard) clear beside the slices, not after.\n",
     "  5b.  [NOW]   The scaffolding checks clear beside the slices: the\n"
     "               dashboard (L-440) built; L-424, L-425, L-426 to come.\n"),
    ('settled: the heading',
     "## Settled\n",
     "## Settled  **>> UPDATED THIS SESSION**\n"),
    ('settled: the dashboard line',
     "  boundaries. A dashboard button is named what the run prints. (Oct 12)\n",
     "  boundaries. A dashboard button is named what the run prints. (Oct 12)\n"
     "- The dashboard: a short line per card, the rest under \"+ more\"; the\n"
     "  website checks in your six headings; only the orrery opens a console. (Oct 13)\n"),
    ('details: the dashboard record',
     "- Your six rulings of Oct 12: `DESIGN_rulings_20261012.md`; the briefs for the\n"
     "  dashboard's labels, L-425, L-424 with L-426 (`HANDOFF_..._brief_20261012.md`)\n",
     "- Your six rulings of Oct 12: `DESIGN_rulings_20261012.md`; briefs for L-425,\n"
     "  L-424 with L-426; the dashboard: `HANDOFF_L440_dashboard_labels_20261013.md`\n"),
]
PAGE_CAP = 130


def _exactly_once(text, old, where):
    n = text.count(old)
    if n != 1:
        raise PatchError('ANCHOR FAIL  %s (found %d times, expected 1)'
                         % (where, n))


def _gating_count(text):
    tree = ast.parse(text)
    for node in tree.body:
        if (isinstance(node, ast.Assign)
                and getattr(node.targets[0], 'id', None) == 'CHECKERS'):
            rows = ast.literal_eval(node.value)
            return sum(1 for r in rows if len(r) < 4 or not r[3])
    raise PatchError('CHECKERS not found in orrery_maintenance_run.py')


def edit_dashboard(t, report):
    t = transform_launch_groups(t, report)
    for old, new, where in ((FONT_OLD, FONT_NEW, 'the fonts'),
                            (TARGETS_OLD, TARGETS_NEW,
                             'the LAUNCH TARGETS comment')):
        _exactly_once(t, old, '%s: %s' % (DASHBOARD, where))
        t = t.replace(old, new)
        report.append('edited   %s' % where)
    _exactly_once(t, CARDS_ANCHOR, '%s: the end of LAUNCH_GROUPS' % DASHBOARD)
    t = t.replace(CARDS_ANCHOR, '\n}\n' + card_lines_source() + CARDS_ANCHOR[2:])
    report.append('added    CARD_LINES (%d lines) and its two helpers'
                  % len(CARD_LINES))
    _exactly_once(t, REGION_START, '%s: _entry_matches' % DASHBOARD)
    _exactly_once(t, REGION_END, '%s: _launch' % DASHBOARD)
    a = t.index(REGION_START)
    b = t.index(REGION_END)
    old_region = t[a:b]
    if hashlib.md5(old_region.encode('utf-8')).hexdigest() != REGION_MD5:
        raise PatchError('%s: the drawing code from _entry_matches to _launch '
                         'is not the code this patch was built on (another '
                         'session has changed it)' % DASHBOARD)
    t = t[:a] + NEW_REGION + t[b:]
    report.append('replaced the search and drawing code: folding headings, '
                  'the new card')
    _exactly_once(t, DASH_DOC_ANCHOR, '%s: the docstring end' % DASHBOARD)
    t = t.replace(DASH_DOC_ANCHOR, DASH_STAMP + DASH_DOC_ANCHOR, 1)
    report.append('stamped  the docstring')
    try:
        compile(t, DASHBOARD, 'exec')
    except SyntaxError as exc:
        raise PatchError('%s would not compile: %s' % (DASHBOARD, exc))
    return t


def edit_runner(t, report):
    _exactly_once(t, RUN_ROW_ANCHOR, '%s: the REPORT-ONLY comment' % RUNNER)
    if "'test_dashboard_parity.py'" in t:
        raise PatchError('%s already has the Dashboard parity row' % RUNNER)
    t = t.replace(RUN_ROW_ANCHOR, RUN_ROW + RUN_ROW_ANCHOR)
    report.append('added    the Dashboard parity row to CHECKERS')
    count = _gating_count(t)
    word = NUMBER_WORDS.get(count)
    m1 = re.search(r'\n([A-Z][a-z]+(?:-[a-z]+)?) checkers are pass/fail', t)
    m2 = re.search(r'\ngating ([a-z]+(?:-[a-z]+)?) in its headline', t)
    if m1 and m2 and word:
        was = m1.group(1)
        t = t[:m1.start(1)] + word.capitalize() + t[m1.end(1):]
        m2 = re.search(r'\ngating ([a-z]+(?:-[a-z]+)?) in its headline', t)
        t = t[:m2.start(1)] + word + t[m2.end(1):]
        report.append('restated the gating count: %s -> %s (counted from '
                      'CHECKERS)' % (was, word.capitalize()))
    else:
        report.append('left     the GATING AND REPORT-ONLY paragraph: it '
                      'names no count; the run counts %d' % count)
    _exactly_once(t, RUN_DOC_ANCHOR, '%s: the docstring end' % RUNNER)
    stamp = ("Module updated: October 13, 2026 with Anthropic's Claude Opus "
             "5.5 (L-440:\nCHECKERS gains Dashboard parity, "
             "test_dashboard_parity.py, which holds\nevery step of this run, "
             "the website's offline run and the Daily Run to\na dashboard "
             "button of the same name and script, and every card to its\n"
             "short line, after nine planted faults are each caught. The run "
             "now counts\n%d gating checkers.)\n" % count)
    t = t.replace(RUN_DOC_ANCHOR, stamp + RUN_DOC_ANCHOR, 1)
    report.append('stamped  the docstring')
    try:
        compile(t, RUNNER, 'exec')
    except SyntaxError as exc:
        raise PatchError('%s would not compile: %s' % (RUNNER, exc))
    return t, count


def edit_ledger(t, report, gating):
    _exactly_once(t, LEDGER_STAMP_ANCHOR, '%s: the header stamp' % LEDGER)
    t = t.replace(LEDGER_STAMP_ANCHOR, LEDGER_STAMP + LEDGER_STAMP_ANCHOR)
    report.append('stamped  the header')
    if '#### [L-440]' in t:
        raise PatchError('%s already has an L-440 block' % LEDGER)
    _exactly_once(t, LEDGER_SECTION_A, '%s: section A' % LEDGER)
    t = t.replace(LEDGER_SECTION_A,
                  LEDGER_SECTION_A + L440_BLOCK % dict(gating=gating) + '\n')
    report.append('added    the L-440 block at the top of section A')
    _exactly_once(t, L324_ANCHOR, '%s: L-324\'s parity line' % LEDGER)
    t = t.replace(L324_ANCHOR, L324_ANCHOR + L324_NOTE)
    report.append('noted    on L-324: its parity row is built')
    return t


def edit_page(t, report):
    if PAGE_MARKER not in t:
        raise PatchError('%s has no run-record marker' % PAGE)
    marker = t.index(PAGE_MARKER)
    for where, old, new in PAGE_EDITS:
        _exactly_once(t, old, '%s: %s' % (PAGE, where))
        if t.index(old) > marker:
            raise PatchError('%s: %s lies below the run-record marker'
                             % (PAGE, where))
        t = t.replace(old, new)
        marker = t.index(PAGE_MARKER)
        report.append('edited   %s' % where)
    m = re.search(r'^Last updated: .*\n- Written at orrery .*\n', t, re.M)
    if not m or m.start() > marker:
        raise PatchError('%s: the "Last updated" lines were not found' % PAGE)
    t = (t[:m.start()] + 'Last updated: October 13, 2026, evening: the '
         'dashboard\'s cards, headings and names.\n- Written at orrery %s and '
         'gallery %s.\n' % (BASE_SHORT, GALLERY_SHORT) + t[m.end():])
    report.append('edited   the "Last updated" lines')
    above = t[:t.index(PAGE_MARKER)].count('\n')
    if above > PAGE_CAP:
        raise PatchError('%s would have %d lines above the marker (cap %d)'
                         % (PAGE, above, PAGE_CAP))
    report.append('checked  %d lines above the run-record marker (cap %d)'
                  % (above, PAGE_CAP))
    return t


def _read(rel):
    path = os.path.join(ROOT, rel)
    if not os.path.exists(path):
        raise PatchError('%s not found in %s' % (rel, ROOT))
    raw = open(path, 'rb').read()
    crlf = b'\r\n' in raw
    try:
        text = raw.replace(b'\r\n', b'\n').decode('utf-8')
    except UnicodeDecodeError as exc:
        raise PatchError('%s is not UTF-8: %s' % (rel, exc))
    return text, crlf


def apply():
    for rel in (PARITY_FILE, HANDOFF_FILE):
        if os.path.exists(os.path.join(ROOT, rel)):
            raise PatchError('%s already exists; this patch has run, or a '
                             'file of that name is in the way' % rel)
    texts, crlf, report = {}, [], {}
    for rel in (DASHBOARD, RUNNER, LEDGER, PAGE):
        texts[rel], was = _read(rel)
        if was:
            crlf.append(rel)
        report[rel] = []
    texts[DASHBOARD] = edit_dashboard(texts[DASHBOARD], report[DASHBOARD])
    texts[RUNNER], gating = edit_runner(texts[RUNNER], report[RUNNER])
    texts[LEDGER] = edit_ledger(texts[LEDGER], report[LEDGER], gating)
    texts[PAGE] = edit_page(texts[PAGE], report[PAGE])
    new_files = {PARITY_FILE: PARITY_SOURCE, HANDOFF_FILE: HANDOFF_TEXT}
    for rel, text in list(texts.items()) + list(new_files.items()):
        bad = [c for c in text if ord(c) > 127]
        if bad:
            raise PatchError('%s would hold %d non-ASCII character(s)'
                             % (rel, len(bad)))
    try:
        compile(PARITY_SOURCE, PARITY_FILE, 'exec')
    except SyntaxError as exc:
        raise PatchError('%s would not compile: %s' % (PARITY_FILE, exc))
    # Every check passed: write, LF, all or nothing from here.
    for rel, text in list(texts.items()) + list(new_files.items()):
        with open(os.path.join(ROOT, rel), 'w', encoding='utf-8',
                  newline='') as f:
            f.write(text)
    for rel in (DASHBOARD, RUNNER, LEDGER, PAGE):
        for line in report[rel]:
            print('ok  %-30s %s' % (rel, line))
    for rel in new_files:
        print('ok  %-30s new file' % rel)
    for rel in crlf:
        print('note: %s was CRLF in the working copy; written LF' % rel)
    return gating


def main():
    print(__doc__.split('\n')[0])
    print('Running in: %s' % ROOT)
    print('')
    try:
        gating = apply()
    except PatchError as exc:
        print('ERROR: %s' % exc)
        print('NOTHING was written. Undo is not needed.')
        return 1
    print('')
    print('patch applied')
    print('Stamps updated: palomas_orrery_dashboard.py and')
    print('orrery_maintenance_run.py docstrings, the ledger header.')
    print('Permanent after this script is spent: CARD_LINES and the new card,')
    print('the folding headings, the six website headings, the run-names on')
    print('the buttons, test_dashboard_parity.py and its row in the run.')
    print('')
    print('NEXT:')
    print('  1. Run orrery_maintenance_run.py. Expect %d of %d gating checkers'
          % (gating, gating))
    print('     to pass, "Dashboard parity" among them with 9 of 9 planted')
    print('     faults caught. If another session\'s patch has added a button')
    print('     since, Dashboard parity names it until it has a short line.')
    print('  2. Open palomas_orrery_dashboard.py and look (the handoff,')
    print('     section 6, says what to see). Launch Paloma\'s Orrery once: it')
    print('     should open its own console window beside the plot window.')
    print('  3. Move this script into documentation/; commit and push.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
