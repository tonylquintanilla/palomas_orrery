# shutdown_handler.py

import os
import threading
import atexit
import signal
import webbrowser
import tempfile
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from contextlib import contextmanager
from save_utils import show_and_save as _show_and_save_impl

class PlotlyShutdownHandler:
    """Handles graceful shutdown for Plotly visualizations and associated threads."""
    
    def __init__(self):
        self.active_threads = set()
        self.is_shutting_down = False
        
        # Register shutdown handlers
        atexit.register(self.cleanup)
        signal.signal(signal.SIGINT, self.handle_interrupt)
        
    def register_thread(self, thread):
        """Register a thread to be monitored during shutdown."""
        self.active_threads.add(thread)
        
    def remove_thread(self, thread):
        """Remove a completed thread from monitoring."""
        self.active_threads.discard(thread)
        
    def cleanup(self):
        """Clean up resources during shutdown."""
        if self.is_shutting_down:
            return
            
        self.is_shutting_down = True
        print("\nCleaning up visualization resources...")
        
        # Wait for active threads to complete
        active_threads = [t for t in self.active_threads if t.is_alive()]
        if active_threads:
            print(f"Waiting for {len(active_threads)} active tasks to complete...")
            for thread in active_threads:
                thread.join(timeout=5.0)
        
        self.active_threads.clear()
        print("Cleanup complete.")
        
    def handle_interrupt(self, signum, frame):
        """Handle keyboard interrupts."""
        print("\nInterrupt received, initiating cleanup...")
        self.cleanup()

def create_monitored_thread(handler, target_func, *args, **kwargs):
    """Create a thread that's monitored by the shutdown handler."""
    def wrapper():
        try:
            target_func(*args, **kwargs)
        finally:
            handler.remove_thread(threading.current_thread())
    
    thread = threading.Thread(target=wrapper)
    handler.register_thread(thread)
    return thread

def show_figure_safely(fig, default_name):
    """
    Show and optionally save a Plotly figure with proper cleanup.
    
    This function now delegates to the consolidated save_utils module
    while maintaining backward compatibility.
    
    Parameters:
        fig: Plotly figure object
        default_name: Default filename without extension
    
    Returns:
        str or None: Path to saved file, or None if not saved
    """
    return _show_and_save_impl(fig, default_name)



