"""
earth_system_common.py - Shared, engine-agnostic helpers for the Earth System
KMZ generators (climate/heat and food insecurity).

Holds the pieces that are identical regardless of boundary type, so they live in
one place instead of being duplicated per generator: the tappable "i" pin
info-balloon builder (CDATA HTML balloon), its plain-text -> HTML reflow helper,
and the Tkinter scenario picker. Both earth_system_generator.py and
food_insecurity_generator.py import from here.

The picker is engine-agnostic via dependency injection: the caller passes a
run_fn(scenario, status_callback) that knows how to build assets for one
scenario (heat passes run_scenario; food passes a small adapter over its run()).

Key functions:
    briefing_to_balloon_html() - plain-text briefing -> safe reflowing balloon HTML.
    create_info_placemark() - add the tappable "i" pin Placemark (CDATA balloon).
    ScenarioPicker - generic Tkinter menu; run_fn(scenario, status_callback) injected.

Consumed by: earth_system_generator.py, food_insecurity_generator.py

Module updated: June 2026 with Anthropic's Claude Opus 4.8
"""
import re
import html

import simplekml

import tkinter as tk
from tkinter import ttk, messagebox


def briefing_to_balloon_html(briefing):
    """Convert a plain-text briefing into safe, reflowing balloon HTML.

    Normalizes <br> to line breaks, strips any other markup, escapes the
    text, then re-emits paragraphs so the balloon wraps to the device width.
    """
    text = briefing.replace('<br>', '\n').replace('<BR>', '\n')
    text = re.sub(r'<[^>]+>', '', text)
    paras = [p.strip() for p in re.split(r'\n\s*\n', text) if p.strip()]
    out = []
    for p in paras:
        esc = html.escape(p).replace('\n', '<br>')
        out.append('<p style="margin:0 0 8px 0;">' + esc + '</p>')
    return ''.join(out)


def create_info_placemark(kml, title, date, briefing, lat, lon, extra_html=""):
    """Add a tappable info "i" placemark whose balloon holds the full briefing.

    Engine-agnostic. The balloon reflows to the device width and renders clear
    of Google Earth's search bar / toolbar, so the narrative does not collide
    with chrome the way a fixed ScreenOverlay PNG does. Default-closed; opens
    on tap.

    extra_html: optional HTML appended after the briefing, inside the balloon
    div -- used for a boundary-specific key (e.g. the heat population-exposure
    key). Pass "" for none.
    """
    balloon = (
        '<div style="max-width:340px; '
        'font-family:-apple-system,Helvetica,Arial,sans-serif; '
        'font-size:14px; line-height:1.4; color:#222;">'
        '<h3 style="margin:0 0 6px 0; font-size:16px;">'
        + html.escape(title) + '</h3>'
        '<div style="font:12px monospace; color:#666; margin-bottom:8px;">'
        'DATE: ' + html.escape(str(date)) + '</div>'
        + briefing_to_balloon_html(briefing)
        + (extra_html or "")
        + '</div>'
    )

    pnt = kml.newpoint(name="%s - tap for details" % title)
    pnt.coords = [(lon, lat, 0)]
    pnt.altitudemode = simplekml.AltitudeMode.clamptoground
    # Wrap in CDATA so simplekml emits the HTML unescaped (base.py leaves
    # CDATA blocks untouched); GE then renders the balloon as HTML rather
    # than printing literal tags -- matching the proven desktop probe.
    pnt.description = '<![CDATA[' + balloon + ']]>'
    pnt.style.iconstyle.icon.href = \
        "http://maps.google.com/mapfiles/kml/shapes/info-i.png"
    pnt.style.iconstyle.scale = 1.3
    pnt.style.labelstyle.scale = 0.9
    pnt.style.balloonstyle.text = "$[description]"
    return pnt


def _default_display(scenario):
    """Default listbox row: [BNDRY] name."""
    return "[%s] %s" % (scenario.get('boundary_type', '?').upper()[:4],
                        scenario['name'])


class ScenarioPicker:
    """Generic Tkinter menu: pick a scenario, run it via an injected run_fn.

    scenarios   - list of scenario dicts (each needs at least 'name'; the
                  default row formatter also reads 'boundary_type').
    run_fn      - callable run_fn(scenario, status_callback) that builds the
                  assets for one scenario. Heat passes run_scenario; food passes
                  a small adapter over its run().
    title       - window title.
    display_fn  - optional row formatter scenario -> str.
    button_text - action-button label.
    """
    def __init__(self, scenarios, run_fn, title="Select Scenario",
                 display_fn=None,
                 button_text="Generate Assets (Teaser + KMZ) in data/"):
        self.scenarios = list(scenarios)
        self.run_fn = run_fn
        self.display_fn = display_fn or _default_display

        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry("500x550")

        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 11), padding=10)

        lbl = tk.Label(self.root, text="Select Scenario",
                       font=("Helvetica", 14, "bold"))
        lbl.pack(pady=15)

        self.listbox = tk.Listbox(self.root, height=14, font=("Helvetica", 11))
        self.listbox.pack(padx=20, pady=5, fill=tk.BOTH, expand=True)
        for scenario in self.scenarios:
            self.listbox.insert(tk.END, self.display_fn(scenario))

        btn = ttk.Button(self.root, text=button_text, command=self.run_selected)
        btn.pack(pady=20)

        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_lbl = tk.Label(self.root, textvariable=self.status_var,
                              font=("Helvetica", 9), fg="gray")
        status_lbl.pack(pady=5)

    def _status_update(self, msg):
        """Thread-safe status update for the GUI."""
        self.status_var.set(msg)
        self.root.update()

    def run_selected(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a scenario.")
            return

        scenario = self.scenarios[selection[0]]

        try:
            self.run_fn(scenario, status_callback=self._status_update)
            self.status_var.set("Ready")
            messagebox.showinfo("Success",
                                "Generated assets for:\n%s in data/"
                                % scenario['name'])
        except Exception as e:
            self.status_var.set("Ready")
            messagebox.showerror("Error", str(e))

    def mainloop(self):
        self.root.mainloop()
