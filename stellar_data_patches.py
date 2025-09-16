# stellar_data_patches.py
import pandas as pd
import numpy as np

# Format: HIP number -> (temperature_K, luminosity_Lsun, spectral_type, notes)
STELLAR_PATCHES = {
    65378: (9440, 63.0, 'A1V', 'Mizar - quadruple system, Ap star'),    # temperature from Gaia (Gaia DR3 1553901267664488064) 
    # Add other problematic stars as discovered
}

def apply_temperature_patches(data):
    """Apply known fixes for stars with missing or incorrect data."""
    patch_count = 0
    
    for hip_id, (temp, lum, spec_type, notes) in STELLAR_PATCHES.items():
        # Find stars with this HIP ID
        mask = (data['HIP'] == hip_id)
        
        if mask.any():
            # Check what needs patching
            needs_temp = pd.isna(data.loc[mask, 'Temperature'].iloc[0]) or data.loc[mask, 'Temperature'].iloc[0] <= 0
            needs_lum = pd.isna(data.loc[mask, 'Luminosity'].iloc[0]) or data.loc[mask, 'Luminosity'].iloc[0] <= 0
            
            if needs_temp:
                data.loc[mask, 'Temperature'] = temp
                data.loc[mask, 'Temperature_Method'] = 'patched'
                print(f"  Patched temperature for HIP {hip_id}: {temp}K")
            
            if needs_lum:
                data.loc[mask, 'Luminosity'] = lum
                print(f"  Patched luminosity for HIP {hip_id}: {lum} L☉")
            
            # Also patch spectral type if missing
            if 'Spectral_Type' in data.columns and pd.isna(data.loc[mask, 'Spectral_Type'].iloc[0]):
                data.loc[mask, 'Spectral_Type'] = spec_type
            
            if needs_temp or needs_lum:
                patch_count += 1
                print(f"  Patched HIP {hip_id} ({notes})")
    
    if patch_count > 0:
        print(f"Applied patches to {patch_count} stars")
    
    return data