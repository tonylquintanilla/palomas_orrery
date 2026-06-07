# Paloma's Orrery - Download & Installation

Welcome! This page helps you download and run Paloma's Orrery, the Python program I use to create the earth science, solar system, and stellar visualizations on my [Instagram](https://www.instagram.com/palomas_orrery/).

Questions? Contact me at tonyquintanilla@gmail.com — Tony

---

## Choose Your Download

| Option | Best For | What You Get |
|--------|----------|--------------|
| **Windows Executable** | Windows users who don't want to install Python | Ready-to-run app (~469 MB) |
| **macOS Executable** | Mac users who don't want to install Python | Ready-to-run app (~300 MB) |
| **Python Source** | All platforms, or if you want to modify code | Python code + data files (~134 MB) |

---

## Option 1: Windows Executable (Easiest)

No Python installation required!

1. Go to [GitHub Releases](https://github.com/tonylquintanilla/palomas_orrery/releases)
2. Download `palomas_orrery.zip` (469 MB)
3. Extract the ZIP file
4. Double-click `START_HERE.bat`

That's it!

---

## Option 2: macOS Executable

No Python installation required!

1. Download from iCloud: [Link on my webpage](https://sites.google.com/view/tony-quintanilla)
2. Extract the ZIP file
3. Double-click `start_orrery.command`
4. First time: Right-click → Open → Open (to bypass Gatekeeper)

---

## Option 3: Python Source Code (All Platforms)

For Windows, macOS, or Linux users who have (or want to install) Python.

### Step 1: Download the Project

**Recommended:** Download from [GitHub Releases](https://github.com/tonylquintanilla/palomas_orrery/releases)
- Get `palomas_orrery_2_2_zip.zip` (~134 MB)
- This includes ALL code and data files

**Alternative:** [Google Drive](https://drive.google.com/drive/folders/1LjMsFH6mx7g21R_F1WVYJ-fZ6bc1LIAm?usp=sharing)
- Right-click `palomas_orrery_python` folder → Download
- Google will zip it automatically

Extract the ZIP to your Desktop or Documents folder.

### Step 2: Install Python

Skip this if you already have Python 3.11, 3.12, or 3.13.

1. Download from [python.org/downloads](https://www.python.org/downloads/)
2. Run the installer
3. **CRITICAL (Windows):** Check ✅ "Add Python to PATH"
4. Click "Install Now"

**Verify it worked:**
- Open Command Prompt (Windows) or Terminal (Mac/Linux)
- Type: `python --version` (Windows) or `python3 --version` (Mac/Linux)
- You should see: `Python 3.13.x` (or similar)

### Step 3: Install Required Libraries

**Windows:**
```
cd Desktop\palomas_orrery
pip install -r requirements.txt
```

**macOS:**
```
cd ~/Desktop/palomas_orrery
pip3 install -r requirements.txt
```

**Linux:** See [Linux Users](#linux-users) section below.

(Installation takes 2-5 minutes)

### Step 4: Run!

**Windows:**
- Double-click `START_HERE.bat`, OR
- In Command Prompt: `python palomas_orrery.py`

**macOS:**
- Double-click `start_orrery.command`, OR
- In Terminal: `python3 palomas_orrery.py`

**Linux:**
- Double-click `start_orrery.desktop` (right-click → "Allow Launching" first), OR
- In Terminal:
  ```bash
  cd ~/Desktop/palomas_orrery
  python3 palomas_orrery.py
  ```

---

## Staying Up to Date

The GitHub repository has the latest code between releases. To update:

**Easy way:** Double-click the update script in your folder:
- Windows: `UPDATE_CODE.bat`
- macOS: `update_code.sh` (run in Terminal)
- Linux: Run in Terminal:
  ```bash
  cd ~/Desktop/palomas_orrery
  ./update_code.sh
  ```

Your data files are preserved — only Python code gets updated.

**Note:** Git must be installed for updates to work.
- Windows: Download from [git-scm.com](https://git-scm.com/downloads)
- macOS: Install Xcode Command Line Tools: `xcode-select --install`
- Linux: `sudo apt install git`

---

## Linux Users

Tested on Linux Mint 22 (Ubuntu/Debian-based). Linux users will find the terminal workflow straightforward.

### Install System Dependencies

```bash
# Ubuntu/Debian/Mint
sudo apt install python3-pip python3-tk python3-pil.imagetk git

# Fedora
sudo dnf install python3-pip python3-tkinter python3-pillow-tk git

# Arch
sudo pacman -S python-pip tk python-pillow git
```

### Install Python Packages

```bash
cd ~/Desktop/palomas_orrery
pip install -r requirements.txt --break-system-packages
```

The `--break-system-packages` flag is required on Ubuntu 24.04+ and Debian 12+ due to PEP 668. This is safe for desktop applications.

### Run the Orrery

**Recommended (Terminal):**
```bash
cd ~/Desktop/palomas_orrery
python3 palomas_orrery.py
```

**Alternative (Desktop Launcher):**
1. Right-click `start_orrery.desktop`
2. Select "Allow Launching" (icon turns green, name changes)
3. Double-click to run — or drag to your dock/favorites

### Update Code from GitHub

**Use the terminal** (most reliable):
```bash
cd ~/Desktop/palomas_orrery
./update_code.sh
```

The `.desktop` updater file may not run on double-click in all desktop environments — terminal is the reliable method.

**Pull a single file** (if you know what changed):
```bash
git checkout origin/main -- palomas_orrery.py
```

### Additional Scripts

| Script | Purpose | How to Run |
|--------|---------|------------|
| `palomas_orrery.py` | Main orrery | `python3 palomas_orrery.py` |
| `star_visualization_gui.py` | Stellar neighborhood | `python3 star_visualization_gui.py` |
| `update_code.sh` | Pull latest from GitHub | `./update_code.sh` |

### Compress Screenshots

Linux screenshots can be large (2+ MB). To compress:
```bash
sudo apt install imagemagick
convert screenshot.png -quality 85 -resize 50% screenshot_small.jpg
```

---

## Troubleshooting

**"python is not recognized" (Windows)**
- Python wasn't added to PATH during install
- Uninstall Python, reinstall, and CHECK the "Add to PATH" box

**"ModuleNotFoundError"**
- Run `pip install -r requirements.txt` again (add `--break-system-packages` on Linux)

**"ImportError: cannot import name 'ImageTk'" (Linux)**
- Install: `sudo apt install python3-pil.imagetk`

**"externally-managed-environment" (Linux)**
- Add `--break-system-packages` flag to pip command

**"git: command not found"**
- Install git first (see Staying Up to Date section)

**Window doesn't appear**
- Check the Terminal for error messages

**Plots don't open**
- Make sure you have a default web browser set

---

## More Resources

- [GitHub Repository](https://github.com/tonylquintanilla/palomas_orrery) — Source code
- [Full README](https://github.com/tonylquintanilla/palomas_orrery/blob/main/README.md) — Complete documentation
- [Instagram @palomas_orrery](https://www.instagram.com/palomas_orrery/) — Visualizations
- [YouTube](https://www.youtube.com/@tony_quintanilla/featured) — Video tutorials

---

*Last updated: January 11, 2026*
