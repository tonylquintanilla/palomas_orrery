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
    """Show and optionally save a Plotly figure with proper cleanup."""
    import tkinter as tk
    from tkinter import filedialog, messagebox
    import webbrowser
    import os
    import tempfile

    # First, create and display the temporary HTML file immediately
    with tempfile.NamedTemporaryFile(suffix='.html', delete=False) as tmp:
        temp_path = tmp.name
        fig.write_html(temp_path, include_plotlyjs='cdn', auto_play=False)
        webbrowser.open(f'file://{os.path.abspath(temp_path)}')

    # Then handle the save options
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)

    try:
        # PNG save option
        save_response = messagebox.askyesno(
            "Save Plot",
            "Would you like to save this plot as a PNG?\n\n"
            "Yes - Save as PNG\n"
            "No - Skip saving as PNG",
            parent=root
        )

        if save_response:
            file_path = filedialog.asksaveasfilename(
                parent=root,
                initialfile=f"{default_name}.png",
                defaultextension=".png",
                filetypes=[("PNG files", "*.png")]
            )
            if file_path:
                try:
                    fig.write_image(file_path)
                    print(f"Plot saved as PNG: {file_path}")
                except ImportError:
                    messagebox.showerror(
                        "Missing Dependency",
                        "The kaleido package is required for saving static images.\n"
                        "Please install it with: pip install kaleido",
                        parent=root
                    )

        # HTML save option
        html_response = messagebox.askyesno(
            "Save Interactive Plot",
            "Would you like to save the interactive HTML version?",
            parent=root
        )

        if html_response:
            file_path = filedialog.asksaveasfilename(
                parent=root,
                initialfile=f"{default_name}.html",
                defaultextension=".html",
                filetypes=[("HTML files", "*.html")]
            )
            if file_path:
                fig.write_html(file_path, include_plotlyjs='cdn', auto_play=False)
                print(f"Plot saved as HTML: {file_path}")

    except Exception as e:
        print(f"Error during save operation: {e}")
        messagebox.showerror(
            "Save Error",
            f"An error occurred while saving:\n{str(e)}",
            parent=root
        )
    finally:
        root.destroy()

        # Schedule cleanup of temporary file
        def cleanup_temp():
            try:
                if os.path.exists(temp_path):
                    os.unlink(temp_path)
            except Exception as e:
                print(f"Error cleaning up temporary file: {e}")

        # Delay cleanup to ensure browser has loaded the file
        root = tk.Tk()
        root.withdraw()
        root.after(5000, cleanup_temp)  # 5-second delay before cleanup
        root.destroy()

