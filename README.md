# Paloma's Orrery

An interactive solar system visualization tool with support for stellar neighborhood mapping and Hertzsprung-Russell diagrams.

## Summary

A comprehensive Python application that visualizes the solar system using data from the JPL Horizons system, combined with stellar visualization capabilities using Hipparcos and Gaia data. The tool allows users to:

1. Visualize and animate solar system objects:
   - Planets, dwarf planets, and their major moons
   - Asteroids and comets
   - Space missions and their trajectories
   - Sun's structure from core to heliopause

2. Create stellar visualizations:
   - 3D maps of the stellar neighborhood
   - Distance-based visualizations up to 100 light-years
   - Magnitude-limited views of visible stars
   - Hertzsprung-Russell diagrams
   - Messier object visualizations

## Features

- Real-time 3D visualization of celestial objects using NASA JPL Horizons data
- Interactive plots with customizable views and scales
- Solar system animation capabilities (hours/days/weeks/months/years)
- Detailed visualization of the Sun's structure from core to Oort Cloud
- Stellar neighborhood mapping up to 100 light-years
- Hertzsprung-Russell diagrams for stellar classification
- Support for both distance-based and apparent magnitude-based star plotting
- Integration of Messier objects (nebulae and star clusters)
- Interactive camera controls and notable star navigation
- Click-to-copy star names and detailed hover information
- Comprehensive data caching system for improved performance

## Requirements

### Python Version
- Python 3.8 or higher

### Required Libraries
```
numpy>=1.24.0
pandas>=2.0.0
plotly>=5.18.0
astropy>=5.3.4
astroquery>=0.4.6
kaleido>=0.2.1  # Required for saving static images
tk>=0.1.0
python-dateutil>=2.8.2
requests>=2.31.0
ipython>=8.12.0
scipy>=1.11.0
```

### Installation

1. Clone this repository:
```bash
git clone https://github.com/tonylquintanilla/palomas_orrery.git
cd palomas_orrery
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the main program:
```bash
python palomas_orrery.py
```

2. Using the Interface:
   - Select celestial objects from the scrollable menu
   - Choose a center object (default: Sun)
   - Set the date and time for visualization
   - Select scale options (Auto or Manual)
   - Generate different types of visualizations:
     * Solar System 3D plots
     * Stellar neighborhood 3D plots (distance or magnitude based)
     * Hertzsprung-Russell diagrams (2D)

## Implementation Details

### Photometric Systems and Magnitude Handling

The program handles data from two major catalogs with different photometric systems:

1. **Hipparcos Catalog**:
   - Uses the Johnson-Cousins photometric system
   - Directly provides standard V magnitudes (Vmag)
   - Provides B magnitudes for B-V color index calculation
   - Traditional system used in most historical astronomical observations

2. **Gaia Catalog**:
   - Uses its own three-band photometric system:
     * G (broad band covering most visible light)
     * BP (Blue Photometer)
     * RP (Red Photometer)
   - V magnitudes must be estimated using the transformation:
     ```python
     V = G - (-0.0257 - 0.0924*(BP-RP) - 0.1623*(BP-RP)**2 + 0.0090*(BP-RP)**3)
     ```
   - Estimation is accurate to within a few hundredths of a magnitude for most stars

### Catalog Separation Logic

1. **Magnitude-based Selection (Default)**:
   - Hipparcos catalog: Used exclusively for stars with Vmag ≤ 4.0
   - Gaia catalog: Used exclusively for stars with Vmag > 4.0
   - This prevents duplicate stars and ensures optimal data quality

2. **Distance-based Selection**:
   - Follows the same separation logic as magnitude-based selection
   - Hipparcos for bright stars (Vmag ≤ 4.0)
   - Gaia for fainter stars (Vmag > 4.0)
   - Selection based on parallax measurements

### Data Processing Pipeline

1. **Data Acquisition**:
   - Hipparcos data fetched first with appropriate magnitude/distance constraints
   - Gaia data fetched with complementary constraints
   - Data cached in VOTable format for future use

2. **Catalog Processing**:
   - Hipparcos stars:
     * Bright stars (Vmag ≤ 1.73)
     * Mid-range stars (1.73 < Vmag ≤ 4.0)
   - Gaia stars:
     * Faint stars (Vmag > 4.0)

3. **Star Properties**:
   - Properties fetched from SIMBAD database
   - Cached in PKL format
   - Includes:
     * Spectral types
     * B-V colors
     * Object classifications
     * Additional notes for notable stars

### Technical Notes

1. **Magnitude Conversion**:
   ```python
   # Gaia G magnitude to Johnson V magnitude conversion
   V = G - (-0.0257 - 0.0924*(BP-RP) - 0.1623*(BP-RP)**2 + 0.0090*(BP-RP)**3)
   ```

2. **Magnitude Standardization**:
   - All magnitudes standardized to `Apparent_Magnitude` column
   - Used consistently across all visualization modes
   - Facilitates proper star selection and display

3. **Temperature Estimation**:
   - Primary: B-V color index when available
   - Secondary: Spectral type
   - Uses interpolation for missing data
   - Required for both HR diagrams and 3D visualizations

4. **Distance Calculations**:
   - Parallax to distance conversion
   - Error handling for uncertain measurements
   - Light-year conversion factor: 3.26156

## Data Files

The program creates and uses several data cache files:

### VOTable Files (.vot)
1. `hipparcos_data_magnitude.vot` (~193KB)
2. `gaia_data_magnitude.vot` 
   - ~1.2MB for magnitude 4 (default)
   - Up to ~292MB for magnitude 9
3. `hipparcos_data_distance.vot` (~30KB)
4. `gaia_data_distance.vot` (~9.4MB)

### Property Cache Files (.pkl)
1. `star_properties_magnitude.pkl` (~12MB)
2. `star_properties_distance.pkl` (~1MB)

Note: Files are created on first run and reused in subsequent sessions.

## Performance Notes

1. **Initial Load**:
   - First run: 2-5 minutes for data fetching
   - Subsequent runs: 5-10 seconds from cache
   - Cache updates: Weekly recommended

2. **Memory Usage**:
   - Magnitude limit 4: ~100MB
   - Magnitude limit 6: ~500MB
   - Magnitude limit 9: ~2GB

3. **Visualization Response**:
   - Interactive updates: <100ms
   - Animation frames: 200-500ms
   - Plot generation: 2-5 seconds

## Troubleshooting

1. **Missing Star Data**:
   - Check cache files are not corrupted
   - Verify SIMBAD connection
   - Confirm magnitude/distance limits

2. **Visualization Issues**:
   - Clear browser cache
   - Check plotly.js loading
   - Verify screen resolution settings

3. **Performance Problems**:
   - Reduce number of selected objects
   - Lower animation frame count
   - Use manual scaling for large distances

## Contributing

1. **Code Style**:
   - Follow PEP 8
   - Use type hints
   - Document complex algorithms

2. **Testing**:
   - Unit tests for core functions
   - Integration tests for data pipeline
   - Performance benchmarks

3. **Documentation**:
   - Update README for new features
   - Document API changes
   - Maintain version history

## Data Sources

- Solar system positions: [JPL Horizons System](https://ssd.jpl.nasa.gov/horizons/)
- Stellar data:
  * [Hipparcos Catalog](https://www.cosmos.esa.int/web/hipparcos)
  * [Gaia DR3](https://www.cosmos.esa.int/web/gaia)
- Object properties: [SIMBAD database](http://simbad.u-strasbg.fr/simbad/)
- Messier objects: [SEDS Messier Database](http://www.messier.seds.org/)

## License

This project is licensed under the MIT License with Non-Commercial Use Restriction.

### Key Points:
1. **Free for Non-Commercial Use**
   - Academic research
   - Personal projects
   - Educational purposes
   - Non-profit organizations

2. **Commercial Use Requires Permission**
   - Contact author for commercial licensing
   - Written permission required
   - Separate terms may apply

3. **Attribution Requirements**
   - Must credit original author
   - Must indicate modifications
   - Must include license notice

4. **Data Source Attributions Required**
   - NASA/JPL-Caltech for Horizons data
   - ESA for Hipparcos data
   - ESA/Gaia/DPAC for Gaia data
   - CDS, Strasbourg, France for SIMBAD data

### Third-Party Components:
This software incorporates several open-source libraries:
- NumPy (BSD 3-Clause)
- Pandas (BSD 3-Clause)
- Plotly (MIT)
- Astropy (BSD 3-Clause)
- Astroquery (BSD 3-Clause)

For commercial licensing inquiries, contact:
Tony Quintanilla (tonyquintanilla@gmail.com)

See LICENSE.txt for complete terms.

## About

Created by Tony Quintanilla with assistance from ChatGPT, Claude and Gemini AI assistants.
Updated February 17, 2025.