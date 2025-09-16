# Complete replacement for test_orbit_cache.py with proper isolation

"""
test_orbit_cache.py - Comprehensive test suite for orbit data caching and repair

This module tests the orbit data manager's caching functionality including:
- Loading and saving cache files
- Format conversion (old to new)
- Corruption detection and repair
- Incremental updates
- Edge cases and error handling

Run this module periodically to ensure cache functionality remains robust.
"""
import json
import os
import shutil
import tempfile
import unittest
from datetime import datetime, timedelta
import numpy as np
from unittest.mock import patch, MagicMock, Mock
import sys

# CRITICAL: DO NOT import orbit_data_manager at module level!
# We'll import it inside each test after setting up patches

class TestOrbitCache(unittest.TestCase):
    """Test suite for orbit data caching functionality"""
    
    def setUp(self):
        """Set up test environment before each test"""
        # Create a test directory in the current project directory
        self.test_dir = os.path.join(os.path.dirname(__file__), "test_output")
        
        # Create the directory if it doesn't exist
        if not os.path.exists(self.test_dir):
            os.makedirs(self.test_dir)
            
        # Clear any existing test files
        for file in os.listdir(self.test_dir):
            file_path = os.path.join(self.test_dir, file)
            if os.path.isfile(file_path):
                os.unlink(file_path)
                
        self.test_cache_file = os.path.join(self.test_dir, "test_orbit_paths.json")
        
        # Create sample data for testing
        self.sample_new_format = {
            "Mars_Sun": {
                "data_points": {
                    "2025-01-01": {"x": 1.5, "y": 0.2, "z": 0.1},
                    "2025-01-02": {"x": 1.51, "y": 0.21, "z": 0.11},
                    "2025-01-03": {"x": 1.52, "y": 0.22, "z": 0.12}
                },
                "metadata": {
                    "start_date": "2025-01-01",
                    "end_date": "2025-01-03",
                    "center_body": "Sun",
                    "last_updated": "2025-01-01"
                }
            },
            "Jupiter_Sun": {
                "data_points": {
                    "2025-01-01": {"x": 5.2, "y": 0.3, "z": 0.15},
                    "2025-01-02": {"x": 5.21, "y": 0.31, "z": 0.16}
                },
                "metadata": {
                    "start_date": "2025-01-01",
                    "end_date": "2025-01-02",
                    "center_body": "Sun",
                    "last_updated": "2025-01-01"
                }
            }
        }
        
        self.sample_old_format = {
            "Venus_Sun": {
                "x": [0.72, 0.73, 0.74],
                "y": [0.1, 0.11, 0.12],
                "z": [0.05, 0.051, 0.052]
            },
            "Earth_Sun": {
                "x": [1.0, 1.01, 1.02],
                "y": [0.0, 0.01, 0.02],
                "z": [0.0, 0.001, 0.002]
            }
        }
        
    def tearDown(self):
        """Clean up test environment after each test"""
        # Don't remove the test directory - keep it for inspection
        # Just clean up the module
        if 'orbit_data_manager' in sys.modules:
            del sys.modules['orbit_data_manager']
            
        print(f"\nTest files saved in: {self.test_dir}")
            
    def test_save_and_load_valid_cache(self):
        """Test saving and loading valid cache data"""
        # Patch BEFORE importing
        with patch.dict('os.environ', {'ORBIT_PATHS_FILE': self.test_cache_file}):
            # Now import with the patch active
            import orbit_data_manager
            
            # Override the constant
            orbit_data_manager.ORBIT_PATHS_FILE = self.test_cache_file
            
            # Save data
            orbit_data_manager.save_orbit_paths(self.sample_new_format, self.test_cache_file)
            
            # Verify file exists in test directory
            self.assertTrue(os.path.exists(self.test_cache_file))
            
            # Load the data
            loaded_data = orbit_data_manager.load_orbit_paths(self.test_cache_file)
            
            # Verify data matches
            self.assertEqual(loaded_data, self.sample_new_format)
            
    def test_load_nonexistent_file(self):
        """Test loading when cache file doesn't exist"""
        with patch.dict('os.environ', {'ORBIT_PATHS_FILE': self.test_cache_file}):
            import orbit_data_manager
            orbit_data_manager.ORBIT_PATHS_FILE = self.test_cache_file
            
            # Ensure file doesn't exist
            self.assertFalse(os.path.exists(self.test_cache_file))
            
            # Mock the status_display to avoid issues
            orbit_data_manager.status_display = None
            
            # Load should return empty dict
            loaded_data = orbit_data_manager.load_orbit_paths(self.test_cache_file)
            self.assertEqual(loaded_data, {})
            
    def test_old_format_conversion(self):
        """Test automatic conversion from old to new format"""
        with patch.dict('os.environ', {'ORBIT_PATHS_FILE': self.test_cache_file}):
            import orbit_data_manager
            orbit_data_manager.ORBIT_PATHS_FILE = self.test_cache_file
            orbit_data_manager.status_display = None
            
            # Save old format data
            with open(self.test_cache_file, 'w') as f:
                json.dump(self.sample_old_format, f)
                
            # Load data (should trigger conversion)
            loaded_data = orbit_data_manager.load_orbit_paths(self.test_cache_file)
            
            # Verify conversion happened
            for key in self.sample_old_format:
                self.assertIn(key, loaded_data)
                self.assertIn("data_points", loaded_data[key])
                self.assertIn("metadata", loaded_data[key])
                
    def test_corrupted_json_file(self):
        """Test handling of corrupted JSON file"""
        with patch.dict('os.environ', {'ORBIT_PATHS_FILE': self.test_cache_file}):
            import orbit_data_manager
            orbit_data_manager.ORBIT_PATHS_FILE = self.test_cache_file
            orbit_data_manager.status_display = None
            
            # Write invalid JSON
            with open(self.test_cache_file, 'w') as f:
                f.write("{invalid json content}")
                
            # Load should handle gracefully
            loaded_data = orbit_data_manager.load_orbit_paths(self.test_cache_file)
            self.assertEqual(loaded_data, {})
            
            # Check that backup was created
            backup_files = [f for f in os.listdir(self.test_dir) if '.corrupted' in f]
            self.assertTrue(len(backup_files) > 0, 
                           f"No backup files found. Files in {self.test_dir}: {os.listdir(self.test_dir)}")
                           
    def test_status_display_updates(self):
        """Test that status display is updated during operations"""
        with patch.dict('os.environ', {'ORBIT_PATHS_FILE': self.test_cache_file}):
            import orbit_data_manager
            orbit_data_manager.ORBIT_PATHS_FILE = self.test_cache_file
            
            # Track all print statements as a proxy for status updates
            print_messages = []
            
            # Mock the print function to capture messages
            with patch('builtins.print') as mock_print:
                mock_print.side_effect = lambda *args, **kwargs: print_messages.append(' '.join(str(arg) for arg in args))
                
                # Create corrupted cache
                corrupted_data = {
                    "Valid_Sun": self.sample_new_format["Mars_Sun"],
                    "Invalid_Sun": "corrupted"
                }
                
                with open(self.test_cache_file, 'w') as f:
                    json.dump(corrupted_data, f)
                    
                # Load with repair - this should trigger status updates
                orbit_data_manager.load_orbit_paths(self.test_cache_file)
                
                # Verify that status messages were printed
                # We should see messages about cache repair
                status_messages = [msg for msg in print_messages if 'CACHE REPAIR' in msg or 'Cache repaired' in msg]
                self.assertTrue(len(status_messages) > 0, 
                              f"No status messages found. All messages: {print_messages}")
            
    def test_partially_corrupted_entries(self):
        """Test detection and removal of corrupted entries"""
        with patch.dict('os.environ', {'ORBIT_PATHS_FILE': self.test_cache_file}):
            import orbit_data_manager
            orbit_data_manager.ORBIT_PATHS_FILE = self.test_cache_file
            orbit_data_manager.status_display = None
            
            # Create mixed valid/invalid data
            corrupted_data = {
                "Mars_Sun": self.sample_new_format["Mars_Sun"],  # Valid
                "Venus_Sun": None,  # Invalid
                "Earth_Sun": "invalid string",  # Invalid
                "Neptune_Sun": {  # Valid old format
                    "x": [30.0, 30.1],
                    "y": [0.1, 0.11],
                    "z": [0.01, 0.011]
                }
            }
            
            with open(self.test_cache_file, 'w') as f:
                json.dump(corrupted_data, f)
                
            # Load with repair
            loaded_data = orbit_data_manager.load_orbit_paths(self.test_cache_file)
            
            # Verify only valid entries remain
            self.assertIn("Mars_Sun", loaded_data)
            self.assertIn("Neptune_Sun", loaded_data)
            self.assertNotIn("Venus_Sun", loaded_data)
            self.assertNotIn("Earth_Sun", loaded_data)


if __name__ == "__main__":
    print(f"Test output will be created in: ./test_output/")
    print("Running tests in isolated environment...")
    
    # Create test output directory if it doesn't exist
    test_output_dir = os.path.join(os.path.dirname(__file__), "test_output")
    if not os.path.exists(test_output_dir):
        os.makedirs(test_output_dir)
        print(f"Created test output directory: {test_output_dir}")
    
    # Run tests
    unittest.main()
