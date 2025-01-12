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

## About

Created by Tony Quintanilla with assistance from ChatGPT, Claude and Gemini AI assistants. Updated January 12, 2025.

## License

MIT License - See LICENSE file for details.