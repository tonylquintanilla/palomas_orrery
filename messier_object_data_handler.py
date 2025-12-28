# messier_object_data_handler.py

from astropy.coordinates import SkyCoord
import astropy.units as u
import pandas as pd
import numpy as np
from messier_catalog import (messier_catalog, 
                            star_cluster_catalog, 
                            get_nebulae, 
                            get_star_clusters,
                            bright_planetaries, 
                            bright_nebulae, 
                            bright_open_clusters,
                            get_all_bright_objects
                            )
from star_notes import unique_notes

class MessierObjectHandler:
    """Handles all Messier object related operations."""
    
    def __init__(self):
        """Initialize with both nebulae and star cluster catalogs."""
        self.nebulae = get_nebulae()
        self.clusters = get_star_clusters()
        
    def get_visible_objects(self, mag_limit, object_type=None):
        """
        Get Messier objects visible up to specified magnitude limit.
        
        Parameters:
            mag_limit (float): Maximum apparent magnitude to include
            object_type (str, optional): Filter by object type 
                ('Nebula', 'Cluster', 'Planetary', 'Emission', etc.)
        
        Returns:
            list: List of visible objects matching criteria
        """
        visible_objects = []
        
        print(f"\nFiltering Messier objects to magnitude {mag_limit}")
        
        # Process both catalogs
        for catalog in [self.nebulae, self.clusters]:
            for messier_id, data in catalog.items():
                if data['vmag'] <= mag_limit:
                    if object_type is None or object_type.lower() in data['type'].lower():
                        obj_data = {
                            'messier_id': messier_id,
                            'name': data['name'],
                            'type': data['type'],
                            'vmag': data['vmag'],
                            'distance_ly': data['distance_ly'],
                            'ra': data['ra'],
                            'dec': data['dec'],
                            'ra_str': data['ra'],  # Original string format like '05h34m31.94s'
                            'dec_str': data['dec'], # Original string format like '+22 deg00 arcmin52.2 arcsec'                            
                            'notes': data.get('notes', ''),
                            'size': data.get('size', None),
                            'age': data.get('age', None),
                            'parent_constellation': data.get('constellation', None)
                        }
                        visible_objects.append(obj_data)
        
        print(f"Found {len(visible_objects)} visible Messier objects")
        if object_type:
            print(f"(Filtered to type: {object_type})")
            
        return visible_objects
    
    def calculate_3d_coordinates(self, objects):
        """
        Calculate x, y, z coordinates for Messier objects.
        
        Parameters:
            objects (list): List of Messier objects with ra, dec, and distance
            
        Returns:
            list: Objects with added x, y, z coordinates in light-years
        """
        for obj in objects:
            try:
                # Parse coordinates
                coords = SkyCoord(obj['ra'], obj['dec'], unit=(u.hourangle, u.deg))
                distance_pc = obj['distance_ly'] / 3.26156
                
                # Create 3D coordinates
                coord_with_dist = SkyCoord(
                    ra=coords.ra,
                    dec=coords.dec,
                    distance=distance_pc * u.pc
                )
                
                # Convert to light-years
                obj['x'] = coord_with_dist.cartesian.x.value * 3.26156
                obj['y'] = coord_with_dist.cartesian.y.value * 3.26156
                obj['z'] = coord_with_dist.cartesian.z.value * 3.26156
                
            except Exception as e:
                print(f"Error calculating coordinates for {obj['messier_id']}: {e}")
                obj['x'] = obj['y'] = obj['z'] = np.nan
        
        return objects
    
    def get_visible_objects(self, mag_limit, object_type=None):
        """
        Get Messier objects visible up to specified magnitude limit.
        
        Parameters:
            mag_limit (float): Maximum apparent magnitude to include
            object_type (str, optional): Filter by object type 
                ('Nebula', 'Cluster', 'Planetary', 'Emission', etc.)
        
        Returns:
            list: List of visible objects matching criteria
        """
        visible_objects = []
        
        print(f"\nFiltering Messier objects to magnitude {mag_limit}")
        
        # Process both catalogs
        for catalog in [self.nebulae, self.clusters]:
            for messier_id, data in catalog.items():
                if data['vmag'] <= mag_limit:
                    if object_type is None or object_type.lower() in data['type'].lower():
                        # Parse RA and Dec from string format to degrees
                        coords = SkyCoord(data['ra'], data['dec'], frame='icrs')
                        
                        obj_data = {
                            'messier_id': messier_id,
                            'name': data['name'],
                            'type': data['type'],
                            'vmag': data['vmag'],
                            'distance_ly': data['distance_ly'],
                            'ra': coords.ra.deg,      # Converted to degrees for calculations
                            'dec': coords.dec.deg,    # Converted to degrees for calculations
                            'ra_str': data['ra'],     # Keep original string for display
                            'dec_str': data['dec'],   # Keep original string for display                            
                            'notes': data.get('notes', ''),
                            'size': data.get('size', None),
                            'age': data.get('age', None),
                            'parent_constellation': data.get('constellation', None)
                        }
                        visible_objects.append(obj_data)
        
        print(f"Found {len(visible_objects)} visible Messier objects")
        if object_type:
            print(f"(Filtered to type: {object_type})")
            
        return visible_objects

    def create_dataframe(self, objects):
        """Convert Messier objects to DataFrame format compatible with stellar data."""
        if not objects:
            return pd.DataFrame()
                
        # Calculate coordinates for each object
        print("\nCalculating coordinates for Messier objects...")
        for obj in objects:
            try:
                # Parse coordinates
        #        coords = SkyCoord(obj['ra'], obj['dec'], unit=(u.hourangle, u.deg))

                coords = SkyCoord(
                    ra=obj['ra'],
                    dec=obj['dec'],
                    unit=(u.deg, u.deg),
                    frame='icrs'
                )

                distance_pc = obj['distance_ly'] / 3.26156
                
                # Create 3D coordinates
                coord_with_dist = SkyCoord(
                    ra=coords.ra,
                    dec=coords.dec,
                    distance=distance_pc * u.pc,
                    frame='icrs'
                )
                
                # Convert to cartesian coordinates
                cart = coord_with_dist.cartesian

                # Convert to light-years and store
                obj['x'] = cart.x.value * 3.26156
                obj['y'] = cart.y.value * 3.26156
                obj['z'] = cart.z.value * 3.26156
                
                print(f"  {obj['messier_id']}: Calculated coordinates ({obj['x']:.1f}, {obj['y']:.1f}, {obj['z']:.1f}) ly")
                
            except Exception as e:
                print(f"Error calculating coordinates for {obj['messier_id']}: {e}")
                obj['x'] = obj['y'] = obj['z'] = np.nan
                
        # Create DataFrame
        df = pd.DataFrame(objects)
        
        # Add required columns to match stellar data format
        df['Star_Name'] = df.apply(lambda row: f"{row['messier_id']}: {row['name']}", axis=1)
    #    df['Star_Name'] = df['name']
        df['Source_Catalog'] = 'Messier'
        df['Apparent_Magnitude'] = df['vmag']
        df['Distance_pc'] = df['distance_ly'] / 3.26156
        df['Distance_ly'] = df['distance_ly']
        df['Object_Type'] = df['type']
        df['Object_Type_Desc'] = df.apply(self._create_type_description, axis=1)
        
        # Add null values for stellar-specific columns
        df['Temperature'] = np.nan
        df['Temperature_Method'] = 'none'  # Added for compatibility
        df['Temperature_Normalized'] = 0.5  # Middle value for color scale
        df['Luminosity'] = np.nan
        df['Luminosity_Estimated'] = False  # Added for compatibility
        df['B_V'] = np.nan
        df['Spectral_Type'] = None
        df['Abs_Mag'] = np.nan  # Added for compatibility
        
        # Add visualization properties
        df['Marker_Size'] = 20  # Fixed larger size for non-stellar objects
        
        # Create hover texts
        df['Hover_Text'] = df.apply(
            lambda row: (
                f"<b>{row['messier_id']}: {row['name']}</b><br>"
        #        f"<b>{row['Star_Name']}</b><br>"
                f"Type: {row['type']}<br>"
        #        f"Apparent Magnitude: {row['Apparent_Magnitude']:.1f}<br>"
                f"Apparent Magnitude: {row['vmag']:.1f}<br>"
        #        f"Distance: {row['Distance_ly']:.1f} ly<br>"
                f"Distance: {row['Distance_pc']:.2f} pc ({row['Distance_ly']:.2f} ly)<br>"
        #        f"Position: ({row['x']:.1f}, {row['y']:.1f}, {row['z']:.1f}) ly<br>"
                f"RA: {row['ra_str']}, Dec: {row['dec_str']} (J2000)<br>"
                f"{unique_notes.get(row['messier_id'], 'None')}<br>"  # Use unique_notes with messier_id
        #        f"Notes: {row['notes']}"
            ),
            axis=1
        )
        df['Min_Hover_Text'] = df.apply(
            lambda row: f"<b>{row['messier_id']}</b>", 
    #        lambda row: f"<b>{row['Star_Name']}</b>", 
            axis=1)
        
        print(f"\nProcessed {len(df)} Messier objects with columns:")
        print(df.columns.tolist())
        
        return df

    def _calculate_marker_size(self, vmag):         # obsolete
        """Calculate marker sizes based on apparent magnitude."""
        def calc_size(mag):
            if pd.isna(mag):
                return 20  # Default size for Messier objects
            mag_min, mag_max = -1.44, 9.0
            size_min, size_max = 2, 24
            mag_clipped = np.clip(mag, mag_min, mag_max)
            log_brightness = -0.4 * mag_clipped
            log_brightness_min = -0.4 * mag_max
            log_brightness_max = -0.4 * mag_min
            normalized_brightness = (log_brightness - log_brightness_min) / (log_brightness_max - log_brightness_min)
            return np.clip(size_min + (size_max - size_min) * normalized_brightness, size_min, size_max)
        
        return vmag.apply(calc_size)

    def _create_hover_text(self, row):      # used?
        """Create hover text for a Messier object."""
        text = [
            f"<b>{row['messier_id']}: {row['name']}</b>",
            f"Type: {row['type']}",
            f"Apparent Magnitude: {row['vmag']:.1f}",
            f"Distance: {row['distance_ly']:.1f} light-years",
        #    f"Position: ({row['x']:.1f}, {row['y']:.1f}, {row['z']:.1f}) ly"
            f"RA: {row['ra_str']}, Dec: {row['dec_str']} (J2000)<br>"
            f"{unique_notes.get(row['messier_id'], 'None')}<br>"  # Use unique_notes with messier_id
        ]
        
        if 'size' in row and pd.notna(row['size']):
            text.append(f"Size: {row['size']}")
        if 'age' in row and pd.notna(row['age']):
            text.append(f"Age: {row['age']}")
        if 'notes' in row and pd.notna(row['notes']):
            text.append(f"Notes: {row['notes']}")
            
        return '<br>'.join(text)
    
    def _create_type_description(self, row):
        """Create detailed type description."""
        desc = row['type']
        if row.get('age'):
            desc += f", Age: {row['age']}"
        if row.get('size'):
            desc += f", Size: {row['size']}"
        return desc
    
    def _get_marker_symbol(self, obj_type):     # I don't think we use this function. all objects look the same. 
            """
            Get appropriate marker symbol based on object type.
            Uses only symbols available in Plotly's Scatter3d:
            - 'circle'
            - 'square'
            - 'diamond'
            - 'cross'
            - 'x'
            - 'triangle-up'
            - 'triangle-down'
            """
            if 'Nebula' in obj_type:
                return 'diamond'  # Compatible with Scatter3d
            elif 'HII Region' in obj_type:
                return 'square'   # Changed from 'diamond' for distinction
            elif 'Cluster' in obj_type:
                return 'triangle-up'  # Changed from 'cross' for better visibility
            elif 'Planetary' in obj_type:
                return 'circle'  # Specific symbol for planetary nebulae
            elif 'Supernova' in obj_type:
                return 'cross'  # Specific symbol for supernova remnants
            return 'diamond'  # Default symbol
    
    def _get_marker_color(self, obj_type):          # I don't think we use this function. all objects look the same. 
        """Get appropriate color based on object type."""
        if 'Emission' in obj_type or 'HII Region' in obj_type:
            return 'red'
        elif 'Planetary' in obj_type:
            return 'green'
        elif 'Reflection' in obj_type:
            return 'blue'
        elif 'Cluster' in obj_type:
            return 'yellow'
        return 'white'
    
    def get_object_info(self, messier_id):
        """Get detailed information for a specific Messier object."""
        obj = self.nebulae.get(messier_id) or self.clusters.get(messier_id)
        if not obj:
            return "Object not found in catalog"
            
        info = [
            f"{messier_id}",
            f"Name: {obj['name']}",
            f"Type: {obj['type']}",
            f"Apparent Magnitude: {obj['vmag']}",
            f"Distance: {obj['distance_ly']} light-years"
        ]
        
        if 'size' in obj:
            info.append(f"Size: {obj['size']}")
        if 'age' in obj:
            info.append(f"Age: {obj['age']}")
        if 'constellation' in obj:
            info.append(f"Constellation: {obj['constellation']}")
        if 'notes' in obj:
            info.append(f"Notes: {obj['notes']}")
            
        return '\n'.join(info)
    
    def analyze_catalog(self):
        """Analyze the catalog contents."""
        total_objects = len(self.nebulae) + len(self.clusters)
        type_counts = {}
        mag_distribution = []
        
        for obj in list(self.nebulae.values()) + list(self.clusters.values()):
            # Count object types
            obj_type = obj['type']
            type_counts[obj_type] = type_counts.get(obj_type, 0) + 1
            
            # Collect magnitudes
            mag_distribution.append(obj['vmag'])
        
        print("\nNon-stellar Object Catalog Analysis")
        print("=" * 50)
        print(f"Total Objects: {total_objects}")
        print("\nObject Types:")
        for obj_type, count in sorted(type_counts.items()):
            print(f"  {obj_type}: {count}")
            
        if mag_distribution:
            print("\nMagnitude Statistics:")
            print(f"  Brightest: {min(mag_distribution):.1f}")
            print(f"  Faintest: {max(mag_distribution):.1f}")
            print(f"  Average: {np.mean(mag_distribution):.1f}")