#Paloma's Orrery - Solar System Visualization Tool

# Import necessary libraries
import tkinter as tk
from tkinter import ttk
from astroquery.jplhorizons import Horizons
import numpy as np
from datetime import datetime, timedelta
import calendar
import plotly.graph_objs as go
import webbrowser
import os
import warnings
from astropy.utils.exceptions import ErfaWarning
from astropy.time import Time
import traceback
from tkinter import scrolledtext
import threading
import time  # Used here for simulation purposes
import subprocess
import sys
import math
import pickle
import re
from typing import Dict, List, Optional

from constants import (
    planetary_params,
    parent_planets,
    color_map,
    note_text,
    INFO,
    hover_text_sun_and_corona,
    gravitational_influence_info,
    outer_oort_info,
    inner_oort_info,
    inner_limit_oort_info,
    solar_wind_info,
    termination_shock_info,
    outer_corona_info,
    inner_corona_info,
    chromosphere_info,
    photosphere_info,
    radiative_zone_info,
    core_info,
    CENTER_BODY_RADII,
    KM_PER_AU, 
    LIGHT_MINUTES_PER_AU
)

from star_notes import unique_notes

from visualization_utils import format_hover_text, add_hover_toggle_buttons

from save_utils import save_plot

# At the very top of the file, after imports:
from shutdown_handler import PlotlyShutdownHandler, create_monitored_thread, show_figure_safely

import sys, os          # troubleshooting VS
print("Interpreter:", sys.executable)
print("Working directory:", os.getcwd())

# Create a global shutdown handler instance
shutdown_handler = PlotlyShutdownHandler()

# Suppress ErfaWarning messages
warnings.simplefilter('ignore', ErfaWarning)

# Initialize the main window
root = tk.Tk()
root.title("Star Visualization -- Updated: February 22, 2025")
# Define 'today' once after initializing the main window
today = datetime.today()
# root.configure(bg="lightblue")  # Set the background color of the root window

# Define a standard font and button width
BUTTON_FONT = ("Arial", 10, "normal")  # You can adjust the font as needed
BUTTON_WIDTH = 30  # Number of characters wide

DEFAULT_MARKER_SIZE = 6
HORIZONS_MAX_DATE = datetime(2199, 12, 29, 0, 0, 0)
CENTER_MARKER_SIZE = 10  # For central objects like the Sun

# Constants
LIGHT_MINUTES_PER_AU = 8.3167  # Approximate light-minutes per Astronomical Unit
KM_PER_AU = 149597870.7       # Kilometers per Astronomical Unit
CORE_AU = 0.00093               # Core in AU, or approximately 0.2 Solar radii
RADIATIVE_ZONE_AU = 0.00325     # Radiative zone in AU, or approximately 0.7 Solar radii
SOLAR_RADIUS_AU = 0.00465047  # Sun's radius in AU
INNER_LIMIT_OORT_CLOUD_AU = 2000   # Inner Oort cloud inner boundary in AU.
INNER_OORT_CLOUD_AU = 20000   # Inner Oort cloud outer boundary in AU.
OUTER_OORT_CLOUD_AU = 100000   # Oort cloud outer boundary in AU.
GRAVITATIONAL_INFLUENCE_AU = 126000   # Sun's gravitational influence in AU.
CHROMOSPHERE_RADII = 1.5    # The Chromosphere extends from about 1 to 1.5 solar radii or about 0.00465 - 0.0070 AU
INNER_CORONA_RADII = 3  # Inner corona extends to 2 to 3 solar radii or about 0.01 AU
OUTER_CORONA_RADII = 50       # Outer corona extends up to 50 solar radii or about 0.2 AU, more typically 10 to 20 solar radii
TERMINATION_SHOCK_AU = 94       # Termination shock where the solar wind slows to subsonic speeds. 
HELIOPAUSE_RADII = 26449         # Outer boundary of the solar wind and solar system, about 123 AU. 
PARKER_CLOSEST_RADII = 8.2    # Parker's closest approach was 3.8 million miles on 12-24-24 at 6:53 AM EST (0.41 AU, 8.2 solar radii)

# Custom Tooltip Class

class CreateToolTip(object):
    """
    Create a tooltip for a given widget with intelligent positioning to prevent clipping.
    """

    def __init__(self, widget, text='widget info'):
        self.waittime = 500     # milliseconds
        self.wraplength = 1000   # Reduced wraplength
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
            # Get screen dimensions and taskbar height (estimated)
            screen_width = self.widget.winfo_screenwidth()
            screen_height = self.widget.winfo_screenheight()
            taskbar_height = 40  # Estimated Windows taskbar height

            # Create the tooltip window
            self.tw = tk.Toplevel(self.widget)
            self.tw.wm_overrideredirect(True)
            
            # Calculate usable screen height
            usable_height = screen_height - taskbar_height

            # Create the tooltip label
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

            # Update the window to calculate its size
            self.tw.update_idletasks()
            tooltip_width = self.tw.winfo_width()
            tooltip_height = self.tw.winfo_height()

            # Initial x position - try positioning to the right of the widget first
            x = self.widget.winfo_rootx() + self.widget.winfo_width() + 5

            # If tooltip would extend beyond right edge, try positioning to the left of the widget
            if x + tooltip_width > screen_width:
                x = self.widget.winfo_rootx() - tooltip_width - 5

            # If that would push it off the left edge, position at left screen edge with padding
            if x < 0:
                x = 5

            # Calculate vertical position
            y = self.widget.winfo_rooty()

            # If tooltip is taller than available space, position at top of screen
            if tooltip_height > usable_height:
                y = 5  # Small padding from top
            else:
                # Center vertically relative to widget if space allows
                widget_center = y + (self.widget.winfo_height() / 2)
                y = widget_center - (tooltip_height / 2)
                
                # Ensure tooltip doesn't go below usable screen area
                if y + tooltip_height > usable_height:
                    y = usable_height - tooltip_height - 5

                # Ensure tooltip doesn't go above top of screen
                if y < 5:
                    y = 5

            # Position the tooltip
            self.tw.wm_geometry(f"+{int(x)}+{int(y)}")

        except Exception as e:
            print(f"Error showing tooltip: {e}")
            traceback.print_exc()

    def hidetip(self):
        if self.tw:
            self.tw.destroy()
        self.tw = None

class StarSearchFrame(ttk.Frame):
    """Frame containing star search functionality."""
    
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        
        # Initialize search states
        self.search_results: Dict[str, List[str]] = {
            "Notable Stars": [],
            "Stars by Distance": [],
            "Stars by Magnitude": []
        }
        
        self.create_widgets()
        self.load_star_data()

    def create_widgets(self):
        """Create the search widgets for each category."""
        # Main label
        ttk.Label(
            self,
            text="(Ctrl+C for copy, Ctrl+X for cut, Ctrl+V for paste)",
        ).pack(pady=(0, 10))

        # Create search boxes for each category
        self.search_frames = {}
        self.search_vars = {}
        self.search_entries = {}
        self.result_listboxes = {}
        
        categories = ["Notable Stars", "Stars by Distance", "Stars by Magnitude"]
        
        for category in categories:
            # Create frame for this category
            frame = ttk.LabelFrame(self, text=category)
            frame.pack(fill='x', padx=5, pady=5)
            self.search_frames[category] = frame
            
            # Create and bind search variable
            search_var = tk.StringVar()
            search_var.trace_add('write', lambda *args, c=category: self.on_search_change(c))
            self.search_vars[category] = search_var
            
            # Create search entry
            entry = ttk.Entry(frame, textvariable=search_var)
            entry.pack(fill='x', padx=5, pady=5)
            self.search_entries[category] = entry
            
            # Create results listbox with scrollbar
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
            
            # Bind selection event
            listbox.bind('<<ListboxSelect>>', 
                        lambda e, c=category: self.on_select(c))
            
            # Add right-click menu for copy
            self.create_right_click_menu(listbox)            
            self.result_listboxes[category] = listbox

            # Add URL display for Notable Stars
            if category == "Notable Stars":
                # Create URL display frame
                url_frame = ttk.Frame(frame)
                url_frame.pack(fill='x', padx=5, pady=(0, 5))
                
                url_label = ttk.Label(url_frame, text="Associated URL:")
                url_label.pack(anchor='w')
                
                # Create URL text widget with scrollbar
                url_scroll = ttk.Scrollbar(url_frame, orient='horizontal')
                url_scroll.pack(side='bottom', fill='x')
                
                self.url_display = tk.Text(
                    url_frame,
                    height=2,
                    wrap='none',
                    xscrollcommand=url_scroll.set
                )
                self.url_display.pack(fill='x', expand=True)
                url_scroll.config(command=self.url_display.xview)
                
                # Add clipboard support to URL display
                add_clipboard_support(self.url_display)

    def extract_url(self, star_name):
        """Extract URL from star notes if it exists."""
        print(f"Extracting URL for star: {star_name}")  # Debug print
        note = unique_notes.get(star_name, "")
        print(f"Found note: {note[:100]}...")  # Debug print first 100 chars
        
        if note:
            # Look for URLs in HTML anchor tags
            url_match = re.search(r'<a href="([^"]+)">', note)
            if url_match:
                url = url_match.group(1)
                print(f"Found URL: {url}")  # Debug print
                return url
            else:
                print("No URL found in note")  # Debug print
        return ""

    def on_select(self, category: str):
        """Handle selection from results listbox."""
        print(f"\nSelection made in category: {category}")  # Debug print
        listbox = self.result_listboxes[category]
        try:
            selection = listbox.get(listbox.curselection())
            print(f"Selected item: {selection}")  # Debug print
            
            if selection:
                # Copy selection to entry
                self.search_vars[category].set(selection)
                # Clear listbox
                listbox.delete(0, tk.END)
                
                # Update URL display for Notable Stars
                if category == "Notable Stars":
                    print("Processing Notable Stars selection")  # Debug print
                    url = self.extract_url(selection)
                    if hasattr(self, 'url_display'):
                        print("URL display widget exists")  # Debug print
                        self.url_display.delete('1.0', tk.END)
                        if url:
                            print(f"Inserting URL: {url}")  # Debug print
                            self.url_display.insert('1.0', url)
                        else:
                            print("No URL to display")  # Debug print
                    else:
                        print("ERROR: URL display widget not found")  # Debug print
                        
        except Exception as e:
            print(f"Error in on_select: {e}")  # Debug print
            traceback.print_exc()  # Print full traceback for debugging

    def create_right_click_menu(self, listbox):
        """Create right-click context menu for copying."""
        menu = tk.Menu(self, tearoff=0)
        menu.add_command(label="Copy", 
                        command=lambda: self.copy_selection(listbox))
        
        # Bind right-click to show menu
        listbox.bind("<Button-3>", 
                    lambda e: self.show_menu(e, menu))
        
        # Also bind Ctrl+C for copy
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

    def load_star_data(self):
        """Load star data from files."""
        self.star_data = {
            "Notable Stars": self.load_notable_stars(),
            "Stars by Distance": self.load_pkl_stars('star_properties_distance.pkl'),
            "Stars by Magnitude": self.load_pkl_stars('star_properties_magnitude.pkl')
        }

    def load_notable_stars(self) -> List[str]:
        """Load notable stars from star_notes."""
        try:
            return sorted(unique_notes.keys())
        except Exception as e:
            print(f"Error loading notable stars: {e}")
            return []

#    def load_notable_stars(self) -> List[str]:
#        """Load notable stars from star_notes.py."""
#        try:
#            with open('star_notes.py', 'r') as f:
#                content = f.read()
#            # Extract star names from the dictionary structure
#            matches = re.findall(r"'([^']+)':\s*'<br>", content)
#            return sorted(matches)
#        except Exception as e:
#            print(f"Error loading notable stars: {e}")
#            return []

    def load_pkl_stars(self, filename: str) -> List[str]:
        """Load star names from pickle files."""
        try:
            with open(filename, 'rb') as f:
                data = pickle.load(f)
            return sorted(data.get('star_names', []))
        except Exception as e:
            print(f"Error loading {filename}: {e}")
            return []

    def on_search_change(self, category: str):
        """Handle changes in search entry."""
        search_term = self.search_vars[category].get().lower()
        listbox = self.result_listboxes[category]
        
        # Clear current results
        listbox.delete(0, tk.END)
        
        if not search_term:
            return
            
        # Filter and display matching stars
        matches = [
            star for star in self.star_data[category]
            if search_term in star.lower()
        ]
        
        # Update listbox with matches
        for star in matches[:50]:  # Limit to 50 results
            listbox.insert(tk.END, star)

    def get_selected_stars(self) -> Dict[str, Optional[str]]:
        """Get currently selected stars for each category."""
        return {
            category: self.search_vars[category].get()
            for category in self.search_vars
        }

def add_clipboard_support(entry_widget):
    """Add copy/paste/cut support to an entry widget."""
    
    def copy(event=None):
        """Copy selected text to clipboard."""
        try:
            selection = entry_widget.selection_get()
            entry_widget.clipboard_clear()
            entry_widget.clipboard_append(selection)
        except:
            pass  # No selection
        return "break"
    
    def cut(event=None):
        """Cut selected text to clipboard."""
        try:
            copy()
            entry_widget.delete("sel.first", "sel.last")
        except:
            pass  # No selection
        return "break"
    
    def paste(event=None):
        """Paste clipboard content at cursor position or over selection."""
        try:
            # Get clipboard content
            text = entry_widget.clipboard_get()
            # If there's a selection, delete it first
            try:
                entry_widget.delete("sel.first", "sel.last")
            except:
                pass  # No selection
            # Insert clipboard content
            entry_widget.insert("insert", text)
        except:
            pass  # Empty clipboard or invalid content
        return "break"

    # Bind standard keyboard shortcuts
    entry_widget.bind('<Control-c>', copy)
    entry_widget.bind('<Control-x>', cut)
    entry_widget.bind('<Control-v>', paste)
    
    # Create right-click menu
    menu = tk.Menu(entry_widget, tearoff=0)
    menu.add_command(label="Cut", command=cut)
    menu.add_command(label="Copy", command=copy)
    menu.add_command(label="Paste", command=paste)
    
    def show_menu(event):
        menu.post(event.x_root, event.y_root)
        return "break"
    
    # Bind right-click to show menu
    entry_widget.bind('<Button-3>', show_menu)


# Function to integrate the search frame into the main GUI
def add_star_search_to_gui(root: tk.Tk) -> StarSearchFrame:
    """Add star search functionality to the main GUI."""
    # Create a new frame for the star search
    search_frame = ttk.LabelFrame(root, text="Star Search")
    search_frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
    
    # Create and return the StarSearchFrame
    return StarSearchFrame(search_frame)

class ScrollableFrame(tk.Frame):
    """
    A scrollable frame that can contain multiple widgets with a vertical scrollbar.
    """
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        # Canvas and Scrollbar
        self.canvas = tk.Canvas(self, bg='SystemButtonFace')
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set) 

        # Layout
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Scrollable Frame
        self.scrollable_frame = tk.Frame(self.canvas, bg='SystemButtonFace')
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Bind mousewheel to the canvas
        self.canvas.bind("<Enter>", self._on_enter)
        self.canvas.bind("<Leave>", self._on_leave)

        # Update scroll region when the canvas size changes
        self.canvas.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

    def _on_mousewheel(self, event):
        if event.delta:
            self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        elif event.num == 4:
            self.canvas.yview_scroll(-1, "units")
        elif event.num == 5:
            self.canvas.yview_scroll(1, "units")

    def _on_enter(self, event):
        # Bind the mousewheel events
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        self.canvas.bind_all("<Button-4>", self._on_mousewheel)  # Linux
        self.canvas.bind_all("<Button-5>", self._on_mousewheel)  # Linux

    def _on_leave(self, event):
        # Unbind mousewheel events
        self.canvas.unbind_all("<MouseWheel>")
        self.canvas.unbind_all("<Button-4>")
        self.canvas.unbind_all("<Button-5>")   

    def _on_enter(self, event):
        # Bind the mouse wheel events when the cursor enters a widget
        event.widget.bind_all("<MouseWheel>", self._on_mousewheel)
        event.widget.bind_all("<Button-4>", self._on_mousewheel)
        event.widget.bind_all("<Button-5>", self._on_mousewheel)

    def _on_leave(self, event):
        # Unbind the mouse wheel events when the cursor leaves a widget
        event.widget.unbind_all("<MouseWheel>")
        event.widget.unbind_all("<Button-4>")
        event.widget.unbind_all("<Button-5>")


# Update grid configuration for three-column layout
root.grid_rowconfigure(0, weight=1)  # Main content row
root.grid_columnconfigure(0, weight=1)  # Star search column
root.grid_columnconfigure(1, weight=1)  # Plot controls column
root.grid_columnconfigure(2, weight=1)  # Note column

# Create and position search frame in left column
search_frame = ttk.LabelFrame(root, text="Star Search")
search_frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

# Initialize the star search
star_search = StarSearchFrame(search_frame)
star_search.pack(fill='both', expand=True)


# Position controls_frame below input_frame
controls_frame = tk.Frame(root)
controls_frame.grid(row=2, column=0, padx=(5, 10), pady=(0, 10), sticky='n')  # Moved to row 2

# Position note_frame to stretch full height
note_frame = tk.Frame(root)
note_frame.grid(row=0, column=2, rowspan=3, padx=(5, 10), pady=(10, 10), sticky='nsew')  # Added rowspan=3 and sticky='nsew'



def get_default_camera():
    """Return the default orthographic camera settings for top-down view"""
    return {
        "projection": {
            "type": "orthographic"
        },
        # Looking straight down the z-axis
        "eye": {"x": 0, "y": 0, "z": 1},  # Position above the x-y plane
        "center": {"x": 0, "y": 0, "z": 0},  # Looking at origin
        "up": {"x": 0, "y": 1, "z": 0}  # "Up" direction aligned with y-axis
    }



def format_maybe_float(value):
    """
    If 'value' is a numeric type (int or float), return it formatted
    with 10 decimal places. Otherwise, return 'N/A'.
    """
    if isinstance(value, (int, float)):
        return f"{value:.10f}"
    return "N/A"

def format_km_float(value):
    """
    Format kilometer values in scientific notation with 2 decimal places.
    """
    if isinstance(value, (int, float)):
        return f"{value:.10e}"              # using .10e for scientific notation instead of .10f
    return "N/A"


def on_closing():
    """Handle cleanup when the main window is closed."""
    try:
        # Attempt to remove any temporary files
        temp_files = ["palomas_orrery.html", "palomas_orrery_animation.html"]
        for temp_file in temp_files:
            try:
                if os.path.exists(temp_file):
                    os.remove(temp_file)
            except:
                pass
    finally:
        root.destroy()

# Add the closing protocol to the root window
root.protocol("WM_DELETE_WINDOW", on_closing)

    
# Get the script's saved date for version control
script_saved_date = datetime.now().strftime("%Y-%m-%d")

# Exception handling for Tkinter
# def report_callback_exception(self, exc, val, tb):
def report_callback_exception(self, exc_type, exc_value, exc_traceback):
    print('Exception in Tkinter callback')
    traceback.print_exception(exc_type, exc_value, exc_traceback)

root.report_callback_exception = report_callback_exception

# Configure grid weights for responsive design
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

input_frame = tk.Frame(root)
input_frame.grid(row=0, column=0, padx=(10, 5), pady=(10, 10), sticky='n')

# Configure grid weights within input_frame for proper spacing
input_frame.grid_rowconfigure(0, weight=0)  # Row for date inputs
input_frame.grid_rowconfigure(1, weight=1)  # Row for __frame
for col in range(0, 9):
    input_frame.grid_columnconfigure(col, weight=1)  # Allow columns to expand if needed


# Create middle column frame for plot controls
plot_controls_frame = ttk.Frame(root)
plot_controls_frame.grid(row=0, column=1, padx=10, pady=10, sticky='n')

# Move light year entry and button to middle column
ly_entry_label = tk.Label(plot_controls_frame, text="Enter number of light-years to plot up to 100:")
ly_entry_label.pack(pady=(0, 5))

ly_entry = tk.Entry(plot_controls_frame)
ly_entry.pack(pady=(0, 10))
ly_entry.insert(0, '20')  # Default ly value


# Function to call the planetarium_distance script with user input
def call_planetarium_distance_script_with_input():
    try:
        ly_value = ly_entry.get()
        ly_value = int(ly_value)
        if ly_value <= 0:
            output_label.config(text="Please enter a positive number of light-years.")
            return
        script_path = os.path.join(os.path.dirname(__file__), 'planetarium_distance.py')
        # Pass the light-years value as a command-line argument
        subprocess.run(['python', script_path, str(ly_value)])
    except ValueError:
        output_label.config(text="Please enter the number of light-years to plot, up to 100.")
    except Exception as e:
        output_label.config(text=f"Error running planetarium_distance.py: {e}")
        print(f"Error running planetarium_distance.py: {e}")

# Add plot buttons to middle column
plot_button_3d = tk.Button(
    plot_controls_frame,
    text="3D Visualization of Stellar Neighborhood",
    command=call_planetarium_distance_script_with_input,
    bg='SystemButtonFace',
    fg='blue',
    width=BUTTON_WIDTH,
    font=BUTTON_FONT
)
plot_button_3d.pack(pady=(0, 10))

CreateToolTip(plot_button_3d, "3D plot of stars within the selected distance from the Sun.")

# Function to call the hr_diagram script with user input
def call_hr_diagram_distance_script_with_input():
    try:
        mag_value = ly_entry.get()
        mag_value = int(mag_value)
        if mag_value <= 0:
            output_label.config(text="Please enter a positive number of light-years.")
            return
        script_path = os.path.join(os.path.dirname(__file__), 'hr_diagram_distance.py')
        # Pass the light-years value as a command-line argument
        subprocess.run(['python', script_path, str(mag_value)])
    except ValueError:
        output_label.config(text="Please enter the number of light-years to plot, up to 100.")
    except Exception as e:
        output_label.config(text=f"Error running hr_diagram_distance.py: {e}")
        print(f"Error running hr_diagram_distance.py: {e}")

plot_button_2d = tk.Button(
    plot_controls_frame,
    text="2D Visualization of Stellar Neighborhood",
    command=call_hr_diagram_distance_script_with_input,
    bg='SystemButtonFace',
    fg='blue',
    width=BUTTON_WIDTH,
    font=BUTTON_FONT
)
plot_button_2d.pack(pady=(0, 20))

CreateToolTip(plot_button_2d, "2D Hertzprung-Russell plot of stars within the selected distance from the Sun.")


# Add scale options frame
stellar_scale_frame = tk.LabelFrame(plot_controls_frame, text="Scale Options for Apparent Magnitude 3D Plots")
stellar_scale_frame.pack(pady=(0, 10), fill='x')

# Scale options remain the same, just moved to middle column
stellar_scale_var = tk.StringVar(value='Auto')
stellar_auto_scale = tk.Radiobutton(stellar_scale_frame, text="Automatic Scaling", 
                                   variable=stellar_scale_var, value='Auto')
stellar_auto_scale.pack(anchor='w')

stellar_manual_scale = tk.Radiobutton(stellar_scale_frame, text="Manual Scale (Light-Years):", 
                                     variable=stellar_scale_var, value='Manual')
stellar_manual_scale.pack(anchor='w')

stellar_scale_entry = tk.Entry(stellar_scale_frame, width=10)
stellar_scale_entry.pack(pady=(0, 5))
stellar_scale_entry.insert(0, '1400')


CreateToolTip(stellar_auto_scale, "Automatically adjust scale based on the data range")

CreateToolTip(stellar_manual_scale, "The range of the axes gets reduced to your input, so visible objects beyond that range will not display. ")

def on_stellar_scale_change(*args):
    """Enable/disable scale entry based on selected mode"""
    stellar_scale_entry.config(state='normal' if stellar_scale_var.get() == 'Manual' else 'disabled')

# Bind the scale variable to the callback
stellar_scale_var.trace('w', on_stellar_scale_change)

# Initial state setup
on_stellar_scale_change()

# Add magnitude controls
mag_entry_label = tk.Label(plot_controls_frame, text="Enter maximum apparent magnitude (-1.44 to 9):")
mag_entry_label.pack(pady=(0, 5))

mag_entry = tk.Entry(plot_controls_frame)
mag_entry.pack(pady=(0, 10))
mag_entry.insert(0, '4')  # Default magnitude value

# After creating entry widgets, add clipboard support:
for entry in [ly_entry, mag_entry, stellar_scale_entry]:
    add_clipboard_support(entry)

def call_planetarium_apparent_magnitude_script_with_input():
    try:
        mag_value = mag_entry.get()
        mag_value = float(mag_value)
        if mag_value < -1.44 or mag_value > 9:
            output_label.config(text="Please enter a magnitude between -1.44 and 9.")
            return
            
        # Get scale value if manual mode is selected
        user_scale = None
        if stellar_scale_var.get() == 'Manual':
            try:
                user_scale = float(stellar_scale_entry.get())
                if user_scale <= 0:
                    output_label.config(text="Please enter a positive scale value.")
                    return
            except ValueError:
                output_label.config(text="Invalid scale value.")
                return
                
        script_path = os.path.join(os.path.dirname(__file__), 'planetarium_apparent_magnitude.py')
        # Pass magnitude value as command-line argument
        cmd = ['python', script_path, str(mag_value)]
        if user_scale is not None:
            cmd.append(str(user_scale))
            
        print(f"Running command: {' '.join(cmd)}")  # Debug print
        subprocess.run(cmd)
        
    except ValueError:
        output_label.config(text="Please enter a valid magnitude between -1.44 (brightest star Sirius) and 9.")
    except Exception as e:
        output_label.config(text=f"Error running planetarium_apparent_magnitude.py: {e}")
        print(f"Error running planetarium_apparent_magnitude.py: {e}")
        traceback.print_exc()  # Add this for more detailed error info

plot_button = tk.Button(
    plot_controls_frame,  # Use plot_controls_frame as the parent
    text="3D Visualization of Stars Visible Unaided",
    command=call_planetarium_apparent_magnitude_script_with_input,
    bg='SystemButtonFace',
    fg='blue',
    width=BUTTON_WIDTH,
    font=BUTTON_FONT
)

# Change the grid placement to pack since we're using plot_controls_frame
plot_button.pack(pady=(0, 10))
CreateToolTip(plot_button, "Space, 8.5-9; perfect, 6.7-7.5; rural, 6.5; suburbs, 5-5.5; urban, 4 or less; stars and non-stellar objects " 
              "-- long load time.")


# Function to call the hr_diagram script with user input

def call_hr_diagram_apparent_magnitude_script_with_input():
    try:
        mag_value = mag_entry.get()
        mag_value = float(mag_value)
        if mag_value < -1.44 or mag_value > 9:
            output_label.config(text="Please enter a magnitude between -1.44 (brightest star Sirius) and 9. (ideal visibility and vision limit).")
            return
        script_path = os.path.join(os.path.dirname(__file__), 'hr_diagram_apparent_magnitude.py')
        # Pass the magnitude value as a command-line argument
        subprocess.run(['python', script_path, str(mag_value)])
    except ValueError:
        output_label.config(text="Please enter a valid magnitude between -1.44 (brightest star Sirius) and 9 (ideal visibility and vision limit).")
    except Exception as e:
        output_label.config(text=f"Error running hr_diagram_apparent_magnitude.py: {e}")
        print(f"Error running hr_diagram_apparent_magnitude.py: {e}")

plot_button_2d_mag = tk.Button(
    plot_controls_frame,
    text="2D Visualization of Stars Visible Unaided",
    command=call_hr_diagram_apparent_magnitude_script_with_input,
    bg='SystemButtonFace',
    fg='blue',
    width=BUTTON_WIDTH,
    font=BUTTON_FONT
)
plot_button_2d_mag.pack(pady=(0, 20))

CreateToolTip(plot_button_2d_mag, "Space, 8.5-9; perfect, 6.7-7.5; rural, 6.5; suburbs, 5-5.5; urban, 4 or less -- long load time.")

# Status frame remains at bottom of middle column
status_frame = tk.LabelFrame(plot_controls_frame, text="Output Errors")
status_frame.pack(pady=(0, 10), fill='x')

output_label = tk.Label(status_frame, text="", fg='red', wraplength=400)
output_label.pack(pady=5)

progress_bar = ttk.Progressbar(status_frame, orient='horizontal', mode='indeterminate', length=300)
progress_bar.pack(pady=5)


# Note frame remains in right column
note_frame = ttk.Frame(root)
note_frame.grid(row=0, column=2, padx=10, pady=10, sticky='nsew')

note_label = tk.Label(note_frame, text="Note:", font=("Arial", 10, "normal"))
note_label.pack(anchor='w', pady=(0, 5))

note_text_widget = scrolledtext.ScrolledText(
    note_frame,
    wrap='word',
    width=44,
    height=44.5,
    bg='SystemButtonFace'
)
note_text_widget.pack(expand=True, fill='both')
note_text_widget.insert(tk.END, note_text)
note_text_widget.config(state='disabled')


# Run the Tkinter main loop
root.mainloop()
