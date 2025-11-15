# incremental_cache_manager.py
"""
Smart incremental cache manager for VizieR catalog data and SIMBAD properties.
Handles incremental fetching when query parameters change, avoiding redundant queries.
"""

import os
import json
import pickle
import time
import hashlib
from typing import Dict, Any, Optional, Tuple, List
from dataclasses import dataclass, asdict
import numpy as np
from astropy.table import Table, vstack
from astropy.io import votable
import logging

logger = logging.getLogger(__name__)


@dataclass
class CacheMetadata:
    """Metadata for cached catalog data."""
    
    catalog: str  # 'hipparcos', 'gaia', or 'simbad'
    mode: str  # 'distance' or 'magnitude'
    limit_value: float  # max distance in ly or magnitude limit
    
    # For distance mode
    min_parallax_mas: Optional[float] = None
    
    # Query metadata
    query_date: str = ""
    entry_count: int = 0
    file_version: str = "2.0"  # Version for compatibility checking
    
    # Data ranges actually present in the cache
    actual_min_distance: Optional[float] = None
    actual_max_distance: Optional[float] = None
    actual_min_magnitude: Optional[float] = None
    actual_max_magnitude: Optional[float] = None
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for JSON serialization."""
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'CacheMetadata':
        """Create from dictionary."""
        return cls(**data)
    
    def get_cache_key(self) -> str:
        """Generate unique key for this cache configuration."""
        key_parts = [self.catalog, self.mode, str(self.limit_value)]
        if self.min_parallax_mas:
            key_parts.append(str(self.min_parallax_mas))
        key_str = "_".join(key_parts)
        return hashlib.md5(key_str.encode()).hexdigest()[:8]


class IncrementalCacheManager:
    """Manages incremental caching for stellar catalog data."""
    
#    def __init__(self, cache_dir: str = "."):
    def __init__(self, cache_dir: str = "star_data"):
        """
        Initialize cache manager.
        
        Args:
            cache_dir: Directory for cache files
        """
        self.cache_dir = cache_dir
        self.metadata_suffix = "_metadata.json"
        
    def _get_metadata_filename(self, data_filename: str) -> str:
        """Get metadata filename for a data file."""
        base = os.path.splitext(data_filename)[0]
        return f"{base}{self.metadata_suffix}"
    
    def load_metadata(self, data_filename: str) -> Optional[CacheMetadata]:
        """Load metadata for a cached data file."""
        metadata_file = self._get_metadata_filename(data_filename)
        metadata_path = os.path.join(self.cache_dir, metadata_file)
        
        if not os.path.exists(metadata_path):
            return None
        
        try:
            with open(metadata_path, 'r') as f:
                data = json.load(f)
            return CacheMetadata.from_dict(data)
        except Exception as e:
            logger.warning(f"Could not load metadata from {metadata_path}: {e}")
            return None
    
    def save_metadata(self, data_filename: str, metadata: CacheMetadata):
        """Save metadata for a cached data file."""
        metadata_file = self._get_metadata_filename(data_filename)
        metadata_path = os.path.join(self.cache_dir, metadata_file)
        
        try:
            with open(metadata_path, 'w') as f:
                json.dump(metadata.to_dict(), f, indent=2)
            logger.info(f"Saved metadata to {metadata_path}")
        except Exception as e:
            logger.error(f"Could not save metadata to {metadata_path}: {e}")
    
    def analyze_data_ranges(self, data: Table, mode: str) -> Dict[str, float]:
        """Analyze actual data ranges in a table."""
        ranges = {}
        
        if mode == 'distance' and 'Distance_ly' in data.colnames:
            distances = data['Distance_ly']
            valid_distances = distances[np.isfinite(distances)]
            if len(valid_distances) > 0:
                ranges['actual_min_distance'] = float(np.min(valid_distances))
                ranges['actual_max_distance'] = float(np.max(valid_distances))
        
        if mode == 'magnitude':
            # Check various magnitude columns
            for mag_col in ['Vmag', 'Gmag', 'Estimated_Vmag']:
                if mag_col in data.colnames:
                    mags = data[mag_col]
                    valid_mags = mags[np.isfinite(mags)]
                    if len(valid_mags) > 0:
                        ranges['actual_min_magnitude'] = float(np.min(valid_mags))
                        ranges['actual_max_magnitude'] = float(np.max(valid_mags))
                        break
        
        return ranges
    
    def check_cache_validity(self, data_filename: str, mode: str, 
                           limit_value: float) -> Tuple[str, Optional[CacheMetadata]]:
        """
        Check if cached data is valid for current query parameters.
        
        Returns:
            (status, metadata) where status is one of:
            - 'exact': Cached data exactly matches requirements
            - 'subset': Cached data contains more than needed (can filter)
            - 'expand': Need to fetch additional data (incremental fetch)
            - 'invalid': Cache is incompatible, need full refetch
            - 'missing': No cache exists
        """
        # Check if cache file exists
        data_path = os.path.join(self.cache_dir, data_filename)
        if not os.path.exists(data_path):
            return 'missing', None
        
        # Load metadata
        metadata = self.load_metadata(data_filename)
        if metadata is None:
            logger.warning(f"Cache file {data_filename} exists but has no metadata")
            return 'invalid', None
        
        # Check compatibility
        if metadata.mode != mode:
            logger.info(f"Cache mode mismatch: {metadata.mode} vs {mode}")
            return 'invalid', None
        
        # Check limits based on mode
        if mode == 'distance':
            if metadata.limit_value == limit_value:
                return 'exact', metadata
            elif metadata.limit_value > limit_value:
                # Cache has more data than needed
                return 'subset', metadata
            else:
                # Need more data
                return 'expand', metadata
                
        elif mode == 'magnitude':
            if metadata.limit_value == limit_value:
                return 'exact', metadata
            elif metadata.limit_value > limit_value:
                # Cache has fainter stars than needed (can filter)
                return 'subset', metadata
            else:
                # Need fainter stars
                return 'expand', metadata
        
        return 'invalid', None
    
    def load_and_filter_cache(self, data_filename: str, metadata: CacheMetadata,
                             mode: str, limit_value: float) -> Optional[Table]:
        """
        Load cached data and filter to match current requirements.
        
        Args:
            data_filename: Name of cache file
            metadata: Cache metadata
            mode: 'distance' or 'magnitude'
            limit_value: Current limit value
            
        Returns:
            Filtered table or None if loading fails
        """
        data_path = os.path.join(self.cache_dir, data_filename)
        
        try:
            # Load cached data
            logger.info(f"Loading cached data from {data_filename}")
            data = Table.read(data_path, format='votable')
            
            # Filter if needed
            if mode == 'distance' and limit_value < metadata.limit_value:
                if 'Distance_ly' in data.colnames:
                    mask = data['Distance_ly'] <= limit_value
                    data = data[mask]
                    logger.info(f"Filtered to {len(data)} stars within {limit_value} ly")
                    
            elif mode == 'magnitude' and limit_value < metadata.limit_value:
                # Find appropriate magnitude column
                mag_col = None
                for col in ['Vmag', 'Gmag', 'Estimated_Vmag']:
                    if col in data.colnames:
                        mag_col = col
                        break
                
                if mag_col:
                    mask = data[mag_col] <= limit_value
                    data = data[mask]
                    logger.info(f"Filtered to {len(data)} stars brighter than {limit_value}")
            
            return data
            
        except Exception as e:
            logger.error(f"Error loading cache file {data_filename}: {e}")
            return None
    
    def calculate_incremental_query_params(self, mode: str, old_limit: float,
                                          new_limit: float) -> Dict[str, Any]:
        """
        Calculate query parameters for incremental fetch.
        
        Returns:
            Dictionary of query parameters for fetching only new data
        """
        if mode == 'distance':
            # For distance, we need stars between old_limit and new_limit
            # This translates to parallax between new_min and old_min
            old_min_parallax = (1 / (old_limit / 3.26156)) * 1000  # mas
            new_min_parallax = (1 / (new_limit / 3.26156)) * 1000  # mas
            
            return {
                'parallax_min': new_min_parallax,
                'parallax_max': old_min_parallax,
                'description': f"stars between {old_limit:.1f} and {new_limit:.1f} ly"
            }
            
        elif mode == 'magnitude':
            # For magnitude, we need stars between old_limit and new_limit
            return {
                'mag_min': old_limit,
                'mag_max': new_limit,
                'description': f"stars between magnitude {old_limit:.1f} and {new_limit:.1f}"
            }
        
        return {}
    
    def merge_tables(self, existing_data: Table, new_data: Table,
                    mode: str) -> Table:
        """
        Merge existing and new data tables, removing duplicates.
        
        Args:
            existing_data: Existing cached data
            new_data: Newly fetched data
            mode: 'distance' or 'magnitude'
            
        Returns:
            Merged table without duplicates
        """
        if new_data is None or len(new_data) == 0:
            return existing_data
        
        if existing_data is None or len(existing_data) == 0:
            return new_data
        
        try:
            # Combine tables
            combined = vstack([existing_data, new_data])
            
            # Remove duplicates based on unique identifier
            # Try different ID columns
            id_columns = ['HIP', 'Source', 'Gaia']
            
            for id_col in id_columns:
                if id_col in combined.colnames:
                    # Get unique IDs
                    unique_ids, unique_indices = np.unique(
                        combined[id_col], return_index=True
                    )
                    
                    # Keep only unique entries
                    combined = combined[unique_indices]
                    logger.info(f"Removed duplicates using {id_col}, "
                               f"{len(combined)} unique entries remain")
                    break
            
            return combined
            
        except Exception as e:
            logger.error(f"Error merging tables: {e}")
            # Return existing data as fallback
            return existing_data
    
    def save_data_with_metadata(self, data: Table, data_filename: str,
                               catalog: str, mode: str, limit_value: float,
                               min_parallax_mas: Optional[float] = None):
        """
        Save data table with associated metadata.
        
        Args:
            data: Table to save
            data_filename: Output filename
            catalog: Catalog name ('hipparcos', 'gaia')
            mode: Query mode ('distance', 'magnitude')
            limit_value: Query limit value
            min_parallax_mas: Minimum parallax for distance queries
        """
        data_path = os.path.join(self.cache_dir, data_filename)
        
        # Analyze data ranges
        ranges = self.analyze_data_ranges(data, mode)
        
        # Create metadata
        metadata = CacheMetadata(
            catalog=catalog,
            mode=mode,
            limit_value=limit_value,
            min_parallax_mas=min_parallax_mas,
            query_date=time.strftime("%Y-%m-%d %H:%M:%S"),
            entry_count=len(data),
            **ranges
        )
        
        # Save data
        try:
            data.write(data_path, format='votable', overwrite=True)
            logger.info(f"Saved {len(data)} entries to {data_filename}")
            
            # Save metadata
            self.save_metadata(data_filename, metadata)
            
        except Exception as e:
            logger.error(f"Error saving data to {data_filename}: {e}")


class SimbadCacheManager:
    """Manages caching for SIMBAD property queries."""
    
#    def __init__(self, cache_dir: str = "."):
    def __init__(self, cache_dir: str = "star_data"):
        """Initialize SIMBAD cache manager."""
        self.cache_dir = cache_dir
        self.cache_index_file = os.path.join(cache_dir, "simbad_cache_index.json")
        self.cache_index = self._load_cache_index()
    
    def _load_cache_index(self) -> Dict[str, Dict]:
        """Load the cache index that tracks all cached objects."""
        if os.path.exists(self.cache_index_file):
            try:
                with open(self.cache_index_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                logger.warning(f"Could not load cache index: {e}")
        return {}
    
    def _save_cache_index(self):
        """Save the cache index."""
        try:
            with open(self.cache_index_file, 'w') as f:
                json.dump(self.cache_index, f, indent=2)
        except Exception as e:
            logger.error(f"Could not save cache index: {e}")
    
    def get_cached_objects(self, object_ids: List[str]) -> Tuple[Dict, List[str]]:
        """
        Get cached SIMBAD properties for a list of objects.
        
        Returns:
            (cached_properties, missing_ids)
        """
        cached = {}
        missing = []
        
        for obj_id in object_ids:
            if obj_id in self.cache_index:
                # Check if cache is recent enough (e.g., less than 30 days old)
                cache_data = self.cache_index[obj_id]
                cache_time = cache_data.get('cache_time', 0)
                age_days = (time.time() - cache_time) / 86400
                
                if age_days < 30:  # Cache valid for 30 days
                    cached[obj_id] = cache_data.get('properties', {})
                else:
                    missing.append(obj_id)
                    logger.info(f"Cache for {obj_id} is {age_days:.1f} days old, refetching")
            else:
                missing.append(obj_id)
        
        logger.info(f"Found {len(cached)} cached objects, {len(missing)} missing")
        return cached, missing
    
    def update_cache(self, new_properties: Dict):
        """Update cache with newly fetched properties."""
        for obj_id, props in new_properties.items():
            self.cache_index[obj_id] = {
                'properties': props,
                'cache_time': time.time()
            }
        
        self._save_cache_index()
        logger.info(f"Updated cache with {len(new_properties)} objects")


# Integration functions for existing code


def smart_load_or_fetch_hipparcos(v, hip_data_file: str, mode: str,
                                  limit_value: float, **kwargs) -> Optional[Table]:
    """
    Smart loading/fetching for Hipparcos data with incremental caching.
    
    This replaces the existing load_or_fetch_hipparcos_data function.
    """
    from data_acquisition import load_or_fetch_hipparcos_data
    
    cache_mgr = IncrementalCacheManager()
    
    # ADD THIS BLOCK (before existing "Check cache status" line):
    # COMPREHENSIVE CACHE PROTECTION
    # If we have a large comprehensive cache, just filter it instead of fetching
    cache_path = os.path.join(cache_mgr.cache_dir, hip_data_file)
    if os.path.exists(cache_path):
        file_size = os.path.getsize(cache_path)
        
        # Check if this is a comprehensive cache (>1MB = likely complete)
        # Hipparcos has ~118,000 stars, comprehensive cache should be 100KB-1MB+
        if file_size > 1_000_000:  # >1MB
            # For magnitude mode with reasonable limits
            if mode == 'magnitude' and limit_value <= 10.0:
                logger.info(f"Using comprehensive Hipparcos magnitude cache (size: {file_size/1e6:.1f}MB)")
                try:
                    data = Table.read(cache_path, format='votable')
                    
                    # Filter to requested magnitude
                    if 'Vmag' in data.colnames:
                        mask = data['Vmag'] <= limit_value
                        filtered = data[mask]
                        logger.info(f"Filtered Hipparcos cache from {len(data)} to {len(filtered)} stars <= mag {limit_value}")
                        return filtered
                    else:
                        logger.warning("No Vmag column found in Hipparcos cache")
                        return data
                        
                except Exception as e:
                    logger.warning(f"Could not read Hipparcos cache, falling back to normal logic: {e}")
            
            # For distance mode with reasonable limits
            elif mode == 'distance' and limit_value <= 150:  # Within 150 light-years
                logger.info(f"Using comprehensive Hipparcos distance cache (size: {file_size/1e6:.1f}MB)")
                try:
                    data = Table.read(cache_path, format='votable')
                    
                    # Filter to requested distance
                    if 'Distance_ly' in data.colnames:
                        mask = data['Distance_ly'] <= limit_value
                        filtered = data[mask]
                        logger.info(f"Filtered Hipparcos cache from {len(data)} to {len(filtered)} stars <= {limit_value} ly")
                        return filtered
                    else:
                        logger.warning("No Distance_ly column found in Hipparcos cache")
                        return data
                        
                except Exception as e:
                    logger.warning(f"Could not read Hipparcos cache, falling back to normal logic: {e}")
    
    # Check cache status
    status, metadata = cache_mgr.check_cache_validity(hip_data_file, mode, limit_value)
   
    logger.info(f"Hipparcos cache status: {status}")
    
    if status == 'exact':
        # Perfect match, just load
        return cache_mgr.load_and_filter_cache(hip_data_file, metadata, mode, limit_value)
    
    elif status == 'subset':
        # Have more data than needed, filter it
        return cache_mgr.load_and_filter_cache(hip_data_file, metadata, mode, limit_value)
    
    elif status == 'expand':
        # Need to fetch additional data
        logger.info(f"Incremental fetch needed: {metadata.limit_value} -> {limit_value}")
        
        # Load existing data
        existing_data = Table.read(os.path.join(cache_mgr.cache_dir, hip_data_file),
                                  format='votable')
        
        # Calculate parameters for incremental fetch
        params = cache_mgr.calculate_incremental_query_params(
            mode, metadata.limit_value, limit_value
        )
        
        logger.info(f"Fetching {params['description']}")
        
        # Fetch only new data
        # This would need modification of the original fetch function
        # to accept min/max constraints
        # For now, we'll fall back to full fetch
        new_data = load_or_fetch_hipparcos_data(
            v, f"temp_{hip_data_file}", mode=mode,
            mag_limit=limit_value if mode == 'magnitude' else None,
            parallax_constraint=kwargs.get('parallax_constraint')
        )
        
        # Merge old and new data
        if new_data is not None:
            combined = cache_mgr.merge_tables(existing_data, new_data, mode)
            
            # Save merged data
            min_parallax = None
            if mode == 'distance':
                min_parallax = (1 / (limit_value / 3.26156)) * 1000
            
            cache_mgr.save_data_with_metadata(
                combined, hip_data_file, 'hipparcos', mode, 
                limit_value, min_parallax
            )
            
            return combined
        
        return existing_data
    
    else:  # 'missing' or 'invalid'
        # Need full fetch
        data = load_or_fetch_hipparcos_data(
            v, hip_data_file, mode=mode,
            mag_limit=limit_value if mode == 'magnitude' else None,
            parallax_constraint=kwargs.get('parallax_constraint')
        )
        
        if data is not None:
            # Save with metadata
            min_parallax = None
            if mode == 'distance':
                min_parallax = (1 / (limit_value / 3.26156)) * 1000
            
            cache_mgr.save_data_with_metadata(
                data, hip_data_file, 'hipparcos', mode,
                limit_value, min_parallax
            )
        
        return data


def smart_load_or_fetch_gaia(v, gaia_data_file: str, mode: str,
                             limit_value: float, **kwargs) -> Optional[Table]:
    """
    Smart loading/fetching for Gaia data with incremental caching.
    
    This replaces the existing load_or_fetch_gaia_data function.
    """
    from data_acquisition import load_or_fetch_gaia_data
    
    cache_mgr = IncrementalCacheManager()
        
    # COMPREHENSIVE CACHE PROTECTION
    # If we have a large comprehensive cache, just filter it instead of fetching
    cache_path = os.path.join(cache_mgr.cache_dir, gaia_data_file)
    if os.path.exists(cache_path):
        file_size = os.path.getsize(cache_path)
        
        # Check if this is a comprehensive cache
        # Gaia has millions of stars, comprehensive cache is >10MB
        if file_size > 10_000_000:  # >10MB
            # For magnitude mode with reasonable limits
            if mode == 'magnitude' and limit_value <= 9.0:
                logger.info(f"Using comprehensive Gaia magnitude cache (size: {file_size/1e6:.1f}MB)")
                try:
                    data = Table.read(cache_path, format='votable')
                    
                    # Filter to requested magnitude
                    mag_col = None
                    for col in ['Gmag', 'Estimated_Vmag']:
                        if col in data.colnames:
                            mag_col = col
                            break
                    
                    if mag_col:
                        mask = data[mag_col] <= limit_value
                        filtered = data[mask]
                        logger.info(f"Filtered Gaia cache from {len(data)} to {len(filtered)} stars <= mag {limit_value}")
                        return filtered
                    else:
                        logger.warning("No magnitude column found in Gaia cache")
                        return data
                        
                except Exception as e:
                    logger.warning(f"Could not read Gaia cache, falling back to normal logic: {e}")
            
            # For distance mode with reasonable limits
            elif mode == 'distance' and limit_value <= 150:  # Within 150 light-years
                logger.info(f"Using comprehensive Gaia distance cache (size: {file_size/1e6:.1f}MB)")
                try:
                    data = Table.read(cache_path, format='votable')
                    
                    # Filter to requested distance
                    if 'Distance_ly' in data.colnames:
                        mask = data['Distance_ly'] <= limit_value
                        filtered = data[mask]
                        logger.info(f"Filtered Gaia cache from {len(data)} to {len(filtered)} stars <= {limit_value} ly")
                        return filtered
                    else:
                        logger.warning("No Distance_ly column found in Gaia cache")
                        return data
                        
                except Exception as e:
                    logger.warning(f"Could not read Gaia cache, falling back to normal logic: {e}")

    # NORMAL CACHE LOGIC for all other cases
    # Check cache status
    status, metadata = cache_mgr.check_cache_validity(gaia_data_file, mode, limit_value)
    
    logger.info(f"Gaia cache status: {status}")
    
    if status == 'exact':
        # Perfect match, just load
        return cache_mgr.load_and_filter_cache(gaia_data_file, metadata, mode, limit_value)
    
    elif status == 'subset':
        # Have more data than needed, filter it
        return cache_mgr.load_and_filter_cache(gaia_data_file, metadata, mode, limit_value)
    
    elif status == 'expand':
        # For magnitude mode, avoid re-fetching if we have a good cache
        if mode == 'magnitude':
            logger.info(f"Avoiding Gaia magnitude mode expansion - using existing cache")
            if metadata:
                return cache_mgr.load_and_filter_cache(gaia_data_file, metadata, mode, limit_value)
        
        # For distance mode, continue with incremental fetch
        logger.info(f"Incremental fetch needed: {metadata.limit_value} -> {limit_value}")
        
        # Load existing data
        existing_data = Table.read(os.path.join(cache_mgr.cache_dir, gaia_data_file),
                                  format='votable')
        
        # Calculate parameters for incremental fetch
        params = cache_mgr.calculate_incremental_query_params(
            mode, metadata.limit_value, limit_value
        )
        
        logger.info(f"Fetching {params['description']}")
        
        # Fetch only new data
        # For now, fall back to full fetch (would need API modification)
        new_data = load_or_fetch_gaia_data(
            v, f"temp_{gaia_data_file}", mode=mode,
            mag_limit=limit_value if mode == 'magnitude' else None,
            parallax_constraint=kwargs.get('parallax_constraint')
        )
        
        # Merge old and new data
        if new_data is not None:
            combined = cache_mgr.merge_tables(existing_data, new_data, mode)
            
            # Save merged data
            min_parallax = None
            if mode == 'distance':
                min_parallax = (1 / (limit_value / 3.26156)) * 1000
            
            cache_mgr.save_data_with_metadata(
                combined, gaia_data_file, 'gaia', mode,
                limit_value, min_parallax
            )
            
            return combined
        
        return existing_data
    
    else:  # 'missing' or 'invalid'
        # Need full fetch
        data = load_or_fetch_gaia_data(
            v, gaia_data_file, mode=mode,
            mag_limit=limit_value if mode == 'magnitude' else None,
            parallax_constraint=kwargs.get('parallax_constraint')
        )
        
        if data is not None:
            # Save with metadata
            min_parallax = None
            if mode == 'distance':
                min_parallax = (1 / (limit_value / 3.26156)) * 1000
            
            cache_mgr.save_data_with_metadata(
                data, gaia_data_file, 'gaia', mode,
                limit_value, min_parallax
            )
        
        return data


"""
def smart_load_or_fetch_gaia(v, gaia_data_file: str, mode: str,
                             limit_value: float, **kwargs) -> Optional[Table]:

    from data_acquisition import load_or_fetch_gaia_data
    
    cache_mgr = IncrementalCacheManager()
    
    # Check cache status
    status, metadata = cache_mgr.check_cache_validity(gaia_data_file, mode, limit_value)
    
    logger.info(f"Gaia cache status: {status}")
    
    if status == 'exact':
        # Perfect match, just load
        return cache_mgr.load_and_filter_cache(gaia_data_file, metadata, mode, limit_value)
    
    elif status == 'subset':
        # Have more data than needed, filter it
        return cache_mgr.load_and_filter_cache(gaia_data_file, metadata, mode, limit_value)
    
    elif status == 'expand':
        # Need to fetch additional data
        logger.info(f"Incremental fetch needed: {metadata.limit_value} -> {limit_value}")
        
        # Load existing data
        existing_data = Table.read(os.path.join(cache_mgr.cache_dir, gaia_data_file),
                                  format='votable')
        
        # Calculate parameters for incremental fetch
        params = cache_mgr.calculate_incremental_query_params(
            mode, metadata.limit_value, limit_value
        )
        
        logger.info(f"Fetching {params['description']}")
        
        # Fetch only new data
        # For now, fall back to full fetch (would need API modification)
        new_data = load_or_fetch_gaia_data(
            v, f"temp_{gaia_data_file}", mode=mode,
            mag_limit=limit_value if mode == 'magnitude' else None,
            parallax_constraint=kwargs.get('parallax_constraint')
        )
        
        # Merge old and new data
        if new_data is not None:
            combined = cache_mgr.merge_tables(existing_data, new_data, mode)
            
            # Save merged data
            min_parallax = None
            if mode == 'distance':
                min_parallax = (1 / (limit_value / 3.26156)) * 1000
            
            cache_mgr.save_data_with_metadata(
                combined, gaia_data_file, 'gaia', mode,
                limit_value, min_parallax
            )
            
            return combined
        
        return existing_data
    
    else:  # 'missing' or 'invalid'
        # Need full fetch
        data = load_or_fetch_gaia_data(
            v, gaia_data_file, mode=mode,
            mag_limit=limit_value if mode == 'magnitude' else None,
            parallax_constraint=kwargs.get('parallax_constraint')
        )
        
        if data is not None:
            # Save with metadata
            min_parallax = None
            if mode == 'distance':
                min_parallax = (1 / (limit_value / 3.26156)) * 1000
            
            cache_mgr.save_data_with_metadata(
                data, gaia_data_file, 'gaia', mode,
                limit_value, min_parallax
            )
        
        return data
        """


# Example usage and testing
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    
    # Test cache manager
    cache_mgr = IncrementalCacheManager()
    
    # Simulate checking cache for different scenarios
    test_cases = [
        ("hipparcos_100ly.vot", "distance", 100.0),  # Original query
        ("hipparcos_100ly.vot", "distance", 105.0),  # Expansion
        ("hipparcos_100ly.vot", "distance", 95.0),   # Subset
        ("gaia_mag6.vot", "magnitude", 6.0),         # Original
        ("gaia_mag6.vot", "magnitude", 6.5),         # Expansion
        ("gaia_mag6.vot", "magnitude", 5.5),         # Subset
    ]
    
    print("\nCache Status Tests:")
    print("-" * 50)
    for filename, mode, limit in test_cases:
        status, metadata = cache_mgr.check_cache_validity(filename, mode, limit)
        print(f"{filename} ({mode}={limit}): {status}")
        if metadata:
            print(f"  Cached: {metadata.limit_value}, {metadata.entry_count} entries")
    
    # Test incremental query parameters
    print("\nIncremental Query Parameters:")
    print("-" * 50)
    params = cache_mgr.calculate_incremental_query_params("distance", 100.0, 105.0)
    print(f"Distance 100->105 ly: {params}")
    
    params = cache_mgr.calculate_incremental_query_params("magnitude", 6.0, 6.5)
    print(f"Magnitude 6.0->6.5: {params}")
