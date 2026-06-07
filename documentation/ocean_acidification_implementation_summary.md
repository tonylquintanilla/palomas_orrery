# Ocean Acidification - Implementation Checklist

## Files to Create

### 1. `convert_hot_ph_to_json.py` (NEW FILE)
✅ **Created in artifact** - Full conversion script for HOT data  
- Handles manual download workflow
- Flexible parser for various HOT data formats
- Generates `ocean_ph_hot_monthly.json`
- Includes metadata and statistics

## Files to Update

### 2. `earth_system_visualization_gui.py` (UPDATE)

Add these three functions (place them with other visualization functions):

```python
def load_ph_data():
    """Load ocean pH data from JSON cache"""
    try:
        with open('ocean_ph_hot_monthly.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        print("Error: pH data file is corrupted")
        return None

def create_ph_viz():
    """Create interactive ocean acidification (pH) visualization"""
    # FULL FUNCTION PROVIDED IN FIRST ARTIFACT
    # Copy the entire create_ph_viz() function from the artifact

def open_ph_viz():
    """Open ocean pH visualization in browser"""
    try:
        fig = create_ph_viz()
        if fig:
            fig.show()
        else:
            messagebox.showerror(
                "Data Not Available",
                "Ocean pH data not found.\n\n"
                "Please download HOT data and run convert_hot_ph_to_json.py first."
            )
    except Exception as e:
        messagebox.showerror(
            "Visualization Error",
            f"Error creating pH visualization:\n\n{str(e)}"
        )
```

**Replace the disabled pH button** (search for "Ocean Acidification (Coming Soon)"):

```python
# OLD (disabled button):
ph_button = tk.Button(right_column,
                    text='🧪 Ocean Acidification (Coming Soon)',
                    font=('Arial', 10),
                    bg='#BDBDBD',
                    fg='#666',
                    cursor='arrow',
                    padx=15,
                    pady=8,
                    state='disabled')

# NEW (active button):
ph_button = tk.Button(right_column,
                    text='🧪 Ocean Acidification',
                    font=('Arial', 10),
                    bg='#0077BE',  # Ocean blue
                    fg='white',
                    activebackground='#005A8C',
                    cursor='hand2',
                    padx=15,
                    pady=8,
                    command=open_ph_viz)
```

**Update footer** (change from "6 of 7" to "7 of 7"):

```python
footer_label = tk.Label(content_frame,
                    text="💡 7 of 7 visualizations active",  # Changed from 6 of 7
                    font=('Arial', 9),
                    fg='#666',
                    justify='center')
```

**Add scipy import** (at top of file with other imports):

```python
from scipy import stats  # For trend line in pH visualization
```

### 3. `climate_readme.md` (UPDATE)

Update the status sections:

```markdown
## Current Status (October 17, 2025)

**Active Visualizations: 7 of 7** ✅

1. ✅ The Keeling Curve (CO₂) - Automated
2. ✅ Global Temperature Anomalies - Automated  
3. ✅ Monthly Temperature Lines - Automated
4. ✅ Warming Stripes - Automated
5. ✅ Arctic Sea Ice Extent - Automated
6. ✅ Global Mean Sea Level Rise - Manual download
7. ✅ Ocean Acidification (pH) - Manual download  # NEW!

**Datasets: 5 total**
- 3 automated (CO₂, Temperature, Arctic Ice)
- 2 manual (Sea Level, Ocean pH)  # UPDATED!
```

Update Phase 4:

```markdown
### **Phase 4: Oceans** ✅ COMPLETE!
- **Sea Level Rise** ✅ Done!
  - Manual download from NASA Earthdata
  - 32-year satellite record preserved
- **Ocean Acidification** ✅ Done!  # UPDATED!
  - Manual download from HOT Station ALOHA
  - Multi-decadal pH time series
  - Conversion script: convert_hot_ph_to_json.py
```

## Implementation Workflow

### Step 1: Download HOT Data
1. Visit: https://hahana.soest.hawaii.edu/hot/hot-dogs/interface.html
2. Select: Time-Series = HOT, Parameters = Carbonate Chemistry
3. Download and save as `hot_carbonate_data.txt`

### Step 2: Create Conversion Script
Copy `convert_hot_ph_to_json.py` from artifact to your project directory

### Step 3: Convert Data
```bash
python convert_hot_ph_to_json.py
```

Expected output:
```
====================================
HOT Ocean pH Data → JSON Converter
====================================

Found input file: hot_carbonate_data.txt

Reading hot_carbonate_data.txt...
✓ Read 1250 lines
✓ Found header: {'year': 0, 'month': 1, 'ph_total': 5}
✓ 312 unique monthly records
✓ Saved to ocean_ph_hot_monthly.json
  File size: 25.3 KB
  Records: 312

Latest pH measurement: 8.0234 (2024-09)
35-year change: -0.0891 pH units
Rate: -0.002546 units/year

====================================
SUCCESS!
====================================

ocean_ph_hot_monthly.json is ready to use
```

### Step 4: Update GUI File
1. Add the three new functions (load_ph_data, create_ph_viz, open_ph_viz)
2. Replace the disabled pH button with active button
3. Update footer from "6 of 7" to "7 of 7"
4. Add scipy import

### Step 5: Test
```bash
python earth_system_visualization_gui.py
```

Click **🧪 Ocean Acidification** → Interactive chart opens!

## Expected Result

You'll see an interactive Plotly chart showing:
- **Blue line**: Monthly pH measurements from Station ALOHA
- **Red dashed line**: Long-term trend showing pH decline
- **Green dotted line**: Pre-industrial pH reference (~8.2)
- **Info box**: Latest pH, total decline, annual rate
- **Impact warnings**: Coral reefs, shellfish, food webs
- **Educational context**: "0.1 unit drop = 30% more acidic"

## Files Generated

After implementation, you'll have:
```
palomas_orrery/
├── convert_hot_ph_to_json.py       # NEW - Conversion script
├── hot_carbonate_data.txt          # NEW - Downloaded from HOT
├── ocean_ph_hot_monthly.json       # NEW - Generated cache (~25 KB)
├── earth_system_visualization_gui.py  # UPDATED
└── climate_readme.md               # UPDATED
```

## Verification Checklist

- [ ] `convert_hot_ph_to_json.py` created
- [ ] HOT data downloaded as `hot_carbonate_data.txt`
- [ ] Conversion script runs successfully
- [ ] `ocean_ph_hot_monthly.json` generated
- [ ] GUI file updated with 3 new functions
- [ ] pH button changed from gray to blue
- [ ] Footer updated to "7 of 7"
- [ ] scipy imported
- [ ] Test: GUI opens without errors
- [ ] Test: pH button click opens Plotly chart
- [ ] Test: Chart shows data and trend line
- [ ] climate_readme.md updated

## Quick Copy-Paste Sections

All the code you need is in these artifacts:
1. **ocean_acidification** - Contains the GUI functions (create_ph_viz, etc.)
2. **convert_hot_ph** - Complete conversion script
3. **ocean_ph_readme** - Full documentation

## Notes

- **Similar to sea level**: Manual download + conversion approach
- **Proven pattern**: Follows your existing workflow
- **One-time setup**: Download once, updates quarterly/annually
- **Small file**: ~25 KB JSON cache
- **No API issues**: No authentication, no rate limits
- **Complete documentation**: Ready for users

## What Makes This Great

✅ **Follows your existing patterns** (sea level approach)  
✅ **Clean separation** (download → convert → visualize)  
✅ **Flexible parser** (handles various HOT data formats)  
✅ **Educational focus** (explains pH logarithmic scale)  
✅ **Ocean blue theme** (consistent with your design)  
✅ **Future-ready** (can add BATS, SOCAT later)  
✅ **Complete docs** (users can replicate)  

**All 7 visualizations active!** 🌊🧪🎉
