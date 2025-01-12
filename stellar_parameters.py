# stellar_parameters.py

import numpy as np
import re
from constants import spectral_subclass_temps  # Import the spectral subclass temperatures

def estimate_temperature_from_spectral_type(sp_type):
    """
    Estimate effective temperature from spectral type.

    Parameters:
        sp_type (str): Spectral type string.

    Returns:
        float: Estimated effective temperature in Kelvin, or np.nan if unavailable.
    """
    if sp_type is None or not isinstance(sp_type, str):
        return np.nan
        
    sp_type = sp_type.strip().upper()
    
    # Extract spectral class and subclass
    match = re.match(r'^([OBAFGKMLT])(?:\s*)(\d+(\.\d+)?|[A-Za-z\-]+)?', sp_type)
    if match:
        spectral_class = match.group(1)
        subclass_str = match.group(2)
        
        temps = spectral_subclass_temps.get(spectral_class)
        if temps:
            temp_start = temps.get(0)
            temp_end = temps.get(9)
            
            if temp_start is None or temp_end is None:
                return np.nan
                
            if subclass_str:
                try:
                    subclass = float(subclass_str)
                    # Linear interpolation
                    T_eff = temp_start - (temp_start - temp_end) * (subclass / 9.0)
                    return T_eff
                except ValueError:
                    # For non-numeric subclasses, use weighted average favoring the cooler temperature
                    return (temp_start + 2 * temp_end) / 3
            else:
                # No subclass, use weighted average
                return (temp_start + 2 * temp_end) / 3
    return np.nan

def calculate_bv_temperature(B_V):
    """
    Calculate temperature from B-V color index using Ballesteros' formula.

    Parameters:
        B_V (float): B-V color index.

    Returns:
        float: Estimated effective temperature in Kelvin, or np.nan if unavailable.
    """
    if np.isnan(B_V):
        return np.nan
        
    try:
        T_eff = 4600 * ((1 / (0.92 * B_V + 1.7)) + (1 / (0.92 * B_V + 0.62)))
        
        # Validity range for B-V method
        if T_eff < 1300 or T_eff > 50000:
            return np.nan
            
        return T_eff
    except:
        return np.nan

def select_best_temperature(T_eff_BV, T_eff_sptype):
    """
    Select the best temperature estimate based on various criteria.

    Parameters:
        T_eff_BV (float): Temperature estimated from B-V color index.
        T_eff_sptype (float): Temperature estimated from spectral type.

    Returns:
        tuple: (Selected temperature, source of temperature)
            - float: Selected temperature in Kelvin.
            - str: Source of temperature ('bv_matched', 'bv_only', 'spectral_type_only', etc.)
    """
    if np.isnan(T_eff_BV) and np.isnan(T_eff_sptype):
        return np.nan, 'none'
        
    # For very hot stars (O and early B types), prefer spectral type
    if not np.isnan(T_eff_sptype) and T_eff_sptype > 25000:
        return T_eff_sptype, 'spectral_type_hot'
        
    # For very cool stars (late M and L types), prefer spectral type
    if not np.isnan(T_eff_sptype) and T_eff_sptype < 2400:
        return T_eff_sptype, 'spectral_type_cool'
        
    # If we only have one method, use it
    if np.isnan(T_eff_BV):
        return T_eff_sptype, 'spectral_type_only'
    if np.isnan(T_eff_sptype):
        return T_eff_BV, 'bv_only'
        
    # For intermediate temperatures, compare both methods
    temp_diff_pct = abs(T_eff_BV - T_eff_sptype) / T_eff_sptype
    if temp_diff_pct <= 0.2:  # Within 20%
        return T_eff_BV, 'bv_matched'  # Prefer B-V when methods agree
    else:
        # When methods disagree significantly, prefer spectral type
        return T_eff_sptype, 'spectral_type_disagreement'

def debug_orionis_stars(data, stage=""):
    """Debug function to compare Epsilon and Zeta Orionis data through processing stages."""
    # Import the calculation functions at the start
    from stellar_parameters import calculate_bv_temperature, estimate_temperature_from_spectral_type, select_best_temperature
    import re

    # HIP IDs: Epsilon = 26311, Zeta = 26727
    eps_ori = data[data['HIP'] == 26311]
    zet_ori = data[data['HIP'] == 26727]
    
    print(f"\nOrionis stars comparison at {stage}:")
    print("=" * 50)
    
    columns = ['HIP', 'Vmag', 'B_mag', 'V_mag', 'Spectral_Type', 'B_V']
    
    print(f"{'Parameter':<15} {'Epsilon Ori':<20} {'Zeta Ori':<20}")
    print("-" * 55)
    
    for col in columns:
        eps_val = eps_ori[col][0] if len(eps_ori) > 0 and col in eps_ori.colnames else "Not in dataset"
        zet_val = zet_ori[col][0] if len(zet_ori) > 0 and col in zet_ori.colnames else "Not in dataset"
        print(f"{col:<15} {str(eps_val):<20} {str(zet_val):<20}")
    
    if len(eps_ori) > 0 and len(zet_ori) > 0:
        print("\nDetailed temperature selection process:")
        for star_data, name in [(eps_ori, "Epsilon Ori"), (zet_ori, "Zeta Ori")]:
            print(f"\n{name}:")
            sp_type = star_data['Spectral_Type'][0]
            
            # Try B-V temperature first
            if 'B_V' in star_data.colnames:
                bv = star_data['B_V'][0]
            else:
                # Calculate B-V from magnitudes
                b_mag = star_data['B_mag'][0]
                v_mag = star_data['V_mag'][0]
                bv = b_mag - v_mag
            print(f"Calculated B-V: {bv}")
            try:
                T_eff_BV = calculate_bv_temperature(bv)
                print(f"B-V temperature result: {T_eff_BV}")
            except Exception as e:
                print(f"B-V temperature calculation error: {str(e)}")
                T_eff_BV = np.nan
            
            # Try spectral type temperature
            try:
                T_eff_sptype = estimate_temperature_from_spectral_type(sp_type)
                print(f"Spectral type: {sp_type}")
                print(f"Spectral type temperature result: {T_eff_sptype}")
            except Exception as e:
                print(f"Spectral type calculation error: {str(e)}")
                T_eff_sptype = np.nan
            
            # Show final selection
            try:
                T_eff, source = select_best_temperature(T_eff_BV, T_eff_sptype)
                print(f"Final selected temperature: {T_eff} (source: {source})")
            except Exception as e:
                print(f"Temperature selection error: {str(e)}")

    # Show final temperature and luminosity if present
    if 'Temperature' in data.colnames or 'Luminosity' in data.colnames:
        print("\nFinal calculated values:")
        for param in ['Temperature', 'Luminosity']:
            if param in data.colnames:
                eps_val = eps_ori[param][0] if len(eps_ori) > 0 else "Not calculated"
                zet_val = zet_ori[param][0] if len(zet_ori) > 0 else "Not calculated"
                print(f"{param:<15} {str(eps_val):<20} {str(zet_val):<20}")
    
    # Additional parameters if present
    for param in ['Temperature', 'Luminosity']:
        if param in data.colnames:
            eps_val = eps_ori[param][0] if len(eps_ori) > 0 else "Not calculated"
            zet_val = zet_ori[param][0] if len(zet_ori) > 0 else "Not calculated"
            print(f"{param:<15} {str(eps_val):<20} {str(zet_val):<20}")
    
    # Check specific conditions for temperature calculation
    if 'B_V' in data.colnames and 'Spectral_Type' in data.colnames:
        print("\nTemperature calculation parameters:")
        for star_data, name in [(eps_ori, "Epsilon Ori"), (zet_ori, "Zeta Ori")]:
            if len(star_data) > 0:
                bv = star_data['B_V'][0]
                sp_type = star_data['Spectral_Type'][0]
                print(f"\n{name}:")
                print(f"B-V value: {bv} ({'Valid' if not np.isnan(bv) else 'Invalid'})")
                print(f"Spectral Type: {sp_type} ({'Valid' if sp_type else 'Invalid'})")
                
                # Test temperature estimation methods
                if not np.isnan(bv):
                    from stellar_parameters import calculate_bv_temperature
                    print(f"B-V temperature: {calculate_bv_temperature(bv)}")
                if sp_type:
                    from stellar_parameters import estimate_temperature_from_spectral_type
                    print(f"Spectral type temperature: {estimate_temperature_from_spectral_type(sp_type)}")

def calculate_stellar_parameters(combined_data):
    """Calculate stellar parameters with parallel debugging of both Orionis stars.
     Includes special handling for bright stars with missing luminosity.
    
    Parameters:
        combined_data (astropy Table): Table containing combined star data.

    Returns:
        combined_data (astropy Table): Updated table with new parameters added.
        source_counts (dict): Counts of temperature determination sources.
        estimation_results (dict): Counts of missing and estimated parameters.
        """
    
    print("\nStarting stellar parameter calculations...")
    debug_orionis_stars(combined_data, "start of parameter calculation")
    
    # After calculating B-V
    debug_orionis_stars(combined_data, "after B-V calculation")
    
    # After temperature calculation
    debug_orionis_stars(combined_data, "after temperature calculation")
    
    # After luminosity calculation
    debug_orionis_stars(combined_data, "after luminosity calculation")

    M_sun = 4.83  # Absolute magnitude of the Sun

    # Absolute magnitude estimates by spectral type and luminosity class
    abs_mag_estimates = {
        'I': {  # Supergiants
            'O': -6.4, 'B': -6.0, 'A': -5.8,
            'F': -5.6, 'G': -5.1, 'K': -4.6, 'M': -4.1
        },
        'II': {  # Bright Giants
            'O': -5.5, 'B': -4.8, 'A': -4.3,
            'F': -3.9, 'G': -3.5, 'K': -3.1, 'M': -2.6
        },
        'III': {  # Giants
            'O': -4.5, 'B': -3.5, 'A': -2.8,
            'F': -2.4, 'G': -2.1, 'K': -1.6, 'M': -1.2
        }
    }

    distance_pc = combined_data['Distance_pc']
    V_mag = combined_data['V_mag']
    B_mag = combined_data['B_mag']
    spectral_types = combined_data['Spectral_Type']

    # Initialize arrays for calculated values
    M_V_list = []
    luminosity_list = []
    B_V_list = []
    temperature_list = []
    temperature_sources = []
    luminosity_estimated = []  # Track which luminosities are estimated

    # Initialize counts for estimation results
    initial_missing_temp = 0
    recovered_temp = 0
    final_missing_temp = 0
    initial_missing_lum = 0
    recovered_lum = 0
    final_missing_lum = 0
    bright_star_estimates = 0

    print("Processing stellar parameters for each star...")

    for i in range(len(combined_data)):
        # Initialize values
        M_V = np.nan
        L_Lsun = np.nan
        B_V = np.nan
        is_estimated = False

        dist_pc = distance_pc[i]
        Vmag = V_mag[i]
        Bmag = B_mag[i]
        sp_type = spectral_types[i]

        # Calculate Absolute Magnitude and Luminosity
        if not np.isnan(Vmag) and dist_pc > 0:
            M_V = Vmag - 5 * (np.log10(dist_pc) - 1)
            if not np.isnan(M_V):
                L_Lsun = 10 ** ((M_sun - M_V) / 2.5)
        else:
            initial_missing_lum += 1

        # If luminosity is missing and star is bright (Vmag ≤ 2.5), attempt estimation
        if np.isnan(L_Lsun) and Vmag is not None and Vmag <= 2.5 and sp_type is not None:
            try:
                sp_type = str(sp_type).strip().upper()
                spectral_class = sp_type[0] if sp_type[0] in 'OBAFGKM' else None
                
                # Extract luminosity class
                lum_class = None
                for cls in ['I', 'II', 'III']:
                    if cls in sp_type:
                        lum_class = cls
                        break

                if spectral_class and lum_class and lum_class in abs_mag_estimates:
                    estimated_M_V = abs_mag_estimates[lum_class][spectral_class]
                    L_Lsun = 10 ** ((M_sun - estimated_M_V) / 2.5)
                    is_estimated = True
                    bright_star_estimates += 1

                    if is_estimated:
                        print(f"\nLuminosity estimated for star:")
                        print(f"  Name: {combined_data['Star_Name'][i]}")
                        print(f"  Source Catalog: {combined_data['Source_Catalog'][i]}")
                        print(f"  Vmag: {Vmag:.3f}")
                        print(f"  Spectral Type: {sp_type}")
                        print(f"  Estimated Luminosity: {L_Lsun:.2f} Lsun")
                        print(f"  Temperature: {T_eff:.0f} K")
                        print(f"  Distance: {combined_data['Distance_pc'][i]:.1f} pc ({combined_data['Distance_ly'][i]:.1f} ly)")
                        if 'P' in str(sp_type).upper() or 'VAR' in str(sp_type).upper():
                            print("  Note: Star is peculiar/variable")

                    # Special handling for peculiar stars
                    if 'P' in sp_type.upper() or 'VAR' in sp_type.upper():
                        combined_data.meta['peculiar_star_note'] = combined_data.meta.get('peculiar_star_note', '') + \
                            f"\nNote: {combined_data['Star_Name'][i]} has peculiar or variable characteristics; " \
                            f"luminosity estimate may have higher uncertainty."
            except Exception as e:
                print(f"Error estimating luminosity for bright star {combined_data['Star_Name'][i]}: {e}")

        # Calculate B-V Color Index
        if not np.isnan(Vmag) and not np.isnan(Bmag):
            B_V = Bmag - Vmag

        # Store B-V for temperature calculation
        B_V_list.append(B_V)

        # Calculate temperatures using both methods
        T_eff_BV = calculate_bv_temperature(B_V)
        T_eff_sptype = estimate_temperature_from_spectral_type(sp_type)

        # Check if initial temperatures are missing
        if np.isnan(T_eff_BV) and np.isnan(T_eff_sptype):
            initial_missing_temp += 1

        # Select best temperature
        T_eff, temp_source = select_best_temperature(T_eff_BV, T_eff_sptype)

        # Check if temperature was recovered
        if not np.isnan(T_eff):
            recovered_temp += 1
        else:
            final_missing_temp += 1

        # Append calculated values
        M_V_list.append(M_V)
        luminosity_list.append(L_Lsun)
        temperature_list.append(T_eff)
        temperature_sources.append(temp_source)
        luminosity_estimated.append(is_estimated)

    # Assign calculated values to combined_data
    combined_data['Abs_Mag'] = M_V_list
    combined_data['Luminosity'] = luminosity_list
    combined_data['B_V'] = B_V_list
    combined_data['Temperature'] = temperature_list
    combined_data['Luminosity_Estimated'] = luminosity_estimated

    # Convert Temperature column to float
    combined_data['Temperature'] = combined_data['Temperature'].astype(float)

    # Calculate detailed statistics
    source_counts = {
        'bv_matched': temperature_sources.count('bv_matched'),
        'bv_only': temperature_sources.count('bv_only'),
        'spectral_type_hot': temperature_sources.count('spectral_type_hot'),
        'spectral_type_cool': temperature_sources.count('spectral_type_cool'),
        'spectral_type_only': temperature_sources.count('spectral_type_only'),
        'spectral_type_disagreement': temperature_sources.count('spectral_type_disagreement'),
        'none': temperature_sources.count('none')
    }

    # Calculate recovered and final missing luminosities
    recovered_lum = len(combined_data) - initial_missing_lum + bright_star_estimates
    final_missing_lum = np.sum(np.isnan(luminosity_list))

    # Print temperature determination statistics
    print("\nTemperature Determination Statistics:")
    for source, count in source_counts.items():
        print(f"{source.replace('_', ' ').title()}: {count}")

    print(f"\nParameter calculation summary:")
    print(f"Total stars processed: {len(combined_data)}")
    print(f"Stars with valid temperatures: {recovered_temp}")
    print(f"Stars with valid luminosities: {len(combined_data) - final_missing_lum}")
    print(f"Stars with estimated luminosities: {bright_star_estimates}")
    print(f"Stars with valid B-V colors: {np.sum(~np.isnan(combined_data['B_V']))}")

    estimation_results = {
        'initial_missing_temp': initial_missing_temp,
        'recovered_temp': recovered_temp,
        'final_missing_temp': final_missing_temp,
        'initial_missing_lum': initial_missing_lum,
        'recovered_lum': recovered_lum,
        'final_missing_lum': final_missing_lum,
        'bright_star_estimates': bright_star_estimates
    }

    return combined_data, source_counts, estimation_results
