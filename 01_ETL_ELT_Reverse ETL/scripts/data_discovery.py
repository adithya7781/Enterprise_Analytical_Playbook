import os
import pandas as pd

RAW_DATA_PATH = "../data/raw"

print("=" * 80)
print(" HOSPITAL DATASET DISCOVERY ")
print("=" * 80)

csv_files = [f for f in os.listdir(RAW_DATA_PATH) if f.endswith(".csv")]

print(f"\nTotal CSV Files : {len(csv_files)}\n")

for file in sorted(csv_files):

    path = os.path.join(RAW_DATA_PATH, file)

    df = pd.read_csv(path)

    print("-" * 80)
    print(f"Table : {file}")

    print(f"Rows : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")

    print("\nColumns")

    for col in df.columns:
        print(f" - {col}")

    print("\nData Types")

    print(df.dtypes)

    print("\nMissing Values")

    print(df.isnull().sum())

    print("\nDuplicate Rows")

    print(df.duplicated().sum())

print("\nCompleted Data Discovery")