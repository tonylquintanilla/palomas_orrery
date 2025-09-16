import pickle
import numpy as np

# Check distance PKL
with open('star_properties_distance.pkl', 'rb') as f:
    data = pickle.load(f)

print(f"Data type: {type(data)}")
print(f"Keys in data: {data.keys() if isinstance(data, dict) else 'Not a dict'}")

if isinstance(data, dict):
    if 'unique_ids' in data:
        # List format
        print(f"Total unique IDs: {len(data['unique_ids'])}")
        
        if 'distance_ly' in data:
            distances = [d for d in data['distance_ly'] if d is not None and not np.isnan(d)]
            if distances:
                print(f"Distance range: {min(distances):.1f} to {max(distances):.1f} ly")
                within_100 = sum(1 for d in distances if d <= 100.1)
                print(f"Stars within 100.1 ly: {within_100}")
            else:
                print("No valid distances found")
    else:
        # Dictionary format (star_id -> properties)
        print(f"Total stars: {len(data)}")
        distances = []
        for star_id, props in data.items():
            if isinstance(props, dict) and 'distance_ly' in props:
                d = props['distance_ly']
                if d is not None and not np.isnan(d):
                    distances.append(d)
        
        if distances:
            print(f"Distance range: {min(distances):.1f} to {max(distances):.1f} ly")
            within_100 = sum(1 for d in distances if d <= 100.1)
            print(f"Stars within 100.1 ly: {within_100}")