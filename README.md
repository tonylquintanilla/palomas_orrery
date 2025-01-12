# Paloma's Orrery

An interactive solar system visualization tool with support for stellar neighborhood mapping.

## Features

- Real-time 3D visualization of celestial objects using NASA JPL Horizons data
- Interactive plots of planets, dwarf planets, moons, asteroids, and space missions
- Solar system animation capabilities (days, weeks, months, years)
- Detailed visualization of the Sun's structure from core to outer corona
- Stellar neighborhood mapping up to 100 light-years
- Hertzsprung-Russell diagrams for stellar classification
- Support for both distance-based and apparent magnitude-based star plotting

## Requirements

- Python 3.8+
- Required Python packages:
  - astropy
  - astroquery
  - numpy
  - pandas
  - plotly
  - tkinter
  - kaleido (for saving static images)

numpy>=1.24.0
pandas>=2.0.0
plotly>=5.18.0
astropy>=5.3.4
astroquery>=0.4.6
kaleido>=0.2.1
tk>=0.1.0
python-dateutil>=2.8.2
requests>=2.31.0
webbrowser>=0.0.1
matplotlib>=3.8.0
scipy>=1.11.3

requirements.txt includes all necessary packages for running Paloma's Orrery:

Core numerical and data processing libraries
Plotting and visualization tools
Astronomical data access
GUI components
Supporting utilities

Users can install these requirements using:
pip install -r requirements.txt

## Installation

1. Clone this repository:
```bash
git clone https://github.com/tonylquintanilla/palomas_orrery.git
cd palomas_orrery
```

2. Install required packages:
```bash
pip install astropy astroquery numpy pandas plotly kaleido
```

## Usage

1. Run the main program:
```bash
python palomas_orrery.py
```

2. Use the GUI to:
   - Select celestial objects to visualize
   - Choose dates and time intervals
   - Set visualization scale
   - Select animation modes
   - Generate stellar neighborhood maps

## Visualization Types

1. Solar System:
   - Interactive 3D plots
   - Accurate orbital trajectories
   - Mission paths
   - Solar structure visualization

2. Stellar Neighborhood:
   - Distance-based mapping (up to 100 light-years)
   - Apparent magnitude plots (-1.44 to 9.0)
   - Hertzsprung-Russell diagrams
   - Messier object visualization

## Data Sources

- Solar system positions: [JPL Horizons System](https://ssd.jpl.nasa.gov/horizons/)
- Star data: 
  - [Hipparcos Catalog](https://www.cosmos.esa.int/web/hipparcos)
  - [Gaia DR3](https://www.cosmos.esa.int/web/gaia)
- Object properties: [SIMBAD database](http://simbad.u-strasbg.fr/simbad/)

There are 4 data storage files created and used by the script. Some are very large, but they need to be created only once:

*.vot files:
1. hipparcos_data_magnitude.vot  (~ 193KB -- generated anew.)
2. gaia_data_magnitude.vot  (~292MB -- this file is very large and will take a very long time to generate. Watch your terminal output for progress in batches. I recommend running it over night and disable sleep mode! The script is fetching data from Gaia DR3.)
3. hipparcos_data_distance.vot  (~30KB -- generated anew.)
4. gaia_data_distance.vot  (~9.4MB)

*.pkl files:
1. star_properties_magnitude.pkl  (~12MB)
2. star_properties_distance.pkl  (~1MB)

These files store:
- .vot: Star catalog data from Hipparcos and Gaia missions
- .pkl: Cached star properties retrieved from SIMBAD database

The files are created when first running the program and reused in subsequent runs to avoid re-fetching data.

## About

Created by Tony Quintanilla with assistance from ChatGPT, Claude and Gemini AI assistants. Updated January 12, 2025.

## License

MIT License - See LICENSE file for details.