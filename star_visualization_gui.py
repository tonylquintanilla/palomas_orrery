# star_visualization_gui.py - Final version with enhanced pickle file support
# This GUI reads the enhanced pickle files that contain both raw and calculated data
# 
# UPDATED: November 28, 2025 - Added PyInstaller frozen executable support
# When running as exe, plotting modules are called directly instead of via subprocess

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
from star_notes import unique_notes
import time
import json
import platform
from threading import Thread

# Import for expanding object types if needed
from constants_new import object_type_mapping, class_mapping, stellar_class_labels
from plot_data_report_widget import PlotDataReportWidget
from plot_data_exchange import PlotDataExchange
from report_manager import ReportManager


# ============================================================
# PyInstaller Support - Detect frozen executable
# ============================================================

def is_frozen():
    """Check if running as a PyInstaller frozen executable."""
    return getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS')

# Set working directory to script location (works for both Python and frozen exe)
# This ensures relative paths (star_data/, reports/, etc.) work correctly
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
print(f"Working directory set to: {os.getcwd()}")

# Import plotting modules for frozen exe (can't use subprocess)
if is_frozen():
    try:
        import hr_diagram_distance
        import hr_diagram_apparent_magnitude  
        import planetarium_distance
        import planetarium_apparent_magnitude
        PLOTTING_MODULES_AVAILABLE = True
        print("Plotting modules loaded for frozen executable")
    except ImportError as e:
        print(f"Warning: Could not import plotting modules: {e}")
        PLOTTING_MODULES_AVAILABLE = False
else:
    PLOTTING_MODULES_AVAILABLE = False


class ScrollableFrame(ttk.Frame):
    """A scrollable frame widget."""
    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)
        canvas = tk.Canvas(self, highlightthickness=0)
        vbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.container = ttk.Frame(canvas)
        self.container.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=self.container, anchor="nw")
        canvas.configure(yscrollcommand=vbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        vbar.pack(side="right", fill="y")
        
        # Optional: mousewheel support
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)

class LazyStarPropertiesLoader:
    """Loads star properties on-demand rather than all at startup."""
    
    def __init__(self):
        self.loaded_properties = {}
        self.property_files = {
            'distance': 'star_data/star_properties_distance.pkl',
            'magnitude': 'star_data/star_properties_magnitude.pkl',
            'notable': 'star_data/star_properties.pkl'
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
            
            # Convert to consistent format
            if isinstance(data, list):
                properties = {}
                for item in data:
                    if isinstance(item, dict) and 'unique_id' in item:
                        properties[item['unique_id']] = item
            elif isinstance(data, dict):
                properties = data
            else:
                properties = {}
            
            # Cache for future use
            self.loaded_properties[property_type] = properties
            print(f"  Loaded {len(properties)} stars from {filename}")
            return properties
            
        except Exception as e:
            print(f"Error loading {filename}: {e}")
            return {}
    
    def get_star_count(self, property_type='distance'):
        """Get count without loading data."""
        if property_type in self.loaded_properties:
            return len(self.loaded_properties[property_type])
        
        # For quick GUI display, return estimate based on file size
        if property_type in self.file_stats and self.file_stats[property_type]['exists']:
            # Rough estimate: ~100 bytes per star
            size_bytes = self.file_stats[property_type]['size_mb'] * 1024 * 1024
            return int(size_bytes / 100)
        return 0
    
    def clear_cache(self, property_type=None):
        """Clear cached data to free memory."""
        if property_type:
            if property_type in self.loaded_properties:
                del self.loaded_properties[property_type]
                print(f"Cleared cache for {property_type}")
        else:
            self.loaded_properties.clear()
            print("Cleared all cached star properties")
    
    def get_status_summary(self):
        """Get quick summary for GUI display."""
        summary = []
        for key, stats in self.file_stats.items():
            if stats['exists']:
                count = self.get_star_count(key)
                loaded = key in self.loaded_properties
                status = "loaded" if loaded else "available"
                summary.append(f"{key.capitalize()}: ~{count} stars ({stats['size_mb']:.1f} MB) - {status}")
            else:
                summary.append(f"{key.capitalize()}: Not available")
        return "\n".join(summary)


class StarVisualizationSearchWidget(ttk.Frame):
    """Search widget with unified display for all star information."""
    
    def __init__(self, parent):
        super().__init__(parent)
        
        self.star_data = {}  # Just the names for search
        self.star_full_data = {}  # Complete properties
        
        self.last_selected_star = None
        self.last_selected_category = None
        
        # Load all data
        self.load_star_data()
        
        # Set up the UI
        self.setup_ui()


    def load_star_data(self):
        """Load only star NAMES for search lists, not full data."""
        # Initialize dictionaries
        self.star_data = {}
        self.star_full_data = {}  # Initialize empty - will load on demand
        
        # Notable stars - just names
        self.star_data["Notable Stars"] = sorted(unique_notes.keys())
        
        # For distance/magnitude - only get names, not full data
        for data_type, category in [('distance', 'Stars by Distance'), 
                                    ('magnitude', 'Stars by Magnitude')]:
            filename = f'star_data/star_properties_{data_type}.pkl'
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
        
        # Print summary - FIXED INDENTATION
        print("\n" + "="*60)
        print("STAR DATA LOADING SUMMARY")
        print("="*60)
        print(f"Notable Stars: {len(self.star_data.get('Notable Stars', []))} stars")
        print(f"Stars by Distance: {len(self.star_data.get('Stars by Distance', []))} stars")  
        print(f"Stars by Magnitude: {len(self.star_data.get('Stars by Magnitude', []))} stars")
        print("="*60 + "\n")        
            

    def load_enhanced_pickle(self, filename: str) -> Dict:
        """Load pickle file - handles both old and enhanced formats."""
        if not os.path.exists(filename):
            print(f"[FAIL] {filename} not found")
            return {}
        
        try:
            with open(filename, 'rb') as f:
                data = pickle.load(f)
            
            # Convert list format to dictionary keyed by star name
            star_dict = {}
            
            if 'star_names' in data:
                num_stars = len(data['star_names'])
                
                # Check if this is enhanced data
                has_calculated = 'Temperature' in data
                
                if has_calculated:
                    print(f"[OK] Loaded {filename}: {num_stars} stars WITH calculated properties")
                else:
                    print(f"[WARN] Loaded {filename}: {num_stars} stars (basic properties only)")
                
                for i in range(num_stars):
                    star_name = data['star_names'][i]
                    
                    # Build star properties dictionary
                    star_dict[star_name] = {
                        'Star_Name': star_name,
                        'unique_id': data.get('unique_ids', [None]*num_stars)[i],
                        'spectral_type': data.get('spectral_types', [None]*num_stars)[i],
                        'V_magnitude': data.get('V_magnitudes', [None]*num_stars)[i],
                        'B_magnitude': data.get('B_magnitudes', [None]*num_stars)[i],
                        'object_type': data.get('object_types', [None]*num_stars)[i],
                        'distance_ly': data.get('distance_ly', [None]*num_stars)[i],
                        'distance_pc': data.get('distance_pc', [None]*num_stars)[i],
                    }
                    
                    # Add calculated properties if they exist
                    if has_calculated:
                        star_dict[star_name].update({
                            'Temperature': data.get('Temperature', [None]*num_stars)[i],
                            'Luminosity': data.get('Luminosity', [None]*num_stars)[i],
                            'Abs_Mag': data.get('Abs_Mag', [None]*num_stars)[i],
                            'RA_ICRS': data.get('RA_ICRS', [None]*num_stars)[i],
                            'DE_ICRS': data.get('DE_ICRS', [None]*num_stars)[i],
                            'ra_str': data.get('ra_str', [None]*num_stars)[i],
                            'dec_str': data.get('dec_str', [None]*num_stars)[i],
                            'Stellar_Class': data.get('Stellar_Class', [None]*num_stars)[i],
                            'Object_Type_Desc': data.get('Object_Type_Desc', [None]*num_stars)[i],
                            'Source_Catalog': data.get('Source_Catalog', [None]*num_stars)[i],
                        })
            
            return star_dict
            
        except Exception as e:
            print(f"Error loading {filename}: {e}")
            return {}

    def setup_ui(self):
        """Set up the UI with single column layout."""
        main_frame = ttk.Frame(self)
        main_frame.pack(fill='both', expand=True, padx=5, pady=5)
        
        self.search_vars = {}
        self.result_listboxes = {}
        self.search_entries = {}
        
        categories = ["Notable Stars", "Stars by Distance", "Stars by Magnitude"]
        
        for category in categories:
            # Create labeled frame for each category
            category_frame = ttk.LabelFrame(main_frame, text=category, padding=5)
            category_frame.pack(fill='x', padx=5, pady=5)
            
            # Search entry
            search_frame = ttk.Frame(category_frame)
            search_frame.pack(fill='x')
            
            ttk.Label(search_frame, text="Search:").pack(side='left')
            search_var = tk.StringVar()
            search_entry = ttk.Entry(search_frame, textvariable=search_var, width=30)
            search_entry.pack(side='left', fill='x', expand=True, padx=(5, 0))
            
            self.search_vars[category] = search_var
            self.search_entries[category] = search_entry
            search_var.trace('w', lambda *args, cat=category: self.on_search_change(cat))
            
            # Results listbox (collapsible)
            list_frame = ttk.Frame(category_frame)
            list_frame.pack(fill='x', pady=(5, 0))
            
            scrollbar = ttk.Scrollbar(list_frame)
            scrollbar.pack(side='right', fill='y')
            
            listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set, height=4)
            listbox.pack(side='left', fill='both', expand=True)
            scrollbar.config(command=listbox.yview)
            
            self.result_listboxes[category] = listbox
            listbox.bind('<<ListboxSelect>>', lambda e, cat=category: self.on_select(cat))
            
            # Initially hide listbox
            list_frame.pack_forget()
            
            # Show/hide listbox when typing
            def toggle_listbox(cat, frame):
                def handler(*args):
                    if self.search_vars[cat].get():
                        frame.pack(fill='x', pady=(5, 0))
                    else:
                        frame.pack_forget()
                return handler
            
            search_var.trace('w', toggle_listbox(category, list_frame))
        
        # Separator
        ttk.Separator(main_frame, orient='horizontal').pack(fill='x', pady=10)
        
        # Combined information display
        info_frame = ttk.LabelFrame(main_frame, text="Star Information", padding=5)
        info_frame.pack(fill='both', expand=True, padx=5, pady=5)
        
        text_frame = ttk.Frame(info_frame)
        text_frame.pack(fill='both', expand=True)
        
        v_scroll = ttk.Scrollbar(text_frame, orient='vertical')
        v_scroll.pack(side='right', fill='y')
        
        h_scroll = ttk.Scrollbar(text_frame, orient='horizontal')
        h_scroll.pack(side='bottom', fill='x')
        
        self.info_display = tk.Text(
            text_frame,
            height=27,
            wrap='word',
            yscrollcommand=v_scroll.set,
            xscrollcommand=h_scroll.set,
            font=('Consolas', 10)
        )
        self.info_display.pack(fill='both', expand=True)
        v_scroll.config(command=self.info_display.yview)
        h_scroll.config(command=self.info_display.xview)
        
        self.add_clipboard_support(self.info_display)
        
        # Initial message
        self.info_display.insert('1.0', 
            "Search for a star using any of the search fields above.\n\n"
            "* Notable Stars: Stars with descriptions and notes\n"
            "* Stars by Distance: Stars within specified distance range\n"
            "* Stars by Magnitude: Stars brighter than specified magnitude\n\n"
            "Start typing to see matching stars...")

        self.after(1000, lambda: print(f"Info display actual height: {self.info_display.winfo_height()} pixels"))
        self.after(1000, lambda: print(f"Info frame height: {info_frame.winfo_height()} pixels"))
        self.after(1000, lambda: print(f"Window height: {self.winfo_height()} pixels"))

    def on_search_change(self, category: str):
        """Handle search input."""
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
        
        if len(matches) == 1:
            listbox.selection_set(0)

    def on_select(self, category: str):
        """Handle star selection."""
        listbox = self.result_listboxes[category]
        try:
            selection = listbox.get(listbox.curselection())
            
            if selection:
                self.search_vars[category].set(selection)
                
                for other_cat in self.search_vars:
                    if other_cat != category:
                        self.search_vars[other_cat].set("")
                
                self.last_selected_star = selection
                self.last_selected_category = category
                
                for lb in self.result_listboxes.values():
                    lb.delete(0, tk.END)
                    lb.master.pack_forget()
                
                info_text = self.format_complete_star_info(selection, category)
                self.info_display.delete('1.0', tk.END)
                self.info_display.insert('1.0', info_text)
                
                self.highlight_urls(self.info_display)
                
        except:
            pass


    def format_complete_star_info(self, star_name: str, category: str) -> str:
        """Format all available star information."""
        output = []
        output.append(f"{'='*60}")
        output.append(f"{star_name}")
        output.append(f"{'='*60}\n")
        
        # CHANGE: Always load on-demand, don't check self.star_full_data
        star_props = self.load_single_star_properties(star_name, category)
        
        # If not found or incomplete, check other catalogs
        if not star_props or len(star_props) < 5:
            for other_category in ["Stars by Distance", "Stars by Magnitude"]:
                if other_category != category:
                    other_props = self.load_single_star_properties(star_name, other_category)
                    if other_props and len(other_props) > len(star_props):
                        star_props = other_props
                        break
        
        # 1. RA/Dec Coordinates
        ra_dec = self.format_ra_dec(star_props)
        if ra_dec:
            output.append("COORDINATES:")
            output.append("-" * 40)
            output.append(ra_dec)
            output.append("")
        
        # 2. Core Properties
        props_text = self.format_core_properties(star_props)
        if props_text:
            output.append("STAR PROPERTIES:")
            output.append("-" * 40)
            output.append(props_text)
            output.append("")
        
        # 3. Description from unique_notes
        note = unique_notes.get(star_name, "")
        if note and note != "None.":
            output.append("DESCRIPTION:")
            output.append("-" * 40)
            clean_note = self.clean_html_note(note)
            output.append(clean_note)
            output.append("")
            
            # 4. URL if present
            url = self.extract_url(note)
            if url:
                output.append("REFERENCE URL:")
                output.append("-" * 40)
                output.append(url)
                output.append("")
        
        # 5. Source information
        output.append("-" * 60)
        output.append(f"Search Category: {category}")
        
        # CHANGE 3: Update the availability check to not rely on pre-loaded data
        available_in = []
        if star_name in unique_notes:
            available_in.append("Notable Stars")

        # Check if star exists in distance catalog
        if self.check_star_exists(star_name, "Stars by Distance"):
            available_in.append("Distance Catalog")

        # Check if star exists in magnitude catalog  
        if self.check_star_exists(star_name, "Stars by Magnitude"):
            available_in.append("Magnitude Catalog")            
        
        if available_in:
            output.append(f"Available in: {', '.join(available_in)}")
        
        return '\n'.join(output)

    def check_star_exists(self, star_name: str, category: str) -> bool:
        """Check if a star exists in a category without loading full data."""
        return star_name in self.star_data.get(category, [])

    def load_single_star_properties(self, star_name: str, category: str) -> dict:
        """Load properties for a single star on-demand."""
        
        # Map category to file
        file_map = {
            "Stars by Distance": "star_data/star_properties_distance.pkl",
            "Stars by Magnitude": "star_data/star_properties_magnitude.pkl",
            "Notable Stars": "star_data/star_properties_distance.pkl"  # Try distance file for notable stars
        }
        
        filename = file_map.get(category)
        if not filename or not os.path.exists(filename):
            return {}
        
        try:
            with open(filename, 'rb') as f:
                data = pickle.load(f)
            
            # Handle dictionary format (new enhanced format)
            if isinstance(data, dict) and star_name in data:
                return data[star_name]
            
            # Handle list format (old format)
            if isinstance(data, dict) and 'star_names' in data:
                try:
                    idx = data['star_names'].index(star_name)
                    props = {'Star_Name': star_name}
                    
                    # In load_single_star_properties(), fix the field mapping:
                    for field in ['unique_ids', 'spectral_types', 'V_magnitudes', 'B_magnitudes',
                                'object_types', 'distance_ly', 'distance_pc', 'Temperature',
                                'Luminosity', 'Abs_Mag', 'RA_ICRS', 'DE_ICRS', 'ra_str',
                                'dec_str', 'Stellar_Class', 'Object_Type_Desc', 'Source_Catalog']:
                        if field in data and idx < len(data[field]):
                            value = data[field][idx]
                            # Better field mapping
                            if field == 'unique_ids':
                                key = 'unique_id'
                            elif field == 'spectral_types':
                                key = 'spectral_type'
                            elif field == 'V_magnitudes':
                                key = 'V_magnitude'
                            elif field == 'B_magnitudes':
                                key = 'B_magnitude'
                            elif field == 'object_types':
                                key = 'object_type'
                            else:
                                key = field  # Use as-is for other fields
                            props[key] = value

                    return props
                except (ValueError, IndexError):
                    pass
        
        except Exception as e:
            print(f"Error loading {star_name} from {filename}: {e}")
        
        return {}

    def format_ra_dec(self, star_props: Dict) -> Optional[str]:
        """Format RA/Dec coordinates."""
        # Try pre-formatted strings first (from enhanced data)
        ra_str = star_props.get('ra_str')
        dec_str = star_props.get('dec_str')
        
        if ra_str and dec_str and str(ra_str).lower() not in ['nan', 'none', '']:
            return f"RA:  {ra_str}\nDec: {dec_str}\n{ra_str} {dec_str}\n(J2000 epoch)"
        
        # Try ICRS coordinates in degrees
        ra_deg = star_props.get('RA_ICRS')
        dec_deg = star_props.get('DE_ICRS')
        
        if ra_deg is not None and dec_deg is not None:
            try:
                ra_deg = float(ra_deg)
                dec_deg = float(dec_deg)
                
                if not np.isnan(ra_deg) and not np.isnan(dec_deg):
                    # Convert to sexagesimal
                    ra_hours = ra_deg / 15.0
                    ra_h = int(ra_hours)
                    ra_m = int((ra_hours - ra_h) * 60)
                    ra_s = ((ra_hours - ra_h) * 60 - ra_m) * 60
                    
                    dec_sign = '+' if dec_deg >= 0 else '-'
                    dec_abs = abs(dec_deg)
                    dec_d = int(dec_abs)
                    dec_m = int((dec_abs - dec_d) * 60)
                    dec_s = ((dec_abs - dec_d) * 60 - dec_m) * 60
                    
                    ra_formatted = f"{ra_h:02d}h {ra_m:02d}m {ra_s:05.2f}s"
                    dec_formatted = f"{dec_sign}{dec_d:02d} deg {dec_m:02d}' {dec_s:04.1f}\""
                    
                    return f"RA:  {ra_formatted}\nDec: {dec_formatted}\n(J2000 epoch)"
            except:
                pass
        
        return None

    def format_core_properties(self, star_props: Dict) -> str:
        """Format star properties - reads from enhanced pickle data."""
        lines = []
        
        # Distance
        distance_ly = star_props.get('distance_ly')
        distance_pc = star_props.get('distance_pc')
        
        if distance_ly is not None and not pd.isna(distance_ly):
            if distance_pc is None or pd.isna(distance_pc):
                distance_pc = distance_ly / 3.26156
            lines.append(f"Distance: {distance_pc:.2f} pc ({distance_ly:.2f} ly)")
        elif distance_pc is not None and not pd.isna(distance_pc):
            distance_ly = distance_pc * 3.26156
            lines.append(f"Distance: {distance_pc:.2f} pc ({distance_ly:.2f} ly)")
        
        # Temperature (from enhanced data or basic)
        temp = star_props.get('Temperature')
        if temp is not None and not pd.isna(temp):
            lines.append(f"Temperature: {temp:.0f} K")
        
        # Luminosity (from enhanced data)
        lum = star_props.get('Luminosity')
        if lum is not None and not pd.isna(lum):
            lines.append(f"Luminosity: {lum:.6f} L[SUN]")
        
        # Absolute Magnitude (from enhanced data)
        abs_mag = star_props.get('Abs_Mag')
        if abs_mag is not None and not pd.isna(abs_mag):
            lines.append(f"Absolute Magnitude: {abs_mag:.2f}")
        
        # Apparent Magnitude
        app_mag = star_props.get('V_magnitude')
        if app_mag is not None and not pd.isna(app_mag):
            lines.append(f"Apparent Magnitude: {app_mag:.2f}")
        
        # Spectral Type
        spec_type = star_props.get('spectral_type')
        if spec_type and str(spec_type) not in ['Unknown', 'nan', 'None']:
            lines.append(f"Spectral Type: {spec_type}")
        
        # Stellar Class (from enhanced data or parse from spectral type)
        stellar_class = star_props.get('Stellar_Class')
        if stellar_class and str(stellar_class) not in ['Unknown', 'nan', 'None']:
            # Get full description if available
            if stellar_class in stellar_class_labels:
                lines.append(f"Stellar Class: {stellar_class_labels[stellar_class]}")
            else:
                lines.append(f"Stellar Class: {stellar_class}")
        
        # Object Type (expanded from enhanced data or basic code)
        obj_type = star_props.get('Object_Type_Desc')  # Try enhanced first
        if not obj_type or pd.isna(obj_type):
            obj_type_code = star_props.get('object_type')  # Fall back to code
            if obj_type_code and str(obj_type_code) not in ['Unknown', 'nan', 'None']:
                # Expand using mapping
                codes = re.split(r'[;, ]+', str(obj_type_code))
                descriptions = []
                for code in codes:
                    code = code.strip()
                    descriptions.append(object_type_mapping.get(code, code))
                obj_type = ', '.join(descriptions)
        
        if obj_type and str(obj_type) not in ['Unknown', 'nan', 'None']:
            lines.append(f"Object Type: {obj_type}")
        
        # Source Catalog (from enhanced data or infer from unique_id)
        source = star_props.get('Source_Catalog')
        if source:
            lines.append(f"Source Catalog: {source}")
        else:
            uid = star_props.get('unique_id')
            if uid:
                if uid.startswith('HIP'):
                    lines.append("Source Catalog: Hipparcos")
                elif uid.startswith('Gaia'):
                    lines.append("Source Catalog: Gaia")
        
        return '\n'.join(lines)

    def clean_html_note(self, note: str) -> str:
        """Remove HTML tags from note content."""
        clean = re.sub(r'<br\s*/?>', '\n', note)
        clean = re.sub(r'<a\s+href="[^"]*"[^>]*>([^<]*)</a>', r'\1', clean)
        clean = re.sub(r'<[^>]+>', '', clean)
        clean = re.sub(r'\n\s*\n', '\n\n', clean)
        return clean.strip()

    def extract_url(self, note: str) -> Optional[str]:
        """Extract URL from HTML anchor tags."""
        url_match = re.search(r'<a href="([^"]+)">', note)
        if url_match:
            return url_match.group(1)
        return None

    def highlight_urls(self, text_widget):
        """Make URLs clickable."""
        content = text_widget.get('1.0', tk.END)
        text_widget.tag_remove("url", "1.0", tk.END)
        
        url_pattern = r'https?://[^\s]+'
        for match in re.finditer(url_pattern, content):
            start_idx = f"1.0 + {match.start()} chars"
            end_idx = f"1.0 + {match.end()} chars"
            text_widget.tag_add("url", start_idx, end_idx)
        
        text_widget.tag_config("url", foreground="blue", underline=True)
        
        def open_url(event):
            index = text_widget.index(f"@{event.x},{event.y}")
            if "url" in text_widget.tag_names(index):
                ranges = text_widget.tag_ranges("url")
                for i in range(0, len(ranges), 2):
                    if text_widget.compare(index, ">=", ranges[i]) and \
                       text_widget.compare(index, "<=", ranges[i+1]):
                        url = text_widget.get(ranges[i], ranges[i+1])
                        webbrowser.open(url)
                        break
        
        text_widget.tag_bind("url", "<Button-1>", open_url)
        text_widget.tag_bind("url", "<Enter>", lambda e: text_widget.config(cursor="hand2"))
        text_widget.tag_bind("url", "<Leave>", lambda e: text_widget.config(cursor=""))

    def add_clipboard_support(self, widget):
        """Add copy/paste support."""
        def copy(event=None):
            try:
                selection = widget.get(tk.SEL_FIRST, tk.SEL_LAST)
                widget.clipboard_clear()
                widget.clipboard_append(selection)
            except:
                pass
            return "break"
        
        def select_all(event=None):
            widget.tag_add(tk.SEL, "1.0", tk.END)
            widget.mark_set(tk.INSERT, "1.0")
            widget.see(tk.INSERT)
            return "break"
        
        widget.bind("<Control-c>", copy)
        widget.bind("<Control-a>", select_all)
        
        menu = tk.Menu(widget, tearoff=0)
        menu.add_command(label="Copy", command=copy)
        menu.add_command(label="Select All", command=select_all)
        
        def show_menu(event):
            menu.post(event.x_root, event.y_root)
        
        widget.bind("<Button-3>", show_menu)

    def get_selected_stars(self) -> Dict[str, Optional[str]]:
        """Get currently selected stars."""
        return {
            category: self.search_vars[category].get()
            for category in self.search_vars
        }


class StarVisualizationGUI(tk.Tk):
    """Main GUI window with search and visualization controls."""
    
    def __init__(self):
        super().__init__()
        self.title("Star Visualization Control Panel -- Updated: January 10, 2026")
        
        # ====================================================================
        # WINDOW GEOMETRY AND CONFIG MANAGEMENT
        # ====================================================================
        
        # Config file in application directory
        self.CONFIG_FILE = os.path.join(os.getcwd(), 'star_viz_config.json')
        print(f"Window config file: {self.CONFIG_FILE}", flush=True)
        
        # Platform-aware defaults
        if platform.system() == 'Linux':
            DEFAULT_GEOMETRY = "1200x850"
            MIN_WIDTH, MIN_HEIGHT = 1050, 700
            self.DEFAULT_SASH = [380, 780]
        elif platform.system() == 'Darwin':
            DEFAULT_GEOMETRY = "1150x830"
            MIN_WIDTH, MIN_HEIGHT = 1000, 680
            self.DEFAULT_SASH = [360, 750]
        else:  # Windows
            DEFAULT_GEOMETRY = "1100x800"
            MIN_WIDTH, MIN_HEIGHT = 980, 650
            self.DEFAULT_SASH = [340, 720]
        
        # Load saved config
        self.saved_config = self.load_window_config()
        if self.saved_config and self.saved_config.get('platform') == platform.system():
            try:
                self.geometry(self.saved_config['geometry'])
                print(f"Restored window geometry: {self.saved_config['geometry']}", flush=True)
                # Restore maximized state if it was saved
                if self.saved_config.get('state') == 'zoomed':
                    self.after(100, lambda: self.state('zoomed'))
                    print("Window will be maximized", flush=True)
            except:
                self.geometry(DEFAULT_GEOMETRY)
        else:
            self.geometry(DEFAULT_GEOMETRY)
            print(f"Using default geometry: {DEFAULT_GEOMETRY}", flush=True)
        
        self.minsize(MIN_WIDTH, MIN_HEIGHT)
        self.resizable(True, True)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # ====================================================================
        
        self.BUTTON_WIDTH = 35
        self.BUTTON_FONT = ("Arial", 10, "normal")
        
        self.setup_ui()
        
        # Restore sash positions after UI is built
        self.after(100, self.restore_sash_positions)
        
        # Check for and load last plot data after UI is ready
        self.after(200, self.check_and_load_last_plot)
    
    def load_window_config(self):
        """Load saved window geometry and sash positions."""
        try:
            if os.path.exists(self.CONFIG_FILE):
                with open(self.CONFIG_FILE, 'r') as f:
                    return json.load(f)
        except Exception as e:
            print(f"Note: Could not load window config: {e}", flush=True)
        return None
    
    def save_window_config(self):
        """Save window geometry and sash positions."""
        try:
            sash_positions = []
            try:
                for i in range(2):
                    sash_positions.append(self.main_paned.sash_coord(i)[0])
            except:
                pass
            config = {
                'geometry': self.geometry(),
                'state': self.state(),
                'platform': platform.system(),
                'sash_positions': sash_positions
            }
            with open(self.CONFIG_FILE, 'w') as f:
                json.dump(config, f, indent=2)
            print(f"Window config saved to {self.CONFIG_FILE}", flush=True)
        except Exception as e:
            print(f"Note: Could not save window config: {e}", flush=True)
    
    def restore_sash_positions(self):
        """Restore saved sash positions."""
        try:
            positions = None
            if self.saved_config and self.saved_config.get('platform') == platform.system():
                positions = self.saved_config.get('sash_positions')
            if positions and len(positions) >= 2:
                self.main_paned.sash_place(0, positions[0], 0)
                self.main_paned.sash_place(1, positions[1], 0)
                print(f"Restored sash positions: {positions}", flush=True)
            else:
                self.main_paned.sash_place(0, self.DEFAULT_SASH[0], 0)
                self.main_paned.sash_place(1, self.DEFAULT_SASH[1], 0)
                print(f"Using default sash positions: {self.DEFAULT_SASH}", flush=True)
        except Exception as e:
            print(f"Note: Could not restore sash positions: {e}", flush=True)
    
    def on_closing(self):
        """Save config and close."""
        self.save_window_config()
        self.destroy()


    def run_visualization_with_console_output(self, script_path, args):
        """Run visualization and print output to console."""
        import subprocess
        import sys
        
        result = subprocess.run(
            [sys.executable, script_path] + args,
            capture_output=True,
            text=True
        )
        
        print("\n" + "="*60)
        print(f"Output from {script_path}:")
        print("="*60)
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print("ERRORS:", result.stderr)
        print("="*60 + "\n")
        
        return result.returncode == 0

    def check_and_load_last_plot(self):
        """Check for and load the last plot data on startup."""
        try:

            # Try to load the scientific report first
            report_mgr = ReportManager()
            report_data = report_mgr.load_last_report()
            
            if report_data:
                print("Found existing scientific report, loading...")
                self.plot_report.display_report(report_data)
                return

            # Try to load the last plot data
            plot_data = PlotDataExchange.load_plot_data()
            
            if plot_data:
                print("Found existing plot data, loading report...")
                
                # Create minimal DataFrame for report
                import pandas as pd
                
                # Get data from the saved plot
                temp_valid = plot_data.get('temp_valid', 0)
                temp_missing = plot_data.get('temp_missing', 0)
                lum_valid = plot_data.get('lum_valid', 0)
                lum_missing = plot_data.get('lum_missing', 0)
                total_stars = plot_data.get('total_stars', 0)
                
                # Create arrays for Temperature and Luminosity
                temp_array = [1] * temp_valid + [0] * temp_missing
                lum_array = [1] * lum_valid + [0] * lum_missing
                
                # Make sure arrays are the same length (use total_stars as reference)
                if len(temp_array) < total_stars:
                    temp_array.extend([0] * (total_stars - len(temp_array)))
                if len(lum_array) < total_stars:
                    lum_array.extend([0] * (total_stars - len(lum_array)))
                    
                # Trim if too long
                temp_array = temp_array[:total_stars]
                lum_array = lum_array[:total_stars]
                
                # Create DataFrame
                pseudo_df = pd.DataFrame({
                    'Temperature': temp_array,
                    'Luminosity': lum_array
                })
                
                # Add catalog information if available
                if plot_data.get('catalog_counts'):
                    catalogs = []
                    for catalog, count in plot_data['catalog_counts'].items():
                        catalogs.extend([catalog] * count)
                    if catalogs:
                        # Make sure catalog list matches DataFrame length
                        if len(catalogs) > len(pseudo_df):
                            catalogs = catalogs[:len(pseudo_df)]
                        elif len(catalogs) < len(pseudo_df):
                            # Pad with 'Unknown' if needed
                            catalogs.extend(['Unknown'] * (len(pseudo_df) - len(catalogs)))
                        pseudo_df['Source_Catalog'] = catalogs
                
                # Add magnitude stats if available
                if plot_data.get('magnitude_stats'):
                    mag_stats = plot_data['magnitude_stats']
                    # Use mean if available, otherwise use a default
                    mag_value = mag_stats.get('mean', 0) if mag_stats else 0
                    pseudo_df['Apparent_Magnitude'] = [mag_value] * len(pseudo_df)
                
                # Update the report widget
                self.plot_report.update_report(
                    combined_df=pseudo_df,
                    counts_dict=plot_data.get('counts_dict', {}),
                    processing_times=plot_data.get('processing_times', {}),
                    mode=plot_data.get('mode', 'unknown'),
                    limit_value=plot_data.get('limit_value')
                )
                
        except Exception as e:
            print(f"Error loading last plot data: {e}")
            import traceback
            traceback.print_exc()
            self.status_label.config(
                text="Ready",
                foreground="green"
            )

    def setup_ui(self):
        """Build the complete user interface."""
        # Create PanedWindow for resizable columns
        self.main_paned = tk.PanedWindow(self, orient=tk.HORIZONTAL, sashwidth=8,
                                         sashrelief=tk.RAISED, bg='gray70')
        self.main_paned.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # LEFT COLUMN - Star Search
        left_frame = ttk.Frame(self.main_paned)
        
        search_label = ttk.Label(left_frame, text="Star Search", font=("Arial", 12, "bold"))
        search_label.pack(pady=(0, 10))
        
        self.search_widget = StarVisualizationSearchWidget(left_frame)
        self.search_widget.pack(fill='both', expand=True)
        
        # MIDDLE COLUMN - Visualization Controls
        middle_scroll = ScrollableFrame(self.main_paned)
        middle_frame = middle_scroll.container
        
        controls_label = ttk.Label(middle_frame, text="Visualization Controls", font=("Arial", 12, "bold"))
        controls_label.pack(pady=(0, 10))
        
        # Distance controls
        distance_frame = ttk.LabelFrame(middle_frame, text="Distance-based Visualization (4.25 through 100 light-years)", padding=10)
        distance_frame.pack(fill='x', pady=(0, 10))
        
        ttk.Label(distance_frame, text="Distance (light-years):").pack(anchor='w')
        self.ly_entry = ttk.Entry(distance_frame, width=20)
        self.ly_entry.pack(fill='x', pady=(5, 10))
        self.ly_entry.insert(0, "20")
        
        self.plot_3d_button = tk.Button(
            distance_frame,
            text="3D Stellar Neighborhood",
            command=self.plot_3d_distance,
            bg='SystemButtonFace',
            fg='blue',
            width=self.BUTTON_WIDTH,
            font=self.BUTTON_FONT
        )
        self.plot_3d_button.pack(pady=(0, 5))
        
        self.plot_2d_button = tk.Button(
            distance_frame,
            text="2D HR Diagram",
            command=self.plot_2d_distance,
            bg='SystemButtonFace',
            fg='blue',
            width=self.BUTTON_WIDTH,
            font=self.BUTTON_FONT
        )
        self.plot_2d_button.pack()
        
        # Magnitude controls
        magnitude_frame = ttk.LabelFrame(middle_frame, text="Apparent Magnitude-based Visualization (-1.44 through 9)", padding=10)
        magnitude_frame.pack(fill='x', pady=(0, 10))

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
        
        ttk.Label(magnitude_frame, text="Limiting Magnitude:").pack(anchor='w')
        self.mag_entry = ttk.Entry(magnitude_frame, width=20)
        self.mag_entry.pack(fill='x', pady=(5, 10))
        self.mag_entry.insert(0, "4")
        
        self.plot_3d_mag_button = tk.Button(
            magnitude_frame,
            text="3D Visible Stars",
            command=self.plot_3d_magnitude,
            bg='SystemButtonFace',
            fg='blue',
            width=self.BUTTON_WIDTH,
            font=self.BUTTON_FONT
        )
        self.plot_3d_mag_button.pack(pady=(0, 5))
        
        self.plot_2d_mag_button = tk.Button(
            magnitude_frame,
            text="2D HR Diagram (Visible)",
            command=self.plot_2d_magnitude,
            bg='SystemButtonFace',
            fg='blue',
            width=self.BUTTON_WIDTH,
            font=self.BUTTON_FONT
        )
        self.plot_2d_mag_button.pack()
        
        # Status display
        status_frame = ttk.LabelFrame(middle_frame, text="Status", padding=10)
        status_frame.pack(fill='x', pady=(10, 0))
        
        self.status_label = ttk.Label(status_frame, text="Ready", foreground="green")
        self.status_label.pack()
        
        # ADD THIS NEW SECTION - Plot Data Report Widget
        self.plot_report = PlotDataReportWidget(middle_frame)
        self.plot_report.pack(fill='both', expand=True, pady=(10, 0))

        # RIGHT COLUMN - Notes
        right_frame = ttk.Frame(self.main_paned)
        
        notes_label = ttk.Label(right_frame, text="Notes", font=("Arial", 12, "bold"))
        notes_label.pack(pady=(0, 10))
        
        notes_text = scrolledtext.ScrolledText(right_frame, wrap='word', width=30, height=45)
        notes_text.pack(fill='both', expand=True)
        notes_text.insert('1.0', 
            "Star Visualization Guide\n"
            "========================\n\n"
            "Distance Visualization:\n"
            "- Enter distance in light-years\n"
            "- Maximum: 100 light-years\n"
            "- Shows: ~9,750 stars at max\n\n"
            "Magnitude Visualization:\n"
            "- Enter limiting magnitude (Vmag)\n"
            "- Range: -1.44 to 9.0\n"
            "- Shows: ~124,000 stars at Vmag 9\n\n"
            "Description	           Vmag\n"
            "--------------------   ---------\n"
            "Earth orbit            8.0 - 9.0\n"
            "Excellent dark sky	    7.6 - 8.0\n"
            "Typical dark sky	      7.1 - 7.5\n"
            "Rural sky	             6.6 - 7.0\n"
            "Rural/suburban sky     6.1 - 6.5\n"
            "Suburban sky	          5.6 - 6.0\n"
            "Bright suburban sky	   5.1 - 5.5\n"
            "Suburban/urban sky	    4.6 - 5.0\n"
            "City sky	              4.1 - 4.5\n"
            "Inner-city sky	        < 4.0\n"
            "Brightest star, Sirius -1.44\n\n"
            "Cache Management:\n"
            "- Protected VOT/PKL files\n"
            "- Automatic backups created\n"
            "- Safe incremental updates\n"
            "- No data loss on errors\n\n"
            "Search Features:\n"
            "- Search any star by name\n"
            "- View properties and notes\n"
            "- Click URLs to open in browser\n"
            "- Coordinates in J2000 epoch\n\n"
            "Data Quality:\n"
            "- 77-99% stars have temperatures\n"
            "- All stars have luminosity\n"
            "- Enhanced stellar parameters\n"
            "- Hipparcos + Gaia catalogs\n\n"
            "Tips:\n"
            "- Reducing limits uses cache only\n"
            "- Progress saves automatically\n"
            "- Safe to interrupt with Ctrl+C\n"
        )
        notes_text.config(state='disabled')
        
        # Add frames to PanedWindow
        self.main_paned.add(left_frame, minsize=250, sticky='nsew')
        self.main_paned.add(middle_scroll, minsize=300, sticky='nsew')
        self.main_paned.add(right_frame, minsize=200, sticky='nsew')

    # ============================================================
    # PLOTTING METHODS - Updated for PyInstaller support
    # ============================================================

    def plot_3d_distance(self):
        """Launch 3D distance visualization."""
        try:
            ly_value = float(self.ly_entry.get())
            if ly_value <= 0 or ly_value > 100.1:
                self.status_label.config(text="Enter 4.25 - 100 light-years", foreground="red")
                return
            
            self.status_label.config(
                text=f"Generating 3D visualization for distance <= {ly_value} (~10-15 seconds)",
                foreground="blue"
            )
            self.update()

            if is_frozen() and PLOTTING_MODULES_AVAILABLE:
                # Running as exe - call function directly
                print(f"Running planetarium_distance.main() directly (frozen exe)")
                old_argv = sys.argv
                sys.argv = ['planetarium_distance.py', str(ly_value)]
                try:
                    planetarium_distance.main()
                    self.status_label.config(text=f"Launched 3D plot ({ly_value} ly)", foreground="green")
                except Exception as e:
                    print(f"Error in planetarium_distance: {e}")
                    import traceback
                    traceback.print_exc()
                    self.status_label.config(text="Error generating 3D plot", foreground="red")
                finally:
                    sys.argv = old_argv
            else:
                # Running as Python script - use subprocess
                script_path = os.path.join(os.path.dirname(__file__), 'planetarium_distance.py')
                result = subprocess.run([sys.executable, script_path, str(ly_value)],
                                    capture_output=True, text=True)
                
                print("\n" + "="*60)
                print(f"Output from planetarium_distance.py ({ly_value} ly):")
                print("="*60)
                if result.stdout:
                    print(result.stdout)
                if result.stderr:
                    print("STDERR:")
                    print(result.stderr)
                print("="*60 + "\n")
                
                if result.returncode == 0:
                    self.status_label.config(text=f"Launched 3D plot ({ly_value} ly)", foreground="green")
                else:
                    self.status_label.config(text="Error generating 3D plot", foreground="red")
                    
        except ValueError:
            self.status_label.config(text="Invalid distance value", foreground="red")
        except Exception as e:
            self.status_label.config(text=f"Error: {e}", foreground="red")


    def plot_2d_distance(self):
        """Launch 2D HR diagram for distance and update report."""
        try:
            ly_value = float(self.ly_entry.get())
            if ly_value <= 0 or ly_value > 100.1:
                self.status_label.config(text="Enter 4.25 - 100 light-years", foreground="red")
                return
            
            self.status_label.config(
                text=f"Generating 2D visualization for distance <= {ly_value} (~5-10 seconds)",
                foreground="blue"
            )
            self.update()

            if is_frozen() and PLOTTING_MODULES_AVAILABLE:
                # Running as exe - call function directly
                print(f"Running hr_diagram_distance.main() directly (frozen exe)")
                old_argv = sys.argv
                sys.argv = ['hr_diagram_distance.py', str(ly_value)]
                try:
                    hr_diagram_distance.main()
                    self.status_label.config(text=f"HR diagram completed ({ly_value} ly)", foreground="green")
                    self.after(500, self.load_and_display_plot_report)
                except Exception as e:
                    print(f"Error in hr_diagram_distance: {e}")
                    import traceback
                    traceback.print_exc()
                    self.status_label.config(text="Error generating plot", foreground="red")
                finally:
                    sys.argv = old_argv
            else:
                # Running as Python script - use subprocess
                script_path = os.path.join(os.path.dirname(__file__), 'hr_diagram_distance.py')
                result = subprocess.run([sys.executable, script_path, str(ly_value)], 
                                    capture_output=True, text=True)
                
                print("\n" + "="*60)
                print(f"Output from hr_diagram_distance.py ({ly_value} ly):")
                print("="*60)
                if result.stdout:
                    print(result.stdout)
                if result.stderr:
                    print("STDERR:")
                    print(result.stderr)
                print("="*60 + "\n")
                
                if result.returncode == 0:
                    self.status_label.config(text=f"HR diagram completed ({ly_value} ly)", foreground="green")
                    self.after(500, self.load_and_display_plot_report)
                else:
                    self.status_label.config(text="Error generating plot", foreground="red")
                    
        except ValueError:
            self.status_label.config(text="Invalid distance value", foreground="red")
        except Exception as e:
            self.status_label.config(text=f"Error: {e}", foreground="red")
            

    def plot_3d_magnitude(self):
        """Launch 3D magnitude visualization with scale options."""
        try:
            mag_value = float(self.mag_entry.get())
            if mag_value < -1.44 or mag_value > 9:
                self.status_label.config(text="Enter magnitude -1.44 to 9", foreground="red")
                return
            
            self.status_label.config(
                text=f"Generating 3D visualization for magnitude <= {mag_value} (~30-75 seconds)",
                foreground="blue"
            )
            self.update()

            # Get scale value if manual mode
            scale_value = None
            if hasattr(self, 'scale_var') and self.scale_var.get() == 'Manual':
                try:
                    scale_value = float(self.scale_entry.get())
                    if scale_value <= 0:
                        self.status_label.config(text="Scale must be positive", foreground="red")
                        return
                except ValueError:
                    self.status_label.config(text="Invalid scale value", foreground="red")
                    return

            if is_frozen() and PLOTTING_MODULES_AVAILABLE:
                # Running as exe - call function directly
                print(f"Running planetarium_apparent_magnitude.main() directly (frozen exe)")
                old_argv = sys.argv
                if scale_value:
                    sys.argv = ['planetarium_apparent_magnitude.py', str(mag_value), str(scale_value)]
                else:
                    sys.argv = ['planetarium_apparent_magnitude.py', str(mag_value)]
                try:
                    planetarium_apparent_magnitude.main()
                    if scale_value:
                        self.status_label.config(text=f"Launched 3D plot (mag {mag_value}, scale {scale_value} ly)", foreground="green")
                    else:
                        self.status_label.config(text=f"Launched 3D plot (mag {mag_value}, auto scale)", foreground="green")
                except Exception as e:
                    print(f"Error in planetarium_apparent_magnitude: {e}")
                    import traceback
                    traceback.print_exc()
                    self.status_label.config(text="Error generating 3D plot", foreground="red")
                finally:
                    sys.argv = old_argv
            else:
                # Running as Python script - use subprocess
                script_path = os.path.join(os.path.dirname(__file__), 'planetarium_apparent_magnitude.py')
                cmd = [sys.executable, script_path, str(mag_value)]
                
                if scale_value:
                    cmd.append(str(scale_value))
                
                result = subprocess.run(cmd, capture_output=True, text=True)
                
                print("\n" + "="*60)
                print(f"Output from planetarium_apparent_magnitude.py (mag {mag_value}):")
                print("="*60)
                if result.stdout:
                    print(result.stdout)
                if result.stderr:
                    print("STDERR:")
                    print(result.stderr)
                print("="*60 + "\n")
                
                if result.returncode == 0:
                    if scale_value:
                        self.status_label.config(text=f"Launched 3D plot (mag {mag_value}, scale {scale_value} ly)", foreground="green")
                    else:
                        self.status_label.config(text=f"Launched 3D plot (mag {mag_value}, auto scale)", foreground="green")
                else:
                    self.status_label.config(text="Error generating 3D plot", foreground="red")
                
        except ValueError:
            self.status_label.config(text="Invalid magnitude value", foreground="red")
        except Exception as e:
            self.status_label.config(text=f"Error: {e}", foreground="red")


    def plot_2d_magnitude(self):
        """Launch 2D HR diagram for magnitude and update report."""
        try:
            mag_value = float(self.mag_entry.get())
            if mag_value < -1.44 or mag_value > 9:
                self.status_label.config(text="Enter magnitude -1.44 to 9", foreground="red")
                return
            
            self.status_label.config(
                text=f"Generating 2D visualization for magnitude <= {mag_value} (~30-60 seconds)",
                foreground="blue"
            )
            self.update()

            if is_frozen() and PLOTTING_MODULES_AVAILABLE:
                # Running as exe - call function directly
                print(f"Running hr_diagram_apparent_magnitude.main() directly (frozen exe)")
                old_argv = sys.argv
                sys.argv = ['hr_diagram_apparent_magnitude.py', str(mag_value)]
                try:
                    hr_diagram_apparent_magnitude.main()
                    self.status_label.config(text=f"HR diagram completed (mag {mag_value})", foreground="green")
                    self.after(500, self.load_and_display_plot_report)
                except Exception as e:
                    print(f"Error in hr_diagram_apparent_magnitude: {e}")
                    import traceback
                    traceback.print_exc()
                    self.status_label.config(text="Error generating plot", foreground="red")
                finally:
                    sys.argv = old_argv
            else:
                # Running as Python script - use subprocess
                script_path = os.path.join(os.path.dirname(__file__), 'hr_diagram_apparent_magnitude.py')
                result = subprocess.run([sys.executable, script_path, str(mag_value)],
                                    capture_output=True, text=True)
                
                print("\n" + "="*60)
                print(f"Output from hr_diagram_apparent_magnitude.py (mag {mag_value}):")
                print("="*60)
                if result.stdout:
                    print(result.stdout)
                if result.stderr:
                    print("STDERR:")
                    print(result.stderr)
                print("="*60 + "\n")
                
                if result.returncode == 0:
                    self.status_label.config(text=f"HR diagram completed (mag {mag_value})", foreground="green")
                    self.after(500, self.load_and_display_plot_report)
                else:
                    self.status_label.config(text="Error generating plot", foreground="red")
                    
        except ValueError:
            self.status_label.config(text="Invalid magnitude value", foreground="red")
        except Exception as e:
            self.status_label.config(text=f"Error: {e}", foreground="red")


    def load_and_display_plot_report(self):
        """Load the plot data from the exchange file and update the report."""
        try:

            # Try to load the scientific report first
            report_mgr = ReportManager()
            report_data = report_mgr.load_last_report()
            
            if report_data:
                print("Loading scientific report with object type analysis...")
                self.plot_report.display_report(report_data)
                return

            plot_data = PlotDataExchange.load_plot_data()
            
            if plot_data:
                # Convert the loaded data to format expected by the report widget
                import pandas as pd
                
                # Get data values with defaults
                temp_valid = plot_data.get('temp_valid', 0)
                temp_missing = plot_data.get('temp_missing', 0)
                lum_valid = plot_data.get('lum_valid', 0)
                lum_missing = plot_data.get('lum_missing', 0)
                total_stars = plot_data.get('total_stars', 0)
                
                # Create pseudo DataFrame ensuring consistent length
                if total_stars > 0:
                    # Create arrays
                    temp_array = [1] * temp_valid + [0] * temp_missing
                    lum_array = [1] * lum_valid + [0] * lum_missing
                    
                    # Ensure arrays match total_stars length
                    temp_array = (temp_array + [0] * total_stars)[:total_stars]
                    lum_array = (lum_array + [0] * total_stars)[:total_stars]
                    
                    pseudo_df = pd.DataFrame({
                        'Temperature': temp_array,
                        'Luminosity': lum_array
                    })
                else:
                    # Empty DataFrame if no stars
                    pseudo_df = pd.DataFrame({
                        'Temperature': [],
                        'Luminosity': []
                    })
                
                # Add catalog information if available
                if plot_data.get('catalog_counts') and len(pseudo_df) > 0:
                    catalogs = []
                    for catalog, count in plot_data['catalog_counts'].items():
                        catalogs.extend([catalog] * min(count, total_stars - len(catalogs)))
                        if len(catalogs) >= total_stars:
                            break
                            
                    # Pad or trim catalog list
                    if len(catalogs) < len(pseudo_df):
                        catalogs.extend(['Unknown'] * (len(pseudo_df) - len(catalogs)))
                    elif len(catalogs) > len(pseudo_df):
                        catalogs = catalogs[:len(pseudo_df)]
                        
                    pseudo_df['Source_Catalog'] = catalogs
                
                # Add magnitude stats if available
                if plot_data.get('magnitude_stats') and len(pseudo_df) > 0:
                    mag_stats = plot_data['magnitude_stats']
                    mag_mean = mag_stats.get('mean', 0) if mag_stats else 0
                    pseudo_df['Apparent_Magnitude'] = [mag_mean] * len(pseudo_df)
                
                # Update the report widget
                self.plot_report.update_report(
                    combined_df=pseudo_df,
                    counts_dict=plot_data.get('counts_dict', {}),
                    processing_times=plot_data.get('processing_times', {}),
                    mode=plot_data.get('mode', 'unknown'),
                    limit_value=plot_data.get('limit_value')
                )
                
                print("Plot report updated successfully")
                
            else:
                self.status_label.config(text="Could not load plot data", foreground="orange")
                print("No plot data to load")
                
        except Exception as e:
            print(f"Error in load_and_display_plot_report: {e}")
            import traceback
            traceback.print_exc()
            self.status_label.config(text="Error loading plot data", foreground="red")


if __name__ == "__main__":
    import multiprocessing
    multiprocessing.freeze_support()
    app = StarVisualizationGUI()
    app.mainloop()
