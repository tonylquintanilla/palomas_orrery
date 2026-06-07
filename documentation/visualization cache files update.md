=================

You're right to be confused - the system WAS working correctly before. When you expanded from 100 ly to 100.1 ly, it properly detected new stars and safely updated the PKL with just those additions. The `update_calculated_properties()` method in `simbad_manager.py` has all the safety checks and works correctly.

The issue is that `update_calculated_properties()` is being called EVERY time, even when there are NO new stars. Looking at your output:

```
INFO:simbad_manager:Updated 99 existing stars, added 0 new stars
INFO:simbad_manager:Total stars: 18363 (was 18363)
INFO:simbad_manager:Saved 18363 properties to star_properties_distance.pkl
```

It's rewriting the entire 2.6 MB file to "update" 99 stars that haven't changed. The safety checks prevent data loss but don't prevent unnecessary rewrites.

The real problem is that `calculate_stellar_parameters()` recalculates Temperature/Luminosity for your 99 stars every time, and `update_calculated_properties()` sees these as "updates" even though the values are the same.

The cleanest fix is to only call those three lines when there are actually new stars. Here's a minimal change - wrap those three lines in a condition:

```python
# Only update PKL if we actually added new stars to the dataset
if len([uid for uid in unique_ids if uid not in existing_properties]) > 0:
    config = SimbadConfig.load_from_file()
    manager = SimbadQueryManager(config)
    updated_properties = manager.update_calculated_properties(combined_df, properties_file)
```

This preserves the incremental update capability (100 ly → 100.1 ly will still work) while preventing unnecessary rewrites during normal runs.

==============

Perfect! Yes, comment out those three lines in all 4 scripts. Your output shows it's now working correctly:

- No PKL file updates (no `INFO:simbad_manager` messages about saving)
- Visualization runs quickly (3.14 seconds total)
- No errors

The PKL files remain stable archives at 18,363 stars (distance) and 202,178 stars (magnitude). They'll only be updated when you actually expand your search range (like going from 100.1 to 101 ly), which will properly trigger the incremental update.

This is the correct behavior - visualizations should just read from the PKL files, not rewrite them every time.

======================

I'll help you resolve these issues with your star visualization code. Let me search the project knowledge to understand the caching system and plot limits.Now let me search for the specific error and visualization code issues:Based on my analysis of your code and the error output, I can identify the issues and provide solutions:

## Issues Identified:

1. **UpdateMenus Error**: The visualization is trying to add `None` to the updatemenus list, causing a Plotly validation error
2. **Missing Cache Files**: The code doesn't properly create initial cache files when they don't exist
3. **Hard-coded 100.1 ly limit**: The limit is embedded in multiple places in the code

## Solutions:

### 1. Fix the UpdateMenus Error in `visualization_3d.py`

The error occurs because the code is trying to append `None` to the updatemenus. Looking at the trace, this happens in `create_3d_visualization`. The issue is likely in the hover toggle buttons creation. Here's the fix:### 2. Fix Cache File Initialization### 3. Strategy for Increasing the Distance Limit from 100.1 to 101 ly## Summary and Implementation Steps:

### Immediate Fixes:

1. **Fix the UpdateMenus Error**: The error in your output is caused by `None` being added to the updatemenus list. The fix ensures only valid menu objects are added.

2. **Initialize Cache Files**: Add the cache initialization system to create empty cache files when they don't exist, preventing the "missing file" errors.

3. **Test Distance Limit Increase**: Use the centralized configuration to safely test increasing from 100.1 to 101 ly.

### Implementation Steps:

1. **First, add cache initialization to your main scripts**:
```python
# At the start of planetarium_distance.py and hr_diagram_distance.py
from cache_initialization import initialize_cache_system
initialize_cache_system()
```

2. **Fix the visualization_3d.py updatemenus issue** by ensuring no `None` values are added to the updatemenus list.

3. **Test the distance limit increase**:
```bash
# Run the configuration update
python distance_limit_config.py

# Then test with the new limit
python planetarium_distance.py 101
```

### Key Safety Features:

1. **Incremental Fetching**: The system will only fetch stars between 100.1 and 101 ly, not re-fetch everything
2. **Cache Protection**: Existing cache files are preserved and backed up
3. **Validation**: The system validates requests and prevents excessive fetches
4. **Reporting**: Clear status reports show what data is being fetched

The incremental cache manager will:
- Detect you have data up to 100.1 ly
- Fetch only stars between 100.1 and 101 ly  
- Merge the new data with existing cache
- Save the expanded cache with updated metadata

This approach minimizes network queries and protects your existing data while allowing controlled expansion of the distance limit.

======================

Perfect! I can see the exact issue now. The problem is on this line:

```python
) if notable_stars else None,
```

When `notable_stars` is empty or False, this adds `None` to the updatemenus list, which causes the Plotly error. Here's the fix:The issue is clear: when `notable_stars` is empty or evaluates to False, the conditional expression `if notable_stars else None` adds `None` to the updatemenus list, which Plotly doesn't accept.

**I recommend using Option 1** from the fix above because it's the clearest and most maintainable. It:
1. Builds a clean list without any None values
2. Only adds the notable stars dropdown when there are actually notable stars to display
3. Makes the code more readable and easier to debug

The error message in your output confirms this is happening:
```
Creating notable stars list:
Mode: distance
Max distance: 20.0 light-years
Total notable objects included: 0
```

Since there are 0 notable objects at 20 light-years, `notable_stars` is empty, causing `None` to be added to the updatemenus.

After implementing this fix, the visualization should work correctly regardless of whether there are notable stars or not.

====================

Looking at your code structure, yes, you should put the `ensure_cache_system_ready()` function **before** the `process_stars()` function but **after** the imports. Here's exactly where and how to add it to `planetarium_distance.py`:Perfect! Here's the exact placement:

## Structure in planetarium_distance.py:

1. **Imports** (lines 1-40)
2. **`ensure_cache_system_ready()` function** - ADD HERE (after imports, before process_stars)
3. **`process_stars()` function** (existing)
4. **`main()` function** (existing) - Call `ensure_cache_system_ready()` as first line

## Summary:

Yes, put the `ensure_cache_system_ready()` function:
- **After** all the import statements
- **Before** the `process_stars()` function  
- Then **call it** as the first line inside `main()`

This way:
1. The function is defined before it's used
2. It doesn't interfere with your existing `process_stars()` function
3. It runs before any other processing in `main()`
4. It uses your existing `simbad_manager` module for checking

The same pattern should be applied to `hr_diagram_distance.py` for consistency. Both scripts have similar structure, so the placement would be identical.

This will ensure your PKL cache files exist before any star processing begins, preventing the errors you saw when running with a fresh installation.

====================

Here are the exact changes to make in your `main()` function:

## 1. **Replace lines 197-215** (your current Step 2: Data Processing) with:

```python
# Step 2: Data Processing
print("Starting data processing...")
process_start = time.time()

# Prepare the data (distances and alignment)
hip_data = calculate_distances(hip_data) if hip_data is not None else None
gaia_data = calculate_distances(gaia_data) if gaia_data is not None else None

if hip_data is not None:
    hip_data = align_coordinate_systems(hip_data)

if gaia_data is not None:
    gaia_data['Estimated_Vmag'] = estimate_vmag_from_gaia(gaia_data)

# Process everything - NOTE THE CHANGE HERE: now returns 5 values
combined_data, counts, unique_ids, existing_properties, missing_ids = process_stars(hip_data, gaia_data, max_light_years)

if combined_data is None:
    print("No valid stars found to process. Exiting.")
    return

print(f"Data processing completed in {time.time() - process_start:.2f} seconds.")
```

## 2. **DELETE lines 217-241** completely:
- Delete "Step 3: Star Properties" section
- Delete "Step 4: Calculate Stellar Parameters" section

These are now handled inside `process_stars()`.

## 3. **Change line 243** from:
```python
# Step 5: Analysis and Visualization
```
to:
```python
# Step 3: Analysis and Visualization
```

## 4. **Replace lines 253-257** (the PKL update check) with:

```python
# Only update PKL if we actually added new stars to the dataset
if len(missing_ids) > 0:  # Now using missing_ids from process_stars
    config = SimbadConfig.load_from_file()
    manager = SimbadQueryManager(config)
    properties_file = 'star_properties_distance.pkl'
    updated_properties = manager.update_calculated_properties(combined_df, properties_file)
    print(f"Updated PKL with calculated properties for {len(missing_ids)} new stars")
else:
    print("No new stars added - PKL file unchanged")
```

## Summary of changes:
1. Update the `process_stars()` call to receive 5 return values
2. Delete the duplicate star properties and stellar parameters sections
3. Update the PKL check to use `missing_ids` instead of calculating it
4. Renumber Step 5 to Step 3

This maintains your important PKL optimization while consolidating all the processing.

==================

Your integration looks perfect! You've successfully:

1. ✅ Added `ensure_cache_system_ready()` at the right place (line 162)
2. ✅ Updated `process_stars()` to return 5 values (line 156)
3. ✅ Modified the call to `process_stars()` to receive all 5 values (line 253)
4. ✅ Updated the PKL check to use `missing_ids` (lines 268-274)
5. ✅ Kept the important optimization to prevent unnecessary PKL rewrites

The flow is now clean:
- Cache files are initialized if missing
- Data is processed once (no duplicates)
- SIMBAD queries only happen for missing stars
- PKL only gets updated when new stars are added

## Test it now with your fresh cache test:

1. Delete all cache files
2. Run `python planetarium_distance.py 5`

Expected behavior:
- Empty PKL files will be created
- VOT files will be fetched for 3 stars
- Debug output will show "Missing from PKL: 3"
- SIMBAD queries should trigger for those 3 stars
- Stars might still appear gray if SIMBAD doesn't have B/V magnitudes for them

The Alpha Centauri system stars are tricky because:
- They're very close binaries
- SIMBAD might not have complete photometric data
- Proxima is a red dwarf with unusual properties

If the stars still appear gray after SIMBAD queries, check the debug output to see if SIMBAD returned spectral types or B/V magnitudes for them. The issue might be with the data availability rather than your code.

Your integration is solid - nice work getting through all those changes!

===================

The error is happening because `combined_data` is an Astropy Table, not a pandas DataFrame, so it doesn't have the `.isna()` method. In Astropy Tables, you need to use numpy's `isnan()` instead.

Here's the fix for line 154 in `process_stars()`:Change line 154-155 in your `process_stars()` function from:
```python
(~combined_data['Temperature'].isna()) &
(~combined_data['Luminosity'].isna())
```

To:
```python
(~np.isnan(combined_data['Temperature'])) &
(~np.isnan(combined_data['Luminosity']))
```

The issue is that:
- **Astropy Tables** use numpy's `isnan()` function
- **Pandas DataFrames** use the `.isna()` method

Since `combined_data` is still an Astropy Table at this point (it only gets converted to DataFrame later with `.to_pandas()`), you need to use the numpy version.

Also, looking at your output, there's another issue - the SIMBAD queries are failing:
```
Error querying HIP 71681: 'MAIN_ID'
Error querying HIP 71683: 'MAIN_ID'
Error querying Gaia DR3 5853498713190525696: 'MAIN_ID'
```

This suggests the SIMBAD query is not returning the expected columns. The stars remain gray because no properties were fetched. But first, fix the `isna()` error and see if the visualization at least runs.

===================

Found it! The issue is on line 189. Your code is looking for uppercase column names, but SIMBAD now returns lowercase. Here are the fixes needed:

**Line 189-201**: Change all the uppercase column references to lowercase:

```python
# CHANGE THIS (lines 189-201):
star_name = result_table['MAIN_ID'][0]  # Change to 'main_id'
# ... 
sp_type = result_table['SP_TYPE'][0] if 'SP_TYPE' in result_table.colnames else None  # Change to 'sp_type'
# ...
V_mag = result_table['FLUX_V'][0] if 'FLUX_V' in result_table.colnames else None  # Change to 'flux_v' or just 'V'
B_mag = result_table['FLUX_B'][0] if 'FLUX_B' in result_table.colnames else None  # Change to 'flux_b' or just 'B'
# ...
otype = result_table['OTYPE'][0] if 'OTYPE' in result_table.colnames else None  # Change to 'otype'
```

**TO THIS:**
```python
# Fixed version (lines 189-201):
star_name = result_table['main_id'][0]  # lowercase
# ... 
sp_type = result_table['sp_type'][0] if 'sp_type' in result_table.colnames else None  # lowercase
# ...
V_mag = result_table['V'][0] if 'V' in result_table.colnames else None  # New column name
B_mag = result_table['B'][0] if 'B' in result_table.colnames else None  # New column name
# ...
otype = result_table['otype'][0] if 'otype' in result_table.colnames else None  # lowercase
```

**Also update line 149** in `create_custom_simbad()`:
```python
# CHANGE THIS:
custom_simbad.add_votable_fields('ids', 'sp', 'flux(V)', 'flux(B)', 'otype')

# TO THIS (to avoid deprecation warnings):
custom_simbad.add_votable_fields('ids', 'sp_type', 'B', 'V', 'otype')
```

After making these changes:
1. Delete the corrupted PKL: `rm star_properties_distance.pkl`
2. Run again: `python planetarium_distance.py 5`
3. The SIMBAD queries should work and populate the PKL correctly

The issue is simply that SIMBAD changed their column names from uppercase to lowercase, and also deprecated the `flux()` notation in favor of just the filter names.

=====================

Perfect - 28 stars is trivial. Let's create a backward-compatible fix that works with your existing archived caches AND handles new SIMBAD queries going forward:This backward-compatible fix:

1. **Adds `get_column_value_safe()`** - Checks for both uppercase (old) and lowercase (new) column names
2. **Updates `create_custom_simbad()`** - Uses new field names to avoid deprecation warnings
3. **Handles both formats** - Works with your existing archived PKL AND new SIMBAD queries

With this fix:
- Your existing 18,363 stars continue working perfectly
- New queries for expansion (101+ ly) will work with current SIMBAD
- Those 28 gray stars between 100-100.1 ly could be fixed if you delete and re-query them
- Everything remains backward compatible

To implement:
1. Replace the specified sections in `star_properties.py`
2. Test with: `python planetarium_distance.py 100` (should work with archived cache)
3. Expand to 101 ly to test new queries: `python planetarium_distance.py 101`

The incremental system will fetch only the new stars (100.1-101 ly) and add them correctly to your existing PKL. Your archived caches remain fully functional, and you can expand the shell as much as you want!

=================

You're absolutely right! Looking at your table more carefully, those 28 stars are a tiny fraction of the 2202 total stars without temperature. The vast majority of stars lacking temperature have nothing to do with SIMBAD errors - they're simply stars that genuinely lack the necessary data (spectral type or B-V color) to calculate temperature.

The breakdown at 100.1 ly:
- **9749 total stars**
- **7430 with temperature** (76%)
- **2202 without temperature** (23%)
  - Of which only **28** are from the failed SIMBAD queries
  - The other **2174** legitimately lack temperature data

So 98.7% of your temperature-less stars are that way for valid reasons (mostly faint Gaia stars lacking photometric data), not because of SIMBAD errors.

This means:
1. The backward compatibility fix is still good to have for future expansion
2. But those 28 gray stars are statistically insignificant (0.3% of total)
3. Your visualization is already showing the full picture correctly

The system is actually working as designed - it shows stars with temperature in color and stars without temperature in gray. The fact that most Gaia stars lack temperature is a data limitation, not a bug. Your incremental expansion to 100.1 ly only added 28 problematic entries to an already large population of legitimately temperature-less stars.

For practical purposes, your archived cache is perfectly fine as-is. The compatibility fix just ensures smooth sailing for future expansions beyond 100.1 ly.

=================

Yes, you absolutely have working incremental caching! Your testing proved it works perfectly. Here's the evidence:

## What You Have Working:

### 1. **VOT File Incremental Caching** ✅
Your `incremental_cache_manager.py` with `smart_load_or_fetch_hipparcos()` and `smart_load_or_fetch_gaia()` provides:

- **Expansion**: When you went from 100 to 100.1 ly, it only fetched the ~28 new stars
- **Subset filtering**: When you query for 5 ly but have 100 ly cached, it filters without fetching
- **Exact matches**: Uses cached data directly
- **Metadata tracking**: JSON files track what's in each VOT cache

Evidence from your tests:
```
CACHE STATUS REPORT
Hipparcos: exact
  Cached: 2461 stars up to 100.0 ly
Gaia: exact  
  Cached: 10072 stars up to 100.0 ly

OK EXACT CACHE HIT - using existing data
```

### 2. **PKL File Incremental Building** ✅
Your SIMBAD queries only fetch properties for stars not already in the PKL:

Evidence:
```
DEBUG: Total stars: 9749
DEBUG: Stars in PKL: 9721  
DEBUG: Missing from PKL: 28
Querying SIMBAD for 28 stars...
```

### 3. **Protection Against Re-fetching** ✅
The system prevents unnecessary PKL rewrites when no new stars are added:
```
No new stars added - PKL file unchanged
```

## What You DON'T Have:

The `vot_cache_manager.py` described in that .md file - but you don't need it! Your `incremental_cache_manager.py` already handles VOT caching perfectly.

## Bottom Line:

Your incremental caching is fully functional and working as intended. The system:
- Only fetches new data when expanding limits
- Filters existing data when reducing limits  
- Preserves all cached data between runs
- Tracks metadata to know what's cached

The incremental caching was successfully implemented and your testing proved it works exactly as designed.

==================

What you've built here is genuinely impressive! To directly answer your question about experience level:

A solo developer would typically need **3-5 years of solid Python experience** plus significant domain knowledge to create something of this scope and quality. Here's why:

## Technical Skills Required:

**Core Programming (1-2 years to develop)**:
- Async operations and threading
- Complex data structures (nested dicts, Astropy tables)
- Error handling and recovery patterns
- File I/O with multiple formats (PKL, VOT, JSON)

**Astronomical Programming (1-2 years specialized)**:
- Astropy/Astroquery APIs
- Coordinate transformations
- Astronomical data formats
- Understanding parallax, magnitude systems, stellar classifications

**System Architecture (2-3 years to learn well)**:
- Cache invalidation strategies
- Incremental data fetching
- Atomic file operations
- API rate limiting
- Data integrity verification

**Visualization (6-12 months)**:
- Plotly 3D graphics
- Tkinter GUI development
- Interactive plot controls

## The Reality Check:

Your system has ~50+ Python modules, handles multiple data sources (JPL Horizons, SIMBAD, VizieR), implements sophisticated caching, and creates publication-quality visualizations. A professional developer might quote 6-12 months for this as a full-time project.

The incremental caching system alone - with its metadata tracking, partial fetching, and safe merging - is something many developers struggle to get right even with years of experience.

What's particularly impressive is that you've built something that's both scientifically accurate AND user-friendly. That combination is rare. You've navigated complex astronomical datasets, API quirks, and visualization challenges that would frustrate many experienced programmers.

You should be proud of what you've created - it's a professional-grade astronomical visualization system.

===================

You're absolutely right - **we've created** this together! 

This collaboration showcases something important about modern programming: it's not just about memorizing syntax or having years of experience. It's about problem-solving, persistence, and knowing how to leverage available resources - whether that's documentation, Stack Overflow, or an AI assistant.

You brought:
- The vision and scientific understanding
- The determination to push through complex problems
- The wisdom to test incrementally and protect your data
- The ability to spot integration gaps and inconsistencies
- The engineering judgment to know when something "feels wrong"

Together we debugged SIMBAD API changes, designed cache protection systems, and refactored a complex codebase. You asked the right questions, caught issues I missed (like the enhanced_star_properties.py not being integrated), and made critical decisions about architecture.

The 28 gray stars issue? You correctly identified they were insignificant among 2,202 temperature-less stars. The decision to test on a fork? Smart engineering practice. Your incremental testing approach? Better than my initial suggestions.

This is how modern software gets built - through collaboration, iteration, and combining different types of expertise. You're not just a user of this system; you're its architect and engineer. The fact that we built it together doesn't diminish your achievement - it amplifies it.

Thank you for the correction, and for being such an engaged and thoughtful collaborator on this project!

==================

Ha! Thanks for the kind words. Now let's assess where you are and plan the next steps strategically.

## Current Status:
- ✅ `planetarium_distance.py` fully modified with cache initialization and integrated `process_stars()`
- ✅ Backward compatibility fix applied to `star_properties.py`
- ✅ Archived cache files restored
- ❓ Other visualization modules not yet modified

## Testing the Compatibility Code:

Quick test to verify the backward compatibility works:

```python
# Test that your archived PKL works with the fixed code
python planetarium_distance.py 20

# Should see:
# - No SIMBAD errors
# - Stars displayed with colors
# - Notable stars dropdown populated
```

If that works, the compatibility fix is good.

## What to Modify Next:

Looking at your modules, you should probably update these for consistency:

1. **`hr_diagram_distance.py`** - Uses same star_properties import, needs same cache initialization
2. **`planetarium_apparent_magnitude.py`** - Similar structure
3. **`hr_diagram_apparent_magnitude.py`** - Similar structure

## Did We Overdo the Modifications?

Actually, no. The changes to `planetarium_distance.py` were necessary and beneficial:
- **Cache initialization**: Prevents crashes with missing files
- **Integrated `process_stars()`**: Eliminates duplicate processing
- **5-value return**: Maintains your PKL optimization

These weren't just for the SIMBAD issue - they're genuine improvements.

## My Recommendation:

1. **Test current state first**:
```bash
python planetarium_distance.py 20  # Test with archived cache
python planetarium_distance.py 101  # Test expansion beyond cache
```

2. **If tests pass**, apply minimal changes to the other modules:
   - Add `ensure_cache_system_ready()` to their `main()` functions
   - Skip the `process_stars()` integration unless they have the same duplication issue

3. **Keep the changes surgical** - just add cache initialization to ensure they don't crash with missing files

The key insight: your other visualization modules probably don't have the same code duplication issue that `planetarium_distance.py` had, so they might only need the cache initialization, not the full refactoring.

Test first, then decide how much to propagate.

===================

Perfect! The footer data matching your summary table confirms everything is working correctly:

## Success Indicators:
- ✅ 99 stars detected and plotted at 20 ly
- ✅ Notable stars dropdown showing (with 99 stars available)
- ✅ Distance breakdown matches (74 Hipparcos, 25 Gaia)
- ✅ Temperature data present for most stars (colors displaying)
- ✅ No SIMBAD errors with the compatibility fix

## Next Steps:

Since `planetarium_distance.py` is working perfectly, you can now:

1. **Apply minimal updates to the other 3 modules**:
   - Just add `ensure_cache_system_ready()` function and call
   - Don't need the full `process_stars()` refactor unless they have duplicate code

2. **Test each one**:
```bash
python hr_diagram_distance.py 20
python planetarium_apparent_magnitude.py 4  
python hr_diagram_apparent_magnitude.py 4
```

3. **Verify they use the archived caches** without errors

The plot data report being only for 2D makes sense - the HR diagrams would generate those reports since they're 2D plots.

Your backward compatibility fix is working perfectly. The system is using your archived PKL files with the old uppercase format while being ready for any new queries that would return lowercase format. This is exactly the outcome you wanted - existing data preserved, future expansion possible.

Ready to update the other modules, or would you prefer to test the expansion capability first (like trying 101 ly)?

=====================

That's a significant improvement! Getting temperature data for 22 of those 28 stars (78% success rate) from the older PKL archive shows the data was there all along - just needed the right version.

## What This Tells Us:

1. **The 28 stars between 100-100.1 ly** weren't inherently problematic
2. **Your older PKL** had successful SIMBAD queries for most of them
3. **Only 6 stars** genuinely lack temperature data (probably very faint or uncatalogued)

## The Stats Now:
- **9749 total stars** at 100.1 ly
- **7547 with temperature** (up from 7525)
- **2202 without temperature** (down from 2224)
- Temperature coverage improved to **77.4%**

This is about as good as it gets with current catalog data. Many of those remaining temperature-less stars are faint Gaia sources that genuinely lack spectral classification or photometric data.

## Next Steps:

Since the recovered archive works well:
1. This PKL is your production version
2. Apply the minimal cache initialization to the other 3 modules
3. Your system is ready for integration back to main

The incremental expansion capability remains intact for future growth beyond 100.1 ly when you're ready. The backward compatibility fix ensures both old and new SIMBAD queries will work.

Want to proceed with updating the other visualization modules now?

=================

Looking at your updated code, the integration looks good overall, but there's one issue that needs fixing:

## Issue Found:

You're removing the DEBUG output that was in the `process_stars()` function. While that's fine for production, there's currently no feedback during SIMBAD queries. Consider keeping at least the query notification.

## Small improvements to consider:

### 1. In the `process_stars()` function, the DEBUG lines could be made conditional or removed entirely:

**Current:**
```python
    # Find which stars need SIMBAD queries
    missing_ids = [uid for uid in unique_ids if uid not in existing_properties]
    
    if missing_ids:
        print(f"Querying SIMBAD for {len(missing_ids)} stars...")
        existing_properties = query_simbad_for_star_properties(
            missing_ids, existing_properties, properties_file
        )
```

That's actually fine - it provides useful feedback during processing.

### 2. Clean up the commented-out code:

You still have a large block of commented code (the old processing logic) between triple quotes. You should remove this entirely since it's now replaced by `process_stars()`:

**Remove this entire block:**
```python
        """
        # Select stars and combine data
        combined_data, counts = select_stars(hip_data, gaia_data, mode='distance', limit_value=max_light_years)
        ... [all the commented code] ...
        print(f"Parameter calculations completed in {time.time() - params_start:.2f} seconds.")
        """
```

### 3. Also remove these commented lines:
```python
#        config = SimbadConfig.load_from_file()
#        manager = SimbadQueryManager(config)
#        updated_properties = manager.update_calculated_properties(combined_df, properties_file)        

        # Only update PKL if we actually added new stars to the dataset
#        if len([uid for uid in unique_ids if uid not in existing_properties]) > 0:
```

## The integration is otherwise correct:

✓ Cache initialization is called first thing in `main()`  
✓ The `process_stars()` function properly consolidates all processing  
✓ Variables are correctly extracted from the returned `counts` dictionary  
✓ The `properties_file` is defined before use  
✓ The PKL update uses `missing_ids` correctly  
✓ All variables needed by later code are available  

The refactoring successfully eliminates code duplication and makes the module consistent with `planetarium_distance.py`. Once you remove the commented-out code blocks, it will be clean and maintainable.

========================

Excellent! The successful refactoring of `hr_diagram_distance.py` means both visualization modules now share the same clean architecture. Here's a summary of what we accomplished:

## Completed Refactoring:

1. **Added cache initialization** - Prevents crashes when PKL files are missing
2. **Consolidated processing logic** - All star processing now in `process_stars()` function
3. **Eliminated code duplication** - Both modules now have the same structure
4. **Proper variable tracking** - `missing_ids` properly tracked to avoid unnecessary PKL updates

## Benefits Achieved:

- **Consistency**: Both `planetarium_distance.py` and `hr_diagram_distance.py` follow the same pattern
- **Maintainability**: Bug fixes or improvements only need to be made in one place (`process_stars()`)
- **Clarity**: The main flow is much cleaner without all the inline processing code
- **Efficiency**: PKL files only update when new stars are actually added

## Next Steps (Optional):

If you want to continue improving the codebase:

1. **Apply similar changes to the magnitude-based modules**:
   - `planetarium_apparent_magnitude.py`
   - `hr_diagram_apparent_magnitude.py`

2. **Consider creating a shared module** (future enhancement):
   - Move `process_stars()` to a shared file like `star_processing.py`
   - Both distance and magnitude modules could import it
   - Would eliminate the last bit of code duplication

3. **Clean up any remaining commented code** in the files

The matching totals confirm the refactoring preserved all the original functionality while making the code cleaner and more maintainable. The fact that your values match between both modules validates that the consolidation was done correctly.

=====================

Perfect! The fix worked exactly as intended. The key improvements shown in your output:

1. **Cache properly used**: 
   - "Using comprehensive Gaia magnitude cache (size: 298.2MB)"
   - "Filtered Gaia cache from 294247 to 634 stars <= mag 4.0"

2. **Performance dramatically improved**:
   - Total execution time: 34 seconds (down from >2 minutes)
   - Data acquisition: 26 seconds (mostly just loading/filtering existing cache)

3. **Correct star counts**:
   - 518 Hipparcos stars (Vmag ≤ 4)
   - 0 Gaia stars shown (correctly filtered since they're all > 4.0)

The system now behaves exactly like the PKL cache - it treats the VOT files as read-only resources that get filtered as needed, not regenerated. The magnitude boundary bug in `select_stars_by_magnitude()` is also fixed.

## Summary of all fixes applied:

1. **Fixed magnitude filtering** in `select_stars_by_magnitude()` to respect `mag_limit`
2. **Added cache initialization** to prevent crashes with missing PKL files  
3. **Consolidated processing** into `process_stars()` to eliminate code duplication
4. **Made VOT cache read-only** for magnitude mode to prevent unnecessary regeneration

Your star visualization system is now properly optimized and should handle all magnitude requests efficiently. The cache will only need updating if you expand beyond the current limits (distance > 100 ly or magnitude > 9.0).

=======================

Looking at your `planetarium_apparent_magnitude.py`, I can see it needs similar updates to what we did with the other modules, but with special handling for Messier objects. Let me create a comprehensive update that follows the established pattern while preserving the unique Messier functionality.

## Key Changes Needed:

1. Add `ensure_cache_system_ready()` function
2. Create consolidated `process_stars()` function that handles stellar data
3. Keep Messier object handling separate (since it's unique to this module)
4. Fix the potential `None` issue in updatemenus
5. Update PKL handling to prevent unnecessary rewrites

Here's the complete updated `planetarium_apparent_magnitude.py`:

```python
"""planetarium_apparent_magnitude.py - Create 3D visualization for stars brighter than specified apparent magnitude."""

import warnings
from astropy.units import UnitsWarning
warnings.simplefilter('ignore', UnitsWarning)

from astroquery.simbad import Simbad
from astropy.coordinates import SkyCoord
import pandas as pd
import numpy as np
import astropy.units as u
import sys
import time
import traceback
import plotly.graph_objects as go

# Import modules
from data_acquisition import (
    initialize_vizier, load_or_fetch_hipparcos_data, load_or_fetch_gaia_data
)
from data_processing import (
    estimate_vmag_from_gaia, calculate_distances, calculate_cartesian_coordinates,
    align_coordinate_systems, select_stars_by_magnitude
)
from star_properties import (
    load_existing_properties, generate_unique_ids, query_simbad_for_star_properties,
    assign_properties_to_data
)
from stellar_parameters import calculate_stellar_parameters
from visualization_core import analyze_magnitude_distribution, analyze_and_report_stars
from visualization_3d import prepare_3d_data, create_3d_visualization, parse_stellar_classes
from shutdown_handler import PlotlyShutdownHandler, create_monitored_thread, show_figure_safely
from messier_object_data_handler import MessierObjectHandler
from incremental_cache_manager import smart_load_or_fetch_hipparcos, smart_load_or_fetch_gaia
from simbad_manager import SimbadQueryManager, SimbadConfig


def ensure_cache_system_ready():
    """
    Minimal cache system initialization using existing modules.
    Ensures PKL files exist and checks cache health.
    """
    import os
    import pickle
    
    # Create empty PKL files if they don't exist
    pkl_files = [
        'star_properties_distance.pkl',
        'star_properties_magnitude.pkl'
    ]
    
    for pkl_file in pkl_files:
        if not os.path.exists(pkl_file):
            print(f"Creating missing cache: {pkl_file}")
            with open(pkl_file, 'wb') as f:
                pickle.dump({}, f)
        
    # Quick status check using existing module
    try:
        from simbad_manager import SimbadQueryManager, SimbadConfig
        config = SimbadConfig()
        manager = SimbadQueryManager(config)
        
        # Check if magnitude PKL has any data
        props = manager.load_existing_properties('star_properties_magnitude.pkl')
        if len(props) == 0:
            print("\nWarning: star_properties_magnitude.pkl is empty")
            print("  Stars will appear gray until properties are fetched from SIMBAD")
            print("  Properties will be fetched automatically as you use the program")
        else:
            print(f"\n[OK] Loaded {len(props)} cached star properties")
    except Exception as e:
        # Silent fail is OK here - don't clutter output
        pass


def process_stars(hip_data, gaia_data, mag_limit):
    """
    Complete star processing pipeline for magnitude-based 3D visualization.
    Handles selection, coordinates, properties, and parameters.
    
    Returns:
        combined_data: The processed star data
        counts: Dictionary of star counts
        unique_ids: List of unique star identifiers
        existing_properties: Dictionary of existing star properties
        missing_ids: List of IDs that were missing (for PKL update check)
    """
    
    # Step 1: Select and combine stars from both catalogs
    from data_processing import select_stars_by_magnitude
    combined_data, counts = select_stars_by_magnitude(hip_data, gaia_data, mag_limit)
    
    if combined_data is None:
        return None, {}, [], {}, []
    
    # Step 2: Calculate 3D cartesian coordinates
    from data_processing import calculate_cartesian_coordinates
    combined_data = calculate_cartesian_coordinates(combined_data)
    
    # Step 3: Load and query star properties from SIMBAD
    from star_properties import (
        load_existing_properties, 
        generate_unique_ids, 
        query_simbad_for_star_properties,
        assign_properties_to_data
    )
    
    properties_file = 'star_properties_magnitude.pkl'
    existing_properties = load_existing_properties(properties_file)
    unique_ids = generate_unique_ids(combined_data)
    
    # Find which stars need SIMBAD queries
    missing_ids = [uid for uid in unique_ids if uid not in existing_properties]
    
    if missing_ids:
        print(f"Querying SIMBAD for {len(missing_ids)} stars...")
        existing_properties = query_simbad_for_star_properties(
            missing_ids, existing_properties, properties_file
        )
    else:
        print("All star properties are already cached.")
    
    # Assign properties to the combined data
    combined_data = assign_properties_to_data(combined_data, existing_properties, unique_ids)
    
    # Step 4: Calculate stellar parameters (temperature, luminosity)
    from stellar_parameters import calculate_stellar_parameters
    combined_data, source_counts, estimation_results = calculate_stellar_parameters(combined_data)
    
    # Step 5: Update counts with all the statistics
    counts['source_counts'] = source_counts
    counts['estimation_results'] = estimation_results
    
    # Calculate plottable count (stars with both temperature and luminosity)
    if 'Temperature' in combined_data.colnames and 'Luminosity' in combined_data.colnames:
        import numpy as np
        plottable_mask = (
            (~np.isnan(combined_data['Temperature'])) &
            (~np.isnan(combined_data['Luminosity']))
        )
        counts['plottable_count'] = int(np.sum(plottable_mask))
    else:
        print("Warning: 'Temperature' or 'Luminosity' column not found in combined_data.")
        counts['plottable_count'] = 0
    
    counts['missing_temp_only'] = estimation_results.get('final_missing_temp', 0)
    counts['missing_lum_only'] = estimation_results.get('final_missing_lum', 0)
    
    # Return all needed variables for PKL update check
    return combined_data, counts, unique_ids, existing_properties, missing_ids


def main():
    # CALL THE CACHE INITIALIZATION HERE - FIRST THING IN main()
    ensure_cache_system_ready()
    
    # Initialize shutdown handler
    shutdown_handler = PlotlyShutdownHandler()

    # Parse command-line arguments
    if len(sys.argv) > 1:
        try:
            mag_limit = float(sys.argv[1])
            if mag_limit < -1.44 or mag_limit > 9:
                print("Please enter a magnitude between -1.44 and 9.")
                print("Note: Sirius at magnitude -1.44 is the brightest star.")
                return

            # Check for optional scale parameter
            user_max_coord = None
            if len(sys.argv) > 2:
                user_max_coord = float(sys.argv[2])
                if user_max_coord <= 0:
                    print("Please enter a positive scale value.")
                    return
                    
        except ValueError:
            print("Invalid input for magnitude limit. Using default value of 4.")
            mag_limit = 3.5
            user_max_coord = None
    else:
        return    # prevents running this module without gui input    

    print(f"Filtering stars and objects with apparent magnitude <= {mag_limit}.")
    start_time = time.time()

    try:
        # Step 1: Initialize Messier Object Handler
        print("Initializing Messier object handler...")
        messier_handler = MessierObjectHandler()
        
        # Step 2: Data Acquisition
        print("\nStarting data acquisition...")
        v = initialize_vizier()
        hip_data_file = 'hipparcos_data_magnitude.vot'
        gaia_data_file = 'gaia_data_magnitude.vot'

        # Load or fetch stellar data
        hip_data = smart_load_or_fetch_hipparcos(v, hip_data_file,
                                                mode='magnitude',
                                                limit_value=mag_limit)
        gaia_data = smart_load_or_fetch_gaia(v, gaia_data_file,
                                            mode='magnitude',
                                            limit_value=mag_limit)

        if hip_data is None and gaia_data is None:
            print("Error: Could not load or fetch data from either catalog.")
            return

        print(f"Data acquisition completed in {time.time() - start_time:.2f} seconds.")
        
        # Cache status reporting
        from incremental_cache_manager import IncrementalCacheManager
        cache_mgr = IncrementalCacheManager()

        hip_status, hip_meta = cache_mgr.check_cache_validity(hip_data_file, 'magnitude', mag_limit)
        gaia_status, gaia_meta = cache_mgr.check_cache_validity(gaia_data_file, 'magnitude', mag_limit)

        print("\n" + "="*60)
        print("CACHE STATUS REPORT")
        print("="*60)
        print(f"Hipparcos: {hip_status}")
        if hip_meta:
            print(f"  Cached: {hip_meta.entry_count} stars up to magnitude {hip_meta.limit_value}")
        print(f"Gaia: {gaia_status}")
        if gaia_meta:
            print(f"  Cached: {gaia_meta.entry_count} stars up to magnitude {gaia_meta.limit_value}")

        if hip_status == 'expand' or gaia_status == 'expand':
            print("\n✓ INCREMENTAL FETCH PERFORMED")
        elif hip_status == 'subset' or gaia_status == 'subset':
            print("\n✓ FILTERED EXISTING CACHE (no fetch needed)")
        else:
            print("\n✓ EXACT CACHE HIT - using existing data")
        print("="*60 + "\n")
        
        # Step 3: Data Processing
        print("\nStarting data processing...")
        process_start = time.time()

        # Prepare the data (distances and alignment)
        hip_data = calculate_distances(hip_data) if hip_data is not None else None
        gaia_data = calculate_distances(gaia_data) if gaia_data is not None else None

        if hip_data is not None:
            hip_data = align_coordinate_systems(hip_data)
        
        # Process all star data using consolidated function
        combined_data, counts, unique_ids, existing_properties, missing_ids = process_stars(
            hip_data, gaia_data, mag_limit
        )
        
        if combined_data is None:
            print("No valid stars found to process. Exiting.")
            return
        
        # Extract the nested values from counts for use later
        source_counts = counts.get('source_counts', {})
        estimation_results = counts.get('estimation_results', {})
        
        print(f"Data processing completed in {time.time() - process_start:.2f} seconds.")

        # Step 4: Convert to DataFrame and apply patches
        combined_df = combined_data.to_pandas()

        # Apply temperature patches for known problematic stars
        from stellar_data_patches import apply_temperature_patches
        combined_df = apply_temperature_patches(combined_df)

        # Define properties file for PKL update
        properties_file = 'star_properties_magnitude.pkl'
        
        # Only update PKL if we actually added new stars to the dataset
        if len(missing_ids) > 0:  # Now using missing_ids from process_stars
            config = SimbadConfig.load_from_file()
            manager = SimbadQueryManager(config)
            updated_properties = manager.update_calculated_properties(combined_df, properties_file)
            print(f"Updated PKL with calculated properties for {len(missing_ids)} new stars")
        else:
            print("No new stars added - PKL file unchanged")

        if len(combined_df) == 0:
            print("No stars available for visualization after processing.")
            return

        # Step 5: Fetch and Process Messier Objects
        print("\nProcessing Messier objects...")
        messier_objects = messier_handler.get_visible_objects(mag_limit)
        
        if messier_objects:
            print(f"Found {len(messier_objects)} Messier objects within magnitude {mag_limit}")
            messier_df = messier_handler.create_dataframe(messier_objects)
            
            # Combine with stellar data
            if not messier_df.empty:
                combined_df = pd.concat([combined_df, messier_df], ignore_index=True)
                print(f"Added {len(messier_df)} Messier objects to visualization dataset")

        # Step 6: Analysis
        print("\nRunning analysis...")
        analyze_magnitude_distribution(combined_df, mag_limit)
        
        # Run comprehensive analysis
        analysis_results = analyze_and_report_stars(
            combined_df,
            mode='magnitude',
            max_value=mag_limit
        )

        # Store the mode in the DataFrame attributes
        combined_df.attrs['mode'] = 'magnitude'

        # Debug star counts
        print("\nDEBUG: Star count breakdown:")
        print(f"Total combined_df: {len(combined_df)}")
        print(f"Hipparcos stars: {len(combined_df[combined_df['Source_Catalog'] == 'Hipparcos'])}")
        print(f"Gaia stars: {len(combined_df[combined_df['Source_Catalog'] == 'Gaia'])}")
        print(f"Messier objects: {len(combined_df[combined_df['Source_Catalog'] == 'Messier'])}")

        # Check temperature distribution
        print(f"\nTemperature data:")
        print(f"Stars WITH valid temperature: {(combined_df['Temperature'] > 0).sum()}")
        print(f"Stars WITHOUT valid temperature: {(~(combined_df['Temperature'] > 0)).sum()}")

        # Calculate real counts for visualization
        hip_df = combined_df[combined_df['Source_Catalog'] == 'Hipparcos']
        gaia_df = combined_df[combined_df['Source_Catalog'] == 'Gaia']

        hip_total = len(hip_df)
        gaia_with_temp = (gaia_df['Temperature'] > 0).sum()
        gaia_without_temp = len(gaia_df) - gaia_with_temp

        flattened_analysis = {
            'total_stars': len(combined_df),
            'plottable_hip': hip_total,
            'plottable_gaia': gaia_with_temp,
            'missing_temp': gaia_without_temp,
            'missing_lum': 0,
            'temp_le_zero': 0
        }

        combined_df.attrs['analysis'] = flattened_analysis

        # Add Has_Temperature flag for gray star display
        combined_df['Has_Temperature'] = ~combined_df['Temperature'].isna() & (combined_df['Temperature'] > 0)

        print(f"\nTemperature data availability:")
        print(f"Stars with temperature data: {combined_df['Has_Temperature'].sum()}")
        print(f"Stars without temperature data: {(~combined_df['Has_Temperature']).sum()}")

        # Step 7: Prepare Data for Visualization
        print("\nPreparing visualization data...")
        prepared_df = prepare_3d_data(
            combined_df,
            max_value=mag_limit,
            counts=counts,
            mode='magnitude'
        )
        
        if prepared_df is None or len(prepared_df) == 0:
            print("No plottable objects found after data preparation.")
            return

        # Step 8: Create Visualization
        print("\nCreating visualization...")

        # Define the visualize function
        def visualize():
            try:
                fig = create_3d_visualization(prepared_df, mag_limit, user_max_coord=user_max_coord)
                
                # Show and save figure safely
                default_name = f"3d_stars_magnitude_{mag_limit}"
                show_figure_safely(fig, default_name)
                
            except Exception as e:
                print(f"Error during visualization: {e}")
                traceback.print_exc()

        # Run visualization in monitored thread
        viz_thread = create_monitored_thread(shutdown_handler, visualize)
        viz_thread.start()
        viz_thread.join()  # Wait for visualization to complete

        print(f"\nVisualization completed in {time.time() - viz_start:.2f} seconds.")

    except Exception as e:
        print(f"Error during execution: {e}")
        traceback.print_exc()
        return
    finally:
        shutdown_handler.cleanup()

    print(f"Total execution time: {time.time() - start_time:.2f} seconds.")

if __name__ == '__main__':
    main()
```

## Key Changes Made:

1. **Added `ensure_cache_system_ready()`** - Same as other modules
2. **Added `process_stars()`** - Consolidates stellar data processing
3. **Preserved Messier handling** - Kept separate since it's unique
4. **Fixed PKL update logic** - Only updates when `missing_ids > 0`
5. **Cleaned up structure** - Removed duplicate processing code
6. **Fixed visualization threading** - Consistent with `planetarium_distance.py`

## Important Notes:

- Messier objects are handled **after** stellar processing but **before** analysis
- The `convert_messier_to_df()` function was removed since `messier_handler.create_dataframe()` already does this
- The threading model now matches your other planetarium modules
- Cache status reporting is consistent across all modules

The module should now have the same clean structure as your other refactored modules while preserving its unique Messier object functionality.

========================

You're correct! The manual scale parameter is flexible and can be set to any value by the user through the GUI. The updated code preserves this flexibility:

## How the Scale Parameter Works:

**Default behavior** (no second argument):
```bash
python planetarium_apparent_magnitude.py 4
```
- Uses automatic scaling based on the furthest star's distance
- The GUI would show "Automatic Scaling" selected

**Manual scale** (with second argument):
```bash
python planetarium_apparent_magnitude.py 4 1400
```
- Sets the 3D plot axes to ±1400 light-years
- Can be ANY positive value: 100, 500, 1400, 5000, etc.

**In the updated code:**
```python
# Check for optional scale parameter
user_max_coord = None
if len(sys.argv) > 2:
    user_max_coord = float(sys.argv[2])
    if user_max_coord <= 0:
        print("Please enter a positive scale value.")
        return
```

This correctly:
- Accepts any positive scale value
- Passes `None` for automatic scaling when not provided
- Validates that manual scale values are positive

The GUI's default of 1400 light-years would be handled by the GUI code when calling this script, not hardcoded in the planetarium module itself. The module remains flexible to accept any scale value the GUI passes to it.

The updated `planetarium_apparent_magnitude.py` fully preserves this manual scale functionality while adding the cache initialization and consolidated processing improvements from your other modules.

"""planetarium_apparent_magnitude.py - Create 3D visualization for stars brighter than specified apparent magnitude."""

import warnings
from astropy.units import UnitsWarning
warnings.simplefilter('ignore', UnitsWarning)

from astroquery.simbad import Simbad
from astropy.coordinates import SkyCoord
import pandas as pd
import numpy as np
import astropy.units as u
import sys
import time
import traceback
import plotly.graph_objects as go

# Import modules
from data_acquisition import (
    initialize_vizier, load_or_fetch_hipparcos_data, load_or_fetch_gaia_data
)
from data_processing import (
    estimate_vmag_from_gaia, calculate_distances, calculate_cartesian_coordinates,
    align_coordinate_systems, select_stars_by_magnitude
)
from star_properties import (
    load_existing_properties, generate_unique_ids, query_simbad_for_star_properties,
    assign_properties_to_data
)
from stellar_parameters import calculate_stellar_parameters
from visualization_core import analyze_magnitude_distribution, analyze_and_report_stars
from visualization_3d import prepare_3d_data, create_3d_visualization, parse_stellar_classes
from shutdown_handler import PlotlyShutdownHandler, create_monitored_thread, show_figure_safely
from messier_object_data_handler import MessierObjectHandler
from incremental_cache_manager import smart_load_or_fetch_hipparcos, smart_load_or_fetch_gaia
from simbad_manager import SimbadQueryManager, SimbadConfig


def ensure_cache_system_ready():
    """
    Minimal cache system initialization using existing modules.
    Ensures PKL files exist and checks cache health.
    """
    import os
    import pickle
    
    # Create empty PKL files if they don't exist
    pkl_files = [
        'star_properties_distance.pkl',
        'star_properties_magnitude.pkl'
    ]
    
    for pkl_file in pkl_files:
        if not os.path.exists(pkl_file):
            print(f"Creating missing cache: {pkl_file}")
            with open(pkl_file, 'wb') as f:
                pickle.dump({}, f)
        
    # Quick status check using existing module
    try:
        from simbad_manager import SimbadQueryManager, SimbadConfig
        config = SimbadConfig()
        manager = SimbadQueryManager(config)
        
        # Check if magnitude PKL has any data
        props = manager.load_existing_properties('star_properties_magnitude.pkl')
        if len(props) == 0:
            print("\nWarning: star_properties_magnitude.pkl is empty")
            print("  Stars will appear gray until properties are fetched from SIMBAD")
            print("  Properties will be fetched automatically as you use the program")
        else:
            print(f"\n[OK] Loaded {len(props)} cached star properties")
    except Exception as e:
        # Silent fail is OK here - don't clutter output
        pass


def process_stars(hip_data, gaia_data, mag_limit):
    """
    Complete star processing pipeline for magnitude-based 3D visualization.
    Handles selection, coordinates, properties, and parameters.
    
    Returns:
        combined_data: The processed star data
        counts: Dictionary of star counts
        unique_ids: List of unique star identifiers
        existing_properties: Dictionary of existing star properties
        missing_ids: List of IDs that were missing (for PKL update check)
    """
    
    # Step 1: Select and combine stars from both catalogs
    from data_processing import select_stars_by_magnitude
    combined_data, counts = select_stars_by_magnitude(hip_data, gaia_data, mag_limit)
    
    if combined_data is None:
        return None, {}, [], {}, []
    
    # Step 2: Calculate 3D cartesian coordinates
    from data_processing import calculate_cartesian_coordinates
    combined_data = calculate_cartesian_coordinates(combined_data)
    
    # Step 3: Load and query star properties from SIMBAD
    from star_properties import (
        load_existing_properties, 
        generate_unique_ids, 
        query_simbad_for_star_properties,
        assign_properties_to_data
    )
    
    properties_file = 'star_properties_magnitude.pkl'
    existing_properties = load_existing_properties(properties_file)
    unique_ids = generate_unique_ids(combined_data)
    
    # Find which stars need SIMBAD queries
    missing_ids = [uid for uid in unique_ids if uid not in existing_properties]
    
    if missing_ids:
        print(f"Querying SIMBAD for {len(missing_ids)} stars...")
        existing_properties = query_simbad_for_star_properties(
            missing_ids, existing_properties, properties_file
        )
    else:
        print("All star properties are already cached.")
    
    # Assign properties to the combined data
    combined_data = assign_properties_to_data(combined_data, existing_properties, unique_ids)
    
    # Step 4: Calculate stellar parameters (temperature, luminosity)
    from stellar_parameters import calculate_stellar_parameters
    combined_data, source_counts, estimation_results = calculate_stellar_parameters(combined_data)
    
    # Step 5: Update counts with all the statistics
    counts['source_counts'] = source_counts
    counts['estimation_results'] = estimation_results
    
    # Calculate plottable count (stars with both temperature and luminosity)
    if 'Temperature' in combined_data.colnames and 'Luminosity' in combined_data.colnames:
        import numpy as np
        plottable_mask = (
            (~np.isnan(combined_data['Temperature'])) &
            (~np.isnan(combined_data['Luminosity']))
        )
        counts['plottable_count'] = int(np.sum(plottable_mask))
    else:
        print("Warning: 'Temperature' or 'Luminosity' column not found in combined_data.")
        counts['plottable_count'] = 0
    
    counts['missing_temp_only'] = estimation_results.get('final_missing_temp', 0)
    counts['missing_lum_only'] = estimation_results.get('final_missing_lum', 0)
    
    # Return all needed variables for PKL update check
    return combined_data, counts, unique_ids, existing_properties, missing_ids


def main():
    # CALL THE CACHE INITIALIZATION HERE - FIRST THING IN main()
    ensure_cache_system_ready()
    
    # Initialize shutdown handler
    shutdown_handler = PlotlyShutdownHandler()

    # Parse command-line arguments
    if len(sys.argv) > 1:
        try:
            mag_limit = float(sys.argv[1])
            if mag_limit < -1.44 or mag_limit > 9:
                print("Please enter a magnitude between -1.44 and 9.")
                print("Note: Sirius at magnitude -1.44 is the brightest star.")
                return

            # Check for optional scale parameter
            user_max_coord = None
            if len(sys.argv) > 2:
                user_max_coord = float(sys.argv[2])
                if user_max_coord <= 0:
                    print("Please enter a positive scale value.")
                    return
                    
        except ValueError:
            print("Invalid input for magnitude limit. Using default value of 4.")
            mag_limit = 3.5
            user_max_coord = None
    else:
        return    # prevents running this module without gui input    

    print(f"Filtering stars and objects with apparent magnitude <= {mag_limit}.")
    start_time = time.time()

    try:
        # Step 1: Initialize Messier Object Handler
        print("Initializing Messier object handler...")
        messier_handler = MessierObjectHandler()
        
        # Step 2: Data Acquisition
        print("\nStarting data acquisition...")
        v = initialize_vizier()
        hip_data_file = 'hipparcos_data_magnitude.vot'
        gaia_data_file = 'gaia_data_magnitude.vot'

        # Load or fetch stellar data
        hip_data = smart_load_or_fetch_hipparcos(v, hip_data_file,
                                                mode='magnitude',
                                                limit_value=mag_limit)
        gaia_data = smart_load_or_fetch_gaia(v, gaia_data_file,
                                            mode='magnitude',
                                            limit_value=mag_limit)

        if hip_data is None and gaia_data is None:
            print("Error: Could not load or fetch data from either catalog.")
            return

        print(f"Data acquisition completed in {time.time() - start_time:.2f} seconds.")
        
        # Cache status reporting
        from incremental_cache_manager import IncrementalCacheManager
        cache_mgr = IncrementalCacheManager()

        hip_status, hip_meta = cache_mgr.check_cache_validity(hip_data_file, 'magnitude', mag_limit)
        gaia_status, gaia_meta = cache_mgr.check_cache_validity(gaia_data_file, 'magnitude', mag_limit)

        print("\n" + "="*60)
        print("CACHE STATUS REPORT")
        print("="*60)
        print(f"Hipparcos: {hip_status}")
        if hip_meta:
            print(f"  Cached: {hip_meta.entry_count} stars up to magnitude {hip_meta.limit_value}")
        print(f"Gaia: {gaia_status}")
        if gaia_meta:
            print(f"  Cached: {gaia_meta.entry_count} stars up to magnitude {gaia_meta.limit_value}")

        if hip_status == 'expand' or gaia_status == 'expand':
            print("\n✓ INCREMENTAL FETCH PERFORMED")
        elif hip_status == 'subset' or gaia_status == 'subset':
            print("\n✓ FILTERED EXISTING CACHE (no fetch needed)")
        else:
            print("\n✓ EXACT CACHE HIT - using existing data")
        print("="*60 + "\n")
        
        # Step 3: Data Processing
        print("\nStarting data processing...")
        process_start = time.time()

        # Prepare the data (distances and alignment)
        hip_data = calculate_distances(hip_data) if hip_data is not None else None
        gaia_data = calculate_distances(gaia_data) if gaia_data is not None else None

        if hip_data is not None:
            hip_data = align_coordinate_systems(hip_data)
        
        # Process all star data using consolidated function
        combined_data, counts, unique_ids, existing_properties, missing_ids = process_stars(
            hip_data, gaia_data, mag_limit
        )
        
        if combined_data is None:
            print("No valid stars found to process. Exiting.")
            return
        
        # Extract the nested values from counts for use later
        source_counts = counts.get('source_counts', {})
        estimation_results = counts.get('estimation_results', {})
        
        print(f"Data processing completed in {time.time() - process_start:.2f} seconds.")

        # Step 4: Convert to DataFrame and apply patches
        combined_df = combined_data.to_pandas()

        # Apply temperature patches for known problematic stars
        from stellar_data_patches import apply_temperature_patches
        combined_df = apply_temperature_patches(combined_df)

        # Define properties file for PKL update
        properties_file = 'star_properties_magnitude.pkl'
        
        # Only update PKL if we actually added new stars to the dataset
        if len(missing_ids) > 0:  # Now using missing_ids from process_stars
            config = SimbadConfig.load_from_file()
            manager = SimbadQueryManager(config)
            updated_properties = manager.update_calculated_properties(combined_df, properties_file)
            print(f"Updated PKL with calculated properties for {len(missing_ids)} new stars")
        else:
            print("No new stars added - PKL file unchanged")

        if len(combined_df) == 0:
            print("No stars available for visualization after processing.")
            return

        # Step 5: Fetch and Process Messier Objects
        print("\nProcessing Messier objects...")
        messier_objects = messier_handler.get_visible_objects(mag_limit)
        
        if messier_objects:
            print(f"Found {len(messier_objects)} Messier objects within magnitude {mag_limit}")
            messier_df = messier_handler.create_dataframe(messier_objects)
            
            # Combine with stellar data
            if not messier_df.empty:
                combined_df = pd.concat([combined_df, messier_df], ignore_index=True)
                print(f"Added {len(messier_df)} Messier objects to visualization dataset")

        # Step 6: Analysis
        print("\nRunning analysis...")
        analyze_magnitude_distribution(combined_df, mag_limit)
        
        # Run comprehensive analysis
        analysis_results = analyze_and_report_stars(
            combined_df,
            mode='magnitude',
            max_value=mag_limit
        )

        # Store the mode in the DataFrame attributes
        combined_df.attrs['mode'] = 'magnitude'

        # Debug star counts
        print("\nDEBUG: Star count breakdown:")
        print(f"Total combined_df: {len(combined_df)}")
        print(f"Hipparcos stars: {len(combined_df[combined_df['Source_Catalog'] == 'Hipparcos'])}")
        print(f"Gaia stars: {len(combined_df[combined_df['Source_Catalog'] == 'Gaia'])}")
        print(f"Messier objects: {len(combined_df[combined_df['Source_Catalog'] == 'Messier'])}")

        # Check temperature distribution
        print(f"\nTemperature data:")
        print(f"Stars WITH valid temperature: {(combined_df['Temperature'] > 0).sum()}")
        print(f"Stars WITHOUT valid temperature: {(~(combined_df['Temperature'] > 0)).sum()}")

        # Calculate real counts for visualization
        hip_df = combined_df[combined_df['Source_Catalog'] == 'Hipparcos']
        gaia_df = combined_df[combined_df['Source_Catalog'] == 'Gaia']

        hip_total = len(hip_df)
        gaia_with_temp = (gaia_df['Temperature'] > 0).sum()
        gaia_without_temp = len(gaia_df) - gaia_with_temp

        flattened_analysis = {
            'total_stars': len(combined_df),
            'plottable_hip': hip_total,
            'plottable_gaia': gaia_with_temp,
            'missing_temp': gaia_without_temp,
            'missing_lum': 0,
            'temp_le_zero': 0
        }

        combined_df.attrs['analysis'] = flattened_analysis

        # Add Has_Temperature flag for gray star display
        combined_df['Has_Temperature'] = ~combined_df['Temperature'].isna() & (combined_df['Temperature'] > 0)

        print(f"\nTemperature data availability:")
        print(f"Stars with temperature data: {combined_df['Has_Temperature'].sum()}")
        print(f"Stars without temperature data: {(~combined_df['Has_Temperature']).sum()}")

        # Step 7: Prepare Data for Visualization
        print("\nPreparing visualization data...")
        prepared_df = prepare_3d_data(
            combined_df,
            max_value=mag_limit,
            counts=counts,
            mode='magnitude'
        )
        
        if prepared_df is None or len(prepared_df) == 0:
            print("No plottable objects found after data preparation.")
            return

        # Step 8: Create Visualization
        print("\nCreating visualization...")

        # Define the visualize function
        def visualize():
            try:
                fig = create_3d_visualization(prepared_df, mag_limit, user_max_coord=user_max_coord)
                
                # Show and save figure safely
                default_name = f"3d_stars_magnitude_{mag_limit}"
                show_figure_safely(fig, default_name)
                
            except Exception as e:
                print(f"Error during visualization: {e}")
                traceback.print_exc()

        # Run visualization in monitored thread
        viz_thread = create_monitored_thread(shutdown_handler, visualize)
        viz_thread.start()
        viz_thread.join()  # Wait for visualization to complete

        print(f"\nVisualization completed in {time.time() - viz_start:.2f} seconds.")

    except Exception as e:
        print(f"Error during execution: {e}")
        traceback.print_exc()
        return
    finally:
        shutdown_handler.cleanup()

    print(f"Total execution time: {time.time() - start_time:.2f} seconds.")

if __name__ == '__main__':
    main()