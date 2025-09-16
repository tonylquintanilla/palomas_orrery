# save_utils.py

"""Utility functions for saving plots with improved error handling.

Dependencies:
    - kaleido>=0.2.1 : Required for saving static images (PNG, JPG, SVG, PDF)
                       Install with: pip install kaleido
    
Note: While HTML saves work without additional dependencies, saving to static image
formats like PNG, JPG, SVG, or PDF requires the kaleido package. If kaleido is not
installed, the script will still allow HTML saves but will raise an error when
attempting to save static images.

Example usage:
    fig = create_hr_diagram(...)  # Create your plotly figure
    save_plot(fig, "hr_diagram_example")

Actually, the HTML file generated with `include_plotlyjs='cdn'` is completely self-contained and can be viewed by anyone with a web browser - they don't need Python or any libraries installed! 

This is because when we use `include_plotlyjs='cdn'`, the HTML file includes a link to load Plotly's JavaScript library from a Content Delivery Network (CDN). When the user opens the HTML file, their browser automatically downloads the necessary Plotly JavaScript code.

The recipient can:
1. Open the HTML file in any modern web browser
2. Use all interactive features like:
   - Rotating the 3D view
   - Zooming in/out
   - Hovering to see star details
   - Using the camera controls
   - Toggling stars on/off in the legend
3. Save static images of their current view

The only requirement is an internet connection when first opening the file (to load the Plotly JavaScript from the CDN) and a modern web browser.

If you need to create a version that works completely offline, you can use `fig.write_html(file_path, include_plotlyjs=True)` instead. This will embed the Plotly JavaScript code directly in the HTML file, making it larger but able to work without internet access.

Would you like me to show you how to modify the code to generate offline-capable HTML files?
"""

import tkinter as tk
from tkinter import filedialog, messagebox
import os

def handle_save(fig, default_name):
    """Handle the actual saving of the figure."""
    try:
        from tkinter import filedialog
        
        # Force dialog to front
        root = tk.Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        
        # Ask for format preference
        format_response = messagebox.askyesno(
            "Save Format",
            "Would you like to save as interactive HTML?\n\n"
            "Yes - Save as interactive HTML\n"
            "No - Save as static image (requires kaleido package)",
            parent=root
        )
        
        if format_response:
            # Save as HTML
            root.lift()  # Bring window to front again
            file_path = filedialog.asksaveasfilename(
                parent=root,
                initialfile=f"{default_name}.html",
                defaultextension=".html",
                filetypes=[("HTML files", "*.html")]
            )
            
            if file_path:
                print(f"Saving interactive plot to {file_path}...")
                fig.write_html(file_path, include_plotlyjs='cdn', auto_play=False)
                print("Interactive plot saved successfully.")
        else:
            # Save as static image
            root.lift()  # Bring window to front again
            file_path = filedialog.asksaveasfilename(
                parent=root,
                initialfile=f"{default_name}.png",
                defaultextension=".png",
                filetypes=[
                    ("PNG files", "*.png"),
                    ("JPEG files", "*.jpg"),
                    ("SVG files", "*.svg"),
                    ("PDF files", "*.pdf")
                ]
            )
            
            if file_path:
                try:
                    print(f"Saving static image to {file_path}...")
                    fig.write_image(file_path)
                    print("Static image saved successfully.")
                except ImportError:
                    messagebox.showerror(
                        "Missing Dependency",
                        "The kaleido package is required for saving static images.\n"
                        "Please install it with: pip install kaleido",
                        parent=root
                    )
                    
    except Exception as e:
        print(f"Error saving plot: {e}")
        messagebox.showerror(
            "Save Error",
            f"An error occurred while saving the plot:\n{str(e)}",
            parent=root
        )
    finally:
        root.destroy()

def save_plot(fig, default_name):
    """
    Save plot with improved error handling and window management.
    Now offers PNG save option upfront.
    
    Parameters:
        fig: plotly figure object
        default_name: default filename without extension
    
    Returns:
        bool: True if save was successful, False otherwise
    """
    try:
        # Create root window but keep it hidden
        root = tk.Tk()
        root.withdraw()
        
        # Make it appear on top of other windows
        root.wm_attributes('-topmost', True)
        
        # Create a temporary window to force focus
        temp = tk.Toplevel(root)
        temp.wm_attributes('-topmost', True)
        temp.focus_force()
        temp.withdraw()
        
        # Ask for save format first
        format_response = messagebox.askyesno(
            "Save Format",
            "Would you like to save as PNG?\n\n"
            "Yes - Save as static PNG\n"
            "No - Save as interactive HTML",
            parent=temp
        )
        
        if format_response:
            # Save as PNG
            file_path = filedialog.asksaveasfilename(
                parent=temp,
                initialfile=f"{default_name}.png",
                defaultextension=".png",
                filetypes=[("PNG files", "*.png")]
            )
            
            if file_path:
                try:
                    print(f"Saving static image to {file_path}...")
                    fig.write_image(file_path)
                    print("Static image saved successfully.")
                except ImportError:
                    messagebox.showerror(
                        "Missing Dependency",
                        "The kaleido package is required for saving static images.\n"
                        "Please install it with: pip install kaleido",
                        parent=temp
                    )
        else:
            # Save as HTML
            file_path = filedialog.asksaveasfilename(
                parent=temp,
                initialfile=f"{default_name}.html",
                defaultextension=".html",
                filetypes=[("HTML files", "*.html")]
            )
            
            if file_path:
                print(f"Saving interactive plot to {file_path}...")
                fig.write_html(file_path, include_plotlyjs='cdn', auto_play=False)
                print("Interactive plot saved successfully.")
                
        return True
        
    except Exception as e:
        print(f"Error saving plot: {e}")
        messagebox.showerror(
            "Save Error",
            f"An error occurred while saving the plot:\n{str(e)}",
            parent=root
        )
        return False
    
    finally:
        try:
            if 'temp' in locals():
                temp.destroy()
            root.destroy()
        except:
            pass
