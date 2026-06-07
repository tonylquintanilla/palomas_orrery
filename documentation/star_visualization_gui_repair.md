Looking at both versions, I can see the key elements you want to combine:

## From the NEW version (keep):
- **LazyStarPropertiesLoader** and on-demand loading (fast startup)
- **Enhanced search functionality** with unified display
- **Improved star property display** with complete information
- **URL extraction and clickable links**
- **Better error handling and data format detection**

## From the OLD version (restore):
- **Scale Options for Apparent Magnitude 3D Plots** (critical missing feature)
- **Three-column layout** (search | controls | notes)
- **CreateToolTip class** for helpful tooltips
- **PlotlyShutdownHandler** for cleanup
- **Full set of constants** (solar system parameters, etc.)
- **Button styling** (BUTTON_WIDTH, BUTTON_FONT)

Here's a merged version that combines the best of both:

```python
# star_visualization_gui.py - Merged version with best of both implementations

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import subprocess
import os
import sys
import pickle
import pandas as pd
import numpy as np
import re
import webbrowser
from typing import Dict, List, Optional
from datetime import datetime
from star_notes import unique_notes

# Import shutdown handler if available
try:
    from shutdown_handler import PlotlyShutdownHandler
    shutdown_handler = PlotlyShutdownHandler()
except ImportError:
    shutdown_handler = None

# Constants from old version
BUTTON_FONT = ("Arial", 10, "normal")
BUTTON_WIDTH = 30

# CreateToolTip class from old version
class CreateToolTip(object):
    """Create a tooltip for a given widget with intelligent positioning."""
    
    def __init__(self, widget, text='widget info'):
        self.waittime = 500
        self.wraplength = 1000
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id_ = self.id
        self.id = None
        if id_:
            self.widget.after_cancel(id_)

    def showtip(self, event=None):
        try:
            screen_width = self.widget.winfo_screenwidth()
            screen_height = self.widget.winfo_screenheight()
            taskbar_height = 40
            
            self.tw = tk.Toplevel(self.widget)
            self.tw.wm_overrideredirect(True)
            
            usable_height = screen_height - taskbar_height
            
            label = tk.Label(
                self.tw,
                text=self.text,
                justify='left',
                background='yellow',
                relief='solid',
                borderwidth=1,
                wraplength=min(self.wraplength, screen_width - 100),
                font=("Arial", 10, "normal")
            )
            label.pack(ipadx=1, ipady=1)
            
            self.tw.update_idletasks()
            tooltip_width = self.tw.winfo_width()
            tooltip_height = self.tw.winfo_height()
            
            x = self.widget.winfo_rootx() + self.widget.winfo_width() + 5
            
            if x + tooltip_width > screen_width:
                x = self.widget.winfo_rootx() - tooltip_width - 5
            
            if x < 0:
                x = 5
            
            y = self.widget.winfo_rooty()
            
            if tooltip_height > usable_height:
                y = 5
            else:
                widget_center = y + (self.widget.winfo_height() / 2)
                y = widget_center - (tooltip_height / 2)
                
                if y + tooltip_height > usable_height:
                    y = usable_height - tooltip_height - 5
                
                if y < 5:
                    y = 5
            
            self.tw.wm_geometry(f"+{int(x)}+{int(y)}")

        except Exception as e:
            print(f"Error showing tooltip: {e}")

    def hidetip(self):
        if self.tw:
            self.tw.destroy()
        self.tw = None


# LazyStarPropertiesLoader from new version
class LazyStarPropertiesLoader:
    """Loads star properties on-demand rather than all at startup."""
    
    def __init__(self):
        self.loaded_properties = {}
        self.property_files = {
            'distance': 'star_properties_distance.pkl',
            'magnitude': 'star_properties_magnitude.pkl',
            'notable': 'star_properties.pkl'
        }
        self.file_stats = {}
        self._scan_files()
    
    def _scan_files(self):
        """Quick scan to get file stats without loading data."""
        for key, filename in self.property_files.items():
            if os.path.exists(filename):
                size_mb = os.path.getsize(filename) / (1024 * 1024)
                self.file_stats[key] = {
                    'exists': True,
                    'size_mb': size_mb,
                    'filename': filename
                }
            else:
                self.file_stats[key] = {
                    'exists': False,
                    'size_mb': 0,
                    'filename': filename
                }
    
    def get_properties(self, property_type='distance'):
        """Load properties on-demand with caching."""
        if property_type in self.loaded_properties:
            return self.loaded_properties[property_type]
        
        if property_type not in self.property_files:
            print(f"Unknown property type: {property_type}")
            return {}
        
        filename = self.property_files[property_type]
        if not os.path.exists(filename):
            print(f"File not found: {filename}")
            return {}
        
        print(f"Loading {property_type} properties (first access)...")
        try:
            with open(filename, 'rb') as f:
                data = pickle.load(f)
            
            if isinstance(data, list):
                properties = {}
                for item in data:
                    if isinstance(item, dict) and 'unique_id' in item:
                        properties[item['unique_id']] = item
            elif isinstance(data, dict):
                properties = data
            else:
                properties = {}
            
            self.loaded_properties[property_type] = properties
            print(f"  Loaded {len(properties)} stars from {filename}")
            return properties
            
        except Exception as e:
            print(f"Error loading {filename}: {e}")
            return {}
    
    def clear_cache(self, property_type=None):
        """Clear cached data to free memory."""
        if property_type:
            if property_type in self.loaded_properties:
                del self.loaded_properties[property_type]
                print(f"Cleared cache for {property_type}")
        else:
            self.loaded_properties.clear()
            print("Cleared all cached star properties")


# Enhanced search widget from new version
class StarSearchFrame(ttk.Frame):
    """Frame containing star search functionality."""
    
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        
        self.search_results = {
            "Notable Stars": [],
            "Stars by Distance": [],
            "Stars by Magnitude": []
        }
        
        self.star_loader = LazyStarPropertiesLoader()
        self.create_widgets()
        self.load_star_data()

    def create_widgets(self):
        """Create the search widgets for each category."""
        ttk.Label(
            self,
            text="(Ctrl+C for copy, Ctrl+X for cut, Ctrl+V for paste)",
        ).pack(pady=(0, 10))

        self.search_frames = {}
        self.search_vars = {}
        self.search_entries = {}
        self.result_listboxes = {}
        
        categories = ["Notable Stars", "Stars by Distance", "Stars by Magnitude"]
        
        for category in categories:
            frame = ttk.LabelFrame(self, text=category)
            frame.pack(fill='x', padx=5, pady=5)
            self.search_frames[category] = frame
            
            search_var = tk.StringVar()
            search_var.trace_add('write', lambda *args, c=category: self.on_search_change(c))
            self.search_vars[category] = search_var
            
            entry = ttk.Entry(frame, textvariable=search_var)
            entry.pack(fill='x', padx=5, pady=5)
            self.search_entries[category] = entry
            
            list_frame = ttk.Frame(frame)
            list_frame.pack(fill='both', expand=True, padx=5, pady=(0, 5))
            
            scrollbar = ttk.Scrollbar(list_frame)
            scrollbar.pack(side='right', fill='y')
            
            listbox = tk.Listbox(
                list_frame,
                height=5,
                yscrollcommand=scrollbar.set,
                exportselection=False
            )
            listbox.pack(side='left', fill='both', expand=True)
            scrollbar.config(command=listbox.yview)
            
            listbox.bind('<<ListboxSelect>>', 
                        lambda e, c=category: self.on_select(c))
            
            self.create_right_click_menu(listbox)
            self.result_listboxes[category] = listbox

            # Add combined display for Notable Stars
            if category == "Notable Stars":
                info_frame = ttk.Frame(frame)
                info_frame.pack(fill='x', padx=5, pady=(0, 5))
                
                info_label = ttk.Label(info_frame, text="Star Information:")
                info_label.pack(anchor='w')
                
                info_scroll = ttk.Scrollbar(info_frame, orient='vertical')
                info_scroll.pack(side='right', fill='y')
                
                self.info_display = tk.Text(
                    info_frame,
                    height=8,
                    wrap='word',
                    yscrollcommand=info_scroll.set
                )
                self.info_display.pack(fill='x', expand=True)
                info_scroll.config(command=self.info_display.yview)
                
                self.add_clipboard_support(self.info_display)

    def load_star_data(self):
        """Load only star NAMES for search lists."""
        self.star_data = {}
        self.star_full_data = {}
        
        self.star_data["Notable Stars"] = sorted(unique_notes.keys())
        
        for data_type, category in [('distance', 'Stars by Distance'), 
                                    ('magnitude', 'Stars by Magnitude')]:
            filename = f'star_properties_{data_type}.pkl'
            if os.path.exists(filename):
                try:
                    with open(filename, 'rb') as f:
                        data = pickle.load(f)
                    if 'star_names' in data:
                        self.star_data[category] = sorted(data['star_names'])
                    else:
                        self.star_data[category] = []
                except:
                    self.star_data[category] = []
            else:
                self.star_data[category] = []
        
        print("\n" + "="*60)
        print("STAR DATA LOADING SUMMARY")
        print("="*60)
        print(f"Notable Stars: {len(self.star_data.get('Notable Stars', []))} stars")
        print(f"Stars by Distance: {len(self.star_data.get('Stars by Distance', []))} stars")
        print(f"Stars by Magnitude: {len(self.star_data.get('Stars by Magnitude', []))} stars")
        print("="*60 + "\n")

    def on_search_change(self, category: str):
        """Handle changes in search entry."""
        search_term = self.search_vars[category].get().lower()
        listbox = self.result_listboxes[category]
        
        listbox.delete(0, tk.END)
        
        if not search_term:
            return
            
        matches = [
            star for star in self.star_data.get(category, [])
            if search_term in star.lower()
        ]
        
        for star in matches[:50]:
            listbox.insert(tk.END, star)

    def on_select(self, category: str):
        """Handle star selection - display info if Notable Stars."""
        listbox = self.result_listboxes[category]
        try:
            selection = listbox.get(listbox.curselection())
            
            if selection:
                self.search_vars[category].set(selection)
                
                for other_cat in self.search_vars:
                    if other_cat != category:
                        self.search_vars[other_cat].set("")
                
                for lb in self.result_listboxes.values():
                    lb.delete(0, tk.END)
                    lb.master.pack_forget()
                
                # Update info display for Notable Stars
                if category == "Notable Stars" and hasattr(self, 'info_display'):
                    note = unique_notes.get(selection, "")
                    url = self.extract_url(note)
                    
                    display_text = self.clean_html_note(note)
                    if url:
                        display_text += f"\n\nURL: {url}"
                    
                    self.info_display.delete('1.0', tk.END)
                    self.info_display.insert('1.0', display_text)
                    
        except:
            pass

    def extract_url(self, note: str) -> str:
        """Extract URL from star notes if it exists."""
        url_match = re.search(r'<a href="([^"]+)">', note)
        if url_match:
            return url_match.group(1)
        return ""

    def clean_html_note(self, note: str) -> str:
        """Remove HTML tags from note content."""
        clean = re.sub(r'<br\s*/?>', '\n', note)
        clean = re.sub(r'<a\s+href="[^"]*"[^>]*>([^<]*)</a>', r'\1', clean)
        clean = re.sub(r'<[^>]+>', '', clean)
        clean = re.sub(r'\n\s*\n', '\n\n', clean)
        return clean.strip()

    def create_right_click_menu(self, listbox):
        """Create right-click context menu for copying."""
        menu = tk.Menu(self, tearoff=0)
        menu.add_command(label="Copy", 
                        command=lambda: self.copy_selection(listbox))
        
        listbox.bind("<Button-3>", 
                    lambda e: self.show_menu(e, menu))
        
        listbox.bind("<Control-c>", 
                    lambda e: self.copy_selection(listbox))

    def show_menu(self, event, menu):
        """Show the context menu at mouse position."""
        menu.post(event.x_root, event.y_root)

    def copy_selection(self, listbox):
        """Copy selected item to clipboard."""
        try:
            selection = listbox.get(listbox.curselection())
            if selection:
                self.clipboard_clear()
                self.clipboard_append(selection)
        except:
            pass

    def add_clipboard_support(self, widget):
        """Add copy/paste/cut support to a text widget."""
        def copy(event=None):
            try:
                if isinstance(widget, tk.Text):
                    selection = widget.get(tk.SEL_FIRST, tk.SEL_LAST)
                else:
                    selection = widget.selection_get()
                widget.clipboard_clear()
                widget.clipboard_append(selection)
            except:
                pass
            return "break"
        
        def cut(event=None):
            try:
                copy()
                if isinstance(widget, tk.Text):
                    widget.delete(tk.SEL_FIRST, tk.SEL_LAST)
                else:
                    widget.delete("sel.first", "sel.last")
            except:
                pass
            return "break"
        
        def paste(event=None):
            try:
                text = widget.clipboard_get()
                try:
                    if isinstance(widget, tk.Text):
                        widget.delete(tk.SEL_FIRST, tk.SEL_LAST)
                    else:
                        widget.delete("sel.first", "sel.last")
                except:
                    pass
                widget.insert("insert", text)
            except:
                pass
            return "break"

        widget.bind('<Control-c>', copy)
        widget.bind('<Control-x>', cut)
        widget.bind('<Control-v>', paste)
        
        menu = tk.Menu(widget, tearoff=0)
        menu.add_command(label="Cut", command=cut)
        menu.add_command(label="Copy", command=copy)
        menu.add_command(label="Paste", command=paste)
        
        def show_menu(event):
            menu.post(event.x_root, event.y_root)
            return "break"
        
        widget.bind('<Button-3>', show_menu)

    def get_selected_stars(self) -> Dict[str, Optional[str]]:
        """Get currently selected stars for each category."""
        return {
            category: self.search_vars[category].get()
            for category in self.search_vars
        }


# Main GUI window
class StarVisualizationGUI(tk.Tk):
    """Main GUI window with three-column layout."""
    
    def __init__(self):
        super().__init__()
        self.title("Star Visualization Control Panel")
        self.geometry("1400x800")
        
        # Configure grid weights for responsive design
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        
        self.setup_ui()
        
        # Cleanup protocol
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def setup_ui(self):
        """Build the three-column interface."""
        
        # LEFT COLUMN - Star Search
        search_frame = ttk.LabelFrame(self, text="Star Search")
        search_frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
        
        self.star_search = StarSearchFrame(search_frame)
        self.star_search.pack(fill='both', expand=True)
        
        # MIDDLE COLUMN - Plot Controls
        plot_controls_frame = ttk.Frame(self)
        plot_controls_frame.grid(row=0, column=1, padx=10, pady=10, sticky='n')
        
        # Light-year entry
        ly_entry_label = tk.Label(plot_controls_frame, 
                                 text="Enter number of light-years to plot (max 100.1):")
        ly_entry_label.pack(pady=(0, 5))
        
        self.ly_entry = tk.Entry(plot_controls_frame)
        self.ly_entry.pack(pady=(0, 10))
        self.ly_entry.insert(0, '20')
        
        # Distance-based buttons
        plot_button_3d = tk.Button(
            plot_controls_frame,
            text="3D Visualization of Stellar Neighborhood",
            command=self.call_planetarium_distance_script,
            bg='SystemButtonFace',
            fg='blue',
            width=BUTTON_WIDTH,
            font=BUTTON_FONT
        )
        plot_button_3d.pack(pady=(0, 10))
        CreateToolTip(plot_button_3d, 
                     "3D plot of stars within the selected distance from the Sun.")
        
        plot_button_2d = tk.Button(
            plot_controls_frame,
            text="2D Visualization of Stellar Neighborhood",
            command=self.call_hr_diagram_distance_script,
            bg='SystemButtonFace',
            fg='blue',
            width=BUTTON_WIDTH,
            font=BUTTON_FONT
        )
        plot_button_2d.pack(pady=(0, 20))
        CreateToolTip(plot_button_2d, 
                     "2D Hertzprung-Russell plot of stars within the selected distance.")
        
        # SCALE OPTIONS FOR APPARENT MAGNITUDE (restored from old version)
        stellar_scale_frame = tk.LabelFrame(plot_controls_frame, 
                                           text="Scale Options for Apparent Magnitude 3D Plots")
        stellar_scale_frame.pack(pady=(0, 10), fill='x')
        
        self.stellar_scale_var = tk.StringVar(value='Auto')
        stellar_auto_scale = tk.Radiobutton(stellar_scale_frame, 
                                           text="Automatic Scaling",
                                           variable=self.stellar_scale_var, 
                                           value='Auto')
        stellar_auto_scale.pack(anchor='w')
        
        stellar_manual_scale = tk.Radiobutton(stellar_scale_frame, 
                                             text="Manual Scale (Light-Years):",
                                             variable=self.stellar_scale_var, 
                                             value='Manual')
        stellar_manual_scale.pack(anchor='w')
        
        self.stellar_scale_entry = tk.Entry(stellar_scale_frame, width=10)
        self.stellar_scale_entry.pack(pady=(0, 5))
        self.stellar_scale_entry.insert(0, '1400')
        
        CreateToolTip(stellar_auto_scale, 
                     "Automatically adjust scale based on the data range")
        CreateToolTip(stellar_manual_scale, 
                     "The range of the axes gets reduced to your input, "
                     "so visible objects beyond that range will not display.")
        
        def on_stellar_scale_change(*args):
            """Enable/disable scale entry based on selected mode"""
            self.stellar_scale_entry.config(
                state='normal' if self.stellar_scale_var.get() == 'Manual' else 'disabled'
            )
        
        self.stellar_scale_var.trace('w', on_stellar_scale_change)
        on_stellar_scale_change()
        
        # Magnitude controls
        mag_entry_label = tk.Label(plot_controls_frame, 
                                  text="Enter maximum apparent magnitude (-1.44 to 9):")
        mag_entry_label.pack(pady=(0, 5))
        
        self.mag_entry = tk.Entry(plot_controls_frame)
        self.mag_entry.pack(pady=(0, 10))
        self.mag_entry.insert(0, '4')
        
        # Add clipboard support to all entries
        for entry in [self.ly_entry, self.mag_entry, self.stellar_scale_entry]:
            self.star_search.add_clipboard_support(entry)
        
        # Magnitude-based buttons
        plot_button_3d_mag = tk.Button(
            plot_controls_frame,
            text="3D Visualization of Stars Visible Unaided",
            command=self.call_planetarium_apparent_magnitude_script,
            bg='SystemButtonFace',
            fg='blue',
            width=BUTTON_WIDTH,
            font=BUTTON_FONT
        )
        plot_button_3d_mag.pack(pady=(0, 10))
        CreateToolTip(plot_button_3d_mag, 
                     "Space, 8.5-9; perfect, 6.7-7.5; rural, 6.5; suburbs, 5-5.5; "
                     "urban, 4 or less; stars and non-stellar objects -- long load time.")
        
        plot_button_2d_mag = tk.Button(
            plot_controls_frame,
            text="2D Visualization of Stars Visible Unaided",
            command=self.call_hr_diagram_apparent_magnitude_script,
            bg='SystemButtonFace',
            fg='blue',
            width=BUTTON_WIDTH,
            font=BUTTON_FONT
        )
        plot_button_2d_mag.pack(pady=(0, 20))
        CreateToolTip(plot_button_2d_mag, 
                     "Space, 8.5-9; perfect, 6.7-7.5; rural, 6.5; suburbs, 5-5.5; "
                     "urban, 4 or less -- long load time.")
        
        # Status frame
        status_frame = tk.LabelFrame(plot_controls_frame, text="Output Messages")
        status_frame.pack(pady=(0, 10), fill='x')
        
        self.output_label = tk.Label(status_frame, text="", fg='red', wraplength=400)
        self.output_label.pack(pady=5)
        
        self.progress_bar = ttk.Progressbar(status_frame, orient='horizontal', 
                                           mode='indeterminate', length=300)
        self.progress_bar.pack(pady=5)
        
        # RIGHT COLUMN - Notes
        note_frame = ttk.Frame(self)
        note_frame.grid(row=0, column=2, padx=10, pady=10, sticky='nsew')
        
        note_label = tk.Label(note_frame, text="Note:", font=("Arial", 10, "normal"))
        note_label.pack(anchor='w', pady=(0, 5))
        
        note_text_widget = scrolledtext.ScrolledText(
            note_frame,
            wrap='word',
            width=44,
            height=44,
            bg='SystemButtonFace'
        )
        note_text_widget.pack(expand=True, fill='both')
        
        # Note text from old version
        note_text = """What's Paloma's Orrery?

Paloma's Orrery is an advanced astronomical visualization tool that transforms real NASA/ESA data into interactive 3D and 2D visualizations of the solar system and nearby stars! This model displays celestial objects and spacecraft in both stationary and animated plots over different time periods, using real-time data from NASA's Jet Propulsion Laboratory's Horizons System to plot actual positions. Complete idealized orbits of planets, asteroids, dwarf planets, and Kuiper belt objects are also calculated from their orbital parameters using Kepler's equations.

STELLAR NEIGHBORHOOD VISUALIZATION:
Explore our cosmic neighborhood in four different ways: by distance (light-years) or brightness (apparent magnitude), displayed in either 2D Hertzprung-Russell diagrams or immersive 3D spatial plots. Plot stars up to 100 light-years away to see the actual 3D structure and beginning shape of our galaxy!

DISTANCE MODE: See all stars within your selected distance from the Sun, revealing the true 3D structure of our local stellar neighborhood.
MAGNITUDE MODE: View stars by apparent brightness (how bright they appear to us), including distant luminous giants thousands of light-years away alongside nearby dim stars. At higher magnitudes, you'll begin to see the galaxy's shape and tilt!
Warning: Higher magnitudes fetch more stars and take longer to plot.

3D SPATIAL PLOTS: Experience stars in their actual 3D positions relative to the Sun. Use 'Move Camera to the Center' to view from the Sun's position and see familiar constellations like Orion with M42 (Orion Nebula)! Toggle between detailed hover information and star names only for clarity.

2D HERTZSPRUNG-RUSSELL DIAGRAMS: The classic scientific plot showing stellar luminosity vs. temperature, revealing stellar types and lifecycles. See main sequence stars, red giants, supergiants, and white dwarfs in their characteristic patterns."""
        
        note_text_widget.insert(tk.END, note_text)
        note_text_widget.config(state='disabled')

    def call_planetarium_distance_script(self):
        """Call the 3D distance visualization script."""
        try:
            ly_value = float(self.ly_entry.get())
            if ly_value <= 0:
                self.output_label.config(text="Please enter a positive number of light-years.")
                return
            if ly_value > 100.1:
                self.output_label.config(text="Please enter a number between 0.1 and 100.1 light-years.")
                return
            script_path = os.path.join(os.path.dirname(__file__), 'planetarium_distance.py')
            subprocess.run([sys.executable, script_path, str(ly_value)])
            self.output_label.config(text=f"Launched 3D plot ({ly_value} ly)")
        except ValueError:
            self.output_label.config(text="Please enter a valid number (e.g., 100 or 100.1)")
        except Exception as e:
            self.output_label.config(text=f"Error: {e}")

    def call_hr_diagram_distance_script(self):
        """Call the 2D HR diagram distance script."""
        try:
            ly_value = float(self.ly_entry.get())
            if ly_value <= 0:
                self.output_label.config(text="Please enter a positive number of light-years.")
                return
            if ly_value > 100.1:
                self.output_label.config(text="Please enter a number between 0.1 and 100.1 light-years.")
                return
            script_path = os.path.join(os.path.dirname(__file__), 'hr_diagram_distance.py')
            subprocess.run([sys.executable, script_path, str(ly_value)])
            self.output_label.config(text=f"Launched HR diagram ({ly_value} ly)")
        except ValueError:
            self.output_label.config(text="Please enter a valid number (e.g., 100 or 100.1)")
        except Exception as e:
            self.output_label.config(text=f"Error: {e}")

    def call_planetarium_apparent_magnitude_script(self):
        """Call the 3D magnitude visualization script with scale options."""
        try:
            mag_value = float(self.mag_entry.get())
            if mag_value < -1.44 or mag_value > 9:
                self.output_label.config(text="Please enter a magnitude between -1.44 and 9.")
                return
            
            # Get scale value if manual mode is selected
            user_scale = None
            if self.stellar_scale_var.get() == 'Manual':
                try:
                    user_scale = float(self.stellar_scale_entry.get())
                    if user_scale <= 0:
                        self.output_label.config(text="Please enter a positive scale value.")
                        return
                except ValueError:
                    self.output_label.config(text="Invalid scale value.")
                    return
            
            script_path = os.path.join(os.path.dirname(__file__), 'planetarium_apparent_magnitude.py')
            cmd = [sys.executable, script_path, str(mag_value)]
            if user_scale is not None:
                cmd.append(str(user_scale))
            
            print(f"Running command: {' '.join(cmd)}")
            subprocess.run(cmd)
            self.output_label.config(text=f"Launched 3D plot (mag {mag_value})")
            
        except ValueError:
            self.output_label.config(text="Please enter a valid magnitude between -1.44 and 9.")
        except Exception as e:
            self.output_label.config(text=f"Error: {e}")

    def call_hr_diagram_apparent_magnitude_script(self):
        """Call the 2D HR diagram magnitude script."""
        try:
            mag_value = float(self.mag_entry.get())
            if mag_value < -1.44 or mag_value > 9:
                self.output_label.config(text="Please enter a magnitude between -1.44 and 9.")
                return
            script_path = os.path.join(os.path.dirname(__file__), 'hr_diagram_apparent_magnitude.py')
            subprocess.run([sys.executable, script_path, str(mag_value)])
            self.output_label.config(text=f"Launched HR diagram (mag {mag_value})")
        except ValueError:
            self.output_label.config(text="Please enter a valid magnitude between -1.44 and 9.")
        except Exception as e:
            self.output_label.config(text=f"Error: {e}")

    def on_closing(self):
        """Handle cleanup when the window is closed."""
        try:
            if shutdown_handler:
                shutdown_handler.cleanup()
            # Clear any cached data
            if hasattr(self.star_search, 'star_loader'):
                self.star_search.star_loader.clear_cache()
        finally:
            self.destroy()


if __name__ == "__main__":
    app = StarVisualizationGUI()
    app.mainloop()
```

This merged version combines:
- **Three-column layout** from the old version
- **Scale options for magnitude plots** (fully restored with functionality)
- **CreateToolTip class** for helpful tooltips
- **LazyStarPropertiesLoader** for fast startup from new version
- **Enhanced search with info display** from new version
- **All button functionality** with proper error handling
- **Cleanup protocols** from both versions

The key restoration is the scale options frame which is now properly connected to the `call_planetarium_apparent_magnitude_script()` method, passing the scale value when in manual mode.

====================

Here are the specific revisions to add to your current version to restore the missing "Scale Options for Apparent Magnitude 3D Plots":

## 1. Add Scale Options Frame (in `StarVisualizationGUI.setup_ui()` method)

**Location:** After creating `magnitude_frame` and before the magnitude buttons (around line 910)

**Add this code:**
```python
# After line: magnitude_frame.pack(fill='x', pady=(0, 10))

# ADD: Scale options for magnitude visualization
scale_frame = ttk.LabelFrame(magnitude_frame, text="Scale Options", padding=5)
scale_frame.pack(fill='x', pady=(10, 0))

self.scale_var = tk.StringVar(value='Auto')
self.auto_scale_radio = ttk.Radiobutton(
    scale_frame, 
    text="Automatic Scaling",
    variable=self.scale_var, 
    value='Auto'
)
self.auto_scale_radio.pack(anchor='w')

self.manual_scale_radio = ttk.Radiobutton(
    scale_frame,
    text="Manual Scale (Light-Years):",
    variable=self.scale_var,
    value='Manual'
)
self.manual_scale_radio.pack(anchor='w')

self.scale_entry = ttk.Entry(scale_frame, width=20)
self.scale_entry.pack(fill='x', pady=(5, 0))
self.scale_entry.insert(0, '1400')

# Enable/disable scale entry based on selection
def on_scale_change(*args):
    self.scale_entry.config(
        state='normal' if self.scale_var.get() == 'Manual' else 'disabled'
    )

self.scale_var.trace('w', on_scale_change)
on_scale_change()  # Set initial state

# Then continue with existing magnitude entry label...
```

## 2. Modify `plot_3d_magnitude()` Method

**Location:** Replace the entire `plot_3d_magnitude()` method (around line 945)

**Replace with:**
```python
def plot_3d_magnitude(self):
    """Launch 3D magnitude visualization with scale options."""
    try:
        mag_value = float(self.mag_entry.get())
        if mag_value < -1.44 or mag_value > 9:
            self.status_label.config(text="Enter magnitude -1.44 to 9", foreground="red")
            return
        
        # Build command with magnitude
        script_path = os.path.join(os.path.dirname(__file__), 'planetarium_apparent_magnitude.py')
        cmd = [sys.executable, script_path, str(mag_value)]
        
        # ADD: Check for scale value if manual mode selected
        if hasattr(self, 'scale_var') and self.scale_var.get() == 'Manual':
            try:
                scale_value = float(self.scale_entry.get())
                if scale_value > 0:
                    cmd.append(str(scale_value))
                else:
                    self.status_label.config(text="Scale must be positive", foreground="red")
                    return
            except ValueError:
                self.status_label.config(text="Invalid scale value", foreground="red")
                return
        
        subprocess.run(cmd)
        
        # Update status with scale info if manual
        if hasattr(self, 'scale_var') and self.scale_var.get() == 'Manual':
            scale_value = float(self.scale_entry.get())
            self.status_label.config(text=f"Launched 3D plot (mag {mag_value}, scale {scale_value} ly)", foreground="green")
        else:
            self.status_label.config(text=f"Launched 3D plot (mag {mag_value}, auto scale)", foreground="green")
        
    except ValueError:
        self.status_label.config(text="Invalid magnitude value", foreground="red")
    except Exception as e:
        self.status_label.config(text=f"Error: {e}", foreground="red")
```

## 3. Optional: Add CreateToolTip Class (for better UX)

**Location:** At the top of the file, after imports

**Add:**
```python
class CreateToolTip(object):
    """Create a tooltip for a given widget."""
    def __init__(self, widget, text='widget info'):
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.tw = None

    def enter(self, event=None):
        self.showtip()

    def leave(self, event=None):
        self.hidetip()

    def showtip(self):
        if self.tw or not self.text:
            return
        x = self.widget.winfo_rootx() + 20
        y = self.widget.winfo_rooty() + self.widget.winfo_height() + 5
        self.tw = tk.Toplevel(self.widget)
        self.tw.wm_overrideredirect(True)
        label = tk.Label(self.tw, text=self.text, justify='left',
                        background='yellow', relief='solid', borderwidth=1,
                        font=("Arial", 10, "normal"))
        label.pack(ipadx=1)
        self.tw.wm_geometry(f"+{x}+{y}")

    def hidetip(self):
        if self.tw:
            self.tw.destroy()
        self.tw = None
```

Then add tooltips after creating the radio buttons:
```python
CreateToolTip(self.auto_scale_radio, "Automatically adjust scale based on data range")
CreateToolTip(self.manual_scale_radio, "Manually set axis range in light-years")
```

## 4. Fix Indentation Issue in `load_star_data()`

**Location:** Around line 250-270

**Fix:** The print summary block has incorrect indentation. It should be at the function level, not inside the for loop:

```python
    # This block should be at the same indentation as the for loop, not inside it
    # Print summary - FIXED INDENTATION
    print("\n" + "="*60)
    print("STAR DATA LOADING SUMMARY")
    print("="*60)
    print(f"Notable Stars: {len(self.star_data.get('Notable Stars', []))} stars")
    print(f"Stars by Distance: {len(self.star_data.get('Stars by Distance', []))} stars")  
    print(f"Stars by Magnitude: {len(self.star_data.get('Stars by Magnitude', []))} stars")
    print("="*60 + "\n")
```

These are the minimal changes needed to restore the scale options functionality while keeping all your current enhancements. The main additions are:
1. The scale options UI frame
2. Modified plot_3d_magnitude() to pass scale value
3. Optional tooltips for better UX
4. Fix for the indentation issue

==================

You're welcome! The changes should integrate smoothly since they're mostly restoring functionality that was already working in the original version. The key points to test:

1. The scale entry field should gray out when "Auto" is selected and become editable when "Manual" is selected
2. When running 3D magnitude visualization with manual scale, check that `planetarium_apparent_magnitude.py` receives the scale value as a second command-line argument
3. The indentation fix should make the GUI load faster since it won't be printing inside the loop

If you do encounter any issues, they'll likely be around:
- The scale value not being passed correctly (check the console output since we added `print(f"Running command: {' '.join(cmd)}")`)
- The on_scale_change callback not triggering (easy fix - just check the trace binding)

The rest of your enhancements (lazy loading, enhanced search, etc.) should continue working as before since we only added to the existing structure rather than modifying core functionality.

====================

Looking at your screenshot, I can see the Star Information field is quite constrained and there's unused vertical space. Here's how to fix it:

## Key Changes Needed:

### 1. **Increase Window Height**
In `StarVisualizationGUI.__init__()`:
```python
# Change from:
self.geometry("700x900")
# To:
self.geometry("1400x900")  # or even "1400x1000"
```

### 2. **Fix the Star Information Height**
In `StarVisualizationSearchWidget.setup_ui()`:
```python
self.info_display = tk.Text(
    text_frame,
    height=25,  # Increase from 12 to 25 or 30
    wrap='word',
    yscrollcommand=v_scroll.set,
    xscrollcommand=h_scroll.set,
    font=('Consolas', 10)
)
```

### 3. **Make the Information Frame Expand Properly**
In `StarVisualizationSearchWidget.setup_ui()`, ensure the info_frame expands:
```python
# The info_frame should have these settings:
info_frame = ttk.LabelFrame(main_frame, text="Star Information", padding=5)
info_frame.pack(fill='both', expand=True, padx=5, pady=5)  # expand=True is crucial
```

### 4. **Adjust the Notes Widget Height**
In the main GUI's `setup_ui()` method, find the notes text widget:
```python
note_text_widget = scrolledtext.ScrolledText(
    note_frame,
    wrap='word',
    width=44,
    height=35,  # Increase from current value (probably 44) to 35
    bg='SystemButtonFace'
)
```

### 5. **Configure Grid Weights for Proper Expansion**
If using grid layout, add these after creating the main window:
```python
# In StarVisualizationGUI.__init__() or setup_ui():
self.grid_rowconfigure(0, weight=1)  # Make row 0 expandable
self.grid_columnconfigure(0, weight=2)  # Give more weight to star search column
self.grid_columnconfigure(1, weight=1)  # Middle column
self.grid_columnconfigure(2, weight=1)  # Notes column
```

### 6. **For the Three-Column Layout Specifically**
If the search categories are taking too much space, reduce their listbox heights:
```python
listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set, height=3)  # Reduce from 5 to 3
```

This will give more room to the Star Information display below.

The main issue is likely that the parent frames aren't configured to expand to fill available space. The combination of increasing the window geometry and ensuring `expand=True` on the info_frame should solve it.

===================

Looking at your debug output and screenshot, I can see the issue clearly:

- **Window height**: 724 pixels (should be ~900 based on geometry setting)
- **Info display**: 456 pixels (not filling available space)
- **Lots of white space** below the Star Information field

## The Problems:

1. **Window not reaching full height** - You set geometry but it's only 724px tall
2. **Info frame not expanding** to fill available vertical space
3. **Search categories** taking fixed space even when empty

## Here's the fix:

### 1. **Force Window Size**
```python
# In StarVisualizationGUI.__init__():
self.geometry("1400x900")
self.minsize(1400, 900)  # Add this to enforce minimum size
self.update_idletasks()   # Force geometry update
```

### 2. **Fix the Pack Weights in StarVisualizationSearchWidget**
In `setup_ui()` method, change how frames are packed:

```python
# For each category frame, use fixed height:
for category in categories:
    category_frame = ttk.LabelFrame(main_frame, text=category, padding=5)
    category_frame.pack(fill='x', padx=5, pady=5, anchor='n')  # Add anchor='n'
    # Don't let these expand vertically

# For the info_frame, make it expand to fill remaining space:
info_frame = ttk.LabelFrame(main_frame, text="Star Information", padding=5)
info_frame.pack(fill='both', expand=True, padx=5, pady=5)  # expand=True is crucial

# Make sure text_frame also expands:
text_frame = ttk.Frame(info_frame)
text_frame.pack(fill='both', expand=True)  # Must have expand=True

# And the text widget:
self.info_display = tk.Text(
    text_frame,
    height=25,  # This is minimum/preferred height
    wrap='word',
    # ... other params
)
self.info_display.pack(fill='both', expand=True)  # Must have expand=True
```

### 3. **Configure Main Frame to Expand**
Add this right after creating `main_frame`:
```python
main_frame = ttk.Frame(self)
main_frame.pack(fill='both', expand=True, padx=5, pady=5)
main_frame.pack_propagate(False)  # Prevent shrinking
```

### 4. **Alternative: Use Grid with Weights**
If pack isn't working, switch to grid:
```python
# Set up grid weights for main_frame
main_frame.grid_rowconfigure(3, weight=1)  # Info frame row gets all extra space
main_frame.grid_columnconfigure(0, weight=1)

# Then place items with grid:
row = 0
for category in categories:
    category_frame = ttk.LabelFrame(main_frame, text=category, padding=5)
    category_frame.grid(row=row, column=0, sticky='ew', padx=5, pady=5)
    row += 1

# Separator
ttk.Separator(main_frame, orient='horizontal').grid(row=row, column=0, sticky='ew', pady=10)
row += 1

# Info frame gets remaining space
info_frame = ttk.LabelFrame(main_frame, text="Star Information", padding=5)
info_frame.grid(row=row, column=0, sticky='nsew', padx=5, pady=5)  # sticky='nsew' for full expansion
```

The key issue is that the packing manager isn't being told to expand the info_frame to fill available space. The `expand=True` parameter is crucial for the info_frame and all its children.