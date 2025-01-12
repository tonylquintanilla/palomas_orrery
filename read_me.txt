# Stellar Data Pipeline Documentation
**Created**: December 13, 2024  
**Last Updated**: December 14, 2024

## Installation Instructions

### System Requirements
- Operating System: Windows 10/11, macOS 10.15+, or Linux
- Python 3.9 or higher
- Minimum 8GB RAM recommended
- Internet connection for data fetching
- Web browser for visualization display

### Python Installation

#### Windows:
1. Visit [python.org/downloads/windows](https://www.python.org/downloads/windows/)
2. Download the latest Python installer (e.g., Python 3.11.x)
3. Run the installer
4. **Important**: Check "Add Python to PATH" during installation
5. Choose "Customize installation"
6. Ensure "pip" and "tkinter" are selected
7. Complete the installation

#### macOS:
1. Visit [python.org/downloads/macos](https://www.python.org/downloads/macos/)
2. Download the latest Python installer
3. Open the downloaded .pkg file
4. Follow installation prompts
5. Verify installation by opening Terminal and typing:
   ```bash
   python3 --version
   pip3 --version
   ```

#### Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install python3 python3-pip python3-tk
```

### Required Python Libraries

Install all required libraries using pip:

#### Windows:
```bash
pip install numpy pandas plotly astropy astroquery requests tkinter pillow
```

#### macOS/Linux:
```bash
pip3 install numpy pandas plotly astropy astroquery requests pillow
```

Detailed library requirements:

1. **Data Processing Libraries**:
   - numpy>=1.21.0
   - pandas>=1.3.0
   - astropy>=5.0.0
   - astroquery>=0.4.6

2. **Visualization Libraries**:
   - plotly>=5.3.0
   - pillow>=9.0.0

3. **Interface Libraries**:
   - tkinter (usually included with Python)
   - requests>=2.26.0

### Module-Specific Requirements

#### data_acquisition.py:
- astroquery for Vizier access
- astropy for data handling
- requests for API calls

#### data_processing.py:
- numpy for numerical operations
- pandas for data manipulation
- astropy for coordinate transformations

#### star_properties.py:
- pickle for data caching
- astroquery for SIMBAD access

#### visualization_2d.py & visualization_3d.py:
- plotly for interactive visualizations
- numpy for calculations
- pandas for data management

#### hr_diagram_*.py:
- All above libraries
- tkinter for progress windows

#### planetarium_*.py:
- All above libraries
- tkinter for user interface

### Verification Steps

After installation, verify the setup:

1. Open Python terminal:
```python
import numpy
import pandas
import plotly
import astropy
import astroquery
import tkinter
from PIL import Image
```

2. Run test script:
```python
from ascii_pipeline import print_visualization_pipeline
print_visualization_pipeline()
```

### Troubleshooting

Common Issues:

1. **ModuleNotFoundError**:
   ```bash
   pip install [missing_module]
   # or
   pip3 install [missing_module]
   ```

2. **Tkinter Missing**:
   - Windows: Reinstall Python with tkinter selected
   - Linux: `sudo apt-get install python3-tk`
   - macOS: `brew install python-tk`

3. **Permission Errors**:
   - Windows: Run command prompt as administrator
   - Linux/macOS: Use `sudo` or create virtual environment

4. **SSL Certificate Errors**:
   - Update certificates: `pip install --upgrade certifi`
   - Check system time is correct

[Original documentation continues...]

## Overview
This document describes the data pipeline architecture for generating both 2D Hertzsprung-Russell diagrams and 3D spatial visualizations of nearby and visible stars. The pipeline supports two distinct modes of operation:
1. Apparent Magnitude Pipeline (stars visible to naked eye)
2. Distance Pipeline (stars within specified light-years)

## Master Data Files
The pipeline uses two master data files that are created once and reused:

1. `star_properties_apparent_magnitude.pkl`
   - Maximum magnitude limit: Vmag = 9.0
   - Contains:
     * Hipparcos stars with Vmag ≤ 4.0
     * Gaia stars with 4.0 < Vmag ≤ 9.0
   - Created once, filtered for subsequent queries

2. `star_properties_distance.pkl`
   - Maximum distance: 100 light-years
   - Contains:
     * Hipparcos stars within 100ly and Vmag ≤ 4.0
     * Gaia stars within 100ly and Vmag > 4.0
   - Created once, filtered for subsequent queries

## Pipeline Components

### 1. Data Acquisition (`data_acquisition.py`)
- Function: `initialize_vizier()`
  * Returns: Vizier instance with no row limit
  * Configuration: `columns=['*']` (fetch all columns)

- Function: `load_or_fetch_hipparcos_data(v, file, mag_limit=None, parallax_constraint=None)`
  * Primary source for bright stars
  * Fetches from Hipparcos catalog (I/239/hip_main)
  * Returns: Astropy Table or None

- Function: `load_or_fetch_gaia_data(v, file, mag_limit=None, parallax_constraint=None)`
  * Primary source for faint stars
  * Fetches from Gaia EDR3 catalog (I/350/gaiaedr3)
  * Returns: Astropy Table or None

### 2. Data Processing (`data_processing.py`)
- Function: `calculate_distances(data)`
  * Converts parallax to parsecs and light-years
  * Handles invalid/missing parallaxes

- Function: `select_stars_by_magnitude(hip_data, gaia_data, mag_limit)`
  * Implements selection logic:
    - Hipparcos: Vmag ≤ 4.0
    - Gaia: Vmag > 4.0
  * Returns: Combined dataset

- Function: `select_stars_by_distance(hip_data, gaia_data, max_light_years)`
  * Applies same magnitude-based selection
  * Additional distance filtering
  * Returns: Combined dataset

### 3. Star Properties (`star_properties.py`)
- Function: `load_existing_properties(properties_file)`
  * Checks for existing .pkl file
  * Creates new file if not exists

- Function: `query_simbad_for_star_properties(missing_ids, existing_properties)`
  * Fetches properties from SIMBAD
  * Includes: spectral type, magnitudes, object type

### 4. Status Reporting (New Module)
- Function: `report_pipeline_stage(stage, message)`
  * Standardized stage transitions
  * Progress tracking

- Function: `validate_star_counts(data)`
  * Verifies expected distributions
  * Reports anomalies

- Function: `generate_footer_text(mode, counts_dict)`
  * Creates visualization footer
  * Includes statistics and sources

## Pipeline Flow

### Apparent Magnitude Mode
1. Check for `star_properties_apparent_magnitude.pkl`
2. If not exists:
   - Fetch Hipparcos stars to Vmag 4.0
   - Fetch Gaia stars 4.0 < Vmag ≤ 9.0
   - Get SIMBAD properties
   - Save master file
3. If exists:
   - Load master file
   - Filter to user's magnitude limit
4. Calculate parameters
5. Create visualization

### Distance Mode
1. Check for `star_properties_distance.pkl`
2. If not exists:
   - Fetch Hipparcos stars within 100ly, Vmag ≤ 4.0
   - Fetch Gaia stars within 100ly, Vmag > 4.0
   - Get SIMBAD properties
   - Save master file
3. If exists:
   - Load master file
   - Filter to user's distance limit
4. Calculate parameters
5. Create visualization

## Status Reporting

### Pipeline Stages
```
[Data Acquisition] Starting Hipparcos fetch...
[Data Processing] Selecting stars...
[Properties] Querying SIMBAD...
[Parameters] Calculating stellar parameters...
[Visualization] Creating plot...
```

### Validation Messages
```
[Validation] Expected counts:
- Bright stars (Vmag ≤ 1.73): ~20
- Mid-range (1.73 < Vmag ≤ 4.0): ~500
- Faint stars (Vmag > 4.0): varies by limit
```

### Progress Tracking
```
[Progress] Hipparcos fetch: 100%
[Progress] SIMBAD queries: 45/100
[Progress] Parameter calculations complete
```

## Validation Checks
1. Star count verification at each stage
2. Data completeness checks
3. Parameter range validation
4. Output consistency validation

## Notes
- Keep .pkl files updated with source catalog versions
- Monitor for expected star count deviations
- Document any anomalies in counts or distributions
- Track processing time for each stage

## Project Development Summary

### Core Objectives
1. **Master File Strategy**
   - Build comprehensive master .pkl files once
   - Reuse for all subsequent runs
   - Support two distinct pipelines:
     * Apparent magnitude (max Vmag = 9.0)
     * Distance (max 100 light-years)

2. **Data Selection Logic**
   - Consistent across both pipelines:
     * Hipparcos: Vmag ≤ 4.0
     * Gaia: Vmag > 4.0
   - Apply selection once during master file creation
   - Filter from master files for user requests

3. **Data Completeness**
   - Fetch all columns from catalogs
   - Ensure no data loss in Gaia star counts
   - Maintain proper deduplication
   - Validate star counts against expected distributions

4. **Status Reporting**
   - Create dedicated status reporting module
   - Standardize output messages
   - Add progress tracking
   - Include validation checks
   - Generate consistent footer text

### Implementation Steps
1. **Flow Diagram Creation**
   - Show both pipeline architectures
   - Include module names
   - List function names
   - Specify key variables
   - Document data flow

2. **Documentation Updates**
   - Describe complete pipeline architecture
   - Detail both operational modes
   - Specify validation checks
   - Include expected outputs

3. **Code Refactoring**
   - Start with data acquisition
   - Implement master file handling
   - Add validation checks
   - Create status reporting module
   - Update visualization handoff

### Success Metrics
1. **Star Count Validation**
   - Match expected distributions
   - Proper Hipparcos/Gaia split
   - No unexplained data loss

2. **Performance**
   - Fast subsequent runs using master files
   - Efficient filtering
   - Proper memory management

3. **User Experience**
   - Clear progress indication
   - Informative status messages
   - Consistent footer text
   - Helpful error messages

### Next Steps
1. Create detailed flow diagram including:
   - Module structure
   - Function relationships
   - Variable flow
   - Decision points
   - Status reporting integration

2. Develop status reporting module:
   - Define message categories
   - Create standard formats
   - Implement progress tracking
   - Add validation checks

3. Update data acquisition:
   - Implement master file creation
   - Add validation
   - Update filtering logic

4. Test and validate:
   - Check star counts
   - Verify data completeness
   - Ensure proper filtering
   - Validate outputs

### Progress Tracking
- ⬜ Flow diagram creation
- ⬜ Status reporting module
- ⬜ Data acquisition updates
- ⬜ Pipeline validation
- ⬜ Documentation updates
- ⬜ Testing and verification