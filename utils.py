# utils.py

import re
import pandas as pd
from constants import class_mapping, object_type_mapping  # Ensure these are defined in constants.py

def parse_luminosity_class(spectral_type):
    """
    Parse the luminosity class from a spectral type string.

    The luminosity class indicates the size and luminosity of a star, represented by Roman numerals in the spectral type.

    Parameters:
        spectral_type (str): The spectral type string of a star (e.g., 'G2V').

    Returns:
        str: The full description of the luminosity class (e.g., 'Main Sequence'), or 'Unknown' if not found.
    """
    if spectral_type is None or pd.isna(spectral_type):
        return "Unknown"
    # Use regular expression to search for luminosity class in spectral type
    match = re.search(r'([IV]+)', str(spectral_type))
    if match:
        luminosity_class = match.group(1)
        # Map the Roman numeral to its description using class_mapping
        return class_mapping.get(luminosity_class, luminosity_class)
    return "Unknown"

def expand_object_type(ot):
    """
    Expands SIMBAD object type codes to full descriptions.

    This function handles multiple object types per star and partial matches.
    It uses the object_type_mapping dictionary to map codes to descriptions.

    Parameters:
        ot (str): The object type code(s) from SIMBAD (e.g., 'Star', 'BYDra', 'RR', etc.).

    Returns:
        str: The expanded description(s) of the object type(s).
    """
    if ot is None:
        return 'Unknown'
    # Split the object type codes by comma, semicolon, or space
    ot_codes = re.split(r'[;, ]+', str(ot))
    descriptions = []
    for code in ot_codes:
        code = code.strip()
        if not code:
            continue
        # Exact match
        if code in object_type_mapping:
            desc = object_type_mapping[code]
        else:
            # Partial match: check if any key in mapping is a substring of the code
            matched = False
            for key in object_type_mapping:
                if key in code:
                    desc = object_type_mapping[key]
                    matched = True
                    break
            if not matched:
                desc = code  # Retain original code if not mapped
                if code != 'None':  # Don't print warning for None values
                    print(f"Warning: Object type code '{code}' not found in mapping.")
        descriptions.append(desc)
    return ', '.join(descriptions)
