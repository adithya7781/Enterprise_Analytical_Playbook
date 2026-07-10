import os
import pandas as pd

RAW_PATH = "../data/raw"
PROCESSED_PATH = "../data/processed"
OUTPUT_PATH = "../data/output"

os.makedirs(PROCESSED_PATH, exist_ok=True)
os.makedirs(OUTPUT_PATH, exist_ok=True)

tables = {
    "patient": "patient.csv",
    "admission": "admission.csv",
    "department": "department.csv",
    "billing": "billing.csv",
    "disease": "disease.csv"
}

dfs = {}

for name, file in tables.items():
    path = os.path.join(RAW_PATH, file)
    dfs[name] = pd.read_csv(path)

print("All tables have been loaded successfully.")

# ==============================
# CLEANING
# ==============================

for name, df in dfs.items():

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Standardize column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # Remove leading/trailing spaces
    object_columns = df.select_dtypes(include="object").columns

    for col in object_columns:
        df[col] = df[col].str.strip()

    dfs[name] = df

print("Cleaning completed.")

date_columns = {
    "patient": ["date_of_birth"],
    "admission": ["admission_date", "discharge_date"],
    "billing": ["bill_date"]
}

for table, columns in date_columns.items():

    for col in columns:

        dfs[table][col] = pd.to_datetime(
            dfs[table][col],
            errors="coerce"
        )

print("Date conversion completed.")

for name, df in dfs.items():

    df.to_csv(
        f"{PROCESSED_PATH}/{name}_clean.csv",
        index=False
    )

print("Processed files saved.")

hospital = dfs["patient"]

hospital = hospital.merge(
    dfs["admission"],
    on="patient_id",
    how="left"
)

hospital = hospital.merge(
    dfs["department"],
    on="department_id",
    how="left"
)

hospital = hospital.merge(
    dfs["billing"],
    on="admission_id",
    how="left"
)

hospital = hospital.merge(
    dfs["disease"],
    on="disease_id",
    how="left"
)

# Object columns
object_cols = hospital.select_dtypes(include="object").columns
hospital[object_cols] = hospital[object_cols].fillna("Unknown")

# Numeric columns
numeric_cols = hospital.select_dtypes(include=["int64", "float64"]).columns
hospital[numeric_cols] = hospital[numeric_cols].fillna(0)

# Datetime columns
date_cols = hospital.select_dtypes(include="datetime64[ns]").columns
hospital[date_cols] = hospital[date_cols].fillna(pd.NaT)

hospital.drop_duplicates(inplace=True)

hospital.to_csv(
    f"{OUTPUT_PATH}/hospital_master.csv",
    index=False
)

print("=" * 50)
print("ETL Completed Successfully")
print("=" * 50)
print(f"Rows : {hospital.shape[0]}")
print(f"Columns : {hospital.shape[1]}")