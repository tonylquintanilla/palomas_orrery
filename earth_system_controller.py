import tkinter as tk
from tkinter import filedialog, messagebox
import os
import subprocess
import platform

class MissionControlApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Paloma's Orrery: Earth System Controller")
        self.root.geometry("500x350")
        
        self.layer_files = []
        
        # Define default data path
        self.data_dir = os.path.join(os.getcwd(), 'data')

        # Header
        header = tk.Label(root, text="Earth System Visualization", font=("Helvetica", 16, "bold"))
        header.pack(pady=15)

        # Requirement note
        req_label = tk.Label(root, text="Requires: Google Earth Pro (free download)", 
                             font=("Helvetica", 9, "italic"), fg="gray")
        req_label.pack()

        # Listbox
        self.listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, width=60, height=8)
        self.listbox.pack(pady=5)

        # Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        self.btn_add = tk.Button(btn_frame, text="Add KML Layers", command=self.add_files, bg="#dddddd")
        self.btn_add.pack(side=tk.LEFT, padx=10)

        self.btn_clear = tk.Button(btn_frame, text="Clear List", command=self.clear_list, bg="#dddddd")
        self.btn_clear.pack(side=tk.LEFT, padx=10)

        self.btn_launch = tk.Button(root, text="LAUNCH SELECTED LAYERS", 
                                    command=self.launch_layers, 
                                    bg="#ffcccc", fg="darkred", font=("Helvetica", 12, "bold"))
        self.btn_launch.pack(pady=15, fill=tk.X, padx=50)

        self.status = tk.Label(root, text="Ready.", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status.pack(side=tk.BOTTOM, fill=tk.X)

    def add_files(self):
        filenames = filedialog.askopenfilenames(
            title="Select KML Layers",
            initialdir=self.data_dir, 
            filetypes=[("Google Earth Files", "*.kml *.kmz")]
        )
        for f in filenames:
            if f not in self.layer_files:
                self.layer_files.append(f)
                self.listbox.insert(tk.END, os.path.basename(f))
        
        self.status.config(text=f"{len(self.layer_files)} layers ready.")

    def clear_list(self):
        self.layer_files = []
        self.listbox.delete(0, tk.END)
        self.status.config(text="List cleared.")

    def launch_layers(self):
        selected_indices = self.listbox.curselection()
        if not selected_indices:
            files_to_launch = self.layer_files
        else:
            files_to_launch = [self.layer_files[i] for i in selected_indices]

        if not files_to_launch:
            messagebox.showwarning("No Layers", "Please add KML files first.")
            return

        self.status.config(text=f"Launching {len(files_to_launch)} layers...")
        for filepath in files_to_launch:
            self.open_file(filepath)

    def open_file(self, filepath):
        if platform.system() == 'Darwin':       
            subprocess.call(('open', filepath))
        elif platform.system() == 'Windows':    
            os.startfile(filepath)
        else:                                   
            subprocess.call(('xdg-open', filepath))

if __name__ == "__main__":
    root = tk.Tk()
    app = MissionControlApp(root)
    root.mainloop()
