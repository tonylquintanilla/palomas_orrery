# save_utils.py

"""
Consolidated utility functions for saving Plotly visualizations.

This module provides a unified API for saving visualizations across all
Paloma's Orrery modules, with consistent behavior for:
- Interactive HTML (CDN - small files, requires internet)
- Interactive HTML (Offline - larger files, works anywhere)
- Static images (PNG, requires kaleido package)

Dependencies:
    - kaleido>=0.2.1 : Required for saving static images (PNG, JPG, SVG, PDF)
                       Install with: pip install kaleido

Usage:
    from save_utils import save_visualization, show_and_save
    
    # Dialog-based save (GUI applications)
    save_visualization(fig, "my_visualization")
    
    # Show in browser first, then offer save dialog
    show_and_save(fig, "my_visualization")
    
    # Direct save without dialog (scripts)
    save_visualization(fig, "my_visualization", mode='direct', 
                       output_path="output.html")

HTML Options:
    - CDN (default): ~10 KB files, requires internet connection to view
    - Offline: ~5 MB files, works without internet (embeds Plotly.js)

Author: Tony Quintanilla / Paloma's Orrery
"""

import tkinter as tk
from tkinter import filedialog, messagebox
import os
import sys
import tempfile
import webbrowser
import threading
import platform

# Module-level state for remembering last save directory within session
_last_save_directory = None


def _get_initial_directory():
    """Get the initial directory for file dialogs.
    
    Returns the last used directory if available, otherwise Documents folder.
    """
    global _last_save_directory
    
    if _last_save_directory and os.path.isdir(_last_save_directory):
        return _last_save_directory
    
    # Default to Documents folder
    if platform.system() == 'Windows':
        docs = os.path.join(os.path.expanduser('~'), 'Documents')
    elif platform.system() == 'Darwin':  # macOS
        docs = os.path.join(os.path.expanduser('~'), 'Documents')
    else:  # Linux
        docs = os.path.expanduser('~')
    
    if os.path.isdir(docs):
        return docs
    return os.getcwd()


def _update_last_directory(file_path):
    """Update the remembered directory based on a saved file path."""
    global _last_save_directory
    if file_path:
        _last_save_directory = os.path.dirname(file_path)


def _is_main_thread():
    """Check if we're running in the main thread."""
    return threading.current_thread() is threading.main_thread()


def _is_macos():
    """Check if we're running on macOS."""
    return platform.system() == 'Darwin'


def _write_html(fig, file_path, offline=False, auto_play=False):
    """Write HTML file with appropriate settings.
    
    Parameters:
        fig: Plotly figure object
        file_path: Output file path
        offline: If True, embed Plotly.js (~5MB). If False, use CDN (~10KB)
        auto_play: If True, start animations automatically
    """
    include_plotlyjs = True if offline else 'cdn'
    
    fig.write_html(
        file_path,
        include_plotlyjs=include_plotlyjs,
        auto_play=auto_play,
        full_html=True,
        config={'displayModeBar': True}
    )


def save_visualization(fig, default_name, mode='dialog', output_path=None,
                       offline=False, auto_play=False, open_browser=False):
    """
    Unified save function for all Plotly visualizations.
    
    Parameters:
        fig: Plotly figure object
        default_name: Default filename without extension
        mode: Save mode
            - 'dialog': Show save dialog with format choice (default)
            - 'direct': Save directly to output_path, no dialog
            - 'temp': Save to temp file and open in browser (no permanent save)
        output_path: For 'direct' mode, the output file path
        offline: For 'direct' mode, whether to embed Plotly.js
        auto_play: Whether to auto-play animations
        open_browser: Whether to open the saved file in browser
    
    Returns:
        str or None: Path to saved file, or None if cancelled/failed
    """
    if mode == 'temp':
        return _save_temp_and_open(fig, auto_play)
    elif mode == 'direct':
        return _save_direct(fig, output_path, offline, auto_play, open_browser)
    else:  # mode == 'dialog'
        return _save_with_dialog(fig, default_name, auto_play, open_browser)


def _save_temp_and_open(fig, auto_play=False):
    """Save to temporary file and open in browser."""
    try:
        with tempfile.NamedTemporaryFile(suffix='.html', delete=False, mode='w') as tmp:
            temp_path = tmp.name
        
        # Use CDN for temp files (faster to create)
        _write_html(fig, temp_path, offline=False, auto_play=auto_play)
        webbrowser.open(f'file://{os.path.abspath(temp_path)}')
        print(f"Visualization opened in browser: {temp_path}")
        
        # Schedule cleanup after delay
        def cleanup():
            try:
                if os.path.exists(temp_path):
                    os.unlink(temp_path)
            except Exception as e:
                print(f"Note: Could not clean up temp file: {e}")
        
        timer = threading.Timer(30.0, cleanup)
        timer.daemon = True
        timer.start()
        
        return temp_path
        
    except Exception as e:
        print(f"Error creating temporary visualization: {e}")
        return None


def _save_direct(fig, output_path, offline=False, auto_play=False, open_browser=False):
    """Save directly to specified path without dialog."""
    if not output_path:
        print("Error: output_path required for direct mode")
        return None
    
    try:
        # Determine format from extension
        ext = os.path.splitext(output_path)[1].lower()
        
        if ext == '.html':
            _write_html(fig, output_path, offline=offline, auto_play=auto_play)
            print(f"Saved HTML to: {output_path}")
        elif ext in ['.png', '.jpg', '.jpeg', '.svg', '.pdf']:
            fig.write_image(output_path)
            print(f"Saved image to: {output_path}")
        else:
            # Default to HTML
            if not output_path.endswith('.html'):
                output_path += '.html'
            _write_html(fig, output_path, offline=offline, auto_play=auto_play)
            print(f"Saved HTML to: {output_path}")
        
        if open_browser and ext == '.html':
            webbrowser.open(f'file://{os.path.abspath(output_path)}')
        
        return output_path
        
    except ImportError:
        print("Error: kaleido package required for image export.")
        print("Install with: pip install kaleido")
        return None
    except Exception as e:
        print(f"Error saving visualization: {e}")
        return None


def _save_with_dialog(fig, default_name, auto_play=False, open_browser=False):
    """Save with interactive dialog for format selection."""
    
    # Check for macOS thread safety issue
    if _is_macos() and not _is_main_thread():
        print("Save dialog skipped (macOS thread safety)")
        print("Use File > Save As in your browser to save the visualization")
        return _save_temp_and_open(fig, auto_play)
    
    root = None
    saved_path = None
    
    try:
        # Create root window for dialogs
        root = tk.Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        
        # Ask if user wants to save
        save_response = messagebox.askyesno(
            "Save Visualization",
            "Would you like to save this visualization?",
            parent=root
        )
        
        if not save_response:
            print("User chose not to save")
            return None
        
        # Format selection dialog
        format_window = tk.Toplevel(root)
        format_window.title("Save Format")
        format_window.attributes('-topmost', True)
        format_window.grab_set()
        
        # Center the window
        format_window.geometry("350x200")
        format_window.resizable(False, False)
        
        # Variable to store selection
        format_var = tk.StringVar(value="html_cdn")
        
        tk.Label(format_window, text="Choose save format:", 
                 font=('TkDefaultFont', 10, 'bold')).pack(pady=(15, 10))
        
        tk.Radiobutton(format_window, text="Interactive HTML - Standard (~10 KB, needs internet)",
                       variable=format_var, value="html_cdn").pack(anchor='w', padx=20)
        tk.Radiobutton(format_window, text="Interactive HTML - Offline (~5 MB, works anywhere)",
                       variable=format_var, value="html_offline").pack(anchor='w', padx=20)
        tk.Radiobutton(format_window, text="Static PNG image",
                       variable=format_var, value="png").pack(anchor='w', padx=20)
        
        # Result holder
        result = {'confirmed': False}
        
        def on_ok():
            result['confirmed'] = True
            format_window.destroy()
        
        def on_cancel():
            format_window.destroy()
        
        button_frame = tk.Frame(format_window)
        button_frame.pack(pady=20)
        tk.Button(button_frame, text="OK", command=on_ok, width=10).pack(side='left', padx=5)
        tk.Button(button_frame, text="Cancel", command=on_cancel, width=10).pack(side='left', padx=5)
        
        # Wait for dialog
        format_window.wait_window()
        
        if not result['confirmed']:
            print("User cancelled format selection")
            return None
        
        format_choice = format_var.get()
        initial_dir = _get_initial_directory()
        
        # File save dialog based on format
        if format_choice == "png":
            file_path = filedialog.asksaveasfilename(
                parent=root,
                initialdir=initial_dir,
                initialfile=f"{default_name}.png",
                defaultextension=".png",
                filetypes=[("PNG files", "*.png")]
            )
            if file_path:
                try:
                    print(f"Saving PNG to {file_path}...")
                    fig.write_image(file_path)
                    print("PNG saved successfully.")
                    _update_last_directory(file_path)
                    saved_path = file_path
                except ImportError:
                    messagebox.showerror(
                        "Missing Dependency",
                        "The kaleido package is required for PNG export.\n"
                        "Install with: pip install kaleido",
                        parent=root
                    )
                except Exception as e:
                    messagebox.showerror("Save Error", f"Error saving PNG:\n{str(e)}", parent=root)
        
        else:  # HTML (CDN or offline)
            offline = (format_choice == "html_offline")
            size_note = "~5 MB, works offline" if offline else "~10 KB, needs internet"
            
            file_path = filedialog.asksaveasfilename(
                parent=root,
                initialdir=initial_dir,
                initialfile=f"{default_name}.html",
                defaultextension=".html",
                filetypes=[("HTML files", "*.html")]
            )
            if file_path:
                try:
                    print(f"Saving HTML ({size_note}) to {file_path}...")
                    _write_html(fig, file_path, offline=offline, auto_play=auto_play)
                    print("HTML saved successfully.")
                    _update_last_directory(file_path)
                    saved_path = file_path
                    
                    if open_browser:
                        webbrowser.open(f'file://{os.path.abspath(file_path)}')
                        
                except Exception as e:
                    messagebox.showerror("Save Error", f"Error saving HTML:\n{str(e)}", parent=root)
        
        return saved_path
        
    except Exception as e:
        print(f"Error during save operation: {e}")
        if root:
            try:
                messagebox.showerror("Save Error", f"An error occurred:\n{str(e)}", parent=root)
            except:
                pass
        return None
    
    finally:
        try:
            if root:
                root.destroy()
        except:
            pass


def show_and_save(fig, default_name, auto_play=False):
    """
    Show visualization in browser, then offer save dialog.
    
    This is the recommended function for GUI applications that want to
    display the visualization immediately and optionally save it.
    
    Parameters:
        fig: Plotly figure object
        default_name: Default filename without extension
        auto_play: Whether to auto-play animations
    
    Returns:
        str or None: Path to saved file, or None if not saved
    """
    # Check for macOS thread safety issue
    if _is_macos() and not _is_main_thread():
        print("Opening in browser (save dialog skipped for macOS thread safety)")
        print("Use File > Save As in your browser to save")
        return _save_temp_and_open(fig, auto_play)
    
    temp_path = None
    root = None
    
    try:
        # First, create and display temp file
        with tempfile.NamedTemporaryFile(suffix='.html', delete=False, mode='w') as tmp:
            temp_path = tmp.name
        
        _write_html(fig, temp_path, offline=False, auto_play=auto_play)
        webbrowser.open(f'file://{os.path.abspath(temp_path)}')
        print("Visualization opened in browser")
        
        # Now offer save dialog
        saved_path = _save_with_dialog(fig, default_name, auto_play, open_browser=False)
        
        return saved_path
        
    except Exception as e:
        print(f"Error during show_and_save: {e}")
        import traceback
        traceback.print_exc()
        return None
    
    finally:
        # Schedule cleanup of temp file
        if temp_path:
            def cleanup():
                try:
                    if os.path.exists(temp_path):
                        os.unlink(temp_path)
                except:
                    pass
            
            timer = threading.Timer(30.0, cleanup)
            timer.daemon = True
            timer.start()


# =============================================================================
# LEGACY COMPATIBILITY FUNCTIONS
# These maintain backward compatibility with existing code
# =============================================================================

def save_plot(fig, default_name):
    """
    Legacy function for backward compatibility.
    
    Equivalent to save_visualization(fig, default_name, mode='dialog')
    
    Parameters:
        fig: Plotly figure object
        default_name: Default filename without extension
    
    Returns:
        bool: True if save was successful or user declined, False on error
    """
    result = save_visualization(fig, default_name, mode='dialog')
    # Return True if saved or user cancelled (not an error), False on error
    return result is not None or result is None  # Always True for backward compat


def handle_save(fig, default_name):
    """
    Legacy function for backward compatibility.
    
    Note: This function is deprecated. Use save_visualization() instead.
    """
    save_visualization(fig, default_name, mode='dialog')


# =============================================================================
# ANIMATION-SPECIFIC FUNCTION
# =============================================================================

def show_animation_safely(fig, default_name):
    """
    Show and optionally save an animation.
    
    This is a convenience wrapper for animations that sets auto_play=False
    (letting the user control playback) and handles the show+save flow.
    
    Parameters:
        fig: Plotly figure object with animation
        default_name: Default filename without extension
    
    Returns:
        str or None: Path to saved file, or None if not saved
    """
    return show_and_save(fig, default_name, auto_play=False)


# =============================================================================
# DIRECT SAVE HELPER (for scripts like Sgr A* modules)
# =============================================================================

def save_html(fig, filename, offline=False, open_browser=True):
    """
    Simple direct save for scripts that don't need dialogs.
    
    Parameters:
        fig: Plotly figure object
        filename: Output filename (will add .html if missing)
        offline: If True, embed Plotly.js for offline viewing
        open_browser: If True, open the file in browser after saving
    
    Returns:
        str: Path to saved file
    
    Example:
        from save_utils import save_html
        fig = create_my_figure()
        save_html(fig, "my_output", open_browser=True)
    """
    if not filename.endswith('.html'):
        filename += '.html'
    
    return save_visualization(
        fig, 
        os.path.splitext(filename)[0],
        mode='direct',
        output_path=filename,
        offline=offline,
        open_browser=open_browser
    )
