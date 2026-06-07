For this more complex all-planets version, I recommend a **combined approach** that balances functionality, reliability, and file size. Here's my recommended strategy:

## Step-by-Step Optimized Approach

### 1. First, Create an Optimized Version of Your Script### 2. Create a Minimal Virtual Environment

This is crucial for reducing file size:

```bash
# Create new virtual environment
python -m venv orrery_env_minimal

# Activate it
orrery_env_minimal\Scripts\activate

# Install ONLY essential packages
pip install numpy matplotlib astroquery pyinstaller

# Don't install any extras like jupyter, ipython, etc.
```

### 3. Build with Smart Exclusions

Use this optimized command:

```bash
pyinstaller --onefile --windowed ^
  --exclude-module pytest ^
  --exclude-module test ^
  --exclude-module tests ^
  --exclude-module IPython ^
  --exclude-module notebook ^
  --exclude-module scipy.spatial.transform._rotation_groups ^
  --exclude-module scipy.datasets ^
  --exclude-module pandas.tests ^
  --exclude-module matplotlib.tests ^
  --exclude-module numpy.tests ^
  --exclude-module astropy.tests ^
  --exclude-module astroquery.tests ^
  --exclude-module astropy.visualization ^
  --exclude-module astropy.cosmology ^
  --exclude-module astropy.modeling ^
  --exclude-module astropy.stats ^
  --exclude-module jinja2 ^
  --exclude-module sphinx ^
  --hidden-import astroquery.jplhorizons ^
  orrery-jpl-all_planets-optimized.py
```

### 4. (Optional) If You Have UPX Installed

Add compression:

```bash
pyinstaller --onefile --windowed ^
  --upx-dir=C:\path\to\upx ^
  --strip ^
  --exclude-module pytest ^
  --exclude-module test ^
  --exclude-module tests ^
  --exclude-module IPython ^
  --exclude-module notebook ^
  --exclude-module scipy.spatial.transform._rotation_groups ^
  --exclude-module scipy.datasets ^
  --exclude-module pandas.tests ^
  --exclude-module matplotlib.tests ^
  --exclude-module numpy.tests ^
  --exclude-module astropy.tests ^
  --exclude-module astroquery.tests ^
  --exclude-module astropy.visualization ^
  --exclude-module astropy.cosmology ^
  --exclude-module astropy.modeling ^
  --exclude-module astropy.stats ^
  --exclude-module jinja2 ^
  --exclude-module sphinx ^
  --hidden-import astroquery.jplhorizons ^
  orrery-jpl-all_planets-optimized.py
```

## Why This Approach?

1. **The optimized script** handles the CITATION file error proactively, preventing runtime crashes
2. **Minimal virtual environment** ensures you're not packaging unnecessary dependencies 
3. **Smart exclusions** remove test suites and unused astropy modules that can add 50+ MB
4. **UPX compression** can reduce size by another 30-40%

## Expected Results

With this approach, you should get:
- **Without UPX**: ~60-80 MB
- **With UPX**: ~40-60 MB
- **Full functionality** preserved including all planets, date advancement buttons, and Paloma's birthday feature

## Quick Alternative

If you want the absolute simplest approach that works (though slightly larger):

```bash
# In your minimal virtual environment
pyinstaller --onefile --windowed --hidden-import astroquery.jplhorizons orrery-jpl-all_planets-optimized.py
```

This will be larger (~80-100 MB) but should work reliably without any complex configuration.

## Recommendation

**Use the full approach with the optimized script and exclusions.** The extra setup time is worth it for:
- Smaller executable (half the size of `--collect-all`)
- Faster startup time
- Better distribution (smaller file to share)
- No runtime errors from missing CITATION file

The key is using the optimized script that handles the astroquery issues combined with smart PyInstaller exclusions to minimize bloat while keeping all functionality intact.