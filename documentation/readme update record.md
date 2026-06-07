Great feedback! Let me search for more context about your project structure and then provide improved installation instructions.

Perfect! Now I have the full context. Here's a comprehensively revised installation section that addresses all your issues:

```markdown
## Installation

### Prerequisites
- **Windows 10/11** (Mac/Linux also supported)
- **Python 3.11 to 3.13** (tested and verified compatible)
- **Git** (optional but recommended - see installation below)
- **300MB free disk space**
- **Internet connection**

### Detailed Installation Guide

#### Step 1: Install Git (Optional but Recommended)

If you don't have Git installed and want to use `git clone`:

1. Download Git from [git-scm.com](https://git-scm.com/downloads)
2. Run installer with default options
3. Verify installation: Open Command Prompt and type `git --version`

**Alternative:** Skip Git and download the project as a ZIP file (see Step 2b)

#### Step 2: Install Python

1. Download **Python 3.11 or 3.13** from [python.org](https://www.python.org/downloads/)
   - ⚠️ **Important:** Avoid the absolute latest Python version if it's brand new (wait 1-2 months for library compatibility)
   - **Recommended:** Python 3.13.x is currently well-tested with all dependencies
   
2. During installation:
   - ✅ **CHECK** "Add Python to PATH" (critical!)
   - ✅ **CHECK** "Install pip"
   - Click "Install Now"

3. **Verify installation:**
   - Open Command Prompt (type `cmd` in Windows search)
   - Type: `python --version`
   - Should show: `Python 3.13.x` (or 3.11.x)
   - Type: `pip --version`
   - Should show pip version info

#### Step 3: Download Paloma's Orrery

**Option A - Using Git (Recommended):**
```bash
# Navigate to where you want the project
cd C:\Users\YourName\Documents

# Clone the repository
git clone https://github.com/tonylquintanilla/palomas_orrery.git

# Enter the directory
cd palomas_orrery
```

**Option B - Download ZIP (No Git Required):**

1. Go to [https://github.com/tonylquintanilla/palomas_orrery](https://github.com/tonylquintanilla/palomas_orrery)
2. Click the green **"Code"** button
3. Click **"Download ZIP"**
4. **Extract the ZIP file:**
   - Right-click the downloaded file
   - Select "Extract All..."
   - Choose destination (e.g., `C:\Users\YourName\Documents\`)
   - Click "Extract"
5. Open Command Prompt and navigate to the extracted folder:
   ```bash
   cd C:\Users\YourName\Documents\palomas_orrery-main
   ```

#### Step 4: Download Cache Files

**Required for star visualization features to work immediately!**

1. Go to [GitHub Releases](https://github.com/tonylquintanilla/palomas_orrery/releases)
2. Find the latest release (v1.0.0 or higher)
3. Under **"Assets"**, download `palomas_orrery_cache_v1.0.0.zip` (120 MB)
4. **Extract to your project folder:**
   - Right-click `palomas_orrery_cache_v1.0.0.zip`
   - Select "Extract All..."
   - **Important:** Extract directly into your `palomas_orrery` folder (the cache files should be in the same directory as `palomas_orrery.py`)
   - Click "Extract"

#### Step 5: Install Python Dependencies

Open Command Prompt in your project folder and run:

**Option A - Use requirements.txt (Simplest):**
```bash
pip install -r requirements.txt
```

**Option B - Manual Installation (If requirements.txt fails):**

Copy and paste this entire block into Command Prompt:
```bash
pip install numpy>=1.24.0 pandas>=2.0.0 scipy>=1.11.0 astropy>=5.3.4 astroquery>=0.4.6 plotly>=5.18.0 kaleido==0.2.1 pillow>=10.0.0 matplotlib>=3.7.0 customtkinter>=5.2.0 requests>=2.31.0 beautifulsoup4>=4.12.0 python-dateutil>=2.8.2 pytz>=2023.3
```

**Common installation issues:**
- If you see "pip is not recognized": Python wasn't added to PATH. Reinstall Python with "Add to PATH" checked.
- If individual packages fail: Try installing them one at a time to identify the problem package.
- **Plotly/Kaleido compatibility**: The specific version `kaleido==0.2.1` is required for compatibility. Do not use `kaleido>=0.2.1`.

#### Step 6: Run Paloma's Orrery

**From Command Prompt (Recommended):**
```bash
# Make sure you're in the project directory
cd C:\Users\YourName\Documents\palomas_orrery

# Run the program
python palomas_orrery.py
```

**Important Notes:**
- ⚠️ **Don't double-click `palomas_orrery.py`** to run it - this may cause crashes
- ✅ **Always use** `python palomas_orrery.py` from Command Prompt
- The GUI window should appear within 5-10 seconds

### Troubleshooting

**"python is not recognized"**
- Python wasn't added to PATH during installation
- Solution: Reinstall Python and check "Add Python to PATH"

**"No module named X"**
- Missing dependency
- Solution: Run `pip install X` where X is the missing module name

**Plotly errors or visualization crashes**
- Incompatible Python/Plotly version
- Solution: Verify you're using Python 3.11-3.13, not a brand new version
- Reinstall plotly and kaleido: `pip uninstall plotly kaleido` then `pip install plotly>=5.18.0 kaleido==0.2.1`

**Program window doesn't appear**
- Check Command Prompt for error messages
- Verify all cache files extracted correctly
- Try: `python palomas_orrery.py` from the correct directory

**Cache files not found**
- Make sure cache files are extracted to the same folder as `palomas_orrery.py`
- Check for a nested folder structure (files should not be in `palomas_orrery_cache_v1.0.0\palomas_orrery_cache_v1.0.0\`)

### First Run

On first successful run:
- The GUI should appear immediately
- Star visualizations work right away (thanks to cache files!)
- Try plotting the solar system for today's date
- Explore star neighborhood visualizations

**No internet?** The program will use cached data for common objects. Internet is only needed when querying new celestial objects not in the cache.

### System Requirements Summary
- **OS:** Windows 10/11, macOS 10.14+, or Linux
- **Python:** 3.11 to 3.13 (tested thoroughly)
- **RAM:** 2GB minimum, 4GB recommended
- **Disk:** 300MB (includes cache files)
- **Internet:** Required for downloading and for querying new objects
```

**Key improvements:**
1. **Added Git installation section** with option to skip it
2. **Specified Python version range** (3.11-3.13) to avoid compatibility issues
3. **Detailed ZIP extraction instructions** since that was confusing
4. **Explicit cache file download and extraction** with clear location guidance
5. **Both requirements.txt AND manual installation** as fallbacks
6. **Added matplotlib** to the dependencies
7. **Emphasized using Command Prompt** over double-clicking
8. **Comprehensive troubleshooting section** for common issues
9. **Explained the kaleido version constraint** (==0.2.1, not >=)

Would you like me to also create a separate "Quick Start for Experienced Users" section that's more concise?