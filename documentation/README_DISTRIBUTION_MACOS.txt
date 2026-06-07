================================================================
  PALOMA'S ORRERY - macOS Distribution
  Version 2.2.0 | December 2025
================================================================

  Created by Tony Quintanilla for Paloma
  "Data Preservation is Climate Action"

================================================================
  DISTRIBUTION METHOD
================================================================

  Due to macOS security restrictions on unsigned applications,
  this software is distributed via USB flash drive or direct
  file transfer - NOT via internet download.

  Downloading from Google Drive, email, or web will trigger
  macOS security blocks that prevent the app from running.

================================================================
  CONTENTS
================================================================

  palomas_orrery        - Main solar system visualization
  star_visualization    - Stellar neighborhood viewer
  _internal/            - Required libraries and data
  README.txt            - This file

================================================================
  INSTALLATION
================================================================

  1. Copy the entire "Palomas_Orrery_macOS" folder from the
     flash drive to your Desktop or Applications folder

  2. Double-click "palomas_orrery" to launch the solar system

  3. Double-click "star_visualization" for the star viewer

  That's it! No additional setup required when copying from
  a flash drive.

================================================================
  IF YOU DOWNLOADED THIS (and it doesn't work)
================================================================

  Internet downloads add security flags that block the app.
  
  Try this in Terminal (Applications > Utilities > Terminal):

    cd ~/Desktop/Palomas_Orrery_macOS
    xattr -cr .
    ./palomas_orrery

  If that still fails with "library validation" errors,
  you'll need to get the app via flash drive instead.

================================================================
  APPLICATIONS
================================================================

  SOLAR SYSTEM ORRERY (palomas_orrery)
  ------------------------------------
  - 3D interactive planetary visualization
  - Real-time positions from NASA JPL Horizons
  - Planets, moons, asteroids, comets, spacecraft
  - Exoplanet systems with habitable zones
  - Climate data visualizations
  - Paleoclimate records (800,000 years)

  STAR VISUALIZATION (star_visualization)
  ---------------------------------------
  - 3D stellar neighborhood (up to 100 light-years)
  - Hertzsprung-Russell diagrams
  - 123,000+ stars from Hipparcos & Gaia catalogs
  - Search by name, distance, or magnitude

================================================================
  KNOWN LIMITATIONS
================================================================

  - Animation runs slowly (threading not optimized for macOS)
  - Must be distributed via flash drive, not internet download
  - Unsigned app - Apple's $99/year fee not paid

================================================================
  DATA SOURCES
================================================================

  - NASA JPL Horizons System (planetary ephemerides)
  - ESA Gaia Mission DR3 (stellar positions)
  - Hipparcos Catalog (bright stars)
  - NOAA/Scripps (CO2 data)
  - NASA GISS (temperature data)
  - NSIDC (sea ice data)

================================================================
  SYSTEM REQUIREMENTS
================================================================

  - macOS 10.15 (Catalina) or later
  - 500 MB disk space
  - Internet connection (for live data updates)
  - Recommended: 8 GB RAM for large star catalogs

================================================================
  CREDITS & CONTACT
================================================================

  Author: Tony Quintanilla
  Email: tonyquintanilla@gmail.com
  
  GitHub: https://github.com/TonyQuintanilla/palomas_orrery
  Instagram: @palomas_orrery
  
  Built with Python, Plotly, Astropy, and PyInstaller
  AI-assisted development with Claude, ChatGPT, Gemini

================================================================

  "The sky's the limit! Or the stars are the limit!"

================================================================
