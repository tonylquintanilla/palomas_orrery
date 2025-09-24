import tkinter as tk
from tkinter import ttk, scrolledtext
import time
from datetime import datetime
from typing import Dict, Any, Optional, List
import numpy as np
import pandas as pd

try:
    from object_type_analyzer import ObjectTypeAnalyzer
    ANALYZER_AVAILABLE = True
except ImportError:
    ANALYZER_AVAILABLE = False
    print("Warning: ObjectTypeAnalyzer not found. Object type analysis will be limited.")

from report_manager import ReportManager    


class PlotDataReportWidget(ttk.Frame):
    """Widget for displaying comprehensive plot data report."""
    
    
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.setup_ui()
        self.last_report_data = None
        self.generation_time = None
        
        # Initialize the object type analyzer if available
        if ANALYZER_AVAILABLE:
            self.object_analyzer = ObjectTypeAnalyzer()
        else:
            self.object_analyzer = None           
        
    def setup_ui(self):
        """Set up the UI with scrollable text display."""
        # Main frame with label
        report_frame = ttk.LabelFrame(self, text="Plot Data Report", padding=5)
        report_frame.pack(fill='both', expand=True)
        
        # Control buttons frame
        button_frame = ttk.Frame(report_frame)
        button_frame.pack(fill='x', pady=(0, 5))
        
        # Refresh button
        self.refresh_button = ttk.Button(
            button_frame, 
            text="Refresh Report",
            command=self.refresh_report,
            state='disabled'
        )
        self.refresh_button.pack(side='left', padx=(0, 5))
        
        # Export button
        self.export_button = ttk.Button(
            button_frame,
            text="Export Report",
            command=self.export_report,
            state='disabled'
        )
        self.export_button.pack(side='left')
        
        # Status label
        self.status_label = ttk.Label(button_frame, text="No plot data available")
        self.status_label.pack(side='right')
        
        # Scrollable text area
        text_frame = ttk.Frame(report_frame)
        text_frame.pack(fill='both', expand=True)
        
        v_scroll = ttk.Scrollbar(text_frame, orient='vertical')
        v_scroll.pack(side='right', fill='y')
        
        h_scroll = ttk.Scrollbar(text_frame, orient='horizontal')
        h_scroll.pack(side='bottom', fill='x')
        
        self.report_display = tk.Text(
            text_frame,
            height=30,
            width=60,
            wrap='word',
            yscrollcommand=v_scroll.set,
            xscrollcommand=h_scroll.set,
            font=('Consolas', 10),
    #        bg='#f5f5f5',
    #        bg='SystemButtonFace',
            bg='white',
            state='normal'  
        )
        self.report_display.pack(fill='both', expand=True)
        v_scroll.config(command=self.report_display.yview)
        h_scroll.config(command=self.report_display.xview)
        
        self._add_clipboard_support(self.report_display)

        # Configure text tags for formatting
        self.report_display.tag_configure('header', font=('Consolas', 12, 'bold'))
        self.report_display.tag_configure('subheader', font=('Consolas', 11, 'bold'))
        self.report_display.tag_configure('warning', foreground='#ff6600')
        self.report_display.tag_configure('error', foreground='red')
        self.report_display.tag_configure('success', foreground='green')
        self.report_display.tag_configure('info', foreground='blue')
        
        # Initial message
        self.report_display.insert('1.0', 
            "Plot Data Report\n"
            "================\n\n"
            "Generate a plot to view the data report.\n\n"
            "This report will include:\n"
            "* Data completeness metrics\n"
            "* Quality indicators and anomalies\n"
            "* Catalog coverage analysis\n"
            "* Processing diagnostics\n"
            "* Notable features and warnings")
        

    def _add_clipboard_support(self, widget):
        """Add clipboard and selection support to text widget."""
        def _copy(event=None):
            try:
                sel = widget.get("sel.first", "sel.last")
                widget.clipboard_clear()
                widget.clipboard_append(sel)
            except tk.TclError:
                pass
            return "break"
        
        def _select_all(event=None):
            widget.tag_add(tk.SEL, "1.0", tk.END)
            widget.mark_set(tk.INSERT, "1.0")
            widget.see("insert")
            return "break"
        
        widget.bind("<Control-c>", _copy)
        widget.bind("<Control-a>", _select_all)
        menu = tk.Menu(widget, tearoff=0)
        menu.add_command(label="Copy", command=_copy)
        menu.add_command(label="Select All", command=_select_all)
        widget.bind("<Button-3>", lambda e: menu.post(e.x_root, e.y_root))        
        
    def generate_report(self, combined_df: pd.DataFrame, counts_dict: Dict, 
                       processing_times: Optional[Dict] = None,
                       mode: str = 'magnitude', limit_value: float = None) -> str:
        """
        Generate comprehensive plot data report.
        
        Parameters:
            combined_df: The dataframe with all star data
            counts_dict: Dictionary with star counts and statistics
            processing_times: Optional timing information
            mode: 'magnitude' or 'distance'
            limit_value: The limiting magnitude or distance
        """
        self.last_report_data = {
            'combined_df': combined_df,
            'counts_dict': counts_dict,
            'processing_times': processing_times,
            'mode': mode,
            'limit_value': limit_value
        }
        self.generation_time = datetime.now()
        
        report_lines = []
        report_lines.append("=" * 46)
        report_lines.append("PLOT DATA REPORT")
        report_lines.append("=" * 46)
        report_lines.append(f"Generated: {self.generation_time.strftime('%Y-%m-%d %H:%M:%S')}")
        report_lines.append(f"Plot Mode: {mode.capitalize()}-based")
        
        if mode == 'magnitude':
            report_lines.append(f"Limiting Magnitude: {limit_value}")
        else:
            report_lines.append(f"Distance Limit: {limit_value} light-years")
        
        report_lines.append("")
        
        # Section 1: Basic Statistics
        report_lines.append("-" * 52)
        report_lines.append("1. BASIC PLOT STATISTICS")
        report_lines.append("-" * 52)
        
        total_stars = counts_dict.get('total_stars', len(combined_df))
        report_lines.append(f"Total Stars in Dataset: {total_stars:,d}")
        
        # Catalog breakdown
        hip_bright = counts_dict.get('hip_bright_count', 0)
        hip_mid = counts_dict.get('hip_mid_count', 0)
        gaia_mid = counts_dict.get('gaia_mid_count', 0)
        gaia_faint = counts_dict.get('gaia_faint_count', 0)
        
        report_lines.append("\nCatalog Distribution:")
        report_lines.append(f"  Hipparcos Bright (Vmag <= 1.73): {hip_bright:,d}")
        report_lines.append(f"  Hipparcos Mid (1.73 < Vmag <= 4.0): {hip_mid:,d}")
        report_lines.append(f"  Gaia Mid (1.73 < Vmag <= 4.0): {gaia_mid:,d}")
        report_lines.append(f"  Gaia Faint (Vmag > 4.0): {gaia_faint:,d}")
        
        # Section 2: Data Completeness
        report_lines.append("\n" + "-" * 52)
        report_lines.append("2. DATA COMPLETENESS METRICS")
        report_lines.append("-" * 52)
        
        # Temperature completeness
        temp_valid = (combined_df['Temperature'] > 0).sum() if 'Temperature' in combined_df else 0
        temp_missing = total_stars - temp_valid
        temp_percent = (temp_valid / total_stars * 100) if total_stars > 0 else 0
        
        report_lines.append("\nTemperature Data:")
        report_lines.append(f"  Valid temperatures: {temp_valid:,d} ({temp_percent:.1f}%)")
        report_lines.append(f"  Missing temperatures: {temp_missing:,d}")
        
        # Temperature source breakdown
        source_counts = counts_dict.get('source_counts', {})
        if source_counts:
            report_lines.append("\n  Temperature Sources:")
            report_lines.append(f"    B-V color matched: {source_counts.get('bv_matched', 0):,d}")
            report_lines.append(f"    B-V only: {source_counts.get('bv_only', 0):,d}")
            report_lines.append(f"    Spectral type (hot): {source_counts.get('spectral_type_hot', 0):,d}")
            report_lines.append(f"    Spectral type (cool): {source_counts.get('spectral_type_cool', 0):,d}")
            report_lines.append(f"    Spectral type only: {source_counts.get('spectral_type_only', 0):,d}")
            report_lines.append(f"    Disagreement: {source_counts.get('spectral_type_disagreement', 0):,d}")
            report_lines.append(f"    No source: {source_counts.get('none', 0):,d}")
        
        # Luminosity completeness
        lum_valid = (combined_df['Luminosity'] > 0).sum() if 'Luminosity' in combined_df else 0
        lum_missing = total_stars - lum_valid
        lum_percent = (lum_valid / total_stars * 100) if total_stars > 0 else 0
        
        report_lines.append("\nLuminosity Data:")
        report_lines.append(f"  Valid luminosities: {lum_valid:,d} ({lum_percent:.1f}%)")
        report_lines.append(f"  Missing luminosities: {lum_missing:,d}")
        
        # Estimation results
        estimation_results = counts_dict.get('estimation_results', {})
        if estimation_results:
            bright_estimates = estimation_results.get('bright_star_estimates', 0)
            if bright_estimates > 0:
                report_lines.append(f"  Estimated (bright stars): {bright_estimates:,d}")
        
        # Plottability
        plottable = counts_dict.get('plottable_count', 0)
        plottable_percent = (plottable / total_stars * 100) if total_stars > 0 else 0
        not_plottable = total_stars - plottable
        
        report_lines.append("\nPlottable Stars:")
        report_lines.append(f"  Total plottable: {plottable:,d} ({plottable_percent:.1f}%)")

        if not_plottable > 0:
            report_lines.append(f"  Not plottable: {not_plottable:,d} (missing temperature or luminosity)")
        else:
            report_lines.append(f"  Not plottable: 0")        
        
        # Section 3: Data Quality Indicators
        report_lines.append("\n" + "-" * 52)
        report_lines.append("3. DATA QUALITY INDICATORS")
        report_lines.append("-" * 52)
        
        # Check for anomalies
        anomalies = []
        
        # Temperature anomalies
        if 'Temperature' in combined_df:
            temp_array = combined_df['Temperature'].dropna()
            if len(temp_array) > 0:
                temp_outliers_low = (temp_array < 2000).sum()
                temp_outliers_high = (temp_array > 50000).sum()
                if temp_outliers_high > 0:
                    anomalies.append(f"  Warning: {temp_outliers_high} stars with T > 50000K (Wolf-Rayet stars or data errors)")
        
        # Luminosity anomalies
        if 'Luminosity' in combined_df:
            lum_array = combined_df['Luminosity'].dropna()
            if len(lum_array) > 0:
                lum_negative = (lum_array <= 0).sum()
                lum_extreme_low = (lum_array < 0.00001).sum()
                lum_extreme_high = (lum_array > 100000).sum()
                
                if lum_negative > 0:
                    anomalies.append(f"  Warning: {lum_negative} stars with L ≤ 0 (impossible - calculation errors)")
                if lum_extreme_low > 0:
                    anomalies.append(f"  Warning: {lum_extreme_low} stars with L < 0.00001 Lsun (very faint white dwarfs or errors)")
                if lum_extreme_high > 0:
                    anomalies.append(f"  Warning: {lum_extreme_high} stars with L > 100000 Lsun (hypergiants or calculation errors)")
        
        # Distance/parallax quality
        if 'Distance_pc' in combined_df:
            dist_array = combined_df['Distance_pc'].dropna()
            if len(dist_array) > 0:
                dist_negative = (dist_array <= 0).sum()
                if dist_negative > 0:
                    anomalies.append(f"  Warning: {dist_negative} stars with invalid distance (parallax calculation errors)")
        
        if anomalies:
            report_lines.append("\nAnomalies Detected:")
            report_lines.extend(anomalies)
        else:
            report_lines.append("\nOK No significant anomalies detected")
        
        # Check for duplicates
        if 'HIP' in combined_df:
            hip_duplicates = combined_df['HIP'].duplicated().sum()
            if hip_duplicates > 0:
                report_lines.append(f"\n  Warning: {hip_duplicates} duplicate HIP entries (database integrity issue)")
        
        # Section 4: Catalog Coverage
        report_lines.append("\n" + "-" * 52)
        report_lines.append("4. CATALOG COVERAGE ANALYSIS")
        report_lines.append("-" * 52)
        
        if 'Source_Catalog' in combined_df:
            catalog_counts = combined_df['Source_Catalog'].value_counts()
            report_lines.append("\nSource Distribution:")
            for catalog, count in catalog_counts.items():
                percent = (count / total_stars * 100) if total_stars > 0 else 0
                report_lines.append(f"  {catalog}: {count:,d} ({percent:.1f}%)")
                
        report_lines.append("\n" + "-" * 52)  # Shortened by 1
        report_lines.append("5. PROCESSING DIAGNOSTICS")
        report_lines.append("-" * 52)  # Shortened by 1
        
        if processing_times and isinstance(processing_times, dict) and processing_times:
            for key, value in processing_times.items():
                if isinstance(value, (int, float)):
                    report_lines.append(f"  {key.replace('_', ' ').title()}: {value:.2f} seconds")
                else:
                    report_lines.append(f"  {key.replace('_', ' ').title()}: {value}")
        else:
            report_lines.append("  Processing times include:")
            report_lines.append("    - Data acquisition (catalog queries)")
            report_lines.append("    - Parameter calculations (temperature, luminosity)")
            report_lines.append("    - Data preparation and validation")
            report_lines.append("    - Visualization generation")
            report_lines.append("  (Times shown when available)")

    
        # Section 6: Object Type Analysis
        report_lines.append("\n" + "-" * 52)
        report_lines.append("6. OBJECT TYPE ANALYSIS")
        report_lines.append("-" * 52)

        # DEBUG: See what columns we actually have
        print("\n" + "="*60)
        print("DEBUG: Object Type Analysis")
        print("="*60)
        print(f"Total columns in dataframe: {len(combined_df.columns)}")
        print(f"All columns: {combined_df.columns.tolist()}")

        # Check for any column with 'type' in name
        type_cols = [col for col in combined_df.columns if 'type' in col.lower()]
        print(f"Columns with 'type' in name: {type_cols}")

        # Check for any column with 'object' in name  
        obj_cols = [col for col in combined_df.columns if 'object' in col.lower()]
        print(f"Columns with 'object' in name: {obj_cols}")

        # Try to find the actual column
        type_column = None
        possible_names = ['Object_Type_Desc', 'Object_Type', 'object_type', 'Object Type', 
                        'object_type_desc', 'ObjectType', 'otype']

        for name in possible_names:
            if name in combined_df.columns:
                type_column = name
                non_null = combined_df[name].notna().sum()
                print(f"Found '{name}' with {non_null} non-null values")
                if non_null > 0:
                    print(f"Sample values: {combined_df[name].dropna().head(3).tolist()}")
                    break

        print("="*60)

        # Now run the analysis if we found the column
        if type_column and combined_df[type_column].notna().any():
            if self.object_analyzer:
                analysis_results = self.object_analyzer.analyze_distribution(combined_df[type_column])
                analysis_lines = self.object_analyzer.format_report_section(analysis_results)
                report_lines.extend(analysis_lines)
                self.last_analysis_results = analysis_results
            else:
                # Simple fallback
                object_types = combined_df[type_column].value_counts()
                report_lines.append(f"\nFound {len(object_types)} unique object types")
                for obj_type, count in object_types.head(5).items():
                    report_lines.append(f"  • {obj_type}: {count}")
        else:
            report_lines.append("\n  Object type information not available in dataset")
            if type_column:
                report_lines.append(f"  Column '{type_column}' found but all values are null")
            else:
                report_lines.append(f"  No object type column found")
                report_lines.append(f"  Searched for: {', '.join(possible_names[:3])}")

        # Section 7: Warnings and Recommendations
        report_lines.append("\n" + "-" * 52)
        report_lines.append("7. WARNINGS AND RECOMMENDATIONS")
        report_lines.append("-" * 52)
        
        warnings = []
        
        # Check completeness thresholds
        if temp_percent < 90:
            warnings.append(f"Warning: Temperature completeness is {temp_percent:.1f}% (< 90%)")
        if lum_percent < 90:
            warnings.append(f"Warning: Luminosity completeness is {lum_percent:.1f}% (< 90%)")
        if plottable_percent < 80:
            warnings.append(f"Warning: Only {plottable_percent:.1f}% of stars are plottable")
        
        # Check for significant missing data
        if temp_missing > 100:
            warnings.append(f"Warning: {temp_missing:,d} stars missing temperature data")
        if lum_missing > 100:
            warnings.append(f"Warning: {lum_missing:,d} stars missing luminosity data")
        
        if warnings:
            report_lines.append("\nWarnings:")
            report_lines.extend(["  " + w for w in warnings])
            
            # Add recommendations
            report_lines.append("\nRecommendations:")
            if temp_percent < 90 or lum_percent < 90:
                report_lines.append("  * Consider adjusting search parameters for better data coverage")
            if mode == 'magnitude' and limit_value and limit_value > 6:
                report_lines.append("  * Large magnitude range may include incomplete Gaia data")
            if mode == 'distance' and limit_value and limit_value > 50:
                report_lines.append("  * Large distance range may have increased parallax uncertainties")
        else:
            report_lines.append("\nOK No warnings - data quality appears good")
        
        report_lines.append("\n" + "=" * 46)
        report_lines.append("END OF REPORT")
        report_lines.append("=" * 46)
        
        return "\n".join(report_lines)
    
    def update_report(self, combined_df: pd.DataFrame, counts_dict: Dict,
                     processing_times: Optional[Dict] = None,
                     mode: str = 'magnitude', limit_value: float = None):
        """Update the report display with new data."""
        # Generate the report
        report_text = self.generate_report(
            combined_df, counts_dict, processing_times, mode, limit_value
        )
        
        # Update display
        self.report_display.delete('1.0', tk.END)
        
        # Add formatted text
        lines = report_text.split('\n')
        for line in lines:
            if line.startswith('='):
                self.report_display.insert(tk.END, line + '\n', 'header')
            elif line.startswith('-'):
                self.report_display.insert(tk.END, line + '\n', 'subheader')
            elif line.startswith('  Warning:'):
                self.report_display.insert(tk.END, line + '\n', 'warning')
            elif line.startswith('  OK') or line.startswith('OK'):
                self.report_display.insert(tk.END, line + '\n', 'success')
            elif line.startswith('1.') or line.startswith('2.') or line.startswith('3.') or \
                 line.startswith('4.') or line.startswith('5.') or line.startswith('6.') or \
                 line.startswith('7.'):
                self.report_display.insert(tk.END, line + '\n', 'subheader')
            else:
                self.report_display.insert(tk.END, line + '\n')
        
        self.report_display.config(state='normal')

        # Update status
        self.status_label.config(text=f"Report updated: {datetime.now().strftime('%H:%M:%S')}")
        self.refresh_button.config(state='normal')
        self.export_button.config(state='normal')
    

    def refresh_report(self):
        """Refresh the report with the last data."""
        if self.last_report_data:
            if isinstance(self.last_report_data, dict) and 'metadata' in self.last_report_data:
                # New format
                self.display_report(self.last_report_data)
            else:
                # Old format
                self.update_report(**self.last_report_data)            
    
    def export_report(self):
        """Export the report to a text file."""
        if not self.last_report_data:
            return
        
        from tkinter import filedialog
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        mode = self.last_report_data.get('mode', 'unknown')
        default_name = f"plot_report_{mode}_{timestamp}.txt"
        
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
            initialfile=default_name
        )
        
        if filename:
            try:
                report_text = self.report_display.get('1.0', tk.END)
                with open(filename, 'w') as f:
                    f.write(report_text)
                self.status_label.config(text=f"Report exported successfully")
            except Exception as e:
                self.status_label.config(text=f"Export failed: {str(e)}")

    def display_report(self, report_data: Dict):
        """Display pre-generated report from visualization script."""
        self.last_report_data = report_data
        self.generation_time = datetime.now()
        
        self.report_display.config(state='normal')
        self.report_display.delete('1.0', tk.END)
        
        # Use the analyzer to format the complete report
        if self.object_analyzer:
            report_lines = self.object_analyzer.format_complete_report(report_data)
        else:
            # Fallback if analyzer not available
            report_lines = self._format_basic_report(report_data)
        
        # Display with formatting
        for line in report_lines:
            if line.startswith("="):
                self.report_display.insert(tk.END, line + '\n', 'header')
            elif line.startswith("-"):
                self.report_display.insert(tk.END, line + '\n', 'subheader')
            elif any(line.startswith(f"{i}.") for i in range(1, 8)):
                self.report_display.insert(tk.END, line + '\n', 'subheader')
            elif "WARNING" in line or "CRITICAL" in line:
                self.report_display.insert(tk.END, line + '\n', 'warning')
            elif line.startswith("✓") or "OK" in line:
                self.report_display.insert(tk.END, line + '\n', 'success')
            elif line.startswith("→"):
                self.report_display.insert(tk.END, line + '\n', 'info')
            else:
                self.report_display.insert(tk.END, line + '\n')
        
        self.report_display.config(state='disabled')
        self.status_label.config(text=f"Report updated: {datetime.now().strftime('%H:%M:%S')}")
        self.refresh_button.config(state='normal')
        self.export_button.config(state='normal')

    def update_report_from_exchange(self, exchange_data: Dict):
        """Update report from exchange data - handles both old and new formats."""
        if 'report_data' in exchange_data:
            # New format with pre-generated report
            self.display_report(exchange_data['report_data'])
        elif 'plot_stats' in exchange_data:
            # Handle intermediate format
            self._handle_plot_stats(exchange_data['plot_stats'])
        else:
            # Old format - create pseudo dataframe and use old method
            self._handle_legacy_format(exchange_data)

    def _handle_plot_stats(self, plot_stats: Dict):
        """Handle plot statistics format (intermediate)."""
        # Create a minimal dataframe for backward compatibility
        import pandas as pd
        
        total_stars = plot_stats.get('total_stars', 0)
        temp_valid = plot_stats.get('temp_valid', 0)
        lum_valid = plot_stats.get('lum_valid', 0)
        
        if total_stars > 0:
            pseudo_df = pd.DataFrame({
                'Temperature': [1] * temp_valid + [0] * (total_stars - temp_valid),
                'Luminosity': [1] * lum_valid + [0] * (total_stars - lum_valid),
                'Source_Catalog': ['Unknown'] * total_stars,
                'Apparent_Magnitude': [0] * total_stars
            })
        else:
            pseudo_df = pd.DataFrame()
        
        counts_dict = plot_stats.get('catalog_counts', {})
        processing_times = plot_stats.get('processing_times', {})
        mode = plot_stats.get('mode', 'unknown')
        limit_value = plot_stats.get('limit_value', 0)
        
        self.update_report(pseudo_df, counts_dict, processing_times, mode, limit_value)

    def _handle_legacy_format(self, exchange_data: Dict):
        """Handle the original format for backward compatibility."""
        # Similar to _handle_plot_stats but directly from exchange_data
        import pandas as pd
        
        total_stars = exchange_data.get('total_stars', 0)
        temp_valid = exchange_data.get('temp_valid', 0)
        lum_valid = exchange_data.get('lum_valid', 0)
        
        if total_stars > 0:
            pseudo_df = pd.DataFrame({
                'Temperature': [1] * temp_valid + [0] * (total_stars - temp_valid),
                'Luminosity': [1] * lum_valid + [0] * (total_stars - lum_valid)
            })
        else:
            pseudo_df = pd.DataFrame()
        
        self.update_report(
            pseudo_df,
            exchange_data.get('counts_dict', {}),
            exchange_data.get('processing_times', {}),
            exchange_data.get('mode', 'unknown'),
            exchange_data.get('limit_value', 0)
        )

    def _format_basic_report(self, report_data: Dict) -> List[str]:
        """Fallback formatter if ObjectTypeAnalyzer is not available."""
        lines = []
        lines.append("=" * 46)
        lines.append("PLOT DATA REPORT")
        lines.append("=" * 46)
        
        metadata = report_data.get('metadata', {})
        lines.append(f"Generated: {metadata.get('generation_time', 'Unknown')}")
        lines.append(f"Mode: {metadata.get('mode', 'Unknown')}")
        lines.append(f"Limit: {metadata.get('limit_value', 'Unknown')}")
        lines.append("")
        
        lines.append("Note: Full analysis requires ObjectTypeAnalyzer module")
        
        return lines               


    def refresh_from_file(self):
        """Load and display the latest report from file."""
        try:
            from report_manager import ReportManager
            report_mgr = ReportManager()
            report_data = report_mgr.load_last_report()
            
            if report_data:
                self.display_report(report_data)
                print("Report refreshed from file")
            else:
                print("No report file found")
        except ImportError:
            print("ReportManager not available")

# Integration function to add to star_visualization_gui.py
def add_plot_report_to_gui(parent_frame, column=1, row=1):
    """
    Add the plot report widget to the star visualization GUI.
    
    This should be called in the setup_ui method of StarVisualizationGUI
    to add the report widget below the status window.
    """
    # Create the report widget
    report_widget = PlotDataReportWidget(parent_frame)
    report_widget.grid(row=row, column=column, sticky='nsew', padx=5, pady=(10, 0))
    
    return report_widget
