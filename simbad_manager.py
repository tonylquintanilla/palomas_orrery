# simbad_manager.py
"""
Enhanced SIMBAD Query Manager with configurable rate limiting and retry logic.
This module replaces simbad_test.py and provides robust SIMBAD querying capabilities.
"""

import os
import time
import pickle
import logging
from dataclasses import dataclass, field
from typing import Optional, Dict, List, Tuple, Any
from astroquery.simbad import Simbad
import numpy as np
import pandas as pd
import shutil
import re
from vot_cache_manager import VOTCacheManager, integrate_vot_protection_with_simbad_manager, verify_vot_cache_integrity

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class SimbadConfig:
    """Configuration for SIMBAD queries with user-adjustable parameters."""
    
    # Rate limiting parameters
    queries_per_second: float = 5.0  # Default 5 queries/second (200ms between queries)
    batch_size: int = 50
    
    # Timeout and retry parameters
    timeout: int = 300  # 5 minutes
    max_retries: int = 3
    retry_delay: float = 1.0  # Base delay for exponential backoff
    
    # Query configuration
    row_limit: int = 1
    votable_fields: List[str] = field(default_factory=lambda: ['ids', 'sp', 'flux(V)', 'flux(B)', 'otype'])
    
    # Progress saving
    save_progress_interval: int = 10  # Save after every N queries
    
    # User preferences
    show_detailed_progress: bool = True
    pause_on_error: bool = False
    
    @classmethod
    def from_dict(cls, config_dict: Dict[str, Any]) -> 'SimbadConfig':
        """Create config from dictionary (e.g., from GUI)."""
        return cls(**{k: v for k, v in config_dict.items() if k in cls.__annotations__})
    
    @classmethod
    def load_from_file(cls, filepath: str = 'simbad_config.pkl') -> 'SimbadConfig':
        """Load saved configuration from file."""
        if os.path.exists(filepath):
            try:
                with open(filepath, 'rb') as f:
                    config_dict = pickle.load(f)
                return cls.from_dict(config_dict)
            except Exception as e:
                logger.warning(f"Could not load config from {filepath}: {e}")
        return cls()  # Return default config
    
    def save_to_file(self, filepath: str = 'simbad_config.pkl'):
        """Save configuration to file."""
        config_dict = {
            k: getattr(self, k) for k in self.__annotations__
        }
        with open(filepath, 'wb') as f:
            pickle.dump(config_dict, f)


class RateLimiter:
    """Token bucket rate limiter for SIMBAD queries."""
    
    def __init__(self, queries_per_second: float = 5.0):
        """Initialize rate limiter with specified queries per second."""
        self.max_tokens = queries_per_second
        self.tokens = self.max_tokens
        self.refill_rate = queries_per_second
        self.last_refill = time.time()
        self.total_wait_time = 0
        self.query_count = 0
    
    def wait_if_needed(self) -> float:
        """Wait if necessary and return wait time in seconds."""
        now = time.time()
        
        # Refill tokens based on elapsed time
        elapsed = now - self.last_refill
        self.tokens = min(self.max_tokens, self.tokens + elapsed * self.refill_rate)
        self.last_refill = now
        
        # Check if we need to wait for a token
        if self.tokens < 1:
            wait_time = (1 - self.tokens) / self.refill_rate
            time.sleep(wait_time)
            self.tokens = 0
            self.total_wait_time += wait_time
            return wait_time
        
        # Consume a token
        self.tokens -= 1
        self.query_count += 1
        return 0
    
    def get_stats(self) -> Dict[str, float]:
        """Get rate limiter statistics."""
        elapsed = time.time() - (self.last_refill - self.total_wait_time)
        actual_rate = self.query_count / elapsed if elapsed > 0 else 0
        
        return {
            'queries_made': self.query_count,
            'total_wait_time': self.total_wait_time,
            'actual_rate': actual_rate,
            'target_rate': self.refill_rate,
            'tokens_available': self.tokens
        }


class QueryStats:
    """Track statistics for SIMBAD queries."""
    
    def __init__(self):
        self.start_time = time.time()
        self.successful = 0
        self.failed = 0
        self.retried = 0
        self.cached = 0
        self.total_time = 0
        self.error_log = []
    
    def log_success(self):
        self.successful += 1
    
    def log_failure(self, obj_name: str, error: str):
        self.failed += 1
        self.error_log.append((obj_name, error, time.time()))
    
    def log_retry(self):
        self.retried += 1
    
    def log_cached(self):
        self.cached += 1
    
    def get_summary(self) -> str:
        """Get a summary of query statistics."""
        elapsed = time.time() - self.start_time
        total = self.successful + self.failed
        
        if total == 0:
            return "No queries performed yet."
        
        success_rate = (self.successful / total) * 100 if total > 0 else 0
        queries_per_second = total / elapsed if elapsed > 0 else 0
        
        summary = f"""
Query Statistics:
-----------------
Total Queries: {total}
Successful: {self.successful} ({success_rate:.1f}%)
Failed: {self.failed}
Cached: {self.cached}
Retried: {self.retried}
Time Elapsed: {elapsed:.1f}s
Query Rate: {queries_per_second:.2f}/s
"""
        return summary


class SimbadQueryManager:
    """Main class for managing SIMBAD queries with rate limiting and error handling."""
    
    def __init__(self, config: Optional[SimbadConfig] = None, 
                 progress_callback: Optional[callable] = None):
        """
        Initialize the SIMBAD Query Manager.
        
        Args:
            config: Configuration object for query parameters
            progress_callback: Optional callback function for progress updates
                              Should accept (current, total, message) parameters
        """
        self.config = config or SimbadConfig()
        self.progress_callback = progress_callback
        self.rate_limiter = RateLimiter(self.config.queries_per_second)
        self.stats = QueryStats()
        self.simbad = self._create_simbad_instance()

        # ADD THIS LINE - Initialize VOT cache manager
#        self.vot_manager = VOTCacheManager()
        self.vot_manager = VOTCacheManager(cache_dir='star_data')
        
        # ADD THIS LOG MESSAGE (optional)
        logger.info(f"VOT cache protection enabled")        
        
    def protect_all_caches(self):
        """
        Protect both PKL and VOT cache files.
        Creates timestamped backups of all critical cache files.
        """
        protected_files = []
        
        # Protect PKL files
        pkl_files = [
            'star_data/star_properties_distance.pkl',
            'star_data/star_properties_magnitude.pkl',
        ]
        
        for pkl_file in pkl_files:
            if os.path.exists(pkl_file):
                backup_name = pkl_file + '.protected_' + time.strftime('%Y%m%d_%H%M%S')
                try:
                    shutil.copy2(pkl_file, backup_name)
                    protected_files.append(backup_name)
                    logger.info(f"Protected PKL: {backup_name}")
                except Exception as e:
                    logger.error(f"Failed to protect {pkl_file}: {e}")
        
        # Protect VOT files using VOT manager
        vot_count = 0
        for vot_file in self.vot_manager.protected_files.keys():
            filepath = os.path.join(self.vot_manager.cache_dir, vot_file)
            if os.path.exists(filepath):
                if self.vot_manager.protect_base_file(filepath):
                    vot_count += 1
        
        logger.info(f"Protected {len(protected_files)} PKL files and {vot_count} VOT files")
        return protected_files
    
    def update_calculated_properties(self, combined_df, properties_file: str) -> Dict:
        """
        Update existing properties with calculated stellar parameters.
        This replaces the save_enhanced_pickle function.
        
        Args:
            combined_df: DataFrame with calculated properties (Temperature, Luminosity, etc.)
            properties_file: Path to the properties pickle file
            
        Returns:
            Updated properties dictionary
        """
        logger.info(f"Updating {properties_file} with calculated properties...")
        
        # Load existing properties using the standard method
        if os.path.exists(properties_file):
            with open(properties_file, 'rb') as f:
                data = pickle.load(f)
            
            # Convert to dictionary format if needed
            if isinstance(data, dict) and 'unique_ids' in data:
                # Old list format - convert to dictionary with safe list access
                existing_properties = {}
                
                # Get all lists with safe defaults
                unique_ids = data.get('unique_ids', [])
                star_names = data.get('star_names', [])
                spectral_types = data.get('spectral_types', [])
                v_magnitudes = data.get('V_magnitudes', [])
                b_magnitudes = data.get('B_magnitudes', [])
                object_types = data.get('object_types', [])
                is_messier_list = data.get('is_messier', [])
                distance_ly_list = data.get('distance_ly', [])
                distance_pc_list = data.get('distance_pc', [])
                temperature_list = data.get('Temperature', [])
                luminosity_list = data.get('Luminosity', [])
                abs_mag_list = data.get('Abs_Mag', [])
                ra_icrs_list = data.get('RA_ICRS', [])
                de_icrs_list = data.get('DE_ICRS', [])
                ra_str_list = data.get('ra_str', [])
                dec_str_list = data.get('dec_str', [])
                stellar_class_list = data.get('Stellar_Class', [])
                object_type_desc_list = data.get('Object_Type_Desc', [])
                source_catalog_list = data.get('Source_Catalog', [])
                
                # Process only valid entries
                for i, uid in enumerate(unique_ids):
                    if uid:
                        existing_properties[uid] = {
                            'star_name': star_names[i] if i < len(star_names) else None,
                            'spectral_type': spectral_types[i] if i < len(spectral_types) else None,
                            'V_magnitude': v_magnitudes[i] if i < len(v_magnitudes) else None,
                            'B_magnitude': b_magnitudes[i] if i < len(b_magnitudes) else None,
                            'object_type': object_types[i] if i < len(object_types) else None,
                            'is_messier': is_messier_list[i] if i < len(is_messier_list) else False,
                            'distance_ly': distance_ly_list[i] if i < len(distance_ly_list) else None,
                            'distance_pc': distance_pc_list[i] if i < len(distance_pc_list) else None,
                            'Temperature': temperature_list[i] if i < len(temperature_list) else None,
                            'Luminosity': luminosity_list[i] if i < len(luminosity_list) else None,
                            'Abs_Mag': abs_mag_list[i] if i < len(abs_mag_list) else None,
                            'RA_ICRS': ra_icrs_list[i] if i < len(ra_icrs_list) else None,
                            'DE_ICRS': de_icrs_list[i] if i < len(de_icrs_list) else None,
                            'ra_str': ra_str_list[i] if i < len(ra_str_list) else None,
                            'dec_str': dec_str_list[i] if i < len(dec_str_list) else None,
                            'Stellar_Class': stellar_class_list[i] if i < len(stellar_class_list) else None,
                            'Object_Type_Desc': object_type_desc_list[i] if i < len(object_type_desc_list) else None,
                            'Source_Catalog': source_catalog_list[i] if i < len(source_catalog_list) else None,
                        }
            elif isinstance(data, dict):
                existing_properties = data
            else:
                existing_properties = {}
        else:
            existing_properties = {}
        
        # Track statistics
        original_count = len(existing_properties)
        updated_count = 0
        new_count = 0
        
        # Update with calculated properties from DataFrame
        for _, row in combined_df.iterrows():
            # Generate unique ID
            uid = row.get('unique_id', None)
            if uid is None:
                if 'HIP' in row and pd.notna(row['HIP']):
                    uid = f"HIP {int(row['HIP'])}"
                elif 'Source' in row and pd.notna(row['Source']):
                    uid = f"Gaia DR3 {int(row['Source'])}"
                else:
                    ra = row.get('RA_ICRS', None)
                    dec = row.get('DE_ICRS', None)
                    if ra and dec:
                        uid = f"J{ra:.6f}{dec:+.6f}"
            
            if not uid:
                continue
            
            # Check if this is a new star or update
            if uid in existing_properties:
                updated_count += 1
                # Update only the calculated fields (preserve SIMBAD data)
                props = existing_properties[uid]
            else:
                new_count += 1
                # Create new entry
                props = {
                    'star_name': row.get('Star_Name', ''),
                    'spectral_type': row.get('Spectral_Type', None),
                    'V_magnitude': row.get('Apparent_Magnitude', row.get('V_mag', None)),
                    'B_magnitude': row.get('B_mag', None),
                    'object_type': row.get('Object_Type', None),
                    'is_messier': row.get('Is_Messier', False),
                }
                existing_properties[uid] = props
            
            # Update calculated properties (these come from stellar_parameters.py)
            calculated_fields = {
                'Temperature': row.get('Temperature', None),
                'Luminosity': row.get('Luminosity', None),
                'Abs_Mag': row.get('Abs_Mag', None),
                'distance_ly': row.get('Distance_ly', None),
                'distance_pc': row.get('Distance_pc', None),
                'RA_ICRS': row.get('RA_ICRS', None),
                'DE_ICRS': row.get('DE_ICRS', None),
                'ra_str': row.get('ra_str', None),
                'dec_str': row.get('dec_str', None),
                'Stellar_Class': row.get('Stellar_Class', None),
                'Object_Type_Desc': row.get('Object_Type_Desc', None),
                'Source_Catalog': row.get('Source_Catalog', None),
            }
            
            # Only update non-None calculated values
            for field, value in calculated_fields.items():
                if value is not None and (pd.notna(value) if hasattr(pd, 'notna') else True):
                    props[field] = value
        
        # Log statistics
        self.stats.cached = updated_count  # Reuse cached field for updates
        logger.info(f"Updated {updated_count} existing stars, added {new_count} new stars")
        logger.info(f"Total stars: {len(existing_properties)} (was {original_count})")
        
        # Save using the existing _save_properties method with safety checks
        self._save_properties_with_safety(existing_properties, properties_file)
        
        return existing_properties


    def _save_properties_with_safety(self, properties: Dict, filepath: str):
        """
        Enhanced save with safety checks similar to orbit_data_manager.
        """
        # Check if file exists and get its size
        original_size = 0
        original_count = 0
        if os.path.exists(filepath):
            original_size = os.path.getsize(filepath)
            try:
                with open(filepath, 'rb') as f:
                    old_data = pickle.load(f)
                if isinstance(old_data, dict) and 'unique_ids' in old_data:
                    original_count = len(old_data.get('unique_ids', []))
                elif isinstance(old_data, dict):
                    original_count = len(old_data)
            except:
                pass
        
        new_count = len(properties)
        
        # Safety check: Don't allow massive data loss
        if original_count > 100 and new_count < original_count * 0.1:
            # Create emergency backup
            emergency_backup = filepath + '.emergency_' + time.strftime('%Y%m%d_%H%M%S')
            shutil.copy2(filepath, emergency_backup)
            logger.error(f"SAFETY: Blocked save that would reduce {original_count} to {new_count} stars")
            logger.info(f"Emergency backup created: {emergency_backup}")
            raise ValueError(f"Refusing to save: would lose {original_count - new_count} stars")
        
        # Safety check: Suspicious size reduction
        if original_size > 1024 * 1024 and new_count < 20:
            emergency_backup = filepath + '.size_warning_' + time.strftime('%Y%m%d_%H%M%S')
            shutil.copy2(filepath, emergency_backup)
            logger.error(f"SAFETY: Large file ({original_size/1024/1024:.1f}MB) -> {new_count} entries")
            raise ValueError("Refusing to save: suspicious size reduction")
        
        # Use atomic save operation
        temp_file = filepath + '.tmp'
        backup_file = filepath + '.backup'
        
        try:
            # Convert to list format for compatibility (existing format)
            all_unique_ids = list(properties.keys())
            property_lists = {
                'unique_ids': all_unique_ids,
                'star_names': [],
                'spectral_types': [],
                'V_magnitudes': [],
                'B_magnitudes': [],
                'object_types': [],
                'is_messier': [],
                'distance_ly': [],
                'distance_pc': [],
                'notes': [],
                # Add calculated fields to the save format
                'Temperature': [],
                'Luminosity': [],
                'Abs_Mag': [],
                'RA_ICRS': [],
                'DE_ICRS': [],
                'ra_str': [],
                'dec_str': [],
                'Stellar_Class': [],
                'Object_Type_Desc': [],
                'Source_Catalog': [],
            }
            
            for uid in all_unique_ids:
                props = properties[uid]
                property_lists['star_names'].append(props.get('star_name'))
                property_lists['spectral_types'].append(props.get('spectral_type'))
                property_lists['V_magnitudes'].append(props.get('V_magnitude'))
                property_lists['B_magnitudes'].append(props.get('B_magnitude'))
                property_lists['object_types'].append(props.get('object_type'))
                property_lists['is_messier'].append(props.get('is_messier', False))
                property_lists['distance_ly'].append(props.get('distance_ly'))
                property_lists['distance_pc'].append(props.get('distance_pc'))
                property_lists['notes'].append(props.get('notes', ''))
                # Add calculated fields
                property_lists['Temperature'].append(props.get('Temperature'))
                property_lists['Luminosity'].append(props.get('Luminosity'))
                property_lists['Abs_Mag'].append(props.get('Abs_Mag'))
                property_lists['RA_ICRS'].append(props.get('RA_ICRS'))
                property_lists['DE_ICRS'].append(props.get('DE_ICRS'))
                property_lists['ra_str'].append(props.get('ra_str'))
                property_lists['dec_str'].append(props.get('dec_str'))
                property_lists['Stellar_Class'].append(props.get('Stellar_Class'))
                property_lists['Object_Type_Desc'].append(props.get('Object_Type_Desc'))
                property_lists['Source_Catalog'].append(props.get('Source_Catalog'))
            
            # Write to temp file
            with open(temp_file, 'wb') as f:
                pickle.dump(property_lists, f)
            
            # Verify temp file
            with open(temp_file, 'rb') as f:
                verify_data = pickle.load(f)
                if len(verify_data.get('unique_ids', [])) != len(all_unique_ids):
                    raise ValueError("Verification failed")
            
            # Backup original if it exists
            if os.path.exists(filepath):
                if os.path.exists(backup_file):
                    os.remove(backup_file)
                shutil.move(filepath, backup_file)
            
            # Move temp to final
            shutil.move(temp_file, filepath)
            
            # Clean up backup if successful
            if os.path.exists(backup_file):
                os.remove(backup_file)
            
            logger.info(f"Saved {len(properties)} properties to {filepath}")
            
        except Exception as e:
            logger.error(f"Error saving properties: {e}")
            # Restore from backup if available
            if os.path.exists(backup_file):
                shutil.copy2(backup_file, filepath)
                logger.info("Restored from backup after save failure")
            # Clean up temp file
            if os.path.exists(temp_file):
                try:
                    os.remove(temp_file)
                except:
                    pass
            raise

    def rebuild_pkl_from_vot_caches(self, mode='distance', force_rebuild=False):
        """
        Rebuild PKL properties file from VOT caches and SIMBAD.
        
        Args:
            mode: 'distance' or 'magnitude'
            force_rebuild: If True, rebuild even if PKL exists
            
        Returns:
            Dictionary of star properties
        """
        if mode == 'distance':
            properties_file = 'star_data/star_properties_distance.pkl'
            vot_files = {
                'hipparcos': 'hipparcos_data_distance.vot',
                'gaia': 'gaia_data_distance.vot'
            }
        else:  # magnitude
            properties_file = 'star_data/star_properties_magnitude.pkl'
            vot_files = {
                'hipparcos': 'hipparcos_data_magnitude.vot',
                'gaia': 'gaia_data_magnitude.vot'
            }
        
        # Check if rebuild is needed
        if not force_rebuild and os.path.exists(properties_file):
            logger.info(f"{properties_file} already exists. Use force_rebuild=True to rebuild.")
            return self.load_existing_properties(properties_file)
        
        logger.info(f"Rebuilding {properties_file} from VOT caches...")
        
        # Step 1: Extract unique IDs from VOT files
        all_unique_ids = set()
        catalog_data = {}
        
        for catalog, vot_file in vot_files.items():
            if not os.path.exists(vot_file):
                logger.warning(f"VOT file not found: {vot_file}")
                continue
            
            table = self.vot_manager.safe_load_vot(vot_file)
            if table is None:
                continue
            
            logger.info(f"Processing {len(table)} entries from {catalog}")
            catalog_data[catalog] = table
            
            # Extract identifiers
            if 'hipparcos' in catalog.lower():
                for row in table:
                    if 'HIP' in row.colnames:
                        all_unique_ids.add(f"HIP {row['HIP']}")
            elif 'gaia' in catalog.lower():
                for row in table:
                    if 'Source' in row.colnames:
                        all_unique_ids.add(f"Gaia DR3 {row['Source']}")
        
        if not all_unique_ids:
            logger.error("No star IDs found in VOT files")
            return {}
        
        logger.info(f"Found {len(all_unique_ids)} unique star IDs from VOT files")
        
        # Step 2: Check existing PKL for any cached SIMBAD data
        existing_properties = {}
        if os.path.exists(properties_file):
            try:
                existing_properties = self.load_existing_properties(properties_file)
                logger.info(f"Loaded {len(existing_properties)} existing properties")
            except Exception as e:
                logger.warning(f"Could not load existing properties: {e}")
        
        # Step 3: Query SIMBAD for missing properties
        missing_ids = list(all_unique_ids - set(existing_properties.keys()))
        
        if missing_ids:
            logger.info(f"Querying SIMBAD for {len(missing_ids)} missing star properties...")
            
            # Query in batches with rate limiting
            batch_size = self.config.batch_size
            for i in range(0, len(missing_ids), batch_size):
                batch = missing_ids[i:i+batch_size]
                logger.info(f"Processing batch {i//batch_size + 1}/{(len(missing_ids) + batch_size - 1)//batch_size}")
                
                for star_id in batch:
                    try:
                        # Apply rate limiting
                        self.rate_limiter.wait_if_needed()
                        
                        # Query SIMBAD
                        result = self.simbad.query_object(star_id)
                        
                        if result is not None and len(result) > 0:
                            existing_properties[star_id] = self._extract_properties_from_result(result[0], star_id)
                        
                    except Exception as e:
                        logger.warning(f"Failed to query {star_id}: {e}")
                        continue
                
                # Save progress periodically
                if (i + batch_size) % (batch_size * 5) == 0:
                    self._save_properties_with_safety(existing_properties, properties_file)
                    logger.info(f"Progress saved: {len(existing_properties)} properties")
        
        # Step 4: Merge with catalog data for complete properties
        final_properties = self._merge_catalog_and_simbad_data(
            existing_properties, catalog_data, mode
        )
        
        # Step 5: Save final properties
        self._save_properties_with_safety(final_properties, properties_file)
        
        logger.info(f"Rebuild complete: {len(final_properties)} star properties saved")
        return final_properties
    
    def _merge_catalog_and_simbad_data(self, simbad_props: Dict, catalog_data: Dict, mode: str) -> Dict:
        """
        Merge SIMBAD properties with catalog data.
        """
        merged = simbad_props.copy()
        
        # Add catalog-specific data
        for catalog, table in catalog_data.items():
            if table is None:
                continue
            
            if 'hipparcos' in catalog.lower():
                for row in table:
                    hip_id = f"HIP {row['HIP']}"
                    if hip_id not in merged:
                        merged[hip_id] = {'unique_id': hip_id}
                    
                    # Add/update catalog data
                    merged[hip_id]['Source_Catalog'] = 'Hipparcos'
                    
                    if 'Plx' in row.colnames and row['Plx'] > 0:
                        merged[hip_id]['distance_pc'] = 1000.0 / row['Plx']
                        merged[hip_id]['distance_ly'] = (1000.0 / row['Plx']) * 3.26156
                    
                    if 'Vmag' in row.colnames:
                        merged[hip_id]['V_magnitude'] = float(row['Vmag'])
                    
                    if 'B-V' in row.colnames and 'Vmag' in row.colnames:
                        merged[hip_id]['B_magnitude'] = float(row['Vmag'] + row['B-V'])
            
            elif 'gaia' in catalog.lower():
                for row in table:
                    gaia_id = f"Gaia DR3 {row['Source']}"
                    if gaia_id not in merged:
                        merged[gaia_id] = {'unique_id': gaia_id}
                    
                    merged[gaia_id]['Source_Catalog'] = 'Gaia'
                    
                    if 'Plx' in row.colnames and row['Plx'] > 0:
                        merged[gaia_id]['distance_pc'] = 1000.0 / row['Plx']
                        merged[gaia_id]['distance_ly'] = (1000.0 / row['Plx']) * 3.26156
                    
                    if 'Gmag' in row.colnames:
                        # Approximate V magnitude from Gaia G magnitude
                        merged[gaia_id]['V_magnitude'] = float(row['Gmag']) - 0.2
        
        return merged
    
    def verify_cache_integrity(self) -> Dict:
        """
        Verify integrity of all cache files (PKL and VOT).
        
        Returns:
            Dictionary with integrity status for each cache file
        """
        report = {
            'pkl_files': {},
            'vot_files': {},
            'summary': {
                'total_pkl_entries': 0,
                'total_vot_entries': 0,
                'issues_found': []
            }
        }
        
        # Check PKL files
        pkl_files = [
            'star_data/star_properties_distance.pkl',
            'star_data/star_properties_magnitude.pkl',
        ]
        
        for pkl_file in pkl_files:
            if os.path.exists(pkl_file):
                try:
                    props = self.load_existing_properties(pkl_file)
                    count = len(props)
                    report['pkl_files'][pkl_file] = {
                        'status': 'valid',
                        'entries': count,
                        'size_mb': os.path.getsize(pkl_file) / (1024 * 1024)
                    }
                    report['summary']['total_pkl_entries'] += count
                except Exception as e:
                    report['pkl_files'][pkl_file] = {
                        'status': 'corrupted',
                        'error': str(e)
                    }
                    report['summary']['issues_found'].append(f"{pkl_file}: corrupted")
            else:
                report['pkl_files'][pkl_file] = {'status': 'missing'}
        
        # Check VOT files using VOT manager
        vot_integrity = verify_vot_cache_integrity()
        for vot_file, status in vot_integrity.items():
            report['vot_files'][vot_file] = status
            if status.get('status') == 'valid':
                report['summary']['total_vot_entries'] += status.get('entries', 0)
            elif status.get('status') != 'missing':
                report['summary']['issues_found'].append(f"{vot_file}: {status.get('status')}")
        
        return report
    
    def generate_cache_report(self) -> str:
        """
        Generate human-readable cache status report.
        """
        integrity = self.verify_cache_integrity()
        
        lines = []
        lines.append("=" * 70)
        lines.append("STAR DATA CACHE STATUS REPORT")
        lines.append("=" * 70)
        lines.append(f"Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append("")
        
        # PKL Files Section
        lines.append("PKL PROPERTY FILES")
        lines.append("-" * 40)
        for file, info in integrity['pkl_files'].items():
            lines.append(f"\n{file}:")
            if info['status'] == 'valid':
                lines.append(f"  [OK] Status: VALID")
                lines.append(f"  * Entries: {info['entries']:,}")
                lines.append(f"  * Size: {info['size_mb']:.2f} MB")
            elif info['status'] == 'missing':
                lines.append(f"  [FAIL] Status: MISSING")
            else:
                lines.append(f"  [WARN] Status: CORRUPTED")
                lines.append(f"  * Error: {info.get('error', 'Unknown')}")
        
        # VOT Files Section
        lines.append("\n" + "=" * 40)
        lines.append("VOT CATALOG FILES")
        lines.append("-" * 40)
        for file, info in integrity['vot_files'].items():
            lines.append(f"\n{file}:")
            if info['status'] == 'valid':
                lines.append(f"  [OK] Status: VALID")
                lines.append(f"  * Entries: {info['entries']:,}")
                lines.append(f"  * Columns: {', '.join(info.get('columns', []))}")
            elif info['status'] == 'missing':
                lines.append(f"  [FAIL] Status: MISSING")
            else:
                lines.append(f"  [WARN] Status: CORRUPTED")
        
        # Summary Section
        lines.append("\n" + "=" * 40)
        lines.append("SUMMARY")
        lines.append("-" * 40)
        lines.append(f"Total PKL entries: {integrity['summary']['total_pkl_entries']:,}")
        lines.append(f"Total VOT entries: {integrity['summary']['total_vot_entries']:,}")
        
        if integrity['summary']['issues_found']:
            lines.append(f"\n[WARN] Issues found ({len(integrity['summary']['issues_found'])}):")
            for issue in integrity['summary']['issues_found']:
                lines.append(f"  * {issue}")
        else:
            lines.append("\n[OK] All cache files are healthy")
        
        lines.append("=" * 70)
        
        return "\n".join(lines)

    def _create_simbad_instance(self):
        """Create and configure a SIMBAD instance."""
        custom_simbad = Simbad()
        custom_simbad.reset_votable_fields()
        custom_simbad.ROW_LIMIT = self.config.row_limit
        custom_simbad.TIMEOUT = self.config.timeout
        
        # Add requested fields
        for field in self.config.votable_fields:
            try:
                custom_simbad.add_votable_fields(field)
            except Exception as e:
                logger.warning(f"Could not add field {field}: {e}")
        
        return custom_simbad
    
    def _update_progress(self, current: int, total: int, message: str = ""):
        """Update progress through callback if available."""
        if self.progress_callback:
            try:
                self.progress_callback(current, total, message)
            except Exception as e:
                logger.error(f"Progress callback error: {e}")
    
    def _query_single_object(self, obj_name: str) -> Optional[Any]:
        """
        Query a single object with retry logic.
        
        Returns:
            Query result table or None if failed
        """
        for attempt in range(self.config.max_retries):
            try:
                # Apply rate limiting
                wait_time = self.rate_limiter.wait_if_needed()
                
                # Perform query
                result = self.simbad.query_object(obj_name)
                
                if result is not None and len(result) > 0:
                    self.stats.log_success()
                    return result
                else:
                    # No results found (not an error, just no data)
                    if attempt == self.config.max_retries - 1:
                        self.stats.log_failure(obj_name, "No data found")
                    return None
                    
            except Exception as e:
                self.stats.log_retry()
                
                if attempt < self.config.max_retries - 1:
                    # Exponential backoff for retries
                    delay = self.config.retry_delay * (2 ** attempt)
                    logger.warning(f"Retry {attempt + 1} for {obj_name} after {delay:.1f}s: {e}")
                    time.sleep(delay)
                else:
                    # Final attempt failed
                    self.stats.log_failure(obj_name, str(e))
                    logger.error(f"Failed to query {obj_name} after {self.config.max_retries} attempts: {e}")
                    
                    if self.config.pause_on_error:
                        input(f"Error querying {obj_name}. Press Enter to continue...")
                    
                    return None
        
        return None
    
    def calculate_optimal_batch_size(self, total_objects: int) -> int:
        """Calculate optimal batch size based on total workload."""
        if total_objects < 50:
            return min(10, total_objects)
        elif total_objects < 500:
            return 25
        elif total_objects < 1000:
            return 50
        elif total_objects < 5000:
            return 100
        else:
            return min(200, self.config.batch_size)
    
    def query_objects(self, object_names: List[str], 
                      existing_properties: Optional[Dict] = None,
                      properties_file: Optional[str] = None) -> Dict:
        """
        Query multiple objects with batching and progress tracking.
        
        Args:
            object_names: List of object names to query
            existing_properties: Dictionary of already known properties
            properties_file: Optional file to save progress
            
        Returns:
            Dictionary of object properties
        """
        if existing_properties is None:
            existing_properties = {}
        
        # Filter out objects we already have
        missing_ids = [name for name in object_names if name not in existing_properties]
        
        if not missing_ids:
            logger.info("All objects already in cache")
            return existing_properties
        
        # Calculate batch size
        batch_size = self.calculate_optimal_batch_size(len(missing_ids))
        total_batches = (len(missing_ids) + batch_size - 1) // batch_size
        
        logger.info(f"Querying {len(missing_ids)} objects in {total_batches} batches of {batch_size}")
        self._update_progress(0, len(missing_ids), f"Starting SIMBAD queries...")
        
        # Reset stats for this query session
        self.stats = QueryStats()
        
        # Process in batches
        for batch_num in range(total_batches):
            batch_start = batch_num * batch_size
            batch_end = min((batch_num + 1) * batch_size, len(missing_ids))
            batch_ids = missing_ids[batch_start:batch_end]
            
            batch_message = f"Batch {batch_num + 1}/{total_batches} ({batch_start + 1}-{batch_end})"
            logger.info(batch_message)
            
            # Process each object in the batch
            for idx, obj_name in enumerate(batch_ids):
                global_idx = batch_start + idx
                
                # Check for Messier objects (if messier_catalog module is available)
                try:
                    from messier_catalog import messier_catalog, star_cluster_catalog
                    supplemental_data = {**messier_catalog, **star_cluster_catalog}
                    
                    if obj_name.startswith('M '):
                        messier_id = f"M{obj_name.split()[1]}"
                        if messier_id in supplemental_data:
                            existing_properties[obj_name] = self._process_messier_object(
                                messier_id, supplemental_data[messier_id]
                            )
                            self.stats.log_cached()
                            continue
                except ImportError:
                    pass  # Messier catalog not available
                
                # Query SIMBAD
                result = self._query_single_object(obj_name)
                
                if result is not None:
                    existing_properties[obj_name] = self._process_simbad_result(result)
                else:
                    # Store empty entry for failed queries
                    existing_properties[obj_name] = self._create_empty_entry(obj_name)
                
                # Update progress
                self._update_progress(
                    global_idx + 1, 
                    len(missing_ids),
                    f"{batch_message} - {obj_name}"
                )
                
                # Save progress periodically
                if (global_idx + 1) % self.config.save_progress_interval == 0:
                    if properties_file:
                        self._save_properties(existing_properties, properties_file)
                        if self.config.show_detailed_progress:
                            logger.info(f"Saved progress at {global_idx + 1} objects")
            
            # Save after each batch
            if properties_file:
                self._save_properties(existing_properties, properties_file)
                logger.info(f"Batch {batch_num + 1} complete and saved")
        
        # Final statistics
        logger.info(self.stats.get_summary())
        rate_stats = self.rate_limiter.get_stats()
        logger.info(f"Rate limiting: {rate_stats['actual_rate']:.2f} queries/s "
                   f"(target: {rate_stats['target_rate']:.2f}/s)")
        
        return existing_properties
    
    def _process_simbad_result(self, result_table) -> Dict:
        """Process SIMBAD query result into property dictionary."""
        props = {
            'star_name': None,
            'spectral_type': None,
            'V_magnitude': None,
            'B_magnitude': None,
            'object_type': None,
            'is_messier': False
        }
        
        try:
            # Extract main identifier
            if 'MAIN_ID' in result_table.colnames:
                star_name = result_table['MAIN_ID'][0]
                props['star_name'] = star_name.decode('utf-8') if isinstance(star_name, bytes) else star_name
            
            # Extract spectral type
            if 'SP_TYPE' in result_table.colnames:
                sp_type = result_table['SP_TYPE'][0]
                if sp_type:
                    props['spectral_type'] = sp_type.decode('utf-8') if isinstance(sp_type, bytes) else sp_type
            
            # Extract magnitudes
            if 'FLUX_V' in result_table.colnames:
                props['V_magnitude'] = self._parse_magnitude(result_table['FLUX_V'][0])
            
            if 'FLUX_B' in result_table.colnames:
                props['B_magnitude'] = self._parse_magnitude(result_table['FLUX_B'][0])
            
            # Extract object type
            if 'OTYPE' in result_table.colnames:
                otype = result_table['OTYPE'][0]
                if otype:
                    props['object_type'] = otype.decode('utf-8') if isinstance(otype, bytes) else otype
        
        except Exception as e:
            logger.error(f"Error processing SIMBAD result: {e}")
        
        return props
    
    def _process_messier_object(self, messier_id: str, messier_data: Dict) -> Dict:
        """Process Messier object data."""
        return {
            'star_name': messier_id,
            'spectral_type': messier_data.get('spectral_type'),
            'V_magnitude': messier_data.get('magnitude'),
            'B_magnitude': None,
            'object_type': messier_data.get('type'),
            'distance_ly': messier_data.get('distance_ly'),
            'notes': messier_data.get('notes', ''),
            'is_messier': True
        }
    
    def _create_empty_entry(self, obj_name: str) -> Dict:
        """Create empty property entry for failed queries."""
        return {
            'star_name': obj_name,
            'spectral_type': None,
            'V_magnitude': None,
            'B_magnitude': None,
            'object_type': None,
            'is_messier': False
        }
    
    def _parse_magnitude(self, value) -> Optional[float]:
        """Parse magnitude value from various formats."""
        if value is None:
            return None
        if isinstance(value, (int, float)):
            return float(value)
        
        value_str = str(value)
        # Remove annotations like [~] or [some text]
        cleaned = re.sub(r"\[.*?\]", "", value_str).strip()
        
        try:
            return float(cleaned)
        except ValueError:
            return None
    
    def _save_properties(self, properties: Dict, filepath: str):
        """Save properties to file."""
        try:
            # Convert to list format for compatibility
            all_unique_ids = list(properties.keys())
            property_lists = {
                'unique_ids': all_unique_ids,
                'star_names': [],
                'spectral_types': [],
                'V_magnitudes': [],
                'B_magnitudes': [],
                'object_types': [],
                'is_messier': [],
                'distance_ly': [],
                'notes': []
            }
            
            for uid in all_unique_ids:
                props = properties[uid]
                property_lists['star_names'].append(props.get('star_name'))
                property_lists['spectral_types'].append(props.get('spectral_type'))
                property_lists['V_magnitudes'].append(props.get('V_magnitude'))
                property_lists['B_magnitudes'].append(props.get('B_magnitude'))
                property_lists['object_types'].append(props.get('object_type'))
                property_lists['is_messier'].append(props.get('is_messier', False))
                property_lists['distance_ly'].append(props.get('distance_ly'))
                property_lists['notes'].append(props.get('notes', ''))
            
            with open(filepath, 'wb') as f:
                pickle.dump(property_lists, f)
        
        except Exception as e:
            logger.error(f"Error saving properties to {filepath}: {e}")


    def _extract_properties_from_result(self, result, star_id):
        """Extract properties from SIMBAD query result."""
        props = {'unique_id': star_id}
        
        # This is similar to your existing _process_simbad_result but returns different format
        if 'MAIN_ID' in result.colnames:
            star_name = result['MAIN_ID']
            props['star_name'] = star_name.decode('utf-8') if isinstance(star_name, bytes) else str(star_name)
        
        if 'SP_TYPE' in result.colnames:
            sp_type = result['SP_TYPE']
            if sp_type:
                props['spectral_type'] = sp_type.decode('utf-8') if isinstance(sp_type, bytes) else str(sp_type)
        
        if 'FLUX_V' in result.colnames:
            props['V_magnitude'] = self._parse_magnitude(result['FLUX_V'])
        
        if 'FLUX_B' in result.colnames:
            props['B_magnitude'] = self._parse_magnitude(result['FLUX_B'])
        
        if 'OTYPE' in result.colnames:
            otype = result['OTYPE']
            if otype:
                props['object_type'] = otype.decode('utf-8') if isinstance(otype, bytes) else str(otype)
        
        return props

    def load_existing_properties(self, filepath: str) -> Dict:
        """Load existing properties from pickle file."""
        if not os.path.exists(filepath):
            return {}
        
        try:
            with open(filepath, 'rb') as f:
                data = pickle.load(f)
            
            # Handle both dict and list formats
            if isinstance(data, dict) and 'unique_ids' in data:
                # Convert list format to dict
                properties = {}
                unique_ids = data.get('unique_ids', [])
                star_names = data.get('star_names', [])
                spectral_types = data.get('spectral_types', [])
                v_mags = data.get('V_magnitudes', [])
                b_mags = data.get('B_magnitudes', [])
                obj_types = data.get('object_types', [])
                
                for i, uid in enumerate(unique_ids):
                    properties[uid] = {
                        'star_name': star_names[i] if i < len(star_names) else None,
                        'spectral_type': spectral_types[i] if i < len(spectral_types) else None,
                        'V_magnitude': v_mags[i] if i < len(v_mags) else None,
                        'B_magnitude': b_mags[i] if i < len(b_mags) else None,
                        'object_type': obj_types[i] if i < len(obj_types) else None,
                    }
                return properties
            elif isinstance(data, dict):
                return data
            else:
                return {}
        except Exception as e:
            logger.error(f"Error loading properties from {filepath}: {e}")
            return {}


# Compatibility wrapper for existing code
def create_custom_simbad():
    """Compatibility function for existing code."""
    config = SimbadConfig()
    manager = SimbadQueryManager(config)
    return manager.simbad


def query_simbad_for_star_properties(missing_ids, existing_properties, properties_file):
    """
    Compatibility wrapper for existing code.
    This maintains the same interface as the original function.
    """
    # Load saved configuration if it exists
    config = SimbadConfig.load_from_file()
    
    # Create manager
    manager = SimbadQueryManager(config)
    
    # Query objects
    updated_properties = manager.query_objects(
        missing_ids,
        existing_properties,
        properties_file
    )
    
    return updated_properties


# Convenience functions to add at module level

def quick_cache_check():
    """Quick check of all cache files."""
    config = SimbadConfig()
    manager = SimbadQueryManager(config)
    print(manager.generate_cache_report())
    return manager.verify_cache_integrity()


def rebuild_from_vot(mode='distance', force=False):
    """
    Rebuild PKL file from VOT caches.
    
    Args:
        mode: 'distance' or 'magnitude'
        force: Force rebuild even if PKL exists
    """
    config = SimbadConfig()
    manager = SimbadQueryManager(config)
    
    # Protect existing files first
    manager.protect_all_caches()
    
    # Rebuild
    result = manager.rebuild_pkl_from_vot_caches(mode=mode, force_rebuild=force)
    
    print(f"Rebuilt {len(result)} star properties for {mode} mode")
    return result


def protect_all_star_data():
    """Create protected backups of all star data files."""
    config = SimbadConfig()
    manager = SimbadQueryManager(config)
    
    protected = manager.protect_all_caches()
    print(f"Protected {len(protected)} cache files")
    
    # Also generate report
    print("\n" + manager.generate_cache_report())
    
    return protected

# Test function for standalone execution
if __name__ == "__main__":
    # Test with a few objects
    test_objects = ["Proxima Centauri", "Sirius", "M31", "Betelgeuse"]
    
    config = SimbadConfig(
        queries_per_second=2.0,  # Slower for testing
        show_detailed_progress=True
    )
    
    manager = SimbadQueryManager(config)
    results = manager.query_objects(test_objects)
    
    for name, props in results.items():
        print(f"\n{name}:")
        for key, value in props.items():
            if value is not None:
                print(f"  {key}: {value}")
