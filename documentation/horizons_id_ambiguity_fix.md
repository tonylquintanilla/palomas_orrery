# Fixing Horizons Query Ambiguity Issue

## Problem Identified

**Current Situation:**
- **Orbital paths** (vectors): Use proper Horizons ID from object's `'id'` field ✓
- **Osculating elements**: Use the name directly, which can be ambiguous! ❌

**Examples of Ambiguous Queries:**
- "Mercury" → Could be planet (199) or asteroid
- "Atlas" → Could be Saturn moon or ATLAS comet
- "3I/ATLAS" → Horizons doesn't recognize this format, needs 'C/2025 N1'
- "Pioneer 10" → Name vs spacecraft ID (-23)

## Current Code Flow

### For Orbital Paths (Works Correctly):
```python
# In orbit_data_manager.py line 671
object_id = obj_info['id']  # e.g., 'C/2025 N1'
id_type = obj_info['id_type']  # e.g., 'smallbody'
obj = Horizons(id=object_id, id_type=id_type, location=location, epochs=epochs)
```

### For Osculating Elements (Has Problem):
```python
# In palomas_orrery.py line 3897
fresh_elements = get_elements_with_prompt(obj_name, parent_window=root)

# In osculating_cache_manager.py line 488
fresh_entry = fetch_osculating_elements(obj_name)  # Just passes name!

# In osculating_cache_manager.py line 342
result = query_horizons_elements(obj_name, date_str)  # Still just name!
```

**Problem:** We're passing `obj_name` (e.g., '3I/ATLAS') instead of the proper Horizons ID ('C/2025 N1').

## Solution Options

### Option 1: Minimal Change - Look Up ID at Pre-fetch Time

**Modify palomas_orrery.py pre-fetch section:**

```python
# BEFORE (line 3894):
for obj_name in pre_fetch_objects:
    fresh_elements = get_elements_with_prompt(obj_name, parent_window=root)

# AFTER:
for obj_name in pre_fetch_objects:
    # Find the object dictionary to get its Horizons ID
    obj_dict = next((obj for obj in selected_objects_for_prefetch if obj['name'] == obj_name), None)
    
    if obj_dict:
        horizons_id = obj_dict.get('id', obj_name)  # Use ID if available, fall back to name
        id_type = obj_dict.get('id_type', 'smallbody')  # Get ID type
        
        # Pass both name (for caching) and Horizons ID (for querying)
        fresh_elements = get_elements_with_prompt(
            obj_name, 
            horizons_id=horizons_id,
            id_type=id_type,
            parent_window=root
        )
    else:
        # Fallback to old behavior if object not found
        fresh_elements = get_elements_with_prompt(obj_name, parent_window=root)
```

### Option 2: Comprehensive - Update All Functions

**1. Update `get_elements_with_prompt` signature:**
```python
def get_elements_with_prompt(obj_name, horizons_id=None, id_type='smallbody', parent_window=None):
    """
    Parameters:
        obj_name (str): Display name for caching and dialogs
        horizons_id (str, optional): Horizons ID to query (defaults to obj_name)
        id_type (str): Horizons ID type ('smallbody', 'majorbody', etc.)
        parent_window: Parent window for dialog
    """
    # Use horizons_id if provided, otherwise fall back to name
    query_id = horizons_id if horizons_id else obj_name
```

**2. Update `fetch_osculating_elements`:**
```python
def fetch_osculating_elements(obj_name, horizons_id=None, id_type='smallbody', date=None):
    """
    Parameters:
        obj_name (str): Display name for metadata
        horizons_id (str, optional): Horizons ID to query
        id_type (str): Horizons ID type
        date (datetime, optional): Date for osculating elements
    """
    query_id = horizons_id if horizons_id else obj_name
    
    # Pass to query function
    result = query_horizons_elements(query_id, id_type, date_str)
```

**3. Create `query_horizons_elements` in orbit_data_manager.py:**
```python
def query_horizons_elements(horizons_id, id_type='smallbody', date_str=None):
    """
    Fetch osculating orbital elements from JPL Horizons.
    
    Parameters:
        horizons_id (str): Horizons ID (e.g., 'C/2025 N1', '199', '-23')
        id_type (str): Horizons ID type ('smallbody', 'majorbody', 'id', etc.)
        date_str (str): Date string in 'YYYY-MM-DD' format
    
    Returns:
        dict: Orbital elements with metadata
    """
    from astropy.time import Time
    
    if date_str is None:
        date_str = datetime.now().strftime('%Y-%m-%d')
    
    # Convert date to Julian Date
    dt = Time(date_str)
    epoch_jd = dt.jd
    
    # Query Horizons with proper ID and ID type
    obj = Horizons(id=horizons_id, id_type=id_type, location='@sun', epochs=epoch_jd)
    el = obj.elements()
    row = el[0]
    
    # Extract elements with flexible column lookup...
    # (existing code for get_col, unit conversion, etc.)
```

## Recommended Solution

**Use Option 2** (Comprehensive) because:
1. ✅ Eliminates ambiguity completely
2. ✅ Consistent with how orbital paths work
3. ✅ Future-proof for new objects
4. ✅ Proper separation of display name vs query ID
5. ✅ Allows cache to use display names while queries use proper IDs

## Implementation Steps

### Step 1: Create `query_horizons_elements` in orbit_data_manager.py
- Use proper Horizons ID and ID type
- Include all the fixes (Julian Date, flexible columns, unit conversion)
- Return standardized dictionary format

### Step 2: Update osculating_cache_manager.py
- Modify `fetch_osculating_elements` to accept horizons_id and id_type
- Modify `get_elements_with_prompt` to accept horizons_id and id_type
- Pass these parameters through the chain

### Step 3: Update palomas_orrery.py pre-fetch sections
- Look up object dictionary to get ID and ID type
- Pass all three parameters: name, horizons_id, id_type
- Do this in BOTH `plot_objects()` and `animate_objects()`

### Step 4: Update animate_objects() similarly
- Same changes as plot_objects()

## Testing Verification

**Test with ambiguous objects:**
1. **Mercury** (planet) - Should query '199' with id_type='majorbody'
2. **3I/ATLAS** - Should query 'C/2025 N1' with id_type='smallbody'
3. **Pioneer 10** - Should query '-23' with id_type='id'

**Check console output:**
```
[PRE-FETCH] Checking osculating elements for 3 objects...
⟳ Fetching osculating elements for Mercury from JPL Horizons...
   Using Horizons ID: 199 (majorbody)
✓ Fetched elements
[PRE-FETCH] ✓ Mercury: Updated with e=0.20563593

⟳ Fetching osculating elements for 3I/ATLAS from JPL Horizons...
   Using Horizons ID: C/2025 N1 (smallbody)
✓ Fetched elements
[PRE-FETCH] ✓ 3I/ATLAS: Updated with e=6.139356
```

## Cache Key Strategy

**Important Decision:** What should cache keys use?

**Option A: Use display names** (Recommended)
```json
{
  "3I/ATLAS": {  ← Display name
    "elements": {...},
    "metadata": {
      "horizons_id": "C/2025 N1",  ← Store actual ID used
      "id_type": "smallbody"
    }
  }
}
```

**Advantages:**
- Human-readable cache
- Matches how user thinks about objects
- Easy to inspect/debug

**Option B: Use Horizons IDs**
```json
{
  "C/2025 N1": {  ← Horizons ID
    "elements": {...},
    "metadata": {
      "display_name": "3I/ATLAS"
    }
  }
}
```

**Advantages:**
- No duplicates if same object has multiple names
- Matches Horizons exactly

**Recommendation:** Use **Option A** (display names as keys) but store the Horizons ID in metadata. This way:
- Cache is human-readable
- We know what ID was actually used for the query
- Can debug ambiguity issues by checking metadata

## Files to Modify

1. **orbit_data_manager.py**
   - Add `query_horizons_elements(horizons_id, id_type, date_str)` function

2. **osculating_cache_manager.py**
   - Update `fetch_osculating_elements` signature
   - Update `get_elements_with_prompt` signature
   - Pass horizons_id and id_type through the chain
   - Store horizons_id in cache metadata

3. **palomas_orrery.py**
   - Update pre-fetch in `plot_objects()` (lines 3894-3900)
   - Update pre-fetch in `animate_objects()` (similar section)
   - Look up object dictionary to get ID and ID type

## Backward Compatibility

**Ensure graceful fallback:**
```python
def get_elements_with_prompt(obj_name, horizons_id=None, id_type='smallbody', parent_window=None):
    # If no horizons_id provided, use obj_name (backward compatible)
    query_id = horizons_id if horizons_id else obj_name
```

This way:
- New code passes proper IDs ✓
- Old code still works (falls back to name) ✓
- Gradual migration possible ✓

## Summary

**Current Problem:** Passing object names to Horizons instead of proper IDs, causing ambiguity

**Root Cause:** Osculating element queries don't use the same ID system as orbital path queries

**Solution:** Pass both display name (for caching/UI) and Horizons ID (for querying) through the entire chain

**Result:** Unambiguous queries, consistent with orbital paths system, future-proof

---

*"When you query Horizons, speak its language."* - Use proper IDs, not display names
