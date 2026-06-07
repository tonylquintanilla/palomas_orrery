# Implementation Steps - Earth System Visualization

## Files Created

1. ✅ **earth_system_visualization_gui.py** - The Keeling Curve visualization
2. ✅ **fetch_climate_data.py** - Data fetcher from NOAA
3. ✅ **palomas_orrery.py integration code** - Earth button with flair

## Step-by-Step Implementation

### Step 1: Add the Files
Copy these files to your project root directory (same level as `palomas_orrery.py`):
- `earth_system_visualization_gui.py`
- `fetch_climate_data.py`

### Step 2: First Data Fetch
```bash
cd /path/to/palomas_orrery
python fetch_climate_data.py
```

**Expected output:**
```
===========================================================
  Climate Data Fetcher - Paloma's Orrery
  Data Preservation is Climate Action
===========================================================

Fetching Mauna Loa CO₂ monthly data...

Fetching data from NOAA...
URL: https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.txt
✓ Download successful
Parsing data...
✓ Parsed 807 records
Saving to co2_mauna_loa_monthly.json...
✓ Saved successfully
  File size: 52.3 KB
  Records: 807
  Date range: 1958-03 to 2025-09

===========================================================
SUCCESS
===========================================================

Latest CO₂ measurement: 424.61 ppm
Date: 2025-09

67-year increase: +108.90 ppm
(1958-2025)

⚠️  WARNING:
   Mauna Loa Observatory may close August 2025 due to budget cuts
```

**Verify:** Check that `co2_mauna_loa_monthly.json` now exists in your root directory (~50 KB).

### Step 3: Test the Visualization
```bash
python earth_system_visualization_gui.py
```

**Expected:** Browser opens showing the Keeling Curve with:
- Blue line (67 years of CO₂ data)
- Current value highlighted (red diamond)
- Pre-industrial baseline (green dashed line)
- High-risk threshold (red dashed line)
- Current CO₂ box (upper right)
- Hover text showing exact values

### Step 4: Integrate with Orrery (Choose One Approach)

#### **Option A: Earth URL Button with Flair** (Professional, Integrated)

**Pros:** 
- Earth button styled specially among URL buttons
- Same size, perfectly integrated
- Professional double-border look

**Cons:** 
- Requires modifying `add_url_buttons()` function

**Implementation:**
1. Add import at top of `palomas_orrery.py`:
   ```python
   try:
       import earth_system_visualization_gui
       EARTH_VIZ_AVAILABLE = True
   except ImportError:
       EARTH_VIZ_AVAILABLE = False
   ```

2. Use the `add_url_buttons_with_earth_flair()` function from the integration code

3. Update Earth's definition to include:
   ```python
   'url': 'earth_system_viz'
   ```

4. Add URL handler to detect and launch GUI

#### **Option B: Dedicated Button** (Simpler, Faster)

**Pros:**
- Quick to implement
- No modification of existing functions
- Clear and obvious

**Cons:**
- Separate from URL buttons
- Requires finding good spot in GUI

**Implementation:**
1. Add import (same as Option A)

2. Add button near Star Visualization button:
   ```python
   earth_viz_button = tk.Button(
       controls_frame,  # or wherever you want it
       text="🌍 Earth System Visualization",
       command=lambda: earth_system_visualization_gui.open_earth_system_gui() 
                      if EARTH_VIZ_AVAILABLE 
                      else messagebox.showwarning("Not Found", 
                          "earth_system_visualization_gui.py not found"),
       font=('Arial', 10, 'bold'),
       bg='#2E86AB',
       fg='white',
       relief=tk.RAISED,
       borderwidth=3,
       width=25
   )
   earth_viz_button.pack(pady=5)
   ```

### Step 5: Test Integration

1. Launch Paloma's Orrery:
   ```bash
   python palomas_orrery.py
   ```

2. Select Earth checkbox

3. Click "Plot Entered Date"

4. **Option A:** Look for Earth in the URL buttons - should have double border, blue color
   
   **Option B:** Look for the "🌍 Earth System Visualization" button

5. Click the button → Keeling Curve should open in browser

## Verification Checklist

- [ ] `fetch_climate_data.py` runs without errors
- [ ] `co2_mauna_loa_monthly.json` created (~50 KB)
- [ ] `earth_system_visualization_gui.py` opens visualization
- [ ] Keeling Curve shows 1958-2025 data
- [ ] Current CO₂ value displayed (should be ~424 ppm)
- [ ] Hover text works (shows date and CO₂ value)
- [ ] Integration with orrery works
- [ ] Earth button has special styling (Option A) or dedicated button visible (Option B)
- [ ] Clicking button opens visualization

## Troubleshooting

### "File not found" error
**Problem:** `co2_mauna_loa_monthly.json` doesn't exist
**Solution:** Run `python fetch_climate_data.py` first

### "Module not found" error  
**Problem:** Can't import `earth_system_visualization_gui`
**Solution:** Make sure file is in same directory as `palomas_orrery.py`

### Fetch fails
**Problem:** Can't download from NOAA
**Solutions:**
- Check internet connection
- Try again later (server may be temporarily down)
- Check if NOAA URL is accessible in browser

### Button doesn't appear
**Problem:** Earth button not showing in orrery
**Solutions:**
- Make sure Earth is selected (checkbox checked)
- Verify integration code was added correctly
- Check console for error messages

### Visualization is blank
**Problem:** Graph opens but no data
**Solution:** Verify JSON file has data (should be ~800 records)

## File Locations Summary

```
palomas_orrery/
├── palomas_orrery.py                    # MODIFIED (add import + button)
├── earth_system_visualization_gui.py    # NEW
├── fetch_climate_data.py                # NEW
├── co2_mauna_loa_monthly.json           # CREATED by fetch script
└── [all your existing files]
```

## Next Steps After Implementation

Once working:
1. ✅ Celebrate! You've preserved the Keeling Curve
2. Add daily CO₂ data (same pattern, different URL)
3. Add global mean CO₂
4. Add temperature data
5. Expand visualization GUI to show multiple datasets
6. Build toward full planetary boundaries framework

## Update Schedule

**First week:** Test and verify everything works  
**Weekly:** Run `fetch_climate_data.py` to get latest measurements  
**Monthly:** After initial testing, monthly updates sufficient

## The Vision

This is **Phase 1** of the Earth System Visualization:

- **Phase 1** (Now): Keeling Curve ✅
- **Phase 2**: More CO₂ datasets (daily, global)
- **Phase 3**: Temperature, sea level, ice extent
- **Phase 4**: Full planetary boundaries framework
- **Phase 5**: Interactive "what-if" scenarios

**One dataset at a time. One visualization at a time. One boundary at a time.**

Not a moment to lose. 🌍
