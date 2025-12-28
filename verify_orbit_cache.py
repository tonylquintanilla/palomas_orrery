#!/usr/bin/env python3
"""
verify_orbit_cache.py - Safely verify and repair orbit_paths.json

This script will:
1. Create a backup of your current orbit_paths.json
2. Load and validate the file
3. Report any issues found
4. Optionally repair corrupted entries
5. Show statistics about your orbit cache
"""

import json
import os
import shutil
from datetime import datetime
import sys

def create_backup(file_path):
    """Create a timestamped backup of the orbit cache file."""
    if not os.path.exists(file_path):
        print(f"No file to backup at {file_path}")
        return None
        
    backup_name = f"{file_path}.verify_backup.{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    try:
        shutil.copy2(file_path, backup_name)
        size_mb = os.path.getsize(file_path) / (1024 * 1024)
        print(f"[OK] Created backup: {backup_name} ({size_mb:.1f} MB)")
        return backup_name
    except Exception as e:
        print(f"[FAIL] Failed to create backup: {e}")
        return None

def verify_orbit_cache(file_path='orbit_paths.json', repair=False):
    """Verify the orbit cache file and optionally repair it."""
    
    print(f"\n{'='*60}")
    print(f"Orbit Cache Verification Tool")
    print(f"{'='*60}\n")
    
    # Step 1: Create backup
    print("Step 1: Creating backup...")
    backup_file = create_backup(file_path)
    if not backup_file and os.path.exists(file_path):
        response = input("Failed to create backup. Continue anyway? (y/n): ")
        if response.lower() != 'y':
            return
    
    # Step 2: Check file exists and size
    print("\nStep 2: Checking file...")
    if not os.path.exists(file_path):
        print(f"[FAIL] File not found: {file_path}")
        return
        
    file_size = os.path.getsize(file_path)
    file_size_mb = file_size / (1024 * 1024)
    print(f"[OK] File exists: {file_size:,} bytes ({file_size_mb:.1f} MB)")
    
    # Step 3: Load and parse JSON
    print("\nStep 3: Loading JSON...")
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        print(f"[OK] JSON is valid")
    except json.JSONDecodeError as e:
        print(f"[FAIL] JSON is corrupted: {e}")
        print(f"\nFile appears to be corrupted beyond simple repair.")
        print(f"You should restore from backup: {backup_file}")
        return
    except Exception as e:
        print(f"[FAIL] Error reading file: {e}")
        return
    
    # Step 4: Validate structure
    print("\nStep 4: Validating orbit data structure...")
    if not isinstance(data, dict):
        print(f"[FAIL] Root structure is not a dictionary")
        return
        
    total_entries = len(data)
    valid_entries = 0
    corrupted_entries = []
    old_format_entries = []
    
    for orbit_key, orbit_data in data.items():
        try:
            # Check basic structure
            if not isinstance(orbit_data, dict):
                corrupted_entries.append((orbit_key, "Not a dictionary"))
                continue
            
            # Check for new format
            if "data_points" in orbit_data and "metadata" in orbit_data:
                # Validate new format
                if not isinstance(orbit_data["data_points"], dict):
                    corrupted_entries.append((orbit_key, "Invalid data_points"))
                    continue
                if not isinstance(orbit_data["metadata"], dict):
                    corrupted_entries.append((orbit_key, "Invalid metadata"))
                    continue
                valid_entries += 1
                
            # Check for old format
            elif all(k in orbit_data for k in ['x', 'y', 'z']):
                # Validate old format
                if not all(isinstance(orbit_data[k], list) for k in ['x', 'y', 'z']):
                    corrupted_entries.append((orbit_key, "Invalid coordinate arrays"))
                    continue
                    
                lens = [len(orbit_data[k]) for k in ['x', 'y', 'z']]
                if len(set(lens)) != 1:
                    corrupted_entries.append((orbit_key, f"Mismatched array lengths: {lens}"))
                    continue
                    
                old_format_entries.append(orbit_key)
                valid_entries += 1
            else:
                corrupted_entries.append((orbit_key, "Unknown format"))
                
        except Exception as e:
            corrupted_entries.append((orbit_key, f"Validation error: {str(e)}"))
    
    # Step 5: Report findings
    print(f"\n{'='*60}")
    print(f"VALIDATION RESULTS")
    print(f"{'='*60}")
    print(f"Total entries: {total_entries}")
    print(f"Valid entries: {valid_entries}")
    print(f"Old format entries: {len(old_format_entries)}")
    print(f"Corrupted entries: {len(corrupted_entries)}")
    
    if old_format_entries:
        print(f"\nOld format entries (will be auto-converted on next load):")
        for entry in old_format_entries[:5]:
            print(f"  - {entry}")
        if len(old_format_entries) > 5:
            print(f"  ... and {len(old_format_entries) - 5} more")
    
    if corrupted_entries:
        print(f"\nCorrupted entries found:")
        for entry, reason in corrupted_entries[:10]:
            print(f"  - {entry}: {reason}")
        if len(corrupted_entries) > 10:
            print(f"  ... and {len(corrupted_entries) - 10} more")
    
    # Step 6: Repair if requested
    if corrupted_entries and repair:
        print(f"\n{'='*60}")
        print(f"REPAIR MODE")
        print(f"{'='*60}")
        
        response = input(f"Remove {len(corrupted_entries)} corrupted entries? (y/n): ")
        if response.lower() == 'y':
            # Remove corrupted entries
            for entry, _ in corrupted_entries:
                del data[entry]
            
            # Save repaired data
            repair_file = file_path + '.repaired'
            with open(repair_file, 'w') as f:
                json.dump(data, f)
            
            print(f"[OK] Repaired data saved to: {repair_file}")
            print(f"  Remaining entries: {len(data)}")
            print(f"\nTo use the repaired file:")
            print(f"  1. Verify the repaired file looks correct")
            print(f"  2. mv {repair_file} {file_path}")
    
    elif corrupted_entries:
        print(f"\nTo repair, run: python {__file__} --repair")
    
    # Step 7: Show sample data
    if valid_entries > 0:
        print(f"\n{'='*60}")
        print(f"SAMPLE DATA")
        print(f"{'='*60}")
        
        sample_key = list(data.keys())[0]
        sample_data = data[sample_key]
        
        print(f"\nExample entry: {sample_key}")
        if "data_points" in sample_data:
            num_points = len(sample_data["data_points"])
            print(f"  Format: New (time-indexed)")
            print(f"  Data points: {num_points}")
            if sample_data.get("metadata"):
                print(f"  Start date: {sample_data['metadata'].get('start_date', 'Unknown')}")
                print(f"  End date: {sample_data['metadata'].get('end_date', 'Unknown')}")
                print(f"  Center body: {sample_data['metadata'].get('center_body', 'Unknown')}")
        else:
            print(f"  Format: Old (array-based)")
            print(f"  Data points: {len(sample_data.get('x', []))}")
    
    print(f"\n{'='*60}")
    print(f"Verification complete!")
    print(f"{'='*60}")

if __name__ == "__main__":
    repair_mode = '--repair' in sys.argv
    verify_orbit_cache(repair=repair_mode)
