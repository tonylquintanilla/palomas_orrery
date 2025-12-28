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
    import threading

    # Create and display temporary HTML file
    temp_path = None
    root = None
    
    try:
        # First, create temporary file for browser display
        with tempfile.NamedTemporaryFile(suffix='.html', delete=False) as tmp:
            temp_path = tmp.name
            fig.write_html(
                temp_path,
                include_plotlyjs=True,
                config={'displayModeBar': True}
            )
        
        # Open in browser immediately
        webbrowser.open(f'file://{os.path.abspath(temp_path)}')
        print(f"Visualization opened in browser")

        # Check if we're in the main thread - dialogs crash macOS if called from worker thread
        import platform
        in_main_thread = threading.current_thread() is threading.main_thread()
        
        if not in_main_thread and platform.system() == 'Darwin':
            # On macOS, skip save dialog when in worker thread to avoid crash
            print("Save dialog skipped (macOS thread safety) - use File menu in browser to save")
            return
        
        # Create root window for dialogs (only safe on main thread or non-macOS)
        root = tk.Tk()
        root.withdraw()
        root.attributes('-topmost', True)

        # Single initial dialog - do you want to save?
        save_response = messagebox.askyesno(
            "Save Visualization",
            "Would you like to save this visualization?",
            parent=root
        )

        if save_response:
            # Ask for format only if they want to save
            format_choice = messagebox.askyesno(
                "Save Format",
                "Choose save format:\n\n"
                "Yes - Static PNG image\n"
                "No - Interactive HTML file",
                parent=root
            )
            
            if format_choice:  # User chose PNG
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
                    except Exception as e:
                        messagebox.showerror(
                            "Save Error",
                            f"Error saving PNG: {str(e)}",
                            parent=root
                        )
            else:  # User chose HTML
                file_path = filedialog.asksaveasfilename(
                    parent=root,
                    initialfile=f"{default_name}.html",
                    defaultextension=".html",
                    filetypes=[("HTML files", "*.html")]
                )
                if file_path:
                    try:
                        fig.write_html(file_path, include_plotlyjs='cdn', auto_play=False)
                        print(f"Interactive plot saved to: {file_path}")
                    except Exception as e:
                        messagebox.showerror(
                            "Save Error",
                            f"Error saving HTML: {str(e)}",
                            parent=root
                        )
        else:
            print("User chose not to save the visualization")

    except Exception as e:
        print(f"Error during visualization/save operation: {e}")
        import traceback
        traceback.print_exc()
    
    finally:
        # Clean up the Tk root window
        try:
            if root:
                root.destroy()
        except:
            pass
        
        # Schedule cleanup of temporary file after a delay
        def cleanup_temp():
            try:
                if temp_path and os.path.exists(temp_path):
                    os.unlink(temp_path)
                    print(f"Cleaned up temporary file: {temp_path}")
            except Exception as e:
                print(f"Error cleaning up temporary file: {e}")
        
        # Use a timer to delay cleanup, ensuring browser has time to load the file
        if temp_path:
            timer = threading.Timer(10.0, cleanup_temp)
            timer.daemon = True
            timer.start()

