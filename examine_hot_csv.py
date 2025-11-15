"""
Examine the HOT CSV file structure
"""
import csv

def examine_csv():
    filename = '3773_v3_niskin_hot001_yr01_to_hot348_yr35.csv'
    
    print("=" * 80)
    print(f"Examining: {filename}")
    print("=" * 80)
    
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        
        # Get header
        header = next(reader)
        
        print(f"\nTotal columns: {len(header)}")
        print("\n" + "=" * 80)
        print("ALL COLUMN NAMES:")
        print("=" * 80)
        for i, col in enumerate(header):
            print(f"{i:3d}: {col}")
        
        # Look for date and pH columns
        print("\n" + "=" * 80)
        print("COLUMNS CONTAINING 'date', 'year', 'month', or 'ph':")
        print("=" * 80)
        for i, col in enumerate(header):
            col_lower = col.lower()
            if any(keyword in col_lower for keyword in ['date', 'year', 'month', 'ph']):
                print(f"{i:3d}: {col}")
        
        # Show first 5 data rows
        print("\n" + "=" * 80)
        print("FIRST 5 DATA ROWS:")
        print("=" * 80)
        for row_num, row in enumerate(reader):
            if row_num >= 5:
                break
            print(f"\nRow {row_num + 1}:")
            # Show date column (index 4)
            if len(row) > 4:
                print(f"  Date (col 4): {row[4]}")
            # Show pH column (index 22)
            if len(row) > 22:
                print(f"  pH (col 22): {row[22]}")
            # Show first 10 columns
            print(f"  First 10 cols: {row[:10]}")

if __name__ == '__main__':
    examine_csv()
