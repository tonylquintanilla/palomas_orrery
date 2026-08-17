"""patch_L196_9_launch_tooltips.py -- dashboard launch-button hover text,
plus a self-explanatory summary line for the 1d/1e checker.

RUN COMMAND
-----------
Save this file into the palomas_orrery repo root (the same folder as
palomas_orrery_dashboard.py), open it in VS Code, and click Run.

    python patch_L196_9_launch_tooltips.py

WHAT IT DOES
------------
1. palomas_orrery_dashboard.py -- every Launch button gets hover text
   naming the repo and the file it actually runs:

       Orrery: palomas_orrery.py
       Gallery: tools/gallery_studio.py
       Orrery: earth_system_controller.py --preload food_insecurity

   The path is shown relative to the repo root it belongs to, so a
   gallery tool reads as tools/<name>.py even though the dashboard
   launches it with its working directory already inside tools/. Args
   are included, which is what tells the two earth_system_controller.py
   cards apart. A card whose script is missing shows the full path the
   dashboard looked at instead, so "Not Found" says where it looked.

   customtkinter has no tooltip, so this adds a small one: a borderless
   Toplevel shown after a short delay, bound to the button AND its child
   widgets, because a CTkButton is a frame whose canvas and label sit on
   top of it and would otherwise swallow the enter event.

2. test_provenance_1d.py and maintenance_run.py -- the checker read
   "Provenance 1d/1e ... All Phase 1d/1e tests passed", which names a
   ledger sub-step twice and says nothing. The runner label becomes
   "Scanner recognition 1d/1e" and the verdict line becomes "Real
   citations recognized, fake ones refused."

   The verdict has to be ONE short line: the runner takes the last
   non-blank line of a checker's output and trims it to 44 characters,
   so a multi-line explanation would surface as its own last fragment.
   The fuller explanation therefore prints ABOVE the verdict, where it
   is visible to anyone running the test on its own and invisible to
   the summary.

   The new label is 25 characters against a 24-wide column, so both
   print statements widen by one. Every other label already fits.

WHY 2 IS IN THE SAME PATCH
--------------------------
Tony asked what the line meant. Explaining it once fixes it for one
reading; making the line say it fixes it for every future run. Both
edits are the same job -- make the output name what it is doing. It is
one line and trivially reverted if the wording is wrong.

PERMANENT vs DISPOSABLE
-----------------------
This script is disposable and one-shot. What it installs is permanent:
the Tooltip class, the launch_target_label() helper, the tooltip on
every launch button, and the reworded summary line.

SAFETY
------
All-or-nothing. Both files are fingerprinted (CRLF-normalized) before
anything is written, and every anchor must match exactly once. Any
mismatch aborts the whole run with nothing written. Each file's own
line endings are preserved.

Success: one 'ok' line per file, then 'patch applied (N bytes)'.
Failure: a single 'ERROR:' or 'ANCHOR FAIL' line; nothing is written.
"""

import hashlib
import os
import sys


OLD_IMPORT = """import webbrowser
import customtkinter as ctk
"""

NEW_IMPORT = """import webbrowser
import tkinter as tk
import customtkinter as ctk
"""

OLD_AFTER_GROUPS = """
# ============================================================
# EXTERNAL LINKS
# ============================================================
"""

NEW_AFTER_GROUPS = '''
# ============================================================
# LAUNCH TARGET LABELS AND HOVER TEXT
# ============================================================

# Longest path first: a nested repo must be tested before its parent,
# or the parent claims every file under it.
REPO_ROOTS = (
    (GALLERY_REPO_DIR, "Gallery"),
    (SCRIPT_DIR, "Orrery"),
)

TOOLTIP_DELAY_MS = 400


def launch_target_label(script, base_dir=None, args=None):
    """'Orrery: palomas_orrery.py' -- which repo, and the path inside it.

    The dashboard launches some tools with a working directory already
    inside the repo (gallery tools run from tools/), so the path is
    rebuilt relative to the repo ROOT rather than shown as handed to
    the subprocess. A target outside both repos falls back to its full
    path, which is also what an unresolvable one shows.
    """
    full = os.path.abspath(os.path.join(base_dir or SCRIPT_DIR, script))
    shown = full
    for root, label in REPO_ROOTS:
        try:
            rel = os.path.relpath(full, os.path.abspath(root))
        except ValueError:
            # Different drive on Windows. Not this repo.
            continue
        if not rel.startswith(os.pardir):
            shown = "%s: %s" % (label, rel.replace(os.sep, "/"))
            break
    if args:
        shown = "%s %s" % (shown, " ".join(args))
    return shown


class Tooltip(object):
    """Hover text for a customtkinter widget.

    Bound to the widget AND every descendant. A CTkButton is a frame
    holding a canvas and a label; those sit on top of the frame and
    receive the enter event instead of it, so binding the frame alone
    shows nothing on the widget it was asked for.
    """

    def __init__(self, widget, text):
        self.text = text
        self.window = None
        self.after_id = None
        self.widget = widget
        self._bind_tree(widget)

    def _bind_tree(self, widget):
        widget.bind("<Enter>", self._schedule, add="+")
        widget.bind("<Leave>", self._hide, add="+")
        widget.bind("<ButtonPress>", self._hide, add="+")
        for child in widget.winfo_children():
            self._bind_tree(child)

    def _schedule(self, _event=None):
        self._cancel()
        self.after_id = self.widget.after(TOOLTIP_DELAY_MS, self._show)

    def _cancel(self):
        if self.after_id is not None:
            try:
                self.widget.after_cancel(self.after_id)
            except Exception:
                pass
            self.after_id = None

    def _show(self):
        if self.window is not None or not self.text:
            return
        try:
            x = self.widget.winfo_rootx()
            y = self.widget.winfo_rooty() + self.widget.winfo_height() + 6
        except Exception:
            return
        self.window = tk.Toplevel(self.widget)
        self.window.wm_overrideredirect(True)
        self.window.wm_geometry("+%d+%d" % (x, y))
        try:
            self.window.wm_attributes("-topmost", True)
        except Exception:
            # Not supported everywhere; the tooltip still shows.
            pass
        tk.Label(
            self.window, text=self.text, justify="left",
            background=COLOR_SURFACE_HOVER, foreground=COLOR_TEXT,
            relief="solid", borderwidth=1,
            font=("Consolas", 10), padx=8, pady=4
        ).pack()

    def _hide(self, _event=None):
        self._cancel()
        if self.window is not None:
            self.window.destroy()
            self.window = None


# ============================================================
# EXTERNAL LINKS
# ============================================================
'''

OLD_BUTTON = """            command=lambda s=script, b=base_dir, ia=interactive, a=args: self._launch(s, b, ia, a),
            state="normal" if exists else "disabled"
        )
        btn.pack(side="right", padx=(12, 0))
"""

NEW_BUTTON = """            command=lambda s=script, b=base_dir, ia=interactive, a=args: self._launch(s, b, ia, a),
            state="normal" if exists else "disabled"
        )
        btn.pack(side="right", padx=(12, 0))

        # Name the repo and file this button runs. A missing script shows
        # the full path instead, so "Not Found" says where it looked.
        if exists:
            hover = launch_target_label(script, base_dir, args)
        else:
            hover = "Not found: %s" % script_path
        Tooltip(btn, hover)
"""

OLD_SUMMARY = '''    print("\\nAll Phase 1d/1e tests passed.")
'''

NEW_SUMMARY = '''    print("\\nPhase 1d/1e (L-156) pins the scanner's recognition rules: "
          "shadow\\nconstants, author-year citation forms, F/C units, "
          "tier labels. Half\\nthe tests are negative, because a regex "
          "that is too loose clears\\nfindings by matching what it "
          "should not, and the tier totals then move\\nin the direction "
          "that looks like success.")
    # The runner quotes the LAST non-blank line and trims it to 44
    # characters, so the verdict goes last and stays one short line.
    print("\\nReal citations recognized, fake ones refused.")
'''

OLD_COL_GEN = ("        print('  %-24s %6.1fs  %s' % (label, seconds, note))\n"
               "        results.append((label, rc, seconds, note, output, False))\n")
NEW_COL_GEN = ("        print('  %-25s %6.1fs  %s' % (label, seconds, note))\n"
               "        results.append((label, rc, seconds, note, output, False))\n")

OLD_COL_CHK = ("        print('  %-24s %6.1fs  %s' % (label, seconds, note))\n"
               "        results.append((label, rc, seconds, note, output, True))\n")
NEW_COL_CHK = ("        print('  %-25s %6.1fs  %s' % (label, seconds, note))\n"
               "        results.append((label, rc, seconds, note, output, True))\n")

OLD_RUNNER_LABEL = ("    ('Provenance 1d/1e', "
                    "['test_provenance_1d.py'], None),\n")
NEW_RUNNER_LABEL = ("    ('Scanner recognition 1d/1e', "
                    "['test_provenance_1d.py'], None),\n")

EDITS = {
    'maintenance_run.py': {
        'fp': '16f9df780cd07d989f2b6c2bcd5cb4d3',
        'edits': [
            (OLD_RUNNER_LABEL, NEW_RUNNER_LABEL),
            (OLD_COL_GEN, NEW_COL_GEN),
            (OLD_COL_CHK, NEW_COL_CHK),
        ],
    },
    'palomas_orrery_dashboard.py': {
        'fp': '2cd067371819df3ad1ef7be5cbd91864',
        'edits': [
            (OLD_IMPORT, NEW_IMPORT),
            (OLD_AFTER_GROUPS, NEW_AFTER_GROUPS),
            (OLD_BUTTON, NEW_BUTTON),
        ],
    },
    'test_provenance_1d.py': {
        'fp': '5077af73cd1cc5d0de22198e41181c61',
        'edits': [
            (OLD_SUMMARY, NEW_SUMMARY),
        ],
    },
}


def normalized(data):
    return data.replace(b'\r\n', b'\n')


def non_ascii_count(data):
    return sum(1 for byte in data if byte > 127)


def main():
    if not os.path.isfile('palomas_orrery_dashboard.py'):
        print('ERROR: run this from the palomas_orrery repo root '
              '(the folder holding palomas_orrery_dashboard.py).')
        return 1

    staged = []
    total = 0
    notes = []

    for name in sorted(EDITS):
        spec = EDITS[name]
        if not os.path.isfile(name):
            print('ERROR: %s not found.' % name)
            return 1

        with open(name, 'rb') as handle:
            raw = handle.read()

        fp = hashlib.md5(normalized(raw)).hexdigest()
        if fp != spec['fp']:
            print('ERROR: %s does not match the base this patch was built '
                  'against.' % name)
            print('       expected %s' % spec['fp'])
            print('       found    %s' % fp)
            print('       Nothing written. If this patch has already run, '
                  'that is the expected abort -- it is one-shot.')
            return 1

        crlf = b'\r\n' in raw
        text = normalized(raw).decode('utf-8')

        for old, new in spec['edits']:
            count = text.count(old)
            if count != 1:
                print('ANCHOR FAIL: %s -- expected 1 match, found %d.'
                      % (name, count))
                print('       anchor starts: %r' % old[:70])
                print('       Nothing written.')
                return 1
            inserted = non_ascii_count(new.encode('utf-8'))
            if inserted:
                print('ERROR: %s -- an inserted block carries %d non-ASCII '
                      'byte(s). Nothing written.' % (name, inserted))
                return 1
            text = text.replace(old, new)

        out = text.encode('utf-8')
        pre_existing = non_ascii_count(out)
        if pre_existing:
            notes.append('note: %s still holds %d non-ASCII byte(s) this '
                         'patch did not reach' % (name, pre_existing))
        if crlf:
            out = out.replace(b'\n', b'\r\n')
        staged.append((name, out, len(spec['edits'])))
        total += len(out)

    for name, out, count in staged:
        with open(name, 'wb') as handle:
            handle.write(out)
        print('ok  %-34s %d edit(s)' % (name, count))

    for note in notes:
        print(note)
    print('patch applied (%d bytes)' % total)
    print('')
    print('Next: launch the dashboard and hover a Launch button, then '
          'run maintenance_run.py.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
