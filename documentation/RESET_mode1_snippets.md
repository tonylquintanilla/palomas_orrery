# Reset Button -- Mode-1 snippets for palomas_orrery.py

Base HEAD: `77dce3ead907b49af70eac05223e0dc7ee007520`. Both snippets are pure
INSERTIONS (no existing lines change). Verified in sandbox: py_compile OK,
ASCII clean, LF clean, and test_reset_completeness.py PASSED against the LIVE
handler (309 IntVars + 3 StringVars + 10 entries all reset; exit 0).

---

## SNIPPET 1 -- the handler

INSERT immediately AFTER the end of `fill_now` (the line
`        fill_now.initialized = True`, ~L8210) and BEFORE
`def calculate_next_vernal_equinox(from_date):` (~L8212). One blank line on
each side.

```python
def reset_all_selections():
    """Return the GUI to its STARTUP state, behind a confirm dialog.

    Date -> now; every checkbutton cleared (bodies, shells, celestial, comets,
    spacecraft); center -> Sun; scale -> Auto; plot scalars -> startup values.

    Completeness is the one real care (a partial reset that clears bodies but
    leaves shells looks clean but is wrong). It is made provably total here by:
      1. a per-object loop clearing the 182 body/spacecraft/comet vars,
      2. restoring the handful of named display/option toggles to their DECLARED
         defaults (two markers default ON -> restored to 1, not 0),
      3. a complement-set sweep that zeroes EVERY remaining module tk.IntVar.
    The sweep reaches all 113 shell/belt vars -- which have no single registry
    that cleanly covers them -- plus a few dead stragglers, and is drift-proof:
    a future checkbox family is cleared automatically. Runtime-proven safe: the
    117 swept vars all have declared default 0; the only default-1 vars (the two
    markers) are handled explicitly in step 2. Guarded against the LIVE handler
    by test_reset_completeness.py.

    Module updated: June 2026 with Anthropic's Claude Opus 4.8. Added GUI Reset
    button + handler (objects loop + named-default restore + IntVar sweep).
    """
    if not messagebox.askyesno("Reset",
                               "Clear all selections and reset to defaults?"):
        return

    # --- Family 1: object selection vars (bodies, moons, comets, spacecraft) ---
    for obj in objects:
        obj['var'].set(0)

    # --- Families 3 & 4: named display/option toggles -> DECLARED defaults ---
    # The two marker toggles default ON (value=1); restore to 1, not 0. (Their
    # inline "NOT showing" comments at declaration are stale -- value is 1.)
    star_background_var.set(0)
    star_names_var.set(0)
    celestial_grid_var.set(0)
    celestial_grid_labels_var.set(0)
    constellation_names_var.set(0)
    show_apsidal_markers_var.set(1)       # declared default = 1
    show_closest_approach_var.set(1)      # declared default = 1
    animate_comet_tails_var.set(0)
    animate_magnetospheres_var.set(0)
    special_fetch_var.set(0)

    # --- Family 2: shell/belt sub-toggles (113) + any other stray IntVar ---
    # Complement-set sweep: zero every module IntVar NOT handled above. This is
    # the mechanism that makes the reset provably total without hardcoding 113
    # shell names or relying on a registry that does not cover all of them.
    # add new checkbox families here: a new family that needs a NON-zero startup
    # default must be restored explicitly above, or the sweep will zero it.
    _handled_ids = {id(obj['var']) for obj in objects}
    _handled_ids.update(id(v) for v in (
        star_background_var, star_names_var, celestial_grid_var,
        celestial_grid_labels_var, constellation_names_var,
        show_apsidal_markers_var, show_closest_approach_var,
        animate_comet_tails_var, animate_magnetospheres_var, special_fetch_var,
    ))
    for _v in list(globals().values()):
        if isinstance(_v, tk.IntVar) and id(_v) not in _handled_ids:
            _v.set(0)

    # --- Family 5: scalar selector StringVars -> startup defaults ---
    scale_var.set('Auto')
    center_object_var.set('Sun')
    track_camera_var.set('None (free camera)')

    # --- Family 6: scalar entry widgets -> startup defaults (delete + insert) ---
    def _set_entry(entry, value):
        entry.delete(0, tk.END)
        entry.insert(0, value)
    # days_to_plot must be reset BEFORE fill_now() so the end date recomputes.
    _set_entry(days_to_plot_entry, '28')
    _set_entry(custom_scale_entry, '10')
    _set_entry(orbital_points_entry, '50')
    _set_entry(trajectory_points_entry, '50')
    _set_entry(satellite_days_entry, '50')
    _set_entry(satellite_points_entry, '50')
    _set_entry(num_frames_entry, '29')
    _set_entry(default_interval_entry, '1d')
    _set_entry(trajectory_interval_entry, '6h')
    _set_entry(satellite_interval_entry, '1h')

    # --- Date fields -> now (reuse the startup helper; recomputes end date) ---
    fill_now()
```

---

## SNIPPET 2 -- the button widget

INSERT immediately AFTER the `vernal_equinox_button` tooltip line
(`CreateToolTip(vernal_equinox_button, "Fill the next vernal equinox ...")`,
~L8503) and BEFORE the `# END DATE ROW (Row 1)` comment. One blank line on
each side.

```python
reset_button = tk.Button(date_frame, text="Reset", command=reset_all_selections, width=5)
reset_button.grid(row=0, column=11, padx=(5, 0), pady=2, sticky='w')
CreateToolTip(reset_button, "Clear all selections and reset the GUI to its startup state (date->now, center Sun, scale Auto)")
```

---

## Placement note

date_frame row 0 ends at column 10 (Vernal Eq). Reset goes at row 0, column 11
-- free, immediately right of Vernal Eq. The `horizons_warning` label below
spans columns 0-10 (columnspan=11), so column 11 does not collide with it.
