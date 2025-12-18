"""
osculating_cache_manager.py

Auto-updating cache for osculating orbital elements from JPL Horizons.
Uses two-generation backup protection and always-prompt user workflow.

Design Philosophy:
- Visibility over automation ("Otherwise it's a third party program")
- User control (always prompt with info, user decides)
- Backup protection (two-generation persistent backups)
- Keep everything forever (no cleanup, no deletion)

Part of Paloma's Orrery - Tony's astronomical visualization suite.
Created: November 18, 2025
"""

import json
import shutil
from datetime import datetime, timedelta
from pathlib import Path
import tkinter.messagebox as messagebox
# Correct import:
# from orbit_data_manager import query_horizons_elements
# Import fallback manual dictionary
try:
    from orbital_elements import planetary_params as FALLBACK_ELEMENTS
except ImportError:
    print("Warning: Could not import orbital_elements - fallback unavailable")
    FALLBACK_ELEMENTS = {}


def get_cache_key(obj_name, center_body=None):
    """
    Generate cache key for an object, optionally with center body suffix.
    
    This enables storing different osculating elements for the same object
    relative to different centers (e.g., heliocentric vs barycentric).
    
    Parameters:
        obj_name (str): Display name of object (e.g., 'Pluto', 'Charon')
        center_body (str, optional): Center body ID (e.g., '@9', '@sun', '9', 'sun')
    
    Returns:
        str: Cache key
    
    Examples:
        get_cache_key('Pluto')           -> 'Pluto'       (heliocentric default)
        get_cache_key('Pluto', '@sun')   -> 'Pluto'       (explicit heliocentric)
        get_cache_key('Pluto', '@9')     -> 'Pluto@9'     (barycentric)
        get_cache_key('Charon', '@9')    -> 'Charon@9'    (barycentric)
        get_cache_key('Charon', '@999')  -> 'Charon@999'  (Pluto body-centered)
    """
    # Heliocentric is the default - no suffix needed
    if center_body is None:
        return obj_name
    
    # Normalize: remove @ prefix if present
    center = center_body.lstrip('@').lower()
    
    # These all mean heliocentric - no suffix
    if center in ['sun', '0', '10', 'ssb']:  # SSB = Solar System Barycenter
        return obj_name
    
    # Non-heliocentric center - add suffix
    return f"{obj_name}@{center_body.lstrip('@')}"


# Cache file paths
CACHE_DIR = Path(__file__).parent / 'data'  # data/ subdirectory
CACHE_FILE = CACHE_DIR / 'osculating_cache.json'
BACKUP_FILE = CACHE_DIR / 'osculating_cache_backup.json'
BACKUP_OLD = CACHE_DIR / 'osculating_cache_backup_old.json'
TEMP_FILE = CACHE_DIR / 'osculating_cache.tmp'

# ============================================================================
# REFRESH INTERVALS - Hybrid Approach
# ============================================================================

REFRESH_INTERVALS = {
    # === PRIORITY 1: SPECIFIC OBJECTS ===
    # Fine control for critical objects
    'Mercury': 7,        # Relativistic precession, high eccentricity
    'Moon': 1,           # Complex 3-body Earth-Moon-Sun dynamics
    'C/2025 N1': 1,      # Active comet at perihelion
    '3I/ATLAS': 1,       # Interstellar visitor (limited observation window)
    
    # === PRIORITY 2: PATTERN MATCHING ===
    # Category-based defaults
    'pattern:C/': 1,     # All comets (C/ designation)
    'pattern:P/': 1,     # Periodic comets (P/ designation)
    'pattern:I/': 1,     # Interstellar objects (I/ designation)
    'pattern:2025': 7,   # Recent discoveries 2025 (might be NEOs)
    'pattern:2024': 7,   # Recent discoveries 2024
    
    # === PRIORITY 3: OBJECT TYPE ===
    # Coarse fallback by type (from idealized_orbits.py)
    'type:satellite': 7,       # Moons/satellites
    'type:orbital': 7,         # Asteroids, general orbits
    'type:trajectory': 30,     # Spacecraft (stable trajectories)
    'type:lagrange_point': 90, # Very stable points
    
    # === PRIORITY 4: DEFAULT ===
    'default': 30  # Monthly for unknowns
}

def get_refresh_interval(obj_name):
    """
    Get recommended refresh interval for object (in days).
    
    Precedence hierarchy:
    1. Specific object name (highest priority)
    2. Pattern matching
    3. Object type
    4. Default (lowest priority)
    
    Parameters:
        obj_name (str): Name of object
    
    Returns:
        int: Refresh interval in days
    """
    
    # Priority 1: Specific object
    if obj_name in REFRESH_INTERVALS:
        return REFRESH_INTERVALS[obj_name]
    
    # Priority 2: Pattern matching
    for key, interval in REFRESH_INTERVALS.items():
        if key.startswith('pattern:'):
            pattern = key.replace('pattern:', '')
            if pattern in obj_name:
                return interval
    
    # Priority 3: Object type (from idealized_orbits.py)
    if obj_name in FALLBACK_ELEMENTS:
        obj_type = FALLBACK_ELEMENTS[obj_name].get('object_type')
        if obj_type:
            type_key = f'type:{obj_type}'
            if type_key in REFRESH_INTERVALS:
                return REFRESH_INTERVALS[type_key]
    
    # Priority 4: Default
    return REFRESH_INTERVALS['default']

# ============================================================================
# TWO-GENERATION BACKUP SYSTEM
# ============================================================================

def save_cache(cache):
    """
    Save cache with two-generation backup protection.
    
    File structure:
        osculating_cache.json          - Current
        osculating_cache_backup.json   - Last good (one save ago)
        osculating_cache_backup_old.json - Previous good (two saves ago)
    
    Process:
        1. Write to temp file
        2. Validate temp file
        3. Rotate: backup → backup_old
        4. Copy: current → backup
        5. Move: temp → current
    
    Recovery:
        - If current corrupted → use backup
        - If backup corrupted → use backup_old
    
    Parameters:
        cache (dict): Cache data to save
    
    Raises:
        Exception: If save fails (after attempting recovery)
    """
    try:
        # Step 1: Write to temp file
        with open(TEMP_FILE, 'w') as f:
            json.dump(cache, f, indent=2)
        
        # Step 2: Validate temp file
        with open(TEMP_FILE, 'r') as f:
            json.load(f)  # Will raise exception if invalid JSON
        
        # Step 3: Rotate backups: backup → backup_old
        if BACKUP_FILE.exists():
            if BACKUP_OLD.exists():
                BACKUP_OLD.unlink()  # Remove oldest backup
            shutil.copy2(BACKUP_FILE, BACKUP_OLD)
            print(f"  Rotated: {BACKUP_FILE.name} → {BACKUP_OLD.name}")
        
        # Step 4: Current → backup
        if CACHE_FILE.exists():
            shutil.copy2(CACHE_FILE, BACKUP_FILE)
            print(f"  Backed up: {CACHE_FILE.name} → {BACKUP_FILE.name}")
        
        # Step 5: Temp → current (atomic on most systems)
        TEMP_FILE.replace(CACHE_FILE)
        print(f"✓ Saved: {CACHE_FILE.name} (2-gen protected)")
        
    except Exception as e:
        print(f"✗ Save failed: {e}")
        
        # Clean up temp file
        if TEMP_FILE.exists():
            TEMP_FILE.unlink()
        
        # Attempt recovery from backup hierarchy
        if not CACHE_FILE.exists():
            if BACKUP_FILE.exists():
                shutil.copy2(BACKUP_FILE, CACHE_FILE)
                print(f"✓ Recovered from {BACKUP_FILE.name}")
            elif BACKUP_OLD.exists():
                shutil.copy2(BACKUP_OLD, CACHE_FILE)
                print(f"✓ Recovered from {BACKUP_OLD.name}")
        
        raise

def load_cache():
    """
    Load cache with two-generation recovery.
    
    Tries:
        1. Main file
        2. Backup file
        3. Old backup file
        4. Returns empty structure if all fail
    
    Returns:
        dict: Cache data or empty cache structure
    """
    
    # Try main file
    if CACHE_FILE.exists():
        try:
            with open(CACHE_FILE, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"⚠ Main cache corrupted: {e}")
    
    # Try backup
    if BACKUP_FILE.exists():
        try:
            with open(BACKUP_FILE, 'r') as f:
                cache = json.load(f)
            print(f"✓ Recovered from {BACKUP_FILE.name}")
            
            # Restore to main file
            shutil.copy2(BACKUP_FILE, CACHE_FILE)
            return cache
        except Exception as e:
            print(f"⚠ Backup also corrupted: {e}")
    
    # Try old backup
    if BACKUP_OLD.exists():
        try:
            with open(BACKUP_OLD, 'r') as f:
                cache = json.load(f)
            print(f"✓ Recovered from {BACKUP_OLD.name}")
            
            # Restore to main file
            shutil.copy2(BACKUP_OLD, CACHE_FILE)
            return cache
        except Exception as e:
            print(f"✗ All backups corrupted: {e}")
    
    # All failed - return empty cache
    print("⚠ No valid cache found - starting fresh")
    return create_empty_cache()

def create_empty_cache():
    """Create empty cache structure with metadata."""
    return {
        '_metadata': {
            'cache_version': '1.0',
            'created': datetime.now().isoformat(),
            'description': 'Auto-updated cache of osculating orbital elements from JPL Horizons',
            'note': 'Elements can be copied to idealized_orbits.py for manual backup'
        }
    }

# ============================================================================
# CACHE STATUS AND AGE CHECKING
# ============================================================================

def calculate_age_days(cache_entry):
    """
    Calculate age of cache entry in days.
    
    Parameters:
        cache_entry (dict): Cache entry with metadata
    
    Returns:
        int: Age in days, or None if can't determine
    """
    try:
        fetched_str = cache_entry['metadata']['fetched']
        fetched = datetime.fromisoformat(fetched_str)
        age = (datetime.now() - fetched).total_seconds() / 86400
        return int(age)
    except:
        return None

#def check_cache_status(obj_name):
def check_cache_status(obj_name, center_body=None):
    """
    Check cache status for an object.
    
    Parameters:
        obj_name (str): Name of object
    
    Returns:
        dict: Status information with keys:
            - exists (bool)
            - age_days (int or None)
            - recommended_days (int)
            - is_fresh (bool)
            - status_text (str): "✓ Fresh" or "⚠ Update recommended" or "Not in cache"
    """

    cache = load_cache()

    cache_key = get_cache_key(obj_name, center_body)
    
    recommended_days = get_refresh_interval(obj_name)
    
    if cache_key not in cache or cache_key.startswith('_'):

        return {
            'exists': False,
            'age_days': None,
            'recommended_days': recommended_days,
            'is_fresh': False,
            'status_text': 'Not in cache'
        }
    
#    age_days = calculate_age_days(cache[obj_name])
    age_days = calculate_age_days(cache[cache_key])
    
    if age_days is None:
        return {
            'exists': True,
            'age_days': None,
            'recommended_days': recommended_days,
            'is_fresh': False,
            'status_text': 'Unknown age'
        }
    
    is_fresh = age_days < recommended_days
    status_text = "✓ Fresh" if is_fresh else "⚠ Update recommended"
    
    return {
        'exists': True,
        'age_days': age_days,
        'recommended_days': recommended_days,
        'is_fresh': is_fresh,
        'status_text': status_text
    }

# ============================================================================
# FETCHING FROM JPL HORIZONS
# ============================================================================

#def fetch_osculating_elements(obj_name, horizons_id=None, id_type='smallbody', date=None):
def fetch_osculating_elements(obj_name, horizons_id=None, id_type='smallbody', date=None, center_body=None):
    """
    Fetch osculating elements from JPL Horizons.
    
    Parameters:
        obj_name (str): Display name of object (used for metadata and messages)
        horizons_id (str, optional): Horizons ID to query (defaults to obj_name)
                                     Examples: 'C/2025 N1', '199', '-23'
        id_type (str): Horizons ID type - 'smallbody', 'majorbody', 'id', etc.
                       Default: 'smallbody'
        date (datetime, optional): Date for osculating elements (default: today)
        center_body (str, optional): Override center body (e.g., '@9' for Pluto barycenter)
                                     If None, auto-detects based on object ID.
    
    Returns:
        dict: Cache entry with elements and metadata, or None if fetch fails
        
    Notes:
        - obj_name is used for display and metadata (e.g., '3I/ATLAS')
        - horizons_id is passed to JPL Horizons query (e.g., 'C/2025 N1')
        - The actual Horizons ID used is stored in metadata['horizons_id']
        - center_body enables fetching barycentric elements for binary systems
    """
    if date is None:
        date = datetime.now()
    
    date_str = date.strftime('%Y-%m-%d')
    
    # Determine which ID to use for querying
    query_id = horizons_id if horizons_id else obj_name
    
    try:
        # Import here to avoid circular dependency
        from orbit_data_manager import query_horizons_elements
        
        print(f"⟳ Fetching osculating elements for {obj_name} from JPL Horizons...", flush=True)
        if horizons_id and horizons_id != obj_name:
            print(f"   Using Horizons ID: {query_id} (id_type: {id_type})", flush=True)
        
        # Query JPL Horizons using proper ID and type
    #    result = query_horizons_elements(query_id, id_type, date_str)
        result = query_horizons_elements(query_id, id_type, date_str, center_body=center_body)
        
        # Package the result
        cache_entry = {
            'elements': {
                'a': result['a'],
                'e': result['e'],
                'i': result['i'],
                'omega': result['omega'],
                'Omega': result['Omega'],
                'epoch': f"{date_str} osc.",
                'TP': result.get('TP'),
                'MA': result.get('MA'),      # Mean anomaly at epoch (degrees)
                'TA': result.get('TA'),      # True anomaly at epoch (degrees)
            },

            'metadata': {
                'fetched': datetime.now().isoformat(),
                'source': 'JPL Horizons',
                'solution_date': result.get('solution_date', date_str),
                'horizons_id': query_id,  # Store the actual ID we queried with
                'display_name': obj_name,  # Store the display name separately
                'refresh_interval_days': get_refresh_interval(obj_name),
                'center_body': result.get('center_body', '@sun'),  # Store which center was used
            }

        }
        
        # Add optional metadata if available
        if 'observations' in result:
            cache_entry['metadata']['observations'] = result['observations']
        if 'arc_days' in result:
            cache_entry['metadata']['arc_days'] = result['arc_days']
        
        print(f"✓ Fetched elements (solution date: {cache_entry['metadata']['solution_date']})", flush=True)
        return cache_entry
        
    except Exception as e:
        print(f"✗ Failed to fetch elements for {obj_name}: {e}")
        return None

# ============================================================================
# USER DIALOG AND PROMPTING
# ============================================================================

def format_age_string(age_days):
    """
    Format age in human-readable string.
    
    Parameters:
        age_days (int): Age in days
    
    Returns:
        str: Formatted string like "2 days ago" or "3 weeks ago"
    """
    if age_days is None:
        return "Unknown"
    elif age_days == 0:
        return "Today"
    elif age_days == 1:
        return "1 day ago"
    elif age_days < 7:
        return f"{age_days} days ago"
    elif age_days < 30:
        weeks = age_days // 7
        return f"{weeks} week{'s' if weeks > 1 else ''} ago"
    elif age_days < 365:
        months = age_days // 30
        return f"{months} month{'s' if months > 1 else ''} ago"
    else:
        years = age_days // 365
        return f"{years} year{'s' if years > 1 else ''} ago"

def format_interval_string(interval_days):
    """
    Format refresh interval in human-readable string.
    
    Parameters:
        interval_days (int): Interval in days
    
    Returns:
        str: Formatted string like "Daily (1 day)" or "Weekly (7 days)"
    """
    if interval_days == 1:
        return "Daily (1 day)"
    elif interval_days == 7:
        return "Weekly (7 days)"
    elif interval_days == 30:
        return "Monthly (30 days)"
    elif interval_days == 90:
        return "Quarterly (90 days)"
    else:
        return f"Every {interval_days} days"

# def get_elements_with_prompt(obj_name, horizons_id=None, id_type='smallbody', plot_date=None, parent_window=None):   
def get_elements_with_prompt(obj_name, horizons_id=None, id_type='smallbody', plot_date=None, parent_window=None, center_body=None):
    """
    Get orbital elements with user prompt - ALWAYS prompts with information.
    
    This is the main user-facing function. It ALWAYS shows a dialog with:
    - Age of cached elements (if available)
    - Recommended refresh frequency
    - Status (fresh or needs update)
    
    User decides whether to update based on visible information.
    
    Philosophy: "System provides information, user makes decision"
    (Not: "System decides for you based on hidden threshold")
    
    Parameters:
        obj_name (str): Display name of object (used for caching and UI)
        horizons_id (str, optional): Horizons ID to query (defaults to obj_name)
                                     Examples: 'C/2025 N1', '199', '-23'
        id_type (str): Horizons ID type - 'smallbody', 'majorbody', 'id', etc.
                       Default: 'smallbody'
        parent_window (tk.Tk, optional): Parent window for dialog
    
    Returns:
        dict: Orbital elements (from cache, fresh fetch, or fallback)
    
    Raises:
        ValueError: If no elements available anywhere
        
    Notes:
        - obj_name is used for cache keys and display (e.g., '3I/ATLAS')
        - horizons_id is used for JPL Horizons queries (e.g., 'C/2025 N1')
        - This separation prevents ambiguous queries to Horizons
    """
    
    # Check cache status
#    status = check_cache_status(obj_name)
    
    # Check cache status (center-body aware)
    cache_key = get_cache_key(obj_name, center_body)
    status = check_cache_status(obj_name, center_body)

    # Build dialog message
    if status['exists']:
        age_str = format_age_string(status['age_days'])
        dialog_msg = f"{obj_name} orbital elements:\n"
        dialog_msg += f"  Last updated: {age_str}\n"
        dialog_msg += f"  Recommended frequency: {format_interval_string(status['recommended_days'])}\n"
        dialog_msg += f"  Status: {status['status_text']}\n\n"
        
        if status['is_fresh']:
            dialog_msg += "Update anyway?"
        else:
            dialog_msg += "Update from JPL Horizons?"
    else:
        dialog_msg = f"{obj_name} orbital elements:\n"
        dialog_msg += f"  Status: Not in cache\n"
        dialog_msg += f"  Recommended frequency: {format_interval_string(status['recommended_days'])}\n\n"
        dialog_msg += "Fetch from JPL Horizons?\n"
        dialog_msg += "(Will use manual dictionary if declined)"
    
    # Show modal dialog - user decides
    response = messagebox.askyesno(
        "Update Orbital Elements?",
        dialog_msg,
        parent=parent_window
    )
    
    if response:  # User clicked YES
        print(f"User chose to update {obj_name}")
        
        # Debug: Show what ID we're actually querying
        query_id = horizons_id if horizons_id else obj_name
        if horizons_id and horizons_id != obj_name:
            print(f"  Using Horizons ID: {query_id} (id_type: {id_type})", flush=True)

        # Fetch fresh elements

        # Pass horizons_id for query, but obj_name for metadata/display
#        fresh_entry = fetch_osculating_elements(
#            obj_name, 
#            horizons_id=horizons_id, 
#            id_type=id_type,
#            date=plot_date
#        )        
        
        fresh_entry = fetch_osculating_elements(
            obj_name, 
            horizons_id=horizons_id, 
            id_type=id_type,
            date=plot_date,
            center_body=center_body
        )

        if fresh_entry:
    #        # Update cache
    #        cache = load_cache()
    #        cache[obj_name] = fresh_entry
    #        save_cache(cache)

            # Update cache with center-aware key
            cache = load_cache()
            cache[cache_key] = fresh_entry
            save_cache(cache)

            return fresh_entry['elements']
        else:
            # Fetch failed - fall back
            print(f"⚠ Fetch failed - falling back to cached/manual elements")
            return get_fallback_elements(obj_name)
        
    else:  # User clicked NO
        print(f"User chose to use existing elements for {obj_name}")
        return get_fallback_elements(obj_name)

def get_fallback_elements(obj_name):
    """
    Get elements from cache or manual dictionary (fallback).
    
    Parameters:
        obj_name (str): Name of object
    
    Returns:
        dict: Orbital elements
    
    Raises:
        ValueError: If no elements available
    """
    # Try cache first
    cache = load_cache()
    if obj_name in cache and not obj_name.startswith('_'):
        age = calculate_age_days(cache[obj_name])
        age_str = format_age_string(age) if age else "unknown age"
        print(f"✓ Using cached elements ({age_str})")
        return cache[obj_name]['elements']
    
    # Try manual dictionary
    if obj_name in FALLBACK_ELEMENTS:
        print(f"⚠ Using manual dictionary backup for {obj_name}")
        return FALLBACK_ELEMENTS[obj_name]
    
    # Nothing available
    raise ValueError(
        f"No orbital elements available for {obj_name}\n"
        f"Not in cache, fetch failed, and not in manual dictionary.\n"
        f"Try adding to idealized_orbits.py or check network connection."
    )

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def format_for_python_dict(obj_name, elements):
    """
    Format elements as Python dictionary string for easy copying.
    
    Useful for copying cache entries to idealized_orbits.py manually.
    
    Parameters:
        obj_name (str): Name of object
        elements (dict): Orbital elements
    
    Returns:
        str: Formatted Python dictionary string
    """
    lines = [f"'{obj_name}': {{"]
    
    for key in ['a', 'e', 'i', 'omega', 'Omega', 'epoch', 'TP']:
        if key in elements:
            value = elements[key]
            if isinstance(value, str):
                lines.append(f"    '{key}': '{value}',")
            else:
                lines.append(f"    '{key}': {value},")
    
    lines.append("},")
    
    return "\n".join(lines)

# ============================================================================
# TESTING AND DEBUGGING
# ============================================================================

if __name__ == '__main__':
    """
    Test the cache manager with various scenarios.
    """
    print("=== Osculating Cache Manager Test ===\n")
    
    # Test 1: Load cache (or create if doesn't exist)
    print("Test 1: Loading cache...")
    cache = load_cache()
    print(f"  Cache loaded: {len([k for k in cache.keys() if not k.startswith('_')])} objects\n")
    
    # Test 2: Check status of a few objects
    print("Test 2: Checking cache status...")
    test_objects = ['Mercury', 'C/2025 N1', '3I/ATLAS', 'NonExistent']
    for obj in test_objects:
        status = check_cache_status(obj)
        print(f"  {obj}: {status['status_text']} (recommended: {status['recommended_days']}d)")
    print()
    
    # Test 3: Test refresh interval logic
    print("Test 3: Testing refresh interval hierarchy...")
    test_cases = [
        ('Mercury', 7, 'specific object'),
        ('C/2026 X1', 1, 'pattern: C/'),
        ('4I/Borisov', 1, 'pattern: I/'),
        ('Phobos', 7, 'type: satellite'),
        ('Random Object', 30, 'default'),
    ]
    for obj, expected, reason in test_cases:
        actual = get_refresh_interval(obj)
        status = "✓" if actual == expected else "✗"
        print(f"  {status} {obj}: {actual}d (expected {expected}d via {reason})")
    print()
    
    # Test 4: Test format functions
    print("Test 4: Testing formatting functions...")
    print(f"  0 days: {format_age_string(0)}")
    print(f"  1 day: {format_age_string(1)}")
    print(f"  5 days: {format_age_string(5)}")
    print(f"  14 days: {format_age_string(14)}")
    print(f"  45 days: {format_age_string(45)}")
    print(f"  400 days: {format_age_string(400)}")
    print()
    
    print("=== Tests Complete ===")
    print(f"\nCache file: {CACHE_FILE}")
    print(f"Backup: {BACKUP_FILE}")
    print(f"Backup old: {BACKUP_OLD}")
