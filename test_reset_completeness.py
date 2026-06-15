#!/usr/bin/env python3
"""test_reset_completeness.py -- guard the Reset button against partial-reset drift.

Snapshots every module-level tk.IntVar / tk.StringVar declared default plus the
scalar entry widgets, dirties each away from its default, calls the LIVE
reset_all_selections() handler (the button's actual command -- not a
reimplemented clear), and asserts every var returns to its startup default.

This is the structural guard from the touchpoint map: if a future shell/toggle
family is added and Reset misses it, this fails loudly and names the missed var.
The guarantee lives in this test, not in an over-built registry architecture.

Runs headless: tk mainloop suppressed, messagebox dialogs neutralized so the
confirm dialog auto-confirms.
    Run:  xvfb-run -a python3 test_reset_completeness.py

Module created: June 2026 with Anthropic's Claude Opus 4.8.
"""
import os
import sys
import tkinter as tk
import tkinter.messagebox as messagebox

# --- headless harness: never block on mainloop; auto-confirm the reset dialog ---
tk.Misc.mainloop = lambda self, *a, **k: None
for _name in ('askyesno', 'askokcancel'):
    setattr(messagebox, _name, lambda *a, **k: True)
for _name in ('showinfo', 'showwarning', 'showerror'):
    setattr(messagebox, _name, lambda *a, **k: None)

# --- import the app under test (live handler comes from here) ---
HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
sys.path.insert(0, HERE)
import importlib  # noqa: E402
po = importlib.import_module('palomas_orrery')
g = vars(po)

# Scalar entry widgets Reset restores to fixed startup strings (name -> default).
ENTRY_DEFAULTS = {
    'days_to_plot_entry': '28',
    'custom_scale_entry': '10',
    'orbital_points_entry': '50',
    'trajectory_points_entry': '50',
    'satellite_days_entry': '50',
    'satellite_points_entry': '50',
    'num_frames_entry': '29',
    'default_interval_entry': '1d',
    'trajectory_interval_entry': '6h',
    'satellite_interval_entry': '1h',
}

# --- snapshot declared defaults (at import == defaults), keyed by object id ---
# Distinct objects only: frag_var aliases comet_2025k1d_var (same id), so the
# de-dup by id() naturally collapses the alias into one entry.
intvars = {}   # id -> [default_value, [names...]]
strvars = {}   # id -> [default_value, [names...]]
id_to_var = {}
for nm, v in list(g.items()):
    if isinstance(v, tk.IntVar):
        intvars.setdefault(id(v), [v.get(), []])[1].append(nm)
        id_to_var[id(v)] = v
    elif isinstance(v, tk.StringVar):
        strvars.setdefault(id(v), [v.get(), []])[1].append(nm)
        id_to_var[id(v)] = v

entries = {}   # name -> widget  (validate present; default comes from ENTRY_DEFAULTS)
for nm in ENTRY_DEFAULTS:
    e = g.get(nm)
    if e is None:
        print(f"  !! expected entry widget missing from module: {nm}")
    else:
        entries[nm] = e

print(f"snapshot: {len(intvars)} distinct IntVars, {len(strvars)} StringVars, "
      f"{len(entries)} scalar entries")

# --- dirty everything away from its default ---
for vid, (default, _names) in intvars.items():
    id_to_var[vid].set(1 - default if default in (0, 1) else default + 1)
for vid, (_default, _names) in strvars.items():
    id_to_var[vid].set('__DIRTY__')
for nm, e in entries.items():
    e.delete(0, tk.END)
    e.insert(0, '999' if nm == 'days_to_plot_entry' else '__DIRTY__')

# --- call the LIVE handler (exactly what the Reset button invokes) ---
po.reset_all_selections()

# --- assert every var is back at its declared default ---
failures = []
for vid, (default, names) in intvars.items():
    got = id_to_var[vid].get()
    if got != default:
        failures.append(f"IntVar {names} = {got}, expected {default}")
for vid, (default, names) in strvars.items():
    got = id_to_var[vid].get()
    if got != default:
        failures.append(f"StringVar {names} = {got!r}, expected {default!r}")
for nm, e in entries.items():
    got = e.get()
    if got != ENTRY_DEFAULTS[nm]:
        failures.append(f"entry {nm} = {got!r}, expected {ENTRY_DEFAULTS[nm]!r}")

# --- date fields should have been set to ~now by fill_now() ---
from datetime import datetime  # noqa: E402
now = datetime.now()
for nm, expected in (('entry_year', now.year), ('entry_month', now.month),
                     ('entry_day', now.day)):
    e = g.get(nm)
    try:
        got = int(e.get())
    except Exception:
        got = None
    if got != expected:
        failures.append(f"date field {nm} = {None if e is None else e.get()!r}, "
                        f"expected ~{expected}")

if failures:
    print(f"\nFAIL -- {len(failures)} var(s) not reset to startup default:")
    for f in failures:
        print("  -", f)
    sys.exit(1)

print(f"\nPASS -- all {len(intvars)} IntVars + {len(strvars)} StringVars + "
      f"{len(entries)} entries reset to startup defaults; date set to now.")
sys.exit(0)
