import json

records = []
with open('nasa_earthdata_sea_level_data.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('HDR') or 'Header_End' in line:
            continue
        
        try:
            parts = line.split()
            if len(parts) >= 3:
                year_decimal = float(parts[0])
                year = int(year_decimal)
                month = int((year_decimal - year) * 12) + 1
                
                records.append({
                    'year': year,
                    'month': month,
                    'year_decimal': year_decimal,
                    'gmsl_cm': float(parts[1]),
                    'gmsl_smoothed_cm': float(parts[2])
                })
        except ValueError:
            continue

data = {
    'data': records,
    'metadata': {
        'source': {
            'organization': 'NASA PO.DAAC',
            'url': 'https://podaac.jpl.nasa.gov/dataset/NASA_SSH_REF_SIMPLE_GRID_V1',
            'citation': 'NASA-SSH. 2025. Global Mean Sea Level'
        },
        'last_updated': '2025-10-13'
    }
}

with open('sea_level_gmsl_monthly.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Converted {len(records)} records to sea_level_gmsl_monthly.json")