"""formatting_utils.py - Basic formatting utilities used by both palomas_orrery.py and visualization_utils.py."""

def format_maybe_float(value):
    """
    If 'value' is a numeric type (int or float), return it formatted
    with 10 decimal places. Otherwise, return 'N/A'.
    """
    if isinstance(value, (int, float)):
        return f"{value:.10f}"
    return "N/A"

def format_km_float(value):
    """
    Format kilometer values in scientific notation with 2 decimal places.
    """
    if isinstance(value, (int, float)):
        return f"{value:.10e}"  # using .10e for scientific notation instead of .10f
    return "N/A"