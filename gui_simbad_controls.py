# gui_simbad_controls.py
"""
GUI controls for SIMBAD rate limiting to be integrated into star_visualization_gui.py
Add this to the middle column (plot_controls_frame) of the Star Visualization GUI.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import os
import sys
from typing import Optional, Dict, Any

# Import the SIMBAD manager
from simbad_manager import SimbadConfig, SimbadQueryManager


class SimbadControlFrame(ttk.LabelFrame):
    """Frame containing SIMBAD query controls and status display."""
    
    def __init__(self, parent, **kwargs):
        """Initialize the SIMBAD control frame."""
        super().__init__(parent, text="SIMBAD Query Settings", **kwargs)
        
        # Load or create configuration
        self.config = SimbadConfig.load_from_file()
        self.query_manager: Optional[SimbadQueryManager] = None
        
        # Create GUI variables
        self.create_variables()
        self.create_widgets()
        self.load_config_to_gui()
    
    def create_variables(self):
        """Create tkinter variables for GUI controls."""
        self.vars = {
            'queries_per_second': tk.DoubleVar(value=self.config.queries_per_second),
            'batch_size': tk.IntVar(value=self.config.batch_size),
            'timeout': tk.IntVar(value=self.config.timeout),
            'max_retries': tk.IntVar(value=self.config.max_retries),
            'show_detailed_progress': tk.BooleanVar(value=self.config.show_detailed_progress),
            'pause_on_error': tk.BooleanVar(value=self.config.pause_on_error)
        }
        
        # Status variables
        self.status_text = tk.StringVar(value="Ready")
        self.progress_text = tk.StringVar(value="")
        self.rate_text = tk.StringVar(value="")
    
    def create_widgets(self):
        """Create the GUI controls."""
        # Main container with padding
        main_frame = ttk.Frame(self, padding="5")
        main_frame.pack(fill='both', expand=True)
        
        # --- Rate Limiting Section ---
        rate_frame = ttk.LabelFrame(main_frame, text="Rate Limiting", padding="5")
        rate_frame.pack(fill='x', pady=(0, 5))
        
        # Queries per second slider
        ttk.Label(rate_frame, text="Queries/Second:").grid(row=0, column=0, sticky='w')
        
        self.rate_slider = ttk.Scale(
            rate_frame,
            from_=0.5,
            to=20.0,
            orient='horizontal',
            variable=self.vars['queries_per_second'],
            command=self.update_rate_display
        )
        self.rate_slider.grid(row=0, column=1, sticky='ew', padx=5)
        
        self.rate_label = ttk.Label(rate_frame, text="5.0/s")
        self.rate_label.grid(row=0, column=2, padx=5)
        
        # Delay between queries (calculated)
        self.delay_label = ttk.Label(rate_frame, text="(200ms delay)", foreground='gray')
        self.delay_label.grid(row=0, column=3, padx=5)
        
        rate_frame.columnconfigure(1, weight=1)
        
        # --- Batch Settings Section ---
        batch_frame = ttk.LabelFrame(main_frame, text="Batch Processing", padding="5")
        batch_frame.pack(fill='x', pady=5)
        
        # Batch size
        ttk.Label(batch_frame, text="Batch Size:").grid(row=0, column=0, sticky='w')
        batch_spinbox = ttk.Spinbox(
            batch_frame,
            from_=10,
            to=200,
            increment=10,
            textvariable=self.vars['batch_size'],
            width=10
        )
        batch_spinbox.grid(row=0, column=1, padx=5, sticky='w')
        
        ttk.Label(batch_frame, text="objects per batch").grid(row=0, column=2, sticky='w')
        
        # --- Error Handling Section ---
        error_frame = ttk.LabelFrame(main_frame, text="Error Handling", padding="5")
        error_frame.pack(fill='x', pady=5)
        
        # Timeout
        ttk.Label(error_frame, text="Timeout:").grid(row=0, column=0, sticky='w')
        timeout_spinbox = ttk.Spinbox(
            error_frame,
            from_=30,
            to=600,
            increment=30,
            textvariable=self.vars['timeout'],
            width=10
        )
        timeout_spinbox.grid(row=0, column=1, padx=5, sticky='w')
        ttk.Label(error_frame, text="seconds").grid(row=0, column=2, sticky='w')
        
        # Max retries
        ttk.Label(error_frame, text="Max Retries:").grid(row=1, column=0, sticky='w', pady=2)
        retry_spinbox = ttk.Spinbox(
            error_frame,
            from_=0,
            to=10,
            increment=1,
            textvariable=self.vars['max_retries'],
            width=10
        )
        retry_spinbox.grid(row=1, column=1, padx=5, sticky='w')
        
        # Checkboxes
        detail_check = ttk.Checkbutton(
            error_frame,
            text="Show detailed progress",
            variable=self.vars['show_detailed_progress']
        )
        detail_check.grid(row=2, column=0, columnspan=3, sticky='w', pady=2)
        
        pause_check = ttk.Checkbutton(
            error_frame,
            text="Pause on error",
            variable=self.vars['pause_on_error']
        )
        pause_check.grid(row=3, column=0, columnspan=3, sticky='w', pady=2)
        
        # --- Control Buttons ---
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill='x', pady=10)
        
        ttk.Button(
            button_frame,
            text="Apply Settings",
            command=self.apply_settings
        ).pack(side='left', padx=2)
        
        ttk.Button(
            button_frame,
            text="Reset Defaults",
            command=self.reset_defaults
        ).pack(side='left', padx=2)
        
        ttk.Button(
            button_frame,
            text="Test Query",
            command=self.test_query
        ).pack(side='left', padx=2)
        
        # --- Status Display ---
        status_frame = ttk.LabelFrame(main_frame, text="Query Status", padding="5")
        status_frame.pack(fill='both', expand=True, pady=5)
        
        # Status text
        status_label = ttk.Label(status_frame, textvariable=self.status_text)
        status_label.pack(anchor='w')
        
        # Progress bar
        self.progress_bar = ttk.Progressbar(
            status_frame,
            mode='determinate',
            length=300
        )
        self.progress_bar.pack(fill='x', pady=5)
        
        # Progress text
        progress_label = ttk.Label(status_frame, textvariable=self.progress_text)
        progress_label.pack(anchor='w')
        
        # Rate display
        rate_display = ttk.Label(status_frame, textvariable=self.rate_text)
        rate_display.pack(anchor='w')
        
        # Statistics text area
        self.stats_text = tk.Text(
            status_frame,
            height=6,
            width=40,
            wrap='word',
            state='disabled'
        )
        self.stats_text.pack(fill='both', expand=True, pady=5)
    
    def update_rate_display(self, value=None):
        """Update the rate display when slider moves."""
        rate = self.vars['queries_per_second'].get()
        self.rate_label.config(text=f"{rate:.1f}/s")
        
        # Calculate and display delay
        delay_ms = 1000 / rate if rate > 0 else 1000
        self.delay_label.config(text=f"({delay_ms:.0f}ms delay)")
    
    def apply_settings(self):
        """Apply current settings to configuration."""
        try:
            # Update config from GUI
            self.config.queries_per_second = self.vars['queries_per_second'].get()
            self.config.batch_size = self.vars['batch_size'].get()
            self.config.timeout = self.vars['timeout'].get()
            self.config.max_retries = self.vars['max_retries'].get()
            self.config.show_detailed_progress = self.vars['show_detailed_progress'].get()
            self.config.pause_on_error = self.vars['pause_on_error'].get()
            
            # Save to file
            self.config.save_to_file()
            
            # Create new query manager with updated config
            self.query_manager = SimbadQueryManager(
                self.config,
                progress_callback=self.update_progress
            )
            
            self.status_text.set("Settings applied successfully")
            messagebox.showinfo("Success", "SIMBAD settings have been applied and saved.")
        
        except Exception as e:
            self.status_text.set(f"Error: {str(e)}")
            messagebox.showerror("Error", f"Failed to apply settings: {str(e)}")
    
    def reset_defaults(self):
        """Reset to default configuration."""
        self.config = SimbadConfig()  # Create default config
        self.load_config_to_gui()
        self.status_text.set("Reset to default settings")
    
    def load_config_to_gui(self):
        """Load configuration values into GUI controls."""
        self.vars['queries_per_second'].set(self.config.queries_per_second)
        self.vars['batch_size'].set(self.config.batch_size)
        self.vars['timeout'].set(self.config.timeout)
        self.vars['max_retries'].set(self.config.max_retries)
        self.vars['show_detailed_progress'].set(self.config.show_detailed_progress)
        self.vars['pause_on_error'].set(self.config.pause_on_error)
        self.update_rate_display()
    
    def test_query(self):
        """Run a test query to verify settings."""
        self.apply_settings()  # Ensure latest settings are applied
        
        if not self.query_manager:
            self.query_manager = SimbadQueryManager(
                self.config,
                progress_callback=self.update_progress
            )
        
        # Test with a few well-known objects
        test_objects = ["Sirius", "Vega", "Polaris"]
        
        self.status_text.set("Running test query...")
        self.progress_bar['value'] = 0
        
        # Run query in a separate thread to avoid blocking GUI
        import threading
        
        def run_test():
            try:
                results = self.query_manager.query_objects(test_objects)
                
                # Display results
                self.display_stats(self.query_manager.stats)
                
                # Show successful results
                success_count = sum(1 for r in results.values() if r.get('star_name'))
                self.status_text.set(f"Test complete: {success_count}/{len(test_objects)} successful")
                
            except Exception as e:
                self.status_text.set(f"Test failed: {str(e)}")
        
        thread = threading.Thread(target=run_test, daemon=True)
        thread.start()
    
    def update_progress(self, current: int, total: int, message: str = ""):
        """Callback for progress updates from query manager."""
        if total > 0:
            progress = (current / total) * 100
            self.progress_bar['value'] = progress
            self.progress_text.set(f"{current}/{total} - {message}")
        
        # Update rate display
        if self.query_manager:
            rate_stats = self.query_manager.rate_limiter.get_stats()
            self.rate_text.set(
                f"Actual rate: {rate_stats['actual_rate']:.1f}/s | "
                f"Target: {rate_stats['target_rate']:.1f}/s"
            )
    
    def display_stats(self, stats):
        """Display query statistics in the text area."""
        self.stats_text.config(state='normal')
        self.stats_text.delete('1.0', 'end')
        self.stats_text.insert('1.0', stats.get_summary())
        self.stats_text.config(state='disabled')
    
    def get_query_manager(self) -> SimbadQueryManager:
        """Get the current query manager instance."""
        if not self.query_manager:
            self.query_manager = SimbadQueryManager(
                self.config,
                progress_callback=self.update_progress
            )
        return self.query_manager


# Integration function to add to star_visualization_gui.py
def add_simbad_controls_to_gui(plot_controls_frame):
    """
    Add SIMBAD controls to the Star Visualization GUI.
    This should be called in star_visualization_gui.py to add the controls
    to the middle column (plot_controls_frame).
    
    Usage in star_visualization_gui.py:
    
        from gui_simbad_controls import add_simbad_controls_to_gui
        
        # After creating plot_controls_frame...
        simbad_controls = add_simbad_controls_to_gui(plot_controls_frame)
    """
    # Create and pack the SIMBAD control frame
    simbad_frame = SimbadControlFrame(plot_controls_frame)
    simbad_frame.pack(fill='x', pady=10)
    
    # Add a separator
    ttk.Separator(plot_controls_frame, orient='horizontal').pack(fill='x', pady=5)
    
    return simbad_frame


# Example of modifying existing star_properties.py to use the new manager
def enhanced_query_simbad_for_star_properties(missing_ids, existing_properties, 
                                              properties_file, gui_controls=None):
    """
    Enhanced version that can use GUI controls if available.
    
    Args:
        missing_ids: List of star IDs to query
        existing_properties: Existing property dictionary
        properties_file: File to save properties
        gui_controls: Optional SimbadControlFrame instance
    """
    if gui_controls:
        # Use GUI-configured manager
        manager = gui_controls.get_query_manager()
    else:
        # Fall back to default configuration
        config = SimbadConfig.load_from_file()
        manager = SimbadQueryManager(config)
    
    # Query objects
    updated_properties = manager.query_objects(
        missing_ids,
        existing_properties,
        properties_file
    )
    
    # Display statistics if GUI is available
    if gui_controls:
        gui_controls.display_stats(manager.stats)
    
    return updated_properties


# Standalone test
if __name__ == "__main__":
    root = tk.Tk()
    root.title("SIMBAD Query Controls Test")
    root.geometry("500x700")
    
    # Create the control frame
    controls = SimbadControlFrame(root)
    controls.pack(fill='both', expand=True, padx=10, pady=10)
    
    root.mainloop()
