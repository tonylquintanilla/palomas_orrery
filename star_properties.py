import os
import pickle
import time
import re
from astroquery.simbad import Simbad
import numpy as np
from simbad_manager import SimbadQueryManager, SimbadConfig

# Replace query_simbad_for_star_properties with the one from enhanced_star_properties.py

def parse_magnitude(value):
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return float(value)
    value_str = str(value)
    # remove anything like “ [~]” or “[some text]”
    cleaned = re.sub(r"\[.*?\]", "", value_str).strip()
    try:
        return float(cleaned)
    except ValueError:
        return None


def load_existing_properties(properties_file):
    """Load existing star and Messier object properties from a file."""
    if os.path.exists(properties_file):
        print("Loading properties from local file...")
        try:
            with open(properties_file, 'rb') as f:
                data = pickle.load(f)
            
            # Verify required keys are present
            required_keys = {
                'unique_ids', 'star_names', 'spectral_types', 
                'V_magnitudes', 'B_magnitudes', 'object_types'
            }
            
            if not required_keys.issubset(data.keys()):
                print("Error: Missing required keys in properties file.")
                return {}
                
            # Create dictionary of properties
            existing_properties = {}
            for i in range(len(data['unique_ids'])):
                uid = data['unique_ids'][i]
                
                # Build properties dictionary with core fields
                props = {
                    'star_name': data['star_names'][i],
                    'spectral_type': data['spectral_types'][i],
                    'V_magnitude': data['V_magnitudes'][i],
                    'B_magnitude': data['B_magnitudes'][i],
                    'object_type': data['object_types'][i],
                }
                
                # Add Messier-specific fields if present
                if 'is_messier' in data:
                    props['is_messier'] = data['is_messier'][i]
                    if data['is_messier'][i]:
                        props['distance_ly'] = data.get('distance_ly', [None] * len(data['unique_ids']))[i]
                        props['notes'] = data.get('notes', [''] * len(data['unique_ids']))[i]
                
                existing_properties[uid] = props
            
            # Report statistics
            messier_count = sum(1 for props in existing_properties.values() if props.get('is_messier', False))
            print(f"Loaded {len(existing_properties)} objects ({messier_count} Messier objects)")
            
            return existing_properties
            
        except Exception as e:
            print(f"Error loading properties from file: {e}")
            return {}
    else:
        print("No existing properties file found. Starting fresh.")
        return {}

def generate_unique_ids(combined_data):
    """Generate unique identifiers for all stars consistently."""
    print("Generating unique identifiers...")
    unique_ids = []

    for row in combined_data:
        # First try HIP ID
        uid = None
        if 'HIP' in combined_data.colnames:
            hip = row['HIP']
            if not np.ma.is_masked(hip) and hip is not None:
                try:
                    uid = f"HIP {int(hip)}"
                except (TypeError, ValueError):
                    uid = None

        # Then try Gaia Source ID
        if uid is None and 'Source' in combined_data.colnames:
            source = row['Source']
            if not np.ma.is_masked(source) and source is not None:
                try:
                    uid = f"Gaia DR3 {int(source)}"
                except (TypeError, ValueError):
                    uid = None

        # Finally use coordinates as fallback
        if uid is None and 'RA_ICRS' in combined_data.colnames and 'DE_ICRS' in combined_data.colnames:
            ra = row['RA_ICRS']
            dec = row['DE_ICRS']
            if not np.ma.is_masked(ra) and not np.ma.is_masked(dec):
                uid = f"J{ra:.6f}{dec:+.6f}"

        unique_ids.append(uid)

    print(f"Generated {len([uid for uid in unique_ids if uid is not None])} unique identifiers")
    return unique_ids

def save_properties_to_file(properties, properties_file):
    """Save star properties to file with Messier object support."""
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
        property_lists['star_names'].append(props['star_name'])
        property_lists['spectral_types'].append(props['spectral_type'])
        property_lists['V_magnitudes'].append(props['V_magnitude'])
        property_lists['B_magnitudes'].append(props['B_magnitude'])
        property_lists['object_types'].append(props['object_type'])
        property_lists['is_messier'].append(props.get('is_messier', False))
        property_lists['distance_ly'].append(props.get('distance_ly', None))
        property_lists['notes'].append(props.get('notes', ''))
    
    with open(properties_file, 'wb') as f:
        pickle.dump(property_lists, f)

def create_custom_simbad():
    custom_simbad = Simbad()
    # Reset to the standard defaults, which typically include 'MAIN_ID'
    custom_simbad.reset_votable_fields()
    custom_simbad.ROW_LIMIT = 1
    custom_simbad.TIMEOUT = 300
    
    # Add the extra fields you need for your script
    custom_simbad.add_votable_fields('ids', 'sp', 'flux(V)', 'flux(B)', 'otype')
    return custom_simbad

def query_simbad_for_star_properties(missing_ids, existing_properties, properties_file):
    """Query Simbad for missing star properties."""
    print(f"\nQuerying Simbad for {len(missing_ids)} missing star properties...")
    try:
        # Initialize supplemental data from Messier catalog
        from messier_catalog import messier_catalog, star_cluster_catalog
        supplemental_data = {**messier_catalog, **star_cluster_catalog}

    #    custom_simbad = Simbad()
        custom_simbad = create_custom_simbad()  # use the helper above

    #    custom_simbad.ROW_LIMIT = 1
    #    custom_simbad.TIMEOUT = 300
    #    custom_simbad.add_votable_fields('ids', 'sp', 'flux(V)', 'flux(B)', 'otype')   
        # removed 'dim' because it was causing the Simbad fetch to fail on MAIN_ID 
        # removed deprecated dist, distance is generated from parallax

        # Process in smaller batches to avoid timeouts
        batch_size = 50
        total_batches = (len(missing_ids) + batch_size - 1) // batch_size

        for batch_num in range(total_batches):
            start_idx = batch_num * batch_size
            end_idx = min((batch_num + 1) * batch_size, len(missing_ids))
            batch_ids = missing_ids[start_idx:end_idx]

            print(f"\nProcessing batch {batch_num + 1}/{total_batches} ({start_idx + 1} to {end_idx})")

            for idx, obj_name in enumerate(batch_ids):
                try:
                    # Check if it's a Messier object
                    messier_id = None
                    if obj_name.startswith('M '):
                        messier_id = f"M{obj_name.split()[1]}"
                    
                    # Query SIMBAD first
                    result_table = custom_simbad.query_object(obj_name)
                    
                    if result_table is not None and len(result_table) > 0:
                        # Extract main identifier
                        star_name = result_table['MAIN_ID'][0]
                        star_name = star_name.decode('utf-8') if isinstance(star_name, bytes) else star_name
                        
                        # Get SIMBAD properties
                        sp_type = result_table['SP_TYPE'][0] if 'SP_TYPE' in result_table.colnames else None
                        sp_type = sp_type.decode('utf-8') if isinstance(sp_type, bytes) else sp_type
                        
                        V_mag = result_table['FLUX_V'][0] if 'FLUX_V' in result_table.colnames else None
                        B_mag = result_table['FLUX_B'][0] if 'FLUX_B' in result_table.colnames else None
                        
                        otype = result_table['OTYPE'][0] if 'OTYPE' in result_table.colnames else None
                        otype = otype.decode('utf-8') if isinstance(otype, bytes) else otype
                        
                        # For Messier objects, supplement missing data from our catalog
                        if messier_id and messier_id in supplemental_data:
                            messier_data = supplemental_data[messier_id]
                            print(f"\nSupplementing {messier_id} data from messier_catalog.py:")
                            
                            # Track what data is being supplemented
                            if V_mag is None and 'vmag' in messier_data:
                                V_mag = messier_data['vmag']
                                print(f"  - Using catalog magnitude: {V_mag}")
                            
                            if not otype and 'type' in messier_data:
                                otype = messier_data['type']
                                print(f"  - Using catalog object type: {otype}")
                                
                            star_name = f"{messier_id}: {messier_data['name']}"
                            print(f"  - Using catalog name: {star_name}")
                            
                            if 'distance_ly' in messier_data:
                                print(f"  - Using catalog distance: {messier_data['distance_ly']} ly")
                                
                            if 'notes' in messier_data:
                                print(f"  - Added catalog notes: {messier_data['notes'][:50]}...")
                            
                            # Add Messier-specific properties
                            existing_properties[obj_name] = {
                                'star_name': star_name,
                                'spectral_type': sp_type,
                                'V_magnitude': V_mag,
                                'B_magnitude': B_mag,
                                'object_type': otype,
                                'distance_ly': messier_data['distance_ly'],
                                'notes': messier_data.get('notes', ''),
                                'is_messier': True
                            }
                            print(f"Added Messier object {star_name}")
                        else:
                            # Standard star properties
                            existing_properties[obj_name] = {
                                'star_name': star_name,
                                'spectral_type': sp_type,
                                'V_magnitude': V_mag,
                                'B_magnitude': B_mag,
                                'object_type': otype,
                                'is_messier': False
                            }
                    
                    elif messier_id and messier_id in supplemental_data:
                        # If SIMBAD query failed but we have Messier data
                        messier_data = supplemental_data[messier_id]
                        print(f"\nUsing only messier_catalog.py data for {messier_id} (SIMBAD query failed):")
                        print(f"  - Using catalog magnitude: {messier_data['vmag']}")
                        print(f"  - Using catalog object type: {messier_data['type']}")
                        print(f"  - Using catalog name: {messier_data['name']}")
                        print(f"  - Using catalog distance: {messier_data['distance_ly']} ly")
                        if 'notes' in messier_data:
                            print(f"  - Added catalog notes: {messier_data['notes'][:50]}...")
                            
                        existing_properties[obj_name] = {
                            'star_name': f"{messier_id}: {messier_data['name']}",
                            'spectral_type': None,
                            'V_magnitude': messier_data['vmag'],
                            'B_magnitude': None,
                            'object_type': messier_data['type'],
                            'distance_ly': messier_data['distance_ly'],
                            'notes': messier_data.get('notes', ''),
                            'is_messier': True
                        }
                        print(f"Added Messier object {messier_id} from catalog")
                    
                    else:
                        # No data found in either source
                        existing_properties[obj_name] = {
                            'star_name': obj_name,
                            'spectral_type': None,
                            'V_magnitude': None,
                            'B_magnitude': None,
                            'object_type': None,
                            'is_messier': False
                        }

                except Exception as e:
                    print(f"Error querying {obj_name}: {e}")
                    existing_properties[obj_name] = {
                        'star_name': obj_name,
                        'spectral_type': None,
                        'V_magnitude': None,
                        'B_magnitude': None,
                        'object_type': None,
                        'is_messier': False
                    }

                if (idx + 1) % 10 == 0:
                    print(f"Processed {idx + 1}/{len(batch_ids)} objects in current batch")

                time.sleep(0.1)  # Rate limiting

            # Save progress after each batch
            try:
                save_properties_to_file(existing_properties, properties_file)
                print(f"Saved progress after batch {batch_num + 1}")
            except Exception as e:
                print(f"Error saving batch progress: {e}")

        return existing_properties

    except Exception as e:
        print(f"Error in Simbad query setup: {e}")
        return existing_properties

    except Exception as e:
        print(f"Error in Simbad query setup: {e}")
        return existing_properties

def assign_properties_to_data(combined_data, existing_properties, unique_ids):
    """Assign retrieved properties to the combined data with Messier object support."""
    print("\nAssigning properties to combined data...")
    
    # Initialize property lists
    props_to_assign = {
        'Star_Name': [],
        'Spectral_Type': [],
        'V_mag': [],
        'B_mag': [],
        'Object_Type': [],
        'Is_Messier': [],
        'Distance_ly': [],
        'Notes': []
    }

    # Collect properties for each object
    for uid in unique_ids:
        if uid is not None and uid in existing_properties:
            props = existing_properties[uid]
            props_to_assign['Star_Name'].append(props['star_name'] if props['star_name'] else "Unknown")
            props_to_assign['Spectral_Type'].append(props['spectral_type'])
            props_to_assign['V_mag'].append(float(props['V_magnitude']) if props['V_magnitude'] is not None else np.nan)
            props_to_assign['B_mag'].append(float(props['B_magnitude']) if props['B_magnitude'] is not None else np.nan)
            props_to_assign['Object_Type'].append(props['object_type'])
            props_to_assign['Is_Messier'].append(props.get('is_messier', False))
            props_to_assign['Distance_ly'].append(props.get('distance_ly', None))
            props_to_assign['Notes'].append(props.get('notes', ''))
        else:
            # Default values for missing properties
            props_to_assign['Star_Name'].append("Unknown")
            props_to_assign['Spectral_Type'].append(None)
            props_to_assign['V_mag'].append(np.nan)
            props_to_assign['B_mag'].append(np.nan)
            props_to_assign['Object_Type'].append(None)
            props_to_assign['Is_Messier'].append(False)
            props_to_assign['Distance_ly'].append(None)
            props_to_assign['Notes'].append('')

    # Assign properties to combined_data
    for col_name, values in props_to_assign.items():
        combined_data[col_name] = values

    # Report statistics
    messier_count = sum(props_to_assign['Is_Messier'])
    total_objects = len(unique_ids)
    print(f"Assigned properties to {total_objects} objects ({messier_count} Messier objects)")

    return combined_data
