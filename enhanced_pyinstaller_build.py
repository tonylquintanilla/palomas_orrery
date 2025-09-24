"""
Enhanced PyInstaller build script for Paloma's Orrery
Includes dependency verification, compression, and version numbering
"""

import os
import sys
import shutil
import subprocess
import zipfile
import json
from pathlib import Path
from datetime import datetime
import importlib.util

# ==================== CONFIGURATION ====================
VERSION = "1.0.0"  # Update this for new releases
BUILD_DATE = datetime.now().strftime("%Y%m%d")
INCLUDE_CACHE_FILES = True  # Always include cache files as requested
TEST_BUILD = False  # Set to True to build only main orrery first for testing

# ==================== FILE STRUCTURE INFO ====================
"""
FINAL DISTRIBUTION STRUCTURE:
palomas_orrery_dist/
├── palomas_orrery/           # Main orrery executable folder
│   ├── palomas_orrery.exe    # Main executable
│   ├── _internal/             # PyInstaller runtime files
│   │   ├── python*.dll        # Python runtime
│   │   ├── tcl/tk/           # Tkinter files
│   │   ├── customtkinter/     # CustomTkinter themes
│   │   ├── plotly/           # Plotly assets
│   │   ├── astropy/          # Astropy data files
│   │   └── [other libs]      # Other bundled libraries
│   ├── orbit_paths.json      # Orbital data cache
│   ├── satellite_ephemerides.json
│   ├── star_properties_distance.pkl  # Star cache (can be 50-200MB)
│   ├── star_properties_magnitude.pkl # Star cache (can be 100-500MB)
│   ├── hipparcos_data_*.vot  # Catalog files
│   ├── gaia_data_*.vot       # Catalog files
│   └── *_metadata.json       # Metadata files
│
├── star_visualization/        # Star viz executable folder
│   ├── star_visualization.exe
│   ├── _internal/            # Similar runtime files
│   └── [cache files]         # Same cache files as above
│
├── Launch_Orrery.bat         # Quick launcher for main program
├── Launch_Star_Visualization.bat  # Quick launcher for star viz
├── README.txt                # User instructions
└── VERSION.txt               # Version information
"""

def check_python_version():
    """Verify Python version is compatible"""
    version = sys.version_info
    print(f"Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ ERROR: Python 3.8+ is required")
        return False
    
    print("✓ Python version OK")
    return True

def verify_dependencies():
    """Verify all required dependencies are installed"""
    print("\n" + "="*60)
    print("Verifying Dependencies")
    print("="*60)
    
    # Core dependencies that must be installed
    required_packages = {
        # Core scientific
        'numpy': 'numpy',
        'pandas': 'pandas',
        'scipy': 'scipy',
        
        # Astronomy
        'astropy': 'astropy',
        'astroquery': 'astroquery',
        'erfa': 'erfa',
        
        # Visualization
        'plotly': 'plotly',
        'PIL': 'Pillow',
        'customtkinter': 'customtkinter',
        'kaleido': 'kaleido',  # For saving plots
        
        # Web and data
        'requests': 'requests',
        'bs4': 'beautifulsoup4',
        'html5lib': 'html5lib',
        'dateutil': 'python-dateutil',
        'pytz': 'pytz',
    }
    
    missing_packages = []
    installed_packages = []
    
    for import_name, package_name in required_packages.items():
        try:
            if import_name == 'PIL':
                # Special case for PIL/Pillow
                spec = importlib.util.find_spec('PIL')
            else:
                spec = importlib.util.find_spec(import_name)
            
            if spec is not None:
                installed_packages.append(package_name)
                print(f"✓ {package_name:20} - installed")
            else:
                missing_packages.append(package_name)
                print(f"❌ {package_name:20} - NOT FOUND")
        except ImportError:
            missing_packages.append(package_name)
            print(f"❌ {package_name:20} - NOT FOUND")
    
    # Check for custom modules
    print("\nChecking custom modules:")
    custom_modules = [
        'palomas_orrery_helpers',
        'idealized_orbits',
        'orbit_data_manager',
        'planet_visualization',
        'star_visualization_gui',
        'data_acquisition',
        'visualization_core',
        'star_properties',
    ]
    
    missing_modules = []
    for module in custom_modules[:8]:  # Just check first 8 as sample
        if os.path.exists(f'{module}.py'):
            print(f"✓ {module:30}.py found")
        else:
            missing_modules.append(module)
            print(f"❌ {module:30}.py NOT FOUND")
    
    # Report results
    print("\n" + "-"*60)
    if missing_packages:
        print(f"❌ Missing {len(missing_packages)} required packages:")
        print(f"   Install with: pip install {' '.join(missing_packages)}")
        return False
    elif missing_modules:
        print(f"❌ Missing {len(missing_modules)} custom modules")
        print("   Make sure you're in the correct project directory")
        return False
    else:
        print(f"✓ All {len(installed_packages)} required packages found")
        print(f"✓ All checked custom modules found")
        return True

def get_cache_files_info():
    """Get detailed information about cache files"""
    print("\n" + "="*60)
    print("Cache Files Analysis")
    print("="*60)
    
    cache_info = {
        'star_data': [],
        'catalog_data': [],
        'orbit_data': [],
        'metadata': [],
        'total_size': 0
    }
    
    # Categorize cache files
    cache_patterns = {
        'star_data': ['star_properties*.pkl'],
        'catalog_data': ['*.vot'],
        'orbit_data': ['orbit_paths.json', 'satellite_ephemerides.json'],
        'metadata': ['*_metadata.json', 'simbad_*.json', 'last_plot*.json'],
    }
    
    for category, patterns in cache_patterns.items():
        for pattern in patterns:
            import glob
            for file in glob.glob(pattern):
                if os.path.exists(file):
                    size_mb = os.path.getsize(file) / (1024 * 1024)
                    cache_info[category].append({
                        'file': file,
                        'size_mb': size_mb
                    })
                    cache_info['total_size'] += size_mb
    
    # Display categorized info
    categories_display = {
        'star_data': '🌟 Star Property Files (PKL)',
        'catalog_data': '📊 Catalog Files (VOT)',
        'orbit_data': '🪐 Orbit Data Files',
        'metadata': '📋 Metadata Files'
    }
    
    for category, display_name in categories_display.items():
        if cache_info[category]:
            print(f"\n{display_name}:")
            for file_info in cache_info[category]:
                print(f"  {file_info['file']:40} {file_info['size_mb']:8.2f} MB")
    
    print(f"\n{'Total cache size:':40} {cache_info['total_size']:8.2f} MB")
    
    if cache_info['total_size'] > 100:
        print(f"⚠️  Large cache detected. Build may take extra time.")
    
    return cache_info

def create_version_file(dist_folder):
    """Create version information file"""
    version_info = {
        'version': VERSION,
        'build_date': BUILD_DATE,
        'build_timestamp': datetime.now().isoformat(),
        'python_version': f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
        'platform': sys.platform,
    }
    
    # JSON version file
    with open(dist_folder / 'version.json', 'w') as f:
        json.dump(version_info, f, indent=2)
    
    # Human-readable version file
    version_text = f"""Paloma's Orrery
Version: {VERSION}
Build Date: {BUILD_DATE}
Build Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Python Version: {version_info['python_version']}
Platform: {sys.platform}

This build includes cached star catalogs and orbital data.
For updates, visit: https://github.com/tonylquintanilla/palomas_orrery
"""
    
    with open(dist_folder / 'VERSION.txt', 'w') as f:
        f.write(version_text)
    
    print(f"Created version files (v{VERSION})")

def create_spec_file_with_error_handling(program_name, entry_point, include_cache=True):
    """Create spec file with comprehensive error handling"""
    
    spec_content = f'''# -*- mode: python ; coding: utf-8 -*-
# Auto-generated spec file for {program_name}
# Version: {VERSION} - Build: {BUILD_DATE}

import sys
import os
from PyInstaller.utils.hooks import collect_all, collect_data_files, collect_submodules

# Initialize collections
datas = []
binaries = []
hiddenimports = []

# Error handling wrapper
def safe_collect(package_name):
    """Safely collect package data with error handling"""
    try:
        return collect_all(package_name)
    except Exception as e:
        print(f"Warning: Could not collect {{package_name}}: {{e}}")
        return [], [], []

# Collect critical packages with error handling
packages_to_collect = [
    'astropy',
    'astroquery', 
    'erfa',
    'plotly',
    'customtkinter',
]

for package in packages_to_collect:
    pkg_datas, pkg_binaries, pkg_hiddenimports = safe_collect(package)
    datas += pkg_datas
    binaries += pkg_binaries
    hiddenimports += pkg_hiddenimports

# Manually ensure critical data files
try:
    plotly_datas = collect_data_files('plotly')
    datas += plotly_datas
except:
    print("Warning: Could not collect plotly data files")

try:
    ct_datas = collect_data_files('customtkinter')
    datas += ct_datas
except:
    print("Warning: Could not collect customtkinter themes")
'''
    
    if include_cache:
        spec_content += '''
# Include cache files
print("Including cache files...")
cache_files = [
    ('orbit_paths.json', '.'),
    ('satellite_ephemerides.json', '.'),
    ('star_properties*.pkl', '.'),
    ('*.vot', '.'),
    ('*_metadata.json', '.'),
    ('simbad_*.json', '.'),
]

import glob
for pattern, dest in cache_files:
    for file in glob.glob(pattern):
        if os.path.exists(file):
            datas.append((file, dest))
            print(f"  Including: {file}")
'''
    
    # Add all hidden imports
    spec_content += '''
# Comprehensive hidden imports
hiddenimports += [
    # Standard library
    'tkinter', 'tkinter.ttk', 'tkinter.scrolledtext', 'tkinter.messagebox',
    'threading', 'json', 'pickle', 'webbrowser', 'os', 'sys', 'time',
    'datetime', 'calendar', 'math', 'warnings', 'traceback', 'subprocess',
    'shutil', 'copy', 're', 'glob', 'pathlib',
    
    # Scientific packages
    'numpy', 'numpy.core', 'numpy.core._multiarray_umath',
    'pandas', 'pandas._libs', 
    'scipy', 'scipy.special', 'scipy.spatial',
    
    # Astronomy
    'astropy', 'astropy.units', 'astropy.time', 'astropy.coordinates',
    'astroquery', 'astroquery.jplhorizons',
    'erfa',
    
    # Visualization
    'plotly', 'plotly.graph_objs', 'plotly.subplots', 'plotly.io',
    'PIL', 'PIL.Image',
    'customtkinter',
    'kaleido',
    
    # Web/Data
    'requests', 'urllib', 'urllib.parse', 'urllib.request',
    'bs4', 'beautifulsoup4',
    'html5lib',
    'dateutil', 'pytz',
]

# Add all custom modules
import glob
for py_file in glob.glob('*.py'):
    module_name = py_file[:-3]
    if module_name != '__pycache__':
        hiddenimports.append(module_name)
'''
    
    # Complete spec file
    spec_content += f'''
a = Analysis(
    ['{entry_point}'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={{}},
    runtime_hooks=[],
    excludes=['matplotlib', 'qt5', 'PyQt5'],  # Exclude unneeded large packages
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='{program_name}',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,  # Keep console for error messages
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    version_file=None,
    icon='{program_name}_icon.ico' if os.path.exists('{program_name}_icon.ico') else None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='{program_name}',
)
'''
    
    spec_filename = f'{program_name}.spec'
    with open(spec_filename, 'w') as f:
        f.write(spec_content)
    
    print(f"Created {spec_filename}")
    return spec_filename

def build_single_executable(program_name, entry_point, spec_file):
    """Build a single executable with error handling"""
    print(f"\nBuilding {program_name}...")
    print("This may take several minutes...")
    
    try:
        # Run PyInstaller with detailed output
        result = subprocess.run(
            ["pyinstaller", spec_file, "--clean", "--noconfirm"],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print(f"✓ {program_name} built successfully")
            return True
        else:
            print(f"❌ Error building {program_name}")
            print("Error output:")
            print(result.stderr[-2000:])  # Last 2000 chars of error
            return False
            
    except Exception as e:
        print(f"❌ Exception while building: {e}")
        return False

def create_compressed_distribution(dist_folder):
    """Create a compressed ZIP file of the distribution"""
    print("\n" + "="*60)
    print("Creating Compressed Distribution")
    print("="*60)
    
    zip_name = f"palomas_orrery_v{VERSION}_{BUILD_DATE}.zip"
    
    print(f"Creating {zip_name}...")
    
    file_count = 0
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(dist_folder):
            # Skip unnecessary folders
            dirs[:] = [d for d in dirs if d not in ['__pycache__', '.git']]
            
            for file in files:
                file_path = Path(root) / file
                archive_name = file_path.relative_to(dist_folder.parent)
                zipf.write(file_path, archive_name)
                file_count += 1
                
                if file_count % 100 == 0:
                    print(f"  Compressed {file_count} files...")
    
    # Get ZIP file size
    zip_size_mb = os.path.getsize(zip_name) / (1024 * 1024)
    
    print(f"\n✓ Created {zip_name}")
    print(f"  Files: {file_count}")
    print(f"  Size: {zip_size_mb:.2f} MB")
    
    return zip_name

def create_launch_scripts(dist_folder):
    """Create batch files and README for the distribution"""
    
    # Main orrery launcher with error handling
    orrery_bat = f'''@echo off
title Paloma's Orrery v{VERSION}
echo ============================================
echo   Paloma's Orrery v{VERSION}
echo   Build: {BUILD_DATE}
echo ============================================
echo.
echo Starting main program...
cd palomas_orrery
if exist palomas_orrery.exe (
    start palomas_orrery.exe
) else (
    echo ERROR: palomas_orrery.exe not found!
    echo Please make sure all files were extracted properly.
    pause
)
'''
    
    with open(dist_folder / "Launch_Orrery.bat", 'w') as f:
        f.write(orrery_bat)
    
    # Star visualization launcher
    star_bat = f'''@echo off
title Star Visualization v{VERSION}
echo ============================================
echo   Star Visualization v{VERSION}
echo   Build: {BUILD_DATE}
echo ============================================
echo.
echo Starting star visualization...
cd star_visualization
if exist star_visualization.exe (
    start star_visualization.exe
) else (
    echo ERROR: star_visualization.exe not found!
    echo Please make sure all files were extracted properly.
    pause
)
'''
    
    with open(dist_folder / "Launch_Star_Visualization.bat", 'w') as f:
        f.write(star_bat)
    
    # Create comprehensive README
    readme_content = f'''Paloma's Orrery - Version {VERSION}
========================================
Build Date: {BUILD_DATE}

QUICK START:
------------
1. Extract ALL files from the ZIP to a folder
2. Double-click "Launch_Orrery.bat" for the main program
3. Double-click "Launch_Star_Visualization.bat" for star visualization

FILE STRUCTURE:
---------------
palomas_orrery_dist/
├── palomas_orrery/          → Main orrery program files
│   ├── palomas_orrery.exe   → Main executable
│   ├── _internal/            → Runtime libraries (do not modify)
│   └── [cache files]         → Pre-built star and orbit data
│
├── star_visualization/       → Star visualization program
│   ├── star_visualization.exe
│   ├── _internal/            → Runtime libraries
│   └── [cache files]         → Shared cache files
│
├── Launch_Orrery.bat        → Click to run main program
├── Launch_Star_Visualization.bat → Click to run star viz
├── VERSION.txt              → Version information
└── README.txt               → This file

INCLUDED CACHE FILES:
---------------------
This distribution includes pre-built cache files containing:
• Star catalogs from Hipparcos and Gaia (thousands of stars)
• Pre-calculated star properties and classifications
• Orbital data for planets, moons, and spacecraft
• These files save 20-30 minutes of initial download time

SYSTEM REQUIREMENTS:
--------------------
• Windows 10 or 11 (64-bit)
• 500 MB free disk space
• Internet connection (for updates and additional data)
• Screen resolution: 1920x1080 or higher recommended

FIRST RUN NOTES:
----------------
• Windows Defender may scan the files - this is normal
• If you see "Windows protected your PC", click "More info" → "Run anyway"
• The programs may take 10-30 seconds to start initially
• All data is cached locally for faster subsequent runs

TROUBLESHOOTING:
----------------
If programs won't start:
1. Verify ALL files were extracted (not just the .exe)
2. Check the _internal/ folders are present
3. Try running as Administrator
4. Temporarily disable antivirus scanning
5. Make sure you have the Visual C++ Redistributables installed

If you see missing module errors:
• The _internal/ folder may be incomplete
• Re-extract all files from the original ZIP

For slow performance:
• First run builds indexes - subsequent runs are faster
• Close other memory-intensive programs
• Check available disk space (need ~100MB free)

FEATURES:
---------
Main Orrery:
• Real-time solar system visualization
• Accurate planetary positions from JPL Horizons
• Spacecraft trajectories
• Planetary interior models
• Educational orbital mechanics demonstrations

Star Visualization:
• HR diagrams (Hertzsprung-Russell)
• 3D star maps of local stellar neighborhood
• Filter by distance or apparent magnitude
• Hipparcos and Gaia catalog integration
• Notable star information and classifications

DATA SOURCES:
-------------
• JPL Horizons: Orbital ephemerides
• Gaia DR3: Stellar positions and properties
• Hipparcos: Bright star catalog
• SIMBAD: Stellar classifications

CONTACT & SUPPORT:
------------------
Developer: Tony Quintanilla
Email: tonyquintanilla@gmail.com
GitHub: https://github.com/tonylquintanilla/palomas_orrery
Website: https://sites.google.com/view/tony-quintanilla

LICENSE:
--------
MIT License - Free to use, modify, and distribute
See LICENSE file for full terms

ACKNOWLEDGMENTS:
----------------
Special thanks to NASA/JPL, ESA Gaia mission, and the
astronomical community for providing open data access.

========================================
Thank you for using Paloma's Orrery!
'''
    
    with open(dist_folder / "README.txt", 'w') as f:
        f.write(readme_content)
    
    print("Created launch scripts and documentation")

def main():
    """Main build process with enhanced error handling"""
    print("\n" + "="*60)
    print(f"  Paloma's Orrery Build System v{VERSION}")
    print("="*60)
    
    # Step 1: Check Python version
    if not check_python_version():
        print("\n❌ Build aborted: Python version incompatible")
        return False
    
    # Step 2: Verify dependencies
    if not verify_dependencies():
        print("\n⚠️  Warning: Missing dependencies detected")
        response = input("\nContinue anyway? (y/n): ").lower()
        if response != 'y':
            print("Build aborted")
            return False
    
    # Step 3: Install PyInstaller
    try:
        import PyInstaller
        print(f"\n✓ PyInstaller {PyInstaller.__version__} is installed")
    except ImportError:
        print("\nInstalling PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
    
    # Step 4: Analyze cache files
    cache_info = get_cache_files_info()
    
    if cache_info['total_size'] == 0:
        print("\n⚠️  No cache files found!")
        print("The executable will need to download data on first run.")
        response = input("\nContinue without cache files? (y/n): ").lower()
        if response != 'y':
            print("Build aborted")
            return False
    
    # Step 5: Create spec files
    print("\n" + "="*60)
    print("Creating Build Specifications")
    print("="*60)
    
    specs_created = []
    
    # Main orrery spec
    spec1 = create_spec_file_with_error_handling(
        'palomas_orrery',
        'palomas_orrery.py',
        include_cache=INCLUDE_CACHE_FILES
    )
    specs_created.append(('palomas_orrery', 'palomas_orrery.py', spec1))
    
    # Star visualization spec (unless test mode)
    if not TEST_BUILD:
        spec2 = create_spec_file_with_error_handling(
            'star_visualization',
            'star_visualization_gui.py',
            include_cache=INCLUDE_CACHE_FILES
        )
        specs_created.append(('star_visualization', 'star_visualization_gui.py', spec2))
    
    # Step 6: Build executables
    print("\n" + "="*60)
    print("Building Executables")
    print("="*60)
    
    build_success = True
    for program_name, entry_point, spec_file in specs_created:
        if not build_single_executable(program_name, entry_point, spec_file):
            build_success = False
            if TEST_BUILD:
                print(f"\n❌ Test build of {program_name} failed")
                return False
    
    if not build_success:
        print("\n❌ Build failed. Check errors above.")
        return False
    
    # Step 7: Create distribution folder
    print("\n" + "="*60)
    print("Creating Distribution Package")
    print("="*60)
    
    dist_folder = Path(f"palomas_orrery_dist_v{VERSION}")
    if dist_folder.exists():
        shutil.rmtree(dist_folder)
    dist_folder.mkdir()
    
    # Copy built files
    for program_name, _, _ in specs_created:
        source = Path("dist") / program_name
        if source.exists():
            dest = dist_folder / program_name
            shutil.copytree(source, dest)
            print(f"✓ Copied {program_name} to distribution")
    
    # Step 8: Create version files and scripts
    create_version_file(dist_folder)
    create_launch_scripts(dist_folder)
    
    # Step 9: Create compressed distribution
    zip_file = create_compressed_distribution(dist_folder)
    
    # Step 10: Final summary
    print("\n" + "="*60)
    print("  BUILD COMPLETE!")
    print("="*60)
    print(f"\n📦 Distribution folder: {dist_folder.absolute()}")
    print(f"🗜️  Compressed package: {zip_file}")
    print(f"📌 Version: {VERSION} (Build {BUILD_DATE})")
    
    if cache_info['total_size'] > 0:
        print(f"💾 Included {cache_info['total_size']:.1f} MB of cache data")
    
    print("\n📋 Next steps:")
    print("1. Test the executables in the distribution folder")
    print("2. Share the ZIP file with users")
    print("3. Users should extract ALL files before running")
    
    if TEST_BUILD:
        print("\n⚠️  This was a TEST BUILD (only main orrery)")
        print("Run with TEST_BUILD=False for complete build")
    
    return True

if __name__ == "__main__":
    # Check we're in the right directory
    if not os.path.exists("palomas_orrery.py"):
        print("❌ Error: palomas_orrery.py not found!")
        print("Please run this script from your project directory.")
        sys.exit(1)
    
    # Run the build
    success = main()
    
    if success:
        print("\n✅ Build completed successfully!")
    else:
        print("\n❌ Build failed. Please check the errors above.")
        sys.exit(1)
