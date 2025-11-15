"""
Convert HOT ocean pH data to JSON format
Manual converter for ocean acidification visualization
"""
import json
import csv
from datetime import datetime
from collections import defaultdict

def find_hot_data_file():
    """Find HOT data file - try multiple possible filenames"""
    import os
    
    # List of possible filenames (in order of preference)
    possible_files = [
        'data/3773_v3_niskin_hot001_yr01_to_hot348_yr35.csv',  # Current BCO-DMO filename
#        'hot_carbonate_data.txt',  # Legacy/manual download name
#        'hot_carbonate_data.csv',
    ]
    
    # Also check for any file matching the pattern
    for file in os.listdir('.'):
        if 'niskin' in file.lower() and 'hot' in file.lower() and file.endswith('.csv'):
            if file not in possible_files:
                possible_files.insert(0, file)
    
    # Find first existing file
    for filename in possible_files:
        if os.path.exists(filename):
            return filename
    
    return None

def parse_hot_ph_csv(filename):
    """
    Parse HOT carbonate chemistry CSV from BCO-DMO
    Format: CSV with ISO datetime and pH columns
    """
    print(f"Parsing {filename}...")
    
    monthly_data = defaultdict(list)  # (year, month) -> [ph_values]
    total_rows = 0
    ph_rows = 0
    surface_rows = 0
    
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            total_rows += 1
            
            # Get date
            date_str = row.get('Sampling_ISO_DateTime_UTC', '')
            if not date_str:
                continue
            
            # Parse ISO datetime: 2023-12-30T20:36Z
            try:
                dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
                year = dt.year
                month = dt.month
            except (ValueError, AttributeError):
                continue
            
            # Get pH value
            ph_str = row.get('pH', '').strip()
            if not ph_str:
                continue
            
            try:
                ph_value = float(ph_str)
            except ValueError:
                continue
            
            # Validate pH range
            if not (7.0 < ph_value < 9.0):
                continue
            
            ph_rows += 1
            
            # Get depth/pressure - prioritize surface measurements
            depth_str = row.get('CTDPRS', '').strip()
            
            # Filter for surface measurements (< 50 meters pressure/depth)
            # This gets the surface ocean pH we want
            try:
                if depth_str:
                    depth = float(depth_str)
                    if depth > 50:  # Skip deep measurements
                        continue
            except ValueError:
                pass  # If no depth, still include it
            
            surface_rows += 1
            
            # Add to monthly data
            key = (year, month)
            monthly_data[key].append(ph_value)
    
    print(f"  Total rows: {total_rows}")
    print(f"  Rows with pH: {ph_rows}")
    print(f"  Surface rows (< 50m): {surface_rows}")
    print(f"  Unique months: {len(monthly_data)}")
    
    # Calculate monthly averages
    records = []
    for (year, month), ph_values in sorted(monthly_data.items()):
        avg_ph = sum(ph_values) / len(ph_values)
        record = {
            'year': year,
            'month': month,
            'date': f"{year}-{month:02d}",
            'ph_total': round(avg_ph, 4),
            'num_measurements': len(ph_values),
            'source': 'HOT Station ALOHA'
        }
        records.append(record)
    
    print(f"\n✓ Created {len(records)} monthly average pH records")
    
    if records:
        print(f"  Date range: {records[0]['date']} to {records[-1]['date']}")
        print(f"  pH range: {min(r['ph_total'] for r in records):.4f} to {max(r['ph_total'] for r in records):.4f}")
    
    return records

def create_metadata(records):
    """Create metadata for the pH dataset"""
    if not records:
        return {}
    
    first = records[0]
    latest = records[-1]
    ph_change = latest['ph_total'] - first['ph_total']
    years_span = latest['year'] - first['year']
    
    return {
        'dataset_name': 'data/ocean_ph_hot_monthly',
        'description': 'Ocean surface pH measurements from Hawaii Ocean Time-series',
        'source': {
            'organization': 'BCO-DMO (Biological and Chemical Oceanography Data Management Office)',
            'data_source': 'Hawaii Ocean Time-series (HOT) Program',
            'station': 'Station ALOHA (22°45\'N, 158°W)',
            'url': 'https://www.bco-dmo.org/dataset/3773',
            'hot_program_url': 'https://hahana.soest.hawaii.edu/hot/',
            'citation': 'Hawaii Ocean Time-series (HOT), University of Hawaii. Data accessed via BCO-DMO dataset 3773.'
        },
        'parameters': {
            'measurement': 'pH (total scale)',
            'location': 'Surface ocean (< 50m depth)',
            'frequency': 'Monthly sampling',
            'method': 'Spectrophotometric',
            'aggregation': 'Monthly averages of surface measurements'
        },
        'time_range': {
            'start': first['date'],
            'end': latest['date'],
            'record_count': len(records)
        },
        'statistics': {
            'first_ph': first['ph_total'],
            'latest_ph': latest['ph_total'],
            'ph_change': round(ph_change, 4),
            'years_span': years_span,
            'annual_rate': round(ph_change / years_span, 6) if years_span > 0 else 0
        },
        'context': {
            'pre_industrial_ph': 8.2,
            'current_decline': 0.1,
            'threat': 'Ocean acidification threatens marine ecosystems',
            'impact': 'pH is logarithmic: 0.1 unit drop = 30% increase in acidity',
            'rate': 'Faster than any time in 300 million years'
        },
        'last_updated': datetime.now().isoformat(),
        'cache_file': 'data/ocean_ph_hot_monthly.json'
    }

def main():
    """Main conversion workflow"""
    print("=" * 70)
    print("  HOT Ocean pH Data Converter")
    print("  Converting carbonate chemistry data to JSON")
    print("=" * 70)
    print()
    
    # Find input file
    input_file = find_hot_data_file()
    
    if not input_file:
        print("❌ No HOT data file found!")
        print()
        print("Please download the data first:")
        print("1. Go to: https://www.bco-dmo.org/dataset/3773")
        print("2. Click the download button for the CSV file")
        print("3. Save it to this directory (any filename is fine)")
        print()
        print("Looking for files matching:")
        print("  - data/3773_v3_niskin_hot001_yr01_to_hot348_yr35.csv")
    #    print("  - hot_carbonate_data.txt")
    #    print("  - hot_carbonate_data.csv")
        print("  - Any file with 'niskin' and 'hot' in the name")
        return
    
    print(f"Found data file: {input_file}\n")
    
    # Parse the file
    records = parse_hot_ph_csv(input_file)
    
    if not records:
        print("\n❌ No valid pH records found!")
        print("Please check the file format.")
        return
    
    # Create output structure
    output = {
        'metadata': create_metadata(records),
        'records': records
    }
    
    # Save to JSON
    output_file = 'data/ocean_ph_hot_monthly.json'
    with open(output_file, 'w') as f:
        json.dump(output, f, indent=2)
    
    print(f"\n✓ Saved {len(records)} records to {output_file}")
    print()
    print(f"Latest ocean pH: {records[-1]['ph_total']:.4f} (from {records[-1]['num_measurements']} measurements)")
    print(f"{records[-1]['year'] - records[0]['year']}-year change: {records[-1]['ph_total'] - records[0]['ph_total']:+.4f} pH units")
    print()
    print("You can now run the visualization!")
    print("=" * 70)

if __name__ == '__main__':
    main()
