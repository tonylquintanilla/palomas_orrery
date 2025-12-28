# vot_cache_manager.py
"""
VOT Cache Manager - Safe management of VizieR VOT cache files
Similar protection protocols as PKL files in simbad_manager.py
"""

import os
import time
import shutil
import logging
from typing import Dict, Optional, Tuple, Any
from astropy.table import Table
from astropy.io import votable
import json
from dataclasses import dataclass, asdict
from datetime import datetime
import numpy as np
import pandas as pd


logger = logging.getLogger(__name__)

@dataclass
class VOTCacheMetadata:
    """Metadata for VOT cache files"""
    filename: str
    query_type: str  # 'distance' or 'magnitude'
    limit_value: float
    entry_count: int
    creation_date: str
    last_modified: str
    catalog: str  # 'hipparcos' or 'gaia'
    min_parallax: Optional[float] = None  # For distance queries
    checksum: Optional[str] = None
    
    def to_dict(self):
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: Dict):
        return cls(**data)


class VOTCacheManager:
    """Manager for safe VOT cache file operations"""
    
#    def __init__(self, cache_dir: str = '.'):
    def __init__(self, cache_dir: str = 'star_data'):
        self.cache_dir = cache_dir
        self.metadata_suffix = '_metadata.json'
        self.backup_suffix = '.backup'
        self.temp_suffix = '.tmp'
        
        # Protected base VOT files (recovered archives)
        self.protected_files = {
            'hipparcos_data_distance.vot': {
                'type': 'distance',
                'limit': 100.1,  # 100.1 light-years
                'catalog': 'hipparcos'
            },
            'hipparcos_data_magnitude.vot': {
                'type': 'magnitude', 
                'limit': 9.0,  # V magnitude 9
                'catalog': 'hipparcos'
            },
            'gaia_data_distance.vot': {
                'type': 'distance',
                'limit': 100.1,
                'catalog': 'gaia'
            },
            'gaia_data_magnitude.vot': {
                'type': 'magnitude',
                'limit': 9.0,
                'catalog': 'gaia'
            }
        }
    
    def protect_base_file(self, filepath: str) -> bool:
        """
        Create protected backup of base VOT file.
        Similar to PKL protection in simbad_manager.
        """
        if not os.path.exists(filepath):
            logger.warning(f"Base file {filepath} does not exist")
            return False
        
        # Create protected backup with timestamp
        protected_backup = filepath + '.protected_' + time.strftime('%Y%m%d_%H%M%S')
        
        try:
            shutil.copy2(filepath, protected_backup)
            logger.info(f"Created protected backup: {protected_backup}")
            
            # Also create metadata for the protected file
            self._create_metadata_for_vot(filepath, protected_backup)
            return True
            
        except Exception as e:
            logger.error(f"Failed to protect base file {filepath}: {e}")
            return False
    
    def _create_metadata_for_vot(self, original_path: str, backup_path: str = None):
        """Create metadata file for VOT cache"""
        target_path = backup_path if backup_path else original_path
        
        try:
            # Load VOT to get entry count
            table = Table.read(target_path, format='votable')
            entry_count = len(table)
            
            # Get file info from protected_files or infer
            basename = os.path.basename(original_path)
            file_info = self.protected_files.get(basename, {})
            
            metadata = VOTCacheMetadata(
                filename=basename,
                query_type=file_info.get('type', 'unknown'),
                limit_value=file_info.get('limit', 0.0),
                entry_count=entry_count,
                creation_date=datetime.now().isoformat(),
                last_modified=datetime.now().isoformat(),
                catalog=file_info.get('catalog', 'unknown')
            )
            
            # Save metadata
            metadata_file = target_path + self.metadata_suffix
            with open(metadata_file, 'w') as f:
                json.dump(metadata.to_dict(), f, indent=2)
            
            logger.info(f"Created metadata for {target_path}: {entry_count} entries")
            
        except Exception as e:
            logger.error(f"Failed to create metadata for {target_path}: {e}")
    
    def safe_load_vot(self, filepath: str) -> Optional[Table]:
        """
        Safely load VOT file with validation.
        Returns None if file is corrupted or missing.
        """
        if not os.path.exists(filepath):
            logger.warning(f"VOT file not found: {filepath}")
            return None
        
        try:
            table = Table.read(filepath, format='votable')
            
            # Basic validation
            if len(table) == 0:
                logger.warning(f"VOT file {filepath} is empty")
                return None
            
            # Check for required columns based on catalog type
            basename = os.path.basename(filepath)
            if 'hipparcos' in basename.lower():
                required_cols = ['HIP', 'Plx', 'Vmag']
            elif 'gaia' in basename.lower():
                required_cols = ['Source', 'Plx', 'Gmag']
            else:
                required_cols = []
            
            missing_cols = [col for col in required_cols if col not in table.colnames]
            if missing_cols:
                logger.warning(f"VOT file {filepath} missing columns: {missing_cols}")
            
            return table
            
        except Exception as e:
            logger.error(f"Failed to load VOT file {filepath}: {e}")
            
            # Try to restore from backup
            backup_file = filepath + self.backup_suffix
            if os.path.exists(backup_file):
                logger.info(f"Attempting to restore from backup: {backup_file}")
                try:
                    table = Table.read(backup_file, format='votable')
                    # Restore the main file
                    shutil.copy2(backup_file, filepath)
                    logger.info(f"Successfully restored {filepath} from backup")
                    return table
                except Exception as e2:
                    logger.error(f"Failed to restore from backup: {e2}")
            
            return None
    
    def safe_save_vot(self, table: Table, filepath: str, metadata: Optional[VOTCacheMetadata] = None):
        """
        Safely save VOT file with atomic operation and backup.
        Similar to safe_save_properties in simbad_manager.
        """
        if table is None or len(table) == 0:
            logger.error("Refusing to save empty table")
            raise ValueError("Cannot save empty VOT table")
        
        # Safety check: prevent data loss
        if os.path.exists(filepath):
            existing_table = self.safe_load_vot(filepath)
            if existing_table is not None:
                original_count = len(existing_table)
                new_count = len(table)
                
                # Don't allow massive data loss
                if original_count > 100 and new_count < original_count * 0.1:
                    emergency_backup = filepath + '.emergency_' + time.strftime('%Y%m%d_%H%M%S')
                    shutil.copy2(filepath, emergency_backup)
                    logger.error(f"SAFETY: Blocked save that would reduce {original_count} to {new_count} entries")
                    logger.info(f"Emergency backup created: {emergency_backup}")
                    raise ValueError(f"Refusing to save: would lose {original_count - new_count} entries")
        
        # Atomic save operation
        temp_file = filepath + self.temp_suffix
        backup_file = filepath + self.backup_suffix
        
        try:
            # Write to temp file
            votable.writeto(votable.from_table(table), temp_file)
            
            # Verify temp file
            verify_table = Table.read(temp_file, format='votable')
            if len(verify_table) != len(table):
                raise ValueError("Verification failed: row count mismatch")
            
            # Backup original if it exists
            if os.path.exists(filepath):
                if os.path.exists(backup_file):
                    os.remove(backup_file)
                shutil.move(filepath, backup_file)
            
            # Move temp to final
            shutil.move(temp_file, filepath)
            
            # Save metadata if provided
            if metadata:
                metadata.last_modified = datetime.now().isoformat()
                metadata.entry_count = len(table)
                metadata_file = filepath + self.metadata_suffix
                with open(metadata_file, 'w') as f:
                    json.dump(metadata.to_dict(), f, indent=2)
            
            # Clean up backup if successful
            if os.path.exists(backup_file):
                os.remove(backup_file)
            
            logger.info(f"Saved {len(table)} entries to {filepath}")
            
        except Exception as e:
            logger.error(f"Error saving VOT file: {e}")
            
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
    
    def merge_vot_incremental(self, existing_table: Table, new_table: Table, 
                             mode: str = 'distance') -> Table:
        """
        Merge new VOT data with existing cache.
        Similar to incremental cache updates for PKL files.
        """
        if existing_table is None:
            return new_table
        if new_table is None or len(new_table) == 0:
            return existing_table
        
        # Identify unique column based on catalog
        if 'HIP' in existing_table.colnames:
            id_col = 'HIP'
        elif 'Source' in existing_table.colnames:
            id_col = 'Source'
        else:
            # Fall back to simple concatenation
            logger.warning("No ID column found, concatenating tables")
            from astropy.table import vstack
            return vstack([existing_table, new_table])
        
        # Get existing IDs
        existing_ids = set(existing_table[id_col])
        
        # Filter new data to only include non-duplicates
        new_mask = [id_val not in existing_ids for id_val in new_table[id_col]]
        unique_new = new_table[new_mask]
        
        if len(unique_new) > 0:
            from astropy.table import vstack
            merged = vstack([existing_table, unique_new])
            logger.info(f"Added {len(unique_new)} new entries to cache")
            return merged
        else:
            logger.info("No new unique entries to add")
            return existing_table
    
    def rebuild_pkl_from_caches(self, properties_file: str, 
                               vot_files: Dict[str, str],
                               simbad_manager_instance: Any) -> Dict:
        """
        Rebuild PKL properties file from existing VOT and PKL caches.
        This merges VizieR catalog data with SIMBAD properties.
        """
        logger.info(f"Rebuilding {properties_file} from VOT and existing caches...")
        
        all_properties = {}
        
        # Load data from each VOT file
        for catalog, vot_file in vot_files.items():
            if not os.path.exists(vot_file):
                logger.warning(f"VOT file not found: {vot_file}")
                continue
            
            table = self.safe_load_vot(vot_file)
            if table is None:
                continue
            
            logger.info(f"Processing {len(table)} entries from {catalog}")
            
            # Extract star identifiers and basic properties
            if 'hipparcos' in catalog.lower():
                for row in table:
                    hip_id = f"HIP {row['HIP']}"
                    
                    # Initialize property dict
                    props = {
                        'unique_id': hip_id,
                        'Source_Catalog': 'Hipparcos',
                        'distance_pc': 1000.0 / row['Plx'] if row['Plx'] > 0 else None,
                        'distance_ly': (1000.0 / row['Plx']) * 3.26156 if row['Plx'] > 0 else None
                    }
                    
                    # Add magnitude data if available
                    if 'Vmag' in row.colnames and not np.isnan(row['Vmag']):
                        props['V_magnitude'] = float(row['Vmag'])
                    if 'B-V' in row.colnames and not np.isnan(row['B-V']):
                        props['B_magnitude'] = float(row['Vmag'] + row['B-V'])
                    
                    all_properties[hip_id] = props
            
            elif 'gaia' in catalog.lower():
                for row in table:
                    gaia_id = f"Gaia DR3 {row['Source']}"
                    
                    props = {
                        'unique_id': gaia_id,
                        'Source_Catalog': 'Gaia',
                        'distance_pc': 1000.0 / row['Plx'] if row['Plx'] > 0 else None,
                        'distance_ly': (1000.0 / row['Plx']) * 3.26156 if row['Plx'] > 0 else None
                    }
                    
                    # Convert Gaia magnitude to V magnitude (approximate)
                    if 'Gmag' in row.colnames and not np.isnan(row['Gmag']):
                        # Rough conversion: V ~ G - 0.2
                        props['V_magnitude'] = float(row['Gmag']) - 0.2
                    
                    all_properties[gaia_id] = props
        
        # Now query SIMBAD for additional properties
        missing_ids = list(all_properties.keys())
        
        if missing_ids and simbad_manager_instance:
            logger.info(f"Querying SIMBAD for {len(missing_ids)} stars...")
            
            # Use existing SIMBAD query function with rate limiting
            updated_properties = simbad_manager_instance.query_simbad_for_star_properties(
                missing_ids, 
                all_properties, 
                properties_file
            )
            
            return updated_properties
        
        # Save properties even without SIMBAD data
        if all_properties:
            simbad_manager_instance.safe_save_properties(all_properties, properties_file)
        
        return all_properties


# Integration functions for existing code
def integrate_vot_protection_with_simbad_manager(simbad_manager):
    """
    Add VOT cache management methods to existing SimbadQueryManager.
    """
    # Create VOT manager instance
    vot_manager = VOTCacheManager()
    
    # Add as attribute to SimbadQueryManager
    simbad_manager.vot_manager = vot_manager
    
    # Add convenience methods
    def protect_vot_caches(self):
        """Protect all base VOT cache files"""
        protected_count = 0
        for vot_file in self.vot_manager.protected_files.keys():
            filepath = os.path.join(self.vot_manager.cache_dir, vot_file)
            if os.path.exists(filepath):
                if self.vot_manager.protect_base_file(filepath):
                    protected_count += 1
        logger.info(f"Protected {protected_count} VOT cache files")
        return protected_count
    
    def rebuild_properties_from_all_caches(self, mode='distance'):
        """Rebuild PKL properties from VOT and existing caches"""
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
        
        return self.vot_manager.rebuild_pkl_from_caches(
            properties_file, vot_files, self
        )
    
    # Bind methods to instance
    import types
    simbad_manager.protect_vot_caches = types.MethodType(protect_vot_caches, simbad_manager)
    simbad_manager.rebuild_properties_from_all_caches = types.MethodType(
        rebuild_properties_from_all_caches, simbad_manager
    )
    
    return simbad_manager


# Standalone utility functions
def verify_vot_cache_integrity():
    """Verify integrity of all VOT cache files"""
    manager = VOTCacheManager()
    results = {}
    
    for vot_file in manager.protected_files.keys():
        filepath = os.path.join(manager.cache_dir, vot_file)
        if os.path.exists(filepath):
            table = manager.safe_load_vot(filepath)
            if table is not None:
                results[vot_file] = {
                    'status': 'valid',
                    'entries': len(table),
                    'columns': table.colnames[:5]  # First 5 columns
                }
            else:
                results[vot_file] = {'status': 'corrupted'}
        else:
            results[vot_file] = {'status': 'missing'}
    
    return results


def create_vot_cache_report():
    """Generate detailed report of VOT cache status"""
    manager = VOTCacheManager()
    report = []
    report.append("=" * 60)
    report.append("VOT Cache Status Report")
    report.append("=" * 60)
    
    total_size = 0
    total_entries = 0
    
    for vot_file, info in manager.protected_files.items():
        filepath = os.path.join(manager.cache_dir, vot_file)
        report.append(f"\n{vot_file}:")
        report.append(f"  Type: {info['type']}")
        report.append(f"  Limit: {info['limit']}")
        report.append(f"  Catalog: {info['catalog']}")
        
        if os.path.exists(filepath):
            size_mb = os.path.getsize(filepath) / (1024 * 1024)
            total_size += size_mb
            report.append(f"  Size: {size_mb:.2f} MB")
            
            table = manager.safe_load_vot(filepath)
            if table:
                total_entries += len(table)
                report.append(f"  Entries: {len(table):,}")
                report.append(f"  Columns: {', '.join(table.colnames[:5])}...")
            else:
                report.append("  Status: CORRUPTED")
        else:
            report.append("  Status: MISSING")
        
        # Check for backups
        backup_files = [
            filepath + '.backup',
            filepath + '.protected_*'
        ]
        for pattern in backup_files:
            import glob
            matches = glob.glob(pattern)
            if matches:
                report.append(f"  Backups: {len(matches)} found")
    
    report.append(f"\n{'-' * 40}")
    report.append(f"Total cache size: {total_size:.2f} MB")
    report.append(f"Total entries: {total_entries:,}")
    report.append("=" * 60)
    
    return "\n".join(report)


if __name__ == "__main__":
    # Test the VOT cache manager
    logging.basicConfig(level=logging.INFO)
    
    # Create manager
    manager = VOTCacheManager()
    
    # Verify cache integrity
    print("\nVerifying VOT cache integrity...")
    integrity = verify_vot_cache_integrity()
    for file, status in integrity.items():
        print(f"  {file}: {status}")
    
    # Generate report
    print("\n" + create_vot_cache_report())
