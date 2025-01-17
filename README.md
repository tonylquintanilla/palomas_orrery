# Paloma's Orrery

An interactive solar system visualization tool with support for stellar neighborhood mapping and Hertzsprung-Russell diagrams.

## Features

- Real-time 3D visualization of celestial objects using NASA JPL Horizons data
- Interactive plots of planets, dwarf planets, moons, asteroids, and space missions
- Solar system animation capabilities (days, weeks, months, years)
- Detailed visualization of the Sun's structure from core to heliopause and Oort Cloud
- Stellar neighborhood mapping up to 100 light-years
- Hertzsprung-Russell diagrams for stellar classification
- Support for both distance-based and apparent magnitude-based star plotting
- Visualization of Messier objects (nebulae and star clusters)
- Interactive camera controls and notable star navigation
- Toggle between detailed and simplified hover information

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

## Visualization Types

### 1. Solar System
- Interactive 3D plots with accurate orbital trajectories
- Detailed Sun visualization from core to outer corona
- Mission paths and comet trajectories
- Animated position tracking
- Scale options from planetary orbits to Oort Cloud

### 2. Stellar Neighborhood
- **Distance-based mapping:**
  * Up to 100 light-years from Sun
  * Shows actual stellar positions in 3D space
  * Combined data from Hipparcos and Gaia catalogs

- **Apparent magnitude plots:**
  * Range from -1.44 (Sirius) to 9.0 (space visibility limit)
  * Includes Messier objects
  * Shows both nearby and distant bright stars
  * Reveals galactic structure at higher magnitudes

### 3. Hertzsprung-Russell Diagrams
- Temperature vs Luminosity plots
- Stellar classification visualization
- Main sequence and evolved star populations
- Options for both distance and magnitude-limited samples

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

## Data Sources

- Solar system positions: [JPL Horizons System](https://ssd.jpl.nasa.gov/horizons/)
- Stellar data:
  * [Hipparcos Catalog](https://www.cosmos.esa.int/web/hipparcos)
  * [Gaia DR3](https://www.cosmos.esa.int/web/gaia)
- Object properties: [SIMBAD database](http://simbad.u-strasbg.fr/simbad/)
- Messier objects: [SEDS Messier Database](http://www.messier.seds.org/)

## Performance Notes

- Initial data fetching may take several minutes, especially for higher magnitude limits
- Animation speed depends on number of objects selected
- Large-scale visualizations (e.g., Oort Cloud) may require manual scale adjustment
- Toggle between detailed and simple hover text can improve performance

## About

Created by Tony Quintanilla with assistance from ChatGPT, Claude and Gemini AI assistants.
Updated January 16, 2025.

## License

MIT License - See LICENSE file for details.