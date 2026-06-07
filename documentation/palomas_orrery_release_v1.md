# Paloma's Orrery v1.0.0

Interactive astronomical visualization tool for exploring the solar system and stellar neighborhood.

## Installation

### From Source 
Requires Python 3.11+ installed

1. Clone this repository

2. Install dependencies: `pip install -r requirements.txt`  

    Or install manually step-by-step:
    1. Core libraries: `pip install numpy pandas scipy`
    2. Astronomy libraries: `pip install astropy astroquery`
    3. Visualization: `pip install plotly pillow`
    4. Kaleido (specific version): `pip install kaleido==0.2.1`
    5. GUI library: `pip install customtkinter`
    6. Utilities: `pip install requests beautifulsoup4 python-dateutil pytz`

3. Download required cache files:

    **Download from this release:** `palomas_orrery_cache_v1.0.0.zip` (120 MB)
    
    Find it in the **Assets** section below. Click to download, then extract all files to your project folder.

    **These cache files are REQUIRED for the star visualization features to work.**

4. Run: `python palomas_orrery.py`

## Features
- Real-time planetary positions from JPL Horizons
- Interactive 3D orbital visualization  
- Stellar neighborhood exploration (100 light-years)
- Support for asteroids, comets, and spacecraft

## Release Assets

This release includes:
- **Source code** (automatically included via git tag)
- **palomas_orrery_cache_v1.0.0.zip** (120 MB) - Required cache files containing:
  - Gaia star catalogs (distance and magnitude)
  - Hipparcos star catalogs
  - Pre-processed star property files
  - JPL Horizons orbital cache (1365 objects)

## System Requirements
- Python 3.11+ 
- 2GB RAM minimum
- Windows/Mac/Linux
- Internet connection (for fetching new orbital data)

## Cache Files Explained

### Static Star Catalogs (Included):
The cache includes star catalogs that are difficult to regenerate:
- Gaia and Hipparcos stellar data
- Pre-processed star properties
- These files represent a working snapshot from 2024-2025

### Dynamic JPL Cache (Included & Expandable):
- Pre-cached orbital data for 1365 common objects
- Automatically grows as you query new objects
- Updates with fresh data for new date ranges

