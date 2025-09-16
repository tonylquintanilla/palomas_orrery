import json
import os
from datetime import datetime
from typing import Dict, Any
import pandas as pd
import numpy as np

class PlotDataExchange:
    """Exchange plot data between subprocess scripts and GUI."""
    
    EXCHANGE_FILE = "last_plot_data.json"
    
    @classmethod
    def save_plot_data(cls, combined_df: pd.DataFrame, counts_dict: Dict,
                       processing_times: Dict = None, mode: str = 'magnitude',
                       limit_value: float = None):
        """
        Save plot data for the GUI to read.
        Called from hr_diagram_apparent_magnitude.py and hr_diagram_distance.py
        """
        # Extract key statistics from DataFrame
        total_stars = len(combined_df)
        
        # Temperature statistics
        temp_valid = (combined_df['Temperature'] > 0).sum() if 'Temperature' in combined_df else 0
        temp_missing = total_stars - temp_valid
        
        # Luminosity statistics
        lum_valid = (combined_df['Luminosity'] > 0).sum() if 'Luminosity' in combined_df else 0
        lum_missing = total_stars - lum_valid
        
        # Catalog distribution
        catalog_counts = {}
        if 'Source_Catalog' in combined_df:
            for catalog, count in combined_df['Source_Catalog'].value_counts().items():
                catalog_counts[str(catalog)] = int(count)
        
        # Magnitude statistics with NaN/Inf handling
        mag_stats = {}
        if 'Apparent_Magnitude' in combined_df:
            mag_array = combined_df['Apparent_Magnitude'].dropna()
            if len(mag_array) > 0:
                # Convert to regular Python floats and handle NaN/Inf
                mag_stats = {
                    'min': cls._safe_float(mag_array.min()),
                    'max': cls._safe_float(mag_array.max()),
                    'mean': cls._safe_float(mag_array.mean()),
                    'median': cls._safe_float(mag_array.median()),
                    'std': cls._safe_float(mag_array.std())
                }
        
        # Clean counts_dict to remove DataFrames and handle NaN/Inf
        clean_counts = {}
        for k, v in counts_dict.items():
            if isinstance(v, pd.DataFrame):
                continue  # Skip DataFrames
            elif isinstance(v, dict):
                # Recursively clean nested dicts
                clean_counts[k] = cls._clean_dict_for_json(v)
            elif isinstance(v, (np.integer, np.floating)):
                # Convert numpy types to Python types
                clean_counts[k] = cls._safe_float(v) if isinstance(v, np.floating) else int(v)
            elif isinstance(v, (int, float)):
                clean_counts[k] = cls._safe_float(v) if isinstance(v, float) else v
            else:
                clean_counts[k] = v
        
        # Clean processing_times
        clean_times = {}
        if processing_times:
            for k, v in processing_times.items():
                if isinstance(v, (float, np.floating)):
                    clean_times[k] = cls._safe_float(v)
                else:
                    clean_times[k] = v
        
        # Prepare data for JSON serialization
        plot_data = {
            'timestamp': datetime.now().isoformat(),
            'mode': mode,
            'limit_value': cls._safe_float(limit_value) if limit_value is not None else None,
            'total_stars': int(total_stars),
            'temp_valid': int(temp_valid),
            'temp_missing': int(temp_missing),
            'lum_valid': int(lum_valid),
            'lum_missing': int(lum_missing),
            'catalog_counts': catalog_counts,
            'magnitude_stats': mag_stats,
            'counts_dict': clean_counts,
            'processing_times': clean_times
        }
        
        # Save to file
        try:
            with open(cls.EXCHANGE_FILE, 'w') as f:
                json.dump(plot_data, f, indent=2)
            print(f"Plot data saved to {cls.EXCHANGE_FILE}")
        except Exception as e:
            print(f"Error saving plot data: {e}")
            # Try to save a minimal version
            try:
                minimal_data = {
                    'timestamp': datetime.now().isoformat(),
                    'mode': mode,
                    'limit_value': limit_value,
                    'total_stars': total_stars,
                    'error': str(e)
                }
                with open(cls.EXCHANGE_FILE, 'w') as f:
                    json.dump(minimal_data, f, indent=2)
                print(f"Saved minimal plot data due to error")
            except:
                print(f"Could not save any plot data")

    @classmethod
    def _safe_float(cls, value):
        """Convert float to JSON-safe value, handling NaN and Inf."""
        if value is None:
            return None
        if isinstance(value, (np.integer, np.floating)):
            value = float(value)
        if isinstance(value, float):
            if np.isnan(value):
                return None  # Or use 0.0 or a placeholder
            elif np.isinf(value):
                return None  # Or use a large number like 1e308
            else:
                return value
        return value
    
    @classmethod
    def _clean_dict_for_json(cls, d):
        """Recursively clean a dictionary for JSON serialization."""
        if not isinstance(d, dict):
            return d
        
        clean = {}
        for k, v in d.items():
            if isinstance(v, pd.DataFrame):
                continue  # Skip DataFrames
            elif isinstance(v, dict):
                clean[k] = cls._clean_dict_for_json(v)
            elif isinstance(v, (np.integer, np.floating)):
                clean[k] = cls._safe_float(v) if isinstance(v, np.floating) else int(v)
            elif isinstance(v, float):
                clean[k] = cls._safe_float(v)
            else:
                clean[k] = v
        return clean

    @classmethod
    def load_plot_data(cls) -> Dict:
        """Load the last plot data. Called from GUI."""
        if not os.path.exists(cls.EXCHANGE_FILE):
            print(f"Plot data file not found: {cls.EXCHANGE_FILE}")
            return None
        
        try:
            with open(cls.EXCHANGE_FILE, 'r') as f:
                data = json.load(f)
            print(f"Successfully loaded plot data from {cls.EXCHANGE_FILE}")
            return data
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from {cls.EXCHANGE_FILE}: {e}")
            # Try to show what's in the file for debugging
            try:
                with open(cls.EXCHANGE_FILE, 'r') as f:
                    content = f.read()
                print(f"File content (first 200 chars): {content[:200]}")
            except:
                pass
            return None
        except Exception as e:
            print(f"Error loading plot data: {e}")
            return None