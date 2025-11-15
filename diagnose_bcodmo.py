"""
Diagnostic script to examine BCO-DMO pH data structure
"""
import requests

def examine_bcodmo_data():
    """Download and examine the structure of BCO-DMO pH data"""
    
    api_url = "https://www.bco-dmo.org/dataset/3773.csv"
    
    try:
        print("Downloading BCO-DMO data...")
        response = requests.get(api_url, timeout=30)
        response.raise_for_status()
        
        lines = response.text.split('\n')
        print(f"\n✓ Downloaded {len(lines)} lines\n")
        
        # Show first 20 lines to understand structure
        print("=" * 80)
        print("FIRST 20 LINES:")
        print("=" * 80)
        for i, line in enumerate(lines[:20]):
            print(f"{i:3d}: {line}")
        
        # Find the header line
        print("\n" + "=" * 80)
        print("LOOKING FOR HEADER:")
        print("=" * 80)
        
        for i, line in enumerate(lines[:50]):
            if 'ph' in line.lower() or 'date' in line.lower() or 'year' in line.lower():
                print(f"Line {i}: {line}")
        
        # Check for common delimiters
        print("\n" + "=" * 80)
        print("DELIMITER ANALYSIS:")
        print("=" * 80)
        
        sample_line = None
        for line in lines:
            if line.strip() and not line.startswith('#') and not line.startswith('!'):
                sample_line = line
                break
        
        if sample_line:
            print(f"Sample data line: {sample_line[:100]}...")
            print(f"Commas: {sample_line.count(',')}")
            print(f"Tabs: {sample_line.count(chr(9))}")
            print(f"Pipes: {sample_line.count('|')}")
            print(f"Semicolons: {sample_line.count(';')}")
        
        # Try to find actual data lines with pH values
        print("\n" + "=" * 80)
        print("SEARCHING FOR pH VALUES (7.0-9.0):")
        print("=" * 80)
        
        count = 0
        for i, line in enumerate(lines):
            if count >= 5:
                break
            parts = line.replace('\t', ',').split(',')
            for part in parts:
                try:
                    val = float(part.strip())
                    if 7.0 < val < 9.0:
                        print(f"Line {i}: {line[:150]}")
                        count += 1
                        break
                except ValueError:
                    continue
        
        return lines
        
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    examine_bcodmo_data()
