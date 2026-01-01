import pandas as pd
import sys
import os


data = {
    'longitude': [-122.23, -122.22, -122.24, -122.25, -122.25],
    'latitude': [37.88, 37.86, 37.85, 37.85, 37.85],
    'housing_median_age': [41, 21, 52, 52, 52],
    'total_rooms': [880, 7099, 1467, 1627, 2366],
    'total_bedrooms': [129.0, 1106.0, 190.0, 280.0, 565.0],
    'population': [322.0, 2401.0, 496.0, 717.0, 2594.0],
    'households': [126.0, 1132.0, 177.0, 259.0, 1145.0],
    'median_income': [8.3252, 8.3014, 7.2574, 5.4339, 3.8462],
    'median_house_value': [452600.0, 358500.0, 352100.0, 341300.0, 342200.0]
}
df = pd.DataFrame(data)

output_file = sys.argv[1] if len(sys.argv) > 1 else 'test.csv'
df.to_csv(output_file, index=False)

print(f"Shape: {df.shape}")
print("\nColumns:", list(df.columns))
print("\nFirst 5 rows:")
print(df.round(2))
print("\nSummary:")
print(df.describe().round(2))
print(f"\nSaved {len(df)} rows to {output_file}")
