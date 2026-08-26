"""
patch_L251_1_galactic_center_launcher.py -- stop serving a cached HTML.

Run:  save into the repo root (the folder holding palomas_orrery.py),
      open in VS Code, click Run.
      Or:  python patch_L251_1_galactic_center_launcher.py

Built on 8847d6be699c49c7e8fa077cc7f1790909c74c47
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

Tony's ruling, 2026-08-25.

THE BUG, AND WHY IT HID FOR SEVEN MONTHS

launch_galactic_center() in palomas_orrery.py opened a permanent
sgr_a_grand_tour.html from the repo root if one existed, and only
generated when it did not:

    if os.path.exists(html_path):
        webbrowser.open('file://' + os.path.realpath(html_path))
    else:
        fig = sgr.create_grand_tour_dashboard()
        fig.write_html(html_path)

So the first click wrote the file and every click after that served it,
unchanged, forever. The file Tony was looking at on 2026-08-25 was
written in January 2026. It survived the L-247 migration, the constants
repair, and every regeneration in between, because nothing in that path
ever looks at the code again.

It was also a parallel pipeline. sgr_a_grand_tour.py's own __main__
already calls show_and_save(fig, "sgr_a_grand_tour"), which writes a
temp file, opens THAT, and then offers a save dialog. Two entry points
to one figure, with different behaviour, and only one of them current.

THE FIX

The launcher generates every time and hands the figure to the same
show_and_save the module's __main__ uses. No permanent file is read.
No permanent file is written unless Tony chooses one in the dialog.

The dead branch goes with it: there is no longer an "if it exists"
case, so there is nothing to be stale.

ONE THING THIS DOES NOT DO

It does not delete an existing sgr_a_grand_tour.html. Deleting a file
in Tony's working folder is not this patch's business, and after this
change nothing reads it. The patch reports whether one is present so
the decision is visible rather than implied.

AFTER THIS RUN
  Click Galactic Center in the orrery. It should take a moment to
  generate, open a tmp*.htm tab, and then offer a save dialog -- the
  same behaviour as running sgr_a_grand_tour.py directly.

Success: one "ok" line per edit, then "patch applied".
Failure: a single "ERROR:" or "ANCHOR FAIL" line; nothing is written.
"""

import hashlib
import os
import sys

TARGET = 'palomas_orrery.py'
BASE_FP = '6fed84d6bbc36397fcfa47d71e6c286b'

OLD = b'''def launch_galactic_center():
    """Launch the Sagittarius A* Grand Tour visualization."""
    import os
    import webbrowser
    
    # Path to the HTML file (same directory as this script)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    html_path = os.path.join(script_dir, "sgr_a_grand_tour.html")
    
    # Check if HTML exists
    if os.path.exists(html_path):
        # Open in default browser
        webbrowser.open('file://' + os.path.realpath(html_path))
        print(f"[GALACTIC CENTER] Opened visualization: {html_path}", flush=True)
    else:
        # Try to generate it
        print(f"[GALACTIC CENTER] HTML not found, attempting to generate...", flush=True)
        try:
            # Import and run the generator
            import sgr_a_grand_tour as sgr
            fig = sgr.create_grand_tour_dashboard()
            fig.write_html(html_path)
            print(f"[GALACTIC CENTER] Generated: {html_path}", flush=True)
            webbrowser.open('file://' + os.path.realpath(html_path))
        except ImportError as e:
            print(f"[GALACTIC CENTER] ERROR: Missing module - {e}", flush=True)
            print("Please ensure sgr_a_grand_tour.py and dependencies are in the same folder.", flush=True)
            # Show error dialog
            import tkinter.messagebox as messagebox
            messagebox.showerror("Galactic Center", 
                f"Could not launch visualization.\\n\\n"
                f"Missing module: {e}\\n\\n"
                f"Please ensure these files are in the same folder:\\n"
                f"- sgr_a_star_data.py\\n"
                f"- sgr_a_visualization_core.py\\n"
                f"- sgr_a_grand_tour.py")
        except Exception as e:
            print(f"[GALACTIC CENTER] ERROR: {e}", flush=True)
            import tkinter.messagebox as messagebox
            messagebox.showerror("Galactic Center", f"Error launching visualization:\\n{e}")
'''

NEW = b'''def launch_galactic_center():
    """Launch the Sagittarius A* Grand Tour visualization.

    Generates the figure every time and hands it to show_and_save --
    the same path sgr_a_grand_tour.py's own __main__ takes. Nothing is
    read from or written to a permanent file in the repo root.

    Until 2026-08-25 this opened a saved HTML of the same name in the
    repo root if one existed, and generated only when it did not -- so
    the first click wrote that file and every click after served it
    unchanged. The copy Tony was reading on that date had been written
    in January 2026 and had survived every constant change since,
    silently (L-251).
    """
    try:
        # Imported here rather than at module scope: this is the one
        # place that needs them, and a missing dependency should show
        # as a dialog on the click, not a failure to start the orrery.
        import sgr_a_grand_tour as sgr
        from save_utils import show_and_save

        print("[GALACTIC CENTER] Generating from current data...", flush=True)
        fig = sgr.create_grand_tour_dashboard()
        # Opens a temp copy in the browser, then offers the save
        # dialog. Declining the dialog is a normal outcome.
        show_and_save(fig, "sgr_a_grand_tour")
        print("[GALACTIC CENTER] Opened in browser", flush=True)
    except ImportError as e:
        print(f"[GALACTIC CENTER] ERROR: Missing module - {e}", flush=True)
        print("Please ensure sgr_a_grand_tour.py and dependencies are in the same folder.", flush=True)
        # Show error dialog
        import tkinter.messagebox as messagebox
        messagebox.showerror("Galactic Center", 
            f"Could not launch visualization.\\n\\n"
            f"Missing module: {e}\\n\\n"
            f"Please ensure these files are in the same folder:\\n"
            f"- sgr_a_star_data.py\\n"
            f"- sgr_a_visualization_core.py\\n"
            f"- sgr_a_grand_tour.py\\n"
            f"- save_utils.py")
    except Exception as e:
        print(f"[GALACTIC CENTER] ERROR: {e}", flush=True)
        import tkinter.messagebox as messagebox
        messagebox.showerror("Galactic Center", f"Error launching visualization:\\n{e}")
'''


def fail(msg):
    print('ERROR: ' + msg)
    sys.exit(1)


def main():
    if not os.path.exists(TARGET):
        fail('%s not found. Run this from the repo root.' % TARGET)
    if not os.path.exists('save_utils.py'):
        fail('save_utils.py not found -- the new launcher imports it.')

    with open(TARGET, 'rb') as handle:
        data = handle.read()

    is_crlf = data.count(b'\r\n') > 0
    fp = hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()
    if fp != BASE_FP:
        print('ERROR: BASE MOVED -- %s' % TARGET)
        print('  expected content fingerprint %s' % BASE_FP)
        print('  found                        %s' % fp)
        sys.exit(1)
    print('base ok  %-20s (%s)  %d bytes'
          % (TARGET, 'CRLF' if is_crlf else 'LF', len(data)))

    o, n = OLD, NEW
    if is_crlf:
        o = o.replace(b'\n', b'\r\n')
        n = n.replace(b'\n', b'\r\n')
    bad = sorted({b for b in n if b > 127})
    if bad:
        fail('non-ASCII byte(s) in inserted text: %r' % bad)
    count = data.count(o)
    if count != 1:
        print('ANCHOR FAIL (%d matches, expected 1): launch_galactic_center()'
              % count)
        print('  nothing written.')
        sys.exit(1)
    out = data.replace(o, n)
    print('ok  launch_galactic_center() routes through show_and_save')

    text = out.replace(b'\r\n', b'\n')
    if b'sgr_a_grand_tour.html' in text:
        fail('post-check: the permanent HTML path survives somewhere in '
             'this file')
    if b'fig.write_html(html_path)' in text:
        fail('post-check: a direct write_html survives')
    if text.count(b'show_and_save(fig, "sgr_a_grand_tour")') != 1:
        fail('post-check: the launcher does not call show_and_save')
    print('ok  post-check: no permanent path, no direct write, one '
          'show_and_save')

    with open(TARGET, 'wb') as handle:
        handle.write(out)
    print('patch applied  %s  %+d bytes  (%s)'
          % (TARGET, len(out) - len(data), 'CRLF' if is_crlf else 'LF'))

    stale = os.path.join(os.path.dirname(os.path.abspath(TARGET)),
                         'sgr_a_grand_tour.html')
    print('')
    if os.path.exists(stale):
        print('NOTE: sgr_a_grand_tour.html is still in the repo root.')
        print('  Nothing reads it now. Deleting it is yours to do; this')
        print('  patch does not touch files in your working folder.')
    else:
        print('NOTE: no sgr_a_grand_tour.html in the repo root.')
    print('')
    print('NEXT: click Galactic Center in the orrery. It should pause to')
    print('  generate, open a tmp*.htm tab, then offer the save dialog --')
    print('  the same behaviour as running sgr_a_grand_tour.py directly.')


if __name__ == '__main__':
    main()
